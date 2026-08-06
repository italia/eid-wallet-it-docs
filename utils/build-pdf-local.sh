#!/usr/bin/env bash
# Build PDFs locally (same steps as .github/workflows/build-pdf.yml).
#
# Requirements (same as CI; includes cmap, fontspec, Latin Modern fonts):
#   - Python venv: source env/bin/activate && pip install -r requirements-dev.txt
#   - TeX Live (Debian/Ubuntu, same as .github/workflows/build-pdf.yml):
#     sudo apt-get update && sudo apt-get install -y texlive-latex-extra texlive-fonts-recommended texlive-luatex
#     sudo apt-get install -y texlive-latex-recommended texlive-fonts-extra \
#       texlive-lang-italian texlive-lang-english texlive-pictures texlive-font-utils
#
# Usage: from repo root, with env activated:
#   ./utils/build-pdf-local.sh
#
# Optional override:
#   PDF_RELEASE_DATE=2026-07-03 ./utils/build-pdf-local.sh
# Otherwise the date is resolved from the current git tag or the build date.

set -e
ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT_DIR"

# Ensure a valid UTF-8 locale for Sphinx/Python inside slim Docker images
export LANG="${LANG:-C.UTF-8}"
export LC_ALL="${LC_ALL:-C.UTF-8}"

if [[ -n "${PDF_RELEASE_DATE:-}" ]]; then
  echo "Using PDF release date override: ${PDF_RELEASE_DATE}"
fi

if ! command -v lualatex &>/dev/null; then
  echo "Error: lualatex not found. Install TeX Live, e.g.:"
  echo "  sudo apt-get install -y texlive-latex-recommended texlive-luatex texlive-latex-extra texlive-fonts-recommended texlive-fonts-extra"
  exit 1
fi
if ! kpsewhich fontspec.sty &>/dev/null; then
  echo "Error: fontspec.sty not found (needed for LuaLaTeX). Install TeX packages:"
  echo "  sudo apt-get update && sudo apt-get install -y texlive-latex-extra texlive-fonts-recommended texlive-luatex"
  exit 1
fi

mkdir -p pdf_output
TIMESTAMP=$(date +%Y%m%d-%H%M%S)

for LANG in en it; do
  ULANG=${LANG^^}
  echo "=== Sphinx LaTeX (${ULANG}) ==="
  sphinx-build -b latex "$ROOT_DIR/docs/${LANG}/" "$ROOT_DIR/build/latex/${LANG}"

  # Normalize copied PDFs to 1.5 so LuaLaTeX can include them
  if command -v gs &>/dev/null; then
    for f in "$ROOT_DIR/build/latex/${LANG}/images/pdf/"*.pdf; do
      [ -f "$f" ] || continue
      out="${f%.pdf}-t.pdf"
      gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.5 -dNOPAUSE -dQUIET -dBATCH -sOutputFile="$out" "$f" 2>/dev/null
      [ -f "$out" ] && mv "$out" "$f"
      rm -f "$out"
    done
  fi

  # Prefer the main Sphinx document (settings_file_name.tex); ignore leftovers
  # such as *-titleonly.tex that may still be present in the build directory.
  TEX_FILE="$ROOT_DIR/build/latex/${LANG}/eid-wallet-it-docs.tex"
  if [[ ! -f "$TEX_FILE" ]]; then
    TEX_FILE=$(find "$ROOT_DIR/build/latex/${LANG}" -maxdepth 1 -type f -name '*.tex' ! -name '*-titleonly.tex' | head -n 1)
  fi
  if [[ -z "$TEX_FILE" || ! -f "$TEX_FILE" ]]; then
    echo "Error: no .tex file found for ${ULANG} build in build/latex/${LANG}"
    exit 1
  fi
  echo "Using TeX file: $(basename "$TEX_FILE")"

  sed -i '/\\documentclass.*sphinxmanual/a \\\\pdfminorversion=7' "$TEX_FILE"

  BASENAME=$(basename "$TEX_FILE" .tex)

  echo "=== LuaLaTeX ${ULANG} (3 passes) ==="
  PWD_BEFORE=$(pwd)
  cd "$ROOT_DIR/build/latex/${LANG}"
  for i in 1 2 3; do
    echo "--- Pass $i ---"
    rc=0
    lualatex -interaction=nonstopmode -file-line-error "${BASENAME}.tex" || rc=$?
    # LuaLaTeX may return non-zero on the first pass due to unresolved refs
    # while still producing usable aux/pdf artifacts for subsequent passes.
    if [[ $rc -ne 0 ]]; then
      echo "Warning: LuaLaTeX returned ${rc} on ${ULANG} pass ${i}; continuing"
    fi
    makeindex -s python.ist "${BASENAME}.idx" 2>/dev/null || true
  done
  if [[ ! -f "${BASENAME}.pdf" ]]; then
    echo "Error: ${ULANG} PDF not generated. Check lualatex output above."
    cd "$PWD_BEFORE"
    exit 1
  fi

  # Post-build compression: downsample embedded bitmaps (typically 35MB → ~16MB).
  # Override with PDF_COMPRESS_SETTINGS=/screen for smaller files (~13MB).
  if command -v gs &>/dev/null; then
    PDF_COMPRESS_SETTINGS="${PDF_COMPRESS_SETTINGS:-/printer}"
    echo "=== Compressing ${ULANG} PDF (Ghostscript ${PDF_COMPRESS_SETTINGS}) ==="
    before_bytes=$(wc -c < "${BASENAME}.pdf")
    rm -f "${BASENAME}-opt.pdf"
    if ! gs -sDEVICE=pdfwrite \
        -dCompatibilityLevel=1.7 \
        -dPDFSETTINGS="${PDF_COMPRESS_SETTINGS}" \
        -dDetectDuplicateImages=true \
        -dCompressFonts=true \
        -dNOPAUSE -dQUIET -dBATCH \
        -sOutputFile="${BASENAME}-opt.pdf" "${BASENAME}.pdf"; then
      echo "Warning: Ghostscript error for ${ULANG}; keeping uncompressed PDF"
      rm -f "${BASENAME}-opt.pdf"
    else
      after_bytes=$(wc -c < "${BASENAME}-opt.pdf" 2>/dev/null || echo 0)
      pages_before=$(pdfinfo "${BASENAME}.pdf"     2>/dev/null | awk '/^Pages:/{print $2}')
      pages_after=$( pdfinfo "${BASENAME}-opt.pdf" 2>/dev/null | awk '/^Pages:/{print $2}')
      if [[ "${after_bytes}" -lt 10000 || "${after_bytes}" -ge "${before_bytes}" ]]; then
        echo "Warning: suspicious output for ${ULANG} (${after_bytes}B vs ${before_bytes}B); keeping original"
        rm -f "${BASENAME}-opt.pdf"
      elif [[ -n "${pages_before}" && "${pages_before}" != "${pages_after}" ]]; then
        echo "Warning: page count changed for ${ULANG} (${pages_after:-?} != ${pages_before}); keeping original"
        rm -f "${BASENAME}-opt.pdf"
      else
        mv "${BASENAME}-opt.pdf" "${BASENAME}.pdf"
        echo "Compressed ${ULANG}: $((before_bytes / 1024 / 1024))MB → $((after_bytes / 1024 / 1024))MB"
      fi
    fi
  else
    echo "Warning: gs not found; skipping post-build PDF compression for ${ULANG}"
  fi

  cd "$PWD_BEFORE"

  cp "$ROOT_DIR/build/latex/${LANG}/${BASENAME}.pdf" "$ROOT_DIR/pdf_output/${BASENAME}-${LANG}-${TIMESTAMP}.pdf"
done

echo "Done. PDFs in pdf_output/"
ls -la "$ROOT_DIR"/pdf_output/*.pdf

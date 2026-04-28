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

set -e
cd "$(dirname "$0")/.."

# Ensure a valid UTF-8 locale for Sphinx/Python inside slim Docker images
export LANG="${LANG:-C.UTF-8}"
export LC_ALL="${LC_ALL:-C.UTF-8}"

# Prepare temporary edits to document titles, similar to .github/workflows/build-pdf.yml
IT_CONF="docs/it/conf.py"
EN_CONF="docs/en/conf.py"
IT_CONF_BAK="$(mktemp)"
EN_CONF_BAK="$(mktemp)"
cp "$IT_CONF" "$IT_CONF_BAK"
cp "$EN_CONF" "$EN_CONF_BAK"

trap 'cp "$IT_CONF_BAK" "$IT_CONF"; cp "$EN_CONF_BAK" "$EN_CONF"' EXIT

# Determine tag:
# - If PDF_BUILD_TAG is set, use that (manual override)
# - Otherwise, if HEAD is exactly at a tag, use that
# - Otherwise use "current version" labels
TAG="${PDF_BUILD_TAG:-}"
if [[ -z "$TAG" ]] && git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  TAG="$(git describe --tags --exact-match HEAD 2>/dev/null || true)"
fi

if [[ -n "$TAG" ]]; then
  # Use Python to robustly normalize titles to "<base> - Release <TAG>" for both languages
  python - <<PY
from pathlib import Path

tag = "${TAG}"
for conf_path in [Path("$IT_CONF"), Path("$EN_CONF")]:
    text = conf_path.read_text(encoding="utf-8")
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.strip().startswith("settings_project_name"):
            # Extract base before the first " - "
            before_eq, _, value = line.partition("=")
            value_str = value.strip().strip('"')
            base = value_str.split(" - ", 1)[0]
            lines[i] = f'{before_eq}= "{base} - Release {tag}"'
            break
    conf_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
print(f"Applied release tag '{tag}' to document titles (local build)")
PY
else
  sed -i 's/\(settings_project_name = ".*\)"/\1 - Versione Corrente"/' "$IT_CONF"
  sed -i 's/\(settings_project_name = ".*\)"/\1 - Editor'"'"'s Copy"/' "$EN_CONF"
  echo "Applied editor/default titles for local build"
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
  sphinx-build -b latex "docs/${LANG}/" "build/latex/${LANG}"

  # Normalize copied PDFs to 1.5 so LuaLaTeX can include them
  if command -v gs &>/dev/null; then
    for f in "build/latex/${LANG}/images/pdf/"*.pdf; do
      [ -f "$f" ] || continue
      out="${f%.pdf}-t.pdf"
      gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.5 -dNOPAUSE -dQUIET -dBATCH -sOutputFile="$out" "$f" 2>/dev/null
      [ -f "$out" ] && mv "$out" "$f"
      rm -f "$out"
    done
  fi

  TEX_FILE=$(find "build/latex/${LANG}" -maxdepth 1 -type f -name '*.tex' | head -n 1)
  if [[ -z "$TEX_FILE" ]]; then
    echo "Error: no .tex file found for ${ULANG} build in build/latex/${LANG}"
    exit 1
  fi

  sed -i '/\\documentclass.*sphinxmanual/a \\\\pdfminorversion=7' "$TEX_FILE"

  BASENAME=$(basename "$TEX_FILE" .tex)

  echo "=== LuaLaTeX ${ULANG} (3 passes) ==="
  PWD_BEFORE=$(pwd)
  cd "build/latex/${LANG}"
  for i in 1 2 3; do
    echo "--- Pass $i ---"
    lualatex -interaction=nonstopmode -file-line-error "${BASENAME}.tex"
    makeindex -s python.ist "${BASENAME}.idx" 2>/dev/null || true
  done
  if [[ ! -f "${BASENAME}.pdf" ]]; then
    echo "Error: ${ULANG} PDF not generated. Check lualatex output above."
    cd "$PWD_BEFORE"
    exit 1
  fi
  cd "$PWD_BEFORE"

  cp "build/latex/${LANG}/${BASENAME}.pdf" "pdf_output/${BASENAME}-${LANG}-${TIMESTAMP}.pdf"
done

echo "Done. PDFs in pdf_output/"
ls -la pdf_output/*.pdf

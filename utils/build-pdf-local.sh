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
SETTINGS_FILE_NAME="${SETTINGS_FILE_NAME:-eid-wallet-it-docs}"

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

echo "=== Sphinx LaTeX (EN) ==="
sphinx-build -b latex docs/en/ build/latex/en
# Normalize copied PDFs to 1.5 so LuaLaTeX can include them
if command -v gs &>/dev/null; then
  for f in build/latex/en/images/pdf/*.pdf; do
    [ -f "$f" ] || continue
    out="${f%.pdf}-t.pdf"
    gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.5 -dNOPAUSE -dQUIET -dBATCH -sOutputFile="$out" "$f" 2>/dev/null; [ -f "$out" ] && mv "$out" "$f"; rm -f "$out"
  done
fi
sed -i '/\\documentclass.*sphinxmanual/a \\\\pdfminorversion=7' build/latex/en/eid-wallet-it-docs.tex

echo "=== LuaLaTeX EN (3 passes) ==="
cd build/latex/en
for i in 1 2 3; do
  echo "--- Pass $i ---"
  lualatex -interaction=nonstopmode -file-line-error "$SETTINGS_FILE_NAME.tex"
  makeindex -s python.ist "$SETTINGS_FILE_NAME.idx" 2>/dev/null || true
done
if [[ ! -f "$SETTINGS_FILE_NAME.pdf" ]]; then
  echo "Error: English PDF not generated. Check lualatex output above."
  exit 1
fi
cd "$OLDPWD"

echo "=== Sphinx LaTeX (IT) ==="
sphinx-build -b latex docs/it/ build/latex/it
if command -v gs &>/dev/null; then
  for f in build/latex/it/images/pdf/*.pdf; do
    [ -f "$f" ] || continue
    out="${f%.pdf}-t.pdf"
    gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.5 -dNOPAUSE -dQUIET -dBATCH -sOutputFile="$out" "$f" 2>/dev/null; [ -f "$out" ] && mv "$out" "$f"; rm -f "$out"
  done
fi
sed -i '/\\documentclass.*sphinxmanual/a \\\\pdfminorversion=7' build/latex/it/eid-wallet-it-docs.tex

echo "=== LuaLaTeX IT (3 passes) ==="
cd build/latex/it
for i in 1 2 3; do
  echo "--- Pass $i ---"
  lualatex -interaction=nonstopmode -file-line-error "$SETTINGS_FILE_NAME.tex"
  makeindex -s python.ist "$SETTINGS_FILE_NAME.idx" 2>/dev/null || true
done
if [[ ! -f "$SETTINGS_FILE_NAME.pdf" ]]; then
  echo "Error: Italian PDF not generated."
  exit 1
fi
cd "$OLDPWD"

mkdir -p pdf_output
TIMESTAMP=$(date +%Y%m%d-%H%M%S)
cp build/latex/it/$SETTINGS_FILE_NAME.pdf pdf_output/$SETTINGS_FILE_NAME-it-${TIMESTAMP}.pdf
cp build/latex/en/$SETTINGS_FILE_NAME.pdf pdf_output/$SETTINGS_FILE_NAME-en-${TIMESTAMP}.pdf
echo "Done. PDFs in pdf_output/"
ls -la pdf_output/*.pdf

#!/bin/bash

# Convert PDFs to version 1.5 in the given directories (in-place).
# Usage:
#   convert_pdf_to_1_5.sh DIR [DIR ...]
#
# Uses Ghostscript (gs) with -dCompatibilityLevel=1.5.

set -euo pipefail

if [ "$#" -lt 1 ] ; then
  echo "Usage: $0 DIR [DIR ...]" >&2
  exit 1
fi

if ! command -v gs >/dev/null 2>&1 ; then
  echo "Error: Ghostscript (gs) is required but not installed." >&2
  exit 1
fi

for dir in "$@"; do
  if [ ! -d "$dir" ]; then
    echo "Skipping missing directory: $dir"
    continue
  fi

  echo "Processing directory: $dir"

  shopt -s nullglob
  for in_pdf in "$dir"/*.pdf; do
    [ -f "$in_pdf" ] || continue

    tmp_out="${in_pdf%.pdf}.tmp_1_5.pdf"

    echo "  Converting: $in_pdf"
    gs -sDEVICE=pdfwrite \
       -dCompatibilityLevel=1.5 \
       -dNOPAUSE -dBATCH -dSAFER \
       -sOutputFile="$tmp_out" \
       "$in_pdf"

    mv "$tmp_out" "$in_pdf"
  done
  shopt -u nullglob
done

echo "Conversion to PDF 1.5 completed."


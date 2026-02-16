#!/bin/bash

# Convert PDFs to version 1.5 in the given directories (in-place).
# Usage:
#   convert_pdf_to_1_5.sh DIR [DIR ...]
#
# Uses Ghostscript (gs) with -dCompatibilityLevel=1.5.
# Simulates a PDF→PostScript print pass to flatten any layers, optional content,
# or extensions before conversion.

set -euo pipefail

if [ "$#" -lt 1 ] ; then
  echo "Usage: $0 DIR [DIR ...]" >&2
  exit 1
fi

if ! command -v gs >/dev/null 2>&1 ; then
  echo "Error: Ghostscript (gs) is required but not installed." >&2
  exit 1
fi

format_size() {
  local n=$1
  if [ "$n" -ge 1048576 ]; then
    echo "$(( n / 1048576 ))M"
  elif [ "$n" -ge 1024 ]; then
    echo "$(( n / 1024 ))K"
  else
    echo "${n}B"
  fi
}

for dir in "$@"; do
  if [ ! -d "$dir" ]; then
    echo "Skipping missing directory: $dir"
    continue
  fi

  echo "Processing directory: $dir"

  shopt -s nullglob
  for in_pdf in "$dir"/*.pdf; do
    [ -f "$in_pdf" ] || continue

    base="${in_pdf%.pdf}"
    tmp_ps="${base}.tmp_print.ps"
    tmp_out="${base}.tmp_1_5.pdf"

    size_before=$(stat -c%s "$in_pdf")
    # Step 1: Print to PS (single file) to flatten layers, optional content, extensions
    gs -sDEVICE=ps2write \
       -dNOPAUSE -dBATCH -dQUIET -dSAFER \
       -sOutputFile="$tmp_ps" \
       "$in_pdf"
    # Step 2: PS → PDF 1.5
    gs -sDEVICE=pdfwrite \
       -dCompatibilityLevel=1.5 -dNOPAUSE -dBATCH -dQUIET -dSAFER \
       -sOutputFile="$tmp_out" \
       "$tmp_ps"
    rm -f "$tmp_ps"
    mv "$tmp_out" "$in_pdf"
    size_after=$(stat -c%s "$in_pdf")
    echo "  Converting: $in_pdf ($(format_size "$size_before") -> $(format_size "$size_after"))"
  done
  shopt -u nullglob
done

echo "Conversion to PDF 1.5 completed."


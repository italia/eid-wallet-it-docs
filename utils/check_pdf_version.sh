#!/bin/bash

# Check that all PDFs in the given directories have the required PDF version.
# Usage:
#   check_pdf_version.sh 1.5 docs/en/images/pdf docs/it/images/pdf

set -euo pipefail

if [ "$#" -lt 2 ]; then
  echo "Usage: $0 REQUIRED_VERSION DIR [DIR ...]" >&2
  exit 1
fi

REQUIRED="$1"
shift

FAIL=0

for dir in "$@"; do
  if [ ! -d "$dir" ]; then
    continue
  fi
  for f in "$dir"/*.pdf; do
    [ -f "$f" ] || continue
    VER=$(pdfinfo "$f" 2>/dev/null | sed -n 's/^PDF version:[[:space:]]*\([0-9.]*\).*/\1/p')
    if [ -z "$VER" ]; then
      echo "Failed: $f (could not read PDF version, file may be corrupt or invalid)"
      echo "::error file=$f::Could not read PDF version (file may be corrupt or invalid)"
      FAIL=1
    elif [ "$VER" != "$REQUIRED" ]; then
      echo "Failed: $f (version: $VER, required: $REQUIRED)"
      echo "::error file=$f::PDF version is $VER (required: $REQUIRED)"
      FAIL=1
    fi
  done
done

if [ "$FAIL" -ne 0 ]; then
  echo "One or more PDFs are not version $REQUIRED. LuaLaTeX inclusion requires 1.5; use gs to convert: gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.5 -dNOPAUSE -dBATCH -sOutputFile=out.pdf in.pdf"
  exit 1
fi

echo "All PDFs are version $REQUIRED."


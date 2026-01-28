#!/bin/bash

# Use the current working directory as the project root
ROOT="$(pwd)"
DOCS="$ROOT/docs"

found_count=0
not_found_count=0

# Function to check if a reference is in a figure block with :target: plantuml
check_plantuml_target() {
  local file="$1"
  local line="$2"
  # Use a configurable window of lines around the reference line.
  # FIGURE_CONTEXT_LINES allows changing the window size without modifying the script.
  local context="${FIGURE_CONTEXT_LINES:-10}"
  local start_line=$((line - context))
  local end_line=$((line + context))
  
  if [ "$start_line" -lt 1 ]; then
    start_line=1
  fi
  
  # Avoid going past the end of the file
  local max_line
  max_line=$(wc -l < "$file")
  if [ "$end_line" -gt "$max_line" ]; then
    end_line="$max_line"
  fi
  
  # Read the context around the line
  sed -n "${start_line},${end_line}p" "$file" | grep -qi ':target:.*plantuml'
  return $?
}

while IFS=$'\t' read -r fileline ref; do
  file="${fileline%%:*}"
  line="${fileline##*:}"
  
  # Skip if the reference directly contains http or plantuml
  if echo "$ref" | grep -qiE '(http|plantuml)'; then
    continue
  fi
  
  # Check if it is in a figure block with :target: plantuml
  if check_plantuml_target "$file" "$line"; then
    continue
  fi
  
  rst="$(basename "$file")"
  file_dir="$(dirname "$file")"

  # Resolve the exact path specified in the RST file
  resolved_ref="$ref"
  # Strip optional leading '<' and trailing '>' (e.g. RST links like `<_static/foo.svg>`)
  resolved_ref="${resolved_ref#<}"
  resolved_ref="${resolved_ref%>}"
  # Remove leading ./ if present
  if [[ "$resolved_ref" == ./* ]]; then
    resolved_ref="${resolved_ref#./}"
  fi
  # Resolve relative path from RST file directory
  if [[ "$resolved_ref" != /* ]]; then
    resolved_path="$file_dir/$resolved_ref"
  else
    resolved_path="$resolved_ref"
  fi

  # Special handling for Sphinx _static assets referenced from RST.
  # RST files may use `_static/foo.svg`, but during the Sphinx build these
  # are actually collected from various static source folders (e.g. docs/**/images/**, official_resources/, etc.).
  # To avoid false negatives, when a reference is under `_static/` we try to
  # resolve it against a set of known static asset roots and consider it valid
  # if it exists in at least one of them.
  if [[ "$resolved_ref" == _static/* || "$resolved_ref" == ./_static/* ]]; then
    # Strip leading ./ if still present
    clean_ref="${resolved_ref#./}"
    filename="${clean_ref#_static/}"

    static_found=false
    # Known static roots used to feed the Sphinx build / GitHub Pages:
    # - docs/en/images/svg: original EN SVG assets
    # - docs/it/images/svg: original IT SVG assets
    # - official_resources: shared official SVG assets (including Authentication Button, Trustmarks, etc.)
    for static_root in \
      "$DOCS/en/images/svg" \
      "$DOCS/it/images/svg" \
      "$ROOT/official_resources"
    do
      candidate="$static_root/$filename"
      if [ -e "$candidate" ]; then
        static_found=true
        resolved_path="$candidate"
        break
      fi
    done

    if "$static_found"; then
      ((found_count++))
      continue
    fi
    # Fall through to generic NOT-FOUND reporting below if none of the candidates exist.
  fi

  # Generic check: use the resolved path from the RST file location
  if [ -e "$resolved_path" ]; then
    ((found_count++))
  else
    printf 'NOT-FOUND: %s:%s -> %s\n' "$rst" "$line" "$resolved_path"
    ((not_found_count++))
  fi
done < <(
  grep -r --include='*.rst' --exclude-dir=.git -nH -E '\.(svg|pdf)' "$DOCS" \
    | grep -vi 'http' \
    | awk -F: '
      {
        file=$1; line=$2; text="";
        for (i=3; i<=NF; i++) { if (i>3) text=text ":"; text=text $i }
        while (match(text, /[[:graph:]]+\.(svg|pdf)/)) {
          ref=substr(text, RSTART, RLENGTH);
          print file ":" line "\t" ref;
          text=substr(text, RSTART+RLENGTH);
        }
      }
    '
)

printf '\nSummary:\n'
printf '  Found: %d\n' "$found_count"
printf '  Not found: %d\n' "$not_found_count"

if [ "$not_found_count" -gt 0 ]; then
  exit 1
fi

exit 0

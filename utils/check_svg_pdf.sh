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
  name="$(basename "$ref")"

  # Clear any previous value of full and search for an exact match by basename
  full=""
  found=0
  for lang in it en; do
    for kind in svg pdf; do
      full_try="$DOCS/$lang/$kind/$name"
      if [ -e "$full_try" ]; then
        found=1
        full="$full_try"
        break 2
      fi
    done
  done

  if [ "$found" -eq 0 ]; then
    rel="${file#"$DOCS"/}"
    lang="${rel%%/*}"
    ext="${name##*.}"
    not_found_path="$DOCS/$lang/images/$ext/$name"
    if [ -e "$not_found_path" ]; then
      ((found_count++))
    else
      printf 'NOT-FOUND: %s:%s -> %s\n' "$rst" "$line" "$not_found_path"
      ((not_found_count++))
    fi
  else
    ((found_count++))
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

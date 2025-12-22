#!/bin/bash

# Usa la directory corrente come root del progetto
ROOT="$(pwd)"
DOCS="$ROOT/docs"

found_count=0
not_found_count=0

# Funzione per controllare se un riferimento è in un blocco figure con :target: plantuml
check_plantuml_target() {
  local file="$1"
  local line="$2"
  local start_line=$((line - 10))
  local end_line=$((line + 10))
  
  if [ "$start_line" -lt 1 ]; then
    start_line=1
  fi
  
  # Leggi il contesto intorno alla riga
  sed -n "${start_line},${end_line}p" "$file" | grep -qi ':target:.*plantuml'
  return $?
}

while IFS=$'\t' read -r fileline ref; do
  file="${fileline%%:*}"
  line="${fileline##*:}"
  
  # Salta se la riga contiene http o plantuml direttamente
  if echo "$ref" | grep -qiE '(http|plantuml)'; then
    continue
  fi
  
  # Controlla se è in un blocco figure con :target: plantuml
  if check_plantuml_target "$file" "$line"; then
    continue
  fi
  
  rst="$(basename "$file")"
  name="$(basename "$ref")"

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
    full="$DOCS/$lang/images/$ext/$name"
    if [ -e "$full" ]; then
      ((found_count++))
    else
      printf 'NOT-FOUND: %s:%s -> %s\n' "$rst" "$line" "$full"
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

printf '\nConteggio:\n'
printf '  Trovati: %d\n' "$found_count"
printf '  Non trovati: %d\n' "$not_found_count"

if [ "$not_found_count" -gt 0 ]; then
  exit 1
fi

exit 0

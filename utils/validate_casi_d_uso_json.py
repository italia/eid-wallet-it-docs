#!/usr/bin/env python3
"""
Valida il file JSON dei Casi d'uso EAA contro lo JSON Schema.
Uso: python validate_casi_d_uso_json.py <percorso_file.json>
"""
import json
import sys
from pathlib import Path

try:
    import jsonschema
except ImportError:
    print("Errore: installare jsonschema (pip install jsonschema)")
    sys.exit(2)


def main():
    if len(sys.argv) < 2:
        print("Uso: python validate_casi_d_uso_json.py <file.json>")
        sys.exit(1)

    json_path = Path(sys.argv[1])
    base_dir = Path(__file__).parent.parent / "handbooks/it/authentic-sources"
    schema_path = base_dir / "json-schemas" / "schema-validazione-form-onboarding-fonte-autentica.schema.json"

    if not json_path.exists():
        print(f"Errore: file non trovato: {json_path}")
        sys.exit(1)

    if not schema_path.exists():
        print(f"Errore: schema non trovato: {schema_path}")
        sys.exit(1)

    try:
        with open(json_path, encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"ERRORE: Il file JSON non è valido.\n{e}")
        sys.exit(1)

    try:
        with open(schema_path, encoding="utf-8") as f:
            schema = json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        print(f"Errore schema: {e}")
        sys.exit(1)

    try:
        jsonschema.validate(data, schema)
        print("OK: Il file JSON è valido e conforme allo schema.")
        sys.exit(0)
    except jsonschema.ValidationError as e:
        print(f"ERRORE di validazione:\n{e}")
        if e.path:
            print(f"Percorso: {' → '.join(str(p) for p in e.path)}")
        sys.exit(1)


if __name__ == "__main__":
    main()

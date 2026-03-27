# Validazione di progettazione-caratteristiche-eaa.json contro lo JSON Schema.
# Obiettivo predefinito: `make` esegue la validazione (equivalente a `make validate`).
# Usa $(ROOT)/env/bin/python se esiste, altrimenti python3/python nel PATH.

ROOT := $(abspath $(dir $(lastword $(MAKEFILE_LIST)))/../../..)
VENV_PY := $(ROOT)/env/bin/python
PY := $(if $(wildcard $(VENV_PY)),$(VENV_PY),$(shell command -v python3 2>/dev/null || command -v python 2>/dev/null))
SCRIPT := $(ROOT)/utils/validate_casi_d_uso_json.py
JSON ?= $(abspath $(dir $(lastword $(MAKEFILE_LIST)))/progettazione-caratteristiche-eaa.json)

.DEFAULT_GOAL := validate

.PHONY: validate help

help:
	@echo "make / make validate  — valida $(JSON)"
	@echo "  override: make JSON=percorso/altro-file.json"
	@echo "Python: $(PY)"

validate:
	@test -n "$(PY)" || (echo "Errore: $(VENV_PY) non trovato e né python3/python in PATH"; exit 1)
	@"$(PY)" -c "import jsonschema" 2>/dev/null || (echo "Errore: modulo jsonschema non disponibile per $(PY)"; exit 1)
	@test -f "$(SCRIPT)" || (echo "Errore: script non trovato: $(SCRIPT)"; exit 1)
	@cd "$(ROOT)" && "$(PY)" "$(SCRIPT)" "$(JSON)"

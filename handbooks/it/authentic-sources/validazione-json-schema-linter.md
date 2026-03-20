# Validazione JSON Schema e Linter – Casi d'uso EAA

Questo documento illustra le modalità di validazione e controllo qualità dei file JSON relativi alla compilazione del template Fonte Autentica (casi d'uso, assistenza, e_service).

## Riferimenti

- **Schema JSON**: `handbooks/it/authentic-sources/json-schemas/schema-validazione-form-onboarding-fonte-autentica.schema.json` (JSON Schema draft 2020-12)
- **Template completo Fonte Autentica**: `handbooks/it/authentic-sources/progettazione-caratteristiche-eaa.json`
- **Validatore Python**: `utils/validate_casi_d_uso_json.py`

---

## 1. Validazione con JSON Schema

La validazione JSON Schema verifica che il file rispetti la struttura e i vincoli definiti nello schema (tipi, campi obbligatori, esattamente una sezione casi d'uso compilata, ecc.).

### Metodo consigliato: script Python (jsonschema)

```bash
# Dalla root del repository
pip install jsonschema
python utils/validate_casi_d_uso_json.py handbooks/it/authentic-sources/tuo-file-compilato.json
```

**Esito positivo**:
```
OK: Il file JSON è valido e conforme allo schema.
```

**Esito negativo**: il messaggio indica il percorso dell'errore e il motivo del fallimento (es. campo mancante, tipo errato, vincolo violato).

### Metodo alternativo: AJV (Node.js)

```bash
npm install -g ajv-cli
ajv validate -s handbooks/it/authentic-sources/json-schemas/schema-validazione-form-onboarding-fonte-autentica.schema.json -d "handbooks/it/authentic-sources/tuo-file-compilato.json" --spec=draft2020
```

---

## 2. JSON Linter (controllo sintattico)

Il linter verifica la correttezza sintattica del JSON (virgole, virgolette, parentesi, codifica caratteri).

### Editor (VS Code / Cursor)

L'estensione **JSON Language Support** evidenzia errori in tempo reale durante la modifica del file.

### Da riga di comando

```bash
python -c "import json; json.load(open('handbooks/it/authentic-sources/tuo-file.json'))"
```

In caso di errore sintattico, Python segnalerà la riga e la posizione.

### Online

[JSONLint](https://jsonlint.com/) — incolla il contenuto e verifica la sintassi.

---

## 3. Workflow consigliato

1. **Compilazione** del template `progettazione-caratteristiche-eaa.json`
2. **Validazione sintattica** (JSON Linter) — es. `python -c "import json; json.load(open('file.json'))"`
3. **Validazione strutturale** (JSON Schema) — es. `python utils/validate_casi_d_uso_json.py file.json`
4. **Checklist pre-sottomissione**:
   - [ ] Validazione JSON Schema superata
   - [ ] JSON Linter senza errori
   - [ ] Tutti i campi obbligatori (`risposta`) compilati per la sezione scelta
   - [ ] File rinominato correttamente (es. `Compilazione-EAA_[Ente]_[EAA].json`)

---

## 4. Versionamento dello schema

Lo schema adotta **Semantic Versioning** (es. `1.0.0`). Il campo `version` nella radice dello schema indica la versione corrente:

- **MAJOR** (es. 2.0.0): modifiche incompatibili (campi rimossi, tipi cambiati)
- **MINOR** (es. 1.1.0): nuove proprietà opzionali, estensioni retrocompatibili
- **PATCH** (es. 1.0.1): correzioni, descrizioni, senza impatto sulla validazione

I file compilati fanno riferimento allo schema tramite `$schema`; in caso di aggiornamento dello schema, verificare la compatibilità con le versioni precedenti dei file già compilati.

---

## 5. Note sullo schema `json-schemas/schema-validazione-form-onboarding-fonte-autentica.schema.json`

- Lo schema valida l'intera struttura del file, incluse le sezioni **casi d'uso**, **assistenza** e **e_service**; queste ultime due sono obbligatorie e validate dallo schema.
- **Sezione casi d'uso**: `casi_d_uso` è obbligatoria e unifica i casi documento esistente e non; i campi opzionali si compilano in base al caso.
- **`metadata`**: `nome_ente_titolare` e `nome_eaa` sono obbligatori con `minLength: 1` (non possono essere stringa vuota).
- **`campo_risposta`**: ogni domanda richiede `domanda` e `risposta`; `suggerimento` è facoltativo.
- **`assistenza.canali`**: ogni elemento ha `tipo` (enum: "Email assistenza", "Numero telefonico", "Altro"), `risposta` (stringa: indirizzo email, numero di telefono o descrizione a seconda del tipo; vuota se il canale non è utilizzato) e `note` (stringa); per tipo "Email assistenza" con risposta non vuota, lo schema valida il formato email.
- **`assistenza.referenti`**: ogni elemento ha `ruolo`, `nome`, `cognome`, `email`, `telefono` (tutti stringa).
- **`assistenza.faq`**: ogni elemento ha `domanda` e `risposta` (stringa).
- **`e_service.response`**: obbligatorio; contiene `versione` (stringa, es. "1.0"), `data_model`, `mappatura_errori` e `stati` (tutti array) relativi alla response dell'endpoint Fonte Autentica. `lista_nome_campo` resta a livello `e_service`.

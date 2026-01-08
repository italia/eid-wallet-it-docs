# Script per aggiornare le GitHub Issues con i requisiti ARF

Questi script permettono di analizzare i file annex-2.0* del documento ARF (Architecture and Reference Framework) versione 2.7.3 e aggiornare automaticamente le tabelle markdown nelle sub-issues della issue #545 su GitHub, aggiornandole da ARF 2.5.0 a ARF 2.7.3.

## Prerequisiti

1. **GitHub CLI (gh)** installato e autenticato:
   ```bash
   gh auth login
   ```

2. **Python 3** con le librerie standard (nessuna dipendenza esterna richiesta)

3. **Accesso ai file ARF**: I file devono essere disponibili in:
   ```
   /home/wert/DEV/DTD/Wallet/eudi-doc-architecture-and-reference-framework/docs/annexes/annex-2/
   ```

## Struttura degli script

### 1. `analyze_arf_requirements.py`

Analizza i file annex-2.0* e estrae tutti i requisiti ARF, generando:
- `arf_requirements/requirements.json`: File JSON con tutti i requisiti
- `arf_requirements/tables_by_topic/`: Tabelle markdown organizzate per topic
- `arf_requirements/tables_by_category/`: Tabelle markdown organizzate per categoria

**Uso:**
```bash
python3 utils/analyze_arf_requirements.py
```

### 2. `update_github_issues.py`

Legge i requisiti dal JSON generato e aggiorna le tabelle markdown nelle sub-issues della issue #545.

**Modalità di utilizzo:**

#### Modalità Preview (consigliata)
Genera file di preview locali da rivedere prima di applicare:

```bash
# Genera solo i preview senza modificare le issues
python3 utils/update_github_issues.py --preview-only
```

I file di preview vengono salvati in `utils/arf_requirements/previews/` con il formato:
- `issue_<numero>_<titolo>.md`

Ogni file contiene:
- Il nuovo body completo della issue
- Un diff delle modifiche
- Informazioni sul topic e numero di requisiti

#### Applicazione delle modifiche
Dopo aver rivisto i preview, applica le modifiche:

```bash
# Applica le modifiche dai file di preview
python3 utils/update_github_issues.py --apply
```

**⚠️ Importante:** Il comando `gh issue edit --body` aggiorna **solo il main body** della issue. Tutti i commenti nel thread vengono **preservati** e non vengono modificati.

#### Modalità interattiva (default)
Genera i preview e chiede conferma prima di applicare:

```bash
python3 utils/update_github_issues.py
```

**Workflow completo:**
1. Carica i requisiti ARF 2.7.3 da `arf_requirements/requirements.json`
2. Recupera la issue #545 e cerca le sue sub-issues
3. Per ogni sub-issue, estrae il topic dal titolo
4. Trova i requisiti corrispondenti al topic in ARF 2.7.3
5. Confronta con i requisiti ARF 2.5.0 esistenti nella tabella
6. Genera file di preview locali con le nuove tabelle e diff dettagliato
7. (Opzionale) Rivedi i preview
8. Applica le modifiche su GitHub

## Formato delle tabelle

Le tabelle generate hanno il seguente formato:

```markdown
| **Requirement ID** | **Legacy ID** | **Description** | **Status** |
|-------------------|---------------|------------------|------------|
| OIA_01 |  | A Wallet Unit SHALL support... | 🟡 |
| OIA_02 | RPA_01 | A Wallet Unit SHALL support... | ✅ |
```

### Status disponibili

- ✅ Complete
- ❌ Not satisfied, not yet in it-wallet milestone
- 🟧 In progress since is configured in milestones or going to be
- 🟠 In progress but not directly deliverable, external dependencies and constraints requires more time
- 🟡 Not started yet, pending external dependencies and constraints, further informations are required
- ⚠️ Attention, something weak, concerning or not deeply understandable, it requires further alignments

**Nota:** Lo script preserva gli status esistenti quando aggiorna una tabella da ARF 2.5.0 a ARF 2.7.3. Se un requisito non ha uno status esistente, viene impostato a 🟡 (default).

**Aggiornamento ARF 2.5.0 → ARF 2.7.3:**
- Lo script confronta i requisiti esistenti (ARF 2.5.0) con quelli nuovi (ARF 2.7.3)
- Genera un diff dettagliato mostrando requisiti aggiunti, rimossi e modificati
- Aggiorna solo la tabella esistente, non aggiunge nuove sezioni

## Workflow consigliato

1. **Prima esecuzione:**
   ```bash
   # Analizza i file ARF e genera i requisiti
   python3 utils/analyze_arf_requirements.py
   ```

2. **Verifica i requisiti generati:**
   ```bash
   # Controlla i file generati
   ls -la utils/arf_requirements/
   cat utils/arf_requirements/requirements.json | jq '.by_topic | length'
   ```

3. **Genera i preview (consigliato):**
   ```bash
   # Assicurati di essere autenticato con GitHub CLI
   gh auth status
   
   # Genera i file di preview senza modificare le issues
   python3 utils/update_github_issues.py --preview-only
   ```

4. **Rivedi i preview:**
   ```bash
   # I file sono in utils/arf_requirements/previews/
   ls -la utils/arf_requirements/previews/
   
   # Apri e rivedi i file di preview
   # Ogni file contiene:
   # - Il nuovo body completo della issue
   # - Un diff delle modifiche
   # - Informazioni sul topic e numero di requisiti
   ```

5. **Applica le modifiche:**
   ```bash
   # Dopo aver rivisto i preview, applica le modifiche
   python3 utils/update_github_issues.py --apply
   ```

6. **Verifica manualmente:**
   - Controlla alcune issues aggiornate su GitHub
   - Verifica che le tabelle siano formattate correttamente
   - Verifica che gli status siano preservati

### Workflow alternativo (interattivo)

Se preferisci un workflow più interattivo:

```bash
# Genera i preview e chiede conferma prima di applicare
python3 utils/update_github_issues.py
```

Lo script genererà i preview e ti chiederà se vuoi procedere con l'aggiornamento.

## Risoluzione problemi

### Errore: "To use GitHub CLI in automation, set the GH_TOKEN environment variable"

**Soluzione:** Autentica GitHub CLI:
```bash
gh auth login
```

### Errore: "File non trovato: .../requirements.json"

**Soluzione:** Esegui prima `analyze_arf_requirements.py`:
```bash
python3 utils/analyze_arf_requirements.py
```

### Nessuna sub-issue trovata

**Soluzione:** Lo script ti permetterà di inserire manualmente i numeri delle issues da aggiornare. In alternativa, puoi modificare lo script per cercare le issues in modo diverso.

### Topic non riconosciuto

**Soluzione:** Verifica che il titolo della issue contenga "Topic X - ..." nel formato corretto. Puoi modificare la funzione `extract_topic_from_issue_title` per gestire altri formati.

## Personalizzazione

### Modificare il formato delle tabelle

Modifica la funzione `generate_requirement_table` in `update_github_issues.py`.

### Aggiungere nuovi pattern di ricerca per le sub-issues

Modifica la funzione `get_sub_issues` in `update_github_issues.py`.

### Cambiare il repository GitHub

Modifica il parametro `repo` nelle chiamate alle funzioni o passa `--repo` come argomento da linea di comando.

## Note

- Lo script preserva gli status esistenti nelle tabelle quando possibile
- Se un requisito non esiste più nel file ARF, non viene rimosso automaticamente dalla tabella (richiede intervento manuale)
- Se un nuovo requisito viene aggiunto al file ARF, viene aggiunto alla tabella con status 🟡 (default)
- Le tabelle vengono cercate e sostituite nel body della issue. Se non viene trovata una tabella esistente, viene aggiunta una nuova sezione alla fine
- **Modalità preview:** I file di preview vengono salvati in `utils/arf_requirements/previews/` e possono essere riveduti prima di applicare le modifiche
- **Sicurezza:** La modalità `--preview-only` non modifica mai le issues su GitHub, permettendo una revisione sicura delle modifiche

#!/usr/bin/env python3
"""
Script per aggiornare le tabelle markdown nelle sub-issues della issue #545
sulla base dei requisiti ARF estratti dai file annex-2.0*
"""

import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass


@dataclass
class IssueInfo:
    """Informazioni su una GitHub issue"""
    number: int
    title: str
    body: str


def run_gh_command(cmd: List[str]) -> Tuple[bool, str]:
    """
    Esegue un comando gh e ritorna (success, output)
    """
    try:
        result = subprocess.run(
            ['gh'] + cmd,
            capture_output=True,
            text=True,
            check=False
        )
        if result.returncode != 0:
            return False, result.stderr
        return True, result.stdout
    except Exception as e:
        return False, str(e)


def get_issue(issue_number: int, repo: str = "italia/eid-wallet-it-docs") -> Optional[IssueInfo]:
    """
    Ottiene le informazioni di una issue
    """
    success, output = run_gh_command([
        'issue', 'view', str(issue_number),
        '--repo', repo,
        '--json', 'number,title,body'
    ])
    
    if not success:
        print(f"❌ Errore nel recupero della issue #{issue_number}: {output}")
        return None
    
    try:
        data = json.loads(output)
        return IssueInfo(
            number=data['number'],
            title=data['title'],
            body=data['body']
        )
    except json.JSONDecodeError as e:
        print(f"❌ Errore nel parsing JSON per issue #{issue_number}: {e}")
        return None


def get_sub_issues(parent_issue_number: int, repo: str = "italia/eid-wallet-it-docs") -> List[IssueInfo]:
    """
    Ottiene tutte le sub-issues della issue parent.
    Cerca issues che menzionano la parent issue nel body o nel titolo.
    """
    sub_issues = []
    
    # Metodo 1: Cerca issues che referenziano la parent nel body
    success, output = run_gh_command([
        'issue', 'list',
        '--repo', repo,
        '--search', f'#{parent_issue_number}',
        '--json', 'number,title,body',
        '--limit', '100'
    ])
    
    if success:
        try:
            issues_data = json.loads(output)
            for issue_data in issues_data:
                if issue_data['number'] == parent_issue_number:
                    continue
                sub_issues.append(IssueInfo(
                    number=issue_data['number'],
                    title=issue_data['title'],
                    body=issue_data['body'] or ""
                ))
        except json.JSONDecodeError:
            pass
    
    # Metodo 2: Cerca issues nel progetto/milestone associato
    # (se la issue #545 è in un progetto, cerca altre issues nello stesso progetto)
    
    # Metodo 3: Cerca issues con "Topic" nel titolo (pattern comune per sub-issues ARF)
    success, output = run_gh_command([
        'issue', 'list',
        '--repo', repo,
        '--search', 'is:issue "Topic"',
        '--json', 'number,title,body',
        '--limit', '100'
    ])
    
    if success:
        try:
            issues_data = json.loads(output)
            for issue_data in issues_data:
                # Verifica che non sia già nella lista e che non sia la parent
                if issue_data['number'] == parent_issue_number:
                    continue
                if any(iss.number == issue_data['number'] for iss in sub_issues):
                    continue
                # Verifica che sia una sub-issue (contiene "Topic" nel titolo)
                if 'Topic' in issue_data['title']:
                    sub_issues.append(IssueInfo(
                        number=issue_data['number'],
                        title=issue_data['title'],
                        body=issue_data['body'] or ""
                    ))
        except json.JSONDecodeError:
            pass
    
    return sub_issues


def extract_topic_from_issue_title(title: str) -> Optional[str]:
    """
    Estrae il topic dalla title dell'issue.
    Es: "Topic 1 - Accessing Online Services" -> "Topic 1 - Accessing Online Services with a Wallet Unit"
    """
    # Cerca pattern come "Topic 1", "Topic 10", etc.
    match = re.search(r'Topic\s+(\d+)', title, re.IGNORECASE)
    if match:
        topic_num = match.group(1)
        # Prova a trovare il topic completo nel titolo
        topic_match = re.search(r'Topic\s+\d+\s*[-–]\s*(.+)', title, re.IGNORECASE)
        if topic_match:
            return f"Topic {topic_num} - {topic_match.group(1).strip()}"
        return f"Topic {topic_num}"
    return None


def find_requirements_for_topic(topic: str, requirements: List[Dict]) -> List[Dict]:
    """
    Trova tutti i requisiti per un dato topic.
    Fa matching esatto prima, poi prova matching per numero di topic se non trova nulla.
    """
    matching = []
    
    # Prima prova matching esatto
    for req in requirements:
        if req.get('topic') == topic:
            matching.append(req)
    
    # Se non trova nulla, prova matching per numero di topic
    if not matching:
        # Estrae il numero del topic (es: "Topic 31" -> 31)
        topic_num_match = re.search(r'Topic\s+(\d+)', topic, re.IGNORECASE)
        if topic_num_match:
            topic_num = topic_num_match.group(1)
            # Cerca requisiti che hanno lo stesso numero di topic
            for req in requirements:
                req_topic = req.get('topic', '')
                if re.search(rf'Topic\s+{topic_num}\s*[-–]', req_topic, re.IGNORECASE):
                    matching.append(req)
    
    return matching


def detect_table_format(existing_table: str, original_body: str = "") -> Dict[str, any]:
    """
    Rileva il formato della tabella esistente e ritorna informazioni su:
    - ordine delle colonne
    - header
    - presenza di colonne aggiuntive (es: IT-Wallet Mapping)
    
    Se original_body è fornito, cerca l'header originale nel body per preservare colonne vuote.
    """
    lines = existing_table.split('\n')
    header_line = None
    header_idx = -1
    
    # Trova l'header originale nel body se fornito (per preservare colonne vuote)
    original_header_line = None
    if original_body:
        body_lines = original_body.split('\n')
        for i, line in enumerate(body_lines):
            if '|' in line and ('ID' in line or 'Requirement' in line or 'Index' in line) and '---' not in line:
                # Verifica se questa riga è nell'area della tabella (ha Status, ID o Index con **)
                # Preferisce header con Status se presente
                if 'Status' in line:
                    # Pulisce l'header da Status duplicati prima di salvarlo
                    parts = [p.strip() for p in line.split('|')]
                    if parts and not parts[0]:
                        parts = parts[1:]
                    if parts and not parts[-1]:
                        parts = parts[:-1]
                    # Rimuove duplicati di Status
                    cleaned_parts = []
                    seen_status = False
                    for part in parts:
                        part_lower = part.strip('*').strip().lower()
                        is_status = 'status' in part_lower and part_lower.strip('*').strip() == 'status'
                        if is_status:
                            if not seen_status:
                                cleaned_parts.append(part)
                                seen_status = True
                            # Salta duplicati
                        else:
                            cleaned_parts.append(part)
                    # Ricostruisce l'header pulito
                    original_header_line = '| ' + ' | '.join(cleaned_parts) + ' |'
                    break
                elif ('ID' in line or 'Index' in line) and '**' in line and not original_header_line:
                    # Salva come fallback se non c'è Status
                    original_header_line = line
    
    # Trova l'header nella tabella estratta (gestisce anche header duplicati o malformati)
    for i, line in enumerate(lines):
        if '|' in line and ('ID' in line or 'Requirement' in line) and '---' not in line:
            if not original_header_line:
                original_header_line = line  # Usa quello della tabella se non trovato nel body
            header_line = line  # Usa quello della tabella per l'analisi
            header_idx = i
            
            # Se l'header contiene un separatore seguito da altro header, prende solo la prima parte
            # Esempio: |---|-----------|...| **Requirement ID** | **Legacy ID** |
            # Rimuove tutto dopo il separatore completo (|---|)
            if '|---' in header_line:
                # Cerca il punto dove inizia il separatore
                sep_pos = header_line.find('|---')
                if sep_pos > 0:
                    # Prende solo la parte prima del separatore
                    header_line = header_line[:sep_pos].rstrip('|').rstrip() + ' |'
            
            # Se l'header contiene ancora un secondo header (es: **Requirement ID**), rimuovilo
            if '**Requirement ID**' in header_line or '**Legacy ID**' in header_line:
                # Cerca dove inizia il secondo header
                match = re.search(r'\|[^\|]*\*\*Requirement ID\*\*', header_line)
                if match:
                    header_line = header_line[:match.start()].rstrip('|').rstrip() + ' |'
            
            # Verifica se la riga successiva contiene un header duplicato e rimuovila
            if i + 1 < len(lines):
                next_line = lines[i + 1]
                if '|---' in next_line and ('**Requirement ID**' in next_line or '**Legacy ID**' in next_line):
                    # La riga successiva contiene un header duplicato, rimuovila dalla tabella
                    # Questo verrà gestito quando si genera la nuova tabella
                    pass
            
            break
    
    if not header_line:
        # Formato default
        return {
            'format': 'standard',
            'columns': ['Requirement ID', 'Legacy ID', 'Description', 'Status'],
            'has_status_first': False,
            'has_mapping_column': False,
            'header': '| **Requirement ID** | **Legacy ID** | **Description** | **Status** |'
        }
    
    # Analizza le colonne dell'header
    header_parts_raw = header_line.split('|')
    # Rimuove solo la parte vuota finale (dopo l'ultimo |)
    if header_parts_raw and not header_parts_raw[-1].strip():
        header_parts_raw = header_parts_raw[:-1]
    # Rimuove solo la parte vuota iniziale (prima del primo |)
    if header_parts_raw and not header_parts_raw[0].strip():
        header_parts_raw = header_parts_raw[1:]
    
    # Preserva le colonne vuote nel mezzo (possono essere intenzionali)
    header_parts = [p.strip() for p in header_parts_raw]
    
    # Analizza la prima riga dati per vedere se c'è una colonna status non nell'header
    first_data_line = None
    if header_idx >= 0 and header_idx + 2 < len(lines):
        first_data_line = lines[header_idx + 2]
    
    first_data_parts = []
    has_status_in_data = False
    if first_data_line:
        first_data_parts = [p.strip() for p in first_data_line.split('|')]
        if first_data_parts and not first_data_parts[0]:
            first_data_parts = first_data_parts[1:]
        if first_data_parts and not first_data_parts[-1]:
            first_data_parts = first_data_parts[:-1]
        # Verifica se la prima colonna dei dati contiene uno status
        if first_data_parts and any(emoji in first_data_parts[0] for emoji in ['✅', '❌', '🟧', '🟠', '🟡', '⚠️']):
            has_status_in_data = True
    
    # Analizza le colonne dell'header originale
    column_names = []
    has_status_first = False
    has_mapping_column = False
    
    # Verifica se c'è uno status nei dati ma non nell'header
    if has_status_in_data and len(first_data_parts) > len(header_parts):
        # C'è una colonna status extra all'inizio dei dati
        column_names.append('Status')
        has_status_first = True
    
    # Analizza le colonne dell'header originale
    for part in header_parts:
        part_lower = part.lower().strip('*').strip()
        if 'status' in part_lower:
            column_names.append('Status')
            if len(column_names) == 1:
                has_status_first = True
        elif 'id' in part_lower and 'requirement' not in part_lower and 'legacy' not in part_lower:
            column_names.append('ID')
        elif 'requirement id' in part_lower or ('requirement' in part_lower and 'id' in part_lower):
            column_names.append('Requirement ID')
        elif 'legacy' in part_lower:
            column_names.append('Legacy ID')
        elif 'description' in part_lower or 'specification' in part_lower:
            column_names.append('Description')
        elif 'mapping' in part_lower or ('wallet' in part_lower and 'documentation' in part_lower):
            column_names.append('IT-Wallet Mapping')
            has_mapping_column = True
        else:
            column_names.append(part.strip('*').strip())
    
    # Verifica se c'è una colonna vuota all'inizio dell'header originale
    has_leading_empty_col = False
    if original_header_line:
        # Controlla se la prima colonna (dopo il | iniziale) è vuota nell'originale
        # Usa regex per rilevare qualsiasi spazio tra | e | all'inizio: |\s+| 
        if re.match(r'^\|\s+\|', original_header_line):
            has_leading_empty_col = True
        else:
            # Verifica anche analizzando le parti
            original_parts = original_header_line.split('|')
            if len(original_parts) > 2:
                first_col_orig = original_parts[1].strip() if len(original_parts) > 1 else ''
                second_col_orig = original_parts[2].strip() if len(original_parts) > 2 else ''
                # Se la prima colonna è vuota e la seconda non lo è, c'è una colonna vuota intenzionale
                if not first_col_orig and second_col_orig:
                    has_leading_empty_col = True
    
    # Costruisce l'header preservando esattamente l'originale
    # Se c'è Status nei dati ma non nell'header, dobbiamo aggiungerlo per allineare
    # Ma preserviamo il testo esatto dell'header originale (inclusa colonna vuota se presente)
    
    # Verifica se l'header generato (dopo pulizia) ha Status
    header_has_status = any('status' in p.lower() for p in header_parts)
    
    if has_status_first and not header_has_status:
        # I dati hanno Status ma l'header no - aggiungiamo Status all'inizio dell'header
        # per mantenere l'allineamento, ma preserviamo il resto esattamente
        # Ricostruisce preservando la formattazione originale
        new_header_parts = ['Status'] + header_parts
        # RIMOSSA colonna vuota iniziale: |   | diventa |
        new_header = '| ' + ' | '.join(new_header_parts) + ' |'
        # Aggiunge Status alle colonne se non presente
        if 'Status' not in column_names:
            column_names.insert(0, 'Status')
            has_status_first = True
    else:
        # Usa l'header originale così com'è (preserva spazi, formattazione, colonne vuote, etc.)
        # Se non c'è Status nei dati o è già nell'header, usa l'originale esattamente
        # Questo preserva anche la colonna vuota se presente
        # IMPORTANTE: Se l'original_header_line ha già Status, usalo direttamente
        # Non aggiungere Status di nuovo
        if original_header_line:
            # Verifica se l'header originale ha già Status
            original_has_status = 'Status' in original_header_line or any('status' in p.lower() for p in original_header_line.split('|'))
            if original_has_status:
                # L'header originale ha già Status, ma potrebbe essere malformato (duplicato)
                # Pulisce l'header originale rimuovendo duplicati
                orig_parts = [p.strip() for p in original_header_line.split('|')]
                if orig_parts and not orig_parts[0]:
                    orig_parts = orig_parts[1:]
                if orig_parts and not orig_parts[-1]:
                    orig_parts = orig_parts[:-1]
                
                # Rimuove duplicati di Status e colonne vuote multiple
                # IMPORTANTE: Rimuove TUTTE le colonne vuote multiple, mantenendo solo la prima se presente all'inizio
                cleaned_parts = []
                seen_status = False
                has_leading_empty = False
                seen_first_empty = False
                for i, part in enumerate(orig_parts):
                    part_stripped = part.strip()
                    part_lower = part_stripped.lower().strip('*').strip()
                    
                    # Verifica se è Status (case-insensitive, con o senza asterischi)
                    is_status = 'status' in part_lower and part_lower.strip('*').strip() == 'status'
                    
                    if is_status:
                        if not seen_status:
                            # Mantieni solo il primo Status
                            cleaned_parts.append(part_stripped)
                            seen_status = True
                        # Salta tutti i duplicati di Status
                        continue
                    elif not part_stripped:  # Colonna vuota
                        # Mantieni solo la PRIMA colonna vuota se presente all'inizio
                        # Salta tutte le altre colonne vuote (anche se consecutive all'inizio)
                        if i == 0 and not seen_first_empty:
                            # Prima colonna vuota all'inizio - mantienila
                            cleaned_parts.append('')
                            has_leading_empty = True
                            seen_first_empty = True
                        # Salta tutte le altre colonne vuote (anche se consecutive)
                        continue
                    else:
                        cleaned_parts.append(part_stripped)
                
                # Ricostruisce l'header pulito - RIMOSSA colonna vuota iniziale
                # Se c'è una colonna vuota iniziale, rimuovila completamente
                if cleaned_parts and not cleaned_parts[0]:
                    cleaned_parts = cleaned_parts[1:]
                new_header = '| ' + ' | '.join(cleaned_parts) + ' |'
                
                # IMPORTANTE: Se l'header pulito ha Status, aggiungilo alle colonne
                if seen_status and 'Status' not in column_names:
                    column_names.insert(0, 'Status')
                    has_status_first = True
            else:
                # L'header originale non ha Status, ma i dati sì - aggiungilo
                if has_status_first:
                    # Estrae le parti dell'header originale
                    orig_parts = [p.strip() for p in original_header_line.split('|')]
                    if orig_parts and not orig_parts[0]:
                        orig_parts = orig_parts[1:]
                    if orig_parts and not orig_parts[-1]:
                        orig_parts = orig_parts[:-1]
                    # Aggiunge Status all'inizio
                    new_header_parts = ['Status'] + orig_parts
                    # RIMOSSA colonna vuota iniziale: |   | diventa |
                    new_header = '| ' + ' | '.join(new_header_parts) + ' |'
                else:
                    new_header = original_header_line
        else:
            new_header = header_line
    
    return {
        'format': 'custom' if has_status_first or has_mapping_column else 'standard',
        'columns': column_names,
        'has_status_first': has_status_first,
        'has_mapping_column': has_mapping_column,
        'header': new_header,
        'original_header': header_line,
        'original_parts': header_parts
    }


def generate_requirement_table(requirements: List[Dict], preserve_existing_status: bool = True, 
                               existing_body: str = "", existing_table: Optional[str] = None) -> str:
    """
    Genera una tabella markdown con i requisiti.
    Se preserve_existing_status è True, cerca di preservare lo status esistente dalla tabella precedente.
    Se existing_table è fornito, preserva l'ordine delle colonne e le colonne aggiuntive.
    """
    if not requirements:
        return ""
    
    # Rileva il formato della tabella esistente
    table_format = None
    if existing_table:
        # Passa anche il body originale per preservare colonne vuote nell'header
        table_format = detect_table_format(existing_table, existing_body if existing_body else "")
    
    # Estrae gli status esistenti e mapping IT-Wallet se presenti
    existing_statuses = {}
    existing_mappings = {}
    if preserve_existing_status and existing_body:
        # Estrae usando parse_existing_table che gestisce già tutti i formati
        existing_reqs_dict = parse_existing_table(existing_table) if existing_table else {}
        for req_id, req_info in existing_reqs_dict.items():
            existing_statuses[req_id] = req_info.get('status', '🟡')
            # Il mapping potrebbe essere nella descrizione o in una colonna separata
            # Per ora estraiamo dalla tabella esistente se disponibile
        
        # Se c'è una colonna mapping, estrae anche quella dalla tabella esistente
        if table_format and table_format.get('has_mapping_column') and existing_table:
            lines = existing_table.split('\n')
            # Trova l'header per capire la posizione della colonna mapping
            header_idx = -1
            for i, line in enumerate(lines):
                if '|' in line and ('ID' in line or 'Requirement' in line) and '---' not in line:
                    header_idx = i
                    break
            
            if header_idx >= 0:
                # Trova l'indice della colonna mapping nell'header
                header_parts = [p.strip() for p in lines[header_idx].split('|')]
                if header_parts and not header_parts[0]:
                    header_parts = header_parts[1:]
                if header_parts and not header_parts[-1]:
                    header_parts = header_parts[:-1]
                
                mapping_col_idx = -1
                for i, part in enumerate(header_parts):
                    if 'mapping' in part.lower() or ('wallet' in part.lower() and 'documentation' in part.lower()):
                        mapping_col_idx = i
                        # Se c'è una colonna status prima, aggiusta l'indice
                        if table_format.get('has_status_first'):
                            mapping_col_idx += 1
                        break
                
                # Estrae i mapping dalle righe dati
                if mapping_col_idx >= 0:
                    for line in lines[header_idx + 2:]:  # Salta header e separatore
                        if not line.strip().startswith('|') or '--' in line:
                            continue
                        parts = [p.strip() for p in line.split('|')]
                        if parts and not parts[0]:
                            parts = parts[1:]
                        if parts and not parts[-1]:
                            parts = parts[:-1]
                        
                        if len(parts) > mapping_col_idx:
                            # Trova l'ID del requisito (di solito nella colonna dopo Status se presente)
                            req_id_col_idx = 1 if table_format.get('has_status_first') else 0
                            if len(parts) > req_id_col_idx:
                                req_id = parts[req_id_col_idx].strip('*').strip()
                                if req_id and req_id not in ['ID', 'Requirement Specification']:
                                    mapping = parts[mapping_col_idx].strip()
                                    existing_mappings[req_id] = mapping
    
    lines = []
    
    # Genera l'header preservando l'ordine originale
    if table_format and table_format['format'] == 'custom':
        # Usa l'header preservato (con Status aggiunto se necessario)
        # RIMOSSA colonna vuota iniziale dall'header se presente: |\s+| diventa |
        # Usa regex per rimuovere qualsiasi spazio tra | e | all'inizio
        header = table_format['header']
        # Rimuove colonna vuota iniziale: | seguito da spazi e poi | -> |
        header = re.sub(r'^\|\s+\|', '|', header)
        lines.append(header)
        
        # Genera il separatore basandosi sull'header originale
        # Estrae il separatore dalla tabella esistente se disponibile
        if existing_table:
            table_lines = existing_table.split('\n')
            separator_line = None
            header_found = False
            for i, line in enumerate(table_lines):
                if '|' in line and ('ID' in line or 'Requirement' in line) and '---' not in line:
                    header_found = True
                    continue
                if header_found and '---' in line and '|' in line:
                    # Prende il primo separatore valido dopo l'header
                    # Verifica che non contenga header duplicati
                    if '**Requirement ID**' not in line and '**Legacy ID**' not in line:
                        separator_line = line
                        break
            
            if separator_line and not table_format.get('has_status_first'):
                # Pulisce il separatore da eventuali parti duplicate
                separator_parts = [p.strip() for p in separator_line.split('|')]
                if separator_parts and not separator_parts[0]:
                    separator_parts = separator_parts[1:]
                if separator_parts and not separator_parts[-1]:
                    separator_parts = separator_parts[:-1]
                # Rimuove eventuali parti dopo un separatore completo (|---|) o header duplicati
                cleaned_parts = []
                for part in separator_parts:
                    # Se contiene header duplicato (es: **Requirement ID**), ferma qui
                    if '**Requirement ID**' in part or '**Legacy ID**' in part or '**Description**' in part:
                        break
                    # Se contiene solo '---', è valido
                    if '---' in part:
                        cleaned_parts.append(part)
                    elif not part:
                        # Colonna vuota, mantienila
                        cleaned_parts.append('---')
                # Verifica che il numero di colonne corrisponda all'header (RIMOSSA colonna vuota)
                expected_cols = len(table_format['columns'])
                if len(cleaned_parts) == expected_cols:
                    # Il separatore ha già il numero corretto di colonne
                    lines.append('|' + '|'.join(cleaned_parts) + '|')
                elif len(cleaned_parts) == expected_cols - 1:
                    # RIMOSSA colonna vuota iniziale: |   | diventa |
                    lines.append('| ' + ' | '.join(cleaned_parts) + ' |')
                elif len(cleaned_parts) < expected_cols:
                    # RIMOSSA colonna vuota iniziale: |   | diventa |
                    lines.append('| ' + ' | '.join(cleaned_parts) + ' |')
                else:
                    # Genera il separatore manualmente se la pulizia fallisce o non corrisponde
                    # RIMOSSA colonna vuota iniziale
                    separator_parts = []
                    for col in table_format['columns']:
                        if col == 'Status':
                            separator_parts.append('---')
                        elif col == 'ID' or col == 'Requirement ID' or col == 'Index':
                            separator_parts.append('---------')
                        elif col == 'Legacy ID':
                            separator_parts.append('---------------')
                        elif col == 'Description' or 'Specification' in col:
                            separator_parts.append('------------------')
                        elif col == 'IT-Wallet Mapping' or 'Mapping' in col:
                            separator_parts.append('-----------------------------------')
                        else:
                            separator_parts.append('---')
                    lines.append('|' + '|'.join(separator_parts) + '|')
            elif separator_line and table_format.get('has_status_first'):
                # Aggiunge una colonna separatore per Status all'inizio
                separator_parts = [p.strip() for p in separator_line.split('|')]
                if separator_parts and not separator_parts[0]:
                    separator_parts = separator_parts[1:]
                if separator_parts and not separator_parts[-1]:
                    separator_parts = separator_parts[:-1]
                # Rimuove eventuali parti duplicate o header duplicati
                cleaned_parts = []
                for part in separator_parts:
                    # Se contiene header duplicato, ferma qui
                    if '**Requirement ID**' in part or '**Legacy ID**' in part or '**Description**' in part:
                        break
                    if '---' in part:
                        cleaned_parts.append(part)
                    elif not part:
                        cleaned_parts.append('---')
                # Verifica se c'è una colonna vuota all'inizio dell'header generato (non original_header)
                # Usa regex per rilevare qualsiasi spazio tra | e | all'inizio: |\s+|
                has_leading_empty = bool(re.match(r'^\|\s+\|', table_format.get('header', '')))
                # expected_cols = numero di colonne nel separatore estratto (senza Status, senza colonna vuota)
                # cleaned_parts contiene le colonne del separatore estratto (senza Status, senza colonna vuota)
                expected_cols_no_status = len(table_format['columns']) - 1  # Meno Status
                if len(cleaned_parts) == expected_cols_no_status:
                    # Il separatore estratto ha il numero corretto di colonne (senza Status, senza colonna vuota)
                    # Aggiunge colonna vuota (se presente) + Status all'inizio
                    # RIMOSSA colonna vuota iniziale
                    cleaned_parts = ['---'] + cleaned_parts
                    lines.append('|' + '|'.join(cleaned_parts) + '|')
                elif len(cleaned_parts) == expected_cols_no_status - 1:
                    # RIMOSSA colonna vuota iniziale
                    cleaned_parts = ['---'] + cleaned_parts
                    lines.append('|' + '|'.join(cleaned_parts) + '|')
                else:
                    # Genera il separatore manualmente - RIMOSSA colonna vuota iniziale
                    separator_parts = []
                    for col in table_format['columns']:
                        if col == 'Status':
                            separator_parts.append('---')
                        elif col == 'ID' or col == 'Requirement ID' or col == 'Index':
                            separator_parts.append('---------')
                        elif col == 'Legacy ID':
                            separator_parts.append('---------------')
                        elif col == 'Description' or 'Specification' in col:
                            separator_parts.append('------------------')
                        elif col == 'IT-Wallet Mapping' or 'Mapping' in col:
                            separator_parts.append('-----------------------------------')
                        else:
                            separator_parts.append('---')
                    lines.append('|' + '|'.join(separator_parts) + '|')
            else:
                # Genera il separatore manualmente - RIMOSSA colonna vuota iniziale
                separator_parts = []
                for col in table_format['columns']:
                    if col == 'Status':
                        separator_parts.append('---')
                    elif col == 'ID' or col == 'Requirement ID':
                        separator_parts.append('---------')
                    elif col == 'Legacy ID':
                        separator_parts.append('---------------')
                    elif col == 'Description':
                        separator_parts.append('------------------')
                    elif col == 'IT-Wallet Mapping':
                        separator_parts.append('-----------------------------------')
                    else:
                        separator_parts.append('---')
                lines.append('|' + '|'.join(separator_parts) + '|')
        else:
            # Genera il separatore manualmente
            separator_parts = []
            for col in table_format['columns']:
                if col == 'Status':
                    separator_parts.append('---')
                elif col == 'ID' or col == 'Requirement ID':
                    separator_parts.append('---------')
                elif col == 'Legacy ID':
                    separator_parts.append('---------------')
                elif col == 'Description':
                    separator_parts.append('------------------')
                elif col == 'IT-Wallet Mapping':
                    separator_parts.append('-----------------------------------')
                else:
                    separator_parts.append('---')
            lines.append('|' + '|'.join(separator_parts) + '|')
    else:
        # Formato standard
        lines.append("| **Requirement ID** | **Legacy ID** | **Description** | **Status** |")
        lines.append("|-------------------|---------------|------------------|------------|")
    
    # Genera le righe dati
    for req in requirements:
        req_id = req['identifier']
        legacy_id = req.get('legacy_identifier') or ""
        # Mantiene il testo completo originale degli ARF HLR senza troncamento
        desc = req['description'].replace('\n', ' ').strip()
        
        # Usa lo status esistente se disponibile, altrimenti default
        status = existing_statuses.get(req_id, "🟡")
        
        # Usa il mapping esistente se disponibile
        mapping = existing_mappings.get(req_id, "")
        
        # Costruisce la riga secondo l'ordine delle colonne
        if table_format and table_format['format'] == 'custom':
            row_parts = []
            # RIMOSSA colonna vuota iniziale - non più necessaria
            
            # Costruisce le parti della riga
            for col in table_format['columns']:
                if col == 'Status':
                    row_parts.append(status)
                elif col == 'ID' or col == 'Requirement ID' or col == 'Index':
                    row_parts.append(req_id)
                elif col == 'Legacy ID':
                    row_parts.append(legacy_id)
                elif col == 'Description' or 'Specification' in col:
                    row_parts.append(desc)
                elif col == 'IT-Wallet Mapping' or 'Mapping' in col:
                    row_parts.append(mapping)
                else:
                    row_parts.append("")
            
            # Costruisce la riga - RIMOSSA colonna vuota iniziale (|   | diventa |)
            # Formato: | status | id | desc | mapping |
            lines.append('| ' + ' | '.join(row_parts) + ' |')
        else:
            # Formato standard
            lines.append(f"| {req_id} | {legacy_id} | {desc} | {status} |")
    
    return "\n".join(lines)


def extract_existing_table(body: str, issue_number: int = 0) -> Tuple[Optional[str], Optional[int], Optional[int]]:
    """
    Estrae la tabella esistente dal body della issue.
    Supporta diversi formati di tabella.
    Ritorna (tabella, start_pos, end_pos) o (None, None, None) se non trovata.
    """
    # Cerca l'inizio della tabella (pattern più flessibile e completo)
    # Cerca TUTTE le possibili varianti di header di tabella
    table_patterns = [
        r'(\|\s*\*\*Requirement ID\*\*\s*\|[^\n]+\n)',  # Standard: | **Requirement ID** |
        r'(\|\s*\*\*Requirement\s+ID\*\*\s*\|[^\n]+\n)',  # Con spazio
        r'(\|\s*\*\*ID\*\*\s*\|[^\n]+\n)',  # Solo ID
        r'(\|\s*ID\s*\|[^\n]+\n)',  # ID senza asterischi
        r'(\|\s*\*\*Index\*\*\s*\|[^\n]+\n)',  # Index (per issue 693 e simili)
        r'(\|\s*Index\s*\|[^\n]+\n)',  # Index senza asterischi
        r'(\|\s*\*\*Requirement specification\*\*\s*\|[^\n]+\n)',  # Requirement specification
        r'(\|\s*Requirement specification\s*\|[^\n]+\n)',  # Requirement specification senza asterischi
        r'(\|\s*Status\s*\|[^\n]+\n)',  # Status
        r'(\|\s*\*\*Status\*\*\s*\|[^\n]+\n)',  # Status con asterischi
        r'(\|\s*\|\s*ID\s*\|[^\n]+\n)',  # Con colonna vuota: | | ID |
        r'(\|\s*\s*\|\s*ID\s*\|[^\n]+\n)',  # Con colonna vuota e spazi: |   | ID |
        r'(\|\s*\|\s*Status\s*\|[^\n]+\n)',  # Con colonna vuota e Status: | | Status |
        r'(\|\s*\s*\|\s*Status\s*\|[^\n]+\n)',  # Con colonna vuota e spazi e Status: |   | Status |
        r'(\|\s*\|\s*\*\*Index\*\*\s*\|[^\n]+\n)',  # Con colonna vuota e Index: | | **Index** |
        r'(\|\s*\s*\|\s*\*\*Index\*\*\s*\|[^\n]+\n)',  # Con colonna vuota e spazi e Index: |   | **Index** |
    ]
    
    table_match = None
    start_pos = None
    
    for pattern in table_patterns:
        match = re.search(pattern, body, re.IGNORECASE)
        if match:
            table_match = match
            start_pos = match.start()
            break
    
    # Se non trova con i pattern specifici, cerca qualsiasi tabella markdown
    # Cerca pattern più generici: qualsiasi riga che inizia con | e contiene "ID", "Requirement", "Status", o "Specification"
    if not table_match:
        generic_patterns = [
            r'(\|\s*[^\n]*(ID|Requirement|Status|Specification)[^\n]*\|[^\n]+\n)',  # Pattern generico
            r'(\|\s*[^\n]*ID[^\n]*\|[^\n]+\n)',  # Pattern con ID
            r'(\|\s*[^\n]*Status[^\n]*\|[^\n]+\n)',  # Pattern con Status
        ]
        
        for generic_pattern in generic_patterns:
            match = re.search(generic_pattern, body, re.IGNORECASE)
            if match:
                # Verifica che sia effettivamente una tabella (almeno 2 righe con |)
                potential_start = match.start()
                # Conta quante righe consecutive iniziano con |
                lines_after = body[potential_start:potential_start+1000].split('\n')
                table_lines = 0
                for line in lines_after[:20]:
                    if line.strip().startswith('|'):
                        table_lines += 1
                    elif line.strip() and not line.strip().startswith('|') and table_lines > 0:
                        # Se abbiamo già visto righe di tabella, fermiamoci
                        break
                
                if table_lines >= 2:  # Almeno header e una riga dati o separatore
                    table_match = match
                    start_pos = potential_start
                    break
    
    # Ultimo tentativo: cerca qualsiasi sequenza di righe che iniziano con |
    # Cerca TUTTE le possibili tabelle, non solo la prima
    if not table_match:
        lines = body.split('\n')
        # Cerca pattern: almeno 2 righe consecutive che iniziano con |
        for i in range(len(lines) - 1):
            if (lines[i].strip().startswith('|') and 
                lines[i+1].strip().startswith('|')):
                # Verifica che non sia solo un separatore
                if '---' not in lines[i] or ('---' in lines[i] and '---' not in lines[i+1]):
                    # Potrebbe essere una tabella - verifica che ci siano almeno 2 righe di tabella
                    table_lines = 0
                    for j in range(i, min(i+20, len(lines))):
                        if lines[j].strip().startswith('|'):
                            table_lines += 1
                        elif lines[j].strip() and not lines[j].strip().startswith('|') and table_lines > 0:
                            # Se abbiamo già visto righe di tabella, fermiamoci
                            break
                    
                    # Accetta se ha almeno 2 righe (header + almeno 1 riga dati o separatore)
                    if table_lines >= 2:
                        start_pos = sum(len(lines[j]) + 1 for j in range(i))  # +1 per il newline
                        # Crea un match fittizio
                        class FakeMatch:
                            def __init__(self, pos):
                                self.start = lambda: pos
                        table_match = FakeMatch(start_pos)
                        break
    
    if not table_match:
        if issue_number > 0:
            print(f"   ⚠️  Issue #{issue_number}: Nessuna tabella trovata. Pattern cercati: {len(table_patterns) + 1}")
            # Debug: mostra le prime righe del body per capire il formato
            first_lines = body[:500].split('\n')[:10]
            print(f"   📄 Prime righe del body:")
            for i, line in enumerate(first_lines):
                if '|' in line:
                    print(f"      {i}: {line[:100]}")
        return None, None, None
    
    # Trova la fine della tabella (due newline consecutivi o nuova sezione)
    end_pattern = r'\n\n(?!\|)|(?=\n##)|(?=\n###)|(?=\n#)'
    end_match = re.search(end_pattern, body[start_pos:])
    
    if end_match:
        end_pos = start_pos + end_match.start()
        old_table = body[start_pos:end_pos].strip()
    else:
        # Se non trova la fine, cerca l'ultima riga che inizia con |
        lines = body[start_pos:].split('\n')
        last_table_line = 0
        for i, line in enumerate(lines):
            if line.strip().startswith('|'):
                last_table_line = i
            elif line.strip() and not line.strip().startswith('|') and i > 2:
                # Se abbiamo già visto almeno 2 righe di tabella, fermiamoci qui
                break
        
        if last_table_line > 0:
            end_pos = start_pos + len('\n'.join(lines[:last_table_line + 1]))
            old_table = body[start_pos:end_pos].strip()
        else:
            # Prende fino alla fine del body
            end_pos = len(body)
            old_table = body[start_pos:].strip()
    
    # Verifica che la tabella estratta abbia almeno 2 righe
    # Accetta anche tabelle con solo header e separatore (2 righe)
    if old_table:
        table_lines = [l for l in old_table.split('\n') if l.strip().startswith('|')]
        if len(table_lines) < 2:
            if issue_number > 0:
                print(f"   ⚠️  Issue #{issue_number}: Tabella trovata ma troppo corta ({len(table_lines)} righe, minimo 2)")
            return None, None, None
    
    return old_table, start_pos, end_pos


def parse_existing_table(table_text: str) -> Dict[str, Dict]:
    """
    Analizza la tabella esistente e ritorna un dizionario {req_id: {status, legacy_id, description}}
    Supporta diversi formati:
    1. | **Requirement ID** | **Legacy ID** | **Description** | **Status** |
    2. | Status | ID | Requirement Specification | IT-Wallet Mapping |
    """
    existing_reqs = {}
    lines = table_text.split('\n')
    
    # Determina il formato della tabella guardando l'header
    header_line = None
    header_idx = -1
    for i, line in enumerate(lines):
        if '|' in line and ('ID' in line or 'Requirement' in line or 'Index' in line) and '---' not in line:
            header_line = line.lower()
            header_idx = i
            break
    
    # Formato 1: Standard con Requirement ID come prima colonna
    # Formato 2: Con colonna status iniziale: | status | ID | Description | Mapping |
    is_standard_format = header_line and 'requirement id' in header_line
    has_status_column = False
    
    # Verifica se c'è una colonna status (guardando la prima riga dati dopo l'header)
    if header_idx >= 0 and header_idx + 2 < len(lines):
        first_data_line = lines[header_idx + 2]
        first_data_parts = [p.strip() for p in first_data_line.split('|')]
        first_data_parts = [p for p in first_data_parts if p]
        if first_data_parts and any(emoji in first_data_parts[0] for emoji in ['✅', '❌', '🟧', '🟠', '🟡', '⚠️']):
            has_status_column = True
    
    for line in lines:
        if not line.strip().startswith('|') or '--' in line:
            continue
        
        # Salta le righe header
        if '**' in line and ('ID' in line or 'Requirement' in line or 'Status' in line):
            continue
        
        # Split mantenendo le colonne vuote (importante per il formato con colonna status)
        parts = [p.strip() for p in line.split('|')]
        # Rimuove solo la prima e l'ultima se vuote (dovute al | iniziale e finale)
        if parts and not parts[0]:
            parts = parts[1:]
        if parts and not parts[-1]:
            parts = parts[:-1]
        
        if len(parts) < 2:
            continue
        
        if is_standard_format:
            # Formato standard: | req_id | legacy_id | description | status |
            req_id = parts[0].strip('*').strip()
            legacy_id = parts[1].strip('*').strip() if len(parts) > 1 else ""
            description = parts[2].strip('*').strip() if len(parts) > 2 else ""
            status = parts[3].strip() if len(parts) > 3 else "🟡"
        elif has_status_column:
            # Formato con colonna status: | status | req_id | description | mapping |
            if len(parts) >= 3:
                status = parts[0].strip() if any(emoji in parts[0] for emoji in ['✅', '❌', '🟧', '🟠', '🟡', '⚠️']) else "🟡"
                req_id = parts[1].strip('*').strip()
                description = parts[2].strip('*').strip()
                legacy_id = ""
            else:
                continue
        else:
            # Formato alternativo: | status | req_id | description | mapping |
            # La prima colonna potrebbe essere vuota o contenere lo status
            first_col = parts[0].strip() if len(parts) > 0 else ""
            second_col = parts[1].strip() if len(parts) > 1 else ""
            
            # Se la prima colonna contiene uno status emoji, è lo status
            if any(emoji in first_col for emoji in ['✅', '❌', '🟧', '🟠', '🟡', '⚠️']):
                status = first_col
                req_id = second_col.strip('*').strip()
                description = parts[2].strip('*').strip() if len(parts) > 2 else ""
                legacy_id = ""
            elif first_col == "" or first_col == "---":
                # La prima colonna è vuota o separatore, lo status è nella seconda colonna
                if any(emoji in second_col for emoji in ['✅', '❌', '🟧', '🟠', '🟡', '⚠️']):
                    status = second_col
                    req_id = parts[2].strip('*').strip() if len(parts) > 2 else ""
                    description = parts[3].strip('*').strip() if len(parts) > 3 else ""
                else:
                    # Nessuno status trovato, usa default
                    status = "🟡"
                    req_id = second_col.strip('*').strip()
                    description = parts[2].strip('*').strip() if len(parts) > 2 else ""
                legacy_id = ""
            else:
                # Formato non riconosciuto, prova a estrarre comunque
                status = "🟡"
                req_id = second_col.strip('*').strip() if second_col else (first_col.strip('*').strip() if first_col else "")
                description = parts[2].strip('*').strip() if len(parts) > 2 else ""
                legacy_id = ""
        
        # Valida che req_id sia un identificatore valido
        # Deve contenere underscore o essere nel formato REQ_XX o AS-XX-XX-XXX
        is_valid_id = (
            req_id and 
            req_id != '--' and 
            not req_id.startswith('---') and 
            req_id not in ['ID', 'Requirement Specification', 'IT-Wallet Mapping & Documentation', 'Requirement ID', 'Legacy ID', 'Description', 'Status'] and
            not req_id.isdigit() and
            ('_' in req_id or '-' in req_id or req_id.startswith(('OIA', 'PID', 'RPA', 'WUA', 'ISSU', 'VCR', 'AS-', 'EW-')))
        )
        
        if is_valid_id:
            # Verifica che non sia solo un emoji o testo header
            if not all(c in ['✅', '❌', '🟧', '🟠', '🟡', '⚠️', ' '] for c in req_id):
                existing_reqs[req_id] = {
                    'status': status,
                    'legacy_id': legacy_id,
                    'description': description
                }
    
    return existing_reqs


def find_diff_parts(old_text: str, new_text: str) -> Tuple[str, str]:
    """
    Trova la parte modificata tra due testi, aggiungendo "..." se necessario.
    Ritorna (old_part, new_part) con solo la parte modificata.
    """
    if old_text == new_text:
        return old_text, new_text
    
    # Trova il prefisso comune
    prefix_len = 0
    min_len = min(len(old_text), len(new_text))
    while prefix_len < min_len and old_text[prefix_len] == new_text[prefix_len]:
        prefix_len += 1
    
    # Trova il suffisso comune
    suffix_len = 0
    while (suffix_len < min_len - prefix_len and 
           old_text[-(suffix_len + 1)] == new_text[-(suffix_len + 1)]):
        suffix_len += 1
    
    # Estrae la parte modificata
    old_part = old_text[prefix_len:len(old_text) - suffix_len] if suffix_len > 0 else old_text[prefix_len:]
    new_part = new_text[prefix_len:len(new_text) - suffix_len] if suffix_len > 0 else new_text[prefix_len:]
    
    # Se old_part è vuoto ma new_part no, significa che è stato aggiunto testo nel mezzo
    # Mostra il contesto intorno alla posizione dell'aggiunta
    if not old_part and new_part:
        # Mostra un po' di contesto prima e dopo la posizione dell'aggiunta
        context_before = old_text[max(0, prefix_len - 15):prefix_len]
        context_after = old_text[len(old_text) - suffix_len:min(len(old_text), len(old_text) - suffix_len + 15)]
        
        old_part = context_before + context_after
        new_part = context_before + new_part + context_after
        
        # Aggiunge "..." se c'è più testo
        if prefix_len > 15:
            old_part = "..." + old_part
            new_part = "..." + new_part
        if suffix_len > 15:
            old_part = old_part + "..."
            new_part = new_part + "..."
    # Se new_part è vuoto ma old_part no, significa che è stato rimosso testo
    elif old_part and not new_part:
        # Mostra il contesto intorno alla posizione della rimozione
        context_before = old_text[max(0, prefix_len - 15):prefix_len]
        context_after = old_text[len(old_text) - suffix_len:min(len(old_text), len(old_text) - suffix_len + 15)]
        
        old_part = context_before + old_part + context_after
        new_part = context_before + context_after
        
        # Aggiunge "..." se c'è più testo
        if prefix_len > 15:
            old_part = "..." + old_part
            new_part = "..." + new_part
        if suffix_len > 15:
            old_part = old_part + "..."
            new_part = new_part + "..."
    # Se entrambe le parti sono vuote (modifica nel mezzo), mostra il contesto intorno
    elif not old_part and not new_part and prefix_len > 0 and suffix_len > 0:
        context_start = max(0, prefix_len - 20)
        context_end_old = min(len(old_text), len(old_text) - suffix_len + 20)
        context_end_new = min(len(new_text), len(new_text) - suffix_len + 20)
        
        old_part = old_text[context_start:context_end_old]
        new_part = new_text[context_start:context_end_new]
        
        # Aggiunge "..." se c'è più testo
        if context_start > 0:
            old_part = "..." + old_part
            new_part = "..." + new_part
        if context_end_old < len(old_text) or context_end_new < len(new_text):
            old_part = old_part + "..."
            new_part = new_part + "..."
    else:
        # Limita la lunghezza della parte modificata
        max_length = 150
        if len(old_part) > max_length:
            old_part = old_part[:max_length] + "..."
        if len(new_part) > max_length:
            new_part = new_part[:max_length] + "..."
        
        # Aggiunge "..." se c'è testo prima o dopo
        if prefix_len > 0:
            old_part = "..." + old_part
            new_part = "..." + new_part
        if suffix_len > 0:
            old_part = old_part + "..."
            new_part = new_part + "..."
    
    return old_part, new_part


def generate_diff_report(existing_reqs: Dict[str, Dict], new_requirements: List[Dict], 
                         existing_table: str) -> str:
    """
    Genera un report dettagliato delle differenze tra ARF 2.5.0 (esistente) e ARF 2.7.3 (nuovo)
    """
    new_req_ids = {req['identifier'] for req in new_requirements}
    old_req_ids = set(existing_reqs.keys())
    
    added = new_req_ids - old_req_ids
    removed = old_req_ids - new_req_ids
    changed = []
    
    # Verifica se ci sono requisiti con descrizioni cambiate
    for req in new_requirements:
        req_id = req['identifier']
        if req_id in existing_reqs:
            old_desc = existing_reqs[req_id].get('description', '')
            new_desc = req['description'].replace('\n', ' ').strip()
            if old_desc != new_desc[:len(old_desc)] if old_desc else True:
                changed.append(req_id)
    
    lines = []
    lines.append("## Diff ARF 2.5.0 → ARF 2.7.3\n\n")
    # Rimuoviamo "Update from ARF 2.5.0 to ARF 2.7.3" per evitare ridondanze
    
    if added:
        lines.append(f"### ✅ Requirements added in ARF 2.7.3 ({len(added)}):\n\n")
        for req_id in sorted(added):
            req = next((r for r in new_requirements if r['identifier'] == req_id), None)
            if req:
                desc = req['description'].replace('\n', ' ').strip()
                # NON troncare - mostra il testo completo
                lines.append(f"- **{req_id}**: {desc}\n")
        lines.append("\n")
    
    if removed:
        lines.append(f"### ❌ Requirements removed in ARF 2.7.3 ({len(removed)}):\n\n")
        for req_id in sorted(removed):
            old_info = existing_reqs[req_id]
            desc = old_info.get('description', '').replace('\n', ' ').strip()
            # NON troncare - mostra il testo completo
            lines.append(f"- **{req_id}**: {desc}\n")
        lines.append("\n")
    
    if changed:
        lines.append(f"### 🔄 Requirements modified in ARF 2.7.3 ({len(changed)}):\n\n")
        for req_id in sorted(changed):
            req = next((r for r in new_requirements if r['identifier'] == req_id), None)
            if req:
                old_info = existing_reqs[req_id]
                old_desc = old_info.get('description', '').replace('\n', ' ').strip()
                new_desc = req['description'].replace('\n', ' ').strip()
                
                # Trova la parte modificata
                old_part, new_part = find_diff_parts(old_desc, new_desc)
                
                lines.append(f"- **{req_id}**:\n")
                if old_part == new_part:
                    # Nessuna differenza visibile (potrebbe essere solo spazi/formattazione)
                    lines.append(f"  - Modified (details not available)\n")
                else:
                    lines.append(f"  - **Old:** {old_part}\n")
                    lines.append(f"  - **New:** {new_part}\n")
        lines.append("\n")
    
    if not added and not removed and not changed:
        lines.append("### ℹ️ No changes detected\n\n")
        lines.append("The requirements are identical between ARF 2.5.0 and ARF 2.7.3.\n\n")
    
    lines.append(f"**Total requirements ARF 2.7.3:** {len(new_requirements)}\n")
    lines.append(f"**Total requirements ARF 2.5.0:** {len(existing_reqs)}\n")
    
    return "".join(lines)


def generate_modified_requirements_section(existing_reqs: Dict[str, Dict], new_requirements: List[Dict]) -> str:
    """
    Genera solo la sezione "Requisiti modificati in ARF 2.7.3" da includere dopo la tabella.
    """
    changed = []
    
    # Verifica se ci sono requisiti con descrizioni cambiate
    for req in new_requirements:
        req_id = req['identifier']
        if req_id in existing_reqs:
            old_desc = existing_reqs[req_id].get('description', '')
            new_desc = req['description'].replace('\n', ' ').strip()
            if old_desc != new_desc[:len(old_desc)] if old_desc else True:
                changed.append(req_id)
    
    if not changed:
        return ""  # Nessun requisito modificato, non aggiungere la sezione
    
    lines = []
    lines.append(f"### 🔄 Modified Requirements in ARF 2.7.3 ({len(changed)}):\n\n")
    
    for req_id in sorted(changed):
        req = next((r for r in new_requirements if r['identifier'] == req_id), None)
        if req:
            old_info = existing_reqs[req_id]
            old_desc = old_info.get('description', '').replace('\n', ' ').strip()
            new_desc = req['description'].replace('\n', ' ').strip()
            
            # Trova la parte modificata
            old_part, new_part = find_diff_parts(old_desc, new_desc)
            
            lines.append(f"- **{req_id}**:\n")
            if old_part == new_part:
                # Nessuna differenza visibile (potrebbe essere solo spazi/formattazione)
                lines.append(f"  - Modified (details not available)\n")
            else:
                lines.append(f"  - **Old:** {old_part}\n")
                lines.append(f"  - **New:** {new_part}\n")
    
    lines.append("\n")
    
    return "".join(lines)


def generate_preview(issue: IssueInfo, requirements: List[Dict], output_dir: Path) -> Optional[Path]:
    """
    Genera un file di preview locale con la nuova tabella aggiornata da ARF 2.5.0 a ARF 2.7.3.
    Aggiorna la tabella esistente e genera un diff dettagliato.
    Ritorna None se non è possibile generare il preview, con un messaggio di errore stampato.
    """
    # Estrae il topic dalla title
    topic = extract_topic_from_issue_title(issue.title)
    if not topic:
        return None
    
    # Trova i requisiti per questo topic
    topic_requirements = find_requirements_for_topic(topic, requirements)
    if not topic_requirements:
        return None
    
    # Estrae la tabella esistente
    existing_table, start_pos, end_pos = extract_existing_table(issue.body, issue.number)
    
    if not existing_table or start_pos is None:
        print(f"   ⚠️  Issue #{issue.number}: Nessuna tabella esistente trovata - saltata")
        return None
    
    # Analizza la tabella esistente
    existing_reqs = parse_existing_table(existing_table)
    
    # Genera la nuova tabella preservando gli status esistenti e l'ordine delle colonne
    new_table = generate_requirement_table(topic_requirements, preserve_existing_status=True, 
                                          existing_body=issue.body, existing_table=existing_table)
    
    # Genera il summary delle modifiche
    diff_report = generate_diff_report(existing_reqs, topic_requirements, existing_table)
    
    # Genera la sezione "Requisiti modificati in ARF 2.7.3" da includere dopo la tabella
    modified_section = generate_modified_requirements_section(existing_reqs, topic_requirements)
    
    # Sostituisce la tabella nel body e aggiunge la sezione dei requisiti modificati dopo
    # IMPORTANTE: Rimuove anche eventuali header duplicati/rotti che potrebbero essere nel body
    # prima della tabella sostituita
    body_before = issue.body[:start_pos]
    body_after = issue.body[end_pos:].lstrip()
    
    # Rimuove e corregge eventuali header/tabelle rotti/duplicati prima della tabella
    # Cerca pattern di header con Status duplicato o colonne vuote multiple
    lines_before = body_before.split('\n')
    cleaned_lines_before = []
    in_table_to_fix = False
    table_lines_to_fix = []
    
    for line in lines_before:
        # Se la riga contiene un header con Status duplicato, salta
        if '|' in line and 'Status' in line and line.count('Status') > 1:
            # Salta questa riga (è un header rotto)
            continue
        
        # Se la riga è un header con colonna vuota iniziale, rimuovila: |\s+| diventa |
        # Usa regex per rilevare qualsiasi spazio tra | e | all'inizio
        if '|' in line and ('Status' in line or '**ID**' in line) and 'ID' in line and '---' not in line:
            if re.match(r'^\|\s+\|', line):
                # Ha colonna vuota iniziale - rimuovila completamente
                in_table_to_fix = True
                table_lines_to_fix = []
                # Rimuove la colonna vuota iniziale dall'header: |\s+| diventa | (usa regex)
                fixed_line = re.sub(r'^\|\s+\|', '|', line)
                table_lines_to_fix.append(fixed_line)
                continue
        
        # Se siamo in una tabella da correggere, aggiungi le righe alla lista
        if in_table_to_fix:
            if '|' in line:
                # Rimuove la colonna vuota iniziale dalle righe dati: |\s+| diventa | (usa regex)
                fixed_line = re.sub(r'^\|\s+\|', '|', line)
                table_lines_to_fix.append(fixed_line)
                continue
            elif line.strip() == '':
                # Fine della tabella, aggiungi le righe corrette
                if table_lines_to_fix:
                    cleaned_lines_before.extend(table_lines_to_fix)
                cleaned_lines_before.append(line)
                in_table_to_fix = False
                table_lines_to_fix = []
                continue
            elif line.startswith('##') or line.startswith('#'):
                # Fine della tabella (nuova sezione), aggiungi le righe corrette
                if table_lines_to_fix:
                    cleaned_lines_before.extend(table_lines_to_fix)
                cleaned_lines_before.append(line)
                in_table_to_fix = False
                table_lines_to_fix = []
                continue
        
        if not in_table_to_fix:
            cleaned_lines_before.append(line)
    
    # Aggiungi eventuali righe rimanenti della tabella da correggere
    if table_lines_to_fix:
        cleaned_lines_before.extend(table_lines_to_fix)
    
    body_before_cleaned = '\n'.join(cleaned_lines_before)
    
    # Rimuove eventuali righe di tabella malformate o incomplete alla fine del body_before
    # Se l'ultima riga contiene solo "| Status" o simili (frammenti di tabella), rimuovila
    lines_before_final = body_before_cleaned.split('\n')
    # Rimuove righe vuote finali e poi controlla l'ultima riga non vuota
    while lines_before_final and not lines_before_final[-1].strip():
        lines_before_final = lines_before_final[:-1]
    
    if lines_before_final:
        last_line = lines_before_final[-1].strip()
        # Se l'ultima riga è solo "| Status" o simile (inizio di tabella malformata), rimuovila
        if last_line and last_line.startswith('|'):
            # Verifica se è una riga completa di tabella o solo un frammento
            parts = [p.strip() for p in last_line.split('|')]
            parts = [p for p in parts if p]  # Rimuove vuoti
            # Se ha solo 1-2 parti (es: "| Status" o "| Status |"), è un frammento - rimuovilo
            if len(parts) <= 2:
                lines_before_final = lines_before_final[:-1]
                body_before_cleaned = '\n'.join(lines_before_final)
    
    # Rimuove eventuali sezioni "Diff ARF 2.5.0 → ARF 2.7.3" e "No changes detected" esistenti dal body_before
    # per evitare duplicazioni quando viene aggiunta la nuova sezione
    lines_before_final = body_before_cleaned.split('\n')
    cleaned_lines_no_diff = []
    skip_until_empty = False
    skip_no_changes = False
    for i, line in enumerate(lines_before_final):
        if line.startswith('## Diff ARF 2.5.0 → ARF 2.7.3'):
            # Salta questa sezione e tutto fino alla prossima sezione ## o fine
            skip_until_empty = True
            continue
        elif (line.strip() == '### ℹ️ No changes detected' or 
              line.strip() == 'ℹ️ No changes detected' or
              (line.strip().startswith('###') and 'No changes detected' in line) or
              (line.strip().startswith('ℹ️') and 'No changes detected' in line)):
            # Salta anche le sezioni standalone "No changes detected"
            skip_no_changes = True
            continue
        elif 'No changes compared to previous versions of ARF' in line:
            # Rimuove anche questa riga ridondante
            continue
        elif skip_until_empty:
            # Continua a saltare fino a una riga vuota seguita da una sezione ## o fine
            if line.strip() == '':
                # Verifica se la prossima riga è una sezione ##
                if i + 1 < len(lines_before_final) and lines_before_final[i+1].startswith('##'):
                    skip_until_empty = False
                    cleaned_lines_no_diff.append(line)
                elif i + 1 >= len(lines_before_final):
                    # Fine del body
                    skip_until_empty = False
            elif line.startswith('##'):
                # Nuova sezione - smetti di saltare
                skip_until_empty = False
                cleaned_lines_no_diff.append(line)
        elif skip_no_changes:
            # Continua a saltare fino a una riga vuota o una nuova sezione
            if line.strip() == '':
                # Verifica se la prossima riga è una sezione ##
                if i + 1 < len(lines_before_final) and lines_before_final[i+1].startswith('##'):
                    skip_no_changes = False
                    cleaned_lines_no_diff.append(line)
                elif i + 1 >= len(lines_before_final):
                    # Fine del body
                    skip_no_changes = False
            elif line.startswith('##'):
                # Nuova sezione - smetti di saltare
                skip_no_changes = False
                cleaned_lines_no_diff.append(line)
            elif ('The requirements are identical' in line or
                  'No changes compared to previous versions of ARF' in line):
                # Salta anche queste righe
                continue
        else:
            cleaned_lines_no_diff.append(line)
    
    body_before_cleaned = '\n'.join(cleaned_lines_no_diff)
    
    # Assicura che body_before_cleaned finisca con una nuova riga vuota per separare la tabella dal testo
    body_before_cleaned = body_before_cleaned.rstrip()
    if body_before_cleaned and not body_before_cleaned.endswith('\n\n'):
        # Aggiunge una nuova riga vuota se non c'è già
        if body_before_cleaned.endswith('\n'):
            body_before_cleaned += '\n'
        else:
            body_before_cleaned += '\n\n'
    
    # Genera la sezione "Diff ARF 2.5.0 → ARF 2.7.3" completa da includere prima della tabella
    # Usa generate_diff_report per ottenere il contenuto completo (non solo l'header)
    diff_report = generate_diff_report(existing_reqs, topic_requirements, existing_table)
    # Estrae solo la sezione "Diff ARF 2.5.0 → ARF 2.7.3" dal diff_report (senza "Total requirements" finale)
    diff_lines = diff_report.split('\n')
    diff_section_lines = []
    in_diff_section = False
    for line in diff_lines:
        if line.startswith('## Diff ARF 2.5.0 → ARF 2.7.3'):
            if not in_diff_section:  # Evita duplicati
                in_diff_section = True
                diff_section_lines.append(line)
        elif in_diff_section:
            # Ferma quando trova "Total requirements" o fine del report
            if line.startswith('**Total requirements') or line.startswith('**Totale requisiti'):
                break
            diff_section_lines.append(line)
    diff_section = '\n'.join(diff_section_lines) + '\n\n' if diff_section_lines else "## Diff ARF 2.5.0 → ARF 2.7.3\n\n"
    
    # Genera la sezione "Modified Requirements in ARF 2.7.3" da includere dopo la tabella
    modified_section = generate_modified_requirements_section(existing_reqs, topic_requirements)
    
    # RIMUOVE colonna vuota iniziale anche dalla nuova tabella generata se presente
    # Usa regex per rimuovere qualsiasi spazio tra | e | all'inizio
    new_table_lines = new_table.split('\n')
    new_table_cleaned_lines = []
    for line in new_table_lines:
        # Rimuove colonna vuota iniziale: |\s+| diventa | (usa regex)
        cleaned_line = re.sub(r'^\|\s+\|', '|', line)
        new_table_cleaned_lines.append(cleaned_line)
    new_table = '\n'.join(new_table_cleaned_lines)
    
    # Rimuove e corregge anche eventuali header/tabelle con colonna vuota iniziale dopo la tabella
    # IMPORTANTE: Correggi SEMPRE le tabelle con colonna vuota iniziale: |\s+| diventa |
    # Usa regex per rilevare qualsiasi spazio tra | e | all'inizio
    if True:  # Sempre correggi le tabelle con colonna vuota iniziale
        lines_after = body_after.split('\n')
        cleaned_lines_after = []
        skip_table = False
        in_table_to_fix = False
        table_lines_to_fix = []
        
        for i, line in enumerate(lines_after):
            # Se la riga è un header con colonna vuota iniziale, rimuovila: |\s+| diventa |
            # Usa regex per rilevare qualsiasi spazio tra | e | all'inizio
            if '|' in line and ('Status' in line or '**ID**' in line) and 'ID' in line and '---' not in line:
                if re.match(r'^\|\s+\|', line):
                    # Ha colonna vuota iniziale - rimuovila completamente
                    in_table_to_fix = True
                    table_lines_to_fix = []
                    # Rimuove la colonna vuota iniziale dall'header: |\s+| diventa |
                    fixed_line = re.sub(r'^\|\s+\|', '|', line)
                    table_lines_to_fix.append(fixed_line)
                    continue
                else:
                    skip_table = False
                    in_table_to_fix = False
                    table_lines_to_fix = []
            
            # Se siamo in una tabella da correggere, aggiungi le righe alla lista
            if in_table_to_fix:
                if '|' in line:
                    # Rimuove la colonna vuota iniziale dalle righe dati: |\s+| diventa | (usa regex)
                    fixed_line = re.sub(r'^\|\s+\|', '|', line)
                    table_lines_to_fix.append(fixed_line)
                    continue
                elif line.strip() == '':
                    # Fine della tabella, aggiungi le righe corrette
                    if table_lines_to_fix:
                        cleaned_lines_after.extend(table_lines_to_fix)
                    cleaned_lines_after.append(line)
                    in_table_to_fix = False
                    table_lines_to_fix = []
                    continue
            
            # Se siamo in una tabella da saltare, continua a saltare fino alla fine
            if skip_table:
                if '|' in line:
                    continue
                elif line.strip() == '':
                    # Fine della tabella, smetti di saltare
                    skip_table = False
                    cleaned_lines_after.append(line)
                    continue
            
            if not skip_table and not in_table_to_fix:
                cleaned_lines_after.append(line)
        
        # Aggiungi eventuali righe rimanenti della tabella da correggere
        if table_lines_to_fix:
            cleaned_lines_after.extend(table_lines_to_fix)
        
        body_after = '\n'.join(cleaned_lines_after)
    
    # Rimuove eventuali sezioni "Requisiti modificati" o "Modified Requirements" esistenti dal body_after
    # per evitare duplicazioni quando viene aggiunta la nuova sezione
    body_after_lines = body_after.split('\n')
    cleaned_body_after_lines = []
    skip_modified_section = False
    for i, line in enumerate(body_after_lines):
        # Rileva l'inizio di una sezione "Requisiti modificati" o "Modified Requirements"
        if (line.startswith('### 🔄 Requisiti modificati') or 
            line.startswith('### 🔄 Modified Requirements') or
            'Requisiti modificati in ARF' in line or
            'Modified Requirements in ARF' in line):
            # Salta questa sezione e tutto fino alla prossima sezione ## o fine
            skip_modified_section = True
            continue
        elif skip_modified_section:
            # Continua a saltare fino a una riga vuota seguita da una sezione ## o fine
            if line.strip() == '':
                # Verifica se la prossima riga è una sezione ##
                if i + 1 < len(body_after_lines) and body_after_lines[i+1].startswith('##'):
                    skip_modified_section = False
                    cleaned_body_after_lines.append(line)
                elif i + 1 >= len(body_after_lines):
                    # Fine del body
                    skip_modified_section = False
            elif line.startswith('##'):
                # Nuova sezione - smetti di saltare
                skip_modified_section = False
                cleaned_body_after_lines.append(line)
        else:
            cleaned_body_after_lines.append(line)
    
    body_after = '\n'.join(cleaned_body_after_lines)
    
    # Costruisce il new_body con la sezione diff prima della tabella
    # Assicura che la tabella parta da una nuova riga
    # Includi modified_section solo se non è vuota (cioè se ci sono requisiti modificati)
    # Se la sezione diff contiene "No changes detected", non includere modified_section
    if "No changes detected" in diff_section:
        modified_section = ""  # Non includere la sezione se non ci sono modifiche
    
    new_body = body_before_cleaned + diff_section + new_table
    if modified_section:
        new_body += '\n\n' + modified_section
    new_body += body_after
    
    # RIMUOVE colonna vuota iniziale da TUTTE le righe della tabella nel new_body finale
    # Applica la correzione anche a eventuali tabelle che non sono state corrette prima
    # Usa regex per rimuovere qualsiasi spazio tra | e | all'inizio
    new_body_lines = new_body.split('\n')
    new_body_cleaned_lines = []
    in_table_to_fix_final = False
    table_lines_to_fix_final = []
    
    # Semplifica: correggi solo le righe con colonna vuota iniziale, senza logica complessa che spezza le tabelle
    for line in new_body_lines:
        # Rimuove colonna vuota iniziale solo se presente: |\s+| diventa |
        # Ma solo se la riga inizia effettivamente con | seguito da spazi e poi |
        if re.match(r'^\|\s+\|', line):
            # Ha colonna vuota iniziale - rimuovila
            cleaned_line = re.sub(r'^\|\s+\|', '|', line)
            new_body_cleaned_lines.append(cleaned_line)
        else:
            new_body_cleaned_lines.append(line)
    
    new_body = '\n'.join(new_body_cleaned_lines)
    
    # Aggiorna i riferimenti alla versione ARF nel body
    new_body = re.sub(
        r'Summary of Changes (with |in )?ARF 2\.5\.0',
        'Summary of Changes in ARF 2.7.3',
        new_body,
        flags=re.IGNORECASE
    )
    new_body = re.sub(
        r'UPDATED TO ARF 2\.5\.0',
        'UPDATED TO ARF 2.7.3',
        new_body,
        flags=re.IGNORECASE
    )
    # Sostituisce solo se non contiene già "to ARF 2.7.3" per evitare duplicazioni
    new_body = re.sub(
        r'what has changed from ARF 2\.5\.0(?! to ARF 2\.7\.3)',
        'what has changed from ARF 2.5.0 to ARF 2.7.3',
        new_body,
        flags=re.IGNORECASE
    )
    # Rimuove eventuali duplicazioni "to ARF 2.7.3 to ARF 2.7.3..."
    new_body = re.sub(
        r'to ARF 2\.7\.3(\s+to ARF 2\.7\.3)+',
        'to ARF 2.7.3',
        new_body,
        flags=re.IGNORECASE
    )
    
    # Verifica che la nuova tabella generata contenga effettivamente una tabella valida
    # Cerca pattern più robusti per identificare tabelle markdown nel new_body
    has_table_in_new_body = False
    new_body_lines = new_body.split('\n')
    for i, line in enumerate(new_body_lines):
        if '|' in line:
            # Verifica se è un header di tabella
            if re.search(r'\|\s*[^\n]*(ID|Status|Requirement|Specification|Index)[^\n]*\|', line, re.IGNORECASE):
                has_table_in_new_body = True
                break
            # Verifica se ci sono almeno 2 righe consecutive con |
            if i < len(new_body_lines) - 1 and new_body_lines[i+1].strip().startswith('|'):
                # Verifica che non sia solo un separatore
                if '---' not in line or '---' not in new_body_lines[i+1]:
                    has_table_in_new_body = True
                    break
    
    if not has_table_in_new_body:
        print(f"   ⚠️  Issue #{issue.number}: La tabella generata non contiene una tabella valida - preview non generato")
        # Ritorna None con un flag speciale che indica che la tabella generata non è valida
        # Questo verrà gestito nel main() per determinare il motivo corretto
        return None
    
    # Salva il preview
    safe_name = re.sub(r'[^\w\s-]', '', issue.title).strip().replace(' ', '_')
    preview_path = output_dir / f"issue_{issue.number}_{safe_name}.md"
    
    with open(preview_path, 'w', encoding='utf-8') as f:
        f.write(f"# Preview: Issue #{issue.number} - {issue.title}\n\n")
        f.write(f"**Topic:** {topic}\n\n")
        f.write(f"**Requirements ARF 2.5.0:** {len(existing_reqs)}\n")
        f.write(f"**Requirements ARF 2.7.3:** {len(topic_requirements)}\n\n")
        f.write("---\n\n")
        f.write(diff_report)
        f.write("---\n\n")
        f.write("## Nuovo body completo della issue:\n\n")
        f.write(new_body)
        f.write("\n\n---\n")
    
    return preview_path


def update_issue_table(issue: IssueInfo, requirements: List[Dict], repo: str = "italia/eid-wallet-it-docs", 
                      preview_body: Optional[str] = None) -> Optional[bool]:
    """
    Aggiorna la tabella markdown esistente nella issue con i nuovi requisiti ARF 2.7.3.
    Ritorna True se aggiornata con successo, False se errore, None se saltata.
    """
    # Se è stato fornito un preview_body, usalo direttamente
    if preview_body:
        new_body = preview_body
    else:
        # Estrae il topic dalla title
        topic = extract_topic_from_issue_title(issue.title)
        if not topic:
            print(f"⚠️  Non riesco a estrarre il topic dalla title: {issue.title}")
            return False
        
        # Trova i requisiti per questo topic
        topic_requirements = find_requirements_for_topic(topic, requirements)
        if not topic_requirements:
            print(f"⚠️  Nessun requisito trovato per: {topic}")
            return False
        
        print(f"   📋 Trovati {len(topic_requirements)} requisiti per {topic}")
        
        # Estrae la tabella esistente
        existing_table, start_pos, end_pos = extract_existing_table(issue.body, issue.number)
        
        if not existing_table or start_pos is None:
            print(f"   ⚠️  Issue #{issue.number}: Nessuna tabella esistente trovata - saltata")
            return False
        
        # Estrae la tabella esistente per preservare il formato
        existing_table_for_format, _, _ = extract_existing_table(issue.body, issue.number)
        
        if not existing_table_for_format:
            print(f"   ⚠️  Issue #{issue.number}: Impossibile estrarre la tabella per preservare il formato")
            return False
        
        # Genera la nuova tabella preservando gli status esistenti e l'ordine delle colonne
        new_table = generate_requirement_table(topic_requirements, preserve_existing_status=True, 
                                              existing_body=issue.body, existing_table=existing_table_for_format)
        
        # Analizza la tabella esistente per generare il report delle modifiche
        existing_reqs = parse_existing_table(existing_table_for_format)
        
        # Assicura che il testo prima della tabella finisca con una nuova riga vuota
        body_before = issue.body[:start_pos].rstrip()
        
        # Rimuove eventuali sezioni "Diff ARF 2.5.0 → ARF 2.7.3" esistenti dal body_before
        # per evitare duplicazioni quando viene aggiunta la nuova sezione
        lines_before = body_before.split('\n')
        cleaned_lines_no_diff = []
        skip_until_empty = False
        for i, line in enumerate(lines_before):
            if line.startswith('## Diff ARF 2.5.0 → ARF 2.7.3'):
                # Salta questa sezione e tutto fino alla prossima sezione ## o fine
                skip_until_empty = True
                continue
            elif skip_until_empty:
                # Continua a saltare fino a una riga vuota seguita da una sezione ## o fine
                if line.strip() == '':
                    # Verifica se la prossima riga è una sezione ##
                    if i + 1 < len(lines_before) and lines_before[i+1].startswith('##'):
                        skip_until_empty = False
                        cleaned_lines_no_diff.append(line)
                    elif i + 1 >= len(lines_before):
                        # Fine del body
                        skip_until_empty = False
                elif line.startswith('##'):
                    # Nuova sezione - smetti di saltare
                    skip_until_empty = False
                    cleaned_lines_no_diff.append(line)
            else:
                cleaned_lines_no_diff.append(line)
        
        body_before = '\n'.join(cleaned_lines_no_diff)
        
        if body_before and not body_before.endswith('\n\n'):
            # Aggiunge una nuova riga vuota se non c'è già
            if body_before.endswith('\n'):
                body_before += '\n'
            else:
                body_before += '\n\n'
        
        # Genera la sezione "Diff ARF 2.5.0 → ARF 2.7.3" completa da includere prima della tabella
        # Usa generate_diff_report per ottenere il contenuto completo (non solo l'header)
        diff_report = generate_diff_report(existing_reqs, topic_requirements, existing_table_for_format)
        # Estrae solo la sezione "Diff ARF 2.5.0 → ARF 2.7.3" dal diff_report (senza "Total requirements" finale)
        diff_lines = diff_report.split('\n')
        diff_section_lines = []
        in_diff_section = False
        for line in diff_lines:
            if line.startswith('## Diff ARF 2.5.0 → ARF 2.7.3'):
                if not in_diff_section:  # Evita duplicati
                    in_diff_section = True
                    diff_section_lines.append(line)
            elif in_diff_section:
                # Ferma quando trova "Total requirements" o fine del report
                if line.startswith('**Total requirements') or line.startswith('**Totale requisiti'):
                    break
                diff_section_lines.append(line)
        diff_section = '\n'.join(diff_section_lines) + '\n\n' if diff_section_lines else "## Diff ARF 2.5.0 → ARF 2.7.3\n\n"
        
        # Genera la sezione "Modified Requirements in ARF 2.7.3"
        modified_section = generate_modified_requirements_section(existing_reqs, topic_requirements)
        
        # Rimuove eventuali sezioni "Requisiti modificati" o "Modified Requirements" esistenti dal body_after
        # per evitare duplicazioni quando viene aggiunta la nuova sezione
        body_after_raw = issue.body[end_pos:].lstrip()
        body_after_lines = body_after_raw.split('\n')
        cleaned_body_after_lines = []
        skip_modified_section = False
        for i, line in enumerate(body_after_lines):
            # Rileva l'inizio di una sezione "Requisiti modificati" o "Modified Requirements"
            if (line.startswith('### 🔄 Requisiti modificati') or 
                line.startswith('### 🔄 Modified Requirements') or
                'Requisiti modificati in ARF' in line or
                'Modified Requirements in ARF' in line):
                # Salta questa sezione e tutto fino alla prossima sezione ## o fine
                skip_modified_section = True
                continue
            elif skip_modified_section:
                # Continua a saltare fino a una riga vuota seguita da una sezione ## o fine
                if line.strip() == '':
                    # Verifica se la prossima riga è una sezione ##
                    if i + 1 < len(body_after_lines) and body_after_lines[i+1].startswith('##'):
                        skip_modified_section = False
                        cleaned_body_after_lines.append(line)
                    elif i + 1 >= len(body_after_lines):
                        # Fine del body
                        skip_modified_section = False
                elif line.startswith('##'):
                    # Nuova sezione - smetti di saltare
                    skip_modified_section = False
                    cleaned_body_after_lines.append(line)
            else:
                cleaned_body_after_lines.append(line)
        
        body_after = '\n'.join(cleaned_body_after_lines)
        
        # Sostituisce la tabella nel body e aggiunge la sezione diff prima e modified dopo
        # Includi modified_section solo se non è vuota (cioè se ci sono requisiti modificati)
        # Se la sezione diff contiene "No changes detected", non includere modified_section
        if "No changes detected" in diff_section:
            modified_section = ""  # Non includere la sezione se non ci sono modifiche
        
        new_body = body_before + diff_section + new_table
        if modified_section:
            new_body += '\n\n' + modified_section
        new_body += body_after
        
        # Aggiorna i riferimenti alla versione ARF nel body
        new_body = re.sub(
            r'Summary of Changes (with |in )?ARF 2\.5\.0',
            'Summary of Changes in ARF 2.7.3',
            new_body,
            flags=re.IGNORECASE
        )
        new_body = re.sub(
            r'UPDATED TO ARF 2\.5\.0',
            'UPDATED TO ARF 2.7.3',
            new_body,
            flags=re.IGNORECASE
        )
        # Sostituisce solo se non contiene già "to ARF 2.7.3" per evitare duplicazioni
        new_body = re.sub(
            r'what has changed from ARF 2\.5\.0(?! to ARF 2\.7\.3)',
            'what has changed from ARF 2.5.0 to ARF 2.7.3',
            new_body,
            flags=re.IGNORECASE
        )
        # Rimuove eventuali duplicazioni "to ARF 2.7.3 to ARF 2.7.3..."
        new_body = re.sub(
            r'to ARF 2\.7\.3(\s+to ARF 2\.7\.3)+',
            'to ARF 2.7.3',
            new_body,
            flags=re.IGNORECASE
        )
    
    # Aggiorna la issue
    success, output = run_gh_command([
        'issue', 'edit', str(issue.number),
        '--repo', repo,
        '--body', new_body
    ])
    
    if success:
        print(f"   ✅ Issue #{issue.number} aggiornata")
        return True
    else:
        print(f"   ❌ Errore nell'aggiornamento della issue #{issue.number}: {output}")
        return False


def main():
    """Funzione principale"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Aggiorna le GitHub issues con i requisiti ARF')
    parser.add_argument('--preview-only', action='store_true', 
                       help='Genera solo i file di preview senza aggiornare le issues')
    parser.add_argument('--apply', action='store_true',
                       help='Applica le modifiche dai file di preview')
    parser.add_argument('--preview-dir', type=str, default=None,
                       help='Directory per i file di preview (default: utils/arf_requirements/previews)')
    args = parser.parse_args()
    
    # Carica i requisiti
    requirements_path = Path(__file__).parent / 'arf_requirements' / 'requirements.json'
    if not requirements_path.exists():
        print(f"❌ File non trovato: {requirements_path}")
        print("   Esegui prima: python3 utils/analyze_arf_requirements.py")
        sys.exit(1)
    
    with open(requirements_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Usa i requisiti by_topic
    requirements = data.get('by_topic', [])
    if not requirements:
        print("❌ Nessun requisito trovato nel file JSON")
        sys.exit(1)
    
    print(f"📋 Caricati {len(requirements)} requisiti")
    
    # Directory per i preview
    if args.preview_dir:
        preview_dir = Path(args.preview_dir)
    else:
        preview_dir = Path(__file__).parent / 'arf_requirements' / 'previews'
    preview_dir.mkdir(parents=True, exist_ok=True)
    
    # Ottiene la issue parent #545
    parent_issue = get_issue(545)
    if not parent_issue:
        print("❌ Impossibile recuperare la issue #545")
        sys.exit(1)
    
    print(f"📌 Issue parent: #{parent_issue.number} - {parent_issue.title}")
    
    # Ottiene le sub-issues
    print("\n🔍 Ricerca delle sub-issues...")
    sub_issues = get_sub_issues(545)
    
    if not sub_issues:
        print("\n⚠️  Nessuna sub-issue trovata automaticamente.")
        print("   Puoi specificare manualmente i numeri delle issues da aggiornare.")
        manual_input = input("\nInserisci i numeri delle issues da aggiornare (separati da virgola): ")
        if manual_input.strip():
            issue_numbers = [int(n.strip()) for n in manual_input.split(',') if n.strip().isdigit()]
            sub_issues = []
            for num in issue_numbers:
                issue = get_issue(num)
                if issue:
                    sub_issues.append(issue)
        else:
            print("❌ Nessuna issue specificata. Uscita.")
            sys.exit(1)
    
    # Mostra le sub-issues trovate
    repo = "italia/eid-wallet-it-docs"
    print("\n📋 Sub-issues trovate:")
    for sub_issue in sub_issues:
        issue_url = f"https://github.com/{repo}/issues/{sub_issue.number}"
        print(f"   #{sub_issue.number}: {sub_issue.title}")
        print(f"      🔗 {issue_url}")
    
    # Modalità preview
    if args.preview_only or not args.apply:
        print(f"\n📝 Generazione preview in: {preview_dir}")
        
        preview_files = []
        skipped_issues = []  # Lista delle issues saltate con motivo
        
        for sub_issue in sub_issues:
            print(f"\n📄 Generazione preview per issue #{sub_issue.number}...")
            preview_path = generate_preview(sub_issue, requirements, preview_dir)
            if preview_path:
                preview_files.append(str(preview_path))
                print(f"   ✅ Preview salvato: {preview_path}")
            else:
                # Determina il motivo per cui è stata saltata
                topic = extract_topic_from_issue_title(sub_issue.title)
                if not topic:
                    reason = "Impossibile estrarre il topic dal titolo"
                else:
                    topic_requirements = find_requirements_for_topic(topic, requirements)
                    if not topic_requirements:
                        reason = f"Nessun requisito trovato per topic: {topic}"
                    else:
                        existing_table, start_pos, end_pos = extract_existing_table(sub_issue.body, sub_issue.number)
                        if not existing_table or start_pos is None:
                            reason = "Nessuna tabella esistente trovata nel body"
                        else:
                            # Verifica se la tabella generata sarebbe valida
                            # Prova a generare la tabella per vedere se contiene una tabella valida
                            try:
                                test_table = generate_requirement_table(topic_requirements, preserve_existing_status=True, 
                                                                        existing_body=sub_issue.body, existing_table=existing_table)
                                # Verifica se la tabella generata contiene una tabella valida
                                has_table = False
                                test_lines = test_table.split('\n')
                                for i, line in enumerate(test_lines):
                                    if '|' in line:
                                        if re.search(r'\|\s*[^\n]*(ID|Status|Requirement|Specification|Index)[^\n]*\|', line, re.IGNORECASE):
                                            has_table = True
                                            break
                                        if i < len(test_lines) - 1 and test_lines[i+1].strip().startswith('|'):
                                            if '---' not in line or '---' not in test_lines[i+1]:
                                                has_table = True
                                                break
                                
                                # Verifica anche nel new_body completo (dopo la sostituzione)
                                body_before = sub_issue.body[:start_pos]
                                body_after = sub_issue.body[end_pos:].lstrip()
                                from update_github_issues import generate_modified_requirements_section, parse_existing_table
                                existing_reqs = parse_existing_table(existing_table)
                                modified_section = generate_modified_requirements_section(existing_reqs, topic_requirements)
                                test_new_body = body_before + test_table + '\n\n' + modified_section + body_after
                                
                                # Verifica se il new_body completo contiene una tabella
                                has_table_in_body = False
                                test_body_lines = test_new_body.split('\n')
                                for i, line in enumerate(test_body_lines):
                                    if '|' in line:
                                        if re.search(r'\|\s*[^\n]*(ID|Status|Requirement|Specification|Index)[^\n]*\|', line, re.IGNORECASE):
                                            has_table_in_body = True
                                            break
                                        if i < len(test_body_lines) - 1 and test_body_lines[i+1].strip().startswith('|'):
                                            if '---' not in line or '---' not in test_body_lines[i+1]:
                                                has_table_in_body = True
                                                break
                                
                                if not has_table:
                                    reason = "La tabella generata non contiene una tabella valida"
                                elif not has_table_in_body:
                                    reason = "Il body completo generato non contiene una tabella valida"
                                else:
                                    reason = "Motivo sconosciuto (tabella generata valida ma preview non creato)"
                            except Exception as e:
                                reason = f"Errore durante la verifica della tabella: {str(e)}"
                
                skipped_issues.append({
                    'number': sub_issue.number,
                    'title': sub_issue.title,
                    'reason': reason
                })
                print(f"   ⚠️  Preview non generato per issue #{sub_issue.number}: {reason}")
        
        print(f"\n✅ Generati {len(preview_files)} file di preview")
        
        # Report completo: issues processate con successo
        print(f"\n📊 Riepilogo completo:")
        print(f"   ✅ Issues processate con successo: {len(preview_files)}")
        print(f"   ⚠️  Issues saltate: {len(skipped_issues)}")
        print(f"   📋 Totale issues: {len(sub_issues)}")
        
        # Report dettagliato delle issues saltate
        if skipped_issues:
            print(f"\n⚠️  Issues saltate durante la generazione del preview ({len(skipped_issues)}):")
            print("   " + "="*80)
            for skipped in skipped_issues:
                issue_url = f"https://github.com/{repo}/issues/{skipped['number']}"
                print(f"   ❌ Issue #{skipped['number']}: {skipped['title']}")
                print(f"      🔗 {issue_url}")
                print(f"      📋 Motivo: {skipped['reason']}")
                print()
        else:
            print(f"\n✅ Nessuna issue saltata - tutti i preview generati con successo!")
        
        # Report delle issues processate con successo (opzionale, solo se richiesto)
        if preview_files:
            print(f"\n✅ Issues processate con successo ({len(preview_files)}):")
            print("   " + "="*80)
            # Estrae i numeri delle issues dai nomi dei file
            processed_numbers = []
            for pf in preview_files:
                match = re.search(r'issue_(\d+)_', pf)
                if match:
                    processed_numbers.append(int(match.group(1)))
            
            # Ordina e mostra
            for num in sorted(processed_numbers):
                # Trova l'issue corrispondente
                issue = next((i for i in sub_issues if i.number == num), None)
                if issue:
                    issue_url = f"https://github.com/{repo}/issues/{num}"
                    print(f"   ✅ Issue #{num}: {issue.title[:70]}...")
                    print(f"      🔗 {issue_url}")
        
        print(f"\n📂 Rivedi i file in: {preview_dir}")
        if args.preview_only:
            print("\nPer applicare le modifiche, esegui:")
            print("   python3 utils/update_github_issues.py --apply")
        else:
            response = input(f"\nVuoi procedere con l'aggiornamento di {len(preview_files)} issue? (s/n): ")
            if response.lower() not in ['s', 'si', 'y', 'yes']:
                print("❌ Operazione annullata.")
                print("   Puoi applicare le modifiche in seguito con: python3 utils/update_github_issues.py --apply")
                sys.exit(0)
            
            # Applica le modifiche
            updated = 0
            failed = 0
            skipped = 0
            
            for preview_file in preview_files:
                match = re.search(r'issue_(\d+)_', Path(preview_file).name)
                if not match:
                    skipped += 1
                    continue
                
                issue_number = int(match.group(1))
                issue = get_issue(issue_number)
                if not issue:
                    failed += 1
                    continue
                
                with open(preview_file, 'r', encoding='utf-8') as f:
                    preview_content = f.read()
                
                body_match = re.search(r'## Nuovo body della issue:\n\n(.*?)\n\n---', preview_content, re.DOTALL)
                if not body_match:
                    failed += 1
                    continue
                
                new_body = body_match.group(1).strip()
                
                print(f"\n📝 Aggiornamento issue #{issue.number}: {issue.title[:60]}...")
                result = update_issue_table(issue, requirements, preview_body=new_body)
                if result:
                    updated += 1
                elif result is False:
                    failed += 1
                else:
                    skipped += 1
            
            print(f"\n✅ Completato: {updated} aggiornate, {failed} fallite, {skipped} saltate")
        
        return
    
    # Modalità apply: legge i preview e applica le modifiche
    if args.apply:
        print("\n📤 Applicazione delle modifiche dai file di preview...")
        
        # Trova tutti i file di preview
        preview_files = list(preview_dir.glob("issue_*.md"))
        if not preview_files:
            print(f"❌ Nessun file di preview trovato in: {preview_dir}")
            print("   Genera prima i preview con: python3 utils/update_github_issues.py --preview-only")
            sys.exit(1)
        
        print(f"📋 Trovati {len(preview_files)} file di preview")
        
        # Chiedi conferma
        response = input(f"\nVuoi procedere con l'aggiornamento di {len(preview_files)} issue? (s/n): ")
        if response.lower() not in ['s', 'si', 'y', 'yes']:
            print("❌ Operazione annullata.")
            sys.exit(0)
        
        updated = 0
        failed = 0
        skipped = 0
        
        for preview_file in preview_files:
            # Estrae il numero della issue dal nome del file
            match = re.search(r'issue_(\d+)_', preview_file.name)
            if not match:
                print(f"⚠️  Impossibile estrarre il numero della issue da: {preview_file.name}")
                skipped += 1
                continue
            
            issue_number = int(match.group(1))
            issue = get_issue(issue_number)
            if not issue:
                print(f"❌ Impossibile recuperare issue #{issue_number}")
                failed += 1
                continue
            
            # Legge il preview e estrae il nuovo body
            with open(preview_file, 'r', encoding='utf-8') as f:
                preview_content = f.read()
            
            # Estrae il nuovo body dalla sezione "## Nuovo body della issue:" o "## Nuovo body completo della issue:"
            # Il body termina con "\n\n---" alla fine del file (separatore finale)
            # Prova prima il pattern che cerca fino a "\n\n---\n" alla fine
            body_match = re.search(r'## Nuovo body (completo della |della )?issue:\n\n(.*?)(?=\n\n---\s*\Z|\Z)', preview_content, re.DOTALL)
            
            if not body_match:
                # Pattern alternativo: tutto fino alla fine del file, poi rimuove "---" finale
                body_match = re.search(r'## Nuovo body (completo della |della )?issue:\n\n(.*)', preview_content, re.DOTALL)
                if body_match:
                    # Rimuove eventuali "---" finali e spazi
                    new_body = body_match.group(2).strip()
                    new_body = re.sub(r'\n\n---\s*$', '', new_body)
                else:
                    print(f"⚠️  Formato preview non valido per: {preview_file.name}")
                    print(f"   Il file potrebbe essere stato generato con una versione precedente dello script.")
                    print(f"   Rigenera i preview con: python3 utils/update_github_issues.py --preview-only")
                    failed += 1
                    continue
            else:
                # Il gruppo 2 contiene il body (dopo "issue:\n\n")
                new_body = body_match.group(2).strip()
                # Rimuove eventuali "---" finali rimasti
                new_body = re.sub(r'\n\n---\s*$', '', new_body)
            
            # Verifica che il nuovo body contenga una tabella
            # Cerca pattern più robusti per identificare tabelle markdown
            # Pattern 1: riga con | che contiene "ID", "Status", "Requirement", "Specification", o "Index"
            # Pattern 2: almeno 2 righe consecutive che iniziano con |
            has_table = False
            lines = new_body.split('\n')
            for i, line in enumerate(lines):
                if '|' in line:
                    # Verifica se è un header di tabella
                    if re.search(r'\|\s*[^\n]*(ID|Status|Requirement|Specification|Index)[^\n]*\|', line, re.IGNORECASE):
                        has_table = True
                        break
                    # Verifica se ci sono almeno 2 righe consecutive con |
                    if i < len(lines) - 1 and lines[i+1].strip().startswith('|'):
                        # Verifica che non sia solo un separatore
                        if '---' not in line or '---' not in lines[i+1]:
                            has_table = True
                            break
            
            if not has_table:
                print(f"⚠️  Issue #{issue_number}: Il preview non contiene una tabella valida - saltata")
                skipped += 1
                continue
            
            print(f"\n📝 Aggiornamento issue #{issue.number}: {issue.title[:60]}...")
            result = update_issue_table(issue, requirements, preview_body=new_body)
            if result is True:
                updated += 1
            elif result is False:
                # False significa che c'è stato un errore
                failed += 1
            else:
                # None significa che è stata saltata (non dovrebbe accadere con preview_body)
                skipped += 1
                print(f"   ⚠️  Issue #{issue.number} saltata (caso inatteso)")
        
        print(f"\n✅ Completato: {updated} aggiornate, {failed} fallite, {skipped} saltate")
        return


if __name__ == '__main__':
    main()

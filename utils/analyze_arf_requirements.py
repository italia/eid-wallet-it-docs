#!/usr/bin/env python3
"""
Script per analizzare i file annex-2.0* e estrarre i requisiti ARF.
Genera tabelle markdown per aggiornare le sub-issues su GitHub.
"""

import re
import json
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass, asdict


@dataclass
class Requirement:
    """Rappresenta un requisito ARF"""
    identifier: str  # Es: OIA_01, AS-WP-06-001
    legacy_identifier: Optional[str] = None  # Es: RPA_01 per AS-WP-06-001
    description: str = ""
    notes: str = ""
    topic: Optional[str] = None
    category: Optional[str] = None


def parse_markdown_table_line(line: str) -> Optional[Tuple[str, str, str, str]]:
    """
    Estrae i dati da una riga di tabella markdown.
    Formato: | identifier | legacy_id | description | notes |
    """
    # Rimuove spazi iniziali/finali e separa per |
    parts = [p.strip() for p in line.split('|')]
    # Rimuove parti vuote all'inizio/fine
    parts = [p for p in parts if p]
    
    if len(parts) < 2:
        return None
    
    # Estrae identifier (prima colonna)
    identifier = parts[0].strip('*').strip()
    
    # Se ci sono almeno 3 colonne, la seconda è legacy_identifier, la terza è description
    if len(parts) >= 3:
        legacy_identifier = parts[1].strip('*').strip() if parts[1].strip() != '--' else None
        description = parts[2].strip('*').strip()
        notes = parts[3].strip('*').strip() if len(parts) > 3 else ""
    else:
        # Formato alternativo: | identifier | description |
        legacy_identifier = None
        description = parts[1].strip('*').strip()
        notes = ""
    
    # Pulisce i valori
    if identifier == '--' or identifier.startswith('**'):
        return None
    
    return (identifier, legacy_identifier, description, notes)


def extract_requirements_from_file(file_path: Path) -> List[Requirement]:
    """
    Estrae tutti i requisiti da un file markdown annex-2.0*
    """
    requirements = []
    current_topic = None
    current_category = None
    in_table = False
    
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    for i, line in enumerate(lines):
        # Rileva i topic (per annex-2.02)
        topic_match = re.search(r'####?\s+A\.2\.3\.(\d+)\s+Topic\s+(\d+)\s*[-–]\s*(.+)', line)
        if topic_match:
            current_topic = f"Topic {topic_match.group(2)} - {topic_match.group(3).strip()}"
            continue
        
        # Rileva le categorie (per annex-2.03)
        category_match = re.search(r'###\s+(\d+)\.\s+(.+)', line)
        if category_match:
            current_category = category_match.group(2).strip()
            continue
        
        # Rileva l'inizio di una tabella
        if '| **Index**' in line or '| **Identifier**' in line:
            in_table = True
            continue
        
        # Rileva la fine di una tabella (riga separatore o nuova sezione)
        if in_table and (line.strip().startswith('####') or line.strip().startswith('###') or 
                         (line.strip() == '' and i < len(lines) - 1 and 
                          not lines[i+1].strip().startswith('|'))):
            in_table = False
            continue
        
        # Se siamo in una tabella, estrae i requisiti
        if in_table and line.strip().startswith('|') and '--' not in line:
            parsed = parse_markdown_table_line(line)
            if parsed:
                identifier, legacy_identifier, description, notes = parsed
                
                # Salta se è una riga vuota o header
                if not identifier or identifier.startswith('**'):
                    continue
                
                req = Requirement(
                    identifier=identifier,
                    legacy_identifier=legacy_identifier if legacy_identifier and legacy_identifier != '--' else None,
                    description=description,
                    notes=notes,
                    topic=current_topic,
                    category=current_category
                )
                requirements.append(req)
    
    return requirements


def generate_markdown_table(requirements: List[Requirement], include_status: bool = True) -> str:
    """
    Genera una tabella markdown con i requisiti nel formato per le GitHub issues.
    Include colonna Status se richiesto.
    """
    lines = []
    
    if include_status:
        lines.append("| **Requirement ID** | **Legacy ID** | **Description** | **Status** |")
        lines.append("|-------------------|---------------|------------------|------------|")
    else:
        lines.append("| **Requirement ID** | **Legacy ID** | **Description** |")
        lines.append("|-------------------|---------------|------------------|")
    
    for req in requirements:
        # Pulisce la descrizione per la tabella (rimuove newline)
        desc = req.description.replace('\n', ' ').strip()
        # Limita la lunghezza se troppo lunga
        if len(desc) > 200:
            desc = desc[:197] + "..."
        
        legacy_id = req.legacy_identifier or ""
        status = "🟡" if include_status else ""
        
        if include_status:
            lines.append(f"| {req.identifier} | {legacy_id} | {desc} | {status} |")
        else:
            lines.append(f"| {req.identifier} | {legacy_id} | {desc} |")
    
    return "\n".join(lines)


def main():
    """Funzione principale"""
    # Percorsi dei file
    base_path = Path("/home/wert/DEV/DTD/Wallet/eudi-doc-architecture-and-reference-framework/docs/annexes/annex-2")
    
    files = {
        'by_topic': base_path / 'annex-2.02-high-level-requirements-by-topic.md',
        'by_category': base_path / 'annex-2.03-high-level-requirements-by-category.md'
    }
    
    all_requirements = {}
    
    print("Analisi dei file annex-2.0*...")
    
    for file_type, file_path in files.items():
        if not file_path.exists():
            print(f"⚠️  File non trovato: {file_path}")
            continue
        
        print(f"\n📄 Analisi di {file_path.name}...")
        requirements = extract_requirements_from_file(file_path)
        all_requirements[file_type] = requirements
        print(f"   ✅ Trovati {len(requirements)} requisiti")
    
    # Salva i requisiti in JSON per riferimento
    output_dir = Path(__file__).parent / 'arf_requirements'
    output_dir.mkdir(exist_ok=True)
    
    # Converte i requisiti in dizionari per JSON
    requirements_dict = {}
    for file_type, reqs in all_requirements.items():
        requirements_dict[file_type] = [asdict(req) for req in reqs]
    
    json_path = output_dir / 'requirements.json'
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(requirements_dict, f, indent=2, ensure_ascii=False)
    
    print(f"\n💾 Requisiti salvati in: {json_path}")
    
    # Genera esempi di tabelle per topic
    if 'by_topic' in all_requirements:
        print("\n📊 Generazione tabelle per topic...")
        topics = {}
        for req in all_requirements['by_topic']:
            topic = req.topic or "Unknown"
            if topic not in topics:
                topics[topic] = []
            topics[topic].append(req)
        
        # Salva le tabelle per topic
        tables_dir = output_dir / 'tables_by_topic'
        tables_dir.mkdir(exist_ok=True)
        
        for topic, reqs in sorted(topics.items()):
            # Crea un nome file sicuro dal topic
            safe_name = re.sub(r'[^\w\s-]', '', topic).strip().replace(' ', '_')
            table_path = tables_dir / f"{safe_name}.md"
            
            table_content = f"# {topic}\n\n"
            table_content += generate_markdown_table(reqs, include_status=True)
            
            with open(table_path, 'w', encoding='utf-8') as f:
                f.write(table_content)
        
        print(f"   ✅ Tabelle salvate in: {tables_dir}")
    
    # Genera esempi di tabelle per categoria
    if 'by_category' in all_requirements:
        print("\n📊 Generazione tabelle per categoria...")
        categories = {}
        for req in all_requirements['by_category']:
            category = req.category or "Unknown"
            if category not in categories:
                categories[category] = []
            categories[category].append(req)
        
        # Salva le tabelle per categoria
        tables_dir = output_dir / 'tables_by_category'
        tables_dir.mkdir(exist_ok=True)
        
        for category, reqs in sorted(categories.items()):
            # Crea un nome file sicuro dalla categoria
            safe_name = re.sub(r'[^\w\s-]', '', category).strip().replace(' ', '_')
            table_path = tables_dir / f"{safe_name}.md"
            
            table_content = f"# {category}\n\n"
            table_content += generate_markdown_table(reqs, include_status=True)
            
            with open(table_path, 'w', encoding='utf-8') as f:
                f.write(table_content)
        
        print(f"   ✅ Tabelle salvate in: {tables_dir}")
    
    print("\n✅ Analisi completata!")
    print(f"\n📈 Statistiche:")
    if 'by_topic' in all_requirements:
        print(f"   - Requisiti per topic: {len(all_requirements['by_topic'])}")
    if 'by_category' in all_requirements:
        print(f"   - Requisiti per categoria: {len(all_requirements['by_category'])}")


if __name__ == '__main__':
    main()

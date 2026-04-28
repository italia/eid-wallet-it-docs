"""
Script to generate the main index.html by scanning the directory structure.

This script:
1. Scans the current directory for documentation folders
2. Builds a structure of available documentation versions
3. Generates an HTML index with links to all available documentation
"""
import shutil
from datetime import datetime
import logging
from pathlib import Path
from typing import Dict, Any
from jinja2 import Environment, FileSystemLoader
from common_utils import get_github_repo, get_pr_info

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Get GitHub directory path
GITHUB_DIR = Path(__file__).resolve().parent.parent


def scan_directory(base_path: str = '.') -> Dict[str, Any]:
    """Scan the directory structure and return a dictionary with the structure.
    
    Args:
        base_path: Base path to scan
        
    Returns:
        Dictionary with the directory structure
    """
    structure = {
        'versione-corrente': {
            'exists': False,
            'languages': {'it': False, 'en': False}
        },
        'prs': {},
        'releases': {}
    }
    
    base_path = Path(base_path)
    logger.info(f"Scanning directory structure at: {base_path}")
    
    # Check versione-corrente
    versione_corrente_path = base_path / "versione-corrente"
    if versione_corrente_path.exists():
        structure['versione-corrente']['exists'] = True
        
        # Check languages
        for lang in ['it', 'en']:
            lang_path = versione_corrente_path / lang
            index_path = lang_path / "index.html"
            structure['versione-corrente']['languages'][lang] = index_path.exists()
    
    # Check PRs
    prs_path = base_path / "prs"
    if prs_path.exists():
        try:
            pr_dirs = [d for d in prs_path.iterdir() if d.is_dir()]
            
            for pr_dir in pr_dirs:
                pr_dir_name = pr_dir.name
                if not pr_dir_name.startswith('pr'):
                    continue
                    
                languages = {}
                
                # Check languages
                for lang in ['it', 'en']:
                    lang_path = pr_dir / lang
                    index_path = lang_path / "index.html"
                    languages[lang] = index_path.exists()
                
                # Extract PR number and get title
                pr_num = pr_dir_name.replace("pr", "")
                pr_info = get_pr_info(pr_num)
                pr_title = pr_info.get('title', f"PR #{pr_num}") if pr_info else f"PR #{pr_num}"

                # Only add to structure if at least one language has an index.html
                if languages['it'] or languages['en']:
                    structure['prs'][pr_dir_name] = {
                        'languages': languages,
                        'title': pr_title,
                        'number': pr_num  # Store PR number for creating the link
                    }
        except Exception as e:
            logger.error(f"Error scanning PRs: {e}")
    
    # Check Releases
    releases_path = base_path / "releases"
    if releases_path.exists():
        try:
            release_dirs = [d for d in releases_path.iterdir() if d.is_dir()]
            
            for release_dir in release_dirs:
                release_dir_name = release_dir.name
                languages = {}
                
                # Check languages
                for lang in ['it', 'en']:
                    lang_path = release_dir / lang
                    index_path = lang_path / "index.html"
                    languages[lang] = index_path.exists()
                    
                # Only add to structure if at least one language has an index.html
                if languages['it'] or languages['en']:
                    structure['releases'][release_dir_name] = {
                        'languages': languages
                    }
        except Exception as e:
            logger.error(f"Error scanning releases: {e}")
    
    return structure


def generate_html(structure: Dict[str, Any]) -> str:
    """Generate HTML content based on the directory structure using external Jinja2 template.
    
    Args:
        structure: Dictionary with the directory structure
        
    Returns:
        HTML content
    """
    # Set up Jinja2 environment with templates directory
    template_dir = GITHUB_DIR / "templates"
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template("index-template.html")
    
    # Prepare template data
    current_date = datetime.now().strftime("%Y-%m-%d")
    repo = get_github_repo() or ""
    
    # Render template
    return template.render(structure=structure, current_date=current_date, repo=repo)


def main() -> None:
    """Main function to scan directories and generate index.html in the GitHub directory level."""
    # Get output directory (GITHUB_DIR)
    output_dir = GITHUB_DIR
    
    # Scan the current directory (we're in the root of gh-pages)
    structure = scan_directory(output_dir)
    logger.info("Directory structure found:")
    logger.info(f"versione-corrente: {structure['versione-corrente']}")
    logger.info(f"PRs: {len(structure['prs'])} found")
    logger.info(f"Releases: {len(structure['releases'])} found")
    
    # Generate HTML content
    html_content = generate_html(structure)
    
    # Write the HTML to index.html in the output directory
    index_path = output_dir / "index.html"
    try:
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(html_content)
        logger.info(f"Generated index.html successfully at {index_path}")
    except Exception as e:
        logger.error(f"Error writing index.html: {e}")


if __name__ == "__main__":
    main()

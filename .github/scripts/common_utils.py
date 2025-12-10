"""
Common utilities for GitHub documentation scripts.
"""
import os
import subprocess
import json
import logging
from typing import Dict, List, Optional, Any, Union

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def run_command(command: str) -> Optional[str]:
    """Run a shell command and return the output.
    
    Args:
        command: Command to execute
        
    Returns:
        Command output if successful, None otherwise
    """
    try:
        result = subprocess.run(
            command, 
            shell=True, 
            check=True, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE,
            text=True  # More readable than universal_newlines
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        logger.error(f"Error executing command: {command}")
        logger.error(f"Error message: {e.stderr}")
        return None


def get_github_repo() -> Optional[str]:
    """Get the GitHub repository from environment variable.
    
    Returns:
        Repository name in format 'owner/repo' or None
    """
    return os.environ.get('GITHUB_REPOSITORY')


def get_pr_info(pr_num: Union[int, str], fields: str = "number,title", repo: Optional[str] = None) -> Optional[Dict[str, Any]]:
    """Get information about a specific PR.
    
    Args:
        pr_num: PR number
        fields: Comma-separated list of fields to retrieve
        repo: Repository in format 'owner/repo'
        
    Returns:
        PR information or None if retrieval failed
    """
    repo_option = f"--repo {repo}" if repo else ""
    command = f"gh pr view {pr_num} --json {fields} {repo_option}"
    
    output = run_command(command)
    if not output:
        return None
    
    try:
        return json.loads(output)
    except json.JSONDecodeError:
        logger.error(f"Failed to parse JSON output: {output}")
        return None


def get_active_pr_numbers(repo: Optional[str] = None) -> List[int]:
    """Get list of active (open) PR numbers using GitHub CLI.
    
    Args:
        repo: Repository in format 'owner/repo'
        
    Returns:
        List of open PR numbers
    """
    repo_option = f"--repo {repo}" if repo else ""
    command = f"gh pr list --state open --json number {repo_option}"
    
    output = run_command(command)
    if not output:
        logger.error("Failed to get list of PRs. Make sure GitHub CLI is installed and authenticated.")
        return []
    
    try:
        prs_data = json.loads(output)
        return [pr['number'] for pr in prs_data]
    except json.JSONDecodeError:
        logger.error(f"Failed to parse JSON output: {output}")
        return []

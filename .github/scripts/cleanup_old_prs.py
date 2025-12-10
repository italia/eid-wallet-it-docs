"""
Script to clean up old PR directories in the gh-pages branch.

This script:
1. Gets a list of active (open) PRs using GitHub CLI
2. Scans the 'prs' directory for PR directories
3. Removes directories for PRs that are no longer active (closed/merged)
"""
import re
import shutil
import logging
import os
import subprocess
from pathlib import Path
from typing import Optional, List, Set

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def get_active_pr_numbers(repo=None) -> Set[int]:
    """Get the PR numbers of all active (open) PRs.
    
    Returns:
        A set of active PR numbers
    """
    try:
        # Fallback to direct GitHub CLI command if repo object is not available
        # This should work in the GitHub Actions environment with GH_TOKEN
        result = subprocess.run(
            ["gh", "pr", "list", "--state", "open", "--json", "number"],
            capture_output=True,
            text=True,
            check=True
        )

        # Try to parse JSON output
        import json
        prs_data = json.loads(result.stdout)
        pr_numbers = {pr['number'] for pr in prs_data}

        # Safety check - if we get 0 PRs, something may be wrong
        if len(pr_numbers) == 0:
            logger.warning("Got 0 active PRs. This might be unexpected - CHECK IF THIS IS CORRECT!")

            # Fall back to a safer behavior - pretend all PRs are active
            logger.info("SAFETY MEASURE: Will not remove any PR directories!")
            return set(range(1, 10000))  # Large range to include all possible PR numbers

        return pr_numbers

    except Exception as e:
        logger.error(f"Error fetching active PRs: {e}")
        logger.info("SAFETY MEASURE: Will not remove any PR directories due to error!")
        # Return a large set to prevent any PR removal
        return set(range(1, 10000))  # Large range to include all possible PR numbers


def extract_pr_number(pr_dir: str) -> Optional[int]:
    """Extract PR number from directory name (e.g., 'pr12' -> 12).
    
    Args:
        pr_dir: PR directory name
        
    Returns:
        PR number if found, None otherwise
    """
    match = re.search(r'pr(\d+)', pr_dir)
    if match:
        return int(match.group(1))
    return None


def clean_old_pr_directories(prs_dir: str = "prs") -> int:
    """Clean up old PR directories.
    
    Args:
        prs_dir: Directory containing PR folders
        
    Returns:
        Number of PR directories removed
    """
    # Check if prs directory exists using Path
    prs_path = Path(prs_dir)
    if not prs_path.is_dir():
        logger.info(f"The '{prs_dir}' directory does not exist. Nothing to clean.")
        return 0

    # Get list of active PR numbers
    logger.info("Getting list of active PRs...")
    active_pr_numbers = get_active_pr_numbers()
    logger.info(f"Active PR numbers: {active_pr_numbers}")

    # SAFETY CHECK: If we got a very large set, it means we're in fallback mode
    # and should not remove any directories
    if len(active_pr_numbers) > 100:  # Arbitrary threshold
        logger.warning("Too many active PRs detected. This is likely a fallback safety measure.")
        logger.info("Skipping cleanup to prevent accidental removal of PR directories.")
        return 0

    # Initialize counter for removed directories
    removed_count = 0

    # Check each PR directory using pathlib
    try:
        # Get all directories in prs_path
        pr_dirs = [d for d in prs_path.iterdir() if d.is_dir()]
    except Exception as e:
        logger.error(f"Error accessing {prs_dir} directory: {e}")
        return 0

    for pr_dir in pr_dirs:
        pr_dir_name = pr_dir.name

        # Skip if not a PR directory pattern
        if not pr_dir_name.startswith('pr'):
            continue

        # Extract PR number
        pr_num = extract_pr_number(pr_dir_name)
        if pr_num is None:
            logger.warning(f"Could not extract PR number from directory: {pr_dir_name}")
            continue

        # Check if PR is active
        if pr_num not in active_pr_numbers:
            logger.info(f"PR #{pr_num} is not active, removing directory {pr_dir}")

            try:
                # Remove the directory and its contents
                if _safe_remove_directory(pr_dir):
                    removed_count += 1
            except Exception as e:
                logger.error(f"Error removing {pr_dir}: {e}")

    logger.info(f"Removed {removed_count} PR directories that were no longer active.")
    return removed_count


def _safe_remove_directory(directory: Path) -> bool:
    """Safely remove a directory by first removing its contents.
    
    Args:
        directory: Path to the directory to remove
        
    Returns:
        True if directory was successfully removed, False otherwise
    """
    try:
        # Remove all files
        for item in directory.rglob("*"):
            if item.is_file():
                try:
                    item.unlink()
                except Exception as e:
                    logger.warning(f"Could not remove file {item}: {e}")

        # Then remove directory
        shutil.rmtree(directory)

        # Verify removal
        if not directory.exists():
            logger.info(f"Successfully removed directory {directory}")
            return True
        else:
            logger.warning(f"Directory {directory} still exists after removal attempt!")
            return False
    except Exception as e:
        logger.error(f"Error during directory removal: {e}")
        return False


if __name__ == "__main__":
    clean_old_pr_directories()

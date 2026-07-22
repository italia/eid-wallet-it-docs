"""Resolve and format release dates for Sphinx PDF title pages."""

from __future__ import annotations

import os
import subprocess
from datetime import date, datetime
from pathlib import Path


def _normalize_iso_date(value: str) -> str:
    value = value.strip()
    if len(value) >= 10 and value[4:5] == '-' and value[7:8] == '-':
        return value[:10]
    try:
        return datetime.fromisoformat(value.replace('Z', '+00:00')).date().isoformat()
    except ValueError:
        return date.today().isoformat()


def _git_tag_date_iso(repo_root: Path) -> str | None:
    try:
        tag = subprocess.run(
            ['git', 'describe', '--tags', '--exact-match', 'HEAD'],
            cwd=repo_root,
            capture_output=True,
            text=True,
            check=False,
        ).stdout.strip()
        if not tag:
            return None
        date_str = subprocess.run(
            ['git', 'log', '-1', '--format=%cs', tag],
            cwd=repo_root,
            capture_output=True,
            text=True,
            check=True,
        ).stdout.strip()
        return date_str or None
    except (OSError, subprocess.SubprocessError):
        return None


def resolve_release_date_iso(repo_root: Path | None = None) -> str:
    """Return YYYY-MM-DD from env override, git tag date, or build date."""
    env_date = os.environ.get('PDF_RELEASE_DATE') or os.environ.get('DOC_RELEASE_DATE')
    if env_date:
        return _normalize_iso_date(env_date)

    if repo_root is not None:
        git_date = _git_tag_date_iso(repo_root)
        if git_date:
            return git_date

    return date.today().isoformat()


def format_release_date(iso_date: str, lang: str) -> str:
    year, month, day = (int(part) for part in iso_date.split('-'))
    if lang == 'it':
        return f'{day:02d}/{month:02d}/{year}'
    return iso_date


def pdf_title_release_date(iso_date: str, lang: str) -> str:
    label = 'Data di rilascio' if lang == 'it' else 'Release date'
    return f'{label}: {format_release_date(iso_date, lang)}'

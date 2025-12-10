# Documentation Build System

This repository contains a comprehensive documentation build system using GitHub Actions workflows to generate HTML documentation for multiple languages, with support for versioning, releases, and pull request previews.

## Overview

The system provides the following functionality:

- **HTML Documentation**: Automatic build and deployment of HTML documentation;
- **Multi-language Support**: Both Italian and English documentation;
- **Release Management**: Dedicated versions for releases;
- **PR Preview System**: Automatic previews for pull requests from the same repository;
- **Fork PR Support**: Manual preview generation for pull requests from forks;
- **Index Page**: Auto-generated index of all available documentation versions.

## Repository Structure

```
├── .github/
│   └── workflows/           # GitHub Actions workflow files
│       ├── build-html.yml           # Main HTML build workflow
│       ├── build-html-manual.yml    # Manual HTML build for fork PRs
│       └── pr-bot-helper.yml        # Fork PR helper bot
├── docs/                    # Documentation source files
│   ├── en/                  # English documentation
│   └── it/                  # Italian documentation
├── scripts/                 # Python utility scripts
│   ├── common_utils.py      # Shared utilities for scripts
│   ├── cleanup_old_prs.py   # Script to remove closed PR previews
│   └── generate_index.py    # Script to generate the index page
├── static/                  # Static assets for the index page
│   └── style.css            # CSS styling for the index page
├── templates/               # HTML templates
│   └── index-template.html  # Template for the index page
└── requirements-dev.txt     # Python dependencies
```

## Workflow Details

### HTML Documentation Build (`build-html.yml`)

This workflow builds and deploys HTML documentation to GitHub Pages.

**Triggers**:
- Push to the `versione-corrente` branch with changes in `docs/`;
- Pull requests (opened, synchronized, reopened) with changes in `docs/`;
- Release publication;
- Manual trigger via GitHub Actions UI.

**Features**:
- Builds both Italian and English documentation;
- Creates different deployment paths for branch pushes, PRs, and releases;
- Removes documentation for closed PRs;
- Auto-generates an index page listing all available documentation versions.

**Usage**:
- For normal development, simply push changes to the `versione-corrente` branch;
- For releases, create a new release in GitHub to trigger the workflow.

### Manual HTML Build for Forks (`build-html-manual.yml`)

This workflow allows repository maintainers to generate documentation previews for pull requests from forks.

**Triggers**:
- Manual trigger via GitHub Actions UI with PR number input.

**Features**:
- Builds both Italian and English documentation;
- Creates different deployment paths for branch pushes, PRs, and releases;
- Removes documentation for closed PRs;
- Auto-generates an index page listing all available documentation versions.

**Usage**:
1. When a PR is created from a fork, the `pr-bot-helper.yml` workflow adds a comment with instructions;
2. A repository maintainer can navigate to the Actions tab, select the "Manual PR Preview" workflow;
3. Enter the PR number and run the workflow;
4. Once completed, the workflow adds a comment to the PR with links to the preview.

### PR Bot for Fork Previews (`pr-bot-helper.yml`)

This workflow adds helpful comments to pull requests from forked repositories.

**Triggers**:
- Pull requests from forks (opened, reopened, synchronized) with changes in `docs/`.

**Features**:
- Adds a comment to the PR with instructions for maintainers to generate a preview.

## Python Scripts

### `generate_index.py`

Generates the main `index.html` page by scanning the available documentation versions.

**Features**:
- Scans the directory structure for documentation folders;
- Creates links to all available documentation versions;
- Uses Jinja2 templates for HTML generation.

### `cleanup_old_prs.py`

Cleans up preview directories for closed pull requests.

**Features**:
- Gets a list of active (open) PRs using GitHub CLI;
- Removes directories for PRs that are no longer active (closed/merged).

### `common_utils.py`

Shared utilities used by the other Python scripts.

**Features**:
- GitHub API integration utilities;
- Command execution helpers;
- PR information retrieval.

## Development Guide

### Creating a Release

1. Ensure your documentation is up to date in the `versione-corrente` branch;

2. Create a new release in GitHub with a tag name (e.g., `v1.0.0`);

3. The workflows will automatically:
   - Build HTML documentation in a dedicated release folder.

## Troubleshooting

### Preview Generation Issues

If PR previews are not generating correctly:

1. Check the workflow run logs for errors;
2. Verify that the PR contains changes in the `docs/` directory;
3. For fork PRs, ensure a maintainer has manually triggered the build.

### Index Page Not Updating

If the index page is not reflecting all available documentation:

1. Check that the generate-index job completed successfully;
2. Verify that the `templates/` and `static/` directories are correctly copied to the output;
3. Try running the workflow manually to regenerate the index.
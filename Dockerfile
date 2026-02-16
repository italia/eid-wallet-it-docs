FROM python:3.12-slim

ENV DEBIAN_FRONTEND=noninteractive \
    TZ=UTC

# Base system + LaTeX + Graphviz + Java + image tooling for Sphinx/PlantUML/PDF
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    graphviz \
    default-jre-headless \
    texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended \
    texlive-lang-italian texlive-lang-english \
    texlive-pictures texlive-font-utils \
    texlive-base texlive-binaries \
    texlive-luatex \
    texlive-fonts-extra texlive-science texlive-publishers texlive-formats-extra \
    ghostscript poppler-utils imagemagick netpbm librsvg2-bin \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

# Install Python deps (including Sphinx, extensions, etc.) and tox
# setuptools required for pkg_resources (sphinxcontrib-redoc/stevedore on Python 3.12)
COPY requirements-dev.txt ./
RUN pip install --upgrade pip "setuptools>=65.0.0,<82" \
 && pip install --no-cache-dir -r requirements-dev.txt \
 && pip install --no-cache-dir tox

# Default command: show Sphinx version
CMD ["python", "-m", "sphinx", "--version"]


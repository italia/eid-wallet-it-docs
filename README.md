# IT-Wallet Technical Specifications

[![GitHub release](https://img.shields.io/github/release/italia/eid-wallet-it-docs.svg?style=plastic)](https://github.com/italia/eid-wallet-it-docs/releases)
[![Get invited](https://slack.developers.italia.it/badge.svg)](https://slack.developers.italia.it/)

---

## Table of Contents

- [Intro](#intro)
- [Versioning and preview](#versioning-and-preview)
- [Releases](#releases)
- [Contributing](#how-to-contribute)
- [Authors](#authors)
- [License](#license)

## Intro

This repository hosts the IT-Wallet Technical Specifications: the technical architecture, implementation framework and design requirements to be adopoted by the IT-Wallet System Technical Solutions.

For more information on the IT-Wallet System please refer to the [official page]([url](https://innovazione.gov.it/progetti/sistema-it-wallet/)).

The repository is structured as sphinx project tree. **The first stable release is v1.0**; older releases are considered experimental.


## Versioning and preview

This project adheres to the [*Semantic
Versioning*](https://semver.org/) model.

Furthermore, this project uses the git *branches* and *tags* in the following way:
* the branch `versione-corrente` contains the last stable version of the documentation;
* The [release page](https://github.com/italia/eid-wallet-it-docs/releases) of
  this project contains all the released versions of the specifications. For the sake of coherence, the *releases* are made according to the tag names.

Each time a release is created or edited, a preview is built based on the tag the release refers to. 
A preview of the latest editor's copy build, corresponding to the branch `versione-corrente` can be navigated using the following link:

English version:

 - [Editor's Copy](https://italia.github.io/eid-wallet-it-docs/versione-corrente/en/)

Versione Italiana:

 - [Ultima versione in corso di sviluppo](https://italia.github.io/eid-wallet-it-docs/versione-corrente/it/)

### Releases

This section contains the references about the official releases of this project.

#### IT-Wallet Releases

Released versions are available in both Italian and English, and can be accessed in HTML and PDF formats.

| Version | English | Italian |
|---------|---------|---------|
| 1.4.0 | [HTML](https://italia.github.io/eid-wallet-it-docs/releases/1.4.0/en/) \| [PDF](https://github.com/italia/eid-wallet-it-docs/releases/download/1.4.0/eid-wallet-it-docs-en-20260210-125829.pdf) | [HTML](https://italia.github.io/eid-wallet-it-docs/releases/1.4.0/it/) \| [PDF](https://github.com/italia/eid-wallet-it-docs/releases/download/1.4.0/eid-wallet-it-docs-it-20260210-125829.pdf) |
| 1.3.3 | [HTML](https://italia.github.io/eid-wallet-it-docs/releases/1.3.3/en/) \| [PDF](https://github.com/italia/eid-wallet-it-docs/releases/download/1.3.3/eid-wallet-it-docs-en-20251223-165425.pdf) | [HTML](https://italia.github.io/eid-wallet-it-docs/releases/1.3.3/it/) \| [PDF](https://github.com/italia/eid-wallet-it-docs/releases/download/1.3.3/eid-wallet-it-docs-it-20251223-165425.pdf) |
| 1.3.2 | [HTML](https://italia.github.io/eid-wallet-it-docs/releases/1.3.2/en/) \| [PDF](https://github.com/italia/eid-wallet-it-docs/releases/download/1.3.2/eid-wallet-it-docs-en-20251210-170029.pdf) | [HTML](https://italia.github.io/eid-wallet-it-docs/releases/1.3.2/it/) \| [PDF](https://github.com/italia/eid-wallet-it-docs/releases/download/1.3.2/eid-wallet-it-docs-it-20251210-170029.pdf) |
| 1.3.1 | [HTML](https://italia.github.io/eid-wallet-it-docs/releases/1.3.1/en/) \| [PDF](https://github.com/italia/eid-wallet-it-docs/releases/download/1.3.1/eid-wallet-it-docs-en-20251128-101201.pdf) | [HTML](https://italia.github.io/eid-wallet-it-docs/releases/1.3.1/it/) \| [PDF](https://github.com/italia/eid-wallet-it-docs/releases/download/1.3.1/eid-wallet-it-docs-it-20251128-101201.pdf) |
| 1.3.0 | [HTML](https://italia.github.io/eid-wallet-it-docs/releases/1.3.0/en/) \| [PDF](https://github.com/italia/eid-wallet-it-docs/releases/download/1.3.0/eid-wallet-it-docs-en-20251105-173944.pdf) | [HTML](https://italia.github.io/eid-wallet-it-docs/releases/1.3.0/it/) \| [PDF](https://github.com/italia/eid-wallet-it-docs/releases/download/1.3.0/eid-wallet-it-docs-it-20251105-173944.pdf) |
| 1.2.1 | [HTML](https://italia.github.io/eid-wallet-it-docs/releases/1.2.1/en/) \| [PDF](https://github.com/italia/eid-wallet-it-docs/releases/download/1.2.1/eid-wallet-it-docs-en-20251021-171536.pdf) | [HTML](https://italia.github.io/eid-wallet-it-docs/releases/1.2.1/it/) \| [PDF](https://github.com/italia/eid-wallet-it-docs/releases/download/1.2.1/eid-wallet-it-docs-it-20251021-171536.pdf) |
| 1.2.0 | [HTML](https://italia.github.io/eid-wallet-it-docs/releases/1.2.0/en/) \| [PDF](https://github.com/italia/eid-wallet-it-docs/releases/download/1.2.0/eid-wallet-it-docs-en-20251008-145727.pdf) | [HTML](https://italia.github.io/eid-wallet-it-docs/releases/1.2.0/it/) \| [PDF](https://github.com/italia/eid-wallet-it-docs/releases/download/1.2.0/eid-wallet-it-docs-it-20251008-145727.pdf) |
| 1.1.0 | [HTML](https://italia.github.io/eid-wallet-it-docs/releases/1.1.0/en/) \| [PDF](https://github.com/italia/eid-wallet-it-docs/releases/download/1.1.0/eid-wallet-it-docs-en-20250731-104027.pdf) | [HTML](https://italia.github.io/eid-wallet-it-docs/releases/1.1.0/it/) \| [PDF](https://github.com/italia/eid-wallet-it-docs/releases/download/1.1.0/eid-wallet-it-docs-it-20250731-104027.pdf) |
| 1.0.2 | [HTML](https://italia.github.io/eid-wallet-it-docs/releases/1.0.2/en/) \| [PDF](https://github.com/italia/eid-wallet-it-docs/releases/download/1.0.2/eid-wallet-it-docs-en-20250618-105321.pdf) | [HTML](https://italia.github.io/eid-wallet-it-docs/releases/1.0.2/it/) \| [PDF](https://github.com/italia/eid-wallet-it-docs/releases/download/1.0.2/eid-wallet-it-docs-it-20250618-105321.pdf) |
| 1.0.1 | [HTML](https://italia.github.io/eid-wallet-it-docs/releases/1.0.1/en/) \| [PDF](https://github.com/italia/eid-wallet-it-docs/releases/download/1.0.1/eid-wallet-it-docs-en-20250603-153138.pdf) | [HTML](https://italia.github.io/eid-wallet-it-docs/releases/1.0.1/it/) \| [PDF](https://github.com/italia/eid-wallet-it-docs/releases/download/1.0.1/eid-wallet-it-docs-it-20250603-153138.pdf) |
| v1.0.0 | [HTML](https://italia.github.io/eid-wallet-it-docs/releases/v1.0.0/en/) | [HTML](https://italia.github.io/eid-wallet-it-docs/releases/v1.0.0/it/) |

#### IT-Wallet Early Stages Releases

The following table contains all historical versions before 1.0.0, representing the early development stages of the IT-Wallet product:

| Version | English | Italian |
|---------|---------|---------|
| v0.9.3 | [HTML](https://italia.github.io/eid-wallet-it-docs/releases/v0.9.3/en/) | [HTML](https://italia.github.io/eid-wallet-it-docs/releases/v0.9.3/it/) |
| v0.9.2 | [HTML](https://italia.github.io/eid-wallet-it-docs/releases/v0.9.2/en/) | [HTML](https://italia.github.io/eid-wallet-it-docs/releases/v0.9.2/it/) |
| v0.9.1 | [HTML](https://italia.github.io/eid-wallet-it-docs/releases/v0.9.1/en/) | [HTML](https://italia.github.io/eid-wallet-it-docs/releases/v0.9.1/it/) |
| v0.9.0 | [HTML](https://italia.github.io/eid-wallet-it-docs/releases/v0.9.0/en/) | [HTML](https://italia.github.io/eid-wallet-it-docs/releases/v0.9.0/it/) |
| v0.8.2 | [HTML](https://italia.github.io/eid-wallet-it-docs/releases/v0.8.2/en/) | [HTML](https://italia.github.io/eid-wallet-it-docs/releases/v0.8.2/it/) |
| v0.8.1 | [HTML](https://italia.github.io/eid-wallet-it-docs/releases/v0.8.1/en/) | [HTML](https://italia.github.io/eid-wallet-it-docs/releases/v0.8.1/it/) |
| v0.8.0 | [HTML](https://italia.github.io/eid-wallet-it-docs/releases/v0.8.0/en/) | [HTML](https://italia.github.io/eid-wallet-it-docs/releases/v0.8.0/it/) |
| v0.7.1 | [HTML](https://italia.github.io/eid-wallet-it-docs/releases/v0.7.1/en/) | [HTML](https://italia.github.io/eid-wallet-it-docs/releases/v0.7.1/it/) |
| v0.7.0 | [HTML](https://italia.github.io/eid-wallet-it-docs/releases/v0.7.0/en/) | [HTML](https://italia.github.io/eid-wallet-it-docs/releases/v0.7.0/it/) |
| v0.6.0 | [HTML](https://italia.github.io/eid-wallet-it-docs/releases/v0.6.0/en/) | [HTML](https://italia.github.io/eid-wallet-it-docs/releases/v0.6.0/it/) |
| v0.5.0 | [HTML](https://italia.github.io/eid-wallet-it-docs/releases/v0.5.0/en/) | [HTML](https://italia.github.io/eid-wallet-it-docs/releases/v0.5.0/it/) |
| v0.4.1 | [HTML](https://italia.github.io/eid-wallet-it-docs/releases/v0.4.1/en/) | [HTML](https://italia.github.io/eid-wallet-it-docs/releases/v0.4.1/it/) |


## Build Previews

### Using Github Actions

- access the manual [build frontend](https://github.com/italia/eid-wallet-it-docs/actions/workflows/build-html-manual.yml)
- insert the Pull Request number using the form and submit the workflow as shown in the image below.

<img width="1894" height="734" alt="image" src="https://github.com/user-attachments/assets/cdc81d14-4665-41c8-b251-385a1170a299" />


#### Build HTML with Sphinx
````
pip install -r requirements-dev.txt

sphinx-build -b html -d html/en/doctrees docs/en/ html/en
````

ODT
````
sudo apt install pandoc
sphinx-build -b singlehtml docs/en/  html/
cd html
pandoc -o eid-it-wallet-docs.odt index.html
````

### Build PDFs (EN and IT) with Docker

You can build the English and Italian PDFs locally using Docker, without installing LaTeX or Sphinx on your machine.

#### Option A: Use the prebuilt image from GitHub Container Registry

A prebuilt image is published on GitHub Container Registry as [`ghcr.io/italia/eidas-it-wallet-docs-builder`](https://github.com/italia/eid-wallet-it-docs/pkgs/container/eidas-it-wallet-docs-builder).

- **1. Pull the image and tag it as `eid-wallet-it-docs`**

```bash
docker pull ghcr.io/italia/eidas-it-wallet-docs-builder:latest
docker tag ghcr.io/italia/eidas-it-wallet-docs-builder:latest eid-wallet-it-docs
```

You can also use a specific digest or tag shown on the package page, e.g.:

```bash
docker pull ghcr.io/italia/eidas-it-wallet-docs-builder:b235e366abbb852177eb2db39c9b2de2a7b71129
docker tag ghcr.io/italia/eidas-it-wallet-docs-builder:b235e366abbb852177eb2db39c9b2de2a7b71129 eid-wallet-it-docs
```

#### Option B: Build the Docker image locally

From the repository root:

```bash
docker build -t eid-wallet-it-docs .
```

#### Run the container to generate PDFs (shared for both options)

From the repository root:

```bash
docker run --rm \
  -e PDF_BUILD_TAG=1.4.0 \
  -v "$PWD":/workspace \
  -w /workspace \
  eid-wallet-it-docs \
  bash -lc "./utils/build-pdf-local.sh"
```

This command:

- uses the `eid-wallet-it-docs` image (either pulled from GHCR and tagged, or built locally);
- mounts the current repository into `/workspace` inside the container;
- runs `./utils/build-pdf-local.sh`, which for each language in `docs/en` and `docs/it`:
  - builds LaTeX with Sphinx,
  - compiles the main `.tex` file with LuaLaTeX,
  - and copies the resulting PDFs into the `pdf_output/` directory in your working tree.


## How to contribute


Refer to [Contributing Rules Section](CONTRIBUTING-RULES.md) for an editorial guideline. Don't hesitate to submit [Pull Requests or raise Issues](CONTRIBUTING.md) if you encounter any problems.


## Authors
These Technical Specifications are drafted and maintained by the [Department for Digital Transformation]([url](https://innovazione.gov.it/)), [IPZS Istituto Poligrafico e Zecca dello Stato]([url](https://www.ipzs.it/ext/index.html)) and [PagoPA]([url](https://www.pagopa.it/it/)), with the supervision of [AGID, Agency for Digital Italy]([url](https://www.agid.gov.it/it)). 

## License

The project is covered by a [CC-0](LICENSE) license.

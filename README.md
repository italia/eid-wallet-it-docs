# IT-Wallet Technical Specifications

[![GitHub release](https://img.shields.io/github/release/italia/eid-wallet-it-docs.svg?style=plastic)](https://github.com/italia/eid-wallet-it-docs/releases)
[![Get invited](https://slack.developers.italia.it/badge.svg)](https://slack.developers.italia.it/)

---

## Table of Contents

- [Intro](#intro)
- [Versioning and preview](#versioning-and-preview)
- [Contributing](#how-to-contribute)
- [Authors](#authors)
- [License](#license)

## Intro

This repository hosts the IT-Wallet Technical Specifications: the technical architecture, implementation framework and design requirements to be adopoted by the IT-Wallet System Technical Solutions.

For more information on the IT-Wallet System please refer to the [official page]([url](https://innovazione.gov.it/progetti/sistema-it-wallet/)).

The repository is structured as sphinx project tree. **The first stable release is v1.0**; other contents in the repository may be considered experimental.


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

Released versions can be navigated by adding the tag in the webpath leaded by a _v_, as follows:

Italian:

 - [https://italia.github.io/eid-wallet-it-docs/releases/v1.0.1/it/](https://italia.github.io/eid-wallet-it-docs/releases/v1.0.1-1/it/)

English:

 - [https://italia.github.io/eid-wallet-it-docs/releases/v1.0.1/en/](https://italia.github.io/eid-wallet-it-docs/releases/v1.0.1-1/en/)
 - [https://italia.github.io/eid-wallet-it-docs/releases/v1.0.0/en/](https://italia.github.io/eid-wallet-it-docs/releases/v1.0.0/en/)
 - [https://italia.github.io/eid-wallet-it-docs/releases/v0.9.3/en/](https://italia.github.io/eid-wallet-it-docs/releases/v0.9.3/en/)
 - [https://italia.github.io/eid-wallet-it-docs/releases/v0.9.2/en/](https://italia.github.io/eid-wallet-it-docs/releases/v0.9.2/en/)
 - [https://italia.github.io/eid-wallet-it-docs/releases/v0.9.1/en/](https://italia.github.io/eid-wallet-it-docs/releases/v0.9.1/en/)
 - [https://italia.github.io/eid-wallet-it-docs/releases/v0.9.0/en/](https://italia.github.io/eid-wallet-it-docs/releases/v0.9.0/en/)
 - [https://italia.github.io/eid-wallet-it-docs/releases/v0.8.2/en/](https://italia.github.io/eid-wallet-it-docs/releases/v0.8.2/en/)
 - [https://italia.github.io/eid-wallet-it-docs/releases/v0.8.1/en/](https://italia.github.io/eid-wallet-it-docs/releases/v0.8.1/en/)
 - [https://italia.github.io/eid-wallet-it-docs/releases/v0.8.0/en/](https://italia.github.io/eid-wallet-it-docs/releases/v0.8.0/en/)
 - [https://italia.github.io/eid-wallet-it-docs/releases/v0.7.1/en/](https://italia.github.io/eid-wallet-it-docs/releases/v0.7.1/en/)
 - [https://italia.github.io/eid-wallet-it-docs/releases/v0.7.0/en/](https://italia.github.io/eid-wallet-it-docs/releases/v0.7.0/en/)
 - [https://italia.github.io/eid-wallet-it-docs/releases/v0.6.0/en/](https://italia.github.io/eid-wallet-it-docs/releases/v0.6.0/en/)
 - [https://italia.github.io/eid-wallet-it-docs/releases/v0.5.0/en/](https://italia.github.io/eid-wallet-it-docs/releases/v0.5.0/en/)
 - [https://italia.github.io/eid-wallet-it-docs/releases/v0.4.1/en/](https://italia.github.io/eid-wallet-it-docs/releases/v0.4.1/en/)

## Build

HTML
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


## How to contribute


Refer to [Contributing Rules Section](CONTRIBUTING-RULES.md) for an editorial guideline. Don't hesitate to submit [Pull Requests or raise Issues](CONTRIBUTING.md) if you encounter any problems.


## Authors
These Technical Specifications are drafted and maintained by the [Department for Digital Transformation]([url](https://innovazione.gov.it/)), [IPZS Istituto Poligrafico e Zecca dello Stato]([url](https://www.ipzs.it/ext/index.html)) and [PagoPA]([url](https://www.pagopa.it/it/)), with the supervision of [AGID, Agency for Digital Italy]([url](https://www.agid.gov.it/it)). 

## License

The project is covered by a [CC-0](LICENSE) license.

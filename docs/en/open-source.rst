.. include:: ../common/common_definitions.rst

.. _open-source.rst:

Open Source Releases for IT-Wallet Solutions  
============================================

In compliance with the LLGG Wallet mandates, IT-Wallet Solution Providers, both public and private, are required to make their source code available. This requirement emphasizes the importance of using open-source software within public administrations to promote transparency and reduce costs. This requirement is supported by the Italian Digital Administration Code (CAD) articles 68 and 69, European regulations (``Artificial Intelligence Act (AI Act)`` <https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689>_, ``Cyber Resilience Act (CRA)`` <https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202402847>_, ``Interoperable Europe Act`` <https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:52022PC0720>_), and best practices in open-source software development. This document defines the specific requirements for different stakeholders involved in the IT-Wallet ecosystem, including Wallet Providers, Credential Issuers, and Relying Parties.

All the implementers, be these Wallet Providers, Credential Issuers or Relying Parties, owning the product code (from now on Open Source Project Owner) SHOULD follow industry best practices for open-source software, including proper documentation, version control, and community engagement. In particular:

    - **Transparency and Documentation**: Open Source Project Owners SHOULD produce clear documentation and contribution guidelines.
    - **Community Engagement**: Open Source Project Owners SHOULD foster active community involvement for development and support.
    - **Version Control**: Open Source Project Owners MAY use systems like Git for managing code changes.
    - **Security Practices**: Open Source Project Owners MUST produce regular code audits and secure coding standards.
    - **Licensing**: Open Source Project Owners MUST use appropriate open-source licenses (e.g., EUPL, MIT, Apache 2.0, GPL, AGPL).
    - **Responsible Security Disclosure**: Open Source Project Owners MUST configure responsible security disclosure procedures to handle the security issues in an appropriate way, mitigating any kind of threat derived by an unresponsible security issue disclosure. 


Wallet Provider Solutions 
^^^^^^^^^^^^^^^^^^^^^^^^^

Wallet Solution Providers are required to release their source code, build system, and all other assets required to the reproducibility of the implementation in order to facilitate transparency, security auditing within the IT-Wallet ecosystem. The release of source code adheres to the following guidelines:

- **European Regulations**: According to the Consolidated Regulation (EU) 2024/2979, Art 5a item 3, `the source code of the application software components of European Digital Identity Wallets shall be open-source licensed. Member States may provide that, for duly justified reasons, the source code of specific components other than those installed on user devices shall not be disclosed`.


Credential Issuers Solutions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Credential Issuers are required to release their source code if they are providers for public administrations or if they are public administrations themselves. The requirements include:

- **Public Administration Engagement**: Issuers working with public administrations MUST ensure their solutions are released with an open source license, in the way specified by the CAD art. 69 (and related guidelines).
- **Catalog of Reuse**: Solutions created with or for public administration MUST be submitted to the public administration reuse catalog to promote widespread adoption and adaptation.

Relying Parties Solutions
^^^^^^^^^^^^^^^^^^^^^^^^^
Relying Parties are subject to the same conditions as Credential Issuers regarding the release of their source code.

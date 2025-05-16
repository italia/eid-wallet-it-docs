.. include:: ../common/common_definitions.rst


Open Source Releases 
=====================

In line with the general principles of openness and transparency, Wallet Providers, Credential Issuers and Relying Parties are encouraged to consider adopting open-source approaches, including during the experimentation phase, to promote collaboration, peer review, and shared improvements across the ecosystem. This encouragement is part of an evolving framework, pending the definition of the relevant procedures by the `guidelines on the acquisition and reuse of software for public administrations <https://docs.italia.it/italia/developers-italia/gl-acquisition-and-reuse-software-for-pa-docs/en/stabile/index.html>`_ pursuant to Article 64-quater of the CAD, which refers to Article 69 regarding the release of source code. Open source is supported by the Italian Digital Administration Code (CAD) articles 68 and 69 (and related guidelines), European regulations (`Artificial Intelligence Act (AI Act) <https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689>`_, `Cyber Resilience Act (CRA) <https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202402847>`_, `Interoperable Europe Act <https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202400903>`_).

All the implementers, be these Wallet Providers, Credential Issuers or Relying Parties, owning the product code (from now on Open Source Project Owner) SHOULD follow industry best practices for open-source software, including proper documentation, version control, and community engagement. In particular:

- **Transparency and Documentation**: Open Source Project Owners SHOULD produce clear documentation and contribution guidelines.
- **Community Engagement**: Open Source Project Owners SHOULD foster active community involvement for development and support.
- **Software Version Control**: Open Source Project Owners SHOULD use version control systems, such as Git, for managing code changes.
- **Security Practices**: Open Source Project Owners SHOULD produce regular code audits and secure coding standards.
- **Licensing**: Open Source Project Owners MUST use appropriate open-source licenses, recognized as "free license" or "open source license" by the Free Software Foundation or the Open Source Initiative.
- **Responsible Security Disclosure**: Open Source Project Owners SHOULD configure responsible security disclosure procedures to handle the security issues in an appropriate way, mitigating any kind of threat derived by an unresponsible security issue disclosure. 

Wallet Providers
^^^^^^^^^^^^^^^^

Wallet Providers are encouraged to release their source code, build system, and all other assets required to the reproducibility of the implementation in order to facilitate transparency, security auditing within the IT-Wallet ecosystem. Where applicable, the release of source code SHOULD follow the specifications below:

- **European Regulations**: According to the Consolidated Regulation (EU) 910/2014, Art 5a item 3, `the source code of the application software components of European Digital Identity Wallets shall be open-source licensed. Member States may provide that, for duly justified reasons, the source code of specific components other than those installed on user devices shall not be disclosed`.

Credential Issuers
^^^^^^^^^^^^^^^^^^

Credential Issuers are encouraged to release their source code under an open-source license, starting from the experimentation phase.

Relying Parties
^^^^^^^^^^^^^^^
Relying Parties are are encouraged to follow the same conditions as Credential Issuers regarding the release of their source code.

Responsible Disclosure
^^^^^^^^^^^^^^^^^^^^^^

In the European context, the Cyber Resilience Act (CRA) mandates procedures for handling vulnerability reports and requires reporting actively exploited vulnerabilities to Computer Security Incident Response Teams (CSIRTs). The Directive on Security of Network and Information Systems Directive (EU) 2022/2555 (NIS2 <https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32022L2555>_) also emphasizes vulnerability handling within cybersecurity risk management.



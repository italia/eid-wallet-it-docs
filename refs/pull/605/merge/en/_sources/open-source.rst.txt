.. include:: ../common/common_definitions.rst

.. _open-source.rst:

Open Source Releases for IT-Wallet Solutions  
============================================

In line with the general principles of openness and transparency, IT-Wallet Solution Providers are encouraged to consider making their source code available, particularly when adopting open-source approaches, including during the experimentation phase, to promote collaboration, peer review, and shared improvements across the ecosystem. This encouragement is part of an evolving framework, pending the definition of the relevant procedures by the Guidelines pursuant to Article 64-quater of the CAD, which refers to Article 69 regarding the release of source code. In particular, public administrations using and producing open-source software promote transparency and reduce costs. Open source is supported by the Italian Digital Administration Code (CAD) articles 68 and 69 (and related guidelines), European regulations (``Artificial Intelligence Act (AI Act)`` <https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689>_, ``Cyber Resilience Act (CRA)`` <https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202402847>_, ``Interoperable Europe Act`` <https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:52022PC0720>_), as well as by best practices in open-source software development. This document defines the specific requirements for different stakeholders involved in the IT-Wallet ecosystem, including Wallet Providers, Credential Issuers, and Relying Parties.

All the implementers, be these Wallet Providers, Credential Issuers or Relying Parties, owning the product code (from now on Open Source Project Owner) SHOULD follow industry best practices for open-source software, including proper documentation, version control, and community engagement. In particular:

    - **Transparency and Documentation**: Open Source Project Owners SHOULD produce clear documentation and contribution guidelines.
    - **Community Engagement**: Open Source Project Owners SHOULD foster active community involvement for development and support.
    - **Software Version Control**: Open Source Project Owners SHOULD use version control systems, such as Git, for managing code changes.
    - **Security Practices**: Open Source Project Owners SHOULD produce regular code audits and secure coding standards.
    - **Licensing**: Open Source Project Owners MUST use appropriate open-source licenses, recognized as "free license" or "open source license" by the Free Software Foundation or the Open Source Initiative.
    - **Responsible Security Disclosure**: Open Source Project Owners SHOULD configure responsible security disclosure procedures to handle the security issues in an appropriate way, mitigating any kind of threat derived by an unresponsible security issue disclosure. 


Wallet Provider Solutions 
^^^^^^^^^^^^^^^^^^^^^^^^^

Wallet Solution Providers are encouraged to release their source code, build system, and all other assets required to the reproducibility of the implementation in order to facilitate transparency, security auditing within the IT-Wallet ecosystem. Where applicable, the release of source code SHOULD follow the specifications below:

- **European Regulations**: According to the Consolidated Regulation (EU) 2024/2979, Art 5a item 3, `the source code of the application software components of European Digital Identity Wallets shall be open-source licensed. Member States may provide that, for duly justified reasons, the source code of specific components other than those installed on user devices shall not be disclosed`.


Credential Issuers Solutions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Credential Issuers are encouraged to release their source code under an open-source license, starting from the experimentation phase, in accordance with the principles set out in Article 69 of the CAD. The requirements include:

- **Public Administration Engagement**: Issuers working with public administrations MUST ensure their solutions are released with an open source license, in the way specified by the CAD art. 69 (and related guidelines).
- **Catalog of Reuse**: Solutions created with or for public administration MUST be submitted to the public administration software reuse catalog to promote widespread adoption and adaptation.

Relying Parties Solutions
^^^^^^^^^^^^^^^^^^^^^^^^^
Relying Parties are are encouraged to follow the same conditions as Credential Issuers regarding the release of their source code.


Responsible Disclosure
^^^^^^^^^^^^^^^^^^^^^^

In the European context, the Cyber Resilience Act (CRA) mandates procedures for handling vulnerability reports and requires reporting actively exploited vulnerabilities to Computer Security Incident Response Teams (CSIRTs). The Directive on Security of Network and Information Systems Directive (EU) 2022/2555 (NIS2 <https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32022L2555>_) also emphasizes vulnerability handling within cybersecurity risk management.

ISO/IEC 29147:2018 (<https://www.iso.org/standard/72311.html>_) provides guidelines for vulnerability disclosure processes. Industry best practices, often seen in bug bounty platforms, clear reporting, response times, safe harbor, and coordinated disclosure.

Security Best Practices for Releasing Source Code of Critical Components
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The EU Open Source Software Strategy encourages open sourcing with an implicit need for security. The CRA's focus on security by design and Software Bill of Materials (SBOMs <https://www.cisa.gov/sbom>_) requires secure development practices relevant to open source releases.

The Open Worldwide Application Security Project (OWASP <https://owasp.org/>_) provides extensive secure coding guidelines and security patterns. The  SysAdmin, Audit, Network, and Security Institute (SANS <https://www.sans.org/>_) and the Italian Computer Emergency Response Team (CERT <https://cert-agid.gov.it/>_) offer secure coding standards for various languages. Version control best practices include regular commits, detailed messages, code reviews, branch protection, and careful secret management. Employing static and dynamic code analysis, along with threat modeling, is required before release. Robust dependency management involves SBOMs, regular updates, vulnerability scanning, and version pinning. Secure build and release processes ensure software integrity. For open-source projects, engaging with the community and maintaining transparency about security practices are RECOMMENDED.

.. include:: ../common/common_definitions.rst


Technical References
====================

This section details the technical references, grouped by scope, that are part of the current implementation profile.
This section includes international and national standards, draft specifications, architecture references and other relevant technical documents foundational for the interoperability and the compliance with industry standards.


Wallet Architecture and Reference Frameworks
--------------------------------------------

.. list-table::
    :widths: 25 75
    :header-rows: 0

    * - `EIDAS-ARF`_
      - EUDI Wallet Architecture and Reference Framework (ARF) v2.8.0.
    

EUDI Wallet Standards and Technical Specifications
--------------------------------------------------

.. list-table::
    :widths: 25 75
    :header-rows: 0

    * - `EUDI-TS 3`_
      - Specification of Wallet Unit Attestations (WUA) used in issuance of PID and Attestations.
    * - `EUDI-TS 10`_
      - Data Portability and Download (Export).
    * - `EUDI-TS 12`_
      - Specification of Strong Customer Authentication (SCA) Implementation with the Wallet.




Infrastructure of Trust
-----------------------

.. list-table::
    :widths: 25 75
    :header-rows: 0

    * - :rfc:`5280`
      - Cooper, D., Santesson, S., Farrell, S., Boeyen, S., Housley, R., and W. Polk, "Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile", RFC 5280, May 2008.
    * - `OID-FED-WALLET`_
      - De Marco, G., Hedberg, R., Jones, M.B., Bradley, J., Dzhuvinov, V., "OpenID Federation Wallet Architectures 1.0", October 2024, Draft 03.
    * - `OID-FED`_
      - Hedberg, R., Jones, M.B., Solberg, A.A., Bradley, J., De Marco, G., Dzhuvinov, V., "OpenID Federation 1.0", December 2025, Draft 46.
    * - `OID-FED-SUBORDINATE-EVENTS`_
      - De Marco, G., Jones, M.B., "OpenID Federation Subordinate Events Endpoint 1.0", January 2026, Draft 00.
    * - `ETSI TS 119 612`_
      - ETSI TS 119 612 v2.4.1 (2025-08) - Electronic Signatures and Infrastructures (ESI); Trusted Lists.
    * - `ETSI TS 119 602`_
      - ETSI TS 119 602 v1.1.1 (2025-11) - Electronic Signatures and Infrastructures (ESI); Lists of trusted entities; Data model.
    * - `ETSI TS 119 615`_
      - ETSI TS 119 615 v1.3.1 (2026-01) - Electronic Signatures and Trust Infrastructures (ESI); Trusted lists; Procedures for using and interpreting European Union Member States national trusted lists.
    * - `ETSI EN 319 132-1`_
      - ETSI EN 319 132-1 v1.3.1 - Electronic Signatures and Infrastructures (ESI); XAdES digital signatures; Part 1: Building blocks and XAdES baseline signatures.
    * - `ETSI TS 119 182-1`_
      - ETSI TS 119 182-1 v1.2.1 - Electronic Signatures and Infrastructures (ESI); JAdES digital signatures; Part 1: Building blocks and JAdES baseline signatures.
    * - `ETSI TS 119 412-6`_
      - ETSI TS 119 412-6 v1.1.1 - Electronic Signatures and Infrastructures (ESI); Part 6: Certificate profile requirements for PID, Wallet, EAA, QEAA, and PSBEAA providers.


Digital Credential Data Format
------------------------------

.. list-table::
    :widths: 25 75
    :header-rows: 0

    * - `SD-JWT-VC`_
      - O. Terbu, D.Fett, B. Campbell, "SD-JWT-based Verifiable Credentials (SD-JWT VC)", September 2025, Draft 11.
    * - `ISO18013-5`_
      - ISO/IEC 18013-5 2020. Information technology — Personal identification — ISO-compliant driving license — Part 5: Mobile driving license (mDL) application.


Digital Credential Issuance
---------------------------

.. list-table::
    :widths: 25 75
    :header-rows: 0

    * - `OpenID4VCI`_
      - Lodderstedt, T., Yasuda, K., Looker, T., Bastian, P., "OpenID for Verifiable Credential Issuance 1.0", September 2025.
    * - `OPENID4VC-HAIP`_
      - K. Yasuda, Lodderstedt, T., Bormann, C., Heenan, J., "OpenID4VC High Assurance Interoperability Profile 1.0", November 2025, Draft 6.
    * - `OAUTH-ATTESTATION-CLIENT-AUTH`_
      - Looker, T., Bastian, P., Bormann, C., "OAuth 2.0 Attestation-Based Client Authentication", September 2025, Draft 7.
    * - `OAUTH-MULT-RESP-TYPE`_
      - de Medeiros, B., Scurtescu, M., Tarjan, P., Jones, M., "OAuth 2.0 Multiple Response Type Encoding Practices", February 2014.


Digital Credential Presentation
-------------------------------

.. list-table::
    :widths: 25 75
    :header-rows: 0

    * - `OpenID4VP`_
      - Terbu, O., Lodderstedt, T., Yasuda, K., Fett, D., Heenan, J., "OpenID for Verifiable Presentations 1.0", July 2025.
    * - `OAuthCrossDeviceSec`_
      - Kasselman, P., Fett, D., Skokan, F.,  "Cross-Device Flows: Security Best Current Practice", July 2024, Draft 8.
    * - `OPENID4VC-HAIP`_
      - Lodderstedt, T., K. Yasuda, "OpenID4VC High Assurance Interoperability Profile", January 2025, Draft 1.
    * - `ISO18013-5`_
      - ISO/IEC 18013-5 2020. Information technology — Personal identification — ISO-compliant driving license — Part 5: Mobile driving license (mDL) application.
    * - `OIDC-RP-Metadata`_
      - Jones, M.B., Hedberg, R., Bradley, J., Skokan, F., "OpenID Connect Relying Party Metadata Choices 1.0", April 2025, Draft 2.

Digital Credential Revocation Check Mechanisms
----------------------------------------------

.. list-table::
    :widths: 25 75
    :header-rows: 0

    * - `TOKEN-STATUS-LIST`_
      - Looker, T., Bastian, P., Bormann, C.,  "Token Status List (TSL)", October 2025, Draft 13.

National Data Interoperability Platform Specifications
------------------------------------------------------

.. list-table::
   :widths: 25 75
   :header-rows: 0

   * - `MODI`_
     - "Linee Guida sull'interoperabilità tecnica delle Pubbliche Amministrazioni", November 2023, Version 1.2.
   * - `PDND`_
     - "Linee Guida sull'infrastruttura tecnologica della Piattaforma Digitale Nazionale Dati per l'interoperabilità dei sistemi informativi e delle basi di dati", June 2025, Version 2.0.
   * - `OAS3`_
     - OpenAPI 3.0 API Specification.

National Digital Identity Platform Specifications
-------------------------------------------------

.. list-table::
    :widths: 25 75
    :header-rows: 0

    * - `SPID/CIE-OpenID-Connect-Specifications`_
      - SPID/CIE OpenID Connect.


Security and Protection Profiles
--------------------------------

.. list-table::
    :widths: 25 75
    :header-rows: 0

    * - `UNI CEI EN ISO/IEC 27001:2024`
      - Information security, cybersecurity and privacy protection — Information security management systems — Requirement

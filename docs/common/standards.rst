.. include:: ../common/common_definitions.rst


Technical References
++++++++++++++++++++

This section details the technical references, grouped by scope, that are part of the current implementation profile or for its future milestones.
It includes international and national standards, draft specifications, architecture references and other relevant technical documents
foundational for the interoperability and the compliance with industry standards.


Wallet Paradigm Frameworks
--------------------------

.. list-table::
    :widths: 25 75
    :header-rows: 0

    * - `EIDAS-ARF`_
      - EUDI Wallet - Architecture and Reference Framework.


Json Web Token Standards
------------------------

.. list-table::
    :widths: 25 75
    :header-rows: 0

    * - :rfc:`7515`
      - Jones, M., Bradley, J. and N. Sakimura, "JSON Web Signature (JWS)", RFC 7515, DOI 10.17487/RFC7515, May 2015.
    * - :rfc:`7516`
      - Jones, M., Hildebrand, J., "JSON Web Encryption (JWE)", May 2015.
    * - :rfc:`7517`
      - Jones, M., "JSON Web Key (JWK)", RFC 7517, DOI 10.17487/RFC7517, May 2015.
    * - :rfc:`7518`
      - Jones, M., "JSON Web Algorithms (JWA)", May 2015.
    * - :rfc:`7519`
      - Jones, M., Bradley, J. and N. Sakimura, "JSON Web Token (JWT)", RFC 7519, DOI 10.17487/RFC7519, May 2015.
    * - :rfc:`7638`
      - Jones, M., Sakimura, N., “JSON Web Key (JWK) Thumbprint”, September 2015.
    * - :rfc:`7800`
      - Jones, M., Bradley, J. and H. Tschofenig, "Proof-of-Possession Key Semantics for JSON Web Tokens (JWTs)", RFC 7800, DOI 10.17487/RFC7800, April 2016.
    * - :rfc:`8725`
      - Jones, M., D. Hardt, Sheffer, Y., "JSON Web Token Best Current Practices", February 2020.
    * - `SD-JWT`_
      - Fett, D., Yasuda, K., Campbell, B., "Selective Disclosure for JWTs (SD-JWT)".

Infrastructure of Trust
-----------------------

.. list-table::
    :widths: 25 75
    :header-rows: 0

    * - `OID-FED`_
      - Hedberg, R., Jones, M.B., Solberg, A.Å., Bradley, J., De Marco, G., Dzhuvinov, V.,  "OpenID Federation 1.0", December 2024, Draft 41.
    * - `OID-FED-WALLET`_
      - De Marco, G., Hedberg, R., Jones, M.B., Bradley, J., Dzhuvinov, V., "OpenID Federation Wallet Architectures 1.0", October 2024, Draft 03.
    * - :rfc:`5280`
      - Cooper, D., Santesson, S., Farrell, S., Boeyen, S., Housley, R., and W. Polk, "Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile", RFC 5280, May 2008.
    * - RTS/ESI-0019612v231 (TS 119 612)
      - Electronic Signatures and Trust Infrastructures (ESI); Trusted Lists
    * - DTS/ESI-0019602
      - Electronic Signatures and Trust Infrastructures (ESI); Trusted lists; Data model
    * - REN/ESI-0019411-1v151
      - Electronic Signatures and Trust Infrastructures (ESI); Policy and security requirements for Trust Service Providers issuing certificates; Part 1: General requirements Policy requirements for certification authorities issuing public key certificates


Digital Credential Data Format
------------------------------

.. list-table::
    :widths: 25 75
    :header-rows: 0

    * - `SD-JWT-VC`_
      - O. Terbu, D.Fett, B. Campbell, "SD-JWT-based Verifiable Credentials (SD-JWT VC)".
    * - ISO18013-5
      - ISO/IEC 18013-5 2020. Information technology — Personal identification — ISO-compliant driving license — Part 5: Mobile driving license (mDL) application.
    * - W3C-VC-DT-1.1
      - "Verifiable Credentials Data Model 1.1.", W3C Recommendation, 3 March 2022.
    * - W3C_VCDM_v2_0
      - Verifiable Credentials Data Model v2.0
    * - ISO-IEC_7367
      - ISO Compliant Mobile Vehicle Registration Certificates, Logical Data Structure

Digital Credential Interoperability
-----------------------------------

.. list-table::
    :widths: 25 75
    :header-rows: 0

    * - `OpenID4VCI`_
      - Lodderstedt, T., Yasuda, K., Looker, T., "OpenID for Verifiable Credential Issuance", December 2024, Draft 15.
    * - `OpenID4VP`_
      - Terbu, O., Lodderstedt, T., Yasuda, K., Looker, T., "OpenID for Verifiable Presentations", December 2024, Draft 23.
    * - `PresentationExch`_
      - Presentation Exchange 2.0 for Presentation Definition.
    * - `JARM`_
      - Lodderstedt, T., Campbell, B., "JWT Secured Authorization Response Mode for OAuth 2.0 (JARM)", November 2022.
    * - :rfc:`6749`
      - The OAuth 2.0 Authorization Framework.
    * - :rfc:`9449`
      - D. Fett, B. Campbell, J. Bradley, T. Lodderstedt, M. Jones, D. Waite, "OAuth 2.0 Demonstrating Proof-of-Possession at the Application Layer (DPoP)".
    * - :rfc:`9207`
      - Meyer zu Selhausen, K., Fett, D., "OAuth 2.0 Authorization Server Issuer Identification", March 2022.
    * - :rfc:`7521`
      - Campbell, Mortimore, C., Jones, M., Goland, Y.,  "Assertion Framework for OAuth 2.0 Client Authentication and Authorization Grants", May 2015.       
    * - `OPENID4VC-HAIP`_
      - Lodderstedt, T., K. Yasuda, "OpenID4VC High Assurance Interoperability Profile", January 2025, Draft 1.
    * - `OAUTH-ATTESTATION-CLIENT-AUTH`_
      - Looker, T., Bastian, P., "OAuth 2.0 Attestation-Based Client Authentication", May 2024, Draft 3.
    * - `OAUTH-MULT-RESP-TYPE`_
      - de Medeiros, B., Scurtescu, M., Tarjan, P., Jones, M., "OAuth 2.0 Multiple Response Type Encoding Practices", February 2014.
    * - `OAuthCrossDeviceSec`_
      - Kasselman, P., Fett, D., Skokan, F.,  "Cross-Device Flows: Security Best Current Practice", July 2024, Draft 8.
    * - `OpenID4VC-SecTrust`_
      - Fett, D., Lodderstedt, T.,  "Security and Trust in OpenID for Verifiable Credentials Ecosystems", March 2024.
    * - ISO18013-5
      - ISO/IEC 18013-5 2020. Information technology — Personal identification — ISO-compliant driving license — Part 5: Mobile driving license (mDL) application. International Organization for Standardization.
    * - ISO/IEC 18013-7
      - Personal identification - ISO-compliant driving licence - Part 7, Mobile driving licence (mDL) add-on functions, February 2024
    * - ISO/IEC 23220-3
      - Cards and security devices for personal identification - Building blocks for identity management via mobile devices - Part 3: Protocols and services for installation and issuing phase
    * - ISO/IEC 23220-4
      - Cards and security devices for personal identification - Building blocks for identity management via mobile devices - Part 4: Protocols and services for operational phase
    * - DTS/ESI-0019472-2
      - Electronic Signatures and Trust Infrastructures (ESI); Profiles for Electronic Attestations of Attributes Part 2: Profiles for Relying party interface to EUDI Wallet
    * - DTS/ESI-0019472-1
      - Electronic Signatures and Trust Infrastructures (ESI); Profiles for Electronic Attestations of Attributes; Part 1: General requirements Profiles for EAA - General requirements 
    * - W3C_Digital_Credentials_API
      - Digital Credentials API (ARF) - Obbligatoria/Raccomandata
    * - W3C_WebAuthn
      - Web Authentication, An API for accessing Public Key Credentials Level 2 (ARF) - Obbligatorio secondo ARF, non legalmente vincolante
    * - CTAP
      - Client to Authenticator Protocol (CTAP) Review Draft (ARF)
    
Digital Credential Revocation Check Mechanisms
----------------------------------------------

.. list-table::
    :widths: 25 75
    :header-rows: 0

    * - `TOKEN-STATUS-LIST`_
      - Tobias Looker and Paul Bastian and Christian Bormann,  "Token Status List", February 2025, Draft 7.
    * - `OAUTH-STATUS-ASSERTION`_
      - De Marco, G., Steele, O., Marino, F., Adomeit, M., "OAuth Status Assertions", June 2024, Draft 3.

National Data Interoperability Platform Specifications
------------------------------------------------------

.. list-table::
    :widths: 25 75
    :header-rows: 0

    * - `MODI`_
      - "Linee Guida sull'interoperabilità tecnica delle Pubbliche Amministrazioni", November 2023, Version 1.2.
    * - `PDND`_
      - "Linee Guida sull'infrastruttura tecnologica della Piattaforma Digitale Nazionale Dati per l'interoperabilità dei sistemi informativi e delle basi di dati", December 2021, Version 1.0.

National Digital Identity Platform Specifications
------------------------------------------------------

.. list-table::
    :widths: 25 75
    :header-rows: 0

    * - `SPID/CIE-OpenID-Connect-Specifications`_
      - SPID/CIE OpenID Connect.


Identity Proofing
-----------------

.. list-table::
    :widths: 25 75
    :header-rows: 0

    * - ETSI_Identity_Proofing
      - ETSI: Policy and security requirements for trust service components for identity proofing
    * - CEN_Biometric_Attack_Detection
      - CEN: Biometric injection attack detection for remote registration
    * - CEN_Biometric_Requirements
      - CEN: European Requirements for Biometric Products

Biometric Data
--------------

.. list-table::
    :widths: 25 75
    :header-rows: 0

    * - ISO_19794_5
      - Biometric data interchange formats
    * - ISO_39794
      - Information technology — Extensible biometric data interchange formats


Onboarding and Interfaces
-------------------------

.. list-table::
    :widths: 25 75
    :header-rows: 0

    * - CEN_Onboarding_Guidelines
      - CEN: Guidelines for the onboarding of user personal identification data within European Digital Identity Wallets
    * - ETSI_Wallet_Interfaces
      - ETSI: Wallet interfaces for trust services


General Certification and Conformity
------------------------------------

.. list-table::
    :widths: 25 75
    :header-rows: 0

    * - ISO_17020
      - Conformity assessment — Requirements for the operation of various types of bodies performing inspection
    * - ISO_17021
      - Conformity assessment — Requirements for bodies providing audit and certification of management systems
    * - ISO_17025
      - General requirements for the competence of testing and calibration laboratories
    * - ISO_17029
      - Conformity assessment — General principles and requirements for validation and verification bodies
    * - ISO_17065
      - Conformity assessment — Requirements for bodies certifying products, processes, and services
    * - ISO_17067
      - Conformity assessment — Fundamentals of product certification and guidelines for product certification schemes
    * - ISO_IEC_30111_2019
      - Vulnerability management policy and procedures
    * - ISO_IEC_27001_2022
      - ISMS (IA1-CER)
    * - ISO_IEC_15408_3_2022
      - Evaluation criteria for IT security (IA1-CER)
    * - ISO_IEC_17000_2020
      - Conformity assessment — Vocabulary and general principles


Identity Management on Personal Devices
----------------------------------------

.. list-table::
    :widths: 25 75
    :header-rows: 0

    * - ISO-IEC DTS 23220-2
      - Cards and securioty devices for personal identification - Building blocks for Identity Management via Mobile Devices - Part 2: data objects and encoding rules for generic eID systems.
    * - ISO_Mobile_Identity_Management
      - ISO JTC1 SC17: Identity management via mobile devices & mobile driving license

Electronic Signatures and Infrastructures
-----------------------------------------

.. list-table::
    :widths: 25 75
    :header-rows: 0

    * - ETSI_TS_119_612
      - Electronic Signatures and Infrastructures (ESI); Trusted Lists (ARF) - Obbligatorio secondo ARF, non legalmente vincolante
    * - ETSI_TS_119_431_1
      - Policy and security requirements for trust service providers; Part 1: TSP service components operating a remote QSCD / SCDev. (ARF) - Obbligatorio secondo ARF, non legalmente vincolante
    * - ETSI_TS_119_431_2
      - Policy and security requirements for trust service providers; Part 2: TSP service components supporting AdES digital signature creation (ARF) - Obbligatorio secondo ARF, non legalmente vincolante
    * - ETSI_TS_119_432
      - Protocols for remote digital signature creation (ARF) - Obbligatorio secondo ARF, non legalmente vincolante
    * - ETSI_EN_319_132_1
      - XAdES digital signatures; Part 1: Building blocks and XAdES baseline signatures (XAdES) (IA1-INT) - Obbligatoria
    * - ETSI_TS_119_182_1
      - JAdES digital signatures; Part 1: Building blocks and JAdES baseline signatures (IA1-INT) - Obbligatoria
    * - ETSI_EN_319_122_1
      - CAdES digital signatures; Part 1: Building blocks and CAdES baseline signatures (IA1-INT) - Obbligatoria
    * - ETSI_EN_319_162_1
      - Associated Signature Containers (ASiC); Part 1: Building blocks and ASiC baseline containers (IA1-INT) - Obbligatoria
    * - ETSI_EN_319_142
      - PAdES digital signatures; Part 1: Building blocks and PAdES baseline signatures (IA1-INT) - Obbligatoria


Remote Signatures and Trust Services
------------------------------------

.. list-table::
    :widths: 25 75
    :header-rows: 0

    * - ETSI_Remote_Signature_Requirements
      - ETSI: Policy and security requirements for trust service providers used for remote signatures.
    * - CEN_Server_Signing_Systems
      - CEN: Trustworthy Systems supporting server signing
    * - CSC_Remote_Signature_Protocols
      - CSC: Cloud Signature Consortium Architectures and protocols for remote signature applications (CSC API v2)
    * - ETSI_Signing_Interfaces
      - ETSI: Wallet interfaces for signing

Security and Protection Profiles
--------------------------------

.. list-table::
    :widths: 25 75
    :header-rows: 0

    * - CEN_Protection_Profiles
      - CEN TC224 WG17: Common Criteria Protection Profiles for the EU Digital Identity Wallet


GlobalPlatform and Secure Elements
----------------------------------

.. list-table::
    :widths: 25 75
    :header-rows: 0

    * - GPC_GUI_217
      - GlobalPlatform SAM Configuration Technical specification for implementation of Secured Applications for Mobile
    * - GP_CS_GPC_SPE_034
      - GPC_SPE_034 Card Specification, v2.3.1
    * - GPC_SPE_007
      - GlobalPlatform Amendment A Confidential Card Content Management v1.2 2019-07
    * - GPC_SPE_013
      - GlobalPlatform Amendment D Secure Channel Protocol 03 v1.2 2020-04
    * - GPC_SPE_093
      - GlobalPlatform Amendment F Secure Channel Protocol 11 v1.4 2024-03
    * - GP_OMAPI_GPD_SPE_075
      - Accesso ai secure elements su dispositivi
    * - GSMA_SAM_01
      - Secured Applications for Mobile – Requirements for supporting 3rd party Applets on eSIM and eSE via SAM


Other Specifications
--------------------

.. list-table::
    :widths: 25 75
    :header-rows: 0

    * - :rfc:`2119`
      - Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels" BCP 14, RFC 2119, March 1997.
    * - :rfc:`2616`
      - Fielding, R., Gettys, J., Mogul, J., Frystyk, H., Masinter, L., Leach, P., and T. Berners-Lee, “Hypertext Transfer Protocol -- HTTP/1.1,” RFC 2616, June 1999.
    * - :rfc:`2898`
      - Kaliski, B., "PKCS #5: Password-Based Cryptography Specification-Version 2.0", RFC 2898, September 2000.
    * - :rfc:`3339`
      - Klyne, G. and C. Newman, "Date and Time on the Internet: Timestamps", RFC 3339, DOI 10.17487/RFC3339, July 2002.
    * - :rfc:`3986`
      - Uniform Resource Identifier (URI): Generic Syntax.
    * - :rfc:`7159`
      - Bray, T., "The JavaScript Object Notation (JSON) Data Interchange Format" RFC 7159, March 2014.
    * - :rfc:`8174`
      - Leiba, B., "Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words", RFC 8174, DOI 10.17487/RFC8174, May 2017.
    * - USASCII
      - American National Standards Institute, "Coded Character Set -- 7-bit American Standard Code for Information Interchange", 1986.
    * - `W3C-SRI`_
      - Akhawe, D., Braun, F., Marier, F., and J. Weinberger, "Subresource Integrity", 23 June 2016.
    * - `OIDC`_
      - Sakimura, N., Bradley, J., Jones, M.,  de Medeiros, B., Mortimore, C., "OpenID Connect Core 1.0 incorporating errata set 2", December 2023.
    * - `OIDC-IDA`_
      - Lodderstedt, T., Fett, D., Haine, M., Pulido, A., Lehmann, K., Koiwai, K., "OpenID Connect for Identity Assurance 1.0", 24 July 2024.

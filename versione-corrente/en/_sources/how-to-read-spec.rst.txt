How to Read the Specification
-----------------------------

This specification is designed to fulfil the requirements from multiple stakeholders within the IT-Wallet ecosystem. Each role has different responsibilities and scopes, and therefore different information needs. This section provides tailored reading paths to help you navigate efficiently to the content most relevant to the implementation goals.

Specification Structure Overview
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The specification is organized into the following major sections:

**Section** :ref:`introduction:Introduction`: 
  Establishes scope, and normative language for the IT-Wallet ecosystem.

**Section** :ref:`design:Design Principles`: 
  Provides design principles, and brand identity requirements for the IT-Wallet ecosystem.

**Section** :ref:`architecture-overview:Architecture Overview`:
  Provides high-level system functionalities and guidance for navigating the specification based on implementation requirements.

**Section** :ref:`trust:The Infrastructure of Trust`:
  Defines the federation-based trust model, entity relationships, and trust evaluation mechanisms that secure the entire ecosystem.

**Section** :ref:`entities:Entities`: 
  Comprehensive implementation requirements for each ecosystem participant: Wallet Solutions, Credential Issuers, Relying Parties, and Authentic Sources, including their components, interaction patterns, and configuration requirements.

**Section** :ref:`digital-credential-management:Digital Credential Management`: 
  Covers Digital Credential data models and formats, lifecycle management, validity verification, and the Credentials catalogue structure.

**Section** :ref:`digital-credential-flows:Digital Credential Flows`:
  Detailed implementation guidance for Digital Credential issuance and presentation workflows, including both remote and proximity interaction flows.

**Section** :ref:`endpoints:Endpoints`: 
  Technical specifications for all API endpoints exposed by each entity type, including federation endpoints and specialized service integrations.

**Section** :ref:`algorithms:Cryptographic Algorithms`, :ref:`security-privacy-considerations:Security and Privacy Considerations`, and :ref:`log-retention-policy:General Log Retention Policies` (**Implementation Support**): 
  Cryptographic requirements, security and privacy considerations, and log retention policies essential for compliant implementations.

**Section** :ref:`defined-terms-and-references:Defined Terms and References`, :ref:`contribute:How to contribute`, and :ref:`open-source:Open Source Releases` (**Terminology and References**):
  Comprehensive terminology, normative references, contribution guidelines.

**Section** :ref:`appendix:Appendix`: 
  Provides supplementary technical details, implementation patterns, and testing frameworks including mobile application instance management, national platform integration specifications, and comprehensive test matrices for ecosystem validation.


Reading Paths by Role
^^^^^^^^^^^^^^^^^^^^^

Before diving into role-specific sections, all readers should be familiar with the foundational concepts outlined in Sections :ref:`introduction:Introduction`, :ref:`architecture-overview:Architecture Overview`, and :ref:`trust:The Infrastructure of Trust`, which establish the common vocabulary, design principles, and trust infrastructure that provide the underlying framework for the entire ecosystem.

Wallet Provider
"""""""""""""""

Readers implementing or operating a **Wallet Provider** Solution should focus on understanding how to securely manage Digital Credentials and facilitate User interactions with other ecosystem participants.

**Essential sections:**

* **Section** :ref:`wallet-solution:Wallet Solution`: Complete wallet implementation requirements, components, and interaction processes.
* **Section** :ref:`digital-credential-management:Digital Credential Management`: Digital Credential data models, formats and lifecycle management.
* **Section** :ref:`digital-credential-flows:Digital Credential Flows`: Issuance and presentation flows for Digital Credentials.
* **Section** :ref:`wallet-provider-endpoint:Wallet Provider Endpoints`: Federation and IT-Wallet specific API specifications.
* **Section** :ref:`algorithms:Cryptographic Algorithms`: Security and cryptographic implementation requirements.
* **Section** :ref:`mobile-application-instance:Mobile Application Instance`: Mobile-specific implementation patterns.
* **Section** :ref:`e-service-pdnd:e-Service PDND`: Integration with the National Data Interoperability Platform.

**Secondary sections:**

* **Section** :ref:`credential-issuer-solution:Credential Issuer Solution`: Understanding issuer interactions and requirements.
* **Section** :ref:`relying-party-solution:Relying Party Solution`: Understanding RP interactions and presentation protocols.


Credential Issuer
"""""""""""""""""

For readers who are interested in implementing a **Credential Issuer** Solution, they should focus on the Digital Credential lifecycle and issuance interaction flows.

**Essential sections:**

* **Section** :ref:`credential-issuer-solution:Credential Issuer Solution`: Credential Issuer Solution - Complete Issuer implementation requirements and component details.
* **Section** :ref:`authentic-sources:Authentic Sources`: Understanding authoritative data source integration patterns.
* **Section** :ref:`digital-credential-management:Digital Credential Management`: Digital Credential formats and lifecycle management.
* **Section** :ref:`credential-issuance:Digital Credential Issuance`: Detailed issuance flow implementation.
* **Section** :ref:`credential-issuer-endpoint:Credential Issuer Endpoints`: Federation and issuance-specific API specifications.
* **Section** :ref:`algorithms:Cryptographic Algorithms`:  Signing algorithms and security implementation requirements.

**Secondary sections:**

* **Section** :ref:`wallet-solution:Wallet Solution`: Understanding Wallet Instance interactions and requirements.
* **Section** :ref:`credential-presentation:Digital Credential Presentation`: Understanding how Digital Credentials are presented in both remote and proximity scenario.
* **Section** :ref:`e-service-pdnd:e-Service PDND`: Integration with the National Data Interoperability Platform.

.. note::

    If the Credential Issuer authenticates the User it must comply with Section :ref:`credential-presentation:Digital Credential Presentation`. If the Authentic Source providing User's attributes belongs to the public sector it must comply with Section :ref:`e-service-pdnd:e-Service PDND`.  

Authentic Source
""""""""""""""""

If the reader wants to operate an **Authentic Source**, the focus should be on secure data provision and integration with Credential Issuers.

**Essential sections:**

* **Section** :ref:`authentic-sources:Authentic Sources`: Requirements and integration patterns with Credential Issuers.
* **Section** :ref:`authentic-source-endpoint:Authentic Source Endpoints`: API specifications and catalogue integration.
* **Section** :ref:`algorithms:Cryptographic Algorithms`: Data integrity, authentication, and security requirements.
* **Section** :ref:`e-service-pdnd:e-Service PDND`: PDND integration and interoperability requirements.

**Secondary sections:**

* **Section** :ref:`credential-issuer-solution:Credential Issuer Solution`: Understanding Credential Issuers main components and integration processes.
* **Section** :ref:`digital-credential-management:Digital Credential Management`: Understanding how authoritative data and attributes becomes Digital Credentials, and how their lifecycle is managed.

Relying Party
"""""""""""""

Readers interested in implementing or operating a **Relying Party** Solution to accept and verify Digital Credentials should focus on presentation protocols and verification mechanisms.

**Essential sections:**

* **Section** :ref:`relying-party-solution:Relying Party Solution`: Complete verifier implementation requirements and Entity Configuration.
* **Section** :ref:`digital-credential-management:Digital Credential Management`: Understanding Digital Credential formats and validity verification.
* **Section** :ref:`credential-presentation:Digital Credential Presentation`: Presentation flow implementation for both remote and proximity scenarios.
* **Section** :ref:`relying-party-endpoint:Relying Party Endpoints`: Federation and verification related API specifications.
* **Section** :ref:`algorithms:Cryptographic Algorithms`: Cryptographic suite requirements.

**Secondary sections:**

* **Section** :ref:`wallet-solution:Wallet Solution`: Understanding Wallet Instance interactions and presentation protocols
* **Section** :ref:`mobile-application-instance:Mobile Application Instance`: Mobile-specific implementation patterns.

Cross-Cutting Topics
^^^^^^^^^^^^^^^^^^^^

Regardless of your primary role, certain sections contain information relevant to all ecosystem participants:

**Security and Compliance:**
    All implementers must implement their solutions according to Section :ref:`security-privacy-considerations:Security and Privacy Considerations` and Section :ref:`log-retention-policy:General Log Retention Policies`.

**Standards and References:**
    Section :ref:`defined-terms-and-references:Defined Terms and References` provides normative references, defined terms, and technical standards to enable secure and proper interoperability among all participants.

**Testing and Validation:**
    Section :ref:`test-plans:Test Plans` provides a comprehensive test matrix for validating implementations across different roles and interaction flows.

Implementation Approach
^^^^^^^^^^^^^^^^^^^^^^^

The following phased reading approach is suggested:

    1. **Foundation Phase**: Read  Sections :ref:`introduction:Introduction`, :ref:`architecture-overview:Architecture Overview`, and :ref:`trust:The Infrastructure of Trust` to establish conceptual understanding of the IT-Wallet paradigm, design principles, and trust infrastructure.
    2. **Role-Specific Phase**: Focus on primary role's essential sections to understand specific implementation requirements, main technical component, the general architecture and interaction flows (see Section :ref:`entities:Entities` and Section :ref:`endpoints:Endpoints` for more details).
    3. **Integration Phase**: Review secondary sections relevant to interactions with other ecosystem participants and platform integration requirements.
    4. **Validation Phase**: Study security considerations, testing guidance, and compliance requirements according to Sections :ref:`security-privacy-considerations:Security and Privacy Considerations`, :ref:`log-retention-policy:General Log Retention Policies`, and :ref:`test-plans:Test Plans` for additional information.

.. note::

    For implementers working on solutions that span multiple roles (e.g., a combined Issuer Relying Party Solutions), it is recommended reviewing the sections for all relevant roles before proceeding with the developments. It is important to take particular note of Entity Configuration requirements and federation flows that apply to multiple roles.




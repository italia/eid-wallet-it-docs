How to Read the Specification
-----------------------------

This specification is designed to fulfil the requirements from multiple stakeholders within the IT-Wallet ecosystem. Each role has different responsibilities and scopes, and therefore different information needs. This section provides tailored reading paths to help you navigate efficiently to the content most relevant to the implementation goals.

Specification Structure Overview
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The specification is organized into the following major sections:

**Section** :ref:`introduction:Introduction`: 
  Establishes scope, and normative language for the IT-Wallet ecosystem.

**Section** :ref:`architecture-overview:Architecture Overview`:
  Provides high-level view on the Architecture in terms of governance and operational processes enabled.

**Section** :ref:`brand-identity:Brand Identity`:
  Provides the IT-Wallet Brand Identity requirements, guidance on the naming convention and on the application of the visual elements that identify the ecosystem.

**Section** :ref:`functionalities:User Experience Design`: 
  Provides design principles and high-level functional requirements to ensure a high-quality User Experience across all stages of interaction between the User and the service.

**Section** :ref:`trust-infrastructure:The Infrastructure of Trust`:
  Defines the federation-based trust model, entity relationships, and trust evaluation mechanisms that secure the entire ecosystem.

**Section** :ref:`entities:Entities`: 
  Comprehensive implementation requirements for each ecosystem participant: Wallet Solutions, Credential Issuers, Relying Parties, and Authentic Sources, including their components, interaction patterns, and configuration requirements.

**Section** :ref:`digital-credential-management:Digital Credential Management`: 
  Covers Digital Credential data models and formats, lifecycle management, validity verification, and the Credentials Catalog structure.

**Section** :ref:`digital-credential-flows:Digital Credential Flows`:
  Detailed implementation guidance for Digital Credential issuance and presentation workflows, including both remote and proximity interaction flows.

**Section** :ref:`endpoints:Endpoints`: 
  Technical specifications for all API endpoints exposed by each entity type, including federation endpoints and specialized service integrations.

**Section** :ref:`algorithms:Cryptographic Algorithms`, :ref:`security-privacy-considerations:Security and Privacy Considerations`, and :ref:`log-retention-policy:General Log Retention Policies` (**Implementation Support**): 
  Cryptographic requirements, security and privacy considerations, and log retention policies essential for compliant implementations.

**Section** :ref:`defined-terms-and-references:Defined Terms and References`, :ref:`official-resources:Official Resources`, :ref:`contribute:How to contribute`, and :ref:`open-source:Open Source Releases` (**Terminology and References**):
  Comprehensive terminology, normative references, additional documentation, tools, resources and contribution guidelines.

**Section** :ref:`appendix:Appendix`: 
  Provides supplementary technical details, implementation patterns, and testing frameworks including mobile application instance management, national platform integration specifications, and comprehensive test matrices for ecosystem validation.


Quick paths by objective
^^^^^^^^^^^^^^^^^^^^^^^^

Use these summaries when you already know your goal; the role sections below expand each path.

**Wallet Provider** — *Ship a Wallet Solution:* :ref:`wallet-solution:Wallet Solution`, :ref:`wallet-provider-endpoint:Wallet Provider Endpoints`; *move Credentials end-to-end:* :ref:`digital-credential-flows:Digital Credential Flows`; *federation and crypto:* :ref:`trust-infrastructure:The Infrastructure of Trust`, :ref:`algorithms:Cryptographic Algorithms`; *security and privacy:* :ref:`security-privacy-considerations:Security and Privacy Considerations`.

**Credential Issuer** — *Issue Credentials:* :ref:`credential-issuer-solution:Credential Issuer Solution`, :ref:`credential-issuance:Digital Credential Issuance`, :ref:`credential-issuer-endpoint:Credential Issuer Endpoints`; *authoritative data:* :ref:`authentic-sources:Authentic Sources`; *if you authenticate Users:* :ref:`credential-presentation:Digital Credential Presentation`; *security:* :ref:`security-privacy-considerations:Security and Privacy Considerations`.

**Authentic Source** — *Expose authoritative data:* :ref:`authentic-sources:Authentic Sources`, :ref:`authentic-source-endpoint:Authentic Source Endpoints`; *integrity and national platforms:* :ref:`algorithms:Cryptographic Algorithms`, :ref:`e-service-pdnd:e-Service PDND`.

**Relying Party** — *Verify User Credentials:* :ref:`relying-party-solution:Relying Party Solution`, :ref:`credential-presentation:Digital Credential Presentation`, :ref:`relying-party-endpoints:Relying Party Endpoints`; *formats and validity:* :ref:`digital-credential-management:Digital Credential Management`; *security:* :ref:`security-privacy-considerations:Security and Privacy Considerations`.


Reading by project phase
------------------------

For easier access to the topics in these specifications, a role-based reading path is presented below. This path considers the phase in which each role operates within the IT-Wallet system and includes direct references to the relevant sections of the document. 

Authentic Sources
^^^^^^^^^^^^^^^^^

The Authentic Source is the owner of the data. Their role is to ensure that original information is transmitted correctly and made securely available to issuing systems, and kept up to date. 
**Focus**: Data availability, accuracy of transmitted information, constant alignment between the original database and the issued credentials. 

**Phase 1: Discovery**

**Objective**: To understand the reference context, technical requirements, and regulations necessary to become part of the Trust Chain upon which the entire system is founded. 

- **Section** :ref:`introduction:Introduction`: Understanding the scope and regulatory language of the IT-Wallet ecosystem. 

- **Section** :ref:`architecture-overview:Architecture Overview`: Overview of the IT-Wallet system architecture in terms of governance and enabled operational processes. 

- **Section** :ref:`trust-infrastructure:The Infrastructure of Trust`: Key requirements of the Trust Chain and registration in the Trust List to operate at both national and European levels. 

- **Section** :ref:`defined-terms-and-references:Defined Terms and References`: Regulatory references, defined terms, and technical standards enabling secure and correct interoperability between all participants. (Use this section for any questions regarding terminology, reference standards, or acronyms). 

**Phase 2: Design**

**Objective**: To understand the implementation requirements for the attributes deemed necessary to translate data into a standardized digital format (EAA) recognized by the Wallet. 

- **Section** :ref:`functionalities:User Experience Design`: How users obtain Electronic Attestations (:ref:`issuance-of-electronic-attestations-of-attributes:paragraph 5.4'). 

- **Section** :ref:`entities:Entities`: Including the attributes necessary to provide the Electronic Attestation requested by the User (:ref:`entities:authentic-sources`paragraph 10.4'). 

- **Section** :ref:`digital-credential-management:Digital Credential Management`: Technical requirements for designing and managing the lifecycle of attestations. 

**Phase 3: Implementation**

**Objective**: To adopt the requirements needed to create the technological interfaces (APIs) required to communicate with Credential Issuers, managing the entire data lifecycle. 

- **Section** :ref:`endpoints:Endpoints`: Implementation of APIs enabling the Credential Issuer to securely and consistently retrieve authoritative data (:ref:`authentic-source-endpoint:paragraph 13.4'). 

- **Section** :ref:`digital-credential-management:Digital Credential Management`: Lifecycle and management of Electronic Attestations (with particular reference to :ref:`credential-revocation:paragraph 11.3'). 

- **Section** :ref:`security-privacy-considerations:Security and Privacy Considerations`: Security and compliance requirements for implemented solutions. 

- **Section** :ref:`log-retention-policy:General Log Retention Policies`: Log retention requirements in accordance with ISO/IEC 27001 

**Phase 4: Registration**

**Objective**: To become accredited as an Authentic Source within the system by following the administrative and technical procedures that guarantee the entity's reliability. 

- **Section** :ref:`onboarding-high-level:Onboarding System': Participation in the IT-Wallet ecosystem and data recognition across all actors (:ref:`authentic-source-registration-process:paragraph 4.2'). 

- **Section** :ref:`x5c-evaluation:X.509 Certificate Management Operations': Operational procedures for managing X.509 Certificates within the IT-Wallet federation

Wallet Provider
^^^^^^^^^^^^^^^

The Wallet Provider is the entity that designs the digital wallet, whether public or private. They serve as the direct point of contact for the citizen; their challenge is to combine a fluid and intuitive user experience with the highest security standards. 
**Focus**: Compliance with protocols and security standards, fluidity of the user experience, adherence to IT-Wallet system guidelines. 

**Phase 1: Discovery**

**Objective**: To understand the reference context, technical requirements, and regulations necessary to become part of the Trust Chain.  

- **Section** :ref:`introduction:Introduction`: Understanding the scope and regulatory language of the IT-Wallet ecosystem. 

- **Section** :ref:`architecture-overview:Architecture Overview`: Overview of the IT-Wallet system architecture in terms of governance and enabled operational processes. 

- **Section** :ref:`trust-infrastructure:The Infrastructure of Trust`: Key requirements of the Trust Chain and registration in the Trust List to operate at both national and European levels. 

- **Section** :ref:`defined-terms-and-references:Defined Terms and References`: Regulatory references, defined terms, and technical standards enabling secure and correct interoperability between all participants. (Use this section for any questions regarding terminology, reference standards, or acronyms). 

**Phase 2: Design**

**Objective**: To define the Wallet's visual identity, design the user experience, model the technical entity, and select the cryptographic algorithms that will ensure data protection on the device. 

- **Section** :ref:`brand-identity:Brand Identity': Ensuring the App complies with communication guidelines and the visual identity of the IT-Wallet system. 

- **Section** :ref:`functionalities:User Experience Design`: Designing simple and secure interfaces, ensuring an immediate and intuitive user experience. 

- **Section** :ref:`entities:Entities`: Implementation requirements and attributes needed to configure the entity (:ref:`wallet-solution:paragraph 10.1'). 

- **Section** :ref:`digital-credential-management:Digital Credential Management`: Technical requirements for designing and managing the lifecycle of attestations. 

- **Section** :ref:`algorithms:Cryptographic Algorithms': Selection and implementation of cryptographic standards required to secure keys and transactions. 

**Phase 3: Implementation**

**Objective**: To implement communication endpoints and adopt technological standards (e.g., SD-JWT) that ensure the Wallet can interface with other actors.

- **Section** :ref:`endpoints:Endpoints`: Implementation of the Wallet Provider’s interfaces (APIs) required for system interoperability (:ref:`wallet-provider-endpoint:paragraph 13.1'). 

- **Section** :ref:`security-privacy-considerations:Security and Privacy Considerations`: Security and compliance requirements for implemented solutions. 

- **Section** :ref:`log-retention-policy:General Log Retention Policies`: Log retention requirements in accordance with ISO/IEC 27001 

**Phase 4: Registration**

**Objective**: To become accredited as a Wallet Provider so that citizens' Wallet Instances are recognized as valid by the system.  

- **Section** :ref:`onboarding-high-level:Onboarding System': Participation methods and data recognizability (:ref:`wallet-provider-operator-journey:paragraph 4.5.4'). 

- **Section** :ref:`x5c-evaluation:X.509 Certificate Management Operations': Operational procedures for managing X.509 Certificates within the IT-Wallet federation

- **Section**: :ref:`est-plans:Test Plans': Information on how test environments support implementers, auditors, and compliance testing in validating Wallet Solution behavior. 

Credential Issuer
^^^^^^^^^^^^^^^^^

The Credential Issuer is the technical provider of credentials. Its main task is to transform data received from Authentic Sources into secure digital attestations, ready to be issued to the Wallet. It is the technical hub ensuring interoperability through international standards like OpenID4VCI. 
**Focus**: Designing credentials from raw data, security of obtained data, credential lifecycle. 

**Phase 1: Discovery**

**Objective**: To understand the reference context, technical requirements, and regulations to join the Trust Chain.

- **Section** :ref:`introduction:Introduction`: Understanding the scope and regulatory language of the IT-Wallet ecosystem. 

- **Section** :ref:`architecture-overview:Architecture Overview`: Overview of the IT-Wallet system architecture in terms of governance and enabled operational processes. 

- **Section** :ref:`trust-infrastructure:The Infrastructure of Trust`: Key requirements of the Trust Chain and registration in the Trust List to operate at both national and European levels. 

- **Section** :ref:`defined-terms-and-references:Defined Terms and References`: Regulatory references, defined terms, and technical standards enabling secure and correct interoperability between all participants. (Use this section for any questions regarding terminology, reference standards, or acronyms).

**Phase 2: Design**

****Objective**: To technically design attestations by structuring metadata to meet technical and regulatory requirements, allowing the user to share only necessary information. 

- **Section** :ref:`functionalities:User Experience Design`: For high-level functional requirements supporting the User Experience during all interaction phases. 

- **Section** :ref:`entities:Entities`: Implementation requirements and attributes for configuring the Issuer profile (:ref:`credential-issuer-solution:paragraphs 10.2', :ref:`authentic-sources:10.4')

- **Section** :ref:`digital-credential-management:Digital Credential Management`: Technical requirements for designing and managing the lifecycle of attestations. 

- **Section** :ref:`algorithms:Cryptographic Algorithms': To meet security requirements by designing digital signature systems that make attestations unfalsifiable. 

**Phase 3: Implementation**

**Objective**: To develop issuing endpoints based on the OpenID4VCI protocol, implementing release, renewal, and technical lifecycle management functions.

- **Section** ref:`digital-credential-flows:`Digital Credential Flows': Detailed specifications on implementing issuance flows, presentation methods, and wallet information retrieval. 

- **Section** :ref:`endpoints:Endpoints`: Implementation of issuance interfaces, including the Credential Endpoint and Token Endpoint (:ref:`credential-issuer-endpoint:`paragraph 13.2'). 

- **Section** :ref:`security-privacy-considerations:Security and Privacy Considerations`: Security and compliance requirements for implemented solutions. 

- **Section** :ref:`log-retention-policy:General Log Retention Policies`: Log retention requirements in accordance with ISO/IEC 27001

**Phase 4: Registration**

**Objective**: To become accredited so that credentials issued to the Wallet are officially "trusted" and verifiable.  

- **Section** :ref:`onboarding-high-level:Onboarding System': Participation methods and data recognizability (:ref:`credential-issuer-operator-journey:paragraph 4.5.3'). 

- **Section** :ref:`x5c-evaluation:X.509 Certificate Management Operations': Operational procedures for managing X.509 Certificates within the IT-Wallet federation

- **Section**: :ref:`est-plans:Test Plans': Information on how test environments support implementers, auditors, and compliance testing in validating Wallet Solution behavior. 


Relying Party
^^^^^^^^^^^^^

The Relying Party is the end-user of the credentials. Its task is to transform digital verification into business value, while ensuring a fast, secure identification process that complies with data minimization principles. 
**Focus**: Designing the credential verification experience, respecting user privacy. 

**Phase 1: Discovery**

**Objective**: To understand the context and regulations to join the Trust Chain.

- **Section** :ref:`introduction:Introduction`: Understanding the scope and regulatory language of the IT-Wallet ecosystem. 

- **Section** :ref:`architecture-overview:Architecture Overview`: Overview of the IT-Wallet system architecture in terms of governance and enabled operational processes. 

- **Section** :ref:`trust-infrastructure:The Infrastructure of Trust`: Key requirements of the Trust Chain and registration in the Trust List to operate at both national and European levels. 

- **Section** :ref:`defined-terms-and-references:Defined Terms and References`: Regulatory references, defined terms, and technical standards enabling secure and correct interoperability between all participants. (Use this section for any questions regarding terminology, reference standards, or acronyms).

**Phase 2: Design**

****Objective**: To define verification requirements by establishing the attributes necessary to provide the service, and to design the request experience by defining data-sharing methods.  

- **Section** :ref:`brand-identity:Brand Identity': Ensuring that any verification applications comply with the communication guidelines and visual identity of the IT-Wallet system. 

- **Section** :ref:`functionalities:User Experience Design`: High-level functional requirements supporting the user experience across all interaction phases between the User and the service.  

- **Section** :ref:`entities:Entities`: Implementation requirements and attributes necessary to configure the Verifier profile (:ref:`relying-party-solution:paragraphs 10.3', :ref:`).

- **Section** :ref:`digital-credential-management:Digital Credential Management`: Formats of Electronic Credentials and methods for verifying their validity. 

- **Section** :ref:`algorithms:Cryptographic Algorithms': Design and implementation of digital signature validation systems ensuring the integrity of the data presented by the user. 

**Phase 3: Implementation**

**Objective**: To implement the OpenID4VP protocol to send requests to the Wallet and receive attestations, ensuring correct format decoding. 

- **Section** ref:`digital-credential-flows:`Digital Credential Flows':  Implementation of presentation flows for both remote and proximity scenarios (ref:`credential-presentation:`paragraph 12.2'). 

- **Section** :ref:`endpoints:Endpoints`: Implementation of receiving and verification interfaces (:ref:`relying-party-endpoints:`paragraph 13.3' and :ref:`relying-party-provider-backend-endpoints:`Relying Party Provider Backend Endpoints'). 

- **Section** :ref:`security-privacy-considerations:Security and Privacy Considerations`: Security and compliance requirements for implemented solutions. 

- **Section** :ref:`log-retention-policy:General Log Retention Policies`: Log retention requirements in accordance with ISO/IEC 27001

**Phase 4: Registration**

**Objective**: To become accredited as a secure and reliable actor when requesting user data.   

- **Section** :ref:`onboarding-high-level:Onboarding System': learning the methods for participating in the IT-Wallet ecosystem  (:ref:`relying-party-operator-journey:paragraph 4.5.5'). 

- **Section** :ref:`x5c-evaluation:X.509 Certificate Management Operations': Operational procedures for managing X.509 Certificates within the IT-Wallet federation

- **Section**: :ref:`est-plans:Test Plans': Information on how test environments support implementers, auditors, and compliance testing in validating Wallet Solution behavior. 






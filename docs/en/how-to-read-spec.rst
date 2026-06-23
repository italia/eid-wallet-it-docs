How to Read the Specification
-----------------------------

This specification is designed to fulfil the requirements from multiple stakeholders within the IT-Wallet System. Each role has different responsibilities and scopes, and therefore different information needs. This section provides tailored reading paths to help you navigate efficiently to the content most relevant to the implementation goals.

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

Role based reading
^^^^^^^^^^^^^^^^^^

Quick paths by objective
^^^^^^^^^^^^^^^^^^^^^^^^

Use these summaries when you already know your goal; the role sections below expand each path.

**Wallet Provider** — *Ship a Wallet Solution:* :ref:`wallet-solution:Wallet Solution`, :ref:`wallet-provider-endpoint:Wallet Provider Endpoints`; *move Credentials end-to-end:* :ref:`digital-credential-flows:Digital Credential Flows`; *federation and crypto:* :ref:`trust-infrastructure:The Infrastructure of Trust`, :ref:`algorithms:Cryptographic Algorithms`; *security and privacy:* :ref:`security-privacy-considerations:Security and Privacy Considerations`.

**Credential Issuer** — *Issue Credentials:* :ref:`credential-issuer-solution:Credential Issuer Solution`, :ref:`credential-issuance:Digital Credential Issuance`, :ref:`credential-issuer-endpoint:Credential Issuer Endpoints`; *authoritative data:* :ref:`authentic-sources:Authentic Sources`; *if you authenticate Users:* :ref:`credential-presentation:Digital Credential Presentation`; *security:* :ref:`security-privacy-considerations:Security and Privacy Considerations`.

**Authentic Source** — *Expose authoritative data:* :ref:`authentic-sources:Authentic Sources`, :ref:`authentic-source-endpoint:Authentic Source Endpoints`; *integrity and national platforms:* :ref:`algorithms:Cryptographic Algorithms`, :ref:`e-service-pdnd:e-Service PDND`.

**Relying Party** — *Verify User Credentials:* :ref:`relying-party-solution:Relying Party Solution`, :ref:`credential-presentation:Digital Credential Presentation`, :ref:`relying-party-endpoints:Relying Party Endpoints`; *formats and validity:* :ref:`digital-credential-management:Digital Credential Management`; *security:* :ref:`security-privacy-considerations:Security and Privacy Considerations`.


Reading paths by roles
^^^^^^^^^^^^^^^^^^^^^^^^

For easier access to the topics covered in these specifications, role-based reading paths are presented below. Each path is organized according to the different stages of onboarding to and participation the IT-Wallet System, with direct references to the sections most relevant to each role. 

The proposed reading paths are intended as guidance and do not replace the need to consult other sections when a broader understanding of the system is required. 

For entities interested in addressing multiple roles, it is recommended to deepen all the reading paths related to relevant roles. 

**Authentic Sources**


The Authentic Source focuses on securely exposing, managing, and guaranteeing the absolute accuracy and integrity of the authoritative raw data underlying (Q)EAA. 

**Phase 1: Discovery**

To understand the general functioning of the ecosystem, the technical architecture and the Infrastructure of Trust.

- **Section** :ref:`introduction:Introduction`: Scope and regulatory context of the IT-Wallet System. 

- **Section** :ref:`architecture-overview:Architecture Overview`: Overview of the IT-Wallet System architecture in terms of governance and enabled operational processes. 

- **Section** :ref:`trust-infrastructure:The Infrastructure of Trust`: Key requirements of the federation-based trust model and trust evaluation mechanisms between entities. 

- **Section** :ref:`defined-terms-and-references:Defined Terms and References`: Comprehensive terminology, normative references, additional documentation, tools, resources and contribution guidelines.

**Phase 2: Design**

To understand the requirements and design the features, functionalities and specific characteristics underlying a (Q)EAA to be issued.

- **Section** :ref:`functionalities:User Experience Design`: Key requirements on how to enable Users to obtain (Q)EAAs, (Q)EAA structures, status and management over time. 


- **Section** :ref:`digital-credential-management:Digital Credential Management`: Section digital-credential-management:Digital Credential Management: Technical and functional requirements related to (Q)EAA lifecycle. 
- **Section** :ref:`e-service-pdnd-template:PDND e-Service Template`: Standardized blueprint containing all necessary technical and descriptive metadata for the e-service definition.
**Phase 3: Implementation**

To implement the technological interfaces required to communicate with Credential Issuers and tomanage the entire (Q)EAA data lifecycle.
- **Section** :ref:`authentic-sources:Authentic Sources`: Authentic Source’s role and responsabilities.

- **Section** :ref:`e-service-pdnd:e-Service PDND`: Mandatory integration specifications with the PDND (National Digital Data Platform) and the associated interoperability requirements for publishing an e-service. 
- **Section** :ref:`authentic-source-endpoint:Authentic Source Endpoints`: Key requirements for the implementation of APIs enabling the Credential Issuer to securely and consistently retrieve authoritative data and to manage the data lifecycle throught Signal Hub endpoint. 

- **Section** :ref:`registry:Registry Infrastructure`: Focus on Registry components of interest to the Authentic Source. 

- **Section** :ref:`log-retention-policy:General Log Retention Policies`: General Log retention requirements and specific requirements for Authentic Sources in accordance with ISO/IEC 27001. 
- **Section** :ref:`test-plans:Test Plans`: Guide to set up the test environment and validate backend interactions with the test matrices provided by the ecosystem.
**Phase 4: Registration**

To become registered as an Authentic Source within the system by completing the administrative and technical procedures required. 

- **Section** :ref:`onboarding-high-level:Onboarding System': Overview of the onboarding system architecture and the Authentic Source registration process. 
- **Section** :ref:`entity-onboarding:Entity Onboarding`: Focus on technical implementation procedures for Authentic Source registration.
- **Section** :ref:`x5c-evaluation:X.509 Certificate Management Operations': Operational procedures for managing X.509 Certificates within the IT-Wallet federation.

**Wallet Provider**


The Wallet Provider focuses on designing and developing the Wallet Solution that enables the User to store, manage, and present their PID and (Q)EAAs. 

**Phase 1: Discovery**

To understand the general functioning of the ecosystem, the technical architecture and the Infrastructure of Trust. 

- **Section** :ref:`introduction:Introduction`: Scope and regulatory context of the IT-Wallet System. 

- **Section** :ref:`architecture-overview:Architecture Overview`: Overview of the IT-Wallet System architecture in terms of governance and enabled operational processes. 

- **Section** :ref:`trust-infrastructure:The Infrastructure of Trust`: Key requirements of the federation-based trust model and trust evaluation mechanisms between entities. 

- **Section** :ref:`defined-terms-and-references:Defined Terms and References`: Comprehensive terminology, normative references, additional documentation, tools, resources and contribution guidelines.

**Phase 2: Design**

To understand the User Experience requirements and design the Wallet Solution following common patterns to ensure the usability and accessibility of the solutions.

- **Section** :ref:`brand-identity:Brand Identity': Overview of the IT-Wallet Brand Identity and indications on assets to be adopted by the Wallet Provider.  

- **Section** :ref:`functionalities:User Experience Design`: Key requirements on Interaction Models and Interface layouts and graphic assets to ensure an effective and seamless User Experience and coherence among Wallet Solutions. 


- **Section** :ref:`digital-credential-management:Digital Credential Management`: Technical and functional requirements related to (Q)EAA lifecycle.


**Phase 3: Implementation**

To implement the Wallet Solution in line with specific technological standards to ensure the communication between the Wallet Solution and other actors.
- **Section** :ref:`wallet-solution:Wallet Solution`: Technical and functional requirements on components, functionalities and lifecycle to configure the Wallet Solution. 

- **Section** :ref:`digital-credential-flows:Digital Credential Flows`: Technical and functional requirements on (Q)EAA issuance and presentation flows. 
- **Section** :ref:`endpoints:Endpoints`: Implementation of the Wallet Provider’s interfaces (APIs) required for system interoperability (see paragraph :ref:`endpoints:Wallet Provider Endpoints'). 

- **Section** :ref:`security-privacy-considerations:Security and Privacy Considerations`: Security and compliance requirements for implemented solutions. 

- **Section** :ref:`log-retention-policy:General Log Retention Policies`: Log retention requirements in accordance with ISO/IEC 27001 

**Phase 4: Registration**

**Objective**: To become accredited as a Wallet Provider so that citizens' Wallet Instances are recognized as valid by the system.  

- **Section** :ref:`onboarding-high-level:Onboarding System': Participation methods and data recognizability (see paragraph :ref:`onboarding-high-level:Wallet Provider Operator Journey'). 

- **Section** :ref:`x5c-evaluation:X.509 Certificate Management Operations': Operational procedures for managing X.509 Certificates within the IT-Wallet federation

- **Section**: :ref:`est-plans:Test Plans': Information on how test environments support implementers, auditors, and compliance testing in validating Wallet Solution behavior. 

**Credential Issuer**

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

- **Section** :ref:`entities:Entities`: Implementation requirements and attributes for configuring the Issuer profile (see paragraphs :ref:`entities:Credential Issuer Solution', and :ref:`entities:Authentic Sources')

- **Section** :ref:`digital-credential-management:Digital Credential Management`: Technical requirements for designing and managing the lifecycle of attestations. 

- **Section** :ref:`algorithms:Cryptographic Algorithms': To meet security requirements by designing digital signature systems that make attestations unfalsifiable. 

**Phase 3: Implementation**

**Objective**: To develop issuing endpoints based on the OpenID4VCI protocol, implementing release, renewal, and technical lifecycle management functions.

- **Section** ref:`digital-credential-flows:`Digital Credential Flows': Detailed specifications on implementing issuance flows, presentation methods, and wallet information retrieval. 

- **Section** :ref:`endpoints:Endpoints`: Implementation of issuance interfaces, including the Credential Endpoint and Token Endpoint (see paragraph :ref:`endpoints:`Credential Issuer Endpoints'). 

- **Section** :ref:`security-privacy-considerations:Security and Privacy Considerations`: Security and compliance requirements for implemented solutions. 

- **Section** :ref:`log-retention-policy:General Log Retention Policies`: Log retention requirements in accordance with ISO/IEC 27001

**Phase 4: Registration**

**Objective**: To become accredited so that credentials issued to the Wallet are officially "trusted" and verifiable.  

- **Section** :ref:`onboarding-high-level:Onboarding System': Participation methods and data recognizability (see paragraph :ref:`onboarding-high-level:Credential Issuer Operator Journey'). 

- **Section** :ref:`x5c-evaluation:X.509 Certificate Management Operations': Operational procedures for managing X.509 Certificates within the IT-Wallet federation

- **Section**: :ref:`est-plans:Test Plans': Information on how test environments support implementers, auditors, and compliance testing in validating Wallet Solution behavior. 


**Relying Party**


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

- **Section** :ref:`entities:Entities`: Implementation requirements and attributes necessary to configure the Verifier profile (see paragraph :ref:`entities:Relying Party Solution').

- **Section** :ref:`digital-credential-management:Digital Credential Management`: Formats of Electronic Credentials and methods for verifying their validity. 

- **Section** :ref:`algorithms:Cryptographic Algorithms': Design and implementation of digital signature validation systems ensuring the integrity of the data presented by the user. 

**Phase 3: Implementation**

**Objective**: To implement the OpenID4VP protocol to send requests to the Wallet and receive attestations, ensuring correct format decoding. 

- **Section** ref:`digital-credential-flows:`Digital Credential Flows':  Implementation of presentation flows for both remote and proximity scenarios (see paragraph ref:`digital-credential-flows:`Digital Credential Presentation'). 

- **Section** :ref:`endpoints:Endpoints`: Implementation of receiving and verification interfaces (see paragraphs :ref:`endpoints:`Relying Party Endpoints' and :ref:`endpoints:Relying Party Provider Backend Endpoints'). 

- **Section** :ref:`security-privacy-considerations:Security and Privacy Considerations`: Security and compliance requirements for implemented solutions. 

- **Section** :ref:`log-retention-policy:General Log Retention Policies`: Log retention requirements in accordance with ISO/IEC 27001

**Phase 4: Registration**

**Objective**: To become accredited as a secure and reliable actor when requesting user data.   

- **Section** :ref:`onboarding-high-level:Onboarding System': learning the methods for participating in the IT-Wallet ecosystem  (see paragraph :ref:`ronboarding-high-level:Relying Party Operator Journey'). 

- **Section** :ref:`x5c-evaluation:X.509 Certificate Management Operations': Operational procedures for managing X.509 Certificates within the IT-Wallet federation

- **Section**: :ref:`est-plans:Test Plans': Information on how test environments support implementers, auditors, and compliance testing in validating Wallet Solution behavior. 

NOTE

For implementers working on solutions that cover multiple roles (e.g., a combination of Credential Provider Solutions and Relying Parties), it is recommended to review the sections for all relevant roles before proceeding with development. It is important to pay particular attention to Entity Configuration requirements and to federation flows that apply across multiple roles.






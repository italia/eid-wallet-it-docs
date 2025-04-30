.. include:: ../common/common_definitions.rst


Normative References
====================

Below the normative references and respective acronyms included in these Technical Specifications:

[CAD]

Legislative Decree No. 82 of March 7, 2005, as amended, containing the 'Digital Administration Code'.

[REF_ACCESSIBILITY]

Accessibility Guidelines for IT Tools as per Article 11 of Law 4/2004.
Directive (EU) 2019/882 of the European Parliament and of the Council of 17 April 2019 on the accessibility requirements for products and services.

[GL_DESIGN]

Design Guidelines for websites and digital services provided by public administrations, pursuant to Article 53, paragraph 1-ter of Legislative Decree No. 82 of March 7, 2005, as amended.


Defined Terms and Acronyms
==========================

The terms *User*, *Trust Service*, *Trust Model*, *Trusted List*, *Trust Framework*, *Attribute*, *Electronic Attestations of Attributes Provider* or *Trust Service Provider (TSP)*, *Person Identification Data (PID)*, *Revocation List*, *Qualified Electronic Attestations of Attributes Provider* or *Qualified Trust Service Provider (QTSP)*, *Electronic Attestation of Attributes (EAA)*, are defined in the `EIDAS-ARF`_.

Below is the description of acronyms and definitions which are useful for further insights into topics that complement the IT-Wallet System and the interacting components.

.. glossary::
    :sorted:

    **Accreditation Process**
      Process performed by the National Accreditation Body to accreditate CABs. As a result of the Accreditation Process, a NAB issues an accreditation certificate to a CAB.

    **Attributes**
    **User Attribute**
    **User Claim**
      A set of characteristics, qualities, rights, or permissions of a natural or legal person, or of an object, or even a single piece of such information. [Aligned with ARF v1.9.].

    **Personal Identification Data**
      A set of data which allow to establish the identity of a natural or legal person, or of a natural person representing another natural or legal person, to be established.

    **Authentication**
      An electronic process that enables the confirmation of the Electronic Identification of a natural or legal person, or the origin and integrity of data in electronic form (in the context of the Guidelines, for example, Attributes).

    **Authentic Source**
      Public entity or private entity responsible for the repository or system, considered a primary source for Attributes or for Personal Identification Data, and whose authenticity is recognized in accordance with Union or national law, including administrative practice. Depending on the context Authentic Source term can be directly referred to the repository or system held under the responsibility of a public entity or private entity.
    
    **Certification Process**
      Process performed by Conformity Assessment Bodies to certify the Wallet Solution. The Certification Process aims to periodically assess technical Wallet Solutions (e.g. performing vulnerability assessment and risk analysis). As a result of the Certification Process a certification is provided to the Wallet Solution.
    
    **Conformity Assessment Body (CAB)**
      A conformity assessment body as defined in Article 2, point 13, of Regulation (EC) No 765/2008, which is accredited in accordance with that Regulation as competent to carry out conformity assessment of a qualified trust service provider and the qualified trust services it provides, or as competent to carry out certification of Wallet Solutions or electronic identification means. [Aligned with ARF v1.9.].

    **Credential Issuer**
    **Issuer**
      An Organizational Entity providing Digital Credentials to Users. It may be PID Provider or (Q)EAA Providers.

    **Credential Status Assertion**
    **Status Assertion**
      Signed document serving as proof of a Digital Credential's current validity status.
    
    **Critical Assets**
      As defined in They are assets within or in relation to a Wallet Unit (for example cryptographic keys) of such importance that their incapacitation or destruction would have a very serious, debilitating effect on the ability to rely on the Wallet Unit. [Aligned with Art. 2 Commission Implementing Regulation `EU_2024/2982`_].

    **Cryptographic Hardware Key Tag**
      A unique identifier created by the operating system for the Cryptographic Hardware Keys, utilized to gain access to the private key stored in the hardware.
    
    **Cryptographic Hardware Keys**
      During the app initialization, the Wallet Instance generates a pair of keys, one public and one private, which remain valid for the entire duration of the Wallet Instance's life. Functioning as a Master Key for the personal device, these Cryptographic Hardware Keys are confined to the OS domain and are not designed for signing arbitrary payloads. Their primary role is to provide a unique identification for each Wallet Instance.
    
    **Device Integrity Service**
      A service provided by device manufacturers that verifies the integrity and authenticity of the app instance (Wallet Instance), as well as certifying the secure storage of private keys generated by the device within its dedicated hardware. It's important to note that the terminology used to describe this service varies among manufacturers.
    
    **Digital Credential**
    **Credential**
      A digitally signed set of Personal Identification Data or Attributes encapsulated in a specific data format, such as mDoc-CBOR format specified in [ISO 18013-5] or the SD-JWT VC format specified in [SD-JWT-VC], resistant to tampering and non-repudiation by its Credential Issuer. This may be a Personal Identification Data (PID), (Qualified) Electronic Attestation of Attribute ((Q)EAA). [Revised from ARF v1.9.]
      *Differences:* The definition from ARF restricts the data format to mDoc-CBOR and SD-JWT VC. A Digital Credential definition should be neutral on the format.

    **Federation Authority**
      A public governance entity that issues guidelines and technical rules and administers - directly or through its intermediary - Trusted Lists, services, and accreditation processes, the status of participants, and their eligibility evaluation. It also performs oversight functions.
    
    **Holder**
      Natural or Legal person that receives Digital Credentials from the Credential Issuers, manages the Digital Credentials within the Wallet Instance, and presents them to Verifiers. The Holder is the User in control of the Wallet.
    
    **Holder Key Binding**
    **Cryptographic Binding**
      Ability of the Holder to prove legitimate possession of the private part, related to the public part attested by a Trusted Third Party. [Revised from Art. 2 Commission Implementing Regulation `EU_2024/2982`_].
    
    **Identity and Access Management (IAM)**
      Identity and access management, or IAM, is a framework of business processes, policies and technologies that facilitates the management of digital identities. With an IAM framework in place, IT security teams can control user access to critical information within their organizations.
    
    **IT-Wallet System**
      Set of Technical Solutions that implement the "Italian Digital Wallet System" pursuant to Article 64-quater of [CAD].
    
    **Key Attestation**
      An attestation from the device's OEM that enhances your confidence in the keys used in your Wallet Instance being securely stored within the device's hardware-backed keystore. Its content is therefore defined by the operating system manufacturer. For Google Android, the term Key Attestation refers to the Strongbox Key Attestation feature. For Apple iOS, the reference is to the `Device Check`_ service, specifically the `attestKey`_ feature.
    
    **Level of Assurance**
      The degree of confidence in the vetting process used to establish the identity of the User and the degree of confidence that the User who presents the credential is the same User to whom the Digital Credential was issued.
    
    **Metadata**
      Digital artifact that contains all the required information about an Organizational Entity, e.g., protocol related endpoints and the Organizational Entity's cryptographic public keys (for the complete list check requirement “Metadata Content”).

    **National Accreditation Bodies (NAB)**
      A body that performs accreditation with authority derived from a Member State under Regulation (EC) No 765/2008. [Aligned with ARF v1.9.].

    **National Identity Provider**
      It represents preexisting identity systems based on SAML2 or OpenID Connect Core 1.0, already in production in each Member State (eg: the Italian SPID and CIE id schemes notified eIDAS with *LoA* **High**, see `SPID/CIE-OpenID-Connect-Specifications`_).
    
    **Notification Process**
      Process defining how information is transferred to the European Commission and the inclusion of an entity in the Trusted List.
    
    **Organizational Entity**
      A legal person (only considering organizations and public entities, not natural/physical persons) recognized through a unique identifier to operate a certain role within the IT-Wallet ecosystem.
      In this category the following entity roles are included: Wallet Provider, Credential Issuer, Relying Party, QTSP in general, any kind of Entity that must be registered through a national registration mechanism.
      *Alternative terms:* legal person (only considering organizations and public entities, not natural/physical persons).

    **PID Provider**
      A Credential Issuer responsible for issuing and revoking Person Identification Data (PID) to Users, ensuring that the PID of a User is cryptographically bound to a Wallet Unit. [Revised from ARF v1.9. and Art. 2 Commission Implementing Regulation `EU_2024/2982`_].

    **Policy Language**
      A formal language used to define security, privacy, and identity management policies that govern interactions and transactions within a Trust Framework. This language allows for the clear and unambiguous expression of rules and conditions, facilitating the automation of processes and interoperability among different systems and organizations.
    
    **Primary Actors**
      The set of public entities and private entities that implement the Technical Solutions for the functioning of the IT-Wallet System.

    **Pseudonym**
      Pseudonyms are alternative identifier used to represent an entity (such as a person or organization) without revealing their true identity. It provides a layer of privacy and anonymity while still allowing for consistent authentication and authorization within a system. [Revised from ARF v1.9.].
    
    **Qualified Electronic Attestation of Attributes (QEAA)**
      A digitally verifiable attestation in electronic form, issued by a QTSP, that substantiates a person's possession of attributes. [Revised from ARF v1.9.].

    **Electronic Attestation of Attributes (EAA)**
      A digitally verifiable attestation in electronic form that substantiates a person's possession of Attributes. [Revised from ARF v1.9.].

    **Public Electronic Attestation of Attributes (Pub-EAA)**
      Electronic Attestation of Attributes that contains Attributes deriving from a public Authentic Source.

    **Electronic Attestation of Public Interest**
    **Credential of Public Interest**
      Electronic Attestation of Attributes that contains Attributes intended to certify the release, by the State or other public administrations, of authorizations, certifications, qualifications, identity and recognition documents, receipts of revenue, or to assume a fiduciary value and protection of public faith afterwards their issuance or the entries made on them and, in general, when they are considered security documents pursuant to Article 2, paragraph 10-bis, Law 13 July 1966, no. 559. 
    
    **Person Identification Data (PID)**
      Electronic Attestation that allows the subject to whom the Personal Identification Data refers to be authenticated.

    **Qualified Electronic Attestation of Attributes Provider**
      Organizational Entity which serves as Credential Issuer providing Qualified Electronic Attestations of Attributes (QEAAs).

    **Electronic Attestation of Attributes Provider**
      Organizational Entity which serves as Credential Issuer providing Electronic Attestations of Attributes (EAAs). 
    
    **Registration Authority**
    **Registrar**
      A party responsible for registering all the Organizational Entities by issuing a Trust Attestation.
    
    **Relying Party**
      An Organizational Entity that relies on the IT-Wallet System for the Authentication of Personal Identification Data and User Attributes. [Revised from ARF v1.9.]

    **Relying Party Solution**
      A comprehensive product that may include software, hardware, cloud services, and configurations. It facilitates Credential presentations in various contexts - online, offline, proximity, or remote - through the use of remote web services or specialized applications, such as Credential Verifier mobile apps and or embedded technologies.
    
    **Relying Party Backend**
      Remote infrastructure with server-side components, generally RESTful, including a predefined set of web endpoints, managed by a Relying Party Solution provider.
    
    **Relying Party Instance**
    **Verifier App**
      A Relying Party Instance in the context of a mobile application or a standalone embedded device refers to a specific deployment of the application or device. These instances depend on an User Authentication through a Wallet Instance to confirm User identities before granting access to their functionalities. Each version or environment where the application or device is running, be it a particular release of a mobile app installed on a User's smartphone or a specific embedded device in use, constitutes a separate instance. In case of proximity supervised scenarios, it belongs to and is controlled by a Verifier. [Revised from ARF v1.9.].
      *Differences:* added a sentence on proximity supervised scenarios.

    **Selective Disclosure**
      Functionality enabling the User to submit a subset of Digital Credentials Data.

    **Self-Sovereign Identity (SSI)**
      Is an approach to digital identity that gives individuals control over the information they use to prove who they are to websites, services, and applications across the web.
    
    **Technical Solutions**
      Set of hardware and software systems and services implemented by the Wallet Solution Providers, the PID Provider, Qualified Electronic Attestation of Attributes Provider, Verifiers and Aggregators.
    
    **Technical Specifications**
      The specifications that provide the technical architecture, implementation framework and design requirements for the User Experience adopted by the IT-Wallet System Technical Solutions.
    
    **Trust**
      Trust, within the technical field, is the confidence in the security, reliability, and integrity of entities (such as systems, organizations, or individuals) and their actions, ensuring that they will operate as expected in a secure and predictable manner. It is often established through empirical proof, such as past performance, security certifications, or transparent operational practices, which demonstrate a track record of adherence to security standards and ethical conduct.

    **Trust Attestation**
      Electronic attestation of an entity's compliance with the national regulatory framework, which is cryptographically verifiable and cannot be repudiated over time by the entity that issued it. A Trust Attestation is always related to a particular Trust Framework.
    
    **Trust Evaluation**
      The process of verifying the trustworthiness of registered Organizational Entities, in accordance with pre-established rules. For example, involving the retrieval and validation of entity configurations and trust chains.

    **Trust Framework**
      A legally enforceable set of operational and technical rules and agreements that govern a multi-party system designed for conducting specific types of transactions among a community of participants and bound by a common set of requirements.
    
    **Trust Model**
      Collection of rules that ensure the legitimacy of the components and the entities involved in the IT-Wallet ecosystem.
    
    **Trust Relationship**
      Positive outcome of Trust Evaluation, which produces a reliable relationship between Organizational Entities, where one Organizational Entity trusts the other to securely handle data, execute transactions, or perform actions on its behalf.
    
    **Access Certificate**
      A Certificate for electronic seals or signatures authenticating and validating the (Wallet-) Relying Party, issued by a provider of wallet-relying party Access Certificates. [Revised from Art. 2 Commission Implementing Regulation `EU_2024/2982`_].
    
    **Registration Certificate**
      A data object that indicates the attributes the Relying Party has registered to intend to request from Users.
    
    **Certificate Signing Request (CSR)**
      Request sent to a Certificate Authority (CA) that contains the public key and identifying information of the entity requesting a digital certificate.
    
    **Trusted List**
      Repository of information about authoritative entities in a particular legal or contractual context which provides information about their current and historical status. It serves as the bedrock of trust, acting as federative sources that publish the crucial information about root entities within the ecosystem. [Aligned with ARF v1.9.].
    
    **User**
      A natural or legal person, or a natural person representing another natural person or a legal person, who uses the IT-Wallet System and is the owner of at least one Wallet Instance.

    **Verifier**
      Also known as Credential Verifier. It is a natural person or a legal person using a Relying Party Instance.
    
    **Wallet Instance**
      It is an application installed and configured on a User's device belonging to and which is controlled by a User, as part of the Wallet Unit. The Wallet Instance provides graphical interfaces for User interaction with the Wallet Unit. [Revised from Art. 2 Commission Implementing Regulation `EU_2024/2982`_].

    **Wallet Provider**
      An Organizational Entity, responsible for the management and provisioning of a Wallet Solution. The IT-Wallet Provider MAY be referred to as Public IT-Wallet Provider for the IT-Wallet Solution referred to in Article 64-quater, paragraph 2, of [CAD] or Private IT-Wallet Provider for the IT-Wallet Solutions made available by private entities. [Revised from ARF v1.9. and Art. 2 Commission Implementing Regulation `EU_2024/2982`_].

    **Wallet Provider Backend**
      Is the technical infrastructure and server-side components, including a set of endpoints, managed by a Wallet Provider.
    
    **Wallet Secure Cryptographic Application (WSCA)**
      An application that manages Critical Assets utilizing the cryptographic functions provided by the wallet secure cryptographic device.
      The type of WSCAs depends on the type of WSCD. For example, it might be an eUICC or JavaCard applet for a local UICC or an external JavaCard-based smart card solution, while in a local Android hardware-backed Keystore solution, native trusted applications may function as the WSCA. [Revised from ARF v1.9. and Art. 2 Commission Implementing Regulation `EU_2024/2982`_].

    **Wallet Secure Cryptographic Device (WSCD)**
      It is a tamper-resistant device that provides an environment that is linked to and used by the WSCA to protect Critical Assets and provide cryptographic functions for the secure execution of critical operations. [Aligned with Art. 2 Commission Implementing Regulation `EU_2024/2982`_].
      Example of WSCD type are: remote solutions (e.g., HSMs), local external solutions (e.g., smart cards), local device-integrated solutions (e.g., UICC or native cryptographic hardware, such as the iOS Secure Enclave, Android Hardware Backed Keystore or StrongBox), and hybrid solutions that combine two or more of these types.

    **Wallet Solution**
      Set of Technical Solutions necessary for the proper functioning of IT-Wallet Instances, implemented in accordance with Article 64-quater of the CAD.
      The IT-Wallet Solution MAY be referred to as Public IT-Wallet Solution for the IT-Wallet Solution referred to in Article 64-quater, paragraph 2, of [CAD] or Private IT-Wallet Solutions for the IT-Wallet Solutions made available by private entities.
      [Revised from ARF v1.9. and Art. 2 Commission Implementing Regulation `EU_2024/2982`_].
    
    **Wallet Unit**
      Unique configuration of a Wallet Solution that includes Wallet Instances, WSCAs, and WSCDs provided by a Wallet Provider to an individual Wallet User. For device-based WSCD implementations like TEEs, the Wallet Provider may not supply the WSCD itself.  [Revised from ARF v1.9. and Art. 2 Commission Implementing Regulation `EU_2024/2982`_].
      A Wallet Unit should be understood as a specific setup of the Wallet Solution for an individual User. It should include the application installed on a Wallet User's device or environment that the Wallet User interacts with directly (the Wallet Instance) and the necessary security features to protect the user's data and transactions. These security features should involve special software or hardware to encrypt and safeguard sensitive information.

    **Wallet Unit Attestation**
    **Wallet Attestation**
    **Wallet Instance Attestation**
      It is a data object issued by a Wallet Provider that describes the components of the Wallet Unit. It allows authentication and validation of those components and is cryptographically bound to Wallet Secure Cryptographic Devices. [Aligned with ARF v1.9. and Art. 2 Commission Implementing Regulation `EU_2024/2982`_]. 

    **Digital Credential Catalogue**
      Electronic catalog containing information about the formats and schemes of Digital Credentials, the data contained and the Authentic Sources. The Catalog contains additional information that allows for the establishment of the authenticity and reliability of the information contained therein.

    **Intermediate Entity**
    **Intermediate**
      Intermediate Entity as defined in `OID-FED`_ Section 1.2, for example in IT-Wallet it could be a Relying Party intermediary that offers and manages, on behalf of Relying Party, the Technical Solutions for the remote or proximity verification of Electronic Attestations.

Below are the main defined terms and definitions related to User Experience aspects:

.. list-table::
  :class: longtable
  :widths: 20 80 20
  :header-rows: 1

  * - Name
    - Description
    - Notes
  * - Authentication Button
    - The Engagement Button that enables the User to access the Authentication process and use the services provided by Verifiers.
    - 
  * - Brand Identity
    - Collection of visual, verbal, and strategic elements that a service, a product or an entity uses to present itself to the User and to distinguish itself from others.
    - 
  * - Catalog
    - Section of the Wallet Instance that displays the list of all the available Digital Credentials that can be obtained through the IT-Wallet Instance, and from which it is possible to start the issuing process.
    - 
  * - Call To Action
    - A clear and direct suggestion that encourages users to take a specific action. It can be a button, a link, or another element guiding the user toward a particular goal.
    - 
  * - Detailed View
    - Extended display mode of the Digital Credentials, showing all the Attributes included.
    - 
  * - Discovery Page
    - It's the page of the Touchpoint of the Relying Party where the User lands to access their authenticated area, and it has the goal to show the User all the Authentication methods available.
    - 
  * - Engagement Button
    - Interactive element of the Interface that allows the User to trigger a process (e.g. to Authenticate, to request the issuance of a Digital Credential, etc.).
    - 
  * - Interaction Model
    - A set of characteristics that define how the User interacts with the Interface of one or multiple Touchpoints in order to complete a task or operation and achieve a specific goal.
    - 
  * - Interface
    - The set of graphic, typographical and interactive elements through which the User interacts with the Touchpoint(s) responsible for the delivery of a product or service, in compliance with [GL_DESIGN].
    - 
  * - Preview View
    - Compact visualization mode of the Digital Credential that allows it to be recognized and distinguished in a list of Electronic Attestations thanks to the presence of minimum data or elements.
    - 
  * - Service Model
    - Set of interactions between actors and touchpoints necessary for service delivery and fruition.
    - 
  * - Touchpoint
    - Point of contact (digital and not) between the User and the product or service.
    - 
  * - Trust Mark
    - A graphic element that gives evidence of the participation of the Primary Actors in the IT-Wallet System and thus guarantees adherence to its standards.
    - 
  * - User Experience
    - The set of people's perceptions and reactions resulting from the use and/or expectation of use of a product, system or service.
    - Aligned with ISO 9241-210:2010
  * - Visual Identity
    - Coherent set of graphic and typographic elements that visually represent a product or service and make it distinguishable and recognizable.
    - 

Acronyms
--------

Below are the main acronyms used in the document:

.. list-table::
  :class: longtable
  :widths: 20 80
  :header-rows: 1

  * - **Acronym**
    - **Description**
  * - **AAL**
    - Authenticator Assurance Level as defined in `<https://csrc.nist.gov/glossary/term/authenticator_assurance_level>`_
  * - **ANPR**
    - Italian National Registry of the Resident Population
  * - **API**
    - Application Programming Interface
  * - **CIE**
    - National Electronic Identity Card
  * - **IAM**
    - Identity and Access Management
  * - **LoA**
    - Level of Assurance
  * - **OID4VP**
    - OpenID for Verifiable Presentation
  * - **PDND**
    - National Digital Data Platform. Article 50-ter, paragraph 2 of the CAD, Legislative Decree 7 March 2005 n. 82.
  * - **PID**
    - Person Identification Data
  * - **PII**
    - Personally Identifiable Information
  * - **SPID**
    - Italian Public Digital Identity System
  * - **SSI**
    - Self Sovereign Identity
  * - **VC**
    - Verifiable Credential
  * - **VP**
    - Verifiable Presentation
  * - **WSCA**
    - Wallet Secure Cryptographic Application
  * - **WSCD**
    - Wallet Secure Cryptographic Device

Normative Language and Conventions
==================================

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all capitals, as shown here.

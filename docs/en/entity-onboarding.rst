.. include:: ../common/common_definitions.rst
.. include:: ../common/symbols.rst

Entity Onboarding
=================

This section defines the technical specifications for entity lifecycle management in the IT-Wallet ecosystem based on the **Registry Infrastructure** defined in :ref:`registry:Registry Infrastructure`. This includes initial onboarding procedures, ongoing management operations (data updates, modifications), and federation exit processes. The lifecycle management system establishes and maintains the federated trust infrastructure and registry coordination necessary for secure Digital Credential operations.

For a high-level overview of the onboarding process, see :ref:`onboarding-high-level:Onboarding System`. In particular, the Section :ref:`onboarding-high-level:Onboarding Journey Maps` provides an onboarding journey map from the perspective of Entity's operators.

Overview
--------

Entity Onboarding System Architecture
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The IT-Wallet ecosystem is based on a federated trust infrastructure where participating entities MUST establish cryptographic trust relationships and maintain compliance with common security standards. 

The onboarding framework MUST allow technical registration procedures that are tailored to the participant's role in the IT-Wallet ecosystem:

  1. For Authentic Sources requiring data-focused registration procedures.
  2. For operational Entities (Credential Issuers, Relying Parties, Wallet Providers) requiring trust establishment.


Entity Types and Onboarding Pathways
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following table summarizes entity types, their roles, and corresponding onboarding pathways:

.. list-table:: Entity Types and Onboarding Pathways
   :class: longtable
   :widths: 20 30 25 25
   :header-rows: 1

   * - **Entity Type**
     - **Primary Role**
     - **Onboarding Pathway**
     - **Key Requiring**
   * - Authentic Sources
     - Authoritative data providers for Credential attributes
     - :ref:`entity-onboarding:Authentic Sources Registration Process`
     - Data authority validation, API integration (PDND/Custom).
   * - Credential Issuers
     - Generate and issue Digital Credentials using Authentic Source's data
     - :ref:`entity-onboarding:Federation Entities Onboarding Process`
     - IT-Wallet Trust Infrastructure compliance, :ref:`trust:The Infrastructure of Trust`.
   * - Relying Parties
     - Verify Digital Credentials for service access
     - :ref:`entity-onboarding:Federation Entities Onboarding Process`
     - IT-Wallet Trust Infrastructure compliance, :ref:`trust:The Infrastructure of Trust`.
   * - Wallet Providers
     - Provide Wallet Solutions to citizens
     - :ref:`entity-onboarding:Federation Entities Onboarding Process`
     - IT-Wallet Trust Infrastructure compliance :ref:`trust:The Infrastructure of Trust`, Wallet Attestation capabilities :ref:`wallet-instance-registration:Wallet Instance Initialization and Registration`.
   * - Wallet Instances
     - User-level digital wallet applications
     - Indirect registration via Wallet Provider, see :ref:`wallet-instance-registration:Wallet Instance Initialization and Registration`.
     - Wallet Attestation from certified Wallet Provider.

Administrative vs Technical Registration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The onboarding process follows a structured multi-phase approach:

  1. **Administrative Registration**: All entities MUST complete initial administrative registration that validates their legal standing, regulatory compliance, and organizational eligibility to participate in the IT-Wallet ecosystem.

  2. **Technical Registration**: Following administrative approval, entities make technical registration through specialised pathways:
    
    - **Authentic Source Registration**: Data-focused registration procedures with API integration validation.
    - **Federation Registration**: Cryptographic trust establishment as defined in Section :ref:`trust:The Infrastructure of Trust`.

  3. **IT-Wallet Registry Integration**:

    - **Claims Registry Integration**: Authentic Sources select standardized claim definitions from Claims Registry during capability declaration.
    - **Taxonomy Integration**: All entities use Taxonomy hierarchical classification (domains, purposes) for organizational structure to categorize Credentials.
    - **AS Registry Integration**: Authentic Sources registered with their declared claims and capabilities, enabling Credential Issuers discovery and coordination.
    - **Federation Registry Integration**: Operational entities included for trust validation during Credential operations.
    - **Catalog Integration**: Credential types published in :ref:`registry:Digital Credentials Catalog Structure` based on supervisory body policies for public discovery eligibility.

All registry components and their interactions are detailed in :ref:`registry:Registry Infrastructure`.


Authentic Sources Registration Process
--------------------------------------

Authentic Sources undergo systematic registration to establish their role as authoritative data providers within the IT-Wallet ecosystem. The registration process consists of requirements specification and procedural validation as described in :ref:`onboarding-high-level:Authentic Source Operator Journey`.

AS Registration Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Authentic Sources MUST comply with the following technical requirements to ensure ecosystem interoperability:

  - **Claims Compliance**:

    - **Claims Registry Adoption**: The Entities MUST use standardized Claims Registry identifiers in data responses without custom claim mapping.

  - **API Integration Standards**:

    - **Public Entities**: MUST integrate through PDND platform with e-service implementation following government standards.
    - **Private Entities**: MUST provide a complete OpenAPI 3.0 API Specification document that includes authorization framework, request/response schemas, error handling mechanisms, and sandbox environment for testing.

  - **Response Format Standardization**:

    - **Standard Claims Format**: The Entities MUST use Claims Registry identifiers and formats in all data responses.
    - **State Mapping**: The Entities MUST handle clear mapping between their internal states and standard Credential states (valid, suspended, revoked).

  - **Security and Quality Assurance**:

    - **Security Standards**: The Entities MUST implement TLS 1.3 or higher with robust authentication mechanisms, forward secrecy, and cryptographic algorithms that meet current and emerging security standards, end-to-end confidentiality and integrity of all communications, maintaining compliance with evolving regulatory requirements and industry best practices.
    - **User Authentication Evidence**: The Entities MAY request User authentication evidence from Credential Issuer before granting access to e-services for obtaining User attributes.
    - **Data Quality**: The Entities MUST specify update frequency and provide data freshness guarantees.
    - **Audit Trail**: The Entities MUST implement logging capabilities for all data access and provisioning activities.

AS Registration Information Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

During registration, Authentic Sources MUST provide the following information:

.. list-table:: AS Registration Information Requirements
   :class: longtable
   :header-rows: 1
   :widths: 30 70

   * - Information Category
     - Description and Examples
   * - **Organization Information**
     - **REQUIRED**. Organization Details including:

       - Organization name, type ("public" or "private") and country (ISO 3166-1 alpha-2).
       - Administrative identifier codes such as IPA registration code (REQUIRED only for public Authentic Sources) and legal identifier (Fiscal Code/VAT Number).
       - Contact Information including technical and administrative contact email addresses, homepage URI, privacy policy URI, etc.
   * - **Data Capabilities Declaration**
     - **REQUIRED**. Available claims:

       - Array of claim identifiers from Claims Registry that the Authentic Source provides (e.g., ``["given_name", "family_name", "driving_privileges"]``).
       - Taxonomy classification for Authentic Source scope (e.g., ``[AUTHORIZATION]`` domains and ``["DRIVING_LICENSE"]`` purposes).
      
   * - **API Implementation Details**
     - **REQUIRED**. Integration information details:

       - Authorization framework for API access.
       - API definitions such as Request/Response Formats, including error management.
   * - **Data Provision Capabilities**
     - **REQUIRED**. Indicates if Authentic Source supports immediate/deferred data provision (boolean).    
   * - **User Information**
     - **OPTIONAL**. Markdown-formatted text containing human-readable information about data availability constraints or limitations. For example, if the AS database only contains data registered after a specific date, this information MUST be conveyed to users.

       **Example**: "Driving license data is available for licenses issued after January 1, 2020. For older licenses, contact the local motorization office.".
   * - **Display Properties**
     - **OPTIONAL**. Visual branding suggestions for Credentials using AS data:

       - Background color for Credentials in hexadecimal format (e.g., ``"#003d82"``).
       - Text color for Credentials in hexadecimal format (e.g., ``"#ffffff"``).
       - Logo URI with cryptographic integrity verification for Credential branding.
       - Visual template URI with integrity verification for Credential presentation.

AS Registration Procedure
^^^^^^^^^^^^^^^^^^^^^^^^^

The Authentic Source registration follows a technical process as described below.

.. plantuml:: plantuml/as-registration-process.puml
    :width: 99%
    :alt: Authentic Source registration process showing the 3-step procedure
    :caption: `Authentic Source Registration Process. <https://www.plantuml.com/plantuml/svg/TLD1Rziw3BxxLn0zlG1vhs_hBK26TkqEFMmBbcAdNcY9SRJAaaPARRDVFzfE6iVBWXmCyUF7Z_p8Qyd8kRGURahUKiZEm3eMDWJVg76I6REB0LOS3ObKM78CfQs9goeXAzmb31akfkaNWAB_Kz2w9E9d9v5ty37QNG-IUiAqFfGUuanDLIsNiCwKuDrYeWlD4pQa-YZX_csvh2hD-_U3PY_s4OB83GRtQu2ui8dSzj-FuP_xrGsOQ6aEdXhqu6pNoSOHp_KzP3HPPYFAEpA-exIO4Gmch9rtsP4erwr7ryfR1oCkcSC3liOGsnreleY-cbx2AVV61OARrJsuDdbgDNtGR2cZyrsDrTsNkyklYKA7klhlVv14vYpRkW_i1gM9eyvU4LFDhct9EinqQMb3p6HXu-CBI4afSZuGIgs4fMvT1XvxmFIpaEIZIUyNy41c6rIGX-_edJqQ8_MUwX0Wc8xCH6tSOJ2asWQVvgTpf5T5aW9cOpvYRVLlCrOg6rjqGTFrXPh8ZlGx5KvHICPCjrioJuC5GP7xDf-9nsoT2IEf41b6bipEDSeaAGOX69e2oHWiiZstDqMmeRb2kiGMKtAXcUbU-poUg1JJdUMc-0hqDzH4cHm9fivwz5hc-PZRQwUiCoGlD6RTeFDa_s3yGQOFlxYyXH6H4odz7dMBuBXVMO4S0QrbLQS5WZrknzK2HYSEgr9xPwOBmjGiXf1iE_WdDJ_lr0_WVQBMEtG0TZX8ErviBQlGDwxF-4GTaNLYebg9jIUebUMMgLyjz73VDSAYwtvsZ8ToYyV0X7RNsGWnqH16FxcogWfHjNN5b6lUgr01MgkN1pKf8PqAUhj4hygABil9gD9nL5LrJS6Mrly6>`_ 

**Step 1 - Registration Package Preparation**: The Entity prepares registration information according to the requirements table above. A non-normative example of information in JSON format is provided below. 

.. code-block:: json

   {
     "entity_id": "https://transport-authority.gov.example",
     "organization_info": {
       "organization_name": "National Transport Authority",
       "organization_type": "public",
       "ipa_code": "nta_001",
       "legal_identifier": "12345678901",
       "organization_country": "XX",
       "homepage_uri": "https://www.gov.example/transport",
       "contacts": ["registry@transport-authority.gov.example", "technical-support@transport-authority.gov.example"],
       "policy_uri": "https://www.gov.example/transport/privacy-policy",
       "user_information": "Driving license data is available for licenses issued after January 1, 2020. For older licenses, contact the local transport authority office."
     },
     "data_capabilities": [
       {
         "domains": ["IDENTITY", "AUTHORIZATION"],
         "intended_purposes": ["DRIVING_LICENSE"],
         "available_claims": [
           "given_name", "family_name", "birth_date", "birth_place",
           "issue_date", "expiry_date", "document_number", "driving_privileges"
         ],
         "integration_method": "pdnd",
         "integration_endpoint": "https://api.gov.example/transport/driving-license",
         "api_specification": "https://docs.gov.example/transport/api-oas3.yaml",
         "data_provision": {
           "immediate_flow": true,
           "deferred_flow": false
         },
         "update_frequency": "real_time"
       }
     ],
     "display": {
       "background_color": "#003d82",
       "text_color": "#ffffff",
       "logo_uri": "https://www.gov.example/assets/transport-logo.svg",
       "logo_uri#integrity": "sha-256-a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3"
     }
   }

**Step 2 - Technical Validation**: Supervisory Body validates submitted registration focusing on:

  - **Claims Registry Compliance**: Validation of claims format, identifiers, and existence in Claims Registry.
  - **Taxonomy Validation**: Verification that declared domains, and purposes are valid taxonomy entries.
  - **API Integration Verification**:

    - **Public Entities**: PDND e-service specification compliance verification
    - **Private Entities**: OpenAPI 3.0 specification completeness including authorization framework, request/response schemas, error handling mechanisms, and sandbox environment.

  - **Response Format Standards**: Verification of Claims Registry format usage and state mapping specification.

**Step 3 - AS Registry Publication**: Upon successful validation:

  - Authentic Source Entity is published in AS Registry with complete declared capabilities.
  - Authentic Source becomes discoverable by Credential Issuers for integration requests.
  - Authentic Source is ready for operational data provision.

.. note::
   AS registration is complete and independent of CI integration. AS entities become discoverable immediately upon AS Registry publication, while Credential availability to end-users depends on administrative AS-CI authorization followed by successful technical integration and Supervisory Body policy approval for catalog eligibility.


Authentic Source - Credential Issuer Integration Process
---------------------------------------------------------

Following administrative AS-CI authorization obtained during the administrative registration phase, technical integration procedures establish the operational API connections and data access mechanisms between Credential Issuers and Authentic Sources.

Technical integration encompasses:

- **API Endpoint Configuration**: Establishment of secure API connections as specified in AS technical specifications (PDND e-services for public AS, OpenAPI 3.0 implementations for private AS).
- **Claims Mapping Validation**: Verification that CI implementation correctly maps AS data responses to standardized Claims Registry identifiers.
- **Data Flow Testing**: Validation of immediate/deferred data provision capabilities and error handling mechanisms.
- **Security Implementation**: Configuration of authentication, authorization, and audit logging as required by AS security standards.


Federation Entities Onboarding Process
---------------------------------------

Federation Entities (Credential Issuers, Relying Parties, and Wallet Providers) MUST undergo onboarding procedures to establish trust relationships within the IT-Wallet ecosystem. The federation onboarding process establishes the distributed trust infrastructure through certificate issuance, trust chain validations, and compliance attestation as detailed in :ref:`trust:The Infrastructure of Trust`.

Hierarchical Federation Authority Model
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The IT-Wallet federation implements a **hierarchical onboarding model** where Federation Entities MUST be onboarded by one of the following actors:

  1. **Trust Anchor**: The root authority that has the capability to directly onboard any Federation Entity.
  2. **Intermediates**: Delegated authorities that onboard Leaf Entities on behalf of Trust Anchor.

This hierarchical approach enables **distributed onboarding management** while maintaining a unified trust establishment. Both Trust Anchors and Intermediates act as **Federation Authorities** with the following onboarding capabilities:

  - **Certificate Issuance**: Issue X.509 Certificates to their Immediate Subordinates with appropriate naming constraints as defined in :ref:`trust:X.509 PKI`.
  - **Metadata Policy Application**: Apply federation-specific metadata policies with **cascading effect** (Trust Anchor policies override Intermediate policies).
  - **Trust Mark Issuance**: Issue Federation Trust Marks attesting Subordinate compliance with federation requirements.

Therefore, Federation Entities MAY be onboarded through different paths:

  - **Direct Trust Anchor Onboarding**: Entity directly registers with the Trust Anchor.
  - **Intermediate-mediated Onboarding**: Entity registers with an appropriate Intermediate.




Federation Onboarding Prerequisites
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Federation Entities MUST comply with the following technical requirements before initiating the onboarding process:

  - **Key Generation**: The entities MUST generate at least two key pairs using elliptic curve cryptography as specified in :ref:`algorithms:Cryptographic Algorithms`:

    - **Federation Key Pair**: Used for signing Entity Configurations and attesting Protocol Keys.
    - **Protocol Key Pair(s)**: Used for entity-specific protocol operations, such as Credential issuance, presentation verification, others.

  - **Protocol Key Attestation**: The entities MUST create self-signed X.509 Certificates for their Protocol Keys using the Federation Private Key. These Certificates establish the authority relationship between Federation and Protocol keys.

  - **Entity Configuration Preparation**: The entities MUST publish an Entity Configuration (EC) signed with their Federation Private Key at the ``/.well-known/openid-federation`` endpoint as defined in :ref:`trust:The Infrastructure of Trust`. The EC MUST include:

    - A ``jwks`` claim containing the Federation Entity Public Key in JSON Web Key (JWK) format.
    - An ``iss`` claim with the Federation Entity Identifier as defined in :ref:`trust:Federation Roles`.
    - A ``sub`` claim equal to the ``iss`` claim.
    - ``iat`` and ``exp`` claims defining a valid time interval.
    - A ``metadata`` claim containing entity-specific metadata organized by Metadata Types (see :ref:`credential-issuer-entity-configuration:Credential Issuer Entity Configuration`, :ref:`relying-party-entity-configuration:Relying Party Entity Configuration`, or :ref:`wallet-provider-entity-configuration:Wallet Provider Entity Configuration`) with Protocol Keys included in the metadata ``jwks`` fields and self-signed certificates in the corresponding ``x5c`` claims.

  - **Certificate Signing Request (CSR)**: The entities MUST prepare a CSR in PKCS #10 format containing **only the Federation Entity Public Key** for X.509 Certificate issuance by the Federation Authority as defined in :ref:`trust:Trust Infrastructure Requirements`.

Federation Onboarding Procedure
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The federation onboarding follows a structured 4-step procedure, it can be performed by the Trust Anchor or an Intermediate**.

.. note::
   The following procedure applies to Wallet Providers, Credential Issuers and Relying Parties that wish to perform onboarding in the IT-Wallet federation. The **Federation Authority** is referred to Trust Anchor or Intermediate according to organizational characteristics and federation governance policies.

.. note::
   This section covers only the technical registration requirements. All administrative information (legal entity validation, regulatory compliance, organizational eligibility, etc.) is assumed to have been collected and validated by the Supervisory Body during the administrative registration phase, which is out of scope for this technical specification. Examples of administrative information include: legal entity name, business registration numbers, contact persons, legal compliance documentation, and operational authorizations.

.. plantuml:: plantuml/federation-onboarding-process.puml
    :width: 99%
    :alt: Federation entity onboarding process showing the 4-step procedure
    :caption: `Federation Entity Onboarding Process. <https://www.plantuml.com/plantuml/svg/dLHHRnit37w_Nq7qOKYmfF6wz646l3NmqY4BXXPEr-t1G41BF5khZhf9L5B_-vqi7quvtu1XRmSToUyZFtvy5mIznCR2UzBaKOnZk6KnieSFl77ejU4jVFHEKGWLHd4ScmtvgcgxHADCYopmwYJx5M20clurwYRApla-KB2g5Wju46hXktc9lAA_8mM1XxXfJ0WfTR6egfhWyaSGdESV0cv8yJbbpMV7Hkv-le2FSMEDWdlQmwz_t5_0yc5rFc2-cSCKD_YCrkZyYAnXILvCRHGAmLq84LdHWOvWJ-SpULFlmTFM13dMCrmxtno-oyXSc_fnBntNPXkFETZnlthzJDPUVc7tp5Uk9JRwiXve4klM6PQYvatRsZqq9AXH45fdZJ8KuDd83XG6XOS9KLsJAlDICmH_ldux-m5KqMJ7UyqdsXR3h2gqKeufH9KsfOws0W3843NDNynExT0mU0gjuq23K2Nqju2z3ELxEA_81YeXQpIMz0XkHN-HIhzpxqOJfnAamQHUGqMi1_s_dq-hy7jxK2XflwBWx1Fr2rbiOOBBWPD5vck-X1kjXtuUTuObWB9eclxdrxSgFnor6azhmChJ3pk81qmDjyl_i2s3O_fE2fzS-VpqKuYR1R4aZaP_8pu6UKHM7Us5OFTKMEPwABJAGkOv5TvTkgQrbD179bcHwkAxyahWAGa91wZSQH7t2t6YJwKvFnqYVqF_9MqdPBRbAhEoKLCPPpXT2PT8fM8FWa8DiKmX1RDbqjsD-9I5A8XThFdfw5azU2prZCbsgUCJvsL_z8CQp05dRsOp-71_VhAsERBtHYRHiUbKAgXqxZYbaciDEhydKRlfpfFcTVhzKl4ncydSJ6aORu6QScw_YaSbBtJohfckDSgzOw6jHncfDschVY2FJHTqD5FcV-gKsZ3Q_tjdyxtfXSd71iwkPxEhwzdrU6AttZi_KYyV7107Hvlbs_EEMCV6_WC0>`_



**Step 1 - Onboarding Request Submission**: Federation Entity initiates the onboarding process by submitting a technical registration request including the following information.

.. list-table:: Federation Onboarding Technical Request Information
   :class: longtable
   :header-rows: 1
   :widths: 30 70

   * - **Technical Information Category**
     - **Requirements and Description**
   * - **Federation Entity Identifier**
     - **REQUIRED**. A unique URL that identifies the Federation Entity as defined in :ref:`trust:Federation Roles`.
   * - **Federation Entity Public Key (JWK)**
     - **REQUIRED**. Elliptic public key in JSON Web Key format used for signing Entity Configurations and attesting Protocol Keys, using cryptographic algorithms specified in :ref:`algorithms:Cryptographic Algorithms`.
   * - **Certificate Signing Request (CSR)**
     - **REQUIRED**. CSR in PKCS #10 format for X.509 Certificate issuance by the Federation Authority. The CSR MUST:

       - Contain **only the Federation Entity Public Key** to be certified.
       - Be signed with the corresponding Federation Private Key.
       - Define the certificate Subject with required attributes as specified in :ref:`trust:X.509 Certificates Issuance` for Federation Entities.

.. warning::
   Before submitting the technical onboarding request, Federation Entities MUST ensure that their ``/.well-known/openid-federation`` endpoint publishes a valid Entity Configuration (as defined in :ref:`trust:Entity Configuration`) signed with their Federation Private Key corresponding to the Federation Entity Public Key provided in the request. The Entity Configuration MUST already include Protocol Keys in the metadata with self-signed X.509 certificates in the ``x5c`` claims.


A non-normative example of the technical information structure that Federation Entities submit during Step 1 onboarding request:

.. code-block:: json

  {
    "entity_id": "https://credentials.example.gov",
    "entity_type": "credential_issuer",
    "jwks": {
      "kid": "NsXymfIILEPR5Y0t",
      "kty": "EC",
      "x": "gXY4FApFJCj91Gpb1K9GEIouTq2X3L0K64Iq0ob4l_g",
      "y": "l-6dcrIrFVdrzoY9cRJv9zNuFOR3MsDz6TSDhB0xEo4",
      "crv": "P-256"
    },
    "certificate_signing_request": "-----BEGIN CERTIFICATE REQUEST-----\nMIIBTTCB9QIBADCBkjELMAkGA1UEBhMCSVQxDjAMBgNVBAgMBUxhemlvMQ0wCwYD\nVQQHDARSb21hMRYwFAYDVQQKDA1QYWdvUEEgUy5wLkEuMSQwIgYDVQQDDBtmb28x\nMS5ibG9iLmNvcmUud2luZG93cy5uZXQxJjAkBgkqhkiG9w0BCQEWF3BhZ29wYXNw\nYUBwZWMucGFnb3BhLml0MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEgXY4FApF\nJCj91Gpb1K9GEIouTq2X3L0K64Iq0ob4l_g\n-----END CERTIFICATE REQUEST-----",
    "submission_timestamp": "2025-09-25T14:30:00Z"
  }

The following shows the decoded content of the CSR example above for reference:

.. code-block:: text

   Certificate Request:
       Data:
           Version: 0 (0x0)
           Subject: CN=credentials.example.gov, OU=Digital Credentials, O=Example Organization, L=Roma, ST=Lazio, C=IT, emailAddress=technical@credentials.example.gov
           Subject Public Key Info:
               Public Key Algorithm: id-ecPublicKey
                   Public-Key: (256 bit)
                   ASN1 OID: prime256v1
                   NIST CURVE: P-256
       Signature Algorithm: ecdsa-with-SHA256

.. note::
   The CSR Subject attributes MUST comply with the requirements specified in :ref:`trust:X.509 Certificates Issuance` for Federation Entities.

.. note::
   The Federation Entity Public Key in the ``jwks`` field and the public key contained in the ``certificate_signing_request`` MUST be the same key. The key is provided in two formats: JWK format for OpenID Federation operations and PKCS #10 CSR format for X.509 certificate issuance by the Federation Authority. Protocol Keys are included only in the Entity Configuration metadata, and they MUST NOT be included in the onboarding request.

.. note::
   The Entity Configuration Endpoint is constructed automatically by appending ``/.well-known/openid-federation`` to the Federation Entity Identifier (``entity_id``). Federation Entities do not need to specify this endpoint separately in the registration request.

**Step 2 - Federation Authority Validation and Certificate Issuance**: Following the onboarding request submission, the **Federation Authority** MUST perform:

  - Verification of information provided in the registration request.
  - Validation of the Entity Configuration published at the entity's ``/.well-known/openid-federation`` endpoint and its contained metadata (as defined in :ref:`trust:The Infrastructure of Trust`).
  - **Metadata Policy Application**: Application of federation-specific metadata policies to the entity's metadata based on organizational characteristics and authorization scope as defined in :ref:`trust:Subordinate Statements`. When onboarded through an Intermediate, both Intermediate and Trust Anchor policies apply, with Trust Anchor policies taking precedence in case of conflicts.
  - **Certificate Issuance**: Certification of the Federation Entity Public Key with X.509 certificate issuance using the trust infrastructure detailed in :ref:`trust:Trust Infrastructure Requirements`. Intermediates issue certificates with appropriate **naming constraints** to scope certificate usage to their subordinates only.

Upon successful validation, the entity receives a response containing a certificate chain where:

  - The first element is the X.509 certificate that certifies the Federation Entity Public Key (issued by the Federation Authority).
  - **For Trust Anchor onboarding**: The second element is the Trust Anchor's self-signed X.509 certificate for validating the first certificate.
  - **For Intermediate onboarding**: Additional elements include the Intermediate's certificate and the Trust Anchor's self-signed certificate, forming a complete certificate chain.
  - All certificates are expressed in DER format encoded in Base64.

Example certificate chain response:

.. code-block:: json

   [
     "MIIDqjCCA1GgAwIBAgIGAZc6/V9qMAoGCCqGSM49BAMCMIGzMQsw...",
     "MIIDQzCCAuigAwIBAgIGAZc6+XlDMAoGCCqGSM49BAMCMIGzMQsw..."
   ]

.. note::
   If validation fails, the entity receives a response with identified issues that must be resolved before submitting a new onboarding request.

**Step 3 - Entity Configuration Update and Resolve Request**: After receiving the certificate chain from the Federation Authority, the entity MUST:

  1. **Update Entity Configuration**:

    - Add an ``authority_hints`` claim with a JSON Array containing the **immediate Federation Authority's** Federation Entity Identifier (Trust Anchor for direct onboarding, or Intermediate for mediated onboarding) as defined in :ref:`trust:Federation Roles`.
    - Update the Federation Entity Public Key in the ``jwks`` claim by adding an ``x5c`` claim with the complete certificate chain received from the Federation Authority.
    - Update the Protocol Keys in the metadata ``jwks`` claims by extending their existing ``x5c`` claims to include the Federation certificate chain, creating complete trust chains from Protocol Keys to the Root Authority.

    Example authority_hints addition:

    .. code-block:: json

        {
          "iat": 1718207217,
          "exp": 1749743216,
          "iss": "https://credentials.example.gov",
          "sub": "https://credentials.example.gov",
          "authority_hints": ["https://trust-anchor.example.gov"],
          //...
        }

    Example Federation JWK with certificate chain:

    .. code-block:: json

        {
          "kid": "NsXymfIILEPR5Y0t",
          "kty": "EC",
          "x": "gXY4FApFJCj91Gpb1K9GEIouTq2X3L0K64Iq0ob4l_g",
          "y": "l-6dcrIrFVdrzoY9cRJv9zNuFOR3MsDz6TSDhB0xEo4",
          "crv": "P-256",
          "x5c": [
            "MIIDqjCCA1GgAwIBAgIGAZc6/V9qMAoGCCqGSM49BAMCMIGzMQsw...",
            "MIIDQzCCAuigAwIBAgIGAZc6+XlDMAoGCCqGSM49BAMCMIGzMQsw..."
          ]
        }

    Example Protocol JWK with extended certificate chain:

    .. code-block:: json

        {
          "kid": "ProtocolKeyId123",
          "kty": "EC",
          "x": "protocol_key_x_coordinate...",
          "y": "protocol_key_y_coordinate...",
          "crv": "P-256",
          "x5c": [
            "MIIDprotocolCert...",  // Protocol cert (signed by Federation key)
            "MIIDqjCCA1GgAwIBAgIGAZc6/V9qMAoGCCqGSM49BAMCMIGzMQsw...",  // Federation cert
            "MIIDQzCCAuigAwIBAgIGAZc6+XlDMAoGCCqGSM49BAMCMIGzMQsw..."   // Root cert
          ]
        }

  2. **Publish Updated Entity Configuration**: Publish the updated EC at the ``/.well-known/openid-federation`` endpoint as specified in :ref:`trust:The Infrastructure of Trust`.

  3. **Submit Resolve Request**: Call the **Trust Anchor**'s ``/resolve`` endpoint (as defined in :ref:`trust:Trust Infrastructure Requirements`) with URL-encoded parameters:

    - ``sub``: Federation Entity Identifier.
    - ``trust_anchor``: **Trust Anchor** Federation Entity Identifier (always the root Trust Anchor, even for Intermediate-mediated onboarding).

    Example resolve request:

    .. code-block:: http

        GET /resolve?sub=https%3A%2F%2Fcredentials.example.gov&trust_anchor=https%3A%2F%2Ftrust-anchor.example.gov HTTP/1.1
        Host: trust-anchor.example.gov

**Step 4: Resolve Response and Onboarding Completion**

Following the resolve request, the **Federation Authority** performs:

  - **Trust Chain Reconstruction**: Reconstruction of a valid trust chain for the entity as defined in :ref:`trust:The Infrastructure of Trust`.
  - **Federation Trust Mark Generation**: Generation of an IT-Wallet Federation Trust Mark as a signed JWT attestation of the entity's federation membership and compliance with IT-Wallet technical requirements.
  - **Trust Mark Integration in Subordinate Statement**: The generated Trust Mark is included in the entity's Subordinate Statement as defined in :ref:`trust:Subordinate Statements`.
  - **Metadata Policy Application**: Application of cascading metadata policies during trust chain construction, ensuring Trust Anchor policies take precedence over Intermediate policies.
  - Generation of a signed JSON Web Token (JWT) using algorithms specified in :ref:`algorithms:Cryptographic Algorithms` containing the reconstructed trust chain and validated entity metadata.
  - Transmission of an HTTP response containing the created JWT (Resolve Response).

If the response status code is 200 OK, the Federation Entity MUST complete the onboarding process by:

  - **Validate Resolve Response**: Validate the JWT contained in the Resolve Response and extract the trust chain and validated metadata from the JWT payload.
  - **Fetch Subordinate Statement**: Retrieve its own Subordinate Statement from the immediate Federation Authority using the ``/fetch`` endpoint as defined in :ref:`trust:Federation API endpoints`.
  - **Extract Trust Mark**: Extract the Federation Trust Mark from the Subordinate Statement ``trust_marks`` claim.
  - **Trust Mark Integration**: Include the extracted Trust Mark in its Entity Configuration using the ``trust_marks`` claim as specified in :ref:`trust:Entity Configuration Leaves and Intermediates`.
  - **Final Entity Configuration Update**: Publish the updated Entity Configuration with the integrated Trust Mark at the ``/.well-known/openid-federation`` endpoint.

Upon successful completion of Step 4, the **entity onboarding is successfully completed**. The entity is now operational within the IT-Wallet federation and ready for operational activities.

.. note::
   If the ``/resolve`` endpoint responds with status code 400 or 404, the entity must resolve the issues described in the response message before calling the resolve endpoint again. 

.. note::
   **Federation Registry Integration**: Upon successful onboarding completion, the entity's Federation Entity Identifier becomes discoverable through the Trust Anchor's entity listing mechanisms (as defined in :ref:`trust:The Infrastructure of Trust`), indicating active federation participation. The entity becomes part of the federation infrastructure detailed in :ref:`registry:Registry Infrastructure`.

IT-Wallet Federation Trust Mark
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Federation Entities receive IT-Wallet Federation Trust Marks during successful onboarding completion. **Trust Marks are issued by the Federation Authority** (Trust Anchor for direct onboarding, Intermediate for mediated onboarding) and serve as verifiable attestations of federation membership, compliance with IT-Wallet technical requirements, and authorization policies for specific operational scopes.

Trust Mark Types and Schema
"""""""""""""""""""""""""""

Entities MAY receive multiple Trust Marks for different purposes and entity types, enabling granular authorization policy enforcement. Trust Mark identifiers MUST follow a hierarchical schema that reflects the authorization scope:

``https://<federation_authority_domain>/trust_marks/<purpose>/<entity_type>``

Where:

  - ``<federation_authority_domain>``: The domain of the issuing Federation Authority.
  - ``<purpose>``: The Trust Mark purpose. The ``federation-entity`` purpose is **REQUIRED** for all entities. Additional Trust Mark purposes MAY be supported, such as ``authorization_policy`` for granular operational scope definitions.
  - ``<entity_type>``: The recipient entity type (e.g., ``credential-issuer``, ``relying-party``, ``wallet-provider``).

Trust Mark Structure
""""""""""""""""""""

Trust Marks in Entity Configuration MUST be represented as JSON objects containing the following claims:

.. list-table:: Trust Mark Object Claims (in Entity Configuration)
   :class: longtable
   :header-rows: 1
   :widths: 20 80

   * - **Claim**
     - **Description**
   * - **trust_mark_type**
     - **REQUIRED**. Identifier for the type of Trust Mark following the schema: ``https://<federation_authority_domain>/trust_marks/<purpose>/<entity_type>``.
   * - **trust_mark**
     - **REQUIRED**. A signed JSON Web Token representing the Trust Mark issued by the Federation Authority.


The Trust Mark JWT (contained in the ``trust_mark`` claim above) includes the following claims:

.. list-table:: Trust Mark JWT Claims
   :class: longtable
   :header-rows: 1
   :widths: 20 80

   * - **Claim**
     - **Description**
   * - **iss**
     - **REQUIRED**. Federation Authority issuing the Trust Mark (immediate superior: Trust Anchor or Intermediate).
   * - **sub**
     - **REQUIRED**. Federation Entity Identifier of the recipient.
   * - **id**
     - **REQUIRED**. Unique Trust Mark identifier, MUST match the ``trust_mark_type`` claim.
   * - **iat**
     - **REQUIRED**. Trust Mark issuance timestamp.
   * - **exp**
     - **REQUIRED**. Trust Mark expiration timestamp.
   * - **organization_type**
     - **REQUIRED**. Entity organization type (``public`` or ``private``).
   * - **id_code**
     - **RECOMMENDED**. JSON object with identification codes (e.g., IPA code for public entities, VAT number).
   * - **organization_name**
     - **RECOMMENDED**. Full name of the Organizational Entity.
   * - **email**
     - **RECOMMENDED**. Institutional or PEC email of the organization.
   * - **logo_uri**
     - **OPTIONAL**. URL pointing to the Trust Mark logo for UI/UX purposes.
   * - **ref**
     - **OPTIONAL**. URL with additional web information about the Trust Mark.


The following non-normative examples illustrate different Trust Mark JWT contents for federation membership and different authorization policies:

.. code-block:: json

   {
     "iss": "https://trust-anchor.eid-wallet.example.it",
     "sub": "https://ci.public-authority.gov.example",
     "id": "https://trust-anchor.eid-wallet.example.it/trust_marks/federation-entity/credential-issuer",
     "iat": 1718207217,
     "exp": 1749743216,
     "organization_type": "public",
     "id_code": {
       "ipa_code": "pub_001",
       "legal_identifier": "12345678901"
     },
     "organization_name": "Public Authority Services",
     "email": "registry@public-authority.gov.example"
   }

.. code-block:: json

   {
     "iss": "https://trust-anchor.eid-wallet.example.it",
     "sub": "https://rental.cars.example.com",
     "id": "https://trust-anchor.eid-wallet.example.it/trust_marks/authorization_policy/relying-party",
     "iat": 1718207217,
     "exp": 1749743216,
     "organization_type": "private",
     "id_code": {
       "vat_number": "IT12345678901",
       "legal_identifier": "12345678901"
     },
     "organization_name": "Premium Car Rental Services Ltd",
     "email": "compliance@rental.cars.example.com",
     "authorized_claims": ["given_name", "family_name", "driving_privileges"],
     "authorized_credential_types": ["mobile-driving-license"],
     "scope_restrictions": {
       "domains": ["AUTHORIZATION"],
       "purposes": ["DRIVING_LICENSE"]
     }
   }

.. code-block:: json

   {
     "iss": "https://trust-anchor.eid-wallet.example.it",
     "sub": "https://private-badge.ci.example.com",
     "id": "https://trust-anchor.eid-wallet.example.it/trust_marks/authorization_policy/credential-issuer",
     "iat": 1718207217,
     "exp": 1749743216,
     "organization_type": "private",
     "id_code": {
       "vat_number": "IT98765432101",
       "legal_identifier": "98765432101"
     },
     "organization_name": "Badge Services Ltd",
     "email": "compliance@rprivate-badge.ci.example.com",
     "authorized_claims": ["given_name", "family_name", "company_id"],
     "authorized_credential_types": ["example-company-badge"],
     "scope_restrictions": {
       "domains": ["MEMBERSHIP"],
       "purposes": ["ASSOCIATION"]
     }
   }



Federation Entities MUST integrate Trust Marks in their Entity Configuration using the ``trust_marks`` claim as specified in :ref:`trust:Entity Configuration Leaves and Intermediates`. Entities MAY receive multiple Trust Marks for different authorization scopes.


.. code-block:: json

   {
     "iss": "https://credentials.example.gov",
     "sub": "https://credentials.example.gov",
     "jwks": { },
     "authority_hints": ["https://trust-anchor.eid-wallet.example.it"],
     "trust_marks": [
       {
         "trust_mark_type": "https://trust-anchor.eid-wallet.example.it/trust_marks/federation-entity/credential-issuer",
         "trust_mark": "eyJhbGciOiJFUzI1NiIsImtpZCI6IlRydXN0QW5jaG9yS2V5SWQiLCJ0eXAiOiJKV1QifQ..."
       }
     ],
     "metadata": { }
   }


.. code-block:: json

   {
     "iss": "https://healthcare-ci.example.gov",
     "sub": "https://healthcare-ci.example.gov",
     "jwks": { },
     "authority_hints": ["https://healthcare.intermediate.eid-wallet.example.it"],
     "trust_marks": [
       {
         "trust_mark_type": "https://healthcare.intermediate.eid-wallet.example.it/trust_marks/federation-entity/credential-issuer",
         "trust_mark": "eyJhbGciOiJFUzI1NiIsImtpZCI6IkhlYWx0aGNhcmVJbnRlcm1lZGlhdGVLZXlJZCIsInR5cCI6IkpXVCJ9..."
       }
     ],
     "metadata": { }
   }


Trust Mark Validation
"""""""""""""""""""""

Federation participants validate Trust Mark status through two mechanisms:

1. **Static Validation**: Cryptographic verification using the issuing Federation Authority's public key from the trust chain.
2. **Dynamic Validation**: Real-time status verification via the issuing Federation Authority's ``/trust_mark_status`` endpoint as defined in :ref:`trust:Federation API endpoints`.


Certificate Management Operations
----------------------------------

This section defines the operational procedures for X.509 certificate management within the IT-Wallet federation, covering certificate chain analysis, validation procedures, and revocation verification. These procedures complement the federation onboarding processes and support ongoing certificate lifecycle management for all federation participants.

Federation PKI Architecture
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The IT-Wallet federation operates a hierarchical Public Key Infrastructure where:

	- **Trust Anchor**: Acts as Root Certificate Authority where root certificates MUST NOT exceed **5-year validity period**.
	- **Federation Entity Certificate**: Each federation participant receives a certificate that operates as a limited sub-CA where certificates MUST NOT exceed **2-year validity period**.
	- **Protocol Certificates**: Self-issued certificates for internal services where certificates SHOULD NOT exceed **1-year validity period**.

Each federation entity MUST expose its Federation Entity certificate on a publicly accessible endpoint. The Federation Entity private key serves dual purposes:

	1. Self-issuing Protocol certificates for internal cryptographic operations (limited sub-CA capability).
	2. Acting as the Federation Entity Key for signing Entity Statements.

.. note:: 
  Federation entities (Leafs) can ONLY issue certificates for themselves (Protocol certificates), NOT for other federation entities. Only Federation Authorities (Trust Anchor and Intermediates) can issue certificates for other entities.

For Protocol certificates with validity periods exceeding 24 hours, the issuing entity MUST publish and regularly update a Certificate Revocation List (CRL) on a publicly accessible endpoint.

Certificate Chain Structure and Analysis
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Federation entities receive certificate chains during the onboarding process. Understanding and validating these chains is essential for proper federation operations and trust verification.

Certificate Chain Visualization
""""""""""""""""""""""""""""""""

Federation entities SHOULD analyze received certificate chains using standard cryptographic tools to verify proper structure and validate trust relationships.

The following script enables federation entities to:

	- Extract certificate details for verification.
	- Analyze certificate extensions and constraints.
	- Verify certificate hierarchy and relationships

.. code-block:: bash

   #!/bin/bash
   # Certificate chain analysis for federation entities
   # Array containing certificates in DER format encoded in Base64
   certificate_chain=(
       "MIIDyzCCA3GgAwIBAgI..." # Federation Entity Certificate
       "MIIDQzCCAuigAwIBAgI..." # Trust Anchor Certificate
   )

   # Display first certificate (Federation Entity)
   echo "===================================="
   echo " Federation Entity Certificate Analysis"
   echo "===================================="
   echo
   echo "${certificate_chain[0]}" | base64 -d > federation_entity.der
   openssl x509 -in federation_entity.der -inform DER -text -noout

   # Display second certificate (Trust Anchor)
   echo "====================================="
   echo " Trust Anchor Certificate Analysis"
   echo "====================================="
   echo
   echo "${certificate_chain[1]}" | base64 -d > trust_anchor.der
   openssl x509 -in trust_anchor.der -inform DER -text -noout

   # Cleanup temporary files
   rm federation_entity.der trust_anchor.der


Certificate Chain Validation
"""""""""""""""""""""""""""""

Federation entities MUST validate certificate chains to ensure proper trust establishment and verify compliance with federation PKI requirements.

A non-normative exampe of certificate chain validation procedure is given below:

.. code-block:: bash

   #!/bin/bash
   # Certificate chain validation for federation entities

   # Convert DER certificates to PEM format for validation
   openssl x509 -inform der -in federation_entity.der -out federation_entity.pem
   openssl x509 -inform der -in trust_anchor.der -out trust_anchor.pem

   # Validate Trust Anchor certificate (self-signed)
   echo "Validating Trust Anchor certificate..."
   openssl verify -CAfile trust_anchor.pem trust_anchor.pem

   # Validate Federation Entity certificate against Trust Anchor
   echo "Validating Federation Entity certificate..."
   openssl verify -CAfile trust_anchor.pem federation_entity.pem

   # Cleanup
   rm federation_entity.pem trust_anchor.pem

Federation entities SHOULD verify:

	1. **Certificate Signatures**: Each certificate MUST be properly signed by its issuer.
	2. **Certificate Chain Integrity**: Issuer-Subject relationships MUST be valid throughout the chain.
	3. **Certificate Validity Periods**: All certificates MUST be within their validity periods and MUST comply with federation limits.
	4. **Certificate Extensions**: Basic Constraints and Key Usage MUST comply with federation requirements:

		- Federation Entity certificates: ``CA:TRUE, pathlen:0`` (can only self-issue certificates).
		- Protocol certificates: ``CA:FALSE`` (cannot issue certificates).

Certificate Revocation Management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Federation entities MUST implement certificate revocation verification to ensure ongoing trust validation and compliance with federation security requirements.

CRL Distribution and Access
""""""""""""""""""""""""""""

Federation authorities publish Certificate Revocation Lists (CRL) at publicly accessible endpoints. Federation entities MUST be able to access and process these CRL distributions for revocation verification.

The following procedure enables federation entities to:

	- Locate CRL distribution endpoints from certificates.
	- Download current revocation lists.
	- Analyze CRL content and validity periods.

.. code-block:: bash

   #!/bin/bash
   # CRL extraction and analysis for federation entities

   # Extract CRL URL from certificate CRL Distribution Points extension
   crl_url=$(openssl x509 -in certificate.der -inform DER -text -noout | \
             grep "URI:" | sed 's/.*URI://')

   echo "CRL Distribution Point: $crl_url"

   # Download CRL from distribution point
   curl -s -O "$crl_url"
   crl_file=$(basename "$crl_url")

   # Display CRL information
   echo "CRL Content Analysis:"
   openssl crl -in "$crl_file" -inform DER -text -noout


Certificate Revocation Verification
""""""""""""""""""""""""""""""""""""

Federation entities MUST verify certificate revocation status by checking certificate serial numbers against current Certificate Revocation Lists.

Federation entities SHOULD implement automated revocation checking for:

	- **Federation Entity Certificates**: Verify own certificate status periodically.
	- **Peer Entity Certificates**: Validate certificates of other federation participants.
	- **Trust Chain Validation**: Ensure entire certificate chains remain valid.

Below a bash script for certificate revocation status verification is given as a non-normative example:

.. code-block:: bash

   #!/bin/bash
   # Certificate revocation verification for federation entities

   # Extract certificate serial number
   certificate_serial=$(openssl x509 -in certificate.der -inform DER -noout -serial | \
                       cut -d= -f2)

   # Normalize serial number (remove leading zeros, convert to lowercase)
   normalized_serial=$(echo "$certificate_serial" | sed 's/^0*//' | tr '[:upper:]' '[:lower:]')

   echo "Certificate Serial Number: $normalized_serial"

   # Extract CRL URL and download
   crl_url=$(openssl x509 -in certificate.der -inform DER -text -noout | \
             grep "URI:" | sed 's/.*URI://')
   curl -s -O "$crl_url"
   crl_file=$(basename "$crl_url")

   # Validate CRL signature against Trust Anchor
   echo "Validating CRL signature..."
   openssl crl -in "$crl_file" -inform DER -noout -text -CAfile trust_anchor.pem

   # Extract revoked serial numbers from CRL
   revoked_serials=$(openssl crl -in "$crl_file" -inform DER -text -noout | \
                    grep 'Serial Number' | \
                    sed 's/.*Serial Number: //' | \
                    sed 's/^0*//' | \
                    tr '[:upper:]' '[:lower:]')

   # Check if certificate is revoked
   if echo "$revoked_serials" | grep -q "$normalized_serial"; then
       echo "Certificate Status: REVOKED"
       exit 1
   else
       echo "Certificate Status: VALID"
       exit 0
   fi



Certificate Management Best Practices
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Certificate Validation Integration
"""""""""""""""""""""""""""""""""""

Federation entities SHOULD integrate certificate validation procedures into their standard federation operations:

	1. **Entity Configuration Updates**: Verify certificate chains when processing authority hints and certificate updates.
	2. **Trust Chain Construction**: Validate all certificates during trust chain building procedures.
	3. **Federation API Operations**: Perform certificate revocation checks during ``/resolve`` and ``/fetch`` operations.
	4. **Protocol Certificate Management**: Validate self-issued Protocol certificates for internal services.
	5. **Periodic Validation**: Implement regular certificate and CRL validation schedules.

Diagnostic and Troubleshooting
"""""""""""""""""""""""""""""""

Federation entities MAY implement diagnostic procedures to identify and resolve certificate-related issues:

  - **Certificate Validation**, including:

    - **Authority Key Identifier Mismatches**: CRL Authority Key Identifier does not match Trust Anchor Subject Key Identifier.
    - **Trust Anchor Certificate Rotation**: Outdated Trust Anchor certificates causing validation failures.
    - **Serial Number Format Issues**: Serial number normalization problems in revocation checking.

  - **CRL Validation Failure**: When CRL validation fails, federation entities SHOULD:

    1. **Verify Trust Anchor Certificate**: Ensure current Trust Anchor certificate is being used.
    2. **Check Authority Key Identifier**: Compare CRL Authority Key Identifier with Trust Anchor Subject Key Identifier.
    3. **Validate CRL Signature**: Verify CRL is properly signed by expected issuing authority.
    4. **Update Trust Anchor Certificate**: Download updated Trust Anchor certificate if rotation has occurred.

  - **Endpoint Accessibility Verification**: Federation entities SHOULD implement connectivity testing for certificate infrastructure endpoints.


The following non-normative example provides a script for Federation certificate infrastructure connectivity test:

.. code-block:: bash

   #!/bin/bash
   # Federation certificate infrastructure connectivity test

   # Test Trust Anchor certificate endpoint
   ta_cert_url="https://trust-anchor.eid-wallet.example.it/pki/ta.cer"
   if curl -f -s "$ta_cert_url" > /dev/null; then
       echo "Trust Anchor certificate endpoint: ACCESSIBLE"
   else
       echo "Trust Anchor certificate endpoint: FAILED"
   fi

   # Test CRL distribution endpoints
   ta_crl_url="https://trust-anchor.eid-wallet.example.it/pki/ta.crl"
   if curl -f -s "$ta_crl_url" > /dev/null; then
       echo "Trust Anchor CRL endpoint: ACCESSIBLE"
   else
       echo "Trust Anchor CRL endpoint: FAILED"
   fi

Certificate Lifecycle Coordination
"""""""""""""""""""""""""""""""""""

Federation entities MUST coordinate certificate management with federation lifecycle procedures following the established validity periods:

- **Certificate Renewal**: Align certificate renewals with Entity Configuration updates and Trust Mark refresh cycles, according to the federation limits defined in :ref:`entity-onboarding:Federation PKI Architecture`.
- **Key Rotation**: Coordinate Federation Entity Key rotation with certificate renewal procedures.
- **CRL Management**: For Protocol certificates with validity > 24 hours, maintain current CRL publication.
- **Federation Exit**: Ensure proper certificate revocation during voluntary or supervisory body-initiated federation exit.


Entity Lifecycle Management
----------------------------

This section provides technical implementation procedures for entity lifecycle management. For high-level lifecycle concepts and business processes, see :ref:`onboarding-high-level:Entity Lifecycle Management`.

While administrative data update MUST follow governance processes that are out of scope of this technical specification, technical configuration updates are described in the following sections.

Technical Configuration Updates
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Technical updates affecting federation protocol operations MUST follow specific procedures for:

  - **Certificate Renewal**

    1. **Pre-renewal Preparation**: The Entity MUST generate a new CSR with updated certificate information.
    2. **Renewal Request**: The Entity MUST submit renewal request with new CSR following the same technical procedure as initial onboarding.
    3. **Certificate Integration**: The Entity MUST update its Entity Configuration with new certificate chain in ``x5c`` parameter.
    4. **Trust Chain Validation**: The Entity MUST verify updated Trust Chain through ``/resolve`` endpoint.
    5. **Registry Update**: The Entity SHOULD confirm updated entity information in Trust Anchor ``/list`` endpoint.

  - **Key Rotation**

    1. **New Key Generation**: The Entity MUST generate a new Federation Entity Public Key pair.
    2. **Parallel Key Publication**: The Entity MUST publish both old and new keys in Entity Configuration ``jwks`` claim during transition period.
    3. **Certificate Request**: The Entity MUST request new certificate for new public key following standard procedure.
    4. **Gradual Migration**: The Entity MUST update Entity Configuration to use new key for signing while maintaining old key for verification.
    5. **Old Key Deprecation**: The Entity MUST remove old key from Entity Configuration after validation period.

  - **Metadata Updates**

    - **Endpoint Changes**: The Entity MAY update service endpoints in entity-specific metadata.
    - **Capability Updates**: The Entity MAY modify supported protocols, algorithms, or service capabilities within the constraints defined by this IT-Wallet implementation profile.



All technical updates MUST be validated through:

  1. **Entity Configuration Validation**: The Entity MUST verify updated EC structure and content.
  2. **Trust Chain Resolution**: The Entity MUST confirm ``/resolve`` endpoint returns valid Trust Chain.
  3. **Federation Status**: The Entity MUST verify entity operational status in federation registry.
  4. **Integration Testing**: The Entity SHOULD test federation protocol operations with updated configuration.

Technical Federation Exit Procedures
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For business context on federation exit processes, see :ref:`onboarding-high-level:Federation Exit and Removal Processes`. This section covers technical implementazione procedurs.

Voluntary Exit - Technical Deactivation
""""""""""""""""""""""""""""""""""""""""""

  1. **Certificate Revocation Request**: The Entity MUST submit a certificate revocation request to Federation Authority with revocation reason. The request MUST be signed with the Federation Entity Private Key corresponding to the certificate being revoked to prove the legitimacy of the revocation request.
  2. **CRL Update Verification**: The Federation Authority MUST revoke the Entity's certificates and the Entity MUST verify they appear in updated Certificate Revocation List.
  3. **Subordinate Statement Removal**: The Federation Authority MUST completely remove the Entity's Subordinate Statement from the Federation Registry to prevent any trust relationship validation.
  4. **Entity Configuration Deactivation**: The Entity MUST deactivate its Entity Configuration. The Entity MAY either:

     a. Remove the Entity Configuration completely from the ``/.well-known/openid-federation`` endpoint (returning HTTP 404), OR
     b. Keep the Entity Configuration available but MUST ensure it remains expired (with ``exp`` claim in the past) and MUST NOT update it with fresh timestamps.

  5. **Registry Status Update**: The Entity SHOULD verify removal from Federation Registry, also verifying the Trust Mark status returns ``{"active": false}`` from ``/trust_mark_status`` endpoint. 

Non-normative example of certificate revocation request following RFC 3280 format:

.. code-block:: text

   Certificate Revocation Request:
   Subject: CN=credentials.example.gov, OU=Digital Credentials, O=Example Organization, L=Roma, ST=Lazio, C=IT, emailAddress=technical@credentials.example.gov
   Certificate Serial Number: 987654321
   Revocation Reason: cessation_of_operation (5)
   Revocation Date: 2025-12-31T23:59:59Z

   Request signed with Federation Entity Private Key corresponding to:
   Public Key Algorithm: id-ecPublicKey
   ASN1 OID: prime256v1
   NIST CURVE: P-256
   Key ID: NsXymfIILEPR5Y0t

   Note: The CRR MUST be signed with the same private key that corresponds to the
   certificate being revoked to authenticate the revocation request.

Example CRR in DER format (Base64 encoded):

.. code-block:: text

   -----BEGIN CERTIFICATE REVOCATION REQUEST-----
   MIIBVjCB/wIBADBpMQswCQYDVQQGEwJJVDEOMAwGA1UECAwFTGF6aW8xDTALBgNV
   BAcMBFJvbWExGjAYBgNVBAoMEUV4YW1wbGUgT3JnYW5pemF0aW9uMR8wHQYDVQQD
   DBZjcmVkZW50aWFscy5leGFtcGxlLmdvdjBZMBMGByqGSM49AgEGCCqGSM49AwEH
   A0IABIBgZ4HBgUCNXwY5LJSlKzm7gXY4FApFJCj91Gpb1K9GEIouTq2X3L0K64Iq
   0ob4l_gslT14644zbYXYF-xmw7aPdlbMuw3T1URwI4nafMtKrYwDQYJKoZIhvcNAQ
   kEAwIJrRLl1VR987654321gBgJKwYBBQUHAgEWHGh0dHBzOi8vZXhhbXBsZS5vcmcv
   cG9saWN5MAoGCCqGSM49BAMCA0gAMEUCIQC9h3Y6hFgd7zUzZyBrQ3jJ8HmVF2Qa
   -----END CERTIFICATE REVOCATION REQUEST-----

Supervisory Body Removal - Technical Implementation
""""""""""""""""""""""""""""""""""""""""""""""""""""""

  1. **Emergency Certificate Revocation**: The Federation Authority MUST immediately revoke certificates with appropriate reason code (e.g., "Key Compromise", "Cessation of Operation").
  2. **CRL Emergency Update**: The Trust Anchor MUST publish updated CRL within emergency timeframe.
  3. **Subordinate Statement Removal**: The Federation Authority MUST immediately and completely remove the Entity's Subordinate Statement from all federation endpoints.
  4. **Entity Configuration Invalidation**: The Entity's Configuration at ``/.well-known/openid-federation`` becomes invalid due to X.509 Certificate revocation (signature verification fails).
  5. **Trust Chain Invalidation**: Trust Chain resolution MUST return error status for affected entity.
  6. **Service Endpoint Isolation**: Federation infrastructure MUST block access to federation service endpoints.

Example emergency revocation verification:

.. code-block:: bash

   # Check emergency CRL update
   curl -o emergency.crl https://trust-anchor.eid-wallet.example.it/pki/ta-sub.crl
   openssl crl -in emergency.crl -text -noout | grep "Last Update"
   
   # Verify Trust Chain resolution fails
   curl "https://trust-anchor.eid-wallet.example.it/resolve?sub=https%3A//suspended-entity.example.it&trust_anchor=https%3A//trust-registry.eid-wallet.example.it"
   # Expected: HTTP 404 or specific error response

**Component-Level Technical Modifications**

Specific technical components MAY be modified while maintaining federation membership:

.. code-block:: json

   {
     "iss": "https://ci.example.it",
     "sub": "https://ci.example.it",
     "jwks": { 
       // jwks content
     },
     "metadata": {
       "openid_credential_issuer": {
         "credential_endpoint": "https://ci.example.it/credential",
         "credentials_supported": [ ]
         // removed: "batch_credential_endpoint" for maintenance
       }
     }
   }

The Entity MUST follow these steps for component modifications:

1. **Entity Configuration Update**: The Entity MUST modify metadata to reflect component changes.
2. **Trust Chain Revalidation**: The Entity MUST verify updated configuration through ``/resolve`` endpoint.
3. **Service Testing**: The Entity SHOULD test remaining federation protocol operations.
4. **Registry Verification**: The Entity SHOULD confirm updated capabilities in federation registry.

**Post-Exit Technical Obligations**

Entities that exit the federation MUST maintain the following for regulatory compliance:

1. **Historical Entity Configuration**: The Entity MUST maintain ``/.well-known/openid-federation`` endpoint accessibility for audit purposes (minimum 7 years).
2. **Certificate Chain Archive**: The Entity MUST keep X.509 Certificate chains accessible for existing Credential verification (minimum 7 years).
3. **Audit Log Preservation**: The Entity MUST archive federation protocol logs per regulatory requirements.



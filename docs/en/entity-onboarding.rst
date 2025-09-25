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

The IT-Wallet ecosystem is based on a federated trust infrastructure where participating entities MUST establish cryptographic trust relationships and maintain compliance with common security standards. The onboarding system addresses the main challenge of enabling secure Digital Credential operations while accommodating the different operational requirements that various participants need according to their role.

The onboarding framework consists of dual-pathway architecture where the technical registration procedures are tailored to the participant's role in the IT-Wallet ecosystem:

  1. For Authentic Sources requiring data-focused registration procedures.
  2. For operational Entities (Credential Issuers, Relying Parties, Wallet Providers) requiring cryptographic trust establishment through federation protocols.


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
     - Authoritative data providers for credential attributes
     - :ref:`entity-onboarding:Authentic Sources Registration Process`
     - Data authority validation, API integration (PDND/Custom)
   * - Credential Issuers
     - Generate and issue Digital Credentials using Authentic Source's data
     - :ref:`entity-onboarding:Federation Entities Onboarding Process`
     - IT-Wallet Trust Infrastructure compliance, :ref:`trust:The Infrastructure of Trust`
   * - Relying Parties 
     - Verify Digital Credentials for service access
     - :ref:`entity-onboarding:Federation Entities Onboarding Process`
     - IT-Wallet Trust Infrastructure compliance, :ref:`trust:The Infrastructure of Trust`
   * - Wallet Providers 
     - Provide Wallet Solutions to citizens
     - :ref:`entity-onboarding:Federation Entities Onboarding Process`
     - IT-Wallet Trust Infrastructure compliance :ref:`trust:The Infrastructure of Trust`, Wallet Attestation capabilities :ref:`wallet-instance-registration:Wallet Instance Initialization and Registration`.
   * - Wallet Instances 
     - User-level digital wallet applications
     - Indirect registration via Wallet Provider, see :ref:`wallet-instance-registration:Wallet Instance Initialization and Registration`.
     - Wallet Attestation from certified Wallet Provider

Administrative vs Technical Registration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The onboarding process follows a structured multi-phase approach:

  1. **Administrative Registration**: All entities MUST complete initial administrative registration that validates their legal standing, regulatory compliance, and organizational eligibility to participate in the IT-Wallet ecosystem.

  2. **Technical Registration**: Following administrative approval, entities make technical registration through specialised pathways:
    
    - **Authentic Source Registration**: Data-focused registration procedures with API integration validation.
    - **Federation Registration**: Cryptographic trust establishment as defined in Section :ref:`trust:The Infrastructure of Trust`.

  3. **IT-Wallet Registry Integration**:

    - **Claims Registry Integration**: Authentic Sources select standardized claim definitions from Claims Registry during capability declaration.
    - **Taxonomy Integration**: All entities use Taxonomy hierarchical classification (domains, categories, purposes) for organizational structure.
    - **AS Registry Integration**: Authentic Sources registered with their declared claims and capabilities, enabling CI discovery and coordination.
    - **Federation Registry Integration**: Operational entities included for trust validation during credential operations.
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
    - **Taxonomy Classification**: The entities MUST classify their data authority within the appropriate domain, category, and purpose structure.

  - **API Integration Standards**:

    - **Public Entities**: MUST integrate through PDND platform with e-service implementation following government standards.
    - **Private Entities**: MUST provide a complete OpenAPI 3.0 API Specification document that includes authorization framework, request/response schemas, error handling mechanisms, and sandbox environment for testing.

  - **Response Format Standardization**:

    - **Standard Claims Format**: The Entities MUST use Claims Registry identifiers and formats in all data responses.
    - **State Mapping**: The Entities MUST handle clear mapping between their internal states and standard credential states (valid, suspended, revoked).

  - **Security and Quality Assurance**:

    - **Security Standards**: The Entities MUST implement TLS 1.3 minimum with proper authentication and security mechanisms.
    - **User Authentication Evidence**: The Entities MAY request user authentication evidence from Credential Issuer before granting access to e-services for obtaining user attributes.
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
     - **REQUIRED**. Available claims with Domain and Category mapping:

       - Array of claim identifiers from Claims Registry that the Authentic Source provides (e.g., ``["given_name", "family_name", "driving_privileges"]``).
       - Taxonomy classification for Authentic Source scope (e.g., ``AUTHORIZATION`` domain, ``DRIVING_LICENSE`` category and ``["driving-authorization", "identity-verification"]`` purposes).
      
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
     - **OPTIONAL**. Visual branding suggestions for credentials using AS data:

       - Background color for Credentials in hexadecimal format (e.g., ``"#003d82"``).
       - Text color for Credentials in hexadecimal format (e.g., ``"#ffffff"``).
       - Logo URI with cryptographic integrity verification for credential branding.
       - Visual template URI with integrity verification for Credential presentation.

AS Registration Procedure
^^^^^^^^^^^^^^^^^^^^^^^^^

The AS registration follows a technical process as described below. 

**Step 1: Registration Package Preparation**

AS entity prepares registration information according to the requirements table above. A non-normative example of information in JSON format is provided below. 

.. code-block:: json

   {
     "as_id": "https://motorizzazione.gov.example",
     "organization_info": {
       "organization_name": "MIT -- Direzione Generale per la Motorizzazione",
       "organization_type": "public",
       "ipa_code": "m_inf",
       "legal_identifier": "80192770587",
       "organization_country": "IT",
       "homepage_uri": "https://www.gov.example/transport",
       "contacts": ["registry@gov.example", "technical-support@gov.example"],
       "policy_uri": "https://www.gov.example/transport/privacy-policy",
       "user_information": "Driving license data is available for licenses issued after January 1, 2020. For older licenses, contact the local motorization office."
     },
     "data_capabilities": [
       {
         "domain": "AUTHORIZATION",
         "category": "DRIVING_LICENSE",
         "intended_purposes": ["driving-authorization", "identity-verification"],
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

**Step 2: Technical Validation**

Supervisory Body validates submitted registration focusing on:

  - **Claims Registry Compliance**: Validation of claims format, identifiers, and existence in Claims Registry.
  - **Taxonomy Validation**: Verification that declared domains, categories, and purposes are valid taxonomy entries.
  - **API Integration Verification**:

    - **Public Entities**: PDND e-service specification compliance verification
    - **Private Entities**: OpenAPI 3.0 specification completeness including authorization framework, request/response schemas, error handling mechanisms, and sandbox environment.

  - **Response Format Standards**: Verification of Claims Registry format usage and state mapping specification.

**Step 3: AS Registry Publication**

Upon successful validation:

  - Authentic Source Entity published in AS Registry with complete declared capabilities.
  - Authentic Source becomes discoverable by Credential Issuers for integration requests.
  - Registration process complete: Authentic Source is ready for operational data provision.

AS-CI Integration Process
^^^^^^^^^^^^^^^^^^^^^^^^^

AS-CI integration occurs separately when Credential Issuers register specific credential types requiring AS data. The complete AS-CI integration process is detailed in Section ... .


.. note::
   AS registration is complete and independent of CI integration. AS entities become discoverable immediately upon AS Registry publication, while credential availability to end-users depends on subsequent CI registration and integration approval.

Federation Entities Onboarding Process
---------------------------------------

Federation Entities (Credential Issuers, Relying Parties, and Wallet Providers) MUST undergo systematic onboarding procedures to establish cryptographic trust relationships within the IT-Wallet ecosystem. The federation onboarding process establishes the distributed trust infrastructure through certificate issuance, trust chain configuration, and compliance attestation as detailed in :ref:`trust:The Infrastructure of Trust`.

Hierarchical Federation Authority Model
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The IT-Wallet federation implements a **hierarchical onboarding model** where Federation Entities can be onboarded by either:

  1. **Trust Anchor**: The root authority that can directly onboard any Federation Entity.
  2. **Intermediates**: Delegated authorities that onboard Leaf Entities on behalf of Trust Anchor.

This hierarchical approach enables **distributed onboarding management** while maintaining unified trust establishment. Both Trust Anchors and Intermediates act as **Federation Authorities** with the following onboarding capabilities:

  - **Certificate Issuance**: Issue X.509 certificates to their immediate subordinates with appropriate naming constraints as defined in :ref:`trust:X.509 PKI`.
  - **Metadata Policy Application**: Apply federation-specific metadata policies with **cascading effect** (Trust Anchor policies override Intermediate policies).
  - **Trust Mark Issuance**: Issue Federation Trust Marks attesting subordinate compliance with federation requirements.
  - **Trust Chain Construction**: Manage subordinate statements and trust chain validation through federation endpoints.

Therefore, Federation Entities MAY be onboarded through different paths:

  - **Direct Trust Anchor Onboarding**: Entity directly registers with the Trust Anchor.
  - **Intermediate-mediated Onboarding**: Entity registers with an appropriate Intermediate.




Federation Onboarding Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Federation Entities MUST comply with the following technical requirements before initiating the onboarding process:

  - **Entity Configuration Preparation**: The entities MUST publish an Entity Configuration (EC) signed with their private key at the ``/.well-known/openid-federation`` endpoint as defined in :ref:`trust:The Infrastructure of Trust`. The EC MUST include:

    - A ``jwks`` claim with a set of public keys in JSON Web Key (JWK) format containing the Federation Entity Public Key, using cryptographic algorithms as specified in :ref:`algorithms:Cryptographic Algorithms`
    - An ``iss`` claim with the Federation Entity Identifier as defined in :ref:`trust:Federation Roles`
    - A ``sub`` claim equal to the ``iss`` claim
    - ``iat`` and ``exp`` claims defining a valid time interval
    - A ``metadata`` claim containing entity-specific metadata organized by Metadata Types (see :ref:`credential-issuer-entity-configuration:Credential Issuer Entity Configuration`, :ref:`relying-party-entity-configuration:Relying Party Entity Configuration`, or :ref:`wallet-provider-entity-configuration:Wallet Provider Entity Configuration`)

  - **Federation Entity Public Key**: The entities MUST generate an elliptic public key in JSON Web Key (JWK) format using algorithms specified in :ref:`algorithms:Cryptographic Algorithms` to be used for signing Entity Configurations.

  - **Certificate Signing Request (CSR)**: The entities MUST prepare a CSR in PKCS #10 format containing the Federation Entity Public Key for X.509 certificate issuance by the Trust Anchor as defined in :ref:`trust:Trust Infrastructure Requirements`.

Federation Onboarding Procedure
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The federation onboarding follows a structured 4-step procedure that enables secure interactions among federation participants, **regardless of whether onboarding is performed by the Trust Anchor or an Intermediate**.

.. note::
   The following procedure applies to Wallet Providers, Credential Issuers and Relying Parties that wish to perform onboarding in the IT-Wallet federation. The **Federation Authority** is referred to Trust Anchor or Intermediate according to organizational characteristics and federation governance policies.

.. note::
   This section covers only the technical registration requirements. All administrative information (legal entity validation, regulatory compliance, organizational eligibility, etc.) is assumed to have been collected and validated by the Supervisory Body during the administrative registration phase, which is out of scope for this technical specification. Examples of administrative information include: legal entity name, business registration numbers, contact persons, legal compliance documentation, and operational authorizations.

.. plantuml:: plantuml/federation-onboarding-process.puml
    :width: 99%
    :alt: Federation entity onboarding process showing the 4-step procedure
    :caption: `Federation Entity Onboarding Process. <https://www.plantuml.com/plantuml/svg/ZLJ1Jcit4DtVhnYzHKNqNbvI6XQDb1QKqWfOW0A5BY8XnvwRkFYER-qnWRylruxbImZIszhZSywSEUDJpy9nQ0pyYGgTO6q9pearly8rhQnmIjCQRfoLw7qb0biApGfTLRN2iPQw5SJmvSFhBo0yrFXfrLdWZNMva4LLpMPmozZ2pzC-ymB_2-WPRiEgqTvtJsUpggeHXhy1YscwOB3bYKjFbdIqQ-JYZszm4rP6IxZ2LxXykFe6yzl5e2BB24wlDmosZcY758B3jVQCpY_feqiN2ebrhT4jIHCOkqKdXKUehMi4bxwEFq6_5qQhT2X8mHnT1oS58rnu7mH9Z2spo2tVezDrbhN3qvJujALIcR4nYvrRglKwk1qTBsdqVOl639_8RcbaMoIjXdMHYQHQgubxcFCDoYTea8KIBA9cMJJxKXdb8_pp_MJyQwyaEdF8oJAYgXA6-yRu8BlyrS5K0029eiRfExVaHcW2XxwrvB6Clq_z5UxEmAEfXrwl2Tz97rHeFFPfQw4DgZtA1VwBCbvlDMz0v_ahq5s_la9IPUg_J0zx_tVRpIMwjq1lpJFcgETy9xfSU0XakgGXd2a58eVfSQE9FKWZT9ClNqvaEaXwvRvZXIjDm6yWH4u5v_CVo4Xl5tCdPGD7BXtzxiDgXh67Hwr-OXSyFmgIRx9dBDwE1iMoIG5Qf64cdtg_mjmshS6EVMyr5YWjUNP1CZntWuH8jUkqrFs5rCb7sCNWyk4kshEaNdraZIZHZHpvbCuiiKGJZex7OxY-6km59bVcP4QYZl7DdpxRrmDS2QjCA2zqzppAmnTsGlA-xe8G0Tv_T3NcKFQ_JPayHRMa1GhrsgqfI8SntyA0RNS3zsbFSbjfIU1eCXwF9kF9VlVdpbctrtjQ560BktYadJb5Kg4n_mC0>`_



**Step 1: Onboarding Request Submission**

Federation Entity initiates the onboarding process by submitting a technical registration request including the following information:



.. list-table:: Federation Onboarding Technical Request Information
   :class: longtable
   :header-rows: 1
   :widths: 30 70

   * - **Technical Information Category**
     - **Requirements and Description**
   * - **Federation Entity Identifier**
     - **REQUIRED**. A unique URL that identifies the Federation Entity as defined in :ref:`trust:Federation Roles`.
   * - **Federation Entity Public Key (JWK)**
     - **REQUIRED**. Elliptic public key in JSON Web Key format used for signing Entity Configurations, using cryptographic algorithms specified in :ref:`algorithms:Cryptographic Algorithms`.
   * - **Certificate Signing Request (CSR)**
     - **REQUIRED**. CSR in PKCS #10 format for X.509 certificate issuance by the Trust Anchor. The CSR MUST:

       - Contain the Federation Entity Public Key to be certified.
       - Be signed with the corresponding private key.
       - Define the certificate Subject with required attributes as specified in :ref:`trust:X.509 Certificates Issuance` for Federation Entities.

.. warning::
   Before submitting the technical onboarding request, Federation Entities MUST ensure that their ``/.well-known/openid-federation`` endpoint publishes a valid Entity Configuration (as defined in :ref:`trust:Entity Configuration`) signed with their private key corresponding to the Federation Entity Public Key provided in the request.


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
   The Federation Entity Public Key in the ``jwks`` field and the public key contained in the ``certificate_signing_request`` MUST be the same key. The key is provided in two formats: JWK format for OpenID Federation operations and PKCS #10 CSR format for X.509 certificate issuance by the Trust Anchor.

.. note::
   The Entty Configuration Endpoint is constructed automatically by appending ``/.well-known/openid-federation`` to the Federation Entity Identifier (``entity_id``). Federation Entities do not need to specify this endpoint separately in the registration request.

**Step 2: Federation Authority Validation and Certificate Issuance**

Following the onboarding request submission, the **Federation Authority** (Trust Anchor or Intermediate) MUST perform:

  - Verification of information provided in the registration request.
  - Validation of the Entity Configuration published at the entity's ``/.well-known/openid-federation`` endpoint and its contained metadata (as defined in :ref:`trust:The Infrastructure of Trust`).
  - **Metadata Policy Application**: Application of federation-specific metadata policies to the entity's metadata based on organizational characteristics and authorization scope as defined in :ref:`trust:Subordinate Statements`. **Cascading Policy Effect**: When onboarded through an Intermediate, both Intermediate and Trust Anchor policies apply, with Trust Anchor policies taking precedence in case of conflicts.
  - **Certificate Issuance**: Certification of the Federation Entity Public Key with X.509 certificate issuance using the trust infrastructure detailed in :ref:`trust:Trust Infrastructure Requirements`. Intermediates issue certificates with appropriate **naming constraints** to scope certificate usage to their subordinates only.

Upon successful validation, the entity receives a response containing a certificate chain where:

  - The first element is the X.509 certificate that certifies the Federation Entity Public Key (issued by the Federation Authority)
  - **For Trust Anchor onboarding**: The second element is the Trust Anchor's self-signed X.509 certificate for validating the first certificate
  - **For Intermediate onboarding**: Additional elements include the Intermediate's certificate and the Trust Anchor's self-signed certificate, forming a complete certificate chain
  - All certificates are expressed in DER format encoded in Base64

Example certificate chain response:

.. code-block:: json

   [
     "MIIDqjCCA1GgAwIBAgIGAZc6/V9qMAoGCCqGSM49BAMCMIGzMQsw...",
     "MIIDQzCCAuigAwIBAgIGAZc6+XlDMAoGCCqGSM49BAMCMIGzMQsw..."
   ]

.. note::
   If validation fails, the entity receives a response with identified issues that must be resolved before submitting a new onboarding request.

**Step 3: Entity Configuration Update and Resolve Request**

After receiving the certificate chain from the Federation Authority, the entity MUST:

1. **Update Entity Configuration**:

   - Add an ``authority_hints`` claim with a JSON Array containing the **immediate Federation Authority's** Federation Entity Identifier (Trust Anchor for direct onboarding, or Intermediate for mediated onboarding) as defined in :ref:`trust:Federation Roles`
   - Update the Federation Entity Public Key in the ``jwks`` claim by adding an ``x5c`` claim with the complete certificate chain received from the Federation Authority

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

   Example JWK with certificate chain:

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

2. **Publish Updated Entity Configuration**: Publish the updated EC at the ``/.well-known/openid-federation`` endpoint as specified in :ref:`trust:The Infrastructure of Trust`

3. **Submit Resolve Request**: Call the **Trust Anchor's** ``/resolve`` endpoint (as defined in :ref:`trust:Trust Infrastructure Requirements`) with URL-encoded parameters:

   - ``sub``: Federation Entity Identifier
   - ``trust_anchor``: **Trust Anchor** Federation Entity Identifier (always the root Trust Anchor, even for Intermediate-mediated onboarding)

   Example resolve request:

   .. code-block:: http

      GET /resolve?sub=https%3A%2F%2Fcredentials.example.gov&trust_anchor=https%3A%2F%2Ftrust-anchor.example.gov HTTP/1.1
      Host: trust-anchor.example.gov

**Step 4: Resolve Response and Onboarding Completion**

Following the resolve request, the **Trust Anchor** performs:

  - **Trust Chain Reconstruction**: Reconstruction of a valid trust chain for the entity (including Intermediate statements if applicable) as defined in :ref:`trust:The Infrastructure of Trust`
  - **Federation Trust Mark Coordination**: Ensures the entity has received appropriate Federation Trust Marks from its immediate Federation Authority (Trust Anchor or Intermediate)
  - Generation of a signed JSON Web Token (JWT) using algorithms specified in :ref:`algorithms:Cryptographic Algorithms` containing the reconstructed trust chain and validated entity metadata
  - Transmission of an HTTP response containing the created JWT (Resolve Response)

If the response status code is 200 OK, the **entity onboarding is successfully completed**. The entity MUST:

  - Validate the JWT contained in the Resolve Response
  - Extract the trust chain and validated metadata from the JWT payload
  - **Trust Mark Integration**: Include the issued Federation Trust Mark in its Entity Configuration ``trust_marks`` claim for ongoing federation compliance attestation

The entity is now operational within the IT-Wallet federation and ready for credential lifecycle activities.

.. note::
   If the ``/resolve`` endpoint responds with status code 400 or 404, the entity must resolve the issues described in the response message before calling the resolve endpoint again. For other status codes, contact the Trust Anchor support.

.. note::
   **Federation Registry Integration**: Upon successful onboarding completion, the entity's Federation Entity Identifier becomes discoverable through the Trust Anchor's entity listing mechanisms (as defined in :ref:`trust:The Infrastructure of Trust`), indicating active federation participation. The entity becomes part of the federation infrastructure detailed in :ref:`registry:Registry Infrastructure`.

IT-Wallet Federation Trust Mark
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Federation Entities receive an IT-Wallet Federation Trust Mark during successful onboarding completion. **Trust Marks are issued by the immediate Federation Authority** (Trust Anchor for direct onboarding, Intermediate for mediated onboarding) and serve as verifiable attestations of federation membership and compliance with IT-Wallet technical requirements.

**Trust Mark Structure**

The IT-Wallet Federation Trust Mark is a signed JSON Web Token (JWT) containing the following claims:

.. list-table:: IT-Wallet Federation Trust Mark Claims
   :class: longtable
   :header-rows: 1
   :widths: 20 60 20

   * - **Claim**
     - **Description**
     - **Required**
   * - **iss**
     - Federation Authority issuing the Trust Mark (immediate superior: Trust Anchor or Intermediate)
     - |check-icon|
   * - **sub**
     - Federation Entity Identifier of the recipient
     - |check-icon|
   * - **id**
     - Unique Trust Mark identifier (``https://registry.itwallet.gov.it/federation_entity``)
     - |check-icon|
   * - **iat**
     - Trust Mark issuance timestamp
     - |check-icon|
   * - **exp**
     - Trust Mark expiration timestamp
     - |check-icon|
   * - **organization_type**
     - Entity organization type (``public`` or ``private``)
     - |check-icon|

**Trust Mark Validation**

Federation participants validate Trust Mark status through two mechanisms:

1. **Static Validation**: Cryptographic verification using the issuing Federation Authority's public key from the trust chain
2. **Dynamic Validation**: Real-time status verification via the issuing Federation Authority's ``/trust_mark_status`` endpoint as defined in :ref:`trust:Federation API endpoints`

**Trust Mark Integration**

Federation Entities MUST integrate the Trust Mark in their Entity Configuration using the ``trust_marks`` claim as specified in :ref:`trust:Entity Configuration Leaves and Intermediates`.

**Example 1: Direct Trust Anchor Onboarding**

Entity onboarded directly by Trust Anchor:

.. code-block:: json

   {
     "iss": "https://credentials.example.gov",
     "sub": "https://credentials.example.gov",
     "jwks": { },
     "authority_hints": ["https://trust-anchor.eid-wallet.example.it"],
     "trust_marks": [
       "eyJhbGciOiJFUzI1NiIsImtpZCI6IlRydXN0QW5jaG9yS2V5SWQiLCJ0eXAiOiJKV1QifQ..."
     ],
     "metadata": { }
   }

**Example 2: Intermediate-Mediated Onboarding**

Entity onboarded through a sectoral Intermediate:

.. code-block:: json

   {
     "iss": "https://healthcare-ci.example.gov",
     "sub": "https://healthcare-ci.example.gov",
     "jwks": { },
     "authority_hints": ["https://healthcare.intermediate.eid-wallet.example.it"],
     "trust_marks": [
       "eyJhbGciOiJFUzI1NiIsImtpZCI6IkhlYWx0aGNhcmVJbnRlcm1lZGlhdGVLZXlJZCIsInR5cCI6IkpXVCJ9..."
     ],
     "metadata": { }
   }

.. note::
   **Trust Chain Construction**: In Intermediate-mediated onboarding, the complete trust chain includes: Entity Configuration → Intermediate Subordinate Statement → Trust Anchor Subordinate Statement. The Trust Anchor's ``/resolve`` endpoint constructs the full chain regardless of onboarding path.


Entity Lifecycle Management
----------------------------

This section provides technical implementation procedures for entity lifecycle management. For high-level lifecycle concepts and business processes, see :ref:`onboarding-high-level:Entity Lifecycle Management`.

Lifecycle Coordination Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
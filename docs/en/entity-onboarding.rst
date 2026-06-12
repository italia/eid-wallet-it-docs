.. include:: ../common/common_definitions.rst
.. include:: ../common/symbols.rst

Entity Onboarding
=================

This section defines the technical specifications for entity lifecycle management in the IT-Wallet ecosystem based on the **Registry Infrastructure** defined in :ref:`registry:Registry Infrastructure`. This includes initial onboarding procedures, ongoing management operations, such as data updates and modifications, and federation exit processes.

For a high-level overview of the onboarding process, see :ref:`onboarding-high-level:Onboarding System`. The Section :ref:`onboarding-high-level:Onboarding Journey Maps` provides an onboarding journey map from the perspective of Entity's operators.

Overview
--------

Entity Onboarding System Architecture
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The IT-Wallet ecosystem operates on a federated trust infrastructure, requiring participating entities to establish mutual trust before engaging in any interactions involving User attributes.

The onboarding framework defines technical registration procedures based on the type of participant:

  1. Authentic Sources follow data-focused registration processes.
  2. Operational Entities (Credential Issuers, Relying Parties, Wallet Providers) follow trust establishment procedures.

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
     - **Key Requirements**
   * - Authentic Sources
     - Authoritative data providers for Digital Credential attributes
     - :ref:`entity-onboarding:Authentic Sources Registration Process`
     - Data authority validation; API integration (PDND)
   * - Credential Issuers
     - Generate and issue Digital Credentials using Authentic Source data
     - :ref:`entity-onboarding:Federation Entities Onboarding Process`
     - IT-Wallet Trust Infrastructure compliance; see :ref:`trust-infrastructure:The Infrastructure of Trust`
   * - Relying Parties
     - Verify Digital Credentials for service access
     - :ref:`entity-onboarding:Federation Entities Onboarding Process`
     - IT-Wallet Trust Infrastructure compliance; see :ref:`trust-infrastructure:The Infrastructure of Trust`
   * - Wallet Providers
     - Provide wallet solutions to citizens
     - :ref:`entity-onboarding:Federation Entities Onboarding Process`
     - IT-Wallet Trust Infrastructure compliance (see :ref:`trust-infrastructure:The Infrastructure of Trust`); Wallet Attestation capabilities (see :ref:`wallet-instance-registration:Wallet Instance Initialization and Registration`)
   * - Wallet Instances
     - User-level digital wallet applications
     - Indirect registration via Wallet Provider, see :ref:`wallet-instance-registration:Wallet Instance Initialization and Registration`
     - Wallet Attestation from trustworthy Wallet Provider

Administrative and Technical Registration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The onboarding process follows a structured multi-phase approach:

  1. **Administrative Registration**: All entities MUST complete initial administrative registration that validates their legal standing, regulatory compliance, and organizational eligibility to participate in the IT-Wallet ecosystem.

  2. **Technical Registration**: Following administrative approval, entities make technical registration through specialised pathways:

    - **Authentic Source Registration**: Data-focused registration procedures with API integration validation.
    - **Federation Registration**: Cryptographic trust establishment as defined in Section :ref:`trust-infrastructure:The Infrastructure of Trust`.

  3. **IT-Wallet Registry Integration**:

    - **Claims Registry Integration**: Authentic Sources select standardized claim definitions from Claims Registry during capability declaration.
    - **Taxonomy Integration**: All entities use Taxonomy hierarchical classification (domains, classes, purposes) for organizational structure to categorize Credentials.
    - **Authentic Source Registry Integration**: Authentic Sources registered with their declared claims and capabilities, enabling Credential Issuers discovery and coordination.
    - **Federation Registry Integration**: Operational entities included for trust validation during Credential operations.
    - **Catalog Integration**: Credential types published in :ref:`registry:Digital Credentials Catalog Structure` based on supervisory body policies for public discovery eligibility.

All registry components and their interactions are detailed in :ref:`registry:Registry Infrastructure`.

Authentic Sources Registration Process
--------------------------------------

Authentic Sources MUST complete a structured registration process to confirm their status as authoritative data providers in the IT-Wallet ecosystem. This process includes specifying requirements and undergoing procedural validation, as detailed in :ref:`onboarding-high-level:Authentic Source Operator Journey`.

Authentic Source Registration Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Authentic Sources MUST comply with the following technical requirements:

  - **Claims Compliance**:

    - **Claims Registry Adoption**: The Entities MUST use standardized Claims Registry identifiers in data responses. Custom claim mapping is not allowed.

  - **API Integration Standards**:

    - **Public Entities**: MUST integrate through PDND platform with e-service implementation following national specifications.
    - **Private Entities**: MUST provide a complete `OAS3`_ Specification document that includes authorization framework, request/response schemas, error handling mechanisms, and sandbox environment for testing.

  - **Response Format Standardization**:

    - **Standard Claims Format**: The Entities MUST use Claims Registry identifiers and formats in all data responses.
    - **State Mapping**: The Entities MUST handle clear mapping between their internal states and standard Credential states (valid, suspended, revoked).

  - **Security and Quality Assurance**:

    - **Security Standards**: The Entities MUST implement TLS 1.3 or higher with robust authentication mechanisms, forward secrecy, and cryptographic algorithms that meet current and emerging security standards, end-to-end confidentiality and integrity of all communications, maintaining compliance with evolving regulatory requirements and industry best practices.
    - **User Authentication Evidence**: The Entities MAY request User authentication evidence from Credential Issuer before granting access to e-services for obtaining User attributes.
    - **Data Quality**: The Entities MUST specify update frequency and provide data freshness guarantees.
    - **Audit Trail**: The Entities MUST implement logging capabilities for all data access and provisioning activities.

Authentic Sources Registration Information Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::
  Only Italian Authentic Sources can be onboarded at the current stage of IT-Wallet.

During registration, Authentic Sources MUST provide the following information:

.. list-table:: Authentic Source Registration Information Requirements
   :class: longtable
   :header-rows: 1
   :widths: 30 70

   * - Information Category
     - Description and Examples
   * - **Organization Information**
     - **REQUIRED**. Organization Details including:

       - Organization name, type ("public" or "private") and country (ISO 3166-1 alpha-2).
       - Administrative identifier codes such as IPA registration code (REQUIRED only for public Authentic Sources) and legal identifier (tax payer's number or VAT number).
       - Contact Information including technical and administrative contacts, such as email addresses, homepage URI, privacy policy URI.
   * - **Data Capabilities Declaration**
     - **REQUIRED**. Available claims:

       - Array of claim identifiers from Claims Registry that the Authentic Source provides (e.g., ``["given_name", "family_name", "driving_privileges"]``).
       - Intended Purposes for verification, using taxonomy purpose identifiers (e.g. ``["DRIVING_RIGHTS_VERIFICATION"]``).

   * - **API Implementation Details**
     - **REQUIRED**. Integration information details:

       - Authorization framework for API access.
       - API definitions such as Request/Response Formats, including error management.
   * - **Data Provision Capabilities**
     - **REQUIRED**. Indicates if Authentic Source supports immediate/deferred data provision (boolean).    
   * - **User Information**
     - **OPTIONAL**. Markdown-formatted text containing human-readable information about data availability constraints or limitations. For example, if the Authentic Source database only contains data registered after a specific date, this information MUST be conveyed to Users.

       **Example**: "Driving license data is available for licenses issued after January 1, 2020. For older licenses, contact the local motorization office.".

   * - **Display Properties**
     - **OPTIONAL**. Visual branding suggestions for Digital Credentials using Authentic Source data:

       - Background color for Digital Credentials in hexadecimal format (e.g., ``"#003d82"``).
       - Logo URI with cryptographic integrity verification for Digital Credential branding.
       - Visual template URI with integrity verification for Digital Credential presentation.

Authentic Source Registration Procedure
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Authentic Source registration follows a technical process as described below.

.. plantuml:: plantuml/as-registration-process.puml
    :width: 99%
    :alt: Authentic Source registration process showing the 3-step procedure
    :caption: `Authentic Source Registration Process. <https://www.plantuml.com/plantuml/svg/TLD1Rziw3BxxLn0zlG1vhs_hBK26TkqEFMmBbcAdNcY9SRJAaaPARRDVFzfE6iVBWXmCyUF7Z_p8Qyd8kRGURahUKiZEm3eMDWJVg76I6REB0LOS3ObKM78CfQs9goeXAzmb31akfkaNWAB_Kz2w9E9d9v5ty37QNG-IUiAqFfGUuanDLIsNiCwKuDrYeWlD4pQa-YZX_csvh2hD-_U3PY_s4OB83GRtQu2ui8dSzj-FuP_xrGsOQ6aEdXhqu6pNoSOHp_KzP3HPPYFAEpA-exIO4Gmch9rtsP4erwr7ryfR1oCkcSC3liOGsnreleY-cbx2AVV61OARrJsuDdbgDNtGR2cZyrsDrTsNkyklYKA7klhlVv14vYpRkW_i1gM9eyvU4LFDhct9EinqQMb3p6HXu-CBI4afSZuGIgs4fMvT1XvxmFIpaEIZIUyNy41c6rIGX-_edJqQ8_MUwX0Wc8xCH6tSOJ2asWQVvgTpf5T5aW9cOpvYRVLlCrOg6rjqGTFrXPh8ZlGx5KvHICPCjrioJuC5GP7xDf-9nsoT2IEf41b6bipEDSeaAGOX69e2oHWiiZstDqMmeRb2kiGMKtAXcUbU-poUg1JJdUMc-0hqDzH4cHm9fivwz5hc-PZRQwUiCoGlD6RTeFDa_s3yGQOFlxYyXH6H4odz7dMBuBXVMO4S0QrbLQS5WZrknzK2HYSEgr9xPwOBmjGiXf1iE_WdDJ_lr0_WVQBMEtG0TZX8ErviBQlGDwxF-4GTaNLYebg9jIUebUMMgLyjz73VDSAYwtvsZ8ToYyV0X7RNsGWnqH16FxcogWfHjNN5b6lUgr01MgkN1pKf8PqAUhj4hygABil9gD9nL5LrJS6Mrly6>`_ 

**Step 1 - Registration Package Preparation**: The Entity prepares registration information according to the requirements table above. A non-normative example of information in JSON format is provided below. 

.. list-table:: First-level Fields of the Authentic Source Registration
   :class: longtable
   :widths: 30 70
   :header-rows: 1

   * - **Field Name**
     - **Description**
   * - **id**
     - REQUIRED. Unique identifier of the Authentic Source Registry (e.g., ``urn:authentic-sources:it-wallet``).
   * - **version**
     - REQUIRED. The version of the Authentic Source Registry (e.g., ``1.0.0``).
   * - **last_modified**
     - REQUIRED. The timestamp indicating when the list was last updated (e.g., ``2025-03-15T12:00:00Z``).
   * - **localization**
     - REQUIRED. Localization configuration object containing:

       * **default_locale**: Default locale code (e.g., ``it``).
       * **available_locales**: Array of supported locale codes (e.g., ``["en", "it"]``).
       * **base_uri**: Base URI for localization bundle retrieval (e.g., ``https://trust-registry.eid-wallet.example.it/.well-known/l10n/authentic-sources/``).
       * **version**: Version of the localization bundle format.
   * - **authentic_sources**
     - REQUIRED. A JSON Array where each entry is a JSON Object representing an Authentic Source entity. Each object contains the parameters defined in the "Authentic Sources Parameters" table below, including entity identification, organizational information, data capabilities, and integration methods.

.. list-table:: Authentic Sources Parameters
   :class: longtable
   :widths: 25 15 60
   :header-rows: 1

   * - **Parameter**
     - **Type**
     - **Description**
   * - **entity_id**
     - string
     - REQUIRED. Unique identifier following the normative schema: ``https://{organization_domain}[/{optional_path}]``.
   * - **organization_info**
     - JSON object
     - REQUIRED. Legal entity details and organizational metadata.
   * - **organization_info.organization_name**
     - JSON Object Array
     - REQUIRED. Object array containing the organization name in multiple languages. It MUST contain ``locale`` and ``name`` claims.
   * - **organization_info.organization_type**
     - string
     - REQUIRED. Entity classification: ``"public"`` or ``"private"``.
   * - **organization_info.ipa_code**
     - string
     - REQUIRED only for Public AS. IPA registration code for government entities.
   * - **organization_info.legal_identifier**
     - string
     - REQUIRED. Legal registration identifier (Fiscal Code/VAT Number, or equivalent national identifier for foreign entities).
   * - **organization_info.homepage_uri**
     - string
     - REQUIRED. URL pointing to the organization's homepage.
   * - **organization_info.contacts**
     - String Array
     - REQUIRED. Array of contact email addresses for at least one user-support, one application, and one systems specialist.
   * - **organization_info.dpa_contact**
     - string
     - REQUIRED. An e-mail address of Authentic Source DPA.
   * - **organization_info.policy_uri**
     - string
     - REQUIRED. URL to privacy policy document.
   * - **organization_info.tos_uri**
     - string
     - OPTIONAL. URL to terms of service document.
   * - **organization_info.organization_country**
     - string
     - REQUIRED. Two-letter ISO 3166-1 alpha-2 country code of the organization.
   * - **organization_info.logo_uri**
     - string
     - OPTIONAL. URL to the organization's logo image.
   * - **organization_info.logo_uri#integrity**
     - string
     - CONDITIONAL. Cryptographic digest of the logo image resource for integrity verification. REQUIRED if ``logo_uri`` is present. Format: ``{digest_method}-{digest_value}`` (e.g., ``"sha-256-abc123..."``).
   * - **organization_info.logo_alt_text_l10n_id**
     - string
     - OPTIONAL. Alternative text for the organization's logo image.
   * - **organization_info.logo_extended_uri**
     - string
     - OPTIONAL. URL to the organization's extended logo image.
   * - **organization_info.logo_extended_uri#integrity**
     - string
     - CONDITIONAL. Cryptographic digest of the extended logo image resource for integrity verification. REQUIRED if ``logo_extended_uri`` is present. Format: ``{digest_method}-{digest_value}`` (e.g., ``"sha-256-abc123..."``).
   * - **organization_info.logo_extended_alt_text_l10n_id**
     - string
     - OPTIONAL. Alternative text for the organization's extended logo image.
   * - **data_capabilities**
     - JSON Objects Array
     - REQUIRED. Array containing data capability specifications.
   * - **data_capabilities[].dataset_id**
     - string
     - REQUIRED. The :term:`Dataset_id` within the scope of the Authentic Source, which MAY be used as a query parameter for the ``GetAttributeClaims`` service.
   * - **data_capabilities[].data_origin**
     - JSON Object Array
     - REQUIRED. Object array containing the human-readable name of the data origin or department providing the data in multiple languages. It MUST contain ``locale`` and ``name`` claims.
   * - **data_capabilities[].intended_purposes**
     - String Array
     - REQUIRED. Business purposes served, using taxonomy purpose identifiers (e.g., ``["IDENTITY_VERIFICATION", "DRIVING_RIGHTS_VERIFICATION"]``).
   * - **data_capabilities[].available_claims**
     - String Array
     - REQUIRED. Claims available from this data capability.
   * - **data_capabilities[].available_claims.claim_name**
     - string
     - REQUIRED. It Contains the name of the claim.
   * - **data_capabilities[].available_claims.order**
     - number
     - REQUIRED. Defines the order in which the information would be shown.
   * - **data_capabilities[].available_claims.mandatory**
     - boolean
     - REQUIRED. Defines if a claim is always available or not.
   * - **data_capabilities[].integration_method**
     - string
     - REQUIRED. Authorization framework used for data access. MUST be ``"pdnd"``.
   * - **data_capabilities[].integration_endpoint**
     - string
     - OPTIONAL. Service access point (PDND endpoint).
   * - **data_capabilities[].api_specification**
     - string
     - OPTIONAL. URL to `OAS3`_ specification document for this data capability.
   * - **data_capabilities[].data_provision**
     - JSON object
     - OPTIONAL. Data provision capabilities and timing specifications.
   * - **data_capabilities[].data_provision.immediate_flow**
     - boolean
     - REQUIRED. Indicates if the Authentic Source supports immediate data provision.
   * - **data_capabilities[].data_provision.deferred_flow**
     - boolean
     - REQUIRED. Indicates if the Authentic Source supports deferred data provision.
   * - **data_capabilities[].data_provision.max_response_time_minutes**
     - integer
     - CONDITIONAL. Maximum time in minutes for the Authentic Source to respond to a deferred data provision request. REQUIRED if ``deferred_flow`` is ``true``.
   * - **data_capabilities[].data_provision.notification_methods**
     - String Array
     - CONDITIONAL. Array of notification methods supported by the Authentic Source for deferred data provision, such as ``"push"``, ``"poll"``. REQUIRED if ``deferred_flow`` is ``true``.
   * - **data_capabilities[].user_information**
     - JSON object Array
     - OPTIONAL. Object array containing information about the data capability relevant to the User in multiple languages. This string MUST be provided by the Authentic Source to the Trust Anchor during onboarding. The Markdown formatting can be plain text or a combination of text and links. For example, if the Authentic Source's database only contains data registered *after* a specific date, this information MUST be conveyed through this key. It MUST contain ``locale`` and ``description`` claims.
   * - **data_capabilities[].administrative_expiration_user_info**
     - JSON object Array
     - OPTIONAL. Object array containing information in multiple languages for the User about the administrative expiration status of the dataset and, eventually recommended actions. This string MUST be provided by the Authentic Source to the Trust Anchor during onboarding. The Markdown formatting can be plain text or a combination of text and links. It MUST contain ``locale``, ``title`` and ``description`` claims.
   * - **data_capabilities[].allowed_states**
     - JSON object Array
     - OPTIONAL. Object array containing information in multiple languages for the User about the current status of the dataset and, eventually recommended actions. The status values are defined in the :ref:`credential-revocation:Token Status Lists` Section. It MUST contain ``locale``, ``title``, ``description`` and ``<Status-Type-Value>`` claims.
   * - **data_capabilities[].service_documentation_uri**
     - string
     - OPTIONAL. URL pointing to the Authentic Source service documentation.
   * - **data_capabilities[].update_frequency**
     - string
     - OPTIONAL. Indicates how frequently the Authentic Source updates its data. Possible values: ``"real_time"`` (near real-time updates, typically within minutes), ``"daily"``, ``"weekly"``, ``"monthly"``, ``"on_demand"``.
   * - **data_capabilities[].logo_uri**
     - string
     - OPTIONAL. URL to the logo image related to the data.
   * - **data_capabilities[].logo_uri#integrity**
     - string
     - CONDITIONAL. Cryptographic digest of the logo image resource for integrity verification. REQUIRED if ``logo_uri`` is present. Format: ``{digest_method}-{digest_value}`` (e.g., ``"sha-256-abc123..."``).
   * - **data_capabilities[].background_color**
     - string
     - OPTIONAL. String value of the background color related to be displayed together with the data.
   * - **data_capabilities[].contacts**
     - String Array
     - OPTIONAL. Array of customer service contact email addresses.

.. literalinclude:: ../../examples/as-registration-example.json
   :language: json
   :caption: Non-normative Authentic Source Registration example

**Step 2 - Technical Validation**: Supervisory Body validates submitted registration focusing on:

  - **Claims Registry Compliance**: Validation of claims format, identifiers, and existence in Claims Registry.
  - **Taxonomy Validation**: Verification that declared purposes are valid taxonomy entries.
  - **API Integration Verification**:

    - **Public Entities**: e-Service PDNDspecification compliance verification
    - **Private Entities**: `OAS3`_ specification completeness including authorization framework, request/response schemas, error handling mechanisms, and sandbox environment.

  - **Response Format Standards**: Verification of Claims Registry format usage and state mapping specification.

**Step 3 - Authentic Source Registry Publication**: Upon successful validation:

  - Authentic Source Entity is published in the Authentic Source Registry with complete declared capabilities.
  - Authentic Source becomes discoverable by Credential Issuers for integration requests.
  - Authentic Source is ready for operational data provision.

.. note::
   Authentic Source registration is complete and independent of Credential Issuer integration. Authentic Sources become discoverable immediately upon Authentic Source Registry publication, while Credential availability to end Users depends on administrative Authentic Source to Credential Issuer authorization followed by successful technical integration and Supervisory Body policy approval for catalog eligibility.

Authentic Source to Credential Issuer Authorization Process
-----------------------------------------------------------

Following administrative Authentic Source to Credential Issuer authorization obtained during the administrative registration phase, technical integration procedures establish the operational API connections and data access mechanisms between Credential Issuers and Authentic Sources.

Technical integration encompasses:

- **API Endpoint Configuration**: Establishment of secure API connections as specified in Authentic Source technical specifications (PDND e-services).
- **Claims Mapping Validation**: Verification that Credential Issuer implementation correctly maps Authentic Source data responses to standardized Claims Registry identifiers.
- **Data Flow Testing**: Validation of immediate or deferred data provision capabilities and error handling mechanisms.
- **Security Implementation**: Configuration of authentication, authorization, and audit logging as required by Authentic Source security standards.

Federation Entities Onboarding Process
---------------------------------------

Federation Entities, including Credential Issuers, Relying Parties, and Wallet Providers, must complete onboarding procedures to become eligible participants in the IT-Wallet ecosystem. This process establishes distributed trust by issuing X.509 Certificates, validating Trust Chains, and confirming compliance, as described in :ref:`trust-infrastructure:The Infrastructure of Trust`.

Hierarchical Federation Authority Model
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The IT-Wallet federation implements a **hierarchical onboarding model** where Federation Entities MUST be onboarded by one of the following actors:

  1. **Trust Anchor**: The root authority that has the capability to directly onboard any Federation Entity.
  2. **Intermediates**: Delegated authorities that onboard Leaf Entities on behalf of Trust Anchor.

Both Trust Anchors and Intermediates act as **Federation Authorities** with the following onboarding capabilities:

  - **X.509 Certificate Issuance**: Issue X.509 Certificates to their Immediate Subordinates with appropriate naming constraints as defined in :ref:`trust-infrastructure:X.509 PKI`.
  - **Metadata Policy Application**: Apply federation-specific metadata policies with **cascading effect** (Trust Anchor policies override Intermediate policies).
  - **Trust Mark Issuance**: Issue Federation Trust Marks attesting Subordinate capabilities and grants, according to the trust framework.

Therefore, Federation Entities MAY be onboarded through different paths:

  - **Direct Trust Anchor Onboarding**: Entity directly registers with the Trust Anchor.
  - **Intermediate-mediated Onboarding**: Entity registers with an appropriate Intermediate.

Federation Onboarding Prerequisites
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Federation Entities MUST comply with the following technical requirements before initiating the onboarding process:

  - **Key Generation**: The entities MUST generate at least two key pairs using elliptic curve cryptography as specified in :ref:`algorithms:Cryptographic Algorithms`:

    - **Federation Key Pair**: Used for signing Entity Configurations and attesting application specific keys. For security best practices and operational continuity, entities SHOULD maintain multiple Federation Entity Keys (at least two) to enable secure key rotation and incident response without impacting entities that have cached Entity Configurations.
    - **Application Specific Key Pair(s)**: Used for entity-specific protocol operations, such as Credential issuance and Credential presentation.

  - **Application Specific Key Attestation**: The entities MUST create self-signed X.509 Certificates for their application specific keys using the Federation Entity Private Key.

  - **Entity Configuration Preparation**: The entities MUST publish an Entity Configuration (EC) signed with their Federation Entity Private Key at the ``/.well-known/openid-federation`` endpoint as defined in :ref:`trust-infrastructure:The Infrastructure of Trust`. The EC MUST include:

    - A ``jwks`` claim containing the Federation Entity Keys in JSON Web Key (JWK) format.
    - An ``iss`` claim with the Federation Entity Identifier as defined in :ref:`trust-infrastructure:Federation Roles`.
    - A ``sub`` claim equal to the ``iss`` claim.
    - ``iat`` and ``exp`` claims defining a valid time interval.
    - A ``metadata`` claim containing entity-specific metadata organized by Metadata Types (see :ref:`credential-issuer-entity-configuration:Credential Issuer Entity Configuration`, :ref:`relying-party-entity-configuration:Relying Party Entity Configuration`, or :ref:`wallet-provider-entity-configuration:Wallet Provider Entity Configuration`) with application specific keys included in the metadata ``jwks`` fields and self-signed X.509 Certificates in the corresponding ``x5c`` claims.

  - **X.509 Certificate Signing Request (CSR)**: The entities MUST prepare a X.509 Certificate Signing Request (CSR) in PKCS #10 format containing **the Federation Entity Key** for X.509 Certificate issuance by the Federation Authority, as defined in :ref:`trust-infrastructure:X.509 Certificates Issuance`.

Key Management Security Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

All federation entities SHOULD maintain at least two signing keys attested by the Trust Anchor:

- **Active Key**: Used for current signing operations
- **Backup Key**: Available for immediate activation during incidents or planned key rotation

This dual-key approach enables:
- Secure key rotation without service interruption
- Rapid incident response when primary keys are compromised
- Continuity for entities with cached Entity Configurations
- Prevention of validation issues during key transitions

The backup key MUST be:
- Registered by the Trust Anchor before deployment
- Published in the entity's JWKS alongside the active key
- Ready for immediate activation without additional certification steps
- Maintained with the same security standards as the active key

Federation Onboarding Procedure
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The federation onboarding follows a structured 4-step procedure, it can be performed by the Trust Anchor or an Intermediate.

.. note::
   The following procedure applies to Wallet Providers, Credential Issuers and Relying Parties that wish to perform onboarding in the IT-Wallet federation. The **Federation Authority** is referred to Trust Anchor or Intermediate according to organizational characteristics and federation governance policies.

.. note::
   This section covers the technical registration requirements. All administrative information, such as legal entity validation, regulatory compliance, organizational eligibility, is assumed to have been collected and validated by the Supervisory Body during the administrative registration phase, which is out of scope for this technical specification. Examples of administrative information include: legal entity name, business registration numbers, contact persons, legal compliance documentation, and operational authorizations.

.. plantuml:: plantuml/federation-onboarding-process.puml
    :width: 99%
    :alt: Federation entity onboarding process showing the 4-step procedure
    :caption: `Federation Entity Onboarding Process. <https://www.plantuml.com/plantuml/svg/ZLDDRnCn4BtxLunwQgIavOCUY4W_b1PKAWHAeN2e54tiSJEjrrxMOqB-FVknoswL8769el6yjs_Up3kFWeMap2bC4dpALbGebPSrrfoZ5pXuJuOA50uUhhomR0y08rZwPzT5adKekaP1fMOpk1NAuUKKFljLmCAmVu05_KmK1MxJAkCOA-XiffGbc9o2uBHv40Wzf6WWz_wmaGBNbsFuabQEDTpG5Zv-lubZcDykugZ_wgifx5C7T-ZOD4Nq1kPK25lMA0JNCIRqccf1WfsWEohORg6W1uxIyh6teSZg_trdnqtGwfm7R_aXjHWi9pW-sf1paoSVDluuvEJPJ6mlaxp90tiPS5xakTj2He861I4FZZLJX0tB6ZH6ZRL7P2tf8QuQXk37qScBjyCX8-0gf5B9pe87ZaPWN_ivuFj0lkgdeQjVYnG5Fc7n5A7q0wWcKWgT37sEIMkAqIQd000QJajJM3opr5HmorGeSf6611RPaTa1FvAkdoihUhW1haQFYhpfp-7r57OdlgmSNP0KJB_GjNVO3rmVQQXk48LA6XJAo5TtU6n9zFeifjMicNd9PgHwRNjniA2O1ny93alW61utfMs7Eni2lKRsSJJ-k_HblVJjIBaGyiPerElMRP1jJhtimKwwg5LwfQekix9wrlzTLj3Pk-htj5S_f1X8xekZvyw-cSB-U_-Mrrb0RuRvduSiToHjxYrr7sswzp9Dx_q4Bem1x5AyNBEN2DeXPztZxnFT5Bfix5ZQTVOEj1IzZ2O4SGsfbcFWQluVkLNdv4tAt1y0>`_

**Step 1 - Onboarding Request Submission**: Federation Entity initiates the onboarding process by submitting a technical registration request including the following information.

.. list-table:: Federation Onboarding Technical Request Information
   :class: longtable
   :header-rows: 1
   :widths: 30 70

   * - **Technical Information Category**
     - **Requirements and Description**
   * - **Federation Entity Identifier**
     - **REQUIRED**. A unique URL that identifies the Federation Entity as defined in :ref:`trust-infrastructure:Federation Roles`.
   * - **Federation Entity Key (JWK)**
     - **REQUIRED**. Elliptic public key in JSON Web Key format used for signing Entity Configurations and attesting application specific keys, using cryptographic algorithms specified in :ref:`algorithms:Cryptographic Algorithms`.
   * - **X.509 Certificate Signing Request (CSR)**
     - **REQUIRED**. CSR in PKCS #10 format for X.509 Certificate issuance by the Federation Authority. The CSR MUST:

       - Contain **only the Federation Entity Keys**.
       - Be signed with the corresponding Federation Entity Private Key.
       - Define the X.509 Certificate Subject with required attributes as specified in :ref:`trust-infrastructure:X.509 Certificates Issuance` for Federation Entities.

.. warning::
   Before submitting the technical onboarding request, Federation Entities MUST ensure that their ``/.well-known/openid-federation`` endpoint publishes a valid Entity Configuration (as defined in :ref:`trust-infrastructure:Entity Configuration`) signed with their Federation Entity Private Key corresponding to the Federation Entity Key provided in the request. The Entity Configuration MUST already include application specific keys in the metadata with self-signed X.509 Certificates in the ``x5c`` claims.

A non-normative example of the technical information structure that Federation Entities submit during Step 1 onboarding request:

.. literalinclude:: ../../examples/federation-onboarding-request-example.json
   :language: json
   :caption: Federation onboarding request example

The example below shows the decoded content of the CSR:

.. literalinclude:: ../../examples/csr-decoded-example.txt
   :language: text
   :caption: CSR decoded content example

.. note::
   The CSR Subject attributes MUST comply with the requirements specified in :ref:`trust-infrastructure:X.509 Certificates Issuance` for Federation Entities.

.. note::
   The Federation Entity Keys contained in the ``jwks`` object and the public keys contained in the ``certificate_signing_requests`` object MUST match. The keys are provided in two formats: JWK format and PKCS #10 CSR format for X.509 Certificate issuance. Application specific keys are included only in the Entity Configuration metadata, and they MUST NOT be included in the onboarding request.

.. note::
   The Entity Configuration Endpoint is constructed automatically by appending ``/.well-known/openid-federation`` to the Federation Entity Identifier (``entity_id``). Federation Entities do not need to specify this endpoint separately in the registration request.

**Step 2 - Federation Authority Validation and X.509 Certificate Issuance**: Following the onboarding request submission, the **Federation Authority** MUST perform:

  - Verification of information provided in the registration request.
  - Validation of the Entity Configuration, and the metadata contained in it, published at the entity's ``/.well-known/openid-federation`` endpoint (as defined in :ref:`trust-infrastructure:The Infrastructure of Trust`).
  - **Metadata Policy Application**: Application of federation-specific metadata policies to the entity's metadata based on organizational characteristics and authorization scope as defined in :ref:`trust-infrastructure:Subordinate Statements`. When onboarded through an Intermediate, both Intermediate and Trust Anchor policies apply, with Trust Anchor policies taking precedence in case of conflicts.
  - **X.509 Certificate Issuance**: Certification of the Federation Entity Key with X.509 Certificate issuance using the trust infrastructure detailed in :ref:`trust-infrastructure:X.509 Certificates Issuance`. Intermediates MUST issue X.509 Certificates using appropriate **naming constraints** limiting the use of DNS names and URIs to their subordinates only.

  Upon successful validation, the entity receives a Registration Identifier.

.. note::
   If issuance process fails, the requestor entity receives a response with identified issues to be resolved before submitting a new onboarding request.

.. note::
   Each entity can collect its X.509 Certificate Chain by obtaining the Trust Anchor's self-signed X.509 Certificate, which is included within the Entity Configuration's ``jwks`` object, and by aggregating all the ``x5c`` values published by its superior entities, from the Trust Anchor down to its immediate superior. This enables the entity to reconstruct the full certificate chain required for validation and trust establishment within the federation.

**Step 3 - Federation Entity Data Retrieval**: as confirmation of success of the onboarding process, the entity MUST fetch the Subordinate Statement about itself from the immediate Federation Authority using the ``/fetch`` endpoint as defined in :ref:`trust-infrastructure:Federation API endpoints`.

In this way, the entity receives a X.509 Certificate Chain(s) within ``jwks`` where:

  - The first element is the X.509 Certificate containing the Federation Entity Key (issued by the Federation Authority).
  - **For Trust Anchor onboarding**: The second element is the Trust Anchor's self-signed X.509 Certificate for validating the first X.509 Certificate.
  - **For Intermediate onboarding**: Additional elements include the Intermediate's X.509 Certificate and the Trust Anchor's self-signed Certificate, forming a complete X.509 X.509 Certificate chain.
  - All X.509 Certificates are expressed in DER format and encoded in Base64.

Example X.509 X.509 Certificate chain within ``jwks`` claim:

.. code-block:: json

 {
    "keys": [
      {
        "crv": "P-256",
        "kty": "EC",
        "x": "qrJrj3Af_B57sbOIRrcBM7br7wOc8ynj7lHFPTeffUk",
        "y": "1H0cWDyGgvU8w-kPKU_xycOCUNT2o0bwslIQtnPU6iM",
        "kid": "5t5YYpBhN-EgIEEI5iUzr6r0MR02LnVQ0OmekmNKcjY",
		    "x5c": ["MIIDqjCCA1GgAwIBAgIGAZc6/V9qMAoGCCqGSM49BAMCMIGzMQsw...", "MIIDQzCCAuigAwIBAgIGAZc6+XlDMAoGCCqGSM49BAMCMIGzMQsw..."]
      }
    ]
  }

Example fetch request:

.. code-block:: http

    GET /fetch?sub=https%3A%2F%2Fcredentials.example.gov HTTP/1.1
    Host: trust-anchor.example.gov

.. note::
   If the ``/fetch`` endpoint responds with status code set to ``400`` or ``404``, the entity MUST resolve the issues described in the response message, before calling the fetch endpoint again. 

Furthermore, the entity can retrieve Trust Marks through Trust Mark Endpoint as defined in :ref:`trust-infrastructure:Federation API endpoints`.

**Step 4: Entity Configuration Update and Onboarding Completion**

Following the fetch request, the **Federation Authority** returns the entity's Subordinate Statement, which is a signed JWT containing:

  - **Entity Metadata**: The entity's validated metadata with applied federation policies.
  - **Trust Information**: Information about the trust relationship between the Federation Authority and the entity, including the issued `x5c` within the `jwk` object about the Subordinate.
  - **Trust Marks**: The Trust Marks issued by the Federation Authority for the entity's specific operational scope and capabilities.

     Example Federation JWK about the Subordinate including the issued X.509 Certificate:

     .. code-block:: json

         {
           "kid": "NsXymfIILEPR5Y0t",
           "kty": "EC",
           "x": "gXY4FApFJCj91Gpb1K9GEIouTq2X3L0K64Iq0ob4l_g",
           "y": "l-6dcrIrFVdrzoY9cRJv9zNuFOR3MsDz6TSDhB0xEo4",
           "crv": "P-256",
           "x5c": [
             "MIIDqjCCA1GgAwIBAgIGAZc6/V9qMAoGCCqGSM49BAMCMIGzMQsw..."
           ]
         }

The Federation Entity MUST complete the onboarding process by:

  1. **Update and Publish the Entity Configuration**:

    The content of ``/.well-known/openid-federation`` endpoint must be updated to include the following claims:

     - Add an ``authority_hints`` claim with a JSON Array containing the **immediate Federation Authority's** Federation Entity Identifier (Trust Anchor for direct onboarding, or Intermediate for mediated onboarding) as defined in :ref:`trust-infrastructure:Federation Roles`.

     - **Integrate Trust Marks**: Include the Trust Marks from the Subordinate Statement in the Entity Configuration using the ``trust_marks`` claim as specified in :ref:`trust-infrastructure:Entity Configuration Leaves and Intermediates`.

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

     Example Trust Marks integration:

     .. code-block:: json

         "trust_marks": [
           {
             "trust_mark_type": "https://trust-anchor.example.gov/trust_marks/federation-entity/credential-issuer",
             "trust_mark": "eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL3RydXN0LWFuY2hvci5leGFtcGxlLmdvdiIsInN1YiI6Imh0dHBzOi8vY3JlZGVudGlhbC1pc3N1ZXIuZXhhbXBsZS5nb3YiLCJ0cnVzdF9tYXJrX3R5cGUiOiJodHRwczovL3RydXN0LWFuY2hvci5leGFtcGxlLmdvdi90cnVzdF9tYXJrcy9mZWRlcmF0aW9uLWVudGl0eS9jcmVkZW50aWFsLWlzc3VlciIsImlhdCI6MTcwMDAwMDAwMCwiZXhwIjoxNzMwMDAwMDAwfQ.abc123signature"
           }
         ]

.. note::
  Federation Entities can obtain Trust Marks anytime needed by using the Trust Mark endpoint exposed by a Trust Mark Issuer as defined in :ref:`trust-infrastructure:Federation API endpoints`.

Upon successful completion of Step 4, the **entity onboarding is successfully completed**. The entity is now operational within the IT-Wallet federation and ready for operational activities.


.. note::
   **Federation Registry Integration**: Upon successful onboarding completion, the entity's Federation Entity Identifier becomes discoverable through the Trust Anchor's entity listing mechanisms (as defined in :ref:`trust-infrastructure:The Infrastructure of Trust`), indicating active federation participation. The entity becomes part of the federation infrastructure detailed in :ref:`registry:Registry Infrastructure`.

IT-Wallet Federation Trust Marks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Federation Entities receive IT-Wallet Federation Trust Marks during successful onboarding completion. **Trust Marks are issued by the Federation Authority** (Trust Anchor for direct onboarding, Intermediate for mediated onboarding) through the Federation Trust Mark Endpoint and serve as verifiable attestations about compliance with IT-Wallet technical profiles and or authorization policies.

Trust Mark Types and Schema
"""""""""""""""""""""""""""

Entities MAY receive multiple Trust Marks for different purposes. Trust Mark identifiers MUST follow a hierarchical schema that reflects the authorization scope:

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
     - **REQUIRED**. Federation Entity Identifier of the subject.
   * - **trust_mark_type**
     - **REQUIRED**. Unique Trust Mark identifier, MUST match the ``trust_mark_type`` claim.
   * - **iat**
     - **REQUIRED**. Trust Mark issuance timestamp.
   * - **exp**
     - **REQUIRED**. Trust Mark expiration timestamp.
   * - **organization_type**
     - **REQUIRED**. Entity organization type (``public`` or ``private``).
   * - **vat_number**
     - **RECOMMENDED**. VAT number of the entity (typically for private organizations).
   * - **legal_identifier**
     - **RECOMMENDED**. Legal registration number or identifier of the entity (e.g., business registration number, tax code).
   * - **ipa_code**
     - **RECOMMENDED**. IPA (Indice delle Pubbliche Amministrazioni) code for public sector entities.
   * - **organization_name**
     - **RECOMMENDED**. Full name of the Organizational Entity.
   * - **email**
     - **RECOMMENDED**. Institutional or PEC email of the organization.
   * - **logo_uri**
     - **REQUIRED**. URL pointing to the :ref:`brand-identity:Trust Mark` for UI/UX purposes.
   * - **ref**
     - **OPTIONAL**. URL with additional web information about the Trust Mark.

The following non-normative examples illustrate different Trust Mark JWT contents for federation membership and different authorization policies:

.. code-block:: json

   {
     "iss": "https://trust-anchor.eid-wallet.example.it",
     "sub": "https://ci.public-authority.gov.example",
     "trust_mark_type": "https://trust-anchor.eid-wallet.example.it/trust_marks/federation-entity/credential-issuer",
     "iat": 1718207217,
     "exp": 1749743216,
     "organization_type": "public",
     "ipa_code": "pub_001",
     "legal_identifier": "12345678901",
     "organization_name": "Public Authority Services",
     "email": "registry@public-authority.gov.example"
   }

.. code-block:: json

   {
     "iss": "https://trust-anchor.eid-wallet.example.it",
     "sub": "https://rental.cars.example.com",
     "trust_mark_type": "https://trust-anchor.eid-wallet.example.it/trust_marks/authorization_policy/relying-party",
     "iat": 1718207217,
     "exp": 1749743216,
     "organization_type": "private",
     "vat_number": "IT12345678901",
     "legal_identifier": "12345678901",
     "organization_name": "Premium Car Rental Services Ltd",
     "email": "compliance@rental.cars.example.com",
     "authorized_claims": ["given_name", "family_name", "driving_privileges"],
     "authorized_credential_types": ["mobile-driving-license"],
     "scope_restrictions": {
       "domains": ["MOBILITY_TRAVEL"],
       "purposes": ["DRIVING_RIGHTS_VERIFICATION"]
     }
   }

.. code-block:: json

   {
     "iss": "https://trust-anchor.eid-wallet.example.it",
     "sub": "https://private-badge.ci.example.com",
     "trust_mark_type": "https://trust-anchor.eid-wallet.example.it/trust_marks/authorization_policy/credential-issuer",
     "iat": 1718207217,
     "exp": 1749743216,
     "organization_type": "private",
     "vat_number": "IT98765432101",
     "legal_identifier": "98765432101",
     "organization_name": "Badge Services Ltd",
     "email": "compliance@rprivate-badge.ci.example.com",
     "authorized_claims": ["given_name", "family_name", "company_id"],
     "authorized_credential_types": ["example-company-badge"],
     "scope_restrictions": {
       "domains": ["EMPLOYMENT"],
       "purposes": ["ACCESS_PERMIT"]
     }
   }

Federation Entities MUST integrate Trust Marks in their Entity Configuration using the ``trust_marks`` claim as specified in :ref:`trust-infrastructure:Entity Configuration Leaves and Intermediates`. Entities MAY receive multiple Trust Marks for different authorization scopes.

.. code-block:: json

   {
     "iss": "https://credentials.example.gov",
     "sub": "https://credentials.example.gov",
     "jwks": { 
      // jwks content
     },
     "authority_hints": ["https://trust-anchor.eid-wallet.example.it"],
     "trust_marks": [
       {
         "trust_mark_type": "https://trust-anchor.eid-wallet.example.it/trust_marks/federation-entity/credential-issuer",
         "trust_mark": "eyJhbGciOiJFUzI1NiIsImtpZCI6IlRydXN0QW5jaG9yS2V5SWQiLCJ0eXAiOiJKV1QifQ..."
       }
     ],
     "metadata": { 
      // Metadata content
     }
   }

.. code-block:: json

   {
     "iss": "https://healthcare-ci.example.gov",
     "sub": "https://healthcare-ci.example.gov",
     "jwks": { 
      // jwks content
     },
     "authority_hints": ["https://healthcare.intermediate.eid-wallet.example.it"],
     "trust_marks": [
       {
         "trust_mark_type": "https://healthcare.intermediate.eid-wallet.example.it/trust_marks/federation-entity/credential-issuer",
         "trust_mark": "eyJhbGciOiJFUzI1NiIsImtpZCI6IkhlYWx0aGNhcmVJbnRlcm1lZGlhdGVLZXlJZCIsInR5cCI6IkpXVCJ9..."
       }
     ],
     "metadata": { 
      // Metadata content  
    }
   }

Trust Mark Validation
"""""""""""""""""""""

Federation participants validate Trust Mark status through two mechanisms:

1. **Static Validation**: Cryptographic verification using the issuing Federation Authority's public key from the Trust Chain.
2. **Dynamic Validation**: Real-time status verification, against any revocations, using the Federation Authority's ``/trust_mark_status`` endpoint as defined in :ref:`trust-infrastructure:Federation API endpoints`.

For comprehensive X.509 Certificate management procedures, including chain validation, revocation verification, and lifecycle management, see :ref:`x5c-evaluation:X.509 Certificate Management Operations`.



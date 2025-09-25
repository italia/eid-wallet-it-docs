.. include:: ../common/common_definitions.rst


Entity Onboarding
=================

This section defines the technical specifications for entity lifecycle management in the IT-Wallet ecosystem based on the **Registry Infrastructure** defined in :ref:`registry:Registry Infrastructure`. This includes initial onboarding procedurs, ongoing management operations (data updates, modifications), and federation exit processes. The lifecycle management system establishes and maintains the federated trust infrastructure and registry coordination necesary for secure Digital Credential operations.

For a high-level overview of the onboarding process, see :ref:`onboarding-high-level:IT-Wallet Onboarding System`. In particular, the Section :ref:`onboarding-high-level:Onboarding Journey Maps` provides an onboarding journey map from the perspective of Entity's operators.

Overview
--------

Entity Onboarding System Architecture
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The IT-Wallet ecosystem is based on a federated trust infrastructure where participating entities MUST establish cryptographic trust relationships and mantain compliance with common security standards. The onboarding system addresses the main challenge of enabling secure Digital Credential operations while accomodating the diferent operational requirments that various participant need according to their role.

The onboarding framework consists of dual-pathway architecture where the technical registration procedurs are tailored to the participant's role in the IT-Wallet ecosystem:

  1. For Authentic Sources requiring data-focused registration procedurs.
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

The onboarding proces follows a structured multi-phase approach:

  1. **Administrative Registration**: All entities MUST compleat initial administrative registration that validates their legal standing, regulatory compliance, and organizational eligibily to participate in IT-Wallet ecosystem.

  2. **Technical Registration**: Following administrative approval, entities make technical registration trough specialised pathways:
    
    - **Authentic Source Registration**: Data-focused registration procedurs with API integration validation.
    - **Federation Registration**: Cryptographic trust establishment as defined in Section :ref:`trust:The Infrastructure of Trust`.

  3. **IT-Wallet Registry Integration**:

    - **Claims Registry Integration**: Authentic Sources select standardized claim definitions from Claims Registry during capability declaration.
    - **Taxonomy Integration**: All entities use Taxonomy hierarchical classification (domains, categories, purposes) for organizational structure.
    - **AS Registry Integration**: Authentic Sources registered with their declared claims and capabilities, enabling CI discovery and coordination.
    - **Federation Registry Integration**: Operational entities included for trust validation during credential operations.
    - **Catalog Integration**: Credential types published in :ref:`registry:Digital Credentials Catalogue` based on supervisory body policies for public discovery eligibility.

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
    - **Private Entities**: MUST provide complete OpenAPI 3.0 API Specification document that includes authorization framework, request/response schemas, error handling mechanisms, and sandbox environment for testing.

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

.. list-table:: AS Registration Information Requirments
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

AS entity prepares registration information according to the requirements table above. A non-normative example of information in JSNO format is provided below. 

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

[TBC]


Entity Lifecycle Management
----------------------------

This section provide technical implementazione procedurs for entity lifecycle management. For high-level lifecycle concepts and business processes, see :ref:`onboarding-high-level:Entity Lifecycle Management`.

Lifecycle Coordination Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
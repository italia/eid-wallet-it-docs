.. include:: ../common/common_definitions.rst


Onboarding System
============================

The IT-Wallet ecosystem operates as a federated trust infrastructure where participants establish trust relationships and maintain compliance with common security standards.

The onboarding system MUST enable secure Digital Credential operations. At the same time, it MUST accommodate the diverse operational requirements that different participants require.

Administrative processes for organizational entities are common to all participants and independent of their technical functions within the ecosystem. However, technical registration processes MUST account for distinct operational roles.

Credential Issuers, Relying Parties, and Wallet Instances (registered indirectly through Wallet Providers) participate directly in Credential issuance and verification operations. These entities require cryptographic trust establishment through federation protocols.

Authentic Sources provide authoritative data through direct trust relationships with Credential Issuers. They serve a central role in data discovery and availability, requiring specialized data-focused registration procedures.

Onboarding System Architecture
------------------------------

The onboarding framework MUST provide specialized onboarding processes that match the operational characteristics and regulatory obligations of different participant types.

.. plantuml:: plantuml/trust-infrastructure-overview.puml
    :width: 99%
    :alt: IT-Wallet onboarding system overview showing dual-path registration processes and trust infrastructure
    :caption: `IT-Wallet Onboarding System Overview. <https://www.plantuml.com/plantuml/svg/hLL_RnCv4Fr_FyLSE954eir1MbJGWSYb0I8LDKe25H9IDB4d6qkElRAzoOKJt_titUtYP0la3o9Lwevddj-y-U4trg5n-KQ2CxbrPqAj35h_FtEveJEz9RCLj4l-48h9d1FyFRpe3IyMGxt9j2BbNYVlnzUZnMm-cevkvvydequtQTyCFjz-d2zkHc_dY-dutVkvDoPjkAQLK0IpoNGy7yqYJ9Tdo4s_jzBAdU6EhDxGsMMFaN5Y9HWwUlrhRuuEbsXFSMKwjIUu2RvWQFW9dZkKajol77j2MITSxeHMhuCWGo-vte1rUqas6N0-ahGXvUQOTbhqhoEZKBQUm9_BTAYbDgzQZruKls0Bo9LrjnQE2ZzjE9dAcXhQjxh7i9aH6pJxGzIdJvzVBVb9g8_-MbvSNLqqWHsnzI7gSxRizrUdeLxWLV_PYoPg6bfGeM9qY7qrwB-uUdiQzkNbi_xbm6CdJZX9C9wVtHK5Wrkrr6YuK2dCzjRH1cwhZW_bcPHImO0vRMpoZyuLzz-TIi8dq3hqQ7bBg_jV0lutzAnGA38TjDuyoDsQb1CCPZetZ0hVQtJeBz5RmQcCVbTa6v87GwcmpWZouPdHAx9MQ8KIj4bHYQyOkiYV4SyPkl8ewYyRP72OsbTrOQpdxUXLwtvGMjqZfYRp5AOazq6F2HedIfv3GpoGHmcVoFY9hDZUnanW6uwAK2vIuRmpg-CihBG16wHb1CWOsOXWfMVCCKneWzykyAig5ybMssPQLhato6N1FTGvAZvccHIiSd0Qc73YAwcV4oidlK6DYKETnjRcP8xLcvK2FC1FUFyVIHTgnK4hGDz4sjFmCLk2KCQVKgtML-Zxv5l1jmrLwcDbNPWfw0Z5XI7coltVK3oaTHGJo7_GIo6fTqTB66HPaMKfNfr0gPE5dN1hEBm4tDheF5t3tQJc7ssxfjPX5kT5vFZWUVe-aGNkGeHJp-KXtuTdKzVplx3xCAUDXH3YfkKe5gKwgE47L9YIXL0fjmSJ-w7YLRfa7IwbiEimrtNoF4Tvbg5RXzuCyq1HuqLRBz8Z6k-g0O_IMH6dylf5nIKigRUr5QQLjLMh55lk_mUzWWgAU9cS80kTwUG9tFc_uRZhhJwd89FEAd2KLRvRb88Nff-sP_IwFvmDsZYBmGngVeyX6geXEfGw3GaS9z7OkaLLS8j2UlOKJHcuVKRbbkB2iY3__gGD-YtnlpOyFOS1tmWLhYx7yw1fEYXbBMGtcPBy_eWqUh21zKN5O2796qfHzhmwkKIdVRAOXGtdn-TNuC_EOUwpKOAXREBMHpscDvaKeGDZx7O0Dzdl9bq1xtu_C9J8JFn-oacrKdrZJj2jYwzmr_4zXstSn_FxY9TVr3KwXEDBXyTT-HWiMzC6RJmdROZcEi01_932mtkXlpoFCIfAvLeOnJihaFe--n0DhYsNS_-y-R3SJM1Jh4VUJUwBMpmd5zvvV93q5nLxXzl61mz6k0HkSB-OXjvZebj-VGnbtMNrbxyXqZesxqIWMK74RqKr9rr_U1ljiO_MCqdQIZk2i0hY6hw4rlNzXl1o7HUh5OSrTG_XfSAVwYtfKQ8oL5l20oLlIF5y8_y7>`_

All Primary Actors MUST undergo administrative registration for legal and regulatory compliance, followed by specialized technical registration processes that MUST reflect their operational roles in the Digital Credential ecosystem.

    1. **Administrative Registration**: All entities (Authentic Sources, Relying Parties, Wallet Providers, Credential Issuers) MUST complete initial administrative registration that validates their legal standing, regulatory compliance, and organizational eligibility to participate in the IT-Wallet ecosystem.

    2. **Technical Registration**: Following administrative approval, entities complete technical registration through specialized pathways:

        a. **Authentic Sources**: Declare their available claims from the Claims Registry and specify intended verification purposes and organization type (public or private). 

        b. **Credential Issuers**: Select Authentic Sources based on required claims, request integration approval (except for regulatory mandates), and register Credential types with automatic catalog publication per Supervisory Body policy.

        c. **Other Federation Entities** (Relying Parties, Wallet Providers): Undergo federation-based registration for cryptographic trust establishment.

    3. **IT-Wallet Registry Integration**:

        a. **Claims Registry and Taxonomy Integration**: Claims Registry provides standardized data definitions for individual Credential attributes, while Taxonomy defines hierarchical classification (domains, classes, purposes) that are then referenced in the Digital Credentials Catalog for specific Credential implementations. All participants leverage these registries for capability declarations and issuance/verification requirements.

        b. **AS Registry Integration**: Authentic Sources registered with their declared claims and capability, enabling CI discovery and coordination.

        c. **Federation Registry Integration**: Operational entities included for trust validation during Credential operations.

        d. **Catalog Integration**: Credential types automatically published in :ref:`registry:Digital Credentials Catalog` based on Supervisory Body policies for public discovery eligibility.

    4. **Wallet Instance Registration**: Wallet Instances are registered indirectly through Wallet Providers, establishing user-level Credential management capabilities. Technical details are provided in :ref:`wallet-instance-registration:Wallet Instance Initialization and Registration`.

Authentic Source Registration Process
---------------------------------------

Authentic Source registration allows data providers to establish their authoritative role in the Digital Credential ecosystem through the registration of their data capabilities and standardized access mechanisms based on the Claims Registry and Taxonomy classifications.

Authentic Source entities MUST undergo registration procedures that validate their data authority, declare their available claims from the standardized Claims Registry, and establish technical integration mechanisms. Authentic Source entities specify intended use cases (formally ``purposes``) that determine catalog eligibility per Supervisory Body policies. 

Public Authentic Sources MUST leverage PDND integration to provide government data through standardized national infrastructure.

Private Authentic Sources MAY establish custom service interfaces that accommodate specific organizational or regulatory requirements. 

Both pathways MUST assure data quality standards and establish audit trails for all data provisioning activities.

**AS-CI Coordination Process**: Following AS registration, Credential Issuers identify suitable AS entities through the AS Registry and request integration authorization during the administrative registration phase. For regulatory mandates, authorization MUST be automatic. Otherwise, Authentic Sources entities evaluate and authorize Credential Issuers requests based on business and technical criteria. Following administrative authorization, technical integration procedures establish the operational data access relationships before Credential type catalog publication.

Successfully registered Authentic Sources MUST be included in the AS Registry with their declared claims and capability. Credential types MUST become publicly discoverable in the :ref:`registry:Digital Credentials Catalog` only after successful AS-CI integration and Supervisory Body policy approval for catalog eligibility.

Technical implementation procedures for Authentic Source registration are provided in :ref:`entity-onboarding:Authentic Sources Registration Process`.


Federation Onboarding Process
-------------------------------

Federation onboarding establishes the trust relationships and compliance frameworks that enable operational entities to participate in secure Credential lifecycle activities.
Operational entities MUST complete onboarding that includes administrative eligibility verification, technical infrastructure validation, and trust establishment. The onboarding process creates cryptographic trust relationships through certificate issuance, trust chain evaluation, and compliance attestation. These mechanisms enable secure interactions among federation participants and provide the foundation for distributed trust validation across the ecosystem.

Successfully onboarded entities are included in the Federation Registry, which maintains the authoritative list of trusted federation participants. This registry enables operational trust validation during Credential lifecycle activities.

Relying Parties MUST verify Digital Credentials with cryptographic assurance, Wallet Providers MUST provide trusted digital wallet services to citizens, and Credential Issuers MUST issue Digital Credentials using authoritative data sources. All operations MUST occur within established trust relationships that assure security and auditability.

Entity Lifecycle Management
---------------------------

Following successful onboarding, entities require ongoing lifecycle management to maintain operational status and compliance within the IT-Wallet ecosystem. Lifecycle management encompasses administrative updates, technical modifications, and federation exit processes that accommodate changing organizational and operational requirements.

Ongoing Operations Management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Entities MUST maintain current administrative and technical information to ensure federation participation and compliance.

**Administrative Updates**

Organizations MAY update administrative information through standard registry channels, such as:

    - **Legal Entity Changes**: Company name changes, organizational restructuring, legal status modifications.
    - **Contact Information**: Updates to official contact channels and responsible personnel.
    - **Regulatory Status**: Changes in licenses, certifications, or regulatory compliance status.
    - **Service Scope**: Modifications to service offerings or user base characteristics.

Administrative updates MUST follow standard governance processes and SHOULD NOT affect technical federation operations.

**Technical Configuration Management**

Technical updates affecting federation protocol operations require coordinated procedures, including:

    - **Certificate Management**: Regular certificate renewal, emergency replacement, revocation handling.
    - **Infrastructure Changes**: Endpoint updates, service migrations, capacity modifications.
    - **Compliance Updates**: Security standard updates, policy changes, audit requirements.
    - **Capability Modifications**: Adding or removing supported protocols, Credential types, or service features.

Technical updates MUST be validated by the Supervisory Body to maintain federation trust relationships and operational integrity.

Federation Exit and Removal Processes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Entities MAY exit the federation voluntarily or be removed by the Supervisory Body for compliance or security reasons.

**Voluntary Federation Exit** - Organizations MAY choose to exit the federation for business or operational reasons, including:

    - **Business Changes**: Organizational restructuring or service discontinuation.
    - **Technical Migration**: Moving to alternative technical solutions or providers.
    - **Regulatory Changes**: Changes in regulatory environment or compliance requirements.

Voluntary exit MUST require coordination with dependent entities and proper handling of existing Credentials and user relationships.

**Supervisory Body Removal** - Supervisory Body MAY initiate entity removal for:

    - **Compliance Violations**: Failure to maintain regulatory compliance or federation policy adherence.
    - **Security Incidents**: Compromise of security infrastructure or failure to maintain security standards.
    - **Operational Failures**: Persistent technical failures that affect federation security.
    - **Policy Violations**: Violations of federation operational policies or agreements.

Removal processes MAY include investigations, remediations, and appeal procedures where appropriate.

.. warning::

    For critical security incidents or immediate threats to federation integrity, the Supervisory Body MAY implement emergency suspension with immediate effect. 

Lifecycle Coordination Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Lifecycle management in the IT-Wallet ecosystem needs coordination between multiple participants to keep operations working and maintain trust relationships. The coordination framework covers three main areas:

    - **Stakeholder communication:** When entities need to make changes that impact IT-Wallet ecosystem operations, they MUST inform the Supervisory Body and relevant federation participants in advance.
    - **Registry synchronization:** When one entity makes changes that affect other entities, all registry systems MUST be properly updated ensuring that all changes are logged securely with timestamps and reasons.
    - **Business continuity assurance:** Entities SHOULD balance between making necessary updates and keeping their obligations to users and regulations. This includes ensuring that the service is as available as possible, handling personal data correctly during changes, and staying compliant with legal requirements even in emergency situations.

Technical procedures and specific compliance requirements for lifecycle management are detailed in the Section :ref:`entity-onboarding:Entity Onboarding`.

Onboarding Journey Maps
-------------------------------

The following journey maps provide a detailed view of the onboarding experience from the perspective of each entity type and their operators. These visual representations help organizations understand the specific steps, requirements, and interactions they will encounter during their onboarding process.

Each journey map shows the complete process from initial planning to final registry integration, highlighting critical touchpoints with the Supervisory Body and dependencies between different entity onboarding processes.

Ecosystem Overview
^^^^^^^^^^^^^^^^^^

.. figure:: ./images/svg/overview-onboarding-journey.svg
    :width: 100%
    :alt: IT-Wallet ecosystem onboarding overview
    :name: onboarding-overview

    Complete ecosystem onboarding showing the main processes

The IT-Wallet Registry system coordinates all registrations through five main components:

    1. **Claims Registry** for standardized semantic definitions of individual Credential attributes.
    2. **AS Registry** for data sources and capabilities.
    3. **Federation Registry** for operational trust relationships.
    4. **Digital Credentials Catalog** (see :ref:`registry:Digital Credentials Catalog`) for Credential type discovery.
    5. **Taxonomy** for hierarchical classification organizing Credentials by domain and purpose.

The following journey maps illustrate two distinct Credential scenarios:

    - **Public Catalog Scenario**: Mobile Driving License (mDL) provided for a public discovery via Credential Catalog.
    - **Private Credential Scenario**: Corporate Employee Badge from Company (Private AS, and therefore provided for discovery via Credential Offer only).

Authentic Source Operator Journey
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

From the Authentic Source operator perspective, the onboarding process begins with evaluating existing data capabilities against the standardized Claims Registry and Taxonomy classifications, determining which user attributes can be made available as a Digital Credential. The operator submits a registration request to the Supervisory Body, declaring specific claims from the Claims Registry with the Taxonomy domains and intended purposes.

**Example - Public Authentic Source (mDL Scenario)**:

    - **Claims Declaration**: Selects standardized claims (``given_name``, ``family_name``, ``driving_privileges``, etc. ) from Claims Registry.
    - **Taxonomy Classification**: Domain ``MOBILITY_TRAVEL``, Purpose ``DRIVING_RIGHTS``.
    - **Use Case**: Public service - driving authorization verification (eligible for Credential Catalog).
    - **Integration**: e-Service PDNDintegration following government standards (see :ref:`e-service-pdnd:e-Service PDND`).
    - **Catalog Outcome**: mDL becomes publicly discoverable after CI integration.

**Example - Corporate AS (Employee Badge Scenario)**:

    - **Claims Declaration**: Selects claims (``given_name``, ``family_name``, ``employee.job_title``, etc.) from Claims Registry.
    - **Taxonomy Classification**: Domain ``MEMBERSHIP``, Purpose ``ASSOCIATION``.
    - **Use Case**: Private corporate access control (non-eligible for Credential Catalog).
    - **Integration**: Custom API for Credential Issuer integration.
    - **Catalog Outcome**: Badge remains private, available only via Credential Offer.

Critical phases include administrative verification by the Supervisory Body (which involves regulatory compliance checks outside the technical scope) and technical validation. The process concludes with registration in the AS Registry, making the declared claims discoverable by Credential Issuers for integration requests. The integration requests can be also send by the Authentic Sources to a specific Credential Issuers.
 
.. warning::

    **Important dependency**: Declared claims in AS Registry remain unavailable to end users until a Credential Issuer completes registration, integration approval, and technical implementation. Catalog publication depends on Supervisory Body policies for public discovery eligibility.

Credential Issuer Operator Journey  
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Credential Issuer operators start by discovering available Authentic Source entities through the AS Registry and evaluating integration feasibility based on required claims. The registration request specifies which Credential types they intend to issue, select appropriate Authentic Source entities, and demonstrate technical capability to access the required data sources. Alternatively, the Credential Issuer operators receive directly the integration request by the Authentic Source.

**Example - mDL (Public Scenario)**:

    - **AS Discovery** or **AS Integration Request**: Identifies the Authentic Source providing mDL attributes in AS Registry with required driving license claims. Alternatively, Credential Issuer receives the integration request directly by mDL Authentic Source.
    - **Integration Request**: Automatic approval due to regulatory mandate. 
    - **Technical Setup**: e-Service PDNDintegration following government standards (see :ref:`e-service-pdnd:e-Service PDND`).
    - **Catalog Publication**: mDL automatically published in the Credential Catalog.
    - **User Access**: Citizens discover mDL through a public catalog in Wallet.

**Example - CI for Employee Badge (Private Scenario)**:

    - **AS Discovery** or **AS Integration Request**: Identifies the Authentic Source in AS Registry with employee access claims. Alternatively, Credential Issuer receives the integration request by the Authentic Source.
    - **Integration Request**: Requires recipient approval.
    - **Technical Setup**: Custom API integration with authentication.
    - **Catalog Publication**: Badge excluded from public catalog per supervisory policy.
    - **User Access**: Employees receive badges only via direct Credential Offer from company systems.

The technical setup phase offers two distinct integration pathways depending on the Authentic Source type:

    - **Public AS Integration**: Uses the PDND platform for accessing government data through standardized APIs.
    - **Private AS Integration**: Establishes direct API connections with custom endpoints provided by private organizations.

Following successful integration testing and Authentic Source approval, the Credential Issuer is registered in the Federation Registry as a trusted Entity, enabling actual Credential issuance to end-users. 

.. warning::

    This step activates Credential availability for end-users. Public Credentials become discoverable through the catalog, while other Credentials remain available only via direct Credential Offers.

Wallet Provider Operator Journey
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Wallet Provider operators follow an independent onboarding path that focuses on application certification and security validation. The process highlights the development and certification of wallet applications that can securely store and manage Digital Credentials for citizens.

A key technical requirement involves implementing Wallet integrity and authenticity check mechanisms. These checks enable the Wallet to obtain a Wallet App Attestation, which serves as proof of the Wallet's security and compliance status during Credential operations.

The certification process includes security evaluation, covering wallet architecture, data protection mechanisms, and user privacy features. Successfully certified wallet providers are registered in the Federation Registry and can distribute their applications through app stores.

Relying Party Operator Journey
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^  

Relying Party operators begin by identifying which EAA types are required for their specific services and evaluating integration complexity with existing authentication systems. The registration request provides evidence of legitimate needs for accessing specific Credential types and User attributes, outlining the intended service use cases and organizational characteristics that justify Credential access.

**Example - Car Rental Service (Private RP)**:

    - **Business Classification**: ATECO code 77.11 (car rental services).
    - **Authorization Request**: Driving authorization verification for rental eligibility.
    - **Claims Requirements**: ``given_name``, ``family_name``, ``driving_privileges``, etc., from mDL.
    - **Use Case Justification**: Legal obligation to verify valid driving license before vehicle rental.
    - **Authorization Scope**: Granted access to ``MOBILITY_TRAVEL`` domain, ``DRIVING_RIGHTS`` purpose.

**Example - Municipal Services (Public RP)**:

    - **Organization Type**: Public Administration with IPA code requirement.
    - **Authorization Request**: Citizen identity verification for municipal services access.
    - **Claims Requirements**: ``given_name``, ``family_name``, ``tax_id_code`` from PID.
    - **Use Case Justification**: Public service delivery requiring citizen identification.
    - **Authorization Scope**: Granted broader access reflecting public service mandate.

**Example - Corporate Access Control (Private RP)**:

    - **Business Classification**: ATECO code 62.01 (computer programming activities).
    - **Authorization Request**: Employee verification for corporate facility access.
    - **Claims Requirements**: ``given_name``, ``family_name``, ``employee.job_title`` from Corporate Employee Badge.
    - **Use Case Justification**: Workplace security requiring employee identification and access control.
    - **Authorization Scope**: Granted access to ``MEMBERSHIP`` domain, ``ASSOCIATION`` purpose.
    - **Credential Discovery**: Badge available only via private Credential Offer (non-eligible for Credential Catalog).


Technical integration focuses on developing authentication flows that can verify Digital Credentials presented by Users. This includes implementing cryptographic verification mechanisms and establishing secure communication channels with the federation infrastructure.

Service authorization by the Supervisory Body MUST involve policy-based evaluation that considers organizational type (private vs public administration), business sector classification, and legitimate service requirements. The authorization process grants specific operational scopes that define which Credential domains and purposes the Relying Party can request. Following approval, the Relying Party is registered in the Federation Registry with clearly defined authorization boundaries for Digital Credentials and User's attributes acceptance.


User Experience Journey
-------------------------------

When all entity onboarding processes are successfully completed, Users can discover and install certified Wallet Instances, obtain available Digital Credentials and present their Digital Credentials to registered Relying Parties (see :ref:`functionalities:Functionalities Overview`). 

This seamless integration depends on all relevant entities having completed their respective onboarding journeys.

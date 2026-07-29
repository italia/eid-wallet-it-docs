.. include:: ../common/common_definitions.rst
.. Included via onboarding-system.rst at title level '-' (level 1).

Registration Model
------------------

This section provides the static view of the registration with the aim of defining the information each entity has to provide, which conditions it has to meet and which artifacts and registry entries it obtains. It is organized as a common part and a profile for each role.

Registration Data Model
^^^^^^^^^^^^^^^^^^^^^^^

This section defines the complete set of the data the entities provide to the Onboarding System, with its semantics and, where applicable, its normative reference.

Depending on the role, the data is then encoded in a different data model, the ``WalletRelyingParty`` schema of the Register for a Wallet-Relying Party (:ref:`infrastructure-trust:Register of WRPs`), the entry of the AS Registry for an Authentic Source (:ref:`registry:Authentic Source Registry`), the Digital Credentials Catalog for the Credential types (:ref:`registry:Digital Credentials Catalog`), and the notification dataset for a Wallet Provider.

The table below is the reference catalog of the data, identified by a format-agnostic **Data Identifier**.
A Data Identifier can group a set of detailed fields of a destination data model that are semantically close and are provided together, in which case the Description lists the fields it provides.
Each :ref:`onboarding-system:Registration Profiles` is an instance of this catalog, that states which Data Identifiers are required for a role and how the entity valorizes them.

.. list-table:: Registration Data Model
   :class: longtable
   :widths: 22 50 28
   :header-rows: 1

   * - **Data Identifier**
     - **Description**
     - **Normative reference**
   * - `legal_name`
     - The name of the organization as it appears in the official records. In the Register it is the ``legalName``, in the AS Registry the ``organization_name_l10n_id``.
     - [`CIR2025/848`_], Annex I
   * - `identifier`
     - One or more official identifiers of the organization. Within IT-Wallet the Value Added Tax Identification Number (VATIN) is required for every entity, and a public body additionally provides its national identifier of type ``NTR``, valued with its IPA code, that is the code of the Italian Index of Public Administrations. The other identifier types of Table 2, such as EUID and LEI, are optional and are not supported in the current version. The syntax of the ``organizationIdentifier`` is defined in clause 5.1.4 of [`ETSI EN 319 412-1`_].
     - [`ETSI TS 119 475`_], Table 2
   * - `legal_nature`
     - Whether the entity is a public sector body or a private entity. In the Register it is the ``isPSB`` flag, in the AS Registry the ``organization_type``.
     - [`CIR2025/848`_], Annex I
   * - `contact_information`
     - The postal address, the information web page and the contacts of the organization. The contacts include at least an institutional contact for the administrative communications, for which a certified electronic mail address (PEC) is RECOMMENDED, and a technical contact for the user support of the service. In the Register the support contact is the ``supportURI`` field.
     - [`CIR2025/848`_], Annex I
   * - `service_policies`
     - The terms and conditions and the privacy policy of the service, each published at its own URL.
     - [`CIR2025/848`_], Annex I
   * - `data_protection_authority`
     - The authority competent for the supervision of the entity under the data-protection law, with the contact information the Users employ to report suspicious actions. In the Register it is the ``supervisoryAuthority`` field (:ref:`infrastructure-trust:Register of WRPs`), in the AS Registry the ``dpa_contact``.
     - Regulation (EU) 2016/679, Article 46a
   * - `entitlements`
     - The entitlements the entity requests, which state the roles it intends to play in the ecosystem and which drive the role-specific information below.
     - [`ETSI TS 119 475`_], Annex A.2
   * - `service_description`
     - The user-facing trade name and the localized description of the service, provided by the entities that offer a service to the Wallet Units, so that the User can recognize the entity.
     - [`CIR2025/848`_], Annex I
   * - `intended_use`
     - The attributes a Relying Party intends to request from the Wallet Units. Provided by the entities that request attributes from the Wallet Units.
     - [`CIR2025/848`_], Annex I
   * - `provided_attestations`
     - The attestation types an Attestation Provider intends to issue. It is declared through the Credential type declaration, that anchors each type to its Rulebook and creates or matches the versioned entry of the Digital Credentials Catalog, see :ref:`registry:Digital Credentials Catalog`.
     - [`CIR2025/848`_], Annex I
   * - `intermediary_relationship`
     - For a Relying Party Intermediary, the declaration that it acts as an intermediary. For an intermediated Relying Party, the reference to the Intermediary it uses.
     - [`ETSI TS 119 475`_], Table 10
   * - `federation_entity_identifier`
     - The identifier of the entity in the National Trust Framework, that is the ``iss`` and ``sub`` of its Entity Configuration. Provided by every Federation Entity, that is every entity except an Authentic Source.
     - `OID-FED`_, Section 3
   * - `federation_entity_key`
     - The public key with which the entity signs its federation statements, provided in JWK format. The rest of the federation configuration is published in the Entity Configuration reachable at the ``.well-known/openid-federation`` endpoint.
     - `OID-FED`_, Section 3
   * - `certificate_signing_requests`
     - An array of Certificate Signing Requests in PKCS #10 format, one for each X.509 certificate the entity needs to obtain, that is the WRPAC and, depending on the role, the Sign/Seal Certificate or the National Authentication Certificate. Each request carries the public key to be certified, distinct from the Federation Entity Key.
     - :rfc:`2986`
   * - `provided_claims_purposes`
     - The claims composing an Attestation, selected from the Claims Registry, and the purposes it serves, selected from the Taxonomy, together with the data-provision capabilities. It is stored in the ``data_capabilities`` of the AS Registry entry, that is the ``available_claims``, the ``intended_purposes`` and the related integration details, see :ref:`registry:Authentic Source Registry`.
     - [`CIR2025/848`_], Annex I
   * - `visual_identity`
     - The visual assets of an Authentic Source, that is the logo of the organization and the logo and the background color associated with a provided dataset, each with its integrity digest and its alternative text. It is stored in the ``organization_info`` and in the ``data_capabilities`` of the AS Registry entry, see :ref:`registry:Authentic Source Registry`. The other entities do not provide it, since their visual assets are carried in their Entity Configuration.
     - This specification
   * - `credential_type_declaration`
     - For a Credential Issuer, the Credential types it issues, each anchored to its Rulebook. It creates or matches the versioned entry of the Digital Credentials Catalog and it groups the metadata of the type, that is the Digital Credential Metadata, that is the unique identifier, the User authentication methods and the minimum Level of Assurance, and the reference to the Authentic Sources that provide its data, see :ref:`registry:Digital Credentials Catalog`.
     - [`CIR2025/848`_], Annex I
   * - `credential_technical_specification`
     - Technical definition of a Credential type, that groups the Technical Specification fields of the Digital Credentials Catalog, that is the Credential schemes, the Credential formats and the authentication policy, see :ref:`registry:Digital Credentials Catalog`.
     - [`CIR2025/848`_], Annex I
   * - `credential_policies`
     - Conditions of use of a Credential type, that group the Terms of Use fields of the Digital Credentials Catalog, that is the Credential validity, the restriction policy, the pricing policy and the Credential purposes, see :ref:`registry:Digital Credentials Catalog`.
     - [`CIR2025/848`_], Annex I
   * - `conformity_assessment`
     - The outcome of the conformity assessment of the entity. For a PuB-EAA Provider it is the conformity assessment report issued by a conformity assessment body under Article 45f of [`EIDAS`_]. For a Wallet Provider and a PID Provider it is the assessment performed under the national certification scheme operated by the Italian National Cybersecurity Agency (ACN). Provided by the notified categories.
     - [`EIDAS-ARF`_], Annex 2
   * - `service_supply_point`
     - The URL at which a Wallet Unit starts the process of requesting and obtaining an Attestation from the Issuer. Provided by the notified categories that issue an Attestation requested by the Wallet Unit, that is the PID Providers and the PuB-EAA Providers.
     - [`EIDAS-ARF`_], Annex 2
   * - `signing_trust_anchor`
     - The trust anchor supporting the validation of the Attestations the entity issues, that is the public key and the name. It is provided as an input by the categories whose Sign/Seal Certificate is not issued by the national Root Certification Authority, that is the QEAA Providers and the PuB-EAA Providers, whose Qualified Certification Authority belongs to the perimeter of a Qualified Trust Service Provider, see :ref:`infrastructure-trust:PKI Architecture`. For the other categories the trust anchor derives from the Sign/Seal Certificate issued through the Certificate Signing Requests.
     - [`EIDAS-ARF`_], Annex 2

The table gives the whole set.
A given entity provides only the subset that applies to its role, as defined in :ref:`onboarding-system:Registration Profiles`.

Eligibility and Compliance Preconditions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Before any technical registration, the eligibility and the compliance of an entity MUST be verified by the Supervisory Body, which relies on the Registrar for the entities it registers and, for the notified categories, acts as the national point of contact toward the European Commission.
Where a national and an EUDIW obligation overlap, the EUDIW obligation is authoritative.

The verification applies to Authentic Sources, Wallet Providers and Wallet-Relying Parties, and its content depends on the role.

  - **Authentic Sources**: the Supervisory Body validates the legal standing and the data authority of the organization and classifies it as public or private.
    The trust of an Authentic Source is governed by the PDND framework and it is out of EUDIW and National Trust Frameworks.
  - **Wallet Providers**: the eligibility is established and the conformity assessment of the Wallet Solution is driven.
    The assessment covers the security of the wallet architecture, its data-protection mechanisms and its user-privacy features, and it is the precondition for the Wallet Solution to be certified.
    The certification of the Wallet Solution is an external process, and this phase uses its outcome as an input.
    The certification follows the national certification scheme operated by the Italian National Cybersecurity Agency (ACN), and the functional testing follows the EU functional conformity assessment framework (FCAF).
  - **PID Providers**: validated per national designation as providers of Person Identification Data, and subject to the national certification scheme operated by the Italian National Cybersecurity Agency (ACN).
  - **QEAA Providers**: validated through the qualification and the supervision of the issuing Qualified Trust Service Provider.
  - **PuB-EAA Providers**: validated through the conformity assessment required by Article 45f of the eIDAS2 Regulation.
  - **Non-qualified EAA Providers**: validated for the eligibility to issue.
    Their trust anchor is distributed through the National Trust Framework and it is defined in the applicable Attestation Rulebook.
  - **Relying Parties**: the Supervisory Body performs a policy-based authorization, evaluating the organizational type, that is public administration or private entity, the business-sector classification, and the legitimate requirements of the service.
  - **Relying Party Intermediaries**: additionally demonstrate their eligibility to act on behalf of Relying Parties, pursuant to Article 5b(8) of the eIDAS2 Regulation ([`EU_2024_1183`_]).
  
  .. note::
   The Credential Issuer declares the Credential types it intends to issue, each anchored to its Rulebook, and its integration with the relevant Authentic Sources is authorized where needed.

The identity proofing of the Wallet-Relying Parties MUST be carried out by the Registrar according to [`ETSI TS 119 461`_], and the verification of the entitlements MUST follow Annex III of [`CIR2025/848`_].
Within IT-Wallet the identity proofing is applied to every entity that onboards, including the entities that do not operate in the EUDIW Trust Framework, even where it is not strictly required for them.

For the notified entities the certifications are a mandatory input to the onboarding, and in every case the eligibility and compliance verification is a mandatory precondition for the technical registration.


Registration Outcomes
^^^^^^^^^^^^^^^^^^^^^

A successful registration produces, depending on the role and on the scope of operation, the entry in the Register, the Trust Artifacts and the entry in the trusted list.
The way each artifact is produced is described in :ref:`onboarding-system:Onboarding Processes`, and the effects of the later changes in :ref:`onboarding-system:Events, Registries and Trust Artifacts`.

The table shows the artifacts that vary by role, that is the EUDIW artifacts obtained when the entity registers as a Wallet-Relying Party, and the national artifacts of the National Trust Framework.

.. list-table:: Registration Outcomes by Entity Type
   :class: longtable
   :widths: 22 12 10 12 20 24
   :header-rows: 1

   * - **Entity type**
     - **Register record**
     - **WRPAC**
     - **WRPRC**
     - **National X.509 certificate**
     - **LoTE entry**
   * - PID Provider
     - yes
     - yes
     - yes
     - no
     - PID Providers LoTE
   * - QEAA Provider
     - yes
     - yes
     - yes
     - no
     - EUMS TL, referenced in the LOTL
   * - PuB-EAA Provider
     - yes
     - yes
     - yes
     - no
     - PuB-EAA Providers LoTE
   * - Non-qualified EAA Provider
     - yes only if it issues an Attestation published in a EU Rulebook
     - yes only if it issues an Attestation published in a EU Rulebook
     - yes only if it issues an Attestation published in a EU Rulebook
     - Sign/Seal Certificate, for the Attestations anchored to the National Trust Framework
     - None, trust anchor distribution defined in the applicable Attestation Rulebook
   * - Relying Party
     - yes
     - yes
     - yes
     - Authentication Certificate, where the Relying Party operates in the Proximity Flow
     - None
   * - Relying Party Intermediary
     - yes
     - yes
     - No
     - No
     - None
   * - Wallet Provider
     - no
     - no
     - no
     - Sign/Seal Certificate
     - Wallet Providers LoTE

.. note::
   The federation registration is common to every entity and, as a result of it, every entity obtains a Subordinate Statement issued by its Federation Authority, and a registration Trust Mark.

.. note::
   An entity operating only at national level obtains no Register record, no WRPAC and no WRPRC.
   It holds its Entity Statement and its registration Trust Mark from the federation registration, and, where its role requires it, its national certificate, that is the Sign/Seal Certificate for a national Credential Issuer or the Authentication Certificate for a Relying Party operating in the Proximity Flow.

Registration Profiles
^^^^^^^^^^^^^^^^^^^^^

This Section describes the registration of each role as a profile.
An entity can hold more than one entitlement in a single registration record and for more than one role, so the profiles are not mutually exclusive and they compose.
For example, an entity can be at the same time a Relying Party and a QEAA Provider, and in that case its input is the union of the two profiles and its outcome is the union of the two.

PID Provider
""""""""""""

The table below lists the Data Identifiers a PID Provider provides to the Onboarding System.
The semantics of each Data Identifier is defined in :ref:`onboarding-system:Registration Data Model`.

.. list-table:: PID Provider Registration Data
   :class: longtable
   :widths: 34 66
   :header-rows: 1

   * - **Data Identifier**
     - **Values**
   * - `legal_name`
     - The legal name of the PID Provider as it appears in the official records.
   * - `identifier`
     - The VATIN of the PID Provider and its ``NTR`` identifier valued with its IPA code.
   * - `legal_nature`
     - The legal nature of the PID Provider as a public sector body.
   * - `contact_information`
     - The institutional contact (PEC) and the technical support contact of the PID Provider, together with the postal address and the information web page are provided where available.
   * - `service_policies`
     - The terms and conditions and the privacy policy of the PID issuance service.
   * - `service_description`
     - The localized description of the PID issuance service. The user-facing trade name is provided where available.
   * - `data_protection_authority`
     - The Data Protection Authority contact email.
   * - `entitlements`
     - The entitlements that state the PID Provider role, and the additional roles it plays where applicable.
   * - `provided_attestations`
     - The declaration that the PID Provider issues the PID, with the format and the attributes of the PID.
   * - `conformity_assessment`
     - The outcome of the assessment performed under the national certification scheme operated by the Italian National Cybersecurity Agency (ACN).
   * - `service_supply_point`
     - The URL at which a Wallet Unit starts the process of requesting and obtaining the PID.
   * - `credential_type_declaration`
     - The PID type the PID Provider issues, anchored to the PID Rulebook.
   * - `credential_technical_specification`
     - The technical definition of the PID, that is its schemes and its formats, the PID being provided in both the SD-JWT VC and the mdoc-CBOR format.
   * - `credential_policies`
     - The conditions of use of the PID, that is its validity and its purposes.
   * - `federation_entity_identifier`
     - The Federation Entity Identifier of the PID Provider in the National Trust Framework.
   * - `federation_entity_key`
     - The Federation Entity Key of the PID Provider.
   * - `certificate_signing_requests`
     - One Certificate Signing Request for the WRPAC, with which the PID Provider authenticates towards the Wallet Units, and one for the Sign/Seal Certificate, with which it signs the issued PID.


QEAA Provider
"""""""""""""

The table below lists the Data Identifiers a QEAA Provider provides to the Onboarding System.
The semantics of each Data Identifier is defined in :ref:`onboarding-system:Registration Data Model`.

.. list-table:: QEAA Provider Registration Data
   :class: longtable
   :widths: 34 66
   :header-rows: 1

   * - **Data Identifier**
     - **Values**
   * - `legal_name`
     - The legal name of the QEAA Provider as it appears in the official records.
   * - `identifier`
     - The VATIN of the QEAA Provider. A public body MUST also provide its ``NTR`` identifier valued with its IPA code.
   * - `legal_nature`
     - Whether the QEAA Provider is a public sector body or a private entity.
   * - `contact_information`
     - The institutional contact (PEC) and the technical support contact of the QEAA Provider, together with the postal address and the information web page provided where available.
   * - `service_policies`
     - The terms and conditions and the privacy policy of the QEAA issuance service.
   * - `service_description`
     - The localized description of the QEAA issuance service. The user-facing trade name is provided where available.
   * - `data_protection_authority`
     - The Data Protection Authority contact email.
   * - `entitlements`
     - The entitlements that state the QEAA Provider role, and the additional roles it plays where applicable.
   * - `provided_attestations`
     - The declaration that the QEAA Provider issues its QEAA types, with the format and the attributes of each type.
   * - `conformity_assessment`
     - The outcome of the conformity assessment supporting the qualification of the Qualified Trust Service Provider that issues the QEAA.
   * - `credential_type_declaration`
     - The QEAA types the QEAA Provider issues, each anchored to its Rulebook.
   * - `credential_technical_specification`
     - The technical definition of each QEAA type, that is its schemes and its formats.
   * - `credential_policies`
     - The conditions of use of each QEAA type, that is its validity and its purposes.
   * - `signing_trust_anchor`
     - The trust anchor supporting the validation of the QEAA the Provider issues, that is the public key and the name. It is provided as an input because the Qualified Certification Authority of the QEAA Provider is not subordinate to the national Root Certification Authority but belongs to the perimeter of a Qualified Trust Service Provider.
   * - `federation_entity_identifier`
     - The Federation Entity Identifier of the QEAA Provider in the National Trust Framework.
   * - `federation_entity_key`
     - The Federation Entity Key of the QEAA Provider.
   * - `certificate_signing_requests`
     - One Certificate Signing Request for the WRPAC, with which the QEAA Provider authenticates towards the Wallet Units.


PuB-EAA Provider
""""""""""""""""

.. note::
   Draft. To be written.


Non-Qualified EAA Provider
""""""""""""""""""""""""""

.. note::
   Draft. To be written.



Relying Party
"""""""""""""

The table below lists the Data Identifiers a Relying Party provides to the Onboarding System.
The semantics of each Data Identifier is defined in :ref:`onboarding-system:Registration Data Model`. Unless otherwise specified, the following information is REQUIRED.

.. list-table:: Relying Party Registration Data
   :class: longtable
   :widths: 34 66
   :header-rows: 1

   * - **Data Identifier**
     - **Values**
   * - `legal_name`
     - The legal name of the Relying Party as it appears in the official records.
   * - `identifier`
     - The VATIN of the Relying Party. A public body also provides its ``NTR`` identifier valued with its IPA code.
   * - `legal_nature`
     - Whether the Relying Party is a public sector body or a private entity.
   * - `contact_information`
     - The institutional contact (PEC) and the technical support contact email address. The information web page are provided where available.
   * - `service_policies`
     - The terms and conditions and the privacy policy of the service.
   * - `service_description`
     - The localized description of the service the Relying Party offers, one description per service. The user-facing trade name is provided where available.
   * - `data_protection_authority`
     - The Data Protection Authority contact.
   * - `entitlements`
     - The entitlements that state the Relying Party role, and the additional roles it plays where applicable.
   * - `intended_use`
     - The Attestation type and optionally attributes the Relying Party intends to request from the Wallet Units, with one intended-use definition per service.
   * - `intermediary_relationship`
     - REQUIRED only where the Relying Party operates through a RP Intermediary. In that case it references its RP intermediary identifier. The RP intermediary side is described in :ref:`onboarding-system:Relying Party Intermediary`.
   * - `federation_entity_identifier`
     - The Federation Entity Identifier of the Relying Party in the National Trust Framework.
   * - `federation_entity_key`
     - REQUIRED for a Relying Party that operates without an intermediary. A Relying Party operating through a RP Intermediary MUST NOT provide it, because it is registered by its RP Intermediary according to the National Trust Framework.
   * - `certificate_signing_requests`
     - One Certificate Signing Request for each X.509 certificate the Relying Party needs, that is the WRPAC when it operates in the EUDIW Trust Framework, and the National Authentication Certificate when it operates only in National Trust Framework and supports the Proximity Flow.

.. note::
   An intermediated Relying Party registers through the Onboarding System only when it operates in the EUDIW Trust Framework, to enable cross-border operations. In this case it MUST have a record in the Register and it MUST obtain its WRPAC and, where applicable, its WRPRC, and these are issued through the Onboarding System.
   An intermediated Relying Party that operates only at national level is registered by its RP Intermediary and is not registered in the Register. In this case, when the Intermediated Relying Party is a Mobile Relying Party Instance, it MUST be registered through the Onboarding System to obtain an Authentication X.509 Certificate.


Relying Party Intermediary
""""""""""""""""""""""""""

In the National Trust Framework the Relying Party Intermediary is a Federation Intermediate, that is it onboards its intermediated Relying Parties autonomously, publishing their Subordinate Statements, as described in :ref:`infrastructure-trust:Trust Mark registration-entity`.
It provides the same Data Identifiers as a :ref:`onboarding-system:Relying Party`, with the differences in the table below.
The Data Identifiers not listed here are provided as for a Relying Party.

.. list-table:: Relying Party Intermediary Registration Data, differences from the Relying Party
   :class: longtable
   :widths: 34 66
   :header-rows: 1

   * - **Data Identifier**
     - **Values**
   * - `intended_use`
     - Not provided. A Relying Party Intermediary does not request attributes for itself, but on behalf of the intermediated Relying Parties.
   * - `intermediary_relationship`
     - Valorized on the intermediary side, that is the Relying Party declares that it is a designated intermediary.
   * - `federation_entity_identifier`
     - The Federation Entity Identifier of the Relying Party Intermediary in the National Trust Framework.
   * - `federation_entity_key`
     - The Federation Entity Key of the Relying Party Intermediary.

.. note::
  The registration of a Relying Party Intermediary and the registration of its intermediated Relying Parties are linked, the Intermediary declares that it acts as an intermediary, and each intermediated Relying Party references it in its own :ref:`onboarding-system:Relying Party` profile.


Wallet Provider
"""""""""""""""

.. note::
   Draft. To be written.


Authentic Source
""""""""""""""""

.. note::
   Draft. To be written.


.. include:: ../common/common_definitions.rst
.. Included via onboarding-system.rst at title level '-' (level 1).

Registration Model
------------------

This section provides the static view of the registration with the aim of defining the information each entity has to provide, which conditions it has to meet and which artifacts and registry entries it obtains. It is organized as a common part and a profile for each role.

Common Registration Data
^^^^^^^^^^^^^^^^^^^^^^^^

Every entity that onboards provides a common set of registration data, regardless of its role and of the registry where the data is finally stored.
This common set identifies the organization, provides the contact information and states the role it intends to play, and it is the same information whether the entity is a Wallet-Relying Party, an Authentic Source or a Wallet Provider.

The common registration data covers the following information.

  - **Legal name** of the organization, as it appears in the official records.
  - **Identifier**, one or more official identifiers of the organization. Within IT-Wallet the Value Added Tax Identification Number (VATIN) is required for every entity, and a public body additionally provides its national identifier of type ``NTR``, valued with its IPA code, that is the code of the Italian Index of Public Administrations (`Indice dei domicili digitali della Pubblica Amministrazione e dei gestori di pubblici servizi <https://indicepa.gov.it/ipa-portale/>`). The other identifier types defined in Table 2 of [`ETSI TS 119 475`_], such as the European Unique Identifier (EUID) and the Legal Entity Identifier (LEI), are optional but they are not supported in the current version of these specifications. The syntax of the ``organizationIdentifier`` is defined in clause 5.1.4 of [`ETSI EN 319 412-1`_].
  - **Legal nature** of the entity, that is whether it is a public sector body or a private entity.
  - **Contact information**, that is the postal address, the electronic mail address, the telephone number and the information web page of the organization.
  - **Policy references**, that is the terms and conditions and the privacy policy of the service, each published at its own URL.
  - **Data Protection Authority**, the authority competent for the supervision of the entity under the data-protection law, with the contact information the Users employ to report suspicious actions. For a Wallet-Relying Party this information is carried by the ``supervisoryAuthority`` field defined in :ref:`infrastructure-trust:Register of WRPs`.
  - **Declared roles**, that is the entitlements the entity requests, which state the roles it intends to play in the ecosystem.

The Onboarding System collects this common set once, at registration, independently of where the data is finally stored.
Depending on the role, the data is then encoded in a different data model, the ``WalletRelyingParty`` schema of the Register for a Wallet-Relying Party (:ref:`infrastructure-trust:Register of WRPs`), the entry of the AS Registry for an Authentic Source (:ref:`registry:Authentic Source Registry`), and the notification dataset for a Wallet Provider.
The common set described above is the information the entity provides, seen from the Onboarding System and independently of its encoding.

Every entity that is a Federation Entity, that is every entity except an Authentic Source, additionally provides the technical data of the National Trust Framework, that is its Federation Entity Identifier, its Federation Entity Keys and its service endpoints.
This technical data is described in the OID Federation Registration, see :ref:`onboarding-system:Entity Registration`, and it is not part of the administrative common set above.

Beyond the common set, each entity provides the data that is specific to its role, such as the attributes a Relying Party intends to request, the attestation types an Attestation Provider intends to issue, and the way an entity valorizes the common data for its role.
This role-specific data, together with the cryptographic material for which a Wallet-Relying Party requests a WRPAC, is described in :ref:`onboarding-system:Registration Profiles`.

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
     - **National x.509 certificate**
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
     - yes only if it issues a Digital Credential published in a EU Rulebook
     - yes only if it issues a Digital Credential published in a EU Rulebook
     - yes only if it issues a Digital Credential published in a EU Rulebook
     - Sign/Seal Certificate, for the Digital Credentials anchored to the National Trust Framework
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

.. note::
   Draft. To be written.


QEAA Provider
"""""""""""""

.. note::
   Draft. To be written.


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

.. note::
   Draft. To be written.


Relying Party Intermediary
""""""""""""""""""""""""""

.. note::
   Draft. To be written.


Wallet Provider
"""""""""""""""

.. note::
   Draft. To be written.


Authentic Source
""""""""""""""""

.. note::
   Draft. To be written.


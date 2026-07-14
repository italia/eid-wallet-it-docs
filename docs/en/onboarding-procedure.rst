.. include:: ../common/common_definitions.rst
.. include:: ../common/symbols.rst

Onboarding Procedure
====================

Onboarding is the process through which an entity becomes operational and recognisable within the IT-Wallet ecosystem: it establishes the entity's legal eligibility, registers it with the competent bodies, and equips it with the trust artifacts other participants rely on to authenticate it and evaluate its authorizations.

The IT-Wallet ecosystem operates two trust frameworks together:

- **National Trust Framework**, built on OpenID Federation 1.0 together with the national X.509 PKI embedded in the same Federation Trust Anchor, is the **root of this onboarding procedure**.
  It is the mandatory National Trust Framework every entity onboards into, and the layer that drives identity proofing and, in turn, certificate issuance for the other framework too.
- **EUDIW Trust Framework**, defined at EU level for Wallet-Relying Parties (`EIDAS-ARF`_, Commission Implementing Regulation (EU) 2025/848), is **additive** on top of the National Trust Framework.
  For entities in a notified category (PID Providers, QEAA Providers, and PuB-EAA Providers) it is mandatory, and becomes the **authoritative** one for the artifacts a Wallet Instance relies on to check identity and legal value.

Non-qualified EAA Providers follow the EUDIW Trust Framework as well: when operating in EUDIW their trust anchor is published in the EAA Providers LoTE, while a national-only EAA Provider relies on the trust anchor distributed through the applicable Attestation Rulebook.

Which verification mechanism a given Credential requires is not up to whoever is checking it, but is dictated by the Credential's own legal category, because that category fixes the applicable signature-verification anchor (Trusted List, LoTE, or OID-FED Trust Chain) regardless of whether the verifying party itself operates only nationally or also cross-border.

Where the two frameworks diverge in configuration, the EUDIW Trust Framework prevails, being legally binding, while the National Trust Framework is functionally binding within the national ecosystem.

This section is organised around the three processes that, together, take an entity from a registration request to full operational status:

- The **Administrative Process** establishes an entity's legal standing, regulatory compliance, and eligibility to participate in the ecosystem, ahead of any technical step;
- The **Registration Process** technically registers the entity: always in the National Trust Infrastructure, and, where the entity's category requires or opts into it, also as a EUDIW Wallet-Relying Party;
- The **Certificate Issuance Process** equips the entity with the cryptographic trust artifacts tied to its registration, again for one or both trust frameworks depending on its category.


Overview
--------

This overview introduces the actors and system components involved in onboarding, the Dual Trust Framework logic that shapes every onboarding decision, and the three processes an entity goes through.
The processes themselves are specified in the sections that follow; the material here is the shared frame they build on.

Entities and Components
^^^^^^^^^^^^^^^^^^^^^^^

Two families of actors take part in onboarding: the entities that are onboarded, and the trust-infrastructure entities that operate the onboarding itself.

Those trust-infrastructure roles are in turn realised by the software components of the Onboarding System, described at the end of this subsection.

**Entities being onboarded**

  - **Authentic Sources**: authoritative providers of the data that Credentials are built from.
    They follow a data-focused registration path based on PDND integration; their trust is governed by the PDND trust framework rather than by the Wallet-Relying Party model, and they are therefore outside the Dual Trust Framework logic described below;
  - **Wallet-Relying Parties (WRPs)**: the umbrella category defined by Commission Implementing Regulation (EU) 2025/848 for every entity that relies on Wallet Units to provide a service.
    It is further split into:

    - **Credential Issuers**, comprising **PID Providers** and **Attestation Providers** (**QEAA Providers**, **PuB-EAA Providers**, and non-qualified **EAA Providers**).
      A PID Provider is a Credential Issuer but is **not** an Attestation Provider;
    - **Relying Parties** and **Relying Party Intermediaries**, which request Attestations from Wallet Units.
      A Relying Party operates through one or more **Relying Party Instances**.

  - **Wallet Providers**: provide the **Wallet Solution** and the **Wallet Instances** that Users install.
    A Wallet Provider is not a WRP; in the EUDIW Trust Framework it follows a notification-only path (no Register entry and no Wallet-Relying Party Access Certificate), but it still onboards into the national federation.

**Trust-infrastructure entities**

  - **Supervisory Body**: runs the Administrative Process, avails itself of the Registrar for technical registration, and acts as the national single point of contact for notification to the European Commission;
  - **Registrar** and **Register**: the Registrar performs the technical registration of WRPs and writes their records into the **Register** defined by Commission Implementing Regulation (EU) 2025/848;
  - **Provider of WRPAC** and **Provider of WRPRC**: issue, respectively, the Wallet-Relying Party Access Certificate (WRPAC) and the Wallet-Relying Party Registration Certificate (WRPRC);
  - **Trusted List / LoTE Provider**: signs and publishes the trusted lists, i.e. the Lists of Trusted Entities (LoTEs) and the EU Member State Trusted List (EUMS TL).
    This provider has a special role, as its own trust anchor is the root against which the trusted lists are validated;
  - **OID-FED Federation Authorities**: the **National Trust Anchor** and its **Intermediates**, which register federation entities, issue X.509 certificates and Trust Marks, and apply metadata policies.
    In IT-Wallet the National Trust Anchor also operates the **root Certification Authority** of the national X.509 signing PKI; its root certificate is distributed through the Trust Anchor's Entity Configuration, in the ``x5c`` of a dedicated JWK, distinct from the federation signing key.

.. note::
   A single organisation may perform several of these functions at once.

**Onboarding System components**

The trust-infrastructure roles listed above are realised, within the Onboarding System, by the following software components:

- the **Onboarding UI** that provides the onboarding entities with a single touchpoint that orchestrates the entire onbording flow;
- the **Registration Service** (the Registrar) that verifies WRPs and writes their records to the **WRP Register**;
- the **WRPAC** and **WRPRC Issuance Services**;
- the **Signature Certificate Issuance Service**;
- the **OID-FED Federation Service**;
- the **Publication Service** that signs and publishes the trusted lists from the **notification dataset**.

Two of these components are data stores, kept separate on purpose:

- the **WRP Register** holds the WRP registration records defined by Commission Implementing Regulation (EU) 2025/848 (identification, intended use, and related data), and drives the issuance of the WRPAC and WRPRC;
- the **notification dataset** holds the notifiable information defined by Commission Implementing Regulation (EU) 2024/2980 (identification, trust anchors, and service supply points), and feeds the Publication Service when an entity is published in a trusted list.

The two overlap only in the identification data, so the split avoids conflating registration with notification: the infrastructure entities that are notified but not registered as WRPs (Wallet Providers, Providers of WRPAC/WRPRC, Registrars) appear in the notification dataset but not in the Register.

These components operate alongside the components of the Registry Infrastructure (Claims Registry, AS Registry, Digital Credentials Catalog, Schema Registry, and Taxonomy, see :ref:`registry:Registry Infrastructure`) and, at EU level, the European Commission LoTE Provider with its Lists of Trusted Lists (LOTLs), LoTEs, and Catalogues.

The Dual Trust Framework
^^^^^^^^^^^^^^^^^^^^^^^^

One principle governs how the two trust frameworks combine: the mechanism used to verify a Credential's signature is bound to the Credential's **legal category**, not to the context of the party that performs the verification.

The legal category confers legal value on the Credential, and that value fixes the signature-verification anchor.

A PuB-EAA, for instance, carries the legal effect its defining regulation attaches to the category, so its signature MUST be verified through the mechanism (LoTE, Trusted List) the category mandates, whichever party verifies it.

.. plantuml:: plantuml/onboarding-system-overview.puml
    :width: 99%
    :alt: IT-Wallet onboarding system overview showing dual trust framework registration processes and trust infrastructure
    :caption: `IT-Wallet Onboarding System Overview. <https://www.plantuml.com/plantuml/svg/ZLJRRjj647tdLmma8AXHoqxTk7NwK4IcAC20MnkMWlH1BwFbY5vakQlkHJ9HvDyxkvG8Ch2548ObSSwPovdB9-VH-b2hp4kl2EwMao-e57buq6k3jfIwWaNZFDNmi2ExaxJFClTLwYrQhC4zOsds4RH1vQXdAMc3GVablVYfafMkINiG_8zi3xL5yHKhMlY6WriI7dMb-cwcrffzRfInCBvEJy_O4U2_3E3Ms9Bi0VjhUh9l_OpGunhTZu5HU6DF8BCMC2eq2zUiz4-M_WtaV9J2TDATZG0TaFPPTgWKHYSa7d7037fbZNgGptV9MP0mdbqNDxCF4TfvdPQrrD9vYrxk21wj4UHST0WmyBW8szX6Psp3fPLDSefb3UFYbzkY-9tntmQUdwWw-3NwXD-7kzbaNinWJYKTmDFWdusLNf9ZWPOsE0zJBVWT_0ntSH9gAYLwScShFPc0JZHKvr2ZBj7752UJbE26IXZVtiwA-UqWS2y_op46kIvYdOBQ7bYgO9pV5B_b7vE3RXX6NvuUeULHT97VFS7L-wlhoviFDorrRxT3zb2VdAoN6odGy_eu5r2BK_gpPITP8Z0RuD3J_1W3HHVYDEMfezWtAGlUEFJ14boo3gXM-hKqanydXxK1lDBzXlkriSZVWeXkZvfAlU4IXuBc2cNjuCXCKD6-6y_dywiy_uumNGp1wDZp6zYPhAH71RcbahINg1paR5McQWEXVuEv4CzKup2II-_U82pnnMXJjqYFBptOS0B-DgsoQUfGb_0Orkhm-xK9IDR1ZAOGsx3kPdoOILeTAk6UCu-hT6-M1JVs_c5vpn_5vxyMiBnlXzMhdWzEa_-oJ2WJIhvLmPejeUPXC7KjdUCC4ea4RtzwieoqvwNxCzwPFy25TIrzokHyfRa6YiS5uoIXy2xBWanWB6j6u-06CRuzYKSGxp23ZdV2zbQLIw8TsGOeNTEp8uCnpE2H_nwja-9KSlN26kScwtIaEs9Q9wOUCcWNBHelBfBH3esyKknq_qoM3gU7oiuNjwLJOgNRoBXMb5GvWjfLO5pOHhOx9jo07EmDDuCjnnpR-lPMUcA2u1eu3HHHlRCirT2JWGMIcmQSHnzu2Dw1CDfn3DAYYM3xms1kH88w6Q7IkK3mpyNr-uzmkM9KfQMkG7JtWfDc3HB3AoP41BoBkYZfdZiRHKrrRnMoZ0U25U-fiqCbepw7Uy0pjGrsQnovyyCkkkmJwJBKwdy0>`_

The table below reads by Credential category: each row is the **provider of that category**, and the columns show the artifacts its onboarding provisions and the signature-verification anchor that follows.
For notified categories the EUDIW mechanism is authoritative, while the National Trust Framework is the mandatory national layer that every provider also holds.
The entity-authentication and signature columns describe how those artifacts are later consumed in the Trust Evaluation Process; they are shown here only to motivate what onboarding must provision.

.. list-table:: Onboarding Artifacts and Signature-Verification Anchor by Credential Category
   :class: longtable
   :widths: 12 32 26 30
   :header-rows: 1

   * - **Category**
     - **Registration and onboarding**
     - **Entity authentication**
     - **Signature (issuer data authentication)**
   * - **PID**
     -
       - EUDIW: notification, WRPRC / Register API, LoTE.
       - OID-FED: Entity Configuration and Trust Mark.
     -
       - EUDIW: WRPAC, LoTE.
       - OID-FED: federation Trust Chain (supplementary).
     - EUDIW only: trust anchor from the PID Providers LoTE.
   * - **QEAA**
     -
       - EUDIW: QTSP qualification and supervision, WRPRC / Register API, Trusted List.
       - OID-FED: Entity Configuration and Trust Mark.
     -
       - EUDIW: WRPAC, LoTE.
       - OID-FED: federation Trust Chain (supplementary).
     - EUDIW only: trust anchor from the QEAA Provider's QTSP Trusted List.
   * - **PuB-EAA**
     -
       - EUDIW: conformity assessment (Art. 45f), notification, WRPRC / Register API, LoTE.
       - OID-FED: Entity Configuration and Trust Mark.
     -
       - EUDIW: WRPAC, LoTE.
       - OID-FED: federation Trust Chain (supplementary).
     - EUDIW only: trust anchor from the PuB-EAA Providers LoTE.
   * - **Non-qualified EAA**
     -
       - EUDIW: WRPRC / Register API, EAA Providers LoTE (when operating in EUDIW).
       - OID-FED: Entity Configuration and Trust Mark.
     -
       - EUDIW: WRPAC, when operating in EUDIW.
       - OID-FED: Federation Entity Authentication.
     -
       - EUDIW: trust anchor from the EAA Providers LoTE (national-only: from the applicable Attestation Rulebook).
       - OID-FED (primary): SD-JWT VC (optionally with a JOSE ``trust_chain`` header); mDoc with an X.509 certificate chaining to the Federation Trust Anchor root, OID-FED identifier in the SAN URI.
   * - **Non-EAA (national)**
     - OID-FED: Entity Configuration and Trust Mark.
     - OID-FED: Federation Entity Authentication.
     - OID-FED: X.509 signing chain anchored to the Federation Trust Anchor.

Wallet Instances are not federation entities and are not onboarded directly: a Wallet Instance is registered indirectly, through its Wallet Provider (see :ref:`wallet-instance-registration:Wallet Instance Initialization and Registration`), and is deemed reliable through a Wallet Instance Attestation issued and signed by that Wallet Provider (see :ref:`wallet-instance-attestation-issuance:Wallet Instance Attestation Issuance`).

The Wallet MUST support both frameworks: the EUDIW Trust Framework because it is legally required, and the National Trust Framework for functional conformance.

The Onboarding Processes
^^^^^^^^^^^^^^^^^^^^^^^^

To participate in the IT-Wallet ecosystem an entity MUST perform an onboarding procedure that establishes its regulatory compliance, its authorizations, and its trust relationships.

The procedure consists of four processes, which apply differently depending on the entity type:

  1. The :ref:`onboarding-procedure:Administrative Process` validates an entity's legal standing, regulatory compliance, and organizational eligibility.
     It is performed by the Supervisory Body and applies to Authentic Sources, Wallet Providers, and WRPs;
  2. The :ref:`onboarding-procedure:Registration Process` performs technical registration.
     Every entity is registered in the National Trust Infrastructure; entities whose category requires it, or that opt in for cross-border recognition, are additionally registered as EUDIW Wallet-Relying Parties in the Register;
  3. The :ref:`onboarding-procedure:Certificate Issuance Process` equips the entity with the cryptographic trust artifacts tied to its registration, for one or both trust frameworks depending on its category;
  4. The :ref:`onboarding-procedure:Notification and Publication` publishes a notified entity in the trusted list for its category, which is what makes it trusted across the ecosystem.

Not every entity performs every process.
A Wallet Provider, for instance, is administratively assessed, completes federation registration, and is then notified, without WRP registration or certificate issuance; a national-only Relying Party stops after federation registration.

Although this document presents the national (federation) and EUDIW flows of the Dual Trust Framework as separate paths, the onboarding entity does not experience them as separate procedures.
The Onboarding System exposes a single entry point, the Onboarding UI, which orchestrates the whole procedure end to end: it drives the entity through the applicable administrative and technical steps of both trust frameworks with a unified UX, so that the dual path remains an implementation detail of the infrastructure rather than a burden on the onboarding entity.

Onboarding consumes and produces a defined set of artifacts.
The inputs depend on the entity's type and selected scope:

  - **Registration data**, for every entity registered in the Register (all WRP types), conforming to the ``WalletRelyingParty`` schema that transposes the Commission Implementing Regulation (EU) 2025/848 Annex I set;
  - **Notifiable data**, for entities published in a trusted list (PID, PuB-EAA, QEAA, and non-qualified EAA Providers, and the Wallet Provider): the identification, trust anchors, and service supply points needed for the trusted-list entry;
  - **Cryptographic material**: the public key(s) for which a WRP requests a WRPAC, generated according to ETSI TS 119 411-8, and the public keys of the signature or seal certificates the entity uses to sign or seal its artifacts.

A WRP that is also a notified entity provides both the registration data and the notifiable data; a Relying Party or Relying Party Intermediary provides only registration data, as it requires no trusted-list entry.

A successful onboarding produces the entity's Register entry (and its publication), its WRPAC, its WRPRC where mandated, and its trusted-list entry where the entity is notified.
The table below lists these artifacts for each entity type **when it registers as a Wallet-Relying Party in the EUDIW path**, which is the maximal set.
An entity operating national-only does not obtain them: it holds only its Entity Configuration and Trust Mark, as the scope table that follows makes explicit (for example, a non-qualified EAA Provider operating national-only obtains no WRPAC).

.. list-table:: Onboarding Path by Entity Type
   :class: longtable
   :widths: 30 18 12 18 22
   :header-rows: 1

   * - **Entity type**
     - **Register record**
     - **WRPAC**
     - **WRPRC**
     - **Trusted-list entry**
   * - PID Provider
     - yes
     - yes
     - where applicable
     - PID Providers LoTE
   * - QEAA Provider
     - yes
     - yes
     - where applicable
     - EUMS TL (referenced in the LOTL)
   * - PuB-EAA Provider
     - yes
     - yes
     - where applicable
     - PuB-EAA Providers LoTE
   * - Non-qualified EAA Provider
     - yes
     - yes
     - where applicable
     - EAA Providers LoTE
   * - Relying Party
     - yes
     - yes
     - where applicable
     - none
   * - Relying Party Intermediary
     - yes
     - yes
     - where applicable
     - none
   * - Wallet Provider
     - no
     - no
     - no
     - Wallet Providers LoTE

The following table makes that scope dependence explicit: it shows, for the entity types that select a scope during onboarding, how the EUDIW or national choice determines the actual outputs.
It uses these abbreviations:

  - ``EC``: the Entity Configuration published in the federation.
  - ``TM``: a Trust Mark.
  - ``Sign/Seal``: the issuer's signature or seal certificate.

.. list-table:: Onboarding Outputs by Entity Type and Selected Scope
   :class: longtable
   :widths: 22 20 58
   :header-rows: 1

   * - **Entity type**
     - **Selected scope**
     - **Onboarding outputs**
   * - Credential Issuer (non-EAA, e.g. PID Provider)
     - EUDIW (notified)
     - EC (for onboarding) + WRPAC + WRPRC + Sign/Seal.
   * - Attestation Provider issuing an EAA Credential
     - EUDIW
     - EC (for onboarding) + WRPAC (LoTE-anchored) + WRPRC (LoTE-anchored) + Sign/Seal X.509 chain (SHOULD be at least anchored in the Trust Anchor's EC via notification at the catalogue).
   * - Attestation Provider issuing a national (non-EAA) Credential
     - National
     - EC (for onboarding and trust evaluation) + TM + Sign/Seal X.509 chain (SHOULD be at least anchored in the Trust Anchor's EC).
   * - Relying Party
     - EUDIW
     - EC (for onboarding) + WRPAC + WRPRC.
   * - Relying Party
     - National
     - EC (for onboarding and trust evaluation) + TM.

.. note::
   A Wallet Provider that completes onboarding in IT-Wallet is notified in the EUDIW ecosystem, and its Wallet Solution is certified.
   Its onboarding produces its Entity Configuration and the certificates for its Wallet Instance Attestation and key-attestation keys, and its trust anchor is published in the Wallet Providers LoTE.

Relying Party Intermediaries onboard through a dedicated variant of this procedure that also grants them the authority to onboard subordinate Relying Parties, handled differently by the two trust frameworks.
This is detailed in :ref:`onboarding-procedure:Relying Party Intermediaries`.

Onboarding Scenarios (Authentic Sources and Relying Parties)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following non-normative examples show how entities onboard and connect, from the Authentic Source that provides the data to the Relying Party that consumes the resulting Credential.
They use two concepts detailed later: the **Taxonomy** domains and purposes (a component of the Registry Infrastructure) and the **operational scope** granted to a Relying Party (see :ref:`onboarding-procedure:Wallet-Relying Parties`).

On the supply side, two scenarios illustrate how a Credential reaches the catalogue:

  - **Public catalogue (Mobile Driving Licence).** An Authentic Source (e.g. the Motorizzazione) declares the mDL claims (``given_name``, ``family_name``, ``driving_privileges``) under Taxonomy domain ``MOBILITY_TRAVEL`` / purpose ``DRIVING_RIGHTS`` and integrates via e-Service PDND (see :ref:`e-service-pdnd:e-Service PDND`).
    A Credential Issuer discovers it in the AS Registry; integration approval is automatic, as the mDL is a regulatory mandate; the mDL type is published in the :ref:`registry:Digital Credentials Catalog` and becomes discoverable by citizens.
  - **Private offer (Corporate Employee Badge).** A private Authentic Source declares the badge claims (``given_name``, ``family_name``, ``employee.job_title``) under Taxonomy domain ``MEMBERSHIP`` / purpose ``ASSOCIATION``.
    Integration requires the Authentic Source's approval, as there is no regulatory mandate; the badge type is published in the catalogue for discovery but is issued to employees only through a direct Credential Offer.

On the demand side, Relying Parties onboard with an operational scope matched to their service and organizational profile:

  - **Car-rental service** (private, ATECO 77.11): requests ``driving_privileges`` from the mDL to verify rental eligibility; granted the ``MOBILITY_TRAVEL`` / ``DRIVING_RIGHTS`` scope.
  - **Municipal service** (public, with IPA code): requests ``given_name``, ``family_name``, and ``tax_id_code`` from the PID for citizen identification; granted a broader scope reflecting its public-service mandate.
  - **Corporate access control** (private, ATECO 62.01): requests ``employee.job_title`` from the Corporate Employee Badge to control facility access; granted the ``MEMBERSHIP`` / ``ASSOCIATION`` scope.

Administrative Process
----------------------

The administrative process is the first phase of onboarding.
It validates an entity's legal standing, regulatory compliance, and organizational eligibility to participate in the IT-Wallet ecosystem, before any technical registration takes place.

It is performed by the **Supervisory Body**, which relies on the Registrar for the entities it registers and, for notified categories, acts as the national point of contact toward the European Commission.

An entity that clears the administrative process becomes eligible for technical registration (see :ref:`onboarding-procedure:Registration Process`) and, where its category requires it, for notification into the EUDIW trusted lists.
Where a national and an EUDIW obligation overlap, the EUDIW obligation is authoritative.

The administrative process applies to Authentic Sources, Wallet Providers, and Wallet-Relying Parties.

Authentic Sources
^^^^^^^^^^^^^^^^^

The administrative process for an Authentic Source validates its authority as an authoritative data provider and its eligibility to expose the declared data.
At the current stage only Italian Authentic Sources can be onboarded.

The Supervisory Body validates the organization's legal standing and data authority and classifies it as public or private.
Authentic Source trust is governed by the PDND trust framework and sits outside the WRP / federation dual path.
The declared data capabilities (the Claims Registry claims the source provides and the purposes it serves) and the full registration data schema are specified in :ref:`registry:Authentic Source Registry`.

Integration and Technical Registration
""""""""""""""""""""""""""""""""""""""

Because it sits outside the WRP / federation dual path, an Authentic Source does not go through the :ref:`onboarding-procedure:Registration Process`; its integration and technical registration are described here.

All Authentic Sources integrate through PDND (see :ref:`e-service-pdnd:e-Service PDND`): public bodies through a national e-service, private entities additionally providing a complete OAS3 specification.
The technical registration follows three steps, each with a defined interaction with the Registry Infrastructure:

  1. **Registration Package Preparation**: the Authentic Source reads the Claims Registry to select the standardized claim identifiers it provides and the Taxonomy to select the domains and purposes it serves, then prepares its registration data (organization information, declared claims and purposes, API integration details, and data-provision capabilities) according to the schema in :ref:`registry:Authentic Source Registry`.
  2. **Technical Validation**: the Supervisory Body validates the declared claims against the Claims Registry, the declared purposes against the Taxonomy, the PDND (or OAS3) integration, and the response-format and state-mapping standards.
  3. **Authentic Source Registry Publication**: on success, the Authentic Source and its declared capabilities are written to the AS Registry, becoming discoverable by Credential Issuers.

.. plantuml:: plantuml/as-registration-process.puml
    :width: 99%
    :alt: Authentic Source registration process showing the 3-step procedure
    :caption: `Authentic Source Registration Process. <https://www.plantuml.com/plantuml/svg/ZLPRRzfO47xthnY1L6tKa7IppMxAGrLYZ8J4bWYekW-y7Em1ZcgVupqNYBNgVzyPNy2EI5GhWiJdczittyp95-k4SJvB0oTTYZ1T3RwBD4K7SxNHmYHIxM1PM8SPp0ze3XAFGM1_I9KB8pAmUv7e8uEs8hNOEabmAtpgLlZiHgdSgGoLWvW-qBHGkOX_Y1qkNK713SPEg5tQTZCoHXz3dMe3_VloQHsU3E2_0E1HcmHDZVsZV8AVxOo44njXVmqiOaSdhoE32j2RvsY4arg9529591PhzPl1VprQnxJe4urNFH0MY80WgAk6tXjqzoWuHJ-Ns6j1larBPrv2VtmVFOm_ClJaTPHaKadhEB43mfFHCLhRAwlfU5pwd5jgjIcepAGedOeaWtxq-sCK_KNudntF2zpLVhLwm-zyEXvCeZ5CCAdPWP5tUssaasY9e9Nnri58nVGEtiEKLP5X8eL3UxLMWm6ecjHho8IYpd6AWq6Pu1OJw3y-ZgF9uyl0JNw6OdHoNNATCLOzCBY3VlWG_Hb-AXsSXD7xldY2oWxPHJXTmDs7k_lRXuyFbUdHv5thBZyX6YUtCgOwO6gj5of-YtywEKYY2FGMAFGeR6A8k9FWwoQBaubvrMH9qoUSDmYtn8D8r-fIcgKVAxkr0LpeVa7zsXf1l_cOtJQSIhMjIpmJ6gP2PXOQon8QL-_waydaBWnV68oMNR2m9TyNiMEvauxcBZIaCvezsa0GqccgTrKWuLwnNCPxp4GtagtUNJPOYMUjT5OXdNXkmReA-AfhPbbrf5nuyfkq_lkI0iwdZKRB4BdVT3JUoeH7XoPWHfdpACtqAgB6pkQh6Nr5t_vUmcfMYTMbBH-K9lq4GPngdq0lyaRdA1I9GMUPjBRCZnSKwIWgdo3WbJqOVEOzCmJhDvbqPIRNQqKr82yNmKgYNMY3W50CvlqnvC_M3c9ykH8R4C_m49ezOLgZIYKXNJG5RqhQfbUD1SjWo99_YLObu-Jl5cAZhHrioeLzCgp6QGXr1jMWyU7DpUTwS3g7Yv2S7lT8yrAj7anElhWj3HDhLKKM6seaizBAb4TX23vdQziaN83ip0qrWukgSwpgEzAAB2z2ge7I86A9lQkWgk5C0n4ajmNGvUqyYU0Tn5fPtbegBeAgfby4SoCOofC_1DA1H_Zdvlx39xXT4sgd-Bg9p_k2BY_YW2r8NKCsK_2EUKcbtP_Ea3bLhL6W-v9amOoVs3c8L38_zJuWJUNUvDgYlQvdqGPVK2Nqpyd_>`_

Following administrative approval, a Credential Issuer that intends to use the source requests integration authorization.
For regulatory mandates this authorization is automatic; otherwise the Authentic Source authorizes the request on business and technical criteria.
Authentic Source registration is complete and independent of Credential Issuer integration: the source becomes discoverable upon publication, while a Credential type becomes publicly discoverable only after a successful Authentic Source to Credential Issuer integration and the Supervisory Body's approval of catalogue eligibility.
At that point the Credential type is written to the :ref:`registry:Digital Credentials Catalog`, with its Credential Schema referenced from the Schema Registry.

Wallet Providers
^^^^^^^^^^^^^^^^

The administrative process for a Wallet Provider establishes its eligibility and drives the conformity assessment of its Wallet Solution.
The assessment covers the security of the wallet architecture, its data-protection mechanisms, and its user-privacy features, and is the precondition for the Wallet Solution to be certified.

A certified Wallet Solution is notified in the EUDIW ecosystem, and the Wallet Provider's trust anchor is published in the Wallet Providers LoTE.
The Wallet Provider follows a notification-only path: it has no Register entry and no WRPAC, but it still onboards into the national federation for functional conformance.
Clearing the administrative process is the green light to the Wallet Provider's technical onboarding.

.. note::
   The certification of the Wallet Solution is an external process; the administrative phase references its outcome rather than performing it.

Wallet-Relying Parties
^^^^^^^^^^^^^^^^^^^^^^

For Wallet-Relying Parties, the administrative process validates legal standing and the entitlement to request or issue, and, for notified categories, establishes the eIDAS2 basis for notification:

  - **PID Providers** are validated per national designation as providers of Person Identification Data;
  - **QEAA Providers** are validated through the qualification and supervision of the issuing QTSP;
  - **PuB-EAA Providers** undergo the conformity assessment required by Art. 45f of the eIDAS2 Regulation;
  - **Non-qualified EAA Providers** are validated for eligibility; when operating in EUDIW their trust anchor is published in the EAA Providers LoTE, while a national-only one relies on the applicable Attestation Rulebook.

For **Relying Parties**, the Supervisory Body performs a policy-based authorization.
It evaluates the organizational type (public administration or private entity), the business-sector classification (e.g. ATECO code), and the legitimate requirements of the service, and grants an **operational scope** defining which Credential domains and purposes the Relying Party may request.
This scope is the administrative boundary later enforced at presentation.

Relying Party Intermediaries additionally demonstrate their eligibility to act on behalf of Relying Parties, pursuant to Art. 5b(8) of the eIDAS2 Regulation (`EU_2024_1183`_).

For **Credential Issuers**, the administrative process records the Credential types the issuer intends to issue and authorizes, where needed, its integration with the relevant Authentic Sources.

Clearing the administrative process is, for every Wallet-Relying Party, the precondition for technical registration in the Register and in the federation.

Administrative Summary
^^^^^^^^^^^^^^^^^^^^^^

The table below summarises the administrative process by entity type.
In every case the checks are performed by the Supervisory Body.

.. list-table:: Administrative Process by Entity Type
   :class: longtable
   :widths: 22 40 38
   :header-rows: 1

   * - **Entity**
     - **Administrative input / checks**
     - **Outcome**
   * - Authentic Source
     - Data authority and legal standing; public/private classification; declared claims and purposes (schema in :ref:`registry:Authentic Source Registry`).
     - Eligibility to complete AS technical registration; entry in the AS Registry.
   * - Wallet Provider
     - Eligibility; conformity assessment of the Wallet Solution (security, data protection, privacy).
     - Certified Wallet Solution; green light to notification and technical onboarding.
   * - PID / QEAA / PuB-EAA Provider
     - Legal standing and category-specific eIDAS2 basis (national designation; QTSP qualification; Art. 45f conformity assessment).
     - Eligibility for technical registration and notification.
   * - Non-qualified EAA Provider
     - Legal standing and eligibility to issue (no notification).
     - Eligibility for technical registration.
   * - Relying Party / RP Intermediary
     - Legal standing; organizational type; business sector; legitimate service requirements → operational scope (domains/purposes).
     - Authorized operational scope; green light to technical registration.
   * - Credential Issuer
     - Intended Credential types; authorization to integrate with Authentic Sources.
     - Green light to technical registration.

Registration Process
----------------------

Following administrative approval, an entity is registered technically.
Registration is founded on the National Trust Infrastructure: every entity MUST join it, because it is what makes the entity exist and be recognisable in the national system, and it drives the rest of onboarding, including certificate issuance.
On top of this foundation, entities whose category requires it (or that opt into cross-border recognition) additionally complete EUDIW Wallet-Relying Party registration, which creates their entry in the Register.
This second step is additive, but normative: for the notified categories it is legally required, and the Register entry it produces carries the legal value on which cross-border participants rely.

Authentic Sources are outside this process: sitting outside the WRP / federation dual path, their technical registration is described under :ref:`onboarding-procedure:Administrative Process`.
Wallet Providers, which are not WRPs, complete OID Federation Registration and are notified, but obtain no Register entry (see :ref:`onboarding-procedure:Overview`).

The certificate issuance that concludes registration (the X.509 federation certificate, and the WRPAC and WRPRC) is specified separately in the :ref:`onboarding-procedure:Certificate Issuance Process`.

OID Federation Registration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

OID Federation Registration is mandatory for every Federation Entity (Credential Issuers, Relying Parties, and Wallet Providers) and onboards it into the national trust hierarchy operated by the Federation Authorities (the National Trust Anchor and its Intermediates).
It is the foundation of onboarding: for a national-only entity it is the sole registration, and for an entity that also registers as a Wallet-Relying Party it is the layer that registration builds upon.
Its prerequisites and artifacts (the Federation Entity keys, the Entity Configuration published at ``/.well-known/openid-federation``, and the Certificate Signing Request) are specified in :ref:`infrastructure-trust:Infrastructure of Trust` and are not restated here.

**Input Model.**
The entity submits an onboarding request to its Federation Authority containing its Federation Entity Identifier, its Federation Entity Key in JWK format, and an X.509 Certificate Signing Request in PKCS #10 format.
The entity MUST already publish a valid Entity Configuration signed with the corresponding private key.

**Output Model.**
An active Subordinate, discoverable through the federation endpoints, whose Entity Configuration carries the ``authority_hints`` pointing to the Federation Authority and the ``trust_marks`` it received.
For a national-only entity, this Entity Configuration and Trust Mark are what make it recognisable and its authorizations verifiable.

**Procedure.**
The Federation Authority validates the request and the published Entity Configuration and applies the applicable metadata policy.
It then registers the entity as its Subordinate and issues the Subordinate Statement and the Trust Marks attesting the entity's role and authorizations.
The entity retrieves its Subordinate Statement and updates its Entity Configuration with the received ``authority_hints`` and ``trust_marks`` (see :ref:`infrastructure-trust:Subordinate Statements`).
The X.509 certificate that certifies the Federation Entity Key is issued in the Certificate Issuance Process, separated from the federation onboarding flow in this profile.

WRP Registration
^^^^^^^^^^^^^^^^^

WRP Registration is the EUDIW step that a Wallet-Relying Party (a Relying Party, a Relying Party Intermediary, or a Credential Issuer that is a PID, QEAA, PuB-EAA, or non-qualified EAA Provider) completes on top of its federation registration.
Additive on the federation identity but normative for the notified categories, it produces the entity's entry in the Register and is the precondition for the issuance of its Wallet-Relying Party Access Certificate.

WRP Registration presupposes that the entity has already completed :ref:`onboarding-procedure:OID Federation Registration`: it is already an active Subordinate with a published Entity Configuration and a Trust Mark.
No Trust Mark is issued here, because the Trust Mark belongs to the OID Federation Registration step; WRP Registration adds the Register record, a separate EUDIW artifact for the same legal entity.
The two are linked by the entity's identifier: the Federation Entity Identifier used in the Entity Configuration also identifies the entity in its Register record.

**Input Model.**
The entity submits its registration data conforming to the ``WalletRelyingParty`` schema (Commission Implementing Regulation (EU) 2025/848, Annex I, and the common data schema of the CIR 2025/848 Amendment, Annex VI).
The data covers the entity's identification and its intended use (the attributes a Relying Party intends to request from Wallet Units, or the attestation types an Attestation Provider intends to issue), together with the cryptographic material, i.e. the public key(s) for which the entity requests a WRPAC.
This key is distinct from the federation signing key carried in the Entity Configuration.

**Output Model.**
A Register entry with status ``active``.
This active status is the green light for the issuance of the WRPAC and, where mandated, the WRPRC (see :ref:`onboarding-procedure:Certificate Issuance Process`).

**Procedure.**
The entity submits its registration data to the Registrar through the Onboarding UI (the Registration Service, over the common Register REST API).
The Registrar verifies the entity's identity and eligibility (the identity proofing carried out during the Administrative Process, per ETSI TS 119 461) and, on success, creates the record in the Register with status ``active``.
The Register record is electronically signed or sealed by, or on behalf of, the Registrar, so that the certificate providers and the Wallet can rely on it.

The Register and the WalletRelyingParty Schema
""""""""""""""""""""""""""""""""""""""""""""""

The Register is the national register of Wallet-Relying Parties that each Member State establishes and maintains under Commission Implementing Regulation (EU) 2025/848 (Article 3), operated by the Registrar.
It is distinct from the five components of the :ref:`registry:Registry Infrastructure`: those hold Credential semantics and discovery data (claims, schemas, catalogue, taxonomy, Authentic Sources), whereas the Register holds the WRP registration records that drive the WRPAC and WRPRC and support Relying Party authorization.

Each record is a ``WalletRelyingParty`` object whose structure is defined normatively by the Annex VI schema (Tables 1-11) of the Commission Implementing Regulation (EU) 2025/848 Amendment: it carries the entity's identification, its intended use, its entitlements, the attestation types it issues where applicable, its intermediary references (``usesIntermediary``, ``isIntermediary``, see :ref:`onboarding-procedure:Relying Party Intermediaries`), and its governance and key material.
The conceptual role of the Register, with non-normative object examples, is described in :ref:`trust-artifact-eudiw:Register of WRPs`, and its public read API in :ref:`trust-artifact-eudiw:Common Register Open APIs`.

Relying Party Intermediaries
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A Relying Party Intermediary is a Relying Party that connects to Wallet Units and requests User attributes on behalf of other (intermediated) Relying Parties (`EIDAS-ARF`_).
Its eligibility to act on behalf of Relying Parties, pursuant to Art. 5b(8) of the eIDAS2 Regulation (`EU_2024_1183`_), is established during the Administrative Process.
Because the two trust frameworks handle intermediation differently, an Intermediary is onboarded in both, and the way the intermediary relationship is expressed differs accordingly.

**OpenID Federation.** A Relying Party Intermediary matches an OpenID Federation Intermediate Entity.
It registers its federation keys and endpoints, publishes its own Entity Configuration, and issues Subordinate Statements for its Leaves.
Upon completion the Trust Anchor issues it an Intermediary Trust Mark (``https://<federation_authority_domain>/trust_marks/federation-entity/openid_credential_verifier_intermediary``) and, through the ``trust_mark_issuers`` claim of its Entity Configuration, authorizes it to issue Trust Marks to its affiliated Relying Parties.
Each affiliated Relying Party sets its ``authority_hints`` to the Intermediary and carries the Trust Mark the Intermediary issued to it.

**EUDIW.** In the EUDIW Trust Framework there is no Intermediate Entity: an Intermediary is registered as an ordinary Wallet-Relying Party (a Relying Party acting on behalf of others) and authenticates towards Wallet Units with its own WRPAC.
The intermediary relationship is expressed in the registration data rather than in a hierarchy of certificates:

  - the Intermediary's own record sets ``isIntermediary`` to ``true`` and omits ``intendedUse``, since it declares no intended use of its own;
  - each intermediated Relying Party's record references the Intermediary through the ``usesIntermediary`` field (identifier, trade name, and register URI of the Intermediary), and its WRPRC carries the ``intermediary`` structure that names the authorized Intermediary (ETSI TS 119 475, Table 10; Commission Implementing Regulation (EU) 2025/848, Annex I).

At presentation time the Wallet Instance verifies that the authenticated Intermediary is authorized to act for the intermediated Relying Party, using the ``intermediary`` structure of the WRPRC or the Register, and displays both identities to the User.
These verification rules belong to the trust-evaluation process (see :ref:`trust-evaluation-eudiw:Authorization Validation`) and are out of scope of onboarding.

Registration Summary
^^^^^^^^^^^^^^^^^^^^

The table below summarises technical registration by entity type.
Federation registration is performed by the Federation Authorities; WRP Registration is performed by the Registrar.

.. list-table:: Registration Process by Entity Type
   :class: longtable
   :widths: 24 40 36
   :header-rows: 1

   * - **Entity**
     - **Technical registration**
     - **Output**
   * - Authentic Source
     - Out of this process: its technical registration runs through PDND integration during the :ref:`onboarding-procedure:Administrative Process`.
     - Entry in the :ref:`registry:Authentic Source Registry`.
   * - Wallet Provider
     - OID Federation Registration only, with no WRP Registration.
     - Active Subordinate with a published Entity Configuration and a Trust Mark.
   * - PID / QEAA / PuB-EAA / non-qualified EAA Provider
     - OID Federation Registration, then WRP Registration in the Register.
     - Active Subordinate and a Register entry with status ``active``.
   * - Relying Party
     - OID Federation Registration, then WRP Registration in EUDIW scope, or federation only in national scope.
     - Active Subordinate and, in EUDIW scope, a Register entry.
   * - Relying Party Intermediary
     - OID Federation Registration as an Intermediate Entity, then WRP Registration with ``isIntermediary``.
     - Active Subordinate authorised for its Leaves and a Register entry.

Certificate Issuance Process
----------------------------



WRPAC Issuance
^^^^^^^^^^^^^^



WRPRC Issuance
^^^^^^^^^^^^^^



Signature/Seal Certificates
^^^^^^^^^^^^^^^^^^^^^^^^^^^



Certificate Issuance Summary
^^^^^^^^^^^^^^^^^^^^^^^^^^^^



Notification and Publication
----------------------------

Notification and Publication is the concluding process of onboarding.
It publishes a notified entity, together with the trust anchor of the technical component it operates, in the trusted list for its category.

It applies only to the notified categories (PID, QEAA, and PuB-EAA Providers, and non-qualified EAA Providers operating in EUDIW) and to the Wallet Provider.
A Wallet Provider reaches this process directly after its administrative assessment and its federation registration, without WRP registration or certificate issuance.

Notification is a Member State level process (Commission Implementing Regulation (EU) 2024/2980) for which the Supervisory Body acts as the national single point of contact toward the European Commission, while the Trusted List / LoTE Provider signs and publishes the lists.

**Input Model.**
The notifiable data collected during onboarding (identification, trust anchors, and service supply points), together with the entity's signing trust anchor produced by the certificate issuance above: for an Attestation Provider, the key with which its credential issuer signs the attestations; for a Wallet Provider, the key that signs the Wallet Unit Attestations of its Wallet Solution.

**Output Model.**
The entity's entry in the trusted list that corresponds to its category, which is what makes a notified entity trusted by the Wallet and by Relying Parties.
If publication does not complete, the entity may already hold its Register entry and its certificates but is not yet trusted for its notified category until the entry appears in the list.

**Procedure.**
The Supervisory Body notifies the entity to the European Commission, and the Trusted List / LoTE Provider signs and publishes it in the trusted list for its category:

  - a **PID Provider** is added to the PID Providers LoTE;
  - a **PuB-EAA Provider** is added to the PuB-EAA Providers LoTE;
  - a **QEAA Provider** is published on the EU Member State Trusted List (EUMS TL), whose URL is referenced in the List Of Trusted Lists (LOTL), under the eIDAS Trusted List framework;
  - a **non-qualified EAA Provider** operating in EUDIW is published in the EAA Providers LoTE; a national-only one is not placed on an EU-level trusted list, its trust anchor being distributed through the trusted list referenced by the applicable Attestation Rulebook, which is its root of trust;
  - a **Wallet Provider** is published in the Wallet Providers LoTE.

A **Relying Party** or a **Relying Party Intermediary** requires no trusted-list entry: trust in it is anchored through the signed Register and its WRPAC.
The trusted-list entry binds the organisational entity to the technical component that operates at runtime.



.. include:: ../common/common_definitions.rst
.. include:: ../common/symbols.rst

Onboarding Procedure
====================

Onboarding is the process through which an entity becomes operational and recognisable within the IT-Wallet ecosystem: it establishes the entity's legal eligibility, registers it with the competent bodies, and equips it with the trust artifacts other participants rely on to authenticate it and evaluate its authorizations.

The IT-Wallet ecosystem operates two trust models together:

- **OpenID Federation 1.0**, together with the national X.509 PKI rooted in the same Federation Trust Anchor, is the **engine of this onboarding procedure**.
  It is the mandatory, national trust model every entity onboards into, and the layer that drives identity proofing and, in turn, certificate issuance for the other model too. 
  A single OpenID Federation onboarding is what makes an entity recognisable within the ecosystem, and it yields, from one procedure, the entity's Entity Configuration, its Trust Marks, its EUDIW trust artifacts, and its signing certificates.
- The **X.509 / Trusted-List trust model** defined at EU level for Wallet-Relying Parties (`EIDAS-ARF`_, Commission Implementing Regulation (EU) 2025/848) is **additive** on top of it: it does not replace OpenID Federation and cannot exist on its own.
  It is optional, added when the entity needs to be recognised beyond the national context.
  For entities in a notified category (PID Providers, QEAA Providers, and PuB-EAA Providers) it is mandatory, and becomes the **authoritative** one for the artifacts a Wallet Instance relies on to check identity and legal value, with OpenID Federation remaining as a supplementary layer for those entities. 
  Non-qualified EAA Providers follow the EUDIW model as well, but without EU-level notification, their trust anchor being distributed through the applicable Attestation Rulebook.

Which verification mechanism a given Credential requires is not up to whoever is checking it, but is dictated by the Credential's own legal category, because that category fixes the applicable signature-verification anchor (Trusted List, LoTE, or OID-FED Trust Chain) regardless of whether the verifying party itself operates only nationally or also cross-border.

Where the two models diverge in configuration, the EUDIW model prevails, being legally binding, while OpenID Federation is functionally binding within the national ecosystem.

This section is organised around the three processes that, together, take an entity from a registration request to full operational status:

- The **Administrative Process** establishes an entity's legal standing, regulatory compliance, and eligibility to participate in the ecosystem, ahead of any technical step;
- The **Registration Process** technically registers the entity: always in the national OpenID Federation trust infrastructure, and, where the entity's category requires or opts into it, also as a EUDIW Wallet-Relying Party;
- The **Certificate Issuance Process** equips the entity with the cryptographic trust artifacts tied to its registration, again for one or both trust models depending on its category.


Overview
--------

This overview introduces the actors and system components involved in onboarding, the dual trust-model logic that shapes every onboarding decision, and the three processes an entity goes through.
The processes themselves are specified in the sections that follow; the material here is the shared frame they build on.

Entities and Components
^^^^^^^^^^^^^^^^^^^^^^^

Two families of actors take part in onboarding: the entities that are onboarded, and the trust-infrastructure entities that operate the onboarding itself.

Those trust-infrastructure roles are in turn realised by the software components of the Onboarding System, described at the end of this subsection.

**Entities being onboarded**

  - **Authentic Sources**: authoritative providers of the data that Credentials are built from.
    They follow a data-focused registration path based on PDND integration; their trust is governed by the PDND trust framework rather than by the Wallet-Relying Party model, and they are therefore outside the dual-path logic described below;
  - **Wallet-Relying Parties (WRPs)**: the umbrella category defined by Commission Implementing Regulation (EU) 2025/848 for every entity that relies on Wallet Units to provide a service.
    It is further split into:

    - **Credential Issuers**, comprising **PID Providers** and **Attestation Providers** (**QEAA Providers**, **PuB-EAA Providers**, and non-qualified **EAA Providers**).
      A PID Provider is a Credential Issuer but is **not** an Attestation Provider;
    - **Relying Parties** and **Relying Party Intermediaries**, which request Attestations from Wallet Units.
      A Relying Party operates through one or more **Relying Party Instances**.

  - **Wallet Providers**: provide the **Wallet Solution** and the **Wallet Instances** that Users install.
    A Wallet Provider is not a WRP; in the EUDIW model it follows a notification-only path (no Register entry and no Wallet-Relying Party Access Certificate), but it still onboards into the national federation.

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

- the **Onboarding UI** that orchestrates the flow;
- the **Registration Service** (the Registrar) writing to the **WRP Register**;
- the **WRPAC** and **WRPRC Issuance Services**;
- the **Signature Certificate Issuance Service**; 
- the **OID-FED Federation Service**;
- the **Publication Service** feeding the trusted lists. These operate alongside the components of the Registry Infrastructure (Claims Registry, AS Registry, Digital Credentials Catalog, Schema Registry, and Taxonomy, see :ref:`registry:Registry Infrastructure`) and, at EU level, the European Commission LoTE Provider with its Lists of Trusted Lists (LOTLs), LoTEs, and Catalogues.

The Onboarding System keeps the **WRP Register** and the **notification dataset** as two distinct data stores. 

The Register holds the WRP registration records defined by Commission Implementing Regulation (EU) 2025/848 (identification, intended use, and related data); the notification dataset holds the notifiable information defined by Commission Implementing Regulation (EU) 2024/2980 (identification, trust anchors, and service supply points).

The two overlap only in the identification data, and the infrastructure entities that are notified but not registered as WRPs (Wallet Providers, Providers of WRPAC/WRPRC, Registrars) are not present in the Register at all.

Roles and mapping
""""""""""""""""""""""""""""""""""""""""

The actors listed above correspond to the official roles defined by the EUDI Wallet Architecture and Reference Framework (`EIDAS-ARF`_) and the eIDAS2 Implementing Regulations.
The table below maps each EUDIW role onto the corresponding role in the IT-Wallet system and, where relevant, onto the OpenID Federation role the entity plays.
This mapping applies throughout this document.

.. list-table:: EUDIW Roles mapped onto IT-Wallet Roles
   :class: longtable
   :widths: 34 34 32
   :header-rows: 1

   * - **EUDIW role**
     - **IT-Wallet role**
     - **OpenID Federation role**
   * - PID Provider
     - Credential Issuer (PID Provider)
     - Leaf
   * - Attestation Provider (QEAA Provider, PuB-EAA Provider, non-qualified EAA Provider)
     - Credential Issuer
     - Leaf
   * - Relying Party (RP)
     - Relying Party
     - Leaf
   * - Relying Party Intermediary (RPI)
     - Relying Party Intermediary
     - Intermediate Entity
   * - Wallet Provider (WP)
     - Wallet Provider
     - Leaf
   * - Wallet-Relying Party (WRP), the umbrella category
     - Relying Parties, Relying Party Intermediaries, and Credential Issuers (PID and Attestation Providers)
     - Leaf (Intermediate Entity for Relying Party Intermediaries)
   * - Registrar
     - Registrar
     - -
   * - Provider of WRPAC
     - Provider of WRPAC
     - -
   * - Provider of WRPRC
     - Provider of WRPRC
     - -
   * - Trusted List / LoTE Provider
     - Trusted List / LoTE Provider
     - -
   * - Trust Anchor
     - National Trust Anchor (also root Certification Authority)
     - Trust Anchor
   * - Supervisory Body
     - Supervisory Body (Organismo di Vigilanza)
     - governance authority over the federation
   * - Wallet Unit / Wallet Instance
     - Wallet Instance
     - not a Federation Entity; trusted through the Wallet Instance Attestation
   * - Authentic Source
     - Authentic Source
     - outside the federation, under the PDND trust framework

The Dual-Path Trust Model
^^^^^^^^^^^^^^^^^^^^^^^^^^

One principle governs how the two trust models combine: the mechanism used to verify a Credential's signature is bound to the Credential's **legal category**, not to the verifier's context.

The legal category confers legal value on the Credential, and that value fixes the signature-verification anchor.

A PuB-EAA, for instance, carries the legal effect its defining regulation attaches to the category, so its signature MUST be verified through the mechanism (LoTE, Trusted List) the category mandates, whichever party verifies it.

.. plantuml:: plantuml/onboarding-system-overview.puml
    :width: 99%
    :alt: IT-Wallet onboarding system overview showing dual-path registration processes and trust infrastructure
    :caption: `IT-Wallet Onboarding System Overview. <https://www.plantuml.com/plantuml/svg/ZLJRRjj647tdLmma8AXHoqxTk7NwK4IcAC20MnkMWlH1BwFbY5vakQlkHJ9HvDyxkvG8Ch2548ObSSwPovdB9-VH-b2hp4kl2EwMao-e57buq6k3jfIwWaNZFDNmi2ExaxJFClTLwYrQhC4zOsds4RH1vQXdAMc3GVablVYfafMkINiG_8zi3xL5yHKhMlY6WriI7dMb-cwcrffzRfInCBvEJy_O4U2_3E3Ms9Bi0VjhUh9l_OpGunhTZu5HU6DF8BCMC2eq2zUiz4-M_WtaV9J2TDATZG0TaFPPTgWKHYSa7d7037fbZNgGptV9MP0mdbqNDxCF4TfvdPQrrD9vYrxk21wj4UHST0WmyBW8szX6Psp3fPLDSefb3UFYbzkY-9tntmQUdwWw-3NwXD-7kzbaNinWJYKTmDFWdusLNf9ZWPOsE0zJBVWT_0ntSH9gAYLwScShFPc0JZHKvr2ZBj7752UJbE26IXZVtiwA-UqWS2y_op46kIvYdOBQ7bYgO9pV5B_b7vE3RXX6NvuUeULHT97VFS7L-wlhoviFDorrRxT3zb2VdAoN6odGy_eu5r2BK_gpPITP8Z0RuD3J_1W3HHVYDEMfezWtAGlUEFJ14boo3gXM-hKqanydXxK1lDBzXlkriSZVWeXkZvfAlU4IXuBc2cNjuCXCKD6-6y_dywiy_uumNGp1wDZp6zYPhAH71RcbahINg1paR5McQWEXVuEv4CzKup2II-_U82pnnMXJjqYFBptOS0B-DgsoQUfGb_0Orkhm-xK9IDR1ZAOGsx3kPdoOILeTAk6UCu-hT6-M1JVs_c5vpn_5vxyMiBnlXzMhdWzEa_-oJ2WJIhvLmPejeUPXC7KjdUCC4ea4RtzwieoqvwNxCzwPFy25TIrzokHyfRa6YiS5uoIXy2xBWanWB6j6u-06CRuzYKSGxp23ZdV2zbQLIw8TsGOeNTEp8uCnpE2H_nwja-9KSlN26kScwtIaEs9Q9wOUCcWNBHelBfBH3esyKknq_qoM3gU7oiuNjwLJOgNRoBXMb5GvWjfLO5pOHhOx9jo07EmDDuCjnnpR-lPMUcA2u1eu3HHHlRCirT2JWGMIcmQSHnzu2Dw1CDfn3DAYYM3xms1kH88w6Q7IkK3mpyNr-uzmkM9KfQMkG7JtWfDc3HB3AoP41BoBkYZfdZiRHKrrRnMoZ0U25U-fiqCbepw7Uy0pjGrsQnovyyCkkkmJwJBKwdy0>`_

The table below summarises, for each notified Credential category, the registration and onboarding artifacts, the entity-authentication artifacts, and the signature-verification anchor.
For notified categories the EUDIW mechanism is authoritative, while OpenID Federation adds an optional layer.

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
       - OID-FED: Entity Configuration and Trust Mark (optional).
     -
       - EUDIW: WRPAC, LoTE.
       - OID-FED: federation Trust Chain (optional).
     - EUDIW only: trust anchor from the PID Providers LoTE.
   * - **QEAA**
     -
       - EUDIW: QTSP qualification and supervision, WRPRC / Register API, Trusted List.
       - OID-FED: Entity Configuration and Trust Mark (optional).
     -
       - EUDIW: WRPAC, LoTE.
       - OID-FED: federation Trust Chain (optional).
     - EUDIW only: trust anchor from the QEAA Provider's QTSP Trusted List.
   * - **PuB-EAA**
     -
       - EUDIW: conformity assessment (Art. 45f), notification, WRPRC / Register API, LoTE.
       - OID-FED: Entity Configuration and Trust Mark (optional).
     -
       - EUDIW: WRPAC, LoTE.
       - OID-FED: federation Trust Chain (optional).
     - EUDIW only: trust anchor from the PuB-EAA Providers LoTE.
   * - **Non-qualified EAA**
     -
       - EUDIW: WRPRC / Register API (no notification).
       - OID-FED: Entity Configuration and Trust Mark.
     -
       - EUDIW: WRPAC, where it operates in EUDIW.
       - OID-FED: Federation Entity Authentication.
     -
       - EUDIW: trust anchor defined by the Rulebook.
       - OID-FED (primary): SD-JWT VC (optionally with a JOSE ``trust_chain`` header); mDoc with an X.509 certificate chaining to the Federation Trust Anchor root, OID-FED identifier in the SAN URI.
   * - **Non-EAA (national)**
     - OID-FED: Entity Configuration and Trust Mark.
     - OID-FED: Federation Entity Authentication.
     - OID-FED: X.509 signing chain anchored to the Federation Trust Anchor.

Wallet Instances are not federation entities and are not onboarded directly: a Wallet Instance is registered indirectly, through its Wallet Provider (see :ref:`wallet-instance-registration:Wallet Instance Initialization and Registration`), and is deemed reliable through a Wallet Instance Attestation issued and signed by that Wallet Provider (see :ref:`wallet-instance-attestation-issuance:Wallet Instance Attestation Issuance`).

The Wallet MUST support both models, EUDIW because it is legally required, and OpenID Federation for functional conformance with the national trust framework.

The Onboarding Processes
^^^^^^^^^^^^^^^^^^^^^^^^

To participate in the IT-Wallet ecosystem an entity MUST perform an onboarding procedure that establishes its regulatory compliance, its authorizations, and its trust relationships.

The procedure consists of three processes, which apply differently depending on the entity type:

  1. The :ref:`onboarding-procedure:Administrative Process` validates an entity's legal standing, regulatory compliance, and organizational eligibility.
     It is performed by the Supervisory Body and applies to Authentic Sources, Wallet Providers, and WRPs;
  2. The :ref:`onboarding-procedure:Registration Process` performs technical registration.
     Every entity is registered in the national OpenID Federation infrastructure; entities whose category requires it, or that opt in for cross-border recognition, are additionally registered as EUDIW Wallet-Relying Parties in the Register;
  3. The :ref:`onboarding-procedure:Certificate Issuance Process` equips the entity with the cryptographic trust artifacts tied to its registration, for one or both trust models depending on its category.

Onboarding consumes and produces a defined set of artifacts.
The inputs depend on the entity's type and selected scope:

  - **Registration data**, for every entity registered in the Register (all WRP types), conforming to the ``WalletRelyingParty`` schema that transposes the Commission Implementing Regulation (EU) 2025/848 Annex I set;
  - **Notifiable data**, for entities published in a trusted list (PID, PuB-EAA, QEAA, and non-qualified EAA Providers, and the Wallet Provider): the identification, trust anchors, and service supply points needed for the trusted-list entry;
  - **Cryptographic material**: the public key(s) for which a WRP requests a WRPAC, generated according to ETSI TS 119 411-8, and the public keys of the signature or seal certificates the entity uses to sign or seal its artifacts.

A WRP that is also a notified entity provides both the registration data and the notifiable data; a Relying Party or Relying Party Intermediary provides only registration data, as it requires no trusted-list entry.

A successful onboarding produces the entity's Register entry (and its publication), its WRPAC, its WRPRC where mandated, and its trusted-list entry where the entity is notified.
Each entity type follows a different combination of these, summarised below.

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
     - Trusted List referenced by the Rulebook
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

The table above shows which artifacts each entity type obtains; the scope an entity selects at onboarding refines that set of outputs.
The following table summarises this for the entity types that select a scope during onboarding, using these abbreviations:

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

Relying Party Intermediaries onboard through a dedicated variant of this procedure that also grants them the authority to onboard subordinate Relying Parties, handled differently by the two trust models.
This is detailed in :ref:`onboarding-procedure:Relying Party Intermediaries`.

Onboarding Examples
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following non-normative examples show how entities onboard and connect, from the Authentic Source that provides the data to the Relying Party that consumes the resulting Credential.

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
  - **Non-qualified EAA Providers** are validated for eligibility but are not notified; their trust anchor is distributed through the applicable Rulebook.

For **Relying Parties**, the Supervisory Body performs a policy-based authorization.
It evaluates the organizational type (public administration or private entity), the business-sector classification (e.g. ATECO code), and the legitimate requirements of the service, and grants an **operational scope** defining which Credential domains and purposes the Relying Party may request.
This scope is the administrative boundary later enforced at presentation.

Relying Party Intermediaries additionally demonstrate their eligibility to act on behalf of Relying Parties, pursuant to Art. 5b(8) of the eIDAS2 Regulation (`EU_2024_1183`_).

For **Credential Issuers**, the administrative process records the Credential types the issuer intends to issue and authorizes, where needed, its integration with the relevant Authentic Sources.

Clearing the administrative process is, for every Wallet-Relying Party, the precondition for technical registration in the Register and in the federation.

Summary
^^^^^^^

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
Registration is founded on the national OpenID Federation infrastructure: every entity MUST join it, because it is what makes the entity exist and be recognisable in the national system, and it drives the rest of onboarding, including certificate issuance.
On top of this foundation, entities whose category requires it (or that opt into cross-border recognition) additionally complete EUDIW Wallet-Relying Party registration, which creates their entry in the Register.
This second step is additive, but normative: for the notified categories it is legally required, and the Register entry it produces carries the legal value on which cross-border participants rely.

Authentic Sources are outside this process: sitting outside the WRP / federation dual path, their technical registration is described under :ref:`onboarding-procedure:Administrative Process`.
Wallet Providers, which are not WRPs, complete OpenID Federation registration and are notified, but obtain no Register entry (see :ref:`onboarding-procedure:Overview`).

The certificate issuance that concludes registration (the X.509 federation certificate, and the WRPAC and WRPRC) is specified separately in the :ref:`onboarding-procedure:Certificate Issuance Process`.

OID Federation Registration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

OID Federation Registration is mandatory for every Federation Entity (Credential Issuers, Relying Parties, and Wallet Providers) and onboards it into the national trust hierarchy operated by the Federation Authorities (the National Trust Anchor and its Intermediates).
It is the foundation of onboarding: for a national-only entity it is the sole registration, and for an entity that also registers as a Wallet-Relying Party it is the layer that registration builds upon.
Its prerequisites and artifacts (the Federation Entity keys, the Entity Configuration published at ``/.well-known/openid-federation``, and the Certificate Signing Request) are specified in :ref:`trust-infrastructure:The Infrastructure of Trust` and are not restated here.

**Input.** The entity submits an onboarding request to its Federation Authority containing its Federation Entity Identifier, its Federation Entity Key in JWK format, and a X.509 Certificate Signing Request in PKCS #10 format.
The entity MUST already publish a valid Entity Configuration signed with the corresponding private key.

**Process.** The Federation Authority validates the request and the published Entity Configuration and applies the applicable metadata policy.
It then registers the entity as its Subordinate and issues the Subordinate Statement and the Trust Marks attesting the entity's role and authorizations.
The X.509 certificate that certifies the Federation Entity Key is issued in the Certificate Issuance Process, separated from the federation onboarding flow in this profile.

**Output.** The entity retrieves its Subordinate Statement and completes registration by updating its Entity Configuration with the ``authority_hints`` pointing to the Federation Authority and the ``trust_marks`` it received (see :ref:`trust-infrastructure:Subordinate Statements`).
It is then an active Subordinate, discoverable through the federation endpoints.
For a national-only entity, this Entity Configuration and Trust Mark are what make it recognisable and its authorizations verifiable.

WRP Registration
^^^^^^^^^^^^^^^^^

WRP Registration is the EUDIW step that a Wallet-Relying Party (a Relying Party, a Relying Party Intermediary, or a Credential Issuer that is a PID, QEAA, PuB-EAA, or non-qualified EAA Provider) completes on top of its federation registration.
Additive on the federation identity but normative for the notified categories, it produces the entity's entry in the Register and is the precondition for the issuance of its Wallet-Relying Party Access Certificate.

**Input.** The entity submits its registration data conforming to the ``WalletRelyingParty`` schema defined by Commission Implementing Regulation (EU) 2025/848 (Annex I, and the common data schema of the CIR 2025/848 Amendment, Annex VI).
The data covers the entity's identification and its intended use (the attributes a Relying Party intends to request from Wallet Units, or the attestation types an Attestation Provider intends to issue), together with the cryptographic material, i.e. the public key(s) for which the entity requests a WRPAC.

**Process.** The entity submits its request, through the onboarding portal, to the Registrar.
The Registrar verifies the entity's identity and eligibility (the identity proofing carried out during the Administrative Process, per ETSI TS 119 461) and, on success, creates the record in the Register with status ``active``.
The Register record is electronically signed or sealed by, or on behalf of, the Registrar, so that the certificate providers and the Wallet can rely on it.

**Output.** A Register entry with status ``active``.
This active status is the green light for the issuance of the WRPAC and, where mandated, the WRPRC (see :ref:`onboarding-procedure:Certificate Issuance Process`).

The Register and the WalletRelyingParty Schema
""""""""""""""""""""""""""""""""""""""""""""""

The Register is the national register of Wallet-Relying Parties that each Member State establishes and maintains under Commission Implementing Regulation (EU) 2025/848 (Article 3), operated by the Registrar.

It is distinct from the five components of the :ref:`registry:Registry Infrastructure`: those hold Credential semantics and discovery data (claims, schemas, catalogue, taxonomy, Authentic Sources), whereas the Register holds the WRP registration records that drive the WRPAC and WRPRC and support Relying Party authorization.

Its schema and API are therefore described here.

Each record conforms to the ``WalletRelyingParty`` schema (Commission Implementing Regulation (EU) 2025/848, Annex I, with the common data schema in Annex VI of the Amendment).
Its main fields are:

  - **Identification**: ``legalPerson`` or ``naturalPerson``, one or more ``identifier`` values from official records (with a normative type URI such as VATIN, LEI, or EUID), ``country``, and contact fields (``email``, ``phone``, ``infoURI``, ``supportURI``);
  - **Intended use** (``intendedUse``): required for entities that are not registering only as an intermediary. Each intended use carries a ``purpose``, a ``privacyPolicy``, and the machine-readable list of requested ``credential`` data (attestations and attributes);
  - **Entitlements** (``entitlement``): one or more entitlement URIs identifying the WRP role (e.g. ``Service_Provider``, ``PID_Provider``, ``QEAA_Provider``, ``PUB_EAA_Provider``, ``Non_Q_EAA_Provider``), as defined in ETSI TS 119 475, Annex A;
  - **Issued attestations** (``providesAttestations``): required when the entity is a PID Provider or an Attestation Provider, listing the attestation types it intends to issue;
  - **Intermediary references** (``usesIntermediary``, ``isIntermediary``): see :ref:`onboarding-procedure:Relying Party Intermediaries`;
  - **Governance and keys**: ``supervisoryAuthority``, ``policy`` (terms, privacy, registration policy URIs), ``registryURI``, and ``x5c`` certificate chains for the entity's services.

The Register is exposed through a single common REST API returning JSON statements signed as JWS (Commission Implementing Regulation (EU) 2025/848, Annex II).

The API allows any requestor, without prior authentication, to search and retrieve the Annex I information together with the current and historic WRPACs and WRPRCs, excluding the Annex I point 4 information.
The concrete API definition is out of scope of this document.

Relying Party Intermediaries
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A Relying Party Intermediary is a Relying Party that connects to Wallet Units and requests User attributes on behalf of other (intermediated) Relying Parties (`EIDAS-ARF`_).
Its eligibility to act on behalf of Relying Parties, pursuant to Art. 5b(8) of the eIDAS2 Regulation (`EU_2024_1183`_), is established during the Administrative Process.
Because the two trust models handle intermediation differently, an Intermediary is onboarded in both, and the way the intermediary relationship is expressed differs accordingly.

**OpenID Federation.** A Relying Party Intermediary matches an OpenID Federation Intermediate Entity.
It registers its federation keys and endpoints, publishes its own Entity Configuration, and issues Subordinate Statements for its Leaves.
Upon completion the Trust Anchor issues it an Intermediary Trust Mark (``https://<federation_authority_domain>/trust_marks/federation-entity/openid_credential_verifier_intermediary``) and, through the ``trust_mark_issuers`` claim of its Entity Configuration, authorizes it to issue Trust Marks to its affiliated Relying Parties.
Each affiliated Relying Party sets its ``authority_hints`` to the Intermediary and carries the Trust Mark the Intermediary issued to it.

**EUDIW.** In the EUDIW model there is no Intermediate Entity: an Intermediary is registered as an ordinary Wallet-Relying Party (a Relying Party acting on behalf of others) and authenticates towards Wallet Units with its own WRPAC.
The intermediary relationship is expressed in the registration data rather than in a hierarchy of certificates:

  - the Intermediary's own record sets ``isIntermediary`` to ``true`` and omits ``intendedUse``, since it declares no intended use of its own;
  - each intermediated Relying Party's record references the Intermediary through the ``usesIntermediary`` field (identifier, trade name, and register URI of the Intermediary), and its WRPRC carries the ``intermediary`` structure that names the authorized Intermediary (ETSI TS 119 475, Table 10; Commission Implementing Regulation (EU) 2025/848, Annex I).

At presentation time the Wallet Instance detects the intermediary scenario, because the entity authenticated by the WRPAC (the Intermediary) differs from the intermediated Relying Party named in the WRPRC or the Register.
It then verifies that the authenticated Intermediary is authorized to act for the intermediated Relying Party, either from the ``intermediary`` structure of the intermediated Relying Party's WRPRC or by querying the Register, and displays both identities to the User.
The presentation-time verification rules belong to the trust-evaluation process and are out of scope of onboarding.

Certificate Issuance Process
----------------------------



WRPAC Issuance
^^^^^^^^^^^^^^



WRPRC Issuance
^^^^^^^^^^^^^^



Signature/Seal Certificates
^^^^^^^^^^^^^^^^^^^^^^^^^^^



Notification and Publication
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The concluding step of onboarding publishes a notified entity, together with the trust anchor of the technical component it operates, in the appropriate trusted list.
Notification is a Member State level process (Commission Implementing Regulation (EU) 2024/2980) for which the Supervisory Body acts as the national single point of contact toward the European Commission, while the Trusted List / LoTE Provider signs and publishes the lists.

**Input.** The notifiable data collected during onboarding (identification, trust anchors, and service supply points), together with the entity's signing trust anchor produced by the certificate issuance above: for an Attestation Provider, the key with which its credential issuer signs the attestations; for a Wallet Provider, the key that signs the Wallet Unit Attestations of its Wallet Solution.

**Process and output.** The entity is published in the trusted list that corresponds to its category:

  - a **PID Provider** is added to the PID Providers LoTE;
  - a **PuB-EAA Provider** is added to the PuB-EAA Providers LoTE;
  - a **QEAA Provider** is published on the EU Member State Trusted List (EUMS TL), whose URL is referenced in the List Of Trusted Lists (LOTL), under the eIDAS Trusted List framework;
  - a **non-qualified EAA Provider** is not placed on any EU-level trusted list: its trust anchor is distributed through the trusted list referenced by the applicable Attestation Rulebook, which is its root of trust;
  - a **Wallet Provider** is published in the Wallet Providers LoTE.

A **Relying Party** or a **Relying Party Intermediary** requires no trusted-list entry: trust in it is anchored through the signed Register and its WRPAC.

The trusted-list entry binds the organisational entity to the technical component that operates at runtime, so a notified entity becomes trusted by the Wallet and by Relying Parties only once its entry is published.
If publication does not complete, the entity may already hold its Register entry and its certificates but is not yet trusted for its notified category until the entry appears in the list.



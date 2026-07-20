.. include:: ../common/common_definitions.rst
.. Included via infrastructure-trust.rst at title level '-' (level 1).

Trust Management and Lifecycle
------------------------------

This section describes first the lifecycle of Entities and Trust Artifacts (:ref:`infrastructure-trust:Lifecycle State Machine`) and then their revocation mechanisms (:ref:`infrastructure-trust:Revocation Mechanisms`).
 
Lifecycle State Machine
^^^^^^^^^^^^^^^^^^^^^^^

This section describes the lifecycle of Entities, Trust Artifacts, and the relationships between them.

Entity Lifecycle State Machine
""""""""""""""""""""""""""""""

As shown in :numref:`fig_WRP_and_Wallet_Providers_States`, WRPs and Wallet Providers have four distinct and mutually exclusive states: ``UNREGISTERED``, ``REGISTERED``, ``OPERATIONAL``, and ``REMOVED``. Each state dictates the Entity's authorization level and operational capabilities.

.. _fig_WRP_and_Wallet_Providers_States:
.. plantuml:: plantuml/wrp-wp-states.puml
    :width: 70%
    :alt: The figure illustrates the WRP and Wallet Providers States.
    :caption: `WRP and Wallet Providers States. <https://www.plantuml.com/plantuml/svg/NP91RzD048Nl-oj6FI10QhbpG0tWGYIeaPkM0-KmyOwJWVMkDJlROduzwtL8tVXWMPettxptvCkeA9fwPyoFrp_X_FmTt7gXdO7yc3nKWhFRwwRwjBxPL4tryGmm7YJb3M_XFKPox0cA_0BkVPqqiYNGFO5AYWhRaBn56I_CV-W9iid0fk1WRSahwmYKfLl7SKzsebPjY6DKwW7RbcA4dQ1Nia_C-blLh3Rh-dhrfK3hmTH3HbubvqR0fFiW_7UYBMnyhUyE7hwpxgtWepV7hsavo2EAXJ2Ge7Bm4OH-KQkpgyySDLDRT4j5ZoDi2HxGiSL9EHTQAYijprbhlmsPpNu7Bvvotv5mnsr1cUQmK8AiOqpeMuBGmQOKknBb3bkDEUa2V384-ZEmaCr-Wu3GG_XD5cmYq03LV3KDazDuFBZeO89or3bSMP_DbPidqW_2MjguGdP92Dv0tNN7cFV-vNDl2zohHUyJDl-HKnIIddq6tYWg6ND9tgRU_GC0>`_

**Transition from UNREGISTERED to REGISTERED**: 

- ``UNREGISTERED``: Indicates that an Entity does not currently hold a valid subscription or registration within the IT Wallet ecosystem. This is the default baseline state. Entities in this state are outside the trust boundary and MUST NOT participate in any operations.
- ``REGISTERED``: Indicates that an Entity has successfully completed the onboarding process and its identity has been verified. 

  - *EUDIW Trust Framework*: WRPs are in ``REGISTERED`` state when their Entity information has been added to the WRP Register, while Wallet Providers become ``REGISTERED`` when the certification and onboarding records have been successfully collected and verified.
  - *National Trust Framework*: WRPs and Wallet Providers are in ``REGISTERED`` state when the onboarding records have been successfully collected and verified.

**Transition from REGISTERED to OPERATIONAL**:  ``OPERATIONAL`` indicates that an Entity has been successfully authorized to perform role-related operations. 

  - *EUDIW Trust Framework*: WRPs are in ``OPERATIONAL`` state if they were in ``REGISTERED`` state and they obtained a WRPAC, optionally a WRPRC and, based on the role, a signing/seal certificate. The signing Trust Anchor of that certificate MUST have been added in the LoTE or in the EUMS TL. Wallet Providers are in ``OPERATIONAL`` state if they were in ``REGISTERED`` state and they obtained a signing/seal certificate whose signing Trust Anchor has been added in the LoTE.
  - *National Trust Framework*: WRPs and Wallet Providers are in ``OPERATIONAL`` state if they were in ``REGISTERED`` state, they have obtained the signing/seal certificate(s) and the Trust Mark(s), and their Subordinate Statement has been published by the Federation Authority.

**Transition from OPERATIONAL to REGISTERED**: an Entity goes back to ``REGISTERED`` state when it no longer possesses valid Trust Artifacts. This can be triggered by their expiration or by their revocation following an update of the Entity. To return to the ``OPERATIONAL`` state, a new Trust Artifact issuance is required.

**Transition from REGISTERED or OPERATIONAL to REMOVED**: ``REMOVED`` indicates the removal of an Entity due to voluntary offboarding, a severe security breach, or a critical compliance failure.

  - *EUDIW Trust Framework*: for WRPs it results in the revocation of the WRPAC/WRPRC and of the signing/seal certificates, in the removal of the entry from the WRP Register and in the update of the status of the signing Trust Anchor in the LoTE or in the EUMS TL. For Wallet Providers it results in the update of the Wallet Providers LoTE.
  - *National Trust Framework*:  for both WRPs and Wallet Providers it results in the removal of the Subordinate Statement, related Trust Mark and revocation of the signing/seal certificates.

An Entity MUST reject new interactions or transactions initiated by a ``REMOVED`` Entity, and all cryptographic keys, active attestations, and operational capabilities associated with the Entity MUST be immediately revoked.
However, Entities MAY continue to validate historical data, signatures, and Attestations generated prior to the removal timestamp, subject to local risk policies. 

Removal events are categorized based on their initiation source:

- Voluntary Exit: Entities MAY choose to exit the federation for standard business or operational reasons (e.g., organizational restructuring, mergers, acquisitions, or complete service discontinuation).
- Supervisory Body Removal: The Supervisory Body MAY initiate a forced removal due to severe compliance failures, fatal security breaches, or other critical ecosystem threats.

.. note::
  Authentic Sources and Trust-infrastructure Entities (e.g., Registrar and Providers of WRPAC) lifecycle are out of scope of this specification. The former follows the PDND framework, the latter has an ad hoc registration path not detailed in this specification.

Trust Artifacts Lifecycle State Machine
"""""""""""""""""""""""""""""""""""""""

State Machines for Trust Artifacts are described below:

- For WRPAC, WRPRC and signing/seal certificates, the lifecycle states are ``VALID`` and ``REVOKED``. The transition from ``VALID`` to ``REVOKED`` is triggered by the revocation of the Trust Artifact, which can be initiated by the corresponding Trust Artifact provider due to various reasons such as key compromise, organizational changes, or non-compliance with framework policies. Once a Trust Artifact is in the ``REVOKED`` state, it MUST NOT be trusted for any operational use within the ecosystem, and any Entity relying on it MUST reject it for authentication, authorization, or any other trust-related operations.
  
  - A WRPAC in ``VALID`` state MUST NOT be present in the designated CRL and/or SHALL return a ``good`` status in the OCSP response. A WRPAC in ``REVOKED`` state MUST be present in the designated CRL and/or MUST return a ``revoked`` status in the OCSP response.
  - A WRPRC in ``VALID`` state MUST return a ``0x00`` status in the corresponding Status List Token. A WRPRC in ``REVOKED`` state MUST have status value ``0x01`` within the corresponding Status List Token.
- For Trust Lists (LoTE, LOTL, EUMS TL), the lifecycle states are ``CURRENT`` and ``HISTORICAL``. The transition from ``CURRENT`` to ``HISTORICAL`` is triggered by the publication of a new version of the Trust List that replaces the previous version. Once a Trust List is in the ``HISTORICAL`` state, it MUST NOT be used for any operational use within the ecosystem. Two exceptions apply: the validation of Trust List trustworthiness via the pivoting mechanism, and the validation of historical operations via the ``ServiceHistory`` component of the Trust List.
- Trust Marks: the status of a Trust Mark are ``ACTIVE``, ``EXPIRED``, ``REVOKED``. The status can be checked using the Trust Mark Status endpoint (see Section 8.4 of `OID-FED`_).

.. note:: 
  Register, Entity Configurations and Subordinate Statements are simply published or unpublished. During their publication they can be updated. 

The diagram :numref:`fig_Trust_Artifacts_States` highlights the state machine of the aforementioned Trust Artifacts:

.. _fig_Trust_Artifacts_States:
.. plantuml:: plantuml/trust-artifacts-states.puml
    :width: 90%
    :caption: `Trust Artifacts States. <https://www.plantuml.com/plantuml/svg/PL5TRzCm57tFhpZQquOwyRu7j2eBB29RgyGK942Rbzmr5aaSNTk52l7ViLENj28lbdFl-JZ7jyPAjgxlabOr1Ef7kqT3fcOrMgM79F4Bbd2H4blrgcf_CRZyNAwNwGB-AFrHgUqWhMDwMv7ihYuW3SB-1zPknEy4mDSttt5z_GwRPP7VuGQvCKuEDVbP_1UcPRPPVSp2lAIThcLm0C5gkoN6j-4oBOi5LccrNa0pAkj53Gfbx5K2HFI1AUZTG13tQf3Tj4h9dtzf13jZ9wGFKsYHBL2iX2SNnMJVdxFvsRqedj9FPPaz2a--TY-TYXxrArB7J8F5XjY4uW8kgaLC93vI98XV0fmo1w7xl1AhCa-NXHUgtEWvgQ46Btiyqi-ZHgX4j0JTDT03GHb8hbkryvjMuxaYtgcQxdrCpVldKD8fS-pflreU9Fym1xCFnnQIEKsiEIuynUlf8ozJaM-o-P4XXmRZULqIivZ7Him4pxwiypAxkq78Hhz6nGUKLVsKaKdMBJNdgDbA1BwdXY9mwMohMTczBuofrrC_BPqxE24uRUQMXiRrtLy0>`_


Entities Updates and Their Effects on Trust Artifacts 
"""""""""""""""""""""""""""""""""""""""""""""""""""""

Entities are characterized by three main categories of registered data:

- *Identity Information*: This includes the organization's name, contact information, and organizational policies.
- *Technical Configuration*: This includes the cryptographic materials (signature/seal keys, authentication keys) and technical endpoints necessary for ecosystem interactions.
- *Authorization Information*: This includes the Entity's entitlements, Attestation provision capabilities, Attestation request capabilities, Intermediary use permissions, intended use cases, EDPs, and compliance with certification schemas.

While in the ``OPERATIONAL`` state, Entities MAY require organizational updates to their registered data. The Trust Framework infrastructure MUST propagate these changes to the relevant Trust Artifacts. The specific operational effects depend on the Entity's role and the Trust Artifacts it utilizes.
Below these updates and their operational effects on the Trust Artifacts state are described.

**Registered Data and Associated Trust Artifact**

In the tables below are found the relationships between the registered data and the Trust Artifacts in which they are contained for specific entity types.

.. list-table:: Entity Data and Trust Artifacts
   :class: longtable
   :widths: 16 18 22 22 22
   :header-rows: 1

   * - Entity Type
     - Data Category
     - Common Trust Artifacts
     - EUDIW Trust Artifacts
     - National Trust Artifacts

   * - WRP (all)
     - Identity Information 
     - n/a
     - Register, WRPAC, WRPRC, LoTE (only for PID, PubEAA and notified non-qualified EAA Provider)
     - Entity Configuration, Trust Mark

   * - WRP (all)
     - Technical Configuration (Authentication key)
     - n/a
     - WRPAC
     - Entity Configuration, Subordinate Statement

   * - WRP (all)
     - Authorization Information (Entitlements, Intermediary,	Service descriptions, Supervision information)
     - n/a
     - Register, WRPRC, LoTE (only for PID, PubEAA and notified non-qualified EAA Provider)
     - Entity Configuration, Trust Mark

   * - Credential Issuer or Wallet Provider
     - Technical Configuration (Signature/Seal key)
     - X.509 Signature/Seal Certificate
     - n/a
     - n/a

   * - Credential Issuer or Wallet Provider
     - Technical Configuration (Signature/Seal Trust Anchor)
     - n/a
     - LoTE
     - Trust Anchor Entity Configuration

   * - Credential Issuer
     - Authorization Information (RP permissions)
     - n/a
     - EDP in the Credential Issuer metadata
     - n/a

   * - Credential Issuer
     - Authorization Information (Attestation provision capabilities)
     - n/a
     - Register, WRPRC
     - Subordinate Statement, Trust Mark

   * - Relying Party or Relying Party Intermediary
     - Authorization Information (Attestation request capabilities)
     - n/a
     - Register, WRPRC
     - Subordinate Statement, Trust Mark

   * - Wallet Provider
     - Identity Information 
     - n/a
     - LoTE 
     - Entity Configuration, Trust Mark

   * - Wallet Provider
     - Authorization Information (Service status)
     - n/a
     - LoTE
     - Subordinate Statement, Trust Mark


.. note::
  The inclusion of Wallet Providers and Credential Issuers in the LoTE is an implicit assertion of their role and authorization within the ecosystem. In particular, their inclusion is a result of the succesful completion of the registration and notification procedures as defined in `CIR2025/848`_ (registration of WRP) and `CIR2024/2980`_ (notifications of WRP and Wallet Provider).
  Similarly, the possibility to fetch a Subordinate Statement of an Entity means that the Entity is currently part of the ecosystem.

.. note::
  QEAAs are provided by Qualified Trust Service Providers (QTSPs). Their identity/technical/authorization information are available in dedicated EUMS TL.

  Identity/technical/authorization information for Registrars, Providers of WRPAC, Providers of WRPRC are available in dedicated LoTE.
  

**Wallet-Relying Party Updates**

For WRP updating their identity information, technical configurations, and/or authorizations, the update MUST trigger the following procedures.

*Identity Information and Authorizations Updates*

- *EUDIW Trust Framework*: 

  - **Registry Update**: the Registrar MUST update the WRP information within the Register.
  - **WRPAC Revocation and Re-issuance**: The Provider of WRPAC MUST revoke the Entity's current WRPAC. Revocation MUST be executed by appending the certificate's serial number to the active CRL or by returning a revoked status in the OCSP response. The Provider of WRPAC MUST issue a new WRPAC with the updated data.
  - **WRPRC Revocation and Re-Issuance**: The Provider of WRPRC MUST revoke the Entity's current WRPRC if present. Revocation MUST be executed by setting the status value of the WRPRC within the corresponding Status List Token to 0x01. The Provider of WRPRC MUST issue a new WRPRC with the updated data if required.
  - **LoTE Update** [ONLY for PID and Pub-EAA Providers]: the LoTE Provider MUST be notified with the updates, it will then publish a new version of the LoTE with the updated ``ServiceInformation`` component using the pivoting mechanism with the PID/PuB-EAA Provider's updated information.

- *National Trust Framework*: 

  - **Entity Configuration Update**: The Entity MUST update the WRP information within its Entity Configuration.
  - **Trust Mark Revocation and Re-Issuance**: The Federation Authority MUST revoke the Trust Mark and issue a new one with the updated information. 

*Technical Configurations Updates*

- **Signature/Seal Key update:**  the WRP MUST notify signature/seal key updates to the Certificate Authority responsible for the issuance of these certificates.

  - *Common*: 

    - **Signature/Seal Certificate Revocation and Re-issuance**: The Certificate Authority MUST revoke the Entity's current signature/seal certificate. The Certificate Authority MUST issue a new signature/seal certificate with the updated key.

  - *EUDIW Trust Framework*: 
  
    - **LoTE Update** [ONLY for PID and Pub-EAA Providers]: Upon obtaining a new signature/seal certificate with the updated key the LoTE Provider MUST be notified, which will then publish a new version of the LoTE with the updated ``ServiceInformation`` component using the pivoting mechanism with the updated Signature/Seal certificate.

- **Authentication Key update:** 

  - *EUDIW Trust Framework*: The WRP MUST notify WRPAC key updates to the Provider of WRPAC

    - **WRPAC Revocation and Re-issuance**: The Provider of WRPAC MUST revoke the Entity's current WRPAC. Revocation MUST be executed by appending the certificate's serial number to the active CRL or by returning a revoked status in the OCSP response. The Provider of WRPAC MUST issue a new WRPAC with the updated key.

  - *National Trust Framework*: 

    - **Entity Configuration Update**: The Entity MUST update its Entity Configuration.
    - **Subordinate Statement Update**: The Federation Authority MUST update the Subordinate Statement of the updated Entity.

**Wallet Provider Updates**

For Wallet Providers updating their identity information and/or technical configurations, the update MUST trigger the following procedures:

*Identity Information Updates*

- *EUDIW Trust Framework*: 

  - **LoTE Update**: the LoTE Provider MUST be notified with the updates, which will then publish a new version of the LoTE with the updated ``ServiceInformation`` component using the pivoting mechanism with the Wallet Provider's updated information.

- *National Trust Framework*: 

  - **Entity Configuration Update**: The Wallet Provider MUST update its Entity Configuration.
  - **Trust Mark Revocation and Re-Issuance**: The Federation Authority MUST revoke the Trust Mark and issue a new one with the updated information. 

*Technical Configurations Updates*

- **Signature/Seal Key update:** the Wallet Provider MUST notify signature/seal key updates to the Certificate Authority responsible for the issuance of these certificates.

  - *Common*: 

    - **Signature/Seal Certificate Revocation and Re-issuance**: The Certificate Authority MUST revoke the Entity's current signature/seal certificate. The Certificate Authority MUST issue a new signature/seal certificate with the updated key.

  - *EUDIW Trust Framework*: 

    - **LoTE Update** [ONLY for Trust Anchor certificates]: Upon obtaining a new signature/seal certificate with the updated key the LoTE Provider MUST be notified, which will then publish a new version of the LoTE with the updated ``ServiceInformation`` component using the pivoting mechanism with the entity's updated Signature/Seal certificate.

Revocation Mechanisms
^^^^^^^^^^^^^^^^^^^^^

This section describes the artifacts that are employed in :ref:`infrastructure-trust:Trust Management and Lifecycle` to manage the status of certificates and entities by detailing respective formats and parameters. The main distinction is the following:

- To manage Wallet-Relying Party Access Certificates and Sign/Seal Certificates, the entities acting as Trust Anchors for these certificates MUST:

  - make available at least one revocation mechanism among :ref:`infrastructure-trust:Certificate Revocation List (CRL)` and :ref:`infrastructure-trust:Online Certificate Status Protocol (OCSP)`;
  - issue WRPACs and Sign/Seal Certificates with at least an extension corresponding to the provided revocation mechanism.

- To manage Wallet-Relying Party Registration Certificates, each Provider of Wallet Relying Party Registration Certificates MUST:

  - make available an endpoint to request :ref:`infrastructure-trust:Status List Token (SLT)`;
  - issue WRPRCs with the appropriate parameter ``status`` as described in :ref:`infrastructure-trust:Wallet-Relying Party Registration Certificate (WRPRC) Profile`.

.. note::
  ETSI 319 411-1 v1.5.1 recommends the support of OCSP, see clause CSS-6.3.10-06 and Note 2.

Certificate Revocation List (CRL)
"""""""""""""""""""""""""""""""""

**Certificate Revocation Lists (CRLs)** are used to check the revocation status of an X509 certificate. A CRL is a digitally signed list of revoked certificates that have been issued by a CA. The CRL is published and made available to any entity via a publicly accessible URI. The CRL MUST be digitally signed by the **CRL issuer**.

CRLs MAY be used for the following types of certificates:

- Wallet Relying Party Access Certificates by including the ``cRLDistributionPoints`` extension in the certificate, as described in `:ref:trust-artifact-eudiw:Wallet-Relying Party Access Certificate`.
- Sign/Seal certificates by including the ``cRLDistributionPoints`` extension in the certificate, as described in `:ref:trust-artifact-eudiw:Sign/Seal Certificate`.

If a CRL is used to manage the status of the certificates, the CRL issuer MUST be the entity referenced in the Trust Anchor certificate ``subject`` field. 

The CRL issuer MAY also generate delta CRLs. A delta CRL only lists those certificates, within its scope, whose revocation status has changed since the issuance of a referenced complete CRL. The referenced complete CRL is referred to as a base CRL. The scope of a delta CRL MUST be the same as the base CRL that it references.

If supported by the CA, the CRL MUST be available at the URI specified in the ``cRLDistributionPoints.distributionPoint`` *[0] CHOICE* structure within the Wallet Relying Party Access Certificate (WRPAC).

An X.509 v2 CRL is represented as the ASN.1 DER encoding of the ``CertificateList`` SEQUENCE. The ASN.1 DER encoding is a strictly defined tag, length, and value encoding system for each element. The final bytes transmitted represent the DER encoding of the top-level SEQUENCE containing the fields in the following table:

.. list-table:: Top-Level CertificateList Structure
   :class: longtable
   :widths: 22 18 10 15 35
   :header-rows: 1

   * - Parameter
     - Defined in
     - Presence
     - Format
     - Description
   * - ``tbsCertList``
     - :rfc:`5280`, clause 5.1.1.1
     - REQUIRED
     - *SEQUENCE*
     - Contains the core CRL information including the name of the issuer, issue date, next update date, the optional list of revoked certificates, and optional CRL extensions.
   * - ``signatureAlgorithm``
     - :rfc:`5280`, clause 5.1.1.2
     - REQUIRED
     - *SEQUENCE*
     - Contains the algorithm identifier for the algorithm used by the CRL issuer to sign the ``CertificateList``. Selection SHOULD align with relevant standards (e.g., [ETSI TS 119 312]).
   * - ``signatureAlgorithm.algorithm``
     - [:rfc:`5280`, clause 4.1.1.2]
     - REQUIRED
     - *OBJECT IDENTIFIER*
     - The OID of the signature algorithm.
   * - ``signatureAlgorithm.parameters``
     - [:rfc:`5280`, clause 4.1.1.2]
     - OPTIONAL
     - *ANY*
     - Algorithm-specific parameters, dependent on the signature algorithm used.
   * - ``signatureValue``
     - [:rfc:`5280`, clause 5.1.1.3]
     - REQUIRED
     - *BIT STRING*
     - Contains the digital signature computed upon the ASN.1 DER encoded ``tbsCertList``.

Certificate List Content
.........................

The ``tbsCertList`` (To Be Signed Certificate List) is an ASN.1 SEQUENCE containing several fields and extensions. The following table lists all such fields and extensions that are required in a CRL or conditionally required.

.. list-table:: tbsCertList Fields and Extensions
   :class: longtable
   :widths: 22 18 10 15 35
   :header-rows: 1

   * - Parameter
     - Defined in
     - Presence
     - Format
     - Description
   * - ``version``
     - [:rfc:`5280`, clause 5.1.2.1]
     - OPTIONAL
     - *INTEGER*
     - Describes the version of the encoded CRL. When extensions are used (as is standard practice), this field MUST be present and MUST specify version 2 (the integer value is ``1``).
   * - ``signature``
     - [:rfc:`5280`, clause 5.1.2.2]
     - REQUIRED
     - *SEQUENCE*
     - The algorithm identifier for the algorithm used to sign the CRL.
   * - ``signature.algorithm``
     - [:rfc:`5280`, clause 4.1.1.2]
     - REQUIRED
     - *OBJECT IDENTIFIER*
     - The OID of the signature algorithm. MUST match the ``signatureAlgorithm`` field in the parent ``CertificateList`` sequence.
   * - ``signature.parameters``
     - [:rfc:`5280`, clause 4.1.1.2]
     - OPTIONAL
     - *ANY*
     - Algorithm-specific parameters, dependent on the algorithm used.
   * - ``issuer``
     - [:rfc:`5280`, clause 5.1.2.3]
     - REQUIRED
     - *Name*
     - Identifies the entity that has signed and issued the CRL. It MUST contain a non-empty X.500 distinguished name (DN) composed of ``AttributeType`` (OID) and ``AttributeValue`` sequences.
   * - ``thisUpdate``
     - [:rfc:`5280`, clause 5.1.2.4]
     - REQUIRED
     - *UTCTime* or *GeneralizedTime*
     - Indicates the issue date of this CRL. Dates through 2049 MUST use ``UTCTime``; dates in 2050 or later MUST use ``GeneralizedTime``.
   * - ``nextUpdate``
     - [:rfc:`5280`, clause 5.1.2.5]
     - REQUIRED
     - *UTCTime* or *GeneralizedTime*
     - Indicates the date by which the next CRL will be issued. Dates through 2049 MUST use ``UTCTime``; dates in 2050 or later MUST use ``GeneralizedTime``.
   * - ``revokedCertificates``
     - [:rfc:`5280`, clause 5.1.2.6]
     - OPTIONAL
     - *SEQUENCE OF*
     - A sequence of revoked certificates. When there are no revoked certificates, this field MUST be absent.
   * - ``revokedCertificates.userCertificate``
     - [:rfc:`5280`, clause 5.1.2.6]
     - REQUIRED
     - *INTEGER*
     - The ``CertificateSerialNumber`` of the revoked certificate.
   * - ``revokedCertificates.revocationDate``
     - [:rfc:`5280`, clause 5.1.2.6]
     - REQUIRED
     - *UTCTime* or *GeneralizedTime*
     - The date on which the revocation occurred.
   * - ``revokedCertificates.crlEntryExtensions``
     - [:rfc:`5280`, clause 5.1.2.6]
     - OPTIONAL
     - *SEQUENCE OF*
     - Extensions specific to this revoked certificate entry. If present, the CRL ``version`` MUST be ``v2``.
   * - ``crlExtensions``
     - [:rfc:`5280`, clause 5.1.2.7]
     - OPTIONAL
     - *[0] EXPLICIT SEQUENCE OF*
     - A sequence of one or more CRL extensions. If present, the CRL ``version`` MUST be ``v2``.

The ``crlExtensions`` field MAY contain various extensions. Notable standard extensions include:

.. list-table:: Notable crlExtensions
   :class: longtable
   :widths: 25 15 15 10 35
   :header-rows: 1

   * - Parameter
     - Defined in
     - Presence
     - Format
     - Description
   * - ``authorityKeyIdentifier``
     - [RFC 5280, clause 5.2.1]
     - REQUIRED
     - *SEQUENCE*
     - Provides a means of identifying the public key corresponding to the private key used to sign the CRL. Contains ``keyIdentifier`` (OCTET STRING), ``authorityCertIssuer``, or ``authorityCertSerialNumber``.
   * - ``cRLNumber``
     - [RFC 5280, clause 5.2.3]
     - REQUIRED
     - *INTEGER*
     - A non-critical extension conveying a monotonically increasing sequence number for a given CRL scope and issuer. Both base CRLs and delta CRLs share the same monotonically increasing sequence; the delta CRL's number MUST be greater than the base CRL's number it references.
   * - ``deltaCRLIndicator``
     - [RFC 5280, clause 5.2.4]
     - REQUIRED for delta CRLs; MUST NOT appear in base CRLs
     - *INTEGER* (``BaseCRLNumber``)
     - A **critical** extension that marks the CRL as a delta CRL and identifies the base CRL it is relative to. The integer value is the ``cRLNumber`` of the base CRL on which this delta is built. A relying party that does not understand this extension MUST reject the CRL. The base CRL MUST still be reachable (cached or retrievable) for the delta to be useful. If this extension is absent, the CRL is a full (base) CRL.
   * - ``freshestCRL`` (a.k.a. *CRL Distribution Points* on a CRL)
     - [RFC 5280, clause 5.2.6]
     - OPTIONAL; RECOMMENDED on base CRLs in deployments that issue delta CRLs
     - *SEQUENCE OF DistributionPointName*
     - A non-critical extension indicating where the most recently issued delta CRL for the same scope can be retrieved. Each ``DistributionPointName`` carries one or more URIs (typically ``uniformResourceIdentifier``). When present on a base CRL, it MUST point to the delta CRL distribution location; when present on a delta CRL, it points to the next delta CRL. A relying party uses this to discover deltas without additional out-of-band configuration.
   * - ``issuingDistributionPoint``
     - [RFC 5280, clause 5.2.5]
     - OPTIONAL; REQUIRED when the CRL scope is restricted (e.g., only-CA, only-end-entity, only-some-reasons) or when the CRL is indirect
     - *SEQUENCE* (``IssuingDistributionPoint``)
     - A **critical** extension describing the scope of the CRL. Contains flags ``distributionPoint``, ``onlyContainsUserCerts``, ``onlyContainsCACerts``, ``onlySomeReasons``, ``indirectCRL``, and ``onlyContainsAttributeCerts``. For delta-CRL deployments, the ``indirectCRL`` bit is set to TRUE when the delta is signed by a CRL issuer other than the Certificate Authority that issued the certificates (common when a delegated revocation service is used), and ``onlySomeReasons`` MAY restrict the delta CRL to specific revocation reasons (e.g., ``keyCompromise`` only). The base CRL and corresponding delta CRLs MUST share the same scope (same ``onlyContains*`` flags and ``distributionPoint``).


Online Certificate Status Protocol (OCSP)
""""""""""""""""""""""""""""""""""""""""""""

The Online Certificate Status Protocol (OCSP) (:rfc:`6960`) enables applications to determine the exact revocation state of identified certificates. It provides more timely revocation information than is typically possible with CRLs and MAY also be used to obtain additional status information.

An OCSP client issues a status request to an OCSP responder and MUST suspend the acceptance of the certificates in question until the responder provides a valid response.

If supported by the Certificate Authority, the URI to which the OCSP Responder can be invoked MUST be present in the ``authorityInfoAccess.accessLocation`` extension of the Wallet Relying Party Access Certificate (WRPAC).

This protocol specifies the data that MUST be exchanged between the OCSP client (which checks the status of one or more certificates) and the OCSP server (which provides the corresponding status). 

The following table sums up the roles of the OCSP client and server in the EUDIW ecosystem.

.. list-table:: OCSP roles in the EUDIW ecosystem
   :class: longtable
   :widths: 28 28 44
   :header-rows: 1

   * - OCSP Client
     - OCSP Server
     - Use case
   * - Wallet Unit
     - WRPAC Provider
     - WRPAC Status Check
   * - Wallet Unit or Relying Party 
     - PID Provider Trust Anchor
     - PID Sign/Seal Certificate Status Check
   * - Wallet Unit or Relying Party 
     - PuB-EAA Provider Trust Anchor
     - PuB-EAA Sign/Seal Certificate Status Check
   * - Wallet Unit or Relying Party 
     - (Q)EAA Provider Trust Anchor
     - (Q)EAA Sign/Seal Certificate Status Check

.. note:: 
    The Status check on Sign/Seal Certificates is needed only in case the Sign/Seal Certificate is not referenced directly as a Trust Anchor Certificate, in which case it is trusted a priori and does not need a separate status check.

Online Certificate Status Protocol Request Format
....................................................

The OCSP request MUST be the ASN.1 DER encoding of the ``OCSPRequest`` SEQUENCE, which contains the ``tbsRequest`` (To-Be-Signed Request) and an optional signature. The following table lists the parameters found within the ``tbsRequest`` structure.

.. list-table:: tbsRequest Structure Parameters
   :class: longtable
   :widths: 22 18 10 15 35
   :header-rows: 1

   * - Parameter
     - Defined in
     - Presence
     - Format
     - Description
   * - ``version``
     - [:rfc:`6960`, clause 4.1.1]
     - OPTIONAL
     - *[0] EXPLICIT INTEGER*
     - Indicates the version of the protocol. If omitted, the default value is ``v1`` (0).
   * - ``requestList``
     - [:rfc:`6960`, clause 4.1.1]
     - REQUIRED
     - *SEQUENCE OF*
     - Contains one or more single certificate status requests.
   * - ``requestList.reqCert``
     - [:rfc:`6960`, clause 4.1.1]
     - REQUIRED
     - *SEQUENCE*
     - The ``CertID`` structure carrying the identifier of a target certificate.
   * - ``requestList.singleRequestExtensions``
     - [:rfc:`6960`, clause 4.1.1]
     - OPTIONAL
     - *[0] EXPLICIT SEQUENCE*
     - Includes extensions applicable to this single certificate status request.
   * - ``requestExtensions``
     - [:rfc:`6960`, clause 4.1.1]
     - OPTIONAL
     - *[2] EXPLICIT SEQUENCE*
     - Includes extensions applicable to the overall requests found within the ``requestList``.

The ``reqCert`` parameter utilizes the ``CertID`` structure, MUST be an ASN.1 *SEQUENCE* containing the following parameters:

.. list-table:: CertID Structure Parameters
   :class: longtable
   :widths: 22 18 10 15 35
   :header-rows: 1

   * - Parameter
     - Defined in
     - Presence
     - Format
     - Description
   * - ``hashAlgorithm``
     - [:rfc:`6960`, clause 4.1.1]
     - REQUIRED
     - *SEQUENCE*
     - Identifies the hash algorithm used to generate the issuer name and key hashes.
   * - ``hashAlgorithm.algorithm``
     - [:rfc:`6960`, clause 4.1.1]
     - REQUIRED
     - *OBJECT IDENTIFIER*
     - The OID of the hash function (e.g., SHA-256, depending on the profile).
   * - ``hashAlgorithm.parameters``
     - [:rfc:`6960`, clause 4.1.1]
     - OPTIONAL
     - *ANY*
     - Algorithm-specific parameters, dependent on the hash algorithm used.
   * - ``issuerNameHash``
     - [:rfc:`6960`, clause 4.1.1]
     - REQUIRED
     - *OCTET STRING*
     - The hash of the issuer's distinguished name (DN), calculated over the DER encoding of the issuer's name field.
   * - ``issuerKeyHash``
     - [:rfc:`6960`, clause 4.1.1]
     - REQUIRED
     - *OCTET STRING*
     - The hash of the issuer's public key, calculated over the value (excluding tag and length) of the subject public key field.
   * - ``serialNumber``
     - [:rfc:`6960`, clause 4.1.1]
     - REQUIRED
     - *INTEGER*
     - The serial number of the target certificate for which the status is being requested.

The ``requestExtensions`` and ``singleRequestExtensions`` structures MAY contain various extensions. The following table lists the requested ones:

.. list-table:: OCSP Nonce Extension
   :class: longtable
   :widths: 22 18 10 15 35
   :header-rows: 1

   * - Parameter
     - Defined in
     - Presence
     - Format
     - Description
   * - ``nonce``
     - [:rfc:`6960`, clause 4.4.1]
     - REQUIRED
     - *OCTET STRING*
     - Cryptographically fresh value used to bind a request and a response to prevent replay attacks. Identifier OID is ``id-pkix-ocsp-nonce``.

When sent over HTTP using POST, the body of this request MUST contain the raw DER encoding of this ``OCSPRequest`` SEQUENCE and MUST have MIME type ``application/ocsp-request``.

Below is a non-normative example of an OCSP request:

.. literalinclude:: ../../examples/ocsp-request.txt
  :language: text

Online Certificate Status Protocol Response Format
...................................................

An OCSP response MUST be the ASN.1 DER encoding of the ``OCSPResponse`` *SEQUENCE*. When transported over HTTP, the body of the HTTP response MUST contain the raw DER encoding of this ``OCSPResponse``, with the MIME type ``application/ocsp-response``. The ``OCSPResponse`` *SEQUENCE* contains the following parameters:

.. list-table:: OCSPResponse Structure Parameters
   :class: longtable
   :widths: 22 18 10 15 35
   :header-rows: 1

   * - Parameter
     - Defined in
     - Presence
     - Format
     - Description
   * - ``responseStatus``
     - [:rfc:`6960`, clause 4.2.1]
     - REQUIRED
     - *ENUMERATED*
     - Indicates the processing status of the prior request. Supported values are: ``successful`` (0), ``malformedRequest`` (1), ``internalError`` (2), ``tryLater`` (3), ``sigRequired`` (5), and ``unauthorized`` (6).
   * - ``responseBytes``
     - [:rfc:`6960`, clause 4.2.1]
     - OPTIONAL
     - *[0] EXPLICIT SEQUENCE*
     - Present only when the ``responseStatus`` is ``successful`` (0). Contains the response type and the encoded response data.
   * - ``responseBytes.responseType``
     - [:rfc:`6960`, clause 4.2.1]
     - REQUIRED
     - *OBJECT IDENTIFIER*
     - Identifier for the response type. For a basic OCSP responder, this value MUST be ``id-pkix-ocsp-basic``.
   * - ``responseBytes.response``
     - [:rfc:`6960`, clause 4.2.1]
     - REQUIRED
     - *OCTET STRING*
     - Contains the DER encoding of the response syntax identified by ``responseType`` (e.g., the ``BasicOCSPResponse`` structure).

.. note::
   OCSP responders MUST be capable of producing responses of the ``id-pkix-ocsp-basic`` response type. Correspondingly, OCSP clients MUST be capable of receiving and processing responses of the ``id-pkix-ocsp-basic`` response type.

``BasicOCSPResponse`` is an ASN.1 SEQUENCE containing the following parameters:

.. list-table:: BasicOCSPResponse Structure Parameters
   :class: longtable
   :widths: 22 18 10 15 35
   :header-rows: 1

   * - Parameter
     - Defined in
     - Presence
     - Format
     - Description
   * - ``tbsResponseData``
     - [:rfc:`6960`, clause 4.2.1]
     - REQUIRED
     - *SEQUENCE*
     - Contains the core response data to be signed by the responder.
   * - ``tbsResponseData.version``
     - [:rfc:`6960`, clause 4.2.1]
     - OPTIONAL
     - *[0] EXPLICIT INTEGER*
     - The version of the response syntax. If omitted, the default value is ``v1`` (0).
   * - ``tbsResponseData.responderID``
     - [:rfc:`6960`, clause 4.2.1]
     - REQUIRED
     - *CHOICE*
     - Identifies the OCSP responder. It MUST contain either ``byName`` or ``byKey``.
   * - ``tbsResponseData.responderID.byName``
     - [:rfc:`6960`, clause 4.2.1]
     - OPTIONAL
     - *[1] EXPLICIT Name*
     - The ``Name`` from the responder’s certificate subject.
   * - ``tbsResponseData.responderID.byKey``
     - [:rfc:`6960`, clause 4.2.1]
     - OPTIONAL
     - *[2] EXPLICIT OCTET STRING*
     - The SHA-1 hash of the responder’s ``subjectPublicKey`` (excluding the tag and length fields).
   * - ``tbsResponseData.producedAt``
     - [:rfc:`6960`, clause 4.2.1]
     - REQUIRED
     - *GeneralizedTime*
     - The time at which the OCSP response was generated.
   * - ``tbsResponseData.responses``
     - [:rfc:`6960`, clause 4.2.1]
     - REQUIRED
     - *SEQUENCE OF*
     - A sequence of ``SingleResponse`` structures, providing the status of each requested certificate.
   * - ``tbsResponseData.responseExtensions``
     - [:rfc:`6960`, clause 4.2.1]
     - OPTIONAL
     - *[1] EXPLICIT SEQUENCE OF*
     - Contains extensions applicable to the overall OCSP response.
   * - ``signatureAlgorithm``
     - [:rfc:`5280`, clause 4.1.1.2]
     - REQUIRED
     - *SEQUENCE*
     - Identifies the cryptographic algorithm used to sign the response.
   * - ``signatureAlgorithm.algorithm``
     - [:rfc:`5280`, clause 4.1.1.2]
     - REQUIRED
     - *OBJECT IDENTIFIER*
     - The OID of the signature algorithm. Selection SHOULD align with relevant standards (e.g., [ETSI TS 119 312]).
   * - ``signatureAlgorithm.parameters``
     - [:rfc:`5280`, clause 4.1.1.2]
     - OPTIONAL
     - *ANY*
     - Algorithm-specific parameters, dependent on the OID defined in ``algorithm``.
   * - ``signature``
     - [:rfc:`6960`, clause 4.2.1]
     - REQUIRED
     - *BIT STRING*
     - The digital signature computed over the hash of the DER-encoded ``tbsResponseData``.
   * - ``certs``
     - [:rfc:`6960`, clause 4.2.1]
     - OPTIONAL
     - *[0] EXPLICIT SEQUENCE OF*
     - Certificate chain to help the client verify the responder's signature. If no certificates are included, this field SHOULD be absent.

The ``responseExtensions`` structure MAY contain various extensions. The following table lists the requested ones:

.. list-table:: Response Extensions Nonce
   :class: longtable
   :widths: 22 18 10 15 35
   :header-rows: 1

   * - Parameter
     - Defined in
     - Presence
     - Format
     - Description
   * - ``nonce``
     - [:rfc:`6960`, clause 4.4.1]
     - REQUIRED
     - *OCTET STRING*
     - Cryptographically fresh value used to bind a request and a response to prevent replay attacks. If included in the request, responders SHOULD include it in the response. Identifier OID is ``id-pkix-ocsp-nonce``.

In the OCSP Response there MUST be at least a ``SingleResponse`` for each ``CertID`` in the request. Each ``SingleResponse`` is an ASN.1 *SEQUENCE* that carries the following parameters:

.. list-table:: SingleResponse Structure Parameters
   :class: longtable
   :widths: 22 18 10 15 35
   :header-rows: 1

   * - Parameter
     - Defined in
     - Presence
     - Format
     - Description
   * - ``certID``
     - [:rfc:`6960`, clause 4.2.1]
     - REQUIRED
     - *SEQUENCE*
     - Identifier of the certificate whose status is determined in ``certStatus``.
   * - ``certStatus``
     - [:rfc:`6960`, clause 4.2.1]
     - REQUIRED
     - *CHOICE*
     - The value of the certificate's status. It MUST be exactly one of: ``good``, ``revoked``, or ``unknown``.
   * - ``certStatus.good``
     - [:rfc:`6960`, clause 4.2.1]
     - OPTIONAL
     - *[0] IMPLICIT NULL*
     - Indicates the certificate is valid.
   * - ``certStatus.revoked``
     - [:rfc:`6960`, clause 4.2.1]
     - OPTIONAL
     - *[1] IMPLICIT SEQUENCE*
     - Indicates the certificate has been revoked. Contains the ``RevokedInfo`` structure.
   * - ``certStatus.revoked.revocationTime``
     - [:rfc:`6960`, clause 4.2.1]
     - REQUIRED
     - *GeneralizedTime*
     - The time at which the certificate was revoked.
   * - ``certStatus.revoked.revocationReason``
     - [:rfc:`6960`, clause 4.2.1]
     - OPTIONAL
     - *[0] EXPLICIT ENUMERATED*
     - Contains the ``CRLReason`` indicating why the certificate was revoked.
   * - ``certStatus.unknown``
     - [:rfc:`6960`, clause 4.2.1]
     - OPTIONAL
     - *[2] IMPLICIT NULL*
     - Indicates the responder does not know the status of the certificate.
   * - ``thisUpdate``
     - [:rfc:`6960`, clause 4.2.1]
     - REQUIRED
     - *GeneralizedTime*
     - Indicates the issue date and time of this OCSP Response.
   * - ``nextUpdate``
     - [:rfc:`6960`, clause 4.2.1]
     - OPTIONAL
     - *[0] EXPLICIT GeneralizedTime*
     - Indicates the date and time by which the next update to the OCSP Responder database will be in place.
   * - ``singleExtensions``
     - [:rfc:`6960`, clause 4.2.1]
     - OPTIONAL
     - *[1] EXPLICIT SEQUENCE*
     - Includes extensions applicable to this single certificate status response.

Below is a non-normative example of an OCSP response with a single ``good`` status.


.. literalinclude:: ../../examples/ocsp-response.txt
  :language: text

Token Status List (TSL)
""""""""""""""""""""""""

This section defines a Status List data structure, which is used to convey information regarding the individual statuses of multiple WRPRCs. A Status List describes the status of the WRPRCs by encoding their validity in a bit array. Each WRPRC is allocated an index during issuance; this index represents its position within the bit array. The value of the bit(s) at this index corresponds to the WRPRC's status. A Status List is provided within a cryptographically signed Status List Token in JWT format. The format, request and response structures are found in :ref:`credential-revocation:Token Status Lists`.

In this specification, the roles of the Provider of WRPRC and Status Issuer (i.e., the entity that issues the Status List Token about the status information of the WRPRC) MUST coincide. Moreover, the Status Provider (i.e., the entity that provides the Status List Token on a public endpoint) MUST be the Provider of WRPRC itself.

The Provider of WRPRC MUST use the following values for the possible statuses of the issued WRPRCs:

- ``0x00`` - ``VALID`` - The WRPRC is valid.
- ``0x01`` - ``INVALID`` - The WRPRC is revoked.


Once the Wallet Unit receives a WRPRC, it can request the Status List to validate its status through the provided URI parameter and look up the corresponding index in the list.

Status List Token (SLT)
........................

The **Status List Token** is available at the Status List Endpoint. It is formatted as a JSON Web Token (JWT) signed by the Provider of WRPRC and contains the parameters described in :ref:`credential-revocation:Status List Token`. The only difference is the ``status_list`` claim, which is a JSON object containing the following parameters:

.. _table_status_list_structure:
.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Parameter**
    - **Description**
    - **Reference**
  * - **bits**
    - REQUIRED. JSON Integer specifying the number of bits per WRPRC in the compressed byte array (`lst`). The allowed values for bits are 1,2,4 and 8.
    - `TOKEN-STATUS-LIST`_
  * - **lst**
    - REQUIRED. JSON String that contains the status values for all the WRPRCs it conveys statuses for. The value MUST be the base64url-encoded compressed byte array.
    - `TOKEN-STATUS-LIST`_
  * - **aggregation_uri**
    - OPTIONAL. JSON String that contains a URI to retrieve the Status List Aggregation for this type of WRPRC or Issuer.
    - `TOKEN-STATUS-LIST`_



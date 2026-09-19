.. include:: ../common/common_definitions.rst
.. Included via infrastructure-trust.rst at title level '-' (level 1).

.. role:: raw-html(raw)
  :format: html

EUDIW Trust Artifacts
---------------------

This section defines the required trust artifacts and their conceptual roles in the EUDIW ecosystem as per `EIDAS-ARF`_, including:

- :ref:`infrastructure-trust:Register of WRPs`;
- :ref:`infrastructure-trust:Wallet-Relying Party Access Certificate (WRPAC) Profile`;
- :ref:`infrastructure-trust:Registrar Sign/Seal Certificate Profile`;
- :ref:`infrastructure-trust:Wallet-Relying Party Registration Certificate (WRPRC) Profile`;
- :ref:`infrastructure-trust:Trusted List, Lists of Trusted Lists, and Lists of Trusted Entities`;
- :ref:`infrastructure-trust:Embedded Disclosure Policy (EDP)`.

The data model of these Trust Artifacts profiles the following external specifications.

- `ETSI TS 119 602`_, which defines the data model of the Lists of Trusted Entities and the profiles of the EUDIW lists.
- `ETSI TS 119 411-8`_, which defines the Wallet-Relying Party Access Certificate.
- `ETSI TS 119 475`_, which defines the Wallet-Relying Party Registration Certificate together with its entitlements.
- `ETSI EN 319 412-1`_, which defines the subject attributes of the certificates.
- `ETSI TS 119 182-1`_, which defines the JAdES format of the signature of a List of Trusted Entities.
- `ETSI EN 319 132-1`_, which defines the XAdES format of the signature of Trusted List and List of Trusted List.

Register of WRPs
^^^^^^^^^^^^^^^^

The national Register of WRPs is the publicly accessible system (dataset + API) that provides signed/sealed registration statements about WRPs, their **Services**, and their authorisations/declared usage.
This section documents a `EUDI-TS 5`_ version 1.5 (2026-08-20) aligned profile that satisfies Annex II of `CIR2025/848`_ as amended by [`CIR2026/1730`_].

A Wallet-Relying Party that operates in the EUDIW Trust Framework MUST register one or more **Relying Party Services** in the ``services`` array of the ``WalletRelyingParty`` object (`EUDI-TS 5`_, ``WalletRelyingPartyService``).
Each Service has a ``serviceTradeName`` suitable for presenting to the User ([`EIDAS-ARF`_] Reg_10a, Reg_34).
``serviceIdentifier`` is unique within the entity when registered. It MUST be registered if the Service relies on an Intermediary (`EUDI-TS 5`_ v1.5) and MUST be registered when a WRPAC is issued for that Service ([`EIDAS-ARF`_] Reg_33, RPRC_07a).
Intended uses, entitlements, provided attestations and intermediary relationships are bound to a Service, not to the entity root ([`EIDAS-ARF`_] Reg_10d).
A pure Intermediary Service MUST NOT register an entitlement (`EUDI-TS 5`_ v1.5). An Intermediary Service MUST list the Service identifiers it serves in ``servedWRPServices`` ([`CIR2026/1730`_], Annex I).

Register Dataset
""""""""""""""""

The data format for the information available through the open API provided by the national Register of WRPs MUST comply with the data schemas described in Tables 1-11 of Annex VI of [`CIR2025/848`_] as amended by [`CIR2026/1730`_], encoded as the ``WalletRelyingParty`` JSON Schema of `EUDI-TS 5`_ version 1.5.
Below some non-normative examples of ``WalletRelyingParty`` objects stored in the Register.

A bank registered as a Relying Party requesting PID for know-your-customer procedures, with one Relying Party Service.

.. literalinclude:: ../../examples/register-wrp-rp.json
  :language: JSON

A bank registered as both a Relying Party requesting PID and a QEAA Provider (issuing bank account attestations to Wallet).
It registers two Services: one Service with ``intendedUses`` and one Service with ``providesAttestations``.

.. literalinclude:: ../../examples/register-wrp-rp-ap.json
  :language: JSON

An entity registered as a designated Intermediary that acts on behalf of WRPs during Wallet interactions.
Each of its ``services[]`` elements has ``isIntermediary: true``, does not declare ``intendedUses`` or entitlements, and lists the served Services in ``servedWRPServices``.

.. literalinclude:: ../../examples/register-wrp-rp-intermediary.json
  :language: JSON


Register Open APIs
""""""""""""""""""

The common API read methods (GET) MUST be open for public access (no prior authentication), return JWS-signed statements,
and provide methods for searching and querying complete data sets of registered WRPs matching with provided query parameters.

- **GET /wrp**: Get a list of WRPs with optional filtering and pagination, as defined in Section 3.2 of `EUDI-TS 5`_ version 1.5.
  The filter parameters are ``identifier``, ``legalname``, ``tradename``, ``serviceidentifier``, ``policy``, ``entitlement``, ``providedattestation``, ``usesintermediary``, ``isintermediary``, ``intendeduseidentifier``, ``claimpath``, ``credentialmeta`` and ``credentialformat``.
  A successful response (``200``) MUST be a JWS-signed response body.
  The decoded payload MUST contain an array of ``WalletRelyingParty`` objects matching the query, and, where relevant, accompanied by WRPAC history information in the statement/profile used by the Member State.
  When the query uses ``serviceidentifier``, the response MUST include only the matching ``WalletRelyingPartyService`` in the ``services`` array of each matching ``WalletRelyingParty``.
  The list of all registered WRPs is returned when no query parameters are provided.
- **GET /wrp/{identifier}**: Retrieve the ``WalletRelyingParty`` object matching the given identifier.
  A successful response (``200``) MUST be a JWS-signed object.
- **GET /wrp/{identifier}/services/{serviceidentifier}**: Retrieve the parent ``WalletRelyingParty`` object with the ``services`` array sliced to the matching Service.
  A successful response (``200``) MUST be a JWS-signed object.
- **GET /wrp/check-intended-use**: A dedicated intended-use check endpoint for making narrowed-down intended use related queries from the Register.
  A successful response (``200``) MUST provide a JWS-signed boolean ``true`` or ``false`` response, determined by the queried parameters in the Registrar's Intended use information.
  If the request is invalid or incomplete the endpoint MUST answer with error code ``400``. If the given WRP is not found, it MUST answer with error code ``404``.

.. note::
    The published API view excludes only ``postalAddress`` ([`CIR2025/848`_] as amended by [`CIR2026/1730`_], Annex I, point 4).
    All other fields, including intended-use credential claims, are published as registered.
    The Register Open APIs remain for publication and transparency ([`EIDAS-ARF`_] Reg_03, Reg_06).
    The Wallet Unit MUST NOT use them as a substitute for a missing or invalid Wallet-Relying Party Registration Certificate during Credential Presentation or Credential Issuance, as specified in :ref:`trust-evaluation:EUDIW Authorization`.

The YAML file of the OpenAPI specification described in Section 3 of `EUDI-TS 5`_ version 1.5 is available as `EUDI-TS 5 OpenAPI`_.
The JSON Schema of the ``WalletRelyingParty`` object, including the ``services`` array of ``WalletRelyingPartyService``, is available as `EUDI-TS 5 JSON Schema`_.
The national read profile of that API is available :raw-html:`<a href="OAS3-Register-API-READ.html" target="_blank">here</a>`.

Wallet-Relying Party Access Certificate (WRPAC) Profile
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section extends the general :ref:`infrastructure-trust:X.509 Certificate Profile` and specifies a **Certificate Profile** for **Wallet-Relying Party Access Certificates (WRPACs)**.

According to the Article 2 of [`CIR2025/848`_], a WRPAC is a certificate for electronic seals or signatures authenticating and validating the WRP when they interact with the EUDI Wallet.
For more details on the authentication process, see :ref:`trust-evaluation:EUDIW Authentication`.

The suspension or cancellation of the WRP services, involves revocation of all valid WRPAC by the relevant issuing authority, such that the WRP is no longer able to interact with Wallet Units.
For more detail on the Trust Management processes, see :ref:`infrastructure-trust:Trust Management and Lifecycle`.

Annex IV of [`CIR2025/848`_] also states that the WRPACs are meant for performing electronic signatures or seals and that they MUST comply with at least the Normalised Certificate Policy (NCP) requirements specified in the ETSI standards.
Taking into account these minimal requirements, different scenarios are possible and specified in the following clauses: certificates issued to natural or legal persons, supporting advanced signatures/seals or even qualified signature/seals.
Conditional requirements are defined according to the specific case the WRPACs fall into.

The specific requirements for WRPACs are specified in `ETSI TS 119 411-8`_.

The following table defines the complete set of extensions applicable to the certificate profile.
Extensions not listed in the table MUST NOT be present.

.. list-table:: Wallet-Relying Party Access Certificate Extensions
   :class: longtable
   :header-rows: 1
   :widths: 25 75

   * - **Extension**
     - **Description**

   * - ``authorityKeyIdentifier``
     - REQUIRED. The value of the ``keyIdentifier`` field SHOULD be derived from the public key using the methods defined in :rfc:`5280#section-4.2.1.1`.

   * - ``subjectKeyIdentifier``
     - OPTIONAL. If present, its value SHOULD be derived from the subject public key using the methods defined in :rfc:`5280#section-4.2.1.2`.

   * - ``keyUsage``
     - REQUIRED. It MUST contain one (and only one) of the key-usage settings *Type A*, *Type B*, or *Type F*. *Type A* SHOULD be used as per LEG-4.3.1-4 in Clause 4.3.1 [`ETSI EN 319 412-3`_]. For additional details, see Clause 4.3.2 [`ETSI EN 319 412-2`_] and Clause 4.3.1 [`ETSI EN 319 412-3`_].

   * - ``certificatePolicies``
     - REQUIRED. It MUST include a ``PolicyInformation`` structure with ``policyIdentifier`` set to one of the following values (defined in `ETSI TS 119 411-8`_):

       * ``0.4.0.194118.1.1`` (``NCP-n-eudiwrp``);
       * ``0.4.0.194118.1.2`` (``NCP-l-eudiwrp``);
       * ``0.4.0.194118.1.3`` (``QCP-n-eudiwrp``);
       * ``0.4.0.194118.1.4`` (``QCP-l-eudiwrp``)

       and ``policyQualifiers`` containing a ``cpsURI`` that references an URL where the CPS of the Provider of WRPAC is located.

   * - ``subjectAltName``
     - REQUIRED. It MUST include a ``GeneralName`` structure with one of the following parameters defined to provide valid contact information of the WRP:
     
       * ``uniformResourceIdentifier``, to provide the URI of a website for helpdesk/support matters;
       * ``otherName`` with ``type-id`` set to ``2.5.4.20`` (``id-at-telephoneNumber``), to provide a phone number for WRP registration/usage matters;
       * ``rfc822Name``, to provide an email address for WRP registration/usage matters.

       In addition, it MUST include a ``uniformResourceIdentifier`` whose last path segment is the Relying Party Service identifier of this certificate (``services[].serviceIdentifier`` in the Register).
       That URI MUST be unique within the entity and MUST be identical to the ``srv_id`` of every WRPRC issued for the same Service of the same entity ([`EIDAS-ARF`_] Reg_33, RPRC_07a).
       Until [`ETSI TS 119 411-8`_] defines a dedicated attribute for the Service identifier, this ``subjectAltName`` URI is the IT-Wallet encoding of Reg_33.

       If the subject is an Intermediary presenting on behalf of an intermediated Relying Party, the certificate MUST additionally include a second ``uniformResourceIdentifier`` of the form ``{registryURI}/wrp/{intermediatedRpIdentifier}/services/{intermediatedServiceIdentifier}``, where ``intermediatedRpIdentifier`` is the EU-wide unique identifier of that Relying Party ([`EIDAS-ARF`_] Reg_32) and ``intermediatedServiceIdentifier`` is the identifier of the intermediated Relying Party Service ([`EIDAS-ARF`_] Reg_33).
       Until [`ETSI TS 119 411-8`_] defines a dedicated attribute for this association, that URI is the IT-Wallet encoding of [`EIDAS-ARF`_] Reg_34a.

   * - ``cRLDistributionPoints``
     - CONDITIONAL. **REQUIRED IF:** the certificate does not include any access location of an OCSP responder or the validity assured extension as defined in `ETSI EN 319 412-1`_.
     
       If present, it MUST contain at least one reference to a publicly available CRL.

   * - ``authorityInfoAccess``
     - REQUIRED. It MUST include an ``AccessDescription`` structure with ``accessMethod`` set to ``1.3.6.1.5.5.7.48.2`` (``id-ad-caIssuers``) and ``accessLocation`` specifying at least one access location of a valid CA certificate of the issuing CA.

       If OCSP is supported by the issuing CA, the extension MUST include an ``AccessDescription`` structure with ``accessMethod`` set to ``1.3.6.1.5.5.7.48.1`` (``id-ad-ocsp``) and ``accessLocation`` specifying at least one OCSP responder authoritative to provide certificate status information for the certificate, as described in :ref:`infrastructure-trust:Online Certificate Status Protocol (OCSP)`.

   * - ``qcStatements``
     - OPTIONAL. It MAY contain `QCStatement` structures among those defined in Clause 4.2 of [ETSI EN 319 412-5].
       In any case, it MUST NOT contain a ``QCStatement`` structure with ``statementId`` set to ``0.4.0.1862.1.7`` (``id-etsi-qcs-QcCClegislation``), referred to as ``esi4-qcStatement-7``.

   * - ``signedCertificateTimestampList``
     - REQUIRED. Non-critical X.509 extension with object identifier ``1.3.6.1.4.1.11129.2.4.5`` (``id-ct-v2-sctList``) as specified in :rfc:`9162`.
       It MUST contain at least one Signed Certificate Timestamp for this certificate ([`EIDAS-ARF`_] CT_04).
       Certificate Transparency version 2.0 applies to Wallet-Relying Party Access Certificates only; it does not apply to the Wallet-Relying Party Registration Certificate.

.. note::
    **Dependency Considerations**: The WRPAC attributes MUST be derived from the information held in the Register as specified in clause 5.1.2 of `ETSI TS 119 475`_.
    This also implies that for some specific attributes in the WRPAC the same value MUST be encountered in the corresponding WRPRC.

    A registering entity MUST receive at least one WRPAC for each registered Service ([`EIDAS-ARF`_] Reg_10a).
    An Intermediary MUST receive a separate set of WRPACs for each intermediated Relying Party, one WRPAC per intermediated Relying Party Service it serves ([`EIDAS-ARF`_] Reg_34a).
    The ``subject.organizationName`` (legal person) or the natural-person name attributes MUST identify the entity and MUST be suitable for presenting to the User ([`EIDAS-ARF`_] Reg_31).
    The ``subject.organizationIdentifier`` (legal person) or ``subject.serialNumber`` (natural person) MUST be the EU-wide unique identifier of the entity ([`EIDAS-ARF`_] Reg_32).
    The ``subject.commonName`` MUST be the ``serviceTradeName`` of the Service this certificate authenticates ([`EIDAS-ARF`_] Reg_34).
    The Service identifier MUST be present in ``subjectAltName`` as specified above ([`EIDAS-ARF`_] Reg_33).
    If the subject is an Intermediary, ``subjectAltName`` MUST also carry the association to the intermediated Relying Party as specified above ([`EIDAS-ARF`_] Reg_34a).

    The Provider of WRPAC SHALL log every issued WRPAC in a Certificate Transparency log according to :rfc:`9162` ([`EIDAS-ARF`_] CT_01) and SHALL describe that logging in its Certification Practice Statement, referenced by the ``cpsURI`` above ([`EIDAS-ARF`_] CT_02, Annex IV, point 3(j) of [`CIR2025/848`_], `ETSI TS 119 411-8`_ OVR-6.4.5-02).
    Until a Certificate Transparency log for access certificates is designated at Union level, the Provider of WRPAC SHALL operate or use a log suitable for WRPACs so that each certificate can carry at least one Signed Certificate Timestamp ([`EIDAS-ARF`_] CT_04).
    When a Certificate Transparency log for access certificates is available, the Provider of WRPAC SHALL act as a monitor in the Certificate Transparency ecosystem and SHOULD continue to monitor during temporary unavailability of the log ([`EIDAS-ARF`_] CT_03).

The following is an example of a WRPAC for legal persons following the NCP.

.. literalinclude:: ../../examples/wrpac-ncp.txt
  :language: text

Registrar Sign/Seal Certificate Profile
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section extends the general :ref:`infrastructure-trust:X.509 Certificate Profile` and specifies a **Certificate Profile** for **Registrar Sign/Seal Certificates**.

The following table defines the complete set of extensions applicable to the certificate profile.
Extensions not listed in the table MUST NOT be present.

.. list-table:: Registrar Sign/Seal Certificate Extensions
   :class: longtable
   :header-rows: 1
   :widths: 25 75

   * - **Extension**
     - **Description**

   * - ``authorityKeyIdentifier``
     - REQUIRED. The value SHOULD be derived from the public key using the methods defined in :rfc:`5280#section-4.2.1.1`.

   * - ``subjectKeyIdentifier``
     - OPTIONAL. If present, the ``keyIdentifier`` field SHOULD be derived from the subject public key using the methods defined in :rfc:`5280#section-4.2.1.2`.

   * - ``keyUsage``
     - REQUIRED. It MUST contain one (and only one) of the key-usage settings *Type A*, *Type B*, or *Type F*. *Type A* SHOULD be used as per LEG-4.3.1-4 in Clause 4.3.1 [`ETSI EN 319 412-3`_]. For additional details, see Clause 4.3.2 [`ETSI EN 319 412-2`_] and Clause 4.3.1 [`ETSI EN 319 412-3`_].

   * - ``certificatePolicies``
     - REQUIRED. It MUST include a ``PolicyInformation`` structure relevant to the issuing CA's practices.

   * - ``subjectAltName``
     - REQUIRED.

   * - ``cRLDistributionPoints``
     - CONDITIONAL. **REQUIRED IF:** the certificate does not include any access location of an OCSP responder or the validity assured extension as defined in `ETSI EN 319 412-1`_.

   * - ``authorityInfoAccess``
     - REQUIRED. It MUST include an ``AccessDescription`` structure with ``accessMethod`` set to ``1.3.6.1.5.5.7.48.2`` (``id-ad-caIssuers``) and ``accessLocation`` specifying at least one access location of a valid CA certificate of the issuing CA.

       If OCSP is supported by the issuing CA, the extension MUST include an ``AccessDescription`` structure with ``accessMethod`` set to ``1.3.6.1.5.5.7.48.1`` (``id-ad-ocsp``) and ``accessLocation`` specifying at least one OCSP responder authoritative to provide certificate status information for the certificate, as described in :ref:`infrastructure-trust:Online Certificate Status Protocol (OCSP)`.

The following is a non-normative example of a Registrar Sign/Seal Certificate for legal persons (non-self-signed).

.. literalinclude:: ../../examples/registrar-sign-seal.txt
  :language: text


Wallet-Relying Party Registration Certificate (WRPRC) Profile
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section defines Wallet-Relying Party Registration Certificate (WRPRC), as described in the `EIDAS-ARF`_ and `ETSI TS 119 475`_.
This Trust Artifact provides detailed information about the Credential Issuer and Relying Party's Authorization profile, including:

- core identification attributes (clause 5.1 `ETSI TS 119 475`_),
- service description attributes (clause 5.2.4 `ETSI TS 119 475`_), including the Relying Party Service identifier and trade name ([`EIDAS-ARF`_] RPRC_07a),
- entitlement attributes (see Annex A.2 `ETSI TS 119 475`_),
- supervisory authority attributes (clause 5.2.4 `ETSI TS 119 475`_),
- Relying Party attributes (clause 5.2.4 `ETSI TS 119 475`_),
- Credential Issuer attributes (clause 5.2.4 `ETSI TS 119 475`_),
- Intermediary attributes; i.e., whether the Relying Party Service relies on an Intermediary to request Digital Credentials (clause 5.2.4 `ETSI TS 119 475`_).

Each WRPRC is bound to a single Relying Party Service.
The Provider of WRPRC issues WRPRCs automatically as defined in :ref:`onboarding-system:Wallet-Relying Party Registration Certificate Issuance`.
The ``name`` claim MUST equal the ``serviceTradeName`` of that Service and, for a non-intermediated presentation, MUST be identical to the ``subject.commonName`` of the WRPAC of the same Service of the same entity ([`EIDAS-ARF`_] Reg_34, RPRC_07a).
The ``srv_id`` claim MUST equal the ``serviceIdentifier`` of that Service and, for a non-intermediated presentation, MUST be identical to the Service identifier encoded in the WRPAC ``subjectAltName`` ([`EIDAS-ARF`_] Reg_33, RPRC_07a).
The WRPRC ``intermediary`` object MUST identify the Intermediary and the Intermediary Service ([`EIDAS-ARF`_] RPRC_04).
The Wallet Unit evaluates intermediated presentation, including the WRPAC ``subjectAltName`` association of [`EIDAS-ARF`_] Reg_34a, as specified in :ref:`trust-evaluation:EUDIW Authorization`.
ETSI TS 119 475 v1.2.1 does not yet define ``srv_id``; this specification profiles it to implement RPRC_07a until that standard is updated. The claim is a JSON string (JWT) or a CBOR text string (CWT) and MUST be identical to ``services[].serviceIdentifier`` in the Register.

The Wallet-Relying Party Registration Certificate MUST be formatted either as a signed JSON Web Token (JWT) or CBOR Web Token (CWT) :rfc:`8392`.
It MUST comply with the syntactic and semantic requirements specified in Annex V paragraph 3 of CIR (EU) 2025/848 and `ETSI TS 119 475`_.

The Wallet-Relying Party Registration Certificate MUST be signed with the private key of Provider of the Wallet-Relying Party Registration Certificates.
In particular:

- The JWT MUST be signed with a JSON Advanced Electronic Signature with the B-B profile as defined in `ETSI TS 119 182-1`_.
- The CWT MUST be signed with an Advanced Electronic Signature following structure as defined in :rfc:`9052` and :rfc:`9360`.

Below a non-normative example of WRPRC header and payload for a Relying Party.

.. literalinclude:: ../../examples/wrprc-jwt-header.json
  :language: json

.. literalinclude:: ../../examples/wrprc-payload-ci.json
  :language: json

Below a non-normative example of WRPRC payload for an intermediated Relying Party.

.. literalinclude:: ../../examples/wrprc-payload-rpi.json
  :language: json

.. warning::

  `ETSI TS 119 475`_, Table 10 defines the intermediary name subfield as ``sname``.
  The example in Annex C of the same standard uses ``name`` instead.
  This specification follows the normative Table 10 and uses ``sname``.

  The Service identifier claim ``srv_id`` is profiled by this specification to implement [`EIDAS-ARF`_] RPRC_07a until `ETSI TS 119 475`_ defines an equivalent member.

Trusted List, Lists of Trusted Lists, and Lists of Trusted Entities
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section describes the format and contents of three types of Trust Artifacts, each of which conveys a list of current and historical Trust Anchors (containers of cryptographic materials and identifiers belonging to trusted Entities).

Ecosystem Entities utilize these lists to:

- **Validate runtime trustworthiness**: Verify a Trust Anchor (see :ref:`infrastructure-trust:Trust Anchor Certificate Profile`) to authenticate, authorize, or validate an entity or artifact during live operations.
- **Perform historical validation**: Validate information contained within the list for historical audit purposes.

The three distinct types of trust lists are:

- Trusted Lists (TLs): Established under Chapter II of Annex I of `CID2015/1505`_, as amended by `CID2025/2164`_, and specified in `ETSI TS 119 612`_.
  Each Member State publishes one TL in XML format.
  It is signed by the respective Member State with an XAdES digital signature at conformance level baseline B (as defined in `ETSI EN 319 132-1`_).
  TLs are published in a machine-readable format at endpoints specified within the LOTL.
  These Lists hold current and historical information about the accreditation of trust service providers, referencing:

  - Qualified Trust Service Providers (QTSP)s, such as Qualified Certificates Issuing and revocation mechanisms, QEAA Providers, Qualified electronic archiving services.
  - Non-Qualified Trust Services such as EAA Providers.
  - Other Trust Services defined at the national level, such as archiving.

   Within eIDAS, TLs are maintained by Member States, who are responsible for keeping record of the trusted services providers under their respective jurisdiction.
   They are numbered and renewed periodically, and published in a website for unrestricted download.
   To protect their integrity and assure authenticity, they are also signed with trusted certificates contained in the LOTL.

- List of Trusted Lists (LOTL): Established under Chapter II of Annex I of `CID2015/1505`_, as amended by `CID2025/2164`_, and specified in `ETSI TS 119 612`_.
  There is only one LOTL, which is published in XML format and signed by the European Commission (EC).
  It utilizes an XAdES digital signature at conformance level baseline B (per `ETSI EN 319 132-1`_) and references the trusted certificates that each National Trusted List.
  To facilitate key rotation and continuous updates, the LOTL implements a pivoting mechanism.
  It is published in a machine-readable format at an endpoint specified within the Official Journal of the European Union (`OJEU`_).

  The XML schema for both Trusted Lists and List of Trusted Lists, containing parameters' name and description can be found at ``https://forge.etsi.org/rep/esi/x19_612_trusted_lists/-/raw/v2.4.1/19612_xsd.xsd``. Currently, the machine-readable version of the LOTL and National TLs is published at `EUMS-LOTL`_.

- Lists of Trusted Entities (LoTE): Established under Articles 4 and 5 of `CIR2024/2980`_ and specified in `ETSI TS 119 602`_.
  These are available in either XML or JSON format and are signed with an AdES digital signature at conformance level baseline B (per `ETSI TS 119 182-1`_).
  To facilitate continuous updates, the LoTE implements a pivoting mechanism and is published in a machine-readable format at an endpoint specified within the `OJEU`_.
  The LoTE types can be one of the following, as defined in annex C.2:

  - PID Provider;
  - Wallet Provider;
  - Provider of Wallet Relying Party Access Certificates;
  - Providers of Wallet Relying Party Registration Certificates;
  - Public sector bodies issuing Electronic Attestations of Attributes;
  - List of Registrars and Registers.

  The following repository provides the normative JSON and XML schemas required for implementing the List of Trusted Entities (`ETSI-LOTE-SCHEMAS`_).

The following table provides a comprehensive overview of the eIDAS trust list architecture, cross-referencing the legal basis, governing technical standards, explicit data formats, signature profiles, and publication dynamics for Trusted Lists (TL), the List of Trusted Lists (LOTL), and the various category-specific Lists of Trusted Entities (LoTE).

.. list-table:: eIDAS Trust List Ecosystem Profiles
   :class: longtable
   :widths: 14 20 16 16 18 16
   :header-rows: 1

   * - **List Type**
     - **Legal Basis**
     - **Governing Standard & Format**
     - **Signature Profile**
     - **Scope & Signer**
     - **Publication & Update Mechanism**
   * - **Trusted Lists (TL)**
     - `CID2015/1505`_ (Annex I, Chapter II), amended by `CID2025/2164`_.
     - `ETSI TS 119 612`_; ``XML`` format.
     - XAdES digital signature, baseline B (`ETSI EN 319 132-1`_).
     - Member State scope; one list per Member State, signed by that Member State.
     - Machine-readable endpoint specified within the LOTL.
   * - **List of Trusted Lists (LOTL)**
     - `CID2015/1505`_ (Annex I, Chapter II), amended by `CID2025/2164`_.
     - `ETSI TS 119 612`_; ``XML`` format.
     - XAdES digital signature, baseline B (`ETSI EN 319 132-1`_).
     - European Union scope; a single global list signed by the European Commission (EC) that anchors the National Trusted Lists.
     - Machine-readable endpoint specified within the `OJEU`_.
       Implements a pivoting mechanism to handle continuous updates.
   * - **LoTE: PID Provider Lists**
     - Articles 4 and 5 of `CIR2024/2980`_.
     - `ETSI TS 119 602`_ Annex D; ``JSON`` format.
     - AdES digital signature, baseline B (`ETSI TS 119 182-1`_).
     - European Union scope; one list per specific ecosystem entity type.
     - Machine-readable endpoint specified within the `OJEU`_.
       Implements a pivoting mechanism to handle continuous updates.
   * - **LoTE: Wallet Provider (WP) Lists**
     - Articles 4 and 5 of `CIR2024/2980`_.
     - `ETSI TS 119 602`_ Annex E; ``JSON`` format.
     - AdES digital signature, baseline B (`ETSI TS 119 182-1`_).
     - European Union scope; one list per specific ecosystem entity type.
     - Machine-readable endpoint specified within the `OJEU`_.
       Implements a pivoting mechanism to handle continuous updates.
   * - **LoTE: Provider of WRPAC Lists**
     - Articles 4 and 5 of `CIR2024/2980`_.
     - `ETSI TS 119 602`_ Annex F; ``JSON`` format.
     - AdES digital signature, baseline B (`ETSI TS 119 182-1`_).
     - European Union scope; one list per specific ecosystem entity type (Wallet Relying Party Access Certificate).
     - Machine-readable endpoint specified within the `OJEU`_.
       Implements a pivoting mechanism to handle continuous updates.
   * - **LoTE: Provider of WRPRC Lists**
     - Articles 4 and 5 of `CIR2024/2980`_.
     - `ETSI TS 119 602`_ Annex G; ``JSON`` format.
     - AdES digital signature, baseline B (`ETSI TS 119 182-1`_).
     - European Union scope; one list per specific ecosystem entity type (Wallet Relying Party Registration Certificate).
     - Machine-readable endpoint specified within the `OJEU`_.
       Implements a pivoting mechanism to handle continuous updates.
   * - **LoTE: PuB-EAA Provider Lists**
     - Articles 4 and 5 of `CIR2024/2980`_.
     - `ETSI TS 119 602`_ Annex H; ``JSON`` or ``XML`` format.
     - AdES digital signature, baseline B (`ETSI TS 119 182-1`_).
     - European Union scope; lists notified PuB-EAA Providers and their Sign/Seal Trust Anchors.
     - Machine-readable endpoint specified within the `OJEU`_.
       Implements a pivoting mechanism to handle continuous updates.
   * - **LoTE: Registrar and Register Provider Lists**
     - Articles 4 and 5 of `CIR2024/2980`_.
     - `ETSI TS 119 602`_ Annex I; ``JSON`` format.
     - AdES digital signature, baseline B (`ETSI TS 119 182-1`_).
     - European Union scope; one list per specific ecosystem entity type.
     - Machine-readable endpoint specified within the `OJEU`_.
       Implements a pivoting mechanism to handle continuous updates.

.. note::
  
  As suggested in the `EIDAS-ARF`_, for efficiency, implementations MAY routinely check Trust Anchors in Lists of Trusted Entities or Trusted Lists and store them locally. This allows, for example, Relying Party Instances running on mobile apps to facilitate offline presentations.
  
The example below shows a non-normative example of payload of a List of Trusted Entities for PID Providers.

.. literalinclude:: ../../examples/lote-pid.json
  :language: json

Embedded Disclosure Policy (EDP)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An Embedded Disclosure Policy (EDP) is defined in Article 2(9) of [`CIR2024/2979`_] as: *"A set of rules, embedded in an electronic attestation of attributes by its provider, that indicates the conditions that a wallet-relying party has to meet to access the electronic attestation of attributes"*.

Attestation Providers (i.e., all Credential Issuers except the PID Provider) can optionally express an EDP which allow indicating which Relying Parties can access specific Digital Credentials.
The Article 10 of [`CIR2024/2979`_] establishes that Wallet Providers MUST ensure that Attestations with common EDPs (as listed in Annex III of [`CIR2024/2979`_]) can be processed by their Wallet Units.

EDPs are applicable to QEAAs, PuB-EAAs, and EAAs.
They MUST NOT be applicable to PIDs.

The EDP is distributed through the Credential Issuer Metadata at issuance time.
The Attestation Provider MUST include the EDP URI together with its policy data, or the URI alone when the exact policy is already preloaded, within the ``credential_configurations_supported`` parameter, in compliance with `OpenID4VCI`_ or the extension thereof specified in `ETSI TS 119 472-3`_.
If available, the Wallet Unit MUST resolve and store the EDP locally and associate the resolved policy with the specific Attestation for which it was retrieved; an unresolved URI MUST cause the association and the affected disclosure to fail.
The Wallet Unit MUST NOT reveal the EDP to the Relying Party through the presentation protocol as per `ETSI TS 119 472-3`_, Section 4.2.5.1.

Embedded Disclosure Policies are used to:

- Implementing sector-specific access control (e.g., only public sector RPs or only healthcare RPs).
- Implementing Member-State-specific access control (e.g., only RPs registered within a specific Member State).

Annex III of [`CIR2024/2979`_] defines three common EDP types.
The Wallet Unit evaluates them as specified in :ref:`trust-evaluation:EUDIW Authorization`.

- **No Policy.** No EDP is present, or the EDP explicitly indicates that no restrictions apply (ISS-MDATA-EBD-4.2.5.2-06).

- **Authorized Relying Parties Only.** The EDP contains a list of authorized entries. Each entry MAY identify the Relying Party by its RFC 4514 subject distinguished name from the authenticated WRPAC, by an entitlement URI from the validated WRPRC, or by an identifier/service duplet from the WRPRC as an additional alternative ([`EIDAS-ARF`_] EDP_02, Reg_32, Reg_33).

  - For legal persons, the relevant DN attributes are ``commonName``, ``organizationName``, ``organizationIdentifier``, and ``countryName``.
  - For natural persons: ``commonName``, ``givenName``, ``surname``, ``serialNumber``, and ``countryName``.
    The ``organizationIdentifier`` attribute type is represented by the LDAP string "ORGID"; the ``serialNumber`` attribute type is represented by "SN" (according to `ETSI TS 119 472-3`_ NOTE 1 and NOTE 2 to ISS-MDATA-EBD-4.2.5.2-07).

- **Specific Root of Trust.** The EDP contains a list of trusted roots or intermediate certificates in the WRPAC certification paths ([`EIDAS-ARF`_] EDP_03).
  Only RPs whose authenticated WRPAC path contains one of these certificates are allowed to access the Attestation.
  According to `ETSI TS 119 472-3`_ (ISS-MDATA-EBD-4.2.5.2-08/09), each authorized root or intermediate is identified by its issuer distinguished name in LDAP string form as defined in RFC 4514 and the issuer's certificate serial number.

.. note::

  `ETSI TS 119 472-3`_ (ISS-MDATA-EBD-4.2.5.2-07) encodes authorized parties by subject DN or by entitlement URI, and the identifier/service duplet is an additional alternative.
  The ``subject_dn`` parameter is matched against the authenticated WRPAC subject using RFC 4514 DN comparison.
  The ``entitlement_uri`` parameter is matched against entitlements or sub-entitlements held in the WRPRC.
  The identifier/service duplet, when present, is matched against ``sub`` and ``srv_id`` from the WRPRC and is not taken from the WRPAC.
  Annex A.3 of `ETSI TS 119 475`_ defines sub-entitlements for Service Providers, currently for Payment Service Providers (e.g. ``https://uri.etsi.org/19475/SubEntitlement/psp/psp-ai``).
  For an **intermediated** presentation the WRPRC in the request is that of the *intermediated* Relying Party ([`EIDAS-ARF`_] RPRC_19).

Embedded Disclosure Policy Data Model
""""""""""""""""""""""""""""""""""""""

The following table provides a comprehensive overview of the Embedded Disclosure Policy data model, including parameter names, data types, descriptions, and the specific clauses in `ETSI TS 119 472-3`_ where each parameter is defined.

.. warning::
  The parameter names are defined in this section and are not based on a normative ETSI specification. Section 4.2.5.2 of `ETSI TS 119 472-3`_ defines the high level requirements for data model, but the final JSON schema will be published separately by ETSI. The structure defined here is an implementation profile based on the ETSI data model requirements, and parameter names MAY change when the ETSI schema is published.

.. list-table:: Embedded Disclosure Policy Parameters
   :class: longtable
   :header-rows: 1
   :widths: 20 60 20

   * - **Parameter**
     - **Description**
     - **Reference**

   * - ``policy_uri``
     - REQUIRED. string (URI).
       Unique identifier of the Embedded Disclosure Policy (EDP).

       The association of the EDP with an EAA MUST be established by including this unique URI.
        The AP MUST either include the URI together with the full policy data set, or provide only the URI if the exact policy data set identified by that URI has already been pre-loaded into the Wallet Unit. A URI that cannot be resolved to the exact included or preloaded policy MUST fail EDP processing; the Wallet Unit MUST NOT proactively retrieve an unspecified replacement policy.
     - Clause 4.2.5.2 of [`ETSI TS 119 472-3`_] (ISS-MDATA-EBD-4.2.5.2-01, ISS-MDATA-EBD-4.2.5.2-02, ISS-MDATA-EBD-4.2.5.2-03)

   * - ``policy_type``
     - REQUIRED. string.
       Policy type classification.
       Valid values:

       * ``"no_policy"``: Indicates that no policy restrictions apply for the associated EAA.
       * ``"authorized_rp_only"``: Access is restricted to an explicit list of allowed Relying Parties.
       * ``"specific_root_of_trust"``: Access is restricted to Relying Parties whose WRPRC signing path contains a specified trusted root or intermediate certificate.
     - Clause 4.2.5.2 of [`ETSI TS 119 472-3`_] (ISS-MDATA-EBD-4.2.5.2-06, ISS-MDATA-EBD-4.2.5.2-07, ISS-MDATA-EBD-4.2.5.2-08)

   * - ``description``
     - OPTIONAL. string.
       Description of the applicability of the policy to a particular community and/or class of application sharing common security requirements.
     - Clause 4.2.5.2 of [`ETSI TS 119 472-3`_] (ISS-MDATA-EBD-4.2.5.2-04)

   * - ``policy_authority``
     - OPTIONAL. string.
       Identifier of the authority or entity responsible for the policy.
     - Clause 4.2.5.2 of [`ETSI TS 119 472-3`_] (ISS-MDATA-EBD-4.2.5.2-05)

   * - ``policy_info_url``
     - OPTIONAL. string (URL).
       Link to a website of the Attestation Provider (AP) explaining the disclosure policy guidelines in layman's terms.
     - Clause 4.2.5.2 of [`ETSI TS 119 472-3`_] (ISS-MDATA-EBD-4.2.5.2-13, EDP_05)

   * - ``authorized_parties``
     - REQUIRED. array of objects if ``policy_type`` is ``"authorized_rp_only"``.
       Contains authorized entries. Each entry MUST contain at least one of ``subject_dn`` or ``entitlement_uri``; an identifier/service duplet MAY be included as an additional alternative.
     - Clause 4.2.5.2 of [`ETSI TS 119 472-3`_] (ISS-MDATA-EBD-4.2.5.2-07)

   * - ``authorized_parties[].identifier``
     - REQUIRED. string.
        EU-wide unique identifier of the authorized Relying Party, as specified in [`EIDAS-ARF`_] Reg_32. When present, it MUST match the ``sub`` of the WRPRC in the request and is an additional matching alternative.
     - [`EIDAS-ARF`_] EDP_02

   * - ``authorized_parties[].service_identifier``
     - REQUIRED. string.
        Identifier of the authorized Relying Party Service, as specified in [`EIDAS-ARF`_] Reg_33. When present with ``identifier``, it MUST match the ``srv_id`` of the WRPRC in the request.
     - [`EIDAS-ARF`_] EDP_02

   * - ``authorized_parties[].subject_dn``
     - OPTIONAL. string.
       Subject Distinguished Name (DN) of the Relying Party, formatted as an LDAP string compliant with :rfc:`4514`.
       This is the ETSI encoding of ISS-MDATA-EBD-4.2.5.2-07 and MUST be matched against the authenticated WRPAC subject DN using RFC 4514 DN comparison.
     - Clause 4.2.5.2 of [`ETSI TS 119 472-3`_] (ISS-MDATA-EBD-4.2.5.2-07)

   * - ``authorized_parties[].entitlement_uri``
     - OPTIONAL. string (URI).
        URI-encoded entitlement or sub-entitlement as specified in Annex A of [`ETSI TS 119 475`_], held within the Wallet-Relying Party Registration Certificate (WRPRC). It MUST be compared exactly.
     - Clause 4.2.5.2 of [`ETSI TS 119 472-3`_] (ISS-MDATA-EBD-4.2.5.2-07)

   * - ``trusted_roots``
     - REQUIRED. array of objects. if ``policy_type`` is ``"specific_root_of_trust"``.
        Defines a precise list of trusted root or intermediate certificates in permitted WRPAC certification paths.
        Only RPs whose validated WRPAC path contains one of these certificates are permitted access.
     - Clause 4.2.5.2 of [`ETSI TS 119 472-3`_] (ISS-MDATA-EBD-4.2.5.2-08)

   * - ``trusted_roots[].issuer_dn``
     - REQUIRED. string.
       Issuer Distinguished Name (DN) in LDAP string form compliant with :rfc:`4514`.
     - Clause 4.2.5.2 of [`ETSI TS 119 472-3`_] (ISS-MDATA-EBD-4.2.5.2-09)

   * - ``trusted_roots[].serial_number``
     - REQUIRED. string.
       Certificate serial number corresponding to the defined issuer.
     - Clause 4.2.5.2 of [`ETSI TS 119 472-3`_] (ISS-MDATA-EBD-4.2.5.2-09)

   * - ``extensions``
     - OPTIONAL. array of objects.
       Container for supplementary EDP extension structures.

        These structures MAY be ignored by the Wallet Unit, but the Wallet Unit MUST successfully process recognized rules even if unrecognized extensions are present. The IT-Wallet extension is an object with an extension identifier, a Credential-format claim ``path``, and an alternative common EDP rule. The base policy governs the Credential; the matching extension rule governs that attribute, and every disclosed attribute MUST satisfy its applicable rule. The extension encoding MUST be serializable in the EDP and MUST NOT change the result for attributes without a matching path.
     - Clause 4.2.5.2 of [`ETSI TS 119 472-3`_] (ISS-MDATA-EBD-4.2.5.2-10, ISS-MDATA-EBD-4.2.5.2-11, ISS-MDATA-EBD-4.2.5.2-12)

The following are non-normative examples of EDPs with Authorized Relying Parties Only and Specific Root of Trust policy types.

.. literalinclude:: ../../examples/edp-authorized-rps.json
  :language: json

.. literalinclude:: ../../examples/edp-specific-root.json
  :language: json

Embedded Disclosure Policy Lifecycle
""""""""""""""""""""""""""""""""""""

The locally stored EDP MUST remain valid as long as the Attestation it is associated with is valid and not revoked.
The EDP MUST NOT have an independent validity status or revocation mechanism separate from the Attestation.

If an Attestation Provider adds, changes, or deletes an EDP for a Digital Credential it issues, the Attestation Provider MUST revoke that Digital Credential.
The Wallet Unit detects the EDP change indirectly through the normal Attestation status checking mechanism (Status List), which will report that the Digital Credential as revoked.
The locally stored EDP is then implicitly invalidated together with the Digital Credential.
The User needs to request a new issuance to obtain the Digital Credential with the updated EDP.

Even a minor policy change (e.g., adding a single RP to the authorized list) requires revocation and re-issuance.
The timing of detection depends on when the Wallet Unit checks the Digital Credential status: if the Wallet Unit checks only at presentation time, a policy change will not be detected until the next presentation attempt.

.. warning::

    **Proactive refresh**.
    The Attestation Provider MAY provide EDP though its URI.
    In this case, the Wallet Unit MAY proactively fetch the EDP content at the ``policy_uri`` to check for updates, without waiting for a Digital Credential revocation signal.
    However, this mechanism SHOULD NOT be used in this specification for the following reason:

    - It enables Attestation Provider to unilaterally change an EDP, and it may introduce privacy risks and management overhead (as stated in the Discussion Topic D)
    - Technical details of this mechanism are not defined within ETSI standard.

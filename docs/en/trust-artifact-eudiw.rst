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
The Register dataset and read API are `EUDI-TS 5`_, objects ``WalletRelyingParty`` and ``WalletRelyingPartyService``, and satisfy Annex II of `CIR2025/848`_ as amended by [`CIR2026/1730`_].
Cardinality of Services, access certificates and registration certificates is [`EIDAS-ARF`_] Reg_10a, Reg_10d, Reg_33, Reg_34 and RPRC_07a.

.. note::
    **Profile deviation.** `EUDI-TS 5`_ marks ``serviceIdentifier`` as ``[0..1]``.
    This specification REQUIRES it on every registered Service, unique within the entity, because Reg_10a issues at least one WRPAC per Service and Reg_33 and RPRC_07a require that identifier in the WRPAC and in the WRPRC.

Register Dataset
""""""""""""""""

The data format for the information available through the open API provided by the national Register of WRPs MUST comply with the data schemas described in Tables 1-11 of Annex VI of [`CIR2025/848`_] as amended by [`CIR2026/1730`_], encoded as the ``WalletRelyingParty`` JSON Schema of `EUDI-TS 5`_.
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

The read methods are Section 3 of `EUDI-TS 5`_.
Methods, filter parameters, response codes and the slicing of ``services`` when ``serviceidentifier`` is used are defined there.

.. note::
    The published API view excludes only ``postalAddress`` ([`CIR2025/848`_] as amended by [`CIR2026/1730`_], Annex I, point 4).
    All other fields, including intended-use credential claims, are published as registered.
    The Register Open APIs remain for publication and transparency ([`EIDAS-ARF`_] Reg_03, Reg_06).
    The Wallet Unit MUST NOT use them as a substitute for a missing or invalid Wallet-Relying Party Registration Certificate during Credential Presentation or Credential Issuance, as specified in :ref:`trust-evaluation:EUDIW Authorization`.

The YAML file of the OpenAPI specification described in Section 3 of `EUDI-TS 5`_ is available as `EUDI-TS 5 OpenAPI`_.
The JSON Schema of the ``WalletRelyingParty`` object, including the ``services`` array of ``WalletRelyingPartyService``, is available as `EUDI-TS 5 JSON Schema`_.
The national read profile of that API is available :raw-html:`<a href="OAS3-Register-API-READ.html" target="_blank">here</a>`.

Wallet-Relying Party Access Certificate (WRPAC) Profile
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section extends the general :ref:`infrastructure-trust:X.509 Certificate Profile` and specifies a **Certificate Profile** for **Wallet-Relying Party Access Certificates (WRPACs)**.

The WRPAC is the certificate defined in Article 2 and Annex IV of [`CIR2025/848`_].
Its profile is `ETSI TS 119 411-8`_.
Extensions not specified by that document MUST NOT be present.
Subject attributes and the number of certificates are [`EIDAS-ARF`_] Reg_10a, Reg_31, Reg_32, Reg_33, Reg_34 and Reg_34a.
Authentication is specified in :ref:`trust-evaluation:EUDIW Authentication`.
Revocation on suspension or cancellation of the WRP services is specified in :ref:`infrastructure-trust:Trust Management and Lifecycle`.

`ETSI TS 119 411-8`_ does not yet define a dedicated attribute for the Relying Party Service identifier (Reg_33) or for the association to an intermediated Relying Party (Reg_34a).
Until it does, this specification encodes both in ``subjectAltName`` as follows.
The contact ``GeneralName`` required by `ETSI TS 119 411-8`_ remains.

.. list-table:: IT-Wallet encoding of the WRPAC Service identifier
   :header-rows: 1
   :widths: 25 75

   * - **Extension**
     - **Profile**

   * - ``subjectAltName``
     - REQUIRED, in addition to the contact ``GeneralName`` specified in `ETSI TS 119 411-8`_.
       It MUST include a ``uniformResourceIdentifier`` whose last path segment is the Relying Party Service identifier of this certificate (``services[].serviceIdentifier`` in the Register).
       That URI MUST be unique within the entity and MUST be identical to the ``srv_id`` of every WRPRC issued for the same Service of the same entity ([`EIDAS-ARF`_] Reg_33, RPRC_07a).

       If the subject is an Intermediary presenting on behalf of an intermediated Relying Party, the certificate MUST additionally include a second ``uniformResourceIdentifier`` of the form ``{registryURI}/wrp/{intermediatedRpIdentifier}/services/{intermediatedServiceIdentifier}``, where ``intermediatedRpIdentifier`` is the EU-wide unique identifier of that Relying Party ([`EIDAS-ARF`_] Reg_32) and ``intermediatedServiceIdentifier`` is the identifier of the intermediated Relying Party Service ([`EIDAS-ARF`_] Reg_33).
       That URI is the IT-Wallet encoding of [`EIDAS-ARF`_] Reg_34a.

.. note::
    The WRPAC attributes MUST be derived from the Register as specified in clause 5.1.2 of `ETSI TS 119 475`_.

    **Profile deviation.** Certificate Transparency ([`EIDAS-ARF`_] CT_01 to CT_06) is not a requirement of this specification until the ARF Technical Specifications make it fully available and clear for implementations.
    The WRPAC profile does not include a Signed Certificate Timestamp, the Provider of WRPAC is not required to log issued WRPACs, and the Wallet Unit is not required to verify Certificate Transparency during Authentication.

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

This section profiles the Wallet-Relying Party Registration Certificate (WRPRC) defined in `EIDAS-ARF`_ and `ETSI TS 119 475`_.
Its contents are clause 5.1, clause 5.2.4 and Annex A.2 of `ETSI TS 119 475`_, and Annex V paragraph 3 of [`CIR2025/848`_].
It is a signed JWT or a CWT (:rfc:`8392`), signed with the private key of the Provider of Wallet-Relying Party Registration Certificates.
The JWT signature is a JAdES signature with the B-B profile (`ETSI TS 119 182-1`_).
The CWT signature follows :rfc:`9052` and :rfc:`9360`.

Each WRPRC is bound to a single Relying Party Service.
The Provider of WRPRC issues WRPRCs automatically as defined in :ref:`onboarding-system:Wallet-Relying Party Registration Certificate Issuance`.

.. note::
    **Profile.** The ``name`` claim MUST equal the ``serviceTradeName`` of that Service and, for a non-intermediated presentation, MUST be identical to the ``subject.commonName`` of the WRPAC of the same Service of the same entity ([`EIDAS-ARF`_] Reg_34, RPRC_07a).
    `ETSI TS 119 475`_ does not yet define ``srv_id``.
    This specification profiles it to implement [`EIDAS-ARF`_] RPRC_07a until that standard defines an equivalent member.
    The claim is a JSON string (JWT) or a CBOR text string (CWT).
    It MUST equal the ``serviceIdentifier`` of that Service and, for a non-intermediated presentation, MUST be identical to the Service identifier encoded in the WRPAC ``subjectAltName`` ([`EIDAS-ARF`_] Reg_33).

The ``intermediary`` object is clause 5.2.4 of `ETSI TS 119 475`_ and [`EIDAS-ARF`_] RPRC_04.
The Wallet Unit evaluates intermediated presentation, including the WRPAC ``subjectAltName`` association of [`EIDAS-ARF`_] Reg_34a, as specified in :ref:`trust-evaluation:EUDIW Authorization`.

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

Trusted List, Lists of Trusted Lists, and Lists of Trusted Entities
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section describes the format and contents of three types of Trust Artifacts, each of which conveys a list of current and historical Trust Anchors (containers of cryptographic materials and identifiers belonging to trusted Entities).

Ecosystem Entities utilize these lists to:

- **Validate runtime trustworthiness**: Verify a Trust Anchor (see :ref:`infrastructure-trust:Trust Anchor Certificate Profile`) to authenticate, authorize, or validate an entity or artifact during live operations.
- **Perform historical validation**: Validate information contained within the list for historical audit purposes.

The table below maps each list to its legal basis, governing standard, format and publication.
The XML schema of Trusted Lists and of the List of Trusted Lists is published at ``https://forge.etsi.org/rep/esi/x19_612_trusted_lists/-/raw/v2.4.1/19612_xsd.xsd``.
The machine-readable List of Trusted Lists and the National Trusted Lists are published at `EUMS-LOTL`_.
The normative JSON and XML schemas of the Lists of Trusted Entities are published at `ETSI-LOTE-SCHEMAS`_.

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

An Embedded Disclosure Policy (EDP) is defined in Article 2(9) of [`CIR2024/2979`_].
Applicability and the three common policy types are Article 10 and Annex III of [`CIR2024/2979`_], encoded in Section 4.2.5.2 of `ETSI TS 119 472-3`_ (ISS-MDATA-EBD-4.2.5.2-06, ISS-MDATA-EBD-4.2.5.2-07, ISS-MDATA-EBD-4.2.5.2-08 and ISS-MDATA-EBD-4.2.5.2-09).
An EDP MUST NOT be applied to a PID.
The Wallet Unit evaluates the common types as specified in :ref:`trust-evaluation:EUDIW Authorization`.
Non-disclosure towards the Relying Party is Section 4.2.5.1 of `ETSI TS 119 472-3`_.

The Attestation Provider MUST include the EDP, if any, as the ``embedded_disclosure_policy`` member of ``credential_metadata`` within ``credential_configurations_supported``, in compliance with `OpenID4VCI`_ or the extension thereof specified in `ETSI TS 119 472-3`_.
The member MUST contain a ``policy_uri`` and MAY contain the complete policy data in ``policy_data``.
The Wallet Unit MAY receive only ``policy_uri`` when the exact policy identified by that URI is already preloaded; otherwise the URI and policy data MUST be provided together.
An unresolved URI MUST cause the association and the affected disclosure to fail.

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

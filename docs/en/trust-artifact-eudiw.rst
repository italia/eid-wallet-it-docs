.. include:: ../common/common_definitions.rst
.. include:: ../common/symbols.rst

EUDIW Trust Artifacts
---------------------

This section defines the required trust artifacts and their conceptual roles in the EUDIW ecosystem as per `EIDAS-ARF`_, including:

- :ref:`infrastructure-trust:Register of WRPs`; 
- :ref:`infrastructure-trust:Wallet-Relying Party Access Certificate (WRPAC) Profile`;
- :ref:`infrastructure-trust:Registrar Sign/Seal Certificate Profile`
- :ref:`infrastructure-trust:Wallet-Relying Party Registration Certificate (WRPRC) Profile`;
- :ref:`infrastructure-trust:Trusted List, Lists of Trusted Lists, and Lists of Trusted Entities`;
- :ref:`infrastructure-trust:Embedded Disclosure Policy (EDP)`.

Register of WRPs
^^^^^^^^^^^^^^^^

The national Register of WRPs is the publicly accessible system (dataset + API) that provides signed/sealed registration statements about WRPs and their authorisations/declared usage.

The data format for the information available through the open API provided by the national Register of WRPs MUST comply with the data schemas described in Tables 1-11 of the Annex VI of the `CIR2025/848-Amendment`_.
Below some non-normative examples of WRP objects stored in the Register. 

A bank registered as a Relying Party requesting PID for know-your-customer procedures.

.. literalinclude:: ../../examples/register-wrp-rp.json
  :language: JSON

A bank registered as both a Relying Party requesting PID and a QEAA Provider (issuing bank account attestations to Wallet). It has both ``intendedUse`` and ``providesAttestations``.

.. literalinclude:: ../../examples/register-wrp-rp-ap.json
  :language: JSON

An entity registered as a designated Intermediary that acts on behalf of WRPs during Wallet interactions. It has ``isIntermediary: true`` and does not declare ``intendedUse`` (not required when registering solely as an Intermediary).

.. literalinclude:: ../../examples/register-wrp-rp-intermediary.json
  :language: JSON


Common Register Open APIs
"""""""""""""""""""""""""

This section documents a `TS05`_ aligned common Register API profile that satisfies Annex II of `CIR2025/848`_ and `CIR2025/848-Amendment`_ constraints.

The common API read methods (GET) MUST be open for public access (no prior authentication), return JWS-signed statements, 
and provide methods for searching and querying complete data sets of registered WRPs matching with provided query parameters.
  
- **GET /wrp**: Get a list of WRPs with optional filtering (defined in Annex VI of `CIR2025/848-Amendment`_) and pagination.
  A successful response (``200``) MUST be a JWS-signed response body. The decoded payload MUST contain an array of ``WalletRelyingParty`` objects matching the query, and, where relevant, accompanied by WRPAC history information in the statement/profile used by the Member State. The list of all registered WRPs is returned when no query parameters are provided.
- **GET /wrp/check-intended-use**: A dedicated intended-use check endpoint for making narrowed-down intended use related queries from the Register. A successful response (``200``) MUST provide a JWS-signed boolean ``true`` or ``false`` response, determined by the queried parameter in the Registrar's Intended use information for the specific WRP. 
  If the request is invalid/incomplete or the given WRP is not found, the endpoint MUST answer with error code ``400`` and ``401``, respectively.

.. note::
    The published API view excludes only `postalAddress` (`CIR2025/848-Amendment`_, Annex I, point 4). All other fields, including intended-use credential claims, are published as registered.

The base OpenAPI Specification is available :raw-html:`<a href="OAS3-Register-API-READ.html" target="_blank">here</a>`.

Wallet-Relying Party Access Certificate (WRPAC) Profile
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section extends the general :ref:`x509-certificate-profile:X.509 Certificate Profile` and specifies a **Certificate Profile** for **Wallet-Relying Party Access Certificates (WRPAC)**.

According to the Article 2 of [`CIR2025/848`_], a WRPAC is a certificate for electronic seals or signatures authenticating and validating the WRP when they interact with the EUDI Wallet. For more details on the authentication process, see :ref:`trust-evaluation-eudiw:Authentication Process`.

The suspension or cancellation of the WRP services, involves revocation of all valid WRPAC by the relevant issuing authority, such that the WRP is no longer able to interact with Wallet Units. For more detail on the Trust Management processes, see :ref:`infrastructure-trust:EUDIW Trust Management Process`.

Annex IV of [`CIR2025/848`_] also states that the WRPACs are meant for performing electronic signatures or seals and that they MUST comply with at least the Normalised Certificate Policy (NCP) requirements specified in the ETSI standards. 
Taking into account these minimal requirements, different scenarios are possible and specified in the following clauses: certificates issued to natural or legal persons, supporting advanced signatures/seals or even qualified signature/seals. Conditional requirements are defined according to the specific case the WRPACs fall into.

The specific requirements for WRPACs are specified in `ETSI TS 119 411-8`_.

- Basic Fields: all required, as described in :ref:`x509-certificate-profile:X.509 Certificate Profile`.

- Extensions:

  - ``subjectKeyIdentifier``: for end-entity certificates, the subject key identifier extension provides a means of identifying certificates that contain the particular public key used in an application. The subject key identifier SHOULD be derived from the public key using the methods defined in Clause 4.2.1.2 of [:rfc:`5280`].

  - ``keyUsage``: it MUST contain exactly one of the following key usage
    settings: *Type A*, *Type B*, *Type C*, or *Type F*.

  - ``certificatePolicies``: it MUST include a ``PolicyInformation`` term with
  
    - ``policyIdentifier`` containing one of the following OIDs defined in [`ETSI TS 119 411-8`_]

      * ``0.4.0.194118.1.1`` (``NCP-n-eudiwrp``)
      * ``0.4.0.194118.1.2`` (``NCP-l-eudiwrp``)
      * ``0.4.0.194118.1.3`` (``QCP-n-eudiwrp``)
      * ``0.4.0.194118.1.4`` (``QCP-l-eudiwrp``)

    - ``policyQualifiers`` containing a ``CPSuri`` that references an URL where the CPS of the Provider of WRPAC is located.

  - ``authorityInfoAccess``: it MUST be present and include an ``AccessDescription`` term with ``1.3.6.1.5.5.7.48.2`` (``id-ad-caIssuers``) as ``accessMethod`` and ``accessLocation`` specifying at least one access location of a valid CA certificate of the issuing CA.

  - ``qcStatements``: TBD.

  - At least one of the following conditions MUST apply:

    * ``cRLDistributionPoints`` is present and contains at least one reference to a publicly available Certificate Revocation List (CRL), as described in :ref:`infrastructure-trust:Certificate Revocation List (CRL)`.

    * ``authorityInfoAccess`` additionally includes an ``AccessDescription`` term with ``1.3.6.1.5.5.7.48.1`` (``id-ad-ocsp``) as ``accessMethod`` and ``accessLocation`` specifying at least one access location of an OCSP responder providing status information for the present certificate, as described in :ref:`infrastructure-trust:Online Certificate Status Protocol (OCSP)`.

.. note::
    **Dependency Considerations**: The WRPAC attributes MUST be derived from the information held in the Register as specified in clause 5.1.2 of `ETSI_TS_119_475`_ `ETSI_TS_119_475`_. This also implies that for some specific attributes in the WRPAC the same value MUST be encountered in the corresponding WRPRC if any.

The following is an example of a WRPAC for legal persons following the NCP.

.. literalinclude:: ../../examples/wrpac-ncp.txt
  :language: text

Registrar Sign/Seal Certificate Profile
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section extends the general :ref:`x509-certificate-profile:X.509 Certificate Profile` and specifies a **Certificate Profile** for **Registrar Sign/Seal Certificates**.

The specific requirements for WRPACs are specified in `CIR 2025/848`_.

- Basic Fields: all required, as described in :ref:`x509-certificate-profile:X.509 Certificate Profile`.

- Extensions:

  - ``certificatePolicies``: it MUST include a ``PolicyInformation`` term with ``0.4.0.2042.1.1`` (*NCP*) as ``policyIdentifier``.

  - At least one of the following conditions MUST apply:

    * ``cRLDistributionPoints`` is present and contains at least one reference to a publicly available Certificate Revocation List (CRL), as described in :ref:`infrastructure-trust:Certificate Revocation List (CRL)`.

    * ``authorityInfoAccess`` additionally includes an ``AccessDescription`` term with ``1.3.6.1.5.5.7.48.1`` (``id-ad-ocsp``) as ``accessMethod`` and ``accessLocation`` specifying at least one access location of an OCSP responder providing status information for the present certificate, as described in :ref:`infrastructure-trust:Online Certificate Status Protocol (OCSP)`.

Wallet-Relying Party Registration Certificate (WRPRC) Profile
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section defines Wallet-Relying Party Registration Certificate (WRPRC), as described in the `EIDAS-ARF`_ and `ETSI_TS_119_475`_. This Trust Artifact provides detailed information about the Credential Issuer and Relying Party's Authorization profile, including:
- core identification attributes (clause 5.1 `ETSI_TS_119_475`_), 
- service description attributes (clause 5.2.4 `ETSI_TS_119_475`_), 
- entitlement attributes (see Annex A.2 `ETSI_TS_119_475`_), 
- supervisory authority attributes (clause 5.2.4 `ETSI_TS_119_475`_),
- Relying Party attributes (clause 5.2.4 `ETSI_TS_119_475`_),
- Credential Issuer attributes (clause 5.2.4 `ETSI_TS_119_475`_),
- Intermediaty attributes; i.e., whether the Relying Party relies on an Intermediary to request Digital Credentials (clause 5.2.4 `ETSI_TS_119_475`_).

The Wallet-Relying Party Registration Certificate MUST be formatted either as a signed JSON Web Token (JWT) or CBOR Web Token (CWT) :rfc:`8392`. It MUST comply with the syntactic and semantic requirements specified in Annex V paragraph 3 of CIR (EU) 2025/848 and `ETSI_TS_119_475`_.

The Wallet-Relying Party Registration Certificate MUST be signed with the private key of Provider of the Wallet-Relying Party Registration Certificates. In particular,
- The JWT MUST be signed with a JSON Advanced Electronic Signature with the B-B profile as defined in `ETSI_TS_119_182_1`
- The CWT MUST be signed with an Advanced Electronic Signature following structure as defined in :rfc:`9052` and :rfc:`9360`.

Below are represented many non-normative examples of WRPRCs' headers and payloads. 

.. literalinclude:: ../../examples/wrprc-jwt-header.json
  :language: json

.. literalinclude:: ../../examples/wrprc-cwt-header.txt
  :language: text

.. literalinclude:: ../../examples/wrprc-payload-ci.json
  :language: json

.. literalinclude:: ../../examples/wrprc-payload-rpi.json
  :language: json

.. warning::

    `ETSI_TS_119_475`, Table 10 defines the intermediary name subfield as ``sname``. The example in Annex C of the same standard uses ``name`` instead. This specification follows the normative Table 10 and uses ``sname``.

Trusted List, Lists of Trusted Lists, and Lists of Trusted Entities
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    
This section describes the format and contents of three types of Trust Artifacts, each of which conveys a list of current and historical Trust Anchors (containers of an Entity public key and identifier which are assumed to be trusted).

Ecosystem Entities utilize these lists to:

- **Validate runtime trustworthiness**: Verify a Trust Anchor (see `:ref:trust-artifact-eudiw:Trust Anchor Certificate Profile`) to authenticate, authorize, or validate an entity or artifact during live operations.
- **Perform historical validation**: Validate information contained within the list for historical audit purposes.

The three distinct types of trust lists are:

- Trusted Lists (TLs): Established under Chapter II of Annex I of CID (EU) 2015/1505, as amended by CID (EU) 2025/2164, and specified in `ETSI_TS_119_612`_. Each Member State publishes one TL in XML format. It is signed by the respective Member State with an AdES digital signature at conformance level baseline B (as defined in `ETSI_TS_119_182_1`_). TLs are published in a machine-readable format at endpoints specified within the LOTL. These Lists hold current and historical information about the accreditation of trust service providers, referencing:

  - Qualified Trust Service Providers (QTSP)s, such as Qualified Certificates Issuing and revocation mechanisms, QEAA Providers, Qualified electronic archiving services.
  - Non-Qualified Trust Services such as EAA Providers, 
  - Other Trust Services defined at the national level, such as archiving.

   Within eIDAS, TLs are maintained by Member States, who are responsible for keeping record of the trusted services providers under their respective jurisdiction. They are numbered and renewed periodically, and published in a website for unrestricted download. To protect their integrity and assure authenticity, they are also signed with trusted certificates contained in the LOTL.

- List of Trusted Lists (LOTL): Established under Chapter II of Annex I of CID (EU) 2015/1505, as amended by CID (EU) 2025/2164, and specified in `ETSI_TS_119_612`_. There is only one LOTL, which is published in XML format and signed by the European Commission (EC). It utilizes an AdES digital signature at conformance level baseline B (per `ETSI_TS_119_182_1`_) and references the trusted certificates that each National Trusted List. To facilitate key rotation and continuous updates, the LOTL implements a pivoting mechanism. It is published in a machine-readable format at an endpoint specified within the Official Journal of the European Union (OJEU).

  The XML schema for both Trusted Lists and List of Trusted Lists, containing parameters' name and description can be found at https://forge.etsi.org/rep/esi/x19_612_trusted_lists/-/raw/v2.4.1/19612_xsd.xsd. Currently, the human-readable version of the LOTL and National TLs are published in the following URI: <https://ec.europa.eu/tools/lotl/eu-lotl.xml>.

- Lists of Trusted Entities (LoTE): Established under Articles 4 and 5 of [CIR 2024/2980] and specified in `ETSI_TS_119_602`_. These are available in either XML or JSON format and are signed with an AdES digital signature at conformance level baseline B (per `ETSI_TS_119_182_1`_). To facilitate continuous updates, the LoTE implements a pivoting mechanism and is published in a machine-readable format at an endpoint specified within the OJEU. The <artifacts:List of Trusted Entities (LoTE)|LoTE> types can be one of the following, as defined in annex C.2:

  - PID Provider;
  - Wallet Provider;
  - Provider of Wallet Relying Party Access Certificates;
  - Providers of Wallet Relying Party Registration Certificates;
  - Public sector bodies issuing Electronic Attestations of Attributes;
  - List of Registrars and Registers.

  The following repository provides the normative JSON and XML schemas required for implementing the List of Trusted Entities https://forge.etsi.org/rep/esi/x19_60201_lists_of_trusted_entities.

The following table provides a comprehensive overview of the eIDAS trust list architecture, cross-referencing the legal basis, governing technical standards, explicit data formats, signature profiles, and publication dynamics for Trusted Lists (TL), the List of Trusted Lists (LOTL), and the various category-specific Lists of Trusted Entities (LoTE).

.. list-table:: eIDAS Trust List Ecosystem Profiles
   :class: longtable
   :header-rows: 1

   * - List Type
     - Legal Basis
     - Governing Standard & Format
     - Signature Profile
     - Scope & Signer
     - Publication & Update Mechanism
   * - **Trusted Lists (TL)**
     - CID (EU) 2015/1505 (Annex I, Chapter II), amended by CID (EU) 2025/2164.
     - ETSI TS 119 612; ``XML`` format.
     - AdES digital signature, baseline B (ETSI TS 119 182-1).
     - Member State scope; one list per Member State, signed by that Member State.
     - Machine-readable endpoint specified within the LOTL.
   * - **List of Trusted Lists (LOTL)**
     - CID (EU) 2015/1505 (Annex I, Chapter II), amended by CID (EU) 2025/2164.
     - ETSI TS 119 612; ``XML`` format.
     - AdES digital signature, baseline B (ETSI TS 119 182-1).
     - European Union scope; a single global list signed by the European Commission (EC) that anchors the National Trusted Lists.
     - Machine-readable endpoint specified within the OJEU. Implements a pivoting mechanism to handle continuous updates.
   * - **LoTE: PID Provider Lists**
     - Articles 4 and 5 of [CIR 2024/2980].
     - ETSI TS 119 602 Annex D; ``JSON`` format.
     - AdES digital signature, baseline B (ETSI TS 119 182-1).
     - European Union scope; one list per specific ecosystem entity type.
     - Machine-readable endpoint specified within the OJEU. Implements a pivoting mechanism to handle continuous updates.
   * - **LoTE: Wallet Provider (WP) Lists**
     - Articles 4 and 5 of [CIR 2024/2980].
     - ETSI TS 119 602 Annex E; ``JSON`` format.
     - AdES digital signature, baseline B (ETSI TS 119 182-1).
     - European Union scope; one list per specific ecosystem entity type.
     - Machine-readable endpoint specified within the OJEU. Implements a pivoting mechanism to handle continuous updates.
   * - **LoTE: Provider of WRPAC Lists**
     - Articles 4 and 5 of [CIR 2024/2980].
     - ETSI TS 119 602 Annex F; ``JSON`` format.
     - AdES digital signature, baseline B (ETSI TS 119 182-1).
     - European Union scope; one list per specific ecosystem entity type (Wallet Relying Party Access Certificate).
     - Machine-readable endpoint specified within the OJEU. Implements a pivoting mechanism to handle continuous updates.
   * - **LoTE: Provider of WRPRC Lists**
     - Articles 4 and 5 of [CIR 2024/2980].
     - ETSI TS 119 602 Annex G; ``JSON`` format.
     - AdES digital signature, baseline B (ETSI TS 119 182-1).
     - European Union scope; one list per specific ecosystem entity type (Wallet Relying Party Registration Certificate).
     - Machine-readable endpoint specified within the OJEU. Implements a pivoting mechanism to handle continuous updates.
   * - **LoTE: PuB-EAA Provider Lists**
     - Articles 4 and 5 of [CIR 2024/2980].
     - ETSI TS 119 602 Annex H; ``JSON`` or ``XML`` format.
     - AdES digital signature, baseline B (ETSI TS 119 182-1).
     - European Union scope; one list per specific ecosystem entity type.
     - Machine-readable endpoint specified within the OJEU. Implements a pivoting mechanism to handle continuous updates.
   * - **LoTE: Registrar and Register Provider Lists**
     - Articles 4 and 5 of [CIR 2024/2980].
     - ETSI TS 119 602 Annex I; ``JSON`` format.
     - AdES digital signature, baseline B (ETSI TS 119 182-1).
     - European Union scope; one list per specific ecosystem entity type.
     - Machine-readable endpoint specified within the OJEU. Implements a pivoting mechanism to handle continuous updates.

The example below shows a non-normative example of payload of a List of Trusted Entities for PID Providers

.. literalinclude:: ../../examples/lote-pid.json
  :language: json

Embedded Disclosure Policy (EDP)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An Embedded Disclosure Policy (EDP) is defined in Article 2(9) of CIR 2024/2979 as: *"A set of rules, embedded in an electronic attestation of attributes by its provider, that indicates the conditions that a wallet-relying party has to meet to access the electronic attestation of attributes"*.

Attestation Providers (i.e., all Credential Issuers except the PID Provider) can optionally express an EDP which allow indicating which Relying Parties can access specific Digital Credentials. The Article 10 of CIR 2024/2979 establishes that Wallet Providers MUST ensure that Attestations with common EDPs (as listed in Annex III of CIR 2024/2979) can be processed by their Wallet Units.

EDPs are applicable to QEAAs, PuB-EAAs, and EAAs. They MUST NOT be applicable to PIDs.

The EDP is distributed through the Credential Issuer Metadata at issuance time. The Attestation Provider MUST include the EDP (if any) by value in the Credential Issuer Metadata, within the ``credential_configurations_supported`` parameter, in compliance with `OpenID4VCI`_ or the extension thereof specified in `ETSI TS 119 472-3`. If availble, the Wallet Unit MUST store the EDP locally and associate it with the specific Attestation for which it was retrieved. The Wallet Unit MUST NOT reveal the EDP to the Relying Party through the presentation protocol as per `ETSI TS 119 472-3`_, Section 4.2.5.1.

Embedded Disclosure Policies are used to:

- Implementing sector-specific access control (e.g., only public sector RPs or only healthcare RPs).
- Implementing Member-State-specific access control (e.g., only RPs registered within a specific Member State).

Annex III of [CIR 2024/2979] defines three common EDP types:

- **No Policy.** No EDP is present, or the EDP explicitly indicates that no restrictions apply (ISS-MDATA-EBD-4.2.5.2-06).

- **Authorized Relying Parties Only.** The EDP contains a list of RPs that are allowed to access the Attestation. According to `ETSI_TS_119_472_3 `_(ISS-MDATA-EBD-4.2.5.2-07), authorized RPs are identified by their subject distinguished name as held in the Wallet-Relying Party Access Certificate, in LDAP string form as defined in :rfc:`4514`.

  - For legal persons, the relevant DN attributes are ``commonName``, ``organizationName``, ``organizationIdentifier``, and ``countryName``. 
  - For natural persons: ``commonName``, ``givenName``, ``surname``, ``serialNumber``, and ``countryName``. The ``organizationIdentifier`` attribute type is represented by the LDAP string "ORGID"; the ``serialNumber`` attribute type is represented by "SN" (according to `ETSI_TS_119_472_3`_ NOTE 1 and NOTE 2 to ISS-MDATA-EBD-4.2.5.2-07).

- **Specific Root of Trust.** The EDP contains a list of trusted roots or intermediate certificates. Only RPs whose Wallet-Relying Party Access Certificate chain to one of these roots are allowed to access the Attestation. According to `ETSI_TS_119_472_3`_ (ISS-MDATA-EBD-4.2.5.2-08/09), each authorized root is identified by its issuer distinguished name in LDAP string form as defined in RFC 4514 and the issuer's certificate serial number.

.. note::

  `ETSI_TS_119_472_3 `_(ISS-MDATA-EBD-4.2.5.2-07) also allows identifying authorized RPs by URI-encoded entitlements as specified in `ETSI_TS_119_475`_, held in the Wallet-Relying Party Registration Certificate. Annex A.3 of `ETSI_TS_119_475`_, defines sub-entitlements for Service Providers, currently for Payment Service Providers (e.g. ``https://uri.etsi.org/19475/SubEntitlement/psp/psp-ai``). Future versions may include additional sector-specific sub-entitlements at national or EU level. This specification supports both the subject DN and the entitlement URI identification mechanisms.

.. note::

  `EIDAS-ARF`_ HLR EDP_02 refers to *EU-wide unique identifiers*, as defined in Reg_32, for the authorized RP list. `ETSI_TS_119_472_3`_ (ISS-MDATA-EBD-4.2.5.2-07) identifies authorized RPs by their subject DN from the Wallet-Relying Party Access Certificate. The ``organizationIdentifier`` attribute within the DN has the same semantics as the identifier given in `EIDAS-ARF`_ HLR Reg_32. This specification aligns with the `ETSI_TS_119_472_3`_ formulation.

Embedded Disclosure Policy Data Model
""""""""""""""""""""""""""""""""""""""

The following table provides a comprehensive overview of the Embedded Disclosure Policy data model, including parameter names, data types, descriptions, and the specific clauses in `ETSI_TS_119_472_3`_ where each parameter is defined.

.. list-table:: Embedded Disclosure Policy Parameters
   :class: longtable
   :header-rows: 1
   :widths: 20 15 45 20

   * - **Parameter**
     - **Type**
     - **Description**
     - **Defined in**

   * - ``policy_uri``
     - string (URI)
     - REQUIRED. Unique identifier of the Embedded Disclosure Policy (EDP). 

       The association of the EDP with an EAA MUST be established by including this unique URI. The AP MUST either include the URI together with the full policy data set, or provide only the URI if the policy data set has already been pre-loaded into the Wallet Instance (WI). The EDP MAY be accessible through this URI.
     - Clause 4.2.5.2 of [`ETSI_TS_119_472_3`_] (ISS-MDATA-EBD-4.2.5.2-01, ISS-MDATA-EBD-4.2.5.2-02, ISS-MDATA-EBD-4.2.5.2-03)

   * - ``policy_type``
     - string
     - REQUIRED. Policy type classification. Valid values:

       * ``"no_policy"``: Indicates that no policy restrictions apply for the associated EAA.
       * ``"authorized_rp_only"``: Access is restricted to an explicit list of allowed Relying Parties.
       * ``"specific_root_of_trust"``: Access is restricted to Relying Parties chaining to specified trusted roots.
     - Clause 4.2.5.2 of [`ETSI_TS_119_472_3`_] (ISS-MDATA-EBD-4.2.5.2-06, ISS-MDATA-EBD-4.2.5.2-07, ISS-MDATA-EBD-4.2.5.2-08)

   * - ``description``
     - string
     - OPTIONAL. Description of the applicability of the policy to a particular community and/or class of application sharing common security requirements.
     - Clause 4.2.5.2 of [`ETSI_TS_119_472_3`_] (ISS-MDATA-EBD-4.2.5.2-04)

   * - ``policy_authority``
     - string
     - OPTIONAL. Identifier of the authority or entity responsible for the policy.
     - Clause 4.2.5.2 of [`ETSI_TS_119_472_3`_] (ISS-MDATA-EBD-4.2.5.2-05)

   * - ``policy_info_url``
     - string (URL)
     - OPTIONAL. Link to a website of the Attestation Provider (AP) explaining the disclosure policy guidelines in layman's terms.
     - Clause 4.2.5.2 of [`ETSI_TS_119_472_3`_] (ISS-MDATA-EBD-4.2.5.2-13, EDP_05)

   * - ``authorized_parties``
     - array of objects
     - REQUIRED if ``policy_type`` is ``"authorized_rp_only"``. Contains a list of authorized Relying Parties allowed to access the Attestation.
     - Clause 4.2.5.2 of [`ETSI_TS_119_472_3`_] (ISS-MDATA-EBD-4.2.5.2-07)

   * - ``authorized_parties[].subject_dn``
     - string
     - OPTIONAL. Subject Distinguished Name (DN) of the Relying Party extracted from its Wallet-Relying Party Access Certificate (WRPAC), formatted as an LDAP string compliant with :rfc:`4514`. At least one of ``subject_dn`` or ``entitlement_uri`` MUST be present in each element.
     - Clause 4.2.5.2 of [`ETSI_TS_119_472_3`_] (ISS-MDATA-EBD-4.2.5.2-07)

   * - ``authorized_parties[].entitlement_uri``
     - string (URI)
     - OPTIONAL. URI-encoded entitlement or sub-entitlement as specified in Annex A of [`ETSI_TS_119_475`_], held within the Wallet-Relying Party Registration Certificate (WRPRC). At least one of ``subject_dn`` or ``entitlement_uri`` MUST be present in each element.
     - Clause 4.2.5.2 of [`ETSI_TS_119_472_3`_] (ISS-MDATA-EBD-4.2.5.2-07)

   * - ``trusted_roots``
     - array of objects
     - REQUIRED if ``policy_type`` is ``"specific_root_of_trust"``. Defines a precise list of trusted root or intermediate certificates. Only RPs whose WRPACs successfully chain to one of these roots are permitted access.
     - Clause 4.2.5.2 of [`ETSI_TS_119_472_3`_] (ISS-MDATA-EBD-4.2.5.2-08)

   * - ``trusted_roots[].issuer_dn``
     - string
     - REQUIRED. Issuer Distinguished Name (DN) in LDAP string form compliant with :rfc:`4514`.
     - Clause 4.2.5.2 of [`ETSI_TS_119_472_3`_] (ISS-MDATA-EBD-4.2.5.2-09)

   * - ``trusted_roots[].serial_number``
     - string
     - REQUIRED. Certificate serial number corresponding to the defined issuer.
     - Clause 4.2.5.2 of [`ETSI_TS_119_472_3`_] (ISS-MDATA-EBD-4.2.5.2-09)

   * - ``extensions``
     - array of objects
     - OPTIONAL. Container for supplementary EDP extension structures. 

       These structures MAY be ignored by the Wallet Unit, but the Wallet Unit SHOULD successfully process the remaining EDP data even if unrecognized extensions are present. Extensions MAY be used to supply alternative policy rules applied to specific attributes within an EAA subject to Selective Disclosure.
     - Clause 4.2.5.2 of [`ETSI_TS_119_472_3`_] (ISS-MDATA-EBD-4.2.5.2-10, ISS-MDATA-EBD-4.2.5.2-11, ISS-MDATA-EBD-4.2.5.2-12)

The following are non-normative examples of EDPs with Authorized Relying Parties Only and Specific Root of Trust policy types.

.. literalinclude:: ../../examples/edp-authorized-rps.json
  :language: json

.. literalinclude:: ../../examples/edp-specific-root.json
  :language: json

Embedded Disclosure Policy Lifecycle
""""""""""""""""""""""""""""""""""""

The locally stored EDP MUST remain valid as long as the Attestation it is associated with is valid and not revoked. The EDP MUST NOT have an independent validity status or revocation mechanism separate from the Attestation.

If an Attestation Provider adds, changes, or deletes an EDP for a Digital Credential it issues, the Attestation Provider MUST revoke that Digital Credential. The Wallet Unit detects the EDP change indirectly through the normal Attestation status checking mechanism (Status List), which will report that the Digital Credential as revoked. The locally stored EDP is then implicitly invalidated together with the Digital Credential. The User needs to request a new issuance to obtain the Digital Credential with the updated EDP.

Even a minor policy change (e.g., adding a single RP to the authorized list) requires revocation and re-issuance. The timing of detection depends on when the Wallet Unit checks the Digital Credential status: if the WI checks only at presentation time, a policy change will not be detected until the next presentation attempt.

.. warning::

    **Proactive refresh**. The Attestation Provider MAY provide EDP though its URI. In this case, the Wallet Unit MAY proactively fetch the EDP content at the ``policy_uri`` to check for updates, without waiting for a Digital Credential revocation signal. However, this mechanism SHOULD NOT be used in this specification for the following reason:
    
    - It enables Attestation Provider to unilaterally change an EDP, and it may introduce privacy risks and management overhead (as stated in the Discussion Topic D)
    - Technical details of this mechanism are not defined within ETSI standard.



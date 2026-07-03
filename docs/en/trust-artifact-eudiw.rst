.. include:: ../common/common_definitions.rst
.. include:: ../common/symbols.rst

EUDIW Trust Artifacts
---------------------

This section defines the required trust artifacts and their conceptual roles in the EUDIW ecosystem as per `EIDAS-ARF`_, including:

- :ref:`trust-artifact-eudiw:Register of WRPs`, 
- :ref:`trust-artifact-eudiw:X509 Certificate Profiles`, containing the following specialized profiles:

  - :ref:`trust-artifact-eudiw:Wallet-Relying Party Access Certificate (WRPAC) Profile`, 
  - :ref:`trust-artifact-eudiw:Entity Sign/Seal Certificate Profile`, and 
  - :ref:`trust-artifact-eudiw:Trust Anchor Certificate Profile`.

- :ref:`trust-artifact-eudiw:Wallet-Relying Party Registration Certificate (WRPRC) Profile`,
- :ref:`trust-artifact-eudiw:Trusted List, Lists of Trusted Lists, and Lists of Trusted Entities`, and 
- :ref:`trust-artifact-eudiw:Embedded Disclosure Policy Data Model`.

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

.. warning::
    DA CAPIRE - controllare: 

    1. he name of some query parameters differ from [TS05] and the corresponding YAML file ts5-openapi31-registrar-api.yml containing the OpenAPI specification of the JSON and REST based application programming interfaces (e.g., intendedusecredentialmeta vs credentialmeta). This profile follows the OpenAPI specification.
    In addition, this specification adds providesattestation to cover the [CIR 2025/848-Amendment] requirement for filtering parameter: type of attestations provided, returning the complete data set of each of the registered wallet-relying parties matching the value provided for this parameter.

    2. where relevant, accompanied by WRPAC history information in the statement/profile used by the Member State. come? 

    3. `postalAddress`  è corretto che non venga pubblicato nel register? alto?

    4. OpenAPI FILTRI: (1) nomi filtri da usare, Annex VI definisce endpoint e il fatto che ci siano dei filtri, i nomi li abbiamo presi da OpenAPI + (2) bastano openAPI o vogliamo le tabelle con i filtri nome filtri?

    5. oltre ai 2 endpoint obbligatori, ci sarebbe anche GET /wrp/{identifier} — get by identifier (OPTIONAL) - lo vogliamo implementare in IT Wallet?


- **GET /wrp — search/list**: Get a list of WRPs with optional filtering (defined in Annex VI of `CIR2025/848-Amendment`_) and pagination.
  A successful response (``200``) MUST be a JWS-signed response body. The decoded payload MUST contain an array of ``WalletRelyingParty`` objects matching the query, and, where relevant, accompanied by WRPAC history information in the statement/profile used by the Member State. The list of all registered WRPs is returned when no query parameters are provided.
- **GET /wrp/check-intended-use — intended use check**: A dedicated intended-use check endpoint for making narrowed-down intended use related queries from the Register. A successful response (``200``) MUST provide a JWS-signed boolean ``true`` or ``false`` response, determined by the queried parameter in the Registrar's Intended use information for the specific WRP. 
  If the request is invalid/incomplete or the given WRP is not found, the endpoint MUST answer with error code ``400`` and ``401``, respectively.

.. note::
    The published API view excludes only `postalAddress` (`CIR2025/848-Amendment`_, Annex I, point 4). All other fields, including intended-use credential claims, are published as registered.

Below is the Open API Specification for the common API read methods of the Register:

.. literalinclude:: ./oas3/OAS3-Register-API-READ.yaml
    :language: yaml
    :linenos:

X509 Certificate Profiles
^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section lists all the parameters and extensions that are required for an X509 certificate profile needed for EUDIW interoperability. This profile is general and is further specialized in the following cases:

- :ref:`trust-artifact-eudiw:Wallet-Relying Party Access Certificate (WRPAC) Profile`;
- :ref:`trust-artifact-eudiw:Trust Anchor Certificate Profile`;
- :ref:`trust-artifact-eudiw:Entity Sign/Seal Certificate Profile`.

The final binary certificate structure is constructed by combining the seven core parameters (from ``version`` through ``subjectPublicKeyInfo``) with the specific extensions mandated by the selected profile, and is subsequently encoded using the ASN.1 Distinguished Encoding Rules (DER) as described in :rfc:`5280`.

The table below lists the Certificate Profile Parameters for generic, EUDIW-compliant X509 certificates.

.. warning::
    TODO:

    3. aggiornare conseguentemente l'esempio

.. list-table:: Certificate Profile Parameters
   :class: longtable
   :header-rows: 1
   :widths: 20 55 25

   * - **Parameter**
     - **Description**
     - **Defined in**

   * - ``version``
     - REQUIRED. Indicates the version of the encoded certificate. For this profile, it MUST be ``v3`` (``2``).
     - :rfc:`5280#section-4.1.2.1`

   * - ``serialNumber``
     - REQUIRED. The serial number of the certificate.
     - :rfc:`5280#section-4.1.2.2`

   * - ``signature``
     - REQUIRED. Identifies the signature algorithm used by the Certificate Authority (CA) to sign the certificate. The signature algorithm SHOULD be selected according to [`ETSITS119312`_], but MAY be superseded by national recommendations.
     - :rfc:`5280#section-4.1.2.3`

   * - ``signature.algorithm``
     - REQUIRED. The OID of the signature algorithm. It MUST be one of the signature algorithms defined in :ref:`algorithms:Cryptographic Algorithms`.
     - :rfc:`5280#section-4.1.1.2`

   * - ``signature.parameters``
     - OPTIONAL. Algorithm-specific parameters, dependent on the algorithm used.
     - :rfc:`5280#section-4.1.1.2`

   * - ``issuer``
     - REQUIRED. Identifies the entity that has signed and issued the certificate.

       If the issuer is a legal person, the following attributes MUST be present:

       * ``countryName`` indicating the country in which the issuer of the certificate is established;
       * ``organizationName`` indicating the full registered name of the certificate issuing organization;
       * ``commonName`` indicating a name commonly used by the subject to represent itself;
       * conditionally, an ``organizationIdentifier`` if an appropriate registration number is known to exist, and it has a value different from the organization name.

       If the issuer is a natural person, the following attributes MUST be present:

       * ``countryName`` indicating a country that is consistent with the legal jurisdiction under which certificates are issued;
       * choice of (``givenName`` and/or ``surname``) or ``pseudonym``; if the given name or surname of the issuer is known, the respective attribute MUST be present;
       * ``commonName``;
       * ``serialNumber``.
     - clause 4.2.3 of [`ETSI_EN_319_412_2`_].

   * - ``validity``
     - REQUIRED. Time interval during which the Certificate Authority (CA) warrants that it will maintain information about the status of the certificate.
     - :rfc:`5280#section-4.1.2.5`.

   * - ``validity.notBefore``
     - REQUIRED. The date on which the certificate validity period begins. Dates through 2049 MUST use ``UTCTime``; dates in 2050 or later MUST use ``GeneralizedTime``.
     - :rfc:`5280#section-4.1.2.5`.

   * - ``validity.notAfter``
     - REQUIRED. The date on which the certificate validity period ends. Dates through 2049 MUST use ``UTCTime``; dates in 2050 or later MUST use ``GeneralizedTime``.
     - :rfc:`5280#section-4.1.2.5`.

   * - ``subject``
     - REQUIRED. Identifies the entity associated with the public key stored in the subject public key field. If present, the size of ``organizationName``, ``organizationalUnitName`` and ``commonName`` MAY be longer than the limit as stated in [RFC 5280].

       If the subject is a natural person, the following attributes MUST be present:

       * ``countryName`` indicating the general context in which other attributes are to be understood;
       * choice of (``givenName`` and/or ``surname``) or ``pseudonym``;
       * ``commonName`` indicating a name of the subject;
       * conditionally, ``serialNumber`` if the above attributes are not sufficient to ensure subject name uniqueness.

       When a natural person subject is associated with an organization, the attributes MAY also identify such organization using attributes like ``organizationName`` and ``organizationIdentifier``.

       If the subject is a legal person, the following attributes MUST be present:

       * ``countryName`` indicating the country in which the subject is established;
       * ``organizationName`` indicating the full registered name of the subject;
       * ``organizationIdentifier`` indicating an identification of the subject organization different from the organization name;
       * ``commonName`` indicating a name commonly used by the subject to represent itself.
     - clause 4.2.4 of [`ETSI_EN_319_412_2`_], clause 4.2.1 of [`ETSI_EN_319_412_3`_].

   * - ``subjectPublicKeyInfo``
     - REQUIRED. Carries the public key and identifies the algorithm with which the key is used. The subject public key SHOULD be selected according to [ETSI TS 119 312] but MAY be superseded by national recommendations.
     - :rfc:`5280#section-4.1.2.7`.

   * - ``subjectPublicKeyInfo.algorithm``
     - REQUIRED. The algorithm identifier for the public key. It MUST be one of the signature algorithms defined in :ref:`algorithms:Cryptographic Algorithms`.
     - :rfc:`5280#section-4.1.2.7`.

   * - ``subjectPublicKeyInfo.subjectPublicKey``
     - REQUIRED. The public key itself.
     - :rfc:`5280#section-4.1.2.7`.

   * - ``extensions``
     - REQUIRED. A sequence of one or more certificate extensions.
     - :rfc:`5280#section-4.1.2.9`.

The extensions field of the WRPAC MUST contain various extensions, each of which is an ASN.1 SEQUENCE containing the following fields:

.. list-table:: Extension Profile Parameters
   :class: longtable
   :header-rows: 1
   :widths: 20 55 25

   * - **Parameter**
     - **Description**
     - **Defined in**

   * - ``[extension_name].extnID``
     - REQUIRED. The OID identifying the specific extension type.
     - :rfc:`5280#section-4.1.2.9`.

   * - ``[extension_name].critical``
     - CONDITIONAL. Indicates whether the extension is critical. DEFAULT is ``FALSE``.
     - :rfc:`5280#section-4.1.2.9`.

   * - ``[extension_name].extnValue``
     - REQUIRED. Contains the DER encoding of the ASN.1 value corresponding to the extension type identified by ``extnID``.
     - :rfc:`5280#section-4.1.2.9`.

Below there is a list of the mandatory extensions and their content, if applicable. The column "Criticality" of the certificate extensions takes the semantics defined in [RFC 5280, clause 4.2] and uses the following acronyms:

- C: The extension MUST be considered critical.
- NC: The extension MUST be considered non-critical.

.. list-table:: Certificate Extensions Profile Parameters
   :class: longtable
   :header-rows: 1
   :widths: 20 15 45 20

   * - **Parameter**
     - **Criticality**
     - **Description**
     - **Defined in**

   * - ``authorityKeyIdentifier``
     - NC
     - REQUIRED. Extension with the OID ``2.5.29.35``.
       Contains the ``keyIdentifier`` for the issuing CA's public key.
       The ``authorityCertIssuer`` and ``authorityCertSerialNumber`` fields MAY be present but are not required.
     - clause 4.3.1 of [`ETSI_EN_319_412_2`_].

   * - ``keyUsage``
     - C
     - REQUIRED. Extension with the OID ``2.5.29.15``.
       It MUST be one of the following:
       A. non-repudiation;
       B. non-repudiation and digital signature;
       C. digital signature;
       D. digital signature and (key encipherment or key agreement);
       E. key encipherment or key agreement;
       F. non-repudiation and digital signature and (key encipherment or key agreement).
       Type A, C, or E should be used to avoid mixed usage of keys.
       Certificates issued to natural persons and used to validate commitment to signed content (e.g., documents/agreements) MUST be limited to type A, B, or F (type A should be used).
       Certificates issued to legal persons and used to validate digital signatures over content MUST be limited to type A, B, or F (type A should be used).
     - clause 4.3.2 of [`ETSI_EN_319_412_2`_], clause 4.3.2 of [`ETSIEN319412-3`_].

   * - ``cRLDistributionPoints``
     - NC
     - CONDITIONAL. Extension with the OID ``2.5.29.31``.
       Sequence of ``distributionPoint`` represented by a CHOICE of ``FullName`` or ``nameRelativeToCRLIssuer``, ``reasons``, and ``cRLIssuer``.
       **Applicable condition:** If the certificate does not include any access location of an Online Certificate Status Protocol (OCSP) responder or the validity assured extension.
       It contains at least one reference to a publicly available Certificate Revocation List (CRL).
     - clause 4.3.11 of [`ETSI_EN_319_412_2`_].
   
   * - ``ext-etsi-valassured-ST-certs``
     - NC
     - CONDITIONAL. Extension with the OID ``0.4.0.194121.2.1``.
       **Applicable condition:** For short-term certificates which cannot be revoked.
       Indicates that the certificate issuer ensures the validity of the certificate is assured at time of use of the corresponding private key. Upon presence of such statement, the WRP can decide not to check the certificate revocation status (e.g., when validating a digital signature).
     - clause 6.6.1 of [`ETSIEN319412-1`_].

   * - ``noRevAvail``
     - NC
     - CONDITIONAL. Extension with the OID ``2.5.29.56``.
       Allows a CA to indicate that no revocation information will be made available for this certificate.
       **Applicable condition:** If the certificate includes the validity assured extension, but neither includes a CRL distribution point nor access location of an OCSP responder.
     - :rfc:`9608#section-2`.

   * - ``authorityInfoAccess``
     - NC
     - CONDITIONAL. Extension with the OID ``1.3.6.1.5.5.7.1.1``.
       Sequence of ``AccessDescription``, containing an ``accessMethod`` (OID) and an ``accessLocation``.
       It MUST at least include the ``id-ad-caIssuers`` OID specifying at least one access location of a valid CA certificate of the issuing CA.
       If OCSP is supported, it MUST include the ``id-ad-ocsp`` OID specifying at least one access location of an OCSP responder providing status information for the present certificate.
       If the certificate does not include any CRL distribution point and does not include the validity assured extension, a reference to at least one OCSP responder MUST be present.
     - clause 4.4.1 of [`ETSI_EN_319_412_2`_].

   * - ``subjectKeyIdentifier``
     - NC
     - REQUIRED. Extension with the OID ``2.5.29.14``. Contains a key identifier for the subject's public key.
     - :rfc:`5280#section-4.2.1.2`.

   * - ``certificatePolicies``
     - NC
     - REQUIRED. Extension with the OID ``2.5.29.32``.
       Sequence of ``PolicyInformation`` elements, each being a SEQUENCE of ``policyIdentifier`` (OID) and ``policyQualifiers``.
     - clause 4.3.3 of [`ETSI_EN_319_412_2`_].

   * - ``subjectAltName``
     - NC
     - REQUIRED. Extension with the OID ``2.5.29.17``.
       Sequence of ``GeneralName`` elements, each representing a possible alternative name for the subject of the certificate (e.g., ``dNSName`` for web site certificates, ``directoryName`` for transliterated names).
       **Note:** This extension is for alternative subject names, not WRP contact information.
     - :rfc:`5280#section-4.2.1.6`.

   * - ``subjectInfoAccess``
     - NC
     - REQUIRED. Extension with the OID ``1.3.6.1.5.5.7.1.11``.
       Sequence of ``AccessDescription``, containing an ``accessMethod`` (OID) and ``accessLocation``.
       **Applicable condition:** Must contain WRP contact information as stated in clause 6.6.1 of [`ETSI_TS_119_411_8`_]. There MUST be at least one element among the following methods:
       * ``id-ad-wrp`` (or equivalent) indicating a URI where the WRP can be contacted for helpdesk/support matters.
       * ``id-ad-wrp`` (or equivalent) indicating a telephone number for WRP registration/usage matters.
       * ``id-ad-wrp`` (or equivalent) indicating an email address for WRP registration/usage matters.
     - clause 6.6.1 of [`ETSI_TS_119_411_8`_].

   * - ``qcStatements`` (esi4-qcStatement-1)
     - NC
     - REQUIRED. ``QCStatement`` carried within the ``qcStatements`` extension (OID 1.3.6.1.5.5.7.1.3).
       **Applicable condition:** For qualified certificates.
       Contains a ``statementId`` (OID ``0.4.0.1862.1.1``). The ``statementInfo`` field MUST be absent.
       It indicates that the certificate is qualified within the defined legal framework. For the eIDAS regulatory environment, the ``QcCClegislation`` MUST be absent.
     - :rfc:`3739#appendix-C.1.1.4`, clause 4.2.1 of [`ETSI_EN_319_412_5`_].

   * - ``qcStatements`` (esi4-qcStatement-4)
     - NC
     - REQUIRED. ``QCStatement`` carried within the ``qcStatements`` extension (OID 1.3.6.1.5.5.7.1.3).
       **Applicable condition:** For qualified certificates where the private key resides in a Qualified Signature/Seal Creation Device (QSCD).
       Contains a ``statementId`` (OID ``0.4.0.1862.1.4``). The ``statementInfo`` field MUST be absent.
     - :rfc:`3739#appendix-C.1.1.4`, clause 4.2.2 of [`ETSI_EN_319_412_5`_].

   * - ``qcStatements`` (esi4-qcStatement-6)
     - NC
     - REQUIRED. ``QCStatement`` carried within the ``qcStatements`` extension (OID 1.3.6.1.5.5.7.1.3).
       **Applicable condition:** Mandatory for qualified certificates issued for electronic seals (Annex III) and qualified certificates for website authentication (Annex IV). Optional for qualified certificates for electronic signatures (Annex I).
       Contains a ``statementId`` (OID ``0.4.0.1862.1.6``) and a ``statementInfo`` containing a ``QcType``.
       The ``QcType`` is a ``SEQUENCE SIZE (1) OF OBJECT IDENTIFIER`` containing exactly one of the following purpose OIDs:
       * ``0.4.0.1862.1.6.1`` (``id-etsi-qct-esign``)
       * ``0.4.0.1862.1.6.2`` (``id-etsi-qct-eseal``)
       * ``0.4.0.1862.1.6.3`` (``id-etsi-qct-web``)
       Declares that a certificate is issued for one and only one of the purposes: electronic signature, electronic seal, or web site authentication.
     - :rfc:`3739#appendix-C.1.1.4`, clause 4.2.3 of [`ETSI_EN_319_412_5`_].

Wallet-Relying Party Access Certificate (WRPAC) Profile
"""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. warning::
    TODO:

    2. decidere estensioni supportate per WRPAC (dipende da scelta meccanismi di revoca + certificatePolicies) 

    3. aggiornare conseguentemente l'esempio

    4. WRPAC sono solo di durata lunga?

This section describes the purpose, format and content of Wallet-Relying Party Access Certificates (WRPACs).

According to the Article 2 of CIR (EU) 2025/848 `CIR2025/848`_, a WRPAC, is a certificate for electronic seals or signatures authenticating and validating the WRP when they interact with the EUDI Wallet. For more details on the authentication process, see :ref:`trust-evaluation-eudiw:Authentication Process`.

The suspension or cancellation of the WRP services, involves revocation of all valid WRPAC by the relevant issuing authority, such that the WRP is no longer able to interact with Wallet Units. For more detail on the Trust Management processes, see :ref:`infrastructure-trust:EUDIW Trust Management Process`.

The Annex IV of `CIR2025/848`_ also states that the WRPACs are meant for performing electronic signatures or seals and that they MUST comply with at least the Normalised Certificate Policy (NCP) requirements specified in the ETSI standards. 
Taking into account these minimal requirements, different scenarios are possible and specified in the following clauses: certificates issued to natural or legal persons, supporting advanced signatures/seals or even qualified signature/seals. Conditional requirements are defined according to the specific case the WRPACs fall into.

The technical standard that defines the common requirements with respect to content and format of these certificates is ETSI TS 119 411-8 `ETSI_TS_119_411_8`_.

Clause 4 in ETSI TS 119 412-6, further specifies PID Providers X509 certificates parameters as follows:

- Among core parameters, all are required as described in :ref:`trust-artifact-eudiw:X509 Certificate Profiles`.

- Among Extensions parameters,

  - the ``keyUsage`` extension MUST contain one (and only one) of the key-usage settings Type A, Type B, Type C, or Type F, as defined in ETSI EN 319 412-2.
  - At least one of the following extensions MUST be present:

    * ``cRLDistributionPoints`` extension with at least one reference to a publicly available Certificate Revocation List (CRL) as described in :ref:`infrastructure-trust:Certificate Revocation List (CRL)`.
    * ``authorityInfoAccess`` extension with at least one reference to a publicly available Online Certificate Status Protocol (OCSP) responder providing status information for the present certificate as described in :ref:`infrastructure-trust:Online Certificate Status Protocol (OCSP)`.

  - the ``certificatePolicies`` extension MUST be present with the ``PolicyInformation`` field containing the following values defined by [`ETSI_TS_119_411_8`_]:

    * ``0.4.0.194118.1.1`` (``NCP-n-eudiwrp``)
    * ``0.4.0.194118.1.2`` (``NCP-l-eudiwrp``)
    * ``0.4.0.194118.1.3`` (``QCP-n-eudiwrp``)
    * ``0.4.0.194118.1.4`` (``QCP-l-eudiwrp``)

   The ``cpsURI`` under Certificate policies MUST indicate a URL where the CPS of the Provider of WRPAC is located.

  - ``subjectKeyIdentifier`` For end entity certificates, the subject key identifier extension provides a means of identifying certificates that contain the particular public key used in an application. The subject key identifier SHOULD be derived from the public key using the methods defined in :rfc:`5280`, clause 4.2.1.2.
  - ``authorityInfoAccess`` MUST be present.
  - the (esi4-qcStatement-6) ``qcStatements`` extension with the OID ``1.3.6.1.5.5.7.1.3`` MUST be present with ``QcType`` valued as ``0.4.0.194126.1.1`` (``id-etsi-qct-pid``) as defined in Annex A of [`ETSI_TS_119_412_6`_].

The extension is mandatory as stated in [`ETSI_TS_119_411_8`_], requirement GEN-6.6.1-03. 
     - :rfc:`3647#section-3.3.1`, :rfc:`5280#section-4.2.1.4`.

.. note::
    **Dependency Considerations**: The WRPAC attributes MUST be derived from the information held in the Register as specified in clause 5.1.2 of `ETSI_TS_119_475`_ `ETSI_TS_119_475`_. This also implies that for some specific attributes in the WRPAC the same value MUST be encountered in the corresponding WRPRC if any.

Wallet-Relying Party Access Certificate compliant with this 

The following is an example of a WRPAC for legal persons following the NCP.

.. literalinclude:: ../../examples/wrpac-ncp.txt
  :language: text

Entity Sign/Seal Certificate Profile
""""""""""""""""""""""""""""""""""""""

This section specifies :ref:`trust-artifact-eudiw:X509 Certificate Profiles` by describing the purpose, format and content of Entity Sign/Seal Certificate which are used for signing and sealing various Attestations. These profiles are specified in `ETSI_TS_119_412_6`.

PID Provider Sign/Seal Certificate
.....................................

Clause 4 in ETSI TS 119 412-6, further specifies PID Providers X509 certificates parameters as follows:

- Among core parameters, all are required as described in :ref:`trust-artifact-eudiw:X509 Certificate Profiles`.

- Among Extensions parameters,

  - the ``keyUsage`` extension MUST contain one (and only one) of the key-usage settings Type A, Type B, Type C, or Type F, as defined in ETSI EN 319 412-2.
  - At least one of the following extensions MUST be present:

    * ``cRLDistributionPoints`` extension with at least one reference to a publicly available Certificate Revocation List (CRL) as described in :ref:`infrastructure-trust:Certificate Revocation List (CRL)`.
    * ``authorityInfoAccess`` extension with at least one reference to a publicly available Online Certificate Status Protocol (OCSP) responder providing status information for the present certificate as described in :ref:`infrastructure-trust:Online Certificate Status Protocol (OCSP)`.

  - the ``certificatePolicies`` extension MUST be present with the ``policyInformation`` field containing the *NCP+* ``policyIdentifier`` (OID ``0.4.0.2042.1.2``).
  - ``subjectKeyIdentifier`` For end entity certificates, the subject key identifier extension provides a means of identifying certificates that contain the particular public key used in an application. The subject key identifier SHOULD be derived from the public key using the methods defined in :rfc:`5280`, clause 4.2.1.2.
  - ``authorityInfoAccess`` MUST be present.
  - the (esi4-qcStatement-6) ``qcStatements`` extension with the OID ``1.3.6.1.5.5.7.1.3`` MUST be present with ``QcType`` valued as ``0.4.0.194126.1.1`` (``id-etsi-qct-pid``) as defined in Annex A of [`ETSI_TS_119_412_6`_].

.. warning::
  the oid ``1.3.6.1.5.5.7.1.3`` might not be the right one for esti uses ``1.3.6.1.5.5.7.0.35``. the latter is however a module oid and not an extension oid. Need to clarify with ETSI.

The following is a non-normative example of a PID Provider's end-entity certificate for legal persons (non-self-signed).

.. literalinclude:: ../../examples/pid-sign-seal.txt
  :language: text

Wallet Provider Sign/Seal Certificate
.....................................

Clause 5 in ETSI TS 119 412-6, further specifies Wallet Providers X509 certificates parameters as follows:

- Among core parameters, all are required as described in :ref:`trust-artifact-eudiw:X509 Certificate Profiles`.

- Among Extensions parameters,

  - the ``keyUsage`` extension MUST contain one (and only one) of the key-usage settings Type A, Type B, Type C, or Type F, as defined in ETSI EN 319 412-2.
  - At least one of the following extensions MUST be present:

    * ``cRLDistributionPoints`` extension with at least one reference to a publicly available Certificate Revocation List (CRL) as described in :ref:`infrastructure-trust:Certificate Revocation List (CRL)`.
    * ``authorityInfoAccess`` extension with at least one reference to a publicly available Online Certificate Status Protocol (OCSP) responder providing status information for the present certificate as described in :ref:`infrastructure-trust:Online Certificate Status Protocol (OCSP)`.

  - ``subjectKeyIdentifier`` For end entity certificates, the subject key identifier extension provides a means of identifying certificates that contain the particular public key used in an application. The subject key identifier SHOULD be derived from the public key using the methods defined in :rfc:`5280`, clause 4.2.1.2.
  - ``authorityInfoAccess`` MUST be present.
  - the (esi4-qcStatement-6) ``qcStatements`` extension with the OID ``1.3.6.1.5.5.7.1.3`` MUST be present with ``QcType`` valued as ``0.4.0.194126.1.2`` (``id-etsi-qct-wal``) as defined in Annex A of [`ETSI_TS_119_412_6`_].

The following is a non-normative example of a Wallet Provider's end-entity certificate for legal persons (non-self-signed).

.. literalinclude:: ../../examples/wp-sign-seal.txt
  :language: text

(Q)EAA Provider Sign/Seal Certificate
.....................................

Clause 6 and 7 in ETSI TS 119 412-6, further specifies (Q)EAA Providers X509 certificates parameters as follows: 

- for EAA Providers Sign/Seal Certificates, all core and extension parameters are required as described in :ref:`trust-artifact-eudiw:X509 Certificate Profiles`.

- for QEAA Providers Sign/Seal Certificates, 

  - all core parameters are required as described in :ref:`trust-artifact-eudiw:X509 Certificate Profiles`

  - Among Extensions parameters,

    - ``authorityInfoAccess`` MUST be present.

For both QEAA and EAA Providers, if they manage the lifecycle of the Digital Credentials they issue and they use signed revocation lists such as Token Status List, they MUST use the same Sign/Seal Certificate to sign/seal the revocation list. 

The following is a non-normative example of a QEAA Provider's end-entity certificate for legal persons (non-self-signed).

.. literalinclude:: ../../examples/qeaa-sign-seal.txt
  :language: text

PuB-EAA Provider Sign/Seal Certificate
......................................

Clause 8 in ETSI TS 119 412-6, further specifies PuB-EAA Providers X509 certificates parameters as follows:

- Among core parameters, all are required as described in :ref:`trust-artifact-eudiw:X509 Certificate Profiles`.

- Among Extensions parameters,

  - ``authorityInfoAccess`` extension with at least one reference to a publicly available Online Certificate Status Protocol (OCSP) responder providing status information for the present certificate as described in :ref:`infrastructure-trust:Online Certificate Status Protocol (OCSP)`.
  - the ``certificatePolicies`` extension MUST be present with the ``policyInformation`` field containing the *NCP+* ``policyIdentifier`` (OID ``0.4.0.2042.1.2``).
  - the ``qcStatements`` extension indicated in the table below MUST be present.

.. list-table:: Additional PuB-EAA Extensions Profile Parameters
   :class: longtable
   :header-rows: 1
   :widths: 20 15 45 20

   * - **Parameter**
     - **Criticality**
     - **Description**
     - **Defined in**

   * - ``qcStatements`` (esi4-qcStatement-10)
     - NC
     - REQUIRED. Extension with the OID ``1.3.6.1.5.5.7.1.3``.

        Sequence of ``QCStatement``, containing a ``statementId`` (OID ``0.4.0.194126.1.3``) and a ``statementInfo`` containing a ``QcPSB`` element.

        The ``QcPSB`` element is a ``SEQUENCE`` containing the following parameters:

       * ``countryOfLegislation``: A ``PrintableString (SIZE (2))`` containing the alpha-2 country code of the legislation framework of the public sector body. In the case of European Union law, ``EU`` MUST be used in place of the country code.
       * ``authSourceIdentification``: A ``UTF8String`` containing the unique identification of the authentic source.
       * ``legislationIdentification``: A ``UTF8String`` containing the identification of the legislation framework.

        **Applicable condition:** Mandatory data requirement for Public Sector Body (PSB) certificates to declare legal frameworks and identity source mappings.
     - :rfc:`3739#appendix-C.1.1.4`, Annex A of [`ETSI_TS_119_412_6`_].

The following is a non-normative example of a PuB-EAA Provider's end-entity certificate for legal persons (non-self-signed).

.. literalinclude:: ../../examples/pubeaa-sign-seal.txt
  :language: text

Registrar Sign/Seal Certificate
................................

CIR 2025/848, further specifies the Registrar Sign/Seal Certificate parameters as follows:

- Among core parameters, all are required as described in :ref:`trust-artifact-eudiw:X509 Certificate Profiles`.

- Among Extensions parameters,

  - At least one of the following extensions MUST be present:

    * ``cRLDistributionPoints`` extension with at least one reference to a publicly available Certificate Revocation List (CRL) as described in :ref:`infrastructure-trust:Certificate Revocation List (CRL)`.
    * ``authorityInfoAccess`` extension with at least one reference to a publicly available Online Certificate Status Protocol (OCSP) responder providing status information for the present certificate as described in :ref:`infrastructure-trust:Online Certificate Status Protocol (OCSP)`.
    
  - the ``certificatePolicies`` extension MUST be present with the ``policyInformation`` field containing the *NCP* ``policyIdentifier`` (OID ``0.4.0.2042.1.1``).

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

Trust Anchor Certificate Profile
""""""""""""""""""""""""""""""""

.. warning:: 
  aggiungere schema dei trust anchors

  non hanno delle certificate policies? tipo NCP o simili? sembra logico di si' a maggior ragione se sono emessi da un CA che emette anche WRPAC o Entity Sign/Seal Certificates che hanno questi requisiti.

This section specifies an **X.509 certificate profile** for **Trust Anchors** used in the European Digital Identity Wallet (EUDIW) ecosystem. These certificates MUST be notified to the European Commission as described in `CIR2025/2980`_ and subsequently included in the appropriate LoTE.

A Trust Anchor is a trusted public key (and associated data) used as an input to the :ref:`trust-evaluation-eudiw:X509 Certificate Chain Validation Algorithm`. In this profile, the Trust Anchor MUST be represented and distributed as an **X.509 certificate**. When published through List of Trusted Entities, that certificate is referenced from the corresponding service entry through the ``serviceDigitalIdentity`` component.

.. note::

  A Trust Anchor certificate may be *self-signed* or *non-self-signed*. In both cases it is treated as a Trust Anchor when found in a LoTE as required by the EUDIW Trust Framework.

Relying Parties, Credential Issuers and Wallet Units validate a presented Access, Registration of Sign/Seal Certificate by building a certification path that MUST end with a certificate signed by the subject of a Trust Anchor certificate. The Trust Anchor certificate is used as the trust termination point for the path validation process (i.e., it is the value of the ``trust_anchor`` variable in :ref:`trust-evaluation-eudiw:X509 Certificate Chain Validation Algorithm`). Implementations MUST support validating both self-signed and non-self-signed Trust Anchor certificates.

This section further specifies the requirements of :ref:`trust-artifact-eudiw:X509 Certificate Profiles` parameters for Trust Anchor certificates, as follows:

.. list-table:: Certificate Extensions Profile for Trust Anchor Parameters
   :class: longtable
   :header-rows: 1
   :widths: 20 15 45 20

   * - **Parameter**
     - **Criticality**
     - **Description**
     - **Defined in**
   * - ``subject``
     - —
     - REQUIRED. The Trust Anchor certificate MUST contain a non-empty subject distinguished name.
       The subject DN MUST identify the entity associated with the trust anchor public key in a clear and unambiguous manner.
       If the Trust Anchor represents a legal or organizational entity, the subject DN MUST contain an ``organizationName`` attribute identifying that entity.
     - :rfc:`5280#section-4.1.2.6`.
   * - ``issuer``
     - —
     - REQUIRED. The Trust Anchor certificate MUST contain an issuer distinguished name.
       If the certificate is self-signed, the issuer DN MUST be identical to the subject DN.
       If the certificate is non-self-signed, the issuer DN MUST identify the entity that signed and issued the certificate and MAY differ from the subject DN.
     - :rfc:`5280#section-4.1.2.4`.
   * - ``subjectKeyIdentifier``
     - NC
     - REQUIRED. Extension with the OID ``2.5.29.14``.
       Identifies the trust anchor public key.
       The value SHOULD be derived from the public key in a stable and interoperable manner (e.g., via SHA-256) to support reliable certificate path construction and certificate matching in LoTE / Trusted List based deployments.
     - :rfc:`5280#section-4.2.1.2`.
   * - ``basicConstraints``
     - C
     - REQUIRED. Extension with the OID ``2.5.29.19``.
       The ``cA`` field MUST be set to TRUE, signalling CA capability for X.509 path validation.
       The ``pathLenConstraint`` field MAY be present.
       If present, ``pathLenConstraint`` MUST limit the number of non-self-issued intermediate CA certificates below the Trust Anchor.
       Setting ``pathLenConstraint`` to 0 is RECOMMENDED unless a documented operational need exists to support additional subordinate CA tiers.
       This extension MUST be critical.
     - :rfc:`5280#section-4.2.1.9`.
   * - ``keyUsage``
     - C
     - REQUIRED. Extension with the OID ``2.5.29.15``.
       The extension MUST include the ``keyCertSign`` bit.
       The extension MAY include the ``cRLSign`` bit if the Trust Anchor certificate is used by the CA to sign certificate revocation lists.
       The extension SHOULD be limited to usages consistent with the certification authority role of the Trust Anchor certificate.
       This extension MUST be critical.
     - :rfc:`5280#section-4.2.1.3`.
   * - ``ext-etsi-valassured-ST-certs``
     - NC
     - OPTIONAL. Extension with the OID ``0.4.0.194121.2.1``.
       Indicates that the certificate issuer ensures the validity of the certificate is assured at time of use of the corresponding private key.
     - clause 6.6.1 of [`ETSIEN319412-1`_].

.. note::
   **Trust Anchor revocation.**
    Trust Anchor certificates are not expected to be revoked as they are trusted by policy when published in a LoTE or Trusted List. As a result, revocation information (e.g., CRL or OCSP) is not required for Trust Anchor certificates and entities using Trust Anchor certificates retrived in a LoTE or Trusted List MAY avoid revocation checking for Trust Anchor certificates.

.. note::

   **Self-signed vs. non-self-signed trust anchors.**
   A LoTE / Trusted List-published trust anchor certificate MAY be self-signed (traditional root CA style) or non-self-signed but treated as a trust anchor by policy (a pinned intermediate CA certificate).
   Relying parties MUST NOT require an additional issuer chain above a LoTE-designated trust anchor, even if it is not self-signed, because the trust anchor is a trust-store input designated by policy.

The following table maps the various Certificates used in the ecosystem, the attested public key uses, and the location of the Trust Anchor.

.. list-table:: Certificate and Trust Anchor Matrix
   :header-rows: 1

   * - **Certificate**
     - **Attested Key Use**
     - **Trust Anchor location**
   * - PID Provider Sign/Seal Certificate
     - signing PID, siging PID Status List Token
     - PID Providers LoTE
   * - Wallet Provider Sign/Seal Certificate
     - signing WIA, KA, signing WIA/KA Status List Token 
     - Wallet Providers LoTE
   * - EAA Provider Sign/Seal Certificate
     - signing EAA, signing EAA Status List Token
     - ``trustedAuthority`` attribute in the machine-readable Attestation Rulebook for the specific EAA
   * - QEAA Provider Sign/Seal Certificate
     - signing QEAA, signing QEAA Status List Token
     - eIDAS I Trusted List
   * - Pub-EAA Provider Sign/Seal Certificate
     - signing PuB-EAA, signing PuB-EAA Status List Token
     - Pub-EAA Providers LoTE
   * - Wallet-Relying Party WRPAC
     - signing Request Objects or ``readerAuth`` during Digital Credential Presentation for Relying Parties; signing Credential Issuer Metadata for Credential Issuers
     - Provider of WRPAC LoTE
   * - Wallet-Relying Party WRPRC
     - N/A
     - Provider of WRPRC LoTE

.. note::

  As described in `Section 4.3.1 of ARF TS11 <https://github.com/eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications/blob/main/docs/technical-specifications/ts11-interfaces-and-formats-for-catalogue-of-attributes-and-catalogue-of-schemes.md#431-schemameta-main-class>`_ the Trust Anchor of a EAA Sign/Seal Certificate is rferenced in the ``trustedAuthority`` attribute of the machine-readable Attestation Rulebook for the specific EAA.

The following is a non-normative example of a trust anchor certificate in a pseudo-structure format.

.. literalinclude:: ../../examples/trust-anchor-cert.txt
  :language: text

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

.. warning::

  can we make this normative? "They are not applicable to PIDs as the EUDI Wallet Regulation does not provide any requirement for PID to contain an EDP."

The EDP is distributed through the Credential Issuer Metadata at issuance time. The Attestation Provider MUST include the EDP (if any) by value in the Credential Issuer Metadata, within the ``credential_configurations_supported`` parameter, in compliance with `OpenID4VCI`_ or the extension thereof specified in `ETSI TS 119 472-3`. If availble, the Wallet Unit MUST store the EDP locally and associate it with the specific Attestation for which it was retrieved. The Wallet Unit MUST NOT reveal the EDP to the Relying Party through the presentation protocol as per `ETSI TS 119 472-3`_, Section 4.2.5.1.

!!! warning

    According to ISS-MDATA-EBD-4.2.5.2-03, the Attestation Provider may provide only the `policy_uri` if the policy data set has already been pre-loaded into the Wallet Unit. As the mechanism for pre-loading policies into a Wallet Unit is not specified in the current normative references, this option MUST be considered out-of-scope of this specification, at least until further implementation details are provided by ETSI.?????

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



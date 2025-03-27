
.. include:: ../common/common_definitions.rst

.. _pid_eaa_data_model.rst:

PID/(Q)EAA Data Model
+++++++++++++++++++++

The Digital Credential Data Model structures Digital Credentials for secure, interoperable use. Key elements include:

    - Credential Subject: The individual or entity receiving the Credential.
    - Issuer: The PID/(Q)EAA Provider issuing and signing the Credential.
    - Metadata: Details about the Credential, like type and validity.
    - Claims: Information about the subject, such as identity or qualifications.
    - Proof: Cryptographic verification of authenticity and legitimate ownership.

The Person Identification Data (PID) is issued by the PID Provider according to national laws. The main scope of the PID is allowing natural persons to be authenticated for the access to a service or to a protected resource. 
The User attributes provided within the Italian PID are the ones listed below:

    - Current Family Name
    - Current First Name
    - Date of Birth
    - Taxpayer identification number

The (Q)EAAs are issued by (Q)EAA Issuers to a Wallet Instance and MUST be provided in SD-JWT-VC or mDOC-CBOR data format. 

The PID/(Q)EAA data format and the mechanism through which a digital credential is issued to the Wallet Instance and presented to a Relying Party are described in the following sections. 

SD-JWT-VC Credential Format
===========================

The PID/(Q)EAA is issued in the form of a Digital Credential. The Digital Credential format is `SD-JWT`_ as specified in `SD-JWT-VC`_.

SD-JWT MUST be signed using the Issuer's private key. SD-JWT MUST be provided along with a Type Metadata related to the issued Digital Credential according to Sections 6 and 6.3 of [`SD-JWT-VC`_]. The payload MUST contain the **_sd_alg** claim described in the Section 4.1.1 `SD-JWT`_ and other claims specified in this section. 

The claim **_sd_alg** indicates the hash algorithm used by the Issuer to generate the digests as described in Section 4.1.1 of `SD-JWT`_. **_sd_alg**  MUST be set to one of the specified algorithms in Section :ref:`Cryptographic Algorithms <supported_algs>`.

Claims that are not selectively disclosable MUST be included in the SD-JWT as they are.  The digests of the disclosures, along with any decoy if present,  MUST be contained in the  **_sd** array, as specified in Section 4.2.4.1 of `SD-JWT`_. 

Each digest value, calculated using a hash function over the disclosures, verifies the integrity and corresponds to a specific Disclosure. Each disclosure includes:

  - a random salt, 
  - the claim name (only when the claim is an object element), 
  - the claim value. 

In case of nested object in a SD-JWT payload each claim, on each level of the JSON, should be individually selectively disclosable or not. Therefore **_sd** claim containing digests MAY appear multiple times at different level in the SD-JWT.

For each claim that is an array element the digests of the respective disclosures and decoy digests are added to the array in the same position of the original claim values as specified in Section 4.2.4.2 of `SD-JWT`_.

In case of array elements, digest values are calculated using a hash function over the disclosures, containing:

  - a random salt, 
  - the array element

In case of multiple array elements, the Issuer may hide the value of the entire array or any of the entry contained within the array, the Holder can disclose both the entire array and any single entry within the array, as defined in Section 4.2.6 of `SD-JWT`_.

The Disclosures are provided to the Holder together with the SD-JWT in the *Combined Format for Issuance* that is an ordered series of base64url-encoded values, each separated from the next by a single tilde ('~') character as follows:

.. code-block::

  <Issuer-Signed-JWT>~<Disclosure 1>~<Disclosure 2>~...~<Disclosure N>

See `SD-JWT-VC`_ and `SD-JWT`_ for additional details. 


PID/(Q)EAA SD-JWT Parameters
----------------------------

The JOSE header contains the following mandatory parameters:

.. _pid_jose_header:

.. list-table:: 
  :widths: 20 60 20
  :header-rows: 1

  * - **Claim**
    - **Description**
    - **Reference**
  * - **typ**
    - REQUIRED. It MUST be set to ``dc+sd-jwt`` as defined in `SD-JWT-VC`_. 
    - :rfc:`7515` Section 4.1.9.
  * - **alg**
    - REQUIRED. Signature Algorithm. 
    - :rfc:`7515` Section 4.1.1.
  * - **kid**
    - REQUIRED. Unique identifier of the public key. 
    - :rfc:`7515` Section 4.1.8.
  * - **trust_chain**
    - OPTIONAL. JSON array containing the trust chain that proves the reliability of the issuer of the JWT. 
    - [`OID-FED`_] Section 4.3.
  * - **x5c**
    - OPTIONAL. Contains the X.509 public key certificate or certificate chain [:rfc:`5280`] corresponding to the key used to digitally sign the JWT. 
    - :rfc:`7515` Section 4.1.8 and [`SD-JWT-VC`_] Section 3.5.
  * - **vctm**
    - OPTIONAL. JSON array of base64url-encoded Type Metadata JSON documents. In case of extended type metadata, this claim contains the entire chain of JSON documents. 
    - [`SD-JWT-VC`_] Section 6.3.5.

The JWT payload contains the following claims. Some of these claims can be disclosed, these are listed in the following tables that specify whether a claim is selectively disclosable [SD] or not [NSD].

.. list-table:: 
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Description**
      - **Reference**
    * - **iss**
      - [NSD]. REQUIRED. URL string representing the PID/(Q)EAA Issuer unique identifier.
      - `[RFC7519, Section 4.1.1] <https://www.iana.org/go/rfc7519>`_.
    * - **sub**
      - [NSD]. REQUIRED. The identifier of the subject of the Digital Credential, the User, MUST be opaque and MUST NOT correspond to any anagraphic data or be derived from the User's anagraphic data via pseudonymization. Additionally, it is required that two different Credentials issued MUST NOT use the same ``sub`` value.
      - `[RFC7519, Section 4.1.2] <https://www.iana.org/go/rfc7519>`_.
    * - **iat**
      - [SD]. REQUIRED. UNIX Timestamp with the time of JWT issuance, coded as NumericDate as indicated in :rfc:`7519`.
      - `[RFC7519, Section 4.1.6] <https://www.iana.org/go/rfc7519>`_.
    * - **exp**
      - [NSD]. REQUIRED. UNIX Timestamp with the expiry time of the JWT, coded as NumericDate as indicated in :rfc:`7519`.
      - `[RFC7519, Section 4.1.4] <https://www.iana.org/go/rfc7519>`_.
    * - **nbf**
      - [NSD]. OPTIONAL. UNIX Timestamp with the start time of validity of the JWT, coded as NumericDate as indicated in :rfc:`7519`.
      - `[RFC7519, Section 4.1.4] <https://www.iana.org/go/rfc7519>`_.    
    * - **issuing_authority**
      - [NSD]. REQUIRED. Name of the administrative authority that has issued the PID/(Q)EAA.
      - Commission Implementing Regulation `EU_2024/2977`_.
    * - **issuing_country**
      - [NSD]. REQUIRED. Alpha-2 country code, as specified in ISO 3166-1, of the country or territory of the PID/(Q)EAA Issuer.
      - Commission Implementing Regulation `EU_2024/2977`_.
    * - **status**
      - [NSD]. REQUIRED only if the Digital Credential is long-lived. JSON object containing the information on how to read the status of the Verifiable Credential. It MUST contain either the JSON member *status_assertion* or *status_list*. 
      - Section 3.2.2.2 `SD-JWT-VC`_ and Section 11 `OAUTH-STATUS-ASSERTION`_.
    * - **cnf**
      - [NSD]. REQUIRED. JSON object containing the proof-of-possession key materials. By including a **cnf** (confirmation) claim in a JWT, the Issuer of the JWT declares that the Holder is in control of the private key related to the public one defined in the **cnf** parameter. The recipient MUST cryptographically verify that the Holder is in control of that key.
      - `[RFC7800, Section 3.1] <https://www.iana.org/go/rfc7800>`_ and Section 3.2.2.2 `SD-JWT-VC`_.
    * - **vct**
      - [NSD]. REQUIRED. Credential type value MUST be an HTTPS URL String and it MUST be set using one of the values obtained from the PID/(Q)EAA Issuer metadata. It is the identifier of the SD-JWT VC type and it MUST be set with a collision-resistant value as defined in Section 2 of :rfc:`7515`. It MUST contain also the number of version of the Credential type (for instance: ``https://issuer.example.org/v1.0/personidentificationdata``).
      - Section 3.2.2.2 `SD-JWT-VC`_.
    * - **vct#integrity**
      - [NSD]. REQUIRED. The value MUST be an "integrity metadata" string as defined in Section 3 of [`W3C-SRI`_]. *SHA-256*, *SHA-384* and *SHA-512* MUST be supported as cryptographic hash functions. *MD5* and *SHA-1* MUST NOT be used. This claim MUST be verified according to Section 3.3.5 of [`W3C-SRI`_].
      - Section 6.1 `SD-JWT-VC`_, [`W3C-SRI`_]
    * - **verification**
      - [SD]. CONDITIONAL. REQUIRED if Credential type is set to `PersonIdentificationData`, otherwise is OPTIONAL. Object containing User authentication and User data verification information. If present MUST include the following sub-value:

          * ``trust_framework``: String identifying the trust framework used for User authentication. It MUST be set using one of the values described in the `trust_frameworks_supported` map provided within the Credential Issuer Metadata.
          * ``assurance_level``: String identifying the level of identity assurance guaranteed during the User authentication process.
          * ``evidence``: Each entry of the array MUST contain the following members:
              - ``type``: It represents evidence type. It MUST be set to ``vouch``.
              - ``time``: UNIX Timestamps with the time of the authentication or verification.
              - ``attestation``: It MUST contain the following members:
                  - ``type``: It MUST be set to ``digital_attestation``.
                  - ``reference_number``: identifier of the authentication or verification response.
                  - ``date_of_issuance``: date of issuance of the attestation.
                  - ``voucher``: It MUST contains ``organization`` claim.
      - `OIDC-IDA`_.
    * - **_sd**
      - [NSD]. REQUIRED. Array of strings, where each string represents a digest of a Disclosure.
      - 4.2.4.1 `SD-JWT`_
    * - **_sd_alg**
      - [NSD]. REQUIRED. Hash algorithm used by the Issuer to generate the digests.
      - 4.1.1 `SD-JWT`_

If the ``status`` parameter is set to ``status_list``, it is a JSON Object containing the following sub-parameters:

 .. list-table:: 
   :widths: 20 60 20
   :header-rows: 1
 
   * - **Parameter**
     - **Description**
     - **Reference**
   * - **idx**
     - REQUIRED. The idx (index) claim MUST specify an Integer that represents the index to check for status information in the Status List for the current Digital Credential. The value of idx MUST be a non-negative number, containing a value of zero or greater.
     - TOKEN-STATUS-LIST_
   * -  **uri** 
     - REQUIRED. The uri (URI) claim MUST specify a String value that identifies the Status List Token containing the status information for the Digital Credential. The value of uri MUST be a URI conforming to [:rfc:3986].
     - TOKEN-STATUS-LIST_


If the ``status`` parameter is set to ``status_assertation``, it is a JSON Object containing the *credential_hash_alg* claim indicating the Algorithm used for hashing the Digital Credential to which the Status Assertion is bound. It is RECOMMENDED to use *sha-256*. 


.. note::

    Credential Type Metadata JSON Document MAY be retrieved directly from the URL contained in the claim **vct**, using the HTTP GET method or using the vctm header parameter if provided. Unlike specified in Section 6.3.1 of `SD-JWT-VC`_ the **.well-known** endpoint is not included in the current implementation profile. Implementers may decide to use it for interoperability with other systems.
    

Digital Credential Metadata Type
--------------------------------

The Metadata type document MUST be a JSON object and contains the following parameters.

.. list-table:: 
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Description**
      - **Reference**
    * - **name**
      - REQUIRED. Human-readable name of the Digital Credential type. In case of multiple languages, the language tags are added to the member name, delimited by a # character as defined in :rfc:`5646` (e.g. *name#it-IT*).
      - [`SD-JWT-VC`_] Section 6.2 and [`OIDC`_] Section 5.2.
    * - **description**
      - REQUIRED. A human-readable description of the Digital Credential type. In case of multiple languages, the language tags are added to the member name, delimited by a # character as defined in :rfc:`5646`.
      - [`SD-JWT-VC`_] Section 6.2 and [`OIDC`_] Section 5.2.
    * - **extends**
      - OPTIONAL. String Identifier of an extended metadata type document.
      - [`SD-JWT-VC`_] Section 6.2.
    * - **extends#integrity**
      - CONDITIONAL. REQUIRED if **extends** is present.
      - [`SD-JWT-VC`_] Section 6.2.
    * - **schema**
      - CONDITIONAL. REQUIRED if **schema_uri** is not present.
      - [`SD-JWT-VC`_] Section 6.2.
    * - **schema_uri**
      - CONDITIONAL. REQUIRED if **schema** is not present.
      - [`SD-JWT-VC`_] Section 6.2.
    * - **schema_uri#integrity**
      - CONDITIONAL. REQUIRED if **schema_uri** is present.
      - [`SD-JWT-VC`_] Section 6.2.
    * - **data_source**
      - REQUIRED. Object containing information about the data origin. It MUST contain the object ``verification`` with the following sub-value:

          * ``trust_framework``: MUST contain trust framework used for digital authentication towards Authentic Source system.
          * ``authentic_source``: MUST contain the following claims related to information about the Authentic Source:
               * ``organization_name`` name of the Authentic Source.
               * ``organization_code`` code identifier of the Authentic Source.
               * ``homepage_uri`` uri pointing to the Authentic Source's homepage.
               * ``contacts`` contact list for info and assistance.
               * ``logo_uri`` URI pointing to the logo image.
      - This specification
    * - **display**
      - REQUIRED. Array of objects, one for each language supported, containing display information for the Digital Credential type. It contains for each object the following properties:

          * ``lang``: language tag as defined in :rfc:`5646` Section 2. [REQUIRED].
          * ``name``: human-readable label for the Digital Credential type. [REQUIRED].
          * ``description``: human-readable description for the Digital Credential type. [REQUIRED].
          * ``rendering``: object containing rendering methods supported by the Digital Credential type. [REQUIRED]. The rendering method `svg_template` MUST be supported.
              The ``svg_templates`` array of objects contains for each SVG template supported the following properties:
                  * ``uri``: URI pointing to the SVG template. [REQUIRED].
                  * ``uri#integrity``: integrity metadata as defined in Section 3 of `W3C-SRI`_. [REQUIRED].
                  * ``properties``: object containing SVG template properties. This property is REQUIRED if more than one SVG template is present. The object MUST contain at least one of the properties defined in `SD-JWT-VC`_ Section 8.1.2.1.
                             
              If rendering method `simple` is also supported, the ``simple`` object contains the following properties: 
                  * ``logo``: object containing information about the logo to display. This property is REQUIRED. The object contains the following sub-values:
                      * ``uri``: URI pointing to the logo image. [REQUIRED]
                      * ``uri#integrity``: integrity metadata as defined in Section 3 of `W3C-SRI`_. [REQUIRED].
                      * ``alt_text``: A string containing alternative text to display instead of the logo image. [OPTIONAL].
                  * ``background_color``: RGB color value as defined in `W3C.CSS-COLOR`_ for the background of the Digital Credential. [OPTIONAL].
                  * ``text_color``: RGB color value as defined in `W3C.CSS-COLOR`_ for the text of the Digital Credential. [OPTIONAL].

          .. note::

            The use of the SVG template is recommended for all applications that support it.

      - [`SD-JWT-VC`_] Section 8.
    * - **claims**
      - REQUIRED. Array of objects containing information for displaying and validating Digital Credential claims. It contains for each Credential claim the following properties:

          * ``path``: array indicating the claim or claims that are being addressed. [REQUIRED].
          * ``display``: array containing display information about the claim indicated in the ``path``. The array contains an object for each language supported by the Digital Credential type. This property is REQUIRED. It contains the following members:
             * ``lang``: language tag as defined in :rfc:`5646` Section 2. [REQUIRED].
             * ``label``: human-readable label for the claim. [REQUIRED].
             * ``description``: human-readable description for the claim. [REQUIRED].
          * ``sd``: string indicating whether the claim is selectively disclosable. It MUST be set to `always` if the claim is selectively disclosure or `never` if not. [REQUIRED].
          * ``svg_id``: alphanumeric string containing ID of the claim referenced in the SVG template as defined in [`SD-JWT-VC`_] Section 9. [REQUIRED].
      - [`SD-JWT-VC`_] Section 9.


A non-normative Digital Credential metadata type is provided below.

.. literalinclude:: ../../examples/vc-metadata-type.json
  :language: JSON  

.. _sec-pid-user-claims:   

PID Claims
----------

Depending on the Digital Credential type **vct**, additional claims data MAY be added. The PID supports the following data:

.. list-table:: 
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Description**
      - **Reference**
    * - **given_name**
      - [SD]. REQUIRED. Current First Name.
      - Section 5.1 of `OIDC`_ and Commission Implementing Regulation `EU_2024/2977`_
    * - **family_name**
      - [SD]. REQUIRED. Current Family Name.
      - Section 5.1 of `OIDC`_ and Commission Implementing Regulation `EU_2024/2977`_
    * - **birth_date**
      - [SD]. REQUIRED. Date of Birth.
      - Commission Implementing Regulation `EU_2024/2977`_
    * - **birth_place**
      - [SD]. REQUIRED. Place of Birth.
      - Commission Implementing Regulation `EU_2024/2977`_
    * - **nationality**
      - [SD]. REQUIRED. One or more alpha-2 country codes as specified in ISO 3166-1.
      - Commission Implementing Regulation `EU_2024/2977`_
    * - **personal_administrative_number**
      - [SD]. CONDITIONAL. REQUIRED if ``tax_id_code`` is not present. National unique identifier of a natural person generated by ANPR in string format.
      - Commission Implementing Regulation `EU_2024/2977`_
    * - **tax_id_code**
      - [SD]. CONDITIONAL. REQUIRED if ``personal_administrative_number`` is not present. National tax identification code of natural person as a String format. It MUST be set according to ETSI EN 319 412-1. For example ``TINIT-<ItalianTaxIdentificationNumber>``
      - 

The PID attribute schema, which encompasses all potential User data, is defined in `ARF`_, and furthermore detailed in the `PID Rulebook`_.


PID Non-Normative Examples
--------------------------

In the following, the non-normative example of the payload of a PID represented in JSON format.

.. literalinclude:: ../../examples/pid-json-example-payload.json
  :language: JSON  

The corresponding SD-JWT version for PID is given by

.. literalinclude:: ../../examples/pid-sd-jwt-example-header.json
  :language: JSON    

.. literalinclude:: ../../examples/pid-sd-jwt-example-payload.json
  :language: JSON  

The disclosure list is presented below.

**Claim** ``iat``:

-  SHA-256 Hash: ``Yrc-s-WSr4exEYtqDEsmRl7spoVfmBxixP12e4syqNE``
-  Disclosure:
   ``WyIyR0xDNDJzS1F2ZUNmR2ZyeU5STjl3IiwgImlhdCIsIDE2ODMwMDAwMDBd``
-  Contents: ``["2GLC42sKQveCfGfryNRN9w", "iat", 1683000000]``

**Claim** ``verification``:

-  SHA-256 Hash: ``h7Egl5H9gTPC_FCU845aadvsC--dTjy9Nrstxh-caRo``
-  Disclosure:
   ``WyJlbHVWNU9nM2dTTklJOEVZbnN4QV9BIiwgInZlcmlmaWNhdGlvbiIsIHsi``
   ``dHJ1c3RfZnJhbWV3b3JrIjogIml0X2NpZSIsICJhc3N1cmFuY2VfbGV2ZWwi``
   ``OiAiaGlnaCIsICJldmlkZW5jZSI6IHsidHlwZSI6ICJ2b3VjaCIsICJ0aW1l``
   ``IjogIjIwMjAtMDMtMTlUMTI6NDJaIiwgImF0dGVzdGF0aW9uIjogeyJ0eXBl``
   ``IjogImRpZ2l0YWxfYXR0ZXN0YXRpb24iLCAicmVmZXJlbmNlX251bWJlciI6``
   ``ICI2NDg1LTE2MTktMzk3Ni02NjcxIiwgImRhdGVfb2ZfaXNzdWFuY2UiOiAi``
   ``MjAyMC0wMy0xOVQxMjo0M1oiLCAidm91Y2hlciI6IHsib3JnYW5pemF0aW9u``
   ``IjogIk1pbmlzdGVybyBkZWxsJ0ludGVybm8ifX19fV0``
-  Contents: ``["eluV5Og3gSNII8EYnsxA_A", "verification",``
   ``{"trust_framework": "it_cie", "assurance_level": "high", "evidence": {"type": "vouch",``
   ``"time": "2020-03-19T12:42Z", "attestation": {"type":``
   ``"digital_attestation", "reference_number":``
   ``"6485-1619-3976-6671", "date_of_issuance":``
   ``"2020-03-19T12:43Z", "voucher": {"organization": "Ministero``
   ``dell'Interno"}}}}]``

**Claim** ``given_name``:

-  SHA-256 Hash: ``zVdghcmClMVWlUgGsGpSkCPkEHZ4u9oWj1SlIBlCc1o``
-  Disclosure:
   ``WyI2SWo3dE0tYTVpVlBHYm9TNXRtdlZBIiwgImdpdmVuX25hbWUiLCAiTWFy``
   ``aW8iXQ``
-  Contents: ``["6Ij7tM-a5iVPGboS5tmvVA", "given_name", "Mario"]``

**Claim** ``family_name``:

-  SHA-256 Hash: ``VQI-S1mT1Kxfq2o8J9io7xMMX2MIxaG9M9PeJVqrMcA``
-  Disclosure:
   ``WyJlSThaV205UW5LUHBOUGVOZW5IZGhRIiwgImZhbWlseV9uYW1lIiwgIlJv``
   ``c3NpIl0``
-  Contents: ``["eI8ZWm9QnKPpNPeNenHdhQ", "family_name", "Rossi"]``

**Claim** ``birth_date``:

-  SHA-256 Hash: ``s1XK5f2pM3-aFTauXhmvd9pyQTJ6FMUhc-JXfHrxhLk``
-  Disclosure:
   ``WyJRZ19PNjR6cUF4ZTQxMmExMDhpcm9BIiwgImJpcnRoX2RhdGUiLCAiMTk4``
   ``MC0wMS0xMCJd``
-  Contents: ``["Qg_O64zqAxe412a108iroA", "birth_date", "1980-01-10"]``

**Claim** ``birth_place``:

- SHA-256 Hash: ``tSL-e1nLdWOU9sFMTCUu5P1tCzxA-TW-VWbHGzYtU7E``
- Disclosure:
  ``WyJBSngtMDk1VlBycFR0TjRRTU9xUk9BIiwgImJpcnRoX3BsYWNlIiwgIlJv``
  ``bWEiXQ``
- Contents: ``["AJx-095VPrpTtN4QMOqROA", "birth_place", "Roma"]``

**Claim** ``nationality``:

- SHA-256 Hash: ``hP79TuWGBwIN0j9NH_fxn8Cvj-dNH_R7nFleeWCE2I4``
- Disclosure:
  ``WyJQYzMzSk0yTGNoY1VfbEhnZ3ZfdWZRIiwgIm5hdGlvbmFsaXR5IiwgIklU``
  ``Il0``
- Contents: ``["Pc33JM2LchcU_lHggv_ufQ", "nationality", "IT"]``

**Claim** ``personal_administrative_number``:

-  SHA-256 Hash: ``6WLNc09rBr-PwEtnWzxGKdzImjrpDxbr4qoIx838a88``
-  Disclosure:
   ``WyJHMDJOU3JRZmpGWFE3SW8wOXN5YWpBIiwgInBlcnNvbmFsX2FkbWluaXN0``
   ``cmF0aXZlX251bWJlciIsICJYWDAwMDAwWFgiXQ``
-  Contents: ``["G02NSrQfjFXQ7Io09syajA", "personal_administrative_number",``
   ``"XX00000XX"]``

**Claim** ``tax_id_code``:

-  SHA-256 Hash: ``LqrtU2rlA51U97cMiYhqwa-is685bYiOJImp8a5KGNA``
-  Disclosure:
   ``WyJsa2x4RjVqTVlsR1RQVW92TU5JdkNBIiwgInRheF9pZF9jb2RlIiwgIlRJ``
   ``TklULVhYWFhYWFhYWFhYWFhYWFgiXQ``
-  Contents: ``["lklxF5jMYlGTPUovMNIvCA", "tax_id_code",``
   ``"TINIT-XXXXXXXXXXXXXXXX"]``

The combined format for the PID issuance is given by:

.. code-block::

  eyJhbGciOiAiRVMyNTYiLCAidHlwIjogImRjK3NkLWp3dCIsICJraWQiOiAiZEI2N2dM
  N2NrM1RGaUlBZjdONl83U0h2cWswTURZTUVRY29HR2xrVUFBdyJ9.eyJfc2QiOiBbIjZ
  XTE5jMDlyQnItUHdFdG5XenhHS2R6SW1qcnBEeGJyNHFvSXg4MzhhODgiLCAiTHFydFU
  ycmxBNTFVOTdjTWlZaHF3YS1pczY4NWJZaU9KSW1wOGE1S0dOQSIsICJWUUktUzFtVDF
  LeGZxMm84Sjlpbzd4TU1YMk1JeGFHOU05UGVKVnFyTWNBIiwgIllyYy1zLVdTcjRleEV
  ZdHFERXNtUmw3c3BvVmZtQnhpeFAxMmU0c3lxTkUiLCAiaDdFZ2w1SDlnVFBDX0ZDVTg
  0NWFhZHZzQy0tZFRqeTlOcnN0eGgtY2FSbyIsICJoUDc5VHVXR0J3SU4wajlOSF9meG4
  4Q3ZqLWROSF9SN25GbGVlV0NFMkk0IiwgInMxWEs1ZjJwTTMtYUZUYXVYaG12ZDlweVF
  USjZGTVVoYy1KWGZIcnhoTGsiLCAidFNMLWUxbkxkV09VOXNGTVRDVXU1UDF0Q3p4QS1
  UVy1WV2JIR3pZdFU3RSIsICJ6VmRnaGNtQ2xNVldsVWdHc0dwU2tDUGtFSFo0dTlvV2o
  xU2xJQmxDYzFvIl0sICJleHAiOiAxODgzMDAwMDAwLCAiaXNzIjogImh0dHBzOi8vcGl
  kcHJvdmlkZXIuZXhhbXBsZS5vcmciLCAic3ViIjogIk56YkxzWGg4dURDY2Q3bm9XWEZ
  aQWZIa3hac1JHQzlYcyIsICJpc3N1aW5nX2F1dGhvcml0eSI6ICJJc3RpdHV0byBQb2x
  pZ3JhZmljbyBlIFplY2NhIGRlbGxvIFN0YXRvIiwgImlzc3VpbmdfY291bnRyeSI6ICJ
  JVCIsICJzdGF0dXMiOiB7InN0YXR1c19hc3NlcnRpb24iOiB7ImNyZWRlbnRpYWxfaGF
  zaF9hbGciOiAic2hhLTI1NiJ9fSwgInZjdCI6ICJodHRwczovL3BpZHByb3ZpZGVyLmV
  4YW1wbGUub3JnL3YxLjAvcGVyc29uaWRlbnRpZmljYXRpb25kYXRhIiwgInZjdCNpbnR
  lZ3JpdHkiOiAiYzVmNzNlMjUwZmU4NjlmMjRkMTUxMThhY2NlMjg2YzliYjU2YjYzYTQ
  0M2RjODVhZjY1M2NkNzNmNjA3OGIxZiIsICJfc2RfYWxnIjogInNoYS0yNTYiLCAiY25
  mIjogeyJqd2siOiB7Imt0eSI6ICJFQyIsICJjcnYiOiAiUC0yNTYiLCAieCI6ICJUQ0F
  FUjE5WnZ1M09IRjRqNFc0dmZTVm9ISVAxSUxpbERsczd2Q2VHZW1jIiwgInkiOiAiWnh
  qaVdXYlpNUUdIVldLVlE0aGJTSWlyc1ZmdWVjQ0U2dDRqVDlGMkhaUSJ9fX0.7lV6m1K
  IsnwuJcR8DgrmRHBkLEXJcx7kVBI1rzlbBwZ_xMPwAd4Dfl06dyLKegdTZO1RDR3IDi-
  JyiuNMFlZOQ~WyIyR0xDNDJzS1F2ZUNmR2ZyeU5STjl3IiwgImlhdCIsIDE2ODMwMDAw
  MDBd~WyJlbHVWNU9nM2dTTklJOEVZbnN4QV9BIiwgInZlcmlmaWNhdGlvbiIsIHsidHJ
  1c3RfZnJhbWV3b3JrIjogIml0X2NpZSIsICJhc3N1cmFuY2VfbGV2ZWwiOiAiaGlnaCI
  sICJldmlkZW5jZSI6IHsidHlwZSI6ICJ2b3VjaCIsICJ0aW1lIjogIjIwMjAtMDMtMTl
  UMTI6NDJaIiwgImF0dGVzdGF0aW9uIjogeyJ0eXBlIjogImRpZ2l0YWxfYXR0ZXN0YXR
  pb24iLCAicmVmZXJlbmNlX251bWJlciI6ICI2NDg1LTE2MTktMzk3Ni02NjcxIiwgImR
  hdGVfb2ZfaXNzdWFuY2UiOiAiMjAyMC0wMy0xOVQxMjo0M1oiLCAidm91Y2hlciI6IHs
  ib3JnYW5pemF0aW9uIjogIk1pbmlzdGVybyBkZWxsJ0ludGVybm8ifX19fV0~WyI2SWo
  3dE0tYTVpVlBHYm9TNXRtdlZBIiwgImdpdmVuX25hbWUiLCAiTWFyaW8iXQ~WyJlSTha
  V205UW5LUHBOUGVOZW5IZGhRIiwgImZhbWlseV9uYW1lIiwgIlJvc3NpIl0~WyJRZ19P
  NjR6cUF4ZTQxMmExMDhpcm9BIiwgImJpcnRoX2RhdGUiLCAiMTk4MC0wMS0xMCJd~WyJ
  BSngtMDk1VlBycFR0TjRRTU9xUk9BIiwgImJpcnRoX3BsYWNlIiwgIlJvbWEiXQ~WyJQ
  YzMzSk0yTGNoY1VfbEhnZ3ZfdWZRIiwgIm5hdGlvbmFsaXR5IiwgIklUIl0~WyJHMDJO
  U3JRZmpGWFE3SW8wOXN5YWpBIiwgInBlcnNvbmFsX2FkbWluaXN0cmF0aXZlX251bWJl
  ciIsICJYWDAwMDAwWFgiXQ~WyJsa2x4RjVqTVlsR1RQVW92TU5JdkNBIiwgInRheF9pZ
  F9jb2RlIiwgIlRJTklULVhYWFhYWFhYWFhYWFhYWFgiXQ~


(Q)EAA non-normative Examples
-----------------------------

Below a non-normative example of (Q)EAA in JSON.

.. literalinclude:: ../../examples/qeaa-json-example-payload.json
  :language: JSON  

The corresponding SD-JWT for the previous data is represented as follow, as decoded JSON for both header and payload.

.. literalinclude:: ../../examples/qeaa-sd-jwt-example-header.json
  :language: JSON  

.. literalinclude:: ../../examples/qeaa-sd-jwt-example-payload.json
  :language: JSON  

In the following the disclosure list is given:

**Claim** ``iat``:

-  SHA-256 Hash: ``Yrc-s-WSr4exEYtqDEsmRl7spoVfmBxixP12e4syqNE``
-  Disclosure:
   ``WyIyR0xDNDJzS1F2ZUNmR2ZyeU5STjl3IiwgImlhdCIsIDE2ODMwMDAwMDBd``
-  Contents: ``["2GLC42sKQveCfGfryNRN9w", "iat", 1683000000]``

**Claim** ``document_number``:

-  SHA-256 Hash: ``Dx-6hjvrcxNzF0slU6ukNmzHoL-YvBN-tFa0T8X-bY0``
-  Disclosure:
   ``WyJlbHVWNU9nM2dTTklJOEVZbnN4QV9BIiwgImRvY3VtZW50X251bWJlciIs``
   ``ICJYWFhYWFhYWFhYIl0``
-  Contents:
   ``["eluV5Og3gSNII8EYnsxA_A", "document_number", "XXXXXXXXXX"]``

**Claim** ``given_name``:

-  SHA-256 Hash: ``zVdghcmClMVWlUgGsGpSkCPkEHZ4u9oWj1SlIBlCc1o``
-  Disclosure:
   ``WyI2SWo3dE0tYTVpVlBHYm9TNXRtdlZBIiwgImdpdmVuX25hbWUiLCAiTWFy``
   ``aW8iXQ``
-  Contents: ``["6Ij7tM-a5iVPGboS5tmvVA", "given_name", "Mario"]``

**Claim** ``family_name``:

-  SHA-256 Hash: ``VQI-S1mT1Kxfq2o8J9io7xMMX2MIxaG9M9PeJVqrMcA``
-  Disclosure:
   ``WyJlSThaV205UW5LUHBOUGVOZW5IZGhRIiwgImZhbWlseV9uYW1lIiwgIlJv``
   ``c3NpIl0``
-  Contents: ``["eI8ZWm9QnKPpNPeNenHdhQ", "family_name", "Rossi"]``

**Claim** ``birth_date``:

-  SHA-256 Hash: ``s1XK5f2pM3-aFTauXhmvd9pyQTJ6FMUhc-JXfHrxhLk``
-  Disclosure:
   ``WyJRZ19PNjR6cUF4ZTQxMmExMDhpcm9BIiwgImJpcnRoX2RhdGUiLCAiMTk4``
   ``MC0wMS0xMCJd``
-  Contents: ``["Qg_O64zqAxe412a108iroA", "birth_date", "1980-01-10"]``

**Claim** ``expiry_date``:

-  SHA-256 Hash: ``aBVdfcnxT0Z5RrwdxZSUhuUxz3gM2vcEZLeYIj61Kas``
-  Disclosure:
   ``WyJBSngtMDk1VlBycFR0TjRRTU9xUk9BIiwgImV4cGlyeV9kYXRlIiwgIjIw``
   ``MjQtMDEtMDEiXQ``
-  Contents: ``["AJx-095VPrpTtN4QMOqROA", "expiry_date", "2024-01-01"]``

**Claim** ``personal_administrative_number``:

-  SHA-256 Hash: ``o1cHG8JbEEYv0HeJINYKbFLd-TnEDUuNzI1XpzV32aU``
-  Disclosure:
   ``WyJQYzMzSk0yTGNoY1VfbEhnZ3ZfdWZRIiwgInBlcnNvbmFsX2FkbWluaXN0``
   ``cmF0aXZlX251bWJlciIsICJYWDAwMDAwWFgiXQ``
-  Contents: ``["Pc33JM2LchcU_lHggv_ufQ", "personal_administrative_number",``
   ``"XX00000XX"]``

**Claim** ``constant_attendance_allowance``:

-  SHA-256 Hash: ``GE3Sjy_zAT34f8wa5DUkVB0FslaSJRAAc8I3lN11Ffc``
-  Disclosure:
   ``WyJHMDJOU3JRZmpGWFE3SW8wOXN5YWpBIiwgImNvbnN0YW50X2F0dGVuZGFu``
   ``Y2VfYWxsb3dhbmNlIiwgdHJ1ZV0``
-  Contents:
   ``["G02NSrQfjFXQ7Io09syajA", "constant_attendance_allowance",``
   ``true]``


The combined format for the (Q)EAA issuance is represented below:

.. code-block::

  eyJhbGciOiAiRVMyNTYiLCAidHlwIjogImRjK3NkLWp3dCIsICJraWQiOiAiZDEyNmE2
  YTg1NmY3NzI0NTYwNDg0ZmE5ZGM1OWQxOTUifQ.eyJfc2QiOiBbIkR4LTZoanZyY3hOe
  kYwc2xVNnVrTm16SG9MLVl2Qk4tdEZhMFQ4WC1iWTAiLCAiR0UzU2p5X3pBVDM0Zjh3Y
  TVEVWtWQjBGc2xhU0pSQUFjOEkzbE4xMUZmYyIsICJWUUktUzFtVDFLeGZxMm84Sjlpb
  zd4TU1YMk1JeGFHOU05UGVKVnFyTWNBIiwgIllyYy1zLVdTcjRleEVZdHFERXNtUmw3c
  3BvVmZtQnhpeFAxMmU0c3lxTkUiLCAiYUJWZGZjbnhUMFo1UnJ3ZHhaU1VodVV4ejNnT
  TJ2Y0VaTGVZSWo2MUthcyIsICJvMWNIRzhKYkVFWXYwSGVKSU5ZS2JGTGQtVG5FRFV1T
  npJMVhwelYzMmFVIiwgInMxWEs1ZjJwTTMtYUZUYXVYaG12ZDlweVFUSjZGTVVoYy1KW
  GZIcnhoTGsiLCAielZkZ2hjbUNsTVZXbFVnR3NHcFNrQ1BrRUhaNHU5b1dqMVNsSUJsQ
  2MxbyJdLCAiZXhwIjogMTg4MzAwMDAwMCwgImlzcyI6ICJodHRwczovL2lzc3Vlci5le
  GFtcGxlLm9yZyIsICJzdWIiOiAiTnpiTHNYaDh1RENjZDdub1dYRlpBZkhreFpzUkdDO
  VhzIiwgImlzc3VpbmdfYXV0aG9yaXR5IjogIklzdGl0dXRvIFBvbGlncmFmaWNvIGUgW
  mVjY2EgZGVsbG8gU3RhdG8iLCAiaXNzdWluZ19jb3VudHJ5IjogIklUIiwgInN0YXR1c
  yI6IHsic3RhdHVzX2Fzc2VydGlvbiI6IHsiY3JlZGVudGlhbF9oYXNoX2FsZyI6ICJza
  GEtMjU2In19LCAidmN0IjogImh0dHBzOi8vaXNzdWVyLmV4YW1wbGUub3JnL3YxLjAvZ
  GlzYWJpbGl0eWNhcmQiLCAidmN0I2ludGVncml0eSI6ICIyZTQwYmNkNjc5OTAwODA4N
  WZmYjFhMWYzNTE3ZWZlZTMzNTI5OGZkOTc2YjNlNjU1YmZiM2Y0ZWFhMTFkMTcxIiwgI
  l9zZF9hbGciOiAic2hhLTI1NiIsICJjbmYiOiB7Imp3ayI6IHsia3R5IjogIkVDIiwgI
  mNydiI6ICJQLTI1NiIsICJ4IjogIlRDQUVSMTladnUzT0hGNGo0VzR2ZlNWb0hJUDFJT
  GlsRGxzN3ZDZUdlbWMiLCAieSI6ICJaeGppV1diWk1RR0hWV0tWUTRoYlNJaXJzVmZ1Z
  WNDRTZ0NGpUOUYySFpRIn19fQ.L-km4kT5RCMVd9S5ZuVxINxfiSOksgcQNTGb71EhjF
  fkqptx-upFnx3KEHHmGFoyftiT1ScKHBUiWvBj32MAYg~WyIyR0xDNDJzS1F2ZUNmR2Z
  yeU5STjl3IiwgImlhdCIsIDE2ODMwMDAwMDBd~WyJlbHVWNU9nM2dTTklJOEVZbnN4QV
  9BIiwgImRvY3VtZW50X251bWJlciIsICJYWFhYWFhYWFhYIl0~WyI2SWo3dE0tYTVpVl
  BHYm9TNXRtdlZBIiwgImdpdmVuX25hbWUiLCAiTWFyaW8iXQ~WyJlSThaV205UW5LUHB
  OUGVOZW5IZGhRIiwgImZhbWlseV9uYW1lIiwgIlJvc3NpIl0~WyJRZ19PNjR6cUF4ZTQ
  xMmExMDhpcm9BIiwgImJpcnRoX2RhdGUiLCAiMTk4MC0wMS0xMCJd~WyJBSngtMDk1Vl
  BycFR0TjRRTU9xUk9BIiwgImV4cGlyeV9kYXRlIiwgIjIwMjQtMDEtMDEiXQ~WyJQYzM
  zSk0yTGNoY1VfbEhnZ3ZfdWZRIiwgInBlcnNvbmFsX2FkbWluaXN0cmF0aXZlX251bWJ
  lciIsICJYWDAwMDAwWFgiXQ~WyJHMDJOU3JRZmpGWFE3SW8wOXN5YWpBIiwgImNvbnN0
  YW50X2F0dGVuZGFuY2VfYWxsb3dhbmNlIiwgdHJ1ZV0~

MDOC-CBOR Credential Format
====================================

The mDOC data model is based on the ISO/IEC 18013-5 standard, initially developed for the mobile driving license (mDL) use case. 
The mDOC data elements MUST be encoded in CBOR as defined in `RFC 8949 - Concise Binary Object Representation (CBOR) <RFC 8949 - Concise Binary Object Representation (CBOR)>`_.

This data model structures mDOC Digital Credentials into distinct components: namespaces (**nameSpaces**), and cryptographic proof (**issuerAuth**). 
Namespaces categorize and structure data elements (or attributes, see `Attribute Namespaces`_). While, the cryptographic proof ensures integrity and authenticity through the Mobile Security Object (MSO).

The MSO securely stores cryptographic digests of attributes within the `nameSpaces`. This allows Relying Parties to validate disclosed attributes against corresponding **digestID** values without revealing the entire credential.
See `Mobile Security Object`_ for details.

The structure of an mDOC-CBOR Credential is outlined below and further elaborated in the following sections.

.. list-table:: 
    :widths: 20 60 20
    :header-rows: 1

    * - **Parameter**
      - **Description**
      - **Reference**
    * - **nameSpaces** 
      - *tstr (text string)*. The namespaces within which the data elements are defined. A Digital Credential MAY include multiple namespaces. Mandatory mDL attributes utilize the standard namespace `org.iso.18013.5.1`. However, it MAY have a domestic namespace, such as `org.iso.18013.5.1.it`, to include additional attributes defined in this implementation profile. Each namespace within the `nameSpaces` MUST share the same issued document type (`docType`) value, which identifies the nature of the Digital Credential, as defined in the `issuerAuth`. 
      - [ISO 18013-5#8.3.2.1.2]
    * - **issuerAuth**
      - *bstr (byte string)*. Contains *Mobile Security Object* (MSO), a COSE Sign1 Document, issued by the Credential Issuer.
      - [ISO 18013-5#9.1.2.4]

Attribute Namespaces
--------------------------------
The **nameSpaces** object contains one or more *nameSpace* entries, each identified by a name. Within each **nameSpace**, it includes one or more *IssuerSignedItemBytes*, each encoded as a CBOR byte sring with Tag 24 (#6.24(bstr .cbor)), which appears as 24(<<... >>) in diagnostic notation. It represents the disclosure information for each digest within the `Mobile Security Object` and MUST contain the following attributes:

.. list-table:: 
    :widths: 20 60 20
    :header-rows: 1

    * - **Name**
      - **Encoding**
      - **Description**
    * - **digestID**
      - *integer*
      - Reference value to one of the ``ValueDigests`` provided in the *Mobile Security Object* (`issuerAuth`).
    * - **random**
      - *bstr (byte string)*
      - Random byte value used as salt for the hash function. This value SHALL be different for each *IssuerSignedItem* and it SHALL have a minimum length of 16 bytes.
    * - **elementIdentifier**
      - *tstr (text string)*
      - Data element identifier.
    * - **elementValue**
      - *any value (depends on the data element)*.
      - Data element value.

Attributes 
--------------------------------
The following **elementIdentifiers**, relevant to the Credential Issuer, MUST be included in a Digital Credential encoded in mDOC-CBOR within the respective *nameSpace*: 

.. list-table:: 
   :widths: 30 70
   :header-rows: 1

   * - **Element Identifier**
     - **Description**

   * - **issuing_country**
     - *tstr (text string)*. Alpha-2 country code as defined in [ISO 3166-1], representing the issuing country or territory. 

   * - **issuing_authority**
     - *tstr (text string)*. Name of the administrative authority that has issued the mDL.  
       The value shall only use Latin1b characters and shall have a maximum length of 150 characters. 

.. note::
      User-specific attributes for mDOC Digital Credentials such as those used in mDL or PID are also included by referencing the appropriate `elementIdentifiers` defined in ISO/IEC 18013-5 or the `EIDAS-ARF`_ specification. Other Digital Credential User-specific attributes are defined in the Catalogue of Digital Credentials.


Mobile security Object
--------------------------

The **issuerAuth** represents the `Mobile Security Object` which is a `COSE Sign1 Document` defined in `RFC 9052 - CBOR Object Signing and Encryption (COSE): Structures and Process <https://www.rfc-editor.org/rfc/rfc9052.html>`_. It has the following data structure:

* protected header
* unprotected header
* payload
* signature.

The **protected header** MUST contain the following parameter encoded in CBOR format:

.. list-table:: 
    :widths: 20 60 20
    :header-rows: 1

    * - **Element**
      - **Description**
      - **Reference**
    * - **1**
      - Algorithm used to verify the cryptographic signature of the mDOC Digital Credential (REQUIRED).
      - :rfc:`9053`

.. note::
    
    Only the signature algorithm MUST be present in the protected header, other elements SHOULD not be present in the protected header.


The **unprotected header** MUST contain the following parameter:

.. list-table:: 
    :widths: 20 60 20
    :header-rows: 1

    * - **Element**
      - **Description**
      - **Reference**
    * - **4**
      - Unique identifier of the Issuer JWK (OPTIONAL). Required when the issuer of mDOC uses OpenID Federation. 
      - `Trust Model`_
    * - **33**
      - X.509 certificate chain about the Issuer (OPTIONAL). Required for X.509 certificate-based authentication.
      - `RFC 9360 CBOR Object Signing and Encryption (COSE) - Header Parameters for Carrying and Referencing X.509 Certificates`_.

.. note::
    The `x5chain` is included in the unprotected header with the aim to allow the Holder to update the X.509 certificate chain, related to the `Mobile Security Object` issuer, without invalidating the signature.

The **payload** MUST contain the *MobileSecurityObject*, without the `content-type` COSE Sign header parameter and encoded as a *byte string* (bstr) using the *CBOR Tag* 24.

The `MobileSecurityObjectBytes` MUST have the following attributes:

.. list-table:: 
    :widths: 20 60 20
    :header-rows: 1

    * - **Element**
      - **Description**
      - **Reference**
    * - **docType**
      - *tstr (text string)*. Defines the type of mDOC Digital Credential being issued. For example, for an mDL, the value MUST be ``org.iso.18013-5.1.mDL``.
      - [ISO 18013-5#8.3.2.1.2]
    * - **version**
      - *(tstr)* Version of the data structure being used.
      - [ISO 18013-5#9.1.2.4]
    * - **validityInfo**
      - Object containing issuance and expiration datetimes. It MUST contain the following sub-value:

          * *signed*
          * *validFrom*
          * *validUntil*
      - [ISO 18013-5#9.1.2.4]
    * - **digestAlgorithm**
      - According to the algorithm defined in the protected header.
      - [ISO 18013-5#9.1.2.4]
    * - **valueDigests**
      - Mapped digest by unique id, grouped by namespaces.
      - [ISO 18013-5#9.1.2.4]
    * - **deviceKeyInfo**
      - It MUST contain the Wallet Instance's public key containing the following sub-values:

          * *deviceKey* (REQUIRED).
          * *keyAuthorizations* (OPTIONAL).
          * *keyInfo* (OPTIONAL).
      - [ISO 18013-5#9.1.2.4]
    * - **status**
      - REQUIRED only if the Digital Credential is long-lived. Contains the MSO revocation information. If present, it includes a *status_list* based on the TOKEN-STATUS-LIST_ mechanism, which uses a bit array to mark revoked MSOs by position (bit set to 1 = revoked). 
      - [ISO 18013-5#9.1.2.6]

The `status_list` MUST have the following attributes:

.. list-table:: 
  :widths: 20 60 20
  :header-rows: 1

  * - **Parameter**
    - **Description**
    - **Reference**
  * - **idx**
    - *integer*.  A non-negative number representing the index to check for the MSO status information in the Status List.
    - [TOKEN-STATUS-LIST_]
  * - **uri**
    - *str*. A URI identifying the Status List Token that contains the MSO status information. The value of `uri` MUST be a URI conforming to [:rfc:3986].
    - [TOKEN-STATUS-LIST_]


.. note::
    The private key related to the public key stored in the `deviceKey` object is used to sign the `DeviceSignedItems` object and proves the possession of the Digital Credential during the presentation phase (see the presentation phase with mDOC-CBOR).


MDOC-CBOR Examples
----------------------
A non-normative example of an mDL encoded in CBOR is shown below in binary encoding.

.. code-block:: cbor

    a26a6e616d65537061636573a2716f72672e69736f2e31383031332e352e318bd818a100a4686469676573744944006672616e646f6d5820352dad268e35f7ae728b0b5ae14537a2f027b730ec25e50d45cfcac0d519ff7371656c656d656e744964656e74696669657268706f7274726169746c656c656d656e7456616c7565590412ffd8ffe000104a46494600010101009000900000ffdb004300130d0e110e0c13110f11151413171d301f1d1a1a1d3a2a2c2330453d4947443d43414c566d5d4c51685241435f82606871757b7c7b4a5c869085778f6d787b76ffdb0043011415151d191d381f1f38764f434f7676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676ffc00011080018006403012200021101031101ffc4001b00000301000301000000000000000000000005060401020307ffc400321000010303030205020309000000000000010203040005110612211331141551617122410781a1163542527391b2c1f1ffc4001501010100000000000000000000000000000001ffc4001a110101010003010000000000000000000000014111213161ffda000c03010002110311003f00a5bbde22da2329c7d692bc7d0d03f52cfb0ff75e7a7ef3e7709723a1d0dae146ddfbb3c039ce07ad2bd47a7e32dbb8dd1d52d6ef4b284f64a480067dfb51f87ffb95ff00eb9ff14d215de66af089ce44b7dbde9cb6890a2838eddf18078f7add62d411ef4db9b10a65d6b95a147381ea0d495b933275fe6bba75c114104a8ba410413e983dff004f5af5d34b4b4cde632d0bf1fd1592bdd91c6411f3934c2fa6af6b54975d106dcf4a65ae56e856001ebc03c7ce29dd9eef1ef10fc447dc9da76ad2aee93537a1ba7e4f70dd8eff0057c6dffb5e1a19854a83758e54528750946ec6704850cd037bceb08b6d7d2cc76d3317fc7b5cc04fb6707269c5c6e0c5b60ae549242123b0e493f602a075559e359970d98db89525456b51c951c8afa13ea8e98e3c596836783d5c63f5a61a99fdb7290875db4be88ab384bbbbbfc7183fdeaa633e8951db7da396dc48524fb1a8bd611a5aa2a2432f30ab420a7a6d3240c718cf031fa9ef4c9ad550205aa02951df4a1d6c8421b015b769db8c9229837ea2be8b1b0d39d0eba9c51484efdb8c0efd8d258daf3c449699f2edbd4584e7af9c64e3f96b9beb28d4ac40931e6478c8e76a24a825449501d867d2b1dcdebae99b9c752ae4ecd6dde4a179c1c1e460938f9149ef655e515c03919a289cb3dca278fb7bf177f4faa829dd8ce3f2ac9a7ecde490971fafd7dce15eed9b71c018c64fa514514b24e8e4f8c5c9b75c1e82579dc1233dfec08238f6add62d391acc1c5256a79e706d52d431c7a0145140b9fd149eb3a60dc5e88cbbc2da092411e9dc71f39a7766b447b344e847dcac9dcb5abba8d145061d43a6fcf1e65cf15d0e90231d3dd9cfe62995c6dcc5ca12a2c904a15f71dd27d451453e09d1a21450961cbb3ea8a956433b781f1ce33dfed54f0e2b50a2b71d84ed6db18028a28175f74fc6bda105c529a791c25c4f3c7a11f71586268f4a66b726e33de9ea6f1b52b181c760724e47b514520a5a28a283ffd9d818a101a4686469676573744944016672616e646f6d5820d40eaba09c935a43245f606a55c943a8d47ec2bf20c839b5572ae96434f0680471656c656d656e744964656e7469666965726f646f63756d656e745f6e756d6265726c656c656d656e7456616c756569585831323334353637d818a102a4686469676573744944026672616e646f6d5820f7ba829250f8d3ff784fb903e9679515d4cb43eb5d992a5d4a912a15961ab0af71656c656d656e744964656e7469666965726b6578706972795f646174656c656c656d656e7456616c7565d903ec6a323032342d30322d3232d818a103a4686469676573744944036672616e646f6d58207b774f01a76ff6f0fb2cc7a510cd6e73ce18bf790a13ec164a34121732e0fc5771656c656d656e744964656e7469666965726a62697274685f646174656c656c656d656e7456616c7565d903ec6a313935362d30312d3132d818a104a4686469676573744944046672616e646f6d58201075baf23ad198552e56dd18df68d663b6fe6580a3701190ca6b0d24016fa0db71656c656d656e744964656e7469666965727169737375696e675f617574686f726974796c656c656d656e7456616c756577476c6920616d6963692064656c6c612053616c61726961d818a105a4686469676573744944056672616e646f6d5820b84e7ab48c417a318f3774e1e416f09709ca90ebc173068d40ec00f5149e4a5671656c656d656e744964656e74696669657276756e5f64697374696e6775697368696e675f7369676e6c656c656d656e7456616c75656149d818a106a4686469676573744944066672616e646f6d5820c3f81e5eef9d0fd29904f9f8044fec5d5e819fa9717252e116797c8fa1a27d8571656c656d656e744964656e7469666965726a69737375655f646174656c656c656d656e7456616c7565d903ec6a323032332d31312d3134d818a107a4686469676573744944076672616e646f6d582055237af20b921a1b4af10e239d394f27aacd9e4c0b8ab49111fd9a494b388f9371656c656d656e744964656e7469666965726b66616d696c795f6e616d656c656c656d656e7456616c756565526f737369d818a108a4686469676573744944086672616e646f6d5820732c9e2f547489c5bda745385740cd95abd87ddf84c89f0a04368632a60aa83f71656c656d656e744964656e7469666965726a676976656e5f6e616d656c656c656d656e7456616c7565654d6172696fd818a109a4686469676573744944096672616e646f6d5820abcb57fa9724d958df0fde346e7a14db9c5aa5c7e9117a4ad60e7a4d33c2744571656c656d656e744964656e7469666965727264726976696e675f70726976696c656765736c656c656d656e7456616c756581a37576656869636c655f63617465676f72795f636f646561416a69737375655f64617465d903ec4b6a323032302d30392d31376b6578706972795f64617465d903ec4b6a323033312d30362d3130d818a10aa46864696765737449440a6672616e646f6d5820360c04252e23402ea2c185d95fbf97e366a46f79e3311f7401d620ce8890a4aa71656c656d656e744964656e7469666965726f69737375696e675f636f756e7472796c656c656d656e7456616c7565624954746f72672e69736f2e31383031332e352e312e697483d818a10ba46864696765737449440b6672616e646f6d58203da584b9db34f95c2775a7fbf38f76da9132f799924c4517943198f2dfa10ff971656c656d656e744964656e74696669657275766572696669636174696f6e2e65766964656e63656c656c656d656e7456616c7565a3716f7267616e697a6174696f6e5f6e616d65754d6f746f72697a7a617a696f6e6520436976696c656f6f7267616e697a6174696f6e5f6964656d5f696e666c636f756e7472795f636f6465626974d818a10ca46864696765737449440c6672616e646f6d58207b5e596c50fdb98ff8eb03c0fa7d182194db03d142cf09263881c9c85b3ca76f71656c656d656e744964656e746966696572781c766572696669636174696f6e2e6173737572616e63655f6c6576656c6c656c656d656e7456616c75656468696768d818a10da46864696765737449440d6672616e646f6d58204cb5c9ebed080245206975bf7a4442a43542e6ab6eae4c448f7cc9e3dcf60bcc71656c656d656e744964656e746966696572781c766572696669636174696f6e2e74727573745f6672616d65776f726b6c656c656d656e7456616c75656565696461736a697373756572417574685907c3d28459021fa30126044864656d6f2d6b6964182159020d30820209308201afa00302010202140f7faf063dcc89971f88c7fc8f085749fe305b8e300a06082a8648ce3d0403023064310b30090603550406130255533113301106035504080c0a43616c69666f726e69613116301406035504070c0d53616e204672616e636973636f31133011060355040a0c0a4d7920436f6d70616e793113301106035504030c0a6d79736974652e636f6d301e170d3235303331393136333932355a170d3235303332393136333932355a3064310b30090603550406130255533113301106035504080c0a43616c69666f726e69613116301406035504070c0d53616e204672616e636973636f31133011060355040a0c0a4d7920436f6d70616e793113301106035504030c0a6d79736974652e636f6d3059301306072a8648ce3d020106082a8648ce3d03010703420004bd341248121b095938b3535100cd681da6a1dd21ae50ef5ffa86fdc7171a3c50853d47361f62b5f994aecba076794720bb3c5c6feee96924fe0ec15cdbed2c6ba33f303d303b0603551d1104343032863068747470733a2f2f63726564656e7469616c2d6973737565722e6f6964632d66656465726174696f6e2e6f6e6c696e65300a06082a8648ce3d0403020348003045022100c9c03d20b3c7ff91691a1579a770200e91a1c31c8caeeeaf1fba5db57ce4126c02207a831486a317dd12558a6ad0daa9fbdd3aee265a8ed85867a21116c1851cacd4a1182159020c30820208308201afa00302010202140dd5a357decd7e620a698cbcba0f8bda9c89f587300a06082a8648ce3d0403023064310b30090603550406130255533113301106035504080c0a43616c69666f726e69613116301406035504070c0d53616e204672616e636973636f31133011060355040a0c0a4d7920436f6d70616e793113301106035504030c0a6d79736974652e636f6d301e170d3235303331393136333932355a170d3235303332393136333932355a3064310b30090603550406130255533113301106035504080c0a43616c69666f726e69613116301406035504070c0d53616e204672616e636973636f31133011060355040a0c0a4d7920436f6d70616e793113301106035504030c0a6d79736974652e636f6d3059301306072a8648ce3d020106082a8648ce3d03010703420004bd341248121b095938b3535100cd681da6a1dd21ae50ef5ffa86fdc7171a3c50853d47361f62b5f994aecba076794720bb3c5c6feee96924fe0ec15cdbed2c6ba33f303d303b0603551d1104343032863068747470733a2f2f63726564656e7469616c2d6973737565722e6f6964632d66656465726174696f6e2e6f6e6c696e65300a06082a8648ce3d040302034700304402206b21dc7c1afbb0a5c160ba90c833203b0cd9753daee05e866538f580fbc16262022015627000f9cfc98d3fc02c35e5092e2dad8cf6ed0f846a7add739c2974ff1594590348a66776657273696f6e63312e306f646967657374416c676f726974686d667368613235366c76616c756544696765737473a2716f72672e69736f2e31383031332e352e31ab005820404412351c233550913d4afa740b7fe24eb6c8346f9e8d84b6b2d20ed2a1df44015820387b0fccb667a0e9a303319b874f80bc7fc76a94c397b372f5d260c90fd87dfb025820b05d51800e5fe503eeb35918a7dba5872fa98bed3ccff1de9157f46f0231cda8035820a8e79da85b283fcf15cd60fcc19a938041291f3f23ab5643d420f92567a948d9045820366870d42facd384f364e0ac134063e5fff619a72aa3fbf727d6eb289d2cbbd30558201d97be51115c7ffdf701397dfd2d18e237a44eab15d0368a72f428fcb7fde7b40658200bafbdc4f6844633bbea942036fff60627b66907010653cdb4b6ce844188d95b0758203f5eb799763b416bb37f2ef0a661c64be5e2058a3a8b9993cbdc9a95d0a9270f08582084930bf9058b03db4588ca55985401665159b1571d99934eb17a8f4080197c420958209a6c112f1191b5bfa274c07574dd0ae588c5895f77c7e0fab1e88788bcda65610a5820a421c1e617c9bd1be62d08198d33a89578db590f84c9ca9268200a31f48cac35746f72672e69736f2e31383031332e352e312e6974a30b58208de0b6d2b48a543dec8f8d782f8f39a9d68ff27ee709b62fd791c519bf933c600c5820bdb221d8591b3879e01781d1082f54d46af32b32f4cf8ef991803a58e51df6d00d5820d2663ee7a94ea6deb412d5354e9a45621e2df12417a6356c53093538895799e46d6465766963654b6579496e666fa1696465766963654b6579a5613102622d3101622d32582096313d6c63e24e3372742bfdb1a33ba2c897dcd68ab8c753e4fbd48dca6b7f9a622d3358201fb3269edd418857de1b39a4e4a44b92fa484caa722c228288f01d0c03a2c3d6636b69644a64656d6f2d642d6b696467646f6354797065716f72672e69736f2e31383031332e352e316c76616c6964697479496e666fa3667369676e656456c074323032352d30332d31395431363a33393a32355a6976616c696446726f6d56c074323032352d30332d31395431363a33393a32355a6a76616c6964556e74696c56c074323033302d30332d31385431363a33393a32355a5840fe9bfb00a0f6bdb184deccd8c7bdf71ce94a8d752267b2fa01c8a554f419d88a2b4121c56692d61b1f9d2823c95c8e6c19f3ffa64193cbf0c18404ff17d024e4

The Diagnostic Notation of the CBOR-encoded mDL is given below. 

.. literalinclude:: ../../examples/mDL-mdoc-cbor-example.txt
  :language: text

Cross-Format Credential Parameters Mapping
======================================================
The following table provides a comparative mapping between the data structures of SD-JWT-VC and mDOC-CBOR Digital Credentials.
It outlines the key data elements and parameters used in each format, highlighting both commonalities and differences.
In particular, it shows how core concepts—such as issuer information, validity, cryptographic binding, and disclosures—are represented in these credential formats.

For SD-JWT-VC, parameters are marked with `(hdr)` if they are located in the JOSE header, and `(pld)` if they appear in the payload of the JWT. In mDOC-CBOR, these parameters are identified within the issuerAuth or nameSpaces structures.

.. list-table:: 
   :header-rows: 1

   * - **Information Related To**
     - **SD-JWT-VC Parameters**
     - **mDOC-CBOR Parameters**
   * - Digital Credential definition
     - vct (pld)
     - | issuerAuth.doctype
       | issuerAuth.version
   * - Digital Credential metadata
     - | vctm.name (hdr)
       | vctm.description (hdr)
       | vctm.extends (hdr)
       | vctm.schema (hdr)
       | vctm.schema_uri (hdr)
       | vctm.data_source (hdr)
       | vctm.display (hdr)
       | vctm.claims (hdr)
     - | –
       | –
       | –
       | –
       | –
       | –
       | –
       | nameSpaces
   * - Issuer
     - | iss (pld)
       | issuing_authority (pld)
       | issuing_country (pld)
     - | –
       | nameSpaces.elementIdentifier.issuing_authority
       | nameSpaces.elementIdentifier.issuing_country
   * - Subject
     - sub (pld)
     - nameSpaces.elementIdentifier.sub
   * - Validity period
     - | iat (pld)
       | exp (pld)
       | nbf (pld)
     - | issuerAuth.validityInfo.signed
       | issuerAuth.validityInfo.validUntil
       | issuerAuth.validityInfo.validFrom
   * - Status mechanism
     - | status_assertation (pld)
       | status_list (pld)
     - | –
       | issuerAuth.status_list
   * - Signature
     - | alg (hdr)
       | kid (hdr)
     - | issuerAuth.1 (alg)
       | issuerAuth.4 (kid)
   * - Trust anchors
     - | trust_chain (OID-FED) (hdr)
       | x5c (hdr)
     - | –
       | issuerAuth.33 (x5chain)
   * - Cryptographic binding
     - cnf.jwk (pld)
     - issuerAuth.deviceKeyInfo.deviceKey
   * - Selective disclosure
     - | _sd_alg (pld)
       | _sd (pld)
     - | issuerAuth.digestAlgorithm
       | issuerAuth.valueDigests
   * - Integrity
     - | vct#integrity (pld)
       | vctm.extends#integrity (hdr)
       | vctm.schema_uri#integrity (hdr)
     - | 
       | –
       | 
   * - Digital Credential format
     - typ (hdr)
     - –
   * - Digital Credential auditability
     - verification (pld)
     - nameSpaces.elementIdentifier.verification
   * - Disclosures
     - | salt
       | claim name
       | claim value
     - | 
       | nameSpaces
       |

.. note::

   - In the mDOC-CBOR format, the version of the Digital Credential is not explicitly defined; it is only available for the IssuerAuth.  In contrast, the SD-JWT format includes version information via the `vct` URL.
   - `Disclosures`, `_sd`, and `_sd_alg` enable selective disclosure of SD-JWT claims.  The `_sd` and `_sd_alg` parameters are part of the SD-JWT payload, while `Disclosures` are sent separately in a Combined Format along with the SD-JWT.
   - The `vctm.claims` parameter in SD-JWT and the `nameSpaces` structure in mDOC-CBOR are functionally equivalent, as both define the claim names and their structure. SD-JWT `Disclosures` for disclosed attributes directly correspond to `nameSpaces`, including attribute names, values, and salt values.
   - A domestic namespace accommodates attributes such as `verification` and `sub`, which are not defined in the standard ISO elementIdentifiers for mDOC-CBOR Digital Credentials.


.. _Attribute Namespaces: pid-eaa-data-model.html#attribute-namespaces
.. _Mobile Security Object: pid-eaa-data-model.html#mobile-security-object
.. _RFC 9360 CBOR Object Signing and Encryption (COSE) - Header Parameters for Carrying and Referencing X.509 Certificates: https://datatracker.ietf.org/doc/rfc9360/
.. _Trust Model: trust.html
.. _ARF: https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/tree/main
.. _PID Rulebook: https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/annexes/annex-3/annex-3.01-pid-rulebook.md


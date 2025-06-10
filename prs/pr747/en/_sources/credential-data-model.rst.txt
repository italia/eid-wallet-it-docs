
.. include:: ../common/common_definitions.rst


Digital Credential Data Model
==============================

The Digital Credential Data Model structures Digital Credentials for secure, interoperable use. Key elements include:

    - Credential Subject: The individual or entity receiving the Credential.
    - Issuer: The Credential Issuer issuing and signing the Credential.
    - Metadata: Details about the Credential, like type and validity.
    - Claims: Information about the subject, such as identity or qualifications.
    - Proof: Cryptographic verification of authenticity and legitimate ownership.

The Person Identification Data (PID) is issued by the PID Provider according to national laws. The main scope of the PID is allowing natural persons to be authenticated for access to a service or to a protected resource.
The User attributes provided within the Italian PID are the ones listed below:

    - Current Family Name
    - Current First Name
    - Date of Birth
    - Taxpayer identification number

The (Q)EAAs are issued by (Q)EAA Issuers to a Wallet Instance and MUST be provided in SD-JWT-VC or mdoc-CBOR data format.

The Digital Credential data format and the mechanism through which a Digital Credential is issued to the Wallet Instance and presented to a Relying Party are described in the following sections.

SD-JWT-VC Credential Format
---------------------------

The PID/(Q)EAA is issued in the form of a Digital Credential. The Digital Credential format is `SD-JWT`_ as specified in `SD-JWT-VC`_.

SD-JWT MUST be signed using the Issuer's private key. SD-JWT MUST be provided along with a Type Metadata related to the issued Digital Credential according to Sections 6 and 6.3 of [`SD-JWT-VC`_]. The payload MUST contain the **_sd_alg** claim described in Section 4.1.1 `SD-JWT`_ and other claims specified in this section.

The claim **_sd_alg** indicates the hash algorithm used by the Issuer to generate the digests as described in Section 4.1.1 of `SD-JWT`_. **_sd_alg** MUST be set to one of the specified algorithms in Section :ref:`Cryptographic Algorithms <algorithms:Cryptographic Algorithms>`.

Claims that are not selectively disclosable MUST be included in the SD-JWT as they are. The digests of the disclosures, along with any decoy if present, MUST be contained in the **_sd** array, as specified in Section 4.2.4.1 of `SD-JWT`_.

Each digest value, calculated using a hash function over the disclosures, verifies the integrity and corresponds to a specific Disclosure. Each disclosure includes:

  - a random salt,
  - the claim name (only when the claim is an object element),
  - the claim value.

In case of nested objects in a SD-JWT payload, each claim at every level of the JSON, should be individually marked as selectively disclosable or not. Therefore **_sd** claim containing digests MAY appear multiple times at different levels in the SD-JWT.

For each claim that is an array element the digests of the respective disclosures and decoy digests are added to the array in the same position of the original claim values as specified in Section 4.2.4.2 of `SD-JWT`_.

In case of array elements, digest values are calculated using a hash function over the disclosures, containing:

  - a random salt,
  - the array element.

In case of multiple array elements, the Issuer may hide the value of the entire array or any of the entry contained within the array, the Holder can disclose both the entire array and any single entry within the array, as defined in Section 4.2.6 of `SD-JWT`_.

The Disclosures are provided to the Holder together with the SD-JWT in the *Combined Format for Issuance* that is an ordered series of base64url-encoded values, each separated from the next by a single tilde ('~') character as follows:

.. code-block:: text

  <Issuer-Signed-JWT>~<Disclosure 1>~<Disclosure 2>~...~<Disclosure N>

See `SD-JWT-VC`_ and `SD-JWT`_ for additional details.


Credential SD-JWT Parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The JOSE header contains the following mandatory parameters:

.. _table_pid_jose_header:
.. list-table::
  :class: longtable
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

.. _table_sd-jwt-vc_parameters:
.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Description**
      - **Reference**
    * - **iss**
      - [NSD]. REQUIRED. URL string representing the Credential Issuer unique identifier.
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
      - [NSD]. REQUIRED. Name of the administrative authority that has issued the Credential.
      - Commission Implementing Regulation `EU_2024/2977`_.
    * - **issuing_country**
      - [NSD]. REQUIRED. Alpha-2 country code, as specified in ISO 3166-1, of the country or territory of the Credential Issuer.
      - Commission Implementing Regulation `EU_2024/2977`_.
    * - **status**
      - [NSD]. REQUIRED only if the Digital Credential is long-lived. JSON object containing the information on how to read the status of the Verifiable Credential. It MUST contain either the JSON member *status_assertion* or *status_list*.
      - Section 3.2.2.2 `SD-JWT-VC`_ and Section 11 `OAUTH-STATUS-ASSERTION`_.
    * - **cnf**
      - [NSD]. REQUIRED. JSON object containing the proof-of-possession key materials. By including a **cnf** (confirmation) claim in a JWT, the Issuer of the JWT declares that the Holder is in control of the private key related to the public one defined in the **cnf** parameter. The recipient MUST cryptographically verify that the Holder is in control of that key.
      - `[RFC7800, Section 3.1] <https://www.iana.org/go/rfc7800>`_ and Section 3.2.2.2 `SD-JWT-VC`_.
    * - **vct**
      - [NSD]. REQUIRED. Credential type value MUST be an HTTPS URL String and it MUST be set using one of the values obtained from the Credential Issuer metadata. It is the identifier of the SD-JWT VC type and it MUST be set with a collision-resistant value as defined in Section 2 of :rfc:`7515`. It MUST contain also the number of version of the Credential type (for instance: ``https://trust-registry.eid-wallet.example.it/credentials/v1.0/personidentificationdata``).
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
   :class: longtable
   :widths: 20 60 20
   :header-rows: 1

   * - **Parameter**
     - **Description**
     - **Reference**
   * - **idx**
     - REQUIRED. The idx (index) claim MUST specify an Integer that represents the index to check for status information in the Status List for the current Digital Credential. The value of idx MUST be a non-negative number, containing a value of zero or greater.
     - TOKEN-STATUS-LIST_
   * - **uri**
     - REQUIRED. The ``uri`` (URI) claim MUST specify a String value that identifies the Status List Token containing the status information for the Digital Credential. The value of ``uri`` MUST be a URI conforming to [:rfc:`3986`].
     - TOKEN-STATUS-LIST_


If the ``status`` parameter is set to ``status_assertion``, it is a JSON Object containing the *credential_hash_alg* claim indicating the Algorithm used for hashing the Digital Credential to which the Status Assertion is bound. It is RECOMMENDED to use *sha-256*.


.. note::
  Credential Type Metadata JSON Document MAY be retrieved directly from the URL contained in the claim **vct**, using the HTTP GET method or using the ``vctm`` header parameter if provided. Unlike specified in Section 6.3.1 of `SD-JWT-VC`_ the **.well-known** endpoint is not included in the current implementation profile. Implementers may decide to use it for interoperability with other systems.


Digital Credential Metadata Type
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Metadata type document MUST be a JSON object and contains the following parameters.

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Description**
      - **Reference**
    * - **name**
      - REQUIRED. Human-readable name of the Digital Credential type. In case of multiple languages, the language tags are added to the member name, delimited with the character `#` as defined in :rfc:`5646` (e.g. *name#it-IT*).
      - [`SD-JWT-VC`_] Section 6.2 and [`OIDC`_] Section 5.2.
    * - **description**
      - REQUIRED. A human-readable description of the Digital Credential type. In case of multiple languages, the language tags are added to the member name, delimited by a `#` character as defined in :rfc:`5646`.
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
            The use of the SVG template is RECOMMENDED for all applications that support it.

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

PID Claims
^^^^^^^^^^

Depending on the Digital Credential type **vct**, additional claims data MAY be added. The PID supports the following data:

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Description**
      - **Reference**
    * - **given_name**
      - [SD]. REQUIRED. Current First Name. (*String*)
      - Section 5.1 of `OIDC`_ and Commission Implementing Regulation `EU_2024/2977`_
    * - **family_name**
      - [SD]. REQUIRED. Current Family Name. (*String*)
      - Section 5.1 of `OIDC`_ and Commission Implementing Regulation `EU_2024/2977`_
    * - **birth_date**
      - [SD]. REQUIRED. Date of Birth. (*String, [ISO8601‑1] YYYY-MM-DD format*)
      - Commission Implementing Regulation `EU_2024/2977`_
    * - **birth_place**
      - [SD]. REQUIRED. Place of Birth. (*String*)
      - Commission Implementing Regulation `EU_2024/2977`_
    * - **nationalities**
      - [SD]. REQUIRED. One or more alpha-2 country codes as specified in ISO 3166-1. (*Array of strings*)
      - Commission Implementing Regulation `EU_2024/2977`_
    * - **personal_administrative_number**
      - [SD]. CONDITIONAL. REQUIRED if ``tax_id_code`` is not present. National unique identifier of a natural person generated by ANPR in string format. (*String*)
      - Commission Implementing Regulation `EU_2024/2977`_
    * - **tax_id_code**
      - [SD]. CONDITIONAL. REQUIRED if ``personal_administrative_number`` is not present. National tax identification code of natural person as a String format. It MUST be set according to ETSI EN 319 412-1. For example ``TINIT-<ItalianTaxIdentificationNumber>``. (*String*)
      -


PID Non-Normative Examples
^^^^^^^^^^^^^^^^^^^^^^^^^^

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

- SHA-256 Hash: ``Yrc-s-WSr4exEYtqDEsmRl7spoVfmBxixP12e4syqNE``
- Disclosure:
   ``WyIyR0xDNDJzS1F2ZUNmR2ZyeU5STjl3IiwgImlhdCIsIDE2ODMwMDAwMDBd``
- Contents: ``["2GLC42sKQveCfGfryNRN9w", "iat", 1683000000]``

**Claim** ``verification``:

- SHA-256 Hash: ``h7Egl5H9gTPC_FCU845aadvsC--dTjy9Nrstxh-caRo``
- Disclosure:
   ``WyJlbHVWNU9nM2dTTklJOEVZbnN4QV9BIiwgInZlcmlmaWNhdGlvbiIsIHsi``
   ``dHJ1c3RfZnJhbWV3b3JrIjogIml0X2NpZSIsICJhc3N1cmFuY2VfbGV2ZWwi``
   ``OiAiaGlnaCIsICJldmlkZW5jZSI6IHsidHlwZSI6ICJ2b3VjaCIsICJ0aW1l``
   ``IjogIjIwMjAtMDMtMTlUMTI6NDJaIiwgImF0dGVzdGF0aW9uIjogeyJ0eXBl``
   ``IjogImRpZ2l0YWxfYXR0ZXN0YXRpb24iLCAicmVmZXJlbmNlX251bWJlciI6``
   ``ICI2NDg1LTE2MTktMzk3Ni02NjcxIiwgImRhdGVfb2ZfaXNzdWFuY2UiOiAi``
   ``MjAyMC0wMy0xOVQxMjo0M1oiLCAidm91Y2hlciI6IHsib3JnYW5pemF0aW9u``
   ``IjogIk1pbmlzdGVybyBkZWxsJ0ludGVybm8ifX19fV0``
- Contents: ``["eluV5Og3gSNII8EYnsxA_A", "verification",``
   ``{"trust_framework": "it_cie", "assurance_level": "high", "evidence": {"type": "vouch",``
   ``"time": "2020-03-19T12:42Z", "attestation": {"type":``
   ``"digital_attestation", "reference_number":``
   ``"6485-1619-3976-6671", "date_of_issuance":``
   ``"2020-03-19T12:43Z", "voucher": {"organization": "Ministero``
   ``dell'Interno"}}}}]``

**Claim** ``given_name``:

- SHA-256 Hash: ``zVdghcmClMVWlUgGsGpSkCPkEHZ4u9oWj1SlIBlCc1o``
- Disclosure:
   ``WyI2SWo3dE0tYTVpVlBHYm9TNXRtdlZBIiwgImdpdmVuX25hbWUiLCAiTWFy``
   ``aW8iXQ``
- Contents: ``["6Ij7tM-a5iVPGboS5tmvVA", "given_name", "Mario"]``

**Claim** ``family_name``:

- SHA-256 Hash: ``VQI-S1mT1Kxfq2o8J9io7xMMX2MIxaG9M9PeJVqrMcA``
- Disclosure:
   ``WyJlSThaV205UW5LUHBOUGVOZW5IZGhRIiwgImZhbWlseV9uYW1lIiwgIlJv``
   ``c3NpIl0``
- Contents: ``["eI8ZWm9QnKPpNPeNenHdhQ", "family_name", "Rossi"]``

**Claim** ``birth_date``:

- SHA-256 Hash: ``s1XK5f2pM3-aFTauXhmvd9pyQTJ6FMUhc-JXfHrxhLk``
- Disclosure:
   ``WyJRZ19PNjR6cUF4ZTQxMmExMDhpcm9BIiwgImJpcnRoX2RhdGUiLCAiMTk4``
   ``MC0wMS0xMCJd``
- Contents: ``["Qg_O64zqAxe412a108iroA", "birth_date", "1980-01-10"]``

**Claim** ``birth_place``:

- SHA-256 Hash: ``tSL-e1nLdWOU9sFMTCUu5P1tCzxA-TW-VWbHGzYtU7E``
- Disclosure:
  ``WyJBSngtMDk1VlBycFR0TjRRTU9xUk9BIiwgImJpcnRoX3BsYWNlIiwgIlJv``
  ``bWEiXQ``
- Contents: ``["AJx-095VPrpTtN4QMOqROA", "birth_place", "Roma"]``

**Claim** ``personal_administrative_number``:

- SHA-256 Hash: ``6WLNc09rBr-PwEtnWzxGKdzImjrpDxbr4qoIx838a88``
- Disclosure:
   ``WyJHMDJOU3JRZmpGWFE3SW8wOXN5YWpBIiwgInBlcnNvbmFsX2FkbWluaXN0``
   ``cmF0aXZlX251bWJlciIsICJYWDAwMDAwWFgiXQ``
- Contents: ``["G02NSrQfjFXQ7Io09syajA", "personal_administrative_number",``
   ``"XX00000XX"]``

**Claim** ``tax_id_code``:

- SHA-256 Hash: ``LqrtU2rlA51U97cMiYhqwa-is685bYiOJImp8a5KGNA``
- Disclosure:
   ``WyJsa2x4RjVqTVlsR1RQVW92TU5JdkNBIiwgInRheF9pZF9jb2RlIiwgIlRJ``
   ``TklULVhYWFhYWFhYWFhYWFhYWFgiXQ``
- Contents: ``["lklxF5jMYlGTPUovMNIvCA", "tax_id_code",``
   ``"TINIT-XXXXXXXXXXXXXXXX"]``

**Array Entry** of ``nationalities``:

- SHA-256 Hash: ``yKeP1CWTQK8Sd9BeNvFhkLXgEu/1G3QQz4CWSlqEOFw``
- Disclosure: ``WyJQYzMzSk0yTGNoY1VfbEhnZ3ZfdWZRIiwgIklUIl0``
- Contents: ``["Pc33JM2LchcU_lHggv_ufQ", "IT"]``

The combined format for the PID issuance is given by:

.. code-block:: text

  eyJhbGciOiAiRVMyNTYiLCAidHlwIjogImRjK3NkLWp3dCIsICJraWQiOiAiZEI2N2dM
  N2NrM1RGaUlBZjdONl83U0h2cWswTURZTUVRY29HR2xrVUFBdyJ9.ewogICJfc2QiOiB
  bCiAgICAiNldMTmMwOXJCci1Qd0V0bld6eEdLZHpJbWpycER4YnI0cW9JeDgzOGE4OCI
  sCiAgICAiTHFydFUycmxBNTFVOTdjTWlZaHF3YS1pczY4NWJZaU9KSW1wOGE1S0dOQSI
  sCiAgICAiVlFJLVMxbVQxS3hmcTJvOEo5aW83eE1NWDJNSXhhRzlNOVBlSlZxck1jQSI
  sCiAgICAiWXJjLXMtV1NyNGV4RVl0cURFc21SbDdzcG9WZm1CeGl4UDEyZTRzeXFORSI
  sCiAgICAiaDdFZ2w1SDlnVFBDX0ZDVTg0NWFhZHZzQy0tZFRqeTlOcnN0eGgtY2FSbyI
  sCiAgICAiczFYSzVmMnBNMy1hRlRhdVhobXZkOXB5UVRKNkZNVWhjLUpYZkhyeGhMayI
  sCiAgICAidFNMLWUxbkxkV09VOXNGTVRDVXU1UDF0Q3p4QS1UVy1WV2JIR3pZdFU3RSI
  sCiAgICAielZkZ2hjbUNsTVZXbFVnR3NHcFNrQ1BrRUhaNHU5b1dqMVNsSUJsQ2MxbyI
  KICBdLAogICJleHAiOiAxODgzMDAwMDAwLAogICJpc3MiOiAiaHR0cHM6Ly9waWRwcm9
  2aWRlci5leGFtcGxlLm9yZyIsCiAgInN1YiI6ICJOemJMc1hoOHVEQ2NkN25vV1hGWkF
  mSGt4WnNSR0M5WHMiLAogICJpc3N1aW5nX2F1dGhvcml0eSI6ICJJc3RpdHV0byBQb2x
  pZ3JhZmljbyBlIFplY2NhIGRlbGxvIFN0YXRvIiwKICAiaXNzdWluZ19jb3VudHJ5Ijo
  gIklUIiwKICAic3RhdHVzIjogewogICAgInN0YXR1c19hc3NlcnRpb24iOiB7CiAgICA
  gICJjcmVkZW50aWFsX2hhc2hfYWxnIjogInNoYS0yNTYiCiAgICB9CiAgfSwKICAibmF
  0aW9uYWxpdGllcyI6IFsKCXsKICAgICAgIi4uLiI6ICJ5S2VQMUNXVFFLOFNkOUJlTnZ
  GaGtMWGdFdS8xRzNRUXo0Q1dTbHFFT0Z3IgogICAgfQogIF0sCiAgInZjdCI6ICJodHR
  wczovL3RydXN0LXJlZ2lzdHJ5LmVpZC13YWxsZXQuZXhhbXBsZS5pdC9jcmVkZW50aWF
  scy92MS4wL3BlcnNvbmlkZW50aWZpY2F0aW9uZGF0YSIsCiAgInZjdCNpbnRlZ3JpdHk
  iOiAiYzVmNzNlMjUwZmU4NjlmMjRkMTUxMThhY2NlMjg2YzliYjU2YjYzYTQ0M2RjODV
  hZjY1M2NkNzNmNjA3OGIxZiIsCiAgIl9zZF9hbGciOiAic2hhLTI1NiIsCiAgImNuZiI
  6IHsKICAgICJqd2siOiB7CiAgICAgICJrdHkiOiAiRUMiLAogICAgICAiY3J2IjogIlA
  tMjU2IiwKICAgICAgIngiOiAiVENBRVIxOVp2dTNPSEY0ajRXNHZmU1ZvSElQMUlMaWx
  EbHM3dkNlR2VtYyIsCiAgICAgICJ5IjogIlp4amlXV2JaTVFHSFZXS1ZRNGhiU0lpcnN
  WZnVlY0NFNnQ0alQ5RjJIWlEiCiAgICB9CiAgfQp9.ISeLw-Tqpmcos9ms7KQTfUhSm4
  srAtGOMNQe3M-toaYhCcT4JnvZANmtBb8rOXdJ60oTtya4krCOjFNirEg3-g~WyIyR0x
  DNDJzS1F2ZUNmR2ZyeU5STjl3IiwgImlhdCIsIDE2ODMwMDAwMDBd~WyJlbHVWNU9nM2
  dTTklJOEVZbnN4QV9BIiwgInZlcmlmaWNhdGlvbiIsIHsidHJ1c3RfZnJhbWV3b3JrIj
  ogIml0X2NpZSIsICJhc3N1cmFuY2VfbGV2ZWwiOiAiaGlnaCIsICJldmlkZW5jZSI6IH
  sidHlwZSI6ICJ2b3VjaCIsICJ0aW1lIjogIjIwMjAtMDMtMTlUMTI6NDJaIiwgImF0dG
  VzdGF0aW9uIjogeyJ0eXBlIjogImRpZ2l0YWxfYXR0ZXN0YXRpb24iLCAicmVmZXJlbm
  NlX251bWJlciI6ICI2NDg1LTE2MTktMzk3Ni02NjcxIiwgImRhdGVfb2ZfaXNzdWFuY2
  UiOiAiMjAyMC0wMy0xOVQxMjo0M1oiLCAidm91Y2hlciI6IHsib3JnYW5pemF0aW9uIj
  ogIk1pbmlzdGVybyBkZWxsJ0ludGVybm8ifX19fV0~WyI2SWo3dE0tYTVpVlBHYm9TNX
  RtdlZBIiwgImdpdmVuX25hbWUiLCAiTWFyaW8iXQ~WyJlSThaV205UW5LUHBOUGVOZW5
  IZGhRIiwgImZhbWlseV9uYW1lIiwgIlJvc3NpIl0~WyJRZ19PNjR6cUF4ZTQxMmExMDh
  pcm9BIiwgImJpcnRoX2RhdGUiLCAiMTk4MC0wMS0xMCJd~WyJBSngtMDk1VlBycFR0Tj
  RRTU9xUk9BIiwgImJpcnRoX3BsYWNlIiwgIlJvbWEiXQ~WyJQYzMzSk0yTGNoY1VfbEh
  nZ3ZfdWZRIiwgIklUIl0~WyJHMDJOU3JRZmpGWFE3SW8wOXN5YWpBIiwgInBlcnNvbmF
  sX2FkbWluaXN0cmF0aXZlX251bWJlciIsICJYWDAwMDAwWFgiXQ~WyJsa2x4RjVqTVls
  R1RQVW92TU5JdkNBIiwgInRheF9pZF9jb2RlIiwgIlRJTklULVhYWFhYWFhYWFhYWFhY
  WFgiXQ~

(Q)EAA non-normative Examples
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Below is a non-normative example of (Q)EAA in JSON.

.. literalinclude:: ../../examples/qeaa-json-example-payload.json
  :language: JSON

The corresponding SD-JWT for the previous data is represented as follow, as decoded JSON for both header and payload.

.. literalinclude:: ../../examples/qeaa-sd-jwt-example-header.json
  :language: JSON

.. literalinclude:: ../../examples/qeaa-sd-jwt-example-payload.json
  :language: JSON

In the following the disclosure list is given:

**Claim** ``iat``:

- SHA-256 Hash: ``Yrc-s-WSr4exEYtqDEsmRl7spoVfmBxixP12e4syqNE``
- Disclosure:
   ``WyIyR0xDNDJzS1F2ZUNmR2ZyeU5STjl3IiwgImlhdCIsIDE2ODMwMDAwMDBd``
- Contents: ``["2GLC42sKQveCfGfryNRN9w", "iat", 1683000000]``

**Claim** ``document_number``:

- SHA-256 Hash: ``Dx-6hjvrcxNzF0slU6ukNmzHoL-YvBN-tFa0T8X-bY0``
- Disclosure:
   ``WyJlbHVWNU9nM2dTTklJOEVZbnN4QV9BIiwgImRvY3VtZW50X251bWJlciIs``
   ``ICJYWFhYWFhYWFhYIl0``
- Contents:
   ``["eluV5Og3gSNII8EYnsxA_A", "document_number", "XXXXXXXXXX"]``

**Claim** ``given_name``:

- SHA-256 Hash: ``zVdghcmClMVWlUgGsGpSkCPkEHZ4u9oWj1SlIBlCc1o``
- Disclosure:
   ``WyI2SWo3dE0tYTVpVlBHYm9TNXRtdlZBIiwgImdpdmVuX25hbWUiLCAiTWFy``
   ``aW8iXQ``
- Contents: ``["6Ij7tM-a5iVPGboS5tmvVA", "given_name", "Mario"]``

**Claim** ``family_name``:

- SHA-256 Hash: ``VQI-S1mT1Kxfq2o8J9io7xMMX2MIxaG9M9PeJVqrMcA``
- Disclosure:
   ``WyJlSThaV205UW5LUHBOUGVOZW5IZGhRIiwgImZhbWlseV9uYW1lIiwgIlJv``
   ``c3NpIl0``
- Contents: ``["eI8ZWm9QnKPpNPeNenHdhQ", "family_name", "Rossi"]``

**Claim** ``birth_date``:

- SHA-256 Hash: ``s1XK5f2pM3-aFTauXhmvd9pyQTJ6FMUhc-JXfHrxhLk``
- Disclosure:
   ``WyJRZ19PNjR6cUF4ZTQxMmExMDhpcm9BIiwgImJpcnRoX2RhdGUiLCAiMTk4``
   ``MC0wMS0xMCJd``
- Contents: ``["Qg_O64zqAxe412a108iroA", "birth_date", "1980-01-10"]``

**Claim** ``expiry_date``:

- SHA-256 Hash: ``aBVdfcnxT0Z5RrwdxZSUhuUxz3gM2vcEZLeYIj61Kas``
- Disclosure:
   ``WyJBSngtMDk1VlBycFR0TjRRTU9xUk9BIiwgImV4cGlyeV9kYXRlIiwgIjIw``
   ``MjQtMDEtMDEiXQ``
- Contents: ``["AJx-095VPrpTtN4QMOqROA", "expiry_date", "2024-01-01"]``

**Claim** ``personal_administrative_number``:

- SHA-256 Hash: ``o1cHG8JbEEYv0HeJINYKbFLd-TnEDUuNzI1XpzV32aU``
- Disclosure:
   ``WyJQYzMzSk0yTGNoY1VfbEhnZ3ZfdWZRIiwgInBlcnNvbmFsX2FkbWluaXN0``
   ``cmF0aXZlX251bWJlciIsICJYWDAwMDAwWFgiXQ``
- Contents: ``["Pc33JM2LchcU_lHggv_ufQ", "personal_administrative_number",``
   ``"XX00000XX"]``

**Claim** ``constant_attendance_allowance``:

- SHA-256 Hash: ``GE3Sjy_zAT34f8wa5DUkVB0FslaSJRAAc8I3lN11Ffc``
- Disclosure:
   ``WyJHMDJOU3JRZmpGWFE3SW8wOXN5YWpBIiwgImNvbnN0YW50X2F0dGVuZGFu``
   ``Y2VfYWxsb3dhbmNlIiwgdHJ1ZV0``
- Contents:
   ``["G02NSrQfjFXQ7Io09syajA", "constant_attendance_allowance",``
   ``true]``


The combined format for the (Q)EAA issuance is represented below:

.. code-block:: text

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
  GEtMjU2In19LCAidmN0IjogImh0dHBzOi8vdHJ1c3QtcmVnaXN0cnkuZWlkLXdhbGxld
  C5leGFtcGxlLml0L2NyZWRlbnRpYWxzL3YxLjAvRXVyb3BlYW5EaXNhYmlsaXR5Q2FyZ
  CIsICJ2Y3QjaW50ZWdyaXR5IjogIjJlNDBiY2Q2Nzk5MDA4MDg1ZmZiMWExZjM1MTdlZ
  mVlMzM1Mjk4ZmQ5NzZiM2U2NTViZmIzZjRlYWExMWQxNzEiLCAiX3NkX2FsZyI6ICJza
  GEtMjU2IiwgImNuZiI6IHsiandrIjogeyJrdHkiOiAiRUMiLCAiY3J2IjogIlAtMjU2I
  iwgIngiOiAiVENBRVIxOVp2dTNPSEY0ajRXNHZmU1ZvSElQMUlMaWxEbHM3dkNlR2VtY
  yIsICJ5IjogIlp4amlXV2JaTVFHSFZXS1ZRNGhiU0lpcnNWZnVlY0NFNnQ0alQ5RjJIW
  lEifX19.2Dt5a6CFNv-YAmfewZGERmlIOdYybaNtZP6Va1zHZ_IqZAGM8S6M4mcTU-RO
  3X4cU4j20xif2Ocf1jvd2L5CRQ~WyIyR0xDNDJzS1F2ZUNmR2ZyeU5STjl3IiwgImlhd
  CIsIDE2ODMwMDAwMDBd~WyJlbHVWNU9nM2dTTklJOEVZbnN4QV9BIiwgImRvY3VtZW50
  X251bWJlciIsICJYWFhYWFhYWFhYIl0~WyI2SWo3dE0tYTVpVlBHYm9TNXRtdlZBIiwg
  ImdpdmVuX25hbWUiLCAiTWFyaW8iXQ~WyJlSThaV205UW5LUHBOUGVOZW5IZGhRIiwgI
  mZhbWlseV9uYW1lIiwgIlJvc3NpIl0~WyJRZ19PNjR6cUF4ZTQxMmExMDhpcm9BIiwgI
  mJpcnRoX2RhdGUiLCAiMTk4MC0wMS0xMCJd~WyJBSngtMDk1VlBycFR0TjRRTU9xUk9B
  IiwgImV4cGlyeV9kYXRlIiwgIjIwMjQtMDEtMDEiXQ~WyJQYzMzSk0yTGNoY1VfbEhnZ
  3ZfdWZRIiwgInBlcnNvbmFsX2FkbWluaXN0cmF0aXZlX251bWJlciIsICJYWDAwMDAwW
  FgiXQ~WyJHMDJOU3JRZmpGWFE3SW8wOXN5YWpBIiwgImNvbnN0YW50X2F0dGVuZGFuY2
  VfYWxsb3dhbmNlIiwgdHJ1ZV0~

mdoc-CBOR Credential Format
---------------------------

The mdoc data model is based on the ISO/IEC 18013-5 standard.
The mdoc data elements MUST be encoded in CBOR as defined in :rfc:`8949`.

This data model structures mdoc Digital Credentials into distinct components: namespaces (**nameSpaces**), and cryptographic proof (**issuerAuth**).
Namespaces categorize and structure data elements (or attributes, see :ref:`credential-data-model:Attribute Namespaces`). While the cryptographic proof ensures integrity and authenticity through the Mobile Security Object (MSO).

The MSO securely stores cryptographic digests of attributes within the `nameSpaces`. This allows Relying Parties to validate disclosed attributes against corresponding **digestID** values without revealing the entire Credential.
See :ref:`credential-data-model:Mobile Security Object` for details.

An mdoc-CBOR Digital Credential MUST be compliant with the following structure:

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Parameter**
      - **Description**
      - **Reference**
    * - **nameSpaces**
      - *(map)*. The namespaces within which the data elements are defined. A Digital Credential MAY include multiple namespaces. Mandatory mDL attributes utilize the standard namespace `org.iso.18013.5.1`. However, it MAY have a domestic namespace, such as `org.iso.18013.5.1.IT`, to include additional attributes defined in this implementation profile. Each namespace within the `nameSpaces` MUST share the same issued document type (`docType`) value, which identifies the nature of the Digital Credential, as defined in the `issuerAuth`.
      - [ISO 18013-5#8.3.2.1.2]
    * - **issuerAuth**
      - *(COSE_Sign1)*. Contains *Mobile Security Object* (MSO), a COSE Sign1 Document, issued by the Credential Issuer.
      - [ISO 18013-5#9.1.2.4]

The structure of an mdoc-CBOR Credential is further elaborated in the following sections.

Attribute Namespaces
^^^^^^^^^^^^^^^^^^^^

The **nameSpaces** contains one or more *nameSpace* entries, each identified by a name. Within each **nameSpace**, it includes one or more *IssuerSignedItemBytes*, each encoded as a CBOR byte string with Tag 24 (#6.24(bstr .cbor)), which appears as 24(<<... >>) in diagnostic notation. It represents the disclosure information for each digest within the `Mobile Security Object` and MUST contain the following attributes:

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Name**
      - **Description**
      - **Reference**
    * - **digestID**
      - *(uint)*. Reference value to one of the ``ValueDigests`` provided in the *Mobile Security Object*.
      - [ISO 18013-5#9.1.2.5]
    * - **random**
      - *(bstr)*. Random byte value used as salt for the hash function. This value SHALL be different for each *IssuerSignedItem* and it SHALL have a minimum length of 16 bytes.
      - [ISO 18013-5#9.1.2.5]
    * - **elementIdentifier**
      - *(tstr)*. Data element identifier.
      - [ISO 18013-5#8.3.2.1.2.3]
    * - **elementValue**
      - *(any)*. Data element value.
      - [ISO 18013-5#8.3.2.1.2.3]

Attributes
^^^^^^^^^^

The following **elementIdentifiers** MUST be included in a Digital Credential encoded in mdoc-CBOR within the respective *nameSpace*, unless otherwise specified:

.. list-table::
   :class: longtable
   :widths: 20 60 20
   :header-rows: 1

   * - **Element Identifier**
     - **Description**
     - **Reference**

   * - **issuing_country**
     - *(tstr)*. Alpha-2 country code as defined in [ISO 3166-1], representing the issuing country or territory.
     - [ISO 18013-5#7.2]

   * - **issuing_authority**
     - *(tstr)*. Name of the administrative authority that has issued the mDL.
       The value shall only use Latin1b characters and shall have a maximum length of 150 characters.
     - [ISO 18013-5#7.2]

   * - **sub**
     - *(uuid)*. Identifies the subject of the mdoc Digital Credential (the User).
       The identifier MUST be opaque, MUST NOT correspond to any anagraphic data, and MUST NOT be derived from the User's anagraphic data through pseudonymization. Additionally, different Credentials issued to the same User MUST NOT reuse the same `sub` value.
     -

   * - **verification**
     - *(map, OPTIONAL)*. Contains authentication and verification details of the User. It has the same logic structure and purpose as reported in the :ref:`Table of the SD-JWT parameters <table_sd-jwt-vc_parameters>`.
     -

.. note::
  Digital Credential User-specific attributes are defined in the Catalogue of Digital Credentials.
  User-specific attributes for mdoc Digital Credentials such as those used in mDL or PID are also included by referencing the appropriate `elementIdentifiers` defined in ISO/IEC 18013-5 or the `EIDAS-ARF`_ specification.

Mobile Security Object
^^^^^^^^^^^^^^^^^^^^^^

The **issuerAuth** represents the `Mobile Security Object` which is a `COSE Sign1 Document` defined in :rfc:`9052`. It has the following data structure:

   * protected header
   * unprotected header
   * payload
   * signature.

The **protected header** MUST contain the following parameter encoded in CBOR format:

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Element**
      - **Description**
      - **Reference**
    * - **1**
      - *(int)*. Algorithm used to verify the cryptographic signature of the mdoc Digital Credential.
      - :rfc:`9053`

.. note::
  Only the signature algorithm MUST be present in the protected header, other elements SHOULD not be present in the protected header.

The **unprotected header** MUST contain the following parameters, unless otherwise specified:

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Element**
      - **Description**
      - **Reference**
    * - **4**
      - *(tstr, OPTIONAL)*. Unique identifier of the Issuer JWK. Required when the Issuer of mdoc uses OpenID Federation.
      - :ref:`trust:The Infrastructure of Trust`
    * - **33**
      - *(array)*. X.509 certificate chain about the Issuer. Required for X.509 certificate-based authentication.
      - :rfc:`9360`

.. note::
  The `x5chain` is included in the unprotected header with the aim to allow the Holder to update the X.509 certificate chain, related to the `Mobile Security Object` issuer, without invalidating the signature.

The **payload** MUST contain the *MobileSecurityObject*, without the `content-type` COSE Sign header parameter and encoded as a *byte string* (bstr) using the *CBOR Tag* 24.

The `MobileSecurityObject` MUST have the following attributes, unless otherwise specified:

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Element**
      - **Description**
      - **Reference**
    * - **docType**
      - *(tstr)*. Defines the type of mdoc Digital Credential being issued. For example, for an mDL, the value MUST be ``org.iso.18013.5.1.mDL``. Specific `docType` MAY be defined for Digital Credential other than mDL.
      - [ISO 18013-5#9.1.2.4]
    * - **version**
      - *(tstr)*. Version of the `MobileSecurityObject`.
      - [ISO 18013-5#9.1.2.4]
    * - **validityInfo**
      - *(map)*. Contains the `MobileSecurityObject` issuance and expiration datetimes. It MUST contain the following sub-value:

          * **signed** *(tdate)*. The timestamp indicating when the `MobileSecurityObject` was signed.
          * **validFrom** *(tdate)*. Timestamp before which the `MobileSecurityObject` is not considered valid. MUST be equal to or later than the `signed` time.
          * **validUntil** *(tdate)*. Timestamp after which the `MobileSecurityObject` is no longer considered valid.

      - [ISO 18013-5#9.1.2.4]
    * - **digestAlgorithm**
      - *(tstr)*. Identifier of the digest algorithm, which MUST match the algorithm defined in the protected header.
      - [ISO 18013-5#9.1.2.4]
    * - **valueDigests**
      - *(map)*. Maps each namespace identifier to a set of digests, where each digest is keyed by a unique `digestID` and holds the digest value.
      - [ISO 18013-5#9.1.2.4]
    * - **deviceKeyInfo**
      - *(map)*. Contains metadata about the Wallet Instance's public key. It MUST include the following sub-fields, unless otherwise specified:

          * **deviceKey** *(COSE_Key)*. Contains the public key parameters.
          * **keyAuthorizations** *(map, OPTIONAL)*. Defines authorizations for either full namespaces or individual data elements.
          * **keyInfo** *(map, OPTIONAL)*. Contains additional metadata about the key.

      - [ISO 18013-5#9.1.2.4]
    * - **status**
      - *(map, CONDITIONAL)*. REQUIRED only if the Digital Credential is long-lived. Contains the MSO revocation information. If present, it includes a *status_list* based on the TOKEN-STATUS-LIST_ mechanism. This mechanism uses a bit array to mark revoked MSOs by their index position.
        The `status_list` MUST contain the following sub-values:

          * **idx**. Position index in the status list.
          * **uri**. URI pointing to the status list resource.
      - [ISO 18013-5#9.1.2.6]

.. note::
  The private key related to the public key stored in the `deviceKey` map is used to sign the `DeviceSignedItems` and to prove the possession of the Digital Credential during the presentation phase (see the presentation phase with mdoc-CBOR).

mdoc-CBOR Examples
^^^^^^^^^^^^^^^^^^
A non-normative example of an mDL encoded in CBOR is shown below in binary encoding.

.. literalinclude:: ../../examples/mDL-cbor-encoded-example.txt
  :language: text

The Diagnostic Notation of the CBOR-encoded mDL is given below.

.. literalinclude:: ../../examples/mDL-mdoc-cbor-example.txt
  :language: text

CBOR Acronyms
^^^^^^^^^^^^^

.. list-table::
   :class: longtable
   :widths: 20 80
   :header-rows: 1

   * - **Acronym**
     - **Meaning**
   * - `tstr`
     - Text String
   * - `bstr`
     - Byte String
   * - `int`
     - Signed Integer
   * - `uint`
     - Unsigned Integer
   * - `uuid`
     - Universally Unique Identifier
   * - `bool`
     - Boolean (true/false)
   * - `tdate`
     - Tagged Date (for example, Tag `0` is used to indicate a date/time string in RFC 3339 format)

Cross-Format Credential Parameters Mapping
------------------------------------------

The following table provides a comparative mapping between the data structures of SD-JWT-VC and mdoc-CBOR Digital Credentials.
It outlines the key data elements and parameters used in each format, highlighting both commonalities and differences.
In particular, it shows how core concepts - such as Credential Issuer information, validity, Cryptographic Binding, and disclosures - are represented in these Credential formats.

For SD-JWT-VC, parameters are marked with `(hdr)` if they are located in the JOSE header, and `(pld)` if they appear in the payload of the JWT. In mdoc-CBOR, these parameters are identified within the issuerAuth or nameSpaces structures.

.. list-table::
   :class: longtable
   :widths: 20 40 40
   :header-rows: 1

   * - **Information Related To**
     - **SD-JWT-VC Parameters**
     - **mdoc-CBOR Parameters**
   * - Digital Credential type definition
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
     - | -
       | -
       | -
       | -
       | -
       | -
       | -
       | nameSpaces
   * - Issuer
     - | iss (pld)
       | issuing_authority (pld)
       | issuing_country (pld)
     - | -
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
     - | status_assertion (pld)
       | status_list (pld)
     - | -
       | issuerAuth.status_list
   * - Signature
     - | alg (hdr)
       | kid (hdr)
     - | issuerAuth.1 (alg)
       | issuerAuth.4 (kid)
   * - Trust anchors
     - | trust_chain (OID-FED) (hdr)
       | x5c (hdr)
     - | -
       | issuerAuth.33 (x5chain)
   * - Cryptographic Binding
     - cnf.jwk (pld)
     - issuerAuth.deviceKeyInfo.deviceKey
   * - Selective Disclosure
     - | _sd_alg (pld)
       | _sd (pld)
     - | issuerAuth.digestAlgorithm
       | issuerAuth.valueDigests
   * - Integrity
     - | vct#integrity (pld)
       | vctm.extends#integrity (hdr)
       | vctm.schema_uri#integrity (hdr)
     - |
       | -
       |
   * - Digital Credential format
     - typ (hdr)
     - -
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
  - In the mdoc-CBOR format, the version of the Digital Credential is not explicitly defined; it is only available for the IssuerAuth. In contrast, the SD-JWT format includes version information via the `vct` URL.
  - `Disclosures`, `_sd`, and `_sd_alg` enable Selective Disclosure of SD-JWT claims. The `_sd` and `_sd_alg` parameters are part of the SD-JWT payload, while `Disclosures` are sent separately in a Combined Format along with the SD-JWT.
  - The `vctm.claims` parameter in SD-JWT and the `nameSpaces` structure in mdoc-CBOR are functionally equivalent, as both define the claim names and their structure. SD-JWT `Disclosures` for disclosed attributes directly correspond to `nameSpaces`, including attribute names, values, and salt values.
  - A domestic namespace accommodates attributes such as `verification` and `sub`, which are not defined in the standard ISO elementIdentifiers for mdoc-CBOR Digital Credentials.






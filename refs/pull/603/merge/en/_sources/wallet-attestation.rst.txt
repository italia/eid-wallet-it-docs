.. include:: ../common/common_definitions.rst

.. _wallet-attestation.rst:

Wallet Attestation
------------------------------


Wallet Attestation contains information regarding the security level of the device hosting the Wallet Instance.
It primarily certifies the **authenticity**, **integrity**, **security**, **privacy**, and **trustworthiness** of a particular Wallet Instance.

.. figure:: ../../images/static_view_wallet_instance_attestation.svg
   :name: Wallet Solution Schema
   :alt: The image illustrates the containment of Wallet Provider and Wallet Instances within the Wallet Solution, managed by the Wallet Provider.
   :target: https://www.plantuml.com/plantuml/uml/VP8nJyCm48Lt_ugdTexOCw22OCY0GAeGOsMSerWuliY-fEg_9mrEPTAqw-VtNLxEtaJHGRh6AMs40rRlaS8AEgAB533H3-qS2Tu2zxPEWSF8TcrYv-mJzTOGNfzVnXXJ0wKCDorxydAUjMNNYMMVpug9OTrR7i22LlaesXlADPiOraToZWyBsgCsF-JhtFhyGyZJgNlbXVR1oX5R2YSoUdQYEzrQO1seLcfUeGXs_ot5_VzqYM6lQlRXMz6hsTccIbGHhGu2_hhfP1tBwHuZqdOUH6WuEmrKIeqtNonvXhq4ThY3Dc9xBNJv_rSwQeyfawhcZsTPIpKLKuFYSa_JyOPytJNk5m00


Wallet Attestation Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The requirements for the Wallet Attestation are defined below:

- The Wallet Attestation MUST contain a Wallet Instance public key.
- The Wallet Attestation MUST use the signed JSON Web Token (JWT) format;
- The Wallet Attestation MUST provide all the relevant information to attest to the **integrity** and **security** of the device where the Wallet Instance is installed.
- The Wallet Attestation MUST be signed by the Wallet Provider that has authority over and is the owner of the Wallet Solution, as specified by the overseeing registration authority. This ensures that the Wallet Attestation uniquely links the Wallet Provider to this particular Wallet Instance.
- The Wallet Provider MUST ensure the integrity, authenticity, and genuineness of the Wallet Instance, preventing any attempts at manipulation or falsification by unauthorized third parties. The Wallet Provider MUST also verify the Wallet Instance using the App Store vendor's API, such as the *Play Integrity API* for Android and *DeviceCheck* for iOS. These services are defined in this specification as **Device Integrity Service (DIS)**.
- The Wallet Attestation MUST have a mechanism in place for revoking the Wallet Instance, allowing the Wallet Provider to terminate service for a specific instance at any time.
- The Wallet Attestation MUST be securely bound to the Wallet Instance's ephemeral public key.
- The Wallet Attestation MAY be used multiple times during its validity period, allowing for repeated authentication and authorization without the need to request new attestations with each interaction.
- The Wallet Attestation MUST be short-lived and MUST have an expiration date/time, after which it SHOULD no longer be considered valid.
- The Wallet Attestation MUST NOT be issued by the Wallet Provider if the authenticity, integrity, and genuineness are not guaranteed. In this case, the Wallet Instance MUST be revoked.
- Each Wallet Instance SHOULD be able to request multiple attestations with different ephemeral public keys associated with them. This requirement provides a privacy-preserving measure, as the public key MAY be used as a tracking tool during the presentation phase (see also the point listed below).
- The Wallet Attestation MUST NOT contain any information that can be used to directly identify the User.
- The Wallet Instance MUST secure a Wallet Attestation as a prerequisite for transitioning to the Operational state, as defined by `ARF`_.
- Private keys MUST be generated and stored in the WSCD using at least one of the approaches listed below:

  - **Local Internal WSCD**: The WSCD relies entirely on the device's native cryptographic hardware, such as the Secure Enclave on iOS devices or the Hardware-Backed Keystore or Strongbox on Android devices.
  - **Local External WSCD**: The WSCD is hardware external to the User's device, such as a smart card compliant with *GlobalPlatform* and supporting *JavaCard*.
  - **Remote WSCD**: The WSCD utilizes a remote Hardware Security Module (HSM).
  - **Local Hybrid WSCD**: The WSCD involves a pluggable internal hardware component within the User's device, such as an *eUICC* that adheres to *GlobalPlatform* standards and supports *JavaCard*.
  - **Remote Hybrid WSCD**: The WSCD involves a local component mixed with a remote service.

- The Wallet Provider MUST offer a set of services, exclusively available to its Wallet Solution instances, for the issuance of Wallet Attestations.

.. warning::
  At the current stage, the implementation profile defined in this document supports only the **Local Internal WSCD**. Future versions of this specification MAY include other approaches depending on the required `AAL`.


Wallet Attestation Issuance
...................................

This section describes the Wallet Attestation format and how the Wallet Provider issues it.

.. figure:: ../../images/wallet_instance_acquisition.svg
   :name: Sequence Diagram for Wallet Attestation acquisition
   :alt: The figure illustrates the sequence diagram for issuing a Wallet Attestation, with the steps explained below.
   :target: https://www.plantuml.com/plantuml/uml/VLJ1Jjj04BtlLupWK8ZIIwNsWDGAH2bGgWe1BHSaQsmFzZJEhhixTff-VMTD4YV6pS4IoxvvyzxRcPm6GI_Dl3BOYBFDF2LlIiu9dfsJrFqnRse5SCOrMZ46Ct4U3du4yWU00PgW-2q473nYLP70jLLccr67mhg6NTHdQZaZHGaLdcK9z-HRNiDH0Xo6shCj2azaHplSUjUgK0yfPZEoULUQPZDZJ5JrzfDsFO4x-jrG442mj01NaqTXPq5Ab2VhzPOzQKkOJ5QyPo9QqA4casYOMnIA7en-Azhpah8PyBEMdVjbBQxmM9USmHNwV86Uu8QMOJ81LkuMkSAq8hD5S4asIecjBL1TqboF5Sne2JMoLzwlZpVQttZhXC2rvAE4gHg4ms_NbrSFbtSN5z_DYv1X9DerHWRkMOqIVA5yxHjj3YuLP0ii0UOacAEWqG2xJcObKlj4aQ92iZAosuAsuuX1wzS1UpVWB87mdE9W34eZUcL-zoAd7LOp5bCigPYi955jKc8eDLmCS7zrzkxzXwCDtnJg9gquItujPiVZJ7jUJ3bltUsJFdov-cyIkB0eZIUz-mZnT3HKCeL5bt-oAT9dJ0IBZG2KS0B5Ii5cwCz282_iNZCUcrZInyNhaWJNDIfdrDxhATxim8Ab_1_P5COzJtSVQ_faz-K73rYyrFIle48Z7-LT_txMDoFUpzizsNoFWTtfwnSZ7iSN8sxeu0SfxWPR5iQA_rBUBKIhV-Uc2MmBs6DEiEZWuqdrAzJlnSz8Z39OXH70-BECGyVRZoDZmjrCzzVga5ukNoSzMDDnn61VjyzQPaurXsPU_GC0

**Step 1**: The User initiates a new operation that necessitates the acquisition of a Wallet Attestation.

**Steps 2-3**: The Wallet Instance MUST:

  1. Verify the existence of Cryptographic Hardware Keys. If none exist, Wallet Instance re-initialization is required.
  2. Generate an ephemeral asymmetric key pair for Wallet Attestation, linking the public key to the attestation.
  3. Verify the Wallet Provider's federation membership and retrieve its metadata.


**Steps 4-6**: The Wallet Instance solicits a one-time "challenge" from the `nonce endpoint`_ of the Wallet Provider Backend. This "challenge" takes the form of a ``nonce``, which is required to be unpredictable and serves as the main defense against replay attacks. 
The ``nonce`` MUST be produced in a manner that ensures its single-use within a predetermined time frame.

.. code-block:: http

    GET /nonce HTTP/1.1
    Host: walletprovider.example.com

.. code-block:: http

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
      "nonce": "d2JhY2NhbG91cmVqdWFuZGFt"
    }


If an error occurs during ``nonce`` generation, the Wallet Provider MUST return an error response.


**Step 7**: The Wallet Instance performs the following actions:

  * Creates ``client_data``, a JSON object that includes the challenge and the thumbprint of ephemeral public ``jwk``.
  * Computes ``client_data_hash`` by applying the ``SHA256`` algorithm to the ``client_data``.

Below is a non-normative example of the ``client_data`` JSON object.

.. code-block:: json

  {
    "challenge": "0fe3cbe0-646d-44b5-8808-917dd5391bd9",
    "jwk_thumbprint": "vbeXJksM45xphtANnCiG6mCyuU4jfGNzopGuKvogg9c"
  }

**Steps 8-10**: The Wallet Instance:

  *  produces an ``hardware_signature`` value by signing the ``client_data_hash`` with the Wallet Hardware's private key, serving as a proof of possession for the Cryptographic Hardware Keys.
  *  requests the Device Integrity Service to create an ``integrity_assertion`` value linked to the ``client_data_hash``.
  *  receives a signed ``integrity_assertion`` value from the Device Integrity Service, authenticated by the OEM.

.. note:: ``integrity_assertion`` is a custom payload generated by Device Integrity Service, signed by device OEM and encoded in base64 to have uniformity between different devices.

**Steps 11-12**: The Wallet Instance:

  * Constructs the Wallet Attestation Request in the form of a JWT. This JWT includes the ``integrity_assertion``, ``hardware_signature``, ``challenge``, ``hardware_key_tag``, ``cnf`` and other configuration related parameters (see :ref:`Table of the Wallet Attestation Request Body <table_wallet_attestation_request_claim>` below) and is signed using the private key of the initially generated ephemeral key pair.
  * Submits the Wallet Attestation Request to the `wallet-attestation endpoint`_ of the Wallet Provider Backend.

Below is a non-normative example of the Wallet Attestation Request JWT without encoding and signature applied:

.. code-block::

  {
    "alg": "ES256",
    "kid": "vbeXJksM45xphtANnCiG6mCyuU4jfGNzopGuKvogg9c",
    "typ": "war+jwt"
  }
  .
  {
    "iss": "https://wallet-provider.example.org/instance/vbeXJksM45xphtANnCiG6mCyuU4jfGNzopGuKvogg9c",
    "sub": "https://wallet-provider.example.org/",
    "challenge": "6ec69324-60a8-4e5b-a697-a766d85790ea",
    "hardware_signature": "KoZIhvcNAQcCoIAwgAIB...redacted",
    "integrity_assertion": "o2NmbXRvYXBwbGUtYXBwYX...redacted",
    "hardware_key_tag": "WQhyDymFKsP95iFqpzdEDWW4l7aVna2Fn4JCeWHYtbU=",
    "cnf": {
      "jwk": {
        "crv": "P-256",
        "kty": "EC",
        "x": "4HNptI-xr2pjyRJKGMnz4WmdnQD_uJSq4R95Nj98b44",
        "y": "LIZnSB39vFJhYgS3k7jXE4r3-CoGFQwZtPBIRqpNlrg"
      }
    },
    "vp_formats_supported": {
        "jwt_vc_json": {
          "alg_values_supported": ["ES256K", "ES384"]
        },
        "jwt_vp_json": {
          "alg_values_supported": ["ES256K", "EdDSA"]
        },
      },
    },
    authorization_endpoint": "https://wallet-solution.digital-strategy.europa.eu/authorization",
    "response_types_supported": [
      "vp_token"
    ],
    "response_modes_supported": [
      "form_post.jwt"
    ],
    "request_object_signing_alg_values_supported": [
      "ES256"
    ],
    "iat": 1686645115,
    "exp": 1686652315
  }

The Wallet Instance MUST send an HTTP request to the Wallet Provider's `wallet-attestation endpoint`_, using the `POST` method with ``Content-Type`` ``application/json``. The request body MUST contain an ``assertion`` parameter whose value is the signed JWT of the Wallet Attestation Request.

.. code-block:: http

    POST /wallet-attestation HTTP/1.1
    Host: wallet-provider.example.org
    Content-Type: application/json

    {
      "assertion": "eyJhbGciOiJFUzI1NiIsImtpZCI6ImtoakZWTE9nRjNHeG..."
    }

**Steps 13-17**: The Wallet Provider Backend evaluates the Wallet Attestation Request and MUST perform the following checks:

    1. The request MUST include all required HTTP header parameters as defined in :ref:`Table of the Wallet Attestation Request Header <table_wallet_attestation_request_claim>`.
    2. The signature of the Wallet Attestation Request MUST be valid and verifiable using the provided ``jwk``.
    3. The ``challenge`` value MUST have been generated by the Wallet Provider and not previously used.
    4. A valid and currently registered Wallet Instance associated with the provided MUST exist.
    5. The ``client_data`` MUST be reconstructed using the ``challenge`` and the ``jwk`` public key.  The ``hardware_signature`` parameter value is then validated using the registered Cryptographic Hardware Key's public key associated with the Wallet Instance.
    6. The ``integrity_assertion`` MUST be validated according to the device manufacturer's guidelines.  The specific checks performed by the Wallet Provider are detailed in the operating system manufacturer's documentation.
    7. The device in use MUST be free of known security flaws and meet the minimum security requirements defined by the Wallet Provider.
    8. The URL in the ``iss`` parameter MUST match the Wallet Provider's URL identifier.

Upon successful completion of all checks, the Wallet Provider issues a Wallet Attestation valid for a maximum of 24 hours.

Below is a non-normative example of the Wallet Attestation without encoding and signature applied:

.. code-block::

    {
    "alg": "ES256",
    "kid": "5t5YYpBhN-EgIEEI5iUzr6r0MR02LnVQ0OmekmNKcjY",
    "trust_chain": [
      "eyJhbGciOiJFUz...6S0A",
      "eyJhbGciOiJFUz...jJLA",
      "eyJhbGciOiJFUz...H9gw",
    ],
    "typ": "wallet-attestation+jwt",
  }
  .
  {
    "iss": "https://wallet-provider.example.org",
    "sub": "vbeXJksM45xphtANnCiG6mCyuU4jfGNzopGuKvogg9c",
    "aal": "https://trust-list.eu/aal/high",
    "cnf":
    {
      "jwk":
      {
        "crv": "P-256",
        "kty": "EC",
        "x": "4HNptI-xr2pjyRJKGMnz4WmdnQD_uJSq4R95Nj98b44",
        "y": "LIZnSB39vFJhYgS3k7jXE4r3-CoGFQwZtPBIRqpNlrg"
      }
    },
    "authorization_endpoint": "https://wallet-solution.digital-strategy.europa.eu/authorization",
    "response_types_supported": [
      "vp_token"
    ],
    "response_modes_supported": [
      "form_post.jwt"
    ],
    "vp_formats_supported": {
        "dc+sd-jwt": {
            "sd-jwt_alg_values": [
                "ES256",
                "ES384"
            ]
        }
    },
    "request_object_signing_alg_values_supported": [
      "ES256"
    ],
    "iat": 1687281195,
    "exp": 1687288395
  }

**Step 18**: Upon successful completion, the Wallet Provider MUST return an HTTP response with a status code of ``200 OK``, containing the Wallet Attestation signed by the Wallet Provider. The Wallet Instance will then perform security, integrity, and trust verification of the Wallet Attestation and its issuer.


Below is a non-normative example of the response.

.. code-block:: http

    HTTP/1.1 200 OK
    Content-Type: application/jwt

    eyJhbGciOiJFUzI1NiIsInR5cCI6IndhbGx ...


.. _table_wallet_attestation_request_claim:

If any errors occur during the Wallet Attestation Request Verification, the Wallet Provider MUST return an error response as defined in :rfc:`7231` (additional details available in :rfc:`7807`). The response MUST use the content type set to *application/json* and MUST include the following parameters:

  - *error*. The error code.
  - *error_description*. Text in human-readable form providing further details to clarify the nature of the error encountered.

Below is a non-normative example of an error response:

.. code:: http

   HTTP/1.1 403 Forbidden
   Content-Type: application/json
   Cache-Control: no-store

.. code:: json

   {
     "error": "integrity_check_error",
     "error_description": "The device does not meet the Wallet Provider’s minimum security requirements."
   }

The following table lists HTTP Status Codes and related error codes that MUST be supported for the error response, unless otherwise specified:

.. list-table::
   :widths: 30 20 50
   :header-rows: 1

   * - **HTTP Status Code**
     - **Error Code**
     - **Description**
   * - ``400 Bad Request`` 
     - ``bad_request``
     - The request is malformed, missing required parameters (e.g., header parameters or integrity assertion), or includes invalid and unknown parameters.
   * - ``403 Forbidden`` 
     - ``invalid_request``
     - The wallet instance was revoked.
   * - ``403 Forbidden`` 
     - ``integrity_check_error``
     - The device does not meet the Wallet Provider’s minimum security requirements.
   * - ``403 Forbidden`` 
     - ``invalid_request``
     - The signature of the Wallet Attestation Request is invalid or does not match the associated public key (JWK).
   * - ``403 Forbidden`` 
     - ``invalid_request``
     - The integrity assertion validation failed; the integrity assertion is tampered with or improperly signed.
   * - ``403 Forbidden`` 
     - ``invalid_request``
     - The provided challenge is invalid, expired, or already used.
   * - ``403 Forbidden`` 
     - ``invalid_request``
     - The Proof of Possession (``hardware_signature``) is invalid.
   * - ``403 Forbidden`` 
     - ``invalid_request``
     - The ``iss`` parameter does not match the Wallet Provider’s expected URL identifier.
   * - ``404 Not Found`` 
     - ``not_found``
     - The Wallet Instance was not found.
   * - ``422 Unprocessable Content`` [OPTIONAL]
     - ``validation_error``
     - The request does not adhere to the required format.
   * - ``500 Internal Server Error`` 
     - ``server_error``
     - An internal server error occurred while processing the request.
   * - ``503 Service Unavailable`` 
     - ``temporarily_unavailable``
     - Service unavailable. Please try again later.

Wallet Attestation Request
...................................

The JOSE header of the Wallet Attestation Request JWT MUST contain the following parameters:

.. list-table::
    :widths: 20 60 20
    :header-rows: 1

    * - **JOSE header**
      - **Description**
      - **Reference**
    * - **alg**
      - A digital signature algorithm identifier such as per IANA "JSON Web Signature and Encryption Algorithms" registry. It MUST be one of the supported algorithms listed in the Section `Cryptographic Algorithms <algorithms.html>`_ and MUST NOT be set to ``none`` or any symmetric algorithm (MAC) identifier.
      - :rfc:`7516#section-4.1.1`.
    * - **kid**
      -  Unique identifier of the ``jwk`` used by the Wallet Provider to sign the Wallet Attestation, essential for matching the Wallet Provider's cryptographic public key needed for signature verification.
      - :rfc:`7638#section_3`.
    * - **typ**
      -  It MUST be set to ``var+jwt``
      -

The body of the Wallet Attestation Request JWT MUST contain the following parameters:

.. list-table::
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Description**
      - **Reference**
    * - **iss**
      - Identifier of the Wallet Provider concatenated with thumbprint of the JWK in the ``cnf`` parameter.
      - :rfc:`9126` and :rfc:`7519`.
    * - **aud**
      - It MUST be set to the identifier of the Wallet Provider.
      - :rfc:`9126` and :rfc:`7519`.
    * - **exp**
      - UNIX Timestamp with the expiry time of the JWT.
      - :rfc:`9126` and :rfc:`7519`.
    * - **iat**
      - REQUIRED. UNIX Timestamp with the time of JWT issuance.
      - :rfc:`9126` and :rfc:`7519`.
    * - **challenge**
      - Challenge data obtained from ``nonce`` endpoint
      -
    * - **hardware_signature**
      - The signature of ``client_data`` obtained using Cryptographic Hardware Key base64 encoded.
      -
    * - **integrity_assertion**
      - The integrity assertion obtained from the **Device Integrity Service** with the holder binding of ``client_data``.
      -
    * - **hardware_key_tag**
      - Unique identifier of the **Cryptographic Hardware Keys**
      -
    * - **cnf**
      - JSON object, containing the public part of an asymmetric key pair owned by the Wallet Instance.
      - :rfc:`7800`
    * - **vp_formats_supported**
      - JSON object with name/value pairs, identifying a Credential format supported by the Wallet.
      -
    * - **authorization_endpoint**
      - URL of the Wallet Authorization Endpoint, it can be a universal link or a custom url-scheme.
      -
    * - **response_types_supported**
      - JSON array containing a list of the OAuth 2.0 ``response_type`` values.
      -
    * - **response_modes_supported**
      - JSON array containing a list of the OAuth 2.0 "response_mode" values that this authorization server supports.
      - :rfc:`8414`
    * - **request_object_signing_alg_values_supported**
      - JSON array containing a list of the signing algorithms (alg values) supported.
      -

.. _table_wallet_attestation_claim:

Wallet Attestation JWT
...................................

The JOSE header of the Wallet Attestation JWT MUST contain the following parameters:

.. list-table::
    :widths: 20 60 20
    :header-rows: 1

    * - **JOSE header**
      - **Description**
      - **Reference**
    * - **alg**
      - A digital signature algorithm identifier such as per IANA "JSON Web Signature and Encryption Algorithms" registry. It MUST be one of the supported algorithms listed in the Section `Cryptographic Algorithms <algorithms.html>`_ and MUST NOT be set to ``none`` or any symmetric algorithm (MAC) identifier.
      - :rfc:`7516#section-4.1.1`.
    * - **kid**
      -  Unique identifier of the ``jwk`` inside the ``cnf`` claim of Wallet Instance as base64url-encoded JWK Thumbprint value.
      - :rfc:`7638#section_3`.
    * - **typ**
      -  It MUST be set to ``wallet-attestation+jwt``
      -  `OPENID4VC-HAIP`_
    * - **trust_chain**
      - Sequence of Entity Statements that composes the Trust Chain related to the Relying Party.
      - `OID-FED`_ Section 4.3 *Trust Chain Header Parameter*.

The body of the Wallet Attestation JWT MUST contain the following parameters:

.. list-table::
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Description**
      - **Reference**
    * - **iss**
      - Identifier of the Wallet Provider
      - :rfc:`9126` and :rfc:`7519`.
    * - **sub**
      - Identifier of the Wallet Instance which is the thumbprint of the Wallet Instance JWK contained in the ``cnf`` claim.
      - :rfc:`9126` and :rfc:`7519`.
    * - **exp**
      - UNIX Timestamp with the expiry time of the JWT.
      - :rfc:`9126` and :rfc:`7519`.
    * - **iat**
      - UNIX Timestamp with the time of JWT issuance.
      - :rfc:`9126` and :rfc:`7519`.
    * - **cnf**
      - JSON object, containing the public part of an asymmetric key pair owned by the Wallet Instance.
      - :rfc:`7800`
    * - **aal**
      - JSON String asserting the authentication level of the Wallet and the key as asserted in the cnf claim.
      -
    * - **authorization_endpoint**
      - URL of the Wallet Authorization Endpoint, it can be a universal link or a custom url-scheme.
      -
    * - **response_types_supported**
      - JSON array containing a list of the OAuth 2.0 ``response_type`` values.
      -
    * - **response_modes_supported**
      - JSON array containing a list of the OAuth 2.0 "response_mode" values that this authorization server supports.
      - :rfc:`8414`
    * - **vp_formats_supported**
      - JSON object with name/value pairs, identifying a Credential format supported by the Wallet.
      -
    * - **request_object_signing_alg_values_supported**
      - JSON array containing a list of the signing algorithms (alg values) supported.
      -
    * - **client_id_schemes_supported**
      - Array of JSON Strings containing the values of the Client Identifier schemes that the Wallet supports.
      - `OpenID4VP`_

.. _wallet-instance endpoint: wallet-solution.html#wallet-provider-endpoints
.. _nonce endpoint: wallet-solution.html#wallet-provider-endpoints
.. _wallet-attestation endpoint: wallet-solution.html#wallet-provider-endpoints
.. _Wallet Attestation Request: wallet-attestation.html#format-of-the-wallet-attestation-request
.. _Wallet Attestation: wallet-attestation.html#format-of-the-wallet-attestation
.. _RFC 7523 section 4: https://www.rfc-editor.org/rfc/rfc7523.html#section-4
.. _RFC 8414 section 2: https://www.rfc-editor.org/rfc/rfc8414.html#section-2
.. _Wallet Provider metadata: wallet-solution.html#wallet-provider-metadata
.. _Play Integrity API: https://developer.android.com/google/play/integrity?hl=it
.. _DeviceCheck: https://developer.apple.com/documentation/devicecheck
.. _OAuth 2.0 Nonce Endpoint: https://datatracker.ietf.org/doc/draft-demarco-oauth-nonce-endpoint/
.. _ARF: https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework
.. _Play Integrity API Errors: https://developer.android.com/google/play/integrity/error-codes
.. _TEE Client API Errors: https://globalplatform.org/wp-content/uploads/2010/07/TEE_Client_API_Specification-V1.0.pdf



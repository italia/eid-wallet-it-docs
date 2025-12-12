.. include:: ../common/common_definitions.rst

.. "included" file, so we start with '-' title level

.. role:: raw-html(raw)
  :format: html


Wallet Provider Endpoints
-------------------------

The Wallet Provider, responsible for delivering a Wallet Solution, MUST expose the endpoints to support trust establishment and essential Wallet Instance functionalities. These include the ``/.well-known/openid-federation`` Federation Endpoint which MUST adhere to the OpenID Federation 1.0 specification to reliably establish trust with the Wallet Provider's as well as, endpoints for Wallet Instance registration, nonce generation (required for registration), attestation issuance, and revocation. Aside from the Federation endpoint, the implementation details of the others are left to the Wallet Provider's discretion.

.. note::
  Tests related to the use of Wallet Provider endpoints are defined in 
  :ref:`wallet-provider-test-matrix`, particularly 
  :ref:`wallet-provider-backend-testcases`,
  :ref:`wallet-instance-testcases`, and 
  :ref:`wallet-instance-optional-testcases`.

Federation Endpoint
^^^^^^^^^^^^^^^^^^^

The ``/.well-known/openid-federation`` endpoint serves as the discovery mechanism for trust establishment by retrieving the Wallet Provider Entity Configuration.

See Section :ref:`wallet-provider-entity-configuration:Wallet Provider Entity Configuration` for technical details (:ref:`WP_001–004 <wallet-provider-backend-testcases>`).


Wallet Solution Nonce Endpoint
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is a RESTful API endpoint that allows the Wallet Instance to request a cryptographic nonce from the Wallet Provider. The nonce serves as an unpredictable, single-use challenge to ensure freshness and prevent replay attacks.

See :ref:`mobile-application-instance:Mobile Application Nonce Request` and :ref:`mobile-application-instance:Mobile Application Nonce Response` for details on the Nonce Request and Nonce Response (:ref:`WP_131 <wallet-instance-optional-testcases>`).

Wallet Instance Management Endpoint
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

These are RESTful API endpoints provided by the Wallet Provider that enables Wallet Instance management, including registration, status retrieval, revocation upon request (e.g., by the User), and deletion.
The following sections describe the registration, status retrieval and revocation requests, along with their corresponding responses, handled by this endpoint, which are required for core :ref:`wallet-instance-functionalities:Wallet Instance Functionalities`.

Wallet Instance Registration Request
"""""""""""""""""""""""""""""""""""""

To register a Wallet Instance, the request to the Wallet Provider MUST use the HTTP POST method with ``Content-Type`` set to `application/json`. The request body MUST contain the claims described in :ref:`mobile-application-instance:Mobile Application Instance Initialization Request` (:ref:`WP_131–134 <wallet-instance-optional-testcases>`).

Wallet Instance Registration Response
"""""""""""""""""""""""""""""""""""""""""

If a Wallet Instance Registration Request is successfully validated, the Wallet Provider provides an HTTP Response with status code 204 (No Content). For detatails see :ref:`mobile-application-instance:Mobile Application Instance Initialization Response` (:ref:`WP_135–137 <wallet-instance-optional-testcases>`).

Wallet Instance Retrieval Request
"""""""""""""""""""""""""""""""""""

To retrieve all Wallet Instances associated with a User, a request MUST be sent using the HTTP GET method to the Wallet Provider (:ref:`WP_145 <wallet-instance-optional-testcases>`).

.. note::
  For retrieving a specific Wallet Instance, the request MUST include the Wallet Instance ID as a path parameter.


Wallet Instance Retrieval Response
"""""""""""""""""""""""""""""""""""

If a Wallet Instance Retrieval Request is successfully processed, the Wallet Provider MUST return an HTTP Response with a 200 (OK) status code.
The response body MUST be in JSON format and include the relevant Wallet Instance information, such as its unique ID, status, and issuance date.
When retrieving all Wallet Instances, the response MUST return an array containing the details of all associated instances (:ref:`WP_146 <wallet-instance-optional-testcases>`).

If any errors occur during the retrieval process, an error response MUST be returned. Refer to :ref:`wallet-provider-endpoint:Error Handling for Wallet Instance Management` for details on error codes and descriptions.

Below is a non-normative example of an error response:

.. code-block:: http

   HTTP/1.1 403 Forbidden
   Content-Type: application/json
   Cache-Control: no-store

   {
     "error": "forbidden",
     "error_description": "User is not authorized to retrieve Wallet Instances."
   }


Wallet Instance Revocation Request
""""""""""""""""""""""""""""""""""

To revoke an active Wallet Instance, a revocation request MUST be sent using the HTTP PATCH method with Content-Type set to ``application/json``. The request body MUST contain a ``status`` parameter set to ``REVOKED`` (:ref:`WP_147 <wallet-instance-optional-testcases>`).

.. note::
  While PATCH is the recommended method, the revocation request MAY also be sent using the POST method, depending on implementation preferences.

Wallet Instance Revocation Response
"""""""""""""""""""""""""""""""""""

If a Wallet Instance Revocation Request is successfully processed, the Wallet Provider provides an HTTP Response with a 204 (No Content) status code (:ref:`WP_148 <wallet-instance-optional-testcases>`).

If any errors occur during the Wallet Instance Revocation, an error response MUST be returned. Refer to :ref:`wallet-provider-endpoint:Error Handling for Wallet Instance Management` for details on error codes and descriptions (:ref:`WP_035–039, WP_043–044 <wallet-instance-testcases>`).

Below is a non-normative example of an error response:

.. code-block:: http

   HTTP/1.1 400 Bad Request
   Content-Type: application/json
   Cache-Control: no-store

   {
     "error": "bad_request",
     "error_description": "The request is missing status parameter."
   }

Error Handling for Wallet Instance Management
"""""""""""""""""""""""""""""""""""""""""""""""

To ensure robustness and security, the Wallet Provider MUST handle errors consistently across all Wallet Instance Management requests, including Registration, Retrieval, and Revocation.

In case of an error, the Wallet Provider MUST return an error response as defined in :rfc:`7231`, with additional details available in :rfc:`7807`. The response MUST use the Content-Type set to ``application/json`` and MUST include the following parameters:

- *error*. The error code.
- *error_description*. Text in human-readable form providing further details to clarify the nature of the error encountered.
 
The following sections categorize errors into **common errors**, which apply to all requests, and **request-specific errors**, which are relevant to particular operations (:ref:`WP_035–044 <wallet-instance-testcases>`, and :ref:`WP_150–155 <wallet-instance-optional-testcases>`).

Common Error Responses
"""""""""""""""""""""""

The following errors apply to all Wallet Instance Management operations (Registration, Retrieval, and Revocation), and MUST be supported for the error response, unless otherwise specified (:ref:`WP_035–039 <wallet-instance-testcases>`):

.. list-table::
   :class: longtable
   :widths: 20 20 50
   :header-rows: 1

   * - **HTTP Status Code**
     - **Error Code**
     - **Description**
   * - ``400 Bad Request``
     - ``bad_request``
     - The request is malformed, missing required parameters, or includes invalid and unknown parameters.
   * - ``422 Unprocessable Content`` [OPTIONAL]
     - ``validation_error``
     - The request does not adhere to the required format.
   * - ``500 Internal Server Error``
     - ``server_error``
     - An internal error occurred while processing the request.
   * - ``503 Service Unavailable``
     - ``temporarily_unavailable``
     - The service is unavailable. Please try again later.

Request-Specific Error Responses
"""""""""""""""""""""""""""""""""

The errors in :ref:`mobile-application-instance:Mobile Application Instance Initialization Error Response` MUST be supported for error responses related to **Wallet Instance Registration**.

The following errors MUST be supported for error responses related to **Wallet Instance Retrieval** (:ref:`WP_041–042 <wallet-instance-testcases>`):

.. list-table::
   :class: longtable
   :widths: 20 20 50
   :header-rows: 1

   * - **HTTP Status Code**
     - **Error Code**
     - **Description**
   * - ``403 Forbidden``
     - ``forbidden``
     - The user does not have permission to retrieve this Wallet Instance.
   * - ``401 Unauthorized``
     - ``unauthorized``
     - The request lacks valid authentication credentials.

The following errors MUST be supported for error responses related to **Wallet Instance Revocation** (:ref:`WP_043–044 <wallet-instance-testcases>`):

.. list-table::
   :class: longtable
   :widths: 20 20 50
   :header-rows: 1

   * - **HTTP Status Code**
     - **Error Code**
     - **Description**
   * - ``403 Forbidden``
     - ``invalid_request``
     - The user does not have permission to revoke this Wallet Instance.
   * - ``401 Unauthorized``
     - ``unauthorized``
     - The request cannot be authenticated or authorized.

Wallet App and Wallet Unit Attestation Issuance Endpoint
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is a RESTful API endpoint provided by the Wallet Provider that enables the Wallet Instance to obtain Wallet App and Wallet Unit Attestation, by sending a Wallet App and Wallet Unit Attestation Issuance Request.

Wallet App and Wallet Unit Attestation Issuance Request
"""""""""""""""""""""""""""""""""""""""""""""""""""""""

The Wallet App and Wallet Unit Attestation Issuance Request uses the HTTP POST method with ``Content-Type`` set to ``application/json``. (:ref:`WP_026 <wallet-instance-testcases>` and :ref:`WP_140–142 <wallet-instance-optional-testcases>`).

The ``typ`` header of the Wallet App and Wallet Unit Attestation Issuance Request JWT assumes the value ``attestations-request+jwt``.

The Wallet App and Wallet Unit Attestation Issuance Request body contains an ``assertion`` parameter whose value is a signed JWT including all header parameters and body claims described below.

Below is a non-normative example of a Wallet App and Wallet Unit Attestation Request.

.. code-block:: http

    POST /wallet-attestation HTTP/1.1
    Host: application-provider.example.org
    Content-Type: application/json

    {
      "assertion": "eyJpc3MiOiJodHRwczovL3dhbGxldC1wcm92aWRlc..."
    }

In particular, the Wallet App and Wallet Unit Attestation Issuance JWT includes the following HTTP header parameters:

.. _table_waa_wua_request_claim:
.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Parameter**
      - **Description**
      - **Reference**
    * - **alg**
      - A digital signature algorithm identifier such as per IANA "JSON Web Signature and Encryption Algorithms" registry. It MUST be one of the supported algorithms listed in the :ref:`algorithms:cryptographic algorithms` and MUST NOT be set to ``none`` or any symmetric algorithm (MAC) identifier.
      - [:rfc:`7516#section-4.1.1`]
    * - **kid**
      - Thumbprint of the Wallet Instance's JWK contained in the ``cnf`` claim.
      - [:rfc:`7638#section_3`]
    * - **typ**
      - The type of the JWT, it MUST set to ``attestations-request+jwt``.
      -

The Wallet App and Wallet Unit Attestation Request JWT includes the following body claims:

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Description**
      - **Reference**
    * - **iss**
      - The identifier of the Wallet Provider concatenated with the thumbprint of the JWK in the ``cnf`` claim.
      - [:rfc:`9126`], [:rfc:`7519`].
    * - **aud**
      - The identifier of the Wallet Provider.
      - [:rfc:`9126`], [:rfc:`7519`].
    * - **exp**
      - UNIX timestamp representing the JWT expiration time.
      - [:rfc:`9126`], [:rfc:`7519`].
    * - **iat**
      - UNIX timestamp representing the JWT issuance time.
      - [:rfc:`9126`], [:rfc:`7519`].
    * - **nonce**
      - The ``nonce`` obtained from the Nonce Endpoint.
      -
    * - **hardware_signature**
      - The signature of ``client_data_hash_waa`` and ``client_data_hash_wua`` obtained using the Cryptographic Hardware Key, encoded in the ``base64url`` format.
      -
    * - **integrity_assertion**
      - The Integrity Assertion for Wallet App Attestation obtained from the **Device Integrity Service APIs** with the holder binding of ``client_data_hash_waa``.
      -
    * - **attested_key**
      - The key Attestation obtained for the credential key either from the **Key Attestation APIs** with the holder binding of ``client_data_hash_wua`` or from the **Device Integrity Service APIs** with the holder binding of ``client_data_hash_wua``.
      -
    * - **hardware_key_tag**
      - The value of the Cryptographic Hardware Key Tag.
      -
    * - **cnf**
      - JSON object containing the public part of an asymmetric key pair owned by the Wallet Instance.
      - :rfc:`7800`.

Below is a non-normative example of a Wallet App and Wallet Unit Attestation Request JWT header and payload.


.. code-block:: json

    {
      "alg": "ES256",
      "kid": "OnsiandrIjp7ImNydiI6IlAtMjU2Iiwia3R5IjoiRUMiL",
      "typ": "attestations-request+jwt"
    }

.. code-block:: json
  
    {
      "iss": "https://wallet-provider.example.org/instance/OnsiandrIjp7ImNydiI6IlAtMjU2Iiwia3R5IjoiRUMiL",
      "sub": "https://wallet-provider.example.org/",
      "nonce": "f3b29a81-45c7-4d12-b8b5-e1f6c9327aef",
      "hardware_signature": "KoZIhvcNAQcCoIAwgAIB...",
      "integrity_assertion": "o2NmbXRvYXBwbGUtYXBwYXNzZXJ0aW9uLXBheWxvYWQtYXBw...",
      "attested_key": "o2CFbXRvYXBwbGUtYXBwYXNzTYU0aW9uLXBheWxvYWQtZvRM..."
      "hardware_key_tag": "QW12DylRTmF89iGkpydNDWW7m8bVpa2Fn9KBeXGYtfX"
      "cnf": {
        "jwk": {
          "crv": "P-256",
          "kty": "EC",
          "x": "8FJtI-yr3pjyRKGMnz4WmdnQD_uJSq4R95Nj98b44",
          "y": "MKZnSB39vFJhYgS3k7jXE4r3-CoGFQwZtPBIRqpNlrg"
        }
      }
    }


Wallet App and Wallet Unit Attestation Issuance Response
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

If the Wallet App and Wallet Unit Attestation Issuance Request is successfully validated, the Wallet Provider returns an HTTP response with a status code of ``200 OK`` and ``Content-Type`` ``application/json``. The returned JSON Object MUST possess the ``wallet_attestations`` parameter, which includes ``wallet_app_attestation`` and ``wallet_unit_attestation`` elements (see :ref:`wallet-attestation-issuance:Wallet App and Wallet Unit Attestation Issuance`). ``wallet_app_attestation`` and ``wallet_unit_attestation`` are single JSON objects containing the Wallet App Attestation and the Wallet Unit Attestation, respectively. Both attestations are signed by the Wallet Provider (:ref:`WP_027–029 <wallet-instance-testcases>` and :ref:`WP_143–144 <wallet-instance-optional-testcases>`). The JWT formatted Wallet App Attestation is to be used for the Issuance phase, as an OAuth Client Attestation, and will be sent to the Credential Issuer as discussed in :ref:`credential-issuance:Digital Credential Issuance`. The JWT formatted Wallet Unit Attestation is to be used for the Issuance phase, as an ``key_attestation`` JOSE header in the JWT ``proof`` type, and will be sent to the Credential Issuer as discussed in :ref:`credential-issuance:Digital Credential Issuance`.


The JSON Object returned in the response has the following claim:

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Parameter**
      - **Description**
      - **Reference**
    * - **wallet_attestations**
      - REQUIRED. A JSON array containing one Wallet App Attestation and one Wallet Unit Attestation in ``wallet_app_attestation`` and ``wallet_unit_attestation`` elements, respectively. It MUST contain the following mandatory claims:


        - **wallet_app_attestation**: A JSON object containing of the issued Wallet App Attestation.
        - **wallet_unit_attestation**: A JSON object containing of the issued Wallet Unit Attestation.
      - This specification.

The value of ``wallet_app_attestation`` and ``wallet_unit_attestation`` parameters are strings representing the Wallet App Attestation and Wallet Unit Attestation in a JWT, respectively. 

If any errors occur during the process, an error response is returned. The response uses ``application/json`` as the ``Content-Type`` and includes the following parameters:

  - *error*. The error code.
  - *error_description*. Text in human-readable form providing further details to clarify the nature of the error encountered (:ref:`WP_035 <wallet-instance-testcases>`).

Below is a non-normative example of a Wallet App and Wallet Unit Attestation Issuance Response.

.. code-block:: http

    HTTP/1.1 403 Forbidden
    Content-Type: application/json

    {
      "error": "invalid_request",
      "error_description": "The provided challenge is invalid, expired, or already used."
    }

The following table lists HTTP Status Codes and related error codes that are supported for the error response, unless otherwise specified  (:ref:`WP_036–039 <wallet-instance-testcases>` and :ref:`WP_150–155 <wallet-instance-optional-testcases>`):

.. list-table::
    :class: longtable
    :widths: 30 20 50
    :header-rows: 1

    * - **HTTP Status Code**
      - **Error Code**
      - **Description**
    * - ``400 Bad Request``
      - ``bad_request``
      - The request is malformed, missing required parameters (e.g., header parameters, Integrity Assertion, or ``attested_key``), or includes invalid and unknown parameters.
    * - ``403 Forbidden``
      - ``invalid_request``
      - The Wallet Instance has been revoked.
    * - ``403 Forbidden``
      - ``integrity_check_error``
      - The device does not meet the Wallet Provider's minimum security requirements.
    * - ``403 Forbidden``
      - ``invalid_request``
      - The signature of the Wallet App and Wallet Unit Attestation Request is invalid or does not match the associated public key (JWK).
    * - ``403 Forbidden``
      - ``invalid_request``
      - The Integrity Assertion or Key Attestation (``attested_key``) validation failed; the Integrity Assertion or Key Attestation (``attested_key``) is tampered with or improperly signed.
    * - ``403 Forbidden``
      - ``invalid_request``
      - The provided ``nonce`` is invalid, expired, or already used.
    * - ``403 Forbidden``
      - ``invalid_request``
      - The Proof of Possession (``hardware_signature``) is invalid.
    * - ``403 Forbidden``
      - ``invalid_request``
      - The ``iss`` parameter does not match the Wallet Provider's expected URL identifier.
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
      - The service is unavailable. Please try again later.



Wallet App Attestation JWT
"""""""""""""""""""""""""""

The JOSE header of the Wallet App Attestation JWT contains the following parameters:

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **JOSE header**
      - **Description**
      - **Reference**
    * - **alg**
      - REQUIRED. A digital signature algorithm identifier such as per IANA "JSON Web Signature and Encryption Algorithms" registry. It MUST be one of the supported algorithms listed in the Section :ref:`algorithms:cryptographic algorithms` and MUST NOT be set to ``none`` or any symmetric algorithm (MAC) identifier.
      - :rfc:`7516#section-4.1.1`.
    * - **kid**
      - REQUIRED. Unique identifier of the public key associated to the private key the Wallet Provider used to sign the Wallet App Attestation.
      - :rfc:`7638#section_3`.
    * - **typ**
      - REQUIRED. It MUST be set to ``oauth-client-attestation+jwt``
      - `OPENID4VC-HAIP`_.
    * - **trust_chain**
      - OPTIONAL. Sequence of Entity Statements that composes the Trust Chain related to the Wallet Provider.
      - `OID-FED`_ Section 4.3 *Trust Chain Header Parameter*.
    * - **x5c**
      - REQUIRED. Contains the X.509 public key certificate or certificate chain (:rfc:`5280`) corresponding to the key used to digitally sign the JWT.
      - :rfc:`7515` Section 4.1.8, `SD-JWT-VC`_ Section 3.5 and `OPENID4VC-HAIP`_.

The body of the Wallet App Attestation JWT contains the following claims:

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Description**
      - **Reference**
    * - **iss**
      - REQUIRED. Identifier of the Wallet Provider.
      - :rfc:`9126` and :rfc:`7519`.
    * - **exp**
      - REQUIRED. UNIX Timestamp with the expiry time of the JWT.
      - :rfc:`9126` and :rfc:`7519`.
    * - **iat**
      - OPTIONAL. UNIX Timestamp with the time of JWT issuance.
      - :rfc:`9126` and :rfc:`7519`.
    * - **nbf**
      - OPTIONAL. UNIX Timestamp with the start time of validity of the JWT issuance.
      - :rfc:`9126` and :rfc:`7519`.
    * - **cnf**
      - REQUIRED. JSON object, containing the public part of an asymmetric key pair owned by the Wallet Instance.
      - :rfc:`7800`.
    * - **wallet_link**
      - OPTIONAL. String containing a URL to get further information about the Wallet and the Wallet Provider.
      - `OpenID4VCI`_.
    * - **wallet_name**
      - OPTIONAL. String containing a human-readable name of the Wallet.
      - `OpenID4VCI`_.
    * - **status**
      - OPTIONAL. Status mechanism for the Wallet Attestation as defined in Section 6.2 of `TOKEN-STATUS-LIST`_.
      - :rfc:`9126` and :rfc:`7519`.
    * - **sub**
      - REQUIRED. Identifier of the Wallet Instance which is the thumbprint of the Wallet App Attestation JWK.
      - :rfc:`9126` and :rfc:`7519`.


Below is a non-normative example of the Wallet App Attestation JWT header and payload, without encoding and signature applied:

.. literalinclude:: ../../examples/wa-jwt_example_header.json
  :language: JSON

.. literalinclude:: ../../examples/wa-jwt_example_payload.json
  :language: JSON


Wallet Unit Attestation JWT
""""""""""""""""""""""""""""

The JOSE header of the Wallet Unit Attestation JWT contains the following parameters:


.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **JOSE header**
      - **Description**
      - **Reference**
    * - **alg**
      - REQUIRED. A digital signature algorithm identifier such as per IANA "JSON Web Signature and Encryption Algorithms" registry. It MUST be one of the supported algorithms listed in the Section :ref:`algorithms:cryptographic algorithms` and MUST NOT be set to ``none`` or any symmetric algorithm (MAC) identifier.
      - :rfc:`7516#section-4.1.1`.
    * - **kid**
      - REQUIRED. Unique identifier of the public key associated to the private key the Wallet Provider used to sign the Wallet Unit Attestation.
      - :rfc:`7638#section_3`.
    * - **typ**
      - REQUIRED. It MUST be set to ``key-attestation+jwt``
      - `OPENID4VC-HAIP`_.
    * - **trust_chain**
      - OPTIONAL. Sequence of Entity Statements that composes the Trust Chain related to the Wallet Provider.
      - `OID-FED`_ Section 4.3 *Trust Chain Header Parameter*.
    * - **x5c**
      - REQUIRED. Contains the X.509 public key certificate or certificate chain (:rfc:`5280`) corresponding to the key used to digitally sign the JWT.
      - :rfc:`7515` Section 4.1.8.

The body of the Wallet Unit Attestation JWT contains the following claims:

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Description**
      - **Reference**
    * - **iss**
      - REQUIRED. Identifier of the Wallet Provider.
      - :rfc:`9126` and :rfc:`7519`.
    * - **exp**
      - REQUIRED. UNIX Timestamp with the expiry time of the JWT.
      - :rfc:`9126` and :rfc:`7519`.
    * - **iat**
      - REQUIRED. UNIX Timestamp with the time of JWT issuance.
      - :rfc:`9126` and :rfc:`7519`.
    * - **attested_keys**
      - REQUIRED. A non-empty array of attested keys from the same key storage component using the syntax of JWK, containing the public part of an asymmetric key pair owned by the Wallet Instance.
      - :rfc:`7517`.
    * - **key_storage**
      - REQUIRED. A non-empty array of case sensitive strings that assert the attack potential resistance of the key storage component and its keys attested in the ``attested_keys`` parameter. The following values are defined as a value for this claim:

        - ``iso_18045_high``: It MUST be used when key storage is resistant to attack with attack potential ``High``.
        - ``iso_18045_moderate``: It MUST be used when key storage is resistant to attack with attack potential ``Moderate``.
        - ``iso_18045_basic``: It MUST be used when key storage is resistant to attack with attack potential ``Basic``.
      - `OpenID4VCI`_.
    * - **user_authentication**
      - REQUIRED. A non-empty array of case sensitive strings that assert the attack potential resistance of the user authentication methods allowed to access the private keys from the ``attested_keys`` parameter. The following values are defined as a value for this claim:

        - ``iso_18045_high``: It MUST be used when user authentication is resistant to attack with attack potential ``High``.
        - ``iso_18045_moderate``: It MUST be used when user authentication is resistant to attack with attack potential ``Moderate``.
        - ``iso_18045_basic``: It MUST be used when user authentication is resistant to attack with attack potential ``Basic``.
      - `OpenID4VCI`_.
    * - **status**
      - REQUIRED. JSON Object representing the supported revocation check mechanisms, such as OAuth Status List.
      - `OpenID4VCI`_.
    * - **certification**
      - OPTIONAL. A String that contains a URL that links to the certification of the key storage component.
      - `OpenID4VCI`_.


Below is a non-normative example of the Wallet Unit Attestation JWT header and payload, without encoding and signature applied:

.. literalinclude:: ../../examples/wua-jwt_example_header.json
  :language: JSON

.. literalinclude:: ../../examples/wua-jwt_example_payload.json
  :language: JSON

e-Service PDND Wallet Provider Catalog
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

User's death leads to the revocation of the Wallet Instances of the User and the deletion of the User account at the Wallet Provider. For this reason, the Wallet Provider provides the following e-service through PDND.
A PID Provider that has been notified by the Authentic Source of the PID of the User's death MUST send a notification to Wallet Providers using this endpoint.

.. only:: html

  .. note::
    A complete OpenAPI Specification is available :raw-html:`<a href="OAS3-PDND-WP.html" target="_blank">here</a>`.

.. only:: latex

  .. note::
    A complete OpenAPI Specification is available :ref:`appendix-oas-pdnd-wp:Wallet Provider PDND OpenAPI Specification`.

Notify User Death
"""""""""""""""""

.. list-table::
    :class: longtable
    :widths: 20 80
    :stub-columns: 1

    * - **Description**
      - This service is used to notify the Wallet Provider of the need to revoke the Wallet Instance and delete the User's account due to the User's death.
    * - **Provider**
      - Wallet Provider
    * - **Consumer**
      - PID Provider


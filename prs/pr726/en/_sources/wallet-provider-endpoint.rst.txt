.. include:: ../common/common_definitions.rst

.. "included" file, so we start with '-' title level

.. role:: raw-html(raw)
  :format: html


Wallet Provider Endpoints
-------------------------

The Wallet Provider, responsible for delivering a Wallet Solution, MUST expose the endpoints to support trust establishment and essential Wallet Instance functionalities. These include the ``/.well-known/openid-federation`` Federation Endpoint which MUST adhere to the OpenID Federation 1.0 specification to reliably establish trust with the Wallet Provider's as well as, endpoints for Wallet Instance registration, nonce generation (required for registration), attestation issuance, and revocation. Aside from the Federation endpoint, the implementation details of the others are left to the Wallet Provider's discretion.

Federation Endpoint
^^^^^^^^^^^^^^^^^^^

The ``/.well-known/openid-federation`` endpoint serves as the discovery mechanism for trust establishment by retrieving the Wallet Provider Entity Configuration. 

See Section :ref:`wallet-provider-entity-configuration:Wallet Provider Entity Configuration` for technical details.


Wallet Solution Nonce Endpoint 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is a RESTful API endpoint that allows the Wallet Instance to request a cryptographic nonce from the Wallet Provider. The nonce serves as an unpredictable, single-use challenge to ensure freshness and prevent replay attacks.

See :ref:`mobile-application-instance:Mobile Application Nonce Request` and :ref:`mobile-application-instance:Mobile Application Nonce Response` for details on the Nonce Request and Nonce Response.

Wallet Instance Management Endpoint
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is a RESTful API endpoint provided by the Wallet Provider that enables Wallet Instance management, including registration, status retrieval, revocation upon request (e.g., by the User), and deletion.
The following sections describe the registration, status retrieval and revocation requests, along with their corresponding responses, handled by this endpoint, which are required for core :ref:`wallet-instance-functionalities:Wallet Instance Functionalities`.

Wallet Instance Registration Request
"""""""""""""""""""""""""""""""""""""

To register a Wallet Instance, the request to the Wallet Provider MUST use the HTTP POST method with ``Content-Type`` set to `application/json`. The request body MUST contain the claims described in :ref:`mobile-application-instance:Mobile Application Instance Initialization Request`.

Wallet Instance Registration Response
"""""""""""""""""""""""""""""""""""""""""

If a Wallet Instance Registration Request is successfully validated, the Wallet Provider provides an HTTP Response with status code 204 (No Content). For detatails see :ref:`mobile-application-instance:Mobile Application Instance Initialization Response`.

Wallet Instance Retrieval Request
"""""""""""""""""""""""""""""""""""

To retrieve all Wallet Instances associated with a User, a request MUST be sent using the HTTP GET method to the Wallet Provider.

.. note::
  For retrieving a specific Wallet Instance, the request MUST include the Wallet Instance ID as a path parameter.


Wallet Instance Retrieval Response
"""""""""""""""""""""""""""""""""""

If a Wallet Instance Retrieval Request is successfully processed, the Wallet Provider MUST return an HTTP Response with a 200 (OK) status code.
The response body MUST be in JSON format and include the relevant Wallet Instance information, such as its unique ID, status, and issuance date.
When retrieving all Wallet Instances, the response MUST return an array containing the details of all associated instances.

If any errors occur during the retrieval process, an error response MUST be returned. Refer to :ref:`wallet-provider-endpoint:Error Handling for Wallet Instance Management` for details on error codes and descriptions.

Below is a non-normative example of an error response:

.. code:: http

   HTTP/1.1 403 Forbidden
   Content-Type: application/json
   Cache-Control: no-store

.. code:: json

   {
     "error": "forbidden",
     "error_description": "User is not authorized to retrieve Wallet Instances."
   }


Wallet Instance Revocation Request
""""""""""""""""""""""""""""""""""

To revoke an active Wallet Instance, a revocation request MUST be sent using the HTTP PATCH method with Content-Type set to ``application/json``. The request body MUST contain a ``status`` parameter set to ``REVOKED``.

.. note::
  While PATCH is the recommended method, the revocation request MAY also be sent using the POST method, depending on implementation preferences.

Wallet Instance Revocation Response
"""""""""""""""""""""""""""""""""""

If a Wallet Instance Revocation Request is successfully processed, the Wallet Provider provides an HTTP Response with a 204 (No Content) status code.

If any errors occur during the Wallet Instance Revocation, an error response MUST be returned. Refer to :ref:`wallet-provider-endpoint:Error Handling for Wallet Instance Management` for details on error codes and descriptions.

Below is a non-normative example of an error response:

.. code:: http

   HTTP/1.1 400 Bad Request
   Content-Type: application/json
   Cache-Control: no-store

.. code:: json

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

The following sections categorize errors into **common errors**, which apply to all requests, and **request-specific errors**, which are relevant to particular operations.

Common Error Responses
"""""""""""""""""""""""

The following errors apply to all Wallet Instance Management operations (Registration, Retrieval, and Revocation), and MUST be supported for the error response, unless otherwise specified:

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

The following errors MUST be supported for error responses related to **Wallet Instance Retrieval**:

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

The following errors MUST be supported for error responses related to **Wallet Instance Revocation**:

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

Wallet Attestation Issuance Endpoint
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is a RESTful API endpoint provided by the Wallet Provider that enables the Wallet Instance to obtain a Wallet Attestation, by sending a Wallet Attestation Issuance Request.

Wallet Attestation Issuance Request
"""""""""""""""""""""""""""""""""""""

Further details on the Wallet Attestation Issuance Request are provided in the :ref:`mobile-application-instance:Mobile Application Key Binding Request` section.

The ``typ`` header of the Integrity Request JWT assumes the value ``wp-war+jwt``.

Wallet Attestation Issuance Response
"""""""""""""""""""""""""""""""""""""

If the Wallet Attestation Issuance Request is successfully validated, the Wallet Provider returns an HTTP response with a status code of ``200 OK`` and Content-Type ``application/json``. The returned JSON Object MUST possess the ``wallet_attestations`` parameter whose value is an array of JSON Objects (see :ref:`wallet-attestation-issuance:Wallet Attestation Issuance`) containing the Wallet Attestations in JWT, SD-JWT and mdoc format signed by the Wallet Provider. The JWT formatted Wallet Attestation is to be used for the Issuance phase, as an OAuth Client Attestation, and will be sent to the Credential Issuer as discussed in :ref:`credential-issuance:Digital Credential Issuance`. The SD-JWT and mdoc formatted Wallet Attestation will instead be used during presentation respectively in the remote (:ref:`remote-flow:Remote Flow`) and proximity (:ref:`proximity-flow:Proximity Flow`) flows.


The JSON Object returned in the response has the following claim:

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Parameter**
      - **Description**
      - **Reference**
    * - **wallet_attestations**
      - REQUIRED. Contains an array of one or more issued Wallet Attestation. The elements of the array MUST be JSON Objects. At least two JSON Objects MUST be present.
      - This specification.

Each JSON Object contained in the ``wallet_attestations`` array MUST have the following form:

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Parameter**
      - **Description**
      - **Reference**
    * - **format**
      - A string identifying the Data Model used to create and represent the Wallet Attestation. It MUST be either ``jwt``, ``dc+sd-jwt`` or ``mso_mdoc`` depending on the credential format.
      - This specification.
    * - **wallet_attestation**
      - A string representing the Wallet Attestation. If

        - the Wallet Attestation is in JWT format, then the claim's value MUST be a string that is a JWT.
        - the Wallet Attestation is in SD-JWT format, then the claim's value MUST be a string that is an SD-JWT VC.
        - the Wallet Attestation is in mdoc format, then the claim's value is the base64url-encoded representation of the CBOR-encoded IssuerSigned structure, as defined in [ISO.18013-5]. This structure MUST contain all Namespaces and IssuerSignedItems that are included in the MobileSecurityObject.

      - This specification.

If any errors occur during the process, an error response is returned. Further details on the error response are provided in the :ref:`mobile-application-instance:Mobile Application Key Binding Error Response` section.


Wallet Attestation JWT
"""""""""""""""""""""""

The JOSE header of the Wallet Attestation JWT contains the following parameters:

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
      - REQUIRED. Unique identifier of the public key associated to the private key the Wallet Provider used to sign the Wallet Attestation.
      - :rfc:`7638#section_3`.
    * - **typ**
      - REQUIRED. It MUST be set to ``oauth-client-attestation+jwt``
      - `OPENID4VC-HAIP`_.
    * - **trust_chain**
      - REQUIRED. Sequence of Entity Statements that composes the Trust Chain related to the Wallet Provider.
      - `OID-FED`_ Section 4.3 *Trust Chain Header Parameter*.
    * - **x5c**
      - OPTIONAL. Contains the X.509 public key certificate or certificate chain (:rfc:`5280`) corresponding to the key used to digitally sign the JWT.
      - :rfc:`7515` Section 4.1.8 and `SD-JWT-VC`_ Section 3.5.

The body of the Wallet Attestation JWT contains the following claims:

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
    * - **cnf**
      - REQUIRED. JSON object, containing the public part of an asymmetric key pair owned by the Wallet Instance.
      - :rfc:`7800`.
    * - **wallet_link**
      - OPTIONAL. String containing a URL to get further information about the Wallet and the Wallet Provider.
      - `OpenID4VCI`_.
    * - **wallet_name**
      - OPTIONAL. String containing a human-readable name of the Wallet.
      - `OpenID4VCI`_.
    * - **sub**
      - REQUIRED. Identifier of the Wallet Instance which is the thumbprint of the Wallet Attestation JWK.
      - :rfc:`9126` and :rfc:`7519`.
    * - **aal**
      - REQUIRED. JSON String asserting the authentication level of the Wallet and the key as asserted in the cnf claim.
      - This specification.

Below is a non-normative example of the SD-JWT Wallet Attestation header and payload without encoding and signature applied:

.. code-block:: json

  {
    "alg": "ES256",
    "kid": "5t5YYpBhN-EgIEEI5iUzr6r0MR02LnVQ0OmekmNKcjY",
    "trust_chain": [
      "eyJhbGciOiJFUz...6S0A",
      "eyJhbGciOiJFUz...jJLA",
      "eyJhbGciOiJFUz...H9gw",
    ],
    "typ": "jwt"
  }
  
.. code-block:: json

  {
    "iss": "https://wallet-provider.example.org",
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
    "iat": 1687281195,
    "exp": 1687288395,
    "vct": "wallet.atestation.example/v1.0",
    "sub": "vbeXJksM45xphtANnCiG6mCyuU4jfGNzopGuKvogg9c",
    "aal": "https://trust-list.eu/aal/high",
    "wallet_name": "Wallet_v1",
    "wallet_link": "https://example.com/wallet/detail_info.html"
  }


Wallet Attestation SD-JWT
"""""""""""""""""""""""""""

The JOSE header of the Wallet Attestation SD-JWT MUST contain the following parameters:

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **JOSE header**
      - **Description**
      - **Reference**
    * - **alg**
      - REQUIRED. A digital signature algorithm identifier such as per IANA "JSON Web Signature and Encryption Algorithms" registry. It MUST be one of the supported algorithms listed in :ref:`algorithms:cryptographic algorithms` and MUST NOT be set to ``none`` or any symmetric algorithm (MAC) identifier.
      - :rfc:`7516#section-4.1.1`.
    * - **kid**
      - REQUIRED. Unique identifier of the public key associated to the private key the Wallet Provider used to sign the Wallet Attestation.
      - :rfc:`7638#section_3`.
    * - **typ**
      - REQUIRED. It MUST be set to ``dc+sd-jwt``
      - `OPENID4VC-HAIP`_.
    * - **trust_chain**
      - REQUIRED. Sequence of Entity Statements that composes the Trust Chain related to the Wallet Provider.
      - `OID-FED`_ Section 4.3 *Trust Chain Header Parameter*.
    * - **x5c**
      - OPTIONAL. Contains the X.509 public key certificate or certificate chain (:rfc:`5280`) corresponding to the key used to digitally sign the JWT.
      - :rfc:`7515` Section 4.1.8 and `SD-JWT-VC`_ Section 3.5.

The body of the Wallet Attestation SD-JWT contains the following claims:

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
    * - **cnf**
      - REQUIRED. JSON object, containing the public part of an asymmetric key pair owned by the Wallet Instance.
      - :rfc:`7800`.
    * - **vct**
      - REQUIRED. Credential type value MUST be an HTTPS URL String and it MUST be set to ``wallet.atestation.example/v1.0``.
      - Section 3.2.2.2 `SD-JWT-VC`_.
    * - **_sd**
      - REQUIRED. JSON array containing a list of all disclusure's digests.
      - `SD-JWT`_.
    * - **sd_alg**
      - REQUIRED. String containing the hash algorithm used by the Wallet Provider to generate the disclusure's digests.
      - `SD-JWT`_.
    * - **sub**
      - REQUIRED. Identifier of the Wallet Instance which is the thumbprint of the Wallet Attestation JWK.
      - :rfc:`9126` and :rfc:`7519`.
    * - **aal**
      - REQUIRED. JSON String asserting the authentication level of the Wallet and the key as asserted in the cnf claim.
      - This specification.

The following disclosures MAY be present:

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Disclosure**
      - **Description**
      - **Reference**
    * - **wallet_link**
      - OPTIONAL. String containing a URL to get further information about the Wallet and the Wallet Provider.
      - `OpenID4VCI`_.
    * - **wallet_name**
      - OPTIONAL. String containing a human-readable name of the Wallet.
      - `OpenID4VCI`_.

Below are described examples of values for the disclosures:

.. **Claim** ``sub``:
..
.. - SHA-256 Hash: ``DTZRbQgOWJlLaBfe6pr+j1vL4B4t6LLWyt9loaEJKe0=``
.. - Disclosure: ``WyIyR0xDNDJzS1F2ZUNmR2ZyeU5STjl3IiwgInN1YiIsICJ2YmVYSmtzTTQ1eHBodEFObkNpRzZtQ3l1VTRqZkdOem9wR3VLdm9nZzljIl0=``
.. - Contents: ``["2GLC42sKQveCfGfryNRN9w", "sub", "vbeXJksM45xphtANnCiG6mCyuU4jfGNzopGuKvogg9c"]``
..
.. **Claim** ``aal``:
..
.. - SHA-256 Hash: ``h+w4Q4dWcHebykPpS4jRsBZVvBhEKszyLeZGmEunDJ4=``
.. - Disclosure: ``WyIyR0xDNDJzS1F2ZUNmR2ZyeU5STjl3IiwgImFhbCIsICJodHRwczovL3RydXN0LWxpc3QuZXUvYWFsL2hpZ2giXQ==``
.. - Contents: ``["2GLC42sKQveCfGfryNRN9w", "aal", "https://trust-list.eu/aal/high"]``

**Claim** ``wallet_link``:

- SHA-256 Hash: ``cD9/XC7t7QVHvmSiE1dGW0WYr0jcqm8n0GA6MGitaik=``
- Disclosure: ``WyIyR0xDNDJzS1F2ZUNmR2ZyeU5STjl3IiwgIndhbGxldF9saW5rIiwgImh0dHBzOi8vZXhhbXBsZS5jb20vd2FsbGV0L2RldGFpbF9pbmZvLmh0bWwiXQ==``
- Contents: ``["2GLC42sKQveCfGfryNRN9w", "wallet_link", "https://example.com/wallet/detail_info.html"]``

**Claim** ``wallet_name``:

- SHA-256 Hash: ``iQQhzf6+saYCzHH92N1QyJisKsZbApbTrJ1amHgLoOk=``
- Disclosure:n``WyIyR0xDNDJzS1F2ZUNmR2ZyeU5STjl3IiwgIndhbGxldF9uYW1lIiwgIldhbGxldF9Ib2JiaXRvbl92MSJd``
- Contents: ``["2GLC42sKQveCfGfryNRN9w", "wallet_name", "Wallet_v1"]``

Below is a non-normative example of the SD-JWT Wallet Attestation header and payload without encoding and signature applied:

.. code-block:: json

  {
    "alg": "ES256",
    "kid": "5t5YYpBhN-EgIEEI5iUzr6r0MR02LnVQ0OmekmNKcjY",
    "trust_chain": [
      "eyJhbGciOiJFUz...6S0A",
      "eyJhbGciOiJFUz...jJLA",
      "eyJhbGciOiJFUz...H9gw"
    ],
    "typ": "dc+sd-jwt"
  }
  
.. code-block:: json

  {
    "iss": "https://wallet-provider.example.org",
    "cnf": {
      "jwk":
      {
        "crv": "P-256",
        "kty": "EC",
        "x": "4HNptI-xr2pjyRJKGMnz4WmdnQD_uJSq4R95Nj98b44",
        "y": "LIZnSB39vFJhYgS3k7jXE4r3-CoGFQwZtPBIRqpNlrg"
      }
    },
    "_sd": ["cD9/XC7t7QVHvmSiE1dGW0WYr0jcqm8n0GA6MGitaik=", "iQQhzf6+saYCzHH92N1QyJisKsZbApbTrJ1amHgLoOk="],
    "_sd_alg": "sha-256",
    "iat": 1687281195,
    "exp": 1687288395,
    "vct": "https://wallet.attestation.example/v1.0",
    "sub": "vbeXJksM45xphtANnCiG6mCyuU4jfGNzopGuKvogg9c",
    "aal": "https://trust-framework.example.it/aal/high"
  }

Wallet Attestation mdoc
"""""""""""""""""""""""

This description further specializes the guidelines given in ref:`pid-eaa-data-model:MDOC-CBOR Credential Format` to represent the Wallet Attestation in mdoc format. The latter MUST:

- Have the domestic namespace ``org.iso.18013.5.1.it``;
- Have **docType** set to ``org.iso.18013.5.1.it.WalletAttestation``; and
- Have **issuerAuth** as described in :ref:`credential-data-model:Mobile security Object`.

The ``nameSpaces`` for the domestic nameSpace Json Objects are defined as follows:

.. list-table:: org.iso.18013.5.1.it
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **elementIdentifier**
      - **Description**
      - **Reference**
    * - **sub**
      - REQUIRED. Identifier of the Wallet Instance which is the thumbprint of the Wallet Attestation COSE Key.
      - :rfc:`9126` and :rfc:`7519`.
    * - **aal**
      - JSON String asserting the authentication level of the Wallet Instance in relation to the COSE Key contained in the ``IssuerAuth.deviceKeyInfo.deviceKey`` claim of the **issuerAuth** Object.
      - :rfc:`9679`.
    * - **wallet_link**
      - JSON String containing a URL to get further information about the Wallet and the Wallet Provider.
      - `OpenID4VCI`_.
    * - **wallet_name**
      - JSON String, it MUST be the Identifier of the Wallet Provider.
      - `OpenID4VCI`_.

Below is a non-normative example of the mdoc Wallet Attestation in CBOR diagnostic notation:

.. code-block:: text

  {
    "docType": "org.iso.18013.5.1.it.WalletAttestation",
    "issuerSigned":{
      "nameSpaces":{
        "org.iso.18013.5.1.it":[
          24(<< {
          "digestID": 0,
          "random": h'960CB15A…E902807AA95',
          "elementIdentifier": "wallet_name",
          "elementValue": "Wallet_v1"
          } >>),
          24(<<
          {
          "digestID": 1,
          "random": h'9D3774BD59…A4F76A',
          "elementIdentifier": "wallet_link",
          "elementValue":"https://example.com/wallet/detail_info.html"
          } >>),
          24(<< {
          "digestID": 2,
          "random": h'AE84834F3…A3E4FCCE',
          "elementIdentifier": "sub",
          "elementValue":"vbeXJksM45xphtANnCiG6mCyuU4jfGNzopGuKvogg9c"
          } >>),
          24(<<
          {
          "digestID": 3,
          "random": h'9D3774BD59…A4F76A',
          "elementIdentifier": "aal",
          "elementValue":"https://trust-list.eu/aal/high"
          } >>)
        ]
  },
    "issuerAuth": [
      << {1: -7} >>,
      {
      33: h'30820215308201BCA003020102021404AD30C…'
      },
      <<
        24(<<
          {
            "docType":"org.iso.18013.5.1.it.WalletAttestation",
            "version": "org.iso.18013.5.1.it",
            "validityInfo": {
              "signed": "2023-02-22T06:23:56Z"
              "validFrom": "2023-02-22T06:23:56Z",
              "validUntil": "2024-02-22T00:00:00Z"
            },
            "valueDigests": {
              "org.iso.18013.5.1.it": {
                0: h'0F1571A988FCDF2929…',
                1: h'0CDFE0774A2B596C90…',
                2: h'E23821492558984395…',
                3: h'BBC77E6CCE544EDF86…'
              }
            },
            "deviceKeyInfo": {
              "deviceKey": {
                1: 2,
                -1: 1,
                -2: h'B820963964E5…',
                -3: h'0A6DA0AF437E…'
              }
            },
            "digestAlgorithm": "SHA-256"
          }
        >>)
      >>,
      h'1AD0D6A7313EFDC…43DEBF48BF5A580D'
    ]
  }


e-Service PDND Wallet Provider Catalogue
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


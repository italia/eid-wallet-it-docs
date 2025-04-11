.. include:: ../common/common_definitions.rst

.. _relying-party-endpoint:

Relying Party Endpoints
=========================

The Relying Party MUST expose a trust endpoint adhering to the OpenID Federation 1.0 Wallet Architecture specification, facilitating the Relying Party's identity and metadata distribution. In addition, in case the Relying Party supports proximity presentation, it MUST expose a set of endpoints for handling the lifecycle of Relying Party Instances (e.g., by providing nonce generation, hardware key registration, integrity validation, and Access Certificate issuance); their specific implementation details are left to the Relying Party's discretion.


Relying Party Federation Endpoint
-----------------------------------

.. include:: relying-party-entity-configuration.rst


Relying Party Nonce Endpoint
----------------------------------

The Relying Party Nonce Endpoint allows the Relying Party Instance to request a cryptographic ``nonce`` from the Relying Party Backend. The ``nonce`` serves as an unpredictable, single-use challenge to ensure freshness and prevent replay attacks.

Further details on the Nonce Request and Response are provided in the :ref:`Nonce Request` and :ref:`Nonce Response` sections, respectively.


Relying Party Instance Initialization Endpoint
---------------------------------------------------

The Relying Party Instance Initialization Endpoint allows for the initialization of Relying Party Instances, consisting in the registration of a pair of long-lived, securely stored Cryptographic Hardware Keys.

Further details on the Relying Party Instance Initialization Request and Response are provided in the :ref:`Mobile Application Instance Registration Request` and :ref:`Mobile Application Instance Registration Response` sections, respectively.


Relying Party Integrity Validation Endpoint
----------------------------------------------

The Relying Party Integrity Validation Endpoint enables Relying Party Instances to prove their integrity, before obtaining an Access Certificate.


Relying Party Integrity Validation Request
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The request uses the HTTP POST method with ``Content-Type`` set to ``application/json``.

The Integrity Validation Request includes the following HTTP header parameters:

.. list-table::
    :widths: 20 60 20
    :header-rows: 1

    * - **Parameter**
      - **Description**
      - **Reference**
    * - **alg**
      - A digital signature algorithm identifier.
      - [:rfc:`7515`]
    * - **kid**
      - Unique identifier of the JWK used by the Relying Party Instance to sign the Integrity Validation Request.
      - [:rfc:`7515`]
    * - **typ**
      - It MUST be set to ``rp-ivr+jwt``
      -

The Integrity Validation Request includes the following body parameters:

.. list-table::
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Description**
      - **Reference**
    * - **iss**
      - The identifier of the Relying Party concatenated with the thumbprint of the JWK in the ``cnf`` claim.
      - [:rfc:`9126`], [:rfc:`7519`].
    * - **aud**
      - The identifier of the Relying Party Backend.
      - [:rfc:`9126`], [:rfc:`7519`].
    * - **exp**
      - UNIX timestamp representing the JWT expiration time.
      - [:rfc:`9126`], [:rfc:`7519`].
    * - **iat**
      - UNIX timestamp representing the JWT issuance time.
      - [:rfc:`9126`], [:rfc:`7519`].
    * - **nonce**
      - The ``nonce`` obtained from the :ref:`Nonce Endpoint`.
      -
    * - **hardware_signature**
      - The signature of ``client_data`` obtained using the Cryptographic Hardware Key, encoded in the ``base64url`` format.
      -
    * - **key_attestation**
      - The key attestation obtained from the Key Attestation APIs with the holder binding of ``client_data``.
      -
    * - **hardware_key_tag**
      - The value of the Cryptographic Hardware Key Tag.
      -


Relying Party Integrity Validation Response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Upon a successful request, the Integrity Validation Endpoint provides an HTTP Response with a ``204 No Content`` status code.

If any errors occur, the Integrity Validation Endpoint returns an error response. The response uses ``application/json`` as the content type and includes the following parameters:

  - *error*. The error code.
  - *error_description*. Text in human-readable form providing further details to clarify the nature of the error encountered.

.. code-block:: http
    :caption: Non-normative example of an Hardware Key Registration Error Response
    :name: code_RelyingParty_Endpoint_IntegrityValidation_Error
    
    HTTP/1.1 403 Forbidden
    Content-Type: application/json

    {
        "error": "forbidden",
        "error_description": "The provided challenge is invalid, expired, or already used."
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
      - ``integrity_check_error``
      - The device does not meet the Relying Party's minimum security requirements.
    * - ``403 Forbidden``
      - ``invalid_request``
      - The signature of the Integrity Validation Request is invalid or does not match the associated public key (JWK).
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
      - The ``iss`` parameter does not match the Relying Party expected URL identifier.
    * - ``404 Not Found`` 
      - ``not_found``
      - The Relying Party Instance was not found.
    * - ``422 Unprocessable Content`` [OPTIONAL]
      - ``validation_error``
      - The request does not adhere to the required format.
    * - ``500 Internal Server Error``
      - ``server_error``
      - The request cannot be fulfilled because the Endpoint encountered an internal problem.
    * - ``503 Service Unavailable``
      - ``temporarily_unavailable``
      - The request cannot be fulfilled because the Endpoint is temporarily unavailable (e.g., due to maintenance or overload).


Relying Party Access Certificate Endpoint
----------------------------------------------

The Relying Party Access Certificate Endpoint enables Relying Party Instances to obtain an Access Certificate.


Relying Party Access Certificate Request
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The request uses the HTTP POST method with ``Content-Type`` set to ``application/json``.

The Access Certificate Request includes the following body parameters:

.. list-table::
    :widths: 20 60 20
    :header-rows: 1

    * - **Parameter**
      - **Description**
      - **Reference**
    * - **csr**
      - The CSR generated by the Relying Party Instance, encoded in the ``base64url`` format as defined in :rfc:`2511`.
      - 


Relying Party Access Certificate Response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Upon a successful request, the Relying Party Access Certificate Endpoint provides an HTTP Response with a ``200 OK`` status code and the Access Certificate. The Access Certificate Response, which uses ``application/json`` as the ``Content-Type``, includes the following body parameters:

.. list-table::
    :widths: 20 60 20
    :header-rows: 1

    * - **Parameter**
      - **Description**
      - **Reference**
    * - **access_certificate**
      - The Access Certificate generated by the CSR.
      - 

If any errors occur, the Relying Party Access Certificate Endpoint returns an error response. The response uses ``application/json`` as the content type and includes the following parameters:

  - *error*. The error code.
  - *error_description*. Text in human-readable form providing further details to clarify the nature of the error encountered.

.. code-block:: http
    :caption: Non-normative example of an Hardware Key Registration Error Response
    :name: code_RelyingParty_Endpoint_AccessCertificate_Error
    
    HTTP/1.1 403 Forbidden
    Content-Type: application/json

    {
        "error": "forbidden",
        "error_description": "The public key in the CSR is different from the one associated with the Cryptographic Hardware Keys."
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
      - The public key in the CSR does not match the public key associated with the Cryptographic Hardware Keys.
    * - ``500 Internal Server Error``
      - ``server_error``
      - The request cannot be fulfilled because the Endpoint encountered an internal problem.
    * - ``503 Service Unavailable``
      - ``temporarily_unavailable``
      - The request cannot be fulfilled because the Endpoint is temporarily unavailable (e.g., due to maintenance or overload).

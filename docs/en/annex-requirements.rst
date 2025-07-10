Requirements
============

This annex reports all the requirements identified in the document, organized in a structured table with the following columns:

- **ID**: unique code that identifies the requirement
- **Description**: detailed description of the requirement
- **Audience**: subject responsible for the implementation and satisfaction of the requirement
- **Category**: classification of the requirement as Security or Privacy
- **Context**: scope of application of the requirement


Trust Framework Requirements
----------------------------

TBD


Wallet Solution Requirements
----------------------------

TBD


Digital Credentials Requirements
------------------------------

TBD


Digital Credentials Provider Requirements
--------------------------------------------

TBD


Relying Party Requirements
---------------------------

TBD


Relying Party Metadata Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following table lists the requirements with a unique identifier.

.. list-table::
    :class: longtable
    :widths: 20 80
    :header-rows: 1

    * - **ID**
      - **Requirement**
      - **Audience**
      - **Category**
      - **Context**

    * - RPMD-1
      - The Relying Party MUST include a ``client_id`` parameter containing an HTTPS URL that uniquely identifies the RP in the openid_credential_verifier metadata.
      - Relying Party
      - Security
      - Metadata Configuration
    * - RPMD-2
      - The Relying Party MUST include a ``client_name`` parameter containing a human-readable string name of the RP in the openid_credential_verifier metadata.
      - Relying Party
      - Privacy
      - Metadata Configuration
    * - RPMD-3
      - The Relying Party MUST include an ``application_type`` parameter set to "web" value in the openid_credential_verifier metadata.
      - Relying Party
      - Security
      - Metadata Configuration
    * - RPMD-4
      - The Relying Party MUST include a request_uris parameter containing a JSON Array of request_uri values that are pre-registered by the RP, using the https scheme.
      - Relying Party
      - Security
      - Metadata Configuration
    * - RPMD-5
      - The Relying Party MUST include a response_uris parameter containing a JSON Array of response URI strings to which the Wallet Instance MUST send the Authorization Response using an HTTP POST request.
      - Relying Party
      - Security
      - Metadata Configuration
    * - RPMD-6
      - The Relying Party MUST include an authorization_signed_response_alg parameter representing the signing alg algorithm that MUST be used for signing authorization responses, excluding the "none" algorithm.
      - Relying Party
      - Security
      - Metadata Configuration
    * - RPMD-7
      - The Relying Party MUST include an authorization_encrypted_response_alg parameter specifying the asymmetric encryption algorithm to the Wallet Instance.
      - Relying Party
      - Security
      - Metadata Configuration
    * - RPMD-8
      - The Relying Party MUST include an authorization_encrypted_response_enc parameter specifying the symmetric encryption algorithm to the Wallet Instance.
      - Relying Party
      - Security
      - Metadata Configuration
    * - RPMD-9
      - The Relying Party MUST include a vp_formats parameter defining the formats and proof types of Verifiable Presentations and Verifiable Credentials the RP supports, with at least "dc+sd-jwt" support.
      - Relying Party
      - Security
      - Metadata Configuration
    * - RPMD-10
      - The Relying Party MUST include a jwks parameter containing the JSON Web Key Set document with protocol specific keys.
      - Relying Party
      - Security
      - Metadata Configuration
    * - RPMD-11
      - The Relying Party MUST include an erasure_endpoint parameter when requesting attributes that can uniquely identify Users, representing the URI for Users' attributes deletion requests.
      - Relying Party
      - Privacy
      - Metadata Configuration


Remote Presentation Flow Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


The following table lists the requirements with a unique identifier.

.. list-table::
    :class: longtable
    :widths: 20 80
    :header-rows: 1

    * - **ID**
      - **Requirement**
      - **Audience**
      - **Category**
      - **Context**

    * - REMFLOW-1
      - The Relying Party MUST inspect the user-agent to determine whether the flow occurs on the same device or cross device or asking the User to manually select the flow type.
      - Relying Party
      - Security
      - Presentation Initiation
    * - REMFLOW-2
      - The Relying Party MUST support a Same Device flow by providing an HTTP location to the Wallet Instance using a redirect (302) or an HTML href in a web page.
      - Relying Party
      - Security
      - Presentation Initiation
    * - REMFLOW-3
      - The Relying Party MUST support a Cross Device flow by providing a QR Code which the User frames with the Wallet Instance.
      - Relying Party
      - Security
      - Presentation Initiation
    * - REMFLOW-4
      - The QR Code MUST contain a URL with the parameters ``client_id``, ``request_uri``, ``state``.
      - Relying Party
      - Security
      - Presentation Initiation
    * - REMFLOW-5
      - The Relying Party MUST ensure proper rate limiting for QR code generation or produce QR Codes using JS within the Holder's user-agent.
      - Relying Party
      - Security
      - Presentation Initiation
    * - REMFLOW-6
      - The Relying Party MUST bind the ``state`` value to the user-agent using a secure method (e.g., HTTP secured cookie).
      - Relying Party
      - Security
      - Presentation Initiation
    * - REMFLOW-7
      - The Relying Party MUST make the Authorization Request Object available for download at the ``request_uri`` location.
      - Relying Party
      - Security
      - Request Processing
    * - REMFLOW-8
      - The Relying Party MUST ensure the Authorization Request Object is properly signed and contains all required claims.
      - Relying Party
      - Security
      - Request Processing
    * - REMFLOW-9
      - The Relying Party MUST ensure proper timeout handling for QR code scanning.
      - Relying Party
      - Security
      - Flow Management
    * - REMFLOW-10
      - The Relying Party MUST implement proper cleanup of expired Authorization sessions.
      - Relying Party
      - Security
      - Flow Management
    * - REMFLOW-11
      - The Relying Party MUST provide the user-agent with a JavaScript page inspecting the status endpoint.
      - Relying Party
      - Security
      - Flow Management
    * - REMFLOW-12
      - The Wallet Instance MUST extract the ``client_id``, ``request_uri``, ``state``, and optionally the ``request_uri_method``, parameters from the payload.
      - Wallet Instance
      - Security
      - Request Processing
    * - REMFLOW-13
      - The Wallet Instance MUST establish trust with the Relying Party before evaluating the request payload.
      - Wallet Instance
      - Security
      - Trust Establishment
    * - REMFLOW-14
      - If ``request_uri_method`` is set with the value ``get`` or not present, the Wallet Instance MUST fetch the signed Request Object using an HTTP request with method GET to the endpoint provided in the ``request_uri`` parameter.
      - Wallet Instance
      - Security
      - Request Processing
    * - REMFLOW-15
      - If ``request_uri_method`` is provided and set with the value ``post``, the Wallet Instance SHOULD transmit its capabilities (wallet metadata) to the Relying Party's ``request_uri`` endpoint using the HTTP POST method.
      - Wallet Instance
      - Privacy
      - Request Processing
    * - REMFLOW-16
      - The Wallet Instance MUST verify the signature of the signed Request Object using the verified public key, identified in the JWT header of the Request Object and in the trust chain related to the Relying Party.
      - Wallet Instance
      - Security
      - Request Validation
    * - REMFLOW-17
      - The Wallet Instance MUST verify that the ``client_id`` contained in the Request Object issuer matches with the one obtained at step 2 and with the Relying Party's identifier within the Trust Chain.
      - Wallet Instance
      - Security
      - Request Validation
    * - REMFLOW-18
      - The Wallet Instance MUST evaluate the requested Digital Credentials and check the eligibility of the Relying Party in asking for these by applying the policies related to that specific Relying Party.
      - Wallet Instance
      - Privacy
      - Policy Enforcement
    * - REMFLOW-19
      - The Wallet Instance MUST ask for User disclosure and consent by showing the Relying Party's identity and the requested attributes.
      - Wallet Instance
      - Privacy
      - User Consent
    * - REMFLOW-20
      - The Wallet Instance MUST ensure secure transmission of all sensitive data.
      - Wallet Instance
      - Security
      - Data Transmission
    * - REMFLOW-21
      - The Wallet Instance MUST present the requested information and Wallet Attestation (if requested) to the Relying Party, including it within the ``vp_token`` object.
      - Wallet Instance
      - Security
      - Credential Presentation
    * - REMFLOW-22
      - The Wallet Instance MUST inform the User about the successful authentication with the Relying Party.
      - Wallet Instance
      - Privacy
      - User Communication
    * - REMFLOW-23
      - The ``redirect_uri`` value MUST be used with an HTTP method GET by the user-agent to redirect the User to a specific Relying Party's endpoint.
      - User Agent
      - Security
      - Flow Completion
    * - REMFLOW-24
      - The Relying Party MUST validate the presented Credentials by verifying the trust with their Issuers and check the Wallet Attestation (if previously requested and made available by the Wallet Instance) to ensure the Wallet Provider is trusted.
      - Relying Party
      - Security
      - Credential Validation
    * - REMFLOW-25
      - The Relying Party MUST validate that the response comes from the same Wallet Instance that initiated the flow.
      - Relying Party
      - Security
      - Response Validation
    * - REMFLOW-26
      - The Relying Party MUST verify the integrity and authenticity of all received messages.
      - Relying Party
      - Security
      - Response Validation
    * - REMFLOW-27
      - The Relying Party MUST validate that all requested attributes are present in the response.
      - Relying Party
      - Security
      - Response Validation
    * - REMFLOW-28
      - The Relying Party MUST validate the format and structure of received Verifiable Presentations.
      - Relying Party
      - Security
      - Response Validation
    * - REMFLOW-29
      - The Relying Party MUST validate the cryptographic proofs in received Verifiable Presentations.
      - Relying Party
      - Security
      - Response Validation
    * - REMFLOW-30
      - The Relying Party MUST verify the validity period of presented Credentials.
      - Relying Party
      - Security
      - Credential Validation
    * - REMFLOW-31
      - The Relying Party MUST check Credential revocation status when applicable.
      - Relying Party
      - Security
      - Credential Validation
    * - REMFLOW-32
      - The Relying Party MUST validate that the response is properly encrypted.
      - Relying Party
      - Security
      - Response Validation
    * - REMFLOW-33
      - The Relying Party MUST validate that the response matches the original request parameters.
      - Relying Party
      - Security
      - Response Validation
    * - REMFLOW-34
      - The Relying Party MUST validate the format and structure of the authorization response.
      - Relying Party
      - Security
      - Response Validation
    * - REMFLOW-35
      - The Relying Party MUST ensure proper error reporting to the User in case of verification failures.
      - Relying Party
      - Privacy
      - Error Handling
    * - REMFLOW-36
      - Relying Party MUST implement the error handling and validation mechanisms for Redirect URIs defined in this specification.
      - Relying Party
      - Security
      - Error Handling
    * - REMFLOW-37
      - The error response MUST use ``application/json`` as the content type.
      - Relying Party
      - Security
      - Error Handling
    * - REMFLOW-38
      - The error response MUST include the ``error`` and ``error_description`` parameters.
      - Relying Party
      - Security
      - Error Handling
    * - REMFLOW-39
      - The specified HTTP Status Codes and related error codes MUST be supported for the error response.
      - Relying Party
      - Security
      - Error Handling
    * - REMFLOW-40
      - The Relying Party MUST implement proper timeout handling for presentation flows.
      - Relying Party
      - Security
      - Flow Management
    * - REMFLOW-41
      - The Relying Party MUST ensure proper cleanup of temporary presentation data.
      - Relying Party
      - Security
      - Flow Management
    * - REMFLOW-42
      - The Relying Party MUST implement proper cleanup of expired Request Objects.
      - Relying Party
      - Security
      - Flow Management
    * - REMFLOW-43
      - The Relying Party MUST implement proper audit logs of all credential verification attempts.
      - Relying Party
      - Security
      - Audit & Compliance
    * - REMFLOW-44
      - The Relying Party MUST implement proper security logs of verification outcomes.
      - Relying Party
      - Security
      - Audit & Compliance


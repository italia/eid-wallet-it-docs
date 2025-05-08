.. include:: ../common/common_definitions.rst

Credential Issuance Low-Level Flows
====================================

Low-Level Issuance Flow
-----------------------

The Credential Issuance flow is based on [`OpenID4VCI`_] and the following main reference standards/specifications MUST be supported on top of `OpenID4VCI`_:

  * **The OAuth 2.0 Authorization Framework** [:rfc:`6749`], as recommended in Section 3 of [`OpenID4VCI`_].
  * **Pushed Authorization Requests** (PAR) [:rfc:`9126`], as recommended in Section 5 of [`OpenID4VCI`_].
  * **Proof Key for Code Exchange** (PKCE) [:rfc:`7636`], as recommended in Section 5 of [`OpenID4VCI`_].
  * **JWT Authorization Requests** (JAR) [:rfc:`9101`].
  * **JWT Authorization Response Modes** (JARM) [`JARM`_].
  * **Rich Authorization Requests** (RAR) [:rfc:`9396`].
  * **OAuth 2.0 Attestation-Based Client Authentication** [`OAUTH-ATTESTATION-CLIENT-AUTH`_].
  * **OpenID Federation 1.0** [`OID-FED`_].

The Credential Issuer MUST use *OAuth 2.0 Authorization Server* based on :rfc:`6749` to authorize the User to obtain a Credential. Credential Issuers MUST support:

  * **Authorization Code Flow**: The Credential Issuer requires User authentication and consent at the Authorization Endpoint before collecting User information to create and provide a Credential.
  * **Wallet Initiated Flow**: The request from the Wallet Instance is sent to the Credential Issuer without any input from the Credential Issuer.
  * **Immediate Issuance flow**: The Credential Issuer issues the Credential directly in response to the Credential Request.

In addition, the Credential Issuers MAY support:

  * **Issuer Initiated Flow**: The Wallet Instance sends its request to the Credential Issuer based on the input provided by the Credential Issuer.

    * **Same-device Issuance flow**: The User receives the Credential on the same device used to initiate the flow.
    * **Cross-device Issuance flow**: The User receives the Credential on another device than the one that initiated the flow.

  * **Refresh Token flow**: The Wallet Instance requests a new Access Token at the Token Endpoint of the PID/(Q)EEA.
  * **Re-issuance flow**: Following updates to an already stored Digital Credential, the Wallet Instance requests a refresh of the Digital Credential at the Credential Endpoint of the Credential Issuer.
  * **Deferred Issuance flow**: The Credential Issuer may require time to issue the requested Digital Credential, due to the Authentic Sources data provisioning rules, and allows the Wallet to retrieve the requested Credential in the future.

The entire Issuance flow can be divided into two sub-flows:

  - **User Request flow**, describing the modes through which the User can request the Credential. It can be:

      **1)** On the initiative of the User (**Wallet Initiated**).

      **2)** Upon proposal of the Credential Issuer (**Issuer Initiated**).

  - **Issuance flow**, describing interactions between Wallet Instance and Credential Issuer.

The following diagram shows the *User request flow*.

.. _fig_Low-Level-Flow-ITWallet-PID-QEAA-User-Request:
.. figure:: ../../images/Low-Level-Flow-ITWallet-PID-QEAA-User-Request.svg
    :figwidth: 100%
    :align: center
    :target: https://www.plantuml.com/plantuml/svg/hP9FJzj04CNlyob6uT3sG14zve20XAgHAWKA5PTUrkknFMAzQ-sV6BvzPpTkapHLAoGkLkJClFTxptCPel8nzGPKYiwclYAFvn_F0GPvpve7PIFElWVoCrG14q3bdhSltWKClKmDdRCqmvElt7RnsYGwtBtsRlorNld3_nwLCHHnPGN3QYep8v2jKLmEhUWvahVAO4qRrjblxPLj_sb6Ewc3gOMdccnaKLk5aAPv1b0c8ZVu6ujb9bADduqR0HAUNk0un_L05cD7-0S-gc7uOOtJefk40gNJBlje5TbPK3hoHlGaufYbqXnT5HLRV779uv9RZhAweykEMyiN2W3UEbbs6r4UyUJno-hX1jP5eD0O3X5TKtu_-1Go-57Ia2ifGW3ZwOKWQ6SRzdrP2sH8PrRHETu5I88ZDEu9eAQzE40ca3Gt3HurjtTSd_9nbIPvQl9sjJnxV_VXxERg2c-zst2T0r8LM23vDKNnLDJq6HVUXO3BSYyJI96hFCsnYxt1GRM2px73ksyBLrCk8_kmRVVZhvj6qilQ17FVkJ7tDMqLcOpmjkSnYf5MLammkm3iQhvNFVqrs56kpbFpdrHJA6rOFnNkibEb60KAtZHNFhxjur8UgJS_0G00


**Steps 1.1-1.4 (Wallet Initiated Flow):** The User, using the Wallet Instance, selects the Credential Issuer from those listed in the list of trustworthy entities.

**Steps 2.1-2.3 (Issuer Initiated Flow):** The User while browsing the Credential Issuer website finds a link to obtain a Digital Credential.

**Steps 2.4-2.7 (Cross-Device):** The Credential Offer is presented as a QR Code displayed to the User. The User scans the QR Code using the Wallet Instance which retrieves the parameters defined in the :ref:`Table of Credential Offer parameters <table_credential_offer_claim>`.

**Steps 2.8-2.10 (Same-Device):** The Credential Offer is presented as an href button containing the URL that allows the User to invoke the Wallet Instance using the Credential Offer Endpoint.

Below a non-normative example of a URL related to a Credential Offer that can be included in a QR Code or in html page with an href button:

.. code-block:: text

  openid-credential-offer://?credential_offer%3D%7B%22credential_issuer%22%3A%22https%3A%2F%2Feaa-provider.example.org%22%2C%22credential_configuration_ids%22%3A%5B%22dc_sd_jwt_EuropeanDisabilityCard%22%5D%2C%22grants%22%3A%7B%22authorization_code%22%3A%7B%22issuer_state%22%3A%22oaKazRN8I0IbtZ0C7JuMn5%22%7D%7D%7D


The following diagram shows the *Issuance flow*.

.. _fig_Low-Level-Flow-ITWallet-PID-QEAA-Issuance:
.. figure:: ../../images/Low-Level-Flow-ITWallet-PID-QEAA-Issuance.svg
    :figwidth: 100%
    :align: center
    :target: https://www.plantuml.com/plantuml/svg/hLPVRo8t47_tfnZb7XeaKAgsJoTTTOJG2sgKq9HJNYeXnpl0A8kzjSTmwQUlFLdmGaYhg9MYxAxd_-ytC-PpOEqvhckb8piRru_ebMhI6Hbgj6Ku-nhGdu4E49LwTDzU3huB4DP9gravYsVmuOQMAxwi8nxQNdgttPlhGzc3hcjacDZ0sXeKdQr2Mq6ASfJ3o6E5badNC0aXjXv9AMyT8xWDUjZsAUKn-N8z-t8_7j-gqGhD4xoo10gGVODR0AyGVabohvcS1PrYkqVMP84um1fPLvfrpadYABM5mS-mXOzWF6f6cFuw6eDn5KBAW1Q4Nfmy30TJDstLAQbFX_TmZtz630pdVrW0KnDQdbFLpr_-HTI3_B4bNi7TCF9gC1AjmP0vIKkERmbpK20hPLsZJdLryJc5Jil1rBiDLV-8JMiGQ6arHu-joix3KOg2tqRNL14_GmT0HJ0G27UOXCRPW73UGZ2Fdlg0tnho6EPaUqfGJ2PHVuHSj_FqbyGfW1OmeUEcfw8MItgteT8rTpldqoUOJguEmEn7-F1mFPcDLGoPzHGWAvkN2CBXY71o1JTk2DTfEk3yviUUO6DonJQ5TqrMJW0-fxC4es6oIuWoNbcBjU7GA-XX7V0ehVFVUkFXiFVUr58r_p4LM-suZ1gE0IwqvjdeG-wCzA0GzgHitsLK1c-95dqIm5LkzYTyVbFMUESMdN64XVCdrW6x9xIGwcaSMLQTePqbIMaMmQtZMCPuwRNbEJytA7ES4YylyzrAQ4Uy8ez66apc_7yTSqM2GKbwZwKs1aEOIvMvonSUmshtAGz9_t3c2WQtpXhSOt0zcqrXUlVx32vi5fIuEyN2uLmqUgzsPWjV-cjS21W2ENkeVgHVC7-3GRC_AJIM2eh-2Igxw0ZcNOABtpd9Y-ntrmquDyukQ1cz42EBH8nVhn0Ae3UQQlrO8wW2N5Ude5SYX3vObqERNOWkf6cEBrvMGDcsgGoPdHZ0v9tTgiUahiEJO9XlyDtigzWwsnq0EmZiF4g3bKnAM14VYKh3b6HFzarNVdvKMXzmWrRkmGv9Go7ffRFLgHljykRhMDtZaWAdKrtNHvaFFDQQiG95DfM_bd02HFAoZt_XSUFQnCgLLPWwAArm9RNzyFrFIGmZPpb3MZPrOV_sRbOwu5_ehr5NSwOrze6zja6R7VVTycEVr2mLUlH3gWzw8JXOq6iNhTpcsHc41arkuWeUds4VGnfckq8Bx6cvH2_o3A7qYInYpq4E5hNRWbvgieTNmUVqBwxhlm40

    Credential Issuance - Detailed flow


Once *User Request flow* is completed, the Wallet Instance processes the Metadata of the Credential Issuer as defined in Section :ref:`trust:Trust Evaluation Mechanism` .

.. note::
  **Federation Check:** The Wallet Instance must verify whether the Credential Issuer is a member of the Federation, obtaining its protocol specific Metadata. A non-normative example of a response from the endpoint **.well-known/openid-federation** with the **Entity Configuration** and the **Metadata** of the Credential Issuer is represented within the section :ref:`credential-issuer-entity-configuration:Entity Configuration of Credential Issuers`.

In case of Issuer Initiated flow, in addition to the Federation Check defined above, the Wallet Instance MUST execute the following checks on the Credential Offer parameters:

  * For each Credential identifier contained in the ``credential_configuration_ids`` array verify if it is supported by the Credential Issuer.
  * The Authorization Server identifier (if present) is contained in the ``authorization_servers`` Credential Issuer metadata parameter.


**Steps 1-2 (PAR Request)**: The Wallet Instance:

  * creates a fresh PKCE code verifier, Wallet Attestation Proof of Possession, and ``state`` parameter for the *Pushed Authorization Request*.
  * provides to the Credential Issuer PAR endpoint the parameters previously listed above, using the ``request`` parameter (hereafter Request Object) according to :rfc:`9126` Section 3 to prevent Request URI swapping attack. The Pushed Authorization Request enables client authentication prior to any User interaction. This step allows for the early rejection of illegitimate requests, effectively preventing spoofing attacks, tampering, and improper use of authorization requests.
  * MUST create the ``code_verifier`` with enough entropy random string using the unreserved characters with a minimum length of 43 characters and a maximum length of 128 characters, making it impractical for an attacker to guess its value. The value MUST be generated following the recommendation in Section 4.1 of :rfc:`7636`.
  * signs this request using the private key that is created during the setup phase to obtain the Wallet Attestation. The related public key that is attested by the Wallet Provider is provided within the Wallet Attestation ``cnf.jwk`` claim.
  * MUST use the ``OAuth-Client-Attestation`` and ``OAuth-Client-Attestation-PoP`` parameters according to OAuth 2.0 Attestation-based Client Authentication [`OAUTH-ATTESTATION-CLIENT-AUTH`_], since in this flow the Pushed Authorization Endpoint is a protected endpoint.
  * specifies the types of the requested credentials using the ``authorization_details`` [RAR :rfc:`9396`] parameter and or scope parameter.

The Credential Issuer performs the following checks upon the receipt of the PAR request:

    1. It MUST validate the signature of the Request Object using the algorithm specified in the ``alg`` header parameter (:rfc:`9126`, :rfc:`9101`) and the public key retrieved from the Wallet Attestation (``cnf.jwk``) referenced in the Request Object, using the ``kid`` JWT header parameter.
    2. It MUST check that the used algorithm for signing the request in the ``alg`` header is one of the listed within the Section :ref:`algorithms:Cryptographic Algorithms`.
    3. It MUST check that the ``client_id`` in the request body of the PAR request matches the ``client_id`` claim included in the Request Object.
    4. It MUST check that the ``iss`` claim in the Request Object matches the ``client_id`` claim in the Request Object (:rfc:`9126`, :rfc:`9101`).
    5. It MUST check that the ``aud`` claim in the Request Object is equal to the identifier of the Credential Issuer (:rfc:`9126`, :rfc:`9101`).
    6. It MUST reject the PAR request, if it contains the ``request_uri`` parameter (:rfc:`9126`).
    7. It MUST check that the Request Object contains all the mandatory parameters which values are validated according to :ref:`Table of the HTTP parameters <table_request_object_claim>` [derived from :rfc:`9126`].
    8. It MUST check that the Request Object is not expired, checking the ``exp`` claim.
    9. It MUST check that the Request Object was issued in a previous time than the value exposed in the ``iat`` claim. It SHOULD reject the request if the ``iat`` claim is far from the current time (:rfc:`9126`) of more than `5` minutes.
    10. It MUST check that the ``jti`` claim in the Request Object has not been used before by the Wallet Instance identified by the ``client_id``. This allows the Credential Issuer to mitigate replay attacks (:rfc:`7519`).
    11. It MUST validate the ``OAuth-Client-Attestation-PoP`` parameter based on Section 4 of [`OAUTH-ATTESTATION-CLIENT-AUTH`_].

Below a non-normative example of the PAR.

.. code-block:: http

    POST /as/par HTTP/1.1
    Host: eaa-provider.example.org
    Content-Type: application/x-www-form-urlencoded
    OAuth-Client-Attestation: eyJhbGciOiJFUzI1NiIsImtpZCI6IjBiNDk4ZGRlMDkxNzJhZGE3MDFkMDdlYjZmOTg2N2FkIiwidHlwIjoid2FsbGV0LWF0dGVzdGF0aW9uK2p3dCJ9.eyJpc3MiOiJodHRwczovL3dhbGxldC1wcm92aWRlci5leGFtcGxlLm9yZyIsInN1YiI6InZiZVhKa3NNNDV4cGh0QU5uQ2lHNm1DeXVVNGpmR056b3BHdUt2b2dnOWMiLCJhYWwiOiJodHRwczovL3RydXN0LWxpc3QuZXUvYWFsL2hpZ2giLCJjbmYiOnsiandrIjp7ImNydiI6IlAtMjU2Iiwia3R5IjoiRUMiLCJ4IjoiNEhOcHRJLXhyMnBqeVJKS0dNbno0V21kblFEX3VKU3E0Ujk1Tmo5OGI0NCIsInkiOiJMSVpuU0IzOXZGSmhZZ1MzazdqWEU0cjMtQ29HRlF3WnRQQklScXBObHJnIn19LCJhdXRob3JpemF0aW9uX2VuZHBvaW50IjoiaHR0cHM6Ly93YWxsZXQtc29sdXRpb24uZGlnaXRhbC1zdHJhdGVneS5ldXJvcGEuZXUvYXV0aG9yaXphdGlvbiIsInJlc3BvbnNlX3R5cGVzX3N1cHBvcnRlZCI6WyJ2cF90b2tlbiJdLCJyZXNwb25zZV9tb2Rlc19zdXBwb3J0ZWQiOlsiZm9ybV9wb3N0Lmp3dCJdLCJ2cF9mb3JtYXRzX3N1cHBvcnRlZCI6eyJkYytzZC1qd3QiOnsic2Qtand0X2FsZ192YWx1ZXMiOlsiRVMyNTYiLCJFUzM4NCJdfX0sInJlcXVlc3Rfb2JqZWN0X3NpZ25pbmdfYWxnX3ZhbHVlc19zdXBwb3J0ZWQiOlsiRVMyNTYiXSwicHJlc2VudGF0aW9uX2RlZmluaXRpb25fdXJpX3N1cHBvcnRlZCI6ZmFsc2UsImNsaWVudF9pZF9zY2hlbWVzX3N1cHBvcnRlZCI6WyJlbnRpdHlfaWQiXSwiaWF0IjoxNzQwMTU4MDQ3LCJleHAiOjE3NDAxNTgxNjd9.paU3FOET8nraQxuesBXD9gw57DL5HfDzkeboKAOinyh5L2MmLwqvRtrSWK8S7qMRWYmdzR-gHMpmebIH7gGE5w
    OAuth-Client-Attestation-PoP: eyJhbGciOiJFUzI1NiIsInR5cCI6Im9hdXRoLWNsaWVudC1hdHRlc3RhdGlvbi1wb3Arand0In0.eyJpc3MiOiIgaHR0cHM6Ly9jbGllbnQuZXhhbXBsZS5jb20iLCJhdWQiOiJodHRwczovL2FzLmV4YW1wbGUuY29tIiwianRpIjoiZDI1ZDAwYWItNTUyYi00NmZjLWFlMTktOThmNDQwZjI1MDY0IiwiaWF0IjoxNzQwMTU4NjE3LCJleHAiOjE3NDAxNTg3Mzd9.B0KOkGi9vMxf3H2Y8rrF-mdLNsuluTvAUbjFfL1Hi-gdaPW7-8ziS9uVh7aTnSAHKWzMfkZLv5q-bxhkglR4PA

    client_id=$thumprint-of-the-jwk-in-the-cnf-wallet-attestation$&
    request=$SIGNED-JWT

Below an non-normative example of the Wallet Attestation Proof of Possession (WIA-PoP) header and body:

.. literalinclude:: ../../examples/wa-pop-header.json
  :language: JSON

.. literalinclude:: ../../examples/wa-pop-payload.json
  :language: JSON


Below an non-normative example of the signed Request Object without encoding and signature applied:

.. literalinclude:: ../../examples/request-object-header.json
  :language: JSON

.. literalinclude:: ../../examples/request-object-payload.json
  :language: JSON


.. note::
  **Federation Check**: The Credential Issuer MUST check that the Wallet Provider is part of the federation.


.. note::
  The Credential Issuer MUST validate the signature of the Wallet Attestation and that it is not expired.

**Step 3 (PAR Response)**: The Credential Issuer provides a one-time use ``request_uri`` value. The issued ``request_uri`` value MUST be bound to the client identifier (``client_id``) that was provided in the Request Object.


.. note::
  The entropy of the ``request_uri`` MUST be sufficiently large. The adequate shortness of the validity and the entropy of the ``request_uri`` depends on the risk calculation based on the value of the resource being protected. The validity time SHOULD be less than a minute, and the ``request_uri`` MUST include a cryptographic random value of 128 bits or more (:rfc:`9101`). The entire ``request_uri`` SHOULD NOT exceed 512 ASCII characters due to the following two main reasons (:rfc:`9101`):

    1. Many phones on the market still do not accept large payloads. The restriction is typically either 512 or 1024 ASCII characters.
    2. On a slow connection such as a 2G mobile connection, a large URL would cause a slow response; therefore, the use of such is not advisable from the user-experience point of view.

The Credential Issuer returns the issued ``request_uri`` to the Wallet Instance. A non-normative example of the response is shown below.

.. code-block:: http

  HTTP/1.1 201 Created
  Cache-Control: no-cache, no-store
  Content-Type: application/json

.. literalinclude:: ../../examples/par-response.json
  :language: JSON

**Steps 4-5 (Authorization Request)**: The Wallet Instance sends an authorization request to the Credential Issuer Authorization Endpoint. Since parts of this Authorization Request content, e.g., the ``code_challenge`` parameter value, are unique to a particular Authorization Request, the Wallet Instance MUST use a ``request_uri`` value once (:rfc:`9126`); The Credential Issuer performs the following checks upon the receipt of the Authorization Request:

    1. It MUST treat ``request_uri`` values as one-time use and MUST reject an expired request. However, it MAY allow for duplicate requests due to a User reloading/refreshing their user-agent (derived from :rfc:`9126`).
    2. It MUST identify the request as a result of the submitted PAR (derived from :rfc:`9126`).
    3. It MUST reject all the Authorization Requests that do not contain the ``request_uri`` parameter as the PAR is the only way to pass the Authorization Request from the Wallet Instance (derived from :rfc:`9126`).


.. code-block:: http

    GET /authorize?client_id=$thumprint-of-the-jwk-in-the-cnf-wallet-attestation$&request_uri=urn%3Aietf%3Aparams%3Aoauth%3Arequest_uri%3Abwc4JK-ESC0w8acc191e-Y1LTC2 HTTP/1.1
    Host: eaa-provider.example.org


.. note::
   **User Authentication and Consent**: The PID Provider performs the User authentication based on CieID scheme with LoA High (CIE L3) and requires the User consent for the PID issuance.
   The (Q)EAA Provider performs the User authentication requesting a valid PID to the Wallet Instance. The (Q)EAA Provider MUST use [`OpenID4VP`_] to request the presentation of the PID. In this circumstance, the (Q)EAA Provider acts as a Relying Party, providing the presentation request to the Wallet Instance. The Wallet Instance MUST have a valid PID, obtained beforehand, to initiate the transaction with the (Q)EAA Provider. During this step, Credential Issuers MAY ask the User's contact details (e.g., their email address) to send notifications about the issued Digital Credential(s).



**Steps 6-7 (Authorization Response)**: The Credential Issuer sends an authorization ``code`` together with ``state`` and ``iss`` parameters to the Wallet Instance. The Wallet Instance performs the following checks on the Authorization Response:

    1. It MUST check the Authorization Response contains all the defined parameters according to :ref:`Table of the HTTP Response parameters <table_http_response_claim>`.
    2. It MUST check the returned value by the Credential Issuer for ``state`` parameter is equal to the value sent by Wallet Instance in the Request Object (:rfc:`6749`).
    3. It MUST check that the URL of Credential Issuer in ``iss`` parameter is equal to the URL identifier of intended Credential Issuer that the Wallet Instance start the communication with (:rfc:`9027`).

.. note::
    The Wallet Instance redirect URI is a universal or app link registered with the local operating system, so this latter will resolve it and pass the response to the Wallet Instance.

.. code-block:: http

    HTTP/1.1 302 Found
    Location: https://start.wallet.example.org?code=SplxlOBeZQQYbYS6WxSbIA&state=fyZiOL9Lf2CeKuNT2JzxiLRDink0uPcd&iss=https%3A%2F%2Feaa-provider.example.org

**Steps 8-9 (DPoP Proof for Token Endpoint)**: The Wallet Instance MUST create a new key pair for the DPoP and a fresh DPoP Proof JWT following the instruction provided in the Section 4 of (:rfc:`9449`) for the token request to the Credential Issuer. The DPoP Proof JWT is signed using the private key for DPoP created by Wallet Instance for this scope. DPoP binds the Access Token, and optionally the Refresh Token, to a certain Wallet Instance (:rfc:`9449`) and mitigates the misuse of leaked or stolen tokens at the Credential Endpoint.

**Step 10 (Token Request):** The Wallet Instance sends a token request to the Credential Issuer Token Endpoint with a *DPoP Proof JWT* and the parameters: ``code``, ``code_verifier``, and OAuth 2.0 Attestation based Client Authentication (``OAuth-Client-Attestation`` and ``OAuth-Client-Attestation-PoP``).

The ``OAuth-Client-Attestation`` is signed using the private key bound to the Wallet Instance. The related public key that is attested by the Wallet Provider is provided within the Wallet Attestation (``cnf.jwk`` claim). The Credential Issuer performs the following checks on the Token Request:

   1. It MUST ensure that the Authorization ``code`` is issued to the authenticated Wallet Instance (:rfc:`6749`) and was not replied.
   2. It MUST ensure the Authorization ``code`` is valid and has not been previously used (:rfc:`6749`).
   3. It MUST ensure the ``redirect_uri`` matches the value included in the previous Request Object (see Section 3.1.3.1. of [`OIDC`_]).
   4. It MUST validate the DPoP Proof JWT, according to (:rfc:`9449`) Section 4.3.

.. code-block:: http

    POST /token HTTP/1.1
    Host: eaa-provider.example.org
    Content-Type: application/x-www-form-urlencoded
    DPoP: eyJ0eXAiOiJkcG9wK2p3dCIsImFsZyI6IkVTMjU2IiwiandrIjp7Imt0eSI6IkVDIiwieCI6IjR2dDhNdEFISmlsMzBDNnpUTmt2c0VVcnlHTEUtQW5BNkc5LV8xa3l5Rk0iLCJ5IjoiTWdiNTFfbjNSRjNtbHNtS3dMd0xtRUFqVmlJM3Q1bTVWNTI2MFA5MzR3RSIsImNydiI6IlAtMjU2In19.eyJqdGkiOiItQndDM0VTYzZhY2MybFRjIiwiaHRtIjoiR0VUIiwiaHR1IjoiaHR0cHM6Ly9yZXNvdXJjZS5leGFtcGxlLm9yZy9wcm90ZWN0ZWRyZXNvdXJjZSIsImlhdCI6MTU2MjI2MjYxOH0.3Tp1ZlZ05PQYeZUHhiZwaQ1etqnwYwoiJHFR_JHb32381lMJL-8o2rE3VZ8X3yuqrGFfCVeP90Ln4J5r8ASIBg
    OAuth-Client-Attestation: eyJhbGciOiJFUzI1NiIsImtpZCI6IjBiNDk4ZGRlMDkxNzJhZGE3MDFkMDdlYjZmOTg2N2FkIiwidHlwIjoid2FsbGV0LWF0dGVzdGF0aW9uK2p3dCJ9.eyJpc3MiOiJodHRwczovL3dhbGxldC1wcm92aWRlci5leGFtcGxlLm9yZyIsInN1YiI6InZiZVhKa3NNNDV4cGh0QU5uQ2lHNm1DeXVVNGpmR056b3BHdUt2b2dnOWMiLCJhYWwiOiJodHRwczovL3RydXN0LWxpc3QuZXUvYWFsL2hpZ2giLCJjbmYiOnsiandrIjp7ImNydiI6IlAtMjU2Iiwia3R5IjoiRUMiLCJ4IjoiNEhOcHRJLXhyMnBqeVJKS0dNbno0V21kblFEX3VKU3E0Ujk1Tmo5OGI0NCIsInkiOiJMSVpuU0IzOXZGSmhZZ1MzazdqWEU0cjMtQ29HRlF3WnRQQklScXBObHJnIn19LCJhdXRob3JpemF0aW9uX2VuZHBvaW50IjoiaHR0cHM6Ly93YWxsZXQtc29sdXRpb24uZGlnaXRhbC1zdHJhdGVneS5ldXJvcGEuZXUvYXV0aG9yaXphdGlvbiIsInJlc3BvbnNlX3R5cGVzX3N1cHBvcnRlZCI6WyJ2cF90b2tlbiJdLCJyZXNwb25zZV9tb2Rlc19zdXBwb3J0ZWQiOlsiZm9ybV9wb3N0Lmp3dCJdLCJ2cF9mb3JtYXRzX3N1cHBvcnRlZCI6eyJkYytzZC1qd3QiOnsic2Qtand0X2FsZ192YWx1ZXMiOlsiRVMyNTYiLCJFUzM4NCJdfX0sInJlcXVlc3Rfb2JqZWN0X3NpZ25pbmdfYWxnX3ZhbHVlc19zdXBwb3J0ZWQiOlsiRVMyNTYiXSwicHJlc2VudGF0aW9uX2RlZmluaXRpb25fdXJpX3N1cHBvcnRlZCI6ZmFsc2UsImNsaWVudF9pZF9zY2hlbWVzX3N1cHBvcnRlZCI6WyJlbnRpdHlfaWQiXSwiaWF0IjoxNzQwMTU4MDQ3LCJleHAiOjE3NDAxNTgxNjd9.paU3FOET8nraQxuesBXD9gw57DL5HfDzkeboKAOinyh5L2MmLwqvRtrSWK8S7qMRWYmdzR-gHMpmebIH7gGE5w
    OAuth-Client-Attestation-PoP: eyJhbGciOiJFUzI1NiIsInR5cCI6Im9hdXRoLWNsaWVudC1hdHRlc3RhdGlvbi1wb3Arand0In0.eyJpc3MiOiIgaHR0cHM6Ly9jbGllbnQuZXhhbXBsZS5jb20iLCJhdWQiOiJodHRwczovL2FzLmV4YW1wbGUuY29tIiwianRpIjoiZDI1ZDAwYWItNTUyYi00NmZjLWFlMTktOThmNDQwZjI1MDY0IiwiaWF0IjoxNzQwMTU4NjE3LCJleHAiOjE3NDAxNTg3Mzd9.B0KOkGi9vMxf3H2Y8rrF-mdLNsuluTvAUbjFfL1Hi-gdaPW7-8ziS9uVh7aTnSAHKWzMfkZLv5q-bxhkglR4PA

    grant_type=authorization_code
    &code=SplxlOBeZQQYbYS6WxSbIA
    &code_verifier=dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk
    &redirect_uri=https://start.wallet.example.org/cb

**Step 11 (Token Response)**: The Credential Issuer validates the request. If successful, the Issuer provides the Wallet Instance with an Access Token and, optionally, a Refresh Token, both bound to the DPoP key.

.. code-block:: http

    HTTP/1.1 200 OK
    Content-Type: application/json
    Cache-Control: no-store

.. literalinclude:: ../../examples/token-response.json
  :language: JSON

The non-normative example of the DPoP Access Token is given below.

.. literalinclude:: ../../examples/at-dpop-header.json
  :language: JSON

.. literalinclude:: ../../examples/at-dpop-payload.json
  :language: JSON

The non-normative example of the DPoP Refresh Token is given below.

.. literalinclude:: ../../examples/rt-dpop-header.json
  :language: JSON

.. literalinclude:: ../../examples/rt-dpop-payload.json
  :language: JSON

**Step 12 (Nonce Request)**: According to Section 7.1 of [`OpenID4VCI`_], the Wallet Instance sends an HTTP POST request to the Nonce Endpoint to obtain a fresh ``c_nonce`` that can be used to create the proof of possession of key material for the subsequent request to the Credential Endpoint.

Below is a non-normative example of a Nonce Request:

.. code-block:: http

    POST /nonce HTTP/1.1
    Host: eaa-provider.example.org
    Content-Length: 0

**Step 13 (Nonce Response)**: The Credential Issuer provides the `c_nonce` to the Wallet Instance. The parameter `c_nonce` is a string value, which MUST be unpredictable and is used later by the Wallet Instance in Step 16 to create the proof of possession of the key (*proof* claim) and it is the primary countermeasure against key proof replay attack.
Note that, the received `c_nonce` value can be used to create the proof as long as the Issuer
provides the Wallet Instance with a new `c_nonce` value.

Below is a non-normative example of a Nonce Response:

.. code-block:: http

    HTTP/1.1 200 OK
    Content-Type: application/json
    Cache-Control: no-store

.. literalinclude:: ../../examples/nonce-response.json
  :language: JSON


**Steps 14-15 (DPoP Proof for Credential Endpoint)**: The Wallet Instance for requesting the Digital Credential creates a proof of possession with ``c_nonce`` obtained in **Step 13** and using the private key used for the DPoP, signing a DPoP Proof JWT according to (:rfc:`9449`) Section 4. The ``jwk`` value in the ``proof`` parameter MUST be equal to the public key referenced in the DPoP.

**Step 16 (Credential Request)**: The Wallet Instance sends a request for the Digital Credential to the Credential endpoint. This request MUST include the Access Token, DPoP Proof JWT, credential type, proof (which demonstrates possession of the key). The proof parameter MUST be an object that contains evidence of possession of the cryptographic key material to which the issued Digital Credential will be bound. To verify the proof, the Credential Issuer conducts the following checks at the Credential endpoint:

 1. the JWT proof MUST include all required claims as specified in the table of Section :ref:`credential-issuance-endpoint:Token Request`;
 2. The key proof MUST be explicitly typed using header parameters as defined for the respective proof type;
 3. The header parameter alg MUST indicate a registered asymmetric digital signature algorithm, and MUST NOT be set to `none`;
 4. The signature on the key proof MUST be verified using the public key specified in the header parameter;
 5. The header parameter MUST NOT contain a private key;
 6. If a `c_nonce` value was previously provided by the server, the nonce claim in the JWT MUST match this `c_nonce` value. Furthermore, the creation time of the JWT, as indicated by the `iat` claim or a server-managed timestamp via the nonce claim, MUST be within an acceptable window of time as determined by the server.


.. note::
  **Credential Schema and Status registration**: The Credential Issuer MUST register all the issued Credentials for their later revocation, if needed.


.. note::
  It is RECOMMENDED that the public key contained in the ``jwt_proof`` be specifically generated for the requested Credential (fresh cryptographic key) to ensure that different issued Credentials do not share the same public key, thereby remaining unlinkable to each other.


A non-normative example of the Credential Request is provided below.


.. code-block:: http

  POST /credential HTTP/1.1
    Host: eaa-provider.example.org
  Content-Type: application/json
  Authorization: DPoP Kz~8mXK1EalYznwH-LC-1fBAo.4Ljp~zsPE_NeO.gxU
  DPoP: eyJ0eXAiOiJkcG9wK2p3dCIsImFsZyI6IkVTMjU2IiwiandrIjp7Imt0eSI6Ik
      VDIiwieCI6Imw4dEZyaHgtMzR0VjNoUklDUkRZOXpDa0RscEJoRjQyVVFVZldWQVdCR
      nMiLCJ5IjoiOVZFNGpmX09rX282NHpiVFRsY3VOSmFqSG10NnY5VERWclUwQ2R2R
      1JEQSIsImNydiI6IlAtMjU2In19.eyJqdGkiOiJlMWozVl9iS2ljOC1MQUVCIiwiaHRtIj
      oiR0VUIiwiaHR1IjoiaHR0cHM6Ly9yZXNvdXJjZS5leGFtcGxlLm9yZy9wcm90ZWN0Z
      WRyZXNvdXJjZSIsImlhdCI6MTU2MjI2MjYxOCwiYXRoIjoiZlVIeU8ycjJaM0RaNTNF
      c05yV0JiMHhXWG9hTnk1OUlpS0NBcWtzbVFFbyJ9.2oW9RP35yRqzhrtNP86L-Ey71E
      OptxRimPPToA1plemAgR6pxHF8y6-yqyVnmcw6Fy1dqd-jfxSYoMxhAJpLjA

.. literalinclude:: ../../examples/credential-request.json
  :language: JSON

Where a non-normative example of the decoded content of the ``jwt`` parameter is represented below,
without encoding and signature. The JWT header:

.. literalinclude:: ../../examples/credential-jwt-proof-header.json
  :language: JSON

.. literalinclude:: ../../examples/credential-jwt-proof-payload.json
  :language: JSON

**Steps 17-21 (Credential Response)**: The Credential Issuer MUST validate the *DPoP JWT Proof* based on the steps defined in Section 4.3 of (:rfc:`9449`) and whether the *Access Token* is valid and suitable for the requested Credential. The Credential Issuer MUST validate the proof of possession for the key material the new Credential SHALL be bound to, according to `OpenID4VCI`_ Section 8.2.2. If all checks succeed, the Credential Issuer creates a new Credential bound to the key material and provides it to the Wallet Instance. The Wallet Instance MUST perform the following checks before proceeding with the secure storage of the Credential:

    1. It MUST check that the PID/(Q)EAA contained in the Credential Response contains all the mandatory parameters and values are validated according to :ref:`Table of the Credential response parameters <table_credential_response_claim>`.
    2. It MUST check the credential integrity by verifying the signature using the algorithm specified in the ``alg`` header parameter of SD-JWT (:ref:`credential-data-model:Digital Credential Data Model`) and the public key that is identified using the ``kid`` header of the SD-JWT.
    3. It MUST check that the received Digital Credential (in credential claim) matches the requested credential type and complies with the specific schema of that Credential defined in :ref:`credential-data-model:Digital Credential Data Model`.
    4. It MUST process and verify the Credential in SD-JWT VC format (according to `SD-JWT`_ Section 5.) or mdoc-CBOR format.
    5. It MUST verify the Trust Chain in the header of SD-JWT VC to verify that the Credential Issuer is trusted.

If the checks above are successful, the Wallet Instance requests the User's consent to store the Digital Credential. Upon receiving consent, the Wallet Instance securely stores the Digital Credential.

Below is a non-normative example of a successful response containing a Credential in SD-JWT VC format.

.. code-block:: http

    HTTP/1.1 200 OK
    Content-Type: application/json
    Cache-Control: no-store
    Pragma: no-cache

.. literalinclude:: ../../examples/sd-jwt-credential-response.json
  :language: JSON

Below is a non-normative example of a successful response containing a Credential in mdoc format.

.. code-block:: http

    HTTP/1.1 200 OK
    Content-Type: application/json
    Cache-Control: no-store
    Pragma: no-cache

.. literalinclude:: ../../examples/mdoc-credential-response.json
  :language: JSON


.. note::
  If the requested Credential cannot be issued immediately and requires more time, the Credential Issuer SHOULD support the Deferred Flow (step 24) as specified in Section :ref:`credential-issuance-endpoint:Deferred Endpoint`.

**Step 22 (Notification Request)**: According to Section 10.1 of [`OpenID4VCI`_], the Wallet sends an HTTP POST request to the Notification Endpoint using the *application/json* media type as in the following non-normative example.

.. code-block:: http

  POST /notification HTTP/1.1
  Host: eaa-provider.example.org
  Content-Type: application/json
  Authorization: DPoP Kz~8mXK1EalYznwH-LC-1fBAo.4Ljp~zsPE_NeO.gxU
  DPoP: eyJ0eXAiOiJkcG9wK2p3dCIsImFsZyI6IkVTMjU2IiwiandrIjp7Imt0eSI6Ik
      VDIiwieCI6Imw4dEZyaHgtMzR0VjNoUklDUkRZOXpDa0RscEJoRjQyVVFVZldWQVdCR
      nMiLCJ5IjoiOVZFNGpmX09rX282NHpiVFRsY3VOSmFqSG10NnY5VERWclUwQ2R2R
      1JEQSIsImNydiI6IlAtMjU2In19.eyJqdGkiOiJlMWozVl9iS2ljOC1MQUVCIiwiaHRtIj
      oiR0VUIiwiaHR1IjoiaHR0cHM6Ly9yZXNvdXJjZS5leGFtcGxlLm9yZy9wcm90ZWN0Z
      WRyZXNvdXJjZSIsImlhdCI6MTU2MjI2MjYxOCwiYXRoIjoiZlVIeU8ycjJaM0RaNTNF
      c05yV0JiMHhXWG9hTnk1OUlpS0NBcWtzbVFFbyJ9.2oW9RP35yRqzhrtNP86L-Ey71E
      OptxRimPPToA1plemAgR6pxHF8y6-yqyVnmcw6Fy1dqd-jfxSYoMxhAJpLjA
.. literalinclude:: ../../examples/notification-request.json
  :language: JSON


**Step 23 (Notification Response)**: When the Credential Issuer has successfully received the Notification Request from the Wallet, it MUST respond with an HTTP status code *204* as recommended in Section 10.2 of [`OpenID4VCI`_]. Below is a non-normative example of response to a successful Notification Request:

.. code-block:: http

  HTTP/1.1 204 No Content


Refresh Token Flow
------------------

To use the Deferred, Credential Request, and Notification endpoints, the Wallet Instance MUST present a valid DPoP Access Token to the Credential Issuer. However, when these endpoints are used in the Deferred Flow, for re-issuing or notifying the deletion of a Digital Credential, the Access Token might expire, as it is designed to be short-lived and these actions MAY occur days later. To address this, the specification RECOMMENDS the use of Refresh Tokens.

An Access Token obtained as a result of a Refresh Token flow MUST be limited to:

  - the Deferred endpoint to obtain a new Digital Credential after time set in the parameter ``lead_time`` or when it is notified as ready to be issued;
  - the Notification endpoint, to notify the deletion of a Digital Credential to the Credential Issuer;
  - the Credential endpoint, to refresh a Digital Credential that is already present in the Wallet Instance (also called Digital Credential re-issuance, see section :ref:`credential-issuance-low-level:Re-Issuance Flow`).

To mitigate the impact of a stolen Refresh Token, the Refresh Tokens MUST be DPoP. These aspects are detailed and discussed in Section :ref:`credential-issuance-low-level:Security Considerations`.

Figure below shows how to obtain a new DPoP Access Token and a new DPoP Refresh Token to the Token Endpoint.

.. _fig_refresh_token_flow:
.. figure:: ../../images/Refresh-Token-Flow.svg
    :figwidth: 100%
    :align: center
    :target: https://www.plantuml.com/plantuml/svg/TPBDQkim48NtUef3xYQ1cEpleYIaXMRLK0BP588gZ-EXpiYLnhXz-yfoJ1jAbvwVpzySj8vgWtQNnjXElNINLmh6jAd6ZbihYjdHDWqfTf96nT4CDgA_7Ta6AacKRODTZ1s5FCJ6z2ZkqEC_pYGKh1BkztwFDdXVmKg9uwOO2fKF-0M1-ZSIa9IjPz4hZHFja1lFzDvHLFIizK_k_4M0Sx2Y9_riQJby1ge2nVgKaGkaKjvwsdHQ5zk6IRJOg2QSLVQItVvgPcCMQ4seoPP3OZmTEgd5raiapArp5EFut-Mjnd8yS9G4VRISUYUMXJ6rU2LO5toC-7Tyt1qU4hecL8tluRmeIxfzFC8YN9DGdwLAgYW4AbU9mXMxRBrot_bEaKun34j2_HZYQ3owcNKQJQ_Z2m00

    Refresh Token Flow

.. note::
  The refresh of a Token may be triggered by different actions (e.g., User deletion of a Digital Credential). In each case, Wallet Instances are supposed to be running and the corresponding cryptographic material unlocked.

**Step 1.** The Wallet Instance MUST create a fresh DPoP Proof JWT and a fresh Wallet Attestation proof of possession for the token request of the Credential Issuer.

**Step 2.** To refresh a DPoP-bound Access Token, the Wallet Instance sends a token request using the parameter ``grant_type`` set to ``refresh_token``, including the DPoP header and the OAuth Client Attestation headers.
A non-normative example of the token request for a DPoP Access Token using a Refresh Token is shown below.

.. code::

  POST /token HTTP/1.1
  Host: eaa-provider.example.org
  Content-Type: application/x-www-form-urlencoded
  DPoP: eyJ0eXAiOiJkcG9wK2p3dCIsImFsZyI6IkVTMjU2IiwiandrIjp7Imt0eSI6IkVDIiwieCI6IjR2dDhNdEFISmlsMzBDNnpUTmt2c0VVcnlHTEUtQW5BNkc5LV8xa3l5Rk0iLCJ5IjoiTWdiNTFfbjNSRjNtbHNtS3dMd0xtRUFqVmlJM3Q1bTVWNTI2MFA5MzR3RSIsImNydiI6IlAtMjU2In19.eyJqdGkiOiItQndDM0VTYzZhY2MybFRjIiwiaHRtIjoiR0VUIiwiaHR1IjoiaHR0cHM6Ly9yZXNvdXJjZS5leGFtcGxlLm9yZy9wcm90ZWN0ZWRyZXNvdXJjZSIsImlhdCI6MTU2MjI2MjYxOH0.3Tp1ZlZ05PQYeZUHhiZwaQ1etqnwYwoiJHFR_JHb32381lMJL-8o2rE3VZ8X3yuqrGFfCVeP90Ln4J5r8ASIBg
  OAuth-Client-Attestation: eyJhbGciOiJFUzI1NiIsImtpZCI6IjBiNDk4ZGRlMDkxNzJhZGE3MDFkMDdlYjZmOTg2N2FkIiwidHlwIjoid2FsbGV0LWF0dGVzdGF0aW9uK2p3dCJ9.eyJpc3MiOiJodHRwczovL3dhbGxldC1wcm92aWRlci5leGFtcGxlLm9yZyIsInN1YiI6InZiZVhKa3NNNDV4cGh0QU5uQ2lHNm1DeXVVNGpmR056b3BHdUt2b2dnOWMiLCJhYWwiOiJodHRwczovL3RydXN0LWxpc3QuZXUvYWFsL2hpZ2giLCJjbmYiOnsiandrIjp7ImNydiI6IlAtMjU2Iiwia3R5IjoiRUMiLCJ4IjoiNEhOcHRJLXhyMnBqeVJKS0dNbno0V21kblFEX3VKU3E0Ujk1Tmo5OGI0NCIsInkiOiJMSVpuU0IzOXZGSmhZZ1MzazdqWEU0cjMtQ29HRlF3WnRQQklScXBObHJnIn19LCJhdXRob3JpemF0aW9uX2VuZHBvaW50IjoiaHR0cHM6Ly93YWxsZXQtc29sdXRpb24uZGlnaXRhbC1zdHJhdGVneS5ldXJvcGEuZXUvYXV0aG9yaXphdGlvbiIsInJlc3BvbnNlX3R5cGVzX3N1cHBvcnRlZCI6WyJ2cF90b2tlbiJdLCJyZXNwb25zZV9tb2Rlc19zdXBwb3J0ZWQiOlsiZm9ybV9wb3N0Lmp3dCJdLCJ2cF9mb3JtYXRzX3N1cHBvcnRlZCI6eyJkYytzZC1qd3QiOnsic2Qtand0X2FsZ192YWx1ZXMiOlsiRVMyNTYiLCJFUzM4NCJdfX0sInJlcXVlc3Rfb2JqZWN0X3NpZ25pbmdfYWxnX3ZhbHVlc19zdXBwb3J0ZWQiOlsiRVMyNTYiXSwicHJlc2VudGF0aW9uX2RlZmluaXRpb25fdXJpX3N1cHBvcnRlZCI6ZmFsc2UsImNsaWVudF9pZF9zY2hlbWVzX3N1cHBvcnRlZCI6WyJlbnRpdHlfaWQiXSwiaWF0IjoxNzQwMTU4MDQ3LCJleHAiOjE3NDAxNTgxNjd9.paU3FOET8nraQxuesBXD9gw57DL5HfDzkeboKAOinyh5L2MmLwqvRtrSWK8S7qMRWYmdzR-gHMpmebIH7gGE5w
  OAuth-Client-Attestation-PoP: eyJhbGciOiJFUzI1NiIsInR5cCI6Im9hdXRoLWNsaWVudC1hdHRlc3RhdGlvbi1wb3Arand0In0.eyJpc3MiOiIgaHR0cHM6Ly9jbGllbnQuZXhhbXBsZS5jb20iLCJhdWQiOiJodHRwczovL2FzLmV4YW1wbGUuY29tIiwianRpIjoiZDI1ZDAwYWItNTUyYi00NmZjLWFlMTktOThmNDQwZjI1MDY0IiwiaWF0IjoxNzQwMTU4NjE3LCJleHAiOjE3NDAxNTg3Mzd9.B0KOkGi9vMxf3H2Y8rrF-mdLNsuluTvAUbjFfL1Hi-gdaPW7-8ziS9uVh7aTnSAHKWzMfkZLv5q-bxhkglR4PA

  grant_type=refresh_token
  &refresh_token=eyJ0eXAiOiJydCtqd3QiLCJhbGciOiJFUzI1NiIsImtpZCI6ImM5NTBjMGU2ZmRlYjVkZTUwYTUwMDk2YjI0N2FmMDNjIn0.eyJpc3MiOiJodHRwczovL2VhYS1wcm92aWRlci53YWxsZXQuaXB6cy5pdCIsImNsaWVudF9pZCI6IjQ3Yjk4MjM2OTc5MWQwODAwM2E3MjgzZjA1OWNiMGQxIiwiYXVkIjoiaHR0cHM6Ly9lYWEtcHJvdmlkZXIud2FsbGV0LmlwenMuaXQiLCJpYXQiOjE3Mzk5NTI5NDgsIm5iZiI6MTczOTk1MzU0OCwiZXhwIjoxNzQyMzcyNzQ4LCJhdGgiOiJmVUh5TzJyMlozRFo1M0VzTnJXQmIweFdYb2FOeTU5SWlLQ0Fxa3NtUUVvIiwianRpIjoiYzY5NTVjZWItYzY1Zi00MDI1LTkzNzgtYjY2NzJiNjE0NWNmIiwiY25mIjp7ImprdCI6Ijk1MTU3NGFlZTFiYjc5MDdhZTFlYzMxMDlkYjJiMjI1In19.qiGM6E-7zci2-3Nnk4OMD7Tv_leUcRPsFsqaBHDHxEEzsGXLNh9qDbLIBk9sujZGVT9xs-28jZhwD6VT-MGTGw

**Step 3.** The Credential Issuer validates the request according to the following checks:

  - It MUST validate the OAuth-Client-Attestation-PoP parameter based on Section 4 of [OAUTH-ATTESTATION-CLIENT-AUTH].
  - It MUST validate the DPoP Proof JWT, according to (RFC 9449) Section 4.3.
  - It MUST check that the Refresh Token is not expired, not revoked and is bound to the same set of DPoP key as the ones used in the DPoP Proof JWT.

If the request checks are successful, the Credential Issuer generates a new Access Token and a new Refresh Token and these MUST be both bound to the DPoP key. Both the Access Token and the Refresh Token are then sent back to the Wallet Instance.

A non-normative example of a successful response is shown below.

.. code::

  HTTP/1.1 200 OK
  Content-Type: application/json
  Cache-Control: no-store
  {
      "access_token": "eyJ0eXAiOiJhdCtqd3QiLCJhbGciOiJFU..",
      "refresh_token": "eyC3fiLdCtqd3QiLCJhbGciOiCL3..",
      "token_type": "DPoP",
      "expires_in": 3600,
  }

If the Refresh Token is expired or invalid, the Credential Issuer MUST issue an error, using the error type member set to ``invalid_grant``. Therefore, to obtain the Digital Credential an issuance flow authenticating the User is required, as defined in Section :ref:`credential-issuance-low-level:Low-Level Issuance Flow`.

Security Considerations
^^^^^^^^^^^^^^^^^^^^^^^

To mitigate the risks of Refresh Token compromise, the following protections are required:

  - **Confidentiality** of Refresh Tokens MUST be guaranteed in transit and storage.
  - **TLS-protected** connections MUST be used for token transmission.
  - Refresh tokens MUST be **unguessable and secure from modification**.
  - Authorization Servers MUST implement the following mechanism to **detect replay attacks**:

    - **Sender-Constrained Tokens**: Crypto-graphically bind the Refresh Token to the Wallet Instance according to :rfc:`9449`. Access Tokens and Refresh Tokens MUST be bound to the same DPoP key. The DPoP Proof of the refresh token is required to refresh an Access Token. The same DPoP key MUST be used to generate Access Token DPoP Proofs in all the Credential Requests.

  - **Limiting the use of Refresh Token**: As specified in `OPENID4VC-HAIP`_: “Credential Issuers should be mindful of how long the usage of the refresh token is allowed to refresh a Credential, as opposed to starting the issuance flow from the beginning. For example, if the User is trying to refresh a Credential more than a year after its original issuance, the usage of the refresh tokens is NOT RECOMMENDED.” In this specification a new Digital Credential obtained performing the re-issuance flow SHOULD have the same expiration of the refreshed one. Thus, this specification does not allow for infinite refresh of Digital Credential with a Refresh Token. Once a Digital Credential expires, the User MUST complete the entire issuance process again, to obtain a new Digital Credential. This specification recommends to set a Refresh Token expiration duration, based on the sensitivity of the associated grant.

.. note::
  *Short-lived Wallet Attestations and DPoP*: Following the specification draft *OAuth 2.0 Attestation Based Client Authentication* (`OAUTH-ATTESTATION-CLIENT-AUTH`_), the Authorization Server MUST bind the Refresh Token to the Client Instance. To prove this binding the Client Instance MUST use the Client Attestation mechanism when refreshing the Access Token and the Client Instance MUST use the same key that was presented in the ``cnf.jwk`` claim of the Client Attestation that was used when the Refresh Token was issued. However this requires that all issued Client Attestations MUST be bound to the same key, thus opening to unlinkability issues. In this specification, both `OAUTH-ATTESTATION-CLIENT-AUTH`_ and *OAuth 2.0 Demonstrating Proof of Possession (DPoP)* (:rfc:`9449`) MUST be used. Using DPoP guarantees the binding of the Refresh Token with the Client Instance as stated in section 5 of :rfc:`9449` *"the Refresh Token MUST be bound to the respective public key [...] a Client MUST present a DPoP proof for the same key that was used to obtain the Refresh Token each time that Refresh Token is used to obtain a new Access Token"*. DPoP ensures that the Refresh Token is bound to the Wallet Instance.


Re-Issuance Flow
----------------

Re-issuance involves replacing Digital Credentials already stored in a Wallet Instance with new ones of the same document type. The new Digital Credentials MUST be issued by the same Credential Issuers that originally provided the existing ones to the same Wallet Instance.

To facilitate this, particularly in scenarios where User authentication is not strictly required, a Refresh Token (RT) flow MAY be used (see Section :ref:`credential-issuance-low-level:Refresh Token Flow` for more details). An Access Token obtained as a result of a Refresh Token flow MUST NOT be used to issue a Digital Credential that is not present in the Wallet Instance (first-time-issuance). The Refresh Token mechanism enables automated Credential replacement, streamlining the process for both the Credential Issuer and the User.

The re-issuance process outlined in this section is limited to the following scenarios:

  - Data model/format technical update;
  - User's attribute set update.

In the first case, the new Digital Credential's Users attribute set will match the original one. For example, a Credential Issuer may need to update the Digital Credential metadata or data format without changing the User's attribute set. In this case, the direct involvement of the User is not mandatory for the replacement and storage of a Digital Credential.

In the second case, Credential Issuers may also need to modify one or more User's attribute values during re-issuance. In this case, the Wallet Instance MUST inform the User that the attribute data set has been changed and MUST then request the User's authorization to store the new Digital Credential.

In both cases, the newly issued Digital Credential MUST have the same expiry date as the previous one.

Re-issuance after Digital Credential expiration MUST always require User authentication.

The following diagram describes the Digital Credential re-issuance flow.

.. _fig_reissuance_flow:
.. figure:: ../../images/Re-Issuance-Flow.svg
    :figwidth: 100%
    :align: center
    :target: https://www.plantuml.com/plantuml/svg/ZLJRRXen47ttLqoVcaXS8ZLFH553GoeX9HMYqAXAAcHsPrchNfjwPY7frtTjBiAuJV73QctFcSlncRaXbexhIejtocIwpX5AvYNrkbqdrvs5uhAUruGkiuRHS2UpLNUffV6ODd6krRnxUzaU-QFfmtstaiJecgFPuDN8IcMTfVVUh1196Ci8JYrA5eyb6f0mK4qKgU7MOOw6LVDh47C2jZ17g9UvPCnRm2KUsWo9QdG43_tlG6Xoa60igq9bafKr7kqHKq87DIcp00aE5ygdXpdOcjksQCzbWsnggcgp0sQbD0PrHtYdFbqXUi6BNQ8XU9HQ8yFG44kJuPKGge2pCQxi5b-Xzw2eWcS3r_2L9TS4zueOFfu3-wBFNf7E1GW0w8sHdS8LHeOJ-nCD5DPv4o2s3lE3ukagd0SkDHOSTcFyLIjlj_OXZ8MLr2eFLwbhV6d-ALpko_GRNyi1oLkWCl1qyNBneGNDz_B7KHb-eIQ4CsFFGS3X8hPB0TimgX2HhV3Rb84-4JfF9Pt6W5VJAHJ4llzAmHiSNCFmoxV-_N2GLhy3PNlGZ09ebYDBfJj-Xw3CtlffEXhq9tSjw4ycu-6dwUHkjZb9kJs9tfZXqvzZyusAw6SP4crb4lXBKjgl9B_uUjCOXKCgJ_C7q6lOTWmnwhEswyrxln4lvGDWBn41yTf4aGOChiCayQqCHHFds7Ajk0n3v3r1l_PvysvGnAPn7wLlakxsFtwym61aHn2HpnRSjZNsfZxVT61koKcrIplj-hvjWNNmRFwZqkj4a_z-hvvlE2GE10Lwh5E_0pjNXtQ9AY9xf2J2iIQiGrzwNFBRUeWLaRv80Zmzub7Nz0QeaH6M3bVArXHXH4ZWfe7KbVu3

    Re-Issuance Flow Diagram


1. The flow starts when the User opens the Wallet Instance: this step MAY be triggered either by a notification sent by the Credential Issuer (using e.g., one of the out-of-band communication contacts registered during the Issuance flow).
2. Regardless of the Digital Credental revocation mechanism supported, if the Wallet Instance.

   - only supports Status List and does not have a valid Status Token for a stored Digital Credential, Wallet Instance MUST retrieve a fresh one following the flow described in Section :ref:`credential-revocation:OAuth Status Lists`. If any Digital Credential has status set to ``0x03`` - ``UPDATE`` or ``0x04`` - ``ATTRIBUTE_UPDATE``; or else
   - together with the Credential Issuer additionally support Status Assertion and the Wallet Instance does not have a valid Status Assertion for a stored Digital Credential, the Wallet Instance MAY retrieve a fresh one following the flow described in Section :ref:`credential-revocation:OAuth Status Assertions`. If any Digital Credentials has the ``credential_status_type`` set to ``INVALID``, the Wallet Instance MUST verify the ``credential_status_detail.state`` claim. If this claim is set to ``UPDATE`` or ``ATTRIBUTE_UPDATE``, then

     the Wallet Instance MUST check if the related Access Tokens are still valid. If the Access Token is valid, then step 3 MAY be skipped.

3. If the Access Token is expired and the Wallet Instance still has a valid Refresh Token, the Wallet Instance MUST obtain a new Access Token starting a Refresh Token Flow, according to Section :ref:`credential-issuance-low-level:Refresh Token Flow`. The Refresh Token Flow enables the Wallet Instance to obtain a new Refresh Token and a new DPoP Access Token to refresh the Digital Credential. If the Refresh Token is expired, a new Issuance Flow authenticating the User is required.
4. The Wallet Instance MUST use a valid DPoP Access Token to retrieve the new Digital Credential requesting it to the Credential endpoint following the steps from 12 to 22 of Figure 9 in Section :ref:`credential-issuance-low-level:Low-Level Issuance Flow`. When the new Digital Credential is successfully stored in the secure storage, the Wallet Instance MUST delete the previous one.

.. note::
  Regardless of the Digital Credental revocation mechanism supported, if either the Digital Credential status is set to ``ATTRIBUTE_UPDATE`` (using OAuth Status List revocation) or ``credential_status_detail.state`` is set to ``ATTRIBUTE_UPDATE`` (using OAuth Status List revocation) the User's attribute set, in the refreshed Digital Credential, doesn't match the one in the stored Digital Credential. In this case, the Wallet Instance MUST request the User's authorization to store the new refreshed Digital Credential. 
  
  If instead, either the Digital Credential status is set to ``UPDATE``(using OAuth Status List revocation) or ``credential_status_detail.state`` set to ``UPDATE`` (using OAuth Status List revocation) the ``credential_status_detail.state`` is set to ``UPDATE``, only the Credential metadata parameters have changed. In this case, the Wallet Instance SHOULD store the new Digital Credential without requiring explicit user authorization and consent.


Re-Issuance Flow: Security Considerations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To ensure the integrity and security of the re-issuance process, the following security considerations apply.

  - Access Token limitations: An Access Token obtained as a result of a Refresh Token flow MUST NOT be used for the first-time issuance of a Digital Credential. This ensures that only existing Credentials in the Wallet Instance are updated.
  - Credential expiry: The Credential Issuer MUST set the same expiry date for the re-issued Digital Credential as the previous one. This prevents indefinite Credential renewals without proper User authentication.
  - User consent: For re-issuance processes triggered by attribute changes, User consent MUST be obtained before storing the new Digital Credential. This ensures that the User is aware of and agrees to the updated information.
  - Sender-constrained Refresh Token: Refresh Tokens MUST be cryptographically bound to the Wallet Instance using DPoP protocol. This mitigates the risk of token misuse by ensuring that only the intended Wallet Instance (the same that originally has obtained the Digital Credential) can use that Refresh Token.




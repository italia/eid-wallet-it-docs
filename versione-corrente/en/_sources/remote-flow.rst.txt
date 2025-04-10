.. include:: ../common/common_definitions.rst

.. _remote-flow.rst:

Remote Flow
===========

Depending on whether the User is using a mobile device or a workstation, the Relying Party MUST support the following remote flows:

* **Same Device**, the Relying Party MUST provide an HTTP location to the Wallet Instance using a redirect (302) or an HTML href in a web page;
* **Cross Device**, the Relying Party MUST provide a QR Code which the User frames with the Wallet Instance.

Once the Wallet Instance establishes the trust with the Relying Party and evaluates the request, the User gives the consent for the disclosure of the Digital Credentials, in the form of a Verifiable Presentation.

.. _fig_High-Level-Flow-Presentation:
.. figure:: ../../images/High-Level-Flow-Presentation.svg
    :figwidth: 100%
    :align: center
    :target: https://www.plantuml.com/plantuml/svg/TL9TJy8m57tlhpZXHLcYYz-61uCXnF34d11UJCZS6bQPRMtlRF3NspB0JUBJidlEFH-v7LhA3DKV5TF-AtAXCqdeBRAgueI9zB3CUG-PXUjIKbvjX5mXySFDbc0qOqRZx05kW8jpHD5ZJQKouZiZeIHI_bbpIr64KmVJ_2nh8_gWqgXwLVfX8GpF2ShWEKMk2WwRPnAlafHdSSHn4-t4eYi-beLMGb8SC-P21gC7k0mXThQOfvDsXAVnBDWaqvTP7mVrDF7AxOssxg7SrR6krKfQtdJR8zEtTr-cpvZRxLs7lSK4evBdQ-l9lz1DWEQM6uo2a2IFjfhS1ZXa_LExQ_obbwJMN1uNQbZ_D0e6TzjAIJlQeUvzm3htxlWg7QBuispWzYTi3ilOaCl2lwuV
    
    High Level Remote Protocol Flow


A High-Level description of the remote flow, from the User's perspective, is given below and shown in :ref:`fig_High-Level-Flow-Presentation`:

  1. *Authorization Request*: the Wallet Instance obtains a URL in the Same Device flow or a QR Code containing the URL in Cross Device flow where the signed presentation Request Object is available for download.
  2. *Request URI Request*: the Wallet Instance extracts from the payload the following parameters: ``client_id``, ``request_uri``, ``state``, ``request_uri_method``.

    * If ``request_uri_method`` is provided and set with the value ``post``, the Wallet Instance SHOULD transmit its metadata to the Relying Party's ``request_uri`` endpoint using the HTTP POST method.
    * If ``request_uri_method`` is set with the value ``get`` or not present, the Wallet Instance MUST fetch the signed Request Object using an HTTP request with method GET to the endpoint provided in the ``request_uri`` parameter.

  3. *Request URI Response*: the Relying Party returns a signed Request Object to the Wallet Instance. 
  4. *WI Checks*: the Wallet Instance:
    
    a. verifies the signature of the signed Request Object using the public key identified in the JWT header of the Request Object. Using that reference, the Wallet Instance is able to select the correct Relying Party's public key for signature verification.
    b. verifies that the ``client_id`` contained in the Request Object issuer (Relying Party) matches with the one obtained at the step number 2 and with the ``sub`` parameter contained in the Relying Party's Entity Configuration within the Trust Chain.
    c. evaluates the requested Digital Credentials and checks the eligibility of the Relying Party in asking for these by applying the policies related to that specific Relying Party, obtained with the Trust Chain.
  
  5. *User Consent*: the Wallet Instance asks User disclosure and consent by showing the Relying Party's identity and the requested attributes.
  6. *POST Authorization Response*: the Wallet Instance presents the requested information to the Relying Party, along with the Wallet Attestation if requested. 
  7. *RP Checks*: The Relying Party validates the presented Credentials by verifying the trust with their Issuers and checks the Wallet Attestation to ensure the Wallet Provider is trusted.
  8. *Relying Party Response*: the Wallet Instance informs the User about the successful authentication with the Relying Party, and the User continues the navigation.

Below is a sequence diagram that details the interactions between all the involved parties.

.. figure:: ../../images/cross_same_device_auth_seq_diagram.svg
    :figwidth: 100%
    :align: center
    :target: https://www.plantuml.com/plantuml/svg/fLPDRnit4BtpLmpKGst0TfCU3RY8uxgsaxHMBIK-r8L0SKSIwnMv9OTIr2B_lJEWbgPa1mXGtPRalFVuE1zw4qa7IijMwKJUfUKKWrBgt90FCFWOCGn0HqXAJVtdlF1zX9znPGt60NptmSuNzBPDg3h6iSPssX4CxdNR8i6DOtXdK31WlNiaCTIndgEZpA0LkWQOPKjrX-t6kZaCEMZpTQQTOm_kuFOyqG8kMil0Xu8Cgxq8baGf0hDrtcxP8nPs_cb3TgK98Qa4np-njbEunocCCCYzmUcLdMkotbL7jMgm3jGIkS9JkCE_4qQ2OV24Xh3XbUXJCAZKsHalOsIjMk1WkD0HuUoiu8hw5VPG5m5bJKCaBNkQxNXmKvzOEtbuiXICzu_sXT2GnKnIi12oZEgKF5Z76ciasdJCmUWDacoPu6Fa3t42V82ebvW_Cr2sQq7B5Zf6WBMb1Vn-T-4REGwBW3DMvqXRP-T02uGKMf1J3yx8iz74DaUrqADytIFuergSB94MllcpSbsyKblZqocC5duj-3svg145J68UPIDhcIOYxsgOf9_iNoir3pvrx9-FVUA3T-r6hOLdpJn6E-O08P4iKf8qUUk3Dxe5AHhGYHaTMPFpfaHVoYCA4uKKARibseeLIkcMmCxW-UN1IkPkWuQtex42_gtxn-I4Mza6OLkC7ACRJHh82qEDLuf10A3sKxvBUbHY5mMMq3WhrpIwqrFRMh8O5ROHlq7qrULOdiHvWYxNWIetg4f7wAATEsnwGF3JloGRPy4lltgR_1eYFtlz8iH-0Zr_cPqM0x_sDchNGESvcIp64lG9WvrjG9WqfO3WPvNwSg7RJ5sYT6kRgZpvvAVXGJpC1zAJ4JCVf7Z4gBqkbO4kl9lPiCHcjnaLGoL9G3ga3_QVt7BkC7Q220yklycgcv1_H5VAhgiwr2IcwTB6A3bSs_PoZcGxh9wskDldI0XAK6L0bLZdH1Zp-HCMbp-h0tr-1nPk8qYFxzt-1NbPIoJlQTUKg6ecIOpaNS0LYsbEAZMPIbfc8oMhMxY9CM60iTJe5h98VdS_Xb7_tXKAopCOOwxc0gLKO5O4lyB0ntYktLnTZw_kBYz_Koz7d2euXei5SjEwzct3OUzn0s-jQoGfHGh7-PdSVUXZP01nE4NP1IadWUlIb3CL7ZaoZmlhPBs-8tdM8zcRNswO7-b42VtbPmhQPFSR6qth8pQWYOAT9i8eCi28HYbwDhhKf6K2oFKI4FHAsrRIuKHgKvn0LLdsiUkJ83VD_Z87UPn1adri3bNVbKSoV79JpidBRCneIFf0LVdNu_7mXzSdh-77Lw_WzZq_uR-3-kX09XPriSmY2Dkoc1YP7L-sbQXPOym2TvYgsI4NUtbeX6ToVQ9lL5pNytglPUM95za_UCS6Zqom7UNNEDsRExcafTGFXA3lD_dAsUH3LR0ZgfW59Vs_FVoYH7O5dOtQ-QEKmVe1rPK_JEMVocxBATA6pq_k3VHTnzumTLgs_m40
    
    Remote Protocol Flow


The details of each step shown in the previous picture are described below.

**Steps 1-2**: The User requests to access to a protected resource of the Relying Party.

**Steps 3-5**: The Relying Party creates a state value bound to the user-agent (e.g., using an HTTP secured cookie), the Request Object available for download at the ``request_uri`` location. It then inspects the user-agent to determine whether the flow occurs on the same device as the user-agent.

**Steps 6-9 (Authorization Request)**: The Relying Party provides the user-agent with a JavaScript page inspecting the status endpoint and the Wallet Instance with a URL containing the Authorization Request. 

  In the **Cross Device Flow**, the Request URI is presented as a QR Code displayed to the User. The User scans the QR Code using the Wallet Instance and retrieves a URL with the parameters ``client_id``, ``request_uri``, ``state`` and ``request_uri_method``. 

  Below is represented a non-normative example of a QR Code issued by the Relying Party.

  .. figure:: ../../images/verifier_qr_code.svg
      :figwidth: 50%
      :align: center


  Below is represented a non-normative example of the QR Code raw payload:

  .. code-block:: text

    https://wallet-solution.example.org/authorization?client_id=https%3A%2F%2Frelying-party.example.org&request_uri=https%3A%2F%2Frelying-party.example.org&request_uri_method=post

  .. note::
      The *error correction level* chosen for the QR Code MUST be Q (Quartily - up to 25%), since it offers a good balance between error correction capability and data density/space. This level of quality and error correction allows the QR Code to remain readable even if it is damaged or partially obscured.

  Conversely, in the **Same Device Flow**, the Relying Party uses an HTTP response redirect (with status code set to 302) or an html page with an href button, containing the URL providing the same information as in the Cross-Device Flow. Below is a non-normative example:

  .. code-block:: http 

      HTTP/1.1 302 Found
      Location: https://wallet-solution.digital-strategy.europa.eu?client_id=https%3A%2F%2Frelying-party.example.org%2Fcb&request_uri=https%3A%2F%2Frelying-party.example.org%2Frequest_uri&request_uri_method=post


**Step 10**: The Wallet Instance evaluates the trust with the Relying Party.

**Steps 11-13 (Request URI Request)**: The Wallet Instance checks if the Relying Party has provided the ``request_uri_method`` within its signed Request Object. 

  - If it is provided and is equal to ``post``, the Wallet Instance SHOULD provide its metadata to the Relying Party. The Relying Party updates the Request Object according with the Wallet technical capabilities.

    The following is a non-normative example of an HTTP request made by the Wallet Instance to the Relying Party.

    .. code-block:: http

      POST /request HTTP/1.1
      Host: client.example.org
      Content-Type: application/x-www-form-urlencoded
      Accept: application/oauth-authz-req+jwt
        
      wallet_metadata=%7B%22authorization_endpoint%22%3A%20%22eudiw%3A%22%2C%20%22response_types_supported%22%3A%20%5B%22vp_token%22%5D%2C%20%22response_modes_supported%22%3A%20%5B%22form_post.jwt%22%5D%2C%20%22vp_formats_supported%22%3A%20%7B%22dc%2Bsd-jwt%22%3A%20%7B%22sd-jwt_alg_values%22%3A%20%5B%22ES256%22%2C%20%22ES384%22%5D%7D%7D%2C%20%22request_object_signing_alg_values_supported%22%3A%20%5B%22ES256%22%5D%7D%2C&wallet_nonce=%22qPmxiNFCR3QTm19POc8u%22

    Where the body of the request prior to being encoded in `application/x-www-form-urlencoded` by the Wallet corresponds to:

    .. code:: json

      {
        "wallet_metadata": {
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
          "client_id_schemes_supported": ["https"],
        },
        "wallet_nonce": "qPmxiNFCR3QTm19POc8u"
      }

  - When the Wallet Instance capabilities discovery is not supported by Relying Party, the Wallet Instance requests the signed Request Object using the HTTP method GET.

**Step 14 (Request URI Response)**: The Relying Party issues the Request Object signing it using one of its cryptographic private keys, where their public parts have been published within its Entity Configuration (`metadata.openid_credential_verifier.jwks`). The Wallet Instance obtains the signed Request Object.

  Below is a non-normative example of the Redirect URI Response:

  .. code-block:: http

    HTTP/1.1 200 OK
    Content-Type: application/oauth-authz-req+jwt

    eyJhbGciOiJFUzI1NiIs...9t2LQ
  
  A non-normative example of a Request Object in the form of decoded header and payload is shown below:

  .. code-block:: json

    {
      "alg": "ES256",
      "typ": "oauth-authz-req+jwt",
      "kid": "9tjiCaivhWLVUJ3AxwGGz_9",
      "trust_chain": [
        "MIICajCCAdOgAwIBAgIC...awz",
        "MIICajCCAdOgAwIBAgIC...2w3",
        "MIICajCCAdOgAwIBAgIC...sf2"
      ]
    }
  
  .. code-block:: json

    {
      "client_id": "https://relying-party.example.org",
      "response_mode": "direct_post.jwt",
      "response_type": "vp_token",
      "dcql_query": {
        "credentials": [
          {
            "id": "personal id data",
            "format": "dc+sd-jwt",
            "meta": {
              "vct_values": [ "https://pidprovider.example.org/v1.0/personidentificationdata" ]
            },
            "claims": [
                {"path": ["given_name"]},
                {"path": ["family_name"]},
                {"path": ["personal_administrative_number"]}
            ]
          },
          {
            "id": "wallet attestation",
            "format": "dc+sd-jwt",
            "meta": {
              "vct_values": ["https://itwallet.registry.example.it/WalletAttestation"]
            },
            "claims": [
                {"path": ["wallet_link"]},
                {"path": ["wallet_name"]}
            ]
          }
        ]
      },
      "response_uri": "https://relying-party.example.org/response_uri",
      "nonce": "2c128e4d-fc91-4cd3-86b8-18bdea0988cb",
      "wallet_nonce": "qPmxiNFCR3QTm19POc8u",
      "state": "3be39b69-6ac1-41aa-921b-3e6c07ddcb03",
      "iss": "https://relying-party.example.org",
      "iat": 1672418465,
      "exp": 1672422065,
      "request_uri_method": "post"
    }

**Steps 15-17 (WI Checks)**: The Wallet Instance verifies the Request Object, which is in the form of a signed JWT. It then processes the Relying Party metadata and applies the relevant policies to determine which Digital Credentials and User data the Relying Party is authorized to request.

**Steps 18-19 (User Consent)**: The Wallet Instance requests the User's consent to disclose the requested Credentials by showing the Relying Party's identity and the requested attributes. The User authorizes and consents the presentation of the Credentials by selecting/deselecting the personal data to release.

**Step 20 (Authorization Response)**: The Wallet Instance provides the Authorization Response to the Relying Party using an HTTP request with the method POST (response mode "direct_post.jwt").
  
  Below is a non-normative example of the Authorization Response:

  .. code-block:: http

    POST /response_uri HTTP/1.1
    HOST: relying-party.example.org
    Content-Type: application/x-www-form-urlencoded
    
    response=eyJhbGciOiJFUzI1NiIs...9t2LQ
  
  Below is a non-normative example of the decrypted payload of the JWT contained in the ``response``, before base64url encoding. The ``vp_token`` parameter value corresponds to the format used when the DCQL query language is used in the presentation request.
  
  .. code-block:: json

    {
      "state": "3be39b69-6ac1-41aa-921b-3e6c07ddcb03",
      "vp_token": {
          "personal id data": "eyJhbGciOiJFUzI1NiIs...PT0iXX0",
          "wallet attestation": "eyJhbGciOiJFUzI1NiIs...NTi0XG"
      }
    }

**Steps 21-25 (RP Checks)**: The Relying Party verifies the Authorization Response, extracts the Wallet Attestation to establish trust with the Wallet Solution. It then extracts the Digital Credentials and attests trust with the Credentials Issuer and the Wallet Instance's proof of possession of the presented Digital Credentials. Finally, the Relying Party verifies the revocation status of the presented Digital Credentials as described in :ref:`Digital Credential Revocation and Suspension`. If all previous verifications yelded positive result, the Relying Party updates the User session.

**Steps 26-27 or 28 (Relying Party Response)**: The Relying Party provides to the Wallet Instance the response about the presentation, which informs the User.

  Upon receiving and validating the Authorization Response at the Response Endpoint, the Relying Party returns to the Wallet Instance a HTTP 200 OK. In particular, in the Same Device Flow, the Relying Party SHOULD also pass the ``redirect_uri`` to the Wallet Instance. Upon receiving the ``redirect_uri``, the Wallet Instance MUST perform a redirect to the URL specified by the ``redirect_uri``. This redirect allows the Relying Party to seamlessly resume interaction with the User on the device which initiated the flow. When the response does not contain the ``redirect_uri`` parameter, the Wallet Instance is not required to perform any further step. The User should manually close the Wallet Instance and open the user-agent to continue the flow. 
  
  The following is a non-normative example of the response in the Same Device Flow.

  .. code-block:: http

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
      "redirect_uri": "https://relying-party.example.org/cb?response_code=091535f699ea575c7937fa5f0f454aee"
    }

**Steps 29-30**: The JavaScript page is inspecting the status endpoint.
  
  Below is a non-normative example of the HTTP Request to the status endpoint, where the parameter ``id`` contains an opaque and random value:

  .. code-block:: http 

    GET /session-state?id=3be39b69-6ac1-41aa-921b-3e6c07ddcb03 HTTP/1.1
    HOST: relying-party.example.org
  
  When the Wallet Instance has provided the presentation to the Relying Party's  **response_uri** endpoint and the User authentication is successful. The Relying Party updates the session cookie allowing the user-agent to access to the protected resource. A redirect URL is provided carrying the location where the user-agent is intended to navigate.
  The following is a non-normative example of the response with the ``redirect_uri`` from the Relying Party to the user-agent.

  .. code-block:: http

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
      "redirect_uri": "https://relying-party.example.org/cb?response_code=091535f699ea575c7937fa5f0f454aee"
    }

**Steps 31-32**: The user-agent is redirected to the redirect URI to continue the navigation with the protected resource made available to the User.


Authorization Request
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The URL parameters contained in the Relying Party Authorization Request, which include the ``request_uri`` where the signed Request Object can be downloaded, are described in the table below.

.. list-table::
  :widths: 25 50
  :header-rows: 1

  * - **Name**
    - **Description**
  * - **client_id**
    - REQUIRED. Unique identifier of the Relying Party.
  * - **request_uri**
    - REQUIRED. The HTTP URL where the Relying Party provides the signed Request Object to the Wallet Instance.
  * - **state**
    - RECOMMENDED. A unique identifier for the current transaction generated by the Relying Party. The value SHOULD be opaque to the Wallet Instance.
  * - **request_uri_method**
    - OPTIONAL. The HTTP method MUST be set with ``get`` or ``post``. The Wallet Instance should use this method to obtain the signed Request Object from the ``request_uri``. If not provided or equal to ``get``, the Wallet Instance SHOULD use the HTTP method ``get``. Otherwise, the Wallet Instance SHOULD provide its metadata within the HTTP POST body encoded in ``application/x-www-form-urlencoded``.    

.. warning::
    For security reasons and to prevent endpoint mix-up attacks, the value contained in the ``request_uri`` parameter MUST be one of those attested by a trusted third party, such as those provided in the ``openid_credential_verifier`` metadata within the ``request_uris`` parameter, obtained from the Trust Chain about the Relying Party.

.. note::
    The ``state`` parameter in an OAuth request is optional, but it is highly recommended. It is primarily used to prevent Cross-Site Request Forgery (CSRF) attacks by including a unique and unpredictable value that the Relying Party can verify upon receiving the response. Additionally, it helps maintain the state between the request and response, such as session information or other data the Relying Party needs after the authorization process.

The value corresponding to the ``request_uri`` endpoint SHOULD be randomized, according to `RFC 9101, The OAuth 2.0 Authorization Framework: JWT-Secured Authorization Request (JAR) <https://www.rfc-editor.org/rfc/rfc9101.html#section-5.2.1>`_ Section 5.2.1.


Request URI Request
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Relying Party SHOULD provide the POST method with its ``request_uri`` endpoint allowing the Wallet Instance to inform the Relying Party about its technical capabilities.

This feature can be useful when, for example, the Wallet Instance supports a restricted set of features, supported algorithms or a specific url for its ``authorization_endpoint``, and any other information that it deems necessary to provide to the Relying Party for interoperability.

.. warning::
    The Wallet Instance, when providing its technical capabilities to the 
    Relying Party, MUST NOT include any User information or other explicit 
    information regarding the hardware used or usage preferences of its User.

If both the Relying Party and the Wallet Instance support the ``request_uri_method`` with HTTP POST, the Wallet Instance capabilities (metadata) MUST be provided using an HTTP request to the `request_uri` endpoint of the Relying Party, with the method POST and content type set to `application/x-www-form-urlencoded`.
The request and its parameters are defined in Section number 5 (Authorization Request) of `OpenID4VP`_. Below are the normative details and references about the parameters to be used by the Wallet Instance in the request.

.. list-table:: Request URI Endpoint Parameters
   :header-rows: 1

   * - Parameter
     - Description
   * - `wallet_metadata`
     - OPTIONAL. JSON object with metadata parameters. See `OpenID4VP`_, Section 9.1 and the table below, "Wallet Metadata Parameters".
   * - `wallet_nonce`
     - RECOMMENDED. String used by Wallet Instance to prevent replay of the Relying Party's responses. See `OpenID4VP`_, Section 9.


.. list-table:: Wallet Metadata Parameters
   :header-rows: 1

   * - Parameter
     - Description
   * - `vp_formats_supported`
     - REQUIRED. Object with Credential format identifiers. See `OpenID4VP`_ Appendix B.
   * - `alg_values_supported`
     - OPTIONAL. Array of cryptographic suites supported. See `OpenID4VP`_ Appendix B.
   * - `client_id_schemes_supported`
     - RECOMMENDED. Array of Client Identifier schemes. Default is `entity_id`.
   * - `authorization_endpoint`
     - URL of the authorization server's endpoint, see `OAUTH2`_. Using an universal link is preferable for enhanced security and fallback support, custom url schemes can also be used if necessary.
   * - `response_types_supported`
     - OPTIONAL. JSON array of OAuth 2.0 "response_type" values. If present it MUST be set to `vp_token`. Default is `vp_token`.
   * - `response_modes_supported`
     - OPTIONAL. JSON array of OAuth 2.0 "response_mode" values. See `JARM`_.
   * - `request_object_signing_alg_values_supported`
     - OPTIONAL. See OpenID Connect Discovery.

.. note::

  The ``wallet_nonce`` parameter is RECOMMENDED for Wallet Instances that want to prevent reply of their http requests to the Relying Parties. 
  When present, the Relying Party MUST evaluate it.

.. note::

  For the ``authorization_endpoint`` the use of universal links are preferred over custom url-schemes because, when properly configured using Assetlinks JSON for Android and Apple App Site Association for iOS, they provide enhanced security by reducing the risk of URL hijacking. 
  Furthermore, universal links offer fallback mechanisms, allowing the flow to continue seamlessly in a browser even if the Wallet Instance is not installed, ensuring a smoother User experience. To ensure interoperability, support custom url-schemes is also RECOMMENDED according to OpenID4VC High Assurance Interoperability Profile (HAIP)  `OPENID4VC-HAIP`_, and in particular using the custom url ``haip://``.

Request URI Response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Relying Party issues the signed Request Object using the content type set to ``application/oauth-authz-req+jwt``.

The JWT header parameters are described below:

.. list-table::
  :widths: 25 50
  :header-rows: 1

  * - **Name**
    - **Description**
  * - **alg**
    - Algorithm used to sign the JWT, according to [:rfc:`7516#section-4.1.1`]. It MUST be one of the supported algorithms in Section *Cryptographic Algorithms* and MUST NOT be set to ``none`` or to a symmetric algorithm (MAC) identifier.
  * - **typ**
    - Media Type of the JWT, as defined in [:rfc:`7519`] and [:rfc:`9101`]. It SHOULD be set to the value ``oauth-authz-req+jwt``.
  * - **kid**
    - Key ID of the public key needed to verify the JWT signature, as defined in [:rfc:`7517`]. REQUIRED when ``trust_chain`` is used.
  * - **trust_chain**
    - Sequence of Entity Statements that composes the Trust Chain related to the Relying Party, as defined in `OID-FED`_ Section 4.3 *Trust Chain Header Parameter*.


The JWT payload parameters are described herein:

.. list-table::
  :widths: 25 50
  :header-rows: 1

  * - **Name**
    - **Description**
  * - **client_id**
    - Unique Identifier of the Relying Party.
  * - **response_mode**
    - It MUST be set to ``direct_post.jwt``.
  * - **dcql_query**
    - Object representing a request for a presentation of Credentials, according to the DCQL query language defined in Section 6 of `OpenID4VP`_.
  * - **response_type**
    - It MUST be set to ``vp_token``.
  * - **wallet_nonce**
    - String value used to mitigate replay attacks of the response, as defined in Section 5.11 (Request URI Method) of `OpenID4VP`_. It MUST be present if previously provided by Wallet Instance.
  * - **response_uri**
    - The Response URI to which the Wallet Instance MUST send the Authorization Response using an HTTP request using the method POST.
  * - **nonce**
    - Fresh cryptographically random number with sufficient entropy, which length MUST be at least 32 digits.
  * - **state**
    - Unique identifier of the Authorization Request.
  * - **iss**
    - The entity that has issued the JWT. It will be populated with the Relying Party client id.
  * - **iat**
    - Unix Timestamp, representing the time at which the JWT was issued.
  * - **exp**
    - Unix Timestamp, representing the expiration time on or after which the JWT MUST NOT be valid anymore.
  * - **request_uri_method**
    - String determining the HTTP method to be used with the `request_uri` endpoint to provide the Wallet Instance metadata to the Relying Party. The value is case-insensitive and can be set to: `get` or `post`. The GET method, as defined in [@RFC9101], involves the Wallet Instance  sending a GET request to retrieve a Request Object. The POST method involves the Wallet Instance requesting the creation of a new Request Object by sending an HTTP POST request, with its metadata, to the request URI of the Relying Party.

.. warning::
    For security reasons and to prevent endpoint mix-up attacks, the value contained in the ``response_uri`` parameter MUST be one of those attested by a trusted third party, such as those provided in the ``openid_credential_verifier`` metadata within the ``response_uris`` parameter, obtained from the Trust Chain about the Relying Party.

.. note::

  The following parameters, even if defined in [OID4VP], are not mentioned in the previous non-normative example, since their usage is conditional and may change in future release of this documentation.

  - ``presentation_definition``: JSON object according to `Presentation Exchange <https://identity.foundation/presentation-exchange/spec/v2.0.0/>`_. This parameter MUST not be present when ``presentation_definition_uri`` or ``scope`` are present.
  - ``presentation_definition_uri``: Not supported. String containing an HTTPS URL pointing to a resource where a Presentation Definition JSON object can be retrieved. This parameter MUST be present when ``presentation_definition`` parameter or a ``scope`` value representing a Presentation Definition is not present. 
  - ``client_metadata``: A JSON object containing the Relying Party metadata values. If the ``client_metadata`` parameter is present, the Wallet Instance MUST ignore it and consider the client metadata obtained through the OpenID Federation Trust Chain.


Request URI Endpoint Errors
----------------------------

When the Relying Party encounters errors while issuing the Request Object from the ``request_uri`` endpoint, it MUST return an error response with ``application/json`` as the content type and MUST include the following parameters:

* ``error``: The error code.
* ``error_description``: Text in human-readable form providing further details to clarify the nature of the error encountered.

The following table lists the HTTP Status Codes and related error codes that MUST be supported for the error response:

.. list-table:: 
    :widths: 20 20 60
    :header-rows: 1

    * - **Status Code**
      - **Error Code**
      - **Description**
    * - ``500 Internal Server Error``
      - ``server_error``
      - The request cannot be fulfilled because the Request URI Endpoint encountered an internal problem. (:rfc:`6749#section-4.1.2.1`).
    * - ``503 Service Unavailable``
      - ``temporarily_unavailable``
      - The request cannot be fulfilled because the Request URI Endpoint is temporarily unavailable (e.g., due to maintenance or overload). (:rfc:`6749#section-4.1.2.1`).


The following is an example of an error response from ``request_uri`` endpoint:

.. code-block:: http

  HTTP/1.1 500 Internal Server Error
  Content-Type: application/json

  {
   "error": "server_error",
   "error_description": "The Request Object cannot be retrieved due to an internal server error."
  }

Upon receiving an error response, the Wallet Instance SHOULD inform the User of the error condition in an appropriate manner. The Wallet Instance SHOULD log the error and MAY attempt to recover from certain errors if feasible. For example, if the error is ``server_error``, the Wallet Instance SHOULD prompt the User to re-enter or scan a new QR code, if applicable.


Authorization Response 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

After obtaining the User authorization and consent for the presentation of the Digital Credentials, the Wallet Instance sends the Authorization Response to the Relying Party ``response_uri`` endpoint using an HTTP request with the method POST, the content SHOULD be encrypted according `OpenID4VP`_ Section 7.3, using the Relying Party public key.

.. note::
    **Why the response is encrypted?**

    The response sent from the Wallet Instance to the Relying Party is encrypted to prevent a malicious agent from gaining access to the plaintext information transmitted within the Relying Party's network. This is only possible if the network environment of the Relying Party employs `TLS termination <https://www.f5.com/glossary/ssl-termination>`_. Such technique employs a termination proxy that acts as an intermediary between the client and the webserver and handles all TLS-related operations. In this manner, the proxy deciphers the transmission's content and either forwards it in plaintext or by negotiates an internal TLS session with the actual webserver's intended target. In the first scenario, any malicious actor within the network segment could intercept the transmitted data and obtain sensitive information, such as an unencrypted response, by sniffing the transmitted data.


Where the following parameters are used:

.. list-table::
  :widths: 25 50
  :header-rows: 1

  * - **Name**
    - **Description**
  * - **vp_token**
    - There MUST be at least two signed presentations in this Array:

      - The requested Digital Credential (one or more, in format of SD-JWT VC)
      - The Wallet Attestation (in SD-JWT VC format)
      
      When `presentation_definition` is used, the ``vp_token`` value is a JSON Array containing the Verifiable Presentation(s) and the `presentation_submission` parameter MUST be also present within the response.

      When the DCQL query language is used, the ``vp_token`` format is a JSON Object which keys corresponds to the requested credential ids in the ``dcql_query`` used in the request, and the values to each presented Digital Credential.

  * - **state**
    - Unique identifier provided by the Relying Party within the Authorization Request.


SD-JWT defines how a Holder can present a Digital Credential to a Relying Party, proving the legitimate possession of the Digital Credential. To do this, the Holder MUST include the ``KB-JWT`` in the SD-JWT by appending the ``KB-JWT`` at the end of the SD-JWT, as represented in the example below

.. code-block::

  <Issuer-Signed-JWT>~<Disclosure 1>~<Disclosure 2>~...~<Disclosure N>~<KB-JWT>

To validate the signature on the Key Binding JWT, the Relying Party MUST use the key material included in the Issuer-Signed-JWT. The Key Binding JWT (KB-JWT) signature validation MUST use the public key included in the SD-JWT, using the ``cnf`` parameter contained in the Issuer-Signed-JWT.

When an SD-JWT is presented, its KB-JWT MUST contain the following parameters in the JWT header:

.. list-table::
  :widths: 25 50
  :header-rows: 1

  * - **Claim**
    - **Description**
  * - **typ**
    - REQUIRED. MUST be ``kb+jwt``, which explicitly types the Key Binding JWT as recommended in Section 3.11 of [RFC8725].
  * - **alg**
    - REQUIRED. Signature Algorithm using one of the specified in the section Cryptographic Algorithms. 


When an SD-JWT is presented, the KB-JWT signature MUST be verified by the same public key included in the SD-JWT within the `cnf` parameter. The KB-JWT MUST contain the following parameters in the JWT payload:

.. list-table::
  :widths: 25 50
  :header-rows: 1

  * - **Claim**
    - **Description**
  * - **iat**
    - REQUIRED. The value of this claim MUST be the time at which the Key Binding JWT was issued, using the syntax defined in [RFC7519].
  * - **aud**
    - REQUIRED. The intended receiver of the Key Binding JWT. The value of this parameter MUST match the Relying Party unique entity identifier.
  * - **nonce**
    - REQUIRED. Ensures the freshness of the signature. The value type of this claim MUST be a string. The value MUST match with the one provided in the request object.
  * - **sd_hash**
    - REQUIRED. The base64url-encoded hash digest over the Issuer-signed JWT and the selected disclosures. 


Authorization Response Errors
-----------------------------

There are cases where the Wallet Instance cannot validate the Request Object or the Request Object results invalid. This error occurs if the Request Object is successfully fetched from the url provided in the parameter ``request_uri`` but fails the validation checks. This could be due to incorrect signatures, malformed claims, or other validation failures, such as the revocation of the Relying Party.

If the Wallet Instance encounters any such errors during the evaluation of the Authorization Request, it MUST notify the Relying Party by sending an Authorization Error Response. 
The Wallet Instance sends the Authorization Error Response to the Relying Party  ``response_uri`` endpoint using an HTTP POST request. 
The Authorization Error Response MUST be encoded in the request body using the format defined by the ``application/x-www-form-urlencoded`` content type.

Below is a non-normative example of an Authorization Error Response.

.. code-block:: http

  POST /response_uri HTTP/1.1
  HOST: relying-party.example.org
  Content-Type: application/x-www-form-urlencoded

  state=3be39b69-6ac1-41aa-921b-3e6c07ddcb03&
  error=invalid_request&
  error_description=...

.. warning::
  The current OpenID4VP specification outlines various error responses that a Wallet Instance may return to the Relying Party (Verifier) in case of faulty requests. For privacy enhancement, Wallet Instances SHOULD NOT notify the Relying Party of faulty requests in certain scenarios. This is to prevent any potential misuse of error responses that could lead to gather informations that could be exploited.

In the following table are listed error codes and descriptions that are supported for the Authorization Error Response:

.. list-table::
   :widths: 20 60
   :header-rows: 1

   * - **Error Code**
     - **Description**
   * - ``invalid_request_object``
     - The Request Object contains invalid parameters or is otherwise malformed. :rfc:`9101` 
   * - ``invalid_request_uri``
     - The `request_uri` in the authorization request returns an error, contains invalid data, or is otherwise malformed. :rfc:`9101` 
   * - ``vp_formats_not_supported``
     - The Wallet Instance does not support any of the vp formats required by the Relying Party. `OpenID4VP`_
   * - ``invalid_request``
     - The Wallet Instance does not support any of the signing algorithms required by the Relying Party. `OpenID4VP`_
   * - ``access_denied``
     - The Wallet did not have the requested credential, the User did not consent, or the Wallet failed to authenticate the User. `OpenID4VP`_
   * - ``invalid_client``
     - The Relying Party cannot be authorized due to trust validation failures or is not a valid participant of the federation. `OID-FED`_


Relying Party Response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As defined in Section 7.2. (Response Mode "direct_post") of the `OpenID4VP`_ specification, if the Response URI has successfully processed the Authorization Response or Authorization Error Response, it MUST respond with an HTTP status code of 200 with ``Content-Type`` of ``application/json`` and a JSON object in the response body. 

In the **Same Device Flow**, the Relying Party SHOULD add the ``redirect_uri`` parameter to the JSON object in the response body. Upon receiving the ``redirect_uri``, the the Wallet Instance MUST perform a redirect to the URL specified by the ``redirect_uri``.  
This redirect allows the Relying Party to seamlessly resume interaction with the User on the device which initiated the flow, after the Wallet Instance has transmitted the Authorization Response to the designated ``response_uri``.

The Relying Party MUST include a response code within the ``redirect_uri``. The response code is a fresh, cryptographically random number used to ensure only the receiver of the redirect can fetch and process the Authorization Response. The number could be added as a path component, as a parameter or as a fragment to the URL. It is RECOMMENDED to use a cryptographic random value of 128 bits or more at the time of the writing of this specification.
Even if an adversary manages to steal the random value used in the request to the status endpoint, their user-agent would be rejected due to the missing cookie in the request.

.. warning::
    For security reasons and to prevent endpoint mix-up attacks, the value contained in the ``redirect_uri`` parameter MUST be one of those attested by a trusted third party, such as those provided in the ``openid_credential_verifier`` metadata within the ``redirect_uris`` parameter, obtained from the Trust Chain about the Relying Party.


Relying Party Response Errors
--------------------------------

If any validation check, performed by the Relying Party on the Authorization Response from the Wallet Instance, fails; the Response URI endpoint MUST return an error response. The structure of this error response should be determined by the specific nature of the error encountered. The response MUST use ``application/json`` as the content type and MUST include the following parameters:

* ``error``: The error code.
* ``error_description``: Text in human-readable form providing further details to clarify the nature of the error encountered.

The following table lists the HTTP Status Codes and related error codes that MUST be supported for the error response:

.. list-table:: 
    :widths: 20 20 60
    :header-rows: 1

    * - **Status Code**
      - **Error Code**
      - **Description**
    * - ``400 Bad Request``
      - ``invalid_request``
      - The response cannot be processed because it is missing required parameters, contains invalid parameters or is otherwise malformed.
    * - ``400 Bad Request``
      - ``invalid_request``
      - The Credentials presented are malformed, invalid or revoked.
    * - ``400 Bad Request``
      - ``invalid_request``
      - The credential presentation, contained in the ``vp_token`` object, is malformed, doesn't have the required parameters or is incorrectly formatted.
    * - ``400 Bad Request``
      - ``invalid_request``
      - The "sd-jwt" returned is malformed, missing required parameters or incorrectly formatted.
    * - ``403 Forbidden``
      - ``invalid_request``
      - The signature of the KB-JWT is invalid or does not match the associated public key (JWK) referenced in the Issuer signed SD-JWT.
    * - ``403 Forbidden``
      - ``invalid_request``
      - The nonce value provided is incorrect or otherwise malformed.
    * - ``403 Forbidden``
      - ``invalid_request``
      - The signature of the Wallet Attestation is not valid or trust cannot be established with its Issuer.
    * - ``403 Forbidden``
      - ``invalid_request``
      - Trust could not be established with the Credential Issuer.
    * - ``500 Internal Server Error``
      - ``server_error``
      - The request cannot be fulfilled because the Response URI Endpoint encountered an internal problem.
    * - ``503 Service Unavailable``
      - ``temporarily_unavailable``
      - The request cannot be fulfilled because the Response URI Endpoint is temporarily unavailable (e.g., due to maintenance or overload).

Below there are two examples of HTTP responses using ``application/json`` that include both the ``error`` and ``error_description`` members:

.. code-block:: http

  HTTP/1.1 403 Forbidden
  Content-Type: application/json

  {
    "error": "invalid_request",
    "error_description": "Trust cannot be established with the issuer: https://issuer.example.com"
  }


.. code-block:: http

  HTTP/1.1 400 Bad Request
  Content-Type: application/json

  {
    "error": "invalid_request",
    "error_description": "The vp_token is malformed, missing required parameters or incorrectly formatted"
  }

     


Status Endpoint
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This specification introduces the Relying Party Status Endpoint for implementations that choose to use it. This endpoint is an internal security feature of the implementation and is not required for interoperability.

Whether the flow is Same Device or Cross Device, the user-agent needs to check the session status at the endpoint made available by the Relying Party (status endpoint).
This check MAY be implemented in the form of JavaScript code, within the page that shows the QRCode or the href button pointing to the request URL.
The JavaScript code makes the user-agent check the status endpoint using either a polling strategy (in seconds) or a push strategy (e.g., WebSocket).

Since the HTML page and the status endpoint are implemented by the Relying Party, the implementation details of this solution are the responsibility of the Relying Party, as this is related to the Relying Party's internal API. However, the text below describes an example implementation.

The Relying Party binds the request of the user-agent, with a session cookie marked as ``Secure`` and ``HttpOnly``, with the issued request.
The request url SHOULD include a parameter with a random value. The HTTP response returned by this status endpoint MAY contain the HTTP status codes listed below:

* **201 Created**. The signed Request Object was issued by the Relying Party that waits to be downloaded by the Wallet Instance at the ``request_uri`` endpoint.
* **202 Accepted**. This response is given when the signed Request Object was obtained by the Wallet Instance.
* **200 OK**. The Wallet Instance has provided the presentation to the Relying Party's  ``response_uri`` endpoint and the User authentication is successful. The Relying Party updates the session cookie allowing the user-agent to access to the protected resource. A redirect URL is provided carrying the location where the user-agent is intended to navigate.

Status Endpoint Errors
------------------------

If instead any validation check performed by the Relying Party fails, the QRCode page SHOULD be updated with an error message. Moreover, the status endpoint MUST return an error response, whose structure depends on the nature of the error. The response MUST use ``application/json`` as the content type and MUST include the following parameters:

* ``error``: The error code.
* ``error_description``: Text in human-readable form providing further details to clarify the nature of the error encountered.

The following table lists the HTTP Status Codes and related error codes that MUST be supported for the error response:

.. list-table:: 
    :widths: 20 20 60
    :header-rows: 1

    * - **Status Code**
      - **Error Code**
      - **Description**
    * - ``401 Unauthorized``
      - ``authentication_failed``
      - The Wallet Instance or its User have rejected the request, the request is expired, or other errors prevented the authentication. 
    * - ``403 Forbidden``
      - ``invalid_session``
      - Either the session id provided in the request is invalid.


Redirect URI 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The ``redirect_uri`` value MUST be used with an HTTP method GET by the user-agent to redirect the User to a specific Relying Party's endpoint in order to complete the process. 


Redirect URI Errors
-----------------------------

When the user-agent is redirected to the Redirect URI provided by the Relying Party, several errors may occur that prevent the successful completion of the process. These errors are critical as they directly impact the User experience by hindering the seamless flow of information between the Wallet Instance and the Relying Party. Handling these errors requires clear communication to the User within the returned navigation web page. Relying Party MUST implement the error handling and validation mechanisms for Redirect URIs defined in this specification. Below are potential errors related to the Redirect URI, the error response MUST use ``application/json`` as the content type and MUST include the following parameters:

    - ``error``: The error code.
    - ``error_description``: Text in human-readable form providing further details to clarify the nature of the error encountered.

The following table lists the HTTP Status Codes and related error codes that MUST be supported for the error response:

.. list-table:: 
    :widths: 20 20 60
    :header-rows: 1

    * - **Status Code**
      - **Error Code**
      - **Description**
    * - ``403 Forbidden``
      - ``invalid_request``
      - The Redirect URI provided by the Relying Party does not match any of the URIs linked with the User session. (:rfc:`6749#section-4.1.2.1`)
    * - ``403 Forbidden``
      - ``invalid_request``
      - The User session is invalid or expired.
    * - ``500 Internal Server Error``
      - ``server_error``
      - The request cannot be fulfilled due to an intenal server error. (:rfc:`6749#section-4.1.2.1`).
    * - ``503 Service Unavailable``
      - ``temporarily_unavailable``
      - The request cannot be fulfilled because the service is temporarily unavailable (e.g., due to maintenance or overload). (:rfc:`6749#section-4.1.2.1`).

.. _Digital Credential Revocation and Suspension section: credential-revocation.html



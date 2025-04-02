.. include:: ../common/common_definitions.rst
.. _Wallet Attestation: wallet-attestation.html
.. _Trust Model: trust.html


Remote Flow
===========

In this flow the Relying Party MUST provide the URL where the signed presentation Request Object is available for download.

Depending on whether the User is using a mobile device or a workstation, the Relying Party MUST support the following remote flows:

* **Same Device**, the Relying Party MUST provide an HTTP location to the Wallet Instance using a redirect (302) or an HTML href in a web page;
* **Cross Device**, the Relying Party MUST provide a QR Code which the User frames with the Wallet Instance.

Once the Wallet Instance establishes the trust with the Relying Party and evaluates the request,
the User gives the consent for the disclosure of the Digital Credentials, in the form of a Verifiable Presentation.

A High-Level description of the remote flow, from the User's perspective, is given below:

  1. the Wallet Instance obtains a URL in the Same Device flow or a QR Code containing the URL in Cross Device flow;
  2. the Wallet Instance extracts from the payload the following parameters: ``client_id``, ``request_uri``, ``state``, ``request_uri_method``;
  3. If ``request_uri_method`` is provided and set with the value ``post``, the Wallet Instance SHOULD transmit its metadata to the Relying Party's ``request_uri`` endpoint using the HTTP POST method and obtain the signed Request Object. If ``request_uri_method`` is set with the value ``get`` or not present, the Wallet Instance MUST fetch the signed Request Object using an HTTP request with method GET to the endpoint provided in the ``request_uri`` parameter;
  4. the Wallet Instance verifies the signature of the signed Request Object using the public key identified in the JWT header of the Request Object. Using that reference, the Wallet Instance is able to select the correct Relying Party's public key for signature verification;
  5. the Wallet Instance verifies that the ``client_id`` contained in the Request Object issuer (Relying Party) matches with the one obtained at the step number 2 and with the ``sub`` parameter contained in the Relying Party's Entity Configuration within the Trust Chain;
  6. the Wallet Instance evaluates the requested Digital Credentials and checks the eligibility of the Relying Party in asking for these by applying the policies related to that specific Relying Party, obtained with the Trust Chain;
  7. the Wallet Instance asks User disclosure and consent by showing the Relying Party's identity and the requested attributes;
  8. the Wallet Instance presents the requested information to the Relying Party, along with the Wallet Attestation. The Relying Party validates the presented Credentials by verifying the trust with their Issuers and checks the Wallet Attestation to ensure the Wallet Provider is trusted;
  9. the Wallet Instance informs the User about the successful authentication with the Relying Party, and the User continues the navigation.

Below is a sequence diagram that summarizes the interactions between all the involved parties.

.. figure:: ../../images/cross_same_device_auth_seq_diagram.svg
    :figwidth: 100%
    :align: center
    :target: https://www.plantuml.com/plantuml/svg/ZLR1RXit4BtpAmRgeJ6Gk4cF1bp4KLtRILkhjX8VgaAWk2E9zOhSaiDLrAB_tY6ffIb70MhuikJCUuzlPaYzzIGTXKqhP21hmcQ1JWXneSWw67tqw4OWFGGX5lPpNlZMmu_OQuL-1D_yh5ThUjS651tZQAKxQGX63x9jaU36CBnHc32sXo61eLx95HhA35AWQO1PzbHtsEwqMS64atPVPJeCcvaNjnU1rZ1kDGEV9EJ-MGPBek21sJghz-mU2pl_IKMwbuGGH81NFx2sCtZ01ToZY-S68tkzagIjgKAbQB1Eb36pnpEumxy2UeA9iuIAiE4LRuDJACJvEI-ZPwq93YPhwH7EpmjkLD_Z03Ls6DSaU4fxaksOcOKDh9qiF5aAojf7VIJLPJ7pu3IuBAEEue9rhB56ebt778pUO9GFobdl-ICvOHrukS7ycO6oNMlQjD0n0cmrr-Etkx5jKlZQuPBL6PBQw1NG6Y6uDaNDZ4fbc-lcPItqPJxkI_YzMfnlaDQs-QDsdRqIU-F36TolxJRXP_AiXXKmYNfC6qdB8X1PSr0y-MJ_LeYLiw5Z_wmV6X-iQNTY6tcspAEaOGvWajH58ZPDthhjq2IcP_C0ikjcfhLAjibga86Z36cLkwfWNyOIHntaWgVaKi8hHWaXMmAzX2-j0HtxUfyqkRsV2W20xL1gRiTUDqKQvyX6aWIoYQ72AwEI02gtqtTfdYAsFZ6XCZeUKybEBdIhIQCNs7hy7wAlBgUnOCOIT7bAH7M2CbYHpkkLmMO01BluC_RgqjdDrq-JQjNZKAoZ4C_QwqXb3YuW-6MmKPe6Eikjfj6Nf4_ez7ANc2G5Xs2NbVfoeDjCNR9agvjgU3doq-I5Fya1uSc8PUnkQv9HXtTO1XfRizHkWytXLLKCZKq2yVwqJl-TEf6XVHSHOMPoJVfkJlOHJHdAhhg_vZuiDjhxsCErRSTx9DkXvQB5mrim4LH9nO2giIw8qEVuKnQNFwk0eRyT2zSUuWimkFqJydBAv3skqz49rJxrdSEUnJIdbPezrTWnZ24jMxZnFg23QPpHFMIH_FvX2lT3lIiKbgVG-ppD1Ke8nwm8jaV7OVpgtLnTJw_kBYz_5SSppWIyWl4QrIDSsxRXj0-uWtVQDDoKIGhdyS7vVsAznrGS23xkWW18S5rOSAV28sVcnqIRj5wTaIpqgNjpvIQvIASYqbz-9YTLTh_HNhNMOmEIoEb58FH9XaeQzHBOw3AJcWaWpuj3aBtKRMo7qpYRoGbHMVQnAqqGVuV0S9WN-R63aFQR4r5FzVLqEldkpUaR-FxrQxZzy7oUgy_jy7PuveBtBEPUETrHLdxsx8xExGypfeyKmspc8Sc2JiJH9yMZy5bUa5_eOxn_HcoATgZITJMARobrlhoIuFOZELUsmNyF7wxworUl8HFTxK672xuhFqVAxu2tx7hOjFy1
    
    Remote Protocol Flow


The details of each step shown in the previous picture are described in the table below.

.. list-table::
  :widths: 10 50
  :header-rows: 1

  * - **Id**
    - **Description**
  * - **1**, **2**
    - The User requests to access to a protected resource of the Relying Party.
  * - **3**, **4**, **5**
    - The Relying Party creates a state value bound to the user-agent (e.g., using an HTTP secured cookie), the Request Object available for download at the ``request_uri`` location and inspects the user-agent to determine whether the flow occurs on the same device of the user-agent or not.
  * - **6**, **7**, **8**, **9**
    - The Relying Party provides the user-agent with a JavaScript page inspecting the status endpoint and the Wallet Instance with a URL containing the Authorization Request. In the **Cross Device Flow**, the Request URI is presented as a QR Code displayed to the User. The User scans the QR Code using the Wallet Instance and retrieves a URL with the parameters ``client_id``, ``request_uri``, ``state`` and ``request_uri_method``. Conversely, in the **Same Device Flow**, the Relying Party initiates the request using a link (e.g., an HTML anchor element with an ``href`` attribute) that points to the request URL, providing the same information as in the Cross-Device Flow.
  * - **10**, 
    - The Wallet Instance evaluates the trust with the Relying Party.
  * - **11**, **12**
    - The Wallet Instance checks if the Relying Party has provided the ``request_uri_method`` within its signed Request Object. If it is provided and is equal to ``post``, the Wallet Instance SHOULD provide its metadata to the Relying Party. The Relying Party updates the Request Object according with the Wallet technical capabilities.
  * - **13**
    - When the Wallet Instance capabilities discovery is not supported by Relying Party, the Wallet Instance requests the signed Request Object using the HTTP method GET.
  * - **14**
    - The Relying Party issues the Request Object signing it using one of its cryptographic private keys, where their public parts have been published within its Entity Configuration (`metadata.openid_credential_verifier.jwks`). The Wallet Instance obtains the signed Request Object.
  * - **15**, **16**, **17**
    - The Request Object, in the form of signed JWT, is verified by the Wallet Instance. The Wallet Instance processes the Relying Party metadata and applies the policies related to the Relying Party, attesting whose Digital Credentials and User data the Relying Party is granted to request.
  * - **18**, **19**
    - The Wallet Instance requests the User's consent to disclose the requested Credentials by showing the Relying Party's identity and the requested attributes. The User authorizes and consents the presentation of the Credentials by selecting/deselecting the personal data to release.
  * - **20**
    - The Wallet Instance provides the Authorization Response to the Relying Party using an HTTP request with the method POST (response mode "direct_post.jwt").
  * - **21**, **22**, **23**, **24**, **25** 
    - The Relying Party verifies the Authorization Response, extracts the Wallet Attestation to establish the trust with the Wallet Solution. The Relying Party extracts the Digital Credentials and attests the trust to the Credentials Issuer and the proof of possession of the Wallet Instance about the presented Digital Credentials. Finally, the Relying Party verifies the revocation status of the presented Digital Credentials. If all previous verifications yelded positive result, the Relying Party updates the User session.
  * - **26**
    - The Relying Party provides to the Wallet Instance the response about the presentation, which informs the User.
  * - **27**, **28**
    - The JavaScript page inspecting the status endpoint has the redirection URI with ''response_code'' returned by the Relying Party.
  * - **29**
    - The user-agent is redirected to the redirect URI to continue the navigation with the protected resource made available to the User.


Request URI with HTTP POST
--------------------------

The Relying Party SHOULD provide the POST method with its ``request_uri`` endpoint
allowing the Wallet Instance to inform the Relying Party about its technical capabilities.

This feature can be useful when, for example, the Wallet Instance supports 
a restricted set of features, supported algorithms or a specific url for 
its ``authorization_endpoint``, and any other information that it deems necessary to
provide to the Relying Party for interoperability.

.. warning::
    The Wallet Instance, when providing its technical capabilities to the 
    Relying Party, MUST NOT include any User information or other explicit 
    information regarding the hardware used or usage preferences of its User.

If both the Relying Party and the Wallet Instance
support the ``request_uri_method`` with HTTP POST,
the Wallet Instance capabilities (metadata) MUST 
be provided using an HTTP request to the `request_uri` endpoint of the Relying Party, with the method POST and content type set to `application/x-www-form-urlencoded`.

A non-normative example of the request object encoded in JSON, prior to being encoded in `application/x-www-form-urlencoded` by the Wallet for the Relying Party.
    
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

The response of the Relying Party is defined in the section below.


Authorization Request Details
-----------------------------

The Relying Party MUST create a Request Object in the form of a signed JWT and
MUST provide it to the Wallet Instance through an HTTP URL (request URI). 
The HTTP URL points to the web resource where the signed Request Object is 
available for download. The URL parameters contained in the Relying Party 
response, containing the request URI, are described in the Table below.

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

Below is a non-normative example of the response containing the required parameters previously described.

.. code-block:: javascript

  https://wallet-solution.digital-strategy.europa.eu/authorization?client_id=...&request_uri=...&request_uri_method=post

The value corresponding to the `request_uri` endpoint SHOULD be randomized, according to `RFC 9101, The OAuth 2.0 Authorization Framework: JWT-Secured Authorization Request (JAR) <https://www.rfc-editor.org/rfc/rfc9101.html#section-5.2.1>`_ Section 5.2.1.


In the **Same Device Flow** the Relying Party uses an HTTP response redirect (with status code set to 302) or an html page with an href button, containing the URL represented in the following non-normative example:

.. code:: text

    HTTP/1.1 /authorization Found
    Location: https://wallet-solution.digital-strategy.europa.eu?
    client_id=https%3A%2F%2Frelying-party.example.org%2Fcb
    &request_uri=https%3A%2F%2Frelying-party.example.org%2Frequest_uri
    &request_uri_method=post


In the **Cross Device Flow**, a QR Code is shown by the Relying Party to the User in order to provide the Authorization Request. The User frames the QR Code using their Wallet Instance.

Below is represented a non-normative example of a QR Code issued by the Relying Party.

.. figure:: ../../images/verifier_qr_code.svg
    :figwidth: 50%
    :align: center


Below is represented a non-normative example of the QR Code raw payload:

.. code-block:: text

  https://wallet-solution.digital-strategy.europa.eu/authorization?client_id=https%3A%2F%2Frelying-party.example.org&request_uri=https%3A%2F%2Frelying-party.example.org&request_uri_method=post

.. note::
    The *error correction level* chosen for the QR Code MUST be Q (Quartily - up to 25%), since it offers a good balance between error correction capability and data density/space. This level of quality and error correction allows the QR Code to remain readable even if it is damaged or partially obscured.


Request URI Request
----------------------

The request and its parameters are defined in Section number 5 (Authorization Request) of `OpenID4VP`_.
Below are the normative details and references about the parameters to be used by the Wallet Instance in the request.

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


Below is a non-normative example of an HTTP request made by the Wallet Instance to the Relying Party.

.. code-block:: javascript

  POST /request HTTP/1.1
  Host: client.example.org
  Content-Type: application/x-www-form-urlencoded

  wallet_metadata%3D%7B%22authorization_endpoint%22%3A%20%22eudiw%3A%22%2C%20%22response_types_supported%22%3A%20%5B%22vp_token%22%5D%2C%20%22response_modes_supported%22%3A%20%5B%22form_post.jwt%22%5D%2C%20%22vp_formats_supported%22%3A%20%7B%22dc%2Bsd-jwt%22%3A%20%7B%22sd-jwt_alg_values%22%3A%20%5B%22ES256%22%2C%20%22ES384%22%5D%7D%7D%2C%20%22request_object_signing_alg_values_supported%22%3A%20%5B%22ES256%22%5D%7D%2C%20wallet_nonce%3D%22qPmxiNFCR3QTm19POc8u%22

.. note::

  The ``wallet_nonce`` parameter is RECOMMENDED for Wallet Instances that want to prevent reply of their http requests to the Relying Parties. 
  When present, the Relying Party MUST evaluate it.


.. note::

  For the ``authorization_endpoint`` the use of universal links are preferred over custom url-schemes because, when properly configured using Assetlinks JSON for Android and Apple App Site Association for iOS, they provide enhanced security by reducing the risk of URL hijacking. 
  Furthermore, universal links offer fallback mechanisms, allowing the flow to continue seamlessly in a browser even if the Wallet Instance is not installed, ensuring a smoother User experience. To ensure interoperability, support custom url-schemes is also RECOMMENDED according to OpenID4VC High Assurance Interoperability Profile (HAIP)  `OPENID4VC-HAIP`_, and in particular using the custom url ``haip://``.

Request Object Details
----------------------

The Relying Party issues the signed Request Object using the content type set to ``application/oauth-authz-req+jwt``,
where a non-normative example in the form of decoded header and payload is shown below:

.. code-block:: text

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
  .
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
          "format": "jwt",
          "claims": [
              {"path": ["iss"]},
              {"path": ["iat"]},
              {"path": ["cnf"]}
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
~~~~~~~~~~~~~~~~~~~~~~~~~~~

When the Relying Party encounters errors while issuing the Request Object from the ``request_uri`` endpoint, it MUST return an error response with ``application/json`` as the content type and MUST include the following parameters:

    - ``error``: The error code.
    - ``error_description``: Text in human-readable form providing further details to clarify the nature of the error encountered.

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

.. code-block:: 

  HTTP/1.1 500 Internal Server Error
  Content-Type: application/json

  {
   "error": "server_error",
   "error_description": "The request_uri cannot be retrieved due to an internal server error."
  }

Upon receiving an error response, the Wallet Instance SHOULD inform the User of the error condition in an appropriate manner. The Wallet Instance SHOULD log the error and MAY attempt to recover from certain errors if feasible. For example, if the error is ``server_error``, the Wallet Instance SHOULD prompt the User to re-enter or scan a new QR code, if applicable.

Authorization Error Response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are cases where the Wallet Instance cannot validate the Request Object or the Request Object results invalid. This error occurs if the Request Object is successfully fetched from the url provided in the parameter ``request_uri`` but fails the validation checks. This could be due to incorrect signatures, malformed claims, or other validation failures, such as the revocation of the Relying Party.

If the Wallet Instance encounters any error during the evaluation of the Authorization Request, it MUST notify the Relying Party by sending an Authorization Error Response. 
The Wallet Instance sends the Authorization Error Response to the Relying Party  ``response_uri`` endpoint using an HTTP POST request. 
The Authorization Error Response MUST be encoded in the request body using the format defined by the ``application/x-www-form-urlencoded`` content type.

Below is a non-normative example of an Authorization Error Response.

.. code-block:: 

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
     

Authorization Response Details
------------------------------

After obtaining the User authorization and consent for the presentation of the Credentials, the Wallet Instance sends the Authorization Response to the Relying Party ``response_uri`` endpoint, the content SHOULD be encrypted according `OpenID4VP`_ Section 7.3, using the Relying Party public key.

.. note::
    **Why the response is encrypted?**

    The response sent from the Wallet Instance to the Relying Party is encrypted to prevent a malicious agent from gaining access to the plaintext information transmitted within the Relying Party's network. This is only possible if the network environment of the Relying Party employs `TLS termination <https://www.f5.com/glossary/ssl-termination>`_. Such technique employs a termination proxy that acts as an intermediary between the client and the webserver and handles all TLS-related operations. In this manner, the proxy deciphers the transmission's content and either forwards it in plaintext or by negotiates an internal TLS session with the actual webserver's intended target. In the first scenario, any malicious actor within the network segment could intercept the transmitted data and obtain sensitive information, such as an unencrypted response, by sniffing the transmitted data.

Below is a non-normative example of the request:

.. code-block:: http

  POST /response_uri HTTP/1.1
  HOST: relying-party.example.org
  Content-Type: application/x-www-form-urlencoded
  
  response=eyJhbGciOiJFUzI1NiIs...9t2LQ
  

Below is a non-normative example of the decrypted payload of the JWT contained in the ``response``, before base64url encoding.
The `vp_token` parameter value corresponds to the format used when the DCQL query language is used in the presentation request.

.. code-block:: 

  {
    "state": "3be39b69-6ac1-41aa-921b-3e6c07ddcb03",
    "vp_token": {
        "personal id data": "eyJhbGciOiJFUzI1NiIs...PT0iXX0",
        "wallet attestation": $WalletAttestation-JWT
    }
  }

Where the following parameters are used:

.. list-table::
  :widths: 25 50
  :header-rows: 1

  * - **Name**
    - **Description**
  * - **vp_token**
    - There MUST be at least two signed presentations in this Array:

      - The requested Digital Credential (one or more, in format of SD-JWT VC)
      - The Wallet Attestation
      
      When `presentation_definition` is used, the ``vp_token`` value is a JSON Array containing the Verifiable Presentation(s) and the `presentation_submission` parameter MUST be also present within the response.

      When the DCQL query language is used, the ``vp_token`` format is a JSON Object which keys corresponds to the requested credential ids in the ``dcql_query`` used in the request, and the values to each presented Digital Credential.

  * - **state**
    - Unique identifier provided by the Relying Party within the Authorization Request.


SD-JWT Presentation
-------------------

SD-JWT defines how an Holder can present a Credential to a Verifier proving the legitimate possession
of the Credential. For doing this the Holder MUST include the ``KB-JWT`` in the SD-JWT,
by appending the ``KB-JWT`` at the end of the of the SD-JWT, as represented in the example below:

.. code-block::

  <Issuer-Signed-JWT>~<Disclosure 1>~<Disclosure 2>~...~<Disclosure N>~<KB-JWT>

To validate the signature on the Key Binding JWT, the Verifier MUST use the key material included in the Issuer-Signed-JWT.
The Key Binding JWT (KB-JWT) signature validation MUST use the public key included in the SD-JWT,
using the ``cnf`` parameter contained in the Issuer-Signed-JWT.

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


When an SD-JWT is presented, the KB-JWT signature MUST be verified by the same public key included in the SD-JWT within the `cnf` parameter. 
The KB-JWT MUST contain the following parameters in the JWT payload:

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


Revocation Checks
~~~~~~~~~~~~~~~~~

The revocation mechanisms that the Relying Parties MUST implement are defined in `Digital Credential Revocation and Suspension section`_.

In the context of Digital Credential evaluation, any Relying Party establishes internal policies that define the meaning and value of presented Credentials. This is particularly important in scenarios where a Credential may be suspended but still holds value for certain purposes. For example, a suspended mobile driving license might still be valid for verifying the age of the Holder.

The process begins with the Relying Party requesting specific Credentials to the Holder. This request should align with the Relying Party's requirements and the context in which the Credentials will be used. The Holder then responds by releasing the requested Credentials.

Upon receiving the Credentials, the Relying Party evaluates their validity and value based on its internal policies. This evaluation considers the current status of the Credential (e.g., active, suspended, revoked) and the specific use case for which the Credential is being presented.

Relying Parties should develop comprehensive internal policies that outline how different types of Credentials are to be evaluated. These policies should address scenarios where a Credential may be partially valid or have limited applicability. Flexibility in evaluation processes is important to accommodate various use cases. For instance, a Credential that is suspended for driving purposes might still be acceptable for age verification.

Relying Party Response
~~~~~~~~~~~~~~~~~~~~~~

If any validation check performed by the Relying Party on the Authorization Response from the Wallet Instance fails, the Response URI endpoint MUST return an error response. The structure of this error response should be determined by the specific nature of the error encountered. The response MUST use ``application/json`` as the content type and MUST include the following parameters:

    - ``error``: The error code.
    - ``error_description``: Text in human-readable form providing further details to clarify the nature of the error encountered.

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

.. code-block:: text

  HTTP/1.1 403 Forbidden
  Content-Type: application/json

  {
    "error": "invalid_request",
    "error_description": "Trust cannot be established with the issuer: https://issuer.example.com"
  }


.. code-block:: text

  HTTP/1.1 400 Bad Request
  Content-Type: application/json

  {
    "error": "invalid_request",
    "error_description": "The vp_token is malformed, missing required parameters or incorrectly formatted"
  }

Redirect URI
------------

As defined in Section 7.2. (Response Mode "direct_post") of the `OpenID4VP`_ specification, if the Response URI has successfully processed the Authorization Response or Authorization Error Response, it MUST respond with an HTTP status code of 200 with ``Content-Type`` of ``application/json`` and a JSON object in the response body. If the User has been correctly authenticated, the Relying Party MUST add the ``redirect_uri`` parameter to the JSON object in the response body. 

.. note::
    In the **Cross Device Flow** the Relying Party uses the ``redirect_uri`` parameter to the user-agent, whereas in the **Same Device Flow** it may also pass the ``redirect_uri`` to the Wallet Instance. When the ``redirect_uri`` is passed through the user-agent and the response sent to the Wallet Instance does not contain the ``redirect_uri`` parameter, the Wallet Instance is not required to perform any further step.

Upon receiving the ``redirect_uri`` from the Relying Party, the receiver (either the user-agent or the Wallet Instance) MUST perform a redirect to the URL specified by the ``redirect_uri``.  This redirect allows the Relying Party to seamlessly resume interaction with the User on the device which initiated the flow, after the Wallet Instance has transmitted the Authorization Response to the designated ``response_uri``.

The Relying Party MUST include a response code within the redirect URI. The response code is a fresh, cryptographically random number used to ensure only the receiver of the redirect can fetch and process the Authorization Response. The number could be added as a path component, as a parameter or as a fragment to the URL. It is RECOMMENDED to use a cryptographic random value of 128 bits or more at the time of the writing of this specification.
Even if an adversary manages to steal the random value used in the request to the status endpoint, their user-agent would be rejected due to the missing cookie in the request.

The following is a non-normative example of the response from the Relying Party to the Wallet Instance upon receiving the Authorization Response at the Response Endpoint.


.. code-block:: http

  HTTP/1.1 200 OK
  Content-Type: application/json

  {
    "redirect_uri": "https://relying-party.example.org/cb?response_code=091535f699ea575c7937fa5f0f454aee"
  }

The ``redirect_uri`` value MUST be used with an HTTP method GET by either the Wallet Instance or the user-agent to redirect the User to a specific Relying Party's endpoint in order to complete the process. The value can be added as a path component, as a fragment or as a parameter to the URL according to Section 6.2 of `OpenID4VP`_. In general, the specific entity that performs this action depends on whether the flow is Same device or Cross device; however, in the case described above, the redirection will always be performed by the user-agent.

.. warning::
    For security reasons and to prevent endpoint mix-up attacks, the value contained in the ``redirect_uri`` parameter MUST be one of those attested by a trusted third party, such as those provided in the ``openid_credential_verifier`` metadata within the ``redirect_uris`` parameter, obtained from the Trust Chain about the Relying Party.

Redirect URI Errors
~~~~~~~~~~~~~~~~~~~

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

Device Flow Status Checks and Security
--------------------------------------

This specification introduces the Relying Party Presentation Request Status Endpoint for implementations that want to use it, as this endpoint is an internal feature for the security of the implementation and is not required for interoperability.

Be the flow Same Device or Cross Device, the user-agent needs to check the session status to the endpoint made available by Relying Party (status endpoint).
This check MAY be implemented in the form of JavaScript code, within the page that shows the QRCode or the href button pointing to the request URL.
The JavaScript code makes the user-agent check the status endpoint using a polling strategy in seconds or a push strategy (e.g., web socket).

Whatever Device Flow is detected by the Relying Party (e.g., by inspecting the user-agent),
the page using the JavaScript code inspecting the status endpoint is always returned to the user-agent.

In the Cross Device Flow the html page that checks the status endpoint also contains the QR Code.
Using the Same Device Flow, the page that checks the status endpoint contains an ``href`` button
or ``http-equiv`` meta header parameter, redirecting to the URL defined at the section "Authorization Request Details".

Since the html page and the status endpoint are implemented by the Relying Party,
it is under the Relying Party responsability the implementation details of this solution,
because this is related to the Relying Party's internal API. However, the text below describes an implementation example.

The Relying Party binds the request of the user-agent, with a session cookie marked as ``Secure`` and ``HttpOnly``, with the issued request.
The request url SHOULD include a parameter with a random value. The HTTP response returned by this status endpoint MAY contain the HTTP status codes listed below:

* **201 Created**. The signed Request Object was issued by the Relying Party that waits to be downloaded by the Wallet Instance at the **request_uri** endpoint.
* **202 Accepted**. This response is given when the signed Request Object was obtained by the Wallet Instance.
* **200 OK**. The Wallet Instance has provided the presentation to the Relying Party's  **response_uri** endpoint and the User authentication is successful. The Relying Party updates the session cookie allowing the user-agent to access to the protected resource. A redirect URL is provided carrying the location where the user-agent is intended to navigate.

If instead any validation check performed by the Relying Party fails, the QRCode page SHOULD be updated with an error message. Moreover, the Response URI endpoint MUST return an error response, whose structure depends on the nature of the error. The response MUST use ``application/json`` as the content type and MUST include the following parameters:

  - ``error``: The error code.
  - ``error_description``: Text in human-readable form providing further details to clarify the nature of the error encountered.

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

Below is a non-normative example of the HTTP Request to the status endpoint, where the parameter ``id`` contains an opaque and random value:

.. code::

  GET /session-state?id=3be39b69-6ac1-41aa-921b-3e6c07ddcb03
  HTTP/1.1
  HOST: relying-party.example.org


.. _Digital Credential Revocation and Suspension section: credential-revocation.html



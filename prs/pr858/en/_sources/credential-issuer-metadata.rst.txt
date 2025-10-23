.. include:: ../common/common_definitions.rst

Credential Issuer Metadata
--------------------------

Metadata for oauth_authorization_server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The *oauth_authorization_server* metadata MUST contain the following parameters.

.. list-table::
  :class: longtable
  :widths: 20 60
  :header-rows: 1

  * - **Claim**
    - **Description**
  * - **issuer**
    - It MUST contain an HTTPS URL that uniquely identifies the Credential Issuer.
  * - **pushed_authorization_request_endpoint**
    - The URL of the pushed authorization request endpoint is where a Wallet Instance MUST submit an authorization request to obtain a *request_uri* value, which can then be used at the authorization endpoint. See :rfc:`9126#as_metadata`.
  * - **authorization_endpoint**
    - URL of the authorization server's authorization endpoint. See :rfc:`8414#section-2`.
  * - **token_endpoint**
    - URL of the authorization server's token endpoint. See :rfc:`8414#section-2`.
  * - **client_registration_types_supported**
    - Array specifying the registration types supported. The authorization server MUST support *automatic*. See `OID-FED`_ Section 5.1.3.
  * - **code_challenge_methods_supported**
    - JSON array containing a list of Proof Key for Code Exchange (PKCE) :rfc:`7636` code challenge methods supported by the authorization server. The authorization server MUST support *S256*.
  * - **acr_values_supported**
    - See `OpenID Connect Discovery 1.0 Section 3 <https://openid.net/specs/openid-connect-discovery-1_0.html#ProviderMetadata>`_. The supported values are:

      - `https://trust-anchor.eid-wallet.example.it/loa/low`
      - `https://trust-anchor.eid-wallet.example.it/loa/substantial`
      - `https://trust-anchor.eid-wallet.example.it/loa/high`
  * - **scopes_supported**
    - JSON array containing a list of the supported *scope* values. See :rfc:`8414#section-2`.
  * - **response_modes_supported**
    - JSON array containing a list of the supported "response_mode" values, as specified in `OAuth 2.0 Multiple Response Type Encoding Practices <https://openid.net/specs/oauth-v2-multiple-response-types-1_0.html>`_. The supported values MAY be *query* and *form_post.jwt* (see `JARM`_).
  * - **response_types_supported**
    - JSON array containing a list of the supported "response_type" values, as specified in :rfc:`8414`. The supported value MUST be *code*.
  * - **authorization_signing_alg_values_supported**
    - JSON array containing a list of the :rfc:`7515` supported signing algorithms (*alg* values). The values MUST be set according to Section :ref:`algorithms:cryptographic algorithms`. See Section 4 of `JARM`_.
  * - **grant_types_supported**
    - JSON array containing a list of the supported grant type values. The authorization server MUST support *authorization_code*.
  * - **token_endpoint_auth_methods_supported**
    - JSON array containing a list of supported client authentication methods. The Token Endpoint MUST support *attest_jwt_client_auth* as defined in `OAUTH-ATTESTATION-CLIENT-AUTH`_.
  * - **token_endpoint_auth_signing_alg_values_supported**
    - JSON array containing a list of the signing algorithms ("*alg*" values) supported by the token endpoint for the signature on the JWT used to authenticate the client at the Token Endpoint. See :rfc:`8414#section-2`.
  * - **request_object_signing_alg_values_supported**
    - JSON array containing a list of the signing algorithms ("*alg*" values) supported for Request Objects. See `[openid-connect-discovery-1_0] <https://openid.net/specs/openid-connect-discovery-1_0.html#ProviderMetadata>`_.
  * - **dpop_signing_alg_values_supported**
    - JSON array containing a list of the signing algorithms ("*alg*" values) supported for DPoP proof JWTs. See :rfc:`9449`.
  * - **jwks**
    - JSON Web Key Set containing the cryptographic keys for the authorization server. See `OID-FED`_ Section 5.2.1 and `JWK`_.

Metadata for openid_credential_issuer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The *openid_credential_issuer* metadata MUST contain the following claims.

.. list-table::
  :class: longtable
  :widths: 20 60
  :header-rows: 1

  * - **Claim**
    - **Description**
  * - **credential_issuer**
    - The Credential Issuer identifier. It MUST be a case sensitive URL using HTTPS scheme as defined in `OpenID4VCI`_ Sections 11.2.1 and 11.2.3.
  * - **logo_uri**
    - URL of the entity's logo that will be shown to the User during Wallet Instance interactions. See `OID-FED`_ Section 5.2.2.
  * - **credential_endpoint**
    - URL of the Credential endpoint. See `OpenID4VCI`_ Section 11.2.3.
  * - **nonce_endpoint**
    - URL of the Nonce Endpoint, as defined in Section 7 of `OpenID4VCI`_.
  * - **revocation_endpoint**
    - URL of the revocation endpoint. See :rfc:`8414#section-2`.
  * - **deferred_credential_endpoint**
    - URL of the deferred Credential endpoint, as defined in Section 11.2.3 of `OpenID4VCI`_.
  * - **status_assertion_endpoint**
    - It MUST be an HTTPs URL indicating the endpoint where the Wallet Instances can request Status Assertions. See Section :ref:`credential-revocation:Digital Credential Lifecycle` for more details. (`OAUTH-STATUS-ASSERTION`_ Section 11.1.).
  * - **notification_endpoint**
    - It MUST be an HTTPs URL indicating the notification endpoint. See Section 11.2.3 of [`OpenID4VCI`_].
  * - **authorization_servers**
    - OPTIONAL. Array of strings, where each string is an identifier of the OAuth 2.0 Authorization Server (as defined in [:rfc:`8414`]) the Credential Issuer relies on for authorization. If this parameter is omitted, the entity providing the Credential Issuer is also acting as the Authorization Server.
  * - **display**
    - See `OpenID4VCI`_ Section 11.2.3. Array of objects containing display language properties. The parameters that MUST be included are:

        - **name**: String value of a display name for the Credential Issuer.
        - **locale**: String value that identifies the language of this object represented as a language tag taken from values defined in *BCP47* :rfc:`5646`. There MUST be only one object for each language identifier.

  * - **credential_configurations_supported**
    - JSON object that outlines the details of the Digital Credentials supported by the Credential Issuer. It includes a list of name/value pairs, where each name uniquely identifies a specific supported Digital Credential. This identifier is utilized to inform the Wallet Instance which Digital Credential can be provided by the Credential Issuer. The associated value within the object MUST contain metadata specific to that Digital Credential, as defined following. See `OpenID4VCI`_ Sections 11.2.3 and A.3.2.

        - **format**: String identifying the format of this Credential. The Digital Credential MUST support the value string "*dc+sd-jwt*" in case of SD-JWT VC (See `OpenID4VCI`_ Section A.3.1.) and "*mso_mdoc*" in case of mdoc (see `OpenID4VCI`_ Section A.2.1.).
        - **scope**: JSON String identifying the supported *scope* value. The Wallet Instance MUST use this value in the Pushed Authorization Request. Scope values MUST be the entire set or a subset of the *scope* values in the *scopes_supported* parameter of the Authorization Server. If the Credential is included in the Digital Credentials Catalog the *scope* value MUST match with the ``credential_type`` parameter defined in :ref:`registry:Digital Credentials Catalog Structure`. [See `OpenID4VCI`_ Section 11.2.3].
        - **cryptographic_binding_methods_supported**: JSON Array of case sensitive strings that identify the representation of the cryptographic key material that the issued Digital Credential is bound to. The Credential Issuer MUST support the value "*jwk*" for "dc+sd-jwt" format and "*cose_key*" for "mso_mdoc".
        - **credential_signing_alg_values_supported**: JSON Array of case sensitive strings that identify the algorithms that the Credential Issuer MUST support to sign the issued Digital Credential. See Section :ref:`algorithms:cryptographic algorithms` for more details.
        - **proof_types_supported**: JSON object which provides detailed information about the key proof(s) supported by the Credential Issuer. It consists of a list of name/value pairs, where each name uniquely identifies a supported proof type. The Credential Issuer MUST support at least "*jwt*" as defined in `OpenID4VCI`_ Section 8.2. The value associated with each name/value pair is a JSON object containing metadata related to the key proof. The Credential Issuer MUST support at least the parameter **proof_signing_alg_values_supported** which MUST be a JSON Array of case sensitive strings that identify the supported algorithms (see Section :ref:`algorithms:cryptographic algorithms` for more details about the supported algorithms).
        - **display**: REQUIRED only if the Digital Credential is not included in the Digital Credentials Catalog. Array of objects containing display language properties. Otherwise it MUST not be present. The following parameters are included:

                - **name**: REQUIRED. String value of a display name for the Digital Credential.
                - **locale**: REQUIRED. String value that identifies the language of this object represented as a language tag taken from values defined in *BCP47* :rfc:`5646`. There MUST be only one object for each language identifier.
                - **logo**: OPTIONAL. Object with information about the logo of the Digital Credential. The following parameters are included:

                  - **uri**: REQUIRED. String value that contains a URI where the Wallet can obtain the logo of the Digital Credential from the Credential Issuer.
                  - **uri#integrity**: REQUIRED. integrity metadata as defined in Section 3 of `W3C-SRI`_.
                  - **alt_text**: OPTIONAL. String value of the alternative text for the logo image.
                
                - **description**: REQUIRED. String value containing a description of the Digital Credential.
                - **background_color**: OPTIONAL. String value of a background color of the Digital Credential represented as numerical color values defined in `W3C.CSS-COLOR`_.
                - **background_image**: OPTIONAL. Object containing ``uri`` parameter indicating where the Wallet can obtain the background image of the Digital Credential from the Credential Issuer.
                - **text_color**: String value of a text color of the Digital Credential represented as numerical color values defined in `W3C.CSS-COLOR`_.

        - **vct**: REQUIRED only if ``format`` is set to "*dc+sd-jwt*". As defined in [:ref:`credential-data-model:SD-JWT-VC Credential Format`].
        - **doctype**: REQUIRED only if ``format`` is set to "*mso_mdoc*". As defined in [:ref:`credential-data-model:mDoc-CBOR Credential Format`].
        - **schema_uri**: REQUIRED only if the Digital Credential is not included in the Digital Credentials Catalog. URI pointing to the schema related to the format.
        - **schema_uri#integrity**: REQUIRED only if **schema_uri** is present. Cryptographic digest of the schema specification for integrity verification. It MUST be a string of the form ``{digest_method}-{digest_value}``, where ``{digest_method}`` is the digest algorithm used (e.g., ``sha-256``) and ``{digest_value}`` is the base64url-encoded digest value.
        - **authentic_source**: REQUIRED only if the Digital Credential is not included in the Digital Credentials Catalog. Object containing ``entity_id`` parameter valued with the identifier referencing authorized Authentic Sources as registered in the :ref:`registry:Authentic Source Registry`.
        - **claims**: REQUIRED only if the Digital Credential is not included in the Digital Credentials Catalog. Array of JSON object each describing how a certain claim related to the Digital Credential MUST be displayed to the User. This Array lists the claims in the order they MUST be displayed by the Wallet. To provide detailed information about the claim, the innermost value MUST contain at least the following parameters. See `OpenID4VCI`_ Section A.3.2.

            - **path**: It contains the pointer that specifies the path to a specific claim within the Digital Credential as defined in Appendix C of `OpenID4VCI`_.
            - **display**: Array of objects containing display language properties. The parameters that MUST be included are

                - **name**: String value of a display name for the claim.
                - **locale**: String value that identifies the language of this object represented as a language tag taken from values defined in *BCP47* :rfc:`5646`. There MUST be only one object for each language identifier.
  * - **jwks**
    - JSON Web Key Set document, passed by value, containing the protocol specific keys for the Credential Issuer. See `OID-FED`_ Section 5.2.1 and `JWK`_.
  * - **trust_frameworks_supported**
    - JSON array containing all supported trust frameworks. See `OIDC-IDA`_ Section 8. The supported values are:
        - *it_cie*: CIE id trust framework supported.
        - *it_wallet*: IT-Wallet trust framework supported.
        - *eudi_wallet*: Member State EUDI Wallet trust framework supported.
        - *it_l2+document_proof*: eID Substantial Authentication with MRTD Verification protocol supported.
  * - **evidence_supported**
    - JSON array containing all types of identity evidence supported by the Credential Issuer. See `OIDC-IDA`_ Section 8. The supported value is ``vouch``.
  * - **credential_hash_alg_supported**
    - The supported algorithm used by the Wallet Instance to hash the Digital Credential for which the Status Assertion is requested. It is RECOMMENDED to use *sha-256*. (See `OAUTH-STATUS-ASSERTION`_ Section 11.1.).
  * - **batch_credential_issuance**
    - Object containing information about the Credential Issuer's support for issuance of Digital Credentials in a batch at the Credential Endpoint. The presence of this parameter means that the Credential Issuer supports the ``proofs`` parameter in the Credential request so can issue more than one Digital Credential for the same Credential with the same attributes about the Holder in a single request/response. The parameter that MUST be included is:


            - **batch_size**: Integer value specifying the maximum array size for the ``proofs`` parameter in a Credential request.


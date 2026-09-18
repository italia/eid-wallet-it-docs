.. include:: ../common/common_definitions.rst
.. Included via relying-party-solution.rst at title level '^' (level 2).


Relying Party Metadata
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The *openid_credential_verifier* metadata contains the Relying Party metadata used by the ``openid_federation`` path (:ref:`test-plans-remote-presentation:Remote Credential Verifier Test Matrix`). It is authoritative only after final Federation policy processing. When the Relying Party's ``client_id`` uses ``x509_hash`` (i.e. the Relying Party has subscribed to the EUDIW Trsut Framework), the signed Request Object's ``client_metadata`` is the authoritative source for Authentication and Authorization and the Entity Configuration is not required.

.. list-table::
   :class: longtable
   :widths: 20 60
   :header-rows: 1

   * - **Claim**
     - **Description**
   * - **client_id**
     - It MUST contain an HTTPS URL that uniquely identifies the RP. See :rfc:`7591#section-3.2.1` and `OpenID Connect Dynamic Client Registration 1.0 <https://openid.net/specs/openid-connect-registration-1_0.html>`_ Section 3.2.
   * - **client_name**
     - Human-readable string name of the RP. See :rfc:`7591#section-2`.
   * - **logo_uri**
     - URL of the entity's logo that will be shown to the User during interactions with the Wallet Instance. See `OID-FED`_ Section 5.2.2. The logo mime type MUST be ``application/svg``.
   * - **application_type**
     - String indicating the type of application. It MUST be set to "*web*" value. See `OpenID Connect Dynamic Client Registration 1.0 <https://openid.net/specs/openid-connect-registration-1_0.html>`_ Section 2.
   * - **request_uris**
     - JSON Array of *request_uri* values that are pre-registered by the RP. These URLs MUST use the *https* scheme. See `OpenID Connect Dynamic Client Registration 1.0 <https://openid.net/specs/openid-connect-registration-1_0.html>`_ Section 2.
   * - **response_uris**
     - JSON Array of response URI strings to which the Wallet Instance MUST send the Authorization Response using an HTTP POST request as defined by the Response Mode ``direct_post`` and ``direct_post.jwt`` (see `OpenID4VP`_ Sections 6.2 and 6.3).
   * - **redirect_uris**
     - JSON Array of redirect URI strings for National ``openid_federation`` same-device endpoint binding. The Wallet Instance MUST validate a redirect URI against this value in the National path.
   * - **encrypted_response_enc_values_supported**
     - JSON array of content encryption algorithms ("enc") the Verifier supports for encrypting the authorization response when using response mode ``direct_post.jwt``. The Verifier MUST support both ``A128GCM`` and ``A256GCM``. See `OpenID4VP`_ Sections 5.1 and 8.3.1.
   * - **vp_formats_supported**
     - JSON object defining the formats and proof types of Verifiable Presentations and Verifiable Credentials the RP supports. It consists of a list of name/value pairs, where each name uniquely identifies a supported type. The RP MUST support at least ``dc+sd-jwt``. For SD-JWT VC, the value associated with each name/value pair MUST include ``sd-jwt_alg_values`` listing acceptable signing algorithms; for mdoc-CBOR, the value MUST include ``issuerauth_alg_values`` and ``deviceauth_alg_values``. The JOSE/COSE headers of presented artifacts MUST match one of the advertised values. See `OpenID4VP`_ §11 and Appendix B.
   * - **jwks**
     - JSON Web Key Set document, passed by value, containing the request-specific ephemeral response-encryption public keys for the Relying Party. Every key MUST have ``kid`` and ``use`` values, and each ``kid`` MUST identify exactly one key. See `JWK`_.
   * - **erasure_endpoint**
     - [CONDITIONAL] JSON String that represents the URI to which the Wallet Instance can request deletion of Users' attributes. This URL MUST use the *https* scheme. Upon receiving an erasure request, the Relying Party MUST uniquely identify one or more Digital Credentials for which the User requests deletion, by applying identity matching.


.. note::
  The parameters **response_uris** and **erasure_endpoint** are introduced in this specification.

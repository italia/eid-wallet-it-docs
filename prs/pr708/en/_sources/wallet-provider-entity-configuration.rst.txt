.. include:: ../common/common_definitions.rst

Wallet Provider Entity Configuration
--------------------------------------

An HTTP GET request to the Federation endpoint allows the retrieval of the Wallet Provider Entity Configuration.

The returned Entity Configuration of the Wallet Provider MUST contain the attributes described in the sections below.

The Wallet Provider Entity Configuration is a signed JWT containing the public keys and supported algorithms of the Wallet Provider. It is structured in accordance with the `OID-FED`_ and the :ref:`trust:The Infrastructure of Trust` outlined in this specification.

Wallet Provider Entity Configuration JWT Header
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Key**
      - **Value**
      - **Reference**
    * - alg
      - Algorithm used to verify the token signature. It MUST be one of the possible values indicated in :ref:`algorithms:Cryptographic Algorithms` (e.g., ES256).
      - `OID-FED`_.
    * - kid
      - Thumbprint of the public key used for the signature.
      - `OID-FED`_ and :rfc:`7638`.
    * - typ
      - Media type, set to ``entity-statement+jwt``.
      - `OID-FED`_.

Wallet Provider Entity Configuration JWT Payload
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Key**
      - **Value**
      - **Reference**
    * - ``iss``
      - REQUIRED. Public URL of the Wallet Provider.
      - `OID-FED`_.
    * - ``sub``
      - REQUIRED. Public URL of the Wallet Provider.
      - `OID-FED`_.
    * - ``iat``
      - REQUIRED. Issuance datetime in Unix Timestamp format.
      - `OID-FED`_.
    * - ``exp``
      - REQUIRED. Expiration datetime in Unix Timestamp format.
      - `OID-FED`_.
    * - ``authority_hints``
      - REQUIRED. Array of URLs (String) containing the list of URLs of the immediate superior Entities, such as the Trust Anchor or an Intermediate, that MAY issue an Entity Statement related to the Wallet Provider.
      - `OID-FED`_.
    * - ``jwks``
      - REQUIRED. A JSON Web Key Set (JWKS) representing the public part of the Wallet Provider's Federation Entity signing keys. The corresponding private key is used by the Entity to sign the Entity Configuration about itself.
      - :rfc:`7517`, `OID-FED`_.
    * - ``metadata``
      - REQUIRED.JSON object that represents the Entity's Types and the metadata for those Entity Types. Each member name of the JSON object is an Entity Type Identifier, and each value MUST be a JSON object containing metadata parameters according to the metadata schema of the Entity Type. It MUST contains the ``wallet_provider`` and OPTIONALLY the ``federation_entity`` metadata.
      - `OID-FED`_.

wallet_provider metadata
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The metadata JSON Object whose key is ``wallet_provider`` contains the following parameters. The public keys found in this object are exclusively used for signing and/or encryption operations required to this Entity when acting as a Wallet Provider (e.g., sign the Wallet Attestations to the Wallet Instance).

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Key**
      - **Value**
      - **Reference**
    * - ``jwks``
      - CONDITIONAL. JSON Web Key Set document, passed by value, containing the Entity's keys for that Entity Type. It MUST be present if ``jwks_uri`` and ``signed_jwks_uri`` are absent.
      - :rfc:`7517`, `OID-FED`_.
    * - ``jwks_uri``
      - CONDITIONAL. URL referencing a JWK Set document containing the Wallet Provider's keys for that Entity Type. This URL MUST use the https scheme. It MUST be present if ``jwks`` and ``signed_jwks_uri`` are absent.
      - `OID-FED`_.
    * - ``signed_jwks_uri``
      - CONDITIONAL. URL referencing a signed JWT having the Entity's JWK Set document for that Entity Type as its payload. This URL MUST use the https scheme. The JWT MUST be signed using a Federation Entity Key. A successful response from the URL MUST use the HTTP status code 200 with the Content Type ``application/jwk-set+jwt``. It MUST be present if ``jwks`` and ``jwks_uri`` are absent.
      - `OID-FED`_.
    * - ``aal_values_supported``
      - OPTIONAL. List of supported values for the certifiable security context. These values specify the security level of the app, according to the levels: low, medium, or high. Authenticator Assurance Level values supported.
      - This specification.

federation_entity metadata
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Key**
      - **Value**
      - **Reference**
    * - ``organization_name``
      - OPTIONAL. A human-readable name representing the organization owning the Wallet Provider.
      - `OID-FED`_.
    * - ``homepage_uri``
      - OPTIONAL. URL of a Web page for the organization owning the Wallet Provider.
      - `OID-FED`_.
    * - ``tos_uri``
      - OPTIONAL. URL that contains the Wallet Provider's terms of service.
      - `OID-FED`_.
    * - ``policy_uri``
      - OPTIONAL. URL of the documentation of conditions and policies relevant to the Wallet Provider.
      - `OID-FED`_.
    * - ``logo_uri``
      - OPTIONAL. String. A URL that points to the logo of the Wallet Provider. The file containing the logo SHOULD be published in a format that can be viewed via the web.
      - `OID-FED`_.

Below is a non-normative example of the Entity Configuration for a Wallet Provider.

.. code-block:: javascript

  {
    "alg": "ES256",
    "kid": "5t5YYpBhN-EgIEEI5iUzr6r0MR02LnVQ0OmekmNKcjY",
    "typ": "entity-statement+jwt"
  }
  .
  {
  "iss": "https://wallet-provider.example.org",
  "sub": "https://wallet-provider.example.org",
  "jwks": {
    "keys": [
      {
        "crv": "P-256",
        "kty": "EC",
        "x": "qrJrj3Af_B57sbOIRrcBM7br7wOc8ynj7lHFPTeffUk",
        "y": "1H0cWDyGgvU8w-kPKU_xycOCUNT2o0bwslIQtnPU6iM",
        "kid": "5t5YYpBhN-EgIEEI5iUzr6r0MR02LnVQ0OmekmNKcjY"
      }
    ]
  },
  "metadata": {
    "wallet_provider": {
      "jwks": {
        "keys": [
          {
            "crv": "P-256",
            "kty": "EC",
            "x": "BxYsu3QvYmOz1fl1l5hGyPWlpvgTzz3AY3j3K_9zGPs",
            "y": "ob34Wmfah_ScQXaYMJWoBkZSwO-kQ0VTgMk4VZfu48w",
            "kid": "749b495837819c00cfee1749b495837819c00cfee1"
          }
        ]
      },
      "aal_values_supported": [
        "https://wallet-provider.example.org/LoA/basic",
        "https://wallet-provider.example.org/LoA/medium",
        "https://wallet-provider.example.org/LoA/high"
      ]
    },
    "federation_entity": {
      "organization_name": "IT-Wallet Provider",
      "homepage_uri": "https://wallet-provider.example.org",
      "policy_uri": "https://wallet-provider.example.org/privacy_policy",
      "tos_uri": "https://wallet-provider.example.org/info_policy",
      "logo_uri": "https://wallet-provider.example.org/logo.svg"
    }
  },
  "authority_hints": [
    "https://registry.eudi-wallet.example.it"
  ]
  "iat": 1687171759,
  "exp": 1709290159
  }


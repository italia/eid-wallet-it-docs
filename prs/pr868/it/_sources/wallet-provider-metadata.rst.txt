.. include:: ../common/common_definitions.rst

Metadati del Fornitore di Wallet
--------------------------------

metadati wallet_provider
^^^^^^^^^^^^^^^^^^^^^^^^

L'oggetto JSON dei metadati la cui chiave è ``wallet_provider`` contiene i seguenti parametri. Le chiavi pubbliche presenti in questo oggetto sono utilizzate esclusivamente per operazioni di firma e/o crittografia richieste a questa Entità quando agisce come Fornitore di Wallet (ad esempio, firmare gli Attestati di Wallet per l'Istanza del Wallet).

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Chiave**
      - **Valore**
      - **Riferimento**
    * - ``jwks``
      - CONDIZIONALE. Documento JSON Web Key Set, passato per valore, contenente le chiavi dell'Entità per quel Tipo di Entità. DEVE essere presente se ``jwks_uri`` e ``signed_jwks_uri`` sono assenti.
      - :rfc:`7517`, `OID-FED`_.
    * - ``jwks_uri``
      - CONDIZIONALE. URL che fa riferimento a un documento JWK Set contenente le chiavi del Fornitore di Wallet per quel Tipo di Entità. Questo URL DEVE utilizzare lo schema https. DEVE essere presente se ``jwks`` e ``signed_jwks_uri`` sono assenti.
      - `OID-FED`_.
    * - ``signed_jwks_uri``
      - CONDIZIONALE. URL che fa riferimento a un JWT firmato avente come payload il documento JWK Set dell'Entità per quel Tipo di Entità. Questo URL DEVE utilizzare lo schema https. Il JWT DEVE essere firmato utilizzando una Chiave di Entità di Federazione. Una risposta positiva dall'URL DEVE utilizzare il codice di stato HTTP 200 con il Content Type ``application/jwk-set+jwt``. DEVE essere presente se ``jwks`` e ``jwks_uri`` sono assenti.
      - `OID-FED`_.
    * - ``logo_uri``
      - OBBLIGATORIO. URL del logo dell’entità che verrà mostrato all’Utente durante le interazioni con l’istanza del Wallet. Il MIME type del logo DEVE essere ``application/svg``.
      - `OID-FED`_ Sezione 5.2.2.
    * - ``wallet_metadata``
      - OBBLIGATORIO. Contiene i parametri relativi ai metadati del Wallet come definiti nella :ref:`Tabella dei parametri dei metadati del portafoglio <table_wallet_metadata_parameters>` e il parametro ``credential_offer_endpoint``.
      - `OpenID4VP`_ Sezione 10.1.

Di seguito è riportato un esempio non normativo della Entity Configuration per un Fornitore di Wallet.

.. code-block:: json

  {
    "alg": "ES256",
    "kid": "5t5YYpBhN-EgIEEI5iUzr6r0MR02LnVQ0OmekmNKcjY",
    "typ": "entity-statement+jwt"
  }
  
.. code-block:: json
  
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
      "wallet_metadata": {
        "authorization_endpoint": "https://wallet-solution.digital-strategy.europa.eu/authorization",
        "credential_offer_endpoint": "https://wallet-solution.digital-strategy.europa.eu/credential_offer",
        "response_types_supported": [
          "vp_token"
        ],
        "response_modes_supported": [
          "query"
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
        "client_id_prefixes_supported": ["openid_federation", "x509_hash"]
      }
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

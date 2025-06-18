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
    * - ``aal_values_supported``
      - OPZIONALE. Elenco dei valori supportati per il contesto di sicurezza certificabile. Questi valori specificano il livello di sicurezza dell'app, secondo i livelli: basso, medio o alto. Valori di Authenticator Assurance Level supportati.
      - Questa specifica.

metadati federation_entity
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Chiave**
      - **Valore**
      - **Riferimento**
    * - ``organization_name``
      - OPZIONALE. Un nome leggibile dall'uomo che rappresenta l'organizzazione proprietaria del Fornitore di Wallet.
      - `OID-FED`_.
    * - ``homepage_uri``
      - OPZIONALE. URL di una pagina Web dell'organizzazione proprietaria del Fornitore di Wallet.
      - `OID-FED`_.
    * - ``tos_uri``
      - OPZIONALE. URL che contiene i termini di servizio del Fornitore di Wallet.
      - `OID-FED`_.
    * - ``policy_uri``
      - OPZIONALE. URL della documentazione delle condizioni e delle politiche rilevanti per il Fornitore di Wallet.
      - `OID-FED`_.
    * - ``logo_uri``
      - OPZIONALE. Stringa. Un URL che punta al logo del Fornitore di Wallet. Il file contenente il logo DOVREBBE essere pubblicato in un formato visualizzabile tramite web.
      - `OID-FED`_.

Di seguito è riportato un esempio non normativo della Entity Configuration per un Fornitore di Wallet.

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

.. include:: ../common/common_definitions.rst

Metadati del Fornitore di Credenziale
-------------------------------------

Metadati per oauth_authorization_server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

I metadati *oauth_authorization_server* DEVONO contenere i seguenti parametri.

.. list-table::
  :class: longtable
  :widths: 20 60
  :header-rows: 1

  * - **Attributi dell'Utente**
    - **Descrizione**
  * - **issuer**
    - DEVE contenere un URL HTTPS che identifica in modo univoco il Fornitore di Credenziale.
  * - **pushed_authorization_request_endpoint**
    - L'URL dell'endpoint di richiesta di autorizzazione inviata è dove un'Istanza del Wallet DEVE inviare una richiesta di autorizzazione per ottenere un valore *request_uri*, che può quindi essere utilizzato all'endpoint di autorizzazione. Vedi :rfc:`9126#as_metadata`.
  * - **authorization_endpoint**
    - URL dell'endpoint di autorizzazione del server di autorizzazione. Vedi :rfc:`8414#section-2`.
  * - **token_endpoint**
    - URL dell'endpoint token del server di autorizzazione. Vedi :rfc:`8414#section-2`.
  * - **client_registration_types_supported**
    - Array che specifica i tipi di registrazione supportati. Il server di autorizzazione DEVE supportare *automatic*. Vedi `OID-FED`_ Sezione 5.1.3.
  * - **code_challenge_methods_supported**
    - Array JSON contenente un elenco di metodi di code challenge Proof Key for Code Exchange (PKCE) :rfc:`7636` supportati dal server di autorizzazione. Il server di autorizzazione DEVE supportare *S256*.
  * - **acr_values_supported**
    - Vedi `OpenID Connect Discovery 1.0 Section 3 <https://openid.net/specs/openid-connect-discovery-1_0.html#ProviderMetadata>`_. I valori supportati sono:

      - `https://trust-registry.eid-wallet.example.it/loa/low`
      - `https://trust-registry.eid-wallet.example.it/loa/substantial`
      - `https://trust-registry.eid-wallet.example.it/loa/high`
  * - **scopes_supported**
    - Array JSON contenente un elenco dei valori *scope* supportati. Vedi :rfc:`8414#section-2`.
  * - **response_modes_supported**
    - Array JSON contenente un elenco dei valori "response_mode" supportati, come specificato in `OAuth 2.0 Multiple Response Type Encoding Practices <https://openid.net/specs/oauth-v2-multiple-response-types-1_0.html>`_. I valori supportati POSSONO essere *query* e *form_post.jwt* (vedi `JARM`_).
  * - **response_types_supported**
    - Array JSON contenente un elenco dei valori "response_type" supportati, come specificato in :rfc:`8414`. Il valore supportato DEVE essere *code*.
  * - **authorization_signing_alg_values_supported**
    - Array JSON contenente un elenco degli algoritmi di firma supportati :rfc:`7515` (valori *alg*). I valori DEVONO essere impostati secondo la Sezione :ref:`algorithms:Algoritmi Crittografici`. Vedi Sezione 4 di `JARM`_.
  * - **grant_types_supported**
    - Array JSON contenente un elenco dei valori di tipo di concessione supportati. Il server di autorizzazione DEVE supportare *authorization_code*.
  * - **token_endpoint_auth_methods_supported**
    - Array JSON contenente un elenco dei metodi di autenticazione client supportati. L'Endpoint Token DEVE supportare *attest_jwt_client_auth* come definito in `OAUTH-ATTESTATION-CLIENT-AUTH`_.
  * - **token_endpoint_auth_signing_alg_values_supported**
    - Array JSON contenente un elenco degli algoritmi di firma ("valori *alg*") supportati dall'endpoint token per la firma sul JWT utilizzato per autenticare il client all'Endpoint Token. Vedi :rfc:`8414#section-2`.
  * - **request_object_signing_alg_values_supported**
    - Array JSON contenente un elenco degli algoritmi di firma ("valori *alg*") supportati per gli Oggetti di Richiesta. Vedi `[openid-connect-discovery-1_0] <https://openid.net/specs/openid-connect-discovery-1_0.html#ProviderMetadata>`_.
  * - **jwks**
    - JSON Web Key Set contenente le chiavi crittografiche per il server di autorizzazione. Vedi `OID-FED`_ Sezione 5.2.1 e `JWK`_.

Metadati per openid_credential_issuer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

I metadati *openid_credential_issuer* DEVONO contenere i seguenti attributi.

.. list-table::
  :class: longtable
  :widths: 20 60
  :header-rows: 1

  * - **Attributi dell'Utente**
    - **Descrizione**
  * - **credential_issuer**
    - L'identificatore del Fornitore di Credenziale. DEVE essere un URL con distinzione tra maiuscole e minuscole che utilizza lo schema HTTPS come definito in `OpenID4VCI`_ Sezioni 11.2.1 e 11.2.3.
  * - **credential_endpoint**
    - URL dell'endpoint Credential. Vedi `OpenID4VCI`_ Sezione 11.2.3.
  * - **nonce_endpoint**
    - URL dell'endpoint Nonce, come definito nella Sezione 7 di `OpenID4VCI`_.
  * - **revocation_endpoint**
    - URL dell'endpoint di revoca. Vedi :rfc:`8414#section-2`.
  * - **deferred_credential_endpoint**
    - URL dell'endpoint di Credenziale differita, come definito nella Sezione 11.2.3 di `OpenID4VCI`_.
  * - **status_assertion_endpoint**
    - DEVE essere un URL HTTPS che indica l'endpoint dove le Istanze del Wallet possono richiedere Status Assertion. Vedi Sezione :ref:`credential-revocation:Ciclo di vita delle Credenziali` per maggiori dettagli. (`OAUTH-STATUS-ASSERTION`_ Sezione 11.1.).
  * - **notification_endpoint**
    - DEVE essere un URL HTTPS che indica l'endpoint di notifica. Vedi Sezione 11.2.3 di [`OpenID4VCI`_].
  * - **authorization_servers**
    - OPZIONALE. Array di stringhe, dove ogni stringa è un identificatore del Server di Autorizzazione OAuth 2.0 (come definito in [:rfc:`8414`]) su cui il Fornitore di Credenziale si basa per l'autorizzazione. Se questo parametro è omesso, l'entità che fornisce il Fornitore di Credenziale agisce anche come Server di Autorizzazione.
  * - **display**
    - Vedi `OpenID4VCI`_ Sezione 11.2.3. Array di oggetti contenenti proprietà di visualizzazione della lingua. I parametri che DEVONO essere inclusi sono:

        - **name**: Valore stringa di un nome visualizzato per il Fornitore di Credenziale.
        - **locale**: Valore stringa che identifica la lingua di questo oggetto rappresentato come un tag linguistico preso dai valori definiti in *BCP47* :rfc:`5646`. DEVE esserci un solo oggetto per ogni identificatore di lingua.

  * - **credential_configurations_supported**
    - Oggetto JSON che delinea i dettagli della Credenziale supportata dal Fornitore di Credenziale. Include un elenco di coppie nome/valore, dove ogni nome identifica in modo univoco una specifica Credenziale supportata. Questo identificatore viene utilizzato per informare l'Istanza del Wallet su quale Credenziale può essere fornita dal Fornitore di Credenziale. Il valore associato all'interno dell'oggetto DEVE contenere metadati specifici per quella Credenziale, come definito di seguito. Vedi `OpenID4VCI`_ Sezioni 11.2.3 e A.3.2.

        - **format**: Stringa che identifica il formato di questa Credenziale. La Credenziale Digitale DEVE supportare il valore stringa "*dc+sd-jwt*" nel caso di SD-JWT VC (Vedi `OpenID4VCI`_ Sezione A.3.1.) e "*mso_mdoc*" nel caso di mdoc (vedi `OpenID4VCI`_ Sezione A.2.1.).
        - **scope**: Stringa JSON che identifica il valore *scope* supportato. L'Istanza del Wallet DEVE utilizzare questo valore nella Richiesta di Autorizzazione Inviata. I valori di scope DEVONO essere l'intero insieme o un sottoinsieme dei valori *scope* nel parametro *scopes_supported* del Server di Autorizzazione. [Vedi `OpenID4VCI`_ Sezione 11.2.3].
        - **cryptographic_binding_methods_supported**: Array JSON di stringhe sensibili alle maiuscole che identificano la rappresentazione del materiale chiave crittografico a cui è vincolata la Credenziale emessa. Il Fornitore di Credenziale DEVE supportare il valore "*jwk*" per il formato "dc+sd-jwt" e "*cose_key*" per "mso_mdoc".
        - **credential_signing_alg_values_supported**: Array JSON di stringhe sensibili alle maiuscole che identificano gli algoritmi che il Fornitore di Credenziale DEVE supportare per firmare la Credenziale emessa. Vedi Sezione :ref:`algorithms:Algoritmi Crittografici` per maggiori dettagli.
        - **proof_types_supported**: Oggetto JSON che fornisce informazioni dettagliate sulle prove di chiave supportate dal Fornitore di Credenziale. Consiste in un elenco di coppie nome/valore, dove ogni nome identifica in modo univoco un tipo di prova supportato. Il Fornitore di Credenziale DEVE supportare almeno "*jwt*" come definito in `OpenID4VCI`_ Sezione 8.2. Il valore associato a ciascuna coppia nome/valore è un oggetto JSON contenente metadati relativi alla prova della chiave. Il Fornitore di Credenziale DEVE supportare almeno il parametro **proof_signing_alg_values_supported** che DEVE essere un Array JSON di stringhe sensibili alle maiuscole che identificano gli algoritmi supportati (vedi Sezione :ref:`algorithms:Algoritmi Crittografici` per maggiori dettagli sugli algoritmi supportati).
        - **display**: Array di oggetti contenenti proprietà di visualizzazione della lingua. I parametri che DEVONO essere inclusi sono:

                - **name**: Valore stringa di un nome visualizzato per la Credenziale.
                - **locale**: Valore stringa che identifica la lingua di questo oggetto rappresentato come un tag linguistico preso dai valori definiti in *BCP47* :rfc:`5646`. DEVE esserci un solo oggetto per ogni identificatore di lingua.

        - **vct**: RICHIESTO solo se ``format`` è impostato su "*dc+sd-jwt*". Come definito in [:ref:`credential-data-model:Formato Credenziale SD-JWT-VC`].
        - **doctype**: RICHIESTO solo se ``format`` è impostato su "*mso_mdoc*". Come definito in [:ref:`credential-data-model:Formato Credenziale mdoc-CBOR`].
        - **claims**: Array di oggetti JSON ciascuno che descrive come un determinato attributo relativo alla Credenziale DEVE essere visualizzato all'Utente. Questo Array elenca gli attributi nell'ordine in cui DEVONO essere visualizzati dal Wallet. Per fornire informazioni dettagliate sull'attributo, il valore più interno DEVE contenere almeno i seguenti parametri. Vedi `OpenID4VCI`_ Sezione A.3.2.

            - **path**: Contiene il puntatore che specifica il percorso verso un attributo specifico all'interno della Credenziale come definito nell'Appendice C di `OpenID4VCI`_.
            - **display**: Array di oggetti contenenti proprietà di visualizzazione della lingua. I parametri che DEVONO essere inclusi sono:

                - **name**: Valore stringa di un nome visualizzato per l'attributo.
                - **locale**: Valore stringa che identifica la lingua di questo oggetto rappresentato come un tag linguistico preso dai valori definiti in *BCP47* :rfc:`5646`. DEVE esserci un solo oggetto per ogni identificatore di lingua.
  * - **jwks**
    - Documento JSON Web Key Set, passato per valore, contenente le chiavi specifiche del protocollo per il Fornitore di Credenziale. Vedi `OID-FED`_ Sezione 5.2.1 e `JWK`_.
  * - **trust_frameworks_supported**
    - Array JSON contenente tutti i trust framework supportati. Vedi `OIDC-IDA`_ Sezione 8. I valori supportati sono:
        - *it_cie*: trust framework CIE supportato.
        - *it_wallet*: trust framework Italian EUDI Wallet supportato.
        - *eudi_wallet*: trust framework Member State EUDI Wallet supportato.
  * - **evidence_supported**
    - Array JSON contenente tutti i tipi di prove di identità supportate dal Fornitore di Credenziale. Vedi `OIDC-IDA`_ Sezione 8. Il valore supportato è ``vouch``.
  * - **credential_hash_alg_supported**
    - L'algoritmo supportato utilizzato dall'Istanza del Wallet per eseguire l'hash della Credenziale Digitale per la quale viene richiesta la Status Assertion. Si RACCOMANDA di utilizzare *sha-256*. (Vedi `OAUTH-STATUS-ASSERTION`_ Sezione 11.1.).

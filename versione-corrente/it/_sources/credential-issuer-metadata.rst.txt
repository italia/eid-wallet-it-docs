.. include:: ../common/common_definitions.rst

Metadata del Fornitore di Attestati Elettronici
------------------------------------------------

Metadata per oauth_authorization_server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

I Metadata *oauth_authorization_server* DEVONO contenere i seguenti parametri.

.. list-table::
  :class: longtable
  :widths: 20 60
  :header-rows: 1

  * - **Claim**
    - **Descrizione**
  * - **issuer**
    - DEVE contenere un URL HTTPS che identifica in modo univoco il Fornitore di Attestati Elettronici.
  * - **pushed_authorization_request_endpoint**
    - L'URL dell'endpoint della *Pushed Authorization Request* dove un'Istanza del Wallet DEVE inviare una *authorization request* per ottenere un valore *request_uri*, che può quindi essere utilizzato all'*authorization endpoint*. Vedi :rfc:`9126#as_metadata`.
  * - **authorization_endpoint**
    - URL dell'*authorization endpoint* dell'*authorization server*. Vedi :rfc:`8414#section-2`.
  * - **token_endpoint**
    - URL del *token endpoint* dell'*authorization server*. Vedi :rfc:`8414#section-2`.
  * - **client_registration_types_supported**
    - Array che specifica i *registration types* supportati. L'*authorization server* DEVE supportare *automatic*. Vedi `OID-FED`_ Sezione 5.1.3.
  * - **code_challenge_methods_supported**
    - Array JSON contenente un elenco di metodi di *code challenge* previsti da Proof Key for Code Exchange (PKCE) :rfc:`7636` e supportati dall'*authorization server*. L'*authorization server* DEVE supportare *S256*.
  * - **acr_values_supported**
    - Vedi `OpenID Connect Discovery 1.0 Section 3 <https://openid.net/specs/openid-connect-discovery-1_0.html#ProviderMetadata>`_. I valori supportati sono:

      - `https://trust-registry.eid-wallet.example.it/loa/low`
      - `https://trust-registry.eid-wallet.example.it/loa/substantial`
      - `https://trust-registry.eid-wallet.example.it/loa/high`
  * - **scopes_supported**
    - Array JSON contenente un elenco dei valori *scope* supportati. Vedi :rfc:`8414#section-2`.
  * - **response_modes_supported**
    - Array JSON contenente un elenco dei valori "*response_mode*" supportati, come specificato in `OAuth 2.0 Multiple Response Type Encoding Practices <https://openid.net/specs/oauth-v2-multiple-response-types-1_0.html>`_. I valori supportati POSSONO essere *query* e *form_post.jwt* (vedi `JARM`_).
  * - **response_types_supported**
    - Array JSON contenente un elenco dei valori "*response_type*" supportati, come specificato in :rfc:`8414`. Il valore supportato DEVE essere *code*.
  * - **authorization_signing_alg_values_supported**
    - Array JSON contenente un elenco degli algoritmi di firma supportati :rfc:`7515` (valori *alg*). I valori DEVONO essere impostati secondo la Sezione :ref:`algorithms:Algoritmi Crittografici`. Vedi Sezione 4 di `JARM`_.
  * - **grant_types_supported**
    - Array JSON contenente un elenco dei valori di *grant type* supportati. L'*authorization server* DEVE supportare *authorization_code*.
  * - **token_endpoint_auth_methods_supported**
    - Array JSON contenente un elenco dei metodi di *client authentication* supportati. Il *token endpoint* DEVE supportare *attest_jwt_client_auth* come definito in `OAUTH-ATTESTATION-CLIENT-AUTH`_.
  * - **token_endpoint_auth_signing_alg_values_supported**
    - Array JSON contenente un elenco degli algoritmi di firma ("valori *alg*") supportati dal *token endpoint* per la firma sul JWT utilizzato per autenticare il client al *token endpoint*. Vedi :rfc:`8414#section-2`.
  * - **request_object_signing_alg_values_supported**
    - Array JSON contenente un elenco degli algoritmi di firma ("valori *alg*") supportati per i *Request Objects*. Vedi `[openid-connect-discovery-1_0] <https://openid.net/specs/openid-connect-discovery-1_0.html#ProviderMetadata>`_.
  * - **jwks**
    - JSON Web Key Set contenente le chiavi crittografiche per '*authorization server*. Vedi `OID-FED`_ Sezione 5.2.1 e `JWK`_.

Metadata per openid_credential_issuer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

I Metadata *openid_credential_issuer* DEVONO contenere i seguenti *claims*.

.. list-table::
  :class: longtable
  :widths: 20 60
  :header-rows: 1

  * - **Claim**
    - **Descrizione**
  * - **credential_issuer**
    - L'identificativo del Fornitore di Attestati Elettronici. DEVE essere un HTTPS URL *case sensitive* come definito in `OpenID4VCI`_ Sezioni 11.2.1 e 11.2.3.
  * - **credential_endpoint**
    - URL del *Credential endpoint*. Vedi `OpenID4VCI`_ Sezione 11.2.3.
  * - **nonce_endpoint**
    - URL del *Nonce endpoint*, come definito nella Sezione 7 di `OpenID4VCI`_.
  * - **revocation_endpoint**
    - URL del *revocation endpoint*. Vedi :rfc:`8414#section-2`.
  * - **deferred_credential_endpoint**
    - URL del *deferred credential endpoint*, come definito nella Sezione 11.2.3 di `OpenID4VCI`_.
  * - **status_assertion_endpoint**
    - DEVE essere un URL HTTPS che indica l'endpoint dove le Istanze del Wallet possono richiedere Status Assertion. Vedi Sezione :ref:`credential-revocation:Ciclo di Vita degli Attestati Elettronici` per maggiori dettagli. (`OAUTH-STATUS-ASSERTION`_ Sezione 11.1.).
  * - **notification_endpoint**
    - DEVE essere un URL HTTPS che indica il *notification endpoint*. Vedi Sezione 11.2.3 di [`OpenID4VCI`_].
  * - **authorization_servers**
    - OPZIONALE. Array di stringhe, dove ogni stringa è un identificativo dell'*authorization server* OAuth 2.0 (come definito in [:rfc:`8414`]) usato dal Fornitore di Attestati Elettronici per gestire l'autenticazione/autorizzazione. Se questo parametro è omesso vuol dire che il Fornitore di Attestati Elettronici agisce direttamente anche come *authorization server*.
  * - **display**
    - Vedi `OpenID4VCI`_ Sezione 11.2.3. Array di oggetti contenenti proprietà di visualizzazione della lingua. I parametri che DEVONO essere inclusi sono:

        - **name**: Denominazione in formato stringa del Fornitore di Attestati Elettronici. 
        - **locale**: Valore stringa che identifica la localizzazione rappresentato come un tag linguistico come definito in *BCP47* :rfc:`5646`. DEVE esserci un solo oggetto per ogni identificativo di localizzazione.

  * - **credential_configurations_supported**
    - Oggetto JSON che delinea i dettagli della Attestato Elettronico supportato dal Fornitore di Attestato Elettronico. Include un elenco di coppie nome/valore, dove ogni nome identifica in modo univoco un specific Attestato Elettronico supportato. Questo identificativo viene utilizzato per informare l'Istanza del Wallet su quale Attestato Elettronico può essere emesso. Il valore associato all'interno dell'oggetto DEVE contenere Metadata specifici per quell'Attestato Elettronico, come definito di seguito. Vedi `OpenID4VCI`_ Sezioni 11.2.3 e A.3.2.

        - **format**: Stringa che identifica il formato di questo Attestato Elettronico. L'Attestato Elettronico DEVE supportare il valore stringa "*dc+sd-jwt*" nel caso di SD-JWT VC (Vedi `OpenID4VCI`_ Sezione A.3.1.) e "*mso_mdoc*" nel caso di mdoc (vedi `OpenID4VCI`_ Sezione A.2.1.).
        - **scope**: Stringa JSON che identifica il valore *scope* supportato. L'Istanza del Wallet DEVE utilizzare questo valore nella *Pushed Authorization Request* inviata. I valori di scope DEVONO essere l'intero insieme o un sottoinsieme dei valori *scope* presenti nel parametro *scopes_supported* del *authorization server*. [Vedi `OpenID4VCI`_ Sezione 11.2.3].
        - **cryptographic_binding_methods_supported**: Array JSON di stringhe *case sensitive* che identificano la rappresentazione della chiave crittografica di *binding* dell'Attestato Elettronico emesso. Il Fornitore di Attestato Elettronico DEVE supportare il valore "*jwk*" per il formato "dc+sd-jwt" e "*cose_key*" per "mso_mdoc".
        - **credential_signing_alg_values_supported**: Array JSON di stringhe *case sensitive* che identificano gli algoritmi che il Fornitore di Attestato Elettronico DEVE supportare per firmare l'Attestato Elettronico emesso. Vedi Sezione :ref:`algorithms:Algoritmi Crittografici` per maggiori dettagli.
        - **proof_types_supported**: Oggetto JSON che fornisce informazioni dettagliate sulle *key proof* supportate dal Fornitore di Attestato Elettronico. Consiste in un elenco di coppie nome/valore, dove ogni nome identifica in modo univoco il *proof type* supportato. Il Fornitore di Attestato Elettronico DEVE supportare almeno "*jwt*" come definito in `OpenID4VCI`_ Sezione 8.2. Il valore associato a ciascuna coppia nome/valore è un oggetto JSON contenente informazioni relative alla *key proof*. Il Fornitore di Attestato Elettronico DEVE supportare almeno il parametro **proof_signing_alg_values_supported** che DEVE essere un Array JSON di stringhe *case sensitive* che identificano gli algoritmi supportati (vedi Sezione :ref:`algorithms:Algoritmi Crittografici` per maggiori dettagli sugli algoritmi supportati).
        - **display**: Array di oggetti contenenti proprietà di visualizzazione della localizzazione. I parametri che DEVONO essere inclusi sono

                - **name**: Valore stringa di un nome visualizzato per l'Attestato Elettronico.
                - **locale**: Valore stringa che identifica la localizzazione rappresentato come un tag linguistico come definito in *BCP47* :rfc:`5646`. DEVE esserci un solo oggetto per ogni identificativo di localizzazione.

        - **vct**: RICHIESTO solo se ``format`` è valorizzato con "*dc+sd-jwt*". Come definito in [:ref:`credential-data-model:Attestato Elettronico in formato SD-JWT-VC`].
        - **doctype**: RICHIESTO solo se ``format`` è valorizzato con "*mso_mdoc*". Come definito in [:ref:`credential-data-model:Attestato Elettronico in formato mdoc-CBOR`].
        - **claims**: Array di oggetti JSON ciascuno che descrive come un determinato attributo relativo all'Attestato Elettronico DEVE essere visualizzato all'Utente. Questo Array elenca gli attributi nell'ordine in cui DEVONO essere visualizzati dal Wallet. Per fornire informazioni dettagliate sull'attributo, il valore più interno DEVE contenere almeno i seguenti parametri. Vedi `OpenID4VCI`_ Sezione A.3.2.

            - **path**: Contiene il puntatore che specifica il percorso all'attributo specifico all'interno dell'Attestato Elettronico come definito nell'Appendice C di `OpenID4VCI`_.
            - **display**: Array di oggetti contenenti proprietà di visualizzazione della localizzazione. I parametri che DEVONO essere inclusi sono

                - **name**: Nome dell'attributo in formato stringa.
                - **locale**: Stringa che identifica la localizzazione con un tag linguistico come definito in *BCP47* :rfc:`5646`. DEVE esserci un solo oggetto per ogni identificativo di localizzazione.
  * - **jwks**
    - JSON Web Key Set, passato per valore, contenente le chiavi specifiche del protocollo usato dal Fornitore di Attestato Elettronico. Vedi `OID-FED`_ Sezione 5.2.1 e `JWK`_.
  * - **trust_frameworks_supported**
    - Array JSON contenente tutti i trust framework supportati. Vedi `OIDC-IDA`_ Sezione 8. I valori supportati sono:
        - *it_cie*: trust framework CIE id supportato.
        - *it_wallet*: trust framework IT-Wallet supportato.
        - *eudi_wallet*: trust framework Member State EUDI Wallet supportato.
  * - **evidence_supported**
    - Array JSON contenente tutti i tipi di evidenze di identità supportate dal Fornitore dell'Attestato Elettronico. Vedi `OIDC-IDA`_ Sezione 8. Il valore supportato è ``vouch``.
  * - **credential_hash_alg_supported**
    - L'algoritmo supportato utilizzato dall'Istanza del Wallet per eseguire l'hash dell'Attestato Elettronico per il quale viene richiesta la Status Assertion. Si RACCOMANDA di utilizzare *sha-256*. (Vedi `OAUTH-STATUS-ASSERTION`_ Sezione 11.1.).

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
  * - **response_types_supported**
    - Array JSON contenente un elenco dei valori "*response_type*" supportati, come specificato in :rfc:`8414`. Il valore supportato DEVE essere *code*.
  * - **authorization_signing_alg_values_supported**
    - Array JSON contenente un elenco degli algoritmi di firma supportati :rfc:`7515` (valori *alg*). I valori DEVONO essere impostati secondo la Sezione :ref:`algorithms:Algoritmi Crittografici`.
  * - **grant_types_supported**
    - Array JSON contenente un elenco dei valori di *grant type* supportati. L'*authorization server* DEVE supportare *authorization_code*.
  * - **token_endpoint_auth_methods_supported**
    - Array JSON contenente un elenco dei metodi di *client authentication* supportati. Il *token endpoint* DEVE supportare *attest_jwt_client_auth* come definito in `OAUTH-ATTESTATION-CLIENT-AUTH`_.
  * - **token_endpoint_auth_signing_alg_values_supported**
    - Array JSON contenente un elenco degli algoritmi di firma ("valori *alg*") supportati dal *token endpoint* per la firma sul JWT utilizzato per autenticare il client al *token endpoint*. Vedi :rfc:`8414#section-2`.
  * - **client_attestation_signing_alg_values_supported**
    - Array JSON con l’elenco dei valori JWS "alg" supportati per la Wallet Attestation (``oauth-client-attestation+jwt``). I valori DEVONO provenire dalla Sezione :ref:`algorithms:Algoritmi Crittografici` e NON DEVONO includere ``none`` né algoritmi simmetrici (MAC).
  * - **client_attestation_pop_signing_alg_values_supported**
    - Array JSON con l’elenco dei valori JWS "alg" supportati per la Proof-of-Possession della Wallet Attestation (``oauth-client-attestation-pop+jwt``). I valori DEVONO provenire dalla Sezione :ref:`algorithms:Algoritmi Crittografici` e NON DEVONO includere ``none`` né algoritmi simmetrici (MAC).
  * - **require_signed_request_object**
    - Booleano. DEVE essere impostato a `true` per indicare che la richiesta di autorizzazione è protetta usando un Request Object firmato [:rfc:`9101`].
  * - **request_object_signing_alg_values_supported**
    - Array JSON contenente un elenco degli algoritmi di firma ("valori *alg*") supportati per i *Request Objects*. Vedi `[openid-connect-discovery-1_0] <https://openid.net/specs/openid-connect-discovery-1_0.html#ProviderMetadata>`_.
  * - **dpop_signing_alg_values_supported**
    - Array JSON contenente un elenco degli algoritmi di firma (valori "*alg*") supportati per i JWT DPoP proof. Vedi :rfc:`9449`.
  * - **jwks**
    - JSON Web Key Set contenente le chiavi crittografiche per '*authorization server*. Vedi `OID-FED`_ Sezione 5.2.1 e `JWK`_.

.. important::
  Se ``token_endpoint_auth_methods_supported`` include ``attest_jwt_client_auth``, l’Authorization Server DEVE includere entrambi ``client_attestation_signing_alg_values_supported`` e ``client_attestation_pop_signing_alg_values_supported`` nei propri metadati. I client DOVREBBERO recuperare e analizzare i metadati per rilevare supporto e requisiti di algoritmo per l’Attestation-Based Client Authentication e, in caso di incompatibilità, POSSONO ottenere una nuova attestation con un algoritmo supportato.


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
    - L'identificativo del Fornitore di Attestati Elettronici. DEVE essere un HTTPS URL *case sensitive* come definito in `OpenID4VCI`_ Sezioni 12.2.1 e 12.2.4.
  * - **credential_endpoint**
    - URL del *Credential endpoint*. Vedi `OpenID4VCI`_ Sezione 12.2.4.
  * - **nonce_endpoint**
    - URL del *Nonce endpoint*, come definito nella Sezione 7 di `OpenID4VCI`_.
  * - **deferred_credential_endpoint**
    - URL del *deferred credential endpoint*, come definito nella Sezione 12.2.4 di `OpenID4VCI`_.
  * - **notification_endpoint**
    - DEVE essere un URL HTTPS che indica il *notification endpoint*. Vedi Sezione 12.2.4 di [`OpenID4VCI`_].
  * - **authorization_servers**
    - OPZIONALE. Array di stringhe, dove ogni stringa è un identificativo dell'*authorization server* OAuth 2.0 (come definito in [:rfc:`8414`]) usato dal Fornitore di Attestati Elettronici per gestire l'autenticazione/autorizzazione. Se questo parametro è omesso vuol dire che il Fornitore di Attestati Elettronici agisce direttamente anche come *authorization server*.
  * - **display**
    - Vedi `OpenID4VCI`_ Sezione 12.2.4 Array di oggetti contenenti proprietà di visualizzazione della lingua. I parametri che DEVONO essere inclusi sono:

        - **name**: Denominazione in formato stringa del Fornitore di Attestati Elettronici. 
        - **locale**: Valore stringa che identifica la localizzazione rappresentato come un tag linguistico come definito in *BCP47* :rfc:`5646`. DEVE esserci un solo oggetto per ogni identificativo di localizzazione.
        - **logo**: Oggetto contenente informazioni relative al logo del Credential Issuer. Contiene i seguenti parametri:

            - **uri**: OBBLIGATORIO. URL del logo dell’entità che verrà mostrato all’Utente durante le interazioni con l’istanza del Wallet. Il MIME type del logo DEVE essere ``application/svg``.
            - **uri#integrity**: OPZIONALE. "integrity metadata" come definito nella Sezione 3 del documento `W3C-SRI`_.
            - **alt_text**: OPZIONALE. Stringa contenente il testo da mostrare in alternativa all’immagine del logo.

  * - **credential_configurations_supported**
    - Oggetto JSON che delinea i dettagli dell'Attestato Elettronico supportato dal Fornitore di Attestato Elettronico. Include un elenco di coppie nome/valore, dove ogni nome identifica in modo univoco un specific Attestato Elettronico supportato. Questo identificativo viene utilizzato per informare l'Istanza del Wallet su quale Attestato Elettronico può essere emesso. Il valore associato all'interno dell'oggetto DEVE contenere Metadata specifici per quell'Attestato Elettronico, come definito di seguito. Vedi `OpenID4VCI`_ Sezioni 12.2.4 e A.3.2.

        - **format**: Stringa che identifica il formato di questo Attestato Elettronico. L'Attestato Elettronico DEVE supportare il valore stringa "*dc+sd-jwt*" nel caso di SD-JWT VC (Vedi `OpenID4VCI`_ Sezione A.3.1.) e "*mso_mdoc*" nel caso di mdoc (vedi `OpenID4VCI`_ Sezione A.2.1.).
        - **scope**: Stringa JSON che identifica il valore *scope* supportato. L'Istanza del Wallet DEVE utilizzare questo valore nella *Pushed Authorization Request* inviata. I valori di scope DEVONO essere l'intero insieme o un sottoinsieme dei valori *scope* presenti nel parametro *scopes_supported* del *authorization server*. Se l’Attestato Elettronico è incluso nel Catalogo degli Attestati Elettronici, il valore scope DEVE corrispondere al parametro ``credential_type`` definito in :ref:`registry:Struttura del Catalogo delle Credenziali Digitali` oppure in :ref:`registry:Registro degli Schema`. [Vedi `OpenID4VCI`_ Sezione 12.2.4]. 
        - **cryptographic_binding_methods_supported**: Array JSON di stringhe *case sensitive* che identificano la rappresentazione della chiave crittografica di *binding* dell'Attestato Elettronico emesso. Il Fornitore di Attestato Elettronico DEVE supportare il valore "*jwk*" per il formato "dc+sd-jwt" e "*cose_key*" per "mso_mdoc".
        - **credential_signing_alg_values_supported**: Array JSON di stringhe *case sensitive* che identificano gli algoritmi che il Fornitore di Attestato Elettronico DEVE supportare per firmare l'Attestato Elettronico emesso. Vedi Sezione :ref:`algorithms:Algoritmi Crittografici` per maggiori dettagli.
        - **proof_types_supported**: Oggetto JSON che fornisce informazioni dettagliate sulle *key proof* supportate dal Fornitore di Attestato Elettronico. Consiste in un elenco di coppie nome/valore, dove ogni nome identifica in modo univoco il *proof type* supportato. Il Fornitore di Attestato Elettronico DEVE supportare almeno "*jwt*" come definito in `OpenID4VCI`_ Appendice F.1. Il valore associato a ciascuna coppia nome/valore è un oggetto JSON contenente informazioni relative alla *key proof(s)*. Il Fornitore di Attestato Elettronico DEVE supportare almeno il parametro **proof_signing_alg_values_supported** che DEVE essere un Array JSON di stringhe *case sensitive* che identificano gli algoritmi supportati (vedi Sezione :ref:`algorithms:Algoritmi Crittografici` per maggiori dettagli sugli algoritmi supportati). Il Fornitore di Attestato Elettronico PUÒ supportare il parametro **key_attestations_required** come definito nella Sezione 12.2 di `OpenID4VCI`_.
        - **vct**: RICHIESTO solo se ``format`` è valorizzato con "*dc+sd-jwt*". Come definito in [:ref:`credential-data-model:Attestato Elettronico in formato SD-JWT-VC`].        
        - **doctype**: RICHIESTO solo se ``format`` è valorizzato con "*mso_mdoc*". Come definito in [:ref:`credential-data-model:Attestato Elettronico in formato mdoc-CBOR`].
        - **credential_metadata**: OBBLIGATORIO. Oggetto contenente informazioni rilevanti per l'utilizzo e la visualizzazione degli Attestati emessi. I parametri che DEVONO essere inclusi sono:

          - **display**: Array di oggetti contenente le proprietà legate alla visualizzazione. I seguenti parametri sono inclusi:

                - **name**: OBBLIGATORIO. Stringa contenente il nome da visualizzare per l'Attestato Elettronico.
                - **locale**: OBBLIGATORIO. Stringa che identifica la localizzazione identificata dal corrispettivo tag linguistico come definito in *BCP47* :rfc:`5646`. DEVE esserci un solo oggetto per ogni identificativo di localizzazione.
                - **description**: OBBLIGATORIO. Stringa contenente la descrizione dell'Attestato Elettronico.
                - **logo**: OPZIONALE. Oggetto contenente informazioni relative al logo dell’Attestato Elettronico. Include i seguenti parametri:

                  - **uri**: OBBLIGATORIO. Stringa che contiene la URI da cui il Wallet può ottenere il logo dell’Attestato Elettronico dal Fornitore di Attestati Elettronici. Il MIME type del logo DEVE essere ``application/svg``.
                  - **uri#integrity**: OBBLIGATORIO. "integrity metadata" come definito nella Sezione 3 del documento `W3C-SRI`_.
                  - **alt_text**: OPZIONALE. Stringa contenente il testo da mostrare in alternativa all’immagine del logo.
                - **background_color**: OBBLIGATORIO. Stringa che rappresenta il colore di sfondo dell’Attestato Elettronico, espresso come valore numerico secondo la definizione del documento `W3C.CSS-COLOR`_
                - **background_image**: OPZIONALE. Oggetto contiene informazioni sull’immagine di sfondo da visualizzare per l'Attestato Elettronico. L’oggetto include i seguenti sotto-valori:

                  - **uri**: OBBLIGATORIO. Stringa che contiene la URI da cui il Wallet può ottenere il logo dell’Attestato Elettronico dal Fornitore di Attestati Elettronici.
                  - **uri#integrity**: OBBLIGATORIO. "integrity metadata" come definito nella Sezione 3 del documento `W3C-SRI`_.

                - **watermark_image**: OPZIONALE. Oggetto contiene informazioni sull’immagine di filigrana da visualizzare per l'Attestato Elettronico. L’oggetto include i seguenti sotto-valori:

                  - **uri**: OBBLIGATORIO. Stringa che contiene la URI da cui il Wallet può ottenere il logo dell’Attestato Elettronico dal Fornitore di Attestati Elettronici.
                  - **uri#integrity**: OBBLIGATORIO. "integrity metadata" come definito nella Sezione 3 del documento `W3C-SRI`_.  

          - **claims**: Array di oggetti JSON ciascuno che descrive come un determinato attributo relativo all'Attestato Elettronico DEVE essere visualizzato all'Utente. Questo array elenca le attestazioni nell’ordine in cui DEVONO essere mostrate dal Wallet. Per fornire informazioni dettagliate sull’attestazione, il valore più interno DEVE contenere almeno i seguenti parametri. Vedi OpenID4VCI_ Sezione A.3.2.


            - **path**: Contiene il puntatore che specifica il percorso all'attributo specifico all'interno dell'Attestato Elettronico come definito nell'Appendice C di `OpenID4VCI`_.
            - **mandatory**: Valore booleano che, se impostato su `true`, indica che il Credential Issuer includerà sempre questo attributo nelle Credenziali che emette.
            - **sd**: Stringa che indica se il claim è divulgabile selettivamente. DEVE essere impostato su `always` se il claim è divulgabile selettivamente o `never` se non lo è.
            - **display**: Array di oggetti contenenti le proprietà di visualizzazione. Array contenente informazioni di visualizzazione relative al claim indicato nel ``path``. L'array contiene un oggetto per ogni lingua supportata. I parametri che DEVONO essere inclusi sono:

                - **name**: Nome dell'attributo in formato stringa.
                - **description**: Descrizione "human-readable" dell'Attributo.
                - **locale**: Stringa che identifica la localizzazione con un tag linguistico come definito in *BCP47* :rfc:`5646`. DEVE esserci un solo oggetto per ogni identificativo di localizzazione.

        - **schema_id**: OBBLIGATORIO. Identificativo dello schema delle credenziali come definito nel :ref:`registry:Registro degli Schema`.
        - **authentic_sources**: OBBLIGATORIO. Oggetto contenente il parametro ``entity_id`` e ``dataset_id``, valorizzato con i rispettivi dentificativi come censiti all'interno del :ref:`registry:Registro delle Fonti Autentiche`.

  * - **jwks**
    - JSON Web Key Set, passato per valore, contenente le chiavi specifiche del protocollo usato dal Fornitore di Attestato Elettronico. Vedi `OID-FED`_ Sezione 5.2.1 e `JWK`_.
  * - **trust_frameworks_supported**
    - Array JSON contenente tutti i trust framework supportati. I valori supportati sono:
        - *it_cie*: trust framework CIE id supportato.
        - *it_wallet*: trust framework IT-Wallet supportato.
        - *eudi_wallet*: trust framework Member State EUDI Wallet supportato.
        - *it_l2+document_proof*: protocollo Autenticazione eID Substantial con Verifica MRTD supportato.
  * - **batch_credential_issuance**
    - Oggetto contenente informazioni sull'emissione di Credenziali in batch da parte del Credential Issuer presso il Credential Endpoint. La presenza di questo parametro indica che il Credential Issuer supporta più di una prova di possesso nel parametro ``proofs`` nella Credential Request, pertanto può emettere più di un Attestato Elettronico con gli stessi attributi relativi al titolare in un'unica richiesta/risposta. Il parametro che DEVE essere incluso è:

            - **batch_size**: Valore intero che specifica la dimensione massima dell'array per il parametro ``proofs`` nella Credential Request.
  * - **status_list_aggregation_endpoint**
    - URL del *Status List Aggregation Endpoint*. Vedi `TOKEN-STATUS-LIST`_ Sezione 9.


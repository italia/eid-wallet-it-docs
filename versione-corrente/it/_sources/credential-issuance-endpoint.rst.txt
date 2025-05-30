.. include:: ../common/common_definitions.rst

Credential Offer Endpoint 
"""""""""""""""""""""""""""""""""""""

Il Credential Offer Endpoint di un Wallet è utilizzato dal Credential Issuer per interagire con l'Utente al fine di avviare un'Emissione di un Attestato Elettronico. DEVE essere utilizzato il *custom URL* ``openid-credential-offer://``.

Credential Offer
......................

La Credential Offer effettuata dal Credential Issuer consiste in un singolo parametro da inviare in query URI ``credential_offer``. L'URL rappresentativa della Credential Offer PUÒ essere inclusa in un QR Code o in una pagina html con un pulsante href e DEVE contenere i seguenti parametri obbligatori:

.. _table_credential_offer_claim:
.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Claim**
    - **Descrizione**
    - **Riferimento**
  * - **credential_issuer**
    - DEVE essere valorizzato con una URL HTTPS che identifica in modo univoco il Credential Issuer. Il Wallet utilizza il valore di questo parametro per ottenere i Metadata del Credential Issuer.
    - Sezione 4.1.1 di [`OpenID4VCI`_].
  * - **credential_configuration_ids**
    - Array di Stringhe, ciascuna delle quali specifica un identificativo univoco dell'Attestato Elettronico descritta nel claim ``credential_configurations_supported`` presente nei Metadata del Credential Issuer.
    - Sezione 4.1.1 di [`OpenID4VCI`_].
  * - **grants**
    - DEVE contenere un oggetto ``authorization_code`` con i seguenti parametri:

        - **issuer_state**: OBBLIGATORIO. Stringa opaca creata dal Credential Issuer utilizzata per correlare la successiva Authorization Request con il Credential Issuer. Il Wallet DEVE includerla nella successiva Authorization Request.
        - **authorization_server**: OBBLIGATORIO se il Credential Issuer utilizza più di un authorization server nella sua Soluzione di Fornitore di Attestati Elettronici. Stringa che identifica l'Authorization Server da utilizzare. Il valore DEVE corrispondere a uno dei valori censiti nell'array ``authorization_servers`` dei Metadata del Credential Issuer. NON DEVE essere utilizzato se ``authorization_servers`` è assente o non ha voci.
    - Sezione 4.1.1 di [`OpenID4VCI`_].


Credential Offer Response
...................................
Non è prevista alcuna response da parte del Wallet.


Pushed Authorization Request Endpoint
""""""""""""""""""""""""""""""""""""""""""""""""""

Pushed Authorization Request (PAR) Request
............................................

La request all'authorization endpoint del Credential Issuer DEVE contenere sia i parametri di header HTTP che i parametri HTTP POST.

Il metodo HTTP POST DEVE avere i parametri nel body del messaggio codificati in formato ``application/x-www-form-urlencoded``.

.. _table_http_request_claim:
.. list-table:: Parametri della PAR request http
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Descrizione**
      - **Riferimento**
    * - **client_id**
      - DEVE essere valorizzato con il *thumbprint* del ``jwk`` presente nel parametro ``cnf`` all'interno dell'Attestato di Unità di Wallet.
      - :rfc:`6749`
    * - **request**
      - DEVE essere un JWT firmato. La chiave privata corrispondente a quella pubblica presente nel parametro ``cnf`` all'interno dell'Attestato di Unità di Wallet che DEVE essere utilizzata per firmare ilRequest Object.
      - `OpenID Connect Core. Sezione 6 <https://openid.net/specs/openid-connect-core-1_0.html#JWTRequests>`_

Il Pushed Authorization Endpoint è protetto con *OAuth 2.0 Attestation-based Client Authentication* [`OAUTH-ATTESTATION-CLIENT-AUTH`_], pertanto
la richiesta all'authorization endpoint del Credential Issuer DEVE utilizzare i seguenti parametri di header HTTP:

.. _table_http_request_headers_claim:
.. list-table:: parametri di header della request http
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **OAuth-Client-Attestation**
      - DEVE contenere il JWT dell'Attestato di Unità di Wallet.
      - `OAUTH-ATTESTATION-CLIENT-AUTH`_.
    * - **OAuth-Client-Attestation-PoP**
      - DEVE contenere la Prova di Possesso del JWT dell'Attestato di Unità di Wallet.
      - `OAUTH-ATTESTATION-CLIENT-AUTH`_.


Il JWT *Request Object* ha i seguenti parametri di header JOSE:

.. _table_request_object_claim:
.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **JOSE Header**
      - **Descrizione**
      - **Riferimento**
    * - **alg**
      - Identificativo dell'algoritmo di firma digitale come definito nel registro IANA "JSON Web Signature and Encryption Algorithms". DEVE essere uno degli algoritmi supportati elencati nella Sezione :ref:`algorithms:Algoritmi Crittografici` e NON DEVE essere valorizzato con ``none`` o con qualsiasi identificativo di algoritmo simmetrico (MAC).
      - :rfc:`7516#section-4.1.1`.
    * - **kid**
      - Identificativo univoco del ``jwk`` presente all'interno del claim ``cnf`` dell'Attestato di Unità di Wallet, ovvero il valore del *thumbprint* del JWK codificato in base64url.
      - :rfc:`7638#section_3`.

.. note::
  Il parametro **typ**, se omesso, assume il valore implicito **JWT**.


Il payload del JWT ``request`` contenuto nel messaggio HTTP POST contiene i seguenti parametri:

.. _table_jwt_request:
.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Descrizione**
      - **Riferimento**
    * - **iss**
      - DEVE essere valorizzato con il ``client_id``.
      - :rfc:`9126` e :rfc:`7519`.
    * - **aud**
      - DEVE essere valorizzato con l'identificativo del Credential Issuer.
      - :rfc:`9126` e :rfc:`7519`.
    * - **exp**
      - Timestamp UNIX con orario di scadenza del JWT. Il valore NON DEVE essere superiore a 300 secondi rispetto all'orario di emissione.
      - :rfc:`9126` e :rfc:`7519`.
    * - **iat**
      - Timestamp UNIX con data e orario di emissione del JWT.
      - :rfc:`9126` e :rfc:`7519`.
    * - **response_type**
      - DEVE essere valorizzato con ``code``.
      - :rfc:`6749`
    * - **response_mode**
      - DEVE essere una stringa che indica il "*response_mode*", come specificato in [`OAUTH-MULT-RESP-TYPE`_]. DEVE essere valorizzato con uno dei valori supportati (*response_modes_supported*) forniti nei Metadata del Credential Issuer. Tale claim informa il Credential Issuer sul meccanismo da utilizzare per la restituizione dei parametri da parte dell' Authorization Endpoint. In caso di *HTTP 302 Redirect Response* il valore DEVE essere *query*. In questa modalità, i parametri dell'Authorization Response sono codificati nella stringa di query aggiunta al ``redirect_uri`` durante il redirect all'Istanza del Wallet. In caso di *HTTP POST Response* il valore DEVE essere *form_post.jwt* secondo [`JARM`_]. In questa modalità, i parametri dell'Authorization Response sono riportati in un JWT codificato in un form HTML che viene inviato automaticamente nell'user-agent, e quindi viene trasmesso tramite il metodo HTTP POST all'Istanza del Wallet, con i parametri risultanti codificati nel body utilizzando il formato *application/x-www-form-urlencoded*. L'attributo *action* del form DEVE contenere il  *Redirection URI* dell'Istanza del Wallet. L'attributo *method* del form DEVE essere POST.
      - Vedi [`OAUTH-MULT-RESP-TYPE`_] e [`JARM`_].
    * - **client_id**
      - DEVE essere valorizzato come indicato nella :ref:`Tabella dei parametri HTTP <table_http_request_claim>`.
      - Vedi :ref:`Tabella dei parametri HTTP <table_http_request_claim>`.
    * - **state**
      - Identificativo univoco della sessione lato client. Questo valore verrà restituito al client nella response, al termine dell'autenticazione. DEVE essere una stringa casuale composta da caratteri alfanumerici e con una lunghezza minima di 32 cifre. Tra i caratteri speciali DEVONO essere considerati quelli non alfanumerici definiti in `[NIST] <https://csrc.nist.gov/glossary/term/special_character>`__.
      - Vedi [`OIDC`_] Sezione 3.1.2.1.
    * - **code_challenge**
      - *Challenge* derivata dal **code verifier** che viene inviata nell'authorization request.
      - :rfc:`7636#section-4.2`.
    * - **code_challenge_method**
      - Metodo utilizzato per derivare il **code challenge**. DEVE essere valorizzato con ``S256``.
      - :rfc:`7636#section-4.3`.
    * - **scope**
      - Stringa JSON. Stringa contenente un identificativo univoco dell'Attestato Elettronico indipendentemente dal suo formato. DEVE essere mappato nel claim `credential_configurations_supported` presente nei Metadata del Credential Issuer. Il valore dell'identificativo univoco DEVE corrispondere al parametro `credential_type` del :ref:`registry-catalogue:Catalogo degli Attestati Elettronici`. Ad esempio, nel caso del PID, può essere valorizzato con ``PersonIdentificationData`` mentre nel caso della patente di guida ``mDL``. Poiché PUÒ essere multivalore, quando ciò si verifica ogni valore DEVE essere separato da uno spazio.
      - :rfc:`6749`
    * - **authorization_details**
      - Array di Oggetti JSON. Ogni Oggetto JSON DEVE includere i seguenti claim:

            - **type**: DEVE essere valorizzato con ``openid_credential``,
            - **credential_configuration_id**: Stringa JSON. Stringa che indica un identificativo univoco dell'Attestato Elettronico in uno specifico formato che DEVE essere mappato nel claim `credential_configurations_supported` presente nei Metadata del Credential Issuer. Ad esempio, ``dc_sd_jwt_PersonIdentificationData`` può essere utilizzato per il PID in formato SD-JWT VC, ``dc_sd_jwt_mDL`` per la patente di guida in formato SD-JWT VC e ``mso_mdoc_mDL`` per la patente di guida in formato mdoc.
      - Vedi [RAR :rfc:`9396`] e [`OpenID4VCI`_].
    * - **redirect_uri**
      - *Redirection URI* a cui è indirizzata la response. DEVE essere un *universal link* oppure un *app link* registrato nel sistema operativo locale, in modo tale che quest'ultimo potrà fornirà la response all'Istanza del Wallet.
      - Vedi [`OIDC`_] Sezione 3.1.2.1.
    * - **jti**
      - Identificativo univoco del JWT che, insieme al valore contenuto nel claim ``iss``, impedisce il riutilizzo del JWT (*replay attack*). Siccome il valore del `jti` da solo non è resistente alle collisioni, esso DOVRA' essere identificato in modo univoco insieme al suo emittente.
      - [:rfc:`7519`].
    * - **issuer_state**
      - DEVE essere presente solo in caso di *issuer initiated flow**. DEVE contenere lo stesso valore presente nel Credential Offer.
      - [:rfc:`7519`].

.. note::
  Se la request contiene sia *scope* che il parametro *authorization_details*, il Credential Issuer DEVE interpretarli individualmente. Tuttavia, se entrambi richiedono lo stesso tipo di Attestato Elettronico, il Credential Issuer DEVE eseguire la richiesta come se pervenuta soltanto dall'oggetto authorization details.

Il JOSE Header della prova di possesso dell'Attestato di Unità di Wallet, contenuta negli header della HTTP Request, DEVE contenere:

.. _table_jwt_pop:
.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **JOSE Header**
      - **Descrizione**
      - **Riferimento**
    * - **alg**
      - Identificativo dell'algoritmo di firma digitale come definito nel registro IANA "JSON Web Signature and Encryption Algorithms". DEVE essere uno degli algoritmi supportati elencati nella Sezione :ref:`algorithms:Algoritmi Crittografici` e NON DEVE essere valorizzato con ``none`` o con qualsiasi identificativo di algoritmo simmetrico (MAC).
      - :rfc:`7516#section-4.1.1`.

Il body del JWT relativo alla prova di possesso dell'Attestato di Unità di Wallet, contenuto negli header della HTTP Request, DEVE contenere:

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Descrizione**
      - **Riferimento**
    * - **iss**
      - *thumbprint* del JWK contenuto nel parametro ``cnf``.
      - :rfc:`9126` e :rfc:`7519`.
    * - **aud**
      - DEVE essere valorizzato con l'identificativo del Credential Issuer.
      - :rfc:`9126` e :rfc:`7519`.
    * - **exp**
      - Timestamp UNIX con data e orario di scadenza del JWT.
      - :rfc:`9126` e :rfc:`7519`.
    * - **iat**
      - Timestamp UNIX con data e orario di emissione del JWT.
      - :rfc:`9126` e :rfc:`7519`.
    * - **jti**
      - Identificativo univoco per il JWT *DPoP proof*. Il valore DOVREBBE essere impostato utilizzando un valore *UUID v4* secondo [:rfc:`4122`].
      - [:rfc:`7519`. Sezione 4.1.7].

Pushed Authorization Request (PAR) Response
......................................................

Se i controlli hanno esito positivo, il Credential Issuer DEVE fornire la response con *status code HTTP 201*. I seguenti parametri sono inclusi come parametri di primo livello nel body del messaggio di HTTP Response, utilizzando il media type ``application/json`` come definito nel [:rfc:`8259`].

.. _table_http_response_claim:
.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Descrizione**
      - **Riferimento**
    * - **request_uri**
      - Request URI associato all'authorization request inviata. Questo URI DEVE essere utilizzabile una sola volta per la corrispondente authorization request. DEVE contenere alcune parti generate utilizzando un algoritmo pseudocasuale crittograficamente forte. Il suo valore DEVE seguire il seguente formato: ``urn:ietf:params:oauth:request_uri:<reference-value>`` con ``<reference-value>`` come parte random dello URI che fa riferimento ai dati inviati nell'authorization request.
      - [:rfc:`9126`].
    * - **expires_in**
      - *JSON number*, numero intero positivo, che rappresenta la durata del Request URI in secondi.
      - [:rfc:`9126`].

Se si verificano errori durante la PAR Request, l'Authorization Server DEVE restituire una response di errore come definito nel :rfc:`9126#section-2.3`. La response DEVE avere un content type *application/json* e DEVE includere i seguenti parametri:

  - *error*. Il codice di errore.
  - *error_description*. Testo in forma *human-readable* che fornisce ulteriori dettagli per chiarire la natura dell'errore riscontrato.

Di seguito è riportato un esempio non normativo di una response di errore.

.. code:: http

  HTTP/1.1 400 Bad Request
  Content-Type: application/json

.. literalinclude:: ../../examples/par-error.json
  :language: JSON

Nella seguente tabella sono elencati gli *Status Code HTTP* e i relativi codici di errore supportati per la response di errore:

.. list-table::
    :class: longtable
    :widths: 20 20 60
    :header-rows: 1

    * - **Status Code**
      - **codice di errore**
      - **Descrizione**
    * - *400 Bad Request* [OBBLIGATORIO]
      - ``invalid_request``
      - Il Credential Issuer non può soddisfare la richiesta a causa di parametri mancanti, parametri non validi o richiesta malformata. (:rfc:`6749#section-5.2`).
    * - *400 Bad Request* [OBBLIGATORIO]
      - ``invalid_scope``
      - Il Credential Issuer non può soddisfare la richiesta perché lo scope richiesto non è valido oppure è sconosciuto. (:rfc:`6749#section-5.2`).
    * - *401 Unauthorized* [OBBLIGATORIO]
      - ``invalid_client``
      - Il Credential Issuer non può soddisfare la richiesta a causa del fallimento della *Client Authentication* (ad esempio in caso di client sconosciuto, nessun parametro relativo alla Client Authentication presente oppure se il metodo di autenticazione non è supportato). (:rfc:`6749#section-5.2`).
    * - *405 Method not allowed* [OPZIONALE]
      - `-`
      - Il Credential Issuer non può soddisfare la richiesta perché il metodo POST non è stato utilizzato nella richiesta. (:rfc:`9126#section-2.3`).
    * - *413 Payload Too Large* [OPZIONALE]
      - `-`
      - Il Credential Issuer non può soddisfare la richiesta perché la dimensione della richiesta è superiore al limite consentito.(:rfc:`9126#section-2.3`).
    * - *429 Too Many Requests* [OPZIONALE]
      - `-`
      - Il Credential Issuer non può soddisfare la richiesta perché il numero di richieste ricevute è superiore al limite consentito.(:rfc:`9126#section-2.3`).
    * - *500 Internal Server Error* [OBBLIGATORIO]
      - ``server_error``
      - Il Credential Issuer ha riscontrato un problema interno. (:rfc:`6749#section-4.1.2.1`).
    * - *503 Service Unavailable* [OBBLIGATORIO]
      - ``temporarily_unavailable``
      - Il Credential Issuer è temporaneamente non disponibile. (:rfc:`6749#section-4.1.2.1`).
    * - *504 Gateway Timeout* [OPZIONALE]
      - `-`
      - Il Credential Issuer non può soddisfare la richiesta entro l'intervallo di tempo definito.



Authorization endpoint
""""""""""""""""""""""""""

L'authorization endpoint viene utilizzato per interagire con il Credential Issuer e ottenere un *authorization grant*.
L'authorization server DEVE prima verificare l'identità dell'Utente proprietario dell'Attestato Elettronico.


Authorization Request
...........................

L'authorization request viene inviata dal Browser Web in uso dall'Istanza del Wallet usando i metodi HTTP **POST** o **GET**. Se viene utilizzato il metodo **POST**, i parametri DEVONO essere inviati utilizzando la *Form Serialization*. Quando viene utilizzato il metodo **GET**, i parametri DEVONO essere inviati utilizzando la *Query String Serialization*. Per maggiori dettagli vedere la Sezione 13 di [`OIDC`_].

I parametri obbligatori nell'authentication request HTTP sono specificati nella seguente tabella.

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Descrizione**
      - **Riferimento**
    * - **client_id**
      - DEVE essere valorizzato come indicato nella :ref:`Tabella dei parametri HTTP <table_http_request_claim>`.
      - Vedi :ref:`Tabella dei parametri HTTP <table_http_request_claim>`.
    * - **request_uri**
      - DEVE essere valorizzato con lo stesso valore ottenuto dalla PAR Response. Vedi :ref:`Tabella dei parametri della Risposta HTTP PAR <table_http_response_claim>`.
      - [:rfc:`9126`].

Authorization Response
..........................

L'authentication response viene restituita dall'authorization endpoint del Credential Issuer al termine del flusso di autenticazione.

Se l'autenticazione ha esito positivo, il Credential Issuer reindirizza l'Utente aggiungendo i seguenti parametri di query al *redirect_uri*. Il redirect URI DEVE essere un *universal link* o un *app link* registrato nel sistema operativo locale, in modo che quest'ultimo sia in grado di fornire la response all'Istanza del Wallet.

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Descrizione**
      - **Riferimento**
    * - **code**
      - *Authorization Code* univoco che l'Istanza del Wallet invia al Token Endpoint.
      - [:rfc:`6749#section-4.1.2`], [:rfc:`7521`].
    * - **state**
      - L'Istanza del Wallet DEVE verificare la corrispondenza con il valore presente nel parametro ``state`` del Request Object, come definito nella :ref:`Tabella dei parametri della Richiesta JWT <table_jwt_request>`.
      - [:rfc:`6749#section-4.1.2`].
    * - **iss**
      - Identificativo univoco del Credential Issuer che ha creato l'Authentication Response. L'Istanza del Wallet DEVE validare questo parametro.
      - [:rfc:`9207`], [:rfc:`7519`, Sezione 4.1.1.].

Se si verificano errori durante l'Authorization Request, l'Authorization Server DEVE restituire una response di errore come definito nel :rfc:`6749#section-4.1.2.1`.
In caso di ``redirect_uri`` o ``client_id`` non valido/mancante, l'Authorization Server DEVE informare l'Utente con l'errore e NON DEVE reindirizzare l'Utente verso il *Redirection URI*.
Se si verifica qualsiasi altro errore, l'Authorization Server DEVE reindirizzare l'Utente aggiungendo i seguenti parametri in query come richiesto al *redirect_uri* utilizzando il formato *application/x-www-form-urlencoded*:

  - *error*. Il codice di errore.
  - *error_description*. Testo in forma *human-readable* che fornisce ulteriori dettagli per chiarire la natura dell'errore riscontrato.
  - *state*. Il valore esatto del parametro ``state`` contenuto nel Request Object.

Di seguito è riportato un esempio non normativo di una response di errore.

.. code:: http

  HTTP/1.1 302 Found
  Location: https://client.example.com/cb?
   error=invalid_request
   &error_description=Unsupported%20response_type%20value
   &state=fyZiOL9Lf2CeKuNT2JzxiLRDink0uPcd

Nel caso in cui l'Authorization Server reindirizza l'Utente verso il *redirect_uri* DEVE essere utilizzato lo *status code HTTP 302 (Found)*. I seguenti codici di errore sono supportati per la response di errore:

.. list-table::
    :class: longtable
    :widths: 20 20 60
    :header-rows: 1

    * - **Status Code**
      - **codice di errore**
      - **Descrizione**
    * - *302 Found* [OBBLIGATORIO]
      - ``invalid_request``
      - Il Credential Issuer non può soddisfare la richiesta a causa di parametri mancanti, parametri non validi o richiesta malformata. (:rfc:`6749#section-4.1.2.1`).
    * - *302 Found* [OBBLIGATORIO]
      - ``unauthorized_client``
      - Il Credential Issuer non può soddisfare la richiesta perché il client non è autorizzato a richiedere *authorization code*. (:rfc:`6749#section-4.1.2.1`).
    * - *302 Found* [OBBLIGATORIO]
      - ``server_error``
      - Il Credential Issuer ha riscontrato un problema interno. (:rfc:`6749#section-4.1.2.1`).
    * - *302 Found* [OBBLIGATORIO]
      - ``temporarily_unavailable``
      - Il Credential Issuer è temporaneamente non disponibile. (:rfc:`6749#section-4.1.2.1`).

Nel caso in cui l'Authorization Server non reindirizza l'Utente verso il *redirect_uri* i seguenti *Status Code HTTP* sono supportati per la respomse di errore:

.. list-table::
    :class: longtable
    :widths: 20 80
    :header-rows: 1

    * - **Codice di Stato**
      - **Descrizione**
    * - *400 Bad Request* [OBBLIGATORIO]
      - Il Credential Issuer non può soddisfare la richiesta a causa del parametro ``redirect_uri`` o ``client_id`` non valido/mancante.
    * - *500 Internal Server Error* [OBBLIGATORIO]
      - Il Credential Issuer ha riscontrato un problema interno.
    * - *503 Service Unavailable* [OBBLIGATORIO]
      - Il Credential Issuer è temporaneamente non disponibile.
    * - *504 Gateway Timeout* [OPZIONALE]
      - Il Credential Issuer non può soddisfare la richiesta entro l'intervallo di tempo definito.


Token Endpoint
""""""""""""""

Il Token Endpoint viene utilizzato dall'Istanza del Wallet per ottenere un *Access Token* previa presentazione dell'*authorization grant*, come
definito nel :rfc:`6749`. Il Token Endpoint è un endpoint protetto con *OAuth 2.0 Attestation-based Client Authentication* [`OAUTH-ATTESTATION-CLIENT-AUTH`_ ].


Token Request
..................

La richiesta al Token Endpoint del Credential Issuer DEVE essere una HTTP request con metodo POST, con il body del messaggio codificato in formato ``application/x-www-form-urlencoded``. L'Istanza del Wallet invia la richiesta al Token Endpoint con ``OAuth-Client-Attestation`` e ``OAuth-Client-Attestation-PoP`` come parametri di header secondo `OAUTH-ATTESTATION-CLIENT-AUTH`_.

Il Token Endpoint è protetto con *OAuth 2.0 Attestation-based Client Authentication* [`OAUTH-ATTESTATION-CLIENT-AUTH`_], pertanto
la richiesta all'authorization endpoint del Credential Issuer DEVE utilizzare i seguenti parametri di header HTTP **OAuth-Client-Attestation** e **OAuth-Client-Attestation-PoP**
come definito in :ref:`credential-issuance-endpoint:Pushed Authorization Request Endpoint`.

Il Token Endpoint emette il token DPoP, pertanto è OBBLIGATORIO che la request includa nel suo header HTTP il parametro *DPoP proof*.
L'Authorization Server DEVE convalidare il *DPoP proof* ricevuto al Token Endpoint, secondo quanto indicato nella Sezione 4.3 di :rfc:`9449`. Ciò mitiga l'uso improprio di Access Token/Refresh Token persi o rubati al Credential/Token Endpoint. Se il *DPoP proof* non è valido, il Token Endpoint restituisce una response di errore, secondo quanto deinito nella Sezione 5.2 del [:rfc:`6749`] con ``invalid_dpop_proof`` come valore del parametro di errore.

La token request contiene i seguenti claim:

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Descrizione**
      - **Riferimento**
    * - **grant_type**
      - OBBLIGATORIO. DEVE essere valorizzato con ``authorization_code`` o ``refresh_token``.
      - [:rfc:`6749`].
    * - **code**
      - OBBLIGATORIO solo se il *grant type* è ``authorization_code``. L'Authorization code restituito nell'Authentication Response. NON DEVE essere presente se il *grant type* è ``refresh_token``.
      - [:rfc:`6749`].
    * - **redirect_uri**
      - OBBLIGATORIO solo se il *grant type* è ``authorization_code``. DEVE essere valorizzato come nel Request Object  :ref:`Tabella dei parametri della Richiesta JWT <table_jwt_request>`. NON DEVE essere presente se il *grant type* è ``refresh_token``.
      - [:rfc:`67491`].
    * - **code_verifier**
      - OBBLIGATORIO solo se il *grant type* è ``authorization_code``. Codice di verifica del **code_challenge**.
      - `Proof Key for Code Exchange by OAuth Public Clients <https://datatracker.ietf.org/doc/html/rfc7636>`_. NON DEVE essere presente se il *grant type* è ``refresh_token``.
    * - **refresh_token**
      - OBBLIGATORIO solo se il *grant type* è ``refresh_token``. Il Refresh Token precedentemente emesso all'Istanza del Wallet. NON DEVE essere presente se il *grant type* è ``authorization_code``.
      - [:rfc:`6749`].
    * - **scope**
      - OPZIONALE solo se il *grant type* è ``refresh_token``. Lo scope richiesto NON DEVE includere alcun valore di scope non originariamente concesso dall'Utente, e se omesso è da intendersi  uguale allo scope originariamente concesso dall'Utente. NON DEVE essere presente se il *grant type* è ``authorization_code``.
      - [:rfc:`6749`].


Un *JWT DPoP Proof** è incluso nella request HTTP utilizzando il parametro di header ``DPoP`` contenente un JWT DPoP.

Il JOSE Header di un **JWT DPoP** DEVE contenere almeno i seguenti parametri:

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **JOSE Header**
      - **Descrizione**
      - **Riferimento**
    * - **typ**
      - DEVE essere uguale a ``dpop+jwt``.
      - [:rfc:`7515`] e [:rfc:`8725`. Sezione 3.11].
    * - **alg**
      - Identificativo dell'algoritmo di firma digitale come definito nel registro IANA "JSON Web Signature and Encryption Algorithms". DEVE essere uno degli algoritmi supportati elencati nella Sezione :ref:`algorithms:Algoritmi Crittografici` e NON DEVE essere valorizzato con ``none`` o con qualsiasi identificativo di algoritmo simmetrico (MAC).
      - [:rfc:`7515`].
    * - **jwk**
      - Rappresenta la chiave pubblica scelta dall'Istanza del Wallet, in formato JSON Web Key (JWK) [:rfc:`7517`] a cui l'Access Token DEVE essere vincolato, come definito nella Sezione 4.1.3 del [:rfc:`7515`]. NON DEVE contenere una chiave privata.
      - [:rfc:`7517`] e [:rfc:`7515`].


Il payload del **JWT DPoP Proof** DEVE contenere i seguenti claim:

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Descrizione**
      - **Riferimento**
    * - **jti**
      - Identificativo univoco per il JWT *DPoP proof*. Il valore DOVREBBE essere un valore *UUID v4* secondo [:rfc:`4122`].
      - [:rfc:`7519`. Sezione 4.1.7].
    * - **htm**
      - Il valore del metodo HTTP della request a cui è allegato il JWT.
      - [:rfc:`9110`. Sezione 9.1].
    * - **htu**
      - Target URI HTTP, senza le parti di query e fragment, della request a cui è allegato il JWT.
      - [:rfc:`9110`. Sezione 7.1].
    * - **iat**
      - Timestamp UNIX con data e orario di emissione del JWT, codificato come NumericDate come indicato nel :rfc:`7519`.
      - [:rfc:`7519`. Sezione 4.1.6].


Token Response
.................

Se la Token Request viene validata con successo, l'Authorization Server fornisce una Token Response con *status code HTTP 200 (OK)*. La Token Response  contiene i seguenti claim.

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Descrizione**
      - **Riferimento**
    * - **access_token**
      - OBBLIGATORIO. Il *DPoP-bound Access Token*, in formato JWT firmato, consente di accedere al Credential Endpoint per ottenere l'Attestato Elettronico.
      - [:rfc:`6749`].
    * - **refresh_token**
      - OPZIONALE. Il *DPoP-bound Refresh Token*, in formato JWT firmato, che può essere utilizzato per ottenere un nuovo Access Token presso il Token Endpoint del Credential Issuer.
      - [:rfc:`6749`].
    * - **token_type**
      - OBBLIGATORIO. Tipo di *Access Token* restituito. DEVE essere uguale a ``DPoP``.
      - [:rfc:`6749`].
    * - **expires_in**
      - OBBLIGATORIO. Tempo di scadenza dell'*Access Token* in secondi.
      - [:rfc:`6749`].
    * - **authorization_details**
      - OBBLIGATORIO quando il parametro ``authorization_details`` viene utilizzato per richiedere l'emissione di un Attestato Elettronico. OPZIONALE quando il parametro ``scope`` viene utilizzato per richiedere l'emissione di un Attestato Elettronico. Array di Oggetti JSON, utilizzati per identificare gli Attestati Elettronici con gli stessi Metadata ma diversi valori di claimset/claim e/o semplificare la Credential Request anche quando viene emessa un solo Attestato Elettronico. Oltre al claim definito nella :ref:`Tabella dei parametri della Richiesta JWT <table_jwt_request>` DEVE includere il seguente claim:

            - **credential_identifiers**: Array di stringhe, ciascuna che identifica in modo univoco un set di dati dell'Attestato Elettronico disponibile per l'emissione.
      - [`OpenID4VCI`_].

Se si verificano errori durante la convalida della Token Request, l'Authorization Server DEVE restituire una response di errore come definito nel :rfc:`6749#section-5.2`. La response DEVE utilizzare il Content-Type HTTP *application/json* e DEVE includere i seguenti parametri:

  - *error*. Il codice di errore.
  - *error_description*. Testo in forma *human-readable* che fornisce ulteriori dettagli per chiarire la natura dell'errore riscontrato.

Di seguito è riportato un esempio non normativo di una response di errore.

.. code:: http

  HTTP/1.1 401 Unauthorized
  Content-Type: application/json;charset=UTF-8
  Cache-Control: no-store
  Pragma: no-cache

.. literalinclude:: ../../examples/token-error.json
  :language: JSON

Nella seguente tabella sono elencati i *status code HTTP* e i relativi codici di errore supportati per la response di errore:

.. list-table::
    :class: longtable
    :widths: 20 20 60
    :header-rows: 1

    * - **Status Code**
      - **codice di errore**
      - **Descrizione**
    * - *400 Bad Request* [OBBLIGATORIO]
      - ``invalid_request``
      - Il Credential Issuer non può soddisfare la richiesta a causa di parametri mancanti, parametri non validi o richiesta malformata. (:rfc:`6749#section-5.2`).
    * - *400 Bad Request* [OBBLIGATORIO]
      - ``invalid_grant``
      - Il Credential Issuer non può soddisfare la richiesta perché l'*authorization code* o il *Refresh Token* fornito non è valido, è scaduto, è stato revocato o non corrisponde al *redirection URI* utilizzato nell'authorization request, o è stato rilasciato ad un altro client. (:rfc:`6749#section-5.2`).
    * - *400 Bad Request* [OBBLIGATORIO]
      - ``unsupported_grant_type``
      - Il Credential Issuer non può soddisfare la richiesta perché il *grant type* non è supportato. (:rfc:`6749#section-5.2`).
    * - *400 Bad Request* [OBBLIGATORIO]
      - ``invalid_dpop_proof``
      - Il Credential Issuer non può soddisfare la richiesta a causa di un *DPoP proof* non valido. Sezione 5 del [:rfc:`9449`].
    * - *401 Unauthorized* [OBBLIGATORIO]
      - ``invalid_client``
      - Il Credential Issuer non può soddisfare la richiesta a causa del fallimento della *Client Authentication* (ad esempio in caso di client sconosciuto, nessun parametro relativo alla Client Authentication presente oppure se il metodo di autenticazione non è supportato). (:rfc:`6749#section-5.2`).
    * - *500 Internal Server Error* [OBBLIGATORIO]
      - ``server_error``
      - Il Credential Issuer ha riscontrato un problema interno.
    * - *503 Service Unavailable* [OBBLIGATORIO]
      - ``temporarily_unavailable``
      - Il Credential Issuer è temporaneamente non disponibile.
    * - *504 Gateway Timeout* [OPZIONALE]
      - `-`
      - Il Credential Issuer non può soddisfare la richiesta entro l'intervallo di tempo definito.

Access Token
................

Un *DPoP-bound Access Token** viene fornito dal Token Endpoint del Credential Issuer come risultato di una token request andata a buon fine . L'Access Token è codificato in formato JWT, secondo [:rfc:`7519`]. L'Access Token DEVE avere almeno i seguenti claim obbligatori e DEVE essere vincolato alla chiave pubblica fornita dal *DPoP proof*. Questo vincolo può essere realizzato in base alla metodologia definita nella Sezione 6 del (:rfc:`9449`).

Il **JWT DPoP** contiene i seguenti parametri di header JOSE e claim.

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **JOSE Header**
      - **Descrizione**
      - **Riferimento**
    * - **typ**
      - OBBLIGATORIO. DEVE essere uguale a ``at+jwt``.
      - [:rfc:`7515`].
    * - **alg**
      - OBBLIGATORIO. Identificativo dell'algoritmo di firma digitale come definito nel registro IANA "JSON Web Signature and Encryption Algorithms". DEVE essere uno degli algoritmi supportati elencati nella Sezione :ref:`algorithms:Algoritmi Crittografici` e NON DEVE essere valorizzato con ``none`` o con qualsiasi identificativo di algoritmo simmetrico (MAC).
      - [:rfc:`7515`].
    * - **kid**
      - OBBLIGATORIO. Identificativo univoco del ``jwk`` utilizzato dal Credential Issuer per firmare l'Access Token.
      - :rfc:`7638#section_3`.


.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Claim**
    - **Descrizione**
    - **Riferimento**
  * - **iss**
    - OBBLIGATORIO. DEVE essere un URL HTTPS che identifica in modo univoco il Credential Issuer. L'Istanza del Wallet DEVE verificare che questo valore corrisponda al Credential Issuer a cui ha richiesto l'Attestato Elettronico.
    - [:rfc:`9068`], [:rfc:`7519`].
  * - **sub**
    - OBBLIGATORIO. Identifica il soggetto del JWT. DEVE essere settato con il valore del campo ``sub`` presente nell'Attestato ELettronico in formato SD-JWT-VC.
    - [:rfc:`9068`], [:rfc:`7519`] e Sezione 8 di [`OIDC`_].
  * - **client_id**
    - OBBLIGATORIO. L'identificativo dell'Istanza del Wallet che ha richiesto l'Access Token; DEVE essere uguale al kid della chiave pubblica dell'Istanza del Wallet specificata nell'Attestato di Unità di Wallet (``cnf.jwk``).
    - [:rfc:`9068`], [:rfc:`7519`] e Sezione 8 di [`OIDC`_].
  * - **aud**
    - OBBLIGATORIO. DEVE essere valorizzato con l'identificativo del Credential Issuer.
    - [:rfc:`9068`].
  * - **iat**
    - OBBLIGATORIO. Timestamp UNIX con data e orario di emissione del JWT, codificato come NumericDate come indicato nel :rfc:`7519`.
    - [:rfc:`9068`], [:rfc:`7519`. Sezione 4.1.6].
  * - **exp**
    - OBBLIGATORIO. Timestamp UNIX con data e orario di scadenza del JWT, codificato come NumericDate come indicato nel :rfc:`7519`.
    - [:rfc:`9068`], [:rfc:`7519`].
  * - **jti**
    - OPZIONALE. DEVE essere una Stringa in formato *uuid4*. Identificativo univoco del Token ID che la RP DOVREBBE utilizzare per prevenire il riutilizzo rifiutando l'ID Token se è stato già elaborato.
    - [:rfc:`9068`], [:rfc:`7519`].
  * - **cnf**
    - OBBLIGATORIO. DEVE contenere un claim **jkt** che è un Metodo di Conferma del *Thumbprint JWK SHA-256*. Il valore del parametro *jkt* DEVE contenere la codifica base64url (come definito nel [:rfc:`7515`]) del *Thumbprint JWK SHA-256* della chiave pubblica DPoP (in formato JWK) a cui è vincolato l'Access Token.
    - [:rfc:`9449`. Sezione 6.1] e [:rfc:`7638`].

Refresh Token
......................

Un *DPoP-bound Refresh Token* viene fornito dal Token endpoint del Credential Issuer come risultato di una token request andata a buon fine. Il Refresh Token è codificato in formato JWT, secondo [:rfc:`7519`]. Il Refresh Token DEVE avere almeno i seguenti claim obbligatori e DEVE essere vincolato alla chiave pubblica fornita dal *DPoP proof*. Questo vincolo può essere realizzato in base alla metodologia definita nella Sezione 6 del (:rfc:`9449`).

Il **JWT DPoP** DEVE contenere i seguenti parametri di header JOSE e claim.

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **JOSE Header**
      - **Descrizione**
      - **Riferimento**
    * - **typ**
      - DEVE essere uguale a ``rt+jwt``.
      - [:rfc:`7515`].
    * - **alg**
      - Identificativo dell'algoritmo di firma digitale come definito nel registro IANA "JSON Web Signature and Encryption Algorithms". DEVE essere uno degli algoritmi supportati elencati nella Sezione :ref:`algorithms:Algoritmi Crittografici` e NON DEVE essere valorizzato con ``none`` o con qualsiasi identificativo di algoritmo simmetrico (MAC).
      - [:rfc:`7515`].
    * - **kid**
      - Identificativo univoco del ``jwk`` utilizzato dal Credential Issuer per firmare l'Access Token.
      - :rfc:`7638#section_3`.


.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Claim**
    - **Descrizione**
    - **Riferimento**
  * - **iss**
    - DEVE essere un URL HTTPS che identifica in modo univoco il Credential Issuer. L'Istanza del Wallet DEVE verificare che questo valore corrisponda al Credential Issuer a cui ha richiesto l'Attestato Elettronico.
    - [:rfc:`9068`], [:rfc:`7519`].
  * - **sub**
    - Identifica il soggetto del JWT. DEVE essere settato con il valore del campo ``sub`` presente nell'Attestato ELettronico in formato SD-JWT-VC.
    - [:rfc:`9068`], [:rfc:`7519`] e Sezione 8 di [`OIDC`_].
  * - **client_id**
    - L'identificativo per l'Istanza del Wallet che ha richiesto l'Access Token; DEVE essere uguale al valore del `kid` che identifica la chiave pubblica utilizzata nell'Istanza del Wallet, utilizzata nell'Attestato di Unità di Wallet (``cnf.jwk``).
    - [:rfc:`9068`], [:rfc:`7519`] e Sezione 8 di [`OIDC`_].
  * - **aud**
    - DEVE essere valorizzato con l'identificativo del Credential Issuer.
    - [:rfc:`9068`].
  * - **iat**
    - Timestamp UNIX con data e orario di emissione del JWT, codificato come NumericDate come indicato nel :rfc:`7519`.
    - [:rfc:`9068`], [:rfc:`7519`. Sezione 4.1.6].
  * - **nbf**
    - Timestamp UNIX con data e orario prima del quale il JWT NON DEVE essere accettato, codificato come NumericDate come indicato nel :rfc:`7519`. DOVREBBE essere impostato sul claim ``exp`` del corrispondente Token di Accesso.
    - [:rfc:`7519`. Sezione 4.1.7].
  * - **exp**
    - Timestamp UNIX con data e orario di scadenza del JWT, codificato come NumericDate come indicato nel :rfc:`7519`.
    - [:rfc:`9068`], [:rfc:`7519`].
  * - **jti**
    - DEVE essere una Stringa in formato *uuid4*. Identificativo univoco del Token ID che la RP DOVREBBE utilizzare per prevenire il riutilizzo rifiutando l'ID Token se è stato già elaborato.
    - [:rfc:`9068`], [:rfc:`7519`].
  * - **cnf**
    - DEVE contenere un claim **jkt** che è un Metodo di Conferma del *Thumbprint JWK SHA-256*. Il valore del parametro *jkt* DEVE contenere la codifica base64url (come definito nel [:rfc:`7515`]) del *Thumbprint JWK SHA-256* della chiave pubblica DPoP (in formato JWK) a cui è vincolato l'Access Token.
    - [:rfc:`9449`. Sezione 6.1] e [:rfc:`7638`].

Nonce Endpoint
""""""""""""""

Il Nonce Endpoint fornisce un valore del ``c_nonce`` utile per creare una prova di possesso del materiale crittografico per la richiesta al Credential Endpoint, come definito nella Sezione 7 di `OpenID4VCI`_.

Nonce Request
..................

La Nonce Request DEVE essere una HTTP POST request senza body indirizzata al Nonce Endpoint del Credential Issuer censito nei Metadata del Credential Issuer.


Nonce Response
.................

La Nonce Response DEVE essere inviata all'Istanza del Wallet utilizzando il media type `application/json`. In caso di Nonce Request andata a buon fine, il Credential Issuer DEVE restituire una HTTP response con *status code HTTP 200 (OK)*.

Come definito nella Sezione 7.2 di `OpenID4VCI`_, il Credential Issuer DEVE rendere la risposta non memorizzabile nella cache aggiungendo il campo di header ``Cache-Control`` valorizzato con *no-store*.

La Nonce Response contiene il seguente parametro:

.. list-table::
  :widths: 20 60 20
  :header-rows: 1

  * - **Claim**
    - **Descrizione**
    - **Riferimento**
  * - **c_nonce**
    - OBBLIGATORIO. Stringa contenente il valore del nonce. Questo valore DEVE essere imprevedibile.
    - Sezione 7.2 di [`OpenID4VCI`_].

Credential Endpoint
"""""""""""""""""""

Il Credential Endpoint emette un'Attestato Eletronico previa presentazione di un Access Token valido, come definito in `OpenID4VCI`_.


Credential Request
........................

L'Istanza del Wallet quando richiede l'Attestato Elettronico al Credential Endpoint, DEVE utilizzare i seguenti parametri nel body del messaggio della HTTP POST request, utilizzando il tipo di media `application/json`.

Il Credential Endpoint DEVE accettare e convalidare il *DPoP proof* inviato nel parametro di header HTTP *DPoP*, secondo i passaggi definiti nella Sezione 4.3 del (:rfc:`9449`). Il *DPoP proof* oltre ai valori definiti nella sezione Token Endpoint DEVE contenere il seguente claim:

  - **ath**: valore di hash dell'Access Token codificato in ASCII. Il valore DEVE utilizzare la codifica base64url (come definito nella Sezione 2 del (:rfc:`7515`) con l'algoritmo SHA-256.

.. warning::
  L'Istanza del Wallet DEVE creare un **nuovo DPoP proof** per la Credential Request e NON DEVE utilizzare la *proof* precedentemente creata per il Token Endpoint.


.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Claim**
    - **Descrizione**
    - **Riferimento**
  * - **credential_identifier**
    - OBBLIGATORIO quando Authorization Details di tipo *openid_credential* è stato restituito dalla Token. In tutti gli altri casi NON DEVE essere utilizzato. Questo DEVE essere valorizzato con uno dei valori ottenuti nel claim ``credential_identifiers`` della Token Response. NON DEVE essere utilizzato se è presente ``credential_configuration_id``.
    - Sezione 8.2 di [`OpenID4VCI`_].
  * - **credential_configuration_id**
    - OBBLIGATORIO se il parametro ``credential_identifiers`` è assente nella Token Response.  In tutti gli altri casi NON DEVE essere utilizzato. Stringa che specifica un identificativo univoco dell'Attestato ELetronico descritto nel claim `credential_configurations_supported` presente nei Metadata del Credential Issuer. Ad esempio, nel caso del PID, può essere valorizzato con ``PersonIdentificationData``.
    - Sezione 8.2 di [`OpenID4VCI`_].
  * - **proof**
    - OBBLIGATORIO. Oggetto JSON contenente la prova di possesso del materiale crittografico a cui sarà vincolato l'Attestato Elettronico emesso. L'oggetto proof DEVE contenere i seguenti claim obbligatori:

      - **proof_type**: stringa JSON che denota il tipo di prova in termini di formato. DEVE essere `jwt`.
      - **jwt**: il JWT utilizzato come prova di possesso.
    - [`OpenID4VCI`_].
  * - **transaction_id**
    - OBBLIGATORIO solo in caso di Deferred Flow. Stringa che identifica una transazione di emissione posticipata. NON DEVE essere presente nel flusso di emissione immediato.
    - Sezione 9.1 di [`OpenID4VCI`_].


Il *proof type* del JWT DEVE contenere i seguenti parametri per l'header JOSE e il body in JWT:

.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **JOSE Header**
    - **Descrizione**
    - **Riferimento**
  * - **alg**
    - Identificativo dell'algoritmo di firma digitale come definito nel registro IANA "JSON Web Signature and Encryption Algorithms". DEVE essere uno degli algoritmi supportati elencati nella Sezione :ref:`algorithms:Algoritmi Crittografici` e NON DEVE essere valorizzato con ``none`` o con qualsiasi identificativo di algoritmo simmetrico (MAC).
    - [`OpenID4VCI`_], [:rfc:`7515`], [:rfc:`7517`].
  * - **typ**
    - DEVE essere valorizzato con `openid4vci-proof+jwt`.
    - [`OpenID4VCI`_], [:rfc:`7515`], [:rfc:`7517`].
  * - **jwk**
    - Rappresenta la chiave pubblica scelta dall'Istanza del Wallet, in formato JSON Web Key (JWK) [:rfc:`7517`] a cui l'Attestato Elettronico sarà vincolato, come definito nella Sezione 4.1.3 del [:rfc:`7515`].
    - [`OpenID4VCI`_], [:rfc:`7515`], [:rfc:`7517`].

.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Claim**
    - **Descrizione**
    - **Riferimento**
  * - **iss**
    - Il valore di questo claim DEVE essere il **client_id** dell'Istanza del Wallet.
    - [`OpenID4VCI`_], [:rfc:`7519`, Sezione 4.1.1].
  * - **aud**
    - DEVE essere valorizzato con l'identificativo del Credential Issuer.
    - [`OpenID4VCI`_].
  * - **iat**
    - Timestamp UNIX con data e orario  di emissione del JWT, codificato come NumericDate come indicato nel :rfc:`7519`.
    - [`OpenID4VCI`_], [:rfc:`7519`. Sezione 4.1.6].
  * - **nonce**
    - Il tipo di valore di questo claim DEVE essere una stringa, dove il valore è un **c_nonce** fornito dal Credential Issuer tramite la Nonce Response.
    - [`OpenID4VCI`_].


Credential Response
.......................

La Credential Response DEVE essere inviata all'Istanza del Wallet utilizzando il media type `application/json`. Se la Credential Request viene validata con successo e l'Attestato Elettronico è immediatamente disponibile, il Credential Issuer DEVE restituire una HTTP response con un *status code HTTP 200 (OK)*. Se l'Attestato Elettronico non è disponibile e il Deferred Flow è supportato dal Credential Issuer, allora DEVE essere restituito un *status code HTTP 202*.

La Credential Response contiene i seguenti parametri:

.. _table_credential_response_claim:
.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Claim**
    - **Descrizione**
    - **Riferimento**
  * - **credentials**
    - OBBLIGATORIO se ``lead_time`` e ``transaction_id`` non sono presenti, altrimenti NON DEVE essere presente. Contiene i seguenti parametri:

          - **credential**: OBBLIGATORIO. Stringa contenente un Attestato Elettronico emesso. Se l'identificativo del formato richiesto è ``dc+sd-jwt`` allora il parametro ``credential`` NON DEVE essere ricodificato. Se l'identificativo di formato richiesto è ``mso_mdoc`` allora il parametro ``credential`` DEVE essere una rappresentazione codificata in base64url della struttura IssuerSigned codificata in CBOR, come definito in [ISO 18013-5]. Questa struttura DOVREBBE contenere tutti i Namespaces e IssuerSignedItems inclusi negli AuthorizedNamespaces del MobileSecurityObject.
    - Sezione 8.3, Allegato A2.4 e Allegato A3.4 di [`OpenID4VCI`_].
  * - **lead_time**
    - OBBLIGATORIO se ``credentials`` non è presente, altrimenti NON DEVE essere presente. La quantità di tempo (espressa in secondi) richiesta prima di effettuare una Deferred Credential Request.
    - Questa Specifica.
  * - **notification_id**
    - OPZIONALE. Stringa che identifica un'Attestato Elettronico emesso che il Wallet include nella Notification Request come definito nella Sezione :ref:`credential-issuance-endpoint:Notification Request`. NON DEVE essere presente se il parametro ``credentials`` non è presente.
    - Sezione 8.3 di [`OpenID4VCI`_].
  * - **transaction_id**
    - OBBLIGATORIO se ``credentials`` non è presente, altrimenti NON DEVE essere presente. Stringa che identifica una transazione di emissione posticipata che il Wallet include nella successiva Credential Request come definito nella Sezione :ref:`credential-issuance-endpoint:Deferred Endpoint`. DEVE essere invalidato dopo che l'Utente ottiene l'Attestato Elettronico.
    - Sezione 8.3 di [`OpenID4VCI`_].

Nel caso in cui la Credential Request non contenga un Access Token valido, il Credential Endpoint restituisce una response di errore come definito nella Sezione 3 del [:rfc:`6750`].
Se si verifica qualsiasi altro errore, il Credential Issuer DEVE restituire una response di errore come definito nella Sezione 8.3.1 di [`OpenID4VCI`_]. La response DEVE utilizzare il content type *application/json* e DEVE includere i seguenti parametri:

  - *error*. Il codice di errore.
  - *error_description*. Testo in forma *human-readable* che fornisce ulteriori dettagli per chiarire la natura dell'errore riscontrato.

Di seguito è riportato un esempio non normativo di una response di errore.

.. code:: http

  HTTP/1.1 400 Bad Request
  Content-Type: application/json
  Cache-Control: no-store

.. literalinclude:: ../../examples/credential-error.json
  :language: JSON

Nella seguente tabella sono elencati i *Status Code HTTP* e i relativi codici di errore supportati per la response di errore:

.. list-table::
    :class: longtable
    :widths: 20 20 60
    :header-rows: 1

    * - **Status Code**
      - **codice di errore**
      - **Descrizione**
    * - *400 Bad Request* [OBBLIGATORIO]
      - ``invalid_credential_request``
      - Il Credential Issuer non può soddisfare la richiesta a causa di parametri mancanti, parametri non validi o richiesta malformata. Sezione 8.3.1 di [`OpenID4VCI`_].
    * - *400 Bad Request* [OBBLIGATORIO]
      - ``unsupported_credential_type``
      - Il Credential Issuer non può soddisfare la richiesta perché il tipo di Attestato Elettronico richiesto non è supportato. Sezione 8.3.1 di [`OpenID4VCI`_].
    * - *400 Bad Request* [OBBLIGATORIO]
      - ``unsupported_credential_format``
      - Il Credential Issuer non può soddisfare la richiesta perché il Formato dell'Attestato Elettronico richiesto non è supportato. Sezione 8.3.1 di [`OpenID4VCI`_].
    * - *400 Bad Request* [OBBLIGATORIO]
      - ``invalid_proof``
      - Il Credential Issuer non può soddisfare la richiesta perché il parametro ``proof`` nella Credential Request non è valido o è assente. Sezione 8.3.1 di [`OpenID4VCI`_].
    * - *400 Bad Request* [OBBLIGATORIO]
      - ``invalid_nonce``
      - Il Credential Issuer non può soddisfare la richiesta perché il parametro ``proof`` nella Credential Request utilizza un nonce non valido. Sezione 8.3.1 di [`OpenID4VCI`_].
    * - *400 Bad Request* [OBBLIGATORIO]
      - ``invalid_encryption_parameters``
      - Il Credential Issuer non può soddisfare la richiesta perché i parametri di crittografia nella Credential Request non sono validi o mancanti. Sezione 8.3.1 di [`OpenID4VCI`_].
    * - *400 Bad Request* [OBBLIGATORIO]
      - ``credential_request_denied``
      - La Credential Request non è stata accettata dal Credential Issuer. Sezione 8.3.1 di [`OpenID4VCI`_].
    * - *400 Bad Request* [OBBLIGATORIO]
      - ``issuance_pending``
      - Solo in caso di Deferred Flow. Il Credential Issuer non può soddisfare la richiesta perché l'Attestato Elettronico non è ancora disponibile per l'emissione. Sezione 9.3 di [`OpenID4VCI`_].
    * - *400 Bad Request* [OBBLIGATORIO]
      - ``invalid_transaction_id``
      - Solo in caso di Deferred Flow. Il Credential Issuer non può soddisfare la richiesta perché la Credential Request contiene un ``transaction_id`` non valido. Sezione 9.3 di [`OpenID4VCI`_].
    * - *400 Bad Request* [OBBLIGATORIO]
      - ``invalid_dpop_proof``
      - Il Credential Issuer non può soddisfare la richiesta a causa del *DPoP proof* non valido. Sezione 7 del [:rfc:`9449`].
    * - *500 Internal Server Error* [OBBLIGATORIO]
      - ``server_error``
      - Il Credential Issuer ha riscontrato un problema interno.
    * - *503 Service Unavailable* [OBBLIGATORIO]
      - ``temporarily_unavailable``
      - Il Credential Issuer è temporaneamente non disponibile.
    * - *504 Gateway Timeout* [OPZIONALE]
      - `-`
      - Il Credential Issuer non può soddisfare la richiesta entro l'intervallo di tempo definito.

Deferred Endpoint
""""""""""""""""""

I Credential Issuer POSSONO supportare il *Deferred Endpoint* con l'obiettivo di soddisfare i casi in cui un'emissione immediata potrebbe non essere possibile, a causa di errori durante la comunicazione tra il Credential Issuer e la Fonte Autentica (ad esempio la Fonte Autentica è temporaneamente non disponibile, ecc.) o a causa di processi amministrativi o tecnici da espletare.

Nel caso in cui la Fonte Autentica e il Credential Issuer siano entrambi abilitati a utilizzare *PDND*, si DEVE seguire quanto descritto nella Sezione :ref:`authentic-sources:Fonti Autentiche`.


Si applicano i seguenti requisiti:

 1. La Deferred Credential Request PUÒ avvenire anche diversi giorni dopo l'iniziale Credenziale Request.
 2. L'Utente DEVE essere informato che l'Attestato Elettronico è disponibile e pronto per essere emesso.
 3. Il Fornitore di Wallet NON DEVE essere informato su quale Attestato Elettronico è disponibile per l'emissione o quale Credential Issuer l'Utente deve contattare.
 4. L'Istanza del Wallet DEVE essere informata sulla quantità di tempo da attendere prima di effettuare una nuova Credential Request.
 5. Poiché, in generale, un'indisponibilità può essere un evento imprevisto, il Credential Issuer DEVE essere in grado di passare al volo tra un flusso *immediato* e uno *posticipato*. Questa decisione DEVE essere presa dopo la fase autorizzativa.


Se i Credential Issuer, che supportano questo flusso, non sono in grado di emettere immediatamente un Attestato ELettronico richiesto, DEVONO fornire all'Istanza del Wallet una Credential Response HTTP contenente la quantità di tempo da attendere prima di effettuare una nuova Credential Request e un identificativo della transazione di emissione posticipata (*transaction_id*). Lo *status code HTTP* previsto DEVE essere il *202* (vedi Sezione 15.3.3 del [:rfc:`9110`]). Di seguito viene fornito un esempio non normativo.

.. code-block:: http

  HTTP/1.1 202 Accepted
  Content-Type: application/json
  Cache-Control: no-store

.. literalinclude:: ../../examples/credential-response-deferred.json
  :language: JSON

L'Istanza del Wallet DEVE utilizzare il valore fornito nel parametro *lead_time* per informare l'Utente quando l'Attestato Elettronico diventa disponibile (ad esempio utilizzando una notifica locale innescata dal valore di tempo *lead_time*). I Credential Issuer POSSONO inviare una notifica all'Utente tramite un canale di comunicazione (ad esempio indirizzo email), se precedentemente fornito dall'Utente al Credential Issuer.

Deferred Request
...................

Una volta ricevuta la notifica (dall'Istanza del Wallet e/o dal Credential Issuer), l'Utente accede all'Istanza del Wallet.

L'Istanza del Wallet DEVE presentare al Deferred Endpoint un Access Token valido per l'emissione dell'Attestato Elettronico precedentemente richiesto al Credential Endpoint.

Se il valore del parametro ``lead_time`` risulta inferiore rispetto alla scadenza dell'Access Token, l'Istanza del Wallet DOVREBBE utilizzare l'Access Token. Altrimenti, l'Istanza del Wallet PUÒ ottenere un nuovo Access Token seguendo il flusso relativo al Refresh Token (vedi Sezione :ref:`credential-issuance-low-level:Refresh Token Flow` per maggiori dettagli). Se il flusso del Refresh Token fallisce, l'Istanza del Wallet deve inviare una nuova authentication request.

La Deferred Credential Request DEVE essere una HTTP POST request. DEVE essere inviata utilizzando il media type ``application/json``.
Il seguente parametro viene utilizzato nella Deferred Credential Request:

  - ``transaction_id``: OBBLIGATORIO. Stringa che identifica una transazione di Emissione posticipata.

Il Credential Issuer DEVE invalidare il ``transaction_id`` dopo che l'Attestato Elettronico per cui era destinato è stata ottenuto dall'Istanza del Wallet.
Di seguito è riportato un esempio non normativo di una Deferred Credential Request:

.. code::

  POST /credential HTTP/1.1
  Host: eaa-provider.example.org
  Content-Type: application/json
  Authorization: DPoP Kz~8mXK1EalYznwH-LC-1fBAo.4Ljp~zsPE_NeO.gxU
  DPoP: eyJ0eXAiOiJkcG9wK2p3dCIsImFsZyI6IkVTMjU2IiwiandrIjp7Imt0eSI6Ik
      VDIiwieCI6Imw4dEZyaHgtMzR0VjNoUklDUkRZOXpDa0RscEJoRjQyVVFVZldWQVdCR
      nMiLCJ5IjoiOVZFNGpmX09rX282NHpiVFRsY3VOSmFqSG10NnY5VERWclUwQ2R2R
      1JEQSIsImNydiI6IlAtMjU2In19.eyJqdGkiOiJlMWozVl9iS2ljOC1MQUVCIiwiaHRtIj
      oiR0VUIiwiaHR1IjoiaHR0cHM6Ly9yZXNvdXJjZS5leGFtcGxlLm9yZy9wcm90ZWN0Z
      WRyZXNvdXJjZSIsImlhdCI6MTU2MjI2MjYxOCwiYXRoIjoiZlVIeU8ycjJaM0RaNTNF
      c05yV0JiMHhXWG9hTnk1OUlpS0NBcWtzbVFFbyJ9.2oW9RP35yRqzhrtNP86L-Ey71E
      OptxRimPPToA1plemAgR6pxHF8y6-yqyVnmcw6Fy1dqd-jfxSYoMxhAJpLjA


  {
    "transaction_id": "8xLOxBtZp8"
  }

Deferred Response
..................

La Deferred Credential Response DEVE essere inviata utilizzando il media type `application/json``. Se l'Attestato Elettronico è disponibile, la Deferred Credential Response DEVE utilizzare i parametri ``credentials`` e ``notification_id`` come definito nella Sezione :ref:`credential-issuance-endpoint:Credential Response`. Se la Deferred Credential Request non è valida o l'Attestato Elettronico non è disponibile, la Deferred Credential Error Response DEVE essere inviata all'Istanza del Wallet secondo quanto indicato nella Sezione 9.3 di `OpenID4VCI`_.

Notification Endpoint
"""""""""""""""""""""

Il Notification Endpoint viene utilizzato dal Wallet per notificare al Credential Issuer determinati eventi relativi agli Attestati Elettronici emessi, come ad esempio se l'Attestato Elettronico è stato memorizzato con successo nell'Istanza del Wallet.

Per salvaguardare la privacy, l'``event_description`` nella notifica NON DOVREBBE contenere alcuna informazione che potrebbe rivelare il comportamento dell'Utente o rivelare lo stato del dispositivo personale (ad esempio, se lo spazio di archiviazione è pieno).

Questo endpoint DEVE essere protetto utilizzando un Access Token di tipo DPoP. Il protocollo TLS per la riservatezza del trasporto su HTTP è OBBLIGATORIO secondo la Sezione 10 di [`OpenID4VCI`_].


Notification Request
.....................

La Notification Request DEVE essere una HTTP POST utilizzando il media type *application/json* con i seguenti parametri.

.. list-table::
  :class: longtable
  :widths: 20 60 25
  :header-rows: 1

  * - **Claim**
    - **Descrizione**
    - **Riferimento**
  * - **notification_id**
    - OBBLIGATORIO. DEVE essere uguale al valore ``notification_id`` restituito nella Credential Response dal Credential Issuer.
    - Sezione 10.1 di [`OpenID4VCI`_].
  * - **event**
    - OBBLIGATORIO. Tipo dell'evento da notificare. DEVE essere una stringa case-sensitive e DEVE supportare i seguenti valori:

      - *credential_accepted*: quando l'Attestato ELettronico è stato memorizzato con successo nell'Istanza del Wallet.
      - *credential_deleted*: quando l'emissione non riuscita dell'Attestato Elettronico è stata causata da un'azione dell'utente.
      - *credential_failure*: in tutti gli altri casi di insuccesso.

    - Sezione 10.1 di [`OpenID4VCI`_].
  * - **event_description**
    - OPZIONALE. Testo ASCII *human-readable* [USASCII] che fornisce informazioni aggiuntive, da utilizzare per informare in merito all'evento verificatosi. I valori per il parametro event_description NON DEVONO includere caratteri al di fuori dell'insieme *%x20-21 / %x23-5B / %x5D-7E*.
    - Sezione 10.1 di [`OpenID4VCI`_].

Notification Response
.....................

La Notification Response DEVE utilizzare un *status code HTTP 204 (No Content)*, come raccomandato nella Sezione 10.2 di [`OpenID4VCI`_].

In caso di errori, si DEVE seguire quanto descritto nella Sezione 10.3 di [`OpenID4VCI`_].

Nel caso in cui la Notification Request non contenga un Access Token valido, il Notification Endpoint restituisce una response di errore come definito nella Sezione 3 del [:rfc:`6750`].
Se si verifica qualsiasi altro errore, il Credential Issuer DEVE restituire una response di errore come definito nella Sezione 10.3 di [`OpenID4VCI`_]. La response DEVE utilizzare il content type *application/json* e DEVE includere i seguenti parametri:

  - *error*. Il codice di errore.
  - *error_description*. Testo in forma *human-readable* che fornisce ulteriori dettagli per chiarire la natura dell'errore riscontrato.

Di seguito è riportato un esempio non normativo di una response di errore.

.. code:: http

  HTTP/1.1 400 Bad Request
  Content-Type: application/json
  Cache-Control: no-store

.. literalinclude:: ../../examples/notification-error.json
  :language: JSON

Nella seguente tabella sono elencati i *Status Code HTTP* e i relativi codici di errore supportati per la response di errore:

.. list-table::
    :class: longtable
    :widths: 20 20 60
    :header-rows: 1

    * - **Codice di Stato**
      - **codice di errore**
      - **Descrizione**
    * - *400 Bad Request* [OBBLIGATORIO]
      - ``invalid_notification_id``
      - Il Credential Issuer non può soddisfare la richiesta a causa del parametro ``notification_id`` non valido. Sezione 10.3 di [`OpenID4VCI`_].
    * - *400 Bad Request* [OBBLIGATORIO]
      - ``invalid_notification_request``
      - Il Credential Issuer non può soddisfare la richiesta a causa di parametri mancanti, parametro non valido o richiesta malformata. Sezione 10.3 di [`OpenID4VCI`_].
    * - *500 Internal Server Error* [OBBLIGATORIO]
      - ``server_error``
      - Il Credential Issuer ha riscontrato un problema interno.
    * - *503 Service Unavailable* [OBBLIGATORIO]
      - ``temporarily_unavailable``
      - Il Credential Issuer è temporaneamente non disponibile.
    * - *504 Gateway Timeout* [OPZIONALE]
      - `-`
      - Il Credential Issuer non può soddisfare la richiesta entro l'intervallo di tempo definito.

.. include:: ../common/common_definitions.rst

Endpoint per l'Offerta di Credenziale
"""""""""""""""""""""""""""""""""""""

L'endpoint per l'Offerta di Credenziale di un Wallet è utilizzato dal Credential Issuer per interagire con l'Utente per avviare un'Emissione di Credenziale. DEVE essere utilizzato lo schema URL personalizzato ``openid-credential-offer://``.

Offerta di Credenziale
......................

L'Offerta di Credenziale effettuata dal Credential Issuer consiste in un singolo parametro di query URI ``credential_offer``. L'URL dell'Offerta di Credenziale PUÒ essere incluso in un Codice QR o in una pagina html con un pulsante href e DEVE contenere i seguenti parametri obbligatori:

.. _table_credential_offer_claim:
.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Claim**
    - **Descrizione**
    - **Riferimento**
  * - **credential_issuer**
    - DEVE essere impostato con un URL HTTPS che identifica in modo univoco il Credential Issuer. Il Wallet utilizza questo valore di parametro per ottenere i metadati del Credential Issuer.
    - Sezione 4.1.1 di [`OpenID4VCI`_].
  * - **credential_configuration_ids**
    - Array di Stringhe, ciascuna delle quali specifica un identificatore univoco della Credenziale descritta nella mappa ``credential_configurations_supported`` nei Metadati del Credential Issuer.
    - Sezione 4.1.1 di [`OpenID4VCI`_].
  * - **grants**
    - DEVE contenere un oggetto ``authorization_code`` con i seguenti parametri:

        - **issuer_state**: OBBLIGATORIO. Stringa opaca creata dal Credential Issuer utilizzata per collegare la successiva Richiesta di Autorizzazione con il Credential Issuer. Il Wallet DEVE includerla nella successiva Richiesta di Autorizzazione.
        - **authorization_server**: OBBLIGATORIO quando il Credential Issuer utilizza più di un server di autorizzazione nella sua Soluzione Issuer. Stringa che identifica il Server di Autorizzazione da utilizzare. Il valore DEVE corrispondere a uno dei valori mappati nell'array ``authorization_servers`` dei metadati del Credential Issuer. NON DEVE essere utilizzato se ``authorization_servers`` è assente o non ha più voci.
    - Sezione 4.1.1 di [`OpenID4VCI`_].


Risposta all'Offerta di Credenziale
...................................
Non è prevista alcuna risposta dal Wallet.


Endpoint per la Richiesta di Autorizzazione Spinta
""""""""""""""""""""""""""""""""""""""""""""""""""

Richiesta di Autorizzazione Spinta (PAR)
........................................

La richiesta all'endpoint di autorizzazione del Credential Issuer DEVE utilizzare parametri di intestazione HTTP e parametri HTTP POST.

Il metodo HTTP POST DEVE utilizzare i parametri nel corpo del messaggio codificati in formato ``application/x-www-form-urlencoded``.

.. _table_http_request_claim:
.. list-table:: Parametri della richiesta http PAR
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Descrizione**
      - **Riferimento**
    * - **client_id**
      - DEVE essere impostato sull'impronta digitale del valore ``jwk`` nel parametro ``cnf`` all'interno dell'Attestato di Wallet.
      - :rfc:`6749`
    * - **request**
      - DEVE essere un JWT firmato. La chiave privata corrispondente a quella pubblica nel parametro ``cnf`` all'interno dell'Attestato di Wallet DEVE essere utilizzata per firmare l'Oggetto Richiesta.
      - `OpenID Connect Core. Sezione 6 <https://openid.net/specs/openid-connect-core-1_0.html#JWTRequests>`_

L'Endpoint di Autorizzazione Spinta è protetto con l'Autenticazione Client basata su Attestato OAuth 2.0 [`OAUTH-ATTESTATION-CLIENT-AUTH`_], pertanto
la richiesta all'endpoint di autorizzazione del Credential Issuer DEVE utilizzare i seguenti parametri di intestazione HTTP:

.. _table_http_request_headers_claim:
.. list-table:: parametri di intestazione della richiesta http
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **OAuth-Client-Attestation**
      - DEVE essere impostato su un valore contenente il JWT dell'Attestato di Wallet.
      - `OAUTH-ATTESTATION-CLIENT-AUTH`_.
    * - **OAuth-Client-Attestation-PoP**
      - DEVE essere impostato su un valore contenente la Prova di Possesso del JWT dell'Attestato di Wallet.
      - `OAUTH-ATTESTATION-CLIENT-AUTH`_.


L'*Oggetto Richiesta* JWT ha i seguenti parametri di intestazione JOSE:

.. _table_request_object_claim:
.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Intestazione JOSE**
      - **Descrizione**
      - **Riferimento**
    * - **alg**
      - Un identificatore di algoritmo di firma digitale come da registro IANA "JSON Web Signature and Encryption Algorithms". DEVE essere uno degli algoritmi supportati elencati nella Sezione :ref:`algorithms:Algoritmi Crittografici` e NON DEVE essere impostato su ``none`` o qualsiasi identificatore di algoritmo simmetrico (MAC).
      - :rfc:`7516#section-4.1.1`.
    * - **kid**
      - Identificatore univoco del ``jwk`` all'interno del claim ``cnf`` dell'Attestato di Wallet come valore dell'Impronta JWK codificato in base64url.
      - :rfc:`7638#section_3`.

.. note::
  Il parametro **typ**, se omesso, assume il valore implicito **JWT**.


Il payload JWT ``request`` contenuto nel messaggio HTTP POST è fornito con i seguenti parametri:

.. _table_jwt_request:
.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Descrizione**
      - **Riferimento**
    * - **iss**
      - DEVE essere impostato sul ``client_id``.
      - :rfc:`9126` e :rfc:`7519`.
    * - **aud**
      - DEVE essere impostato sull'identificatore del Credential Issuer.
      - :rfc:`9126` e :rfc:`7519`.
    * - **exp**
      - Timestamp UNIX con il tempo di scadenza del JWT. Il valore del claim NON DEVE essere superiore a 300 secondi dal momento dell'emissione.
      - :rfc:`9126` e :rfc:`7519`.
    * - **iat**
      - Timestamp UNIX con il tempo di emissione del JWT.
      - :rfc:`9126` e :rfc:`7519`.
    * - **response_type**
      - DEVE essere impostato su ``code``.
      - :rfc:`6749`
    * - **response_mode**
      - DEVE essere una stringa che indica il "*response_mode*", come specificato in [`OAUTH-MULT-RESP-TYPE`_]. DEVE essere uno dei valori supportati (*response_modes_supported*) forniti nei metadati del Credential Issuer. Informa il Credential Issuer del meccanismo da utilizzare per restituire i parametri dall'Endpoint di Autorizzazione. In caso di *Risposta di Reindirizzamento HTTP 302* il valore DEVE essere *query*. In questa modalità, i parametri della Risposta di Autorizzazione sono codificati nella stringa di query aggiunta all'``redirect_uri`` durante il reindirizzamento all'Istanza del Wallet. In caso di *Risposta HTTP POST* il valore DEVE essere *form_post.jwt* secondo [`JARM`_]. In questa modalità, i parametri della Risposta di Autorizzazione sono specificati in un JWT codificato come valore di un modulo HTML che viene inviato automaticamente nell'user-agent, e quindi viene trasmesso tramite il metodo HTTP POST all'Istanza del Wallet, con i parametri risultanti codificati nel corpo utilizzando il formato *application/x-www-form-urlencoded*. L'attributo action del modulo DEVE essere l'URI di Reindirizzamento dell'Istanza del Wallet. Il metodo dell'attributo del modulo DEVE essere POST.
      - Vedi [`OAUTH-MULT-RESP-TYPE`_] e [`JARM`_].
    * - **client_id**
      - DEVE essere impostato come nella :ref:`Tabella dei parametri HTTP <table_http_request_claim>`.
      - Vedi :ref:`Tabella dei parametri HTTP <table_http_request_claim>`.
    * - **state**
      - Identificatore di sessione univoco lato client. Questo valore verrà restituito al client nella risposta, al termine dell'autenticazione. DEVE essere una stringa casuale composta da caratteri alfanumerici e con una lunghezza minima di 32 cifre. I caratteri speciali DEVONO essere considerati caratteri non alfanumerici come definito in `[NIST] <https://csrc.nist.gov/glossary/term/special_character>`__.
      - Vedi [`OIDC`_] Sezione 3.1.2.1.
    * - **code_challenge**
      - Una sfida derivata dal **code verifier** che viene inviata nella richiesta di autorizzazione.
      - :rfc:`7636#section-4.2`.
    * - **code_challenge_method**
      - Un metodo utilizzato per derivare **code challenge**. DEVE essere impostato su ``S256``.
      - :rfc:`7636#section-4.3`.
    * - **scope**
      - Stringa JSON. Stringa che specifica un identificatore univoco della Credenziale indipendentemente dal suo formato. DEVE essere mappato nel claim di metadati `credential_configurations_supported` del Credential Issuer. Il valore dell'identificatore univoco DEVE corrispondere al parametro `credential_type` del Catalogo degli Attestati Elettronici. Ad esempio, nel caso del PID, può essere impostato su ``PersonIdentificationData`` mentre nel caso della patente di guida mobile ``mDL``. Poiché PUÒ essere multivalore, quando ciò si verifica ogni valore DEVE essere separato da uno spazio.
      - :rfc:`6749`
    * - **authorization_details**
      - Array di Oggetti JSON. Ogni Oggetto JSON DEVE includere i seguenti claim:

            - **type**: DEVE essere impostato su ``openid_credential``,
            - **credential_configuration_id**: Stringa JSON. Stringa che specifica un identificatore univoco della Credenziale in un formato specifico che DEVE essere mappato nel claim di metadati `credential_configurations_supported` del Credential Issuer. Ad esempio, ``dc_sd_jwt_PersonIdentificationData`` può essere utilizzato per PID in formato SD-JWT VC, ``dc_sd_jwt_mDL`` per la patente di guida mobile in formato SD-JWT VC e ``mso_mdoc_mDL`` per la patente di guida mobile in formato mdoc.
      - Vedi [RAR :rfc:`9396`] e [`OpenID4VCI`_].
    * - **redirect_uri**
      - URI di reindirizzamento a cui è destinata la risposta. DEVE essere un link universale o un link app registrato con il sistema operativo locale, in modo che quest'ultimo fornirà la risposta all'Istanza del Wallet.
      - Vedi [`OIDC`_] Sezione 3.1.2.1.
    * - **jti**
      - Identificatore univoco del JWT che, insieme al valore contenuto nel claim ``iss``, impedisce il riutilizzo del JWT (attacco replay). Poiché il valore `jti` da solo non è resistente alle collisioni, DEVE essere identificato in modo univoco insieme al suo emittente.
      - [:rfc:`7519`].
    * - **issuer_state**
      - DEVE essere presente solo in caso di flusso avviato dall'emittente. DEVE contenere lo stesso valore contenuto nell'Offerta di Credenziale.
      - [:rfc:`7519`].

.. note::
  Se la richiesta contiene il valore scope e il parametro *authorization_details*, il Credential Issuer DEVE interpretarli individualmente. Tuttavia, se entrambi richiedono lo stesso tipo di Credenziale, il Credential Issuer DEVE seguire la richiesta come indicato dall'oggetto authorization details.

L'intestazione JOSE della prova di possesso dell'Attestato di Wallet, contenuta nelle intestazioni della Richiesta HTTP, DEVE contenere:

.. _table_jwt_pop:
.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Intestazione JOSE**
      - **Descrizione**
      - **Riferimento**
    * - **alg**
      - Un identificatore di algoritmo di firma digitale come da registro IANA "JSON Web Signature and Encryption Algorithms". DEVE essere uno degli algoritmi supportati elencati nella Sezione :ref:`algorithms:Algoritmi Crittografici` e NON DEVE essere impostato su ``none`` o qualsiasi identificatore di algoritmo simmetrico (MAC).
      - :rfc:`7516#section-4.1.1`.

Il corpo della prova di possesso dell'Attestato di Wallet JWT, contenuto nelle intestazioni della Richiesta HTTP, DEVE contenere:

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Descrizione**
      - **Riferimento**
    * - **iss**
      - Impronta digitale del JWK nel parametro ``cnf``.
      - :rfc:`9126` e :rfc:`7519`.
    * - **aud**
      - DEVE essere impostato sull'identificatore del Credential Issuer.
      - :rfc:`9126` e :rfc:`7519`.
    * - **exp**
      - Timestamp UNIX con il tempo di scadenza del JWT.
      - :rfc:`9126` e :rfc:`7519`.
    * - **iat**
      - Timestamp UNIX con il tempo di emissione del JWT.
      - :rfc:`9126` e :rfc:`7519`.
    * - **jti**
      - Identificatore univoco per il JWT di prova DPoP. Il valore DOVREBBE essere impostato utilizzando un valore *UUID v4* secondo [:rfc:`4122`].
      - [:rfc:`7519`. Sezione 4.1.7].

Risposta alla Richiesta di Autorizzazione Spinta (PAR)
......................................................

Se la verifica ha esito positivo, il Credential Issuer DEVE fornire la risposta con un *codice di stato HTTP 201*. I seguenti parametri sono inclusi come membri di primo livello nel corpo del messaggio di risposta HTTP, utilizzando il tipo di media ``application/json`` come definito in [:rfc:`8259`].

.. _table_http_response_claim:
.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Descrizione**
      - **Riferimento**
    * - **request_uri**
      - L'URI di richiesta corrispondente alla richiesta di autorizzazione inviata. Questo URI DEVE essere un riferimento monouso alla rispettiva richiesta di autorizzazione. DEVE contenere alcune parti generate utilizzando un algoritmo pseudocasuale crittograficamente forte. Il formato del valore DEVE essere ``urn:ietf:params:oauth:request_uri:<reference-value>`` con ``<reference-value>`` come parte casuale dell'URI che fa riferimento ai rispettivi dati della richiesta di autorizzazione.
      - [:rfc:`9126`].
    * - **expires_in**
      - Un numero JSON che rappresenta la durata dell'URI di richiesta in secondi come numero intero positivo.
      - [:rfc:`9126`].

Se si verificano errori durante la Richiesta PAR, il Server di Autorizzazione DEVE restituire una risposta di errore come definito in :rfc:`9126#section-2.3`. La risposta DEVE utilizzare *application/json* come tipo di contenuto e DEVE includere i seguenti parametri:

  - *error*. Il codice di errore.
  - *error_description*. Testo in forma leggibile dall'uomo che fornisce ulteriori dettagli per chiarire la natura dell'errore riscontrato.

Di seguito è riportato un esempio non normativo di una risposta di errore.

.. code:: http

  HTTP/1.1 400 Bad Request
  Content-Type: application/json

.. literalinclude:: ../../examples/par-error.json
  :language: JSON

Nella seguente tabella sono elencati i Codici di Stato HTTP e i relativi codici di errore supportati per la risposta di errore:

.. list-table::
    :class: longtable
    :widths: 20 20 60
    :header-rows: 1

    * - **Codice di Stato**
      - **codice di errore**
      - **Descrizione**
    * - *400 Bad Request* [OBBLIGATORIO]
      - ``invalid_request``
      - Il Credential Issuer non può soddisfare la richiesta a causa di parametri mancanti, parametri non validi o richiesta malformata. (:rfc:`6749#section-5.2`).
    * - *400 Bad Request* [OBBLIGATORIO]
      - ``invalid_scope``
      - Il Credential Issuer non può soddisfare la richiesta perché lo scope richiesto non è valido o è sconosciuto. (:rfc:`6749#section-5.2`).
    * - *401 Unauthorized* [OBBLIGATORIO]
      - ``invalid_client``
      - Il Credential Issuer non può soddisfare la richiesta a causa del fallimento dell'Autenticazione Client (ad esempio in caso di client sconosciuto, nessun parametro di Autenticazione Client incluso o metodo di autenticazione non supportato). (:rfc:`6749#section-5.2`).
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



Endpoint di autorizzazione
""""""""""""""""""""""""""

L'endpoint di autorizzazione viene utilizzato per interagire con il Credential Issuer e ottenere una concessione di autorizzazione.
Il server di autorizzazione DEVE prima verificare l'identità dell'Utente proprietario della Credenziale.


Richiesta di Autorizzazione
...........................

La richiesta di Autorizzazione viene emessa dal Browser Web in uso dall'Istanza del Wallet, vengono utilizzati i metodi HTTP **POST** o **GET**. Quando viene utilizzato il metodo **POST**, i parametri DEVONO essere inviati utilizzando la *Serializzazione del Modulo*. Quando viene utilizzato il metodo **GET**, i parametri DEVONO essere inviati utilizzando la *Serializzazione della Stringa di Query*. Per maggiori dettagli vedere la Sezione 13 di [`OIDC`_].

I parametri obbligatori nella richiesta di autenticazione HTTP sono specificati nella seguente tabella.

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Descrizione**
      - **Riferimento**
    * - **client_id**
      - DEVE essere impostato come nella :ref:`Tabella dei parametri HTTP <table_http_request_claim>`.
      - Vedi :ref:`Tabella dei parametri HTTP <table_http_request_claim>`.
    * - **request_uri**
      - DEVE essere impostato sullo stesso valore ottenuto dalla Risposta PAR. Vedi :ref:`Tabella dei parametri della Risposta HTTP PAR <table_http_response_claim>`.
      - [:rfc:`9126`].

Risposta di Autorizzazione
..........................

La risposta di autenticazione viene restituita dall'endpoint di autorizzazione del Credential Issuer al termine del flusso di autenticazione.

Se l'autenticazione ha esito positivo, il Credential Issuer reindirizza l'Utente aggiungendo i seguenti parametri di query come richiesto all'*redirect_uri*. L'URI di reindirizzamento DEVE essere un link universale o un link app registrato con il sistema operativo locale, in modo che quest'ultimo sia in grado di fornire la risposta all'Istanza del Wallet.

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Descrizione**
      - **Riferimento**
    * - **code**
      - *Codice di Autorizzazione* univoco che l'Istanza del Wallet invia all'Endpoint Token.
      - [:rfc:`6749#section-4.1.2`], [:rfc:`7521`].
    * - **state**
      - L'Istanza del Wallet DEVE verificare la corrispondenza con il valore del parametro ``state`` nell'Oggetto Richiesta. È definito come nella :ref:`Tabella dei parametri della Richiesta JWT <table_jwt_request>`.
      - [:rfc:`6749#section-4.1.2`].
    * - **iss**
      - Identificatore univoco del Credential Issuer che ha creato la Risposta di Autenticazione. L'Istanza del Wallet DEVE convalidare questo parametro.
      - [:rfc:`9207`], [:rfc:`7519`, Sezione 4.1.1.].

Se si verificano errori durante la Richiesta di Autorizzazione, il Server di Autorizzazione DEVE restituire una risposta di errore come definito in :rfc:`6749#section-4.1.2.1`.
In caso di ``redirect_uri`` o ``client_id`` non valido/mancante, il Server di Autorizzazione DEVE informare l'Utente con l'errore e NON DEVE reindirizzare l'Utente all'URI di reindirizzamento.
Se si verifica qualsiasi altro errore, il Server di Autorizzazione DEVE reindirizzare l'Utente aggiungendo i seguenti parametri di query come richiesto all'*redirect_uri* utilizzando il formato *application/x-www-form-urlencoded*:

  - *error*. Il codice di errore.
  - *error_description*. Testo in forma leggibile dall'uomo che fornisce ulteriori dettagli per chiarire la natura dell'errore riscontrato.
  - *state*. Il valore esatto del parametro ``state`` contenuto nell'Oggetto Richiesta.

Di seguito è riportato un esempio non normativo di una risposta di errore.

.. code:: http

  HTTP/1.1 302 Found
  Location: https://client.example.com/cb?
   error=invalid_request
   &error_description=Unsupported%20response_type%20value
   &state=fyZiOL9Lf2CeKuNT2JzxiLRDink0uPcd

Nel caso in cui il Server di Autorizzazione reindirizza l'Utente all'*redirect_uri* DEVE essere utilizzato il codice di stato HTTP *302 (Found)*. I seguenti codici di errore sono supportati per la risposta di errore:

.. list-table::
    :class: longtable
    :widths: 20 20 60
    :header-rows: 1

    * - **Codice di Stato**
      - **codice di errore**
      - **Descrizione**
    * - *302 Found* [OBBLIGATORIO]
      - ``invalid_request``
      - Il Credential Issuer non può soddisfare la richiesta a causa di parametri mancanti, parametri non validi o richiesta malformata. (:rfc:`6749#section-4.1.2.1`).
    * - *302 Found* [OBBLIGATORIO]
      - ``unauthorized_client``
      - Il Credential Issuer non può soddisfare la richiesta perché il client non è autorizzato a richiedere un codice di autorizzazione. (:rfc:`6749#section-4.1.2.1`).
    * - *302 Found* [OBBLIGATORIO]
      - ``server_error``
      - Il Credential Issuer ha riscontrato un problema interno. (:rfc:`6749#section-4.1.2.1`).
    * - *302 Found* [OBBLIGATORIO]
      - ``temporarily_unavailable``
      - Il Credential Issuer è temporaneamente non disponibile. (:rfc:`6749#section-4.1.2.1`).

Nel caso in cui il Server di Autorizzazione non reindirizza l'Utente all'*redirect_uri* i seguenti Codici di Stato HTTP sono supportati per la risposta di errore:

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


Endpoint token
""""""""""""""

L'endpoint token viene utilizzato dall'Istanza del Wallet per ottenere un Token di Accesso presentando una concessione di autorizzazione, come
definito in :rfc:`6749`. L'Endpoint Token è un endpoint protetto con un'autenticazione client basata sul modello definito in OAuth 2.0 Attestation-based Client Authentication [`OAUTH-ATTESTATION-CLIENT-AUTH`_ ].


Richiesta di Token
..................

La richiesta all'endpoint Token del Credential Issuer DEVE essere una richiesta HTTP con metodo POST, con il corpo del messaggio codificato in formato ``application/x-www-form-urlencoded``. L'Istanza del Wallet invia la richiesta all'endpoint Token con ``OAuth-Client-Attestation`` e ``OAuth-Client-Attestation-PoP`` come parametri di intestazione secondo `OAUTH-ATTESTATION-CLIENT-AUTH`_.

L'endpoint Token è protetto con *OAuth 2.0 Attestation-based Client Authentication* [`OAUTH-ATTESTATION-CLIENT-AUTH`_], pertanto
la richiesta all'endpoint di autorizzazione del Credential Issuer DEVE utilizzare i seguenti parametri di intestazione HTTP **OAuth-Client-Attestation** e **OAuth-Client-Attestation-PoP**
come definito in "Endpoint per la Richiesta di Autorizzazione Spinta (PAR)".

L'endpoint Token emette token DPoP, pertanto è RICHIESTO che la richiesta includa nella sua intestazione HTTP il parametro di prova DPoP.
Il Server di Autorizzazione DEVE convalidare la prova DPoP ricevuta all'endpoint Token, secondo la Sezione 4.3 di :rfc:`9449`. Ciò mitiga l'uso improprio di Token di Accesso/Token di Aggiornamento persi o rubati all'endpoint Credential/Token. Se la prova DPoP non è valida, l'endpoint Token restituisce una risposta di errore, secondo la Sezione 5.2 di [:rfc:`6749`] con ``invalid_dpop_proof`` come valore del parametro di errore.

La richiesta di token contiene i seguenti claim:

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Descrizione**
      - **Riferimento**
    * - **grant_type**
      - OBBLIGATORIO. DEVE essere impostato su ``authorization_code`` o ``refresh_token``.
      - [:rfc:`6749`].
    * - **code**
      - OBBLIGATORIO solo se il tipo di concessione è ``authorization_code``. Codice di autorizzazione restituito nella Risposta di Autenticazione. NON DEVE essere presente se il tipo di concessione è ``refresh_token``.
      - [:rfc:`6749`].
    * - **redirect_uri**
      - OBBLIGATORIO solo se il tipo di concessione è ``authorization_code``. DEVE essere impostato come nell'Oggetto Richiesta :ref:`Tabella dei parametri della Richiesta JWT <table_jwt_request>`. NON DEVE essere presente se il tipo di concessione è ``refresh_token``.
      - [:rfc:`67491`].
    * - **code_verifier**
      - OBBLIGATORIO solo se il tipo di concessione è ``authorization_code``. Codice di verifica del **code_challenge**.
      - `Proof Key for Code Exchange by OAuth Public Clients <https://datatracker.ietf.org/doc/html/rfc7636>`_. NON DEVE essere presente se il tipo di concessione è ``refresh_token``.
    * - **refresh_token**
      - OBBLIGATORIO solo se il tipo di concessione è ``refresh_token``. Il Token di Aggiornamento precedentemente emesso all'Istanza del Wallet. NON DEVE essere presente se il tipo di concessione è ``authorization_code``.
      - [:rfc:`6749`].
    * - **scope**
      - OPZIONALE solo se il tipo di concessione è ``refresh_token``. Lo scope richiesto NON DEVE includere alcuno scope non originariamente concesso dall'Utente, e se omesso viene trattato come uguale allo scope originariamente concesso dall'Utente. NON DEVE essere presente se il tipo di concessione è ``authorization_code``.
      - [:rfc:`6749`].


Un **JWT di Prova DPoP** è incluso nella richiesta HTTP utilizzando il parametro di intestazione ``DPoP`` contenente un JWT DPoP.

L'intestazione JOSE di un **JWT DPoP** DEVE contenere almeno i seguenti parametri:

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Intestazione JOSE**
      - **Descrizione**
      - **Riferimento**
    * - **typ**
      - DEVE essere uguale a ``dpop+jwt``.
      - [:rfc:`7515`] e [:rfc:`8725`. Sezione 3.11].
    * - **alg**
      - Un identificatore di algoritmo di firma digitale come da registro IANA "JSON Web Signature and Encryption Algorithms". DEVE essere uno degli algoritmi supportati nella Sezione :ref:`algorithms:Algoritmi Crittografici` e NON DEVE essere impostato su ``none`` o con un identificatore di algoritmo simmetrico (MAC).
      - [:rfc:`7515`].
    * - **jwk**
      - Rappresenta la chiave pubblica scelta dall'Istanza del Wallet, in formato JSON Web Key (JWK) [:rfc:`7517`] a cui il Token di Accesso DEVE essere vincolato, come definito nella Sezione 4.1.3 di [:rfc:`7515`]. NON DEVE contenere una chiave privata.
      - [:rfc:`7517`] e [:rfc:`7515`].


Il payload di una **Prova JWT DPoP** DEVE contenere i seguenti claim:

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Descrizione**
      - **Riferimento**
    * - **jti**
      - Identificatore univoco per il JWT di prova DPoP. Il valore DOVREBBE essere impostato utilizzando un valore *UUID v4* secondo [:rfc:`4122`].
      - [:rfc:`7519`. Sezione 4.1.7].
    * - **htm**
      - Il valore del metodo HTTP della richiesta a cui è allegato il JWT.
      - [:rfc:`9110`. Sezione 9.1].
    * - **htu**
      - L'URI di destinazione HTTP, senza parti di query e frammento, della richiesta a cui è allegato il JWT.
      - [:rfc:`9110`. Sezione 7.1].
    * - **iat**
      - Timestamp UNIX con il tempo di emissione del JWT, codificato come NumericDate come indicato in :rfc:`7519`.
      - [:rfc:`7519`. Sezione 4.1.6].


Risposta di Token
.................

Se la Richiesta di Token viene convalidata con successo, il Server di Autorizzazione fornisce una Risposta di Token HTTP con un codice di stato *200 (OK)*. La Risposta di Token contiene i seguenti claim.

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Descrizione**
      - **Riferimento**
    * - **access_token**
      - OBBLIGATORIO. Il *Token di Accesso vincolato a DPoP*, in formato JWT firmato, consente di accedere all'Endpoint Credential per ottenere la Credenziale.
      - [:rfc:`6749`].
    * - **refresh_token**
      - OPZIONALE. Il *Token di Aggiornamento vincolato a DPoP*, in formato JWT firmato, che può essere utilizzato per ottenere un nuovo Token di Accesso all'Endpoint Token del Credential Issuer.
      - [:rfc:`6749`].
    * - **token_type**
      - OBBLIGATORIO. Tipo di *Token di Accesso* restituito. DEVE essere uguale a ``DPoP``.
      - [:rfc:`6749`].
    * - **expires_in**
      - OBBLIGATORIO. Tempo di scadenza del *Token di Accesso* in secondi.
      - [:rfc:`6749`].
    * - **authorization_details**
      - OBBLIGATORIO quando il parametro ``authorization_details`` viene utilizzato per richiedere l'emissione di una Credenziale. OPZIONALE quando il parametro ``scope`` viene utilizzato per richiedere l'emissione di una Credenziale. Array di Oggetti JSON, utilizzati per identificare Credenziali con gli stessi metadati ma diversi valori di claimset/claim e/o semplificare la richiesta di Credenziale anche quando viene emessa una sola Credenziale. Oltre al claim definito nella :ref:`Tabella dei parametri della Richiesta JWT <table_jwt_request>` DEVE includere il seguente claim:

            - **credential_identifiers**: Array di stringhe, ciascuna che identifica in modo univoco un set di dati di Credenziale disponibile per l'emissione.
      - [`OpenID4VCI`_].

Se si verificano errori durante la convalida della Richiesta di Token, il Server di Autorizzazione DEVE restituire una risposta di errore come definito in :rfc:`6749#section-5.2`. La risposta DEVE utilizzare il Content-Type HTTP impostato su *application/json* e DEVE includere i seguenti parametri:

  - *error*. Il codice di errore.
  - *error_description*. Testo in forma leggibile dall'uomo che fornisce ulteriori dettagli per chiarire la natura dell'errore riscontrato.

Di seguito è riportato un esempio non normativo di una risposta di errore.

.. code:: http

  HTTP/1.1 401 Unauthorized
  Content-Type: application/json;charset=UTF-8
  Cache-Control: no-store
  Pragma: no-cache

.. literalinclude:: ../../examples/token-error.json
  :language: JSON

Nella seguente tabella sono elencati i Codici di Stato HTTP e i relativi codici di errore supportati per la risposta di errore:

.. list-table::
    :class: longtable
    :widths: 20 20 60
    :header-rows: 1

    * - **Codice di Stato**
      - **codice di errore**
      - **Descrizione**
    * - *400 Bad Request* [OBBLIGATORIO]
      - ``invalid_request``
      - Il Credential Issuer non può soddisfare la richiesta a causa di parametri mancanti, parametri non validi o richiesta malformata. (:rfc:`6749#section-5.2`).
    * - *400 Bad Request* [OBBLIGATORIO]
      - ``invalid_grant``
      - Il Credential Issuer non può soddisfare la richiesta perché il codice di autorizzazione fornito o il Token di Aggiornamento non è valido, è scaduto, è stato revocato o non corrisponde all'URI di reindirizzamento utilizzato nella richiesta di autorizzazione, o è stato emesso a un altro client. (:rfc:`6749#section-5.2`).
    * - *400 Bad Request* [OBBLIGATORIO]
      - ``unsupported_grant_type``
      - Il Credential Issuer non può soddisfare la richiesta perché il tipo di concessione di autorizzazione non è supportato. (:rfc:`6749#section-5.2`).
    * - *400 Bad Request* [OBBLIGATORIO]
      - ``invalid_dpop_proof``
      - Il Credential Issuer non può soddisfare la richiesta a causa di *prova DPoP* non valida. Sezione 5 di [:rfc:`9449`].
    * - *401 Unauthorized* [OBBLIGATORIO]
      - ``invalid_client``
      - Il Credential Issuer non può soddisfare la richiesta a causa di parametri non validi, l'Autenticazione Client è fallita (ad esempio in caso di client sconosciuto, nessun parametro di Autenticazione Client incluso o metodo di autenticazione non supportato). (:rfc:`6749#section-5.2`).
    * - *500 Internal Server Error* [OBBLIGATORIO]
      - ``server_error``
      - Il Credential Issuer ha riscontrato un problema interno.
    * - *503 Service Unavailable* [OBBLIGATORIO]
      - ``temporarily_unavailable``
      - Il Credential Issuer è temporaneamente non disponibile.
    * - *504 Gateway Timeout* [OPZIONALE]
      - `-`
      - Il Credential Issuer non può soddisfare la richiesta entro l'intervallo di tempo definito.

Token di Accesso
................

Un Token di Accesso vincolato a DPoP viene fornito dall'endpoint Token del Credential Issuer come risultato di una richiesta di token riuscita. Il Token di Accesso è codificato in formato JWT, secondo [:rfc:`7519`]. Il Token di Accesso DEVE avere almeno i seguenti claim obbligatori e DEVE essere vincolato alla chiave pubblica fornita dalla prova DPoP. Questo vincolo può essere realizzato in base alla metodologia definita nella Sezione 6 di (:rfc:`9449`).

Il **JWT DPoP** contiene i seguenti parametri di intestazione JOSE e claim.

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Intestazione JOSE**
      - **Descrizione**
      - **Riferimento**
    * - **typ**
      - OBBLIGATORIO. DEVE essere uguale a ``at+jwt``.
      - [:rfc:`7515`].
    * - **alg**
      - OBBLIGATORIO. Un identificatore di algoritmo di firma digitale come da registro IANA "JSON Web Signature and Encryption Algorithms". DEVE essere uno degli algoritmi supportati nella Sezione :ref:`Cryptographic Algorithms <algorithms:Algoritmi Crittografici>` e NON DEVE essere impostato su ``none`` o con un identificatore di algoritmo simmetrico (MAC).
      - [:rfc:`7515`].
    * - **kid**
      - OBBLIGATORIO. Identificatore univoco del ``jwk`` utilizzato dal Credential Issuer per firmare il Token di Accesso.
      - :rfc:`7638#section_3`.


.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Claim**
    - **Descrizione**
    - **Riferimento**
  * - **iss**
    - OBBLIGATORIO. DEVE essere un URL HTTPS che identifica in modo univoco il Credential Issuer. L'Istanza del Wallet DEVE verificare che questo valore corrisponda al Credential Issuer a cui ha richiesto la Credenziale.
    - [:rfc:`9068`], [:rfc:`7519`].
  * - **sub**
    - OBBLIGATORIO. Identifica il soggetto del JWT. DEVE essere impostato sul valore del campo ``sub`` nella Credenziale SD-JWT-VC.
    - [:rfc:`9068`], [:rfc:`7519`] e Sezione 8 di [`OIDC`_].
  * - **client_id**
    - OBBLIGATORIO. L'identificatore per l'Istanza del Wallet che ha richiesto il Token di Accesso; DEVE essere uguale al kid della chiave pubblica dell'Istanza del Wallet specificata nell'Attestato di Wallet (``cnf.jwk``).
    - [:rfc:`9068`], [:rfc:`7519`] e Sezione 8 di [`OIDC`_].
  * - **aud**
    - OBBLIGATORIO. DEVE essere impostato sull'identificatore del Credential Issuer.
    - [:rfc:`9068`].
  * - **iat**
    - OBBLIGATORIO. Timestamp UNIX con il tempo di emissione del JWT, codificato come NumericDate come indicato in :rfc:`7519`.
    - [:rfc:`9068`], [:rfc:`7519`. Sezione 4.1.6].
  * - **exp**
    - OBBLIGATORIO. Timestamp UNIX con il tempo di scadenza del JWT, codificato come NumericDate come indicato in :rfc:`7519`.
    - [:rfc:`9068`], [:rfc:`7519`].
  * - **jti**
    - OPZIONALE. DEVE essere una Stringa in formato *uuid4*. Identificatore univoco del Token ID che la RP DOVREBBE utilizzare per prevenire il riutilizzo rifiutando l'ID Token se già elaborato.
    - [:rfc:`9068`], [:rfc:`7519`].
  * - **cnf**
    - OBBLIGATORIO. DEVE contenere un claim **jkt** che è un Metodo di Conferma dell'Impronta SHA-256 JWK. Il valore del membro *jkt* DEVE essere la codifica base64url (come definito in [:rfc:`7515`]) dell'Impronta SHA-256 JWK della chiave pubblica DPoP (in formato JWK) a cui è vincolato il Token di Accesso.
    - [:rfc:`9449`. Sezione 6.1] e [:rfc:`7638`].

Token di Aggiornamento
......................

Un *Token di Aggiornamento vincolato a DPoP* viene fornito dall'endpoint Token del Credential Issuer come risultato di una richiesta di token riuscita. Il Token di Aggiornamento è codificato in formato JWT, secondo [:rfc:`7519`]. Il Token di Aggiornamento DEVE avere almeno i seguenti claim obbligatori e DEVE essere vincolato alla chiave pubblica fornita dalla prova DPoP. Questo vincolo può essere realizzato in base alla metodologia definita nella Sezione 6 di (:rfc:`9449`).

Il **JWT DPoP** DEVE contenere i seguenti parametri di intestazione JOSE e claim.

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Intestazione JOSE**
      - **Descrizione**
      - **Riferimento**
    * - **typ**
      - DEVE essere uguale a ``rt+jwt``.
      - [:rfc:`7515`].
    * - **alg**
      - Un identificatore di algoritmo di firma digitale come da registro IANA "JSON Web Signature and Encryption Algorithms". DEVE essere uno degli algoritmi supportati nella Sezione :ref:`algorithms:Algoritmi Crittografici` e NON DEVE essere impostato su ``none`` o con un identificatore di algoritmo simmetrico (MAC).
      - [:rfc:`7515`].
    * - **kid**
      - Identificatore univoco del ``jwk`` utilizzato dal Credential Issuer per firmare il Token di Accesso.
      - :rfc:`7638#section_3`.


.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Claim**
    - **Descrizione**
    - **Riferimento**
  * - **iss**
    - DEVE essere un URL HTTPS che identifica in modo univoco il Credential Issuer. L'Istanza del Wallet DEVE verificare che questo valore corrisponda al Credential Issuer a cui ha richiesto la Credenziale.
    - [:rfc:`9068`], [:rfc:`7519`].
  * - **sub**
    - Identifica il soggetto del JWT. DEVE essere impostato sul valore del campo ``sub`` nella Credenziale SD-JWT-VC.
    - [:rfc:`9068`], [:rfc:`7519`] e Sezione 8 di [`OIDC`_].
  * - **client_id**
    - L'identificatore per l'Istanza del Wallet che ha richiesto il Token di Accesso; DEVE essere uguale al valore `kid` che identifica la chiave pubblica utilizzata nell'Istanza del Wallet, utilizzata nell'Attestato di Wallet (``cnf.jwk``).
    - [:rfc:`9068`], [:rfc:`7519`] e Sezione 8 di [`OIDC`_].
  * - **aud**
    - DEVE essere impostato sull'identificatore del Credential Issuer.
    - [:rfc:`9068`].
  * - **iat**
    - Timestamp UNIX con il tempo di emissione del JWT, codificato come NumericDate come indicato in :rfc:`7519`.
    - [:rfc:`9068`], [:rfc:`7519`. Sezione 4.1.6].
  * - **nbf**
    - Timestamp UNIX con il tempo prima del quale il JWT NON DEVE essere accettato per l'elaborazione, codificato come NumericDate come indicato in :rfc:`7519`. DOVREBBE essere impostato sul claim ``exp`` del corrispondente Token di Accesso.
    - [:rfc:`7519`. Sezione 4.1.7].
  * - **exp**
    - Timestamp UNIX con il tempo di scadenza del JWT, codificato come NumericDate come indicato in :rfc:`7519`.
    - [:rfc:`9068`], [:rfc:`7519`].
  * - **jti**
    - DEVE essere una Stringa in formato *uuid4*. Identificatore univoco del Token ID che la RP DOVREBBE utilizzare per prevenire il riutilizzo rifiutando l'ID Token se già elaborato.
    - [:rfc:`9068`], [:rfc:`7519`].
  * - **cnf**
    - DEVE contenere un claim **jkt** che è un Metodo di Conferma dell'Impronta SHA-256 JWK. Il valore del membro *jkt* DEVE essere la codifica base64url (come definito in [:rfc:`7515`]) dell'Impronta SHA-256 JWK della chiave pubblica DPoP (in formato JWK) a cui è vincolato il Token di Accesso.
    - [:rfc:`9449`. Sezione 6.1] e [:rfc:`7638`].

Endpoint Nonce
""""""""""""""

L'Endpoint Nonce fornisce un valore ``c_nonce`` utile per creare una prova di possesso del materiale chiave per la richiesta all'Endpoint Credential, come definito nella Sezione 7 di `OpenID4VCI`_.

Richiesta di Nonce
..................

La richiesta di un nonce DEVE essere una richiesta HTTP POST senza corpo indirizzata all'Endpoint Nonce del Credential Issuer mappato nei Metadati del Credential Issuer.


Risposta di Nonce
.................

La Risposta di Nonce all'Istanza del Wallet DEVE essere inviata utilizzando il tipo di media `application/json`. In caso di Richiesta di Nonce riuscita, il Credential Issuer DEVE restituire una risposta HTTP con un codice di stato *200 (OK)*.

Come definito nella Sezione 7.2 di `OpenID4VCI`_, il Credential Issuer DEVE rendere la risposta non memorizzabile nella cache aggiungendo un campo di intestazione ``Cache-Control`` valorizzato con *no-store*.

La Risposta di Nonce contiene il seguente parametro:

.. list-table::
  :widths: 20 60 20
  :header-rows: 1

  * - **Claim**
    - **Descrizione**
    - **Riferimento**
  * - **c_nonce**
    - OBBLIGATORIO. Stringa contenente il valore del nonce. Questo valore DEVE essere imprevedibile.
    - Sezione 7.2 di [`OpenID4VCI`_].

Endpoint credential
"""""""""""""""""""

L'Endpoint Credential emette una Credenziale alla presentazione di un Token di Accesso valido, come definito in `OpenID4VCI`_.


Richiesta di Credenziale
........................

L'Istanza del Wallet quando richiede l'Attestato Elettronico all'endpoint Credential, DEVE utilizzare i seguenti parametri nel corpo del messaggio della richiesta HTTP POST, utilizzando il tipo di media `application/json`.

L'endpoint Credential DEVE accettare e convalidare la *prova DPoP* inviata nel parametro di intestazione HTTP DPoP, secondo i passaggi definiti nella Sezione 4.3 di (:rfc:`9449`). La *prova DPoP* oltre ai valori definiti nella sezione Endpoint Token DEVE contenere il seguente claim:

  - **ath**: valore hash del Token di Accesso codificato in ASCII. Il valore DEVE utilizzare la codifica base64url (come definito nella Sezione 2 di :rfc:`7515`) con l'algoritmo SHA-256.

.. warning::
  L'Istanza del Wallet DEVE creare una **nuova prova DPoP** per la richiesta di Credenziale e NON DEVE utilizzare la prova precedentemente creata per l'Endpoint Token.


.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Claim**
    - **Descrizione**
    - **Riferimento**
  * - **credential_identifier**
    - OBBLIGATORIO quando un Authorization Details di tipo *openid_credential* è stato restituito dalla Risposta Token. NON DEVE essere utilizzato altrimenti. Questo DEVE essere impostato con uno dei valori ottenuti nel claim ``credential_identifiers`` della Risposta Token. NON DEVE essere utilizzato se è presente ``credential_configuration_id``.
    - Sezione 8.2 di [`OpenID4VCI`_].
  * - **credential_configuration_id**
    - OBBLIGATORIO se il parametro ``credential_identifiers`` è assente nella Risposta Token. NON DEVE essere utilizzato altrimenti. Stringa che specifica un identificatore univoco della Credenziale descritta nella mappa `credential_configurations_supported` nei Metadati del Credential Issuer. Ad esempio, nel caso del PID, può essere impostato su ``PersonIdentificationData``.
    - Sezione 8.2 di [`OpenID4VCI`_].
  * - **proof**
    - OBBLIGATORIO. Oggetto JSON contenente la prova di possesso del materiale chiave a cui sarà vincolata la Credenziale emessa. L'oggetto proof DEVE contenere i seguenti claim obbligatori:

      - **proof_type**: stringa JSON che denota il tipo di prova. DEVE essere `jwt`.
      - **jwt**: il JWT utilizzato come prova di possesso.
    - [`OpenID4VCI`_].
  * - **transaction_id**
    - OBBLIGATORIO solo in caso di flusso differito. Stringa che identifica una transazione di emissione differita. NON DEVE essere presente nel flusso immediato
    - Sezione 9.1 di [`OpenID4VCI`_].


Il tipo di prova JWT DEVE contenere i seguenti parametri per l'intestazione JOSE e il corpo JWT:

.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Intestazione JOSE**
    - **Descrizione**
    - **Riferimento**
  * - **alg**
    - Un identificatore di algoritmo di firma digitale come da registro IANA "JSON Web Signature and Encryption Algorithms". DEVE essere uno degli algoritmi supportati nella Sezione :ref:`algorithms:Algoritmi Crittografici` e NON DEVE essere impostato su ``none`` o su un identificatore di algoritmo simmetrico (MAC).
    - [`OpenID4VCI`_], [:rfc:`7515`], [:rfc:`7517`].
  * - **typ**
    - DEVE essere impostato su `openid4vci-proof+jwt`.
    - [`OpenID4VCI`_], [:rfc:`7515`], [:rfc:`7517`].
  * - **jwk**
    - Rappresenta la chiave pubblica scelta dall'Istanza del Wallet, in formato JSON Web Key (JWK) [:rfc:`7517`] a cui l'Attestato Elettronico sarà vincolato, come definito nella Sezione 4.1.3 di [:rfc:`7515`].
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
    - DEVE essere impostato sull'identificatore del Credential Issuer.
    - [`OpenID4VCI`_].
  * - **iat**
    - Timestamp UNIX con il tempo di emissione del JWT, codificato come NumericDate come indicato in :rfc:`7519`.
    - [`OpenID4VCI`_], [:rfc:`7519`. Sezione 4.1.6].
  * - **nonce**
    - Il tipo di valore di questo claim DEVE essere una stringa, dove il valore è un **c_nonce** fornito dal Credential Issuer nella Risposta di Nonce.
    - [`OpenID4VCI`_].


Risposta di Credenziale
.......................

La Risposta di Credenziale all'Istanza del Wallet DEVE essere inviata utilizzando il tipo di media `application/json`. Se la Richiesta di Credenziale viene convalidata con successo e la Credenziale è immediatamente disponibile, il Credential Issuer DEVE restituire una risposta HTTP con un codice di stato *200 (OK)*. Se la Credenziale non è disponibile e il flusso differito è supportato dal Credential Issuer, DEVE essere restituito un codice di stato HTTP *202*.

La Risposta di Credenziale contiene i seguenti parametri:

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

          - **credential**: OBBLIGATORIO. Stringa contenente un Attestato Elettronico emesso. Se l'identificatore di formato richiesto è ``dc+sd-jwt`` allora il parametro ``credential`` NON DEVE essere ricodificato. Se l'identificatore di formato richiesto è ``mso_mdoc`` allora il parametro ``credential`` DEVE essere una rappresentazione codificata in base64url della struttura IssuerSigned codificata in CBOR, come definito in [ISO 18013-5]. Questa struttura DOVREBBE contenere tutti i Namespaces e IssuerSignedItems inclusi negli AuthorizedNamespaces del MobileSecurityObject.
    - Sezione 8.3, Allegato A2.4 e Allegato A3.4 di [`OpenID4VCI`_].
  * - **lead_time**
    - OBBLIGATORIO se ``credentials`` non è presente, altrimenti NON DEVE essere presente. La quantità di tempo (in secondi) richiesta prima di effettuare una Richiesta di Credenziale Differita.
    - Questa Specifica.
  * - **notification_id**
    - OPZIONALE. Stringa che identifica una Credenziale emessa che il Wallet include nella Richiesta di Notifica come definito nella Sezione :ref:`credential-issuance-endpoint:Richiesta di Notifica`. NON DEVE essere presente se il parametro ``credentials`` non è presente.
    - Sezione 8.3 di [`OpenID4VCI`_].
  * - **transaction_id**
    - OBBLIGATORIO se ``credentials`` non è presente, altrimenti NON DEVE essere presente. Stringa che identifica una transazione di emissione differita che il Wallet include nella successiva Richiesta di Credenziale come definito nella Sezione :ref:`credential-issuance-endpoint:Endpoint Differito`. DEVE essere invalidato dopo che l'Utente ottiene la Credenziale.
    - Sezione 8.3 di [`OpenID4VCI`_].

Nel caso in cui la Richiesta di Credenziale non contenga un Token di Accesso valido, l'Endpoint Credential restituisce una risposta di errore come definito nella Sezione 3 di [:rfc:`6750`].
Se si verifica qualsiasi altro errore, il Credential Issuer DEVE restituire una risposta di errore come definito nella Sezione 8.3.1 di [`OpenID4VCI`_]. La risposta DEVE utilizzare il tipo di contenuto *application/json* e DEVE includere i seguenti parametri:

  - *error*. Il codice di errore.
  - *error_description*. Testo in forma leggibile dall'uomo che fornisce ulteriori dettagli per chiarire la natura dell'errore riscontrato.

Di seguito è riportato un esempio non normativo di una risposta di errore.

.. code:: http

  HTTP/1.1 400 Bad Request
  Content-Type: application/json
  Cache-Control: no-store

.. literalinclude:: ../../examples/credential-error.json
  :language: JSON

Nella seguente tabella sono elencati i Codici di Stato HTTP e i relativi codici di errore supportati per la risposta di errore:

.. list-table::
    :class: longtable
    :widths: 20 20 60
    :header-rows: 1

    * - **Codice di Stato**
      - **codice di errore**
      - **Descrizione**
    * - *400 Bad Request* [OBBLIGATORIO]
      - ``invalid_credential_request``
      - Il Credential Issuer non può soddisfare la richiesta a causa di parametri mancanti, parametri non validi o richiesta malformata. Sezione 8.3.1 di [`OpenID4VCI`_].
    * - *400 Bad Request* [OBBLIGATORIO]
      - ``unsupported_credential_type``
      - Il Credential Issuer non può soddisfare la richiesta perché il tipo di Credenziale richiesto non è supportato. Sezione 8.3.1 di [`OpenID4VCI`_].
    * - *400 Bad Request* [OBBLIGATORIO]
      - ``unsupported_credential_format``
      - Il Credential Issuer non può soddisfare la richiesta perché il Formato di Credenziale richiesto non è supportato. Sezione 8.3.1 di [`OpenID4VCI`_].
    * - *400 Bad Request* [OBBLIGATORIO]
      - ``invalid_proof``
      - Il Credential Issuer non può soddisfare la richiesta perché il parametro ``proof`` nella Richiesta di Credenziale non è valido o è assente. Sezione 8.3.1 di [`OpenID4VCI`_].
    * - *400 Bad Request* [OBBLIGATORIO]
      - ``invalid_nonce``
      - Il Credential Issuer non può soddisfare la richiesta perché il parametro ``proof`` nella Richiesta di Credenziale utilizza un nonce non valido. Sezione 8.3.1 di [`OpenID4VCI`_].
    * - *400 Bad Request* [OBBLIGATORIO]
      - ``invalid_encryption_parameters``
      - Il Credential Issuer non può soddisfare la richiesta perché i parametri di crittografia nella Richiesta di Credenziale non sono validi o mancanti. Sezione 8.3.1 di [`OpenID4VCI`_].
    * - *400 Bad Request* [OBBLIGATORIO]
      - ``credential_request_denied``
      - La Richiesta di Credenziale non è stata accettata dal Credential Issuer. Sezione 8.3.1 di [`OpenID4VCI`_].
    * - *400 Bad Request* [OBBLIGATORIO]
      - ``issuance_pending``
      - Solo in caso di flusso differito. Il Credential Issuer non può soddisfare la richiesta perché la Credenziale non è ancora disponibile per l'emissione. Sezione 9.3 di [`OpenID4VCI`_].
    * - *400 Bad Request* [OBBLIGATORIO]
      - ``invalid_transaction_id``
      - Solo in caso di flusso differito. Il Credential Issuer non può soddisfare la richiesta perché la Richiesta di Credenziale contiene un ``transaction_id`` non valido. Sezione 9.3 di [`OpenID4VCI`_].
    * - *400 Bad Request* [OBBLIGATORIO]
      - ``invalid_dpop_proof``
      - Il Credential Issuer non può soddisfare la richiesta a causa di *prova DPoP* non valida. Sezione 7 di [:rfc:`9449`].
    * - *500 Internal Server Error* [OBBLIGATORIO]
      - ``server_error``
      - Il Credential Issuer ha riscontrato un problema interno.
    * - *503 Service Unavailable* [OBBLIGATORIO]
      - ``temporarily_unavailable``
      - Il Credential Issuer è temporaneamente non disponibile.
    * - *504 Gateway Timeout* [OPZIONALE]
      - `-`
      - Il Credential Issuer non può soddisfare la richiesta entro l'intervallo di tempo definito.

Endpoint Differito
""""""""""""""""""

I Credential Issuer POSSONO supportare l'*Endpoint Differito* con l'obiettivo di soddisfare i casi in cui un'emissione immediata potrebbe non essere possibile, a causa di errori durante la comunicazione tra il Credential Issuer e la Fonte Autentica (ad esempio la Fonte Autentica è temporaneamente non disponibile, ecc.) o a causa di processi amministrativi o tecnici.

Nel caso in cui la Fonte Autentica e il Credential Issuer siano entrambi abilitati a utilizzare *PDND*, si DEVE applicare quanto descritto nella Sezione :ref:`authentic-sources:Fonti Autentiche`.


Si applicano i seguenti requisiti:

 1. La richiesta di Credenziale Differita PUÒ avvenire anche diversi giorni dopo la richiesta iniziale di Credenziale.
 2. L'Utente DEVE essere informato che la Credenziale è disponibile e pronta per essere emessa.
 3. Il Fornitore di Wallet NON DEVE essere informato su quale Credenziale è disponibile per l'emissione o quale Credential Issuer l'Utente deve contattare.
 4. L'Istanza del Wallet DEVE essere informata sulla quantità di tempo da attendere prima di effettuare una nuova richiesta di Credenziale.
 5. Poiché, in generale, un'indisponibilità può essere un evento imprevisto, il Credential Issuer DEVE essere in grado di passare al volo tra un flusso *immediato* e uno *differito*. Questa decisione DEVE essere presa dopo la fase di autorizzazione.


Se i Credential Issuer, che supportano questo flusso, non sono in grado di emettere immediatamente una Credenziale richiesta, DEVONO fornire all'Istanza del Wallet una Risposta di Credenziale HTTP contenente la quantità di tempo da attendere prima di effettuare una nuova richiesta di Credenziale e un identificatore della transazione di emissione differita (*transaction_id*). Il codice di stato HTTP DEVE essere *202* (vedi Sezione 15.3.3 di [:rfc:`9110`]). Di seguito viene fornito un esempio non normativo.

.. code-block:: http

  HTTP/1.1 202 Accepted
  Content-Type: application/json
  Cache-Control: no-store

.. literalinclude:: ../../examples/credential-response-deferred.json
  :language: JSON

L'Istanza del Wallet DEVE utilizzare il valore fornito nel parametro *lead_time* per informare l'Utente quando la Credenziale diventa disponibile (ad esempio utilizzando una notifica locale attivata dal valore di tempo *lead_time*). I Credential Issuer POSSONO inviare una notifica all'Utente tramite un canale di comunicazione (ad esempio indirizzo email), se precedentemente fornito dall'Utente al Credential Issuer.

Richiesta Differita
...................

Al ricevimento della notifica (dall'Istanza del Wallet e/o dal Credential Issuer), l'Utente accede all'Istanza del Wallet.

L'Istanza del Wallet DEVE presentare all'Endpoint Differito un Token di Accesso valido per l'emissione dell'Attestato Elettronico precedentemente richiesto all'Endpoint Credential.

Se il valore del parametro ``lead_time`` risulta inferiore al tempo di scadenza impostato per il Token di Accesso, l'Istanza del Wallet DOVREBBE utilizzare il Token di Accesso. Altrimenti, l'Istanza del Wallet PUÒ ottenere un nuovo Token di Accesso seguendo il flusso del Token di Aggiornamento (vedi Sezione :ref:`credential-issuance-low-level:Flusso del Refresh Token` per maggiori dettagli). Se il flusso del Token di Aggiornamento fallisce, l'Istanza del Wallet deve inviare una nuova richiesta di autenticazione.

La Richiesta di Credenziale Differita DEVE essere una richiesta HTTP POST. DEVE essere inviata utilizzando il tipo di media ``application/json``.
Il seguente parametro viene utilizzato nella Richiesta di Credenziale Differita:

  - ``transaction_id``: OBBLIGATORIO. Stringa che identifica una transazione di Emissione Differita.

Il Credential Issuer DEVE invalidare il ``transaction_id`` dopo che la Credenziale per cui era destinato è stata ottenuta dall'Istanza del Wallet.
Di seguito è riportato un esempio non normativo di una Richiesta di Credenziale Differita:

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

Risposta Differita
..................

La Risposta di Credenziale Differita DEVE essere inviata utilizzando il tipo di media `application/json``. Se l'Attestato Elettronico è disponibile, la Risposta di Credenziale Differita DEVE utilizzare i parametri ``credentials`` e ``notification_id`` come definito nella Sezione :ref:`credential-issuance-endpoint:Risposta di Credenziale`. Se la Richiesta di Credenziale Differita non è valida o l'Attestato Elettronico non è disponibile, la Risposta di Errore di Credenziale Differita DEVE essere inviata all'Istanza del Wallet secondo la Sezione 9.3 di `OpenID4VCI`_.

Endpoint di notifica
""""""""""""""""""""

L'Endpoint di Notifica viene utilizzato dal Wallet per notificare al Credential Issuer determinati eventi per le Credenziali emesse, come ad esempio se la Credenziale è stata memorizzata con successo nell'Istanza del Wallet.

Per salvaguardare la privacy, l'``event_description`` nella notifica NON DOVREBBE contenere alcuna informazione che potrebbe rivelare il comportamento dell'Utente o rivelare lo stato del dispositivo personale (ad esempio, spazio di archiviazione pieno).

Questo endpoint DEVE essere protetto utilizzando un Token di Accesso DPoP. TLS per la riservatezza del trasporto HTTP è RICHIESTO secondo la Sezione 10 di [`OpenID4VCI`_].


Richiesta di Notifica
.....................

La Richiesta di Notifica DEVE essere un HTTP POST utilizzando il tipo di media *application/json* con i seguenti parametri.

.. list-table::
  :class: longtable
  :widths: 20 60 25
  :header-rows: 1

  * - **Claim**
    - **Descrizione**
    - **Riferimento**
  * - **notification_id**
    - OBBLIGATORIO. DEVE essere uguale al valore ``notification_id`` restituito nella Risposta di Credenziale dal Credential Issuer.
    - Sezione 10.1 di [`OpenID4VCI`_].
  * - **event**
    - OBBLIGATORIO. Tipo dell'evento di notifica. DEVE essere una stringa sensibile alle maiuscole e DEVE supportare i seguenti valori:

      - *credential_accepted*: quando la Credenziale è stata memorizzata con successo nell'Istanza del Wallet.
      - *credential_deleted*: quando l'emissione non riuscita della Credenziale è stata causata da un'azione dell'utente.
      - *credential_failure*: in tutti gli altri casi non riusciti.

    - Sezione 10.1 di [`OpenID4VCI`_].
  * - **event_description**
    - OPZIONALE. Testo ASCII leggibile dall'uomo [USASCII] che fornisce informazioni aggiuntive, utilizzato per informare sull'evento verificatosi. I valori per il parametro event_description NON DEVONO includere caratteri al di fuori dell'insieme *%x20-21 / %x23-5B / %x5D-7E*.
    - Sezione 10.1 di [`OpenID4VCI`_].

Risposta di Notifica
....................

La Risposta di Notifica DEVE utilizzare un codice di stato HTTP *204 (No Content)*, come raccomandato nella Sezione 10.2 di [`OpenID4VCI`_].

In caso di errori, si DEVE applicare quanto descritto nella Sezione 10.3 di [`OpenID4VCI`_].

Nel caso in cui la Richiesta di Notifica non contenga un Token di Accesso valido, l'Endpoint di Notifica restituisce una risposta di errore come definito nella Sezione 3 di [:rfc:`6750`].
Se si verifica qualsiasi altro errore, il Credential Issuer DEVE restituire una risposta di errore come definito nella Sezione 10.3 di [`OpenID4VCI`_]. La risposta DEVE utilizzare il tipo di contenuto *application/json* e DEVE includere i seguenti parametri:

  - *error*. Il codice di errore.
  - *error_description*. Testo in forma leggibile dall'uomo che fornisce ulteriori dettagli per chiarire la natura dell'errore riscontrato.

Di seguito è riportato un esempio non normativo di una risposta di errore.

.. code:: http

  HTTP/1.1 400 Bad Request
  Content-Type: application/json
  Cache-Control: no-store

.. literalinclude:: ../../examples/notification-error.json
  :language: JSON

Nella seguente tabella sono elencati i Codici di Stato HTTP e i relativi codici di errore supportati per la risposta di errore:

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

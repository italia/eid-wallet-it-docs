.. include:: ../common/common_definitions.rst


Metadati della Soluzione Wallet
-------------------------------

L'oggetto JSON dei metadati la cui chiave è ``openid_wallet_provider`` contiene i seguenti parametri. Le chiavi pubbliche presenti in questo oggetto sono utilizzate esclusivamente per operazioni di firma e/o crittografia richieste a questa Entità quando agisce come componente del Fornitore di Wallet (ad esempio, firmare gli Attestati di Wallet per l'Istanza del Wallet).

.. list-table::
    :class: longtable
    :widths: 30 70
    :header-rows: 1

    * - **Chiave**
      - **Valore**
    * - ``jwks``
      - Documento JSON Web Key Set, passato per valore, contenente le chiavi dell'Entità per quel Tipo di Entità. DEVE essere presente se ``jwks_uri`` e ``signed_jwks_uri`` sono assenti.
    * - ``jwks_uri``
      - URL che fa riferimento a un documento JWK Set contenente le chiavi del Fornitore di Wallet per quel Tipo di Entità. Questo URL DEVE utilizzare lo schema https. DEVE essere presente se ``jwks`` e ``signed_jwks_uri`` sono assenti.
    * - ``signed_jwks_uri``
      - URL che fa riferimento a un JWT firmato avente come payload il documento JWK Set dell'Entità per quel Tipo di Entità. Questo URL DEVE utilizzare lo schema https. Il JWT DEVE essere firmato utilizzando una Chiave di Entità di Federazione. Una risposta positiva dall'URL DEVE utilizzare il codice di stato HTTP 200 con il Content Type ``application/jwk-set+jwt``. DEVE essere presente se ``jwks`` e ``jwks_uri`` sono assenti.
    * - ``logo_uri``
      - OBBLIGATORIO. URL del logo dell'entità che verrà mostrato all’Utente durante le interazioni con l’istanza del Wallet. Il MIME type del logo DEVE essere ``application/svg``.
    * - ``wallet_name`` 
      - OBBLIGATORIO. Stringa contenente il nome del Wallet. 
    * - ``authorization_endpoint``
      - OBBLIGATORIO. URL dell'endpoint del server di autorizzazione, vedi `OAUTH2`_. Gli schemi di invocazione sono specificati in :ref:`remote-flow:Flusso Remoto`.
    * - ``credential_offer_endpoint`` 
      - OBBLIGATORIO. Credential Offer Endpoint del Wallet.
    * - ``response_types_supported``
      - OPZIONALE. Array JSON di valori "response_type" di OAuth 2.0. Se presente DEVE essere impostato su ``vp_token``. Il valore predefinito è ``vp_token``.
    * - ``response_modes_supported``
      - OPZIONALE. Array JSON di valori "response_mode" di OAuth 2.0 come specificato in `OAUTH-MULT-RESP-TYPE`_. Il valore supportato DEVE essere *query*.
    * - ``vp_formats_supported``
      - OBBLIGATORIO. Oggetto contenente un elenco di coppie nome/valore, in cui il nome è un identificatore di formato di Credenziale e il valore definisce i parametri specifici del formato supportati da un Wallet. Vedere `OpenID4VP`_ Appendice B. Le Istanze del Wallet DEVONO supportare gli identificatori di formato di Credenziale richiesti da `OPENID4VC-HAIP`_ (inclusi ``dc+sd-jwt`` e ``mso_mdoc``).
    * - ``client_id_prefixes_supported``
      - RACCOMANDATO. Un array non vuoto dei prefissi dell’identificatore del Client supportati dall’Istanza del Wallet. I valori validi includono ``openid_federation`` e ``x509_hash``; se omesso, il valore predefinito è pre-registrato.
    * - ``request_object_signing_alg_values_supported``
      - OPZIONALE. Vedi OpenID Connect Discovery.

.. note::
  Alcuni flussi relativi agli Attestati Elettronici richiedono il recupero delle informazioni del Wallet prima di interagire con il Wallet stesso. Il flusso è descritto in :ref:`wallet-metadata-retrieval:Flusso di Recupero dei Wallet Metadata`.

.. note::
  Per l'``authorization_endpoint``, un link universale configurato con Assetlinks JSON per Android e Apple App Site Association per iOS riduce il rischio di dirottamento degli URL.
  Un link universale consente anche al flusso di continuare in un browser quando l'Istanza del Wallet non è installata.
  Gli schemi di invocazione sono specificati in :ref:`remote-flow:Flusso Remoto`.



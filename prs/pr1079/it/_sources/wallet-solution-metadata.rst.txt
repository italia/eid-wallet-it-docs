.. include:: ../common/common_definitions.rst

.. _wallet-solution-metadata-metadati-della-soluzione-wallet:

Metadati della Soluzione Wallet
--------------------------------

L'oggetto JSON dei metadati la cui chiave è ``wallet_solution`` contiene i seguenti parametri. Le chiavi pubbliche presenti in questo oggetto sono utilizzate esclusivamente per operazioni di firma e/o crittografia richieste a questa Entità quando agisce come componente del Fornitore di Wallet (ad esempio, firmare gli Attestati di Wallet per l'Istanza del Wallet).

.. list-table::
    :class: longtable
    :widths: 30 70
    :header-rows: 1

    * - **Chiave**
      - **Valore**
    * - ``jwks``
      - CONDIZIONALE. Documento JSON Web Key Set, passato per valore, contenente le chiavi dell'Entità per quel Tipo di Entità. DEVE essere presente se ``jwks_uri`` e ``signed_jwks_uri`` sono assenti.
    * - ``jwks_uri``
      - CONDIZIONALE. URL che fa riferimento a un documento JWK Set contenente le chiavi del Fornitore di Wallet per quel Tipo di Entità. Questo URL DEVE utilizzare lo schema https. DEVE essere presente se ``jwks`` e ``signed_jwks_uri`` sono assenti.
    * - ``signed_jwks_uri``
      - CONDIZIONALE. URL che fa riferimento a un JWT firmato avente come payload il documento JWK Set dell'Entità per quel Tipo di Entità. Questo URL DEVE utilizzare lo schema https. Il JWT DEVE essere firmato utilizzando una Chiave di Entità di Federazione. Una risposta positiva dall'URL DEVE utilizzare il codice di stato HTTP 200 con il Content Type ``application/jwk-set+jwt``. DEVE essere presente se ``jwks`` e ``jwks_uri`` sono assenti.
    * - ``logo_uri``
      - OBBLIGATORIO. URL del logo dell’entità che verrà mostrato all’Utente durante le interazioni con l’istanza del Wallet. Il MIME type del logo DEVE essere ``application/svg``.
    * - ``wallet_metadata``
      - OBBLIGATORIO. Contiene i parametri relativi ai metadati del Wallet come definiti nella :ref:`Tabella dei parametri dei metadati del portafoglio <table_wallet_metadata_parameters>` e seguenti due parametri 
      
         - ``credential_offer_endpoint`` Credential Offer Endpoint del Wallet.
         - ``wallet_name`` Stringa contenente il nome del Wallet. 


.. nota::
  Alcuni flussi relativi agli Attestati Elettronici richiedono il recupero delle informazioni del Wallet prima di interagire con il Wallet stesso. Il flusso è descritto in :ref:`wallet-metadata-retrieval:Flusso di Recupero dei Wallet Metadata`.


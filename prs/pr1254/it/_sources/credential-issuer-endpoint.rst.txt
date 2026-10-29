.. include:: ../common/common_definitions.rst
.. Incluso tramite endpoints.rst al livello di titolo '-' (livello 1).

.. role:: raw-html(raw)
  :format: html

Endpoint del Credential Issuer
------------------------------

Endpoint Metadata
^^^^^^^^^^^^^^^^^

I Credential Issuer DEVONO fornire una Entity Configuration attraverso l'endpoint ``/.well-known/openid-federation``, secondo la Sezione :ref:`infrastructure-trust:Entity Configuration`. I dettagli tecnici sono forniti nella Sezione :ref:`credential-issuer-entity-configuration:Entity Configuration del Fornitore di Attestati Elettronici`.

Alternativamente i metadati del Credential Issuer possono essere recuperati utilizzando l’identificativo del Credential Issuer. Il documento di metadata DEVE essere reso disponibile in formato JSON e JWT presso l’endpoint ``/.well-known/openid-credential-issuer`` come definito nella Sezione 12.2.2 di `OpenID4VCI`_.

L’header ``Accept-Language`` nella richiesta HTTP GET può essere utilizzato per indicare la/le lingua/e preferite.
In tal caso, il Credential Issuer può inviare un sottoinsieme dei metadati contenente dati di visualizzazione internazionalizzati per una o tutte le lingue richieste, e può indicare le lingue restituite utilizzando l’header HTTP ``Content-Language``.

Di seguito è riportato un esempio non normativo.

.. literalinclude:: ../../examples/shared/credential-issuer-endpoint-1.http
   :language: http

.. literalinclude:: ../../examples/shared/credential-issuer-endpoint-2.http
   :language: http

Il Credential Issuer DEVE rispondere con il Status Code HTTP 200 e restituire i metadati del Credential Issuer contenenti:

- i parametri definiti nella sezione :ref:`credential-issuer-metadata:Metadata per openid_credential_issuer` all’interno di un documento JSON non firmato utilizzando il media type *application/json*.

          oppure

- i parametri di header e payload definiti nella sezione 12.2.3 di `OpenID4VCI`_ oltre a quelli definiti nella sezione  :ref:`credential-issuer-metadata:Metadata per openid_credential_issuer` all'interno di un JSON Web Token firmato utilizzando il media type *application/jwt*.

Sul percorso EUDIW la Wallet Unit ottiene i Metadata del Credential Issuer come tale JSON Web Token firmato. Il media type è *application/jwt*. Il documento JSON non firmato resta disponibile allo stesso endpoint. Il documento JSON non firmato non è l'artefatto autenticato in :ref:`trust-evaluation:Metadata Validation`.

Sul filo il documento EUDIW è un solo JSON Web Token firmato. Di seguito è riportato un esempio non normativo del suo header protetto e del suo payload per un Fornitore di Attestati Elettronici. La catena ``x5c`` inizia con l'access certificate. Il trust anchor è assente. Il valore ``registration_cert`` rimanda all'esempio di WRPRC di una Relying Party in :ref:`infrastructure-trust:Wallet-Relying Party Registration Certificate (WRPRC) Profile`.

.. literalinclude:: ../../examples/credential-issuer-metadata-header.json
   :language: json

.. literalinclude:: ../../examples/credential-issuer-metadata-payload.json
   :language: json

Di seguito è riportato un esempio non normativo dei Metadata firmati del Credential Issuer di un PID Provider sul percorso EUDIW. Il primo certificato di ``x5c`` è l'access certificate illustrato in :ref:`infrastructure-trust:Wallet-Relying Party Access Certificate (WRPAC) Profile`. Il trust anchor è assente. Il valore ``registration_cert`` è la serializzazione compatta del WRPRC del PID Provider in :ref:`infrastructure-trust:Wallet-Relying Party Registration Certificate (WRPRC) Profile`. La firma è illustrativa.

.. literalinclude:: ../../examples/credential-issuer-metadata-pid-header.json
   :language: json

.. literalinclude:: ../../examples/credential-issuer-metadata-pid-payload.json
   :language: json

Gli elementi contenuti in ``authorization_servers`` nei metadati del Credential Issuer possono essere utilizzati per ottenere i metadati dell'OAuth Authorization Server tramite l’endpoint ``/.well-known/oauth-authorization-server``, come definito nella Sezione 3 del :rfc:`8414`.
Nel caso in cui il parametro ``authorization_servers`` venga omesso, è possibile utilizzare l’identificativo del Credential Issuer per recuperare i metadati del Authorization Server.

Di seguito è riportato un esempio non normativo.

.. literalinclude:: ../../examples/shared/credential-issuer-endpoint-3.http
   :language: http

OAuth Authorization Server DEVE rispondere con Status Code HTTP 200 e restituire i metadati dell’OAuth Authorization Server, contenenti i parametri definiti nella sezione :ref:`credential-issuer-metadata:Metadata per oauth_authorization_server`, all’interno di un documento JSON utilizzando il media type *application/json*.

Endpoint di Rilascio degli Attestati Elettronici
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: credential-issuance-endpoint.rst

Catalogo degli e-Service PDND del Credential Issuer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

I Credential Issuer DEVONO fornire i seguenti e-service attraverso PDND per:

   - fornire statistiche sugli Attestati Elettronici emessi


Get Statistics
""""""""""""""

.. list-table::
  :class: longtable
  :widths: 20 80
  :stub-columns: 1

  * - **Descrizione**
    - Questo servizio restituisce dati statistici sugli Attestati Elettronici emessi.
  * - **Erogatore**
    - Credential Issuer
  * - **Fruitore**
    - Terza Parte Autorizzata



.. include:: ../common/common_definitions.rst

.. "included" file, so we start with '-' title level

.. role:: raw-html(raw)
  :format: html


Endpoint del Credential Issuer
-------------------------------

Endpoint Metadata
^^^^^^^^^^^^^^^^^^^^^^^

I Credential Issuer DEVONO fornire una Entity Configuration attraverso l'endpoint ``/.well-known/openid-federation``, secondo la Sezione :ref:`trust-infrastructure:Entity Configuration`. I dettagli tecnici sono forniti nella Sezione :ref:`credential-issuer-entity-configuration:Entity Configuration del Fornitore di Attestati Elettronici`.

Alternativamente i metadati del Credential Issuer possono essere recuperati utilizzando l’identificativo del Credential Issuer. Il documento di metadata in formato JSON o JWT DEVE essere reso disponibile presso l’endpoint ``/.well-known/openid-credential-issuer`` come definito nella Sezione 12.2.2 di `OpenID4VCI`_.

L’header ``Accept-Language`` nella richiesta HTTP GET può essere utilizzato per indicare la/le lingua/e preferite.
In tal caso, il Credential Issuer può inviare un sottoinsieme dei metadati contenente dati di visualizzazione internazionalizzati per una o tutte le lingue richieste, e può indicare le lingue restituite utilizzando l’header HTTP ``Content-Language``.

Di seguito è riportato un esempio non normativo.

.. code-block:: http

    GET /.well-known/openid-credential-issuer HTTP/1.1
    Host: issuer.example.com
    Accept: application/json
    Accept-Language: it-IT, it;q=0.9

Il Credential Issuer DEVE rispondere con il Status Code HTTP 200 e restituire i metadati del Credential Issuer contenenti i parametri definiti nella sezione 12.2.3 di `OpenID4VCI`_ oltre a quelli definiti nella sezione  :ref:`credential-issuer-metadata:Metadata per openid_credential_issuer` all’interno di un documento JSON non firmato utilizzando il media type *application/json* oppure all'interno di un JSON Web Token firmato utilizzando il media type *application/jwt*.

Gli elementi contenuti in ``authorization_servers`` nei metadati del Credential Issuer possono essere utilizzati per ottenere i metadati dell'OAuth Authorization Server tramite l’endpoint ``/.well-known/oauth-authorization-server``, come definito nella Sezione 3 del :rfc:`8414`.
Nel caso in cui il parametro ``authorization_servers`` venga omesso, è possibile utilizzare l’identificativo del Credential Issuer per recuperare i metadati del Authorization Server.

Di seguito è riportato un esempio non normativo.

.. code-block:: http

    GET /.well-known/oauth-authorization-server HTTP/1.1
    Host: oauth-authorization-server.example.com

OAuth Authorization Server DEVE rispondere con Status Code HTTP 200 e restituire i metadati dell’OAuth Authorization Server, contenenti i parametri definiti nella sezione :ref:`credential-issuer-metadata:Metadata per oauth_authorization_server`, all’interno di un documento JSON utilizzando il media type *application/json*.

Endpoint di Rilascio degli Attestati Elettronici
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: credential-issuance-endpoint.rst

Catalogo degli e-Service PDND del Credential Issuer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

I Credential Issuer DEVONO fornire i seguenti e-service attraverso PDND per:

  - gestire le notifiche di disponibilità dei dati e gli aggiornamenti degli Attributi provenienti da una Fonte Autentica;
  - revocare gli Attestati Elettronici emessi per un'Istanza del Wallet revocata
  - fornire statistiche sugli Attestati Elettronici emessi

.. only:: html

  .. note::
    Lna Specifica OpenAPI completa è disponibile :raw-html:`<a href="OAS3-PDND-Issuer.html" target="_blank">qui</a>`.

.. only:: latex

  .. note::
    Lna Specifica OpenAPI completa è disponibile :ref:`appendix-oas-pdnd-issuer:Specifica OpenAPI del Credential Issuer PDND`.


Notify Wallet Instance Revocation
""""""""""""""""""""""""""""""""""

.. list-table::
  :class: longtable
  :widths: 20 80
  :stub-columns: 1
  
  * - **Descrizione**
    - Questo servizio revoca tutti gli Attestati Elettronici associati a uno specifico Utente.
  * - **Erogatore**
    - Fornitore di Attestato Elettronico
  * - **fruitore**
    - Fornitore di Wallet


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

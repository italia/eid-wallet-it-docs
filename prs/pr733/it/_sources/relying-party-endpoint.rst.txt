.. include:: ../common/common_definitions.rst

.. "included" file, so we start with '-' title level

Endpoint della Relying Party
----------------------------

La Relying Party DEVE esporre un endpoint di trust conforme alla specifica OpenID Federation 1.0 Wallet Architecture, facilitando la distribuzione dell'identità e dei metadati della Relying Party. Inoltre, nel caso in cui la Relying Party supporti la presentazione di prossimità, DEVE esporre una serie di endpoint per gestire il ciclo di vita delle Istanze di Relying Party (ad esempio, fornendo generazione di nonce, registrazione delle chiavi hardware, convalida dell'integrità e rilascio del Certificato di Accesso); i dettagli specifici della loro implementazione sono lasciati alla discrezione della Relying Party.


Endpoint di Federazione della Relying Party
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

La Relying Party DEVE fornire la propria Entity Configuration attraverso l'endpoint ``/.well-known/openid-federation``, secondo la Sezione :ref:`trust:Entity Configuration`. I dettagli tecnici sono forniti nella Sezione :ref:`relying-party-entity-configuration:Entity Configuration Relying Party`.


Endpoint Nonce della Relying Party
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

L'Endpoint Nonce della Relying Party consente all'Istanza di Relying Party di richiedere un ``nonce`` crittografico dal Backend della Relying Party. Il ``nonce`` serve come sfida imprevedibile e monouso per garantire la freschezza e prevenire attacchi di replay.

Ulteriori dettagli sulla Richiesta e Risposta Nonce sono forniti rispettivamente nelle Sezioni :ref:`mobile-application-instance:Richiesta di Nonce dell'Applicazione Mobile` e :ref:`mobile-application-instance:Richiesta di Nonce dell'Applicazione Mobile`.

Endpoint di Inizializzazione dell'Istanza di Relying Party
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

L'Endpoint di Inizializzazione dell'Istanza di Relying Party consente l'inizializzazione delle Istanze di Relying Party, consistente nella registrazione di una coppia di Cryptographic Hardware Keys a lunga durata, memorizzate in modo sicuro.

Ulteriori dettagli sulla Richiesta e Risposta di Inizializzazione dell'Istanza di Relying Party sono forniti rispettivamente nelle Sezioni :ref:`mobile-application-instance:Richiesta di Inizializzazione dell'Istanza dell'Applicazione Mobile` e :ref:`mobile-application-instance:Risposta di Inizializzazione dell'Istanza dell'Applicazione Mobile`.

Endpoint di Associazione Chiavi della Relying Party
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

L'Endpoint di Associazione Chiavi della Relying Party consente alle Istanze di Relying Party di associare la coppia di chiavi appena creata, che sarà associata a un Certificato di Accesso, all'Istanza di Relying Party, basandosi su una prova di possesso delle Cryptographic Hardware Keys generate durante la fase di :ref:`mobile-application-instance:Inizializzazione dell'Istanza dell'Applicazione Mobile`. Prima di completare il processo, il Backend della Relying Party deve anche verificare l'integrità dell'Istanza di Relying Party.

Richiesta di Associazione Chiavi della Relying Party
""""""""""""""""""""""""""""""""""""""""""""""""""""

Ulteriori dettagli sulla Richiesta di Associazione Chiavi della Relying Party sono forniti nella sezione :ref:`mobile-application-instance:Richiesta di Associazione Chiave dell'Applicazione Mobile`.


L'header ``typ`` del JWT di Richiesta di Integrità assume il valore ``rp-kb+jwt``.


Risposta di Associazione Chiavi della Relying Party
"""""""""""""""""""""""""""""""""""""""""""""""""""

In caso di richiesta riuscita, il Backend della Relying Party fornisce una Risposta HTTP con un codice di stato ``204 No Content``.

Di seguito è riportato un esempio non normativo di una Risposta alla Richiesta di Associazione Chiavi.

.. code-block:: http

    HTTP/1.1 204 No content

Se si verificano errori durante il processo, viene restituita una risposta di errore. Ulteriori dettagli sulla risposta di errore sono forniti nella sezione :ref:`mobile-application-instance:Risposta di Errore di Associazione Chiave dell'Applicazione Mobile`.


Endpoint del Certificato di Accesso della Relying Party
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

L'Endpoint del Certificato di Accesso della Relying Party consente alle Istanze di Relying Party di ottenere un Certificato di Accesso.


Richiesta del Certificato di Accesso della Relying Party
""""""""""""""""""""""""""""""""""""""""""""""""""""""""

La Richiesta del Certificato di Accesso utilizza il metodo HTTP POST con ``Content-Type`` impostato su ``application/json``.

La richiesta include il seguente parametro nel corpo:

.. list-table::
    :widths: 20 60 20
    :header-rows: 1

    * - **Parametro**
      - **Descrizione**
      - **Riferimento**
    * - **csr**
      - Il CSR generato dall'Istanza di Relying Party, codificato nel formato ``base64url`` come definito in :rfc:`2511`.
      -

Di seguito è riportato un esempio non normativo di una Richiesta di Certificato di Accesso.

.. code-block:: http

    POST /access-certificate HTTP/1.1
    Host: relying-party.example.org
    Content-Type: application/json

    {
      "csr": "MIIBvzCCAa..."
    }


Risposta del Certificato di Accesso della Relying Party
"""""""""""""""""""""""""""""""""""""""""""""""""""""""

In caso di richiesta riuscita, l'Endpoint del Certificato di Accesso della Relying Party fornisce una Risposta HTTP con un codice di stato ``200 OK`` e il Certificato di Accesso. La Risposta del Certificato di Accesso, che utilizza ``application/json`` come ``Content-Type``, include i seguenti parametri nel corpo:

.. list-table::
    :widths: 20 60 20
    :header-rows: 1

    * - **Parametro**
      - **Descrizione**
      - **Riferimento**
    * - **access_certificate**
      - Il Certificato di Accesso generato dal CSR.
      - Questa specifica.

Di seguito è riportato un esempio non normativo di una Risposta del Certificato di Accesso.

.. code-block:: http

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
      "access_certificate": "hajdnhaghSDGns..."
    }

Se si verificano errori, l'Endpoint del Certificato di Accesso della Relying Party restituisce una risposta di errore. La risposta utilizza ``application/json`` come tipo di contenuto e include i seguenti parametri:

  - *error*. Il codice di errore.
  - *error_description*. Testo in forma leggibile dall'uomo che fornisce ulteriori dettagli per chiarire la natura dell'errore riscontrato.

Di seguito è riportato un esempio non normativo di una Risposta di Errore del Certificato di Accesso.

.. code-block:: http

    HTTP/1.1 403 Forbidden
    Content-Type: application/json

    {
        "error": "invalid_request",
        "error_description": "The public key in the CSR is different from the one associated with the Cryptographic Hardware Keys."
    }

La seguente tabella elenca i Codici di Stato HTTP e i relativi codici di errore che DEVONO essere supportati per la risposta di errore, se non diversamente specificato:

.. list-table::
    :class: longtable
    :widths: 30 20 50
    :header-rows: 1

    * - **Codice di Stato HTTP**
      - **Codice di Errore**
      - **Descrizione**
    * - ``400 Bad Request``
      - ``bad_request``
      - La richiesta è malformata, mancano parametri richiesti (ad esempio, parametri di intestazione o asserzione di integrità), o include parametri non validi e sconosciuti.
    * - ``403 Forbidden``
      - ``invalid_request``
      - La chiave pubblica nel CSR non corrisponde alla chiave pubblica associata alle Cryptographic Hardware Keys.
    * - ``500 Internal Server Error``
      - ``server_error``
      - La richiesta non può essere soddisfatta perché l'Endpoint ha riscontrato un problema interno.
    * - ``503 Service Unavailable``
      - ``temporarily_unavailable``
      - La richiesta non può essere soddisfatta perché l'Endpoint è temporaneamente non disponibile (ad esempio, a causa di manutenzione o sovraccarico).

Endpoint di Cancellazione della Relying Party
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

L'Endpoint di Cancellazione, che è descritto in :ref:`relying-party-metadata:Metadati della Relying Party`, consente alle Istanze di Wallet di richiedere la cancellazione degli attributi presentati alla Relying Party. La Relying Party DEVE richiedere l'autenticazione dell'Utente prima di procedere con la cancellazione degli attributi.

Richiesta di Cancellazione
""""""""""""""""""""""""""

La Richiesta di Cancellazione DEVE essere una richiesta GET all'Endpoint di Cancellazione. L'Istanza di Wallet DEVE anche supportare un meccanismo di callback che consenta all'User-Agent di notificare all'Istanza di Wallet (e quindi all'Utente) una volta che viene restituita la Risposta di Cancellazione.

Di seguito è riportato un esempio non normativo di una Richiesta di Cancellazione in cui l'URL di callback viene passato come parametro di query.

.. code-block:: http

  GET /erasure-endpoint?callback_url=https://wallet-instance/erasure_response HTTP/1.1
  Host: relying-party.example.org

Risposta di Cancellazione
"""""""""""""""""""""""""

Se la cancellazione di tutti gli attributi associati all'Utente è avvenuta con successo, la Risposta di Cancellazione DEVE restituire un codice di stato HTTP 204.

Se invece la procedura di cancellazione degli attributi fallisce per qualsiasi circostanza, la Relying Party DEVE restituire una risposta di errore con ``application/json`` come tipo di contenuto e DEVE includere i seguenti parametri:

    - ``error``: Il codice di errore.
    - ``error_description``: Testo in forma leggibile dall'uomo che fornisce ulteriori dettagli per chiarire la natura dell'errore riscontrato.

La seguente tabella elenca i Codici di Stato HTTP e i relativi codici di errore che DEVONO essere supportati per la risposta di errore:

.. list-table::
    :class: longtable
    :widths: 20 20 60
    :header-rows: 1

    * - **Codice di Stato**
      - **Codice di Errore**
      - **Descrizione**
    * - ``400 Bad Request``
      - ``bad_request``
      - La richiesta è malformata, mancano parametri richiesti (ad esempio, parametri di intestazione o asserzione di integrità), o include parametri non validi e sconosciuti.
    * - ``401 Unauthorized``
      - ``unauthorized``
      - La richiesta non può essere soddisfatta a causa dell'autenticazione non valida da parte dell'Utente.
    * - ``500 Internal Server Error``
      - ``server_error``
      - La richiesta non può essere soddisfatta perché l'Endpoint di Cancellazione ha riscontrato un problema interno. (:rfc:`6749#section-4.1.2.1`).
    * - ``503 Service Unavailable``
      - ``temporarily_unavailable``
      - La richiesta non può essere soddisfatta perché l'Endpoint di Cancellazione è temporaneamente non disponibile (ad esempio, a causa di manutenzione o sovraccarico). (:rfc:`6749#section-4.1.2.1`).


Di seguito è riportato un esempio di risposta di errore dall'Endpoint di Cancellazione:

.. code-block:: http

  HTTP/1.1 500 Internal Server Error
  Content-Type: application/json

  {
   "error": "server_error",
   "error_description": "The request cannot be fulfilled due to an internal server error."
  }

Alla ricezione di una risposta di errore, l'Istanza di Wallet che ha effettuato la Richiesta di Cancellazione DEVE informare l'Utente della condizione di errore in modo appropriato.

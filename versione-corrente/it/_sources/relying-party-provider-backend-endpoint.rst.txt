.. include:: ../common/common_definitions.rst

.. "included" file, so we start with '-' title level

La Relying Party DEVE esporre una serie di endpoint per gestire il ciclo di vita delle App di Verifica che utilizzano un servizio di backend remoto fornito dal loro Backend del Provider di Relying Party. Questi endpoint supportano i flussi di presentazione in prossimità fornendo generazione di nonce, registrazione delle chiavi hardware, convalida dell'integrità e rilascio del Certificato di Accesso. I dettagli specifici della loro implementazione sono lasciati alla discrezione della Relying Party.

.. note::
  I test relativi agli endpoint della Relying Party sono definiti nella matrice di test per presentazione remota (:ref:`test-plans-remote-presentation:Matrice di Test per il Verificatore di Credenziali in Remoto`) e prossimità (:ref:`test-plans-proximity-presentation:Matrice di Test per il Verificatore di Credenziali in Prossimità`).


Endpoint di Federazione della Relying Party
"""""""""""""""""""""""""""""""""""""""""""

La Relying Party DEVE fornire la propria Entity Configuration attraverso l'Endpoint ``/.well-known/openid-federation``, secondo la Sezione :ref:`trust-infrastructure:Entity Configuration`. I dettagli tecnici sono forniti nella Sezione :ref:`relying-party-entity-configuration:Entity Configuration Relying Party`.


Endpoint Nonce della Relying Party
""""""""""""""""""""""""""""""""""

Il Nonce Endpoint della Relying Party consente all'App di Verifica di richiedere un ``nonce`` crittografico dal Backend del Provider di Relying Party. Il ``nonce``, un codice monouso e casuale, serve per garantire l'unicità e prevenire replay attacks.

Ulteriori dettagli sulla Richiesta e Risposta Nonce sono forniti rispettivamente nelle Sezioni :ref:`mobile-application-instance:Richiesta di Nonce dell'Applicazione Mobile` e :ref:`mobile-application-instance:Richiesta di Nonce dell'Applicazione Mobile`.

Endpoint di Inizializzazione dell'App di Verifica della Relying Party
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

L'Endpoint di Inizializzazione dell'App di Verifica consente l'inizializzazione delle App di Verifica, consistente nella registrazione di una coppia di Cryptographic Hardware Keys a lunga durata, memorizzate in modo sicuro (:ref:`test-plans-proximity-presentation:Matrice di Test per il Verificatore di Credenziali in Prossimità`).

Ulteriori dettagli sulla Richiesta e Risposta di Inizializzazione dell'App di Verifica sono forniti rispettivamente nelle Sezioni :ref:`mobile-application-instance:Richiesta di Inizializzazione dell'Istanza dell'Applicazione Mobile` e :ref:`mobile-application-instance:Risposta di Inizializzazione dell'Istanza dell'Applicazione Mobile`.

Endpoint di Associazione Chiavi della Relying Party
"""""""""""""""""""""""""""""""""""""""""""""""""""

Il Key Binding Endpoint della Relying Party consente alle App di Verifica di associare la coppia di chiavi appena creata, che sarà associata a un Certificato di Accesso, all'App di Verifica, basandosi su una dimostrazione di possesso delle Cryptographic Hardware Keys generate durante la fase di :ref:`mobile-application-instance:Inizializzazione dell'Istanza dell'Applicazione Mobile`. Prima di completare il processo, il Backend del Provider di Relying Party deve anche verificare l'integrità dell'App di Verifica.

Richiesta di Associazione Chiavi della Relying Party
....................................................

Ulteriori dettagli sulla Relying Party Key Binding Request sono forniti nella sezione :ref:`wallet-provider-endpoint:Richiesta di Emissione della Wallet App e Wallet Unit Attestation`. 

Le uniche differenze sono le seguenti:

- L'intestazione ``typ`` del JWT della Integrity Request assume il valore ``rp-kb+jwt``.
- Il corpo del JWT della Integrity Request non include la dichiarazione ``attested_key``.
- Il valore della dichiarazione ``hardware_signature`` viene ottenuto basandosi esclusivamente sul valore di ``client_data_hash_waa``.


Risposta di Associazione Chiavi della Relying Party
...................................................

In caso di richiesta riuscita, il Backend del Provider di Relying Party fornisce una HTTP Response con Status Code ``204 No Content``.

Di seguito è riportato un esempio non normativo di una Risposta alla Richiesta di Associazione Chiavi.

.. code-block:: http

    HTTP/1.1 204 No content

Se si verifica un errore durante il processo, viene restituita una risposta di errore. La risposta utilizza ``application/json`` come ``Content-Type`` e include i seguenti parametri:

  - *error*. Il codice di errore.
  - *error_description*. Testo in formato leggibile dall'uomo che fornisce ulteriori dettagli per chiarire la natura dell'errore riscontrato (:ref:`WP_035 <wallet-instance-testcases>`).


Di seguito è riportato un esempio non normativo di una Key Binding Error Response.

.. code-block:: http

    HTTP/1.1 403 Forbidden
    Content-Type: application/json

    {
      "error": "invalid_request",
      "error_description": "The provided challenge is invalid, expired, or already used."
    }

La seguente tabella elenca i codici di stato HTTP e i relativi codici di errore supportati per la risposta di errore, salvo diversa indicazione (:ref:`WP_036–0339 <wallet-instance-testcases>` and :ref:`WP_150–155 <wallet-instance-optional-testcases>`):

.. list-table::
    :class: longtable
    :widths: 30 20 50
    :header-rows: 1

    * - **HTTP Status Code**
      - **Error Code**
      - **Descrizione**
    * - ``400 Bad Request``
      - ``bad_request``
      - La richiesta è malformata, mancano parametri obbligatori (ad esempio parametri di intestazione o Integrity Assertion), oppure include parametri non validi o sconosciuti.
    * - ``403 Forbidden``
      - ``invalid_request``
      - The Verifier App è stata revocata.
    * - ``403 Forbidden``
      - ``integrity_check_error``
      - Il dispositivo non soddisfa i requisiti minimi di sicurezza del Fornitore della Relying Party.
    * - ``403 Forbidden``
      - ``invalid_request``
      - La firma della Integrity Request non è valida oppure non corrisponde alla chiave pubblica (JWK) associata.
    * - ``403 Forbidden``
      - ``invalid_request``
      - La validazione della Integrity Assertion non è riuscita; la Integrity Assertion è stata manomessa o firmata in modo non corretto.
    * - ``403 Forbidden``
      - ``invalid_request``
      - Il ``nonce`` fornito non è valido, è scaduto oppure è già stato utilizzato.
    * - ``403 Forbidden``
      - ``invalid_request``
      - La Proof of Possession (``hardware_signature``) non è valida.
    * - ``403 Forbidden``
      - ``invalid_request``
      - Il parametro ``iss`` non corrisponde all'identificatore URL previsto dal Fornitore della Relying Party.
    * - ``404 Not Found``
      - ``not_found``
      - L'istanza dell'applicazione di verifica (Verifier App) non è stata trovata.
    * - ``422 Unprocessable Content`` [OPTIONAL]
      - ``validation_error``
      - La richiesta non rispetta il formato richiesto.
    * - ``500 Internal Server Error``
      - ``server_error``
      - Si è verificato un errore interno del server durante l'elaborazione della richiesta.
    * - ``503 Service Unavailable``
      - ``temporarily_unavailable``
      - Il servizio non è disponibile. Si prega di riprovare più tardi.


Endpoint del Certificato di Accesso della Relying Party
"""""""""""""""""""""""""""""""""""""""""""""""""""""""

L'Endpoint del Certificato di Accesso della Relying Party consente alle App di Verifica di ottenere un Certificato di Accesso.


Richiesta del Certificato di Accesso della Relying Party
........................................................

La Richiesta del Certificato di Accesso utilizza il metodo HTTP POST con ``Content-Type`` impostato su ``application/json``.

La richiesta include il seguente parametro nel body:

.. list-table::
    :widths: 20 60 20
    :header-rows: 1

    * - **Parametro**
      - **Descrizione**
      - **Riferimento**
    * - **csr**
      - Il CSR generato dall'App di Verifica, codificato nel formato ``base64url`` come definito in :rfc:`2511`.
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
.......................................................

In caso di richiesta riuscita, l'Access Certificate Endpoint della Relying Party fornisce un HTTP Response con Status Code ``200 OK`` e il Certificato di Accesso. La Risposta dell'Access Certificate Endpoint, che utilizza ``application/json`` come ``Content-Type``, include i seguenti parametri nel body:

.. list-table::
    :widths: 20 60 20
    :header-rows: 1

    * - **Parametro**
      - **Descrizione**
      - **Riferimento**
    * - **access_certificate**
      - Il Certificato di Accesso generato dal CSR.
      - Questa specifica.

Di seguito è riportato un esempio non normativo di Risposta dall'Access Certificate Endpoint.

.. code-block:: http

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
      "access_certificate": "hajdnhaghSDGns..."
    }

Se si verificano errori, l'Access Certificate Endpoint della Relying Party restituisce una Error Response. La risposta utilizza ``application/json`` come tipo di contenuto e include i seguenti parametri:

  - *error*. Il codice di errore.
  - *error_description*. Testo in forma leggibile che fornisce ulteriori dettagli per chiarire la natura dell'errore riscontrato.

Di seguito è riportato un esempio non normativo di una Error Response dell'Access Certificate Endpoint.

.. code-block:: http

    HTTP/1.1 403 Forbidden
    Content-Type: application/json

    {
        "error": "invalid_request",
        "error_description": "The public key in the CSR is different from the one associated with the Cryptographic Hardware Keys."
    }

La seguente tabella elenca gli HTTP Status Code e i relativi codici di errore che DEVONO essere supportati per l'Error Response, se non diversamente specificato:

.. list-table::
    :class: longtable
    :widths: 30 20 50
    :header-rows: 1

    * - **Codice di Stato HTTP**
      - **Codice di Errore**
      - **Descrizione**
    * - ``400 Bad Request``
      - ``bad_request``
      - La richiesta non è conforme allo standard, mancano parametri richiesti (ad esempio, ``integrity_assertion``), oppure sono includi parametri non validi e sconosciuti.
    * - ``403 Forbidden``
      - ``invalid_request``
      - La chiave pubblica nel CSR non corrisponde alla chiave pubblica associata alle Cryptographic Hardware Keys.
    * - ``500 Internal Server Error``
      - ``server_error``
      - La richiesta non può essere soddisfatta perché l'Endpoint ha riscontrato un problema interno.
    * - ``503 Service Unavailable``
      - ``temporarily_unavailable``
      - La richiesta non può essere soddisfatta perché l'Endpoint è temporaneamente non disponibile (ad esempio, a causa di manutenzione o sovraccarico).

Endpoint di Cancellazione della Relying Party del Provider Backend
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

L'Endpoint di Cancellazione consente alle Istanze di Wallet di richiedere la cancellazione degli attributi presentati alla Relying Party, supportando i diritti di privacy dell'utente e la conformità normativa.

Per i requisiti di implementazione dettagliati, vedere :ref:`relying-party-remote-flow-endpoints:Endpoint di Cancellazione della Relying Party`.

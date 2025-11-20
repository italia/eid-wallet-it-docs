.. include:: ../common/common_definitions.rst

.. "included" file, so we start with '-' title level

.. role:: raw-html(raw)
  :format: html


Endpoint del Fornitore di Wallet
--------------------------------

Il Fornitore di Wallet, responsabile della fornitura di una Soluzione Wallet, DEVE esporre gli endpoint per supportare l'instaurazione della fiducia e le funzionalità essenziali dell'Istanza di Wallet. Questi includono l'endpoint di Federazione ``/.well-known/openid-federation`` che DEVE aderire alla specifica OpenID Federation 1.0 per stabilire in modo affidabile la fiducia con il Fornitore di Wallet, nonché endpoint per la registrazione dell'Istanza di Wallet, la generazione di nonce (richiesta per la registrazione), l'emissione di attestati e la revoca. A parte l'endpoint di Federazione, i dettagli di implementazione degli altri sono lasciati alla discrezione del Fornitore di Wallet.

.. note::
   I test relativi all'uso degli endpoint del Wallet Provider sono definiti in 
   :ref:`wallet-provider-test-matrix`, in particolare in 
   :ref:`wallet-provider-backend-testcases`, 
   :ref:`wallet-instance-testcases` e 
   :ref:`wallet-instance-optional-testcases`.


Endpoint di Federazione
^^^^^^^^^^^^^^^^^^^^^^^

L'endpoint ``/.well-known/openid-federation`` serve come meccanismo di discovery per l'instaurazione della fiducia recuperando la Entity Configuration del Fornitore di Wallet.

Vedere la Sezione :ref:`wallet-provider-entity-configuration:Entity Configuration del Fornitore di Wallet` per i dettagli tecnici (:ref:`WP_001–004 <wallet-provider-backend-testcases>`).



Endpoint Nonce della Soluzione Wallet
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Questo è un endpoint API RESTful che consente all'Istanza di Wallet di richiedere un nonce crittografico dal Fornitore di Wallet. Il nonce serve come sfida imprevedibile, monouso per garantire la freschezza e prevenire attacchi di replay.

Vedere :ref:`mobile-application-instance:Richiesta di Nonce dell'Applicazione Mobile` e :ref:`mobile-application-instance:Risposta di Nonce dell'Applicazione Mobile` per i dettagli sulla Richiesta di Nonce e sulla Risposta di Nonce (:ref:`WP_131 <wallet-instance-optional-testcases>`).

Endpoint di Gestione dell'Istanza di Wallet
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Questo è un endpoint API RESTful fornito dal Fornitore di Wallet che consente la gestione dell'Istanza di Wallet, inclusa la registrazione, il recupero dello stato, la revoca su richiesta (ad esempio, da parte dell'Utente) e l'eliminazione.
Le seguenti sezioni descrivono le richieste di registrazione, recupero dello stato e revoca, insieme alle relative risposte, gestite da questo endpoint, che sono necessarie per le funzionalità di base dell':ref:`wallet-instance-functionalities:Funzionalità dell'Istanza del Wallet`.

Richiesta di Registrazione dell'Istanza di Wallet
"""""""""""""""""""""""""""""""""""""""""""""""""

Per registrare un'Istanza di Wallet, la richiesta al Fornitore di Wallet DEVE utilizzare il metodo HTTP POST con ``Content-Type`` impostato su `application/json`. Il corpo della richiesta DEVE contenere i claim descritti in :ref:`mobile-application-instance:Richiesta di Inizializzazione dell'Istanza dell'Applicazione Mobile` (:ref:`WP_131–134 <wallet-instance-optional-testcases>`).

Risposta alla Registrazione dell'Istanza di Wallet
""""""""""""""""""""""""""""""""""""""""""""""""""

Se una Richiesta di Registrazione dell'Istanza di Wallet viene convalidata con successo, il Fornitore di Wallet fornisce una Risposta HTTP con codice di stato 204 (No Content). Per i dettagli vedere :ref:`mobile-application-instance:Risposta di Inizializzazione dell'Istanza dell'Applicazione Mobile` (:ref:`WP_135–137 <wallet-instance-optional-testcases>`).

Richiesta di Recupero dell'Istanza di Wallet
""""""""""""""""""""""""""""""""""""""""""""

Per recuperare tutte le Istanze di Wallet associate a un Utente, una richiesta DEVE essere inviata utilizzando il metodo HTTP GET al Fornitore di Wallet (:ref:`WP_145 <wallet-instance-optional-testcases>`).

.. note::
  Per recuperare una specifica Istanza di Wallet, la richiesta DEVE includere l'ID dell'Istanza di Wallet come parametro di percorso.


Risposta al Recupero dell'Istanza di Wallet
"""""""""""""""""""""""""""""""""""""""""""

Se una Richiesta di Recupero dell'Istanza di Wallet viene elaborata con successo, il Fornitore di Wallet DEVE restituire una Risposta HTTP con un codice di stato 200 (OK).
Il corpo della risposta DEVE essere in formato JSON e includere le informazioni rilevanti dell'Istanza di Wallet, come il suo ID univoco, lo stato e la data di emissione.
Quando si recuperano tutte le Istanze di Wallet, la risposta DEVE restituire un array contenente i dettagli di tutte le istanze associate (:ref:`WP_146 <wallet-instance-optional-testcases>`).

Se si verificano errori durante il processo di recupero, DEVE essere restituita una risposta di errore. Fare riferimento a :ref:`wallet-provider-endpoint:Gestione degli Errori per la Gestione dell'Istanza di Wallet` per i dettagli sui codici di errore e le descrizioni.

Di seguito è riportato un esempio non normativo di una risposta di errore:

.. code:: http

   HTTP/1.1 403 Forbidden
   Content-Type: application/json
   Cache-Control: no-store

.. code:: json

   {
     "error": "forbidden",
     "error_description": "User is not authorized to retrieve Wallet Instances."
   }


Richiesta di Revoca dell'Istanza di Wallet
""""""""""""""""""""""""""""""""""""""""""

Per revocare un'Istanza di Wallet attiva, una richiesta di revoca DEVE essere inviata utilizzando il metodo HTTP PATCH con Content-Type impostato su ``application/json``. Il corpo della richiesta DEVE contenere un parametro ``status`` impostato su ``REVOKED`` (:ref:`WP_147 <wallet-instance-optional-testcases>`).

.. note::
  Mentre PATCH è il metodo consigliato, la richiesta di revoca PUÒ anche essere inviata utilizzando il metodo POST, a seconda delle preferenze di implementazione.

Risposta alla Revoca dell'Istanza di Wallet
"""""""""""""""""""""""""""""""""""""""""""

Se una Richiesta di Revoca dell'Istanza di Wallet viene elaborata con successo, il Fornitore di Wallet fornisce una Risposta HTTP con un codice di stato 204 (No Content) come specificato in :ref:`WP_148 <wallet-instance-optional-testcases>`.

Se si verificano errori durante la Revoca dell'Istanza di Wallet, DEVE essere restituita una risposta di errore. Fare riferimento a :ref:`wallet-provider-endpoint:Gestione degli Errori per la Gestione dell'Istanza di Wallet` per i dettagli sui codici di errore e le descrizioni (:ref:`WP_035–039, WP_043–044 <wallet-instance-testcases>`).

Di seguito è riportato un esempio non normativo di una risposta di errore:

.. code:: http

   HTTP/1.1 400 Bad Request
   Content-Type: application/json
   Cache-Control: no-store

.. code:: json

   {
     "error": "bad_request",
     "error_description": "The request is missing status parameter."
   }

Gestione degli Errori per la Gestione dell'Istanza di Wallet
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Per garantire robustezza e sicurezza, il Fornitore di Wallet DEVE gestire gli errori in modo coerente in tutte le richieste di Gestione dell'Istanza di Wallet, incluse Registrazione, Recupero e Revoca (:ref:`WP_035–044 <wallet-instance-testcases>`, e :ref:`WP_150–155 <wallet-instance-optional-testcases>`).

In caso di errore, il Fornitore di Wallet DEVE restituire una risposta di errore come definito in :rfc:`7231`, con ulteriori dettagli disponibili in :rfc:`7807`. La risposta DEVE utilizzare il Content-Type impostato su ``application/json`` e DEVE includere i seguenti parametri:

- *error*. Il codice di errore.
- *error_description*. Testo in forma leggibile dall'uomo che fornisce ulteriori dettagli per chiarire la natura dell'errore riscontrato.

Le seguenti sezioni classificano gli errori in **errori comuni**, che si applicano a tutte le richieste, ed **errori specifici della richiesta**, che sono rilevanti per operazioni particolari.

Risposte di Errore Comuni
"""""""""""""""""""""""""

I seguenti errori si applicano a tutte le operazioni di Gestione dell'Istanza di Wallet (Registrazione, Recupero e Revoca) e DEVONO essere supportati per la risposta di errore, se non diversamente specificato (:ref:`WP_035–039 <wallet-instance-testcases>`):

.. list-table::
   :class: longtable
   :widths: 20 20 50
   :header-rows: 1

   * - **Codice di Stato HTTP**
     - **Codice di Errore**
     - **Descrizione**
   * - ``400 Bad Request``
     - ``bad_request``
     - La richiesta è malformata, mancano parametri richiesti o include parametri non validi e sconosciuti.
   * - ``422 Unprocessable Content`` [OPZIONALE]
     - ``validation_error``
     - La richiesta non aderisce al formato richiesto.
   * - ``500 Internal Server Error``
     - ``server_error``
     - Si è verificato un errore interno durante l'elaborazione della richiesta.
   * - ``503 Service Unavailable``
     - ``temporarily_unavailable``
     - Il servizio non è disponibile. Si prega di riprovare più tardi.

Risposte di Errore Specifiche della Richiesta
"""""""""""""""""""""""""""""""""""""""""""""

Gli errori in :ref:`mobile-application-instance:Risposta di Errore di Inizializzazione dell'Istanza dell'Applicazione Mobile` DEVONO essere supportati per le risposte di errore relative alla **Registrazione dell'Istanza di Wallet**.

I seguenti errori DEVONO essere supportati per le risposte di errore relative al **Recupero dell'Istanza di Wallet** (:ref:`WP_041–042 <wallet-instance-testcases>`):

.. list-table::
   :class: longtable
   :widths: 20 20 50
   :header-rows: 1

   * - **Codice di Stato HTTP**
     - **Codice di Errore**
     - **Descrizione**
   * - ``403 Forbidden``
     - ``forbidden``
     - L'Utente non ha il permesso di recuperare questa Istanza di Wallet.
   * - ``401 Unauthorized``
     - ``unauthorized``
     - La richiesta manca di Credenziali di autenticazione valide.

I seguenti errori DEVONO essere supportati per le risposte di errore relative alla **Revoca dell'Istanza di Wallet** (:ref:`WP_043–044 <wallet-instance-testcases>`):

.. list-table::
   :class: longtable
   :widths: 20 20 50
   :header-rows: 1

   * - **Codice di Stato HTTP**
     - **Codice di Errore**
     - **Descrizione**
   * - ``403 Forbidden``
     - ``invalid_request``
     - L'Utente non ha il permesso di revocare questa Istanza di Wallet.
   * - ``401 Unauthorized``
     - ``unauthorized``
     - La richiesta non può essere autenticata o autorizzata.

Endpoint di Emissione della Wallet App e Wallet Unit Attestation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Questo è un endpoint API RESTful fornito dal Fornitore di Wallet che consente all'Istanza di Wallet di ottenere una Wallet App Attestation e Wallet Unit Attestation, inviando una Richiesta di Emissione della Wallet App e Wallet Unit Attestation.

Richiesta di Emissione della Wallet App e Wallet Unit Attestation
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

La richiesta di emissione della Wallet App e la Wallet Unit Attestation utilizza il metodo HTTP POST con il ``Content-Type`` impostato su ``application/json`` (:ref:`WP_026 <wallet-instance-testcases>` e :ref:`WP_140–142 <wallet-instance-optional-testcases>`).

L'intestazione ``typ`` del JWT della richiesta di emissione della Wallet App e Wallet Unit Attestation assume il valore ``wp-war-wua+jwt``.

Il body della richiesta di emissione della Wallet App e Wallet Unit Attestation contiene un parametro ``assertion`` il cui valore è un JWT firmato che include tutti i parametri di intestazione e le claim descritti di seguito.

Di seguito è riportato un esempio non normativo di una richiesta di emissione della Wallet App e Wallet Unit Attestation.

.. code-block:: http

    POST /wallet-attestation HTTP/1.1
    Host: application-provider.example.org
    Content-Type: application/json

    {
      "assertion": "eyJpc3MiOiJodHRwczovL3dhbGxldC1wcm92aWRlc..."
    }

In particolare, il JWT della richiesta di emissione della Wallet App e Wallet Unit Attestation include i seguenti parametri di intestazione HTTP:

.. _table_waa_wua_request_claim:
.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Parametro**
      - **Descrizione**
      - **Riferimento**
    * - **alg**
      - Identificatore dell'algoritmo di firma digitale, come definito nel registro IANA "JSON Web Signature and Encryption Algorithms". DEVE essere uno degli algoritmi supportati elencati in :ref:`algorithms:cryptographic algorithms` e non DEVE essere impostato su ``none`` né su alcun identificatore di algoritmo simmetrico (MAC).
      - [:rfc:`7516#section-4.1.1`]
    * - **kid**
      - thumbprint della JWK dell'Istanza del Wallet contenuta nella dichiarazione ``cnf``.
      - [:rfc:`7638#section_3`]
    * - **typ**
      - Il tipo del JWT, che DEVE essere impostato su ``wp-war-wua+jwt``.
      - 

Il JWT della richiesta include le seguenti claim nel body:

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Descrizione**
      - **Riferimento**
    * - **iss**
      - L'identificatore del Fornitore di Wallet concatenato con l'impronta digitale (thumbprint) della JWK nella dichiarazione ``cnf``.
      - [:rfc:`9126`], [:rfc:`7519`].
    * - **aud**
      - L'identificatore del Fornitore di Wallet.
      - [:rfc:`9126`], [:rfc:`7519`].
    * - **exp**
      - UNIX timestamp che rappresenta il tempo di scadenza del JWT.
      - [:rfc:`9126`], [:rfc:`7519`].
    * - **iat**
      - UNIX timestamp che rappresenta il tempo di emissione del JWT.
      - [:rfc:`9126`], [:rfc:`7519`].
    * - **nonce**
      - Il ``nonce`` ottenuto dal Nonce Endpoint.
      -
    * - **hardware_signature**
      - la firma di ``client_data_hash_waa`` e ``client_data_hash_wua`` ottenuta utilizzando la Chiave Crittografica Hardware, codificata nel formato ``base64url``.
      -
    * - **integrity_assertion**
      - L'Integrity Assertion per la Wallet App Attestation ottenuta dalle **Device Integrity Service APIs** con il binding di ``client_data_hash_waa``.
      -
    * - **attested_key**
      - La key Attestation ottenuta per la chiave di credenziale proveniente dalle **Key Attestation APIs** con il binding di ``client_data_hash_wua`` oppure dalle **Device Integrity Service APIs** con il binding di ``client_data_hash_wua``.
      -
    * - **hardware_key_tag**
      - Il valore del Tag della Chiave Crittografica Hardware.
      -
    * - **cnf**
      - Oggetto JSON contenente la parte pubblica di una coppia di chiavi asimmetriche posseduta dall'istanza del Wallet.
      - :rfc:`7800`.

Di seguito è riportato un esempio non normativo dell'intestazione e del payload del JWT della Wallet App e Wallet Unit Attestation Request.

.. code-block:: json

    {
      "alg": "ES256",
      "kid": "OnsiandrIjp7ImNydiI6IlAtMjU2Iiwia3R5IjoiRUMiL",
      "typ": "wp-war-wua+jwt"
    }

.. code-block:: json
  
    {
      "iss": "https://wallet-provider.example.org/instance/OnsiandrIjp7ImNydiI6IlAtMjU2Iiwia3R5IjoiRUMiL",
      "sub": "https://wallet-provider.example.org/",
      "nonce": "f3b29a81-45c7-4d12-b8b5-e1f6c9327aef",
      "hardware_signature": "KoZIhvcNAQcCoIAwgAIB...",
      "integrity_assertion": "o2NmbXRvYXBwbGUtYXBwYXNzZXJ0aW9uLXBheWxvYWQtYXBw...",
      "attested_key": "o2CFbXRvYXBwbGUtYXBwYXNzTYU0aW9uLXBheWxvYWQtZvRM..."
      "hardware_key_tag": "QW12DylRTmF89iGkpydNDWW7m8bVpa2Fn9KBeXGYtfX"
      "cnf": {
        "jwk": {
          "crv": "P-256",
          "kty": "EC",
          "x": "8FJtI-yr3pjyRKGMnz4WmdnQD_uJSq4R95Nj98b44",
          "y": "MKZnSB39vFJhYgS3k7jXE4r3-CoGFQwZtPBIRqpNlrg"
        }
      }
    }


Risposta all'Emissione della Wallet App e Wallet Unit Attestation
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Se la Richiesta di Emissione della Wallet App e Wallet Unit Attestation viene convalidata con successo, il Fornitore di Wallet restituisce una risposta HTTP con un codice di stato ``200 OK`` e Content-Type ``application/json``. L'Oggetto JSON restituito DEVE possedere il parametro ``wallet_attestations`` che include gli elementi ``wallet_app_attestations`` e ``wallet_unit_attestation`` (vedi :ref:`wallet-attestation-issuance:Emissione della Wallet App e Wallet Unit Attestation`). ``wallet_app_attestations`` è un array che contiene le Wallet App Attestation nei formati ``JWT``, ``SD-JWT`` e ``mdoc``, mentre ``wallet_unit_attestation`` è un singolo oggetto che contiene la Wallet Unit Attestation. Entrambe le attestazioni sono firmate dal Fornitore di Wallet (:ref:`WP_027–029 <wallet-instance-testcases>` e :ref:`WP_143–144 <wallet-instance-optional-testcases>`). La Wallet App Attestation in formato JWT deve essere utilizzato per la fase di Emissione di un Attestato Elettronico, come OAuth Client Attestation, e sarà inviato al Fornitore di Attestati Elettronici come discusso in :ref:`credential-issuance:Emissione di Attestati Elettronici`. La Wallet App Attestation in formato SD-JWT e mdoc sarà invece utilizzato durante la presentazione rispettivamente nei flussi remoto (:ref:`remote-flow:Flusso Remoto`) e di prossimità (:ref:`proximity-flow:Flusso di Prossimità`). La Wallet Unit Attestation in formato JWT deve essere utilizzata nella fase di Emissione di un Attestato Elettronico, come intestazione JOSE ``key_attestation`` nel JWT di tipo ``proof``, e verrà inviata al Fornitore di Attestati Elettronici come discusso in :ref:`credential-issuance:Emissione di Attestati Elettronici`.


L'Oggetto JSON restituito nella risposta ha il seguente claim:

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Parametro**
      - **Descrizione**
      - **Riferimento**
    * - **wallet_attestations**
      - OBBLIGATORIO. Un array JSON contenente una o più Wallet App Attestation e una Wallet Unit Attestation negli elementi ``wallet_app_attestations`` e ``wallet_unit_attestation``, rispettivamente. Deve contenere le seguenti dichiarazioni obbligatorie:

        - **wallet_app_attestation**: un array JSON contenente una o più Wallet App Attestation emesse. Gli elementi dell'array DEVONO essere oggetti JSON. Devono essere presenti almeno due oggetti JSON.
        - **wallet_unit_attestation**: un oggetto JSON contenente la Wallet Unit Attestation emessa.
      - Questa specifica.

Ogni oggetto JSON contenuto nell'array ``wallet_app_attestations`` DEVE avere la seguente forma:

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Parametro**
      - **Descrizione**
      - **Riferimento**
    * - **format**
      - Una stringa che identifica il Modello di Dati utilizzato per creare e rappresentare la Wallet App Attestation. DEVE essere ``jwt``, ``dc+sd-jwt`` o ``mso_mdoc`` a seconda del formato della Credenziale.
      - Questa specifica.
    * - **wallet_app_attestation**
      - Una stringa che rappresenta la Wallet App Attestation. Se

        - la Wallet App Attestation è in formato JWT, allora il valore del claim DEVE essere una stringa che è un JWT.
        - la Wallet App Attestation è in formato SD-JWT, allora il valore del claim DEVE essere una stringa che è un SD-JWT VC.
        - la Wallet App Attestation è in formato mdoc, allora il valore del claim è la rappresentazione codificata in base64url della struttura IssuerSigned codificata in CBOR, come definito in [ISO.18013-5]. Questa struttura DEVE contenere tutti i Namespace e gli IssuerSignedItems inclusi nel MobileSecurityObject.

      - Questa specifica.

Nel caso del parametro ``wallet_unit_attestation``, il suo valore è una stringa che rappresenta la Wallet Unit Attestation in formato JWT.

Se si verifica un errore durante il processo, viene restituita una risposta di errore. La risposta utilizza ``application/json`` come ``Content-Type`` e include i seguenti parametri:

  - *error*: il codice di errore.
  - *error_description*: testo in formato leggibile dall'uomo che fornisce ulteriori dettagli per chiarire la natura dell'errore riscontrato (:ref:`WP_035 <wallet-instance-testcases>`).

Di seguito è riportato un esempio non normativo di una Wallet App e Wallet Unit Attestation Issuance Response.

.. code-block:: http

    HTTP/1.1 403 Forbidden
    Content-Type: application/json

    {
      "error": "invalid_request",
      "error_description": "The provided challenge is invalid, expired, or already used."
    }

La seguente tabella elenca i codici di stato HTTP e i relativi codici di errore supportati per la risposta di errore, salvo diversa indicazione (:ref:`WP_036–039 <wallet-instance-testcases>` e :ref:`WP_150–155 <wallet-instance-optional-testcases>`):

.. list-table::
    :class: longtable
    :widths: 30 20 50
    :header-rows: 1

    * - **HTTP Status Code**
      - **Error Code**
      - **Descrizione**
    * - ``400 Bad Request``
      - ``bad_request``
      - La richiesta è malformata, mancano parametri obbligatori (ad esempio parametri di intestazione, Integrity Assertion o ``attested_key``), oppure include parametri non validi o sconosciuti.
    * - ``403 Forbidden``
      - ``invalid_request``
      - L'istanza del Wallet è stata revocata.
    * - ``403 Forbidden``
      - ``integrity_check_error``
      - Il dispositivo non soddisfa i requisiti minimi di sicurezza del Fornitore di Wallet.
    * - ``403 Forbidden``
      - ``invalid_request``
      - La firma della Wallet App e della Wallet Unit Attestation Request non è valida oppure non corrisponde alla chiave pubblica (JWK) associata.
    * - ``403 Forbidden``
      - ``invalid_request``
      - La validazione della Integrity Assertion o della Key Attestation (``attested_key``) non è riuscita; la Integrity Assertion o la Key Attestation (``attested_key``) è stata manomessa o firmata in modo non corretto.
    * - ``403 Forbidden``
      - ``invalid_request``
      - Il ``nonce`` fornito non è valido, è scaduto oppure è già stato utilizzato.
    * - ``403 Forbidden``
      - ``invalid_request``
      - La Proof of Possession (``hardware_signature``) non è valida.
    * - ``403 Forbidden``
      - ``invalid_request``
      - Il parametro ``iss`` non corrisponde all'identificatore URL previsto dal Fornitore di Wallet.
    * - ``404 Not Found``
      - ``not_found``
      - L'istanza del Wallet non è stata trovata.
    * - ``422 Unprocessable Content`` [OPTIONAL]
      - ``validation_error``
      - La richiesta non rispetta il formato richiesto.
    * - ``500 Internal Server Error``
      - ``server_error``
      - Si è verificato un errore interno del server durante l'elaborazione della richiesta.
    * - ``503 Service Unavailable``
      - ``temporarily_unavailable``
      - Il servizio non è disponibile. Si prega di riprovare più tardi.



JWT della Wallet App Attestation
"""""""""""""""""""""""""""""""""

L'header JOSE del JWT della Wallet App Attestation contiene i seguenti parametri:

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Header JOSE**
      - **Descrizione**
      - **Riferimento**
    * - **alg**
      - OBBLIGATORIO. Un identificatore di algoritmo di firma digitale come da registro IANA "JSON Web Signature and Encryption Algorithms". DEVE essere uno degli algoritmi supportati elencati nella Sezione :ref:`algorithms:Algoritmi Crittografici` e NON DEVE essere impostato su ``none`` o qualsiasi identificatore di algoritmo simmetrico (MAC).
      - :rfc:`7516#section-4.1.1`.
    * - **kid**
      - OBBLIGATORIO. Identificatore univoco della chiave pubblica associata alla chiave privata che il Fornitore di Wallet ha utilizzato per firmare la Wallet App Attestation.
      - :rfc:`7638#section_3`.
    * - **typ**
      - OBBLIGATORIO. DEVE essere impostato su ``oauth-client-attestation+jwt``
      - `OPENID4VC-HAIP`_.
    * - **trust_chain**
      - OBBLIGATORIO. Sequenza di Entity Statement che compone la Catena di Fiducia relativa al Fornitore di Wallet.
      - `OID-FED`_ Sezione 4.3 *Trust Chain Header Parameter*.
    * - **x5c**
      - OBBLIGATORIO. Contiene il certificato di chiave pubblica X.509 o la catena di certificati (:rfc:`5280`) corrispondente alla chiave utilizzata per firmare digitalmente il JWT.
      - :rfc:`7515` Sezione 4.1.8 e `SD-JWT-VC`_ Sezione 3.5.

Il corpo del JWT della Wallet App Attestation contiene i seguenti claim:

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Descrizione**
      - **Riferimento**
    * - **iss**
      - OBBLIGATORIO. Identificatore del Fornitore di Wallet.
      - :rfc:`9126` e :rfc:`7519`.
    * - **exp**
      - OBBLIGATORIO. Timestamp UNIX con il tempo di scadenza del JWT.
      - :rfc:`9126` e :rfc:`7519`.
    * - **iat**
      - OBBLIGATORIO. Timestamp UNIX con il tempo di emissione del JWT.
      - :rfc:`9126` e :rfc:`7519`.
    * - **cnf**
      - OBBLIGATORIO. Oggetto JSON, contenente la parte pubblica di una coppia di chiavi asimmetriche posseduta dall'Istanza di Wallet.
      - :rfc:`7800`.
    * - **wallet_link**
      - OPZIONALE. Stringa contenente un URL per ottenere ulteriori informazioni sul Wallet e sul Fornitore di Wallet.
      - `OpenID4VCI`_.
    * - **wallet_name**
      - OPZIONALE. Stringa contenente un nome leggibile dall'uomo del Wallet.
      - `OpenID4VCI`_.
    * - **sub**
      - OBBLIGATORIO. Identificatore dell'Istanza di Wallet che è l'impronta digitale della JWK della Wallet App Attestation.
      - :rfc:`9126` e :rfc:`7519`.

Di seguito è riportato un esempio non normativo dell'header e del payload della Wallet App Attestation JWT senza codifica e firma applicata:

.. literalinclude:: ../../examples/wa-jwt_example_header.json
  :language: JSON

.. literalinclude:: ../../examples/wa-jwt_example_payload.json
  :language: JSON

SD-JWT della Wallet App Attestation
"""""""""""""""""""""""""""""""""""

L'header JOSE dell'SD-JWT della Wallet App Attestation DEVE contenere i seguenti parametri:

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Header JOSE**
      - **Descrizione**
      - **Riferimento**
    * - **alg**
      - OBBLIGATORIO. Un identificatore di algoritmo di firma digitale come da registro IANA "JSON Web Signature and Encryption Algorithms". DEVE essere uno degli algoritmi supportati elencati in :ref:`algorithms:Algoritmi Crittografici` e NON DEVE essere impostato su ``none`` o qualsiasi identificatore di algoritmo simmetrico (MAC).
      - :rfc:`7516#section-4.1.1`.
    * - **kid**
      - OBBLIGATORIO. Identificatore univoco della chiave pubblica associata alla chiave privata che il Fornitore di Wallet ha utilizzato per firmare la Wallet App Attestation.
      - :rfc:`7638#section_3`.
    * - **typ**
      - OBBLIGATORIO. DEVE essere impostato su ``dc+sd-jwt``
      - `OPENID4VC-HAIP`_.
    * - **trust_chain**
      - OBBLIGATORIO. Sequenza di Entity Statement che compone la Catena di Fiducia relativa al Fornitore di Wallet.
      - `OID-FED`_ Sezione 4.3 *Trust Chain Header Parameter*.
    * - **x5c**
      - OBBLIGATORIO. Contiene il certificato di chiave pubblica X.509 o la catena di certificati (:rfc:`5280`) corrispondente alla chiave utilizzata per firmare digitalmente il JWT.
      - :rfc:`7515` Sezione 4.1.8 e `SD-JWT-VC`_ Sezione 3.5.

Il corpo dell'SD-JWT della Wallet App Attestation contiene i seguenti claim:

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Descrizione**
      - **Riferimento**
    * - **iss**
      - OBBLIGATORIO. Identificatore del Fornitore di Wallet.
      - :rfc:`9126` e :rfc:`7519`.
    * - **exp**
      - OBBLIGATORIO. Timestamp UNIX con il tempo di scadenza del JWT.
      - :rfc:`9126` e :rfc:`7519`.
    * - **iat**
      - OBBLIGATORIO. Timestamp UNIX con il tempo di emissione del JWT.
      - :rfc:`9126` e :rfc:`7519`.
    * - **cnf**
      - OBBLIGATORIO. Oggetto JSON, contenente la parte pubblica di una coppia di chiavi asimmetriche posseduta dall'Istanza di Wallet.
      - :rfc:`7800`.
    * - **vct**
      - OBBLIGATORIO. Il valore del tipo di Credenziale DEVE essere una Stringa URL HTTPS e DEVE essere impostato come ``urn:eudi:wallet_app_attestation:it:{version}``; si veda :ref:`registry:Struttura del Catalogo degli Attestati Elettronici` per dettagli.
      - Sezione 3.2.2.2 `SD-JWT-VC`_.
    * - **_sd**
      - OBBLIGATORIO. Array JSON contenente un elenco di tutti i digest delle divulgazioni.
      - `SD-JWT`_.
    * - **sd_alg**
      - OBBLIGATORIO. Stringa contenente l'algoritmo di hash utilizzato dal Fornitore di Wallet per generare i digest delle divulgazioni.
      - `SD-JWT`_.
    * - **sub**
      - OPZIONALE. Identificatore dell'Istanza di Wallet che può essere l'impronta del JWK della Wallet App Attestation.
      - :rfc:`9126` e :rfc:`7519`.
    

Le seguenti divulgazioni POSSONO essere presenti:

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Divulgazione**
      - **Descrizione**
      - **Riferimento**
    * - **wallet_link**
      - OPZIONALE. Stringa contenente un URL per ottenere ulteriori informazioni sul Wallet e sul Fornitore di Wallet.
      - `OpenID4VCI`_.
    * - **wallet_name**
      - OPZIONALE. Stringa contenente un nome leggibile dall'uomo del Wallet.
      - `OpenID4VCI`_.

.. note:: 
  
  Indipendentemente dal fatto che ``wallet_link`` e ``wallet_name`` siano divulgabili selettivamente, questi valori NON DEVONO essere mostrati all'Utente, in quanto non sono attributi dell'Utente.

Di seguito sono descritti esempi di valori per le divulgazioni:

**Claim** ``wallet_link``:

- Hash SHA-256: ``cD9/XC7t7QVHvmSiE1dGW0WYr0jcqm8n0GA6MGitaik=``
- Divulgazione: ``WyIyR0xDNDJzS1F2ZUNmR2ZyeU5STjl3IiwgIndhbGxldF9saW5rIiwgImh0dHBzOi8vZXhhbXBsZS5jb20vd2FsbGV0L2RldGFpbF9pbmZvLmh0bWwiXQ==``
- Contenuti: ``["2GLC42sKQveCfGfryNRN9w", "wallet_link", "https://example.com/wallet/detail_info.html"]``

**Claim** ``wallet_name``:

- Hash SHA-256: ``iQQhzf6+saYCzHH92N1QyJisKsZbApbTrJ1amHgLoOk=``
- Divulgazione:n``WyIyR0xDNDJzS1F2ZUNmR2ZyeU5STjl3IiwgIndhbGxldF9uYW1lIiwgIldhbGxldF9Ib2JiaXRvbl92MSJd``
- Contenuti: ``["2GLC42sKQveCfGfryNRN9w", "wallet_name", "Wallet_v1"]``

Di seguito è riportato un esempio non normativo dell'header e del payload della Wallet App Attestation SD-JWT senza codifica e firma applicata:

.. literalinclude:: ../../examples/wa_sd_jwt_example_header.json
  :language: JSON

.. literalinclude:: ../../examples/wa_sd_jwt_example_payload.json
  :language: JSON

Wallet App Attestation mdoc
""""""""""""""""""""""""""""

Questa descrizione specializza ulteriormente le linee guida fornite in ref:`pid-eaa-data-model:MDOC-CBOR Credential Format` per rappresentare la Wallet App Attestation in formato mdoc. Quest'ultimo DEVE avere il ``docType`` alorizzato come ``{Trust Anchor reverse domain}.{wallet_app_attestation}.{versione}``; si veda :ref:`registry:Struttura del Catalogo degli Attestati Elettronici` per dettagli.

I ``nameSpaces`` per gli Oggetti Json del nameSpace domestico sono definiti come segue:

.. list-table:: it.wallet.trust-registry.WalletAttestation.1
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **elementIdentifier**
      - **Descrizione**
      - **Riferimento**
    * - **sub**
      - OPZIONALE. Identificatore dell'Istanza di Wallet che è l'impronta digitale della Chiave COSE della Wallet App Attestation.
      - :rfc:`9126` e :rfc:`7519`.
    * - **wallet_link**
      - OPZIONALE. Stringa JSON contenente un URL per ottenere ulteriori informazioni sul Wallet e sul Fornitore di Wallet.
      - `OpenID4VCI`_.
    * - **wallet_name**
      - OPZIONALE. Stringa JSON, DEVE essere l'Identificatore del Fornitore di Wallet.
      - `OpenID4VCI`_.

Di seguito è riportato un esempio non normativo della Wallet App Attestation mdoc in notazione diagnostica CBOR:

.. literalinclude:: ../../examples/wa_mso_mdoc_example.txt
  :language: text

.. note:: 
  
  Indipendentemente dal fatto che ``sub``, ``wallet_link`` e ``wallet_name`` siano contenuti nel namespace, questi valori NON DEVONO essere mostrati all'Utente, in quanto non sono un attributo dell'Utente.


Wallet Unit Attestation JWT
""""""""""""""""""""""""""""

L'intestazione JOSE del Wallet Unit Attestation JWT contiene i seguenti parametri:


.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **JOSE header**
      - **Descrizione**
      - **Riferimento**
    * - **alg**
      - OBBLIGATORIO. Un identificatore di algoritmo di firma digitale come da registro IANA "JSON Web Signature and Encryption Algorithms". DEVE essere uno degli algoritmi supportati elencati in :ref:`algorithms:Algoritmi Crittografici` e NON DEVE essere impostato su ``none`` o qualsiasi identificatore di algoritmo simmetrico (MAC).
      - :rfc:`7516#section-4.1.1`.
    * - **kid**
      - OBBLIGATORIO. Identificatore univoco della chiave pubblica associata alla chiave privata che il Fornitore di Wallet ha utilizzato per firmare la Wallet Unit Attestation.
      - :rfc:`7638#section_3`.
    * - **typ**
      - OBBLIGATORIO. Deve essere impostato su ``key-attestation+jwt``
      - `OPENID4VC-HAIP`_.
    * - **trust_chain**
      - OBBLIGATORIO. Sequenza di Entity Statement che compone la Catena di Fiducia relativa al Fornitore di Wallet.
      - `OID-FED`_ Sezione 4.3 *Trust Chain Header Parameter*.
    * - **x5c**
      - OPZIONALE. Contiene il certificato di chiave pubblica X.509 o la catena di certificati (:rfc:`5280`) corrispondente alla chiave utilizzata per firmare digitalmente il JWT.
      - :rfc:`7515` Sezione 4.1.8 e `SD-JWT-VC`_ Sezione 3.5.

Il corpo del Wallet Unit Attestation JWT contiene le seguenti dichiarazioni (claims):

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Descrizione**
      - **Riferimento**
    * - **iss**
      - OBBLIGATORIO. Identificatore del Fornitore di Wallet.
      - :rfc:`9126` e :rfc:`7519`.
    * - **exp**
      - OBBLIGATORIO. Timestamp UNIX con il tempo di scadenza del JWT.
      - :rfc:`9126` e :rfc:`7519`.
    * - **iat**
      - OBBLIGATORIO. Timestamp UNIX con il tempo di emissione del JWT.
      - :rfc:`9126` e :rfc:`7519`.
    * - **attested_keys**
      - OBBLIGATORIO. Un array non vuoto di chiavi attestate provenienti dallo stesso componente di archiviazione delle chiavi, utilizzando la sintassi JWK, contenente la parte pubblica di una coppia di chiavi asimmetriche posseduta dall'istanza del Wallet.
      - :rfc:`7517`.
    * - **key_storage**
      - OBBLIGATORIO. Un array non vuoto di stringhe sensibili alle maiuscole che dichiarano la resistenza al potenziale di attacco del componente di archiviazione delle chiavi e delle chiavi attestate nel parametro ``attested_keys``. I seguenti valori sono definiti come possibili valori per questa dichiarazione claim:

        - ``iso_18045_high``: Deve essere utilizzato quando l'archiviazione delle chiavi è resistente ad attacchi con potenziale di attacco ``High``.
        - ``iso_18045_moderate``: Deve essere utilizzato quando l'archiviazione delle chiavi è resistente ad attacchi con potenziale di attacco  ``Moderate``.
        - ``iso_18045_basic``: Deve essere utilizzato quando l'archiviazione delle chiavi è resistente ad attacchi con potenziale di attacco  ``Basic``.
      - `OpenID4VCI`_.
    * - **user_authentication**
      - OBBLIGATORIO. Un array non vuoto di stringhe sensibili alle maiuscole che dichiarano la resistenza al potenziale di attacco dei metodi di autenticazione utente autorizzati ad accedere alle chiavi private dal parametro attested_keys. I seguenti valori sono definiti come possibili valori per questa dichiarazione claim:

        - ``iso_18045_high``: Deve essere utilizzato quando l'autenticazione dell'utente è resistente ad attacchi con potenziale di attacco ``High``.
        - ``iso_18045_moderate``: Deve essere utilizzato quando l'autenticazione dell'utente è resistente ad attacchi con potenziale di attacco ``Moderate``.
        - ``iso_18045_basic``: Deve essere utilizzato quando l'autenticazione dell'utente è resistente ad attacchi con potenziale di attacco ``Basic``.
      - `OpenID4VCI`_.
    * - **status**
      - OBBLIGATORIO. Oggetto JSON che rappresenta i meccanismi supportati per la verifica della revoca, come ad esempio OAuth Status List.
      - `OpenID4VCI`_.
    * - **certification**
      - OPZIONALE. Una stringa che contiene un URL che rimanda alla certificazione del componente di archiviazione delle chiavi.
      - `OpenID4VCI`_.


Di seguito è riportato un esempio non normativo dell'intestazione e del payload del Wallet Unit Attestation JWT, senza codifica né firma applicata:

.. literalinclude:: ../../examples/wua-jwt_example_header.json
  :language: JSON

.. literalinclude:: ../../examples/wua-jwt_example_payload.json
  :language: JSON


Catalogo e-Service PDND del Fornitore di Wallet
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

La morte dell'Utente porta alla revoca delle Istanze di Wallet dell'Utente e all'eliminazione dell'account dell'Utente presso il Fornitore di Wallet. Per questo motivo, il Fornitore di Wallet fornisce il seguente e-service tramite PDND.
Un Fornitore di Attestati Elettronici di Dati di Identificazione Personale che è stato notificato dalla Fonte Autentica del PID della morte dell'Utente DEVE inviare una notifica ai Fornitori di Wallet utilizzando questo endpoint.

.. only:: html

  .. note::
    Una Specifica OpenAPI completa è disponibile :raw-html:`<a href="OAS3-PDND-WP.html" target="_blank">qui</a>`.

.. only:: latex

  .. note::
    Una Specifica OpenAPI completa è disponibile :ref:`appendix-oas-pdnd-wp:Specifica OpenAPI del Fornitore di Wallet PDND`.

Notifica Morte Utente
"""""""""""""""""""""

.. list-table::
    :class: longtable
    :widths: 20 80
    :stub-columns: 1

    * - **Descrizione**
      - Questo servizio viene utilizzato per notificare al Fornitore di Wallet la necessità di revocare l'Istanza di Wallet ed eliminare l'account dell'Utente a causa della morte dell'Utente.
    * - **Fornitore**
      - Fornitore di Wallet
    * - **Consumatore**
      - Fornitore di Attestati Elettronici di Dati di Identificazione Personale

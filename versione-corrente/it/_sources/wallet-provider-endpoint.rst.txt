.. include:: ../common/common_definitions.rst

.. "included" file, so we start with '-' title level

.. role:: raw-html(raw)
  :format: html


Endpoint del Fornitore di Wallet
--------------------------------

Il Fornitore di Wallet, responsabile della fornitura di una Soluzione Wallet, DEVE esporre gli endpoint per supportare l'instaurazione della fiducia e le funzionalità essenziali dell'Istanza di Wallet. Questi includono l'endpoint di Federazione ``/.well-known/openid-federation`` che DEVE aderire alla specifica OpenID Federation 1.0 per stabilire in modo affidabile la fiducia con il Fornitore di Wallet, nonché endpoint per la registrazione dell'Istanza di Wallet, la generazione di nonce (richiesta per la registrazione), l'emissione di attestati e la revoca. A parte l'endpoint di Federazione, i dettagli di implementazione degli altri sono lasciati alla discrezione del Fornitore di Wallet.

Endpoint di Federazione
^^^^^^^^^^^^^^^^^^^^^^^

L'endpoint ``/.well-known/openid-federation`` serve come meccanismo di discovery per l'instaurazione della fiducia recuperando la Entity Configuration del Fornitore di Wallet.

Vedere la Sezione :ref:`wallet-provider-entity-configuration:Entity Configuration del Fornitore di Wallet` per i dettagli tecnici.


Endpoint Nonce della Soluzione Wallet
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Questo è un endpoint API RESTful che consente all'Istanza di Wallet di richiedere un nonce crittografico dal Fornitore di Wallet. Il nonce serve come sfida imprevedibile, monouso per garantire la freschezza e prevenire attacchi di replay.

Vedere :ref:`mobile-application-instance:Richiesta di Nonce dell'Applicazione Mobile` e :ref:`mobile-application-instance:Risposta di Nonce dell'Applicazione Mobile` per i dettagli sulla Richiesta di Nonce e sulla Risposta di Nonce.

Endpoint di Gestione dell'Istanza di Wallet
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Questo è un endpoint API RESTful fornito dal Fornitore di Wallet che consente la gestione dell'Istanza di Wallet, inclusa la registrazione, il recupero dello stato, la revoca su richiesta (ad esempio, da parte dell'Utente) e l'eliminazione.
Le seguenti sezioni descrivono le richieste di registrazione, recupero dello stato e revoca, insieme alle relative risposte, gestite da questo endpoint, che sono necessarie per le funzionalità di base dell':ref:`wallet-instance-functionalities:Funzionalità dell'Istanza del Wallet`.

Richiesta di Registrazione dell'Istanza di Wallet
"""""""""""""""""""""""""""""""""""""""""""""""""

Per registrare un'Istanza di Wallet, la richiesta al Fornitore di Wallet DEVE utilizzare il metodo HTTP POST con ``Content-Type`` impostato su `application/json`. Il corpo della richiesta DEVE contenere i claim descritti in :ref:`mobile-application-instance:Richiesta di Inizializzazione dell'Istanza dell'Applicazione Mobile`.

Risposta alla Registrazione dell'Istanza di Wallet
""""""""""""""""""""""""""""""""""""""""""""""""""

Se una Richiesta di Registrazione dell'Istanza di Wallet viene convalidata con successo, il Fornitore di Wallet fornisce una Risposta HTTP con codice di stato 204 (No Content). Per i dettagli vedere :ref:`mobile-application-instance:Risposta di Inizializzazione dell'Istanza dell'Applicazione Mobile`.

Richiesta di Recupero dell'Istanza di Wallet
""""""""""""""""""""""""""""""""""""""""""""

Per recuperare tutte le Istanze di Wallet associate a un Utente, una richiesta DEVE essere inviata utilizzando il metodo HTTP GET al Fornitore di Wallet.

.. note::
  Per recuperare una specifica Istanza di Wallet, la richiesta DEVE includere l'ID dell'Istanza di Wallet come parametro di percorso.


Risposta al Recupero dell'Istanza di Wallet
"""""""""""""""""""""""""""""""""""""""""""

Se una Richiesta di Recupero dell'Istanza di Wallet viene elaborata con successo, il Fornitore di Wallet DEVE restituire una Risposta HTTP con un codice di stato 200 (OK).
Il corpo della risposta DEVE essere in formato JSON e includere le informazioni rilevanti dell'Istanza di Wallet, come il suo ID univoco, lo stato e la data di emissione.
Quando si recuperano tutte le Istanze di Wallet, la risposta DEVE restituire un array contenente i dettagli di tutte le istanze associate.

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

Per revocare un'Istanza di Wallet attiva, una richiesta di revoca DEVE essere inviata utilizzando il metodo HTTP PATCH con Content-Type impostato su ``application/json``. Il corpo della richiesta DEVE contenere un parametro ``status`` impostato su ``REVOKED``.

.. note::
  Mentre PATCH è il metodo consigliato, la richiesta di revoca PUÒ anche essere inviata utilizzando il metodo POST, a seconda delle preferenze di implementazione.

Risposta alla Revoca dell'Istanza di Wallet
"""""""""""""""""""""""""""""""""""""""""""

Se una Richiesta di Revoca dell'Istanza di Wallet viene elaborata con successo, il Fornitore di Wallet fornisce una Risposta HTTP con un codice di stato 204 (No Content).

Se si verificano errori durante la Revoca dell'Istanza di Wallet, DEVE essere restituita una risposta di errore. Fare riferimento a :ref:`wallet-provider-endpoint:Gestione degli Errori per la Gestione dell'Istanza di Wallet` per i dettagli sui codici di errore e le descrizioni.

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

Per garantire robustezza e sicurezza, il Fornitore di Wallet DEVE gestire gli errori in modo coerente in tutte le richieste di Gestione dell'Istanza di Wallet, incluse Registrazione, Recupero e Revoca.

In caso di errore, il Fornitore di Wallet DEVE restituire una risposta di errore come definito in :rfc:`7231`, con ulteriori dettagli disponibili in :rfc:`7807`. La risposta DEVE utilizzare il Content-Type impostato su ``application/json`` e DEVE includere i seguenti parametri:

- *error*. Il codice di errore.
- *error_description*. Testo in forma leggibile dall'uomo che fornisce ulteriori dettagli per chiarire la natura dell'errore riscontrato.

Le seguenti sezioni classificano gli errori in **errori comuni**, che si applicano a tutte le richieste, ed **errori specifici della richiesta**, che sono rilevanti per operazioni particolari.

Risposte di Errore Comuni
"""""""""""""""""""""""""

I seguenti errori si applicano a tutte le operazioni di Gestione dell'Istanza di Wallet (Registrazione, Recupero e Revoca) e DEVONO essere supportati per la risposta di errore, se non diversamente specificato:

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

I seguenti errori DEVONO essere supportati per le risposte di errore relative al **Recupero dell'Istanza di Wallet**:

.. list-table::
   :class: longtable
   :widths: 20 20 50
   :header-rows: 1

   * - **Codice di Stato HTTP**
     - **Codice di Errore**
     - **Descrizione**
   * - ``403 Forbidden``
     - ``forbidden``
     - L'utente non ha il permesso di recuperare questa Istanza di Wallet.
   * - ``401 Unauthorized``
     - ``unauthorized``
     - La richiesta manca di Credenziali di autenticazione valide.

I seguenti errori DEVONO essere supportati per le risposte di errore relative alla **Revoca dell'Istanza di Wallet**:

.. list-table::
   :class: longtable
   :widths: 20 20 50
   :header-rows: 1

   * - **Codice di Stato HTTP**
     - **Codice di Errore**
     - **Descrizione**
   * - ``403 Forbidden``
     - ``invalid_request``
     - L'utente non ha il permesso di revocare questa Istanza di Wallet.
   * - ``401 Unauthorized``
     - ``unauthorized``
     - La richiesta non può essere autenticata o autorizzata.

Endpoint di Emissione dell'Attestato di Wallet
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Questo è un endpoint API RESTful fornito dal Fornitore di Wallet che consente all'Istanza di Wallet di ottenere un Attestato di Wallet, inviando una Richiesta di Emissione dell'Attestato di Wallet.

Richiesta di Emissione dell'Attestato di Wallet
"""""""""""""""""""""""""""""""""""""""""""""""

Ulteriori dettagli sulla Richiesta di Emissione dell'Attestato di Wallet sono forniti nella sezione :ref:`mobile-application-instance:Richiesta di Associazione Chiave dell'Applicazione Mobile`.

L'header ``typ`` del JWT della Richiesta di Integrità assume il valore ``wp-war+jwt``.

Risposta all'Emissione dell'Attestato di Wallet
"""""""""""""""""""""""""""""""""""""""""""""""

Se la Richiesta di Emissione dell'Attestato di Wallet viene convalidata con successo, il Fornitore di Wallet restituisce una risposta HTTP con un codice di stato ``200 OK`` e Content-Type ``application/json``. L'Oggetto JSON restituito DEVE possedere il parametro ``wallet_attestations`` il cui valore è un array di Oggetti JSON (vedi :ref:`wallet-attestation-issuance:Emissione dell'Attestato di Wallet`) contenente gli Attestati di Wallet in formato JWT, SD-JWT e mdoc firmati dal Fornitore di Wallet. L'Attestato di Wallet in formato JWT deve essere utilizzato per la fase di Emissione, come Attestato Client OAuth, e sarà inviato al Credential Issuer come discusso in :ref:`credential-issuance:Emissione di Attestati Elettronici`. L'Attestato di Wallet in formato SD-JWT e mdoc sarà invece utilizzato durante la presentazione rispettivamente nei flussi remoto (:ref:`remote-flow:Flusso Remoto`) e di prossimità (:ref:`proximity-flow:Flusso di Prossimità`).


L'Oggetto JSON restituito nella risposta ha il seguente claim:

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Parametro**
      - **Descrizione**
      - **Riferimento**
    * - **wallet_attestations**
      - OBBLIGATORIO. Contiene un array di uno o più Attestati di Wallet emessi. Gli elementi dell'array DEVONO essere Oggetti JSON. Devono essere presenti almeno due Oggetti JSON.
      - Questa specifica.

Ogni Oggetto JSON contenuto nell'array ``wallet_attestations`` DEVE avere la seguente forma:

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Parametro**
      - **Descrizione**
      - **Riferimento**
    * - **format**
      - Una stringa che identifica il Modello di Dati utilizzato per creare e rappresentare l'Attestato di Wallet. DEVE essere ``jwt``, ``dc+sd-jwt`` o ``mso_mdoc`` a seconda del formato della Credenziale.
      - Questa specifica.
    * - **wallet_attestation**
      - Una stringa che rappresenta l'Attestato di Wallet. Se

        - l'Attestato di Wallet è in formato JWT, allora il valore del claim DEVE essere una stringa che è un JWT.
        - l'Attestato di Wallet è in formato SD-JWT, allora il valore del claim DEVE essere una stringa che è un SD-JWT VC.
        - l'Attestato di Wallet è in formato mdoc, allora il valore del claim è la rappresentazione codificata in base64url della struttura IssuerSigned codificata in CBOR, come definito in [ISO.18013-5]. Questa struttura DEVE contenere tutti i Namespace e gli IssuerSignedItems inclusi nel MobileSecurityObject.

      - Questa specifica.

Se si verificano errori durante il processo, viene restituita una risposta di errore. Ulteriori dettagli sulla risposta di errore sono forniti nella sezione :ref:`mobile-application-instance:Risposta di Errore di Associazione Chiave dell'Applicazione Mobile`.


JWT dell'Attestato di Wallet
""""""""""""""""""""""""""""

L'header JOSE del JWT dell'Attestato di Wallet contiene i seguenti parametri:

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
      - OBBLIGATORIO. Identificatore univoco della chiave pubblica associata alla chiave privata che il Fornitore di Wallet ha utilizzato per firmare l'Attestato di Wallet.
      - :rfc:`7638#section_3`.
    * - **typ**
      - OBBLIGATORIO. DEVE essere impostato su ``oauth-client-attestation+jwt``
      - `OPENID4VC-HAIP`_.
    * - **trust_chain**
      - OBBLIGATORIO. Sequenza di Entity Statement che compone la Catena di Fiducia relativa al Fornitore di Wallet.
      - `OID-FED`_ Sezione 4.3 *Trust Chain Header Parameter*.
    * - **x5c**
      - OPZIONALE. Contiene il certificato di chiave pubblica X.509 o la catena di certificati (:rfc:`5280`) corrispondente alla chiave utilizzata per firmare digitalmente il JWT.
      - :rfc:`7515` Sezione 4.1.8 e `SD-JWT-VC`_ Sezione 3.5.

Il corpo del JWT dell'Attestato di Wallet contiene i seguenti claim:

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
      - OBBLIGATORIO. Identificatore dell'Istanza di Wallet che è l'impronta digitale della JWK dell'Attestato di Wallet.
      - :rfc:`9126` e :rfc:`7519`.
    * - **aal**
      - OBBLIGATORIO. Stringa JSON che attesta il livello di autenticazione del Wallet e della chiave come affermato nel claim cnf.
      - Questa specifica.

Di seguito è riportato un esempio non normativo dell'header e del payload dell'Attestato di Wallet SD-JWT senza codifica e firma applicata:

.. code-block:: json

  {
    "alg": "ES256",
    "kid": "5t5YYpBhN-EgIEEI5iUzr6r0MR02LnVQ0OmekmNKcjY",
    "trust_chain": [
      "eyJhbGciOiJFUz...6S0A",
      "eyJhbGciOiJFUz...jJLA",
      "eyJhbGciOiJFUz...H9gw",
    ],
    "typ": "jwt"
  }

.. code-block:: json

  {
    "iss": "https://wallet-provider.example.org",
    "cnf":
    {
      "jwk":
      {
        "crv": "P-256",
        "kty": "EC",
        "x": "4HNptI-xr2pjyRJKGMnz4WmdnQD_uJSq4R95Nj98b44",
        "y": "LIZnSB39vFJhYgS3k7jXE4r3-CoGFQwZtPBIRqpNlrg"
      }
    },
    "iat": 1687281195,
    "exp": 1687288395,
    "vct": "wallet.atestation.example/v1.0",
    "sub": "vbeXJksM45xphtANnCiG6mCyuU4jfGNzopGuKvogg9c",
    "aal": "https://trust-list.eu/aal/high",
    "wallet_name": "Wallet_v1",
    "wallet_link": "https://example.com/wallet/detail_info.html"
  }


SD-JWT dell'Attestato di Wallet
"""""""""""""""""""""""""""""""

L'header JOSE dell'SD-JWT dell'Attestato di Wallet DEVE contenere i seguenti parametri:

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
      - OBBLIGATORIO. Identificatore univoco della chiave pubblica associata alla chiave privata che il Fornitore di Wallet ha utilizzato per firmare l'Attestato di Wallet.
      - :rfc:`7638#section_3`.
    * - **typ**
      - OBBLIGATORIO. DEVE essere impostato su ``dc+sd-jwt``
      - `OPENID4VC-HAIP`_.
    * - **trust_chain**
      - OBBLIGATORIO. Sequenza di Entity Statement che compone la Catena di Fiducia relativa al Fornitore di Wallet.
      - `OID-FED`_ Sezione 4.3 *Trust Chain Header Parameter*.
    * - **x5c**
      - OPZIONALE. Contiene il certificato di chiave pubblica X.509 o la catena di certificati (:rfc:`5280`) corrispondente alla chiave utilizzata per firmare digitalmente il JWT.
      - :rfc:`7515` Sezione 4.1.8 e `SD-JWT-VC`_ Sezione 3.5.

Il corpo dell'SD-JWT dell'Attestato di Wallet contiene i seguenti claim:

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
      - OBBLIGATORIO. Il valore del tipo di Credenziale DEVE essere una Stringa URL HTTPS e DEVE essere impostato su ``wallet.atestation.example/v1.0``.
      - Sezione 3.2.2.2 `SD-JWT-VC`_.
    * - **_sd**
      - OBBLIGATORIO. Array JSON contenente un elenco di tutti i digest delle divulgazioni.
      - `SD-JWT`_.
    * - **_sd_alg**
      - OBBLIGATORIO. Stringa contenente l'algoritmo di hash utilizzato dal Fornitore di Wallet per generare i digest delle divulgazioni.
      - `SD-JWT`_.
    * - **sub**
      - OBBLIGATORIO. Identificatore dell'Istanza di Wallet che è l'impronta digitale della JWK dell'Attestato di Wallet.
      - :rfc:`9126` e :rfc:`7519`.
    * - **aal**
      - OBBLIGATORIO. Stringa JSON che attesta il livello di autenticazione del Wallet e della chiave come affermato nel claim cnf.
      - Questa specifica.

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

Di seguito sono descritti esempi di valori per le divulgazioni:

**Claim** ``wallet_link``:

- Hash SHA-256: ``cD9/XC7t7QVHvmSiE1dGW0WYr0jcqm8n0GA6MGitaik=``
- Divulgazione: ``WyIyR0xDNDJzS1F2ZUNmR2ZyeU5STjl3IiwgIndhbGxldF9saW5rIiwgImh0dHBzOi8vZXhhbXBsZS5jb20vd2FsbGV0L2RldGFpbF9pbmZvLmh0bWwiXQ==``
- Contenuti: ``["2GLC42sKQveCfGfryNRN9w", "wallet_link", "https://example.com/wallet/detail_info.html"]``

**Claim** ``wallet_name``:

- Hash SHA-256: ``iQQhzf6+saYCzHH92N1QyJisKsZbApbTrJ1amHgLoOk=``
- Divulgazione:n``WyIyR0xDNDJzS1F2ZUNmR2ZyeU5STjl3IiwgIndhbGxldF9uYW1lIiwgIldhbGxldF9Ib2JiaXRvbl92MSJd``
- Contenuti: ``["2GLC42sKQveCfGfryNRN9w", "wallet_name", "Wallet_v1"]``

Di seguito è riportato un esempio non normativo dell'header e del payload dell'Attestato di Wallet SD-JWT senza codifica e firma applicata:

.. code-block:: json

  {
    "alg": "ES256",
    "kid": "5t5YYpBhN-EgIEEI5iUzr6r0MR02LnVQ0OmekmNKcjY",
    "trust_chain": [
      "eyJhbGciOiJFUz...6S0A",
      "eyJhbGciOiJFUz...jJLA",
      "eyJhbGciOiJFUz...H9gw"
    ],
    "typ": "dc+sd-jwt"
  }

.. code-block:: json

  {
    "iss": "https://wallet-provider.example.org",
    "cnf": {
      "jwk":
      {
        "crv": "P-256",
        "kty": "EC",
        "x": "4HNptI-xr2pjyRJKGMnz4WmdnQD_uJSq4R95Nj98b44",
        "y": "LIZnSB39vFJhYgS3k7jXE4r3-CoGFQwZtPBIRqpNlrg"
      }
    },
    "_sd": ["cD9/XC7t7QVHvmSiE1dGW0WYr0jcqm8n0GA6MGitaik=", "iQQhzf6+saYCzHH92N1QyJisKsZbApbTrJ1amHgLoOk="],
    "_sd_alg": "sha-256",
    "iat": 1687281195,
    "exp": 1687288395,
    "vct": "https://wallet.attestation.example/v1.0",
    "sub": "vbeXJksM45xphtANnCiG6mCyuU4jfGNzopGuKvogg9c",
    "aal": "https://trust-framework.example.it/aal/high"
  }

Attestato di Wallet mdoc
""""""""""""""""""""""""

Questa descrizione specializza ulteriormente le linee guida fornite in ref:`pid-eaa-data-model:MDOC-CBOR Credential Format` per rappresentare l'Attestato di Wallet in formato mdoc. Quest'ultimo DEVE:

- Avere il namespace domestico ``org.iso.18013.5.1.it``;
- Avere **docType** impostato su ``org.iso.18013.5.1.it.WalletAttestation``; e
- Avere **issuerAuth** come descritto in :ref:`credential-data-model:Mobile security Object`.

I ``nameSpaces`` per gli Oggetti Json del nameSpace domestico sono definiti come segue:

.. list-table:: org.iso.18013.5.1.it
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **elementIdentifier**
      - **Descrizione**
      - **Riferimento**
    * - **sub**
      - OBBLIGATORIO. Identificatore dell'Istanza di Wallet che è l'impronta digitale della Chiave COSE dell'Attestato di Wallet.
      - :rfc:`9126` e :rfc:`7519`.
    * - **aal**
      - Stringa JSON che attesta il livello di autenticazione dell'Istanza di Wallet in relazione alla Chiave COSE contenuta nel claim ``IssuerAuth.deviceKeyInfo.deviceKey`` dell'Oggetto **issuerAuth**.
      - :rfc:`9679`.
    * - **wallet_link**
      - Stringa JSON contenente un URL per ottenere ulteriori informazioni sul Wallet e sul Fornitore di Wallet.
      - `OpenID4VCI`_.
    * - **wallet_name**
      - Stringa JSON, DEVE essere l'Identificatore del Fornitore di Wallet.
      - `OpenID4VCI`_.

Di seguito è riportato un esempio non normativo dell'Attestato di Wallet mdoc in notazione diagnostica CBOR:

.. code-block:: text

  {
    "docType": "org.iso.18013.5.1.it.WalletAttestation",
    "issuerSigned":{
      "nameSpaces":{
        "org.iso.18013.5.1.it":[
          24(<< {
          "digestID": 0,
          "random": h'960CB15A…E902807AA95',
          "elementIdentifier": "wallet_name",
          "elementValue": "Wallet_v1"
          } >>),
          24(<<
          {
          "digestID": 1,
          "random": h'9D3774BD59…A4F76A',
          "elementIdentifier": "wallet_link",
          "elementValue":"https://example.com/wallet/detail_info.html"
          } >>),
          24(<< {
          "digestID": 2,
          "random": h'AE84834F3…A3E4FCCE',
          "elementIdentifier": "sub",
          "elementValue":"vbeXJksM45xphtANnCiG6mCyuU4jfGNzopGuKvogg9c"
          } >>),
          24(<<
          {
          "digestID": 3,
          "random": h'9D3774BD59…A4F76A',
          "elementIdentifier": "aal",
          "elementValue":"https://trust-list.eu/aal/high"
          } >>)
        ]
  },
    "issuerAuth": [
      << {1: -7} >>,
      {
      33: h'30820215308201BCA003020102021404AD30C…'
      },
      <<
        24(<<
          {
            "docType":"org.iso.18013.5.1.it.WalletAttestation",
            "version": "org.iso.18013.5.1.it",
            "validityInfo": {
              "signed": "2023-02-22T06:23:56Z"
              "validFrom": "2023-02-22T06:23:56Z",
              "validUntil": "2024-02-22T00:00:00Z"
            },
            "valueDigests": {
              "org.iso.18013.5.1.it": {
                0: h'0F1571A988FCDF2929…',
                1: h'0CDFE0774A2B596C90…',
                2: h'E23821492558984395…',
                3: h'BBC77E6CCE544EDF86…'
              }
            },
            "deviceKeyInfo": {
              "deviceKey": {
                1: 2,
                -1: 1,
                -2: h'B820963964E5…',
                -3: h'0A6DA0AF437E…'
              }
            },
            "digestAlgorithm": "SHA-256"
          }
        >>)
      >>,
      h'1AD0D6A7313EFDC…43DEBF48BF5A580D'
    ]
  }


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

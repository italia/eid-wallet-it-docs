.. include:: ../common/common_definitions.rst

.. "included" file, so we start with '-' title level

.. role:: raw-html(raw)
  :format: html


Endpoint del Signal Hub PDND
-----------------------------
All'interno della piattaforma PDND, il Signal Hub funge da intermediario tra un Provider PDND e i suoi Consumer PDND per segnalare variazioni dei dati. Per raggiungere questo obiettivo, il gestore della piattaforma PDND, di seguito denominato PDND Manager, fornisce (svolgendo il ruolo di PDND e-Service Provider) due e-Service del Signal Hub PDND:
  - l'e-Service di Raccolta Segnali che viene utilizzato dai PDND e-Service Provider per depositare i Segnali, poiché il PDND e-Service Provider agisce come Consumer dell'e-Service di Raccolta Segnali;
  - l'e-Service di Distribuzione Segnali che viene utilizzato dai PDND e-Service Consumer per recuperare i Segnali raccolti, poiché il PDND e-Service Consumer agisce anche come Consumer dell'e-Service di Distribuzione Segnali.

Al fine di proteggere la privacy del soggetto del Segnale, il PDND Manager richiede a ciascun PDND e-Service Provider di pseudonimizzare l'identificatore del soggetto utilizzato all'interno dei Segnali e di configurare un endpoint di pseudonimizzazione per il proprio PDND e-Service. Questo endpoint di pseudonimizzazione viene utilizzato dagli e-Service Consumer per ottenere l'algoritmo di pseudonimizzazione al fine di calcolare il Pseudonimo del soggetto del Segnale. Solo il PDND e-Service Provider e i suoi PDND e-Service Consumer sono in grado di collegare un Segnale ai dati personali del soggetto, mentre il PDND Manager gestisce solo identificatori pseudonimizzati.

Per specifiche tecniche dettagliate e linee guida per l'implementazione, si prega di fare riferimento alla `Signal Hub Guide`_.

Nel contesto dell'IT Wallet, le Fonti Autentiche interagiscono con il Signal Hub per notificare ai Credential Issuer i cambiamenti nello stato e/o nel valore degli Attributi associati alle Credenziali Digitali. Nello specifico,
  - la Fonte Autentica depositerà i Segnali nel Signal Hub, svolgendo quindi il ruolo di PDND Consumer dell'e-Service di Raccolta Segnali;
  - il Credential Issuer recupererà i Segnali dal Signal Hub, e svolgerà quindi il ruolo di PDND e-Service Consumer dell'e-Service di Distribuzione Segnali.

.. note::
  Nel contesto dell'IT Wallet, a causa della particolare natura dei dati scambiati, la pseudonimizzazione del soggetto del Segnale non è necessaria poiché è già un identificatore opaco non correlato al soggetto della Credenziale Digitale. Pertanto, la Fonte Autentica non ha bisogno di configurare un endpoint di pseudonimizzazione per i suoi e-Service.

Le Fonti Autentiche che utilizzano PDND devono utilizzare gli e-Service del Signal Hub.

Di seguito viene fornita la descrizione di come le Fonti Autentiche e i Credential Issuer interagiscono con gli e-Service del Signal Hub insieme ai formati dettagliati delle richieste e delle risposte.

Prerequisiti
^^^^^^^^^^^^
Prima di utilizzare il Signal Hub, tutte le Fonti Autentiche DEVONO:

  - essersi registrate come Provider del loro e-Service presso il PDND;
  - essersi registrate come Consumer dell'e-Service di Raccolta Segnali del Signal Hub;

Prima di utilizzare il Signal Hub, tutti i Credential Issuer DEVONO:

  - essersi registrati come Consumer degli e-Service delle Fonti Autentiche pertinenti;
  - essersi registrati come Consumer dell'e-Service di Distribuzione Segnali del Signal Hub;

e-Service del Signal Hub
^^^^^^^^^^^^^^^^^^^^^^^^
Questa sezione descrive gli endpoint disponibili per gli e-Service di Raccolta e Distribuzione del Signal Hub, incluse le loro funzionalità e i formati di richiesta e risposta previsti.

e-Service di Raccolta Segnali
"""""""""""""""""""""""""""""

Le Fonti Autentiche nell'ecosistema IT Wallet utilizzano l'e-Service di Raccolta Segnali per:

  - notificare al Credential Issuer un cambiamento di stato e/o valore di un Attributo specifico associato a una Credenziale Digitale emessa dal Credential Issuer;
  - notificare al Credential Issuer la disponibilità degli Attributi relativi a una Credenziale Digitale specifica che un Utente ha richiesto nel suo Wallet.

L'ultimo caso, denominato emissione differita, si verifica quando il Credential Issuer ha richiesto gli Attributi di una Credenziale Digitale dalla Fonte Autentica (invocando l'endpoint PDND :ref:`authentic-source-endpoint:Ottenere gli Attributi dell'Utente`) e la Fonte Autentica non può rispondere immediatamente con gli Attributi richiesti. Pertanto, la Fonte Autentica notifica al Credential Issuer tramite il Signal Hub in un momento successivo che gli Attributi richiesti sono ora disponibili.

L'endpoint dell'e-Service di Raccolta Segnali viene utilizzato dalle Fonti Autentiche per depositare i Segnali nel Signal Hub tramite una richiesta di Raccolta Segnali. Quest'ultima DEVE essere una richiesta POST con ``Content-Type`` impostato su ``application/json``, il cui header DEVE avere i parametri descritti nella `Signal Hub Guide`_ e il cui body DEVE contenere i seguenti parametri:

.. _table_Signal_deposit_request_parameters:
.. list-table::
  :widths: 25 75
  :header-rows: 1

  * - **Nome Parametro**
    - **Descrizione**
  * - **signalId**
    - OBBLIGATORIO. Un numero intero positivo a 64 bit che fa riferimento all'identificatore del Segnale in ordine cronologico.
  * - **objectType**
    - OBBLIGATORIO. Questo campo è un campo libero che la Fonte Autentica PUÒ utilizzare per specificare ulteriormente il Segnale.
  * - **objectId**
    - OBBLIGATORIO. Il soggetto a cui è legato il Segnale. Se il Segnale ha ``signalType``:
    
      - ``CREATE``, allora DEVE essere impostato sul valore ``jti`` che il Credential Issuer ha utilizzato nel token Agid-JWT-Signature della richiesta `get attributes` alla Fonte Autentica per ottenere gli Attributi relativi a una Credenziale Digitale specifica (vedere :ref:`authentic-source-endpoint:Ottenere gli Attributi dell'Utente`);
      - ``UPDATE``, allora DEVE essere impostato sull'identificatore univoco del database della Fonte Autentica degli Attributi della Credenziale Digitale a cui si riferisce il Segnale.
      
  * - **signalType**
    - OBBLIGATORIO. Tipo di Segnale. DEVE essere uno dei seguenti:

      - ``UPDATE``, quando il Segnale si riferisce a un cambiamento nello stato e/o valore di un Attributo specifico associato a una Credenziale Digitale;
      - ``CREATE``, quando il Segnale si riferisce alla disponibilità degli Attributi di una Credenziale Digitale specifica;

  * - **eserviceId**
    - OBBLIGATORIO. e-Service a cui è legato il Segnale. DEVE corrispondere al valore dell'Id dell'e-Service di cui la Fonte Autentica è Provider.

.. note::
  Nel flusso di emissione differita, cioè quando la Fonte Autentica notifica al Credential Issuer la disponibilità degli Attributi della Credenziale Digitale tramite Signal Hub; entrambe le entità DEVONO tenere traccia del valore ``jti`` del Credential Issuer utilizzato nell'Agid-JWT-Signature della richiesta ``get attributes``. Questo è necessario poiché l'``objectId`` del Segnale DEVE essere impostato su quel valore ``jti`` quando il Segnale ha ``signalType`` ``CREATE``.

Un esempio non normativo di richiesta di Raccolta Segnali può essere trovato in `Signal Hub push`_.

La risposta dell'e-Service di Raccolta Segnali, che conferma la corretta analisi della richiesta, è specificata in `Signal Hub push`_, e ha ``Content-Type`` impostato su ``application/json``. Il payload contiene il parametro del body:

.. _table_Signal_deposit_response_parameters:
.. list-table::
  :widths: 25 75
  :header-rows: 1

  * - **Nome Parametro**
    - **Descrizione**
  * - **signalId**
    - OBBLIGATORIO. L'identificatore del Segnale che è stato raccolto con successo dall'e-Service di Raccolta Segnali.

Se si verifica un errore durante l'analisi della richiesta, la risposta DEVE aderire al formato di errore definito in `Signal Hub push-yaml`_.

.. note::
    Una Specifica OpenAPI completa dell'e-Service di Raccolta Segnali è disponibile in `Signal Hub push-yaml`_.

La Fonte Autentica DEVE implementare la logica necessaria per gestire le richieste all'endpoint dell'e-Service di Raccolta Segnali, nel fare ciò deve considerare i seguenti aspetti:

  - I Segnali vengono inviati per e-Service PDND, pertanto la Fonte Autentica DOVREBBE implementare un ciclo di deposito Segnali per ogni ID e-Service di cui è Provider PDND;
  - I Segnali sono etichettati da un identificatore univoco, il ``signalId``, che è un numero intero positivo a 64 bit. Il ``signalId`` DEVE essere incrementato di 1 per ogni nuovo Segnale che la Fonte Autentica desidera depositare nell'endpoint dell'e-Service di Raccolta Segnali. Spetta alla Fonte Autentica tenere traccia dell'ultimo ``signalId`` che ha inviato. I Segnali con valori ``signalId`` più bassi sono considerati più vecchi dall'endpoint dell'e-Service di Raccolta Segnali e genereranno un errore quando ricevuti.

e-Service di Distribuzione Segnali
"""""""""""""""""""""""""""""""""""
I Credential Issuer nell'ecosistema IT Wallet utilizzano l'e-Service di Distribuzione Segnali per:

  - verificare i cambiamenti nello stato e/o valore di un Attributo specifico associato a una Credenziale Digitale emessa dal Credential Issuer stesso;
  - verificare la disponibilità degli Attributi relativi a una Credenziale Digitale richiesta da un Utente.

L'endpoint dell'e-Service di Distribuzione Segnali viene utilizzato dai Credential Issuer per recuperare i Segnali dal Signal Hub tramite una richiesta di Distribuzione Segnali. Quest'ultima DEVE essere una richiesta GET e DEVE avere i seguenti parametri:

  - Parametri del Percorso:
    
    -  ``eserviceId``. OBBLIGATORIO. e-Service a cui è legato il Segnale. DEVE corrispondere al valore dell'Id dell'e-Service di cui il Credential Issuer è Consumer.

  - Parametri di Query:

    - ``signalId``. OPZIONALE. Intero che rappresenta l'ultimo numero di Segnale elaborato dal Credential Issuer. L'e-Service di Distribuzione Segnali risponderà con Segnali aventi valori ``signalId`` progressivamente maggiori. Se non specificato, il valore predefinito è il valore ``signalId`` più basso disponibile nell'e-Service di Distribuzione Segnali.
    - ``size``. OPZIONALE. Intero che rappresenta il numero massimo di Segnali da restituire nella risposta di Distribuzione Segnali. Se non specificato, il valore predefinito è ``10``.

  - Parametri degli Header: questi sono quelli descritti in `Signal Hub pull`_.

Se la richiesta di Distribuzione Segnali viene elaborata correttamente, l'e-Service risponderà con codice di stato

 - HTTP 200 OK se la richiesta è formata correttamente e non ci sono più Segnali da richiedere;
 - HTTP 206 OK se la richiesta è formata correttamente ma ci sono più Segnali da richiedere.

Indipendentemente dal codice di risposta utilizzato, la risposta ha ``Content-Type`` impostato su ``application/json`` e i parametri dell'header indicati in `Signal Hub pull`_. Il parametro del body ``lastSignalId``, che fa riferimento al ``signalId`` dell'ultimo Segnale trasmesso dall'e-Service di Distribuzione Segnali, viene aggiunto al payload della risposta.

In `Signal Hub pull`_ si possono trovare esempi non normativi di richieste e risposte di Distribuzione Segnali.

Se si verifica un errore durante l'analisi della richiesta, la risposta DEVE aderire al formato di errore definito in `Signal Hub pull-yaml`_.

.. note::
  Una Specifica OpenAPI completa dell'e-Service di Raccolta Segnali è disponibile in `Signal Hub pull-yaml`_.

Il Credential Issuer DEVE implementare la logica necessaria per gestire il Polling dell'endpoint dell'e-Service di Distribuzione Segnali, nel fare ciò deve considerare i seguenti aspetti:

  - I Segnali vengono interrogati e recuperati per e-Service PDND, il che significa che il Credential Issuer DEVE implementare un ciclo di polling per ogni ID e-Service;
  - il periodo di conservazione dei Segnali nel Signal Hub è specificato nella `Signal Hub Guide`_. I Segnali più vecchi del periodo di conservazione specificato non sono disponibili per il recupero;
  - il Signal Hub non tiene traccia dell'ultimo ``signalId`` notificato a un Credential Issuer specifico. Ogni Credential Issuer DEVE tenere traccia dell'ultimo ``signalId`` che ha ricevuto per ogni ID e-Service PDND;
  - l'endpoint dell'e-Service di Distribuzione Segnali restituisce i Segnali in lotti. La dimensione massima del lotto è specificata nella `Signal Hub Guide`_. L'e-Service di Distribuzione Segnali indicherà se sono disponibili Segnali aggiuntivi per il recupero.

Elaborazione dei Segnali
^^^^^^^^^^^^^^^^^^^^^^^^
Dopo che i Segnali sono stati recuperati con successo dal Credential Issuer, quest'ultimo DEVE elaborarli come segue:

  - Per ogni Segnale, il Credential Issuer DEVE verificare il valore ``SignalType``:
    
    - se il ``SignalType`` del Segnale è ``UPDATE``, lo stato e/o il valore dell'Attributo associato a una Credenziale Digitale necessitano di aggiornamenti;
    - se il ``SignalType`` del Segnale è ``CREATE``, gli Attributi richiesti di una Credenziale Digitale specifica sono ora disponibili;

    Se l'``objectId`` non corrisponde ad alcun identificatore valido noto al Credential Issuer, il Segnale DEVE essere ignorato. Altrimenti, se corrisponde a un identificatore noto e valido, il Credential Issuer DEVE utilizzare l'endpoint PDND :ref:`authentic-source-endpoint:Ottenere gli Attributi dell'Utente` della Fonte Autentica per recuperare le informazioni aggiornate e, se necessario, applicare il nuovo stato alla Credenziale corrispondente.
    
    Quando il Segnale è stato elaborato, il Credential Issuer passerà al Segnale successivo e aggiornerà il suo contatore ``signalId``; oppure, se non ci sono più Segnali da elaborare, riprenderà il ciclo di Pull.

.. warning::

  Dati i pattern di sicurezza attualmente supportati dal Signal Hub, se la Fonte Autentica richiede il pattern di sicurezza `AUDIT_REST_02` dal Credential Issuer, quest'ultimo DEVE revocare la Credenziale Digitale referenziata nei Segnali con ``signalType`` ``UPDATE`` poiché non può contattare la Fonte Autentica per recuperare le informazioni aggiornate senza aver prima autenticato l'Utente.

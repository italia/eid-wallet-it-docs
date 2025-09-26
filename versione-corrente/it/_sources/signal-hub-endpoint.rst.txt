.. include:: ../common/common_definitions.rst

.. "included" file, so we start with '-' title level

.. role:: raw-html(raw)
  :format: html


Endpoint di PDND Signal Hub
-----------------------------
All'interno della piattaforma PDND, Signal Hub funge da intermediario tra un Provider PDND e i suoi Consumer PDND per facilitare le segnalazioni di variazioni dei dati. Per abilitare tale funzionalità, il gestore della piattaforma PDND, di seguito denominato PDND Manager, agendo come PDND e-Service Provider, fornisce due e-Service PDND di Signal Hub:
  - l'e-Service di Raccolta Segnali che viene utilizzato dai PDND e-Service Provider per depositare i Segnali; in questo caso, il PDND e-Service Provider agisce come Consumer dell'e-Service di Raccolta Segnali;
  - l'e-Service di Distribuzione Segnali che viene utilizzato dai PDND e-Service Consumer per recuperare i Segnali raccolti; in questo caso, il PDND e-Service Consumer agisce anche come Consumer dell'e-Service di Distribuzione Segnali.

Al fine di proteggere la privacy del soggetto del Segnale, il PDND Manager richiede a ciascun PDND e-Service Provider di pseudonimizzare l'identificativo del soggetto utilizzato all'interno dei Segnali e di configurare un endpoint di pseudonimizzazione per il proprio PDND e-Service. Questo endpoint di pseudonimizzazione viene utilizzato dagli e-Service Consumer per ottenere l'algoritmo di pseudonimizzazione al fine di calcolare lo Pseudonimo del soggetto del Segnale. Solo il PDND e-Service Provider e i suoi PDND e-Service Consumer sono in grado di collegare un Segnale ai dati personali del soggetto, mentre il PDND Manager gestisce solo gli identificativi pseudonimizzati.

Per specifiche tecniche dettagliate e linee guida per l'implementazione, si prega di fare riferimento alla `Signal Hub Guide`_.

Nel contesto dell'IT Wallet, le Fonti Autentiche interagiscono con Signal Hub per notificare ai Fornitori di Attestati Elettronici i cambiamenti nello stato e/o nel valore degli Attributi associati agli Attestati Elettronici. Nello specifico,
  - la Fonte Autentica depositerà i Segnali in Signal Hub, svolgendo quindi il ruolo di PDND Consumer dell'e-Service di Raccolta Segnali;
  - il Fornitore di Attestati Elettronici recupererà i Segnali da Signal Hub, e svolgerà quindi il ruolo di PDND e-Service Consumer dell'e-Service di Distribuzione Segnali.

.. note::
  Nel contesto dell'IT Wallet, a causa della particolare natura dei dati scambiati, la pseudonimizzazione del soggetto del Segnale non è necessaria poiché l'identificativo è già opaco e non correlato al soggetto dell'Attestato Elettronico. Pertanto, la Fonte Autentica non ha bisogno di configurare un endpoint di pseudonimizzazione per i suoi e-Service.

Le Fonti Autentiche che utilizzano PDND DEVONO utilizzare gli e-Service di Signal Hub.

Di seguito viene fornita la descrizione di come le Fonti Autentiche e i Fornitori di Attestati Elettronici interagiscono con gli e-Service di Signal Hub insieme ai formati dettagliati delle request e delle response.

Prerequisiti
^^^^^^^^^^^^
Prima di utilizzare Signal Hub, tutte le Fonti Autentiche DEVONO:

  - essersi registrate come Provider del loro e-Service presso PDND;
  - essersi registrate come Consumer dell'e-Service di Raccolta Segnali di Signal Hub;

Prima di utilizzare Signal Hub, tutti i Fornitori di Attestati Elettronici DEVONO:

  - essersi registrati come Consumer degli e-Service delle Fonti Autentiche pertinenti;
  - essersi registrati come Consumer dell'e-Service di Distribuzione Segnali di Signal Hub;

e-Service di Signal Hub
^^^^^^^^^^^^^^^^^^^^^^^^
Questa sezione descrive gli endpoint disponibili per gli e-Service di Raccolta e Distribuzione di Signal Hub, incluse le loro funzionalità e i formati di richiesta e risposta previsti.

e-Service di Raccolta Segnali
"""""""""""""""""""""""""""""

Le Fonti Autentiche nell'ecosistema IT Wallet utilizzano l'e-Service di Raccolta Segnali per:

  - notificare al Fornitore di Attestati Elettronici un cambiamento di stato e/o valore di un Attributo specifico associato a un Attestato Elettronico emesso dal Fornitore di Attestati Elettronici;
  - notificare al Fornitore di Attestati Elettronici la disponibilità degli Attributi relativi a un Attestato Elettronico specifico che un Utente ha richiesto nel suo Wallet.

L'ultimo caso, denominato *deferred issuance*, si verifica quando il Fornitore di Attestati Elettronici ha richiesto gli Attributi di un Attestato Elettronico dalla Fonte Autentica (invocando l'endpoint PDND :ref:`authentic-source-endpoint:Get Attribute Claims`) e la Fonte Autentica non può rispondere immediatamente con gli Attributi richiesti. Pertanto, la Fonte Autentica notifica al Fornitore di Attestati Elettronici tramite Signal Hub in un momento successivo che gli Attributi richiesti sono ora disponibili.

L'endpoint dell'e-Service di Raccolta Segnali viene utilizzato dalle Fonti Autentiche per depositare i Segnali in Signal Hub tramite una request di Raccolta Segnali. Quest'ultima DEVE essere una richiesta POST con ``Content-Type`` impostato su ``application/json``, il cui header DEVE avere i parametri descritti nel `Signal Hub Guide`_ e il cui body DEVE contenere i seguenti parametri:

.. _table_Signal_deposit_request_parameters:
.. list-table::
  :widths: 25 75
  :header-rows: 1

  * - **Nome Parametro**
    - **Descrizione**
  * - **signalId**
    - OBBLIGATORIO. Numero intero positivo a 64 bit identificativo del Segnale.
  * - **objectType**
    - OBBLIGATORIO. Questo è un campo libero che la Fonte Autentica PUÒ utilizzare per specificare ulteriormente il Segnale.
  * - **objectId**
    - OBBLIGATORIO. Il soggetto a cui è legato il Segnale. Se il Segnale ha ``signalType``:
    
      - ``CREATE``, allora DEVE essere impostato sul valore ``jti`` che il Fornitore di Attestati Elettronici ha utilizzato nel token Agid-JWT-Signature della richiesta `get attributes` alla Fonte Autentica per ottenere gli Attributi relativi a un Attestato Elettronico specifico (vedere :ref:`authentic-source-endpoint:Get Attribute Claims`);
      - ``UPDATE``, allora DEVE essere impostato sull'identificatore univoco del database della Fonte Autentica degli Attributi dell'Attestato Elettronico a cui si riferisce il Segnale.
      
  * - **signalType**
    - OBBLIGATORIO. Tipo di Segnale. DEVE essere uno dei seguenti:

      - ``UPDATE``, quando il Segnale si riferisce a un cambiamento nello stato e/o valore di un Attributo specifico associato a un Attestato Elettronico;
      - ``CREATE``, quando il Segnale si riferisce alla disponibilità degli Attributi di un Attestato Elettronico specifico;

  * - **eserviceId**
    - OBBLIGATORIO. e-Service a cui è legato il Segnale. DEVE corrispondere al valore dell'Id dell'e-Service di cui la Fonte Autentica è Provider.

.. note::
  Nel Deferred Issuance Flow, cioè quando la Fonte Autentica notifica al Fornitore di Attestati Elettronici la disponibilità degli Attributi dell'Attestato Elettronico tramite Signal Hub; entrambe le entità DEVONO tenere traccia del valore ``jti`` del Fornitore di Attestati Elettronici utilizzato nell'Agid-JWT-Signature della richiesta `get attributes`. Questo è necessario poiché l'``objectId`` del Segnale DEVE essere impostato su quel valore ``jti`` quando il Segnale ha ``signalType`` valorizzato con ``CREATE``.

Un esempio non normativo di richiesta di richiesta di Raccolta Segnali può essere trovato nel `Signal Hub push`_.

La response dell'e-Service di Raccolta Segnale è specificata nel `Signal Hub push`_ e ha ``Content-Type`` impostato su ``application/json``. Il payload contiene il parametro del body:

.. _table_Signal_deposit_response_parameters:
.. list-table::
  :widths: 25 75
  :header-rows: 1

  * - **Nome Parametro**
    - **Descrizione**
  * - **signalId**
    - OBBLIGATORIO. L'identificativo del Segnale che è stato raccolto con successo dall'e-Service di Raccolta Segnali.

Se si verifica un errore, la response DEVE aderire alla specifica definita nel `Signal Hub push-yaml`_.

.. note::
    Lna Specifica OpenAPI completa dell'e-Service di Raccolta Segnali è disponibile nel `Signal Hub push-yaml`_.

La Fonte Autentica DEVE implementare la logica necessaria per gestire le richieste all'endpoint dell'e-Service di Raccolta Segnali, nel fare ciò deve considerare i seguenti aspetti:

  - I Segnali vengono inviati per e-Service PDND, pertanto la Fonte Autentica DOVREBBE implementare un ciclo di deposito Segnali per ogni e-Service ID di cui è Provider PDND;
  - I Segnali sono etichettati da un identificativo univoco, il ``signalId``, che è un numero intero positivo a 64 bit. Il ``signalId`` DEVE essere incrementato di 1 per ogni nuovo Segnale che la Fonte Autentica desidera depositare nell'endpoint dell'e-Service di Raccolta Segnali. Spetta alla Fonte Autentica tenere traccia dell'ultimo ``signalId`` che ha inviato. I Segnali con valori ``signalId`` più bassi sono considerati più vecchi dall'endpoint dell'e-Service di Raccolta Segnali e genereranno un errore quando ricevuti.

e-Service di Distribuzione Segnali
"""""""""""""""""""""""""""""""""""
I Fornitori di Attestati Elettronici nell'ecosistema IT Wallet utilizzano l'e-Service di Distribuzione Segnali per:

  - verificare i cambiamenti nello stato e/o il valore di un Attributo specifico associato a un Attestato Elettronico emesso dal Fornitore di Attestati Elettronici stesso;
  - verificare la disponibilità degli Attributi relativi a un Attestato Elettronico richiesto da un Utente.

L'endpoint dell'e-Service di Distribuzione Segnali viene utilizzato dai Fornitori di Attestati Elettronici per recuperare i Segnali da Signal Hub tramite una richiesta di Distribuzione Segnali. Quest'ultima DEVE essere una richiesta HTTP con metodo GET e DEVE avere i seguenti parametri:

  - Parametri di Path:
    
    -  ``eserviceId``. OBBLIGATORIO. e-Service a cui è legato il Segnale. DEVE corrispondere al valore dell'Id dell'e-Service di cui il Fornitore di Attestati Elettronici è Consumer.

  - Parametri di Query:

    - ``signalId``. OPZIONALE. Intero che rappresenta l'ultimo numero di Segnale elaborato dal Fornitore di Attestati Elettronici. L'e-Service di Distribuzione Segnali risponderà con Segnali aventi valori ``signalId`` progressivamente maggiori. Se non specificato, il valore predefinito è il valore ``signalId`` più basso disponibile nell'e-Service di Distribuzione Segnali.
    - ``size``. OPZIONALE. Intero che rappresenta il numero massimo di Segnali da restituire nella risposta di Distribuzione Segnali. Se non specificato, il valore predefinito è ``10``.

  - Parametri degli Header: questi sono quelli descritti in `Signal Hub pull`_.

Se la richiesta di Distribuzione Segnali viene elaborata correttamente, l'e-Service risponderà con Status Code:

 - HTTP 200 OK se la richiesta è formata correttamente e non ci sono più Segnali da richiedere;
 - HTTP 206 OK se la richiesta è formata correttamente ma ci sono più Segnali da richiedere.

Indipendentemente dal codice di risposta utilizzato, la risposta ha ``Content-Type`` impostato su ``application/json`` e i parametri dell'header indicati nel `Signal Hub pull`_. Il parametro del body ``lastSignalId``, che fa riferimento al ``signalId`` dell'ultimo Segnale trasmesso dall'e-Service di Distribuzione Segnali, viene aggiunto al payload della risposta.

In `Signal Hub pull`_ si possono trovare esempi non normativi di richieste e risposte di Distribuzione Segnali.

Se si verifica un errore durante l'analisi della request, la risposta DEVE aderire al formato di errore definito in `Signal Hub pull-yaml`_.

.. note::
  La Specifica OpenAPI completa dell'e-Service di Raccolta Segnali è disponibile in `Signal Hub pull-yaml`_.

Il Fornitore di Attestati Elettronici DEVE implementare la logica necessaria per gestire il polling presso l'endpoint dell'e-Service di Distribuzione Segnali, nel fare ciò deve considerare i seguenti aspetti:

  - I Segnali vengono richiesti e recuperati per e-Service PDND, il che significa che il Fornitore di Attestati Elettronici DEVE implementare un ciclo di polling per ogni e-Service;
  - il periodo di conservazione dei Segnali in Signal Hub è specificato nella `Signal Hub Guide`_. I Segnali più vecchi del periodo di conservazione specificato non saranno disponibili per il recupero;
  - Signal Hub non tiene traccia dell'ultimo ``signalId`` notificato ai Fornitori di Attestati Elettronici. Ogni Fornitore di Attestati Elettronici DEVE tenere traccia dell'ultimo ``signalId`` che ha ricevuto per ogni e-Service ID PDND;
  - l'endpoint dell'e-Service di Distribuzione Segnali restituisce i Segnali in batch. La dimensione massima del batch è specificata nella `Signal Hub Guide`_. L'e-Service di Distribuzione Segnali indicherà se sono disponibili Segnali aggiuntivi per il recupero.

Elaborazione dei Segnali
^^^^^^^^^^^^^^^^^^^^^^^^
Dopo che i Segnali sono stati recuperati con successo dal Fornitore di Attestati Elettronici, quest'ultimo DEVE elaborarli come segue:

  - Per ogni Segnale, il Fornitore di Attestati Elettronici DEVE verificare il valore ``SignalType``:
    
    - se il ``SignalType`` del Segnale è ``UPDATE``, lo stato e/o il valore dell'Attributo associato a un Attestato Elettronico necessitano di aggiornamenti;
    - se il ``SignalType`` del Segnale è ``CREATE``, gli Attributi richiesti di un Attestato Elettronico specifico sono ora disponibili;

    Se l'``objectId`` non corrisponde ad alcun identificativo valido noto al Fornitore di Attestati Elettronici, il Segnale DEVE essere ignorato. Altrimenti, se corrisponde a un identificativo noto e valido, il Fornitore di Attestati Elettronici DEVE utilizzare l'endpoint PDND :ref:`authentic-source-endpoint:Get Attribute Claims` della Fonte Autentica per recuperare le informazioni aggiornate e, se possibile, applicare il nuovo stato/attributo all'Attestato Elettronico corrispondente.
    
    Quando il Segnale è stato elaborato, il Fornitore di Attestati Elettronici passerà al Segnale successivo e aggiornerà il suo contatore ``signalId``; oppure, se non ci sono più Segnali da elaborare, riprenderà il polling.

.. warning::

  Dati i pattern di sicurezza attualmente supportati da Signal Hub, se la Fonte Autentica richiede il pattern di sicurezza `AUDIT_REST_02` dal Fornitore di Attestati Elettronici, quest'ultimo DEVE revocare l'Attestato Elettronico referenziato nei Segnali con ``signalType`` ``UPDATE`` non potendo contattare la Fonte Autentica per recuperare le informazioni aggiornate senza aver prima autenticato l'Utente.

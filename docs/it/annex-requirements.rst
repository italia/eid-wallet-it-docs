Requisiti
=========

Questo allegato riporta tutti i requisiti identificati nel documento, organizzati in una tabella strutturata con le seguenti colonne:

- **ID**: codice univoco che identifica il requisito
- **Descrizione**: descrizione dettagliata del requisito
- **Audience**: soggetto responsabile dell'implementazione e del soddisfacimento del requisito
- **Categoria**: classificazione del requisito come Security o Privacy
- **Contesto**: ambito di applicazione del requisito


Requisiti Trust Framework
----------------------------

TBD


Requisiti Wallet Solution
----------------------------

TBD


Requisiti Credenziali Digitali
------------------------------

TBD


Requisiti Provider di Credenziali Digitali
--------------------------------------------

TBD


Requisiti Relying Party
---------------------------

TBD


Requisiti Metadati Relying Party
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

La seguente tabella elenca i requisiti con un identificatore univoco.

.. list-table::
    :class: longtable
    :widths: 20 80
    :header-rows: 1

    * - **ID**
      - **Requisito**
      - **Audience**
      - **Categoria**
      - **Contesto**

    * - RPMD-1
      - La Relying Party DEVE includere un parametro ``client_id`` contenente un URL HTTPS che identifica univocamente la RP nei metadati ``openid_credential_verifier``.
      - Relying Party
      - Entity Identification
      - Metadata Configuration
    * - RPMD-2
      - La Relying Party DEVE includere un parametro ``client_name`` contenente una stringa leggibile dall'uomo del nome della RP nei metadati ``openid_credential_verifier``.
      - Relying Party
      - Entity Identification
      - Metadata Configuration
    * - RPMD-3
      - La Relying Party DEVE includere un parametro ``application_type`` impostato al valore "web" nei metadati ``openid_credential_verifier``.
      - Relying Party
      - Entity Type
      - Metadata Configuration
    * - RPMD-4
      - La Relying Party DEVE includere un parametro ``request_uris`` contenente un Array JSON di valori ``request_uri`` che sono pre-registrati dalla RP, utilizzando lo schema https.
      - Relying Party
      - Security
      - Metadata Configuration
    * - RPMD-5
      - La Relying Party DEVE includere un parametro ``response_uris`` contenente un Array JSON di stringhe URI di risposta a cui l'Istanza del Wallet DEVE inviare la Risposta di Autorizzazione utilizzando una richiesta HTTP POST.
      - Relying Party
      - Security
      - Metadata Configuration
    * - RPMD-6
      - La Relying Party DEVE includere un parametro ``authorization_signed_response_alg`` che rappresenta l'algoritmo alg di firma che DEVE essere utilizzato per firmare le risposte di autorizzazione, escludendo l'algoritmo "none".
      - Relying Party
      - Security
      - Metadata Configuration
    * - RPMD-7
      - La Relying Party DEVE includere un parametro ``authorization_encrypted_response_alg`` che specifica l'algoritmo di crittografia asimmetrica all'Istanza del Wallet.
      - Relying Party
      - Security
      - Metadata Configuration
    * - RPMD-8
      - La Relying Party DEVE includere un parametro ``authorization_encrypted_response_enc`` che specifica l'algoritmo di crittografia simmetrica all'Istanza del Wallet.
      - Relying Party
      - Security
      - Metadata Configuration
    * - RPMD-9
      - La Relying Party DEVE includere un parametro ``vp_formats`` che definisce i formati e i tipi di prova delle Verifiable Presentations e Verifiable Credentials che la RP supporta, con almeno il supporto "dc+sd-jwt".
      - Relying Party
      - Security
      - Metadata Configuration
    * - RPMD-10
      - La Relying Party DEVE includere un parametro ``jwks`` contenente il documento JSON Web Key Set con le chiavi specifiche del protocollo.
      - Relying Party
      - Security
      - Metadata Configuration
    * - RPMD-11
      - La Relying Party DEVE includere un parametro ``erasure_endpoint`` quando richiede attributi che possono identificare univocamente gli Utenti, rappresentando l'URI per le richieste di cancellazione degli attributi degli Utenti.
      - Relying Party
      - Privacy
      - Metadata Configuration


Requisiti Flusso di Presentazione Remoto
----------------------------------------


La seguente tabella elenca i requisiti con un identificatore univoco.

.. list-table::
    :class: longtable
    :widths: 20 80
    :header-rows: 1

    * - **ID**
      - **Requisito**
      - **Audience**
      - **Categoria**
      - **Contesto**

    * - REMFLOW-1
      - La Relying Party DEVE ispezionare l'user-agent per determinare se il flusso avviene sullo stesso dispositivo o cross-device o chiedere all'Utente di selezionare manualmente il tipo di flusso.
      - Relying Party
      - Security
      - Presentation Initiation
    * - REMFLOW-2
      - La Relying Party DEVE supportare un flusso Same Device fornendo una posizione HTTP all'Istanza del Wallet utilizzando un redirect (302) o un href HTML in una pagina web.
      - Relying Party
      - Security
      - Presentation Initiation
    * - REMFLOW-3
      - La Relying Party DEVE supportare un flusso Cross Device fornendo un Codice QR che l'Utente inquadra con l'Istanza del Wallet.
      - Relying Party
      - Security
      - Presentation Initiation
    * - REMFLOW-4
      - Il Codice QR DEVE contenere un URL con i parametri ``client_id``, ``request_uri``, ``state``.
      - Relying Party
      - Security
      - Presentation Initiation
    * - REMFLOW-5
      - La Relying Party DEVE garantire un rate limiting appropriato per la generazione di codici QR o produrre Codici QR utilizzando JS all'interno dell'user-agent del Titolare.
      - Relying Party
      - Security
      - Presentation Initiation
    * - REMFLOW-6
      - La Relying Party DEVE associare il valore ``state`` all'user-agent utilizzando un metodo sicuro (es. cookie HTTP protetto).
      - Relying Party
      - Security
      - Presentation Initiation
    * - REMFLOW-7
      - La Relying Party DEVE rendere disponibile l'Authorization Request Object per il download alla posizione ``request_uri``.
      - Relying Party
      - Security
      - Request Processing
    * - REMFLOW-8
      - La Relying Party DEVE garantire che l'Authorization Request Object sia correttamente firmato e contenga tutti i claim richiesti.
      - Relying Party
      - Security
      - Request Processing
    * - REMFLOW-9
      - La Relying Party DEVE garantire una gestione appropriata dei timeout per la scansione dei codici QR.
      - Relying Party
      - Security
      - Flow Management
    * - REMFLOW-10
      - La Relying Party DEVE implementare una pulizia appropriata delle sessioni di autorizzazione scadute.
      - Relying Party
      - Security
      - Flow Management
    * - REMFLOW-11
      - La Relying Party DEVE fornire all'user-agent una pagina JavaScript per ispezionare l'endpoint di stato.
      - Relying Party
      - Security
      - Flow Management
    * - REMFLOW-12
      - L'Istanza del Wallet DEVE estrarre i parametri ``client_id``, ``request_uri``, ``state``, e opzionalmente ``request_uri_method``, dal payload.
      - Wallet Instance
      - Security
      - Request Processing
    * - REMFLOW-13
      - L'Istanza del Wallet DEVE stabilire la fiducia con la Relying Party prima di valutare il payload della richiesta.
      - Wallet Instance
      - Security
      - Trust Establishment
    * - REMFLOW-14
      - Se ``request_uri_method`` è impostato con il valore ``get`` o non presente, l'Istanza del Wallet DEVE recuperare il Request Object firmato utilizzando una richiesta HTTP con metodo GET all'endpoint fornito nel parametro ``request_uri``.
      - Wallet Instance
      - Security
      - Request Processing
    * - REMFLOW-15
      - Se ``request_uri_method`` è fornito e impostato con il valore ``post``, l'Istanza del Wallet DOVREBBE trasmettere le sue capacità (metadata del wallet) all'endpoint ``request_uri`` della Relying Party utilizzando il metodo HTTP POST.
      - Wallet Instance
      - Privacy
      - Request Processing
    * - REMFLOW-16
      - L'Istanza del Wallet DEVE verificare la firma del Request Object firmato utilizzando la chiave pubblica verificata, identificata nell'header JWT del Request Object e nella catena di fiducia relativa alla Relying Party.
      - Wallet Instance
      - Security
      - Request Validation
    * - REMFLOW-17
      - L'Istanza del Wallet DEVE verificare che il ``client_id`` contenuto nell'emittente del Request Object corrisponda a quello ottenuto al passo 2 e con l'identificatore della Relying Party all'interno della Catena di Fiducia.
      - Wallet Instance
      - Security
      - Request Validation
    * - REMFLOW-18
      - L'Istanza del Wallet DEVE valutare le Credenziali Digitali richieste e verificare l'idoneità della Relying Party nel richiedere queste applicando le policy relative a quella specifica Relying Party.
      - Wallet Instance
      - Privacy
      - Policy Enforcement
    * - REMFLOW-19
      - L'Istanza del Wallet DEVE chiedere la divulgazione e il consenso dell'Utente mostrando l'identità della Relying Party e gli attributi richiesti.
      - Wallet Instance
      - Privacy
      - User Consent
    * - REMFLOW-20
      - L'Istanza del Wallet DEVE garantire la trasmissione sicura di tutti i dati sensibili.
      - Wallet Instance
      - Security
      - Data Transmission
    * - REMFLOW-21
      - L'Istanza del Wallet DEVE presentare le informazioni richieste e l'Attestazione del Wallet (se richiesta) alla Relying Party, includendola all'interno dell'oggetto ``vp_token``.
      - Wallet Instance
      - Security
      - Credential Presentation
    * - REMFLOW-22
      - L'Istanza del Wallet DEVE informare l'Utente dell'autenticazione riuscita con la Relying Party.
      - Wallet Instance
      - Privacy
      - User Communication
    * - REMFLOW-23
      - Il valore ``redirect_uri`` DEVE essere utilizzato con un metodo HTTP GET dall'user-agent per reindirizzare l'Utente a un endpoint specifico della Relying Party.
      - User Agent
      - Security
      - Flow Completion
    * - REMFLOW-24
      - La Relying Party DEVE validare le Credenziali presentate verificando la fiducia con i loro Emittenti e controllare l'Attestazione del Wallet (se precedentemente richiesta e resa disponibile dall'Istanza del Wallet) per garantire che il Wallet Provider sia attendibile.
      - Relying Party
      - Security
      - Credential Validation
    * - REMFLOW-25
      - La Relying Party DEVE validare che la risposta provenga dalla stessa Istanza del Wallet che ha avviato il flusso.
      - Relying Party
      - Security
      - Response Validation
    * - REMFLOW-26
      - La Relying Party DEVE verificare l'integrità e l'autenticità di tutti i messaggi ricevuti.
      - Relying Party
      - Security
      - Response Validation
    * - REMFLOW-27
      - La Relying Party DEVE validare che tutti gli attributi richiesti siano presenti nella risposta.
      - Relying Party
      - Security
      - Response Validation
    * - REMFLOW-28
      - La Relying Party DEVE validare il formato e la struttura delle Verifiable Presentations ricevute.
      - Relying Party
      - Security
      - Response Validation
    * - REMFLOW-29
      - La Relying Party DEVE validare le prove crittografiche nelle Verifiable Presentations ricevute.
      - Relying Party
      - Security
      - Response Validation
    * - REMFLOW-30
      - La Relying Party DEVE verificare il periodo di validità delle Credenziali presentate.
      - Relying Party
      - Security
      - Credential Validation
    * - REMFLOW-31
      - La Relying Party DEVE controllare lo stato di revoca delle Credenziali quando applicabile.
      - Relying Party
      - Security
      - Credential Validation
    * - REMFLOW-32
      - La Relying Party DEVE validare che la risposta sia correttamente crittografata.
      - Relying Party
      - Security
      - Response Validation
    * - REMFLOW-33
      - La Relying Party DEVE validare che la risposta corrisponda ai parametri della richiesta originale.
      - Relying Party
      - Security
      - Response Validation
    * - REMFLOW-34
      - La Relying Party DEVE validare il formato e la struttura della risposta di autorizzazione.
      - Relying Party
      - Security
      - Response Validation
    * - REMFLOW-35
      - La Relying Party DEVE garantire un reporting appropriato degli errori all'Utente in caso di fallimenti di verifica.
      - Relying Party
      - Privacy
      - Error Handling
    * - REMFLOW-36
      - La Relying Party DEVE implementare i meccanismi di gestione degli errori e validazione per gli URI di reindirizzamento definiti in questa specifica.
      - Relying Party
      - Security
      - Error Handling
    * - REMFLOW-37
      - La risposta di errore DEVE utilizzare ``application/json`` come tipo di contenuto.
      - Relying Party
      - Security
      - Error Handling
    * - REMFLOW-38
      - La risposta di errore DEVE includere i parametri ``error`` e ``error_description``.
      - Relying Party
      - Security
      - Error Handling
    * - REMFLOW-39
      - I Codici di Stato HTTP specificati e i relativi codici di errore DEVONO essere supportati per la risposta di errore.
      - Relying Party
      - Security
      - Error Handling
    * - REMFLOW-40
      - La Relying Party DEVE implementare una gestione appropriata dei timeout per i flussi di presentazione.
      - Relying Party
      - Security
      - Flow Management
    * - REMFLOW-41
      - La Relying Party DEVE garantire una pulizia appropriata dei dati temporanei di presentazione.
      - Relying Party
      - Security
      - Flow Management
    * - REMFLOW-42
      - La Relying Party DEVE implementare una pulizia appropriata dei Request Object scaduti.
      - Relying Party
      - Security
      - Flow Management
    * - REMFLOW-43
      - La Relying Party DEVE implementare log di audit appropriati di tutti i tentativi di verifica delle credenziali.
      - Relying Party
      - Security
      - Audit & Compliance
    * - REMFLOW-44
      - La Relying Party DEVE implementare log di sicurezza appropriati degli esiti di verifica.
      - Relying Party
      - Security
      - Audit & Compliance


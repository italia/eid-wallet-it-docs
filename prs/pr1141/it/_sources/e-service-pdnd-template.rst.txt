.. include:: ../common/common_definitions.rst


PDND e-Service Template
=======================

La PDND fornisce uno strumento specializzato che migliora i processi di co-progettazione delle API ottimizzando la pubblicazione e il riutilizzo dei servizi elettronici. Questa funzionalità è definita e regolamentata nel presente documento.

    - "Linee Guida sull'infrastruttura tecnologica della Piattaforma Digitale Nazionale Dati per l'interoperabilità dei sistemi informativi e delle basi di dati" (`PDND`_).

Il template del servizio elettronico serve come modello standardizzato contenente tutti i metadati tecnici e descrittivi necessari per un servizio elettronico. I Gestori delle API, che possono essere sia Fornitori che Consumatori all'interno dell'ecosistema PDND, POSSONO creare e mantenere questi template.

Una volta che un e-service template è pubblicato, è accessibile attraverso il Catalogo Template PDND che è un repository centralizzato che facilita il riutilizzo. Questo catalogo consente a qualsiasi Partecipante PDND autorizzato di sfogliare i template disponibili e istanziare nuovi servizi elettronici basati su progetti esistenti.


Definizione e linee guida dell'e-service template PDND
------------------------------------------------------

L'infrastruttura PDND supporta la gestione del ciclo di vita dei Servizi Elettronici Template, simile a quella dei servizi elettronici tradizionali. Gli stati del ciclo di vita includono: **Draft**, **Active**, **Supsended** e **Deprecated**. Come per i servizi elettronici tradizionali, PDND applica il controllo degli accessi basato sui ruoli per governare le transizioni di stato.

Gestione dei Servizi Elettronici Template
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Creazione del Servizio Elettronico Template
"""""""""""""""""""""""""""""""""""""""""""
I Partecipanti sono abilitati a creare Servizi Elettronici Template tramite una procedura guidata accessibile attraverso l'interfaccia web PDND (le API saranno disponibili in futuro). Il flusso di lavoro di creazione rispecchia da vicino quello della creazione standard di servizi elettronici, con le seguenti distinzioni:

    - Un campo aggiuntivo identifica il destinatario previsto del template.
    - Il campo "Audience" è omesso.
    - Le soglie sono opzionali e servono come raccomandazioni per i Partecipanti che implementano il template.

Ai Partecipanti è vietato creare più template con lo stesso nome: i nomi dei template DEVONO essere unici per partecipante. Alla creazione, un template è inizialmente impostato sullo stato Draft. I template possono quindi essere pubblicati nel Catalogo Template, rendendoli così accessibili a tutti i Partecipanti.

Modifica del Servizio Elettronico Template
""""""""""""""""""""""""""""""""""""""""""
I Partecipanti che hanno creato un template possono modificarlo. La portata dei campi modificabili dipende dallo stato del ciclo di vita del template:

    - Se il template è in stato Draft, tutti i campi sono modificabili.
    - Per i template in altri stati, solo un sottoinsieme limitato di campi può essere modificato direttamente.
    - I campi che non possono essere modificati nei template pubblicati richiedono la creazione di una nuova versione del template per applicare le modifiche.

Il versionamento dei template funziona in modo simile a quello dei servizi elettronici, dato che le modifiche al modello possono impattare i servizi istanziati e quindi i Partecipanti che consumano quell'istanza.

I seguenti campi possono essere modificati senza attivare una nuova versione del template:

    - Name
    - Intended Recipient
    - Description
    - Voucher Time Limit
    - Documentation (escludendo la specifica OpenAPI)
    - Attributes

Sospensione del e-service Template
""""""""""""""""""""""""""""""""""
I template, come i servizi elettronici, possono essere Sospesi. Quando sospesi:

    - Il template viene rimosso dal catalogo pubblico dei template.
    - L'istanziazione di nuove istanze dal template sospeso è disabilitata.
    - Le istanze precedentemente istanziate rimangono inalterate.
    - I template possono essere riattivati in qualsiasi momento.
    - I template non possono essere eliminati.

Istanziazione del e-service Template
""""""""""""""""""""""""""""""""""""
I Partecipanti possono istanziare un Servizio Elettronico Template sfogliando il Catalogo Template e selezionando un template. Questo processo genera un nuovo servizio elettronico.

I vincoli di istanziazione includono:

    - Solo i template in stato Attivo sono idonei per l'istanziazione.
    - L'istanziazione è facilitata attraverso una procedura guidata nell'interfaccia web PDND.
    - A causa dell'obiettivo di standardizzazione dei template, la maggior parte dei campi è pre-compilata e immutabile durante l'istanziazione.
    - Le seguenti informazioni non possono essere modificate durante l'istanziazione:

        - Caricamento della documentazione
        - Tempo di scadenza del token
        - Nome, descrizione e attributi

Invece, i seguenti campi devono essere specificati durante l'istanziazione:

    - Audience
    - Thresholds
    - Automatic/Manual Approval Policy

Inoltre, sebbene la specifica OpenAPI sia fissa, i seguenti campi di metadati possono essere forniti in modo che PDND possa aggiornare automaticamente la specifica YAML:

    - Contatti (nome, email, URL, URL Termini e Condizioni)
    - URL del server

Ogni servizio elettronico istanziato mantiene un ciclo di vita indipendente analogo ai servizi elettronici standard.

Gestione delle Versioni
^^^^^^^^^^^^^^^^^^^^^^^
Il versioning dei template segue un processo controllato:

    - La pubblicazione di una nuova versione del template la imposta su Active.
    - La versione precedentemente Active viene automaticamente trasferita a Deprecated.
    - È consentita solo una versione Active per template in qualsiasi momento.
    - I template possono anche avere una singola versione Draft che coesiste con la versione Active.

Le istanze derivate dai template mantengono un versioning indipendente poiché i Partecipanti possono aggiornare i campi specifici dell'istanza (ad esempio, URL del server) più volte, mentre l'istanza rimane collegata alla versione del template di origine.

Di conseguenza, le versioni dei template e le versioni delle istanze sono indipendenti e non direttamente correlate.

I Partecipanti che istanziano un template possono quindi aggiornare sia l'istanza specifica o, se disponibile, aggiornare a una versione più recente del template.

Template per Fonte Autentica
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

La funzionalità del servizio elettronico template viene utilizzata per standardizzare la trasmissione dei dati dalle Fonti Autentiche ai Fornitori di Attestati Elettronici.
Il servizio elettronico template DOVREBBE essere pubblicato all'interno della PDND dal Fornitore di Attestati Elettronici ed è accessibile attraverso il Catalogo Template PDND.

Parametri del Template per Fonte Autentica
""""""""""""""""""""""""""""""""""""""""""

Il servizio elettronico template **DEVE** rispettare le seguenti proprietà:

    - **Name**: IT Wallet - Fonte Autentica - <``Nome dell'Attestato Elettronico``>
    - **Intended Recipients**: IT Wallet - Fonte Autentica - <``Dominio della Fonte Autentica``>
    - **Description**: Descrizioni utili al Fornitore di Attestati Elettronici in relazione al nuovo attestato elettronico <``Nome dell'Attestato Elettronico``>
    - **Technology**: REST
    - **Data variation via Signal Hub**: True
    - **Version changelog**: Servizio elettronico Fonte Autentica tramite implementazione template
    - **Voucher Time Limit**: 20
    - **Suggest custom threshold**: False
    - **Suggest manual agreement approval policy**: False
    - **Attributes**: <``Nome ufficiale dell'Ente Pubblico Fornitore di Attestati Elettronici``>

Istanziazione del Template per Fonte Autentica
""""""""""""""""""""""""""""""""""""""""""""""

Ogni Fonte Autentica **DOVREBBE** istanziare il servizio elettronico template *IT Wallet - Fonte Autentica* nella PDND.  
Il processo di istanziazione risulterà in un nuovo servizio elettronico che **DEVE** soddisfare i seguenti requisiti:

    - **Signal Hub**: True
    - **Politica di approvazione manuale**: False
    - **Soglia giornaliera chiamate API per ogni fornitore**: maggiore di 10000
    - **Soglia giornaliera chiamate API**: maggiore di 10000

Informazioni aggiuntive richieste durante il processo di creazione sono dipendenti dal fornitore.

Specifica OpenAPI della Fonte Autentica PDND
""""""""""""""""""""""""""""""""""""""""""""

Di seguito è riportata la specifica OpenAPI completa per i servizi elettronici della Fonte Autentica PDND:

.. literalinclude:: ./oas3/OAS3-PDND-AS.yaml
    :language: yaml
    :linenos:



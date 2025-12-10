.. include:: ../common/common_definitions.rst


Sistema di Onboarding
============================

L'ecosistema IT-Wallet opera come un'infrastruttura di trust federata dove le entità partecipanti devono stabilire relazioni di trust crittografiche e mantenere la conformità con standard di sicurezza comuni.

Il sistema di onboarding DEVE abilitare operazioni sicure con Attestati Elettronici. Allo stesso tempo, DEVE soddisfare i diversi requisiti operativi che i diversi partecipanti richiedono.

I processi amministrativi per le entità organizzative sono comuni a tutti i partecipanti e indipendenti dalle loro funzioni tecniche all'interno dell'ecosistema. Tuttavia, i processi di registrazione tecnica DEVONO tenere conto dei ruoli operativi distinti.

I Credential Issuer, le Relying Party e le Istanze del Wallet (registrate indirettamente tramite i Fornitori di Wallet) partecipano direttamente alle operazioni di emissione e verifica delle Credenziali. Queste entità richiedono la costituzione di trust crittografico attraverso protocolli di federazione.

Le Fonti Autentiche forniscono dati autorevoli attraverso relazioni di trust dirette con i Credential Issuer. Servono un ruolo centrale nella discovery e disponibilità dei dati, richiedendo procedure di registrazione specializzate focalizzate sui dati.

Architettura del Sistema di Onboarding
---------------------------------------

Il framework di onboarding DEVE fornire processi di onboarding specializzati che corrispondano alle caratteristiche operative e agli obblighi normativi dei diversi tipi di partecipanti.

.. plantuml:: plantuml/trust-infrastructure-overview.puml
    :width: 99%
    :alt: Panoramica del sistema di onboarding IT-Wallet che mostra i processi di registrazione a doppio Journey e l'infrastruttura di trust
    :caption: `Panoramica del Sistema di Onboarding IT-Wallet. <//www.plantuml.com/plantuml/svg/hLL_RnCv4Fr_FyLSE954eir1MbJGWSYb0I8LDKe25H9IDB4d6qkElRAzoOKJt_titUtYP0la3o9Lwevddj-y-U4trg5n-KQ2CxbrPqAj35h_FtEveJEz9RCLj4l-48h9d1FyFRpe3IyMGxt9j2BbNYVlnzUZnMm-cevkvvydequtQTyCFjz-d2zkHc_dY-dutVkvDoPjkAQLK0IpoNGy7yqYJ9Tdo4s_jzBAdU6EhDxGsMMFaN5Y9HWwUlrhRuuEbsXFSMKwjIUu2RvWQFW9dZkKajol77j2MITSxeHMhuCWGo-vte1rUqas6N0-ahGXvUQOTbhqhoEZKBQUm9_BTAYbDgzQZruKls0Bo9LrjnQE2ZzjE9dAcXhQjxh7i9aH6pJxGzIdJvzVBVb9g8_-MbvSNLqqWHsnzI7gSxRizrUdeLxWLV_PYoPg6bfGeM9qY7qrwB-uUdiQzkNbi_xbm6CdJZX9C9wVtHK5Wrkrr6YuK2dCzjRH1cwhZW_bcPHImO0vRMpoZyuLzz-TIi8dq3hqQ7bBg_jV0lutzAnGA38TjDuyoDsQb1CCPZetZ0hVQtJeBz5RmQcCVbTa6v87GwcmpWZouPdHAx9MQ8KIj4bHYQyOkiYV4SyPkl8ewYyRP72OsbTrOQpdxUXLwtvGMjqZfYRp5AOazq6F2HedIfv3GpoGHmcVoFY9hDZUnanW6uwAK2vIuRmpg-CihBG16wHb1CWOsOXWfMVCCKneWzykyAig5ybMssPQLhato6N1FTGvAZvccHIiSd0Qc73YAwcV4oidlK6DYKETnjRcP8xLcvK2FC1FUFyVIHTgnK4hGDz4sjFmCLk2KCQVKgtML-Zxv5l1jmrLwcDbNPWfw0Z5XI7coltVK3oaTHGJo7_GIo6fTqTB66HPaMKfNfr0gPE5dN1hEBm4tDheF5t3tQJc7ssxfjPX5kT5vFZWUVe-aGNkGeHJp-KXtuTdKzVplx3xCAUDXH3YfkKe5gKwgE47L9YIXL0fjmSJ-w7YLRfa7IwbiEimrtNoF4Tvbg5RXzuCyq1HuqLRBz8Z6k-g0O_IMH6dylf5nIKigRUr5QQLjLMh55lk_mUzWWgAU9cS80kTwUG9tFc_uRZhhJwd89FEAd2KLRvRb88Nff-sP_IwFvmDsZYBmGngVeyX6geXEfGw3GaS9z7OkaLLS8j2UlOKJHcuVKRbbkB2iY3__gGD-YtnlpOyFOS1tmWLhYx7yw1fEYXbBMGtcPBy_eWqUh21zKN5O2796qfHzhmwkKIdVRAOXGtdn-TNuC_EOUwpKOAXREBMHpscDvaKeGDZx7O0Dzdl9bq1xtu_C9J8JFn-oacrKdrZJj2jYwzmr_4zXstSn_FxY9TVr3KwXEDBXyTT-HWiMzC6RJmdROZcEi01_932mtkXlpoFCIfAvLeOnJihaFe--n0DhYsNS_-y-R3SJM1Jh4VUJUwBMpmd5zvvV93q5nLxXzl61mz6k0HkSB-OXjvZebj-VGnbtMNrbxyXqZesxqIWMK74RqKr9rr_U1ljiO_MCqdQIZk2i0hY6hw4rlNzXl1o7HUh5OSrTG_XfSAVwYtfKQ8oL5l20oLlIF5y8_y7>`_

Tutti gli Attori Primari DEVONO sottoporsi alla registrazione amministrativa per la conformità legale e normativa, seguita da processi di registrazione tecnica specializzati che DEVONO riflettere i loro ruoli operativi nell'ecosistema degli Attestati Elettronici.

    1. **Registrazione Amministrativa**: Tutte le entità (Fonti Autentiche, Relying Party, Fornitori di Wallet, Credential Issuer) DEVONO completare la registrazione amministrativa iniziale che convalida la loro posizione legale, conformità normativa ed eleggibilità organizzativa per partecipare all'ecosistema IT-Wallet.

    2. **Registrazione Tecnica**: Dopo l'approvazione amministrativa, le entità completano la registrazione tecnica attraverso Journey specializzati:

        a. **Fonti Autentiche**: Dichiarano i loro Attributi dell'Utente disponibili dal Registro degli Attributi dell'Utente e specificano domini, scopi e tipo di organizzazione (pubblica o privata) previsti.

        b. **Credential Issuer**: Selezionano le Fonti Autentiche basate sugli Attributi dell'Utente richiesti, richiedono l'approvazione dell'integrazione (eccetto per i mandati normativi) e registrano i tipi di Credenziali con pubblicazione automatica del catalogo secondo la politica dell'Organismo di Supervisione.

        c. **Altre Entità di Federazione** (Relying Party, Fornitori di Wallet): Subiscono registrazione basata su federazione per l'istituzione di trust crittografico.

    3. **Integrazione del Registro IT-Wallet**:

        a. **Integrazione del Registro degli Attributi dell'Utente e della Tassonomia**: Il Registro degli Attributi dell'Utente fornisce definizioni di dati standardizzate per i singoli Attributi delle Credenziali, mentre la Tassonomia definisce la classificazione gerarchica (domini, scopi) che vengono poi referenziati nel Catalogo degli Attestati Elettronici per implementazioni specifiche di Credenziali. Tutti i partecipanti sfruttano questi registri per dichiarazioni di capacità di fornitura dati e requisiti di emissione/verifica.

        b. **Integrazione del Registro AS**: Fonti Autentiche registrate con i loro Attributi dell'Utente dichiarati e relative specifiche, abilitando la discovery e coordinazione dei CI.

        c. **Integrazione del Registro di Federazione**: Entità operative incluse per la validazione del trust durante le operazioni delle Credenziali.

        d. **Integrazione del Catalogo**: Tipi di Credenziali automaticamente pubblicati nel :ref:`registry:Catalogo degli Attestati Elettronici` basato sulle politiche dell'Organismo di Supervisione per l'eleggibilità alla discovery pubblica.

    4. **Registrazione dell'Istanza del Wallet**: Le Istanze del Wallet sono registrate indirettamente attraverso i Fornitori di Wallet, stabilendo le specifiche di gestione delle Credenziali a livello utente. I dettagli tecnici sono forniti in :ref:`wallet-instance-registration:Inizializzazione e Registrazione dell'Istanza del Wallet`.

Processo di Registrazione della Fonte Autentica
------------------------------------------------

La registrazione della Fonte Autentica consente ai fornitori di dati di stabilire il loro ruolo autorevole nell'ecosistema degli Attestati Elettronici attraverso la registrazione delle loro specifiche di fornire dati e meccanismi di accesso standardizzati basati sul Registro degli Attributi dell'Utente e sulle classificazioni della Tassonomia.

Le Fonti Autentiche DEVONO sottoporsi a procedure di registrazione che convalidano la loro autorità sui dati, dichiarano i loro Attributi dell'Utente disponibili dal Registro degli Attributi dell'Utente standardizzato e stabiliscono meccanismi di integrazione tecnica. Le Fonti Autentiche specificano casi d'uso previsti (formalmente ``purposes``) che determinano l'eleggibilità del catalogo secondo le politiche dell'Organismo di Supervisione.

Le Fonti Autentiche Pubbliche DEVONO sfruttare l'integrazione PDND per fornire dati governativi attraverso l'infrastruttura nazionale standardizzata.

Le Fonti Autentiche Private POSSONO stabilire interfacce di servizio personalizzate che soddisfano requisiti organizzativi o normativi specifici.

Entrambe i flussi DEVONO assicurare standard di qualità dei dati e stabilire tracce di audit per tutte le attività di fornitura dati.

**Processo di Coordinamento AS-CI**: Dopo la registrazione AS, i Credential Issuer identificano entità AS adatte attraverso il Registro AS e richiedono autorizzazione all'integrazione durante la fase di registrazione amministrativa. Per i mandati normativi, l'autorizzazione DEVE essere automatica. Altrimenti, le entità Fonti Autentiche valutano e autorizzano le richieste dei Credential Issuer basate su criteri commerciali e tecnici. Dopo l'autorizzazione amministrativa, le procedure di integrazione tecnica stabiliscono le relazioni operative di accesso ai dati prima della pubblicazione del catalogo dei tipi di Credenziali.

Le Fonti Autentiche registrate con successo DEVONO essere incluse nel Registro AS con i loro Attributi dell'Utente dichiarati e le relative specifiche. I tipi di Credenziali DEVONO diventare pubblicamente scopribili nel :ref:`registry:Catalogo degli Attestati Elettronici` solo dopo l'integrazione AS-CI riuscita e l'approvazione della politica dell'Organismo di Supervisione per l'eleggibilità del catalogo.

Le procedure di implementazione tecnica per la registrazione della Fonte Autentica sono fornite in :ref:`entity-onboarding:Procedura di Registrazione AS`.


Processo di Onboarding della Federazione
-----------------------------------------

L'onboarding della federazione stabilisce le relazioni di trust crittografiche e i framework di conformità che consentono alle entità operative di partecipare ad attività sicure del ciclo di vita delle Credenziali.
Le entità operative DEVONO completare l'onboarding che include la verifica dell'eleggibilità amministrativa, la validazione dell'infrastruttura tecnica e l'istituzione del trust crittografico. Il processo di onboarding crea relazioni di trust crittografiche attraverso l'emissione di certificati, la configurazione della catena di trust e l'attestazione di conformità. Questi meccanismi abilitano interazioni sicure tra i partecipanti della federazione e forniscono la base per la validazione del trust distribuito attraverso l'ecosistema.

Le entità registrate con successo sono incluse nel Registro di Federazione, che mantiene l'elenco autorevole dei partecipanti della federazione fidati. Questo registro abilita la validazione del trust operativo durante le attività del ciclo di vita delle Credenziali.

Le Relying Party DEVONO verificare gli Attestati Elettronici con garanzia crittografica, i Fornitori di Wallet DEVONO fornire servizi di portafoglio digitale fidati ai cittadini, e i Credential Issuer DEVONO emettere Attestati Elettronici utilizzando fonti di dati autorevoli. Tutte le operazioni DEVONO avvenire all'interno di relazioni di trust stabilite che assicurano sicurezza e auditabilità.

Gestione del Ciclo di Vita delle Entità
----------------------------------------

Dopo l'onboarding riuscito, le entità richiedono una gestione continua del ciclo di vita per mantenere lo stato operativo e la conformità all'interno dell'ecosistema IT-Wallet. La gestione del ciclo di vita comprende aggiornamenti amministrativi, modifiche tecniche e processi di uscita dalla federazione che soddisfano i requisiti organizzativi e operativi in evoluzione.

Gestione delle Operazioni Continuative
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Le entità DEVONO mantenere informazioni amministrative e tecniche aggiornate per assicurare la partecipazione alla federazione e la conformità.

**Aggiornamenti Amministrativi**

Le organizzazioni POSSONO aggiornare le informazioni amministrative attraverso canali di registro standard, come:

    - **Cambiamenti dell'Entità Legale**: Cambiamenti del nome dell'azienda, ristrutturazione organizzativa, modifiche dello stato legale.
    - **Informazioni di Contatto**: Aggiornamenti ai canali di contatto ufficiali e al personale responsabile.
    - **Stato Normativo**: Cambiamenti in licenze, certificazioni o stato di conformità normativa.
    - **Ambito del Servizio**: Modifiche alle offerte di servizio o alle caratteristiche della base utenti.

Gli aggiornamenti amministrativi DEVONO seguire processi di governance standard e NON DOVREBBERO influenzare le operazioni tecniche della federazione.

**Gestione della Configurazione Tecnica**

Gli aggiornamenti tecnici che influenzano le operazioni del protocollo di federazione richiedono procedure coordinate, inclusi:

    - **Gestione dei Certificati**: Rinnovo regolare dei certificati, sostituzione di emergenza, gestione della revoca.
    - **Cambiamenti dell'Infrastruttura**: Aggiornamenti degli endpoint, migrazioni di servizio, modifiche della capacità.
    - **Aggiornamenti di Conformità**: Aggiornamenti degli standard di sicurezza, cambiamenti delle politiche, requisiti di audit.
    - **Modifiche delle Capacità**: Aggiunta o rimozione di protocolli supportati, tipi di Credenziali o caratteristiche del servizio.

Gli aggiornamenti tecnici DEVONO essere validati dall'Organismo di Supervisione per mantenere le relazioni di trust della federazione e l'integrità operativa.

Processi di Uscita e Rimozione dalla Federazione
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Le entità POSSONO uscire dalla federazione volontariamente o essere rimosse dall'Organismo di Supervisione per ragioni di conformità o sicurezza.

**Uscita Volontaria dalla Federazione** - Le organizzazioni POSSONO scegliere di uscire dalla federazione per ragioni commerciali o operative, inclusi:

    - **Cambiamenti Commerciali**: Ristrutturazione organizzativa o interruzione del servizio.
    - **Migrazione Tecnica**: Passaggio a soluzioni tecniche o fornitori alternativi.
    - **Cambiamenti Normativi**: Cambiamenti nell'ambiente normativo o nei requisiti di conformità.

L'uscita volontaria DEVE richiedere coordinamento con entità dipendenti e gestione appropriata delle Credenziali esistenti e delle relazioni con gli utenti.

**Rimozione dell'Organismo di Supervisione** - L'Organismo di Supervisione PUÒ avviare la rimozione dell'entità per:

    - **Violazioni di Conformità**: Mancato mantenimento della conformità normativa o aderenza alle politiche della federazione.
    - **Incidenti di Sicurezza**: Compromissione dell'infrastruttura di sicurezza o mancato mantenimento degli standard di sicurezza.
    - **Fallimenti Operativi**: Fallimenti tecnici persistenti che influenzano la sicurezza della federazione.
    - **Violazioni delle Politiche**: Violazioni delle politiche operative della federazione o degli accordi.

I processi di rimozione POSSONO includere indagini, rimedi e procedure di appello dove appropriato.

.. warning::

    Per incidenti di sicurezza critici o minacce immediate all'integrità della federazione, l'Organismo di Supervisione PUÒ implementare la sospensione di emergenza con effetto immediato.

Requisiti di Coordinamento del Ciclo di Vita
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

La gestione del ciclo di vita nell'ecosistema IT-Wallet necessita di coordinamento tra più partecipanti per mantenere le operazioni funzionanti e mantenere le relazioni di trust. Il framework di coordinamento copre tre aree principali:

    - **Comunicazione degli stakeholder:** Quando le entità devono apportare cambiamenti che impattano le operazioni dell'ecosistema IT-Wallet, DEVONO informare l'Organismo di Supervisione e i partecipanti della federazione rilevanti in anticipo.
    - **Sincronizzazione del registro:** Quando un'entità apporta cambiamenti che influenzano altre entità, tutti i sistemi di registro DEVONO essere aggiornati correttamente assicurando che tutti i cambiamenti siano registrati in modo sicuro con timestamp e ragioni.
    - **Garanzia di continuità aziendale:** Le entità DOVREBBERO bilanciare tra l'apportare aggiornamenti necessari e mantenere i loro obblighi verso utenti e normative. Questo include assicurare che il servizio sia il più disponibile possibile, gestire i dati personali correttamente durante i cambiamenti e rimanere conformi ai requisiti legali anche in situazioni di emergenza.

Le procedure tecniche e i requisiti di conformità specifici per la gestione del ciclo di vita sono dettagliati nella Sezione :ref:`entity-onboarding:Gestione del Ciclo di Vita delle Entità`.

Onboarding Journey Maps
------------------------

Le seguenti mappe dei Journey forniscono una vista dettagliata dell'esperienza di onboarding dalla prospettiva di ogni tipo di entità e dei loro operatori. Queste rappresentazioni grafiche aiutano le organizzazioni a comprendere i passaggi specifici, i requisiti e le interazioni che incontreranno durante il loro processo di onboarding.

Ogni mappa del Journey mostra il processo completo dalla pianificazione iniziale all'integrazione finale del registro, evidenziando i punti di contatto critici con l'Organismo di Supervisione e le dipendenze tra i diversi processi di onboarding delle entità.

Panoramica dell'Ecosistema
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ./images/svg/onboarding-journey-maps/overview-onboarding-journey.svg
    :width: 100%
    :alt: Panoramica dell'onboarding dell'ecosistema IT-Wallet
    :name: onboarding-overview

    Onboarding completo dell'ecosistema che mostra i processi principali

Il sistema Registro IT-Wallet coordina tutte le registrazioni attraverso cinque componenti principali:

    1. **Registro degli Attributi dell'Utente** per definizioni semantiche standardizzate dei singoli Attributi delle Credenziali.
    2. **Registro AS** per fonti di dati e capacità di fornitura dati.
    3. **Registro di Federazione** per relazioni di trust operative.
    4. **Catalogo degli Attestati Elettronici** (vedi :ref:`registry:Catalogo degli Attestati Elettronici`) per la discovery dei tipi di Credenziali.
    5. **Tassonomia** per la classificazione gerarchica che organizza le Credenziali per dominio e scopo.

Le seguenti mappe dei Journey illustrano due scenari di Credenziali distinti:

    - **Scenario Catalogo Pubblico**: Patente di Guida Mobile (mDL) fornita per una discovery pubblica tramite Catalogo delle Credenziali.
    - **Scenario Credenziale Privata**: Badge Dipendente Aziendale dall'Azienda (AS Privata, e quindi fornita per la discovery solo tramite Offerta di Credenziale).

Journey dell'Operatore della Fonte Autentica
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. .. figure:: ./images/svg/onboarding-journey-maps/as-onboarding-journey.svg
..     :width: 100%
..     :alt: Journey di onboarding della Fonte Autentica
..     :name: as-onboarding-journey

..     Processo di registrazione della Fonte Autentica e interazioni con l'Organismo di Supervisione

Dalla prospettiva dell'operatore della Fonte Autentica, il processo di onboarding inizia con la valutazione delle capacità di fornire dati esistenti rispetto al Registro degli Attributi dell'Utente standardizzato e alle classificazioni della Tassonomia, determinando quali Attributi dell'Utente possono essere resi disponibili come Attestato Elettronico. L'operatore invia una richiesta di registrazione all'Organismo di Supervisione, dichiarando Attributi dell'Utente specifici dal Registro degli Attributi dell'Utente con i domini della Tassonomia e gli scopi previsti.

**Esempio - Fonte Autentica Pubblica (Scenario mDL)**:

    - **Dichiarazione degli Attributi dell'Utente**: Seleziona Attributi dell'Utente standardizzati (``given_name``, ``family_name``, ``driving_privileges``, ecc.) dal Registro degli Attributi dell'Utente.
    - **Classificazione della Tassonomia**: Dominio ``AUTHORIZATION``, Scopo ``DRIVING_LICENSE``.
    - **Caso d'Uso**: Servizio pubblico - verifica dell'autorizzazione alla guida (eleggibile per il Catalogo delle Credenziali).
    - **Integrazione**: Integrazione e-service PDND seguendo gli standard governativi (vedi :ref:`e-service-pdnd:e-Service PDND`).
    - **Risultato del Catalogo**: mDL diventa pubblicamente scopribile dopo l'integrazione CI.

**Esempio - AS Aziendale (Scenario Badge Dipendente)**:

    - **Dichiarazione degli Attributi dell'Utente**: Seleziona Attributi dell'Utente (``given_name``, ``family_name``, ``employee.job_title``, ecc.) dal Registro degli Attributi dell'Utente.
    - **Classificazione della Tassonomia**: Dominio ``MEMBERSHIP``, Scopo ``ASSOCIATION``.
    - **Caso d'Uso**: Controllo accessi aziendale privato (non eleggibile per il Catalogo delle Credenziali).
    - **Integrazione**: API personalizzata per l'integrazione del Credential Issuer.
    - **Risultato del Catalogo**: Il badge rimane privato, disponibile solo tramite Offerta di Credenziale.

Le fasi critiche includono la verifica amministrativa da parte dell'Organismo di Supervisione (che coinvolge controlli di conformità normativa al di fuori dell'ambito tecnico) e la validazione tecnica. Il processo si conclude con la registrazione nel Registro AS, rendendo gli Attributi dell'Utente dichiarati scopribili dai Credential Issuer per le richieste di integrazione.

.. warning::

    **Dipendenza importante**: Gli Attributi dell'Utente dichiarati nel Registro AS rimangono non disponibili agli utenti finali fino a quando un Credential Issuer completa la registrazione, l'approvazione dell'integrazione e l'implementazione tecnica. La pubblicazione del catalogo dipende dalle politiche dell'Organismo di Supervisione per l'eleggibilità alla discovery pubblica.

Journey dell'Operatore del Credential Issuer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. .. figure:: ./images/svg/onboarding-journey-maps/ci-onboarding-journey.svg
..     :width: 100%
..     :alt: Journey di onboarding del Credential Issuer
..     :name: ci-onboarding-journey

..     Registrazione del Credential Issuer con alternative del flusso di integrazione

Gli operatori del Credential Issuer iniziano effettuando la discovery delle Fonti Autentiche disponibili attraverso il Registro AS e valutando la fattibilità dell'integrazione basata sugli Attributi dell'Utente richiesti. La richiesta di registrazione specifica quali tipi di Credenziali intendono emettere, seleziona entità Fonte Autentica appropriate e dimostra la capacità tecnica di accedere alle fonti di dati richieste.

**Esempio - mDL (Scenario Pubblico)**:

    - **discovery AS**: Identifica la Fonte Autentica che fornisce Attributi mDL nel Registro AS con gli Attributi dell'Utente della patente di guida richiesti.
    - **Richiesta di Integrazione**: Approvazione automatica dovuta al mandato normativo.
    - **Configurazione Tecnica**: Integrazione e-service PDND seguendo gli standard governativi (vedi :ref:`e-service-pdnd:e-Service PDND`).
    - **Pubblicazione del Catalogo**: mDL automaticamente pubblicato nel Catalogo delle Credenziali.
    - **Accesso Utente**: I cittadini scoprono mDL attraverso un catalogo pubblico nel Wallet.

**Esempio - CI per Badge Dipendente (Scenario Privato)**:

    - **discovery AS**: Identifica la Fonte Autentica nel Registro AS con gli Attributi dell'Utente di accesso dipendente.
    - **Richiesta di Integrazione**: Richiede approvazione AS.
    - **Configurazione Tecnica**: Integrazione API personalizzata con autenticazione.
    - **Pubblicazione del Catalogo**: Badge escluso dal catalogo pubblico per politica di supervisione.
    - **Accesso Utente**: I dipendenti ricevono badge solo tramite Offerta di Credenziale diretta dai sistemi aziendali.

La fase di configurazione tecnica offre due flussi di integrazione distinti a seconda del tipo di Fonte Autentica:

    - **Integrazione AS Pubblica**: Utilizza la piattaforma PDND per accedere ai dati governativi attraverso API standardizzate.
    - **Integrazione AS Privata**: Stabilisce connessioni API dirette con endpoint personalizzati forniti da organizzazioni private.

Dopo il test di integrazione riuscito e l'approvazione della Fonte Autentica, il Credential Issuer è registrato nel Registro di Federazione come Entità fidata, abilitando l'emissione effettiva di Credenziali agli utenti finali.

.. warning::

    Questo passaggio attiva la disponibilità delle Credenziali per gli utenti finali. Le Credenziali pubbliche diventano scopribili attraverso il catalogo, mentre altre Credenziali rimangono disponibili solo tramite Offerte di Credenziale dirette.

Journey dell'Operatore del Fornitore di Wallet
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. .. figure:: ./images/svg/onboarding-journey-maps/wp-onboarding-journey.svg
..     :width: 100%
..     :alt: Journey di onboarding del Fornitore di Wallet
..     :name: wp-onboarding-journey

..     Processo di certificazione del Fornitore di Wallet e validazione della sicurezza

Gli operatori del Fornitore di Wallet seguono un Journey di onboarding indipendente che si concentra sulla certificazione dell'applicazione e sulla validazione della sicurezza. Il processo evidenzia lo sviluppo e la certificazione di applicazioni Wallet che possono memorizzare e gestire in modo sicuro gli Attestati Elettronici per i cittadini.

Un requisito tecnico chiave coinvolge l'implementazione di meccanismi di controllo dell'integrità e autenticità del Wallet. Questi controlli consentono al Wallet di ottenere un Wallet App Attestation, che serve come prova dello stato di sicurezza e conformità del Wallet durante le operazioni delle Credenziali.

Il processo di certificazione include la valutazione della sicurezza, coprendo l'architettura del Wallet, i meccanismi di protezione dei dati e le caratteristiche di privacy dell'utente. I fornitori di Wallet certificati con successo sono registrati nel Registro di Federazione e possono distribuire le loro applicazioni attraverso gli app store.

Journey dell'Operatore della Relying Party
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. .. figure:: ./images/svg/onboarding-journey-maps/rp-onboarding-journey.svg
..     :width: 100%
..     :alt: Journey di onboarding della Relying Party
..     :name: rp-onboarding-journey

..     Integrazione del servizio della Relying Party e processo di autorizzazione

Gli operatori della Relying Party iniziano identificando quali tipi di EAA sono richiesti per i loro servizi specifici e valutando la complessità dell'integrazione con i sistemi di autenticazione esistenti. La richiesta di registrazione fornisce evidenza di necessità legittime per accedere a tipi di Credenziale specifici e Attributi dell'Utente, delineando i casi d'uso del servizio previsti e le caratteristiche organizzative che giustificano l'accesso alle Credenziali.

**Esempio - Servizio di Noleggio Auto (RP Privata)**:

    - **Classificazione Aziendale**: Codice ATECO 77.11 (servizi di noleggio auto).
    - **Richiesta di Autorizzazione**: Verifica dell'autorizzazione alla guida per l'eleggibilità al noleggio.
    - **Requisiti degli Attributi dell'Utente**: ``given_name``, ``family_name``, ``driving_privileges``, ecc., da mDL.
    - **Giustificazione del Caso d'Uso**: Obbligo legale di verificare la patente di guida valida prima del noleggio del veicolo.
    - **Ambito di Autorizzazione**: Concesso accesso al dominio ``AUTHORIZATION``, scopo ``DRIVING_LICENSE``.

**Esempio - Servizi Municipali (RP Pubblica)**:

    - **Tipo di Organizzazione**: Pubblica Amministrazione con requisito codice IPA.
    - **Richiesta di Autorizzazione**: Verifica dell'identità del cittadino per l'accesso ai servizi municipali.
    - **Requisiti degli Attributi dell'Utente**: ``given_name``, ``family_name``, ``tax_id_code`` da PID.
    - **Giustificazione del Caso d'Uso**: Erogazione di servizi pubblici che richiede identificazione del cittadino.
    - **Ambito di Autorizzazione**: Concesso accesso più ampio riflettendo il mandato del servizio pubblico.

**Esempio - Controllo Accessi Aziendale (RP Privata)**:

    - **Classificazione Aziendale**: Codice ATECO 62.01 (attività di programmazione informatica).
    - **Richiesta di Autorizzazione**: Verifica del dipendente per l'accesso alle strutture aziendali.
    - **Requisiti degli Attributi dell'Utente**: ``given_name``, ``family_name``, ``employee.job_title`` dal Badge Dipendente Aziendale.
    - **Giustificazione del Caso d'Uso**: Sicurezza del posto di lavoro che richiede identificazione del dipendente e controllo degli accessi.
    - **Ambito di Autorizzazione**: Concesso accesso al dominio ``MEMBERSHIP``, scopo ``ASSOCIATION``.
    - **Discovery delle Credenziali**: Badge disponibile solo tramite Offerta di Credenziale privata (non eleggibile per il Catalogo delle Credenziali).

L'integrazione tecnica si concentra sullo sviluppo di flussi di autenticazione che possono verificare gli Attestati Elettronici presentati dagli Utenti. Questo include l'implementazione di meccanismi di verifica crittografica e l'istituzione di canali di comunicazione sicuri con l'infrastruttura di federazione.

L'autorizzazione del servizio da parte dell'Organismo di Supervisione DEVE coinvolgere una valutazione basata su politiche che considera il tipo di organizzazione (privata vs pubblica amministrazione), la classificazione del settore aziendale e i requisiti di servizio legittimi. Il processo di autorizzazione concede ambiti operativi specifici che definiscono quali domini di Credenziali e scopi la Relying Party può richiedere. Dopo l'approvazione, la Relying Party è registrata nel Registro di Federazione con profili di autorizzazione chiaramente definiti per l'accettazione degli Attestati Elettronici e degli Attributi dell'Utente.

Journey dell'Esperienza Utente
-------------------------------

Quando tutti i processi di onboarding delle entità sono completati con successo, gli Utenti possono scoprire e installare Istanze del Wallet certificate, ottenere gli Attestati Elettronici disponibili e presentare i loro Attestati elettronici a Fornitori di Servizi registrati (vedi :ref:`functionalities:Panoramica delle Funzionalità`).

Questa modalità di integrazione dipende dal fatto che tutte le entità rilevanti abbiano completato i rispettivi Journey di onboarding.

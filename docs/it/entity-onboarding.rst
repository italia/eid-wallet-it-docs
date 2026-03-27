.. include:: ../common/common_definitions.rst
.. include:: ../common/symbols.rst

Onboarding delle Entità
=======================

Questa sezione definisce le specifiche tecniche per la gestione del ciclo di vita delle entità nell'ecosistema IT-Wallet, basate sull'**Infrastruttura del Registro** definita in :ref:`registry:Infrastruttura del Registro`. Sono incluse le procedure di onboarding iniziale, le operazioni di gestione continuativa, quali aggiornamenti e modifiche dei dati, e i processi di uscita dalla federazione.

Per una panoramica di alto livello del processo di onboarding, vedere :ref:`onboarding-high-level:Sistema di Onboarding`. La sezione :ref:`onboarding-high-level:Onboarding Journey Maps` fornisce una mappa del percorso di onboarding dal punto di vista degli operatori dell'Entità.

Panoramica
----------

Architettura del Sistema di Onboarding delle Entità
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

L'ecosistema IT-Wallet opera su un'infrastruttura di fiducia federata, che richiede alle entità partecipanti di stabilire una fiducia reciproca prima di intraprendere qualsiasi interazione che coinvolga attributi dell'Utente.

Il framework di onboarding definisce procedure di registrazione tecnica in base alla tipologia di partecipante:

  1. Le Fonti Autentiche seguono processi di registrazione incentrati sui dati.
  2. Le Entità Operative (Emittenti di Credenziali, Relying Party, Fornitori di Wallet) seguono procedure di instaurazione della fiducia.

Tipologie di Entità e Percorsi di Onboarding
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

La seguente tabella riepiloga le tipologie di entità, i loro ruoli e i relativi percorsi di onboarding:

.. list-table:: Tipologie di Entità e Percorsi di Onboarding
   :class: longtable
   :widths: 20 30 25 25
   :header-rows: 1

   * - **Tipologia di Entità**
     - **Ruolo Principale**
     - **Percorso di Onboarding**
     - **Requisiti Chiave**
   * - Fonti Autentiche
     - Fornitori di dati autorevoli per gli attributi delle Credenziali Digitali
     - :ref:`entity-onboarding:Procedura di registrazione delle Fonti Autentiche`
     - Validazione della titolarità dei dati; integrazione API (es. PDND)
   * - Emittenti di Credenziali
     - Generano ed emettono Credenziali Digitali utilizzando i dati delle Fonti Autentiche
     - :ref:`entity-onboarding:Processo di Onboarding delle Entità Federate`
     - Conformità all'Infrastruttura di Fiducia IT-Wallet; vedere :ref:`trust-infrastructure:L'Infrastruttura di Trust`
   * - Relying Party
     - Verificano le Credenziali Digitali per l'accesso ai servizi
     - :ref:`entity-onboarding:Processo di Onboarding delle Entità Federate`
     - Conformità all'Infrastruttura di Fiducia IT-Wallet; vedere :ref:`trust-infrastructure:L'Infrastruttura di Trust`
   * - Fornitori di Wallet
     - Forniscono soluzioni wallet ai cittadini
     - :ref:`entity-onboarding:Processo di Onboarding delle Entità Federate`
     - Conformità all'Infrastruttura di Fiducia IT-Wallet (vedere :ref:`trust-infrastructure:L'Infrastruttura di Trust`); capacità di Attestazione del Wallet (vedere :ref:`wallet-instance-registration:Inizializzazione e Registrazione dell'Istanza del Wallet`)
   * - Istanze di Wallet
     - Applicazioni di wallet digitale a livello utente
     - Registrazione indiretta tramite il Fornitore di Wallet, vedere :ref:`wallet-instance-registration:Inizializzazione e Registrazione dell'Istanza del Wallet`
     - Attestazione del Wallet da un Fornitore di Wallet affidabile

Registrazione Amministrativa e Tecnica
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Il processo di onboarding segue un approccio strutturato in più fasi:

  1. **Registrazione Amministrativa**: Tutte le entità DEVONO completare la registrazione amministrativa iniziale che ne valida la posizione giuridica, la conformità normativa e l'idoneità organizzativa a partecipare all'ecosistema IT-Wallet.

  2. **Registrazione Tecnica**: A seguito dell'approvazione amministrativa, le entità effettuano la registrazione tecnica attraverso percorsi specializzati:
    
    - **Registrazione Fonte Autentica**: Procedure di registrazione incentrate sui dati con validazione dell'integrazione API.
    - **Registrazione in Federazione**: Instaurazione della fiducia crittografica come definito nella Sezione :ref:`trust-infrastructure:L'Infrastruttura di Trust`.

  3. **Integrazione con il Registro IT-Wallet**:

    - **Integrazione nel Registro dei Claims**: Le Fonti Autentiche selezionano definizioni standardizzate di claim dal Registro dei Claims durante la dichiarazione delle capacità.
    - **Integrazione nella Tassonomia**: Tutte le entità utilizzano la classificazione gerarchica della Tassonomia (domini, classi, finalità) per strutturare organizzativamente le Credenziali.
    - **Integrazione nel Registro delle Fonti Autentiche**: Le Fonti Autentiche vengono registrate con i claim e le capacità dichiarate, abilitando la discovery e il coordinamento degli Emittenti di Credenziali.
    - **Integrazione nel Registro della Federazione**: Le entità operative vengono incluse per la validazione della fiducia durante le operazioni sulle Credenziali.
    - **Integrazione nel Catalogo**: I tipi di Credenziale vengono pubblicati in :ref:`registry:Struttura del Catalogo degli Attestati Elettronici` in base alle politiche dell'Organismo di Vigilanza per l'idoneità alla discovery pubblica.

Tutti i componenti del registro e le loro interazioni sono descritti in dettaglio in :ref:`registry:Infrastruttura del Registro`.

Processo di Registrazione delle Fonti Autentiche
-------------------------------------------------

Le Fonti Autentiche DEVONO completare un processo di registrazione strutturato per confermare il loro status di fornitori di dati autorevoli nell'ecosistema IT-Wallet. Tale processo include la specifica dei requisiti e la validazione procedurale, come descritto in :ref:`onboarding-high-level:Journey dell'Operatore della Fonte Autentica`.

Requisiti di Registrazione delle Fonti Autentiche
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Le Fonti Autentiche DEVONO rispettare i seguenti requisiti tecnici:

  - **Conformità dei Claims**:

    - **Adozione del Registro dei Claims**: Le Entità DEVONO utilizzare identificatori standardizzati del Registro dei Claims nelle risposte ai dati. La mappatura personalizzata dei claim non è consentita.

  - **Standard di Integrazione API**:

    - **Entità Pubbliche**: DEVONO integrarsi tramite la piattaforma PDND con un'implementazione dell'e-service conforme alle specifiche nazionali.
    - **Entità Private**: DEVONO fornire un documento di Specifica `OAS3`_ completo che includa il framework di autorizzazione, gli schemi di richiesta/risposta, i meccanismi di gestione degli errori e un ambiente sandbox per i test.

  - **Standardizzazione del Formato di Risposta**:

    - **Formato Standard dei Claims**: Le Entità DEVONO utilizzare gli identificatori e i formati del Registro dei Claims in tutte le risposte ai dati.
    - **Mappatura degli Stati**: Le Entità DEVONO gestire una mappatura chiara tra i propri stati interni e gli stati standard delle Credenziali (valida, sospesa, revocata).

  - **Sicurezza e Garanzia della Qualità**:

    - **Standard di Sicurezza**: Le Entità DEVONO implementare TLS 1.3 o superiore con robusti meccanismi di autenticazione, perfect forward secrecy e algoritmi crittografici conformi agli standard di sicurezza attuali ed emergenti, con riservatezza e integrità end-to-end di tutte le comunicazioni, mantenendo la conformità ai requisiti normativi in evoluzione e alle best practice di settore.
    - **Evidenza di Autenticazione dell'Utente**: Le Entità POSSONO richiedere all'Emittente di Credenziali un'evidenza di autenticazione dell'Utente prima di concedere l'accesso agli e-service per l'ottenimento degli attributi dell'Utente.
    - **Qualità dei Dati**: Le Entità DEVONO specificare la frequenza di aggiornamento e fornire garanzie sull'aggiornamento dei dati.
    - **Audit Trail**: Le Entità DEVONO implementare capacità di logging per tutte le attività di accesso e fornitura dei dati.

Requisiti sulle informazioni di registrazione delle Fonti Autentiche
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::
  Solo le Fonti Autentiche italiane possono essere registrate nella fase attuale di IT-Wallet.

Durante la registrazione, le Fonti Autentiche DEVONO fornire le seguenti informazioni:

.. list-table:: Requisiti Informativi per la Registrazione delle Fonti Autentiche
   :class: longtable
   :header-rows: 1
   :widths: 30 70

   * - Categoria Informativa
     - Descrizione ed Esempi
   * - **Informazioni sull'Organizzazione**
     - **OBBLIGATORIO**. Dettagli dell'organizzazione inclusi:

       - Nome dell'organizzazione, tipologia ("public" o "private") e paese (ISO 3166-1 alpha-2).
       - Codici identificativi amministrativi, come il codice di registrazione IPA (OBBLIGATORIO solo per le Fonti Autentiche pubbliche) e l'identificativo legale (codice fiscale o partita IVA).
       - Informazioni di contatto, compresi riferimenti tecnici e amministrativi, quali indirizzi email, URI della homepage, URI dell'informativa sulla privacy.
   * - **Dichiarazione delle Capacità sui Dati**
     - **OBBLIGATORIO**. Claim disponibili:

       - Array di identificatori di claim del Registro dei Claims forniti dalla Fonte Autentica (es. ``["given_name", "family_name", "driving_privileges"]``).
       - Finalità previste per la verifica, utilizzando gli identificatori di finalità della tassonomia (es. ``["DRIVING_RIGHTS_VERIFICATION"]``).
      
   * - **Dettagli di Implementazione API**
     - **OBBLIGATORIO**. Informazioni dettagliate sull'integrazione:

       - Framework di autorizzazione per l'accesso API.
       - Definizioni API quali Formati di Richiesta/Risposta, inclusa la gestione degli errori.
   * - **Capacità di Fornitura dei Dati**
     - **OBBLIGATORIO**. Indica se la Fonte Autentica supporta la fornitura immediata/differita dei dati (booleano).    
   * - **Informazioni per l'Utente**
     - **OPZIONALE**. Testo in formato Markdown contenente informazioni in linguaggio naturale sui vincoli o limitazioni nella disponibilità dei dati. Ad esempio, se il database della Fonte Autentica contiene solo dati registrati dopo una data specifica, questa informazione DEVE essere comunicata agli Utenti.

       **Esempio**: "I dati della patente di guida sono disponibili per le patenti rilasciate dopo il 1° gennaio 2020. Per le patenti più vecchie, contattare l'ufficio motorizzazione locale.".

   * - **Proprietà di Visualizzazione**
     - **OPZIONALE**. Suggerimenti di branding visivo per le Credenziali Digitali che utilizzano i dati della Fonte Autentica:

       - Colore di sfondo per le Credenziali Digitali in formato esadecimale (es. ``"#003d82"``).
       - URI del logo con verifica dell'integrità crittografica per il branding delle Credenziali Digitali.
       - URI del modello visivo con verifica dell'integrità per la presentazione delle Credenziali Digitali.

Procedura di registrazione delle Fonti Autentiche
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

La registrazione della Fonte Autentica segue un processo tecnico descritto di seguito.

.. plantuml:: plantuml/as-registration-process.puml
    :width: 99%
    :alt: Processo di registrazione della Fonte Autentica che mostra la procedura in 3 fasi
    :caption: `Processo di Registrazione della Fonte Autentica. <https://www.plantuml.com/plantuml/svg/TLD1Rziw3BxxLn0zlG1vhs_hBK26TkqEFMmBbcAdNcY9SRJAaaPARRDVFzfE6iVBWXmCyUF7Z_p8Qyd8kRGURahUKiZEm3eMDWJVg76I6REB0LOS3ObKM78CfQs9goeXAzmb31akfkaNWAB_Kz2w9E9d9v5ty37QNG-IUiAqFfGUuanDLIsNiCwKuDrYeWlD4pQa-YZX_csvh2hD-_U3PY_s4OB83GRtQu2ui8dSzj-FuP_xrGsOQ6aEdXhqu6pNoSOHp_KzP3HPPYFAEpA-exIO4Gmch9rtsP4erwr7ryfR1oCkcSC3liOGsnreleY-cbx2AVV61OARrJsuDdbgDNtGR2cZyrsDrTsNkyklYKA7klhlVv14vYpRkW_i1gM9eyvU4LFDhct9EinqQMb3p6HXu-CBI4afSZuGIgs4fMvT1XvxmFIpaEIZIUyNy41c6rIGX-_edJqQ8_MUwX0Wc8xCH6tSOJ2asWQVvgTpf5T5aW9cOpvYRVLlCrOg6rjqGTFrXPh8ZlGx5KvHICPCjrioJuC5GP7xDf-9nsoT2IEf41b6bipEDSeaAGOX69e2oHWiiZstDqMmeRb2kiGMKtAXcUbU-poUg1JJdUMc-0hqDzH4cHm9fivwz5hc-PZRQwUiCoGlD6RTeFDa_s3yGQOFlxYyXH6H4odz7dMBuBXVMO4S0QrbLQS5WZrknzK2HYSEgr9xPwOBmjGiXf1iE_WdDJ_lr0_WVQBMEtG0TZX8ErviBQlGDwxF-4GTaNLYebg9jIUebUMMgLyjz73VDSAYwtvsZ8ToYyV0X7RNsGWnqH16FxcogWfHjNN5b6lUgr01MgkN1pKf8PqAUhj4hygABil9gD9nL5LrJS6Mrly6>`_ 

**Fase 1 - Predisposizione del Pacchetto di Registrazione**: L'Entità predispone le informazioni di registrazione conformemente alla tabella dei requisiti sopra riportata. Di seguito è fornito un esempio non normativo delle informazioni in formato JSON. 

.. list-table:: Campi di Primo Livello del Registro delle Fonti Autentiche
   :class: longtable
   :widths: 30 70
   :header-rows: 1

   * - **Nome Campo**
     - **Descrizione**
   * - **id**
     - OBBLIGATORIO. Identificatore univoco del Registro delle Fonti Autentiche (es. ``urn:authentic-sources:it-wallet``).
   * - **version**
     - OBBLIGATORIO. La versione del Registro delle Fonti Autentiche (es. ``1.0.0``).
   * - **last_modified**
     - OBBLIGATORIO. Il timestamp che indica quando l'elenco è stato aggiornato l'ultima volta (es. ``2025-03-15T12:00:00Z``).
   * - **localization**
     - OBBLIGATORIO. Oggetto di configurazione della localizzazione contenente:

       * **default_locale**: Codice locale predefinito (es. ``it``).
       * **available_locales**: Array dei codici locale supportati (es. ``["en", "it"]``).
       * **base_uri**: URI base per il recupero del bundle di localizzazione (es. ``https://trust-registry.eid-wallet.example.it/.well-known/l10n/authentic-sources/``).
       * **version**: Versione del formato del bundle di localizzazione.
   * - **authentic_sources**
     - OBBLIGATORIO. Un Array JSON in cui ogni voce è un Oggetto JSON che rappresenta un'entità Fonte Autentica. Ogni oggetto contiene i parametri definiti nella tabella "Parametri delle Fonti Autentiche" di seguito, inclusi identificazione dell'entità, informazioni organizzative, capacità sui dati e metodi di integrazione.

.. list-table:: Parametri delle Fonti Autentiche
   :class: longtable
   :widths: 25 15 60
   :header-rows: 1

   * - **Parametro**
     - **Tipo**
     - **Descrizione**
   * - **entity_id**
     - string
     - OBBLIGATORIO. Identificatore univoco che segue lo schema normativo: ``https://{organization_domain}[/{optional_path}]``.
   * - **organization_info**
     - oggetto JSON
     - OBBLIGATORIO. Dettagli della persona giuridica e metadati organizzativi.
   * - **organization_info.organization_name**
     -  JSON Object Array
     - OBBLIGATORIO. Array di oggetti che contengono il nome dell'organizzazione in più lingue. DEVE contenere i claim ``locale`` e ``name``.
   * - **organization_info.organization_type**
     - string
     - OBBLIGATORIO. Classificazione dell'entità: ``"public"`` o ``"private"``.
   * - **organization_info.ipa_code**
     - string
     - OBBLIGATORIO solo per FA Pubbliche. Codice di registrazione IPA per gli enti pubblici.
   * - **organization_info.legal_identifier**
     - string
     - OBBLIGATORIO. Identificativo di registrazione legale (Codice Fiscale/Partita IVA, o equivalente identificativo nazionale per entità straniere).
   * - **organization_info.homepage_uri**
     - string
     - OBBLIGATORIO. URL della homepage dell'organizzazione.
   * - **organization_info.contacts**
     - Array di stringhe
     - OBBLIGATORIO. Array di indirizzi email di contatto per almeno un referente di supporto utenti, uno applicativo e uno sistemistico.
   * - **organization_info.dpa_contact**
     - string
     - OBBLIGATORIO. Indirizzo email del DPA della Fonte Autentica.
   * - **organization_info.policy_uri**
     - string
     - OBBLIGATORIO. URL del documento di informativa sulla privacy.
   * - **organization_info.tos_uri**
     - string
     - OBBLIGATORIO solo per FA Private. URL del documento dei termini di servizio.
   * - **organization_info.organization_country**
     - string
     - OBBLIGATORIO. Codice paese ISO 3166-1 alpha-2 a due lettere dell'organizzazione.
   * - **organization_info.logo_uri**
     - string
     - OPZIONALE. URL dell'immagine del logo dell'organizzazione.
   * - **organization_info.logo_uri#integrity**
     - string
     - CONDIZIONALE. Digest crittografico della risorsa immagine del logo per la verifica dell'integrità. OBBLIGATORIO se ``logo_uri`` è presente. Formato: ``{digest_method}-{digest_value}`` (es. ``"sha-256-abc123..."``).
   * - **organization_info.logo_alt_text**
     - JSON Object Array
     - OPZIONALE. Array di oggetti contenente il testo alternativo per l'immagine del logo dell'organizzazione in più lingue. DEVE contenere i claim ``locale`` e ``description``.
   * - **organization_info.logo_extended_uri**
     - string
     - OPZIONALE. URL dell'immagine del logo esteso dell'organizzazione.
   * - **organization_info.logo_extended_uri#integrity**
     - string
     - CONDIZIONALE. Digest crittografico della risorsa immagine del logo esteso per la verifica dell'integrità. OBBLIGATORIO se ``logo_extended_uri`` è presente. Formato: ``{digest_method}-{digest_value}`` (es. ``"sha-256-abc123..."``).
   * - **organization_info.logo_extended_alt_text**
     - JSON Object Array
     - OPZIONALE. Array di oggetti contenente il testo alternativo per l'immagine del logo esteso dell'organizzazione in più lingue. DEVE contenere i claim ``locale`` e ``description``.
   * - **data_capabilities**
     - Array di oggetti JSON
     - OBBLIGATORIO. Array contenente le specifiche delle capacità sui dati.
   * - **data_capabilities[].dataset_id**
     - string
     - OBBLIGATORIO. L'identificatore univoco del dataset nell'ambito della Fonte Autentica, che PUÒ essere utilizzato come parametro di query per il servizio ``GetAttributeClaims``.
   * - **data_capabilities[].data_origin**
     - JSON Object Array
     - OBBLIGATORIO. Array di oggetti contenente il nome leggibile dell'origine o del dipartimento che fornisce i dati in più lingue. DEVE contenere i claim ``locale`` e ``name``.
   * - **data_capabilities[].intended_purposes**
     - Array di stringhe
     - OBBLIGATORIO. Finalità aziendali soddisfatte, utilizzando gli identificatori di finalità della tassonomia (es. ``["IDENTITY_VERIFICATION", "DRIVING_RIGHTS_VERIFICATION"]``).
   * - **data_capabilities[].available_claims**
     - Array di stringhe
     - OBBLIGATORIO. Claim disponibili da questa capacità dati.
   * - **data_capabilities[].available_claims.claim_name**
     - string
     - OBBLIGATORIO. Contiene il nome del claim.
   * - **data_capabilities[].available_claims.order**
     - number
     - OBBLIGATORIO. Definisce l'ordine in cui le informazioni vengono mostrate.
   * - **data_capabilities[].available_claims.mandatory**
     - boolean
     - OBBLIGATORIO. Definisce se un claim è sempre disponibile o meno.
   * - **data_capabilities[].integration_method**
     - string
     - OBBLIGATORIO. Framework di autorizzazione utilizzato per l'accesso ai dati. DEVE essere ``"pdnd"`` per le FA Pubbliche. Le FA Private POSSONO utilizzare altri framework di autorizzazione come: ``"oauth2"``, ``"api_key"``, ``"mtls"``, ecc.
   * - **data_capabilities[].integration_endpoint**
     - string
     - OBBLIGATORIO. Punto di accesso al servizio (endpoint PDND per FA Pubbliche, endpoint API per FA Private).
   * - **data_capabilities[].api_specification**
     - string
     - OBBLIGATORIO. URL del documento di specifica `OAS3`_ per questa capacità dati.
   * - **data_capabilities[].data_provision**
     - oggetto JSON
     - OPZIONALE. Capacità di fornitura dei dati e specifiche temporali.
   * - **data_capabilities[].data_provision.immediate_flow**
     - boolean
     - OBBLIGATORIO. Indica se la Fonte Autentica supporta la fornitura immediata dei dati.
   * - **data_capabilities[].data_provision.deferred_flow**
     - boolean
     - OBBLIGATORIO. Indica se la Fonte Autentica supporta la fornitura differita dei dati.
   * - **data_capabilities[].data_provision.max_response_time_minutes**
     - integer
     - CONDIZIONALE. Tempo massimo in minuti per la risposta della Fonte Autentica a una richiesta di fornitura dati differita. OBBLIGATORIO se ``deferred_flow`` è ``true``.
   * - **data_capabilities[].data_provision.notification_methods**
     - Array di stringhe
     - CONDIZIONALE. Array dei metodi di notifica supportati dalla Fonte Autentica per la fornitura dati differita, come ``"push"``, ``"poll"``. OBBLIGATORIO se ``deferred_flow`` è ``true``.
   * - **data_capabilities[].user_information**
     - JSON object Array
     - OPZIONALE. Array di Oggetti contenenti informazioni per l'Utente in più lingue sulla disponibilità dei dati. Questa stringa DEVE essere fornita dalla Fonte Autentica al Trust Anchor durante l'onboarding. La formattazione Markdown può essere testo semplice o una combinazione di testo e link. Ad esempio, se il database della Fonte Autentica contiene solo dati registrati *dopo* una data specifica, questa informazione DEVE essere comunicata tramite questa chiave. DEVE contenere i claim ``locale`` e ``description``.
   * - **data_capabilities[].administrative_expiration_user_info**
     - JSON object Array
     - OPZIONALE. Array di Oggetti contenenti informazioni per l'Utente in più lingue sulla scadenza amministrativa dei dati ed eventualmente le azioni raccomandate. Questa stringa DEVE essere fornita dalla Fonte Autentica al Trust Anchor durante l'onboarding. La formattazione Markdown può essere testo semplice o una combinazione di testo e link. DEVE contenere i claim ``locale``, ``title`` e ``description``.
   * - **data_capabilities[].allowed_states**
     - JSON object Array
     - OPZIONALE. Array di Oggetti contenente informazioni per l'Utente in più lingue sullo stato corrente dei dati forniti ed eventualmente le azioni raccomandate. I valori degli stati sono definiti nella sezione :ref:`credential-revocation:Token Status Lists`. DEVE contenere i claim ``locale``, ``title``, ``description`` e ``<Status-Type-Value>``.
     
     La formattazione Markdown può essere testo semplice o una combinazione di testo e link. DEVE contenere i claim ``locale``, ``title`` e ``description``.
   * - **data_capabilities[].service_documentation**
     - string
     - OPZIONALE. URL che punta alla documentazione del servizio della Fonte Autentica.
   * - **data_capabilities[].update_frequency**
     - string
     - OPZIONALE. Indica la frequenza con cui la Fonte Autentica aggiorna i propri dati. Valori possibili: ``"real_time"`` (aggiornamenti quasi in tempo reale, tipicamente entro minuti), ``"daily"``, ``"weekly"``, ``"monthly"``, ``"on_demand"``.
   * - **data_capabilities[].logo_uri**
     - string
     - OPZIONALE. URL dell'immagine del logo relativa ai dati.
   * - **data_capabilities[].logo_uri#integrity**
     - string
     - CONDIZIONALE. Digest crittografico della risorsa immagine del logo per la verifica dell'integrità. OBBLIGATORIO se ``logo_uri`` è presente. Formato: ``{digest_method}-{digest_value}`` (es. ``"sha-256-abc123..."``).
   * - **data_capabilities[].background_image**
     - oggetto JSON
     - OPZIONALE. Oggetto contenente informazioni sull'immagine di sfondo da visualizzare insieme ai dati. L'oggetto contiene i parametri ``uri`` e ``uri#integrity``.
   * - **data_capabilities[].watermark_image**
     - oggetto JSON
     - OPZIONALE. Oggetto contenente informazioni sull'immagine filigrana da visualizzare insieme ai dati. L'oggetto contiene i parametri ``uri`` e ``uri#integrity``.
   * - **data_capabilities[].background_color**
     - string
     - OPZIONALE. Valore stringa del colore di sfondo da visualizzare insieme ai dati.
   * - **data_capabilities[].contacts**
     - Array di stringhe
     - OPZIONALE. Array di indirizzi email di contatto del servizio clienti.

.. literalinclude:: ../../examples/as-registration-example.json
   :language: json
   :caption: Esempio non normativo di Registrazione Fonte Autentica

**Fase 2 - Validazione Tecnica**: L'Organismo di Vigilanza valida la registrazione inviata con focus su:

  - **Conformità al Registro dei Claims**: Validazione del formato dei claim, degli identificatori e della loro esistenza nel Registro dei Claims.
  - **Validazione della Tassonomia**: Verifica che le finalità dichiarate siano voci valide della tassonomia.
  - **Verifica dell'Integrazione API**:

    - **Entità Pubbliche**: Verifica della conformità alla specifica PDND dell'e-service
    - **Entità Private**: Completezza della specifica `OAS3`_ inclusi framework di autorizzazione, schemi richiesta/risposta, meccanismi di gestione errori e ambiente sandbox.

  - **Standard del Formato di Risposta**: Verifica dell'utilizzo del formato del Registro dei Claims e delle specifiche di mappatura degli stati.

**Fase 3 - Pubblicazione nel Registro delle Fonti Autentiche**: Al termine della validazione positiva:

  - L'Entità Fonte Autentica viene pubblicata nel Registro delle Fonti Autentiche con le capacità dichiarate complete.
  - La Fonte Autentica diventa rilevabile dagli Emittenti di Credenziali per le richieste di integrazione.
  - La Fonte Autentica è pronta per la fornitura operativa dei dati.

.. note::
   La registrazione della Fonte Autentica è completa e indipendente dall'integrazione con l'Emittente di Credenziali. Le Fonti Autentiche diventano rilevabili immediatamente dopo la pubblicazione nel Registro delle Fonti Autentiche, mentre la disponibilità delle Credenziali per gli Utenti finali dipende dall'autorizzazione amministrativa dalla Fonte Autentica all'Emittente di Credenziali, seguita dalla riuscita integrazione tecnica e dall'approvazione dell'Organismo di Vigilanza per l'idoneità al catalogo.

Processo di Autorizzazione dalla Fonte Autentica all'Emittente di Credenziali
------------------------------------------------------------------------------

A seguito dell'autorizzazione amministrativa dalla Fonte Autentica all'Emittente di Credenziali ottenuta durante la fase di registrazione amministrativa, le procedure di integrazione tecnica stabiliscono le connessioni API operative e i meccanismi di accesso ai dati tra gli Emittenti di Credenziali e le Fonti Autentiche.

L'integrazione tecnica comprende:

- **Configurazione degli Endpoint API**: Instaurazione di connessioni API sicure come specificato nelle specifiche tecniche delle Fonti Autentiche (e-service PDND per le Fonti Autentiche pubbliche, implementazioni `OAS3`_ per le Fonti Autentiche private).
- **Validazione della Mappatura dei Claims**: Verifica che l'implementazione dell'Emittente di Credenziali mappi correttamente le risposte della Fonte Autentica agli identificatori standardizzati del Registro dei Claims.
- **Test del Flusso dei Dati**: Validazione delle capacità di fornitura dei dati immediata o differita e dei meccanismi di gestione degli errori.
- **Implementazione della Sicurezza**: Configurazione dell'autenticazione, dell'autorizzazione e del logging di audit come richiesto dagli standard di sicurezza delle Fonti Autentiche.

Processo di Onboarding delle Entità Federate
---------------------------------------------

Le Entità Federate, tra cui Emittenti di Credenziali, Relying Party e Fornitori di Wallet, devono completare le procedure di onboarding per diventare partecipanti idonei nell'ecosistema IT-Wallet. Tale processo stabilisce la fiducia distribuita mediante l'emissione di Certificati X.509, la validazione delle Catene di Fiducia e la verifica della conformità, come descritto in :ref:`trust-infrastructure:L'Infrastruttura di Trust`.

Modello Gerarchico dell'Autorità di Federazione
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

La federazione IT-Wallet implementa un **modello di onboarding gerarchico** in cui le Entità Federate DEVONO essere registrate da uno dei seguenti attori:

  1. **Trust Anchor**: L'autorità radice con la capacità di registrare direttamente qualsiasi Entità Federata.
  2. **Intermediari**: Autorità delegate che registrano le Entità Foglia per conto del Trust Anchor.

Sia i Trust Anchor che gli Intermediari agiscono come **Autorità di Federazione** con le seguenti capacità di onboarding:

  - **Emissione di Certificati X.509**: Emettono Certificati X.509 ai propri Subordinati Immediati con opportuni vincoli di denominazione come definito in :ref:`trust-infrastructure:X.509 PKI`.
  - **Applicazione di Politiche sui Metadati**: Applicano politiche sui metadati specifiche della federazione con **effetto a cascata** (le politiche del Trust Anchor prevalgono su quelle degli Intermediari).
  - **Emissione di Trust Mark**: Emettono Trust Mark di Federazione attestanti le capacità e le concessioni dei Subordinati, conformemente al framework di fiducia.

Pertanto, le Entità Federate POSSONO essere registrate attraverso percorsi differenti:

  - **Onboarding Diretto dal Trust Anchor**: L'Entità si registra direttamente presso il Trust Anchor.
  - **Onboarding Mediato da un Intermediario**: L'Entità si registra presso un Intermediario appropriato.

Prerequisiti di Onboarding alla Federazione
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Le Entità Federate DEVONO rispettare i seguenti requisiti tecnici prima di avviare il processo di onboarding:

  - **Generazione delle Chiavi**: Le entità DEVONO generare almeno due coppie di chiavi mediante crittografia a curva ellittica come specificato in :ref:`algorithms:Algoritmi Crittografici`:

    - **Coppia di Chiavi della Federazione**: Utilizzata per firmare le Configurazioni dell'Entità e attestare le chiavi specifiche dell'applicazione. Per le best practice di sicurezza e la continuità operativa, le entità DOVREBBERO mantenere più Chiavi di Entità della Federazione (almeno due) per abilitare la rotazione sicura delle chiavi e la risposta agli incidenti senza impatto sulle entità che hanno memorizzato nella cache le Configurazioni dell'Entità.
    - **Coppia/i di Chiavi Specifiche dell'Applicazione**: Utilizzate per le operazioni protocollari specifiche dell'entità, come l'emissione e la presentazione delle Credenziali.

  - **Attestazione delle Chiavi Specifiche dell'Applicazione**: Le entità DEVONO creare Certificati X.509 auto-firmati per le proprie chiavi specifiche dell'applicazione utilizzando la Chiave Privata dell'Entità della Federazione.

  - **Predisposizione della Configurazione dell'Entità**: Le entità DEVONO pubblicare una Configurazione dell'Entità (CE) firmata con la propria Chiave Privata dell'Entità della Federazione all'endpoint ``/.well-known/openid-federation`` come definito in :ref:`trust-infrastructure:L'Infrastruttura di Trust`. La CE DEVE includere:

    - Un claim ``jwks`` contenente le Chiavi dell'Entità della Federazione in formato JSON Web Key (JWK).
    - Un claim ``iss`` con l'Identificatore dell'Entità della Federazione come definito in :ref:`trust-infrastructure:Ruoli di Federazione`.
    - Un claim ``sub`` uguale al claim ``iss``.
    - I claim ``iat`` ed ``exp`` che definiscono un intervallo di tempo valido.
    - Un claim ``metadata`` contenente i metadati specifici dell'entità organizzati per Tipologie di Metadati (vedere :ref:`credential-issuer-entity-configuration:Entity Configuration del Fornitore di Attestati Elettronici`, :ref:`relying-party-entity-configuration:Entity Configuration Relying Party`, o :ref:`wallet-provider-entity-configuration:Entity Configuration del Fornitore di Wallet`) con chiavi specifiche dell'applicazione incluse nei campi ``jwks`` dei metadati e Certificati X.509 auto-firmati nei relativi claim ``x5c``.

  - **Richiesta di Firma del Certificato X.509 (CSR)**: Le entità DEVONO predisporre una Richiesta di Firma del Certificato X.509 (CSR) in formato PKCS #10 contenente **la Chiave dell'Entità della Federazione** per l'emissione del Certificato X.509 da parte dell'Autorità di Federazione, come definito in :ref:`trust-infrastructure:Emissione di Certificati X.509`.

Requisiti di Sicurezza per la Gestione delle Chiavi
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Tutte le entità federate DOVREBBERO mantenere almeno due chiavi di firma attestate dal Trust Anchor:

- **Chiave Attiva**: Utilizzata per le operazioni di firma correnti
- **Chiave di Backup**: Disponibile per l'attivazione immediata durante incidenti o rotazione pianificata delle chiavi

Questo approccio a doppia chiave consente:
- Rotazione sicura delle chiavi senza interruzione del servizio
- Risposta rapida agli incidenti in caso di compromissione della chiave primaria
- Continuità per le entità con Configurazioni dell'Entità in cache
- Prevenzione di problemi di validazione durante le transizioni di chiave

La chiave di backup DEVE essere:
- Registrata dal Trust Anchor prima del deployment
- Pubblicata nel JWKS dell'entità accanto alla chiave attiva
- Pronta per l'attivazione immediata senza ulteriori fasi di certificazione
- Mantenuta con gli stessi standard di sicurezza della chiave attiva

Procedura di Onboarding alla Federazione
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
La procedura di onboarding alla federazione segue una procedura strutturata in 4 fasi e può essere eseguita dal Trust Anchor o da un Intermediario.

.. note::
   La seguente procedura si applica ai Fornitori di Wallet, agli Emittenti di Credenziali e alle Relying Party che desiderano effettuare l'onboarding nella federazione IT-Wallet. L'**Autorità di Federazione** si riferisce al Trust Anchor o all'Intermediario in base alle caratteristiche organizzative e alle politiche di governance della federazione.

.. note::
   Questa sezione copre i requisiti di registrazione tecnica. Tutte le informazioni amministrative, quali la validazione della persona giuridica, la conformità normativa e l'idoneità organizzativa, si considerano già raccolte e validate dall'Organismo di Vigilanza durante la fase di registrazione amministrativa, che esula dalla presente specifica tecnica. Esempi di informazioni amministrative includono: denominazione legale, numeri di registrazione dell'impresa, persone di contatto, documentazione di conformità legale e autorizzazioni operative.

.. plantuml:: plantuml/federation-onboarding-process.puml
    :width: 99%
    :alt: Processo di onboarding dell'entità federata che mostra la procedura in 4 fasi
    :caption: `Processo di Onboarding dell'Entità Federata. <https://www.plantuml.com/plantuml/svg/dLHHRnit37w_Nq7qOKYmfF6wz646l3NmqY4BXXPEr-t1G41BF5khZhf9L5B_-vqi7quvtu1XRmSToUyZFtvy5mIznCR2UzBaKOnZk6KnieSFl77ejU4jVFHEKGWLHd4ScmtvgcgxHADCYopmwYJx5M20clurwYRApla-KB2g5Wju46hXktc9lAA_8mM1XxXfJ0WfTR6egfhWyaSGdESV0cv8yJbbpMV7Hkv-le2FSMEDWdlQmwz_t5_0yc5rFc2-cSCKD_YCrkZyYAnXILvCRHGAmLq84LdHWOvWJ-SpULFlmTFM13dMCrmxtno-oyXSc_fnBntNPXkFETZnlthzJDPUVc7tp5Uk9JRwiXve4klM6PQYvatRsZqq9AXH45fdZJ8KuDd83XG6XOS9KLsJAlDICmH_ldux-m5KqMJ7UyqdsXR3h2gqKeufH9KsfOws0W3843NDNynExT0mU0gjuq23K2Nqju2z3ELxEA_81YeXQpIMz0XkHN-HIhzpxqOJfnAamQHUGqMi1_s_dq-hy7jxK2XflwBWx1Fr2rbiOOBBWPD5vck-X1kjXtuUTuObWB9eclxdrxSgFnor6azhmChJ3pk81qmDjyl_i2s3O_fE2fzS-VpqKuYR1R4aZaP_8pu6UKHM7Us5OFTKMEPwABJAGkOv5TvTkgQrbD179bcHwkAxyahWAGa91wZSQH7t2t6YJwKvFnqYVqF_9MqdPBRbAhEoKLCPPpXT2PT8fM8FWa8DiKmX1RDbqjsD-9I5A8XThFdfw5azU2prZCbsgUCJvsL_z8CQp05dRsOp-71_VhAsERBtHYRHiUbKAgXqxZYbaciDEhydKRlfpfFcTVhzKl4ncydSJ6aORu6QScw_YaSbBtJohfckDSgzOw6jHncfDschVY2FJHTqD5FcV-gKsZ3Q_tjdyxtfXSd71iwkPxEhwzdrU6AttZi_KYyV7107Hvlbs_EEMCV6_WC0>`_

**Fase 1 - Invio della Richiesta di Onboarding**: L'Entità Federata avvia il processo di onboarding inviando una richiesta di registrazione tecnica contenente le seguenti informazioni.

.. list-table:: Informazioni della Richiesta Tecnica di Onboarding alla Federazione
   :class: longtable
   :header-rows: 1
   :widths: 30 70

   * - **Categoria Informativa Tecnica**
     - **Requisiti e Descrizione**
   * - **Identificatore dell'Entità Federata**
     - **OBBLIGATORIO**. Un URL univoco che identifica l'Entità Federata come definito in :ref:`trust-infrastructure:Ruoli di Federazione`.
   * - **Chiave dell'Entità Federata (JWK)**
     - **OBBLIGATORIO**. Chiave pubblica a curva ellittica in formato JSON Web Key utilizzata per firmare le Configurazioni dell'Entità e attestare le chiavi specifiche dell'applicazione, con algoritmi crittografici specificati in :ref:`algorithms:Algoritmi Crittografici`.
   * - **Richiesta di Firma del Certificato X.509 (CSR)**
     - **OBBLIGATORIO**. CSR in formato PKCS #10 per l'emissione del Certificato X.509 da parte dell'Autorità di Federazione. La CSR DEVE:

       - Contenere **solo le Chiavi dell'Entità Federata**.
       - Essere firmata con la corrispondente Chiave Privata dell'Entità Federata.
       - Definire il Soggetto del Certificato X.509 con gli attributi richiesti come specificato in :ref:`trust-infrastructure:Emissione di Certificati X.509` per le Entità Federate.

.. warning::
   Prima di inviare la richiesta tecnica di onboarding, le Entità Federate DEVONO assicurarsi che il proprio endpoint ``/.well-known/openid-federation`` pubblichi una Configurazione dell'Entità valida (come definito in :ref:`trust-infrastructure:Entity Configuration`) firmata con la propria Chiave Privata dell'Entità Federata corrispondente alla Chiave dell'Entità Federata fornita nella richiesta. La Configurazione dell'Entità DEVE già includere le chiavi specifiche dell'applicazione nei metadati con Certificati X.509 auto-firmati nei claim ``x5c``.

Un esempio non normativo della struttura delle informazioni tecniche che le Entità Federate inviano durante la richiesta di onboarding della Fase 1:

.. literalinclude:: ../../examples/federation-onboarding-request-example.json
   :language: json
   :caption: Esempio di richiesta di onboarding alla federazione

L'esempio seguente mostra il contenuto decodificato della CSR:

.. literalinclude:: ../../examples/csr-decoded-example.txt
   :language: text
   :caption: Esempio di contenuto decodificato della CSR

.. note::
   Gli attributi del Soggetto della CSR DEVONO rispettare i requisiti specificati in :ref:`trust-infrastructure:Emissione di Certificati X.509` per le Entità Federate.

.. note::
   Le Chiavi dell'Entità Federata contenute nell'oggetto ``jwks`` e le chiavi pubbliche contenute nell'oggetto ``certificate_signing_requests`` DEVONO corrispondere. Le chiavi sono fornite in due formati: formato JWK e formato PKCS #10 CSR per l'emissione del Certificato X.509. Le chiavi specifiche dell'applicazione sono incluse solo nei metadati della Configurazione dell'Entità e NON DEVONO essere incluse nella richiesta di onboarding.

.. note::
   L'Endpoint della Configurazione dell'Entità è costruito automaticamente aggiungendo ``/.well-known/openid-federation`` all'Identificatore dell'Entità Federata (``entity_id``). Le Entità Federate non devono specificare separatamente questo endpoint nella richiesta di registrazione.

**Fase 2 - Validazione dell'Autorità di Federazione ed Emissione del Certificato X.509**: A seguito dell'invio della richiesta di onboarding, l'**Autorità di Federazione** DEVE eseguire:

  - Verifica delle informazioni fornite nella richiesta di registrazione.
  - Validazione della Configurazione dell'Entità, e dei metadati in essa contenuti, pubblicata all'endpoint ``/.well-known/openid-federation`` dell'entità (come definito in :ref:`trust-infrastructure:L'Infrastruttura di Trust`).
  - **Applicazione delle Politiche sui Metadati**: Applicazione delle politiche sui metadati specifiche della federazione ai metadati dell'entità in base alle caratteristiche organizzative e all'ambito di autorizzazione come definito in :ref:`trust-infrastructure:Subordinate Statement`. Quando registrata tramite un Intermediario, si applicano le politiche sia dell'Intermediario che del Trust Anchor, con le politiche del Trust Anchor prevalenti in caso di conflitti.
  - **Emissione del Certificato X.509**: Certificazione della Chiave dell'Entità Federata con l'emissione del Certificato X.509 utilizzando l'infrastruttura di fiducia dettagliata in :ref:`trust-infrastructure:Emissione di Certificati X.509`. Gli Intermediari DEVONO emettere Certificati X.509 utilizzando **vincoli di denominazione** appropriati che limitino l'uso di nomi DNS e URI ai soli propri subordinati.

Al termine della validazione positiva, l'entità riceve una risposta contenente una Catena di Certificati X.509 in cui:

  - Il primo elemento è il Certificato X.509 contenente la Chiave dell'Entità Federata (emesso dall'Autorità di Federazione).
  - **Per l'onboarding da Trust Anchor**: Il secondo elemento è il Certificato X.509 auto-firmato del Trust Anchor per la validazione del primo Certificato X.509.
  - **Per l'onboarding da Intermediario**: Gli elementi aggiuntivi includono il Certificato X.509 dell'Intermediario e il Certificato auto-firmato del Trust Anchor, formando una catena di Certificati X.509 completa.
  - Tutti i Certificati X.509 sono espressi in formato DER e codificati in Base64.

Esempio di risposta con catena di Certificati X.509:

.. code-block:: json

   [
     "MIIDqjCCA1GgAwIBAgIGAZc6/V9qMAoGCCqGSM49BAMCMIGzMQsw...",
     "MIIDQzCCAuigAwIBAgIGAZc6+XlDMAoGCCqGSM49BAMCMIGzMQsw..."
   ]

.. note::
   Se il processo di emissione fallisce, l'entità richiedente riceve una risposta con i problemi identificati da risolvere prima di inviare una nuova richiesta di onboarding.

.. note::
   Ciascuna entità può raccogliere la propria Catena di Certificati X.509 ottenendo il Certificato X.509 auto-firmato del Trust Anchor, incluso nell'oggetto ``jwks`` della Configurazione dell'Entità, e aggregando tutti i valori ``x5c`` pubblicati dalle entità superiori, dal Trust Anchor fino al suo superiore immediato. Questo consente all'entità di ricostruire la catena di certificati completa necessaria per la validazione e l'instaurazione della fiducia all'interno della federazione.

**Fase 3 - Recupero della Dichiarazione del Subordinato**: come conferma del successo del processo di onboarding, l'entità DEVE recuperare la Dichiarazione del Subordinato che la riguarda dalla Federazione Immediata utilizzando l'endpoint ``/fetch`` come definito in :ref:`trust-infrastructure:Endpoint API di Federazione`.

Esempio di richiesta fetch:

.. code-block:: http

    GET /fetch?sub=https%3A%2F%2Fcredentials.example.gov HTTP/1.1
    Host: trust-anchor.example.gov

.. note::
   Se l'endpoint ``/fetch`` risponde con codice di stato ``400`` o ``404``, l'entità DEVE risolvere i problemi descritti nel messaggio di risposta prima di richiamare nuovamente l'endpoint fetch. 

**Fase 4: Aggiornamento della Configurazione dell'Entità e Completamento dell'Onboarding**

A seguito della richiesta fetch, l'**Autorità di Federazione** restituisce la Dichiarazione del Subordinato dell'entità, un JWT firmato contenente:

  - **Metadati dell'Entità**: I metadati validati dell'entità con le politiche di federazione applicate.
  - **Informazioni sulla Fiducia**: Informazioni sul rapporto di fiducia tra l'Autorità di Federazione e l'entità, inclusa la `x5c` emessa nell'oggetto `jwk` relativo al Subordinato.
  - **Trust Mark**: I Trust Mark emessi dall'Autorità di Federazione per l'ambito operativo e le capacità specifiche dell'entità.

     Esempio di JWK di Federazione relativo al Subordinato incluso il Certificato X.509 emesso:

     .. code-block:: json

         {
           "kid": "NsXymfIILEPR5Y0t",
           "kty": "EC",
           "x": "gXY4FApFJCj91Gpb1K9GEIouTq2X3L0K64Iq0ob4l_g",
           "y": "l-6dcrIrFVdrzoY9cRJv9zNuFOR3MsDz6TSDhB0xEo4",
           "crv": "P-256",
           "x5c": [
             "MIIDqjCCA1GgAwIBAgIGAZc6/V9qMAoGCCqGSM49BAMCMIGzMQsw..."
           ]
         }

L'Entità Federata DEVE completare il processo di onboarding:

  1. **Aggiornare e Pubblicare la Configurazione dell'Entità**:

    Il contenuto dell'endpoint ``/.well-known/openid-federation`` deve essere aggiornato per includere i seguenti claim:

     - Aggiungere un claim ``authority_hints`` con un Array JSON contenente l'Identificatore dell'Entità Federata dell'**Autorità di Federazione immediata** (Trust Anchor per l'onboarding diretto, o Intermediario per l'onboarding mediato) come definito in :ref:`trust-infrastructure:Ruoli di Federazione`.

     - **Integrare i Trust Mark**: Includere i Trust Mark della Dichiarazione del Subordinato nella Configurazione dell'Entità usando il claim ``trust_marks`` come specificato in :ref:`trust-infrastructure:Entity Configuration Foglie e Intermediari`.

     Esempio di aggiunta di authority_hints:

     .. code-block:: json

         {
           "iat": 1718207217,
           "exp": 1749743216,
           "iss": "https://credentials.example.gov",
           "sub": "https://credentials.example.gov",
           "authority_hints": ["https://trust-anchor.example.gov"],
           //...
         }

     Esempio di integrazione dei Trust Mark:

     .. code-block:: json

         "trust_marks": [
           {
             "trust_mark_type": "https://trust-anchor.example.gov/trust_marks/federation-entity/credential-issuer",
             "trust_mark": "eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL3RydXN0LWFuY2hvci5leGFtcGxlLmdvdiIsInN1YiI6Imh0dHBzOi8vY3JlZGVudGlhbC1pc3N1ZXIuZXhhbXBsZS5nb3YiLCJ0cnVzdF9tYXJrX3R5cGUiOiJodHRwczovL3RydXN0LWFuY2hvci5leGFtcGxlLmdvdi90cnVzdF9tYXJrcy9mZWRlcmF0aW9uLWVudGl0eS9jcmVkZW50aWFsLWlzc3VlciIsImlhdCI6MTcwMDAwMDAwMCwiZXhwIjoxNzMwMDAwMDAwfQ.abc123signature"
           }
         ]

.. note::
   Per aggiornare i Trust Mark dopo l'onboarding, l'entità può utilizzare l'endpoint fetch del proprio superiore immediato per ottenere tutti i Trust Mark aggiornati che la riguardano. Quando l'emittente del Trust Mark è diverso dall'entità superiore che ha registrato l'entità, le Entità Federate possono ottenere Trust Mark aggiornati in qualsiasi momento utilizzando l'endpoint Federation Trust Mark come definito in :ref:`trust-infrastructure:Endpoint API di Federazione`.

Al completamento positivo della Fase 4, **l'onboarding dell'entità è completato con successo**. L'entità è ora operativa all'interno della federazione IT-Wallet e pronta per le attività operative.
   

.. note::
   **Integrazione nel Registro della Federazione**: Al completamento positivo dell'onboarding, l'Identificatore dell'Entità Federata dell'entità diventa rilevabile tramite i meccanismi di listing del Trust Anchor (come definito in :ref:`trust-infrastructure:L'Infrastruttura di Trust`), indicando la partecipazione attiva alla federazione. L'entità diventa parte dell'infrastruttura di federazione dettagliata in :ref:`registry:Infrastruttura del Registro`.

Trust Mark della Federazione IT-Wallet
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Le Entità Federate ricevono i Trust Mark della Federazione IT-Wallet al completamento positivo dell'onboarding. **I Trust Mark sono emessi dall'Autorità di Federazione** (Trust Anchor per l'onboarding diretto, Intermediario per l'onboarding mediato) e fungono da attestazioni verificabili sulla conformità ai profili tecnici IT-Wallet e/o alle politiche di autorizzazione.

Tipologie e Schema dei Trust Mark
""""""""""""""""""""""""""""""""""

Le Entità POSSONO ricevere più Trust Mark per finalità diverse. Gli identificatori dei Trust Mark DEVONO seguire uno schema gerarchico che rispecchia l'ambito di autorizzazione:

``https://<federation_authority_domain>/trust_marks/<purpose>/<entity_type>``

Dove:

  - ``<federation_authority_domain>``: Il dominio dell'Autorità di Federazione emittente.
  - ``<purpose>``: La finalità del Trust Mark. La finalità ``federation-entity`` è **OBBLIGATORIA** per tutte le entità. Finalità aggiuntive dei Trust Mark POSSONO essere supportate, come ``authorization_policy`` per definizioni granulari dell'ambito operativo.
  - ``<entity_type>``: La tipologia dell'entità destinataria (es. ``credential-issuer``, ``relying-party``, ``wallet-provider``).

Struttura dei Trust Mark
"""""""""""""""""""""""""

I Trust Mark nella Configurazione dell'Entità DEVONO essere rappresentati come oggetti JSON contenenti i seguenti claim:

.. list-table:: Claim dell'Oggetto Trust Mark (nella Configurazione dell'Entità)
   :class: longtable
   :header-rows: 1
   :widths: 20 80

   * - **Claim**
     - **Descrizione**
   * - **trust_mark_type**
     - **OBBLIGATORIO**. Identificatore della tipologia di Trust Mark secondo lo schema: ``https://<federation_authority_domain>/trust_marks/<purpose>/<entity_type>``.
   * - **trust_mark**
     - **OBBLIGATORIO**. Un JSON Web Token firmato che rappresenta il Trust Mark emesso dall'Autorità di Federazione.

Il JWT del Trust Mark (contenuto nel claim ``trust_mark`` di cui sopra) include i seguenti claim:

.. list-table:: Claim del JWT del Trust Mark
   :class: longtable
   :header-rows: 1
   :widths: 20 80

   * - **Claim**
     - **Descrizione**
   * - **iss**
     - **OBBLIGATORIO**. Autorità di Federazione emittente il Trust Mark (superiore immediato: Trust Anchor o Intermediario).
   * - **sub**
     - **OBBLIGATORIO**. Identificatore dell'Entità Federata del soggetto.
   * - **trust_mark_type**
     - **OBBLIGATORIO**. Identificatore univoco del Trust Mark, DEVE corrispondere al claim ``trust_mark_type``.
   * - **iat**
     - **OBBLIGATORIO**. Timestamp di emissione del Trust Mark.
   * - **exp**
     - **OBBLIGATORIO**. Timestamp di scadenza del Trust Mark.
   * - **organization_type**
     - **OBBLIGATORIO**. Tipologia organizzativa dell'entità (``public`` o ``private``).
   * - **vat_number**
     - **RACCOMANDATO**. Partita IVA dell'entità (tipicamente per le organizzazioni private).
   * - **legal_identifier**
     - **RACCOMANDATO**. Numero o identificativo di registrazione legale dell'entità (es. numero di registrazione dell'impresa, codice fiscale).
   * - **ipa_code**
     - **RACCOMANDATO**. Codice IPA (Indice delle Pubbliche Amministrazioni) per le entità del settore pubblico.
   * - **organization_name**
     - **RACCOMANDATO**. Denominazione completa dell'Entità Organizzativa.
   * - **email**
     - **RACCOMANDATO**. Email istituzionale o PEC dell'organizzazione.
   * - **logo_uri**
     - **OBBLIGATORIO**. URL che punta al :ref:`brand-identity:Trust Mark` per scopi UI/UX.
   * - **ref**
     - **OPZIONALE**. URL con informazioni web aggiuntive sul Trust Mark.

I seguenti esempi non normativi illustrano diversi contenuti del JWT del Trust Mark per l'appartenenza alla federazione e diverse politiche di autorizzazione:

.. code-block:: json

   {
     "iss": "https://trust-anchor.eid-wallet.example.it",
     "sub": "https://ci.public-authority.gov.example",
     "trust_mark_type": "https://trust-anchor.eid-wallet.example.it/trust_marks/federation-entity/credential-issuer",
     "iat": 1718207217,
     "exp": 1749743216,
     "organization_type": "public",
     "ipa_code": "pub_001",
     "legal_identifier": "12345678901",
     "organization_name": "Public Authority Services",
     "email": "registry@public-authority.gov.example"
   }

.. code-block:: json

   {
     "iss": "https://trust-anchor.eid-wallet.example.it",
     "sub": "https://rental.cars.example.com",
     "trust_mark_type": "https://trust-anchor.eid-wallet.example.it/trust_marks/authorization_policy/relying-party",
     "iat": 1718207217,
     "exp": 1749743216,
     "organization_type": "private",
     "vat_number": "IT12345678901",
     "legal_identifier": "12345678901",
     "organization_name": "Premium Car Rental Services Ltd",
     "email": "compliance@rental.cars.example.com",
     "authorized_claims": ["given_name", "family_name", "driving_privileges"],
     "authorized_credential_types": ["mobile-driving-license"],
     "scope_restrictions": {
       "domains": ["MOBILITY_TRAVEL"],
       "purposes": ["DRIVING_RIGHTS_VERIFICATION"]
     }
   }

.. code-block:: json

   {
     "iss": "https://trust-anchor.eid-wallet.example.it",
     "sub": "https://private-badge.ci.example.com",
     "trust_mark_type": "https://trust-anchor.eid-wallet.example.it/trust_marks/authorization_policy/credential-issuer",
     "iat": 1718207217,
     "exp": 1749743216,
     "organization_type": "private",
     "vat_number": "IT98765432101",
     "legal_identifier": "98765432101",
     "organization_name": "Badge Services Ltd",
     "email": "compliance@rprivate-badge.ci.example.com",
     "authorized_claims": ["given_name", "family_name", "company_id"],
     "authorized_credential_types": ["example-company-badge"],
     "scope_restrictions": {
       "domains": ["EMPLOYMENT"],
       "purposes": ["ACCESS_PERMIT"]
     }
   }

Le Entità Federate DEVONO integrare i Trust Mark nella propria Configurazione dell'Entità utilizzando il claim ``trust_marks`` come specificato in :ref:`trust-infrastructure:Entity Configuration Foglie e Intermediari`. Le Entità POSSONO ricevere più Trust Mark per diversi ambiti di autorizzazione.

.. code-block:: json

   {
     "iss": "https://credentials.example.gov",
     "sub": "https://credentials.example.gov",
     "jwks": { 
      // contenuto jwks
     },
     "authority_hints": ["https://trust-anchor.eid-wallet.example.it"],
     "trust_marks": [
       {
         "trust_mark_type": "https://trust-anchor.eid-wallet.example.it/trust_marks/federation-entity/credential-issuer",
         "trust_mark": "eyJhbGciOiJFUzI1NiIsImtpZCI6IlRydXN0QW5jaG9yS2V5SWQiLCJ0eXAiOiJKV1QifQ..."
       }
     ],
     "metadata": { 
      // contenuto dei Metadati
     }
   }

.. code-block:: json

   {
     "iss": "https://healthcare-ci.example.gov",
     "sub": "https://healthcare-ci.example.gov",
     "jwks": { 
      // contenuto jwks
     },
     "authority_hints": ["https://healthcare.intermediate.eid-wallet.example.it"],
     "trust_marks": [
       {
         "trust_mark_type": "https://healthcare.intermediate.eid-wallet.example.it/trust_marks/federation-entity/credential-issuer",
         "trust_mark": "eyJhbGciOiJFUzI1NiIsImtpZCI6IkhlYWx0aGNhcmVJbnRlcm1lZGlhdGVLZXlJZCIsInR5cCI6IkpXVCJ9..."
       }
     ],
     "metadata": { 
      // contenuto dei Metadati  
    }
   }

Validazione dei Trust Mark
"""""""""""""""""""""""""""

I partecipanti alla federazione validano lo stato dei Trust Mark tramite due meccanismi:

1. **Validazione Statica**: Verifica crittografica utilizzando la chiave pubblica dell'Autorità di Federazione emittente dalla Catena di Fiducia.
2. **Validazione Dinamica**: Verifica dello stato in tempo reale, contro eventuali revoche, utilizzando l'endpoint ``/trust_mark_status`` dell'Autorità di Federazione come definito in :ref:`trust-infrastructure:Endpoint API di Federazione`.

Per le procedure complete di gestione dei Certificati X.509, inclusa la validazione della catena, la verifica delle revoche e la gestione del ciclo di vita, vedere :ref:`x5c-evaluation:Operazioni di Gestione dei Certificati X.509`.



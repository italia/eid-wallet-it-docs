.. include:: ../common/common_definitions.rst


Infrastruttura del Registro
============================

L'ecosistema IT-Wallet opera attraverso un'infrastruttura di registro che fornisce definizioni standardizzate dei dati, registrazione delle entità e capacità di discovery delle credenziali. Il sistema di registro è composto da più componenti interconnessi che supportano l'intero ciclo di vita delle operazioni degli Attestati Elettronici, dall'onboarding delle entità alla presentazione delle credenziali.

L'architettura del registro è necessaria a definire i requisiti di standardizzazione semantica, gestione del trust della federazione e discovery delle credenziali attraverso componenti di registro specializzati che garantiscono interoperabilità e conformità in tutto l'ecosistema.

Panoramica dell'Architettura del Registro
------------------------------------------

Il sistema di registro IT-Wallet comprende cinque componenti principali:

  1. **Registro degli Attributi**: Definizioni semantiche standardizzate per singoli attributi delle credenziali, tipi di dati e regole di validazione.
  2. **Registro delle Fonti Autentiche (AS)**: Catalogo dei fornitori di dati registrati con le loro capacità dichiarate e claim disponibili.
  3. **Registro della Federazione**: Elenco autorevole delle entità fidate che partecipano alla federazione con le loro configurazioni tecniche.
  4. **Catalogo degli Attestati Elettronici**: Meccanismo di discovery pubblico per i tipi di credenziali disponibili con i loro metadati e informazioni di rilascio.
  5. **Tassonomia**: Sistema di classificazione gerarchica che organizza le credenziali per dominio e scopo.

Questi componenti del registro sono interconnessi e mantenuti dall'Organismo di Supervisione per garantire coerenza, sicurezza e conformità normativa in tutto l'ecosistema.

Endpoint di Discovery del Registro
----------------------------------

Il Trust Anchor DEVE fornire un meccanismo di discovery per tutti i componenti del registro attraverso endpoint *well-known* standardizzati che forniscono metadati e informazioni di discovery delle API REST per gestire operazioni complesse come paginazione e filtraggio.

Il Trust Anchor DEVE pubblicare i metadati di discovery del registro all'endpoint ``.well-known/it-wallet-registry`` con supporto per la negoziazione del contenuto:

  - **Content-Type Predefinito**: ``application/jwt`` (JWT firmato che garantisce autenticità e integrità)
  - **Content-Type Alternativo**: ``application/json`` (JSON semplice per scopi di sviluppo/debug)

Inoltre, il sistema di registro IT-Wallet DEVE utilizzare due modelli di accesso distinti:

  - **API del Registro Dati**: DEVONO supportare capacità di paginazione e filtraggio.
  - **Infrastruttura di Trust della Federazione**: come definito in :ref:`trust-infrastructure:L'Infrastruttura di Trust`.

Di seguito viene fornito un esempio non normativo.

.. code-block:: http

    GET /.well-known/it-wallet-registry HTTP/1.1
    Host: trust-anchor.eid-wallet.example.it
    Accept: application/jwt

    HTTP/1.1 200 OK
    Content-Type: application/jwt

    eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...

.. code-block:: http

    GET /.well-known/it-wallet-registry HTTP/1.1
    Host: trust-anchor.eid-wallet.example.it
    Accept: application/json

    HTTP/1.1 200 OK
    Content-Type: application/json

Struttura del payload JWT (decodificato):

.. code-block:: json

    {
      "registry_version": "1.0",
      "last_updated": "2024-03-15T10:30:00Z",
      "endpoints": {
        "claims_registry": "https://trust-anchor.eid-wallet.example.it/api/v1/claims",
        "authentic_sources": "https://trust-anchor.eid-wallet.example.it/api/v1/authentic-sources",
        "credential_catalog": "https://trust-anchor.eid-wallet.example.it/api/v1/credential-catalog",
        "taxonomy": "https://trust-anchor.eid-wallet.example.it/api/v1/taxonomy",
        "federation_list": "https://trust-anchor.eid-wallet.example.it/list",
        "federation_fetch": "https://trust-anchor.eid-wallet.example.it/fetch",
        "federation_resolve": "https://trust-anchor.eid-wallet.example.it/resolve",
        "federation_trust_mark_status": "https://trust-anchor.eid-wallet.example.it/trust_mark_status",
        "federation_historical_keys": "https://trust-anchor.eid-wallet.example.it/historical-jwks"
      },
      "content_negotiation": ["application/json", "application/jwt"]
    }



Registro degli Attributi
------------------------------

Il **Registro degli Attributi** fornisce definizioni semantiche standardizzate per singoli attributi delle credenziali, tipi di dati e regole di validazione. Questo registro serve come fondamento semantico per la standardizzazione degli attributi delle credenziali in tutto l'ecosistema IT-Wallet, lavorando in coordinamento con il componente Tassonomia per la classificazione gerarchica.

L'Organismo di Supervisione DEVE mantenere il Registro degli Attributi per garantire coerenza semantica e conformità normativa in tutto l'ecosistema. Il registro DEVE contenere:

  - **Claim Standardizzati**: Definizioni semantiche per tutti gli attributi delle credenziali con tipi di dati e regole di validazione.
  - **Mappature di Interoperabilità**: Definizioni di alias per gli attributi che utilizzano terminologie diverse tra gli standard (ad esempio, ISO18013-5 ``place_of_birth`` mappato al canonico ``birth_place``).
  - **Formati dei Dati**: Tipi di dati standardizzati (string, date, numeric, boolean, email, url, image, array, object) con pattern di validazione.

Il Registro degli Attributi DEVE garantire:

  - **Coerenza Semantica**: Previene conflitti tra attributi duplicati o ridondanti in tutto l'ecosistema.
  - **Interoperabilità Transfrontaliera**: Garantisce conformità UE e interpretazione coerente degli attributi.
  - **Validazione dello Schema**: Fornisce definizioni autorevoli per la validazione degli attributi in tutti gli scenari di credenziali.
  - **Allineamento Normativo**: Si coordina con il quadro normativo nazionale ed europeo.
  - **Scenari Credential-Agnostic**: Supporta scenari in cui la **convenienza dell'utente** e l'**efficienza operativa aziendale** sono prioritarie rispetto alla **conformità normativa** e ai **log di audit**.

.. note::
   Il Registro degli Attributi definisce le proprietà semantiche dei singoli attributi, ma NON DEVE specificare le capacità di selective disclosure. La selective disclosure dipende dalle implementazioni del formato delle credenziali (SD-JWT, mDocs), dalle configurazioni tecniche dell'emittente e dal contesto di presentazione. Queste capacità sono specificate a livello del tipo di credenziale all'interno del Catalogo degli Attestati Elettronici e implementate durante i flussi di presentazione delle credenziali.


Utilizzo del Registro degli Attributi
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Il Registro degli Attributi DEVE supportare l'intero ciclo di vita dell'ecosistema:

**Durante il Processo di Onboarding**:

  - **Registrazione AS**: Le Fonti Autentiche dichiarano i proprio claim disponibili tra quelli presenti nel registro standardizzato durante la registrazione delle capacità di fornitura dati.
  - **Registrazione CI**: I Credential Issuer selezionano le entità AS basandosi sugli attributi richiesti e registrano i tipi di credenziali per la pubblicazione nel catalogo.
  - **Registrazione RP**: Le Relying Party specificano i requisiti di autorizzazione utilizzando domini/scopi per tipi di credenziali specifici e/o attributi dell'Utente.

**Durante le Attività Operative**:

  - **Rilascio di Credenziali**: Le definizioni degli attributi garantiscono rappresentazione coerente dei dati tra diversi tipi di credenziali.
  - **Richieste di Presentazione**: Le RP fanno riferimento agli attributi per la validazione dello schema e la verifica dell'autorizzazione in scenari sia credential-specific che credential-agnostic.
  - **Applicazione delle Policy**: Le policy di autorizzazione sfruttano le classificazioni dominio/scopo per il controllo degli accessi.


Struttura del Registro degli Attributi
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Il Registro degli Attributi mantiene definizioni tecniche, linguisticamente neutrali per la coerenza semantica in tutto l'ecosistema. Le localizzazioni rivolte all'utente per nomi e descrizioni degli attributi sono fornite attraverso i bundle di localizzazione del Catalogo degli Attestati Elettronici, abilitando un supporto multilingue efficiente senza compromettere l'integrità strutturale del registro.

Un esempio non normativo della struttura del Registro degli Attributi è fornito di seguito:

.. literalinclude:: ../../examples/claims-registry-example.json
  :language: JSON

Registro delle Fonti Autentiche
--------------------------------

L'Organismo di Supervisione DEVE mantenere il Registro delle Fonti Autentiche per abilitare l'accesso coordinato ai dati e il rilascio di credenziali in tutto l'ecosistema. Il Registro AS DEVE contenere almeno:

  - **Informazioni sull'Organizzazione**: Dettagli dell'entità legale, stato normativo e ruolo autorevole all'interno di domini specifici.
  - **Capacità di Fornitura Dati**: Disponibilità dichiarata degli attributi che fanno riferimento alle definizioni standardizzate del Registro degli Attributi con le corrispondenti classificazioni della Tassonomia.
  - **Metodi di Integrazione**: Meccanismi di accesso tecnico (PDND per AS pubbliche, API personalizzate per AS private).
  - **Scopi Previsti**: Tipi di credenziali supportati e contesti aziendali per il coordinamento AS-CI.
  - **Garanzia della Qualità dei Dati**: Stato autoritativo, frequenza di aggiornamento e capacità di traccia di audit.

Il Registro AS DEVE garantire:

  - **Accesso Coordinato ai Dati**: Abilita la discovery CI di dati appropriati dalle Fonti Autentiche per il rilascio di credenziali.
  - **Integrazione AS-CI**: Facilita i flussi di lavoro di approvazione e il coordinamento dell'accesso ai dati tra le entità.
  - **Garanzia della Qualità**: Mantiene lo stato autoritativo e l'affidabilità dei dati tra diversi domini.
  - **Conformità Normativa**: Supporta i requisiti di trasparenza dell'amministrazione pubblica e il coordinamento del settore privato.

Utilizzo del Registro AS
^^^^^^^^^^^^^^^^^^^^^^^^^

Il Registro AS supporta il coordinamento dell'ecosistema durante tutto il ciclo di vita operativo:

**Durante il Processo di Onboarding**:
  - **Auto-Dichiarazione AS**: Le Fonti Autentiche registrano le specifiche prima che esista un qualsiasi tipo di credenziali nel catalogo.
  - **Discovery dei CI**: I Credential Issuer cercano entità AS basandosi sugli attributi richiesti e sui tipi di credenziali previsti.
  - **Coordinamento delle Approvazioni**: Le entità AS valutano e approvano le richieste di accesso CI per la fornitura di dati.

**Durante le Attività Operative**:
  - **Risoluzione della Fonte Dati**: I sistemi CI fanno riferimento al Registro AS per l'accesso ai dati in tempo reale durante il rilascio delle credenziali.
  - **Validazione della Qualità**: Le informazioni del Registro AS supportano la verifica dell'origine dei dati e i requisiti di audit.
  - **Gestione dell'Integrazione**: Gli endpoint tecnici e i metodi di accesso abilitano la comunicazione standardizzata AS-CI.

Coordinamento AS Pubbliche vs Private
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

L'architettura del Registro AS supporta diversi pattern di coordinamento che riflettono requisiti operativi distinti:

  1. **AS dell'Amministrazione Pubblica** (Integrazione Standardizzata): Le entità governative forniscono dati autorevoli attraverso meccanismi regolamentati:

    - **Integrazione PDND**: ``"integration_method": "pdnd_eservice"`` per l'accesso standardizzato ai dati governativi.
    - **Conformità Normativa**: Requisiti di trasparenza completa con pubblicazione nel catalogo pubblico.
    - **Requisiti di Audit**: Tracciabilità completa per i processi di rilascio delle credenziali governative.

  2. **AS del Settore Privato** (Integrazione Flessibile): Le entità private forniscono dati specializzati attraverso accordi personalizzati:

    - **API Personalizzate**: ``"integration_method": "custom_api"`` per pattern di accesso ai dati specifici dell'azienda.
    - **Selective Disclosurea**: Visibilità pubblica limitata con flussi di lavoro di approvazione specifici per CI.
    - **Flessibilità Aziendale**: Integrazione su misura che supporta diversi casi d'uso del settore privato.

Questo approccio abilita sia la **trasparenza normativa** per l'amministrazione pubblica che la **flessibilità aziendale** per le entità del settore privato mantenendo l'accesso coordinato ai dati in tutto l'ecosistema.

Struttura del Registro AS
^^^^^^^^^^^^^^^^^^^^^^^^^^

Durante la registrazione, le Fonti Autentiche dichiarano le loro specifiche prima che esista un qualsiasi tipo di credenziale nel catalogo. Questa dichiarazione stabilisce le fondamenta per la successiva registrazione CI e creazione di tipi di credenziali.

Schema dell'Identificatore Univoco AS
""""""""""""""""""""""""""""""""""""""

Ad ogni Fonte Autentica DEVE essere assegnato un identificatore univoco che segue lo schema URL HTTPS definito di seguito. Questo identificatore è utilizzato per fare riferimento alle entità AS in tutto il sistema di registro e nel Catalogo degli Attestati Elettronici, garantendo coerenza con i pattern di identificazione delle entità OpenID Federation.

**Schema dell'Identificatore AS:**

.. code-block:: text

    https://{organization_domain}[/{optional_path}]

**Componenti dello Schema:**

  - **organization_domain**: Dominio DNS controllato dall'organizzazione
  - **optional_path**: Componente di path aggiuntivo per servizi o dipartimenti specifici


L'identificatore AS DEVE seguire queste regole normative:

1. **Protocollo HTTPS**: DEVE utilizzare lo schema HTTPS per sicurezza e verifica del trust
2. **Proprietà del Dominio**: L'organizzazione DEVE controllare il dominio DNS utilizzato nell'identificatore
3. **Unicità**: Garantita attraverso l'unicità del namespace DNS
4. **Stabilità**: DOVREBBE rimanere stabile nel tempo per evitare la corruzione dei riferimenti
5. **Risolvibilità**: L'URL DOVREBBE essere risolvibile (anche se non è richiesto che serva contenuto)

**Esempi di identificatori AS conformi:**

  - ``https://motorizzazione.gov.example``: Pubblico - Ministero dei Trasporti, Dipartimento Motorizzazione
  - ``https://registry.anpr.example``: Pubblico - Anagrafe Nazionale della Popolazione Residente
  - ``https://api.bank.example/auth-source``: Privato - Servizi Finanziari Banca Esempio
  

Parametri del Registro AS
""""""""""""""""""""""""""

Il Registro AS DEVE contenere i seguenti parametri per ogni Fonte Autentica registrata:

.. list-table:: Registro AS - Parametri Richiesti
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
     - JSON object
     - OBBLIGATORIO. Dettagli dell'entità legale e metadati organizzativi.
   * - **organization_info.organization_name**
     - string
     - OBBLIGATORIO. Nome legale dell'organizzazione.
   * - **organization_info.organization_type**
     - string
     - OBBLIGATORIO. Classificazione dell'entità: ``"public"`` o ``"private"``.
   * - **organization_info.ipa_code**
     - string
     - OBBLIGATORIO solo per AS Pubbliche. Codice di registrazione IPA per entità governative.
   * - **organization_info.legal_identifier**
     - string
     - OBBLIGATORIO. Identificatore di registrazione legale (Codice Fiscale/Partita IVA, o identificatore nazionale equivalente per entità straniere).
   * - **organization_info.homepage_uri**
     - string
     - OBBLIGATORIO. URL che punta alla homepage dell'organizzazione.
   * - **organization_info.contacts**
     - String Array
     - OBBLIGATORIO. Array di indirizzi email di contatto tecnico/amministrativo.
   * - **organization_info.policy_uri**
     - string
     - OBBLIGATORIO. URL al documento della privacy policy.
   * - **organization_info.tos_uri**
     - string
     - OBBLIGATORIO solo per AS Private. URL al documento dei termini di servizio.
   * - **organization_info.organization_country**
     - string
     - OBBLIGATORIO. Codice paese ISO 3166-1 alpha-2 a due lettere dell'organizzazione.
   * - **organization_info.logo_uri**
     - string
     - OPZIONALE. URL al logo dell'organizzazione.
   * - **organization_info.service_documentation**
     - string
     - OPZIONALE. URL che punta alla documentazione del servizio della Fonte Autentica.
   * - **organization_info.user_information**
     - string
     - OPZIONALE. Una stringa contenente informazioni "human-readable" sulla Attestato Elettronico rilevante per l'Utente. Questa stringa DEVE essere fornita dalla Fonte Autentica al Trust Anchor durante l'onboarding e DEVE essere formattata utilizzando il formato Markdown come definito in :rfc:`7763`. La formattazione Markdown può essere testo semplice o una combinazione di testo e link. Ad esempio, se il database della Fonte Autentica contiene solo i dati richiesti per gli attributi dell'Attestato Elettronico registrati *dopo* una data specifica, questa informazione DEVE essere comunicata al Trust Anchor in questa stringa Markdown.
   * - **data_capabilities**
     - JSON Objects Array
     - OBBLIGATORIO. Array contenente le specifiche delle capacità dei dati.
   * - **data_capabilities[].domains**
     - String Array
     - OBBLIGATORIO. Dominio della tassonomia (ad esempio, ``["AUTHORIZATION"]``, ``["FINANCIAL"]``).
   * - **data_capabilities[].intended_purposes**
     - String Array
     - OBBLIGATORIO. Scopi aziendali serviti (ad esempio, ``["driving-authorization", "identity-verification"]``).
   * - **data_capabilities[].available_claims**
     - String Array
     - OBBLIGATORIO. I claim disponibili da questa capacità di fornitura dati.
   * - **data_capabilities[].integration_method**
     - string
     - OBBLIGATORIO. Framework di autorizzazione utilizzato per l'accesso ai dati. DEVE essere ``"pdnd"`` per AS Pubbliche. Le AS Private POSSONO utilizzare altri framework di autorizzazione come: ``"oauth2"``, ``"api_key"``, ``"mtls"``, ecc.
   * - **data_capabilities[].integration_endpoint**
     - string
     - OBBLIGATORIO. Punto di accesso al servizio (endpoint PDND per AS Pubbliche, endpoint API per AS Private).
   * - **data_capabilities[].api_specification**
     - string
     - OBBLIGATORIO. URL al documento di specifica OpenAPI 3.0 per questa capacità di fornitura dati.
   * - **data_capabilities[].data_provision**
     - JSON object
     - OPZIONALE. Capacità di fornitura dati e specifiche di tempistica.
   * - **data_capabilities[].data_provision.immediate_flow**
     - boolean
     - OBBLIGATORIO. Indica se la Fonte Autentica supporta la fornitura immediata dei dati.
   * - **data_capabilities[].data_provision.deferred_flow**
     - boolean
     - OBBLIGATORIO. Indica se la Fonte Autentica supporta la fornitura differita dei dati.
   * - **data_capabilities[].data_provision.max_response_time_minutes**
     - integer
     - CONDIZIONALE. Tempo massimo in minuti per la Fonte Autentica per rispondere a una richiesta di fornitura dati differita. OBBLIGATORIO se ``deferred_flow`` è ``true``.
   * - **data_capabilities[].data_provision.notification_methods**
     - String Array
     - CONDIZIONALE. Array di metodi di notifica supportati dalla Fonte Autentica per la fornitura dati differita, come ``"push"``, ``"poll"``. OBBLIGATORIO se ``deferred_flow`` è ``true``.
   * - **data_capabilities[].update_frequency**
     - string
     - OPZIONALE. Indica quanto frequentemente la Fonte Autentica aggiorna i suoi dati. Valori possibili: ``"real_time"`` (aggiornamenti quasi in tempo reale, tipicamente entro minuti), ``"daily"``, ``"weekly"``, ``"monthly"``, ``"on_demand"``.
   * - **display**
     - JSON object
     - OPZIONALE. Suggerimenti di branding visivo che le Fonti Autentiche possono fornire per le credenziali che utilizzano i loro dati.
   * - **display.background_color**
     - string
     - OPZIONALE. Colore di sfondo suggerito per le credenziali in formato esadecimale (ad esempio, ``"#003d82"``).
   * - **display.text_color**
     - string
     - OPZIONALE. Colore del testo suggerito per le credenziali in formato esadecimale (ad esempio, ``"#ffffff"``).
   * - **display.logo_uri**
     - string
     - OPZIONALE. URI al logo della Fonte Autentica per il branding delle credenziali.
   * - **display.logo_uri#integrity**
     - string
     - CONDIZIONALE. Digest crittografico del logo per la verifica dell'integrità. OBBLIGATORIO se ``logo_uri`` è presente. Formato: ``{digest_method}-{digest_value}`` (ad esempio, ``"sha-256-abc123..."``)
   * - **display.template_uri**
     - string
     - OPZIONALE. URI a un template visivo che la Fonte Autentica suggerisce per le credenziali che utilizzano i loro dati.
   * - **display.template_uri#integrity**
     - string
     - CONDIZIONALE. Digest crittografico del template per la verifica dell'integrità. OBBLIGATORIO se ``template_uri`` è presente. Formato: ``{digest_method}-{digest_value}`` (ad esempio, ``"sha-256-def456..."``).

Esempio del Registro AS
"""""""""""""""""""""""

Un esempio non normativo della struttura del Registro AS è fornito di seguito:

.. literalinclude:: ../../examples/as-registry-example.json
  :language: JSON

Coordinamento AS-CI
^^^^^^^^^^^^^^^^^^^

Dopo la registrazione AS, il Registro AS abilita i Credential Issuer a scoprire entità AS adatte e richiedere l'approvazione dell'integrazione. Questo processo di coordinamento è dettagliato in :ref:`entity-onboarding:Processo di Integrazione AS-CI`.

Registro della Federazione
---------------------------

Il **Registro della Federazione** fornisce l'infrastruttura di trust crittografico per tutti i partecipanti dell'ecosistema IT-Wallet. Il Registro della Federazione mantiene l'elenco autorevole delle entità fidate e il loro stato operativo utilizzando endpoint specifici della federazione come definito in :ref:`trust-infrastructure:Endpoint API di Federazione`.

Ruolo di Integrazione del Registro
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

All'interno dell'architettura del registro IT-Wallet, il Registro della Federazione serve come **livello di validazione del trust** per:

1. **Autenticazione delle Entità**: Valida l'identità crittografica di tutti i partecipanti prima delle operazioni del registro
2. **Verifica della Catena di Trust**: Fornisce le fondamenta crittografiche per la validazione delle entità Credential Issuer, Relying Party e Wallet Provider
3. **Verifica della Conformità**: Mantiene Trust Mark che attestano la conformità normativa e lo stato operativo

Accesso al Registro della Federazione
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Le operazioni del Registro della Federazione sono accessibili attraverso gli endpoint della federazione del Trust Anchor come dettagliato in :ref:`trust-infrastructure:Endpoint API di Federazione`. L'architettura di discovery del registro fornisce informazioni sugli endpoint della federazione tramite l'Endpoint di Discovery del Registro descritto in `Endpoint di Discovery del Registro`_.

.. note::
   Gli endpoint della federazione sono disponibili sia attraverso il meccanismo di discovery del registro (per l'accesso unificato al registro) che attraverso l'Entity Configuration del Trust Anchor a ``.well-known/openid-federation`` (per operazioni specifiche della federazione). Entrambe le fonti forniscono gli stessi URL degli endpoint ma servono pattern di discovery diversi: discovery del registro per l'orientamento iniziale dell'ecosistema, Entity Configuration per la conformità standard OpenID Federation 1.0.

Per le specifiche tecniche complete dei protocolli di federazione, configurazioni delle entità, meccanismi di valutazione del trust e validazione della catena di trust, vedere :ref:`trust-infrastructure:L'Infrastruttura di Trust`.

Catalogo degli Attestati Elettronici
-------------------------------------

Il Catalogo degli Attestati Elettronici è il registro di tutti gli Attestati Elettronici disponibili riconosciuti all'interno dell'ecosistema IT-Wallet. È pubblicato dal Trust Anchor e pubblicamente disponibile da tutte le Entità attraverso un endpoint specializzato della Federazione. Agisce come un singolo punto di riferimento per tutti gli attori coinvolti nel processo di rilascio, verifica e utilizzo degli Attestati Elettronici.

Il Catalogo degli Attestati Elettronici mira a:

  1. Facilitare la discovery degli Attestati Elettronici per gli Utenti.
  2. Standardizzare la descrizione tecnica e funzionale degli Attestati Elettronici.
  3. Abilitare l'interoperabilità tra diversi Issuer e Relying Party.
  4. Semplificare il processo di integrazione per Wallet Provider e Relying Party.
  5. Garantire il trust nell'ecosistema attraverso informazioni certificate.
  6. Fornire trasparenza sull'ecosistema degli Attestati Elettronici disponibili.


Le principali Entità coinvolte nel Catalogo degli Attestati Elettronici sono:

  - **Trust Anchor**: Gestisce e mantiene il Catalogo degli Attestati Elettronici, garantendone l'autenticità e l'integrità.
  - **Organismo di Supervisione**: Interagisce con il Trust Anchor e il Catalogo degli Attestati Elettronici per monitorare la fase di registrazione garantendo sicurezza e privacy secondo le normative nazionali/europee, mantenendo tutte le informazioni affidabili e aggiornate.
  - **Credential Issuer**: Le entità autorizzate a rilasciare Attestati Elettronici, registrandoli nel Catalogo.
  - **Relying Party**: Utilizzano il Catalogo degli Attestati Elettronici per raccogliere tutte le informazioni necessarie sugli Attestati Elettronici che intendono richiedere durante la fase di presentazione.
  - **Wallet Provider**: Accedono al Catalogo degli Attestati Elettronici per identificare gli Attestati Elettronici disponibili e per recuperare tutte le informazioni necessarie per integrarli nelle loro Soluzioni Wallet.
  - **Utenti**: Gli Utenti che utilizzano indirettamente il Catalogo degli Attestati Elettronici attraverso le loro Istanze del Wallet per scoprire e richiedere Attestati Elettronici.
  - **Fonti Autentiche**: Le Entità che detengono i dati originali che sono attestati negli Attestati Elettronici. Forniscono supporto agli Issuer nella registrazione degli Attestati Elettronici nel Catalogo.


.. _fig_catalog.svg:
.. plantuml:: plantuml/credential-catalog-entities.puml
    :width: 99%
    :alt: La figura illustra le Entità degli Attestati Elettronici.
    :caption: `Diagramma Entità-Relazione del Catalogo degli Attestati Elettronici. <https://www.plantuml.com/plantuml/svg/ZLJ1Rkis4BpxAxP6WQP00X-QtjeWgPEsFXGmuXGz6ZIvbeb8fCfTEbM__YrDELAUb6ST34khuSnmESjxOXKuLYKysiAoAc4PqA1ZcnwL57mH4Pwam1Pfzfrrkem6uPVbxM9vkrtwglPEy7UpsG_mY7lh43RhvzNBqwO7vbWh4tvQQ5zLtjsDVDbxnpVg3SbNUFFpGcDWkxTQCKv06p6wKpG5MdhzEW4M2GDDyUcBAJ1XEsAO07p5PgAx2J1hjbe5Cm69_-c3SWLkLSbJ-etqohwUW7nJPOaNAHVM4LkER5CuPhFtL5tfSmIlOJvCA7KHdGlW6GjB79hql1H4471eQ-3t85v07PKjrQv46A6JXTzJ7IpZh_DpfkO_Yg4r1lBkAlLTkF-MlvE6PVi_EeAtWmTZINivP53EYEg_4OalQIG-uU-soo4IFpXzy4dd9Rr1VarwwVUNSgf0EgbKoZgM7m4Vy9i3t1ULY8dcfY76wefYBT6qv4FpcpUD26ow2gJIITGxopxGkPig7HJK1qK8w2W6wmeWrFB0pScQQ1sLRlgwlP7kz2rHn42Zfmkh_34vU8WiJP1k6y3sBf9DAuP4SF4isq7eP0EMZNXUgv2OKdHo0ThAF9_ogQ_l4GJsK2Wf1R1kxqELsw1sFZBeSUN-O7NoUIhMmH-joRl_vrI1jjJkMMia6dgmZh48Yh4lcgeUCl471xdKQIlfP5gZDpu64KX2vnAqjQJ-foyD-22DTTBOD0sWc54uZ6XTx7Wtq6c0fBqVijrjg8lqTPVd7A6uAoqTiflVHQMD7JfJUm4Ahz0E4_nnXbQEPQ5c6LBBX_4rVJkVXZtuT1gPe8jjVs6-VZ2CzGQiQvSE-tyc6pSxo6fVyezFuZXc8TCDizVnTP7pO4_BzatlmjG3hdmV3XZJw12qaLuvOkKqGfq11dPDNhvzR0dw3bREs82Qo-RzHgN-bKfVsRYNECIg_080>`_


.. .. figure:: ../../images/catalog.svg
..     :figwidth: 100%
..     :align: center
..     :target: https://www.plantuml.com/plantuml/svg/ZLHDZnit3BtxLp16WMw1E3wqlHGeaDJR3mD9Qwopw751I_HOM8qq5JdhJdzzAMkyCnixs3aOy53aUq_aezwpO9AszhCtBXZVMeA3ICC_BPS9Z-yg9uTsrp8b4uDGa7Scril6OyWr2nRhtMwv-c6noQ7xJn-NDR9Gqj33AjPD3BccoVYpR-6MzYuGR3Ttwy-_RcTlRFbUh_xwy_xkumHYQHkqwVj1WDFJnLup5jma9yGz_t2R7dofvNKCHSh5uGa1ZyInfiMFIqD9tDuP59fMO55mXpmnsqVpE2qptvydQexLn4p5VA8qBVUHkkbAfsKw-s0msMd9zAyvOAZe0RrC70NneyHcMl8HlQSfm4iNM9oquiuUcisU_NrZKD37ggMtCBzrbTClM2MoUkRGCwpEvtDDkAFAiQGk_rzfHjBarCSWxa4b0JwXyxZp15VWjF2RulQVvsVZpRzJGHjA7CDD7eLYtpEb4uSJzny5XkCXWdLieauVC5Xb_QSbbjSuCfxY3zULrB9y2EOGCy_d_0NbC_FbtoSCM16VM6fqGVJ788ThzncwCoPLuoddjcEX-eRRHZthEARkbsWx9TWE4SYX4saCJcBYSpSn3mkQ0p811MwJ2nKm6VqZtKcQSZsXwSQyezKV-1rpIuclJXVMvJ0h-D2ADa6xRI4VYgDyQHJ80A_Eib-CWJQHxrJp1bD6ojOf0UWZypBbKr-VBGWIeK8D9N1X7rDTse2xs0gOwypZBHleot9iKdnojjp-xrC4-b1_PsE8-LA32q9LGg4nQOv6AC0l59JGm8tQoLnZjh5DIf29pY7eOvdzZ-WjnAID3UWXRmEW22c6LQvNEpuiTLuWRUyBRmyN6YpzTl1piL2xyuuFHSrlojBRZe9jeYOghi9UElZb3gs3QA4HXgEJm_MQiPolcZt5F8q2CDXsN5YU7qhNUWCkzAMN_J-3NHTxuTKnvUzVi-CL2GNkqdi3tc2v2EvKjkz63wQvm2hluGLYNXs6tjBhm8B143GbmSAkA-KFjpt0MC4wM9V8YE-UNrGUFwdyXOpt56nR-_y1


La seguente tabella riassume le principali informazioni che DEVONO essere fornite dal Catalogo degli Attestati Elettronici:

.. list-table:: Catalogo degli Attestati Elettronici - Informazioni principali
   :class: longtable
   :widths: 30 70
   :header-rows: 1

   * - Informazioni relative a
     - Descrizione
   * - Metadati degli Attestati Elettronici
     - Informazioni identificative essenziali e caratteristiche degli Attestati Elettronici, inclusi:

       - **Identificatore univoco delle credenziali**: Una stringa identificatore univoco di ogni Attestato Elettronico.
       - **Metodi di autenticazione dell'utente**: Meccanismi di autenticazione dell'utente utilizzati per richiedere l'Attestato Elettronico, se richiesto dagli Issuer o dalle Fonti Autentiche.
       - **Livello di Garanzia minimo**: Il Livello di Garanzia minimo richiesto per l'affidabilità dell'Attestato Elettronico. DEVE tenere conto del Livello di Garanzia dell'autenticazione dell'Utente, quando applicabile, e dell'Istanza del Wallet.
       - **Caratteristiche di visualizzazione aggiuntive**: Specifiche visive e di formattazione, come un'immagine di riferimento di sfondo, logo, ecc.
   * - Credential Issuer
     - Dettagli sull'organizzazione autorizzata a rilasciare l'Attestato Elettronico, come:

       - **Identificatori dell'issuer**: Identificatore univoco per il Credential Issuer.
       - **Tipo di issuer**: Classificazione come PID, (Q)EAA, o Fornitore Pub-EAA.
       - **Informazioni aggiuntive**: Dettagli organizzativi inclusi nome, codice e informazioni di contatto.
   * - Fonti Autentiche
     - Informazioni sulla fonte dati autorevole.
   * - Specifiche Tecniche
     - Dettagli tecnici, inclusi:

       - **Schemi degli Attestati Elettronici**: Specifiche del framework e della struttura.
       - **Formati degli Attestati Elettronici**: Standard di formato dati e codifica.
       - **Policy di autenticazione**: Metodi e requisiti per la verifica.
   * - Termini di Utilizzo
     - Condizioni e limitazioni per l'utilizzo degli Attestati Elettronici, come:

       - **Validità delle credenziali**: Periodo di tempo durante il quale l'Attestato Elettronico è valido e, quando applicabile, meccanismi e dettagli tecnici per invalidare gli Attestati Elettronici (metodi di revoca/sospensione).
       - **Policy di restrizione**: Se applicabile, regole che governano l'uso e le limitazioni dell'Attestato Elettronico secondo le normative nazionali. È utilizzata, ad esempio, per specificare se solo specifici tipi legali di Entità, ad esempio Fornitore Pub-EAA e Soluzioni Wallet pubbliche, sono autorizzate a rilasciare e ottenere l'Attestato Elettronico.
       - **Policy di costo**: Informazioni relative ai modelli di costo dell'Attestato Elettronico, come `free`, `issuance_based`, `verification_based`.
       - **Scopi degli Attestati Elettronici**: Informazioni relative agli scopi consentiti per i quali l'Attestato Elettronico può essere utilizzato. Ogni tipo di Attestato Elettronico può essere utilizzato per scopi multipli.


Il Trust Anchor DEVE pubblicare e mantenere aggiornate tutte le informazioni all'endpoint `.well-known` del Catalogo degli Attestati Elettronici garantendo affidabilità, autenticità e integrità dei dati. In particolare, il Catalogo degli Attestati Elettronici, i claim e la tassonomia DEVONO essere disponibili attraverso l'endpoint ``.well-known/credential-catalog``.

Gerarchia degli Attestati Elettronici
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gli Attestati Elettronici riconosciuti all'interno dell'ecosistema IT-Wallet sono classificati e standardizzati gerarchicamente secondo i seguenti domini e scopi principali. Scopi aggiuntivi POSSONO essere aggiunti man mano che l'ecosistema IT-Wallet cresce.

.. _it-wallet-dc-domains:
.. list-table:: Domini e Scopi degli Attestati Elettronici
   :class: longtable
   :header-rows: 1
   :widths: 20 30 50

   * - **Dominio**
     - **Scopo**
     - **Descrizione**
   * - *IDENTITY*
     - * PERSON_IDENTIFICATION
       * ELECTRONIC_RESIDENCY
     - Credenziali che stabiliscono o verificano l'identità di una persona, inclusi documenti di identità fisici e digitali legalmente riconosciuti dalle leggi nazionali.
   * - *AUTHORIZATION*
     - * DRIVING_LICENSE
       * PROFESSIONAL_LICENSE
       * TRAVEL_DOCUMENT
       * ACCESS_PERMIT
     - Credenziali che concedono permessi, diritti o autorizzazioni specifiche per svolgere certe attività o accedere ad aree ristrette.
   * - *EDUCATION*
     - * ACADEMIC_DEGREE
       * CERTIFICATE
       * TRAINING_RECOGNITION
     - Credenziali relative a risultati educativi, qualifiche e riconoscimento di formazione professionale.
   * - *HEALTH*
     - * INSURANCE_CARD
       * DISABILITY_CARD
       * MEDICAL_PRESCRIPTION
     - Credenziali relative all'accesso sanitario, storia medica, copertura assicurativa e documenti relativi alla salute.
   * - *FINANCIAL*
     - * INCOME_CERTIFICATE
       * TAX_STATEMENT
       * FAMILY_ECONOMIC_STATUS
       * BANK_ACCOUNT
       * PAYMENT_HISTORY
     - Credenziali che attestano lo stato finanziario, livelli di reddito, tassazione, informazioni bancarie o situazione economica di individui o famiglie.
   * - *MEMBERSHIP*
     - * ASSOCIATION
       * LOYALTY_PROGRAM
       * CLUB_MEMBERSHIP
     - Credenziali che confermano l'affiliazione con organizzazioni, partecipazione a programmi o stato di appartenenza.
   * - *ATTESTATION*
     - * PUBLIC_STATEMENT
       * CIVIL_STATUS
       * CERTIFICATION
     - Credenziali che forniscono dichiarazioni ufficiali, conferme di stato o certificazioni rilasciate dalle autorità.


Ogni Credenziale DEVE specificare domini e scopi per abilitare sia **Scenari Credential-Specific** che **Scenari Credential-Agnostic** secondo i requisiti delle Relying Party e i pattern di richiesta di presentazione:

  1. **Scenari Credential-Specific** (Primari per Settori Governativi/Regolamentati): Le RP richiedono tipi specifici di credenziali per requisiti di conformità e audit, inclusi ad esempio:

    - **Servizi Governativi**: ``"vct_values": ["urn:eudi:pid:it:1"]`` per la verifica dell'identità specifica del PID.
    - **Controlli di Polizia**: ``"docType": "org.iso.18013.5.1.mDL"`` per la verifica della patente di guida.
    - **KYC Bancario**: Tipi di credenziali specifici richiesti dalle normative finanziarie.
    - **Servizi Sanitari**: ``"vct_values": ["urn:eudi:european_disability_card:it:1"]`` per l'accesso ai benefici per disabilità conforme all'UE.

  2. **Scenari Credential-Agnostic** (Tipici per Aziende Private): Le RP richiedono gli attributi specifichi indipendentemente dalla fonte delle credenziali per efficienza operativa, come:

    - **Consegna E-commerce**: Qualsiasi credenziale, tra quelle a cui è autorizzato ad accedere, contenente ``given_name``, ``family_name``, ``address`` per la spedizione.
    - **Abbonamenti**: Qualsiasi credenzialetra quelle a cui è autorizzato ad accedere, con ``given_name``, ``email`` per la personalizzazione.
    - **Personalizzazione del Servizio**: Applicazioni aziendali che richiedono dati personali di base senza forti requisiti di fonte.

Questo approccio consente:

  - **Autorizzazione basata su policy** tramite l'utilizzo della mappatura dominio/scopo.
  - **Registrazione RP flessibile** che supporta sia le esigenze di conformità governativa che i requisiti operativi aziendali.


Struttura del Catalogo degli Attestati Elettronici
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Il contenuto del Catalogo degli Attestati Elettronici è protetto in un JWS che contiene i seguenti parametri dell'header JOSE:

.. _table_catalog_parameters:
.. list-table::
   :class: longtable
   :header-rows: 1
   :widths: 25 50 25

   * - Header JOSE
     - Descrizione
     - Riferimento
   * - **typ**
     - OBBLIGATORIO. DEVE essere impostato a ``JOSE``.
     - [:rfc:`7515` Sezione 4.1.9].
   * - **alg**
     - OBBLIGATORIO. Un identificatore di algoritmo di firma digitale come per il registro IANA "JSON Web Signature and Encryption Algorithms". DEVE essere uno degli algoritmi supportati nella Sezione :ref:`Algoritmi Crittografici <algorithms:Algoritmi Crittografici>` e NON DEVE essere impostato a ``none`` o con un identificatore di algoritmo simmetrico (MAC).
     - [:rfc:`7515` Sezione 4.1.1].
   * - **kid**
     - OBBLIGATORIO. Identificatore univoco della chiave pubblica.
     - [:rfc:`7515` Sezione 4.1.4].
   * - **x5c**
     - OPZIONALE. Contiene il Certificato X.509 della chiave pubblica o la catena di Certificati [:rfc:`5280`] corrispondente alla chiave utilizzata per firmare digitalmente il JWS. Quando il valore del parametro header `kid` è presente, DEVE riferirsi alla stessa chiave pubblica crittografica del leaf utilizzata con il Certificato X.509.
     - [:rfc:`7515` Sezione 4.1.6.].
   * - **cty**
     - OBBLIGATORIO. DEVE essere impostato a ``application/json``.
     - [:rfc:`7515` Sezione 4.1.6.].

Il payload JWS contiene i seguenti parametri:

.. list-table:: Campi di Primo Livello del Catalogo
   :class: longtable
   :header-rows: 1
   :widths: 30 70

   * - Nome Campo
     - Descrizione
   * - **catalog_version**
     - OBBLIGATORIO. Versione del formato del Catalogo degli Attestati Elettronici.
   * - **iss**
     - OBBLIGATORIO. Identificatore dell'issuer del Catalogo degli Attestati Elettronici.
   * - **last_modified**
     - OBBLIGATORIO. Timestamp dell'ultima modifica al Catalogo degli Attestati Elettronici.
   * - **credentials**
     - OBBLIGATORIO. Array contenente le definizioni degli Attestati Elettronici.
   * - **wallet_app_attestation**
     - OBBLIGATORIO. Un Oggetto JSON contenente  informazioni relative alle Wallet App Attestation, inclusi i loro formati supportati e attributi associati. Questo Oggetto è utilizzato da altre entità, come il Fornitore di Attestati Elettronici e il Fornitore di Servizi, per recuperare informazioni sui formati di Wallet App Attestation supportati all'interno dell'ecosistema.

Ogni elemento dell'array ``credentials`` contiene almeno le seguenti informazioni:

.. list-table:: Campi di Primo Livello di Ogni Voce di Credenziale
  :class: longtable
  :header-rows: 1
  :widths: 30 70

  * - Nome Campo
    - Descrizione
  * - **version**
    - OBBLIGATORIO. Versione della definizione dell'Attestato Elettronico.
  * - **credential_type**
    - RICHIESTO. Identificatore univoco del tipo di Attestato Elettronico. Per il PID DEVE essere ``pid``.
  * - **legal_type**
    - RICHIESTO. Classificazione legale della Credenziale (ad esempio, ``pub-eaa``, ``qeaa``, ``eaa``).
  * - **vct**: 
    - RICHIESTO. DEVE essere impostato come un URN del formato definito in :ref:`credential-data-model:Credential SD-JWT Parameters`. La corrispondenza dei letterali inclusi in questa stringa URN DEVE essere eseguita tenendo conto della distinzione tra maiuscole e minuscole.
  * - **restriction_policy**
    - OPZIONALE. Restrizioni legali su Soluzioni Wallet e/o Credential Issuer autorizzati a richiedere/rilasciare l'Attestato Elettronico.

      * **allowed_wallet_ids**: Elenco degli identificatori delle Soluzioni Wallet consentite.
      * **allowed_issuer_ids**: Elenco degli identificatori dei Credential Issuer consentiti. Se presente, rappresenta una whitelist di Credential Issuer che possono essere aggiunti dal Trust Anchor nel campo **issuers** dell'Attestato Elettronico corrispondente.
  * - **pricing_policy**
    - OPZIONALE. Informazioni sui prezzi degli Attestati Elettronici, inclusi:

      * **models**: OBBLIGATORIO. Array di modelli di costo applicabili all'Attestato Elettronico, ognuno contenente

        - **pricing_type**: Tipo di modello di costo, come ``issuance_based``, ``verification_based``, ``subscription_based``, ``other``.
        - **price**: Costo associato al modello.
        - **currency**: Valuta del costo.

      * **pricing_model_uri**: URI alla documentazione dettagliata del modello di costo.
  * - **validity_info**
    - Informazioni sulla validità degli Attestati Elettronici, inclusi almeno:

      * **max_validity_days**: Periodo di validità massimo in giorni.
      * **status_methods**: Metodi di verifica dello stato supportati (ad esempio ``status_list``).
      * **allowed_states**: Stati degli Attestati Elettronici consentiti (ad esempio ``valid``, ``revoked``, ``suspended``).
  * - **authentication**
    - OBBLIGATORIO. Requisiti di autenticazione degli Attestati Elettronici.

      * **user_auth_required**: OBBLIGATORIO. Flag che indica se l'autenticazione dell'Utente è richiesta durante il rilascio dell'Attestato Elettronico.
      * **min_loa**: OBBLIGATORIO. Livello di Garanzia minimo OBBLIGATORIO per l'autenticazione dell'Attestato Elettronico. DEVE includere il Livello di Garanzia dell'autenticazione dell'Utente e dell'Istanza del Wallet che richiede l'Attestato Elettronico.
      * **supported_eid_schemes**: OBBLIGATORIO se ``user_auth_required`` è ``true``. Schemi di autenticazione dell'identità digitale supportati.
  * - **purposes**
    - OBBLIGATORIO. Array di scopi di utilizzo per i quali l'Attestato Elettronico può essere utilizzato, definendo contesti di utilizzo specifici e attributi richiesti per ogni scopo, come:

      * **id**: Identificatore univoco per lo scopo (ad esempio, "driving-authorization", "person-identification").
      * **description**: Descrizione "human-readable" dello scopo con un suffisso ``_l10n_id`` per la localizzazione del contenuto.
      * **claims_required**: Array di identificatori di attributi che sono richiesti quando si utilizza la Credenziale per questo scopo.
      * **claims_recommended**: Array di identificatori di attributi che sono raccomandati ma non obbligatori per questo scopo.
  * - **issuers**
    - OBBLIGATORIO. Array di informazioni rilevanti sui Credential Issuer autorizzati, inclusi dati amministrativi e tecnici come nome dell'Organizzazione, riferimento al documento di specifica API e meccanismi di rilascio supportati (ad esempio il supporto del flusso differito).
  * - **authentic_sources**
    - OBBLIGATORIO. Array di identificatori stringa che fanno riferimento alle Fonti Autentiche autorizzate come registrate nel :ref:`registry:Registro delle Fonti Autentiche`. Ogni identificatore corrisponde a un valore ``entity_id`` dal Registro AS, che fornisce metadati organizzativi e tecnici completi incluse capacità di fornitura dati, metodi di integrazione e informazioni di contatto.
  * - **formats**
    - OBBLIGATORIO. Array di formati tecnici supportati degli Attestati Elettronici, inclusi:

      * **format**: Tipo di formato (ad esempio, ``dc+sd-jwt``, ``mso_mdoc``)
      * **configuration_id**: Identificatore di configurazione del :term:formato Credenziale. Questo è formato concatenando il valore ``credential_type`` al ``format`` (ad esempio, ``dc_sd_jwt_mDL`` o ``mso_mdoc_mDL``), ed è utilizzato per fare riferimento univocamente alla configurazione per questo :term:formato Credenziale.
      * **docType**: CONDIZIONALE. È OBBLIGATORIO solo se il ``format`` è ``mso_mdoc``. Se la :term:Credenziale è:

        * definita da uno standard ISO, DEVE essere una stringa della forma ``iso.org.{iso-number}.{part}.{version}.{credential_type}`` (ad esempio, ``iso.org.18013.5.1.mDL``).
        * definita a livello europeo, DEVE essere una stringa della forma ``eu.europa.ec.{credential_type}.{version}`` (ad esempio, ``eu.europa.ec.loyaltycard.1.0``).
        * definita da uno standard nazionale, DEVE essere una stringa della forma ``{dominio inverso Trust Anchor}.{credential_type}.{version}`` (ad esempio, ``it.wallet.trust-registry.pid.1``).
      * **schema_uri**: URI che punta al documento di specifica del formato.
      * **schema_uri#integrity**: Digest crittografico del documento di specifica del formato per la verifica dell'integrità. DEVE essere una stringa della forma ``{digest_method}-{digest_value}``, dove ``{digest_method}`` è l'algoritmo di digest utilizzato (ad esempio, ``sha-256``) e ``{digest_value}`` è il valore del digest codificato in base64url.


L'Oggetto ``wallet_app_attestation`` contiene almeno le seguenti informazioni:


.. list-table:: Campi di Primo Livello di Ogni Voce di Credenziale
  :class: longtable
  :header-rows: 1
  :widths: 30 70

  * - Nome Campo
    - Descrizione
  * - **credential_type**
    - OBBLIGATORIO. Identificatore univoco della Wallet App Attestation. DEVE essere impostato a ``wallet_app_attestation``.
  * - **vct**
    - OBBLIGATORIO. DEVE essere impostato come un URN nel formato definito in :ref:`credential-data-model:Credential SD-JWT Parameters`. La corrispondenza dei letterali inclusi in questa stringa URI DEVE essere eseguita in modo case-sensitive.
  * - **formats**
    - OBBLIGATORIO. Array di formati supportati per la Wallet App Attestation, inclusi:

      * **format**: Tipo di formato (ad esempio, ``dc+sd-jwt``, ``mso_mdoc`` o ``oauth-client-attestation+jwt``)
      * **configuration_id**: Identificatore di configurazione della Wallet App Attestation. Questo è formato concatenando la stringa ``wa`` al ``format`` (ad esempio, ``dc_sd_jwt_wa``, ``mso_mdoc_wa``, o ``jwt_wa``), ed è utilizzato per fare riferimento univocamente alla configurazione del formato della Wallet App Attestation.
      * **docType**: CONDIZIONALE. È presente solo se il ``format`` è ``mso_mdoc``. È una stringa della forma ``{dominio inverso Trust Anchor}.{credential_type}`` (ad esempio, ``it.wallet.trust-registry.wallet_app_attestation``).
      * **schema_uri**: URI che punta al documento di specifica del formato.
      * **schema_uri#integrity**: Digest crittografico del documento di specifica del formato per la verifica dell'integrità. DEVE essere una stringa della forma ``{digest_method}-{digest_value}``, dove ``{digest_method}`` è l'algoritmo di digest utilizzato (ad esempio, ``sha-256``) e ``{digest_value}`` è il valore del digest codificato in base64url.

L'esempio corrispondente del Catalogo degli Attestati Elettronici come decodificato in JSON sia per header che payload è il seguente:

.. literalinclude:: ../../examples/catalog-example-header.json
  :language: JSON

.. literalinclude:: ../../examples/catalog-example-payload.json
  :language: JSON

.. note::
  Per una gestione migliore e più efficiente della localizzazione delle informazioni contenute nel Catalogo degli Attestati Elettronici, un'Entità che lo consulta DOVREBBE:

    - Scaricare la versione base del Catalogo degli Attestati Elettronici (compatta, senza localizzazioni) utilizzando l'endpoint ``.well-known/credential-catalog``.
    - Determinare la lingua preferita dell'Utente.
    - Scaricare solo i bundle di localizzazione necessari.
    - Unire dinamicamente il contenuto localizzato con la struttura del Catalogo degli Attestati Elettronici.

  Un esempio non normativo di output di un bundle di localizzazione è fornito di seguito:

    .. code-block:: json

      {
        "driving_license.name": "Patente di Guida",
        "driving_license.description": "Patente di guida ufficiale valida in Italia e nell'UE",
        "purpose.driving_authorization.name": "Abilitazione alla guida",
        "purpose.driving_authorization.description": "Verifica di Abilitazione alla guida",
        "claims.given_name.name": "Nome",
        "...": "..."
      }

  I bundle di localizzazione DEVONO essere disponibili all'URI specificato nell'attibuto **localization_info.bundles_base_uri** del Catalogo degli Attestati Elettronici. Ogni bundle locale DEVE essere accessibile seguendo il pattern di denominazione **{locale_code}.json**, dove **{locale_code}** è sostituito con il codice locale corrispondente dall'array **available_locales**.

  Un esempio non normativo dell'URI di localizzazione italiana per il bundle mDL sarebbe **https://trust-registry.eid-wallet.example.it/.well-known/l10n/mdl/it.json**.

  Le Entità DOVREBBERO verificare l'integrità dei bundle di localizzazione scaricati utilizzando il metodo di digest e i valori specificati nel claim **localization_info.integrity**. Questo garantisce che i dati di localizzazione non siano stati manomessi durante la trasmissione.

Il Catalogo come Fonte Canonica per le Informazioni di Visualizzazione
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  Per ridurre la duplicazione garantendo coerenza di presentazione nell'ecosistema, il Catalogo degli Attestati Elettronici è la fonte canonica delle informazioni di visualizzazione rivolte all'Utente finale relative agli Attestati Elettronici (ad es. nome/descrizione dell'Attestato Elettronico, etichette degli attributi, template visivi, colori, URI del logo).

  - Per gli Attestati inclusi nel Catalogo degli Attestati Elettronici, le Soluzioni Wallet e le Relying Party DEVONO utilizzare i campi relativi alla visualizzazione recuperati tramite il ``vct`` contenuto nel Catalogo per la rappresentazione degli Attestati Elettronici e dei relativi Attributi.

  - Per gli Attestati che non sono inclusi nel Catalogo degli Attestati Elettronici (ad esempio, Attestati non considerati di interesse pubblico), le Soluzioni Wallet POSSONO utilizzare le informazioni di visualizzazione provenienti dai metadati del Fornitore di Attestati Elettronici e/o dal Type Metadata dell’Attestato Elettronico. Quando entrambe le fonti sono disponibili, si applica la seguente regola di precedenza:

    1. Utilizzare il Type Metadata dell'Attestato Elettronico, se disponibile.
    2. In caso contrario, utilizzare i Metadata del Fornitore di Attestati Elettronici.

- Le implementazioni DOVREBBERO memorizzare nella cache i dati di visualizzazione del Type Metadata e applicare la selezione della lingua utilizzando il parametri ``locale``.


Tassonomia
----------

La **Tassonomia** fornisce le fondamenta semantiche per l'interoperabilità degli Attestati Elettronici mantenendo il vocabolario autorevole per organizzare le credenziali all'interno dell'ecosistema IT-Wallet. La tassonomia è neutrale rispetto al formato delle credenziali e ha l'obiettivo di facilitare le integrazioni degli Attestati Elettronici nelle Soluzioni Tecniche IT-Wallet.

La tassonomia fornisce, in una singola risorsa, il sistema di classificazione gerarchica che organizza domini e scopi che possono essere applicati ai tipi di credenziali, supportando la valutazione delle policy di autorizzazione e la standardizzazione a livello di ecosistema.

**Obiettivi della Tassonomia:**

1. **Fondamento Semantico**: Stabilire vocabolario standardizzato per domini e scopi in tutto l'ecosistema
2. **Framework delle Policy**: Abilitare decisioni di autorizzazione strutturate basate sulla classificazione gerarchica
3. **Interoperabilità**: Garantire interpretazione coerente delle classificazioni delle credenziali
4. **Estensibilità**: Supportare l'evoluzione dell'ecosistema con nuovi domini e scopi
5. **Conformità Transfrontaliera**: Allinearsi con i requisiti normativi UE e gli standard internazionali

**Struttura della Tassonomia:**

La tassonomia mantiene una struttura gerarchica a due livelli:

- **Domini**: Classificazione di livello superiore che rappresenta aree funzionali ampie (ad esempio, IDENTITY, AUTHORIZATION, FINANCIAL)
- **Scopi**: Casi d'uso specifici delle credenziali all'interno di ogni dominio (ad esempio, PERSON_IDENTIFICATION, DRIVING_LICENSE, BANK_ACCOUNT) per i quali le credenziali possono essere utilizzate

**Supporto alla Localizzazione:**

La tassonomia supporta ambienti multilingue attraverso il pattern del suffisso ``_l10n_id``, abilitando una gestione efficiente della localizzazione per interfacce utente e implementazioni transfrontaliere.

**Utilizzo della Tassonomia:**

- **Registro degli Attributi**: Catalogo degli attributi individuali
- **Registro AS**: Le Fonti Autentiche dichiarano capacità di fornitura dati utilizzando classificazioni della tassonomia
- **Catalogo degli Attestati Elettronici**: I tipi di credenziali specificano domini e scopi supportati
- **Policy di Autorizzazione**: La valutazione delle policy sfrutta la struttura della tassonomia per decisioni di controllo degli accessi

La tassonomia è accessibile attraverso l'endpoint dedicato della tassonomia come definito nel meccanismo di discovery del registro ed è mantenuta dall'Organismo di Supervisione per garantire conformità normativa e coerenza semantica.

Un esempio non normativo della struttura della Tassonomia è fornito di seguito:

.. literalinclude:: ../../examples/taxonomy-example.json
  :language: JSON

Integrazione del Registro e Riferimenti Incrociati
---------------------------------------------------

I componenti del registro sono interconnessi e lavorano insieme per supportare l'ecosistema completo delle credenziali:

1. **Registro AS** ↔ **Tassonomia**: Le entità AS dichiarano capacità di fornitura utilizzando classificazioni della tassonomia per la categorizzazione standardizzata.
2. **Registro AS** ↔ **Catalogo**: I tipi di credenziali fanno riferimento alle capacità AS per la validazione della fonte dati.
3. **Catalogo** ↔ **Tassonomia**: Le voci delle credenziali specificano domini e scopi dalla tassonomia per discovery e autorizzazione.
4. **Registro della Federazione** ↔ **Tutti i Componenti**: Fornisce validazione del trust crittografico per tutte le operazioni del registro e autenticazione delle entità.

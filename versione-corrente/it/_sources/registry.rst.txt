.. include:: ../common/common_definitions.rst


Infrastruttura del Registro
============================

L'ecosistema IT-Wallet opera attraverso un'infrastruttura di registro che fornisce definizioni dati standardizzate, registrazione delle entità e capacità di scoperta delle Credenziali. Il sistema di registro consiste di molteplici componenti interconnessi che supportano il ciclo di vita completo delle operazioni degli Attestati Elettronici dall'onboarding delle entità alla presentazione delle Credenziali.

L'architettura di registro affronta la standardizzazione semantica, la gestione della fiducia federata e i requisiti di scoperta delle Credenziali attraverso componenti di registro specializzati che assicurano interoperabilità e conformità attraverso l'ecosistema.

Panoramica dell'Architettura del Registro
------------------------------------------

Il Registro del Sistema IT-Wallet comprende sei componenti principali:

1. **Registro dei Claims**: Definizioni semantiche standardizzate per attributi individuali delle Credenziali, tipi di dati e regole di validazione.
2. **Registro delle Fonti Autentiche (AS)**: Catalogo dei fornitori di dati registrati con le loro capacità dichiarate e claims disponibili.
3. **Registro di Federazione**: Elenco autorevole delle entità fidate che partecipano alla federazione con le loro configurazioni tecniche.
4. **Catalogo degli Attestati Elettronici**: Meccanismo di scoperta pubblico per i tipi di Credenziali disponibili con i loro metadati e informazioni di emissione.
5. **Registro degli Schema**: Elenco autorevole degli schemi di Credenziali.
6. **Tassonomia**: Sistema di classificazione gerarchico che organizza le Credenziali per dominio e scopo.

Questi componenti di registro sono interconnessi e mantenuti dall'Organismo di Supervisione per garantire coerenza, sicurezza e conformità normativa attraverso l'ecosistema.

Endpoint di Scoperta del Registro
----------------------------------

Il Trust Anchor DEVE fornire un meccanismo di scoperta per tutti i componenti di registro attraverso endpoint *well-known* standardizzati che forniscono metadati e informazioni di scoperta API REST per gestire operazioni complesse come paginazione e filtraggio.

Il Trust Anchor DEVE pubblicare metadati di scoperta del registro all'endpoint ``.well-known/it-wallet-registry`` con supporto per la negoziazione del contenuto:

- **Content-Type Predefinito**: ``application/jwt`` (JWT firmato che garantisce autenticità e integrità)
- **Content-Type Alternativo**: ``application/json`` (JSON semplice per scopi di sviluppo/debug)

Inoltre, il Registro del Sistema IT-Wallet DEVE usare due pattern di accesso distinti:

- **API di Registro Dati**: DEVONO supportare capacità di paginazione e filtraggio.
- **Infrastruttura di Fiducia della Federazione**: come definito in :ref:`trust-infrastructure:L'Infrastruttura di Trust`.

Di seguito è fornito un esempio non normativo.

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
      "schema_registry": "https://trust-anchor.eid-wallet.example.it/api/v1/schemas",
      "federation_list": "https://trust-anchor.eid-wallet.example.it/list",
      "federation_fetch": "https://trust-anchor.eid-wallet.example.it/fetch",
      "federation_resolve": "https://trust-anchor.eid-wallet.example.it/resolve",
      "federation_trust_mark_status": "https://trust-anchor.eid-wallet.example.it/trust_mark_status",
      "federation_historical_keys": "https://trust-anchor.eid-wallet.example.it/historical-jwks"
    },
    "content_negotiation": ["application/json", "application/jwt"]
  }



Registro dei Claims
-------------------

Il **Registro dei Claims** fornisce definizioni semantiche standardizzate per attributi individuali delle Credenziali, tipi di dati e regole di validazione. Questo registro serve come fondamento semantico per la standardizzazione degli attributi delle Credenziali attraverso l'ecosistema IT-Wallet, lavorando in coordinamento con il componente Tassonomia per la classificazione gerarchica.

L'Organismo di Supervisione DEVE mantenere il Registro dei Claims per garantire coerenza semantica e conformità normativa attraverso l'ecosistema. Il registro DEVE contenere:

  - **Claims Standardizzati**: Definizioni semantiche per tutti gli attributi delle Credenziali con tipi di dati e regole di validazione.
  - **Mappature di Interoperabilità**: Definizioni di alias per claims che usano terminologia diversa tra standard (es. ISO18013-5 ``place_of_birth`` mappato al canonico ``birth_place``).
  - **Formati Dati**: Tipi di dati standardizzati (string, date, numeric, boolean, email, url, image, array, object) con pattern di validazione.

Il Registro dei Claims DEVE garantire:

  - **Coerenza Semantica**: Previene conflitti tra claims duplicati o sovrapposti attraverso l'ecosistema.
  - **Interoperabilità Transfrontaliera**: Garantisce conformità UE e interpretazione coerente dei claims.
  - **Validazione degli Schema**: Fornisce definizioni autorevoli per la validazione dei claims attraverso tutti gli scenari delle Credenziali.
  - **Allineamento Normativo**: Si coordina con il quadro normativo nazionale ed europeo.
  - **Scenari Credential-Agnostic**: Supporta scenari dove **convenienza dell'utente** ed **efficienza operativa aziendale** sono prioritari rispetto a **conformità normativa** e **tracce di audit**.

.. note::
   Il Registro dei Claims definisce le proprietà semantiche degli attributi individuali, ma NON DEVE specificare capacità di divulgazione selettiva. La divulgazione selettiva dipende dalle implementazioni del formato delle Credenziali (SD-JWT VC, mDoc), dalle configurazioni tecniche dell'emittente e dal contesto di presentazione. Queste capacità sono specificate a livello di tipo di Credenziale all'interno del Catalogo degli Attestati Elettronici e implementate durante i flussi di presentazione delle Credenziali.


Utilizzo del Registro dei Claims
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Il Registro dei Claims DEVE supportare il ciclo di vita completo dell'ecosistema:

**Durante il Processo di Onboarding**:

  - **Registrazione AS**: Le Fonti Autentiche dichiarano i claims disponibili dal registro standardizzato durante la registrazione delle capacità.
  - **Registrazione CI**: Gli Emittenti di Credenziali selezionano le entità AS in base ai claims richiesti e registrano i tipi di Credenziali per la pubblicazione nel catalogo.
  - **Registrazione RP**: Le Relying Parties specificano i requisiti di autorizzazione usando domini/scopi per tipi di Credenziali specifici e/o attributi dell'Utente.

**Durante le Attività Operative**:

  - **Emissione di Credenziali**: Le definizioni dei claims garantiscono una rappresentazione dati coerente attraverso diversi tipi di Credenziali.
  - **Richieste di Presentazione**: Le RP fanno riferimento ai claims per la validazione dello schema e la verifica dell'autorizzazione in scenari sia credential-specific che credential-agnostic.
  - **Applicazione delle Policy**: Le policy di autorizzazione sfruttano le classificazioni dominio/scopo per il controllo degli accessi.


Struttura del Registro dei Claims
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Il Registro dei Claims mantiene definizioni tecniche, indipendenti dalla lingua, per la coerenza semantica attraverso l'ecosistema. Le localizzazioni rivolte all'utente per nomi e descrizioni dei claims sono fornite attraverso i bundle di localizzazione del Catalogo degli Attestati Elettronici, abilitando un supporto multilingue efficiente senza compromettere l'integrità strutturale del registro.

Un esempio non normativo della struttura del Registro dei Claims è fornito di seguito:

.. literalinclude:: ../../examples/claims-registry-example.json
  :language: JSON

Registro delle Fonti Autentiche
--------------------------------

L'Organismo di Supervisione DEVE mantenere il Registro delle Fonti Autentiche per abilitare l'accesso coordinato ai dati e l'emissione di Credenziali attraverso l'ecosistema. Il Registro AS DEVE contenere almeno:

  - **Informazioni sull'Organizzazione**: Dettagli dell'entità legale, stato normativo e ruolo autorevole all'interno di domini specifici.
  - **Capacità dei Dati**: Disponibilità dichiarata dei claims che fanno riferimento a definizioni standardizzate dal Registro dei Claims con le corrispondenti classificazioni della Tassonomia.
  - **Metodi di Integrazione**: Meccanismi di accesso tecnico (PDND per AS pubblici, API personalizzate per AS privati).
  - **Scopi Previsti**: Tipi di Credenziali supportati e contesti aziendali per il coordinamento AS-CI.
  - **Garanzia della Qualità dei Dati**: Stato autorevole, frequenza di aggiornamento e capacità di traccia di audit.

Il Registro AS DEVE garantire:

  - **Accesso Coordinato ai Dati**: Abilita la scoperta da parte dei CI di dati appropriati dalle Fonti Autentiche per l'emissione di Credenziali.
  - **Integrazione AS-CI**: Facilita flussi di lavoro di approvazione e coordinamento dell'accesso ai dati tra entità.
  - **Garanzia della Qualità**: Mantiene lo stato autorevole e l'affidabilità dei dati attraverso diversi domini.
  - **Conformità Normativa**: Supporta i requisiti di trasparenza della pubblica amministrazione e coordinamento del settore privato.

.. note::
   Il Registro delle Fonti Autentiche è un registro tecnico e non pubblico che fornisce linee guida per l'Emittente di Credenziali per il provisioning delle Credenziali.

Utilizzo del Registro delle Fonti Autentiche
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Il Registro AS supporta il coordinamento dell'ecosistema durante tutto il ciclo di vita operativo:

**Durante il Processo di Onboarding**:
  - **Auto-Dichiarazione AS**: Le Fonti Autentiche registrano le capacità prima che esistano tipi di Credenziali nel catalogo.
  - **Scoperta CI**: Gli Emittenti di Credenziali cercano entità AS in base ai claims richiesti e ai tipi di Credenziali previsti.
  - **Coordinamento delle Approvazioni**: Le entità AS valutano e approvano le richieste di accesso dei CI per la fornitura di dati.

**Durante le Attività Operative**:
  - **Risoluzione della Fonte Dati**: I sistemi CI fanno riferimento al Registro AS per l'accesso ai dati in tempo reale durante l'emissione delle Credenziali.
  - **Validazione della Qualità**: Le informazioni del Registro AS supportano la verifica dell'origine dei dati e i requisiti di audit.
  - **Gestione dell'Integrazione**: Gli endpoint tecnici e i metodi di accesso abilitano la comunicazione standardizzata AS-CI.

Coordinamento AS Pubblici vs Privati
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

L'architettura del Registro AS supporta diversi pattern di coordinamento che riflettono requisiti operativi distinti:

  1. **AS della Pubblica Amministrazione** (Integrazione Standardizzata): Le entità governative forniscono dati autorevoli attraverso meccanismi regolamentati:

    - **Integrazione PDND**: ``"integration_method": "pdnd_eservice"`` per l'accesso standardizzato ai dati governativi.
    - **Conformità Normativa**: Requisiti di trasparenza completi con pubblicazione nel catalogo pubblico.
    - **Requisiti di Audit**: Tracciabilità completa per i processi di emissione di Credenziali governative.

  2. **AS del Settore Privato** (Integrazione Flessibile): Le entità private forniscono dati specializzati attraverso accordi personalizzati:

    - **API Personalizzate**: ``"integration_method": "custom_api"`` per pattern di accesso ai dati specifici dell'azienda.
    - **Divulgazione Selettiva**: Visibilità pubblica limitata con flussi di lavoro di approvazione specifici per CI.
    - **Flessibilità Aziendale**: Integrazione su misura che supporta diversi casi d'uso del settore privato.

Questo approccio abilita sia la **trasparenza normativa** per la pubblica amministrazione che la **flessibilità aziendale** per le entità del settore privato mantenendo l'accesso coordinato ai dati attraverso l'ecosistema.

Struttura del Registro AS
^^^^^^^^^^^^^^^^^^^^^^^^^^

Durante la registrazione, le Fonti Autentiche dichiarano le loro capacità prima che esistano tipi di Credenziali nel catalogo. Questa dichiarazione stabilisce le fondamenta per la successiva registrazione CI e creazione dei tipi di Credenziali.

Schema dell'Identificatore Univoco AS
""""""""""""""""""""""""""""""""""""""

A ciascuna Fonte Autentica DEVE essere assegnato un identificatore univoco che segue lo schema URL HTTPS definito di seguito. Questo identificatore è usato per fare riferimento alle entità AS attraverso il sistema di registro e nel Catalogo degli Attestati Elettronici, garantendo coerenza con i pattern di identificazione delle entità OpenID Federation.

**Schema dell'Identificatore AS:**

.. code-block:: text

  https://{organization_domain}[/{optional_path}]

**Componenti dello Schema:**

  - **organization_domain**: Dominio DNS controllato dall'organizzazione
  - **optional_path**: Componente di percorso aggiuntivo per servizi o dipartimenti specifici


L'identificatore AS DEVE seguire queste regole normative:

1. **Protocollo HTTPS**: DEVE usare lo schema HTTPS per la sicurezza e la verifica della fiducia
2. **Proprietà del Dominio**: L'organizzazione DEVE controllare il dominio DNS usato nell'identificatore
3. **Univocità**: Garantita attraverso l'univocità del namespace DNS
4. **Stabilità**: DOVREBBE rimanere stabile nel tempo per evitare la rottura dei riferimenti
5. **Risolvibilità**: L'URL DOVREBBE essere risolvibile (anche se non è richiesto servire contenuto)

**Esempi di identificatori AS conformi:**

  - ``https://motorizzazione.gov.example``: Pubblico - Ministero dei Trasporti, Dip. Motorizzazione
  - ``https://registry.anpr.example``: Pubblico - Anagrafe Nazionale della Popolazione Residente
  - ``https://api.bank.example/auth-source``: Privato - Servizi Finanziari Banca di Esempio


Parametri del Registro delle Fonti Autentiche
""""""""""""""""""""""""""""""""""""""""""""""

Il Registro delle Fonti Autentiche DEVE contenere i seguenti parametri per ciascuna Fonte Autentica registrata:


.. list-table:: Campi di Primo Livello del Registro delle Fonti Autentiche
   :class: longtable
   :widths: 30 70
   :header-rows: 1

   * - **Nome del Campo**
     - **Descrizione**
   * - **version**
     - RICHIESTO. La versione del Registro delle Fonti Autentiche (es., ``1.0``).
   * - **last_modified**
     - RICHIESTO. Il timestamp che indica quando l'elenco è stato aggiornato l'ultima volta (es., ``2025-03-15T12:00:00Z``).
   * - **authentic_sources**
     - RICHIESTO. Un Array JSON dove ogni elemento è un Oggetto JSON che rappresenta un'entità Fonte Autentica. Ogni oggetto contiene i parametri definiti nella tabella "Parametri delle Fonti Autentiche" sottostante, inclusi identificazione dell'entità, informazioni organizzative, capacità dei dati e metodi di integrazione.


.. list-table:: Parametri delle Fonti Autentiche
   :class: longtable
   :widths: 25 15 60
   :header-rows: 1

   * - **Parametro**
     - **Tipo**
     - **Descrizione**
   * - **entity_id**
     - string
     - RICHIESTO. Identificatore univoco che segue lo schema normativo: ``https://{organization_domain}[/{optional_path}]``.
   * - **organization_info**
     - JSON object
     - RICHIESTO. Dettagli dell'entità legale e metadati organizzativi.
   * - **organization_info.organization_name**
     - string
     - RICHIESTO. Nome legale dell'organizzazione.
   * - **organization_info.organization_type**
     - string
     - RICHIESTO. Classificazione dell'entità: ``"public"`` o ``"private"``.
   * - **organization_info.ipa_code**
     - string
     - RICHIESTO solo per AS Pubblici. Codice di registrazione IPA per entità governative.
   * - **organization_info.legal_identifier**
     - string
     - RICHIESTO. Identificatore di registrazione legale (Codice Fiscale/Partita IVA, o identificatore nazionale equivalente per entità straniere).
   * - **organization_info.homepage_uri**
     - string
     - RICHIESTO. URL che punta alla homepage dell'organizzazione.
   * - **organization_info.contacts**
     - String Array
     - RICHIESTO. Array di indirizzi email di contatto tecnici/amministrativi.
   * - **organization_info.policy_uri**
     - string
     - RICHIESTO. URL al documento della politica sulla privacy.
   * - **organization_info.tos_uri**
     - string
     - RICHIESTO solo per AS Privati. URL al documento dei termini di servizio.
   * - **organization_info.organization_country**
     - string
     - RICHIESTO. Codice paese a due lettere ISO 3166-1 alpha-2 dell'organizzazione.
   * - **organization_info.logo_uri**
     - string
     - OPZIONALE. URL all'immagine del logo dell'organizzazione.
   * - **organization_info.logo_uri#integrity**
     - string
     - CONDIZIONALE. Digest crittografico della risorsa immagine del logo per la verifica dell'integrità. RICHIESTO se ``logo_uri`` è presente. Formato: ``{digest_method}-{digest_value}`` (es., ``"sha-256-abc123..."``).
   * - **organization_info.logo_uri_extended**
     - string
     - RICHIESTO. URL all'immagine del logo esteso dell'organizzazione.
   * - **organization_info.logo_uri_extended#integrity**
     - string
     - CONDIZIONALE. Digest crittografico della risorsa immagine del logo esteso per la verifica dell'integrità. RICHIESTO se ``logo_uri_extended`` è presente. Formato: ``{digest_method}-{digest_value}`` (es., ``"sha-256-abc123..."``).
   * - **data_capabilities**
     - JSON Objects Array
     - RICHIESTO. Array contenente specifiche delle capacità dei dati.
   * - **data_capabilities[].dataset_id**
     - string
     - RICHIESTO. L'identificatore univoco del dataset nell'ambito della Fonte Autentica, che PUÒ essere usato come parametro di query per il servizio ``GetAttributeClaims``.
   * - **data_capabilities[].data_origin**
     - string
     - OPZIONALE. Nome leggibile dall'uomo dell'origine dati specifica o del dipartimento che fornisce i dati.
   * - **data_capabilities[].domains**
     - String Array
     - RICHIESTO. Dominio della tassonomia (es., ``["AUTHORIZATION"]``, ``["FINANCIAL"]``).
   * - **data_capabilities[].intended_purposes**
     - String Array
     - RICHIESTO. Scopi aziendali serviti (es., ``["driving-authorization", "identity-verification"]``).
   * - **data_capabilities[].available_claims**
     - String Array
     - RICHIESTO. Claims disponibili da questa capacità di dati.
   * - **data_capabilities[].available_claims.claim_name**
     - string
     - RICHIESTO. Contiene il nome del claim.
   * - **data_capabilities[].available_claims.order**
     - number
     - RICHIESTO. Definisce l'ordine in cui l'informazione verrebbe mostrata.
   * - **data_capabilities[].available_claims.mandatory**
     - boolean
     - RICHIESTO. Definisce se un claim è sempre disponibile o no.
   * - **data_capabilities[].integration_method**
     - string
     - RICHIESTO. Framework di autorizzazione usato per l'accesso ai dati. DEVE essere ``"pdnd"`` per AS Pubblici. Gli AS Privati POSSONO usare altri framework di autorizzazione come: ``"oauth2"``, ``"api_key"``, ``"mtls"``, ecc.
   * - **data_capabilities[].integration_endpoint**
     - string
     - RICHIESTO. Punto di accesso al servizio (endpoint PDND per AS Pubblici, endpoint API per AS Privati).
   * - **data_capabilities[].api_specification**
     - string
     - RICHIESTO. URL al documento di specifica `OAS3`_ per questa capacità di dati.
   * - **data_capabilities[].data_provision**
     - JSON object
     - OPZIONALE. Capacità di fornitura dati e specifiche dei tempi.
   * - **data_capabilities[].data_provision.immediate_flow**
     - boolean
     - RICHIESTO. Indica se la Fonte Autentica supporta la fornitura immediata di dati.
   * - **data_capabilities[].data_provision.deferred_flow**
     - boolean
     - RICHIESTO. Indica se la Fonte Autentica supporta la fornitura differita di dati.
   * - **data_capabilities[].data_provision.max_response_time_minutes**
     - integer
     - CONDIZIONALE. Tempo massimo in minuti per la Fonte Autentica per rispondere a una richiesta di fornitura dati differita. RICHIESTO se ``deferred_flow`` è ``true``.
   * - **data_capabilities[].data_provision.notification_methods**
     - String Array
     - CONDIZIONALE. Array di metodi di notifica supportati dalla Fonte Autentica per la fornitura dati differita, come ``"push"``, ``"poll"``. RICHIESTO se ``deferred_flow`` è ``true``.
   * - **data_capabilities[].user_information**
     - string
     - OPZIONALE. Una stringa contenente informazioni leggibili dall'uomo sulla Credenziale Digitale rilevanti per l'Utente. Questa stringa DEVE essere fornita dalla Fonte Autentica al Trust Anchor durante l'onboarding e DEVE essere formattata usando il formato Markdown come definito in :rfc:`7763`. La formattazione Markdown può essere testo semplice o una combinazione di testo e link. Ad esempio, se il database della Fonte Autentica contiene solo i dati richiesti per gli attributi della Credenziale Digitale registrati *dopo* una data specifica, questa informazione DEVE essere trasmessa al Trust Anchor in questa stringa Markdown.
   * - **data_capabilities[].service_documentation**
     - string
     - OPZIONALE. URL che punta alla documentazione del servizio della Fonte Autentica.
   * - **data_capabilities[].update_frequency**
     - string
     - OPZIONALE. Indica con quale frequenza la Fonte Autentica aggiorna i suoi dati. Valori possibili: ``"real_time"`` (aggiornamenti quasi in tempo reale, tipicamente entro minuti), ``"daily"``, ``"weekly"``, ``"monthly"``, ``"on_demand"``.
   * - **data_capabilities[].logo_uri**
     - string
     - OPZIONALE. URL all'immagine del logo relativa ai dati forniti.
   * - **data_capabilities[].logo_uri#integrity**
     - string
     - CONDIZIONALE. Digest crittografico della risorsa immagine del logo per la verifica dell'integrità. RICHIESTO se ``logo_uri`` è presente. Formato: ``{digest_method}-{digest_value}`` (es., ``"sha-256-abc123..."``).
   * - **data_capabilities[].background_image**
     - JSON object
     - OPZIONALE. Oggetto contiene informazioni sull’immagine di sfondo da visualizzare insieme ai dati forniti. L’oggetto include i parametri ``uri`` e ``uri#integrity``.
   * - **data_capabilities[].watermark_image**
     - JSON object
     - OPZIONALE. Oggetto contiene informazioni sull’immagine di filigrana da visualizzare insieme ai dati forniti. L’oggetto include i parametri ``uri`` e ``uri#integrity``.
   * - **data_capabilities[].background_color**
     - string
     - OPZIONALE. Stringa che rappresenta il colore di sfondo da visualizzare insieme ai dati forniti
   * - **data_capabilities[].contacts**
     - String Array
     - OPZIONALE. Indirizzi email di contatto del servizio clienti.

Esempio del Registro AS
""""""""""""""""""""""""

Un esempio non normativo della struttura del Registro AS è fornito di seguito:

.. literalinclude:: ../../examples/as-registry-example.json
  :language: JSON

.. note::
  Per una gestione migliore e più efficiente della localizzazione delle informazioni contenute nel Catalogo degli Attestati Elettronici, un'Entità che lo consulta DOVREBBE:

    - Scaricare la versione base del Catalogo degli Attestati Elettronici (compatta, senza localizzazioni) usando l'endpoint ``.well-known/authentic-sources``.
    - Determinare la lingua preferita dell'Utente.
    - Scaricare solo i bundle di localizzazione necessari.
    - Unire dinamicamente il contenuto localizzato con la struttura del Catalogo degli Attestati Elettronici.

Un esempio non normativo di output di un bundle di localizzazione è fornito di seguito:

.. code-block:: json

 {
    "authentic_source1.name": "Ministry of Infrastructure and Transport",
    "authentic_source1.dataset1.origin": "MIT -- General Directorate for Motorization",
    "authentic_source1.dataset1.userinfo": "###### Driving License\nVehicle registration data is available for licenses issued after January 1, 2020. For older licenses, contact the local motorization office.",
    "authentic_source2.name": "Example Bank S.p.A.",
    "authentic_source2.dataset1.origin": "Example data origin 1",
    "authentic_source2.dataset1.userinfo": "###### Information on data availability\nFinancial data access requires customer consent and is subject to PSD2 regulations. Account information is available for active accounts only.",
    "...": "..."
  }

I bundle di localizzazione DEVONO essere disponibili all'URI specificato nell'attibuto **localization_info.bundles_base_uri** del Catalogo degli Attestati Elettronici. Ogni bundle locale DEVE essere accessibile seguendo il pattern di denominazione **{locale_code}.json**, dove **{locale_code}** è sostituito con il codice locale corrispondente dall'array **available_locales**.

Un esempio non normativo dell'URI di localizzazione italiana per il bundle sarebbe **https://trust-registry.eid-wallet.example.it/.well-known/authentic-sources/it.json**. 

Le Entità DOVREBBERO verificare l'integrità dei bundle di localizzazione scaricati utilizzando il metodo di digest e i valori specificati nel claim **localization_info.integrity**. Questo garantisce che i dati di localizzazione non siano stati manomessi durante la trasmissione.

Coordinamento AS-CI
^^^^^^^^^^^^^^^^^^^

Dopo la registrazione AS, il Registro AS abilita gli Emittenti di Credenziali a scoprire entità AS adatte e richiedere l'approvazione dell'integrazione. Questo processo di coordinamento è dettagliato in :ref:`entity-onboarding:Processo di Integrazione AS-CI`.

Registro di Federazione
-----------------------

Il **Registro di Federazione** fornisce l'infrastruttura di fiducia crittografica per tutti i partecipanti dell'ecosistema IT-Wallet. Il Registro di Federazione mantiene l'elenco autorevole delle entità fidate e il loro stato operativo usando endpoint specifici della federazione come definito in :ref:`trust-infrastructure:Endpoint API di Federazione`.

Ruolo di Integrazione del Registro
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

All'interno dell'architettura del Registro del Sistema IT-Wallet, il Registro di Federazione serve come **livello di validazione della fiducia** per:

1. **Autenticazione delle Entità**: Valida l'identità crittografica di tutti i partecipanti prima delle operazioni di registro
2. **Verifica della Catena di Fiducia**: Fornisce la fondazione crittografica per la validazione delle entità Emittenti di Credenziali, Relying Parties e Fornitori di Wallet
3. **Verifica della Conformità**: Mantiene Trust Marks che attestano la conformità normativa e lo stato operativo

Accesso al Registro di Federazione
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Le operazioni del Registro di Federazione sono accessibili attraverso gli endpoint di federazione del Trust Anchor come dettagliato in :ref:`trust-infrastructure:Endpoint API di Federazione`. L'architettura di scoperta del registro fornisce informazioni sugli endpoint di federazione tramite l'endpoint di scoperta del registro descritto in `Endpoint di Scoperta del Registro`_.

.. note::
   Gli endpoint di federazione sono disponibili sia attraverso il meccanismo di scoperta del registro (per l'accesso unificato al registro) che attraverso l'Entity Configuration del Trust Anchor a ``.well-known/openid-federation`` (per operazioni specifiche della federazione). Entrambe le fonti forniscono gli stessi URL degli endpoint ma servono diversi pattern di scoperta: scoperta del registro per l'orientamento iniziale nell'ecosistema, Entity Configuration per la conformità standard OpenID Federation 1.0.
   
   Per le specifiche tecniche complete dei protocolli di federazione, configurazioni delle entità, meccanismi di valutazione della fiducia e validazione della catena di fiducia, vedere :ref:`trust-infrastructure:L'Infrastruttura di Trust`.

Catalogo degli Attestati Elettronici
------------------------------------

Il Catalogo degli Attestati Elettronici è il registro di tutte gli Attestati Elettronici disponibili riconosciute all'interno dell'ecosistema IT-Wallet. È pubblicato dal Trust Anchor e pubblicamente disponibile da tutte le Entità attraverso un endpoint di Federazione specializzato. Agisce come un punto di riferimento unico per tutti gli attori coinvolti nel processo di emissione, verifica e utilizzo degli Attestati Elettronici.

Il Catalogo degli Attestati ElettroniciCatalogo degli Attestati Elettronici mira a:

  1. Facilitare la scoperta degli Attestati Elettronici per gli Utenti.
  2. Standardizzare la descrizione tecnica e funzionale degli Attestati Elettronici.
  3. Abilitare l'interoperabilità tra diversi Emittenti e Relying Parties.
  4. Semplificare il processo di integrazione per Fornitori di Wallet e Relying Parties.
  5. Garantire la fiducia nell'ecosistema attraverso informazioni verificabili e affidabili.
  6. Fornire trasparenza sull'ecosistema degli Attestati Elettronici disponibili.


Le principali Entità coinvolte nel Catalogo degli Attestati Elettronici sono:

  - **Trust Anchor**: Gestisce e mantiene il Catalogo degli Attestati Elettronici, garantendone l'autenticità e l'integrità.
  - **Organismo di Supervisione**: Interagisce con il Trust Anchor e il Catalogo degli Attestati Elettronici per monitorare la fase di registrazione garantendo sicurezza e privacy secondo le normative nazionali/europee, mantenendo tutte le informazioni affidabili e aggiornate.
  - **Emittenti di Attestati Elettronici**: Le entità autorizzate a emettere Attestati Elettronici, registrandole nel Catalogo.
  - **Relying Parties**: Usano il Catalogo degli Attestati Elettronici per raccogliere tutte le informazioni necessarie sulgli Attestati Elettronici che intendono richiedere durante la fase di presentazione.
  - **Fornitori di Wallet**: Accedono al Catalogo degli Attestati Elettronici per identificare gli Attestati Elettronici disponibili e per recuperare tutte le informazioni necessarie per integrarle nelle loro Soluzioni Wallet.
  - **Utenti**: Gli Utenti che usano indirettamente il Catalogo degli Attestati Elettronici attraverso le loro Istanze Wallet per scoprire e richiedere Attestati Elettronici.
  - **Fonti Autentiche**: Le Entità che detengono i dati originali che sono attestati nelgli Attestati Elettronici. Forniscono supporto agli Emittenti nella registrazione degli Attestati Elettronici nel Catalogo.


.. _fig_catalog:
.. plantuml:: plantuml/credential-catalog-entities.puml
    :width: 99%
    :alt: La figura illustra le Entità degli Attestati Elettronici.
    :caption: `Diagramma Entità-Relazione del Catalogo degli Attestati Elettronici. <https://www.plantuml.com/plantuml/svg/ZLJ1Rkis4BpxAxP6WQP00X-QtjeWgPEsFXGmuXGz6ZIvbeb8fCfTEbM__YrDELAUb6ST34khuSnmESjxOXKuLYKysiAoAc4PqA1ZcnwL57mH4Pwam1Pfzfrrkem6uPVbxM9vkrtwglPEy7UpsG_mY7lh43RhvzNBqwO7vbWh4tvQQ5zLtjsDVDbxnpVg3SbNUFFpGcDWkxTQCKv06p6wKpG5MdhzEW4M2GDDyUcBAJ1XEsAO07p5PgAx2J1hjbe5Cm69_-c3SWLkLSbJ-etqohwUW7nJPOaNAHVM4LkER5CuPhFtL5tfSmIlOJvCA7KHdGlW6GjB79hql1H4471eQ-3t85v07PKjrQv46A6JXTzJ7IpZh_DpfkO_Yg4r1lBkAlLTkF-MlvE6PVi_EeAtWmTZINivP53EYEg_4OalQIG-uU-soo4IFpXzy4dd9Rr1VarwwVUNSgf0EgbKoZgM7m4Vy9i3t1ULY8dcfY76wefYBT6qv4FpcpUD26ow2gJIITGxopxGkPig7HJK1qK8w2W6wmeWrFB0pScQQ1sLRlgwlP7kz2rHn42Zfmkh_34vU8WiJP1k6y3sBf9DAuP4SF4isq7eP0EMZNXUgv2OKdHo0ThAF9_ogQ_l4GJsK2Wf1R1kxqELsw1sFZBeSUN-O7NoUIhMmH-joRl_vrI1jjJkMMia6dgmZh48Yh4lcgeUCl471xdKQIlfP5gZDpu64KX2vnAqjQJ-foyD-22DTTBOD0sWc54uZ6XTx7Wtq6c0fBqVijrjg8lqTPVd7A6uAoqTiflVHQMD7JfJUm4Ahz0E4_nnXbQEPQ5c6LBBX_4rVJkVXZtuT1gPe8jjVs6-VZ2CzGQiQvSE-tyc6pSxo6fVyezFuZXc8TCDizVnTP7pO4_BzatlmjG3hdmV3XZJw12qaLuvOkKqGfq11dPDNhvzR0dw3bREs82Qo-RzHgN-bKfVsRYNECIg_080>`_


La seguente tabella riassume le informazioni principali che DEVONO essere fornite dal Catalogo degli Attestati Elettronici:


.. list-table:: Catalogo degli Attestati Elettronici - Informazioni principali
   :class: longtable
   :widths: 30 70
   :header-rows: 1

   * - **Informazioni relative a**
     - **Descrizione**
   * - Metadati della Credenziale Digitale
     - Informazioni identificative essenziali e caratteristiche della Credenziale Digitale, inclusi:

       - **Identificatore univoco della Credenziale**: Una stringa identificativa univoca di ciascuna Credenziale Digitale.
       - **Metodi di autenticazione dell'utente**: Meccanismi di autenticazione dell'utente usati per richiedere la Credenziale Digitale, se richiesto dagli Emittenti o dalle Fonti Autentiche.
       - **Livello Minimo di Garanzia**: Il Livello Minimo di Garanzia richiesto per l'affidabilità della Credenziale Digitale. DEVE tenere conto del Livello di Garanzia dell'autenticazione dell'Utente, quando applicabile, e dell'Istanza Wallet.
   * - Emittenti di Attestati Elettronici
     - Dettagli sull'organizzazione autorizzata a emettere la Credenziale Digitale, come:

       - **Identificatori dell'emittente**: Identificatore univoco per l'emittente della Credenziale Digitale.
       - **Tipo di emittente**: Classificazione come Fornitore PID, (Q)EAA o Pub-EAA.
       - **Informazioni aggiuntive**: Dettagli organizzativi inclusi nome, codice e informazioni di contatto.
   * - Fonti Autentiche
     - Informazioni sulla fonte dati autorevole.
   * - Specifica Tecnica
     - Dettagli tecnici, inclusi:

       - **Schemi della Credenziale Digitale**: Specifiche del framework e della struttura.
       - **Formati della Credenziale Digitale**: Formato dati e standard di codifica.
       - **Policy di autenticazione**: Metodi e requisiti per la verifica.
   * - Termini d'Uso
     - Condizioni e limitazioni per l'uso della Credenziale Digitale, come:

       - **Validità della Credenziale**: Periodo di tempo durante il quale la Credenziale Digitale è valida e, quando applicabile, meccanismi e dettagli tecnici per invalidare gli Attestati Elettronici (metodi di revoca/sospensione).
       - **Policy di restrizione**: Se applicabile, regole che governano l'uso e le limitazioni della Credenziale Digitale secondo le normative nazionali. È usata, ad esempio, per specificare se solo Entità di tipo legale specifico, per esempio Fornitore Pub-EAA e Soluzioni Wallet pubbliche, sono autorizzate a emettere e ottenere la Credenziale Digitale.
       - **Policy di prezzo**: Informazioni relative ai modelli di prezzo della Credenziale Digitale, come `free`, `issuance_based`, `verification_based`.
       - **Scopi della Credenziale Digitale**: Informazioni relative agli scopi consentiti per cui la Credenziale Digitale può essere usata. Ogni tipo di Credenziale Digitale può essere usato per molteplici scopi.


Il Trust Anchor DEVE pubblicare e mantenere aggiornate tutte le informazioni all'endpoint `.well-known` del Catalogo degli Attestati Elettronici garantendo affidabilità, autenticità e integrità dei dati. In particolare, il Catalogo degli Attestati Elettronici, i claims e la tassonomia DEVONO essere disponibili attraverso l'endpoint ``.well-known/credential-catalog``.

Gerarchia degli Attestati Elettronici
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

gli Attestati Elettronici riconosciute all'interno dell'ecosistema IT-Wallet sono classificate e standardizzate gerarchicamente secondo i seguenti domini e scopi principali. Scopi aggiuntivi POSSONO essere aggiunti man mano che l'ecosistema IT-Wallet cresce.


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
     - Credenziali che concedono permessi, diritti o autorizzazioni specifici per eseguire determinate attività o accedere ad aree riservate.
   * - *EDUCATION*
     - * ACADEMIC_DEGREE
       * CERTIFICATE
       * TRAINING_RECOGNITION
     - Credenziali relative a risultati educativi, qualifiche e riconoscimento di formazione professionale.
   * - *HEALTH*
     - * INSURANCE_CARD
       * DISABILITY_CARD
       * MEDICAL_PRESCRIPTION
     - Credenziali relative all'accesso sanitario, storia medica, copertura assicurativa e documenti sanitari.
   * - *FINANCIAL*
     - * INCOME_CERTIFICATE
       * TAX_STATEMENT
       * FAMILY_ECONOMIC_STATUS
       * BANK_ACCOUNT
       * PAYMENT_HISTORY
     - Credenziali che attestano stato finanziario, livelli di reddito, tassazione, informazioni bancarie o situazione economica di individui o famiglie.
   * - *MEMBERSHIP*
     - * ASSOCIATION
       * LOYALTY_PROGRAM
       * CLUB_MEMBERSHIP
     - Credenziali che confermano affiliazione con organizzazioni, partecipazione a programmi o stato di membership.
   * - *ATTESTATION*
     - * PUBLIC_STATEMENT
       * CIVIL_STATUS
       * CERTIFICATION
     - Credenziali che forniscono dichiarazioni ufficiali, conferme di stato o certificazioni rilasciate da autorità.

Ogni Credenziale DEVE specificare domini e scopi per abilitare sia **Scenari Credential-Specific** che **Scenari Credential-Agnostic** secondo i requisiti della Relying Party e i pattern di richiesta di presentazione:

  1. **Scenari Credential-Specific** (Primari per Settori Governativi/Regolamentati): Le RP richiedono tipi di Credenziali specifici per requisiti di conformità e audit, includendo ad esempio:

    - **Servizi Governativi**: ``"vct_values": ["urn:eudi:pid:it:1"]`` per la verifica dell'identità specifica del PID.
    - **Controlli di Polizia**: ``"docType": "org.iso.18013.5.1.mDL"`` per la verifica della patente di guida.
    - **KYC Bancario**: Tipi di Credenziali specifici richiesti dalle normative finanziarie.
    - **Servizi Sanitari**: ``"vct_values": ["urn:eudi:european_disability_card:it:1"]`` per l'accesso ai benefici per disabilità conforme all'UE.

  2. **Scenari Credential-Agnostic** (Tipici per Business Privato): Le RP richiedono claims specifici indipendentemente dalla fonte della Credenziale per efficienza operativa, come:

    - **Consegna E-commerce**: Qualsiasi Credenziale, tra quelle a cui è autorizzato ad accedere, contenente ``given_name``, ``family_name``, ``address`` per la spedizione.
    - **Abbonamenti**: Qualsiasi Credenziale, tra quelle a cui è autorizzato ad accedere, con ``given_name``, ``email`` per la personalizzazione.
    - **Personalizzazione del Servizio**: Applicazioni aziendali che richiedono dati personali di base senza forti requisiti sulla fonte.

Questo approccio consente:

  - **Autorizzazione basata su policy** usando mappature dominio/scopo.
  - **Registrazione RP flessibile** supportando sia le esigenze di conformità governativa che i requisiti operativi aziendali.

Struttura del Catalogo degli Attestati Elettronici
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
     - RICHIESTO. DEVE essere impostato a ``JOSE``.
     - [:rfc:`7515` Sezione 4.1.9].
   * - **alg**
     - RICHIESTO. Un identificatore di algoritmo di firma digitale come da registro IANA "JSON Web Signature and Encryption Algorithms". DEVE essere uno degli algoritmi supportati nella Sezione :ref:`algorithms:Algoritmi Crittografici` e NON DEVE essere impostato a ``none`` o con un identificatore di algoritmo simmetrico (MAC).
     - [:rfc:`7515` Sezione 4.1.1].
   * - **kid**
     - RICHIESTO. Identificatore univoco della chiave pubblica.
     - [:rfc:`7515` Sezione 4.1.4].
   * - **x5c**
     - OPZIONALE. Contiene il Certificato di chiave pubblica X.509 o la catena di Certificati [:rfc:`5280`] corrispondente alla chiave usata per firmare digitalmente il JWS. Quando il valore del parametro header `kid` è presente, DEVE fare riferimento alla stessa chiave pubblica crittografica del foglio usata con il Certificato X.509.
     - [:rfc:`7515` Sezione 4.1.6.].
   * - **cty**
     - RICHIESTO. DEVE essere impostato a ``application/json``.
     - [:rfc:`7515` Sezione 4.1.6.].

Il payload JWS contiene i seguenti parametri:


.. list-table:: Campi di Primo Livello del Catalogo degli Attestati Elettronici
   :class: longtable
   :header-rows: 1
   :widths: 30 70

   * - **Nome del Campo**
     - **Descrizione**
   * - **version**
     - RICHIESTO. Versione del formato del Catalogo degli Attestati Elettronici.
   * - **last_modified**
     - RICHIESTO. Timestamp dell'ultima modifica al Catalogo degli Attestati Elettronici.
   * - **iss**
     - RICHIESTO. Identificatore dell'emittente del Catalogo degli Attestati Elettronici.
   * - **credentials**
     - RICHIESTO. Array contenente definizioni di Credenziali Digitali.

Ogni elemento dell'array ``credentials`` contiene almeno le seguenti informazioni:


.. _table_catalog_parameters_first_level:
.. list-table:: Campi di Primo Livello di Ciascuna Voce di Credenziale
  :class: longtable
  :header-rows: 1
  :widths: 30 70

  * - **Nome del Campo**
    - **Descrizione**
  * - **version**
    - RICHIESTO. Versione della definizione della Credenziale Digitale.
  * - **credential_type**
    - RICHIESTO. Identificatore univoco del tipo di Credenziale Digitale. Per il PID DEVE essere ``pid``.
  * - **credential_name**
    - RICHIESTO. Nome leggibile dall'uomo della Credenziale Digitale.
  * - **legal_type**
    - RICHIESTO. Classificazione legale della Credenziale (es., ``pub-eaa``, ``qeaa``, ``eaa``).
  * - **restriction_policy**
    - OPZIONALE. Restrizioni legali sulle Soluzioni Wallet e/o Emittenti di Credenziali autorizzati a richiedere/emettere la Credenziale Digitale.

      * **allowed_wallet_ids**: Elenco di identificatori di Soluzioni Wallet consentite.
      * **allowed_issuer_ids**: Elenco di identificatori di Emittenti di Credenziali consentiti. Se presente, rappresenta una whitelist di Emittenti di Credenziali che possono essere aggiunti dal Trust Anchor nel campo **issuers** della corrispondente Credenziale Digitale.
  * - **pricing_policy**
    - OPZIONALE. Informazioni sul prezzo della Credenziale Digitale, inclusi:

      * **models**: RICHIESTO. Array di modelli di prezzo applicabili alla Credenziale Digitale, ciascuno contenente

        - **pricing_type**: Tipo di modello di prezzo, come ``issuance_based``, ``verification_based``, ``subscription_based``, ``other``.
        - **price**: Costo associato al modello.
        - **currency**: Valuta del prezzo.

      * **pricing_model_uri**: URI alla documentazione dettagliata del modello di prezzo.
  * - **validity_info**
    - Informazioni sulla validità della Credenziale Digitale, inclusi almeno:

      * **max_validity_days**: Periodo di validità massimo in giorni.
      * **status_methods**: Metodi di verifica dello stato supportati (es. ``status_list``).
      * **allowed_states**: Stati consentiti della Credenziale Digitale (es. ``VALID``, ``INVALID``, ``SUSPENDED``).
  * - **authentication**
    - RICHIESTO. Requisiti di autenticazione della Credenziale Digitale.

      * **user_auth_required**: RICHIESTO. Flag che indica se è richiesta l'autenticazione dell'Utente durante l'emissione della Credenziale Digitale.
      * **min_loa**: RICHIESTO. Livello Minimo di Garanzia richiesto per l'autenticazione della Credenziale Digitale. DEVE includere il Livello di Garanzia dell'autenticazione dell'Utente e dell'Istanza Wallet che richiede la Credenziale Digitale.
      * **supported_eid_schemes**: RICHIESTO se ``user_auth_required`` è ``true``. Schemi di autenticazione di identità digitale supportati.
  * - **purposes**
    - RICHIESTO. Array di scopi di utilizzo per cui la Credenziale Digitale può essere usata, definendo contesti di utilizzo specifici e claims richiesti per ciascuno scopo, come:

      * **id**: Identificatore univoco per lo scopo (es., "driving-authorization", "person-identification").
      * **description**: Descrizione dello scopo leggibile dall'uomo con un suffisso ``_l10n_id`` per la localizzazione del contenuto.
      * **claims_required**: Array di identificatori di claims che sono richiesti quando si usa la Credenziale per questo scopo.
      * **claims_recommended**: Array di identificatori di claims che sono raccomandati ma non obbligatori per questo scopo.
  * - **issuers**
    - RICHIESTO. Array di informazioni rilevanti sugli Emittenti di Credenziali autorizzati, inclusi dati amministrativi e tecnici come nome dell'Organizzazione, un riferimento al documento di specifica API e meccanismi di emissione supportati (ad esempio il supporto del flusso differito).
  * - **authentic_sources**
    - RICHIESTO. Array di oggetti JSON delle Fonti Autentiche che fanno riferimento alle Fonti Autentiche autorizzate. Ogni oggetto DEVE contenere l'identificatore dell'entità AS e l'identificatore specifico della capacità di dati:

      * **id**: Identificatore stringa che fa riferimento all'entity_id della Fonte Autentica come registrato nel :ref:`registry:Registro delle Fonti Autentiche`.
      * **dataset_id**: Identificatore stringa della capacità di dati/dataset specifico usato dall'Emittente dall'AS.

.. note::
  L'unione di ``credential_type`` e ``version`` DEVE essere univoca nel Catalogo delle Credenziali.

L'esempio corrispondente del Catalogo delle Credenziali Digitali decodificato in JSON sia per l'header che per il payload è il seguente:

.. literalinclude:: ../../examples/catalog-example-header.json
  :language: JSON

.. literalinclude:: ../../examples/catalog-example-payload.json
  :language: JSON

.. note::
  Per una gestione migliore e più efficiente della localizzazione delle informazioni contenute nel Catalogo degli Attestati Elettronici, un'Entità che lo consulta DOVREBBE:

    - Scaricare la versione base del Catalogo degli Attestati Elettronici (compatta, senza localizzazioni) usando l'endpoint ``.well-known/credential-catalog``.
    - Determinare la lingua preferita dell'Utente.
    - Scaricare solo i bundle di localizzazione necessari.
    - Unire dinamicamente il contenuto localizzato con la struttura del Catalogo degli Attestati Elettronici.

Un esempio non normativo di output di un bundle di localizzazione è fornito di seguito:

.. code-block:: json

  {
    "mDL.name": "Driving License",
    "mDL.issuer1.name": "Example of Credential Issuer",
    "...": "..."
  }

I bundle di localizzazione DEVONO essere disponibili all'URI specificato nell'attibuto **localization_info.bundles_base_uri** del Catalogo degli Attestati Elettronici. Ogni bundle locale DEVE essere accessibile seguendo il pattern di denominazione **{locale_code}.json**, dove **{locale_code}** è sostituito con il codice locale corrispondente dall'array **available_locales**.

Un esempio non normativo dell'URI di localizzazione italiana per il bundle sarebbe **https://trust-registry.eid-wallet.example.it/.well-known/credential-catalog/it.json**. 

Le Entità DOVREBBERO verificare l'integrità dei bundle di localizzazione scaricati utilizzando il metodo di digest e i valori specificati nel claim **localization_info.integrity**. Questo garantisce che i dati di localizzazione non siano stati manomessi durante la trasmissione.

Decentralizzazione delle Informazioni di Visualizzazione e dei Claims
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

La fonte canonica per le caratteristiche di visualizzazione e la struttura dei claims è determinata dai **Metadati dell'Emittente di Credenziali (Entity Configuration)**.

La logica complessiva per presentare una Credenziale è:

1. Il Wallet/Relying Party recupera il **Catalogo degli Attestati Elettronici** leggero per scoprire il `credential_type` disponibile e l'`entity_id` dei loro Emittenti di Credenziali.
2. Recupera i **Metadati dell'Emittente di Credenziali** completi (Entity Configuration) dall'`entity_id` scoperto.
3. I Metadati dell'Emittente di Credenziali DEVONO contenere le caratteristiche di visualizzazione complete (loghi, colori) e le informazioni dettagliate dello schema (tramite link ai Metadati di Tipo appropriati o direttamente nella configurazione). L'Emittente costruisce questi metadati in base ai suggerimenti forniti dalla Fonte Autentica (tramite il Registro AS) e le specifiche dello schema standard (tramite il Registro degli Schema).

Tassonomia
----------

La **Tassonomia** fornisce le fondamenta semantiche per l'interoperabilità degli Attestati Elettronici mantenendo il vocabolario autorevole per organizzare le Credenziali all'interno dell'ecosistema IT-Wallet. La tassonomia è neutrale rispetto al formato delle Credenziali e ha l'obiettivo di facilitare le integrazioni degli Attestati Elettronici nelle Soluzioni Tecniche IT-Wallet.

La tassonomia fornisce, in una singola risorsa, il sistema di classificazione gerarchica che organizza domini e scopi che possono essere applicati ai tipi di Credenziali, supportando la valutazione delle policy di autorizzazione e la standardizzazione a livello di ecosistema.

**Obiettivi della Tassonomia:**

1. **Fondamento Semantico**: Stabilire vocabolario standardizzato per domini e scopi in tutto l'ecosistema
2. **Framework delle Policy**: Abilitare decisioni di autorizzazione strutturate basate sulla classificazione gerarchica
3. **Interoperabilità**: Garantire interpretazione coerente delle classificazioni delle Credenziali
4. **Estensibilità**: Supportare l'evoluzione dell'ecosistema con nuovi domini e scopi
5. **Conformità Transfrontaliera**: Allinearsi con i requisiti normativi UE e gli standard internazionali

**Struttura della Tassonomia:**

La tassonomia mantiene una struttura gerarchica a due livelli:

- **Domini**: Classificazione di livello superiore che rappresenta aree funzionali ampie (ad esempio, IDENTITY, AUTHORIZATION, FINANCIAL)
- **Scopi**: Casi d'uso specifici delle Credenziali all'interno di ogni dominio (ad esempio, PERSON_IDENTIFICATION, DRIVING_LICENSE, BANK_ACCOUNT) per i quali le Credenziali possono essere utilizzate

**Supporto alla Localizzazione:**

La tassonomia supporta ambienti multilingue attraverso il pattern del suffisso ``_l10n_id``, abilitando una gestione efficiente della localizzazione per interfacce utente e implementazioni transfrontaliere.

**Utilizzo della Tassonomia:**

- **Registro degli Attributi**: Catalogo degli attributi individuali
- **Registro AS**: Le Fonti Autentiche dichiarano capacità di fornitura dati utilizzando classificazioni della tassonomia
- **Catalogo degli Attestati Elettronici**: I tipi di Credenziali specificano domini e scopi supportati
- **Policy di Autorizzazione**: La valutazione delle policy sfrutta la struttura della tassonomia per decisioni di controllo degli accessi

La tassonomia è accessibile attraverso l'endpoint dedicato della tassonomia come definito nel meccanismo di discovery del registro ed è mantenuta dall'Organismo di Supervisione per garantire conformità normativa e coerenza semantica.

Un esempio non normativo della struttura della Tassonomia è fornito di seguito:

.. literalinclude:: ../../examples/taxonomy-example.json
  :language: JSON

.. note::
  Per una gestione migliore e più efficiente della localizzazione delle informazioni contenute nel Catalogo degli Attestati Elettronici, un'Entità che lo consulta DOVREBBE:

    - Scaricare la versione base del Catalogo degli Attestati Elettronici (compatta, senza localizzazioni) usando l'endpoint ``.well-known/taxonomy``.
    - Determinare la lingua preferita dell'Utente.
    - Scaricare solo i bundle di localizzazione necessari.
    - Unire dinamicamente il contenuto localizzato con la struttura del Catalogo degli Attestati Elettronici.

Un esempio non normativo di output di un bundle di localizzazione è fornito di seguito:

.. code-block:: json

 {
    "domain.identity.name": "Identity",
    "domain.identity.description": "Credentials that establish or verify the identity of a person, including physical and digital identity documents legally recognized by national laws.",
    "purpose.person_identification.name": "Person identification",
    "...": "..."
  }

I bundle di localizzazione DEVONO essere disponibili all'URI specificato nell'attibuto **localization_info.bundles_base_uri** del Catalogo degli Attestati Elettronici. Ogni bundle locale DEVE essere accessibile seguendo il pattern di denominazione **{locale_code}.json**, dove **{locale_code}** è sostituito con il codice locale corrispondente dall'array **available_locales**.

Un esempio non normativo dell'URI di localizzazione italiana per il bundle sarebbe **https://trust-registry.eid-wallet.example.it/.well-known/taxonomy/it.json**. 

Le Entità DOVREBBERO verificare l'integrità dei bundle di localizzazione scaricati utilizzando il metodo di digest e i valori specificati nel claim **localization_info.integrity**. Questo garantisce che i dati di localizzazione non siano stati manomessi durante la trasmissione.

Registro degli Schema
---------------------

Il **Registro degli Schema** è l'inventario autorevole di tutti gli **Schema delle Credenziali** conosciuti e accettati (JSON Schema per SD-JWT, CBOR Schema per mDOC) all'interno dell'ecosistema IT-Wallet. È gestito dal Trust Anchor e fornisce una singola fonte verificabile per recuperare le specifiche tecniche richieste per analizzare, validare e visualizzare gli Attestati Elettronici.

**Obiettivi del Registro degli Schema:**

1. **Centralizzazione degli Schema**: Fornire un punto di accesso centralizzato per tutti gli schemi tecnici usati dalgli Attestati Elettronici.
2. **Integrità e Autenticità**: Garantire l'integrità e l'autenticità dei documenti degli schema attraverso digest crittografici.
3. **Interoperabilità**: Facilitare l'integrazione senza soluzione di continuità di Fornitori di Wallet e Relying Parties fornendo versioni di schema coerenti.
4. **Supporto al Ciclo di Vita delle Credenziali**: Agire come punto di riferimento verificabile per la validazione dello schema durante l'emissione e la presentazione.

**Struttura e Accesso al Registro degli Schema:**

Il Registro degli Schema è accessibile tramite l'endpoint di scoperta ``.well-known/it-wallet-registry`` sotto il campo `schema_registry`. Permette la scoperta di URI degli schema e i loro controlli di integrità crittografica.


.. list-table:: Campi di Primo Livello del Registro degli Schema
   :class: longtable
   :widths: 30 70
   :header-rows: 1

   * - **Nome del Campo**
     - **Descrizione**
   * - **version**
     - RICHIESTO. La versione del Registro degli Schema (es., ``1.0``).
   * - **last_modified**
     - RICHIESTO. Il timestamp che indica quando l'elenco è stato aggiornato l'ultima volta (es., ``2025-03-15T12:00:00Z``).
   * - **schemas**
     - RICHIESTO. Un Array JSON dove ogni elemento è un Oggetto JSON che rappresenta una definizione di Schema di Credenziale. Ogni oggetto contiene i parametri definiti nella tabella "Parametri della Definizione dello Schema" sottostante, inclusi identificazione dello schema, specifiche del formato, URI e dati di verifica dell'integrità.


.. list-table:: Parametri della Definizione dello Schema
   :widths: 25 75
   :header-rows: 1

   * - **Nome del Campo**
     - **Descrizione**
   * - **id**
     - RICHIESTO. L'identificatore univoco dello schema (es., ``mDL+mso_mdoc+org.iso.18013.5.1.mDL``).
   * - **version**
     - RICHIESTO. La versione della definizione dello schema (es., ``1.0``).
   * - **credential_type**
     - RICHIESTO. L'identificatore univoco del tipo di Credenziale Digitale (es., ``mDL``, ``pid``).
   * - **format**
     - RICHIESTO. Il formato tecnico dello schema (es., ``mso_mdoc``, ``dc+sd-jwt``).
   * - **vct**
     - CONDIZIONALE. È RICHIESTO se il ``format`` è ``dc+sd-jwt``, indicando il Tipo di Credenziale Verificabile (es., ``urn:eudi:mDL:it:1``).
   * - **docType**
     - CONDIZIONALE. È RICHIESTO se il ``format`` è ``mso_mdoc``, indicando il tipo di documento usato (es., ``org.iso.18013.5.1.mDL``).
   * - **schema_uri**
     - RICHIESTO. L'URI dove può essere recuperato il documento dello schema (es., ``https://trust-registry.it-wallet.example.it/.well-known/schemas/mdoc/mDL``).
   * - **schema_uri#integrity**
     - RICHIESTO. Digest crittografico del documento dello schema per la verifica dell'integrità. Formato: ``{digest_method}-{digest_value}`` (es., ``sha256-c8b708728e4c5756e35c03aeac257ca878d1f717d7b61f621be4d36dbd9b9c16``).
   * - **description**
     - OPZIONALE. Una descrizione leggibile dall'uomo dello schema, che può essere localizzata (es., "Schema tecnico per la mobile Driving License in formato mdoc.").

**Esempio del Registro degli Schema:**

Un esempio non normativo del payload del Registro degli Schema:

.. literalinclude:: ../../examples/schema-registry-example-payload.json
  :language: JSON

Integrazione del Registro e Riferimenti Incrociati
---------------------------------------------------

I componenti del registro sono interconnessi e lavorano insieme per supportare l'ecosistema completo delle Credenziali:

1. **Registro AS** ↔ **Tassonomia**: Le entità AS dichiarano capacità di fornitura utilizzando classificazioni della tassonomia per la categorizzazione standardizzata.
2. **Registro AS** ↔ **Catalogo**: I tipi di Credenziali fanno riferimento alle capacità AS per la validazione della fonte dati.
3. **Catalogo** ↔ **Tassonomia**: Le voci delle Credenziali specificano domini e scopi dalla tassonomia per discovery e autorizzazione.
4. **Registro della Federazione** ↔ **Tutti i Componenti**: Fornisce validazione del trust crittografico per tutte le operazioni del registro e autenticazione delle entità.
5. **Registro degli Schema** ↔ **Emittente/RP**: Fornisce il collegamento verificabile a tutte le specifiche di formato delle Credenziali conosciute usate nell'ecosistema.


Utilizzo dell'Infrastruttura di Registro
-----------------------------------------------------


I componenti dell'Infrastruttura di Registro sono progettati per supportare le varie fasi operative dell'ecosistema IT-Wallet, ciascuna coinvolgendo interazioni specifiche tra entità.
I principali Percorsi di utilizzo illustrano di seguito le interazioni con l'Infrastruttura di Registro.

Navigazione del Catalogo
^^^^^^^^^^^^^^^^^^^^^^^^^

Il percorso di utilizzo *Navigazione del Catalogo* supporta gli Utenti (sia utenti umani tramite un'**Istanza Wallet** che sistemi automatizzati come **Relying Parties** o portali web) nella scoperta e selezione degli Attestati Elettronici disponibili.

1.  **Accesso all'Endpoint di Scoperta**: L'entità (es., un Fornitore di Wallet o portale informativo) accede all'`Endpoint di Scoperta del Registro` (``.well-known/it-wallet-registry``) per ottenere l'URI del **Catalogo degli Attestati Elettronici**.

2.  **Navigazione e Selezione**:

  * **Scoperta delle Credenziali**: L'entità naviga l'elenco delle Credenziali (campo ``credentials``) per identificare tipi di Credenziali rilevanti (es., ``pid``, ``driving_license``).
  * **Metadati dell'Emittente**: L'entità estrae l'**Identificatore dell'Emittente** (`entity_id` all'interno del campo `issuers`) associato alla Credenziale desiderata.
  * **Consultazione dei Dettagli**: Per ottenere informazioni complete e requisiti tecnici specifici, l'entità accede all'**Entity Configuration** (Metadati dell'Emittente) usando l'identificatore recuperato.

3.  **Azione Finale**: L'entità può quindi usare i metadati per visualizzare le informazioni del catalogo a un Utente (o usare le informazioni in altro modo).

Emissione di Credenziali
^^^^^^^^^^^^^^^^^^^^^^^^^

Questo percorso definisce come un Emittente di Credenziali usa l'Infrastruttura di Registro per preparare ed emettere una Credenziale Digitale conforme.

1.  **Identificazione dei Requisiti**: Il CI consulta il **Catalogo degli Attestati Elettronici** per i requisiti tecnici del tipo di Credenziale da emettere (es., ``max_validity_days``, ``min_loa``).

2.  **Risoluzione dello Schema e dei Claims**:

  * Il CI consulta il **Registro degli Schema** per recuperare la specifica tecnica del formato e dello schema (es., JSON Schema per SD-JWT) richiesto dal Catalogo, garantendo validità e integrità tramite l'hash (`schema_uri#integrity`).
  * Il CI accede al **Registro dei Claims** per recuperare le definizioni semantiche standardizzate e i formati dati (tipi di dati) degli attributi necessari (claims).

3.  **Recupero dei Dati Autentici**:

  * Il CI consulta il **Registro delle Fonti Autentiche (AS)** per identificare la **Fonte Autentica** (AS) autorizzata per il dataset richiesto. Il Registro AS fornisce l'``entity_id`` dell'AS e i dettagli tecnici dell'interfaccia (`integration_endpoint`, `integration_method`).
  * Il CI consulta la specifica dell'endpoint AS per implementare l'integrazione necessaria per recuperare i dati dell'Utente richiesti per popolare la Credenziale Digitale.

4.  **Emissione della Credenziale**: Il CI usa i dati recuperati, gli schemi validati e i formati specificati per generare e firmare la Credenziale Digitale nel formato corretto (es., SD-JWT o mDOC).

Presentazione e Verifica delle Credenziali
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Questo percorso descrive come un'**Istanza Wallet** e una **Relying Party (RP)** interagiscono con l'Infrastruttura di Registro quando una Credenziale Digitale deve essere presentata da un Utente.

1.  **Autorizzazione e Selezione del Wallet**:

  * Il Wallet riceve una Richiesta di Presentazione dall'RP, verifica la validità della richiesta confrontando i *claims* richiesti con le *Policy di Autorizzazione* relative all'RP (tramite le definizioni della **Tassonomia**).
  * Il Wallet consulta il **Catalogo degli Attestati Elettronici** per verificare i *Domini* e *Scopi* associati ai tipi di Credenziali che detiene, valutando quali Credenziali sono adatte per la richiesta.
  * Il Wallet verifica se gli attributi richiesti (claims) sono disponibili e autorizzati per la divulgazione in base alla policy della richiesta (scenari **Credential-Specific** o **Credential-Agnostic**).
  * L'Utente autorizza il rilascio degli attributi selezionati, divulgati selettivamente. Il Wallet quindi confeziona e presenta la Credenziale Digitale all'RP.

2.  **Scoperta e Integrità**:

  * L'RP riceve la Credenziale Digitale dall'Utente.
  * L'RP consulta il **Registro di Federazione** tramite l'endpoint del Trust Anchor (`federation_resolve`, `federation_trust_mark_status`) per verificare la **fiducia crittografica** (Trust Mark) dell'Emittente e del Fornitore di Wallet, come definito nella Sezione :ref:`trust-infrastructure:L'Infrastruttura di Trust`.
  * L'RP consulta il **Registro degli Schema** per scaricare lo schema della Credenziale presentata (`schema_uri`), verificandone l'integrità (`schema_uri#integrity`).

3.  **Validazione dello Schema e della Policy Finale**:

  * L'RP usa lo schema recuperato per validare la struttura della Credenziale e i tipi di dati degli attributi rivelati.
  * L'RP esegue il controllo finale per garantire che gli attributi presentati siano conformi ai requisiti specifici della richiesta iniziale e della policy di autorizzazione.

4.  **Accettazione o Rifiuto**: In base alla validazione crittografica, alla conformità dello schema e all'autorizzazione basata su policy, l'RP accetta o rifiuta la Credenziale per l'accesso al servizio.



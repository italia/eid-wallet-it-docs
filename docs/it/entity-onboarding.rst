.. include:: ../common/common_definitions.rst
.. include:: ../common/symbols.rst

Onboarding delle Entità
========================

Questa sezione definisce le Specifiche Tecniche per la gestione del ciclo di vita delle entità nell'ecosistema IT-Wallet basato sull'**Infrastruttura di Registro** definita in :ref:`registry:Infrastruttura del Registro`. Questo include le procedure di onboarding iniziale, le operazioni di gestione continua (aggiornamenti dei dati, modifiche) e i processi di uscita dalla federazione. Il sistema di gestione del ciclo di vita stabilisce e mantiene l'infrastruttura di trust federata e il coordinamento del registro necessari per le operazioni sicure degli Attestati Elettronici.

Per una panoramica di alto livello del processo di onboarding, vedere :ref:`onboarding-high-level:Sistema di Onboarding`. In particolare, la Sezione :ref:`onboarding-high-level:Onboarding Journey Maps` fornisce una mappa delle Journey di onboarding dal punto di vista degli operatori delle Entità.

Panoramica
----------

Architettura del Sistema di Onboarding delle Entità
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

L'ecosistema IT-Wallet è basato su un'infrastruttura di trust federata dove le entità partecipanti DEVONO stabilire relazioni di trust crittografiche e mantenere la conformità A standard di sicurezza comuni.

Il framework di onboarding DEVE consentire procedure di registrazione tecnica specifiche rispetto al ruolo del partecipante nell'ecosistema IT-Wallet:

  1. Per le Fonti Autentiche sono richieste procedure di registrazione focalizzate sui dati.
  2. Per le Entità operative (Credential Issuer, Relying Party, Fornitori di Wallet) è richiesta l'istituzione di trust crittografico attraverso protocolli di federazione.

Tipi di Entità e percorsi di Onboarding
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

La seguente tabella riassume i tipi di entità, i loro ruoli e i corrispondenti percorsi di onboarding:

.. list-table:: Tipi di Entità e percorsi di Onboarding
   :class: longtable
   :widths: 20 30 25 25
   :header-rows: 1

   * - **Tipo di Entità**
     - **Ruolo Primario**
     - **Percorso di Onboarding**
     - **Requisiti Chiave**
   * - Fonti Autentiche
     - Fornitori di dati autorevoli per gli Attributi degli Attestati Elettronici
     - :ref:`entity-onboarding:Processo di Registrazione delle Fonti Autentiche`
     - Validazione dell'autorità dei dati, integrazione API (PDND/Custom).
   * - Credential Issuer
     - Generano ed emettono Attestati Elettronici utilizzando i dati delle Fonti Autentiche
     - :ref:`entity-onboarding:Processo di Onboarding delle Entità di Federazione`
     - Conformità all'Infrastruttura di Trust IT-Wallet, :ref:`trust-infrastructure:L'Infrastruttura di Trust`.
   * - Relying Party
     - Verificano gli Attestati Elettronici per l'accesso ai servizi
     - :ref:`entity-onboarding:Processo di Onboarding delle Entità di Federazione`
     - Conformità all'Infrastruttura di Trust IT-Wallet, :ref:`trust-infrastructure:L'Infrastruttura di Trust`.
   * - Fornitori di Wallet
     - Forniscono Soluzioni Wallet ai cittadini
     - :ref:`entity-onboarding:Processo di Onboarding delle Entità di Federazione`
     - Conformità all'Infrastruttura di Trust IT-Wallet :ref:`trust-infrastructure:L'Infrastruttura di Trust`, capacità di emissione della Wallet Attestation :ref:`wallet-instance-registration:Inizializzazione e Registrazione dell'Istanza del Wallet`.
   * - Istanze del Wallet
     - Applicazioni di portafoglio digitale reso disponibile all'Utente
     - Registrazione indiretta tramite Fornitore di Wallet, vedere :ref:`wallet-instance-registration:Inizializzazione e Registrazione dell'Istanza del Wallet`.
     - Wallet Attestation emessa da Fornitore di Wallet affidabile.

Registrazione Amministrativa vs Tecnica
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Il processo di onboarding segue un approccio strutturato multi-fase:

  1. **Registrazione Amministrativa**: Tutte le entità DEVONO completare la registrazione amministrativa iniziale che valida la loro posizione legale, conformità normativa ed eleggibilità organizzativa per partecipare all'ecosistema IT-Wallet.

  2. **Registrazione Tecnica**: Dopo l'approvazione amministrativa, le entità effettuano la registrazione tecnica secondo il proprio percorso previsto:
    
    - **Registrazione Fonte Autentica**: Procedure di registrazione focalizzate sui dati con validazione dell'integrazione API.
    - **Registrazione di Federazione**: Istituzione di trust crittografico come definito nella Sezione :ref:`trust-infrastructure:L'Infrastruttura di Trust`.

  3. **Integrazione del Registro IT-Wallet**:

    - **Integrazione del Registro Claims**: Le Fonti Autentiche selezionano definizioni di claim standardizzate dal Registro degli Attributi durante la dichiarazione delle specifiche.
    - **Integrazione della Tassonomia**: Tutte le entità utilizzano la classificazione gerarchica della Tassonomia (domini, scopi) per la struttura organizzativa per categorizzare gli Attestati Elettronici.
    - **Integrazione del Registro AS**: Le Fonti Autentiche registrate con i loro attributi dichiarati e le relative specifiche, abilitando la discovery e coordinamento con i Credential Issuer.
    - **Integrazione del Registro di Federazione**: Entità operative incluse per la validazione del trust durante le operazioni delle attestazioni elettroniche.
    - **Integrazione del Catalogo**: Tipi di attestati elettronici pubblicati in :ref:`registry:catalogo degli attestati elettronici` basati sulle policy dell'organismo di supervisione per l'eleggibilità alla discovery pubblica.

Tutti i componenti del registro e le loro interazioni sono dettagliati in :ref:`registry:Infrastruttura del Registro`.

Processo di Registrazione delle Fonti Autentiche
-------------------------------------------------

Le Fonti Autentiche subiscono una registrazione sistematica per stabilire il loro ruolo come fornitori di dati autorevoli all'interno dell'ecosistema IT-Wallet. Il processo di registrazione consiste nella specifica dei requisiti e nella validazione procedurale come descritto in :ref:`onboarding-high-level:Journey dell'Operatore della Fonte Autentica`.

Requisiti di Registrazione AS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Le Fonti Autentiche DEVONO rispettare i seguenti requisiti tecnici per garantire l'interoperabilità dell'ecosistema:

  - **Conformità dei Claims**:

    - **Adozione del Registro dei Claims**: Le Entità DEVONO necessariamente utilizzare identificativi standardizzati censiti nel Registro dei Claims all'interno delle response.

  - **Standard di Integrazione API**:

    - **Entità Pubbliche**: DEVONO integrarsi attraverso la piattaforma PDND con implementazione di e-service seguendo gli standard governativi.
    - **Entità Private**: DEVONO fornire un documento completo di Specifica `OAS3`_ che include framework di autorizzazione, schemi di request/response, meccanismi di gestione degli errori e ambiente sandbox per i test.

  - **Standardizzazione del Formato di Response**:

    - **Formato Standard dei Claims**: Le Entità DEVONO utilizzare identificativi e formati censiti nel Registro dei Claims in tutte le response relative ai dati.
    - **Mappatura degli Stati**: Le Entità DEVONO gestire una mappatura chiara tra i loro stati interni e gli stati standard delle attestazioni elettroniche (valido, sospeso, revocato).

  - **Sicurezza e Garanzia di Qualità**:

    - **Standard di Sicurezza**: Le Entità DEVONO implementare minimo TLS 1.3 con meccanismi di autenticazione e sicurezza appropriati.
    - **Evidenza di Autenticazione dell'Utente**: Le Entità POSSONO richiedere l'evidenza di autenticazione dell'Utente dal Credential Issuer prima di concedere l'accesso agli e-service per ottenere gli Attributi dell'Utente.
    - **Qualità dei Dati**: Le Entità DEVONO specificare la frequenza di aggiornamento e fornire garanzie sulla freschezza dei dati.
    - **Traccia di Audit**: Le Entità DEVONO implementare capacità di logging per tutte le attività di accesso e fornitura dei dati.

Requisiti sulle Informazioni di Registrazione delle AS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Durante la registrazione, le Fonti Autentiche DEVONO fornire le seguenti informazioni:

.. list-table:: sulle Informazioni di Registrazione delle AS
   :class: longtable
   :header-rows: 1
   :widths: 30 70

   * - Categoria delle Informazioni
     - Descrizione ed Esempi
   * - **Informazioni Organizzazione**
     - **OBBLIGATORIO**. Dettagli dell'organizzazione inclusi:

       - Nome dell'organizzazione, tipo ("publico" o "privata") e paese (ISO 3166-1 alpha-2).
       - Codici identificativi amministrativi come codice di registrazione IPA (OBBLIGATORIO solo per Fonti Autentiche pubbliche) e identificatore legale (Codice Fiscale/Partita IVA).
       - Informazioni di contatto inclusi indirizzi email di contatto tecnico e amministrativo, URI homepage, URI politica privacy, ecc.
   * - **Dichiarazione Disponibilità dei Dati**
     - **OBBLIGATORIO**. Claims disponibili:

       - Array che include identificativi dei claim censiti nel Registro Claims che la Fonte Autentica fornisce (es., ``["given_name", "family_name", "driving_privileges"]``).
       - Classificazione tassonomica per l'ambito della Fonte Autentica (es., domini ``[AUTHORIZATION]`` e scopi ``["DRIVING_LICENSE"]``).
      
   * - **Dettagli di Implementazione API**
     - **OBBLIGATORIO**. Dettagli sulle informazioni di integrazione:

       - Framework di autorizzazione per l'accesso API.
       - Definizioni delle API come i formati di Request/Response, inclusa la gestione degli errori.
   * - **Capacità di Fornitura Dati**
     - **OBBLIGATORIO**. Indica se la Fonte Autentica supporta la fornitura di dati in modalità immediate/deferred (booleano).    
   * - **Informazioni Utente**
     - **OBBLIGATORIO**. Testo formattato in Markdown contenente informazioni leggibili dall'uomo sui vincoli o limitazioni di disponibilità dei dati. Ad esempio, se il database AS contiene solo dati registrati dopo una data specifica, questa informazione DEVE essere comunicata agli utenti.

       **Esempio**: "I dati della patente di guida sono disponibili per le patenti rilasciate dopo il 1° gennaio 2020. Per patenti più vecchie, contattare l'ufficio di motorizzazione locale.".
   * - **Proprietà di Visualizzazione**
     - **OPZIONALE**. Suggerimenti di branding visivo per le attestati elettronici che utilizzano i dati AS:

       - Colore di sfondo per gli Attestati Elettronici in formato esadecimale (es., ``"#003d82"``).
       - Colore del testo per gli Attestati Elettronici in formato esadecimale (es., ``"#ffffff"``).
       - URI del logo con verifica dell'integrità crittografica per il branding degli Attestati Elettronici.
       - URI del template visivo con verifica dell'integrità per la presentazione degli Attestati Elettronici.

.. note::
  Solo Fonti Autentiche italiane possono essere onboardate nella fase attuale di IT-Wallet.

Procedura di Registrazione AS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

La registrazione della Fonte Autentica segue un processo tecnico come descritto di seguito.

.. plantuml:: plantuml/as-registration-process.puml
    :width: 99%
    :alt: Processo di registrazione della Fonte Autentica che mostra la procedura in 3 fasi
    :caption: `Processo di Registrazione della Fonte Autentica. <https://www.plantuml.com/plantuml/svg/TLD1Rziw3BxxLn0zlG1vhs_hBK26TkqEFMmBbcAdNcY9SRJAaaPARRDVFzfE6iVBWXmCyUF7Z_p8Qyd8kRGURahUKiZEm3eMDWJVg76I6REB0LOS3ObKM78CfQs9goeXAzmb31akfkaNWAB_Kz2w9E9d9v5ty37QNG-IUiAqFfGUuanDLIsNiCwKuDrYeWlD4pQa-YZX_csvh2hD-_U3PY_s4OB83GRtQu2ui8dSzj-FuP_xrGsOQ6aEdXhqu6pNoSOHp_KzP3HPPYFAEpA-exIO4Gmch9rtsP4erwr7ryfR1oCkcSC3liOGsnreleY-cbx2AVV61OARrJsuDdbgDNtGR2cZyrsDrTsNkyklYKA7klhlVv14vYpRkW_i1gM9eyvU4LFDhct9EinqQMb3p6HXu-CBI4afSZuGIgs4fMvT1XvxmFIpaEIZIUyNy41c6rIGX-_edJqQ8_MUwX0Wc8xCH6tSOJ2asWQVvgTpf5T5aW9cOpvYRVLlCrOg6rjqGTFrXPh8ZlGx5KvHICPCjrioJuC5GP7xDf-9nsoT2IEf41b6bipEDSeaAGOX69e2oHWiiZstDqMmeRb2kiGMKtAXcUbU-poUg1JJdUMc-0hqDzH4cHm9fivwz5hc-PZRQwUiCoGlD6RTeFDa_s3yGQOFlxYyXH6H4odz7dMBuBXVMO4S0QrbLQS5WZrknzK2HYSEgr9xPwOBmjGiXf1iE_WdDJ_lr0_WVQBMEtG0TZX8ErviBQlGDwxF-4GTaNLYebg9jIUebUMMgLyjz73VDSAYwtvsZ8ToYyV0X7RNsGWnqH16FxcogWfHjNN5b6lUgr01MgkN1pKf8PqAUhj4hygABil9gD9nL5LrJS6Mrly6>`_ 

**Fase 1 - Preparazione del Pacchetto di Registrazione**: L'Entità prepara le informazioni di registrazione secondo la tabella dei requisiti sopra. Un esempio non normativo di informazioni in formato JSON è fornito di seguito.

.. code-block:: json

   {
     "entity_id": "https://transport-authority.gov.example",
     "organization_info": {
       "organization_name": "Autorità Nazionale dei Trasporti",
       "organization_type": "public",
       "ipa_code": "nta_001",
       "legal_identifier": "12345678901",
       "organization_country": "XX",
       "homepage_uri": "https://www.gov.example/transport",
       "contacts": ["registry@transport-authority.gov.example", "technical-support@transport-authority.gov.example"],
       "policy_uri": "https://www.gov.example/transport/privacy-policy",
       "user_information": "I dati della patente di guida sono disponibili per le patenti rilasciate dopo il 1° gennaio 2020. Per patenti più vecchie, contattare l'ufficio dell'autorità dei trasporti locale.",
       "logo_uri": "https://www.gov.example/assets/transport-logo.svg",
       "logo_uri#integrity": "sha-256-a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3"
     },
     "data_capabilities": [
       {
         "domains": ["IDENTITY", "AUTHORIZATION"],
         "intended_purposes": ["DRIVING_LICENSE"],
         "available_claims": [
           "given_name", "family_name", "birth_date", "birth_place",
           "issue_date", "expiry_date", "document_number", "driving_privileges"
         ],
         "integration_method": "pdnd",
         "integration_endpoint": "https://api.gov.example/transport/driving-license",
         "api_specification": "https://docs.gov.example/transport/api-oas3.yaml",
         "data_provision": {
           "immediate_flow": true,
           "deferred_flow": false
         },
         "update_frequency": "real_time",
         "display": {
          "background_color": "#003d82",
          "text_color": "#ffffff",
         }
       }
     ]
   }

**Fase 2 - Validazione Tecnica**: L'Organismo di Supervisione valida la registrazione presentata concentrandosi su:

  - **Conformità con il Registro dei Claims**: Validazione del formato dei claim, degli identificativi ed esistenza nel Registro dei Claims.
  - **Validazione Tassonomia**: Verifica che i domini e finalità dichiarate siano voci tassonomiche valide.
  - **Verifica Integrazione API**:

    - **Entità Pubbliche**: Verifica della conformità della specifica e-service PDND
    - **Entità Private**: Completezza della specifica `OAS3`_ inclusi framework di autorizzazione, schemi di request/response, meccanismi di gestione degli errori e ambiente sandbox.

  - **Formato Standard della Response**: Verifica dell'utilizzo del formato del Registro dei Claims e specifica della mappatura degli stati.

**Fase 3 - Pubblicazione Registro AS**: Dopo la validazione con successo:

  - L'Entità Fonte Autentica viene pubblicata nel Registro AS con le informazioni dichiarate complete.
  - La Fonte Autentica diventa scopribile dai Credential Issuer per le richieste di integrazione.
  - La Fonte Autentica è pronta per la fornitura operativa dei dati.

.. note::
   La registrazione AS è completa e indipendente dall'integrazione CI. Le entità AS diventano scopribili immediatamente dopo la pubblicazione del Registro AS, mentre la disponibilità degli Attestati Elettronici agli utenti finali dipende dall'autorizzazione amministrativa AS-CI seguita da un'integrazione tecnica di successo e dall'approvazione della politica dell'Organismo di Supervisione per l'eleggibilità al catalogo.

Processo di Integrazione AS-CI
-------------------------------

Dopo l'autorizzazione amministrativa AS-CI ottenuta durante la fase di registrazione amministrativa, le procedure di integrazione tecnica stabiliscono le connessioni API operative e i meccanismi di accesso ai dati tra Credential Issuer e Fonti Autentiche.

L'integrazione tecnica comprende:

- **Configurazione degli Endpoint API**: Istituzione di connessioni API sicure come specificato nelle Specifiche Tecniche AS (e-service PDND per AS pubbliche, implementazioni `OAS3`_ per AS private).
- **Validazione Mappatura Claims**: Verifica che l'implementazione CI mappi correttamente le response dei dati AS agli identificativi standardizzati del Registro dei Claims.
- **Test Flusso Dati**: Validazione delle specifiche di fornitura dati immediate/deferred e meccanismi di gestione degli errori.
- **Implementazione Sicurezza**: Configurazione di autenticazione, autorizzazione e logging di audit come richiesto dagli standard di sicurezza AS.

Processo di Onboarding delle Entità di Federazione
---------------------------------------------------

Le Entità di Federazione (Credential Issuer, Relying Party e Fornitori di Wallet) DEVONO sottoporsi a procedure di onboarding per stabilire relazioni di trust crittografiche all'interno dell'ecosistema IT-Wallet. Il processo di onboarding della federazione stabilisce l'infrastruttura di trust distribuita attraverso l'emissione di certificati, la configurazione della catena di trust e l'attestazione di conformità come dettagliato in :ref:`trust-infrastructure:L'Infrastruttura di Trust`.

Modello Gerarchico dell'Autorità di Federazione
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

La federazione IT-Wallet implementa un **modello di onboarding gerarchico** dove le Entità di Federazione POSSONO essere onboardate da:

  1. **Trust Anchor**: L'autorità radice che ha la capacità di onboardare direttamente qualsiasi Entità di Federazione.
  2. **Intermediari**: Autorità delegate che onboardano Entità Foglia per conto del Trust Anchor.

Questo approccio gerarchico abilita la **gestione distribuita dell'onboarding** mantenendo un'istituzione di trust unificata. Sia i Trust Anchor che gli Intermediari agiscono come **Autorità di Federazione** con le seguenti capacità di onboarding:

  - **Emissione dei Certificati**: Emettono certificati X.509 ai loro subordinati immediati con vincoli di denominazione appropriati come definito in :ref:`trust-infrastructure:X.509 PKI`.
  - **Applicazione delle Metadata Policy**: Applicano le metadata policy specifiche della federazione con **effetto a cascata** (le policy del Trust Anchor prevalgono sulle policy degli Intermediari).
  - **Emissione del Trust Mark**: Emettono Trust Mark di Federazione attestando la conformità dei subordinati ai requisiti della federazione.

Pertanto, le Entità di Federazione POSSONO essere onboardate attraverso percorsi diversi:

  - **Onboarding Diretto dal Trust Anchor**: L'entità si registra direttamente con il Trust Anchor.
  - **Onboarding Mediato da Intermediario**: L'entità si registra con un Intermediario appropriato.

Prerequisiti di Onboarding della Federazione
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Le Entità di Federazione DEVONO rispettare i seguenti requisiti tecnici prima di iniziare il processo di onboarding:

  - **Generazione delle Chiavi**: Le entità DEVONO generare almeno due coppie di chiavi utilizzando la crittografia a curva ellittica come specificato in :ref:`algorithms:Algoritmi Crittografici`:

    - **Coppia di Chiavi di Federazione**: Utilizzata per firmare Entity Configuration e attestare Chiavi di Protocollo. Per le migliori pratiche di sicurezza e continuità operativa, le entità DOVREBBERO mantenere multiple Chiavi dell'Entità di Federazione (almeno due) per abilitare la rotazione sicura delle chiavi e la risposta agli incidenti senza impattare le entità che hanno memorizzato nella cache le Entity Configuration.
    - **Coppia/e di Chiavi di Protocollo**: Utilizzate per operazioni di protocollo specifiche dell'entità (emissione attestati elettronici, verifica presentazione, ecc.).

  - **Attestazione delle Chiavi di Protocollo**: Le entità DEVONO creare certificati X.509 auto-firmati per le loro Chiavi di Protocollo utilizzando la Chiave Privata di Federazione. Questi certificati stabiliscono la relazione di autorità tra le chiavi di Federazione e di Protocollo.

  - **Preparazione Entity Configuration**: Le entità DEVONO pubblicare una Entity Configuration (EC) firmata con la loro Chiave Privata di Federazione all'endpoint ``/.well-known/openid-federation`` come definito in :ref:`trust-infrastructure:L'Infrastruttura di Trust`. L'EC DEVE includere:

    - Un claim ``jwks`` contenente le Chiavi dell'Entità di Federazione in formato JSON Web Key (JWK).
    - Un claim ``iss`` con l'Identificativo dell'Entità di Federazione come definito in :ref:`trust-infrastructure:Ruoli di Federazione`.
    - Un claim ``sub`` uguale al claim ``iss``.
    - Claim ``iat`` ed ``exp`` che definiscono un intervallo di tempo valido.
    - Un claim ``metadata`` contenente metadati specifici dell'entità organizzati per Tipi di Metadati (vedere :ref:`credential-issuer-entity-configuration:Entity Configuration del Fornitore di Attestati Elettronici`, :ref:`relying-party-entity-configuration:Entity Configuration di una Relying Party`, o :ref:`wallet-provider-entity-configuration:Entity Configuration del Fornitore di Wallet`) con Chiavi di Protocollo incluse nei campi ``jwks`` dei metadati e certificati auto-firmati nei corrispondenti claim ``x5c``.

  - **Certificate Signing Request (CSR)**: Le entità DEVONO preparare un CSR in formato PKCS #10 contenente **solo la Chiave Pubblica dell'Entità di Federazione** per l'emissione del certificato X.509 da parte dell'Autorità di Federazione come definito in :ref:`trust-infrastructure:Requisiti dell'Infrastruttura di Trust`.

Requisiti di Sicurezza per la Gestione delle Chiavi
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Tutte le entità di federazione DOVREBBERO mantenere almeno due chiavi di firma certificate dal Trust Anchor:

- **Chiave Attiva**: Utilizzata per le operazioni di firma correnti
- **Chiave di Backup**: Disponibile per l'attivazione immediata durante incidenti o rotazione pianificata delle chiavi

Questo approccio a doppia chiave abilita:
- Rotazione sicura delle chiavi senza interruzione del servizio
- Risposta rapida agli incidenti quando le chiavi primarie sono compromesse
- Continuità per le entità con Entity Configuration memorizzate nella cache
- Prevenzione di problemi di validazione durante le transizioni delle chiavi

La chiave di backup DEVE essere:
- Registrata dal Trust Anchor prima del deployment
- Pubblicata nel JWKS dell'entità insieme alla chiave attiva
- Pronta per l'attivazione immediata senza passaggi di certificazione aggiuntivi
- Mantenuta con gli stessi standard di sicurezza della chiave attiva

Procedura di Onboarding della Federazione
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

L'onboarding della federazione segue una procedura strutturata in 4 fasi che abilita interazioni sicure tra i partecipanti della federazione, **indipendentemente dal fatto che l'onboarding sia eseguito dal Trust Anchor o da un Intermediario**.

.. note::
   La seguente procedura si applica ai Fornitori di Wallet, Credential Issuer e Relying Party che desiderano eseguire l'onboarding nella federazione IT-Wallet. L'**Autorità di Federazione** si riferisce al Trust Anchor o Intermediario secondo le caratteristiche organizzative e le policy di governance della federazione.

.. note::
   Questa sezione copre solo i requisiti di registrazione tecnica. Tutte le informazioni amministrative (validazione dell'entità legale, conformità normativa, eleggibilità organizzativa, ecc.) si presume siano state raccolte e validate dall'Organismo di Supervisione durante la fase di registrazione amministrativa, che è fuori dall'ambito di questa specifica tecnica. Esempi di informazioni amministrative includono: nome dell'entità legale, numeri di registrazione aziendale, persone di contatto, documentazione di conformità legale e autorizzazioni operative.

.. plantuml:: plantuml/federation-onboarding-process.puml
    :width: 99%
    :alt: Processo di onboarding dell'entità di federazione che mostra la procedura in 4 fasi
    :caption: `Processo di Onboarding dell'Entità di Federazione. <https://www.plantuml.com/plantuml/svg/dLHHRnit37w_Nq7qOKYmfF6wz646l3NmqY4BXXPEr-t1G41BF5khZhf9L5B_-vqi7quvtu1XRmSToUyZFtvy5mIznCR2UzBaKOnZk6KnieSFl77ejU4jVFHEKGWLHd4ScmtvgcgxHADCYopmwYJx5M20clurwYRApla-KB2g5Wju46hXktc9lAA_8mM1XxXfJ0WfTR6egfhWyaSGdESV0cv8yJbbpMV7Hkv-le2FSMEDWdlQmwz_t5_0yc5rFc2-cSCKD_YCrkZyYAnXILvCRHGAmLq84LdHWOvWJ-SpULFlmTFM13dMCrmxtno-oyXSc_fnBntNPXkFETZnlthzJDPUVc7tp5Uk9JRwiXve4klM6PQYvatRsZqq9AXH45fdZJ8KuDd83XG6XOS9KLsJAlDICmH_ldux-m5KqMJ7UyqdsXR3h2gqKeufH9KsfOws0W3843NDNynExT0mU0gjuq23K2Nqju2z3ELxEA_81YeXQpIMz0XkHN-HIhzpxqOJfnAamQHUGqMi1_s_dq-hy7jxK2XflwBWx1Fr2rbiOOBBWPD5vck-X1kjXtuUTuObWB9eclxdrxSgFnor6azhmChJ3pk81qmDjyl_i2s3O_fE2fzS-VpqKuYR1R4aZaP_8pu6UKHM7Us5OFTKMEPwABJAGkOv5TvTkgQrbD179bcHwkAxyahWAGa91wZSQH7t2t6YJwKvFnqYVqF_9MqdPBRbAhEoKLCPPpXT2PT8fM8FWa8DiKmX1RDbqjsD-9I5A8XThFdfw5azU2prZCbsgUCJvsL_z8CQp05dRsOp-71_VhAsERBtHYRHiUbKAgXqxZYbaciDEhydKRlfpfFcTVhzKl4ncydSJ6aORu6QScw_YaSbBtJohfckDSgzOw6jHncfDschVY2FJHTqD5FcV-gKsZ3Q_tjdyxtfXSd71iwkPxEhwzdrU6AttZi_KYyV7107Hvlbs_EEMCV6_WC0>`_

**Fase 1 - Invio Richiesta di Onboarding**: L'Entità di Federazione inizia il processo di onboarding inviando una richiesta di registrazione tecnica includendo le seguenti informazioni.

.. list-table:: Informazioni della Richiesta Tecnica di Onboarding della Federazione
   :class: longtable
   :header-rows: 1
   :widths: 30 70

   * - **Categoria delle Informazioni Tecniche**
     - **Requisiti e Descrizione**
   * - **Identificativo Entità di Federazione**
     - **OBBLIGATORIO**. Un URL unico che identifica l'Entità di Federazione come definito in :ref:`trust-infrastructure:Ruoli di Federazione`.
   * - **Chiave Pubblica Entità di Federazione (JWK)**
     - **OBBLIGATORIO**. Chiave pubblica ellittica in formato JSON Web Key utilizzata per firmare Entity Configuration e attestare Chiavi di Protocollo, utilizzando algoritmi crittografici specificati in :ref:`algorithms:Algoritmi Crittografici`.
   * - **Certificate Signing Request (CSR)**
     - **OBBLIGATORIO**. CSR in formato PKCS #10 per l'emissione del certificato X.509 da parte dell'Autorità di Federazione. Il CSR DEVE:

       - Contenere **solo la Chiave Pubblica dell'Entità di Federazione** da certificare.
       - Essere firmato con la corrispondente Chiave Privata di Federazione.
       - Definire il Subject del certificato con gli attributi richiesti come specificato in :ref:`trust-infrastructure:Emissione di Certificati X.509` per le Entità di Federazione.

.. warning::
   Prima di inviare la richiesta di onboarding tecnico, le Entità di Federazione DEVONO assicurarsi che il loro endpoint ``/.well-known/openid-federation`` pubblichi una Entity Configuration valida (come definita in :ref:`trust-infrastructure:Entity Configuration`) firmata con la loro Chiave Privata di Federazione corrispondente alla Chiave Pubblica dell'Entità di Federazione fornita nella richiesta. L'Entity Configuration DEVE già includere le Chiavi di Protocollo nei metadati con certificati X.509 auto-firmati nei claim ``x5c``.

Un esempio non normativo della struttura delle informazioni tecniche che le Entità di Federazione inviano durante la richiesta di onboarding della Fase 1:

.. code-block:: json

  {
    "entity_id": "https://credentials.example.gov",
    "entity_type": "credential_issuer",
    "jwks": {
      "keys": [
        {
          "kid": "NsXymfIILEPR5Y0t",
          "kty": "EC",
          "x": "gXY4FApFJCj91Gpb1K9GEIouTq2X3L0K64Iq0ob4l_g",
          "y": "l-6dcrIrFVdrzoY9cRJv9zNuFOR3MsDz6TSDhB0xEo4",
          "crv": "P-256"
        }
      ]
    },
    "certificate_signing_request": "-----BEGIN CERTIFICATE REQUEST-----\nMIIBTTCB9QIBADCBkjELMAkGA1UEBhMCSVQxDjAMBgNVBAgMBUxhemlvMQ0wCwYD\nVQQHDARSb21hMRYwFAYDVQQKDA1QYWdvUEEgUy5wLkEuMSQwIgYDVQQDDBtmb28x\nMS5ibG9iLmNvcmUud2luZG93cy5uZXQxJjAkBgkqhkiG9w0BCQEWF3BhZ29wYXNw\nYUBwZWMucGFnb3BhLml0MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEgXY4FApF\nJCj91Gpb1K9GEIouTq2X3L0K64Iq0ob4l_g\n-----END CERTIFICATE REQUEST-----",
    "submission_timestamp": "2025-09-25T14:30:00Z"
  }

Di seguito viene mostrato il contenuto decodificato dell'esempio CSR sopra riportato per riferimento:

.. code-block:: text

   Certificate Request:
       Data:
           Version: 0 (0x0)
           Subject: CN=credentials.example.gov, OU=Digital Credentials, O=Example Organization, L=Roma, ST=Lazio, C=IT, emailAddress=technical@credentials.example.gov
           Subject Public Key Info:
               Public Key Algorithm: id-ecPublicKey
                   Public-Key: (256 bit)
                   ASN1 OID: prime256v1
                   NIST CURVE: P-256
       Signature Algorithm: ecdsa-with-SHA256

.. note::
   Gli attributi Subject del CSR DEVONO rispettare i requisiti specificati in :ref:`trust-infrastructure:Emissione di Certificati X.509` per le Entità di Federazione.

.. note::
   La Chiave Pubblica dell'Entità di Federazione nel campo ``jwks`` e la chiave pubblica contenuta nel ``certificate_signing_request`` DEVONO essere la stessa chiave. La chiave è fornita in due formati: formato JWK per le operazioni OpenID Federation e formato CSR PKCS #10 per l'emissione del certificato X.509 da parte dell'Autorità di Federazione. Le Chiavi di Protocollo sono incluse solo nei metadati dell'Entity Configuration e NON DEVONO essere incluse nella richiesta di onboarding.

.. note::
   L'Endpoint Entity Configuration è costruito automaticamente aggiungendo ``/.well-known/openid-federation`` all'Identificativo dell'Entità di Federazione (``entity_id``). Le Entità di Federazione non devono specificare questo endpoint separatamente nella richiesta di registrazione.

**Fase 2 - Validazione dell'Autorità di Federazione ed Emissione Certificato**: Dopo l'invio della richiesta di onboarding, l'**Autorità di Federazione** DEVE eseguire:

  - Verifica delle informazioni fornite nella richiesta di registrazione.
  - Validazione dell'Entity Configuration pubblicata all'endpoint ``/.well-known/openid-federation`` dell'entità e dei suoi metadati contenuti (come definito in :ref:`trust-infrastructure:L'Infrastruttura di Trust`).
  - **Applicazione delle Metadata Policy**: Applicazione di metadata policy specifiche della federazione ai metadati dell'entità basate su caratteristiche organizzative e ambito di autorizzazione come definito in :ref:`trust-infrastructure:Subordinate Statement`. Quando onboardata attraverso un Intermediario, si applicano sia le policy dell'Intermediario che del Trust Anchor, con le policy del Trust Anchor che hanno precedenza in caso di conflitti.
  - **Emissione Certificato**: Certificazione della Chiave Pubblica dell'Entità di Federazione con emissione del certificato X.509 utilizzando l'infrastruttura di trust dettagliata in :ref:`trust-infrastructure:Requisiti dell'Infrastruttura di Trust`. Gli Intermediari emettono certificati con **naming constraints** appropriati per limitare l'uso del certificato solo ai loro subordinati.

Dopo la validazione con successo, l'entità riceve una risposta contenente una catena di certificati dove:

  - Il primo elemento è il certificato X.509 che certifica la Chiave Pubblica dell'Entità di Federazione (emesso dall'Autorità di Federazione).
  - **Per onboarding attraverso Trust Anchor**: Il secondo elemento è il certificato X.509 auto-firmato del Trust Anchor per validare il primo certificato.
  - **Per onboarding attraverso Intermediario**: Elementi aggiuntivi includono il certificato dell'Intermediario e il certificato auto-firmato del Trust Anchor, formando una catena di certificati completa.
  - Tutti i certificati sono espressi in formato DER codificato in Base64.

Esempio di risposta catena di certificati:

.. code-block:: json

   [
     "MIIDqjCCA1GgAwIBAgIGAZc6/V9qMAoGCCqGSM49BAMCMIGzMQsw...",
     "MIIDQzCCAuigAwIBAgIGAZc6+XlDMAoGCCqGSM49BAMCMIGzMQsw..."
   ]

.. note::
   Se la validazione fallisce, l'entità riceve una response con i problemi identificati che devono essere risolti prima di inviare una nuova richiesta di onboarding.

**Fase 3 - Aggiornamento Entity Configuration e Richiesta Resolve**: Dopo aver ricevuto la catena di certificati dall'Autorità di Federazione, l'entità DEVE:

  1. **Aggiornare Entity Configuration**:

    - Aggiungere un claim ``authority_hints`` con un Array JSON contenente l'Identificativo dell'Entità di Federazione dell'**immediate Federation Authority** (Trust Anchor per onboarding diretto, o Intermediario per onboarding mediato) come definito in :ref:`trust-infrastructure:Ruoli di Federazione`.
    - Aggiornare la Chiave Pubblica dell'Entità di Federazione nel claim ``jwks`` aggiungendo un claim ``x5c`` con la catena di certificati completa ricevuta dall'Autorità di Federazione.
    - Aggiornare le Chiavi di Protocollo nei claim ``jwks`` dei metadati estendendo i loro claim ``x5c`` esistenti per includere la catena di certificati di Federazione, creando catene di trust complete dalle Chiavi di Protocollo all'Autorità Radice.

    Esempio aggiunta authority_hints:

    .. code-block:: json

        {
          "iat": 1718207217,
          "exp": 1749743216,
          "iss": "https://credentials.example.gov",
          "sub": "https://credentials.example.gov",
          "authority_hints": ["https://trust-anchor.example.gov"],
          //...
        }

    Esempio JWK di Federazione con catena di certificati:

    .. code-block:: json

        {
          "kid": "NsXymfIILEPR5Y0t",
          "kty": "EC",
          "x": "gXY4FApFJCj91Gpb1K9GEIouTq2X3L0K64Iq0ob4l_g",
          "y": "l-6dcrIrFVdrzoY9cRJv9zNuFOR3MsDz6TSDhB0xEo4",
          "crv": "P-256",
          "x5c": [
            "MIIDqjCCA1GgAwIBAgIGAZc6/V9qMAoGCCqGSM49BAMCMIGzMQsw...",
            "MIIDQzCCAuigAwIBAgIGAZc6+XlDMAoGCCqGSM49BAMCMIGzMQsw..."
          ]
        }

    Esempio JWK di Protocollo con catena di certificati estesa:

    .. code-block:: json

        {
          "kid": "ProtocolKeyId123",
          "kty": "EC",
          "x": "protocol_key_x_coordinate...",
          "y": "protocol_key_y_coordinate...",
          "crv": "P-256",
          "x5c": [
            "MIIDprotocolCert...",  // Cert protocollo (firmato da chiave federazione)
            "MIIDqjCCA1GgAwIBAgIGAZc6/V9qMAoGCCqGSM49BAMCMIGzMQsw...",  // Cert federazione
            "MIIDQzCCAuigAwIBAgIGAZc6+XlDMAoGCCqGSM49BAMCMIGzMQsw..."   // Cert radice
          ]
        }

  2. **Pubblicare Entity Configuration Aggiornata**: Pubblicare l'EC aggiornata all'endpoint ``/.well-known/openid-federation`` come specificato in :ref:`trust-infrastructure:L'Infrastruttura di Trust`.

  3. **Inviare Richiesta Resolve**: Chiamare l'endpoint ``/resolve`` del **Trust Anchor** (come definito in :ref:`trust-infrastructure:Requisiti dell'Infrastruttura di Trust`) con parametri URL-encoded:

    - ``sub``: Identificativo Entità di Federazione.
    - ``trust_anchor``: Identificativo Entità di Federazione del **Trust Anchor** (sempre il Trust Anchor radice, anche per onboarding mediato da Intermediario).

    Esempio richiesta resolve:

    .. code-block:: http

        GET /resolve?sub=https%3A%2F%2Fcredentials.example.gov&trust_anchor=https%3A%2F%2Ftrust-anchor.example.gov HTTP/1.1
        Host: trust-anchor.example.gov

**Fase 4: Risposta Resolve e Completamento Onboarding**

Dopo la resolve request, l'**Autorità di Federazione** esegue:

  - La **Ricostruzione della Catena di Trust**: Ricostruzione di una catena di trust valida per l'entità come definito in :ref:`trust-infrastructure:L'Infrastruttura di Trust`.
  - La **Generazione delTrust Mark di Federazione**: Generazione di un Trust Mark di Federazione IT-Wallet come attestazione JWT firmata dell'appartenenza alla federazione dell'entità e conformità ai requisiti tecnici IT-Wallet.
  - L'**Integrazione del Trust Mark nel Subordinate Statement**: Il Trust Mark generato è incluso nel Subordinate Statement dell'entità come definito in :ref:`trust-infrastructure:Subordinate Statement`.
  - L'**Applicazione di Metadata Policy**: Applicazione di metadata policy a cascata durante la costruzione della catena di trust, assicurando che le policy del Trust Anchor abbiano precedenza sulle policy degli Intermediari.
  - Generazione di un JSON Web Token (JWT) firmato utilizzando algoritmi specificati in :ref:`algorithms:Algoritmi Crittografici` contenente la catena di trust ricostruita e i metadati dell'entità validati.
  - Trasmissione di una HTTP response contenente il JWT creato (Resolve Response).

Se lo status code della responsr è 200 OK, l'Entità di Federazione DEVE completare il processo di onboarding, seguendo i seguenti step:

  - **Validare la Resolve Response**: Validare il JWT contenuto nella Resolve Response ed estrarre la catena di trust e i metadati validati dal payload JWT.
  - **Recuperare i Subordinate Statement**: Recuperare il proprio Subordinate Statement dall'Autorità di Federazione immediata utilizzando l'endpoint ``/fetch`` come definito in :ref:`trust-infrastructure:Endpoint API di Federazione`.
  - **Estrarre il Trust Mark**: Estrarre il Trust Mark di Federazione dal claim ``trust_marks`` del Subordinate Statement.
  - **Integrazione del Trust Mark**: Includere il Trust Mark estratto nella sua Entity Configuration utilizzando il claim ``trust_marks`` come specificato in :ref:`trust-infrastructure:Entity Configuration Foglie e intermediari`.
  - **Aggiornamento Finale Entity Configuration**: Pubblicare l'Entity Configuration aggiornata con il Trust Mark integrato all'endpoint ``/.well-known/openid-federation``.

Dopo il completamento con successo della Fase 4, **l'onboarding dell'entità è completato con successo**. L'entità è ora operativa all'interno della federazione IT-Wallet e pronta per le attività operative.

.. note::
   Se l'endpoint ``/resolve`` risponde con status code 400 o 404, l'entità deve risolvere i problemi descritti nel messaggio di risposta prima di chiamare nuovamente l'endpoint resolve.

.. note::
   **Integrazione del Registro di Federazione**: Dopo il completamento con successo dell'onboarding, l'Identificativo dell'Entità di Federazione diventa scopribile attraverso i meccanismi di elenco delle entità del Trust Anchor (come definito in :ref:`trust-infrastructure:L'Infrastruttura di Trust`), indicando la partecipazione attiva alla federazione. L'entità diventa parte dell'infrastruttura di federazione dettagliata in :ref:`registry:Infrastruttura del Registro`.

Trust Mark di Federazione IT-Wallet
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Le Entità di Federazione ricevono il Trust Mark di Federazione IT-Wallet durante il completamento con successo dell'onboarding. **I Trust Mark sono emessi dall'Autorità di Federazione** (Trust Anchor per onboarding diretto, Intermediario per onboarding mediato) e servono come attestazioni verificabili dell'appartenenza alla federazione, conformità ai requisiti tecnici IT-Wallet e politiche di autorizzazione per ambiti operativi specifici.

Tipi di Trust Mark e Schema
"""""""""""""""""""""""""""

Le entità POSSONO ricevere più Trust Mark per scopi diversi e tipi di entità, abilitando l'applicazione granulare delle politiche di autorizzazione. Gli identificativi dei Trust Mark DEVONO seguire uno schema gerarchico che riflette l'ambito di autorizzazione:

``https://<federation_authority_domain>/trust_marks/<purpose>/<entity_type>``

Dove:

  - ``<federation_authority_domain>``: Il dominio dell'Autorità di Federazione emittente.
  - ``<purpose>``: Lo scopo del Trust Mark. Lo scopo ``federation-entity`` è **OBBLIGATORIO** per tutte le entità. Scopi aggiuntivi di Trust Mark POSSONO essere supportati, come ``authorization_policy`` per definizioni granulari dell'ambito operativo.
  - ``<entity_type>``: Il tipo di entità destinataria (es., ``credential-issuer``, ``relying-party``, ``wallet-provider``).

Struttura Trust Mark
""""""""""""""""""""

I Trust Mark nell'Entity Configuration DEVONO essere rappresentati come oggetti JSON contenenti i seguenti claim:

.. list-table:: Trust Mark Object Claims (nell'Entity Configuration)
   :class: longtable
   :header-rows: 1
   :widths: 20 80

   * - **Claim**
     - **Descrizione**
   * - **trust_mark_type**
     - **OBBLIGATORIO**. Identificativo del tipo di Trust Mark in accordo allo schema: ``https://<federation_authority_domain>/trust_marks/<purpose>/<entity_type>``.
   * - **trust_mark**
     - **OBBLIGATORIO**. Un JSON Web Token firmato che rappresenta il Trust Mark emesso dall'Autorità di Federazione.

Il JWT del Trust Mark (contenuto nel claim ``trust_mark`` sopra) include i seguenti claim:

.. list-table:: Claim JWT Trust Mark
   :class: longtable
   :header-rows: 1
   :widths: 20 80

   * - **Claim**
     - **Descrizione**
   * - **iss**
     - **OBBLIGATORIO**. Autorità di Federazione che emette il Trust Mark (superiore immediato: Trust Anchor o Intermediario).
   * - **sub**
     - **OBBLIGATORIO**. Identificativo dell'Entità di Federazione del destinatario.
   * - **id**
     - **OBBLIGATORIO**. Identificativo unico del Trust Mark, DEVE corrispondere al claim ``trust_mark_type``.
   * - **iat**
     - **OBBLIGATORIO**. Timestamp di emissione del Trust Mark.
   * - **exp**
     - **OBBLIGATORIO**. Timestamp di scadenza del Trust Mark.
   * - **organization_type**
     - **OBBLIGATORIO**. Tipo di organizzazione dell'entità (``public`` o ``private``).
   * - **id_code**
     - **RACCOMANDATO**. Oggetto JSON con codici di identificazione (es., codice IPA per entità pubbliche, partita IVA).
   * - **organization_name**
     - **RACCOMANDATO**. Nome completo dell'Entità Organizzativa.
   * - **email**
     - **RACCOMANDATO**. Email istituzionale o PEC dell'organizzazione.
   * - **logo_uri**
     - **OPZIONALE**. URL che punta al logo del Trust Mark per scopi UI/UX.
   * - **ref**
     - **OPZIONALE**. URL con informazioni web aggiuntive sul Trust Mark.

I seguenti esempi non normativi illustrano diversi JWT di Trust Mark che attestano l'appartenenza alla federazione con differenti politiche di autorizzazione:

.. code-block:: json

   {
     "iss": "https://trust-anchor.eid-wallet.example.it",
     "sub": "https://ci.public-authority.gov.example",
     "id": "https://trust-anchor.eid-wallet.example.it/trust_marks/federation-entity/credential-issuer",
     "iat": 1718207217,
     "exp": 1749743216,
     "organization_type": "public",
     "id_code": {
       "ipa_code": "pub_001",
       "legal_identifier": "12345678901"
     },
     "organization_name": "Servizi Autorità Pubblica",
     "email": "registry@public-authority.gov.example"
   }

.. code-block:: json

   {
     "iss": "https://trust-anchor.eid-wallet.example.it",
     "sub": "https://rental.cars.example.com",
     "id": "https://trust-anchor.eid-wallet.example.it/trust_marks/authorization_policy/relying-party",
     "iat": 1718207217,
     "exp": 1749743216,
     "organization_type": "private",
     "id_code": {
       "vat_number": "IT12345678901",
       "legal_identifier": "12345678901"
     },
     "organization_name": "Premium Car Rental Services Ltd",
     "email": "compliance@rental.cars.example.com",
     "authorized_claims": ["given_name", "family_name", "driving_privileges"],
     "authorized_credential_types": ["mobile-driving-license"],
     "scope_restrictions": {
       "domains": ["AUTHORIZATION"],
       "purposes": ["DRIVING_LICENSE"]
     }
   }

.. code-block:: json

   {
     "iss": "https://trust-anchor.eid-wallet.example.it",
     "sub": "https://private-badge.ci.example.com",
     "id": "https://trust-anchor.eid-wallet.example.it/trust_marks/authorization_policy/credential-issuer",
     "iat": 1718207217,
     "exp": 1749743216,
     "organization_type": "private",
     "id_code": {
       "vat_number": "IT98765432101",
       "legal_identifier": "98765432101"
     },
     "organization_name": "Badge Services Ltd",
     "email": "compliance@rprivate-badge.ci.example.com",
     "authorized_claims": ["given_name", "family_name", "company_id"],
     "authorized_credential_types": ["example-company-badge"],
     "scope_restrictions": {
       "domains": ["MEMBERSHIP"],
       "purposes": ["ASSOCIATION"]
     }
   }

Le Entità di Federazione DEVONO integrare i Trust Mark nella loro Entity Configuration utilizzando il claim ``trust_marks`` come specificato in :ref:`trust-infrastructure:Entity Configuration Foglie e intermediari`. Le entità POSSONO ricevere più Trust Mark per diversi ambiti autorizzativi.

.. code-block:: json

   {
     "iss": "https://credentials.example.gov",
     "sub": "https://credentials.example.gov",
     "jwks": { 
      // jwks content
     },
     "authority_hints": ["https://trust-anchor.eid-wallet.example.it"],
     "trust_marks": [
       {
         "trust_mark_type": "https://trust-anchor.eid-wallet.example.it/trust_marks/federation-entity/credential-issuer",
         "trust_mark": "eyJhbGciOiJFUzI1NiIsImtpZCI6IlRydXN0QW5jaG9yS2V5SWQiLCJ0eXAiOiJKV1QifQ..."
       }
     ],
     "metadata": { 
      // Metadata content
     }
   }

.. code-block:: json

   {
     "iss": "https://healthcare-ci.example.gov",
     "sub": "https://healthcare-ci.example.gov",
     "jwks": { 
           // jwks content
     },
     "authority_hints": ["https://healthcare.intermediate.eid-wallet.example.it"],
     "trust_marks": [
       {
         "trust_mark_type": "https://healthcare.intermediate.eid-wallet.example.it/trust_marks/federation-entity/credential-issuer",
         "trust_mark": "eyJhbGciOiJFUzI1NiIsImtpZCI6IkhlYWx0aGNhcmVJbnRlcm1lZGlhdGVLZXlJZCIsInR5cCI6IkpXVCJ9..."
       }
     ],
     "metadata": { 
      // Metadata content
     }
   }

Validazione Trust Mark
""""""""""""""""""""""

I partecipanti alla federazione validano lo stato del Trust Mark attraverso due meccanismi:

1. **Validazione Statica**: Verifica crittografica utilizzando la chiave pubblica dell'Autorità di Federazione emittente dalla catena di trust.
2. **Validazione Dinamica**: Verifica dello stato in tempo reale tramite l'endpoint ``/trust_mark_status`` dell'Autorità di Federazione emittente come definito in :ref:`trust-infrastructure:Endpoint API di Federazione`.

Per le procedure complete di gestione dei certificati X.509, inclusa la validazione delle catene, la verifica della revoca e la gestione del ciclo di vita, vedere :ref:`x5c-evaluation:Operazioni di Gestione dei Certificati X.509`.

.. include:: ../common/common_definitions.rst
.. include:: ../common/symbols.rst



L'Infrastruttura di Trust
==========================

L'ecosistema IT-Wallet opera all'interno di un'infrastruttura di trust federata dove le entità partecipanti stabiliscono relazioni di trust crittografiche e mantengono la conformità con standard di sicurezza comuni. Questa infrastruttura fornisce le fondamenta per operazioni sicure di Credenziali Elettroniche tra i partecipanti dell'ecosistema.

Questa sezione definisce l'implementazione del Trust Model in un'infrastruttura che è conforme all'`EIDAS-ARF`_ e a OpenID Federation 1.0 `OID-FED`_. OpenID Federation opera a livello nazionale ed è completata dalle eIDAS Trusted Lists per QEAA ed EAA Provider, come dettagliato in :ref:`trust-infrastructure:trusted-lists-eaa-provider-profilo-implementazione`. La List of Trusted Lists (LoTL), mantenuta dalla Commissione Europea, aggrega i puntatori a tutte le eIDAS Trusted Lists pubblicate, abilitando l'instaurazione del trust transfrontaliero e la scoperta centralizzata delle posizioni delle Trusted Lists e delle relative chiavi di firma.

L'infrastruttura nazionale fornisce un'API RESTful per distribuire metadati, policy dei metadati, trust mark, chiavi pubbliche crittografiche e certificati X.509, e lo stato di revoca dei partecipanti, denominati anche Entità di Federazione.

L'Infrastruttura di trust facilita l'applicazione di un meccanismo di valutazione del trust tra le parti definite nell'`EIDAS-ARF`_.

Questa infrastruttura di trust lavora in coordinamento con l'Infrastruttura del Registro (vedi :ref:`registry:Infrastruttura del Registro`) per abilitare i processi di onboarding delle entità dettagliati in :ref:`entity-onboarding:Onboarding delle Entità`. In particolare, abilita l'implementazione tecnica dei processi di onboarding descritti in :ref:`entity-onboarding:Onboarding delle Entità` e supporta gli scenari operativi illustrati in :ref:`onboarding-high-level:Onboarding Journey Maps`.

**Abilitazione dell'Onboarding**: L'Infrastruttura di Trust fornisce i meccanismi crittografici che consentono alle nuove entità (Credential Issuer, Relying Party, Fornitori di Wallet) di stabilire relazioni di trust verificabili durante il loro processo di registrazione. Senza questa infrastruttura, le entità non sarebbero in grado di dimostrare il loro stato di conformità o le capacità operative agli altri partecipanti dell'ecosistema.

**Supporto al Ciclo di Vita delle Entità**: Durante tutto il ciclo di vita operativo di un'entità, l'Infrastruttura di Trust mantiene attestazioni di trust aggiornate, gestisce la rotazione delle chiavi, gestisce scenari di revoca e supporta il monitoraggio della conformità. Questo supporta direttamente le procedure di gestione del ciclo di vita dettagliate in :ref:`entity-onboarding:Onboarding delle Entità`.

**Integrazione con l'Infrastruttura del Registro**: L'Infrastruttura di Trust implementa il componente Federation Registry dell'Infrastruttura del Registro più ampia, fornendo le fondamenta tecniche per la scoperta delle entità e la validazione del trust che sottende tutte le procedure di onboarding.

.. plantuml:: plantuml/trust-roles.puml
   :width: 99%
   :alt: La figura illustra i ruoli di trust.
   :caption: `I ruoli all'interno della Federazione, dove il National Trust Anchor supervisiona i suoi subordinati, che includono uno o più Intermediari e Foglie. <https://www.plantuml.com/plantuml/png/XT1HQy90303Wz_iLcNkMiIAoXo5AtK3OWup17aViPUxmcYkvd29Z_tsjThM2kBSc-P9UCesAegdqviPnuPCbUCn7T_de8m-iw9XaOapSEAvGi8GL5fkrXCGs3pu8g237kaIiFJKJ2RiZMFcwmnYXGf7Ndc3m9YagpBZu2Z80ZA08j_FnqyDpTkOMh2GbMOTA1-TOxplv3ymkZdmXt58y64_u6UjnZPcFhw6iGzTKTwu_3Ty6eDUG2rbYTUXX4MEYu-w5wnvwfj_HUr9OIjWwszfTTTc-ajyxNiCIHVS7AIVvOqpzZs6gXXDGDBkg_MwEQQGNPQOzIQ_UxjypJVeqhKcTeYcnJQN_1G00>`_

In questa rappresentazione, sia il :term:`National Trust Anchor` che gli Intermediari assumono il ruolo di Registration Authority.

Ruoli di Federazione
--------------------

Tutti i partecipanti sono Entità di Federazione che DEVONO essere registrate da un Registration Body, eccetto le Istanze del Wallet che sono dispositivi personali dell'Utente finale autenticati dal loro Fornitore di Wallet.

.. note::
  L'Istanza del Wallet, come dispositivo personale, è considerata affidabile attraverso un'attestazione verificabile rilasciata e firmata da una terza parte fidata.

  Questo è chiamato *Wallet Attestation* ed è documentato nella sezione dedicata :ref:`wallet-attestation-issuance:Emissione della Wallet App e Wallet Unit Attestation`.

**Ruolo nell'Onboarding**: Durante la registrazione delle entità, il Trust Anchor e gli Intermediari agiscono come Autorità di Federazione. Ciò stabilisce la posizione del partecipante nella gerarchia di trust e consente di partecipare alle operazioni sulle credenziali. Le Foglie (Credential Issuer, Relying Party, Fornitori di Wallet) completano la registrazione per dimostrare l'idoneità e ricevere l'autorizzazione a svolgere le funzioni designate.

**Ruolo nelle Operazioni**: Durante l'emissione e la presentazione delle credenziali, questi ruoli consentono la validazione distribuita del trust senza richiedere una verifica centralizzata per ogni transazione. Le Foglie utilizzano il proprio stato registrato per emettere credenziali, verificare presentazioni o fornire servizi di wallet agli utenti finali.

Di seguito la tabella riassuntiva dei ruoli delle Entità di Federazione, mappati sui corrispondenti ruoli EUDI Wallet definiti nell'`EIDAS-ARF`_.

.. list-table::
   :class: longtable
   :widths: 20 20 60
   :header-rows: 1

   * - Ruolo EUDI
     - Ruolo di Federazione
     - Note
   * - Public Key Infrastructure (PKI)
     - :term:`National Trust Anchor`
     - La Federazione ha capacità PKI e utilizza OpenID Federation 1.0 `OID-FED`_. L'Entità che configura l'intera infrastruttura a livello nazionale è il :term:`National Trust Anchor`.
   * - Qualified Trust Service Provider (QTSP)
     - Leaf
     -
   * - Fornitore di Attestati Elettronici di Dati di Identificazione Personale
     - Leaf
     -
   * - Fornitore di Attestati Elettronici di Attributi Qualificati
     - Leaf
     -
   * - Fornitore di Attestati Elettronici di Attributi
     - Leaf
     -
   * - Relying Party
     - Leaf
     -
   * - Trust Service Provider (TSP)
     - Leaf
     -
   * - Fornitore di Wallet
     - Leaf
     -
   * - eIDAS Trusted List Provider
     - eIDAS Trust Anchor
     - Compila, firma e pubblica le eIDAS Trusted Lists a livello UE per QTSP, Fornitori di Wallet, PID Provider, Access CA e Fornitori di Certificati di Registrazione, come descritto nello schema dell'infrastruttura di trust dell'EUDI Wallet.
   * - National eIDAS Trusted List Provider
     - :term:`National Trust Anchor`
     - Compila, firma e pubblica le Trusted Lists nazionali per i QEAA Provider e per gli EAA Provider non qualificati secondo il quadro nazionale dei servizi fiduciari, come descritto in questo documento per la pubblicazione delle Trusted Lists degli EAA Provider e dei QEAA Provider.

.. _trust-infrastructure-trust-registry-integration:
.. _trust-infrastructure-integrazione-tra-infrastruttura-di-trust-e-registry:

Integrazione dell'Infrastruttura di Trust e del Registro
--------------------------------------------------------

L'Infrastruttura di Trust implementa il componente Federation Registry dell'Infrastruttura del Registro. Il Federation Registry mantiene l'elenco autorevole delle entità fidate attraverso gli endpoint di federazione definiti in questa sezione, inclusi l'elenco delle entità (/list), le dichiarazioni dei subordinati (/fetch), la validazione dei trust mark (/trust_mark_status), gli eventi sui subordinati (/federation_subordinate_events_endpoint) e la gestione delle chiavi storiche (/historical-jwks).

Questo Federation Registry opera insieme ad altri componenti del registro (Claims Registry, AS Registry, Catalogo degli Attestati Elettronici, Taxonomy) per fornire supporto completo all'ecosistema. Per l'architettura completa del registro e le interazioni dei componenti, vedi :ref:`registry:Infrastruttura del Registro`.

Proprietà Generali
-------------------

L'architettura dell'infrastruttura di trust si basa sui seguenti principi fondamentali:

.. list-table::
   :class: longtable
   :widths: 20 20 80
   :header-rows: 1

   * - Identificatore
     - Proprietà
     - Descrizione
   * - P1
     - **Sicurezza**
     - Incorpora meccanismi per garantire integrità, riservatezza e autenticità delle Trust Relationship e delle interazioni nella federazione.
   * - P2
     - **Privacy**
     - Progettata per rispettare e proteggere la privacy delle entità coinvolte; la divulgazione minima ne fa parte.
   * - P3
     - **Interoperabilità**
     - Supporta l'interazione fluida e l'istituzione del trust tra sistemi ed entità diversi nella federazione.
   * - P4
     - **Trust transitivo**
     - Trust instaurato indirettamente attraverso una catena di relazioni fidate, che consente alle entità di fidarsi sulla base di autorità comuni e intermediari fidati.
   * - P5
     - **Delega**
     - Capacità o funzionalità tecnica di delegare autorità o responsabilità ad altre entità, consentendo un meccanismo di trust distribuito.
   * - P6
     - **Scalabilità**
     - Progettata per gestire in modo efficiente un numero crescente di entità o interazioni senza un aumento significativo della complessità della gestione del trust.
   * - P7
     - **Flessibilità**
     - Adattabile a esigenze operative e organizzative diverse, consentendo alle entità di definire e adeguare le Trust Relationship e le policy.
   * - P8
     - **Autonomia**
     - Pur facendo parte di un ecosistema federato, ogni entità mantiene il controllo sulle proprie definizioni e configurazioni.
   * - P9
     - **Decentralizzazione**
     - A differenza dei sistemi centralizzati tradizionali, l'infrastruttura di trust consente un approccio decentralizzato.

Requisiti dell'Infrastruttura di Trust
--------------------------------------

Questa sezione include i requisiti necessari per l'implementazione e il funzionamento dell'infrastruttura di trust.

.. list-table:: Requisiti funzionali
   :class: longtable
   :widths: 20 80
   :header-rows: 1

   * - ID
     - Descrizione
   * - FR1
     - **Istituzione del trust di federazione**: il sistema deve poter instaurare il trust tra entità diverse (Credential Issuer, Relying Party, ecc.) in una federazione, usando firme crittografiche per lo scambio sicuro di informazioni sui partecipanti dell'ecosistema.
   * - FR2
     - **Autenticazione delle entità**: il sistema deve implementare meccanismi di autenticazione delle entità nella federazione, garantendo la conformità alle regole condivise.
   * - FR3
     - **Validazione delle firme**: il sistema deve supportare creazione, verifica e validazione di firme elettroniche e fornire meccanismi standard e sicuri per ottenere le chiavi pubbliche crittografiche necessarie alla validazione delle firme.
   * - FR4
     - **Marcatura temporale**: gli artefatti firmati devono contenere marcature temporali per garantire integrità e non ripudio delle transazioni nel tempo, tramite le interfacce, i servizi, il modello di storage e gli approcci definiti nella federazione.
   * - FR5
     - **Validazione dei certificati**: il sistema richiede trasmissione riservata, protetta tramite TLS su HTTP, e validazione dei certificati per l'autenticazione dei siti web.
   * - FR6
     - **Interoperabilità e conformità agli standard**: garantire l'interoperabilità tra i membri della federazione rispettando standard tecnici, facilitando le transazioni elettroniche transfrontaliere.
   * - FR7
     - **Protezione dei dati e privacy**: implementare misure di protezione dei dati conformi al GDPR, garantendo privacy e sicurezza dei dati personali trattati nella federazione.
   * - FR8
     - **Risoluzione delle controversie e responsabilità**: stabilire procedure chiare per la risoluzione delle controversie e definire la responsabilità tra i membri della federazione.
   * - FR9
     - **Servizi di emergenza e revoca**: implementare meccanismi per la revoca immediata dei partecipanti in caso di incidenti di sicurezza o altre emergenze.
   * - FR10
     - **Infrastruttura di trust scalabile**: il sistema deve supportare meccanismi scalabili di instaurazione del trust, sfruttando approcci e soluzioni tecniche che integrano approcci di delega transitiva per gestire in modo efficiente le Trust Relationship con la crescita della federazione, riducendo registri centrali che possano fallire tecnicamente o amministrativamente.
   * - FR11
     - **Scalabilità di storage efficiente**: implementare una soluzione di storage che scala orizzontalmente per volumi crescenti riducendo storage centrale e costi amministrativi. I membri devono poter conservare e presentare in modo indipendente attestazioni di trust storiche e artefatti firmati nelle controversie, mentre l'infrastruttura di federazione mantiene solo un registro di chiavi storiche per validare i dati storici conservati e forniti dai partecipanti.
   * - FR12
     - **Attestazione verificabile (Trust Mark)**: incorporare un meccanismo per emettere e verificare attestazioni verificabili come prova di conformità a profili o standard specifici, consentendo alle entità di dimostrare aderenza a standard di sicurezza, privacy e operativi concordati.
   * - FR13
     - **Meccanismo decentralizzato di risoluzione delle controversie**: progettare un meccanismo decentralizzato che consenta ai membri di verificare in modo indipendente l'istituzione storica del trust e gli artefatti firmati, riducendo la dipendenza da autorità centrali.
   * - FR14
     - **Interoperabilità tra federazioni**: garantire la capacità di interoperare con altre federazioni o Trust Framework, facilitando transazioni e instaurazione del trust tra federazioni senza compromettere sicurezza o conformità.
   * - FR15
     - **Organismi di registrazione autonomi**: il sistema deve facilitare l'integrazione di organismi di registrazione autonomi che operano secondo le regole della federazione, incaricati di valutare e registrare le entità secondo regole predefinite e conformità da rivalutare periodicamente.
   * - FR16
     - **Verifica periodica di organismi ed entità registrate**: implementare meccanismi di verifica e monitoraggio periodico dello stato di conformità degli organismi di registrazione e delle entità da essi registrate.
   * - FR17
     - **Attestazione di conformità per dispositivi personali**: organismi fidati, come entità di federazione, dovrebbero emettere attestazioni di conformità e prove firmate per l'hardware dei dispositivi personali usati nella federazione; tali attestazioni vanno attestate e rinnovate periodicamente per garantire standard di sicurezza attuali.
   * - FR18
     - **Monitoraggio automatizzato della conformità**: il sistema dovrebbe includere strumenti automatizzati per monitorare la conformità delle entità agli standard della federazione, favorendo la rilevazione precoce di problemi di conformità.
   * - FR19
     - **Binding delle capacità del protocollo sicuro**: il protocollo sicuro deve consentire lo scambio di dati sulle capacità specifiche del protocollo come metadati legati crittograficamente a un'identità; tali metadati definiscono le capacità tecniche associate all'identità, con prova verificabile e associazione anti-manomissione per un'istituzione robusta del trust e il controllo degli accessi.

Schema dell'Infrastruttura di Trust: Onboarding e Trusted Lists
-----------------------------------------------------------------

L'infrastruttura di trust si basa su cinque processi distinti ma complementari:

1. **Registrazione/Onboarding**: Le entità (PID Provider, QEAA Provider, EAA Provider, Relying Party, Wallet Provider) si registrano con il Registrar nazionale o tramite il sistema di onboarding dell'IT-Wallet per definire l'autorizzazione operativa e i diritti.
2. **Notifica**: Lo Stato Membro notifica alla Commissione Europea, in qualità di operatore dell'eIDAS Trusted List Provider a livello UE, i **PID Provider**, i **PuB-EAA Provider**, i **Wallet Provider**, le **Autorità Certificatrici di Accesso (Access CA)** e i **Fornitori di Certificati di Registrazione** per l'inclusione nelle relative Trusted Lists.
3. **Pubblicazione di Cataloghi e Liste Nazionali**: Pubblicazione di cataloghi e liste nazionali relative alle entità registrate tramite endpoint RESTful.
4. **Pubblicazione delle eIDAS Trusted Lists**: Pubblicazione delle eIDAS Trusted Lists a livello UE da parte della Commissione Europea, basata sulle notifiche dello Stato Membro per Wallet Provider, PID Provider, PuB-EAA Provider, Access CA e Fornitori di Certificati di Registrazione.
5. **Pubblicazione delle Trusted Lists Nazionali**: Pubblicazione delle Trusted Lists nazionali per i QEAA Provider e per gli EAA Provider non qualificati da parte del Fornitore di Trusted Lists dello Stato Membro (MS TLP), basata sui dati del Registrar nazionale.

.. _trust-infrastructure:trusted-lists-eaa-provider-profilo-implementazione:

Trusted Lists per EAA Provider: Profilo di Implementazione
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Questa sezione fornisce il profilo di implementazione per le Trusted Lists nazionali, compilate e pubblicate dal Fornitore di Trusted Lists dello Stato Membro (MS TLP), sia per i Fornitori di Attestazioni Elettroniche di Attributi Qualificati (QEAA Provider) che per i Fornitori di Attestazioni Elettroniche di Attributi non qualificati (EAA Provider), come richiesto dall'infrastruttura di trust dell'EUDI Wallet.

Requisiti Normativi e Motivazioni
"""""""""""""""""""""""""""""""""

Il requisito per le Trusted Lists degli EAA Provider è stabilito dal quadro dei servizi fiduciari e dalle specifiche tecniche ETSI:

- **`ETSI TS 119 612`_**: definisce il formato Trusted Service Lists (TSL) basato su XML per le trusted lists, inclusi i tipi di servizio e la gestione dello stato. Questo profilo continua a essere utilizzato per le **Trusted Lists QTSP**, inclusi i **QEAA Provider**.
- **`ETSI TS 119 602`_** e il relativo Allegato H: definiscono il modello di dati astratto e il profilo per le Liste di Entità Fidate (LoTE), incluse le **Trusted Lists degli Attestation Provider per gli EAA Provider non qualificati e, ove applicabile, per i PuB‑EAA Provider**. I QEAA Provider rimangono invece nelle Trusted Lists QTSP secondo `ETSI TS 119 612`_, mentre l'Allegato H viene utilizzato per le Trusted Lists nazionali degli EAA Provider con binding JSON e XML.

Profilo di Implementazione per le Trusted Lists dei QEAA Provider
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

I **QEAA Provider** sono Fornitori di Servizi Fiduciari Qualificati (QTSP) ai sensi del `EIDAS`_. Dopo la registrazione riuscita con un Registrar dello Stato Membro, i QEAA Provider sono inclusi nelle **Trusted Lists QTSP degli Stati Membri**, che sono:

- **Compilate e Pubblicate Da**: Fornitore di Trusted Lists dello Stato Membro (MS TLP)
- **Base Legale**: `EIDAS`_ Articolo 22 e Decisione di Implementazione della Commissione (UE) 2015/1505
- **Notifica**: Gli Stati Membri notificano queste Trusted Lists QTSP alla Commissione Europea ai sensi dell'`EIDAS`_ Articolo 22(3) in modo che le posizioni delle TL QTSP e le chiavi di firma possano essere esposte tramite la **Lista delle Trusted Lists (LoTL)**
- **Formato**: DEVE essere conforme alle specifiche `ETSI TS 119 612`_ (formato XML) - **OBBLIGATORIO** secondo la Decisione di Implementazione della Commissione (UE) 2015/1505
- **Firma**: XAdES Baseline B (formato firma avvolta) - **OBBLIGATORIA** secondo `ETSI TS 119 612`_ e `ETSI EN 319 132-1`_

.. note::
  Il requisito del formato XML per le Trusted Lists QTSP (inclusi i QEAA Provider) è obbligatorio secondo la Decisione di Implementazione della Commissione (UE) 2015/1505, che stabilisce le specifiche tecniche per le Trusted Lists ai sensi dell'`EIDAS`_ Articolo 22(5). Questa decisione richiede agli Stati Membri di pubblicare le Trusted Lists QTSP in formato XML secondo `ETSI TS 119 612`_ con firme XAdES Baseline B.


Di seguito è riportato un esempio non normativo di una voce relativa a un QEAA Provider all'interno di una Trusted List QTSP di uno Stato Membro, seguendo il formato XML `ETSI TS 119 612`_ (solo payload, senza firma XAdES):

.. literalinclude:: ../../examples/qeaa-provider-trusted-list-example.xml
   :language: xml
   :caption: Esempio non normativo di una voce relativa a un QEAA Provider in una Trusted List QTSP di uno Stato Membro (formato XML, `ETSI TS 119 612`_ solo payload, senza firma)

Profilo di Implementazione per le Trusted Lists degli EAA Provider Non Qualificati
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Gli **EAA Provider non qualificati** sono inclusi nelle **Trusted Lists nazionali degli EAA Provider**, che rappresentano un'estensione nazionale complementare alle Trusted Lists QTSP:

- **Compilate e Pubblicate Da**: Fornitore di Trusted Lists dello Stato Membro (MS TLP)
- **Base Legale**: Estensione nazionale decisa dallo Stato Membro
- **Notifica**: Gli Stati Membri inviano gli URL delle Trusted Lists degli EAA Provider non qualificati alla Commissione Europea per l'inclusione nella LoTL
- **Formato**: Può utilizzare il profilo `ETSI TS 119 602`_ Allegato H (Trusted Lists degli Attestation Provider), pubblicato in formato JSON con firma compact JAdES Baseline B OPPURE formato XML con firma XAdES Baseline B (per `ETSI EN 319 132-1`_). Quando viene utilizzato XML, deve essere una firma digitale avvolta.
- **Firma**: Compact JAdES Baseline B (JSON) o XAdES Baseline B (XML) secondo `ETSI TS 119 182-1`_ o `ETSI EN 319 132-1`_

**Requisiti di Firma**:

Le Trusted Lists in formato JSON DEVONO essere firmate utilizzando firme compact JAdES Baseline B come richiesto da `ETSI TS 119 182-1`_. Le Trusted Lists in formato XML DEVONO essere firmate utilizzando firme XAdES Baseline B come richiesto da `ETSI EN 319 132-1`_. La firma garantisce l'integrità, l'autenticità e il non-ripudio del contenuto della Trusted List.

Requisiti ETSI per le Trusted Lists degli EAA Provider
""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Requisiti del Profilo `ETSI TS 119 602`_ Allegato H** (per TL degli EAA Provider non qualificati):

- **Tipo LoTE**: URI appropriato per le Trusted Lists degli Attestation Provider
- **Tipi di Servizio**: 
  - URI del tipo di servizio di emissione
  - URI del tipo di servizio di revoca (se applicabile)
- **Stato del Servizio**: Il componente ServiceStatus **deve** essere presente per i PuB-EAA Provider; per gli EAA Provider non qualificati, la gestione dello stato segue la politica dello Stato Membro
- **Tempo di Inizio dello Stato**: Il componente StatusStartingTime **deve** essere presente quando viene utilizzato ServiceStatus
- **Informazioni Storiche**: HistoricalInformationPeriod **deve** essere presente con un valore appropriato quando viene mantenuta la cronologia del servizio
- **Prossimo Aggiornamento**: Massimo 6 mesi tra gli aggiornamenti
- **Firma**: Compact JAdES Baseline B (JSON) o XAdES Baseline B (XML) - **OBBLIGATORIA** secondo i requisiti ETSI

Di seguito è riportato un esempio non normativo del payload di una Trusted List di EAA Provider non qualificato (senza firma) seguendo il profilo `ETSI TS 119 602`_ Allegato H in formato JSON:

.. literalinclude:: ../../examples/eaa-provider-trusted-list-example.json
   :language: json
   :caption: Esempio non normativo del payload di una Trusted List di EAA Provider non qualificato (formato JSON, profilo `ETSI TS 119 602`_ Allegato H, solo payload, senza firma)

**Requisiti `ETSI TS 119 612`_** (per TL QTSP inclusi QEAA Provider):

- **Tipo TSL**: `http://uri.etsi.org/TrstSvc/TrustedList/TSLType/EUgeneric` o tipo TSL appropriato dello Stato Membro
- **Identificatori del Tipo di Servizio**: URI del tipo di servizio appropriati per i servizi QEAA
- **Stato del Servizio**: Valori di stato del servizio eIDAS standard
- **Firma**: XAdES Baseline B (formato firma avvolta)

Integrazione con la Lista delle Trusted Lists (LoTL)
"""""""""""""""""""""""""""""""""""""""""""""""""""""

Per la clausola D.5 di `ETSI TS 119 612`_, la Commissione Europea mantiene una Lista delle Trusted Lists (LoTL) che:

- Contiene puntatori (TrustedListPointers) a tutte le Trusted Lists pubblicate
- Ogni puntatore include la posizione della Trusted List (TSLLocation), il territorio dello schema e il nome dell'operatore dello schema
- Facilita l'istituzione di trust transfrontaliera
- Centralizza la distribuzione delle trusted lists
- Supporta la discovery dei servizi a livello di federazione

La Commissione Europea:

- Compila la LoTL da:
  - Le Trusted Lists direttamente compilate e pubblicate (TL Wallet Provider, TL PID Provider, TL Access CA, TL Fornitore Cert. Reg.)
  - Le notifiche degli URL delle Trusted Lists ricevute dai MS TLP (per EAA Provider qualificati e non qualificati)
- Firma/sigilla la LoTL utilizzando la chiave di firma della Commissione
- Pubblica la LoTL in formati leggibili da macchina e da uomo
- Pubblica la posizione della LoTL e gli anchor di trust nella Gazzetta Ufficiale dell'Unione Europea (GUUE)

.. _trust-infrastructure-endpoint-delle-api-della-federazione:

Endpoint API di Federazione
---------------------------

OpenID Federation 1.0 utilizza servizi web RESTful protetti su HTTPS. OpenID Federation 1.0 definisce quali endpoint web i partecipanti DEVONO rendere pubblicamente disponibili. La tabella seguente riassume gli endpoint e i relativi ambiti.

Tutti gli endpoint elencati di seguito sono definiti nelle specifiche `OID-FED`_.

.. list-table::
   :class: longtable
   :widths: 20 20 20 20
   :header-rows: 1

   * - nome endpoint
     - richiesta http
     - ambito
     - richiesto per
   * - federation metadata
     - **GET** .well-known/openid-federation
     - Metadati che un'entità pubblica su se stessa, verificabili con una terza parte fidata (entità superiore). È l'Entity Configuration.
     - Trust Anchor, Intermediario, Fornitore di Wallet, Relying Party, Credential Issuer
   * - subordinate list endpoint
     - **GET** /list
     - Elenca i subordinati. Vedi `OID-FED`_ sezione 8.2
     - Trust Anchor, Intermediario
   * - fetch endpoint
     - **GET** /federation_fetch_endpoint?sub=https://rp.example.org
     - Restituisce un JWT firmato su un soggetto specifico, il subordinato (Subordinate Statement). Vedi `OID-FED`_ sezione 8.1
     - Trust Anchor, Intermediario
   * - trust mark status
     - **POST** /federation_trust_mark_status_endpoint
     - Restituisce lo stato di emissione (validità) di un Trust Mark relativo a un soggetto specifico. Vedi `OID-FED`_ sezione 8.4
     - Trust Anchor, Intermediario
   * - trust marked listing
     - **GET** /trust_marked_list?trust_mark_type=...
     - Elenca tutte le entità per cui sono stati emessi Trust Mark ancora validi. Vedi `OID-FED`_ sezione 8.5
     - Trust Anchor, Intermediario
   * - historical keys
     - **GET** /federation_historical_keys
     - Elenca le chiavi scadute e revocate, con la motivazione della revoca. Vedi `OID-FED`_ sezione 8.7
     - Trust Anchor, Intermediario
   * - subordinate events
     - **GET** /federation_subordinate_events_endpoint?sub=https://rp.example.org
     - Restituisce la cronologia degli eventi di registrazione sui subordinati immediati (registrazione, revoca, aggiornamenti delle chiavi dell'entità di federazione). Vedi la sezione :ref:`trust-infrastructure:Federation Subordinate Events Endpoint`.
     - Trust Anchor, Intermediario


Tutte le risposte degli endpoint di federazione sono in forma di JWT firmato, salvo l'endpoint di elenco subordinati e l'endpoint di stato dei Trust Mark, serviti per impostazione predefinita come JSON semplice. L'endpoint Federation Subordinate Events restituisce inoltre JWT firmati con content type ``application/entity-events-statement+jwt``.

Endpoint delle Trusted Lists nazionali
--------------------------------------

Oltre agli endpoint di OpenID Federation, l'ecosistema IT-Wallet espone punti di distribuzione HTTPS per le eIDAS Trusted Lists e per le Trusted Lists nazionali degli EAA Provider. Questi endpoint sono gestiti dal Fornitore di Trusted Lists dello Stato Membro (MS TLP) e pubblicano le Trusted Lists autorevoli e firmate referenziate dalla LoTL e consumate da Wallet Unit, Credential Issuer e Relying Party.

- La Trusted List per i QEAA Provider DEVE essere pubblicata dal :term:`National Trust Anchor` come documenti TSL XML conformi a `ETSI TS 119 612`_ in posizioni HTTPS sotto il FQDN del National Trust Anchor (ad esempio ``https://<FQDNNationalTrustAnchor>/tsl/qeaa-tsl.xml``), con firma XAdES Baseline B secondo `ETSI EN 319 132-1`_.
- La Trusted List nazionale degli EAA Provider (per EAA Provider non qualificati e, ove applicabile, PuB-EAA Provider) DEVE essere pubblicata come documenti LoTE secondo `ETSI TS 119 602`_ Allegato H in posizioni HTTPS sotto il FQDN del National Trust Anchor (ad esempio ``https://<FQDNNationalTrustAnchor>/lote/eaa-providers.json``), in JSON (preferito) o XML, con firma compact JAdES Baseline B o XAdES Baseline B secondo `ETSI TS 119 182-1`_ e `ETSI EN 319 132-1`_.

I client dell'ecosistema EUDI Wallet consumano questi endpoint scaricando periodicamente le liste, validando le firme digitali e applicando le semantiche di stato del servizio e di sequenza definite in `ETSI TS 119 612`_ e `ETSI TS 119 602`_ per costruire e aggiornare i trust store locali.

Configurazione della Federazione
--------------------------------

La configurazione della federazione è pubblicata dal Trust Anchor all'interno della sua Entity Configuration, è disponibile nel path web well-known corrispondente a **.well-known/openid-federation**.

Tutti i partecipanti nella federazione DEVONO ottenere la configurazione di federazione prima di entrare nella fase operativa, e DEVONO mantenerla aggiornata. La configurazione di federazione è l'Entity Configuration del Trust Anchor, contiene le chiavi pubbliche per le operazioni di firma.

Di seguito è riportato un esempio non normativo di un'Entity Configuration del Trust Anchor, dove ogni parametro è documentato nella specifica `OpenID Federation <OID-FED>`_:

.. code-block:: json

    {
        "alg": "ES256",
        "kid": "FifYx03bnosD8m6gYQIfNHNP9cM_Sam9Tc5nLloIIrc",
        "typ": "entity-statement+jwt"
    }

.. code-block:: json

      {
        "exp": 1649375259,
        "iat": 1649373279,
        "iss": "https://trust-anchor.eid-wallet.example.it",
        "sub": "https://trust-anchor.eid-wallet.example.it",
        "jwks": {
            "keys": [
                {

                    "kty": "EC",
                    "kid": "X2ZOMHNGSDc4ZlBrcXhMT3MzRmRZOG9Jd3o2QjZDam51cUhhUFRuOWd0WQ",
                    "crv": "P-256",
                    "x": "1kNR9Ar3MzMokYTY8BRvRIue85NIXrYX4XD3K4JW7vI",
                    "y": "slT14644zbYXYF-xmw7aPdlbMuw3T1URwI4nafMtKrY",
                    "x5c": [
                      // <self-issued X.509 certificate about the Trust Anchor>
                      ]
                }
            ]
        },
        "metadata": {
            "federation_entity": {
                "organization_name": "example TA",
                "contacts":[
                    "tech@eid.trust-anchor.example.eu"
                ],
                "homepage_uri": "https://trust-anchor.eid-wallet.example.it",
                "logo_uri":"https://trust-anchor.eid-wallet.example.it/static/svg/logo.svg",
                "federation_fetch_endpoint": "https://trust-anchor.eid-wallet.example.it/fetch",
                "federation_resolve_endpoint": "https://trust-anchor.eid-wallet.example.it/resolve",
                "federation_list_endpoint": "https://trust-anchor.eid-wallet.example.it/list",
                "federation_trust_mark_status_endpoint": "https://trust-anchor.eid-wallet.example.it/trust_mark_status",
                "federation_trust_mark_listing_endpoint": "https://trust-anchor.eid-wallet.example.it/trust_mark_listing",
                "federation_subordinate_events_endpoint": "https://trust-anchor.eid-wallet.example.it/events"
            }
        },
        "trust_mark_issuers": {
            "https://trust-anchor.eid-wallet.example.it/openid_relying_party/public": [
                "https://trust-anchor.eid-wallet.example.it",
                "https://public.intermediary.other.org"
            ],
            "https://trust-anchor.eid-wallet.example.it/openid_relying_party/private": [
                "https://private.other.intermediary.org"
            ]
        }
    }


Entity Configuration
--------------------

L'Entity Configuration è il documento verificabile che ogni Entità di Federazione DEVE pubblicare per proprio conto, nell'endpoint **.well-known/openid-federation**.

La Risposta HTTP dell'Entity Configuration DEVE impostare il tipo di media su `application/entity-statement+jwt`.

L'Entity Configuration DEVE essere firmata crittograficamente. La parte pubblica di questa chiave DEVE essere fornita nell'Entity Configuration e all'interno del Subordinate Statement emesso da un superiore immediato e relativo alla sua Entità di Federazione subordinata.

L'Entity Configuration PUÒ anche contenere uno o più Trust Mark.

**Ruolo nell'Onboarding**: Le nuove entità pubblicano la loro Entity Configuration come parte del loro processo di registrazione, dichiarando le loro capacità, protocolli supportati e stato di conformità alla federazione. La configurazione serve come dichiarazione iniziale dell'entità della sua prontezza tecnica e ambito operativo, consentendo ad altri partecipanti di scoprire e validare il suo stato di registrazione.

**Ruolo nelle Operazioni**: Durante le operazioni di credenziali, le Entity Configuration sono recuperate da wallet, credential issuer e relying party per verificare lo stato operativo corrente, le capacità supportate e le attestazioni di conformità di altre entità. Questo abilita la scoperta dinamica degli endpoint di servizio, delle chiavi crittografiche e delle versioni di protocollo richieste per lo scambio sicuro di credenziali.

I dettagli tecnici sull'Entity Configuration del Fornitore di Wallet, Credential Issuer e Relying Party sono forniti rispettivamente nelle Sezioni :ref:`wallet-provider-entity-configuration:Entity Configuration del Fornitore di Wallet`, :ref:`credential-issuer-entity-configuration:Entity Configuration del Fornitore di Attestati Elettronici` e :ref:`relying-party-entity-configuration:Entity Configuration di una Relying Party`.

.. note::
  **Firma dell'Entity Configuration**

  Tutte le operazioni di controllo della firma riguardanti le Entity Configuration, i Subordinate Statement e i Trust Mark, sono eseguite con le chiavi pubbliche di Federazione. Per gli algoritmi supportati fare riferimento alla Sezione `Algoritmo Crittografico`.

Parametri Comuni delle Entity Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Le Entity Configuration di tutti i partecipanti nella federazione DEVONO avere in comune i parametri elencati di seguito.


.. list-table::
   :class: longtable
   :widths: 20 60
   :header-rows: 1

   * - **Claim**
     - **Descrizione**
   * - **iss**
     - String. Identificatore dell'Entità emittente.
   * - **sub**
     - String. Identificatore dell'Entità a cui si riferisce. DEVE essere uguale a ``iss``.
   * - **iat**
     - UNIX Timestamp con il tempo di generazione del JWT, codificato come NumericDate come indicato in :rfc:`7519`.
   * - **exp**
     - UNIX Timestamp con il tempo di scadenza del JWT, codificato come NumericDate come indicato in :rfc:`7519`.
   * - **jwks**
     - Un JSON Web Key Set (JWKS) :rfc:`7517` che rappresenta la parte pubblica delle chiavi di firma dell'Entità in questione. Ogni JWK nel set JWK DEVE avere un ID chiave (claim kid) e PUÒ avere un parametro `x5c`, come definito in :rfc:`7517`. Contiene le Chiavi dell'Entità di Federazione richieste per le operazioni di Trust Evaluation.

       **x5c**: Il parametro `x5c` incluso nel parametro `jwks` dell'Entity Configuration DEVE contenere solo il Certificato X.509 auto-emesso relativo al corrispondente `jwk`.
   * - **metadata**
     - Oggetto JSON. Ogni chiave dell'Oggetto JSON rappresenta un identificatore di tipo di metadati contenente un Oggetto JSON che rappresenta i metadati, secondo lo schema di metadati di quel tipo. Un'Entity Configuration PUÒ contenere più dichiarazioni di metadati, ma solo una per ogni tipo di metadati (<**entity_type**>). i tipi di metadati sono definiti nella sezione `Tipi di Metadati <Metadata Types>`_.


Entity Configuration Trust Anchor
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

L'Entity Configuration del Trust Anchor, oltre ai parametri comuni elencati sopra, utilizza i seguenti parametri:

.. list-table::
   :class: longtable
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Descrizione**
     - **Richiesto**
   * - **trust_mark_issuers**
     - Array JSON che definisce quali autorità di Federazione sono considerate affidabili per l'emissione di Trust Mark specifici, assegnati con i loro identificatori unici.
     - |uncheck-icon|


Entity Configuration Foglie e Intermediari
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Oltre ai claim precedentemente definiti, l'Entity Configuration delle Foglie e delle Entità Intermedie utilizza i seguenti parametri:


.. list-table::
   :class: longtable
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Descrizione**
     - **Richiesto**
   * - **authority_hints**
     - Array di URL (String). Contiene un elenco di URL delle entità superiori immediate, come il Trust Anchor o un Intermediario, che emette un Subordinate Statement relativo a questo soggetto.
     - |check-icon|
   * - **trust_marks**
     - Un Array JSON contenente i Trust Mark.
     - |check-icon|


Tipi di Metadati
^^^^^^^^^^^^^^^^

In questa sezione sono definiti i principali tipi di metadati mappati sui ruoli dell'ecosistema, fornendo i riferimenti del protocollo di metadati per ognuno di questi.


.. note::
  Le voci che non hanno alcun riferimento a una bozza o standard noto sono intese per essere definite in questo riferimento tecnico.

.. list-table::
   :class: longtable
   :widths: 20 20 20 60
   :header-rows: 1

   * - Entità OpenID
     - Entità EUDI
     - Tipo di Metadati
     - Riferimenti
   * - Trust Anchor
     - Trust Anchor
     - ``federation_entity``
     - `OID-FED`_
   * - Intermediario
     - Intermediario
     - ``federation_entity``
     - `OID-FED`_
   * - Fornitore di Wallet
     - Fornitore di Wallet
     - ``federation_entity``, ``wallet_solution``
     - --
   * - Authorization Server
     -
     - ``federation_entity``, ``oauth_authorization_server``
     - `OPENID4VCI`_
   * - Credential Issuer
     - Fornitore PID, Fornitore (Q)EAA
     - ``federation_entity``, ``openid_credential_issuer``, [``oauth_authorization_server``]
     - `OPENID4VCI`_
   * - Relying Party
     - Relying Party
     - ``federation_entity``, ``openid_credential_verifier``
     - `OID-FED`_, `OpenID4VP`_


.. note::
  I metadati del Fornitore di Wallet sono definiti nella sezione sottostante.

  :ref:`wallet-solution:Soluzione Wallet`.


.. note::
  Nei casi in cui un Fornitore PID/EAA implementa sia il Credential Issuer che l'Authorization Server, DEVE incorporare sia ``oauth_authorization_server`` che ``openid_credential_issuer`` all'interno dei suoi tipi di metadati.
  Altre implementazioni possono dividere il Credential Issuer dall'Authorization Server, quando questo accade i metadati del Credential Issuer DEVONO contenere i parametri `authorization_servers`, incluso l'identificatore unico dell'Authorization Server.
  Inoltre, se dovesse esserci la necessità di Autenticazione dell'Utente da parte del Credential Issuer, potrebbe essere necessario includere il tipo di metadati pertinente, sia ``openid_relying_party`` che ``openid_credential_verifier``.


Metadati di federation_entity Foglie
------------------------------------

I metadati *federation_entity* per le Foglie DEVONO contenere i seguenti claim.


.. list-table::
  :class: longtable
  :widths: 20 60
  :header-rows: 1

  * - **Claim**
    - **Descrizione**
  * - **organization_name**
    - Vedi `OID-FED`_ Sezione 5.2.2
  * - **homepage_uri**
    - Vedi `OID-FED`_ Sezione 5.2.2
  * - **policy_uri**
    - Vedi `OID-FED`_ Sezione 5.2.2
  * - **logo_uri**
    - URL del logo dell'entità; DEVE essere in formato SVG. Vedi `OID-FED`_ Sezione 5.2.2
  * - **contacts**
    - Indirizzo email verificato istituzionale (PEC) dell'entità. Vedi `OID-FED`_ Sezione 5.2.2
  * - **federation_resolve_endpoint**
    - Vedi `OID-FED`_ sezione 8.3
  * - **tos_uri**
    - [OPZIONALE] Stringa URL che punta a un documento di termini di servizio leggibile dall'uomo per il client che descrive una relazione contrattuale tra l'utente finale e il client che l'utente finale accetta quando autorizza il client. Vedi `OID-FED`_.


Subordinate Statements
----------------------

I Subordinate Statement (Entity Statement su un Subordinato) sono emessi da Trust Anchor e Intermediari e ottenuti tramite l'endpoint Federation Fetch. Struttura, claim, policy dei metadati, trust mark, firma, validazione ed esempi sono definiti in modo normativo in `OID-FED`_.

.. note::
  L'endpoint Federation Fetch PUÒ anche pubblicare certificati X.509 per ciascuna delle chiavi pubbliche del Subordinato, consentendo la distribuzione dei certificati X.509 emessi tramite un servizio RESTful.


Discovery della Federazione
---------------------------

La Scoperta di Entità di Federazione è il processo attraverso il quale i partecipanti verificano l'identità e lo stato di altre entità di federazione. Questo comporta l'interrogazione degli endpoint di federazione per confermare lo stato di validità dell'entità e la conformità al Trust Framework.

Il processo di scoperta utilizza l'API di Federazione per raccogliere informazioni sulle entità e produce Trust Chain che validano la conformità e l'autorizzazione dell'entità all'interno della federazione.

Il processo di scoperta stabilisce i concetti fondamentali che vengono poi applicati in scenari operativi specifici come dettagliato nella sezione Meccanismo di Trust Evaluation.

.. note::
  I Trust Anchor DEVONO distribuire le loro Chiavi Pubbliche di Federazione attraverso meccanismi sicuri fuori banda, come pubblicarle su una pagina web verificata o archiviarle in un repository remoto come parte di una lista di trust. La logica dietro questo requisito è che fare affidamento solo sui dati forniti all'interno dell'Entity Configuration del Trust Anchor non mitiga adeguatamente i rischi associati agli attacchi di manipolazione DNS e TLS. Per garantire la sicurezza, tutti i partecipanti DEVONO ottenere le chiavi pubbliche del Trust Anchor utilizzando questi metodi fuori banda. Dovrebbero quindi confrontare queste chiavi con quelle ottenute dall'Entity Configuration del Trust Anchor, scartando qualsiasi chiave che non corrisponda. Questo processo aiuta a garantire l'integrità e l'autenticità delle chiavi pubbliche del Trust Anchor e la sicurezza generale della federazione (:ref:`WP_017 <wallet-instance-testcases>`).

Validità, scadenza e revoca dei Subordinate Statement sono definite in `OID-FED`_.

La concatenazione delle dichiarazioni, attraverso la combinazione di questi meccanismi di firma e il binding di claim e chiavi pubbliche, forma la Trust Chain.

Le Trust Chain possono anche essere verificate offline, utilizzando una delle chiavi pubbliche del Trust Anchor.

.. note::
  Poiché l'Istanza del Wallet non è un'Entità di Federazione, il Meccanismo di Trust Evaluation relativo ad essa **richiede la presentazione del Wallet Attestation durante le fasi di emissione e presentazione delle credenziali**.

  Il Wallet Attestation trasmette tutte le informazioni richieste riguardanti l'istanza, come la sua chiave pubblica e qualsiasi altra informazione tecnica o amministrativa, senza alcun dato personale dell'Utente.


Trust Chain
-----------

La Trust Chain è una sequenza di dichiarazioni verificate che valida la conformità di un partecipante con la Federazione. Ha una data di scadenza, oltre la quale DEVE essere rinnovata per ottenere i metadati freschi e aggiornati. La data di scadenza della Trust Chain è determinata dal timestamp di scadenza più precoce tra tutti i timestamp di scadenza contenuti nelle dichiarazioni. Nessuna Entità può forzare la data di scadenza della Trust Chain ad essere superiore a quella configurata dal Trust Anchor.

**Ruolo nell'Onboarding**: Durante l'onboarding delle entità, le Trust Chain sono costruite per dimostrare la relazione di trust gerarchica completa dal Trust Anchor alla nuova entità.

**Ruolo nelle Operazioni**: Durante l'emissione e la presentazione delle credenziali, le Trust Chain forniscono prova crittografica della validità dell'entità e dello stato di conformità.

Di seguito è riportata una rappresentazione astratta di una Trust Chain.

.. code-block:: json

    [
        "EntityConfiguration-as-SignedJWT-selfissued-byLeaf",
        "EntityStatement-as-SignedJWT-issued-byTrustAnchor"
    ]

Di seguito è riportato un esempio non normativo di una Trust Chain, composta da un Array JSON contenente JWT, con un Intermediario coinvolto.

.. code-block:: json

    [
      "eyJhbGciOiJFUzI1NiIsImtpZCI6Ik5GTTFXVVZpVWxZelVXcExhbWxmY0VwUFJWWTJWWFpJUmpCblFYWm1SSGhLWVVWWVVsZFRRbkEyTkEiLCJ0eXAiOiJhcHBsaWNhdGlvbi9lbnRpdHktc3RhdGVtZW50K2p3dCJ9.eyJleHAiOjE2NDk1OTA2MDIsImlhdCI6MTY0OTQxNzg2MiwiaXNzIjoiaHR0cHM6Ly9ycC5leGFtcGxlLm9yZyIsInN1YiI6Imh0dHBzOi8vcnAuZXhhbXBsZS5vcmciLCJqd2tzIjp7ImtleXMiOlt7Imt0eSI6IkVDIiwia2lkIjoiTkZNMVdVVmlVbFl6VVdwTGFtbGZjRXBQUlZZMlZYWklSakJuUVhabVJIaEtZVVZZVWxkVFFuQTJOQSIsImNydiI6IlAtMjU2IiwieCI6InVzbEMzd2QtcFgzd3o0YlJZbnd5M2x6cGJHWkZoTjk2aEwyQUhBM01RNlkiLCJ5IjoiVkxDQlhGV2xkTlNOSXo4a0gyOXZMUjROMThCa3dHT1gyNnpRb3J1UTFNNCJ9XX0sIm1ldGFkYXRhIjp7Im9wZW5pZF9yZWx5aW5nX3BhcnR5Ijp7ImFwcGxpY2F0aW9uX3R5cGUiOiJ3ZWIiLCJjbGllbnRfaWQiOiJodHRwczovL3JwLmV4YW1wbGUub3JnLyIsImNsaWVudF9yZWdpc3RyYXRpb25fdHlwZXMiOlsiYXV0b21hdGljIl0sImp3a3MiOnsia2V5cyI6W3sia3R5IjoiRUMiLCJraWQiOiJORk0xV1VWaVVsWXpVV3BMYW1sZmNFcFBSVlkyVlhaSVJqQm5RWFptUkhoS1lVVllVbGRUUW5BMk5BIiwiY3J2IjoiUC0yNTYiLCJ4IjoidXNsQzN3ZC1wWDN3ejRiUllud3kzbHpwYkdaRmhOOTZoTDJBSEEzTVE2WSIsInkiOiJWTENCWEZXbGROU05JejhrSDI5dkxSNE4xOEJrd0dPWDI2elFvcnVRMU00In1dfSwiY2xpZW50X25hbWUiOiJOYW1lIG9mIGFuIGV4YW1wbGUgb3JnYW5pemF0aW9uIiwiY29udGFjdHMiOlsib3BzQHJwLmV4YW1wbGUuaXQiXSwiZ3JhbnRfdHlwZXMiOlsicmVmcmVzaF90b2tlbiIsImF1dGhvcml6YXRpb25fY29kZSJdLCJyZWRpcmVjdF91cmlzIjpbImh0dHBzOi8vcnAuZXhhbXBsZS5vcmcvb2lkYy9ycC9jYWxsYmFjay8iXSwicmVzcG9uc2VfdHlwZXMiOlsiY29kZSJdLCJzY29wZSI6ImV1LmV1cm9wYS5lYy5ldWRpdy5waWQuMSBldS5ldXJvcGEuZWMuZXVkaXcucGlkLml0LjEgZW1haWwiLCJzdWJqZWN0X3R5cGUiOiJwYWlyd2lzZSJ9LCJmZWRlcmF0aW9uX2VudGl0eSI6eyJmZWRlcmF0aW9uX3Jlc29sdmVfZW5kcG9pbnQiOiJodHRwczovL3JwLmV4YW1wbGUub3JnL3Jlc29sdmUvIiwib3JnYW5pemF0aW9uX25hbWUiOiJFeGFtcGxlIFJQIiwiaG9tZXBhZ2VfdXJpIjoiaHR0cHM6Ly9ycC5leGFtcGxlLml0IiwicG9saWN5X3VyaSI6Imh0dHBzOi8vcnAuZXhhbXBsZS5pdC9wb2xpY3kiLCJsb2dvX3VyaSI6Imh0dHBzOi8vcnAuZXhhbXBsZS5pdC9zdGF0aWMvbG9nby5zdmciLCJjb250YWN0cyI6WyJ0ZWNoQGV4YW1wbGUuaXQiXX19LCJ0cnVzdF9tYXJrcyI6W3siaWQiOiJodHRwczovL3JlZ2lzdHJ5LmVpZGFzLnRydXN0LWFuY2hvci5leGFtcGxlLmV1L29wZW5pZF9yZWx5aW5nX3BhcnR5L3B1YmxpYy8iLCJ0cnVzdF9tYXJrIjoiZXlKaCBcdTIwMjYifV0sImF1dGhvcml0eV9oaW50cyI6WyJodHRwczovL2ludGVybWVkaWF0ZS5laWRhcy5leGFtcGxlLm9yZyJdfQ.Un315HdckvhYA-iRregZAmL7pnfjQH2APz82blQO5S0sl1JR0TEFp5E1T913g8GnuwgGtMQUqHPZwV6BvTLA8g",
      "eyJhbGciOiJFUzI1NiIsImtpZCI6IlNURkRXV2hKY0dWWFgzQjNSVmRaYWtsQ0xUTnVNa000WTNGNlFUTk9kRXRyZFhGWVlYWjJjWGN0UVEiLCJ0eXAiOiJhcHBsaWNhdGlvbi9lbnRpdHktc3RhdGVtZW50K2p3dCJ9.eyJleHAiOjE2NDk2MjM1NDYsImlhdCI6MTY0OTQ1MDc0NiwiaXNzIjoiaHR0cHM6Ly9pbnRlcm1lZGlhdGUuZWlkYXMuZXhhbXBsZS5vcmciLCJzdWIiOiJodHRwczovL3JwLmV4YW1wbGUub3JnIiwiandrcyI6eyJrZXlzIjpbeyJrdHkiOiJFQyIsImtpZCI6Ik5GTTFXVVZpVWxZelVXcExhbWxmY0VwUFJWWTJWWFpJUmpCblFYWm1SSGhLWVVWWVVsZFRRbkEyTkEiLCJjcnYiOiJQLTI1NiIsIngiOiJ1c2xDM3dkLXBYM3d6NGJSWW53eTNsenBiR1pGaE45NmhMMkFIQTNNUTZZIiwieSI6IlZMQ0JYRldsZE5TTkl6OGtIMjl2TFI0TjE4Qmt3R09YMjZ6UW9ydVExTTQifV19LCJtZXRhZGF0YV9wb2xpY3kiOnsib3BlbmlkX3JlbHlpbmdfcGFydHkiOnsic2NvcGUiOnsic3Vic2V0X29mIjpbImV1LmV1cm9wYS5lYy5ldWRpdy5waWQuMSwgIGV1LmV1cm9wYS5lYy5ldWRpdy5waWQuaXQuMSJdfSwicmVxdWVzdF9hdXRoZW50aWNhdGlvbl9tZXRob2RzX3N1cHBvcnRlZCI6eyJvbmVfb2YiOlsicmVxdWVzdF9vYmplY3QiXX0sInJlcXVlc3RfYXV0aGVudGljYXRpb25fc2lnbmluZ19hbGdfdmFsdWVzX3N1cHBvcnRlZCI6eyJzdWJzZXRfb2YiOlsiUlMyNTYiLCJSUzUxMiIsIkVTMjU2IiwiRVM1MTIiLCJQUzI1NiIsIlBTNTEyIl19fX0sInRydXN0X21hcmtzIjpbeyJpZCI6Imh0dHBzOi8vdHJ1c3QtYW5jaG9yLmV4YW1wbGUuZXUvb3BlbmlkX3JlbHlpbmdfcGFydHkvcHVibGljLyIsInRydXN0X21hcmsiOiJleUpoYiBcdTIwMjYifV19._qt5-T6DahP3TuWa_27klE8I9Z_sPK2FtQlKY6pGMPchbSI2aHXY3aAXDUrObPo4CHtqgg3J2XcrghDFUCFGEQ","eyJhbGciOiJFUzI1NiIsImtpZCI6ImVXa3pUbWt0WW5kblZHMWxhMjU1ZDJkQ2RVZERSazQwUWt0WVlVMWFhRFZYT1RobFpHdFdXSGQ1WnciLCJ0eXAiOiJhcHBsaWNhdGlvbi9lbnRpdHktc3RhdGVtZW50K2p3dCJ9.eyJleHAiOjE2NDk2MjM1NDYsImlhdCI6MTY0OTQ1MDc0NiwiaXNzIjoiaHR0cHM6Ly90cnVzdC1hbmNob3IuZXhhbXBsZS5ldSIsInN1YiI6Imh0dHBzOi8vaW50ZXJtZWRpYXRlLmVpZGFzLmV4YW1wbGUub3JnIiwiandrcyI6eyJrZXlzIjpbeyJrdHkiOiJFQyIsImtpZCI6IlNURkRXV2hKY0dWWFgzQjNSVmRaYWtsQ0xUTnVNa000WTNGNlFUTk9kRXRyZFhGWVlYWjJjWGN0UVEiLCJjcnYiOiJQLTI1NiIsIngiOiJyQl9BOGdCUnh5NjhVTkxZRkZLR0ZMR2VmWU5XYmgtSzh1OS1GYlQyZkZJIiwieSI6IlNuWVk2Y3NjZnkxcjBISFhLTGJuVFZsamFndzhOZzNRUEs2WFVoc2UzdkUifV19LCJ0cnVzdF9tYXJrcyI6W3siaWQiOiJodHRwczovL3RydXN0LWFuY2hvci5leGFtcGxlLmV1L2ZlZGVyYXRpb25fZW50aXR5L3RoYXQtcHJvZmlsZSIsInRydXN0X21hcmsiOiJleUpoYiBcdTIwMjYifV19.r3uoi-U0tx0gDFlnDdITbcwZNUpy7M2tnh08jlD-Ej9vMzWMCXOCCuwIn0ZT0jS4M_sHneiG6tLxRqj-htI70g"
    ]


.. note::
  L'intera Trust Chain è verificabile possedendo solo le chiavi pubbliche del Trust Anchor.

Ci sono eventi in cui le chiavi non sono disponibili per verificare l'intera catena di trust:

 - **Cambio di Chiave da parte del Credential Issuer**: Il Credential Issuer PUÒ aggiornare le sue chiavi crittografiche. Le chiavi crittografiche DEVONO essere considerate valide se valutate entro il loro periodo di validità originariamente designato a meno che una ragione di sicurezza non le renda inutilizzabili. La ragione di revoca DEVE essere pubblicata. Le chiavi crittografiche storiche, cioè le chiavi crittografiche pubbliche inutilizzate o revocate, DEVONO essere pubblicate utilizzando l'Endpoint delle Chiavi Storiche di Federazione.

 - **Cambio nei Tipi di Credenziali**: Se il Credential Issuer cambia i **tipi** di Credenziali emesse, per esempio decidendo di non emettere più uno o più tipi di Credenziali, le relative chiavi crittografiche pubbliche DEVONO essere disponibili per il periodo di validità originariamente designato.

 - **Fusione di Credential Issuer**: Se un Credential Issuer si fonde con un altro, creando una nuova Entità Organizzativa o lavorando per conto di un'altra utilizzando un hostname o dominio diverso, la configurazione di federazione **precedentemente** disponibile e le chiavi storiche DEVONO essere mantenute disponibili agli endpoint well-known del Credential Issuer originale.

 - **Credential Issuer Diventa Inattivo**: Se un Credential Issuer diventa inattivo, la sua **relativa** Entity Configuration e l'Endpoint di Entità Storica di Federazione DEVONO essere mantenuti disponibili.

Meccanismi di Attestazione di Trust Offline
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

I flussi offline non consentono la valutazione in tempo reale dello stato di un'Entità, come la sua revoca. Allo stesso tempo, l'utilizzo di Trust Chain di breve durata consente il raggiungimento di attestazioni di trust compatibili con i protocolli amministrativi di revoca richiesti (ad esempio, una revoca deve essere propagata in meno di 24 ore, quindi la Trust Chain non deve essere valida per più di quel periodo).


Attestazione di Trust del Wallet Offline
""""""""""""""""""""""""""""""""""""""""

Dato che l'Istanza del Wallet non può pubblicare i suoi metadati online all'endpoint *.well-known/openid-federation*, DEVE ottenere un Wallet Attestation emesso dal suo Fornitore di Wallet. Il Wallet Attestation DEVE contenere tutte le informazioni rilevanti riguardanti le capacità di sicurezza dell'Istanza del Wallet e la sua configurazione relativa al protocollo. DOVREBBE contenere la Trust Chain relativa al suo emittente (Fornitore di Wallet).


Metadati del Relying Party Offline
""""""""""""""""""""""""""""""""""

Poiché la Scoperta di Entità di Federazione è applicabile solo in scenari online, è possibile includere la Trust Chain nelle richieste di presentazione che il Relying Party può emettere per un'Istanza del Wallet.

Il Relying Party DEVE firmare la richiesta di presentazione, la richiesta DOVREBBE includere il claim `trust_chain` nei suoi parametri di header JWT, contenente la Trust Chain di Federazione relativa a se stesso.

L'Istanza del Wallet che verifica la richiesta emessa dal Relying Party DEVE utilizzare le chiavi pubbliche del Trust Anchor per validare l'intera Trust Chain relativa al Relying Party prima di attestare la sua affidabilità.

Inoltre, l'Istanza del Wallet applica la policy dei metadati, se presente.

Rinnovo Rapido della Trust Chain
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Il metodo di rinnovo rapido della Trust Chain offre un modo semplificato per mantenere la validità di una catena di trust senza sottoporsi nuovamente al processo di scoperta completo. È particolarmente utile per aggiornare rapidamente le Trust Relationship quando si verificano cambiamenti minori o quando la Trust Chain è vicina alla scadenza ma la struttura generale della federazione non è cambiata significativamente.

Il processo di rinnovo rapido della Trust Chain è iniziato recuperando nuovamente l'Entity Configuration della foglia. Tuttavia, a differenza del processo di scoperta di federazione che può comportare il recupero delle Entity Configuration a partire dagli authority hint, il rinnovo rapido si concentra sull'ottenere direttamente i Subordinate Statement. Queste dichiarazioni sono richieste utilizzando il `source_endpoint` fornito al loro interno, che punta alla posizione dove le dichiarazioni possono essere recuperate.


Meccanismo di Trust Evaluation
------------------------------

I Trust Anchor DEVONO distribuire le loro Chiavi Pubbliche di Federazione attraverso meccanismi sicuri fuori banda, come pubblicarle su una pagina web verificata o archiviarle in un repository remoto come parte di una lista di trust. La logica dietro questo requisito è che fare affidamento solo sui dati forniti all'interno dell'Entity Configuration del Trust Anchor non mitiga adeguatamente i rischi associati agli attacchi di manipolazione DNS e TLS. Per garantire la sicurezza, tutti i partecipanti DEVONO ottenere le chiavi pubbliche del Trust Anchor utilizzando questi metodi fuori banda. Dovrebbero quindi confrontare queste chiavi con quelle ottenute dall'Entity Configuration del Trust Anchor, scartando qualsiasi chiave che non corrisponda. Questo processo aiuta a garantire l'integrità e l'autenticità delle chiavi pubbliche del Trust Anchor e la sicurezza generale della federazione.

Il Trust Anchor pubblica l'elenco dei suoi subordinati (Federation Subordinate Listing endpoint), le attestazioni dei loro metadati e chiavi pubbliche (Subordinate Statement) e gli eventi storici relativi al loro ciclo di vita (Federation Subordinate Events endpoint).

Ogni partecipante, inclusi Trust Anchor, Intermediario, Credential Issuer, Fornitore di Wallet e Relying Party, pubblica i propri metadati e chiavi pubbliche (endpoint Entity Configuration) nella risorsa web well-known **.well-known/openid-federation**.

Ognuno di questi può essere verificato utilizzando il Subordinate Statement emesso da un superiore, come il Trust Anchor o un Intermediario; per validità e revoca dei Subordinate Statement vedere `OID-FED`_.

La concatenazione delle dichiarazioni, attraverso la combinazione di questi meccanismi di firma e il binding di claim e chiavi pubbliche, forma la Trust Chain.

Le Trust Chain possono anche essere verificate offline, utilizzando una delle chiavi pubbliche del Trust Anchor.

.. note::
  Poiché l'Istanza del Wallet non è un'Entità di Federazione, il Meccanismo di Trust Evaluation relativo ad essa **richiede la presentazione del Wallet Attestation durante le fasi di emissione e presentazione delle credenziali**.

  Il Wallet Attestation trasmette tutte le informazioni richieste riguardanti l'istanza, come la sua chiave pubblica e qualsiasi altra informazione tecnica o amministrativa, senza alcun dato personale dell'Utente.

**Ruolo nell'Onboarding**: I meccanismi di trust evaluation sono essenziali durante la registrazione delle entità e la gestione del ciclo di vita per verificare lo stato di conformità dei nuovi partecipanti e validare i cambiamenti alle entità esistenti. Questo include la validazione delle credenziali di registrazione delle entità che richiedono l'onboarding e garantire che soddisfino le policy di federazione prima di concedere l'autorizzazione operativa.

**Ruolo nelle Operazioni**: Durante le operazioni di emissione e presentazione delle credenziali, la trust evaluation fornisce verifica in tempo reale della validità dell'entità e dello stato di conformità. Questo abilita transazioni di credenziali sicure garantendo che tutte le entità partecipanti (credential issuer, relying party, fornitori di wallet) mantengano il loro stato autorizzato e siano conformi alle policy di federazione correnti.


Stabilire Trust con i Credential Issuer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Nel processo di emissione, la Trust Evaluation garantisce l'integrità e l'autenticità delle Credenziali emesse e l'affidabilità dei loro Emittenti. Questa sezione delinea i meccanismi di Trust Evaluation distinti dai flussi di protocollo, implementati dalle Istanze del Wallet e dai Relying Party, come descritto nella sezione dedicata.

Le Trust Evaluation implementano modi diversi, come definito di seguito:

* **Scoperta di Entità di Federazione**: le Istanze del Wallet e i Relying Party DEVONO verificare l'identità dell'Emittente con il processo di Federation Entity Discovery definito in :ref:`trust-infrastructure:Discovery della Federazione`, interrogando gli endpoint di federazione per confermare validità e conformità al Trust Framework. I dati storici degli eventi dal Federation Subordinate Events Endpoint possono fornire contesto aggiuntivo sul ciclo di vita e sulla conformità dell'entità.

* **Trust Chain**: le Istanze del Wallet e i Relying Party valutano le Trust Chain dell'Emittente con i meccanismi definiti in :ref:`trust-infrastructure:Trust Chain`. Le Trust Chain possono essere fornite staticamente o costruite tramite Federation Entity Discovery, per garantire che l'entità che richiede la Credenziale appartenga a una federazione riconosciuta e fidata.

* **Valutazione dei Trust Mark**: i Trust Mark sono valutati per la conformità continua alle policy di federazione e indicano l'aderenza a standard e pratiche richieste.

* **Valutazione delle Policy**: le Istanze del Wallet e i Relying Party DEVONO verificare che il Credential Issuer sia autorizzato all'emissione della Credenziale di interesse. Metadati, policy dei metadati e Trust Mark supportano questi controlli (:ref:`WP_050a <wallet-credential-issuance-testcases>`).

Nel processo rappresentato nel diagramma di sequenza sottostante, l'Istanza del Wallet utilizza l'API di Federazione per scoprire e raccogliere i Credential Issuer abilitati nella federazione. Il processo di scoperta produce la Trust Chain. Quando la Trust Chain è fornita staticamente in una richiesta firmata o nella Credenziale, è sufficiente aggiornarla quando è disponibile la connessione a Internet, mentre DEVE essere aggiornata quando la Trust Chain fornita staticamente è scaduta.

.. plantuml:: plantuml/trust-evaluation-flow.puml
    :width: 99%
    :alt: La figura illustra il Processo di Trust Evaluation.
    :caption: `Processo di Trust Evaluation. <https://www.plantuml.com/plantuml/svg/fPE_Rjmm38TtFGMHfTCrUuOWXwlJ6bs2fd-MB8n5nqHbIg2ek-JjwxFW9XUSkzIJ87_y-AD1tsH3jJ86-Aub6pHx30MDey2TnevoTWdLkEE4Ol0BGo0xkTgrW1akTagUn1W3j3aNqeiJgcrcgXKZ7Sap6btMZblfXZZHhhfXStqzEQ_WbgmRfjE738qOsmlielJyL7IEzo201XyF5CBcjyI3NCP4mdxJawUA08bFaSNShfsrjSCLV2ChAcUrIumJldasnMwAMco8Ugpvmc8PUerZJVZE4M9Cq4S5mcvuL-PWUjuqQPjbrlyUSzLyNnwZUXOqWdj3ev74ghe_0gkAvGlynC3-M6q3GLBQSomPygkgP9Qd-Utjts3BG5_f9Jz8qhXdJnvOZjpvJ8x4E_Ul07LfTWEoE8V1eEtVtW7doWAAXnz2pucL_CfSTSV9mu5jgCbFTvz2fhNQxPJV5h8Q6jMegpDiKmfC6UvYu6uwd6C-aVAUwbBrB1XW94EFXkVepsI0U-I0Zu7WzHVCC07nG7vUGiwve7JaRaXy6SCV>`_

.. note::
  Come mostrato nella figura, il processo di Trust Evaluation è completamente separato e distinto dal flusso specifico del protocollo. Opera in un flusso diverso e utilizza protocolli specializzati progettati specificamente per questo scopo.

Stabilire Trust con il Relying Party
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Nel contesto della valutazione dei Relying Party, la responsabilità per la Trust Evaluation spetta esclusivamente all'Istanza del Wallet.
I meccanismi di Trust Evaluation sono distinti dai flussi di protocollo e sono implementati dall'Istanza del Wallet, come dettagliato nella sezione dedicata.

Le Trust Evaluation sono condotte come segue:

* **Scoperta di Entità di Federazione**: quando l'Istanza del Wallet riceve una richiesta firmata da un Relying Party, DEVE verificarne l'identità con il Federation Entity Discovery definito in :ref:`trust-infrastructure:Discovery della Federazione`, interrogando gli endpoint di federazione per confermare validità e conformità al Trust Framework e valutando la firma della richiesta con il materiale crittografico della Trust Chain. I dati storici dal Federation Subordinate Events Endpoint possono fornire contesto aggiuntivo sul ciclo di vita e sulla conformità del Relying Party.

* **Trust Chain**: l'Istanza del Wallet valuta le Trust Chain del Relying Party con i meccanismi definiti in :ref:`trust-infrastructure:Trust Chain`. Le Trust Chain possono essere fornite staticamente o costruite tramite Federation Entity Discovery, per garantire che il Relying Party appartenga a una federazione riconosciuta e fidata. Ciò include il controllo della Trust Chain dall'autorità radice (Trust Anchor) al Relying Party (:ref:`WP_079 <wallet-credential-presentation-testcases>`).

* **Valutazione dei Trust Mark**: i Trust Mark sono valutati per la conformità continua alle policy di federazione. I Relying Party POSSONO includere Trust Mark nella Entity Configuration per segnalare proprietà amministrative e conformità a profili specifici, ad esempio le concessioni nell'interazione con utenti minorenni (:ref:`WP_080 <wallet-credential-presentation-testcases>`).

* **Valutazione delle Policy**: l'Istanza del Wallet DEVE verificare che il Relying Party sia autorizzato a richiedere la Credenziale di interesse. Metadati, policy dei metadati e Trust Mark implementano questi controlli (:ref:`WP_087 <wallet-credential-presentation-testcases>`).

Nel processo raffigurato nel diagramma di sequenza sottostante, l'Istanza del Wallet utilizza l'API di Federazione per scoprire e raccogliere tutti i Relying Party abilitati all'interno della federazione. Il processo di scoperta produce la Trust Chain. Quando la Trust Chain è fornita staticamente all'interno di una richiesta firmata, deve solo essere aggiornata quando una connessione internet è disponibile, ma DEVE essere aggiornata se la Trust Chain fornita staticamente è scaduta.

.. plantuml:: plantuml/trust-rp-discovery-flow.puml
    :width: 99%
    :alt: La figura illustra il Processo di Scoperta del Relying Party.
    :caption: `Trust Evaluation - Processo di Scoperta del Relying Party. <https://www.plantuml.com/plantuml/svg/ZLDFRzi-3BtxKn2z_4xvzTv3qQ1_i64x16dNNGeKgaGdH6NAawYq_lPZvBbD33Tm3ev5Fpw-Hv5NIKoKt7XOe--8Dx3ISmStb6pOOUogLizagJKiyDjuZ_ATDOajWabmreTWY9qTuQyV2-Q8-XZni2o8XvYJm9BjDaGuLpR1sA0Z8yfOZSekBY-L-G8Y_iceQGRQ60IjeDDO2ZbQhBJqGe4ZoHUGQCEAin4Tif3ncen9NurGu85pikQOog4D3i6m0zmPdrLi0jdY9qbblBQcXjxUzTOG0wMzt1qvLV56iYK-p2bi781OC38AsC2CTg-j0ltDaAN_GbQ37QWgSYghL3WKaTF-FWwx_f_AoY-UBBnYbohq2Vk2qxs_Gx5RMAyqxPQ5f8Fhm3LjSYnzV68m0l-_eVUBLmvlV1vQP7AB6Xr6CzXHgaaBQvGSUPAvEgNgzbsYiMefYrhQvtuZbWHr34qHE-8w8M7Ltz6OgY_lGsYX3X7GsEq8KW1VQ7nO3fsRigOGsA30Pu-UwptusRG4lzO_1sQbcPJSCz_dbn0TiH64Uz5dWwT5ZMaU3uUcZRYZa1EaWUg9o_2KhtSVIWT3Fx1BJ_mnuFrmdz24xAggFEOhEnhbhtQiZ7xPfiputb94DtU1zEej_jlEGuibdlhTcCkrLECoPFQCjp66EDlpicqzOO9Ly6JrPKxE3KRQOJ_mDR7nqA0OPyHKLretD_ul>`_

.. note::
  Come mostrato nella figura, è richiesta una connessione internet per aggiornare la Trust Chain su un RP e controllare il suo stato di revoca.

Valutare Trust con i Wallet
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Il Fornitore di Wallet emette il Wallet Attestation, certificando lo stato operativo delle sue Istanze del Wallet e includendo una delle loro chiavi pubbliche.

Il Wallet Attestation PUÒ contenere la Trust Chain che attesta l'affidabilità per il suo emittente (Fornitore di Wallet) al momento dell'emissione.

L'Istanza del Wallet fornisce il suo Wallet Attestation all'interno della richiesta firmata durante la fase di emissione PID. Il Credential Issuer DEVE valutare la Trust Chain sull'emittente del Wallet Attestation (formalmente, il Fornitore di Wallet).

Non-ripudio delle Attestazioni di Lunga Durata
----------------------------------------------

Il Trust Anchor e i suoi Intermediari DEVONO esporre l'endpoint delle Chiavi Storiche di Federazione, dove sono pubblicate tutte le parti pubbliche delle Chiavi dell'Entità di Federazione che non sono più utilizzate, sia scadute che revocate.

I dettagli di questo endpoint sono definiti nella `OID-FED`_ Sezione 8.7.

Ogni JWT contenente una Trust Chain negli header JWT può essere verificato nel tempo, poiché l'intera Trust Chain è verificabile utilizzando la chiave pubblica del Trust Anchor.

Anche se il Trust Anchor ha cambiato le sue chiavi crittografiche per la firma digitale, l'endpoint delle Chiavi Storiche di Federazione rende sempre disponibili le chiavi non più utilizzate per le verifiche di firma storiche.

.. _trust-infrastructure-pki-x509:

X.509 PKI
---------

L'Infrastruttura a Chiave Pubblica (PKI) X.509 è un framework progettato per creare, gestire, distribuire, utilizzare, archiviare e revocare certificati digitali X.509. Al centro della PKI X.509 c'è il concetto di Autorità di Certificazione (CA), che emette certificati digitali alle entità. Questi certificati sono richiesti per stabilire comunicazioni sicure su reti, incluso internet, abilitando funzionalità di crittografia e firma digitale. La gerarchia PKI tipicamente coinvolge una CA radice in cima, con una o più CA subordinate sotto, formando una catena di trust. Le entità si affidano a questa catena di trust per verificare l'autenticità dei certificati. Gli standard X.509 definiscono il formato dei certificati a chiave pubblica.

L'integrazione di OpenID Federation 1.0 con la PKI tradizionale basata su X.509 (rfc:5280), completata da un'API RESTful, mira a migliorare l'infrastruttura con funzionalità aggiuntive, rendendola navigabile e trasparente.

Questo approccio sfrutta la natura dinamica e flessibile di OpenID Federation insieme al requisito dei Certificati X.509 per applicazioni legacy e scopi di interoperabilità, mirando ad affrontare le esigenze in evoluzione di verifica dello stato di registrazione dei partecipanti alla federazione, la loro conformità alle regole condivise e la gestione generale e interoperabile del trust in ecosistemi digitali multilaterali.

**Ruolo nell'Onboarding**: durante la registrazione delle entità, i certificati X.509 integrano i meccanismi OpenID Federation per l'interoperabilità con sistemi legacy e l'integrazione con infrastrutture PKI esistenti.

**Ruolo nelle Operazioni**: durante le operazioni sulle credenziali, i certificati X.509 consentono comunicazioni sicure con sistemi legacy e percorsi di verifica alternativi per entità che richiedono validazione PKI tradizionale.

OpenID Federation e PKI basata su X.509 condividono diversi elementi, come elencato di seguito:

- **Approccio gerarchico**: entrambi utilizzano un Trust Model gerarchico con un'unica terza parte fidata sovrastante, il Trust Anchor, fidata al di sopra di tutte le altre.
- **Scalabilità con più Trust Anchor e Intermediari**: nonostante un modello gerarchico unico, la possibilità di avere più Trust Anchor e Intermediari, al di sotto di uno o più Trust Anchor, scala le responsabilità.
- **Estensioni personalizzate**: entrambi i sistemi consentono estensioni personalizzate per requisiti specifici o per funzionalità aggiuntive. I certificati X.509 supportano estensioni personalizzate; OpenID Federation consente metadati di protocollo specifici, Trust Mark e policy tramite un linguaggio di policy.
- **Catena di trust/certificato**: si basano su una prova concatenata di trust, dal Trust Anchor agli Intermediari fino all'entità finale (Foglia).
- **Vincoli nella catena**: è possibile applicare vincoli nella Trust Chain su delega del trust, numero di intermediari e domini coinvolti.
- **Distribuzione delle chiavi pubbliche**: entrambi prevedono la distribuzione della chiave pubblica del Trust Anchor per consentire la verifica della catena.
- **Registro delle chiavi scadute**: mantenere un registro delle chiavi scadute è essenziale per entrambi, per il non ripudio delle firme passate anche quando le chiavi cambiano.


Trust Anchor di Federazione e CA X.509
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Nel contesto di OpenID Federation, il Trust Anchor gioca un ruolo simile a quello di un'Autorità di Certificazione (CA) nelle Infrastrutture a Chiave Pubblica (PKI) basate su X.509. Entrambi servono come elementi fondamentali di trust all'interno dei loro rispettivi sistemi. In questo documento, il termine "Trust Anchor" è spesso utilizzato per comprendere entrambi i concetti. L'infrastruttura di trust descritta qui allinea il Trust Anchor di OpenID Federation con l'Autorità di Certificazione PKI X.509, rendendoli quindi un'unica entità unica che supporta sia `RFC 5280`_ che OpenID Federation 1.0.

Emissione di Certificati X.509
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In una Federazione OpenID, ogni partecipante è richiesto di auto-emettere la sua Entity Configuration, firmandola con una delle sue chiavi crittografiche che sono attestate dai Superiori Immediati.

Allo stesso modo, ogni Entità di federazione ha l'autonomia di emettere una dichiarazione firmata su se stessa sotto forma di un Certificato X.509.
I partecipanti alla federazione che hanno bisogno di emettere Certificati X.509 su se stessi e per i loro scopi specifici, possono emettere e firmare Certificati X.509 utilizzando una delle loro Chiavi dell'Entità di Federazione attestate dalle loro Autorità di Federazione (Superiore Immediato). Questo processo allinea l'emissione di Certificati X.509 con il paradigma di delegazione della federazione.

Questo è fattibile perché il Certificato X.509 può essere verificato utilizzando una Catena di Certificati X.509, simile all'approccio utilizzato per le Entity Configuration in OpenID Federation.

Le Foglie di Federazione non sono Autorità di Certificazione (CA) o intermediari CA autorizzati a emettere certificati X.509 per i loro subordinati. Invece, le Foglie di Federazione agiscono come intermediari per l'emissione di certificati esclusivamente su se stesse. Questo è realizzato applicando vincoli di denominazione appropriati per garantire che i certificati X.509 siano correttamente delimitati.
I vincoli di denominazione sono applicati dai Superiori Immediati all'interno dei certificati emessi all'entità Foglia, specificamente riguardo alle Chiavi dell'Entità di Federazione della Foglia. Di conseguenza, la Foglia può emettere certificati X.509 solo su se stessa, mantenendo così l'integrità della Trust Chain.

Quando un partecipante auto-emette un Certificato X.509, aderisce ai seguenti requisiti:

1. **Nome del soggetto**: il nome del soggetto del certificato X.509 DEVE corrispondere all'identità del partecipante. Per Intermediari e Foglie il nome del soggetto DEVE includere i seguenti attributi:

   .. list-table::
      :widths: 30 70
      :header-rows: 1

      * - Attributo
        - Requisito
      * - ``Country Name (C)``
        - DEVE contenere il codice paese ISO a due lettere.
      * - ``State or Province Name (ST)``
        - DEVE contenere la regione o provincia in cui l'entità ha sede.
      * - ``Locality Name (L)``
        - DEVE contenere la città in cui l'entità ha sede.
      * - ``Organization Name (O)``
        - DEVE contenere la ragione sociale legale dell'organizzazione.
      * - ``Organizational Unit Name (OU)``
        - PUÒ contenere il dipartimento nell'organizzazione (opzionale).
      * - ``Common Name (CN)``
        - DEVE contenere l'identificatore DNS univoco dell'Entità di Federazione incluso nel valore ``sub`` della Entity Configuration, rimuovendo ``https://`` e i path web.
      * - ``Email Address``
        - DEVE contenere l'email di contatto dell'organizzazione.
      * - ``organizationIdentifier``
        - DEVE contenere il numero di registrazione che identifica univocamente l'organizzazione nel servizio di registrazione, con OID ``2.5.4.97`` come definito in ``ITU-T X.500``.

2. **Subject Alternative Name (SAN)**: il certificato X.509 DEVE includere un ``SAN URI`` che DEVE corrispondere ai valori **sub** e **iss** della Entity Configuration di federazione.
3. **Nome DNS**: Il Certificato X.509 DEVE includere un Nome DNS nel SAN che corrisponde al nome DNS contenuto all'interno dei valori **sub** e **iss** della sua Entity Configuration, rimuovendo ``https://`` e qualsiasi path web.
4. **Certificate Revocation List (CRL)**: Se il Certificato X.509 emesso ha un tempo di scadenza superiore a 24 ore, l'Emittente X.509 DEVE pubblicare una CRL per i Certificati X.509 emessi. Questo elenco DEVE essere accessibile e regolarmente aggiornato per garantire che qualsiasi Certificato X.509 compromesso o non valido sia prontamente revocato con la motivazione della revoca, se presente.
5. **Basic Constraints**: Il Certificato X.509 DEVE includere un'estensione ``Basic Constraints`` con ``CA:TRUE`` e una lunghezza massima del path di 1 se l'emittente del certificato è un Intermediario di Federazione. Se è una Foglia, la lunghezza massima del path DEVE essere impostata a 0. Questo indica che il Subordinato a cui il certificato si riferisce, può emettere Certificati X.509 solo su se stesso. L'estensione ``BasicConstraints`` DEVE essere impostata ``critical``.
6. **Key Usage**: ``Digital Signature``, ``Key Encipherment``, ``Certificate Sign``, ``CRL Sign`` DEVONO essere inclusi. L'estensione ``KeyUsage`` DEVE essere impostata ``critical``.
7. **Name Constraints**: Il Certificato X.509 DEVE includere ``Name Constraints`` per specificare domini e URI permessi ed esclusi. Per esempio:

   - Permessi:
     - ``URI.1=https://leaf.example.com``
     - ``DNS.1=leaf.example.com``
   - Esclusi:
     - ``DNS=localhost``
     - ``DNS=localhost.localdomain``
     - ``DNS=127.0.0.1``
     - ``DNS=example.com``
     - ``DNS=example.org``
     - ``DNS=example.net``
     - ``DNS=*.example.org``

8. **AuthorityKeyIdentifier**: Il Certificato X.509 DEVE includere un'estensione ``AuthorityKeyIdentifier``. Il campo ``keyIdentifier`` dell'estensione ``AuthorityKeyIdentifier`` DEVE essere presente e DEVE essere identico al campo ``SubjectKeyIdentifier`` del certificato dell'emittente. Questo consolida la costruzione e validazione della catena di certificati.

Di seguito è riportato un esempio non normativo, in testo semplice (formato OpenSSL), di una catena di certificati X.509 con una CA intermedia, a partire dal certificato Foglia.

.. literalinclude:: ../../examples/x5c.json
  :language: text

Utilizzando il livello sottostante stabilito con OpenID Federation 1.0, tutti i certificati X.509 sono emessi in modo propriamente decentralizzato utilizzando il pattern di delegazione.


.. _trust-infrastructure-revoca-dei-certificati-x509:

Revoca di Certificati X.509
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Un Certificato X.509 può essere revocato dal suo Emittente.
Le liste di revoca, e/o qualsiasi altro meccanismo di controllo della revoca, sono particolarmente richieste per i Certificati X.509 con un tempo di scadenza superiore a 24 ore; altrimenti, non sono richieste.

Quando l'emittente del Certificato X.509 è la Foglia e quindi il Certificato X.509 si riferisce a se stesso, se il tempo di scadenza del certificato è superiore a 24 ore dal tempo ``X509_NOT_VALID_BEFORE``, DEVE implementare una CRL relativa al certificato emesso e mantenerla aggiornata.
Quando l'emittente del Certificato X.509 è un Superiore immediato, come il Trust Anchor o un Intermediario, e revoca il certificato relativo alla Foglia, cioè il Certificato X.509 relativo a una delle Chiavi dell'Entità di Federazione della Foglia, questa azione invalida l'intera Trust Chain associata a quella chiave pubblica crittografica della Foglia, rimuovendo effettivamente la sua capacità di emettere ulteriori Certificati X.509 su se stessa. Questo meccanismo di revoca gerarchico garantisce che qualsiasi compromissione o comportamento scorretto da parte di un'entità Foglia possa essere rapidamente affrontato.

Di seguito è riportato un esempio non normativo, in testo semplice, che illustra il contenuto di una CRL.

.. code-block:: text

    Certificate Revocation List (CRL):
    Version: 2 (0x1)
    Signature Algorithm: sha256WithRSAEncryption
    Issuer: CN=leaf.example.org, O=Leaf, C=IT
    Last Update: Sep 1 00:00:00 2023 GMT
    Next Update: Sep 8 00:00:00 2023 GMT
    Revoked Certificates:
        Serial Number: 987654320
            Revocation Date: Aug 25 12:00:00 2023 GMT
            CRL Entry Extensions:
                Reason Code: Key Compromise
        Serial Number: 987654321
            Revocation Date: Aug 30 15:00:00 2023 GMT
            CRL Entry Extensions:
                Reason Code: Cessation of Operation
    Signature Algorithm: sha256WithRSAEncryption
    Signature:
        5c:4f:3b:...


Federation Subordinate Events Endpoint
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

L'endpoint Federation Subordinate Events è definito in `OID-FED-SUBORDINATE-EVENTS`_. Questo endpoint fornisce un meccanismo che consente a Trust Anchor e Intermediari di pubblicare eventi storici relativi allo stato di registrazione dei loro Subordinati Immediati. Garantisce trasparenza e responsabilità nella federazione mantenendo un record storico completo degli eventi significativi che riguardano i partecipanti alla federazione.

Per i dettagli completi della specifica, inclusi posizione dell'endpoint, formato della richiesta, formato della risposta, claim JWT, parametri degli oggetti evento e tipi di evento supportati, fare riferimento a `OID-FED-SUBORDINATE-EVENTS`_.

Di seguito è riportato un esempio non normativo di richiesta e risposta dell'endpoint Federation Subordinate Events:

**Esempio di richiesta**:

.. code-block:: http

   GET /federation_subordinate_events_endpoint?sub=https%3A%2F%2Frp%2Eexample%2Eorg HTTP/1.1
   Host: immediate-superior.example.org

**Esempio di risposta**:

.. code-block:: json

   {
     "iss": "https://immediate-superior.example.org",
     "sub": "https://rp.example.org",
     "iat": 1590000000,
     "federation_registration_events": [
       {
         "iat": 1590000000,
         "event": "registration"
       },
       {
         "iat": 1590000000,
         "event": "jwks_update"
       },
       {
         "iat": 1600000000,
         "event": "revocation",
         "event_description": "compromised node"
       },
       {
         "iat": 1610000000,
         "event": "registration"
       }
     ]
   }

**Integrazione con la gestione del ciclo di vita delle entità**:

Questo endpoint integra le procedure di gestione del ciclo di vita delle entità definite in :ref:`entity-onboarding:Onboarding delle Entità` fornendo il tracciamento storico dettagliato di tutti gli eventi significativi che riguardano i partecipanti alla federazione. Supporta sia il monitoraggio automatico della conformità sia le audit manuali.

Osservazioni sulla Privacy
--------------------------

- Le Istanze del Wallet NON DEVONO pubblicare i loro metadati attraverso un servizio online.
- L'infrastruttura di trust DEVE essere pubblica, con tutti gli endpoint pubblicamente accessibili senza alcuna credenziale client che possa rivelare chi sta richiedendo l'accesso.
- Quando un'Istanza del Wallet richiede i Subordinate Statement per costruire la Trust Chain per un Relying Party specifico o valida un Trust Mark online, emesso per un Relying Party specifico, il Trust Anchor o il suo Intermediario non sanno che una particolare Istanza del Wallet sta indagando su un Relying Party specifico; invece, servono solo le dichiarazioni relative a quel Relying Party come risorsa pubblica.
- I metadati dell'Istanza del Wallet NON DEVONO contenere informazioni che possano rivelare informazioni tecniche sull'hardware utilizzato.
- I metadati dell'entità Foglia, Intermediario e Trust Anchor possono includere la quantità necessaria di dati come parte delle informazioni di contatto amministrative, tecniche e di sicurezza. Generalmente non è raccomandato utilizzare dettagli di contatto personali in tali casi. Dal punto di vista legale, la pubblicazione di tali informazioni è necessaria per il supporto operativo riguardante questioni tecniche e di sicurezza e la regolamentazione GDPR.


Considerazioni sulla Decentralizzazione
---------------------------------------

- Ci può essere più di un singolo Trust Anchor.
- In alcuni casi, un verificatore di trust può fidarsi di un Intermediario, specialmente quando l'Intermediario agisce come Trust Anchor all'interno di un perimetro specifico, come casi dove le Foglie sono entrambe nello stesso perimetro come una giurisdizione di Stato Membro (ad esempio: un Relying Party italiano con un'Istanza del Wallet italiana può considerare l'Intermediario italiano come Trust Anchor per gli scopi delle loro interazioni).
- Le attestazioni di trust (Trust Chain) dovrebbero essere incluse nei JWT emessi dai Credential Issuer, e le Richieste di Presentazione degli RP dovrebbero contenere la Trust Chain relativa a loro (emittenti delle richieste di presentazione).
- Poiché la presentazione delle credenziali deve essere firmata, memorizzando le richieste e risposte di presentazione firmate, che includono la Trust Chain, l'Istanza del Wallet può avere lo snapshot della configurazione di federazione (Entity Configuration del Trust Anchor nella Trust Chain) e l'affidabilità verificabile del Relying Party con cui ha interagito.
- Ogni attestazione firmata è di lunga durata poiché può essere validata crittograficamente anche quando la configurazione di federazione cambia o le chiavi dei suoi emittenti sono rinnovate.
- Ogni partecipante dovrebbe essere in grado di aggiornare la sua Entity Configuration senza notificare i cambiamenti a qualsiasi terza parte. La policy dei metadati contenuta all'interno di una Trust Chain deve essere applicata per sovrascrivere qualsiasi informazione relativa ai metadati specifici del protocollo.


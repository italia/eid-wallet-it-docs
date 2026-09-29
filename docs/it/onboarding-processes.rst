.. include:: ../common/common_definitions.rst
.. Included via onboarding-system.rst at title level '-' (level 1).

Onboarding Processes
--------------------

Questa parte fornisce la vista dinamica dell'onboarding.
Ciascun processo è descritto con il proprio Input, il proprio Outcome e il proprio Process, ossia la sequenza di passi.

I processi sono organizzati in tre famiglie.

- Il :ref:`onboarding-system:Entity Onboarding` copre la registrazione di un'entità e di una Fonte Autentica, e il loro aggiornamento, sospensione e rimozione.
- Il :ref:`onboarding-system:Certificate and Trust Artifact Issuance` copre l'emissione dei certificati e dei Trust Mark che un'entità ottiene.
- Il :ref:`onboarding-system:Attestation Onboarding` copre la registrazione dei claim, degli schema e dei tipi di Credenziale, e il ciclo di vita dei tipi di Credenziale.

Le Sezioni :ref:`onboarding-system:Process Dependency Map` e :ref:`onboarding-system:Notification and Publication` seguenti forniscono rispettivamente l'ordine dei processi e le dipendenze tra essi, e il processo di notifica delle entità che ne sono soggette.

Process Dependency Map
^^^^^^^^^^^^^^^^^^^^^^

Questa sezione mappa ogni processo di onboarding rispetto a quattro relazioni:

- **Preconditions** sono le condizioni che DEVONO sussistere prima che il processo possa essere eseguito. Includono il completamento di un altro processo e le condizioni esterne al Sistema di Onboarding, quali la certificazione di una Soluzione Wallet o lo status qualificato di un Qualified Trust Service Provider.
- **Started by** è chi o che cosa avvia il processo. Un processo è avviato da una parte esterna che lo richiede, oppure è invocato da un altro processo, oppure non ha una richiesta esplicita ed è una rivalutazione di condizioni.
- **Activates** sono i processi che si avviano come conseguenza di questo.
- **Enables** sono le capacità che diventano possibili in seguito, che non sono processi del Sistema di Onboarding.

I processi sono eseguiti dai componenti descritti in :ref:`onboarding-system:System Components and Services`, e viene fornita una tabella per ciascuna famiglia di :ref:`onboarding-system:Onboarding Processes`.

.. _table_map_entity:
.. list-table:: Process Map of the Entity Onboarding Processes
   :class: longtable
   :widths: 18 22 22 20 18
   :header-rows: 1

   * - **Process**
     - **Preconditions**
     - **Started by**
     - **Activates**
     - **Enables**
   * - :ref:`onboarding-system:Entity Registration`
     - Verifica di eleggibilità e conformità, compreso l'identity proofing e la verifica degli entitlement
     - L'Entità, che richiede la registrazione
     - Registration Trust Mark Issuance; Credential Type Activation and Deactivation, ``if it completes a versioned entry``
     - La richiesta, da parte dell'Entità, del WRPAC ``if EUDIW Trust Framework``, del Sign/Seal Certificate ``if National PKI``, e del National Authentication Certificate ``if Proximity Flow``; la :ref:`onboarding-system:Notification and Publication` dell'Entità, ``if notified category``, per la quale il Sistema di Onboarding mantiene le informazioni notificabili
   * - :ref:`onboarding-system:Entity Update`
     - :ref:`onboarding-system:Entity Registration`
     - L'Entità, che presenta una modifica di una o più categorie dei propri dati di registrazione
     - Registration Trust Mark Issuance, ove la modifica incida sui dati che reca; :ref:`onboarding-system:Wallet-Relying Party Registration Certificate Issuance`, ove la modifica incida su un Service o su un intended use
     - La richiesta, da parte dell'Entità, della riemissione dei certificati X.509 che recano i dati modificati; la revoca e la riemissione automatizzate del WRPRC da parte del relativo Provider; la ri-verifica dell'eleggibilità ove la modifica incida sull'Authorization Information; e la :ref:`onboarding-system:Notification and Publication` della modifica, ``if notified category``
   * - :ref:`onboarding-system:Entity Suspension and Removal`
     - :ref:`onboarding-system:Entity Registration`
     - L'autorità competente o l'Entità, che richiede una sospensione, una riattivazione o una cancellazione
     - Credential Type Activation and Deactivation, ``if Credential Issuer``
     - La :ref:`onboarding-system:Notification and Publication` del nuovo stato dell'Entità, ``if notified category``
   * - :ref:`onboarding-system:Authentic Source Registration`
     - Verifica di eleggibilità e conformità da parte dell'Organismo di Supervisione; la sottoscrizione della Fonte Autentica a PDND e la pubblicazione del proprio e-Service
     - La Fonte Autentica, che dichiara i propri dati di registrazione
     - Claim Registration, ``if a claim is missing``
     - La registrazione dei tipi di Credenziale che referenziano la Fonte Autentica come propria fonte dati
   * - :ref:`onboarding-system:Authentic Source Update`
     - :ref:`onboarding-system:Authentic Source Registration`
     - La Fonte Autentica, o la notifica tramite PDND della modifica di un e-Service
     - Credential Type Activation and Deactivation, ``if a type loses its data source``
     - —
   * - :ref:`onboarding-system:Authentic Source Removal`
     - :ref:`onboarding-system:Authentic Source Registration`
     - Una richiesta di rimozione
     - Credential Type Activation and Deactivation, ``if a type loses its data source``
     - —

.. _table_map_artifacts:
.. list-table:: Process Map of the Certificate and Trust Artifact Issuance Processes
   :class: longtable
   :widths: 18 22 22 20 18
   :header-rows: 1

   * - **Process**
     - **Preconditions**
     - **Started by**
     - **Activates**
     - **Enables**
   * - :ref:`onboarding-system:Wallet-Relying Party Access Certificate Issuance`
     - :ref:`onboarding-system:Entity Registration`, con un record dell'Entità nel Register, ``if EUDIW Trust Framework``
     - L'Entità, con un ordine ACME, per la prima emissione o per una riemissione
     - :ref:`onboarding-system:Wallet-Relying Party Registration Certificate Issuance`
     - L'autenticazione dell'Entità verso le Wallet Unit
   * - :ref:`onboarding-system:Wallet-Relying Party Registration Certificate Issuance`
     - :ref:`onboarding-system:Entity Registration`, con un record con uno stato di registrazione valido nel Register e un WRPAC valido del Service, ``if EUDIW Trust Framework``
     - Il Provider of WRPRC, invocato senza una richiesta dell'Entità quando esiste un WRPAC valido del Service o quando il record del Register di quel Service o intended use cambia
     - —
     - La presentazione dei dati di registrazione dell'Entità alle Wallet Unit
   * - :ref:`onboarding-system:Signature and Seal Certificate Issuance`
     - :ref:`onboarding-system:Entity Registration`, ``if National PKI``. Per un QEAA Provider e un PuB-EAA Provider il certificato è qualificato ed è emesso da un Qualified Trust Service Provider al di fuori di questo processo
     - L'Entità, con un ordine ACME, per la prima emissione o per una riemissione
     - —
     - La firma o il sigillo degli Attestati che l'Entità emette
   * - :ref:`onboarding-system:National Authentication Certificate Issuance`
     - :ref:`onboarding-system:Entity Registration`, ``if Proximity Flow``
     - L'Entità, con un ordine ACME, per la prima emissione o per una riemissione
     - —
     - L'autenticazione dell'Entità nel Proximity Flow
   * - :ref:`onboarding-system:Registration Trust Mark Issuance`
     - Il completamento della registrazione di federazione dell'Entità
     - Invocato dall'Entity Registration, e dall'Entity Update ove la modifica incida sui dati che il Trust Mark reca
     - —
     - Il riconoscimento dell'Entità come partecipante registrato del National Trust Framework, e la lettura dei suoi dati di autorizzazione ove non abbia un record nel Register

.. _table_map_attestation:
.. list-table:: Process Map of the Attestation Onboarding Processes
   :class: longtable
   :widths: 18 22 22 20 18
   :header-rows: 1

   * - **Process**
     - **Preconditions**
     - **Started by**
     - **Activates**
     - **Enables**
   * - :ref:`onboarding-system:Claim Registration`
     - —
     - Invocato dall'Authentic Source Registration, dallo Schema Provisioning o dal Credential Type Registration, ``if a claim is missing``
     - —
     - Lo Schema Provisioning e il Credential Type Registration che utilizzano il claim
   * - :ref:`onboarding-system:Schema Provisioning`
     - I claim che compongono lo schema sono disponibili nel Claims Registry
     - Invocato dal Credential Type Registration, ``if the schema is missing``
     - Claim Registration, ``if a claim is missing``
     - L'attivazione di un tipo di Credenziale, come una delle sue condizioni
   * - :ref:`onboarding-system:Credential Type Registration`
     - La definizione e la disponibilità dell'Attestation Rulebook applicabile; l'Authentic Source Registration, o un tipo di Credenziale padre, come fonte dati
     - L'Attestation Scheme Provider, che richiede la registrazione
     - Claim Registration, ``if a claim is missing``; Schema Provisioning, ``if the schema is missing``; Credential Type Activation and Deactivation
     - La dichiarazione del tipo di Credenziale da parte di un Credential Issuer in sede di Entity Registration
   * - :ref:`onboarding-system:Credential Type Activation and Deactivation`
     - :ref:`onboarding-system:Credential Type Registration`
     - Nessuna richiesta esplicita. La voce versionata è rivalutata ogni volta che una delle sue tre condizioni cambia
     - —
     - L'emissione del tipo di Credenziale da parte dei Credential Issuer elencati nella voce versionata
   * - :ref:`onboarding-system:Credential Type Update`
     - :ref:`onboarding-system:Credential Type Registration`
     - L'Attestation Scheme Provider, che pubblica una nuova versione
     - Credential Type Registration per la nuova voce versionata; Credential Type Activation and Deactivation
     - —

I processi che agiscono sul ciclo di vita di un'entità o di un tipo di Credenziale sono governati come descritto in :ref:`onboarding-system:Lifecycle Management`, e gli effetti di ciascun evento sui registri e sui Trust Artifact sono dati in :ref:`onboarding-system:Events, Registries and Trust Artifacts`.

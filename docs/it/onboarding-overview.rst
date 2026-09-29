.. include:: ../common/common_definitions.rst
.. Included via onboarding-system.rst at title level '-' (level 1).
 
Overview
--------
 
Questa Sezione introduce gli attori che partecipano all'onboarding, i componenti e i servizi del Sistema di Onboarding che li realizzano, e il modo in cui i due Trust Framework si combinano.
Fornisce al lettore il contesto necessario per seguire il modello di registrazione, i processi e il ciclo di vita descritti nelle Sezioni che seguono.
 
System Actors and Roles
^^^^^^^^^^^^^^^^^^^^^^^
 
Due famiglie di attori partecipano all'onboarding, le entità che vengono onboardate e le entità dell'infrastruttura di trust che operano l'onboarding stesso.
I ruoli dell'infrastruttura di trust sono realizzati dai componenti e dai servizi del Sistema di Onboarding, descritti nella sottosezione successiva.
 
**Entità oggetto di onboarding**
 
  - **Fonti Autentiche**: si onboardano per rendere i propri dati disponibili ai Credential Issuer, in modo che i dati possano essere inclusi negli Attestati.
  - **Wallet-Relying Parties**: si onboardano per essere autorizzate a fare affidamento sulle Wallet Unit e per ottenere i Trust Artifact di cui necessitano per operare. Sono ulteriormente suddivise in:
 
    - **Credential Issuer**, che si onboardano per essere autorizzati a emettere i tipi di Credenziale che dichiarano;
    - **Relying Party** e **Intermediari di Relying Party**, che si onboardano per essere autorizzati a richiedere attributi dell'Utente dalle Wallet Unit.
 
  - **Fornitori di Wallet**: si onboardano per far riconoscere la propria Soluzione Wallet nell'ecosistema e per essere notificati.
 
**Entità dell'infrastruttura di trust**
 
  - **Organismo di Supervisione**: durante l'onboarding verifica l'eleggibilità e la conformità delle entità, si avvale del Registrar per la registrazione tecnica e agisce come punto di contatto unico nazionale per la notifica alla Commissione Europea.
  - **Registrar** e **Register**: il Registrar esegue la registrazione tecnica delle Wallet-Relying Party e scrive i loro record nel **Register** come definito da [`CIR2025/848`_].
  - :term:`Provider of WRPAC` e :term:`Provider of WRPRC`: emettono, rispettivamente, il WRPAC e il WRPRC. Gli obblighi di Certificate Transparency del Provider of WRPAC sono definiti in :ref:`infrastructure-trust:Wallet-Relying Party Access Certificate (WRPAC) Profile`. L'emissione automatica del WRPRC è definita in :ref:`onboarding-system:Wallet-Relying Party Registration Certificate Issuance`.
  - **National Federation Authorities**: il **Federation Trust Anchor** e i suoi **Federation Intermediate**, che registrano le Entità di Federazione e applicano le metadata policy. Ciascuna Federation Authority emette i certificati X.509 e i Trust Mark per le Entità di Federazione che registra, mentre il Trust Mark di registrazione è emesso solo dal Federation Trust Anchor, come descritto in :ref:`infrastructure-trust:Trust Mark registration-entity`.
    In IT-Wallet il National Trust Anchor opera anche la Certification Authority radice della PKI nazionale di firma X.509, il cui certificato radice e la cui distribuzione sono descritti in :ref:`infrastructure-trust:PKI Architecture`.
 
**Entità che interagiscono con il Sistema di Onboarding senza essere onboardate**

  - **Attestation Scheme Provider**: possiedono l'Attestation Rulebook di un tipo di Credenziale e richiedono la registrazione della corrispondente voce versionata nel Digital Credentials Catalog, fornendo la definizione e lo schema tratti dal Rulebook, si veda :ref:`onboarding-system:Credential Type Registration`. Un Attestation Scheme Provider non è registrato come Entità per questo ruolo. All'interno di IT-Wallet il ruolo è ricoperto da un'organizzazione che possiede il Rulebook.

.. note::
   Una singola organizzazione PUÒ svolgere contemporaneamente diverse di queste funzioni.
 
Le Istanze del Wallet non sono Entità di Federazione e non sono onboardate direttamente.
Un'Istanza del Wallet è registrata indirettamente, tramite il proprio Fornitore di Wallet, si veda :ref:`wallet-instance-registration:Inizializzazione e Registrazione dell'Istanza del Wallet`, ed è ritenuta affidabile tramite una Wallet Instance Attestation emessa e firmata da tale Fornitore di Wallet, si veda :ref:`wallet-instance-attestation-issuance:Emissione della Wallet Instance Attestation`.
 
La notifica di un'entità notificata è un processo dello Stato membro definito da [`CIR2024/2980`_], descritto in :ref:`onboarding-system:Notification and Publication`.
 
System Components and Services
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 
I ruoli dell'infrastruttura di trust sono realizzati, all'interno del Sistema di Onboarding, da un insieme di componenti, ciascuno dei quali fornisce uno o più servizi.
Un'entità in onboarding interagisce con il sistema tramite un unico punto di ingresso, l'Onboarding UI, che orchestra il flusso e instrada ciascuna richiesta al componente responsabile, e che pertanto non è rappresentata come componente distinto nel diagramma seguente.

La tabella seguente elenca i componenti, i servizi che ciascuno di essi fornisce e il processo di onboarding che ciascun servizio realizza.
 
.. list-table:: Componenti, Servizi e Processi
   :class: longtable
   :widths: 24 30 46
   :header-rows: 1
 
   * - **Component**
     - **Services**
     - **Realized process**
   * - National Federation Management
     - Registrazione di federazione, emissione dei Trust Mark, pubblicazione dei registri firmati
     - :ref:`onboarding-system:Entity Registration`, :ref:`onboarding-system:Entity Update`, :ref:`onboarding-system:Entity Suspension and Removal`, :ref:`onboarding-system:Registration Trust Mark Issuance`
   * - EUDIW Registration Management
     - Verifica e registrazione delle Wallet-Relying Party nel Register
     - :ref:`onboarding-system:Entity Registration`, :ref:`onboarding-system:Entity Update`, :ref:`onboarding-system:Entity Suspension and Removal`
   * - Certificate Management
     - Emissione e aggiornamento di WRPAC, WRPRC, certificati Sign/Seal e National Authentication
     - :ref:`onboarding-system:Certificate and Trust Artifact Issuance`, :ref:`onboarding-system:Entity Update`
   * - Notification Dataset Management
     - Raccolta e mantenimento, nel dataset di notifica, delle informazioni oggetto di notifica
     - :ref:`onboarding-system:Entity Registration`, :ref:`onboarding-system:Entity Update`, :ref:`onboarding-system:Entity Suspension and Removal`
   * - Authentic Source Management
     - Registrazione, aggiornamento e rimozione delle Fonti Autentiche nell'AS Registry
     - :ref:`onboarding-system:Authentic Source Registration`, :ref:`onboarding-system:Authentic Source Update`, :ref:`onboarding-system:Authentic Source Removal`
   * - Claims and Schema Management
     - Registrazione dei claim e provisioning degli schema
     - :ref:`onboarding-system:Claim Registration`, :ref:`onboarding-system:Schema Provisioning`
   * - Catalog Management
     - Registrazione, attivazione e versionamento dei tipi di Credenziale nel Digital Credentials Catalog
     - :ref:`onboarding-system:Credential Type Registration`, :ref:`onboarding-system:Credential Type Activation and Deactivation`, :ref:`onboarding-system:Credential Type Update`

I componenti scrivono nei registri nazionali e negli store di dati descritti in :ref:`registry:Registry Infrastructure`, raggruppati per finalità come in :ref:`registry:Registries and Catalogues of the Ecosystem`.

Due store di dati sono mantenuti distinti di proposito, il Register, che contiene i record di registrazione delle Wallet-Relying Party definiti da [`CIR2025/848`_] e guida l'emissione dei certificati, e il dataset di notifica, che contiene le informazioni notificabili definite da [`CIR2024/2980`_].
Si sovrappongono solo nei dati di identificazione, così che la separazione mantiene distinta la registrazione dalla notifica.
 
Il diagramma seguente raggruppa i componenti per responsabilità e mostra gli store di dati con cui interagiscono.
Un componente può realizzare processi di più di una famiglia, quindi i gruppi del diagramma non coincidono con le famiglie di :ref:`onboarding-system:Onboarding Processes`, e la corrispondenza è quella data dalla tabella precedente.
Le Fonti Autentiche si registrano solo nell'AS Registry, senza un record nel Register e senza Trust Artifact, poiché non sono né Wallet-Relying Party né Entità di Federazione.
I Credential Issuer, invece, si registrano come Entità e dichiarano inoltre i tipi di Credenziale che emettono, e sono aggiunti agli issuer dei tipi che dichiarano nel Digital Credentials Catalog.

.. plantuml:: plantuml/onboarding-system-overview.puml
    :width: 99%
    :caption: `IT-Wallet Onboarding System. <https://www.plantuml.com/plantuml/svg/XLRVRzis47xNNt587WO4YRiiIz42Gr77iO4yh0ki37tn2osTPCxKKJXISxoX_tj9YX9OntOLm3_8--w-k_lkdC_62hPTe-3fvUQhK0ej_4LhBRYKL4E-DnQRJ65bmMfWMMyib9Ani59JPhQIMi6Y0RCHfTvvI2MKmUIcn4fqohxWgvqgMLE3PA5mByY9LIkAhQWnjtk5uDqBgbNgPigiTpEjDCFb-_0SNYuqsLp-Xt1xcrmfIMZtBO9ckz791UaI3RPm-o4vP45RV_ZxVN8uqddGN2974dVXISrqH-LCCo53whCKLgo5-GbQ55RpCPCibWOkpdJe0lxFCe3HT8crD9Q5xz8520FjjcQiuN9nx_-SDG2CYJd0rTMNO2mKBB347Wb_2dBkVCUkhbOqcQnegdumc9ELLgAvNb7UhRMd92n2ReKDC0E2IdZXpbZdZBScaAcmXClvtUAtnUDR7lE_7v--GapW58s-3ZTBL7jVX6V1dWNeDX2ZUaMIm6uGWhT8OC6YmPtcRI31M9ycCUqSsELMGAuxBl08XKEJFZLXcfeJlzz-QCiC7SzA5hv6JyPqWWeSsbEuktFzIR372h9ydiwkmRqjtLikQtgNer2-_2iQMpjo3WTGZ2uZ-zVxNp-U93-rpimUTcIWB-nvzah8fbT3Ncom4KToI6ncZAKdwZYRO1xu-Sz9UOz44LOeNH_ndJXqso2cwn8_rwqlEbOd6IBIPzDC8V3es1YqnzW8YxLcBrdJhV_18cnNUXElMvya5mT4OYXOY0MvrOnceEhtJiBLWHDuFn5jnwqsemIjFtIGyCJqODXVOqpa5UdAIwqFjUCspDB3m-DyyV06b6oBwVCJpAbijIJhLqRO7ljaMwpenBeu3F3j89qS6n5cqUDBQGhzB_B-C3-3pPdiXYbnevqF-sSVXph4dtsOlvzzF8c3gDztAueITqucr_0YNZNfPZzidRkVUahbQY2AUb1iYevrI5oa0bnHL6201dKvEOKdoCc12wMxCXrj1rfs2jTQnosv7Y7Hjj-eaLI7e2jmS9Rhpc9iO7hPZtjK9NQEsUWm-mLkt0CS0m9ZXOnKO3ZFNEp9v5DSBgDrePjM4r8O6UCL3xsvamdySNFpAUebyprpNwC-ix2Pmq5ePnPtYJi8JSaSi-6x-vYvsGkVGzd6u6By3sOdxIR-ma0nv6jw9b5gZdpCUCGd6nTa_07eCP5jMC6PV_6v3D8V3s8oeyEuCyHQENzKQMv24qSQWrUNJPPzHYgxHdq7>`_

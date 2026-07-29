.. include:: ../common/common_definitions.rst
.. Included via onboarding-system.rst at title level '-' (level 1).
 
Overview
--------
 
Questa Sezione introduce gli attori che partecipano all'onboarding, i componenti e i servizi del Sistema di Onboarding che li realizzano, e il modo in cui i due Trust Framework si combinano.
Fornisce al lettore il contesto necessario per seguire il registration model, i processi e il lifecycle descritti nelle Sezioni successive.
 
System Actors and Roles
^^^^^^^^^^^^^^^^^^^^^^^
 
Due famiglie di attori partecipano all'onboarding: le entità che vengono onboardate e le entità dell'infrastruttura di trust che operano l'onboarding stesso.
I ruoli dell'infrastruttura di trust sono realizzati dai componenti e dai servizi del Sistema di Onboarding, descritti nella sottosezione successiva.
 
**Entities being onboarded**
 
  - **Authentic Sources**: effettuano l'onboarding per rendere disponibili i propri dati ai Credential Issuer, affinché i dati possano essere inclusi nelle Attestation.
  - **Wallet-Relying Parties**: effettuano l'onboarding per essere autorizzate a fare affidamento sulle Wallet Unit e per ottenere i Trust Artifacts necessari a operare. Sono ulteriormente suddivise in:
 
    - **Credential Issuers**, che effettuano l'onboarding per essere autorizzati a emettere i Credential types che dichiarano;
    - **Relying Parties** e **Relying Party Intermediaries**, che effettuano l'onboarding per essere autorizzati a richiedere attributi User dalle Wallet Unit.
 
  - **Wallet Providers**: effettuano l'onboarding per far riconoscere la propria Wallet Solution nell'ecosistema e per essere notificati.
 
**Trust-infrastructure entities**
 
  - **Supervisory Body**: durante l'onboarding verifica l'idoneità e la conformità delle entità, si avvale del Registrar per la registrazione tecnica e agisce come single point of contact nazionale per la notifica alla Commissione europea.
  - **Registrar** e **Register**: il Registrar esegue la registrazione tecnica delle Wallet-Relying Party e scrive i relativi record nel **Register** come definito da [`CIR2025/848`_].
  - **Provider of WRPAC** e **Provider of WRPRC**: emettono, rispettivamente, il WRPAC e il WRPRC.
  - **National Federation Authorities**: il **Federation Trust Anchor** e i suoi **Federation Intermediates**, che registrano le Federation Entity e applicano le metadata policy. Ciascuna Federation Authority emette i certificati X.509 e i Trust Mark per le Federation Entity che registra, mentre il registration Trust Mark è emesso solo dal Federation Trust Anchor, come descritto in :ref:`infrastructure-trust:Trust Mark registration-entity`.
    Nell'IT-Wallet il National Trust Anchor opera anche la root Certification Authority della PKI X.509 nazionale di firma, il cui certificato root e la relativa distribuzione sono descritti in :ref:`infrastructure-trust:PKI Architecture`.
 
.. note::
   Una singola organizzazione può svolgere più di una di queste funzioni contemporaneamente.
 
Le Wallet Instance non sono Federation Entity e non vengono onboardate direttamente.
Una Wallet Instance è registrata indirettamente, tramite il proprio Wallet Provider, vedi :ref:`wallet-instance-registration:Inizializzazione e Registrazione dell'Istanza del Wallet`, ed è considerata affidabile tramite una Wallet Instance Attestation emessa e firmata da quel Wallet Provider, vedi :ref:`wallet-instance-attestation-issuance:Emissione della Wallet Instance Attestation`.
 
La notifica di un'entità notificata è un processo dello Stato membro definito da [`CIR2024/2980`_], descritto in :ref:`onboarding-system:Notification and Publication`.
 
System Components and Services
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 
I ruoli dell'infrastruttura di trust sono realizzati, all'interno del Sistema di Onboarding, da un insieme di componenti, ciascuno dei quali fornisce uno o più servizi.
Un'entità in onboarding interagisce con il sistema tramite un unico punto di ingresso, l'Onboarding UI, che orchestra il flusso e instrada ciascuna richiesta al componente responsabile, e che per questo non è mostrata come componente separato nel diagramma di seguito.
 
La tabella di seguito elenca i componenti, i servizi che ciascuno di essi fornisce e il processo di onboarding che ciascun servizio realizza.
 
.. list-table:: Components, Services and Processes
   :class: longtable
   :widths: 24 30 46
   :header-rows: 1
 
   * - **Component**
     - **Services**
     - **Realized process**
   * - Supervisory Body
     - Eligibility and compliance verification, approval of claims, schemas and Credential types
     - Precondition to every registration, see :ref:`onboarding-system:Eligibility and Compliance Preconditions`
   * - National Federation Management
     - Federation registration, issuance of Trust Marks, publication of the signed registries
     - :ref:`onboarding-system:Entity Registration`
   * - EUDIW Registration Management
     - Verification and registration of the Wallet-Relying Parties in the Register
     - :ref:`onboarding-system:Entity Registration`
   * - X.509 Certificate Management
     - Issuance and update of WRPAC, WRPRC, Sign/Seal and National Authentication certificates
     - :ref:`onboarding-system:Certificate and Trust Artifact Issuance`
   * - EU Notification Management
     - Signature of the EU Member State Trusted List and notification to the European Commission
     - :ref:`onboarding-system:Notification and Publication`
   * - Authentic Source Management
     - Registration of the Authentic Sources in the AS Registry
     - :ref:`onboarding-system:Authentic Source Registration`
   * - Claims and Schema Management
     - Registration of the claims and provisioning of the schemas
     - :ref:`onboarding-system:Attestation Onboarding`
   * - Catalog Management
     - Registration, activation and versioning of the Credential types in the Digital Credentials Catalog
     - :ref:`onboarding-system:Attestation Onboarding`
 
I componenti scrivono i registri nazionali e gli archivi dati descritti in :ref:`registry:Infrastruttura del Registro`, e interagiscono, a livello UE, con la Commissione europea per la notifica e l'allineamento dei Catalog.
Due archivi dati sono mantenuti separati di proposito: il Register, che contiene i record di registrazione delle Wallet-Relying Party definiti da [`CIR2025/848`_] e guida l'emissione dei certificati, e il notification dataset, che contiene le informazioni notificabili definite da [`CIR2024/2980`_] e alimenta il Publication Service.
Si sovrappongono solo nei dati identificativi, così la separazione mantiene distinta la registrazione dalla notifica.
 
Il diagramma di seguito mostra i componenti, gli attori che interagiscono con essi e gli archivi dati che scrivono.
Le Authentic Sources si registrano solo nell'AS Registry, senza record nel Register e senza Trust Artifacts, poiché non sono né Wallet-Relying Party né Federation Entity.
I Credential Issuer, invece, si registrano come Entity e dichiarano anche i Credential types che emettono, e vengono aggiunti agli issuer dei tipi che dichiarano nel Digital Credentials Catalog.

.. plantuml:: plantuml/onboarding-system-overview.puml
    :width: 99%
    :caption: `IT-Wallet Onboarding System. <https://www.plantuml.com/plantuml/svg/bLPHRnit37xNho3iXsr6x3RhqhLzA6exPo05rcLpXkp1B_8TVHQiamwIBeatzB-Fr9slYkEac0pO9v7yIF4ZUVxaWtIXgJHStOnlfTOOu7Upjj8LofImtFk0bT2u2H0iE5Lk0nJAOHwKDSBlbAcbanNuhIpiFPjifFQOI0hSo4Q76tm8KwrAKw49aDCNkaIhblbEbhWCUut0yDAKEeMPEcVlvrPR1yEtSHqB5zQ4fVe7uVmy4MbbCEnh1El2rYO2OmlqMCFvk-JGIRFZmrykqiD3E3Fh2dHT46_YIjLiOugvTGOTf9Y5378j_NUiPHwiEwKYeWG6owP6TwUyTNkOsM8_0Eb15XKCi_DPblqgH9T36Bn0vG3-5GAWLvs6W5G2p6QY7B7hNIb3WE7YWZza1xJwNC1WD9esOKj4gXoMjd4vZaQmCgFHRz8GDlCy6gtCPB8onug-3TvN9Trp_YvxEt__57skfQf8onImpBTOoVy9x_Fjo_Z4YxObWy19LArXxh1WP4dzuNs3heNEPNWC_VLHKZEo2FiJ-UJIVo6VNo8Fv6j1NbrBokcueWVLNNI3nVEtpFwwlBg5Fx5KFZmB-VIQPsIYzrmtrpGVoDFPogGdUxZY3gwmKDAHU6Li7KCckJBGUbrpHqZNbgh34eQpsMMsc9tW0id9Hb5Udo-YpxStiHZ-dboyVayjJmRK6cqA7lXek5XahsS_7-WuIWDyiPsBqpculhg4L_17DftIptKp6_FJjRDtgk1yh4pNKlrHIsgpxc-Lba2NSCfCZFcIQWsMrCSTPLGBF1QEYk4mAM1mg0HYUtaWh-ju7nEPqFtK2hhMURKoRUSmnEGCRkI3DRRg-NZp7PoqC3nq_N9eW6Ti8_DSAnmpkgXzx-fZzfyOF6A7q-KnH6F3WiJsgo1sSssRuj7q8fUDnhMrk_PsH4iMrq4tQnoLg2J5kQqgvJqPHLNCUrNn0unfWKzcxPfcBT0a92PP9dZaZiSV3-Fn0zWxAWPiYLwPahV6fshSzHy0wUMdrahpP8YQkQrghQJ9iVVhkYiGEHjqIABM9zrcCldOZPrUcm6iONHwDNikBlZntYcAzASkr3XWEOfODQARY7p0x8jkZF6U7WLpnCyjNO9BcxUHWBZZ633_vlzRqmBbiv5zl3oHs9JRieUD6z7b8wQcMGln2Kr1Vp_4Vm00>`_


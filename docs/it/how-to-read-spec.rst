.. include:: ../common/common_definitions.rst

Come leggere le Specifiche
--------------------------

Questa specifica è progettata per soddisfare i requisiti di molteplici stakeholder all'interno dell'ecosistema IT-Wallet. Ogni ruolo ha responsabilità e ambiti diversi e diverse esigenze informative. Questa sezione fornisce percorsi di lettura personalizzati per aiutare il lettore a navigare in modo efficiente verso i contenuti più rilevanti per gli obiettivi di implementazione.

Panoramica della Struttura delle Specifiche
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

La specifica è organizzata nelle seguenti sezioni principali:

**Sezione** :ref:`introduction:Introduzione`: 
  Stabilisce l'ambito e il linguaggio normativo per l'ecosistema IT-Wallet.

**Sezione** :ref:`architecture-overview:Panoramica dell'Architettura`:
  Fornisce una visione di alto livello dell'Architettura, in termini di governance e processi operativi abilitati.

**Sezione** :ref:`brand-identity:Brand Identity`:
  Fornisce i requisiti relativi alla Brand Identity del Sistema IT-Wallet, le indicazioni relative al naming e all'applicazione degli elementi visivi che identificano l'ecosistema.

**Sezione** :ref:`functionalities:Design dell'Esperienza Utente`: 
  Fornisce i principi di design e i requisiti funzionali di alto livello per garantire un’Esperienza Utente di qualità in tutte le fasi di interazione tra l’Utente e il servizio. 

**Sezione** :ref:`trust-infrastructure:L'Infrastruttura di Trust`:
  Definisce il modello di trust basato sulla federazione, le relazioni tra entità e i meccanismi di valutazione della fiducia che proteggono l'intero ecosistema.

**Sezione** :ref:`entities:Entità`: 
  Requisiti di implementazione completi per ogni partecipante all'ecosistema: Soluzioni Wallet, Fornitori di Credenziali, Relying Party e Fonti Autentiche, inclusi i loro componenti, modelli di interazione e requisiti di configurazione.

**Sezione** :ref:`digital-credential-management:Gestione degli Attestati Elettronici`: 
  Copre i modelli di dati e i formati delle Credenziali Elettroniche, la gestione del ciclo di vita, la verifica della validità e la struttura del catalogo delle Credenziali.

**Sezione** :ref:`digital-credential-flows:Flussi relativi agli Attestati Elettronici`:
  Guida dettagliata all'implementazione per i flussi di emissione e presentazione delle Credenziali Elettroniche, inclusi i flussi di interazione remota e di prossimità.

**Sezione** :ref:`endpoints:Endpoints`: 
  Specifiche tecniche per tutti gli endpoint API esposti da ciascun tipo di entità, inclusi gli endpoint di federazione e le integrazioni di servizi specializzati.

**Sezione** :ref:`algorithms:Algoritmi Crittografici`, :ref:`security-privacy-considerations:Considerazioni di Sicurezza e Privacy`, e :ref:`log-retention-policy:Politiche Generali di Conservazione dei Log` (**Supporto all'Implementazione**): 
  Requisiti crittografici, considerazioni sulla sicurezza e sulla privacy, e politiche di conservazione dei log essenziali per implementazioni conformi.

**Sezione** :ref:`defined-terms-and-references:Termini Definiti e Riferimenti`, :ref:`official-resources:Risorse Ufficiali`, :ref:`contribute:Come contribuire`, e :ref:`open-source:Rilasci Open Source` (**Terminologia e Riferimenti**):
  Terminologia completa, riferimenti normativi, documentazione, risorse e strumenti aggiuntivi, linee guida per i contributi.

**Sezione** :ref:`appendix:Appendice`: 
  Fornisce dettagli tecnici supplementari, modelli di implementazione e framework di test, inclusa la gestione delle istanze di applicazioni mobili, specifiche di integrazione della piattaforma nazionale e matrici di test complete per la validazione dell'ecosistema.


Lettura per ruolo
^^^^^^^^^^^^^^^^^

Lettura rapida per obiettivi  
""""""""""""""""""""""""""""


Lettura per fasi di progetto  
""""""""""""""""""""""""""""

Per un accesso semplificato agli argomenti di queste specifiche, di seguito viene presentato un percorso di lettura per ruoli che tiene conto della fase in cui si trovano a operare all’interno del sistema IT-Wallet con un rimando preciso alla sezione di interesse del documento. 
Fonte Autentica
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

La Fonte Autentica si occupa di rendere disponibili i dati affidabili alla base dei (Q)EAA e di garantirne e gestirne in modo sicuro l’assoluta accuratezza e integrità. 

**Fase 1: Scoperta**

Comprendere il funzionamento generale dell’ecosistema, l’architettura tecnica e l’Infrastruttura di Trust. 

- **Sezione** :ref:`introduction:Introduzione`: per comprendere l’ambito e il linguaggio normativo dell'ecosistema IT-Wallet. 

- **Sezione** :ref:`architecture-overview:Panoramica dell'Architettura`: per conoscere l’Architettura del sistema IT-Wallet, in termini di governance e processi operativi abilitati. 

- **Sezione** :ref:`trust-infrastructure:L'Infrastruttura di Trust`: per conoscere i requisiti chiave della Trust Chain e come essere registrati nella Trust List per poter operare sia a livello nazionale che europeo.  

- **Sezione** :ref:`defined-terms-and-references:Termini Definiti e Riferimenti`: per conoscere i riferimenti normativi, i termini definiti e gli standard tecnici per consentire un'interoperabilità sicura e corretta tra tutti i partecipanti (puoi ricorrere a questa sezione per ogni dubbio su terminologia, standard di riferimento, acronimi...) 
**Fase 2: Progettazione**

Comprendere i requisiti e progettare gli aspetti, le funzionalità e le caratteristiche specifiche del (Q)EAA da emettere. 


- **Sezione** :ref:`functionalities:Design dell'Esperienza Utente`: Requisiti chiave relativi alle modalità con cui consentire agli Utenti di ottenere i (Q)EAA, alla struttura dei (Q)EAA, al loro stato e alla loro gestione nel tempo.


**Sezione** :ref:`digital-credential-management:Gestione degli Attestati Elettronici`: Requisiti tecnici e funzionali relativi al ciclo di vita dei (Q)EAA. 

- **Sezione** :ref:`e-service-pdnd-template:PDND e-Service Template`: Modello di riferimento contenente tutti i metadati tecnici e descrittivi necessari per la definizione dell’e-service. 

**Fase 3: Implementazione**

Implementare le interfacce tecnologiche necessarie per comunicare con il Fornitore di Attestati Elettronici e gestire l’intero ciclo di vita dei dati associati ai (Q)EAA. 

- **Sezione** :ref:`authentic-sources:Fonti Autentiche`: Ruolo e responsabilità della Fonte Autentica. 
**Sezione** :ref:`e-service-pdnd:e-Service PDND`: Specifiche obbligatorie per l’integrazione con la PDND (Piattaforma Digitale Nazionale Dati) e relativi requisiti di interoperabilità per la pubblicazione di un e-service.

**Sezione** :ref:`authentic-source-endpoint:Endpoint delle Fonti Autentiche`: Requisiti chiave per l’implementazione delle API che consentono al Credential Issuer di recuperare in modo sicuro e coerente i dati autorevoli e di gestirne il ciclo di vita tramite gli endpoint del Signal Hub. 
- **Sezione** :ref:`registry infrastructure:Infrastruttura del Registro`: Approfondimento sui componenti del Registro di interesse per la Fonte Autentica. 

- **Sezione** :ref:`log-retention-policy:Politiche Generali di Conservazione dei Log`: Requisiti generali per la conservazione dei log e requisiti specifici per le Fonti Autentiche, in conformità alla norma ISO/IEC 27001. 
- **Sezione** :ref:`test-plans:Test Plans`: Guida alla configurazione dell’ambiente di test e alla validazione delle interazioni backend tramite l’utilizzo delle matrici di test fornite dall’ecosistema. 
**Fase 4: Registrazione**

Registrarsi al sistema come Fonte Autentica, completando le procedure amministrative e tecniche richieste. 

- **Sezione** :ref:`onboarding-high-level:Sistema di Onboarding`: Panoramica dell’architettura del sistema di onboarding e del processo di registrazione della Fonte Autentica. 

- **Sezione** :ref:`entity-onboarding:Onboarding delle Entità`: Approfondimento sulle procedure tecniche per la registrazione della Fonte Autentica. 

- **Sezione** :ref:`x5c-evaluation:Operazioni di Gestione dei Certificati X.509`: Procedure operative per la gestione dei certificati X.509 nell’ambito della federazione IT-Wallet. 


**Fornitore di Wallet**
~~~~~~~~~~~~~~~~~~~

Il Fornitore di Wallet si occupa della progettazione e dello sviluppo della Soluzione Wallet, che consente all’Utente di conservare, gestire e presentare il proprio PID e i propri (Q)EAA. 

**Fase 1: Scoperta**

Comprendere il funzionamento generale dell’ecosistema, l’architettura tecnica e l’Infrastruttura di Trust. 

- **Sezione** :ref:`introduction:Introduzione`: Scopo e contesto normativo del Sistema IT-Wallet.

- **Sezione** :ref:`architecture-overview:Panoramica dell'Architettura`: Panoramica dell’architettura del Sistema IT-Wallet in termini di governance e processi operativi abilitati. 

- **Sezione** :ref:`trust-infrastructure:L'Infrastruttura di Trust`: Requisiti chiave del modello di fiducia federato e dei meccanismi di valutazione della fiducia tra le entità.

- **Sezione** :ref:`defined-terms-and-references:Termini Definiti e Riferimenti`: Terminologia completa, riferimenti normativi, documentazione, risorse e strumenti aggiuntivi, linee guida per i contributi. 

**Fase 2: Progettazione**

Comprendere i requisiti relativi all’Esperienza Utente e progettare la Soluzione Wallet secondo modelli comuni, al fine di garantirne l’usabilità e l’accessibilità. 

- **Sezione** :ref:`brand-identity:Brand Identity`: Panoramica della Brand Identity del Sistema IT-Wallet e indicazioni sugli asset di riferimento per il Fornitore di Wallet.

- **Sezione** :ref:`functionalities:Design dell'Esperienza Utente`: Requisiti chiave relativi ai modelli di interazione, ai layout delle interfacce e agli asset grafici, al fine di garantire un’esperienza utente efficace, fluida e assicurare coerenza tra le diverse Soluzioni Wallet.

**Sezione** :ref:`digital-credential-management:Gestione degli Attestati Elettronici`: Gestione degli Attestati Elettronici: Requisiti tecnici e funzionali relativi al ciclo di vita dei (Q)EAA. 

**Fase 3: Implementazione**

Implementare la Soluzione Wallet in conformità a specifici standard tecnologici, al fine di garantire la comunicazione tra la Soluzione Wallet e gli altri attori del Sistema. 

- **Sezione** :ref:`wallet-solution:Soluzione Wallet`: Requisiti tecnici e funzionali relativi ai componenti, alle funzionalità e al ciclo di vita necessari per la configurazione della Soluzione Wallet. 

- **Sezione** :ref:`digital-credential-flows: Flussi relativi agli Attestati Elettronici`: Requisiti tecnici e funzionali relativi ai flussi di emissione e presentazione dei (Q)EAA.

- **Sezione** :ref:`wallet-provider-endpoint:Endpoint del Fornitore di Wallet`: Requisiti chiave per l’implementazione delle interfacce (API) del Fornitore di Wallet necessarie a garantire l’interoperabilità tra le entità. 

- **Sezione** :ref:`registry-infrastructure:Infrastruttura del Registro`: Approfondimento sui componenti del Registro. 

- **Sezione** :ref:`algorithms:Algoritmi Crittografici’: Selezione e implementazione degli standard crittografici necessari a garantire la sicurezza delle chiavi e delle transazioni. 

- **Sezione** :ref:`security-privacy-considerations:Considerazioni di Sicurezza e Privacy`: Requisiti di sicurezza e conformità per le Soluzioni Wallet. 

- **Sezione** :ref:`log-retention-policy:Politiche Generali di Conservazione dei Log`: Requisiti generali per la conservazione dei log e requisiti specifici per i Fornitori di Wallet, in conformità alla norma ISO/IEC 27001. 

- **Sezione** :ref:`mobile-application-instance: Istanza dell'Applicazione Mobile`: Requisiti relativi all’istanza dell’applicazione mobile, con riferimento alla richiesta e alla risposta di inizializzazione. 

- **Sezione** :ref:`test-plans:Test Plans`: Guida alla configurazione dell’ambiente di test e alla validazione delle interazioni backend tramite l’utilizzo delle matrici di test fornite dall’ecosistema. 

**Fase 4: Registrazione**

Registrarsi al sistema come Fornitore di Wallet, completando le procedure amministrative e tecniche richieste per il riconoscimento della Soluzione Wallet da parte del sistema. 

- **Sezione** :ref:`onboarding-high-level:Sistema di Onboarding`: Panoramica dell’architettura del sistema di onboarding e del processo di registrazione del Fornitore di Wallet.

- **Sezione** :ref:`entity-onboarding:Onboarding delle Entità`: Approfondimento sulle procedure tecniche per la registrazione del Fornitore di Wallet. 

- **Sezione** :ref:`x5c-evaluation:Operazioni di Gestione dei Certificati X.509`: Procedure operative per la gestione dei certificati X.509 nell’ambito della federazione IT-Wallet. 



Fornitore di Attestati Elettronici 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Il Fornitore di Attestati Elettronici si occupa di trasformare i dati autorevoli di origine provenienti dalle Fonti Autentiche in (Q)EAA e di gestirne l’intero ciclo di vita, dall’emissione alla revoca o alla scadenza. 

**Fase 1: Scoperta del sistema IT-Wallet**

**Obiettivo**: conoscere il contesto di riferimento, i requisiti tecnici e la normativa per entrare a far parte della Trust Chain (catena di fiducia) su cui si fonda tutto il sistema. 

- **Sezione** :ref:`introduction:Introduzione`: per comprendere l’ambito e il linguaggio normativo dell'ecosistema IT-Wallet. 

- **Sezione** :ref:`architecture-overview:Panoramica dell'Architettura`: per conoscere l’Architettura del sistema IT-Wallet, in termini di governance e processi operativi abilitati.  

- **Sezione** :ref:`trust-infrastructure:L'Infrastruttura di Trust`: per comprendere come il Credential Issuer viene riconosciuto nel sistema del Wallet come emittente autorizzato e come deve validare a sua volta le Fonti Autentiche.

- **Sezione** :ref:`defined-terms-and-references:Termini Definiti e Riferimenti`: per conoscere i riferimenti normativi, i termini definiti e gli standard tecnici per consentire un'interoperabilità sicura e corretta tra tutti i partecipanti (puoi ricorrere a questa sezione per ogni dubbio su terminologia, standard di riferimento, acronimi...).

**Fase 2: Design**

**Obiettivo**: progettare tecnicamente gli attestati strutturando i metadati affinché rispondano ai requisiti tecnici e normativi e permettano all'utente di condividere solo le informazioni necessarie. 

- **Sezione** :ref:`functionalities:Design dell'Esperienza Utente`: per conoscere i requisiti funzionali di alto livello a supporto dell’Esperienza Utente in tutte le fasi di interazione tra l’Utente e il servizio. 

- **Sezione** :ref:`entities:Entità`: per conoscere i requisiti di implementazione e gli attributi necessari per configurare il proprio profilo di Issuer (riferimento ai paragrafi :ref:`Soluzione del Fornitore di Attestati Elettronici` e :ref:`aFonti Autentiche`).

**Sezione** :ref:`digital-credential-management:Gestione degli Attestati Elettronici`:  per conoscere i requisiti tecnici necessari per la progettazione e gestione degli attestati e il loro ciclo di vita. 

**Sezione** :ref:`algorithms:Algoritmi Crittografici`: per rispondere ai requisiti di sicurezza progettando sistemi di firma digitale che rendano gli attestati non falsificabili.

**Fase 3: Implementazione**

Sviluppare endpoint secondo su specifici protocolli e implementare le funzionalità di emissione, rinnovo, revoca e tutte le altre funzioni tecniche di gestione del ciclo di vita dei (Q)EAA. 

- **Sezione** :ref:`credential-issuer-solution:Soluzione del Fornitore di Attestati Elettronici`: Requisiti tecnici e funzionali relativi ai componenti e ai modelli di interazione necessari per l’emissione e la gestione del ciclo di vita dei (Q)EAA. 

- **Sezione** :ref:`digital-credential-flows:Flussi relativi agli attestati elettronici`: Requisiti tecnici e funzionali relativi ai flussi di emissione e presentazione dei (Q)EAA.

- **Sezione** :ref:`credential-issuer-endopoint:Endpoint del Credential Issuer`: Requisiti chiave per l’implementazione dei metadati del Fornitore di Attestati Elettronici e degli endpoint di autorizzazione. 

- **Sezione** :ref:`algorithms:Algoritmi Crittografici’: Selezione e implementazione degli standard crittografici necessari a garantire la sicurezza delle chiavi e delle transazioni. 

- **Sezione** :ref:`e-service-pdnd:e-Service PDND’: Specifiche obbligatorie per l’integrazione con la PDND (Piattaforma Digitale Nazionale Dati) e relativi requisiti di interoperabilità per la pubblicazione di un e-service. 

- **Sezione** :ref:`security-privacy-considerations:Considerazioni di Sicurezza e Privacy`: Requisiti di sicurezza e conformità per le soluzioni implementate. 

- **Sezione** :ref:`log-retention-policy:Politiche Generali di Conservazione dei Log`: Requisiti generali per la conservazione dei log e requisiti specifici per i Fornitori di Attestati Elettronici, in conformità alla norma ISO/IEC 27001. 

- **Sezione** :ref:`test-plans:Test Plans`: Guida alla configurazione dell’ambiente di test e alla validazione delle interazioni backend tramite l’utilizzo delle matrici di test fornite dall’ecosistema. 

**Fase 4: Registrazione**

Registrarsi al sistema come Credential Issuer, completando le procedure amministrative e tecniche previste affinché i (Q)EAA emessi verso i Wallet siano riconosciuti come affidabili dal Sistema. 

- **Sezione** :ref:`onboarding-high-level:Sistema di Onboarding`: Panoramica dell’architettura del sistema di onboarding e del processo di registrazione della Fonte Autentica. 

- **Sezione** :ref:`Entity Onboarding:Onboarding delle Entità`: Approfondimento sulle procedure tecniche per la registrazione del Fornitore di Attestati Elettronici. 

- **Sezione** :ref:`x5c-evaluation:Operazioni di Gestione dei Certificati X.509`: Procedure operative per la gestione dei certificati X.509 nell’ambito della federazione IT-Wallet. 


Fornitori di servizi (Relying Party)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Fase 1: Scoperta*

Comprendere il funzionamento generale dell’ecosistema, l’architettura tecnica e l’Infrastruttura di Trust. 

- **Sezione** :ref:`introduction:Introduzione`: Scopo e contesto normativo del Sistema IT-Wallet.

- **Sezione** :ref:`architecture-overview:Panoramica dell'Architettura`: Panoramica dell’architettura del Sistema IT-Wallet in termini di governance e processi operativi abilitati. 

- **Sezione** :ref:`trust-infrastructure:L'Infrastruttura di Trust`: Requisiti chiave del modello di fiducia federato e dei meccanismi di valutazione della fiducia tra le entità.

- **Sezione** :ref:`defined-terms-and-references:Termini Definiti e Riferimenti`: Terminologia completa, riferimenti normativi, documentazione, risorse e strumenti aggiuntivi, linee guida per i contributi. 
**Fase 2: Progettazione**

Comprendere i requisiti di Esperienza Utente e progettare le funzionalità di verifica necessarie all’erogazione del servizio all’Utente finale. 

- **Sezione** :ref:`brand-identity:Brand Identity`: Panoramica della Brand Identity del Sistema IT-Wallet e indicazioni sugli asset da adottare da parte della Relying Party.

- **Sezione** :ref:`functionalities:Design dell'Esperienza Utente`: Requisiti chiave relativi ai modelli di interazione, ai layout delle interfacce e agli asset grafici, al fine di garantire un’esperienza utente efficace, fluida e assicurare coerenza tra i sistemi di presentazione e verifica. 


**Sezione** :ref:`digital-credential-management:Gestione degli Attestati Elettronici`: Gestione degli Attestati Elettronici: Requisiti tecnici e funzionali relativi al ciclo di vita dei (Q)EAA.


**Fase 3: Implementazione**

Implementare le funzionalità di verifica secondo specifici protocolli, al fine di inviare richieste di verifica al Wallet e ricevere una risposta con l’autorizzazione dell’Utente. 


- **Sezione** :ref:`relying-party-solution:Soluzione di Relying Party`: Requisiti tecnici e funzionali relativi ai componenti e alle funzionalità per la verifica del PID e dei (Q)EAA. 

- **Sezione** :ref:`digital-credential-flows:Flussi relativi agli Attestati Elettronici`: Requisiti tecnici e funzionali relativi ai flussi di emissione e presentazione dei (Q)EAA. 

- **Sezione** :ref:`relying-party-endpoint:Endpoint della Relying Party`: Requisiti chiave per l’implementazione degli endpoint di verifica dei (Q)EAA.

- **Sezione** :ref:`security-privacy-considerations:Considerazioni di Sicurezza e Privacy`: Requisiti di sicurezza e conformità per le soluzioni implementate. 

- **Sezione** :ref:`log-retention-policy:Politiche Generali di Conservazione dei Log`: Requisiti generali per la conservazione dei log e requisiti specifici per le Relying Party, in conformità alla norma ISO/IEC 27001. 

- **Sezione** :ref:`test-plans:Test Plans`: Guida alla configurazione dell’ambiente di test e alla validazione delle interazioni backend tramite l’utilizzo delle matrici di test fornite dall’ecosistema. 

**Fase 4: Registrazione**

Registrarsi al sistema come Relying Party, completando le procedure amministrative e tecniche previste, e diventare soggetto affidabile per la richiesta dei dati degli Utenti. 

- **Sezione** :ref:`onboarding-high-level:Sistema di Onboarding`: Approfondimento sulle procedure tecniche per la registrazione della Relying Party. 

- **Sezione** :ref:`entity Onboarding:Onboarding delle Entità`: Approfondimento sulle procedure tecniche per la registrazione della Relying Party. 

- **Sezione** :ref:`x5c-evaluation:Operazioni di Gestione dei Certificati X.509`: Procedure operative per la gestione dei certificati X.509 nell’ambito della federazione IT-Wallet. 



.. note::


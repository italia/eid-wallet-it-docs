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

Da usare quando si conosce già il compito da svolgere; le sezioni per ruolo sotto approfondiscono ciascun percorso.

**Fornitore di Wallet** — *Realizzare la Soluzione Wallet:* :ref:`wallet-solution:Soluzione Wallet`, :ref:`wallet-provider-endpoint:Endpoint del Fornitore di Wallet`; *far circolare gli attestati:* :ref:`digital-credential-flows:Flussi relativi agli Attestati Elettronici`; *federazione e crittografia:* :ref:`trust-infrastructure:L'Infrastruttura di Trust`, :ref:`algorithms:Algoritmi Crittografici`; *sicurezza e privacy:* :ref:`security-privacy-considerations:Considerazioni di Sicurezza e Privacy`.

**Credential Issuer** — *Emettere attestati:* :ref:`credential-issuer-solution:Soluzione del Fornitore di Attestati Elettronici`, :ref:`credential-issuance:Emissione di Attestati Elettronici`, :ref:`credential-issuer-endpoint:Endpoint del Credential Issuer`; *dati da Fonti Autentiche:* :ref:`authentic-sources:Fonti Autentiche`; *se si autentica l'Utente:* :ref:`credential-presentation:Presentazione dell'Attestato Elettronico`; *sicurezza:* :ref:`security-privacy-considerations:Considerazioni di Sicurezza e Privacy`.

**Fonte Autentica** — *Erogare dati autorevoli:* :ref:`authentic-sources:Fonti Autentiche`, :ref:`authentic-source-endpoint:Endpoint delle Fonti Autentiche`; *integrità e piattaforme nazionali:* :ref:`algorithms:Algoritmi Crittografici`, :ref:`e-service-pdnd:e-Service PDND`.

**Relying Party** — *Verificare le credenziali presentate:* :ref:`relying-party-solution:Soluzione di Relying Party`, :ref:`credential-presentation:Presentazione dell'Attestato Elettronico`, :ref:`relying-party-endpoints:Endpoint della Relying Party`; *formati e validità:* :ref:`digital-credential-management:Gestione degli Attestati Elettronici`; *sicurezza:* :ref:`security-privacy-considerations:Considerazioni di Sicurezza e Privacy`.


Lettura per fasi di progetto  
""""""""""""""""""""""""""""

Per un accesso semplificato agli argomenti di queste specifiche, di seguito viene presentato un percorso di lettura per ruoli che tiene conto della fase in cui si trovano a operare all’interno del sistema IT-Wallet con un rimando preciso alla sezione di interesse del documento. 

Fonti Autentiche (Authentic Source)  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

L’Authentic Source è il proprietario del dato. Il suo ruolo è garantire che le informazioni originali siano trasmesse correttamente e rese disponibili ai sistemi di emissione in modo sicuro e sempre aggiornato.  
**Focus**: disponibilità del dato, correttezza delle informazioni trasmesse, allineamento costante tra il database originale e le credenziali emesse.  

**Fase 1: Scoperta del sistema IT-Wallet**

**Obiettivo**: conoscere il contesto di riferimento, i requisiti tecnici e la normativa per entrare a far parte della Trust Chain (catena di fiducia) su cui si fonda tutto il sistema.  

- **Sezione** :ref:`introduction:Introduzione`: per comprendere l’ambito e il linguaggio normativo dell'ecosistema IT-Wallet. 

- **Sezione** :ref:`architecture-overview:Panoramica dell'Architettura`: per conoscere l’Architettura del sistema IT-Wallet, in termini di governance e processi operativi abilitati. 

- **Sezione** :ref:`trust-infrastructure:L'Infrastruttura di Trust`: per conoscere i requisiti chiave della Trust Chain e come essere registrati nella Trust List per poter operare sia a livello nazionale che europeo.  

- **Sezione** :ref:`defined-terms-and-references:Termini Definiti e Riferimenti`: per conoscere i riferimenti normativi, i termini definiti e gli standard tecnici per consentire un'interoperabilità sicura e corretta tra tutti i partecipanti (puoi ricorrere a questa sezione per ogni dubbio su terminologia, standard di riferimento, acronimi...) 

**Fase 2: Design**

**Obiettivo**: conoscere i requisiti di implementazione degli attributi ritenuti necessari per tradurre i dati in un formato digitale standardizzato (EAA) riconosciuto dal Wallet.  


- **Sezione** :ref:`functionalities:Design dell'Esperienza Utente`: per conoscere le modalità di ottenimento degli Attestati Elettronici da parte dell’utente (riferimento al paragrafo :ref:`functionalities:Ottenimento degli Attestati Elettronici di Attributi`). 

- **Sezione** :ref:`entities:Entità`: per conoscere i requisiti di implementazione e in particolare gli attributi necessari per fornire l'Attestato Elettronico richiesto dall'Utente (riferimento a paragrafo :ref:`authentic-sources:Fonti Autentiche`) 

**Sezione** :ref:`digital-credential-management:Gestione degli Attestati Elettronici`:  per conoscere come i dati autorevoli e gli attributi diventano Credenziali Elettroniche e in cosa consiste il loro ciclo di vita.

**Fase 3: Implementazione**

**Obiettivo**: adottare i requisiti che servono a realizzare le interfacce tecnologiche (API) necessarie per dialogare con i Credential Issuer gestendo l'intero ciclo di vita del dato. 

- **Sezione** :ref:`endpoints:Endpoint`: per implementare correttamente le interfacce (API) che permettono al Credential Issuer di recuperare i dati autorevoli in modo sicuro e standardizzato (riferimento a paragrafo :ref:`endpoints:Endpoint delle Fonti Autentiche`) 

- **Sezione** :ref:`digital-credential-management:Gestione degli Attestati Elettronici`: per conoscere nello specifico il ciclo di vita e la gestione degli Attestati elettronici (riferimento al paragrafo :ref:`cdigital-credential-management:Ciclo di vita degli Attestati Elettronici`) 

- **Sezione** :ref:`security-privacy-considerations:Considerazioni di Sicurezza e Privacy` per implementare soluzioni che rispettino tutti i parametri di sicurezza  

- **Sezione** :ref:`log-retention-policy:Politiche Generali di Conservazione dei Log`: per implementare soluzioni che rispettino i parametri di sicurezza e i requisiti definiti nella norma ISO/IEC 27001 

**Fase 4: Registrazione**

**Obiettivo**: accreditarsi come Fonte Autentica nel sistema rispettando le procedure amministrative e tecniche che garantiscono sull’affidabilità dell'ente. 

- **Sezione** :ref:`onboarding-high-level:Sistema di Onboarding`: per conoscere le modalità di partecipazione all’ecosistema IT-Wallet e tutto ciò che riguarda la riconoscibilità dei propri dati da parte di tutti gli attori (riferimento al paragrafo :ref:`onboarding-high-level:Processo di registrazione della Fonte Autentica`).  

- **Sezione** :ref:`x5c-evaluation:Operazioni di Gestione dei Certificati X.509`: per conoscere le procedure operative per la gestione dei Certificati X.509 all'interno della federazione IT-Wallet. 


**Wallet Provider**
~~~~~~~~~~~~~~~~~~~

Il Wallet Provider è colui che progetta il portafoglio digitale, pubblico o privato. Funge da punto di contatto diretto con il cittadino e la sua sfida consiste nel coniugare un'esperienza utente fluida e intuitiva con i più alti standard di sicurezza. 
**Focus**: rispetto dei protocolli e degli standard di sicurezza, fluidità dell’esperienza utente, rispetto delle linee guida del sistema IT-Wallet. 

**Fase 1: Scoperta del sistema IT-Wallet**

**Obiettivo:** conoscere il contesto di riferimento, i requisiti tecnici e la normativa per entrare a far parte della Trust Chain (catena di fiducia) su cui si fonda tutto il sistema. 

- **Sezione** :ref:`introduction:Introduzione`: per comprendere l’ambito e il linguaggio normativo dell'ecosistema IT-Wallet. 

- **Sezione** :ref:`architecture-overview:Panoramica dell'Architettura`: per conoscere l’Architettura del sistema IT-Wallet, in termini di governance e processi operativi abilitati.  

- **Sezione** :ref:`trust-infrastructure:L'Infrastruttura di Trust`: per comprendere il funzionamento della Trust Chain e capire come validare gli attestati delle Fonti Autentiche (AS) e degli Issuer (CI). 

- **Sezione** :ref:`defined-terms-and-references:Termini Definiti e Riferimenti`: per conoscere i riferimenti normativi, i termini definiti e gli standard tecnici per consentire un'interoperabilità sicura e corretta tra tutti i partecipanti (puoi ricorrere a questa sezione per ogni dubbio su terminologia, standard di riferimento, acronimi...). 

**Fase 2: Design**

**Obiettivo**: definire l'identità visiva del Wallet, progettare l’esperienza utente, modellare l'entità tecnica e scegliere gli algoritmi crittografici che garantiranno la protezione dei dati sul dispositivo. 

- **Sezione** :ref:`brand-identity:Brand Identity`: per garantire che l'App rispetti le linee guida di comunicazione e l'identità visiva del sistema IT-Wallet.  

- **Sezione** :ref:`functionalities:Design dell'Esperienza Utente`: per progettare interfacce semplici e sicure garantendo che l’esperienza utente sia immediata e intuitiva. 

- **Sezione** :ref:`entities:Entità`: per conoscere i requisiti di implementazione e gli attributi necessari per configurare la propria entità (riferimento al paragrafo :ref:`entities:Soluzione Wallet`). 

**Sezione** :ref:`digital-credential-management:Gestione degli Attestati Elettronici`: per progettare come l'App gestirà tecnicamente il ciclo di vita dei dati (archiviazione protetta e presentazione). 

**Sezione** :ref:`algorithms:Algoritmi Crittografici`: per selezionare e progettare l'implementazione degli standard crittografici necessari alla messa in sicurezza delle chiavi e delle transazioni. 

**Fase 3: Implementazione**

**Obiettivo**: implementare gli endpoint per la comunicazione e adottare gli standard tecnologici (es. SD-JWT) che assicurano al Wallet di interfacciarsi con gli altri attori.

- **Sezione** ref:`endpoints:Endpoints`: per implementare correttamente le interfacce (API) del Wallet Provider necessarie all'interoperabilità del sistema (riferimento al paragrafo ref:`endpoints:Endpoint del Fornitore di Wallet`). 

- **Sezione** :ref:`security-privacy-considerations:Considerazioni di Sicurezza e Privacy`: per implementare soluzioni che rispettino tutti i parametri di sicurezza.  

- **Sezione** :ref:`log-retention-policy:Politiche Generali di Conservazione dei Log`: per implementare soluzioni che rispettino i parametri di sicurezza e i requisiti definiti nella norma ISO/IEC 27001.

**Fase 4: Registrazione**

**Obiettivo**: accreditarsi come Wallet Provider nel sistema in modo tale che le Wallet Instance dei cittadini siano riconosciute come valide dal sistema.  

- **Sezione** :ref:`onboarding-high-level:Sistema di Onboarding`: per conoscere le modalità di partecipazione all’ecosistema IT-Wallet e tutto ciò che riguarda la riconoscibilità dei propri dati da parte di tutti gli attori (riferimento al paragrafo :ref:`onboarding-high-level:Journey dell'Operatore del Fornitore di Wallet`).  

- **Sezione** :ref:`x5c-evaluation:Operazioni di Gestione dei Certificati X.509`: per conoscere le procedure operative per la gestione dei Certificati X.509 all'interno della federazione IT-Wallet. 

- **Sezione** :ref:`test-plans:Test Plans`: per avere informazioni in merito a come gli ambienti di test possono supportare implementatori, auditor e ambienti di test di conformità nella validazione del comportamento delle Soluzioni Wallet.


Fornitori di Credenziali (Credential Issuer)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Il Credential Issuer è il fornitore tecnico delle credenziali. Il suo compito principale è trasformare i dati ricevuti dalle Fonti Autentiche in attestati digitali sicuri, pronti per essere emessi verso il Wallet. È il fulcro tecnico che garantisce l'interoperabilità attraverso l'uso di standard internazionali come OpenID4VCI. 
**Focus**: progettazione delle credenziali a partire dal dato grezzo, sicurezza del dato ottenuto, ciclo di vita delle credenziali. 

**Fase 1: Scoperta del sistema IT-Wallet**

**Obiettivo**: conoscere il contesto di riferimento, i requisiti tecnici e la normativa per entrare a far parte della Trust Chain (catena di fiducia) su cui si fonda tutto il sistema. 

- **Sezione** :ref:`introduction:Introduzione`: per comprendere l’ambito e il linguaggio normativo dell'ecosistema IT-Wallet. 

- **Sezione** :ref:`architecture-overview:Panoramica dell'Architettura`: per conoscere l’Architettura del sistema IT-Wallet, in termini di governance e processi operativi abilitati.  

- **Sezione** :ref:`trust-infrastructure:L'Infrastruttura di Trust`: per comprendere come il Credential Issuer viene riconosciuto nel sistema del Wallet come emittente autorizzato e come deve validare a sua volta le Fonti Autentiche.

- **Sezione** :ref:`defined-terms-and-references:Termini Definiti e Riferimenti`: per conoscere i riferimenti normativi, i termini definiti e gli standard tecnici per consentire un'interoperabilità sicura e corretta tra tutti i partecipanti (puoi ricorrere a questa sezione per ogni dubbio su terminologia, standard di riferimento, acronimi...).

**Fase 2: Design**

**Obiettivo**: progettare tecnicamente gli attestati strutturando i metadati affinché rispondano ai requisiti tecnici e normativi e permettano all'utente di condividere solo le informazioni necessarie. 

- **Sezione** :ref:`functionalities:Design dell'Esperienza Utente`: per conoscere i requisiti funzionali di alto livello a supporto dell’Esperienza Utente in tutte le fasi di interazione tra l’Utente e il servizio. 

- **Sezione** :ref:`entities:Entità`: per conoscere i requisiti di implementazione e gli attributi necessari per configurare il proprio profilo di Issuer (riferimento ai paragrafi :ref:`entities:Soluzione del Fornitore di Attestati Elettronici` e :ref:`aentities:Fonti Autentiche`).

**Sezione** :ref:`digital-credential-management:Gestione degli Attestati Elettronici`:  per conoscere i requisiti tecnici necessari per la progettazione e gestione degli attestati e il loro ciclo di vita. 

**Sezione** :ref:`algorithms:Algoritmi Crittografici`: per rispondere ai requisiti di sicurezza progettando sistemi di firma digitale che rendano gli attestati non falsificabili.

**Fase 3: Implementazione**

**Obiettivo**: sviluppare gli endpoint di emissione in base al protocollo OpenID4VCI, implementando le funzioni di rilascio, rinnovo e gestione tecnica del ciclo di vita della credenziale.

- **Sezione** ref:`digital-credential-flows:Flussi relativi agli attestati elettronici`: per conoscere le specifiche di dettaglio per implementare i flussi di emissione, le modalità di presentazione dell’attestato elettronico e il flusso di recupero delle informazioni del wallet. 

- **Sezione** ref:`endpoints:Endpoints`: per implementare correttamente le interfacce (API) di emissione, in particolare il Credential Endpoint e il Token Endpoint  (riferimento al paragrafo ref:`endpoints:Endpoint del Credential Issuer`). 

- **Sezione** :ref:`security-privacy-considerations:Considerazioni di Sicurezza e Privacy`: per implementare soluzioni che rispettino tutti i parametri di sicurezza.  

- **Sezione** :ref:`log-retention-policy:Politiche Generali di Conservazione dei Log`: per implementare soluzioni che rispettino i parametri di sicurezza e i requisiti definiti nella norma ISO/IEC 27001.

**Fase 4: Registrazione**

**Obiettivo**: accreditarsi nel sistema in modo tale che gli attestati emessi verso il Wallet risultino ufficialmente “fidati” e verificabili. 

- **Sezione** :ref:`onboarding-high-level:Sistema di Onboarding`: per conoscere le modalità di partecipazione all’ecosistema IT-Wallet  (riferimento al paragrafo :ref:`onboarding-high-level:Journey dell'Operatore del Credential Issuer`).  

- **Sezione** :ref:`x5c-evaluation:Operazioni di Gestione dei Certificati X.509`: per conoscere le procedure operative per la gestione dei Certificati X.509 all'interno della federazione IT-Wallet. 

- **Sezione** :ref:`test-plans:Test Plans`: per avere informazioni in merito a come gli ambienti di test possono supportare implementatori, auditor e ambienti di test di conformità nella validazione del comportamento delle Soluzioni Wallet.


Fornitori di servizi (Relying Party)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Il Relying Party è l'utilizzatore finale delle credenziali. Il suo compito è trasformare la verifica digitale in un valore aggiunto per il proprio business, garantendo al contempo all'utente un processo di identificazione rapido, sicuro e rispettoso della minimizzazione dei dati richiesti. 
**Focus**: progettazione dell’esperienza di verifica delle credenziali, rispetto della privacy dell’utente  

**Fase 1: Scoperta del sistema IT-Wallet**

**Obiettivo**: conoscere il contesto di riferimento, i requisiti tecnici e la normativa per entrare a far parte della Trust Chain (catena di fiducia) su cui si fonda tutto il sistema.

- **Sezione** :ref:`introduction:Introduzione`: per comprendere l’ambito e il linguaggio normativo dell'ecosistema IT-Wallet. 

- **Sezione** :ref:`architecture-overview:Panoramica dell'Architettura`: per conoscere l’Architettura del sistema IT-Wallet, in termini di governance e processi operativi abilitati.   

- **Sezione** :ref:`trust-infrastructure:L'Infrastruttura di Trust`: per capire come verificare che la credenziale presentata dall'utente provenga da una Fonte Autentica certificata.

- **Sezione** :ref:`defined-terms-and-references:Termini Definiti e Riferimenti`: per conoscere i riferimenti normativi, i termini definiti e gli standard tecnici per consentire un'interoperabilità sicura e corretta tra tutti i partecipanti (puoi ricorrere a questa sezione per ogni dubbio su terminologia, standard di riferimento, acronimi...).

**Fase 2: Design**

**Obiettivo**: definire i requisiti di verifica, stabilendo gli attributi necessari per erogare il servizio; progettare l'esperienza di richiesta, definendo le modalità di condivisione dei dati. 

- **Sezione** :ref:`brand-identity:Brand Identity`: per garantire che le eventuali app di verifica rispettino le linee guida di comunicazione e l'identità visiva del sistema IT-Wallet.  

- **Sezione** :ref:`functionalities:Design dell'Esperienza Utente`: per conoscere i requisiti funzionali di alto livello a supporto dell’Esperienza Utente in tutte le fasi di interazione tra l’Utente e il servizio.  

- **Sezione** :ref:`entities:Entità`: per conoscere i requisiti di implementazione e gli attributi necessari per configurare il profilo del Verificatore (riferimento al paragrafo :ref:`entities:Soluzione di Relying Party`). 

**Sezione** :ref:`digital-credential-management:Gestione degli Attestati Elettronici`: per comprendere quali sono i formati delle Credenziali Elettroniche e verifica della validità. 

**Sezione** :ref:`algorithms:Algoritmi Crittografici`: per progettare i sistemi di validazione delle firme digitali che "sigillano" i dati presentati dall'utente. 

**Fase 3: Implementazione**

**Obiettivo**: implementare il protocollo OpenID4VP per inviare le richieste al Wallet e ricevere gli attestati, assicurando la corretta decodifica dei formati. 

- **Sezione** ref:`digital-credential-flows:Flussi relativi agli attestati elettronici`: per l’implementazione del flusso di presentazione sia per scenari remoti che di prossimità (ref:`dcredential-presentation:12.2`. 

- **Sezione** ref:`endpoints:Endpoints`: per implementare correttamente le interfacce di ricezione e verifica dei dati (riferimento ai paragrafi ref:`endpoints:Endpoint della Relying Party` e ref:`endpoints:Endpoint del Backend del Provider di Relying Party`). 

- **Sezione** :ref:`security-privacy-considerations:Considerazioni di Sicurezza e Privacy`: per implementare soluzioni che rispettino tutti i parametri di sicurezza.  

- **Sezione** :ref:`log-retention-policy:Politiche Generali di Conservazione dei Log`: per implementare soluzioni che rispettino i parametri di sicurezza e i requisiti definiti nella norma ISO/IEC 27001.

**Fase 4: Registrazione**

**Obiettivo**: accreditarsi nel sistema in modo tale da essere riconosciuti come attore sicuro e affidabile nel momento della richiesta dei dati dell’utente.  

- **Sezione** :ref:`onboarding-high-level:Sistema di Onboarding`: per conoscere le modalità di partecipazione all’ecosistema IT-Wallet (riferimento al paragrafo :ref:`onboarding-high-level:Journey dell'Operatore della Relying Party`).  

- **Sezione** :ref:`x5c-evaluation:Operazioni di Gestione dei Certificati X.509`: per conoscere le procedure operative per la gestione dei Certificati X.509 all'interno della federazione IT-Wallet. 

- **Sezione** :ref:`test-plans:Test Plans`: per avere informazioni in merito a come gli ambienti di test possono supportare implementatori, auditor e ambienti di test di conformità nella validazione del comportamento delle Soluzioni Wallet.


.. note::

    Per gli implementatori che lavorano su soluzioni che coprono più ruoli (ad esempio, una combinazione di Soluzioni di Fornitore di Credenziali e Relying Party), si raccomanda di rivedere le sezioni per tutti i ruoli pertinenti prima di procedere con gli sviluppi. È importante prestare particolare attenzione ai requisiti di Entity Configuration e ai flussi di federazione che si applicano a più ruoli.

.. include:: ../common/common_definitions.rst


Politiche Generali di Conservazione dei Log
===========================================

La conservazione dei log è un elemento chiave per garantire la sicurezza, inclusa la prevenzione delle frodi, il rilevamento degli incidenti, l'integrità del sistema e la conformità con gli obblighi legali applicabili. DEVE anche essere allineata con i requisiti definiti nella norma ISO/IEC 27001, in particolare per quanto riguarda la verificabilità, il controllo degli accessi e l'archiviazione sicura. Poiché la gestione dei log può comportare il trattamento di dati personali, costituisce anche una misura di responsabilizzazione ai sensi del GDPR, con implicazioni per la minimizzazione dei dati, la limitazione della conservazione e la limitazione delle finalità; per questi aspetti, si fa riferimento alle disposizioni pertinenti del GDPR e alle normative specifiche del settore.

Per tutto ciò che riguarda la gestione dei log, i Fornitori di Wallet, i Fornitori di Credenziale e le Relying Party sono considerati Entità Organizzative.

I log relativi alle attività di scambio dati del Wallet (accessi, transazioni, emissione/revoca di Credenziali) riguardanti l'Utente, in quanto interessato, DEVONO essere conservati per un periodo limitato per motivi di sicurezza, prevenzione delle frodi, risoluzione delle controversie e obblighi legali.

Le Entità Organizzative sono responsabili della conservazione dei log in base ai rispettivi ruoli. Le soluzioni relative ai Fornitori di Wallet, ai Fornitori di Credenziale e alle Relying Party DEVONO implementare la registrazione di audit per le attività degli amministratori e degli operatori di servizio con accesso ai processi di scambio dati e ai log.

A meno che specifici obblighi legali non dispongano diversamente, e con la definizione di normative specifiche di settore che definiscano motivazioni appropriate, **il periodo massimo di conservazione per i log dei dati è di 12 mesi**. I log DEVONO essere archiviati in modo sicuro per garantirne l'integrità e l'immutabilità.

Requisiti Generali di Logging ISO/IEC 27001
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Le Entità Organizzative DEVONO implementare misure tecniche e organizzative appropriate in conformità con ISO/IEC 27001 per mantenere un sistema di gestione della sicurezza delle informazioni per il monitoraggio, l'audit e la risposta agli incidenti. Gli aspetti chiave della gestione dei log secondo ISO/IEC 27001 includono i seguenti requisiti:

- **A.12.4 Logging e Monitoraggio**: Le Entità Organizzative DEVONO produrre log che registrino eccezioni, guasti ed eventi di sicurezza delle informazioni. Quando necessario per motivi di sicurezza, i log DOVREBBERO acquisire le attività degli utenti con un livello di dettaglio appropriato e sufficiente per soddisfare i requisiti di sicurezza, assicurando che i dati raccolti siano pertinenti e non eccessivi. I log DOVREBBERO essere rivisti regolarmente per garantire che gli incidenti di sicurezza siano identificati e affrontati tempestivamente.

- **A.12.4.1 Registrazione degli Eventi**: Le Entità Organizzative DEVONO stabilire procedure per la registrazione degli eventi, inclusi i tipi di eventi da registrare, le informazioni da acquisire e il periodo di conservazione dei log.

- **A.12.4.2 Protezione delle Informazioni di Log**: Le Entità Organizzative DEVONO essere protette contro l'accesso non autorizzato e la manomissione. Ciò include l'implementazione di controlli di accesso, crittografia e controlli di integrità per garantire che i dati di log rimangano sicuri e affidabili.

- **A.12.4.3 Log degli Amministratori e degli Operatori**: Le attività degli amministratori di sistema e degli operatori DEVONO essere registrate e riviste regolarmente. Le Entità Organizzative DEVONO rilevare attività non autorizzate e garantire la responsabilità per le azioni intraprese sui sistemi critici.

- **A.12.4.4 Sincronizzazione degli Orologi**: Tutti i sistemi delle Entità Organizzative coinvolti nella registrazione DEVONO essere sincronizzati con una fonte temporale affidabile, garantendo timestamp accurati per correlare gli eventi tra diversi sistemi e condurre indagini forensi efficaci.

- **A.16.1.7 Gestione degli Incidenti di Sicurezza delle Informazioni**: Le Entità Organizzative DEVONO garantire che i log siano disponibili e affidabili per supportare i processi di gestione degli incidenti.


Politica di Conservazione dei Log del Fornitore di Wallet
---------------------------------------------------------

Le informazioni relative alla registrazione e alla gestione delle Istanze del Wallet possono essere conservate fino a 12 mesi dopo la disattivazione/revoca del Wallet o dell'account Utente associato, a meno che obblighi legali non richiedano una conservazione più lunga.



Politica di Conservazione dei Log del Fornitore di Credenziale
--------------------------------------------------------------

I Fornitori di Credenziale definiscono il periodo di conservazione per le Credenziali in base alle normative specifiche del settore. In assenza di normative specifiche, il periodo di conservazione per le Credenziali NON DOVREBBE superare i 12 mesi dopo la data di scadenza, configurata al momento dell'emissione nei metadati della parte firmata dall'Emittente della Credenziale.



Politica di Conservazione dei Log della Relying Party
-----------------------------------------------------

Le Relying Party POSSONO conservare i log relativi al trattamento dei dati ricevuti dal Wallet solo per la durata necessaria a fornire il servizio richiesto. Il periodo massimo di conservazione è di 24 mesi dopo la conclusione del servizio o la data di scadenza delle Credenziali presentate, a meno che obblighi legali non richiedano diversamente.


- Le Relying Party NON DOVREBBERO registrare le mappe di divulgazione della presentazione delle Credenziali, ove non necessario.

Funzionalità di Logging delle Istanze del Wallet
------------------------------------------------

Oltre ai requisiti inclusi nel Regolamento consolidato (UE) n. 910/2014, Art 5a 4(d) e alle informazioni aggiuntive fornite nei Considerando (11) e (13), il Regolamento di esecuzione (UE) 2024/2979 della Commissione stabilisce regole dettagliate per l'applicazione del Regolamento consolidato (UE) n. 910/2014, incluso il logging nelle funzionalità principali dei Portafogli di Identità Digitale Europea.

Il Regolamento (UE) 2024/2979, Articolo 9, definisce gli obblighi di logging relativi alle Soluzioni Wallet e ai meccanismi di portabilità dei dati.

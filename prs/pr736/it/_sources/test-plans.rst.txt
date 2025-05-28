.. include:: ../common/common_definitions.rst


Piani di Test
=============

Lo scopo dei piani di test è supportare gli implementatori, i revisori e gli ambienti di test di conformità nella validazione del comportamento delle Soluzioni Wallet, delle Relying Party e dei Credential Issuer in vari scenari operativi e di sicurezza.

Tutti i casi di test derivano da regole normative definite nelle specifiche sopra indicate, senza assunzioni o estensioni.

.. note::
  Si noti che la matrice dei piani di test potrebbe essere soggetta a modifiche future.

Struttura della Matrice di Test
-------------------------------

Ogni caso di test è identificato da un ID di test univoco (ad esempio, WS-001) e categorizzato utilizzando i domini funzionali definiti di seguito. Possono essere utilizzati anche altri identificatori di categoria.

- **Discovery**
- **Security**
- **Authorization**
- **Authentication**
- **User Interaction**
- **User Notification**
- **Credential Issuance**
- **Proof of Possession**
- **Attestation Evaluation**
- **Credential Presentation**
- **Credential Status**
- **Backup & Restore**

Per ogni caso di test, la tabella specifica:

- **Test Case**: un identificatore univoco.
- **Category**: l'area funzionale coperta dal test.
- **Description**: il requisito testato, sempre basato su un MUST normativo dalla specifica.
- **Expected Result**: il risultato atteso quando la soluzione è implementata correttamente.


Matrice di Test per la Valutazione delle Dichiarazioni Firmate
--------------------------------------------------------------

Questa sezione fornisce l'insieme comune di casi di test per Soluzioni Wallet, Relying Party e Credential Issuer che valutano qualsiasi dichiarazione firmata, siano esse asserzioni, richieste, attestati o credenziali.


.. list-table::
  :class: longtable
  :widths: 15 15 35 35
  :header-rows: 1

  * - Test Case
    - Category
    - Description
    - Expected Result
  * - ATT-001
    - Discovery, Security
    - Valutazione dell'emittente
    - Le entità che valutano le dichiarazioni firmate stabiliscono la fiducia con l'emittente e ne valutano la conformità. Gli emittenti non individuabili all'interno della federazione o non collegabili a qualsiasi Ancora di Fiducia nota, interrompono qualsiasi comunicazione di protocollo.
  * - ATT-002
    - Discovery, Security
    - Valutazione della firma
    - Le entità valutano le dichiarazioni firmate verificando la firma con il materiale crittografico dell'emittente, a condizione che sia considerato affidabile attraverso un'Ancora di Fiducia nota. Qualsiasi materiale crittografico non affidabile o firme non valide interrompono le comunicazioni del protocollo.
  * - ATT-003
    - Algorithm Verification
    - Verificare che l'algoritmo specificato nell'intestazione corrisponda a quello utilizzato per le operazioni crittografiche.
    - L'algoritmo nell'intestazione deve corrispondere all'operazione crittografica.
  * - ATT-004
    - Appropriate Algorithms
    - Garantire che vengano utilizzati solo algoritmi crittograficamente attuali.
    - Vengono accettati solo algoritmi approvati; quelli obsoleti vengono rifiutati.
  * - ATT-005
    - Signature Validation
    - Convalidare tutte le operazioni crittografiche e rifiutare se una qualsiasi fallisce.
    - Tutte le firme devono essere valide; qualsiasi fallimento comporta il fallimento di conformità.
  * - ATT-006
    - Key Entropy
    - Garantire che le chiavi crittografiche abbiano entropia sufficiente.
    - Le chiavi devono soddisfare i requisiti di entropia; le chiavi deboli vengono rifiutate.
  * - ATT-007
    - Issuer Validation
    - Convalidare che le chiavi crittografiche appartengano all'emittente.
    - Le chiavi devono essere verificate come appartenenti all'emittente.
  * - ATT-008
    - Audience Validation
    - Convalidare il claim dell'audience per garantire che il token sia utilizzato dalla parte prevista.
    - Il claim dell'audience deve corrispondere al destinatario previsto.
  * - ATT-009
    - Claim Trust
    - Non fidarsi dei claim ricevuti senza convalida.
    - I claim devono essere convalidati; i claim non attendibili vengono rifiutati.
  * - ATT-010
    - Explicit Typing
    - Utilizzare la tipizzazione esplicita per prevenire la confusione COSE/JOSE.
    - La tipizzazione deve essere esplicita e convalidata.
  * - ATT-011
    - Cross-JWT Confusion
    - Impedire che COSE/JOSE vengano utilizzati in contesti non previsti.
    - COSE/JOSE devono essere convalidati contestualmente per prevenire l'uso improprio.
  * - ATT-012
    - Substitution Attacks
    - Garantire che COSE/JOSE non vengano sostituiti in contesti diversi.
    - COSE/JOSE devono essere convalidati per l'uso specifico del contesto.
  * - ATT-013
    - Issued At Validation
    - Verificare che il parametro `issued at` sia impostato sull'ora corrente, consentendo un periodo di tolleranza non superiore a 120 secondi.
    - Il valore `issued at` deve essere entro 120 secondi dall'ora corrente.
  * - ATT-014
    - Expiration Validation
    - Garantire che il tempo di `expiration` sia maggiore del tempo di `issued at`.
    - Il tempo di `expiration` deve essere successivo al tempo di `issued at`.
  * - ATT-015
    - Data model validation
    - Garantire che il tipo JOSE/COSE corrisponda al modello di dati definito.
    - I parametri o i claim, i loro valori e lo schema utilizzato per rappresentarli sono conformi al modello di dati.


Matrice di Test per la Valutazione della Fiducia
------------------------------------------------

Questa sezione fornisce l'insieme comune di casi di test per Soluzioni Wallet, Relying Party e Credential Issuer.


.. list-table::
  :class: longtable
  :widths: 15 15 35 35
  :header-rows: 1

  * - Test Case
    - Category
    - Description
    - Expected Result
  * - ALL-001
    - Security
    - Ottenimento dei materiali crittografici pubblici delle Ancore di Fiducia
    - Le entità ottengono l'elenco delle Ancore di Fiducia o delle Autorità di Certificazione e i loro materiali di chiave crittografica pubblica, assicurandosi periodicamente che questi non siano scaduti, revocati o aggiornati. L'infrastruttura di fiducia fornisce queste informazioni attraverso endpoint web e meccanismi di recapito alternativi, per facilitare il confronto delle informazioni fornite a tutte le entità.
  * - ALL-002
    - Security
    - Autovalutazione della conformità
    - Le entità valutano periodicamente la loro conformità e presenza all'interno della federazione, verificando che la catena di fiducia su se stesse sia ancora valida, non revocata e conforme alla specifica tecnica. Le entità applicano le politiche, verificando che la loro configurazione attuale sia valida con le politiche attive su di esse all'interno della federazione. La catena di fiducia, valutata e memorizzata in più formati per facilitare l'interoperabilità nella scoperta della fiducia con altre entità, viene memorizzata dalle entità e utilizzata all'occorrenza durante i flussi di scambio dati. La catena di fiducia sulle entità viene recuperata utilizzando le asserzioni emesse dall'entità.
  * - ALL-003
    - Discovery
    - Pubblicazione di informazioni su se stessi
    - Le entità firmano e pubblicano tutte le informazioni su di loro, contenenti tutti i metadati del protocollo, il materiale crittografico, i Trust Mark, utilizzando l'endpoint well-known definito in questa specifica, rendendo queste informazioni pubblicamente individuabili da altre entità.
  * - ALL-004
    - Security
    - Pubblicazione del registro storico delle chiavi
    - Le entità firmano e pubblicano tutte le informazioni sul materiale crittografico inutilizzato o revocato utilizzando endpoint well-known definiti in questa specifica, rendendo queste informazioni pubblicamente individuabili da altre entità.
  * - ALL-005
    - Security
    - Valutazione della conformità con le entità prima di scambiare dati sull'Utente
    - Le entità valutano la fiducia e la conformità con altre entità prima che qualsiasi informazione relativa a una persona fisica o giuridica possa essere scambiata. Configurazioni errate non consentono scambi di dati.
  * - ALL-006
    - Security
    - Valutazione della prova di possesso durante l'uso di un'asserzione firmata in base al metodo di conferma di proprietà dell'uso configurato.
    - Le entità valutano il metodo di conferma e applicano il suo protocollo per considerare valida la dichiarazione firmata.
  * - ALL-007
    - Security
    - Algoritmi di crittografia supportati
    - Le entità valutano la crittografia utilizzando in conformità con gli algoritmi consentiti.
  * - ALL-008
    - Security
    - Attacchi di replay
    - Le dichiarazioni firmate che utilizzano identificatori univoci vengono memorizzate fino alla loro scadenza e verificate rispetto a qualsiasi replay di esse.


Matrice di Test per la Soluzione Wallet
---------------------------------------

Questa sezione fornisce l'insieme di casi di test per verificare la conformità di un'implementazione di Soluzione Wallet alle regole tecniche definite nell'ecosistema IT-Wallet.
Il piano di test si basa sui requisiti obbligatori (dichiarazioni MUST) estratti dai seguenti documenti:

- Wallet Solution
- Wallet Instance Revocation
- Wallet Attestation Issuance
- Backup and Restore


.. list-table::
  :class: longtable
  :widths: 15 15 35 35
  :header-rows: 1

  * - Test Case
    - Category
    - Description
    - Expected Result
  * - WS-001
    - Wallet Initialization
    - La Soluzione Wallet DEVE garantire che ogni Istanza del Wallet sia generata secondo le specifiche e includa un identificatore univoco e chiavi crittografiche associate a un elemento sicuro.
    - Viene generata un'Istanza del Wallet conforme con identificatori corretti e associazioni sicure.
  * - WS-002
    - User Interaction
    - La Soluzione Wallet DEVE richiedere e ottenere il Consenso esplicito dell'Utente durante l'inizializzazione dell'Istanza del Wallet.
    - L'Istanza del Wallet viene attivata solo dopo aver ottenuto il Consenso dell'Utente.
  * - WS-003
    - Security
    - La Soluzione Wallet DEVE memorizzare le chiavi private all'interno di un Elemento Hardware Sicuro o di un archivio sicuro equivalente.
    - Tutti i materiali delle chiavi private sono inaccessibili dal sistema operativo o da qualsiasi applicazione esterna alla Soluzione Wallet.
  * - WS-004
    - Attestation
    - Il Wallet DEVE essere in grado di generare e presentare un Attestato di Wallet quando richiesto dalle Relying Party o dagli Emittenti.
    - Vengono generati Attestati validi e verificabili, incluse prove di integrità e origine.
  * - WS-005
    - Attestation
    - Il Wallet DEVE supportare l'elaborazione delle Richieste di Attestato di Wallet e generare risposte appropriate in conformità con eIDAS.
    - Il Wallet interpreta correttamente e soddisfa le richieste di attestato, inclusi i dati del soggetto e le firme crittografiche.
  * - WS-006
    - Remote Credential Presentation
    - La Soluzione Wallet DEVE implementare sia il flusso di presentazione di prossimità che quello remoto, garantendo la selezione delle Credenziali Verificabili, l'integrità e l'interazione dell'Utente.
    - La presentazione delle Credenziali Verificabili ha successo, è corretta e sotto il controllo dell'Utente.
  * - WS-007
    - Credential Issuance
    - Il Wallet DEVE supportare il flusso dell'Emittente per ricevere e memorizzare le Credenziali Verificabili.
    - Le credenziali vengono memorizzate in modo sicuro e analizzate correttamente secondo la struttura definita.
  * - WS-008
    - Revocation
    - Il Wallet DEVE consentire all'Utente di attivare una Revoca dell'Istanza del Wallet in qualsiasi momento.
    - La revoca viene eseguita e il materiale crittografico viene eliminato in modo sicuro o reso inutilizzabile.
  * - WS-009
    - Revocation
    - In caso di Revoca dell'Istanza del Wallet, la Soluzione Wallet DEVE notificare ai sistemi di backend pertinenti di propagare la revoca.
    - Lo stato di revoca si riflette in tutti i componenti dell'ecosistema (ad esempio, Emittenti, Verificatori).
  * - WS-010
    - Backup & Restore
    - Il Wallet DEVE supportare operazioni di Backup e Ripristino crittografate in conformità con i requisiti di privacy e integrità.
    - Il backup è crittografato e legato all'Utente; l'operazione di Ripristino verifica l'integrità e l'autenticità dell'Utente prima del recupero.
  * - WS-011
    - Backup & Restore
    - Il Wallet DEVE gestire le chiavi di crittografia del backup in modo sicuro e derivarle da segreti o credenziali controllati dall'Utente.
    - Nessuna entità non autorizzata può decrittografare i backup; i backup sono resi inutili se manomessi.
  * - WS-012
    - Backup & Restore
    - Il Wallet DEVE autenticare l'Utente prima di consentire il Ripristino.
    - Il Ripristino avviene con successo solo dopo l'autenticazione verificata dell'Utente utilizzando metodi approvati (ad esempio, biometria, PIN, sfida crittografica).
  * - WS-013
    - Attestation
    - Il Wallet DEVE rilevare gli Attestati scaduti e supportare i flussi di aggiornamento.
    - Gli Attestati scaduti non vengono utilizzati; l'aggiornamento viene attivato automaticamente o tramite richiesta dell'Utente.
  * - WS-014
    - Compliance
    - Tutte le operazioni, inclusi Emissione, Presentazione, Attestato e Revoca, DEVONO essere conformi agli standard europei.
    - Viene mantenuta una traccia verificabile delle operazioni conformi; non si osserva alcuna deviazione dal comportamento eIDAS 2.0.
  * - WS-015
    - User Interaction
    - Il Wallet DEVE operare secondo il principio del controllo dell'Utente e della minimizzazione dei dati.
    - Vengono utilizzati e trasmessi solo i dati esplicitamente consentiti e richiesti; tutte le operazioni richiedono azioni esplicite dell'Utente.
  * - WS-016
    - Credential Presentation
    - Il Wallet DEVE supportare la presentazione offline delle Credenziali Verificabili quando consentito.
    - Le credenziali vengono presentate in modo sicuro anche in modalità offline, mantenendo l'integrità e l'autenticità.
  * - WS-017
    - Security
    - Il Wallet DEVE garantire protezioni anti-replay durante la presentazione delle credenziali.
    - Ogni presentazione è crittograficamente unica e legata alla richiesta del Verificatore.
  * - WS-018
    - Revocation
    - Il Wallet DEVE registrare e rendere verificabile il processo di revoca delle Istanze del Wallet.
    - I log completi e a prova di manomissione sono disponibili per l'ispezione su richiesta.
  * - WS-019
    - Security
    - Il Wallet DEVE stabilire canali reciprocamente autenticati e crittografati durante tutte le interazioni.
    - Tutti i messaggi sono protetti contro l'intercettazione, la modifica o l'impersonificazione.
  * - WS-020
    - Security
    - Il Wallet DEVE bloccarsi e/o revocare l'Istanza del Wallet in caso di rilevamento di manomissioni.
    - Il Wallet diventa inoperabile e la revoca viene attivata se la manomissione è confermata.
  * - WS-021
    - Security
    - Il Wallet DEVE eseguire l'Attestato del Dispositivo utilizzando meccanismi specifici della piattaforma come Play Integrity (Android) o DC App Attest (iOS) durante la creazione dell'Istanza del Wallet.
    - L'Attestato del Dispositivo ha successo e i risultati sono inclusi nel payload dell'Attestato del Wallet.
  * - WS-022
    - Attestation
    - L'Attestato del Wallet DEVE includere una firma utilizzando la Chiave di Binding del Wallet, e la catena di certificati DEVE essere verificabile fino a una radice attendibile.
    - La firma è presente, valida e verificabile utilizzando la catena di certificati fornita.
  * - WS-023
    - Attestation
    - Il Wallet DEVE includere un risultato dell'Attestato del Dispositivo nella struttura dell'Attestato del Wallet.
    - Un oggetto di Attestato del Dispositivo valido (risultato di Play Integrity o DC App Attest) è incorporato nell'Attestato.
  * - WS-024
    - Backup & Restore
    - Durante il Ripristino, il Wallet DEVE convalidare l'integrità del file di backup crittografato utilizzando un meccanismo di controllo dell'integrità.
    - Il Wallet rifiuta di ripristinare un file di backup manomesso o corrotto.
  * - WS-025
    - Revocation
    - In caso di Revoca dell'Istanza del Wallet, il Wallet DEVE eliminare qualsiasi Credenziale Verificabile memorizzata localmente.
    - Nessun dato di credenziale rimane accessibile dopo l'attivazione della revoca.
  * - WS-026
    - Revocation
    - Il Wallet DEVE notificare al Backend del Wallet una Richiesta di Revoca che includa una prova valida di possesso della Chiave di Binding del Wallet.
    - La Richiesta di Revoca viene accettata e lo stato di revoca viene aggiornato nel backend.
  * - WS-027
    - Security
    - Il Wallet DEVE impedire il riutilizzo delle Chiavi di Binding del Wallet revocate o delle credenziali nelle future Istanze del Wallet.
    - Qualsiasi tentativo di riutilizzo viene rilevato e bloccato.
  * - WS-028
    - Attestation
    - Il Wallet DEVE supportare l'aggiornamento dell'Attestato tramite l'API definita esposta dal Backend del Wallet.
    - L'Attestato viene rinnovato e la nuova versione viene accettata dai Verificatori e dagli Emittenti.
  * - WS-029
    - Backup & Restore
    - La crittografia del backup DEVE utilizzare algoritmi di crittografia forti e conformi agli standard (ad esempio, AES-GCM).
    - Il file di backup crittografato è resistente agli attacchi di forza bruta e agli attacchi crittografici noti.
  * - WS-030
    - User Interaction
    - Il Wallet DEVE richiedere all'Utente di confermare l'intenzione prima di qualsiasi operazione distruttiva come la Revoca o l'Eliminazione delle Credenziali.
    - Le azioni distruttive vengono eseguite solo dopo la conferma esplicita dell'Utente.
  * - WS-031
    - Attestation
    - Il Wallet DEVE generare un Attestato del Wallet contenente informazioni sullo stato di integrità del dispositivo, utilizzando l'API Play Integrity su Android.
    - L'Attestato del Wallet include un payload Play Integrity valido con il campo 'MEETS_DEVICE_INTEGRITY' impostato.
  * - WS-032
    - Attestation
    - Il Wallet DEVE generare un Attestato del Wallet utilizzando DeviceCheck App Attest su iOS e includere il risultato dell'attestato nell'Attestato del Wallet.
    - L'Attestato del Wallet include una risposta JWT DC App Attest valida firmata da Apple.
  * - WS-033
    - Security
    - Il Wallet DEVE verificare che la firma del token Play Integrity sia valida e emessa da Google.
    - Il Wallet rifiuta i token Play Integrity non validi o contraffatti.
  * - WS-034
    - Security
    - Il Wallet DEVE convalidare che il valore 'nonce' utilizzato in Play Integrity sia crittograficamente legato all'Istanza del Wallet.
    - Qualsiasi manomissione del nonce viene rilevata e porta al rifiuto dell'Attestato.
  * - WS-035
    - Attestation
    - Il Wallet DEVE inviare l'Attestato del Wallet al Backend del Wallet durante la registrazione.
    - Il Backend del Wallet riceve l'attestato e ne verifica la validità.
  * - WS-036
    - Backup & Restore
    - Il Wallet DEVE crittografare i backup utilizzando una chiave simmetrica derivata dai segreti dell'Utente.
    - Il backup non può essere decrittografato senza il materiale di autenticazione originale dell'Utente.
  * - WS-037
    - Backup & Restore
    - Il Wallet DEVE includere metadati nel backup che identifichino la versione e il timestamp di creazione.
    - Il processo di Ripristino legge e verifica i metadati del backup prima di procedere.
  * - WS-038
    - Revocation
    - Il Wallet DEVE inviare una Richiesta di Revoca firmata che includa la firma della Chiave di Binding del Wallet al Backend.
    - Il backend elabora la revoca e aggiorna lo stato del Wallet a revocato.
  * - WS-039
    - Revocation
    - Il Wallet NON DEVE consentire ulteriori Emissioni o Presentazioni di Credenziali dopo la revoca.
    - Tutte le operazioni sono bloccate una volta che il Wallet è revocato.
  * - WS-040
    - Credential Issuance
    - Il Wallet DEVE convalidare la struttura dell'Offerta di Credenziale ricevuta dall'Emittente.
    - Il Wallet accetta solo Offerte di Credenziale che corrispondono al formato e alla firma previsti.
  * - WS-041
    - Credential Issuance
    - Il Wallet DEVE garantire che l'Utente acconsenta a ricevere una nuova Credenziale.
    - Nessuna Credenziale viene memorizzata senza l'approvazione esplicita dell'Utente.
  * - WS-042
    - Credential Presentation
    - Il Wallet DEVE verificare la Richiesta di Presentazione del Verificatore prima di rispondere.
    - Le richieste non valide o malformate vengono rifiutate.
  * - WS-043
    - Security
    - Il Wallet DEVE firmare le Presentazioni Verificabili con la chiave privata corretta associata all'Istanza del Wallet.
    - I Verificatori sono in grado di convalidare la firma e fidarsi della presentazione.
  * - WS-044
    - User Interaction
    - Il Wallet DEVE richiedere all'Utente prima di inviare una Credenziale Verificabile a un Verificatore.
    - Nessuna credenziale viene condivisa senza la conferma esplicita dell'Utente.
  * - WS-045
    - Backup & Restore
    - Il Wallet DEVE consentire all'Utente di eliminare tutti i dati di backup memorizzati.
    - Tutto il materiale di backup viene eliminato in modo sicuro e non può essere recuperato.
  * - WS-046
    - Revocation
    - Se il Wallet viene ripristinato su un nuovo dispositivo, DEVE verificare se l'Istanza del Wallet originale è stata revocata.
    - Le Istanze del Wallet revocate non possono essere ripristinate.
  * - WS-047
    - Security
    - Il Wallet DEVE verificare la validità temporale delle Credenziali ricevute (ad esempio, issuanceDate, expirationDate).
    - Le credenziali scadute vengono contrassegnate come non valide e non vengono utilizzate.
  * - WS-048
    - Attestation
    - Il Wallet DEVE includere la chiave pubblica della Chiave di Binding del Wallet nell'Attestato del Wallet.
    - I Verificatori e gli Emittenti possono convalidare le firme effettuate con la chiave privata corrispondente.
  * - WS-049
    - Credential Presentation
    - Il Wallet DEVE supportare la Divulgazione Selettiva degli attributi delle Credenziali.
    - Solo i campi selezionati sono inclusi nella presentazione inviata al Verificatore.
  * - WS-050
    - Credential Presentation
    - Il Wallet DEVE consentire all'Utente di visualizzare in anteprima quali attributi delle Credenziali saranno divulgati prima della conferma.
    - All'Utente vengono mostrati i dati esatti da condividere e li approva esplicitamente.
  * - WS-051
    - Proximity Flow
    - Il Wallet DEVE avviare il flusso di prossimità solo dopo il Consenso esplicito dell'Utente a interagire con un'Istanza di Relying Party Mobile.
    - Il flusso di presentazione di prossimità del Wallet è bloccato a meno che l'Utente non abbia approvato la richiesta.
  * - WS-052
    - Proximity Flow
    - Il Wallet DEVE convalidare il Certificato di Accesso presentato da un'Istanza di Relying Party Mobile prima di procedere.
    - Se il Certificato di Accesso è mancante, non valido o scaduto, il Wallet DEVE rifiutare la richiesta.
  * - WS-053
    - Proximity Flow
    - Il Wallet DEVE visualizzare un disclaimer quando il Certificato di Accesso è scaduto ma ancora entro il periodo di tolleranza consentito.
    - Il disclaimer viene mostrato chiaramente all'Utente e la presentazione procede solo dopo il consenso.
  * - WS-054
    - Relying Party Instance
    - Il Wallet DEVE applicare il controllo che lo stato dell'Istanza di Relying Party sia 'Verificato' prima di consentire la presentazione delle credenziali.
    - Il Wallet nega il flusso se l'Istanza di Relying Party è in qualsiasi stato diverso da 'Verificato'.
  * - WS-055
    - Security
    - Il Wallet DEVE registrare qualsiasi tentativo di presentazione fallito a causa di uno stato non valido dell'Istanza di Relying Party o di un Certificato di Accesso scaduto.
    - Viene generato e memorizzato in modo sicuro un log degli eventi di sicurezza.
  * - WS-056
    - Interoperability
    - Il Wallet DEVE supportare la comunicazione con le Istanze di Relying Party utilizzando codici QR standardizzati per la negoziazione della sessione come definito nella specifica.
    - Il Wallet legge e analizza con successo i codici QR e avvia la sessione secondo il protocollo.
  * - WS-057
    - Proximity Flow
    - Il Wallet DEVE stabilire una sessione sicura e autenticata con l'Istanza di Relying Party Mobile utilizzando chiavi effimere prima della presentazione.
    - Le chiavi di sessione vengono negoziate e verificate, e tutta la comunicazione è crittografata.
  * - WS-058
    - Credential Presentation
    - Il Wallet DEVE consentire all'Utente di scegliere quale Credenziale presentare a un'Istanza di Relying Party anche nel flusso di prossimità.
    - L'interfaccia di selezione delle Credenziali viene mostrata all'Utente durante il flusso di prossimità.
  * - WS-059
    - Security
    - Il Wallet DEVE interrompere la sessione se l'Istanza di Relying Party non riesce a dimostrare il possesso della chiave privata associata al Certificato di Accesso.
    - La sessione viene terminata e nessun dato di Credenziale viene divulgato.
  * - WS-060
    - User Interaction
    - Il Wallet DEVE indicare chiaramente all'Utente quando una richiesta di presentazione proviene da un'Istanza di Relying Party Mobile utilizzando un canale di prossimità.
    - La fonte della richiesta viene mostrata prima di consentire alla presentazione di procedere.

Matrice di Test per l'Emissione di Credenziali
----------------------------------------------

Questa sezione fornisce l'insieme di casi di test per verificare la conformità delle implementazioni di Emissione di Credenziali alle regole tecniche definite nell'ecosistema IT-Wallet.
I test relativi al Credential Issuer sono relativi all'emissione di Credenziali di Interesse Pubblico, come pubblicato nel Catalogo delle Credenziali.

.. note::
  I riferimenti ai piani di test ufficiali OpenID4VCI aggiorneranno questa sezione nelle versioni future.

- Emissione PID/EAA


.. list-table::
  :class: longtable
  :widths: 15 15 35 35
  :header-rows: 1

  * - Test Case
    - Category
    - Description
    - Expected Result
  * - ISS-001
    - Setup
    - Convalidare la configurazione dell'Istanza del Wallet
    - L'Istanza del Wallet è configurata con un Attestato di Wallet valido. Assicurarsi che la chiave pubblica sia valida e correttamente associata a un elemento sicuro.
  * - ISS-002
    - Discovery
    - Scoperta del Credential Issuer
    - L'Istanza del Wallet scopre con successo i Credential Issuer digitali affidabili utilizzando il Catalogo delle Credenziali e la loro conformità alla configurazione e alle politiche con l'API di Federazione.
  * - ISS-003
    - Metadata
    - Recupero dei metadati del Credential Issuer
    - L'Istanza del Wallet recupera e convalida i metadati del Credential Issuer. I metadati includono formati PID, algoritmi supportati e parametri di interoperabilità.
  * - ISS-004
    - Authorization, Authentication
    - Richiesta di Credenziale utilizzando il flusso Authorization Code
    - L'Istanza del Wallet richiede con successo la Credenziale utilizzando il flusso Authorization Code. Convalidare l'uso di PKCE con un code verifier di 43-128 caratteri.
  * - ISS-005
    - Authentication
    - Autenticazione dell'Utente con il Fornitore di Attestati Elettronici di Dati di Identificazione Personale
    - L'Utente viene autenticato con LoA 3 (Alto) dal Fornitore di Attestati Elettronici di Dati di Identificazione Personale. Convalidare l'uso dello schema di identità digitale CieID e assicurarsi che venga ottenuto il consenso dell'Utente.
  * - ISS-006
    - Issuance
    - Emissione di Credenziale
    - La Credenziale viene emessa e associata al materiale chiave dell'Istanza del Wallet. Convalidare il processo di associazione e garantire l'integrità e la conformità al modello di dati della Credenziale emessa.
  * - ISS-007
    - Authentication
    - Autenticazione dell'Utente con il Fornitore di Attestati Elettronici di Attributi (Q)ualificati
    - L'Utente viene autenticato presentando un PID valido. La richiesta di presentazione, il PID è valido e precedentemente ottenuto.
  * - ISS-008
    - Security
    - Convalida della Pushed Authorization Request (PAR)
    - Il Credential Issuer convalida con successo la richiesta PAR.
  * - ISS-009
    - Security
    - Convalida della richiesta di token
    - Il Credential Issuer convalida la richiesta di token e emette i token. Convalidare la prova DPoP e assicurarsi che il codice di autorizzazione sia valido e non riutilizzato.
  * - ISS-010
    - Security
    - Convalida della richiesta di Credenziale
    - Il Credential Issuer convalida la richiesta di Credenziali e emette le Credenziali. Convalidare la prova di possesso e assicurarsi che il tipo di credenziale corrisponda alla richiesta.
  * - ISS-011
    - Deferred Issuance
    - Flusso di emissione differita
    - L'Istanza del Wallet gestisce correttamente l'emissione differita e recupera le credenziali in un secondo momento. Convalidare l'uso dell'identificatore univoco della transazione (`transaction_id`) e assicurarsi che la Credenziale venga emessa dopo il tempo di attesa specificato.
  * - ISS-012
    - Notification
    - Gestione delle notifiche
    - L'Istanza del Wallet invia e riceve correttamente le notifiche. Convalidare l'uso di `notification_id` e assicurarsi che il tipo di evento sia riportato correttamente.
  * - ISS-013
    - Credential Issuance
    - Il Fornitore di Attestati Elettronici di Attributi (Q)ualificati offre Credenziali al Titolare
    - Le Istanze del Wallet valutano l'offerta e avviano il flusso di autorizzazione dopo aver valutato la fiducia con il Fornitore di Attestati Elettronici di Attributi (Q)ualificati.
  * - ISS-014
    - Security
    - Convalidare `client_id` nella richiesta PAR
    - Assicurarsi che il `client_id` nel corpo della richiesta corrisponda al claim `client_id` nell'Oggetto Richiesta.
  * - ISS-015
    - Security
    - Convalidare il claim `iss` nell'Oggetto Richiesta
    - Assicurarsi che il claim `iss` nell'Oggetto Richiesta corrisponda al claim `client_id`.
  * - ISS-016
    - Security
    - Convalidare il claim `aud` nell'Oggetto Richiesta
    - Assicurarsi che il claim `aud` nell'Oggetto Richiesta sia uguale all'identificatore del Credential Issuer.
  * - ISS-017
    - Security
    - Rifiutare la richiesta PAR con `request_uri`
    - Assicurarsi che la richiesta PAR venga rifiutata se contiene il parametro `request_uri`.
  * - ISS-018
    - Security
    - Convalidare i parametri obbligatori nell'Oggetto Richiesta
    - Assicurarsi che l'Oggetto Richiesta contenga tutti i parametri obbligatori e che i valori siano convalidati.
  * - ISS-019
    - Security
    - Convalidare `OAuth-Client-Attestation-PoP`
    - Assicurarsi che il parametro `OAuth-Client-Attestation-PoP` sia convalidato.
  * - ISS-020
    - Authorization
    - Convalidare `request_uri` nella richiesta di autorizzazione
    - Assicurarsi che i valori `request_uri` siano trattati come monouso e che le richieste scadute vengano rifiutate.
  * - ISS-021
    - Authorization
    - Identificare la richiesta dalla PAR inviata
    - Assicurarsi che la richiesta sia identificata come risultato della PAR inviata.
  * - ISS-022
    - Authorization
    - Rifiutare le richieste di autorizzazione senza `request_uri`
    - Assicurarsi che tutte le richieste di autorizzazione senza `request_uri` vengano rifiutate.
  * - ISS-023
    - Security
    - Convalidare i parametri della risposta di autorizzazione
    - Assicurarsi che la risposta di autorizzazione contenga tutti i parametri definiti.
  * - ISS-024
    - Security
    - Convalidare il parametro `state` nella risposta di autorizzazione
    - Assicurarsi che il parametro `state` nella risposta corrisponda al valore inviato nell'Oggetto Richiesta.
  * - ISS-025
    - Security
    - Convalidare il parametro `iss` nella risposta di autorizzazione
    - Assicurarsi che il parametro `iss` corrisponda al Credential Issuer previsto.
  * - ISS-026
    - Security
    - Convalidare la prova DPoP per l'endpoint Token
    - Assicurarsi che il JWT della prova DPoP sia valido e associ il Token di Accesso all'Istanza del Wallet.
  * - ISS-027
    - Security
    - Convalidare i parametri della richiesta di token
    - Assicurarsi che la richiesta di token includa `code`, `code_verifier` e un Attestato OAuth 2.0 valido.
  * - ISS-028
    - Security
    - Convalidare il codice di autorizzazione nella richiesta di token
    - Assicurarsi che il `code` di autorizzazione sia valido e non riutilizzato.
  * - ISS-029
    - Security
    - Convalidare `redirect_uri` nella richiesta di token
    - Assicurarsi che il `redirect_uri` corrisponda al valore nel precedente Oggetto Richiesta.
  * - ISS-030
    - Security
    - Convalidare il JWT della prova DPoP nella richiesta di token
    - Assicurarsi che il JWT della prova DPoP sia convalidato secondo la specifica.
  * - ISS-031
    - Security
    - Convalidare la richiesta di Nonce
    - Assicurarsi che la richiesta di Nonce sia inviata correttamente e che venga ottenuto un `c_nonce` fresco.
  * - ISS-032
    - Security
    - Convalidare la risposta di Nonce
    - Assicurarsi che il `c_nonce` nella risposta di Nonce sia imprevedibile e utilizzato correttamente.
  * - ISS-033
    - Security
    - Convalidare la prova DPoP per l'endpoint Credential
    - Assicurarsi che il JWT della prova DPoP per l'endpoint Credential sia valido e associ la Credenziale all'Istanza del Wallet.
  * - ISS-034
    - Security
    - Convalidare i parametri della richiesta di Credenziale
    - Assicurarsi che la richiesta di Credenziale includa il Token di Accesso, il JWT della prova DPoP e una prova di possesso valida.
  * - ISS-035
    - Security
    - Convalidare la prova JWT nella richiesta di Credenziale
    - Assicurarsi che la prova JWT includa tutti i claim richiesti e sia firmata correttamente.
  * - ISS-036
    - Security
    - Convalidare `c_nonce` nella richiesta di Credenziale
    - Assicurarsi che il `c_nonce` nel JWT corrisponda al valore fornito dal server.
  * - ISS-037
    - Security
    - Convalidare i parametri della risposta di Credenziale
    - Assicurarsi che la risposta di Credenziale contenga tutti i parametri obbligatori e che i valori siano convalidati.
  * - ISS-038
    - Security
    - Convalidare l'integrità della Credenziale
    - Assicurarsi dell'integrità della Credenziale emessa verificando la firma.
  * - ISS-039
    - Security
    - Convalidare il tipo e lo schema della Credenziale
    - Assicurarsi che la Credenziale emessa corrisponda al tipo richiesto e sia conforme allo schema.
  * - ISS-040
    - Security
    - Convalidare la catena di fiducia nella Credenziale
    - Assicurarsi che la catena di fiducia nell'intestazione della Credenziale verifichi la fiducia del Credential Issuer al momento dell'emissione.
  * - ISS-041
    - Security
    - Convalidare i parametri dell'emissione differita
    - Assicurarsi che i parametri dell'emissione differita siano utilizzati correttamente e che la Credenziale venga emessa dopo il tempo di attesa specificato.
  * - ISS-042
    - Security
    - Convalidare i parametri della richiesta di notifica
    - Assicurarsi che la richiesta di notifica includa `notification_id` e un tipo di evento valido.
  * - ISS-043
    - Security
    - Convalidare la risposta di notifica
    - Assicurarsi che la risposta di notifica venga ricevuta con il codice di stato corretto.
  * - ISS-044
    - Security
    - Convalidare il flusso del token di aggiornamento
    - Assicurarsi che il flusso del token di aggiornamento sia utilizzato correttamente e che i token siano associati alla chiave DPoP.
  * - ISS-045
    - Security
    - Convalidare la scadenza del token di aggiornamento
    - Assicurarsi che il token di aggiornamento non sia scaduto e sia utilizzato entro il periodo di tempo consentito.
  * - ISS-046
    - Security
    - Convalidare i token vincolati al mittente
    - Assicurarsi che i token di aggiornamento siano crittograficamente associati all'Istanza del Wallet.
  * - ISS-047
    - Security
    - Convalidare la limitazione dell'uso del token di aggiornamento
    - Assicurarsi che l'uso dei token di aggiornamento sia limitato e conforme alla specifica.
  * - ISS-048
    - Revocation
    - Convalidare la durata degli Attestati del Wallet
    - Assicurarsi che gli Attestati del Wallet siano di breve durata o forniti con Status List se di lunga durata.
  * - ISS-049
    - Security
    - Convalidare il flusso di riemissione
    - Assicurarsi che il flusso di riemissione sia utilizzato correttamente e sia conforme alla specifica.
  * - ISS-050
    - Security
    - Convalidare l'aggiornamento del modello/formato dei dati
    - Assicurarsi che l'aggiornamento del modello/formato dei dati sia gestito correttamente durante la riemissione.
  * - ISS-051
    - Security
    - Convalidare l'aggiornamento del set di attributi dell'Utente
    - Assicurarsi che gli aggiornamenti del set di attributi dell'Utente siano gestiti correttamente durante la riemissione.
  * - ISS-052
    - Security
    - Convalidare la scadenza della Credenziale nella riemissione
    - Assicurarsi che la Credenziale appena emessa abbia la stessa data di scadenza della precedente.
  * - ISS-053
    - Security
    - Convalidare l'autenticazione dell'Utente nella riemissione
    - Assicurarsi che l'autenticazione dell'Utente sia richiesta per la riemissione dopo la scadenza della Credenziale.
  * - ISS-054
    - Security
    - Convalidare i parametri dell'endpoint differito
    - Assicurarsi che i parametri dell'endpoint differito siano utilizzati correttamente e che la Credenziale venga emessa dopo il tempo di attesa specificato.
  * - ISS-055
    - Security
    - Convalidare la richiesta di Credenziale differita
    - Assicurarsi che la richiesta di Credenziale differita sia inviata correttamente e che la Credenziale venga emessa.
  * - ISS-056
    - Security
    - Convalidare la risposta di Credenziale differita
    - Assicurarsi che la risposta di Credenziale differita contenga tutti i parametri obbligatori e che i valori siano convalidati.
  * - ISS-057
    - Security
    - Convalidare i parametri dell'endpoint di notifica
    - Assicurarsi che i parametri dell'endpoint di notifica siano utilizzati correttamente e che l'evento sia riportato.
  * - ISS-058
    - Security
    - Convalidare la gestione degli errori nell'endpoint di notifica
    - Assicurarsi che gli errori nell'endpoint di notifica siano gestiti correttamente e riportati.
  * - ISS-059
    - Security
    - Convalidare la gestione degli errori nell'endpoint Credential
    - Assicurarsi che gli errori nell'endpoint Credential siano gestiti correttamente e riportati.
  * - ISS-060
    - Security
    - Convalidare la gestione degli errori nell'endpoint Token
    - Assicurarsi che gli errori nell'endpoint Token siano gestiti correttamente e riportati.
  * - ISS-061
    - Security
    - Convalidare la gestione degli errori nell'endpoint Authorization
    - Assicurarsi che gli errori nell'endpoint Authorization siano gestiti correttamente e riportati.
  * - ISS-062
    - Error Handling
    - Convalidare la gestione degli errori nell'endpoint PAR
    - Assicurarsi che gli errori nell'endpoint PAR siano gestiti correttamente e riportati.
  * - ISS-063
    - Error Handling
    - Convalidare la gestione degli errori nell'endpoint Nonce
    - Assicurarsi che gli errori nell'endpoint Nonce siano gestiti correttamente e riportati.
  * - ISS-064
    - Error Handling
    - Convalidare la gestione degli errori nell'endpoint differito
    - Assicurarsi che gli errori nell'endpoint differito siano gestiti correttamente e riportati.
  * - ISS-065
    - Error Handling
    - Convalidare la gestione degli errori nel flusso di riemissione
    - Assicurarsi che gli errori nel flusso di riemissione siano gestiti correttamente e riportati.
  * - ISS-066
    - Error Handling
    - Convalidare la gestione degli errori nel flusso del token di aggiornamento
    - Assicurarsi che gli errori nel flusso del token di aggiornamento siano gestiti correttamente e riportati.
  * - ISS-067
    - Error Handling
    - Convalidare la gestione degli errori nell'emissione di Credenziale
    - Assicurarsi che gli errori nel processo di emissione di Credenziale siano gestiti correttamente e riportati.
  * - ISS-068
    - Error Handling
    - Convalidare la gestione degli errori nella richiesta di Credenziale
    - Assicurarsi che gli errori nel processo di richiesta di Credenziale siano gestiti correttamente e riportati.
  * - ISS-069
    - Error Handling
    - Convalidare la gestione degli errori nella risposta di Credenziale
    - Assicurarsi che gli errori nel processo di risposta di Credenziale siano gestiti correttamente e riportati.
  * - ISS-070
    - Error Handling
    - Convalidare la gestione degli errori nella convalida della Credenziale
    - Assicurarsi che gli errori nel processo di convalida della Credenziale siano gestiti correttamente e riportati.
  * - ISS-071
    - Error Handling
    - Convalidare la gestione degli errori nell'integrità della Credenziale
    - Assicurarsi che gli errori nel processo di integrità della Credenziale siano gestiti correttamente e riportati.
  * - ISS-072
    - Error Handling
    - Convalidare la gestione degli errori nel tipo e nello schema della Credenziale
    - Assicurarsi che gli errori nel processo di tipo e schema della Credenziale siano gestiti correttamente e riportati.
  * - ISS-073
    - Error Handling
    - Convalidare la gestione degli errori nella convalida della catena di fiducia
    - Assicurarsi che gli errori nel processo di convalida della catena di fiducia siano gestiti correttamente e riportati.
  * - ISS-074
    - Error Handling
    - Convalidare la gestione degli errori nell'emissione differita
    - Assicurarsi che gli errori nel processo di emissione differita siano gestiti correttamente e riportati.
  * - ISS-075
    - Error Handling
    - Convalidare la gestione degli errori nella gestione delle notifiche
    - Assicurarsi che gli errori nel processo di gestione delle notifiche siano gestiti correttamente e riportati.
  * - ISS-076
    - Error Handling
    - Convalidare la gestione degli errori nell'autenticazione dell'Utente
    - Assicurarsi che gli errori nel processo di autenticazione dell'Utente siano gestiti correttamente e riportati.
  * - ISS-077
    - Error Handling
    - Convalidare la gestione degli errori nel consenso dell'Utente
    - Assicurarsi che gli errori nel processo di consenso dell'Utente siano gestiti correttamente e riportati.
  * - ISS-078
    - Error Handling
    - Convalidare la gestione degli errori nella notifica dell'Utente
    - Assicurarsi che gli errori nel processo di notifica dell'Utente siano gestiti correttamente e riportati.
  * - ISS-079
    - Error Handling
    - Convalidare la gestione degli errori nell'aggiornamento del set di attributi dell'Utente
    - Assicurarsi che gli errori nel processo di aggiornamento del set di attributi dell'Utente siano gestiti correttamente e riportati.
  * - ISS-080
    - Error Handling
    - Convalidare la gestione degli errori nell'aggiornamento del modello/formato dei dati
    - Assicurarsi che gli errori nel processo di aggiornamento del modello/formato dei dati siano gestiti correttamente e riportati.
  * - ISS-081
    - Error Handling
    - Convalidare la gestione degli errori nella scadenza della Credenziale
    - Assicurarsi che gli errori nel processo di scadenza della Credenziale siano gestiti correttamente e riportati.
  * - ISS-082
    - Error Handling
    - Convalidare la gestione degli errori nella riemissione della Credenziale
    - Assicurarsi che gli errori nel processo di riemissione della Credenziale siano gestiti correttamente e riportati.
  * - ISS-083
    - Error Handling
    - Convalidare la gestione degli errori nell'associazione della Credenziale
    - Assicurarsi che gli errori nel processo di associazione della Credenziale siano gestiti correttamente e riportati.
  * - ISS-084
    - Error Handling
    - Convalidare la gestione degli errori nella valutazione della fiducia della Credenziale
    - Assicurarsi che gli errori nel processo di valutazione della fiducia della Credenziale siano gestiti correttamente e riportati.
  * - ISS-085
    - Error Handling
    - Convalidare la gestione degli errori nel recupero dei metadati della Credenziale
    - Assicurarsi che gli errori nel processo di recupero dei metadati della Credenziale siano gestiti correttamente e riportati.
  * - ISS-086
    - Error Handling
    - Convalidare la gestione degli errori nella scoperta della Credenziale
    - Assicurarsi che gli errori nel processo di scoperta della Credenziale siano gestiti correttamente e riportati.
  * - ISS-087
    - Error Handling
    - Convalidare la gestione degli errori nella valutazione dell'offerta di Credenziale
    - Assicurarsi che gli errori nel processo di valutazione dell'offerta di Credenziale siano gestiti correttamente e riportati.
  * - ISS-088
    - Error Handling
    - Convalidare la gestione degli errori nell'accettazione dell'offerta di Credenziale
    - Assicurarsi che gli errori nel processo di accettazione dell'offerta di Credenziale siano gestiti correttamente e riportati.
  * - ISS-089
    - Error Handling
    - Convalidare la gestione degli errori nel rifiuto dell'offerta di Credenziale
    - Assicurarsi che gli errori nel processo di rifiuto dell'offerta di Credenziale siano gestiti correttamente e riportati.
  * - ISS-090
    - Error Handling
    - Convalidare la gestione degli errori nella revoca dell'offerta di Credenziale
    - Assicurarsi che gli errori nel processo di revoca dell'offerta di Credenziale siano gestiti correttamente e riportati.
  * - ISS-091
    - Error Handling
    - Convalidare la gestione degli errori nella scadenza dell'offerta di Credenziale
    - Assicurarsi che gli errori nel processo di scadenza dell'offerta di Credenziale siano gestiti correttamente e riportati.
  * - ISS-092
    - Error Handling
    - Convalidare la gestione degli errori nel rinnovo dell'offerta di Credenziale
    - Assicurarsi che gli errori nel processo di rinnovo dell'offerta di Credenziale siano gestiti correttamente e riportati.
  * - ISS-093
    - Error Handling
    - Convalidare la gestione degli errori nell'aggiornamento dell'offerta di Credenziale
    - Assicurarsi che gli errori nel processo di aggiornamento dell'offerta di Credenziale siano gestiti correttamente e riportati.
  * - ISS-094
    - Error Handling
    - Convalidare la gestione degli errori nella convalida dell'offerta di Credenziale
    - Assicurarsi che gli errori nel processo di convalida dell'offerta di Credenziale siano gestiti correttamente e riportati.
  * - ISS-095
    - Error Handling
    - Convalidare la gestione degli errori nella verifica dell'offerta di Credenziale
    - Assicurarsi che gli errori nel processo di verifica dell'offerta di Credenziale siano gestiti correttamente e riportati.
  * - ISS-096
    - Error Handling
    - Convalidare la gestione degli errori nella conferma dell'offerta di Credenziale
    - Assicurarsi che gli errori nel processo di conferma dell'offerta di Credenziale siano gestiti correttamente e riportati.
  * - ISS-097
    - Error Handling
    - Convalidare la gestione degli errori nella notifica dell'offerta di Credenziale
    - Assicurarsi che gli errori nel processo di notifica dell'offerta di Credenziale siano gestiti correttamente e riportati.
  * - ISS-098
    - Error Handling
    - Convalidare la gestione degli errori nella comunicazione dell'offerta di Credenziale
    - Assicurarsi che gli errori nel processo di comunicazione dell'offerta di Credenziale siano gestiti correttamente e riportati.
  * - ISS-099
    - Error Handling
    - Convalidare la gestione degli errori nella trasmissione dell'offerta di Credenziale
    - Assicurarsi che gli errori nel processo di trasmissione dell'offerta di Credenziale siano gestiti correttamente e riportati.
  * - ISS-100
    - Error Handling
    - Convalidare la gestione degli errori nella ricezione dell'offerta di Credenziale
    - Assicurarsi che gli errori nel processo di ricezione dell'offerta di Credenziale siano gestiti correttamente e riportati.
  * - ISS-101
    - Error Handling
    - Convalidare la gestione degli errori nell'elaborazione dell'offerta di Credenziale
    - Assicurarsi che gli errori nel processo di elaborazione dell'offerta di Credenziale siano gestiti correttamente e riportati.
  * - ISS-102
    - Error Handling
    - Convalidare la gestione degli errori nella gestione dell'offerta di Credenziale
    - Assicurarsi che gli errori nel processo di gestione dell'offerta di Credenziale siano gestiti correttamente e riportati.
  * - ISS-103
    - Error Handling
    - Convalidare la gestione degli errori nella gestione dell'offerta di Credenziale
    - Assicurarsi che gli errori nel processo di gestione dell'offerta di Credenziale siano gestiti correttamente e riportati.
  * - ISS-104
    - Error Handling
    - Convalidare la gestione degli errori nell'amministrazione dell'offerta di Credenziale
    - Assicurarsi che gli errori nel processo di amministrazione dell'offerta di Credenziale siano gestiti correttamente e riportati.
  * - ISS-105
    - Error Handling
    - Convalidare la gestione degli errori nel controllo dell'offerta di Credenziale
    - Assicurarsi che gli errori nel processo di controllo dell'offerta di Credenziale siano gestiti correttamente e riportati.
  * - ISS-106
    - Error Handling
    - Convalidare la gestione degli errori nella supervisione dell'offerta di Credenziale
    - Assicurarsi che gli errori nel processo di supervisione dell'offerta di Credenziale siano gestiti correttamente e riportati.
  * - ISS-107
    - Error Handling
    - Convalidare la gestione degli errori nella supervisione dell'offerta di Credenziale
    - Assicurarsi che gli errori nel processo di supervisione dell'offerta di Credenziale siano gestiti correttamente e riportati.
  * - ISS-108
    - Error Handling
    - Convalidare la gestione degli errori nel monitoraggio dell'offerta di Credenziale
    - Assicurarsi che gli errori nel processo di monitoraggio dell'offerta di Credenziale siano gestiti correttamente e riportati.
  * - ISS-109
    - Error Handling
    - Convalidare la gestione degli errori nella valutazione dell'offerta di Credenziale
    - Assicurarsi che gli errori nel processo di valutazione dell'offerta di Credenziale siano gestiti correttamente e riportati.
  * - ISS-110
    - Error Handling
    - Convalidare la gestione degli errori nella valutazione dell'offerta di Credenziale
    - Assicurarsi che gli errori nel processo di valutazione dell'offerta di Credenziale siano gestiti correttamente e riportati.

Matrice di Test per la Presentazione di Credenziali
---------------------------------------------------

Questa sezione fornisce l'insieme di casi di test per verificare la conformità delle implementazioni dei Verificatori di Credenziali alle regole tecniche definite nell'ecosistema IT-Wallet.


Matrice di Test per la Presentazione Remota di Credenziali
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Questa sezione definisce i casi di test relativi al flusso di presentazione remota.

.. note::
  I riferimenti ai piani di test ufficiali OpenID4VP aggiorneranno questa sezione nelle versioni future.

.. list-table::
  :class: longtable
  :widths: 15 15 35 35
  :header-rows: 1

  * - Test Case
    - Category
    - Description
    - Expected Result
  * - RPR-01
    - Same Device Flow
    - Verificare l'URL di reindirizzamento HTTP (302).
    - L'Istanza del Wallet riceve l'URL corretto.
  * - RPR-02
    - Cross Device Flow
    - Verificare la generazione del codice QR per l'Istanza del Wallet.
    - L'Istanza del Wallet scansiona il codice QR con successo.
  * - RPR-03
    - Cross Device Flow
    - Verificare che il codice QR contenga i parametri URL corretti.
    - L'Istanza del Wallet recupera l'URL con i parametri.
  * - RPR-04
    - Cross Device Flow
    - Testare la scansione del codice QR in condizioni di scarsa illuminazione.
    - Il codice QR viene scansionato con successo.
  * - RPR-05
    - Cross Device Flow
    - Verificare il livello di correzione degli errori del codice QR.
    - Il codice QR rimane leggibile se danneggiato.
  * - RPR-06
    - Cross Device Flow
    - Testare la scansione del codice QR con dispositivi diversi.
    - Il codice QR viene scansionato con successo.
  * - RPR-07
    - Request URI Method
    - Testare `request_uri_method` come `post`.
    - L'Istanza del Wallet invia i metadati tramite POST.
  * - RPR-08
    - Request URI Method
    - Testare `request_uri_method` come `get`.
    - L'Istanza del Wallet recupera l'Oggetto Richiesta tramite GET.
  * - RPR-09
    - Request URI Method
    - Testare l'assenza di `request_uri_method`.
    - L'Istanza del Wallet utilizza il metodo GET come predefinito.
  * - RPR-10
    - Metadata
    - Verificare che i parametri corrispondano ai metadati del verificatore di credenziali openid.
    - Verranno considerati solo i parametri consentiti.
  * - RPR-11
    - User Consent
    - Testare l'idoneità di un verificatore di credenziali nel richiedere attributi dell'utente.
    - L'utente può modificare la selezione dei dati relativi agli attributi opzionali.
  * - RPR-12
    - Authorization Response
    - Testare l'invio della risposta di presentazione.
    - La Relying Party riceve e convalida la risposta con state e nonce.
  * - RPR-13
    - Authorization Response
    - Verificare la crittografia della risposta.
    - La risposta è crittografata utilizzando la chiave pubblica della Relying Party.
  * - RPR-14
    - Error Handling
    - Testare la gestione dell'Oggetto Richiesta non valido.
    - Viene inviata una risposta di errore di autorizzazione.
  * - RPR-15
    - Error Handling
    - Verificare la registrazione degli errori da parte dell'Istanza del Wallet.
    - Gli errori vengono registrati in modo appropriato.
  * - RPR-16
    - Error Handling
    - Testare il recupero da `server_error`.
    - L'utente viene invitato a riprovare o a scansionare un nuovo codice QR.
  * - RPR-17
    - Relying Party Response
    - Verificare la gestione corretta della risposta.
    - La sessione dell'utente viene aggiornata, viene fornito l'URI di reindirizzamento.
  * - RPR-18
    - Relying Party Response
    - Testare l'assenza di `redirect_uri`.
    - Viene restituita una risposta di errore.
  * - RPR-19
    - Redirect URI
    - Testare il reindirizzamento all'endpoint della Relying Party.
    - L'utente viene reindirizzato correttamente.
  * - RPR-20
    - Redirect URI
    - Verificare la gestione di `redirect_uri` non valido.
    - Viene restituita una risposta di errore.
  * - RPR-21
    - User Consent
    - Verificare la visualizzazione dell'identità della Relying Party.
    - L'identità viene visualizzata chiaramente al Titolare.
  * - RPR-22
    - User Consent
    - Testare la revoca del consenso dell'utente.
    - L'utente può revocare il consenso prima dell'invio.
  * - RPR-23
    - Credential Presentation
    - Verificare la conformità del formato della risposta.
    - Ogni Credenziale aderisce al formato specificato.
  * - RPR-24
    - Authorization Response
    - Testare la gestione dei timeout della risposta.
    - I tentativi devono avere successo a meno che la risposta non venga acquisita.
  * - RPR-25
    - Error Handling
    - Verificare la gestione dei claim malformati nel payload di presentazione.
    - Viene inviata una risposta di errore di autorizzazione.
  * - RPR-26
    - Error Handling
    - Verificare la gestione dei claim malformati nelle credenziali presentate.
    - Viene inviata una risposta di errore di autorizzazione.
  * - RPR-27
    - Error Handling
    - Testare la gestione delle richieste scadute.
    - Il Titolare viene notificato della scadenza.
  * - RPR-28
    - Relying Party Response
    - Verificare l'inclusione del codice di risposta.
    - Il codice di risposta è crittograficamente casuale.
  * - RPR-29
    - Relying Party Response
    - Testare la gestione dei codici di risposta non validi.
    - Viene restituita una risposta di errore.
  * - RPR-30
    - Status Endpoint
    - Verificare la gestione dell'accesso non autorizzato.
    - L'accesso non autorizzato viene negato.
  * - RPR-31
    - Status Endpoint
    - Testare la gestione degli ID di sessione non validi.
    - Viene restituita una risposta di errore.
  * - RPR-32
    - Redirect URI
    - Verificare la gestione delle sessioni scadute.
    - Viene restituita una risposta di errore.
  * - RPR-33
    - Redirect URI
    - Testare la gestione degli errori del server.
    - Viene restituita una risposta di errore.
  * - RPR-34
    - Same Device Flow
    - Verificare la gestione delle condizioni di rete lente.
    - L'Istanza del Wallet riprova o notifica all'utente.
  * - RPR-35
    - Request URI Method
    - Testare la gestione di payload di metadati di grandi dimensioni.
    - I metadati vengono inviati con successo.
  * - RPR-36
    - Presentation Response
    - Verificare la gestione di payload di risposta di grandi dimensioni.
    - La risposta viene inviata con successo.
  * - RPR-37
    - Presentation Response
    - Testare la gestione dei fallimenti di crittografia della risposta.
    - Viene restituita una risposta di errore.
  * - RPR-38
    - Error Handling
    - Verificare la gestione delle firme non valide.
    - Viene inviata una risposta di errore di autorizzazione.
  * - RPR-39
    - Error Handling
    - Testare la gestione dei valori nonce non validi.
    - Viene restituita una risposta di errore.
  * - RPR-40
    - Relying Party Response
    - Verificare la gestione delle risposte malformate.
    - Viene restituita una risposta di errore.
  * - RPR-41
    - Relying Party Response
    - Testare la gestione dei parametri di risposta mancanti.
    - Viene restituita una risposta di errore.
  * - RPR-42
    - Status Endpoint
    - Verificare la gestione dei timeout di sessione.
    - Viene restituita una risposta di errore.
  * - RPR-43
    - Status Endpoint
    - Testare la gestione dei codici di stato non validi.
    - Viene restituita una risposta di errore.
  * - RPR-44
    - Redirect URI
    - Verificare la gestione delle sessioni utente non valide.
    - Viene restituita una risposta di errore.
  * - RPR-45
    - Redirect URI
    - Testare la gestione dei servizi non disponibili.
    - Viene restituita una risposta di errore.
  * - RPR-46
    - Same Device Flow
    - Verificare la gestione delle cancellazioni dell'utente.
    - L'utente può annullare il processo.
  * - RPR-47
    - Cross Device Flow
    - Testare la scansione del codice QR con app diverse.
    - Il codice QR viene scansionato con successo.
  * - RPR-48
    - Cross Device Flow
    - Verificare la scansione del codice QR con illuminazione diversa.
    - Il codice QR viene scansionato con successo.
  * - RPR-49
    - Request URI Method
    - Testare la gestione dei tipi di contenuto non supportati.
    - Viene restituita una risposta di errore.
  * - RPR-50
    - User Consent
    - Verificare la notifica all'utente delle modifiche al consenso.
    - L'utente viene informato sulle modifiche al consenso.
  * - RPR-51
    - User Consent
    - Testare il consenso dell'utente per i dati sensibili.
    - L'utente può acconsentire ai dati sensibili.
  * - RPR-52
    - Authorization Response
    - Verificare la gestione dei fallimenti di decrittografia della risposta.
    - Viene restituita una risposta di errore.
  * - RPR-53
    - Authorization Response
    - Testare la gestione dei controlli di integrità della risposta.
    - L'integrità della risposta viene verificata.
  * - RPR-54
    - Relying Party Response
    - Verificare la gestione dei fallimenti di convalida della risposta.
    - Viene restituita una risposta di errore.
  * - RPR-55
    - Relying Party Response
    - Testare la gestione degli errori di elaborazione della risposta.
    - Viene restituita una risposta di errore.
  * - RPR-56
    - Protected Resource Endpoint
    - Verificare la gestione dell'accesso non autorizzato alla sessione.
    - L'accesso non autorizzato viene negato.
  * - RPR-57
    - Redirect URI
    - Verificare la gestione dei parametri di reindirizzamento non validi.
    - Viene restituita una risposta di errore.
  * - RPR-58
    - Redirect URI
    - Testare la gestione dei fallimenti di reindirizzamento.
    - Viene restituita una risposta di errore.
  * - RPR-59
    - Same Device Flow
    - Verificare la gestione delle interruzioni dell'utente.
    - L'utente può riprendere o annullare il processo.
  * - RPR-60
    - Request URI Method
    - Testare la gestione dei metodi HTTP non validi.
    - Viene restituita una risposta di errore.
  * - RPR-61
    - User Consent
    - Verificare la notifica all'utente della revoca del consenso.
    - L'utente viene informato sulla revoca del consenso.
  * - RPR-62
    - User Consent
    - Testare il consenso dell'utente per i dati opzionali.
    - L'utente può acconsentire ai dati opzionali.
  * - RPR-63
    - Authorization Response
    - Verificare la gestione dei fallimenti di firma della risposta.
    - Viene restituita una risposta di errore.
  * - RPR-64
    - Authorization Response
    - Testare la gestione degli errori di formato della risposta.
    - Viene restituita una risposta di errore.
  * - RPR-65
    - Error Handling
    - Verificare la gestione delle firme JWT non valide.
    - Viene inviata una risposta di errore di autorizzazione.
  * - RPR-66
    - Error Handling
    - Testare la gestione dei claim JWT non validi.
    - Viene restituita una risposta di errore.
  * - RPR-67
    - Relying Party Response
    - Verificare la gestione degli errori di analisi della risposta.
    - Viene restituita una risposta di errore.
  * - RPR-68
    - Relying Party Response
    - Testare la gestione degli errori di timeout della risposta.
    - Viene restituita una risposta di errore.
  * - RPR-69
    - Status Endpoint
    - Verificare la gestione della scadenza della sessione.
    - Viene restituita una risposta di errore.
  * - RPR-70
    - Status Endpoint
    - Testare la gestione degli errori di rinnovo della sessione.
    - Viene restituita una risposta di errore.
  * - RPR-71
    - Redirect URI
    - Verificare la gestione degli errori di loop di reindirizzamento.
    - Viene restituita una risposta di errore.
  * - RPR-72
    - Redirect URI
    - Testare la gestione degli errori di sicurezza del reindirizzamento.
    - Viene restituita una risposta di errore.
  * - RPR-73
    - Same Device Flow
    - Verificare la gestione dei timeout dell'utente.
    - L'utente viene notificato del timeout.
  * - RPR-74
    - Cross Device Flow
    - Testare la scansione del codice QR con dispositivi diversi.
    - Il codice QR viene scansionato con successo.
  * - RPR-75
    - Cross Device Flow
    - Verificare la scansione del codice QR con app diverse.
    - Il codice QR viene scansionato con successo.
  * - RPR-76
    - Request URI Method
    - Testare la gestione dei metodi HTTP non supportati.
    - Viene restituita una risposta di errore.


Matrice di Test per la Presentazione di Credenziali di Prossimità
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Questa sezione definisce i casi di test generali relativi al flusso di presentazione di prossimità.

.. note::
  I riferimenti ai piani di test ISO-1813-5 aggiorneranno questa sezione nelle versioni future.


.. list-table::
  :class: longtable
  :widths: 15 15 35 35
  :header-rows: 1

  * - Test Case
    - Category
    - Description
    - Expected Result

  * - PPR-001
    - Device Engagement
    - Testare l'avvio del coinvolgimento del dispositivo utilizzando il codice QR.
    - Il coinvolgimento del dispositivo viene avviato con successo e il codice QR viene scansionato.

  * - PPR-002
    - Session Establishment
    - Verificare l'instaurazione della sessione con le chiavi di sessione corrette.
    - La sessione viene stabilita in modo sicuro con le chiavi di sessione corrette.

  * - PPR-003
    - Communication
    - Testare la trasmissione della richiesta mdoc tramite BLE.
    - La richiesta mdoc viene trasmessa in modo sicuro tramite BLE.

  * - PPR-004
    - User Authentication
    - Convalidare l'autenticazione dell'utente tramite WSCA.
    - L'utente viene autenticato con successo utilizzando WSCA.

  * - PPR-005
    - Attribute Consent
    - Verificare il consenso dell'utente per il rilascio degli attributi.
    - L'utente acconsente al rilascio degli attributi richiesti.

  * - PPR-006
    - Data Retrieval
    - Testare il recupero delle Credenziali Digitali mdoc.
    - Le Credenziali Digitali mdoc vengono recuperate con successo.

  * - PPR-007
    - Session Termination
    - Verificare la terminazione della sessione dopo lo scambio di dati.
    - La sessione viene terminata e le chiavi vengono distrutte.

  * - PPR-008
    - Error Handling
    - Testare la gestione delle chiavi di sessione non valide.
    - Viene visualizzato un messaggio di errore appropriato per le chiavi non valide.

  * - PPR-009
    - BLE Connection
    - Testare la stabilità della connessione BLE durante lo scambio di dati.
    - La connessione BLE rimane stabile durante tutto lo scambio.

  * - PPR-010
    - Document Verification
    - Verificare l'integrità dei documenti ricevuti.
    - I documenti vengono verificati e l'integrità è confermata.

  * - PPR-011
    - Security
    - Testare la crittografia delle richieste e risposte mdoc.
    - Tutte le richieste e risposte mdoc sono crittografate correttamente.

  * - PPR-012
    - User Interface
    - Verificare l'interfaccia utente per il consenso agli attributi.
    - L'interfaccia utente visualizza chiaramente la richiesta di consenso agli attributi.

  * - PPR-013
    - Error Handling
    - Testare la risposta ai tipi di documento non supportati.
    - Il sistema restituisce un errore appropriato per i tipi di documento non supportati.

  * - PPR-014
    - Performance
    - Misurare il tempo impiegato per l'instaurazione della sessione.
    - La sessione viene stabilita entro limiti di tempo accettabili.

  * - PPR-015
    - Compatibility
    - Verificare la compatibilità con diversi dispositivi mobili.
    - Il sistema funziona perfettamente su vari dispositivi mobili.

  * - PPR-016
    - Data Integrity
    - Testare l'integrità dei dati durante la trasmissione.
    - L'integrità dei dati viene mantenuta durante la trasmissione.

  * - PPR-017
    - Session Management
    - Testare la gestione della sessione sotto carico elevato.
    - Le sessioni vengono gestite efficacemente in condizioni di carico elevato.

  * - PPR-018
    - BLE Connection
    - Testare la riconnessione dopo la disconnessione BLE.
    - Il sistema si riconnette con successo dopo la disconnessione BLE.

  * - PPR-019
    - User Experience
    - Valutare l'esperienza dell'utente durante il flusso di prossimità.
    - Gli utenti riportano un'esperienza positiva con il flusso di prossimità.

  * - PPR-020
    - Security
    - Testare la resistenza agli attacchi di replay.
    - Il sistema è resistente agli attacchi di replay.

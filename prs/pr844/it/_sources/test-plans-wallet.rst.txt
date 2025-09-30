Matrice di Test per la Soluzione Wallet
---------------------------------------

Questa sezione fornisce l'insieme di casi di test per verificare la conformità di un'implementazione di Soluzione Wallet alle regole tecniche definite nell'ecosistema IT-Wallet.
Il piano di test è basato sui requisiti obbligatori (dichiarazioni MUST) estratti dai seguenti documenti:

- Wallet Solution
- Wallet Instance Revocation
- Wallet Attestation Issuance
- Backup and Restore


.. list-table::
  :class: longtable
  :widths: 15 15 35 35
  :header-rows: 1

  * - Test Case ID
    - Purpose
    - Description
    - Expected Result
  * - WS-001
    - Wallet Initialization
    - Il Wallet Solution DEVE assicurare che ogni Wallet Instance sia generata secondo le specifiche e includa un identificatore univoco e chiavi crittografiche legate a un elemento sicuro.
    - Una Wallet Instance conforme viene generata con identificatori corretti e legami sicuri.
  * - WS-002
    - User Interaction
    - Il Wallet Solution DEVE richiedere e ottenere il consenso esplicito dell'Utente durante l'inizializzazione delIl Wallet Instance.
    - Il Wallet Instance viene attivata solo dopo aver ottenuto il consenso verificabile dell'Utente.
  * - WS-003
    - Security
    - Il Wallet Solution DEVE memorizzare le chiavi private all'interno di un Secure Hardware Element o storage sicuro equivalente.
    - Tutti i materiali delle chiavi private sono inaccessibili dal sistema operativo o da qualsiasi applicazione esterna alIl Wallet Solution.
  * - WS-004
    - Attestation
    - Il Wallet DEVE essere in grado di generare e presentare una Wallet Attestation quando richiesto dalle Relying Party o dagli Issuer.
    - Attestation valide e verificabili vengono generate includendo prove di integrità e origine.
  * - WS-005
    - Attestation
    - Il Wallet DEVE supportare l'elaborazione delle Wallet Attestation Request e la generazione di risposte appropriate in conformità con eIDAS.
    - Il Wallet interpreta e soddisfa correttamente le richieste di attestation includendo i dati del soggetto e le firme crittografiche.
  * - WS-006
    - Remote Credential Presentation
    - Il Wallet Solution DEVE implementare sia il flusso di presentazione di prossimità che remoto, assicurando la selezione delle Verifiable Credential, l'integrità e l'interazione dell'Utente.
    - La presentazione delle Verifiable Credential ha successo, è corretta e sotto il controllo dell'Utente.
  * - WS-007
    - Credential Issuance
    - Il Wallet DEVE supportare il flusso Issuer per ricevere e memorizzare Verifiable Credentials.
    - Le Credential vengono memorizzate in modo sicuro e analizzate correttamente secondo la struttura definita.
  * - WS-008
    - Revocation
    - Il Wallet DEVE permettere all'Utente di attivare una Wallet Instance Revocation in qualsiasi momento.
    - La revoca viene eseguita e i materiali crittografici vengono eliminati in modo sicuro o resi inutilizzabili.
  * - WS-009
    - Revocation
    - AlIl Wallet Instance Revocation, Il Wallet Solution DEVE notificare i sistemi backend rilevanti per propagare la revoca.
    - Lo stato di revoca si riflette in tutti i componenti dell'ecosistema (es. Issuer, Verifier).
  * - WS-010
    - Backup & Restore
    - Il Wallet DEVE supportare operazioni di Backup e Restore crittografate in conformità con i requisiti di privacy e integrità.
    - Il Backup è crittografato e legato all'Utente; l'operazione di Restore verifica l'integrità e l'autenticità dell'Utente prima del recupero.
  * - WS-011
    - Backup & Restore
    - Il Wallet DEVE gestire le chiavi di crittografia del backup in modo sicuro e derivarle da segreti controllati dall'Utente o credenziali.
    - Nessuna entità non autorizzata può decrittografare i backup; i backup diventano inutili se manomessi.
  * - WS-012
    - Backup & Restore
    - Il Wallet DEVE autenticare l'Utente prima di permettere il Restore.
    - Il Restore ha successo solo dopo l'autenticazione verificata dell'Utente utilizzando metodi approvati (es. biometrici, PIN, challenge crittografico).
  * - WS-013
    - Attestation
    - Il Wallet DEVE rilevare le Attestation scadute e supportare i flussi di refresh.
    - Le Attestation scadute non vengono utilizzate; il refresh viene attivato automaticamente o tramite prompt dell'Utente.
  * - WS-014
    - Compliance
    - Tutte le operazioni inclusi Issuance, Presentation, Attestation e Revocation DEVONO conformarsi agli standard europei.
    - Una traccia verificabile delle operazioni conformi viene mantenuta; non si osserva alcuna deviazione dal comportamento eIDAS 2.0.
  * - WS-015
    - User Interaction
    - Il Wallet DEVE operare sotto il principio del controllo dell'Utente e della minimizzazione dei dati.
    - Solo i dati esplicitamente consenziti e richiesti vengono utilizzati e trasmessi; tutte le operazioni richiedono azioni esplicite dell'Utente.
  * - WS-016
    - Credential Presentation
    - Il Wallet DEVE supportare la presentazione offline delle Verifiable Credential quando consentito.
    - Le Credential vengono presentate in modo sicuro anche in modalità offline, mantenendo integrità e autenticità.
  * - WS-017
    - Security
    - Il Wallet DEVE assicurare protezioni anti-replay durante la presentazione delle credenziali.
    - Ogni presentazione è crittograficamente unica e legata alla richiesta del Verifier.
  * - WS-018
    - Revocation
    - Il Wallet DEVE registrare e rendere verificabile il processo di revoca delle Wallet Instance.
    - Log completi e resistenti alla manomissione sono disponibili per l'ispezione su richiesta.
  * - WS-019
    - Security
    - Il Wallet DEVE stabilire canali mutuamente autenticati e crittografati durante tutte le interazioni.
    - Tutti i messaggi sono protetti contro intercettazione, modifica o impersonificazione.
  * - WS-020
    - Security
    - Il Wallet DEVE bloccarsi e/o revocare Il Wallet Instance al rilevamento di manomissioni.
    - Il Wallet diventa inoperabile e la revoca viene attivata se la manomissione è confermata.
  * - WS-021
    - Security
    - Il Wallet DEVE eseguire Device Attestation utilizzando meccanismi specifici della piattaforma come Play Integrity (Android) o DC App Attest (iOS) durante la creazione delIl Wallet Instance.
    - La Device Attestation ha successo e i risultati sono inclusi nel payload delIl Wallet Attestation.
  * - WS-022
    - Attestation
    - Il Wallet Attestation DEVE includere una firma utilizzando Il Wallet Binding Key, e la catena di certificati DEVE essere verificabile fino a una root attendibile.
    - La firma è presente, valida e verificabile utilizzando la catena di certificati fornita.
  * - WS-023
    - Attestation
    - Il Wallet DEVE includere un risultato di Device Attestation nella struttura delIl Wallet Attestation.
    - Un oggetto Device Attestation valido (risultato Play Integrity o DC App Attest) è incorporato nell'Attestation.
  * - WS-024
    - Backup & Restore
    - Durante il Restore, Il Wallet DEVE validare l'integrità del file di backup crittografato utilizzando un meccanismo di controllo dell'integrità.
    - Il Wallet rifiuta di ripristinare un file di backup manomesso o corrotto.
  * - WS-025
    - Revocation
    - In caso di Wallet Instance Revocation, Il Wallet DEVE eliminare tutte le Verifiable Credential memorizzate localmente.
    - Nessun dato di credenziale rimane accessibile dopo che la revoca è stata attivata.
  * - WS-026
    - Revocation
    - Il Wallet DEVE notificare il Wallet Backend con una Revocation Request che contiene un parametro 'status'  impostato a 'REVOKED'.
    - La Revocation Request viene accettata e lo stato di revoca viene aggiornato nel backend.
  * - WS-027
    - Security
    - Il Wallet DEVE prevenire il riutilizzo di Wallet Binding Key revocate o credenziali in future Wallet Instance.
    - Qualsiasi tentativo di riutilizzo viene rilevato e bloccato.
  * - WS-028
    - Attestation
    - Il Wallet DEVE supportare il refresh dell'Attestation tramite l'API definita esposta dal Wallet Backend.
    - L'Attestation viene rinnovata e la nuova versione viene accettata dai Verifier e dagli Issuer.
  * - WS-029
    - Backup & Restore
    - La crittografia del Backup DEVE utilizzare algoritmi di crittografia forti e conformi agli standard (es. AES-GCM).
    - Il file di backup crittografato è resistente ad attacchi brute-force e crittografici noti.
  * - WS-030
    - User Interaction
    - Il Wallet DEVE richiedere all'Utente di confermare l'intento prima di qualsiasi operazione distruttiva come Revocation o Credential Deletion.
    - Le azioni distruttive vengono eseguite solo dopo la conferma esplicita dell'Utente.
  * - WS-031
    - Attestation
    - Il Wallet DEVE generare una Wallet Attestation contenente informazioni sullo stato di integrità del dispositivo, utilizzando Play Integrity API su Android.
    - Il Wallet Attestation include un payload Play Integrity valido con il campo 'MEETS_DEVICE_INTEGRITY' impostato.
  * - WS-032
    - Attestation
    - Il Wallet DEVE generare una Wallet Attestation utilizzando DeviceCheck App Attest su iOS e includere il risultato dell'attestation nelIl Wallet Attestation.
    - Il Wallet Attestation include una risposta JWT DC App Attest valida firmata da Apple.
  * - WS-033
    - Security
    - Il Wallet DEVE verificare che la firma del token Play Integrity sia valida e emessa da Google.
    - Il Wallet rifiuta token Play Integrity non validi o contraffatti.
  * - WS-034
    - Security
    - Il Wallet DEVE validare che il valore 'nonce' utilizzato in Play Integrity sia crittograficamente legato alIl Wallet Instance.
    - Qualsiasi manomissione del nonce viene rilevata e porta al rifiuto dell'Attestation.
  * - WS-035
    - Attestation
    - Il Wallet DEVE inviare Il Wallet Attestation al Wallet Backend durante la registrazione.
    - Il Wallet Backend riceve l'attestation e ne verifica la validità.
  * - WS-036
    - Backup & Restore
    - Il Wallet DEVE crittografare i backup utilizzando una chiave simmetrica derivata dai segreti dell'Utente.
    - Il backup non può essere decrittografato senza i materiali di autenticazione originali dell'Utente.
  * - WS-037
    - Backup & Restore
    - Il Wallet DEVE includere metadata nel backup che identificano la versione e il timestamp di creazione.
    - Il processo di Restore legge e verifica i metadata del backup prima di procedere.
  * - WS-038
    - Revocation
    - Il Wallet DEVE inviare una Revocation Request all’endpoint del Backend, includendo l’ID delIl Wallet come parametro nel path dell’URL.
    - Il backend elabora la revoca e aggiorna lo stato delIl Wallet a revocata.
  * - WS-039
    - Revocation
    - Il Wallet DEVE non permettere ulteriori Credential Issuance o Presentation dopo la revoca.
    - Tutte le operazioni vengono bloccate una volta che Il Wallet è revocata.
  * - WS-040
    - Credential Issuance
    - Il Wallet DEVE validare la struttura della Credential Offer ricevuta dall'Issuer.
    - Il Wallet accetta solo Credential Offer che corrispondono al formato e alla firma previsti.
  * - WS-041
    - Credential Issuance
    - Il Wallet DEVE assicurare che l'Utente acconsenta a ricevere una nuova Credential.
    - Nessuna Credential viene memorizzata senza l'approvazione esplicita dell'Utente.
  * - WS-042
    - Credential Presentation
    - Il Wallet DEVE verificare la Presentation Request del Verifier prima di rispondere.
    - Richieste non valide o malformate vengono rifiutate.
  * - WS-043
    - Security
    - Il Wallet DEVE firmare le Verifiable Presentations con la chiave privata corretta legata alIl Wallet Instance.
    - I Verifier sono in grado di validare la firma e fidarsi della presentazione.
  * - WS-044
    - User Interaction
    - Il Wallet DEVE richiedere all'Utente prima di inviare una Verifiable Credential a un Verifier.
    - Nessuna credenziale viene condivisa senza la conferma esplicita dell'Utente.
  * - WS-045
    - Backup & Restore
    - Il Wallet DEVE permettere all'Utente di eliminare tutti i dati di backup memorizzati.
    - Tutti i materiali di backup vengono eliminati in modo sicuro e non possono essere recuperati.
  * - WS-046
    - Revocation
    - Se Il Wallet viene ripristinata su un nuovo dispositivo, DEVE controllare se Il Wallet Instance originale era stata revocata.
    - Le Wallet Instance revocate non possono essere ripristinate.
  * - WS-047
    - Security
    - Il Wallet DEVE verificare la validità temporale delle Credential ricevute (es. issuanceDate, expirationDate).
    - Le credenziali scadute sono marcate come non valide e non vengono utilizzate.
  * - WS-048
    - Attestation
    - Il Wallet DEVE includere la chiave pubblica delIl Wallet Binding Key nelIl Wallet Attestation.
    - I Verifier e gli Issuer possono validare le firme effettuate con la corrispondente chiave privata.
  * - WS-049
    - Credential Presentation
    - Il Wallet DEVE supportare la Selective Disclosure degli attributi delle Credential.
    - Solo i campi selezionati sono inclusi nella presentazione inviata al Verifier.
  * - WS-050
    - Credential Presentation
    - Il Wallet DEVE permettere all'Utente di visualizzare in anteprima quali attributi delle Credential saranno divulgati prima della conferma.
    - All'Utente viene mostrato l'esatto dato da condividere e lo approva esplicitamente.
  * - WS-051
    - Proximity Flow
    - Il Wallet DEVE avviare il flusso di prossimità solo dopo il consenso esplicito dell'Utente di interagire con una Mobile Relying Party Instance.
    - Il flusso di presentazione di prossimità delIl Wallet viene bloccato a meno che l'Utente non abbia approvato la richiesta.
  * - WS-052
    - Proximity Flow
    - Il Wallet DEVE validare l'Access Certificate presentato da una Mobile Relying Party Instance prima di procedere.
    - Se l'Access Certificate è mancante, non valido o scaduto, Il Wallet DEVE rifiutare la richiesta.
  * - WS-053
    - Proximity Flow
    - Il Wallet DEVE visualizzare una disclaimer quando l'Access Certificate è scaduto ma ancora all'interno del periodo di grazia consentito.
    - La disclaimer viene mostrata chiaramente all'Utente e la presentazione procede solo dopo il consenso.
  * - WS-054
    - Relying Party Instance
    - Il Wallet DEVE applicare il controllo che lo stato della Relying Party Instance sia 'Verified' prima di permettere la presentazione delle credenziali.
    - Il Wallet nega il flusso se la Relying Party Instance è in qualsiasi stato diverso da 'Verified'.
  * - WS-055
    - Security
    - Il Wallet DEVE registrare qualsiasi tentativo di presentazione fallito a causa di stato non valido della Relying Party Instance o Access Certificate scaduto.
    - Un log di eventi di sicurezza viene generato e memorizzato in modo sicuro.
  * - WS-056
    - Interoperability
    - Il Wallet DEVE supportare la comunicazione con le Relying Party Instance utilizzando QR code standardizzati per la negoziazione di sessione come definito nella specifica.
    - Il Wallet legge e analizza con successo i QR code e avvia la sessione secondo il protocollo.
  * - WS-057
    - Proximity Flow
    - Il Wallet DEVE stabilire una sessione sicura e autenticata con la Mobile Relying Party Instance utilizzando chiavi effimere prima della presentazione.
    - Le chiavi di sessione vengono negoziate e verificate, e tutta la comunicazione è crittografata.
  * - WS-058
    - Credential Presentation
    - Il Wallet DEVE permettere all'Utente di scegliere quale Credential presentare a una Relying Party Instance anche nel flusso di prossimità.
    - L'interfaccia di selezione delle Credential viene mostrata all'Utente durante il flusso di prossimità.
  * - WS-059
    - Security
    - Il Wallet DEVE interrompere la sessione se la Relying Party Instance non riesce a dimostrare il possesso della chiave privata associata all'Access Certificate.
    - La sessione viene terminata e nessun dato di Credential viene divulgato.
  * - WS-060
    - User Interaction
    - Il Wallet DEVE indicare chiaramente all'Utente quando una richiesta di presentazione proviene da una Mobile Relying Party Instance utilizzando un canale di prossimità.
    - La fonte della richiesta viene mostrata prima di permettere alla presentazione di procedere.

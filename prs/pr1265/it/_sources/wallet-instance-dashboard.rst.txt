.. include:: ../common/common_definitions.rst


Dashboard dell’Istanza del Wallet e Registrazione delle Transazioni
===================================================================

L’Istanza del Wallet DEVE mantenere un registro delle transazioni sicuro e locale al Wallet. Il registro garantisce trasparenza, tracciabilità e consapevolezza dell’Utente rispetto alle azioni eseguite tramite l’Istanza del Wallet, come definito in `EIDAS-ARF`_ (Annex 2.02 HLRs, Topic 19). Il registro DEVE coprire tutte le transazioni (incluse quelle non completate) nelle seguenti categorie:

- rilascio e ri-rilascio delle Credenziali.
- presentazione delle Credenziali alle Relying Party.
- richieste di cancellazione dei dati inviate alle Relying Party.

Per ciascuna di tali transazioni, l’Istanza del Wallet DEVE creare un record di transazione corrispondente. Il record contiene gli elementi informativi previsti dai requisiti ARF applicabili per la relativa categoria di registrazione. Ove applicabile, l’Istanza del Wallet DEVE aggiornare il record con l’esito finale.

Per le transazioni di presentazione, i valori degli attributi NON DEVONO essere registrati. Qualora una richiesta di presentazione contenga dati transazionali, l’Istanza del Wallet DEVE registrare il valore di tali dati transazionali esclusivamente nella misura esplicitamente richiesta da `EUDI-TS 12`_. La registrazione resta collegata all’attestazione richiesta. La registrazione rispetta i principi di minimizzazione dei dati. In assenza di tale requisito, i valori dei dati transazionali NON DEVONO essere registrati.

Per supportare l’accesso dell’Utente al registro delle transazioni, l’Istanza del Wallet DEVE fornire un’interfaccia di dashboard. La dashboard consente all’Utente di visualizzare una panoramica dei record di transazione presenti nel registro. La dashboard consente all’Utente di accedere ai dettagli dei singoli record. La dashboard consente all’Utente di esportare e cancellare i record. Ove una transazione coinvolga una Relying Party, la dashboard consente all’Utente di avviare una richiesta di cancellazione dei dati verso la relativa Relying Party, utilizzando le informazioni di contatto registrate se disponibili.

Il Fornitore del Wallet DEVE proteggere la riservatezza, l’integrità e l’autenticità del registro delle transazioni e di eventuali oggetti di log esportati in conformità a `EUDI-TS 10`_. L’accesso al registro DEVE essere limitato all’Utente e all’Istanza del Wallet.

I record DEVONO essere conservati per almeno il periodo minimo previsto dalla normativa applicabile, come definito in :ref:`log-retention-policy:Politiche Generali di Conservazione dei Log`. Qualora limiti di spazio richiedano una cancellazione automatica, l’Istanza del Wallet DEVE notificare l’Utente tramite la dashboard, avvertire delle possibili conseguenze e offrire la possibilità di esportare i record interessati prima della cancellazione.

Esportazione e Cancellazione dei Record di Transazione
""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Esportazione**: la dashboard DEVE consentire all’Utente di esportare uno o più record di transazione in un file utilizzando il formato comune e le misure di sicurezza definite in `EUDI-TS 10`_.

Il file esportato DEVE poter essere salvato in una posizione di archiviazione esterna o remota scelta dall’Utente, tra le opzioni di archiviazione supportate dall’Istanza del Wallet.

Questa esportazione è il download dei record di transazione. Il ripristino del registro delle transazioni in un'Istanza del Wallet ricevente è specificato in :ref:`backup-restore:Migrazione verso una Soluzione Wallet diversa`.

**Cancellazione**: la dashboard DEVE consentire all’Utente di cancellare uno o più record di transazione dall’Istanza del Wallet in qualsiasi momento.

Prima di cancellare qualsiasi record di transazione, l’Istanza del Wallet DEVE mostrare all’Utente un avviso chiaro sulle possibili conseguenze per i diritti dell’Utente in materia di protezione dei dati.

La cancellazione dei record di transazione DEVE:

- applicarsi esclusivamente alle copie locali al Wallet dei record.
- essere irreversibile per l’Istanza del Wallet una volta completata.

L’Istanza del Wallet DEVE continuare a proteggere eventuali record di transazione rimanenti in conformità ai requisiti di riservatezza, integrità e autenticità definiti per il registro delle transazioni nella presente sezione.

Nessuna entità diversa dall’Utente PUÒ cancellare i record di transazione.



.. include:: ../common/common_definitions.rst


Dashboard dell’Istanza del Wallet e Registrazione delle Transazioni
===================================================================

L’Istanza del Wallet DEVE mantenere un registro delle transazioni sicuro e locale al Wallet, al fine di garantire trasparenza, tracciabilità e consapevolezza dell’Utente rispetto alle azioni eseguite tramite l’Istanza del Wallet, come definito in `EIDAS-ARF`_ (Annex 2.02 HLRs, Topic 19). Il registro DEVE coprire tutte le transazioni (incluse quelle non completate) nelle seguenti categorie:

- rilascio e ri-rilascio delle credenziali;
- presentazione delle credenziali alle Relying Party;
- richieste di cancellazione dei dati inviate alle Relying Party.

Per ciascuna di tali transazioni, l’Istanza del Wallet DEVE creare un record di transazione corrispondente contenente gli elementi informativi previsti dai requisiti ARF applicabili per la relativa categoria di registrazione, e DEVE aggiornarlo con l’esito finale, ove applicabile.

Per le transazioni di presentazione, i valori degli attributi NON DEVONO essere registrati. Qualora una richiesta di presentazione contenga dati transazionali, l’Istanza del Wallet DEVE registrare il valore di tali dati transazionali esclusivamente nella misura esplicitamente richiesta da `EUDI-TS 12`_ in relazione all’attestazione richiesta e nel rispetto dei principi di minimizzazione dei dati. In assenza di tale requisito, i valori dei dati transazionali NON DEVONO essere registrati.

Per supportare l’accesso dell’Utente al registro delle transazioni, l’Istanza del Wallet DEVE fornire un’interfaccia di dashboard che consenta all’Utente di visualizzare una panoramica dei record di transazione presenti nel registro, accedere ai dettagli dei singoli record, esportare e cancellare i record e, ove una transazione coinvolga una Relying Party, avviare una richiesta di cancellazione dei dati verso la relativa Relying Party (utilizzando, se disponibili, le informazioni di contatto registrate).

Il Fornitore del Wallet DEVE proteggere la riservatezza, l’integrità e l’autenticità del registro delle transazioni e di eventuali oggetti di log esportati in conformità a `EUDI-TS 10`_; l’accesso al registro DEVE essere limitato all’Utente e all’Istanza del Wallet.

I record DEVONO essere conservati per almeno il periodo minimo previsto dalla normativa applicabile, come definito in :ref:`log-retention-policy:Politiche Generali di Conservazione dei Log`. Qualora limiti di spazio richiedano una cancellazione automatica, l’Istanza del Wallet DEVE notificare l’Utente tramite la dashboard, avvertire delle possibili conseguenze e offrire la possibilità di esportare i record interessati prima della cancellazione.

Esportazione e Cancellazione dei Record di Transazione
""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Esportazione**: la dashboard DEVE consentire all’Utente di esportare uno o più record di transazione in un file utilizzando il formato comune e le misure di sicurezza definite in `EUDI-TS 10`_.

Il file esportato DEVE poter essere salvato in una posizione di archiviazione esterna o remota scelta dall’Utente, tra le opzioni di archiviazione supportate dall’Istanza del Wallet.

**Cancellazione**: la dashboard DEVE consentire all’Utente di cancellare uno o più record di transazione dall’Istanza del Wallet in qualsiasi momento.

Prima di cancellare qualsiasi record di transazione, l’Istanza del Wallet DEVE mostrare all’Utente un avviso chiaro sulle possibili conseguenze per i diritti dell’Utente in materia di protezione dei dati.

La cancellazione dei record di transazione DEVE:

- applicarsi esclusivamente alle copie locali al Wallet dei record;
- essere irreversibile per l’Istanza del Wallet una volta completata.

L’Istanza del Wallet DEVE continuare a proteggere eventuali record di transazione rimanenti in conformità ai requisiti di riservatezza, integrità e autenticità definiti per il registro delle transazioni nella presente sezione.

Nessuna entità diversa dall’Utente PUÒ cancellare i record di transazione.



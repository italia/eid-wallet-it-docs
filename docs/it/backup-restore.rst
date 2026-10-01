.. include:: ../common/common_definitions.rst


Backup e Ripristino
===================

La funzionalità di **Backup e Ripristino** diventa rilevante quando l'Utente desidera cambiare dispositivo e/o Soluzione Wallet per accedere nuovamente alle Credenziali Elettroniche precedentemente emesse.

- Il dispositivo mobile è stato **perso**, **rubato**, **danneggiato** o **compromesso** (ad esempio, a causa di accesso non autorizzato).
- L'Utente sostituisce un'Istanza del Wallet esistente con una nuova istanza della stessa Soluzione Wallet.
- L'Utente ha cambiato il proprio dispositivo mobile e deve configurare la Soluzione Wallet sul nuovo dispositivo.
- L'Utente esegue un ripristino delle impostazioni di fabbrica sul telefono attuale e deve configurare nuovamente la Soluzione Wallet.

L'Istanza del Wallet DEVE eseguire il backup, il ripristino, l'esportazione e la portabilità di cui alla presente sezione in modo semplice, trasparente e tracciabile per l'Utente.

L'Istanza del Wallet DEVE consentire all'Utente di scaricare i dati dell'Utente, gli attestati elettronici di attributi e le configurazioni, nella misura in cui ciò sia tecnicamente fattibile, come richiesto dall'articolo 5a(4)(f) del Regolamento (UE) n. 910/2014, come modificato da [`EU_2024_1183`_].

L'Istanza del Wallet DEVE consentire all'Utente di esercitare i diritti di portabilità dei dati, come richiesto dall'articolo 5a(4)(g) di tale Regolamento.

L'Istanza del Wallet DEVE supportare l'esportazione sicura e la portabilità dei dati personali dell'Utente, ove tecnicamente fattibile e ad eccezione degli asset critici, in modo che l'Utente possa migrare verso un'Istanza del Wallet di una Soluzione Wallet diversa mantenendo il livello di garanzia alto di cui al Regolamento di esecuzione (UE) 2015/1502. Si tratta dell'articolo 13 di [`CIR2024/2979`_].

Il file di backup specificato in :ref:`backup-restore:Flusso di Backup` è il backup e il recupero dei riferimenti alle Credenziali Elettroniche con associazione hardware.

Il download dei dati dell'Utente e degli attestati elettronici di attributi, e la portabilità verso una Soluzione Wallet diversa, utilizzano l'oggetto di migrazione specificato in :ref:`backup-restore:Migrazione verso una Soluzione Wallet diversa`.

Il download dei record di transazione utilizza anche l'esportazione dalla dashboard specificata in :ref:`wallet-instance-dashboard:Esportazione e Cancellazione dei Record di Transazione`.

Il download delle configurazioni utilizza :ref:`backup-restore:Download della configurazione del Wallet`.

Una chiave privata con associazione al dispositivo è un asset critico. Una chiave privata con associazione al dispositivo NON DEVE essere inclusa nel file di backup. Una chiave privata con associazione al dispositivo NON DEVE essere inclusa nell'oggetto di migrazione.


Flusso di Backup
----------------

.. _fig_Backup_flow:

.. plantuml:: plantuml/backup-flow.puml
   :width: 90%
   :alt: La figura illustra il diagramma di sequenza per il flusso di backup, con i passaggi spiegati di seguito.
   :caption: `Flusso di backup <https://www.plantuml.com/plantuml/png/VP5HRzGm3CVVyodClMn8j1KmU9YcqxPZe8bDEkaqyG1eIbFlQaYJAd4uAhJlJj96WuvZUMhj_y_-spxrB1s7JejdP9GE3KBBtFlZgd9oLsw9sr07ZqvPmsYuLBQhUYrDOWhFZQQwMXqLwnIwkRwgEkaPNGpThY8XoQ0h-rHVICNMmKsi1TB38dqiXDWCKT_TdjjW6kc6mvtK6dbZTM2oviMaE_3m3d-GmiLp-2KWlltOfV4iZSA8VHe3a2CPpE_1sM6Wt24A6TsTJCezkbggxw4_wsc3Blc8rFaOWhFr9UHW9k_5dEriJHetR9tS9l1w_Cy3mPLLKaFE9fUvnhqG1t3nizUaY47BmGO6sNmBdZiq37VMGMyzfIsHsOfP5oW-jzGqQBuMIvYlHeXnt28c0i4nB4xgvSiIyZGhXv5YajgVLFLo8QBc96aVBs02NvNm0GqwoGWVSO1rwwJ7FsWYKxj9_ReSvzmZVLmT_j_og4mcKyCBezpGCpQGpRydZK_K2pHLU5F-Y-vp_8GKlXY8QTWHjx1sjkkdW_oL6-zQhRGDJRvkzlQm_ld5fePlInZ1ENAAfWcT_Wq0>`_

.. .. figure:: ../../images/Backup_flow.svg
..   :name: Sequence Diagram for Wallet Instance Backup
..   :figwidth: 90%
..   :alt: The figure illustrates the sequence diagram for backup flow, with the steps explained below.
..   :target: https://www.plantuml.com/plantuml/png/VP5HRzGm3CVVyodClMn8j1KmU9YcqxPZe8bDEkaqyG1eIbFlQaYJAd4uAhJlJj96WuvZUMhj_y_-spxrB1s7JejdP9GE3KBBtFlZgd9oLsw9sr07ZqvPmsYuLBQhUYrDOWhFZQQwMXqLwnIwkRwgEkaPNGpThY8XoQ0h-rHVICNMmKsi1TB38dqiXDWCKT_TdjjW6kc6mvtK6dbZTM2oviMaE_3m3d-GmiLp-2KWlltOfV4iZSA8VHe3a2CPpE_1sM6Wt24A6TsTJCezkbggxw4_wsc3Blc8rFaOWhFr9UHW9k_5dEriJHetR9tS9l1w_Cy3mPLLKaFE9fUvnhqG1t3nizUaY47BmGO6sNmBdZiq37VMGMyzfIsHsOfP5oW-jzGqQBuMIvYlHeXnt28c0i4nB4xgvSiIyZGhXv5YajgVLFLo8QBc96aVBs02NvNm0GqwoGWVSO1rwwJ7FsWYKxj9_ReSvzmZVLmT_j_og4mcKyCBezpGCpQGpRydZK_K2pHLU5F-Y-vp_8GKlXY8QTWHjx1sjkkdW_oL6-zQhRGDJRvkzlQm_ld5fePlInZ1ENAAfWcT_Wq0

  .. Backup flow.

Di seguito, la descrizione dei passaggi di :numref:`fig_Backup_flow`:

**Passaggio 1**: L'Utente seleziona l'opzione per eseguire il backup delle Credenziali memorizzate nell'Istanza del Wallet (:ref:`WP_120 <credential-backup-testcases>`).

**Passaggi 2-3**: L'Istanza del Wallet, utilizzando le API di backup, seleziona casualmente 10 frasi chiave da un elenco di parole pre-generato e le mostra all'Utente (:ref:`WP_120a <credential-backup-testcases>`).
L'Utente DEVE conservare in modo sicuro la frase chiave scelta tra quelle proposte dal sistema (ad esempio, in un'app di gestione password) poiché sono fondamentali per il ripristino del backup (:ref:`WP_120b <credential-backup-testcases>`).

.. note::
  Come evidenziato nell'ARF, la crittografia è necessaria perché il file di backup è considerato sensibile. Anche se un attaccante conosce solo gli identificatori del Fornitore di Credenziali, può dedurre i diversi tipi di Credenziali Elettroniche, il che costituisce una violazione della privacy dell'Utente.

.. note::
  Per estrarre la chiave dall'elenco delle parole selezionate DEVE essere applicata una funzione di derivazione della chiave. Password-Based-Key-Derivation Function 2 (PBKDF2) è tra le più utilizzate basate su `RFC 2898`_ ed è raccomandata dal `NIST 800-132 <https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-132.pdf>`_. Esistono anche altre tecniche rilevanti disponibili e ampiamente utilizzate, come Bcrypt, Scrypt e Argon2. Maggiori dettagli su questo approccio possono essere trovati `qui <https://cryptobook.nakov.com/mac-and-key-derivation/kdf-deriving-key-from-password>`_ (:ref:`WP_121 <credential-backup-testcases>`).

.. note::
  Il livello di complessità per PBKDF2 è implementato attraverso un conteggio di iterazioni, che dovrebbe essere impostato diversamente in base all'algoritmo di hashing interno utilizzato. Il valore consigliato per l'algoritmo di hashing ``SHA-256`` è di 600000 iterazioni come indicato nell’`OWASP Password Storage Cheatsheet <https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html#pbkdf2>`_ (:ref:`WP_121a <credential-backup-testcases>`).

**Passaggio 4**: L'Istanza del Wallet esegue le seguenti operazioni per creare il file JWT di backup (:ref:`WP_122 <credential-backup-testcases>`):

- Per ciascuna delle Credenziali con chiave vincolata all'hardware, aggiunge l'identificatore del Fornitore di Credenziali e il ``credential_configuration_id`` come voce nel JWT di backup (:ref:`WP_122d <credential-backup-testcases>`).
- Il file di backup NON DEVE contenere un attestato non vincolato al dispositivo.
- Firma il JWT di backup utilizzando la chiave privata la cui chiave pubblica è attestata nella Wallet Instance Attestation. La relativa chiave pubblica attestata dal Fornitore di Wallet è fornita nella Wallet Instance Attestation (claim ``cnf``). L'Istanza del Wallet DEVE verificare la validità della Wallet Instance Attestation prima di firmare il JWT di backup (:ref:`WP_123 <credential-backup-testcases>`).
- Aggiunge il JWT di backup firmato come voce al file di backup (:ref:`WP_122 <credential-backup-testcases>`).
- Cripta il file di backup utilizzando la frase chiave fornita (:ref:`WP_124 <credential-backup-testcases>`).

.. note::
  Il JWT di Backup PUÒ contenere la cronologia delle transazioni per ogni voce di Credenziale all'interno del claim ``credentials_backup`` (:ref:`WP_122c <credential-backup-testcases>`). Tale cronologia non è il registro delle transazioni. L'Istanza del Wallet NON DEVE ripristinare tale cronologia come registro delle transazioni della nuova Istanza del Wallet.

**Passaggio 5**: All'Utente verrà richiesto di scegliere un'opzione di archiviazione per conservare in modo sicuro il file di backup. Le opzioni possono includere l'archiviazione nativa o soluzioni di archiviazione esterne, come l'archiviazione cloud, dispositivi USB, consegna via e-mail o altro (:ref:`WP_125 <credential-backup-testcases>`).

**Passaggio 6**: Nel caso in cui l'Utente preferisca l'archiviazione nativa, il file di backup viene memorizzato sul dispositivo dell'Utente.

Un esempio non normativo dell'intestazione e del payload del JWT di backup è il seguente:

.. code-block:: json

  {
    "alg": "ES256",
    "typ": "wallet-unit-credentials-backup+jwt"
  }

.. code-block:: json

  {
    "timestamp":"2024-12-13T16:35:06+01:00",
    "wallet_provider_id":"https://wallet-provider.example.org/",
    "wallet_instance_version":"v1.0",
    "wallet_instance_attestation":"eyJhbGciOiJFUzI1NiIsImVVfQz.eyJpc3MiOiAiaH...LCAibmJ",
    "credentials_backup": {
        "https://issuer.example.org/v1.0/mDL": ["org.iso.18013-5.1.mDL"],
        "https://eaa-provider.example.org/": ["dc_sd_jwt_EuropeanDisabilityCard"]
     }
  }

L'intestazione JOSE del JWT di backup DEVE contenere i seguenti parametri OBBLIGATORI (:ref:`WP_122a <credential-backup-testcases>`):

.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Intestazione JOSE**
    - **Descrizione**
    - **Riferimento**
  * - **alg**
    - Un identificatore di algoritmo di firma digitale come da registro IANA "JSON Web Signature and Encryption Algorithms". DEVE essere uno degli algoritmi supportati elencati nella Sezione :ref:`algorithms:Algoritmi Crittografici` e NON DEVE essere impostato su ``none`` o qualsiasi identificatore di algoritmo simmetrico (MAC).
    - :rfc:`7516#section-4.1.1`.
  * - **typ**
    - DEVE essere impostato su ``wallet-unit-credentials-backup+jwt``
    - N/A

Il corpo del JWT di backup contiene i seguenti claim OBBLIGATORI (:ref:`WP_122b <credential-backup-testcases>`):

.. list-table::
  :class: longtable
  :widths: 20 60
  :header-rows: 1

  * - **Claim**
    - **Descrizione**
  * - **timestamp**
    - Timestamp UNIX con l'ora di creazione del file di backup. Questo valore viene aggiornato ogni volta che una nuova voce di Credenziale viene aggiunta al file di backup.
  * - **wallet_provider_id**
    - DEVE essere impostato sull'identificatore univoco del Fornitore di Wallet.
  * - **wallet_instance_version**
    - DEVE essere impostato sulla versione della Soluzione Wallet di cui è stato eseguito il backup.
  * - **wallet_instance_attestation**
    - DEVE essere impostato su un valore contenente il JWT della Wallet Instance Attestation.
  * - **credentials_backup**
    - Oggetto che descrive le specifiche delle Credenziali di cui è stato eseguito il backup. Questo oggetto contiene un elenco di coppie nome/valore, dove ogni nome è un identificatore univoco del Fornitore di Credenziali. Questo identificatore viene utilizzato per avviare la fase di emissione. Il valore è un array di stringhe univoche. Ogni stringa corrisponde al ``credential_configuration_id`` che identifica la specifica Credenziale Elettronica che è stata emessa.


Flusso di ripristino per Credenziale con associazione hardware
--------------------------------------------------------------

.. _fig_Restore_flow:

.. plantuml:: plantuml/restore-flow.puml
   :width: 90%
   :alt: La figura illustra il diagramma di sequenza per il flusso di ripristino, con i passaggi spiegati di seguito.
   :caption: `Flusso di Ripristino <https://www.plantuml.com/plantuml/png/TP5DRnCn48Rl-ok6N9fAP5T0-L0LHVrea2fQ4OWg3e2gsVKqCNZjbJrk6w7-T-or5TYssPCpVfzd9kCZnsZPjwfu8NMZl21OCtVkiAeitfKhoMjVUqUsCPf9SzcOjkeKwiXC70ibw-hqOBA8fQlBYwf5nsH3wVeq42WrsRAB_W8RDXQkWWlGmIWUHaMnt8HyUtrYl1PeD-CxL8fuQPHdQVJBbDjpS4Qtig7HFlmf87pFO-VQCUg60lQjBq2kP31_syd6NkOE8SXaRp0cdydLsFpstN4dbsJZ784wwKjml3Y7NCpaGr4CuTRKKj6IZSLL92_xt_aVmOLfK46wJMCcoSDsD_Dx7fyxvya6E1r2gs8FvlUTaeraKBWndW75B--u9SrmOonqnicuHAbNnM06c7nVIo58_vpCOBYvgFrA2YFdrh9pHR-TaFCI3c4qhMUlof1mmKIGbZojwjaevQQJVxdN9IoiQJi6Dd3LAOC2yj8-IaK3QWR30PFXJGbBKjJm_npS12dau5QIHqpSGT_vLWg2kMxifcCI0mLg4MuuK9ze0ukrHKSkkRoCfiVldRnlozs-fwR7ZjtUToMSKVP65dxeKCqDaYmzEpnvhoHuNyBdcb5gk2H6WOn3RBg3-r12du3nb_tv_BXde3WYBNoh_W80>`_


.. .. figure:: ../../images/Restore_Flow.svg
..   :name: Sequence Diagram for Wallet Instance Restore
..   :figwidth: 90%
..   :alt: The figure illustrates the sequence diagram for restore flow, with the steps explained below.
..   :target: https://www.plantuml.com/plantuml/png/TP5DRnCn48Rl-ok6N9fAP5T0-L0LHVrea2fQ4OWg3e2gsVKqCNZjbJrk6w7-T-or5TYssPCpVfzd9kCZnsZPjwfu8NMZl21OCtVkiAeitfKhoMjVUqUsCPf9SzcOjkeKwiXC70ibw-hqOBA8fQlBYwf5nsH3wVeq42WrsRAB_W8RDXQkWWlGmIWUHaMnt8HyUtrYl1PeD-CxL8fuQPHdQVJBbDjpS4Qtig7HFlmf87pFO-VQCUg60lQjBq2kP31_syd6NkOE8SXaRp0cdydLsFpstN4dbsJZ784wwKjml3Y7NCpaGr4CuTRKKj6IZSLL92_xt_aVmOLfK46wJMCcoSDsD_Dx7fyxvya6E1r2gs8FvlUTaeraKBWndW75B--u9SrmOonqnicuHAbNnM06c7nVIo58_vpCOBYvgFrA2YFdrh9pHR-TaFCI3c4qhMUlof1mmKIGbZojwjaevQQJVxdN9IoiQJi6Dd3LAOC2yj8-IaK3QWR30PFXJGbBKjJm_npS12dau5QIHqpSGT_vLWg2kMxifcCI0mLg4MuuK9ze0ukrHKSkkRoCfiVldRnlozs-fwR7ZjtUToMSKVP65dxeKCqDaYmzEpnvhoHuNyBdcb5gk2H6WOn3RBg3-r12du3nb_tv_BXde3WYBNoh_W80

..   Restore flow.

Il ripristino del file di backup si applica quando la nuova Istanza del Wallet è già attiva con un PID o un IT-Wallet ID.

Il PID NON DEVE essere incluso nel file di backup. L'IT-Wallet ID NON DEVE essere incluso nel file di backup.

L'elenco delle credenziali dell'oggetto di migrazione specificato in :ref:`backup-restore:Migrazione verso una Soluzione Wallet diversa` include il PID e l'IT-Wallet ID.

Di seguito, la descrizione dei passaggi di :numref:`fig_Restore_flow`:

**Passaggi 1-6**: L'Utente desidera ripristinare le Credenziali Elettroniche utilizzando il backup precedentemente creato con la propria Istanza del Wallet.
L'Utente seleziona `ripristina backup delle Credenziali Elettroniche` nell'app dell'Istanza del Wallet e viene fornito all'Utente un prompt con la funzione di importazione. Il file di backup da importare può essere fornito utilizzando un archivio locale o una posizione remota utilizzando anche un archivio cloud, e quindi inviare le frasi chiave di recupero (:ref:`WP_126 <credential-backup-testcases>`, :ref:`WP_127 <credential-backup-testcases>`).
Per verificare l'autenticità del file, l'Istanza del Wallet DEVE verificare la firma del JWT di backup per garantirne l'autenticità (:ref:`WP_129 <credential-backup-testcases>`). Per fare ciò, estrae prima il JWT della Wallet Instance Attestation dal claim ``wallet_instance_attestation`` e ottiene la relativa chiave pubblica utilizzando la Wallet Instance Attestation (claim ``cnf``) come specificato in :ref:`WP_128 <credential-backup-testcases>`.

**Passaggi 7-8**: L'Istanza del Wallet per ogni voce di Credenziale con associazione hardware nel payload del JWT di backup esegue i seguenti passaggi (:ref:`WP_130 <credential-backup-testcases>`):

- Estrae l'identificatore del Fornitore di Credenziali e il ``credential_configuration_id`` dalla voce. Il primo viene utilizzato per identificare il Fornitore di Credenziali e ottenere i suoi metadati, mentre il secondo verrà utilizzato per segnalare il tipo di Credenziale al Fornitore di Credenziali (:ref:`WP_130a <credential-backup-testcases>`).
- Utilizzando l'identificatore del Fornitore di Credenziali, l'Istanza del Wallet ottiene i metadati del Fornitore di Credenziali e effettua una richiesta di emissione al Fornitore di Credenziali fornendo la nuova Associazione Crittografica con l'Utente (:ref:`WP_130b <credential-backup-testcases>`).

.. note::
  Durante il ripristino, l'Istanza del Wallet DEVE eseguire un Wallet-Initiated Authorization Code Issuance Flow come definito nella Sezione :ref:`credential-issuance-low-level:Issuance Flow`, utilizzando una nuova Associazione Crittografica con l'Utente. Per le (Q)EAA, ciò include il gate di presentazione presso il Fornitore di Credenziali che agisce come Relying Party, secondo :ref:`credential-issuance-endpoint:Selezione del Metodo di Autenticazione dell'Utente`. Questo NON DEVE essere interpretato come il Re-issuance Flow definito nella Sezione :ref:`credential-issuance-low-level:Re-issuance Flow`, che si applica solo all'aggiornamento della Credenziale sulla stessa istanza (``UPDATE`` / ``ATTRIBUTE_UPDATE``) e richiede un Refresh Token associato all'Istanza del Wallet originale. Dal punto di vista del Fornitore di Credenziali, il ripristino è indistinguibile da una prima emissione Wallet-Initiated. Le Credenziali ripristinate da Fornitori distinti RICHIEDONO un Authorization Code Issuance Flow separato per ciascun Fornitore.

.. note::
  L'Istanza del Wallet NON DEVE verificare la scadenza della Wallet Instance Attestation poiché il suo scopo principale è consentire all'Istanza del Wallet di verificare l'autenticità del file di backup assicurandosi che sia stato creato e firmato da un'Istanza del Wallet di uno specifico Fornitore di Wallet (:ref:`WP_128a <credential-backup-testcases>`).


Migrazione verso una Soluzione Wallet diversa
---------------------------------------------

L'Istanza del Wallet DEVE fornire l'oggetto di migrazione nel formato comune di `EUDI-TS 10`_.

L'oggetto di migrazione è distinto dal JWT di backup di tipo ``wallet-unit-credentials-backup+jwt``.

L'Istanza del Wallet NON DEVE presentare il JWT di backup come oggetto di migrazione.

L'accettazione dell'oggetto di migrazione NON DEVE dipendere dal supporto del JWT di backup.

L'Istanza del Wallet DEVE mantenere aggiornato l'oggetto di migrazione rispetto alle Credenziali Elettroniche che conserva e rispetto al registro delle transazioni specificato in :ref:`wallet-instance-dashboard:Dashboard dell’Istanza del Wallet e Registrazione delle Transazioni`.

L'oggetto di migrazione DEVE contenere l'elenco delle Credenziali Elettroniche presenti nell'Istanza del Wallet, incluso il PID e l'IT-Wallet ID.

L'oggetto di migrazione DEVE contenere ciascun attestato non vincolato al dispositivo come attestato stesso.

L'oggetto di migrazione DEVE contenere il registro delle transazioni.

Per ciascun PID, IT-Wallet ID o altra Credenziale Elettronica in tale elenco, l'oggetto di migrazione DEVE includere il tipo di attestato, il fornitore che ha emesso la credenziale e il punto di fornitura del servizio di tale fornitore, come specificato in `EUDI-TS 10`_.

L'elenco delle credenziali NON DEVE contenere valori di attributo.

L'elenco delle credenziali NON DEVE contenere una chiave privata.

L'oggetto di migrazione NON DEVE contenere una copia di un attestato con associazione al dispositivo.

L'oggetto di migrazione NON DEVE contenere una Wallet Instance Attestation.

L'Istanza del Wallet DEVE proteggere la riservatezza, l'integrità e l'autenticità dell'oggetto di migrazione con le misure specificate in `EUDI-TS 10`_.

L'Istanza del Wallet NON DEVE proteggere l'oggetto di migrazione firmandolo come ``wallet-unit-credentials-backup+jwt``.

L'Istanza del Wallet DEVE consentire all'Utente di conservare l'oggetto di migrazione in una posizione esterna o remota scelta dall'Utente, tra le opzioni di archiviazione supportate dall'Istanza del Wallet.

Subito dopo l'installazione, la nuova Istanza del Wallet DEVE consentire all'Utente di importare un oggetto di migrazione da una posizione indicata dall'Utente, tra le opzioni di archiviazione supportate dall'Istanza del Wallet.

La nuova Istanza del Wallet DEVE chiedere all'Utente se ripristinare il registro delle transazioni dall'oggetto di migrazione.

Quando l'Utente acconsente, l'Istanza del Wallet DEVE ripristinare tale registro.

L'Istanza del Wallet DEVE accodare le transazioni successive al registro ripristinato.

L'esportazione dei record di transazione dalla dashboard resta il download di tali record, come specificato in :ref:`wallet-instance-dashboard:Esportazione e Cancellazione dei Record di Transazione`.

La nuova Istanza del Wallet DEVE copiare nell'Istanza del Wallet ciascun attestato non vincolato al dispositivo presente nell'oggetto di migrazione.

Per ciascun PID, IT-Wallet ID e altra Credenziale Elettronica con associazione al dispositivo elencata nell'oggetto di migrazione, l'Istanza del Wallet DEVE consentire all'Utente di selezionarla.

Quando l'Utente seleziona una credenziale elencata, l'Istanza del Wallet DEVE richiederne l'emissione al fornitore identificato nell'elenco.

La richiesta DEVE utilizzare una nuova Associazione Crittografica con l'Utente.

Se l'elenco contiene un PID, l'Istanza del Wallet DEVE richiedere l'emissione del PID prima delle altre credenziali dell'elenco.

L'Istanza del Wallet DEVE richiedere tale emissione con il Wallet-Initiated Authorization Code Issuance Flow definito nella Sezione :ref:`credential-issuance-low-level:Issuance Flow`.

Per una (Q)EAA si applica il gate di presentazione di :ref:`credential-issuance-endpoint:Selezione del Metodo di Autenticazione dell'Utente`.

L'Istanza del Wallet NON DEVE utilizzare il Re-issuance Flow definito nella Sezione :ref:`credential-issuance-low-level:Re-issuance Flow`.

Download della configurazione del Wallet
----------------------------------------

L'Istanza del Wallet DEVE consentire all'Utente di scaricare la configurazione del Wallet dell'Utente nella misura in cui ciò sia tecnicamente fattibile.

La configurazione del Wallet è l'insieme delle impostazioni scelte dall'Utente e conservate dall'Istanza del Wallet.

Il download NON DEVE includere un asset critico.

Un asset critico include una chiave privata con associazione al dispositivo, il materiale di chiave conservato nel Keystore o in un Remote WSCD, e una copia di un attestato con associazione al dispositivo.

Il file di configurazione è distinto dal JWT di backup e dall'oggetto di migrazione.

L'Istanza del Wallet DEVE consentire all'Utente di conservare il file di configurazione in una posizione scelta dall'Utente, tra le opzioni di archiviazione supportate dall'Istanza del Wallet.



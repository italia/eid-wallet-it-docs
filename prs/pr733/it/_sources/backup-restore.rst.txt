.. include:: ../common/common_definitions.rst


Backup e Ripristino
===================

La funzionalità di **Backup e Ripristino** diventa rilevante quando l'Utente desidera cambiare dispositivo e/o Soluzione Wallet per accedere nuovamente alle Credenziali Elettroniche precedentemente emesse.

- Il dispositivo mobile è stato **perso**, **rubato**, **danneggiato** o **compromesso** (ad esempio, a causa di accesso non autorizzato).
- L'Utente sostituisce un'Istanza del Wallet esistente con una nuova istanza della stessa Soluzione Wallet.
- L'Utente ha cambiato il proprio dispositivo mobile e deve configurare la Soluzione Wallet sul nuovo dispositivo.
- L'Utente esegue un ripristino delle impostazioni di fabbrica sul telefono attuale e deve configurare nuovamente la Soluzione Wallet.

.. note::
  Per le Soluzioni Wallet basate sulle Specifiche Tecniche dell'IT Wallet, la migrazione verso una Soluzione Wallet diversa (nota come portabilità dei dati) può essere supportata seguendo la funzionalità di backup e ripristino descritta in questa sezione.


Flusso di Backup
----------------

.. _fig_Backup_flow:
.. plantuml:: plantuml/backup-flow.puml
   :width: 90%
   :alt: La figura illustra il diagramma di sequenza per il flusso di backup, con i passaggi spiegati di seguito.
   :caption: `Flusso di backup <https://www.plantuml.com/plantuml/png/VP5HRzGm3CVVyodClMn8j1KmU9YcqxPZe8bDEkaqyG1eIbFlQaYJAd4uAhJlJj96WuvZUMhj_y_-spxrB1s7JejdP9GE3KBBtFlZgd9oLsw9sr07ZqvPmsYuLBQhUYrDOWhFZQQwMXqLwnIwkRwgEkaPNGpThY8XoQ0h-rHVICNMmKsi1TB38dqiXDWCKT_TdjjW6kc6mvtK6dbZTM2oviMaE_3m3d-GmiLp-2KWlltOfV4iZSA8VHe3a2CPpE_1sM6Wt24A6TsTJCezkbggxw4_wsc3Blc8rFaOWhFr9UHW9k_5dEriJHetR9tS9l1w_Cy3mPLLKaFE9fUvnhqG1t3nizUaY47BmGO6sNmBdZiq37VMGMyzfIsHsOfP5oW-jzGqQBuMIvYlHeXnt28c0i4nB4xgvSiIyZGhXv5YajgVLFLo8QBc96aVBs02NvNm0GqwoGWVSO1rwwJ7FsWYKxj9_ReSvzmZVLmT_j_og4mcKyCBezpGCpQGpRydZK_K2pHLU5F-Y-vp_8GKlXY8QTWHjx1sjkkdW_oL6-zQhRGDJRvkzlQm_ld5fePlInZ1ENAAfWcT_Wq0>`_

Di seguito, la descrizione dei passaggi di :numref:`fig_Backup_flow`:

**Passaggio 1**: L'Utente seleziona l'opzione per eseguire il backup delle Credenziali memorizzate nell'Istanza del Wallet.

**Passaggi 2-3**: L'Istanza del Wallet, utilizzando le API di backup, seleziona casualmente 10 frasi chiave da un elenco di parole pre-generato e le mostra all'Utente.
L'Utente DEVE conservare in modo sicuro la frase chiave scelta tra quelle proposte dal sistema (ad esempio, in un gestore di password o in una cassaforte fisica) poiché sono fondamentali per il ripristino del backup.

.. note::
  Come evidenziato nell'ARF, la crittografia è necessaria perché il file di backup è considerato sensibile. Anche se un attaccante conosce solo gli identificatori del Fornitore di Credenziale, può dedurre i diversi tipi di Credenziali Elettroniche, il che costituisce una violazione della privacy dell'Utente.

.. note::
  Per estrarre la chiave dall'elenco delle parole selezionate DEVE essere applicata una funzione di derivazione della chiave. Password-Based-Key-Derivation Function 2 (PBKDF2) è tra le più utilizzate basate su `RFC 2898`_ ed è raccomandata dal `NIST 800-132 <https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-132.pdf>`_. Esistono altre tecniche rilevanti disponibili e ampiamente utilizzate, come Bcrypt, Scrypt e Argon2. Maggiori dettagli su questo approccio possono essere trovati `qui <https://cryptobook.nakov.com/mac-and-key-derivation/kdf-deriving-key-from-password>`_.

.. note::
  Il fattore di lavoro per PBKDF2 è implementato attraverso un conteggio di iterazioni, che dovrebbe essere impostato diversamente in base all'algoritmo di hashing interno utilizzato. Il valore consigliato per l'algoritmo di hashing ``SHA-256`` è di 600000 iterazioni come indicato nel `OWASP Password Storage Cheatsheet <https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html#pbkdf2>`_.

**Passaggio 4**: L'Istanza del Wallet esegue le operazioni seguenti per creare la voce JWT di backup per il file di backup.

- Per ciascuna delle Credenziali con chiave vincolata all'hardware, aggiunge l'identificatore del Fornitore di Credenziale e il ``credential_configuration_id`` come voce nel JWT di backup.
- Firma il JWT di backup utilizzando la chiave privata la cui chiave pubblica è attestata nell'Attestato di Unità di Portafoglio. La relativa chiave pubblica attestata dal Fornitore di Wallet è fornita nell'Attestato di Unità di Portafoglio (claim ``cnf``). L'Istanza del Wallet DEVE verificare la validità dell'Attestato di Unità di Portafoglio prima di firmare il JWT di backup.
- Aggiunge il JWT di backup firmato come voce al file di backup.
- Cripta il file di backup utilizzando la frase chiave fornita.

.. note::
  Il JWT di Backup PUÒ contenere la cronologia delle transazioni per ogni voce di Credenziale all'interno del claim ``credentials_backup``.

**Passaggio 5**: All'Utente verrà richiesto di scegliere un'opzione di archiviazione per conservare in modo sicuro il file di backup. Le opzioni possono includere l'archiviazione nativa o soluzioni di archiviazione esterne, come l'archiviazione cloud, dispositivi USB, consegna via e-mail o altro.

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
    "wallet_attestation":"eyJhbGciOiJFUzI1NiIsImVVfQz.eyJpc3MiOiAiaH...LCAibmJ",
    "credentials_backup": {
        "https://issuer.example.org/v1.0/mdl": ["org.iso.18013-5.1.mDL"],
        "https://eaa-provider.example.org/": ["dc_sd_jwt_EuropeanDisabilityCard"]
     }
  }

L'intestazione JOSE del JWT di backup DEVE contenere i seguenti parametri OBBLIGATORI:

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

Il corpo del JWT di backup contiene i seguenti claim OBBLIGATORI:

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
  * - **wallet_attestation**
    - DEVE essere impostato su un valore contenente il JWT dell'Attestato di Unità di Portafoglio.
  * - **credentials_backup**
    - Oggetto che descrive le specifiche delle Credenziali di cui è stato eseguito il backup. Questo oggetto contiene un elenco di coppie nome/valore, dove ogni nome è un identificatore univoco del Fornitore di Credenziale. Questo identificatore viene utilizzato per avviare la fase di emissione. Il valore è un array di stringhe univoche. Ogni stringa corrisponde al ``credential_configuration_id`` che identifica la specifica Credenziale Elettronica che è stata emessa.


Flusso di ripristino per Credenziale con associazione hardware
--------------------------------------------------------------

.. _fig_Restore_flow:

.. plantuml:: plantuml/restore-flow.puml
   :width: 90%
   :alt: La figura illustra il diagramma di sequenza per il flusso di ripristino, con i passaggi spiegati di seguito.
   :caption: `Flusso di Ripristino <https://www.plantuml.com/plantuml/png/TP5DRnCn48Rl-ok6N9fAP5T0-L0LHVrea2fQ4OWg3e2gsVKqCNZjbJrk6w7-T-or5TYssPCpVfzd9kCZnsZPjwfu8NMZl21OCtVkiAeitfKhoMjVUqUsCPf9SzcOjkeKwiXC70ibw-hqOBA8fQlBYwf5nsH3wVeq42WrsRAB_W8RDXQkWWlGmIWUHaMnt8HyUtrYl1PeD-CxL8fuQPHdQVJBbDjpS4Qtig7HFlmf87pFO-VQCUg60lQjBq2kP31_syd6NkOE8SXaRp0cdydLsFpstN4dbsJZ784wwKjml3Y7NCpaGr4CuTRKKj6IZSLL92_xt_aVmOLfK46wJMCcoSDsD_Dx7fyxvya6E1r2gs8FvlUTaeraKBWndW75B--u9SrmOonqnicuHAbNnM06c7nVIo58_vpCOBYvgFrA2YFdrh9pHR-TaFCI3c4qhMUlof1mmKIGbZojwjaevQQJVxdN9IoiQJi6Dd3LAOC2yj8-IaK3QWR30PFXJGbBKjJm_npS12dau5QIHqpSGT_vLWg2kMxifcCI0mLg4MuuK9ze0ukrHKSkkRoCfiVldRnlozs-fwR7ZjtUToMSKVP65dxeKCqDaYmzEpnvhoHuNyBdcb5gk2H6WOn3RBg3-r12du3nb_tv_BXde3WYBNoh_W80>`_
    

Considerando che l'Utente ha inizializzato la nuova Istanza del Wallet e questa è in stato attivo avendo ottenuto un nuovo Attestato Elettronico di Dati di Identificazione Personale, questa specifica allenta il requisito dell'ARF riguardante l'aggiunta dell'Attestato Elettronico di Dati di Identificazione Personale nel file di backup.
Di seguito, la descrizione dei passaggi di :numref:`fig_Restore_flow`:

**Passaggi 1-6**: L'Utente desidera ripristinare le Credenziali Elettroniche utilizzando il backup precedentemente creato con la propria Istanza del Wallet.
L'Utente seleziona `ripristina backup delle Credenziali Elettroniche` nell'app dell'Istanza del Wallet e viene fornito all'Utente un prompt con la funzione di importazione. Il file di backup da importare può essere fornito utilizzando un archivio locale o una posizione remota utilizzando anche un archivio cloud, e quindi inviare le frasi chiave di recupero.
Per verificare l'autenticità del file, l'Istanza del Wallet DEVE verificare la firma del JWT di backup per garantirne l'autenticità. Per fare ciò, estrae prima il JWT dell'Attestato di Unità di Portafoglio dal claim ``wallet_attestation`` e ottiene la relativa chiave pubblica utilizzando l'Attestato di Unità di Portafoglio (claim ``cnf``).

**Passaggi 7-8**: L'Istanza del Wallet per ogni voce di Credenziale con associazione hardware nel payload del JWT di backup esegue i seguenti passaggi:

- Estrae l'identificatore del Fornitore di Credenziale e il ``credential_configuration_id`` dalla voce. Il primo viene utilizzato per identificare il Fornitore di Credenziale e ottenere i suoi metadati, mentre il secondo verrà utilizzato per segnalare il tipo di Credenziale al Fornitore di Credenziale.
- Utilizzando l'identificatore del Fornitore di Credenziale, l'Istanza del Wallet ottiene i metadati del Fornitore di Credenziale e effettua una richiesta di riemissione al Fornitore di Credenziale fornendo la nuova Associazione Crittografica con l'Utente.

.. note::
  L'Istanza del Wallet NON DEVE verificare la scadenza dell'Attestato di Unità di Portafoglio poiché il suo scopo principale è consentire all'Istanza del Wallet di verificare l'autenticità del file di backup assicurandosi che sia stato creato e firmato da un'Istanza del Wallet di uno specifico Fornitore di Wallet.

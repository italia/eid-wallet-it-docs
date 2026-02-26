.. include:: ../common/common_definitions.rst

.. level 2 "included" file, so we start with '^' title level

Requisiti della Soluzione Wallet
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Questa sezione elenca i requisiti per la Soluzione Wallet, strutturati secondo la scomposizione per la certificazione definita nella :ref:`wallet-solution:Soluzione Wallet` e nella :ref:`Scomposizione e Ambito di Certificazione <wallet-solution-components-decomposition>`. I requisiti si applicano ai componenti **Wallet Instance (WI)**, **Wallet Provider Backend (WPBE)**, **Wallet Secure Cryptographic Device (WSCD)** e **Wallet Secure Cryptographic Application (WSCA)** del macro-componente di certificazione **Servizi ICT Wallet**.

.. list-table::
   :widths: 8 55 37
   :header-rows: 1

   * - ID Req.
     - Requisito
     - Ambito di certificazione
   * - WS-001
     - La Soluzione Wallet DEVE aderire alle specifiche stabilite da questo documento per ottenere Attestati Elettronici di Dati di Identificazione Personale (PID) e Attestati Elettronici di Attributi (Q)EAA.
     - WI, WPBE, WSCD, WSCA
   * - WS-002
     - Il Fornitore di Wallet DEVE esporre un insieme di endpoint, disponibili esclusivamente per le istanze della sua Soluzione Wallet, che supportano le funzionalità principali delle Istanze del Wallet.
     - WPBE
   * - WS-003
     - L'Istanza del Wallet DEVE periodicamente ristabilire la trust con il suo Fornitore di Wallet, ottenendo una nuova Wallet App Attestation (:ref:`WP_018 <wallet-instance-testcases>`).
     - WI
   * - WS-004
     - L'istanza del Wallet DEVE stabilire un rapporto di fiducia con gli altri partecipanti dell'ecosistema del Wallet, come i Fornitori di Attributi Elettronici. Nel caso dei Fornitori di Attributi Elettronici, l'istanza del Wallet presenta sia la Wallet App Attestation che la Wallet Unit Attestation.
     - WI
   * - WS-005
     - L'Istanza del Wallet DEVE essere compatibile e funzionale sia sui sistemi operativi Android che iOS e disponibile rispettivamente sul Play Store e sull'App Store (:ref:`WP_015 <wallet-instance-testcases>`).
     - WI
   * - WS-006
     - L'Istanza del Wallet DEVE fornire un meccanismo per verificare l'effettivo possesso e il pieno controllo da parte dell'Utente del proprio dispositivo personale.
     - WI
   * - WS-007
     - L'Istanza del Wallet DEVE fornire agli Utenti un elenco aggiornato delle Relying Party con cui l'Utente ha stabilito una connessione e, ove applicabile, tutti i dati scambiati.
     - WI
   * - WS-008
     - L'Istanza del Wallet DEVE fornire agli Utenti un meccanismo per richiedere la cancellazione degli attributi personali da parte di una Relying Party ai sensi dell'articolo 17 del `Regulation (EU) 2016/679`_, e per registrare ogni Richiesta di Cancellazione effettuata.
     - WI

.. note::
   Non esiste una corrispondenza stretta uno-a-uno tra i requisiti in questa sezione e i casi di test in :ref:`wallet-provider-test-matrix`. Alcuni requisiti sono espressi a un livello troppo alto per poter essere rappresentati come casi di test atomici, mentre altri sono già affrontati in modo più dettagliato all'interno dei flussi correlati (ad es. :ref:`wallet-attestation-issuance:Emissione della Wallet App e Wallet Unit Attestation`).

Requisiti della Wallet App Attestation
""""""""""""""""""""""""""""""""""""""""

La Wallet App Attestation è emessa dal **Wallet Provider Backend (WPBE)** come parte del sottocomponente Wallet Instance Lifecycle Management (vedere :ref:`Scomposizione e Ambito di Certificazione <wallet-solution-components-decomposition>`). Contiene informazioni riguardanti il livello di sicurezza del dispositivo che ospita l'Istanza del Wallet.
Esso dimostra principalmente l'**autenticità**, l'**integrità**, la **sicurezza** e in generale l'**affidabilità** di una particolare Istanza del Wallet.

I requisiti per la Wallet App Attestation sono definiti di seguito:

.. list-table::
   :widths: 8 55 37
   :header-rows: 1

   * - ID Req.
     - Requisito
     - Ambito di certificazione
   * - WAA-001
     - La Wallet App Attestation DEVE fornire tutte le informazioni rilevanti per attestare l'**integrità** e la **sicurezza** del dispositivo in cui è installata l'Istanza del Wallet (:ref:`WP_019 <wallet-instance-testcases>`).
     - WPBE
   * - WAA-002
     - La Wallet App Attestation DEVE essere firmata dal Fornitore di Wallet che ha autorità e proprietà sulla Soluzione Wallet, come specificato dalla Registration Authority di supervisione. Questo garantisce che la Wallet App Attestation colleghi in modo univoco il Fornitore di Wallet a questa particolare Istanza del Wallet (:ref:`WP_020 <wallet-instance-testcases>`).
     - WPBE
   * - WAA-003
     - Il Fornitore di Wallet DEVE periodicamente valutare e garantire l'integrità, l'autenticità e la genuinità dell'Istanza del Wallet. Il Fornitore di Wallet verifica l'Istanza del Wallet utilizzando il flusso più sicuro reso disponibile dalle API del Fornitore del Sistema Operativo, come la *Play Integrity API* per Android e *App Attest* per iOS (:ref:`WP_011 <wallet-provider-backend-testcases>`).
     - WPBE
   * - WAA-004
     - Il Fornitore di Wallet DEVE possedere un meccanismo di revoca per l'Istanza del Wallet, che consenta al Fornitore di Wallet di terminare il servizio per una specifica Istanza in qualsiasi momento (:ref:`WP_011 <wallet-provider-backend-testcases>`).
     - WPBE
   * - WAA-005
     - La Wallet App Attestation DEVE essere vincolata in modo sicuro alla chiave pubblica effimera dell'Istanza del Wallet (:ref:`WP_019b <wallet-instance-testcases>`).
     - WPBE
   * - WAA-006
     - La Wallet App Attestation PUÒ essere utilizzata più volte durante il suo periodo di validità, consentendo autenticazioni e autorizzazioni ripetute senza la necessità di richiedere nuovi attestati ad ogni interazione. Tuttavia, è RACCOMANDATO che le Istanze del Wallet evitino di utilizzare ripetutamente lo stesso attestato, a causa di preoccupazioni sulla privacy come la possibilità di collegamento tra diverse interazioni.
     - WI
   * - WAA-007
     - La Wallet App Attestation DEVE avere una durata limitata e DEVE includere un tempo di scadenza, oltre il quale NON DEVE più essere considerata valida.
     - WPBE
   * - WAA-008
     - La Wallet App Attestation NON DEVE essere rilasciata dal Fornitore di Wallet se l'autenticità, l'integrità e la genuinità dell'Istanza del Wallet che la richiede non possono essere garantite (:ref:`WP_019a <wallet-instance-testcases>`).
     - WPBE
   * - WAA-009
     - Ogni Istanza del Wallet DOVREBBE essere in grado di richiedere più Wallet App Attestation utilizzando diverse chiavi pubbliche crittografiche associate ad esse.
     - WI
   * - WAA-010
     - La Wallet App Attestation NON DEVE contenere informazioni sull'Utente che controlla l'Istanza del Wallet (:ref:`WP_029b <wallet-instance-testcases>`).
     - WPBE
   * - WAA-011
     - L'Istanza del Wallet DEVE ottenere una Wallet App Attestation come prerequisito per passare allo stato Operativo, come definito da `EIDAS-ARF`_.
     - WI
   * - WAA-012
     - Un Fornitore di Wallet DEVE garantire che una Wallet Unit non revocata presenti sempre una Wallet App Attestation temporalmente valida e non revocata a un PID Provider o Attestation Provider durante il processo di emissione di un PID o attestazione. Nota: Questo requisito si applica sia alle attestazioni vincolate al dispositivo che a quelle non vincolate, come definito da `EIDAS-ARF`_.
     - WPBE
   * - WAA-013
     - Una Wallet Unit DEVE presentare una Wallet App Attestation solo a un PID Provider o Attestation Provider, come parte del processo di emissione di un PID o un'attestazione, e non a una Relying Party o a qualsiasi altra entità.
     - WI

.. note::
  In questa sezione, i servizi utilizzati per attestare la genuinità dell'Istanza del Wallet e del dispositivo in cui è installata sono indicati come **API del Servizio di Integrità del Dispositivo**. L'API del Servizio di Integrità del Dispositivo è considerata in modo astratto e si presume sia un servizio fornito da una terza parte affidabile (cioè, l'API del Fornitore del Sistema Operativo) in grado di eseguire controlli di integrità sull'Istanza del Wallet e sul dispositivo in cui è installata.


Requisiti della Wallet Unit Attestation
"""""""""""""""""""""""""""""""""""""""""

La Wallet Unit Attestation è emessa dal **Wallet Provider Backend (WPBE)** e attesta le proprietà della **Wallet Secure Cryptographic Application (WSCA)** e del **Wallet Secure Cryptographic Device (WSCD)** (vedere :ref:`Scomposizione e Ambito di Certificazione <wallet-solution-components-decomposition>`). Contiene informazioni che garantiscono che le chiavi utilizzate per il collegamento crittografico degli Attestati Elettronici siano archiviate in un WSCD **affidabile**.
Inoltre, fornisce un metodo per autenticare il WSCD presso il Fornitore di Attributi Elettronici e verifica che la Wallet Unit non sia stata revocata.

I requisiti per la Wallet Unit Attestation sono definiti di seguito:

.. list-table::
   :widths: 8 55 37
   :header-rows: 1

   * - ID Req.
     - Requisito
     - Ambito di certificazione
   * - WUA-001
     - La Wallet Unit Attestation DEVE fornire al PID Provider o all'Attestation Provider informazioni sulle capacità del WSCA e del WSCD della Wallet Unit, in modo che possano prendere una decisione ben fondata sull'opportunità di emettere un PID o un'attestazione per tale Wallet Unit.
     - WPBE
   * - WUA-002
     - La Wallet Unit Attestation DEVE consentire ai PID Provider e agli Attestation Provider di verificare l'autenticità e lo stato di revoca della Wallet Unit.
     - WPBE
   * - WUA-003
     - Un Fornitore di Wallet DEVE garantire che una Wallet Unit non revocata possa in ogni momento presentare una Wallet Unit Attestation, quando richiesta da un PID Provider o da un Attestation Provider.
     - WPBE
   * - WUA-004
     - Durante l'emissione di un PID, la Wallet Unit DEVE fornire al PID Provider una WUA valida che descriva il WSCA/WSCD che ha generato la nuova chiave privata del PID. Nota: Una chiave privata PID è sempre generata e gestita dal WSCA/WSCD. Durante l'emissione di un'attestazione vincolata al dispositivo, una Wallet Unit DEVE recuperare dai metadati dell'emittente (come specificato in `OpenID4VCI`_) i requisiti dell'Attestation Provider riguardanti l'archiviazione delle chiavi da parte del WSCA/WSCD. La Wallet Unit DEVE determinare quale dei propri WSCA/WSCD o keystore, se presente, soddisfi tali requisiti. Se un WSCA/WSCD o keystore conforme è disponibile, la Wallet Unit DEVE fornire all'Attestation Provider una WUA valida che descriva il WSCA/WSCD o keystore selezionato. Nota: Una WUA descrive le proprietà del WSCA/WSCD o keystore e contiene una o più chiavi pubbliche corrispondenti alle chiavi private generate e archiviate in quel WSCA/WSCD o keystore.
     - WI, WSCA, WSCD
   * - WUA-005
     - Se una Wallet Unit contiene più WSCA, essa DEVE, in modo interno e sicuro, tenere traccia di quali PID e attestazioni sono associati a ciascun WSCA.
     - WI, WSCA
   * - WUA-006
     - Una Wallet Unit DEVE presentare una Wallet Unit Attestation solo come parte del processo di emissione di un PID o di un'attestazione vincolata alla chiave.
     - WI
   * - WUA-007
     - La Wallet Unit Attestation DEVE consentire ai PID Provider di richiedere a un Wallet Provider la revoca di una Wallet Unit, includendo un identificatore per la Wallet Unit all'interno della WUA (ad esempio, un URI e un indice a una Attestation Status List). Il Wallet Provider DEVE garantire che tale identificatore della Wallet Unit non consenta il tracciamento dell'utente.
     - WPBE
   * - WUA-008
     - La Wallet Unit Attestation DEVE contenere una o più chiavi pubbliche di credenziali attestate provenienti dallo stesso WSCD.
     - WPBE
   * - WUA-009
     - La Wallet Unit Attestation DEVE essere firmata dal Wallet Provider che ha autorità e proprietà sulla Wallet Solution, come specificato dall'Autorità di Registrazione di riferimento. I Wallet Provider DEVONO garantire che i certificati utilizzati per firmare WUA e WAA siano conformi a tutti i requisiti applicabili di `ETSI TS 119 412-6`_, in particolare la Clausola 5.
     - WPBE
   * - WUA-010
     - La Wallet Unit Attestation NON DEVE essere emessa dal Wallet Provider se l'affidabilità del WSCD non è garantita. In tal caso, l'istanza del Wallet DEVE essere revocata.
     - WPBE, WI
   * - WUA-011
     - Un Attestation Provider che emette attestazioni non vincolate al dispositivo DEVE indicare nei propri metadati del Credential Issuer che non richiede una WUA. Una Wallet Unit NON DEVE inviare una WUA a un Attestation Provider quando richiede un'attestazione non vincolata al dispositivo. Nota: Una Wallet Unit invia una WIA all'Attestation Provider indipendentemente dal fatto che le attestazioni emesse siano vincolate o meno al dispositivo.
     - WPBE
   * - WUA-012
     - Un Wallet Provider DEVE garantire che la presentazione di una WUA sia vincolata crittograficamente al contesto specifico in cui è destinata ad essere utilizzata. Nota: Come specificato in `OpenID4VCI`_, ciò si ottiene facendo sì che la Wallet Unit presenti la WUA insieme a una Proof-of-Possession consistente in una firma su un nonce fornito dal PID Provider o dall'Attestation Provider durante il processo di emissione, creata dalla chiave privata corrispondente a una delle chiavi pubbliche attestate nella WUA.
     - WPBE
   * - WUA-013
     - Durante l'emissione di un PID o di un'attestazione vincolata al dispositivo, il PID Provider o l'Attestation Provider DEVE verificare la WUA in conformità con i requisiti dell'Appendice F.4 di `OpenID4VCI`_.
     - -
   * - WUA-014
     - Durante l'emissione di un PID o di un'attestazione vincolata al dispositivo, il PID Provider o l'Attestation Provider DEVE ricevere una prova che la Wallet Unit possiede le chiavi private corrispondenti a tutte le chiavi pubbliche nella WUA.
     - -
   * - WUA-015
     - Se il WSCA/WSCD è in grado di esportare una chiave privata, il Wallet Provider DEVE specificare questa capacità come attributo nella WUA.
     - WPBE

.. note::
   Considerazione di sicurezza: nel decidere il periodo di validità di una WUA, il Wallet Provider dovrebbe considerare tutti i fattori rilevanti, inclusi l'utilizzo offline, l'interoperabilità e il rischio che una WUA diventi un vettore per tracciare l'Utente.

Requisiti WSCD
"""""""""""""""""

Il **Wallet Secure Cryptographic Device (WSCD)** include l'Hardware Secure Element, il WSCD Firmware e il Secure Key Storage System (vedere :ref:`Scomposizione e Ambito di Certificazione <wallet-solution-components-decomposition>`). Per garantire la massima sicurezza, le chiavi crittografiche associate a un'Istanza del Wallet (ad esempio, utilizzate per generare la Wallet App Attestation) DEVONO essere generate e memorizzate in modo sicuro all'interno del WSCD. Solo l'Utente legittimo può accedere alle chiavi crittografiche private, impedendo l'uso non autorizzato o la manomissione. Il WSCD PUÒ essere implementato utilizzando almeno uno degli approcci elencati di seguito:

.. list-table::
   :widths: 8 55 37
   :header-rows: 1

   * - ID Req.
     - Requisito
     - Ambito di certificazione
   * - WSCD-001
     - Le chiavi crittografiche associate a un'Istanza del Wallet DEVONO essere generate e memorizzate in modo sicuro all'interno del WSCD.
     - WSCD
   * - WSCD-002
     - **WSCD Interno Locale**: Il WSCD si basa interamente sull'hardware crittografico nativo del dispositivo, come il Secure Enclave su iOS, o il Trusted Execution Environment (TEE) e Strongbox su Android.
     - WSCD
   * - WSCD-003
     - **WSCD Esterno Locale**: Il WSCD è un hardware esterno al dispositivo dell'Utente, come una smart card conforme a *GlobalPlatform* e che supporta *JavaCard*.
     - WSCD
   * - WSCD-004
     - **WSCD Remoto**: Il WSCD utilizza un Hardware Security Module (HSM) remoto.
     - WSCD
   * - WSCD-005
     - **WSCD Ibrido Locale**: Il WSCD coinvolge un componente hardware interno collegabile all'interno del dispositivo dell'Utente, come un *eUICC* che aderisce agli standard *GlobalPlatform* e supporta *JavaCard*.
     - WSCD
   * - WSCD-006
     - **WSCD Ibrido Remoto**: Il WSCD coinvolge un componente locale combinato con un servizio remoto.
     - WSCD

.. _wscd-security-levels:

.. warning::
  Nella fase attuale, il profilo di implementazione definito in questo documento supporta solo il **WSCD Interno Locale** (:ref:`WP_014 <wallet-instance-testcases>`). Le versioni future di questa specifica POTREBBERO includere altri approcci a seconda del Livello di Garanzia dell'Autenticatore richiesto (`AAL`).

  Il WSCD opera a due livelli di sicurezza:

  - **WSCD WL3**: certificato come resistente ad attaccanti con alto potenziale d'attacco (es. HSM, smart card certificata almeno Common Criteria EAL4+ AVA_VAN.5). Le chiavi vincolate al PID e alla WUA WL3 DEVONO essere archiviate in un WSCD WL3.
  - **WSCD WL2**: basato su ambienti hardware non facilmente certificabili contro alto potenziale d'attacco (es. TEE). Le chiavi vincolate a (Pub/Q)EAA, EAA e WUA WL2 POSSONO essere archiviate in un WSCD WL2.

  Il WSCD WL3 PUÒ essere utilizzato anche per archiviare chiavi private corrispondenti alle Credenziali Elettroniche WL2, purché ogni singola Credenziale Elettronica abbia la propria chiave distinta. Il WSCD WL2 NON DEVE essere utilizzato per ospitare chiavi PID in alcuna circostanza.

Per informazioni più dettagliate, fare riferimento a :ref:`wallet-instance-registration:Inizializzazione e Registrazione dell'Istanza del Wallet` e :ref:`wallet-attestation-issuance:Emissione della Wallet App e Wallet Unit Attestation` di questo documento.

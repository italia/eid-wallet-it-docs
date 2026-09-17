.. include:: ../common/common_definitions.rst
.. Incluso tramite wallet-solution.rst al livello di titolo '^' (livello 2).

Requisiti della Soluzione Wallet
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Questa sezione elenca i requisiti relativi ai Fornitori di Wallet e alle Soluzioni Wallet con le loro Istanze del Wallet, nonché i corrispondenti Wallet Instance Attestation, Key Attestation e il componente di secure storage (WSCD o Keystore).

- La Soluzione Wallet DEVE aderire alle specifiche stabilite da questo documento per ottenere Attestati Elettronici di Dati di Identificazione Personale (PID) e Attestati Elettronici di Attributi (Q)EAA.
- Il Fornitore di Wallet DEVE esporre un insieme di endpoint, disponibili esclusivamente per le istanze della sua Soluzione Wallet, che supportano le funzionalità principali delle Istanze del Wallet.
- L'Istanza del Wallet DEVE periodicamente ristabilire la trust con il suo Fornitore di Wallet, ottenendo una nuova Wallet Instance Attestation (:ref:`WP_018 <wallet-instance-testcases>`).
- L'istanza del Wallet DEVE stabilire un rapporto di fiducia con gli altri partecipanti dell'ecosistema del Wallet, come i Fornitori di Attributi Elettronici. Nel caso dei Fornitori di Attributi Elettronici, l'istanza del Wallet presenta sia la Wallet Instance Attestation che la Key Attestation.
- L'Istanza del Wallet DEVE essere compatibile e funzionale sia sui sistemi operativi Android che iOS e disponibile rispettivamente sul Play Store e sull'App Store (:ref:`WP_015 <wallet-instance-testcases>`).
- L'Istanza del Wallet DEVE fornire un meccanismo per verificare l'effettivo possesso e il pieno controllo da parte dell'Utente del proprio dispositivo personale.
- L'Istanza del Wallet DEVE fornire agli Utenti un elenco aggiornato delle Relying Party con cui l'Utente ha stabilito una connessione e, ove applicabile, tutti i dati scambiati;
- L'Istanza del Wallet DEVE fornire agli Utenti un meccanismo per richiedere la cancellazione degli attributi personali da parte di una Relying Party ai sensi dell'articolo 17 del Regolamento (UE) 2016/679, e per registrare ogni Richiesta di Cancellazione effettuata.

.. note::
   Non esiste una corrispondenza stretta uno-a-uno tra i requisiti in questa sezione e i casi di test in :ref:`test-plans-wallet-provider:Matrice di Test per Wallet Provider`. Alcuni requisiti sono espressi a un livello troppo alto per poter essere rappresentati come casi di test atomici, mentre altri sono già affrontati in modo più dettagliato all'interno dei flussi correlati (ad es. :ref:`wallet-instance-attestation-issuance:Emissione della Wallet Instance Attestation`).

Requisiti della Wallet Instance Attestation
"""""""""""""""""""""""""""""""""""""""""""

la Wallet Instance Attestation contiene informazioni riguardanti il livello di sicurezza del dispositivo che ospita l'Istanza del Wallet.
Esso dimostra principalmente l'**autenticità**, l'**integrità**, la **sicurezza** e in generale l'**affidabilità** di una particolare Istanza del Wallet.

I requisiti per la Wallet Instance Attestation sono definiti di seguito:

- la Wallet Instance Attestation DEVE fornire tutte le informazioni rilevanti per attestare l'**integrità** e la **sicurezza** del dispositivo in cui è installata l'Istanza del Wallet (:ref:`WP_019 <wallet-instance-testcases>`).
- la Wallet Instance Attestation DEVE essere firmato dal Fornitore di Wallet che ha autorità e proprietà sulla Soluzione Wallet, come specificato dalla Registration Authority di supervisione. Questo garantisce che la Wallet Instance Attestation colleghi in modo univoco il Fornitore di Wallet a questa particolare Istanza del Wallet (:ref:`WP_020 <wallet-instance-testcases>`).
- Il Fornitore di Wallet DEVE periodicamente valutare e garantire l'integrità, l'autenticità e la genuinità dell'Istanza del Wallet. Il Fornitore di Wallet verifica l'Istanza del Wallet utilizzando il flusso più sicuro reso disponibile dalle API del Fornitore del Sistema Operativo, come la *Play Integrity API* per Android e *App Attest* per iOS (:ref:`WP_011 <wallet-provider-backend-testcases>`).
- la Wallet Instance Attestation DEVE essere vincolato in modo sicuro alla chiave pubblica effimera dell'Istanza del Wallet (:ref:`WP_019b <wallet-instance-testcases>`).
- la Wallet Instance Attestation PUÒ essere utilizzato più volte durante il suo periodo di validità, consentendo autenticazioni e autorizzazioni ripetute senza la necessità di richiedere nuovi attestati ad ogni interazione. Tuttavia, è RACCOMANDATO che le Istanze del Wallet evitino di utilizzare ripetutamente lo stesso attestato, a causa di preoccupazioni sulla privacy come la possibilità di collegamento tra diverse interazioni.
- La Wallet Instance Attestation DEVE avere un tempo di scadenza (``exp``) al massimo 24 ore dopo l'emissione (``iat``), oltre il quale NON DEVE più essere considerata valida (:ref:`WP_028 <wallet-instance-testcases>`, :ref:`WP_144 <wallet-instance-optional-testcases>`).
- la Wallet Instance Attestation NON DEVE essere rilasciato dal Fornitore di Wallet se l'autenticità, l'integrità e la genuinità dell'Istanza del Wallet che lo richiede non possono essere garantite (:ref:`WP_019a <wallet-instance-testcases>`).
- Ogni Istanza del Wallet DOVREBBE essere in grado di richiedere più Wallet Instance Attestation utilizzando diverse chiavi pubbliche crittografiche associate ad essi.
- la Wallet Instance Attestation NON DEVE contenere informazioni sull'Utente che controlla l'Istanza del Wallet (:ref:`WP_029b <wallet-instance-testcases>`).
- L'Istanza del Wallet DEVE ottenere una Wallet Instance Attestation come prerequisito per passare allo stato Operativo, come definito da `EIDAS-ARF`_.
- Un Wallet Provider DEVE garantire che una Wallet Unit non revocata presenti in ogni momento una Wallet Instance Attestation temporalmente valida e non revocata a un PID Provider o a un Attestation Provider durante il processo di emissione di un PID o di un'attestazione. Nota: questo requisito si applica sia alle attestazioni associate a un dispositivo che a quelle non associate a un dispositivo, come definito da `EIDAS-ARF`_.
- Una Wallet Unit DEVE presentare una Wallet Instance Attestation esclusivamente a un PID Provider o a un Attestation Provider, nell'ambito del processo di emissione di un PID o di un'attestazione, e non a una Relying Party o a qualsiasi altra entità.

.. note::
  In questa sezione, i servizi utilizzati per attestare la genuinità dell'Istanza del Wallet e del dispositivo in cui è installata sono indicati come **API del Servizio di Integrità del Dispositivo**. L'API del Servizio di Integrità del Dispositivo è considerata in modo astratto e si presume sia un servizio fornito da una terza parte affidabile (cioè, l'API del Fornitore del Sistema Operativo) in grado di eseguire controlli di integrità sull'Istanza del Wallet e sul dispositivo in cui è installata.


Requisiti della Key Atestation
""""""""""""""""""""""""""""""""""""""""

La Key Attestation contiene informazioni che garantiscono che le chiavi utilizzate per il collegamento crittografico degli Attestati Elettronici siano archiviate in un WSCD o in un Keystore **affidabile**. Inoltre, fornisce un metodo per autenticare quel componente di memorizzazione presso il Credential Issuer e verifica che la Wallet Unit non sia stata revocata.

I requisiti per la Key Attestation sono definiti di seguito:

- La Key Attestation DEVE fornire al PID Provider o all'Attestation Provider informazioni sulle capacità del WSCA e del WSCD della Wallet Unit, in modo che possano prendere una decisione ben fondata sull'opportunità di emettere un PID o un'attestazione per tale Wallet Unit.
- La Key Attestation DEVE consentire ai PID Provider e agli Attestation Provider di verificare l'autenticità e lo stato di revoca della Wallet Unit.
- Un Wallet Provider DEVE garantire che una Wallet Unit non revocata possa in ogni momento presentare una Key Attestation, quando richiesto da un PID Provider o da un Attestation Provider.
- Durante l'emissione di un PID a Livello di Garanzia Alto, la Wallet Unit DEVE fornire al PID Provider una Key Attestation (KA) valida che descriva il WSCD che ha generato la nuova chiave privata del PID. Le chiavi del PID a LoA High DEVONO essere generate e memorizzate solo in un WSCD. Il profilo implementativo attuale non include l'emissione di PID High; le chiavi dell'IT-Wallet ID e delle (Q)EAA POSSONO essere generate e memorizzate in un Keystore.
- Durante l'emissione di un'attestazione vincolata al dispositivo, una Wallet Unit DEVE recuperare dai metadati dell'Emittente (come specificato in OpenID4VCI_) i requisiti dell'Attestation Provider riguardanti l'archiviazione delle chiavi da parte del WSCA/WSCD o del Keystore. La Wallet Unit DEVE determinare quale dei propri WSCA/WSCD o Keystore, se presente, soddisfi tali requisiti. Se un WSCA/WSCD o un Keystore conforme è disponibile per la Wallet Unit, quest'ultima DEVE fornire all'Attestation Provider una KA valida che descriva il WSCA/WSCD o il Keystore selezionato. Nota: una KA descrive le proprietà del WSCA/WSCD o di un Keystore e contiene una o più chiavi pubbliche corrispondenti a chiavi private generate e archiviate in tale WSCA/WSCD o Keystore.
- Se una Wallet Unit contiene più WSCA, essa DEVE, in modo interno e sicuro, tenere traccia di quali PID e attestazioni sono associati a ciascun WSCA.
- Una Wallet Unit DEVE presentare una Key Attestation solo come parte del processo di emissione di un PID o di un'attestazione.
- La Key Attestation DEVE consentire ai PID Provider di richiedere a un Wallet Provider la revoca di una Wallet Unit, includendo un identificatore per la Wallet Unit all'interno della KA (ad esempio, un URI e un indice a una Attestation Status List). Il Wallet Provider DEVE garantire che tale identificatore della Wallet Unit non consenta il tracciamento dell'utente.
- La Key Attestation DEVE contenere una o più chiavi pubbliche di credenziali attestate provenienti dallo stesso WSCD o Keystore.
- La Key Attestation DEVE essere firmata dal Wallet Provider che ha autorità e proprietà sulla Wallet Solution, come specificato dall'Autorità di Registrazione di riferimento. I Wallet Provider DEVONO garantire che i certificati utilizzati per firmare le KA e le WIA siano conformi a tutti i requisiti applicabili della `ETSI TS 119 412-6`_, in particolare alla Clausola 5.
- Un Attestation Provider che emette attestazioni non vincolate al dispositivo DEVE indicare nei propri metadati di Credential Issuer che non necessita di una KA. Una Wallet Unit NON DEVE inviare una KA a un Attestation Provider quando richiede un'attestazione non vincolata al dispositivo. Nota: una Wallet Unit invia una WIA all'Attestation Provider indipendentemente dal fatto che le attestazioni da esso emesse siano vincolate al dispositivo o meno.
- Un Wallet Provider DEVE garantire che la presentazione di una KA sia crittograficamente vincolata allo specifico contesto in cui è destinata a essere utilizzata. Nota: come specificato in OpenID4VCI_, ciò si ottiene facendo sì che la KA firmata contenga essa stessa un nonce fornito dal PID Provider o dall'Attestation Provider durante il processo di emissione. In alternativa, la Wallet Unit presenta la KA insieme a una Proof-of-Possession costituita da una firma su tale nonce, creata dalla chiave privata corrispondente a una delle chiavi pubbliche attestate nella KA.
- Durante l'emissione di un PID o di un'attestazione vincolata al dispositivo, il PID Provider o l'Attestation Provider DEVE verificare la KA in conformità ai requisiti dell'Appendice F.4 di OpenID4VCI_.
- Durante l'emissione di un PID o di un'attestazione vincolata al dispositivo, il PID Provider o l'Attestation Provider DEVE ricevere una prova che la Wallet Unit possiede le chiavi private corrispondenti a tutte le chiavi pubbliche presenti nella KA.
- Il WSCA, il WSCD o il Keystore NON DEVONO consentire l'esportazione in chiaro delle chiavi private dell'Utente. Se un dispositivo segnala una chiave privata come esportabile, il Fornitore di Wallet DEVE rifiutare la Key Attestation e NON DEVE attivare l'Istanza del Wallet (:ref:`WP_014b <wallet-instance-testcases>`).
- Un Wallet Provider DEVE considerare tutti i fattori rilevanti, inclusi l'uso offline, l'interoperabilità e il rischio che una KA diventi un vettore per tracciare l'Utente, nel decidere il periodo di validità di una KA.
- La Key Attestation NON DEVE essere emessa dal Wallet Provider se l'affidabilità del WSCD o del Keystore non è garantita. In tal caso, l'Istanza del Wallet DEVE essere revocata.


Requisiti WSCD e Keystore
"""""""""""""""""""""""""

Per garantire la massima sicurezza, le chiavi crittografiche associate a un'Istanza del Wallet (ad esempio, utilizzate per generare la Wallet Instance Attestation) DEVONO essere generate e memorizzate in modo sicuro in un **Keystore** o in un **WSCD**, come definiti in :ref:`defined-terms:Definizioni e Acronimi`.
L'Utente DEVE mantenere il controllo esclusivo di tali chiavi private (Sole Control). Il Keystore o il WSCD DEVE richiedere l'autenticazione dell'Utente (sblocco del Wallet: PIN o biometrico) prima di qualsiasi firma o altra operazione con la chiave privata (:ref:`WP_014c <wallet-instance-testcases>`).

Possono essere utilizzati i seguenti approcci:

- **Keystore Interno Locale**: memorizzazione delle chiavi hardware-backed nativa del dispositivo dell'Utente, come il Secure Enclave su iOS, o il Trusted Execution Environment (TEE) e StrongBox su Android. È il componente denominato Local Internal WSCD in alcuni testi ARF. È un Keystore, non un WSCD certificabile High.
- **WSCD Esterno Locale**: hardware esterno al dispositivo dell'Utente, come una smart card conforme a *GlobalPlatform* e che supporta *JavaCard*, certificabile come WSCD.
- **WSCD Remoto**: un Hardware Security Module (HSM) remoto certificabile come WSCD.
- **WSCD Ibrido Locale**: un componente hardware interno collegabile all'interno del dispositivo dell'Utente, come un *eUICC* che aderisce agli standard *GlobalPlatform* e supporta *JavaCard*.
- **WSCD Ibrido Remoto**: un componente locale combinato con un servizio remoto.

Le chiavi private di un IT-Wallet ID e di una (Q)EAA POSSONO essere memorizzate in un Keystore Interno Locale (eIDAS Substantial). Le chiavi private di un PID a LoA High DEVONO essere memorizzate solo in un WSCD. Un Keystore Interno Locale NON DEVE essere trattato come prova di LoA High. Le chiavi private vincolate a una WIA DEVONO essere generate e memorizzate nello stesso Keystore o WSCD che la WIA attesta (:ref:`WP_014 <wallet-instance-testcases>`–:ref:`WP_014e <wallet-instance-testcases>`).

Un'Istanza di Relying Party Mobile che non memorizza chiavi di identità dell'Utente PUÒ usare un Keystore Interno Locale e non è tenuta a usare un WSCD certificabile High (:ref:`WP_014f <wallet-instance-testcases>`).

Gli Attestati Elettronici le cui chiavi private vincolate sono memorizzate in un Keystore locale o in un WSCD locale POSSONO essere presentati in prossimità o comunque offline. Gli Attestati Elettronici le cui chiavi private vincolate sono memorizzate in un WSCD remoto NON DEVONO essere presentati offline (:ref:`WP_160 <wallet-instance-testcases>`).

.. warning::
  Nella fase attuale, il profilo di implementazione definito in questo documento supporta solo il **Keystore Interno Locale** (:ref:`WP_014 <wallet-instance-testcases>`). Le versioni future di questa specifica POTREBBERO includere altri approcci a seconda del Livello di Garanzia dell'Autenticatore richiesto (`AAL`).

Per informazioni più dettagliate, fare riferimento a :ref:`wallet-instance-registration:Inizializzazione e Registrazione dell'Istanza del Wallet`, :ref:`wallet-instance-attestation-issuance:Emissione della Wallet Instance Attestation` e :ref:`wallet-attestation-issuance:Emissione della Key Attestation` di questo documento.



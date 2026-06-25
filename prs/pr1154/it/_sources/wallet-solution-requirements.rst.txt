.. include:: ../common/common_definitions.rst
.. Incluso tramite wallet-solution.rst al livello di titolo '^' (livello 2).

Requisiti della Soluzione Wallet
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Questa sezione elenca i requisiti relativi ai Fornitori di Wallet e alle Soluzioni Wallet con le loro Istanze del Wallet, nonché i corrispondenti Wallet Instance Attestation, Wallet Unit Attestation e il componente di secure storage (WSCD).

- La Soluzione Wallet DEVE aderire alle specifiche stabilite da questo documento per ottenere Attestati Elettronici di Dati di Identificazione Personale (PID) e Attestati Elettronici di Attributi (Q)EAA.
- Il Fornitore di Wallet DEVE esporre un insieme di endpoint, disponibili esclusivamente per le istanze della sua Soluzione Wallet, che supportano le funzionalità principali delle Istanze del Wallet.
- L'Istanza del Wallet DEVE periodicamente ristabilire la trust con il suo Fornitore di Wallet, ottenendo una nuova Wallet Instance Attestation (:ref:`WP_018 <wallet-instance-testcases>`).
- L'istanza del Wallet DEVE stabilire un rapporto di fiducia con gli altri partecipanti dell'ecosistema del Wallet, come i Fornitori di Attributi Elettronici. Nel caso dei Fornitori di Attributi Elettronici, l'istanza del Wallet presenta sia la Wallet Instance Attestation che la Wallet Unit Attestation.
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
- La Wallet Instance Attestation DEVE avere una durata limitata e DEVE includere un tempo di scadenza, oltre il quale NON DEVE più essere considerata valida.
- la Wallet Instance Attestation NON DEVE essere rilasciato dal Fornitore di Wallet se l'autenticità, l'integrità e la genuinità dell'Istanza del Wallet che lo richiede non possono essere garantite (:ref:`WP_019a <wallet-instance-testcases>`).
- Ogni Istanza del Wallet DOVREBBE essere in grado di richiedere più Wallet Instance Attestation utilizzando diverse chiavi pubbliche crittografiche associate ad essi.
- la Wallet Instance Attestation NON DEVE contenere informazioni sull'Utente che controlla l'Istanza del Wallet (:ref:`WP_029b <wallet-instance-testcases>`).
- L'Istanza del Wallet DEVE ottenere una Wallet Instance Attestation come prerequisito per passare allo stato Operativo, come definito da `EIDAS-ARF`_.
- Un Wallet Provider DEVE garantire che una Wallet Unit non revocata presenti in ogni momento una Wallet Instance Attestation temporalmente valida e non revocata a un PID Provider o a un Attestation Provider durante il processo di emissione di un PID o di un'attestazione. Nota: questo requisito si applica sia alle attestazioni associate a un dispositivo che a quelle non associate a un dispositivo, come definito da `EIDAS-ARF`_.
- Una Wallet Unit DEVE presentare una Wallet Instance Attestation esclusivamente a un PID Provider o a un Attestation Provider, nell'ambito del processo di emissione di un PID o di un'attestazione, e non a una Relying Party o a qualsiasi altra entità.

.. note::
  In questa sezione, i servizi utilizzati per attestare la genuinità dell'Istanza del Wallet e del dispositivo in cui è installata sono indicati come **API del Servizio di Integrità del Dispositivo**. L'API del Servizio di Integrità del Dispositivo è considerata in modo astratto e si presume sia un servizio fornito da una terza parte affidabile (cioè, l'API del Fornitore del Sistema Operativo) in grado di eseguire controlli di integrità sull'Istanza del Wallet e sul dispositivo in cui è installata.


Requisiti della Wallet Unit Attestation
"""""""""""""""""""""""""""""""""""""""

La Wallet Unit Attestation contiene informazioni che garantiscono che le chiavi utilizzate per il collegamento crittografico degli Attestati Elettronici siano archiviate in un WSCD **affidabile**. Inoltre, fornisce un metodo per autenticare il WSCD presso il Fornitore di Attributi Elettronici e verifica che la Wallet Unit non sia stata revocata.

I requisiti per la Wallet Unit Attestation sono definiti di seguito:

- La Wallet Unit Attestation DEVE fornire al PID Provider o all'Attestation Provider informazioni sulle capacità del WSCA e del WSCD della Wallet Unit, in modo che possano prendere una decisione ben fondata sull'opportunità di emettere un PID o un'attestazione per tale Wallet Unit.
- La Wallet Unit Attestation DEVE consentire ai PID Provider e agli Attestation Provider di verificare l'autenticità e lo stato di revoca della Wallet Unit.
- Un Wallet Provider DEVE garantire che una Wallet Unit non revocata possa in ogni momento presentare una Wallet Unit Attestation, quando richiesto da un PID Provider o da un Attestation Provider.
- Durante l'emissione di un PID, la Wallet Unit DEVE fornire al PID Provider una WUA valida che descriva il WSCA/WSCD che ha generato la nuova chiave privata del PID. Nota: una chiave privata del PID è sempre generata e gestita dal WSCA/WSCD, che per definizione è conforme ai requisiti per il Livello di Garanzia Alto.
- Durante l'emissione di un'attestazione vincolata al dispositivo, una Wallet Unit DEVE recuperare dai metadati dell'emittente (come specificato in `OpenID4VCI`_) i requisiti dell'Attestation Provider riguardanti l'archiviazione delle chiavi da parte del WSCA/WSCD. La Wallet Unit DEVE determinare quale dei propri WSCA/WSCD, se presente, soddisfi tali requisiti. Se un WSCA/WSCD o un keystore conforme è disponibile per la Wallet Unit, quest'ultima DEVE fornire all'Attestation Provider una WUA valida che descriva il WSCA/WSCD o il keystore selezionato. Nota: una WUA descrive le proprietà del WSCA/WSCD o di un keystore e contiene una o più chiavi pubbliche corrispondenti a chiavi private generate e archiviate in tale WSCA/WSCD o keystore.
- Se una Wallet Unit contiene più WSCA, essa DEVE, in modo interno e sicuro, tenere traccia di quali PID e attestazioni sono associati a ciascun WSCA.
- Una Wallet Unit DEVE presentare una Wallet Unit Attestation solo come parte del processo di emissione di un PID o di un'attestazione vincolata a chiave.
- La Wallet Unit Attestation DEVE consentire ai PID Provider di richiedere a un Wallet Provider la revoca di una Wallet Unit, includendo un identificatore per la Wallet Unit all'interno della WUA (ad esempio, un URI e un indice a una Attestation Status List). Il Wallet Provider DEVE garantire che tale identificatore della Wallet Unit non consenta il tracciamento dell'utente.
- La Wallet Unit Attestation DEVE contenere una o più chiavi pubbliche di credenziali attestate provenienti dallo stesso WSCD.
- La Wallet Unit Attestation DEVE essere firmata dal Wallet Provider che ha autorità e proprietà sulla Wallet Solution, come specificato dall'Autorità di Registrazione di riferimento. I Wallet Provider DEVONO garantire che i certificati utilizzati per firmare le WUA e le WIA siano conformi a tutti i requisiti applicabili della `ETSI TS 119 412-6`_, in particolare alla Clausola 5.
- Un Attestation Provider che emette attestazioni non vincolate al dispositivo DEVE indicare nei propri metadati di Credential Issuer che non necessita di una WUA. Una Wallet Unit NON DEVE inviare una WUA a un Attestation Provider quando richiede un'attestazione non vincolata al dispositivo. Nota: una Wallet Unit invia una WIA all'Attestation Provider indipendentemente dal fatto che le attestazioni emesse siano vincolate al dispositivo o meno.
- Un Wallet Provider DEVE garantire che la presentazione di una WUA sia crittograficamente vincolata allo specifico contesto in cui è destinata a essere utilizzata. Nota: come specificato in `OpenID4VCI`_, ciò si ottiene facendo sì che la WUA firmata contenga essa stessa un nonce fornito dal PID Provider o dall'Attestation Provider durante il processo di emissione. In alternativa, la Wallet Unit presenta la WUA insieme a una Proof-of-Possession consistente in una firma su tale nonce, creata con la chiave privata corrispondente a una delle chiavi pubbliche attestate nella WUA.
- Durante l'emissione di un PID o di un'attestazione vincolata al dispositivo, il PID Provider o l'Attestation Provider DEVE verificare la WUA in conformità ai requisiti dell'Appendice F.4 di `OpenID4VCI`_.
- Durante l'emissione di un PID o di un'attestazione vincolata al dispositivo, il PID Provider o l'Attestation Provider DEVE ricevere una prova che la Wallet Unit possiede le chiavi private corrispondenti a tutte le chiavi pubbliche presenti nella WUA.
- Se il WSCA/WSCD è in grado di esportare una chiave privata, il Wallet Provider DEVE specificare questa capacità come attributo nella WUA.
- Un Wallet Provider DEVE considerare tutti i fattori rilevanti, inclusi l'utilizzo offline, l'interoperabilità e il rischio che una WUA diventi un vettore di tracciamento dell'Utente, nel decidere il periodo di validità di una WUA.
- La Wallet Unit Attestation NON DEVE essere emessa dal Wallet Provider se l'affidabilità del WSCD non è garantita. In tal caso, l'istanza del Wallet DEVE essere revocata.


Requisiti WSCD
""""""""""""""

Per garantire la massima sicurezza, le chiavi crittografiche associate a un'Istanza del Wallet (ad esempio, utilizzate per generare la Wallet Instance Attestation) DEVONO essere generate e memorizzate in modo sicuro all'interno del Dispositivo Crittografico Sicuro per il Portafoglio (WSCD).
Solo l'Utente legittimo può accedere alle chiavi crittografiche private, impedendo l'uso non autorizzato o la manomissione. Il WSCD PUÒ essere implementato utilizzando almeno uno degli approcci elencati di seguito:

- **WSCD Interno Locale**: Il WSCD si basa interamente sull'hardware crittografico nativo del dispositivo, come il Secure Enclave su iOS, o il Trusted Execution Environment (TEE) e Strongbox su Android.
- **WSCD Esterno Locale**: Il WSCD è un hardware esterno al dispositivo dell'Utente, come una smart card conforme a *GlobalPlatform* e che supporta *JavaCard*.
- **WSCD Remoto**: Il WSCD utilizza un Hardware Security Module (HSM) remoto.
- **WSCD Ibrido Locale**: Il WSCD coinvolge un componente hardware interno collegabile all'interno del dispositivo dell'Utente, come un *eUICC* che aderisce agli standard *GlobalPlatform* e supporta *JavaCard*.
- **WSCD Ibrido Remoto**: Il WSCD coinvolge un componente locale combinato con un servizio remoto.

.. warning::
  Nella fase attuale, il profilo di implementazione definito in questo documento supporta solo il **WSCD Interno Locale** (:ref:`WP_014 <wallet-instance-testcases>`). Le versioni future di questa specifica POTREBBERO includere altri approcci a seconda del Livello di Garanzia dell'Autenticatore richiesto (`AAL`).

Per informazioni più dettagliate, fare riferimento a :ref:`wallet-instance-registration:Inizializzazione e Registrazione dell'Istanza del Wallet`, :ref:`wallet-instance-attestation-issuance:Emissione della Wallet Instance Attestation` e :ref:`wallet-attestation-issuance:Emissione della Wallet Unit Attestation` di questo documento.



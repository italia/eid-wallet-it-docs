.. include:: ../common/common_definitions.rst

.. level 2 "included" file, so we start with '^' title level

Requisiti della Soluzione Wallet
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Questa sezione elenca i requisiti relativi ai Fornitori di Wallet e alle Soluzioni Wallet con le loro Istanze del Wallet.

- La Soluzione Wallet DEVE aderire alle specifiche stabilite da questo documento per ottenere Attestati Elettronici di Dati di Identificazione Personale (PID) e Attestati Elettronici di Attributi (Q)EAA.
- Il Fornitore di Wallet DEVE esporre un insieme di endpoint, disponibili esclusivamente per le istanze della sua Soluzione Wallet, che supportano le funzionalità principali delle Istanze del Wallet.
- L'Istanza del Wallet DEVE periodicamente ristabilire la trust con il suo Fornitore di Wallet, ottenendo un nuovo Attestato di Wallet.
- L'Istanza del Wallet DEVE stabilire la trust con altri partecipanti dell'ecosistema Wallet, come i Fornitori di Credenziali e le Relying Party, presentando un Attestato di Wallet.
- L'Istanza del Wallet DEVE essere compatibile e funzionale sia sui sistemi operativi Android che iOS e disponibile rispettivamente sul Play Store e sull'App Store.
- L'Istanza del Wallet DEVE fornire un meccanismo per verificare l'effettivo possesso e il pieno controllo da parte dell'Utente del proprio dispositivo personale.
- L'Istanza del Wallet DEVE fornire agli Utenti un elenco aggiornato delle Relying Party con cui l'Utente ha stabilito una connessione e, ove applicabile, tutti i dati scambiati;
- L'Istanza del Wallet DEVE fornire agli Utenti un meccanismo per richiedere la cancellazione degli attributi personali da parte di una Relying Party ai sensi dell'articolo 17 del Regolamento (UE) 2016/679, e per registrare ogni Richiesta di Cancellazione effettuata.

Requisiti dell'Attestato di Wallet
""""""""""""""""""""""""""""""""""

L'Attestato di Wallet contiene informazioni riguardanti il livello di sicurezza del dispositivo che ospita l'Istanza del Wallet.
Esso dimostra principalmente l'**autenticità**, l'**integrità**, la **sicurezza** e in generale l'**affidabilità** di una particolare Istanza del Wallet.

I requisiti per l'Attestato di Wallet sono definiti di seguito:

- L'Attestato di Wallet DEVE fornire tutte le informazioni rilevanti per attestare l'**integrità** e la **sicurezza** del dispositivo in cui è installata l'Istanza del Wallet.
- L'Attestato di Wallet DEVE essere firmato dal Fornitore di Wallet che ha autorità e proprietà sulla Soluzione Wallet, come specificato dalla Registration Authority di supervisione. Questo garantisce che l'Attestato di Wallet colleghi in modo univoco il Fornitore di Wallet a questa particolare Istanza del Wallet.
- Il Fornitore di Wallet DEVE periodicamente valutare e garantire l'integrità, l'autenticità e la genuinità dell'Istanza del Wallet. Il Fornitore di Wallet verifica l'Istanza del Wallet utilizzando il flusso più sicuro reso disponibile dalle API del Fornitore del Sistema Operativo, come la *Play Integrity API* per Android e *App Attest* per iOS.
- Il Fornitore di Wallet DEVE possedere un meccanismo di revoca per l'Istanza del Wallet, che consenta al Fornitore di Wallet di terminare il servizio per una specifica Istanza in qualsiasi momento.
- L'Attestato di Wallet DEVE essere vincolato in modo sicuro alla chiave pubblica effimera dell'Istanza del Wallet.
- L'Attestato di Wallet PUÒ essere utilizzato più volte durante il suo periodo di validità, consentendo autenticazioni e autorizzazioni ripetute senza la necessità di richiedere nuovi attestati ad ogni interazione. Tuttavia, è RACCOMANDATO che le Istanze del Wallet evitino di utilizzare ripetutamente lo stesso attestato, a causa di preoccupazioni sulla privacy come la possibilità di collegamento tra diverse interazioni.
- L'Attestato di Wallet che non implementa metodi di controllo della revoca, DEVE avere una durata breve e DEVE avere un tempo di scadenza, dopo il quale NON DEVE più essere considerato valido.
- L'Attestato di Wallet NON DEVE essere rilasciato dal Fornitore di Wallet se l'autenticità, l'integrità e la genuinità dell'Istanza del Wallet che lo richiede non possono essere garantite.
- Ogni Istanza del Wallet DOVREBBE essere in grado di richiedere più Attestati di Wallet utilizzando diverse chiavi pubbliche crittografiche associate ad essi.
- L'Attestato di Wallet NON DEVE contenere informazioni sull'Utente che controlla l'Istanza del Wallet.
- L'Istanza del Wallet DEVE ottenere un Attestato di Wallet come prerequisito per passare allo stato Operativo, come definito da `EIDAS-ARF`_.


.. note::
  In questa sezione, i servizi utilizzati per attestare la genuinità dell'Istanza del Wallet e del dispositivo in cui è installata sono indicati come **API del Servizio di Integrità del Dispositivo**. L'API del Servizio di Integrità del Dispositivo è considerata in modo astratto e si presume sia un servizio fornito da una terza parte affidabile (cioè, l'API del Fornitore del Sistema Operativo) in grado di eseguire controlli di integrità sull'Istanza del Wallet e sul dispositivo in cui è installata.

Requisiti WSCD
""""""""""""""

Per garantire la massima sicurezza, le chiavi crittografiche associate a un'Istanza del Wallet (ad esempio, utilizzate per generare l'Attestato di Wallet) DEVONO essere generate e memorizzate in modo sicuro all'interno del Dispositivo Crittografico Sicuro per il Portafoglio (WSCD).
Solo l'Utente legittimo può accedere alle chiavi crittografiche private, impedendo l'uso non autorizzato o la manomissione. Il WSCD PUÒ essere implementato utilizzando almeno uno degli approcci elencati di seguito:

- **WSCD Interno Locale**: Il WSCD si basa interamente sull'hardware crittografico nativo del dispositivo, come il Secure Enclave su iOS, o il Trusted Execution Environment (TEE) e Strongbox su Android.
- **WSCD Esterno Locale**: Il WSCD è un hardware esterno al dispositivo dell'Utente, come una smart card conforme a *GlobalPlatform* e che supporta *JavaCard*.
- **WSCD Remoto**: Il WSCD utilizza un Hardware Security Module (HSM) remoto.
- **WSCD Ibrido Locale**: Il WSCD coinvolge un componente hardware interno collegabile all'interno del dispositivo dell'Utente, come un *eUICC* che aderisce agli standard *GlobalPlatform* e supporta *JavaCard*.
- **WSCD Ibrido Remoto**: Il WSCD coinvolge un componente locale combinato con un servizio remoto.

.. warning::
  Nella fase attuale, il profilo di implementazione definito in questo documento supporta solo il **WSCD Interno Locale**. Le versioni future di questa specifica POTREBBERO includere altri approcci a seconda del Livello di Garanzia dell'Autenticatore richiesto (`AAL`).

Per informazioni più dettagliate, fare riferimento a :ref:`wallet-instance-registration:Inizializzazione e Registrazione dell'Istanza del Wallet` e :ref:`wallet-attestation-issuance:Emissione dell'Attestato di Wallet` di questo documento.

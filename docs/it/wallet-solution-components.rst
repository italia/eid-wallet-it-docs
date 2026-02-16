.. include:: ../common/common_definitions.rst


Componenti della Soluzione Wallet
=================================

.. note::
   I test relativi ai componenti della Wallet Solution (Backend del Wallet e Unità di Wallet) sono riassunti in :ref:`WP_012 <wallet-provider-backend-testcases>` e in :ref:`WP_013 <wallet-instance-testcases>`, rispettivamente.

.. _wallet-solution-components-decomposition:

Scomposizione e Ambito di Certificazione
-----------------------------------------

La **certificazione** è il processo con cui gli Organismi di Valutazione della Conformità valutano le soluzioni tecniche rispetto ai requisiti di sicurezza e conformità previsti dal `CIR 2024/2981`_. La **scomposizione dei componenti per la certificazione** è una struttura gerarchica (macro-componente di certificazione, componente, sottocomponente) utilizzata per definire l'ambito della valutazione della certificazione e stabilire la tracciabilità tra elementi architetturali e requisiti di certificazione.

Questa sezione specifica la mappatura tra i componenti della Soluzione Wallet descritti in questa specifica tecnica e il macro-componente di certificazione **Servizi ICT Wallet** (proprietario: Fornitore di Wallet). Indica quali componenti sono conformi alla scomposizione e rientrano nell'ambito di certificazione.

.. list-table:: Soluzione Wallet — Mappatura Scomposizione
   :widths: 30 40 15
   :header-rows: 1

   * - Componente / Sottocomponente
     - Equivalente nella Specifica Tecnica
     - Ambito Certificazione
   * - **Wallet Instance (WI)** — Application Logic
     - User Interface, Issuer Component, Presentation Component, Wallet Instance Lifecycle Management
     - In scopo
   * - **Wallet Instance (WI)** — Local Data management
     - Local Data Store, Backup and Restore Component, interazione Secure Storage
     - In scopo
   * - **Wallet Instance (WI)** — Presentation Interface (PI)
     - Presentazione remota e di prossimità PID/(Pub/Q)EAA (`OpenID4VP`_, `ISO18013-5`_)
     - In scopo
   * - **Wallet Instance (WI)** — Attestation Issuance Interface
     - PID Issuance Interface (PII), Attestation Issuance Interface (AII)
     - In scopo
   * - **Wallet Secure Cryptographic Device (WSCD)**
     - Hardware Secure Element, WSCD Firmware, Secure Key Storage System
     - In scopo
   * - **Wallet Secure Cryptographic Application (WSCA)**
     - WSCD Interface (WWI), WSCA Authentication, Cryptographic Keys and Functions Manager
     - In scopo
   * - **Wallet Provider Backend (WPBE)** — API Interface
     - API Interface (incl. PDND per notifiche da PID Provider)
     - In scopo
   * - **Wallet Provider Backend (WPBE)** — Wallet Instance Lifecycle Management
     - Registrazione, Attestation Issuance (WAA/WUA), Status e revoca
     - In scopo
   * - **Wallet Provider Backend (WPBE)** — Trust & Security Component
     - Gestione chiavi e certificati, audit logging, incident response, conformità Federation
     - In scopo
   * - **Wallet Provider Backend (WPBE)** — User web portal
     - Frontend Component
     - In scopo

Per lo schema di certificazione completo e gli elementi trasversali (ad es. eID Scheme), vedere :ref:`annex-certification-scheme:Schema di Certificazione e Approccio Complessivo`.

Backend del Wallet
------------------

Componente Frontend
^^^^^^^^^^^^^^^^^^^

Il Componente Frontend DEVE fornire un'interfaccia Utente basata sul web per la gestione dell'Istanza del Wallet, offrendo funzionalità per:

- Visualizzare e verificare le Istanze del Wallet e il loro stato.
- Gestire il ciclo di vita dell'Istanza del Wallet (ad esempio, revoca).
- Fornire supporto e documentazione all'Utente.

Interfaccia API
^^^^^^^^^^^^^^^

Questo componente DEVE:

- inoltrare la richiesta dal Componente Frontend o dall'Istanza del Wallet al componente di Gestione del Ciclo di Vita dell'Istanza del Wallet.
- utilizzare PDND secondo le regole nella Sezione :ref:`e-service-pdnd:e-Service PDND` per essere notificato dal Fornitore di Attestati Elettronici di Dati di Identificazione Personale della necessità di revocare l'Istanza del Wallet e cancellare l'account dell'Utente a causa del decesso dell'Utente.

Gestione del Ciclo di Vita dell'Istanza del Wallet
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Questo componente DEVE gestire:

- Registrazione dell'Istanza del Wallet (dettagliata in :ref:`wallet-instance-registration:Inizializzazione e Registrazione dell'Istanza del Wallet`).
- Emissione della Wallet App e Wallet Unit Attestation (dettagliata in :ref:`wallet-attestation-issuance:Emissione della Wallet App e Wallet Unit Attestation`).
- Gestione dello stato (mantenimento e aggiornamento della validità).
- Processi di revoca (implementazione di meccanismi per revocare le Istanze del Wallet), secondo la Sezione :ref:`wallet-instance-revocation:Revoca dell'Istanza del Wallet`.

Componente Trust & Security
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Questo componente DEVE garantire la sicurezza attraverso:

- Gestione di chiavi e certificati.
- Registrazione degli audit.
- Monitoraggio della sicurezza e risposta agli incidenti.
- Conformità ai requisiti di sicurezza della Federazione IT-Wallet.



Unità di Wallet
---------------

Interfaccia Utente
^^^^^^^^^^^^^^^^^^

L'Interfaccia Utente è il punto di interazione e comunicazione tra l'Utente e l'Istanza del Wallet.

Componente di Gestione del Ciclo di Vita dell'Istanza del Wallet
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Interagendo con il Backend del Wallet, questo componente DEVE gestire:

- Registrazione dell'Istanza del Wallet (dettagliata in :ref:`wallet-instance-registration:Inizializzazione e Registrazione dell'Istanza del Wallet`).
- Emissione della Wallet Unit Attestation (dettagliata in :ref:`wallet-attestation-issuance:Emissione della Wallet App e Wallet Unit Attestation`).
- Gestione dello stato (mantenimento e aggiornamento della validità).
- Processi di revoca (implementazione di meccanismi per revocare le Istanze del Wallet), secondo la Sezione :ref:`wallet-instance-revocation:Revoca dell'Istanza del Wallet`.

In base allo stato dell'Istanza del Wallet e alla richiesta dell'Utente, questo componente interagisce con gli altri componenti dell'Istanza del Wallet.

Componente Issuer
^^^^^^^^^^^^^^^^^

Seguendo la specifica `OpenID4VCI`_ e il profilo di implementazione nella Sezione :ref:`credential-issuance:Emissione di Attestati Elettronici`, questo componente DEVE implementare i protocolli e i flussi di emissione delle Credenziali Elettroniche per richiedere Credenziali Elettroniche ai Credential Issuer.

Componente di Presentazione
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Seguendo il profilo di implementazione nella Sezione :ref:`credential-presentation:Presentazione dell'Attestato Elettronico`, questo componente DEVE essere conforme ai flussi remoti basati su `OpenID4VP`_ e ai flussi di prossimità basati su `ISO18013-5`_.

Componente di Backup e Ripristino
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Per ogni Credenziale Elettronica emessa all'Istanza del Wallet, questo componente DEVE aggiungere tutti i dati necessari per richiedere la riemissione di quella Credenziale Elettronica come specificato nella Sezione :ref:`backup-restore:Backup e Ripristino`.

.. note::
   Attualmente la riemissione del PID non è gestita dal Componente di Backup e Ripristino.


Archiviazione Sicura
^^^^^^^^^^^^^^^^^^^^

L'Istanza del Wallet DEVE utilizzare questo componente per proteggere gli asset critici e per eseguire in modo sicuro funzioni crittografiche.


Modelli di Interazione della Soluzione Wallet
=============================================

La Soluzione Wallet supporta questi modelli di interazione:

1. **Utente verso Frontend del Backend del Wallet**: Interazioni basate sul web per la gestione dell'Istanza del Wallet.
2. **Istanza del Wallet verso API del Backend del Wallet**: per la registrazione dell'Istanza del Wallet e l'emissione della Wallet App e Wallet Unit Attestation.
3. **Fornitore di Attestati Elettronici di Dati di Identificazione Personale verso API del Backend del Wallet**: Chiamate API sicure per richiedere la revoca dell'Istanza del Wallet.
4. **Utente verso Interfaccia Utente dell'Istanza del Wallet**: per la gestione delle Credenziali Elettroniche (emissione, presentazione, backup, ripristino, eliminazione).
5. **Istanza del Wallet verso Relying Party**: per la presentazione delle Credenziali Elettroniche.

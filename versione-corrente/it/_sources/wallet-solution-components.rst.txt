.. include:: ../common/common_definitions.rst


Componenti della Soluzione Wallet
=================================

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
- Emissione dell'Attestato di Unità di Portafoglio (dettagliata in :ref:`wallet-attestation-issuance:Emissione dell'Attestato di Wallet`).
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
- Emissione dell'Attestato di Unità di Portafoglio (dettagliata in :ref:`wallet-attestation-issuance:Emissione dell'Attestato di Wallet`).
- Gestione dello stato (mantenimento e aggiornamento della validità).
- Processi di revoca (implementazione di meccanismi per revocare le Istanze del Wallet), secondo la Sezione :ref:`wallet-instance-revocation:Revoca dell'Istanza del Wallet`.

In base allo stato dell'Istanza del Wallet e alla richiesta dell'Utente, questo componente interagisce con gli altri componenti dell'Istanza del Wallet.

Componente Issuer
^^^^^^^^^^^^^^^^^

Seguendo la specifica `OpenID4VCI`_ e il profilo di implementazione nella Sezione :ref:`credential-issuance:Emissione di Attestati Elettronici`, questo componente DEVE implementare i protocolli e i flussi di emissione delle Credenziali Elettroniche per richiedere Credenziali Elettroniche ai Credential Issuer.

Componente di Presentazione
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Seguendo il profilo di implementazione nella Sezione :ref:`credential-presentation:Presentazione della Credenziale Digitale`, questo componente DEVE essere conforme ai flussi remoti basati su `OpenID4VP`_ e ai flussi di prossimità basati su `ISO18013-5`_.

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
2. **Istanza del Wallet verso API del Backend del Wallet**: per la registrazione dell'Istanza del Wallet e l'emissione dell'Attestato di Unità di Portafoglio.
3. **Fornitore di Attestati Elettronici di Dati di Identificazione Personale verso API del Backend del Wallet**: Chiamate API sicure per richiedere la revoca dell'Istanza del Wallet.
4. **Utente verso Interfaccia Utente dell'Istanza del Wallet**: per la gestione delle Credenziali Elettroniche (emissione, presentazione, backup, ripristino, eliminazione).
5. **Istanza del Wallet verso Relying Party**: per la presentazione delle Credenziali Elettroniche.

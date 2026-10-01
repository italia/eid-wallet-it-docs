.. include:: ../common/common_definitions.rst


Funzionalità dell'Istanza del Wallet
====================================

Un'Istanza del Wallet DEVE supportare le seguenti funzionalità, corrispondenti alle funzionalità principali di [`CIR2024/2979`_] eccetto l'interazione Wallet-to-Wallet e la creazione di firme elettroniche qualificate, che sono fuori dall'ambito di questa versione:

  - Registrazione del Wallet (dettagliata in :ref:`wallet-instance-registration:Inizializzazione e Registrazione dell'Istanza del Wallet`),
  - Emissione della Wallet Instance Attestation (descritta in dettaglio in :ref:`wallet-instance-attestation-issuance:Emissione della Wallet Instance Attestation`),
  - Emissione della Key Attestation (descritta in dettaglio in :ref:`wallet-attestation-issuance:Emissione della Key Attestation`),
  - Emissione di Attestati Elettronici (dettagliata in :ref:`credential-issuance:Emissione di Attestati Elettronici`),
  - Presentazione di Attestati Elettronici, in remoto e in prossimità (dettagliata in :ref:`credential-presentation:Presentazione dell'Attestato Elettronico`),
  - Disclosure selettiva degli attributi,
  - Dashboard delle transazioni (dettagliata in :ref:`wallet-instance-dashboard:Dashboard dell’Istanza del Wallet e Registrazione delle Transazioni`),
  - Revoca del Wallet (dettagliata in :ref:`wallet-instance-revocation:Revoca dell'Istanza del Wallet`) e
  - Cancellazione degli attributi presentati (dettagliata in :ref:`user-attribute-deletion:Eliminazione degli Attributi dell'Utente`).

Ciascuna funzionalità è descritta in dettaglio nelle sezioni seguenti.

.. note::
  I dettagli forniti di seguito sono non normativi e hanno lo scopo di chiarire le funzionalità della Registrazione dell'Istanza del Wallet. L'implementazione effettiva può variare in base al caso d'uso specifico e ai requisiti del Fornitore di Wallet.

.. toctree::
  :caption: Indice delle Funzionalità dell'Istanza del Wallet
  :maxdepth: 3

  wallet-instance-registration.rst
  wallet-instance-attestation-issuance.rst
  wallet-attestation-issuance.rst
  wallet-instance-revocation.rst
  user-attribute-deletion.rst
  wallet-instance-dashboard.rst



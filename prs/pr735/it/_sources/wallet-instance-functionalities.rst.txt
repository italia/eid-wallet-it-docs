.. include:: ../common/common_definitions.rst

Funzionalità dell'Istanza del Wallet
====================================

Un'Istanza del Wallet DEVE supportare le seguenti funzionalità:

  - Registrazione del Wallet (dettagliata in :ref:`wallet-instance-registration:Inizializzazione e Registrazione dell'Istanza del Wallet`),
  - Emissione dell'Attestato del Wallet (dettagliata in :ref:`wallet-attestation-issuance:Emissione dell'Attestato di Wallet`),
  - Revoca del Wallet (dettagliata in :ref:`wallet-instance-revocation:Revoca dell'Istanza del Wallet`) e
  - Cancellazione degli attributi presentati (dettagliata in :ref:`user-attribute-deletion:Eliminazione degli Attributi dell'Utente`).

Ciascuna funzionalità è descritta in dettaglio nelle sezioni seguenti.

.. note::
  I dettagli forniti di seguito sono non normativi e hanno lo scopo di chiarire le funzionalità della Registrazione dell'Istanza del Wallet. L'implementazione effettiva può variare in base al caso d'uso specifico e ai requisiti del Fornitore di Wallet.

.. toctree::
  :caption: Indice delle Funzionalità dell'Istanza del Wallet
  :maxdepth: 3

  wallet-instance-registration.rst
  wallet-attestation-issuance.rst
  wallet-instance-revocation.rst
  user-attribute-deletion.rst

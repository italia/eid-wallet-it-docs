.. include:: ../common/common_definitions.rst


Emissione di Attestati Elettronici
==================================

Questa sezione descrive il flusso di emissione di un Attestato Elettronico di Dati di Identificazione Personale (PID) e di Attestati Elettronici di Attributi ((Q)EAA) con un elevato livello di sicurezza. Nelle sezioni successive vengono utilizzati i termini Credential Issuer, PID Provider, (Q)EAA Provider per riferirsi rispettivamente a Fornitore di Attestati Elettronici, Fornitore di Attestati Elettronici di Dati di Identificazione Personale e Fornitore di Attestati Elettronici di Attributi.

L'emissione utilizza [`OpenID4VCI`_], profilato da [`OPENID4VC-HAIP`_], come richiesto da [`CIR2024/2982`_], ed è controllata da [`ETSI TS 119 472-3`_].
La Wallet Unit DEVE supportare l'Authorization Code Grant.
Dove [`ETSI TS 119 472-3`_] lo richiede, la Wallet Unit supporta il Pre-Authorized Code Grant.
Ciascun Credential Issuer DEVE supportare l'Authorization Code Grant.
Il Trust Framework applicabile è selezionato come specificato in :ref:`trust-evaluation:Selection at Issuance`.
Un Credential Issuer richiamato attraverso il flusso EUDI Wallet DEVE usare lo schema ``eu-eaa-offer://`` per le Credential Offer, come profilato da [`ETSI TS 119 472-3`_].
L'emissione del PID prima della notifica EUDIW è specificata in :ref:`pid-until-notification`.


.. toctree::
  :caption: Indice dei Contenuti per l'Emissione di Attestati Elettronici
  :maxdepth: 3

  credential-issuance-high-level.rst
  credential-issuance-low-level.rst
  credential-issuance-l2plus.rst



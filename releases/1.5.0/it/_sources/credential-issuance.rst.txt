.. include:: ../common/common_definitions.rst


Emissione di Attestati Elettronici
==================================

Questa sezione descrive il flusso di emissione di un Attestato Elettronico di Dati di Identificazione Personale (PID) e di Attestati Elettronici di Attributi ((Q)EAA) con un elevato livello di sicurezza.
I flussi ad alto livello sono specificati in :ref:`credential-issuance-high-level:Flussi ad Alto Livello per l'Emissione di Attestati Elettronici`.
Nelle sezioni successive, Credential Issuer indica il Fornitore di Attestati Elettronici.
PID Provider indica il Fornitore di Attestati Elettronici di Dati di Identificazione Personale.
(Q)EAA Provider indica il Fornitore di Attestati Elettronici di Attributi.

L'emissione utilizza [`OpenID4VCI`_], profilato da [`OPENID4VC-HAIP`_], come richiesto da [`CIR2024/2982`_], ed è controllata da [`ETSI TS 119 472-3`_].
Il supporto all'Authorization Code Grant è specificato in :ref:`credential-issuance-low-level:Issuance Flow`.
Dove [`ETSI TS 119 472-3`_] lo richiede, la Wallet Unit supporta il Pre-Authorized Code Grant.
Il Trust Framework applicabile è selezionato come specificato in :ref:`trust-evaluation:Selection at Issuance`.
Lo schema per le Credential Offer nel flusso EUDI Wallet è specificato in :ref:`credential-issuance-low-level:Flusso Credential Offer`.
L'emissione del PID prima della notifica EUDIW è specificata in :ref:`pid-until-notification`.


.. toctree::
  :caption: Indice dei Contenuti per l'Emissione di Attestati Elettronici
  :maxdepth: 3

  credential-issuance-high-level.rst
  credential-issuance-low-level.rst
  credential-issuance-l2plus.rst



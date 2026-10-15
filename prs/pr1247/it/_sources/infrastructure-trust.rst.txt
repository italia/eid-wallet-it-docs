.. include:: ../common/common_definitions.rst
.. include:: ../common/symbols.rst
.. Included via index.rst at title level '=' (document title).

Infrastructure of Trust
=======================

Questo capitolo specifica i Trust Artifact, i profili dei certificati e il loro ciclo di vita.
La decisione di trust che usa tali artifact è specificata in :ref:`trust-evaluation:Trust Evaluation Process`.
La registrazione e la pubblicazione delle entità sono specificate in :ref:`onboarding-system:Onboarding System and Lifecycle Management`.

L'ecosistema IT-Wallet opera all'interno di un'infrastruttura di trust federata in cui le entità partecipanti stabiliscono relazioni di trust crittografiche e mantengono la conformità a standard di sicurezza comuni.
Questa infrastruttura fornisce il fondamento per operazioni sicure sugli Attestati Elettronici tra i partecipanti dell'ecosistema.

Nell'IT-Wallet coesistono due Trust Framework.
Il Trust Framework di ciascuna interazione è selezionato come specificato in :ref:`trust-evaluation:Trust Framework Selection`.

  - Il **Trust Framework EUDIW** è definito dal Regolamento eIDAS2 (`EU_2024_1183`_), dai relativi regolamenti di esecuzione e dall'ARF (`EIDAS-ARF`_).
    Una Wallet Unit che implementa solo le procedure EUDIW DEVE poter richiedere, presentare e verificare un PID, una (Q)EAA o una PuB-EAA di un altro Stato membro.
    Tale Wallet Unit DEVE poter autenticare una Wallet-Relying Party di un altro Stato membro.
    I PID Provider, i QEAA Provider e i PuB-EAA Provider DEVONO supportare il Trust Framework EUDIW.
  - Il **Trust Framework Nazionale** è un overlay nazionale basato su OpenID Federation (`OID-FED`_) combinato con una PKI X.509 per gli Attestati Elettronici ancorati a tale framework.
    È **fuori dall'ARF**.
    Fornisce registrazione, onboarding e discovery per le entità che operano nel perimetro nazionale.
    La discovery attraverso il Trust Framework Nazionale PUÒ includere le entità ancorate al Trust Framework EUDIW.
    Tale discovery non sostituisce la registrazione, la notifica o il percorso di trust EUDIW.

Questa sezione fornisce innanzitutto una panoramica delle entità e dei processi coinvolti nell'infrastruttura di trust (:ref:`infrastructure-trust:Overview`).
Definisce quindi il :ref:`infrastructure-trust:X.509 Certificate Profile` generale e i :ref:`infrastructure-trust:Common Trust Artifacts` condivisi da entrambi i framework, seguiti dagli artifact specifici di ciascun framework (:ref:`infrastructure-trust:EUDIW Trust Artifacts` e :ref:`infrastructure-trust:National Trust Artifacts`).
Infine, descrive il relativo ciclo di vita (:ref:`infrastructure-trust:Trust Management and Lifecycle`).

Overview
--------

Per eseguire una trust evaluation, le entità effettuano prima l'onboarding nell'ecosistema (vedere :ref:`onboarding-system:Onboarding System and Lifecycle Management`).
Un Fornitore di EAA non qualificato e una Relying Party dichiarano lì il Trust Framework di ciascun ruolo, come specificato in :ref:`onboarding-system:Registration Profiles`.

L'onboarding e, ove applicabile, la notifica europea rilasciano o aggiornano i Trust Artifact (vedere :ref:`infrastructure-trust:Common Trust Artifacts`, :ref:`infrastructure-trust:EUDIW Trust Artifacts` e :ref:`infrastructure-trust:National Trust Artifacts`).
La trust evaluation usa quindi tali artifact (vedere :ref:`trust-evaluation:Trust Evaluation Process`).


.. include:: trust-pki-architecture.rst
.. include:: x509-certificate-profile.rst
.. include:: trust-artifact-common.rst
.. include:: trust-artifact-eudiw.rst
.. include:: trust-artifact-oidfed.rst
.. include:: trust-management.rst



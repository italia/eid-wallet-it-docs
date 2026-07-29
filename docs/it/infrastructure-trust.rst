.. include:: ../common/common_definitions.rst
.. include:: ../common/symbols.rst
.. Included via index.rst at title level '=' (document title).

Infrastructure of Trust
=======================

L'ecosistema IT-Wallet opera all'interno di un'infrastruttura di trust federata in cui le entità partecipanti stabiliscono relazioni di trust crittografiche e mantengono la conformità a standard di sicurezza comuni.
Questa infrastruttura fornisce le fondamenta per operazioni sicure di Credenziali Digitali tra i partecipanti dell'ecosistema.

Nell'IT-Wallet coesistono due trust framework.

  - Il **EUDIW Trust Framework** è definito dal Regolamento eIDAS2 (`EU_2024_1183`_), dai relativi regolamenti di esecuzione e dall'ARF (`EIDAS-ARF`_).
    È obbligatorio e autorevole per le entità notificate e per l'interoperabilità transfrontaliera.
  - Il **National Trust Framework** si basa su OpenID Federation (`OID-FED`_) combinata con una PKI X.509 dedicata alla firma delle Credenziali Digitali che richiedono X.509.
    È il livello di registrazione e onboarding per tutte le entità dell'ecosistema e fornisce meccanismi di valutazione del trust per le fasi operative in cui il EUDIW Trust Framework non è richiesto.

Questa sezione fornisce innanzitutto una panoramica delle entità e dei processi coinvolti nell'infrastruttura di trust (:ref:`infrastructure-trust:Overview`).
Definisce quindi il profilo generale :ref:`infrastructure-trust:X.509 Certificate Profile` e gli :ref:`infrastructure-trust:Common Trust Artifacts` condivisi da entrambi i framework, seguiti dagli artifact specifici di ciascun framework (:ref:`infrastructure-trust:EUDIW Trust Artifacts` e :ref:`infrastructure-trust:National Trust Artifacts`).
Infine descrive il relativo ciclo di vita (:ref:`infrastructure-trust:Trust Management and Lifecycle`).

Overview
--------

L'ecosistema IT-Wallet opera su un'infrastruttura di trust federata, che richiede alle entità partecipanti di stabilire trust reciproco prima di qualsiasi interazione che coinvolga attributi dell'Utente.
Per poter eseguire un processo di valutazione del trust, le entità devono innanzitutto effettuare l'onboarding nell'ecosistema (vedere :ref:`onboarding-system:Onboarding System and Lifecycle Management`).
Durante questa fase, i Non-Qualified EAA Provider e le Relying Party DEVONO dichiarare se necessitano di interoperare con entità europee oppure se operano solo entro il perimetro nazionale.

Questa scelta influisce sia sulle procedure di onboarding sia su quelle di valutazione del trust.
Se è richiesto solo il perimetro nazionale, l'infrastruttura di trust è conforme al National Trust Framework.
Altrimenti è necessario il EUDIW Trust Framework.

.. note::
    Poiché il Wallet non può sapere in anticipo se sarà usato per interagire con servizi nazionali o europei, DEVONO essere supportati sia il National Trust Framework sia il EUDIW Trust Framework.
    I PID Provider, i QEAA Provider e i PuB-EAA Provider DEVONO supportare il EUDIW Trust Framework, in quanto emettono Credenziali regolate da eIDAS 2.0.

In entrambi i casi, i processi di onboarding e, eventualmente, di notifica europea determinano il rilascio o l'aggiornamento di diversi artifact di trust (dettagliati nelle sezioni :ref:`infrastructure-trust:Common Trust Artifacts`, :ref:`infrastructure-trust:EUDIW Trust Artifacts` e :ref:`infrastructure-trust:National Trust Artifacts`), poi utilizzati durante i processi di valutazione del trust (dettagliati nella sezione :ref:`trust-evaluation:Trust Evaluation Process`).


.. include:: trust-pki-architecture.rst
.. include:: x509-certificate-profile.rst
.. include:: trust-artifact-common.rst
.. include:: trust-artifact-eudiw.rst
.. include:: trust-artifact-oidfed.rst
.. include:: trust-management.rst



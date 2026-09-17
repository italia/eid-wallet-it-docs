.. include:: ../common/common_definitions.rst
.. include:: ../common/symbols.rst
.. Included via index.rst at title level '=' (document title).

Infrastructure of Trust
=======================

L'ecosistema IT-Wallet opera all'interno di un'infrastruttura di trust federata in cui le entità partecipanti stabiliscono relazioni di trust crittografiche e mantengono la conformità a standard di sicurezza comuni.
Questa infrastruttura fornisce il fondamento per operazioni sicure sugli Attestati Elettronici tra i partecipanti dell'ecosistema.

Nell'IT-Wallet coesistono due Trust Framework.

  - Il **Trust Framework EUDIW** è definito dal Regolamento eIDAS2 (`EU_2024_1183`_), dai relativi regolamenti di esecuzione e dall'ARF (`EIDAS-ARF`_).
    È il percorso notificato e interoperabile e DEVE essere autonomo per i PID, le (Q)EAA o le PuB-EAA, e per le Wallet-Relying Party, di altri Stati membri: una Wallet Unit che implementa solo le procedure EUDIW DEVE poter emettere, presentare e verificare tali Attestati, e autenticare tali Wallet-Relying Party.
    È obbligatorio e autorevole per tali Attestati e Wallet-Relying Party di altri Stati membri, e per l'interoperabilità transfrontaliera.
  - Il **Trust Framework Nazionale** è un overlay nazionale basato su OpenID Federation (`OID-FED`_) combinato con una PKI X.509 dedicata alla firma degli Attestati Elettronici che richiedono una PKI X.509.
    È **fuori dall'ARF**. È il livello di registrazione e onboarding per tutte le entità dell'ecosistema.
    OpenID Federation DOVREBBE essere utilizzata da un'entità nazionale che si rivolge esclusivamente a un pubblico nazionale.

Il Trust Framework Nazionale NON DEVE essere selezionato, e NON DEVE essere usato come fallback, per l'emissione o la presentazione di un PID, di una (Q)EAA o di una PuB-EAA di un altro Stato membro.
Una Wallet-Relying Party nazionale che offre servizi di interoperabilità al di fuori del pubblico nazionale DEVE utilizzare il Trust Framework EUDIW, come specificato in :ref:`trust-evaluation:Trust Framework Selection`.

Questa sezione fornisce innanzitutto una panoramica delle entità e dei processi coinvolti nell'infrastruttura di trust (:ref:`infrastructure-trust:Overview`).
Definisce quindi il :ref:`infrastructure-trust:X.509 Certificate Profile` generale e i :ref:`infrastructure-trust:Common Trust Artifacts` condivisi da entrambi i framework, seguiti dagli artifact specifici di ciascun framework (:ref:`infrastructure-trust:EUDIW Trust Artifacts` e :ref:`infrastructure-trust:National Trust Artifacts`).
Infine, descrive il relativo ciclo di vita (:ref:`infrastructure-trust:Trust Management and Lifecycle`).

Overview
--------

L'ecosistema IT-Wallet opera su un'infrastruttura di trust federata, che richiede alle entità partecipanti di stabilire un trust reciproco prima di impegnarsi in qualsiasi interazione che coinvolga attributi dell'Utente.
Per poter eseguire un processo di trust evaluation, le entità devono prima effettuare l'onboarding nell'ecosistema (vedere :ref:`onboarding-system:Onboarding System and Lifecycle Management`).
Durante questa fase, i Fornitori di EAA non qualificati e le Relying Party DEVONO dichiarare se hanno necessità di interoperare con entità europee oppure se operano solo all'interno del perimetro nazionale.

Questa scelta influisce sia sulle procedure di onboarding sia su quelle di trust evaluation, come specificato in :ref:`trust-evaluation:Trust Framework Selection`.
Ad esempio, l'IT-Wallet ID di ambito nazionale è emesso e validato nell'ambito del Trust Framework Nazionale, mentre un PID, una (Q)EAA o una PuB-EAA di un altro Stato membro appartiene al Trust Framework EUDIW (vedere :term:`IT-Wallet ID`).

.. note::
    Poiché il Wallet non può sapere in anticipo se sarà utilizzato per interagire con servizi nazionali o europei, DEVONO essere supportati sia il Trust Framework Nazionale sia il Trust Framework EUDIW.
    I PID Provider, i QEAA Provider e i PuB-EAA Provider DEVONO supportare il Trust Framework EUDIW, in quanto emettono Attestati regolati da eIDAS 2.0, in modo che una Wallet Unit di un altro Stato membro possa interagire con essi.
    L'overlay nazionale NON DEVE ritardare né sostituire il percorso EUDIW specificato sopra.

In entrambi i casi, i processi di onboarding e, ove applicabile, di notifica europea determinano il rilascio o l'aggiornamento dei Trust Artifact (dettagliati nelle sezioni :ref:`infrastructure-trust:Common Trust Artifacts`, :ref:`infrastructure-trust:EUDIW Trust Artifacts` e :ref:`infrastructure-trust:National Trust Artifacts`), quindi utilizzati durante i processi di trust evaluation (dettagliati nella sezione :ref:`trust-evaluation:Trust Evaluation Process`).


.. include:: trust-pki-architecture.rst
.. include:: x509-certificate-profile.rst
.. include:: trust-artifact-common.rst
.. include:: trust-artifact-eudiw.rst
.. include:: trust-artifact-oidfed.rst
.. include:: trust-management.rst



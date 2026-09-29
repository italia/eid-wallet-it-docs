.. include:: ../common/common_definitions.rst


Presentazione dell'Attestato Elettronico
========================================

Questa sezione descrive come un'Istanza di Relying Party richiede a un'Istanza del Wallet la presentazione dell'Attestato Elettronico di Dati di Identificazione Personale/Attestati Elettronici di Attributi.

La presentazione utilizza [`OpenID4VP`_] per il flusso remoto, profilato da [`OPENID4VC-HAIP`_], e [`ISO18013-5`_] per il flusso di prossimità, come richiesto da [`CIR2024/2982`_].
Il Trust Framework applicabile è selezionato come specificato in :ref:`trust-evaluation:Selection at Presentation`.
Un'Istanza del Wallet che implementa solo le procedure EUDIW DEVE poter presentare un PID, una (Q)EAA o una PuB-EAA a una Wallet-Relying Party di un altro Stato membro, come specificato in :ref:`infrastructure-trust:Infrastructure of Trust`.
La presentazione del PID prima della notifica EUDIW è specificata in :ref:`pid-until-notification`.

Quando una Embedded Disclosure Policy è memorizzata con un Attestato Elettronico, la Wallet Unit DEVE applicarla prima della disclosure, come specificato in :ref:`infrastructure-trust:Embedded Disclosure Policy (EDP)`.

In questa sezione vengono descritti i seguenti flussi:

- :ref:`remote-flow:Flusso Remoto`, dove l'Utente presenta un Attestato Elettronico a un'Istanza di Relying Party web secondo `OpenID4VP`_. In questo scenario, l'user-agent e l'Istanza del Wallet possono essere utilizzati nello stesso dispositivo (**Same Device Flow**), o in dispositivi diversi (**Cross Device Flow**).
- :ref:`proximity-flow:Flusso di Prossimità`, dove l'Utente presenta un Attestato Elettronico a un'Istanza di Relying Party mobile secondo `ISO18013-5`_. L'Utente interagisce con un Verificatore di Attestati Elettronici utilizzando tecnologie di connessione di prossimità come i Codici QR e il Bluetooth Low Energy (BLE).

.. note::
  In caso di utilizzo di credenziali ottenute in batch, l'Istanza del Wallet DOVREBBE implementare una logica di selezione delle Credenziali (ad esempio, basata sulla prima in scadenza) e DEVE contrassegnarla come consumata. Al termine del flusso, DEVE ridurre il numero di credenziali disponibili nel batch e, in base a ciò, può verificare se è il momento di richiedere un nuovo batch di credenziali.


.. toctree::
  :caption: Indice dei Contenuti della Presentazione della Credenziale
  :maxdepth: 3

  remote-flow.rst
  proximity-flow.rst



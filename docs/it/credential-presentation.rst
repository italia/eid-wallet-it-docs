.. include:: ../common/common_definitions.rst


Presentazione dell'Attestato Elettronico
========================================

Questa sezione descrive come un'Istanza di Relying Party richiede a un'Istanza del Wallet la presentazione del PID e degli Attestati Elettronici di Attributi.

Il flusso remoto utilizza [`OpenID4VP`_], profilato da [`OPENID4VC-HAIP`_]. Il flusso di prossimità utilizza [`ISO18013-5`_]. [`CIR2024/2982`_] richiede entrambi i flussi.
Il Trust Framework applicabile è selezionato come specificato in :ref:`trust-evaluation:Selection at Presentation`.
La presentazione del PID prima della notifica EUDIW è specificata in :ref:`pid-until-notification`.
Quando una Embedded Disclosure Policy è memorizzata con un Attestato Elettronico, la Wallet Unit la applica prima della disclosure, come specificato in :ref:`infrastructure-trust:Embedded Disclosure Policy (EDP)`.

In questa sezione vengono descritti i seguenti flussi:

- :ref:`remote-flow:Flusso Remoto`, dove l'Utente presenta un Attestato Elettronico a un'Istanza di Relying Party web. L'user-agent e l'Istanza del Wallet possono essere sullo stesso dispositivo (**Same Device Flow**) o su dispositivi diversi (**Cross Device Flow**).
- :ref:`proximity-flow:Flusso di Prossimità`, dove l'Utente presenta un Attestato Elettronico a un'Istanza di Relying Party mobile. L'Utente interagisce con un Verificatore di Attestati Elettronici utilizzando tecnologie di prossimità come i Codici QR e il Bluetooth Low Energy (BLE).

L'identity matching, dopo la verifica crittografica di un Attestato Elettronico presentato, è specificato in :ref:`identity-matching`. L'identity matching non è un flusso di presentazione.
La presentazione offline e la sede delle chiavi private vincolate sono specificate in :ref:`wallet-solution-requirements:Requisiti del Keystore`.

.. toctree::
  :caption: Indice dei Contenuti della Presentazione della Credenziale
  :maxdepth: 3

  remote-flow.rst
  proximity-flow.rst
  identity-matching.rst



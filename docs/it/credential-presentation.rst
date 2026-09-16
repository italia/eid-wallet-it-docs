.. include:: ../common/common_definitions.rst


Presentazione dell'Attestato Elettronico
========================================

Questa sezione descrive come un'Istanza di Relying Party richiede a un'Istanza del Wallet la presentazione dell'Attestato Elettronico di Dati di Identificazione Personale/Attestati Elettronici di Attributi.

In questa sezione vengono descritti i seguenti flussi:

- :ref:`remote-flow:Flusso Remoto`, dove l'Utente presenta un Attestato Elettronico a un'Istanza di Relying Party web secondo `OpenID4VP`_. In questo scenario, l'user-agent e l'Istanza del Wallet possono essere utilizzati nello stesso dispositivo (**Same Device Flow**), o in dispositivi diversi (**Cross Device Flow**).
- :ref:`proximity-flow:Flusso di Prossimità`, dove l'Utente presenta un Attestato Elettronico a un'Istanza di Relying Party mobile secondo `ISO18013-5`_. L'Utente interagisce con un Verificatore di Attestati Elettronici utilizzando tecnologie di connessione di prossimità come i Codici QR e il Bluetooth Low Energy (BLE).

La presentazione in prossimità o comunque offline di un Attestato Elettronico DEVE riuscire solo quando le chiavi private vincolate sono memorizzate in un Keystore locale o in un WSCD locale. Gli Attestati Elettronici le cui chiavi private vincolate sono memorizzate in un WSCD remoto NON DEVONO essere presentati offline (:ref:`WP_160 <wallet-instance-testcases>`).

.. note::
  In caso di utilizzo di credenziali ottenute in batch, l'Istanza del Wallet DOVREBBE implementare una logica di selezione delle Credenziali (ad esempio, basata sulla prima in scadenza) e DEVE contrassegnarla come consumata. Al termine del flusso, DEVE ridurre il numero di credenziali disponibili nel batch e, in base a ciò, può verificare se è il momento di richiedere un nuovo batch di credenziali.


.. toctree::
  :caption: Indice dei Contenuti della Presentazione della Credenziale
  :maxdepth: 3

  remote-flow.rst
  proximity-flow.rst



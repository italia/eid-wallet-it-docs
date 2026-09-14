.. include:: ../common/common_definitions.rst


Presentazione dell'Attestato Elettronico
========================================

Questa sezione descrive come un'Istanza di Relying Party richiede a un'Istanza del Wallet la presentazione dell'Attestato Elettronico di Dati di Identificazione Personale/Attestati Elettronici di Attributi.

In questa sezione vengono descritti i seguenti flussi:

- :ref:`remote-flow:Flusso Remoto`, dove l'Utente presenta un Attestato Elettronico a un'Istanza di Relying Party web secondo `OpenID4VP`_. In questo scenario, l'user-agent e l'Istanza del Wallet possono essere utilizzati nello stesso dispositivo (**Same Device Flow**), o in dispositivi diversi (**Cross Device Flow**).
- :ref:`proximity-flow:Flusso di Prossimità`, dove l'Utente presenta un Attestato Elettronico a un'Istanza di Relying Party mobile secondo `ISO18013-5`_. L'Utente interagisce con un Verificatore di Attestati Elettronici utilizzando tecnologie di connessione di prossimità come i Codici QR e il Bluetooth Low Energy (BLE).

.. note::
  Quando una Relying Party deve autenticare l'Utente distinguendo se è maggiorenne o minorenne, DEVE utilizzare una delle seguenti opzioni. In entrambi i casi il claim corrispondente DEVE essere incluso nella richiesta di presentazione:

  1. **Data di nascita dal PID o dall'IT-Wallet ID.** La Relying Party DEVE richiedere la data di nascita nell'ambito della presentazione del PID o dell'IT-Wallet ID (``birthdate`` in formato SD-JWT VC, ``birth_date`` in formato mdoc-CBOR). Vedere :ref:`credential-data-model-pid:Modello di Dati del PID` e :ref:`credential-data-model-it-wallet-id:Modello di Dati dell'IT-Wallet ID`.

  2. **``age_over_18`` dall'Attestazione di Età.** La Relying Party DEVE richiedere il claim ``age_over_18`` nell'ambito della presentazione dell'Attestazione di Età. L'Attestazione di Età è l'Attestato Elettronico pubblicato nel :ref:`registry:Catalogo degli Attestati Elettronici` con ``credential_type`` ``av``. Il relativo modello dati è definito dallo schema corrispondente nel :ref:`registry:Registro degli Schema` (formato mdoc-CBOR, ``docType`` ``eu.europa.ec.av.1``). Il claim ``age_over_18``, nel namespace ``eu.europa.ec.av.1``, attesta se l'Utente ha compiuto 18 anni senza divulgare la data di nascita.

.. note::
  In caso di utilizzo di credenziali ottenute in batch, l'Istanza del Wallet DOVREBBE implementare una logica di selezione delle Credenziali (ad esempio, basata sulla prima in scadenza) e DEVE contrassegnarla come consumata. Al termine del flusso, DEVE ridurre il numero di credenziali disponibili nel batch e, in base a ciò, può verificare se è il momento di richiedere un nuovo batch di credenziali.


.. toctree::
  :caption: Indice dei Contenuti della Presentazione della Credenziale
  :maxdepth: 3

  remote-flow.rst
  proximity-flow.rst



.. include:: ../common/common_definitions.rst


Presentazione dell'Attestato Elettronico
========================================

Questa sezione descrive come un'Istanza di Relying Party richiede a un'Istanza del Wallet la presentazione dell'Attestato Elettronico di Dati di Identificazione Personale/Attestati Elettronici di Attributi.

In questa sezione vengono descritti i seguenti flussi:

- :ref:`remote-flow:Flusso Remoto`, dove l'Utente presenta un Attestato Elettronico a un'Istanza di Relying Party web secondo `OpenID4VP`_. In questo scenario, l'user-agent e l'Istanza del Wallet possono essere utilizzati nello stesso dispositivo (**Same Device Flow**), o in dispositivi diversi (**Cross Device Flow**).
- :ref:`proximity-flow:Flusso di Prossimità`, dove l'Utente presenta un Attestato Elettronico a un'Istanza di Relying Party mobile secondo `ISO18013-5`_. L'Utente interagisce con un Verificatore di Attestati Elettronici utilizzando tecnologie di connessione di prossimità come i Codici QR e il Bluetooth Low Energy (BLE).

.. note::
  Quando una Relying Party deve distinguere l'Utente in fase di autenticazione, DEVE farlo sulla base delle informazioni contenute negli Attestati Elettronici richiesti nella richiesta di presentazione. I claim corrispondenti devono essere inclusi nella richiesta di presentazione. La Relying Party distingue l'Utente valutando i valori dei claim effettivamente presentati.

  Di seguito sono riportati esempi non normativi.

  1. **PID o IT-Wallet ID.** La Relying Party richiede i claim di identificazione previsti dal relativo modello dati, ad esempio ``given_name``, ``family_name`` e ``personal_administrative_number`` per il PID, oppure ``tax_id_code`` per l'IT-Wallet ID. Vedere :ref:`credential-data-model-pid:Modello di Dati del PID` e :ref:`credential-data-model-it-wallet-id:Modello di Dati dell'IT-Wallet ID`.

     Esempio di ``dcql_query`` nel flusso remoto (PID in formato SD-JWT VC):

     .. code-block:: json

       {
         "credentials": [
           {
             "id": "pid",
             "format": "dc+sd-jwt",
             "meta": {
               "vct_values": [ "urn:eudi:pid:it:1" ]
             },
             "claims": [
               {"path": ["given_name"]},
               {"path": ["family_name"]},
               {"path": ["personal_administrative_number"]}
             ]
           }
         ]
       }

     Gli stessi claim, nel flusso di prossimità, sono richiesti nell'``ItemsRequest`` mdoc:

     .. code-block:: json

       {
         "docType": "eu.europa.ec.eudi.pid.1",
         "nameSpaces": {
           "eu.europa.ec.eudi.pid.1": {
             "given_name": false,
             "family_name": false,
             "personal_administrative_number": false
           }
         }
       }

  2. **Altro Attestato Elettronico di catalogo.** La Relying Party richiede i claim previsti dallo schema dell'Attestato Elettronico pubblicato nel :ref:`registry:Catalogo degli Attestati Elettronici`. Il relativo modello dati è definito dallo schema corrispondente nel :ref:`registry:Registro degli Schema`.

     Esempio di ``dcql_query`` nel flusso remoto per una mDL (``credential_type`` ``mDL``, formato mdoc-CBOR, ``docType`` ``org.iso.18013.5.1.mDL``):

     .. code-block:: json

       {
         "credentials": [
           {
             "id": "mobile driving license",
             "format": "mso_mdoc",
             "meta": {
               "doctype_value": "org.iso.18013.5.1.mDL"
             },
             "claims": [
               {"path": ["org.iso.18013.5.1", "given_name"]},
               {"path": ["org.iso.18013.5.1", "family_name"]},
               {"path": ["org.iso.18013.5.1", "document_number"]}
             ]
           }
         ]
       }

.. note::
  In caso di utilizzo di credenziali ottenute in batch, l'Istanza del Wallet DOVREBBE implementare una logica di selezione delle Credenziali (ad esempio, basata sulla prima in scadenza) e DEVE contrassegnarla come consumata. Al termine del flusso, DEVE ridurre il numero di credenziali disponibili nel batch e, in base a ciò, può verificare se è il momento di richiedere un nuovo batch di credenziali.


.. toctree::
  :caption: Indice dei Contenuti della Presentazione della Credenziale
  :maxdepth: 3

  remote-flow.rst
  proximity-flow.rst



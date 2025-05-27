.. include:: ../common/common_definitions.rst


Configurazione dell'Entità Relying Party
----------------------------------------

Secondo la Sezione :ref:`trust:Configurazione della Federazione`, come Entità di Federazione, la Relying Party è tenuta a mantenere un endpoint well-known che ospita la sua Configurazione di Entità.
La Configurazione di Entità delle Relying Party DEVE contenere i parametri definiti nelle Sezioni :ref:`trust:Entity Configuration Foglie e Intermediari` e :ref:`trust:Parametri Comuni delle Entity Configuration`.

Le Relying Party DEVONO fornire i seguenti tipi di metadati:

  - `federation_entity`
  - `openid_credential_verifier`

I metadati *federation_entity* DEVONO contenere i claim come definito nella Sezione :ref:`trust:Metadati delle Foglie federation_entity`.


Esempio di Configurazione di Entità di una Relying Party
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Di seguito un esempio non normativo della richiesta effettuata dall'Istanza del Wallet all'endpoint well-known *openid-federation* per ottenere la Configurazione di Entità della Relying Party:

.. code-block:: http

  GET /.well-known/openid-federation HTTP/1.1
  HOST: relying-party.example.org


Di seguito un esempio non normativo di risposta:

.. literalinclude:: ../../examples/ec-rp.json
  :language: JSON

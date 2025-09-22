.. include:: ../common/common_definitions.rst


Entity Configuration Relying Party
----------------------------------

Secondo la Sezione :ref:`trust:Configurazione della Federazione`, come Entità di Federazione, la Relying Party è tenuta a mantenere un endpoint well-known che ospita la sua Entity Configuration.
L'Entity Configuration delle Relying Party DEVE contenere i parametri definiti nelle Sezioni :ref:`trust:Entity Configuration Foglie e Intermediari` e :ref:`trust:Parametri Comuni delle Entity Configuration` (:ref:`test-plans-remote-presentation:RPR-01`, :ref:`test-plans-remote-presentation:RPR-02`, :ref:`test-plans-remote-presentation:RPR-03`, :ref:`test-plans-remote-presentation:RPR-04`, :ref:`test-plans-remote-presentation:RPR-05`, :ref:`test-plans-remote-presentation:RPR-06`).

Le Relying Party DEVONO fornire i seguenti tipi di metadata (:ref:`test-plans-remote-presentation:RPR-01`, :ref:`test-plans-remote-presentation:RPR-02`, :ref:`test-plans-remote-presentation:RPR-03`, :ref:`test-plans-remote-presentation:RPR-04`, :ref:`test-plans-remote-presentation:RPR-05`, :ref:`test-plans-remote-presentation:RPR-06`):

  - ``federation_entity``
  - ``openid_credential_verifier``

I metadata contenuti in ``federation_entity`` DEVONO contenere i claim come definito nella Sezione :ref:`trust:Metadati delle Foglie federation_entity` (:ref:`test-plans-remote-presentation:RPR-01`, :ref:`test-plans-remote-presentation:RPR-02`, :ref:`test-plans-remote-presentation:RPR-03`, :ref:`test-plans-remote-presentation:RPR-04`, :ref:`test-plans-remote-presentation:RPR-05`, :ref:`test-plans-remote-presentation:RPR-06`).


Entity Configuration di una Relying Party
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Di seguito un esempio non normativo della richiesta effettuata dall'Istanza del Wallet all'endpoint well-known ``openid-federation`` per ottenere l'Entity Configuration della Relying Party:

.. code-block:: http

  GET /.well-known/openid-federation HTTP/1.1
  HOST: relying-party.example.org


Di seguito un esempio non normativo di risposta:

.. literalinclude:: ../../examples/ec-rp.json
  :language: JSON

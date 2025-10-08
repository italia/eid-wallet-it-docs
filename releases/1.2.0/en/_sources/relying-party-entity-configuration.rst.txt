.. include:: ../common/common_definitions.rst


Relying Party Entity Configuration
------------------------------------------

According to Section :ref:`trust:Configuration of the Federation`, as a Federation Entity, the Relying Party is required to maintain a well-known endpoint that hosts its Entity Configuration.
The Entity Configuration of Relying Parties MUST contain the parameters defined in the Sections :ref:`trust:Entity Configuration Leaves and Intermediates` and :ref:`trust:Entity Configurations Common Parameters`.

The Relying Parties MUST provide the following metadata types:

  - `federation_entity`
  - `openid_credential_verifier`

The *federation_entity* metadata MUST contain the claims as defined in Section :ref:`trust:Metadata of federation_entity Leaves`.


Example of a Relying Party Entity Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Below a non-normative example of the request made by the Wallet Instance to the *openid-federation* well-known endpoint to obtain the Relying Party Entity Configuration:

.. code-block:: http

  GET /.well-known/openid-federation HTTP/1.1
  HOST: relying-party.example.org


Below is a non-normative response example:

.. literalinclude:: ../../examples/ec-rp.json
  :language: JSON


.. include:: ../common/common_definitions.rst


Entity Configuration del Fornitore di Attestati Elettronici
------------------------------------------------------------

I Fornitori di Attestati Elettronici, in quanto Entità di Federazione, DEVONO rispettare le linee guida delineate nella Sezione :ref:`trust:Configurazione della Federazione`. In particolare, DEVONO fornire un endpoint *well-known* che ospiti la loro Entity Configuration.
Quest'ultima DEVE contenere i parametri definiti nelle Sezioni :ref:`trust:Entity Configuration Foglie e Intermediari` e :ref:`trust:Parametri Comuni delle Entity Configuration`.

I Fornitori di Attestati Elettronici DEVONO fornire i seguenti Metadata:

- `federation_entity`
- `oauth_authorization_server`
- `openid_credential_issuer`

Nei casi in cui i Fornitori di Attestati Elettronici di Attributi autenticano gli Utenti utilizzando la loro Istanza del Wallet, allora i Metadata per *openid_credential_verifier* DEVONO essere forniti in aggiunta ai Metadata sopra indicati. Nel caso in cui uno schema nazionale di Identità Digitale sia utilizzato dal Fornitore di Attestati Elettronici di Dati di Identificazione Personale per l'autenticazione dell'Utente, essi POSSONO includere i Metadata per *openid_relying_party* all'interno della loro Configurazione dell'Entità. I Metadata *openid_relying_party* DEVONO essere conformi alle Regole Tecniche `SPID/CIE-OpenID-Connect-Specifications`_.


I Metadata *federation_entity* DEVONO contenere i parametri come definiti nella Sezione :ref:`trust:Metadati delle Foglie federation_entity`.

I Metadata *openid_credential_verifier* DEVONO contenere i parametri come definiti nella Sezione :ref:`relying-party-entity-configuration:Configurazione dell'Entità Relying Party`.

Esempio di Entity Configuration di un Fornitore di Attestati Elettronici di Attributi
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Di seguito è riportato un esempio non normativo di una Entity Configuration di un Fornitore di Attestati Elettronici di Attributi contenente Metadata per:

- `federation_entity`
- `oauth_authorization_server`
- `openid_credential_issuer`
- `openid_credential_verifier`

.. literalinclude:: ../../examples/ec-eaa.json
  :language: JSON

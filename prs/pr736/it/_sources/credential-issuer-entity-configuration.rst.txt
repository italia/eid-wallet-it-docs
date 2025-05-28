.. include:: ../common/common_definitions.rst


Configurazione dell'Entità Fornitore di Credenziale
---------------------------------------------------

I Fornitori di Credenziale, in quanto Entità di Federazione, sono tenuti a rispettare le linee guida delineate nella Sezione :ref:`trust:Configurazione della Federazione`. In particolare, DEVONO fornire un endpoint well-known che ospiti la loro Configurazione dell'Entità.
La Configurazione dell'Entità dei Fornitori di Credenziale DEVE contenere i parametri definiti nelle Sezioni :ref:`trust:Entity Configuration Foglie e Intermediari` e :ref:`trust:Parametri Comuni delle Entity Configuration`.

I Fornitori di Credenziale DEVONO fornire i seguenti tipi di metadati:

- `federation_entity`
- `oauth_authorization_server`
- `openid_credential_issuer`

Nei casi in cui i Fornitori di Attestati Elettronici di Attributi (Qualificati) autenticano gli Utenti utilizzando la loro Istanza del Wallet, i metadati per *openid_credential_verifier* DEVONO essere forniti in aggiunta ai metadati sopra indicati. Nel caso in cui uno schema nazionale di eID sia utilizzato dai Fornitori di Credenziale per l'autenticazione dell'Utente, essi POSSONO includere i metadati per *openid_relying_party* all'interno della loro Configurazione dell'Entità. I metadati *openid_relying_party* DEVONO essere conformi alla versione corrente delle `SPID/CIE-OpenID-Connect-Specifications`_.


I metadati *federation_entity* DEVONO contenere i parametri come definiti nella Sezione :ref:`trust:Metadati delle Foglie federation_entity`.

I metadati *openid_credential_verifier* DEVONO contenere i parametri come definiti nella Sezione :ref:`relying-party-entity-configuration:Configurazione dell'Entità Relying Party`.

Esempio di Configurazione dell'Entità di un Fornitore di Attestati Elettronici di Attributi (Qualificati)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Di seguito è riportato un esempio non normativo di una Configurazione dell'Entità di un Fornitore di Attestati Elettronici di Attributi (Qualificati) contenente metadati per:

- `federation_entity`
- `oauth_authorization_server`
- `openid_credential_issuer`
- `openid_credential_verifier`

.. literalinclude:: ../../examples/ec-eaa.json
  :language: JSON

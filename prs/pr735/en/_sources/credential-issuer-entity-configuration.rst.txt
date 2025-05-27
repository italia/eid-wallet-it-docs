.. include:: ../common/common_definitions.rst


Credential Issuer Entity Configuration
--------------------------------------

The Credential Issuers, as Federation Entity, are required to adhere to the guidelines outlined in Section :ref:`trust:Configuration of the Federation`. Specifically, they MUST provide a well-known endpoint that hosts their Entity Configuration.
The Entity Configuration of Credential Issuers MUST contain the parameters defined in the Sections :ref:`trust:Entity Configuration Leaves and Intermediates` and :ref:`trust:Entity Configurations Common Parameters`.

The Credential Issuers MUST provide the following metadata types:

- `federation_entity`
- `oauth_authorization_server`
- `openid_credential_issuer`

In cases where the (Q)EAA Providers authenticate Users using their Wallet Instance, then the metadata for *openid_credential_verifier* MUST be provided in addition to the metadata above. In case a national eID scheme is used by the Credential Issuers for the User authentication, they MAY include a metadata for *openid_relying_party* within their Entity Configuration. The *openid_relying_party* metadata MUST be compliant with the current version of `SPID/CIE-OpenID-Connect-Specifications`_.


The *federation_entity* metadata MUST contain the parameters as defined in Section :ref:`trust:Metadata of federation_entity Leaves`.

The *openid_credential_verifier* metadata MUST contain the parameters as defined in Section :ref:`relying-party-entity-configuration:Relying Party Entity Configuration`.

Example of a (Q)EAA Provider Entity Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Below is a non-normative example of an Entity Configuration of a (Q)EAA Provider containing a metadata for

- `federation_entity`
- `oauth_authorization_server`
- `openid_credential_issuer`
- `openid_credential_verifier`

.. literalinclude:: ../../examples/ec-eaa.json
  :language: JSON


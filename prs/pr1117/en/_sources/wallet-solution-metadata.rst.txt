.. include:: ../common/common_definitions.rst

Wallet Solution Metadata
------------------------

The metadata JSON Object whose key is ``wallet_solution`` contains the following parameters. The public keys found in this object are exclusively used for signing and/or encryption operations required by this Entity when acting as a component of the Wallet Provider (e.g., sign the Wallet Attestations to the Wallet Instance).

.. list-table::
    :class: longtable
    :widths: 30 70
    :header-rows: 1

    * - **Key**
      - **Value**
    * - ``jwks``
      - CONDITIONAL. JSON Web Key Set document, passed by value, containing the Entity's keys for that Entity Type. It MUST be present if ``jwks_uri`` and ``signed_jwks_uri`` are absent.
    * - ``jwks_uri``
      - CONDITIONAL. URL referencing a JWK Set document containing the Wallet Solution's keys for that Entity Type. This URL MUST use the https scheme. It MUST be present if ``jwks`` and ``signed_jwks_uri`` are absent.
    * - ``signed_jwks_uri``
      - CONDITIONAL. URL referencing a signed JWT having the Entity's JWK Set document for that Entity Type as its payload. This URL MUST use the https scheme. The JWT MUST be signed using a Federation Entity Key. A successful response from the URL MUST use the HTTP status code 200 with the Content Type ``application/jwk-set+jwt``. It MUST be present if ``jwks`` and ``jwks_uri`` are absent.
    * - ``logo_uri``
      - REQUIRED. URL of the entity's logo that will be shown to the User. The logo mime type MUST be ``application/svg``.
    * - ``wallet_metadata``
      - REQUIRED. It contains the Wallet Metadata parameters as defined in :ref:`Table of Wallet Metadata Parameters <table_wallet_metadata_parameters>` and the following two parameters
        
         - ``credential_offer_endpoint`` Credential Offer Endpoint of a Wallet.
         - ``wallet_name`` String containing a human-readable name of the Wallet. 


.. note::
  There are Digital Credential flows that require retrieving Wallet Solution metadata before interacting with the Wallet itself. The flow is described in :ref:`wallet-metadata-retrieval:Wallet Metadata Retrieval Flow`.

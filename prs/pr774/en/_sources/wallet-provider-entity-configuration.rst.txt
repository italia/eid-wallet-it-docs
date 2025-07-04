.. include:: ../common/common_definitions.rst

Wallet Provider Entity Configuration
--------------------------------------

An HTTP GET request to the Federation endpoint allows the retrieval of the Wallet Provider Entity Configuration.

The returned Entity Configuration of the Wallet Provider MUST contain the attributes described in the sections below.

The Wallet Provider Entity Configuration is a signed JWT containing the public keys and supported algorithms of the Wallet Provider. It is structured in accordance with the `OID-FED`_ and the :ref:`trust:The Infrastructure of Trust` outlined in this specification.

Wallet Provider Entity Configuration JWT Header
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Key**
      - **Value**
      - **Reference**
    * - alg
      - Algorithm used to verify the token signature. It MUST be one of the possible values indicated in :ref:`algorithms:Cryptographic Algorithms` (e.g., ES256).
      - `OID-FED`_.
    * - kid
      - Thumbprint of the public key used for the signature.
      - `OID-FED`_ and :rfc:`7638`.
    * - typ
      - Media type, set to ``entity-statement+jwt``.
      - `OID-FED`_.

Wallet Provider Entity Configuration JWT Payload
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Key**
      - **Value**
      - **Reference**
    * - ``iss``
      - REQUIRED. Public URL of the Wallet Provider.
      - `OID-FED`_.
    * - ``sub``
      - REQUIRED. Public URL of the Wallet Provider.
      - `OID-FED`_.
    * - ``iat``
      - REQUIRED. Issuance datetime in Unix Timestamp format.
      - `OID-FED`_.
    * - ``exp``
      - REQUIRED. Expiration datetime in Unix Timestamp format.
      - `OID-FED`_.
    * - ``authority_hints``
      - REQUIRED. Array of URLs (String) containing the list of URLs of the immediate superior Entities, such as the Trust Anchor or an Intermediate, that MAY issue an Entity Statement related to the Wallet Provider.
      - `OID-FED`_.
    * - ``jwks``
      - REQUIRED. A JSON Web Key Set (JWKS) representing the public part of the Wallet Provider's Federation Entity signing keys. The corresponding private key is used by the Entity to sign the Entity Configuration about itself.
      - :rfc:`7517`, `OID-FED`_.
    * - ``metadata``
      - REQUIRED.JSON object that represents the Entity's Types and the metadata for those Entity Types. Each member name of the JSON object is an Entity Type Identifier, and each value MUST be a JSON object containing metadata parameters according to the metadata schema of the Entity Type. It MUST contains the ``wallet_provider`` and OPTIONALLY the ``federation_entity`` metadata.
      - `OID-FED`_.

.. include:: ../common/common_definitions.rst

Entity Configuration of Relying Parties
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

According to Section :ref:`Configuration of the Federation`, as a Federation Entity, the Relying Party is required to maintain a well-known endpoint that hosts its Entity Configuration.
The Entity Configuration of Relying Parties MUST contain the parameters defined in the Sections :ref:`Entity Configuration Leaves and Intermediates` and :ref:`Entity Configurations Common Parameters`. 

The Relying Parties MUST provide the following metadata types:

  - `federation_entity`
  - `openid_credential_verifier`

The *federation_entity* metadata MUST contain the claims as defined in Section :ref:`Metadata of federation_entity Leaves`.

Metadata for openid_credential_verifier
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The *openid_credential_verifier* metadata MUST contain the following parameters.

.. list-table:: 
  :widths: 20 60
  :header-rows: 1

  * - **Claim**
    - **Description**
  * - **client_id**
    - It MUST contain an HTTPS URL that uniquely identifies the RP. See :rfc:`7591#section-3.2.1` and `OpenID Connect Dynamic Client Registration 1.0 <https://openid.net/specs/openid-connect-registration-1_0.html>`_ Section 3.2. 
  * - **client_name**
    - Human-readable string name of the RP. See :rfc:`7591#section-2`. 
  * - **application_type**
    - String indicating the type of application. It MUST be set to "*web*" value. See `OpenID Connect Dynamic Client Registration 1.0 <https://openid.net/specs/openid-connect-registration-1_0.html>`_ Section 2. 
  * - **request_uris**
    - JSON Array of *request_uri* values that are pre-registered by the RP. These URLs MUST use the *https* scheme. See `OpenID Connect Dynamic Client Registration 1.0 <https://openid.net/specs/openid-connect-registration-1_0.html>`_ Section 2.
  * - **response_uris**
    - JSON Array of response URI strings to which the Wallet Instance MUST send the Authorization Response using an HTTP POST request as defined by the Response Mode ``direct_post`` and ``direct_post.jwt`` (see `OpenID4VP`_ Draft 20 Sections 6.2 and 6.3).
  * - **authorization_signed_response_alg**
    - String representing the signing [:rfc:`7515`] *alg* algorithm that MUST be used for signing authorization responses. The algorithm "*none*" MUST NOT be used. See `JARM`_.
  * - **authorization_encrypted_response_alg**
    - Algorithm used to encrypt the authorization response. It specifies to the Wallet Instance the asymmetric encryption algorithm. See `JARM`_.
  * - **authorization_encrypted_response_enc**
    - Encryption algorithm used for the authorization response. It specifies to the Wallet Instance the symmetric encryption algorithm. See `JARM`_.
  * - **vp_formats**
    - JSON object defining the formats and proof types of Verifiable Presentations and Verifiable Credentials the RP supports. It consists of a list of name/value pairs, where each name uniquely identifies a supported type. The RP MUST support at least "*dc+sd-jwt*". The value associated with each name/value pair MUST be a JSON object "**sd-jwt_alg_values**" that MUST contain a JSON array containing identifiers of cryptographic algorithms the RP supports for protection of a SD-JWT. The *alg* JOSE header (as defined in :rfc:`7515`) of the presented SD-JWT MUST match one of the array values. See also `OpenID4VP`_ Draft 20 Section 9.1.
  * - **jwks**
    - JSON Web Key Set document, passed by value, containing the protocol specific keys for the Relying Party. See `JARM`_ Section 3, `OID-FED`_ Draft 41 Section 5.2.1 and `JWK`_.
.. note::
    The parameter **response_uris** is introduced in this specification. 

Example of a Relying Party Entity Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Below a non-normative example of the request made by the Wallet Instance to the *openid-federation* well-known endpoint to obtain the Relying Party Entity Configuration:

.. code-block:: http

  GET /.well-known/openid-federation HTTP/1.1
  HOST: relying-party.example.org


Below is a non-normative response example:

.. literalinclude:: ../../examples/ec-rp.json
  :language: JSON


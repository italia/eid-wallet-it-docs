.. include:: ../common/common_definitions.rst
.. Included via endpoints.rst at title level '-' (level 1).

.. role:: raw-html(raw)
  :format: html

Credential Issuer Endpoints
---------------------------

Metadata Endpoints
^^^^^^^^^^^^^^^^^^^^

The Credential Issuers MUST provide an Entity Configuration through the ``/.well-known/openid-federation`` endpoint, according to Section :ref:`infrastructure-trust:Entity Configuration`. Technical details are provided in Section :ref:`credential-issuer-entity-configuration:Credential Issuer Entity Configuration`.

Alternatively the Credential Issuer's Metadata can be retrieved using the Credential Issuer Identifier. The Metadata document MUST be made available in JSON and JWT format through the ``/.well-known/openid-credential-issuer`` endpoint as defined in Section 12.2.2 of `OpenID4VCI`_.

The ``Accept-Language`` header in the HTTP GET request can be used to indicate the language(s) preferred.
In this case the Credential Issuer can send a subset of the metadata containing internationalized display data for one or all of the requested languages and indicate returned languages using the HTTP ``Content-Language`` Header.

Below is a non-normative example.

.. literalinclude:: ../../examples/shared/credential-issuer-endpoint-1.http
   :language: http

.. literalinclude:: ../../examples/shared/credential-issuer-endpoint-2.http
   :language: http

The Credential Issuer MUST respond with HTTP Status Code 200 and return the Credential Issuer Metadata containing:

- the parameters defined in :ref:`credential-issuer-metadata:Metadata for openid_credential_issuer` as an unsigned JSON document using the media type *application/json*.

          or

- the header and payload parameters defined in Section 12.2.3 of `OpenID4VCI`_ in addition to those defined in :ref:`credential-issuer-metadata:Metadata for openid_credential_issuer` as a signed JSON Web Token using the media type *application/jwt*.

On the EUDIW path the Wallet Unit obtains the Credential Issuer Metadata as that signed JSON Web Token. The media type is *application/jwt*. The unsigned JSON document remains available at the same endpoint. The unsigned JSON document is not the artifact authenticated in :ref:`trust-evaluation:Metadata Validation`.

On the wire the EUDIW document is one signed JSON Web Token. Below is a non-normative example of its protected header and payload. The ``x5c`` chain starts with the access certificate. The trust anchor is absent. The ``registration_cert`` value is the compact serialization of the WRPRC example in :ref:`infrastructure-trust:Wallet-Relying Party Registration Certificate (WRPRC) Profile`.

.. literalinclude:: ../../examples/credential-issuer-metadata-header.json
   :language: json

.. literalinclude:: ../../examples/credential-issuer-metadata-payload.json
   :language: json

The ``authorization_servers`` entries of the Credential Issuer Metadata can be used to obtain the Authorization Server metadata from the Oauth Authorization Server ``/.well-known/oauth-authorization-server`` as defined in Section 3 of :rfc:`8414`.
In case the ``authorization_servers`` parameter is omitted, the Credential Issuer's identifier can be used to retrieve the Authorization Server metadata.

Below is a non-normative example.

.. literalinclude:: ../../examples/shared/credential-issuer-endpoint-3.http
   :language: http

The Oauth Authorization Server MUST respond with HTTP Status Code 200 and return the Oauth Authorization Server Metadata containing the parameters defined in :ref:`credential-issuer-metadata:Metadata for oauth_authorization_server`, using a JSON document with the media type *application/json*.

Credential Issuance Endpoints
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: credential-issuance-endpoint.rst

e-Service PDND Credential Issuer Catalog
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Credential Issuers MUST provide the following e-services through PDND to:

  - provide statistics about issued Credentials


Get Statistics
""""""""""""""

.. list-table::
  :class: longtable
  :widths: 20 80
  :stub-columns: 1

  * - **Description**
    - This service returns statistical data on issued Digital Credentials.
  * - **Provider**
    - Credential Issuer
  * - **Consumer**
    - Authorized Third Party

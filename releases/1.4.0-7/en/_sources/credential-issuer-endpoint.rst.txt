.. include:: ../common/common_definitions.rst

.. "included" file, so we start with '-' title level

.. role:: raw-html(raw)
  :format: html


Credential Issuer Endpoints
---------------------------

Metadata Endpoints
^^^^^^^^^^^^^^^^^^^^

The Credential Issuers MUST provide an Entity Configuration through the ``/.well-known/openid-federation`` endpoint, according to Section :ref:`trust-infrastructure:Entity Configuration`. Technical details are provided in Section :ref:`credential-issuer-entity-configuration:Credential Issuer Entity Configuration`.

Alternatively the Credential Issuer's Metadata can be retrieved using the Credential Issuer Identifier. The Metadata document in JSON or JWT format MUST be made available through the ``/.well-known/openid-credential-issuer`` endpoint as defined in Section 12.2.2 of `OpenID4VCI`_.

The ``Accept-Language`` header in the HTTP GET request can be used to indicate the language(s) preferred. In this case the Credential Issuer can send a subset of the metadata containing internationalized display data for one or all of the requested languages and indicate returned languages using the HTTP ``Content-Language`` Header.

Below is a non-normative example.

.. code-block:: http

    GET /.well-known/openid-credential-issuer HTTP/1.1
    Host: issuer.example.com
    Accept: application/json
    Accept-Language: it-IT, it;q=0.9


The Credential Issuer MUST respond with HTTP Status Code 200 and return the Credential Issuer Metadata containing the parameters defined in Section 12.2.3 of `OpenID4VCI`_ in addition to those defined in :ref:`credential-issuer-metadata:Metadata for openid_credential_issuer` as an unsigned JSON document using the media type *application/json* or a signed JSON Web Token using the media type *application/jwt*.

The ``authorization_servers`` entries of the Credential Issuer Metadata can be used to obtain the Authorization Server metadata from the Oauth Authorization Server ``/.well-known/oauth-authorization-server`` as defined in Section 3 of :rfc:`8414`. In case the ``authorization_servers`` parameter is omitted, the Credential Issuer's identifier can be used to retrieve the Authorization Server metadata.

Below is a non-normative example.

.. code-block:: http

    GET /.well-known/oauth-authorization-server HTTP/1.1
    Host: oauth-authorization-server.example.com

The Oauth Authorization Server MUST respond with HTTP Status Code 200 and return the Oauth Authorization Server Metadata containing the parameters defined in :ref:`credential-issuer-metadata:Metadata for oauth_authorization_server`, using a JSON document with the media type *application/json*.

Credential Issuance Endpoints
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: credential-issuance-endpoint.rst

e-Service PDND Credential Issuer Catalog
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Credential Issuers MUST provide the following e-services through PDND to:

  - manage data availability notifications and attribute updates coming from an Authentic Source;
  - revoke Digital Credentials issued to a revoked Wallet Instance
  - provide statistics about issued Credentials

.. only:: html

  .. note::
    A complete OpenAPI Specification is available :raw-html:`<a href="OAS3-PDND-Issuer.html" target="_blank">here</a>`.

.. only:: latex

  .. note::
    A complete OpenAPI Specification is available :ref:`appendix-oas-pdnd-issuer:Credential Issuer PDND OpenAPI Specification`.


Notify Wallet Instance Revocation
"""""""""""""""""""""""""""""""""

.. list-table::
  :class: longtable
  :widths: 20 80
  :stub-columns: 1
  
  * - **Description**
    - This service revokes all Digital Credentials associated with a specific User.
  * - **Provider**
    - Credential Issuer
  * - **Consumer**
    - Wallet Provider


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

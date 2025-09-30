.. include:: ../common/common_definitions.rst

.. "included" file, so we start with '-' title level

.. role:: raw-html(raw)
  :format: html


Credential Issuer Endpoints
---------------------------

Federation Endpoints
^^^^^^^^^^^^^^^^^^^^

The Credential Issuers MUST provide an Entity Configuration through the ``/.well-known/openid-federation`` endpoint, according to Section :ref:`trust:Entity Configuration`. Technical details are provided in Section :ref:`credential-issuer-entity-configuration:Credential Issuer Entity Configuration`.

Credential Issuance Endpoints
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: credential-issuance-endpoint.rst

e-Service PDND Credential Issuer Catalogue
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

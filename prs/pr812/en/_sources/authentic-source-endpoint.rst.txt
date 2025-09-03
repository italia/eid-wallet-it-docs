.. include:: ../common/common_definitions.rst


.. role:: raw-html(raw)
  :format: html

Authentic Source Endpoints
--------------------------

e-Service PDND Authentic Source Catalogue
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Public Authentic Sources MUST provide the following e-Service through PDND to provide the Credential Issuer with User's attributes required to the issuance of a Digital Credential.

.. only:: html

  .. note::
    A complete OpenAPI Specification is available :raw-html:`<a href="OAS3-PDND-AS.html" target="_blank">here</a>`.

.. only:: latex

  .. note::
    A complete OpenAPI Specification is available :ref:`appendix-oas-pdnd-as:Authentic Source PDND OpenAPI Specification`.

Get Attribute Claims
""""""""""""""""""""

.. _authentic-source-endpoint-get-attribute-claims:
.. list-table::
  :class: longtable
  :widths: 20 80
  :stub-columns: 1

  * - **Description**
    - This e-Service provides the Credential Issuer with all attribute claims necessary for the issuance of a Digital Credential.
  * - **Provider**
    - Authentic Source
  * - **Consumer**
    - Credential Issuer

Get Pseudonymization Algorithm
""""""""""""""""""""""""""""""""

.. _table_pseudonymization_endpoint_description:
.. list-table::
  :class: longtable
  :widths: 20 80
  :stub-columns: 1

  * - **Description**
    - This e-Service provides the Credential Issuer with the pseudonymization algorithm and salt used to compute each subject's pseudonym.
  * - **Provider**
    - Authentic Source
  * - **Consumer**
    - Credential Issuer


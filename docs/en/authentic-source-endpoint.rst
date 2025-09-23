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

.. note::
  The Authentic Source and the Credential Issuer MUST implement the necessary logic to keep track of the requests and responses exchanged via this e-Service, in order to be able to correlate them with the related issuance of a Digital Credential. In particular,
  - both MUST save the ``jti`` value in the Agid-JWT-Signature payload of the request to manage Signals related to the deffered issuance of a Digital Credential (see :ref:`signal-hub-endpoint:Signals Processing`);
  - the Authentic Source MUST record the ``last_updated`` `data-time` value which indicates the last time the User's attributes were updated in the Authentic Source's database;
  - the Credential Issuer MUST read the ``last_updated`` value received in the response to be able to check if the User's attributes have changed since the last issuance of a Digital Credential.



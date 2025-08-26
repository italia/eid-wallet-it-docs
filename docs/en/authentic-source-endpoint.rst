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

.. The Pseudonymization Endpoint is used by Credential Issuers to request Authentic Sources for the pseudonymization algorithm and salt used to compute each subject's pseudonym. 

.. The Pseudonymization Endpoint MUST be a GET request with the following parameters:

..   - Path Parameters:
    
..     - ``eserviceId``. REQUIRED. e-Service for which the pseudonymization algorithms is requested. It MUST correspond to the e-service Id value the Authentic Source is a Provider of.

..   - Headers parameters: these are those described in :ref:`e-service-pdnd:e-service Usage`.

.. ..note::
..   The Authentic Source, in addition to the checks described in :ref:`e-service-pdnd:e-service Usage`, SHOULD also check that the e-Service Id in the path corresponds to the e-Service Id referenced in the PDND Voucher.

.. If the Pseudonymization Endpoint request is correctly processed, the e-Service will then respond with status code HTTP 200 OK and ``Content-Type`` set to ``application/jwt`` as described in :ref:`e-service-pdnd:e-service Usage`, with the body containing the following additional parameters:

.. .. _table_pseudonymization_response_parameters:
.. .. list-table::
..   :widths: 25 75
..   :header-rows: 1

..   * - **Name**
..     - **Description**
..   * - **salt**
..     - REQUIRED. The salt value used to generate Pseudonymized Identifiers.
..   * - **cryptoHashFunction**
..     - REQUIRED. It MUST be the ``alg`` Identifier of the Cryptographic Hash Function; e.g., for SHA-256, the value MUST be ``sha-256``. 

.. If any error occurs during the request parsing, the response MUST adhere to the error format defined in :ref:`e-service-pdnd:e-Service Response`.

.. The pseudonym of a subject with Tax Id Number ``tax_id`` is computed as:

.. .. math::
..   pseudonym = hash(``tax_id``||``cryptoHashFunction``||``salt``)

.. where ``hash`` is the cryptographic hash function specified by the Authentic Source, and ``||`` denotes concatenation.


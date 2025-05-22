.. include:: ../common/common_definitions.rst


.. role:: raw-html(raw)
  :format: html


e-Service PDND Catalogue
==========================

Credential Issuer Catalogue
-----------------------------

Credential Issuers MUST provide the following e-services through PDND to:

  - manage data availability notifications and attribute updates coming from an Authentic Source;
  - revoke Digital Credentials issued to a revoked Wallet Instance
  - provide statistics about issued Credentials

.. only:: html

  .. note::
    A complete OpenAPI Specification is available :raw-html:`<a href="OAS3-PDND-Issuer.html" target="_blank">here</a>`.

.. only:: latex

  .. note::
    A complete OpenAPI Specification is available :ref:`appendix-oas-pdnd-issuer:Appendix B - Credential Issuer PDND e-services`.

Notify Available Credential
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
  :class: longtable
  :widths: 20 80
  :stub-columns: 1

  * - **Description**
    - This service informs Users when a specific credential has become
      available to be entered into the Wallet
  * - **Provider**
    - Credential Issuer
  * - **Consumer**
    - Authentic Source

Notify Update Credential
^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
  :class: longtable
  :widths: 20 80
  :stub-columns: 1

  * - **Description**
    - The service is designed to receive from Authentic Source (AS), via PDND,
      notification of a change of status and/or value of a specific attribute (e.g. MDL)
      with which a digital document issued by the Credential Issuer is
      associated.
  * - **Provider**
    - Credential Issuer
  * - **Consumer**
    - Authentic Source


Notify Wallet Instance Revocation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^

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

Authentic Source Catalogue
----------------------------

Public Authentic Sources MUST provide the following e-service through PDND to provide the Credential Issuer with User's attributes required to the issuance of a Digital Credential.

.. only:: html

  .. note::
    A complete OpenAPI Specification is available :raw-html:`<a href="OAS3-PDND-AS.html" target="_blank">here</a>`.

.. only:: latex

  .. note::
    A complete OpenAPI Specification is available :ref:`appendix-oas-pdnd-as:Appendix A - Authentic Source PDND e-services`.

Get Attribute Claims
^^^^^^^^^^^^^^^^^^^^

.. list-table::
  :class: longtable
  :widths: 20 80
  :stub-columns: 1

  * - **Description**
    - This service provides the Credential Issuer with all attribute claims necessary for the issuance of a Digital Credential.
  * - **Provider**
    - Authentic Source
  * - **Consumer**
    - Credential Issuer

Wallet Provider Catalogue
-------------------------

User's death leads to the revocation of the Wallet Instances of the User and the deletion of the User account at the Wallet Provider. For this reason, the Wallet Provider provides the following e-service through PDND.
A PID Provider that has been notified by the Authentic Source of the PID of the User's death MUST send a notification to Wallet Providers using this endpoint.

.. only:: html

  .. note::
    A complete OpenAPI Specification is available :raw-html:`<a href="OAS3-PDND-WP.html" target="_blank">here</a>`.

.. only:: latex

  .. note::
    A complete OpenAPI Specification is available :ref:`appendix-oas-pdnd-wp:Appendix C - Wallet Provider PDND e-services`.

Notify User Death
^^^^^^^^^^^^^^^^^

.. list-table::
    :class: longtable
    :widths: 20 80
    :stub-columns: 1

    * - **Description**
      - This service is used to notify the Wallet Provider of the need to revoke the Wallet Instance and delete the User's account due to the User's death.
    * - **Provider**
      - Wallet Provider
    * - **Consumer**
      - PID Provider


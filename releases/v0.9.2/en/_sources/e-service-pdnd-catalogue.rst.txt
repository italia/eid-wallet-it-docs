.. include:: ../common/common_definitions.rst

.. role:: raw-html(raw)
   :format: html

e-Service PDND Catalogue
========================

Credential Issuer Catalogue
---------------------------

Credential Issuers MUST provide the following e-services through PDND to:

    - manage data availability notifications and attribute updates coming from an Authentic Source;
    - revoke Digital Credentials issued to a revoked Wallet Instance
    - provide statistics about issued Credentials

.. note::
    A complete OpenAPI Specification is available :raw-html:`<a href="OAS3-PDND-Issuer.html" target="_blank">here</a>`.

Notify Available Credential
+++++++++++++++++++++++++++
.. list-table::
    :widths: 20 80 
    :stub-columns: 1

    * - **Description**
      - This service informs Users when a specific credential has become
        available to be entered into the Wallet
    * - **Provider**
      - PID/(Q)EAA Provider
    * - **Consumer**
      - Authentic Source

Notify Update Credential
++++++++++++++++++++++++

.. list-table::
    :widths: 20 80 
    :stub-columns: 1

    * - **Description**
      - The service is designed to receive from Authentic Source (AS), via PDND,
        notification of a change of status and/or value of a specific attribute (e.g. MDL)
        with which a digital document issued by the Credential Issuer is
        associated.
    * - **Provider**
      - PID/(Q)EAA Provider
    * - **Consumer**
      - Authentic Source


Notify Wallet Instance Revocation
++++++++++++++++++++++++++++++++++

.. list-table::
    :widths: 20 80 
    :stub-columns: 1

    * - **Description**
      - This service revokes all Digital Credentials associated with a specific
        User
    * - **Provider**
      - PID/(Q)EAA Provider
    * - **Consumer**
      - Wallet Provider

Get Statistics
++++++++++++++++++++++++++++++++++

.. list-table::
    :widths: 20 80 
    :stub-columns: 1

    * - **Description**
      - This service returns statistical data on issued Digital Credentials
    * - **Provider**
      - PID/(Q)EAA Provider
    * - **Consumer**
      - Authorized Third Party 


Authentic Source Catalogue
---------------------------

Public Authentic Sources MUST provide the following e-service through PDND to provide the Credential Issuer with User's attributes required to the issuance of a Digital Credential.  

.. note::
    A complete OpenAPI Specification is available :raw-html:`<a href="OAS3-PDND-AS.html" target="_blank">here</a>`.

Get Attribute Claims
+++++++++++++++++++++

.. list-table::
    :widths: 20 80 
    :stub-columns: 1

    * - **Description**
      - This service provides the Credential Issuer with all attribute claims necessary for the issuance of a Digital Credential.
    * - **Provider**
      - Authentic Source 
    * - **Consumer**
      - PID/(Q)EAA Provider

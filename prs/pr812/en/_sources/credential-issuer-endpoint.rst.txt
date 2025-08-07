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


PDND Signal Hub Notifications
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Signal Hub is a service provided by the PDND. It enables a PDND e-service Provider to issue a Signal of Change, which notifies all relevant e-service Consumers about a data variation within the Provider's domain.
Although the Signal Hub is hosted and managed by the PDND (acting as the service provider), all participating entities are considered consumers of the Signal Hub service. However, it is important to distinguish this from the actual consumer of the Signal of Change, which is always the Credential Issuer.
The Signal Hub allows the Credential Issuer to receive notifications indicating that a change has occurred. To access the updated data, the signal recipient must query the corresponding e-service, following standard PDND procedures.
For detailed technical specifications and implementation guidelines, please refer to the :raw-html:`<a href="https://developer.pagopa.it/pdnd-interoperabilita/guides/manuale-operativo-signal-hub" target="_blank">Signal Hub User Guide</a>`.

Authentic Sources
"""""""""""""""""

Authentic Sources MUST perform the following actions through PDND:

    - enable the Signal Hub feature for each credential e-service via GUI
    - submit a Signal of Change for each e-service output data variation

  .. note::
    A complete OpenAPI Specification is available :raw-html:`<a href="https://github.com/pagopa/interop-signalhub-core/blob/main/docs/openAPI/push-signals.yaml" target="_blank">here</a>`.


Notify Update Credential
........................

.. list-table::
  :class: longtable
  :widths: 20 80 
  :stub-columns: 1

  * - **Description**
    - The service is designed to allow Authentic Source (AS), via Signal Hub, to submit
      notification of a change of status and/or value of a specific attribute (e.g. MDL)
      associated with a digital document issued by the Credential Issuer.
  * - **Provider**
    - PDND
  * - **Consumer**
    - Authentic Source


Notify Available Credential
...........................

.. list-table::
  :class: longtable
  :widths: 20 80
  :stub-columns: 1

  * - **Description**
    - The service is designed to allow the Authentic Source (AS), via Signal Hub, to
      notify the User of the availability of a specific Credential to be entered
      into the Wallet.
  * - **Provider**
    - PDND
  * - **Consumer**
    - Authentic Source


Credential Issuer
"""""""""""""""""

Credential Issuers MUST perform the following actions through PDND:

    - monitor data changes for each e-service with Signal Hub enabled
    - retrieve the updated data from the subscribed e-service

  .. note::
    A complete OpenAPI Specification is available :raw-html:`<a href="https://github.com/pagopa/interop-signalhub-core/blob/main/docs/openAPI/pull-signals.yaml" target="_blank">here</a>`.


Check for Update Credential
...........................

.. list-table::
  :class: longtable
  :widths: 20 80 
  :stub-columns: 1

  * - **Description**
    - The service is designed to allow Credential Issuers (CI), via SignalHub, to check
      for changes in the status and/or value of a specific attribute (e.g. MDL)
      as notified by the Authentic Source.
  * - **Provider**
    - PDND
  * - **Consumer**
    - Credential Issuers


Check for Credential availability
.................................

.. list-table::
  :class: longtable
  :widths: 20 80 
  :stub-columns: 1

  * - **Description**
    - The service is designed to allow Credential Issuers (CI), via SignalHub, to check
      for the availability of a specific Credential in order to notify the User.
  * - **Provider**
    - PDND
  * - **Consumer**
    - Credential Issuers

.. include:: ../common/common_definitions.rst

.. "included" file, so we start with '-' title level

.. role:: raw-html(raw)
  :format: html


PDND Signal Hub Endpoints
-------------------------
Within the PDND platform, the Signal Hub acts as an intermediary between a PDND Provider and its PDND Consumers to signal data variations. To achieve that, the manager of the PDND platform, hereafter the PDND Manager, provides (playing the role of PDND e-Service Provider) two PDND Signal Hub e-Services:
  - the Signal Collection e-Service which is used by PDND e-Service Providers to deposit Signals (here, the PDND e-Service Provider acts as Consumer of the Signal Collection e-Service);
  - the Signal Distribution e-Service which is used by PDND e-Service Consumers to retrieve collected Signals (here, the PDND e-Service Consumer also acts as Consumer of the Signal Distribution e-Service).

In order to protect the privacy of the Signal's subject, the PDND Manager requires each PDND e-Service Provider to pseudonymize the subject's identifier inside Signals and set up a pseudonymization endpoint for their PDND e-Service. This pseudonymization endpoint is used by e-Service Consumers to obtain the pseudonymization algorithm used to calculate the Signal subject's pseudonym. In this way, only the PDND e-Service Provider and its PDND e-Service Consumers are able to link a Signal to the subject's personal data, while the PDND Manager only handles pseudonymized identifiers.

For detailed technical specifications and implementation guidelines, please refer to the :raw-html:`<a href="https://developer.pagopa.it/pdnd-interoperabilita/guides/manuale-operativo-Signal-hub" target="_blank">Signal Hub User Guide</a>`.

In the context of the IT Wallet, Authentic Sources interact with the Signal Hub to notify Credential Issuers about changes in the status and/or value of attributes associated with Digital Credentials. Specifically, 
  - the Authentic Source will deposit Signals in the Signal Hub, thus playing the role of PDND Consumer of the Signal Collection e-Service; 
  - the Credential Issuer will retrieve Signals from the Signal Hub, and will thus play the role of PDND e-Service Consumer of the Signal Distribution e-Service. 

.. note::

  In the context of IT Wallet, due to the particular nature of the data exchanged, the pseudonymization of the Signal's subject is not needed since it is already an opaque identifier unrelated to the Digial Credential's subject. Thus, the Authentic Source does not need to set up a pseudonymization endpoint for its e-Services. 

The use of the Signal Hub e-Services is mandatory for all Authentic Sources and Credential Issuers that are part of the IT Wallet ecosystem. 

Below it is provided the description of how the Authentic Sources and Credential Issuers interact with the Signal Hub e-Services together with the detailed formats of the requests and responses.

Prerequisites
^^^^^^^^^^^^^^^
Before using the Signal Hub, all Authentic Sources MUST:

  - have registered as Providers of their e-Service with the PDND;
  - have registered as Consumers of the Signal Collection e-Service of the Signal Hub;

Before using the Signal Hub, all Credential Issuers MUST:

  - have registered as Consumers of the relevant Authentic Sources' e-Services;
  - have registered as Consumers of the Signal Distribution e-Service of the Signal Hub;

Signal Hub e-Services
^^^^^^^^^^^^^^^^^^^^^^
This section describes the endpoints available for the Signal Hub Collection and Distribution e-Services, including their functionalities and the expected request and response formats.

Signal Collection e-Service
""""""""""""""""""""""""""""

Authentic Sources in the IT Wallet ecosystem use the Signal Collection e-Service to:

  - notify the Credential Issuer of a change of status and/or value of a specific attribute associated with a Digital Credential issued by the Credential Issuer;
  - notify the Credential Issuer of the availability of the attributes related to a specific Digital Credential which a User requested in its Wallet. 
  
The last case, referred to as deferred issuance, happens when the Credential Issuer has requested a Digital Credential's attributes from the Authentic Source (invoking the :ref:`authentic-source-endpoint:Get Attribute Claims` PDND endpoint) and the Authentic Source cannot respond immediately with the requested attributes. Thus, the Authentic Source notifies the Credential Issuer via the Signal Hub at a later time that the requested attributes are now available.

The Signal Collection e-Service endpoint is used by Authentic Sources to deposit Signals to the Signal Hub via a Signal Collection request. The latter MUST be a POST request with ``Content-Type`` set to ``application-json``, whose header MUST have the parameters described in :raw-html:`<a href="https://developer.pagopa.it/pdnd-interoperabilita/guides/manuale-operativo-signal-hub/1.0/tutorial/come-depositare-un-segnale" target="_blank">Signal Hub Signal Collection</a>` and whose body MUST contain the following parameters:

.. _table_Signal_deposit_request_parameters:
.. list-table::
  :widths: 25 75
  :header-rows: 1

  * - **Parameter Name**
    - **Description**
  * - **signalId**
    - REQUIRED. A positive 64 bit integer number referencing the identifier of the Signal in chronological order.
  * - **objectType**
    - REQUIRED. This filed is a free filed which the Authentic Source MAY use to further specify the Signal.
  * - **objectId**
    - REQUIRED. The subject to which the Signal is bound. If the Signal 
    
      - has ``signalType`` ``CREATE``, then it MUST be set to the ``jti`` value the Credental Issuer used in the Agid-JWT-Signature token of the `get_attributes` request to the Authentic Source to obtain the attributes related to a specific Digital Credential (see :ref:`authentic-source-endpoint:Get Attribute Claims`);
      - has ``signalType`` ``UPDATE``, then it MUST be set to the Authentic Source's unique database identifier of the Digial Credential's attributes the Signal refers to.
      
  * - **signalType**
    - REQUIRED. Signal Type. It MUST be one of the following: 

      - ``UPDATE``, when the Signal refers to a change in the status and/or value of a specific attribute associated with a Digital Credential;
      - ``CREATE``, when the Signal refers to the availability of the attributes of a specific Digital Credential;

  * - **eserviceId**
    - REQUIRED. e-Service to which the Signal is bound. It MUST correspond to the e-Service Id value the Authentic Source is a Provider of.

.. note::
  In the deffered issuance flow, i.e., when the Authentic Source notifies the Credential Issuer of the availability of the Digital Credential's attributes via Signal Hub; both entities MUST keep track of the Credential Issuer's ``jti`` value used in the Agid-JWT-Signature of the ``get_attributes`` request. This is necessary since the ``objectId`` of the Signal MUST be set to that ``jti`` value when the Signal has ``signalType`` ``CREATE``.

Non normative example of Signal Collection request for an can be found at :raw-html:`<a href="https://developer.pagopa.it/pdnd-interoperabilita/guides/manuale-operativo-signal-hub/1.0/tutorial/come-depositare-un-segnale" target="_blank">Signal Hub Signal Collection</a>`.

The Signal Collection e-Service response, acknowledging the correct parsing of the request, is specified in :raw-html:`<a href="https://developer.pagopa.it/pdnd-interoperabilita/guides/manuale-operativo-signal-hub/1.0/tutorial/come-depositare-un-segnale" target="_blank">Signal Hub Signal Collection</a>`, and has ``Content-Type`` set to ``application/json``. The payload contains the body parameter:

.. _table_Signal_deposit_response_parameters:
.. list-table::
  :widths: 25 75
  :header-rows: 1

  * - **Parameter Name**
    - **Description**
  * - **signalId**
    - REQUIRED. The identifier of the Signal that has been successfully collected by the Signal Collection e-Service.

If any error occurs during the request parsing, the response MUST adhere to the error format defined in :raw-html:`<a href="https://raw.githubusercontent.com/pagopa/interop-signalhub-core/refs/tags/1.0.1/docs/openAPI/push-signals.yaml" target="_blank">OAS-push</a>`.

.. only:: html

  .. note::
    A complete OpenAPI Specification of the Signal Collection e-Service is available :raw-html:`<a href="https://raw.githubusercontent.com/pagopa/interop-signalhub-core/refs/tags/1.0.1/docs/openAPI/push-signals.yaml" target="_blank">here</a>`.

The Authentic Source MUST implement the necessary logic to handle the requests to the Signal Collection e-Service endpoint, in doing this it has to consider the following aspects:

  - Signals are sent per PDND e-Service, meaning that the Authentic Source SHOULD implement a Signal deposit cycle for each e-Service ID it is a PDND Provider of;
  - Signals are labeled by a unique identifier, the ``signalId``, which is a positive 64 bit integer number. The ``signalId`` MUST be incremented by 1 for each new Signal the Authentic Source wishes to deposit in the Signal Collection e-Service endpoint. It is up to the Authentic Source to keep track of the last ``signalId`` it has sent. Signals with lower ``signalId`` values are considered older by the Signal Collection e-Service endpoint and will raise an error when received.

Signal Distribution e-Service
""""""""""""""""""""""""""""""
Credential Issuers in the IT Wallet ecosystem use the Signal Distribution e-Service to:

  - check for changes in the status and/or value of a specific attribute associated with a Digital Credential issued by the Credential Issuer itself;
  - check for the availability of attributes related to a Digital Credential requested by a User.

The Signal Distribution e-Service endpoint is used by Credential Issuers to retrieve Signals from the Signal Hub via a Signal Distribution request. The latter MUST be a GET request and MUST have the following parameters:

  - Path Parameters: 
    
    -  ``eserviceId``. REQUIRED. e-Service to which the Signal is bound. It MUST correspond to the e-Service Id value the Credential Issuer is a Consumer of.

  - Query Parameters:

    - ``signalId``. OPTIONAL. Integer representing the last Signal number processed by the Credential Issuer. The Signal Distribution e-Service will respond with Signals having progressively greater ``signalId`` values. If not specified, the default value is the lowest ``signalId`` value available in the Signal Distribution e-Service. 
    - ``size``. OPTIONAL. Integer representing the maximum number of Signals to be returned in the Signal Distribution response. If not specified, the default value is ``10``.

  - Headers parameters: these are those described in :raw-html:`<a href="https://developer.pagopa.it/pdnd-interoperabilita/guides/manuale-operativo-signal-hub/1.0/tutorial/come-recuperare-i-segnali" target="_blank">Signal Hub Signal Distribution</a>`.

If the Signal Distribution request is correctly processed, the e-Service will then respond with status code

 - HTTP 200 OK if the request is correctly formed and there are no more Signals to request;
 - HTTP 206 OK if the request is correctly formed but there are more Signals to request.

Regardless of the response code used, the response has ``Content-Type`` set to ``application/json`` an the header parameters indicated in :raw-html:`<a href="https://developer.pagopa.it/pdnd-interoperabilita/guides/manuale-operativo-signal-hub/1.0/tutorial/come-recuperare-i-segnali" target="_blank">Signal Hub Signal Distribution</a>`. The body parameter ``lastSignalId``, referencing the ``signalId`` of the last Signal transmitted by the Signal Distribution e-Service is added to the response's payload.

In :raw-html:`<a href="https://developer.pagopa.it/pdnd-interoperabilita/guides/manuale-operativo-signal-hub/1.0/tutorial/come-recuperare-i-segnali" target="_blank">Signal Hub Signal Distribution</a>` can be found non normative examples of a Signal Distribution requests and responses.

If any error occurs during the request parsing, the response MUST adhere to the error format defined in :raw-html:`<a href="https://raw.githubusercontent.com/pagopa/interop-signalhub-core/refs/tags/1.0.1/docs/openAPI/pull-signals.yaml" target="_blank">Signal Hub - Pull</a>`.

  .. note::
    A complete OpenAPI Specification of the Signal Collection e-Service is available :raw-html:`<a href="https://raw.githubusercontent.com/pagopa/interop-signalhub-core/refs/tags/1.0.1/docs/openAPI/pull-signals.yaml" target="_blank">here</a>`.

The Credential Issuer MUST implement the necessary logic to handle the Polling of the Signal Distribution e-Service endpoint, in doing this it has to consider the following aspects:

  - Signals are queried and retrieved per PDND e-Service, meaning that the Credential Issuer MUST implement a poll cycle for each e-Service ID;
  - the retention period of Signals in the Signal Hub is specified in :raw-html:`<a href="https://developer.pagopa.it/pdnd-interoperabilita/guides/manuale-operativo-signal-hub/1.0/la-guida-tecnica/retention-period-e-api-polling" target="_blank">Signal Hub User Guide</a>`. Signals older than the specified retention period are not available for retrieval;
  - the Signal Hub does not keep trak of the last ``signalId`` notified to a specific Credential Issuer. Thus each Credential Issuer MUST keep track of the last ``signalId`` it has received for each PDND e-Service ID;
  - the Signal Distribution e-Service endpoint returns Signals in batches. The maximal size the batch is specified in :raw-html:`<a href="https://developer.pagopa.it/pdnd-interoperabilita/guides/manuale-operativo-Signal-hub" target="_blank">Signal Hub User Guide</a>`. The Signal Distribution e-Service will indicate if additional Signals are available for retrieval.

Signals Processing
^^^^^^^^^^^^^^^^^^^^
After the Signals have been successfully recovered by the Credential Issuer, the latter MUST process them as follows:

  - For each Signal, the Credential Issuer MUST check the ``SignalType`` value:
    
    - if the Signal ``SignalType`` is ``UPDATE``, it means that the status and/or value of the attribute associated with a Digest Credential need updates; instead,
    - if the Signal ``SignalType`` is ``CREATE``, it means that the requested attributes of a specific Digital Credential are now available; 

    If the ``objectId`` does not correspond to any identifier know to the Credential Issuer, the Signal MUST be ignored. If instead it corresponds to a known identifier, the Credential Issuer MUST use the :ref:`authentic-source-endpoint:Get Attribute Claims` PDND endpoint of the Authentic Source to retrieve the updated information.
    
    When the Signal has been processed, the Credential Issuer will either move to the next Signal and update its ``signalId`` counter; or, if there are no more Signals to process, it will resume the Pull cycle.

.. warning::

  Given Signal Hub's currently supported security patterns, if the Authentic Source requires the `AUDIT_REST_02` security pattern from the Credential Issuer, the latter MUST revoke the Digital Credential referenced in Signals with ``signalType`` ``UPDATE`` before contacting the Authentic Source using the :ref:`authentic-source-endpoint:Get Attribute Claims` PDND endpoint. This process allows the Credential Issuer to provide evidence to the Authentic Source, via the `Agid-JWT-TrackingEvidence`, that the request includes the User's consent. 
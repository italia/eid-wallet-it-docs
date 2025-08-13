.. include:: ../common/common_definitions.rst

.. "included" file, so we start with '-' title level

.. role:: raw-html(raw)
  :format: html


PDND Signal Hub Endpoints
-------------------------

Signal Hub is a service provided by the PDND that enables two distinct interactions:
 - an e-service Provider is able to issue a "Signal" to the Signal Hub Push endpoint. This signal notifies all relevant e-service Consumers about a data change within the Provider's domain.
 - an e-service Consumer can query the Signal Hub Pull endpoint to check for updates related to the specific e-service they are Consumers of. This allows them to retrieve the latest data changes that have been signaled by the e-service Provider.

To preserve the anonimity of the Signal's subject, the e-service Provider MUST set un a pseudonymization endpoint. This MUST be an authenticated endpoint only available to PDND members which have subscribed as Consumer of the Producer's e-service.

Although the Signal Hub is hosted and managed by the PDND, all participating entities, i.e., e-service Producers and Consumers, are considered Consumers of the Signal Hub service.

For detailed technical specifications and implementation guidelines, please refer to the :raw-html:`<a href="https://developer.pagopa.it/pdnd-interoperabilita/guides/manuale-operativo-signal-hub" target="_blank">Signal Hub User Guide</a>`.

The use of the Signal Hub e-service is mandatory for all Authentic Sources and Credential Issuers that are part of the IT Wallet ecosystem. 

Below it is provided the description of how the Authentic Sources and Credential Issuers interacts with the Signal Hub service, the high livel flows and the detailed form of the requests and responses. Throughout this section, we assume that all requests to an e-service Provider, be it the Authentic Sources or the PDND (as the Signal Hub Provider), and all responses to the e-service Consumer follow :ref:`e-service-pdnd:e-service PDND`.    

Prerequisites
^^^^^^^^^^^^^^^

Before using the Signal Hub, all Authentic Sources MUST:

  - have registered as Providers of their e-service with the PDND;
  - have registered as Consumers of the Push e-service of the Signal Hub;
  - have set up the pseudonymization endpoint for their e-service, chosing an appropriate hash function and salt according to :raw-html:`<a href="https://developer.pagopa.it/pdnd-interoperabilita/guides/manuale-operativo-signal-hub/tutorial/come-esporre-le-informazioni-crittografiche-pseudonimizzazione" target="_blank">Signal Hub - Pseudonymization Guide</a>`. This SHOULD be a PDND e-service endpoint.

Before using the Signal Hub, all Credential Issuers MUST:

  - have registered as Consumers of the relevant Authentic Sources' e-services;
  - have registered as Consumers of the Pull e-service of the Signal Hub, and implement the necessary logic to handle the polling of the Signal Hub Pull endpoint;
  - have obtained the necessary pseudonymization algorithm and salt from the Authentic Sources' pseudonymization endpoints as described in :raw-html:`<a href="https://developer.pagopa.it/pdnd-interoperabilita/guides/manuale-operativo-signal-hub/tutorial/come-ottenere-le-informazioni-crittografiche" target="_blank">Signal Hub - Pseudonymization</a>`.

Authentic Sources
"""""""""""""""""""

Authentic Sources in the IT Wallet ecosystem use the Signal Hub Push e-service to:

  - notify the Credential Issuer of a change of status and/or value of a specific attribute associated with a Digital Credential issued by the Credential Issuer;
  - notify the Credential Issuer of a variation in the pseudonymization algorithm;
  - notify the Credential Issuer of the availability of a specific Credential to be entered into the Wallet. 
  
The last case happens whenever the Credential Issuer has requested the Digital Credential attributes from the Authentic Source (invoking the `get_attribute` PDND endpoint), but the Authentic Source cannot respond immediately with the requested attributes. Thus, the Authentic Source notifies the Credential Issuer via the Signal Hub at a later time that the requested Digital Credential is now available.

The Authentic Source MUST implement the necessary logic to handle the Signal Hub Push endpoint, in doing this it has to consider the following aspects:

  - Signals are sent per e-service, meaning that the Authentic Source SHOULD implement a push cycle for each e-service ID it is a Producer of;
  - Signals are labeled by a unique identifier, the ``signalId``, which is a positive 64 bit integer number. The Signal ID MUST be incremented by 1 for each new Signal sent by the Authentic Source. It is up to the Authentic Source to keep track of the last ``signalId`` it has sent. Signals with lower ``signalId`` values are considered older by the PDND and will raise an error if received.

Credential Issuers
""""""""""""""""""""

Credential Issuers in the IT Wallet ecosystem use the Signal Hub Pull e-service to:

  - check for changes in the status and/or value of a specific attribute associated with a Digital Credential issued by the Credential Issuer;
  - check for the availability of a specific Digiatal Credential;
  - check for changes in the pseudonymization algorithm used by the Authentic Source.

The Credential Issuer MUST implement the necessary logic to handle the polling of the Signal Hub Pull endpoint, in doing this it has to consider the following aspects:

  - Signals are queried and retrieved per e-service, meaning that the Credential Issuer MUST implement a poll cycle for each e-service ID;
  - the retention period of Signals in Signal Hub is 30 days;
  - the Signal Hub platform does not keep trak of the last ``signalId`` notified to a specific Credential Issuers. Thus each Credential Issuer MUST keep track of the last ``signalId`` it has received for each e-service ID;
  - the Signal Hub Pull endpoint returns Signals in batches of at most 100 Signals at a time, specifying if more signals are available for retrieval;  

Signal Hub Endpoints
^^^^^^^^^^^^^^^^^^^^^^

This section describes the endpoints available for the Signal Hub Push and Pull services, including their functionalities and the expected request and response formats.

Push Endpoint
""""""""""""""""""

The Push Endpoint is used by Authentic Sources to deposit Signals to the Signal Hub. The PUSH request MUST be a POST request with ``Content-Type`` set to ``application-json``, whose header MUST have the the parameters described in :ref:`e-service-pdnd:e-service Usage` and whose body MUST contain the following parameters:

.. _table_signal_push_request_parameters:
.. list-table::
  :widths: 25 75
  :header-rows: 1

  * - **Parameter Name**
    - **Description**
  * - **signalID**
    - REQUIRED. It MUST be a positive 64 bit integer number referencing the identifier of the signal in chronological order.
  * - **objectType**
    - REQUIRED. Signal category. If the e-service is used by different Credential Issuers, this parameter MAY be used to distinguish the type of object the Signal refers to. If the Signal refers to a cryptographic variation, then it MUST be set to ``-``.
  * - **objectId**
    - REQUIRED. The pseudonym to which the Signal is bound. If the Signal refers to a cryptographic variation, then it MUST be set to ``-``.
  * - **signalType**
    - REQUIRED. Signal Type. It MUST be one of the following: 
    
      - ``UPDATE``, when the Signal refers to a change of status and/or value for a specific attribute associated with a Digital Credential;
      - ``CREATE``, when the Signal refers to the availability of the attributes of a specific Digital Credential;
      - ``DELETE``, when the Signal refers to the deletion of a specific attribute associated with a Digital Credential;
      - ``SALTUPDATE``, when the Signal refers to a change in the pseudonymization algorithm' salt value used by the Authentic Source. 
  * - **eserviceId**
    - REQUIRED. e-Service to which the Signal is bound. It MUST correspond to the e-service Id value the Authentic Source is a Producer of.

Non normative examples of payloads of Phus Requests by the Authentic Source are presented below.

.. code-block:: http
    :name: code_Signal_PUSH_Request_1

    POST /1.0/push/signals HTTP/1.1
    Host: api.signalhub.interop.pagopa.it
    Authorization: DPoP eyJhbGciOiJFUzI1NiIsImtpZCI6ImI4MzlmNGM3LTFlNWQtNGE4YS05ZmM2LTcyZDNiN2YwOTFlYyIsInR5cCI6ImF0K2p3dCJ9.eyJhdWQiOiJodHRwczovL2lzc3Vlci5leGFtcGxlLml0Iiwic3ViIjoiMzE2NzAwOTItZWVjMC00Zjk1LTg4ZGEtZTFjN2NlNWU0NTA1IiwibmJmIjoxNzM2ODQ2Njg4LCJwdXJwb3NlSWQiOiI1NzBhNDE1ZS0wZTdmLTQxMGQtODVlZC1jNTVlYTU1Mzc5MzIiLCJpc3MiOiJ1YXQuaW50ZXJvcC5wYWdvcGEuaXQiLCJleHAiOjE3MzY4NDY5MjgsImlhdCI6MTczNjg0NjY4OCwiY2xpZW50X2lkIjoiMzE2NzAwOTItZWVjMC00Zjk1LTg4ZGEtZTFjN2NlNWU0NTA1IiwianRpIjoiOGI5NzFiNDMtZTk5MC00NGZhLTkwMTMtMWIzNTNiZmM1YTBmIiwiZGlnZXN0Ijp7ImFsZyI6IlNIQTI1NiIsInZhbHVlIjoiMzM2YjYyY2FlZTc0YWFjMzUyOTM1MmJiM2I1ODM5NWFhYzU4MGRjNzYyMDE0Mzc3ZTRmNjdlODY5YWUzNzM4OSJ9LCJjbmYiOnsiamt0IjoiZjgyMTc2MDY2ZWIzOGZkMzM4MGQyZDNkMzRkZWI1ODkwZTY4NWVlOGU5ZTE1YTdlYjg0ODcyYTZmYWMzNDA2MyJ9fQ.y42yfMeW2H9h0b0j0BODUml8yF20stY9q3BwoVU5BB90afBj852Q0QlInncdhjXhUjLS1V76cGBxkutDNvxRNA
    DPoP: eyJ0eXAiOiJkcG9wK2p3dCIsImFsZyI6IkVTMjU2IiwiandrIjp7Imt0eSI6IkVDIiwia2V5X29wcyI6WyJzaWduIl0sImtpZCI6ImRGVTNNRDI4REpfamZzZmloUHZpMm8tQ3RqTEVVejNwT0lWMEJkTk1mZjgiLCJjcnYiOiJQLTI1NiIsIngiOiJodXlYSVFOdjkwMm9Mc3BYNF96b25DOTRHNnlFbG42bHNkbS0xd003MzJvIiwieSI6Ikk5UERFYXdXSHFhRkRHeDFaa05rLTJQVjZXZHBjYUgzQWZPYkJTTGloZ3cifX0.eyJqdGkiOiItQndDM0VTYzZhY2MybFRjIiwiaHRtIjoiUE9TVCIsImF0aCI6ImNiZGJmNmZlZWY0ODA2MjI4ZGJmNDY0Yjc1MGE5NGMyOGQ4ZTUzMDFhNzE1ZmZjM2U2Y2QyZjk0YjZlOGUxNTQiLCJodHUiOiJodHRwczovL3NlcnZlci5leGFtcGxlLmNvbS90b2tlbiIsImlhdCI6MTc2MjI2MjYxNn0.uL017GdfXzJ-9jhs6AUpwtkWLgyBgDWOtlrFvMltLp0C0NFwwMpOGnv-FxxwfYdJj--cteyCjGnmJZhekEKIEA
    Agi-JWT-Signature: eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6ImY3YjI1NDhjYTZjYjM4NzY2YTU5NTFiYiJ9.eyJhdWQiOiJodHRwczovL2lzc3Vlci5leGFtcGxlLml0Iiwic3ViIjoiMzE2NzAwOTItZWVjMC00Zjk1LTg4ZGEtZTFjN2NlNWU0NTA1IiwibmJmIjoxNzM2ODQ2Njg4LCJwdXJwb3NlSWQiOiI1NzBhNDE1ZS0wZTdmLTQxMGQtODVlZC1jNTVlYTU1Mzc5MzIiLCJpc3MiOiIzMTY3MDA5Mi1lZWMwLTRmOTUtODhkYS1lMWM3Y2U1ZTQ1MDUiLCJleHAiOjE3MzY4NDY5MjgsImlhdCI6MTczNjg0NjY4OCwiY2xpZW50X2lkIjoiMzE2NzAwOTItZWVjMC00Zjk1LTg4ZGEtZTFjN2NlNWU0NTA1IiwianRpIjoiOGI5NzFiNDMtZTk5MC00NGZhLTkwMTMtMWIzNTNiZmM1YTBkIiwic2lnbmVkX2hlYWRlcnMiOnsiZGlnZXN0IjoiU0hBLTI1Nj1hZTVjMDNmZTM4MThiNDRiM2U2MDA0MDZjZWYzNzQwNGEyN2JkNTZiMzk4MTk1MjE4Mzg5ZjJlZDRhZThlMTBmIiwiY29udGVudC10eXBlIjoiYXBwbGljYXRpb24vanNvbiJ9fQ.a6Vd2s128ANPR-AWIEbLwEBtylYtLuH1IYKL-xCQG31BMBzB6F28PmFmw5_gxPRvzAJzyLuImSZX2VVrUmabGA
    Digest: ae5c03fe3818b44b3e600406cef37404a27bd56b398195218389f2ed4ae8e10f
    Content-Type: application/json

    {
      "signalID": 1,
      "objectType": "domicilio"
      "objectId": "fec44ba9afc68492a387199c9faaaa5d954b19b39140637712a67cb90c726575"
      "eserviceId": "b1817321-0486-4c75-89e5-4ee297250418",
      "signalType": "UPDATE"
    }

.. code-block:: http
    :name: code_Signal_PUSH_Request_2

    POST /1.0/push/signals HTTP/1.1
    Host: api.signalhub.interop.pagopa.it
    Authorization: DPoP eyJhbGciOiJFUzI1NiIsImtpZCI6ImI4MzlmNGM3LTFlNWQtNGE4YS05ZmM2LTcyZDNiN2YwOTFlYyIsInR5cCI6ImF0K2p3dCJ9.eyJhdWQiOiJodHRwczovL2lzc3Vlci5leGFtcGxlLml0Iiwic3ViIjoiMzE2NzAwOTItZWVjMC00Zjk1LTg4ZGEtZTFjN2NlNWU0NTA1IiwibmJmIjoxNzM2ODQ2Njg4LCJwdXJwb3NlSWQiOiI1NzBhNDE1ZS0wZTdmLTQxMGQtODVlZC1jNTVlYTU1Mzc5MzIiLCJpc3MiOiJ1YXQuaW50ZXJvcC5wYWdvcGEuaXQiLCJleHAiOjE3MzY4NDY5MjgsImlhdCI6MTczNjg0NjY4OCwiY2xpZW50X2lkIjoiMzE2NzAwOTItZWVjMC00Zjk1LTg4ZGEtZTFjN2NlNWU0NTA1IiwianRpIjoiOGI5NzFiNDMtZTk5MC00NGZhLTkwMTMtMWIzNTNiZmM1YTBmIiwiZGlnZXN0Ijp7ImFsZyI6IlNIQTI1NiIsInZhbHVlIjoiMzM2YjYyY2FlZTc0YWFjMzUyOTM1MmJiM2I1ODM5NWFhYzU4MGRjNzYyMDE0Mzc3ZTRmNjdlODY5YWUzNzM4OSJ9LCJjbmYiOnsiamt0IjoiZjgyMTc2MDY2ZWIzOGZkMzM4MGQyZDNkMzRkZWI1ODkwZTY4NWVlOGU5ZTE1YTdlYjg0ODcyYTZmYWMzNDA2MyJ9fQ.y42yfMeW2H9h0b0j0BODUml8yF20stY9q3BwoVU5BB90afBj852Q0QlInncdhjXhUjLS1V76cGBxkutDNvxRNA
    DPoP: eyJ0eXAiOiJkcG9wK2p3dCIsImFsZyI6IkVTMjU2IiwiandrIjp7Imt0eSI6IkVDIiwia2V5X29wcyI6WyJzaWduIl0sImtpZCI6ImRGVTNNRDI4REpfamZzZmloUHZpMm8tQ3RqTEVVejNwT0lWMEJkTk1mZjgiLCJjcnYiOiJQLTI1NiIsIngiOiJodXlYSVFOdjkwMm9Mc3BYNF96b25DOTRHNnlFbG42bHNkbS0xd003MzJvIiwieSI6Ikk5UERFYXdXSHFhRkRHeDFaa05rLTJQVjZXZHBjYUgzQWZPYkJTTGloZ3cifX0.eyJqdGkiOiItQndDM0VTYzZhY2MybFRjIiwiaHRtIjoiUE9TVCIsImF0aCI6ImNiZGJmNmZlZWY0ODA2MjI4ZGJmNDY0Yjc1MGE5NGMyOGQ4ZTUzMDFhNzE1ZmZjM2U2Y2QyZjk0YjZlOGUxNTQiLCJodHUiOiJodHRwczovL3NlcnZlci5leGFtcGxlLmNvbS90b2tlbiIsImlhdCI6MTc2MjI2MjYxNn0.uL017GdfXzJ-9jhs6AUpwtkWLgyBgDWOtlrFvMltLp0C0NFwwMpOGnv-FxxwfYdJj--cteyCjGnmJZhekEKIEA
    Agi-JWT-Signature: eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6ImY3YjI1NDhjYTZjYjM4NzY2YTU5NTFiYiJ9.eyJhdWQiOiJodHRwczovL2lzc3Vlci5leGFtcGxlLml0Iiwic3ViIjoiMzE2NzAwOTItZWVjMC00Zjk1LTg4ZGEtZTFjN2NlNWU0NTA1IiwibmJmIjoxNzM2ODQ2Njg4LCJwdXJwb3NlSWQiOiI1NzBhNDE1ZS0wZTdmLTQxMGQtODVlZC1jNTVlYTU1Mzc5MzIiLCJpc3MiOiIzMTY3MDA5Mi1lZWMwLTRmOTUtODhkYS1lMWM3Y2U1ZTQ1MDUiLCJleHAiOjE3MzY4NDY5MjgsImlhdCI6MTczNjg0NjY4OCwiY2xpZW50X2lkIjoiMzE2NzAwOTItZWVjMC00Zjk1LTg4ZGEtZTFjN2NlNWU0NTA1IiwianRpIjoiOGI5NzFiNDMtZTk5MC00NGZhLTkwMTMtMWIzNTNiZmM1YTBkIiwic2lnbmVkX2hlYWRlcnMiOnsiZGlnZXN0IjoiU0hBLTI1Nj05NzYwMTg0NDlkMWJkMmJjMzY1MTdhODlkMzhhODBiMmQ4NjY3YTAwZGNjMmQzZGUyNmE2NDY5NjM0OGY5ZDAwIiwiY29udGVudC10eXBlIjoiYXBwbGljYXRpb24vanNvbiJ9fQ.P0iv1Lq2Yhw10Qu3XGikK6H8eb4flqzCfu2WwYZ-x7VbdbdnU3aWP2PsYVXu0Y2tBijQZC_6lx6uxUsG5GOLLQ
    Digest: 976018449d1bd2bc36517a89d38a80b2d8667a00dcc2d3de26a64696348f9d00
    Content-Type: application/json

    {
      "signalID": 2,
      "objectType": "-"
      "objectId": "-"
      "eserviceId": "b1817321-0486-4c75-89e5-4ee297250418",
      "signalType": "SALTUPDATE"
    }

The response acknowledgind the correct parsing of the request MUST be a HTTP 200 OK with ``Content-Type`` set to ``application/json`` and the body containing the following parameters:

.. _table_signal_push_response_parameters:
.. list-table::
  :widths: 25 75
  :header-rows: 1

  * - **Parameter Name**
    - **Description**
  * - **signalID**
    - REQUIRED. The identifier of the Signal that has been successfully transmitted.

If any error occurs during the request parsing, the response MUST adhere to the error format defined in :ref:`e-service-pdnd:e-Service Response`.

Pull Endpoint
""""""""""""""""
The PULL endpoint is used by Credential Issuers to retrieve Signals from the Signal Hub. The PULL request MUST be a GET request which MUST have 

  - Path Parameters: 
    
    -  ``eserviceId``. REQUIRED. e-Service to which the Signal is bound. It MUST correspond to the e-service Id value the Credential Issuer is a Consumer of.

  - Query Parameters:

    - ``signalID``. OPTIONAL. Integer representing the number of Signals the PULL endpoint is expected to return. If not specified, the default value is 100.
    - ``size``. OPTIONAL. Integer representing the maximum number of Signals to be returned in the response. If not specified, the default value is 10.

  - Headers parameters: these are those described in :ref:`e-service-pdnd:e-service Usage`.

Below it is provided a non normative example of a PULL request by the Credential Issuer:

.. code-block:: http
    :name: code_Signal_Pull_Request

    GET /1.0/pull/signals/b1817321-0486-4c75-89e5-4ee297250418?signalID=100&size=10 HTTP/1.1
    Host: api.signalhub.interop.pagopa.it
    Authorization: DPoP eyJhbGciOiJFUzI1NiIsImtpZCI6ImI4MzlmNGM3LTFlNWQtNGE4YS05ZmM2LTcyZDNiN2YwOTFlYyIsInR5cCI6ImF0K2p3dCJ9.eyJhdWQiOiJodHRwczovL2lzc3Vlci5leGFtcGxlLml0Iiwic3ViIjoiMzE2NzAwOTItZWVjMC00Zjk1LTg4ZGEtZTFjN2NlNWU0NTA1IiwibmJmIjoxNzM2ODQ2Njg4LCJwdXJwb3NlSWQiOiI1NzBhNDE1ZS0wZTdmLTQxMGQtODVlZC1jNTVlYTU1Mzc5MzIiLCJpc3MiOiJ1YXQuaW50ZXJvcC5wYWdvcGEuaXQiLCJleHAiOjE3MzY4NDY5MjgsImlhdCI6MTczNjg0NjY4OCwiY2xpZW50X2lkIjoiMzE2NzAwOTItZWVjMC00Zjk1LTg4ZGEtZTFjN2NlNWU0NTA1IiwianRpIjoiOGI5NzFiNDMtZTk5MC00NGZhLTkwMTMtMWIzNTNiZmM1YTBmIiwiZGlnZXN0Ijp7ImFsZyI6IlNIQTI1NiIsInZhbHVlIjoiMzM2YjYyY2FlZTc0YWFjMzUyOTM1MmJiM2I1ODM5NWFhYzU4MGRjNzYyMDE0Mzc3ZTRmNjdlODY5YWUzNzM4OSJ9LCJjbmYiOnsiamt0IjoiZjgyMTc2MDY2ZWIzOGZkMzM4MGQyZDNkMzRkZWI1ODkwZTY4NWVlOGU5ZTE1YTdlYjg0ODcyYTZmYWMzNDA2MyJ9fQ.y42yfMeW2H9h0b0j0BODUml8yF20stY9q3BwoVU5BB90afBj852Q0QlInncdhjXhUjLS1V76cGBxkutDNvxRNA
    DPoP: eyJ0eXAiOiJkcG9wK2p3dCIsImFsZyI6IkVTMjU2IiwiandrIjp7Imt0eSI6IkVDIiwia2V5X29wcyI6WyJzaWduIl0sImtpZCI6ImRGVTNNRDI4REpfamZzZmloUHZpMm8tQ3RqTEVVejNwT0lWMEJkTk1mZjgiLCJjcnYiOiJQLTI1NiIsIngiOiJodXlYSVFOdjkwMm9Mc3BYNF96b25DOTRHNnlFbG42bHNkbS0xd003MzJvIiwieSI6Ikk5UERFYXdXSHFhRkRHeDFaa05rLTJQVjZXZHBjYUgzQWZPYkJTTGloZ3cifX0.eyJqdGkiOiItQndDM0VTYzZhY2MybFRjIiwiaHRtIjoiUE9TVCIsImF0aCI6ImNiZGJmNmZlZWY0ODA2MjI4ZGJmNDY0Yjc1MGE5NGMyOGQ4ZTUzMDFhNzE1ZmZjM2U2Y2QyZjk0YjZlOGUxNTQiLCJodHUiOiJodHRwczovL3NlcnZlci5leGFtcGxlLmNvbS90b2tlbiIsImlhdCI6MTc2MjI2MjYxNn0.uL017GdfXzJ-9jhs6AUpwtkWLgyBgDWOtlrFvMltLp0C0NFwwMpOGnv-FxxwfYdJj--cteyCjGnmJZhekEKIEA

If the POLL request is correctly processed, the e-Service will then respond with status code

 - HTTP 200 OK if the Signal Distribution Request is correctly formed and there are no more signals to request,
 - HTTP 206 OK if the Signal Distribution Request is correctly formed and there are more signals to request.

Regardless of the response code used, the response MUST have ``Content-Type`` set to ``application/jwt`` with the header and body containing the parameters described in :ref:`e-service-pdnd:e-Service Response` with the addition of the body parameters:

.. _table_signal_pull_response_parameters:
.. list-table::
  :widths: 25 75
  :header-rows: 1

  * - **Parameter Name**
    - **Description**
  * - **signals**
    - REQUIRED. JSON Array of JSON Objects containing the Signals transmitted by the PDND to the Credential Issuer. Each JSON Object SHOULD contain the following parameters:
    
      - **signalId**: REQUIRED. Integer corresponding to the identifier of the Signal in chronological order.
      - **objectType**: REQUIRED. Signal category. If the e-service is used by different Credential Issuers, this parameter MAY be used to distinguish the type of object the Signal refers to.
      - **objectId**: REQUIRED. The pseudonym to which the Signal is bound.
      - **signalType**: REQUIRED. Signal Type. It MUST be one of the following:
      
        - ``UPDATE``, when the Signal refers to a change of status and/or value for a specific attribute associated with a Digital Credential;
        - ``CREATE``, when the Signal refers to the availability of the attributes of a specific Digital Credential;
        - ``DELETE``, when the Signal refers to the deletion of a specific attribute associated with a Digital Credential;
        - ``SALTUPDATE``, when the Signal refers to a change in the pseudonymization algorithm' salt value used by the Authentic Source.
      - **eserviceId**: REQUIRED. e-Service to which the Signal is bound. It MUST correspond to the e-service Id value the PDND is a Consumer of.
  * - **lastSignalId**
    - REQUIRED. Integer corresponding to the ``signalId`` of the last Signal included in the Response by the PDND e-Service. If no Signals are available, this value must be ``null``.

Below it is provided a non normative example of a PULL response by the PDND:

.. code-block:: http
    :name: code_Signal_Pull_Response

    HTTP/1.1 200 OK
    Content-Type: application/jwt
    
    eyJhbGciOiJFUzI1NiIsImtpZCI6IjI4MDJhNjktMTYwNC00MjYxLTkyNDYtMjE0NTNlMjA2NThlIiwidHlwIjoiSldUIn0.eyJpc3MiOiJodHRwczovL2FwaS5zaWduYWxodWIuaW50ZXJvcC5wYWdvcGEuaXQvMS4wL3B1bGwvc2lnbmFscyIsImF1ZCI6IjlhOGI3YzZkLWU1ZjQtZzNoMi1pMWowLWtsbW5vcHFyc3R1diIsImV4cCI6MTc4MzQwMTc4NSwibmJmIjoxNzUzNDAxMzg3LCJpYXQiOjE3NTM0MDEyNTYsImp0aSI6Ijk5NzUzMmUtODcxYS00OTY5LTk5OTktMTIzNDU2Nzg5YWJjIiwic2lnbmFscyI6W3sic2lnbmFsSWQiOjEsIm9iamVjdFR5cGUiOiJkb21pY2lsaW8iLCJvYmplY3RJZCI6ImZlYzQ0YmE5YWZjNjg0OTJhMzg3MTk5YzlmYWFhYTVkOTU0YjE5YjM5MTQwNjM3NzEyYTY3Y2I5MGM3MjY1NzUiLCJzaWduYWxUeXBlIjoiVVBEQVRFIiwiZXNlcnZpY2VJZCI6ImIxODE3MzIxLTA0ODYtNGM3NS04OWU1LTRlZTI5NzI1MDQxOCJ9LHsic2lnbmFsSWQiOjIsIm9iamVjdFR5cGUiOiItIiwib2JqZWN0SWQiOiItIiwic2lnbmFsVHlwZSI6IlNBTFRVUERBVEUiLCJlc2VydmljZUlkIjoiYjE4MTczMjEtMDQ4Ni00Yzc1LTg5ZTUtNGVlMjk3MjUwNDE4In1dLCJsYXN0U2lnbmFsSWQiOjJ9.MpF2pqoVZJwVBEkfcX3xGn_B_zmYSuYjd1JXVIImDT-yMxC9o1QOCRUjoJ-xTdHBqJzhzMHo22-rpZAADbhgdQ

The decoded body of the JWT is as follows:

.. literalinclude:: ../../examples/SH-pull-response-example-payload.json
  :language: JSON

If any error occurs during the request parsing, the response MUST adhere to the error format defined in :ref:`e-service-pdnd:e-Service Response`.

Signals Processing
^^^^^^^^^^^^^^^^^^^^

After the Signals have been successfully recovered by the Credential Issuer, the latter MUST process them as follows:

  - For each Signal, the Credential Issuer MUST check the ``objectId`` value:
    
    - if the latter is ``-`` and the ``signalType`` is ``SALTUPDATE``, it means that the Signal refers to a variation of the pseudonymization algorithm. It MUST immediately stop all Signal processing and request the updated information from the Authentic Source pseudonymization endpoint. Having obtained the updated information, it MUST update its all its pseudonyms accordingly before proceeding with the processing of the remaining Signals.
    - if it is not ``-``, it means that the Signal refers to a change of status and/or value of a specific attribute associated with a Digital Credential. In this case, the Credential Issuer MUST check if the ``objectId`` corresponds to a pseudonym of a subject with an on-going process with the Credential Issuer. If so, if
      
      - the Signal ``signalType`` is ``UPDATE``, it means that the status and/or value of the attribute associated with a Digest Credential need updates; instead,
      - if the Signal ``signalType`` is ``CREATE``, it means that the requested attributes of a specific Digital Credential are now available; 

      in both cases the Credential Issuer MUST use the `Get Attributes` PDND endpoint of the Authentic Source to retrive the updated information. 

  ..note::
    
    When the Credential Issuer requests the credential attributes by invoking the `Get Attributes` PDND endpoint of the Authentic Source, it has already all information to generate the pseudonym of the Digital Credential' subject. Thus, to be able to use the Signal Hub it SHOULD immediately calculate and store the subject's pseudonym, using the same pseudonymization algorithm and salt given by the Authentic Source pseudonymization endpoint.  


.. include:: ../common/common_definitions.rst

.. "included" file, so we start with '-' title level

.. role:: raw-html(raw)
  :format: html


PDND Signal Hub Endpoints
-------------------------
Within the PDND platform, the Signal Hub acts as an intermediary between a PDND Provider and its PDND Consumers to centralize and facilitate the exchange of messages containing data variations called Signals. To achieve that the manager of the PDND platform, hereafter the PDND Manager, provides (playing the role of PDND e-Service Provider) two PDND Signal Hub e-Services:
  - the Signal Collection e-Service which is used by PDND e-Service Providers to deposit Signals (here, the PDND e-Service Provider acts as Consumer of the Signal Collection e-Service);
  - the Signal Distribution e-Service which is used by PDND e-Service Consumers to retrieve collected Signals (here, the PDND e-Service Consumer also acts as Consumer of the Signal Distribution e-Service).

In order to protect the privacy of the Signal's subject, the PDND Manager requires each PDND e-Service Provider to pseudonymize the subject's identifier inside Signals and set up a pseudonymization endpoint for their PDND e-Service. This pseudonymization endpoint is used by e-Service Consumers to obtain the pseudonymization algorithm used to calculate the Signal subject's pseudonym. In this way, only the PDND e-Service Provider and its PDND e-Service Consumers are able to link a Signal to the subject's personal data, while the PDND Manager only handles pseudonymized identifiers.

For detailed technical specifications and implementation guidelines, please refer to the :raw-html:`<a href="https://developer.pagopa.it/pdnd-interoperabilita/guides/manuale-operativo-Signal-hub" target="_blank">Signal Hub User Guide</a>`.

In the context of the IT Wallet, Authentic Sources interact with the Signal Hub to notify Credential Issuers about changes in the status and/or value of attributes associated with Digital Credentials, as well as to notify changes in the pseudonymization algorithm used by the Authentic Source. Specifically, 
  - the Authentic Source will deposit Signals in the Signal Hub, thus playing the role of PDND Consumer of the Signal Collection e-Service; 
  - the Credential Issuer will retrieve Signals from the Signal Hub, and will thus play the role of PDND e-Service Consumer of the Signal Distribution e-Service. 

In addition, for the the pseudonymization algorithm,
  - the Authentic Sources exposes the pseudonymization endpoint and notifies, with a Signal, the Crededential Issuer whenever the pseudonimization algorithm's parameters changes;
  - the Credential Issuer will monitors for these Signal and, if found, requests the updated algorithm's parameters to the pseudonymization endpoint.

For details on this endpoint, please refer to :ref:`authentic-source-endpoint:Get Pseudonymization Algorithm`.

The use of the Signal Hub e-Services is mandatory for all Authentic Sources and Credential Issuers that are part of the IT Wallet ecosystem. 

Below it is provided the description of how the Authentic Sources and Credential Issuers interact with the Signal Hub e-Services together with the detailed formats of the requests and responses. Throughout this section, it is assumed that all requests and all responses follow :ref:`e-Service-pdnd:e-Service PDND`.    

Prerequisites
^^^^^^^^^^^^^^^
Before using the Signal Hub, all Authentic Sources MUST:

  - have registered as Providers of their e-Service with the PDND;
  - have registered as Consumers of the Signal Collection e-Service of the Signal Hub;
  - have set up the pseudonymization endpoint for their e-Service, chosing an appropriate hash function and salt according to :raw-html:`<a href="https://developer.pagopa.it/pdnd-interoperabilita/guides/manuale-operativo-Signal-hub/tutorial/come-esporre-le-informazioni-crittografiche-pseudonimizzazione" target="_blank">Signal Hub - Pseudonymization Guide</a>`.

Before using the Signal Hub, all Credential Issuers MUST:

  - have registered as Consumers of the relevant Authentic Sources' e-Services;
  - have registered as Consumers of the Signal Distribution e-Service of the Signal Hub;
  - have obtained the necessary pseudonymization algorithm from the Authentic Sources' pseudonymization endpoints as described in :raw-html:`<a href="https://developer.pagopa.it/pdnd-interoperabilita/guides/manuale-operativo-Signal-hub/tutorial/come-ottenere-le-informazioni-crittografiche" target="_blank">Signal Hub - Pseudonymization</a>`.

Signal Hub e-Services
^^^^^^^^^^^^^^^^^^^^^^
This section describes the endpoints available for the Signal Hub Collection and Distribution e-Services, including their functionalities and the expected request and response formats.

Signal Collection e-Service
""""""""""""""""""""""""""""

Authentic Sources in the IT Wallet ecosystem use the Signal Collection e-Service to:

  - notify the Credential Issuer of a change of status and/or value of a specific attribute associated with a Digital Credential issued by the Credential Issuer;
  - notify the Credential Issuer of a variation in the pseudonymization algorithm;
  - notify the Credential Issuer of the availability of the attributes related to a specific Digital Credential which a User requested in its Wallet. 
  
The last case happens whenever the Credential Issuer has requested a Digital Credential's attributes from the Authentic Source (invoking the :ref:`authentic-source-endpoint:Get Attribute Claims` PDND endpoint), but the Authentic Source cannot respond immediately with the requested attributes. Thus, the Authentic Source notifies the Credential Issuer via the Signal Hub at a later time that the requested attributes are now available.

The Signal Collection e-Service endpoint is used by Authentic Sources to deposit Signals to the Signal Hub via a Signal Collection request. The latter MUST be a POST request with ``Content-Type`` set to ``application-json``, whose header MUST have the parameters described in :ref:`e-Service-pdnd:e-Service Usage` and whose body MUST contain the following parameters:

.. _table_Signal_deposit_request_parameters:
.. list-table::
  :widths: 25 75
  :header-rows: 1

  * - **Parameter Name**
    - **Description**
  * - **signalId**
    - REQUIRED. A positive 64 bit integer number referencing the identifier of the Signal in chronological order.
  * - **objectType**
    - REQUIRED. REQUIRED. Digital Credential Type. The value of this parameter is the same as the ``credential_type`` value present in the Catalogue. If the Signal refers to a cryptographic variation, then it MUST be set to ``-``.
  * - **objectId**
    - REQUIRED. The pseudonym to which the Signal is bound. If the Signal refers to a cryptographic variation, then it MUST be set to ``-``.
  * - **SignalType**
    - REQUIRED. Signal Type. It MUST be one of the following: 
    
      - ``ATTRIBUTE_UPDATE``, when the Signal refers to a change of status and/or value for a specific attribute associated with a Digital Credential;
      - ``CREATE``, when the Signal refers to the availability of the attributes of a specific Digital Credential;
      - ``REVOKE``, when the Signal refers to the revocation of the attributes contained in the Digital Credential;
      - ``SUSPEND``, when the Signal refers to the temporary suspension of the attributes contained in the Digital Credential;
      - ``SALTUPDATE``, when the Signal refers to a change in the pseudonymization algorithm' salt value used by the Authentic Source.
  * - **dataId**
    - OPTIONAL. Authentic Source database identifier of the Digial Credential's attributes the Signal refers to. This parameter MUST be provided when the Signal refers to a set of multiple attributes in the Authentic Source system.   
  * - **eserviceId**
    - REQUIRED. e-Service to which the Signal is bound. It MUST correspond to the e-Service Id value the Authentic Source is a Provider of.

Non normative examples of Signal Collection requests for an UPDATE and a SEEDUPDATE Signal by the Authentic Source are presented below.

.. code-block:: http
    :name: code_Signal_deposit_Request_1

    POST /1.0/push/Signals HTTP/1.1
    Host: api.Signalhub.interop.pagopa.it
    Authorization: DPoP eyJhbGciOiJFUzI1NiIsImtpZCI6ImI4MzlmNGM3LTFlNWQtNGE4YS05ZmM2LTcyZDNiN2YwOTFlYyIsInR5cCI6ImF0K2p3dCJ9.eyJhdWQiOiJodHRwczovL2lzc3Vlci5leGFtcGxlLml0Iiwic3ViIjoiMzE2NzAwOTItZWVjMC00Zjk1LTg4ZGEtZTFjN2NlNWU0NTA1IiwibmJmIjoxNzM2ODQ2Njg4LCJwdXJwb3NlSWQiOiI1NzBhNDE1ZS0wZTdmLTQxMGQtODVlZC1jNTVlYTU1Mzc5MzIiLCJpc3MiOiJ1YXQuaW50ZXJvcC5wYWdvcGEuaXQiLCJleHAiOjE3MzY4NDY5MjgsImlhdCI6MTczNjg0NjY4OCwiY2xpZW50X2lkIjoiMzE2NzAwOTItZWVjMC00Zjk1LTg4ZGEtZTFjN2NlNWU0NTA1IiwianRpIjoiOGI5NzFiNDMtZTk5MC00NGZhLTkwMTMtMWIzNTNiZmM1YTBmIiwiZGlnZXN0Ijp7ImFsZyI6IlNIQTI1NiIsInZhbHVlIjoiMzM2YjYyY2FlZTc0YWFjMzUyOTM1MmJiM2I1ODM5NWFhYzU4MGRjNzYyMDE0Mzc3ZTRmNjdlODY5YWUzNzM4OSJ9LCJjbmYiOnsiamt0IjoiZjgyMTc2MDY2ZWIzOGZkMzM4MGQyZDNkMzRkZWI1ODkwZTY4NWVlOGU5ZTE1YTdlYjg0ODcyYTZmYWMzNDA2MyJ9fQ.y42yfMeW2H9h0b0j0BODUml8yF20stY9q3BwoVU5BB90afBj852Q0QlInncdhjXhUjLS1V76cGBxkutDNvxRNA
    DPoP: eyJ0eXAiOiJkcG9wK2p3dCIsImFsZyI6IkVTMjU2IiwiandrIjp7Imt0eSI6IkVDIiwia2V5X29wcyI6WyJzaWduIl0sImtpZCI6ImRGVTNNRDI4REpfamZzZmloUHZpMm8tQ3RqTEVVejNwT0lWMEJkTk1mZjgiLCJjcnYiOiJQLTI1NiIsIngiOiJodXlYSVFOdjkwMm9Mc3BYNF96b25DOTRHNnlFbG42bHNkbS0xd003MzJvIiwieSI6Ikk5UERFYXdXSHFhRkRHeDFaa05rLTJQVjZXZHBjYUgzQWZPYkJTTGloZ3cifX0.eyJqdGkiOiItQndDM0VTYzZhY2MybFRjIiwiaHRtIjoiUE9TVCIsImF0aCI6ImNiZGJmNmZlZWY0ODA2MjI4ZGJmNDY0Yjc1MGE5NGMyOGQ4ZTUzMDFhNzE1ZmZjM2U2Y2QyZjk0YjZlOGUxNTQiLCJodHUiOiJodHRwczovL3NlcnZlci5leGFtcGxlLmNvbS90b2tlbiIsImlhdCI6MTc2MjI2MjYxNn0.uL017GdfXzJ-9jhs6AUpwtkWLgyBgDWOtlrFvMltLp0C0NFwwMpOGnv-FxxwfYdJj--cteyCjGnmJZhekEKIEA
    Agid-JWT-Signature: eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6ImY3YjI1NDhjYTZjYjM4NzY2YTU5NTFiYiJ9.eyJhdWQiOiJodHRwczovL2lzc3Vlci5leGFtcGxlLml0Iiwic3ViIjoiMzE2NzAwOTItZWVjMC00Zjk1LTg4ZGEtZTFjN2NlNWU0NTA1IiwibmJmIjoxNzM2ODQ2Njg4LCJwdXJwb3NlSWQiOiI1NzBhNDE1ZS0wZTdmLTQxMGQtODVlZC1jNTVlYTU1Mzc5MzIiLCJpc3MiOiIzMTY3MDA5Mi1lZWMwLTRmOTUtODhkYS1lMWM3Y2U1ZTQ1MDUiLCJleHAiOjE3MzY4NDY5MjgsImlhdCI6MTczNjg0NjY4OCwiY2xpZW50X2lkIjoiMzE2NzAwOTItZWVjMC00Zjk1LTg4ZGEtZTFjN2NlNWU0NTA1IiwianRpIjoiOGI5NzFiNDMtZTk5MC00NGZhLTkwMTMtMWIzNTNiZmM1YTBkIiwic2lnbmVkX2hlYWRlcnMiOnsiZGlnZXN0IjoiU0hBLTI1Nj1hZTVjMDNmZTM4MThiNDRiM2U2MDA0MDZjZWYzNzQwNGEyN2JkNTZiMzk4MTk1MjE4Mzg5ZjJlZDRhZThlMTBmIiwiY29udGVudC10eXBlIjoiYXBwbGljYXRpb24vanNvbiJ9fQ.a6Vd2s128ANPR-AWIEbLwEBtylYtLuH1IYKL-xCQG31BMBzB6F28PmFmw5_gxPRvzAJzyLuImSZX2VVrUmabGA
    Digest: SHA-256=ae5c03fe3818b44b3e600406cef37404a27bd56b398195218389f2ed4ae8e10f
    Content-Type: application/json

    {
      "signalId": 1,
      "objectType": "domicilio"
      "objectId": "fec44ba9afc68492a387199c9faaaa5d954b19b39140637712a67cb90c726575"
      "eserviceId": "b1817321-0486-4c75-89e5-4ee297250418",
      "SignalType": "UPDATE"
    }

.. code-block:: http
    :name: code_Signal_deposit_Request_2

    POST /1.0/push/Signals HTTP/1.1
    Host: api.Signalhub.interop.pagopa.it
    Authorization: DPoP eyJhbGciOiJFUzI1NiIsImtpZCI6ImI4MzlmNGM3LTFlNWQtNGE4YS05ZmM2LTcyZDNiN2YwOTFlYyIsInR5cCI6ImF0K2p3dCJ9.eyJhdWQiOiJodHRwczovL2lzc3Vlci5leGFtcGxlLml0Iiwic3ViIjoiMzE2NzAwOTItZWVjMC00Zjk1LTg4ZGEtZTFjN2NlNWU0NTA1IiwibmJmIjoxNzM2ODQ2Njg4LCJwdXJwb3NlSWQiOiI1NzBhNDE1ZS0wZTdmLTQxMGQtODVlZC1jNTVlYTU1Mzc5MzIiLCJpc3MiOiJ1YXQuaW50ZXJvcC5wYWdvcGEuaXQiLCJleHAiOjE3MzY4NDY5MjgsImlhdCI6MTczNjg0NjY4OCwiY2xpZW50X2lkIjoiMzE2NzAwOTItZWVjMC00Zjk1LTg4ZGEtZTFjN2NlNWU0NTA1IiwianRpIjoiOGI5NzFiNDMtZTk5MC00NGZhLTkwMTMtMWIzNTNiZmM1YTBmIiwiZGlnZXN0Ijp7ImFsZyI6IlNIQTI1NiIsInZhbHVlIjoiMzM2YjYyY2FlZTc0YWFjMzUyOTM1MmJiM2I1ODM5NWFhYzU4MGRjNzYyMDE0Mzc3ZTRmNjdlODY5YWUzNzM4OSJ9LCJjbmYiOnsiamt0IjoiZjgyMTc2MDY2ZWIzOGZkMzM4MGQyZDNkMzRkZWI1ODkwZTY4NWVlOGU5ZTE1YTdlYjg0ODcyYTZmYWMzNDA2MyJ9fQ.y42yfMeW2H9h0b0j0BODUml8yF20stY9q3BwoVU5BB90afBj852Q0QlInncdhjXhUjLS1V76cGBxkutDNvxRNA
    DPoP: eyJ0eXAiOiJkcG9wK2p3dCIsImFsZyI6IkVTMjU2IiwiandrIjp7Imt0eSI6IkVDIiwia2V5X29wcyI6WyJzaWduIl0sImtpZCI6ImRGVTNNRDI4REpfamZzZmloUHZpMm8tQ3RqTEVVejNwT0lWMEJkTk1mZjgiLCJjcnYiOiJQLTI1NiIsIngiOiJodXlYSVFOdjkwMm9Mc3BYNF96b25DOTRHNnlFbG42bHNkbS0xd003MzJvIiwieSI6Ikk5UERFYXdXSHFhRkRHeDFaa05rLTJQVjZXZHBjYUgzQWZPYkJTTGloZ3cifX0.eyJqdGkiOiItQndDM0VTYzZhY2MybFRjIiwiaHRtIjoiUE9TVCIsImF0aCI6ImNiZGJmNmZlZWY0ODA2MjI4ZGJmNDY0Yjc1MGE5NGMyOGQ4ZTUzMDFhNzE1ZmZjM2U2Y2QyZjk0YjZlOGUxNTQiLCJodHUiOiJodHRwczovL3NlcnZlci5leGFtcGxlLmNvbS90b2tlbiIsImlhdCI6MTc2MjI2MjYxNn0.uL017GdfXzJ-9jhs6AUpwtkWLgyBgDWOtlrFvMltLp0C0NFwwMpOGnv-FxxwfYdJj--cteyCjGnmJZhekEKIEA
    Agid-JWT-Signature: eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6ImY3YjI1NDhjYTZjYjM4NzY2YTU5NTFiYiJ9.eyJhdWQiOiJodHRwczovL2lzc3Vlci5leGFtcGxlLml0Iiwic3ViIjoiMzE2NzAwOTItZWVjMC00Zjk1LTg4ZGEtZTFjN2NlNWU0NTA1IiwibmJmIjoxNzM2ODQ2Njg4LCJwdXJwb3NlSWQiOiI1NzBhNDE1ZS0wZTdmLTQxMGQtODVlZC1jNTVlYTU1Mzc5MzIiLCJpc3MiOiIzMTY3MDA5Mi1lZWMwLTRmOTUtODhkYS1lMWM3Y2U1ZTQ1MDUiLCJleHAiOjE3MzY4NDY5MjgsImlhdCI6MTczNjg0NjY4OCwiY2xpZW50X2lkIjoiMzE2NzAwOTItZWVjMC00Zjk1LTg4ZGEtZTFjN2NlNWU0NTA1IiwianRpIjoiOGI5NzFiNDMtZTk5MC00NGZhLTkwMTMtMWIzNTNiZmM1YTBkIiwic2lnbmVkX2hlYWRlcnMiOnsiZGlnZXN0IjoiU0hBLTI1Nj05NzYwMTg0NDlkMWJkMmJjMzY1MTdhODlkMzhhODBiMmQ4NjY3YTAwZGNjMmQzZGUyNmE2NDY5NjM0OGY5ZDAwIiwiY29udGVudC10eXBlIjoiYXBwbGljYXRpb24vanNvbiJ9fQ.P0iv1Lq2Yhw10Qu3XGikK6H8eb4flqzCfu2WwYZ-x7VbdbdnU3aWP2PsYVXu0Y2tBijQZC_6lx6uxUsG5GOLLQ
    Digest: SHA-256=976018449d1bd2bc36517a89d38a80b2d8667a00dcc2d3de26a64696348f9d00
    Content-Type: application/json

    {
      "signalId": 2,
      "objectType": "-"
      "objectId": "-"
      "eserviceId": "b1817321-0486-4c75-89e5-4ee297250418",
      "SignalType": "SALTUPDATE"
    }

The Signal Collection e-Service response, acknowledging the correct parsing of the request, MUST have ``Content-Type`` set to ``application/jwt`` with the header and body containing the parameters described in :ref:`e-Service-pdnd:e-Service Response` with the addition of the body parameter:

.. _table_Signal_deposit_response_parameters:
.. list-table::
  :widths: 25 75
  :header-rows: 1

  * - **Parameter Name**
    - **Description**
  * - **signalId**
    - REQUIRED. The identifier of the Signal that has been successfully collected by the Signal Collection e-Service.

If any error occurs during the request parsing, the response MUST adhere to the error format defined in :ref:`e-Service-pdnd:e-Service Response`.

.. only:: html

  .. note::
    A complete OpenAPI Specification of the Signal Collection e-Service is available :raw-html:`<a href="OAS3-SH-AS.html" target="_blank">here</a>`.

The Authentic Source MUST implement the necessary logic to handle the requests to the Signal Collection e-Service endpoint, in doing this it has to consider the following aspects:

  - Signals are sent per PDND e-Service, meaning that the Authentic Source SHOULD implement a Signal deposit cycle for each e-Service ID it is a PDND Provider of;
  - Signals are labeled by a unique identifier, the ``signalId``, which is a positive 64 bit integer number. The ``signalId`` MUST be incremented by 1 for each new Signal the Authentic Source wishes to deposit in the Signal Collection e-Service endpoint. It is up to the Authentic Source to keep track of the last ``signalId`` it has sent. Signals with lower ``signalId`` values are considered older by the Signal Collection e-Service endpoint and will raise an error when received.

Signal Distribution e-Service
""""""""""""""""""""""""""""""
Credential Issuers in the IT Wallet ecosystem use the Signal Distribution e-Service to:

  - check for changes in the status and/or value of a specific attribute associated with a Digital Credential issued by the Credential Issuer itself;
  - check for the availability of attributes related to a Digital Credential requested by a User;
  - check for variations in the pseudonymization algorithm used by the Authentic Source.

The Signal Distribution e-Service endpoint is used by Credential Issuers to retrieve Signals from the Signal Hub via a Signal Distribution request. The latter MUST be a GET request and MUST have 

  - Path Parameters: 
    
    -  ``eserviceId``. REQUIRED. e-Service to which the Signal is bound. It MUST correspond to the e-Service Id value the Credential Issuer is a Consumer of.

  - Query Parameters:

    - ``signalId``. OPTIONAL. Integer representing the last Signal number processed by the Credential Issuer. The Signal Distribution e-Service will respond with Signals having progressively greater ``signalId`` values. If not specified, the default value is the lowest ``signalId`` value available in the Signal Distribution e-Service. 
    - ``size``. OPTIONAL. Integer representing the maximum number of Signals to be returned in the Signal Distribution response. If not specified, the default value is ``10``.

  - Headers parameters: these are those described in :ref:`e-Service-pdnd:e-Service Usage`.

Below it is provided a non normative example of a Signal Distribution request by the Credential Issuer:

.. code-block:: http
    :name: code_Signal_retrieve_Request

    GET /1.0/pull/Signals/b1817321-0486-4c75-89e5-4ee297250418?signalId=100&size=10 HTTP/1.1
    Host: api.Signalhub.interop.pagopa.it
    Authorization: DPoP eyJhbGciOiJFUzI1NiIsImtpZCI6ImI4MzlmNGM3LTFlNWQtNGE4YS05ZmM2LTcyZDNiN2YwOTFlYyIsInR5cCI6ImF0K2p3dCJ9.eyJhdWQiOiJodHRwczovL2lzc3Vlci5leGFtcGxlLml0Iiwic3ViIjoiMzE2NzAwOTItZWVjMC00Zjk1LTg4ZGEtZTFjN2NlNWU0NTA1IiwibmJmIjoxNzM2ODQ2Njg4LCJwdXJwb3NlSWQiOiI1NzBhNDE1ZS0wZTdmLTQxMGQtODVlZC1jNTVlYTU1Mzc5MzIiLCJpc3MiOiJ1YXQuaW50ZXJvcC5wYWdvcGEuaXQiLCJleHAiOjE3MzY4NDY5MjgsImlhdCI6MTczNjg0NjY4OCwiY2xpZW50X2lkIjoiMzE2NzAwOTItZWVjMC00Zjk1LTg4ZGEtZTFjN2NlNWU0NTA1IiwianRpIjoiOGI5NzFiNDMtZTk5MC00NGZhLTkwMTMtMWIzNTNiZmM1YTBmIiwiZGlnZXN0Ijp7ImFsZyI6IlNIQTI1NiIsInZhbHVlIjoiMzM2YjYyY2FlZTc0YWFjMzUyOTM1MmJiM2I1ODM5NWFhYzU4MGRjNzYyMDE0Mzc3ZTRmNjdlODY5YWUzNzM4OSJ9LCJjbmYiOnsiamt0IjoiZjgyMTc2MDY2ZWIzOGZkMzM4MGQyZDNkMzRkZWI1ODkwZTY4NWVlOGU5ZTE1YTdlYjg0ODcyYTZmYWMzNDA2MyJ9fQ.y42yfMeW2H9h0b0j0BODUml8yF20stY9q3BwoVU5BB90afBj852Q0QlInncdhjXhUjLS1V76cGBxkutDNvxRNA
    DPoP: eyJ0eXAiOiJkcG9wK2p3dCIsImFsZyI6IkVTMjU2IiwiandrIjp7Imt0eSI6IkVDIiwia2V5X29wcyI6WyJzaWduIl0sImtpZCI6ImRGVTNNRDI4REpfamZzZmloUHZpMm8tQ3RqTEVVejNwT0lWMEJkTk1mZjgiLCJjcnYiOiJQLTI1NiIsIngiOiJodXlYSVFOdjkwMm9Mc3BYNF96b25DOTRHNnlFbG42bHNkbS0xd003MzJvIiwieSI6Ikk5UERFYXdXSHFhRkRHeDFaa05rLTJQVjZXZHBjYUgzQWZPYkJTTGloZ3cifX0.eyJqdGkiOiItQndDM0VTYzZhY2MybFRjIiwiaHRtIjoiUE9TVCIsImF0aCI6ImNiZGJmNmZlZWY0ODA2MjI4ZGJmNDY0Yjc1MGE5NGMyOGQ4ZTUzMDFhNzE1ZmZjM2U2Y2QyZjk0YjZlOGUxNTQiLCJodHUiOiJodHRwczovL3NlcnZlci5leGFtcGxlLmNvbS90b2tlbiIsImlhdCI6MTc2MjI2MjYxNn0.uL017GdfXzJ-9jhs6AUpwtkWLgyBgDWOtlrFvMltLp0C0NFwwMpOGnv-FxxwfYdJj--cteyCjGnmJZhekEKIEA

If the Signal Distribution request is correctly processed, the e-Service will then respond with status code

 - HTTP 200 OK if the request is correctly formed and there are no more Signals to request,
 - HTTP 206 OK if the request is correctly formed but there are more Signals to request.

Regardless of the response code used, the response MUST have ``Content-Type`` set to ``application/jwt`` with the header and body containing the parameters described in :ref:`e-Service-pdnd:e-Service Response` with the addition of the body parameters:

.. _table_Signal_retrieve_response_parameters:
.. list-table::
  :widths: 25 75
  :header-rows: 1

  * - **Parameter Name**
    - **Description**
  * - **Signals**
    - REQUIRED. JSON Array of JSON Objects containing the Signals transmitted by the Signal Distribution e-Service to the Credential Issuer. Each JSON Object MUST contain the following parameters:
    
      - **signalId**: REQUIRED. Integer corresponding to the identifier of the Signal in chronological order.
      - **objectType**: REQUIRED. Digital Credential Type. The value of this parameter is the same as the ``credential_type`` value present in the Catalogue. If the Signal refers to a cryptographic variation, then it MUST be set to ``-``.
      - **objectId**: REQUIRED. The pseudonym to which the Signal is bound.
      - **SignalType**: REQUIRED. Signal Type. It MUST be one of the following:
      
        - ``ATTRIBUTE_UPDATE``, when the Signal refers to a change of status and/or value for a specific attribute associated with a Digital Credential;
        - ``CREATE``, when the Signal refers to the availability of the attributes of a specific Digital Credential;
        - ``REVOKE``, when the Signal refers to the revocation of the attributes contained in the Digital Credential;
        - ``SUSPEND``, when the Signal refers to the temporary suspension of the attributes contained in the Digital Credential;
        - ``SALTUPDATE``, when the Signal refers to a change in the pseudonymization algorithm' salt value used by the Authentic Source.
      - **eserviceId**: REQUIRED. e-Service to which the Signal is bound. It MUST correspond to the e-Service Id value the PDND is a Consumer of.
      - **dataId**: OPTIONAL. Authentic Source database identifier of the Digial Credential's attributes the Signal refers to.  This parameter MUST be provided when the Signal refers to a set of multiple attributes in the Authentic Source system.
  * - **lastsignalId**
    - REQUIRED. Integer corresponding to the ``signalId`` of the last Signal included in the Signal Distribution response by the Signal Distribution e-Service. If no Signals are available, this value must be ``null``.

Below it is provided a non normative example of a Signal Distribution response:

.. code-block:: http
    :name: code_Signal_Signal Distribution_Response

    HTTP/1.1 200 OK
    Content-Type: application/jwt
    
    eyJhbGciOiJFUzI1NiIsImtpZCI6IjI4MDJhNjktMTYwNC00MjYxLTkyNDYtMjE0NTNlMjA2NThlIiwidHlwIjoiSldUIn0.eyJpc3MiOiJodHRwczovL2FwaS5zaWduYWxodWIuaW50ZXJvcC5wYWdvcGEuaXQvMS4wL3B1bGwvc2lnbmFscyIsImF1ZCI6IjlhOGI3YzZkLWU1ZjQtZzNoMi1pMWowLWtsbW5vcHFyc3R1diIsImV4cCI6MTc4MzQwMTc4NSwibmJmIjoxNzUzNDAxMzg3LCJpYXQiOjE3NTM0MDEyNTYsImp0aSI6Ijk5NzUzMmUtODcxYS00OTY5LTk5OTktMTIzNDU2Nzg5YWJjIiwic2lnbmFscyI6W3sic2lnbmFsSWQiOjEsIm9iamVjdFR5cGUiOiJkb21pY2lsaW8iLCJvYmplY3RJZCI6ImZlYzQ0YmE5YWZjNjg0OTJhMzg3MTk5YzlmYWFhYTVkOTU0YjE5YjM5MTQwNjM3NzEyYTY3Y2I5MGM3MjY1NzUiLCJzaWduYWxUeXBlIjoiVVBEQVRFIiwiZXNlcnZpY2VJZCI6ImIxODE3MzIxLTA0ODYtNGM3NS04OWU1LTRlZTI5NzI1MDQxOCJ9LHsic2lnbmFsSWQiOjIsIm9iamVjdFR5cGUiOiItIiwib2JqZWN0SWQiOiItIiwic2lnbmFsVHlwZSI6IlNBTFRVUERBVEUiLCJlc2VydmljZUlkIjoiYjE4MTczMjEtMDQ4Ni00Yzc1LTg5ZTUtNGVlMjk3MjUwNDE4In1dLCJsYXN0U2lnbmFsSWQiOjJ9.MpF2pqoVZJwVBEkfcX3xGn_B_zmYSuYjd1JXVIImDT-yMxC9o1QOCRUjoJ-xTdHBqJzhzMHo22-rpZAADbhgdQ

The decoded body of the JWT is as follows:

.. literalinclude:: ../../examples/SH-pull-response-example-payload.json
  :language: JSON

If any error occurs during the request parsing, the response MUST adhere to the error format defined in :ref:`e-Service-pdnd:e-Service Response`.

.. only:: html

  .. note::
    A complete OpenAPI Specification of the Signal Distribution e-Service is available :raw-html:`<a href="OAS3-SH-CI.html" target="_blank">here</a>`.

The Credential Issuer MUST implement the necessary logic to handle the Polling of the Signal Distribution e-Service endpoint, in doing this it has to consider the following aspects:

  - Signals are queried and retrieved per PDND e-Service, meaning that the Credential Issuer MUST implement a poll cycle for each e-Service ID;
  - the retention period of Signals in the Signal Hub is 30 days, meaning that Signals older than 30 days are not available for retrieval;
  - the Signal Hub does not keep trak of the last ``signalId`` notified to a specific Credential Issuer. Thus each Credential Issuer MUST keep track of the last ``signalId`` it has received for each PDND e-Service ID;
  - the Signal Distribution e-Service endpoint returns Signals in batches of at most 100 Signals at a time, specifying if more Signals are available for retrieval;  

Signals Processing
^^^^^^^^^^^^^^^^^^^^
After the Signals have been successfully recovered by the Credential Issuer, the latter MUST process them as follows:

  - For each Signal, the Credential Issuer MUST check the ``objectId`` value:
    
    - if the latter is ``-`` and the ``SignalType`` is ``SALTUPDATE``, it means that the Signal refers to a variation of the pseudonymization algorithm. It MUST immediately stop all Signal processing and request the updated information from the Authentic Source pseudonymization endpoint. After having obtained the updated cryptographic information, it MUST update all pseudonyms related to the Signal's ``eserviceId`` and ``objectType`` values. After completion of this operation, the Credential Issuer can proceed to process the remaining Signals.
    - if it is not ``-``, it means that the Signal refers to a change of status and/or value of a specific attribute associated with a Digital Credential or that the User's attributes of a specific Digital Credential are available. In each case, the Credential Issuer MUST check if the ``objectId`` corresponds to the pseudonym of a User with an on-going process with the Credential Issuer itself. If so,
      
      - if the Signal ``SignalType`` is ``UPDATE``, it means that the status and/or value of the attribute associated with a Digest Credential need updates; instead,
      - if the Signal ``SignalType`` is ``REVOKE``, it means that the attributes contained in the Digital Credential have been revoked;
      - if the Signal ``SignalType`` is ``SUSPEND``, it means that the attributes contained in the Digital Credential have been temporarily suspended;
      - if the Signal ``SignalType`` is ``CREATE``, it means that the requested attributes of a specific Digital Credential are now available; 

      in both cases the Credential Issuer MUST use the :ref:`authentic-source-endpoint:Get Attribute Claims` PDND endpoint of the Authentic Source to retrieve the updated information. 
    
    If the ``objectId`` does not correspond to any pseudonym of a User with an on-going process with the Credential Issuer, the Signal MUST be ignored. When the Signal has been processed, the Credential Issuer will either move to the next Signal or, if there are no more Signals to process, update its ``signalId`` counter and resume the Pull cycle.

.. note::
  When the Credential Issuer requests the credential attributes by invoking the :ref:`authentic-source-endpoint:Get Attribute Claims` PDND endpoint of the Authentic Source, it already possesses all information to generate the pseudonym of the Digital Credential' subject. Therefore, to be able to use the Signal Hub, it SHOULD immediately calculate and store the subject's pseudonym, using the same pseudonymization algorithm and salt given by the Authentic Source pseudonymization endpoint.


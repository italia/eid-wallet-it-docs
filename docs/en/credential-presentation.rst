.. include:: ../common/common_definitions.rst


Digital Credential Presentation
================================

This section describes how a Relying Party Instance requests to a Wallet Instance the presentation of the PID/EAAs.

In this section the following flows are described:

- :ref:`remote-flow:Remote Flow`, where the User presents a Digital Credential to a web Relying Party Instance according to `OpenID4VP`_. In this scenario the user-agent and the Wallet Instance can be used in the same device (**Same Device Flow**), or in different devices (**Cross Device Flow**).
- :ref:`proximity-flow:Proximity Flow`, where the User presents a Digital Credential to a mobile Relying Party Instance according to `ISO18013-5`_. The User interacts with a Verifier using proximity connection technologies such as using QR Codes and Bluetooth Low Energy (BLE).

.. note::
  When a Relying Party needs to distinguish the User during authentication, it MUST do so on the basis of the information contained in the Digital Credentials requested in the presentation request. The corresponding claims must be included in the presentation request. The Relying Party distinguishes the User by evaluating the values of the claims actually presented.

  Non-normative examples are provided below.

  1. **PID or IT-Wallet ID.** The Relying Party requests the identification claims defined by the relevant data model, for example ``given_name``, ``family_name`` and ``personal_administrative_number`` for the PID, or ``tax_id_code`` for the IT-Wallet ID. See :ref:`credential-data-model-pid:PID Data Model` and :ref:`credential-data-model-it-wallet-id:IT-Wallet ID Data Model`.

     Example of a ``dcql_query`` in the remote flow (PID in SD-JWT VC format):

     .. code-block:: json

       {
         "credentials": [
           {
             "id": "pid",
             "format": "dc+sd-jwt",
             "meta": {
               "vct_values": [ "urn:eudi:pid:it:1" ]
             },
             "claims": [
               {"path": ["given_name"]},
               {"path": ["family_name"]},
               {"path": ["personal_administrative_number"]}
             ]
           }
         ]
       }

     The same claims, in the proximity flow, are requested in the mdoc ``ItemsRequest``:

     .. code-block:: json

       {
         "docType": "eu.europa.ec.eudi.pid.1",
         "nameSpaces": {
           "eu.europa.ec.eudi.pid.1": {
             "given_name": false,
             "family_name": false,
             "personal_administrative_number": false
           }
         }
       }

  2. **Another Digital Credential from the catalog.** The Relying Party requests the claims defined by the schema of the Digital Credential published in the :ref:`registry:Digital Credentials Catalog`. The corresponding data model is defined by the related schema in the :ref:`registry:Schema Registry`.

     Example of a ``dcql_query`` in the remote flow for an mDL (``credential_type`` ``mDL``, mdoc-CBOR format, ``docType`` ``org.iso.18013.5.1.mDL``):

     .. code-block:: json

       {
         "credentials": [
           {
             "id": "mobile driving license",
             "format": "mso_mdoc",
             "meta": {
               "doctype_value": "org.iso.18013.5.1.mDL"
             },
             "claims": [
               {"path": ["org.iso.18013.5.1", "given_name"]},
               {"path": ["org.iso.18013.5.1", "family_name"]},
               {"path": ["org.iso.18013.5.1", "document_number"]}
             ]
           }
         ]
       }

.. note::
  In the case of using the batch Credential, the Wallet Instance SHOULD implement a Credential selection logic (e.g., based on the earliest expiring one) and MUST mark it as consumed. At the end of the flow it MUST decrease the number of available Credentials in the batch and using that it can control the time when it needs to obtain a new batch of Credentials.


.. toctree::
  :caption: Credential Presentation Table of Contents
  :maxdepth: 3

  remote-flow.rst
  proximity-flow.rst



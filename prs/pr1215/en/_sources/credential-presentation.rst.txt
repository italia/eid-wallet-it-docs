.. include:: ../common/common_definitions.rst


Digital Credential Presentation
================================

This section describes how a Relying Party Instance requests to a Wallet Instance the presentation of the PID/EAAs.

In this section the following flows are described:

- :ref:`remote-flow:Remote Flow`, where the User presents a Digital Credential to a web Relying Party Instance according to `OpenID4VP`_. In this scenario the user-agent and the Wallet Instance can be used in the same device (**Same Device Flow**), or in different devices (**Cross Device Flow**).
- :ref:`proximity-flow:Proximity Flow`, where the User presents a Digital Credential to a mobile Relying Party Instance according to `ISO18013-5`_. The User interacts with a Verifier using proximity connection technologies such as using QR Codes and Bluetooth Low Energy (BLE).

.. note::
  When a Relying Party needs to authenticate the User while distinguishing whether the User is of legal age or a minor, it MUST use one of the following options. In both cases the corresponding claim MUST be included in the presentation request:

  1. **Date of birth from the PID or the IT-Wallet ID.** The Relying Party MUST request the date of birth as part of the PID or IT-Wallet ID presentation (``birthdate`` in SD-JWT VC format, ``birth_date`` in mdoc-CBOR format). See :ref:`credential-data-model-pid:PID Data Model` and :ref:`credential-data-model-it-wallet-id:IT-Wallet ID Data Model`.

  2. **``age_over_18`` from the Age Attestation.** The Relying Party MUST request the ``age_over_18`` claim as part of the Age Attestation presentation. The Age Attestation is the Digital Credential published in the :ref:`registry:Digital Credentials Catalog` with ``credential_type`` ``av``. Its data model is defined by the corresponding schema in the :ref:`registry:Schema Registry` (mdoc-CBOR format, ``docType`` ``eu.europa.ec.av.1``). The ``age_over_18`` claim, in the ``eu.europa.ec.av.1`` namespace, attests whether the User is 18 years of age or older without disclosing the date of birth.

.. note::
  In the case of using the batch Credential, the Wallet Instance SHOULD implement a Credential selection logic (e.g., based on the earliest expiring one) and MUST mark it as consumed. At the end of the flow it MUST decrease the number of available Credentials in the batch and using that it can control the time when it needs to obtain a new batch of Credentials.


.. toctree::
  :caption: Credential Presentation Table of Contents
  :maxdepth: 3

  remote-flow.rst
  proximity-flow.rst



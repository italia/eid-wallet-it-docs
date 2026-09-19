.. include:: ../common/common_definitions.rst
.. Included via digital-credential-flows.rst at title level '=' (document title).


Digital Credential Presentation
================================

This section describes how a Relying Party Instance requests to a Wallet Instance the presentation of the PID/EAAs.

Presentation uses [`OpenID4VP`_] for the remote flow, profiled by [`OPENID4VC-HAIP`_], and [`ISO18013-5`_] for the proximity flow, as required by [`CIR2024/2982`_].
The applicable Trust Framework is selected as specified in :ref:`trust-evaluation:Selection at Presentation`.
A Wallet Unit that implements only the EUDIW procedures SHALL be able to present a PID, (Q)EAA or PuB-EAA to a Wallet-Relying Party of another Member State, as specified in :ref:`infrastructure-trust:Infrastructure of Trust`.
PID presentation before EUDIW notification is specified in :ref:`pid-until-notification`.

When an Embedded Disclosure Policy is stored with a Digital Credential, the Wallet Unit MUST evaluate it for the Credential and each requested attribute before User consent, display the results and any policy information link, and exclude or block every Credential or attribute with an unsatisfied result, as specified in :ref:`infrastructure-trust:Embedded Disclosure Policy (EDP)`. User approval MAY override ``EDP_NOT_SATISFIED``.

In this section the following flows are described:

- :ref:`remote-flow:Remote Flow`, where the User presents a Digital Credential to a web Relying Party Instance according to `OpenID4VP`_. In this scenario the user-agent and the Wallet Instance can be used in the same device (**Same Device Flow**), or in different devices (**Cross Device Flow**).
- :ref:`proximity-flow:Proximity Flow`, where the User presents a Digital Credential to a mobile Relying Party Instance according to `ISO18013-5`_. The User interacts with a Verifier using proximity connection technologies such as using QR Codes and Bluetooth Low Energy (BLE).

.. note::
  In the case of using the batch Credential, the Wallet Instance SHOULD implement a Credential selection logic (e.g., based on the earliest expiring one) and MUST mark it as consumed. At the end of the flow it MUST decrease the number of available Credentials in the batch and using that it can control the time when it needs to obtain a new batch of Credentials.


.. toctree::
  :caption: Credential Presentation Table of Contents
  :maxdepth: 3

  remote-flow.rst
  proximity-flow.rst


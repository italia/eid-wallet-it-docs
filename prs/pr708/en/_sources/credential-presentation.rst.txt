.. include:: ../common/common_definitions.rst


Digital Credential Presentation
================================

This section describes how a Relying Party Instance requests to a Wallet Instance the presentation of the PID/EAAs.

In this section the following flows are described:

- :ref:`remote-flow:Remote Flow`, where the User presents a Digital Credential to a web Relying Party Instance according to `OpenID4VP`_. In this scenario the user-agent and the Wallet Instance can be used in the same device (**Same Device Flow**), or in different devices (**Cross Device Flow**).
- :ref:`proximity-flow:Proximity Flow`, where the User presents a Digital Credential to a mobile Relying Party Instance according to `ISO18013-5`_. The User interacts with a Verifier using proximity connection technologies such as using QR Codes and Bluetooth Low Energy (BLE).



.. toctree::
  :caption: Credential Presentation Table of Contents
  :maxdepth: 3

  remote-flow.rst
  proximity-flow.rst

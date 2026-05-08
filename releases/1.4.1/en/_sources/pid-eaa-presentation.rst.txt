.. include:: ../common/common_definitions.rst

.. _pid-eaa-presentation.rst:

PID/(Q)EAA Presentation
++++++++++++++++++++++++

This section describes how a Relying Party Instance requests to a Wallet Instance the presentation of the PID/EAAs.

In this section the following flows are described:

- :ref:`Remote Flow`, where the User presents a Digital Credential to a web Relying Party Instance according to `OpenID4VP`_. In this scenario the user-agent and the Wallet Instance can be used in the same device (**Same Device Flow**), or in different devices (**Cross Device Flow**).
- :ref:`Proximity Flow`, where the User presents a Digital Credential to a mobile Relying Party Instance according to `ISO18013-5`_. The User interacts with a Verifier using proximity connection technologies such as using QR Codes and Bluetooth Low Energy (BLE).

.. include:: remote-flow.rst

.. include:: proximity-flow.rst


.. include:: ../common/common_definitions.rst
.. Included via digital-credential-flows.rst at title level '=' (document title).


Digital Credential Presentation
================================

This section describes how a Relying Party Instance requests a Wallet Instance to present the PID and the Electronic Attestations of Attributes.

The remote flow uses [`OpenID4VP`_], profiled by [`OPENID4VC-HAIP`_]. The proximity flow uses [`ISO18013-5`_]. [`CIR2024/2982`_] requires both flows.
The applicable Trust Framework is selected as specified in :ref:`trust-evaluation:Selection at Presentation`.
PID presentation before EUDIW notification is specified in :ref:`pid-until-notification`.
When an Embedded Disclosure Policy is stored with a Digital Credential, the Wallet Unit applies it before disclosure, as specified in :ref:`infrastructure-trust:Embedded Disclosure Policy (EDP)`.

In this section the following flows are described:

- :ref:`remote-flow:Remote Flow`, where the User presents a Digital Credential to a web Relying Party Instance. The user-agent and the Wallet Instance can be on the same device (**Same Device Flow**) or on different devices (**Cross Device Flow**).
- :ref:`proximity-flow:Proximity Flow`, where the User presents a Digital Credential to a mobile Relying Party Instance. The User interacts with a Verifier using proximity technologies such as QR Codes and Bluetooth Low Energy (BLE).

Identity matching, after cryptographic verification of a presented Digital Credential, is specified in :ref:`identity-matching`. Identity matching is not a presentation flow.
Offline presentation and the storage of the bound private keys are specified in :ref:`wallet-solution-requirements:Keystore Requirements`.

.. toctree::
  :caption: Credential Presentation Table of Contents
  :maxdepth: 3

  remote-flow.rst
  proximity-flow.rst
  identity-matching.rst


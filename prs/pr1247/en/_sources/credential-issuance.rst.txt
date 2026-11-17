.. include:: ../common/common_definitions.rst
.. Included via digital-credential-flows.rst at title level '=' (document title).


Digital Credential Issuance
============================

This section describes the PID and (Q)EAAs issuance flow with a high level of security.
The high-level flows are specified in :ref:`credential-issuance-high-level:Credential Issuance High-Level Flows`.

Issuance uses [`OpenID4VCI`_], profiled by [`OPENID4VC-HAIP`_], as required by [`CIR2024/2982`_], and is controlled by [`ETSI TS 119 472-3`_].
Support for the Authorization Code Grant is specified in :ref:`credential-issuance-low-level:Low-Level Issuance Flow`.
Where [`ETSI TS 119 472-3`_] requests it, the Wallet Unit supports the Pre-Authorized Code Grant.

The applicable Trust Framework is selected as specified in :ref:`trust-evaluation:Selection at Issuance`.

The scheme for Credential Offers in the EUDI Wallet flow is specified in :ref:`credential-issuance-low-level:Credential Offer Flow`.
PID issuance before EUDIW notification is specified in :ref:`pid-until-notification`.


.. toctree::
  :caption: Credential Issuance Table of Contents
  :maxdepth: 3

  credential-issuance-high-level.rst
  credential-issuance-low-level.rst
  credential-issuance-l2plus.rst


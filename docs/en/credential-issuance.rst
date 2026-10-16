.. include:: ../common/common_definitions.rst
.. Included via digital-credential-flows.rst at title level '=' (document title).


Digital Credential Issuance
============================

This section describes the PID and (Q)EAAs issuance flow with a high level of security.

Issuance uses [`OpenID4VCI`_], profiled by [`OPENID4VC-HAIP`_], as required by [`CIR2024/2982`_], and is controlled by [`ETSI TS 119 472-3`_].
The Wallet Unit MUST support the Authorization Code Grant.
Where [`ETSI TS 119 472-3`_] requests it, the Wallet Unit supports the Pre-Authorized Code Grant.
Each Credential Issuer MUST support the Authorization Code Grant.

The applicable Trust Framework is selected as specified in :ref:`trust-evaluation:Selection at Issuance`.

A Credential Issuer invoked through the EUDI Wallet flow MUST use the ``eu-eaa-offer://`` scheme for Credential Offers as profiled by [`ETSI TS 119 472-3`_].
PID issuance before EUDIW notification is specified in :ref:`pid-until-notification`.


.. toctree::
  :caption: Credential Issuance Table of Contents
  :maxdepth: 3

  credential-issuance-high-level.rst
  credential-issuance-low-level.rst
  credential-issuance-l2plus.rst


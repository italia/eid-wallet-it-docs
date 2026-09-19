.. include:: ../common/common_definitions.rst
.. Included via digital-credential-flows.rst at title level '=' (document title).


Digital Credential Issuance
============================

This section describes the PID and (Q)EAAs issuance flow with a high level of security.

Issuance uses [`OpenID4VCI`_], profiled by [`OPENID4VC-HAIP`_], as required by [`CIR2024/2982`_], and is controlled by [`ETSI TS 119 472-3`_] V1.1.1, clauses 4.1 through 4.3, where ETSI specializes or conflicts with OpenID4VCI or HAIP.
The Wallet Unit MUST support the Authorization Code Grant and possibly the Pre-Authorized Code Grant (as requested by [`ETSI TS 119 472-3`_]), and each Credential Issuer MUST support the Authorization Code Grant.

The applicable Trust Framework is selected as specified in :ref:`trust-evaluation:Selection at Issuance`; the EUDIW and National paths are mutually exclusive for each interaction, and a failed path MUST NOT be retried or supplemented with evidence from the other path.

A Credential Issuer invoked through the EUDI Wallet flow MUST use the ``eu-eaa-offer://`` scheme for Credential Offers as profiled by [`ETSI TS 119 472-3`_].
A Wallet Unit that implements only the EUDIW procedures SHALL be able to complete issuance of a PID, (Q)EAA or PuB-EAA of another Member State, as specified in :ref:`infrastructure-trust:Infrastructure of Trust`.
PID issuance before EUDIW notification is specified in :ref:`pid-until-notification`.


.. toctree::
  :caption: Credential Issuance Table of Contents
  :maxdepth: 3

  credential-issuance-high-level.rst
  credential-issuance-low-level.rst
  credential-issuance-l2plus.rst


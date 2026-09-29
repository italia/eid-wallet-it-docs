.. include:: ../common/common_definitions.rst
.. Included via digital-credential-flows.rst at title level '=' (document title).


Digital Credential Issuance
============================

This section describes the PID and (Q)EAAs issuance flow with a high level of security.

Issuance uses [`OpenID4VCI`_], profiled by [`OPENID4VC-HAIP`_], as required by [`CIR2024/2982`_].
The applicable Trust Framework is selected as specified in :ref:`trust-evaluation:Selection at Issuance`.
A Wallet Unit that implements only the EUDIW procedures SHALL be able to complete issuance of a PID, (Q)EAA or PuB-EAA of another Member State, as specified in :ref:`infrastructure-trust:Infrastructure of Trust`.
PID issuance before EUDIW notification is specified in :ref:`pid-until-notification`.


.. toctree::
  :caption: Credential Issuance Table of Contents
  :maxdepth: 3

  credential-issuance-high-level.rst
  credential-issuance-low-level.rst
  credential-issuance-l2plus.rst



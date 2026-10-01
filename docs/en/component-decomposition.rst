.. include:: ../common/common_definitions.rst
.. Included via appendix.rst at title level '=' (document title).


Component Decomposition
=======================

This annex decomposes the PID Provider and the Wallet Solution with the matrix used by the Agenzia per la Cybersicurezza Nazionale (ACN): scope, sub-components, certification scope, standards, risks, and controls.

The functional requirements stay in the sections cited by the Standards column. This annex does not restate them.


PID Provider
------------

The PID Provider is the Credential Issuer that issues the PID. The Authentic Source that supplies the PID attributes is outside the certification scope of the PID Provider. The PID Provider components that retrieve those attributes are inside that scope.

.. _table_pid_provider_decomposition:
.. list-table:: PID Provider decomposition
   :class: longtable
   :widths: 14 16 14 20 18 18
   :header-rows: 1

   * - **Scope**
     - **Sub-components**
     - **Certification scope**
     - **Standards**
     - **Risks**
     - **Controls**
   * - Identity proofing
     - User authentication for PID issuance
     - In scope
     - :ref:`credential-issuance-endpoint:User Authentication Method Selection`
     - Issuance to a User who has not been authenticated at the assurance required for the PID
     - User authentication for PID issuance, as specified in :ref:`credential-issuance-endpoint:User Authentication Method Selection`
   * - PID issuance
     - Credential Issuer component and Authorization Server
     - In scope
     - [`OpenID4VCI`_], [`ETSI TS 119 472-3`_], [`CIR2024/2982`_]
     - Issuance to a Wallet Unit that is not authentic, or whose PID key is not bound to that Wallet Unit
     - Wallet Instance Attestation and Key Attestation checks in :ref:`credential-issuance:Digital Credential Issuance`
   * - PID management
     - Lifecycle of the issued PID
     - In scope
     - :ref:`credential-revocation:Digital Credential Lifecycle`
     - Use of a PID that is expired, suspended, or no longer bound to the Wallet Instance
     - Expiry, suspension, and revocation in :ref:`credential-revocation:Digital Credential Lifecycle`
   * - PID status management
     - Publication of the Token Status List for the PID
     - In scope
     - `TOKEN-STATUS-LIST`_, :ref:`credential-revocation:Token Status List (Digital Credentials Profile)`
     - Presentation of a revoked PID
     - Status evaluation in :ref:`credential-revocation:Token Status List (Digital Credentials Profile)`
   * - Audit logging
     - Audit trail of PID issuance and lifecycle events
     - In scope
     - :ref:`log-retention-policy:General Log Retention Policies`
     - Misuse of the issuance service without a retained record
     - Audit logging required by :ref:`credential-issuer-solution:Credential Issuer Requirements` and :ref:`log-retention-policy:General Log Retention Policies`
   * - Authentic Sources interaction
     - Retrieval of PID attributes from the Authentic Source
     - In scope. The Authentic Source is out of scope
     - :ref:`authentic-sources:Authentic Sources`
     - Issuance of PID attributes that do not come from the Authentic Source
     - Retrieval through the Authentic Source interface in :ref:`authentic-sources:Authentic Sources`
   * - Signature device
     - Sign/Seal key used to sign the PID
     - In scope
     - :ref:`infrastructure-trust:X.509 Certificate Profile`, :ref:`infrastructure-trust:EUDIW Trust Artifacts`
     - A PID signed with a key that Relying Parties cannot anchor to the PID Provider
     - Sign/Seal trust anchor published in the PID Providers LoTE, as specified in :ref:`infrastructure-trust:EUDIW Trust Artifacts`


Wallet Solution
---------------

.. note::
   This table is non-normative. The ACN discussion of the Wallet Solution decomposition is still open. Certification scope, risks, and controls in this table become normative only after that discussion. Until then, the Wallet Solution requirements remain those in :ref:`wallet-solution-requirements:Wallet Solution Requirements` and :ref:`wallet-solution-components:Wallet Solution Components`.

The rows below name the sub-components already specified for the Wallet Solution. Wallet-to-Wallet interaction and qualified electronic signature creation are outside the scope of this version, as specified in :ref:`wallet-solution:Wallet Solution`.

.. _table_wallet_solution_decomposition:
.. list-table:: Wallet Solution decomposition
   :class: longtable
   :widths: 16 22 16 16 15 15
   :header-rows: 1

   * - **Scope**
     - **Sub-components**
     - **Certification scope**
     - **Standards**
     - **Risks**
     - **Controls**
   * - Wallet Backend
     - Frontend Component
     - Pending ACN discussion
     - :ref:`wallet-solution-components:Frontend Component`
     - Pending ACN discussion
     - Pending ACN discussion
   * - Wallet Backend
     - API Interface
     - Pending ACN discussion
     - :ref:`wallet-solution-components:API Interface`
     - Pending ACN discussion
     - Pending ACN discussion
   * - Wallet Backend
     - Wallet Instance Lifecycle Management
     - Pending ACN discussion
     - :ref:`wallet-solution-components:Wallet Instance Lifecycle Management`
     - Pending ACN discussion
     - Pending ACN discussion
   * - Wallet Backend
     - Trust and Security Component
     - Pending ACN discussion
     - :ref:`wallet-solution-components:Trust & Security Component`
     - Pending ACN discussion
     - Pending ACN discussion
   * - Wallet Unit
     - User Interface
     - Pending ACN discussion
     - :ref:`wallet-solution-components:User Interface`
     - Pending ACN discussion
     - Pending ACN discussion
   * - Wallet Unit
     - Wallet Instance Lifecycle Management Component
     - Pending ACN discussion
     - :ref:`wallet-solution-components:Wallet Instance Lifecycle Management Component`
     - Pending ACN discussion
     - Pending ACN discussion
   * - Wallet Unit
     - Issuer Component
     - Pending ACN discussion
     - :ref:`wallet-solution-components:Issuer Component`, [`OpenID4VCI`_]
     - Pending ACN discussion
     - Pending ACN discussion
   * - Wallet Unit
     - Presentation Component
     - Pending ACN discussion
     - :ref:`wallet-solution-components:Presentation Component`, [`OpenID4VP`_], [`ISO18013-5`_]
     - Pending ACN discussion
     - Pending ACN discussion
   * - Wallet Unit
     - Backup and Restore Component
     - Pending ACN discussion
     - :ref:`wallet-solution-components:Backup and Restore Component`
     - Pending ACN discussion
     - Pending ACN discussion
   * - Wallet Unit
     - Dashboard and Transaction Log
     - Pending ACN discussion
     - :ref:`wallet-solution-components:Dashboard and Transaction Log`
     - Pending ACN discussion
     - Pending ACN discussion
   * - Wallet Unit
     - Keystore
     - Pending ACN discussion
     - :ref:`wallet-solution-components:Keystore`
     - Pending ACN discussion
     - Pending ACN discussion
   * - Wallet Unit
     - WSCA/WSCD Interface
     - Pending ACN discussion
     - :ref:`wallet-solution-components:WSCA/WSCD Interface`
     - Pending ACN discussion
     - Pending ACN discussion

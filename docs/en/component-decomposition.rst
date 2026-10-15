.. include:: ../common/common_definitions.rst
.. Included via appendix.rst at title level '=' (document title).


Cybersecurity Component Decomposition
=====================================

This annex guides the EUDIW-IT-Cyber certification scheme of the Agenzia per la Cybersicurezza Nazionale (ACN). It decomposes the PID Provider and the Wallet Solution with the matrix of that scheme: scope, sub-components, certification scope, standards, risks, and controls. Certification scope follows Annex A of EUDIW-IT-Cyber draft v1.9.2.

The functional requirements stay in the sections cited by the Standards column. This annex does not restate them and does not add requirements.


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
   * - PID signature
     - Backend Crypto Module
     - In scope
     - :ref:`infrastructure-trust:X.509 Certificate Profile`, :ref:`infrastructure-trust:EUDIW Trust Artifacts`
     - A PID signed with a key that Relying Parties cannot anchor to the PID Provider
     - Sign/Seal trust anchor published in the PID Providers LoTE, as specified in :ref:`infrastructure-trust:EUDIW Trust Artifacts`
   * - Processes and ICT Systems
     - ICT systems and processes used to provide the PID
     - In scope
     - :ref:`credential-issuer-solution:Credential Issuer Requirements`
     - \-
     - As specified in :ref:`credential-issuer-solution:Credential Issuer Requirements`
   * - (Q)EAA Provider
     - Attribute attestation provider
     - Out of scope
     - \-
     - \-
     - \-
   * - Relying Party
     - Relying Party
     - Out of scope
     - \-
     - \-
     - \-
   * - Qualified signature or seal
     - Qualified signature or seal creation device
     - Out of scope
     - \-
     - \-
     - \-


Wallet Solution
---------------

This table guides EUDIW-IT-Cyber and does not add requirements. The Wallet Solution requirements remain those in :ref:`wallet-solution-requirements:Wallet Solution Requirements` and :ref:`wallet-solution-components:Wallet Solution Components`. Wallet-to-Wallet interaction and qualified electronic signature creation are outside this version of the specification, as specified in :ref:`wallet-solution-requirements:Wallet Solution Requirements`.

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
   * - Wallet Instance
     - User Interface
     - In scope
     - :ref:`wallet-solution-components:User Interface`
     - Addressed by the cited control
     - :ref:`wallet-solution-components:User Interface`
   * - Wallet Instance
     - Wallet Instance Lifecycle Management Component
     - In scope
     - :ref:`wallet-solution-components:Wallet Instance Lifecycle Management Component`
     - Addressed by the cited control
     - :ref:`wallet-solution-components:Wallet Instance Lifecycle Management Component`
   * - Wallet Instance
     - Issuer Component
     - In scope
     - :ref:`wallet-solution-components:Issuer Component`, [`OpenID4VCI`_]
     - Addressed by the cited control
     - :ref:`wallet-solution-components:Issuer Component`
   * - Wallet Instance
     - Presentation Component
     - In scope
     - :ref:`wallet-solution-components:Presentation Component`, [`OpenID4VP`_], [`ISO18013-5`_]
     - Addressed by the cited control
     - :ref:`wallet-solution-components:Presentation Component`
   * - Wallet Instance
     - Backup and Restore Component
     - In scope
     - :ref:`wallet-solution-components:Backup and Restore Component`
     - Addressed by the cited control
     - :ref:`wallet-solution-components:Backup and Restore Component`
   * - Wallet Instance
     - Dashboard and Transaction Log
     - In scope
     - :ref:`wallet-solution-components:Dashboard and Transaction Log`
     - Addressed by the cited control
     - :ref:`wallet-solution-components:Dashboard and Transaction Log`
   * - Wallet Instance
     - Signature Creation Application
     - In scope
     - \-
     - \-
     - This specification does not yet state that control
   * - Remote WSCD and WSCA
     - WSCA/WSCD Interface for the PID at Level of Assurance High
     - In scope
     - :ref:`wallet-solution-components:WSCA/WSCD Interface`
     - Addressed by the cited control
     - :ref:`wallet-solution-components:WSCA/WSCD Interface`
   * - Wallet Backend
     - Frontend Component (user web portal)
     - In scope
     - :ref:`wallet-solution-components:Frontend Component`
     - Addressed by the cited control
     - :ref:`wallet-solution-components:Frontend Component`
   * - Wallet Backend
     - API Interface
     - In scope
     - :ref:`wallet-solution-components:API Interface`
     - Addressed by the cited control
     - :ref:`wallet-solution-components:API Interface`
   * - Wallet Backend
     - Wallet Instance Lifecycle Management
     - In scope
     - :ref:`wallet-solution-components:Wallet Instance Lifecycle Management`
     - Addressed by the cited control
     - :ref:`wallet-solution-components:Wallet Instance Lifecycle Management`
   * - Wallet Backend
     - Trust & Security Component
     - In scope
     - :ref:`wallet-solution-components:Trust & Security Component`
     - Addressed by the cited control
     - :ref:`wallet-solution-components:Trust & Security Component`
   * - Wallet Backend
     - Fraud Detection
     - In scope
     - \-
     - \-
     - This specification does not yet state that control
   * - Wallet Backend
     - Backend Crypto Module
     - In scope
     - \-
     - \-
     - This specification does not yet state that control
   * - User device
     - Keystore
     - Out of scope
     - :ref:`wallet-solution-components:Keystore`
     - \-
     - The device Keystore is outside EUDIW-IT-Cyber. The Wallet Instance requirement for device-bound Credentials remains in :ref:`wallet-solution-components:Keystore`
   * - User device
     - Operating system and application stores
     - Out of scope
     - \-
     - \-
     - \-

.. include:: ../common/common_definitions.rst


Wallet Solution Components
==========================

Wallet Backend
--------------

Frontend Component
^^^^^^^^^^^^^^^^^^

The Frontend Component MUST provide a web-based User interface for Wallet Instance management, offering functionality to:

- Display and verify Wallet Instances and their status.
- Manage Wallet Instance lifecycle (e.g., revocation).
- Provide User support and documentation.

API Interface
^^^^^^^^^^^^^

This component MUST:

- forward the request from the Frontend Component or the Wallet Instance to the Wallet Instance Lifecycle Management component.
- use PDND according to rules in Section :ref:`e-service-pdnd:e-Service PDND` to be notified by the PID Provider of the need to revoke the Wallet Instance and delete the User's account due to the User's death.

Wallet Instance Lifecycle Management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This component MUST handle:

- Wallet Instance Registration (detailed in :ref:`wallet-instance-registration:Wallet Instance Initialization and Registration`).
- Wallet Attestation Issuance (detailed in :ref:`wallet-attestation-issuance:Wallet Attestation Issuance`).
- Status management (maintaining and updating validity).
- Revocation processes (implementing mechanisms to revoke Wallet Instances), according to Section :ref:`wallet-instance-revocation:Wallet Instance Revocation`.

Trust & Security Component
^^^^^^^^^^^^^^^^^^^^^^^^^^

This component MUST ensure security through:

- Key and certificate management.
- Audit logging.
- Security monitoring and incident response.
- Compliance with IT-Wallet Federation security requirements.



Wallet Unit
-----------

User Interface
^^^^^^^^^^^^^^

The User Interface is the point of interaction and communication between the User and the Wallet Instance.

Wallet Instance Lifecycle Management Component
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Interacting with the Wallet Backend, this component MUST handle:

- Wallet Instance Registration (detailed in :ref:`wallet-instance-registration:Wallet Instance Initialization and Registration`).
- Wallet Attestation Issuance (detailed in :ref:`wallet-attestation-issuance:Wallet Attestation Issuance`).
- Status management (maintaining and updating validity).
- Revocation processes (implementing mechanisms to revoke Wallet Instances), according to Section :ref:`wallet-instance-revocation:Wallet Instance Revocation`.

Based on the status of the Wallet Instance and the User request, this component interact with the other Wallet Instance components. 

Issuer Component
^^^^^^^^^^^^^^^^

Following the `OpenID4VCI`_ specification and the implementation profile in Section :ref:`credential-issuance:Digital Credential Issuance`, this component MUST implement the Digital Credential issuance protocols and flows to request Digital Credentials to Credential Issuers.

Presentation Component
^^^^^^^^^^^^^^^^^^^^^^

Following the implementation profile in Section :ref:`credential-presentation:Digital Credential Presentation`, this component MUST implement remote flows based on `OpenID4VP`_ and proximity flow based on `ISO18013-5`_ .

Backup and Restore Component
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For each Digital Credential that is issued to the Wallet Instance, this component MUST add all data that is necessary to request re-issuance of that Digital Credential as specified in Section :ref:`backup-restore:Backup and Restore`.

.. note::
   Currently the re-issuance of the PID is not managed by the Backup and Restore Component.


Secure Storage
^^^^^^^^^^^^^^

The Wallet Instance MUST use this component to protect critical assets and to securely execute cryptographic functions.


Wallet Solution Interaction Patterns
====================================

The Wallet Solution supports these interaction patterns:

1. **User to Wallet Backend Frontend**: Web-based interactions for Wallet Instance management.
2. **Wallet Instance to Wallet Backend API**: for Wallet Instance registration and Wallet Attestation issuance.
3. **PID Provider to Wallet Backend API**: Secure API calls to request Wallet Instance revocation.
4. **User to Wallet Instance User Interface**: for Digital Credential management (issuance, presentation, backup, restore, deletion).
5. **Wallet Intance to Relying Party**: for Digital Credential presentation.


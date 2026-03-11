.. include:: ../common/common_definitions.rst

.. _wallet-solution-components:

Wallet Solution Components
--------------------------

The following table describes the main components of the Wallet Solution.

.. list-table::
   :widths: 20 50 30
   :header-rows: 1

   * - **Component**
     - **Description**
     - **Reference**
   * - Mobile App
     - Primary interface for Users to access and manage digital assets.
     - Wallet Solution
   * - Wallet Instance
     - Installation of the Wallet Solution on a User's device.
     - Wallet Solution
   * - Wallet Provider
     - Entity that issues the Wallet Solution and Wallet Instance Attestations.
     - Trust Model
   * - Wallet Instance Attestation
     - Cryptographic proof of authenticity and integrity of the Wallet Instance.
     - Wallet Instance Attestation
   * - PID Provider
     - Issues Personal Identification Data to the Wallet Instance.
     - Trust Model
   * - (Q)EAA Provider
     - Issues Qualified or non-qualified Electronic Attestations of Attributes.
     - Trust Model
   * - Relying Party
     - Entity that accepts attestations from the Wallet Instance for authentication.
     - Relying Party Solution
   * - Trust Anchor
     - Root of trust in the federation.
     - Trust Model
   * - Federation Authority
     - Public governance entity for guidelines and accreditation.
     - Defined Terms

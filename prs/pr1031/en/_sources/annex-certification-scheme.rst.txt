.. include:: ../common/common_definitions.rst


.. _annex-certification-scheme:

Certification Scheme and Overall Approach
=========================================

This annex describes the certification scheme and overall approach for the IT-Wallet System, aligning the technical specifications with the component decomposition paradigm used for certification evaluation.

Certification Context: IT-Wallet System vs. EUDI-Wallet
-------------------------------------------------------

The **IT-Wallet System** is the national ecosystem enabling Digital Identity management and Credential exchange. A **EUDI-Wallet** is an IT-Wallet solution designated by the Member State as the national implementation of the European Digital Identity Wallet framework.

Certification per `CIR 2024/2981`_ applies **only when the IT-Wallet operates in the EUDI-Wallet context**. A Wallet Provider offering a solution exclusively within the IT-Wallet System (e.g., a private-sector wallet not designated as EUDI-Wallet) is not required to obtain certification. Conversely, once a solution is designated as the Italian EUDI-Wallet, it undergoes certification and retains that certified status also when operating as a public solution within the IT-Wallet System.

**Servizi ICT eID** and **Servizi ICT di Validazione** are unique elements identical in both ecosystems; they require certification in the EUDI-Wallet context and therefore carry that characteristic in the IT-Wallet System as well, even where certification is not otherwise mandated.

Regulatory Framework
--------------------

The certification of IT-Wallet System components is mandated by `CIR 2024/2981`_ (**Commission Implementing Regulation (EU) 2024/2981**). The regulation requires, under Article 4(4)(d), that risks, threats, and implemented controls be assessed as part of the certification process.

The decomposition follows:

- **`ARF`_** (Architecture Reference Framework) for EUDI-Wallet
- **IT-Wallet Technical Documentation** (this specification)
- **ENISA National Schema** template for certification documentation

Paradigm: Decomposition Hierarchy
----------------------------------

The decomposition paradigm structures the system into:

.. list-table:: Decomposition Hierarchy
   :widths: 25 75
   :header-rows: 1

   * - Level
     - Description
   * - Certification Macro-component
     - Top-level grouping (e.g. ICT Wallet Services, eID ICT Services); each has an owner (Wallet Provider, PID Provider).
   * - Component
     - Main architectural component (e.g. Wallet Instance, Wallet Provider Backend, PID Provider Backend).
   * - Sub-component
     - Sub-component with specific functional responsibility.
   * - Low-level sub-components
     - Optional further decomposition not tied to external standards.

Each element may be classified as an **ICT product** or an **ICT process**. The **Certification Scope** indicates whether the component is evaluated during certification (In scope / No).

Components In Scope for Certification
-------------------------------------

The following components are **in scope** for certification per `CIR 2024/2981`_:

.. list-table:: In-Scope Components
   :widths: 35 35 30
   :header-rows: 1

   * - Certification Macro-component
     - Owner
     - Technical Specification Reference
   * - **Servizi ICT Wallet**
     - Wallet Provider
     - :ref:`wallet-solution-components:Wallet Solution Components`
   * - **Servizi ICT eID**
     - PID Provider
     - :ref:`credential-issuer-solution:Credential Issuer Solution`
   * - **Servizi ICT di Validazione**
     - Validation Services Provider
     - :ref:`trust-infrastructure:The Infrastructure of Trust`
   * - **Regime di identificazione elettronica**
     - Cross-cutting (Wallet Provider and PID Provider)
     - National eID schemes (CIEid, SPID); :ref:`credential-issuance-l2plus:eID Substantial Authentication with MRTD Verification for PID Issuance`

Components Out of Scope for Certification
------------------------------------------

The following components are **out of scope** for certification:

.. list-table:: Out-of-Scope Components
   :widths: 40 60
   :header-rows: 1

   * - Component
     - Notes
   * - User Device (Operating System, platform, local crypto)
     - Provided by Device Manufacturer; not within the certification scope.
   * - Attribute Attestation Provider ((Pub/Q)EAA)
     - Certified under separate schemes.
   * - Authentic Source (AS)
     - External authoritative data sources.
   * - Relying Party (RP)
     - Consumer of Credentials; separate certification path.
   * - Qualified Signature/Seal Creation Device (QSCD)
     - Provided by QTSP under qualified trust services regulation.

Cross-Reference: Decomposition to Technical Specification
----------------------------------------------------------

The following table provides a consolidated cross-reference from decomposition elements to the relevant technical specification sections.

.. list-table:: Cross-Reference Table
   :widths: 30 45 25
   :header-rows: 1

   * - Decomposition Element
     - Technical Specification Section
     - Certification Macro-component
   * - Wallet Instance (WI)
     - :ref:`wallet-solution-components:Wallet Unit`
     - Servizi ICT Wallet
   * - Wallet Provider Backend (WPBE)
     - :ref:`wallet-solution-components:Wallet Backend`
     - Servizi ICT Wallet
   * - WSCD (WL3) / Cryptographic device (WL2) / WSCA
     - :ref:`wallet-solution-components:Secure Storage`
     - Servizi ICT Wallet
   * - PID Provider Backend (PPBE)
     - :ref:`credential-issuer-solution:Credential Issuer Solution`
     - Servizi ICT eID
   * - Identity Proofing (PPBE)
     - :ref:`credential-issuer-solution:Relying Party Component`, :ref:`credential-issuance-l2plus:eID Substantial Authentication with MRTD Verification for PID Issuance`
     - Servizi ICT eID
   * - Trust List Backend Services
     - :ref:`trust-infrastructure:The Infrastructure of Trust`
     - Servizi ICT di Validazione
   * - eID Scheme
     - National eID schemes; :ref:`credential-issuance:Digital Credential Issuance`
     - Regime di identificazione elettronica

Mandatory Certification
------------------------

The **Certification Scope** column in the decomposition tables (see :ref:`Decomposition and Certification Scope <wallet-solution-components-decomposition>` and :ref:`Decomposition and Certification Scope <credential-issuer-solution-decomposition>`) indicates whether security certification is required. The **eID Scheme** is always in scope for certification, as it is the cross-cutting element between Wallet Provider and PID Provider that triggers the certification requirement. Conditional cases include:

- **WSCD** (WL3 level) or cryptographic device (WL2 level) provided by the User or Wallet Provider (device ownership affects scope).
- **Wallet Instance** execution environment (User device vs. web-based interface).

Risk Assessment
---------------

The decomposition supports risk assessment per `CIR 2024/2981`_ Article 4(4)(d) through:

- **Risks (ID & Name)**: in compliance with `CIR 2024/2981`_ Annex I requirements.
- **Threats**: Identified per component.
- **Implemented controls**: Documented in the technical specifications and test plans.

For test coverage, see :ref:`Test Plans <test-plans>` and :ref:`Wallet Provider Test Plans <test-plans-wallet-provider>`.

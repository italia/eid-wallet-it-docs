.. include:: ../common/common_definitions.rst


.. _annex-certification-scheme:

Certification Scheme and Overall Approach
=========================================

This annex describes the certification scheme and overall approach for the IT-Wallet System, aligning the technical specifications with the component decomposition paradigm used for certification evaluation.

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
     - Top-level grouping (e.g. Servizi ICT Wallet, Servizi ICT PID Provider); each has an owner (Wallet Provider, PID Provider).
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
   * - **Servizi ICT PID Provider**
     - PID Provider
     - :ref:`credential-issuer-solution:Credential Issuer Solution`
   * - **Servizi ICT di Validazione** (Trust List Backend Services)
     - Validation Services Provider
     - :ref:`trust-infrastructure:The Infrastructure of Trust`
   * - **Regime di identificazione elettronica** (eID Scheme)
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
     - Provided by Device Manufacturer; not within certification scope.
   * - Attribute Attestation Provider ((Pub/Q)EAA)
     - Certified under separate schemes.
   * - Authentic Source (AS)
     - External authoritative data sources.
   * - Relying Party (RP)
     - Consumer of credentials; separate certification path.
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
   * - WSCD / WSCA
     - :ref:`wallet-solution-components:Secure Storage`
     - Servizi ICT Wallet
   * - PID Provider Backend (PPBE)
     - :ref:`credential-issuer-solution:Credential Issuer Solution`
     - Servizi ICT PID Provider
   * - Identity Proofing (PPBE)
     - :ref:`credential-issuer-solution:Relying Party Component`, :ref:`credential-issuance-l2plus:eID Substantial Authentication with MRTD Verification for PID Issuance`
     - Servizi ICT PID Provider
   * - Trust List Backend Services
     - :ref:`trust-infrastructure:The Infrastructure of Trust`
     - Servizi ICT di Validazione
   * - eID Scheme
     - National eID schemes; :ref:`credential-issuance:Digital Credential Issuance`
     - Regime di identificazione elettronica

Mandatory Certification
------------------------

The **Certification Scope** column in the decomposition tables (see :ref:`Decomposition and Certification Scope <wallet-solution-components-decomposition>` and :ref:`Decomposition and Certification Scope <credential-issuer-solution-decomposition>`) indicates whether security certification is required. Conditional cases include:

- **WSCD** provided by the User or Wallet Provider (device ownership affects scope).
- **Wallet Instance** execution environment (User device vs. web-based interface).
- **eID Scheme** as cross-cutting between Wallet Provider and PID Provider.

Risk Assessment
---------------

The decomposition supports risk assessment per `CIR 2024/2981`_ Article 4(4)(d) through:

- **Risks (ID & Name)**: in compliance with `CIR 2024/2981`_ Annex I requirements.
- **Threats**: Identified per component.
- **Implemented controls**: Documented in the technical specifications and test plans.

For test coverage, see :ref:`Test Plans <test-plans>` and :ref:`Wallet Provider Test Plans <test-plans-wallet-provider>`.

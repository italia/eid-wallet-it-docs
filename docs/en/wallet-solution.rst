.. include:: ../common/common_definitions.rst

.. "included" file, so we start with '-' title level

Wallet Solution
---------------

The Wallet Solution is issued by the Wallet Provider in the form of a mobile app and services, such as web interfaces. The mobile app serves as the primary interface for Users, allowing them to hold their Digital Credentials and interact with other participants of the ecosystem, such as Credential Issuers and Relying Parties. These Digital Credentials are a set of data that can uniquely identify a natural or legal person, along with other Qualified and non-qualified Electronic Attestations of Attributes, also known as QEAAs and EAAs respectively, or (Q)EAAs for short. Once a User installs the mobile app on their device, such an installation is referred to as a Wallet Instance for the User. By supporting the mobile app, the Wallet Provider ensures the security and reliability of the entire Wallet Solution, as it is responsible for issuing the Wallet App Attestation (WAA) and Wallet Unit Attestation (WUA). WAA proves the authenticity and integrity of the Wallet Instance, while WUA provides evidence that the keys used for Credential key binding are securely stored in a trustworthy WSCD. Additionally, WUA confirms that the Wallet Unit has not been revoked.

Architecture and Certification Decomposition
--------------------------------------------

The Wallet Solution architecture is described according to the certification macro-component **Servizi ICT Wallet** (owner: Wallet Provider). It comprises the following components and sub-components, all of which fall within certification scope:

- **Wallet Instance (WI)**:
  - Application Logic: User Interface, Issuer Component, Presentation Component, Wallet Instance Lifecycle Management
  - Local Data management: Local Data Store, Backup and Restore Component, Secure Storage interaction
  - Presentation Interface (PI): Remote and Proximity PID/(Pub/Q)EAA presentation (`OpenID4VP`_, `ISO18013-5`_)
  - Attestation Issuance Interface: PID Issuance Interface (PII), Attestation Issuance Interface (AII)

- **Wallet Secure Cryptographic Device (WSCD)**: Hardware Secure Element, WSCD Firmware, Secure Key Storage System

- **Wallet Secure Cryptographic Application (WSCA)**: WSCD Interface (WWI), WSCA Authentication, Cryptographic Keys and Functions Manager

- **Wallet Provider Backend (WPBE)**:
  - API Interface (incl. PDND for PID Provider notifications)
  - Wallet Instance Lifecycle Management: Registration, Attestation Issuance (WAA/WUA), Status and Revocation
  - Trust & Security Component: Key and Certificate Management, Audit Logging, Incident Response, Federation Compliance
  - User Web Portal (Frontend Component)

For the complete decomposition mapping and certification scope, see :ref:`Decomposition and Certification Scope <wallet-solution-components-decomposition>`.

The following diagram depicts the Wallet Solution High Level Architecture.

.. _fig_wallet-solution-high-level-architecture:
.. plantuml:: plantuml/wallet-solution-architecture.puml
    :width: 99%
    :alt: The image illustrates the Wallet Solution and its relations and interactions within the ecosystem.
    :caption: `Wallet Solution High Level Architecture. <https://www.plantuml.com/plantuml/svg/nLVVRo8t47xdht2vgkKaKYu7EH6fEHs1H4Mwqw4ZkJwkZ3tiMjcrjxOtX5RztsjxJRm_2BTvQXwIC9xvvlDuvhFvf3IMkiZIta-CaxIWW7wVJqRpIJGNMIuuSFsnr_iLBM3BEA3rwjloxcPTSTP5ZgaSZuZ8Ci4_7bdP2gxFy0wKoE3iOaH0QhPb16leu9qAyj31hL0WLPVa8kxYPj0UGNPmP3GYMD8Edl144inZY72gExXJK0zQv1qyCx5XwGzBEM9SQQOBpGHt1pelb1OPKdgVWkhDABr98GEkxt0ywCEJ1ibnsX-YdpVnNAH2NlNVNBeVQxF8thfBc0Rd9oG5wQsnX7t_RHCsbop3Sbz7FJ__CDtGJgXltcqcq-ca3Qo024vRq1_8PZpUTeEUuEdu_MKRMij2wJhiT3Q-dDvsWxsuU3--c1dOC4Cw0OI95b8Xp2awr1gflTAGgTuAf19yO5jwYFhtve-1xPTMb8YKCXwZ1OkPDa5p2THGPJXLDhao9TPmrNVpOBAk7MPqywG7RYCHvYGH5lVEVaGp-z7XVnD28x55sjctGZgUoxkpFt6QWaQtG45YspusZyQnkggqISXS6UzwVlBCD69A5I2LoHheesLfj5nEP_0pLqUNaEvDNQ8Sc_IWx8PA2revInVSC25rRAgO2Lx08oEc8bn3R0BsQ0tIMbuBN6y4NzsrIDqwseZ2DNBlslyps3cFI7aFaot4U4pqpt7KbHIFZ894rvWy0ASleszAXm3U32sJFDy9WrqURQNWkWowzV-YPuU-XO8DKcMHobQtlOmEOTR3Pp6hb3Ax5vo629r8KSG9miW2kLXc8kKM4q03sw7mXBCy1RHEn4wDleCqZGTgz0Lp78CwL679bSRS8BuDn-ILg7fANd7D2OLTvfJJ20wC3E7PQcdmF8c-Dy3PmSDP2fq8oVu6YgWVqb04OduhqvM7wy0sACKQ_nQeUIshawlU7ZM6EnQbR0jaJr8moHjRHfyFQwWiIkQFfjAxVs1EqtQra8IOAIrnsNJ6g0irTCSeuL6GXXHucGoCxKrRPUhrHm4fxFGyAz0lQErDlddQ30_d-G1xmw0YC9xF0HDbWZCjf2dg2MBsHM68_NjyPEuDmijZKfXLNsNlw-QYvSTy4Tiduln3KGeM-URmKX-wwsIpbfT-hRwbg5RWIa6jL_Lh3dovc7oVBvtcmry5AAsEtIP82zHMvzDjsZxqN88oVrspLAYjAkRZ15T3j5n_FP--En-VNVH3o8jSwtB_Qg9M08kyGl7Q6Mn_6MYbXOH0zBNWkt3A_yU8_cX6pImqo6eXSMp9kja4j2uD3NbVpsT3P7ulXkWBP4BkcyFgg91mJfsciZcO4bAt4PMmNFLwvfpzqwX-1PdXCNknoz7dXYgsLDpD62PQeHtJIOWAW5s2hfdbqlIhdNKp1hbCzmr-TMNqUt5FC2BtkHQnn7d221AvVu7vZJPWg68-zaLonzvWxOs54ZVboNMBnwxhJJVi47rS6Dglk3Q0Bs6WThhceIM2JxjIjUMMaZObn-kXdS6Z0FNDdOAf2k5Hg5Ew9BqkjN739BGkf33UtHeDcOhxchUVeetl5FuxWd_jYOt69czDfQgtjtq9PeRe9-2qoDB_0000>`_



.. toctree::
  :caption: Wallet Solution Table of Contents
  :maxdepth: 2

  wallet-solution-requirements.rst
  wallet-solution-components.rst
  wallet-instance.rst
  backup-restore.rst
  wallet-provider-entity-configuration.rst
  wallet-solution-metadata.rst


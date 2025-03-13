.. _wallet-revocation.rst:


Wallet Instance Revocation
--------------------------------

This section describes the involved entities and modalities to request a Wallet Instance revocation in the IT-Wallet system.

The Wallet Provider MUST ensure the security and reliability of Wallet Instances, keeping them updated and compliant with security requirements. When, for technical security reasons (e.g., relating to the compromise of cryptographic material) the security of the Wallet Instance is compromised, the Wallet Provider MUST revoke the Wallet Instance. 

As shown in :numref:`fig_Wallet_Instance_Revoc_Entities`, other actors MAY trigger the Wallet Instance revocation process:

- **Users**, connecting to the Wallet Provider’s web portal from their Wallet Instance or using an external browser.
- **PID Providers** when notified by the Authentic Source of the PID (ANPR) of the User’s death.
- **Legal Authorities or the Supervisory Body** in cases of proven illegal activities.


.. _fig_Wallet_Instance_Revoc_Entities:
.. figure:: ../../images/wallet_instance_revocation.svg
    :figwidth: 80%
    :align: center
    :target: https://www.plantuml.com/plantuml/uml/fL9TZn8z5BwVNt5URbusSPSRhxnQ5oOHuog1tHYJJIPbMk74JZksf-1e_E-UKmiguvqafFIXpyVvk8sa0gNELl-XQstI1lP4VNmncmLrlDaXxTCsHHDQxyWukcbzD-kjSiAvZgGjRcVpvzShWHxltymw5Sa4XfgvxthlXDEBVlLgkQYRpKEzhjyzV5ZLqwkgMfaGlPkA_ZEOFF8nuRDsX3I0FpfqEw2zWIVtNbbh29QEyxhMJ9XyvvFJAWpJO_wlYGCxTymlRpVvFhc2RnNmvnpdz1wBbZ0kr1cIxxroQcSYIBx_8ooGsw4ip8FHh8FAHixnL-q--0DghkealIh0IRhS8rnOWt8QZcOBR7d0reZ3zwhwPQ0IxSMyRQ9F8QT_UO9Waw6HXpGM5570RIA-ayzTNSQOJCYENQbKu8Eog6K0d8YI13YxD_MNdmbymAz6Drkl1mbmHY3F3aqyPTYaNWg9FWnmnw-ps-kaiKLbeH1fO9FVQiGSJ2fOBaQTowdZ7wdbcTnBr-Db0wjgRMpPiei1ZOSFQtFmhIBqZdz-PYyI2L4OSSUR9EHFvdAg4a84fB1_3J5UW7Extdh2ZuECMzRroMcZQ5-iHrCRPoZq9UCx6KvBU432dFxME9qw-mC0

    Entities involved in the Wallet Instance revocation process.

.. note::
   Detailed flows for **PID Provider, Legal Authorities,** and **Supervisory Body** will be covered in future versions of the technical specification.

Revocation Request from the User
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Users MAY request the Wallet Instance revocation by:

- *Selecting the revocation functionality from their Wallet Instance*: this functionality may be used by Users before changing their phone.
- *Using an external user agent*: this covers cases where Users lose their device, and so their access to their Wallet Instance.

In both cases, by using the Wallet Provider portal:

- Users MUST authenticate with at least a second-factor authentication mechanism, or have an active session that meets this requirement. 
- The Wallet Provider MUST allow Users to view the state of all their Wallet Instances and ask for their revocation.

Revocation Check Mechanisms
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The verification of the Wallet Instance validity MUST be performed:

- **During Digital Credential issuance or presentation phase** by the Credential Issuers and Relying Parties, respectively. Only Wallet Instances in Operational or Valid state have valid Wallet Attestations. Thus, the verification of the validity of a Wallet Instance is indirectly performed by Credential Issuers and Relying Parties by checking the presence of valid Wallet Attestation (i.e. not expired and signed by a trusted Wallet Provider). 

- **During the validity period of the Digital Credential**  by the Credential Issuers. Indeed, if the Wallet Instance is revoked, the PID hosted within it MUST be revoked. Any other Digital Credential obtained through the presentation of the PID MUST therefore be revoked too. In the current version of the specification, Credential Issuers are directly notified of a Wallet Instance revocation by the Wallet Provider using a PDND e-service.


.. note::
   With the introduction of the **Wallet Trust Evidence (WTE)**, this section will be updated accordingly.



.. include:: ../common/common_definitions.rst

.. level 2 "included" file, so we start with '^' title level

Wallet Solution Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section lists the requirements for the Wallet Solution, structured along the certification decomposition defined in :ref:`wallet-solution:Wallet Solution` and :ref:`Decomposition and Certification Scope <wallet-solution-components-decomposition>`. Requirements apply to the **Wallet Instance (WI)**, **Wallet Provider Backend (WPBE)**, **Wallet Secure Cryptographic Device (WSCD)**, and **Wallet Secure Cryptographic Application (WSCA)** components of the certification macro-component **Servizi ICT Wallet**.

.. list-table::
   :widths: 8 55 37
   :header-rows: 1

   * - Req. ID
     - Requirement
     - Certification scope
   * - WS-001
     - The Wallet Solution MUST adhere to the specifications set by this document for obtaining Personal Identification (PID) and (Q)EAAs.
     - WI, WPBE, WSCD, WSCA
   * - WS-002
     - The Wallet Provider MUST expose a set of endpoints, exclusively available to its Wallet Solution instances, supporting the core functionalities of the Wallet Instances.
     - WPBE
   * - WS-003
     - The Wallet Instance MUST periodically reestablish trust with its Wallet Provider, obtaining a fresh Wallet App Attestation (:ref:`WP_018 <wallet-instance-testcases>`).
     - WI
   * - WS-004
     - The Wallet Instance MUST establish trust with other participants of the Wallet ecosystem, such as Credential Issuers. In case of Credential Issuers, Wallet Instance presents both Wallet App and Wallet Unit Attestations.
     - WI
   * - WS-005
     - The Wallet Instance MUST be compatible and functional on both Android and iOS operating systems and available on the Play Store and App Store, respectively (:ref:`WP_015 <wallet-instance-testcases>`).
     - WI
   * - WS-006
     - The Wallet Instance MUST provide a mechanism to verify the User's actual possession and full control of their personal device.
     - WI
   * - WS-007
     - The Wallet Instance MUST provide Users with an up-to-date list of Relying Parties with which the User has established a connection and, where applicable, all data exchanged.
     - WI
   * - WS-008
     - The Wallet Instance MUST provide Users with a mechanism to request the erasure of personal attributes by a Relying Party pursuant to Article 17 of `Regulation (EU) 2016/679`_, and to log each Erasure Request made.
     - WI

.. note::
   There is no strict one-to-one mapping between the requirements in this section and the test cases in :ref:`wallet-provider-test-matrix`. Some requirements are expressed at too high a level to be represented as atomic test cases, while others are already addressed in greater detail within related flows (e.g., :ref:`wallet-attestation-issuance:Wallet App and Wallet Unit Attestation Issuance`).

Wallet App Attestation Requirements
""""""""""""""""""""""""""""""""""""

The Wallet App Attestation is issued by the **Wallet Provider Backend (WPBE)** as part of the Wallet Instance Lifecycle Management sub-component (see :ref:`Decomposition and Certification Scope <wallet-solution-components-decomposition>`). It contains information regarding the security level of the device hosting the Wallet Instance.
It primarily proves the **authenticity**, **integrity**, **security**, and in general the **trustworthiness** of a particular Wallet Instance.

The requirements for the Wallet App Attestation are defined below:

.. list-table::
   :widths: 8 55 37
   :header-rows: 1

   * - Req. ID
     - Requirement
     - Certification scope
   * - WAA-001
     - The Wallet App Attestation MUST provide all the relevant information to attest to the **integrity** and **security** of the device where the Wallet Instance is installed (:ref:`WP_019 <wallet-instance-testcases>`).
     - WPBE
   * - WAA-002
     - The Wallet App Attestation MUST be signed by the Wallet Provider that has authority over and is the owner of the Wallet Solution, as specified by the overseeing Registration Authority. This ensures that the Wallet App Attestation uniquely links the Wallet Provider to this particular Wallet Instance (:ref:`WP_020 <wallet-instance-testcases>`).
     - WPBE
   * - WAA-003
     - The Wallet Provider MUST periodically evaluate and guarantee the integrity, the authenticity, and the genuineness of the Wallet Instance. The Wallet Provider verifies the Wallet Instance using the most secure flow made available by OS Provider's API, such as the *Play Integrity API* for Android and *App Attest* for iOS (:ref:`WP_011 <wallet-provider-backend-testcases>`).
     - WPBE
   * - WAA-004
     - The Wallet Provider MUST possess a revocation mechanism for the Wallet Instance, allowing the Wallet Provider to terminate service for a specific Instance at any time (:ref:`WP_011 <wallet-provider-backend-testcases>`).
     - WPBE
   * - WAA-005
     - The Wallet App Attestation MUST be securely bound to the Wallet Instance's ephemeral public key (:ref:`WP_019b <wallet-instance-testcases>`).
     - WPBE
   * - WAA-006
     - The Wallet App Attestation MAY be used multiple times during its validity period, allowing for repeated authentication and authorization without the need to request new attestations with each interaction. However, it is RECOMMENDED that Wallet Instances avoid using the same attestation repeatedly, due to privacy concerns such as linkability between different interactions.
     - WI
   * - WAA-007
     - The Wallet App Attestation MUST be short-lived and MUST have an expiration time, after which it MUST no longer be considered valid.
     - WPBE
   * - WAA-008
     - The Wallet App Attestation MUST NOT be issued by the Wallet Provider if the authenticity, integrity, and genuineness of the Wallet Instance requesting it cannot be guaranteed (:ref:`WP_019a <wallet-instance-testcases>`).
     - WPBE
   * - WAA-009
     - Each Wallet Instance SHOULD be able to request multiple Wallet App Attestations using different cryptographic public keys associated with them.
     - WI
   * - WAA-010
     - The Wallet App Attestation MUST NOT contain information about the User in control of the Wallet Instance (:ref:`WP_029b <wallet-instance-testcases>`).
     - WPBE
   * - WAA-011
     - The Wallet Instance MUST secure a Wallet App Attestation as a prerequisite for transitioning to the Operational state, as defined by `EIDAS-ARF`_.
     - WI
   * - WAA-012
     - A Wallet Provider SHALL ensure that a non-revoked Wallet Unit at all times presents a temporally valid and non-revoked Wallet App Attestation to a PID Provider or Attestation Provider during the issuance process of a PID or attestation. Note: This requirement applies to both device-bound and non-device-bound attestations, as defined by `EIDAS-ARF`_.
     - WPBE
   * - WAA-013
     - A Wallet Unit SHALL present a Wallet App Attestation only to a PID Provider or Attestation Provider, as part of the issuance process of a PID or an attestation, and not to a Relying Party or any other entity.
     - WI


.. note::
  Throughout this section, the services used to attest genuineness of the Wallet Instance and the device in which it is installed are referred to as **Device Integrity Service API**. The Device Integrity Service API is considered in an abstract fashion and it is assumed to be a service provided by a trusted third party (i.e., the OS Provider's API) which is able to perform integrity checks on the Wallet Instance as well as on the device where it is installed.


Wallet Unit Attestation Requirements
""""""""""""""""""""""""""""""""""""

The Wallet Unit Attestation is issued by the **Wallet Provider Backend (WPBE)** and attests to the properties of the **Wallet Secure Cryptographic Application (WSCA)** and **Wallet Secure Cryptographic Device (WSCD)** (see :ref:`Decomposition and Certification Scope <wallet-solution-components-decomposition>`). It contains information to ensure that keys used for Digital Credential key binding are stored in a **trustworthy** WSCD. It also provides a method to authenticate the WSCD with the Credential Issuer and verifies that the Wallet Unit has not been revoked.

The requirements for the Wallet Unit Attestation are defined below:

.. list-table::
   :widths: 8 55 37
   :header-rows: 1

   * - Req. ID
     - Requirement
     - Certification scope
   * - WUA-001
     - The Wallet Unit Attestation SHALL provide a PID Provider or Attestation Provider with information about the capabilities of the WSCA and WSCD of the Wallet Unit, such that they are able to take a well-grounded decision on whether to issue a PID or attestation to the Wallet Unit.
     - WPBE
   * - WUA-002
     - The Wallet Unit Attestation SHALL enable PID Providers and Attestation Providers to verify the authenticity and revocation status of the Wallet Unit.
     - WPBE
   * - WUA-003
     - A Wallet Provider SHALL ensure that a non-revoked Wallet Unit at all times can present a Wallet Unit Attestation, when requested by a PID Provider or Attestation Provider.
     - WPBE
   * - WUA-004
     - During issuance of a PID, the Wallet Unit SHALL provide the PID Provider with a valid WUA describing the WSCA/WSCD that generated the new PID private key. Note: A PID private key is always generated and managed by the WSCA/WSCD, which by definition complies with requirements for Level of Assurance High. During issuance of a device-bound attestation, a Wallet Unit SHALL retrieve the requirements of the Attestation Provider regarding key storage by the WSCA/WSCD from the Issuer metadata (as specified in `OpenID4VCI`_). The Wallet Unit SHALL determine which of its WSCA/WSCD(s) or keystore(s), if any, comply with these requirements. If a compliant WSCA/WSCD or keystore is available, the Wallet Unit SHALL provide the Attestation Provider with a valid WUA describing the selected WSCA/WSCD or keystore. Note: A WUA describes the properties of the WSCA/WSCD or keystore and contains one or more public key(s) corresponding to private key(s) generated by and stored in that WSCA/WSCD or keystore.
     - WI, WSCA, WSCD
   * - WUA-005
     - If a Wallet Unit contains multiple WSCAs, it SHALL, internally and securely, keep track of which PIDs and attestations are bound to which WSCA.
     - WI, WSCA
   * - WUA-006
     - A Wallet Unit SHALL present a Wallet Unit Attestation only as part of the issuance of a PID or a key-bound attestation.
     - WI
   * - WUA-007
     - The Wallet Unit Attestation SHALL enable PID Providers to request a Wallet Provider to revoke a Wallet Unit, by including an identifier for the Wallet Unit in the WUA (e.g., a URI and index to an Attestation Status List). The Wallet Provider SHALL ensure that this Wallet Unit identifier does not enable tracking of the User.
     - WPBE
   * - WUA-008
     - The Wallet Unit Attestation MUST contain one or multiple attested credential's public key that are coming from the same WSCD.
     - WPBE
   * - WUA-009
     - The Wallet Unit Attestation MUST be signed by the Wallet Provider that has authority over and is the owner of the Wallet Solution, as specified by the overseeing Registration Authority. Wallet Providers SHALL ensure that the certificates they use for signing WUAs and WAAs comply with all applicable requirements in `ETSI TS 119 412-6`_, in particular Clause 5.
     - WPBE
   * - WUA-010
     - The Wallet Unit Attestation MUST NOT be issued by the Wallet Provider if the WSCD trustworthiness is not guaranteed. In this case, the Wallet Instance MUST be revoked.
     - WPBE, WI
   * - WUA-011
     - An Attestation Provider issuing non-device-bound attestations SHALL indicate in its Credential Issuer metadata that it does not need a WUA. A Wallet Unit SHALL NOT send a WUA to an Attestation Provider when requesting a non-device-bound attestation. Note: A Wallet Unit sends a WIA to the Attestation Provider regardless of whether the attestations it issues are device-bound or not.
     - WPBE
   * - WUA-012
     - A Wallet Provider SHALL ensure that the presentation of a WUA is cryptographically bound to the specific context it is intended to be used in. Note: As specified in `OpenID4VCI`_, this is achieved by letting the signed WUA itself contain a nonce provided by the PID Provider or Attestation Provider during the issuance process. Alternatively, the Wallet Unit presents the WUA along with a Proof-of-Possession consisting of a signature over that nonce, created by the private key corresponding to one of the public keys attested in the WUA.
     - WPBE
   * - WUA-013
     - During issuance of a PID or a device-bound attestation, the PID Provider or Attestation Provider SHALL verify the WUA in accordance with the requirements in `OpenID4VCI`_ Appendix F.4.
     - -
   * - WUA-014
     - During issuance of a PID or a device-bound attestation, the PID Provider or Attestation Provider SHALL receive a proof that the Wallet Unit possesses the private keys corresponding to all public keys in the WUA.
     - -
   * - WUA-015
     - If the WSCA/WSCD is able to export a private key, the Wallet Provider SHALL specify this capability as an attribute in the WUA.
     - WPBE
   * - WUA-016
     - A Wallet Provider SHALL consider all relevant factors, including offline usage, interoperability, and the risk of a WUA becoming a vector to track the User, when deciding on the validity period of a WUA.
     - WPBE


WSCD Requirements
""""""""""""""""""

The **Wallet Secure Cryptographic Device (WSCD)** includes the Hardware Secure Element, WSCD Firmware, and Secure Key Storage System (see :ref:`Decomposition and Certification Scope <wallet-solution-components-decomposition>`). To guarantee the utmost security, the cryptographic keys associated with a Wallet Instance (e.g., used to generate the Wallet App Attestation) MUST be securely generated and stored within the WSCD. Only the legitimate User can access the private cryptographic keys, preventing unauthorized usage or tampering. The WSCD MAY be implemented using at least one of the approaches listed below:

.. list-table::
   :widths: 8 55 37
   :header-rows: 1

   * - Req. ID
     - Requirement
     - Certification scope
   * - WSCD-001
     - The cryptographic keys associated with a Wallet Instance MUST be securely generated and stored within the WSCD.
     - WSCD
   * - WSCD-002
     - **Local Internal WSCD**: The WSCD relies entirely on the device's native cryptographic hardware, such as the Secure Enclave on iOS, or the Trusted Execution Environment (TEE) and Strongbox on Android.
     - WSCD
   * - WSCD-003
     - **Local External WSCD**: The WSCD is hardware external to the User's device, such as a smart card compliant with *GlobalPlatform* and supporting *JavaCard*.
     - WSCD
   * - WSCD-004
     - **Remote WSCD**: The WSCD utilizes a remote Hardware Security Module (HSM).
     - WSCD
   * - WSCD-005
     - **Local Hybrid WSCD**: The WSCD involves a pluggable internal hardware component within the User's device, such as an *eUICC* that adheres to *GlobalPlatform* standards and supports *JavaCard*.
     - WSCD
   * - WSCD-006
     - **Remote Hybrid WSCD**: The WSCD involves a local component mixed with a remote service.
     - WSCD

.. _wscd-security-levels:

.. warning::
  At the current stage, the implementation profile defined in this document supports only the Local Internal WSCD (:ref:`WP_014 <wallet-instance-testcases>`).
  Future versions of this specification MAY include other approaches depending on the required Authenticator Assurance Level (AAL).

  The WSCD operates at two security levels:
  - **WL3 WSCD**: certified as resistant against attackers with a high attack potential (e.g., HSM, smart card certified at least Common Criteria EAL4+ AVA_VAN.5). Keys bound to PID and WUA WL3 MUST be stored in a WL3 WSCD.
  - **WL2 WSCD**: based on hardware environments not easily certifiable against high attack potential (e.g., TEE). Keys bound to NPID, (Pub/Q)EAA, EAA, and WUA WL2 MAY be stored in a WL2 WSCD.
  
  The WL3 WSCD MAY also be used to store private keys corresponding to WL2 Digital Credentials, provided that each Digital Credential has its own distinct key. The WL2 WSCD MUST NOT be used to host PID keys under any circumstance.
  
  For more detailed information, please refer to :ref:`wallet-instance-registration:Wallet Instance Initialization and Registration` and :ref:`wallet-attestation-issuance:Wallet App and Wallet Unit Attestation Issuance` of this document.



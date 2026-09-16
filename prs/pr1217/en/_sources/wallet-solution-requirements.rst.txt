.. include:: ../common/common_definitions.rst
.. Included via wallet-solution.rst at title level '^' (level 2).

Wallet Solution Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section lists the requirements about Wallet Providers and Wallet Solutions with their Wallet Instances, as well as the corresponding Wallet Instance Attestation, Key Attestation and the secure storage component (WSCD or Keystore).

- The Wallet Solution MUST adhere to the specifications set by this document for obtaining Personal Identification (PID) and (Q)EAAs.
- The Wallet Provider MUST expose a set of endpoints, exclusively available to its Wallet Solution instances, supporting the core functionalities of the Wallet Instances.
- The Wallet Instance MUST periodically reestablish trust with its Wallet Provider, obtaining a fresh Wallet Instance Attestation (:ref:`WP_018 <wallet-instance-testcases>`).
- The Wallet Instance MUST establish trust with other participants of the Wallet ecosystem, such as Credential Issuers. In case of Credential Issuers, Wallet Instance presents both Wallet Instance and Key Attestations.
- The Wallet Instance MUST be compatible and functional on both Android and iOS operating systems and available on the Play Store and App Store, respectively (:ref:`WP_015 <wallet-instance-testcases>`).
- The Wallet Instance MUST provide a mechanism to verify the User's actual possession and full control of their personal device.
- The Wallet Instance MUST provide Users with an up-to-date list of Relying Parties with which the User has established a connection and, where applicable, all data exchanged;
- The Wallet Instance MUST provide Users with a mechanism to request the erasure of personal attributes by a Relying Party pursuant to Article 17 of Regulation (EU) 2016/679, and to log each Erasure Request made.

.. note::
   There is no strict one-to-one mapping between the requirements in this section and the test cases in :ref:`test-plans-wallet-provider:Wallet Provider Test Matrix`. Some requirements are expressed at too high a level to be represented as atomic test cases, while others are already addressed in greater detail within related flows (e.g., :ref:`wallet-instance-attestation-issuance:Wallet Instance Attestation Issuance`).

Wallet Instance Attestation Requirements
"""""""""""""""""""""""""""""""""""""""""

Wallet Instance Attestation contains information regarding the security level of the device hosting the Wallet Instance.
It primarily proves the **authenticity**, **integrity**, **security**, and in general the **trustworthiness** of a particular Wallet Instance.

The requirements for the Wallet Instance Attestation are defined below:

- The Wallet Instance Attestation MUST provide all the relevant information to attest to the **integrity** and **security** of the device where the Wallet Instance is installed  (:ref:`WP_019 <wallet-instance-testcases>`).
- The Wallet Instance Attestation MUST be signed by the Wallet Provider that has authority over and is the owner of the Wallet Solution, as specified by the overseeing Registration Authority. This ensures that the Wallet Instance Attestation uniquely links the Wallet Provider to this particular Wallet Instance (:ref:`WP_020 <wallet-instance-testcases>`).
- The Wallet Provider MUST periodically evaluate and guarantee the integrity, the authenticity, and the genuineness of the Wallet Instance. The Wallet Provider verifies the Wallet Instance using the most secure flow made available by OS Provider's API, such as the *Play Integrity API* for Android and *App Attest* for iOS (:ref:`WP_011 <wallet-provider-backend-testcases>`).
- The Wallet Instance Attestation MUST be securely bound to the Wallet Instance's ephemeral public key (:ref:`WP_019b <wallet-instance-testcases>`).
- The Wallet Instance Attestation MAY be used multiple times during its validity period, allowing for repeated authentication and authorization without the need to request new attestations with each interaction. However, it is RECOMMENDED that Wallet Instances avoid using the same attestation repeatedly, due to privacy concerns such as linkability between different interactions.
- The Wallet Instance Attestation MUST have an expiration time (``exp``) that is at most 24 hours after issuance (``iat``), after which it MUST no longer be considered valid (:ref:`WP_028 <wallet-instance-testcases>`, :ref:`WP_144 <wallet-instance-optional-testcases>`).
- The Wallet Instance Attestation MUST NOT be issued by the Wallet Provider if the authenticity, integrity, and genuineness of the Wallet Instance requesting it cannot be guaranteed (:ref:`WP_019a <wallet-instance-testcases>`).
- Each Wallet Instance SHOULD be able to request multiple Wallet Instance Attestations using different cryptographic public keys associated with them.
- The Wallet Instance Attestation MUST NOT contain information about the User in control of the Wallet Instance (:ref:`WP_029b <wallet-instance-testcases>`).
- The Wallet Instance MUST secure a Wallet Instance Attestation as a prerequisite for transitioning to the Operational state, as defined by `EIDAS-ARF`_.
- A Wallet Provider SHALL ensure that a non-revoked Wallet Unit at all times presents a temporally valid and non-revoked Wallet Instance Attestation to a PID Provider or Attestation Provider during the issuance process of a PID or attestation. Note: This requirement applies to both device-bound and non-device-bound attestations, as defined by `EIDAS-ARF`_.
- A Wallet Unit SHALL present a Wallet Instance Attestation only to a PID Provider or Attestation Provider, as part of the issuance process of a PID or an attestation, and not to a Relying Party or any other entity.

.. note::
  Throughout this section, the services used to attest genuineness of the Wallet Instance and the device in which it is installed are referred to as **Device Integrity Service API**. The Device Integrity Service API is considered in an abstract fashion and it is assumed to be a service provided by a trusted third party (i.e., the OS Provider's API) which is able to perform integrity checks on the Wallet Instance as well as on the device where it is installed.


Key Attestation Requirements
""""""""""""""""""""""""""""""""""""

Key Attestation contains information to ensure that keys used for Digital Credential key binding are stored in a **trustworthy** WSCD or Keystore. It also provides a method to authenticate that storage component with the Credential Issuer and verifies that the Wallet Unit has not been revoked.

The requirements for the Key Attestation are defined below:

- The Key Attestation SHALL provide a PID Provider or Attestation Provider with information about the capabilities of the WSCA and WSCD of the Wallet Unit, such that they are able to take a well-grounded decision on whether to issue a PID or attestation to the Wallet Unit.
- The Key Attestation SHALL enable PID Providers and Attestation Providers to verify the authenticity and revocation status of the Wallet Unit.
- A Wallet Provider SHALL ensure that a non-revoked Wallet Unit at all times can present a Key Attestation, when requested by a PID Provider or Attestation Provider.
- During issuance of a PID at Level of Assurance High, the Wallet Unit SHALL provide the PID Provider with a valid Key Attestation (KA) describing the WSCD that generated the new PID private key. PID keys at LoA High MUST be generated and stored only in a WSCD. The current implementation profile does not include PID High issuance; IT-Wallet ID and (Q)EAA keys MAY be generated and stored in a Keystore.
- During issuance of device-bound attestation, a Wallet Unit SHALL retrieve the requirements of the Attestation Provider regarding key storage by the WSCA/WSCD or Keystore from the Issuer metadata (as specified in `OpenID4VCI`_). The Wallet Unit SHALL determine which of its WSCA/WSCD or Keystore instances, if any, comply with these requirements.  If a compliant WSCA/WSCD or Keystore is available to the Wallet Unit, the Wallet Unit SHALL provide the Attestation Provider with a valid KA describing the selected WSCA/WSCD or Keystore. Note: A KA describes the properties of the WSCA/WSCD or Keystore and contains one or more public key(s) corresponding to private key(s) generated by and stored in that WSCA/WSCD or Keystore.
- If a Wallet Unit contains multiple WSCAs, it SHALL, internally and securely, keep track of which PIDs and attestations are bound to which WSCA.
- A Wallet Unit SHALL present a Key Attestation only as part of the issuance of a PID or a key-bound attestation.
- The Key Attestation SHALL enable PID Providers to request a Wallet Provider to revoke a Wallet Unit, by including an identifier for the Wallet Unit in the KA (e.g., a URI and index to an Attestation Status Lis). The Wallet Provider SHALL ensure that this Wallet Unit identifier does not enable tracking of the User.
- The Key Attestation MUST contain one or multiple attested credential's public key that are coming from the same WSCD or Keystore.
- The Key Attestation MUST be signed by the Wallet Provider that has authority over and is the owner of the Wallet Solution, as specified by the overseeing Registration Authority. Wallet Providers SHALL ensure that the certificates they use for signing KAs and WIAs comply with all applicable requirements in `ETSI TS 119 412-6`_, in particular Clause 5.
- An Attestation Provider issuing non-device-bound attestations SHALL indicate in its Credential Issuer metadata that it does not need a KA. A Wallet Unit SHALL NOT send a KA to an Attestation Provider when requesting a non-device-bound attestation. Note: A Wallet Unit sends a WIA to the Attestation Provider regardless of whether the attestations it issues are device-bound or not.
- A Wallet Provider SHALL ensure that the presentation of a KA is cryptographically bound to the specific context it is intended to be used in. Note: As specified in `OpenID4VCI`_, this is achieved by letting the signed KA itself contain a nonce provided by the PID Provider or Attestation Provider during the issuance process. Alternatively, the Wallet Unit presents the KA along with a Proof-of-Possession consisting of a signature over that nonce, created by the private key corresponding to one of the public keys attested in the KA.
- During issuance of a PID or a device-bound attestation, the PID Provider or Attestation Provider SHALL verify the KA in accordance with the requirements in `OpenID4VCI`_ Appendix F.4.
- During issuance of a PID or a device-bound attestation, the PID Provider or Attestation Provider SHALL receive a proof that the Wallet Unit possesses the private keys corresponding to all public keys in the KA.
- The WSCA, WSCD or Keystore MUST NOT allow export of User private keys in clear. If a device reports a private key as exportable, the Wallet Provider MUST reject the Key Attestation and MUST NOT activate the Wallet Instance (:ref:`WP_014b <wallet-instance-testcases>`).
- A Wallet Provider SHALL consider all relevant factors, including offline usage, interoperability, and the risk of a KA becoming a vector to track the User, when deciding on the validity period of a KA.
- The Key Attestation MUST NOT be issued by the Wallet Provider if the trustworthiness of the WSCD or Keystore is not guaranteed. In this case, the Wallet Instance MUST be revoked.


WSCD and Keystore Requirements
""""""""""""""""""""""""""""""

To guarantee the utmost security, the cryptographic keys associated with a Wallet Instance (for example keys used to generate the Wallet Instance Attestation) MUST be securely generated and stored in a **Keystore** or a **WSCD**, as defined in :ref:`defined-terms:Defined Terms and Acronyms`.
The User MUST retain exclusive control of those private keys (Sole Control). The Keystore or WSCD MUST require User authentication (Wallet unlock: PIN or biometric) before any signature or other private-key operation (:ref:`WP_014c <wallet-instance-testcases>`).

The following approaches MAY be used:

- **Local Internal Keystore**: hardware-backed key storage native to the User's device, such as the Secure Enclave on iOS, or the Trusted Execution Environment (TEE) and StrongBox on Android. This is the component named Local Internal WSCD in some ARF texts. It is a Keystore, not a High-certifiable WSCD.
- **Local External WSCD**: hardware external to the User's device, such as a smart card compliant with *GlobalPlatform* and supporting *JavaCard*, certifiable as a WSCD.
- **Remote WSCD**: a remote Hardware Security Module (HSM) certifiable as a WSCD.
- **Local Hybrid WSCD**: a pluggable internal hardware component within the User's device, such as an *eUICC* that adheres to *GlobalPlatform* standards and supports *JavaCard*.
- **Remote Hybrid WSCD**: a local component mixed with a remote service.

Private keys of an IT-Wallet ID and of a (Q)EAA MAY be stored in a Local Internal Keystore (eIDAS Substantial). Private keys of a PID at LoA High MUST be stored only in a WSCD. A Local Internal Keystore MUST NOT be treated as evidence of LoA High. Private keys bound to a WIA MUST be generated and stored in the same Keystore or WSCD that the WIA attests (:ref:`WP_014 <wallet-instance-testcases>`–:ref:`WP_014e <wallet-instance-testcases>`).

A Mobile Relying Party Instance that does not store User identity keys MAY use a Local Internal Keystore and is not required to use a High-certifiable WSCD (:ref:`WP_014f <wallet-instance-testcases>`).

Digital Credentials whose bound private keys are stored in a local Keystore or local WSCD MAY be presented in proximity or otherwise offline. Digital Credentials whose bound private keys are stored in a remote WSCD MUST NOT be presented offline (:ref:`WP_160 <wallet-instance-testcases>`).

.. warning::
  At the current stage, the implementation profile defined in this document supports only the **Local Internal Keystore** (:ref:`WP_014 <wallet-instance-testcases>`). Future versions of this specification MAY include other approaches depending on the required Authenticator Assurance Level (`AAL`).

For more detailed information, please refer to :ref:`wallet-instance-registration:Wallet Instance Initialization and Registration`, :ref:`wallet-instance-attestation-issuance:Wallet Instance Attestation Issuance`, and :ref:`wallet-attestation-issuance:Key Attestation Issuance` of this document.



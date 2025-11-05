.. include:: ../common/common_definitions.rst

.. level 2 "included" file, so we start with '^' title level

Wallet Solution Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section lists the requirements about Wallet Providers and Wallet Solutions with their Wallet Instances, as well as the corresponding Wallet App Attestation, Wallet Unit Attestation and the secure storage component (WSCD).

- The Wallet Solution MUST adhere to the specifications set by this document for obtaining Personal Identification (PID) and (Q)EAAs.
- The Wallet Provider MUST expose a set of endpoints, exclusively available to its Wallet Solution instances, supporting the core functionalities of the Wallet Instances.
- The Wallet Instance MUST periodically reestablish trust with its Wallet Provider, obtaining a fresh Wallet App Attestation (:ref:`WP_018 <wallet-instance-testcases>`).
- The Wallet Instance MUST establish trust with other participants of the Wallet ecosystem, such as Credential Issers and Relying Parties. In case of Credential Issuers, Wallet Instance presents both Wallet App and Wallet Unit Attestations, while for Relying Parties, it only presents Wallet App Attestation. 
- The Wallet Instance MUST be compatible and functional on both Android and iOS operating systems and available on the Play Store and App Store, respectively (:ref:`WP_015 <wallet-instance-testcases>`).
- The Wallet Instance MUST provide a mechanism to verify the User's actual possession and full control of their personal device.
- The Wallet Instance MUST provide Users with an up-to-date list of Relying Parties with which the User has established a connection and, where applicable, all data exchanged;
- The Wallet Instance MUST provide Users with a mechanism to request the erasure of personal attributes by a Relying Party pursuant to Article 17 of Regulation (EU) 2016/679, and to log each Erasure Request made.

.. note::
   There is no strict one-to-one mapping between the requirements in this section and the test cases in :ref:`wallet-provider-test-matrix`. Some requirements are expressed at too high a level to be represented as atomic test cases, while others are already addressed in greater detail within related flows (e.g., :ref:`wallet-attestation-issuance:Wallet App and Wallet Unit Attestation Issuance`).

Wallet App Attestation Requirements
"""""""""""""""""""""""""""""""""""

Wallet App Attestation contains information regarding the security level of the device hosting the Wallet Instance.
It primarily proves the **authenticity**, **integrity**, **security**, and in general the **trustworthiness** of a particular Wallet Instance.

The requirements for the Wallet App Attestation are defined below:

- The Wallet App Attestation MUST provide all the relevant information to attest to the **integrity** and **security** of the device where the Wallet Instance is installed  (:ref:`WP_019 <wallet-instance-testcases>`).
- The Wallet App Attestation MUST be signed by the Wallet Provider that has authority over and is the owner of the Wallet Solution, as specified by the overseeing Registration Authority. This ensures that the Wallet App Attestation uniquely links the Wallet Provider to this particular Wallet Instance (:ref:`WP_020 <wallet-instance-testcases>`).
- The Wallet Provider MUST periodically evaluate and guarantee the integrity, the authenticity, and the genuineness of the Wallet Instance. The Wallet Provider verifies the Wallet Instance using the most secure flow made available by OS Provider's API, such as the *Play Integrity API* for Android and *App Attest* for iOS (:ref:`WP_011 <wallet-provider-backend-testcases>`).
- The Wallet Provider MUST possess a revocation mechanism for the Wallet Instance, allowing the Wallet Provider to terminate service for a specific Instance at any time (:ref:`WP_011 <wallet-provider-backend-testcases>`).
- The Wallet App Attestation MUST be securely bound to the Wallet Instance's ephemeral public key (:ref:`WP_019b <wallet-instance-testcases>`).
- The Wallet App Attestation MAY be used multiple times during its validity period, allowing for repeated authentication and authorization without the need to request new attestations with each interaction. However, it is RECOMMENDED that Wallet Instances avoid using the same attestation repeatedly, due to privacy concerns such as linkability between different interactions.
- The Wallet App Attestation MUST be short-lived and MUST have an expiration time, after which it MUST no longer be considered valid.
- The Wallet App Attestation MUST NOT be issued by the Wallet Provider if the authenticity, integrity, and genuineness of the Wallet Instance requesting it cannot be guaranteed (:ref:`WP_019a <wallet-instance-testcases>`).
- Each Wallet Instance SHOULD be able to request multiple Wallet App Attestations using different cryptographic public keys associated with them.
- The Wallet App Attestation MUST NOT contain information about the User in control of the Wallet Instance (:ref:`WP_029a <wallet-instance-testcases>`).
- The Wallet Instance MUST secure a Wallet App Attestation as a prerequisite for transitioning to the Operational state, as defined by `EIDAS-ARF`_.


.. note::
  Throughout this section, the services used to attest genuineness of the Wallet Instance and the device in which it is installed are referred to as **Device Integrity Service API**. The Device Integrity Service API is considered in an abstract fashion and it is assumed to be a service provided by a trusted third party (i.e., the OS Provider's API) which is able to perform integrity checks on the Wallet Instance as well as on the device where it is installed.


Wallet Unit Attestation Requirements
""""""""""""""""""""""""""""""""""""

Wallet Unit Attestation contains information to ensure that keys used for Digital Credential key binding are stored in a **trustworthy** WSCD. It also provides a method to authenticate the WSCD with the Credential Issuer and verifies that the Wallet Unit has not been revoked.

The requirements for the Wallet Unit Attestation are defined below:

- The Wallet Unit Attestation SHALL provide a PID Provider or Attestation Provider with information about the capabilities of the WSCA and WSCD of the Wallet Unit, such that they are able to take a well-grounded decision on whether to issue a PID or attestation to the Wallet Unit.
- The Wallet Unit Attestation SHALL enable PID Providers and Attestation Providers to verify the authenticity and revocation status of the Wallet Unit.
- A Wallet Provider SHALL ensure that a non-revoked Wallet Unit at all times can present a Wallet Unit Attestation, when requested by a PID Provider or Attestation Provider.
- During issuance of a PID or device-bound attestation, a Wallet Unit SHALL retrieve the requirements of the PID Provider or Attestation Provider regarding User authentication and key storage by the WSCA/WSCD from the Issuer metadata (as specified in `OpenID4VCI`_). The Wallet Unit SHALL determine which of its WSCA/WSCD(s), if any, comply with these requirements. If a compliant WSCA/WSCD is available to the Wallet Unit, the Wallet Unit SHALL request it to generate a new key pair for the new PID or attestation. The Wallet Unit SHALL provide the PID Provider or Attestation Provider with the Wallet Unit Attestation describing the properties of the WSCA/WSCD that generated the new PID or attestation private key.
- If a Wallet Unit contains multiple WSCAs, it SHALL, internally and securely, keep track of which PIDs and attestations are bound to which WSCA.
- A Wallet Unit SHALL present a Wallet Unit Attestation only as part of the issuance of a PID or an attestation.
- The Wallet Unit Attestation SHALL enable PID Providers to request a Wallet Provider to revoke a Wallet Unit, by including an identifier for the Wallet Unit in the WUA (e.g., a URI and index to an Attestation Status Lis). The Wallet Provider SHALL ensure that this Wallet Unit identifier does not enable tracking of the User.
- The Wallet Unit Attestation MUST contain one or multiple attested credential's public key that are coming from the same WSCD.
- The Wallet Unit Attestation MUST be signed by the Wallet Provider that has authority over and is the owner of the Wallet Solution, as specified by the overseeing Registration Authority. 
- The Wallet Unit Attestation MUST NOT be issued by the Wallet Provider if the WSCD trustworthiness is not guaranteed. In this case, the Wallet Instance MUST be revoked.


WSCD Requirements
"""""""""""""""""

To guarantee the utmost security, the cryptographic keys associated with a Wallet Instance (e.g., used to generate the Wallet App Attestation) MUST be securely generated and stored within the Wallet Secure Cryptographic Device (WSCD).
Only the legitimate User can access the private cryptographic keys, preventing unauthorized usage or tampering. The WSCD MAY be implemented using at least one of the approaches listed below:

- **Local Internal WSCD**: The WSCD relies entirely on the device's native cryptographic hardware, such as the Secure Enclave on iOS, or the Trusted Execution Environment (TEE) and Strongbox on Android.
- **Local External WSCD**: The WSCD is hardware external to the User's device, such as a smart card compliant with *GlobalPlatform* and supporting *JavaCard*.
- **Remote WSCD**: The WSCD utilizes a remote Hardware Security Module (HSM).
- **Local Hybrid WSCD**: The WSCD involves a pluggable internal hardware component within the User's device, such as an *eUICC* that adheres to *GlobalPlatform* standards and supports *JavaCard*.
- **Remote Hybrid WSCD**: The WSCD involves a local component mixed with a remote service.

.. warning::
  At the current stage, the implementation profile defined in this document supports only the **Local Internal WSCD** (:ref:`WP_014 <wallet-instance-testcases>`). Future versions of this specification MAY include other approaches depending on the required Authenticator Assurance Level (`AAL`).

For more detailed information, please refer to :ref:`wallet-instance-registration:Wallet Instance Initialization and Registration` and :ref:`wallet-attestation-issuance:Wallet App Attestation Issuance` of this document.



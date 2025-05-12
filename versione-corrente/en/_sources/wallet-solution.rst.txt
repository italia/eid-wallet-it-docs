.. include:: ../common/common_definitions.rst


Wallet Solution
===============

The Wallet Solution is issued by the Wallet Provider in the form of a mobile app and services, such as web interfaces. The mobile app serves as the primary interface for Users, allowing them to hold their Digital Credentials and interact with other participants of the ecosystem, such as Credential Issuers and Relying Parties. These Credentials are a set of data that can uniquely identify a natural or legal person, along with other Qualified and non-qualified Electronic Attestations of Attributes, also known as QEAAs and EAAs respectively, or (Q)EAAs for short. Once a User installs the mobile app on their device, such an installation is referred to as a Wallet Instance for the User. By supporting the mobile app, the Wallet Provider ensures the security and reliability of the entire Wallet Solution, as it is responsible for issuing the Wallet Attestation, which is a cryptographic proof about the authenticity and integrity of the Wallet Instance.

Wallet Solution Requirements
----------------------------

This section lists the requirements that Wallet Providers, Wallet Solutions, and their Wallet Instances must meet.

- The Wallet Solution MUST adhere to the specifications set by this document for obtaining Personal Identification (PID) and (Q)EAAs.
- The Wallet Provider MUST expose a set of endpoints, exclusively available to its Wallet Solution instances, supporting the core functionalities of the Wallet Instances.
- The Wallet Instance MUST periodically reestablish trust with its Wallet Provider, obtaining a fresh Wallet Attestation.
- The Wallet Instance MUST establish trust with other participants of the Wallet ecosystem, such as Credential Issers and Relying Parties, presenting a Wallet Attestation.
- The Wallet Instance MUST be compatible and functional on both Android and iOS operating systems and available on the Play Store and App Store, respectively.
- The Wallet Instance MUST provide a mechanism to verify the User's actual possession and full control of their personal device.
- The Wallet Instance MUST provide Users with an up-to-date list of Relying Parties with which the User has established a connection and, where applicable, all data exchanged;
- The Wallet Instance MUST provide Users with a mechanism to request the erasure of personal attributes by a Relying Party pursuant to Article 17 of Regulation (EU) 2016/679, and to log each Erasure Request made.

Wallet Attestation Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Wallet Attestation contains information regarding the security level of the device hosting the Wallet Instance.
It primarily certifies the **authenticity**, **integrity**, **security**, **privacy**, and **trustworthiness** of a particular Wallet Instance.

The requirements for the Wallet Attestation are defined below:

- The Wallet Attestation MUST provide all the relevant information to attest to the **integrity** and **security** of the device where the Wallet Instance is installed.
- The Wallet Attestation MUST be signed by the Wallet Provider that has authority over and is the owner of the Wallet Solution, as specified by the overseeing Registration Authority. This ensures that the Wallet Attestation uniquely links the Wallet Provider to this particular Wallet Instance.
- The Wallet Provider MUST ensure the integrity, authenticity, and genuineness of the Wallet Instance, preventing any attempts at manipulation or falsification by unauthorized third parties. The Wallet Provider MUST also verify the Wallet Instance using the available OS Provider's API and MUST do so using the most secure flow allowed by the OS Provider's API. Examples include *Play Integrity API* for Android and *App Attest* for iOS.
- The Wallet Provider MUST possess a revocation mechanism for the Wallet Instance, allowing the Wallet Provider to terminate service for a specific Instance at any time.
- The Wallet Attestation MUST be securely bound to the Wallet Instance's ephemeral public key.
- The Wallet Attestation MAY be used multiple times during its validity period, allowing for repeated authentication and authorization without the need to request new attestations with each interaction. However, it is RECOMMENDED that Wallet Instances avoid using the same attestation repeatedly, due to privacy concerns such as linkability between different interactions.
- The Wallet Attestation MUST be short-lived and MUST have an expiration time, after which it MUST no longer be considered valid.
- The Wallet Attestation MUST NOT be issued by the Wallet Provider if the authenticity, integrity, and genuineness of the Wallet Instance requesting it cannot be guaranteed.
- Each Wallet Instance SHOULD be able to request multiple Wallet Attestations using different cryptographic public keys associated with them.
- The Wallet Attestation MUST NOT contain information about the User in control of the Wallet Instance.
- The Wallet Instance MUST secure a Wallet Attestation as a prerequisite for transitioning to the Operational state, as defined by `EIDAS-ARF`_.

.. plantuml:: plantuml/wallet-solution-architecture.puml
    :width: 99%
    :alt: The figure illustrates the Wallet Solution Architecture.
    :caption: `Wallet Solution Architecture. <https://www.plantuml.com/plantuml/svg/VPAnJiCm48PtFyKfcIFs3AWW638Wa2B4M1tEqLhOliY-fEhRquPOSjEqwv_li_-SRnC5WmpEmXTQIm8jsq4CUsZrdXmgrC81Yiz8eG2CC4GAaDBP-GWyccu63bEsxQSiOrzeD9hW_VLjmfWSAANPzUp92nIB-_EpOkfKZePFmOhM-2ZeDUMQcJCeZsGj7rQqPzI_vBlS-lwF8ADJzyOBxOAH8xGKpidacPHkiJS0PQ1EgMM5AfZTNgh7Ixg6qrpLuk9xw4rsCQaQcWWz1W7-kUja7UlqZZ7jmfC8HS7pWKgfwUMhDK-pby0M7W2rc165hl__HaVqa9XKDL-UDItLL4mEgkivfSyRyjtWx1y0>`_


.. .. figure:: ../../images/static_view_wallet_instance_attestation.svg
..     :figwidth: 100%
..     :align: center
..     :target: https://www.plantuml.com/plantuml/svg/VP8nJyCm48Lt_ugdTexOCw22OCY0GAeGOsMSerWuliY-fEg_9mrEPTAqw-VtNLxEtaJHGRh6AMs40rRlaS8AEgAB533H3-qS2Tu2zxPEWSF8TcrYv-mJzTOGNfzVnXXJ0wKCDorxydAUjMNNYMMVpug9OTrR7i22LlaesXlADPiOraToZWyBsgCsF-JhtFhyGyZJgNlbXVR1oX5R2YSoUdQYEzrQO1seLcfUeGXs_ot5_VzqYM6lQlRXMz6hsTccIbGHhGu2_hhfP1tBwHuZqdOUH6WuEmrKIeqtNonvXhq4ThY3Dc9xBNJv_rSwQeyfawhcZsTPIpKLKuFYSa_JyOPytJNk5m00

..     Wallet Solution Schema

.. note::
  Throughout this section, the services used to attest genuineness of the Wallet Instance and the device in which it is installed are referred to as **Device Integrity Service API**. The Device Integrity Service API is considered in an abstract fashion and it is assumed to be a service provided by a trusted third party (i.e., the OS Provider's API) which is able to perform integrity checks on the Wallet Instance as well as on the device where it is installed.

WSCD Requirements
^^^^^^^^^^^^^^^^^

To guarantee the utmost security, the cryptographic keys associated with a Wallet Instance (e.g., used to generate the Wallet Attestation) MUST be securely generated and stored within the Wallet Secure Cryptographic Device (WSCD).
This ensures that only the User can access these keys, thus preventing unauthorized usage or tampering. The WSCD MAY be implemented using at least one of the approaches listed below:

- **Local Internal WSCD**: The WSCD relies entirely on the device's native cryptographic hardware, such as the Secure Enclave on iOS, or the Trusted Execution Environment (TEE) and Strongbox on Android.
- **Local External WSCD**: The WSCD is hardware external to the User's device, such as a smart card compliant with *GlobalPlatform* and supporting *JavaCard*.
- **Remote WSCD**: The WSCD utilizes a remote Hardware Security Module (HSM).
- **Local Hybrid WSCD**: The WSCD involves a pluggable internal hardware component within the User's device, such as an *eUICC* that adheres to *GlobalPlatform* standards and supports *JavaCard*.
- **Remote Hybrid WSCD**: The WSCD involves a local component mixed with a remote service.

.. warning::
  At the current stage, the implementation profile defined in this document supports only the **Local Internal WSCD**. Future versions of this specification MAY include other approaches depending on the required Authenticator Assurance Level (`AAL`).

For more detailed information, please refer to :ref:`wallet-instance-registration:Wallet Instance Initialization and Registration` and :ref:`wallet-attestation-issuance:Wallet Attestation Issuance` of this document.



.. toctree::
  :caption: Wallet Solution Table of Contents
  :maxdepth: 2

  wallet-instance.rst
  wallet-provider-endpoint.rst

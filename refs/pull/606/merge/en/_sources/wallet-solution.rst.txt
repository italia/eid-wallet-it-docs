.. include:: ../common/common_definitions.rst

.. _wallet-solution.rst:

Wallet Solution
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Wallet Solution is issued by the Wallet Provider in the form of a mobile app and services, such as web interfaces.

The mobile app serves as the primary interface for Users,
allowing them to hold their Digital Credentials and interact with other participants of the ecosystem,
such as Credential Issuers and Relying Parties.

These Credentials are a set of data that can uniquely identify a natural or legal person,
along with other Qualified and non-qualified Electronic Attestations of Attributes,
also known as QEAAs and EAAs respectively, or (Q)EAAs for short [1]_.

Once a User installs the mobile app on their device, such an installation is referred to as a Wallet Instance for the User.

By supporting the mobile app, the Wallet Provider ensures the security and reliability of the entire Wallet Solution,
as it is responsible for issuing the Wallet Attestation,
which is a cryptographic proof about the authenticity and integrity of the Wallet Instance.

Wallet Solution Requirements
-----------------------------

This section lists the requirements that are to be met by Wallet Providers, Wallet Solutions, and their Wallet Instances.

 - The Wallet Provider MUST expose a set of endpoints, exclusively available to its Wallet Solution instances, supporting the core functionalities of the Wallet Instances.
 - The Wallet Instance MUST periodically reestablish trust with its Wallet Provider, obtaining a fresh Wallet Attestation.
 - The Wallet Instance MUST establish trust with other participants of the Wallet ecosystem, such as Credential Issers and Relying Parties, presenting a Wallet Attestation.
 - The Wallet Solutions MUST adhere to the specifications set by this document for obtaining Personal Identification (PID) and (Q)EAAs.
 - The Wallet Instance MUST be compatible and functional on both Android and iOS operating systems and available on the Play Store and App Store, respectively.
 - The Wallet Instance MUST provide a mechanism to verify the User's actual possession and full control of their personal device.

Wallet Attestation Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Wallet Attestation contains information regarding the security level of the device hosting the Wallet Instance.
It primarily certifies the **authenticity**, **integrity**, **security**, **privacy**, and **trustworthiness** of a particular Wallet Instance.

.. figure:: ../../images/static_view_wallet_instance_attestation.svg
   :name: Wallet Solution Schema
   :alt: The image illustrates the containment of Wallet Provider and Wallet Instances within the Wallet Solution, managed by the Wallet Provider.
   :target: https://www.plantuml.com/plantuml/uml/VP8nJyCm48Lt_ugdTexOCw22OCY0GAeGOsMSerWuliY-fEg_9mrEPTAqw-VtNLxEtaJHGRh6AMs40rRlaS8AEgAB533H3-qS2Tu2zxPEWSF8TcrYv-mJzTOGNfzVnXXJ0wKCDorxydAUjMNNYMMVpug9OTrR7i22LlaesXlADPiOraToZWyBsgCsF-JhtFhyGyZJgNlbXVR1oX5R2YSoUdQYEzrQO1seLcfUeGXs_ot5_VzqYM6lQlRXMz6hsTccIbGHhGu2_hhfP1tBwHuZqdOUH6WuEmrKIeqtNonvXhq4ThY3Dc9xBNJv_rSwQeyfawhcZsTPIpKLKuFYSa_JyOPytJNk5m00


The requirements for the Wallet Attestation are defined below:

- The Wallet Attestation MUST use the signed JSON Web Token (JWT) format.
- The Wallet Attestation MUST provide all the relevant information to attest to the **integrity** and **security** of the device where the Wallet Instance is installed.
- The Wallet Attestation MUST be signed by the Wallet Provider that has authority over and is the owner of the Wallet Solution, as specified by the overseeing registration authority. This ensures that the Wallet Attestation uniquely links the Wallet Provider to this particular Wallet Instance.
- The Wallet Provider MUST ensure the integrity, authenticity, and genuineness of the Wallet Instance, preventing any attempts at manipulation or falsification by unauthorized third parties. The Wallet Provider MUST also verify the Wallet Instance using the App Store vendor's API, such as the *Play Integrity API* for Android and *DeviceCheck* for iOS. These services are defined in this specification as **Device Integrity Service (DIS)**.
- The Wallet Attestation MUST have a mechanism in place for revoking the Wallet Instance, allowing the Wallet Provider to terminate service for a specific instance at any time.
- The Wallet Attestation MUST be securely bound to the Wallet Instance's ephemeral public key.
- The Wallet Attestation MAY be used multiple times during its validity period, allowing for repeated authentication and authorization without the need to request new attestations with each interaction. However, it is RECOMMENDED that Wallet Instances avoid using the same attestation repeatedly, due to privacy concerns such as linkability between different interactions. 
- The Wallet Attestation MUST be short-lived and MUST have an expiration time, after which it MUST no longer be considered valid.
- The Wallet Attestation MUST NOT be issued by the Wallet Provider if the authenticity, integrity, and genuineness of the Wallet Instance requesting it cannot be guaranteed.
- Each Wallet Instance SHOULD be able to request multiple Wallet Attestations using different cryptographic public keys associated with them.
- The Wallet Attestation MUST NOT contain information about the User in control of the Wallet Instance.
- The Wallet Instance MUST secure a Wallet Attestation as a prerequisite for transitioning to the Operational state, as defined by `ARF`_.

WSCD Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To guarantee the utmost security, the cryptographic keys associated with a Wallet Instance (e.g., used to generate the Wallet Attestation) MUST be securely generated and stored within the WSCD.
This ensures that only the User can access these keys, thus preventing unauthorized usage or tampering. The WSCD MAY be implemented using at least one of the approaches listed below:

  - **Local Internal WSCD**: The WSCD relies entirely on the device's native cryptographic hardware, such as the Secure Enclave on iOS, or the Trusted Execution Environment (TEE) and Strongbox on Android [3]_.
  - **Local External WSCD**: The WSCD is hardware external to the User's device, such as a smart card compliant with *GlobalPlatform* and supporting *JavaCard*.
  - **Remote WSCD**: The WSCD utilizes a remote Hardware Security Module (HSM).
  - **Local Hybrid WSCD**: The WSCD involves a pluggable internal hardware component within the User's device, such as an *eUICC* that adheres to *GlobalPlatform* standards and supports *JavaCard*.
  - **Remote Hybrid WSCD**: The WSCD involves a local component mixed with a remote service.

.. warning::
  At the current stage, the implementation profile defined in this document supports only the **Local Internal WSCD**. Future versions of this specification MAY include other approaches depending on the required `AAL`.

For more detailed information, please refer to `Wallet Instance Initialization and Registration`_ and `Wallet Attestation Issuance`_  of this document. 

Wallet Instance
------------------------------

The Wallet Instance serves as a unique and secure device for authenticating the User within the Wallet ecosystem.
It establishes a strong and reliable mechanism for the User to engage in various digital transactions in a secure and privacy-preserving manner [2]_.

The Wallet Instance allows other entities within the ecosystem to establish trust with it, by consistently
presenting a Wallet Attestation during interactions with PID Providers,
(Q)EAA Providers, and Relying Parties. These verifiable attestations, provided by the Wallet Provider,
serve to authenticate the Wallet Instance itself, ensuring its reliability when engaging with other ecosystem actors.


Wallet Instance Lifecycle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Wallet Provider is in charge of the implementation and provision of Wallet Instances also handling their entire lifecycle.

In this section, state machines are presented to explain the Wallet Instance and Digital Credential states and their transitions and relations.

.. note::

  PID is a specialized Digital Credential type that has impacts on the Wallet Instance's lifecycle. The revocation of the PID MAY also have potential impacts on (Q)EAAs, if they were issued using the presentation of the PID. 
  When the distinction between PID and (Q)EAA is not needed, the term Digital Credential is used.

.. note::

  In the current version of `EIDAS-ARF`_, two types of attestations have been introduced: Wallet Trust Evidence (WTE) and Wallet Instance Attestation (WIA). The first proves that the keys used for key 
  binding of Digital Credentials reside in a trustworthy WSCD, and the second proves that the Wallet Instance is authentic. In this technical specification, a single attestation (Wallet Attestation) is 
  used as proof of both the Wallet Instance authenticity and the WSCD trustworthiness. The future version of this specification will be updated accordingly. 

As shown in :numref:`fig_Wallet_Instance_States`, the Wallet Instance has four distinct states: **Installed**, **Operational**, **Valid**, and **Uninstalled**.
Each state represents a specific functional status and determines the actions that can be performed.

.. _fig_Wallet_Instance_States:
.. figure:: ../../images/Wallet_Instance_States.svg
    :figwidth: 100%
    :align: center
    :target: https://www.plantuml.com/plantuml/svg/XPBHIuH04CRVzwyOk9SAH8ipGaHESW-4kEpihg1wi7ElMzXRHLUY_lfMAvtMZlD5cUytttpZxgnMMQMQlI0xdZDW-r9zGCxgJSLBnGj9Y0OKWrZgjn0iXyby7hgEyrE_BLcLjM0cOBBLJw-iCy4rxJXNJbzRIJxuH9TJT-eI0W1FPozWvSMxj89XaWSFCSIBzBubXd8FjcOONIt-Wol-jbEQHa4xEhpkK5m_xcpWWctLAF6IhaUaET_V5AAel5VHiE3axfI68SHfQYTBwjkT51pCrltMlmv97BNjkFKR0wifZT5c7trCxDz6U9POrelO4RqvP3jU6n4egB4gnQlYiJWLKf7fyUF14bWQrHTBHwZv9_FEBmBVRhy2CcCorrV-2m00

    Wallet Instance Lifecycle.

.. note::

  The Wallet Provider MUST ensure the security and reliability of the Wallet Instances. To achieve this, the Wallet Provider MUST periodically check the Wallet Instances security and compliance status. 

.. note::

  The Wallet Attestation is short-lived. It MUST be automatically re-issued before its expiration time. For this reason, the Wallet Instance expiration
  transition is not considered in :numref:`fig_Wallet_Instance_States`.

Transition to Installed
....................................
The state machine begins with the Wallet Instance installation (**WI INST**) transition, where Users download and install a Wallet Instance provided by the Wallet Provider using the
official app store of their device's operating system (this ensures authenticity via system checks), leading to the **Installed** state.

When the state is **Installed**, the Wallet Instance MUST interact only with the Wallet Provider to be activated. When the revocation of the Wallet Instance occurs, the Wallet Instance MUST go back from **Operational** or **Valid** to **Installed**. The revocation marks the Wallet Cryptographic Hardware Key, registered during activation 
(see `Transition to Operational`_), as not usable anymore. Revocation can occur in the following cases:

  * for technical security reasons (e.g., relating to the compromise of cryptographic material); 
  * in case of explicit User requests (e.g., due to loss, or theft of the Wallet Instance);
  * death of the User;
  * illegal activities reported by Judicial or Supervisory Bodies.

.. note::

  While for the ARF the revocation of the Wallet Instance is accomplished by revoking the Wallet Attestation (see Topic 9 and Topic 38 in Annex 2),
  in this specification the revocation is managed differently. Being the Wallet Attestation short-lived, it does not have a status management mechanism.
  For this reason, the Wallet Instance revocation transition is accomplished by deleting the Wallet Cryptographic Hardware Key from the WSCD of the Wallet
  Instance and from the account associated with the User. This transition is completed when the Wallet Instance is online.

Transition to Operational
....................................

After installation, the User opens the Wallet Instance and an activation begins (**WI ACT**). 
At this stage, a User account MUST be created with the Wallet Provider and associated with the Wallet Instance through the Wallet Cryptographic 
Hardware Key Tag, subject to obtaining the User's consent (see `Wallet Instance Initialization and Registration`_ for more details). 
This association allows the User to directly request Wallet Instance revocation from the Wallet Provider, and it also allows the Wallet Provider to 
revoke the Wallet Instance associated with that User.

.. note::

  As a result of the User account creation, an authentication mechanism MUST be set for the User to interact with the Wallet Provider portal.
  This specification mandates the use of at least a second-factor for User authentication.

As part of the activation, the Wallet Provider MUST evaluate the operating system and general technical capabilities of the device to check compliance
with the technical and security requirements, and the authenticity and integrity of the installed Wallet Instance.
Upon successful verification, the Wallet Provider MUST issue at least one valid Wallet Attestation to the Wallet Instance, therefore the Wallet Instance enters the **Operational** state.

In addition, if not already done, Users MUST set their preferred method of unlocking their Wallet Instance; this MAY be accomplished by entering a 
personal identification number (PIN) or by utilizing biometric authentication, such as fingerprint or facial recognition, according to personal 
preferences and device's capabilities. Please refer to `Wallet Attestation Issuance`_.

In the **Operational** state, Users can request the issuance of PID (**PID ISS**) or (Q)EAAs if the PID is not required in the issuance
(**(Q)EEA ISS**). In addition, if the Digital Credentials are (Q)EEAs and for the presentation they do not require the PID, they can be presented
without transitioning the Wallet Instance to another state (**(Q)EEA PRE** transition).

A **Valid** Wallet Instance MUST transition back to the **Operational** state due to **PID EXP/REV/DEL** transition, when the associated PID expires, is revoked by its Provider or either deleted by the User. 

Transition to Valid
....................................
A transition to the Valid state occurs only when the Wallet Instance obtains a valid PID (**PID ISS**). In this state, Users can obtain and present
new (Q)EAAs (**(Q)EAA ISS/PRE**), and present the PID (**PID PRE**). Please refer to :ref:`PID/(Q)EAA Issuance` and :ref:`Relying Party Solution`.

.. note::

  Users can have only one Wallet Instance in **Valid** state for the same Wallet Solution. Thus, when a User installs and obtains a PID on a new Wallet
  Instance of the same Wallet Solution from the same Wallet Provider, the PID in the previous Wallet Instance MUST be revoked and the Wallet Instance became
  **Operational**.

Transition to Uninstalled
....................................

Across all states, **Installed**, **Activated**, **Operational**, or **Valid**, the Wallet Instance can be removed entirely through the Wallet Instance 
uninstall (**WI UNINST**) transition, leading to the **Uninstalled** state. If a Wallet Instance is **Uninstalled** it ends its lifecycle.

Wallet Instance Lifecycle Management
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

While :numref:`fig_Wallet_Instance_States` shows the different states a Wallet Instance may acquire during its lifecycle,
:numref:`fig_Wallet_Instance_Lifecycle` shows the point of view of Wallet Instances and Wallet Providers in managing the Wallet Instance lifecycle
and the effect on their local storage.

.. _fig_Wallet_Instance_Lifecycle:
.. figure:: ../../images/wallet_instance_lifecycle.svg
    :figwidth: 100%
    :align: center
    :target: https://www.plantuml.com/plantuml/png/dP9Vgvim6CRl_HIPd0k5ddgpgq7XE0sSGhUAUbO6WnBDYnLYuf9NkpBstPUurPLEs9yRBzuyloV-aZmPP1g7JdYlMbcBWGCv8VRcJHHfTbutBPw6QZ2WQoKH9AvhrKMzOD8nZmQvQAieUVsOkT7BkrtKCOEWxUYOM8Ar4lIwT_tFsvGUYvBcT5z-p6WGUbxnl3ySCveN-_V7R9-NURmjtJpcF0THiYRmUUMlo0F25qoKK7hZAyra0sueRFVYiC2B0B8XAJCdu3ix2KBR-bODaZDz2OPgHVm34mAGRAL19ciWrrK_95yzuX5INAn85x3wyq8whh4T6RPAaayoE6n9d9IXRuD--0lb81RG74PLtw8v_N15BJkVMbe5PuDAh_p2Vba3SxttpRkngMziCgt6beE-ixd-K0FoVrqqZF_cSgSocP3VLEP8q0zkFMN8I3ReffND55ezc5wt21jVgqgXXPny3k87yBCsfJjQqWbmhuKrPkDUJkY2pdeE9ZcD5uDJShhhyv-YBZbTxVblTjSmphk_PEbovHD8FdJYEm00

    Wallet Instance Lifecycle Management.

Through a Wallet Instance in an **Installed** state, a User is able to start the **Wallet Instance Activation** (**WI ACT**).
As a result, the Wallet Instance MUST create a Wallet Cryptographic Hardware Key pair. In addition, if not already done,
Users MUST set their preferred method of unlocking their Wallet Instance. As a result of the **Wallet Instance Revocation** (**WI REV**), the Wallet Instance MUST
delete the Wallet Cryptographic Hardware Key pairs.

A Wallet Provider instead is responsible for:

  * **Wallet Instance Activation** (**WI ACT**): a User account MUST be created and associated with the Wallet Instance through the Wallet Cryptographic Hardware Key Tag. As a result of the User account creation, an authentication mechanism of at least two factors MUST be set for the User to interact with the Wallet Provider portal.
  * **Wallet Instance Revocation** (**WI REV**): for technical security reasons or triggered by external entities (e.g., Users and Supervisory Bodies) the Wallet Cryptographic Hardware Key Tag MUST be deleted from the User account.
  * **Data Purging**: through an explicit request of Users, the User account at the Wallet Provider MUST be removed from the local storage.


Wallet Instance Functionalities
-------------------------------
A Wallet Instance, provided by a Wallet Provider, MUST support three fundamental functionalities: Wallet Instance Registration, Wallet Instance Attestation Issuance, and Wallet Instance Revocation. Each functionality is described in detail in the following sections.

Wallet Instance Initialization and Registration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: ../../images/wallet_instance_initialization.svg
   :name: Sequence Diagram for Wallet Instance Initialization
   :alt: The figure illustrates the sequence diagram for initializing a Wallet Instance, with the steps explained below.
   :target: https://www.plantuml.com/plantuml/uml/ZLJ1RjD04BtlLupQ0sqKVY07L5H2MXKe8WKkNCRsn1d5tZMpiu7mzSpQROYZK3WuMis-z-QzjrAkeg9eQXk7IODFRK7YrbmHh4BG8lnqBpe3SCaTUdKEImq2PvyZoHbWX1GDVu20iw_ODAHmwqtPbzIZiEjWZ7f3Mox9K4griEvWIP8d0nmrmddiX7rT2v4_kU6ZXAqP5IYmt92lUcfHRfoh9QGEWczsaBhWOSKI5TWS6HELRHHMe6lAnboEyFALdMRGbn6VRk1Y81hWCWVdBUf0iU-HSRscSWCyg5L3g9ReKQHbpsrg8LAP-fH2tnCBjUGrVlFegqoTJFxMncG2706to0qM3JadFYX1s99a7rDB2-VlRXSt3ujFy_a7DxWvxiSaSdzFcT-I3OSMie5GAB87rcZ65IjKTDPclycv8QhjcS62rAoMwwpkQ_EsxwHltRuzq9FaSV04oYtb1e-e6JrKU7HHqKXrt_HUrV3Nikiqr8BTcakuGQb-e13SqIvQOnsozCcY1daU3WzOsyvX2MgS0QfILBkws9kQmlC2bovJ_wJ9uzUzJ5-oEOfSUwgWsC7z_Fr1eqlhUHn_Uf9lOVuhnkdd-88DLpOURpeDEDezWYt_MMSSF-pztOdNjCiKIMPmz3zX1rOs9x-eEgGPnLbDxif-Kjly1W00

**Step 1**: The User starts the Wallet Instance mobile app for the first time.

**Step 2**: The Wallet Instance:

  * Checks whether the device meets the minimum security requirements.
  * Checks if the Device Integrity Service is available.

.. note::

    **Federation Check**: The Wallet Instance needs to check if the Wallet Provider is part of the Federation, obtaining its protocol-specific Metadata. A non-normative example of a response from the `Federation endpoint`_ with the **Entity Configuration** and the **Metadata** of the Wallet Provider is represented within the `Federation endpoint`_ section.

**Steps 3-5 (Nonce Retrieval)**: The Wallet Instance requests a one-time ``challenge``  from the `Nonce endpoint`_ of the Wallet Provider Backend. This "challenge" known as a ``nonce``, MUST be unpredictable to serve as the main defense against replay attacks. 

Below is a non-normative example of a Nonce Request.

.. code-block:: http

    GET /nonce HTTP/1.1
    Host: walletprovider.example.com

Upon a successful request, the Wallet Provider Backend generates and returns the ``nonce`` value to the Wallet Instance. The backend MUST ensure that it is single-use and valid only within a specific time frame. 
Below is a non-normative example of a Nonce Response.

.. code-block:: http

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
      "nonce": "d2JhY2NhbG91cmVqdWFuZGFt"
    }

**Step 6**: The Wallet Instance, through the operating system, creates a pair of Cryptographic Hardware Keys and stores the corresponding Cryptographic Hardware Key Tag in local storage once the following requirements are met:

   1. It MUST ensure that Cryptographic Hardware Keys do not already exist. If they do exist and the Wallet is in the initialization phase, they MUST be deleted.
   2. It MUST generate a pair of asymmetric Elliptic Curve keys (Cryptographic Hardware Keys) via a local WSCD.
   3. It SHOULD obtain a unique identifier (Cryptographic Hardware Key Tag) for the generated Cryptographic Hardware Keys from the operating system. If the operating system permits specifying a tag during the creation of keys, then a random string for the Cryptographic Hardware Key Tag MUST be selected. This random value MUST be collision-resistant and unpredictable to ensure security. To achieve this, consider using a cryptographic hash function or a secure random number generator provided by the operating system or a reputable cryptographic library.
   4. If the previous points are satisfied, it MUST store the Cryptographic Hardware Key Tag in local storage.

.. note::

    **WSCD**: The Wallet Instance MAY use a local WSCD for cryptographic operations, including key generation, secure storage, and cryptographic processing,  on devices that support this feature. On Android devices, Strongbox is RECOMMENDED; Trusted Execution Environment (TEE) MAY be used only when Strongbox is unavailable. For iOS devices, Secure Elements (SE) MUST be used. Given that each OEM offers a distinct SDK for accessing the local WSCD, the discussion hereafter will address this topic in a general context.

    If the WSCD fails during any of these operations, for example due to hardware limitations, it will raise an error response to the Wallet Instance (e.g., see `TEE Client API Errors <TEE Client API Errors_>`_). The Wallet Instance MUST handle these errors accordingly to ensure secure operation. Details on error handling are left to the Wallet Instance implementation.

**Step 7**: The Wallet Instance uses the Device Integrity Service, providing the "challenge" and the Cryptographic Hardware Key Tag to acquire the Key Attestation.

.. note::

    **Device Integrity Service**: In this section, the Device Integrity Service is considered as it is provided by device manufacturers. This service allows the verification of a key being securely stored within the device's hardware through a signed object. Additionally, it offers verifiable proof that a specific Wallet Instance is authentic, unaltered, and in its original state using a specialized signed document made for this purpose.

    The service also incorporates details in the signed object, such as the device type, model, app version, operating system version, bootloader status, and other relevant information to assess whether the device has been compromised. For Android, the DIS is represented by *Key Attestation*, a feature supported by *StrongBox Keymaster*, which is a physical HSM installed directly on the motherboard, and the *TEE* (Trusted Execution Environment), a secure area of the main processor. *Key Attestation* aims to provide a way to strongly determine if a key pair is hardware-backed, what the properties of the key are, and what constraints are applied to its usage. Developers can leverage its functionality through the *Play Integrity API*. For Apple devices, the DIS is represented by *DeviceCheck*, which provides a framework and server interface to manage device-specific data securely. *DeviceCheck* is used in combination with the *Secure Enclave*, a dedicated HSM integrated into Apple's SoCs. *DeviceCheck* can be used to attest to the integrity of the device, apps, and/or encryption keys generated on the device, ensuring they were created in a secure environment like *Secure Enclave*. Developers can leverage *DeviceCheck* functionality by using the framework itself.
    These services, specifically developed by the manufacturer, are integrated within the Android or iOS SDKs, eliminating the need for a predefined endpoint to access them. Additionally, as they are specifically developed for mobile architecture, they do not need to be registered as Federation Entities through national registration systems.
    *Secure Enclave* has been available on Apple devices since the iPhone 5s (2013).
    For Android devices, the inclusion of **Strongbox Keymaster** may vary by manufacturer, who decides whether to include it or not.

    If any errors occur in any DIS process, such as device integrity verification, for example, due to an unavailable DIS, an internal error, or an invalid nonce in the integrity request, the DIS raises an error response (e.g., see  `Play Integrity API Errors <Play Integrity API Errors_>`_). The Wallet Instance MUST process these errors accordingly. Details on error handling are left to the Wallet Instance implementation.
 

**Step 8**: The Device Integrity Service performs the following actions:

* Creates a Key Attestation that is linked with the provided "challenge" and the public key of the Wallet Hardware.
* Incorporates information pertaining to the device's security.
* Uses an OEM private key to sign the Key Attestation, therefore verifiable with the related OEM certificate, confirming that the Cryptographic Hardware Keys are securely managed by the operating system.

**Step 9 (Wallet Instance Registration Request)**: The Wallet Instance sends a request to the `Wallet Instance Management endpoint`_ of the Wallet Provider Backend to register the Wallet Instance, identified by the Cryptographic Hardware Key public key. 
The request body includes the following claims: the ``challenge``, Key Attestation (``key_attestation``), and Cryptographic Hardware Key Tag (``hardware_key_tag``).

Below is a non-normative example of a Wallet Instance Registration Request.

.. code-block:: http

    POST /wallet-instances HTTP/1.1
    Host: walletprovider.example.com
    Content-Type: application/json

    {
      "challenge": "0fe3cbe0-646d-44b5-8808-917dd5391bd9",
      "key_attestation": "o2NmbXRvYXBwbGUtYXBw... redacted",
      "hardware_key_tag": "WQhyDymFKsP95iFqpzdEDWW4l7aVna2Fn4JCeWHYtbU="
    }

.. note::
  It is not necessary to send the Wallet Hardware public key because it is already included in the ``key_attestation``.
  As seen in the previous steps, the Device Integrity Service (DIS) creates a Key Attestation linked to the provided "challenge" and the public key of the Wallet Hardware. This process eliminates the need to send the Wallet Hardware public key directly, as it is already included in the key attestation. The ``hardware_key_tag`` serves as a reference or identifier for the corresponding Cryptographic Hardware key stored by the Wallet Provider. Therefore, the Wallet Provider can associate the received ``hardware_key_tag`` with the appropriate Cryptographic Hardware key in its storage.

.. warning::
  During the registration phase of the Wallet Instance with the Wallet Provider it is also necessary to associate the Wallet Instace with a specific User, authenticating the User with the Wallet Provider. The authentication mechanism is at the discretion of the Wallet Provider and it will not be addressed within these guidelines, as each Wallet Provider may have its User authentication systems already implemented.


**Steps 10-12 (Wallet Instance Registration Response)**: The Wallet Provider validates the ``challenge`` and ``key_attestation`` signature, therefore:

  1. It MUST verify that the ``challenge`` was generated by Wallet Provider and has not already been used.
  2. It MUST validate the ``key_attestation`` as defined by the device manufacturers' guidelines.
  3. It MUST verify that the device in use has no security flaws and reflects the minimum security requirements defined by the Wallet Provider.
  4. If these checks are passed, it MUST register the Wallet Instance, keeping the Cryptographic Hardware Key Tag and all useful information related to the device.
  5. It SHOULD associate the Wallet Instance with a specific User uniquely identified within the Wallet Provider's systems. This will be useful for the lifecycle of the Wallet Instance and for a future revocation.

Upon successful registration of the Wallet Instance, the Wallet Provider responds with a confirmation of success.
Below is a non-normative example of  a Wallet Instance Registration Response.

.. code-block:: http

    HTTP/1.1 204 No content


**Steps 13-14**: The Wallet Instance has been initialized and becomes operational.

.. note:: **Threat Model**: while the registration endpoint does not necessitate to authenticate the client, it is safeguarded through the use of `key_attestation`. Proper validation of this attestation permits the registration of authentic and unaltered app instances. Any other claims submitted will not undergo validation, leading the endpoint to respond with an error. Additionally, the inclusion of a challenge helps prevent replay attacks. The authenticity of both the challenge and the ``hardware_key_tag`` is ensured by the signature found within the ``key_attestation``.


.. include:: wallet-attestation.rst
.. include:: wallet-revocation.rst


Wallet Provider Endpoints
------------------------------------

The Wallet Provider, responsible for delivering a Wallet Solution, MUST expose endpoints to support trust establishment and essential Wallet Instance functionalities. This includes a trust endpoint - the Federation Endpoint - that MUST adhere to the OpenID Federation 1.0 specification to reliably establish the Wallet Provider’s identity within the ecosystem. In addition, endpoints for Wallet Instance registration, nonce generation (required for registration), attestation issuance, and revocation are also mandatory, although their specific implementation details are left to the Wallet Provider’s discretion.

Federation Endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The **/.well-known/openid-federation** endpoint serves as the discovery mechanism for trust establishment by retrieving the Wallet Provider Entity Configuration.

Wallet Provider Entity Configuration
...................................................

An HTTP GET request to the Federation endpoint allows the retrieval of the Wallet Provider Entity Configuration.

The returning Entity Configuration of the Wallet Provider MUST contain the attributes described in the sections below.

The Wallet Provider Entity Configuration is a signed JWT containing the
public keys and supported algorithms of the Wallet Provider metadata definition.
It is structured in accordance with the `OpenID Connect Federation <https://openid.net/specs/openid-connect-federation-1_0.html>`_
and the `Trust Model`_ outlined in this specification.


Wallet Provider Entity Configuration JWT Header
...................................................

.. list-table::
    :widths: 20 80
    :header-rows: 1

    * - **Key**
      - **Value**
    * - alg
      - Algorithm used to verify the token signature. It MUST be one of the possible values indicated in this `table <https://italia.github.io/eid-wallet-it-docs/versione-corrente/en/algorithms.html>`_ (e.g., ES256).
    * - kid
      - Thumbprint of the public key used for signing, according to :rfc:`7638`.
    * - typ
      - Media type, set to ``entity-statement+jwt``.

Wallet Provider Entity Configuration JWT Payload
.....................................................

.. list-table::
    :widths: 20 80
    :header-rows: 1

    * - **Key**
      - **Value**
    * - iss
      - Public URL of the Wallet Provider.
    * - sub
      - Public URL of the Wallet Provider.
    * - iat
      - Issuance datetime in Unix Timestamp format.
    * - exp
      - Expiration datetime in Unix Timestamp format.
    * - authority_hints
      - Array of URLs (String) containing the list of URLs of the immediate superior Entities, such as the Trust Anchor or an Intermediate, that MAY issue an Entity Statement related to this subject.
    * - jwks
      - A JSON Web Key Set (JWKS) `RFC 7517 <http://tools.ietf.org/html/rfc7517.html>`_ that represents the public part of the signing keys of the Entity at issue. Each JWK in the JWK set MUST have a key ID (claim kid).
    * - metadata
      - Contains the ``wallet_provider`` and ``federation_entity`` metadata.

wallet_provider metadata
..................................

+---------------------------------------------+---------------------------------------------------------------------+
| **Key**                                     | **Value**                                                           |
+---------------------------------------------+---------------------------------------------------------------------+
| jwks                                        | A JSON Web Key Set (JWKS)                                           |
|                                             | that represents the  Wallet                                         |
|                                             | Provider's public keys.                                             |
+---------------------------------------------+---------------------------------------------------------------------+
| aal_values_supported                        | List of supported values for the                                    |
|                                             | certifiable security context. These                                 |
|                                             | values specify the security level                                   |
|                                             | of the app, according to the levels: low, medium, or high.          |
|                                             | Authenticator Assurance Level values supported.                     |
+---------------------------------------------+---------------------------------------------------------------------+

.. note::
   The `aal_values_supported` parameter is experimental and under review.

federation_entity metadata
...................................

+-------------------+----------------------------------------------+
| **Key**           | **Value**                                    |
+-------------------+----------------------------------------------+
| organization_name | Organization name.                           |
+-------------------+----------------------------------------------+
| homepage_uri      | Organization's website URL.                  |
+-------------------+----------------------------------------------+
| tos_uri           | URL to the terms of service.                 |
+-------------------+----------------------------------------------+
| policy_uri        | URL to the privacy policy.                   |
+-------------------+----------------------------------------------+
| logo_uri          | URL of the organization's logo in SVG format.|
+-------------------+----------------------------------------------+

Below is a non-normative example of the Entity Configuration.

.. code-block:: javascript

  {
    "alg": "ES256",
    "kid": "5t5YYpBhN-EgIEEI5iUzr6r0MR02LnVQ0OmekmNKcjY",
    "typ": "entity-statement+jwt"
  }
  .
  {
  "iss": "https://wallet-provider.example.org",
  "sub": "https://wallet-provider.example.org",
  "jwks": {
    "keys": [
      {
        "crv": "P-256",
        "kty": "EC",
        "x": "qrJrj3Af_B57sbOIRrcBM7br7wOc8ynj7lHFPTeffUk",
        "y": "1H0cWDyGgvU8w-kPKU_xycOCUNT2o0bwslIQtnPU6iM",
        "kid": "5t5YYpBhN-EgIEEI5iUzr6r0MR02LnVQ0OmekmNKcjY"
      }
    ]
  },
  "metadata": {
    "wallet_provider": {
      "jwks": {
        "keys": [
          {
            "crv": "P-256",
            "kty": "EC",
            "x": "qrJrj3Af_B57sbOIRrcBM7br7wOc8ynj7lHFPTeffUk",
            "y": "1H0cWDyGgvU8w-kPKU_xycOCUNT2o0bwslIQtnPU6iM",
            "kid": "5t5YYpBhN-EgIEEI5iUzr6r0MR02LnVQ0OmekmNKcjY"
          }
        ]
      },
      "aal_values_supported": [
        "https://wallet-provider.example.org/LoA/basic",
        "https://wallet-provider.example.org/LoA/medium",
        "https://wallet-provider.example.org/LoA/high"
      ]
    },
    "federation_entity": {
      "organization_name": "IT-Wallet Provider",
      "homepage_uri": "https://wallet-provider.example.org",
      "policy_uri": "https://wallet-provider.example.org/privacy_policy",
      "tos_uri": "https://wallet-provider.example.org/info_policy",
      "logo_uri": "https://wallet-provider.example.org/logo.svg"
    }
  },
  "authority_hints": [
    "https://registry.eudi-wallet.example.it"
  ]
  "iat": 1687171759,
  "exp": 1709290159
  }


Nonce Endpoint 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This is a RESTful API endpoint that allows the Wallet Instance to request a cryptographic nonce from the Wallet Provider. The nonce serves as an unpredictable, single-use challenge to ensure freshness and prevent replay attacks.

Nonce Request
.............

The request for a nonce MUST be an HTTP GET request sent to the Wallet Provider’s Nonce Endpoint.

Nonce Response
..............
Upon a successful request, the Wallet Provider MUST return an HTTP response with a 200 OK status code. The response MUST be in `application/json` format, including the ``nonce``.
If any errors occur during the the nonce generation, an error response MUST be returned. Refer to `Error Handling for Nonce Generation`_ for details on error codes and descriptions.

Error Handling for Nonce Generation
.......................................

If any errors occur during the nonce generation, the Wallet Provider MUST return an error response as defined in :rfc:`6749#section-5.2`. The response MUST use *application/json* as the content type and MUST include the following parameters:

  - *error*. The error code.
  - *error_description*. Text in human-readable form providing further details to clarify the nature of the error encountered.

The following table lists HTTP Status Codes and related error codes that MUST be supported for the error response:

.. list-table::
   :widths: 30 20 50
   :header-rows: 1

   * - **HTTP Status Code**
     - **Error Code**
     - **Description**
   * - ``500 Internal Server Error``
     - ``server_error``
     - An internal server error occurred while processing the request.
   * - ``503 Service Unavailable``
     - ``temporarily_unavailable``
     - Service unavailable. Please try again later.


Wallet Instance Management Endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This is a RESTful API endpoint provided by the Wallet Provider that enables Wallet Instance management, including registration, status retrieval, revocation upon request (e.g., by the User), and deletion. 
The following sections describe the registration, status retrieval and revocation requests, along with their corresponding responses, handled by this endpoint, which are required for core `Wallet Instance Functionalities`_.

Wallet Instance Registration Request
.............................................
To register a Wallet Instance, the request to the Wallet Provider MUST use the HTTP POST method with ``Content-Type`` set to `application/json`. The request body MUST contain the following claims:

.. _table_http_request_claim:
.. list-table:: 
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Description**
      - **Reference**
    * - **challenge**
      - MUST be set to the value obtained from the Wallet Provider through the ``Nonce`` endpoint.
      - 
    * - **key_attestation**
      - It MUST be a ``base64url`` encoded Key Attestation obtained from the **Device Integrity Service**.
      -
    * - **hardware_key_tag**
      - It MUST be set with the unique identifier of the **Cryptographic Hardware Keys** and encoded in ``base64url``.
      -

Wallet Instance Registration Response
.............................................
If a Wallet Instance Registration Request is successfully validated, the Wallet Provider provides an HTTP Response with a 204 (No Content) status code.

If any errors occur during the Wallet Instance registration, an error response MUST be returned. Refer to `Error Handling for Wallet Instance Management`_ for details on error codes and descriptions.

Below is a non-normative example of an error response:

.. code:: http

   HTTP/1.1 403 Forbidden
   Content-Type: application/json
   Cache-Control: no-store

.. code:: json

   {
     "error": "forbidden",
     "error_description": "The provided challenge is invalid, expired, or already used."
   }


Wallet Instance Retrieval Request
.............................................

To retrieve all Wallet Instances associated with a User, a request MUST be sent using the HTTP GET method to the Wallet Provider with ``Content-Type`` set to `application/json`. 
 
.. note:: 
    For retrieving a specific Wallet Instance, the request MUST include the Wallet Instance ID as a path parameter.


Wallet Instance Retrieval Response
.............................................

If a Wallet Instance Retrieval Request is successfully processed, the Wallet Provider MUST return an HTTP Response with a 200 (OK) status code. 
The response body MUST be in JSON format and include the relevant Wallet Instance information, such as its unique ID, status, and issuance date. 
When retrieving all Wallet Instances, the response MUST return an array containing the details of all associated instances.

If any errors occur during the retrieval process, an error response MUST be returned. Refer to `Error Handling for Wallet Instance Management`_ for details on error codes and descriptions.

Below is a non-normative example of an error response:

.. code:: http

   HTTP/1.1 403 Forbidden
   Content-Type: application/json
   Cache-Control: no-store

.. code:: json

   {
     "error": "forbidden",
     "error_description": "User is not authorized to retrieve Wallet Instances."
   }


Wallet Instance Revocation Request
.............................................

To revoke an active Wallet Instance, a revocation request MUST be sent using the HTTP PATCH method with ``Content-Type`` set to `application/json`. The request body MUST contain a ``status`` parameter set to "REVOKED".

.. note:: 
  While PATCH is the recommended method, the revocation request MAY also be sent using the POST method, depending on implementation preferences.

Wallet Instance Revocation Response
.............................................
If a Wallet Instance Revocation Request is successfully processed, the Wallet Provider provides an HTTP Response with a 204 (No Content) status code.

If any errors occur during the Wallet Instance Revocation, an error response MUST be returned. Refer to `Error Handling for Wallet Instance Management`_ for details on error codes and descriptions.

Below is a non-normative example of an error response:

.. code:: http

   HTTP/1.1 400 Bad Request
   Content-Type: application/json
   Cache-Control: no-store

.. code:: json

   {
     "error": "bad_request",
     "error_description": "The request is missing status parameter."
   }

Error Handling for Wallet Instance Management 
..................................................
To ensure robustness and security, the Wallet Provider MUST handle errors consistently across all Wallet Instance Management requests, including Registration, Retrieval, and Revocation.

In case of an error, the Wallet Provider MUST return an error response as defined in :rfc:`7231`, with additional details available in :rfc:`7807`. The response MUST use the ``Content-Type`` set to `application/json` and MUST include the following parameters:

  - *error*. The error code.
  - *error_description*. Text in human-readable form providing further details to clarify the nature of the error encountered.

The following sections categorize errors into **common errors**, which apply to all requests, and **request-specific errors**, which are relevant to particular operations.

Common Error Responses
'''''''''''''''''''''''''''''''''''''''
The following errors apply to all Wallet Instance Management operations (Registration, Retrieval, and Revocation), and MUST be supported for the error response, unless otherwise specified:

.. list-table:: 
   :widths: 20 20 50
   :header-rows: 1

   * - **HTTP Status Code**
     - **Error Code**
     - **Description**
   * - ``400 Bad Request``
     - ``bad_request``
     - The request is malformed, missing required parameters, or includes invalid and unknown parameters.
   * - ``422 Unprocessable Content`` [OPTIONAL]
     - ``validation_error``
     - The request does not adhere to the required format.
   * - ``500 Internal Server Error``
     - ``server_error``
     - An internal error occurred while processing the request.
   * - ``503 Service Unavailable``
     - ``temporarily_unavailable``
     - The service is unavailable. Please try again later.

Request-Specific Error Responses
'''''''''''''''''''''''''''''''''''''''
The following errors MUST be supported for error responses related to **Wallet Instance Registration**:

.. list-table:: 
   :widths: 20 20 50
   :header-rows: 1

   * - **HTTP Status Code**
     - **Error Code**
     - **Description**
   * - ``403 Forbidden``
     - ``integrity_check_error``
     - The device does not meet the Wallet Provider's minimum security requirements.
   * - ``403 Forbidden``
     - ``invalid_request``
     - The provided challenge is invalid, expired, or already used.
   * - ``403 Forbidden``
     - ``invalid_request``
     - The signature of the Key Attestation is invalid.


The following errors MUST be supported for error responses related to **Wallet Instance Retrieval**:

.. list-table:: 
   :widths: 20 20 50
   :header-rows: 1

   * - **HTTP Status Code**
     - **Error Code**
     - **Description**
   * - ``403 Forbidden``
     - ``forbidden``
     - The user does not have permission to retrieve this Wallet Instance.
   * - ``401 Unauthorized``
     - ``unauthorized``
     - The request lacks valid authentication credentials.
  
The following errors MUST be supported for error responses related to **Wallet Instance Revocation**:

.. list-table:: 
   :widths: 20 20 50
   :header-rows: 1

   * - **HTTP Status Code**
     - **Error Code**
     - **Description**
   * - ``403 Forbidden``
     - ``invalid_request``
     - The user does not have permission to revoke this Wallet Instance.
   * - ``401 Unauthorized``
     - ``unauthorized``
     - The request cannot be authenticated or authorized.

Wallet Attestation Issuance Endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This is a RESTful API endpoint provided by the Wallet Provider that enables the Wallet Instance to obtain a Wallet Attestation, by sending a Wallet Attestation Issuance Request.

Wallet Attestation Issuance Request
.............................................
The request to the Wallet Provider MUST use the HTTP POST method with ``Content-Type`` set to `application/json`. The request body MUST contain an ``assertion`` parameter whose value is a signed JWT of the Wallet Attestation Request, including all header and body parameters (see :ref:`Table of the Wallet Attestation Request Body <table_wallet_attestation_request_claim>` below).

.. _table_wallet_attestation_request_claim:

Wallet Attestation Request
...................................

The JOSE header of the Wallet Attestation Request JWT MUST contain the following parameters:

.. list-table::
    :widths: 20 60 20
    :header-rows: 1

    * - **JOSE header**
      - **Description**
      - **Reference**
    * - **alg**
      - A digital signature algorithm identifier such as per IANA "JSON Web Signature and Encryption Algorithms" registry. It MUST be one of the supported algorithms listed in the `Cryptographic Algorithms <algorithms.html>`_ and MUST NOT be set to ``none`` or any symmetric algorithm (MAC) identifier.
      - :rfc:`7516#section-4.1.1`.
    * - **kid**
      -  Unique identifier of the ``jwk`` used by the Wallet Provider to sign the Wallet Attestation, essential for matching the Wallet Provider's cryptographic public key needed for signature verification.
      - :rfc:`7638#section_3`.
    * - **typ**
      -  It MUST be set to ``var+jwt``
      -

The body of the Wallet Attestation Request JWT MUST contain the following claims:

.. list-table::
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Description**
      - **Reference**
    * - **iss**
      - Identifier of the Wallet Provider concatenated with the thumbprint of the JWK in the ``cnf`` claim.
      - :rfc:`9126` and :rfc:`7519`.
    * - **aud**
      - It MUST be set to the identifier of the Wallet Provider.
      - :rfc:`9126` and :rfc:`7519`.
    * - **exp**
      - UNIX Timestamp with the expiry time of the JWT.
      - :rfc:`9126` and :rfc:`7519`.
    * - **iat**
      - REQUIRED. UNIX Timestamp with the time of JWT issuance.
      - :rfc:`9126` and :rfc:`7519`.
    * - **challenge**
      - Challenge data obtained from the ``nonce`` endpoint.
      -
    * - **hardware_signature**
      - The signature of ``client_data`` obtained using Cryptographic Hardware Key base64 encoded.
      -
    * - **integrity_assertion**
      - The integrity assertion obtained from the **Device Integrity Service** with the holder binding of ``client_data``.
      -
    * - **hardware_key_tag**
      - Unique identifier of the **Cryptographic Hardware Keys**.
      -
    * - **cnf**
      - JSON object, containing the public part of an asymmetric key pair owned by the Wallet Instance.
      - :rfc:`7800`
    * - **vp_formats_supported**
      - JSON object with name/value pairs, identifying a Credential format supported by the Wallet.
      -
    * - **authorization_endpoint**
      - URL of the Wallet Authorization Endpoint, it can be a universal link or a custom url-scheme.
      -
    * - **response_types_supported**
      - JSON array containing a list of the OAuth 2.0 ``response_type`` values.
      -
    * - **response_modes_supported**
      - JSON array containing a list of the OAuth 2.0 "response_mode" values that this authorization server supports.
      - :rfc:`8414`
    * - **request_object_signing_alg_values_supported**
      - JSON array containing a list of the signing algorithms (alg values) supported.
      -


Wallet Attestation Issuance Response
.............................................
If the Wallet Attestation Issuance Request is successfully validated, the Wallet Provider returns an HTTP response with a 200 (OK) status code. The response includes the Wallet Attestation, signed by the Wallet Provider, containing the header and body claims (see :ref:`Table of the Wallet Attestation <table_wallet_attestation_claim>` below).

If any errors occur during the Wallet Attestation Issuance, an error response MUST be returned. Refer to `Error Handling for Wallet Attestation Issuance`_ for details on error codes and descriptions.
Below is a non-normative example of an error response:

.. code:: http

   HTTP/1.1 403 Forbidden
   Content-Type: application/json
   Cache-Control: no-store

.. code:: json

   {
     "error": "integrity_check_error",
     "error_description": "The device does not meet the Wallet Provider’s minimum security requirements."
   }

.. _table_wallet_attestation_claim:

Wallet Attestation JWT
...................................

The JOSE header of the Wallet Attestation JWT MUST contain the following parameters:

.. list-table::
    :widths: 20 60 20
    :header-rows: 1

    * - **JOSE header**
      - **Description**
      - **Reference**
    * - **alg**
      - A digital signature algorithm identifier such as per IANA "JSON Web Signature and Encryption Algorithms" registry. It MUST be one of the supported algorithms listed in the Section `Cryptographic Algorithms <algorithms.html>`_ and MUST NOT be set to ``none`` or any symmetric algorithm (MAC) identifier.
      - :rfc:`7516#section-4.1.1`.
    * - **kid**
      -  Unique identifier of the ``jwk`` inside the ``cnf`` claim of Wallet Instance as base64url-encoded JWK Thumbprint value.
      - :rfc:`7638#section_3`.
    * - **typ**
      -  It MUST be set to ``wallet-attestation+jwt``
      -  `OPENID4VC-HAIP`_
    * - **trust_chain**
      - Sequence of Entity Statements that composes the Trust Chain related to the Relying Party.
      - `OID-FED`_ Section 4.3 *Trust Chain Header Parameter*.

The body of the Wallet Attestation JWT MUST contain the following claims:

.. list-table::
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Description**
      - **Reference**
    * - **iss**
      - Identifier of the Wallet Provider
      - :rfc:`9126` and :rfc:`7519`.
    * - **sub**
      - Identifier of the Wallet Instance which is the thumbprint of the Wallet Instance JWK contained in the ``cnf`` claim.
      - :rfc:`9126` and :rfc:`7519`.
    * - **exp**
      - UNIX Timestamp with the expiry time of the JWT.
      - :rfc:`9126` and :rfc:`7519`.
    * - **iat**
      - UNIX Timestamp with the time of JWT issuance.
      - :rfc:`9126` and :rfc:`7519`.
    * - **cnf**
      - JSON object, containing the public part of an asymmetric key pair owned by the Wallet Instance.
      - :rfc:`7800`
    * - **aal**
      - JSON String asserting the authentication level of the Wallet and the key as asserted in the cnf claim.
      -
    * - **authorization_endpoint**
      - URL of the Wallet Authorization Endpoint, it can be a universal link or a custom url-scheme.
      -
    * - **response_types_supported**
      - JSON array containing a list of the OAuth 2.0 ``response_type`` values.
      -
    * - **response_modes_supported**
      - JSON array containing a list of the OAuth 2.0 "response_mode" values that this authorization server supports.
      - :rfc:`8414`
    * - **vp_formats_supported**
      - JSON object with name/value pairs, identifying a Credential format supported by the Wallet.
      -
    * - **request_object_signing_alg_values_supported**
      - JSON array containing a list of the signing algorithms (alg values) supported.
      -
    * - **client_id_schemes_supported**
      - Array of JSON Strings containing the values of the Client Identifier schemes that the Wallet supports.
      - `OpenID4VP`_

Error Handling for Wallet Attestation Issuance 
..................................................

If any errors occur during the Wallet Attestation Request verification, the Wallet Provider MUST return an error response as defined in :rfc:`7231` (additional details available in :rfc:`7807`). The response MUST use the content type set to *application/json* and MUST include the following parameters:

  - *error*. The error code.
  - *error_description*. Text in human-readable form providing further details to clarify the nature of the error encountered.

The following table lists HTTP Status Codes and related error codes that MUST be supported for the error response, unless otherwise specified:

.. list-table::
   :widths: 30 20 50
   :header-rows: 1

   * - **HTTP Status Code**
     - **Error Code**
     - **Description**
   * - ``400 Bad Request``
     - ``bad_request``
     - The request is malformed, missing required parameters (e.g., header parameters or integrity assertion), or includes invalid and unknown parameters.
   * - ``403 Forbidden`` 
     - ``invalid_request``
     - The wallet instance was revoked.
   * - ``403 Forbidden`` 
     - ``integrity_check_error``
     - The device does not meet the Wallet Provider’s minimum security requirements.
   * - ``403 Forbidden``
     - ``invalid_request``
     - The signature of the Wallet Attestation Request is invalid or does not match the associated public key (JWK).
   * - ``403 Forbidden`` 
     - ``invalid_request``
     - The integrity assertion validation failed; the integrity assertion is tampered with or improperly signed.
   * - ``403 Forbidden`` 
     - ``invalid_request``
     - The provided challenge is invalid, expired, or already used.
   * - ``403 Forbidden``
     - ``invalid_request``
     - The Proof of Possession (``hardware_signature``) is invalid.
   * - ``403 Forbidden`` 
     - ``invalid_request``
     - The ``iss`` parameter does not match the Wallet Provider’s expected URL identifier.
   * - ``404 Not Found`` 
     - ``not_found``
     - The Wallet Instance was not found.
   * - ``422 Unprocessable Content`` [OPTIONAL]
     - ``validation_error``
     - The request does not adhere to the required format.
   * - ``500 Internal Server Error``
     - ``server_error``
     - An internal server error occurred while processing the request.
   * - ``503 Service Unavailable``
     - ``temporarily_unavailable``
     - Service unavailable. Please try again later.

External references
--------------------------

.. [1] Definitions are inherited from the EUDI Wallet Architecture and Reference Framework, version 1.1.0 at the time of writing. Please refer to `this page <https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/9647a408f628569449af6b30a15fed82cd41129a/arf.md#2-definitions>`_ for extended definitions and details.

.. [2] Wallet Instance states adhere to the EUDI Wallet Architecture and Reference Framework, as defined `here <https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/9647a408f628569449af6b30a15fed82cd41129a/arf.md#424-eudi-wallet-instance-lifecycle>`_.

.. [3] Depending on the device operating system, TEE is defined by `Trusty`_ or `Secure Enclave`_ for Android and iOS devices, respectively.

.. _Trust Model: trust.html
.. _Wallet Attestation Issuance: wallet-solution.html#wallet-attestation-issuance
.. _Wallet Instance Initialization and Registration: wallet-solution.html#wallet-instance-initialization-and-registration
.. _Transition to Operational: wallet-solution.html#transition-to-operational
.. _Trusty: https://source.android.com/docs/security/features/trusty
.. _Secure Enclave: https://support.apple.com/en-gb/guide/security/sec59b0b31ff/web
.. _Wallet Provider metadata: wallet-solution.html#wallet-provider-metadata
.. _Nonce endpoint: wallet-solution.html#nonce-endpoint
.. _Wallet Attestation Issuance endpoint: wallet-solution.html#wallet-attestation-issuance-endpoint
.. _Federation endpoint: wallet-solution.html#federation-endpoint
.. _Wallet Instance Management endpoint: wallet-solution.html#wallet-instance-management-endpoint
.. _Wallet Instance Functionalities: wallet-solution.html#wallet-instance-functionalities
.. _Error Handling for Wallet Instance Management: wallet-solution.html#error-handling-for-wallet-instance-management 
.. _Error Handling for Wallet Attestation Issuance: wallet-solution.html#error-handling-for-wallet-attestation-issuance
.. _Error Handling for Nonce Generation: wallet-solution.html#error-handling-for-nonce-generation


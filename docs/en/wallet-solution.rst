.. include:: ../common/common_definitions.rst

.. _wallet-solution.rst:

Wallet Solution
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Wallet Solution is issued by the Wallet Provider in the form of a mobile app and services, such as web interfaces. The mobile app serves as the primary interface for Users, allowing them to hold their Digital Credentials and interact with other participants of the ecosystem, such as Credential Issuers and Relying Parties. These Credentials are a set of data that can uniquely identify a natural or legal person, along with other Qualified and non-qualified Electronic Attestations of Attributes, also known as QEAAs and EAAs respectively, or (Q)EAAs for short. Once a User installs the mobile app on their device, such an installation is referred to as a Wallet Instance for the User. By supporting the mobile app, the Wallet Provider ensures the security and reliability of the entire Wallet Solution, as it is responsible for issuing the Wallet Attestation, which is a cryptographic proof about the authenticity and integrity of the Wallet Instance.

Wallet Solution Requirements
-----------------------------

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Wallet Attestation contains information regarding the security level of the device hosting the Wallet Instance.
It primarily certifies the **authenticity**, **integrity**, **security**, **privacy**, and **trustworthiness** of a particular Wallet Instance.

The requirements for the Wallet Attestation are defined below:

- The Wallet Attestation MUST provide all the relevant information to attest to the **integrity** and **security** of the device where the Wallet Instance is installed.
- The Wallet Attestation MUST be signed by the Wallet Provider that has authority over and is the owner of the Wallet Solution, as specified by the overseeing registration authority. This ensures that the Wallet Attestation uniquely links the Wallet Provider to this particular Wallet Instance.
- The Wallet Provider MUST ensure the integrity, authenticity, and genuineness of the Wallet Instance, preventing any attempts at manipulation or falsification by unauthorized third parties. The Wallet Provider MUST also verify the Wallet Instance using the available OS Provider's API and MUST do so using the securest flow alloweded by the OS Provider's API. Examples include *Play Integrity API* for Android and *App Attest* for iOS.
- The Wallet Provider MUST possess a revocation mechanism for the Wallet Instance, allowing the Wallet Provider to terminate service for a specific Instance at any time.
- The Wallet Attestation MUST be securely bound to the Wallet Instance's ephemeral public key.
- The Wallet Attestation MAY be used multiple times during its validity period, allowing for repeated authentication and authorization without the need to request new attestations with each interaction. However, it is RECOMMENDED that Wallet Instances avoid using the same attestation repeatedly, due to privacy concerns such as linkability between different interactions.
- The Wallet Attestation MUST be short-lived and MUST have an expiration time, after which it MUST no longer be considered valid.
- The Wallet Attestation MUST NOT be issued by the Wallet Provider if the authenticity, integrity, and genuineness of the Wallet Instance requesting it cannot be guaranteed.
- Each Wallet Instance SHOULD be able to request multiple Wallet Attestations using different cryptographic public keys associated with them.
- The Wallet Attestation MUST NOT contain information about the User in control of the Wallet Instance.
- The Wallet Instance MUST secure a Wallet Attestation as a prerequisite for transitioning to the Operational state, as defined by :ref:`ARF`.

.. figure:: ../../images/static_view_wallet_instance_attestation.svg
    :figwidth: 100%
    :align: center
    :target: https://www.plantuml.com/plantuml/svg/VP8nJyCm48Lt_ugdTexOCw22OCY0GAeGOsMSerWuliY-fEg_9mrEPTAqw-VtNLxEtaJHGRh6AMs40rRlaS8AEgAB533H3-qS2Tu2zxPEWSF8TcrYv-mJzTOGNfzVnXXJ0wKCDorxydAUjMNNYMMVpug9OTrR7i22LlaesXlADPiOraToZWyBsgCsF-JhtFhyGyZJgNlbXVR1oX5R2YSoUdQYEzrQO1seLcfUeGXs_ot5_VzqYM6lQlRXMz6hsTccIbGHhGu2_hhfP1tBwHuZqdOUH6WuEmrKIeqtNonvXhq4ThY3Dc9xBNJv_rSwQeyfawhcZsTPIpKLKuFYSa_JyOPytJNk5m00

    Wallet Solution Schema

.. note::

  Throughout this section, the services used to attest genuineness of the Wallet Instance and the device in which it is installed are referred to as **Device Integrity Service API**. The Device Integrity Service API is considered in an abstract fashion and it is assumed to be a service provided by a trusted third party (i.e., the OS Provider's API) which is able to perform integrity checks on the Wallet Instance as well as on the device where it is installed.

WSCD Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To guarantee the utmost security, the cryptographic keys associated with a Wallet Instance (e.g., used to generate the Wallet Attestation) MUST be securely generated and stored within the Wallet Secure Cryptographic Device (WSCD).
This ensures that only the User can access these keys, thus preventing unauthorized usage or tampering. The WSCD MAY be implemented using at least one of the approaches listed below:

- **Local Internal WSCD**: The WSCD relies entirely on the device's native cryptographic hardware, such as the Secure Enclave on iOS, or the Trusted Execution Environment (TEE) and Strongbox on Android.
- **Local External WSCD**: The WSCD is hardware external to the User's device, such as a smart card compliant with *GlobalPlatform* and supporting *JavaCard*.
- **Remote WSCD**: The WSCD utilizes a remote Hardware Security Module (HSM).
- **Local Hybrid WSCD**: The WSCD involves a pluggable internal hardware component within the User's device, such as an *eUICC* that adheres to *GlobalPlatform* standards and supports *JavaCard*.
- **Remote Hybrid WSCD**: The WSCD involves a local component mixed with a remote service.

.. warning::
  At the current stage, the implementation profile defined in this document supports only the **Local Internal WSCD**. Future versions of this specification MAY include other approaches depending on the required Authenticator Assurance Level (`AAL`).

For more detailed information, please refer to :ref:`Wallet Instance Initialization and Registration` and :ref:`Wallet Attestation Issuance`  of this document.

Wallet Instance
------------------------------

The Wallet Instance establishes a strong and reliable mechanism for the User to engage in various digital transactions in a secure and privacy-preserving manner.

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

Transition to Installed
....................................
The state machine begins with the Wallet Instance installation (**WI INST**) transition, where Users download and install a Wallet Instance provided by the Wallet Provider using the
official app store of their device's operating system (this ensures authenticity via system checks), leading to the **Installed** state.

When the state is **Installed**, the Wallet Instance MUST interact only with the Wallet Provider to be activated. When the revocation of the Wallet Instance occurs, the Wallet Instance MUST go back from **Operational** or **Valid** to **Installed**. The revocation marks the Wallet Cryptographic Hardware Key, registered during activation
(see :ref:`Transition to Operational`), as not usable anymore. Revocation can occur in the following cases:

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
Hardware Key Tag, subject to obtaining the User's consent (see :ref:`Wallet Instance Initialization and Registration` for more details).
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
preferences and device's capabilities. Please refer to :ref:`Wallet Attestation Issuance`.

In the **Operational** state, Users can request the issuance of PID (**PID ISS**) or (Q)EAAs if the PID is not required in the issuance
(**(Q)EEA ISS**). In addition, if the Digital Credentials are (Q)EEAs and for the presentation they do not require the PID, they can be presented
without transitioning the Wallet Instance to another state (**(Q)EEA PRE** transition).

A **Valid** Wallet Instance MUST transition back to the **Operational** state due to **PID EXP/REV/DEL** transition, when the associated PID expires, is revoked by its Provider or either deleted by the User.

Transition to Valid
....................................
A transition to the Valid state occurs only when the Wallet Instance obtains a valid PID (**PID ISS**). In this state, Users can obtain and present
new (Q)EAAs (**(Q)EAA ISS/PRE**), and present the PID (**PID PRE**). Please refer to :ref:`PID/(Q)EAA Issuance` and :ref:`PID/(Q)EAA Presentation`.

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
    :target: https://www.plantuml.com/plantuml/svg/dP9Vgvim6CRl_HIPd0k5ddgpgq7XE0sSGhUAUbO6WnBDYnLYuf9NkpBstPUurPLEs9yRBzuyloV-aZmPP1g7JdYlMbcBWGCv8VRcJHHfTbutBPw6QZ2WQoKH9AvhrKMzOD8nZmQvQAieUVsOkT7BkrtKCOEWxUYOM8Ar4lIwT_tFsvGUYvBcT5z-p6WGUbxnl3ySCveN-_V7R9-NURmjtJpcF0THiYRmUUMlo0F25qoKK7hZAyra0sueRFVYiC2B0B8XAJCdu3ix2KBR-bODaZDz2OPgHVm34mAGRAL19ciWrrK_95yzuX5INAn85x3wyq8whh4T6RPAaayoE6n9d9IXRuD--0lb81RG74PLtw8v_N15BJkVMbe5PuDAh_p2Vba3SxttpRkngMziCgt6beE-ixd-K0FoVrqqZF_cSgSocP3VLEP8q0zkFMN8I3ReffND55ezc5wt21jVgqgXXPny3k87yBCsfJjQqWbmhuKrPkDUJkY2pdeE9ZcD5uDJShhhyv-YBZbTxVblTjSmphk_PEbovHD8FdJYEm00

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
A Wallet Instance, MUST support the following functionalities:

  - Wallet Registration (detailed in :ref:`Wallet Instance Initialization and Registration`),
  - Wallet Attestation Issuance (detailed in :ref:`Wallet Attestation Issuance`),
  - Wallet Revocation (detailed in :ref:`Wallet Instance Revocation`) and
  - Deletion of presented attributes (detailed in :ref:`User's Attributes Deletion`).

Each functionality is described in detail in the following sections.

.. note::

  The details provided below are non-normative and are intended to clarify the functionalities of the Wallet Instance Registration. The actual implementation may vary based on the specific use case and requirements of the Wallet Provider.

Wallet Instance Initialization and Registration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This process allows the User who has just installed the Wallet Instance application to register the Wallet Instance with the Wallet Provider backend. During this process, the Wallet Instance application will request a security and integrity assertion from the OS manufacturer, which also binds a long-lived key pair stored in a proper secure storage within the device itself. This assertion will be validated by the Wallet Provider, and if the validation is successful, the Wallet Provider will authenticate the Wallet Instance. For details see :ref:`Mobile Application Instance Initialization`.

.. warning::

  During the registration phase of the Wallet Instance with the Wallet Provider it is also necessary to associate the Wallet Instance with a specific User, authenticating the User with the Wallet Provider. The authentication mechanism is at the discretion of the Wallet Provider and it will not be addressed within these guidelines, as each Wallet Provider may have its User authentication systems already implemented.

.. note::

  The Wallet Provider SHOULD associate the Wallet Instance (through the ``hardware_key_tag`` identifier) with a specific User uniquely identified within the Wallet Provider's systems. This will be useful for the lifecycle of the Wallet Instance and for a future revocation. For details see :ref:`Mobile Application Instance`.

.. include:: wallet-attestation.rst
.. include:: wallet-revocation.rst

User's Attributes Deletion
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This Wallet Instance functionality allows Users to obtain a list of all Relying Parties towards which attributes that can uniquely identify Users (e.g., the tax_id_code claim of the PID) have been presented. Subsequently Users may request deletion of all attributes presented to a Relying Party of their choice. Below the high level flow regarding this interaction is presented.

.. figure:: ../../images/user's_data_deletion_flow.svg
    :figwidth: 100%
    :align: center
    :target: https://www.plantuml.com/plantuml/png/RLBDZjD03BxdAQozS67t0Nf0ksABn0KX5iI5YvCuxOZfE8mzBNrxx2bDcBAtTFpv-_7NHr7CMWwnmwASog6dtE6WdE7kcr2-0nGeOezTpx_1dzu8FDCn3DJDjXg6C6DIkFkECPB2nsICQQ2wYFCCBSe9u6b7II_Cs54QmQWl_5yedaFQmMVRERURsunICi4sZHp-hXFDsg8-q4WPDN1ouBmW9qSkKb0ZmVqxTxWnpqV-IO2gEVH52KQAL3ccaWR_m1ZC3pZSjtnx0ozxFa4Cei1JupoGm8yK4imiGYBEnDFrU4zNcLiRBwOwAEYUsZk0ij5b-bL8wdZrnzFgMbP_ddRJafZmzhqzLH93EWJkhz9r93Cd8RzEOYNW8sMVsc-0hwPwqp1mhnYIrBcxMXkw71wcp0UVLCI154TKDC__HpI4b-EwtHh3hRsg77dd5_vNT4csT8GRFp3wD_azNe4sKRsBjnMw96vhm6A2ISE0Ib8pUACF5Jb5Fi70Dat63IS3BWZOeq1FzY9b64XaAZ6sTED3Uu5gOtN-x7tJMhM7xxaONdcHMRPg-2LkKsp1fVFRV_CdrZ2TBqoFPgKSuXy0

    Sequence Diagram for Deletion of User's Attributes

**Step 1:** The User requests the deletion of attributes invoking the Wallet Instance’s attribute deletion function.

**Step 2:** The Wallet Instance collects all transaction data and shows the User the list of Relying Parties with which it has had interactions throughout the Wallet Instance lifecycle and are in possession of User's attributes. The Wallet Instance SHOULD filter the transaction logs so that only the Relying Parties which have had access to attributes uniquely identifying the User are shown.

**Step 3:** The User selects the target Relying Party for attributes deletion.

**Steps 4 - 5:** The Wallet Instance obtains the Relying Party Entity Configuration at the Federation ./well-known/ endpoint. The URL or the Erasure Endpoint (``erasure_endpoint``) can be found inside the metadata parameter.

**Step 6:** The Wallet Instance logs the Erasure Request’s relevant information. These logs MUST include at least:
  * the date of request,
  * the Relying Party to which the request was made,
  * the attributes requested to be removed.

**Steps 7 - 8:** The Wallet Instance redirects the User to the Erasure Endpoint. It MUST also ensure that a callback mechanism to allow the User-Agent to notify the Wallet Instance (and thus the User) after the Erasure Response is present. Details on the Erasure Request can be found in :ref:`Erasure Request`.

.. note::

  The Relying Party web page will authenticate the User with an appropriate level of assurance using any method such as SPID/CIE or the PID presentation. The specific mechanism used for authentication is left to the Relying Party. Upon authenticating the User, the Relying Party MAY prompt the User to perform additional steps needed for the deletion of attributes, e.g., it might require the User to confirm the deletion operation.

**Step 9:** Upon successful authentication of the User the Relying Party MUST delete all attributes bound to the User in its possession.

**Step 10:** The Relying Party returns the Erasure Response in the form of an HTTP Response to the User-Agent and includes the callback URL if provided in the Erasure Request. Details on the Erasure Response can be found in :ref:`Erasure Response`.

**Steps 11 - 12:**  The User-Agent uses the implemented method to return the Erasure Response to the Wallet Instance. Finally, the User is notified via the Wallet Instance regarding the Erasure Response outcome.

Wallet Provider Endpoints
------------------------------------

The Wallet Provider, responsible for delivering a Wallet Solution, MUST expose the endpoints to support trust establishment and essential Wallet Instance functionalities. These include the ``/.well-known/openid-federation`` Federation Endpoint which MUST adhere to the OpenID Federation 1.0 specification to reliably establish trust with the Wallet Provider’s as well as, endpoints for Wallet Instance registration, nonce generation (required for registration), attestation issuance, and revocation. Aside from the Federation endpoint, the implementation details of the others are left to the Wallet Provider’s discretion.

Federation Endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The ``/.well-known/openid-federation`` endpoint serves as the discovery mechanism for trust establishment by retrieving the Wallet Provider Entity Configuration.

Wallet Provider Entity Configuration
...................................................

An HTTP GET request to the Federation endpoint allows the retrieval of the Wallet Provider Entity Configuration.

The returned Entity Configuration of the Wallet Provider MUST contain the attributes described in the sections below.

The Wallet Provider Entity Configuration is a signed JWT containing the public keys and supported algorithms of the Wallet Provider. It is structured in accordance with the `OID-FED`_ and the :ref:`Trust Model` outlined in this specification.

Wallet Provider Entity Configuration JWT Header
...................................................

.. list-table::
    :widths: 20 60 20
    :header-rows: 1

    * - **Key**
      - **Value**
      - **Reference**
    * - alg
      - Algorithm used to verify the token signature. It MUST be one of the possible values indicated in :ref:`supported_algs` (e.g., ES256).
      - `OID-FED`_.
    * - kid
      - Thumbprint of the public key used for the signature.
      - `OID-FED`_ and :rfc:`7638`.
    * - typ
      - Media type, set to ``entity-statement+jwt``.
      - `OID-FED`_.

Wallet Provider Entity Configuration JWT Payload
.....................................................

.. list-table::
    :widths: 20 60 20
    :header-rows: 1

    * - **Key**
      - **Value**
      - **Reference**
    * - ``iss``
      - REQUIRED. Public URL of the Wallet Provider.
      - `OID-FED`_.
    * - ``sub``
      - REQUIRED. Public URL of the Wallet Provider.
      - `OID-FED`_.
    * - ``iat``
      - REQUIRED. Issuance datetime in Unix Timestamp format.
      - `OID-FED`_.
    * - ``exp``
      - REQUIRED. Expiration datetime in Unix Timestamp format.
      - `OID-FED`_.
    * - ``authority_hints``
      - REQUIRED. Array of URLs (String) containing the list of URLs of the immediate superior Entities, such as the Trust Anchor or an Intermediate, that MAY issue an Entity Statement related to the Wallet Provider.
      - `OID-FED`_.
    * - ``jwks``
      - REQUIRED. A JSON Web Key Set (JWKS) representing the public part of the Wallet Provider's Federation Entity signing keys. The corresponding private key is used by the Entity to sign the Entity Configuration about itself.
      - :rfc:`7517`, `OID-FED`_.
    * - ``metadata``
      - REQUIRED.  JSON object that represents the Entity's Types and the metadata for those Entity Types. Each member name of the JSON object is an Entity Type Identifier, and each value MUST be a JSON object containing metadata parameters according to the metadata schema of the Entity Type. It MUST contains the ``wallet_provider`` and OPTIONALLY the ``federation_entity`` metadata.
      - `OID-FED`_.

wallet_provider metadata
..................................

The metadata JSON Object whose key is ``wallet_provider`` contains the following parameters. The public keys found in this object are exclusively used for signing and/or encryption operations required to this Entity when acting as a Wallet Provider (e.g., sign the Wallet Attestations to the Wallet Instance).

.. list-table::
    :widths: 20 60 20
    :header-rows: 1

    * - **Key**
      - **Value**
      - **Reference**
    * - ``jwks``
      - CONDITIONAL. JSON Web Key Set document, passed by value, containing the Entity's keys for that Entity Type. It MUST be present if ``jwks_uri`` and ``signed_jwks_uri`` are absent.
      - :rfc:`7517`, `OID-FED`_.
    * - ``jwks_uri``
      - CONDITIONAL. URL referencing a JWK Set document containing the Wallet Provider's keys for that Entity Type. This URL MUST use the https scheme. It MUST be present if ``jwks`` and ``signed_jwks_uri`` are absent.
      - `OID-FED`_.
    * - ``signed_jwks_uri``
      - CONDITIONAL. URL referencing a signed JWT having the Entity's JWK Set document for that Entity Type as its payload. This URL MUST use the https scheme. The JWT MUST be signed using a Federation Entity Key. A successful response from the URL MUST use the HTTP status code 200 with the Content Type ``application/jwk-set+jwt``. It MUST be present if ``jwks`` and ``jwks_uri`` are absent.
      - `OID-FED`_.
    * - ``aal_values_supported``
      - OPTIONAL. List of supported values for the certifiable security context. These values specify the security level  of the app, according to the levels: low, medium, or high. Authenticator Assurance Level values supported.
      - This specification.

federation_entity metadata
...................................

.. list-table::
    :widths: 20 60 20
    :header-rows: 1

    * - **Key**
      - **Value**
      - **Reference**
    * - ``organization_name``
      - OPTIONAL.  A human-readable name representing the organization owning the Wallet Provider.
      - `OID-FED`_.
    * - ``homepage_uri``
      - OPTIONAL. URL of a Web page for the organization owning the Wallet Provider.
      - `OID-FED`_.
    * - ``tos_uri``
      - OPTIONAL. URL that contains the Wallet Provider's terms of service.
      - `OID-FED`_.
    * - ``policy_uri``
      - OPTIONAL. URL of the documentation of conditions and policies relevant to the Wallet Provider.
      -  `OID-FED`_.
    * - ``logo_uri``
      - OPTIONAL. String. A URL that points to the logo of the Wallet Provider. The file containing the logo SHOULD be published in a format that can be viewed via the web.
      -  `OID-FED`_.

Below is a non-normative example of the Entity Configuration for a Wallet Provider.

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
            "x": "BxYsu3QvYmOz1fl1l5hGyPWlpvgTzz3AY3j3K_9zGPs",
            "y": "ob34Wmfah_ScQXaYMJWoBkZSwO-kQ0VTgMk4VZfu48w",
            "kid": "749b495837819c00cfee1749b495837819c00cfee1"
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

See :ref:`Mobile Application Nonce Request` and :ref:`Mobile Application Nonce Response` for details on the Nonce Request and Nonce Response.

Wallet Instance Management Endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This is a RESTful API endpoint provided by the Wallet Provider that enables Wallet Instance management, including registration, status retrieval, revocation upon request (e.g., by the User), and deletion.
The following sections describe the registration, status retrieval and revocation requests, along with their corresponding responses, handled by this endpoint, which are required for core :ref:`Wallet Instance Functionalities`.

Wallet Instance Registration Request
.............................................

To register a Wallet Instance, the request to the Wallet Provider MUST use the HTTP POST method with ``Content-Type`` set to `application/json`. The request body MUST contain the claims described in :ref:`Mobile Application Instance Initialization Request`.

Wallet Instance Registration Response
.............................................

If a Wallet Instance Registration Request is successfully validated, the Wallet Provider provides an HTTP Response with status code 204 (No Content). For detatails see :ref:`Mobile Application Instance Initialization Response`.

Wallet Instance Retrieval Request
.............................................

To retrieve all Wallet Instances associated with a User, a request MUST be sent using the HTTP GET method to the Wallet Provider.

.. note::
    For retrieving a specific Wallet Instance, the request MUST include the Wallet Instance ID as a path parameter.


Wallet Instance Retrieval Response
.............................................

If a Wallet Instance Retrieval Request is successfully processed, the Wallet Provider MUST return an HTTP Response with a 200 (OK) status code.
The response body MUST be in JSON format and include the relevant Wallet Instance information, such as its unique ID, status, and issuance date.
When retrieving all Wallet Instances, the response MUST return an array containing the details of all associated instances.

If any errors occur during the retrieval process, an error response MUST be returned. Refer to :ref:`Error Handling for Wallet Instance Management` for details on error codes and descriptions.

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

To revoke an active Wallet Instance, a revocation request MUST be sent using the HTTP PATCH method with Content-Type set to ``application/json``. The request body MUST contain a ``status`` parameter set to ``REVOKED``.

.. note::

  While PATCH is the recommended method, the revocation request MAY also be sent using the POST method, depending on implementation preferences.

Wallet Instance Revocation Response
.............................................
If a Wallet Instance Revocation Request is successfully processed, the Wallet Provider provides an HTTP Response with a 204 (No Content) status code.

If any errors occur during the Wallet Instance Revocation, an error response MUST be returned. Refer to :ref:`Error Handling for Wallet Instance Management` for details on error codes and descriptions.

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

In case of an error, the Wallet Provider MUST return an error response as defined in :rfc:`7231`, with additional details available in :rfc:`7807`. The response MUST use the Content-Type set to ``application/json`` and MUST include the following parameters:

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

The errors in :ref:`Mobile Application Instance Initialization Error Response` MUST be supported for error responses related to **Wallet Instance Registration**.

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

Further details on the Wallet Attestation Issuance Request are provided in the :ref:`Mobile Application Key Binding Request` section.

The ``typ`` header of the Integrity Request JWT assumes the value ``wp-war+jwt``.

.. _wallet_attestation_issuance_response:

Wallet Attestation Issuance Response
.............................................

If the Wallet Attestation Issuance Request is successfully validated, the Wallet Provider returns an HTTP response with a status code of ``200 OK`` and Content-Type ``application/json``. The returned JSON Object MUST possess the ``wallet_attestations`` parameter whose value is an array of JSON Objects (see :ref:`Wallet Attestation Issuance`) containing the Wallet Attestations in JWT, SD-JWT and mdoc format signed by the Wallet Provider. The JWT formatted Wallet Attestation is to be used for the Issuance phase, as an OAuth Client Attestation, and will be sent to the Credential Issuer as discussed in :ref:`pid_eaa_issuance.rst`. The SD-JWT and mdoc formatted Wallet Attestation will instead be used during presentation respectively in the remote (:ref:`remote_flow.rst`) and proximity (:ref:`proximity_flow_sec_main`) flows.


The JSON Object returned in the response has the following claim:

.. list-table::
    :widths: 20 60 20
    :header-rows: 1

    * - **Parameter**
      - **Description**
      - **Reference**
    * - **wallet_attestations**
      - REQUIRED. Contains an array of one or more issued Wallet Attestation. The elements of the array MUST be JSON Objects. At least two JSON Objects MUST be present.
      - This specification.

Each JSON Object contained in the ``wallet_attestations`` array MUST have the following form:

.. list-table::
    :widths: 20 60 20
    :header-rows: 1

    * - **Parameter**
      - **Description**
      - **Reference**
    * - **format**
      - A string identifying the Data Model used to create and represent the Wallet Attestation. It MUST be either ``jwt``, ``dc+sd-jwt`` or ``mso_mdoc`` depending on the credential format.
      - This specification.
    * - **wallet_attestation**
      - A string representing the Wallet Attestation. If

        - the Wallet Attestation is in JWT format, then the claim's value MUST be a string that is a JWT.
        - the Wallet Attestation is in SD-JWT format, then the claim's value MUST be a string that is an SD-JWT VC.
        - the Wallet Attestation is in mdoc format, then the claim's value is the base64url-encoded representation of the CBOR-encoded IssuerSigned structure, as defined in [ISO.18013-5]. This structure MUST contain all Namespaces and IssuerSignedItems that are included in the MobileSecurityObject.

      - This specification.

If any errors occur during the process, an error response is returned. Further details on the error response are provided in the :ref:`Mobile Application Key Binding Error Response` section.


Wallet Attestation JWT
'''''''''''''''''''''''''''''''''''

The JOSE header of the Wallet Attestation JWT contains the following parameters:

.. list-table::
    :widths: 20 60 20
    :header-rows: 1

    * - **JOSE header**
      - **Description**
      - **Reference**
    * - **alg**
      - REQUIRED. A digital signature algorithm identifier such as per IANA "JSON Web Signature and Encryption Algorithms" registry. It MUST be one of the supported algorithms listed in the Section :ref:`Cryptographic Algorithms` and MUST NOT be set to ``none`` or any symmetric algorithm (MAC) identifier.
      - :rfc:`7516#section-4.1.1`.
    * - **kid**
      - REQUIRED. Unique identifier of the public key associated to the private key the Wallet Provider used to sign the Wallet Attestation.
      - :rfc:`7638#section_3`.
    * - **typ**
      - REQUIRED. It MUST be set to ``oauth-client-attestation+jwt``
      - `OPENID4VC-HAIP`_.
    * - **trust_chain**
      - REQUIRED. Sequence of Entity Statements that composes the Trust Chain related to the Wallet Provider.
      - `OID-FED`_ Section 4.3 *Trust Chain Header Parameter*.
    * - **x5c**
      - OPTIONAL. Contains the X.509 public key certificate or certificate chain (:rfc:`5280`) corresponding to the key used to digitally sign the JWT.
      - :rfc:`7515` Section 4.1.8 and `SD-JWT-VC`_ Section 3.5.

The body of the Wallet Attestation JWT contains the following claims:

.. list-table::
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Description**
      - **Reference**
    * - **iss**
      - REQUIRED. Identifier of the Wallet Provider.
      - :rfc:`9126` and :rfc:`7519`.
    * - **exp**
      - REQUIRED. UNIX Timestamp with the expiry time of the JWT.
      - :rfc:`9126` and :rfc:`7519`.
    * - **iat**
      - REQUIRED. UNIX Timestamp with the time of JWT issuance.
      - :rfc:`9126` and :rfc:`7519`.
    * - **cnf**
      - REQUIRED. JSON object, containing the public part of an asymmetric key pair owned by the Wallet Instance.
      - :rfc:`7800`.
    * - **wallet_link**
      - OPTIONAL. String containing a URL to get further information about the Wallet and the Wallet Provider.
      - `OpenID4VCI`_.
    * - **wallet_name**
      - OPTIONAL. String containing a human-readable name of the Wallet.
      - `OpenID4VCI`_.
    * - **sub**
      - REQUIRED. Identifier of the Wallet Instance which is the thumbprint of the Wallet Attestation JWK.
      - :rfc:`9126` and :rfc:`7519`.
    * - **aal**
      - REQUIRED. JSON String asserting the authentication level of the Wallet and the key as asserted in the cnf claim.
      - This specification.

Below is a non-normative example of the SD-JWT Wallet Attestation without encoding and signature applied:

.. code-block::

  {
    "alg": "ES256",
    "kid": "5t5YYpBhN-EgIEEI5iUzr6r0MR02LnVQ0OmekmNKcjY",
    "trust_chain": [
      "eyJhbGciOiJFUz...6S0A",
      "eyJhbGciOiJFUz...jJLA",
      "eyJhbGciOiJFUz...H9gw",
    ],
    "typ": "jwt",
  }
  .
  {
    "iss": "https://wallet-provider.example.org",
    "cnf":
    {
      "jwk":
      {
        "crv": "P-256",
        "kty": "EC",
        "x": "4HNptI-xr2pjyRJKGMnz4WmdnQD_uJSq4R95Nj98b44",
        "y": "LIZnSB39vFJhYgS3k7jXE4r3-CoGFQwZtPBIRqpNlrg"
      }
    },
    "iat": 1687281195,
    "exp": 1687288395,
    "vct": "wallet.atestation.example/v1.0",
    "sub": "vbeXJksM45xphtANnCiG6mCyuU4jfGNzopGuKvogg9c",
    "aal": "https://trust-list.eu/aal/high",
    "wallet_name": "Wallet_v1",
    "wallet_link": "https://example.com/wallet/detail_info.html"
  }


Wallet Attestation SD-JWT
'''''''''''''''''''''''''''''''''''

The JOSE header of the Wallet Attestation SD-JWT MUST contain the following parameters:

.. list-table::
    :widths: 20 60 20
    :header-rows: 1

    * - **JOSE header**
      - **Description**
      - **Reference**
    * - **alg**
      - REQUIRED. A digital signature algorithm identifier such as per IANA "JSON Web Signature and Encryption Algorithms" registry. It MUST be one of the supported algorithms listed in :ref:`Cryptographic Algorithms` and MUST NOT be set to ``none`` or any symmetric algorithm (MAC) identifier.
      - :rfc:`7516#section-4.1.1`.
    * - **kid**
      - REQUIRED. Unique identifier of the public key associated to the private key the Wallet Provider used to sign the Wallet Attestation.
      - :rfc:`7638#section_3`.
    * - **typ**
      - REQUIRED. It MUST be set to ``dc+sd-jwt``
      - `OPENID4VC-HAIP`_.
    * - **trust_chain**
      - REQUIRED. Sequence of Entity Statements that composes the Trust Chain related to the Wallet Provider.
      - `OID-FED`_ Section 4.3 *Trust Chain Header Parameter*.
    * - **x5c**
      - OPTIONAL. Contains the X.509 public key certificate or certificate chain (:rfc:`5280`) corresponding to the key used to digitally sign the JWT.
      - :rfc:`7515` Section 4.1.8 and `SD-JWT-VC`_ Section 3.5.

The body of the Wallet Attestation SD-JWT contains the following claims:

.. list-table::
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Description**
      - **Reference**
    * - **iss**
      - REQUIRED. Identifier of the Wallet Provider.
      - :rfc:`9126` and :rfc:`7519`.
    * - **exp**
      - REQUIRED. UNIX Timestamp with the expiry time of the JWT.
      - :rfc:`9126` and :rfc:`7519`.
    * - **iat**
      - REQUIRED. UNIX Timestamp with the time of JWT issuance.
      - :rfc:`9126` and :rfc:`7519`.
    * - **cnf**
      - REQUIRED. JSON object, containing the public part of an asymmetric key pair owned by the Wallet Instance.
      - :rfc:`7800`.
    * - **vct**
      - REQUIRED. Credential type value MUST be an HTTPS URL String and it MUST be set to ``wallet.atestation.example/v1.0``.
      - Section 3.2.2.2 `SD-JWT-VC`_.
    * - **_sd**
      - REQUIRED. JSON array containing a list of all disclusure's digests.
      - `SD-JWT`_.
    * - **sd_alg**
      - REQUIRED. String containing the hash algorithm used by the Wallet Provider to generate the disclusure's digests.
      - `SD-JWT`_.
    * - **sub**
      - REQUIRED. Identifier of the Wallet Instance which is the thumbprint of the Wallet Attestation JWK.
      - :rfc:`9126` and :rfc:`7519`.
    * - **aal**
      - REQUIRED. JSON String asserting the authentication level of the Wallet and the key as asserted in the cnf claim.
      - This specification.

The following disclosures MAY be present:

.. list-table::
    :widths: 20 60 20
    :header-rows: 1

    * - **Disclosure**
      - **Description**
      - **Reference**
    * - **wallet_link**
      - OPTIONAL. String containing a URL to get further information about the Wallet and the Wallet Provider.
      - `OpenID4VCI`_.
    * - **wallet_name**
      - OPTIONAL. String containing a human-readable name of the Wallet.
      - `OpenID4VCI`_.

Below are described examples of values for the disclosures:

.. **Claim** ``sub``:
..
.. -  SHA-256 Hash: ``DTZRbQgOWJlLaBfe6pr+j1vL4B4t6LLWyt9loaEJKe0=``
.. -  Disclosure: ``WyIyR0xDNDJzS1F2ZUNmR2ZyeU5STjl3IiwgInN1YiIsICJ2YmVYSmtzTTQ1eHBodEFObkNpRzZtQ3l1VTRqZkdOem9wR3VLdm9nZzljIl0=``
.. -  Contents: ``["2GLC42sKQveCfGfryNRN9w", "sub", "vbeXJksM45xphtANnCiG6mCyuU4jfGNzopGuKvogg9c"]``
..
.. **Claim** ``aal``:
..
.. -  SHA-256 Hash: ``h+w4Q4dWcHebykPpS4jRsBZVvBhEKszyLeZGmEunDJ4=``
.. -  Disclosure: ``WyIyR0xDNDJzS1F2ZUNmR2ZyeU5STjl3IiwgImFhbCIsICJodHRwczovL3RydXN0LWxpc3QuZXUvYWFsL2hpZ2giXQ==``
.. -  Contents: ``["2GLC42sKQveCfGfryNRN9w", "aal", "https://trust-list.eu/aal/high"]``

**Claim** ``wallet_link``:

-  SHA-256 Hash: ``cD9/XC7t7QVHvmSiE1dGW0WYr0jcqm8n0GA6MGitaik=``
-  Disclosure: ``WyIyR0xDNDJzS1F2ZUNmR2ZyeU5STjl3IiwgIndhbGxldF9saW5rIiwgImh0dHBzOi8vZXhhbXBsZS5jb20vd2FsbGV0L2RldGFpbF9pbmZvLmh0bWwiXQ==``
-  Contents: ``["2GLC42sKQveCfGfryNRN9w", "wallet_link", "https://example.com/wallet/detail_info.html"]``

**Claim** ``wallet_name``:

-  SHA-256 Hash: ``iQQhzf6+saYCzHH92N1QyJisKsZbApbTrJ1amHgLoOk=``
-  Disclosure:n``WyIyR0xDNDJzS1F2ZUNmR2ZyeU5STjl3IiwgIndhbGxldF9uYW1lIiwgIldhbGxldF9Ib2JiaXRvbl92MSJd``
-  Contents: ``["2GLC42sKQveCfGfryNRN9w", "wallet_name", "Wallet_v1"]``

Below is a non-normative example of the SD-JWT Wallet Attestation without encoding and signature applied:

.. code-block::

  {
    "alg": "ES256",
    "kid": "5t5YYpBhN-EgIEEI5iUzr6r0MR02LnVQ0OmekmNKcjY",
    "trust_chain": [
      "eyJhbGciOiJFUz...6S0A",
      "eyJhbGciOiJFUz...jJLA",
      "eyJhbGciOiJFUz...H9gw"
    ],
    "typ": "dc+sd-jwt"
  }
  .
  {
    "iss": "https://wallet-provider.example.org",
    "cnf": {
      "jwk":
      {
        "crv": "P-256",
        "kty": "EC",
        "x": "4HNptI-xr2pjyRJKGMnz4WmdnQD_uJSq4R95Nj98b44",
        "y": "LIZnSB39vFJhYgS3k7jXE4r3-CoGFQwZtPBIRqpNlrg"
      }
    },
    "_sd": ["cD9/XC7t7QVHvmSiE1dGW0WYr0jcqm8n0GA6MGitaik=", "iQQhzf6+saYCzHH92N1QyJisKsZbApbTrJ1amHgLoOk="],
    "_sd_alg": "sha-256",
    "iat": 1687281195,
    "exp": 1687288395,
    "vct": "https://wallet.attestation.example/v1.0",
    "sub": "vbeXJksM45xphtANnCiG6mCyuU4jfGNzopGuKvogg9c",
    "aal": "https://trust-framework.example.it/aal/high"
  }

Wallet Attestation mdoc
'''''''''''''''''''''''''''''''''''

This description further specializes the guidelines given in `MDOC-CBOR Credential Format` to represent the Wallet Attestation in mdoc format. The latter MUST:

- have the domestic namespace ``org.iso.18013.5.1.it``;
- have **docType** set to ``org.iso.18013.5.1.it.WalletAttestation``; and
- have **issuerAuth** as described in :ref:`Mobile security Object`.

The ``nameSpaces`` for the domestic nameSpace Json Objects are defined as follows:

.. list-table:: org.iso.18013.5.1.it
    :widths: 20 60 20
    :header-rows: 1

    * - **elementIdentifier**
      - **Description**
      - **Reference**
    * - **sub**
      - REQUIRED. Identifier of the Wallet Instance which is the thumbprint of the Wallet Attestation COSE Key.
      - :rfc:`9126` and :rfc:`7519`.
    * - **aal**
      - JSON String asserting the authentication level of the Wallet Instance in relation to the COSE Key contained in the ``IssuerAuth.deviceKeyInfo.deviceKey`` claim of the **issuerAuth** Object.
      - :rfc:`9679`.
    * - **wallet_link**
      - JSON String containing a URL to get further information about the Wallet and the Wallet Provider.
      - `OpenID4VCI`_.
    * - **wallet_name**
      - JSON String, it MUST be the Identifier of the Wallet Provider.
      - `OpenID4VCI`_.

Below is a non-normative example of the mdoc Wallet Attestation in CBOR diagnostic notation:

.. code-block::

  {
    "docType": "org.iso.18013.5.1.it.WalletAttestation",
    "issuerSigned":{
      "nameSpaces":{
        "org.iso.18013.5.1.it":[
          24(<< {
          "digestID": 0,
          "random": h'960CB15A…E902807AA95',
          "elementIdentifier": "wallet_name",
          "elementValue": "Wallet_v1"
          } >>),
          24(<<
          {
          "digestID": 1,
          "random": h'9D3774BD59…A4F76A',
          "elementIdentifier": "wallet_link",
          "elementValue":"https://example.com/wallet/detail_info.html"
          } >>),
          24(<< {
          "digestID": 2,
          "random": h'AE84834F3…A3E4FCCE',
          "elementIdentifier": "sub",
          "elementValue":"vbeXJksM45xphtANnCiG6mCyuU4jfGNzopGuKvogg9c"
          } >>),
          24(<<
          {
          "digestID": 3,
          "random": h'9D3774BD59…A4F76A',
          "elementIdentifier": "aal",
          "elementValue":"https://trust-list.eu/aal/high"
          } >>)
        ]
  },
    "issuerAuth": [
      << {1: -7} >>,
      {
      33: h'30820215308201BCA003020102021404AD30C…'
      },
      <<
        24(<<
          {
            "docType":"org.iso.18013.5.1.it.WalletAttestation",
            "version": "org.iso.18013.5.1.it",
            "validityInfo": {
              "signed": "2023-02-22T06:23:56Z"
              "validFrom": "2023-02-22T06:23:56Z",
              "validUntil": "2024-02-22T00:00:00Z"
            },
            "valueDigests": {
              "org.iso.18013.5.1.it": {
                0: h'0F1571A988FCDF2929…',
                1: h'0CDFE0774A2B596C90…',
                2: h'E23821492558984395…',
                3: h'BBC77E6CCE544EDF86…'
              }
            },
            "deviceKeyInfo": {
              "deviceKey": {
                1: 2,
                -1: 1,
                -2: h'B820963964E5…',
                -3: h'0A6DA0AF437E…'
              }
            },
            "digestAlgorithm": "SHA-256"
          }
        >>)
      >>,
      h'1AD0D6A7313EFDC…43DEBF48BF5A580D'
    ]
  }

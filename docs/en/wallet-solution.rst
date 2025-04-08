.. include:: ../common/common_definitions.rst

.. _wallet-solution.rst:

Wallet Solution
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Wallet Solution is issued by the Wallet Provider in the form of a mobile app and services, such as web interfaces. The mobile app serves as the primary interface for Users, allowing them to hold their Digital Credentials and interact with other participants of the ecosystem, such as Credential Issuers and Relying Parties. These Credentials are a set of data that can uniquely identify a natural or legal person, along with other Qualified and non-qualified Electronic Attestations of Attributes, also known as QEAAs and EAAs respectively, or (Q)EAAs for short. Once a User installs the mobile app on their device, such an installation is referred to as a Wallet Instance for the User. By supporting the mobile app, the Wallet Provider ensures the security and reliability of the entire Wallet Solution, as it is responsible for issuing the Wallet Attestation, which is a cryptographic proof about the authenticity and integrity of the Wallet Instance.

Wallet Solution Requirements
-----------------------------

This section lists the requirements that Wallet Providers, Wallet Solutions, and their Wallet Instances must meet.

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

  Throughout this section, the services used to attest genuineness of the Wallet Instance and the device in which it is installed are referred to as **Key Attestation API**. The Key Attestation API is considered in an abstract fashion and it is assumed to be a service provided by a trusted third party (i.e., the OS Provider's API) which is able to perform integrity checks on the Wallet Instance as well as on the device where it is installed.

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
A Wallet Instance, MUST support three fundamental functionalities: Registration, Attestation Issuance, and Revocation. Each functionality is described in detail in the following sections.

.. note::

  The details provided below are non-normative and are intended to clarify the functionalities of the Wallet Instance Registration. The actual implementation may vary based on the specific use case and requirements of the Wallet Provider.

Wallet Instance Initialization and Registration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This process allows the User who has just installed the Wallet Instance application to register the Wallet Instance with the Wallet Provider backend. During this process, the Wallet Instance application will request a security and integrity assertion from the OS manufacturer, which also binds a long-lived key pair stored in a proper secure storage within the device itself. This assertion will be validated by the Wallet Provider, and if the validation is successful, the Wallet Provider will authenticate the Wallet Instance. For details see :ref:`mobile-instance-app-initialization-and-registration.rst`.

.. include:: wallet-attestation.rst
.. include:: wallet-revocation.rst


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

Below is a non-normative example of the Entity Configuration for a Wallet PRovider.

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

See :ref:`Nonce Request` and :ref:`Nonce Response` for details on the Nonce Request and Nonce Response.

Wallet Instance Management Endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This is a RESTful API endpoint provided by the Wallet Provider that enables Wallet Instance management, including registration, status retrieval, revocation upon request (e.g., by the User), and deletion.
The following sections describe the registration, status retrieval and revocation requests, along with their corresponding responses, handled by this endpoint, which are required for core :ref:`Wallet Instance Functionalities`.

Wallet Instance Registration Request
.............................................

To register a Wallet Instance, the request to the Wallet Provider MUST use the HTTP POST method with ``Content-Type`` set to `application/json`. The request body MUST contain the claims described in :ref:`Mobile Application Instance Initialization Request`.

.. warning::
  During the registration phase of the Wallet Instance with the Wallet Provider it is also necessary to associate the Wallet Instace with a specific User, authenticating the User with the Wallet Provider. The authentication mechanism is at the discretion of the Wallet Provider and it will not be addressed within these guidelines, as each Wallet Provider may have its User authentication systems already implemented.

Wallet Instance Registration Response
.............................................

If a Wallet Instance Registration Request is successfully validated, the Wallet Provider provides an HTTP Response with status code 204 (No Content). For detatails see :ref:`Mobile Application Instance Initialization Response`.

.. note::

  The Wallet Provider SHOULD associate the Wallet Instance (through the ``hardware_key_tag`` identifier) with a specific User uniquely identified within the Wallet Provider's systems. This will be useful for the lifecycle of the Wallet Instance and for a future revocation.

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

The request to the Wallet Provider MUST use the HTTP POST method with Content-Type set to ``application/json``. The request body MUST contain an ``assertion`` parameter whose value is a signed JWT of the Wallet Attestation Request, including all header parameters and body claims described below.

Wallet Attestation Request JWT
...................................

The JOSE header of the Wallet Attestation Request JWT MUST contain the following parameters:

.. list-table::
    :widths: 20 60 20
    :header-rows: 1

    * - **JOSE header**
      - **Description**
      - **Reference**
    * - **alg**
      - A digital signature algorithm identifier such as per IANA "JSON Web Signature and Encryption Algorithms" registry. It MUST be one of the supported algorithms listed in the :ref:`Cryptographic Algorithms` and MUST NOT be set to ``none`` or any symmetric algorithm (MAC) identifier.
      - :rfc:`7516#section-4.1.1`.
    * - **kid**
      -  Thumbprint of the Wallet Instance's JWK contained in the ``cnf`` claim.
      - :rfc:`7638#section_3`.
    * - **typ**
      -  It MUST be set to ``war+jwt``
      - This specification.

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
    * - **nonce**
      - ``nonce`` obtained from the Nonce endpoint.
      - This specification.
    * - **hardware_signature**
      - The signature of ``client_data`` obtained using Cryptographic Hardware Key base64 encoded.
      - This specification.
    * - **key_attestation**
      - The key attestation obtained from the **Key Attestation API** with the holder binding of ``client_data``.
      - This specification.
    * - **hardware_key_tag**
      - Unique identifier of the **Cryptographic Hardware Keys**.
      - This specification.
    * - **cnf**
      - JSON object, containing the public part of an asymmetric key pair owned by the Wallet Instance. This is the public key to which the Wallet Attestations returned shall be bound.
      - :rfc:`7800`.

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


If any errors occur during the Wallet Attestation Issuance, an error response MUST be returned. Refer to :ref:`Error Handling for Wallet Attestation Issuance` for details on error codes and descriptions.
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

Wallet Attestation JWT
...................................

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
...................................

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
      - REQUIRED. String containing the hash algorithm used by the Wallet Provider to generate the digests.
      - `SD-JWT`_.
    * - **sd_alg**
      - REQUIRED. JSON array containing a list of the signing algorithms (alg values) supported.
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
...................................

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
          } >>),
          24(<<
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
     - The provided nonce is invalid, expired, or already used.
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

Wallet Solution Test Plan
-----------------------------

This section provides a comprehensive set of test cases for verifying conformance of a Wallet Solution implementation to the technical rules defined in the IT Wallet ecosystem. The test plan is based on the mandatory requirements (MUST statements) extracted from the following documents:

- Wallet Solution
- Wallet Instance Revocation
- Wallet Attestation Issuance
- Backup and Restore

The purpose of the test plan is to support implementers, auditors, and conformance test environments in validating the behavior of the Wallet under various operational and security scenarios. All test cases are derived from normative rules defined in the above specifications, with no assumptions or extensions. Please note that this is a draft list and is subject to future changes.

Structure of the Table
~~~~~~~~~~~~~~~~~~~~~~

Each test case is identified by a unique test ID (e.g., WS-001) and categorized by functional domain such as Security, Backup & Restore, Credential Issuance, Credential Presentation, Attestation, Revocation, and User Interaction.

For each test case, the table specifies:

- **Test Case**: a unique identifier.
- **Category**: the functional area covered by the test.
- **Description**: the requirement being tested, always based on a normative MUST from the specification.
- **Expected Result**: the expected outcome when the Wallet is implemented correctly.

.. list-table::
   :widths: 10 15 40 35
   :header-rows: 1

   * - Test Case
     - Category
     - Description
     - Expected Result
   * - WS-001
     - Wallet Initialization
     - The Wallet Solution MUST ensure that each Wallet Instance is generated according to the specifications and includes a unique identifier, cryptographic keys, and secure element binding.
     - A compliant Wallet Instance is generated with correct identifiers and secure bindings.
   * - WS-002
     - User Interaction
     - The Wallet Solution MUST request and obtain explicit User Consent during Wallet Instance initialization.
     - The Wallet Instance is activated only after obtaining verifiable User Consent.
   * - WS-003
     - Security
     - The Wallet Solution MUST store private keys within a Secure Hardware Element or equivalent secure storage.
     - All private key material is inaccessible from the operating system or any application outside the Wallet Solution.
   * - WS-004
     - Attestation
     - The Wallet MUST be capable of generating and presenting a Wallet Attestation when required by Verifiers or Issuers.
     - Valid, verifiable Attestations are generated including integrity and origin proofs.
   * - WS-005
     - Attestation
     - The Wallet MUST support processing Wallet Attestation Requests and generating appropriate responses in compliance with eIDAS 2.0.
     - The Wallet correctly interprets and fulfills attestation requests including subject data and cryptographic signatures.
   * - WS-006
     - Credential Presentation
     - The Wallet Solution MUST implement the Verifier flow, ensuring Verifiable Credential selection, integrity, and User interaction.
     - Verifiable Credential presentation is successful, correct, and under User control.
   * - WS-007
     - Credential Issuance
     - The Wallet MUST support the Issuer flow for receiving and storing Verifiable Credentials.
     - Credentials are securely stored and correctly parsed as per defined structure.
   * - WS-008
     - Revocation
     - The Wallet MUST allow the User to trigger a Wallet Instance Revocation at any time.
     - Revocation is executed and cryptographic material is securely deleted or rendered unusable.
   * - WS-009
     - Revocation
     - Upon Wallet Instance Revocation, the Wallet Solution MUST notify the relevant backend systems to propagate revocation.
     - Revocation status is reflected in all ecosystem components (e.g., Issuers, Verifiers).
   * - WS-010
     - Backup & Restore
     - The Wallet MUST support encrypted Backup and Restore operations in compliance with privacy and integrity requirements.
     - Backup is encrypted and tied to the User; Restore operation verifies integrity and User authenticity before recovery.
   * - WS-011
     - Backup & Restore
     - The Wallet MUST manage backup encryption keys securely and derive them from User-controlled secrets or credentials.
     - No unauthorized entity can decrypt backups; backups are rendered useless if tampered with.
   * - WS-012
     - Backup & Restore
     - The Wallet MUST authenticate the User before allowing Restore.
     - Successful Restore only occurs upon verified User authentication using approved methods (e.g., biometrics, PIN, cryptographic challenge).
   * - WS-013
     - Attestation
     - The Wallet MUST detect expired Attestations and support refresh workflows.
     - Expired Attestations are not used; refresh is triggered automatically or via User prompt.
   * - WS-014
     - Compliance
     - All operations including Issuance, Presentation, Attestation, and Revocation MUST comply with the European standards.
     - Auditable trace of compliant operations is maintained; no deviation from eIDAS 2.0 behavior is observed.
   * - WS-015
     - User Interaction
     - The Wallet MUST operate under the principle of User control and data minimization.
     - Only explicitly consented and required data is used and transmitted; all operations require explicit User actions.
   * - WS-016
     - Credential Presentation
     - The Wallet MUST support offline Verifiable Credential presentation when allowed.
     - Credentials are presented securely even in offline mode, with integrity and authenticity maintained.
   * - WS-017
     - Security
     - The Wallet MUST ensure anti-replay protections during credential presentation.
     - Each presentation is cryptographically unique and bound to the Verifier request.
   * - WS-018
     - Revocation
     - The Wallet MUST log and make auditable the revocation process of Wallet Instances.
     - Complete, tamper-evident logs are available for inspection upon request.
   * - WS-019
     - Security
     - The Wallet MUST establish mutually authenticated and encrypted channels during all interactions.
     - All messages are protected against interception, modification, or impersonation.
   * - WS-020
     - Security
     - The Wallet MUST lock itself and/or revoke the Wallet Instance upon detection of tampering.
     - Wallet becomes inoperable and revocation is triggered if tampering is confirmed.
   * - WS-021
     - Security
     - The Wallet MUST perform Device Attestation using platform-specific mechanisms such as Play Integrity (Android) or DC App Attest (iOS) during Wallet Instance creation.
     - Device Attestation is successful and results are included in the Wallet Attestation payload.
   * - WS-022
     - Attestation
     - The Wallet Attestation MUST include a signature using the Wallet Binding Key, and the certificate chain MUST be verifiable to a trusted root.
     - Signature is present, valid, and verifiable using the provided certificate chain.
   * - WS-023
     - Attestation
     - The Wallet MUST include a Device Attestation result in the Wallet Attestation structure.
     - A valid Device Attestation object (Play Integrity or DC App Attest result) is embedded in the Attestation.
   * - WS-024
     - Backup & Restore
     - During Restore, the Wallet MUST validate the integrity of the encrypted backup file using an integrity check mechanism.
     - The Wallet refuses to restore a tampered or corrupted backup file.
   * - WS-025
     - Revocation
     - In case of Wallet Instance Revocation, the Wallet MUST delete any locally stored Verifiable Credentials.
     - No credential data remains accessible after revocation is triggered.
   * - WS-026
     - Revocation
     - The Wallet MUST notify the Wallet Backend with a Revocation Request that includes a valid proof of possession of the Wallet Binding Key.
     - The Revocation Request is accepted and revocation status is updated in the backend.
   * - WS-027
     - Security
     - The Wallet MUST prevent reuse of revoked Wallet Binding Keys or credentials in future Wallet Instances.
     - Any reuse attempt is detected and blocked.
   * - WS-028
     - Attestation
     - The Wallet MUST support Attestation refresh via the defined API exposed by the Wallet Backend.
     - Attestation is renewed and the new version is accepted by Verifiers and Issuers.
   * - WS-029
     - Backup & Restore
     - Backup encryption MUST use strong, standards-compliant encryption algorithms (e.g., AES-GCM).
     - Encrypted backup file is resistant to brute-force and known cryptographic attacks.
   * - WS-030
     - User Interaction
     - The Wallet MUST prompt the User to confirm intent before any destructive operation such as Revocation or Credential Deletion.
     - Destructive actions are only performed after explicit User confirmation.
   * - WS-031
     - Attestation
     - The Wallet MUST generate a Wallet Attestation containing information about the device integrity status, using Play Integrity API on Android.
     - Wallet Attestation includes a valid Play Integrity payload with 'MEETS_DEVICE_INTEGRITY' field set.
   * - WS-032
     - Attestation
     - The Wallet MUST generate a Wallet Attestation using DeviceCheck App Attest on iOS and include the attestation result in the Wallet Attestation.
     - Wallet Attestation includes a valid DC App Attest JWT response signed by Apple.
   * - WS-033
     - Security
     - The Wallet MUST verify that the Play Integrity token signature is valid and issued by Google.
     - The Wallet rejects invalid or forged Play Integrity tokens.
   * - WS-034
     - Security
     - The Wallet MUST validate that the 'nonce' value used in Play Integrity is cryptographically bound to the Wallet Instance.
     - Any tampering with the nonce is detected and leads to Attestation rejection.
   * - WS-035
     - Attestation
     - The Wallet MUST send the Wallet Attestation to the Wallet Backend during registration.
     - Wallet Backend receives the attestation and verifies its validity.
   * - WS-036
     - Backup & Restore
     - The Wallet MUST encrypt backups using a symmetric key derived from User secrets.
     - The backup cannot be decrypted without the original User authentication material.
   * - WS-037
     - Backup & Restore
     - The Wallet MUST include metadata in the backup that identifies the version and creation timestamp.
     - Restore process reads and verifies backup metadata before proceeding.
   * - WS-038
     - Revocation
     - The Wallet MUST send a signed Revocation Request including the Wallet Binding Key signature to the Backend.
     - The backend processes the revocation and updates the Wallet status to revoked.
   * - WS-039
     - Revocation
     - The Wallet MUST not allow any further Credential Issuance or Presentation after revocation.
     - All operations are blocked once the Wallet is revoked.
   * - WS-040
     - Credential Issuance
     - The Wallet MUST validate the structure of the Credential Offer received from the Issuer.
     - The Wallet only accepts Credential Offers that match the expected format and signature.
   * - WS-041
     - Credential Issuance
     - The Wallet MUST ensure that the User consents to receiving a new Credential.
     - No Credential is stored without explicit User approval.
   * - WS-042
     - Credential Presentation
     - The Wallet MUST verify the Verifier’s Presentation Request before responding.
     - Invalid or malformed requests are rejected.
   * - WS-043
     - Security
     - The Wallet MUST sign Verifiable Presentations with the correct private key bound to the Wallet Instance.
     - Verifiers are able to validate the signature and trust the presentation.
   * - WS-044
     - User Interaction
     - The Wallet MUST prompt the User before sending a Verifiable Credential to a Verifier.
     - No credential is shared without explicit User confirmation.
   * - WS-045
     - Backup & Restore
     - The Wallet MUST allow the User to delete all stored backup data.
     - All backup material is securely deleted and cannot be recovered.
   * - WS-046
     - Revocation
     - If the Wallet is restored on a new device, it MUST check whether the original Wallet Instance was revoked.
     - Revoked Wallet Instances cannot be restored.
   * - WS-047
     - Security
     - The Wallet MUST verify the time validity of received Credentials (e.g., issuanceDate, expirationDate).
     - Expired credentials are marked as invalid and are not used.
   * - WS-048
     - Attestation
     - The Wallet MUST include the public key of the Wallet Binding Key in the Wallet Attestation.
     - Verifiers and Issuers can validate signatures made with the corresponding private key.
   * - WS-049
     - Credential Presentation
     - The Wallet MUST support selective disclosure of Credential attributes.
     - Only selected fields are included in the presentation sent to the Verifier.
   * - WS-050
     - Credential Presentation
     - The Wallet MUST allow the User to preview which Credential attributes will be disclosed before confirmation.
     - User is shown the exact data to be shared and approves it explicitly.
   * - WS-051
     - Proximity Flow
     - The Wallet MUST initiate the proximity flow only after explicit User Consent to interact with a Mobile Relying Party Instance.
     - The Wallet proximity presentation flow is blocked unless User has approved the request.
   * - WS-052
     - Proximity Flow
     - The Wallet MUST validate the Access Certificate presented by a Mobile Relying Party Instance before proceeding.
     - If the Access Certificate is missing, invalid or expired, the Wallet MUST refuse the request.
   * - WS-053
     - Proximity Flow
     - The Wallet MUST display a disclaimer when the Access Certificate is expired but still within the allowed grace period.
     - The disclaimer is shown clearly to the User and presentation proceeds only after consent.
   * - WS-054
     - Relying Party Instance
     - The Wallet MUST enforce the check that the Relying Party Instance state is 'Verified' before allowing credential presentation.
     - The Wallet denies the flow if the Relying Party Instance is in any state other than 'Verified'.
   * - WS-055
     - Security
     - The Wallet MUST log any failed presentation attempt due to invalid Relying Party Instance state or expired Access Certificate.
     - A security event log is generated and stored securely.
   * - WS-056
     - Interoperability
     - The Wallet MUST support communication with Relying Party Instances using standardized QR codes for session negotiation as defined in the specification.
     - The Wallet successfully reads and parses QR codes and initiates the session as per protocol.
   * - WS-057
     - Proximity Flow
     - The Wallet MUST establish a secure and authenticated session with the Mobile Relying Party Instance using ephemeral keys before presentation.
     - Session keys are negotiated and verified, and all communication is encrypted.
   * - WS-058
     - Credential Presentation
     - The Wallet MUST allow the User to choose which Credential to present to a Relying Party Instance even in proximity flow.
     - Credential selection interface is shown to the User during proximity flow.
   * - WS-059
     - Security
     - The Wallet MUST abort the session if the Relying Party Instance fails to prove possession of the private key associated with the Access Certificate.
     - Session is terminated and no Credential data is disclosed.
   * - WS-060
     - User Interaction
     - The Wallet MUST clearly indicate to the User when a presentation request comes from a Mobile Relying Party Instance using a proximity channel.
     - The source of the request is shown before allowing presentation to proceed.


.. .. _Trust Model: trust.html
.. _Wallet Attestation Issuance: wallet-solution.html#wallet-attestation-issuance
.. _Wallet Instance Initialization and Registration: wallet-solution.html#wallet-instance-initialization-and-registration
.. _Transition to Operational: wallet-solution.html#transition-to-operational
.. _Trusty: https://source.android.com/docs/security/features/trusty
.. _Secure Enclave: https://support.apple.com/en-gb/guide/security/sec59b0b31ff/web
.. _Wallet Provider metadata: wallet-solution.html#wallet-provider-metadata
.. _Wallet Attestation Issuance endpoint: wallet-solution.html#wallet-attestation-issuance-endpoint
.. _Federation endpoint: wallet-solution.html#federation-endpoint
.. _Wallet Instance Functionalities: wallet-solution.html#wallet-instance-functionalities
.. _Error Handling for Wallet Instance Management: wallet-solution.html#error-handling-for-wallet-instance-management
.. _Error Handling for Wallet Attestation Issuance: wallet-solution.html#error-handling-for-wallet-attestation-issuance
.. _Error Handling for Nonce Generation: wallet-solution.html#error-handling-for-nonce-generation


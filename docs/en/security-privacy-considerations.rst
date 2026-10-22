.. include:: ../common/common_definitions.rst
.. include:: ../common/symbols.rst
.. Included via index.rst at title level '=' (document title).

Security and Privacy Considerations
===================================

This section provides an informal security analysis of the IT-Wallet specification by analyzing the compliance with the security and privacy requirements identified in [`OpenID4VC-SecTrust`_].

.. note::

  As [`OpenID4VC-SecTrust`_] is still a work in progress, the security and privacy considerations described may change in the future.

.. note::
  The focus of the analysis is the compliance of the design choices in the IT-Wallet specification with respect to the OpenID4VC protocols.
  It is currently out-of-scope *(i)* the analysis of the design of the proximity flow based on ISO 18013-5, and *(ii)* the analysis of the implementation.
  As a consequence 7 requirements specifically related to the implementation are not considered (e.g., SV-00: The Verifier must implement the protocol securely and correctly).

As in [`OpenID4VC-SecTrust`_], all requirements are numbered for reference. Together with the respective component that needs to implement the requirement:

* **CF**: Credential Format.
* **P**: Protocol.
* **E**: Ecosystem.
* **I**: Issuer.
* **V**: Verifier.
* **W**: Wallet.

This specification adds the requirement category as a prefix:

* **SR**: Security Requirements.
* **PR**: Privacy Requirements.
* **SPR**: Security and Privacy Requirements.

The final identifier uses the following name space: *requirement_category-component-id*.

For each requirement defined below, this section uses the description defined in [`OpenID4VC-SecTrust`_], specifying whether the requirement is satisfied (fully satisfied: |check-icon|, partially satisfied: |partially-check-icon|, and not satisfied: |uncheck-icon|).
In the following, the requirements are grouped based on their category.

Security Requirements
---------------------

SR-CF-10 and SR-E-10
^^^^^^^^^^^^^^^^^^^^
.. list-table::
   :widths: 8 92

   * - |check-icon|
     - For any presentation, the Credential format and Trust Framework must be designed in a secure way to determine the Issuer and to check that the original Credential was issued by this Issuer (e.g., by using a cryptographic signature).

The IT-Wallet specification supports both SD-JWT VC and mdoc-CBOR Credential formats. The authenticity and integrity of a Credential is checked by verifying the Credential Issuer's signature.

- For SD-JWT, the verification uses the algorithm specified in the **alg** header parameter of SD-JWT. The verification also uses a verifiable reference to the public key for the signature verification. Using OpenID Federation, that reference is the **kid** header of the SD-JWT. The cryptographic material is obtained from the Trust Chain about the Credential Issuer, specified in the **iss** claim.
- For mdoc-CBOR, the Credential Issuer's signature is contained in the *Mobile Security Object* (MSO). The signature is validated using the Credential Issuer's public key. The key is taken from a trusted certificate chain in the **x5chain** header parameter.

SR-CF-20
^^^^^^^^
.. list-table::
   :widths: 8 92

   * - |check-icon|
     - For any presentation, the Credential format must ensure that the data that is tied to the original Credential cannot be altered (e.g., by using a cryptographic signature.)

The cryptographic signature included in the Credential format ensures that any tampering with the Credential will result in a failed verification.

SR-CF-21
^^^^^^^^
.. list-table::
   :widths: 8 92

   * - |check-icon|
     - For cryptographic Holder binding, the presentation format requires the Holder to demonstrate possession of the private key associated with the Credential. This is typically achieved by having the Holder sign a challenge, which consists of a nonce value and the Verifier's unique identifier.

Both SD-JWT and mdoc-CBOR support cryptographic Holder binding by defining how a Holder can present a Credential to a Relying Party, providing cryptographic proof of legitimate possession of the Credential.

Currently, for the remote flow, IT-Wallet supports only SD-JWT presentations. In this scenario, the KB-JWT (Key-Bound JWT) parameter is utilized to demonstrate that the Holder possesses the private key associated with the Credential. The Holder signs the KB-JWT using a **nonce** and a Relying Party identifier, using the **aud** parameter, as a challenge.

SR-E-20
^^^^^^^
.. list-table::
   :widths: 8 92

   * - |check-icon|
     - The Trust Framework must ensure that the identification of an Issuer is unique and unambiguous. If there are multiple instances of the same Issuer using the same key material, the Verifier must trust all instances equally.

The IT Wallet Trust Framework ensures that each entity (for example, a Credential Issuer) is uniquely identified through cryptographic keys and metadata. The keys and metadata are distributed via a verifiable attestation, such as the OpenID Federation Entity Configuration verified within a Trust Chain.

SR-E-30
^^^^^^^
.. list-table::
   :widths: 8 92

   * - |check-icon|
     - The way in which the Verifier determines the trustworthiness of the Issuer defined in the Trust Framework must be secured from influence by a malicious party that can, for example, introduce untrustworthy entities into a directory.

Credential Issuers are registered by a Trust Anchor or its Intermediate. To verify the trust of a Credential Issuer, a Relying Party must verify that the Trust Chain related to the Credential Issuer is valid and still active. This validation process ensures that only trusted entities are permitted to participate in the system, preventing the introduction of untrustworthy actors.

SR-E-40
^^^^^^^
.. list-table::
   :widths: 8 92

   * - |check-icon|
     - The Trust Framework must ensure that there is a way for Verifiers to keep their information on trusted Issuers up to date and that there is a way to revoke trust in an Issuer.

If a Credential Issuer's Entity Statement is revoked or unavailable, means that Credential Issuer is no longer considered valid within the federation. This ensures that Relying Parties have real-time access to the status of trusted entities and can revoke trust if necessary. However, Relying Parties must actively check the Credential Issuer's status by querying federation endpoints (i.e., the fetch endpoint for obtaining the Subordinate Statement).

SR-I-10
^^^^^^^
.. list-table::
   :widths: 8 92

   * - |check-icon|
     - The Issuer must authenticate and identify the User properly according to the expectations of the Verifier (which may be defined in a specification, Trust Framework, or by convention).

The issuance process utilizes OAuth 2.0-based flows, specifically the Authorization Code Flow, to securely authenticate the User. Moreover, the User authentication is performed using CieID scheme with high LoA, eID Substantial Authentication with MRTD Verification or the PID/IT-Wallet ID.

SR-I-20
^^^^^^^
.. list-table::
   :widths: 8 92

   * - |check-icon|
     - The Issuer must only use correct and up-to-date claims about the User into the Credential where verified data is expected.

When verified data is expected, the Credential Issuer obtains the correct and up-to-date claims from the relevant Authentic Sources, ensuring their accuracy at the time of issuance.

SR-I-30
^^^^^^^
.. list-table::
   :widths: 8 92

   * - |check-icon|
     - The Issuer must revoke a Credential once the Issuer learns about potential abuse of the Credential.

The Credential Issuer is the entity responsible for revoking a Credential. The specification describes several use cases that may trigger a revocation process. The specification details the revocation flow in which the Credential Issuer revokes Credentials at the User's request (through the Wallet Instance) after verifying possession of the Credentials.

SR-I-40
^^^^^^^
.. list-table::
   :widths: 8 92

   * - |check-icon|
     - The Issuer must only include Holder-binding data into the Credential that is tied to the actual User (and not, e.g., include a cryptographic key under control by a third party).

The issuance process securely binds the Credential to the User as follows (see :numref:`fig_Low-Level-Flow-ITWallet-PID-QEAA-Issuance`).

* Authorization (Steps 8-10): The Wallet Instance sends an authorization request. The Credential Issuer authenticates the User using a CieID scheme or a valid PID/IT-Wallet ID. The Credential Issuer provides the Access Token to the User.
* Proof of Key Possession (Steps 12-13, 16-17): The Wallet creates a DPoP Proof JWT, binding the Access Token to the Wallet Instance. The same key is then used later to request the Credential, ensuring continuity of ownership.
* Credential Issuance (Steps 18-21): The Credential request is verified using proof of possession, which is cryptographically bound to the User. The use of the same key in the DPoP ensures that the key material is controlled by the Wallet Instance, and not by a third party.

SR-I-50
^^^^^^^
.. list-table::
   :widths: 8 92

   * - |check-icon|
     - (conditional w.r.t I-10) The Issuer must ensure that the Credential was stored in a secure Wallet.

A trusted Wallet Attestation ensures that the Wallet Instance is secure and meets the required security standards before any Credentials are issued or stored.
In Steps 5-6 of :numref:`fig_Low-Level-Flow-ITWallet-PID-QEAA-Issuance`, the Wallet Instance provides a Wallet Attestation, which includes a proof of possession
signed with the Wallet's private key. This attestation confirms that the Wallet Instance is genuine and has been verified by the Wallet Provider.

The Credential Issuer verifies this attestation before allowing the Wallet to participate in the issuance process, ensuring that the Wallet adheres to specific security standards.
Afterward, all cryptographic keys generated and used in the process come from this attested Wallet Instance.

.. note::
  There is currently an open issue on this aspect (https://github.com/openid/OpenID4VCI/issues/355) in the OpenID4VCI spec.

SR-P-20
^^^^^^^
.. list-table::
   :widths: 8 92

   * - |check-icon|
     - The protocol must ensure that no third party can interfere with the issuance process such that the Issuer issues Credentials for the third party to the User.

This requirement is addressed by secure identification of the Credential Issuer. The ^iss^ parameter in the authorization response assures the Wallet that the response comes from the expected Credential Issuer. The cryptographic verification of the received tokens ensures that the tokens were issued by the legitimate Credential Issuer. In addition, the use of PKCE avoids injection of the code from another session into the User session.

SR-P-30
^^^^^^^
.. list-table::
   :widths: 8 92

   * - |check-icon|
     - The protocol must ensure that the interaction between the Wallet and Verifier is protected such that no third party can interfere with the interaction by modifying the information transmitted.

The presentation process occurs through different flows, including remote and proximity. In the remote flow, signed Request Objects, **nonce** usage, Trust Chain validation, Wallet Attestation, and Holder binding protect the exchange. No third party can interfere with or modify the information transmitted between the Wallet and the Relying Party. These mechanisms align with Security Requirement P-30. The mechanisms protect the interaction from tampering or injection attacks.

SR-P-40
^^^^^^^
.. list-table::
   :widths: 8 92

   * - |partially-check-icon|
     - The protocol must ensure that the interaction between an attacker and a Verifier cannot be forwarded to and successfully completed by a User.

In the case of the same device flow, this can be prevented by using and properly checking the **nonce** value, which is created and sent by the Relying Party in the authorization request.
The Relying Party should maintain a mapping between User sessions and the **nonce** that is expected in the flow. The Relying Party should only accept a presentation if the **nonce** in the presentation
matches the **nonce** that is expected for the User session. With this countermeasure, the Relying Party must detect if a presentation is sent that was not bound to the User's session or if no
User session exists at all, preventing the attack.

For the cross-device flow the requirement is partially satisfied. The flow is vulnerable to Cross-Device Consent Phishing attacks. An attacker could initiate the presentation flow, obtain the signed Request Object and QR code, and forward them to the victim.

Some security measures are already in place, such as the use of **nonce** and state. The **nonce** ensures freshness of the request, and the state binds the flow to a unique transaction,
thus reducing the opportunity for a successful attack.

.. note::
  Other security measures are currently under evaluation in issue number [117](https://github.com/italia/eid-wallet-it-docs/issues/117),
  where a list of mitigations from [`OAuthCrossDeviceSec`_] are discussed. Two examples are:

  - Short Lived/Timebound QR Codes: Reducing the lifetime of the QR code (e.g., 2-3 mins) is necessary to restrict the time window available for the attacks.
  - One-Time QR Codes: One-Time QR codes restrict the possibility of attacks when the same QR code is sent to multiple victims.

SR-P-41
^^^^^^^
.. list-table::
   :widths: 8 92

   * - |check-icon|
     - The protocol must ensure that an attacker cannot successfully forward an interaction between a Wallet and a Verifier to a Verifier under the control of the attacker.

A prerequisite for a successful attack of this kind is attacker access to some messages between the Wallet and the Relying Party. For example, the attacker might have access to the presentation contained in the VP Token. Given that, the proper implementation of TLS guarantees confidentiality and avoids leakage of the response.
In addition to TLS, the existing implementation of **nonce** and audience checks in the presentation protocol should help to meet the P-41 security requirement.
Regarding the **nonce** claim, the Relying Party MUST check that the **nonce** value in the VP Token matches the **nonce** value that is created by the Relying Party during the authorization request.
Regarding the **aud** value, the Relying Party must check that the audience of the presentation matches the Relying Party's identifier.

SR-P-50
^^^^^^^
.. list-table::
   :widths: 8 92

   * - |partially-check-icon|
     - The protocol must ensure that third parties cannot interfere with the binding process.

In the issuance phase, the Holder binding happens at the Credential request to the protected Credential endpoint. This means that the attacker needs to obtain the access token
first and therefore send the request to the Credential endpoint and bind the Credentials to the keys under his control. The IT-Wallet specification requires the use of a sender-constrained
access token, which means that the access token binds to the device using cryptographic materials.

The second surface for the attack is related to key management. With software-based keys, the keys can be cloned and moved to a device under attacker control. If the Credentials are stolen as well, the attacker can create proof of possession of the keys. IT-Wallet is less vulnerable to these attacks because IT-Wallet supports a hardware-backed Keystore that uses hardware-based keys. A certification profile that certifies the Keystore (TEE) against highly capable attackers is still missing. Current TEE solutions on the market reach AVA_VAN.3 at most, as shown for example in this `Certification Report <https://www.tuv-nederland.nl/assets/files/cerfiticaten/2021/08/nscib-cc-0244671-cr-1.0.pdf>`_ or on the `Global Platform site <https://globalplatform.org/specs-library/tee-protection-profile-v1-3/>`_. The requirement is therefore only partially satisfied for standard Digital Credentials. For the PID, this limitation is addressed by requiring a WSCA operating within a Remote WSCD (remote HSM operated server-side). The Remote WSCD provides certification at a higher assurance level.

SR-V-10
^^^^^^^
.. list-table::
   :widths: 8 92

   * - |partially-check-icon|
     - (conditional w.r.t I-50+V-20) The Verifier must ensure that the Credential is stored in a secure Wallet.

The Relying Party checks the Wallet Attestation during exchanges sent with the authorization response. The check confirms that the Wallet Attestation meets the security criteria required by the Relying Party. The Wallet Attestation remains under the sole responsibility of its issuer, the trusted Wallet Provider.

.. note::
  Currently, no explicit security and privacy measures related to this requirement are specified in [`OpenID4VC-SecTrust`_] and it is not clearly defined what ^stored in a secure Wallet^ means. Without this detail, this requirement is considered only partially satisfied. Indeed, the Wallet Attestation guarantees
  that the Wallet Instance is operating on a secure, trusted device and adheres to the strict security policies set by the Wallet Provider. However, the attestation does not directly guarantee that each
  Credential within the Wallet is stored securely. The attestation verifies the overall security of the Wallet environment, within which the Credentials reside. Therefore, while the attestation supports the Relying Party's
  confidence that the Credential comes from a secure source, it is ultimately a broad assurance of the Wallet's security, rather than a specific validation of individual Credential storage.

SR-V-20
^^^^^^^
.. list-table::
   :widths: 8 92

   * - |check-icon|
     - (conditional w.r.t. I-10) The Verifier must ensure that the Credential was issued by an Issuer that only issues Credentials to trustworthy Wallets.

By checking the trust of the Credential Issuer, the Relying Party ensures that the Credential was issued by a trusted Credential Issuer committed to issuing Credentials only to secure Wallets (as for SR-I-50).

.. note::
  Currently, no explicit security and privacy measures related to this requirement are specified in [`OpenID4VC-SecTrust`_], configuring this item as something that requires further developments and clarifications.

SR-W-20
^^^^^^^
.. list-table::
   :widths: 8 92

   * - |check-icon|
     - The Wallet must provide trustworthy and complete information about Issuers to the User.

The Wallet Instance discovers the trusted Credential Issuers using trusted third party resources, such as the Federation API. An example is the Subordinate Listing Endpoint of the Trust Anchor and its Intermediates. The Wallet Instance inspects the Credential Issuer metadata and Trust Marks to filter the PID Provider.

The Credential Issuer's information is displayed to the User during the issuance process and can be subsequently read by the User as it is inside the issued Credential.
In addition to the Credential Issuer's information, the Digital Credential Type Metadata also contains information on the Authentic Source.

SR-W-30
^^^^^^^
.. list-table::
   :widths: 8 92

   * - |check-icon|
     - The Wallet must provide trustworthy and complete information about Verifiers to the User.

The Wallet validates the Trust Chain related to the Relying Party and its information is displayed to the User before the presentation.

Privacy Requirements
--------------------

PR-CF-30
^^^^^^^^
.. list-table::
   :widths: 8 92

   * - |check-icon|
     - The Credential Format must ensure that there is a robust mechanism to ensure that data that is not to be released to a Verifier cannot be extracted by the Verifier (Selective Disclosure).

Both SD-JWT and mdoc-CBOR provide Selective Disclosure capability, allowing Holders to reveal only specific fields to the Relying Party.

PR-CF-40
^^^^^^^^
.. list-table::
   :widths: 8 92

   * - |partially-check-icon|
     - The Credential Format must support correlation protection.

While Selective Disclosure is a strong tool for preventing correlation, full unlinkability is not guaranteed in all cases. Issues like Relying Party collusion or Credential Issuer tracking can arise.

.. tip::
  Batch issuance, using different key binding keys and salts for each Credential, can mitigate Relying Party/Relying Party and presentation unlinkability risks.

PR-E-60
^^^^^^^
.. list-table::
   :widths: 8 92

   * - |check-icon|
     - The Trust Framework must ensure that the Issuer cannot learn where the User uses the Credential.

The Relying Party performing the Trust Evaluation about the Credential Issuer of a Credential must not release any information to the Credential Issuer about the Wallet Instance it is interacting with. Using [`OID-FED`_] the Credential Issuer doesn't know who is the User presenting the Credential.
In addition, privacy is protected also during the check of the Credential's status. By using Status List [`TOKEN-STATUS-LIST`_], the IT-Wallet specification ensures that while the Relying Party checks the Credential's validity, the Credential Issuer does not learn where or when the Credential is being used.

PR-E-70
^^^^^^^
.. list-table::
   :widths: 8 92

   * - |partially-check-icon|
     - The Trust Framework must support correlation protection.

The following mechanisms may be implemented to reduce the correlation:

- *Relying Party-Relying Party*: evaluation mechanisms to ensure that a Relying Party requests only the information it is authorized to obtain from the Wallet. This approach minimizes data exchange and helps prevent User profiling through potential collusion between Relying Parties.
- *Credential Issuer-Relying Party*: The Credential Issuer does not require the authentication of the Relying Party during the Trust Evaluation. In principle, the Credential Issuer does not know which Relying Parties the User is accessing and will avoid User activity profiling based on the Relying Party's access.

.. tip::
 OpenID Federation Trust Marks allow the definition of custom policies suitable to the satisfaction of this requirement.

PR-W-40
^^^^^^^
.. list-table::
   :widths: 8 92

   * - |check-icon|
     - The Wallet must ask the User for meaningful consent before a Credential is used. The Wallet must provide the User the opportunity to review any data that is released to a Verifier.

After establishing trust with the Relying Party, the Wallet asks for the User's consent and provides the User the opportunity to review and select the data to be presented to the Relying Party.

PR-W-60
^^^^^^^
.. list-table::
   :widths: 8 92

   * - |check-icon|
     - The Wallet must ensure that the Issuer cannot learn where the User uses the Credential.

Same as for SR-P-80.

PR-W-70
^^^^^^^
.. list-table::
   :widths: 8 92

   * - |uncheck-icon|
     - The Wallet must ensure that the Verifier cannot learn that the same User is using other Verifiers.

To mitigate Relying Party/Relying Party linkability for SD-JWT Credentials, one proposed solution is batch issuance, which involves using different cryptographic keys used in the key binding and salts for each issued Credential. However, the effectiveness of these methods has not yet been thoroughly evaluated, even in consideration of the impacts that these might result with the user experience, and is not available for IT-Wallet yet.

Security and Privacy Requirements
---------------------------------

SPR-E-50
^^^^^^^^
.. list-table::
   :widths: 8 92

   * - |check-icon|
     - The Trust Framework must ensure that lifecycles of keys, certificates, and Credentials are designed such that the impact of a compromise is minimized.

The Credential lifecycle includes a Credential revocation mechanism based on Status List [`TOKEN-STATUS-LIST`_] that ensures that Credentials are properly revoked when compromised or outdated.

Revocation of a Federation Entity (Credential Issuer, Relying Party, or Wallet Provider) is possible by not issuing the corresponding Subordinate Statement about that Entity. A short expiration of the Trust Chain prevents misuse during compromise.

.. tip::
  In addition, [`OID-FED`_] supports a historical key endpoint to retrieve the list of expired and revoked keys, with the motivation of the revocation.

SPR-P-10
^^^^^^^^
.. list-table::
   :widths: 8 92

   * - |check-icon|
     - The protocol must ensure that no third party can read the Credential issued by the Issuer.

To mitigate this threat, the IT-Wallet specification requires the following security mechanisms in the issuance process:

- *TLS*: Used in all communication between the Wallet and the Credential Issuer. Data in transit is encrypted and protected from interception by attackers.
- *Wallet Attestation*: Ensures that the Wallet operates on a secure, trusted device and complies with the security standards required by the Credential Issuer. The attestation gives additional assurance that the Credential Issuer is interacting with a legitimate Wallet Instance.
- *DPoP*: Ensures that the Holder of the access token possesses the private key associated with it, preventing attackers from reusing intercepted tokens.
- *Holder binding*: Ties the Credential to a specific Holder, ensuring that only the legitimate Holder can use a Credential to authenticate with the Credential Issuer.
- *redirect_uri validation*: This validation ensures that the authorization response is sent to the correct and authorized endpoint, thereby preventing unauthorized interception by malicious actors. Ensuring the integrity of the **redirect_uri** is critical to avoid any manipulation or misdirection of the URI.
- *PKCE*: Avoids injection of a legit authorization **code** in another session.

SPR-P-60
^^^^^^^^
.. list-table::
   :widths: 8 92

   * - |check-icon|
     - The protocol must ensure that during an interaction with a Verifier, an attacker cannot read PII.

The IT Wallet complies with the requirements of P-60 by ensuring that all network connections are secured by TLS.

In addition, as the Authorization Response contains PII is important that it is not sent to an attacker-controlled endpoint.
In the IT Wallet specification the **response_uri** is the endpoint where the Wallet sends the Authorization Response. The **response_uri** is included in the signed Request Object. The Wallet verifies that object using the Relying Party's public key and Trust Chain. This guarantees that the Authorization Response is sent to the correct endpoint.
Additionally, the Authorization Response is encrypted with the Relying Party's public key, ensuring that only the intended recipient can decrypt and read the sensitive information,
further securing the transmission.

Another endpoint to be validated is the **redirect_uri**, which is used to redirect the User back to the Relying Party after the Credential presentation is complete.
In the IT-Wallet specification, the **redirect_uri** is registered and validated beforehand during the Relying Party onboarding using OpenID Federation. During the presentation phase, the Wallet validates this value by verifying trust in the Relying Party according to `Trust Evaluation Mechanism <trust.html#trust-evaluation-mechanism>`_.

The Relying Party response endpoint checks that the **redirect_uri** comes from a legitimate Wallet and not from an attacker. Upon receipt of a valid authorization response, the endpoint creates a fresh cryptographic value linked to that response. The endpoint attaches the value to the **redirect_uri** sent to the Wallet.
When the Relying Party receives the redirect, it can extract the response code and check with its response endpoint whether the response code was associated with this Authorization Response. (See :ref:`remote-flow:Redirect URI`).

SPR-P-70
^^^^^^^^
.. list-table::
   :widths: 8 92

   * - |check-icon|
     - The protocol must ensure that during an interaction with an Issuer, an attacker cannot read PII.

In the issuance process, as the Credential inside a Credential Response contains PII, it is required that the Credential is not sent to or intercepted by an attacker.
To mitigate these threats, the IT-Wallet specification requires the following security mechanisms:

- *TLS*: Used in all communication between the Wallet and the Credential Issuer. Data in transit is encrypted and protected from interception by attackers.
- *Wallet Instance Attestation*: Ensures that the Wallet operates on a secure, trusted device and complies with the security standards required by the Credential Issuer. The attestation gives additional assurance that the Credential Issuer is interacting with a legitimate Wallet Instance.
- *DPoP*: Ensures that the Holder of the access token possesses the private key associated with it, preventing attackers from reusing intercepted tokens.
- *Holder binding*: Ties the Credential to a specific Holder, ensuring that only the legitimate Holder can use a Credential to authenticate with the Credential Issuer.
- *redirect_uri validation*: This validation ensures that the authorization response is sent to the correct and authorized endpoint, thereby preventing unauthorized interception by malicious actors. Ensuring the integrity of the **redirect_uri** is critical to avoid any manipulation or misdirection of the URI.
- *PKCE*: Avoids injection of a legit authorization **code** in another session.

.. tip::
  A further security enhancement that could be applied to add an extra layer of protection for sensitive User information is the encryption of Credential responses.
  OpenID4VCI standard provides the option for the Wallet to request encrypted Credentials containing PII by including a **credential_response_encryption** object in its request.

.. note::
  Currently, no explicit security and privacy measures related to this requirement are specified in [`OpenID4VC-SecTrust`_], it remains a work in progress.

SPR-P-80
^^^^^^^^
.. list-table::
   :widths: 8 92

   * - |check-icon|
     - The protocol must ensure that the Issuer cannot learn where the User uses the Credential.

The exchange protocol does not require any interactions between Relying Parties and Credential Issuers.
In addition, privacy-preserving Status List mechanism ensure that while the Relying Party checks the Credential's validity, the Credential Issuer does not learn where or when the Credential is being used.

SPR-W-50
^^^^^^^^
.. list-table::
   :widths: 8 92

   * - |check-icon|
     - The Wallet must ensure that the Credentials and private keys are protected from unauthorized access.

To prevent unauthorized access, the Wallet is unlocked on the User's device by a personal identification number (PIN) or by biometric authentication. Biometric authentication includes fingerprint or facial recognition, based on the User's preferences and the device's capabilities. The cryptographic keys are stored within the Keystore, or within the WSCA/WSCD for the PID. Only the User can access those keys. That storage prevents unauthorized use or tampering.



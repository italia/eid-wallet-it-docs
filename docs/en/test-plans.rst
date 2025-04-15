.. include:: ../common/common_definitions.rst

.. _test-plans.rst:

Test Plans
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The purpose of the test plans is to support implementers, auditors, and conformance test environments in validating the behavior of the Wallet Solutions, Relying Parties and Credential Issuers under various operational and security scenarios.

All test cases are derived from normative rules defined in the above specifications, with no assumptions or extensions.

.. note::

  Please note that the test plans matrix may be subject to future changes.


Structure of the Test Matrix
-----------------------------

Each test case is identified by a unique test ID (e.g., WS-001) and categorized using the functional domains defined below. Other category identifiers can be used as well.

- **Discovery**
- **Security**
- **Authorization**
- **Authentication**
- **User Interaction**
- **User Notification**
- **Credential Issuance**
- **Proof of Possession**
- **Attestation Evaluation**
- **Credential Presentation**
- **Credential Status**
- **Backup & Restore**

For each test case, the table specifies:

- **Test Case**: a unique identifier.
- **Category**: the functional area covered by the test.
- **Description**: the requirement being tested, always based on a normative MUST from the specification.
- **Expected Result**: the expected outcome when the solution is implemented correctly.


Signed Statements Evaluation Test Matrix
------------------------------------------

This section provides the common set of test cases for Wallet Solutions, Relying Parties and Credential Issuers evaluating any signed statements, be these assertions, requests, attestation or credentials.


.. list-table::
   :widths: 10 15 40 35
   :header-rows: 1

   * - Test Case
     - Category
     - Description
     - Expected Result
   * - ATT-001
     - Discovery, Security
     - Evaluation of the issuer
     - Entities evaluating signed statements establish trust with the issuer and assess its compliance. Undiscoverable Issuers within the federation or unlinkable to any known Trust Anchor, halt any protocol communications.
   * - ATT-002
     - Discovery, Security
     - Evaluation of the signature
     - Entities evaluate signed statements by verifying the signature with the issuer's cryptographic material, provided it is trusted through a well-known Trust Anchor. Any untrusted cryptographic material or invalid signatures halt protocol communications.
   * - ATT-003
     - Algorithm Verification
     - Verify that the algorithm specified in the header matches the one used for cryptographic operations.
     - The algorithm in the header must match the cryptographic operation.
   * - ATT-004
     - Appropriate Algorithms
     - Ensure only cryptographically current algorithms are used.
     - Only approved algorithms are accepted; deprecated ones are rejected.
   * - ATT-005
     - Signature Validation
     - Validate all cryptographic operations and reject if any fail.
     - All signatures must be valid; any failure results in rejection.
   * - ATT-006
     - Key Entropy
     - Ensure cryptographic keys have sufficient entropy.
     - Keys must meet entropy requirements; weak keys are rejected.
   * - ATT-007
     - Issuer Validation
     - Validate that the cryptographic keys belong to the issuer.
     - Keys must be verified as belonging to the issuer.
   * - ATT-008
     - Audience Validation
     - Validate the audience claim to ensure the token is used by the intended party.
     - Audience claim must match the intended recipient.
   * - ATT-009
     - Claim Trust
     - Do not trust received claims without validation.
     - Claims must be validated; untrusted claims are rejected.
   * - ATT-010
     - Explicit Typing
     - Use explicit typing to prevent COSE/JOSE confusion.
     - Typing must be explicit and validated.
   * - ATT-011
     - Cross-JWT Confusion
     - Prevent COSE/JOSE from being used in unintended contexts.
     - COSE/JOSE must be contextually validated to prevent misuse.
   * - ATT-012
     - Substitution Attacks
     - Ensure COSE/JOSE are not substituted across different contexts.
     - COSE/JOSE must be validated for context-specific use.
   * - ATT-013
     - Issued At Validation
     - Verify that the `issued at` parameter is set to the current time, allowing a grace period not exceeding 120 seconds.
     - The `issued at` value must be within 120 seconds of the current time.
   * - ATT-014
     - Expiration Validation
     - Ensure the `expiration` time is greater than the `issued at` time.
     - The `expiration` time must be later than the `issued at` time.
   * - ATT-015
     - Data model validation
     - Ensure JOSE/COSE type matches with the defined data model.
     - The parameters or claims, their values and the schema used to represent them are compliant with the data model.


Trust Evaluation Test Matrix
-----------------------------

This section provides the common set of test cases for Wallet Solutions, Relying Parties and Credential Issuers.


.. list-table::
   :widths: 10 15 40 35
   :header-rows: 1

   * - Test Case
     - Category
     - Description
     - Expected Result
   * - ALL-001
     - Security
     - Obtaining Trust Anchors public cryptographic materials
     - Entities obtain the list of Trust Anchors or Certificate Authorities and their public cryptographic key materials, periodically ensuring that these are not expired, revoked or updated. Infrastructure of Trust provides these information through web endpoints and other out of band mechanisms, to facilitate comparison of the provided information to all the entities.
   * - ALL-002
     - Security
     - Compliance self evaluation
     - Entities periodically evaluate their compliance and presence within the federation, checking the trust chain about themselves as still valid, not revoked and compliant with the tecnhical specification. Entities apply the policies, checking that their current configuration is valid with the active policies about them within the federation. Trust chain, evaluated and stored in mutiple formats to facilitate interoperability in trust discovery with other entities, are stored by entities and used on occurrence during the data exchange flows. Trust chain about entities are fetched or discovered using the entitie's issued assertions.
   * - ALL-003
     - Discovery
     - Publication of information about itself
     - Entities sign and publish all the information about them, containing all the protocol metadata, cryptographic material, trust marks, using the well-known endpoint defined in this specification, making these information publicly discoverable by other entities.
   * - ALL-004
     - Security
     - Publication of the historical key registry
     - Entities sign and publish all the information about the unused or revoked cryptographic material using well known endpoints defined in this specification, making these information publicly discoverable by other entities.
   * - ALL-005
     - Security
     - Evaluation of compliance with entities before exchanging data about the User
     - Entities evaluate trust and compliance with other entities before any information related to a natural or legal person might be exchanged. Bogus configurations don't allow data exchanges.
   * - ALL-006
     - Security
     - Evaluation of proof of possession during the use of a signed assertion in according to the configured usage ownership confirmation method. 
     - Entities evaluate the confirmation method and apply its protocol to consider valid the signed statement.
   * - ALL-007
     - Security
     - Supported cryptography algorithms
     - Entities evaluate cryptography using in compliance of the allowed algorithms.
   * - ALL-008
     - Security
     - Replay attacks
     - Signed statements using unique identifiers are stored until their expiration time and checked against any replay of them.


Wallet Solution Test Matrix
-----------------------------

This section provides the set of test cases for verifying conformance of a Wallet Solution implementation to the technical rules defined in the IT-Wallet ecosystem.
The test plan is based on the mandatory requirements (MUST statements) extracted from the following documents:

- Wallet Solution
- Wallet Instance Revocation
- Wallet Attestation Issuance
- Backup and Restore


.. list-table::
   :widths: 10 15 40 35
   :header-rows: 1

   * - Test Case
     - Category
     - Description
     - Expected Result
   * - WS-001
     - Wallet Initialization
     - The Wallet Solution MUST ensure that each Wallet Instance is generated according to the specifications and includes a unique identifier, and cryptographic keys bound to a secure element.
     - A compliant Wallet Instance is generated with correct identifiers and secure bindings.
   * - WS-002
     - User Interaction
     - The Wallet Solution MUST request and obtain explicit User Consent during Wallet Instance initialization.
     - The Wallet Instance is activated only after obtaining verifiable User Consent.
   * - WS-003
     - Security
     - The Wallet Solution MUST store private keys within a Secure Hardware Element or equivalent secure storage.
     - All private key materials are inaccessible from the operating system or any application outside the Wallet Solution.
   * - WS-004
     - Attestation
     - The Wallet MUST be capable of generating and presenting a Wallet Attestation when required by Relying Parties or Issuers.
     - Valid, verifiable Attestations are generated including integrity and origin proofs.
   * - WS-005
     - Attestation
     - The Wallet MUST support processing Wallet Attestation Requests and generating appropriate responses in compliance with eIDAS.
     - The Wallet correctly interprets and fulfills attestation requests including subject data and cryptographic signatures.
   * - WS-006
     - Remote Credential Presentation
     - The Wallet Solution MUST implement both the proximity and remote presentation flow, ensuring Verifiable Credential selection, integrity, and User interaction.
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

Credential Issuance Test Matrix
---------------------------------

This section provides the set of test cases for verifying conformance of a Credential Issuance implementations to the technical rules defined in the IT-Wallet ecosystem.
Tests related to both PID and (Q)EAA Providers are related to the issuance of credential of public interest, as published within the Credential Catalogue.

.. note::

  References about official OpenID4VCI test plans will update this section in future releases.

- PID/EAA Issuance


.. list-table::
   :widths: 10 15 40 35
   :header-rows: 1

   * - Test Case
     - Category
     - Description
     - Expected Result
   * - ISS-001
     - Setup
     - Validate Wallet Instance Setup
     - Wallet Instance is set up with a valid Wallet Attestation. Ensure the public key is valid and correctly bound to a secure element.
   * - ISS-002
     - Discovery
     - PID/(Q)EAA Provider Discovery
     - Wallet Instance successfully discovers trusted Digital Credential Issuers using the Credential Catalogue and their configuration compliance and policies with Federation API.
   * - ISS-003
     - Metadata
     - PID/(Q)EAA Provider Metadata Retrieval
     - Wallet Instance retrieves and validates PID/(Q)EAA Provider metadata. Metadata includes PID formats, supported algorithms, and interoperability parameters.
   * - ISS-004
     - Authorization, Authentication
     - PID/(Q)EAA Request using Authorization Code Flow
     - Wallet Instance successfully requests PID/(Q)EAA using Authorization Code Flow. Validate PKCE use with a code verifier of 43-128 characters.
   * - ISS-005
     - Authentication
     - User Authentication with PID Provider
     - User is authenticated with LoA 3 (High) by the PID Provider. Validate the use of the digital identity scheme CieID and ensure that User consent is obtained.
   * - ISS-006
     - Issuance
     - PID/(Q)EAA Issuance
     - PID/(Q)EAA is issued and bound to the Wallet Instance's key material. Validate the binding process and ensure the integrity and the compliance to data model of the issued PID/(Q)EAA.
   * - ISS-007
     - Authentication
     - User Authentication with (Q)EAA Provider
     - User is authenticated by presenting a valid PID. The presentation request, the PID is valid and previously obtained.
   * - ISS-008
     - Security
     - Pushed Authorization Request (PAR) Validation
     - PID/(Q)EAA Provider validates the PAR request successfully.
   * - ISS-009
     - Security
     - Token Request Validation
     - PID/(Q)EAA Provider validates the token request and issues tokens. Validate the DPoP proof and ensure the authorization code is valid and not reused.
   * - ISS-010
     - Security
     - Credential Request Validation
     - PID/(Q)EAA Provider validates the Credentials request and issues Credentials. Validate the proof of possession and ensure the credential type matches the request.
   * - ISS-011
     - Deferred Issuance
     - Deferred Issuance Flow
     - Wallet Instance handles deferred issuance correctly and retrieves credentials later. Validate the use of transaction unique identifier (`transaction_id`) and ensure the Credential is issued after the specified lead time.
   * - ISS-012
     - Notification
     - Notification Handling
     - Wallet Instance sends and receives notifications correctly. Validate the use of `notification_id` and ensure the event type is correctly reported.
   * - ISS-013
     - Credential Issuance
     - (Q)EAA Provider offers Credentials to Holder
     - Wallet Instances evaluate the offer and start the authorization flow after having evaluated the trust with the (Q)EAA Provider.
   * - ISS-014
     - Security
     - Validate `client_id` in PAR Request
     - Ensure the `client_id` in the request body matches the `client_id` claim in the Request Object.
   * - ISS-015
     - Security
     - Validate `iss` Claim in Request Object
     - Ensure the `iss` claim in the Request Object matches the `client_id` claim.
   * - ISS-016
     - Security
     - Validate `aud` Claim in Request Object
     - Ensure the `aud` claim in the Request Object is equal to the identifier of the PID/(Q)EAA Provider.
   * - ISS-017
     - Security
     - Reject PAR Request with `request_uri`
     - Ensure the PAR request is rejected if it contains the `request_uri` parameter.
   * - ISS-018
     - Security
     - Validate Mandatory Parameters in Request Object
     - Ensure the Request Object contains all mandatory parameters and values are validated.
   * - ISS-019
     - Security
     - Validate `OAuth-Client-Attestation-PoP`
     - Ensure the `OAuth-Client-Attestation-PoP` parameter is validated.
   * - ISS-020
     - Authorization
     - Validate `request_uri` in Authorization Request
     - Ensure `request_uri` values are treated as one-time use and expired requests are rejected.
   * - ISS-021
     - Authorization
     - Identify Request from Submitted PAR
     - Ensure the request is identified as a result of the submitted PAR.
   * - ISS-022
     - Authorization
     - Reject Authorization Requests without `request_uri`
     - Ensure all Authorization Requests without `request_uri` are rejected.
   * - ISS-023
     - Security
     - Validate Authorization Response Parameters
     - Ensure the Authorization Response contains all defined parameters.
   * - ISS-024
     - Security
     - Validate `state` Parameter in Authorization Response
     - Ensure the `state` parameter in the response matches the value sent in the Request Object.
   * - ISS-025
     - Security
     - Validate `iss` Parameter in Authorization Response
     - Ensure the `iss` parameter matches the intended PID/(Q)EAA Provider.
   * - ISS-026
     - Security
     - Validate DPoP Proof for Token Endpoint
     - Ensure the DPoP Proof JWT is valid and binds the Access Token to the Wallet Instance.
   * - ISS-027
     - Security
     - Validate Token Request Parameters
     - Ensure the token request includes `code`, `code_verifier`, and valid OAuth 2.0 Attestation.
   * - ISS-028
     - Security
     - Validate Authorization Code in Token Request
     - Ensure the Authorization `code` is valid and not reused.
   * - ISS-029
     - Security
     - Validate `redirect_uri` in Token Request
     - Ensure the `redirect_uri` matches the value in the previous Request Object.
   * - ISS-030
     - Security
     - Validate DPoP Proof JWT in Token Request
     - Ensure the DPoP Proof JWT is validated according to the specification.
   * - ISS-031
     - Security
     - Validate Nonce Request
     - Ensure the Nonce Request is sent correctly and a fresh `c_nonce` is obtained.
   * - ISS-032
     - Security
     - Validate Nonce Response
     - Ensure the `c_nonce` in the Nonce Response is unpredictable and used correctly.
   * - ISS-033
     - Security
     - Validate DPoP Proof for Credential Endpoint
     - Ensure the DPoP Proof JWT for the Credential Endpoint is valid and binds the Credential to the Wallet Instance.
   * - ISS-034
     - Security
     - Validate Credential Request Parameters
     - Ensure the Credential Request includes Access Token, DPoP Proof JWT, and valid proof of possession.
   * - ISS-035
     - Security
     - Validate JWT Proof in Credential Request
     - Ensure the JWT proof includes all required claims and is signed correctly.
   * - ISS-036
     - Security
     - Validate `c_nonce` in Credential Request
     - Ensure the `c_nonce` in the JWT matches the value provided by the server.
   * - ISS-037
     - Security
     - Validate Credential Response Parameters
     - Ensure the Credential Response contains all mandatory parameters and values are validated.
   * - ISS-038
     - Security
     - Validate Credential Integrity
     - Ensure the integrity of the issued Credential by verifying the signature.
   * - ISS-039
     - Security
     - Validate Credential Type and Schema
     - Ensure the issued Credential matches the requested type and complies with the schema.
   * - ISS-040
     - Security
     - Validate Trust Chain in Credential
     - Ensure the Trust Chain in the Credential header verifies the PID/(Q)EAA Provider's trust at time of issuance.
   * - ISS-041
     - Security
     - Validate Deferred Issuance Parameters
     - Ensure the Deferred Issuance parameters are used correctly and the Credential is issued after the specified lead time.
   * - ISS-042
     - Security
     - Validate Notification Request Parameters
     - Ensure the Notification Request includes `notification_id` and valid event type.
   * - ISS-043
     - Security
     - Validate Notification Response
     - Ensure the Notification Response is received with the correct status code.
   * - ISS-044
     - Security
     - Validate Refresh Token Flow
     - Ensure the Refresh Token flow is used correctly and tokens are bound to the DPoP key.
   * - ISS-045
     - Security
     - Validate Refresh Token Expiry
     - Ensure the Refresh Token is not expired and is used within the allowed timeframe.
   * - ISS-046
     - Security
     - Validate Sender-Constrained Tokens
     - Ensure Refresh Tokens are cryptographically bound to the Wallet Instance.
   * - ISS-047
     - Security
     - Validate Limiting Use of Refresh Token
     - Ensure the use of Refresh Tokens is limited and complies with the specification.
   * - ISS-048
     - Revocation
     - Validate life time of Wallet Attestations
     - Ensure Wallet Attestations are short-lived or provided with Status List if long-lived.
   * - ISS-049
     - Security
     - Validate Re-Issuance Flow
     - Ensure the Re-Issuance flow is used correctly and complies with the specification.
   * - ISS-050
     - Security
     - Validate Data Model/Format Update
     - Ensure the Data Model/Format update is handled correctly during Re-Issuance.
   * - ISS-051
     - Security
     - Validate User Attribute Set Update
     - Ensure User attribute set updates are handled correctly during Re-Issuance.
   * - ISS-052
     - Security
     - Validate Credential Expiry in Re-Issuance
     - Ensure the newly issued Credential has the same expiry date as the previous one.
   * - ISS-053
     - Security
     - Validate User Authentication in Re-Issuance
     - Ensure User authentication is required for Re-Issuance after Credential expiration.
   * - ISS-054
     - Security
     - Validate Deferred Endpoint Parameters
     - Ensure the Deferred Endpoint parameters are used correctly and the Credential is issued after the specified lead time.
   * - ISS-055
     - Security
     - Validate Deferred Credential Request
     - Ensure the Deferred Credential Request is sent correctly and the Credential is issued.
   * - ISS-056
     - Security
     - Validate Deferred Credential Response
     - Ensure the Deferred Credential Response contains all mandatory parameters and values are validated.
   * - ISS-057
     - Security
     - Validate Notification Endpoint Parameters
     - Ensure the Notification Endpoint parameters are used correctly and the event is reported.
   * - ISS-058
     - Security
     - Validate Error Handling in Notification Endpoint
     - Ensure errors in the Notification Endpoint are handled correctly and reported.
   * - ISS-059
     - Security
     - Validate Error Handling in Credential Endpoint
     - Ensure errors in the Credential Endpoint are handled correctly and reported.
   * - ISS-060
     - Security
     - Validate Error Handling in Token Endpoint
     - Ensure errors in the Token Endpoint are handled correctly and reported.
   * - ISS-061
     - Security
     - Validate Error Handling in Authorization Endpoint
     - Ensure errors in the Authorization Endpoint are handled correctly and reported.
   * - ISS-062
     - Error Handling
     - Validate Error Handling in PAR Endpoint
     - Ensure errors in the PAR Endpoint are handled correctly and reported.
   * - ISS-063
     - Error Handling
     - Validate Error Handling in Nonce Endpoint
     - Ensure errors in the Nonce Endpoint are handled correctly and reported.
   * - ISS-064
     - Error Handling
     - Validate Error Handling in Deferred Endpoint
     - Ensure errors in the Deferred Endpoint are handled correctly and reported.
   * - ISS-065
     - Error Handling
     - Validate Error Handling in Re-Issuance Flow
     - Ensure errors in the Re-Issuance Flow are handled correctly and reported.
   * - ISS-066
     - Error Handling
     - Validate Error Handling in Refresh Token Flow
     - Ensure errors in the Refresh Token Flow are handled correctly and reported.
   * - ISS-067
     - Error Handling
     - Validate Error Handling in Credential Issuance
     - Ensure errors in the Credential Issuance process are handled correctly and reported.
   * - ISS-068
     - Error Handling
     - Validate Error Handling in Credential Request
     - Ensure errors in the Credential Request process are handled correctly and reported.
   * - ISS-069
     - Error Handling
     - Validate Error Handling in Credential Response
     - Ensure errors in the Credential Response process are handled correctly and reported.
   * - ISS-070
     - Error Handling
     - Validate Error Handling in Credential Validation
     - Ensure errors in the Credential Validation process are handled correctly and reported.
   * - ISS-071
     - Error Handling
     - Validate Error Handling in Credential Integrity
     - Ensure errors in the Credential Integrity process are handled correctly and reported.
   * - ISS-072
     - Error Handling
     - Validate Error Handling in Credential Type and Schema
     - Ensure errors in the Credential Type and Schema process are handled correctly and reported.
   * - ISS-073
     - Error Handling
     - Validate Error Handling in Trust Chain Validation
     - Ensure errors in the Trust Chain Validation process are handled correctly and reported.
   * - ISS-074
     - Error Handling
     - Validate Error Handling in Deferred Issuance
     - Ensure errors in the Deferred Issuance process are handled correctly and reported.
   * - ISS-075
     - Error Handling
     - Validate Error Handling in Notification Handling
     - Ensure errors in the Notification Handling process are handled correctly and reported.
   * - ISS-076
     - Error Handling
     - Validate Error Handling in User Authentication
     - Ensure errors in the User Authentication process are handled correctly and reported.
   * - ISS-077
     - Error Handling
     - Validate Error Handling in User Consent
     - Ensure errors in the User Consent process are handled correctly and reported.
   * - ISS-078
     - Error Handling
     - Validate Error Handling in User Notification
     - Ensure errors in the User Notification process are handled correctly and reported.
   * - ISS-079
     - Error Handling
     - Validate Error Handling in User Attribute Set Update
     - Ensure errors in the User Attribute Set Update process are handled correctly and reported.
   * - ISS-080
     - Error Handling
     - Validate Error Handling in Data Model/Format Update
     - Ensure errors in the Data Model/Format Update process are handled correctly and reported.
   * - ISS-081
     - Error Handling
     - Validate Error Handling in Credential Expiry
     - Ensure errors in the Credential Expiry process are handled correctly and reported.
   * - ISS-082
     - Error Handling
     - Validate Error Handling in Credential Re-Issuance
     - Ensure errors in the Credential Re-Issuance process are handled correctly and reported.
   * - ISS-083
     - Error Handling
     - Validate Error Handling in Credential Binding
     - Ensure errors in the Credential Binding process are handled correctly and reported.
   * - ISS-084
     - Error Handling
     - Validate Error Handling in Credential Trust Evaluation
     - Ensure errors in the Credential Trust Evaluation process are handled correctly and reported.
   * - ISS-085
     - Error Handling
     - Validate Error Handling in Credential Metadata Retrieval
     - Ensure errors in the Credential Metadata Retrieval process are handled correctly and reported.
   * - ISS-086
     - Error Handling
     - Validate Error Handling in Credential Discovery
     - Ensure errors in the Credential Discovery process are handled correctly and reported.
   * - ISS-087
     - Error Handling
     - Validate Error Handling in Credential Offer Evaluation
     - Ensure errors in the Credential Offer Evaluation process are handled correctly and reported.
   * - ISS-088
     - Error Handling
     - Validate Error Handling in Credential Offer Acceptance
     - Ensure errors in the Credential Offer Acceptance process are handled correctly and reported.
   * - ISS-089
     - Error Handling
     - Validate Error Handling in Credential Offer Rejection
     - Ensure errors in the Credential Offer Rejection process are handled correctly and reported.
   * - ISS-090
     - Error Handling
     - Validate Error Handling in Credential Offer Revocation
     - Ensure errors in the Credential Offer Revocation process are handled correctly and reported.
   * - ISS-091
     - Error Handling
     - Validate Error Handling in Credential Offer Expiry
     - Ensure errors in the Credential Offer Expiry process are handled correctly and reported.
   * - ISS-092
     - Error Handling
     - Validate Error Handling in Credential Offer Renewal
     - Ensure errors in the Credential Offer Renewal process are handled correctly and reported.
   * - ISS-093
     - Error Handling
     - Validate Error Handling in Credential Offer Update
     - Ensure errors in the Credential Offer Update process are handled correctly and reported.
   * - ISS-094
     - Error Handling
     - Validate Error Handling in Credential Offer Validation
     - Ensure errors in the Credential Offer Validation process are handled correctly and reported.
   * - ISS-095
     - Error Handling
     - Validate Error Handling in Credential Offer Verification
     - Ensure errors in the Credential Offer Verification process are handled correctly and reported.
   * - ISS-096
     - Error Handling
     - Validate Error Handling in Credential Offer Confirmation
     - Ensure errors in the Credential Offer Confirmation process are handled correctly and reported.
   * - ISS-097
     - Error Handling
     - Validate Error Handling in Credential Offer Notification
     - Ensure errors in the Credential Offer Notification process are handled correctly and reported.
   * - ISS-098
     - Error Handling
     - Validate Error Handling in Credential Offer Communication
     - Ensure errors in the Credential Offer Communication process are handled correctly and reported.
   * - ISS-099
     - Error Handling
     - Validate Error Handling in Credential Offer Transmission
     - Ensure errors in the Credential Offer Transmission process are handled correctly and reported.
   * - ISS-100
     - Error Handling
     - Validate Error Handling in Credential Offer Reception
     - Ensure errors in the Credential Offer Reception process are handled correctly and reported.
   * - ISS-101
     - Error Handling
     - Validate Error Handling in Credential Offer Processing
     - Ensure errors in the Credential Offer Processing process are handled correctly and reported.
   * - ISS-102
     - Error Handling
     - Validate Error Handling in Credential Offer Handling
     - Ensure errors in the Credential Offer Handling process are handled correctly and reported.
   * - ISS-103
     - Error Handling
     - Validate Error Handling in Credential Offer Management
     - Ensure errors in the Credential Offer Management process are handled correctly and reported.
   * - ISS-104
     - Error Handling
     - Validate Error Handling in Credential Offer Administration
     - Ensure errors in the Credential Offer Administration process are handled correctly and reported.
   * - ISS-105
     - Error Handling
     - Validate Error Handling in Credential Offer Control
     - Ensure errors in the Credential Offer Control process are handled correctly and reported.
   * - ISS-106
     - Error Handling
     - Validate Error Handling in Credential Offer Oversight
     - Ensure errors in the Credential Offer Oversight process are handled correctly and reported.
   * - ISS-107
     - Error Handling
     - Validate Error Handling in Credential Offer Supervision
     - Ensure errors in the Credential Offer Supervision process are handled correctly and reported.
   * - ISS-108
     - Error Handling
     - Validate Error Handling in Credential Offer Monitoring
     - Ensure errors in the Credential Offer Monitoring process are handled correctly and reported.
   * - ISS-109
     - Error Handling
     - Validate Error Handling in Credential Offer Evaluation
     - Ensure errors in the Credential Offer Evaluation process are handled correctly and reported.
   * - ISS-110
     - Error Handling
     - Validate Error Handling in Credential Offer Assessment
     - Ensure errors in the Credential Offer Assessment process are handled correctly and reported.

Credential Presentation Test Matrix
------------------------------------

This section provides the set of test cases for verifying conformance of a Credential Verifiers implementations to the technical rules defined in the IT-Wallet ecosystem.


Remote Credential Presentation Test Matrix
...........................................

This section defines the test cases about the remote presentation flow.

.. note::

  References about official OpenID4VP test plans will update this section in future releases.

.. list-table::
   :widths: 10 15 40 35
   :header-rows: 1

   * - Test Case
     - Category
     - Description
     - Expected Result
   * - RPR-01
     - Same Device Flow
     - Verify HTTP redirect (302) URL.
     - Wallet Instance receives correct URL.
   * - RPR-02
     - Cross Device Flow
     - Verify QR Code generation for Wallet Instance.
     - Wallet Instance scans QR Code successfully.
   * - RPR-03
     - Cross Device Flow
     - Verify QR Code contains correct URL parameters.
     - Wallet Instance retrieves URL with parameters.
   * - RPR-04
     - Cross Device Flow
     - Test QR Code scanning in low light.
     - QR Code is scanned successfully.
   * - RPR-05
     - Cross Device Flow
     - Verify QR Code error correction level.
     - QR Code remains readable if damaged.
   * - RPR-06
     - Cross Device Flow
     - Test QR Code scanning with different devices.
     - QR Code is scanned successfully.
   * - RPR-07
     - Request URI Method
     - Test `request_uri_method` as `post`.
     - Wallet Instance sends metadata via POST.
   * - RPR-08
     - Request URI Method
     - Test `request_uri_method` as `get`.
     - Wallet Instance fetches Request Object via GET.
   * - RPR-09
     - Request URI Method
     - Test absence of `request_uri_method`.
     - Wallet Instance defaults to GET method.
   * - RPR-10
     - Metadata
     - Verify parameters match openid credential verifier metadata.
     - Only allowed parameters will be considered.
   * - RPR-11
     - User Consent
     - Test eligibility of a credential verifier in requesting user attributes.
     - User can modify data selection about optional attributes.
   * - RPR-12
     - Authorization Response
     - Test sending of Presentation Response.
     - Relying Party receives and validates response with state and nonce.
   * - RPR-13
     - Authorization Response
     - Verify response encryption.
     - Response is encrypted using Relying Party's public key.
   * - RPR-14
     - Error Handling
     - Test invalid Request Object handling.
     - Authorization Error Response is sent.
   * - RPR-15
     - Error Handling
     - Verify error logging by Wallet Instance.
     - Errors are logged appropriately.
   * - RPR-16
     - Error Handling
     - Test recovery from `server_error`.
     - User prompted to retry or scan new QR code.
   * - RPR-17
     - Relying Party Response
     - Verify successful Response handling.
     - User session is updated, redirect URI provided.
   * - RPR-18
     - Relying Party Response
     - Test absence of `redirect_uri`.
     - Error response is returned.
   * - RPR-19
     - Redirect URI
     - Test redirection to Relying Party's endpoint.
     - User is redirected correctly.
   * - RPR-20
     - Redirect URI
     - Verify handling of invalid `redirect_uri`.
     - Error response is returned.
   * - RPR-21
     - User Consent
     - Verify display of Relying Party's identity.
     - Identity is displayed clearly to Holder.
   * - RPR-22
     - User Consent
     - Test user consent revocation.
     - User can revoke consent before submission.
   * - RPR-23
     - Credential Presentation
     - Verify response format compliance.
     - Each Credential adheres to specified format.
   * - RPR-24
     - Authorization Response
     - Test handling of response timeouts.
     - Retries must be successful unless response is acquired.
   * - RPR-25
     - Error Handling
     - Verify handling of malformed claims in presentation payload.
     - Authorization Error Response is sent.
   * - RPR-26
     - Error Handling
     - Verify handling of malformed claims in presented credentials.
     - Authorization Error Response is sent.
   * - RPR-27
     - Error Handling
     - Test handling of expired requests.
     - Holder is notified of expiration.
   * - RPR-28
     - Relying Party Response
     - Verify inclusion of response code.
     - Response code is cryptographically random.
   * - RPR-29
     - Relying Party Response
     - Test handling of invalid response codes.
     - Error response is returned.
   * - RPR-30
     - Status Endpoint
     - Verify handling of unauthorized access.
     - Unauthorized access is denied.
   * - RPR-31
     - Status Endpoint
     - Test handling of invalid session IDs.
     - Error response is returned.
   * - RPR-32
     - Redirect URI
     - Verify handling of expired sessions.
     - Error response is returned.
   * - RPR-33
     - Redirect URI
     - Test handling of server errors.
     - Error response is returned.
   * - RPR-34
     - Same Device Flow
     - Verify handling of slow network conditions.
     - Wallet Instance retries or notifies user.
   * - RPR-35
     - Request URI Method
     - Test handling of large metadata payloads.
     - Metadata is sent successfully.
   * - RPR-36
     - Presentation Response
     - Verify handling of large response payloads.
     - Response is sent successfully.
   * - RPR-37
     - Presentation Response
     - Test handling of response encryption failures.
     - Error response is returned.
   * - RPR-38
     - Error Handling
     - Verify handling of invalid signatures.
     - Authorization Error Response is sent.
   * - RPR-39
     - Error Handling
     - Test handling of invalid nonce values.
     - Error response is returned.
   * - RPR-40
     - Relying Party Response
     - Verify handling of malformed responses.
     - Error response is returned.
   * - RPR-41
     - Relying Party Response
     - Test handling of missing response parameters.
     - Error response is returned.
   * - RPR-42
     - Status Endpoint
     - Verify handling of session timeouts.
     - Error response is returned.
   * - RPR-43
     - Status Endpoint
     - Test handling of invalid status codes.
     - Error response is returned.
   * - RPR-44
     - Redirect URI
     - Verify handling of invalid user sessions.
     - Error response is returned.
   * - RPR-45
     - Redirect URI
     - Test handling of unavailable services.
     - Error response is returned.
   * - RPR-46
     - Same Device Flow
     - Verify handling of user cancellations.
     - User can cancel the process.
   * - RPR-47
     - Cross Device Flow
     - Test QR Code scanning with different apps.
     - QR Code is scanned successfully.
   * - RPR-48
     - Cross Device Flow
     - Verify QR Code scanning with different lighting.
     - QR Code is scanned successfully.
   * - RPR-49
     - Request URI Method
     - Test handling of unsupported content types.
     - Error response is returned.
   * - RPR-50
     - User Consent
     - Verify user notification of consent changes.
     - User is informed about consent changes.
   * - RPR-51
     - User Consent
     - Test user consent for sensitive data.
     - User can consent to sensitive data.
   * - RPR-52
     - Authorization Response
     - Verify handling of response decryption failures.
     - Error response is returned.
   * - RPR-53
     - Authorization Response
     - Test handling of response integrity checks.
     - Response integrity is verified.
   * - RPR-54
     - Relying Party Response
     - Verify handling of response validation failures.
     - Error response is returned.
   * - RPR-55
     - Relying Party Response
     - Test handling of response processing errors.
     - Error response is returned.
   * - RPR-56
     - Protected Resource Endpoint
     - Verify handling of unauthorized session access.
     - Unauthorized access is denied.
   * - RPR-57
     - Redirect URI
     - Verify handling of invalid redirect parameters.
     - Error response is returned.
   * - RPR-58
     - Redirect URI
     - Test handling of redirect failures.
     - Error response is returned.
   * - RPR-59
     - Same Device Flow
     - Verify handling of user interruptions.
     - User can resume or cancel the process.
   * - RPR-60
     - Request URI Method
     - Test handling of invalid HTTP methods.
     - Error response is returned.
   * - RPR-61
     - User Consent
     - Verify user notification of consent revocation.
     - User is informed about consent revocation.
   * - RPR-62
     - User Consent
     - Test user consent for optional data.
     - User can consent to optional data.
   * - RPR-63
     - Authorization Response
     - Verify handling of response signature failures.
     - Error response is returned.
   * - RPR-64
     - Authorization Response
     - Test handling of response format errors.
     - Error response is returned.
   * - RPR-65
     - Error Handling
     - Verify handling of invalid JWT signatures.
     - Authorization Error Response is sent.
   * - RPR-66
     - Error Handling
     - Test handling of invalid JWT claims.
     - Error response is returned.
   * - RPR-67
     - Relying Party Response
     - Verify handling of response parsing errors.
     - Error response is returned.
   * - RPR-68
     - Relying Party Response
     - Test handling of response timeout errors.
     - Error response is returned.
   * - RPR-69
     - Status Endpoint
     - Verify handling of session expiration.
     - Error response is returned.
   * - RPR-70
     - Status Endpoint
     - Test handling of session renewal errors.
     - Error response is returned.
   * - RPR-71
     - Redirect URI
     - Verify handling of redirect loop errors.
     - Error response is returned.
   * - RPR-72
     - Redirect URI
     - Test handling of redirect security errors.
     - Error response is returned.
   * - RPR-73
     - Same Device Flow
     - Verify handling of user timeouts.
     - User is notified of timeout.
   * - RPR-74
     - Cross Device Flow
     - Test QR Code scanning with different devices.
     - QR Code is scanned successfully.
   * - RPR-75
     - Cross Device Flow
     - Verify QR Code scanning with different apps.
     - QR Code is scanned successfully.
   * - RPR-76
     - Request URI Method
     - Test handling of unsupported HTTP methods.
     - Error response is returned.


Proximity Credential Presentation Test Matrix
.............................................

This section defines the general test cases about the proximity presentation flow.

.. note::

  References about ISO-1813-5 test plans will update this section in future releases.


.. list-table::
   :widths: 10 15 40 35
   :header-rows: 1

   * - Test Case
     - Category
     - Description
     - Expected Result

   * - PPR-001
     - Device Engagement
     - Test the initiation of device engagement using QR code.
     - Device engagement is successfully initiated and QR code is scanned.

   * - PPR-002
     - Session Establishment
     - Verify session establishment with correct session keys.
     - Session is established securely with correct session keys.

   * - PPR-003
     - Communication
     - Test the transmission of mdoc request over BLE.
     - mdoc request is transmitted securely over BLE.

   * - PPR-004
     - User Authentication
     - Validate user authentication via WSCA.
     - User is authenticated successfully using WSCA.

   * - PPR-005
     - Attribute Consent
     - Check user consent for attribute release.
     - User consents to release requested attributes.

   * - PPR-006
     - Data Retrieval
     - Test retrieval of mdoc Digital Credentials.
     - mdoc Digital Credentials are retrieved successfully.

   * - PPR-007
     - Session Termination
     - Verify session termination after data exchange.
     - Session is terminated and keys are destroyed.

   * - PPR-008
     - Error Handling
     - Test handling of invalid session keys.
     - Appropriate error message is displayed for invalid keys.

   * - PPR-009
     - BLE Connection
     - Test BLE connection stability during data exchange.
     - BLE connection remains stable throughout the exchange.

   * - PPR-010
     - Document Verification
     - Verify the integrity of received documents.
     - Documents are verified and integrity is confirmed.

   * - PPR-011
     - Security
     - Test encryption of mdoc requests and responses.
     - All mdoc requests and responses are encrypted correctly.

   * - PPR-012
     - User Interface
     - Check the user interface for attribute consent.
     - User interface displays attribute consent request clearly.

   * - PPR-013
     - Error Handling
     - Test response to unsupported document types.
     - System returns appropriate error for unsupported document types.

   * - PPR-014
     - Performance
     - Measure time taken for session establishment.
     - Session is established within acceptable time limits.

   * - PPR-015
     - Compatibility
     - Verify compatibility with different mobile devices.
     - System works seamlessly across various mobile devices.

   * - PPR-016
     - Data Integrity
     - Test integrity of data during transmission.
     - Data integrity is maintained during transmission.

   * - PPR-017
     - Session Management
     - Test session management under high load.
     - Sessions are managed effectively under high load conditions.

   * - PPR-018
     - BLE Connection
     - Test reconnection after BLE disconnection.
     - System reconnects successfully after BLE disconnection.

   * - PPR-019
     - User Experience
     - Evaluate user experience during the proximity flow.
     - Users report a positive experience with the proximity flow.

   * - PPR-020
     - Security
     - Test resistance to replay attacks.
     - System is resistant to replay attacks.


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


Wallet Solution Test Matrix
-----------------------------

This section provides the set of test cases for verifying conformance of a Wallet Solution implementation to the technical rules defined in the IT-Wallet ecosystem.
The test plan is based on the mandatory requirements (MUST statements) extracted from the following documents:

- Wallet Solution
- Wallet Instance Revocation
- Wallet Attestation Issuance
- Backup and Restore


.. list-table::
  :class: longtable
  :widths: 15 15 35 35
  :header-rows: 1

  * - Test Case ID
    - Purpose
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
    - The Wallet MUST notify the Wallet Backend with a Revocation Request containing a 'status' parameter set to 'REVOKED'.
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
    - The Wallet MUST send a Revocation Request to the Backend endpoint, including the Wallet ID as a path parameter.
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
    - The Wallet MUST verify the Verifier's Presentation Request before responding.
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
    - The Wallet MUST support Selective Disclosure of Credential attributes.
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

.. include:: ../common/common_definitions.rst
.. Included via test-plans-presentation.rst at title level '^' (level 2).


Proximity Credential Verifier Test Matrix
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section provides the set of test cases designed for technical implementers and development teams responsible for creating and deploying Credential Verifiers solutions for proximity flows. It is also intended for assessment bodies inspecting and validating the implementations of Credential Verifiers solutions for proximity flows.

.. note::
  Further references about official ISO-18013-5 test plans, if available, will update this section in future releases.


.. list-table::
  :class: longtable
  :widths: 15 15 35 35
  :header-rows: 1

  * - **Test Case ID**
    - **Purpose**
    - **Description**
    - **Expected Result**

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

  * - PPR-021
    - Device Engagement
    - Verify that Device Engagement structure is CBOR encoded.
    - Device Engagement structure is correctly encoded in CBOR format.

  * - PPR-022
    - Device Engagement
    - Test that ephemeral public key is of type allowed by selected cipher suite.
    - Ephemeral public key meets the requirements of the selected cipher suite.

  * - PPR-023
    - Server Retrieval
    - Verify that the ETSI profile rejects Server Retrieval.
    - Server Retrieval is rejected; only profiled proximity retrieval methods are accepted.

  * - PPR-024
    - Capabilities
    - Test that ``HandoverSessionEstablishmentSupport`` is set to ``true`` when present.
    - ``HandoverSessionEstablishmentSupport`` is correctly set to ``true``.

  * - PPR-025
    - Capabilities
    - Verify that ``ReaderAuthAllSupport`` is optional and does not replace per-request authentication.
    - The flag is not required merely because ``Capabilities`` is present, and ``readerAuthAll`` never substitutes for ``readerAuth``.

  * - PPR-026
    - mdoc Request
    - Test that mdoc Request messages are CBOR encoded.
    - mdoc Request messages are correctly encoded in CBOR format.

  * - PPR-027
    - mdoc Request
    - Verify that mdoc request is encrypted with session key.
    - mdoc request is correctly encrypted with session key.

  * - PPR-028
    - mdoc Request
    - Test that mdoc request is transmitted via BLE protocol.
    - mdoc request is correctly transmitted via BLE protocol.

  * - PPR-029
    - mdoc Response
    - Verify that mdoc Response messages are CBOR encoded.
    - mdoc Response messages are correctly encoded in CBOR format.

  * - PPR-030
    - mdoc Response
    - Test that mdoc response is encrypted with session key.
    - mdoc response is correctly encrypted with session key.

  * - PPR-031
    - Key Management
    - Test that private ephemeral key is kept secret.
    - Private ephemeral key is properly secured and not exposed.

  * - PPR-032
    - Key Management
    - Test that public ephemeral key is used in session establishment.
    - Public ephemeral key is correctly used for session establishment.

  * - PPR-033
    - Session Key Derivation
    - Test that session keys are derived using key agreement protocol.
    - Session keys are correctly derived using the key agreement protocol.

  * - PPR-034
    - Session Establishment
    - Test that ``SessionEstablishment`` message is prepared correctly.
    - The envelope carries ``EReaderKey.Pub`` and encrypted ``DeviceRequest`` and is not treated as a signed object.

  * - PPR-035
    - Session Establishment
    - Test per-``DocRequest`` ``readerAuth`` signatures and their ``ReaderAuthentication`` input.
    - Every ``DocRequest`` contains an independently valid ``readerAuth``; no whole-envelope signature is required.

  * - PPR-036
    - Session Establishment
    - Test that ``SessionEstablishment`` message is encrypted with session keys.
    - ``SessionEstablishment`` message is properly encrypted with session keys.

  * - PPR-037
    - Session Establishment
    - Test that ``SessionEstablishment`` includes ``EReaderKey.Pub`` and encrypted ``DeviceRequest``.
    - The envelope includes the key and encrypted request, whose ``DocRequest`` entries contain the required reader authentication.

  * - PPR-038
    - Message Transmission
    - Test that ``SessionEstablishment`` is transmitted over secure BLE connection.
    - ``SessionEstablishment`` message is transmitted over secure BLE connection.

  * - PPR-039
    - Session Key Computation
    - Test that Relying Party correctly handles Wallet Instance session key computation.
    - Wallet Instance correctly computes session key.

  * - PPR-040
    - Message Decryption
    - Test that Relying Party correctly handles Wallet Instance decrypting ``SessionEstablishment`` message.
    - Wallet Instance successfully decrypts ``SessionEstablishment`` message.

  * - PPR-041
    - Signature Verification
    - Test that the Wallet validates every ``readerAuth`` and selects exactly one trust path.
    - The Wallet validates the certificate chain and signature for every request, rejects ambiguity, and never retries under the other framework.

  * - PPR-042
    - Attribute Request Processing
    - Test that Relying Party correctly handles Wallet Instance decrypting attribute request.
    - Wallet Instance successfully decrypts attribute request.

  * - PPR-043
    - User Consent
    - Test that Relying Party correctly handles Wallet Instance prompting user for consent.
    - Wallet Instance correctly prompts user for consent to release attributes.

  * - PPR-044
    - Certificate Display
    - Test path-correct User Transparency data.
    - Wallet Instance displays validated RP/Service, purpose, requested Credentials/attributes, retention and privacy-policy information; raw certificate/JWT display is not required.

  * - PPR-045
    - Credential Retrieval
    - Test that Relying Party correctly handles Wallet Instance retrieving requested mdoc Digital Credentials.
    - Wallet Instance successfully retrieves requested mdoc Digital Credentials.

  * - PPR-046
    - SessionData Preparation
    - Test that Relying Party correctly handles Wallet Instance preparing ``SessionData`` message.
    - Wallet Instance correctly prepares ``SessionData`` message with Digital Credentials.

  * - PPR-047
    - Authentication Data Signing
    - Test that Relying Party correctly handles Wallet Instance signing required authentication data.
    - Wallet Instance correctly signs required authentication data.

  * - PPR-048
    - Message Encryption
    - Test that ``SessionData`` is encrypted with session keys.
    - ``SessionData`` message is properly encrypted with session keys.

  * - PPR-049
    - CBOR Encoding
    - Test that mdoc response is encoded in CBOR format.
    - mdoc response is correctly encoded in CBOR format.

  * - PPR-050
    - Data Verification
    - Test that RP Instance decrypts ``SessionData``.
    - Relying Party Instance successfully decrypts ``SessionData``.

  * - PPR-051
    - Signature Verification
    - Test that RP Instance verifies Wallet Instance signature.
    - Relying Party Instance correctly verifies Wallet Instance signature.

  * - PPR-052
    - Document Validation
    - Test independent device, issuer, digest, temporal and status validation.
    - Relying Party validates each mdoc under its Credential Rulebook independently of reader trust and applies applicable Token Status List processing.

  * - PPR-053
    - BLE Disconnection
    - Test that GATT Client unsubscribes from characteristics.
    - GATT Client properly unsubscribes from characteristics.

  * - PPR-054
    - BLE Disconnection
    - Test that GATT Client disconnects from GATT server.
    - GATT Client properly disconnects from GATT server.

  * - PPR-055
    - Request Structure Compliance
    - Test that mdoc Request is compliant with required structure. In particular, it includes ``readerAuth`` and every ``ItemsRequest`` has non-empty ``requestInfo`` with ``euWrprc`` and complete ``euWrpRegistrarInfo``.
    - mdoc Request complies with ETSI ``ISO/IEC 18013-REQ-01`` through ``-11`` and the selected path semantics.

  * - PPR-056
    - Response Structure Compliance
    - Test that mdoc Response is compliant with required structure.
    - A successful ``Document`` has no ``errors``; error-bearing documents are not successful EAAPs.

  * - PPR-057
    - Document Structure Compliance
    - Test map structures and attribute placement.
    - ``issuerSigned`` and ``deviceSigned`` are maps, issuer-signed disclosures are in ``issuerSigned``, and ``deviceSigned`` contains only Provider-authorized device attributes.

  * - PPR-058
    - Document Type Validation
    - Test that mDL document type is correctly set.
    - mDL document type is correctly set to ``org.iso.18013.5.1.mDL``.

  * - PPR-059
    - DeviceSigned Structure
    - Test that deviceSigned structure is compliant.
    - deviceSigned structure complies with required format and includes necessary components.

  * - PPR-060
    - Device Authentication
    - ``deviceAuth`` is a map including the required ``deviceSignature`` and supports ECDSA P-256/SHA-256.
    - Device authentication is correctly represented and validated with the applicable cryptographic baseline.

  * - PPR-061
    - Wallet Attestation Inclusion
    - Test that Relying Party correctly handles Wallet Instance including Wallet Attestation when requested.
    - Wallet Instance includes Wallet Attestation when requested by Relying Party.

  * - PPR-062
    - AAL Claim Inclusion
    - Test that Relying Party correctly handles Wallet Instance including ``aal`` claim in Wallet Attestation.
    - Wallet Instance includes ``aal`` claim as disclosure in Wallet Attestation.

  * - PPR-063
    - User Consent Bypass
    - Test that Relying Party correctly handles Wallet Instance not requesting user consent for Wallet Attestation.
    - Wallet Instance does not request user consent for technical Wallet Attestation attributes.

  * - PPR-064
    - Session Termination Conditions
    - Test that session is terminated under specified conditions.
    - Session is properly terminated when specified conditions occur.

  * - PPR-065
    - Session Termination Initiation
    - Test that session termination is initiated correctly.
    - Session termination is properly initiated when no further requests are sent.

  * - PPR-066
    - Key Destruction
    - Test that session keys are destroyed on termination.
    - Session keys and ephemeral key material are properly destroyed.

  * - PPR-067
    - Channel Closure
    - Test that communication channel is closed on termination.
    - Communication channel used for data retrieval is properly closed.
  * - PPR-068
    - Trust Path Selection
    - Test EUDIW selection from a WRPAC path and National selection from an Authentication Trust Anchor path.
    - The validating Trust Anchor selects exactly one path before authorization.
  * - PPR-069
    - Trust Path Failure
    - Test ambiguous, invalid, mixed-evidence and cross-framework retry cases.
    - The Wallet rejects ambiguity or failure, does not combine WRPAC/WRPRC with National evidence, and does not retry the other path.
  * - PPR-070
    - EUDIW Reader Authentication
    - Test WRPAC chain order, Trust Anchor exclusion, revocation, SCT and proof of possession.
    - EUDIW ``readerAuth`` validates only with the applicable WRPAC List of Trusted Entities and the WRPAC end entity first.
  * - PPR-071
    - National Reader Authentication
    - Test the National authentication certificate, path validation and revocation against the Authentication Trust Anchor.
    - National ``readerAuth`` validates only against the Authentication Trust Anchor distributed in the Federation Trust Anchor Entity Configuration.
  * - PPR-072
    - Request Information
    - Test mandatory non-empty ``requestInfo`` and complete Registrar data in every ``ItemsRequest``.
    - Missing, empty or mistyped ``euWrprc`` or ``euWrpRegistrarInfo`` is rejected.
  * - PPR-073
    - EUDIW Authorization Artifact
    - Test that EUDIW ``euWrprc`` is a serialized ``rc-wrp+cwt`` WRPRC and remains authoritative.
    - The WRPRC is validated, Registrar data cannot replace it, and a missing or invalid WRPRC does not trigger a Register lookup.
  * - PPR-074
    - National Authorization Artifact
    - Test that National ``euWrprc`` is UTF-8 compact signed ``registration-entity`` Trust Mark JWT bytes.
    - The Trust Mark is validated only on the National path; EUDIW evidence and fallback are rejected.
  * - PPR-075
    - National Identity Binding
    - Test binding of certificate identity, Trust Mark subject/official identifiers and Registrar identifiers.
    - All identifiers resolve to the same direct Relying Party; mismatches are terminal and National intermediated proximity is not introduced.
  * - PPR-076
    - Authorization Scope
    - Test entitlement, exact case-sensitive ``docType`` and namespace scope, overasking and applicable EDP checks under both paths.
    - Disclosure is blocked for missing entitlement, overasking, or an unsatisfied applicable EDP.
  * - PPR-077
    - User Transparency
    - Test path-correct identity, service, purpose, retention, privacy-policy and Registrar transparency data.
    - The User sees validated information for the selected path and EUDIW intermediation does not expose Intermediary trade names.
  * - PPR-078
    - ReaderAuthAll Non-Substitution
    - Test a request containing ``readerAuthAll`` with missing per-request ``readerAuth``.
    - The request is rejected because ``readerAuthAll`` is additional and cannot replace ``readerAuth``.
  * - PPR-079
    - Attribute Placement
    - Test issuer-signed and device-signed attribute placement.
    - All issuer-signed attributes are in ``issuerSigned`` and ``deviceSigned`` contains attributes only when explicitly authorized by the Provider.
  * - PPR-080
    - HAIP Cryptographic Baseline
    - Test P-256/SHA-256 signature validation and SHA-256 mdoc digest support without importing HAIP transport parameters.
    - The baseline is supported, stricter Rulebooks remain effective, and no OpenID4VP transport, DCQL, ``vp_token``, JAR, JWE, redirect or Digital Credentials API behavior is required.

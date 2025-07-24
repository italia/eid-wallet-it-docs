
Proximity Credential Presentation Test Matrix
----------------------------------------------

This section defines the general test cases about the proximity presentation flow.

.. note::
  References about ISO-1813-5 test plans will update this section in future releases.


.. list-table::
  :class: longtable
  :widths: 15 15 35 35
  :header-rows: 1

  * - Test Case ID
    - Purpose
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

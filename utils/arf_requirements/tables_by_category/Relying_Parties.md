# Relying Parties

| **Requirement ID** | **Legacy ID** | **Description** | **Status** |
|-------------------|---------------|------------------|------------|
| AS-RP-06-001 | RPA_02a | The technical specifications mentioned in RPA_02 SHALL ensure that a Relying Party Instance includes its access certificates in the presentation request by value, not by reference. | 🟡 |
| AS-RP-48-003 | DATA_DLT_03 | A Wallet Instance SHALL provide a function where the User may select one Relying Party to which a data deletion request must be submitted. | 🟡 |
| AS-RP-48-004 | DATA_DLT_06 | For the initiation of a data deletion request, the log SHALL contain at least: - Date and time of the initiation of the request, - Name and unique identifier of the Relying Party to which the reque... | 🟡 |
| AS-RP-48-005 | DATA_DLT_07 | Before executing a data deletion request, a Relying Party SHALL authenticate the requesting User (or the request itself), using appropriate authentication mechanisms of its own choosing. The Relyin... | 🟡 |
| AS-RP-51-002 | RPI_02 | Empty | 🟡 |
| AS-RP-51-004 | RPI_04 | When registering an intermediated Relying Party, an intermediary SHALL provide legally valid evidence that this Relying Party will indeed use the services of this intermediary to interact with Wall... | 🟡 |
| AS-RP-51-005 | RPI_05 | When an intermediated Relying Party asks its intermediary to request some attributes from a Wallet Unit, it SHALL specify  a) its user-friendly name, b) its unique identifier, c) the URL of its Reg... | 🟡 |
| AS-RP-51-006 | RPI_06 | When requested by an intermediated Relying Party, an intermediary SHALL request a presentation of attributes from a specific Wallet Unit. In the request, the intermediary SHALL include the intermed... | 🟡 |
| AS-RP-51-007 | RPI_06a | Empty | 🟡 |
| AS-RP-51-008 | RPI_07 | In case a Wallet Unit receives a presentation request from an intermediary on behalf of an intermediated Relying Party, it SHALL display the names and identifiers of both the intermediary and the i... | 🟡 |
| AS-RP-51-009 | RPI_07a | In case a Wallet Unit receives a presentation request from an intermediary on behalf of an intermediated Relying Party, and if the User indicated that they want to verify the information registered... | 🟡 |
| AS-RP-51-010 | RPI_07b | Empty | 🟡 |
| AS-RP-51-011 | RPI_08 | When a Wallet Unit presents to an intermediary any User attributes from a PID or attestation, the intermediary SHALL, after successfully carrying out the verifications in RPI_09, forward these attr... | 🟡 |
| AS-RP-51-012 | RPI_09 | When a Wallet Unit presents to an intermediary any attributes from a PID or attestation, the intermediary SHALL verify the authenticity of the PID or attestation, its revocation status, device bind... | 🟡 |
| AS-RP-51-013 | RPI_10 | The intermediary SHALL delete any PIDs or attestations it obtained from the Wallet Unit, including any User attributes, completely and immediately after it has sent the User attributes to the inter... | 🟡 |
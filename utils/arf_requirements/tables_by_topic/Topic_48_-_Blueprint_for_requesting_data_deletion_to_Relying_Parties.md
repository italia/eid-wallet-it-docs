# Topic 48 - Blueprint for requesting data deletion to Relying Parties

| **Requirement ID** | **Legacy ID** | **Description** | **Status** |
|-------------------|---------------|------------------|------------|
| DATA_DLT_01 |  | A Wallet Provider SHALL ensure that its Wallet Units support the possibilities mentioned in DATA_DLT_02, allowing a User to request from a Relying Party the erasure of their attributes that were pr... | 🟡 |
| DATA_DLT_02 |  | A Wallet Unit SHALL support at least the following possibilities to send a data erasure request to a Relying Party: a) Open a URL in an external browser to ask for the deletion of data in a web for... | 🟡 |
| DATA_DLT_02a |  | If the User initiates sending a data erasure request for a particular attestation presentation transaction, but no Relying Party URL, e-mail address, or telephone number is available in the log for... | 🟡 |
| DATA_DLT_03 |  | A Wallet Instance SHALL provide a function where the User may select one Relying Party to which a data deletion request must be submitted. | 🟡 |
| DATA_DLT_04 |  | Empty | 🟡 |
| DATA_DLT_05 |  | A Wallet Unit SHALL include the initiation of a data deletion request in a log, so it can be displayed to the User via the dashboard as specified in [Topic 19](./annex-2.02-high-level-requirements-... | 🟡 |
| DATA_DLT_06 |  | For the initiation of a data deletion request, the log SHALL contain at least: - Date and time of the initiation of the request, - Name and unique identifier of the Relying Party to which the reque... | 🟡 |
| DATA_DLT_07 |  | Before executing a data deletion request, a Relying Party SHALL authenticate the requesting User (or the request itself), using appropriate authentication mechanisms of its own choosing. The Relyin... | 🟡 |
| DATA_DLT_08 |  | Wallet Units, Relying Parties, and Registrars SHALL comply with the relevant requirements in [Technical Specification 7](../../technical-specifications/ts7-common-interface-for-data-deletion-reques... | 🟡 |
# Topic 19 - User navigation requirements (Dashboard logs for transparency)

| **Requirement ID** | **Legacy ID** | **Description** | **Status** |
|-------------------|---------------|------------------|------------|
| DASH_01 |  | A Wallet Provider SHALL enable a User to access a user-friendly dashboard functionality in their Wallet Unit. | 🟡 |
| DASH_02 |  | The Wallet Unit SHALL log all transactions executed through the Wallet Unit, including any transactions that were not completed successfully. This log SHALL include all types of transaction execute... | 🟡 |
| DASH_02a |  | The Wallet Unit SHALL retain transactions in the log at least for the minimum retention period specified in applicable legislation. If the Wallet Unit must delete transactions from the log, for ins... | 🟡 |
| DASH_02b |  | The dashboard SHALL include a functionality to display to the User an overview of all transactions in the log. | 🟡 |
| DASH_02c |  | The transaction log meant in DASH_02 SHALL comply with all relevant requirement in [Technical Specification 10](../../technical-specifications/ts10-data-portability-and-download-(export).md), inclu... | 🟡 |
| DASH_03 |  | For a PID or attestation presentation transaction executed through the Wallet Unit, the log SHALL contain at least: a) the date and time of the transaction, b) the name and unique identifier of the... | 🟡 |
| DASH_03a |  | For a PID or attestation presentation transaction or a Wallet-to-Wallet transaction executed through the Wallet Unit, the log SHALL NOT contain the value of any attributes presented to the Relying ... | 🟡 |
| DASH_03b |  | For a Wallet-to-Wallet transaction executed through the Wallet Unit, the log SHALL contain at least: a) the date and time of the transaction, b) the role of the Wallet Unit (Holder Wallet Unit or V... | 🟡 |
| DASH_03c |  | For a pseudonym registration or presentation transaction executed through the Wallet Unit, the log SHALL contain at least: a) the date and time of the transaction, b) identifying information about ... | 🟡 |
| DASH_04 |  | For a signature or seal creation transaction executed through the Wallet Unit, the log SHALL contain at least: a) the date and time of the transaction, b) the document or data signed or sealed (if ... | 🟡 |
| DASH_05 |  | For a PID or attestation issuance or re-issuance transaction executed through the Wallet Unit, the log SHALL contain at least: a) the date and time of the transaction, b) the name, contact details ... | 🟡 |
| DASH_05a |  | For the deletion of a PID or attestation by the User, the log SHALL contain at least: a) the date and time of the deletion event, b) the attestation type of the deleted PID or attestation. c) The n... | 🟡 |
| DASH_06 |  | The Wallet Provider SHALL ensure the confidentiality, integrity, and authenticity of all transactions included in the log. | 🟡 |
| DASH_06a |  | Via the dashboard, the Wallet Unit SHALL enable the User to delete any transaction in the log. Before deleting any transactions, the Wallet Unit SHALL indicate to the User the potential consequence... | 🟡 |
| DASH_06b |  | The Wallet Unit SHALL ensure that no entity other than the User can delete transactions from the log, except possibly for the reason mentioned in DASH_02a. | 🟡 |
| DASH_07 |  | The dashboard SHALL allow the User to export the details of one or more transactions in the log to a file, using the common format specified according to DASH_02c, while ensuring their confidential... | 🟡 |
| DASH_08 |  | For a natural-person User, a Wallet Instance SHALL provide a User interface. | 🟡 |
| DASH_09 |  | The User interface referred to in DASH_08 SHALL provide a view with - the EU Digital Identity Wallet Trust Mark, - accompanying general information on the certification of Wallet Solutions, - links... | 🟡 |
| DASH_09a |  | Positioning of the view meant in DASH_09 in the Wallet UI navigation SHALL follow design guidelines provided by the European Commission. | 🟡 |
| DASH_09b |  | Wallet Providers and Wallet Units SHALL comply with all relevant requirements in [Technical Specification 1](../../technical-specifications/ts1-eudi-wallet-trust-mark.md) for the EUDI Wallet Trust ... | 🟡 |
| DASH_10 |  | Empty. *Note: See requirement WIAM_12a in [Topic 40](./annex-2.02-high-level-requirements-by-topic.md#a2323-topic-40---wallet-instance-installation-and-wallet-unit-activation-and-management). | 🟡 |
| DASH_11 |  | A Wallet Unit issued to a legal person SHALL allow the legal person to interact with the Wallet Unit in the appropriate interface provided by the Wallet Provider. | 🟡 |
| DASH_12 |  | The User interface referred to in DASH_08 SHALL enable the User, for each presentation transaction in the log, to easily request the Relying Party to delete any or all attributes presented to it in... | 🟡 |
# Preview: Issue #688 - 🟧 ARF HLR Topic 19 - User navigation requirements (Dashboard logs for transparency)

**Topic:** Topic 19 - User navigation requirements (Dashboard logs for transparency)

**Requirements ARF 2.5.0:** 19
**Requirements ARF 2.7.3:** 19

---

## Diff ARF 2.5.0 → ARF 2.7.3

### ℹ️ No changes detected

The requirements are identical between ARF 2.5.0 and ARF 2.7.3.

**Total requirements ARF 2.7.3:** 19
**Total requirements ARF 2.5.0:** 19
---

## Nuovo body completo della issue:

**ARF VERSION:**  
UPDATED TO ARF 2.7.3.

Please refer to the "Summary of Changes" section and subsequent sections to see what has changed from ARF 2.5.0 to ARF 2.7.3.

---

Legend:
- ~~Strikethrough text~~ = Removed or modified content
- **Bold text [NEW]** = New or added content
- **Bold text [MODIFIED]** = Modified content| Status

## Diff ARF 2.5.0 → ARF 2.7.3

### ℹ️ No changes detected

The requirements are identical between ARF 2.5.0 and ARF 2.7.3.


| Status | **ID** | **Requirement specification** | **IT-Wallet Mapping & Documentation** |
|---|---------|------------------|-----------------------------------|
| 🟡 | DASH_01 | A Wallet Provider SHALL enable a User to access a user-friendly dashboard functionality in their Wallet Unit. |  |
| 🟡 | DASH_02a | The Wallet Unit SHALL retain transactions in the log at least for the minimum retention period specified in applicable legislation. If the Wallet Unit must delete transactions from the log, for instance because of size limitations, the Wallet Unit SHALL notify the User via the dashboard before doing so, indicating the potential consequences for the User's data protection rights, and SHALL instruct the User how to export the transactions that are about to be deleted; see DASH_07. |  |
| 🟡 | DASH_02b | The dashboard SHALL include a functionality to display to the User an overview of all transactions in the log. |  |
| 🟡 | DASH_02c | The transaction log meant in DASH_02 SHALL comply with all relevant requirement in [Technical Specification 10](../../technical-specifications/ts10-data-portability-and-download-(export).md), including measures to ensure and/or verify its confidentiality, integrity, and authenticity. |  |
| 🟡 | DASH_03a | For a PID or attestation presentation transaction or a Wallet-to-Wallet transaction executed through the Wallet Unit, the log SHALL NOT contain the value of any attributes presented to the Relying Party or the Verifier Wallet Unit, or the value of any transactional data included in the presentation request. |  |
| 🟡 | DASH_03b | For a Wallet-to-Wallet transaction executed through the Wallet Unit, the log SHALL contain at least: a) the date and time of the transaction, b) the role of the Wallet Unit (Holder Wallet Unit or Verifier Wallet Unit), c) the attestation type(s) and the identifier(s) of the attribute(s) that were requested, as well as those that were presented, d) in the case of non-completed transactions, the reason for such non-completion. |  |
| 🟡 | DASH_04 | For a signature or seal creation transaction executed through the Wallet Unit, the log SHALL contain at least: a) the date and time of the transaction, b) the document or data signed or sealed (if available to the Wallet Unit), c) in the case of non-completed transactions, the reason for such non-completion. |  |
| 🟡 | DASH_05 | For a PID or attestation issuance or re-issuance transaction executed through the Wallet Unit, the log SHALL contain at least: a) the date and time of the transaction, b) the name, contact details (if available), and unique identifier of the corresponding PID Provider or Attestation Provider, c) the attestation type requested, as well as the attestation type issued, d) the number of attestations requested and issued (i.e., the size of the batch in case of batch issuance). d) in the case of non-completed transactions, the reason for such non-completion. e) for a re-issuance transaction, whether it was triggered by the User or by the Wallet Unit without involvement of the User, f) the URL of the associated Registrar's online service. *Note: this URL can be retrieved from the access certificate. |  |
| 🟡 | DASH_05a | For the deletion of a PID or attestation by the User, the log SHALL contain at least: a) the date and time of the deletion event, b) the attestation type of the deleted PID or attestation. c) The name and unique identifier of the corresponding PID Provider or Attestation Provider. *Note: This requirement is not about deletion of transactions from the log, as per DASH_06a. |  |
| 🟡 | DASH_06 | The Wallet Provider SHALL ensure the confidentiality, integrity, and authenticity of all transactions included in the log. |  |
| 🟡 | DASH_06a | Via the dashboard, the Wallet Unit SHALL enable the User to delete any transaction in the log. Before deleting any transactions, the Wallet Unit SHALL indicate to the User the potential consequences for the User's data protection rights. *Note: This requirement applies even in case the minimum retention period specified in applicable legislation (see DASH_02a) is not yet over. |  |
| 🟡 | DASH_06b | The Wallet Unit SHALL ensure that no entity other than the User can delete transactions from the log, except possibly for the reason mentioned in DASH_02a. |  |
| 🟡 | DASH_07 | The dashboard SHALL allow the User to export the details of one or more transactions in the log to a file, using the common format specified according to DASH_02c, while ensuring their confidentiality, authenticity and integrity. The file SHALL be stored in an external storage or remote storage location of the User's choice, from among the storage options supported by the Wallet Unit and SHALL use the common format and security measures specified according to DASH_02c. |  |
| 🟡 | DASH_08 | For a natural-person User, a Wallet Instance SHALL provide a User interface. |  |
| 🟡 | DASH_09 | The User interface referred to in DASH_08 SHALL provide a view with - the EU Digital Identity Wallet Trust Mark, - accompanying general information on the certification of Wallet Solutions, - links to the certification status information as defined in the [Technical Specification 1](../../technical-specifications/ts1-eudi-wallet-trust-mark.md). |  |
| 🟡 | DASH_09a | Positioning of the view meant in DASH_09 in the Wallet UI navigation SHALL follow design guidelines provided by the European Commission. |  |
| 🟡 | DASH_09b | Wallet Providers and Wallet Units SHALL comply with all relevant requirements in [Technical Specification 1](../../technical-specifications/ts1-eudi-wallet-trust-mark.md) for the EUDI Wallet Trust Mark. |  |
| 🟡 | DASH_11 | A Wallet Unit issued to a legal person SHALL allow the legal person to interact with the Wallet Unit in the appropriate interface provided by the Wallet Provider. |  |
| 🟡 | DASH_12 | The User interface referred to in DASH_08 SHALL enable the User, for each presentation transaction in the log, to easily request the Relying Party to delete any or all attributes presented to it in that transaction, or to send a report about that particular transaction to a DPA. |  |

---

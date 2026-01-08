# Preview: Issue #680 - ✅🟧 ARF HLR Topic 6 - Relying Party authentication and User approval

**Topic:** Topic 6 - Relying Party authentication and User approval

**Requirements ARF 2.5.0:** 14
**Requirements ARF 2.7.3:** 14

---

## Diff ARF 2.5.0 → ARF 2.7.3

### ℹ️ No changes detected

The requirements are identical between ARF 2.5.0 and ARF 2.7.3.

**Total requirements ARF 2.7.3:** 14
**Total requirements ARF 2.5.0:** 14
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


| Status | ID | Requirement Specification | IT-Wallet Mapping & Documentation |
|---|---------|------------------|-----------------------------------|
| 🟧 | RPA_01a | If a Wallet Unit supports the [W3C Digital Credentials API] for remote presentation flows, it SHALL retain full authority over the process meant in RPA_01. In particular, this process SHALL NOT be handled by a third party, including the browser and the operating system. | [Digital Credential Presentation](https://italia.github.io/eid-wallet-it-docs/versione-corrente/en/credential-presentation.html) |
| 🟡 | RPA_02 | The Commission SHALL ensure that technical specifications for the Relying Party authentication mechanism mentioned in RPA_01 are created both for Wallet Units complying with [ISO/IEC 18013-5] and for Wallet Units complying with [OpenID4VP]. These specifications SHALL comply with applicable requirements in these standards. | [Digital Credential Presentation](https://italia.github.io/eid-wallet-it-docs/versione-corrente/en/credential-presentation.html) |
| 🟧 | RPA_02a | The technical specifications mentioned in RPA_02 SHALL ensure that a Relying Party Instance includes its access certificates in the presentation request by value, not by reference. *Note: This ensures that no external requests are necessary to carry out Relying Party authentication, and that transactions are atomic and self-contained. | [Digital Credential Presentation](https://italia.github.io/eid-wallet-it-docs/versione-corrente/en/credential-presentation.html) |
| 🟡 | RPA_03 | A Wallet Unit and a Relying Party Instance SHALL perform Relying Party authentication in all PID or attestation presentation transactions to Relying Parties, whether proximity or remote, using a Relying Party Instance access certificate. *Note: The actions both entities perform differ. For example, while the Relying Party creates a signature over some data in the request, the Wallet Unit validates that signature. | [Digital Credential Presentation](https://italia.github.io/eid-wallet-it-docs/versione-corrente/en/credential-presentation.html) |
| ✅ | RPA_05 | If Relying Party authentication fails for any reason, the Wallet Instance SHALL inform the User that the identity of the Relying Party could not be verified and that therefore the request is not trustworthy. | [Digital Credential Presentation](https://italia.github.io/eid-wallet-it-docs/versione-corrente/en/credential-presentation.html) |
| 🟧 | RPA_06 | If Relying Party authentication succeeds, the Wallet Instance SHALL display to the User the name of the Relying Party as included in the Relying Party access certificate, together with the attributes requested by the Relying Party. The Wallet Instance SHALL do so when asking the User for approval according to RPA_07. *Note: If the Relying Party is an intermediary acting on behalf of an intermediated Relying Party, the Wallet Instance displays the names of both the intermediary and the intermediated Relying Party to the User, see RPI_07. | [Digital Credential Presentation](https://italia.github.io/eid-wallet-it-docs/versione-corrente/en/credential-presentation.html) |
| 🟧 | RPA_06a | If Relying Party authentication fails for any reason, the Wallet Unit SHALL notify the User. In addition, the Wallet Unit SHALL either not present the requested attributes to the Relying Party, or give the User the choice to present the requested attributes or not. *Note: It is up to the Wallet Provider to make a choice for one of these two options. |  |
| ✅ | RPA_07 | A Wallet Unit SHALL ensure the User approved the release of any attribute(s) in the Wallet Unit to a Relying Party, prior to releasing these attributes. A Wallet Unit SHALL always allow the User to refuse releasing an attribute requested by the Relying Party. | [Digital Credential Presentation](https://italia.github.io/eid-wallet-it-docs/versione-corrente/en/credential-presentation.html) |
| 🟧 | RPA_07a | If a Wallet Unit supports the [W3C Digital Credentials API] for remote presentation flows, it SHALL retain full authority over the process meant in RPA_07. In particular, this process SHALL NOT be handled by a third party, including the browser and the operating system. | [Digital Credential Presentation](https://italia.github.io/eid-wallet-it-docs/versione-corrente/en/credential-presentation.html) |
| 🟡 | RPA_08 | A Wallet Unit SHALL authenticate the User before allowing the User to give or refuse approval for releasing any attributes, in accordance with WIAM_14 or WIAM_15, as applicable. |  |
| 🟧 | RPA_09 | Empty | [Digital Credential Presentation](https://italia.github.io/eid-wallet-it-docs/versione-corrente/en/credential-presentation.html) |
| 🟡 | RPA_10a | The Wallet Unit SHOULD ensure that the User gives approval either to present all attributes requested in a presentation request, or none of them. *Note: This means that a User should be asked either to approve the presentation of all requested attributes or to deny all of them. The Wallet Unit should not allow partial approval, since this would mean that the Relying Party cannot deliver the service, but nevertheless receives some User attributes. This would be a violation of the User's privacy. Note that a Relying Party is not allowed to request more data than is justified for the intended use. So if the User feels that the Relying Party is actually requesting more data than needed, that implies that the Relying Party is not trustworthy and should not receive any data. |  |
| ✅ | RPA_11 | When the presentation of an attestation is denied by the User, the Wallet Unit SHALL behave towards the Relying Party as if the attestation did not exist. | [Digital Credential Presentation](https://italia.github.io/eid-wallet-it-docs/versione-corrente/en/credential-presentation.html) |
| 🟡 | RPA_12 | When asking for User approval, the Wallet Unit MAY indicate to the User whether the attestation requested by a Relying Party is device-bound or not. *Note: The intent of this indication is to warn the User than a non-device bound attestation may be copied by the Relying Party and presented to a third party. |  |

---

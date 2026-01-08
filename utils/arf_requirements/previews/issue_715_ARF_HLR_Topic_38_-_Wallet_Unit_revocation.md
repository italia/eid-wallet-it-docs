# Preview: Issue #715 - ARF HLR Topic 38 - Wallet Unit revocation

**Topic:** Topic 38 - Wallet Unit revocation

**Requirements ARF 2.5.0:** 21
**Requirements ARF 2.7.3:** 21

---

## Diff ARF 2.5.0 → ARF 2.7.3

### ℹ️ No changes detected

The requirements are identical between ARF 2.5.0 and ARF 2.7.3.

**Total requirements ARF 2.7.3:** 21
**Total requirements ARF 2.5.0:** 21
---

## Nuovo body completo della issue:

# Topic 38 - Wallet Unit Revocation (WURevocation) - Changelog

**ARF VERSION:**  
UPDATED TO ARF 2.7.3.

Please refer to the "Summary of Changes" section and subsequent sections to see what has changed from ARF 2.5.0 to ARF 2.7.3.

---

Legend:
- ~~Strikethrough text~~ = Removed or modified content
- **Bold text [NEW]** = New or added content
- **Bold text [MODIFIED]** = Modified content

---

## A. Issuing a Wallet Unit Attestation


### 🔄 Requirements modified in ARF 2.7.3 (3):

- **WURevocation_06**:
  - **Old:** ~~Empty~~ **Empty [NO CHANGE]
  - **New:** Empty
- **WURevocation_08**:
  - **Old:** ~~Empty~~ **Empty [NO CHANGE]
  - **New:** Empty
- **WURevocation_09**:
  - **Old:** ...a WSCA/WSCD it uses for managing cryptographic keys and sensitive data...
  - **New:** ...the WSCA/WSCD or a keystore it uses for managing cryptographic assets...

## Diff ARF 2.5.0 → ARF 2.7.3

### ℹ️ No changes detected

The requirements are identical between ARF 2.5.0 and ARF 2.7.3.


| Status | **Index** | **Requirement specification** | **IT-Wallet Mapping & Documentation** |
|---|---------|------------------|-----------------------------------|
| 🟧 | WURevocation_01 | To enable a PID Provider or an Attestation Provider to verify the authenticity and the revocation status of a Wallet Unit it is interacting with, a Wallet Provider SHALL issue one or more Wallet Unit Attestations to the Wallet Unit, as specified in Topic 9. *Note: The first of these WUAs will be issued during the activation phase of a Wallet Unit. During the lifetime of the Wallet Unit, the Wallet Provider will re-issue WUAs as needed. |  |
| 🟧 | WURevocation_02 | During the lifetime of the Wallet Unit, the Wallet Provider SHALL ensure that the Wallet Unit at all times is in possession of at least one valid WUA. |  |
| 🟧 | WURevocation_03 | Empty |  |
| 🟧 | WURevocation_04 | Empty |  |
| 🟧 | WURevocation_05 | Empty |  |
| 🟧 | WURevocation_06 | Empty |  |
| 🟧 | WURevocation_08 | Empty |  |
| 🟧 | WURevocation_09 | During the lifetime of a Wallet Unit, the Wallet Provider SHALL regularly verify that the security of the Wallet Unit is not breached or compromised. If the Wallet Provider detects a security breach or compromise, the Wallet Provider SHALL analyse its cause(s) and impact(s). If the breach or compromise affects the trustworthiness or reliability of the Wallet Unit, the Wallet Provider SHALL administratively revoke or suspend the Wallet Unit and SHALL immediately revoke the corresponding WUA(s). The Wallet Provider SHALL do so at least in the following circumstances: - If the security of the Wallet Unit, or the security of the mobile device and OS on which the corresponding Wallet Instance is installed, or the security of the WSCA/WSCD or a keystore it uses for managing cryptographic assets, is breached or compromised in a manner that affects its trustworthiness or reliability. - If the security of the Wallet Solution is breached or compromised in a manner that affects the trustworthiness or reliability of all corresponding Wallet Units. - If the security of the common authentication and data protection mechanisms used by the Wallet Unit is breached or compromised in a manner that affects their trustworthiness or reliability. - If the security of the electronic identification scheme under which the Wallet Unit is provided is breached or compromised in a manner that affects its trustworthiness or reliability. |  |
| 🟧 | WURevocation_9b | If within three months from an administrative suspension of a Wallet Unit the security breach or compromise is remedied, the Wallet Provider SHALL issue one or more WUAs to the Wallet Unit, such that the User can again use it. |  |
| 🟧 | WURevocation_11 | A Wallet Provider SHALL revoke a Wallet Unit upon the explicit request of a PID Provider, in case the natural person using the Wallet Unit has died or the legal person using the Wallet Unit has ceased operations. To do so, the Wallet Provider SHALL revoke all valid WUA(s) for that Wallet Unit. To identify the Wallet Unit that is to be revoked, the PID Provider SHALL use a Wallet Unit identifier provided by the Wallet Provider in the WUA during PID issuance. *Note: See the notes to WUA_08. |  |
| 🟧 | WURevocation_12 | Before revoking a Wallet Unit per WURevocation_11, the Wallet Provider SHALL verify that the party requesting revocation is indeed a valid PID Provider listed in the Trusted List of PID Providers. |  |
| 🟧 | WURevocation_13 | Before requesting a Wallet Provider to revoke a Wallet Unit per WURevocation_11, the PID Provider SHALL ensure that the revocation does not harm the interests of any of the stakeholders. The PID Provider SHALL have (and follow) a documented policy to ensure that this is the case. |  |
| 🟡 | WURevocation_14 | A Wallet Provider SHALL inform a User without delay, and within 24 hours at most, in case the Wallet Provider decided to revoke the User's Wallet Unit. The Wallet Provider SHALL also inform the User about the reason(s) for the revocation. This information SHALL be understandable for the general public. It SHALL include (a reference to) technical details about any security breach if applicable. |  |
| 🟡 | WURevocation_15 | Empty |  |
| 🟡 | WURevocation_16 | To inform a User about the revocation of their Wallet Unit, the Wallet Provider SHALL use a communication channel that is independent of the Wallet Unit. In addition, the Wallet Provider MAY use the Wallet Unit itself to inform the User. |  |
| 🟡 | WURevocation_17 | Empty |  |
| 🟡 | WURevocation_19 | An Attestation Provider issuing revocable attestations MAY decide to revoke an attestation if the Wallet Provider revoked the Wallet Unit on which that attestation is residing, in the same manner as described in WURevocation_18. An Attestation Provider SHALL publish its policy in this regard. *Note: Publishing its policy regarding revocation allows a Relying Party to decide if it can put sufficient trust in the attestations issued by that Attestation Provider. |  |
| 🟡 | WURevocation_19a | Empty |  |
| 🟡 | WURevocation_19b | Empty |  |
| 🟡 | WURevocation_20 | Empty |  |
| 🟡 | WURevocation_21 | Empty |  |
## C. Informing the User

| **Index**         | **Requirement specification** | **IT-Wallet Mapping & Documentation** |
|---|-------------------|------------------------------|---------------------------------------|
| 🟧 | WURevocation_14   | A Wallet Provider SHALL inform a User without delay, and within 24 hours at most, in case the Wallet Provider decided to revoke the User's Wallet Unit. The Wallet Provider SHALL also inform the User about the reason(s) for the revocation. This information SHALL be understandable for the general public. It SHALL include (a reference to) technical details about any security breach if applicable. | |
| 🟧 | WURevocation_15   | ~~Empty~~ **Empty [NO CHANGE]** | |
| 🟧 | WURevocation_16   | To inform a User about the revocation of their Wallet Unit, the Wallet Provider SHALL use a communication channel that is independent of the Wallet Unit. In addition, the Wallet Provider MAY use the Wallet Unit itself to inform the User. | |

---

## D. Verifying the revocation status of a Wallet Unit

| **Index**         | **Requirement specification** | **IT-Wallet Mapping & Documentation** |
|---|-------------------|------------------------------|---------------------------------------|
| 🟧 | WURevocation_17   | ~~Empty~~ **Empty [NO CHANGE]** | |
| 🟧 | WURevocation_18   | A PID Provider issuing revocable PIDs SHALL, for each of its valid PIDs, regularly verify whether the Wallet Provider revoked the Wallet Unit on which that PID is residing, using the revocation information in the WUA it received during issuance of that PID. If it turns out that the Wallet Unit is revoked, the PID Provider SHALL immediately revoke the respective PID in accordance with all requirements in [[Topic 7](#a237-topic-7---attestation-revocation-and-revocation-checking)]. *Notes: - This is a consequence of the legal requirement in [CIR 2024/2977], Article 5, 4.(b). - See [Technical Specification 3](../../technical-specifications/ts3-wallet-unit-attestation.md) for how the PID Provider can do this verification. - The reverse is not true: When a PID is revoked, this does not imply that the Wallet Unit on which it is residing should also be revoked. Instead, the Wallet Unit moves to the Operational state. See [ARF main document Section 4.6.3](../../architecture-and-reference-framework-main.md#463-wallet-unit).* | |
| 🟧 | WURevocation_19   | An Attestation Provider issuing revocable attestations MAY decide to  revoke an attestation if the Wallet Provider revoked the Wallet Unit on which that attestation is residing, in the same manner as described in WURevocation_18. An Attestation Provider SHALL publish its policy in this regard. *Note: Publishing its policy regarding revocation allows a Relying Party to decide if it can put sufficient trust in the attestations issued by that Attestation Provider.* | |
| 🟧 | WURevocation_19a  | ~~?~~ **Empty [MODIFIED]** | |
| 🟧 | WURevocation_19b  | ~~?~~ **Empty [MODIFIED]** | |
| 🟧 | WURevocation_20   | ~~?~~ **Empty [MODIFIED]** | |
| 🟧 | WURevocation_21   | ~~?~~ **Empty [MODIFIED]** | |

---

## Summary of Changes

### Modified Requirements:

**WURevocation_19a, 19b, 20, 21**: Changed from "?" to "Empty"
- **OLD**: Listed as "?" (undefined placeholders)
- **NEW**: Changed to "Empty" (defined placeholders)
- **Significance**: Clarifies these are intentional empty placeholders, not missing requirements

### No Other Changes:

All substantive WURevocation requirements (WURevocation_01, 02, 07, 09, 9b, 10-14, 16, 18, 19) remain completely unchanged.

### Related Topics:

- **Topic 7** (Attestation Revocation): Revocation mechanisms referenced
- **Topic 9** (WUA): WUA issuance specifications
- **Topic 40** (Activation): User registration process
- **Topic 31** (Trusted Lists): PID Provider verification

All requirements remain assigned to 🟧 status, with clear responsibilities for PID/Attestation Providers. The numerous empty placeholders suggest potential for future expansion of revocation procedures.

---

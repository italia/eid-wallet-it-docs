# Preview: Issue #692 - ⚠️❌ ARF HLR Topic 30 - Interaction between Wallet Units

**Topic:** Topic 30 - Interaction between Wallet Units

**Requirements ARF 2.5.0:** 20
**Requirements ARF 2.7.3:** 20

---

## Diff ARF 2.5.0 → ARF 2.7.3

### ℹ️ No changes detected

The requirements are identical between ARF 2.5.0 and ARF 2.7.3.

**Total requirements ARF 2.7.3:** 20
**Total requirements ARF 2.5.0:** 20
---

## Nuovo body completo della issue:

**ARF VERSION:**  
UPDATED TO ARF 2.7.3.

Please refer to the "Summary of Changes" section and subsequent sections to see what has changed from ARF 2.5.0 to ARF 2.7.3.

---

Legend:
- ~~Strikethrough text~~ = Removed or modified content
- **Bold text [NEW]** = New or added content
- **Bold text [MODIFIED]** = Modified content

---


### ✅ Requirements added in ARF 2.7.3 (1):

- **W2W_22**: Wallet Providers SHOULD take measures to prevent a User from taking screenshots while their Wallet Unit is acting as a Verifier Wallet Unit.


### ✅ Requirements added in ARF 2.7.3 (1):

- **W2W_22**: Wallet Providers SHOULD take measures to prevent a User from taking screenshots while their Wallet Unit is acting as a Verifier Wallet Unit.

## Diff ARF 2.5.0 → ARF 2.7.3

### ℹ️ No changes detected

The requirements are identical between ARF 2.5.0 and ARF 2.7.3.


| Status | **Index** | **Requirement specification** | **IT-Wallet Mapping & Documentation** |
|---|---------|------------------|-----------------------------------|
| ⚠️ | W2W_01 | A Wallet Unit SHALL be able to act as a Holder Wallet Unit, in accordance with all requirements in this Topic. |  |
| ⚠️ | W2W_02 | When acting as a Holder Wallet Unit, if there is a contradiction between a requirement for Holder Wallet Units in this Topic and any requirement for Wallet Units in other Topics in this document, the requirement in this Topic SHALL take precedence. However, when acting as a Holder Wallet Unit, a Wallet Unit SHALL comply with all requirements for Wallet Units in other Topics in this document that do not contradict any requirement in this Topic. |  |
| ⚠️ | W2W_03 | A Wallet Unit SHALL be able to act as a Verifier Wallet Unit, in accordance with all requirements in this Topic. |  |
| ⚠️ | W2W_04 | When acting as a Verifier Wallet Unit, a Wallet Unit SHALL NOT comply with any requirement for Wallet Units in other Topics in this document. |  |
| ⚠️ | W2W_05 | A Wallet Unit SHALL act as a Holder Wallet Unit only if the User selects a 'Holder Wallet Unit mode'. If the User closes the Wallet Unit, or after a period of non-activity, the Wallet Unit SHALL return to 'normal' mode. |  |
| ⚠️ | W2W_06 | When entering the Holder Wallet Unit mode, a Wallet Unit SHALL inform its User that this mode should only be used for interactions with natural persons using a Wallet Unit, and that the User should not proceed if they are in fact interacting with a Relying Party. |  |
| ⚠️ | W2W_07 | A Wallet Unit SHALL act as a Verifier Wallet Unit only if the User selects a 'Verifier Wallet Unit mode'. If the User closes the Wallet Unit, or after a period of non-activity, the Wallet Unit SHALL return to 'normal' mode. |  |
| ⚠️ | W2W_08 | A Verifier Wallet Unit and a Holder Wallet Unit SHALL support attestation presentation only in proximity, meaning they SHALL support only [ISO/IEC 18013-5] to communicate. |  |
| ⚠️ | W2W_09 | Holder Wallet Units SHALL comply with the requirements for mDLs and for mdocs in ISO/IEC 18013-5, unless specified differently in [Technical Specification 9](../../technical-specifications/ts9-wallet-to-wallet-interactions.md). |  |
| ⚠️ | W2W_10 | Verifier Wallet Units SHALL comply with the requirements for mDL readers and for mdoc readers in ISO/IEC 18013-5, unless specified differently in [Technical Specification 9](../../technical-specifications/ts9-wallet-to-wallet-interactions.md). |  |
| 🟡 | W2W_11 | A Holder Wallet Unit SHOULD provide the Holder, through a user-friendly UI, with the option to inform the Verifier Wallet Unit about the attributes which the Verifier should include in the presentation request, by sending a presentation offer. If the Holder creates a presentation offer, the Holder Wallet Unit SHALL transfer it to the Verifier Wallet Unit as specified in [Technical Specification 9](../../technical-specifications/ts9-wallet-to-wallet-interactions.md). *Note: TS9 specifies an extension of the device engagement structure specified in ISO/IEC 18013-5. |  |
| 🟡 | W2W_12 | A Holder Wallet Unit SHALL recommend the Holder to create a presentation offer, as this will increase the chance of success of the use case. |  |
| 🟡 | W2W_13 | A Verifier Wallet Unit SHALL provide the Verifier, through a user-friendly UI, with the possibility to select the attributes that will be included in the presentation request. |  |
| 🟡 | W2W_14 | For the purposes of W2W_07, if the Verifier Wallet Unit received a presentation offer, it SHALL present this offer to the Verifier, and enable the Verifier to include one or more of the attributes in the offer into the presentation request. However, the Verifier Wallet Unit SHALL NOT allow the Verifier to include any attribute not present in the offer. |  |
| 🟡 | W2W_15 | For the purposes of W2W_07, if the Verifier Wallet Unit did not receive a presentation offer, it SHALL present the Verifier with a list of attributes that can be included in the presentation request. The Verifier Wallet Unit MAY ask the Verifier some questions about the purpose of the use case to narrow down the list. |  |
| 🟡 | W2W_16 | A Verifier Wallet Unit SHALL authenticate the Verifier and SHALL obtain the Verifier's approval prior to sending a presentation request to a Holder Wallet Unit. |  |
| 🟡 | W2W_17 | A Verifier Wallet Unit SHALL implement measures to limit the number of presentation requests it can send per unit of time, to prevent abuse of the Wallet-to-Wallet functionality by Relying Parties. The limitation strategy, for instance exponential backoff time between subsequent presentation requests or hard limits for the number of requests, SHALL be decided by the Wallet Provider, based on applicable requirements in [Technical Specification 9](../../technical-specifications/ts9-wallet-to-wallet-interactions.md). |  |
| 🟡 | W2W_18 | When receiving a presentation request, a Holder Wallet Unit SHOULD verify the validity of the Verifier Wallet Unit before presenting a received request to the Holder, provided [Technical Specification 9](../../technical-specifications/ts9-wallet-to-wallet-interactions.md) specifies a suitable mechanism for doing so. |  |
| 🟡 | W2W_20 | A Verifier Wallet Unit SHALL display all verified attributes to the Verifier. |  |
| 🟡 | W2W_22 | Wallet Providers SHOULD take measures to prevent a User from taking screenshots while their Wallet Unit is acting as a Verifier Wallet Unit. |  |

---

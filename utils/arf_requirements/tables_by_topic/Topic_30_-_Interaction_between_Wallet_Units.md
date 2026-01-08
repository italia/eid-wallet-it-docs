# Topic 30 - Interaction between Wallet Units

| **Requirement ID** | **Legacy ID** | **Description** | **Status** |
|-------------------|---------------|------------------|------------|
| W2W_01 |  | A Wallet Unit SHALL be able to act as a Holder Wallet Unit, in accordance with all requirements in this Topic. | 🟡 |
| W2W_02 |  | When acting as a Holder Wallet Unit, if there is a contradiction between a requirement for Holder Wallet Units in this Topic and any requirement for Wallet Units in other Topics in this document, t... | 🟡 |
| W2W_03 |  | A Wallet Unit SHALL be able to act as a Verifier Wallet Unit, in accordance with all requirements in this Topic. | 🟡 |
| W2W_04 |  | When acting as a Verifier Wallet Unit, a Wallet Unit SHALL NOT comply with any requirement for Wallet Units in other Topics in this document. | 🟡 |
| W2W_05 |  | A Wallet Unit SHALL act as a Holder Wallet Unit only if the User selects a 'Holder Wallet Unit mode'. If the User closes the Wallet Unit, or after a period of non-activity, the Wallet Unit SHALL re... | 🟡 |
| W2W_06 |  | When entering the Holder Wallet Unit mode, a Wallet Unit SHALL inform its User that this mode should only be used for interactions with natural persons using a Wallet Unit, and that the User should... | 🟡 |
| W2W_07 |  | A Wallet Unit SHALL act as a Verifier Wallet Unit only if the User selects a 'Verifier Wallet Unit mode'. If the User closes the Wallet Unit, or after a period of non-activity, the Wallet Unit SHAL... | 🟡 |
| W2W_08 |  | A Verifier Wallet Unit and a Holder Wallet Unit SHALL support attestation presentation only in proximity, meaning they SHALL support only [ISO/IEC 18013-5] to communicate. | 🟡 |
| W2W_09 |  | Holder Wallet Units SHALL comply with the requirements for mDLs and for mdocs in ISO/IEC 18013-5, unless specified differently in [Technical Specification 9](../../technical-specifications/ts9-wall... | 🟡 |
| W2W_10 |  | Verifier Wallet Units SHALL comply with the requirements for mDL readers and for mdoc readers in ISO/IEC 18013-5, unless specified differently in [Technical Specification 9](../../technical-specifi... | 🟡 |
| W2W_11 |  | A Holder Wallet Unit SHOULD provide the Holder, through a user-friendly UI, with the option to inform the Verifier Wallet Unit about the attributes which the Verifier should include in the presenta... | 🟡 |
| W2W_12 |  | A Holder Wallet Unit SHALL recommend the Holder to create a presentation offer, as this will increase the chance of success of the use case. | 🟡 |
| W2W_13 |  | A Verifier Wallet Unit SHALL provide the Verifier, through a user-friendly UI, with the possibility to select the attributes that will be included in the presentation request. | 🟡 |
| W2W_14 |  | For the purposes of W2W_07, if the Verifier Wallet Unit received a presentation offer, it SHALL present this offer to the Verifier, and enable the Verifier to include one or more of the attributes ... | 🟡 |
| W2W_15 |  | For the purposes of W2W_07, if the Verifier Wallet Unit did not receive a presentation offer, it SHALL present the Verifier with a list of attributes that can be included in the presentation reques... | 🟡 |
| W2W_16 |  | A Verifier Wallet Unit SHALL authenticate the Verifier and SHALL obtain the Verifier's approval prior to sending a presentation request to a Holder Wallet Unit. | 🟡 |
| W2W_17 |  | A Verifier Wallet Unit SHALL implement measures to limit the number of presentation requests it can send per unit of time, to prevent abuse of the Wallet-to-Wallet functionality by Relying Parties.... | 🟡 |
| W2W_18 |  | When receiving a presentation request, a Holder Wallet Unit SHOULD verify the validity of the Verifier Wallet Unit before presenting a received request to the Holder, provided [Technical Specificat... | 🟡 |
| W2W_20 |  | A Verifier Wallet Unit SHALL display all verified attributes to the Verifier. | 🟡 |
| W2W_22 |  | Wallet Providers SHOULD take measures to prevent a User from taking screenshots while their Wallet Unit is acting as a Verifier Wallet Unit. | 🟡 |
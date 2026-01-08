# Topic 6 - Relying Party authentication and User approval

| **Requirement ID** | **Legacy ID** | **Description** | **Status** |
|-------------------|---------------|------------------|------------|
| RPA_01a |  | If a Wallet Unit supports the [W3C Digital Credentials API] for remote presentation flows, it SHALL retain full authority over the process meant in RPA_01. In particular, this process SHALL NOT be ... | 🟡 |
| RPA_02 |  | The Commission SHALL ensure that technical specifications for the Relying Party authentication mechanism mentioned in RPA_01 are created both for Wallet Units complying with [ISO/IEC 18013-5] and f... | 🟡 |
| RPA_02a |  | The technical specifications mentioned in RPA_02 SHALL ensure that a Relying Party Instance includes its access certificates in the presentation request by value, not by reference. *Note: This ensu... | 🟡 |
| RPA_03 |  | A Wallet Unit and a Relying Party Instance SHALL perform Relying Party authentication in all PID or attestation presentation transactions to Relying Parties, whether proximity or remote, using a Re... | 🟡 |
| RPA_05 |  | If Relying Party authentication fails for any reason, the Wallet Instance SHALL inform the User that the identity of the Relying Party could not be verified and that therefore the request is not tr... | 🟡 |
| RPA_06 |  | If Relying Party authentication succeeds, the Wallet Instance SHALL display to the User the name of the Relying Party as included in the Relying Party access certificate, together with the attribut... | 🟡 |
| RPA_06a |  | If Relying Party authentication fails for any reason, the Wallet Unit SHALL notify the User. In addition, the Wallet Unit SHALL either not present the requested attributes to the Relying Party, or ... | 🟡 |
| RPA_07 |  | A Wallet Unit SHALL ensure the User approved the release of any attribute(s) in the Wallet Unit to a Relying Party, prior to releasing these attributes. A Wallet Unit SHALL always allow the User to... | 🟡 |
| RPA_07a |  | If a Wallet Unit supports the [W3C Digital Credentials API] for remote presentation flows, it SHALL retain full authority over the process meant in RPA_07. In particular, this process SHALL NOT be ... | 🟡 |
| RPA_08 |  | A Wallet Unit SHALL authenticate the User before allowing the User to give or refuse approval for releasing any attributes, in accordance with WIAM_14 or WIAM_15, as applicable. | 🟡 |
| RPA_09 |  | Empty | 🟡 |
| RPA_10a |  | The Wallet Unit SHOULD ensure that the User gives approval either to present all attributes requested in a presentation request, or none of them. *Note: This means that a User should be asked eithe... | 🟡 |
| RPA_11 |  | When the presentation of an attestation is denied by the User, the Wallet Unit SHALL behave towards the Relying Party as if the attestation did not exist. | 🟡 |
| RPA_12 |  | When asking for User approval, the Wallet Unit MAY indicate to the User whether the attestation requested by a Relying Party is device-bound or not. *Note: The intent of this indication is to warn ... | 🟡 |
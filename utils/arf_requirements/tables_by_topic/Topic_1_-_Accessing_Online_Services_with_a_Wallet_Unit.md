# Topic 1 - Accessing Online Services with a Wallet Unit

| **Requirement ID** | **Legacy ID** | **Description** | **Status** |
|-------------------|---------------|------------------|------------|
| OIA_01 |  | A Wallet Unit SHALL support [OpenID4VP] for remote presentation flows and [ISO/IEC 18013-5] for proximity presentation flows, to receive and respond to presentation requests for person identificati... | 🟡 |
| OIA_02 |  | A Wallet Unit SHALL support proving cryptographic device binding between the WSCA/WSCD or a keystore included in the Wallet Unit and a PID or attestation, in accordance with [SD-JWT VC] or [ISO/IEC... | 🟡 |
| OIA_03 |  | Empty | 🟡 |
| OIA_03a |  | Wallet Providers SHALL ensure that their Wallet Solution supports the protocol specified in 'OpenID for Verifiable Presentations', see [OpenID4VP], with additions and changes as documented in this ... | 🟡 |
| OIA_03b |  | For remote presentation flows, when the format of the requested attestation complies with [ISO/IEC 18013-5], Relying Parties and Wallet Units SHALL comply with the requirements in the profile for O... | 🟡 |
| OIA_03c |  | For remote presentation flows, when the format of the requested attestation complies with [SD-JWT VC], Relying Parties and Wallet Units SHALL comply with the requirements in the 'OpenID for Verifia... | 🟡 |
| OIA_04 |  | A Wallet Unit SHALL verify and process PID or attestation presentation requests from Relying Parties in accordance with the protocols and interfaces specified in [OpenID4VP] for remote flows. | 🟡 |
| OIA_05 |  | After verifying and processing a PID or attestation request, the Wallet Unit SHALL display to the User the identity of the requesting Relying Party and the requested attributes. | 🟡 |
| OIA_06 |  | A Wallet Unit SHALL present the requested attributes only after having received the User's authorisation. *Note: See also OIA_07. | 🟡 |
| OIA_07 |  | A Wallet Unit SHALL support selective disclosure of attributes from PIDs and attestations to be released to the requesting Relying Parties. | 🟡 |
| OIA_08 |  | Wallet Units and Relying Party Instances SHALL support the [W3C Digital Credentials API]](<https://wicg.github.io/digital-credentials/>) for remote presentation flows, provided that a) this API is ... | 🟡 |
| OIA_08a |  | If Wallet Units and Relying Party Instances do not support the [W3C Digital Credentials API], they SHALL implement adequate mitigations for the challenges described in [Section 4.4.3.1](../../archi... | 🟡 |
| OIA_08b |  | If a Wallet Unit supports the [W3C Digital Credentials API], it SHALL, by default (see OIA_08d), disclose the presence of all stored attestations (mean their attestation type) to the Digital Creden... | 🟡 |
| OIA_08c |  | If a Relying Party supports the [W3C Digital Credentials API], the Relying Party's presentation request MAY be processed by the browser and/or the operating system for searching available attestati... | 🟡 |
| OIA_08d |  | If a Wallet Unit supports the [W3C Digital Credentials API], it SHALL provide a global User setting to disable the disclosure of stored attestations via the Digital Credentials API framework, as de... | 🟡 |
| OIA_08e |  | If a Wallet Unit supports the [W3C Digital Credentials API], it SHALL use the CTAP-Hybrid flow only if the expectations outlined in Chapter 4 of the [Topic F discussion paper](../../discussion-topi... | 🟡 |
| OIA_09 |  | For remote presentation flows the Wallet Unit SHALL ensure that the attributes included in the presented attestation are accessible only to the Relying Party Instance, by encrypting the presentatio... | 🟡 |
| OIA_10 |  | For both proximity and remote presentation flows, if a Wallet Unit contains two PIDs having the same encoding (e.g. ISO/IEC 18013-5 or SD-JWT VC-compliant) and a Relying Party requests a PID, the W... | 🟡 |
| OIA_13 |  | For both proximity and remote presentation flows, a Relying Party SHALL validate the qualified signature of a QEAA in accordance with Art.32 of the [European Digital Identity Regulation]. For the v... | 🟡 |
| OIA_14 |  | For both proximity and remote presentation flows, a Relying Party SHALL validate the qualified signature of a PuB-EAA in accordance with [Art.32](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri... | 🟡 |
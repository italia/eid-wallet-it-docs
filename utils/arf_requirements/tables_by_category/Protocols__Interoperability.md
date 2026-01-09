# Protocols & Interoperability

| **Requirement ID** | **Legacy ID** | **Description** | **Status** |
|-------------------|---------------|------------------|------------|
| EW-PIO-01-001 | OIA_01 | A Wallet Unit SHALL support [OpenID4VP] for remote presentation flows and [ISO/IEC 18013-5] for proximity presentation flows, to receive and respond to presentation requests for person identificati... | 🟡 |
| EW-PIO-01-002 | OIA_02 | A Wallet Unit SHALL support proving cryptographic device binding between the WSCA/WSCD or a keystore included in the Wallet Unit and a PID or attestation, in accordance with [SD-JWT VC] or [ISO/IEC... | 🟡 |
| EW-PIO-01-003 | OIA_03 | Empty | 🟡 |
| EW-PIO-01-004 | OIA_03a | Wallet Providers SHALL ensure that their Wallet Solution supports the protocol specified in 'OpenID for Verifiable Presentations', see [OpenID4VP], with additions and changes as documented in this ... | 🟡 |
| EW-PIO-01-005 | OIA_03b | For remote presentation flows, when the format of the requested attestation complies with [ISO/IEC 18013-5], Relying Parties and Wallet Units SHALL comply with the requirements in the profile for O... | 🟡 |
| EW-PIO-01-006 | OIA_03c | For remote presentation flows, when the format of the requested attestation complies with [SD-JWT VC], Relying Parties and Wallet Units SHALL comply with the requirements in the 'OpenID for Verifia... | 🟡 |
| EW-PIO-01-007 | OIA_04 | A Wallet Unit SHALL verify and process PID or attestation presentation requests from Relying Parties in accordance with the protocols and interfaces specified in [OpenID4VP] for remote flows. | 🟡 |
| EW-PIO-01-008 | OIA_05 | After verifying and processing a PID or attestation request, the Wallet Unit SHALL display to the User the identity of the requesting Relying Party and the requested attributes. | 🟡 |
| EW-PIO-01-009 | OIA_06 | A Wallet Unit SHALL present the requested attributes only after having received the User's authorisation. | 🟡 |
| EW-PIO-01-010 | OIA_07 | A Wallet Unit SHALL support selective disclosure of attributes from PIDs and attestations to be released to the requesting Relying Parties. | 🟡 |
| EW-PIO-01-011 | OIA_08 | Wallet Units and Relying Party Instances SHALL support the [W3C Digital Credentials API]](<https://wicg.github.io/digital-credentials/>) for remote presentation flows, provided that a) this API is ... | 🟡 |
| EW-PIO-01-012 | OIA_08a | If Wallet Units and Relying Party Instances do not support the [W3C Digital Credentials API], they SHALL implement adequate mitigations for the challenges described in [Section 4.4.3.1](../../archi... | 🟡 |
| EW-PIO-01-013 | OIA_08b | If a Wallet Unit supports the [W3C Digital Credentials API], it SHALL, by default (see OIA_08d), disclose the presence of all stored attestations (mean their attestation type) to the Digital Creden... | 🟡 |
| EW-PIO-01-014 | OIA_08c | If a Relying Party supports the [W3C Digital Credentials API], the Relying Party's presentation request MAY be processed by the browser and/or the operating system for searching available attestati... | 🟡 |
| EW-PIO-01-015 | OIA_08d | If a Wallet Unit supports the [W3C Digital Credentials API], it SHALL provide a global User setting to disable the disclosure of stored attestations via the Digital Credentials API framework, as de... | 🟡 |
| EW-PIO-01-016 | OIA_08e | If a Wallet Unit supports the [W3C Digital Credentials API], it SHALL use the CTAP-Hybrid flow only if the expectations outlined in Chapter 4 of the [Topic F discussion paper](../../discussion-topi... | 🟡 |
| EW-PIO-01-017 | OIA_09 | For remote presentation flows the Wallet Unit SHALL ensure that the attributes included in the presented attestation are accessible only to the Relying Party Instance, by encrypting the presentatio... | 🟡 |
| EW-PIO-01-018 | OIA_10 | For both proximity and remote presentation flows, if a Wallet Unit contains two PIDs having the same encoding (e.g. ISO/IEC 18013-5 or SD-JWT VC-compliant) and a Relying Party requests a PID, the W... | 🟡 |
| EW-PIO-01-019 | OIA_11 | For both proximity and remote presentation flows, if a Wallet Unit contains two attestations having the same encoding (e.g. ISO/IEC 18013-5 or SD-JWT VC-compliant) and the same attestation type, an... | 🟡 |
| EW-PIO-01-021 | OIA_13 | For both proximity and remote presentation flows, a Relying Party SHALL validate the qualified signature of a QEAA in accordance with Art.32 of the [European Digital Identity Regulation]. For the v... | 🟡 |
| EW-PIO-01-022 | OIA_14 | For both proximity and remote presentation flows, a Relying Party SHALL validate the qualified signature of a PuB-EAA in accordance with [Art.32](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri... | 🟡 |
| EW-PIO-01-023 | OIA_15 | For both proximity and remote presentation flows, a Relying Party SHALL validate the signature of a non-qualified EAA using a trust anchor provided according to the mechanism(s) specified in the ap... | 🟡 |
| EW-PIO-10-001 | ISSU_01 | Wallet Providers SHALL ensure that their Wallet Solution supports the OpenID4VCI protocol specified in [OpenID4VCI], as profiled by the 'OpenID for Verifiable Credential Issuance' profile specified... | 🟡 |
| EW-PIO-24-001 | ProxId_01 | To enable identification using proximity flows, Wallet Units SHALL support device retrieval as specified in ISO/IEC 18013-5 for presenting PID or attestation attributes. Wallet Units SHALL comply w... | 🟡 |
| EW-PIO-24-002 | ProxId_01a | If a Relying Party supports using proximity flows, its Relying Party Instances SHALL support device retrieval as specified in ISO/IEC 18013-5 for requesting PID or attestation attributes. Such Rely... | 🟡 |
| EW-PIO-24-003 | ProxId_02 | Wallet Units, PID Providers, Attestation Providers, Wallet Providers, and Relying Parties SHALL NOT support server retrieval as specified in ISO/IEC 18013-5 for requesting and presenting PID or att... | 🟡 |
| EW-PIO-24-004 | ProxId_03 | A Wallet Unit SHALL present the presentation request and the identity of the Relying Party to the User when processing the request. | 🟡 |
| EW-PIO-24-005 | ProxId_04 | A Wallet Unit SHALL request its User to approve the presentation of attributes from their Wallet Unit for proximity identification before presenting them to the Relying Party. | 🟡 |
| EW-PIO-24-006 | ProxId_05 | A Wallet Unit SHALL transmit the requested User attributes to the requesting Relying Party Instance securely in accordance with ISO/IEC 18013-5 for proximity flows. | 🟡 |
| EW-PIO-24-007 | ProxId_06 | Empty | 🟡 |
| EW-PIO-29-001 | RP_02 | An Attestation Provider issuing representation attestations to a natural person representing another natural person SHALL ensure that either the attestations are short-lived or that all entities wh... | 🟡 |
| EW-PIO-30-001 | W2W_08 | A Verifier Wallet Unit and a Holder Wallet Unit SHALL support attestation presentation only in proximity, meaning they SHALL support only [ISO/IEC 18013-5] to communicate. | 🟡 |
| EW-PIO-43-001 | EDP_09 | An Attestation Provider SHALL include an embedded disclosure policy (if any) by value in the Issuer metadata related to the attestation, in compliance with the [OpenID4VCI] issuance protocol or an ... | 🟡 |
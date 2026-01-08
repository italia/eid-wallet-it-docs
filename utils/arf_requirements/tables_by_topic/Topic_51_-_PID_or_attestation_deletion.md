# Topic 51 - PID or attestation deletion

| **Requirement ID** | **Legacy ID** | **Description** | **Status** |
|-------------------|---------------|------------------|------------|
| PAD_01 |  | A Wallet Unit SHALL at any time enable the User to delete any PID or attestation from their Wallet Unit. | 🟡 |
| PAD_02 |  | If the User indicates that a PID or attestation must be deleted, and the Wallet Unit contains multiple PIDs or attestation having the corresponding attestation type and Provider, a Wallet Unit SHAL... | 🟡 |
| PAD_03 |  | If the Wallet Unit deletes a PID or attestation on the User's request, the Wallet Unit SHALL NOT notify the respective PID Provider or Attestation Provider. *Note: This is a matter of User privacy. | 🟡 |
| PAD_04 |  | If the Wallet Unit deletes a PID or device-bound attestation on the User's request, the Wallet Unit SHALL ensure that all cryptographic assets in the WSCA/WSCD related to this PID, or in a keystore... | 🟡 |
| PAD_05 |  | If a Wallet Unit supports the [W3C Digital Credentials API] and it deletes, on the User's request, a PID or attestation previously disclosed to the Digital Credentials API framework, the Wallet Ins... | 🟡 |
| PAD_06 |  | If the User uninstalls the Wallet Instance, the Wallet Instance SHALL request the associated WSCA/WSCD and keystore(s) to delete all cryptographic assets related to the Wallet Unit and to all PIDs ... | 🟡 |
| RPI_02 |  | Empty | 🟡 |
| RPI_04 |  | When registering an intermediated Relying Party, an intermediary SHALL provide legally valid evidence that this Relying Party will indeed use the services of this intermediary to interact with Wall... | 🟡 |
| RPI_05 |  | When an intermediated Relying Party asks its intermediary to request some attributes from a Wallet Unit, it SHALL specify  a) its user-friendly name, b) its unique identifier, c) the URL of its Reg... | 🟡 |
| RPI_06 |  | When requested by an intermediated Relying Party, an intermediary SHALL request a presentation of attributes from a specific Wallet Unit. In the request, the intermediary SHALL include the intermed... | 🟡 |
| RPI_06a |  | Empty | 🟡 |
| RPI_07 |  | In case a Wallet Unit receives a presentation request from an intermediary on behalf of an intermediated Relying Party, it SHALL display the names and identifiers of both the intermediary and the i... | 🟡 |
| RPI_07a |  | In case a Wallet Unit receives a presentation request from an intermediary on behalf of an intermediated Relying Party, and if the User indicated that they want to verify the information registered... | 🟡 |
| RPI_07b |  | Empty | 🟡 |
| RPI_08 |  | When a Wallet Unit presents to an intermediary any User attributes from a PID or attestation, the intermediary SHALL, after successfully carrying out the verifications in RPI_09, forward these attr... | 🟡 |
| RPI_09 |  | When a Wallet Unit presents to an intermediary any attributes from a PID or attestation, the intermediary SHALL verify the authenticity of the PID or attestation, its revocation status, device bind... | 🟡 |
| RPI_10 |  | The intermediary SHALL delete any PIDs or attestations it obtained from the Wallet Unit, including any User attributes, completely and immediately after it has sent the User attributes to the inter... | 🟡 |
| ZKP_01 |  | A ZKP scheme SHALL provide support for the following generic functions, while hiding all attributes of PIDs or attestations: (i) generation of a proof that an (some) attribute(s) having a specific ... | 🟡 |
| ZKP_02 |  | A ZKP scheme SHALL support proving possession of attestation of a given type. *Note: See section 4.1.2 and 4.1.3 of the Discussion Paper for Topic G. | 🟡 |
| ZKP_03 |  | A ZKP scheme SHOULD support the privacy-preserving binding of an attestation to a PID. In addition to the generic functions defined in ZKP_01, for this use case, a ZKP scheme SHALL provide support ... | 🟡 |
| ZKP_04 |  | A ZKP scheme SHOULD support the derivation of a verifiable User pseudonym, by combining an attribute value that is unique for the User with Relying Party-specific context (e.g., the Relying Party i... | 🟡 |
| ZKP_05 |  | A ZKP scheme SHALL be usable in both remote and proximity presentation flows. While the inclusion of ZKP will introduce computational and verification delays, these delays SHALL NOT critically unde... | 🟡 |
| ZKP_06 |  | A ZKP scheme SHOULD be able to generate proofs for already issued PIDs and attestations in the formats specified in [ISO/IEC 18013-5] or [SD-JWT VC]. | 🟡 |
| ZKP_07 |  | A ZKP scheme SHALL NOT introduce any additional communication or information that could be used to track or link User activity during, before, or after proof generation. | 🟡 |
| ZKP_08 |  | A ZKP scheme SHALL rely solely on algorithms standardised by a standardisation organisation recognised by the Commission or in a standard recognised by the Commission. | 🟡 |
| ZKP_09 |  | Use of a ZKP scheme SHALL NOT prevent the Wallet Unit's ability to provide User authentication with Level of Assurance High. | 🟡 |
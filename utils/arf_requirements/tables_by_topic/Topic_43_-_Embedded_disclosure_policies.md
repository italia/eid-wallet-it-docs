# Topic 43 - Embedded disclosure policies

| **Requirement ID** | **Legacy ID** | **Description** | **Status** |
|-------------------|---------------|------------------|------------|
| EDP_01 |  | A Wallet Unit SHALL enable an Attestation Provider to optionally express an embedded disclosure policy for a QEAA, PuB-EAA, or non-qualified EAA. *Note: The [European Digital Identity Regulation] d... | 🟡 |
| EDP_02 |  | A Wallet Unit SHALL support embedded disclosure policies implementing the 'Authorised relying parties only policy' described in Annex III of Implementing Regulation (EU) 2024/2979. If present, such... | 🟡 |
| EDP_03 |  | A Wallet Unit SHALL support embedded disclosure policies implementing the 'Specific root of trust' policy described in Annex III of Implementing Regulation (EU) 2024/2979. If present, such an embed... | 🟡 |
| EDP_04 |  | Empty | 🟡 |
| EDP_05 |  | An embedded disclosure policy SHOULD contain a link to a website of the Attestation Provider explaining the disclosure policy in layman's terms. If this is the case, the Wallet Unit SHALL display t... | 🟡 |
| EDP_06 |  | The Wallet Unit SHALL evaluate an embedded disclosure policy in conjunction with the information received from the requesting Relying Party, in order to determine if the Relying Party has permissio... | 🟡 |
| EDP_07 |  | The Wallet Unit SHALL enable the User, based on the outcome of the evaluation of the applicable embedded disclosure policy(s), to deny or allow the presentation of the requested attestation to the ... | 🟡 |
| EDP_08 |  | The Commission SHALL take measures to ensure a technical specification is created establishing common mechanisms for the specification of embedded disclosure policies by Attestation Providers, and ... | 🟡 |
| EDP_09 |  | An Attestation Provider SHALL include an embedded disclosure policy (if any) by value in the Issuer metadata related to the attestation, in compliance with the [OpenID4VCI] issuance protocol or an ... | 🟡 |
| EDP_10 |  | During attestation issuance, a Wallet Unit SHALL retrieve and store locally the corresponding embedded disclosure policy, if any. | 🟡 |
| EDP_11 |  | An Attestation Provider SHALL revoke an attestation if a corresponding embedded disclosure policy is added, changed, or deleted. | 🟡 |
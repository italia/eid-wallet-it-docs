# Topic 7 - Attestation revocation and revocation checking

| **Requirement ID** | **Legacy ID** | **Description** | **Status** |
|-------------------|---------------|------------------|------------|
| VCR_01 |  | A PID Provider, QEAA Provider, or PuB-EAA Provider SHALL use one of the following methods for revocation of a PID, QEAA, or PuB-EAA: - Only issue short-lived attestations having a validity period o... | 🟡 |
| VCR_01a |  | A Wallet Provider SHALL use either the second or the third of the methods specified in VCR_01 for revocation of a WUA. *Note: Due to requirement WUA_08 in [Topic 9](./annex-2.02-high-level-requirem... | 🟡 |
| VCR_02 |  | For non-qualified EAAs, the relevant Rulebook SHALL specify whether that type of EAA must be revocable. If a non-qualified EAA type must be revocable, the relevant Rulebook SHALL determine which of... | 🟡 |
| VCR_03 |  | If a PID or attestation is revocable, the PID Provider of a given PID, or the Attestation Provider of a given attestation, SHALL be the only party in the EUDI Wallet ecosystem responsible for execu... | 🟡 |
| VCR_03a |  | The Wallet Provider of a given WUA SHALL be the only party in the EUDI Wallet ecosystem responsible for executing the revocation of that WUA. *Note: A Wallet Provider MAY outsource the operation of... | 🟡 |
| VCR_04 |  | A PID Provider, Attestation Provider or Wallet Provider that revoked a PID, attestation, or WUA SHALL NOT reverse the revocation. | 🟡 |
| VCR_05 |  | If a PID, attestation, or WUA is revocable, the PID Provider, Attestation Provider, or Wallet Provider SHALL have a policy specifying under which conditions a PID, attestation, or WUA it issued wil... | 🟡 |
| VCR_06 |  | If a PID, attestation, or WUA is revocable, the PID Provider, Attestation Provider, or Wallet Provider SHALL revoke a PID, attestation, or WUA when its security has been compromised. | 🟡 |
| VCR_07 |  | A Wallet Provider SHALL revoke all valid WUAs issued to a Wallet Unit upon the explicit request of the User to revoke their Wallet Unit. | 🟡 |
| VCR_07a |  | If a PID or attestation is revocable, the PID Provider or Attestation Provider SHOULD revoke that PID or attestation upon the explicit request of the User to whom the PID or the attestation was iss... | 🟡 |
| VCR_07b |  | If a PID or attestation is revocable, the PID Provider or Attestation Provider SHOULD revoke that PID if the Wallet Unit on which it resides is revoked, in compliance with requirement WURevocation_... | 🟡 |
| VCR_08 |  | If a PID is revocable, the PID Provider SHALL revoke a PID upon the death of the natural person who is the subject of the PID, or the cease of activity of the legal person who is the subject of the... | 🟡 |
| VCR_09 |  | If a PID, attestation, or WUA is revocable, the PID Provider, Attestation Provider or Wallet Provider SHALL revoke a PID, attestation, or WUA if the value of one or more attributes in the PID, atte... | 🟡 |
| VCR_10 |  | Wallet Providers SHALL implement the attestation revocation mechanisms specified per VCR_11 in their Wallet Solutions. | 🟡 |
| VCR_11 |  | The Commission SHALL create or reference technical specifications providing all necessary details for PID Providers, Attestation Providers, and Wallet Providers to implement an Attestation Status L... | 🟡 |
| VCR_12 |  | If a Relying Party decides it needs to be able to verify the revocation status of PIDs or attestations, it SHALL support both the Attestation Status List mechanism and the Attestation Revocation Li... | 🟡 |
| VCR_12a |  | A PID Provider or Attestation Provider SHALL support both the Attestation Status List mechanism and the Attestation Revocation List mechanism specified per VCR_11 for verifying the revocation statu... | 🟡 |
| VCR_13 |  | A Relying Party Instance SHOULD verify the revocation status of a PID or attestation upon obtaining it from a Wallet Unit, following the steps specified per VCR_11. | 🟡 |
| VCR_14 |  | When no reliable information regarding the revocation status of a PID or attestation is available, a Relying Party SHOULD perform a risk analysis considering all relevant factors for the use case, ... | 🟡 |
| VCR_15 |  | A Relying Party Instance SHOULD NOT request the relevant Attestation Status List or Attestation Revocation List each time an attestation is presented to it by a Wallet Unit. Rather, the Relying Par... | 🟡 |
| VCR_16 |  | A PID Provider, Attestation Provider or Wallet Provider SHALL NOT require the Relying Party or Relying Party Instance to authenticate itself before downloading an Attestation Status List or Attesta... | 🟡 |
| VCR_17 |  | When using an Attestation Status List for revocation, the PID Provider, Attestation Provider or Wallet Provider SHALL randomly assign the index for each PID or attestation, to prevent this index fr... | 🟡 |
| VCR_18 |  | When using an Attestation Status List for revocation, the PID Provider, Attestation Provider, or Wallet Provider SHALL represent a sufficiently large number of PIDs, attestations, or WUAs on each A... | 🟡 |
| VCR_19 |  | A Wallet Unit SHOULD regularly check the revocation status of its PIDs, attestations, and WUAs, and notify the User if a PID, attestation, or WUA (i.e, the Wallet Unit itself), is revoked. | 🟡 |
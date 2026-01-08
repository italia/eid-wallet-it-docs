# Preview: Issue #681 - ✅ ARF HLR REV: Topic 7 - Attestation revocation and revocation checking

**Topic:** Topic 7 - Attestation revocation and revocation checking

**Requirements ARF 2.5.0:** 22
**Requirements ARF 2.7.3:** 22

---

## Diff ARF 2.5.0 → ARF 2.7.3

### ℹ️ No changes detected

The requirements are identical between ARF 2.5.0 and ARF 2.7.3.

**Total requirements ARF 2.7.3:** 22
**Total requirements ARF 2.5.0:** 22
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

---| Status

## Diff ARF 2.5.0 → ARF 2.7.3

### ℹ️ No changes detected

The requirements are identical between ARF 2.5.0 and ARF 2.7.3.


| Status | **Index** | **Requirement specification** | IT-Wallet Mapping & Documentation |
|---|---------|------------------|-----------------------------------|
| 🟡 | VCR_01 | A PID Provider, QEAA Provider, or PuB-EAA Provider SHALL use one of the following methods for revocation of a PID, QEAA, or PuB-EAA: - Only issue short-lived attestations having a validity period of 24 hours or less, such that revocation will never be necessary, - Use an Attestation Status List mechanism specified per VCR_11, or - Use an Attestation Revocation List mechanism specified per VCR_11. *Note: The 24-hour period originates from ETSI EN 319 411-1 V1.4.1, requirement REV-6.2.4-03A. This requires that the process of revocation must take at most 24 hours. Consequently, revocation may make no sense if the attestation is valid for less than 24 hours, because it may reach the end of its validity period before it is revoked. |  |
| 🟡 | VCR_02 | For non-qualified EAAs, the relevant Rulebook SHALL specify whether that type of EAA must be revocable. If a non-qualified EAA type must be revocable, the relevant Rulebook SHALL determine which of the methods mentioned in VCR_01 must be implemented by the relevant EAA Providers for the revocation of such an EAA. |  |
| 🟡 | VCR_03 | If a PID or attestation is revocable, the PID Provider of a given PID, or the Attestation Provider of a given attestation, SHALL be the only party in the EUDI Wallet ecosystem responsible for executing the revocation of that PID or attestation. *Note: A PID Provider, Attestation Provider MAY outsource the operation of the revocation process to a third party. |  |
| 🟡 | VCR_03a | The Wallet Provider of a given WUA SHALL be the only party in the EUDI Wallet ecosystem responsible for executing the revocation of that WUA. *Note: A Wallet Provider MAY outsource the operation of the revocation process to a third party. |  |
| 🟡 | VCR_04 | A PID Provider, Attestation Provider or Wallet Provider that revoked a PID, attestation, or WUA SHALL NOT reverse the revocation. |  |
| 🟡 | VCR_05 | If a PID, attestation, or WUA is revocable, the PID Provider, Attestation Provider, or Wallet Provider SHALL have a policy specifying under which conditions a PID, attestation, or WUA it issued will be revoked. |  |
| 🟡 | VCR_06 | If a PID, attestation, or WUA is revocable, the PID Provider, Attestation Provider, or Wallet Provider SHALL revoke a PID, attestation, or WUA when its security has been compromised. |  |
| 🟡 | VCR_07 | A Wallet Provider SHALL revoke all valid WUAs issued to a Wallet Unit upon the explicit request of the User to revoke their Wallet Unit. |  |
| 🟡 | VCR_07a | If a PID or attestation is revocable, the PID Provider or Attestation Provider SHOULD revoke that PID or attestation upon the explicit request of the User to whom the PID or the attestation was issued. |  |
| 🟡 | VCR_08 | If a PID is revocable, the PID Provider SHALL revoke a PID upon the death of the natural person who is the subject of the PID, or the cease of activity of the legal person who is the subject of the PID. |  |
| 🟡 | VCR_09 | If a PID, attestation, or WUA is revocable, the PID Provider, Attestation Provider or Wallet Provider SHALL revoke a PID, attestation, or WUA if the value of one or more attributes in the PID, attestation, or WUA was changed (including attributes being added or deleted) and it is still valid for at least 24 hours. Subsequently, if the User's contact details are known, the PID Provider, Attestation Provider, or Wallet Provider SHOULD, via an out-of-band manner, notify the User about the revocation and ask the User to request re-issuance of the PID, attestation, or WUA using their Wallet Unit. *Note: If the value of the attributes is determined by a party different from the Provider, such as an Authentic Source, the Provider is responsible for ensuring that this third party notifies them about such changes. |  |
| 🟡 | VCR_10 | Wallet Providers SHALL implement the attestation revocation mechanisms specified per VCR_11 in their Wallet Solutions. |  |
| 🟡 | VCR_11 | The Commission SHALL create or reference technical specifications providing all necessary details for PID Providers, Attestation Providers, and Wallet Providers to implement an Attestation Status List mechanism or an Attestation Revocation List mechanism for the PIDs, attestations, and WUAs they issue. These technical specifications SHALL also contain all details necessary for Relying Party Instances, Relying Parties, and Wallet Units interacting with other Wallet Units to use these mechanisms to verify the revocation status of PIDs, attestations, and WUAs. *Note: 'Attestation Status List' and 'Attestation Revocation List' are specific mechanisms, defined in Annex 1. Attestation Revocation Lists are sometimes referred to as 'Identifier Lists'. |  |
| 🟡 | VCR_12 | If a Relying Party decides it needs to be able to verify the revocation status of PIDs or attestations, it SHALL support both the Attestation Status List mechanism and the Attestation Revocation List mechanism specified per VCR_11. *Note: Per VCR_13, it is recommended but not mandatory for a Relying Party to verify whether a PID or attestation is revoked. |  |
| 🟡 | VCR_12a | A PID Provider or Attestation Provider SHALL support both the Attestation Status List mechanism and the Attestation Revocation List mechanism specified per VCR_11 for verifying the revocation status of a WUA. |  |
| 🟡 | VCR_13 | A Relying Party Instance SHOULD verify the revocation status of a PID or attestation upon obtaining it from a Wallet Unit, following the steps specified per VCR_11. |  |
| 🟡 | VCR_14 | When no reliable information regarding the revocation status of a PID or attestation is available, a Relying Party SHOULD perform a risk analysis considering all relevant factors for the use case, before taking a decision to accept or refuse the PID or attestation. |  |
| 🟡 | VCR_15 | A Relying Party Instance SHOULD NOT request the relevant Attestation Status List or Attestation Revocation List each time an attestation is presented to it by a Wallet Unit. Rather, the Relying Party operating the Relying Party Instance SHOULD download each new version of the list once, at a time and from a location unrelated to the presentation of a PID or attestation by a User. The Relying Party SHOULD then distribute the list to all of its Relying Party Instances, using an Relying Party-internal distribution mechanism. |  |
| 🟡 | VCR_16 | A PID Provider, Attestation Provider or Wallet Provider SHALL NOT require the Relying Party or Relying Party Instance to authenticate itself before downloading an Attestation Status List or Attestation Revocation List. |  |
| 🟡 | VCR_17 | When using an Attestation Status List for revocation, the PID Provider, Attestation Provider or Wallet Provider SHALL randomly assign the index for each PID or attestation, to prevent this index from becoming a correlator. *Note: Randomly assigning indices within a bitstring or byte array is more complicated than creating random identifiers (e.g. serial numbers) for attestations, as is needed for an Attestation Revocation List. This is because duplicate indices and unnecessarily long bitstrings or byte arrays must be prevented. |  |
| 🟡 | VCR_18 | When using an Attestation Status List for revocation, the PID Provider, Attestation Provider, or Wallet Provider SHALL represent a sufficiently large number of PIDs, attestations, or WUAs on each Attestation Status List to ensure herd privacy. *Note: In this context, herd privacy means that if an entity requests a particular status list, the PID Provider, Attestation Provider, or Wallet Provider is not able to deduce which PID, attestation or WUA (likely) was presented to that entity. Complying with this requirement may be difficult in case the number of PIDs, attestations, or WUAs to be represented on the list is small. In such a case, decoy entries can be added to the list to obfuscate the real number of referenced PIDs, attestations, or WUAs. |  |
| 🟡 | VCR_19 | A Wallet Unit SHOULD regularly check the revocation status of its PIDs, attestations, and WUAs, and notify the User if a PID, attestation, or WUA (i.e, the Wallet Unit itself), is revoked. |  |

---

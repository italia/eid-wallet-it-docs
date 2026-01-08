# Preview: Issue #687 - ✅⚠️ ARF HLR INT: Topic 18 - Combined presentations of attributes

**Topic:** Topic 18 - Combined presentations of attributes

**Requirements ARF 2.5.0:** 6
**Requirements ARF 2.7.3:** 6

---

## Diff ARF 2.5.0 → ARF 2.7.3

### ℹ️ No changes detected

The requirements are identical between ARF 2.5.0 and ARF 2.7.3.

**Total requirements ARF 2.7.3:** 6
**Total requirements ARF 2.5.0:** 6
---

## Nuovo body completo della issue:

**ARF VERSION:**  
UPDATED TO ARF 2.7.3.

Please refer to the "Summary of Changes" section and subsequent sections to see what has changed from ARF 2.5.0 to ARF 2.7.3.

---

Legend:
- ~~Strikethrough text~~ = Removed or modified content
- **Bold text [NEW]** = New or added content
- **Bold text [MODIFIED]** = Modified content| Status

## Diff ARF 2.5.0 → ARF 2.7.3

### ℹ️ No changes detected

The requirements are identical between ARF 2.5.0 and ARF 2.7.3.


| Status | **ID** | **Requirement specification** | **IT-Wallet Mapping & Documentation** |
|---|---------|------------------|-----------------------------------|
| 🟡 | ACP_01 | A Cryptographic Binding of Attestations scheme SHALL enable a WSCA/WSCD to prove that it manages two or more private keys, paired with two or more public keys provided to it by the Wallet Unit. *Note: a)These public keys may be included in WUAs, PIDs, attestations, or pseudonyms. b) The proof may be transitive, so a proof that two keys are stored/managed in the same WSCA/WSCD may be done by proving these keys relate to each other via a third key (also stored in the WSCA/WSCD). |  |
| 🟡 | ACP_02 | A Cryptographic Binding of Attestations scheme SHALL rely solely on algorithms standardised by a standardisation organisation recognised by the Commission or in a standard recognised by the Commission. |  |
| 🟡 | ACP_03 | A Cryptographic Binding of Attestations scheme SHOULD be implemented using a Zero-Knowledge Proof mechanism that satisfies the requirements specified in [Topic 53](./annex-2.02-high-level-requirements-by-topic.md#a2331-topic-53-zero-knowledge-proofs). |  |
| 🟡 | ACP_05 | A Cryptographic Binding of Attestations scheme SHALL enable an Attestation Provider, during the issuance of an attestation, to request and obtain proof that the private key for the new attestation is managed by the same WSCA/WSCD as the private key of a PID or another attestation already existing on the Wallet Unit. *Note: ACP_05 and ACP_06 may require an addition to the common OpenID4VCI protocol referenced in requirement ISSU_01, or an extension or profile thereof. |  |
| 🟡 | ACP_06 | A Cryptographic Binding of Attestations scheme SHALL enable a PID Provider or Attestation Provider, during the issuance of a PID or attestation, to request and obtain proof that the private key for the new PID or attestation is managed by the same WSCA/WSCD as the private key of the WUA received. |  |
| 🟡 | ACP_07 | Before making a request according to ACP_05, an Attestation Provider SHALL verify that the new attestation indeed belongs to the User of the existing PID or attestation. |  |

---

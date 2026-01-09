# Preview: Issue #777 - ARF HLR Topic 28 - Wallet Unit for legal persons

**Topic:** Topic 28 - Wallet Unit for legal persons

**Requirements ARF 2.5.0:** 1
**Requirements ARF 2.7.3:** 3

---

## Diff ARF 2.5.0 → ARF 2.7.3

### ✅ Requirements added in ARF 2.7.3 (2):

- **LP_02**: The attestation type of a legal-person PID SHALL be different from the attestation type of a natural person PID. *Note: See [[Topic 12](./annex-2.02-high-level-requirements-by-topic.md#a239-topic-12---attestation-rulebooks)] for an explanation of the concept of attestation type.
- **LP_03**: A legal-person PID SHALL comply with all requirements in the Legal-person PID Rulebook mentioned in LP_01.

**Total requirements ARF 2.7.3:** 3
**Total requirements ARF 2.5.0:** 1
---

## Nuovo body completo della issue:

**ARF VERSION:**  
UPDATED TO ARF 2.7.3.

Please refer to the "Summary of Changes" section and subsequent sections to see what has changed from ARF 2.5.0 to ARF 2.7.3.

---

## HLRs

## Diff ARF 2.5.0 → ARF 2.7.3

### ✅ Requirements added in ARF 2.7.3 (2):

- **LP_02**: The attestation type of a legal-person PID SHALL be different from the attestation type of a natural person PID. *Note: See [[Topic 12](./annex-2.02-high-level-requirements-by-topic.md#a239-topic-12---attestation-rulebooks)] for an explanation of the concept of attestation type.
- **LP_03**: A legal-person PID SHALL comply with all requirements in the Legal-person PID Rulebook mentioned in LP_01.


| Status | **Index** | **Requirement specification** | **IT-Wallet Mapping & Documentation** |
|---|---------|------------------|-----------------------------------|
| 🟡 | LP_01 | The Commission SHALL develop a Legal-person PID Rulebook to specify the attestation scheme and other technical details applicable for legal-person PIDs. | Pending: Not yet established, planned at EU level. |
| 🟡 | LP_02 | The attestation type of a legal-person PID SHALL be different from the attestation type of a natural person PID. *Note: See [[Topic 12](./annex-2.02-high-level-requirements-by-topic.md#a239-topic-12---attestation-rulebooks)] for an explanation of the concept of attestation type. |  |
| 🟡 | LP_03 | A legal-person PID SHALL comply with all requirements in the Legal-person PID Rulebook mentioned in LP_01. | Pending: Not yet established, planned at EU level. |**LP_02**: Legal-person PID SHALL have different attestation type from natural person PID
- Ensures distinction between legal and natural person PIDs
- References Topic 12 for attestation type explanation

**LP_03**: Legal-person PIDs SHALL comply with Legal-person PID Rulebook
- **Note**: Contains reference inconsistency - states "mentioned in LP_02" but should reference "LP_01" where the Rulebook is introduced

### Related Topics:

- **Topic 12** (Attestation Rulebooks): Framework for Legal-person PID Rulebook
- **Topic 19** (Dashboard): DASH_11 references legal person Wallet Unit interfaces
- **Topic 27** (Registration): Registration processes apply to legal person entities

### Overall Assessment:

Topic 28 contains 3 foundational requirements that establish the framework for legal person PIDs. All technical details are delegated to the Legal-person PID Rulebook to be developed by the Commission. The topic distinguishes legal person identity from natural person identity but does not yet specify attribute schemas, issuance processes, or delegation mechanisms.

All requirements are assigned to 🟡 status

---

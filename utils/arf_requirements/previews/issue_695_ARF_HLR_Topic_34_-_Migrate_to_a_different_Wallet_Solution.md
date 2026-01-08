# Preview: Issue #695 - 🟧🟡 ARF HLR Topic 34 - Migrate to a different Wallet Solution

**Topic:** Topic 34 - Migrate to a different Wallet Solution

**Requirements ARF 2.5.0:** 18
**Requirements ARF 2.7.3:** 18

---

## Diff ARF 2.5.0 → ARF 2.7.3

### ℹ️ No changes detected

The requirements are identical between ARF 2.5.0 and ARF 2.7.3.

**Total requirements ARF 2.7.3:** 18
**Total requirements ARF 2.5.0:** 18
---

## Nuovo body completo della issue:

# Topic 34 - Migration and Backup (Mig) - Changelog

**ARF VERSION:**  
UPDATED TO ARF 2.7.3.

### No Substantive Changes

---

## A. Back-up requirements


### 🔄 Requirements modified in ARF 2.7.3 (9):

- **Mig_07**:
  - **Old:** ...attestation listed in the Migration Object, the Wallet Unit SHALL enable the User to select that PID or attestation. When selected, the Wallet Unit SH......
  - **New:** ...device-bound attestation listed in the Migration Object, the Wallet Unit SHALL enable the User to select that PID or attestation. When a PID or device......
- **Mig_08**:
  - **Old:** ~~Empty~~ **Empty [NO CHANGE]
  - **New:** Empty
- **Mig_09**:
  - **Old:** ~~Empty~~ **Empty [NO CHANGE]
  - **New:** Empty
- **Mig_10**:
  - **Old:** ~~Empty~~ **Empty [NO CHANGE]
  - **New:** Empty
- **Mig_12**:
  - **Old:** ~~Empty~~ **Empty [NO CHANGE]
  - **New:** Empty
- **Mig_13**:
  - **Old:** ~~Empty~~ **Empty [NO CHANGE]
  - **New:** Empty
- **Mig_14**:
  - **Old:** ~~Empty~~ **Empty [NO CHANGE]
  - **New:** Empty
- **Mig_15**:
  - **Old:** ~~Empty~~ **Empty [NO CHANGE]
  - **New:** Empty
- **Mig_16**:
  - **Old:** ~~Empty~~ **Empty [NO CHANGE]
  - **New:** Empty

## Diff ARF 2.5.0 → ARF 2.7.3

### ℹ️ No changes detected

The requirements are identical between ARF 2.5.0 and ARF 2.7.3.


| Status | **Index** | **Requirement specification** | **IT-Wallet Mapping & Documentation** |
|---|---------|------------------|-----------------------------------|
| 🟡 | Mig_01 | A Wallet Unit SHALL include and keep up-to-date a Migration Object, containing the following information: - The contents of the log for all transactions executed through the Wallet Unit, as listed in requirement DASH_02. - A list of PIDs and attestations, except Wallet Unit Attestations, present in the Wallet Unit, according to the requirements in this Topic. | Pending: Not yet established, planned at EU level. |
| 🟡 | Mig_02 | The Migration Object SHALL comply with all requirements in [Technical Specification 10](../../technical-specifications/ts10-data-portability-and-download-(export).md). | Pending: Not yet established, planned at EU level. |
| 🟡 | Mig_03 | For each PID or device-bound attestation that is issued to it, a Wallet Unit SHALL add to the Migration Object all data necessary to request issuance of that PID or attestation once again. This SHALL include at least the attestation type and the PID Provider or Attestation Provider that issued the PID or attestation, as well as their service supply points. However, the Migration Object SHALL NOT contain attribute identifiers or attribute values, and SHALL NOT contain any private keys of the PID or device-bound attestation. |  |
| 🟡 | Mig_03a | For each non-device bound attestation that is issued to it, a Wallet Unit SHALL add to the Migration Object one of the following: either all data necessary to request issuance of that attestation once again, as listed in Mig_03, or all data necessary to transfer the attestation to a new device without involvement of the Attestation Provider, including attribute identifiers and attribute values. The Wallet Unit SHALL enable the User to indicate if they want to store attribute identifiers and values in the Migration Object. | Pending: Not yet established, planned at EU level. |
| 🟡 | Mig_03b | If the User deletes a PID or attestation from their Wallet Unit, the Wallet Unit SHALL delete the corresponding entry from the Migration Object. |  |
| 🟡 | Mig_04 | The Wallet Unit SHALL store the Migration Object in an external storage or remote storage location of the User's choice, from among the storage options supported by the Wallet Unit, in such a way that the User can still retrieve the object from a new Wallet Unit in case the existing Wallet Unit becomes unavailable. *Note: a) It is up to the Wallet Provider to decide which external storage options or remote storage locations the Wallet Unit supports for storing the Migration Object. b) The new Wallet Unit may be either an instance of the same Wallet Solution as the old one, or an instance of a different Wallet Solution. |  |
| 🟡 | Mig_05 | The Wallet Unit SHALL store the Migration Object in such a way that its confidentiality, integrity, and authenticity is protected and that it is protected against use by others than the User. *Note: This could be done, for example, by using password-based cryptography to encrypt the object. |  |
| 🟡 | Mig_06 | Directly after installation of a new Wallet Instance, the Wallet Instance SHALL enable the User to import a Migration Object from an external storage or remote storage location indicated by the User, from among the storage options supported by the Wallet Unit. |  |
| 🟡 | Mig_07 | When importing a Migration Object, for each PID and device-bound attestation listed in the Migration Object, the Wallet Unit SHALL enable the User to select that PID or attestation. When a PID or device-bound attestation is selected, the Wallet Unit SHALL request the respective PID Provider or Attestation Provider to re-issue that PID or attestation. If the User selects a PID, the PID SHALL be the first to be restored. |  |
| 🟡 | Mig_07a | When importing a Migration Object, for each non device-bound attestation listed in the Migration Object, the Wallet Unit SHALL enable the User to select that attestation. When an attestation is selected, the Wallet Unit SHALL, depending on whether the Migration Object contains attribute identifiers and attribute values (see Mig_03a), either restore the attestation or request the respective Attestation Provider to re-issue it. |  |
| 🟡 | Mig_08 | Empty |  |
| 🟡 | Mig_09 | Empty |  |
| 🟡 | Mig_10 | Empty |  |
| 🟡 | Mig_12 | Empty |  |
| 🟡 | Mig_13 | Empty |  |
| 🟡 | Mig_14 | Empty |  |
| 🟡 | Mig_15 | Empty |  |
| 🟡 | Mig_16 | Empty |  |
## Summary of Changes

### No Substantive Changes

**All Mig requirements remain completely unchanged** between versions. 

### Related Topics:

- **Topic 10** (Issuance): Migration uses same issuance processes
- **Topic 19** (Dashboard): Transaction logs included in Migration Object (DASH_02)
- **Topic 38** (WUA Revocation): WUAs excluded from Migration Object

### Overall Assessment:

Topic 34 maintains complete stability with well-defined backup and restore mechanisms. The framework enables:
- **Device migration**: Move to new device (same or different Wallet Solution)
- **Disaster recovery**: Restore after device loss
- **Privacy preservation**: No sensitive data in backup
- **User empowerment**: User controls storage and restoration

All requirements remain assigned to Commission (technical specs) or Wallet Units (implementation), with no changes in this version. The numerous empty placeholders (9 out of 16 requirements) suggest potential for future expansion of migration functionality.

---

# Preview: Issue #721 - ARF HLR Topic 48 - Blueprint for requesting data deletion to Relying Parties

**Topic:** Topic 48 - Blueprint for requesting data deletion to Relying Parties

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

# Topic 48 - Data Deletion Requests (DATA_DLT) - Changelog

**ARF VERSION:**  
UPDATED TO ARF 2.7.3.

Please refer to the "Summary of Changes" section and subsequent sections to see what has changed from ARF 2.5.0 to ARF 2.7.3.

---

Legend:
- ~~Strikethrough text~~ = Removed or modified content
- **Bold text [NEW]** = New or added content
- **Bold text [MODIFIED]** = Modified content

---

## HLRs


### ✅ Requirements added in ARF 2.7.3 (1):

- **DATA_DLT_08**: Wallet Units, Relying Parties, and Registrars SHALL comply with the relevant requirements in [Technical Specification 7](../../technical-specifications/ts7-common-interface-for-data-deletion-request.md).

## Diff ARF 2.5.0 → ARF 2.7.3

### ℹ️ No changes detected

The requirements are identical between ARF 2.5.0 and ARF 2.7.3.


| Status | **ID** | **Requirement specification** | **IT-Wallet Mapping & Documentation** |
|---|---------|------------------|-----------------------------------|
| 🟧 | DATA_DLT_01 | A Wallet Provider SHALL ensure that its Wallet Units support the possibilities mentioned in DATA_DLT_02, allowing a User to request from a Relying Party the erasure of their attributes that were presented by that Wallet Unit to that Relying Party, in accordance with Article 17 of Regulation (EU) 2016/679. |  |
| 🟧 | DATA_DLT_03 | A Wallet Instance SHALL provide a function where the User may select one Relying Party to which a data deletion request must be submitted. |  |
| 🟧 | DATA_DLT_04 | Empty |  |
| 🟧 | DATA_DLT_06 | For the initiation of a data deletion request, the log SHALL contain at least: - Date and time of the initiation of the request, - Name and unique identifier of the Relying Party to which the request was made, - Attributes requested to be deleted. |  |
| 🟧 | DATA_DLT_07 | Before executing a data deletion request, a Relying Party SHALL authenticate the requesting User (or the request itself), using appropriate authentication mechanisms of its own choosing. The Relying Party SHOULD use the authentication or signature facilities offered by the User's Wallet Unit for this purpose. |  |
| 🟡 | DATA_DLT_08 | Wallet Units, Relying Parties, and Registrars SHALL comply with the relevant requirements in [Technical Specification 7](../../technical-specifications/ts7-common-interface-for-data-deletion-request.md). |  |1. **Terminology consistency**: All references changed from "attribute erasure" to "data erasure/deletion"
2. **Reference updates**: Updated cross-references to Topic 44 requirements (RPRC_04-06b → RPRC_16-18)
3. **Topic 44 title updated**: Full title now includes all entity types in reference
4. **No substantive changes**: All functional requirements remain identical

### Changes by Requirement

- **DATA_DLT_02a**: Updated Topic 44 cross-reference from "RPRC_04 - RPRC_06b" to "RPRC_16 - RPRC_18" (due to Topic 44 renumbering), and full Topic 44 title updated
- **All other requirements**: No changes

## Overall Assessment

Topic 48 shows **minimal changes** with the primary update being cross-reference adjustments to reflect Topic 44's reorganization. The data deletion request framework remains stable and fully functional:

**Framework components:**
- User-initiated deletion requests (GDPR Article 17 compliance)
- Multiple contact methods (web form, email, phone)
- Fallback to Registrar lookup when contact info missing
- Logging of deletion request initiations
- RP authentication requirements

**Key requirement**: DATA_DLT_02a now correctly references RPRC_16-18 (instead of old RPRC_04-06b) for registration certificate verification requirements, maintaining proper cross-topic alignment after Topic 44's restructuring.

All requirements remain assigned to Wallet Providers/Units and Relying Parties (🟧 status).

---

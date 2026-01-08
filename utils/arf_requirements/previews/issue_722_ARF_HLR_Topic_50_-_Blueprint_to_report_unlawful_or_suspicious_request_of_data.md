# Preview: Issue #722 - ARF HLR Topic 50 - Blueprint to report unlawful or suspicious request of data

**Topic:** Topic 50 - Blueprint to report unlawful or suspicious request of data

**Requirements ARF 2.5.0:** 5
**Requirements ARF 2.7.3:** 5

---

## Diff ARF 2.5.0 → ARF 2.7.3

### ℹ️ No changes detected

The requirements are identical between ARF 2.5.0 and ARF 2.7.3.

**Total requirements ARF 2.7.3:** 5
**Total requirements ARF 2.5.0:** 5
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

---

## HLRs

## Diff ARF 2.5.0 → ARF 2.7.3

### ℹ️ No changes detected

The requirements are identical between ARF 2.5.0 and ARF 2.7.3.


| Status | **ID** | **Requirement specification** | **IT-Wallet Mapping & Documentation** |
|---|---------|------------------|-----------------------------------|
| 🟧 | RPT_DPA_02a | A Wallet Unit SHALL support at least the following possibilities to report a suspicious presentation request to a DPA, depending on what contact details are available for the DPA: a) Open a URL in an external browser to report the request in a web form provided by the DPA. b) Open an external e-mail client and start a draft e-mail to the DPA, with a suitable template text, c) open an external phone client and start a phone call. |  |
| 🟡 | RPT_DPA_03 | Empty |  |
| 🟧 | RPT_DPA_04 | A Wallet Provider SHALL ensure that a Wallet Unit allows its User to substantiate a report sent to a DPA, including by attaching relevant information to identify the Relying Party and the Users' claims in a machine-readable format. *Note: The log kept by the Wallet Unit will be standardized and is machine-readable in order to enable data portability. An excerpt from this log therefore can be used to substantiate the report. |  |
| 🟡 | RPT_DPA_05a | For a report sent to a DPA, the log SHALL contain at least: a) the date and time when the report was sent, b) the name and country of the DPA, and c) the channel and contact information used for initiating sending the report, i.e., the URL, e-mail address, or phone number of the DPA. |  |
| 🟧 | RPT_DPA_06 | Wallet Units, Data Protection Authorities, and Registrars SHALL comply with the relevant requirements in [Technical Specification 8](../../technical-specifications/ts8-common-interface-for-reporting-of-wrp-to-dpa.md). |  |1. **RPT_DPA_01**: Updated Topic 44 cross-reference from "RPRC_04 - RPRC_06b" to "RPRC_16 - RPRC_18" and updated Topic 44 title
2. **RPT_DPA_03**: Removed (was "?")
3. **RPT_DPA_05**: Split into two requirements (RPT_DPA_05 and RPT_DPA_05a)
   - RPT_DPA_05: General logging requirement
   - RPT_DPA_05a: **NEW** - Specific log contents requirement

### Changes by Requirement

- **RPT_DPA_01**: Cross-reference updated for Topic 44 renumbering
- **RPT_DPA_02, 02a, 04**: No changes
- **RPT_DPA_03**: Removed (was empty placeholder)
- **RPT_DPA_05**: Modified and split - now focuses on general logging requirement
- **RPT_DPA_05a**: **NEW** - Details what must be in the log
- **RPT_DPA_06**: No changes

## Detailed Analysis of Changes

### RPT_DPA_01 - Cross-reference Update

**Change type**: Reference update due to Topic 44 renumbering

The note now correctly references:
- **Old**: "See RPRC_04 - RPRC_06b in Topic 44"
- **New**: "See RPRC_16 - RPRC_18 in Topic 44"

This aligns with Topic 44's restructuring where registration certificate verification requirements were renumbered.

### RPT_DPA_03 - Removed

**Change type**: Removal of empty placeholder

The requirement was just "?" and has been removed, cleaning up the specification.

### RPT_DPA_05 - Split and Enhanced

**Change type**: Requirement split for clarity

**Old RPT_DPA_05**:
- Single requirement covering logging "reports sent to the DPA"
- Vague about what should be logged

**New RPT_DPA_05**:
- Clarifies it logs "the fact that it initiated the sending"
- Emphasizes it's about initiation (since actual sending happens via external apps)
- References RPT_DPA_02a for context
- More explicit Topic 19 reference

**New RPT_DPA_05a**:
- Completely new requirement
- Specifies exactly what must be in the log:
  - Date and time of transaction
  - Name and country of DPA
  - Channel and contact info (URL/email/phone)
- Provides clear implementation guidance

This split improves clarity by separating "what to log" (RPT_DPA_05) from "what the log must contain" (RPT_DPA_05a), parallel to similar patterns in other topics.

---

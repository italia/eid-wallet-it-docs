# Preview: Issue #690 - 🟡 ARF HLR Topic 25 - Unified definition and controlled vocabularies for attributes

**Topic:** Topic 25 - Unified definition and controlled vocabularies for attributes

**Requirements ARF 2.5.0:** 7
**Requirements ARF 2.7.3:** 7

---

## Diff ARF 2.5.0 → ARF 2.7.3

### ℹ️ No changes detected

The requirements are identical between ARF 2.5.0 and ARF 2.7.3.

**Total requirements ARF 2.7.3:** 7
**Total requirements ARF 2.5.0:** 7
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


| Status | **Index** | **Requirement specification** | **IT-Wallet Mapping & Documentation** |
|---|---------|------------------|-----------------------------------|
| 🟡 | CAT_01 | Empty | Pending: Not yet established, planned at EU level. |
| 🟡 | CAT_01a | Empty | Pending: Not yet established, planned at EU level. |
| 🟡 | CAT_01b | Empty | Pending: Not yet established, planned at EU level. |
| 🟡 | CAT_02 | Empty |  |
| 🟡 | CAT_03 | Empty | Pending: Not yet established, planned at EU level. |
| 🟡 | CAT_03b | Empty | DE4A](https://www.de4a.eu/semper), - [SEMIC Core Vocabularies](https://interoperable-europe.ec.europa.eu/collection/semic-support-centre/core-vocabularies#What%20are%20the%20Core%20Vocabularies), - [IANA Registry for JSON Web Token Claims](https://www.iana.org/assignments/jwt/jwt.xhtml) (for JSON-based attributes only), - [ISO/IEC 23220-2](https://www.iso.org/standard/86782.html) (for CBOR-based attributes only). |
| 🟡 | CAT_04 | A request to include or to modify an attribute in the catalogue of attributes SHALL indicate how a QTSP can use the verification point for that attribute. *Note: This could be, for instance, in the form of (a reference to) an endpoint description text. | Pending: Not yet established, planned at EU level. |**CAT_01**: Added note on catalogue architecture:
- **NEW NOTE**: "The catalogue of attributes does not need to be a separate catalogue, but could be combined with the Attestation Rulebooks catalogue mentioned in CAT_05."
- **Purpose**: Provides flexibility in implementation by clarifying that a single combined catalogue is acceptable

**CAT_03**: Added note on availability requirements:
- **NEW NOTE**: "The requirement for availability implies setting up the required means for high availability and avoiding a single point of failure."
- **Purpose**: Clarifies that "publicly available and machine-readable" means robust, reliable infrastructure with redundancy

**CAT_04**: Added note on maintenance scope:
- **NEW NOTE**: "There are layers on top of the attributes that need maintenance as well. So, maintenance in this case is more generic and encompasses more than just the attribute itself."
- **Purpose**: Clarifies that maintenance includes not just attributes but their relationships, metadata, and supporting structures

### No Changes to:

- All requirement specifications (CAT_01 through CAT_11) remain textually unchanged
- Empty placeholders (CAT_02, CAT_08, CAT_11) remain empty
- No new requirements added
- No requirements removed

### Overall Assessment:

The CAT requirements demonstrate **complete stability in substantive content** with only clarifying notes added. The catalogue framework for both attributes and Attestation Rulebooks remains unchanged, including:

**Attributes Catalogue (CAT_01 - CAT_04):**
- Commission responsibility to establish and maintain
- Open registration process
- Public availability and machine-readability
- Consideration of existing semantic artifacts (RPaM, SEMPER, SEMIC, IANA, ISO/IEC 23220-2)

**Attestation Rulebooks Catalogue (CAT_05 - CAT_10):**
- Commission responsibility to establish and maintain
- Self-registration without pre-approval
- Public availability with e-discovery
- Versioning and change history

The new notes provide useful implementation guidance without changing the fundamental requirements. They clarify:
1. **Architectural flexibility**: Single vs. separate catalogues
2. **Operational requirements**: High availability and redundancy
3. **Maintenance scope**: Beyond individual attributes to their context and relationships

All requirements remain assigned to the Commission (🟡 status), indicating these are EU-level responsibilities not yet fully implemented. The stability of these requirements suggests the catalogue framework is well-defined and ready for implementation once the Commission establishes the necessary infrastructure.

---

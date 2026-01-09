# Preview: Issue #679 - ✅🟧 ARF HLR Topic 3 - PID Rulebook

**Topic:** Topic 3 - PID Rulebook

**Requirements ARF 2.5.0:** 18
**Requirements ARF 2.7.3:** 21

---

## Diff ARF 2.5.0 → ARF 2.7.3

### ✅ Requirements added in ARF 2.7.3 (3):

- **PID_06**: When issuing a PID compliant with [ISO/IEC 18013-5], a PID Provider MAY include attributes that are not defined in the [PID Rulebook](../annex-3/annex-3.01-pid-rulebook.md). If so, these attributes SHALL be defined within a domestic PID namespace as meant in requirement ARB_10 in [Topic 12](./annex-2.02-high-level-requirements-by-topic.md#a239-topic-12---attestation-rulebooks). The PID Provider SHALL generate the identifier for this domestic PID namespace by appending the applicable ISO 3166-1 alpha-2 country code or the ISO 3166-2 region code, separated by a period, to the PID namespace identifier specified in PID_05, excluding the version number. The PID Provider MAY include a version number in the domestic PID namespace identifier. *Note: For example, the identifier of the first domestic PID namespace for Germany could be "eu.europa.ec.eudi.pid.de.1".
- **PID_07**: A PID Provider that defines a domestic namespace SHALL publish the namespace, including all attribute identifiers, their definition, presence and encoding format, in an Attestation Rulebook complying with all applicable requirements in [Topic 12](./annex-2.02-high-level-requirements-by-topic.md#a239-topic-12---attestation-rulebooks).
- **PID_16**: A PID Provider that defines a domestic type SHALL publish information about the type, including all claim identifiers, their definition, presence and encoding format, in an Attestation Rulebook complying with all applicable requirements in [Topic 12](./annex-2.02-high-level-requirements-by-topic.md#a239-topic-12---attestation-rulebooks).

**Total requirements ARF 2.7.3:** 21
**Total requirements ARF 2.5.0:** 18
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

### ✅ Requirements added in ARF 2.7.3 (3):

- **PID_06**: When issuing a PID compliant with [ISO/IEC 18013-5], a PID Provider MAY include attributes that are not defined in the [PID Rulebook](../annex-3/annex-3.01-pid-rulebook.md). If so, these attributes SHALL be defined within a domestic PID namespace as meant in requirement ARB_10 in [Topic 12](./annex-2.02-high-level-requirements-by-topic.md#a239-topic-12---attestation-rulebooks). The PID Provider SHALL generate the identifier for this domestic PID namespace by appending the applicable ISO 3166-1 alpha-2 country code or the ISO 3166-2 region code, separated by a period, to the PID namespace identifier specified in PID_05, excluding the version number. The PID Provider MAY include a version number in the domestic PID namespace identifier. *Note: For example, the identifier of the first domestic PID namespace for Germany could be "eu.europa.ec.eudi.pid.de.1".
- **PID_07**: A PID Provider that defines a domestic namespace SHALL publish the namespace, including all attribute identifiers, their definition, presence and encoding format, in an Attestation Rulebook complying with all applicable requirements in [Topic 12](./annex-2.02-high-level-requirements-by-topic.md#a239-topic-12---attestation-rulebooks).
- **PID_16**: A PID Provider that defines a domestic type SHALL publish information about the type, including all claim identifiers, their definition, presence and encoding format, in an Attestation Rulebook complying with all applicable requirements in [Topic 12](./annex-2.02-high-level-requirements-by-topic.md#a239-topic-12---attestation-rulebooks).


| Status | ID | Requirement Specification | IT-Wallet Mapping & Documentation |
|---|---------|------------------|-----------------------------------|
| 🟡 | PID_01 | PIDs and PID Providers SHALL comply with all requirements in [PID Rulebook]. |  |
| 🟡 | PID_02 | A PID Provider SHALL issue any PID in both the format specified in ISO/IEC 18013-5 [ISO/IEC 18013-5] and the format specified in [SD-JWT VC].  *Note: [CIR 2024/2977] mentions the W3C Verifiable Credentials Data Model v1.1 instead of [SD-JWT VC]. The latest stable version of this standard is [W3C VCDM 2.0].  However, W3C VCDM is not a complete specification of an attestation format. In particular, it does not specify a specific proof method to be used. Without additional specification, such as those in [W3C VC-JOSE-COSE] or [W3C VC Data Integrity], and making further choices, it is impossible to implement a PID based on W3C VCDM. This Rulebook considers [SD-JWT VC] to essentially be such an additional specification. See also [Section 5.3.4](../../architecture-and-reference-framework-main.md#534-w3c-verifiable-credentials) of the ARF main document. |  |
| 🟡 | PID_03 | The portrait in a PID SHALL consist of a single portrait image in JPEG format. The portrait image SHALL comply with the quality requirements for a Full Frontal Image Type in ISO/IEC 19794-5 clauses 8.2, 8.3, and 8.4. However, the attribute portrait SHALL NOT comply with the format requirements in ISO/IEC 19794-5 clauses 8.1 and 8.5, meaning it SHALL NOT contain any of the headers or blocks specified in clause 5 except for the image data itself (a JPEG). |  |
| 🟡 | PID_04 | PID Providers SHALL use eu.europa.ec.eudi.pid.1 as the attestation type for ISO/IEC 18013-5-compliant PIDs. *Note: a) This identifier uses the general format [Reverse Domain].[Domain Specific Extension]. Since the European Commission controls the domain ec.europa.eu, this attestation type identifier will not collide with any attestation type identifiers defined by other organisations in other Attestation Rulebooks. b) The version number 1 in this identifier is used to distinguish between the first version of the PID, defined in the [PID Rulebook](../annex-3/annex-3.01-pid-rulebook.md), and any future version, which will then have an incremented version number. |  |
| 🟡 | PID_05 | When issuing a PID compliant with [ISO/IEC 18013-5], a PID Provider SHALL use the value "eu.europa.ec.eudi.pid.1" for the identifier of the namespace for the PID attributes specified in [Section 4.2 of the PID Rulebook](../annex-3/annex-3.01-pid-rulebook.md#42-encoding-of-pid-attributes-and-metadata). *Note: a) The version number "1" allows for future extension(s) or change(s) of the ISO/IEC 18013-5-compliant PID attributes. b) This namespace has the same value as the attestation type specified in requirement PID_04. This is allowed according to ISO/IEC 18013-5. |  |
| 🟡 | PID_06 | When issuing a PID compliant with [ISO/IEC 18013-5], a PID Provider MAY include attributes that are not defined in the [PID Rulebook](../annex-3/annex-3.01-pid-rulebook.md). If so, these attributes SHALL be defined within a domestic PID namespace as meant in requirement ARB_10 in [Topic 12](./annex-2.02-high-level-requirements-by-topic.md#a239-topic-12---attestation-rulebooks). The PID Provider SHALL generate the identifier for this domestic PID namespace by appending the applicable ISO 3166-1 alpha-2 country code or the ISO 3166-2 region code, separated by a period, to the PID namespace identifier specified in PID_05, excluding the version number. The PID Provider MAY include a version number in the domestic PID namespace identifier. *Note: For example, the identifier of the first domestic PID namespace for Germany could be "eu.europa.ec.eudi.pid.de.1". |  |
| 🟡 | PID_07 | A PID Provider that defines a domestic namespace SHALL publish the namespace, including all attribute identifiers, their definition, presence and encoding format, in an Attestation Rulebook complying with all applicable requirements in [Topic 12](./annex-2.02-high-level-requirements-by-topic.md#a239-topic-12---attestation-rulebooks). |  |
| 🟡 | PID_08 | When issuing a PID compliant with [ISO/IEC 18013-5], a PID Provider SHALL include both the attributes and the metadata specified in [CIR 2024/2977] in the PID as (issuer-signed or device-signed) data elements. *Note: This implies that technically speaking, there is no difference between these attributes and metadata. |  |
| 🟡 | PID_09 | When issuing a PID compliant with [ISO/IEC 18013-5], a PID Provider SHALL encode each attribute or metadata in the PID as specified in the third column of the tables in [Section 4.2.1 of the PID Rulebook](../annex-3/annex-3.01-pid-rulebook.md#421-overview). |  |
| 🟡 | PID_10 | When issuing a PID compliant with [ISO/IEC 18013-5], a PID Provider SHALL encode each attribute or metadata in the PID in Concise Binary Object Representation (CBOR) according to [RFC 8949]. |  |
| 🟡 | PID_11 | When issuing a PID compliant with [ISO/IEC 18013-5], a PID Provider SHALL ensure that each PID contains at most one attribute with the same attribute identifier. |  |
| 🟡 | PID_12 | When issuing a PID compliant with [ISO/IEC 18013-5], a PID Provider SHALL ensure that the value of all attributes and metadata in the PID is valid at the value of the timestamp in the validFrom element in the MSO, see [ISO/IEC 18013-5] clause 9.1.2.4. *Note: The value of the age_over_18, age_over_NN, or age_in_years attributes, if present, changes whenever the User to whom the person identification data relates has a relevant birthday. The value of many other attributes will also change over time. |  |
| 🟡 | PID_13 | When issuing a PID compliant with [ISO/IEC 18013-5], a PID Provider SHALL ensure that the issuance_date attribute, if present, is not later than the validFrom element in the MSO, see [ISO/IEC 18013-5] clause 9.1.2.4. |  |
| 🟡 | PID_14 | A PID Provider issuing [SD-JWT VC]-compliant PIDs SHALL include the vct claim in their PIDs, where the vct claim SHALL be a URN within the `urn:eudi:pid:` namespace. The type indicated by the vct claim SHALL be `urn:eudi:pid:1` for the type defined in this document or a domestic type that extends it. |  |
| 🟡 | PID_15 | Empty |  |
| 🟡 | PID_16 | A PID Provider that defines a domestic type SHALL publish information about the type, including all claim identifiers, their definition, presence and encoding format, in an Attestation Rulebook complying with all applicable requirements in [Topic 12](./annex-2.02-high-level-requirements-by-topic.md#a239-topic-12---attestation-rulebooks). |  |
| 🟡 | PID_17 | When issuing a PID compliant with [SD-JWT VC], a PID Provider SHALL include both the attributes and the metadata specified in [CIR 2024/2977] in the PID as claims. *Note: This implies that technically speaking, there is no difference between these attributes and metadata. |  |
| 🟡 | PID_18 | When issuing a PID compliant with [SD-JWT VC], a PID Provider SHALL encode each attribute or metadata in the PID as specified in the tables in [Section 5.2 of the PID Rulebook](../annex-3/annex-3.01-pid-rulebook.md#52-encoding-of-pid-attributes). |  |
| 🟡 | PID_19 | When issuing a PID compliant with [SD-JWT VC], a PID Provider SHALL ensure that the value of all attributes and metadata in the PID is valid at the value of the timestamp in the nbf claim, if present. *Note: The value of the age-related claims, if present, changes whenever the User to whom the person identification data relates has a relevant birthday. The value of many other attributes will also change over time. |  |
| 🟡 | PID_20 | When issuing a PID compliant with [SD-JWT VC], a PID Provider SHALL ensure that the date_of_issuance claim, if present, is not later than the value of the timestamp in the nbf claim, if present. |  |
| 🟡 | PID_21 | When issuing a PID compliant with [SD-JWT VC], a PID Provider SHALL make all claims (i.e., all top-level properties, all nested properties, and all array entries) selectively disclosable individually, except those claims defined as non-selectively disclosable in [SD-JWT VC]. |  |

---

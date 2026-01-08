# Topic 3 - PID Rulebook

| **Requirement ID** | **Legacy ID** | **Description** | **Status** |
|-------------------|---------------|------------------|------------|
| PID_01 |  | PIDs and PID Providers SHALL comply with all requirements in [PID Rulebook]. | 🟡 |
| PID_02 |  | A PID Provider SHALL issue any PID in both the format specified in ISO/IEC 18013-5 [ISO/IEC 18013-5] and the format specified in [SD-JWT VC].  *Note: [CIR 2024/2977] mentions the W3C Verifiable Cre... | 🟡 |
| PID_03 |  | The portrait in a PID SHALL consist of a single portrait image in JPEG format. The portrait image SHALL comply with the quality requirements for a Full Frontal Image Type in ISO/IEC 19794-5 clauses... | 🟡 |
| PID_04 |  | PID Providers SHALL use eu.europa.ec.eudi.pid.1 as the attestation type for ISO/IEC 18013-5-compliant PIDs. *Note: a) This identifier uses the general format [Reverse Domain].[Domain Specific Exten... | 🟡 |
| PID_05 |  | When issuing a PID compliant with [ISO/IEC 18013-5], a PID Provider SHALL use the value "eu.europa.ec.eudi.pid.1" for the identifier of the namespace for the PID attributes specified in [Section 4.... | 🟡 |
| PID_08 |  | When issuing a PID compliant with [ISO/IEC 18013-5], a PID Provider SHALL include both the attributes and the metadata specified in [CIR 2024/2977] in the PID as (issuer-signed or device-signed) da... | 🟡 |
| PID_09 |  | When issuing a PID compliant with [ISO/IEC 18013-5], a PID Provider SHALL encode each attribute or metadata in the PID as specified in the third column of the tables in [Section 4.2.1 of the PID Ru... | 🟡 |
| PID_10 |  | When issuing a PID compliant with [ISO/IEC 18013-5], a PID Provider SHALL encode each attribute or metadata in the PID in Concise Binary Object Representation (CBOR) according to [RFC 8949]. | 🟡 |
| PID_11 |  | When issuing a PID compliant with [ISO/IEC 18013-5], a PID Provider SHALL ensure that each PID contains at most one attribute with the same attribute identifier. | 🟡 |
| PID_12 |  | When issuing a PID compliant with [ISO/IEC 18013-5], a PID Provider SHALL ensure that the value of all attributes and metadata in the PID is valid at the value of the timestamp in the validFrom ele... | 🟡 |
| PID_13 |  | When issuing a PID compliant with [ISO/IEC 18013-5], a PID Provider SHALL ensure that the issuance_date attribute, if present, is not later than the validFrom element in the MSO, see [ISO/IEC 18013... | 🟡 |
| PID_14 |  | A PID Provider issuing [SD-JWT VC]-compliant PIDs SHALL include the vct claim in their PIDs, where the vct claim SHALL be a URN within the `urn:eudi:pid:` namespace. The type indicated by the vct c... | 🟡 |
| PID_15 |  | Empty | 🟡 |
| PID_17 |  | When issuing a PID compliant with [SD-JWT VC], a PID Provider SHALL include both the attributes and the metadata specified in [CIR 2024/2977] in the PID as claims. *Note: This implies that technica... | 🟡 |
| PID_18 |  | When issuing a PID compliant with [SD-JWT VC], a PID Provider SHALL encode each attribute or metadata in the PID as specified in the tables in [Section 5.2 of the PID Rulebook](../annex-3/annex-3.0... | 🟡 |
| PID_19 |  | When issuing a PID compliant with [SD-JWT VC], a PID Provider SHALL ensure that the value of all attributes and metadata in the PID is valid at the value of the timestamp in the nbf claim, if prese... | 🟡 |
| PID_20 |  | When issuing a PID compliant with [SD-JWT VC], a PID Provider SHALL ensure that the date_of_issuance claim, if present, is not later than the value of the timestamp in the nbf claim, if present. | 🟡 |
| PID_21 |  | When issuing a PID compliant with [SD-JWT VC], a PID Provider SHALL make all claims (i.e., all top-level properties, all nested properties, and all array entries) selectively disclosable individual... | 🟡 |
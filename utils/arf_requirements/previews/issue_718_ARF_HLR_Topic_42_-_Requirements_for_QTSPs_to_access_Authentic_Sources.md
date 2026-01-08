# Preview: Issue #718 - ARF HLR Topic 42 - Requirements for QTSPs to access Authentic Sources

**Topic:** Topic 42 - Requirements for QTSPs to access Authentic Sources

**Requirements ARF 2.5.0:** 9
**Requirements ARF 2.7.3:** 9

---

## Diff ARF 2.5.0 → ARF 2.7.3

### ℹ️ No changes detected

The requirements are identical between ARF 2.5.0 and ARF 2.7.3.

**Total requirements ARF 2.7.3:** 9
**Total requirements ARF 2.5.0:** 9
---

## Nuovo body completo della issue:

# Topic 42 - QTSP and Authentic Sources (QTSPAS) - Changelog

**ARF VERSION:**  
UPDATED TO ARF 2.7.3.

### No Changes Detected

---

## HLRs


### ✅ Requirements added in ARF 2.7.3 (1):

- **QTSPAS_08**: A QTSP SHALL obtain approval from the User to verify the authenticity of the attributes, before requesting the verification of those attributes by the relevant Authentic Source or designated intermediary.

## Diff ARF 2.5.0 → ARF 2.7.3

### ℹ️ No changes detected

The requirements are identical between ARF 2.5.0 and ARF 2.7.3.


| Status | **Index** | **Requirement specification** | **IT-Wallet Mapping & Documentation** |
|---|---------|------------------|-----------------------------------|
| ✅ | QTSPAS_01 | In accordance with technical specifications referred to in QTSPAS_07, Member States SHALL define: - discovery mechanisms that enable QTSPs to request information about Authentic Sources or designated intermediaries recognised at the national level. This includes information regarding the attributes of a natural or legal person for which the Authentic Source or designated intermediary is considered a primary source, or for which it is recognised as authentic in accordance with Union law or national law, including administrative practices. - procedures for QTSPs to request the verification of attributes from Authentic Sources. |  |
| 🟧 | QTSPAS_02 | An Authentic Source in the public sector, or its designated intermediary, SHALL implement an interface complying with the technical specification mentioned in QTSPAS_07 for receiving verification requests and sending responses. For each received request, the Authentic Source SHALL - identify and authenticate the requestor in such a way that it can subsequently determine whether the requestor is a QTSP issuing qualified electronic attestation of attributes, for example by means of a lookup in the QTSP Trusted List. - authenticate the User and obtain their approval, if it is legally obliged to do so, in addition to the User authentication and approval already performed by the QTSP according to QTSPAS_08. - verify whether the attribute values claimed by the QTSP match the values held by the Authentic Source; and, finally, - respond with one of the following for each attribute: +'match', if the attribute value held for this User by the Authentic Source is identical to the value claimed by the QTSP, + 'no match', if the attribute value held for this User by the Authentic Source is not identical to the value claimed by the QTSP, including if the Authentic Source is the authentic source for this attribute but does not hold a value for this User, +'unknown', if the Authentic Source is not the authentic source for this attribute. |  |
| 🟧 | QTSPAS_03 | An Authentic Source or designated intermediary SHALL respond to a verification request for attributes by any QTSP issuing qualified electronic attestation of attributes. |  |
| 🟧 | QTSPAS_04 | An Authentic Source or designated intermediary SHALL implement the technical specifications mentioned in QTSPAS_01, so that the QTSP will receive the result of the verification of the requested attributes as described in QTSPAS_02. If the verification is deferred, the response to the QTSP SHALL include the maximum time that it will take to verify the requested attributes, and a unique identifier that the QTSP SHALL use to obtain the result of the verification. |  |
| 🟧 | QTSPAS_05 | A QTSP SHALL send an attribute verification request directly to the Authentic Source or designated intermediary recognised at national level, after discovering it using the mechanisms mentioned in QTSPAS_01. |  |
| 🟧 | QTSPAS_06 | Member States SHALL specify the processes and mechanisms to designate the Authentic Sources or intermediaries recognised at national level in accordance with Union or national law, allowing these Authentic Sources or intermediaries to verify the attributes presented to them by QTSPs. |  |
| 🟧 | QTSPAS_07 | The Commission SHALL publish, in cooperation with the European Digital Identity Cooperation Group, a technical specification, referring to applicable standards, specifications and procedures, that will cover at least the attributes specified in Annex VI, wherever those attributes rely on Authentic Sources within the public sector, for which Member States must ensure that measures are taken to allow qualified providers of electronic attestations of attributes to verify by electronic means, at the request of the User, their authenticity against the relevant authentic source. |  |
| 🟧 | QTSPAS_07a | The standards and procedures mentioned in QTSPAS_07 SHOULD, whenever possible, be aligned and compatible with those used for the platforms implementing the Once Only Technical System (OOTS). *Note: There is a clear synergy of both of these data exchange approaches. In fact, the national OOTS node would be a candidate for acting as an intermediary between QTSPs issuing QEAAs and the Authentic Sources. |  |
| 🟡 | QTSPAS_08 | A QTSP SHALL obtain approval from the User to verify the authenticity of the attributes, before requesting the verification of those attributes by the relevant Authentic Source or designated intermediary. |  |**All QTSPAS requirements remain completely unchanged** between versions. 
### Related Topics:

- **Topic 31** (Notification): QTSP Trusted List referenced
- **Annex VI**: Attributes covered by technical specification
- **OOTS** (Once Only Technical System): Platform alignment

---

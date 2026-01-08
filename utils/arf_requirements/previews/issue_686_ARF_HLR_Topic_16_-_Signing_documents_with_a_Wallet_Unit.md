# Preview: Issue #686 - ❌ ARF HLR Topic 16 - Signing documents with a Wallet Unit

**Topic:** Topic 16 - Signing documents with a Wallet Unit

**Requirements ARF 2.5.0:** 26
**Requirements ARF 2.7.3:** 27

---

## Diff ARF 2.5.0 → ARF 2.7.3

### ✅ Requirements added in ARF 2.7.3 (1):

- **QES_26**: Empty

**Total requirements ARF 2.7.3:** 27
**Total requirements ARF 2.5.0:** 26
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

## A. Requirement for Wallet Providers

## Diff ARF 2.5.0 → ARF 2.7.3

### ✅ Requirements added in ARF 2.7.3 (1):

- **QES_26**: Empty


| Status | **ID** | **Requirement specification** | **IT-Wallet Mapping & Documentation** |
|---|---------|------------------|-----------------------------------|
| ❌ | QES_01 | Wallet Providers SHALL ensure that each User has the possibility to receive a qualified certificate for Qualified Electronic Signatures, bound to a QSCD, that is either local, external, or remotely managed in relation to the Wallet Instance. |  |
| ❌ | QES_02 | Wallet Providers SHALL ensure that each User who is a natural person has, at least for non-professional purposes, free-of-charge access to a Signature Creation Application which allows the creation of free-of-charge Qualified Electronic Signatures using the certificates referred to in QES_01. Wallet Providers SHALL ensure that: - The Signature Creation Application SHALL, as a minimum, be capable of signing or sealing User-provided data and Relying Party-provided data. - The Signature Creation Application SHALL be implemented as part of a Wallet Solution or external to it (by providers of trust services or by Relying Parties). - The Signature Creation Application SHALL be able to generate signatures or seals in formats compliant with at least the mandatory formats referred to in QES_08. *Note: a) Signature Creation Application (SCA): see definition in the ETSI TS 119 432 standard. 2) If the SCA is external to the Wallet Solution, it may be for example a separate mobile application, or be hosted remotely, for instance by the QTSP or by a Relying Party. |  |
| ❌ | QES_03 | For the use of the qualified certificate referred to in QES_01, Wallet Providers SHALL ensure that a Wallet Unit implements secure authentication of the User, as well as signature or seal invocation capabilities, as a part of a local, external or remote QSCD. |  |
| ❌ | QES_04 | Wallet Providers SHALL enable their Wallet Units to interface with QSCDs using protocols and interfaces necessary for the implementation of secure User authentication and signature or seal functionality. *Note: In a Relying Party-centric flow, the remote QTSP will likely be selected by the Relying Party, which implies the QSCD is managed by the remote QTSP. In a Wallet Unit-driven flow, the User should be able to choose the QSCD. |  |
| ❌ | QES_05 | Wallet Providers SHALL enable their Wallet Units to be used for User enrolment to a remote QES Provider (i.e., a QTSP offering remote QES), except where the Wallet Unit interfaces with local or external QSCDs. |  |
| ❌ | QES_06 | Wallet Providers SHALL ensure that their Wallet Solution supports at least one of the following options for remote QES signature creation: - remote QES creation through secure authentication to a QTSP signature web portal, - remote QES creation channelled by the Wallet Unit, - remote QES creation channelled by a Relying Party. |  |
| ❌ | QES_07 | Wallet Providers SHALL ensure that, where a Signature Creation Application relies on a remote Qualified Signature Creation Device and where it is integrated into a Wallet Instance, it supports the Cloud Signature Consortium API Specification 2.0 [CSC API]. |  |
| ❌ | QES_08 | Wallet Providers SHALL ensure that their Wallet Units are able to create signatures or seals in accordance with the mandatory PAdES format as specified in ETSI EN 319 142-1 V1.1.1 (2016-04). In addition, Wallet Providers SHOULD ensure that their Wallet Units are able to create signatures or seals in accordance with the following formats: - XAdES as specified in ETSI EN 319 132-1 V1.2.1 (2022-02), - JAdES as specified in ETSI TS 119 182-1 V1.2.1 (2024-07), - CAdES as specified in ETSI EN 3191 22-1 V1.3.1 (2023-06), and - ASiC as specified in ETSI EN 319 162-1 V1.1.1 (2016-04) and ETSI EN 319 162-2 V1.1.1 (2016-04). |  |
| ❌ | QES_09 | Empty |  |
| ❌ | QES_10 | Wallet Providers SHALL ensure that, where the Signature Creation Application is implemented as part of the Wallet Unit and is used to generate signatures or seals of the representation of the document or data to be signed or sealed, the Wallet Unit presents the representation of the document or data to be signed or sealed to the User. |  |
| ❌ | QES_11 | Wallet Providers SHALL ensure that, where the Signature Creation Application is implemented as part of the Wallet Unit, a Wallet Unit computes the hash or digest of the document or data to be signed through a Signature Create Application component. |  |
| ❌ | QES_12 | Wallet Providers SHALL ensure that a Wallet Unit is able to create the signature value of the document or data to be signed either using a local or a remote signing application. *Note: a local signing application is on-device. It may either be embedded in the Wallet Unit or be an external application. |  |
| ❌ | QES_14 | Wallet Providers SHALL ensure that the User will be able to explicitly authorise the creation of a qualified electronic signature or seal through their Wallet Unit. |  |
| ❌ | QES_15 | Wallet Providers SHALL ensure that a Wallet Unit can verify, in remote signature creation scenarios, that the qualified electronic signature or seal creation device is part of a qualified service, which is carried out by a qualified trust service provider. |  |
| ❌ | QES_16 | Wallet Providers SHOULD ensure that a Wallet Unit supports multiple-signing scenarios where multiple signatories are required to sign the same document or data. |  |
| ❌ | QES_17 | Wallet Providers SHALL ensure that Wallet Units provide a signature creation confirmation upon the creation of a qualified electronic signature, informing the User about the outcome of the signature creation process. *Note: See also QES_17a. |  |
| ❌ | QES_17a | If the Signature Creation Application is external to the Wallet Unit, after the User authorises the usage of the private signing key, the Signature Creation Application SHALL return the outcome of the signature creation process to the Wallet Unit. |  |
| ❌ | QES_18 | Wallet Providers SHALL configure at least one default qualified signing service in the Wallet Unit. |  |
| ❌ | QES_19 | Wallet Providers SHALL ensure that, where the Signature Creation Application is implemented as part of the Wallet Unit, a Wallet Unit supports ETSI TS 119 101 (Electronic Signatures and Infrastructures (ESI); Policy and security requirements for applications for signature creation and signature validation) when using signing keys managed by the QSCD, whether locally, externally, or remotely in relation to the Wallet Instance. |  |
| ❌ | QES_20 | Empty |  |
| ❌ | QES_21 | Empty |  |
| ❌ | QES_22 | Empty |  |
| ❌ | QES_23 | QTSPs providing the remote QES part of a Wallet Solution SHALL support: 1. ETSI TS 119 431-1 (Electronic Signatures and Infrastructures (ESI); Policy and security requirements for trust service providers; Part 1: TSP service components operating a remote QSCD / SCDev), 2. ETSI TS 119 431-2 (Electronic Signatures and Infrastructures (ESI); Policy and security requirements for trust service providers; Part 2: TSP service components supporting AdES digital signature creation), 3. ETSI TS 119 432 (Electronic Signatures and Infrastructures (ESI); Protocols for remote digital signature creation). Wallet Providers and QTSPs providing the remote QES part of a Wallet Solution SHALL comply with Sole Control Assurance Level (SCAL) 2 as defined in CEN EN 419 241-1 (Trustworthy Systems Supporting Server Signing - Part 1: General System Security Requirements). |  |
| ❌ | QES_24 | QTSPs providing the Signature Creation Application as part of the remote QES part of a Wallet Solution SHALL support ETSI TS 119 101 (Electronic Signatures and Infrastructures (ESI); Policy and security requirements for applications for signature creation and signature validation). |  |
| 🟡 | QES_24a | Relying Parties providing the Signature Creation Application in a Relying Party-centric flow SHALL support ETSI TS 119 101 (Electronic Signatures and Infrastructures (ESI); Policy and security requirements for applications for signature creation and signature validation). |  |
| 🟡 | QES_25 | Empty |  |
| 🟡 | QES_26 | Empty |  |## C. Requirements for Relying Parties

| **ID**   | **Requirement specification** | **IT-Wallet Mapping & Documentation** |
|---|----------|------------------------------|---------------------------------------|
| ❌ | QES_24a | Relying Parties providing the Signature Creation Application in a Relying Party-centric flow SHALL support ETSI TS 119 101 (Electronic Signatures and Infrastructures (ESI); Policy and security requirements for applications for signature creation and signature validation). | |

---

## D. Requirements for the Commission

| **ID**   | **Requirement specification** | **IT-Wallet Mapping & Documentation** |
|---|----------|------------------------------|---------------------------------------|
| ❌ | QES_25  | ~~Empty~~ **Empty [NO CHANGE]** |  |
| ❌ | QES_26  | ~~Empty~~ **Empty [NO CHANGE]** |  |

---

## Summary of Changes in ARF 2.7.3

### Structural Organization:

The requirements have been organized into clear sections:
- **Section A**: Requirement for Wallet Providers (QES_01 - QES_22)
- **Section B**: Requirements for QTSPs (QES_23 - QES_24)
- **Section C**: Requirements for Relying Parties (QES_24a)
- **Section D**: Requirements for the Commission (QES_25 - QES_26)

### No Substantive Changes:

**ALL QES requirements remain completely unchanged** from the previous version to ARF 2.5.0. This topic shows complete stability with:
- No modifications to existing requirements
- No new requirements added
- No requirements removed
- All empty placeholders (QES_09, QES_20, QES_21, QES_22, QES_25, QES_26) remain empty

### Overall Assessment:

The QES requirements demonstrate complete stability between versions. The qualified electronic signature framework, including:
- Wallet Provider obligations for QSCD support and signature formats
- QTSP requirements for remote QES services
- Relying Party requirements for signature creation applications
- Logging, user authorization, and verification requirements

All remain exactly as specified in the previous version. This stability suggests that the QES framework is mature and well-established, with no need for adjustments or clarifications in this release.

The only organizational improvement is the clear sectioning of requirements by stakeholder type (Wallet Providers, QTSPs, Relying Parties, Commission), making the document easier to navigate for different implementers.

---

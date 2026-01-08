# Preview: Issue #678 - ✅ ARF HLR Topic 1 - Accessing Online Services with a Wallet Unit

**Topic:** Topic 1 - Accessing Online Services with a Wallet Unit

**Requirements ARF 2.5.0:** 20
**Requirements ARF 2.7.3:** 20

---

## Diff ARF 2.5.0 → ARF 2.7.3

### ℹ️ No changes detected

The requirements are identical between ARF 2.5.0 and ARF 2.7.3.

**Total requirements ARF 2.7.3:** 20
**Total requirements ARF 2.5.0:** 20
---

## Nuovo body completo della issue:

**ARF VERSION:**  
UPDATED TO ARF 2.7.3.

## Diff ARF 2.5.0 → ARF 2.7.3

### ℹ️ No changes detected

The requirements are identical between ARF 2.5.0 and ARF 2.7.3.


| Status | ID | Requirement Specification | IT-Wallet Mapping & Documentation |
|---|---------|------------------|-----------------------------------|
| ✅ | OIA_01 | A Wallet Unit SHALL support [OpenID4VP] for remote presentation flows and [ISO/IEC 18013-5] for proximity presentation flows, to receive and respond to presentation requests for person identification data (PID) and attestations by Relying Parties. | IT-Wallet supports both remote and proximity presentation flows. [Digital Credential Presentation](https://italia.github.io/eid-wallet-it-docs/versione-corrente/en/credential-presentation.html) |
| ✅ | OIA_02 | A Wallet Unit SHALL support proving cryptographic device binding between the WSCA/WSCD or a keystore included in the Wallet Unit and a PID or attestation, in accordance with [SD-JWT VC] or [ISO/IEC 18013-5]. *Note: Such a mechanism is called 'mdoc authentication' in [ISO/IEC 18013-5] and 'key binding' in [SD-JWT VC]. | IT-Wallet uses cryptographic proofs for binding. [Digital Credential Presentation](https://italia.github.io/eid-wallet-it-docs/versione-corrente/en/credential-presentation.html) |
| ✅ | OIA_03 | Empty |  |
| ✅ | OIA_03a | Wallet Providers SHALL ensure that their Wallet Solution supports the protocol specified in 'OpenID for Verifiable Presentations', see [OpenID4VP], with additions and changes as documented in this Annex and in technical specifications referenced in this Annex. | IT-Wallet supports OpenID4VP. [Digital Credential Presentation](https://italia.github.io/eid-wallet-it-docs/versione-corrente/en/credential-presentation.html) |
| ✅ | OIA_03b | For remote presentation flows, when the format of the requested attestation complies with [ISO/IEC 18013-5], Relying Parties and Wallet Units SHALL comply with the requirements in the profile for OpenID4VP specified in [ISO/IEC 18013-7] Annex B. | IT-Wallet supports ISO/IEC 18013-7 Annex B profile. [Digital Credential Presentation](https://italia.github.io/eid-wallet-it-docs/versione-corrente/en/credential-presentation.html) |
| ✅ | OIA_03c | For remote presentation flows, when the format of the requested attestation complies with [SD-JWT VC], Relying Parties and Wallet Units SHALL comply with the requirements in the 'OpenID for Verifiable Presentations for IETF SD-JWT VC' profile specified in [HAIP]. | IT-Wallet supports SD-JWT VC profile. [Digital Credential Presentation](https://italia.github.io/eid-wallet-it-docs/versione-corrente/en/credential-presentation.html) |
| ✅ | OIA_04 | A Wallet Unit SHALL verify and process PID or attestation presentation requests from Relying Parties in accordance with the protocols and interfaces specified in [OpenID4VP] for remote flows. | IT-Wallet verifies requests and ensures secure processing. [Digital Credential Presentation](https://italia.github.io/eid-wallet-it-docs/versione-corrente/en/credential-presentation.html) |
| ✅ | OIA_05 | After verifying and processing a PID or attestation request, the Wallet Unit SHALL display to the User the identity of the requesting Relying Party and the requested attributes. | IT-Wallet requires explicit user consent before sharing data. [Digital Credential Presentation](https://italia.github.io/eid-wallet-it-docs/versione-corrente/en/credential-presentation.html) |
| ✅ | OIA_06 | A Wallet Unit SHALL present the requested attributes only after having received the User's authorisation. *Note: See also OIA_07. | IT-Wallet allows users to choose which attributes to share.[Digital Credential Presentation](https://italia.github.io/eid-wallet-it-docs/versione-corrente/en/credential-presentation.html) |
| ✅ | OIA_07 | A Wallet Unit SHALL support selective disclosure of attributes from PIDs and attestations to be released to the requesting Relying Parties. | IT-Wallet supports selective disclosure. [Digital Credential Presentation](https://italia.github.io/eid-wallet-it-docs/versione-corrente/en/credential-presentation.html) |
| 🟧 | OIA_08 | Wallet Units and Relying Party Instances SHALL support the [W3C Digital Credentials API]](<https://wicg.github.io/digital-credentials/>) for remote presentation flows, provided that a) this API is a W3C Recommendation, b) this API complies with the expectations outlined in [Chapter 3](../../discussion-topics/f-digital-credential-api.md#3) of the Topic F discussion paper, and c) this API is broadly supported by relevant browsers and operating systems. | IT-Wallet supports W3C Digital Credentials API (when available). [Digital Credential Presentation](https://italia.github.io/eid-wallet-it-docs/versione-corrente/en/credential-presentation.html) |
| ⚠️ | OIA_08a | If Wallet Units and Relying Party Instances do not support the [W3C Digital Credentials API], they SHALL implement adequate mitigations for the challenges described in [Section 4.4.3.1](../../architecture-and-reference-framework-main.md#4431-introduction) of the ARF main document. |  |
| ⚠️ | OIA_08b | If a Wallet Unit supports the [W3C Digital Credentials API], it SHALL, by default (see OIA_08d), disclose the presence of all stored attestations (mean their attestation type) to the Digital Credentials API framework, but it SHALL NOT disclose the attributes and their values in these attestations. *Note: The latter restriction applies even if such disclosure would enhance the services provided by the operating system to the Wallet Unit, for example, attestation selection in the context of the Digital Credentials API. |  |
| ⚠️ | OIA_08c | If a Relying Party supports the [W3C Digital Credentials API], the Relying Party's presentation request MAY be processed by the browser and/or the operating system for searching available attestations, for preventing fraud targeting the User, or for troubleshooting purposes. Moreover, the request SHOULD be processed by the browser and/or the Operating System for User security purposes. However, the request SHALL NOT be processed by the browser and/or the operating system for market analysis purposes (including as a secondary purpose) or for the browser's and/or the operating system's own purposes. |  |
| 🟡 | OIA_08d | If a Wallet Unit supports the [W3C Digital Credentials API], it SHALL provide a global User setting to disable the disclosure of stored attestations via the Digital Credentials API framework, as described in OIA_08b. When this setting is disabled, the Wallet Unit SHALL NOT advertise or respond to presentation requests or issuance requested communicated via the DC API. |  |
| 🟡 | OIA_08e | If a Wallet Unit supports the [W3C Digital Credentials API], it SHALL use the CTAP-Hybrid flow only if the expectations outlined in Chapter 4 of the [Topic F discussion paper](../../discussion-topics/f-digital-credential-api.md) are met. |  |
| ✅ | OIA_09 | For remote presentation flows the Wallet Unit SHALL ensure that the attributes included in the presented attestation are accessible only to the Relying Party Instance, by encrypting the presentation response. The technical specification meant in OIA_03a SHALL specify mechanisms preventing decryption of the presentation response via Man-in-the-Middle attacks by the browser, the operating system, or other components between the Wallet Unit and the Relying Party. | IT-Wallet ensures secure encrypted presentation responses. [Digital Credential Presentation](https://italia.github.io/eid-wallet-it-docs/versione-corrente/en/credential-presentation.html) |
| ✅ | OIA_10 | For both proximity and remote presentation flows, if a Wallet Unit contains two PIDs having the same encoding (e.g. ISO/IEC 18013-5 or SD-JWT VC-compliant) and a Relying Party requests a PID, the Wallet Unit SHALL ask the User which of these PIDs they want to release, unless the Wallet Unit can decide from context. | IT-Wallet supports user selection of PID. [Digital Credential Presentation](https://italia.github.io/eid-wallet-it-docs/versione-corrente/en/credential-presentation.html) |
| ✅ | OIA_13 | For both proximity and remote presentation flows, a Relying Party SHALL validate the qualified signature of a QEAA in accordance with Art.32 of the [European Digital Identity Regulation]. For the verification, the Relying Party SHALL use a trust anchor provided in a QEAA Provider Trusted List made available in accordance with [Art. 22](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=uriserv%3AOJ.L_.2014.257.01.0073.01.ENG#d1e2162-73-1) of the [European Digital Identity Regulation]. | IT-Wallet supports QEAA signature validation. [Digital Credential Presentation](https://italia.github.io/eid-wallet-it-docs/versione-corrente/en/credential-presentation.html) |
| ✅ | OIA_14 | For both proximity and remote presentation flows, a Relying Party SHALL validate the qualified signature of a PuB-EAA in accordance with [Art.32](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=uriserv%3AOJ.L_.2014.257.01.0073.01.ENG#d1e2594-73-1) of the [European Digital Identity Regulation]. For that verification, the Relying Party SHALL use the public key provided in the qualified certificate of the QTSP supporting the qualified signature. The Relying Party SHALL also validate the qualified certificate of the QTSP using a trust anchor provided in a Trusted List made available in accordance with [Art. 22](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=uriserv%3AOJ.L_.2014.257.01.0073.01.ENG#d1e2162-73-1) of the [European Digital Identity Regulation]. The Relying Party SHALL also verify the certified attributes of the qualified certificate, as specified in [Article 45f](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32024R1183#d1e3902-1-1). | IT-Wallet supports PuB-EAA signature validation. [Digital Credential Presentation](https://italia.github.io/eid-wallet-it-docs/versione-corrente/en/credential-presentation.html) |

---

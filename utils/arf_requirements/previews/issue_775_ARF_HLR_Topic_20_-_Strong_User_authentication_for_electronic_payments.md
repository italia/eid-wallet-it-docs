# Preview: Issue #775 - ARF HLR Topic 20 - Strong User authentication for electronic payments

**Topic:** Topic 20 - Strong User authentication for electronic payments

**Requirements ARF 2.5.0:** 1
**Requirements ARF 2.7.3:** 6

---

## Diff ARF 2.5.0 → ARF 2.7.3

### ✅ Requirements added in ARF 2.7.3 (6):

- **SUA_01**: The Wallet Units SHALL be able to process the transactional data included in a presentation request for that an attestation, according to all requirements in the associated Attestation Rulebook.
- **SUA_02**: The Attestation Rulebook (see [Topic 12](./annex-2.02-high-level-requirements-by-topic.md#a239-topic-12---attestation-rulebooks) of a SUA attestation SHALL specify the syntax and semantics of the transactional data associated with that attestation, as well as all necessary requirements for Wallet Units to process that transactional data, at least regarding a) displaying the data to the User when obtaining consent for signing the data, b) processing (e.g., hashing) the data for inclusion in the device binding signature, and c) the scope of information to be logged about a SUA attestation presentation transaction by a Wallet Unit.
- **SUA_03**: The Attestation Provider of a SUA attestation SHALL NOT issue such an attestation to a Wallet Unit that does not comply with all relevant requirements in the Attestation Rulebook for that attestation.
- **SUA_04**: In the response to a presentation request that includes transactional data, a Wallet Unit SHALL include (a representation of) that data, according to requirements included in the Attestation Rulebook or in information provided to the Wallet Unit in the presentation request. In the latter case, the rules to interpret such information SHALL be included in the Attestation Rulebook. *Note: This requirement, as well as SUA_05, only applies if the requested SUA attestation is present on the Wallet Unit and if the User consents to signing the transactional data and presenting the requested attributes.
- **SUA_05**: The Wallet Unit SHALL include (a representation of) the transactional data received in a presentation request in the signature creation process used for device binding, using the private key of the requested SUA attestation, using the mechanisms provided for key binding in [SD-JWT-VC] and mdoc authentication in [ISO/IEC 18013-5], and complying with the applicable requirements in the Attestation Rulebook, see SUA_02. *Note: a) The resulting signature value constitutes a proof of transaction and fulfils the requirement of the authentication code required in [PSD2]. b) See also requirement OIA_02 in [Topic 1](./annex-2.02-high-level-requirements-by-topic.md#a231-topic-1---accessing-online-services-with-a-wallet-unit).
- **SUA_06**: The Wallet Unit SHALL be able to adapt the dialogue message(s) displayed to the User (like font size and colour, background colour, text position, labels in the buttons to 'approve' or 'reject' a transaction), according to requirements in an Attestation Rulebook or in information provided to the Wallet Unit in the presentation request. In the latter case, the rules to interpret such information SHALL be included in the Attestation Rulebook.

### ❌ Requirements removed in ARF 2.7.3 (1):

- **In the response to a presentation request that includes transactional data, a Wallet Unit SHALL include (a representation of) that data, according to requirements included in the Attestation Rulebook or in information provided to the Wallet Unit in the presentation request. In the latter case, the rules to interpret such information SHALL be included in the Attestation Rulebook. *Note: This requirement, as well as SUA_05, only applies if the requested SUA attestation is present on the Wallet Unit and if the User consents to signing the transactional data and presenting the requested attributes.**: 

**Total requirements ARF 2.7.3:** 6
**Total requirements ARF 2.5.0:** 1
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


### ✅ Requirements added in ARF 2.7.3 (4):

- **SUA_01**: The Wallet Units SHALL be able to process the transactional data included in a presentation request for that an attestation, according to all requirements in the associated Attestation Rulebook.
- **SUA_03**: The Attestation Provider of a SUA attestation SHALL NOT issue such an attestation to a Wallet Unit that does not comply with all relevant requirements in the Attestation Rulebook for that attestation.
- **SUA_04**: In the response to a presentation request that includes transactional data, a Wallet Unit SHALL include (a representation of) that data, according to requirements included in the Attestation Rulebook or in information provided to the Wallet Unit in the presentation request. In the latter case, the rules to interpret such information SHALL be included in the Attestation Rulebook. *Note: This requirement, as well as SUA_05, only applies if the requested SUA attestation is present on the Wallet Unit and if the User consents to signing the transactional data and presenting the requested attributes.
- **SUA_06**: The Wallet Unit SHALL be able to adapt the dialogue message(s) displayed to the User (like font size and colour, background colour, text position, labels in the buttons to 'approve' or 'reject' a transaction), according to requirements in an Attestation Rulebook or in information provided to the Wallet Unit in the presentation request. In the latter case, the rules to interpret such information SHALL be included in the Attestation Rulebook.

### ❌ Requirements removed in ARF 2.7.3 (1):

- **In the response to a presentation request that includes transactional data, a Wallet Unit SHALL include (a representation of) that data, according to requirements included in the Attestation Rulebook or in information provided to the Wallet Unit in the presentation request. In the latter case, the rules to interpret such information SHALL be included in the Attestation Rulebook. *Note: This requirement, as well as SUA_05, only applies if the requested SUA attestation is present on the Wallet Unit and if the User consents to signing the transactional data and presenting the requested attributes.**:


### ✅ Requirements added in ARF 2.7.3 (4):

- **SUA_01**: The Wallet Units SHALL be able to process the transactional data included in a presentation request for that an attestation, according to all requirements in the associated Attestation Rulebook.
- **SUA_03**: The Attestation Provider of a SUA attestation SHALL NOT issue such an attestation to a Wallet Unit that does not comply with all relevant requirements in the Attestation Rulebook for that attestation.
- **SUA_04**: In the response to a presentation request that includes transactional data, a Wallet Unit SHALL include (a representation of) that data, according to requirements included in the Attestation Rulebook or in information provided to the Wallet Unit in the presentation request. In the latter case, the rules to interpret such information SHALL be included in the Attestation Rulebook. *Note: This requirement, as well as SUA_05, only applies if the requested SUA attestation is present on the Wallet Unit and if the User consents to signing the transactional data and presenting the requested attributes.
- **SUA_06**: The Wallet Unit SHALL be able to adapt the dialogue message(s) displayed to the User (like font size and colour, background colour, text position, labels in the buttons to 'approve' or 'reject' a transaction), according to requirements in an Attestation Rulebook or in information provided to the Wallet Unit in the presentation request. In the latter case, the rules to interpret such information SHALL be included in the Attestation Rulebook.

### ❌ Requirements removed in ARF 2.7.3 (1):

- **In the response to a presentation request that includes transactional data, a Wallet Unit SHALL include (a representation of) that data, according to requirements included in the Attestation Rulebook or in information provided to the Wallet Unit in the presentation request. In the latter case, the rules to interpret such information SHALL be included in the Attestation Rulebook. *Note: This requirement, as well as SUA_05, only applies if the requested SUA attestation is present on the Wallet Unit and if the User consents to signing the transactional data and presenting the requested attributes.**:


### ✅ Requirements added in ARF 2.7.3 (4):

- **SUA_01**: The Wallet Units SHALL be able to process the transactional data included in a presentation request for that an attestation, according to all requirements in the associated Attestation Rulebook.
- **SUA_03**: The Attestation Provider of a SUA attestation SHALL NOT issue such an attestation to a Wallet Unit that does not comply with all relevant requirements in the Attestation Rulebook for that attestation.
- **SUA_04**: In the response to a presentation request that includes transactional data, a Wallet Unit SHALL include (a representation of) that data, according to requirements included in the Attestation Rulebook or in information provided to the Wallet Unit in the presentation request. In the latter case, the rules to interpret such information SHALL be included in the Attestation Rulebook. *Note: This requirement, as well as SUA_05, only applies if the requested SUA attestation is present on the Wallet Unit and if the User consents to signing the transactional data and presenting the requested attributes.
- **SUA_06**: The Wallet Unit SHALL be able to adapt the dialogue message(s) displayed to the User (like font size and colour, background colour, text position, labels in the buttons to 'approve' or 'reject' a transaction), according to requirements in an Attestation Rulebook or in information provided to the Wallet Unit in the presentation request. In the latter case, the rules to interpret such information SHALL be included in the Attestation Rulebook.

### ❌ Requirements removed in ARF 2.7.3 (1):

- **In the response to a presentation request that includes transactional data, a Wallet Unit SHALL include (a representation of) that data, according to requirements included in the Attestation Rulebook or in information provided to the Wallet Unit in the presentation request. In the latter case, the rules to interpret such information SHALL be included in the Attestation Rulebook. *Note: This requirement, as well as SUA_05, only applies if the requested SUA attestation is present on the Wallet Unit and if the User consents to signing the transactional data and presenting the requested attributes.**:


### ✅ Requirements added in ARF 2.7.3 (4):

- **SUA_01**: The Wallet Units SHALL be able to process the transactional data included in a presentation request for that an attestation, according to all requirements in the associated Attestation Rulebook.
- **SUA_03**: The Attestation Provider of a SUA attestation SHALL NOT issue such an attestation to a Wallet Unit that does not comply with all relevant requirements in the Attestation Rulebook for that attestation.
- **SUA_04**: In the response to a presentation request that includes transactional data, a Wallet Unit SHALL include (a representation of) that data, according to requirements included in the Attestation Rulebook or in information provided to the Wallet Unit in the presentation request. In the latter case, the rules to interpret such information SHALL be included in the Attestation Rulebook. *Note: This requirement, as well as SUA_05, only applies if the requested SUA attestation is present on the Wallet Unit and if the User consents to signing the transactional data and presenting the requested attributes.
- **SUA_06**: The Wallet Unit SHALL be able to adapt the dialogue message(s) displayed to the User (like font size and colour, background colour, text position, labels in the buttons to 'approve' or 'reject' a transaction), according to requirements in an Attestation Rulebook or in information provided to the Wallet Unit in the presentation request. In the latter case, the rules to interpret such information SHALL be included in the Attestation Rulebook.

### ❌ Requirements removed in ARF 2.7.3 (1):

- **In the response to a presentation request that includes transactional data, a Wallet Unit SHALL include (a representation of) that data, according to requirements included in the Attestation Rulebook or in information provided to the Wallet Unit in the presentation request. In the latter case, the rules to interpret such information SHALL be included in the Attestation Rulebook. *Note: This requirement, as well as SUA_05, only applies if the requested SUA attestation is present on the Wallet Unit and if the User consents to signing the transactional data and presenting the requested attributes.**:


### ✅ Requirements added in ARF 2.7.3 (4):

- **SUA_01**: The Wallet Units SHALL be able to process the transactional data included in a presentation request for that an attestation, according to all requirements in the associated Attestation Rulebook.
- **SUA_03**: The Attestation Provider of a SUA attestation SHALL NOT issue such an attestation to a Wallet Unit that does not comply with all relevant requirements in the Attestation Rulebook for that attestation.
- **SUA_04**: In the response to a presentation request that includes transactional data, a Wallet Unit SHALL include (a representation of) that data, according to requirements included in the Attestation Rulebook or in information provided to the Wallet Unit in the presentation request. In the latter case, the rules to interpret such information SHALL be included in the Attestation Rulebook. *Note: This requirement, as well as SUA_05, only applies if the requested SUA attestation is present on the Wallet Unit and if the User consents to signing the transactional data and presenting the requested attributes.
- **SUA_06**: The Wallet Unit SHALL be able to adapt the dialogue message(s) displayed to the User (like font size and colour, background colour, text position, labels in the buttons to 'approve' or 'reject' a transaction), according to requirements in an Attestation Rulebook or in information provided to the Wallet Unit in the presentation request. In the latter case, the rules to interpret such information SHALL be included in the Attestation Rulebook.

### ❌ Requirements removed in ARF 2.7.3 (1):

- **In the response to a presentation request that includes transactional data, a Wallet Unit SHALL include (a representation of) that data, according to requirements included in the Attestation Rulebook or in information provided to the Wallet Unit in the presentation request. In the latter case, the rules to interpret such information SHALL be included in the Attestation Rulebook. *Note: This requirement, as well as SUA_05, only applies if the requested SUA attestation is present on the Wallet Unit and if the User consents to signing the transactional data and presenting the requested attributes.**:

## Diff ARF 2.5.0 → ARF 2.7.3

### ✅ Requirements added in ARF 2.7.3 (6):

- **SUA_01**: The Wallet Units SHALL be able to process the transactional data included in a presentation request for that an attestation, according to all requirements in the associated Attestation Rulebook.
- **SUA_02**: The Attestation Rulebook (see [Topic 12](./annex-2.02-high-level-requirements-by-topic.md#a239-topic-12---attestation-rulebooks) of a SUA attestation SHALL specify the syntax and semantics of the transactional data associated with that attestation, as well as all necessary requirements for Wallet Units to process that transactional data, at least regarding a) displaying the data to the User when obtaining consent for signing the data, b) processing (e.g., hashing) the data for inclusion in the device binding signature, and c) the scope of information to be logged about a SUA attestation presentation transaction by a Wallet Unit.
- **SUA_03**: The Attestation Provider of a SUA attestation SHALL NOT issue such an attestation to a Wallet Unit that does not comply with all relevant requirements in the Attestation Rulebook for that attestation.
- **SUA_04**: In the response to a presentation request that includes transactional data, a Wallet Unit SHALL include (a representation of) that data, according to requirements included in the Attestation Rulebook or in information provided to the Wallet Unit in the presentation request. In the latter case, the rules to interpret such information SHALL be included in the Attestation Rulebook. *Note: This requirement, as well as SUA_05, only applies if the requested SUA attestation is present on the Wallet Unit and if the User consents to signing the transactional data and presenting the requested attributes.
- **SUA_05**: The Wallet Unit SHALL include (a representation of) the transactional data received in a presentation request in the signature creation process used for device binding, using the private key of the requested SUA attestation, using the mechanisms provided for key binding in [SD-JWT-VC] and mdoc authentication in [ISO/IEC 18013-5], and complying with the applicable requirements in the Attestation Rulebook, see SUA_02. *Note: a) The resulting signature value constitutes a proof of transaction and fulfils the requirement of the authentication code required in [PSD2]. b) See also requirement OIA_02 in [Topic 1](./annex-2.02-high-level-requirements-by-topic.md#a231-topic-1---accessing-online-services-with-a-wallet-unit).
- **SUA_06**: The Wallet Unit SHALL be able to adapt the dialogue message(s) displayed to the User (like font size and colour, background colour, text position, labels in the buttons to 'approve' or 'reject' a transaction), according to requirements in an Attestation Rulebook or in information provided to the Wallet Unit in the presentation request. In the latter case, the rules to interpret such information SHALL be included in the Attestation Rulebook.

### ❌ Requirements removed in ARF 2.7.3 (1):

- **In the response to a presentation request that includes transactional data, a Wallet Unit SHALL include (a representation of) that data, according to requirements included in the Attestation Rulebook or in information provided to the Wallet Unit in the presentation request. In the latter case, the rules to interpret such information SHALL be included in the Attestation Rulebook. *Note: This requirement, as well as SUA_05, only applies if the requested SUA attestation is present on the Wallet Unit and if the User consents to signing the transactional data and presenting the requested attributes.**: 


| **Index** | **Requirement specification** | **IT-Wallet Mapping & Documentation** |
|---------|------------------|-----------------------------------|
| SUA_01 | The Wallet Units SHALL be able to process the transactional data included in a presentation request for that an attestation, according to all requirements in the associated Attestation Rulebook. |  |
| SUA_02 | The Attestation Rulebook (see [Topic 12](./annex-2.02-high-level-requirements-by-topic.md#a239-topic-12---attestation-rulebooks) of a SUA attestation SHALL specify the syntax and semantics of the transactional data associated with that attestation, as well as all necessary requirements for Wallet Units to process that transactional data, at least regarding a) displaying the data to the User when obtaining consent for signing the data, b) processing (e.g., hashing) the data for inclusion in the device binding signature, and c) the scope of information to be logged about a SUA attestation presentation transaction by a Wallet Unit. |  |
| SUA_03 | The Attestation Provider of a SUA attestation SHALL NOT issue such an attestation to a Wallet Unit that does not comply with all relevant requirements in the Attestation Rulebook for that attestation. |  |
| SUA_04 | In the response to a presentation request that includes transactional data, a Wallet Unit SHALL include (a representation of) that data, according to requirements included in the Attestation Rulebook or in information provided to the Wallet Unit in the presentation request. In the latter case, the rules to interpret such information SHALL be included in the Attestation Rulebook. *Note: This requirement, as well as SUA_05, only applies if the requested SUA attestation is present on the Wallet Unit and if the User consents to signing the transactional data and presenting the requested attributes. |  |
| SUA_05 | The Wallet Unit SHALL include (a representation of) the transactional data received in a presentation request in the signature creation process used for device binding, using the private key of the requested SUA attestation, using the mechanisms provided for key binding in [SD-JWT-VC] and mdoc authentication in [ISO/IEC 18013-5], and complying with the applicable requirements in the Attestation Rulebook, see SUA_02. *Note: a) The resulting signature value constitutes a proof of transaction and fulfils the requirement of the authentication code required in [PSD2]. b) See also requirement OIA_02 in [Topic 1](./annex-2.02-high-level-requirements-by-topic.md#a231-topic-1---accessing-online-services-with-a-wallet-unit). |  |
| SUA_06 | The Wallet Unit SHALL be able to adapt the dialogue message(s) displayed to the User (like font size and colour, background colour, text position, labels in the buttons to 'approve' or 'reject' a transaction), according to requirements in an Attestation Rulebook or in information provided to the Wallet Unit in the presentation request. In the latter case, the rules to interpret such information SHALL be included in the Attestation Rulebook. |  |

---

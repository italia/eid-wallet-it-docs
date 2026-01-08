# Preview: Issue #691 - 🟧🟡 ARF HLR Topic 27 - Registration of PID Providers, Providers of QEAAs, PuB-EAAs, and non-qualified EAAs, and Relying Parties

**Topic:** Topic 27 - Registration of PID Providers, Providers of QEAAs, PuB-EAAs, and non-qualified EAAs, and Relying Parties

**Requirements ARF 2.5.0:** 37
**Requirements ARF 2.7.3:** 37

---

## Diff ARF 2.5.0 → ARF 2.7.3

### ℹ️ No changes detected

The requirements are identical between ARF 2.5.0 and ARF 2.7.3.

**Total requirements ARF 2.7.3:** 37
**Total requirements ARF 2.5.0:** 37
---

## Nuovo body completo della issue:

# Reg Requirements - Changelog

**ARF VERSION:**  
UPDATED TO ARF 2.7.3.

Please refer to the "Summary of Changes" section and subsequent sections to see what has changed from ARF 2.5.0 to ARF 2.7.3.

---

Legend:
- ~~Strikethrough text~~ = Removed or modified content
- **Bold text [NEW]** = New or added content
- **Bold text [MODIFIED]** = Modified content

---

## A. General requirements for Member State registration processes


### ❌ Requirements removed in ARF 2.7.3 (1):

- **Reg_13**: The common Certificate Policy mentioned in Reg_12 SHALL require that an Access Certificate Authority logs all issued certificates for Certificate Transparency (CT). ***Note: This requirement is still under discussion and might be changed or removed in a future version of this ARF. [NEW]

### 🔄 Requirements modified in ARF 2.7.3 (1):

- **Reg_11**:
  - **Old:** ...cate Authority. [NEW]
  - **New:** ...cate Authority.

## Diff ARF 2.5.0 → ARF 2.7.3

### ℹ️ No changes detected

The requirements are identical between ARF 2.5.0 and ARF 2.7.3.


| Status | **Index** | **Requirement specification** | **IT-Wallet Mapping & Documentation** |
|---|---------|------------------|-----------------------------------|
| 🟡 | Reg_01 | Member States SHALL provide processes and mechanisms for PID Providers, QEAA Providers, PuB-EAA Providers, non-qualified EAA Providers, and Relying Parties to register in a registry. *Note: Member States may choose to implement a single registry for all these roles, or a separate registry for each of these roles. | Pending: Not yet established, planned at EU/Member State level. |
| 🟡 | Reg_01a | Member States SHALL register a common set of data about a) PID Providers, b) QEAA Providers, c) PuB-EAA Providers, d) non-qualified EAA Providers. and e) Relying Parties, according to the relevant requirements in [Technical Specification 6](../../technical-specifications/ts6-common-set-of-rp-information-to-be-registered.md). *Note: For PID Providers, QEAA Providers, PuB-EAA Providers, and non-qualified EAA Providers, the common set of data specified in [Technical Specification 6] include the attestation type(s) that the provider intends to issue to Wallet Units. |  |
| 🟡 | Reg_01b | Empty |  |
| 🟧🟡 | Reg_02 | Member States SHALL make publicly available all necessary details and documentation about the registration processes for their registry. | Pending: Not yet established, planned at EU/Member State level. |
| 🟧🟡 | Reg_03 | Member States SHALL publish the registry entries online, in a sealed or signed machine-readable common format suitable for automated processing, according to the relevant requirements in [Technical Specification 5](../../technical-specifications/ts5-common-formats-and-api-for-rp-registration-information.md), for the purpose of transparency to Users and other stakeholders. | Pending: Not yet established, planned at EU/Member State level. |
| 🟧🟡 | Reg_04 | Member States SHALL make the registry entries available online, in a human-readable format. The website used for this purpose SHALL use a secure channel protecting the authenticity and integrity of the information in the registry during transport. Member States SHALL NOT require authentication or prior registration and authorisation of any person wishing to retrieve the information in the registry. |  |
| 🟡 | Reg_05 | Empty | Pending: Not yet established, planned at EU level. |
| 🟡 | Reg_06 | Member States SHALL support the common API specified in [Technical Specification 5](../../technical-specifications/ts5-common-formats-and-api-for-rp-registration-information.md) for to enable automated retrieval of registry entries from the Member States' registries. *Note: [Technical Specification 5] specifies the use of a secure channel protecting the authenticity and integrity of the information in the registry during transport, and does not require authentication or prior registration and authorisation of any entity wishing to retrieve the information in the registry. |  |
| 🟡 | Reg_07 | A Member State SHALL enable a registered PID Provider, QEAA Provider, PuB-EAA Provider, non-qualified EAA Provider, or Relying Party to update the information registered on it, using a process comparable to the original registration process. For Relying Parties, this SHALL be possible using the API or user interface mentioned in Reg_24. |  |
| 🟡 | Reg_08 | A registered PID Provider, QEAA Provider, PuB-EAA Provider, non-qualified EAA Provider, or Relying Party SHALL make any updates necessary to ensure the continued correctness of the registered information without undue delay. |  |
| 🟡 | Reg_09 | Member States SHALL log all changes made on the information registered regarding a PID Provider, QEAA Provider, PuB-EAA Provider, non-qualified EAA Provider, or Relying Party, including at least initial registration, updates, deletion of information, and suspension or cancellation. |  |
| 🟡 | Reg_11 | A Member State SHALL ensure that the issuance process of access certificates by their notified Access Certificate Authority(s) complies with a common Certificate Policy for Access Certificate Authority. |  |
| 🟡 | Reg_12 | The Commission SHALL provide technical specifications establishing the common Access Certificate Authority Certificate Policy mentioned in Reg_11. | Pending: Not yet established, planned at EU level. |
| 🟡 | Reg_14 | The common Certificate Policy mentioned in Reg_12 SHALL require that an Access Certificate Authority provides one or more method(s) to revoke the access certificates it issued. | Pending: Not yet established, planned at EU level. |
| 🟡 | Reg_15 | The common Certificate Policy mentioned in Reg_12 SHALL include a policy for revocation, which SHALL require that an Access Certificate Authority revokes an access certificate at least when: - the certificate subject which is a Relying Party is suspended or cancelled by the respective Registrar, - the certificate subject which is a PID Provider, QEAA Provider, PuB-EAA Provider, or non-qualified EAA Provider is suspended or cancelled by the respective Registrar, - on request of the certificate subject, or - on request of a competent national authority. | Pending: Not yet established, planned at EU level. |
| 🟡 | Reg_16 | The common Certificate Policy mentioned in Reg_12 SHALL specify the profile of access certificates in detail. | Pending: Not yet established, planned at EU level. |
| 🟡 | Reg_17 | Empty | Pending: Not yet established, planned at EU level. |
| 🟡 | Reg_18 | The common Certificate Policy mentioned in Reg_12 SHALL define the minimum change history information to be stored for resolving possible disputes regarding registration. | Pending: Not yet established, planned at EU level. |
| 🟡 | Reg_19 | A Member State SHALL approve a PID Provider according to a well-defined policy before including it in its PID Provider Registry. To that end, a Member State SHALL define specific vetting processes and rules of acceptance for inclusion of PID Providers in its Registry. |  |
| 🟡 | Reg_20 | A Member State SHALL identify PID Providers at a level of confidence proportionate to the risk arising from the potential harm a fraudulent PID Provider could cause to Users and other stakeholders in the EUDI Wallet ecosystem. |  |
| 🟡 | Reg_20a | A Registrar SHALL provide a method to suspend or cancel a registered PID Provider. |  |
| 🟡 | Reg_20b | A Registrar SHALL have a policy for the suspension or cancellation of a registered PID Provider, which SHALL specify that a PID Provider is suspended or cancelled at least on request of the PID Provider or of a competent national authority. |  |
| 🟡 | Reg_21 | A Member State SHALL approve an Attestation Provider according to a well-defined policy before including it in its Attestation Provider Registry. To that end, a Member State SHALL define specific vetting processes and rules of acceptance for inclusion of Attestation Providers in its Registry. These processes and rules SHOULD consider any relevant differences between QEAA Providers, PuB-EAA Providers, and non-qualified EAA Providers. |  |
| 🟡 | Reg_22 | A Member State SHALL identify Attestation Providers (i.e., QEAA Providers, PuB-EAA Providers and non-qualified EAA Providers) at a level of confidence proportionate to the risk arising from the potential harm a fraudulent Attestation Provider could cause to Users and other stakeholders in the EUDI Wallet ecosystem. |  |
| 🟡 | Reg_22a | A Registrar SHALL provide a method to suspend or cancel a registered Attestation Provider. |  |
| 🟡 | Reg_22b | A Registrar SHALL have a policy for the suspension or cancellation of a registered Attestation Provider, which SHALL specify that an Attestation Provider is suspended or cancelled at least on request of the Attestation Provider or of a competent national authority. |  |
| 🟡 | Reg_23 | Empty |  |
| 🟡 | Reg_24 | A Member State SHALL enable a Relying Party to register remotely, using an API or user interface. |  |
| 🟡 | Reg_25 | A Member State SHALL identify a Relying Party at a level of confidence proportionate to the risk arising from the potential harm a fraudulent Relying Party could cause to Users and other stakeholders in the EUDI Wallet ecosystem. |  |
| 🟡 | Reg_26 | With respect to Reg_25, a Member State SHALL consider whether a registering entity intends to act as an intermediary. *Note: According to the [European Digital Identity Regulation], an intermediary is a Relying Party. |  |
| 🟡 | Reg_27 | Empty |  |
| 🟡 | Reg_28 | Empty |  |
| 🟡 | Reg_29 | A Member State SHALL have a policy for the cancellation of a registered Relying Party, which SHALL specify that a Relying Party is cancelled at least on request of the Relying Party or of a competent national authority. |  |
| 🟡 | Reg_30 | Empty |  |
| 🟡 | Reg_31 | The common Certificate Policy mentioned in Reg_12 SHALL require that an access certificate contains a name for the PID Provider, QEAA Provider, PuB-EAA Provider, non-qualified EAA Provider, or Relying Party, in a format suitable for presenting to a User. |  |
| 🟡 | Reg_32 | The common Certificate Policy mentioned in Reg_12 SHALL require that an access certificate contains an EU-wide unique identifier for the PID Provider, QEAA Provider, PuB-EAA Provider, non-qualified EAA Provider, or Relying Party, and SHALL specify a method for deriving such identifiers. *Note: a) The EU-wide unique identifier could, for example, be a composition of a unique identifier of the Registrar, defined in the policy, and a unique identifier for the Relying Party allocated by this Registrar. b) This Relying Party identifier is identical in all access certificates issued to a given entity. |  |
| 🟡 | Reg_33 | Empty |  |
## C. Requirements for the registration of PID Providers

| **Index** | **Requirement specification** | **IT-Wallet Mapping & Documentation** |
|---|-----------|------------------------------|---------------------------------------|
| 🟡 | Reg_19    | A Member State SHALL approve a PID Provider according to a well-defined policy before including it in its PID Provider Registry. To that end, a Member State SHALL define specific vetting processes and rules of acceptance for inclusion of PID Providers in its Registry. | Pending: Not yet established, planned at Member State level. |
| 🟡 | Reg_20    | A Member State SHALL identify PID Providers at a level of confidence proportionate to the risk arising from the potential harm a fraudulent PID Provider could cause to Users and other stakeholders in the EUDI Wallet ecosystem. | Pending: Not yet established, planned at Member State level. |
| 🟡 | Reg_20a   | A Registrar SHALL provide a method to suspend or cancel a registered PID Provider. | |
| 🟡 | Reg_20b   | A Registrar SHALL have a policy for the suspension or cancellation of a registered PID Provider, which SHALL specify that a PID Provider is suspended or cancelled at least on request of the PID Provider or of a competent national authority. | Pending: Not yet established, planned at Member State level. |

---

## D. Requirements for the registration of Attestation Providers

| **Index** | **Requirement specification** | **IT-Wallet Mapping & Documentation** |
|---|-----------|------------------------------|---------------------------------------|
| 🟡 | Reg_21    | A Member State SHALL approve an Attestation Provider according to a well-defined policy before including it in its Attestation Provider Registry. To that end, a Member State SHALL define specific vetting processes and rules of acceptance for inclusion of Attestation Providers in its Registry. These processes and rules SHOULD consider any relevant differences between QEAA Providers, PuB-EAA Providers, and non-qualified EAA Providers. | Pending: Not yet established, planned at Member State level. |
| 🟡 | Reg_22    | A Member State SHALL identify Attestation Providers (i.e., QEAA Providers, PuB-EAA Providers and non-qualified EAA Providers) at a level of confidence proportionate to the risk arising from the potential harm a fraudulent Attestation Provider could cause to Users and other stakeholders in the EUDI Wallet ecosystem. | Pending: Not yet established, planned at Member State level. |
| 🟡 | Reg_22a   | A Registrar SHALL provide a method to suspend or cancel a registered Attestation Provider. | |
| 🟡 | Reg_22b   | A Registrar SHALL have a policy for the suspension or cancellation of a registered Attestation Provider, which SHALL specify that an Attestation Provider is suspended or cancelled at least on request of ~~the PID Provider~~ **the Attestation Provider [MODIFIED]** or of a competent national authority. | Pending: Not yet established, planned at Member State level. |

---

## E. Requirements for the registration of Relying Parties

| **Index** | **Requirement specification** | **IT-Wallet Mapping & Documentation** |
|---|-----------|------------------------------|---------------------------------------|
| 🟡 | Reg_23    | The Commission SHALL establish a technical specification for a common set of Relying Party information to be registered in Member State registries. This set SHALL include at least the information defined in [European Digital Identity Regulation] [article 5b](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32024R1183#d1e1776-1-1) 2 (c). | Pending: Not yet established, planned at EU level. |
| 🟡 | Reg_24    | A Member State SHALL enable a Relying Party to register remotely, using an API or user interface. | Pending: Not yet established, planned at Member State level. |
| 🟡 | Reg_25    | A Member State SHALL identify a Relying Party at a level of confidence proportionate to the risk arising from the potential harm a fraudulent Relying Party could cause to Users and other stakeholders in the EUDI Wallet ecosystem. | Pending: Not yet established, planned at Member State level. |
| **NEW** | **Reg_26** | **With respect to Reg_25, a Member State SHALL consider whether a registering entity intends to act as an intermediary. [NEW]** ***Note: According to the [European Digital Identity Regulation], an intermediary is a Relying Party. [NEW]*** | **Pending: Not yet established, planned at Member State level.** |
| 🟡 | Reg_27    | ~~Relying Parties SHALL make any updates necessary to ensure the continued correctness of the registered information without undue delay.~~ **Empty [MODIFIED]** | Pending: Not yet established, planned at Member State level. |
| 🟡 | Reg_28    | ~~A Member State's Registry SHALL log all changes made on the information regarding a Relying Party, including at least initial registration, updates, deletion of information, and suspension or cancellation.~~ **Empty [MODIFIED]** | |
| 🟡 | Reg_29    | A ~~Registrar~~ **Member State [MODIFIED]** SHALL have a policy for the cancellation of a registered Relying Party, which SHALL specify that a Relying Party is cancelled at least on request of the Relying Party or of a competent national authority. | |
| 🟡 | Reg_30    | ~~Empty~~ **Empty [NO CHANGE]** |  |

---

## F. Requirements for the contents of access certificates

| **Index** | **Requirement specification** | **IT-Wallet Mapping & Documentation** |
|---|-----------|------------------------------|---------------------------------------|
| 🟡 | Reg_31    | The common Certificate Policy mentioned in Reg_12 SHALL require that ~~a Relying Party Instance~~ **an [MODIFIED]** access certificate contains a name for the ~~Relying Party~~ **PID Provider, QEAA Provider, PuB-EAA Provider, non-qualified EAA Provider, or Relying Party [MODIFIED]**, in a format suitable for presenting to a User. | Pending: Not yet established, planned at EU level. |
| 🟡 | Reg_32    | The common Certificate Policy mentioned in Reg_12 SHALL require that ~~a Relying Party Instance~~ **an [MODIFIED]** access certificate contains an EU-wide unique identifier for the ~~Relying Party~~ **PID Provider, QEAA Provider, PuB-EAA Provider, non-qualified EAA Provider, or Relying Party [MODIFIED]**, and SHALL specify a method for deriving such identifiers. *Notes: - ~~The Wallet Instance needs such an identifier at least to send a report of suspicious Relying Party presentation requests to a data protection authority according to [Topic 50](#a2350-topic-50---blueprint-to-report-unlawful-or-suspicious-request-of-data).~~ **[REMOVED]** - The EU-wide unique identifier could, for example, be a composition of a unique identifier of the Registrar, defined in the policy, and a unique identifier for the Relying Party allocated by this Registrar. - This ~~Relying Party~~ **[REMOVED]** identifier is identical in all ~~Relying Party Instance~~ **[REMOVED]** access certificates issued to a given ~~Relying Party~~ **entity [MODIFIED]**.* | |
| **NEW** | **Reg_33** | **The common Certificate Policy mentioned in Reg_12 SHALL require that an access certificate contains the URL of the online service of the Member State Registrar, which Wallet Units and other parties can use to obtain the information registered about the PID Provider, QEAA Provider, PuB-EAA Provider, non-qualified EAA Provider, or Relying Party. [NEW]** | |

---

## Summary of Changes in ARF 2.7.3

### Major Structural Improvements:

1. **Requirements consolidated and generalized**: Previously separate RP-specific requirements (Reg_26, Reg_27, Reg_28) have been consolidated into general requirements (Reg_07, Reg_08, Reg_09) that apply to ALL registered entities

2. **Better organization**: Clear sectioning (A-F) makes it easier to navigate requirements by stakeholder type

### New Requirements:

**Reg_07** [NEW]: General update requirement for all registered entities
- Covers PID Providers, Attestation Providers, AND Relying Parties
- Consolidates and replaces old Reg_26

**Reg_08** [NEW]: General obligation to maintain correct information
- Applies to ALL registered entities
- Consolidates and replaces old Reg_27

**Reg_09** [NEW]: General logging requirement for all changes
- Applies to ALL registered entities  
- Consolidates and replaces old Reg_28

**Reg_11** [NEW]: Member State obligation for Certificate Policy compliance
- Links notified Access Certificate Authorities to common Certificate Policy

**Reg_26** [NEW]: Intermediary consideration requirement
- Member States must consider intermediary status when identifying RPs
- With note clarifying intermediaries are Relying Parties

**Reg_33** [NEW]: URL requirement in access certificates
- Access certificates must contain Registrar's online service URL
- Enables information lookup for Wallet Units and others

### Modified Requirements:

**Reg_01**: Added note on registry architecture flexibility
- Member States can choose single or multiple registries

**Reg_01b, Reg_05**: Changed from "?" to "Empty"
- Clarifies these are intentional placeholders

**Reg_13**: Added cautionary note
- "This requirement is still under discussion and might be changed or removed in a future version"

**Reg_17**: Changed from substantive requirement to "Empty"
- Previously required access certificates to indicate entity type
- Content apparently moved elsewhere or deemed unnecessary

**Reg_22b**: Fixed typo
- Changed "PID Provider" to "Attestation Provider" (correct entity type)

**Reg_27, Reg_28**: Changed to "Empty"
- Content consolidated into new general requirements Reg_07, Reg_08, Reg_09

**Reg_29**: Changed from "Registrar" to "Member State"
- Clarifies responsibility level

**Reg_31**: Broadened scope
- Now applies to ALL entity types, not just Relying Parties
- Changed from "Relying Party Instance access certificate" to "access certificate"

**Reg_32**: Broadened scope and simplified notes
- Now applies to ALL entity types
- Removed RP-specific notes about DPA reporting
- Simplified to generic "entity" instead of "Relying Party"

### Overall Assessment:

The Reg requirements have undergone **significant reorganization and generalization**:

1. **Unified approach**: Requirements now treat PID Providers, Attestation Providers, and Relying Parties more uniformly where appropriate

2. **Better consolidation**: Eliminated redundancy by creating general requirements (Reg_07-09) instead of entity-specific ones

3. **Clearer structure**: Six logical sections (A-F) improve navigability

4. **Enhanced accountability**: New Reg_11 ensures Member States enforce Certificate Policy compliance

5. **Improved traceability**: New Reg_33 provides URL for information lookup

6. **Fixed errors**: Corrected typo in Reg_22b

The changes reflect maturation of the registration framework with emphasis on:
- Consistency across entity types
- Better information accessibility  
- Clearer responsibilities
- Reduced redundancy

These improvements should facilitate implementation by Member States and improve interoperability across the EUDI Wallet ecosystem.

---

# Preview: Issue #719 - ARF HLR Topic 43 - Embedded disclosure policies

**Topic:** Topic 43 - Embedded disclosure policies

**Requirements ARF 2.5.0:** 11
**Requirements ARF 2.7.3:** 11

---

## Diff ARF 2.5.0 → ARF 2.7.3

### ℹ️ No changes detected

The requirements are identical between ARF 2.5.0 and ARF 2.7.3.

**Total requirements ARF 2.7.3:** 11
**Total requirements ARF 2.5.0:** 11
---

## Nuovo body completo della issue:

# Topic 43 - Embedded Disclosure Policies (EDP) - Changelog

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
| 🟧 | EDP_01 | A Wallet Unit SHALL enable an Attestation Provider to optionally express an embedded disclosure policy for a QEAA, PuB-EAA, or non-qualified EAA. *Note: The [European Digital Identity Regulation] does not contain a requirement for PIDs to be able to contain an embedded disclosure policy. |  |
| 🟧 | EDP_02 | A Wallet Unit SHALL support embedded disclosure policies implementing the 'Authorised relying parties only policy' described in Annex III of Implementing Regulation (EU) 2024/2979. If present, such an embedded disclosure policy SHALL contain a list of EU-wide unique identifiers of Relying Parties, as specified in Reg_32. The Wallet Unit SHALL retrieve the Relying Party identifier from the access certificate presented by the Relying Party, and compare it to the list of authorised identifiers in the policy, unless the Relying Party is an intermediary. If the Relying Party is an intermediary, the Wallet Unit SHALL retrieve the unique identifier of the intermediated Relying Party from the presentation request or from the registration certificate of the intermediated Relying Party and compare this identifier to the list of authorised identifiers in the policy. *Note: See RPI_07 for how the Wallet Unit can see if the Relying Party is an intermediary. |  |
| 🟧 | EDP_03 | A Wallet Unit SHALL support embedded disclosure policies implementing the 'Specific root of trust' policy described in Annex III of Implementing Regulation (EU) 2024/2979. If present, such an embedded disclosure policy SHALL contain a list of root or intermediate certificates used for signing Relying Party access certificates. The Wallet Unit SHALL compare the certificate chain that was used to sign the access certificate provided by the Relying Party to the list of authorised root or intermediate certificates in the policy, unless the Relying Party is an intermediary. If the Relying Party is an intermediary, the Wallet Unit SHALL retrieve the root certificate of the Provider of registration certificates of the intermediated Relying Party from the presentation request or from the Registrar's online service (as applicable) and compare this certificate to the list of authorised certificates in the policy. *Note: See RPI_07 for how the Wallet Unit can see if the Relying Party is an intermediary. |  |
| 🟧 | EDP_04 | Empty |  |
| 🟧 | EDP_05 | An embedded disclosure policy SHOULD contain a link to a website of the Attestation Provider explaining the disclosure policy in layman's terms. If this is the case, the Wallet Unit SHALL display the link to the User and allow them to navigate to that website. |  |
| 🟧 | EDP_06 | The Wallet Unit SHALL evaluate an embedded disclosure policy in conjunction with the information received from the requesting Relying Party, in order to determine if the Relying Party has permission from the Attestation Provider to access the requested attestation. |  |
| 🟧 | EDP_07 | The Wallet Unit SHALL enable the User, based on the outcome of the evaluation of the applicable embedded disclosure policy(s), to deny or allow the presentation of the requested attestation to the Relying Party. |  |
| 🟧 | EDP_08 | The Commission SHALL take measures to ensure a technical specification is created establishing common mechanisms for the specification of embedded disclosure policies by Attestation Providers, and for the evaluation of such policies by Wallet Units. |  |
| 🟧 | EDP_09 | An Attestation Provider SHALL include an embedded disclosure policy (if any) by value in the Issuer metadata related to the attestation, in compliance with the [OpenID4VCI] issuance protocol or an extension thereof specified in the technical specification mentioned in EDP_08. |  |
| 🟧 | EDP_10 | During attestation issuance, a Wallet Unit SHALL retrieve and store locally the corresponding embedded disclosure policy, if any. |  |
| 🟧 | EDP_11 | An Attestation Provider SHALL revoke an attestation if a corresponding embedded disclosure policy is added, changed, or deleted. |  |### Analysis of EDP_02 Change:

**Previous approach (two options):**
1. Presentation request
2. Registrar's online service (conditional)

**New approach (two options):**
1. Presentation request
2. Registration certificate of intermediated RP

**Rationale for change:**
- **More direct**: Registration certificate contains RP identifier directly
- **Less dependency**: No need to query Registrar's online service
- **Better performance**: Avoids additional network call
- **More reliable**: Certificate already validated as part of intermediary flow
- **Aligns with Topic 44**: Registration certificates are specifically for this purpose

**Technical implications:**
- Wallet Unit can extract identifier from registration certificate locally
- Faster policy evaluation (no external lookup)
- Consistent with registration certificate framework (Topic 44)

### No Changes to Other Requirements:

All other EDP requirements (EDP_01, 03-11) remain completely unchanged.

### Related Topics:

- **Topic 27** (Registration): Reg_32 defines EU-wide unique identifiers
- **Topic 44** (Registration Certificates): Source for RP identifiers
- **Topic 6** (RP Authentication): RPI_07 defines intermediary detection
- **Annex III, Implementing Regulation (EU) 2024/2979**: Policy types described

---

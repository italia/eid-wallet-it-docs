# Preview: Issue #720 - ARF HLR Topic 44 - Relying Party registration certificates

**Topic:** Topic 44 - Relying Party registration certificates

**Requirements ARF 2.5.0:** 20
**Requirements ARF 2.7.3:** 26

---

## Diff ARF 2.5.0 → ARF 2.7.3

### ✅ Requirements added in ARF 2.7.3 (6):

- **RPRC_06**: The contents of a registration certificate SHALL include a name for the subject of the certificate, in a format suitable for presenting to a User. *Note: A Wallet Unit needs the name of a Relying Party at least when requesting User approval according to [[Topic 6](./annex-2.02-high-level-requirements-by-topic.md#a234-topic-6---relying-party-authentication-and-user-approval)]
- **RPRC_07**: The contents of a registration certificate SHALL include an EU-wide unique identifier for the subject of the certificate. *Note: a) A Wallet Unit needs an identifier for a Relying Party at least to allow the User to send a report of suspicious Relying Party presentation requests to a data protection authority according to [Topic 50](./annex-2.02-high-level-requirements-by-topic.md#a2328-topic-50---blueprint-to-report-unlawful-or-suspicious-request-of-data). b) The EU-wide unique identifier could, for example, be a concatenated list of one or more registered official Relying Party identifiers listed in Annex I(3) of the [CIR 2025/848](https://data.europa.eu/eli/reg_impl/2025/848/oj) regarding registration of Wallet Relying Parties, expressed in the semantic form defined in [ETSI EN 319 412-1] sections 5.1.4 or 5.1.5.
- **RPRC_09**: A Member State Registrar MAY decide that, during the registration process for Relying Parties, as specified in [Topic 27](./annex-2.02-high-level-requirements-by-topic.md#a2316-topic-27---registration-of-pid-providers-providers-of-qeaas-pub-eaas-and-non-qualified-eaas-and-relying-parties), a Provider of registration certificates associated to the Registrar must create and sign or seal one or more registration certificates. If the Registrar decides to do so, the Provider of registration certificates SHALL create and sign or seal a separate registration certificate for each intended use registered by each Relying Party, and issue it to the Relying Party. Each registration certificate SHALL comply with the requirements in the technical specification mentioned in RPRC_02.  *Note: See also [Topic 52](./annex-2.02-high-level-requirements-by-topic.md#a2330-topic-52-relying-party-intermediaries).
- **RPRC_11**: The contents of a registration certificate issued to a Relying Party SHALL at least one of the following: a) the URL of a web form provided by the Relying Party, which Users can use to send data deletion requests, b) an e-mail address of the Relying Party, on which the Relying Party is prepared to receive data deletion requests from Users, c) a telephone number of the Relying Party, on which the Relying Party is prepared to receive data deletion requests from Users. *Note: See [Topic 48](./annex-2.02-high-level-requirements-by-topic.md#a2327-topic-48---blueprint-for-requesting-data-deletion-to-relying-parties) for more information about data deletion requests.
- **RPRC_12**: The contents of a registration certificate issued to a Relying Party SHALL contain the name and country of the Data Protection Authority supervising the Relying Party. In addition, the registration certificate SHALL contain at least one of the following: a) the URL of a web form provided by the DPA, which Users can use to report suspicious attribute presentation requests. c) an e-mail address of the DPA, on which the DPA is prepared to receive reports about suspicious attribute presentation requests from Users, c) a telephone number of the DPA, on which the DPA is prepared to receive reports about suspicious attribute presentation requests from Users. *Note: See [Topic 50](./annex-2.02-high-level-requirements-by-topic.md#a2328-topic-50---blueprint-to-report-unlawful-or-suspicious-request-of-data) for more information about reporting suspicious attribute presentation requests.
- **RPRC_13**: A Registrar MAY decide that, during the registration process for PID Providers, QEAA Providers, PuB-EAA Provider, or non-qualified EAA Providers, as specified in [Topic 27](./annex-2.02-high-level-requirements-by-topic.md#a2316-topic-27---registration-of-pid-providers-providers-of-qeaas-pub-eaas-and-non-qualified-eaas-and-relying-parties), a Provider of registration certificates associated to the Member State Registrar must create and sign or seal a registration certificate and issue it to the registering party. If so, that registration certificate SHALL comply with the requirements in the technical specification mentioned in RPRC_02.

### 🔄 Requirements modified in ARF 2.7.3 (1):

- **RPRC_14**:
  - **Old:** ...a...
  - **New:** ...A...

**Total requirements ARF 2.7.3:** 26
**Total requirements ARF 2.5.0:** 20
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

## Summary of Changes

### Major Reorganization

Topic 44 has been **completely restructured** with requirements renumbered and reorganized into clear sections:

**New Structure:**
- **Section A**: Generic requirements (RPRC_01-08) - apply to all entities
- **Section B**: Issuance to Relying Parties (RPRC_09-12)
- **Section C**: Issuance to PID/Attestation Providers (RPRC_13-15) - **NEW SECTION**
- **Section D**: Presentation/verification for RPs (RPRC_16-21)
- **Section F**: Presentation/verification for PID/Attestation Providers (RPRC_22-23) - **NEW SECTION**

### Scope Expansion

**Previous scope**: Only Relying Parties
**New scope**: Relying Parties + PID Providers + QEAA Providers + PuB-EAA Providers + non-qualified EAA Providers

### Key Changes

1. **Requirements renumbered**: Almost all requirements have different numbers (e.g., old RPRC_10 → new RPRC_01)
2. **Requirements generalized**: Changed from "Relying Party" to "entity" or "subject of certificate" in generic requirements
3. **New sections added**: Sections C and F cover PID/Attestation Provider registration certificates
4. **New requirements**: RPRC_04a (Registrar URL for intermediaries), RPRC_05 (non-RP distinctions), RPRC_13-15 (PID/Attestation Provider issuance), RPRC_19a (fallback without certificate), RPRC_22-23 (PID/Attestation Provider verification)
5. **Terminology changes**: "attribute erasure" → "data deletion" (more user-friendly)
6. **Mandatory behavior**: RPRC_09 changed from "Provider MAY" to "Registrar decides, then Provider MUST"
7. **Enhanced requirements**: RPRC_12 now includes DPA name and country (not just contact info)

### Mapping Examples

- Old RPRC_01 → New RPRC_09 (issuance to RPs)
- Old RPRC_02 → New RPRC_02 (technical spec - generalized)
- Old RPRC_03a → New RPRC_06 (name requirement - generalized)
- Old RPRC_10 → New RPRC_01 (certificate policy - moved to front)

---

## A. Generic Requirements (RPRC_01-08)


### ✅ Requirements added in ARF 2.7.3 (1):

- **RPRC_23**: A Wallet Unit SHALL verify that the type of attestation it wants to request from the PID Provider or Attestation Provider is registered by the relevant Registrar, according to ISSU_24a for PID Providers and ISSU_34a for Attestation Providers. *Note: Unlike for Relying Parties, see RPRC_21, the Wallet Unit always carries out this verification, regardless of the preference of the User set as per RPRC_16.

## Diff ARF 2.5.0 → ARF 2.7.3

### ✅ Requirements added in ARF 2.7.3 (6):

- **RPRC_06**: The contents of a registration certificate SHALL include a name for the subject of the certificate, in a format suitable for presenting to a User. *Note: A Wallet Unit needs the name of a Relying Party at least when requesting User approval according to [[Topic 6](./annex-2.02-high-level-requirements-by-topic.md#a234-topic-6---relying-party-authentication-and-user-approval)]
- **RPRC_07**: The contents of a registration certificate SHALL include an EU-wide unique identifier for the subject of the certificate. *Note: a) A Wallet Unit needs an identifier for a Relying Party at least to allow the User to send a report of suspicious Relying Party presentation requests to a data protection authority according to [Topic 50](./annex-2.02-high-level-requirements-by-topic.md#a2328-topic-50---blueprint-to-report-unlawful-or-suspicious-request-of-data). b) The EU-wide unique identifier could, for example, be a concatenated list of one or more registered official Relying Party identifiers listed in Annex I(3) of the [CIR 2025/848](https://data.europa.eu/eli/reg_impl/2025/848/oj) regarding registration of Wallet Relying Parties, expressed in the semantic form defined in [ETSI EN 319 412-1] sections 5.1.4 or 5.1.5.
- **RPRC_09**: A Member State Registrar MAY decide that, during the registration process for Relying Parties, as specified in [Topic 27](./annex-2.02-high-level-requirements-by-topic.md#a2316-topic-27---registration-of-pid-providers-providers-of-qeaas-pub-eaas-and-non-qualified-eaas-and-relying-parties), a Provider of registration certificates associated to the Registrar must create and sign or seal one or more registration certificates. If the Registrar decides to do so, the Provider of registration certificates SHALL create and sign or seal a separate registration certificate for each intended use registered by each Relying Party, and issue it to the Relying Party. Each registration certificate SHALL comply with the requirements in the technical specification mentioned in RPRC_02.  *Note: See also [Topic 52](./annex-2.02-high-level-requirements-by-topic.md#a2330-topic-52-relying-party-intermediaries).
- **RPRC_11**: The contents of a registration certificate issued to a Relying Party SHALL at least one of the following: a) the URL of a web form provided by the Relying Party, which Users can use to send data deletion requests, b) an e-mail address of the Relying Party, on which the Relying Party is prepared to receive data deletion requests from Users, c) a telephone number of the Relying Party, on which the Relying Party is prepared to receive data deletion requests from Users. *Note: See [Topic 48](./annex-2.02-high-level-requirements-by-topic.md#a2327-topic-48---blueprint-for-requesting-data-deletion-to-relying-parties) for more information about data deletion requests.
- **RPRC_12**: The contents of a registration certificate issued to a Relying Party SHALL contain the name and country of the Data Protection Authority supervising the Relying Party. In addition, the registration certificate SHALL contain at least one of the following: a) the URL of a web form provided by the DPA, which Users can use to report suspicious attribute presentation requests. c) an e-mail address of the DPA, on which the DPA is prepared to receive reports about suspicious attribute presentation requests from Users, c) a telephone number of the DPA, on which the DPA is prepared to receive reports about suspicious attribute presentation requests from Users. *Note: See [Topic 50](./annex-2.02-high-level-requirements-by-topic.md#a2328-topic-50---blueprint-to-report-unlawful-or-suspicious-request-of-data) for more information about reporting suspicious attribute presentation requests.
- **RPRC_13**: A Registrar MAY decide that, during the registration process for PID Providers, QEAA Providers, PuB-EAA Provider, or non-qualified EAA Providers, as specified in [Topic 27](./annex-2.02-high-level-requirements-by-topic.md#a2316-topic-27---registration-of-pid-providers-providers-of-qeaas-pub-eaas-and-non-qualified-eaas-and-relying-parties), a Provider of registration certificates associated to the Member State Registrar must create and sign or seal a registration certificate and issue it to the registering party. If so, that registration certificate SHALL comply with the requirements in the technical specification mentioned in RPRC_02.

### 🔄 Requirements modified in ARF 2.7.3 (1):

- **RPRC_14**:
  - **Old:** ...a...
  - **New:** ...A...


| Status | **ID** | **Requirement specification** | **IT-Wallet Mapping & Documentation** |
|---|---------|------------------|-----------------------------------|
| 🟧 | RPRC_01 | The Commission SHALL provide a technical specification establishing a common Certificate Policy for registration certificates, covering at least management and selection of signing keys, revocation and lifecycle management of registration certificates on individual intended use level. *Note: The technical specification may require the Provider of registration certificates to follow applicable parts of technical standards such as EN 319 401 (for General Policy Requirements for TSPs) and TS 119 461 (for identity proofing of Relying Party representatives). |  |
| 🟧 | RPRC_02 | The Commission SHALL ensure that a technical specification is created, describing at least 1. the contents and format of registration certificates for Relying Parties, see the other requirements in this section below. 2. the signing method(s) used to ensure the authenticity of the registration certificate. 3. the trust infrastructure necessary for signing registration certificates and for verifying these signatures, including the use of Trusted Lists to establish trust in Providers of registration certificates and to distribute their trust anchors to Wallet Units. 4. the method used for binding each registration certificate to the access certificate that will be used in the same presentation request. This binding method SHALL enable a Wallet Unit to verify that the registration certificate is bound to the entity that authenticated itself using the access certificate. The binding method SHALL consider situations in which a Relying Party uses the services of an intermediary (see [Topic 52](./annex-2.02-high-level-requirements-by-topic.md#a2330-topic-52-relying-party-intermediaries)) to connect to the Wallet Unit. 5. whether or not a registration certificate must have a validity period. 6. the method to be used for revocation of registration certificates. Moreover, the technical specification SHALL describe the impact of revocation, especially compared to the impact of revocation of the access certificate(s) of the same entity. |  |
| 🟧 | RPRC_03 | The contents of a registration certificate SHALL include at least the information required in Annex V of the [CIR 2025/848](https://data.europa.eu/eli/reg_impl/2025/848/oj) regarding registration of wallet-relying parties. |  |
| 🟧 | RPRC_04 | If the subject of the registration certificate uses the services of an intermediary (see [Topic 52](./annex-2.02-high-level-requirements-by-topic.md#a2330-topic-52-relying-party-intermediaries)), the 'association to the intermediary' mentioned in Annex I (15) of [CIR 2025/848] SHALL consist of the user-friendly name and unique identifier of this intermediary, as meant in requirements Reg_31 and Reg_32. *Note: This name and identifier are identical to those in the access certificate of the intermediary. |  |
| 🟧 | RPRC_04a | Empty |  |
| 🟧 | RPRC_05 | If the subject of the registration certificate is not a Relying Party (i.e. in the terms of CIR 2025/848, a Service Provider), the certificate SHALL NOT contain the intended use as meant in Annex I (9) and (10) of CIR 2025/848. *Note: A PID Provider or Attestation Provider may request attributes from the Wallet Unit during issuance. If so, it registers as both a Service Provider and an Attestation Provider, and consequently its registration certificate contains its intended use. |  |
| 🟡 | RPRC_06 | The contents of a registration certificate SHALL include a name for the subject of the certificate, in a format suitable for presenting to a User. *Note: A Wallet Unit needs the name of a Relying Party at least when requesting User approval according to [[Topic 6](./annex-2.02-high-level-requirements-by-topic.md#a234-topic-6---relying-party-authentication-and-user-approval)] |  |
| 🟡 | RPRC_07 | The contents of a registration certificate SHALL include an EU-wide unique identifier for the subject of the certificate. *Note: a) A Wallet Unit needs an identifier for a Relying Party at least to allow the User to send a report of suspicious Relying Party presentation requests to a data protection authority according to [Topic 50](./annex-2.02-high-level-requirements-by-topic.md#a2328-topic-50---blueprint-to-report-unlawful-or-suspicious-request-of-data). b) The EU-wide unique identifier could, for example, be a concatenated list of one or more registered official Relying Party identifiers listed in Annex I(3) of the [CIR 2025/848](https://data.europa.eu/eli/reg_impl/2025/848/oj) regarding registration of Wallet Relying Parties, expressed in the semantic form defined in [ETSI EN 319 412-1] sections 5.1.4 or 5.1.5. |  |
| 🟧 | RPRC_08 | The EU-wide unique identifier meant in RPRC_07 SHALL be identical in all registration certificates issued for a given entity. *Note: In case the registration certificates issued to an intermediated Relying Party are held and presented by an intermediary, the entity meant in this requirement is the intermediated Relying Party. An intermediary may obtain and hold registration certificates with a different unique identifier for other intermediated Relying Parties. |  |
| 🟡 | RPRC_09 | A Member State Registrar MAY decide that, during the registration process for Relying Parties, as specified in [Topic 27](./annex-2.02-high-level-requirements-by-topic.md#a2316-topic-27---registration-of-pid-providers-providers-of-qeaas-pub-eaas-and-non-qualified-eaas-and-relying-parties), a Provider of registration certificates associated to the Registrar must create and sign or seal one or more registration certificates. If the Registrar decides to do so, the Provider of registration certificates SHALL create and sign or seal a separate registration certificate for each intended use registered by each Relying Party, and issue it to the Relying Party. Each registration certificate SHALL comply with the requirements in the technical specification mentioned in RPRC_02.  *Note: See also [Topic 52](./annex-2.02-high-level-requirements-by-topic.md#a2330-topic-52-relying-party-intermediaries). |  |
| 🟧 | RPRC_10 | If, during registration, a Relying Party received one or more registration certificates, it SHALL distribute these to all its Relying Party Instances. |  |
| 🟡 | RPRC_11 | The contents of a registration certificate issued to a Relying Party SHALL at least one of the following: a) the URL of a web form provided by the Relying Party, which Users can use to send data deletion requests, b) an e-mail address of the Relying Party, on which the Relying Party is prepared to receive data deletion requests from Users, c) a telephone number of the Relying Party, on which the Relying Party is prepared to receive data deletion requests from Users. *Note: See [Topic 48](./annex-2.02-high-level-requirements-by-topic.md#a2327-topic-48---blueprint-for-requesting-data-deletion-to-relying-parties) for more information about data deletion requests. |  |
| 🟡 | RPRC_12 | The contents of a registration certificate issued to a Relying Party SHALL contain the name and country of the Data Protection Authority supervising the Relying Party. In addition, the registration certificate SHALL contain at least one of the following: a) the URL of a web form provided by the DPA, which Users can use to report suspicious attribute presentation requests. c) an e-mail address of the DPA, on which the DPA is prepared to receive reports about suspicious attribute presentation requests from Users, c) a telephone number of the DPA, on which the DPA is prepared to receive reports about suspicious attribute presentation requests from Users. *Note: See [Topic 50](./annex-2.02-high-level-requirements-by-topic.md#a2328-topic-50---blueprint-to-report-unlawful-or-suspicious-request-of-data) for more information about reporting suspicious attribute presentation requests. |  |
| 🟡 | RPRC_13 | A Registrar MAY decide that, during the registration process for PID Providers, QEAA Providers, PuB-EAA Provider, or non-qualified EAA Providers, as specified in [Topic 27](./annex-2.02-high-level-requirements-by-topic.md#a2316-topic-27---registration-of-pid-providers-providers-of-qeaas-pub-eaas-and-non-qualified-eaas-and-relying-parties), a Provider of registration certificates associated to the Member State Registrar must create and sign or seal a registration certificate and issue it to the registering party. If so, that registration certificate SHALL comply with the requirements in the technical specification mentioned in RPRC_02. |  |
| 🟧 | RPRC_14 | If, during registration, a PID Provider, QEAA Provider, PuB-EAA Provider, or non-qualified EAA Provider received a registration certificate, it SHALL distribute it to all its service supply points. *Note: A service supply point is a system at which a Wallet Unit can start the process of requesting and obtaining a PID or attestation. |  |
| 🟧 | RPRC_15 | The contents of a registration certificate issued to a PID Provider, a QEAA Provider, a PuB-EAA Provider, or a non-qualified EAA Provider SHALL contain the type(s) of attestation that this entity intends to issue to Wallet Units. |  |
| 🟡 | RPRC_16 | Either after receiving a presentation request or as a general User setting, a Wallet Unit SHALL offer the User the possibility to indicate whether the User wants to verify the information registered by the competent Registrar about the Relying Party the User is interacting with. |  |
| 🟡 | RPRC_17 | If the User indicated that they want to verify the information registered about the Relying Party and the Relying Party sent a registration certificate to the Wallet Unit, the Wallet Unit SHALL verify the authenticity and validity of the registration certificate according to the technical specification meant in RPRC_02. If the outcome of the verification is negative, the Wallet Unit SHALL, when asking for User approval according to RPA_07, notify the User that it could not obtain the information registered about the entity. |  |
| 🟡 | RPRC_18 | If the User indicated that they want to verify the information registered about the Relying Party, but the Relying Party did not send a registration certificate to the Wallet Unit, the Wallet Unit SHALL connect to the URL of the online service of the Registrar to obtain this information. If the Wallet Unit cannot connect to this URL or if it cannot verify the authenticity and validity of the registered information, it SHALL, when asking for User approval according to RPA_07, notify the User that it could not obtain the information registered about the Relying Party. *Note: The URL of the Registrar is included in the extension of the presentation request, see RPRC_19a. |  |
| 🟡 | RPRC_19 | If a Relying Party Instance received one or more registration certificates (see RPRC_10), it SHALL include a single registration certificate applicable for its current intended use in each presentation request to a Wallet Unit, according to the applicable standard's extension mentioned in RPRC_20. The registration certificate SHALL be included in the request by value, not by reference. The Relying Party Instance SHALL do so both in proximity and remote presentation flows. *Note:  This ensures that no external requests are necessary to validate the Relying Party. |  |
| 🟡 | RPRC_19a | A Relying Party Instance SHALL include in each presentation request the following information,  according to the applicable standard's extension mentioned in RPRC_20a: a) the user-friendly name of the Relying Party, b)the unique identifier of the Relying Party, c) a User-friendly description of the intended use of the Relying Party, d) the URL of the Registrar of the Relying Party, and e) the identifier of the intended use of the Relying Party. *Note: Including items a) and b) enables the Wallet Unit to show to the User the name of the Relying Party. Including c) enables the Wallet Unit to inform the User about the intended use. Including c) and d) enables the Wallet Unit, if desired by the User, to request from the Registrar the attributes registered by the Relying Party for this intended use, as well as the corresponding privacy policy and other registered information. See [Technical Specification 5](../../technical-specifications/ts5-common-formats-and-api-for-rp-registration-information.md) for the definition of this information. Note that in case the Relying Party Instance is operated by an intermediary, items a) - e) pertain to the intermediated Relying Party, see also RPI_06. |  |
| 🟡 | RPRC_20 | Relying Party Instances and Wallet Units SHALL support the extension for [ISO/IEC 18013-5] or the extension for [OpenID4VP], as specified in ETSI TS 119 472-2 and amended by a CIR in preparation, as applicable, for transferring a single Relying Party registration certificate from a Relying Party Instance to a Wallet Unit. *Note: The correct CIR will be referenced here when it is published. |  |
| 🟡 | RPRC_20a | Relying Party Instances and Wallet Units SHALL support the extension for [ISO/IEC 18013-5] or the extension for [OpenID4VP], as specified in ETSI TS 119 472-2 and amended by a CIR in preparation, as applicable, for transferring the information listed in RPRC_19a from a Relying Party Instance to a Wallet Unit. *Note: The correct CIR will be referenced here when it is published. |  |
| 🟡 | RPRC_21 | If the User indicated that they want to verify the information registered about a Relying Party and the Wallet Unit retrieved this information either from the registration certificate or from the online service of the Registrar (see RPRC_16 - RPRC_18), it SHALL verify that all attributes requested in the presentation request are included in the list of attributes registered by the Registrar. If the outcome of the verification is negative, the Wallet Unit SHALL, when asking for User approval according to RPA_07, notify the User about the requested attributes that the Relying Party did not register. |  |
| 🟡 | RPRC_22 | If a PID Provider or Attestation Provider received a registration certificate (see RPRC_14), it SHALL include the registration certificate in its Issuer metadata used in the common OpenID4VCI protocol referenced in ISSU_01. The registration certificate SHALL be included in the metadata by value, not by reference. *Note: a) This ensures that no external requests are necessary to validate the PID Provider or Attestation Provider, and that issuance transactions are atomic and self-contained. b) See also ISSU_22 - ISSU_22b and ISSU_32 - ISSU_32b. |  |
| 🟡 | RPRC_23 | A Wallet Unit SHALL verify that the type of attestation it wants to request from the PID Provider or Attestation Provider is registered by the relevant Registrar, according to ISSU_24a for PID Providers and ISSU_34a for Attestation Providers. *Note: Unlike for Relying Parties, see RPRC_21, the Wallet Unit always carries out this verification, regardless of the preference of the User set as per RPRC_16. |  |

### 🔄 Modified Requirements in ARF 2.7.3 (1):

- **RPRC_14**:
  - **Old:** ...a...
  - **New:** ...A...

---

## D. Presentation/Verification for RPs (RPRC_16-21)

| **ID**     | **Requirement specification** | **IT-Wallet Mapping & Documentation** |
|---|------------|------------------------------|---------------------------------------|
| 🟧 | RPRC_16    | Either during a presentation transaction or as a general User setting, a Wallet Unit SHALL offer the User the possibility to indicate whether the User wants to verify the information registered by the competent Registrar about the Relying Party the User is interacting with. | |
| 🟧 | RPRC_17    | If the User indicated that they want to verify the information registered about the Relying Party and the Relying Party sent a registration certificate to the Wallet Unit, the Wallet Unit SHALL verify the authenticity and validity of the registration certificate according to the technical specification meant in RPRC_02. If the outcome of the verification is negative, the Wallet Unit SHALL, when asking for User approval according to RPA_07, notify the User that it could not obtain the information registered about the entity. | |
| 🟧 | RPRC_18    | If the User indicated that they want to verify the information registered about the Relying Party, but the Relying Party did not send a registration certificate to the Wallet Unit, the Wallet Unit SHALL connect to the URL of the online service of the Registrar to obtain this information. If the Wallet Unit cannot connect to this URL or if it cannot verify the authenticity and validity of the registered information, it SHALL, when asking for User approval according to RPA_07, notify the User that it could not obtain the information registered about the Relying Party. *Note: If the Relying Party does not use the services of an intermediary, the URL of the Registrar is included in the access certificate received by the Wallet Unit, see Reg_33. If the Relying Party uses an intermediary, this URL is included in the received registration certificate if available (see RPRC_04a) or directly in the presentation request if no registration certificate is available (see RPI_06).* | |
| 🟧 | RPRC_19    | If a Relying Party Instance received one or more registration certificates (see RPRC_10), it SHALL include a single registration certificate applicable for its current intended use in each presentation request to a Wallet Unit, according to the applicable standard's extension mentioned in RPRC_20. The registration certificate SHALL be included in the request by value, not by reference. The Relying Party Instance SHALL do so both in proximity and remote presentation flows. *Note: - This ensures that no external requests are necessary to validate the Relying Party, and that presentation transactions are atomic and self-contained.* | |
| 🟧 | RPRC_19a   | If a Relying Party Instance did not receive a registration certificate, it SHALL include in each presentation request a) a User-friendly description of the Relying Party's intended use, b) the URL of its Registrar, and c) the identifier of the intended use. *Note: including a) enables the Wallet Unit to inform the User about the intended use even in case there is no registration certificate. Including b) and c) enables the Wallet Unit, if desired by the User, to request from the Registrar the attributes registered by the Relying Party for this intended use, as well as the corresponding privacy policy and other registered information. See [Technical Specification 5](../../technical-specifications/ts5-common-formats-and-api-for-rp-registration-information.md) for the definition of this information.*  | |
| 🟧 | RPRC_20    | The Commission SHALL ensure that extensions are specified for [ISO/IEC 18013-5] and for [OpenID4VP], allowing a Relying Party to transfer a single Relying Party registration certificate to a Wallet Unit in a presentation request. These extensions SHALL comply with applicable requirements in these standards. *Note: It must not be possible to include multiple registration certificates in a single presentation request.* | |
| 🟧 | RPRC_21    | If the User indicated that they want to verify the information registered about a Relying Party and the Wallet Unit retrieved this information either from the registration certificate or from the online service of the Registrar (see RPRC_16 - RPRC_18), it SHALL verify that all attributes requested in the presentation request are included in the list of attributes registered by the Registrar. If the outcome of the verification is negative, the Wallet Unit SHALL, when asking for User approval according to RPA_07, notify the User about the requested attributes that the Relying Party did not register. | |

---

## F. Presentation/Verification for PID/Attestation Providers (RPRC_22-23)

| **ID**     | **Requirement specification** | **IT-Wallet Mapping & Documentation** |
|---|------------|------------------------------|---------------------------------------|
| 🟧 | RPRC_22    | If a PID Provider or Attestation Provider received a registration certificate (see RPRC_14), it SHALL include the registration certificate in its Issuer metadata used in the common OpenID4VCI protocol referenced in ISSU_01. The registration certificate SHALL be included in the metadata by value, not by reference. *Notes: - This ensures that no external requests are necessary to validate the PID Provider or Attestation Provider, and that issuance transactions are atomic and self-contained. - See also ISSU_22 - ISSU_22b and ISSU_32 - ISSU_32b.* | |
| 🟧 | RPRC_23    | A Wallet Unit SHALL verify that the type of attestation it wants to request from the PID Provider or Attestation Provider is registered by the Registrar, according to ISSU_24a for PID Providers and ISSU_34a for Attestation Providers. *Note: Unlike for Relying Parties, see RPRC_21, the Wallet Unit always carries out this verification, regardless of the preference of the User set as per RPRC_16.* | |

---

## Overall Assessment

Topic 44 has been **extensively restructured** to support registration certificates for all ecosystem participants, not just Relying Parties. The new organization provides clear separation between generic requirements, entity-specific issuance procedures, and verification mechanisms. Key improvements include better intermediary support, fallback mechanisms when certificates are unavailable, and user-friendly terminology. Almost all requirement numbers have changed, requiring documentation updates across the ecosystem.

---

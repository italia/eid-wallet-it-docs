# Preview: Issue #723 - ARF HLR Topic 51 - PID or attestation deletion

**Topic:** Topic 51 - PID or attestation deletion

**Requirements ARF 2.5.0:** 26
**Requirements ARF 2.7.3:** 28

---

## Diff ARF 2.5.0 → ARF 2.7.3

### ✅ Requirements added in ARF 2.7.3 (2):

- **RPI_01**: An intermediary SHALL register as a Relying Party, in accordance with all requirements in [Topic 27](./annex-2.02-high-level-requirements-by-topic.md#a2316-topic-27---registration-of-pid-providers-providers-of-qeaas-pub-eaas-and-non-qualified-eaas-and-relying-parties), while indicating it intends to act as an intermediary. *Note: a) This implies that an intermediary obtains an access certificate containing its own name and unique Relying Party identifier. b) An intermediary may also obtain a registration certificate according to [Topic 44](./annex-2.02-high-level-requirements-by-topic.md#a2326-topic-44---registration-certificates-for-pid-providers-providers-of-qeaas-pub-eaas-and-non-qualified-eaas-and-relying-parties), but this certificate will not be used for intermediated transactions. c) An entity that registered as an intermediary may also register as a Relying Party in its own capacity. In such a case, it will receive one or more registration certificates for its intended use(s), and will use one of these certificates when interacting with a Wallet Unit.
- **RPI_03**: An intermediary SHALL register each intermediated Relying Party it is acting on behalf of at a Registrar in the Member State where the intermediated Relying Party is established, according all requirements in [Topic 44](./annex-2.02-high-level-requirements-by-topic.md#a2326-topic-44---registration-certificates-for-pid-providers-providers-of-qeaas-pub-eaas-and-non-qualified-eaas-and-relying-parties). If a Provider of registration certificates associated with the Registrar issues registration certificates, the intermediary SHALL receive a registration certificate for each of the registered intended uses of the intermediated Relying Party.

**Total requirements ARF 2.7.3:** 28
**Total requirements ARF 2.5.0:** 26
---

## Nuovo body completo della issue:

# Topic 51 - PID/Attestation Deletion (PAD) - Changelog

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

### ✅ Requirements added in ARF 2.7.3 (2):

- **RPI_01**: An intermediary SHALL register as a Relying Party, in accordance with all requirements in [Topic 27](./annex-2.02-high-level-requirements-by-topic.md#a2316-topic-27---registration-of-pid-providers-providers-of-qeaas-pub-eaas-and-non-qualified-eaas-and-relying-parties), while indicating it intends to act as an intermediary. *Note: a) This implies that an intermediary obtains an access certificate containing its own name and unique Relying Party identifier. b) An intermediary may also obtain a registration certificate according to [Topic 44](./annex-2.02-high-level-requirements-by-topic.md#a2326-topic-44---registration-certificates-for-pid-providers-providers-of-qeaas-pub-eaas-and-non-qualified-eaas-and-relying-parties), but this certificate will not be used for intermediated transactions. c) An entity that registered as an intermediary may also register as a Relying Party in its own capacity. In such a case, it will receive one or more registration certificates for its intended use(s), and will use one of these certificates when interacting with a Wallet Unit.
- **RPI_03**: An intermediary SHALL register each intermediated Relying Party it is acting on behalf of at a Registrar in the Member State where the intermediated Relying Party is established, according all requirements in [Topic 44](./annex-2.02-high-level-requirements-by-topic.md#a2326-topic-44---registration-certificates-for-pid-providers-providers-of-qeaas-pub-eaas-and-non-qualified-eaas-and-relying-parties). If a Provider of registration certificates associated with the Registrar issues registration certificates, the intermediary SHALL receive a registration certificate for each of the registered intended uses of the intermediated Relying Party.


| Status | **ID** | **Requirement specification** | **IT-Wallet Mapping & Documentation** |
|---|---------|------------------|-----------------------------------|
| 🟧 | PAD_01 | A Wallet Unit SHALL at any time enable the User to delete any PID or attestation from their Wallet Unit. |  |
| 🟡 | PAD_02 | If the User indicates that a PID or attestation must be deleted, and the Wallet Unit contains multiple PIDs or attestation having the corresponding attestation type and Provider, a Wallet Unit SHALL delete all of these PIDs and attestations simultaneously. *Note: This situation may occur if the PID Provider or Attestation Provider issued a batch of attestations to the Wallet Unit, rather than a single one. |  |
| 🟧 | PAD_03 | If the Wallet Unit deletes a PID or attestation on the User's request, the Wallet Unit SHALL NOT notify the respective PID Provider or Attestation Provider. *Note: This is a matter of User privacy. |  |
| 🟧 | PAD_04 | If the Wallet Unit deletes a PID or device-bound attestation on the User's request, the Wallet Unit SHALL ensure that all cryptographic assets in the WSCA/WSCD related to this PID, or in a keystore related to this attestation, are securely destroyed. *Note: Key deletion for a PID key is a cryptographic key operation and requires User authentication, as specified in requirement WIAM_14. |  |
| 🟧 | PAD_05 | If a Wallet Unit supports the [W3C Digital Credentials API] and it deletes, on the User's request, a PID or attestation previously disclosed to the Digital Credentials API framework, the Wallet Instance SHALL disclose the fact that it no longer stores this PID or attestation to the Digital Credentials API framework. |  |
| 🟡 | PAD_06 | If the User uninstalls the Wallet Instance, the Wallet Instance SHALL request the associated WSCA/WSCD and keystore(s) to delete all cryptographic assets related to the Wallet Unit and to all PIDs and device-bound attestations on the Wallet Unit, if the WSCA/WSCD and keystore(s) are connected to the User device at the moment the Wallet Instance is uninstalled. *Note: It may happen there is no connection to the WSCA/WSCD or to a keystore at the moment the User uninstalls the Wallet Instance; for instance, in case the WSCA/WSCD is an external smart card and the User does not present that card to the User device. Another example occurs when the WSCA/WSCD is a remote HSM and the User device is offline at the moment the User uninstalls the Wallet Instance. In such cases, the cryptographic assets will probably remain present on the WSCA/WSCD or on the keystore, even though they will never be used again. If needed, it is up to the Wallet Provider to define how the Wallet Unit should handle such situations. For example, an HSM manager could address such cases by deciding to delete cryptographic keys in the HSM that are too old or haven't been used for too long, while being aware of the risks in doing so. |  |
| 🟡 | RPI_01 | An intermediary SHALL register as a Relying Party, in accordance with all requirements in [Topic 27](./annex-2.02-high-level-requirements-by-topic.md#a2316-topic-27---registration-of-pid-providers-providers-of-qeaas-pub-eaas-and-non-qualified-eaas-and-relying-parties), while indicating it intends to act as an intermediary. *Note: a) This implies that an intermediary obtains an access certificate containing its own name and unique Relying Party identifier. b) An intermediary may also obtain a registration certificate according to [Topic 44](./annex-2.02-high-level-requirements-by-topic.md#a2326-topic-44---registration-certificates-for-pid-providers-providers-of-qeaas-pub-eaas-and-non-qualified-eaas-and-relying-parties), but this certificate will not be used for intermediated transactions. c) An entity that registered as an intermediary may also register as a Relying Party in its own capacity. In such a case, it will receive one or more registration certificates for its intended use(s), and will use one of these certificates when interacting with a Wallet Unit. |  |
| 🟡 | RPI_02 | Empty |  |
| 🟡 | RPI_03 | An intermediary SHALL register each intermediated Relying Party it is acting on behalf of at a Registrar in the Member State where the intermediated Relying Party is established, according all requirements in [Topic 44](./annex-2.02-high-level-requirements-by-topic.md#a2326-topic-44---registration-certificates-for-pid-providers-providers-of-qeaas-pub-eaas-and-non-qualified-eaas-and-relying-parties). If a Provider of registration certificates associated with the Registrar issues registration certificates, the intermediary SHALL receive a registration certificate for each of the registered intended uses of the intermediated Relying Party. |  |
| 🟡 | RPI_04 | When registering an intermediated Relying Party, an intermediary SHALL provide legally valid evidence that this Relying Party will indeed use the services of this intermediary to interact with Wallet Units. The Registrar SHALL verify this evidence, and, if it is found to be correct, SHALL register the relationship between the intermediary and the intermediated Relying Party. *Note: Such evidence may, for instance, be a contract between the intermediary and the intermediated Relying Party. |  |
| 🟡 | RPI_05 | When an intermediated Relying Party asks its intermediary to request some attributes from a Wallet Unit, it SHALL specify  a) its user-friendly name, b) its unique identifier, c) the URL of its Registrar. d) the identifier of its intended use, e) a User-friendly description of its intended use. In addition, if the intermediated Relying Party has registration certificates, it SHALL indicate which single registration certificate the intermediary must include in the presentation request. *Note: a) See RPRC_19a for why the intermediary needs this information. b)  Since a), b) and c) will not change for each request, specification of this information can be done once. The same is true for d) and e) if the intermediated Relying Party has only one registered intended use. |  |
| 🟡 | RPI_06 | When requested by an intermediated Relying Party, an intermediary SHALL request a presentation of attributes from a specific Wallet Unit. In the request, the intermediary SHALL include the intermediary's access certificate meant in requirement RPI_01 and the registration certificate of the Relying Party, as meant in RPI_03, if available. In addition, whether or not a registration certificate is available, the intermediary SHALL include in the request the information about the intermediated Relying Party required in RPRC_19a. |  |
| 🟡 | RPI_06a | Empty |  |
| 🟡 | RPI_07 | In case a Wallet Unit receives a presentation request from an intermediary on behalf of an intermediated Relying Party, it SHALL display the names and identifiers of both the intermediary and the intermediated Relying Party to the User when asking for User approval, as described in RPA_07. *Note: In this case, the name and identifier of the intermediary are included in the access certificate presented by the Relying Party Instance, whereas the name and identifier of the intermediated Relying Party are included in the extension of the presentation  request (see RPRC_19a), and in the registration certificate if available. If these names and identifiers are different, the Wallet Unit knows that the presentation request is from an intermediary on behalf of an intermediated Relying Party. |  |
| 🟡 | RPI_07a | In case a Wallet Unit receives a presentation request from an intermediary on behalf of an intermediated Relying Party, and if the User indicated that they want to verify the information registered about this Relying Party (according to RPRC_16), the Wallet Unit SHALL verify that that the contractual relationship between the Relying Party and the intermediary is indeed registered by the responsible Registrar according to RPI_04, see also RPRC_04.  If this verification fails, the Wallet Unit SHALL notify the User when asking for User consent. *Note: The Wallet Unit can either do this by inspecting the registration certificate (if available) or by querying the Registrar. |  |
| 🟡 | RPI_07b | Empty |  |
| 🟡 | RPI_08 | When a Wallet Unit presents to an intermediary any User attributes from a PID or attestation, the intermediary SHALL, after successfully carrying out the verifications in RPI_09, forward these attributes (only) to the Relying Party on behalf of which the presentation request was made. If any of the verifications in RPI_09 fail, the intermediary SHALL NOT forward any attributes to the Relying Party. |  |
| 🟡 | RPI_09 | When a Wallet Unit presents to an intermediary any attributes from a PID or attestation, the intermediary SHALL verify the authenticity of the PID or attestation, its revocation status, device binding, and User binding, as well as any combined presentation of attributes, if applicable, as specified in this ARF and if agreed with the Relying Party. Furthermore, the intermediary SHALL verify the authenticity of the Wallet Unit and its revocation status, as specified in this ARF, if agreed with the Relying Party. *Note: This ARF does not mandate that a Relying Party must carry out all of these verifications. Therefore, the intermediary and any Relying Party using its services must agree on what verifications the intermediary will carry out. |  |
| 🟡 | RPI_10 | The intermediary SHALL delete any PIDs or attestations it obtained from the Wallet Unit, including any User attributes, completely and immediately after it has sent the User attributes to the intermediated Relying Party. If the intermediary does not send any User attributes to the intermediated Relying Party, for example because one of the verifications in the previous step failed, the intermediary SHALL delete the PIDs, attestations, or WUAs completely and immediately as soon as it has completed all necessary verifications. |  |
| 🟡 | ZKP_01 | A ZKP scheme SHALL provide support for the following generic functions, while hiding all attributes of PIDs or attestations: (i) generation of a proof that an (some) attribute(s) having a specific value is (are) included in a PID or attestation, (ii) generation of a proof that a PID or attestation is within its validity period, (iii) generation of a proof that a PID or attestation has not been revoked, and (iv) generation of a proof that a PID or device-bound attestation is bound to a key stored in the WSCA/WSCD or in a keystore of the Wallet Unit. Additionally, a ZKP scheme SHOULD provide support for the following function, which SHOULD be used only when hiding the PID Provider or Attestation Provider is necessary: (v) generation of a proof that a PID or attestation has been issued by a trusted PID Provider or Attestation Provider, without revealing the PID Provider or Attestation Provider. *Note: See section 4.1.1 of the Discussion Paper for Topic G. |  |
| 🟡 | ZKP_02 | A ZKP scheme SHALL support proving possession of attestation of a given type. *Note: See section 4.1.2 and 4.1.3 of the Discussion Paper for Topic G. |  |
| 🟡 | ZKP_03 | A ZKP scheme SHOULD support the privacy-preserving binding of an attestation to a PID. In addition to the generic functions defined in ZKP_01, for this use case, a ZKP scheme SHALL provide support for the following functions: (i) generation of a proof that the Wallet Unit stores an attestation and a PID and that the attestation includes a specific attribute, having a specific value, which is also present in the PID. *Note: See section 4.1.4 of the Discussion Paper for Topic G. |  |
| 🟡 | ZKP_04 | A ZKP scheme SHOULD support the derivation of a verifiable User pseudonym, by combining an attribute value that is unique for the User with Relying Party-specific context (e.g., the Relying Party identifier) In addition to the generic functions defined in ZKP_01, for this use case, a ZKP scheme SHALL provide support for the following functions: (i) generation of a request for the issuance of an attestation that includes a secret attribute unique to the User, without revealing this attribute to the Attestation Provider, (ii) generation of an attestation presentation that includes a verifiable pseudonym derived from the secret attribute, a Relying Party identifier, and context-related information. *Note: See section 4.1.5 of the Discussion Paper for Topic G. |  |
| 🟡 | ZKP_05 | A ZKP scheme SHALL be usable in both remote and proximity presentation flows. While the inclusion of ZKP will introduce computational and verification delays, these delays SHALL NOT critically undermine or defeat the purpose of the Relying Party service (e.g. because of a critical impact on the User experience of the Wallet Unit). |  |
| 🟡 | ZKP_06 | A ZKP scheme SHOULD be able to generate proofs for already issued PIDs and attestations in the formats specified in [ISO/IEC 18013-5] or [SD-JWT VC]. |  |
| 🟡 | ZKP_07 | A ZKP scheme SHALL NOT introduce any additional communication or information that could be used to track or link User activity during, before, or after proof generation. |  |
| 🟡 | ZKP_08 | A ZKP scheme SHALL rely solely on algorithms standardised by a standardisation organisation recognised by the Commission or in a standard recognised by the Commission. |  |
| 🟡 | ZKP_09 | Use of a ZKP scheme SHALL NOT prevent the Wallet Unit's ability to provide User authentication with Level of Assurance High. |  |### Changes by Requirement

- **PAD_01, PAD_03, PAD_04, PAD_05**: No changes
- **PAD_02**: Note added for clarity
- **PAD_06**: Completely new requirement

---

## Detailed Analysis of Changes

### PAD_02 - Clarifying Note Added

**Change type**: Documentation enhancement

**Addition**: Note explaining when multiple PIDs/attestations would exist
- Clarifies this occurs with batch issuance
- Explains why simultaneous deletion is necessary
- No functional change, just better documentation

### PAD_06 - New Uninstall Requirement

**Change type**: New requirement

**Purpose**: Addresses Wallet Instance uninstallation scenario

**Key aspects**:

1. **Main requirement**: On uninstall, SHALL request WSCA(s) to delete:
   - All sensitive data related to Wallet Unit
   - All cryptographic keys for Wallet Unit
   - All keys for all PIDs and attestations

2. **Condition**: Only if WSCA(s) are connected at uninstall moment

3. **Comprehensive note addressing edge cases**:
   
   **Problem scenarios**:
   - External smart card not present during uninstall
   - Remote HSM unreachable (device offline)
   - Any disconnected WSCD at uninstall time
   
   **Consequence**: Keys may remain on WSCD indefinitely (orphaned keys)
   
   **Solution approach**: Wallet Provider MAY define handling strategy
   
   **Example strategy**: HSM manager could delete keys based on:
   - Age threshold (too old)
   - Inactivity period (not used for too long)
   - With awareness of associated risks

**Rationale**: 
- Completes the lifecycle management story (complements WIAM_13)
- Addresses real-world deployment scenarios (external cards, remote HSMs)
- Balances security (delete keys) with practicality (can't always reach WSCD)
- Provides guidance without mandating specific solutions for edge cases

**Related requirements**:
- **WIAM_13**: User uninstalls Wallet Unit → destroy all keys (general requirement)
- **PAD_06**: Adds specific handling for uninstall scenario with practical considerations

---

## Overall Assessment

Topic 51 shows **targeted enhancement** with focus on uninstallation edge cases:

**Core deletion framework remains stable**:
- User can delete PIDs/attestations anytime (PAD_01)
- Batch deletion for same type/provider (PAD_02)
- No provider notification (privacy) (PAD_03)
- Secure key destruction (PAD_04)
- W3C Digital Credentials API disclosure (PAD_05)

**New addition (PAD_06)**:
- Addresses uninstallation lifecycle stage
- Acknowledges real-world constraints (disconnected WSCDs)
- Provides flexibility for Wallet Providers
- Maintains security emphasis while being pragmatic

**Key improvement**: The comprehensive note in PAD_06 demonstrates mature understanding of deployment challenges and provides implementers with clear guidance on handling edge cases that will inevitably occur in production (external smart cards, remote HSMs, offline scenarios).

**Documentation enhancement**: PAD_02 note improves clarity about batch attestation handling.

All requirements remain assigned to Wallet Units/Providers (🟧 status). The topic now covers the complete PID/attestation deletion lifecycle, including the critical uninstallation scenario with practical considerations for various WSCD configurations.

---

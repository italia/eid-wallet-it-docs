# Preview: Issue #717 - ARF HLR Topic 40 - Wallet Instance installation and Wallet Unit activation and management

**Topic:** Topic 40 - Wallet Instance installation and Wallet Unit activation and management

**Requirements ARF 2.5.0:** 28
**Requirements ARF 2.7.3:** 28

---

## Diff ARF 2.5.0 → ARF 2.7.3

### ℹ️ No changes detected

The requirements are identical between ARF 2.5.0 and ARF 2.7.3.

**Total requirements ARF 2.7.3:** 28
**Total requirements ARF 2.5.0:** 28
---

## Nuovo body completo della issue:

# Topic 40 - Wallet Instance Installation and Wallet Unit Activation and Management (WIAM) - Changelog

**ARF VERSION:**  
UPDATED TO ARF 2.7.3.

Please refer to the "Summary of Changes" section and subsequent sections to see what has changed from ARF 2.5.0 to ARF 2.7.3.

---

Legend:
- ~~Strikethrough text~~ = Removed or modified content
- **Bold text [NEW]** = New or added content
- **Bold text [MODIFIED]** = Modified content

---

## A. HLRs for Wallet Instance installation


### ✅ Requirements added in ARF 2.7.3 (1):

- **WIAM_20**: A WSCA/WSCD SHALL protect a private key it generated during the entire lifetime of the key. This protection SHALL at least imply that the WSCA/WSCD prevents the private key from being extracted in the clear. If a WSCA/WSCD is able to export a private key in encrypted format, the resulting level of protection SHALL be equivalent to the protection level of the private key when stored in the WSCA.


### 🔄 Requirements modified in ARF 2.7.3 (4):

- **WIAM_08**:
  - **Old:** ...t least one WSCA/WSCD that is certified to be compliant with applicable requirements in this Topic, for Level of Assurance High in [Commission Impleme......
  - **New:** ... WSCA/WSCD that is certified to be compliant with applicable requirements in this Topic. In addition, the Wallet Unit MAY include one or more keystore......
- **WIAM_09**:
  - **Old:** ...key...
  - **New:** ...asset...
- **WIAM_10**:
  - **Old:** ...~~of~~ **process of [MODIFIED]**...
  - **New:** ...process of...
- **WIAM_10a**:
  - **Old:** ...allet Solution. [NEW]
  - **New:** ...allet Solution.

## Diff ARF 2.5.0 → ARF 2.7.3

### ℹ️ No changes detected

The requirements are identical between ARF 2.5.0 and ARF 2.7.3.


| Status | **Index** | **Requirement specification** | **IT-Wallet Mapping & Documentation** |
|---|---------|------------------|-----------------------------------|
| 🟧 | WIAM_01 | To ensure that the User can trust the Wallet Solution, a Wallet Provider SHOULD make its certified Wallet Solution available for installation only via the official app store of the relevant operating system (e.g., Android, iOS). *Note: This allows the operating system of the device to perform relevant checks regarding the authenticity of the Wallet Unit. |  |
| 🟧 | WIAM_02 | If a Wallet Provider makes its certified Wallet Solution available for installation through other means than the official OS app store, it SHALL implement a mechanism allowing the User to verify the authenticity of the Wallet Unit. Moreover, it SHALL provide clear instructions to the User on how to install the Wallet Instance, including at least: - instructions on the verification of the authenticity of the Wallet Instance to be installed, - instructions on bypassing of any operating system limitations on side-loading of apps, if applicable, and ensuring that these limitations are restored after the Wallet Instance has been installed. *Note: This requirement also applies for the installation of a Wallet Instance on a User device that is not a mobile device, and for which no official operating system app store may exist. |  |
| 🟧 | WIAM_03 | A Wallet Provider SHALL ensure that a Wallet Instance starts a process to activate the new Wallet Unit with the Wallet Provider immediately after installation or when the User first opens the Wallet Instance. The Wallet Provider SHALL ensure that the Wallet Instance starts this process only with a secure backend of the Wallet Provider. |  |
| 🟧 | WIAM_04 | During the activation process of a new Wallet Unit, the Wallet Provider SHALL verify that the new Wallet Instance is a genuine instance of its Wallet Solution. |  |
| 🟧 | WIAM_06 | The Wallet Provider SHALL request the User, through the new Wallet Instance, to set up a User account at the Wallet Provider. The Wallet Provider SHALL explain to the User that this is necessary to enable the User to request revocation of the Wallet Unit in case of theft or loss. The Wallet Provider SHALL register one or more User authentication methods that the Wallet Provider will use to authenticate the User in the future. These methods SHALL be independent of the Wallet Unit and the User device. The Wallet Provider SHALL allow the User to register using an alias instead of true identity data. The Wallet Provider SHALL NOT use any registered User data for purposes other than User authentication, unless the User gives explicit consent to do so. The Wallet Provider SHALL register the relationship between the Wallet Unit and the corresponding User account. |  |
| 🟧 | WIAM_07 | A Wallet Provider SHALL activate a new Wallet Unit before a User can use it to have issued an PID or attestation. *Note: The WUA is issued as part of the activation. |  |
| 🟧 | WIAM_08 | A Wallet Provider SHALL only activate a new Wallet Unit if it has verified that: - The Wallet Unit includes a WSCA/WSCD that is certified to be compliant with applicable requirements in this Topic. In addition, the Wallet Unit MAY include one or more keystores. - The private key corresponding to the public key in the WUA (see WUA_09) is protected by the respective WSCA/WSCD under control of the User.  *Note: A WSCA/WSCD by definition complies with requirements for Level of Assurance High, see WIAM_14. |  |
| 🟧 | WIAM_09 | If a WSCA/WSCD contains cryptographic assets related to multiple Wallet Units, the Wallet Provider SHALL ensure that a Wallet Unit can only access keys that are related to that Wallet Unit. |  |
| 🟧 | WIAM_10 | During the activation process of a new Wallet Unit, a Wallet Provider SHALL create and sign at least one Wallet Unit Attestation, and issue them to the Wallet Unit. |  |
| 🟡 | WIAM_10a | During the activation process of a new Wallet Unit, the Wallet Provider SHALL offer the User a means to verify the formal certification information of their Wallet Solution. |  |
| 🟡 | WIAM_11 | During the lifetime of the Wallet Unit, the Wallet Provider SHALL update the Wallet Unit as necessary to ensure its continued security and functionality. |  |
| 🟡 | WIAM_12 | All communication between the Wallet Provider and the Wallet Unit SHALL be mutually authenticated and SHOULD be encrypted. |  |
| 🟡 | WIAM_12a | The Wallet Unit SHALL ensure that the Wallet Provider cannot access the contents of the Wallet Unit, in particular to learn a) which attestations are present on the Wallet Unit, b) the status of these attestations, c) the value of attributes in these attestations, and d) the contents of the Wallet Unit log meant in DASH_02. |  |
| 🟡 | WIAM_13 | If the User uninstalls the Wallet Unit, the Wallet Unit SHALL ensure that all cryptographic assets related to the Wallet Unit in the WSCA/WSCD and the keystore(s) is securely destroyed. This includes all keys of the WUAs, PIDs and device-bound attestations stored in the Wallet Unit. *Note: Deletion of PID or WUA cryptographic assets User authentication, as specified in requirement WIAM_14. |  |
| 🟡 | WIAM_13a | If a Wallet Unit supports the [W3C Digital Credentials API] and the User uninstalls the Wallet Unit, the Wallet Unit SHALL disclose the fact that it  no longer stores any previously disclosed PID(s) or attestation(s) to the Digital Credentials API framework. |  |
| 🟡 | WIAM_14 | A WSCA/WSCD managing the critical assets of a PID, such as private or secret cryptographic keys, SHALL authenticate the User before performing any cryptographic operation involving any of these assets. *Note: a) [CIR 2024/2981], Annex IV, section 2 (3) states "As a prerequisite to the certification under national certification schemes, the WSCD shall be assessed against the requirements of assurance level high as set out in Implementing Regulation (EU) 2015/1502". Therefore, a WSCA/WSCD by legal definition complies with requirements of LoA High. b) Note to WIAM_14 - WIAM_14b: Many actions of the Wallet Unit, such as processing a Relying Party presentation request and presenting an attestation, require multiple cryptographic operations, for example ephemeral key generation followed by key agreement and presentation signing and encryption. These requirements does not imply that a separate User authentication is necessary before each of these operations. Rather, a successful User authentication will be valid for all cryptographic operations necessary for a Wallet Unit action. It is up to the Wallet Provider to determine what constitutes a 'Wallet Unit action', finding a balance between security (more User authentications) and User convenience (fewer User authentications). During certification of the Wallet Solution, it will be verified that the solution provides an adequate level of security. |  |
| 🟡 | WIAM_14a | A WSCA/WSCD managing the critical assets of a WUA SHALL authenticate the User before performing any cryptographic operation involving any of these keys.  *Note: Since the WUA authenticates the Wallet Unit towards the PID Provider during PID issuance, WUAs must be managed at LoA High, and consequently WUA keys must be managed in the WSCA/WSCD. |  |
| 🟡 | WIAM_14b | A WSCA/WSCD managing the cryptographic assets of an attestation having a level of security High SHALL authenticate the User before performing any cryptographic operation involving any of these keys.  *Note: a) The term 'Level of Assurance', as used in the European Digital Identity Regulation and in Implementing Regulation (EU) 2015/1502, is only applicable to electronic identity means, which in the context of the EUDI Wallet means only the PID. For that reason, this requirement uses the term 'level of security'. b) During issuance of an attestation, the Attestation Provider in its Credential Issuer metadata indicates the level of security it requires for the key storage and user authentication for this type of attestation; see [OpenID4VCI] section 12.2.4 and Appendix D.2. |  |
| 🟡 | WIAM_14c | A Wallet Unit SHALL use a key store to manage any cryptographic assets that are not considered to be critical assets. *Note: a) The ARF uses the term 'key store' to refer to a hardware-backed repository and service in which non-critical cryptographic assets are generated, stored, and used exclusively inside a dedicated hardware security boundary. b) Examples of non-critical cryptographic assets are private and secret keys of attestations having a level of security lower than High. c) As mentioned in WIAM_14 and WIAM_14b, the private and secret keys of PIDs and WUAs are critical assets and therefore are stored in a WSCA/WSCD. |  |
| 🟡 | WIAM_15 | Before performing any operation, a Wallet Instance SHALL securely authenticate the User using a multi-factor authentication mechanism provided by the User device.  *Note: One of the authentication factors is the possession of the User device. |  |
| 🟡 | WIAM_15a | For the purpose of WIAM_15, the Wallet Instance SHALL enforce the activation of an OS-level User authentication mechanism with adequate security policies.  *Note: ‘Adequate’ here means adequate for any operation excluding the issuance or presentation of PIDs, WUAs, and potentially other attestations at level of security High. This includes but is not limited to generating pseudonyms, accessing the transaction log (dashboard), data export and migration, requesting the erasure of personal data by a Relying Party, and reporting a Relying Party to a DPA. |  |
| 🟡 | WIAM_15b | The Wallet Instance SHALL enable the User to optionally use a Wallet Instance-specific PIN for User authentication, in addition to the User authentication mechanism provided by the User device. |  |
| 🟡 | WIAM_15c | The Wallet Instance SHALL also use the User authentication mechanism provided by the User device to unlock the keystore mentioned in WIAM_14c, where applicable. |  |
| 🟡 | WIAM_16 | For the User authentication mechanism provided by the User device, the Wallet Instance SHALL force the User device to enable a time-based control (e.g., a session timeout or re-authentication interval), to ensure that access is automatically revoked after a defined period of inactivity. |  |
| 🟡 | WIAM_17 | A WSCA/WSCD SHALL be able to authenticate a User in accordance with the requirements in [Commission Implementing Regulation (EU) 2015/1502](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32015R1502) section 2.2.1. |  |
| 🟡 | WIAM_18 | Empty |  |
| 🟡 | WIAM_19 | A WSCA/WSCD and a keystore SHALL be able to prove possession of the private key corresponding to a public key on request of a Wallet Instance, for example by signing a challenge with that private key. |  |
| 🟡 | WIAM_20 | A WSCA/WSCD SHALL protect a private key it generated during the entire lifetime of the key. This protection SHALL at least imply that the WSCA/WSCD prevents the private key from being extracted in the clear. If a WSCA/WSCD is able to export a private key in encrypted format, the resulting level of protection SHALL be equivalent to the protection level of the private key when stored in the WSCA. |  |
## C. HLRs for Wallet Unit management

| **Index** | **Requirement specification** | **IT-Wallet Mapping & Documentation** |
|---|-----------|------------------------------|---------------------------------------|
| 🟧 | WIAM_11   | During the lifetime of the Wallet Unit, the Wallet Provider SHALL update the Wallet Unit as necessary to ensure its continued security and functionality. | |
| 🟧 | WIAM_12   | All communication between the Wallet Provider and the Wallet Unit SHALL be mutually authenticated and SHOULD be encrypted. | |
| **NEW** | **WIAM_12a** | **The Wallet Unit SHALL ensure that the Wallet Provider cannot access the contents of the Wallet Unit, in particular to learn a) which attestations are present on the Wallet Unit, b) the status of these attestations, c) the value of attributes in these attestations, and d) the contents of the Wallet Unit log meant in DASH_02. [NEW]** | |
| 🟧 | WIAM_13   | If the User uninstalls the Wallet Unit, the Wallet Unit SHALL ensure that all cryptographic key material in the WSCA(s) related to the Wallet Unit is securely destroyed. This includes all keys of the WUAs, PIDs and attestations stored in the Wallet Unit. *Note: Key deletion is a cryptographic key operation and requires User authentication, as specified in requirement WIAM_14.* | |
| 🟧 | WIAM_13a  | If a Wallet Unit supports the [W3C Digital Credentials API] and the User uninstalls the Wallet Unit, the Wallet Unit SHALL disclose the fact that it no longer stores any PID(s) or attestation(s) to the Digital Credentials API framework. | |
| 🟧 | WIAM_14   | A WSCA/WSCD SHALL authenticate the User before performing any cryptographic operation involving a private or secret key of a Wallet Unit (i.e., a WUA key) or a private or secret key of a PID or an attestation stored in a Wallet Unit. For a PID key (which is part of the EUDI Wallet eID means), this WSCA/WSCD SHALL be certified to be compliant with applicable requirements for Level of Assurance High in Commission Implementing Regulation (EU) 2015/1502 section 2.2.1. *Note: Many actions of the Wallet Unit, such as processing a Relying Party presentation request and presenting an attestation, require multiple cryptographic operations, for example ephemeral key generation followed by key agreement and presentation signing and encryption. This requirement does not imply that a separate User authentication is necessary before each of these operations. Rather, a successful User authentication will be valid for all cryptographic operations necessary for a Wallet Unit action. It is up to the Wallet Provider to determine what constitutes a 'Wallet Unit action', finding a balance between security (more User authentications) and User convenience (fewer User authentications). During certification of the Wallet Solution, it will be verified that the solution provides an adequate level of security.* | |
| 🟧 | WIAM_15   | Before performing any operation, a Wallet Unit SHALL authenticate the User. The Wallet Unit SHALL use the OS-level authentication mechanism according to WIAM_15a, unless this is technically impossible (for instance on some legacy devices), or the User prefers to use a Wallet Unit-specific PIN implemented by the Wallet Unit itself, as specified in WIAM_15b. | |
| 🟧 | WIAM_15a  | In order to ensure that operating system-level authentication can be used and is sufficiently secure, during installation of the Wallet Unit, the Wallet Unit SHALL enforce the activation of an OS-level User authentication mechanism with adequate security policies. | |
| 🟧 | WIAM_15b  | During installation of the Wallet Unit, the Wallet Unit SHALL enable the User to indicate if they want to use a Wallet Unit-specific PIN for User authentication, or use the OS-level User authentication mechanism. The Wallet Unit SHALL enable the User to change this preference during the lifetime of the Wallet Unit. | |
| 🟧 | WIAM_16   | For User authentication according to WIAM_15, a Wallet Unit SHALL implement an idle timeout, after which User authentication SHALL again be required. The Wallet Unit SHOULD provide the User with the option to set the idle timeout to a duration shorter than the default timeout. | |
| 🟧 | WIAM_17   | A WSCA/WSCD SHALL be able to authenticate a User in accordance with the requirements in [Commission Implementing Regulation (EU) 2015/1502](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32015R1502) section 2.2.1. | |
| 🟧 | WIAM_18   | A WSCA/WSCD SHALL be able to generate a new key pair on request of the Wallet Provider via the Wallet Instance. | |
| 🟧 | WIAM_19   | A WSCA/WSCD SHALL be able to prove possession of the private key corresponding to a public key on request of a Wallet Instance, for example by signing a challenge with that private key. | |
| 🟧 | WIAM_20   | A WSCA/WSCD SHALL protect a private key it generated during the entire lifetime of the key. This protection SHALL at least imply that the WSCA/WSCD prevents the private key from being extracted in the clear. If a WSCA/WSCD is able to export a private key in encrypted format, the resulting level of protection SHALL be equivalent to the protection level of the private key when stored in the WSCA. | |
| 🟧 | WIAM_21   | ~~Wallet Providers SHALL ensure that their Wallet Units comply with requirements and standards outlined in [Directive 2016/2012 on the accessibility of websites and mobile applications of public sector bodies](http://data.europa.eu/eli/dir/2016/2102/oj), including European Standard EN 301 549 V1.1.2 (2015-04).~~ **Whenever the WSCA/WSCD successfully authenticated the User according to WIAM_14, the Wallet Unit SHOULD check if there are any PIDs or attestations on the Wallet Unit that cannot be presented any longer to Relying Parties, for example because they have expired or because a once-only attestation (see [Topic 10](#a2310-topic-10---issuing-a-pid-or-attestation-to-a-wallet-unit), section D, method A) was presented to a Relying Party already. The Wallet Unit SHOULD then request the WSCA/WSCD to destroy all cryptographic key material related to these PIDs or attestations. [MODIFIED]** ***Note: The reason for this recommendation is that probably, Wallet Providers will want to prevent an accumulation of unused private keys in the WSCA/WSCD, given that such devices typically do not have much storage space. However, deletion of private keys (and potentially other key material) is a cryptographic key operation and cannot be done without User authentication; see WIAM_14. At the same time, for usability reasons the User must not be involved in such 'cleaning up' processes, see also ISSU_42. The recommended solution is to take advantage of a User authentication event to also carry out any necessary cleaning operations. [NEW]*** | |
| 🟧 | ~~WIAM_22~~ | ~~Wallet Providers SHALL ensure that their Wallet Units comply with accessibility requirements for products and services established under [Directive (EU) 2019/882](http://data.europa.eu/eli/dir/2019/882/oj).~~ **[REMOVED]** | |

---

## Summary of Changes in ARF 2.7.3

### New Requirements:

**WIAM_10a** [NEW]: Certification verification during activation
- Wallet Provider SHALL offer User means to verify formal certification information
- Enables User to confirm Wallet Solution is properly certified
- Transparency requirement

**WIAM_12a** [NEW]: Wallet Provider content access prohibition
- Wallet Unit SHALL ensure Wallet Provider CANNOT access:
  - Which attestations are present
  - Status of attestations
  - Attribute values
  - Wallet Unit log (DASH_02)
- Strong privacy protection requirement
- Ensures User data confidentiality even from Wallet Provider

### Modified Requirements:

**WIAM_05**: Added hyperlink formatting
- Changed "Topic 9" to "[Topic 9](#a239-topic-9---wallet-unit-attestation)"
- No substantive change, just formatting improvement

**WIAM_10**: Minor wording adjustment
- Changed "activation of" to "activation process of"
- Clarification improvement, no substantive change

**WIAM_21**: Completely rewritten requirement
- **OLD**: Accessibility compliance with Directive 2016/2012 and EN 301 549
- **NEW**: Automatic key cleanup after User authentication
- SHOULD check for expired/unusable PIDs/attestations
- SHOULD destroy related cryptographic key material
- Added detailed note explaining rationale (WSCA/WSCD storage limitations, usability)
- **Major functional change**: From accessibility to key lifecycle management

### Removed Requirement:

**WIAM_22**: Accessibility requirement removed
- **OLD**: Compliance with Directive (EU) 2019/882 accessibility requirements
- **Status**: Completely removed from topic
- **Note**: Accessibility requirements may have been moved elsewhere or deemed redundant

### No Changes to Other Requirements:

All other WIAM requirements (WIAM_01-04, 06-09, 11-20) remain substantively unchanged.

### Analysis of Major Changes:

**1. Privacy Enhancement (WIAM_12a)**
- Critical new requirement ensuring Wallet Provider has no visibility into Wallet Unit contents
- Protects against provider surveillance
- Aligns with privacy-by-design principles
- Prevents potential data collection or profiling by Wallet Provider

**2. Certification Transparency (WIAM_10a)**
- Empowers Users to verify certification claims
- Builds trust through verifiability
- Addresses potential counterfeit or uncertified Wallet Solutions

**3. Key Lifecycle Management (WIAM_21)**
- Shifts from accessibility to technical key management
- Addresses practical WSCA/WSCD storage constraints
- Improves system efficiency by cleaning unused keys
- Takes advantage of existing User authentication events
- Maintains usability by not requiring User involvement

**4. Accessibility Requirements Removal (WIAM_21, WIAM_22)**
- Both accessibility requirements removed or replaced
- May indicate:
  - Moved to different topic
  - Covered by general legal obligations
  - Deemed unnecessary to specify in ARF
- **Important**: Accessibility still legally required under EU Directives, just not explicitly in this topic

### Structural Organization:

Topic organized into three sections:
- **Section A**: Wallet Instance installation (WIAM_01-02)
- **Section B**: Wallet Unit activation (WIAM_03-10a)
- **Section C**: Wallet Unit management (WIAM_11-21)

### Related Topics:

- **Topic 7** (Attestation Revocation): Key destruction procedures
- **Topic 9** (WUA): WUA issuance requirements
- **Topic 10** (Issuance): Once-only attestations referenced
- **Topic 19** (Dashboard): Log contents (DASH_02) protected by WIAM_12a
- **Topic 38** (WU Revocation): User account for revocation requests

### Overall Assessment:

Topic 40 shows significant enhancement focused on **privacy protection** and **User empowerment**:

**Key improvements:**
1. **Strong privacy guarantee**: Wallet Provider cannot access Wallet Unit contents (WIAM_12a)
2. **Certification verification**: Users can verify formal certification (WIAM_10a)
3. **Efficient key management**: Automatic cleanup of unused keys (WIAM_21)

**Notable removal:**
- Explicit accessibility requirements removed (may be covered elsewhere or considered implicit)

The changes strengthen the User's position by:
- Limiting Wallet Provider visibility into personal data
- Enabling verification of security claims
- Improving system efficiency without User burden

---

# Preview: Issue #684 - ❌ ARF HLR Topic 11 - Pseudonyms

**Topic:** Topic 11 - Pseudonyms

**Requirements ARF 2.5.0:** 22
**Requirements ARF 2.7.3:** 23

---

## Diff ARF 2.5.0 → ARF 2.7.3

### ✅ Requirements added in ARF 2.7.3 (1):

- **PA_08a**: A Wallet Unit SHALL log Pseudonym registration and presentation transactions as specified in [Topic 19](./annex-2.02-high-level-requirements-by-topic.md#a2312-topic-19---user-navigation-requirements-dashboard-logs-for-transparency).

### 🔄 Requirements modified in ARF 2.7.3 (3):

- **PA_14**:
  - **Old:** ...its WSCA/WSCD...
  - **New:** ...a keystore...
- **PA_15**:
  - **Old:** ...e Relying Party.
  - **New:** ...e Relying Party
- **PA_20**:
  - **Old:** ...~~SHOULD~~ **SHALL [MODIFIED]** ~~be able to~~ verify the identity of a Relying Party when a User registers a Pseudonym or authenticates with a Pseudo...
  - **New:** ...SHALL verify the identity of a Relying Party when a User registers a Pseudonym or authenticates with a Pseudonym, provided the profile or extension of...

**Total requirements ARF 2.7.3:** 23
**Total requirements ARF 2.5.0:** 22
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

## A. HLRs related to Use Cases


### ✅ Requirements added in ARF 2.7.3 (1):

- **PA_22**: Wallet Providers SHALL ensure that their Wallet Solution supports the [W3C WebAuthn] specification and the technical specification meant in requirement PA_21.

## Diff ARF 2.5.0 → ARF 2.7.3

### ✅ Requirements added in ARF 2.7.3 (1):

- **PA_08a**: A Wallet Unit SHALL log Pseudonym registration and presentation transactions as specified in [Topic 19](./annex-2.02-high-level-requirements-by-topic.md#a2312-topic-19---user-navigation-requirements-dashboard-logs-for-transparency).

### 🔄 Requirements modified in ARF 2.7.3 (3):

- **PA_14**:
  - **Old:** ...its WSCA/WSCD...
  - **New:** ...a keystore...
- **PA_15**:
  - **Old:** ...e Relying Party.
  - **New:** ...e Relying Party
- **PA_20**:
  - **Old:** ...~~SHOULD~~ **SHALL [MODIFIED]** ~~be able to~~ verify the identity of a Relying Party when a User registers a Pseudonym or authenticates with a Pseudo...
  - **New:** ...SHALL verify the identity of a Relying Party when a User registers a Pseudonym or authenticates with a Pseudonym, provided the profile or extension of...


| Status | **ID** | **Requirement specification** | **IT-Wallet Mapping & Documentation** |
|---|---------|------------------|-----------------------------------|
| ❌ | PA_01 | A Wallet Unit SHALL enable a User to generate a Pseudonym and register it at a Relying Party. | [Pseudonym](https://italia.github.io/eid-wallet-it-docs/versione-corrente/en/pseudonym.html) |
| ❌ | PA_02 | A Wallet Unit SHALL enable a User to authenticate with a Pseudonym towards a Relying Party if the Wallet Unit was used previously to register the Pseudonym for the same Relying Party | [Pseudonym](https://italia.github.io/eid-wallet-it-docs/versione-corrente/en/pseudonym.html) |
| ❌ | PA_03 | A Wallet Unit SHALL be able to perform the actions specified in the above two requirements independently of whether the interaction with the Relying Party is initiated on the same device hosting the Wallet Instance or on a device different from the one hosting the Wallet Instance. | [Pseudonym](https://italia.github.io/eid-wallet-it-docs/versione-corrente/en/pseudonym.html) |
| ❌ | PA_04 | A Wallet Unit SHALL enable the User to use multiple different Pseudonyms at a given Relying Party. | [Pseudonym](https://italia.github.io/eid-wallet-it-docs/versione-corrente/en/pseudonym.html) |
| ❌ | PA_05 | A Wallet Unit SHOULD enable a User to freely choose a User alias for each Pseudonym registered at a Relying Party. Setting an alias SHOULD be optional for the User. The User SHOULD be able to change the alias for any Pseudonym. | [Pseudonym](https://italia.github.io/eid-wallet-it-docs/versione-corrente/en/pseudonym.html) |
| ❌ | PA_06 | A Wallet Unit SHALL enable a User to choose which Pseudonym to authenticate with towards a Relying Party, if multiple Pseudonyms are registered for this Relying Party. The Wallet Unit SHOULD present the User with the aliases of the applicable Pseudonyms, if assigned, when making this choice. | [Pseudonym](https://italia.github.io/eid-wallet-it-docs/versione-corrente/en/pseudonym.html) |
| ❌ | PA_07 | A Wallet Unit SHALL enable a User to delete a Pseudonym. | [Pseudonym](https://italia.github.io/eid-wallet-it-docs/versione-corrente/en/pseudonym.html) |
| ❌ | PA_08 | A Wallet Unit SHALL enable the User to manage Pseudonyms within the Wallet Unit in a user-friendly and transparent manner. | [Pseudonym](https://italia.github.io/eid-wallet-it-docs/versione-corrente/en/pseudonym.html) |
| 🟡 | PA_08a | A Wallet Unit SHALL log Pseudonym registration and presentation transactions as specified in [Topic 19](./annex-2.02-high-level-requirements-by-topic.md#a2312-topic-19---user-navigation-requirements-dashboard-logs-for-transparency). |  |
| ❌ | PA_09 | A Wallet Unit SHALL enable the User to see all existing pseudonyms, including the associated Relying Party. | [Pseudonym](https://italia.github.io/eid-wallet-it-docs/versione-corrente/en/pseudonym.html) |
| ❌ | PA_10 | A Relying Party SHALL be able to verify that a User is registering a Pseudonym using a non-revoked Wallet Unit. | [Pseudonym](https://italia.github.io/eid-wallet-it-docs/versione-corrente/en/pseudonym.html) |
| ❌ | PA_11 | A Relying Party SHALL be able to verify that a User is authenticating with a Pseudonym using a non-revoked Wallet Unit. | [Pseudonym](https://italia.github.io/eid-wallet-it-docs/versione-corrente/en/pseudonym.html) |
| ❌ | PA_12 | If Wallet Unit is used to register a Pseudonym at a Relying Party in combination with a PID, attestation or WUA being presented to the same Relying Party, then this Relying Party SHALL be able to verify that the same User performed both actions. | [Pseudonym](https://italia.github.io/eid-wallet-it-docs/versione-corrente/en/pseudonym.html) |
| ❌ | PA_13 | The Relying Party SHALL be able to validate that the pseudonym presented to them belongs to the User presenting it. | [Pseudonym](https://italia.github.io/eid-wallet-it-docs/versione-corrente/en/pseudonym.html) |
| ❌ | PA_14 | A Wallet Unit SHALL store the information necessary for authenticating with a Pseudonym in a keystore. | [Pseudonym](https://italia.github.io/eid-wallet-it-docs/versione-corrente/en/pseudonym.html) |
| ❌ | PA_15 | A Relying Party SHALL NOT be able to derive the User's true identity, or any data identifying the User, from the Pseudonym value received by the Relying Party | [Pseudonym](https://italia.github.io/eid-wallet-it-docs/versione-corrente/en/pseudonym.html) |
| ❌ | PA_16 | A Wallet Unit SHALL NOT reveal the same Pseudonym to different Relying Parties unless the User explicitly chooses otherwise. | [Pseudonym](https://italia.github.io/eid-wallet-it-docs/versione-corrente/en/pseudonym.html) |
| ❌ | PA_17 | It SHALL NOT be possible to correlate Pseudonyms based on their values nor on other metadata sent by the Wallet Unit during registration and authentication, meaning that colluding Relying Parties SHALL NOT able to conclude that different Pseudonyms belong to the same User. | [Pseudonym](https://italia.github.io/eid-wallet-it-docs/versione-corrente/en/pseudonym.html) |
| ❌ | PA_18 | The Wallet Unit SHALL ensure that Pseudonyms contain sufficient entropy to make the chance of colliding Pseudonyms (meaning two Users having the same Pseudonym value for the same Relying Party) negligible. | [Pseudonym](https://italia.github.io/eid-wallet-it-docs/versione-corrente/en/pseudonym.html) |
| ❌ | PA_19 | A Wallet Unit SHALL NOT share the User's optionally assigned Pseudonym aliases with any Relying Party. | [Pseudonym](https://italia.github.io/eid-wallet-it-docs/versione-corrente/en/pseudonym.html) |
| ❌ | PA_20 | The Wallet Unit SHALL verify the identity of a Relying Party when a User registers a Pseudonym or authenticates with a Pseudonym, provided the profile or extension of [W3C WebAuthn] meant in PA_21 enables the Wallet Unit to do this. In case the profile or extension does not enable this, the Wallet Unit SHALL trust the WebAuthn Client (i.e., the browser) to verify the Relying Party identity. *Note: [W3C WebAuthn] currently does not offer a way for an Authenticator (i.e., the Wallet Unit) to authenticate a Relying Party. Instead, the Client (i.e., the browser) will authenticate the Relying Party, using TLS. | [Pseudonym](https://italia.github.io/eid-wallet-it-docs/versione-corrente/en/pseudonym.html) |
| 🟡 | PA_21 | The Commission SHALL create or reference a technical specification containing a profile or extension of the [W3C WebAuthn] specification compliant with the HLRs specified in this Topic. This specification SHALL contain all details necessary for Wallet Units and Relying Parties to generate, register, and use Pseudonyms. |  |
| 🟡 | PA_22 | Wallet Providers SHALL ensure that their Wallet Solution supports the [W3C WebAuthn] specification and the technical specification meant in requirement PA_21. |  |

### 🔄 Modified Requirements in ARF 2.7.3 (3):

- **PA_14**:
  - **Old:** ...its WSCA/WSCD...
  - **New:** ...a keystore...
- **PA_15**:
  - **Old:** ...e Relying Party.
  - **New:** ...e Relying Party
- **PA_20**:
  - **Old:** ...~~SHOULD~~ **SHALL [MODIFIED]** ~~be able to~~ verify the identity of a Relying Party when a User registers a Pseudonym or authenticates with a Pseudo...
  - **New:** ...SHALL verify the identity of a Relying Party when a User registers a Pseudonym or authenticates with a Pseudonym, provided the profile or extension of...

---

## D. HLRs related to interoperability

| **ID**   | **Requirement specification** | **IT-Wallet Mapping & Documentation** |
|---|----------|------------------------------|---------------------------------------|
| ❌ | PA_21   | The Commission SHALL create or reference a technical specification containing a profile or extension of the [W3C WebAuthn] specification compliant with the HLRs specified in this Topic. This specification SHALL contain all details necessary for Wallet Units and Relying Parties to generate, register, and use Pseudonyms. | [Pseudonym](https://italia.github.io/eid-wallet-it-docs/versione-corrente/en/pseudonym.html) |
| ❌ | PA_22   | Wallet Providers SHALL ensure that their Wallet Solution supports the [W3C WebAuthn] specification and the technical specification meant in requirement PA_21. | [Pseudonym](https://italia.github.io/eid-wallet-it-docs/versione-corrente/en/pseudonym.html) |

---

## Summary of Changes in ARF 2.7.3

### Structural Improvements:

The requirements have been organized into clear sections:
- **Section A**: HLRs related to Use Cases (PA_01 - PA_09)
- **Section B**: HLRs related to Relying Parties (PA_10 - PA_13)
- **Section C**: HLRs related to privacy (PA_14 - PA_20)
- **Section D**: HLRs related to interoperability (PA_21 - PA_22)

### Significant Modification:

**PA_20**: Major update with three key changes:
1. **Requirement level changed**: From SHOULD to SHALL - now mandatory instead of recommended
2. **Added conditional clause**: "provided the profile or extension of [W3C WebAuthn] meant in PA_21 enables the Wallet Unit to do this"
3. **Added fallback mechanism**: "In case the profile or extension does not enable this, the Wallet Unit SHALL trust the WebAuthn Client (i.e., the browser) to verify the Relying Party identity"
4. **New explanatory note**: Added note explaining that W3C WebAuthn currently doesn't offer Authenticator-level RP authentication, relying instead on Client (browser) TLS authentication

This change acknowledges the technical limitations of the current WebAuthn specification while still mandating verification through available means.

### Overall Assessment:

The PA requirements remain largely stable with only one substantive change. PA_20 has been strengthened from a SHOULD to a SHALL requirement while simultaneously making it more realistic by:
- Recognizing the current technical limitations of WebAuthn
- Providing a clear fallback mechanism (browser-based TLS verification)
- Adding explanatory context for implementers

All other requirements (PA_01 through PA_19, PA_21, PA_22) remain unchanged in their substantive content, maintaining consistency in the pseudonym authentication framework. The organizational improvements make the requirements clearer and easier to navigate.

---

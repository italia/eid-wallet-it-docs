# Topic 11 - Pseudonyms

| **Requirement ID** | **Legacy ID** | **Description** | **Status** |
|-------------------|---------------|------------------|------------|
| PA_01 |  | A Wallet Unit SHALL enable a User to generate a Pseudonym and register it at a Relying Party. | 🟡 |
| PA_02 |  | A Wallet Unit SHALL enable a User to authenticate with a Pseudonym towards a Relying Party if the Wallet Unit was used previously to register the Pseudonym for the same Relying Party | 🟡 |
| PA_03 |  | A Wallet Unit SHALL be able to perform the actions specified in the above two requirements independently of whether the interaction with the Relying Party is initiated on the same device hosting th... | 🟡 |
| PA_04 |  | A Wallet Unit SHALL enable the User to use multiple different Pseudonyms at a given Relying Party. | 🟡 |
| PA_05 |  | A Wallet Unit SHOULD enable a User to freely choose a User alias for each Pseudonym registered at a Relying Party. Setting an alias SHOULD be optional for the User. The User SHOULD be able to chang... | 🟡 |
| PA_06 |  | A Wallet Unit SHALL enable a User to choose which Pseudonym to authenticate with towards a Relying Party, if multiple Pseudonyms are registered for this Relying Party. The Wallet Unit SHOULD presen... | 🟡 |
| PA_07 |  | A Wallet Unit SHALL enable a User to delete a Pseudonym. | 🟡 |
| PA_08 |  | A Wallet Unit SHALL enable the User to manage Pseudonyms within the Wallet Unit in a user-friendly and transparent manner. | 🟡 |
| PA_08a |  | A Wallet Unit SHALL log Pseudonym registration and presentation transactions as specified in [Topic 19](./annex-2.02-high-level-requirements-by-topic.md#a2312-topic-19---user-navigation-requirement... | 🟡 |
| PA_09 |  | A Wallet Unit SHALL enable the User to see all existing pseudonyms, including the associated Relying Party. | 🟡 |
| PA_10 |  | A Relying Party SHALL be able to verify that a User is registering a Pseudonym using a non-revoked Wallet Unit. | 🟡 |
| PA_11 |  | A Relying Party SHALL be able to verify that a User is authenticating with a Pseudonym using a non-revoked Wallet Unit. | 🟡 |
| PA_12 |  | If Wallet Unit is used to register a Pseudonym at a Relying Party in combination with a PID, attestation or WUA being presented to the same Relying Party, then this Relying Party SHALL be able to v... | 🟡 |
| PA_13 |  | The Relying Party SHALL be able to validate that the pseudonym presented to them belongs to the User presenting it. | 🟡 |
| PA_14 |  | A Wallet Unit SHALL store the information necessary for authenticating with a Pseudonym in a keystore. | 🟡 |
| PA_15 |  | A Relying Party SHALL NOT be able to derive the User's true identity, or any data identifying the User, from the Pseudonym value received by the Relying Party | 🟡 |
| PA_16 |  | A Wallet Unit SHALL NOT reveal the same Pseudonym to different Relying Parties unless the User explicitly chooses otherwise. | 🟡 |
| PA_17 |  | It SHALL NOT be possible to correlate Pseudonyms based on their values nor on other metadata sent by the Wallet Unit during registration and authentication, meaning that colluding Relying Parties S... | 🟡 |
| PA_18 |  | The Wallet Unit SHALL ensure that Pseudonyms contain sufficient entropy to make the chance of colliding Pseudonyms (meaning two Users having the same Pseudonym value for the same Relying Party) neg... | 🟡 |
| PA_19 |  | A Wallet Unit SHALL NOT share the User's optionally assigned Pseudonym aliases with any Relying Party. | 🟡 |
| PA_20 |  | The Wallet Unit SHALL verify the identity of a Relying Party when a User registers a Pseudonym or authenticates with a Pseudonym, provided the profile or extension of [W3C WebAuthn] meant in PA_21 ... | 🟡 |
| PA_21 |  | The Commission SHALL create or reference a technical specification containing a profile or extension of the [W3C WebAuthn] specification compliant with the HLRs specified in this Topic. This specif... | 🟡 |
| PA_22 |  | Wallet Providers SHALL ensure that their Wallet Solution supports the [W3C WebAuthn] specification and the technical specification meant in requirement PA_21. | 🟡 |
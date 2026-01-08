# Topic 40 - Wallet Instance installation and Wallet Unit activation and management

| **Requirement ID** | **Legacy ID** | **Description** | **Status** |
|-------------------|---------------|------------------|------------|
| WIAM_01 |  | To ensure that the User can trust the Wallet Solution, a Wallet Provider SHOULD make its certified Wallet Solution available for installation only via the official app store of the relevant operati... | 🟡 |
| WIAM_02 |  | If a Wallet Provider makes its certified Wallet Solution available for installation through other means than the official OS app store, it SHALL implement a mechanism allowing the User to verify th... | 🟡 |
| WIAM_03 |  | A Wallet Provider SHALL ensure that a Wallet Instance starts a process to activate the new Wallet Unit with the Wallet Provider immediately after installation or when the User first opens the Walle... | 🟡 |
| WIAM_04 |  | During the activation process of a new Wallet Unit, the Wallet Provider SHALL verify that the new Wallet Instance is a genuine instance of its Wallet Solution. | 🟡 |
| WIAM_06 |  | The Wallet Provider SHALL request the User, through the new Wallet Instance, to set up a User account at the Wallet Provider. The Wallet Provider SHALL explain to the User that this is necessary to... | 🟡 |
| WIAM_07 |  | A Wallet Provider SHALL activate a new Wallet Unit before a User can use it to have issued an PID or attestation. *Note: The WUA is issued as part of the activation. | 🟡 |
| WIAM_08 |  | A Wallet Provider SHALL only activate a new Wallet Unit if it has verified that: - The Wallet Unit includes a WSCA/WSCD that is certified to be compliant with applicable requirements in this Topic.... | 🟡 |
| WIAM_09 |  | If a WSCA/WSCD contains cryptographic assets related to multiple Wallet Units, the Wallet Provider SHALL ensure that a Wallet Unit can only access keys that are related to that Wallet Unit. | 🟡 |
| WIAM_10 |  | During the activation process of a new Wallet Unit, a Wallet Provider SHALL create and sign at least one Wallet Unit Attestation, and issue them to the Wallet Unit. | 🟡 |
| WIAM_10a |  | During the activation process of a new Wallet Unit, the Wallet Provider SHALL offer the User a means to verify the formal certification information of their Wallet Solution. | 🟡 |
| WIAM_11 |  | During the lifetime of the Wallet Unit, the Wallet Provider SHALL update the Wallet Unit as necessary to ensure its continued security and functionality. | 🟡 |
| WIAM_12 |  | All communication between the Wallet Provider and the Wallet Unit SHALL be mutually authenticated and SHOULD be encrypted. | 🟡 |
| WIAM_12a |  | The Wallet Unit SHALL ensure that the Wallet Provider cannot access the contents of the Wallet Unit, in particular to learn a) which attestations are present on the Wallet Unit, b) the status of th... | 🟡 |
| WIAM_13 |  | If the User uninstalls the Wallet Unit, the Wallet Unit SHALL ensure that all cryptographic assets related to the Wallet Unit in the WSCA/WSCD and the keystore(s) is securely destroyed. This includ... | 🟡 |
| WIAM_13a |  | If a Wallet Unit supports the [W3C Digital Credentials API] and the User uninstalls the Wallet Unit, the Wallet Unit SHALL disclose the fact that it  no longer stores any previously disclosed PID(s... | 🟡 |
| WIAM_14 |  | A WSCA/WSCD managing the critical assets of a PID, such as private or secret cryptographic keys, SHALL authenticate the User before performing any cryptographic operation involving any of these ass... | 🟡 |
| WIAM_14a |  | A WSCA/WSCD managing the critical assets of a WUA SHALL authenticate the User before performing any cryptographic operation involving any of these keys.  *Note: Since the WUA authenticates the Wall... | 🟡 |
| WIAM_14b |  | A WSCA/WSCD managing the cryptographic assets of an attestation having a level of security High SHALL authenticate the User before performing any cryptographic operation involving any of these keys... | 🟡 |
| WIAM_14c |  | A Wallet Unit SHALL use a key store to manage any cryptographic assets that are not considered to be critical assets. *Note: a) The ARF uses the term 'key store' to refer to a hardware-backed repos... | 🟡 |
| WIAM_15 |  | Before performing any operation, a Wallet Instance SHALL securely authenticate the User using a multi-factor authentication mechanism provided by the User device.  *Note: One of the authentication ... | 🟡 |
| WIAM_15a |  | For the purpose of WIAM_15, the Wallet Instance SHALL enforce the activation of an OS-level User authentication mechanism with adequate security policies.  *Note: ‘Adequate’ here means adequate for... | 🟡 |
| WIAM_15b |  | The Wallet Instance SHALL enable the User to optionally use a Wallet Instance-specific PIN for User authentication, in addition to the User authentication mechanism provided by the User device. | 🟡 |
| WIAM_15c |  | The Wallet Instance SHALL also use the User authentication mechanism provided by the User device to unlock the keystore mentioned in WIAM_14c, where applicable. | 🟡 |
| WIAM_16 |  | For the User authentication mechanism provided by the User device, the Wallet Instance SHALL force the User device to enable a time-based control (e.g., a session timeout or re-authentication inter... | 🟡 |
| WIAM_17 |  | A WSCA/WSCD SHALL be able to authenticate a User in accordance with the requirements in [Commission Implementing Regulation (EU) 2015/1502](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX... | 🟡 |
| WIAM_18 |  | Empty | 🟡 |
| WIAM_19 |  | A WSCA/WSCD and a keystore SHALL be able to prove possession of the private key corresponding to a public key on request of a Wallet Instance, for example by signing a challenge with that private key. | 🟡 |
| WIAM_20 |  | A WSCA/WSCD SHALL protect a private key it generated during the entire lifetime of the key. This protection SHALL at least imply that the WSCA/WSCD prevents the private key from being extracted in ... | 🟡 |
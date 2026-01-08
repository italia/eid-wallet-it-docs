# Topic 10 - Issuing a PID or attestation to a Wallet Unit

| **Requirement ID** | **Legacy ID** | **Description** | **Status** |
|-------------------|---------------|------------------|------------|
| ISSU_02 |  | Wallet Providers SHALL ensure that their Wallet Solution supports the attestation formats specified in ISO/IEC 18013-5, see [ISO18013-5], and in "SD-JWT-based Verifiable Credentials (SD-JWT VC)", s... | 🟡 |
| ISSU_03 |  | Wallet Units, PID Providers, and Attestation Providers SHALL support the [W3C Digital Credentials API]](<https://wicg.github.io/digital-credentials/>) for the issuance of PIDs and attestations, pro... | 🟡 |
| ISSU_04 |  | The OpenID4VCI protocol referenced in requirement ISSU_01, or an EUDI Wallet-specific extension or profile thereof, SHALL enable PID Providers and Attestation Provider to issue to a Wallet Unit a b... | 🟡 |
| ISSU_05 |  | A Wallet Unit SHALL support a process to activate a newly issued PID, in accordance with the requirements for LoA High in [Commission Implementing Regulation (EU) 2015/1502](https://eur-lex.europa.... | 🟡 |
| ISSU_06 |  | After a Wallet Unit receives a PID or an attestation from a PID Provider or Attestation Provider, it SHALL verify that the PID or attestation it received matches the PID or attestation requested by... | 🟡 |
| ISSU_08 |  | After a Wallet Unit receives a QEAA from a QEAA Provider, it SHALL validate the qualified signature of the QEAA in accordance with Art.32 of the [European Digital Identity Regulation]. For the veri... | 🟡 |
| ISSU_09 |  | After a Wallet Unit receives a PuB-EAA from a PUB-EAA Provider, it SHALL validate the qualified signature of the PuB-EAA in accordance with Art. 32 of the [European Digital Identity Regulation]. Fo... | 🟡 |
| ISSU_11 |  | A Wallet Unit SHALL request the User's approval before storing a PID or attestation obtained from a PID Provider or Attestation Provider. When requesting approval, the Wallet Instance SHALL display... | 🟡 |
| ISSU_11b |  | In case one or more of the verifications in ISSU_06 - ISSU_11 fail, the Wallet Unit SHALL immediately delete the PID or attestation it received. The Wallet Instance SHALL notify the User about the ... | 🟡 |
| ISSU_12a |  | A Wallet Provider SHALL ensure that, when a User instructs their Wallet Unit to request a PID or attestation from a PID Provider or Attestation Provider, the Wallet Unit requests that PID or attest... | 🟡 |
| ISSU_12b |  | During issuance of a PID or a device-bound attestation, the WSCA/WSCD or a key store SHALL generate a new key pair for a new PID or attestation, on request of the PID Provider or Attestation Provid... | 🟡 |
| ISSU_13 |  | A Wallet Provider SHALL ensure that at least one PID Provider is willing to issue a PID complying with [PID Rulebook] to Users of the Wallet Units it provides. | 🟡 |
| ISSU_14 |  | A PID Provider SHALL ensure that all PIDs it issues to Wallet Units comply with the requirements specified in [PID Rulebook]. | 🟡 |
| ISSU_15 |  | A PID Provider SHALL support the OpenID4VCI protocol referenced in ISSU_01 for issuing PIDs. | 🟡 |
| ISSU_16 |  | Empty | 🟡 |
| ISSU_18 |  | A PID Provider SHALL verify the identity of the subject of the PID in compliance with Level of Assurance (LoA) High requirements. *Note: These requirements will be determined by the relevant eID sc... | 🟡 |
| ISSU_18a |  | A PID Provider SHALL ensure that the attributes attested in the PID issued are valid for the identified PID subject at any point of time of PID validity. | 🟡 |
| ISSU_19a |  | A PID Provider SHALL support at least one Wallet Solution, meaning that it is willing and able to issue a PID to a Wallet Unit on request of the User. | 🟡 |
| ISSU_20 |  | To inform its potential PID subjects about the Wallet Solution(s) they can use for requesting a PID, a PID Provider SHALL publish a list of supported Wallet Solutions in such a way that it can be e... | 🟡 |
| ISSU_22 |  | A PID Provider SHALL include its PID Provider access certificate in its Issuer metadata used in the common OpenID4VCI protocol referenced in ISSU_01. | 🟡 |
| ISSU_22a |  | A PID Provider SHALL sign its metadata (as defined in OpenID4VCI) using the private key corresponding to its PID Provider access certificate. | 🟡 |
| ISSU_22b |  | The common OpenID4VCI protocol referenced in requirement ISSU_01, or an EUDI Wallet-specific extension or profile thereof, SHALL enable a PID Provider or Attestation Provider to include its access ... | 🟡 |
| ISSU_23a |  | A Wallet Provider SHALL support at least one PID Provider, meaning that its Wallet Units SHALL be capable of requesting the issuance of a PID from these PID Provider(s), and that the Wallet Provide... | 🟡 |
| ISSU_23b |  | Prior to or during installation of a Wallet Instance, the Wallet Provider SHALL notify the User about the PID Provider(s) that are supported by the Wallet Unit. | 🟡 |
| ISSU_24 |  | A Wallet Unit SHALL authenticate and validate the PID Provider access certificate before requesting the issuance of a PID. The Wallet Unit SHALL verify that the access certificate is authentic and ... | 🟡 |
| ISSU_24a |  | Before requesting the issuance of a PID, the Wallet Unit SHALL verify that the PID Provider is indeed a registered PID Provider. The Wallet Unit SHALL do so using information contained in the PID P... | 🟡 |
| ISSU_26 |  | An Attestation Provider SHALL support the OpenID4VCI protocol referenced in ISSU_01 for issuing attestations. | 🟡 |
| ISSU_27a |  | If the subject of the attestation is a natural person, an Attestation Provider SHALL verify the identity of the subject of the attestation, in compliance with applicable requirements and in accorda... | 🟡 |
| ISSU_27b |  | If applicable, an Attestation Provider SHALL ensure that the attributes attested in the attestation issued are valid for the identified attestation subject. | 🟡 |
| ISSU_27c |  | The Attestation Provider SHALL verify that the User requesting the attestation has the right to receive it. | 🟡 |
| ISSU_31 |  | Empty | 🟡 |
| ISSU_32 |  | An Attestation Provider SHALL include its Attestation Provider access certificate and registration certificate(s) in its Issuer metadata used in the common OpenID4VCI protocol referenced in ISSU_01. | 🟡 |
| ISSU_32a |  | An Attestation Provider SHALL sign its metadata (as defined in OpenID4VCI) using the private key corresponding to its Attestation Provider access certificate. | 🟡 |
| ISSU_33a |  | For the verification of Attestation Provider registration certificates, a Wallet Unit SHALL accept the trust anchors in all Trusted List(s) for Providers of registration certificates. | 🟡 |
| ISSU_34a |  | Before requesting the issuance of an attestation, the Wallet Unit SHALL verify that the Attestation Provider is a registered QEAA Provider, PuB-EAA Provider, or EAA Provider. The Wallet Unit SHALL ... | 🟡 |
| ISSU_35 |  | A PID Provider or Attestation Provider SHALL ensure that all unique elements in a PID or attestation have a negligible chance of having the same value across all PIDs or attestations issued by that... | 🟡 |
| ISSU_35a |  | A Wallet Provider SHALL ensure that all unique elements in a WUA have a negligible chance of having the same value across all WUAs issued by that Wallet Provider. This SHALL include at least a) the... | 🟡 |
| ISSU_35b |  | After issuing a PID, attestation, or WUA, a PID Provider, Attestation Provider or Wallet Provider SHALL discard the values of all unique elements, including at least the ones mentioned in requireme... | 🟡 |
| ISSU_36 |  | When issuing PIDs, attestations, or WUAs in a batch to a Wallet Unit, a PID Provider, Attestation Provider, or Wallet Provider SHALL ensure that the timestamps in these PIDs, attestations, or WUAs ... | 🟡 |
| ISSU_37 |  | A Wallet Provider SHALL ensure that its Wallet Solution supports the following methods for limiting the number of times a User can present the same PID or attestation to Relying Parties: Method A (... | 🟡 |
| ISSU_38 |  | A PID Provider, Attestation Provider, or Wallet Provider SHALL have a policy describing which of the methods A, B, C, or D, it will use to limit the number of times a Wallet Unit may present a sing... | 🟡 |
| ISSU_39 |  | The Commission SHALL create or reference a profile or extension of the OpenID4VCI specification enabling a PID Provider, Attestation Provider, or Wallet Provider to indicate in their OpenID4VCI Iss... | 🟡 |
| ISSU_40 |  | PID Providers, Attestation Providers, and Wallet Providers SHALL indicate in their OpenID4VCI Issuer metadata at least that either method A or method B must be used for a given type of PID, attesta... | 🟡 |
| ISSU_41 |  | To the maximum extent possible, Wallet Providers, PID Providers, and Attestation Providers SHALL ensure that Users do not notice which of the methods A, B, C, or D is used for their PIDs, attestati... | 🟡 |
| ISSU_42 |  | To the maximum extent possible, Wallet Providers, PID Providers, and Attestation Providers SHALL ensure that no User action is needed for the re-issuance of WUAs, PIDs, or attestations. *Note: For ... | 🟡 |
| ISSU_43 |  | The Wallet Unit SHALL request the PID Provider, Attestation Provider, or Wallet Provider to issue PIDs, attestations, or WUAs in batches to the Wallet Unit. All PIDs, attestations, or WUAs in a bat... | 🟡 |
| ISSU_44 |  | The Wallet Unit SHALL present each PID, attestation, or WUA only once to a Relying Party, except when it has fallen back to Method B as specified below, or to another available method. | 🟡 |
| ISSU_45 |  | The Wallet Unit SHALL have a lower limit for the number of unused PIDs, attestations, or WUAs it holds, and SHALL request the issuance of a new batch when this limit is reached. During the first is... | 🟡 |
| ISSU_46 |  | If the Wallet Unit must request a new batch of PIDs, attestations, or WUAs, but is not able to do so because it is offline, the Wallet Unit SHALL warn the User that they are about to lose the possi... | 🟡 |
| ISSU_47 |  | If the Wallet Unit has run out of unused PIDs, attestations, or WUAs, but is not able to request a new batch because it is offline, it SHALL fall back to method B (see requirement 6), or another av... | 🟡 |
| ISSU_48 |  | The Wallet Unit SHALL request the PID Provider, Attestation Provider, or Wallet Provider to issue a single PID, attestation, or WUA to the Wallet Unit. | 🟡 |
| ISSU_49 |  | The Wallet Unit SHALL present that PID, attestation, or WUA multiple times to the same Relying Party or Attestation Provider, or to different Relying Parties or Attestation Providers, when requeste... | 🟡 |
| ISSU_50 |  | The Wallet Unit SHALL request the PID Provider, Attestation Provider, or Wallet Provider to re-issue a PID, attestation, or WUA some time before the one existing in the Wallet Unit expires. The PID... | 🟡 |
| ISSU_51 |  | The Wallet Unit SHALL request the PID Provider, Attestation Provider, or Wallet Provider to issue PIDs, attestations, or WUAs in batches to the Wallet Unit. All PIDs, attestations, or WUAs in a bat... | 🟡 |
| ISSU_52 |  | When a presentation of attributes is requested by multiple Relying Parties, the Wallet Unit SHALL present each PID or attestation in a batch once, in a random order. Similarly, when a WUA is reques... | 🟡 |
| ISSU_53 |  | When all PIDs, attestations, or WUAs in a batch have been presented once, the Wallet Unit SHALL reset the batch, and start presenting each PID, attestation, or WUA in the batch again in a random or... | 🟡 |
| ISSU_54 |  | The Wallet Unit SHALL request the PID Provider, Attestation Provider, or Wallet Provider to re-issue a batch of PIDs, attestations, or WUAs, some time before the batch in the Wallet Unit expires. T... | 🟡 |
| ISSU_55 |  | The Wallet Unit SHALL present a different PID, attestation, or WUA to each different Relying Party or Attestation Provider upon their request. This means that it SHALL comply with Method A for such... | 🟡 |
| ISSU_56 |  | In case a given Relying Party requests attributes from a given type of PID or attestation multiple times, the Wallet Unit MAY present the same PID or attestation to this Relying Party each time. If... | 🟡 |
| ISSU_56a |  | In case a given Attestation Provider requests a WUA multiple times, the Wallet Unit MAY present the same WUA to this Attestation Provider each time. If it does, it SHALL comply with Method B or Met... | 🟡 |
| ISSU_57 |  | The Wallet Unit SHALL keep track of which PID or attestation it has presented to which Relying Party. *Note: To do so, the Wallet Unit can use the unique RP identifier from the extension of the pre... | 🟡 |
| ISSU_57a |  | The Wallet Unit SHALL keep track of which WUA it has presented to which Attestation Provider, using the unique identifier obtained from the respective access certificate. | 🟡 |
| ISSU_58 |  | A Wallet Unit SHALL give its User the option to manually initiate a re-issuance process for any of the PIDs or attestations in their Wallet Unit. *Note: This requirement does not apply for WUAs, si... | 🟡 |
| ISSU_59 |  | After a successful re-issuance, a Wallet Unit SHALL compare the attribute values of the re-issued PID or attestation with those of the existing PID or attestation, and SHALL notify the User in case... | 🟡 |
| ISSU_60 |  | A Wallet Unit SHALL gracefully handle situations in which re-issuance of a PID, attestation, or WUA is refused by the PID Provider, Attestation Provider, or Wallet Provider,for example by attemptin... | 🟡 |
| ISSU_61 |  | A Wallet Unit SHALL support PID or attestation first-time batch issuance with a single User authentication, regardless of the size of the batch. *Note: a) See also requirement WIAM_14. b) This requ... | 🟡 |
| ISSU_62 |  | If a PID, attestation, or WUA was successfully re-issued because the value of one or more of its attributes was changed (including attributes being added or deleted), a Wallet Unit SHOULD delete th... | 🟡 |
| ISSU_63 |  | PID Providers, Attestation Providers, Wallet Providers, and Wallet Units SHALL support the features of [OpenID4VCI] enabling the re-issuance of PIDs, attestations, and WUAs. | 🟡 |
| ISSU_64 |  | PID Providers, Attestation Providers, Wallet Providers, and Wallet Units SHALL support the features of [OpenID4VCI] enabling the batch issuance of PIDs, attestations, and WUAs. | 🟡 |
| ISSU_65 |  | The common OpenID4VCI protocol referenced in requirement ISSU_01, or an EUDI Wallet-specific extension or profile thereof, SHALL enable a PID Provider, Attestation Provider or Wallet Provider to ve... | 🟡 |
| ISSU_66 |  | The common OpenID4VCI protocol referenced in requirement ISSU_01, or an EUDI Wallet-specific extension or profile thereof, SHALL enable an Attestation Provider to verify that the Refresh Token used... | 🟡 |
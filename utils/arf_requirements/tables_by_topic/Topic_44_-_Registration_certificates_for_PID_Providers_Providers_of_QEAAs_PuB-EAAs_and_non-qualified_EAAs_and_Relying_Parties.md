# Topic 44 - Registration certificates for PID Providers, Providers of QEAAs, PuB-EAAs, and non-qualified EAAs, and Relying Parties

| **Requirement ID** | **Legacy ID** | **Description** | **Status** |
|-------------------|---------------|------------------|------------|
| RPRC_01 |  | The Commission SHALL provide a technical specification establishing a common Certificate Policy for registration certificates, covering at least management and selection of signing keys, revocation... | 🟡 |
| RPRC_02 |  | The Commission SHALL ensure that a technical specification is created, describing at least 1. the contents and format of registration certificates for Relying Parties, see the other requirements in... | 🟡 |
| RPRC_03 |  | The contents of a registration certificate SHALL include at least the information required in Annex V of the [CIR 2025/848](https://data.europa.eu/eli/reg_impl/2025/848/oj) regarding registration o... | 🟡 |
| RPRC_04 |  | If the subject of the registration certificate uses the services of an intermediary (see [Topic 52](./annex-2.02-high-level-requirements-by-topic.md#a2330-topic-52-relying-party-intermediaries)), t... | 🟡 |
| RPRC_04a |  | Empty | 🟡 |
| RPRC_05 |  | If the subject of the registration certificate is not a Relying Party (i.e. in the terms of CIR 2025/848, a Service Provider), the certificate SHALL NOT contain the intended use as meant in Annex I... | 🟡 |
| RPRC_08 |  | The EU-wide unique identifier meant in RPRC_07 SHALL be identical in all registration certificates issued for a given entity. *Note: In case the registration certificates issued to an intermediated... | 🟡 |
| RPRC_10 |  | If, during registration, a Relying Party received one or more registration certificates, it SHALL distribute these to all its Relying Party Instances. | 🟡 |
| RPRC_14 |  | If, during registration, a PID Provider, QEAA Provider, PuB-EAA Provider, or non-qualified EAA Provider received a registration certificate, it SHALL distribute it to all its service supply points.... | 🟡 |
| RPRC_15 |  | The contents of a registration certificate issued to a PID Provider, a QEAA Provider, a PuB-EAA Provider, or a non-qualified EAA Provider SHALL contain the type(s) of attestation that this entity i... | 🟡 |
| RPRC_16 |  | Either after receiving a presentation request or as a general User setting, a Wallet Unit SHALL offer the User the possibility to indicate whether the User wants to verify the information registere... | 🟡 |
| RPRC_17 |  | If the User indicated that they want to verify the information registered about the Relying Party and the Relying Party sent a registration certificate to the Wallet Unit, the Wallet Unit SHALL ver... | 🟡 |
| RPRC_18 |  | If the User indicated that they want to verify the information registered about the Relying Party, but the Relying Party did not send a registration certificate to the Wallet Unit, the Wallet Unit ... | 🟡 |
| RPRC_19 |  | If a Relying Party Instance received one or more registration certificates (see RPRC_10), it SHALL include a single registration certificate applicable for its current intended use in each presenta... | 🟡 |
| RPRC_19a |  | A Relying Party Instance SHALL include in each presentation request the following information,  according to the applicable standard's extension mentioned in RPRC_20a: a) the user-friendly name of ... | 🟡 |
| RPRC_20 |  | Relying Party Instances and Wallet Units SHALL support the extension for [ISO/IEC 18013-5] or the extension for [OpenID4VP], as specified in ETSI TS 119 472-2 and amended by a CIR in preparation, a... | 🟡 |
| RPRC_20a |  | Relying Party Instances and Wallet Units SHALL support the extension for [ISO/IEC 18013-5] or the extension for [OpenID4VP], as specified in ETSI TS 119 472-2 and amended by a CIR in preparation, a... | 🟡 |
| RPRC_21 |  | If the User indicated that they want to verify the information registered about a Relying Party and the Wallet Unit retrieved this information either from the registration certificate or from the o... | 🟡 |
| RPRC_22 |  | If a PID Provider or Attestation Provider received a registration certificate (see RPRC_14), it SHALL include the registration certificate in its Issuer metadata used in the common OpenID4VCI proto... | 🟡 |
| RPRC_23 |  | A Wallet Unit SHALL verify that the type of attestation it wants to request from the PID Provider or Attestation Provider is registered by the relevant Registrar, according to ISSU_24a for PID Prov... | 🟡 |
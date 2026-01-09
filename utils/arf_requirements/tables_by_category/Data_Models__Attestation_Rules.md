# Data Models & Attestation Rules

| **Requirement ID** | **Legacy ID** | **Description** | **Status** |
|-------------------|---------------|------------------|------------|
| EW-DM-03-01 | PID_01 | PIDs and PID Providers SHALL comply with all requirements in [PID Rulebook]. | 🟡 |
| EW-DM-03-02 | PID_02 | A PID Provider SHALL issue any PID in both the format specified in ISO/IEC 18013-5 [ISO/IEC 18013-5] and the format specified in [SD-JWT VC]. | 🟡 |
| EW-DM-03-03 | PID_03 | The portrait in a PID SHALL consist of a single portrait image in JPEG format. The portrait image SHALL comply with the quality requirements for a Full Frontal Image Type in ISO/IEC 19794-5 clauses... | 🟡 |
| EW-DM-03-04 | PID_04 | PID Providers SHALL use eu.europa.ec.eudi.pid.1 as the attestation type for ISO/IEC 18013-5-compliant PIDs. | 🟡 |
| EW-DM-03-05 | PID_05 | When issuing a PID compliant with [ISO/IEC 18013-5], a PID Provider SHALL use the value "eu.europa.ec.eudi.pid.1" for the identifier of the namespace for the PID attributes specified in [Section 4.... | 🟡 |
| EW-DM-03-06 | PID_06 | When issuing a PID compliant with [ISO/IEC 18013-5], a PID Provider MAY include attributes that are not defined in the [PID Rulebook](../annex-3/annex-3.01-pid-rulebook.md). If so, these attributes... | 🟡 |
| EW-DM-03-07 | PID_07 | A PID Provider that defines a domestic namespace SHALL publish the namespace, including all attribute identifiers, their definition, presence and encoding format, in an Attestation Rulebook complyi... | 🟡 |
| EW-DM-03-08 | PID_08 | When issuing a PID compliant with [ISO/IEC 18013-5], a PID Provider SHALL include both the attributes and the metadata specified in [CIR 2024/2977] in the PID as (issuer-signed or device-signed) da... | 🟡 |
| EW-DM-03-09 | PID_09 | When issuing a PID compliant with [ISO/IEC 18013-5], a PID Provider SHALL encode each attribute or metadata in the PID as specified in the third column of the tables in [Section 4.2.1 of the PID Ru... | 🟡 |
| EW-DM-03-10 | PID_10 | When issuing a PID compliant with [ISO/IEC 18013-5], a PID Provider SHALL encode each attribute or metadata in the PID in Concise Binary Object Representation (CBOR) according to [RFC 8949]. | 🟡 |
| EW-DM-03-11 | PID_11 | When issuing a PID compliant with [ISO/IEC 18013-5], a PID Provider SHALL ensure that each PID contains at most one attribute with the same attribute identifier. | 🟡 |
| EW-DM-03-12 | PID_12 | When issuing a PID compliant with [ISO/IEC 18013-5], a PID Provider SHALL ensure that the value of all attributes and metadata in the PID is valid at the value of the timestamp in the validFrom ele... | 🟡 |
| EW-DM-03-13 | PID_13 | When issuing a PID compliant with [ISO/IEC 18013-5], a PID Provider SHALL ensure that the issuance_date attribute, if present, is not later than the validFrom element in the MSO, see [ISO/IEC 18013... | 🟡 |
| EW-DM-03-14 | PID_14 | A PID Provider issuing [SD-JWT VC]-compliant PIDs SHALL include the vct claim in their PIDs, where the vct claim SHALL be a URN within the `urn:eudi:pid:` namespace. The type indicated by the vct c... | 🟡 |
| EW-DM-03-15 | PID_15 | Empty | 🟡 |
| EW-DM-03-16 | PID_16 | A PID Provider that defines a domestic type SHALL publish information about the type, including all claim identifiers, their definition, presence and encoding format, in an Attestation Rulebook com... | 🟡 |
| EW-DM-03-17 | PID_17 | When issuing a PID compliant with [SD-JWT VC], a PID Provider SHALL include both the attributes and the metadata specified in [CIR 2024/2977] in the PID as claims. | 🟡 |
| EW-DM-03-18 | PID_18 | When issuing a PID compliant with [SD-JWT VC], a PID Provider SHALL encode each attribute or metadata in the PID as specified in the tables in [Section 5.2 of the PID Rulebook](../annex-3/annex-3.0... | 🟡 |
| EW-DM-03-19 | PID_19 | When issuing a PID compliant with [SD-JWT VC], a PID Provider SHALL ensure that the value of all attributes and metadata in the PID is valid at the value of the timestamp in the nbf claim, if present. | 🟡 |
| EW-DM-03-20 | PID_20 | When issuing a PID compliant with [SD-JWT VC], a PID Provider SHALL ensure that the date_of_issuance claim, if present, is not later than the value of the timestamp in the nbf claim, if present. | 🟡 |
| EW-DM-03-21 | PID_21 | When issuing a PID compliant with [SD-JWT VC], a PID Provider SHALL make all claims (i.e., all top-level properties, all nested properties, and all array entries) selectively disclosable individual... | 🟡 |
| EW-DM-04-001 | mDL_01 | mDLs and mDL Providers SHALL comply with all requirements in [mDL Rulebook]. | 🟡 |
| EW-DM-12-001 | ARB_01a | The Scheme Provider for an Attestation Rulebook describing a type of attestation that is a non-qualified EAA SHALL specify that one or more of the following three common format(s) must be used for ... | 🟡 |
| EW-DM-12-002 | ARB_01b | The Scheme Provider for an Attestation Rulebook describing attestations using the format specified in [SD-JWT VC] SHALL ensure that these attestations comply with the 'SD-JWT VCs' profile specified... | 🟡 |
| EW-DM-12-003 | ARB_02 | The Scheme Provider for an Attestation Rulebook SHALL analyse whether it must be possible for a User to present that type of attestation when the Wallet Unit and the Relying Party are in proximity ... | 🟡 |
| EW-DM-12-004 | ARB_03 | The Scheme Provider for an Attestation Rulebook MAY specify in the Attestation Rulebook that that type of attestation must be issued in the [SD-JWT VC]-compliant format, provided the [SD-JWT VC] sp... | 🟡 |
| EW-DM-12-005 | ARB_04 | If an Attestation Rulebook specifies that a type of attestation can be issued in a format compliant with [W3C VCDM v2.0], the Scheme Provider for that Attestation Rulebook SHALL ensure the Rulebook... | 🟡 |
| EW-DM-12-006 | ARB_05 | The Scheme Provider for an Attestation Rulebook SHALL specify a value for the attestation type, which SHALL be unique within the scope of the EUDI Wallet ecosystem. | 🟡 |
| EW-DM-12-007 | ARB_06 | The Scheme Provider for an Attestation Rulebook SHALL define all attributes that an attestation of that type may contain. This definition SHALL first describe the semantics of each attribute in an ... | 🟡 |
| EW-DM-12-008 | ARB_06a | For ISO/IEC 18013-5-compliant attestations, the Attestation Rulebook SHALL define each attribute within an attribute namespace. An attribute namespace SHALL fully define the identifier, the syntax,... | 🟡 |
| EW-DM-12-009 | ARB_06b | For [SD-JWT VC]-compliant attestations, the Scheme Provider for the Attestation Rulebook SHALL ensure that each claim name is either: - included in the IANA registry for JWT claims, - is a Public N... | 🟡 |
| EW-DM-12-010 | ARB_07 | When determining the attributes to be included in a new attestation type, the Scheme Provider for the applicable Attestation Rulebook SHOULD consider referring to attributes that are already includ... | 🟡 |
| EW-DM-12-011 | ARB_08 | The Scheme Provider for an Attestation Rulebook SHOULD, when specifying a new attribute, take into consideration existing conventions for attribute identifier values and attribute syntaxes. | 🟡 |
| EW-DM-12-012 | ARB_09 | The Scheme Provider for an Attestation Rulebook SHALL specify, for each attribute in the attestation, whether the presence of that attribute is mandatory, optional, or conditional. | 🟡 |
| EW-DM-12-013 | ARB_10 | The Scheme Provider for an Attestation Rulebook for an ISO/IEC 18013-5 compliant attestation MAY define a domestic namespace to specify attributes that are specific to that Rulebook and are not inc... | 🟡 |
| EW-DM-12-014 | ARB_11 | The Scheme Provider for an Attestation Rulebook describing a type of attestation that is a QEAA or a PuB-EAA SHALL include in the Rulebook an attribute as meant in [Annex V](https://eur-lex.europa.... | 🟡 |
| EW-DM-12-015 | ARB_12 | The Scheme Provider for an Attestation Rulebook describing a type of attestation that is a non-qualified EAA SHOULD include an attribute in the Rulebook indicating that the attestation is an EAA. T... | 🟡 |
| EW-DM-12-016 | ARB_13 | The Scheme Provider for an Attestation Rulebook describing a type of attestation that is a QEAA SHALL include in the Rulebook one or more attributes or metadata representing the set of data meant i... | 🟡 |
| EW-DM-12-017 | ARB_14 | The Scheme Provider for an attestation Rulebook describing a type of attestation that is a PuB-EAA SHALL include in the Rulebook one or more attributes or metadata representing the set of data mean... | 🟡 |
| EW-DM-12-018 | ARB_15 | The Scheme Provider for an Attestation Rulebook describing a type of attestation that is a non-qualified EAA SHOULD include in the Rulebook one or more attributes or metadata representing the set o... | 🟡 |
| EW-DM-12-019 | ARB_16 | The Scheme Provider for an Attestation Rulebook describing a type of attestation that is a QEAA or a PuB-EAA SHALL include in the Rulebook one or more attributes representing the set of data meant ... | 🟡 |
| EW-DM-12-020 | ARB_17 | The Scheme Provider for an Attestation Rulebook describing a type of attestation that is a non-qualified EAA SHOULD include in the Rulebook one or more attributes representing the set of data meant... | 🟡 |
| EW-DM-12-021 | ARB_18 | The Scheme Provider for an Attestation Rulebook describing a type of attestation that is a QEAA or a PuB-EAA SHALL include in the Rulebook one or more attributes or metadata representing the set of... | 🟡 |
| EW-DM-12-022 | ARB_19 | The Scheme Provider for an Attestation Rulebook describing a type of attestation that is a non-qualified EAA SHOULD include in the Rulebook one or more attributes representing the set of data meant... | 🟡 |
| EW-DM-12-023 | ARB_20 | The Scheme Provider for an Attestation Rulebook describing a type of attestation that is a QEAA or a PuB-EAA SHALL include in the Rulebook one or more attributes or metadata representing the locati... | 🟡 |
| EW-DM-12-024 | ARB_21 | The Scheme Provider for an Attestation Rulebook describing a type of attestation that is a non-qualified EAA SHOULD include in the Rulebook one or more attributes or metadata representing the locat... | 🟡 |
| EW-DM-12-025 | ARB_22 | The Scheme Provider for an Attestation Rulebook SHALL specify all technical details necessary to ensure interoperability, security, and privacy of that attestation. | 🟡 |
| EW-DM-12-026 | ARB_23 | The Scheme Provider for an Attestation Rulebook describing a type of attestation that is a QEAA or a PuB-EAA SHALL specify which of the revocation mechanisms specified in [Topic 7](./annex-2.02-hig... | 🟡 |
| EW-DM-12-027 | ARB_24 | The Scheme Provider for an Attestation Rulebook describing a type of attestation that is a non-qualified EAA SHALL specify whether that type of EAA must be revocable. If an EAA type must be revocab... | 🟡 |
| EW-DM-12-028 | ARB_25 | The Commission SHALL take measures to ensure that the following information is included in a technical specification: - The identifier of the attribute containing the indication meant in [Annex V](... | 🟡 |
| EW-DM-12-029 | ARB_26 | The Scheme Provider for an Attestation Rulebook describing a type of attestation that is a non-qualified EAA SHOULD define in the Rulebook: - mechanisms allowing a Wallet Unit to verify that the EA... | 🟡 |
| EW-DM-12-030 | ARB_27 | The Scheme Provider for an Attestation Rulebook describing a type of attestation that is a QEAA, PuB-EAA, or non-qualified EAA SHOULD specify in the Rulebook whether a Relying Party receiving the a... | 🟡 |
| EW-DM-12-031 | ARB_28 | An Attribute Scheme Provider SHOULD specify an attribute in an Attestation Rulebook that indicates whether the Attestation Provider during attestation issuance requested a cryptographic binding (as... | 🟡 |
| EW-DM-12-032 | ARB_29 | The Scheme Provider for an Attestation Rulebook describing a type of attestation that is a QEAA, PuB-EAA, or non-qualified EAA SHOULD ensure that the structure and contents of the Attestation Ruleb... | 🟡 |
| EW-DM-12-033 | ARB_30 | If an Attestation Rulebook specifies a [SD-JWT VC]-compliant attestation, the Scheme Provider for that Attestation Rulebook SHALL specify for all claims (i.e., all top-level properties, all nested ... | 🟡 |
| EW-DM-12-034 | ARB_31 | If an Attestation Rulebook specifies a [SD-JWT VC]-compliant attestation, the Scheme Provider for that Attestation Rulebook SHOULD consider defining a Type Metadata Document for it, as defined in C... | 🟡 |
| EW-DM-12-035 | ARB_32 | If an Attestation Rulebook specifies a [SD-JWT VC]-compliant attestation, the Scheme Provider for that Attestation Rulebook SHOULD consider defining a JSON Schema for it, as defined in Section 6.5 ... | 🟡 |
| EW-DM-12-036 | ARB_33 | If a Scheme Provider for an Attestation Rulebook registers an attestation scheme in the catalogue of attestation schemes meant in [Commission Implementing Regulation 2025/1569](http://data.europa.e... | 🟡 |
| EW-DM-12-036 | ARB_34 | The Scheme Provider for an Attestation Rulebook SHALL specify whether that attestation is device-bound or not. | 🟡 |
| EW-DM-28-001 | LP_03 | A legal-person PID SHALL comply with all requirements in the Legal-person PID Rulebook mentioned in LP_01. | 🟡 |
| EW-DM-31-001 | RPACANot_06 | If an Access Certificate Authority is suspended or cancelled (see requirement GenNot_05 above), that Access Certificate Authority SHALL immediately revoke all of its temporally valid access certifi... | 🟡 |
| EW-DM-31-002 | TLPub_03 | The publication of the information referred to in TLPub_01 SHALL take place over a secure channel protecting the authenticity and integrity of the published information. | 🟡 |
| EW-DM-31-003 | TLPub_04 | The technical system mentioned in TLPub_01 SHALL NOT require authentication or prior registration and authorisation of any entity wishing to retrieve the published information. | 🟡 |
| EW-DM-31-004 | TLPub_05 | The information referred to in TLPub_01 SHALL be published in an electronically signed or sealed form that is suitable for automated processing, and in a human-readable format, e.g., through intros... | 🟡 |
| EW-DM-38-001 | WURevocation_03 | Empty | 🟡 |
| EW-DM-38-002 | WURevocation_04 | Empty | 🟡 |
| EW-DM-38-003 | WURevocation_05 | Empty | 🟡 |
| EW-DM-38-004 | WURevocation_06 | Empty | 🟡 |
| EW-DM-38-005 | WURevocation_08 | Empty | 🟡 |
| EW-DM-38-006 | WURevocation_15 | Empty | 🟡 |
| EW-DM-38-007 | WURevocation_17 | Empty | 🟡 |
| EW-DM-38-008 | WURevocation_19a | Empty | 🟡 |
| EW-DM-38-009 | WURevocation_19b | Empty | 🟡 |
| EW-DM-38-010 | WURevocation_20 | Empty | 🟡 |
| EW-DM-38-011 | WURevocation_21 | Empty | 🟡 |
| EW-DM-43-001 | EDP_04 | Empty | 🟡 |
| EW-DM-44-001 | RPRC_01 | The Commission SHALL provide a technical specification establishing a common Certificate Policy for registration certificates, covering at least management and selection of signing keys, revocation... | 🟡 |
| EW-DM-44-002 | RPRC_02 | The Commission SHALL ensure that a technical specification is created, describing at least 1. the contents and format of registration certificates for Relying Parties, see the other requirements in... | 🟡 |
| EW-DM-44-003 | RPRC_03 | The contents of a registration certificate SHALL include at least the information required in Annex V of the [CIR 2025/848](https://data.europa.eu/eli/reg_impl/2025/848/oj) regarding registration o... | 🟡 |
| EW-DM-44-004 | RPRC_04 | If the subject of the registration certificate uses the services of an intermediary (see [Topic 52](./annex-2.02-high-level-requirements-by-topic.md#a2330-topic-52-relying-party-intermediaries)), t... | 🟡 |
| EW-DM-44-005 | RPRC_04a | Empty | 🟡 |
| EW-DM-44-006 | RPRC_05 | If the subject of the registration certificate is not a Relying Party (i.e. in the terms of CIR 2025/848, a Service Provider), the certificate SHALL NOT contain the intended use as meant in Annex I... | 🟡 |
| EW-DM-44-007 | RPRC_06 | The contents of a registration certificate SHALL include a name for the subject of the certificate, in a format suitable for presenting to a User. | 🟡 |
| EW-DM-44-008 | RPRC_07 | The contents of a registration certificate SHALL include an EU-wide unique identifier for the subject of the certificate. | 🟡 |
| EW-DM-44-009 | RPRC_08 | The EU-wide unique identifier meant in RPRC_07 SHALL be identical in all registration certificates issued for a given entity. | 🟡 |
| EW-DM-44-010 | RPRC_09 | A Member State Registrar MAY decide that, during the registration process for Relying Parties, as specified in [Topic 27](./annex-2.02-high-level-requirements-by-topic.md#a2316-topic-27---registrat... | 🟡 |
| EW-DM-44-011 | RPRC_10 | If, during registration, a Relying Party received one or more registration certificates, it SHALL distribute these to all its Relying Party Instances. | 🟡 |
| EW-DM-44-012 | RPRC_11 | The contents of a registration certificate issued to a Relying Party SHALL at least one of the following: a) the URL of a web form provided by the Relying Party, which Users can use to send data de... | 🟡 |
| EW-DM-44-013 | RPRC_12 | The contents of a registration certificate issued to a Relying Party SHALL contain the name and country of the Data Protection Authority supervising the Relying Party. In addition, the registration... | 🟡 |
| EW-DM-44-014 | RPRC_16 | Either after receiving a presentation request or as a general User setting, a Wallet Unit SHALL offer the User the possibility to indicate whether the User wants to verify the information registere... | 🟡 |
| EW-DM-44-015 | RPRC_17 | If the User indicated that they want to verify the information registered about the Relying Party and the Relying Party sent a registration certificate to the Wallet Unit, the Wallet Unit SHALL ver... | 🟡 |
| EW-DM-44-016 | RPRC_18 | If the User indicated that they want to verify the information registered about the Relying Party, but the Relying Party did not send a registration certificate to the Wallet Unit, the Wallet Unit ... | 🟡 |
| EW-DM-44-017 | RPRC_19 | If a Relying Party Instance received one or more registration certificates (see RPRC_10), it SHALL include a single registration certificate applicable for its current intended use in each presenta... | 🟡 |
| EW-DM-44-018 | RPRC_19a | A Relying Party Instance SHALL include in each presentation request the following information,  according to the applicable standard's extension mentioned in RPRC_20a: a) the user-friendly name of ... | 🟡 |
| EW-DM-44-019 | RPRC_20 | Relying Party Instances and Wallet Units SHALL support the extension for [ISO/IEC 18013-5] or the extension for [OpenID4VP], as specified in ETSI TS 119 472-2 and amended by a CIR in preparation, a... | 🟡 |
| EW-DM-44-020 | RPRC_20a | Relying Party Instances and Wallet Units SHALL support the extension for [ISO/IEC 18013-5] or the extension for [OpenID4VP], as specified in ETSI TS 119 472-2 and amended by a CIR in preparation, a... | 🟡 |
| EW-DM-44-021 | RPRC_21 | If the User indicated that they want to verify the information registered about a Relying Party and the Wallet Unit retrieved this information either from the registration certificate or from the o... | 🟡 |
| EW-DM-50-001 | RPT_DPA_03 | Empty | 🟡 |
| EW-DM-50-002 | RPT_DPA_05a | For a report sent to a DPA, the log SHALL contain at least: a) the date and time when the report was sent, b) the name and country of the DPA, and c) the channel and contact information used for in... | 🟡 |
| EW-DM-51-001 | ZKP_01 | A ZKP scheme SHALL provide support for the following generic functions, while hiding all attributes of PIDs or attestations: (i) generation of a proof that an (some) attribute(s) having a specific ... | 🟡 |
| EW-DM-51-002 | ZKP_02 | A ZKP scheme SHALL support proving possession of attestation of a given type. | 🟡 |
| EW-DM-51-003 | ZKP_03 | A ZKP scheme SHOULD support the privacy-preserving binding of an attestation to a PID. In addition to the generic functions defined in ZKP_01, for this use case, a ZKP scheme SHALL provide support ... | 🟡 |
| EW-DM-51-004 | ZKP_05 | A ZKP scheme SHALL be usable in both remote and proximity presentation flows. While the inclusion of ZKP will introduce computational and verification delays, these delays SHALL NOT critically unde... | 🟡 |
| EW-DM-51-005 | ZKP_06 | A ZKP scheme SHOULD be able to generate proofs for already issued PIDs and attestations in the formats specified in [ISO/IEC 18013-5] or [SD-JWT VC]. | 🟡 |
| EW-DM-51-006 | ZKP_07 | A ZKP scheme SHALL NOT introduce any additional communication or information that could be used to track or link User activity during, before, or after proof generation. | 🟡 |
| EW-DM-51-007 | ZKP_08 | A ZKP scheme SHALL rely solely on algorithms standardised by a standardisation organisation recognised by the Commission or in a standard recognised by the Commission. | 🟡 |
| EW-DM-51-008 | ZKP_09 | Use of a ZKP scheme SHALL NOT prevent the Wallet Unit's ability to provide User authentication with Level of Assurance High. | 🟡 |
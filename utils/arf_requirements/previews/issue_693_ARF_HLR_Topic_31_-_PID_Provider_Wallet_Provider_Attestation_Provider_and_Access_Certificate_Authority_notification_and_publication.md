# Preview: Issue #693 - 🟧🟡 ARF HLR Topic 31 - PID Provider, Wallet Provider, Attestation Provider, and Access Certificate Authority notification and publication

**Topic:** Topic 31 - PID Provider, Wallet Provider, Attestation Provider, and Access Certificate Authority notification and publication

**Requirements ARF 2.5.0:** 33
**Requirements ARF 2.7.3:** 37

---

## Diff ARF 2.5.0 → ARF 2.7.3

### ✅ Requirements added in ARF 2.7.3 (4):

- **PPNot_02**: The common set of information to be notified about a PID Provider SHALL include at least: 1. Identification data: i. MS/Country of establishment, ii. Name as registered in an official record, iii. Where applicable: a. A business registration number from an official record, b. Identification data from that official record. 2. PID Provider trust anchors, i.e., public keys and name as per point 1) ii) above, supporting the authentication of PIDs issued by the PID Provider, 3. Trust anchors of Access Certificate Authorities for PID Providers, i.e., public keys and CA name, supporting the authentication of the PID Provider by Wallet Units at the service supply point(s) listed per point 4. below. 4. Service supply point(s), i.e., the URL(s) at which a Wallet Unit can start the process of requesting and obtaining a PID. *Note: a) Relating to point 3. above: PID Provider Access Certificate Authority trust anchors are notified separately from the Access Certificate Authority for Relying Parties (see Section G below), since PID Providers are -legally speaking- not Relying Parties. b) For the concept of an Access Certificate Authority, see also [[Topic 27](./annex-2.02-high-level-requirements-by-topic.md#a2316-topic-27---registration-of-pid-providers-providers-of-qeaas-pub-eaas-and-non-qualified-eaas-and-relying-parties)] and [Section 6.3.2 of the ARF main document](../../architecture-and-reference-framework-main.md#632-pid-provider-or-attestation-provider-registration-and-notification).
- **PPNot_04**: PID Providers SHALL ensure that their PID Provider access certificates can be authenticated using the applicable Access Certificate Authority trust anchors notified to the Commission. *Note: [[Topic 6](./annex-2.02-high-level-requirements-by-topic.md#a234-topic-6---relying-party-authentication-and-user-approval)] describes how access certificates will be used.
- **WPNot_02**: The common set of information to be notified about a Wallet Provider SHALL include: 1. Identification data: i. MS/Country of establishment, ii. Name as registered in an official record, iii. Where applicable: a. Business registration number from an official record, and b. Identification data from the official record. 2. Wallet Provider trust anchors, i.e., public keys and name as per point 1. b. above, supporting the authentication of Wallet Unit Attestations issued by the Wallet Provider. *Note: a) See [[Topic 9](./annex-2.02-high-level-requirements-by-topic.md#a236-topic-9---wallet-unit-attestation)] and [[Topic 38](./annex-2.02-high-level-requirements-by-topic.md#a2322-topic-38---wallet-unit-revocation)] for the definition of the WUA. b) A Wallet Provider does not need an access certificate to interact with Wallet Units.
- **WPNot_06**: If a Wallet Provider is cancelled (see requirement GenNot_05 above), that Wallet Provider SHALL immediately revoke all of its valid WUAs, in accordance with the requirements in [Topic 38](./annex-2.02-high-level-requirements-by-topic.md#a2322-topic-38---wallet-unit-revocation). If a Wallet Provider is suspended, that Wallet Provider and the Member State SHALL agree on the necessary precautionary measures that need to be taken, which MAY include the immediate revocation of all or some of its valid WUAs.

**Total requirements ARF 2.7.3:** 37
**Total requirements ARF 2.5.0:** 33
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

## A. Generic requirements for notification


### ✅ Requirements added in ARF 2.7.3 (1):

- **TLPub_08**: As part of the specifications referred to in TLPub_01, the European Commission SHALL establish technical specifications for ensuring the availability and authenticity of the full history regarding the information notified about PID Providers, Wallet Providers, PuB-EAA Providers, Access Certificate Authorities, and Providers of registration certificates.


### ✅ Requirements added in ARF 2.7.3 (1):

- **TLPub_08**: As part of the specifications referred to in TLPub_01, the European Commission SHALL establish technical specifications for ensuring the availability and authenticity of the full history regarding the information notified about PID Providers, Wallet Providers, PuB-EAA Providers, Access Certificate Authorities, and Providers of registration certificates.

## Diff ARF 2.5.0 → ARF 2.7.3

### ✅ Requirements added in ARF 2.7.3 (4):

- **PPNot_02**: The common set of information to be notified about a PID Provider SHALL include at least: 1. Identification data: i. MS/Country of establishment, ii. Name as registered in an official record, iii. Where applicable: a. A business registration number from an official record, b. Identification data from that official record. 2. PID Provider trust anchors, i.e., public keys and name as per point 1) ii) above, supporting the authentication of PIDs issued by the PID Provider, 3. Trust anchors of Access Certificate Authorities for PID Providers, i.e., public keys and CA name, supporting the authentication of the PID Provider by Wallet Units at the service supply point(s) listed per point 4. below. 4. Service supply point(s), i.e., the URL(s) at which a Wallet Unit can start the process of requesting and obtaining a PID. *Note: a) Relating to point 3. above: PID Provider Access Certificate Authority trust anchors are notified separately from the Access Certificate Authority for Relying Parties (see Section G below), since PID Providers are -legally speaking- not Relying Parties. b) For the concept of an Access Certificate Authority, see also [[Topic 27](./annex-2.02-high-level-requirements-by-topic.md#a2316-topic-27---registration-of-pid-providers-providers-of-qeaas-pub-eaas-and-non-qualified-eaas-and-relying-parties)] and [Section 6.3.2 of the ARF main document](../../architecture-and-reference-framework-main.md#632-pid-provider-or-attestation-provider-registration-and-notification).
- **PPNot_04**: PID Providers SHALL ensure that their PID Provider access certificates can be authenticated using the applicable Access Certificate Authority trust anchors notified to the Commission. *Note: [[Topic 6](./annex-2.02-high-level-requirements-by-topic.md#a234-topic-6---relying-party-authentication-and-user-approval)] describes how access certificates will be used.
- **WPNot_02**: The common set of information to be notified about a Wallet Provider SHALL include: 1. Identification data: i. MS/Country of establishment, ii. Name as registered in an official record, iii. Where applicable: a. Business registration number from an official record, and b. Identification data from the official record. 2. Wallet Provider trust anchors, i.e., public keys and name as per point 1. b. above, supporting the authentication of Wallet Unit Attestations issued by the Wallet Provider. *Note: a) See [[Topic 9](./annex-2.02-high-level-requirements-by-topic.md#a236-topic-9---wallet-unit-attestation)] and [[Topic 38](./annex-2.02-high-level-requirements-by-topic.md#a2322-topic-38---wallet-unit-revocation)] for the definition of the WUA. b) A Wallet Provider does not need an access certificate to interact with Wallet Units.
- **WPNot_06**: If a Wallet Provider is cancelled (see requirement GenNot_05 above), that Wallet Provider SHALL immediately revoke all of its valid WUAs, in accordance with the requirements in [Topic 38](./annex-2.02-high-level-requirements-by-topic.md#a2322-topic-38---wallet-unit-revocation). If a Wallet Provider is suspended, that Wallet Provider and the Member State SHALL agree on the necessary precautionary measures that need to be taken, which MAY include the immediate revocation of all or some of its valid WUAs.


| Status | **Index** | **Requirement specification** | **IT-Wallet Mapping & Documentation** |
|---|---------|------------------|-----------------------------------|
| 🟡 | GenNot_01 | Member States SHALL notify all PID Providers, PuB-EAA Providers, Wallet Providers, Access Certificate Authorities, and Providers of registration certificates to the European Commission, according all relevant requirements in [Technical Specification 2](../../technical-specifications/ts2-notification-publication-provider-information.md). |  |
| 🟡 | GenNot_02 | As part of [Technical Specification 2] referred to in GenNot_01, the European Commission SHALL establish standard operating procedures for the notification of a PID Provider, PuB-EAA Provider, Wallet Provider, Access Certificate Authority, or Provider of registration certificates to the Commission. *Note: The outcome of the notification procedure is the publication of the information notified by the Member State according to [Article 5a](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32024R1183#d1e1347-1-1) (18) in a machine and human readable manner using the common system mentioned in Section H, TLPub_01. | Pending: Not yet established, planned at EU level. |
| 🟡 | GenNot_03 | The common system mentioned in GenNot_01 SHALL enable: - A secure notification channel between Member States and the Commission for all notifications. - A notification, verification, and publication process and associated validation steps (with follow-up and monitoring) at the Commission side. - Collected data to be processed, consolidated, signed or sealed, and published in both a machine-processable Trusted List and in a human-readable format, manually and/or automatically using e.g. a web service and/or API. | Pending: Not yet established, planned at EU level. |
| 🟡 | GenNot_04 | As regard to GenNot_03, second bullet, the Commission SHALL verify whether the notified data is complete and meets the technical specifications, while the Member States SHALL be responsible for the correctness of the notified information. | Pending: Not yet established, planned at EU level. |
| 🟡 | GenNot_05 | As part of the specifications referred to in GenNot_01, the European Commission SHALL establish standard operating procedures for the suspension or cancellation of a PID Provider, PuB-EAA Provider, Wallet Provider, Access Certificate Authority, or Provider of registration certificates. These operating procedures SHALL include unambiguous conditions for suspension or cancellation. As an outcome of the suspension or cancellation procedure, the status of the suspended or cancelled PID Provider, PuB-EAA Provider, Wallet Provider, Access Certificate Authority or Provider of registration certificates in the Trusted List SHALL be changed to Invalid. |  |
| 🟡 | PPNot_01 | The European Commission SHALL establish technical specifications for the common set of information to be notified about PID Providers. | Pending: Not yet established, planned at EU level. |
| 🟡 | PPNot_02 | The common set of information to be notified about a PID Provider SHALL include at least: 1. Identification data: i. MS/Country of establishment, ii. Name as registered in an official record, iii. Where applicable: a. A business registration number from an official record, b. Identification data from that official record. 2. PID Provider trust anchors, i.e., public keys and name as per point 1) ii) above, supporting the authentication of PIDs issued by the PID Provider, 3. Trust anchors of Access Certificate Authorities for PID Providers, i.e., public keys and CA name, supporting the authentication of the PID Provider by Wallet Units at the service supply point(s) listed per point 4. below. 4. Service supply point(s), i.e., the URL(s) at which a Wallet Unit can start the process of requesting and obtaining a PID. *Note: a) Relating to point 3. above: PID Provider Access Certificate Authority trust anchors are notified separately from the Access Certificate Authority for Relying Parties (see Section G below), since PID Providers are -legally speaking- not Relying Parties. b) For the concept of an Access Certificate Authority, see also [[Topic 27](./annex-2.02-high-level-requirements-by-topic.md#a2316-topic-27---registration-of-pid-providers-providers-of-qeaas-pub-eaas-and-non-qualified-eaas-and-relying-parties)] and [Section 6.3.2 of the ARF main document](../../architecture-and-reference-framework-main.md#632-pid-provider-or-attestation-provider-registration-and-notification). |  |
| 🟡🟧 | PPNot_03 | PID Providers SHALL ensure that all PIDs they issue can be authenticated using the PID Provider trust anchors notified to the Commission. | Pending: Not yet established, planned at EU level. |
| 🟡 | PPNot_04 | PID Providers SHALL ensure that their PID Provider access certificates can be authenticated using the applicable Access Certificate Authority trust anchors notified to the Commission. *Note: [[Topic 6](./annex-2.02-high-level-requirements-by-topic.md#a234-topic-6---relying-party-authentication-and-user-approval)] describes how access certificates will be used. |  |
| 🟡🟧 | PPNot_05 | PID Provider trust anchors SHALL be accepted because of their secure notification by the Member States to the Commission and by their publication in the corresponding Commission-compiled PID Provider Trusted List which is sealed by the Commission. | Pending: Not yet established, planned at EU level. |
| 🟡🟧 | PPNot_06 | Access Certificate Authority trust anchors SHALL be accepted because of their secure notification by the Member States to the Commission and by their publication in the corresponding Commission-compiled Access Certificate Authority Trusted List which is signed or sealed by the Commission. |  |
| 🟡🟧 | PPNot_07 | The format of the PID Provider Trusted List SHALL comply with ETSI TS 119 612 v2.1.1 or with a suitable profile similarly derived from ETSI TS 102 231. | Pending: Not yet established, planned at EU level. |
| 🟡 | WPNot_01 | The European Commission SHALL establish technical specifications for the common set of information to be notified about Wallet Providers. | Pending: Not yet established, planned at EU level. |
| 🟡 | WPNot_02 | The common set of information to be notified about a Wallet Provider SHALL include: 1. Identification data: i. MS/Country of establishment, ii. Name as registered in an official record, iii. Where applicable: a. Business registration number from an official record, and b. Identification data from the official record. 2. Wallet Provider trust anchors, i.e., public keys and name as per point 1. b. above, supporting the authentication of Wallet Unit Attestations issued by the Wallet Provider. *Note: a) See [[Topic 9](./annex-2.02-high-level-requirements-by-topic.md#a236-topic-9---wallet-unit-attestation)] and [[Topic 38](./annex-2.02-high-level-requirements-by-topic.md#a2322-topic-38---wallet-unit-revocation)] for the definition of the WUA. b) A Wallet Provider does not need an access certificate to interact with Wallet Units. |  |
| 🟡🟧 | WPNot_03 | Wallet Providers SHALL ensure that all WUAs they issue can be authenticated using the trust anchors notified to the Commission. | Pending: Not yet established, planned at EU level. |
| 🟡🟧 | WPNot_04 | Wallet Provider trust anchors SHALL be accepted because of their secure notification by the Member States to the Commission and by their publication in the corresponding Commission-compiled Wallet Provider Trusted List which is sealed by the Commission. | Pending: Not yet established, planned at EU level. |
| 🟡🟧 | WPNot_05 | The format of the Wallet Provider Trusted List SHALL comply with ETSI TS 119 612 v2.1.1 or with a suitable profile similarly derived from ETSI TS 102 231. | Pending: Not yet established, planned at EU level. |
| 🟡 | WPNot_06 | If a Wallet Provider is cancelled (see requirement GenNot_05 above), that Wallet Provider SHALL immediately revoke all of its valid WUAs, in accordance with the requirements in [Topic 38](./annex-2.02-high-level-requirements-by-topic.md#a2322-topic-38---wallet-unit-revocation). If a Wallet Provider is suspended, that Wallet Provider and the Member State SHALL agree on the necessary precautionary measures that need to be taken, which MAY include the immediate revocation of all or some of its valid WUAs. |  |
| 🟡 | PuBPNot_01 | The European Commission SHALL establish technical specifications for the common set of information to be notified about PuB-EAA Providers. |  |
| 🟡 | PuBPNot_02 | The common set of information to be notified by Member States about PuB-EAA Providers SHALL include at least: 1. Identification data: i. MS/Country of establishment, ii. Name as registered in an official record, iii. Where applicable: a. Registration number as in official record, and b. Official record identification data. iv. Identification data of the Union or national law under which a. Either the PuB-EAA Provider is established as the responsible body for the Authentic Source based on which the electronic attestation of attributes is issued, or b. The PuB-EAA Provider is the body designated to act on behalf of the responsible body referred to in point 1. iv. a. v.The conformity assessment report issued by a conformity assessment body, confirming that the requirements set out in paragraphs 1, 2 and 6 of [Article 45f](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32024R1183#d1e3902-1-1) are met. 2. Service supply point(s), i.e., the URL(s) at which a Wallet Unit can start the process of requesting and obtaining a PuB-EAA from the PuB-EAA Provider. |  |
| 🟡 | PuBPNot_03 | The format of the PuB-EAA Provider Trusted List SHALL comply with ETSI TS 119 612 v2.1.1 or with a suitable profile similarly derived from ETSI TS 102 231. |  |
| 🟡 | RPACANot_01 | The European Commission SHALL establish technical specifications for the common set of information to be notified about Access Certificate Authorities and Providers of registration certificates. |  |
| 🟡 | RPACANot_02 | The common set of information to be notified about an Access Certificate Authority or a Provider of registration certificates SHALL include: 1. Identification data: i) Member State or country of establishment, ii) Name as registered in an official record, iii) Where applicable: - A business registration number from an official record, - Identification data from that official record. 2. Trust anchors of the Access Certificate Authority or Provider of registration certificates, i.e., public keys and name as per point 1) ii), supporting the authentication of Relying Parties, PID Providers, QEAA Providers, PuB-EAA Providers, and non-qualified EAA Providers by Wallet Units. |  |
| 🟡 | RPACANot_03 | Relying Parties, PID Providers, QEAA Providers, PuB-EAA Providers, and non-qualified EAA Providers SHALL ensure that their access certificates can be authenticated using the trust anchors of an Access Certificate Authority notified to the Commission. |  |
| 🟡 | RPACANot_03a | Relying Parties, PID Providers, QEAA Providers, PuB-EAA Providers, and non-qualified EAA Providers SHALL ensure that their registration certificates, if issued to them, can be authenticated using the trust anchors of a Provider of registration certificates notified to the Commission. |  |
| 🟡 | RPACANot_04 | The trust anchors of Access Certificate Authorities and Providers of registration certificates SHALL be accepted because of their secure notification by the Member States to the Commission and by their publication in the corresponding Commission-compiled Trusted Lists, which are signed or sealed by the Commission. |  |
| 🟡 | RPACANot_05 | The format of the Trusted Lists mentioned in RPACANot_04 SHALL comply with ETSI TS 119 612 v2.1.1 or with a suitable profile similarly derived from ETSI TS 102 231. |  |
| 🟡 | RPACANot_06 | If an Access Certificate Authority is suspended or cancelled (see requirement GenNot_05 above), that Access Certificate Authority SHALL immediately revoke all of its temporally valid access certificates. *Note: This implies that if an intermediary obtained its access certificates from an Access Certificate Authority that is suspended or cancelled, any intermediated Relying Parties depending on that intermediary will not be able to request attributes from Wallet Units, even though it has valid registration certificates. Such an intermediated Relying Party will either have to transit to another intermediary (which has access certificates issued by an active Access Certification Authority) or wait until the original intermediary obtains new access certificates either from another Access CA or from the original one, once that CA can continue its operations. |  |
| 🟡 | RPACANot_07 | If a Provider of registration certificates is suspended or cancelled (see requirement GenNot_05 above), that Provider SHALL immediately revoke all of its valid registration certificates (if any). Moreover, the corresponding Registrar SHALL prohibit all access to the registry entries published online per Reg_03 and Reg_04. |  |
| 🟡 | TLPub_01 | The European Commission SHALL establish technical specifications for the system enabling the publication by the Commission of the information notified by the Member States regarding PID Providers, Wallet Providers, PuB-EAA Providers, Access Certificate Authorities, and Providers of registration certificates. |  |
| 🟡 | TLPub_02 | The European Commission SHALL establish technical specifications for the set of information to be published about PID Providers, Wallet Providers, PuB-EAA Providers, Access Certificate Authorities and Providers of registration certificates, based on the information notified by the Member States. *Note: The information to be published MAY be different from the information to be notified per requirements PPNot_01, WPNot_01, PuBPNot_01, and RPACANot_01 above, respectively. |  |
| 🟡 | TLPub_03 | The publication of the information referred to in TLPub_01 SHALL take place over a secure channel protecting the authenticity and integrity of the published information. |  |
| 🟡 | TLPub_04 | The technical system mentioned in TLPub_01 SHALL NOT require authentication or prior registration and authorisation of any entity wishing to retrieve the published information. |  |
| 🟡 | TLPub_05 | The information referred to in TLPub_01 SHALL be published in an electronically signed or sealed form that is suitable for automated processing, and in a human-readable format, e.g., through introspection and display facilities, over an authenticated channel. |  |
| 🟡 | TLPub_06 | The Commission SHALL publish in the OJEU the locations of the Trusted Lists for PID Providers, Wallet Providers, PuB-EAA Providers, Access Certificate Authorities, and Providers of registration certificates. |  |
| 🟡 | TLPub_07 | The Commission SHALL publish in the OJEU the trust anchors to be used for verifying the signature or seal mentioned in TLPub_05. |  |
| 🟡 | TLPub_08 | As part of the specifications referred to in TLPub_01, the European Commission SHALL establish technical specifications for ensuring the availability and authenticity of the full history regarding the information notified about PID Providers, Wallet Providers, PuB-EAA Providers, Access Certificate Authorities, and Providers of registration certificates. |  |---

## D. Requirements for the notification of QEAA Providers

**Section content [MODIFIED]:**

There is no notification of QEAA Provider foreseen by the [European Digital Identity Regulation], except for establishing the [Art. 22](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=uriserv%3AOJ.L_.2014.257.01.0073.01.ENG#d1e2162-73-1) Trusted List once a qualified status is granted. QTSPs issuing QEAAs to Wallet Units SHALL abide by the Implementing Act to be adopted under [Art. 45d](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32024R1183#d1e3849-1-1)(5).

---

## E. Requirements for the notification of PuB-EAA Providers

**Section introduction [MODIFIED]:**

This notification is pursuant to [Art.45f](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32024R1183#d1e3902-1-1)(3) and to the implementing acts to be adopted pursuant to [Art.45f](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32024R1183#d1e3902-1-1)(7). It should be noted that the purpose of this notification is mainly to the attention of QTSPs issuing qualified certificates for electronic signatures or seals to those public sector bodies referred to in [Article 3](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32024R1183#d1e739-1-1), point (46), and identified as the issuer in the PuB-EAA. The Trusted List compiled by the Commission is deemed to be a constitutive list of such [Art.3](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32024R1183#d1e739-1-1)(46) bodies recognised for issuing PUB-EAAs. Consequently, QTSPs are expected to verify such lists prior to issuing a qualified certificate to any entity claiming to be a [Art.3](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32024R1183#d1e739-1-1)(46) body.

| **Index**    | **Requirement specification** | **IT-Wallet Mapping & Documentation** |
|---|--------------|------------------------------|---------------------------------------|
| 🟡 | PuBPNot_01   | The European Commission SHALL establish technical specifications for the common set of information to be notified about PuB-EAA Providers. | Pending: Not yet established, planned at EU level. |
| 🟡 | PuBPNot_02   | The common set of information to be notified by Member States about PuB-EAA Providers SHALL include at least: **1. Identification data: i. MS/Country of establishment, ii. Name as registered in an official record, iii. Where applicable: a. Registration number as in official record, and b. Official record identification data. iv. Identification data of the Union or national law under which a. Either the PuB-EAA Provider is established as the responsible body for the Authentic Source based on which the electronic attestation of attributes is issued, or b. The PuB-EAA Provider is the body designated to act on behalf of the responsible body referred to in point 1. iv. a. v.The conformity assessment report issued by a conformity assessment body, confirming that the requirements set out in paragraphs 1, 2 and 6 of [Article 45f](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32024R1183#d1e3902-1-1) are met. 2. Service supply point(s), i.e., the URL(s) at which a Wallet Unit can start the process of requesting and obtaining a PuB-EAA from the PuB-EAA Provider. [MODIFIED]** | Pending: Not yet established, planned at EU level. |
| 🟡 | PuBPNot_03   | The format of the PuB-EAA Provider Trusted List SHALL comply with ETSI TS 119 612 v2.1.1 or with a suitable profile similarly derived from ETSI TS 102 231. | Pending: Not yet established, planned at EU level. |

---

## F. Requirements for the notification of non-qualified EAA Providers

**Section content [MODIFIED]:**

There is no notification of non-qualified EAA Providers foreseen by the [European Digital Identity Regulation]. As stated in [[Topic 12](#a2312-topic-12---attestation-rulebooks)], the Schema Provider for an Attestation Rulebook describing a type of attestation that is an EAA defines in the Rulebook the mechanisms allowing a Relying Party to obtain, in a trustworthy manner, the trust anchor(s) of EAA Providers issuing this type of EAA.

---

## G. Requirements for the notification of Access Certificate Authorities and Providers of registration certificates

**Section introduction [MODIFIED]:**

Access Certificate Authorities (CA) are responsible for signing access certificates they issue to PID Providers, QEAA Providers, PuB-EAA Providers, and non-qualified EAA Providers, as well as to Relying Parties. For more information about Access Certificate Authorities, see [[Topic 27](#a2327-topic-27---registration-of-pid-providers-providers-of-qeaas-pub-eaas-and-non-qualified-eaas-and-relying-parties)].

Providers of registration certificates are responsible for signing registration certificates they issue to PID Providers, QEAA Providers, PuB-EAA Providers, and non-qualified EAA Providers, as well as to Relying Parties. For more information about Access Certificate Authorities, see [[Topic 44](#a2344-topic-44---registration-certificates-for-pid-providers-providers-of-qeaas-pub-eaas-and-non-qualified-eaas-and-relying-parties)].

| **Index**     | **Requirement specification** | **IT-Wallet Mapping & Documentation** |
|---|---------------|------------------------------|---------------------------------------|
| 🟡 | RPACANot_01   | The European Commission SHALL establish technical specifications for the common set of information to be notified about Access Certificate Authorities and Providers of registration certificates. | |
| 🟡 | RPACANot_02   | The common set of information to be notified about an Access Certificate Authority or a Provider of registration certificates SHALL include: 1. Identification data: i) Member State or country of establishment, ii) Name as registered in an official record, iii) Where applicable: - A business registration number from an official record, - Identification data from that official record. 2. Trust anchors of the Access Certificate Authority or Provider of registration certificates, i.e., public keys and name as per point 1) ii), supporting the authentication of Relying Parties, PID Providers, QEAA Providers, PuB-EAA Providers, and non-qualified EAA Providers by Wallet Units. | |
| 🟡 | RPACANot_03   | Relying Parties, PID Providers, QEAA Providers, PuB-EAA Providers, and non-qualified EAA Providers SHALL ensure that their access certificates can be authenticated using the trust anchors of an Access Certificate Authority notified to the Commission. | |
| 🟡 | RPACANot_03a  | Relying Parties, PID Providers, QEAA Providers, PuB-EAA Providers, and non-qualified EAA Providers SHALL ensure that their registration certificates, if issued to them, can be authenticated using the trust anchors of a Provider of registration certificates notified to the Commission. | |
| 🟡 | RPACANot_04   |The trust anchors of Access Certificate Authorities and Providers of registration certificates SHALL be accepted because of their secure notification by the Member States to the Commission and by their publication in the corresponding Commission-compiled Trusted Lists, which are signed or sealed by the Commission.  | |
| 🟡🟧 | RPACANot_05   | The format of the Trusted Lists mentioned in RPACANot_04 SHALL comply with ETSI TS 119 612 v2.1.1 or with a suitable profile similarly derived from ETSI TS 102 231. | Pending: Not yet established, planned at EU level. |
| 🟡 | RPACANot_06   | If an Access Certificate Authority is suspended or cancelled (see requirement GenNot_05 above), that Access Certificate Authority SHALL immediately revoke all of its temporally valid access certificates. *Note: This implies that if an intermediary obtained its access certificates from an Access Certificate Authority that is suspended or cancelled, any intermediated Relying Parties depending on that intermediary will not be able to request attributes from Wallet Units, even though it has valid registration certificates. Such an intermediated Relying Party will either have to transit to another intermediary (which has access certificates issued by an active Access Certification Authority) or wait until the original intermediary obtains new access certificates either from another Access CA or from the original one, once that CA can continue its operations.* | |
| 🟡 | RPACANot_07   | If a Provider of registration certificates is suspended or cancelled (see requirement GenNot_05 above), that Provider SHALL immediately revoke all of its valid registration certificates (if any). Moreover, the corresponding Registrar SHALL prohibit all access to the registry entries published online per Reg_03 and Reg_04. | |

---

## H. Requirements for the publication of Trusted Lists compiled by the Commission

| **Index** | **Requirement specification** | **IT-Wallet Mapping & Documentation** |
|---|-----------|------------------------------|---------------------------------------|
| 🟡 | TLPub_01  | The European Commission SHALL establish technical specifications for the system enabling the publication by the Commission of the information notified by the Member States regarding PID Providers, Wallet Providers, PuB-EAA Providers, Access Certificate Authorities, and Providers of registration certificates. | |
| 🟡 | TLPub_02  | The European Commission SHALL establish technical specifications for the set of information to be published about PID Providers, Wallet Providers, PuB-EAA Providers, Access Certificate Authorities and Providers of registration certificates, based on the information notified by the Member States. *Note: The information to be published MAY be different from the information to be notified per requirements PPNot_01, WPNot_01, PuBPNot_01, and RPACANot_01 above, respectively.* | |
| 🟡 | TLPub_03  | The publication of the information referred to in TLPub_01 SHALL take place over a secure channel protecting the authenticity and integrity of the published information. | Pending: Not yet established, planned at EU level. |
| 🟡 | TLPub_04  | The technical system mentioned in TLPub_01 SHALL NOT require authentication or prior registration and authorisation of any entity wishing to retrieve the published information. | Pending: Not yet established, planned at EU level. |
| 🟡 | TLPub_05  | The information referred to in TLPub_01 SHALL be published in an electronically signed or sealed form that is suitable for automated processing, and in a human-readable format, e.g., through introspection and display facilities, over an authenticated channel. | Pending: Not yet established, planned at EU level. |
| 🟡 | TLPub_06  | The Commission SHALL publish in the OJEU the locations of the Trusted Lists for PID Providers, Wallet Providers, PuB-EAA Providers, Access Certificate Authorities, and Providers of registration certificates. | Pending: Not yet established, planned at EU level. |
| 🟡 | TLPub_07  | The Commission SHALL publish in the OJEU the trust anchors to be used for verifying the signature or seal mentioned in TLPub_05. | Pending: Not yet established, planned at EU level. |
| 🟡 | TLPub_08  | As part of the specifications referred to in TLPub_01, the European Commission SHALL establish technical specifications for ensuring the availability and authenticity of the full history regarding the information notified about PID Providers, Wallet Providers, PuB-EAA Providers, Access Certificate Authorities, and Providers of registration certificates. | |

---

## Summary of Changes in ARF 2.7.3

### Modified Requirements:

**WPNot_02**: Detailed specification added
- **OLD**: Listed as "..." (incomplete)
- **NEW**: Full specification with identification data and trust anchors
- Added two explanatory notes about WUA definition and access certificate

**PuBPNot_02**: Detailed specification added
- **OLD**: Listed as "..." (incomplete)
- **NEW**: Comprehensive specification including identification data, legal basis, conformity assessment, and service supply points

### New Section Content:

**Section D (QEAA Providers)**: Explanatory text added
- Clarifies no notification foreseen except Art. 22 Trusted List
- References Implementing Act under Art. 45d(5)

**Section E (PuB-EAA Providers)**: Extended introduction added
- Explains purpose of notification for QTSPs
- Clarifies Trusted List is constitutive for Art. 3(46) bodies
- Establishes verification requirement for QTSPs

**Section F (non-qualified EAA Providers)**: Explanatory text added
- Clarifies no notification foreseen by Regulation
- References Topic 12 for trust anchor mechanisms

**Section G introduction**: Extended description added
- Clarifies role of Access Certificate Authorities
- Adds new paragraph about Providers of registration certificates
- References Topics 27 and 44

### No Changes to Other Requirements:

All requirements in sections A (Generic), B (PID Providers), C (WPNot_01/03/04/05/06), E (PuBPNot_01/03), G (RPACANot_01-07), and H (TLPub_01-08) remain substantively unchanged in their requirement text.

### Overall Assessment:

Topic 31 shows moderate enhancement with two previously incomplete requirements now fully specified (WPNot_02, PuBPNot_02) and substantial addition of explanatory text across multiple sections. The changes primarily:

1. **Complete specifications**: Fill in missing details for Wallet Provider and PuB-EAA Provider notification data
2. **Add context**: Provide regulatory and legal context for QEAA, PuB-EAA, and non-qualified EAA providers
3. **Clarify roles**: Better explain the distinction between Access CAs and Providers of registration certificates
4. **Legal grounding**: Add references to specific articles of the European Digital Identity Regulation

The notification and publication framework remains stable with enhancements focused on completeness and clarity rather than structural changes. All requirements remain assigned to Commission/Member States as appropriate.

---

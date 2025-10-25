# Certificate Requirements Analysis from Annex 2 High-Level Requirements

## Overview

This document extracts and analyzes all certificate-related requirements from the Annex 2 High-Level Requirements document, focusing on X.509 certificates, registration certificates, access certificates, and onboarding/registration of wallet providers, relying parties, and credential issuers.

## Extracted Certificate-Related Requirements

### 1. Access Certificates for Relying Parties

#### RPA_01 - Relying Party Authentication
- **UID**: RPA_01
- **Requirement**: The Wallet Unit used by a User, as well as the Relying Party Instance used by the Relying Party, SHALL implement a mechanism for Relying Party authentication in PID or attestation presentation transactions. This mechanism SHALL: enable the Wallet Unit to identify and authenticate the Relying Party, enable the Wallet Unit to verify that the request from the Relying Party was not copied and replayed, use Relying Party Instance access certificates issued in accordance with Topic 27.

#### RPA_04 - Trust Anchor Acceptance
- **UID**: RPA_04
- **Requirement**: For the verification of Relying Party Instance access certificates, a Wallet Unit SHALL accept the trust anchors in the Trusted List(s) of Relying Party Access Certificate Authorities of all Member States.

### 2. Access Certificates for PID Providers and Attestation Providers

#### PPNot_04 - PID Provider Access Certificates
- **UID**: PPNot_04
- **Requirement**: PID Providers SHALL ensure that their PID Provider access certificates can be authenticated using the applicable Access Certificate Authority trust anchors notified to the Commission.

#### RPACANot_03 - Access Certificate Authentication
- **UID**: RPACANot_03
- **Requirement**: Relying Parties, PID Providers, QEAA Providers, PuB-EAA Providers, and non-qualified EAA Providers SHALL ensure that their access certificates can be authenticated using the trust anchors of an Access Certificate Authority notified to the Commission.

### 3. Registration Certificates

#### RPRC_01 - Certificate Policy for Registration Certificates
- **UID**: RPRC_01
- **Requirement**: The Commission SHALL provide a technical specification establishing a common Certificate Policy for registration certificates, covering at least management and selection of signing keys, revocation and lifecycle management of registration certificates on individual intended use level.

#### RPRC_02 - Technical Specification for Registration Certificates
- **UID**: RPRC_02
- **Requirement**: The Commission SHALL ensure that a technical specification is created, describing at least:
1. the contents and format of registration certificates for Relying Parties
2. the signing method(s) used to ensure the authenticity of the registration certificate
3. the trust infrastructure necessary for signing registration certificates and for verifying these signatures, including the use of Trusted Lists to establish trust in Providers of registration certificates and to distribute their trust anchors to Wallet Units
4. the method used for binding each registration certificate to the access certificate that will be used in the same presentation request
5. whether or not a registration certificate must have a validity period
6. the method to be used for revocation of registration certificates

### 4. Access Certificate Authorities

#### Reg_10 - Access Certificate Issuance
- **UID**: Reg_10
- **Requirement**: A Member State SHALL ensure that an Access Certificate Authority notified according to Topic 31 issues an access certificate to all PID Providers, QEAA Providers, PuB-EAA Providers, non-qualified EAA Providers, and Relying Parties registered in one of the Member State's registries.

#### Reg_11 - Common Certificate Policy
- **UID**: Reg_11
- **Requirement**: A Member State SHALL ensure that the issuance process of access certificates by their notified Access Certificate Authority(s) complies with a common Certificate Policy for Access Certificate Authority.

#### Reg_12 - Technical Specifications for Certificate Policy
- **UID**: Reg_12
- **Requirement**: The Commission SHALL provide technical specifications establishing the common Access Certificate Authority Certificate Policy mentioned in Reg_11.

#### Reg_13 - Certificate Transparency
- **UID**: Reg_13
- **Requirement**: The common Certificate Policy mentioned in Reg_12 SHALL require that an Access Certificate Authority logs all issued certificates for Certificate Transparency (CT).

#### Reg_14 - Certificate Revocation
- **UID**: Reg_14
- **Requirement**: The common Certificate Policy mentioned in Reg_12 SHALL require that an Access Certificate Authority provides one or more method(s) to revoke the access certificates it issued.

#### Reg_15 - Revocation Policy
- **UID**: Reg_15
- **Requirement**: The common Certificate Policy mentioned in Reg_12 SHALL include a policy for revocation, which SHALL require that an Access Certificate Authority revokes an access certificate at least when:
- the certificate subject which is a Relying Party is suspended or cancelled by the respective Registrar
- the certificate subject which is a PID Provider, QEAA Provider, PuB-EAA Provider, or non-qualified EAA Provider is suspended or cancelled by the respective Registrar
- on request of the certificate subject, or
- on request of a competent national authority

#### Reg_16 - Certificate Profile
- **UID**: Reg_16
- **Requirement**: The common Certificate Policy mentioned in Reg_12 SHALL specify the profile of access certificates in detail.

### 5. Trust Anchors and Trusted Lists

#### PPNot_05 - PID Provider Trust Anchors
- **UID**: PPNot_05
- **Requirement**: PID Provider trust anchors SHALL be accepted because of their secure notification by the Member States to the Commission and by their publication in the corresponding Commission-compiled PID Provider Trusted List which is sealed by the Commission.

#### PPNot_06 - Access Certificate Authority Trust Anchors
- **UID**: PPNot_06
- **Requirement**: Access Certificate Authority trust anchors SHALL be accepted because of their secure notification by the Member States to the Commission and by their publication in the corresponding Commission-compiled Access Certificate Authority Trusted List which is signed or sealed by the Commission.

#### PPNot_07 - Trusted List Format
- **UID**: PPNot_07
- **Requirement**: The format of the PID Provider Trusted List SHALL comply with ETSI TS 119 612 v2.1.1 or with a suitable profile similarly derived from ETSI TS 102 231.

### 6. Certificate Contents and Format

#### Reg_31 - Certificate Name
- **UID**: Reg_31
- **Requirement**: The common Certificate Policy mentioned in Reg_12 SHALL require that an access certificate contains a name for the PID Provider, QEAA Provider, PuB-EAA Provider, non-qualified EAA Provider, or Relying Party, in a format suitable for presenting to a User.

#### Reg_32 - EU-wide Unique Identifier
- **UID**: Reg_32
- **Requirement**: The common Certificate Policy mentioned in Reg_12 SHALL require that an access certificate contains an EU-wide unique identifier for the PID Provider, QEAA Provider, PuB-EAA Provider, non-qualified EAA Provider, or Relying Party, and SHALL specify a method for deriving such identifiers.

#### Reg_33 - Registrar URL
- **UID**: Reg_33
- **Requirement**: The common Certificate Policy mentioned in Reg_12 SHALL require that an access certificate contains the URL of the online service of the Member State Registrar, which Wallet Units and other parties can use to obtain the information registered about the PID Provider, QEAA Provider, PuB-EAA Provider, non-qualified EAA Provider, or Relying Party.

### 7. Registration Certificate Contents

#### RPRC_03 - Registration Certificate Contents
- **UID**: RPRC_03
- **Requirement**: The contents of a registration certificate SHALL include at least the information required in Annex V of the CIR 2025/848 regarding registration of wallet-relying parties.

#### RPRC_06 - Registration Certificate Name
- **UID**: RPRC_06
- **Requirement**: The contents of a registration certificate SHALL include a name for the subject of the certificate, in a format suitable for presenting to a User.

#### RPRC_07 - Registration Certificate Identifier
- **UID**: RPRC_07
- **Requirement**: The contents of a registration certificate SHALL include an EU-wide unique identifier for the subject of the certificate, and SHALL specify a method for deriving such identifiers.

### 8. Certificate Revocation and Lifecycle Management

#### RPACANot_06 - Access Certificate Revocation
- **UID**: RPACANot_06
- **Requirement**: If an Access Certificate Authority is suspended or cancelled, that Access Certificate Authority SHALL immediately revoke all of its temporally valid access certificates.

#### RPACANot_07 - Registration Certificate Revocation
- **UID**: RPACANot_07
- **Requirement**: If a Provider of registration certificates is suspended or cancelled, that Provider SHALL immediately revoke all of its valid registration certificates (if any). Moreover, the corresponding Registrar SHALL prohibit all access to the registry entries published online.

### 9. Certificate Verification and Validation

#### RPRC_17 - Registration Certificate Verification
- **UID**: RPRC_17
- **Requirement**: If the User indicated that they want to verify the information registered about the Relying Party and the Relying Party sent a registration certificate to the Wallet Unit, the Wallet Unit SHALL verify the authenticity and validity of the registration certificate according to the technical specification meant in RPRC_02.

#### RPRC_18 - Online Service Verification
- **UID**: RPRC_18
- **Requirement**: If the User indicated that they want to verify the information registered about the Relying Party, but the Relying Party did not send a registration certificate to the Wallet Unit, the Wallet Unit SHALL connect to the URL of the online service of the Registrar to obtain this information.

### 10. Certificate Presentation and Binding

#### RPRC_19 - Registration Certificate Presentation
- **UID**: RPRC_19
- **Requirement**: If a Relying Party Instance received one or more registration certificates, it SHALL include a single registration certificate applicable for its current intended use in each presentation request to a Wallet Unit, according to the applicable standard's extension mentioned in RPRC_20. The registration certificate SHALL be included in the request by value, not by reference.

#### RPRC_20 - Presentation Protocol Extensions
- **UID**: RPRC_20
- **Requirement**: The Commission SHALL ensure that extensions are specified for ISO/IEC 18013-5 and for OpenID4VP, allowing a Relying Party to transfer a single Relying Party registration certificate to a Wallet Unit in a presentation request.

#### RPRC_22 - Issuer Metadata Registration Certificate
- **UID**: RPRC_22
- **Requirement**: If a PID Provider or Attestation Provider received a registration certificate, it SHALL include the registration certificate in its Issuer metadata used in the common OpenID4VCI protocol referenced in ISSU_01. The registration certificate SHALL be included in the metadata by value, not by reference.

## Key Differences and Alignment Requirements

### 1. Certificate Infrastructure Gaps

**Current IT-Wallet Specification Gaps:**
- No comprehensive access certificate infrastructure for relying parties
- Missing registration certificate framework for PID providers and attestation providers
- Lack of standardized certificate policies for access and registration certificates
- No certificate transparency logging requirements

**Required Alignments:**
- Implement access certificate issuance and management for all ecosystem participants
- Establish registration certificate framework with proper lifecycle management
- Define common certificate policies meeting ETSI standards
- Implement certificate transparency logging for all issued certificates

### 2. Trust Anchor Management

**Current IT-Wallet Specification Gaps:**
- Limited trust anchor distribution mechanisms
- No standardized trusted list formats
- Missing cross-border trust anchor acceptance

**Required Alignments:**
- Implement ETSI TS 119 612 v2.3.1 compliant trusted lists
- Establish cross-border trust anchor acceptance mechanisms
- Create secure notification and publication processes for trust anchors

### 3. Certificate Revocation and Lifecycle

**Current IT-Wallet Specification Gaps:**
- Incomplete certificate revocation mechanisms
- Missing certificate lifecycle management policies
- No automated certificate status checking

**Required Alignments:**
- Implement comprehensive certificate revocation policies
- Establish certificate lifecycle management with proper status tracking
- Create automated certificate status verification mechanisms

### 4. Certificate Contents and Format

**Current IT-Wallet Specification Gaps:**
- Missing standardized certificate content requirements
- No EU-wide unique identifier framework
- Limited certificate binding mechanisms

**Required Alignments:**
- Implement standardized certificate content requirements
- Establish EU-wide unique identifier framework
- Create proper certificate binding mechanisms between access and registration certificates

### 5. Certificate Verification and Validation

**Current IT-Wallet Specification Gaps:**
- Limited certificate verification capabilities
- Missing registration information validation
- No proper certificate chain validation

**Required Alignments:**
- Implement comprehensive certificate verification mechanisms
- Create registration information validation processes
- Establish proper certificate chain validation with trust anchor verification

### 6. Certificate Presentation and Binding

**Current IT-Wallet Specification Gaps:**
- No standardized certificate presentation mechanisms
- Missing certificate binding to presentation requests
- Limited metadata integration

**Required Alignments:**
- Implement standardized certificate presentation in presentation requests
- Create proper certificate binding mechanisms
- Integrate certificates into issuer metadata and presentation protocols

## Recommendations for IT-Wallet Specification Alignment

### Immediate Actions Required:

1. **Certificate Infrastructure Development**
   - Develop access certificate issuance and management system
   - Create registration certificate framework
   - Implement certificate policies meeting ETSI standards

2. **Trust Management Enhancement**
   - Implement ETSI TS 119 612 v2.3.1 compliant trusted lists
   - Establish cross-border trust mechanisms
   - Create secure notification and publication processes

3. **Revocation and Lifecycle Management**
   - Implement comprehensive revocation policies
   - Create certificate lifecycle management system
   - Establish automated status checking

4. **Certificate Content Standardization**
   - Define standardized certificate content requirements
   - Implement EU-wide unique identifier framework
   - Create proper certificate binding mechanisms

5. **Verification and Validation Enhancement**
   - Implement comprehensive verification mechanisms
   - Create registration information validation
   - Establish proper certificate chain validation

6. **Presentation Protocol Integration**
   - Implement certificate presentation in requests
   - Create proper binding mechanisms
   - Integrate with issuer metadata

### Long-term Strategic Actions:

1. **Interoperability Framework**
   - Ensure cross-border certificate acceptance
   - Implement standardized verification processes
   - Create unified certificate management interfaces

2. **Security Enhancement**
   - Implement advanced certificate security features
   - Create comprehensive audit trails
   - Establish incident response procedures

3. **Scalability and Performance**
   - Optimize certificate verification performance
   - Implement efficient revocation checking
   - Create scalable trust anchor distribution

This analysis provides a comprehensive overview of the certificate-related requirements from Annex 2 and identifies the key areas where the IT-Wallet specification needs to align to meet these requirements.

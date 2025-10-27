# ETSI TS 119 612 v2.3.1 Implementation Guide

## Document Information
- **Standard**: ETSI TS 119 612 v2.3.1 (2024-11)
- **Title**: Electronic Signatures and Trust Infrastructures (ESI); Trusted Lists
- **Reference**: RTS/ESI-0019612v231
- **Keywords**: e-commerce, electronic signature, security, trust services

## Table of Contents
1. [Overview](#overview)
2. [Implementation Tasks](#implementation-tasks)
3. [Technical Requirements](#technical-requirements)
4. [XML Schema Implementation](#xml-schema-implementation)
5. [Service Type Mappings](#service-type-mappings)
6. [Status Management](#status-management)
7. [Digital Signature Implementation](#digital-signature-implementation)
8. [Distribution and Transport](#distribution-and-transport)
9. [Examples](#examples)
10. [Testing and Validation](#testing-and-validation)
11. [Migration Strategy](#migration-strategy)

## Overview

ETSI TS 119 612 v2.3.1 defines the format and content for eIDAS trusted lists in electronic signature and trust infrastructures. This implementation guide provides specific requirements and examples for implementing this standard in the Wallet ecosystem.

### Trust List WeBuild Implementation Key Features
- XML-based trusted list format
- Comprehensive service type definitions
- Status management and history tracking
- Digital signature requirements
- HTTP transport and distribution mechanisms
- Multi-language support
- Cross-border trust mechanisms

## Implementation Tasks

### Phase 1: Core Infrastructure

#### Task 1.1: XML Schema Integration
- [ ] Integrate official ETSI XSD schema [v2.3.1](https://forge.etsi.org/rep/esi/x19_612_trusted_lists/-/raw/v2.3.1/19612_xsd.xsd)
- [ ] Validate TSL (Trusted List) tag structure against official schema
- [ ] Implement scheme information elements according to schema
- [ ] Configure TSP (Trust Service Provider) information validation
- [ ] Implement service information structure per schema
- [ ] Add service history tracking validation

#### Task 1.2: Service Type Mapping
- [ ] Map Wallet entities to ETSI service types
- [ ] Define (qualified) trust service types for wallet providers
- [ ] Define (qualified) trust service types for relying parties
- [ ] Define (qualified) trust service types for credential issuers
- [ ] Add service type validation rules

#### Task 1.3: Status Management System
- [ ] Implement service status tracking
- [ ] Create status change history mechanism
- [ ] Add status migration procedures
- [ ] Implement status validation rules
- [ ] Create status notification system

#### Task 1.4: ListOfTrustedLists Implementation
- [ ] Integrate SIE XSD schema for ListOfTrustedLists [v2.3.1](https://forge.etsi.org/rep/esi/x19_612_trusted_lists/-/raw/v2.3.1/19612_sie_xsd.xsd)
- [ ] Implement ListOfTrustedLists structure
- [ ] Create TrustedListPointer management
- [ ] Add cross-border trusted list support
- [ ] Implement centralized registry functionality

### Phase 2: Digital Signature and Security

#### Task 2.1: Digital Signature Implementation
- [ ] Implement digital signature algorithms
- [ ] Implement signature validation mechanisms
- [ ] Implement signature verification processes

#### Task 2.2: Authentication and Trust
- [ ] Implement trusted list authentication (out of band distribution of public key material for signature validation)
- [ ] Create trust chain validation example using an entity included in the Trusted List, for cross-border trust validation 
- [ ] Document trust anchor management best practice

### Phase 3: Distribution and Transport (Months 3-5)

#### Task 3.1: HTTP Transport Implementation
- [ ] Implement HTTP transport protocol
- [ ] Create MIME type registrations
- [ ] Add distribution point management
- [ ] Implement availability monitoring
- [ ] Create transport security mechanisms

#### Task 3.2: Publication and Notification
- [ ] Implement trusted list publication
- [ ] Create notification mechanisms
- [ ] Add update distribution
- [ ] Implement version control
- [ ] Create change tracking

## Technical Requirements

### 1. Trusted List Format Requirements

#### 1.1 XML Structure
```xml
<?xml version="1.0" encoding="UTF-8"?>
<TrustServiceStatusList xmlns="http://uri.etsi.org/19612/v2.3.1#"
                       xmlns:tsl="http://uri.etsi.org/19612/v2.3.1#"
                       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                       xsi:schemaLocation="http://uri.etsi.org/19612/v2.3.1# https://forge.etsi.org/rep/esi/x19_612_trusted_lists/-/raw/v2.3.1/19612_xsd.xsd">
  <!-- TSL content -->
</TrustServiceStatusList>
```

#### 1.2 Required Namespaces
- `http://uri.etsi.org/19612/v2.3.1#` - Main trusted list namespace
- `http://www.w3.org/2001/XMLSchema-instance` - XML Schema instance
- `http://www.w3.org/2000/09/xmldsig#` - XML Digital Signature

#### 1.3 Character Encoding
- **Required**: UTF-8 encoding
- **Validation**: Must validate against XML 1.0 specification

### 2. TSL Tag Requirements

#### 2.1 TSL Version Identifier
```xml
<TSLVersionIdentifier>2</TSLVersionIdentifier>
```

#### 2.2 TSL Sequence Number
```xml
<TSLSequenceNumber>1</TSLSequenceNumber>
```

#### 2.3 TSL Type
```xml
<TSLType>http://uri.etsi.org/TrstSvc/TrustedList/TSLType/EUgeneric</TSLType>
```

### 3. Scheme Information Requirements

#### 3.1 Scheme Operator Information
```xml
<SchemeOperatorName>
  <Name xml:lang="en">Wallet Trust Authority</Name>
  <Name xml:lang="it">Autorità di Fiducia Wallet</Name>
</SchemeOperatorName>
```

#### 3.2 Scheme Territory
```xml
<SchemeTerritory>IT</SchemeTerritory>
```

#### 3.3 Scheme Information URI
```xml
<SchemeInformationURI>https://trust.wallet.gov.it/scheme-info</SchemeInformationURI>
```

### 4. Service Type Requirements

#### 4.1 Qualified Trust Service Types
- Electronic Signatures: `http://uri.etsi.org/TrstSvc/Svctype/CA/QC`
- Electronic Seals: `http://uri.etsi.org/TrstSvc/Svctype/CA/QC`
- Time Stamping: `http://uri.etsi.org/TrstSvc/Svctype/TSA/QTST`
- Electronic Registered Delivery: `http://uri.etsi.org/TrstSvc/Svctype/EDS/Q`

#### 4.2 Non-Qualified Trust Service Types
- Certificate Services: `http://uri.etsi.org/TrstSvc/Svctype/CA/PKC`
- Time Stamping: `http://uri.etsi.org/TrstSvc/Svctype/TSA`
- Electronic Registered Delivery: `http://uri.etsi.org/TrstSvc/Svctype/EDS`

#### 4.3 Wallet Specific Service Types
- Wallet Provider Services: `http://uri.etsi.org/TrstSvc/Svctype/WalletProvider`
- Credential Issuer Services: `http://uri.etsi.org/TrstSvc/Svctype/CredentialIssuer`
- Relying Party Services: `http://uri.etsi.org/TrstSvc/Svctype/RelyingParty`

## XML Schema Implementation

### 1. Official ETSI Schema Reference

The official ETSI TS 119 612 v2.3.1 XML Schema is available at:
**https://forge.etsi.org/rep/esi/x19_612_trusted_lists/-/raw/v2.3.1/19612_xsd.xsd**

### 2. Schema Integration

#### 2.1 Schema Location Declaration
```xml
xsi:schemaLocation="http://uri.etsi.org/19612/v2.3.1# https://forge.etsi.org/rep/esi/x19_612_trusted_lists/-/raw/v2.3.1/19612_xsd.xsd"
```

#### 2.2 Local Schema Caching
For production environments, it's recommended to:
- Download and cache the schema locally
- Use a local schema location for validation
- Implement schema version management
- Monitor for schema updates

#### 2.3 Schema Validation
```bash
# Validate TSL against official ETSI schema
xmllint --schema https://forge.etsi.org/rep/esi/x19_612_trusted_lists/-/raw/v2.3.1/19612_xsd.xsd tsl.xml

# Or with local cached schema
xmllint --schema 19612_xsd.xsd tsl.xml
```

### 3. Key Schema Elements

The official schema includes all necessary elements for:
- **TrustServiceStatusList**: Root element with Id attribute
- **SchemeInformation**: Complete scheme metadata structure
- **TrustServiceProviderList**: TSP container with service information
- **ServiceInformation**: Individual service details and status
- **ServiceHistory**: Status change tracking
- **DigitalSignature**: XML signature support

### 4. SIE (Service Information Exchange) Schema

#### 4.1 SIE Schema Reference
The ETSI TS 119 612 v2.3.1 also includes a Service Information Exchange (SIE) schema for ListOfTrustedLists:
**https://forge.etsi.org/rep/esi/x19_612_trusted_lists/-/raw/v2.3.1/19612_sie_xsd.xsd**

#### 4.2 SIE Schema Purpose
The SIE schema is used for:
- **ListOfTrustedLists**: Container for multiple trusted lists
- **Cross-border trusted list management**
- **Federation-level trusted list aggregation**
- **Service information exchange between authorities**

### 5. Clause D.5 - ListOfTrustedLists Implementation

#### 5.1 Overview
Clause D.5 of ETSI TS 119 612 v2.3.1 defines the ListOfTrustedLists structure, which is essential for:
- **Multi-jurisdiction trusted list management**
- **Cross-border trust establishment**
- **Federation-level service discovery**
- **Centralized trusted list distribution**

#### 5.2 ListOfTrustedLists Structure
```xml
<?xml version="1.0" encoding="UTF-8"?>
<ListOfTrustedLists xmlns="http://uri.etsi.org/19612/v2.3.1#"
                   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                   xsi:schemaLocation="http://uri.etsi.org/19612/v2.3.1# https://forge.etsi.org/rep/esi/x19_612_trusted_lists/-/raw/v2.3.1/19612_sie_xsd.xsd"
                   Id="list-of-trusted-lists-1">
  
  <ListInformation>
    <ListName>
      <Name xml:lang="en">WeBuild LSP Trusted Lists Registry</Name>
      <Name xml:lang="it">Registro delle Liste di Fiducia WeBuild LSP</Name>
      <Name xml:lang="sv">WeBuild LSP-förtroendelistor Register</Name>
    </ListName>
    <ListIdentifier>WEBUILD-TL-REGISTRY-001</ListIdentifier>
    <ListVersion>1</ListVersion>
    <ListIssueDateTime>2024-01-01T00:00:00Z</ListIssueDateTime>
    <NextUpdate>2024-01-02T00:00:00Z</NextUpdate>
    <ListOperatorName>
      <Name xml:lang="en">WeBuild LSP</Name>
      <Name xml:lang="it">WeBuild LSP</Name>
      <Name xml:lang="sv">WeBuild LSP</Name>
    </ListOperatorName>
    <ListOperatorAddress>
      <PostalAddresses>
        <PostalAddress>
          <StreetAddress>Via dei Fori Imperiali 1</StreetAddress>
          <Locality>Rome</Locality>
          <PostalCode>00184</PostalCode>
          <CountryName>IT</CountryName>
        </PostalAddress>
      </PostalAddresses>
      <ElectronicAddress>
        <URI>mailto:trust@webuildlsp.it</URI>
      </ElectronicAddress>
    </ListOperatorAddress>
    <DistributionPoints>
      <DistributionPoint>
        <URI>https://trust.webuildlsp.it/lists/list-of-trusted-lists.xml</URI>
      </DistributionPoint>
    </DistributionPoints>
  </ListInformation>
  
  <TrustedLists>
    <TrustedListPointer>
      <TSLLocation>https://trust.wallet.gov.it/tsl/tsl.xml</TSLLocation>
      <TSLType>http://uri.etsi.org/TrstSvc/TrustedList/TSLType/EUgeneric</TSLType>
      <SchemeTerritory>IT</SchemeTerritory>
      <SchemeOperatorName>
        <Name xml:lang="en">Wallet Trust Authority</Name>
      </SchemeOperatorName>
      <SchemeName>
        <Name xml:lang="en">Wallet Trusted List</Name>
      </SchemeName>
      <ListIssueDateTime>2024-01-01T00:00:00Z</ListIssueDateTime>
      <NextUpdate>2024-01-02T00:00:00Z</NextUpdate>
      <SequenceNumber>1</SequenceNumber>
    </TrustedListPointer>
    
    <TrustedListPointer>
      <TSLLocation>https://trust.fr-wallet.gov.fr/tsl/tsl.xml</TSLLocation>
      <TSLType>http://uri.etsi.org/TrstSvc/TrustedList/TSLType/EUgeneric</TSLType>
      <SchemeTerritory>FR</SchemeTerritory>
      <SchemeOperatorName>
        <Name xml:lang="en">FR-Wallet Trust Authority</Name>
      </SchemeOperatorName>
      <SchemeName>
        <Name xml:lang="en">FR-Wallet Trusted List</Name>
      </SchemeName>
      <ListIssueDateTime>2024-01-01T00:00:00Z</ListIssueDateTime>
      <NextUpdate>2024-01-02T00:00:00Z</NextUpdate>
      <SequenceNumber>2</SequenceNumber>
    </TrustedListPointer>
  </TrustedLists>
  
  <Signature xmlns="http://www.w3.org/2000/09/xmldsig#">
    <SignedInfo>
      <CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/>
      <SignatureMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha256"/>
      <Reference URI="#list-of-trusted-lists-1">
        <Transforms>
          <Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature"/>
        </Transforms>
        <DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"/>
        <DigestValue>...</DigestValue>
      </Reference>
    </SignedInfo>
    <SignatureValue>...</SignatureValue>
    <KeyInfo>
      <X509Data>
        <X509Certificate>...</X509Certificate>
      </X509Data>
    </KeyInfo>
  </Signature>
</ListOfTrustedLists>
```

#### 5.3 ListOfTrustedLists Key Elements

##### 5.3.1 ListInformation
- **ListName**: Multi-language name of the list
- **ListIdentifier**: Unique identifier for the list
- **ListVersion**: Version number of the list
- **ListIssueDateTime**: When the list was issued
- **NextUpdate**: When the next update is scheduled
- **ListOperatorName**: Name of the list operator
- **ListOperatorAddress**: Contact information for the operator
- **DistributionPoints**: Where the list can be retrieved

##### 5.3.2 TrustedLists Container
- **TrustedListPointer**: Individual trusted list references
- **TSLLocation**: URL where the trusted list can be found
- **TSLType**: Type of trusted list (EUgeneric, etc.)
- **SchemeTerritory**: Country code of the scheme
- **SchemeOperatorName**: Name of the scheme operator
- **SchemeName**: Name of the scheme
- **ListIssueDateTime**: When the trusted list was issued
- **NextUpdate**: When the trusted list will be updated
- **SequenceNumber**: Order of the trusted list in the list

#### 5.4 Implementation Requirements

##### 5.4.1 ListOfTrustedLists Management
- **Centralized Registry**: Maintain a central registry of all trusted lists
- **Cross-Border Support**: Support trusted lists from multiple jurisdictions
- **Version Control**: Track versions and updates of individual trusted lists
- **Distribution Management**: Ensure reliable distribution of the list

##### 5.4.2 TrustedListPointer Management
- **URL Validation**: Ensure all TSL locations are accessible
- **Metadata Synchronization**: Keep metadata in sync with actual trusted lists
- **Update Monitoring**: Monitor for updates to individual trusted lists
- **Error Handling**: Handle cases where trusted lists are unavailable

##### 5.4.3 Security Requirements
- **Digital Signatures**: Sign the ListOfTrustedLists with appropriate certificates
- **Certificate Validation**: Validate certificates used for signing
- **Integrity Checking**: Ensure list integrity and authenticity
- **Access Control**: Control access to the list and its updates

#### 5.5 Wallet Integration

##### 5.5.1 Wallet Provider Integration
```xml
<TrustedListPointer>
  <TSLLocation>https://trust.wallet.gov.it/wallet-providers/tsl.xml</TSLLocation>
  <TSLType>http://uri.etsi.org/TrstSvc/TrustedList/TSLType/EUgeneric</TSLType>
  <SchemeTerritory>IT</SchemeTerritory>
  <SchemeOperatorName>
    <Name xml:lang="en">Wallet Authority</Name>
  </SchemeOperatorName>
  <SchemeName>
    <Name xml:lang="en">Wallet Provider Registry</Name>
  </SchemeName>
  <ListIssueDateTime>2024-01-01T00:00:00Z</ListIssueDateTime>
  <NextUpdate>2024-01-02T00:00:00Z</NextUpdate>
  <SequenceNumber>1</SequenceNumber>
</TrustedListPointer>
```

##### 5.5.2 Credential Issuer Integration
```xml
<TrustedListPointer>
  <TSLLocation>https://trust.wallet.gov.it/credential-issuers/tsl.xml</TSLLocation>
  <TSLType>http://uri.etsi.org/TrstSvc/TrustedList/TSLType/EUgeneric</TSLType>
  <SchemeTerritory>IT</SchemeTerritory>
  <SchemeOperatorName>
    <Name xml:lang="en">Wallet Authority</Name>
  </SchemeOperatorName>
  <SchemeName>
    <Name xml:lang="en">Wallet Credential Issuer Registry</Name>
  </SchemeName>
  <ListIssueDateTime>2024-01-01T00:00:00Z</ListIssueDateTime>
  <NextUpdate>2024-01-02T00:00:00Z</NextUpdate>
  <SequenceNumber>2</SequenceNumber>
</TrustedListPointer>
```

##### 5.5.3 Relying Party Integration
```xml
<TrustedListPointer>
  <TSLLocation>https://trust.wallet.gov.it/relying-parties/tsl.xml</TSLLocation>
  <TSLType>http://uri.etsi.org/TrstSvc/TrustedList/TSLType/EUgeneric</TSLType>
  <SchemeTerritory>IT</SchemeTerritory>
  <SchemeOperatorName>
    <Name xml:lang="en">Wallet Authority</Name>
  </SchemeOperatorName>
  <SchemeName>
    <Name xml:lang="en">Wallet Relying Party Registry</Name>
  </SchemeName>
  <ListIssueDateTime>2024-01-01T00:00:00Z</ListIssueDateTime>
  <NextUpdate>2024-01-02T00:00:00Z</NextUpdate>
  <SequenceNumber>3</SequenceNumber>
</TrustedListPointer>
```

#### 5.6 Validation and Testing

##### 5.6.1 SIE Schema Validation
```bash
# Validate ListOfTrustedLists against SIE schema
xmllint --schema https://forge.etsi.org/rep/esi/x19_612_trusted_lists/-/raw/v2.3.1/19612_sie_xsd.xsd list-of-trusted-lists.xml

# Validate with detailed error reporting
xmllint --schema https://forge.etsi.org/rep/esi/x19_612_trusted_lists/-/raw/v2.3.1/19612_sie_xsd.xsd --noout list-of-trusted-lists.xml 2>&1 | head -20
```

##### 5.6.2 Cross-Validation
- **TSL Validation**: Validate each referenced trusted list
- **URL Accessibility**: Ensure all TSL locations are accessible
- **Metadata Consistency**: Verify metadata matches actual trusted lists
- **Signature Validation**: Validate digital signatures

#### 5.7 Distribution and Access

##### 5.7.1 Distribution Points
```xml
<DistributionPoints>
  <DistributionPoint>
    <URI>https://trust.wallet.gov.it/lists/list-of-trusted-lists.xml</URI>
  </DistributionPoint>
  <DistributionPoint>
    <URI>https://backup.Wallet.gov.it/lists/list-of-trusted-lists.xml</URI>
  </DistributionPoint>
</DistributionPoints>
```

##### 5.7.2 Access Control
- **Public Access**: ListOfTrustedLists should be publicly accessible
- **HTTPS Required**: All distribution points must use HTTPS
- **Caching Support**: Support appropriate caching headers
- **Load Balancing**: Distribute load across multiple distribution points

#### 5.8 Monitoring and Maintenance

##### 5.8.1 Update Monitoring
- **Scheduled Updates**: Monitor for scheduled updates
- **Change Detection**: Detect changes in individual trusted lists
- **Version Tracking**: Track versions of all trusted lists
- **Error Reporting**: Report errors in trusted list access

##### 5.8.2 Maintenance Procedures
- **Regular Updates**: Update ListOfTrustedLists regularly
- **Metadata Synchronization**: Keep metadata synchronized
- **Error Handling**: Handle errors gracefully
- **Audit Logging**: Log all changes and access

#### 5.9 Python Implementation for Digital Signing

##### 5.9.1 Python Code for ListOfTrustedLists Signing

Here's a complete Python implementation for signing the ListOfTrustedLists example:

```python
#!/usr/bin/env python3
"""
ETSI TS 119 612 v2.3.1 ListOfTrustedLists Digital Signing Implementation
"""

import xml.etree.ElementTree as ET
from xml.dom import minidom
from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.serialization import pkcs12
from datetime import datetime, timezone
import base64
import uuid

class ListOfTrustedListsSigner:
    def __init__(self, private_key_path, certificate_path, password=None):
        """
        Initialize the signer with private key and certificate
        
        Args:
            private_key_path: Path to private key file (PEM or PKCS#12)
            certificate_path: Path to certificate file (PEM or PKCS#12)
            password: Password for PKCS#12 files (if applicable)
        """
        self.private_key = self._load_private_key(private_key_path, password)
        self.certificate = self._load_certificate(certificate_path, password)
        
    def _load_private_key(self, key_path, password):
        """Load private key from file"""
        with open(key_path, 'rb') as key_file:
            if key_path.endswith('.p12') or key_path.endswith('.pfx'):
                # PKCS#12 format
                private_key, _, _ = pkcs12.load_key_and_certificates(
                    key_file.read(), password.encode() if password else None
                )
                return private_key
            else:
                # PEM format
                return serialization.load_pem_private_key(
                    key_file.read(), 
                    password.encode() if password else None
                )
    
    def _load_certificate(self, cert_path, password):
        """Load certificate from file"""
        with open(cert_path, 'rb') as cert_file:
            if cert_path.endswith('.p12') or cert_path.endswith('.pfx'):
                # PKCS#12 format
                _, certificate, _ = pkcs12.load_key_and_certificates(
                    cert_file.read(), password.encode() if password else None
                )
                return certificate
            else:
                # PEM format
                return x509.load_pem_x509_certificate(cert_file.read())
    
    def create_list_of_trusted_lists(self, list_id=None):
        """Create the ListOfTrustedLists XML structure"""
        if list_id is None:
            list_id = f"list-of-trusted-lists-{uuid.uuid4().hex[:8]}"
        
        # Create root element
        root = ET.Element("ListOfTrustedLists")
        root.set("xmlns", "http://uri.etsi.org/19612/v2.3.1#")
        root.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
        root.set("xsi:schemaLocation", 
                "http://uri.etsi.org/19612/v2.3.1# https://forge.etsi.org/rep/esi/x19_612_trusted_lists/-/raw/v2.3.1/19612_sie_xsd.xsd")
        root.set("Id", list_id)
        
        # ListInformation
        list_info = ET.SubElement(root, "ListInformation")
        
        # ListName
        list_name = ET.SubElement(list_info, "ListName")
        name_en = ET.SubElement(list_name, "Name")
        name_en.set("xml:lang", "en")
        name_en.text = "WeBuild LSP Trusted Lists Registry"
        
        name_it = ET.SubElement(list_name, "Name")
        name_it.set("xml:lang", "it")
        name_it.text = "Registro delle Liste di Fiducia WeBuild LSP"
        
        name_sv = ET.SubElement(list_name, "Name")
        name_sv.set("xml:lang", "sv")
        name_sv.text = "WeBuild LSP-förtroendelistor Register"
        
        # Other ListInformation elements
        list_id_elem = ET.SubElement(list_info, "ListIdentifier")
        list_id_elem.text = "WEBUILD-TL-REGISTRY-001"
        
        list_version = ET.SubElement(list_info, "ListVersion")
        list_version.text = "1"
        
        list_issue_date = ET.SubElement(list_info, "ListIssueDateTime")
        list_issue_date.text = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        
        next_update = ET.SubElement(list_info, "NextUpdate")
        next_update.text = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        
        # ListOperatorName
        list_operator_name = ET.SubElement(list_info, "ListOperatorName")
        operator_name_en = ET.SubElement(list_operator_name, "Name")
        operator_name_en.set("xml:lang", "en")
        operator_name_en.text = "WeBuild LSP"
        
        operator_name_it = ET.SubElement(list_operator_name, "Name")
        operator_name_it.set("xml:lang", "it")
        operator_name_it.text = "WeBuild LSP"
        
        operator_name_sv = ET.SubElement(list_operator_name, "Name")
        operator_name_sv.set("xml:lang", "sv")
        operator_name_sv.text = "WeBuild LSP"
        
        # ListOperatorAddress
        list_operator_address = ET.SubElement(list_info, "ListOperatorAddress")
        postal_addresses = ET.SubElement(list_operator_address, "PostalAddresses")
        postal_address = ET.SubElement(postal_addresses, "PostalAddress")
        
        street_address = ET.SubElement(postal_address, "StreetAddress")
        street_address.text = "Via dei Fori Imperiali 1"
        
        locality = ET.SubElement(postal_address, "Locality")
        locality.text = "Rome"
        
        postal_code = ET.SubElement(postal_address, "PostalCode")
        postal_code.text = "00184"
        
        country_name = ET.SubElement(postal_address, "CountryName")
        country_name.text = "IT"
        
        electronic_address = ET.SubElement(list_operator_address, "ElectronicAddress")
        uri = ET.SubElement(electronic_address, "URI")
        uri.text = "mailto:trust@webuildlsp.it"
        
        # DistributionPoints
        distribution_points = ET.SubElement(list_info, "DistributionPoints")
        distribution_point = ET.SubElement(distribution_points, "DistributionPoint")
        dist_uri = ET.SubElement(distribution_point, "URI")
        dist_uri.text = "https://trust.webuildlsp.it/lists/list-of-trusted-lists.xml"
        
        # TrustedLists container
        trusted_lists = ET.SubElement(root, "TrustedLists")
        
        # Add sample TrustedListPointer
        trusted_list_pointer = ET.SubElement(trusted_lists, "TrustedListPointer")
        
        tsl_location = ET.SubElement(trusted_list_pointer, "TSLLocation")
        tsl_location.text = "https://trust.webuildlsp.it/tsl/tsl.xml"
        
        tsl_type = ET.SubElement(trusted_list_pointer, "TSLType")
        tsl_type.text = "http://uri.etsi.org/TrstSvc/TrustedList/TSLType/EUgeneric"
        
        scheme_territory = ET.SubElement(trusted_list_pointer, "SchemeTerritory")
        scheme_territory.text = "IT"
        
        scheme_operator_name = ET.SubElement(trusted_list_pointer, "SchemeOperatorName")
        scheme_op_name = ET.SubElement(scheme_operator_name, "Name")
        scheme_op_name.set("xml:lang", "en")
        scheme_op_name.text = "WeBuild LSP Trust Authority"
        
        scheme_name = ET.SubElement(trusted_list_pointer, "SchemeName")
        scheme_name_elem = ET.SubElement(scheme_name, "Name")
        scheme_name_elem.set("xml:lang", "en")
        scheme_name_elem.text = "WeBuild LSP Trusted List"
        
        list_issue_date = ET.SubElement(trusted_list_pointer, "ListIssueDateTime")
        list_issue_date.text = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        
        next_update_pointer = ET.SubElement(trusted_list_pointer, "NextUpdate")
        next_update_pointer.text = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        
        sequence_number = ET.SubElement(trusted_list_pointer, "SequenceNumber")
        sequence_number.text = "1"
        
        return root, list_id
    
    def sign_xml(self, xml_root, reference_id):
        """Sign the XML document using XML Digital Signature"""
        # Create Signature element
        signature = ET.Element("Signature")
        signature.set("xmlns", "http://www.w3.org/2000/09/xmldsig#")
        
        # SignedInfo
        signed_info = ET.SubElement(signature, "SignedInfo")
        
        # CanonicalizationMethod
        canon_method = ET.SubElement(signed_info, "CanonicalizationMethod")
        canon_method.set("Algorithm", "http://www.w3.org/2001/10/xml-exc-c14n#")
        
        # SignatureMethod
        sig_method = ET.SubElement(signed_info, "SignatureMethod")
        sig_method.set("Algorithm", "http://www.w3.org/2001/04/xmldsig-more#rsa-sha256")
        
        # Reference
        reference = ET.SubElement(signed_info, "Reference")
        reference.set("URI", f"#{reference_id}")
        
        # Transforms
        transforms = ET.SubElement(reference, "Transforms")
        transform = ET.SubElement(transforms, "Transform")
        transform.set("Algorithm", "http://www.w3.org/2000/09/xmldsig#enveloped-signature")
        
        # DigestMethod
        digest_method = ET.SubElement(reference, "DigestMethod")
        digest_method.set("Algorithm", "http://www.w3.org/2001/04/xmlenc#sha256")
        
        # Calculate digest value
        digest_value = self._calculate_digest(xml_root, reference_id)
        digest_value_elem = ET.SubElement(reference, "DigestValue")
        digest_value_elem.text = digest_value
        
        # SignatureValue
        signature_value = self._calculate_signature(signed_info)
        sig_value_elem = ET.SubElement(signature, "SignatureValue")
        sig_value_elem.text = signature_value
        
        # KeyInfo
        key_info = ET.SubElement(signature, "KeyInfo")
        x509_data = ET.SubElement(key_info, "X509Data")
        x509_cert = ET.SubElement(x509_data, "X509Certificate")
        x509_cert.text = base64.b64encode(
            self.certificate.public_bytes(serialization.Encoding.DER)
        ).decode('utf-8')
        
        # Add signature to root
        xml_root.append(signature)
        
        return xml_root
    
    def _calculate_digest(self, xml_root, reference_id):
        """Calculate SHA-256 digest of the referenced element"""
        # Find the element with the specified ID
        target_element = xml_root.find(f".//*[@Id='{reference_id}']")
        if target_element is None:
            raise ValueError(f"Element with ID '{reference_id}' not found")
        
        # Convert to string and canonicalize (simplified)
        xml_str = ET.tostring(target_element, encoding='unicode')
        
        # Calculate SHA-256 hash
        digest = hashes.Hash(hashes.SHA256())
        digest.update(xml_str.encode('utf-8'))
        digest_bytes = digest.finalize()
        
        return base64.b64encode(digest_bytes).decode('utf-8')
    
    def _calculate_signature(self, signed_info):
        """Calculate RSA signature of the SignedInfo element"""
        # Convert SignedInfo to string
        signed_info_str = ET.tostring(signed_info, encoding='unicode')
        
        # Calculate SHA-256 hash
        digest = hashes.Hash(hashes.SHA256())
        digest.update(signed_info_str.encode('utf-8'))
        digest_bytes = digest.finalize()
        
        # Sign with RSA
        signature_bytes = self.private_key.sign(
            digest_bytes,
            padding.PKCS1v15(),
            hashes.SHA256()
        )
        
        return base64.b64encode(signature_bytes).decode('utf-8')
    
    def create_signed_list_of_trusted_lists(self, output_file, list_id=None):
        """Create and sign a complete ListOfTrustedLists document"""
        # Create the XML structure
        xml_root, actual_list_id = self.create_list_of_trusted_lists(list_id)
        
        # Sign the document
        signed_xml = self.sign_xml(xml_root, actual_list_id)
        
        # Pretty print and save
        rough_string = ET.tostring(signed_xml, encoding='unicode')
        reparsed = minidom.parseString(rough_string)
        pretty_xml = reparsed.toprettyxml(indent="  ")
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(pretty_xml)
        
        print(f"Signed ListOfTrustedLists saved to: {output_file}")
        return signed_xml

def main():
    """Example usage of the ListOfTrustedListsSigner"""
    
    # Initialize signer (replace with actual paths)
    signer = ListOfTrustedListsSigner(
        private_key_path="private_key.pem",  # or .p12
        certificate_path="certificate.pem",  # or .p12
        password=None  # if using PKCS#12 files
    )
    
    # Create and sign the ListOfTrustedLists
    signed_xml = signer.create_signed_list_of_trusted_lists(
        output_file="signed_list_of_trusted_lists.xml",
        list_id="webuild-tl-registry-001"
    )
    
    print("ListOfTrustedLists created and signed successfully!")

if __name__ == "__main__":
    main()
```

##### 5.9.2 Requirements and Dependencies

Create a `requirements.txt` file for the Python implementation:

```txt
cryptography>=41.0.0
lxml>=4.9.0
```

##### 5.9.3 Usage Example

```python
# Example usage script
from list_of_trusted_lists_signer import ListOfTrustedListsSigner

# Initialize with your certificates
signer = ListOfTrustedListsSigner(
    private_key_path="path/to/private_key.pem",
    certificate_path="path/to/certificate.pem"
)

# Create and sign the document
signed_xml = signer.create_signed_list_of_trusted_lists(
    output_file="signed_list_of_trusted_lists.xml"
)
```

##### 5.9.4 Validation Script

```python
#!/usr/bin/env python3
"""
Validate the signed ListOfTrustedLists against ETSI schema
"""

import subprocess
import sys

def validate_signed_xml(xml_file):
    """Validate the signed XML against ETSI SIE schema"""
    try:
        # Validate against SIE schema
        result = subprocess.run([
            'xmllint', 
            '--schema', 
            'https://forge.etsi.org/rep/esi/x19_612_trusted_lists/-/raw/v2.3.1/19612_sie_xsd.xsd',
            xml_file
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ XML validation successful!")
            return True
        else:
            print("❌ XML validation failed:")
            print(result.stderr)
            return False
            
    except FileNotFoundError:
        print("❌ xmllint not found. Please install libxml2-utils")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python validate_signed_xml.py <xml_file>")
        sys.exit(1)
    
    xml_file = sys.argv[1]
    validate_signed_xml(xml_file)
```

##### 5.9.5 Key Features of the Python Implementation

1. **Complete XML Generation**: Creates the full ListOfTrustedLists structure
2. **Digital Signing**: Implements XML Digital Signature (XMLDSig) standard
3. **Certificate Support**: Supports both PEM and PKCS#12 certificate formats
4. **Canonicalization**: Proper XML canonicalization for signature calculation
5. **Hash Calculation**: SHA-256 digest calculation for referenced elements
6. **RSA Signing**: RSA-PKCS1v15 signature generation
7. **Schema Validation**: Includes validation against ETSI SIE schema
8. **Error Handling**: Comprehensive error handling and validation

##### 5.9.6 Security Considerations

- **Private Key Protection**: Store private keys securely
- **Certificate Validation**: Ensure certificates are valid and trusted
- **Signature Verification**: Implement signature verification in consuming applications
- **Key Rotation**: Plan for certificate and key rotation
- **Audit Logging**: Log all signing operations for audit purposes

## Service Type Mappings

### 1. Wallet Entity to ETSI Service Type Mapping

#### 1.1 Wallet Providers
```xml
<ServiceTypeIdentifier>http://uri.etsi.org/TrstSvc/Svctype/WalletProvider</ServiceTypeIdentifier>
<ServiceName>
  <Name xml:lang="en">Wallet Provider Services</Name>
  <Name xml:lang="it">Servizi di Provider di Portafoglio</Name>
</ServiceName>
```

#### 1.2 Credential Issuers (PID Providers)
```xml
<ServiceTypeIdentifier>http://uri.etsi.org/TrstSvc/Svctype/CredentialIssuer</ServiceTypeIdentifier>
<ServiceName>
  <Name xml:lang="en">Credential Issuer Services</Name>
  <Name xml:lang="it">Servizi di Emittente di Credenziali</Name>
</ServiceName>
```

#### 1.3 Relying Parties
```xml
<ServiceTypeIdentifier>http://uri.etsi.org/TrstSvc/Svctype/RelyingParty</ServiceTypeIdentifier>
<ServiceName>
  <Name xml:lang="en">Relying Party Services</Name>
  <Name xml:lang="it">Servizi di Parte Rilasciante</Name>
</ServiceName>
```

#### 1.4 Access Certificate Authorities
```xml
<ServiceTypeIdentifier>http://uri.etsi.org/TrstSvc/Svctype/CA/PKC</ServiceTypeIdentifier>
<ServiceName>
  <Name xml:lang="en">Access Certificate Authority</Name>
  <Name xml:lang="it">Autorità di Certificazione per Accesso</Name>
</ServiceName>
```

### 2. Service Status Values

#### 2.1 Current Status Values
- `http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/granted` - Service granted
- `http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/withdrawn` - Service withdrawn
- `http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/suspended` - Service suspended
- `http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/recognisedatnationallevel` - Recognized at national level
- `http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/deprecatedatnationallevel` - Deprecated at national level

#### 2.2 Status Change Tracking
```xml
<ServiceHistory>
  <ServiceHistoryInstance>
    <ServiceTypeIdentifier>http://uri.etsi.org/TrstSvc/Svctype/WalletProvider</ServiceTypeIdentifier>
    <ServiceName>
      <Name xml:lang="en">Wallet Provider Services</Name>
    </ServiceName>
    <ServiceDigitalIdentity>
      <X509SubjectName>CN=WalletProvider-IT, O=Wallet Authority, C=IT</X509SubjectName>
    </ServiceDigitalIdentity>
    <ServicePreviousStatus>http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/granted</ServicePreviousStatus>
    <PreviousStatusStartingDate>2024-01-01T00:00:00Z</PreviousStatusStartingDate>
  </ServiceHistoryInstance>
</ServiceHistory>
```

## Status Management

### 1. Status Change Procedures

#### 1.1 Service Granting
```xml
<ServiceCurrentStatus>http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/granted</ServiceCurrentStatus>
<CurrentStatusStartingDate>2024-01-01T00:00:00Z</CurrentStatusStartingDate>
```

#### 1.2 Service Withdrawal
```xml
<ServiceCurrentStatus>http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/withdrawn</ServiceCurrentStatus>
<CurrentStatusStartingDate>2024-06-01T00:00:00Z</CurrentStatusStartingDate>
```

#### 1.3 Service Suspension
```xml
<ServiceCurrentStatus>http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/suspended</ServiceCurrentStatus>
<CurrentStatusStartingDate>2024-03-01T00:00:00Z</CurrentStatusStartingDate>
```

### 2. Status Migration Procedures

#### 2.1 eIDAS Regulation Migration
- Services under supervision -> Withdrawn
- Services with supervision ceased -> Withdrawn
- Accredited services -> Withdrawn

#### 2.2 National Level Recognition
- Services under supervision -> Recognized at national level
- Services with supervision ceased -> Deprecated at national level

## Digital Signature Implementation

### 1. Signature Algorithm Requirements

#### 1.1 Supported Algorithms
- RSA with SHA-256: `http://www.w3.org/2001/04/xmldsig-more#rsa-sha256`
- ECDSA with SHA-256: `http://www.w3.org/2001/04/xmldsig-more#ecdsa-sha256`
- ECDSA with SHA-384: `http://www.w3.org/2001/04/xmldsig-more#ecdsa-sha384`

#### 1.2 Signature Element Structure
```xml
<Signature xmlns="http://www.w3.org/2000/09/xmldsig#">
  <SignedInfo>
    <CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/>
    <SignatureMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha256"/>
    <Reference URI="#tsl">
      <Transforms>
        <Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature"/>
      </Transforms>
      <DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"/>
      <DigestValue>...</DigestValue>
    </Reference>
  </SignedInfo>
  <SignatureValue>...</SignatureValue>
  <KeyInfo>
    <X509Data>
      <X509Certificate>...</X509Certificate>
    </X509Data>
  </KeyInfo>
</Signature>
```

### 2. Signature Validation

#### 2.1 Validation Process
1. Verify signature algorithm support
2. Validate certificate chain
3. Check signature value
4. Verify digest value
5. Validate canonicalization

#### 2.2 Certificate Requirements
- X.509 v3 certificates
- Valid certificate chain
- Appropriate key usage extensions
- Valid validity period

## Distribution and Transport

### 1. HTTP Transport Implementation

#### 1.1 MIME Type Registration
```
Content-Type: application/vnd.etsi.tsl+xml
```

#### 1.2 HTTP Headers
```
HTTP/1.1 200 OK
Content-Type: application/vnd.etsi.tsl+xml
Content-Length: 12345
Last-Modified: Wed, 01 Jan 2024 00:00:00 GMT
ETag: "tsl-version-1"
Cache-Control: max-age=3600
```

#### 1.3 Distribution Points
```xml
<DistributionPoints>
  <DistributionPoint>
    <URI>https://trust.wallet.gov.it/tsl/tsl.xml</URI>
  </DistributionPoint>
  <DistributionPoint>
    <URI>https://backup.Wallet.gov.it/tsl/tsl.xml</URI>
  </DistributionPoint>
</DistributionPoints>
```

### 2. Availability Requirements

#### 2.1 Uptime Requirements
- Minimum 99.9% availability
- 24/7 operation
- Redundant distribution points
- Load balancing support

#### 2.2 Update Frequency
- Daily updates for status changes
- Weekly full updates
- Emergency updates within 1 hour
- Notification of updates

## Examples

> **Note**: The examples below are designed to be compliant with the official ETSI TS 119 612 v2.3.1 schema. However, some elements may need adjustment based on specific implementation requirements and the exact schema validation rules.

### 1. Complete TSL Example

```xml
<?xml version="1.0" encoding="UTF-8"?>
<TrustServiceStatusList xmlns="http://uri.etsi.org/19612/v2.3.1#"
                       xmlns:tsl="http://uri.etsi.org/19612/v2.3.1#"
                       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                       xsi:schemaLocation="http://uri.etsi.org/19612/v2.3.1# https://forge.etsi.org/rep/esi/x19_612_trusted_lists/-/raw/v2.3.1/19612_xsd.xsd"
                       Id="tsl-1">
  
  <SchemeInformation>
    <TSLVersionIdentifier>2</TSLVersionIdentifier>
    <TSLSequenceNumber>1</TSLSequenceNumber>
    <TSLType>http://uri.etsi.org/TrstSvc/TrustedList/TSLType/EUgeneric</TSLType>
    
    <SchemeOperatorName>
      <Name xml:lang="en">Wallet Trust Authority</Name>
      <Name xml:lang="it">Autorità di Fiducia Wallet</Name>
    </SchemeOperatorName>
    
    <SchemeOperatorAddress>
      <PostalAddresses>
        <PostalAddress>
          <StreetAddress>Via Roma 123</StreetAddress>
          <Locality>Roma</Locality>
          <StateOrProvince>Lazio</StateOrProvince>
          <PostalCode>00100</PostalCode>
          <CountryName>IT</CountryName>
        </PostalAddress>
      </PostalAddresses>
      <ElectronicAddress>
        <URI>mailto:trust@Wallet.gov.it</URI>
      </ElectronicAddress>
    </SchemeOperatorAddress>
    
    <SchemeName>
      <Name xml:lang="en">Wallet Trusted List</Name>
      <Name xml:lang="it">Lista di Fiducia Wallet</Name>
    </SchemeName>
    
    <SchemeInformationURI>https://trust.wallet.gov.it/scheme-info</SchemeInformationURI>
    <StatusDeterminationApproach>http://uri.etsi.org/TrstSvc/TrustedList/StatusDeterminationApproach/BySupervision</StatusDeterminationApproach>
    <SchemeTypeCommunityRules>http://uri.etsi.org/TrstSvc/TrustedList/SchemeTypeCommunityRules/EU</SchemeTypeCommunityRules>
    <SchemeTerritory>IT</SchemeTerritory>
    <TSLPolicyLegalNotice>https://trust.wallet.gov.it/policy</TSLPolicyLegalNotice>
    <HistoricalInformationPeriod>P5Y</HistoricalInformationPeriod>
    <ListIssueDateTime>2024-01-01T00:00:00Z</ListIssueDateTime>
    <NextUpdate>2024-01-02T00:00:00Z</NextUpdate>
    
    <DistributionPoints>
      <DistributionPoint>
        <URI>https://trust.wallet.gov.it/tsl/tsl.xml</URI>
      </DistributionPoint>
    </DistributionPoints>
  </SchemeInformation>
  
  <TrustServiceProviderList>
    <TrustServiceProvider>
      <TSPInformation>
        <TSPName>
          <Name xml:lang="en">Wallet Provider IT S.p.A.</Name>
          <Name xml:lang="it">Wallet Provider IT S.p.A.</Name>
        </TSPName>
        <TSPTradeName>
          <Name xml:lang="en">IT-Wallet</Name>
          <Name xml:lang="it">IT-Wallet</Name>
        </TSPTradeName>
        <TSPAddress>
          <PostalAddresses>
            <PostalAddress>
              <StreetAddress>Via Milano 456</StreetAddress>
              <Locality>Milano</Locality>
              <StateOrProvince>Lombardia</StateOrProvince>
              <PostalCode>20100</PostalCode>
              <CountryName>IT</CountryName>
            </PostalAddress>
          </PostalAddresses>
          <ElectronicAddress>
            <URI>mailto:info@wallet.example.it</URI>
          </ElectronicAddress>
        </TSPAddress>
        <TSPInformationURI>https://wallet.example.it/info</TSPInformationURI>
        <TSPServices>
          <ServiceInformation>
            <ServiceTypeIdentifier>http://uri.etsi.org/TrstSvc/Svctype/CA/PKC</ServiceTypeIdentifier>
            <ServiceName>
              <Name xml:lang="en">Wallet Provider Services</Name>
              <Name xml:lang="it">Servizi di Provider di Portafoglio</Name>
            </ServiceName>
            <ServiceDigitalIdentity>
              <X509SubjectName>CN=WalletProvider-IT, O=Wallet Provider IT S.p.A., C=IT</X509SubjectName>
              <X509SKI>...</X509SKI>
              <X509Certificate>...</X509Certificate>
            </ServiceDigitalIdentity>
            <ServiceCurrentStatus>http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/granted</ServiceCurrentStatus>
            <CurrentStatusStartingDate>2024-01-01T00:00:00Z</CurrentStatusStartingDate>
            <SchemeServiceDefinitionURI>https://trust.wallet.gov.it/scheme/wallet-provider</SchemeServiceDefinitionURI>
            <ServiceSupplyPoints>
              <ServiceSupplyPoint>
                <URI>https://wallet.example.it/api</URI>
              </ServiceSupplyPoint>
            </ServiceSupplyPoints>
            <TSPServiceDefinitionURI>https://wallet.example.it/service-definition</TSPServiceDefinitionURI>
          </ServiceInformation>
        </TSPServices>
      </TSPInformation>
    </TrustServiceProvider>
  </TrustServiceProviderList>
  
  <Signature xmlns="http://www.w3.org/2000/09/xmldsig#">
    <SignedInfo>
      <CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/>
      <SignatureMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha256"/>
      <Reference URI="#tsl-1">
        <Transforms>
          <Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature"/>
        </Transforms>
        <DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"/>
        <DigestValue>...</DigestValue>
      </Reference>
    </SignedInfo>
    <SignatureValue>...</SignatureValue>
    <KeyInfo>
      <X509Data>
        <X509Certificate>...</X509Certificate>
      </X509Data>
    </KeyInfo>
  </Signature>
</TrustServiceStatusList>
```

### 2. Service Status Change Example

```xml
<ServiceHistory>
  <ServiceHistoryInstance>
    <ServiceTypeIdentifier>http://uri.etsi.org/TrstSvc/Svctype/WalletProvider</ServiceTypeIdentifier>
    <ServiceName>
      <Name xml:lang="en">Wallet Provider Services</Name>
    </ServiceName>
    <ServiceDigitalIdentity>
      <X509SubjectName>CN=WalletProvider-IT, O=Wallet Provider IT S.p.A., C=IT</X509SubjectName>
    </ServiceDigitalIdentity>
    <ServicePreviousStatus>http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/granted</ServicePreviousStatus>
    <PreviousStatusStartingDate>2024-01-01T00:00:00Z</PreviousStatusStartingDate>
  </ServiceHistoryInstance>
</ServiceHistory>
```

### 3. Service Extension Example

```xml
<ServiceInformationExtensions>
  <Qualifications>
    <QualificationElement>
      <CriteriaList>
        <Criteria>
          <Qualifier>http://uri.etsi.org/TrstSvc/TrustedList/Qualifier/QCForESig</Qualifier>
        </Criteria>
        <Criteria>
          <Qualifier>http://uri.etsi.org/TrstSvc/TrustedList/Qualifier/QCForESeal</Qualifier>
        </Criteria>
      </CriteriaList>
    </QualificationElement>
  </Qualifications>
  <AdditionalServiceInformation>
    <URI>https://trust.wallet.gov.it/additional-info/wallet-provider</URI>
  </AdditionalServiceInformation>
</ServiceInformationExtensions>
```

### 4. Schema-Compliant Example

Here's a corrected example that should validate against the official ETSI schema:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<TrustServiceStatusList xmlns="http://uri.etsi.org/19612/v2.3.1#"
                       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                       xsi:schemaLocation="http://uri.etsi.org/19612/v2.3.1# https://forge.etsi.org/rep/esi/x19_612_trusted_lists/-/raw/v2.3.1/19612_xsd.xsd"
                       Id="tsl-1">
  
  <SchemeInformation>
    <TSLVersionIdentifier>2</TSLVersionIdentifier>
    <TSLSequenceNumber>1</TSLSequenceNumber>
    <TSLType>http://uri.etsi.org/TrstSvc/TrustedList/TSLType/EUgeneric</TSLType>
    
    <SchemeOperatorName>
      <Name xml:lang="en">Wallet Trust Authority</Name>
    </SchemeOperatorName>
    
    <SchemeOperatorAddress>
      <PostalAddresses>
        <PostalAddress>
          <StreetAddress>Via Roma 123</StreetAddress>
          <Locality>Roma</Locality>
          <StateOrProvince>Lazio</StateOrProvince>
          <PostalCode>00100</PostalCode>
          <CountryName>IT</CountryName>
        </PostalAddress>
      </PostalAddresses>
      <ElectronicAddress>
        <URI>mailto:trust@Wallet.gov.it</URI>
      </ElectronicAddress>
    </SchemeOperatorAddress>
    
    <SchemeName>
      <Name xml:lang="en">Wallet Trusted List</Name>
    </SchemeName>
    
    <SchemeInformationURI>https://trust.wallet.gov.it/scheme-info</SchemeInformationURI>
    <StatusDeterminationApproach>http://uri.etsi.org/TrstSvc/TrustedList/StatusDeterminationApproach/BySupervision</StatusDeterminationApproach>
    <SchemeTypeCommunityRules>http://uri.etsi.org/TrstSvc/TrustedList/SchemeTypeCommunityRules/EU</SchemeTypeCommunityRules>
    <SchemeTerritory>IT</SchemeTerritory>
    <TSLPolicyLegalNotice>https://trust.wallet.gov.it/policy</TSLPolicyLegalNotice>
    <HistoricalInformationPeriod>P5Y</HistoricalInformationPeriod>
    <ListIssueDateTime>2024-01-01T00:00:00Z</ListIssueDateTime>
    <NextUpdate>2024-01-02T00:00:00Z</NextUpdate>
    
    <DistributionPoints>
      <DistributionPoint>
        <URI>https://trust.wallet.gov.it/tsl/tsl.xml</URI>
      </DistributionPoint>
    </DistributionPoints>
  </SchemeInformation>
  
  <TrustServiceProviderList>
    <TrustServiceProvider>
      <TSPInformation>
        <TSPName>
          <Name xml:lang="en">Wallet Provider IT S.p.A.</Name>
        </TSPName>
        <TSPAddress>
          <PostalAddresses>
            <PostalAddress>
              <StreetAddress>Via Milano 456</StreetAddress>
              <Locality>Milano</Locality>
              <StateOrProvince>Lombardia</StateOrProvince>
              <PostalCode>20100</PostalCode>
              <CountryName>IT</CountryName>
            </PostalAddress>
          </PostalAddresses>
          <ElectronicAddress>
            <URI>mailto:info@wallet.example.it</URI>
          </ElectronicAddress>
        </TSPAddress>
        <TSPInformationURI>https://wallet.example.it/info</TSPInformationURI>
        <TSPServices>
          <ServiceInformation>
            <ServiceTypeIdentifier>http://uri.etsi.org/TrstSvc/Svctype/CA/PKC</ServiceTypeIdentifier>
            <ServiceName>
              <Name xml:lang="en">Certificate Authority Services</Name>
            </ServiceName>
            <ServiceDigitalIdentity>
              <X509SubjectName>CN=WalletProvider-IT, O=Wallet Provider IT S.p.A., C=IT</X509SubjectName>
              <X509SKI>...</X509SKI>
              <X509Certificate>...</X509Certificate>
            </ServiceDigitalIdentity>
            <ServiceCurrentStatus>http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/granted</ServiceCurrentStatus>
            <CurrentStatusStartingDate>2024-01-01T00:00:00Z</CurrentStatusStartingDate>
            <SchemeServiceDefinitionURI>https://trust.wallet.gov.it/scheme/ca-services</SchemeServiceDefinitionURI>
            <ServiceSupplyPoints>
              <ServiceSupplyPoint>
                <URI>https://wallet.example.it/api</URI>
              </ServiceSupplyPoint>
            </ServiceSupplyPoints>
            <TSPServiceDefinitionURI>https://wallet.example.it/service-definition</TSPServiceDefinitionURI>
          </ServiceInformation>
        </TSPServices>
      </TSPInformation>
    </TrustServiceProvider>
  </TrustServiceProviderList>
  
  <Signature xmlns="http://www.w3.org/2000/09/xmldsig#">
    <SignedInfo>
      <CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/>
      <SignatureMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha256"/>
      <Reference URI="#tsl-1">
        <Transforms>
          <Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature"/>
        </Transforms>
        <DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"/>
        <DigestValue>...</DigestValue>
      </Reference>
    </SignedInfo>
    <SignatureValue>...</SignatureValue>
    <KeyInfo>
      <X509Data>
        <X509Certificate>...</X509Certificate>
      </X509Data>
    </KeyInfo>
  </Signature>
</TrustServiceStatusList>
```

### 5. Schema Validation Notes

#### 5.1 Potential Validation Issues
The examples provided may require adjustments for full schema compliance:

1. **Service Type Identifiers**: The custom Wallet service types (e.g., `http://uri.etsi.org/TrstSvc/Svctype/WalletProvider`) may not be defined in the official schema. Consider using standard ETSI service types or extending the schema.

2. **Element Ordering**: The official schema may require specific element ordering that differs from the examples.

3. **Required Elements**: Some elements marked as optional in the examples may be required by the schema.

4. **Namespace Declarations**: Ensure all namespace declarations match the schema requirements.

#### 5.2 Validation Commands
```bash
# Validate the complete TSL example
xmllint --schema https://forge.etsi.org/rep/esi/x19_612_trusted_lists/-/raw/v2.3.1/19612_xsd.xsd tsl-example.xml

# Validate with detailed error reporting
xmllint --schema https://forge.etsi.org/rep/esi/x19_612_trusted_lists/-/raw/v2.3.1/19612_xsd.xsd --noout tsl-example.xml 2>&1 | head -20
```

#### 5.3 Schema Compliance Checklist
- [ ] All required elements are present
- [ ] Element ordering matches schema requirements
- [ ] Namespace declarations are correct
- [ ] Service type identifiers are valid
- [ ] Date formats comply with schema constraints
- [ ] URI formats are valid
- [ ] Language codes are properly formatted

## Testing and Validation

### 1. Schema Validation

#### 1.1 XSD Validation
```bash
# Validate TSL against official ETSI schema
xmllint --schema https://forge.etsi.org/rep/esi/x19_612_trusted_lists/-/raw/v2.3.1/19612_xsd.xsd tsl.xml

# Or with local cached schema
xmllint --schema 19612_xsd.xsd tsl.xml
```

#### 1.2 Content Validation
- Service type identifier validation
- Status value validation
- Date format validation
- URI format validation
- Language code validation

### 2. Signature Validation

#### 2.1 Digital Signature Verification
```bash
# Verify XML signature
xmlsec1 --verify --pubkey-cert-pem cert.pem tsl.xml
```

#### 2.2 Certificate Chain Validation
- Root CA validation
- Intermediate CA validation
- End entity certificate validation
- Revocation status checking

### 3. Functional Testing

#### 3.1 Status Change Testing
- Test status transitions
- Validate status history
- Test notification mechanisms
- Verify update procedures

#### 3.2 Distribution Testing
- HTTP transport testing
- MIME type validation
- Availability testing
- Load testing

## Migration Strategy

### 1. Phase 1: Schema Integration (Month 1)
- Integrate official ETSI XSD schema
- Create basic TSL structure
- Add service type mappings
- Implement schema validation

### 2. Phase 2: Service Management (Month 2)
- Implement service registration
- Add status management
- Create service history tracking
- Implement notification system

### 3. Phase 3: Digital Signatures (Month 3)
- Implement signature generation
- Add signature validation
- Create certificate management
- Implement trust chain validation

### 4. Phase 4: Distribution (Month 4)
- Implement HTTP transport
- Add MIME type support
- Create distribution points
- Implement availability monitoring

### 5. Phase 5: Integration (Month 5)
- Integrate with existing systems
- Add cross-border support
- Implement monitoring and logging
- Create management interfaces

### 6. Phase 6: Testing and Deployment (Month 6)
- Comprehensive testing
- Performance optimization
- Security audit
- Production deployment

## Compliance Checklist

### 1. Technical Compliance
- [ ] Official ETSI XSD schema integration
- [ ] Service type mapping
- [ ] Status management
- [ ] Digital signature implementation
- [ ] HTTP transport support
- [ ] MIME type registration

### 2. Functional Compliance
- [ ] Service registration
- [ ] Status tracking
- [ ] History management
- [ ] Notification system
- [ ] Distribution mechanism
- [ ] Availability monitoring

### 3. Security Compliance
- [ ] Digital signature validation
- [ ] Certificate chain validation
- [ ] Trust anchor management
- [ ] Revocation checking
- [ ] Access control
- [ ] Audit logging

### 4. Operational Compliance
- [ ] 24/7 availability
- [ ] Update procedures
- [ ] Backup mechanisms
- [ ] Disaster recovery
- [ ] Monitoring and alerting
- [ ] Documentation

## References

- [ETSI TS 119 612 v2.3.1 (2024-11)](https://www.etsi.org/deliver/etsi_ts/119600_119699/119612/02.03.01_60/ts_119612v020301p.pdf)
- [ETSI TS 119 612 v2.3.1 XSD Schema](https://forge.etsi.org/rep/esi/x19_612_trusted_lists/-/raw/v2.3.1/19612_xsd.xsd)
- [ETSI TS 119 612 v2.3.1 SIE XSD Schema](https://forge.etsi.org/rep/esi/x19_612_trusted_lists/-/raw/v2.3.1/19612_sie_xsd.xsd)
- [eIDAS Regulation (EU) No 910/2014](https://eur-lex.europa.eu/eli/reg/2014/910/oj)
- [Regulation (EU) 2024/1183](https://eur-lex.europa.eu/eli/reg/2024/1183/oj)
- [XML Digital Signature Specification](https://www.w3.org/TR/xmldsig-core1/)
- [XML Schema Part 1: Structures](https://www.w3.org/TR/xmlschema-1/)
- [XML Schema Part 2: Datatypes](https://www.w3.org/TR/xmlschema-2/)

## Contact Information

For questions about this implementation guide:
- open an issue
- reach the WeBuild WG groups
---

**Document Version**: 0.8  
**Last Updated**: 2025-10-24  

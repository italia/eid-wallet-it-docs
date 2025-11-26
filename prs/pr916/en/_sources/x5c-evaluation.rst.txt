X.509 Certificate Management Operations
=========================================

This section defines the operational procedures for X.509 Certificate management within the IT-Wallet federation, covering X.509 Certificate chain analysis, validation procedures, and revocation verification. These procedures complement the federation onboarding processes and support ongoing X.509 Certificate lifecycle management for all the participants.

For the foundational X.509 PKI infrastructure and certificate issuance procedures, see :ref:`trust-infrastructure:X.509 PKI`.

Federation PKI Architecture
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The IT-Wallet federation operates a hierarchical Public Key Infrastructure where:

	- **Trust Anchor**: Acts as Root X.509 Certificate Authority where CA X.509 Certificates MUST NOT exceed **5-year validity period**.
	- **Federation Entity X.509 Certificate**: Each federation participant receives an X.509 certificate that operates as a limited sub-CA where X.509 Certificates MUST NOT exceed **2-year validity period**.
	- **Protocol X.509 Certificates**: Self-issued X.509 Certificates for internal services where X.509 Certificates SHOULD NOT exceed **1-year validity period**.

Each federation entity MUST expose its Federation Entity X.509 Certificate on a publicly accessible endpoint. The Federation Entity private key serves dual purposes:

	1. Self-issuing Protocol X.509 Certificates for internal cryptographic operations (limited sub-CA capability).
	2. Acting as the Federation Entity Key for signing Entity Statements.

.. note:: 
  Federation Leaves can ONLY issue X.509 Certificates about themselves and for application specific purposes. Federation Leaves MUST NOT issue X.509 Certificates for other federation entities, as limited by their Federation Authorities using X.509 Name Constraints extension.

For protocol specific X.509 Certificates, with validity periods exceeding 24 hours, the issuing entity MUST publish and regularly update an X.509 Certificate Revocation List (CRL) on a publicly accessible endpoint.

X.509 Certificate Chain Structure and Analysis
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Federation entities receive X.509 Certificate chains during the onboarding process. Federation entities MUST validate these chains about themselves.


X.509 Certificate Chain Visualization
""""""""""""""""""""""""""""""""""""""

The following script enables federation entities to:

	- Extract X.509 certificate details for verification.
	- Analyze X.509 certificate extensions and constraints.
	- Verify X.509 certificate hierarchy and relationships

.. literalinclude:: ../../utils/certificate-chain-analysis.sh
   :language: bash
   :caption: X.509 Certificate chain analysis script


X.509 Certificate Chain Validation
""""""""""""""""""""""""""""""""""

Federation entities MUST validate X.509 certificate chains to ensure proper trust establishment and verify compliance with federation PKI requirements.

A non-normative exampe of X.509 Certificate chain validation procedure is given below:

.. literalinclude:: ../../utils/certificate-chain-validation.sh
   :language: bash
   :caption: X.509 Certificate chain validation script


Federation entities SHOULD verify:

	1. **X.509 Certificate Signatures**: Each X.509 Certificate MUST be properly signed by its issuer.
	2. **X.509 Certificate Chain Integrity**: Issuer-Subject relationships MUST be valid throughout the X.509 Certificate chain.
	3. **X.509 Certificate Validity Periods**: All X.509 Certificates MUST be within their validity periods and MUST comply with federation limits.
	4. **X.509 Certificate Extensions**: Basic Constraints and Key Usage MUST comply with federation requirements:

		- Federation Entity X.509 Certificates: ``CA:TRUE, pathlen:0`` (can only issue certificates about itself).
		- Protocol X.509 Certificates: ``CA:FALSE`` (cannot issue certificates).

X.509 Certificate Revocation Management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Federation entities MUST implement X.509 Certificate revocation verification to ensure ongoing trust validation and compliance with federation security requirements.

CRL Distribution and Access
""""""""""""""""""""""""""""

Federation authorities publish X.509 Certificate Revocation Lists (CRL) at publicly accessible endpoints. Federation entities MUST be able to access and process these CRL distributions for revocation verification.

The following procedure enables federation entities to:

	- Locate CRL distribution endpoints from X.509 Certificates.
	- Download current revocation lists.
	- Analyze CRL content and validity periods.

.. literalinclude:: ../../utils/crl-analysis.sh
   :language: bash


X.509 Certificate Revocation Verification
""""""""""""""""""""""""""""""""""""""""""

Federation entities MUST verify X.509 certificate revocation status by checking X.509 certificate serial numbers against current X.509 Certificate Revocation Lists.

Federation entities SHOULD implement automated revocation checking for:

	- **Federation Entity X.509 Certificates**: Verify own X.509 certificate status periodically.
	- **Peer Entity X.509 Certificates**: Validate X.509 Certificates of other federation participants.
	- **Trust Chain Validation**: Ensure entire X.509 certificate chains remain valid.

Below a bash script for X.509 certificate revocation status verification is given as a non-normative example:

.. literalinclude:: ../../utils/certificate-revocation-verification.sh
   :language: bash


X.509 Certificate Management Best Practices
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

X.509 Certificate Validation Integration
""""""""""""""""""""""""""""""""""""""""

Federation entities SHOULD integrate X.509 Certificate validation procedures into their standard federation operations:

	1. **Entity Configuration Updates**: Verify X.509 Certificate chains when processing authority hints and X.509 Certificate updates.
	2. **Trust Chain Construction**: Validate all X.509 Certificates during trust chain building procedures.
	3. **X.509 PKI Operations**: Perform X.509 Certificate revocation checks using CRL endpoints.
	4. **Protocol Certificate Management**: Validate self-issued protocol specific X.509 Certificate for internal services.
	5. **Periodic Validation**: Implement regular X.509 Certificate and CRL validation schedules.

Diagnostic and Troubleshooting
"""""""""""""""""""""""""""""""

Federation entities MUST implement diagnostic procedures to identify and resolve X.509 Certificate-related issues:

  - **X.509 Certificate Validation**, including:

    - **Authority Key Identifier Mismatches**: CRL Authority Key Identifier does not match Trust Anchor Subject Key Identifier.
    - **Trust Anchor X.509 Certificate Rotation**: Outdated Trust Anchor X.509 Certificate causing validation failures.
    - **Serial Number Format Issues**: Serial number normalization problems in revocation checking.

  - **CRL Validation Failure**: When CRL validation fails, federation entities SHOULD:

    1. **Verify Trust Anchor X.509 Certificate**: Ensure current Trust Anchor X.509 certificate is being used.
    2. **Check Authority Key Identifier**: Compare CRL Authority Key Identifier with Trust Anchor Subject Key Identifier.
    3. **Validate CRL Signature**: Verify CRL is properly signed by expected issuing authority.
    4. **Update Trust Anchor X.509 Certificate**: Download updated Trust Anchor X.509 certificate if rotation has occurred.

  - **Endpoint Accessibility Verification**: Federation entities SHOULD implement connectivity testing for certificate infrastructure endpoints.


The following non-normative example provides a script for Federation X.509 certificate infrastructure connectivity test:

.. literalinclude:: ../../utils/federation-connectivity-test.sh
   :language: bash


X.509 Certificate Lifecycle Coordination
""""""""""""""""""""""""""""""""""""""""""

Federation entities MUST coordinate X.509 Certificate management with federation lifecycle procedures following the established validity periods:

- **X.509 Certificate Renewal**: Align X.509 certificate renewals with Entity Configuration updates and Trust Mark refresh cycles, according to the federation limits defined in :ref:`x5c-evaluation:Federation PKI Architecture`.
- **Key Rotation**: Coordinate Federation Entity Key rotation with X.509 certificate renewal procedures.
- **CRL Management**: For Protocol X.509 Certificates with validity > 24 hours, maintain current CRL publication.
- **Federation Exit**: Ensure proper X.509 Certificate revocation during voluntary or supervisory body-initiated federation exit.


Entity Lifecycle Management
----------------------------

This section provides technical implementation procedures for entity lifecycle management. For high-level lifecycle concepts and business processes, see :ref:`onboarding-high-level:Entity Lifecycle Management`.

While administrative data update MUST follow governance processes that are out of scope of this technical specification, technical configuration updates are described in the following sections.

Technical Configuration Updates
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Technical updates affecting federation protocol operations MUST follow specific procedures for:

  - **X.509 Certificate Renewal**

    1. **Pre-renewal Preparation**: The Entity MUST generate a new CSR with updated X.509 certificate information.
    2. **Renewal Request**: The Entity MUST submit renewal request with new CSR following the same technical procedure as initial onboarding.
    3. **X.509 Certificate Integration**: The Entity MUST update its Entity Configuration with new X.509 certificate chain in ``x5c`` parameter.
    4. **Trust Chain Validation**: The Entity MUST verify updated Trust Chain through ``/resolve`` endpoint.
    5. **Registry Update**: The Entity SHOULD confirm updated entity information in Trust Anchor ``/list`` endpoint.

  - **Key Rotation**

    1. **Key Activation**: In case of incident or planned rotation, the Entity MUST activate an alternative Federation Entity Key for signing operations.
    2. **New Key Generation**: The Entity MUST generate a new Federation Entity Public Key pair to serve as an additional key.
    3. **Parallel Key Publication**: The Entity MUST publish all available keys in Entity Configuration ``jwks`` claim during transition period.
    4. **X.509 Certificate Request**: The Entity MUST request new X.509 certificate for new key following standard procedure.
    5. **Gradual Migration**: The Entity MUST update Entity Configuration to use the activated key for signing while maintaining all keys for verification.
    6. **Old Key Deprecation**: The Entity MUST remove the old key from Entity Configuration after validation period, maintaining the alternative key and new key.

  - **Metadata Updates**

    - **Endpoint Changes**: The Entity MAY update service endpoints in entity-specific metadata.
    - **Capability Updates**: The Entity MAY modify supported protocols, algorithms, or service capabilities within the constraints defined by this IT-Wallet implementation profile.



All technical updates MUST be validated through:

  1. **Entity Configuration Validation**: The Entity MUST verify updated EC structure and content.
  2. **Trust Chain Resolution**: The Entity MUST confirm ``/resolve`` endpoint returns valid Trust Chain.
  3. **Federation Status**: The Entity MUST verify entity operational status in federation registry.
  4. **Integration Testing**: The Entity SHOULD test federation protocol operations with updated configuration.

Technical Federation Exit Procedures
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For business context on federation exit processes, see :ref:`onboarding-high-level:Federation Exit and Removal Processes`. This section covers technical implementation procedures.

Voluntary Exit - Technical Deactivation
""""""""""""""""""""""""""""""""""""""""""

  1. **X.509 Certificate Revocation Request**: The Entity MUST submit a X.509 Certificate revocation request to Federation Authority with revocation reason. The request MUST be signed with the Federation Entity Private Key corresponding to the X.509 Certificate being revoked to prove the legitimacy of the revocation request.
  2. **CRL Update Verification**: The Federation Authority MUST revoke the Entity's X.509 Certificate and the Entity MUST verify they appear in updated X.509 Certificate Revocation List.
  3. **Subordinate Statement Removal**: The Federation Authority MUST completely remove the Entity's Subordinate Statement from the Federation Registry to prevent any trust relationship validation, and therefore remove any reference to that Entity in the listing endpoint, resolve endpoint or trust marked listing endpoint.
  4. **Entity Configuration Deactivation**: The Entity MUST deactivate its Entity Configuration. The Entity MAY either:

     a. Remove the Entity Configuration completely from the ``/.well-known/openid-federation`` endpoint (returning HTTP 404), OR
     b. Keep the Entity Configuration as expired (with ``exp`` claim in the past). It therefore MUST NOT update it with fresh timestamps.

  5. **Registry Status Update**: The Entity SHOULD verify removal from Federation Registry, also verifying the Trust Mark status using the Trust Mark Status endpoint. 

Non-normative example of X.509 Certificate revocation request following :rfc:`3280` format:

.. code-block:: text

   X.509 Certificate Revocation Request:
   Subject: CN=credentials.example.gov, OU=Digital Credentials, O=Example Organization, L=Roma, ST=Lazio, C=IT, emailAddress=technical@credentials.example.gov
   X.509 Certificate Serial Number: 987654321
   Revocation Reason: cessation_of_operation (5)
   Revocation Date: 2025-12-31T23:59:59Z

   Request signed with Federation Entity Private Key corresponding to:
   Public Key Algorithm: id-ecPublicKey
   ASN1 OID: prime256v1
   NIST CURVE: P-256
   Key ID: NsXymfIILEPR5Y0t

   Note: The CRR MUST be signed with the same private key that corresponds to the
   X.509 certificate being revoked to authenticate the revocation request.

Example CRR in DER format (Base64 encoded):

.. code-block:: text

   -----BEGIN CERTIFICATE REVOCATION REQUEST-----
   MIIBVjCB/wIBADBpMQswCQYDVQQGEwJJVDEOMAwGA1UECAwFTGF6aW8xDTALBgNV
   BAcMBFJvbWExGjAYBgNVBAoMEUV4YW1wbGUgT3JnYW5pemF0aW9uMR8wHQYDVQQD
   DBZjcmVkZW50aWFscy5leGFtcGxlLmdvdjBZMBMGByqGSM49AgEGCCqGSM49AwEH
   A0IABIBgZ4HBgUCNXwY5LJSlKzm7gXY4FApFJCj91Gpb1K9GEIouTq2X3L0K64Iq
   0ob4l_gslT14644zbYXYF-xmw7aPdlbMuw3T1URwI4nafMtKrYwDQYJKoZIhvcNAQ
   kEAwIJrRLl1VR987654321gBgJKwYBBQUHAgEWHGh0dHBzOi8vZXhhbXBsZS5vcmcv
   cG9saWN5MAoGCCqGSM49BAMCA0gAMEUCIQC9h3Y6hFgd7zUzZyBrQ3jJ8HmVF2Qa
   -----END CERTIFICATE REVOCATION REQUEST-----

Supervisory Body Removal - Technical Implementation
""""""""""""""""""""""""""""""""""""""""""""""""""""""

  1. **Emergency X.509 Certificate Revocation**: The Federation Authority MUST immediately revoke X.509 Certificate with appropriate reason code (e.g., "Key Compromise", "Cessation of Operation").
  2. **CRL Emergency Update**: The Trust Anchor MUST publish updated CRL within emergency timeframe.
  3. **Subordinate Statement Removal**: The Federation Authority MUST immediately stop issuing the Entity's Subordinate Statements using the fetch endpoint, and or any reference to that Entity using the listing endpoint, or the trust marked listing endpoint, or the resolve endpoint.
  4. **Entity Configuration Invalidation**: The Entity's Configuration at ``/.well-known/openid-federation`` becomes invalid due to X.509 Certificate revocation (signature verification fails).
  5. **Trust Chain Invalidation**: Trust Chain resolution MUST return error status for affected entity.
  6. **Service Endpoint Isolation**: Federation infrastructure MUST block access to federation service endpoints.

Example emergency revocation verification:

.. code-block:: bash

   # Check emergency CRL update
   curl -o emergency.crl https://trust-anchor.eid-wallet.example.it/pki/ta-sub.crl
   openssl crl -in emergency.crl -text -noout | grep "Last Update"
   
   # Verify Trust Chain resolution fails
   curl "https://trust-anchor.eid-wallet.example.it/resolve?sub=https%3A//suspended-entity.example.it&trust_anchor=https%3A//trust-registry.eid-wallet.example.it"
   # Expected: HTTP 404 or specific error response

**Component-Level Technical Modifications**

Specific technical components MAY be modified while maintaining federation membership:

.. code-block:: json

   {
     "iss": "https://ci.example.it",
     "sub": "https://ci.example.it",
     "jwks": { 
       // jwks content
     },
     "metadata": {
       "openid_credential_issuer": {
         "credential_endpoint": "https://ci.example.it/credential",
         "credentials_supported": [ ]
         // removed: "batch_credential_endpoint" for maintenance
       }
     }
   }

The Entity MUST follow these steps for component modifications:

1. **Entity Configuration Update**: The Entity MUST modify metadata to reflect component changes.
2. **Trust Chain Revalidation**: The Entity MUST verify updated configuration through ``/resolve`` endpoint.
3. **Service Testing**: The Entity SHOULD test remaining federation protocol operations.
4. **Registry Verification**: The Entity SHOULD confirm updated capabilities in federation registry.

**Post-Exit Technical Obligations**

Entities that exit the federation MUST maintain the following for regulatory compliance:

1. **Historical Entity Configuration**: The Entity MUST maintain ``/.well-known/openid-federation`` endpoint accessibility for audit purposes.
2. **X.509 Certificate Chain Archive**: The Entity MUST keep X.509 Certificate chains accessible for existing Credential verification (minimum 7 years).
3. **Audit Log Preservation**: The Entity MUST archive federation protocol logs per regulatory requirements.

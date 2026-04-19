X.509 Certificate Management Operations
=========================================

This section describes PKIX work that operators perform once certificate material exists in the deployment. Typical tasks include building certificate chains, validating signatures and extensions, checking revocation status, planning renewal before expiry, and retiring credentials that are no longer authorised.

The relationship between OpenID Federation enrolment and PKIX, together with the rules for requesting certificate bundles, is explained in :ref:`trust-infrastructure:The Infrastructure of Trust` and in :ref:`trust-infrastructure:X.509 PKI`. Those chapters describe how participants obtain material during onboarding. The present section stays strictly on the PKIX side. Assessments MUST rely on conventional X.509 or PKIX libraries and command-line tools rather than on inference from federation metadata alone.

IT-Wallet PKI certificate classes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The normative PKIX issuance text remains in :ref:`trust-infrastructure:X.509 PKI`. The following tiers summarise how IT-Wallet groups PKIX material for orientation.

	- **Trust Anchor**: Root CA X.509 certificates MUST NOT exceed a **5-year** validity period.
	- **Entity issuance certificate**: Limited sub-CA certificate issued by a superior to a participant that is authorised to issue further X.509 certificates within policy constraints (Federation Intermediates in this profile). That certificate MUST NOT exceed a **2-year** validity period. Federation Leaves MUST NOT hold this role.
	- **Protocol certificate**: End-entity or service certificate with ``CA:FALSE`` for application use. Federation Leaves MUST NOT self-issue. Their protocol certificates MUST be issued by an Immediate Superior or by a certification authority that the superior delegates. Validity SHOULD NOT exceed **one year**.

For protocol-specific X.509 certificates whose validity exceeds twenty-four hours, the issuer MUST publish and maintain a CRL as specified in :ref:`trust-infrastructure:X.509 PKI`.

X.509 Certificate Chain Structure and Analysis
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Participants normally receive certificate chains while completing onboarding flows that are defined elsewhere in this specification. Regardless of how a chain was delivered, each participant MUST PKIX-validate the chain for its own use before relying on it.

X.509 Certificate Chain Visualization
""""""""""""""""""""""""""""""""""""""

The script below is a non-normative aid. It helps operators extract certificate fields, inspect extensions and constraints, and review the hierarchy that connects end-entity certificates to their issuers.

.. literalinclude:: ../../../utils/certificate-chain-analysis.sh
   :language: bash
   :caption: X.509 Certificate chain analysis script


X.509 Certificate Chain Validation
""""""""""""""""""""""""""""""""""

Each participant MUST PKIX-validate every received chain in line with `RFC 5280`_ and with the IT-Wallet PKIX profile in :ref:`trust-infrastructure:X.509 PKI`. Validation covers signatures, issuer-to-subject continuity, validity windows, and every extension that the profile marks as mandatory.

Non-normative validation example:

.. literalinclude:: ../../../utils/certificate-chain-validation.sh
   :language: bash
   :caption: X.509 Certificate chain validation script


Detailed extension expectations for issuance certificates compared with protocol certificates appear in :ref:`trust-infrastructure:X.509 PKI`.

X.509 Certificate Revocation Management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Participants MUST implement PKIX revocation checking for every certificate that their systems trust for authentication, signing, or transport protection.

CRL Distribution and Access
""""""""""""""""""""""""""""

Certificate issuers publish CRLs at endpoints that PKIX clients can reach without special credentials. Participants MUST be able to download a CRL, parse it, and map serial numbers to revocation entries whenever the PKIX profile requires CRL use.

The script below illustrates a non-normative workflow for locating CRL distribution points on a certificate, fetching the current list, and reviewing its freshness fields.

.. literalinclude:: ../../../utils/crl-analysis.sh
   :language: bash


X.509 Certificate Revocation Verification
""""""""""""""""""""""""""""""""""""""""""

Participants MUST determine revocation status by comparing each certificate serial number against the authoritative CRL (or another PKIX mechanism that the deployment adopts). They SHOULD automate that work for their own PKIX material, for peer material that they rely on, and for every intermediate certificate that remains in an active chain.

Non-normative revocation-check example:

.. literalinclude:: ../../../utils/certificate-revocation-verification.sh
   :language: bash


X.509 Certificate Management Best Practices
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

X.509 Certificate Validation Integration
""""""""""""""""""""""""""""""""""""""""

Whenever certificate material in use may have changed, repeat PKIX checks on the full chain, on every notBefore and notAfter field, and on revocation evidence such as CRL or OCSP responses. Apply the same discipline to protocol-facing certificates.

Diagnostic and Troubleshooting
"""""""""""""""""""""""""""""""

Participants MUST implement diagnostic procedures to identify and resolve X.509 certificate-related issues. Typical PKIX validation work includes at least the following checks.

  - **Authority key identifier mismatch.** The CRL Authority Key Identifier does not match the Trust Anchor Subject Key Identifier.
  - **Trust Anchor certificate rotation.** An outdated Trust Anchor certificate still anchors validation paths.
  - **Serial number normalisation.** Serial numbers are represented differently between certificates and CRL entries.

When CRL validation fails, participants SHOULD confirm that they trust the current Trust Anchor certificate, compare Authority Key Identifier values between the CRL and the Trust Anchor, validate the CRL signature with the expected issuer, and download a fresh Trust Anchor certificate if rotation has been announced.

Participants SHOULD also run connectivity tests toward the certificate infrastructure endpoints that their PKIX clients depend on.


The following non-normative example provides a script for PKI connectivity testing:

.. literalinclude:: ../../../utils/federation-connectivity-test.sh
   :language: bash


X.509 Certificate Lifecycle Coordination
""""""""""""""""""""""""""""""""""""""""""

Operational work SHOULD stay aligned with the PKIX class summaries earlier in :ref:`annex/x5c-evaluation:IT-Wallet PKI certificate classes`. PKIX tooling MUST cover validity windows and revocation evidence. Operators MUST publish CRLs whenever the PKIX profile demands them, and MUST complete revocation steps that governance requires when an entity exits.


Certificate material updates (PKIX)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Whenever a participant receives new, renewed, or reissued X.509 material, including after an issuer rotates a signing key, the participant MUST PKIX-validate the chain, notBefore and notAfter fields, and revocation status in line with this section and with :ref:`trust-infrastructure:X.509 Certificate Revocation`. The trust framework chapters :ref:`trust-infrastructure:The Infrastructure of Trust` and :ref:`entity-onboarding:Entity Onboarding` describe how that material is obtained.

After generating a new key pair, the participant obtains a matching certificate through the registration path in :ref:`entity-onboarding:Entity Onboarding`, PKIX-validates it before use, and retires superseded PKIX material according to local policy.

.. note::
   Initiating a participant key rotation is always a participant decision; the issuing authority responds with new PKIX material according to trust rules.


Entity Lifecycle Management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

High-level lifecycle and business rules are documented in :ref:`onboarding-high-level:Entity Lifecycle Management`. Administrative updates that sit outside PKIX remain governed by the wider programme rules.

Operational maintenance (PKIX)
""""""""""""""""""""""""""""""

  - **Renewal.** Generate a CSR, submit it through the trust registration process described in :ref:`entity-onboarding:Entity Onboarding`, install the issued certificates, and PKIX-validate them before production use.
  - **Key rotation.** Follow the same registration path for replacement keys, PKIX-validate the new material, and retire superseded certificates according to local policy and :ref:`trust-infrastructure:X.509 Certificate Revocation`.
  - **Service metadata.** When endpoints or capabilities change in a way that affects certificates or keys that are already in use, operators MUST run a fresh PKIX pass on every impacted artefact.

After substantive technical changes, PKIX-validate all impacted X.509 material using this section together with :ref:`trust-infrastructure:X.509 Certificate Revocation`. Additional deployment checks remain in the trust framework chapters.

Technical Exit Procedures (PKIX)
""""""""""""""""""""""""""""""""

Business context for exit appears in :ref:`onboarding-high-level:Federation Exit and Removal Processes`. Removal of federation registrations is specified in :ref:`trust-infrastructure:The Infrastructure of Trust`.

Voluntary Exit - PKIX and issuance
""""""""""""""""""""""""""""""""""

  1. **Revocation request.** Submit a signed revocation request to the issuing authority. The request MUST be signed with the private key that matches the certificate being revoked.
  2. **CRL verification.** Confirm that the certificate serial number appears on the updated CRL that the issuer publishes.
  3. **Trust-layer cleanup.** Complete de-registration with the issuing authority according to the trust framework rules that apply to your role.
  4. **Publication withdrawal.** Stop publishing participant trust material when governance requires it.
  5. **Operational confirmation.** When the deployment provides registry or status channels, operators SHOULD confirm that downstream consumers have picked up the revocation outcome. 

Non-normative example of X.509 Certificate revocation request following :rfc:`3280` format:

.. code-block:: text

   X.509 Certificate Revocation Request:
   Subject: CN=credentials.example.gov, OU=Digital Credentials, O=Example Organization, L=Roma, ST=Lazio, C=IT, emailAddress=technical@credentials.example.gov
   X.509 Certificate Serial Number: 987654321
   Revocation Reason: cessation_of_operation (5)
   Revocation Date: 2025-12-31T23:59:59Z

   Request signed with the private key corresponding to:
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

Supervisory removal (PKIX)
""""""""""""""""""""""""""

  1. **Emergency revocation**: Issuing authority revokes the certificate with an appropriate reason code.
  2. **CRL update**: Trust Anchor publishes an updated CRL within the emergency window.
  3. **Trust-layer suspension**: Issuing authority withdraws trust registrations for the participant per trust framework rules.
  4. **PKIX impact**: Relying parties MUST treat the certificate as untrusted after revocation and successful CRL verification.

Example emergency CRL check:

.. code-block:: bash

   curl -o emergency.crl https://trust-anchor.eid-wallet.example.it/pki/ta-sub.crl
   openssl crl -in emergency.crl -text -noout | grep "Last Update"

**Component-level changes**

Service components MAY change while the participant stays registered. Update published service metadata as required by the trust framework, PKIX-validate any impacted certificates, then run operational tests.

**Post-exit obligations**

1. **Historical publication**: Maintain required historical endpoints for audit if governance mandates.
2. **X.509 archive**: Keep certificate chains available for existing credential verification (minimum 7 years).
3. **Audit logs**: Archive logs per regulatory requirements.

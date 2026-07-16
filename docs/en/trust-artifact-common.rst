.. include:: ../common/common_definitions.rst

Common Trust Artifacts
----------------------

This section details the common artifacts involved in both the EUDIW and National Trust Frameworks, including:

- :ref:`infrastructure-trust:Entity Sign/Seal Certificate Profile`;
- :ref:`infrastructure-trust:Trust Anchor Certificate Profile`.

Entity Sign/Seal Certificate Profile
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section extends the general :ref:`infrastructure-trust:X.509 Certificate Profile` and specifies a **Certificate Profile** for **Entity Sign/Seal Certificates**, which are used for signing and sealing various Attestations. This profile is originally defined in `ETSI TS 119 412-6`_.

.. warning::

  The Entity Sign/Seal Certificate Profiles defined in this specification assume that Entity Sign/Seal Certificates are issued by a CA and are not self-signed. A self-signed certificate intended to act as a Trust Anchor is outside the scope of this certificate profile and MUST comply with the requirements defined in :ref:`infrastructure-trust:Trust Anchor Certificate Profile`.

PID Provider Sign/Seal Certificate
""""""""""""""""""""""""""""""""""

The specific requirements for PID Provider Sign/Seal Certificates are specified in Clause 4 of [`ETSI TS 119 412-6`_].

The following table defines the complete set of extensions applicable to the certificate profile. Extensions not listed in the table MUST NOT be present.

.. list-table:: PID Provider Sign/Seal Certificate Extensions
   :class: longtable
   :header-rows: 1
   :widths: 30 20 50

   * - **Extension**
     - **Presence**
     - **Notes**

   * - ``authorityKeyIdentifier``
     - REQUIRED
     - The value SHOULD be derived from the public key using the methods defined in :rfc:`5280#section-4.2.1.1`.

   * - ``subjectKeyIdentifier``
     - REQUIRED
     - The ``keyIdentifier`` field SHOULD be derived from the subject public key using the methods defined in :rfc:`5280#section-4.2.1.2`.

   * - ``keyUsage``
     - REQUIRED
     - It MUST contain one (and only one) of the key-usage settings *Type A*, *Type B*, *Type C*, or *Type F*.

   * - ``certificatePolicies``
     - REQUIRED
     - It MUST include a ``PolicyInformation`` structure with ``policyIdentifier`` set to ``0.4.0.2042.1.2`` (*NCP+*).

   * - ``subjectAltName``
     - REQUIRED
     -

   * - ``cRLDistributionPoints``
     - CONDITIONAL
     - **REQUIRED IF:** the certificate does not include any access location of an OCSP responder or the validity assured extension as defined in `ETSI EN 319 412-1`_.

   * - ``authorityInfoAccess``
     - REQUIRED
     - It MUST include an ``AccessDescription`` structure with ``accessMethod`` set to ``1.3.6.1.5.5.7.48.2`` (``id-ad-caIssuers``) and ``accessLocation`` specifying at least one access location of a valid CA certificate of the issuing CA.
     
       If OCSP is supported by the issuing CA, the extension MUST include an ``AccessDescription`` structure with ``accessMethod`` set to ``1.3.6.1.5.5.7.48.1`` (``id-ad-ocsp``) and ``accessLocation`` specifying at least one OCSP responder authoritative to provide certificate status information for the certificate, as described in :ref:`infrastructure-trust:Online Certificate Status Protocol (OCSP)`.

   * - ``qcStatements``
     - REQUIRED
     - It MUST contain a ``QCStatement`` structure with ``statementId`` set to ``0.4.0.1862.1.6`` (``id-etsi-qcs-QcType``). The corresponding ``statementInfo`` MUST contain a ``QcType`` structure including exactly one object identifier, namely ``0.4.0.194126.1.1`` (``id-etsi-qct-pid``), as defined in Clause 4.5 of [`ETSI TS 119 412-6`_].


The following is a non-normative example of a PID Provider's end-entity certificate for legal persons (non-self-signed).

.. literalinclude:: ../../examples/pid-sign-seal.txt
  :language: text

Wallet Provider Sign/Seal Certificate
"""""""""""""""""""""""""""""""""""""

The specific requirements for Wallet Provider Sign/Seal Certificates are specified in Clause 5 of [`ETSI TS 119 412-6`_].

The following table defines the complete set of extensions applicable to the certificate profile. Extensions not listed in the table MUST NOT be present.

.. list-table:: Wallet Provider Sign/Seal Certificate Extensions
   :class: longtable
   :header-rows: 1
   :widths: 30 20 50

   * - **Extension**
     - **Presence**
     - **Notes**

   * - ``authorityKeyIdentifier``
     - REQUIRED
     - The value SHOULD be derived from the public key using the methods defined in :rfc:`5280#section-4.2.1.1`.

   * - ``subjectKeyIdentifier``
     - REQUIRED
     - The ``keyIdentifier`` field SHOULD be derived from the subject public key using the methods defined in :rfc:`5280#section-4.2.1.2`.

   * - ``keyUsage``
     - REQUIRED
     - It MUST contain one (and only one) of the key-usage settings *Type A*, *Type B*, *Type C*, or *Type F*.

   * - ``certificatePolicies``
     - REQUIRED
     - TBD.

   * - ``subjectAltName``
     - REQUIRED
     -

   * - ``cRLDistributionPoints``
     - CONDITIONAL
     - **REQUIRED IF:** the certificate does not include any access location of an OCSP responder or the validity assured extension as defined in `ETSI EN 319 412-1`_.

   * - ``authorityInfoAccess``
     - REQUIRED
     - It MUST include an ``AccessDescription`` structure with ``accessMethod`` set to ``1.3.6.1.5.5.7.48.2`` (``id-ad-caIssuers``) and ``accessLocation`` specifying at least one access location of a valid CA certificate of the issuing CA.
     
       If OCSP is supported by the issuing CA, the extension MUST include an ``AccessDescription`` structure with ``accessMethod`` set to ``1.3.6.1.5.5.7.48.1`` (``id-ad-ocsp``) and ``accessLocation`` specifying at least one OCSP responder authoritative to provide certificate status information for the certificate, as described in :ref:`infrastructure-trust:Online Certificate Status Protocol (OCSP)`.

   * - ``qcStatements``
     - REQUIRED
     - It MUST contain a ``QCStatement`` structure with ``statementId`` set to ``0.4.0.1862.1.6`` (``id-etsi-qcs-QcType``). The corresponding ``statementInfo`` MUST contain a ``QcType`` structure including exactly one object identifier, namely ``0.4.0.194126.1.2`` (``id-etsi-qct-wal``), as defined in Clause 5.2 of [`ETSI TS 119 412-6`_].


The following is a non-normative example of a Wallet Provider's end-entity certificate for legal persons (non-self-signed).

.. literalinclude:: ../../examples/wp-sign-seal.txt
  :language: text

(Q)EAA Provider Sign/Seal Certificate
"""""""""""""""""""""""""""""""""""""

The specific requirements for EAA Provider and QEAA Provider Sign/Seal Certificates are specified in Clauses 6 and 7 of [`ETSI TS 119 412-6`_], respectively.

The following table defines the complete set of extensions applicable to the certificate profile. Extensions not listed in the table MUST NOT be present.

The following table defines the complete set of extensions applicable to the certificate profile. Extensions not listed in the table MUST NOT be present.

.. list-table:: (Q)EAA Provider Sign/Seal Certificate Extensions
   :class: longtable
   :header-rows: 1
   :widths: 30 20 50

   * - **Extension**
     - **Presence**
     - **Notes**

   * - ``authorityKeyIdentifier``
     - REQUIRED
     - The value SHOULD be derived from the public key using the methods defined in :rfc:`5280#section-4.2.1.1`.

   * - ``keyUsage``
     - REQUIRED
     - 

   * - ``certificatePolicies``
     - REQUIRED
     - TBD.

   * - ``subjectAltName``
     - REQUIRED
     -

   * - ``cRLDistributionPoints``
     - CONDITIONAL
     - **REQUIRED IF:** the certificate does not include any access location of an OCSP responder or the validity assured extension as defined in `ETSI EN 319 412-1`_.

   * - ``authorityInfoAccess``
     - REQUIRED (only for QEAA)
     - It MUST include an ``AccessDescription`` structure with ``accessMethod`` set to ``1.3.6.1.5.5.7.48.2`` (``id-ad-caIssuers``) and ``accessLocation`` specifying at least one access location of a valid CA certificate of the issuing CA.
     
       If OCSP is supported by the issuing CA, the extension MUST include an ``AccessDescription`` structure with ``accessMethod`` set to ``1.3.6.1.5.5.7.48.1`` (``id-ad-ocsp``) and ``accessLocation`` specifying at least one OCSP responder authoritative to provide certificate status information for the certificate, as described in :ref:`infrastructure-trust:Online Certificate Status Protocol (OCSP)`.

   * - ``qcStatements``
     - REQUIRED
     - TBD.


For both QEAA and EAA Providers, if they manage the lifecycle of the Digital Credentials they issue and they use signed revocation lists such as Token Status List, they MUST use the same Sign/Seal Certificate to sign/seal the revocation list.

The following is a non-normative example of a QEAA Provider's end-entity certificate for legal persons (non-self-signed).

.. literalinclude:: ../../examples/qeaa-sign-seal.txt
  :language: text

PuB-EAA Provider Sign/Seal Certificate
""""""""""""""""""""""""""""""""""""""

The specific requirements for PuB-EAA Provider Sign/Seal Certificates are specified in Clause 8 of [`ETSI TS 119 412-6`_].

The following table defines the complete set of extensions applicable to the certificate profile. Extensions not listed in the table MUST NOT be present.

.. list-table:: PuB-EAA Provider Sign/Seal Certificate Extensions
   :class: longtable
   :header-rows: 1
   :widths: 30 20 50

   * - **Extension**
     - **Presence**
     - **Notes**

   * - ``authorityKeyIdentifier``
     - REQUIRED
     - The value SHOULD be derived from the public key using the methods defined in :rfc:`5280#section-4.2.1.1`.

   * - ``keyUsage``
     - REQUIRED
     - 

   * - ``certificatePolicies``
     - REQUIRED
     - It MUST include a ``PolicyInformation`` structure with ``policyIdentifier`` set to ``0.4.0.2042.1.2`` (*NCP+*).

   * - ``subjectAltName``
     - REQUIRED
     -

   * - ``cRLDistributionPoints``
     - CONDITIONAL
     - **REQUIRED IF:** the certificate does not include any access location of an OCSP responder or the validity assured extension as defined in `ETSI EN 319 412-1`_.

   * - ``authorityInfoAccess``
     - REQUIRED
     - It MUST include an ``AccessDescription`` structure with ``accessMethod`` set to ``1.3.6.1.5.5.7.48.2`` (``id-ad-caIssuers``) and ``accessLocation`` specifying at least one access location of a valid CA certificate of the issuing CA.
     
       If OCSP is supported by the issuing CA, the extension MUST include an ``AccessDescription`` structure with ``accessMethod`` set to ``1.3.6.1.5.5.7.48.1`` (``id-ad-ocsp``) and ``accessLocation`` specifying at least one OCSP responder authoritative to provide certificate status information for the certificate, as described in :ref:`infrastructure-trust:Online Certificate Status Protocol (OCSP)`.

   * - ``qcStatements``
     - REQUIRED
     - It MUST contain a ``QCStatement`` structure with ``statementId`` set to the OID corresponding to ``id-etsi-qcs-QcPSB``. The corresponding ``statementInfo`` MUST contain a ``QcPSB`` structure including the fields defined in Clause 8.3 of [`ETSI TS 119 412-6`_].

The following is a non-normative example of a PuB-EAA Provider's end-entity certificate for legal persons (non-self-signed).

.. literalinclude:: ../../examples/pubeaa-sign-seal.txt
  :language: text

Trust Anchor Certificate Profile
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section extends the general :ref:`infrastructure-trust:X.509 Certificate Profile` and specifies a **Certificate Profile** for **Trust Anchors**. These certificates MUST be notified to the European Commission as described in `CIR2024/2980`_ and subsequently included in the appropriate LoTE.

A Trust Anchor is a trusted public key (and associated data) used as an input to the :ref:`trust-evaluation-eudiw:X509 Certificate Chain Validation Algorithm`. In this profile, the Trust Anchor MUST be represented and distributed as an **X.509 certificate**. When published through List of Trusted Entities, that certificate is referenced from the corresponding service entry through the ``serviceDigitalIdentity`` component.

.. note::

  A Trust Anchor certificate may be *self-signed* or *non-self-signed*. In both cases it is treated as a Trust Anchor when found in a LoTE as required by the EUDIW Trust Framework.

Relying Parties, Credential Issuers and Wallet Units validate a presented Access, Registration or Sign/Seal Certificate by building a certification path that MUST end with a certificate signed by the subject of a Trust Anchor certificate. The Trust Anchor certificate is used as the trust termination point for the path validation process (i.e., it is the value of the ``trust_anchor`` variable in :ref:`trust-evaluation-eudiw:X509 Certificate Chain Validation Algorithm`). Implementations MUST support validating both self-signed and non-self-signed Trust Anchor certificates.

The following table defines the profile-specific requirements for the certificate fields. Fields not listed in the table remain subject to the requirements defined in the common :ref:`infrastructure-trust:X.509 Certificate Profile`.

.. list-table:: Trust Anchor Certificate Fields
   :class: longtable
   :header-rows: 1
   :widths: 30 70

   * - **Field**
     - **Additional Requirements**

   * - ``issuer``
     - If the certificate is self-signed, the issuer DN MUST be identical to the subject DN. Otherwise, the issuer DN MUST identify the entity that signed and issued the certificate and MAY differ from the subject DN.

   * - ``subject``
     - The subject DN MUST identify the entity associated with the trust anchor public key in a clear and unambiguous manner. If the Trust Anchor represents a legal or organizational entity, the subject DN MUST contain an ``organizationName`` attribute identifying that entity.


.. list-table:: Trust Anchor Certificate Extensions
   :class: longtable
   :header-rows: 1
   :widths: 30 20 50

   * - **Extension**
     - **Presence**
     - **Notes**

   * - ``authorityKeyIdentifier``
     - CONDITIONAL
     - **REQUIRED IF:** the certificate is not self-signed, to facilitate chain building towards the LoTE Trust Anchor. For self-signed certificates, it is RECOMMENDED. If present, the value SHOULD be derived from the public key using the methods defined in :rfc:`5280#section-4.2.1.1`.

   * - ``subjectKeyIdentifier``
     - REQUIRED
     - Provides a key identifier for the Trust Anchor public key, enabling reliable chain building and LoTE matching. The ``keyIdentifier`` field SHOULD be derived from the subject public key using the methods defined in :rfc:`5280#section-4.2.1.2`.

   * - ``keyUsage``
     - REQUIRED
     - It MUST assert the ``keyCertSign`` bit. It MAY assert the ``cRLSign`` bit if the Trust Anchor certificate is used by the CA to sign CRLs. It SHOULD be limited to usages consistent with the CA role of the Trust Anchor certificate.

   * - ``certificatePolicies``
     - OPTIONAL
     - It MAY be used to signal policy OIDs relevant to the issuing CA's practices.

   * - ``basicConstraints``
     - REQUIRED
     - The ``cA`` field MUST be set to ``TRUE``, signalling CA capability for X.509 path validation. The ``pathLenConstraint`` MAY be present; in that case, it MUST limit the number of non-self-issued intermediate CA certificates below this Trust Anchor. It is RECOMMENDED to set ``pathLenConstraint`` to 0 to prevent subordinate CA layers, unless a documented operational need exists to support additional intermediate CA tiers.

   * - ``cRLDistributionPoints``
     - OPTIONAL
     - It MAY include CRL distribution point URIs when CRL-based revocation is used.

   * - ``authorityInfoAccess``
     - CONDITIONAL
     - **REQUIRED IF:** the certificate contains ``basicConstraints`` with ``pathLenConstraint`` > 0. If present, it MUST include an ``AccessDescription`` structure with ``accessMethod`` set to ``1.3.6.1.5.5.7.48.2`` (``id-ad-caIssuers``) and an ``accessLocation`` that MUST use the ``http://`` scheme and MUST NOT use the ``https://`` scheme.

   * - ``ext-etsi-valassured-ST-certs``
     - OPTIONAL
     - If present, it indicates that the certificate issuer ensures the validity of the certificate is assured at time of use of the corresponding private key.


.. note::
   **Trust Anchor revocation.**
    Trust Anchor certificates are not expected to be revoked as they are trusted by policy when published in a LoTE or Trusted List. As a result, revocation information (e.g., CRL or OCSP) is not required for Trust Anchor certificates and entities using Trust Anchor certificates retrived in a LoTE or Trusted List MAY avoid revocation checking for Trust Anchor certificates.

.. note::

   **Self-signed vs. non-self-signed trust anchors.**
   A LoTE / Trusted List-published trust anchor certificate MAY be self-signed (traditional root CA style) or non-self-signed but treated as a trust anchor by policy (a pinned intermediate CA certificate).
   Relying parties MUST NOT require an additional issuer chain above a LoTE-designated trust anchor, even if it is not self-signed, because the trust anchor is a trust-store input designated by policy.

The following table maps the various Certificates used in the ecosystem, the attested public key uses, and the location of the Trust Anchor.

.. list-table:: Certificate and Trust Anchor Matrix
   :header-rows: 1

   * - **Certificate**
     - **Attested Key Use**
     - **Trust Anchor location**
   * - PID Provider Sign/Seal Certificate
     - signing PID, siging PID Status List Token
     - PID Providers LoTE
   * - Wallet Provider Sign/Seal Certificate
     - signing WIA, KA, signing WIA/KA Status List Token
     - Wallet Providers LoTE
   * - EAA Provider Sign/Seal Certificate
     - signing EAA, signing EAA Status List Token
     - ``trustedAuthority`` attribute in the machine-readable Attestation Rulebook for the specific EAA
   * - QEAA Provider Sign/Seal Certificate
     - signing QEAA, signing QEAA Status List Token
     - eIDAS I Trusted List
   * - Pub-EAA Provider Sign/Seal Certificate
     - signing PuB-EAA, signing PuB-EAA Status List Token
     - Pub-EAA Providers LoTE
   * - Wallet-Relying Party WRPAC
     - signing Request Objects or ``readerAuth`` during Digital Credential Presentation for Relying Parties; signing Credential Issuer Metadata for Credential Issuers
     - Provider of WRPAC LoTE
   * - Wallet-Relying Party WRPRC
     - N/A
     - Provider of WRPRC LoTE

.. note::

  As described in Section 4.3.1 of [`EUDI-TS 12`_], the Trust Anchor of a EAA Sign/Seal Certificate is referenced in the ``trustedAuthority`` attribute of the machine-readable Attestation Rulebook for the specific EAA.

The following is a non-normative example of a trust anchor certificate in a pseudo-structure format.

.. literalinclude:: ../../examples/trust-anchor-cert.txt
  :language: text

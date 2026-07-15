.. include:: ../common/common_definitions.rst
.. include:: ../common/symbols.rst

X.509 Certificate Profile
-------------------------

This section defines a general **X.509 Certificate Profile**, which is further specialized for the following artifacts:

- :ref:`trust-artifact-common:Entity Sign/Seal Certificate Profile` (EUDIW and National Trust Framework);
- :ref:`trust-artifact-common:Trust Anchor Certificate Profile` (EUDIW and National Trust Framework);
- :ref:`trust-artifact-eudiw:Wallet-Relying Party Access Certificate (WRPAC) Profile` (EUDIW Trust Framework);
- :ref:`trust-artifact-eudiw:Registrar Sign/Seal Certificate Profile` (EUDIW Trust Framework).

The common profile establishes the syntax, semantics and encoding requirements for X.509 certificates based on :rfc:`5280` and ETSI EN 319 412. Each X.509 certificate profile defined by this specification MUST conform to the requirements of this section unless explicitly stated otherwise.

The final certificate is obtained by combining the certificate body (``version`` through ``subjectPublicKeyInfo``) with the certificate extensions required by the selected certificate profile. The resulting ASN.1 structure MUST be encoded using the Distinguished Encoding Rules (DER) as specified in :rfc:`5280`.

Common Basic Fields
^^^^^^^^^^^^^^^^^^^

The following table defines the common basic fields of an X.509 certificate.

.. list-table:: Certificate Profile Parameters
   :class: longtable
   :header-rows: 1
   :widths: 20 15 45 20

   * - **Parameter**
     - **Presence**
     - **Description**
     - **Defined in**

   * - ``version``
     - REQUIRED
     - Indicates the version of the encoded certificate. Certificates conforming to this specification MUST use X.509 version 3 (value ``2``).
     - :rfc:`5280#section-4.1.2.1`, Clause 4.2.1 of [`ETSI EN 319 412-2`_].

   * - ``serialNumber``
     - REQUIRED
     - Contains the unique identifier assigned by the issuing CA to the certificate.
     - :rfc:`5280#section-4.1.2.2`

   * - ``signature``
     - REQUIRED
     - Identifies the algorithm used by the CA to sign the certificate, which MUST be among those defined in :ref:`algorithms:Cryptographic Algorithms`. It consists of an ``AlgorithmIdentifier`` structure with the following available fields

       * ``signature.algorithm`` (REQUIRED): represents the OID of the signature algorithm used to sign the certificate.
       * ``signature.parameters`` (OPTIONAL): contains algorithm-specific parameters associated with the signature algorithm.

     - :rfc:`5280#section-4.1.2.3`, :rfc:`5280#section-4.1.1.2`, Clause 4.2.2 of [`ETSI EN 319 412-2`_].

   * - ``issuer``
     - REQUIRED
     - Identifies the entity that issued and signed the certificate.

       For natural persons, this field MUST contain:

       * ``countryName``: represents a country that is consistent with the legal jurisdiction under which certificates are issued;
       * choice of (``givenName`` and/or ``surname``) or ``pseudonym``; if the given name or surname of the issuer is known, the respective attribute MUST be present;
       * ``commonName``;
       * ``serialNumber``.

       For legal persons, this field MUST contain:

       * ``countryName``: represents the country in which the certificate issuer is established.
       * ``organizationName``: represents the full registered name of the certificate issuer.
       * ``commonName``: represents a name commonly used by the certificate issuer to represent itself.
       * ``organizationIdentifier`` (CONDITIONAL): represents an identifier of the certificate issuer. It MUST be present if an appropriate registration number exists and its value is different from the organization name.
     - :rfc:`5280#section-4.1.2.4`, Clause 4.2.3 of [`ETSI EN 319 412-2`_].

   * - ``validity``
     - REQUIRED
     - Specifies the period during which the CA warrants the validity of the certificate. It consists of a ``Validity`` structure with the following available fields:

       * ``validity.notBefore`` (REQUIRED): specifies the beginning of the certificate validity period. Dates through 2049 MUST be encoded using ``UTCTime``, while dates from 2050 onwards MUST be encoded using ``GeneralizedTime``.
       * ``validity.notAfter`` (REQUIRED): specifies the end of the certificate validity period. Dates through 2049 MUST be encoded using ``UTCTime``, while dates from 2050 onwards MUST be encoded using ``GeneralizedTime``.
     - :rfc:`5280#section-4.1.2.5`.

   * - ``subject``
     - REQUIRED
     - Identifies the entity associated with the public key contained in ``subjectPublicKeyInfo``. The size of ``organizationName``, ``organizationalUnitName`` and ``commonName`` MAY be longer than the limit as stated in :rfc:`5280`.

       For natural persons, this field MUST contain:

       * ``countryName``: represents the general context in which other attributes are to be understood.
       * choice of (``givenName`` and/or ``surname``) or ``pseudonym``;
       * ``commonName``: represents a name of the subject.
       * ``serialNumber`` (CONDITIONAL): represents a unique identifier of the subject. It MUST be present if the above attributes are not sufficient to ensure subject name uniqueness.

       When a natural person subject is associated with an organization, the attributes MAY also identify such organization using attributes like ``organizationName`` and ``organizationIdentifier``.

       For legal persons, this field MUST contain:

       * ``countryName``: represents the country in which the subject is established.
       * ``organizationName``: represents the full registered name of the subject.
       * ``commonName``: represents a name commonly used by the subject to represent itself.
       * ``organizationIdentifier``: represents an identifier of the subject, different from the organization name.
     - :rfc:`5280#section-4.1.2.6`, Clause 4.2.4 of [`ETSI EN 319 412-2`_], Clause 4.2.1 of [`ETSI EN 319 412-3`_].

   * - ``subjectPublicKeyInfo``
     - REQUIRED
     - Contains the public key of the certificate subject and identifies the algorithm associated with that key. It consists of an ``SubjectPublicKeyInfo`` structure with the following available fields:

       * ``algorithm`` (REQUIRED): identifies the algorithm associated with the the public key of the certificate subject, which MUST be among those defined in :ref:`algorithms:Cryptographic Algorithms`. It consists of an ``AlgorithmIdentifier`` structure.
       * ``subjectPublicKey`` (REQUIRED): the public key of the certificate subject.
     - :rfc:`5280#section-4.1.2.7`, Clause 4.2.5 of [`ETSI EN 319 412-2`_].

   * - ``extensions``
     - REQUIRED
     - Contains one or more certificate extensions.
     - :rfc:`5280#section-4.1.2.9`, Clause 4.3 of [`ETSI EN 319 412-2`_].

Common Extensions
^^^^^^^^^^^^^^^^^

The ``extensions`` field is encoded as a sequence of one or more ASN.1 ``Extension`` structures:

.. list-table:: Extension Profile Parameters
   :class: longtable
   :header-rows: 1
   :widths: 20 15 45 20

   * - **Parameter**
     - **Presence**
     - **Description**
     - **Defined in**

   * - ``extnID``
     - REQUIRED
     - Represents the OID identifying the extension type.
     - :rfc:`5280#section-4.1.2.9`.

   * - ``critical``
     - OPTIONAL
     - Indicates whether the extension is critical. If omitted, the default value is ``FALSE``.
     - :rfc:`5280#section-4.1.2.9`.

   * - ``extnValue``
     - REQUIRED
     - Contains the DER encoding of the ASN.1 value corresponding to the extension type identified by ``extnID``.
     - :rfc:`5280#section-4.1.2.9`.

The following table defines the semantics and baseline requirements of the certificate extensions applicable to the X.509 certificate profiles defined in this specification. Specific certificate profiles MAY further constrain or extend these requirements.

The criticality values used in this specification have the following meaning:

- **C**: the extension MUST be marked critical;
- **NC**: the extension MUST be marked non-critical.

.. list-table:: Certificate Extensions Profile Parameters
   :class: longtable
   :header-rows: 1
   :widths: 20 12 12 8 33 15

   * - **Parameter**
     - **Presence**
     - **Criticality**
     - **OID**
     - **Description**
     - **Defined in**

   * - ``authorityKeyIdentifier``
     - REQUIRED
     - NC
     - ``2.5.29.35``
     - Identifies the public key corresponding to the issuing CA. It contains the ``keyIdentifier`` identifying the public key, while the ``authorityCertIssuer`` and ``authorityCertSerialNumber`` fields MAY be present but are not required.
     - :rfc:`5280#section-4.2.1.1`, Clause 4.3.1 of [`ETSI EN 319 412-2`_].

   * - ``subjectKeyIdentifier``
     - REQUIRED
     - NC
     - ``2.5.29.14``
     - Contains a key identifier that uniquely identifies the subject's public key.
     - :rfc:`5280#section-4.2.1.2`.

   * - ``keyUsage``
     - REQUIRED
     - C
     - ``2.5.29.15``
     - Specifies the purposes for which the certified public key may be used. The extension consists of a bit string in which each asserted bit indicates that the corresponding key usage is permitted:

       * 0 (``digitalSignature``): the subject public key is used to verify digital signatures (except on certificates and CRLs).
       * 1 (``nonRepudiation``): the subject public key is used to verify digital signatures (except on certificates and CRLs) used to provide a non-repudiation service.
       * 2 (``keyEncipherment``): the subject public key is used for enciphering private or secret keys.
       * 3 (``dataEncipherment``): the subject public key is used for directly enciphering raw user data without the use of an intermediate symmetric cipher
       * 4 (``keyAgreement``): the subject public key is used for key agreement.
       * 5 (``keyCertSign``): the subject public key is used for verifying signatures on public key certificates.
       * 6 (``cRLSign``): the subject public key is used for verifying signatures on certificate revocation lists.
       * 7 (``encipherOnly``): the subject public key may be used only for enciphering data while performing key agreement; it is only considered when ``keyAgreement`` is asserted as well.
       * 8 (``decipherOnly``): the subject public key may be used only for deciphering data while performing key agreement; it is only considered when ``keyAgreement`` is asserted as well.

       Based on these key usage bits, [`ETSI EN 319 412-2`_] defines the following key usage settings:

       * Type A: ``nonRepudiation``.
       * Type B: ``nonRepudiation`` and ``digitalSignature``.
       * Type C: ``digitalSignature``.
       * Type D: ``digitalSignature`` and one among ``keyEncipherment`` and ``keyAgreement``.
       * Type E: ``keyEncipherment`` or ``keyAgreement``.
       * Type F: ``nonRepudiation``, ``digitalSignature``, and one among ``keyEncipherment`` and ``keyAgreement``.

       Type A, C, or E SHOULD be used to avoid mixed usage of keys.

       Certificates issued to natural persons and used to validate commitment to signed content (e.g., documents/agreements) MUST be limited to Types A, B, or F; Type A SHOULD be used.

       Certificates issued to legal persons and used to validate digital signatures over content MUST be limited to Types A, B, or F; Type A SHOULD be used.
     - :rfc:`5280#section-4.2.1.3`, Clause 4.3.2 of [`ETSI EN 319 412-2`_], Clause 4.3.1 of [`ETSI EN 319 412-3`_].

   * - ``certificatePolicies``
     - REQUIRED
     - NC
     - ``2.5.29.32``
     - Contains a sequence of certificate policies that reflect the practices and procedures undertaken by the CA. For each element, in the form of a ``PolicyInformation`` structure, the following fields are available:
     
       * ``policyIdentifier`` (REQUIRED): represents the OID identifying the certificate policy applicable to the certificate.
       * ``policyQualifiers`` (OPTIONAL): contains a sequence of policy qualifier information associated with the certificate policy. The supported policy qualifiers are defined by the applicable certificate profile.
     - :rfc:`5280#section-4.2.1.4`, Clause 4.3.3 of [`ETSI EN 319 412-2`_].

   * - ``subjectAltName``
     - REQUIRED
     - NC
     - ``2.5.29.17``
     - Contains a sequence alternative names and contact information associated with the subject of the certificate. For each element, in the form of a ``GeneralName`` structure, the following fields are available:
     
       * ``otherName`` (OPTIONAL): contains an alternative name of a type identified by an OID.
       * ``rfc822Name`` (OPTIONAL): contains an email address.
       * ``dNSName`` (OPTIONAL): contains a domain name.
       * ``x400Address`` (OPTIONAL): contains an X.400 address.
       * ``directoryName`` (OPTIONAL): contains a distinguished name.
       * ``ediPartyName`` (OPTIONAL): contains an EDI party name.
       * ``uniformResourceIdentifier`` (OPTIONAL): contains a URI.
       * ``iPAddress`` (OPTIONAL): contains an IP address.
       * ``registeredID`` (OPTIONAL): contains an object identifier.

       This extension MUST contain at least one access description providing one of the following contact methods:

       * A URI where the WRP can be contacted for helpdesk or support matters, to be included in the ``uniformResourceIdentifier`` field.
       * A telephone number for WRP registration or usage matters, to be included in the ``otherName`` field, with ``2.5.4.20`` (``id-at-telephoneNumber``) as ``type-id`` and the telephone number as ``value``.
       * An email address for WRP registration or usage matters, to be included in the ``rfc822Name`` field.
     - :rfc:`5280#section-4.2.1.6`, Clause 4.3.5 of [`ETSI EN 319 412-2`_], Clause 6.6.1 of [`ETSI TS 119 411-8`_].

   * - ``basicConstraints``
     - CONDITIONAL
     - C
     - ``2.5.29.19``
     - Identifies whether the subject of the certificate is a CA and the maximum depth of valid certification paths that include this certificate. It consists of a ``BasicConstraints`` structure with the following available fields

       * ``cA``: indicates whether the certified public key may be used to verify certificate signatures. If this field or the whole extension is omitted, the default value is ``FALSE``.
       * ``pathLenConstraint``: represents the maximum number of non-self-issued intermediate certificates that may follow this certificate in a valid certification path. It is meaningful only if ``cA`` is asserted and ``keyUsage`` asserts the ``keyCertSign`` bit.

       **REQUIRED IF:** the certificate is a CA certificate. In this case, the ``cA`` field MUST be set to ``TRUE``.
     - :rfc:`5280#section-4.2.1.9`.

   * - ``cRLDistributionPoints``
     - CONDITIONAL
     - NC
     - ``2.5.29.31``
     - Contains a sequence of references to Certificate Revocation List (CRL) distribution points. For each element, in the form of a ``DistributionPoint`` structure, the following fields are available:

       * ``distributionPoint`` (OPTIONAL): Identifies the location of the CRL. It may contain either

         * ``fullName``: a sequence of ``GeneralName`` elements identifying the CRL distribution point; or
         * ``nameRelativeToCRLIssuer``: a relative distinguished name identifying the CRL distribution point.

       * ``reasons`` (OPTIONAL): indicates the reasons for which the CRL is issued.
       * ``cRLIssuer`` (OPTIONAL): identifies the entity that issues the CRL when it is different from the certificate issuer.
       
       **REQUIRED IF:** the certificate does not include any access location of an Online Certificate Status Protocol (OCSP) responder or the validity assured extension.
     - :rfc:`5280#section-4.2.1.13`, Clause 4.3.11 of [`ETSI EN 319 412-2`_].

   * - ``authorityInfoAccess``
     - REQUIRED
     - NC
     - ``1.3.6.1.5.5.7.1.1``
     - Contains a sequence of ``AccessDescription`` structures, each containing the following fields:

       * ``accessMethod`` (REQUIRED): contains an OID identifying the type of access information.
       * ``accessLocation`` (REQUIRED): contains the location of the access information, encoded as a ``GeneralName``.

       The extension MUST include an ``AccessDescription`` structure with ``accessMethod`` set to ``1.3.6.1.5.5.7.48.2`` (``id-ad-caIssuers``). The corresponding ``accessLocation`` MUST specify at least one access location of a valid CA certificate of the issuing CA.

       If OCSP is supported by the issuing CA, the extension MUST include an ``AccessDescription`` structure with ``accessMethod`` set to ``1.3.6.1.5.5.7.48.1`` (``id-ad-ocsp``), and the corresponding ``accessLocation`` MUST specify at least one OCSP responder authoritative to provide certificate status information for the certificate.
     
       It MUST include an ``AccessDescription`` term with ``1.3.6.1.5.5.7.48.2`` (``id-ad-caIssuers``) as ``accessMethod`` and ``accessLocation`` specifying at least one access location of a valid CA certificate of the issuing CA.

       If OCSP is supported, it MUST include an ``AccessDescription`` term with ``1.3.6.1.5.5.7.48.1`` (``id-ad-ocsp``) as ``accessMethod`` and ``accessLocation`` specifying at least one access location of an OCSP responder providing status information for the present certificate.

       If the certificate does not include any CRL distribution point and does not include the validity assured extension, a reference to at least one OCSP responder MUST be present.
     - :rfc:`5280#section-4.2.2.1`, Clause 4.4.1 of [`ETSI EN 319 412-2`_].
   
   * - ``ext-etsi-valassured-ST-certs``
     - CONDITIONAL
     - NC
     - ``0.4.0.194121.2.1``
     - Indicates that the validity of the certificate is assured because the certificate is a short-term certificate. Upon presence of such statement, the WRP can decide not to check the certificate revocation status (e.g., when validating a digital signature).

       **REQUIRED IF:** certificates are short-term and cannot be revoked.
     - Clause 5.2.2 of [`ETSI EN 319 412-1`_].

   * - ``noRevAvail``
     - CONDITIONAL
     - NC
     - ``2.5.29.56``
     - Allows a CA to indicate that no revocation information will be made available for this certificate.

       **REQUIRED IF:** the certificate includes the validity assured extension, but it does not contain neither a CRL distribution point nor the access location of an OCSP responder.
     - :rfc:`9608#section-2`.

   * - ``qcStatements``
     - CONDITIONAL
     - NC
     - ``1.3.6.1.5.5.7.1.3``
     - Contains a sequence of statements defining explicit properties of the certificate. For each element, in the form of a ``QCStatement`` structure, the following fields are available:

       * ``statementId`` (REQUIRED): contains the OID identifying the type of qualified certificate statement.
       * ``statementInfo`` (OPTIONAL): contains additional information associated with the qualified certificate statement. Its presence and encoding depend on the value of ``statementId``.

       The specific certificate profiles defined in this specification specify the ``QCStatement`` structures that MUST be present, including the required ``statementId`` values and the associated ``statementInfo`` contents, where applicable.

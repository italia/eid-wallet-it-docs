.. include:: ../common/common_definitions.rst
.. include:: ../common/symbols.rst



Infrastructure of Trust
=======================

The IT-Wallet ecosystem operates within a federated trust infrastructure where participating entities establish cryptographic trust relationships and maintain compliance with common security standards. This infrastructure provides the foundation for secure Digital Credential operations across the ecosystem participants.

This section provides first an overview of the entities and processes involved in the trust infrastructure (:ref:`infrastructure-trust:Overview`). Then, it defines the essential trust artifacts (:ref:`infrastructure-trust:EUDIW Trust Artifacts` and :ref:`infrastructure-trust:OID FED Trust Artifacts`). Finally, it describes the related lifecycle (:ref:`infrastructure-trust:Trust Management and Lifecycle`).

.. warning::
    DA CAPIRE: parliamo ancora di IT-Wallet ecosystem?
   
    TODO: add ref `CIR2025/848`_, `CIR2025/848-Amendment`_, `TS05`_, `ETSITS119411-8`_, `ETSITS119475`_

Overview
--------

The IT-Wallet ecosystem operates on a federated trust infrastructure, requiring participating entities to establish mutual trust before engaging in any interactions involving User attribute.
To be able to perform a trust evaluation process, entities first needs to onboard in the ecosystem (see :ref:`onboarding-procedure:Onboarding Procedure`). 
During this phase, the entity performing the onboarding specifies whether it requires to be interoperable with European entities or it operates only in the national boundary. 
This choice will affect both the onboarding and the trust evaluation procedures. If only the national boundary is requested, the infrastructure of trust complies with OpenID Federation 1.0 (`OID-FED`_). Otherwise, the EUDI Wallet (EUDIW) trust infrastructure defined in `ARF`_ is necessary.

.. note::
    As the Wallet cannot know in advance whether it will be used to interact with national or European services, both `OID-FED`_ and EUDIW trust mechanisms MUST be supported.
    Credential Issuers and Relying Parties can instead decide based on their business logic.


In both cases, the onboarding and, eventually, European notification processes result in the release or update of different trust artifacts (detailed in sections :ref:`infrastructure-trust:EUDIW Trust Artifacts` and :ref:`infrastructure-trust:OID FED Trust Artifacts`), then used during the trust evalution processes (detailed in section :ref:`trust-evaluation:Trust Evaluation`).

.. warning::
    TODO: fare figura con entities e cosa gestiscono? Registrar / Federation Auhtority / WRPAC Provider... 

    A Registrar is the designated body that:

    - Manages the WRP registration lifecycle (onboarding, update, suspension, cancellation),
    - Ensures the integrity and publication of registration information,
    - Ensures interoperability by exposing WRP registration data via a national website and a single common REST API.

.. warning::
    TODO: fare figura con i vari livelli dell pki per la distribuzione dei certificati come doc di Francesco.

.. include:: trust-artifact-eudiw.rst
.. include:: trust-artifact-oidfed.rst

Trust Management and Lifecycle
------------------------------

.. warning::
  TODO: concordare struttura e contenuto
 
State Machine for Entities
^^^^^^^^^^^^^^^^^^^^^^^^^^

EUDIW Trust Management Process
""""""""""""""""""""""""""""""

OID FED Trust Management Process
""""""""""""""""""""""""""""""""

Revocation Mechanisms
^^^^^^^^^^^^^^^^^^^^^

This section describes the artifacts that are employed in :ref:`infrastructure-trust:Trust Management and Lifecycle` to manage the status of certificates and entities by detailing respective formats and parameters. The main distinction is the following:

- To manage Wallet-Relying Party Access Certificates and Sign/Seal Certificates, the entities acting as Trust Anchors for these certificates MUST:
    - make available at least one revocation mechanism among :ref:`infrastructure-trust:Certificate Revocation List (CRL)` and :ref:`infrastructure-trust:Online Certificate Status Protocol (OCSP)`;
    - issue WRPACs and Sign/Seal Certificates with at least an extension corresponding to the provided revocation mechanism.
- To manage Wallet-Relying Party Registration Certificates, each Provider of Wallet Relying Party Registration Certificates MUST:
    - make available an endpoint to request :ref:`infrastructure-trust:Status List Token (SLT)`;
    - issue WRPRCs with the appropriate parameter ``status`` as described in :ref:`trust-artifact-eudiw:Wallet-Relying Party Registration Certificate (WRPRC)`.


Certificate Revocation List (CRL)
"""""""""""""""""""""""""""""""""

**Certificate Revocation Lists (CRLs)** are used to check the revocation status of an X509 certificate. A CRL is a digitally signed list of revoked certificates that have been issued by a CA. The CRL is published and made available to any entity via a publicly accessible URI. The CRL MUST be digitally signed by the **CRL issuer**.

CRLs MAY be used for the following types of certificates:

- Wallet Relying Party Access Certificates by including the ``cRLDistributionPoints`` extension in the certificate, as described in `:ref:trust-artifact-eudiw:Wallet-Relying Party Access Certificate`.
- Sign/Seal certificates by including the ``cRLDistributionPoints`` extension in the certificate, as described in `:ref:trust-artifact-eudiw:Sign/Seal Certificate`.

If a CRL is used to manage the status of the certificates, the CRL issuer MUST be the entity referenced in the Trust Anchor certificate ``subject`` field. 

The CRL issuer MAY also generate delta CRLs. A delta CRL only lists those certificates, within its scope, whose revocation status has changed since the issuance of a referenced complete CRL. The referenced complete CRL is referred to as a base CRL. The scope of a delta CRL MUST be the same as the base CRL that it references.

If supported by the CA, the CRL MUST be available at the URI specified in the ``cRLDistributionPoints.distributionPoint`` *[0] CHOICE* structure within the Wallet Relying Party Access Certificate (WRPAC).

An X.509 v2 CRL is represented as the ASN.1 DER encoding of the ``CertificateList`` SEQUENCE. The ASN.1 DER encoding is a strictly defined tag, length, and value encoding system for each element. The final bytes transmitted represent the DER encoding of the top-level SEQUENCE containing the fields in the following table:

.. list-table:: Top-Level CertificateList Structure
   :header-rows: 1

   * - Parameter
     - Defined in
     - Presence
     - Format
     - Description
   * - ``tbsCertList``
     - :rfc:`5280`, clause 5.1.1.1
     - REQUIRED
     - *SEQUENCE*
     - Contains the core CRL information including the name of the issuer, issue date, next update date, the optional list of revoked certificates, and optional CRL extensions.
   * - ``signatureAlgorithm``
     - :rfc:`5280`, clause 5.1.1.2
     - REQUIRED
     - *SEQUENCE*
     - Contains the algorithm identifier for the algorithm used by the CRL issuer to sign the ``CertificateList``. Selection SHOULD align with relevant standards (e.g., [ETSI TS 119 312]).
   * - ``signatureAlgorithm.algorithm``
     - [:rfc:`5280`, clause 4.1.1.2]
     - REQUIRED
     - *OBJECT IDENTIFIER*
     - The OID of the signature algorithm.
   * - ``signatureAlgorithm.parameters``
     - [:rfc:`5280`, clause 4.1.1.2]
     - OPTIONAL
     - *ANY*
     - Algorithm-specific parameters, dependent on the signature algorithm used.
   * - ``signatureValue``
     - [:rfc:`5280`, clause 5.1.1.3]
     - REQUIRED
     - *BIT STRING*
     - Contains the digital signature computed upon the ASN.1 DER encoded ``tbsCertList``.

Certificate List Content
.........................

The ``TBSCertList`` (To Be Signed Certificate List) is an ASN.1 SEQUENCE containing several fields and extensions. The following table lists all such fields and extensions that are required in a CRL or conditionally required.

.. list-table:: TBSCertList Fields and Extensions
   :header-rows: 1

   * - Parameter
     - Defined in
     - Presence
     - Format
     - Description
   * - ``version``
     - [:rfc:`5280`, clause 5.1.2.1]
     - OPTIONAL
     - *INTEGER*
     - Describes the version of the encoded CRL. When extensions are used (as is standard practice), this field MUST be present and MUST specify version 2 (the integer value is ``1``).
   * - ``signature``
     - [:rfc:`5280`, clause 5.1.2.2]
     - REQUIRED
     - *SEQUENCE*
     - The algorithm identifier for the algorithm used to sign the CRL.
   * - ``signature.algorithm``
     - [:rfc:`5280`, clause 4.1.1.2]
     - REQUIRED
     - *OBJECT IDENTIFIER*
     - The OID of the signature algorithm. MUST match the ``signatureAlgorithm`` field in the parent ``CertificateList`` sequence.
   * - ``signature.parameters``
     - [:rfc:`5280`, clause 4.1.1.2]
     - OPTIONAL
     - *ANY*
     - Algorithm-specific parameters, dependent on the algorithm used.
   * - ``issuer``
     - [:rfc:`5280`, clause 5.1.2.3]
     - REQUIRED
     - *Name*
     - Identifies the entity that has signed and issued the CRL. It MUST contain a non-empty X.500 distinguished name (DN) composed of ``AttributeType`` (OID) and ``AttributeValue`` sequences.
   * - ``thisUpdate``
     - [:rfc:`5280`, clause 5.1.2.4]
     - REQUIRED
     - *UTCTime* or *GeneralizedTime*
     - Indicates the issue date of this CRL. Dates through 2049 MUST use ``UTCTime``; dates in 2050 or later MUST use ``GeneralizedTime``.
   * - ``nextUpdate``
     - [:rfc:`5280`, clause 5.1.2.5]
     - REQUIRED
     - *UTCTime* or *GeneralizedTime*
     - Indicates the date by which the next CRL will be issued. Dates through 2049 MUST use ``UTCTime``; dates in 2050 or later MUST use ``GeneralizedTime``.
   * - ``revokedCertificates``
     - [:rfc:`5280`, clause 5.1.2.6]
     - OPTIONAL
     - *SEQUENCE OF*
     - A sequence of revoked certificates. When there are no revoked certificates, this field MUST be absent.
   * - ``revokedCertificates.userCertificate``
     - [:rfc:`5280`, clause 5.1.2.6]
     - REQUIRED
     - *INTEGER*
     - The ``CertificateSerialNumber`` of the revoked certificate.
   * - ``revokedCertificates.revocationDate``
     - [:rfc:`5280`, clause 5.1.2.6]
     - REQUIRED
     - *UTCTime* or *GeneralizedTime*
     - The date on which the revocation occurred.
   * - ``revokedCertificates.crlEntryExtensions``
     - [:rfc:`5280`, clause 5.1.2.6]
     - OPTIONAL
     - *SEQUENCE OF*
     - Extensions specific to this revoked certificate entry. If present, the CRL ``version`` MUST be ``v2``.
   * - ``crlExtensions``
     - [:rfc:`5280`, clause 5.1.2.7]
     - OPTIONAL
     - *[0] EXPLICIT SEQUENCE OF*
     - A sequence of one or more CRL extensions. If present, the CRL ``version`` MUST be ``v2``.

The ``crlExtensions`` field MAY contain various extensions. Notable standard extensions include:

.. list-table:: Notable crlExtensions
   :header-rows: 1

   * - Parameter
     - Defined in
     - Presence
     - Format
     - Description
   * - ``authorityKeyIdentifier``
     - [RFC 5280, clause 5.2.1]
     - REQUIRED
     - *SEQUENCE*
     - Provides a means of identifying the public key corresponding to the private key used to sign the CRL. Contains ``keyIdentifier`` (OCTET STRING), ``authorityCertIssuer``, or ``authorityCertSerialNumber``.
   * - ``cRLNumber``
     - [RFC 5280, clause 5.2.3]
     - REQUIRED
     - *INTEGER*
     - A non-critical extension conveying a monotonically increasing sequence number for a given CRL scope and issuer. Both base CRLs and delta CRLs share the same monotonically increasing sequence; the delta CRL's number MUST be greater than the base CRL's number it references.
   * - ``deltaCRLIndicator``
     - [RFC 5280, clause 5.2.4]
     - REQUIRED for delta CRLs; MUST NOT appear in base CRLs
     - *INTEGER* (``BaseCRLNumber``)
     - A **critical** extension that marks the CRL as a delta CRL and identifies the base CRL it is relative to. The integer value is the ``cRLNumber`` of the base CRL on which this delta is built. A relying party that does not understand this extension MUST reject the CRL. The base CRL MUST still be reachable (cached or retrievable) for the delta to be useful. If this extension is absent, the CRL is a full (base) CRL.
   * - ``freshestCRL`` (a.k.a. *CRL Distribution Points* on a CRL)
     - [RFC 5280, clause 5.2.6]
     - OPTIONAL; RECOMMENDED on base CRLs in deployments that issue delta CRLs
     - *SEQUENCE OF DistributionPointName*
     - A non-critical extension indicating where the most recently issued delta CRL for the same scope can be retrieved. Each ``DistributionPointName`` carries one or more URIs (typically ``uniformResourceIdentifier``). When present on a base CRL, it MUST point to the delta CRL distribution location; when present on a delta CRL, it points to the next delta CRL. A relying party uses this to discover deltas without additional out-of-band configuration.
   * - ``issuingDistributionPoint``
     - [RFC 5280, clause 5.2.5]
     - OPTIONAL; REQUIRED when the CRL scope is restricted (e.g., only-CA, only-end-entity, only-some-reasons) or when the CRL is indirect
     - *SEQUENCE* (``IssuingDistributionPoint``)
     - A **critical** extension describing the scope of the CRL. Contains flags ``distributionPoint``, ``onlyContainsUserCerts``, ``onlyContainsCACerts``, ``onlySomeReasons``, ``indirectCRL``, and ``onlyContainsAttributeCerts``. For delta-CRL deployments, the ``indirectCRL`` bit is set to TRUE when the delta is signed by a CRL issuer other than the CA that issued the certificates (common when a delegated revocation service is used), and ``onlySomeReasons`` MAY restrict the delta CRL to specific revocation reasons (e.g., ``keyCompromise`` only). The base CRL and corresponding delta CRLs MUST share the same scope (same ``onlyContains*`` flags and ``distributionPoint``).


Online Certificate Status Protocol (OCSP)
""""""""""""""""""""""""""""""""""""""""""""

The Online Certificate Status Protocol (OCSP) (:rfc:`6960`) enables applications to determine the exact revocation state of identified certificates. It provides more timely revocation information than is typically possible with CRLs and MAY also be used to obtain additional status information.

An OCSP client issues a status request to an OCSP responder and MUST suspend the acceptance of the certificates in question until the responder provides a valid response.

If supported by the Certificate Authority (CA), the URI to which the OCSP Responder can be invoked MUST be present in the ``authorityInfoAccess.accessLocation`` extension of the Wallet Relying Party Access Certificate (WRPAC).

This protocol specifies the data that MUST be exchanged between the OCSP client (which checks the status of one or more certificates) and the OCSP server (which provides the corresponding status). 

The following table sums up the roles of the OCSP client and server in the EUDIW ecosystem.

.. list-table:: tbsRequest Structure Parameters
   :header-rows: 1

   * - OCSP Client
     - OCSP Server
     - Use case
   * - Wallet Unit
     - WRPAC Provider
     - WRPAC Status Check
   * - Wallet Unit or Relying Party 
     - PID Provider Trust Anchor
     - PID Sign/Seal Certificate Status Check
   * - Wallet Unit or Relying Party 
     - PuB-EAA Provider Trust Anchor
     - PuB-EAA Sign/Seal Certificate Status Check
   * - Wallet Unit or Relying Party 
     - (Q)EAA Provider Trust Anchor
     - (Q)EAA Sign/Seal Certificate Status Check

.. note:: 
    The Status check on Sign/Seal Certificates is needed only in case the Sign/Seal Certificate is not referenced directly as a Trust Anchor Certificate, in which case it is trusted a priori and does not need a separate status check.

Online Certificate Status Protocol Request Format
....................................................

The OCSP request MUST be the ASN.1 DER encoding of the ``OCSPRequest`` SEQUENCE, which contains the ``tbsRequest`` (To-Be-Signed Request) and an optional signature. The following table lists the parameters found within the ``tbsRequest`` structure.

.. list-table:: tbsRequest Structure Parameters
   :header-rows: 1

   * - Parameter
     - Defined in
     - Presence
     - Format
     - Description
   * - ``version``
     - [:rfc:`6960`, clause 4.1.1]
     - OPTIONAL
     - *[0] EXPLICIT INTEGER*
     - Indicates the version of the protocol. If omitted, the default value is ``v1`` (0).
   * - ``requestList``
     - [:rfc:`6960`, clause 4.1.1]
     - REQUIRED
     - *SEQUENCE OF*
     - Contains one or more single certificate status requests.
   * - ``requestList.reqCert``
     - [:rfc:`6960`, clause 4.1.1]
     - REQUIRED
     - *SEQUENCE*
     - The ``CertID`` structure carrying the identifier of a target certificate.
   * - ``requestList.singleRequestExtensions``
     - [:rfc:`6960`, clause 4.1.1]
     - OPTIONAL
     - *[0] EXPLICIT SEQUENCE*
     - Includes extensions applicable to this single certificate status request.
   * - ``requestExtensions``
     - [:rfc:`6960`, clause 4.1.1]
     - OPTIONAL
     - *[2] EXPLICIT SEQUENCE*
     - Includes extensions applicable to the overall requests found within the ``requestList``.

The ``reqCert`` parameter utilizes the ``CertID`` structure, MUST be an ASN.1 *SEQUENCE* containing the following parameters:

.. list-table:: CertID Structure Parameters
   :header-rows: 1

   * - Parameter
     - Defined in
     - Presence
     - Format
     - Description
   * - ``hashAlgorithm``
     - [:rfc:`6960`, clause 4.1.1]
     - REQUIRED
     - *SEQUENCE*
     - Identifies the hash algorithm used to generate the issuer name and key hashes.
   * - ``hashAlgorithm.algorithm``
     - [:rfc:`6960`, clause 4.1.1]
     - REQUIRED
     - *OBJECT IDENTIFIER*
     - The OID of the hash function (e.g., SHA-256, depending on the profile).
   * - ``hashAlgorithm.parameters``
     - [:rfc:`6960`, clause 4.1.1]
     - OPTIONAL
     - *ANY*
     - Algorithm-specific parameters, dependent on the hash algorithm used.
   * - ``issuerNameHash``
     - [:rfc:`6960`, clause 4.1.1]
     - REQUIRED
     - *OCTET STRING*
     - The hash of the issuer's distinguished name (DN), calculated over the DER encoding of the issuer's name field.
   * - ``issuerKeyHash``
     - [:rfc:`6960`, clause 4.1.1]
     - REQUIRED
     - *OCTET STRING*
     - The hash of the issuer's public key, calculated over the value (excluding tag and length) of the subject public key field.
   * - ``serialNumber``
     - [:rfc:`6960`, clause 4.1.1]
     - REQUIRED
     - *INTEGER*
     - The serial number of the target certificate for which the status is being requested.

The ``requestExtensions`` and ``singleRequestExtensions`` structures MAY contain various extensions. The following table lists the requested ones:

.. list-table:: OCSP Nonce Extension
   :header-rows: 1

   * - Parameter
     - Defined in
     - Presence
     - Format
     - Description
   * - ``nonce``
     - [:rfc:`6960`, clause 4.4.1]
     - REQUIRED
     - *OCTET STRING*
     - Cryptographically fresh value used to bind a request and a response to prevent replay attacks. Identifier OID is ``id-pkix-ocsp-nonce``.

When sent over HTTP using POST, the body of this request MUST contain the raw DER encoding of this ``OCSPRequest``SEQUENCE and MUST have MIME type ``application/ocsp-request``.

Below is a non-normative example of an OCSP request:

.. literalinclude:: ../../examples/ocsp-request.txt
  :language: text

Online Certificate Status Protocol Response Format
...................................................

An OCSP response MUST be the ASN.1 DER encoding of the ``OCSPResponse`` *SEQUENCE*. When transported over HTTP, the body of the HTTP response MUST contain the raw DER encoding of this ``OCSPResponse``, with the MIME type ``application/ocsp-response``. The ``OCSPResponse`` *SEQUENCE* contains the following parameters:

.. list-table:: OCSPResponse Structure Parameters
   :header-rows: 1

   * - Parameter
     - Defined in
     - Presence
     - Format
     - Description
   * - ``responseStatus``
     - [:rfc:`6960`, clause 4.2.1]
     - REQUIRED
     - *ENUMERATED*
     - Indicates the processing status of the prior request. Supported values are: ``successful`` (0), ``malformedRequest`` (1), ``internalError`` (2), ``tryLater`` (3), ``sigRequired`` (5), and ``unauthorized`` (6).
   * - ``responseBytes``
     - [:rfc:`6960`, clause 4.2.1]
     - OPTIONAL
     - *[0] EXPLICIT SEQUENCE*
     - Present only when the ``responseStatus`` is ``successful`` (0). Contains the response type and the encoded response data.
   * - ``responseBytes.responseType``
     - [:rfc:`6960`, clause 4.2.1]
     - REQUIRED
     - *OBJECT IDENTIFIER*
     - Identifier for the response type. For a basic OCSP responder, this value MUST be ``id-pkix-ocsp-basic``.
   * - ``responseBytes.response``
     - [:rfc:`6960`, clause 4.2.1]
     - REQUIRED
     - *OCTET STRING*
     - Contains the DER encoding of the response syntax identified by ``responseType`` (e.g., the ``BasicOCSPResponse`` structure).

.. note::
   OCSP responders MUST be capable of producing responses of the ``id-pkix-ocsp-basic`` response type. Correspondingly, OCSP clients MUST be capable of receiving and processing responses of the ``id-pkix-ocsp-basic`` response type.

``BasicOCSPResponse`` is an ASN.1 SEQUENCE containing the following parameters:

.. list-table:: BasicOCSPResponse Structure Parameters
   :header-rows: 1

   * - Parameter
     - Defined in
     - Presence
     - Format
     - Description
   * - ``tbsResponseData``
     - [:rfc:`6960`, clause 4.2.1]
     - REQUIRED
     - *SEQUENCE*
     - Contains the core response data to be signed by the responder.
   * - ``tbsResponseData.version``
     - [:rfc:`6960`, clause 4.2.1]
     - OPTIONAL
     - *[0] EXPLICIT INTEGER*
     - The version of the response syntax. If omitted, the default value is ``v1`` (0).
   * - ``tbsResponseData.responderID``
     - [:rfc:`6960`, clause 4.2.1]
     - REQUIRED
     - *CHOICE*
     - Identifies the OCSP responder. It MUST contain either ``byName`` or ``byKey``.
   * - ``tbsResponseData.responderID.byName``
     - [:rfc:`6960`, clause 4.2.1]
     - OPTIONAL
     - *[1] EXPLICIT Name*
     - The ``Name`` from the responder’s certificate subject.
   * - ``tbsResponseData.responderID.byKey``
     - [:rfc:`6960`, clause 4.2.1]
     - OPTIONAL
     - *[2] EXPLICIT OCTET STRING*
     - The SHA-1 hash of the responder’s ``subjectPublicKey`` (excluding the tag and length fields).
   * - ``tbsResponseData.producedAt``
     - [:rfc:`6960`, clause 4.2.1]
     - REQUIRED
     - *GeneralizedTime*
     - The time at which the OCSP response was generated.
   * - ``tbsResponseData.responses``
     - [:rfc:`6960`, clause 4.2.1]
     - REQUIRED
     - *SEQUENCE OF*
     - A sequence of ``SingleResponse`` structures, providing the status of each requested certificate.
   * - ``tbsResponseData.responseExtensions``
     - [:rfc:`6960`, clause 4.2.1]
     - OPTIONAL
     - *[1] EXPLICIT SEQUENCE OF*
     - Contains extensions applicable to the overall OCSP response.
   * - ``signatureAlgorithm``
     - [:rfc:`5280`, clause 4.1.1.2]
     - REQUIRED
     - *SEQUENCE*
     - Identifies the cryptographic algorithm used to sign the response.
   * - ``signatureAlgorithm.algorithm``
     - [:rfc:`5280`, clause 4.1.1.2]
     - REQUIRED
     - *OBJECT IDENTIFIER*
     - The OID of the signature algorithm. Selection SHOULD align with relevant standards (e.g., [ETSI TS 119 312]).
   * - ``signatureAlgorithm.parameters``
     - [:rfc:`5280`, clause 4.1.1.2]
     - OPTIONAL
     - *ANY*
     - Algorithm-specific parameters, dependent on the OID defined in ``algorithm``.
   * - ``signature``
     - [:rfc:`6960`, clause 4.2.1]
     - REQUIRED
     - *BIT STRING*
     - The digital signature computed over the hash of the DER-encoded ``tbsResponseData``.
   * - ``certs``
     - [:rfc:`6960`, clause 4.2.1]
     - OPTIONAL
     - *[0] EXPLICIT SEQUENCE OF*
     - Certificate chain to help the client verify the responder's signature. If no certificates are included, this field SHOULD be absent.

The ``responseExtensions`` structure MAY contain various extensions. The following table lists the requested ones:

.. list-table:: Response Extensions Nonce
   :header-rows: 1

   * - Parameter
     - Defined in
     - Presence
     - Format
     - Description
   * - ``nonce``
     - [:rfc:`6960`, clause 4.4.1]
     - REQUIRED
     - *OCTET STRING*
     - Cryptographically fresh value used to bind a request and a response to prevent replay attacks. If included in the request, responders SHOULD include it in the response. Identifier OID is ``id-pkix-ocsp-nonce``.

In the OCSP Response there MUST be at least a ``SingleResponse`` for each ``CertID`` in the request. Each ``SingleResponse`` is an ASN.1 *SEQUENCE* that carries the following parameters:

.. list-table:: SingleResponse Structure Parameters
   :header-rows: 1

   * - Parameter
     - Defined in
     - Presence
     - Format
     - Description
   * - ``certID``
     - [:rfc:`6960`, clause 4.2.1]
     - REQUIRED
     - *SEQUENCE*
     - Identifier of the certificate whose status is determined in ``certStatus``.
   * - ``certStatus``
     - [:rfc:`6960`, clause 4.2.1]
     - REQUIRED
     - *CHOICE*
     - The value of the certificate's status. It MUST be exactly one of: ``good``, ``revoked``, or ``unknown``.
   * - ``certStatus.good``
     - [:rfc:`6960`, clause 4.2.1]
     - OPTIONAL
     - *[0] IMPLICIT NULL*
     - Indicates the certificate is valid.
   * - ``certStatus.revoked``
     - [:rfc:`6960`, clause 4.2.1]
     - OPTIONAL
     - *[1] IMPLICIT SEQUENCE*
     - Indicates the certificate has been revoked. Contains the ``RevokedInfo`` structure.
   * - ``certStatus.revoked.revocationTime``
     - [:rfc:`6960`, clause 4.2.1]
     - REQUIRED
     - *GeneralizedTime*
     - The time at which the certificate was revoked.
   * - ``certStatus.revoked.revocationReason``
     - [:rfc:`6960`, clause 4.2.1]
     - OPTIONAL
     - *[0] EXPLICIT ENUMERATED*
     - Contains the ``CRLReason`` indicating why the certificate was revoked.
   * - ``certStatus.unknown``
     - [:rfc:`6960`, clause 4.2.1]
     - OPTIONAL
     - *[2] IMPLICIT NULL*
     - Indicates the responder does not know the status of the certificate.
   * - ``thisUpdate``
     - [:rfc:`6960`, clause 4.2.1]
     - REQUIRED
     - *GeneralizedTime*
     - Indicates the issue date and time of this OCSP Response.
   * - ``nextUpdate``
     - [:rfc:`6960`, clause 4.2.1]
     - OPTIONAL
     - *[0] EXPLICIT GeneralizedTime*
     - Indicates the date and time by which the next update to the OCSP Responder database will be in place.
   * - ``singleExtensions``
     - [:rfc:`6960`, clause 4.2.1]
     - OPTIONAL
     - *[1] EXPLICIT SEQUENCE*
     - Includes extensions applicable to this single certificate status response.

Below is a non-normative example of an OCSP response with a single ``good`` status.


.. literalinclude:: ../../examples/ocsp-response.txt
  :language: text

Token Status List (TSL)
""""""""""""""""""""""""

This section defines a Status List data structure, which is used to convey information regarding the individual statuses of multiple WRPRCs. A Status List describes the status of the WRPRCs by encoding their validity in a bit array. Each WRPRC is allocated an index during issuance; this index represents its position within the bit array. The value of the bit(s) at this index corresponds to the WRPRC's status. A Status List is provided within a cryptographically signed Status List Token in JWT format. The format, request and response structures are found in :ref:`credential-revocation:Token Status Lists`.

In this specification, the roles of the Provider of WRPRC and Status Issuer (i.e., the entity that issues the Status List Token about the status information of the WRPRC) MUST coincide. Moreover, the Status Provider (i.e., the entity that provides the Status List Token on a public endpoint) MUST be the Provider of WRPRC itself.

The Provider of WRPRC MUST use the following values for the possible statuses of the issued WRPRCs:

- `0x00` - `VALID` - The WRPRC is valid.
- `0x01` - `INVALID` - The WRPRC is revoked.
- `0x02` - `SUSPENDED` - The WRPRC is suspended.


Once the <components:Wallet Unit> receives a WRPRC, it can request the Status List to validate its status through the provided URI parameter and look up the corresponding index in the list.

Status List Token (SLT)
........................

The **Status List Token** is available at the Status List Endpoint. It is formatted as a JSON Web Token (JWT) signed by the Provider of WRPRC and contains the parameters described in :ref:`credential-revocation:Status List Token`. The only difference is the ``status_list`` claim, which is a JSON object containing the following parameters:

.. _table_status_list_structure:
.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Parameter**
    - **Description**
    - **Reference**
  * - **bits**
    - REQUIRED. JSON Integer specifying the number of bits per WRPRC in the compressed byte array (`lst`). The allowed values for bits are 1,2,4 and 8.
    - `TOKEN-STATUS-LIST`_
  * - **lst**
    - REQUIRED. JSON String that contains the status values for all the WRPRCs it conveys statuses for. The value MUST be the base64url-encoded compressed byte array.
    - `TOKEN-STATUS-LIST`_
  * - **aggregation_uri**
    - OPTIONAL. JSON String that contains a URI to retrieve the Status List Aggregation for this type of WRPRC or Issuer.
    - `TOKEN-STATUS-LIST`_



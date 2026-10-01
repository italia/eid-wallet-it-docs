.. include:: ../common/common_definitions.rst
.. Included via digital-credential-management.rst at title level '=' (document title).


QEAA and PuB-EAA Data Model
===========================

This section profiles a Qualified Electronic Attestation of Attributes (QEAA) and an Electronic Attestation of Attributes issued by or on behalf of a public body responsible for an authentic source (PuB-EAA).

It applies when the Credential Catalog entry has ``legal_type`` set to ``qeaa`` or ``pub-eaa``.
The generic rules in :ref:`credential-data-model:Digital Credential Data Model` apply.
This section adds the rules of [`ETSI TS 119 472-1`_] for those two legal classifications.

A QEAA or a PuB-EAA MUST be encoded as SD-JWT VC, the realization in clause 5 of [`ETSI TS 119 472-1`_], or as mdoc-CBOR, the realization in clause 6 of [`ETSI TS 119 472-1`_].
The JSON-LD W3C VC realization in clause 7 of [`ETSI TS 119 472-1`_] and the X.509 attribute certificate realization in clause 8 of [`ETSI TS 119 472-1`_] are outside this specification.

Issuance of these attestations follows [`ETSI TS 119 472-3`_].
Presentation of these attestations follows [`ETSI TS 119 472-2`_].
Provider registration and trust anchors remain those specified for a QEAA Provider and a PuB-EAA Provider in :ref:`onboarding-system:QEAA Provider` and :ref:`onboarding-system:PuB-EAA Provider`.

Scope
-----

User attributes of a QEAA or a PuB-EAA depend on the credential type registered in the Credential Catalog.
This section specifies the metadata that [`ETSI TS 119 472-1`_] requires for every such type.

Annex V of [`EU_2024_1183`_] sets the content of a QEAA.
Annex VII of [`EU_2024_1183`_] sets the content of a PuB-EAA.
Where those annexes require an issuer name, a country, a validity period, or the location of the signing certificate, the encoding is the one in this section.

Category
--------

The ``category`` value identifies the legal classification inside the attestation.

.. _table_qeaa_pub_eaa_category:
.. list-table::
    :class: longtable
    :widths: 20 40 40
    :header-rows: 1

    * - **legal_type**
      - **SD-JWT VC claim ``category``**
      - **mdoc element ``category``**
    * - ``qeaa``
      - REQUIRED. The value MUST be ``urn:etsi:esi:eaa:eu:qualified``.
      - REQUIRED. The value MUST be ``urn:etsi:esi:eaa:eu:qualified``.
    * - ``pub-eaa``
      - REQUIRED. The value MUST be ``urn:etsi:esi:eaa:eu:pub``.
      - REQUIRED. The value MUST be ``urn:etsi:esi:eaa:eu:pub``.

The claim and the element implement [`ETSI TS 119 472-1`_] QEAA-5.2.2.2-02, PuB-EAA-5.2.2.3-02, QEAA-6.2.2.2-02 and PuB-EAA-6.2.2.3-02.
In mdoc the element ``category`` MUST be placed in the namespace ``org.etsi.01947201.010101``.
An attestation whose ``legal_type`` is ``eaa`` MUST NOT contain ``category`` ([`ETSI TS 119 472-1`_] EAA-5.2.2.1-01 and EAA-6.2.2.1-01).

Issuer Identification
---------------------

The signer certificate MUST be a qualified certificate.
A QEAA uses the profile in :ref:`infrastructure-trust:(Q)EAA Provider Sign/Seal Certificate`.
A PuB-EAA uses the profile in :ref:`infrastructure-trust:PuB-EAA Provider Sign/Seal Certificate`.
The signature MUST be a qualified electronic signature or a qualified electronic seal ([`ETSI TS 119 472-1`_] QEAA-5.6.2-01, PuB-EAA-5.6.3-01, QEAA-6.6.2-01 and PuB-EAA-6.6.3-01).

The registration identifier in that certificate MUST follow clause 5.1.4 of [`ETSI EN 319 412-1`_] ([`ETSI TS 119 472-1`_] QEAA-5.2.4.2-04, PuB-EAA-5.2.4.3-04, QEAA-6.2.4.2-02 and PuB-EAA-6.2.4.3-02).
The claims ``issuing_authority`` and ``issuing_country`` remain those specified in :ref:`credential-data-model:Digital Credential SD-JWT Metadata Attributes` and in [`EU_2024/2977`_].
The value of ``issuing_authority`` MUST be equal to the issuer name in the qualified certificate.
The value of ``issuing_country`` MUST be equal to the country in the qualified certificate.
The claim or element ``iss_reg_id`` MUST NOT be present when the qualified certificate already contains the registration identifier ([`ETSI TS 119 472-1`_] EAA-5.2.4.1-11 and EAA-6.2.4.1-13).

Attestation Identity
--------------------

The attestation identity code identifies one issued attestation.

In SD-JWT VC the attestation identity code is the ``jti`` claim ([`ETSI TS 119 472-1`_] EAA-5.2.3-01).
``jti`` MAY be present.
When ``jti`` is present, its value MUST uniquely identify that attestation.

In mdoc the attestation identity code is the ``document_number`` data element ([`ETSI TS 119 472-1`_] EAA-6.2.3-01).
``document_number`` MUST be present.
For an mDL, ``document_number`` MUST use the namespace ``org.iso.18013.5.1``.
For an mdoc that is not an mDL, ``document_number`` MUST use the namespace ``org.iso.23220.1``.

Subject
-------

Every attribute in a QEAA or a PuB-EAA MUST refer to one subject ([`ETSI TS 119 472-1`_] QEAA-5.2.5.5-01, PuB-EAA-5.2.5.6-01, QEAA-6.2.5.5-01 and PuB-EAA-6.2.5.6-01).
A QEAA or a PuB-EAA MUST NOT contain ``subAttrs``.
A QEAA or a PuB-EAA MUST NOT contain a ``SubAttr`` value.

In SD-JWT VC, ``sub`` follows :ref:`credential-data-model:Digital Credential SD-JWT Metadata Attributes`.
``also_known_as`` is the subject pseudonym ([`ETSI TS 119 472-1`_] EAA-5.2.5.2-01).
``also_known_as`` MUST be a string when present.
A PuB-EAA in SD-JWT VC MUST contain exactly one of ``sub`` and ``also_known_as`` ([`ETSI TS 119 472-1`_] PuB-EAA-4.2.6.8-01).
A QEAA in SD-JWT VC MAY contain ``sub``.
A QEAA in SD-JWT VC MAY contain ``also_known_as``.
A QEAA in SD-JWT VC MUST NOT contain both ``sub`` and ``also_known_as``.

In mdoc, the subject is identified either by ``also_known_as`` or by the set ``given_name``, ``family_name`` and ``document_number`` ([`ETSI TS 119 472-1`_] EAA-6.2.5.1-02 and EAA-6.2.5.1-05).
The attestation MUST contain one of those two identifications.
The attestation MUST NOT contain both.
``also_known_as`` MUST be a text string in the namespace ``org.etsi.01947201.010101``.
For an mDL, ``given_name`` and ``family_name`` MUST use the namespace ``org.iso.18013.5.1``.
For an mdoc that is not an mDL, ``given_name`` and ``family_name`` MUST use the namespace ``org.iso.23220.1`` ([`ISO-IEC-23220-2`_] and [`ETSI TS 119 472-1`_] EAA-6.1-03).

Technical and Administrative Validity
-------------------------------------

Technical validity is the interval during which the encoded attestation and its signature are valid.
Administrative validity is the interval during which the attested attributes remain valid, such as the expiry of a licence.

In SD-JWT VC, technical validity MUST be expressed by ``nbf`` and ``exp``, as already required for an EAA in :ref:`credential-data-model:Digital Credential SD-JWT Metadata Attributes` ([`ETSI TS 119 472-1`_] EAA-5.2.7.1-01 and EAA-5.2.7.1-03).
Administrative validity MUST be expressed by ``issuance_date`` and ``date_of_expiry`` when the credential type defines them.
A QEAA or a PuB-EAA MUST NOT contain ``adm_nbf``.
A QEAA or a PuB-EAA MUST NOT contain ``adm_exp``.

In mdoc, technical validity MUST be expressed by ``validFrom`` and ``validUntil`` inside ``validityInfo`` ([`ETSI TS 119 472-1`_] EAA-6.2.7.1-01 and EAA-6.2.7.1-02).
``validFrom`` MUST be present.
``validUntil`` MUST be present.
Both values MUST be UTC times.
Both values MUST have a precision of whole seconds.
Both values MUST omit fractions of a second ([`ETSI TS 119 472-1`_] EAA-6.2.7.1-03, EAA-6.2.7.1-04 and EAA-6.2.7.1-05).
Administrative validity MUST be expressed by ``issue_date`` and ``expiry_date`` in the document namespace ([`ETSI TS 119 472-1`_] EAA-6.2.6-01 and EAA-6.2.7.2-01).

Status and Short-Lived Attestations
------------------------------------

The short-lived signal means that the validity period is short enough that a revocation check is not required ([`ETSI TS 119 472-1`_] EAA-4.2.13-02).

In SD-JWT VC the short-lived signal is the claim ``shortLived`` with the JSON null value ([`ETSI TS 119 472-1`_] EAA-5.2.12-02).
In mdoc the short-lived signal is the element ``shortLived`` set to ``true`` in the namespace ``org.etsi.01947201.010101`` ([`ETSI TS 119 472-1`_] EAA-6.2.12-04).
``shortLived`` MAY be present.

When the short-lived signal is absent, ``status`` MUST be present ([`ETSI TS 119 472-1`_] QEAA-5.2.10.2-01, PuB-EAA-5.2.10.3-01, QEAA-6.2.10.2-01 and PuB-EAA-6.2.10.3-01).
That ``status`` value MUST follow :ref:`credential-data-model:Digital Credential SD-JWT Metadata Attributes` for SD-JWT VC.
That ``status`` value MUST follow :ref:`credential-data-model:Mobile Security Object` for mdoc.
Token Status List, as already required by those sections, is the EAA status service of [`ETSI TS 119 472-1`_] clause 5.2.10 and clause 6.2.10.

A QEAA or a PuB-EAA MAY contain ``oneTime``.
In SD-JWT VC, a present ``oneTime`` claim MUST have the JSON null value ([`ETSI TS 119 472-1`_] EAA-5.2.8.2-05).
In mdoc, ``oneTime`` MUST be a boolean in the namespace ``org.etsi.01947201.010101`` ([`ETSI TS 119 472-1`_] EAA-6.2.8.2-03).
When ``oneTime`` is present in SD-JWT VC, the Wallet Unit MUST present the attestation only once.
When ``oneTime`` is ``true`` in mdoc, the Wallet Unit MUST present the attestation only once.

Components Not Used
-------------------

A QEAA or a PuB-EAA MUST NOT contain an audience component ([`ETSI TS 119 472-1`_] EAA-5.2.8.1-01 and EAA-6.2.8.1-01).
Relying Party restrictions for these attestations use the :ref:`infrastructure-trust:Embedded Disclosure Policy (EDP)`.
A QEAA or a PuB-EAA MUST NOT contain a renewal-service component ([`ETSI TS 119 472-1`_] EAA-5.2.11-01 and EAA-6.2.11-01).
An SD-JWT VC QEAA or PuB-EAA MUST NOT contain an ``evidence`` claim.
An mdoc QEAA or PuB-EAA MUST NOT contain an attributes-evidence element ([`ETSI TS 119 472-1`_] EAA-6.2.9-01).

SD-JWT VC Profile
-----------------

Selective disclosure, ``vct``, ``vct#integrity``, ``_sd`` and ``_sd_alg`` remain those specified in :ref:`credential-data-model:SD-JWT-VC Credential Format`.
The ``vct`` value MUST identify a Credential Catalog entry whose ``legal_type`` is ``qeaa`` or ``pub-eaa``.

Protected Header
^^^^^^^^^^^^^^^^

The protected JOSE header MUST contain ``x5u`` ([`ETSI TS 119 472-1`_] QEAA-5.6.2-02 and PuB-EAA-5.6.3-02).
The protected JOSE header MUST contain ``x5t#S256`` ([`ETSI TS 119 472-1`_] QEAA-5.6.2-02 and PuB-EAA-5.6.3-02).
``x5u`` MUST be an HTTPS URI at which the signer certificate is available free of charge.
``x5c`` remains REQUIRED as specified in :ref:`credential-data-model:Digital Credential SD-JWT Metadata Attributes`.
The end-entity certificate in ``x5c`` MUST be the certificate identified by ``x5u`` and ``x5t#S256``.

Payload Claims
^^^^^^^^^^^^^^

The following claims apply in addition to :ref:`credential-data-model:Digital Credential SD-JWT Metadata Attributes`.

.. _table_qeaa_pub_eaa_sdjwt_claims:
.. list-table::
    :class: longtable
    :widths: 20 55 25
    :header-rows: 1

    * - **Claim**
      - **Description**
      - **Reference**
    * - ``category``
      - REQUIRED. String. Values are specified in :ref:`credential-data-model-qeaa-pub-eaa:Category`.
      - [`ETSI TS 119 472-1`_] clause 5.2.2
    * - ``jti``
      - OPTIONAL. String. Attestation identity code. See :ref:`credential-data-model-qeaa-pub-eaa:Attestation Identity`.
      - [`ETSI TS 119 472-1`_] EAA-5.2.3-02
    * - ``also_known_as``
      - CONDITIONAL. See :ref:`credential-data-model-qeaa-pub-eaa:Subject`.
      - [`ETSI TS 119 472-1`_] EAA-5.2.5.2-02
    * - ``shortLived``
      - OPTIONAL. JSON null. See :ref:`credential-data-model-qeaa-pub-eaa:Status and Short-Lived Attestations`.
      - [`ETSI TS 119 472-1`_] EAA-5.2.12-02
    * - ``oneTime``
      - OPTIONAL. JSON null. See :ref:`credential-data-model-qeaa-pub-eaa:Status and Short-Lived Attestations`.
      - [`ETSI TS 119 472-1`_] EAA-5.2.8.2-05

mdoc-CBOR Profile
-----------------

An mDL QEAA or PuB-EAA MUST carry the mDL data elements in the namespace ``org.iso.18013.5.1`` ([`ISO18013-5`_] and [`ETSI TS 119 472-1`_] EAA-6.1-02).
A QEAA or PuB-EAA that is not an mDL MUST carry its document data elements in the namespace ``org.iso.23220.1`` ([`ISO-IEC-23220-2`_] and [`ETSI TS 119 472-1`_] EAA-6.1-03).
Data elements defined by [`ETSI TS 119 472-1`_] MUST use the namespace ``org.etsi.01947201.010101`` ([`ETSI TS 119 472-1`_] EAA-6.1-04).

Mobile Security Object Headers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For a QEAA or a PuB-EAA the protected header of ``issuerAuth`` is specified in this section.
The rule that limits the protected header to the signature algorithm applies only to other Digital Credentials, as stated in :ref:`credential-data-model:Mobile Security Object`.

The protected header MUST contain the signature algorithm, label ``1``.
The protected header MUST contain ``x5u``, label ``35``, as specified in :rfc:`9360` ([`ETSI TS 119 472-1`_] QEAA-6.6.2-02 and PuB-EAA-6.6.3-02).
The protected header MUST contain ``x5t``, label ``34``, as specified in :rfc:`9360` ([`ETSI TS 119 472-1`_] QEAA-6.6.2-02 and PuB-EAA-6.6.3-02).
The hash algorithm inside ``x5t`` MUST be SHA-256 ([`ETSI TS 119 472-1`_] QEAA-6.6.2-03 and PuB-EAA-6.6.3-03).
``x5u`` MUST be an HTTPS URI at which the signer certificate is available free of charge.

The unprotected header MUST contain ``x5chain``, label ``33``, as specified in :ref:`credential-data-model:Mobile Security Object`.
The Wallet Unit MUST retrieve the signer certificate from ``x5u``.
The Wallet Unit MUST reject the attestation when the SHA-256 thumbprint of that certificate differs from ``x5t``.
The Wallet Unit MUST reject the attestation when the end-entity certificate in ``x5chain`` differs from the certificate retrieved from ``x5u``.

Namespace org.etsi.01947201.010101
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _table_qeaa_pub_eaa_mdoc_etsi_namespace:
.. list-table::
    :class: longtable
    :widths: 22 53 25
    :header-rows: 1

    * - **Element**
      - **Description**
      - **Reference**
    * - ``category``
      - REQUIRED. Text string. Values are specified in :ref:`credential-data-model-qeaa-pub-eaa:Category`.
      - [`ETSI TS 119 472-1`_] clause 6.2.2
    * - ``also_known_as``
      - CONDITIONAL. Text string. See :ref:`credential-data-model-qeaa-pub-eaa:Subject`.
      - [`ETSI TS 119 472-1`_] EAA-6.2.5.2-01
    * - ``iss_reg_id``
      - See :ref:`credential-data-model-qeaa-pub-eaa:Issuer Identification`. Text string when present.
      - [`ETSI TS 119 472-1`_] EAA-6.2.4.1-13
    * - ``shortLived``
      - OPTIONAL. Boolean. See :ref:`credential-data-model-qeaa-pub-eaa:Status and Short-Lived Attestations`.
      - [`ETSI TS 119 472-1`_] EAA-6.2.12-03
    * - ``oneTime``
      - OPTIONAL. Boolean. See :ref:`credential-data-model-qeaa-pub-eaa:Status and Short-Lived Attestations`.
      - [`ETSI TS 119 472-1`_] EAA-6.2.8.2-03

Verification
------------

The Wallet Unit MUST reject a QEAA whose ``category`` differs from ``urn:etsi:esi:eaa:eu:qualified``.
The Wallet Unit MUST reject a PuB-EAA whose ``category`` differs from ``urn:etsi:esi:eaa:eu:pub``.
The Wallet Unit MUST validate the qualified signature or seal.
The Wallet Unit MUST validate the issuer certificate path as specified in :ref:`trust-evaluation:Trust Evaluation Process`.
A QEAA path ends at the Trusted List of the Qualified Trust Service Provider.
A PuB-EAA path ends at the PuB-EAA Providers List of Trusted Entities.
The Wallet Unit MUST reject the attestation outside its technical validity.
When the short-lived signal is absent, the Wallet Unit MUST reject the attestation when the Token Status List reports it as invalid.

Remote presentation MUST use [`OpenID4VP`_] as profiled by [`OPENID4VC-HAIP`_].
Proximity presentation of an mdoc MUST use [`ISO18013-5`_].

Non-normative Examples
----------------------

The following examples are non-normative.

SD-JWT VC protected header for a QEAA:

.. literalinclude:: ../../examples/qeaa-sd-jwt-profile-header.json
    :language: JSON

SD-JWT VC claims that this section adds, shown without selective-disclosure encoding:

.. literalinclude:: ../../examples/qeaa-sd-jwt-profile-claims.json
    :language: JSON

The same claims for a PuB-EAA, with ``category`` set to ``urn:etsi:esi:eaa:eu:pub``:

.. literalinclude:: ../../examples/pub-eaa-sd-jwt-profile-claims.json
    :language: JSON

mdoc elements in the namespace ``org.etsi.01947201.010101`` for a QEAA, shown in diagnostic JSON and not as encoded CBOR:

.. literalinclude:: ../../examples/qeaa-mdoc-etsi-namespace.json
    :language: JSON

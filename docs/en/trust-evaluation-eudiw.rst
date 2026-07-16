Trust Evaluation in the EUDIW Trust Framework
------------------------------------------------

EUDIW Trust Evaluation Processes by Context
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The procedures are defined in a general form, with a Trust Evaluator and a Trust Evaluated Party, and the following table defines which entity acts in which role, when and for which purpose.

.. _table_eudiw_tf_roles:
.. list-table:: Trust Evaluation Processes by Entity and Context in the EUDIW Trust Framework
    :class: longtable
    :widths: 12 20 40 28
    :header-rows: 1

    * - **Entity**
      - **Context**
      - **As Trust Evaluator, implements**
      - **As Trust Evaluated Party, provides**
    * - Wallet Unit
      - Issuance of a Credential in the EU catalogue
      - On the Credential Issuer:

        - :ref:`trust-evaluation-eudiw:EUDIW Authentication`
        - :ref:`trust-evaluation-eudiw:EUDIW Authorization`
        - :ref:`trust-evaluation-eudiw:EUDIW Metadata Retrieval and Validation`

        On the received Credential:

        - :ref:`trust-evaluation-eudiw:EUDIW Signing Trust Anchor Validation`
      - The Wallet Instance Attestation, validated against the Wallet Providers List of Trusted Entities.
    * - Wallet Unit
      - Remote presentation, ``x509_hash`` prefix
      - On the Relying Party:

        - :ref:`trust-evaluation-eudiw:EUDIW Authentication`
        - :ref:`trust-evaluation-eudiw:EUDIW Authorization`
        - :ref:`trust-evaluation-eudiw:EUDIW Metadata Retrieval and Validation`
      - No entity level artifact is required from the Wallet Unit.
    * - Wallet Unit
      - Proximity presentation
      - On the Relying Party:

        - :ref:`trust-evaluation-eudiw:EUDIW Authentication`, based on the mdoc reader authentication
        - :ref:`trust-evaluation-eudiw:EUDIW Authorization`
      - No entity level artifact is required from the Wallet Unit.
    * - Credential Issuer
      - Issuing Credentials in the EU catalogue
      - On the Wallet Instance:

        - :ref:`trust-evaluation-eudiw:EUDIW Signing Trust Anchor Validation`, applied to the Wallet Instance Attestation
      - The Wallet-Relying Party Access Certificate and its registration, that is the Wallet-Relying Party Registration Certificate or the corresponding Register entry.
    * - Relying Party
      - Remote or proximity presentation
      - On the received Credentials:

        - :ref:`trust-evaluation-eudiw:EUDIW Signing Trust Anchor Validation`
      - The Wallet-Relying Party Access Certificate and its registration, that is the Wallet-Relying Party Registration Certificate or the corresponding Register entry.
    * - Relying Party Intermediary
      - Presentation, on behalf of an intermediated Relying Party
      - It does not act as Trust Evaluator in the operational flows.
      - Its own Wallet-Relying Party Access Certificate and the Wallet-Relying Party Registration Certificate of the intermediated Relying Party.

EUDIW Trust Anchor Validation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section specifies the **Trust Anchor Validation Process** that a Wallet Unit or Wallet-Relying Party uses to establish the cryptographic integrity and authenticity of a List of Trusted Entities, or a Trusted Lists in order to:

- validate the trustworthiness of a Trust Anchor (see :ref:`trust-artifact-eudiw:Trust Anchor Certificate Profile`) to authenticate, authorize or validate an entity or artifact during *runtime*.
- validate the information contained in the List for *historcal purposes*.

Depending on the Trust Artifact or Attestation being verified, the Trust Evaluator MUST fetch, download, and validate the List which references the appropriate Trust Anchor:

1. *List of Trusted Entities* MUST be used to retrieve Trust Anchors for validating:

   - **WRPAC** in the Providers of WRPAC LoTE.
   - **WRPRC** in the Providers of WRPRC LoTE.
   - **Wallet Unit Attestation Sign/Seal Certificates** in the Wallet Providers LoTE.
   - **PID Sign/Seal Certificates** in the PID Providers LoTE.
   - **Registrar Sign/Seal Certificates** in the Registrar LoTE.
   - **PuB-EAA Sign/Seal Certificates** in the PuB-EAA Providers LoTE.
2. *Trusted Lists* are used to retrieve Trust Anchors for validating:

   - **QEAA Sign/Seal Certificates** in the corresponding Member State Trusted List.

To verify the authenticity of the retrieved Lists, the Entity MUST perform the following validations:

- :ref:`trust-evaluation-eudiw:List of Trusted Entities Validation`: Validate the digital signature of the List of Trusted Entities by verifying it against the List of Trusted Entities Provider certificate. This certificate is published in the Official Journal of the European Union.
- :ref:`trust-evaluation-eudiw:Trusted List Validation`: Validate the digital signature of the TL by verifying it against the corresponding Member State public keys published in the List Of Trusted Lists (LOTL). The List Of Trusted Lists (LOTL) itself is authenticated by validating its digital signature against the Official Journal of the European Union.

**Input**

The validating Entity MUST base Trust Anchor validation decisions only on information derived from:

- The Official Journal of the EU (OJEU) anchoring trust in the root certificates that signed the Lists of Trusted Entities and List of Trusted Lists. The current version of OJEU can be found `here <https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ:C_202601944>`_.
- A validated Lists of Trusted Entities or List of Trusted Lists and Member State level Trusted Lists.

**Outcome**

Each validation procedure (defined in :ref:`trust-evaluation-eudiw:List of Trusted Entities Validation` and :ref:`trust-evaluation-eudiw:Trusted List Validation`) gives a granular verification result code when it detects a negative condition. These codes feed into the final decision:

- If the validation algorithms terminate with:

    - ``LoTE-Status == LoTE_VERIFICATION_PASSED``, or
    - ``LOTL-Status == LOTL_VERIFICATION_PASSED``, or
    - ``EU-TL-Status == EU-TL_VERIFICATION_PASSED``;

    Then the List of Trusted Entities or Trusted List is valid and the Trust Anchor certificates (see :ref:`trust-artifact-eudiw:Trust Anchor Certificate Profile`) therein MUST be considered trustworthy.

- If the validation algorithms terminate with:

    - ``LoTE-Status == LoTE_VERIFICATION_FAILED``, or
    - ``LOTL-Status == LOTL_VERIFICATION_FAILED``, or
    - ``EU-TL-Status == EU-TL_VERIFICATION_FAILED``;

     Then the List of Trusted Entities or Trusted List is not valid and the Trust Anchor certificates (see :ref:`trust-artifact-eudiw:Trust Anchor Certificate Profile`) therein MUST NOT be considered trustworthy. 

.. note::

    Within IT-Wallet, a Wallet Unit is expected to cache validated Lists of Trusted Lists, Lists of Trusted Entities and Member States' Trusted Lists, so that it does not retrieve them at every interaction. The frequency of updates and the types of lists to cache represent a trade-off between interoperability and resource utilization.

List Key Rotation and Historical Verification
"""""""""""""""""""""""""""""""""""""""""""""

To support continuous key rotation and regular updates, the LoTE and LOTL implement a *pivoting mechanism*. This mechanism consists of publishing the most recent version of the List at the primary URI referenced in the Official Journal of the European Union, while archiving earlier versions at distinct URI *pivots*. Each List version is signed with a public key referenced within the immediately preceding version, rather than reusing the same key. The newest List version explicitly contains the URIs where all historical versions are hosted. An Entity validates this chain of pivots from the newest version back to the oldest by verifying that each subsequent artifact is correctly signed by the public key authorized in the prior version. Final validation is achieved by verifying the trustworthiness of the oldest public key, either via a lookup in the OJEU or directly against a cached, previously validated version of the List. This ensures that an entity possessing the last known valid version can reliably discover the next version and validate it via an unbroken chain of trust rooted in the OJEU.

List of Trusted Entities Validation
"""""""""""""""""""""""""""""""""""""

This section defines the validation of the EU-level List of Trusted Entities (List of Trusted Entities). The List of Trusted Entities is a digitally signed/sealed artifact (JWT format) containing metadata and public keys for entities operating at the EU level.

**List of Trusted Entities Validation Algorithm**

The validating Entity MUST initializes the following variables as described in [`ETSI_TS_119_615`_].

**Input Variables**:

- ``OJEU-Loc``: URI of the latest (known) Official Journal of the European Union OJEU publication.
- ``OJEU-LoTE-Loc``: URI of the last processed LoTE. Defaults to the value in ``OJEU-Loc``.
- ``OJEU-LoTE-Certs-Set``: The set of Trust Anchor certificates from the ``OJEU-Loc`` publication.
- ``LoTE``: The LoTE JWT currently being processed. Initialized as ``NULL``.
- ``LoTE-Signer-Cert``: The certificate extracted from the ``x5c`` header parameter of the LoTE.
- ``LoTESO-Cert``: Temporary variable for the Scheme Operator certificate being validated. Initialized as ``NULL``.
- ``LoTESO-Certs-Set``: Trusted certificates extracted from the ``PointersToOtherLoTE`` claim (``SchemeTerritory`` ``EU``) of a LoTE or Pivot. Initialized as ``NULL``.

**Output Variables**:

- ``Authenticated-LoTE``: The validated JSON payload.
- ``LoTE-Status``: The validation result (e.g., ``LoTE_VERIFICATION_PASSED``).
- ``LoTE-Sub-Status``: detailed error codes.

**Validation Steps**:
The validation MUST perform the following steps:

1. (Initialization) Download the JWT file from ``OJEU-LoTE-Loc`` and assign it to ``LoTE``.
2. (Parsing) Extract the first certificate from the ``x5c`` header of ``LoTE`` and assign it to ``LoTE-Signer-Cert``.
3. (Pivot Discovery) Iterate through the ``uriValue`` claims in the ``SchemeInformationURI`` object. Count the number of valid URIs found before encountering the URI matching ``OJEU-Loc``. Let ``n`` be that count.

    - If no URI matches ``OJEU-Loc``: Validation MUST fail with ``LoTE-Status`` set to ``LoTE_VERIFICATION_FAILED`` and ``LoTE-Sub-Status`` set to ``OJEU_LOCATION_INPUT_NOT_MATCHING_OJEU_LOCATION_IN_LoTE``. (This may imply that a new version of the OJEU is available).

4. (LoTE Location Conflict) Check the condition: ``OJEU-LoTE-Loc != LoTE Location`` AND ``LoTE != Content at LoTE Location``.

    - (``LoTE Location`` is the URI in the ``PointersToOtherLoTE`` claim of ``LoTE`` with ``SchemeTerritory`` = ``EU``).
    - If ``TRUE``: Validation MUST stop with ``LoTE-Status`` set to ``LoTE_VERIFICATION_FAILED`` and ``LoTE-Sub-Status`` set to ``LoTE_FILE_CONFLICT``.
    - If ``FALSE``, proceed to the next step.

5. (LoTE Freshness) Check the condition: ``OJEU-LoTE-Loc == LoTE Location`` AND ``LoTE !=`` Content at ``LoTE Location``.

    - If ``TRUE``: Set ``OJEU-LoTE-Loc`` to ``LoTE Location`` and restart from Step 1.
    - If ``FALSE``, proceed to the next step.

6. (Digital Signature Validation) Validate the cryptographic signature of the current ``LoTE`` using the public key from ``LoTE-Signer-Cert``.

    - If validation fails: Stop with ``LoTE-Status`` set to ``LoTE_VERIFICATION_FAILED`` and ``LoTE-Sub-Status`` set to ``LoTE_SIGNATURE_VERIFICATION_FAILED``.
    - If successful:

        - Set ``LoTESO-Cert`` to ``LoTE-Signer-Cert``.
        - Set ``LoTESO-Certs-Set`` to the certificates found in the ``PointersToOtherLoTE`` claim (territory ``EU``) of the current ``LoTE`` payload.

7. (Intermediate Pivot Validation)

    - Case ``n = 0`` (No Pivots): Proceed directly to Step 8.
    - Case ``n != 0`` (History Chain):

        - Iterate ``i`` from 1 to ``n`` (from most recent Pivot to oldest). Let ``Pivot`` be the file downloaded from the ``i``-th URI.
        - (Link Check) Set ``Pivot-Certs-Set`` to the certificates in the ``PointersToOtherLoTE`` claim (territory ``EU``) of ``Pivot``. If ``LoTESO-Cert`` (the signer of the previous file in the chain) is not in ``Pivot-Certs-Set``, validation MUST fail with ``LoTE-Sub-Status`` set to ``PIVOT_i-1_SIGNER_CERT_NOT_AUTHENTICATED_BY_PIVOT_i``.
        - (Update Signer) Set ``LoTESO-Cert`` to the first certificate in the ``x5c`` header parameter of ``Pivot``.
        - (Verify Signature) Validate the signature of ``Pivot`` using ``LoTESO-Cert``. If it fails, validation MUST fail with ``LoTE-Status`` set to ``LoTE_VERIFICATION_FAILED``, and ``LoTE-Sub-Status`` set to ``PIVOT_i_SIGNATURE_VERIFICATION_FAILED``.
        - The loop continues, walking backwards until ``LoTESO-Cert`` represents the signer of the oldest Pivot.

8. (Trust Root Validation) Verify the end of the chain. If ``LoTESO-Cert`` (from the last Pivot or current LoTE List of Trusted Entitie) is not in ``OJEU-LoTE-Certs-Set`` (the Trust Anchor), validation MUST fail with ``LoTE-Sub-Status`` set to ``PIVOT_n_SIGNER_CERT_NOT_AUTHENTICATED_BY_OJEU``.

9. (Expiration) If current time is greater than the ``NextUpdate`` parameter's value of ``LoTE``, validation MUST fail.

10. (Success) Set ``Authenticated-LoTE`` to ``LoTE``, ``LoTE-Status`` to ``LoTE_VERIFICATION_PASSED``.

11. (Update Bookmark) If ``OJEU-LoTE-Loc`` does not match the ``LoTE Location`` in ``Authenticated-LoTE`` (territory ``EU``), update ``OJEU-LoTE-Loc`` to that value.

12. (Update Trust Root) [Caution: This step modifies the Root of Trust configuration]

    - If ``OJEU-Loc`` does not match the first URI in ``SchemeInformationURI``, update ``OJEU-LoTE-Loc``.
    - Update ``OJEU-LoTE-Certs-Set`` according to the new Trust Anchor either in ``Authenticated-LoTE`` or from a new Official Journal of the European Union OJEU publication.

.. note::
    
    - Steps 4, 5 and 11 allow modifying the location of the List of Trusted Entities file without changing the initial trusted signer public key, as long as the both the old and the new location have the same content (otherwise the validation fails with ``LoTE_FILE_CONFLICT`` status). This allows the List of Trusted Entities to be retrieved from different locations without affecting the Trust Anchor validation as long as the content is the same.
    - In case of ``OJEU_LOCATION_INPUT_NOT_MATCHING_OJEU_LOCATION_IN_LoTE`` error, it is likely that the Official Journal of the European Union OJEU publication has been updated with a new location for the List of Trusted Entities List of Trusted Entities. The validating Entity SHOULD repeat the validation process after having downloaded the most recent version of the OJEU.
    - In step 8, the validating Entity established the binding of the signer certificate of the ``LoTE`` XML with the certificate referenced in the Official Journal of the European Union OJEU, effectively using the latter as a Trust Anchor.

Below is a flowchart summarizing the above steps for the validation of the List of Trusted Entities List of Trusted Entities:

.. plantuml:: plantuml/lote-val-alg.puml
    :width: 99%
    :alt: The figure illustrates the Flowchart of the LoTE Validation Algorithm.
    :caption: `Flowchart of the LoTE Validation Algorithm. <https://www.plantuml.com/plantuml/png/ZLL_Rzf84FtVds9EbQwWNdnGcgO7WJGXH9UAqgWaEPt4Fnll65QOMMjt2SctF-zwoHhEf46A5DjlPjxyU3DVjM7Ah5TPf9U2SgRO2iuJ8nw5URvWoNAkv9huK6PImRlK_UgGKd5K7jLnlnhKbIIpYwc0XfAuC4BI_wBYITf9iHPQ3Tjg7Nz-wDJ1VDmAA3B2P0XZeGt856xLMXlaC29J6A26R__SmZtB16VMFefSaQ98OOxCH000tNOCroGC_0wNSaEPPFoWkncbIgxWnxVHtT4XpD5O9ZtdkNJ_COORfZJ2tyWugkwCHaz6iSJ0LCm95GnH6NWwhXg951gT6AvixNmqcS3TpsiG18iYi5JFPqqm2oHeJAJzCmxSR3fx5zWPWZKilfQ-PlIdemldb2oaWkzYhbnXO8B8aVTUh8iGkNl0J2Cq_aKDZIaQe131iVmKsmZEXsrJced4dCteHyPTWHplt_g5-qruFfzS1aJrgy_8HWjHN2vN8iCN_xtJqtVf5tx2sM0GO5NIWVX4xdfw3rSAzO9GQqWMc2o19KO3qpOqP5BcC6S6WnVY8et2Vz53CTGRfZXqxt9U8Dym39PkcdOIFXZumOFDmYRKE8uhT8QMpbxf-cyldT2-JSKhk4UbRKikqM1Yi9WB86dAMHckbK8ori05BpeQsLP-ZhTAGKWyvb1URdQPMIlSzkoQ7grnCohxnKJMVTNQKXIfyADZySZt6kiRMZRolkBT3k8zKu8zPAWBGVcCjeBgmy5sb8WZAxcWmotAkdNwlc7FTWtq8jzpMvsJ6AurKE6y1GsIS2CUfT7D7HKI3A3r1qpjZe6nb7dJ4oxVE1Ft7aI_3KO2LJHVMKdEPhkCl9a8sjmHu5ZGiXoTeX05mxrQ69_Rm_FM3-HbTe5vLIAXUHTABf7AuXG1cA2twwvEmbukLNvrsz0rm5FrAxEtgyRwEhoChhTzVK83BGSFOF2ej-VgG--lcQ4a8sYDO6IvLfBj4Nijcztr8E0K28fr-bqgdvW-goXTVFWGXDsCzYh_7gPBaPTcbHjOzjBMZFgjweH_YNspVyeTW_qvwOxbxSZT5BQsNun8c1ynkmjV4N7WPkFz5SFeAHVAi_8ZF94R6DYzzcJAYJchlGhTGn8lVTRiaj2yskFGRRVYQfLkpgVJqQNrmZyXTrv2ptpLkkrs32LBTmKpk91okM9g-UkhC2EHGh9WD4SEWhQgx5cl7r-yLg_rZEm157CGgNCFA_c8VEUwM6BHLoI-NcN_0G00>`_

Below are listed the Sub-Status error codes of the List of Trusted Entities in tabular format.

.. list-table:: List of Trusted Entities Sub-Status Error Codes
   :class: longtable
   :header-rows: 1

   * - Code
     - Phase
     - Meaning
   * - ``OJEU_LOCATION_INPUT_NOT_MATCHING_OJEU_LOCATION_IN_LoTE``
     - both
     - No URI matches the expected ``OJEU-Loc`` within the LoTE's ``SchemeInformationURI``. This typically implies that a newer version of the OJEU publication is available.
   * - ``LoTE_FILE_CONFLICT``
     - both
     - A location conflict is detected where the tracked LoTE location differs from the active LoTE location, and the content across these files does not match.
   * - ``LoTE_SIGNATURE_VERIFICATION_FAILED``
     - both
     - The cryptographic signature validation of the current LoTE file failed using the extracted signer certificate, indicating potential tampering or corruption.
   * - ``PIVOT_i-1_SIGNER_CERT_NOT_AUTHENTICATED_BY_PIVOT_i``
     - both
     - The historical chain of trust is broken because the signing certificate of the previous pivot or file (i-1) cannot be found in the trusted certificate set of the succeeding pivot (i).
   * - ``PIVOT_i_SIGNATURE_VERIFICATION_FAILED``
     - both
     - The cryptographic signature validation failed for an intermediate pivot file (i) within the historical chain.
   * - ``PIVOT_n_SIGNER_CERT_NOT_AUTHENTICATED_BY_OJEU``
     - both
     - The final certificate at the root of the pivot chain (or the current LoTE signer if no pivots exist) is not found in the initial ``OJEU-LoTE-Certs-Set`` Trust Anchor.
   * - ``EUTL_SIGNATURE_VERIFICATION_FAILED``
     - both
     - The digital signature of the Trusted List failed validation or is undetermined when checked against the signer certificate's public key.
   * - ``EUTLSO_SIGNER_CERT_NOT_AUTHENTICATED_BY_LoTE``
     - both
     - The Trusted List signer certificate is not present in the certificate set extracted from the LOTL, indicating the signing certificate of the TL is not authenticated and may have been tampered with.
   * - ``WARNING_EUTL_NEXTUPDATE_PASSED``
     - both
     - The current date and time are greater than the ``NextUpdate`` value specified in the Trusted List, indicating the list is expired or out of date.

Trusted List Validation
"""""""""""""""""""""""""""""

This section defines the validation of Trusted List. In order to validate the Trusted List, the Wallet Unit MUST:

1. Validate the EU List of Trusted Lists using the algorithm described in section 4.1 of [`ETSITS119615`_]. If this fails, the validation stops and the Wallet Unit MUST consider the Entity it is interacting with as not trusted. The validation process is analogue to the :ref:`trust-evaluation-eudiw:List of Trusted Entities Validation` except for the LOTL format which is always XML.
2. Parse the validated EU List of Trusted Lists to discover the necessary certificate to validate the relevant Member State Trusted List.
3. Obtain and validate the relevant Trusted List as described in section 4.2 of [`ETSITS119615`_].

X509 Certificate Chain Validation Algorithm
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This procedure validates a certification path. It is invoked by the :ref:`trust-evaluation-eudiw:EUDIW Authentication` and by the :ref:`trust-evaluation-eudiw:Authorization Artifacts Validation` to validate the Wallet-Relying Party Access Certificate, the Wallet-Relying Party Registration Certificate and the Registrar Sign/Seal Certificate chains. The Trust Anchor consumed as ``trust_anchor`` is profiled in :ref:`trust-artifact-common:Trust Anchor Certificate Profile`.

The certification path validation is the standard X.509 path validation defined in :rfc:`5280#section-6`, with the revocation status checking defined in :rfc:`5280` and :rfc:`6960`. The certificate lifecycle and the revocation mechanisms, including the CRL and the OCSP formats and parameters, are defined in :ref:`infrastructure-trust:Revocation Mechanisms`. The algorithm details are not redefined here. This is the same certification path validation used in the National Trust Framework (see :ref:`trust-evaluation:X.509 Certificate Chain Validation`), where the difference is the origin of the trust anchor and the additional extraction of the Federation Entity Identifier.

Within the EUDIW Trust Framework the following applies.

  - The ``trust_anchor`` is the trusted certificate obtained from the ``ServiceDigitalIdentity`` component of the applicable, validated List of Trusted Entities (see :ref:`trust-evaluation-eudiw:List of Trusted Entities Validation`), that is the Provider of WRPAC LoTE for the Wallet-Relying Party Access Certificate, the Provider of WRPRC LoTE for the Wallet-Relying Party Registration Certificate, and the Registrar LoTE for the Registrar Sign/Seal Certificate.
  - The revocation status checking MAY be skipped for a certificate that carries both the ``noRevAvail`` and the ``ETSIValAssuredCertMod`` extensions (see :ref:`trust-artifact-eudiw:Wallet-Relying Party Access Certificate (WRPAC) Profile`), whose status is then determined solely by its validity period.

**Input**

- ``path``: the sequence of ``n`` certificates ``C_1, ..., C_n`` provided by the Entity, where ``C_1`` is the first certificate of the chain and ``C_n`` is the end-entity certificate. For any ``i`` in ``1, ..., n-1``, ``C_i`` is the issuer of ``C_i+1``.
- ``trust_anchor``: the trusted certificate obtained from the ``ServiceDigitalIdentity`` of the validated List of Trusted Entities. It MUST either be exactly ``C_1`` or contain the public key used to sign ``C_1``. Implementations MUST support both self-signed and non-self-signed Trust Anchor certificates.
- ``current_time``: the current date and time.

**Outcome**

- The validated end-entity certificate ``C_n``, or a failure.

**Process**

1. Build the certification path from the end-entity certificate ``C_n`` to the ``trust_anchor``.
2. Execute the path validation defined in :rfc:`5280#section-6`, using the ``trust_anchor`` as the trust anchor input of the algorithm and ``current_time`` as the validation time.
3. Verify the revocation status of the certificates in the path according to :rfc:`5280` and :rfc:`6960`, unless the check is skipped as described above.

If any step fails, the certification path MUST be considered invalid and the artifact signature MUST NOT be verified with the presented certificate chain.

EUDIW Signing Trust Anchor Validation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This process provides and validates the root of trust for the verification of the issuer data authentication of a received attestation, that is a Digital Credential or the Wallet Instance Attestation. The validation of the Lists of Trusted Entities and Trusted Lists, and the extraction of the Trust Anchors they publish, is defined in :ref:`trust-evaluation-eudiw:EUDIW Trust Anchor Validation`. This section defines how such a validated Trust Anchor is then used to validate the signer of a received attestation.

.. note::
  In the National Trust Framework this root of trust is the Signing Trust Anchor of the signing X.509 PKI (see :ref:`trust-evaluation:Signing Trust Anchor Distribution and Validation`). Within the EUDIW Trust Framework the root of trust of a received attestation is the Trust Anchor published in the applicable List of Trusted Entities or Trusted List.

The applicable Trust Anchor depends on the type of the received attestation. For a Digital Credential it is selected according to the Credential Rulebook; for the Wallet Instance Attestation, for which no Rulebook applies, it is the Trust Anchor of the Wallet Provider:

- the PID Providers List of Trusted Entities for a PID;
- the corresponding Member State Trusted List for a QEAA;
- the PuB-EAA Providers List of Trusted Entities for a PuB-EAA;
- the Wallet Providers List of Trusted Entities for the Wallet Instance Attestation.

**Input**

- The received attestation and the signer certificate chain carried with it.
- The Credential type of the attestation, used to select the applicable List of Trusted Entities or Trusted List.

**Outcome**

- The validated Trust Anchor and the validated signer certificate for the attestation, or a failure.

**Process**

1. Select the applicable List of Trusted Entities or Trusted List according to the type of the received attestation, that is the Credential Rulebook for a Digital Credential and the Wallet Providers List of Trusted Entities for the Wallet Instance Attestation, and validate it as defined in :ref:`trust-evaluation-eudiw:EUDIW Trust Anchor Validation`, obtaining the Trust Anchor.
2. Validate the signer certificate chain of the attestation, for a Digital Credential the Document Signer certificate, against the obtained Trust Anchor, as defined in :ref:`trust-evaluation-eudiw:X509 Certificate Chain Validation Algorithm`.
3. Verify the attestation signature with the validated signer certificate.

If any step fails, the attestation MUST NOT be considered issued by a trusted issuer.

EUDIW Authentication
^^^^^^^^^^^^^^^^^^^^

The **Authentication Process** enables the Wallet Unit to authenticate a Wallet-Relying Party during an interaction. It establishes trust by validating the Wallet-Relying Party's X.509 certificate chain, starting from a trusted Provider of Wallet-Relying Party Access Certificate down to the presented Wallet-Relying Party Access Certificate, and verifying the Wallet-Relying Party's possession of the corresponding private key.

To authenticate the Wallet-Relying Party, the Wallet Unit MUST verify the authenticity and integrity of the presented Wallet-Relying Party Access Certificate by performing the following steps:

1. **Verify the Signature:** Use the public key from the validated Wallet-Relying Party Access Certificate to verify the Wallet-Relying Party's signature on the artifact it produces in the specific interaction, as detailed below.

    - During Credential Issuance, the Wallet Unit MUST obtain the Credential Issuer Metadata, extract the ``x5c`` claim value from the header and verify the Credential Issuer Metadata signature using the top certificate of the certificate chain (i.e., the one whose subject DN corresponds to the Credential Issuer's name).
    - During Credential Presentation,

        - if the Presentation follows the Remote Flow, the Wallet Unit MUST extract the ``x5c`` claim value from the header of the Request Object and verify the Request Object's signature using the top certificate of the certificate chain (i.e., the one whose subject DN corresponds to the Relying Party's name).
        - if the Presentation follows the Proximity Flow, the Wallet Unit MUST extract the ``readerAuthAll[].33`` (or alternatively ``readerAuth[].33``) claim value from the mdoc Request and check its signature using the top certificate of the certificate chain (i.e., the one whose subject DN corresponds to the Relying Party's name).

2. **Construct the Certification Path:** Build a path starting from the certificate issued by the Provider of WRPAC (``C_1``) and ending with the Wallet-Relying Party Access Certificate presented by the WRP (``C_n``). *(Note: The simplest path consists of just one certificate, where ``n = 1``).*

3. **LoTE Validation:** Retrieve the WRPAC Trust Anchor that anchors the root of the certificate path from the validated List of Trusted Entities (see :ref:`trust-evaluation-eudiw:List of Trusted Entities Validation`).

4. **Trust Anchor Retrieval:** To retrieve the correct Trust Anchor, the Wallet Unit MUST:
    
    - match the ``issuer.organizationIdentifier`` field value of certificate ``C_1`` with the ``TrustedEntityList[].TrustedEntity.TETradeName`` field value of the LoTE; and
    - use the certificates found in the ``TrustedEntityServices[].ServiceInformation.ServiceDigitalIdentity`` field as the Trust Anchor.

5. **Execute Path Validation:** Run the algorithm defined in :ref:`trust-evaluation-eudiw:X509 Certificate Chain Validation Algorithm` as described in :ref:`trust-evaluation-eudiw:Wallet-Relying Party Access Certificate Validation`.

.. warning::

    A Wallet-Relying Party MUST distinguish between transient authentication (e.g., access control) and content commitment (non-repudiation). To prevent an attacker from disguising a legal commitment as a protocol nonce, the Wallet-Relying Party MUST NOT use the Wallet-Relying Party Access Certificate private key to sign arbitrary data that could be controlled by an external party.


**Input**

The Wallet Unit's Authentication output MUST be based only on information derived from:

- The appropriate Trust Anchor obtained from a valid instance of the Provider of WRPAC LoTE;
- The X509 certificate path terminating with the WRPAC end-entity certificate;
- A Wallet-Relying Party signature over some data carrying the proof of possession of the private key referenced in the WRPAC. 

**Outcome**

The Wallet Unit MUST output a decision from the Authentication process: the Wallet-Relying Party can either be ``AUTHENTICATED`` or ``NON_AUTHENTICATED``. In the first case, the Wallet Unit SHOULD proceed in the interaction flow with the Wallet-Relying Party; in the second, the Wallet Unit MUST inform the User that the identity of the Wallet-Relying Party could not be verified and MUST stop the interaction flow as the entity is not trustworthy.

Wallet-Relying Party Access Certificate Validation
"""""""""""""""""""""""""""""""""""""""""""""""""""""

The Entity performing Wallet-Relying Party Access Certificate validation initializes the algorithm in :ref:`trust-evaluation-eudiw:X509 Certificate Chain Validation Algorithm` with the ``path`` and ``trust_anchor`` defined there, where ``C_1`` is the first certificate of the chain provided by the Wallet-Relying Party, ``C_n`` is the Wallet-Relying Party Access Certificate, and the ``trust_anchor`` is a certificate of the Provider of Wallet-Relying Party Access Certificate obtained from the List of Trusted Entities.

EUDIW Authorization
^^^^^^^^^^^^^^^^^^^
 
This section specifies the EUDIW Authorization Process that a Wallet Unit MUST execute to determine whether an interaction with a Wallet-Relying Party is allowed within the EUDI Wallet ecosystem. The EUDIW Authorization Process MUST start only *after* the Wallet-Relying Party has been successfully authenticated according to :ref:`trust-evaluation-eudiw:EUDIW Authentication`. If the Wallet-Relying Party has not been authenticated, the EUDIW Authorization Process MUST NOT start.
 
The authorization data of a Wallet-Relying Party is carried by the Wallet-Relying Party Registration Certificate or, equivalently, by the Register Response. Both are profiled in [`ETSI TS 119 475`_] and their data model is described in :ref:`trust-artifact-eudiw:Common Register Open APIs`. 
 
The EUDIW Authorization Process is split into:
 
- :ref:`trust-evaluation-eudiw:Authorization Artifacts Validation`, which validates integrity and authenticity of the Trust Artifact carrying the authorization data; and
- :ref:`trust-evaluation-eudiw:Authorization Validation`, which validates the information content of the validated artifact. In particular this validation covers:
 
    - **Issuance authorization**: determines whether a Credential Issuer is registered for the relevant role and authorized to issue the specific Digital Credential. This applies to PID, QEAA, PuB-EAA and EAA Providers operating within the EUDIW ecosystem.
    - **Presentation authorization**: determines whether a Relying Party request falls within its registered scope, whether an Embedded Disclosure Policy permits the disclosure, and whether the User approves. This applies to interactions involving both Relying Parties and Relying Party Intermediaries, across both Remote and Proximity Flows.
 
- :ref:`trust-evaluation:Authorization Decision and Override Rules`, which outputs an *Authorization Decision* expressed as ``AUTHORIZED`` or ``NOT_AUTHORIZED`` on the base of the Authorization Artifacts Validation and Authorization Validation results. Depending on the Flow type the User MAY *override* the Authorization Decision.
 
Within the *Authorization Validation*, the Wallet Unit MUST distinguish between the authenticated Wallet-Relying Party and the *Authorization Subject*, that is the entity whose authorization is being evaluated:
 
- During Issuance, the Authorization Subject is the Credential Issuer.
- During *direct* presentation, the Authorization Subject is the Relying Party.
- During *intermediated* presentation, the authenticated Wallet-Relying Party is the Relying Party Intermediary, while the Authorization Subject for the data request is the *intermediated Relying Party*, whose registered scope governs the request. The Relying Party Intermediary is itself a registered entity, and its authorization to act as an intermediary is established through the ``intermediary`` binding declared in the intermediated Relying Party authorization data (see the Binding verification below).
 
The Wallet Unit MUST support authorization-context resolution from both a Wallet-Relying Party Registration Certificate, where available, and the Register, where a Wallet-Relying Party Registration Certificate is not available or cannot be relied upon. The substantive authorization logic MUST NOT change based on the data source. Where both sources are available, the Wallet Unit MUST normalize both into the same internal authorization model before applying the rules.
 
Authorization Artifacts Validation
"""""""""""""""""""""""""""""""""""
 
The artifacts that carry the authorization data of an entity are the Wallet-Relying Party Registration Certificate and the Register Response. Both carry equivalent information, in the JWT and CWT profiles defined in Section 5.2.1 of [`ETSI TS 119 475`_]. The Wallet Unit MUST support the validation of both and MUST validate at least one of the two. Each validation procedure specifies its inputs, its processing logic and its output, a verification result code. The result MAY be overridden by the User under the conditions detailed in :ref:`trust-evaluation:Authorization Decision and Override Rules`.
 
The validation flow depends on the availability of the Wallet-Relying Party Registration Certificate in the interaction.
 
- During the Presentation flow the Relying Party MAY convey the Wallet-Relying Party Registration Certificate by value:
 
    - in the ``verifier_info`` parameter of the Request Object, in the Remote Flow, as defined in [`ETSI TS 119 472-2`_] and Section 5.1 of [`OpenID4VP`_];
    - in the ``euwrprc`` member of ``requestInfo`` in the ISO ``DeviceRequest``, in the Proximity Flow, as defined in Section 5.3 of [`ETSI TS 119 472-2`_] and in [`ISO18013-5`_].
 
- During the Issuance flow the Credential Issuer conveys the authorization data in the Credential Issuer Metadata through the ``issuer_info`` array, as defined in Section 4.2.3 of [`ETSI TS 119 472-3`_]. The array MAY contain a ``registration_cert`` element with the Wallet-Relying Party Registration Certificate by value, and MUST contain a ``registrar_dataset`` element with the self-declared registration information. The Embedded Disclosure Policy is distributed through the Credential Issuer Metadata within the ``credential_configurations_supported`` field, as defined in [`OpenID4VCI`_].
 
In case the Wallet-Relying Party Registration Certificate is not available, or its validation fails, the Wallet Unit MUST query the Register as described in :ref:`Register Query Validation <register-query-validation>`. The Register Response provides the same authorization-relevant data as the Wallet-Relying Party Registration Certificate. Each Registrar exposes an online service through the API described in :ref:`trust-artifact-eudiw:Common Register Open APIs`. When using this service the Wallet Unit SHOULD inform the User that an external query will be made.
 
**Wallet-Relying Party Registration Certificate Validation**
 
When a Wallet-Relying Party Registration Certificate is available, the Wallet Unit MUST validate it before relying on it:
 
1. **Format verification**: confirm that ``typ`` is ``rc-wrp+jwt`` in the Remote Flow, or ``rc-wrp+cwt`` in the Proximity Flow, as defined in Section 5.2.1 of [`ETSI TS 119 475`_].
2. **Algorithm verification**: verify that the signature algorithm is conformant, that is ``alg`` is neither ``none`` nor a deprecated algorithm.
3. **Signature validation**: verify that the Wallet-Relying Party Registration Certificate signature is valid.
4. **Trust Anchor validation**: validate the Providers of WRPRC List of Trusted Entities (see :ref:`trust-evaluation-eudiw:List of Trusted Entities Validation`) and retrieve the Trust Anchor from its ``TrustedEntitiesList.ServiceDigitalIdentity`` field.
5. **Path validation**: validate the certificate chain of the Wallet-Relying Party Registration Certificate as defined in :ref:`trust-evaluation-eudiw:X509 Certificate Chain Validation Algorithm`, where ``C_1`` is the certificate issued by the Provider of WRPRC, ``C_n`` is the Wallet-Relying Party Registration Certificate, and the ``trust_anchor`` is the Trust Anchor obtained at the previous step.
6. **Temporal validity**: check ``iat`` and ``exp`` if present.
7. **Status verification**: check the revocation status through the ``status`` field of the Wallet-Relying Party Registration Certificate, as defined in [`ETSI TS 119 475`_], following :ref:`credential-revocation:Checking Credentials Statuses`.
8. **Coherence check**: verify that the subject and the fields of the Wallet-Relying Party Registration Certificate are coherent with the interaction.
 
**Outcome**
 
- If all the steps succeed and the Wallet-Relying Party Registration Certificate is in the ``VALID`` state, the Wallet Unit MUST set ``authz_art_state`` to ``CERTIFICATE_VALID``.
- If any step fails, the Wallet Unit MUST set ``authz_art_state`` to ``CERTIFICATE_INVALID``. This is not a final authorization decision: it triggers :ref:`Register Query Validation <register-query-validation>` as fallback.
 
.. _register-query-validation:
 
**Register Query Validation**
 
When the Wallet-Relying Party Registration Certificate is not available or its validation has failed, the Wallet Unit MUST query the Register API:
 
1. **Extract the Registrar URL** from the Presentation Request, that is the ``verifier_info`` in the Remote Flow or the ``requestInfo`` in the Proximity Flow, or from the Credential Issuer Metadata, that is ``issuer_info[].registry_uri``, during Issuance.
2. **Connect** to the Registrar online service over HTTPS.
3. **Query** the service with the entity identifier and, optionally, the ``intended_use_id``. The entity identifier is the ``verifier_info[].data.identifier`` in the Remote Flow, the ``docRequest.itemsRequest[].requestInfo.EUWrpRegistrarInfo.identifier`` in the Proximity Flow, or the ``issuer_info[].data.identifier`` during Issuance.
4. **Format verification**: confirm that ``typ`` is ``jwt``, as defined in Section 5.2.1 of [`ETSI TS 119 475`_].
5. **Verify pertinence**: verify that the response pertains to the relevant Authorization Subject and intended use.
6. **Verify the response signature**: verify the Registrar signature using the Sign/Seal certificate carried in the ``x5c`` claim of the response.
7. **Trust Anchor validation**: validate the Registrars List of Trusted Entities (see :ref:`trust-evaluation-eudiw:List of Trusted Entities Validation`) and retrieve the Registrar Trust Anchor from its ``TrustedEntitiesList.ServiceDigitalIdentity`` field.
8. **Path validation**: validate the Registrar Sign/Seal certificate chain as defined in :ref:`trust-evaluation-eudiw:X509 Certificate Chain Validation Algorithm`, where ``C_1`` is the first certificate of the chain provided by the Registrar, ``C_n`` is the Registrar Sign/Seal Certificate, and the ``trust_anchor`` is the Trust Anchor obtained at the previous step.
9. **Normalize** the Register-derived data into the same internal model used for the Wallet-Relying Party Registration Certificate.
 
.. note::
 
    Even when the Relying Party requesting the presentation is a Relying Party Intermediary, the Presentation Request MUST carry the intermediated Relying Party data, as defined in [`ETSI TS 119 475`_].
 
**Outcome**
 
- If all the steps succeed, the Wallet Unit MUST set ``authz_art_state`` to ``REGISTER_VALID``.
- If any step fails, the Wallet Unit MUST set ``authz_art_state`` to ``FAILED``.
 
During Issuance only, the ``registrar_dataset`` self-declared data MAY be used as a further fallback, as advisory information only, and MUST NOT be presented to the User as verified.
 
Authorization Validation
"""""""""""""""""""""""""""""
 
The Authorization Validation MUST follow the Authorization Artifacts Validation when ``authz_art_state == REGISTER_VALID`` or ``authz_art_state == CERTIFICATE_VALID``. If ``authz_art_state == FAILED`` the Wallet Unit SHOULD NOT execute any Authorization Validation, as it cannot change the final Authorization Decision.
 
**Input**
 
The Wallet Unit MUST base the Authorization Validation only on:
 
- the authenticated Wallet-Relying Party and the interaction context, authoritative only for the identity of the Wallet-Relying Party;
- a validated Authorization Artifact, that is a Wallet-Relying Party Registration Certificate or a Register Response, authoritative for the subject identity, entitlements, intended use, registered scope, intermediary relationships, issuance-specific data and privacy policy references, as defined in [`ETSI TS 119 475`_];
- explicitly identified self-declared fallback information, non-authoritative;
- a verified Embedded Disclosure Policy, REQUIRED when provided by the Attestation Provider during Credential Issuance, authoritative when present.
 
Where authoritative sources conflict with non-authoritative sources, the authoritative sources MUST supersede. Where the authenticated Wallet-Relying Party context conflicts with the identity or the intermediary binding in the verified authorization context, the Wallet Unit MUST produce ``NOT_AUTHORIZED``, non-overridable. A request-carried Registrar URL MUST NOT be treated as sufficient proof of registered information by itself; it MAY be used only as a discovery hint unless confirmed by an authoritative source.
 
**Outcome**
 
The Wallet Unit MUST output the ``authz_val_state`` and ``edp_state`` variables, both initialized to ``none``.
 
**Process**
 
1. **Binding verification**. The Wallet Unit MUST ensure that the authenticated entity is the same as the entity described in the authorization data. The Wallet-Relying Party identity is the ``organizationIdentifier`` of the Wallet-Relying Party Access Certificate subject (clause 5.1.4 of [`ETSI EN 319 412-1`_]; the Wallet-Relying Party Access Certificate profile is defined in [`ETSI TS 119 411-8`_]).
 
    - **Credential Issuance**. The Wallet Unit MUST match the Credential Issuer identifier with the ``sub`` of the Wallet-Relying Party Registration Certificate or, if no Wallet-Relying Party Registration Certificate is available, with the ``identifier`` used in the Register query, and with the ``issuer_info.data.identifier`` of the Credential Issuer Metadata.
    - **Credential Presentation**. The Wallet Unit MUST first assume the **direct** scenario and match the Relying Party identifier with the ``sub`` of the Wallet-Relying Party Registration Certificate or, if not available, the ``identifier`` used in the Register query, and with the ``verifier_info.data.identifier`` of the Request Object in the Remote Flow or the ``docRequest.itemsRequest[].requestInfo.EUWrpRegistrarInfo.identifier`` in the Proximity Flow. If the match fails, the Wallet Unit MUST attempt the **intermediated** scenario and match the identifier against the ``intermediary.sub`` field carried in the Wallet-Relying Party Registration Certificate or in the Register Response.
 
    If the Binding verification fails, the Wallet Unit MUST stop the Authorization Validation and set ``authz_val_state`` to ``BINDING_FAILED``. If it succeeds, the Wallet Unit MUST make available to the User the identity of the Relying Party Intermediary, the identity or service description of the intermediated Relying Party, and the intended use of the request; how this information is presented is defined in the relevant User interaction sections of the IT-Wallet specification.
 
    .. note::
 
        If the Wallet Unit used only the Wallet-Relying Party Registration Certificate ``sub`` for the Binding verification and the outcome is ``BINDING_FAILED``, the Wallet-Relying Party Registration Certificate is not valid for this Relying Party. The Wallet Unit MUST query the Register, validate the response as described in :ref:`Register Query Validation <register-query-validation>`, and repeat the Binding verification.
 
2. **Entitlement verification**. The Wallet Unit MUST verify that the entitlements of the Authorization Subject match the expected role. The Wallet Unit MUST parse the ``entitlements`` field of the Wallet-Relying Party Registration Certificate or of the Register Response and check that it contains the entitlement URI expected for the interaction, among those defined in Annex A.2 of [`ETSI TS 119 475`_]:
 
    - ``https://uri.etsi.org/19475/Entitlement/PID_Provider`` for PID Providers, during PID Issuance;
    - ``https://uri.etsi.org/19475/Entitlement/QEAA_Provider`` for QEAA Providers, during QEAA Issuance;
    - ``https://uri.etsi.org/19475/Entitlement/PUB_EAA_Provider`` for PuB-EAA Providers, during PuB-EAA Issuance;
    - ``https://uri.etsi.org/19475/Entitlement/Non_Q_EAA_Provider`` for EAA Providers, during EAA Issuance;
    - ``https://uri.etsi.org/19475/Entitlement/Service_Provider`` for Relying Parties, during Credential Presentation.
 
    If the expected entitlement is not present, the Wallet Unit MUST set ``authz_val_state`` to ``WRONG_ENTITLEMENT``.
 
3. **Attestation Type verification**. During Credential Issuance, the Wallet Unit MUST verify that the PID or the Attestation Type being issued is registered for the Credential Issuer. A PID Provider issuing PIDs MAY skip this step. Otherwise the Wallet Unit MUST match the ``provides_attestations`` array of the Wallet-Relying Party Registration Certificate or of the Register Response (defined in Table 8 of [`ETSI TS 119 475`_]) against the ``credential_configurations_supported`` keys of the Credential Issuer Metadata ([`OpenID4VCI`_]). The match MUST be exact and case sensitive, on ``vct`` for SD-JWT VC and on ``doctype`` for mdoc. If not found, the Wallet Unit MUST set ``authz_val_state`` to ``ATTESTATION_TYPE_NOT_REGISTERED``.
 
4. **Scope Comparison**. During Credential Presentation, the Wallet Unit MUST verify that the requested Digital Credentials and attributes fall within the registered scope, carried in the ``credentials`` array of the Wallet-Relying Party Registration Certificate or of the Register Response (defined in Table 9 of [`ETSI TS 119 475`_]).
 
    - **Remote Flow**: extract the requested Digital Credentials and attributes from the ``dcql_query`` of the Request Object ([`OpenID4VP`_]) and match them against the ``credentials`` entries, comparing ``format`` and ``meta`` (``vct_values`` for SD-JWT VC) and the requested attributes against the ``claim`` paths.
    - **Proximity Flow**: extract the ``docType`` and the ``nameSpaces`` from the ``docRequests`` of the mdoc Request ([`ISO18013-5`_]) and match them against ``credentials[].meta.doctype_value`` and ``credentials[].claim`` respectively.
 
    The match MUST be exact and case sensitive. If any requested Digital Credential or attribute is not registered, the Wallet Unit MUST set ``authz_val_state`` to ``OVERASKING_DETECTED`` and identify the unregistered attributes or Digital Credentials.
 
    If all the checks above that apply to the interaction are satisfied, the Wallet Unit MUST set ``authz_val_state`` to ``VERIFICATION_PASSED``.
 
5. **Embedded Disclosure Policy evaluation**. During Credential Presentation, for each Digital Credential matching the Presentation Request, the Wallet Unit MUST check for a locally stored Embedded Disclosure Policy. If none exists, this check is superseded. Otherwise, according to the ``policy_type`` defined in Section 4.2.5 of [`ETSI TS 119 472-3`_]:
 
    - ``no_policy``: no restriction applies.
    - ``authorized_rp_only``: only the Relying Parties in the ``authorized_parties`` list are authorized. The Wallet Unit MUST compare the Relying Party subject DN of the Wallet-Relying Party Access Certificate against the ``subject_dn`` entries, and the Relying Party entitlements or sub-entitlements of the Wallet-Relying Party Registration Certificate against the ``entitlement_uri`` entries. A match on either criterion is sufficient.
    - ``specific_root_of_trust``: only the Relying Parties whose Wallet-Relying Party Access Certificate chain contains one of the ``trusted_roots`` are authorized. The Wallet Unit MUST match ``issuer_dn`` using LDAP DN comparison and ``serial_number`` using integer comparison.
 
    If the applicable check is satisfied, or no Embedded Disclosure Policy is present, the Wallet Unit MUST set ``edp_state`` to ``EDP_SATISFIED``; otherwise it MUST set ``edp_state`` to ``EDP_NOT_SATISFIED``.
 
**Outcome**
 
At the end of the Authorization Validation the Wallet Unit MUST output the ``authz_val_state`` and ``edp_state`` values. The table below summarizes the codes.
 
=====================  ===================================  ==============  ====================================================================================================================================
Variable               Code                                 Phase           Meaning
=====================  ===================================  ==============  ====================================================================================================================================
``authz_art_state``    ``CERTIFICATE_VALID``                both            The Wallet-Relying Party Registration Certificate format, signature, trust anchor and status are successfully verified.
``authz_art_state``    ``CERTIFICATE_INVALID``              both            A format, signature, trust anchor or status check fails on the presented registration certificate.
``authz_art_state``    ``REGISTER_VALID``                   both            The online Registrar query completed, and the response signature, pertinence and trust anchor passed.
``authz_art_state``    ``FAILED``                           both            The online Registrar query or response verification failed during the fallback procedures.
``authz_val_state``    ``WRONG_ENTITLEMENT``                both            The entitlements of the Authorization Subject do not match the expected role for the active context.
``authz_val_state``    ``BINDING_FAILED``                   both            The identity binding between the authenticated Wallet-Relying Party and the authorization data fails.
``authz_val_state``    ``ATTESTATION_TYPE_NOT_REGISTERED``  issuance        The Attestation Type being issued is not found in the Credential Issuer registered profiles.
``authz_val_state``    ``OVERASKING_DETECTED``              presentation    The Relying Party requests Digital Credentials, formats or namespaces that exceed its registered scope.
``authz_val_state``    ``VERIFICATION_PASSED``              both            Identity binding, entitlement verification, attestation matching and scope checking all passed.
``edp_state``          ``EDP_SATISFIED``                    presentation    No Embedded Disclosure Policy restriction applies, or the Relying Party satisfies the local policy.
``edp_state``          ``EDP_NOT_SATISFIED``                presentation    The Relying Party does not satisfy any locally stored Embedded Disclosure Policy.
=====================  ===================================  ==============  ====================================================================================================================================
 
The final Authorization Decision, ``AUTHORIZED`` or ``NOT_AUTHORIZED``, is elaborated from the ``authz_art_state``, ``authz_val_state`` and ``edp_state`` values, as defined in :ref:`trust-evaluation:Authorization Decision and Override Rules`.
 
.. plantuml:: plantuml/eudiw-authz-eval.puml
    :width: 99%
    :alt: Flowchart of the EUDIW Authorization Algorithm.
    :caption: Flowchart of the EUDIW Authorization Algorithm.

EUDIW Metadata Retrieval and Validation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Within the EUDIW Trust Framework the metadata of a Wallet-Relying Party are obtained through the protocol flow and their authenticity is established through the Wallet-Relying Party Access Certificate. This applies to Credential Issuance and to Credential Presentation in the Remote Flow. In the Proximity Flow no separate metadata retrieval is performed: the Relying Party identity is established through the mdoc reader authentication (see :ref:`trust-evaluation-eudiw:EUDIW Authentication`).

**Metadata Retrieval**

The Wallet Unit obtains the metadata of the Wallet-Relying Party according to the interaction:

- During Credential Issuance, the Credential Issuer Metadata is obtained from the Credential Issuer well-known metadata endpoint, as defined in [`OPENID4VCI`_] (see :ref:`credential-issuer-endpoint:Metadata Endpoints`).
- During Credential Presentation in the Remote Flow, the Relying Party metadata is carried in the Request Object of the authorization request, as defined in [`OpenID4VP`_] (see :ref:`remote-flow:Request Object`).

**Metadata Validation**

The authenticity of the retrieved metadata is established through the Wallet-Relying Party Access Certificate. The signed metadata artifact carries the ``x5c`` header with the certificate chain of the Wallet-Relying Party, and the Wallet Unit validates the signature and the certificate chain as defined in :ref:`trust-evaluation-eudiw:EUDIW Authentication`. The Wallet Unit MUST use only the metadata whose signature is verified against the authenticated Wallet-Relying Party Access Certificate.


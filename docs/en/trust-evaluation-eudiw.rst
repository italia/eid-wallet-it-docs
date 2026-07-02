Trust Anchor Validation Process
-------------------------------

This section specifies the **Trust Anchor Validation Process** that a Wallet Unit or Wallet-Relying Party (the validating Entity) uses to establish the cryptographic integrity and authenticity of a List of Trusted Entities, or a Trusted Lists in order to:

- validate the trustworthiness of a Trust Anchor (see :ref:`trust-artifact-eudiw:Trust Anchor Certificate Profile`) to authenticate, authorize or validate an entity or artifact during *runtime*.
- validate the information contained in the List for *historcal purposes*.

Depending on the Trust Artifact or Attestation being verified, the validating Entity MUST fetch, download, and validate the List which references the appropriate Trust Anchor:

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

- :ref:`trust-evaluation-eudiw:List of Trusted Entities Validation`: Validate the digital signature of the List of Trusted Entities by verifying it against the List of Trusted Entities Provider certificate. This certificate is authenticated via the Official Journal of the European Union.
- :ref:`trust-evaluation-eudiw:Trusted List Validation`: Validate the digital signature of the TL by verifying it against the corresponding Member State public keys published in the List Of Trusted Lists (LOTL). The List Of Trusted Lists (LOTL) itself is authenticated by validating its digital signature against the Official Journal of the European Union.

To support continuous key rotation and regular updates, the LoTE and LOTL implement a *pivoting mechanism*. This mechanism consists of publishing the most recent version of the List at the primary URI referenced in the Official Journal of the European Union, while archiving earlier versions at distinct URI *pivots*. Each List version is signed with a public key referenced within the immediately preceding version, rather than reusing the same key. The newest List version explicitly contains the URIs where all historical versions are hosted. An Entity validates this chain of pivots from the newest version back to the oldest by verifying that each subsequent artifact is correctly signed by the public key authorized in the prior version. Final validation is achieved by verifying the trustworthiness of the oldest public key, either via a lookup in the OJEU or directly against a cached, previously validated version of the List. This ensures that an entity possessing the last known valid version can reliably discover the next version and validate it via an unbroken chain of trust rooted in the OJEU.

**Input Model**

The validating Entity MUST base Trust Anchor validation decisions only on information derived from:

- The Official Journal of the EU (OJEU) anchoring trust in the root certificates that signed the Lists of Trusted Entities and List of Trusted Lists. The current version of OJEU can be found `here <https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ:C_202601944>`_.
- A validated Lists of Trusted Entities or List of Trusted Lists and Member State level Trusted Lists.

**Otput Model**

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

List of Trusted Entities Validation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section defines the validation of the EU-level List of Trusted Entities (List of Trusted Entities). The List of Trusted Entities is a digitally signed/sealed artifact (JWT format) containing metadata and public keys for entities operating at the EU level.

List of Trusted Entities Validation Algorithm
""""""""""""""""""""""""""""""""""""""""""""""

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
3. (Pivot Discovery) Iterate through the ``uriValue`` claims in the ``SchemeInformationURI`` object. Count the number of valid URIs found before encountering the URI matching ``OJEU-Loc``. Let $n$ be that count.

    - If no URI matches ``OJEU-Loc``: Validation MUST fail with ``LoTE-Status`` set to ``LoTE_VERIFICATION_FAILED`` and ``LoTE-Sub-Status`` set to ``OJEU_LOCATION_INPUT_NOT_MATCHING_OJEU_LOCATION_IN_LoTE``. (This may imply that a new version of the OJEU is available).

4. (LoTE Location Conflict) Check the condition: ``OJEU-LoTE-Loc != LoTE Location`` AND ``LoTE != Content at LoTE Location``.

    - (`LoTE Location`` is the URI in the ``PointersToOtherLoTE`` claim of ``LoTE`` with ``SchemeTerritory`` = ``EU``).
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

    - Case $n=0$ (No Pivots): Proceed directly to Step 8.
    - Case $n \neq 0$ (History Chain):

        - Iterate $i$ from 1 to $n$ (from most recent Pivot to oldest). Let ``Pivot`` be the file downloaded from the $i$-th URI.
        - (Link Check) Set ``Pivot-Certs-Set`` to the certificates in the ``PointersToOtherLoTE`` claim (territory ``EU``) of ``Pivot`. If ``LoTESO-Cert`` (the signer of the previous file in the chain) is not in ``Pivot-Certs-Set``, validation MUST fail with ``LoTE-Sub-Status`` set to ``PIVOT_i-1_SIGNER_CERT_NOT_AUTHENTICATED_BY_PIVOT_i``.
        - (Update Signer) Set ``LoTESO-Cert`` to the first certificate in the ``x5c`` header parameter of ``Pivot``.
        - (Verify Signature) Validate the signature of ``Pivot`` using ``LoTESO-Cert``. If it fails, validation MUST fail with ``LoTE-Status`` set to ``LoTE_VERIFICATION_FAILED``, and ``LoTE-Sub-Status`` set to ``PIVOT_i_SIGNATURE_VERIFICATION_FAILED``.
        - The loop continues, walking backwards until ``LoTESO-Cert`` represents the signer of the oldest Pivot.

8. (Trust Root Validation) Verify the end of the chain. If ``LoTESO-Cert`` (from the last Pivot or current LoTE List of Trusted Entitie) is not in ``OJEU-LoTE-Certs-Set`` (the Trust Anchor), validation MUST fail with ``LoTE-Sub-Status`` set to ``PIVOT_n_SIGNER_CERT_NOT_AUTHENTICATED_BY_OJEU``.

9. (Expiration) If current time is greater than the ``NextUpdate`` parameter's value of ``LoTE``, validation MUST fail.

10. (Success) Set ``Authenticated-LoTE`` to ``LoTE`, ``LoTE-Status`` to ``LoTE_VERIFICATION_PASSED``.

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
^^^^^^^^^^^^^^^^^^^^^^^^

This section defines the validation of Trusted List. In order to validate the Trusted List, the Wallet Unit MUST:

1. Validate the EU List of Trusted Lists using the algorithm described in section 4.1 of [`ETSITS119615`_]. If this fails, the validation stops and the Wallet Unit MUST consider the Entity it is interacting with as not trusted. The validation process is analogue to the validation of the :ref:`trust-evaluation-eudiw:List of Trusted Entities Validation Algorithm` except for the LOTL format which is always XML.
2. Parse the validated EU List of Trusted Lists to discover the necessary certificate to validate the relevant Member State Trusted List.
3. Obtain and validate the relevant Trusted List as described in section 4.2 of [`ETSITS119615`_].

Authentication Process
----------------------

The **Authentication Process** enables the Wallet Unit to authenticate a Wallet-Relying Party during an interaction. It establishes trust by validating the Wallet-Relying Party's X.509 certificate chain, starting from a trusted Provider of Wallet-Relying Party Access Certificate down to the presented Wallet-Relying Party Access Certificate, and verifying the Wallet-Relying Party's possession of the corresponding private key.

To authenticate the Wallet-Relying Party, the Wallet Unit MUST verify the authenticity and integrity of the presented Wallet-Relying Party Access Certificate by performing the following steps:

1. **Verify the Signature:** Use the public key from the validated Wallet-Relying Party Access Certificate to verify the WRP's signature on the metadata presented during the specific interaction.

    - During Credential, the Wallet Unit MUST obtain the Credential Issuer Metadata, extract the ``x5c`` claim value from the header and verify the Credential Issuer Metadata signature using the top certificate of the certificate chain (i.e., the one whose subject DN corresponds to the Credential Issuer's name).
    - During Credential Presentation,

        - if the Presentation follows the Remote Flow, the Wallet Unit MUST extract the ``x5c`` claim value from the header of the Request Object and verify the Request Object's signature using the top certificate of the certificate chain (i.e., the one whose subject DN corresponds to the Credential Issuer's name).
        - if the Presentation follows the Proximity Flow, the Wallet Unit MUST extract the ``readerAuthAll[].33`` (or alternatively ``readerAuth[].33``) claim value from the mdoc Request and check its signature using the top certificate of the certificate chain (i.e., the one whose subject DN corresponds to the Credential Issuer's name).

2. **Construct the Certification Path:** Build a path starting from the certificate issued by the Provider of WRPAC ($C_1$) and ending with the Wallet-Relying Party Access Certificate presented by the WRP ($C_n$). *(Note: The simplest path consists of just one certificate, where $n=1$).*

3. **LoTE Validation:** Retrieve the WRPAC Trust Anchor that anchors the root of the certificate path from the validated List of Trusted Entities (see :ref:`trust-evaluation-eudiw:List of Trusted Entities Validation`).

4. **Trust Anchor Retrieval:** To retrieve the correct Trust Anchor, the Wallet Unit MUST:
    
    - match the ``issuer.organizationIdentifier`` field value of certificate $C_1$ with the ``TrustedEntityList[].TrustedEntity.TETradeName`` field value of the LoTE; and
    - use the certificates found in the ``TrustedEntityServices[].ServiceInformation.ServiceDigitalIdentity`` field as the Trust Anchor.

5. **Execute Path Validation:** Run the algorithm defined in :ref:`trust-evaluation-eudiw:X509 Certificate Chain Validation Algorithm` as described in :ref:`trust-evaluation-eudiw:Wallet-Relying Party Access Certificate Validation`.

.. warning::

    Implementers:
    
        -  SHOULD consider strategies to cache validated Lists of Trusted Lists, Lists of Trusted Entities, and Member States' Trusted Lists to allow the Wallet Unit to correctly process the Authentication Validation. The frequency of updates and the types of lists that should be cached represent a trade-off between interoperability and resource utilization.
        
        - MUST distinguish between transient authentication (e.g., access control) and content commitment (non-repudiation). To prevent an attacker from disguising a legal commitment as a protocol nonce, the WRP MUST NOT use the Wallet-Relying Party Access Certificate private key to sign arbitrary data that could be controlled by an external party.


**Input Model**

The Wallet Unit's Authentication output MUST be based only on information derived from:

- The appropriate Trust Anchor obtained from a valid instance of the Provider of WRPAC LoTE;
- The X509 certificate path terminating with the WRPAC end-entity certificate;
- A Wallet-Relying Party signature over some data carrying the proof of possession of the private key referenced in the WRPAC. 

**Output Model**

The Wallet Unit MUST output a decision from the Authentication process: the Wallet-Relying Party can either be ``AUTHENTICATED`` or ``NON_AUTHENTICATED``. In the first case, the Wallet Unit SHOULD proceed in the interaction flow with the Wallet-Relying Party; in the second, the Wallet Unit MUST inform the User that the identity of the Wallet-Relying Party could not be verified and MUST stop the interaction flow as the entity is not trustworthy.

Wallet-Relying Party Access Certificate Validation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Entity performing Wallet-Relying Party Access Certificate validation initializes the algorithm in :ref:`trust-evaluation-eudiw:X509 Certificate Chain Validation Algorithm` as follows:

- The ``path`` is the sequence of $n$ certificates ($C_1, \dots, C_n$) provided by the Wallet-Relying Party, where:

    - $C_1$ is the root certificate.
    - $C_n$ is the Wallet-Relying Party Access Certificate (the target certificate).
    - For any $i$ in $1, \dots, n-1$, $C_i$ is the issuer of $C_{i+1}$.

- The ``trust_anchor`` MUST be the key and subject identifier of a certificate of the Provider of Wallet-Relying Party Access Certificate obtained from the List of Trusted Entities. This certificate MUST either be exactly $C_1$ or contain the public key used to sign $C_1$.

EUDIW Authorization Process
----------------------------

This section specifies the EUDIW Authorization Process that a Wallet Unit MUST execute to determine whether an interaction with a Wallet-Relying Party is allowed within the EUDI Wallet ecosystem. A Wallet Unit compliant with this specification MUST implement all the authorization-processing rules defined in this section. The EUDIW Authorization Process MUST start only *after* the Wallet Unit has been successfully authenticated the WRP according to :ref:`trust-evaluation-eudiw:Authentication Process`. If the WRP has not been authenticated (i.e. the :ref:`trust-evaluation-eudiw:Authentication Process` has failed), the EUDIW Authorization Process MUST NOT start as the other entity is deemed untrustworthy.

The EUDIW Authorization Process is split into:
- :ref:`trust-evaluation-eudiw:Authorization Artifacts Validation` which validates integrity and authenticity of the Trust Artifact carrying the authorization data; and
- :ref:`trust-evaluation-eudiw:Authorization Validation` which validates the information content of the validated artifact. In particular, this validation process covers:

    - **Issuance authorization**: Determines whether a Credential Issuer is registered for the relevant role and authorized to issue the specific Digital Credential. This applies to PID, QEAA, PuB-EAA, and EAA Providers operating within the EUDIW ecosystem.
    - **Presentation authorization**: Determines whether a Relying Party's request falls within its registered scope, whether an Embedded Disclosure Policy permits the disclosure, and whether the User approves.This applies to interactions involving both Relying Parties and Relying Party Intermediaries, across both Remote and Proximity Flows.

- :ref:`trust-evaluation:Authorization Decision and Override Rules` which outputs an *Authorization Decision* expressed as ``AUTHORIZED`` or ``NOT_AUTHORIZED`` on the base of the Authorization Artifacts Validation and Authorization Validation results. Depending on the Flow type the User MAY *override* the Authorization Decision.

Within the *Authorization Validation*, the Wallet Unit MUST distinguish between the authenticated WRP and the *Authorization Subject*. The latter being the entity whose authorization is being evaluated:

- During Issuance, the authorization subject is the Credential Issuer.
- During *direct* presentation, the authorization subject is the Relying Party.
- During *intermediated* presentation, the authorization subject is the *intermediated RP*, while the authenticated WRP is the Relying-Party Intermediary.

The Wallet Unit MUST support authorization-context resolution from both a Wallet-Relying Party Registration Certificate (where available) and the Register (where a Wallet-Relying Party Registration Certificate is not available or cannot be relied upon). The substantive authorization logic MUST NOT change based on the data source. Where both sources are available, the Wallet Unit MUST normalize both into the same internal authorization model before applying rules.

Authorization Artifacts Validation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section defines the validation procedures for the Authorization Artifacts that are exchanged in the various flows. The Artifacts that carry the Authorization data of an entity are the Wallet-Relying Party Registration Certificate and the Register Response. Both carry equivalent information albeit in different formats. The Wallet Unit MUST support the validation of both and MUST validate at least one of the two. Each validation procedure is self-contained: it specifies its inputs, its processing logic, and its output (a verification result code). The Authorization Artifacts Validation result MAY be overridden by the User under the conditions detailed in the :ref:`trust-evaluation-eudiw:Override Rules` section.

The Validation flow that the Wallet Unit performs, depends on the availability of the Wallet-Relying Party Registration Certificate in the interaction with the Wallet-Relying Party. 

- During the Presentation flow, the Relying-Party MAY include the Wallet-Relying Party Registration Certificate in the Presentation Request. In case, depending on the Presentation type, i.e., remote or proximity; the Relying-Party MUST include the Wallet-Relying Party Registration Certificate by value in the:

    - ``verifier_info`` parameter included in the Request Object JWT within the authorization request (see [`ETSITS119472-2`_] and Section 5.1 of [`OpenID4VP`_]). This is an array of JSON Objects containing Wallet-Relying Party Registration Certificate in base64-encoded format and data including the URL of Registrar online service.
    - ``euwrprc`` CBOR byte string with serialized Wallet-Relying Party Registration Certificate member of ``requestInfo`` included in the ISO ``DeviceRequest`` Proximity Flow, Section 5.3 [`ETSITS119472-2`_].

     !!! warning

        Currently, the mapping of `EIDAS-ARF`_ HRL RPRC_19a data in the ``requestInfo`` map is not defined in [`ETSITS119472-2`_]

- During the Issuance flow, the Credential Issuer includes authorization data in the Credential Issuer Metadata through the ``issuer_info`` array (Section 4.2.3 of [`ETSITS119472-3`_]). This array contains:

    - [OPTIONAL] A ``registration_cert`` element containing the Wallet-Relying Party Registration Certificate by value (ISS-MDATA-REG_CERT-4.2.3-04/05) (OPTIONAL).
    - [REQUIRED] An element with format ``registrar_dataset`` containing self-declared registration information including ``identifier``, ``srvDescription``, ``registryURI`, and ``providesAttestations``.

     Metadata is signed with the Attestation Provider Wallet-Relying Party Access Certificate private key (ISSU_22a). Authorization data contained in the Embedded Disclosure Policy is also distributed through the Credential Issuer Metadata within ``credential_configurations_supported`` field.

In case the Wallet-Relying Party Registration Certificate is not available, or its validation fails, the Wallet Unit MUST use the entity identifier and, OPTIONALLY, the ``intended_use_id`` (``presentation``) or (``issuance``). use the Registrar URL and query this service using the entity unique identifier and, for presentation, the ``intended_use_id``.

The response provides the same authorization-relevant data as a Wallet-Relying Party Registration Certificate. Each Registrar provides an online service available through an API interface, obtained as described in the :ref:`trust-artifact-eudiw:Common Register Open APIs` section. When using this service, the Wallet Unit SHOULD inform the User that an external query will be made.

Wallet Relying Party Registration Certificate Validation 
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

When a Wallet-Relying Party Registration Certificate is available, the Wallet Unit MUST validate it before relying on it:

1. **Format verification**: confirm ``typ`` is ``rc-wrp+jwt`` (remote flow) or ``rc-wrp+cwt`` (proximity flow) (Section 5.2.1 of [`ETSITS119475`_]).
2. **Algorithm verification**: verify the conformance of signature algorithm (``alg`` neither ``none`` nor deprecated).
3. **Signature validation**: verify that the Wallet-Relying Party Registration Certificate signature is valid.
4. **Trust Anchor validation**: Validate the Providers of WRPRC List of Trusted Entities (see :ref:`trust-evaluation-eudiw:List of Trusted Entities Validation`) and retrieve the WRPRC Trust Anchor (found in the ``TrustedEntitiesList.ServiceDigitalIdentity`` field of the Providers of WRPRC List of Trusted Entities) that anchors the root of the certificate path.
5. **WRPRC validation**: initialize the algorithm in :ref:`trust-evaluation-eudiw:X509 Certificate Chain Validation Algorithm` as follows:

    - The ``path`` is the sequence of $n$ certificates ($C_1 \dots C_n$) provided by the Wallet-Relying Party, where:

        - $C_1$ is the certificate issued by the Provider of WRPRC.
        - $C_n$ is the Wallet-Relying Party Registration Certificate (the target certificate).
        - For any $i$ in $1 \dots n-1$, $C_i$ is the issuer of $C_{i+1}$.

    - The ``trust_anchor`` MUST be a certificate of the Provider of Wallet-Relying Party Registration Certificates obtained from the List of Trusted Entities. This certificate MUST either be exactly or be used to sign/seal $C_1$.

6. **Temporal validity**: check ``iat`` and ``exp`` (if present).
7. **Status verification**: check revocation status via the ``status`` field of the WRPRC.
8. **Coherence check**: verify Wallet-Relying Party Registration Certificate subject and fields are coherent with the scenario.

**Output Model**

 - If all of the above steps succeeds and the Wallet-Relying Party Registration Certificates is in ``VALID`` state, the Wallet Unit MUST set the ``authz_art_state`` to ``CERTIFICATE_VALID``.
 - If any step fails, the Wallet Unit MUST set the ``authz_art_state`` to ``CERTIFICATE_INVALID``. This is not a final authorization decision; it triggers the :ref:`trust-evaluation-eudiw:Register Query Validation` as fallback.

Register Query Validation
""""""""""""""""""""""""""""

When the Wallet-Relying Party Registration Certificate is not available or validation has failed, the Wallet Unit MUST attempt to contact the Register APIs:

1. **Extract Registrar URL** from the Presentation Request (``verifier_info`` in remote scenario or ``requestInfo`` in proximity scenario) during presentation flow, or from the Credential Issuer Metadata (``issuer_info[].registry_uri``) during issuance flow.
2. **Connect** to the Registrar online service using HTTPS.
3. **Query** the Registrar service using the entity identifier and, OPTIONALLY, the ``intended_use_id`` (``presentation``) or (``issuance``).

    - During the Presentation flow the entity identifiers is either the value of the ``verifier_info[].data.identifier`` parameter in the Request object for the Remote flow, or the value of the ``docRequest.itemsRequest[].requestInfo.EUWrpRegistrarInfo.identifier`` parameter in the mdoc Request.
    - During the Issuance flow the entity identifier is the value of the ``issuer_info[].data.identifier`` parameter.
 
4. **Format verification**: confirm ``typ`` is ``jwt`` (Section 5.2.1 of [`ETSITS119475`_]).
5. **Verify pertinence**: the Wallet Unit MUST verify that the response pertains to the relevant authorization subject and intended use.
6. **Verify response signature**: verify that the Registrar signature in the response is valid using the Sign/Seal certificate of the Registrar in the ``x5c`` claim of the response.
7. **Trust Anchor validation**: Validate the Registrars List of Trusted Entities (see :ref:`trust-evaluation-eudiw:List of Trusted Entities Validation`) and retrieve the Registrar Trust Anchor (found in the ``TrustedEntitiesList.ServiceDigitalIdentity`` field of the Registrar List of Trusted Entities) that anchors the root of the certificate path.
8. **Sign/Seal certificate validation**: initialize the algorithm in :ref:`trust-evaluation-eudiw:X509 Certificate Chain Validation Algorithm` as follows:

    - The ``path`` is the sequence of $n$ certificates ($C_1 \dots C_n$) provided by the Registrar, where:

        - $C_1$ is the root certificate.
        - $C_n$ is the Registrar's Sign/Seal Certificate (the target certificate).
        - For any $i$ in $1 \dots n-1$, $C_i$ is the issuer of $C_{i+1}$.

    - The ``trust_anchor`` MUST be a certificate of the Registrar obtained from the List of Trusted Entities. This certificate MUST be the Trust Anchor certificate of the Provider of WRPRC which issued certificate $C_1$.

9. **Normalize** Register-derived data into the same internal model used for Wallet-Relying Party Registration Certificate data.

.. note::

    As per RPRC_19a in the `EIDAS-ARF`_, even if the Relying Party requesting the presentation is a Relying Party Intermediary, it MUST use the intermediated Relying Party data in the Presentation Request.

**Output Model**

 - If all of the above steps succeeds, the Wallet Unit MUST set the ``authz_art_state`` to ``REGISTER_VALID``.
 - If any of the above steps fails, the Wallet Unit MUST set the ``authz_art_state`` to ``FAILED``.

**Three-tier fallback (issuance only)**: self-declared data from ``registrar_dataset`` (advisory only, MUST NOT be presented as verified).

Authorization Validation
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Wallet Unit's Authorization Validation procedure MUST follow the Authorization Artifacts Validation when ``authz_art_state == REGISTER_VALID`` or ``authz_art_state == CERTIFICATE_VALID``. If ``authz_art_state == FAILED``, the Wallet Unit SHOULD NOT execute any Authorization Validation procedure as it cannot change the final Authorization Decision outcome.

**Input Model**

The Wallet Unit MUST base Authorization Validation only on information derived from:

- The Authenticated WRP and the interaction context.
- A validated Authorization Artifact (either the Wallet-Relying Party Registration Certificate or a Register-derived response).
- Explicitly identified self-declared fallback information.
- A verified Embedded Disclosure Policy, REQUIRED when provided by the Attestation Provider during Credential Issuance.

The Wallet Unit MUST maintain an internal distinction between the following input classes:

- **Authenticated WRP context**: authoritative only for the identity of the WRP.
- **Verified information derived from a Wallet-Relying Party Registration Certificate or Register**: Authoritative for the subject's identity, entitlements, intended use, registered scope, intermediary relationships, issuance-specific data, and privacy policy references.
- **Self-declared information**: non-authoritative. The Wallet Unit MUST NOT rely solely on self-declared information for checks that require registered information.
- **Verified Embedded Disclosure Policy**: Authoritative when present. If available, the Wallet Unit MUST rely on this policy to determine access permissions.

Where authoritative sources conflict with non-authoritative sources, the authoritative sources MUST supersede. Where the authenticated WRP context conflicts with the identity or intermediary binding in the verified authorization context, the Wallet Unit MUST produce ``NOT_AUTHORIZED`` (non-overridable).

A request-carried Registrar URL MUST NOT be treated as sufficient proof of registered information by itself; it MAY be used only as a discovery hint unless confirmed by an authoritative source.

**Output Model**

The Wallet Unit MUST output the variables ``authz_val_state`` and ``edp_state`` to indicate the final state of the Authorization Validation procedure. The initialization values of ``authz_val_state`` and ``edp_state`` MUST be ``none``.

Authorization Validation Procedure
""""""""""""""""""""""""""""""""""""

To validate the Authorization profile of a Wallet-Relying Party, the Wallet Unit MUST perform the following steps:

1. **Binding verification**. The Wallet Unit MUST ensure that the authenticated entity is the same as the entity described in the authorization data. The types of checks depend on the flow as well as the context.

    - **Credential Issuance**. The Wallet Unit MUST match the Credential Issuer identifier extracted from the Wallet-Relying Party Access Certificate subject in the ``subject.organizationIdentifier`` (clause 5.1.4 in `ETSIEN319412-1`_) with 
    
        - the Credential Issuer's WRPRC ``sub`` field's value; or,
        - in case no WRPRC is available, the Credential Issuer ``identifier`` value used in the GET request (``/wrp/{identifier}``) to the Register endpoint; and
        - the ``issuer_info.data.identifier`` field's value from the Credential Issuer Metadata's payload.

     If any checks fail, the Wallet Unit MUST set the ``authz_val_state`` to ``BINDING_FAILED``.

    - **Credential Presentation**. The Wallet Unit MUST extract the Relying Party identifier from the Wallet-Relying Party Access Certificate subject in the ``subject.organizationIdentifier`` (clause 5.1.4 in `ETSIEN319412-1`_).
    
     The Wallet Unit first assumes the **No intermediary** scenario. The Wallet Unit MUST match the extracted Relying Party identifier with

        - the Relying Party's WRPRC ``sub`` field's value; or,
        - in case no WRPRC is available, the Relying Party ``identifier`` value used in the GET request (``/wrp/{identifier}``) to the Register endpoint; and
        - the ``verifier_info.data.identifier`` field's value from the Request Object's payload during the Remote flow; or,
        - the ``docRequest.itemsRequest[].requestInfo.EUWrpRegistrarInfo.identifier`` field in the mdoc Request during the proximity flow.

     If any checks fail, it is possible that the Presentation happens in the **Intermediary** scenario, where the Presentation Request is intermediated by a Relying Party Intermediary. The Wallet Unit MUST attempt to match the Relying Party identifier extracted from the WRPAC (``subject.organizationIdentifier``) with 
        - the Relying Party Intermediary's ``intermediary.sub`` field's value (in either the WRPRC or Register Response depending on availability);

If the Binding verification fails, the Wallet Unit MUST stop the Authorization Validation Procedure and set the ``authz_val_state`` to ``BINDING_FAILED``. 

If the Binding verification succeedes, the Wallet Unit MUST display to the User both the Intermediary identity and the intermediated RP identity. The display SHOULD follow the pattern: 

- *"[``intermediary.sname``] acting on behalf of [``verifier_info.data.srvDescription``] for [``verifier_info.data.intendedUseIdentifier``]"* when in Remote flow.
- *"[``intermediary.sname``] acting on behalf of [``docRequest.itemsRequest[].requestInfo.EUWrpRegistrarInfo.srvDescription``] for [``docRequest.itemsRequest[].requestInfo.EUWrpRegistrarInfo.intendedUseIdentifier``]"* when in proximity flow.

.. note::
    
    If the Wallet used only the Wallet-Relying Party Registration Certificate ``sub`` for the Binding Verification, and ``authz_val_state == BINDING_FAILED``, the WRPRC is not valid for this Relying Party. The Wallet Unit MUST attempt to query the Registrar URI, validate the response as described in :ref:`trust-evaluation-eudiw:Register Query Validation`, and repeat the binding procedure.

.. note::

    The Registrar online service API, including the specific parameters for querying intermediary relationships, is defined in TS5. This specification does not define the Register API; it only defines how the Wallet Unit uses the Register response for authorization purposes.

2. **Entitlement Verification**. The Wallet Unit MUST verify that the entitlements of the authorization subject match the expected role. The Wallet Unit MUST parse the ``entitlement`` field from the WRPRC or the ``data.entitlements`` field from Register response's payload, and MUST check that its value is equal to:

    - ``https://uri.etsi.org/19475/Entitlement/PID_Provider`` for PID Providers in the context of PID Issuance;
    - ``https://uri.etsi.org/19475/Entitlement/Q_EAA_Provider`` for QEAA Providers in the context of QEAA Issuance;
    - ``https://uri.etsi.org/19475/Entitlement/PuB_EAA_Provider`` for PuB-EAA Providers in the context of PuB-EAA Issuance;
    - ``https://uri.etsi.org/19475/Entitlement/Non_Q_EAA_Provider`` for EAA Providers in the context of EAA Issuance;
    - ``https://uri.etsi.org/19475/Entitlement/Service_Provider`` for Relying Parties in the context of Credential Presentation.

     If the ``entitlements`` array does not contain the expected value, the Wallet Unit MUST set the ``authz_val_state`` to ``WRONG_ENTITLEMENT``.

3. **Attestation Type Verification**. During Credential Issuance, the Wallet Unit MUST verify that the PID or Attestation Type being issued is registered for the Credential Issuer:

    - For a PID Provider issuing PIDs, the Wallet Unit MAY skip this step.
    - Otherwise, the Wallet Unit MUST match 
    
        - the ``provides_attestations[]`` (in the WRPRC) or ``data.providesAttestations`` (in the Registrar Response) array against the ``credential_configurations_supported`` keys in the Credential Issuer Metadata. Matching MUST be case-sensitive and exact (``vct_value`` for SD-JWT VC, ``doctype`` for mDL).

     If not found, the procedure MUST output ``ATTESTATION_TYPE_NOT_REGISTERED``.

4. **Scope Comparison**. During Credential Presentation, the Wallet Unit MUST verify that the PID or Attestation Type being requested is registered for the Relying Party. Depending on the flow, the Wallet Unit MUST:

    - **Remote Flow**: extract the requested attributes from the Request Object ``dcql_query.credentials[]`` and match them against the ``credentials[]`` or ``data.credentials[]`` claims of either the WRPRC or the Register Query Response.
    - **Proximity Flow**: extract ``docRequests.itemsRequest[].nameSpaces``, from the mdoc Request and match them against the ``credentials[]`` or ``data.credentials[]`` claims of either the WRPRC or the Register Query Response

        - extract the ``docRequests.itemsRequest[].docType`` array from the mdoc Request and match it against the ``credentials[].meta.doctype_value`` or ``data.credentials[].meta.doctype_value`` claims of either the WRPRC or the Register Query Response.
        - extract the ``docRequests.itemsRequest[].nameSpaces{}`` objects from the mdoc Request and match it against the objects in the ``credentials[].claim[]`` or ``data.credentials[].claim[]`` array of either the WRPRC or the Register Query Response.

     If some of these checks fail, the Wallet Unit MUST set the ``authz_val_state`` to ``OVERASKING_DETECTED`` and identify the unregistered attributes or Digital Credentials.

If all of the above checks (when required) are satisfied, the Wallet Unit MUST set the ``authz_val_state`` to ``VERIFICATION_PASSED``.

.. warning ::

    1. The code names may be changed a bit...

    2. unsure about the value of constraining the implementation algorithm that much...

5. **EDP Evaluation**. During Credential Presentation, for each Digital Credential matching a Presentation Request, the Wallet Unit MUST check for a locally stored Embedded Disclosure Policy. If no Embedded Disclosure Policy exists, this check is superseded. Otherwise, if the Embedded Disclosure Policy are present and 

    - ``policy_type = no_policy``; no restriction applies.
    - ``policy_type = authorized_rp_only``; only **Authorized Relying Parties** within the ``authorized_parties[]`` list can be authorized for the Presentation. The Wallet Unit MUST compare the Relying Party subject DN from Wallet-Relying Party Access Certificate against ``subject_dn`` entries, and/or compare the RP entitlements or sub-entitlements from Wallet-Relying Party Registration Certificate against ``entitlement_uri`` entries. A match on either criterion is sufficient.
    - ``policy_type = specific_root_of_trust`` only Relying Parties whose WRPAC trust chain contains one of the ``trusted_roots[]`` array of objects can be authorized for the Presentation. The Wallet Unit MUST compare against the ``trusted_roots`` list and match ``issuer_dn`` using LDAP DN comparison and ``serial_number`` using integer comparison (as defined in ISS-MDATA-EBD-4.2.5.2-09, [`ETSITS119472-3`_]). 
    
     If either of these checks is satisfied or no EDP are present, the Wallet Unit MUST set the ``edp_state`` to ``EDP_SATISFIED``; on the contrary, if none are satisfied the Wallet Unit MUST set the ``edp_state`` to ``EDP_NOT_SATISFIED``.


**Output Model**

At the end of the Authorization Validation, the Wallet Unit MUST output the ``authz_val_state`` and ``edp_state`` values. The table below sums up the various codes values.

=====================  ===================================  ==============  ====================================================================================================================================
Variable               Code                                 Phase           Meaning
=====================  ===================================  ==============  ====================================================================================================================================
``authz_art_state``    ``CERTIFICATE_VALID``                both            The Wallet-Relying Party Registration Certificate format, signature, trust anchor, and status are successfully verified.
``authz_art_state``    ``CERTIFICATE_INVALID``              both            Any format, signature, trust anchor, or status validation check fails on the presented registration certificate.
``authz_art_state``    ``REGISTER_VALID``                   both            The online Registrar query successfully completed, and the response signature, pertinence, and trust anchor passed.
``authz_art_state``    ``FAILED``                           both            The online Registrar query or response verification failed completely during the fallback procedures.
``authz_val_state``    ``WRONG_ENTITLEMENT``                both            The parsed entitlements of the authorization subject do not match the expected ecosystem role for the active context.
``authz_val_state``    ``BINDING_FAILED``                   both            Cryptographic binding check or identity cross-reference fails between the authenticated WRP and the authorization data.
``authz_val_state``    ``ATTESTATION_TYPE_NOT_REGISTERED``  issuance        The requested PID or Attestation type being issued is not found in the Credential Issuer's registered profiles.
``authz_val_state``    ``OVERASKING_DETECTED``              presentation    The Relying Party requests credential types, formats, or namespaces that exceed its registered data access scope.
``authz_val_state``    ``VERIFICATION_PASSED``              both            All structural identity binding, entitlement verification, attestation matching, and scope checking passed.
``edp_state``          ``EDP_SATISFIED``                    presentation    No Embedded Disclosure Policy restriction applies, or the Relying Party satisfies the local policy constraints.
``edp_state``          ``EDP_NOT_SATISFIED``                presentation    The Relying Party attributes or trust chain roots fail to meet any locally stored Embedded Disclosure Policy constraints.
=====================  ===================================  ==============  ====================================================================================================================================

The diagram below illustrates the various steps of the Authorization Process and its algorithms.

.. plantuml:: plantuml/eudiw-authz-eval.puml
    :width: 99%
    :alt: The figure illustrates the Flowchart of the EUDIW Authorization Algorithm.
    :caption: `Flowchart of the EUDIW Authorization Algorithm. <https://www.plantuml.com/plantuml/png/hPRFSjis4CRlV8eTvs8VghPnq_XFaeQIePHJLrP9rfwUD0YuaZ2c00q0Ag4xUVS2XAaW1ktuK7g65e5lTxzT_q3hlJPKcMPJ9_gMYorLT0FQj3NQk-BimKxA3DznquufkrqfsOXg8ckfuCNqrFqCAQMgKDshZhihKCrjRMwu5552Cfw-ceu7fM76bwSdFut3kZDfC7P7fgVaTP9qlIR9MTgODGh36JK8D_aS3alLQ0DaH-k6kY97vmbVmg7R2yNLRqVWdk1GoAC4uEm2SGDkrxJG2EEoV9BAhDjpkwkDt2POQuJ35lLHWgBYooJPzft0WSij5R_hQa9grvUK6GtNjEPLjtW0_zfCpakcdTLy0dH7UKq_rjYRyTd1NgxhBHpSqBf6yqEETSl5gXjT2pckk3RAbvgWgzNr51LprzdF8vXAjQ46TgYyqWhE--sN8qZhbRLkrfjXnV482huIr3GAOUTBXFk_ZC0FFHNCpc18ycfqtp5RKow65B_Q9BZPIaLhlyrDkzzyRHqOMryF6pmPmKIkKQ5WQ2iWk_LRNxgxlVcnftNjNNYD1jqmXbelcpgUlqqx8NcPJRD9MfB5TNgPNPo_UVEYObYnatVlEf4dGiZ1a6os3rek6Vjut0Trx3mCFgCMeBi5LMQXRQi8Rq58WQuH7t3FJYHx2mD5uIg_RrL8ynMpnoZpGA62lnfKxQCOaSz6MQZt_2duExyCGPf88T0AZ0mqEqxXzxAS5o5Glb2ZBTJzeUCL2aSoge2i8NH3ggxTUWjRTmW42eO1KFscGhsLGYFedk8GhE-XU-Bf_x50IoOB3jk0zdG4C-UtvdS8bQs-mmgiXlOyViDYF_LdufYJ3rbHalovB4xJx98y3p-_PkqzWx0zNmEwRoq-QEAnbsM06yoLj3qr2dlmafwzCHULW-Kw0c4_qruIpp4SopYRNMIp3uj7nkFVzS54dVi0SU9WhN63miHUl9lUJo3LO25cwzYFotgJNra_P5PcvINvq_wEJ4LUWag-LYOCAigw8Kvh-GdATelxSfdM3HKC--3-5AR6e3P-z2uWwYYgvQk5SJt5qN_Ke5HQbgGeqpAxcYtAV-PaCRig5pqiGt-4gESmspN9FOmktJmj2XAV1e2GzQWDdtgkKAFmVOGrt7kdO7ABC94RYotNJqx3IybdXbW5KuYDNrddQV67e--2b6HIVgTr8V__plrharpCWwz8J_JcX8KLwIN72gI2cUo2jtvqJpHhLOl2EYscMUGoQZCEjOI4uU6KuYQZ9_yv_FGb-LhChoNTGNzl7vfD_Hy0>`_


The final Authorization Decision (i.e., ``AUTHORIZED`` or ``NOT_AUTHORIZED``) is elaborated on input the values of the ``edp_state`, ``authz_val_state`` and ``authz_art_state``. More details are found in the :ref:`trust-evaluation:Authorization Decision and Override Rules` section.

X509 Certificate Chain Validation Algorithm
-------------------------------------------

This section defines the algorithm of the certification path validation as in :rfc:`5280` and :rfc:`6960`. The Entity performing validation MUST initialize the algorithm with:

- ``path``: The sequence $C_1 \dots C_n$.
- ``trust_anchor``: The *trusted certificate* obtained from the ``ServiceDigitalIdentity`` component after validation of the relevant List of Trusted Entities.
- ``current_time``: The current date and time.

**Step 1: Initialization**
Initialize the state variables:

- ``valid_policy_tree``: A single node (depth 0, ``valid_policy``= ``anyPolicy``, ``qualifier_set``=``{}``, ``expected_policy_set``=``{anyPolicy}``).
- ``explicit_policy`` (how many certificates in the chain are allowed to lack a specific, valid policy): $n+1$.
- ``inhibit_any_policy`` (how many certificates are allowed to use the ``anyPolicy`` OID): $n+1$ (no inhibition of policies allowed).
- ``policy_mapping``: $n+1$ (no policy mapping allowed).
- ``working_public_key``: The public key of the ``trust_anchor``.
- ``working_public_key_parameters``: The parameters of the ``trust_anchor`` public key.
- ``working_issuer_name``: The subject Distinguished Name (DN) of the ``trust_anchor``.
- ``max_path_length``: $n$.

**Step 2: Certificate Processing**
Iterate through the path for $i$ from $1$ to $n$:

1. Basic Integrity & Binding Checks:

    - Verify the signature of $C_i$ using ``working_public_key``, ``working_public_key_parameters``, and the algorithm identifier.
    - Ensure ``current_time`` falls within the ``notBefore`` and ``notAfter`` validity period of $C_i$.
    - Check revocation status (Certificate Revocation List (CRL) or Online Certificate Status Protocol (OCSP)) as defined in [Revocation Checking](#revocation-checking).
    - Verify that the issuer name of $C_i$ matches ``working_issuer_name``.

2. Policy Processing:

    - If ``certificatePolicies`` extension is present and ``valid_policy_tree`` is not ``NULL``:
        - Process policy constraints, qualifiers, and mappings according to [RFC 5280, Section 6.1.3].

        - for each policy $P$ not equal to ``anyPolicy`` in the certificate policies extension, let $P$-OID denote the OID for policy $P$ and $P$-Q denote the qualifier set for policy $P$.
            - for each node of depth $i-1$ in the ``valid_policy_tree`` where $P$-OID is in the node's ``expected_policy_set``, create a child node with ``valid_policy`` $P$-OID, ``qualifier_set`` $P$-Q, and ``expected_policy_set`` set to {$P$-OID}.
            - If no match is found for $P$-OID in any node of depth $i-1$ and the ``valid_policy_tree`` has a node of depth $i-1$ with ``valid_policy`` set to ``anyPolicy`, generate a child node with ``valid_policy`` $P$-OID, ``qualifier_set`` $P$-Q, and ``expected_policy_set`` set to {``anyPolicy``}.

        - if the ``certificatePolicies`` extension contains ``anyPolicy`` with the qualifier set $AP$-Q, $i \leq n$, and the certificate is self issued, then for each node of depth $i-1$ in the ``valid_policy_tree`` and each value in the ``expected_policy_set`` of that node, generate a child node with ``valid_policy`` and ``expected_policy_set`` set to the ``expected_policy_set`` value, set the ``qualifier_set`` set to $AP$-Q.
        - Update the ``valid_policy_tree`` by pruning nodes that do not match the policies in $C_i$.

    - If ``certificatePolicies`` is missing, set ``valid_policy_tree`` to ``NULL``.

3. Policy State Verification:

    - Verify that either ``explicit_policy > 0`` OR ``valid_policy_tree`` is not ``NULL``. If this fails, abort.

**Step 3: Preparation for Next Certificate**

1. If $i < n$ (i.e., $C_i$ is an intermediate Certificate Authority), perform the following updates:

    - Set ``working_issuer_name`` to the Subject DN of $C_i$.
    - Set ``working_public_key`` to the Subject Public Key of $C_i$.
    - Update ``working_public_key_parameters`` and ``working_public_key_algorithm`` from $C_i$.

2. Constraint Checks (Intermediates Only):

    - Verify ``basicConstraints`` extension is present and ``cA`` is set to TRUE.
    - If ``keyUsage`` extension is present, verify the ``keyCertSign`` bit is set.
    - Path Length: Verify ``max_path_length`` > 0. Decrement ``max_path_length`` by 1.

        - If $C_i$ contains ``pathLenConstraint``, set ``max_path_length`` to $\min(\text{current}, \text{pathLenConstraint})$.

3. Policy Counters:

    - Decrement ``explicit_policy`` and ``inhibit_any_policy`` (if > 0).

**Step 4: Wrap-up**

After processing $C_n$:

1. If ``explicit_policy`` > 0, decrement it.
2. If ``explicit_policy`` > 0 OR ``valid_policy_tree`` is not ``NULL``, the path is VALID.
3. Otherwise, the path is INVALID.

The following figure illustrates the flowchart of the X509 Certificate Chain Validation Algorithm.

.. plantuml:: plantuml/x509-chain-val-alg.puml
    :width: 99%
    :alt: The figure illustrates the Flowchart of the X509 Certificate Chain Validation Algorithm.
    :caption: `Flowchart of the X509 Certificate Chain Validation Algorithm. <https://www.plantuml.com/plantuml/png/ZLLXRzis4FtENt50WSr57Izkbcsruwo9cc06Z3IeutR3EWYqTB8FbaY2fDAultwaw3Xi90FvabZKlRjxZ-zExutbsjPLoSo6XEAQLt17jiHhAMmYIwdXrV7mzFTtooZW8hDqJtPxoRFDIijQvBj871Qd1NP5IfsZxiuN5PpJTuJXRunPVm9_3qwFtq62sb916RS8jzokuJClAUUMf81RBJCqXh661cEZgL2rDIEMHI3bGHFuDnds1uD1Fn7_zPdLjR4f5zbQwZwmhDOQXKqjLJXsQUOM5Gn7C1LaoPNxtfHZ-qS4OttgUww9Bqjq5UzzLwcI9MNRr6f4bnOVb7iakpkUY3V3FYEnfYNvujlu7DWEMt6bIAnsXz-athYdLDLBzpRTuBRVSPOsGg95RI8C6LEZJeLxuquh_f1wAT8InSgk9sBWYQA5Kae5979y078w3Pq0tzPK8lIc1WZE9Y3-V0raeFSFcjSC062q4_w7oqbetBmC4Os4RmTEn4jkA7DIMbnfvmNu2IvTDTSW96lCDgQ9FuBFgAdOWg6LuBRM2BNnCMso8Jw0eP7TPrKEBdFWAqx2M8Xlz0U0ndkP1VSOwmezAnyq0wyPLDncQpJGeMV4b0he1Og1ZZEfCKumkqOHIHQBydO4jyrbxmpiYUw3Zc1QWD9eKDW-g9tGaQ4RAA6940kLknU_A5qBX9OJOSaDvY25lw8zgjNLoRwhkJTtK8I2LllW828LyCpRS0x7yF5JHt4o8AI5cyLirYeUrEkeYdc7WZ4snWUREfT-5TvbkiAS6aDUGERRFP0fPd_YZHfKX2_XkaC_hVX7iRjS0OMM5IHq6DHsCpoDxYDytC8VxDevAP72MCr9s9q1My5xSo-zJP_Y3MGNaxjFYwl32DVWml0L-Xz-rkUq4h0aUnZnRCruN_GXnqnZXS929_GlBl8oBEePYeWGxIVX1PfuApnX3yvXjvAH-nDPUnUPpl0FZqnQ0-0uG2UalV212gzBcnEM1g5t8m-q6dtvhY-ciwiFuxEpLqMHPSkJy_DEYB5IjQk8d0hMLHTwkxtPB7OW0ubutMxcPmYY-G2p8QKmXq9gi5olqCQxYdNNxRp3qLJiNGAZvbj4y0Q6upQahTNBDUhM9lJMollod56-aClz3P_H9XSBFljr05yqLqUrOjFs3ctDoc3CcBVrDGbUUk-H8Ib6Ri-P0mlug-ZSm3SVxveDt9w7cDnyaIHNy_drOkO9vXdcsH-1O20NIVCYMG8goC7Uk_zrLVuF>`_

X509 Certificate Chain Status Checking
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. warning::
    
    TODO: richiamare il trust managemnt.

The Entity performing validation MUST determine the revocation status for every certificate in the path with one of the following methods:

- If the certificate contains the ``noRevAvail`` extension *and* the ``ETSIValAssuredCertMod`` extension (see :ref:`trust-artifact-eudiw:Wallet-Relying Party Access Certificate (WRPAC) Profile`), status checking SHOULD be skipped (as the certificate's status is determined solely by validity period).
- If the ``cRLDistributionPoints`` extension is present, the Entity performing validation MAY retrieve and validate the Certificate Revocation List (CRL).
- If the ``authorityInfoAccess`` extension (with ``id-ad-ocsp``) is present, the Entity performing validation MAY perform an Online Certificate Status Protocol (OCSP) lookup.

For details regarding the formats and parameters of Certificate Revocation List and Online Certificate Status Protocol responses, see :ref:`infrascructure-trust:Revocation Mechanisms`.

Status Checking via Certificate Revocation List
""""""""""""""""""""""""""""""""""""""""""""""""

When using a Certificate Revocation List, the Entity performing validation MUST:

1. Verify ``current_time`` is between ``thisUpdate`` and ``nextUpdate``. If the Certificate Revocation List is expired, the Entity performing validation SHOULD attempt to retrieve an updated Certificate Revocation List.
2. Verify the Certificate Revocation List is signed by the certificate issuer (or an authorized Certificate Revocation List issuer) by:
    - matching the ``issuer`` field of the Certificate Revocation List with the ``issuer`` field of the certificate being checked;
3. Verify the ``issuingDistributionPoint`` matches the certificate's distribution point.
    - ``distributionPoint`` field of the ``cRLDistributionPoints`` extension matches the ``distributionPoint`` field of the ``IssuingDistributionPoint`` extension of the Certificate Revocation List (if present);
    - if the ``BasicConstraints`` extension is present in the certificate being checked, and has ``cA`` set to ``TRUE`` (respectively ``FALSE``), the Certificate Revocation List Issuing Distribution Point extension MUST have the ``onlyContainsCACerts`` field set to ``TRUE`` (respectively have the ``onlyContainsUserCerts`` field set to ``TRUE``)
4. Validate the Certificate Revocation List signature using the issuer's public key. If a key usage extension is present in the Certificate Revocation List issuer's certificate, verify that the ``cRLSign`` bit is set.
5. Check if the certificate's serial number is listed in ``revokedCertificates``. If an entry is found then the certificate status is set to ``revoked``.

!!! note

    In this case it is assumed that the issuer of both the Certificate Revocation List and certificate do coincide, and that the Certificate Revocation List is not signed by a delegated Certificate Revocation List issuer.

If any of the steps 1-4 fail or the Certificate Revocation List is unavailable, the Entity performing validation SHOULD attempt to query the OCSP responder (if available) to determine the status of the Certificate. If this is not possible, it MUST consider the certificate status as ``unknown``. When all steps 1-4 succeed and the certificate serial number is not found in the Certificate Revocation List (CRL), the certificate MUST be considered ``good``.

.. warning::

    armonize certificate state value with the trust management

The following figure illustrates the flowchart of the CRL Status Validation Algorithm.

.. plantuml:: plantuml/crl-revocation.puml
    :width: 99%
    :alt: The figure illustrates the Flowchart of the CRL Validation Algorithm.
    :caption: `Flowchart of the CRL Status Validation Algorithm. <https://www.plantuml.com/plantuml/png/pPNHJzj84CRV_LUCX7G7JmSvq87XA24GAI9DguHGLOfKrjvniegpQ-sC0_dlQ-_6Q4FI5bKyzCdAUkQRx_TvjBaY5fRBHHxHNEb2MB60TifggNXrBTBvr9fIoux9ZOKzFCfECjnLQQn4kwuwF3hvxom9gZf6IyNAw2t1BClEqkETfQ5YbgI7BHcKtIlEiMiqRuwCk3w7ph0F3o9NKjHAyDcQ58cYoA56aSK21KS0AeFz4MC1Ht6bkAWQPvZE9xf7a9RMekPlN1ydo4-8Ug9vfcXSLB88GalG-Cp-vuS3u1bgsF-AT10102GMnJm2m9mGzWV6dyPjPbmK36p08bk5IuJIISZQzda4u7rvNHYkY-Js182_eMzCGP1KiTQAdYL0SNMX0-UXWvPLfj9QdrXmIJ6KUgxDKuKuH456nox3s-T2MPJ_ZBLO2fMB9CVpYukzRglREkrUNgxrY4tX1scfigXv-fJXQQRoQlozBV4WYc9diHN30rgLhQ17LA8zZshY6uFanlf3M0XEPnCTklLlcYWyqswUyU1kyEdBu8Md4VseoEbkSdW67vJBro4qTlzziNkZYArAIhzMHcbkhEzuHPxWjznkgxtLkTyUz_NXMf1AEqPNMg8sr3W9B4pqJ10yTjh_tm_7juzrlrVe-MzXTBwg5BZgfqwxRYHN-OeAu9t9jdOh80nMpH-7WoLceioP9fgDu-gs-wDVW8q9xH-7vfyRYtWSmqXDTJNU8lm5TxY2COaf-YLSttZey5xg6fYUNjRltxw2wuPDjHyltqEZxZBEQdFE6nGM2JN7_beTzcijI1G38Mz5_NxMrkR2U7U7UXB349SczVyLVMFcPU43hVo6TaPebSXXK2uIj1EjDDYgRuuoAABDQtetKDDNEywoLChMwp1_SbLCZN6DCaMPdWQDdkcgUfQB_3i0>`_

Status Checking via OCSP
""""""""""""""""""""""""""""

When using OCSP, the Entity performing validation MUST:

1. Verify ``responseStatus`` is ``successful (0)``. If the ``responseStatus`` is not ``successful``, the Entity performing validation SHOULD attempt to retrieve an updated OCSP response, and if that fails, the certificate status MUST be considered ``unknown``.
2. Verify ``responseType`` is ``id-pkix-ocsp-basic``.
3. Verify the response ``signature`` using the Responder's public key (``certs`` field in the OCSP response).
    - *Note*: To ensure the OCSP Responder is authorized, match the certificate issuer's key or check the delegation certificate signed by the issuer.
4. Verify ``responderID`` matches the signer, and the ``CertID`` hash fields match the certificate being checked.
    - ``issuerNameHash`` field value is the hash (via ``hashAlgorithm``) of the DER encoding of the issuer's Name.
    - ``issuerKeyHash`` field value is the hash (via ``hashAlgorithm``) of the issuer’s ``subjectPublicKey`` BIT STRING (excluding tag/length/unused-bits).
    - ``serialNumber`` field value is the certificate’s serial number.
5. Check ``thisUpdate`` and ``nextUpdate`` (or ``producedAt``) against local freshness policies.
6. If any of the checks in 2-4 fail, the certificate status MUST be considered ``unknown``. If all checks succeed, update the status of each certificate by matching the ``certStatus`` value in the ``SingleResponse`` to the requested ``CertID``.

.. note::

    It is assumed that only basic OCSP responses (i.e., where ``responseType`` is ``id-pkix-ocsp-basic``) are supported.

The following figure illustrates the flowchart of the OCSP Response Validation Algorithm.

.. plantuml:: plantuml/ocsp-revocation.puml
    :width: 99%
    :alt: The figure illustrates the Flowchart of the OCSP Response Validation Algorithm.
    :caption: `Flowchart of the OCSP Response Validation Algorithm. <https://www.plantuml.com/plantuml/png/dLDVJren57_lfpY9oG8F9ieqK_m_78aFsumuaoKcQsbFuOHBUzEUY_BjHxaKH0WnzgazFVtz-RMzZgm2L-D2n16vKWKrXXlDD26UVbTwD0Y-SgRZ2nzW3m_jiSLjdJuO38kkWyFZRwVzDrqTxmmnURS1QAqzrKVRMjSGRLyVjCoRjaVY0hlUyJgbu5I7tvtUFJnWBBsB24-g8ACI9jm7hp568UQcXGXOec81iq4M6Zt64WxRy8I1x1HaM43qM74LuU82OgKJWAqAQ1mqPHDuY0uQKunD0OlH3wX6ynKMC_g6y_LUPdb03bEucIWgLB_0gmpoDuFaqRvXnd79m1u2SY2SuBEhIgCOJMqoApnR7CoSl_mxg0u69ajQCK9jfmsoSYFdNvmyEp_VwxQwhPFkvUNQiSY-N24xGrQiPdLuy3Aa0g7n62fi2h6CiRKPu-Eqn1GYcVroHA_xNiTolwyYwMMGEQlTUf_T0wheNHlkt2JTxkgo4yUwdMoZ3cQJkobgEolfNvVIUpHmYgk0MHyj-6BU-9pSZBjJwWRJUvr7RRZrELw3uUvMmXUGIKkQZXNhuTMdaxs5dnJd63j4ffU_9kmkWjHL2EZu7zCO9VIHNn3TivCyfFWdlTvPLJa3qk4hBmgVrhd-rt-ybXJGV5Hn-rw5MKtso0qAp2XoPW43rwJoRExhJIKzuO7tPgKvhNQfJllpJsOq6dtoNjCM_80JFy8bnGxit9dWhTN6j3OjVoJHhP7bdAxHcMfS_0S0>`_



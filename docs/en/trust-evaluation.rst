.. include:: ../common/common_definitions.rst
.. include:: ../common/symbols.rst

Trust Evaluation Process
========================

Every trust evaluation process involves the following roles:

- The **Trust Evaluator** is the party that performs the evaluation.
- The **Trust Evaluated Party** is the entity, or the attestation, that is the object of the evaluation.

The same entity can act in both roles at different moments of the flows. The framework specific sections define which entity acts in which role, when, and for which purpose.

Each process requires a validated root of trust as a precondition. Each trust framework defines how its own root of trust is established, distributed and maintained. In the National Trust Framework this is the Federation Trust Anchor (see :ref:`trust-evaluation-oidfed:Federation Trust Anchor Distribution and Validation`). In the EUDIW Trust Framework these are the Trust Anchors obtained from the applicable Trusted Lists and Lists of Trusted Entities (see :ref:`trust-evaluation-eudiw:List of Trusted Entities Validation`).

The trust evaluation processes are the following:

  - **Authentication**. It asserts the cryptographic identity of a transacting entity. The Trust Evaluator binds the identifier of the Trust Evaluated Party to the proof of possession of a private key whose public part is trusted under the applicable root of trust.
  - **Authorization**. It evaluates a registration artifact to assert the entitlements of the Trust Evaluated Party, that is the specific capabilities the entity is authorized to perform, such as issuing a given Credential type or requesting a given set of attributes.
  - **Metadata Retrieval and Validation**. It obtains and validates the technical configuration of the Trust Evaluated Party, such as endpoints, public keys and supported algorithms.
  - **Signing Trust Anchor Validation**. It ingests an attestation and outputs the validated root of trust, identifier and public key, to be used for the verification of the issuer data authentication of that attestation.

The first three processes have an entity as their object. The fourth one has an attestation as its object and this includes Digital Credentials and the Wallet Instance Attestation.

Trust Framework Selection
------------------------------------

This section describes the Trust Framework selection rules applicable to the operational flows of the Entities involved.

For the Signing Trust Anchor Validation there is no selection to perform: the trust anchor for the verification of an attestation is defined by the Rulebook of its Credential type, in every phase and whichever party performs the verification. Attestations whose Rulebook anchors them to a List of Trusted Entities or to a Trusted List, such as PIDs, QEAAs and PuB-EAAs, MUST be validated against those trust anchors also when the interaction follows the National Trust Framework (see OIA_12, OIA_13, OIA_14 and OIA_15 of the ARF Annex 2, `EIDAS-ARF`_). For example, a Relying Party that obtains a PID from a national Wallet Instance MUST validate it against the trust anchors published in the PID Providers List of Trusted Entities.

The procedure for the Credentials anchored to the National Trust Framework is defined in :ref:`trust-evaluation-oidfed:Signing Trust Anchor Validation Procedure` (see also :ref:`onboarding-procedure:The Dual Trust Framework`).

The table below gives a high-level view of which trust framework applies to each entity in the operational phases. In particular, each cell indicates the applicable framework and the selection criterion, and points to the section where the corresponding procedures are defined. A more detailed view of which procedures each entity implements, and in which role, is given in the table of each framework section (see :ref:`trust-evaluation-oidfed:Trust Evaluation Processes by Context` for the National Trust Framework and the corresponding detail section of the EUDIW Trust Framework). The onboarding paths and the artifacts obtained by each entity type are defined in :ref:`onboarding-procedure:The Onboarding Processes`.

The Signing Trust Anchor Validation is not included in the table below, since, as noted above, it does not depend on the entity or on the selected framework.

.. _table_applicable_tf_by_entity:
.. list-table:: Applicable Trust Framework by Entity and Phase
    :class: longtable
    :widths: 16 42 42
    :header-rows: 1

    * - **Entity**
      - **Issuance**
      - **Presentation**
    * - Wallet Provider
      - Not applicable as a transacting party. The Wallet Provider is evaluated indirectly, as the issuer of the Wallet Instance Attestation, through the framework selected by the counterpart.
      - Not applicable as a transacting party.
    * - Wallet Instance
      - Acts as Trust Evaluator toward the Credential Issuer. It MUST support both EUDIW and National Trust Framework depending on whether the requested  Credential is in the EU catalogue or only in the national catalogue (see :ref:`trust-evaluation:Selection at Issuance`).
      - Acts as Trust Evaluator toward the Relying Party. It MUST support both EUDIW and National Trust Framework. In the remote flow the framework follows the ``client_id`` prefix declared by the Relying Party, while in the proximity flow only the EUDIW mdoc reader authentication applies (see :ref:`trust-evaluation:Selection at Presentation`).
    * - Credential Issuer
      - Acts as Trust Evaluator toward the Wallet Instance. It MUST support EUDIW when the Credential being issued is in the EU catalogue, or National Trust Framework only when the Credential is not in the EU catalogue (see :ref:`trust-evaluation:Selection at Issuance`).
      - Not applicable.
    * - Relying Party
      - Not applicable.
      - Acts as Trust Evaluated Party toward the Wallet Instance. It MUST support EUDIW Trust Framework when it operates under the EUDIW profile, that is for cross-border services, or National Trust Framework otherwise (see :ref:`trust-evaluation:Selection at Presentation`).

.. note::
  In case of technical divergence between the configuration published through EUDIW mechanisms and the configuration published through the federation, for example different certificates for the same entity in a List of Trusted Entities and in the Trust Anchor Entity Configuration, the EUDIW configuration MUST prevail.

Selection at Issuance
^^^^^^^^^^^^^^^^^^^^^

At issuance the Wallet Instance initiates the interaction and knows the requested Credential. The selection is driven by the catalogue of the requested Credential (see :ref:`registry:Digital Credentials Catalog`).

For Authentication, Authorization and Metadata Retrieval and Validation of the Credential Issuer, the Wallet Instance MUST apply the EUDIW procedures when the requested Credential is present in the EU catalogue, and the National Trust Framework procedures when the Credential is present only in the national catalogue. This rule MUST be applied also to EAA Providers, therefore, the same Credential Issuer MAY be evaluated under different frameworks in different interactions, according to the Credential requested. The headers of the signed artifacts of the Credential Issuer manifest the same selection, an ``x5c`` header carrying the access certificate for the EUDIW path, a ``kid`` header, with the optional ``trust_chain`` header, for the National Trust Framework path and they MUST be consistent with the framework selected by the catalogue.

For the validation of the Wallet Instance, the Credential Issuer MUST validate the Wallet Instance Attestation through the Wallet Providers List of Trusted Entities when the Credential being issued is present in the EU catalogue. A Credential Issuer MAY validate the Wallet Instance Attestation through the National Trust Framework only when the Credential being issued is not present in the EU catalogue (see :ref:`trust-evaluation-oidfed:Wallet Instance Authentication`).

Selection at Presentation
^^^^^^^^^^^^^^^^^^^^^^^^^

In the remote flow the selection is declared by the Relying Party through the ``client_id`` prefix of the request (see `OpenID4VP`_, Section 5.9).

A Relying Party interacting with a Wallet Unit under the EUDIW profile (i.e. when a Relying Party wants to provide cross-border online services to the users), MUST use the ``x509_hash`` Client Identifier Prefix and the EUDIW artifacts, as required by [`ETSI TS 119 472-2`_] (OIDFVP-HAIP-COMMON-REQ-01). A Relying Party that knows it is interacting with a national Wallet Instance, through the wallet discovery mechanism of the ecosystem (see :ref:`wallet-metadata-retrieval:Wallet Metadata Retrieval Flow` and the Selection Page in :ref:`functionalities:User Experience Design`), MAY use the ``openid_federation`` prefix with the federation artifacts.

The Wallet Instance MUST support both prefixes and MUST process each request under the trust evaluation procedures of the framework declared by the prefix. In particular, the ``x509_hash`` prefix selects the EUDIW procedures (see :ref:`trust-evaluation-eudiw:EUDIW Authentication`), the ``openid_federation`` prefix selects the National Trust Framework procedures (see :ref:`trust-evaluation-oidfed:Trust Evaluation Processes by Context`). The Authentication, Authorization and Metadata Retrieval and Validation processes run under the selected framework.

In the proximity flow the Relying Party Instance authentication follows the mdoc reader authentication defined in [`ISO18013-5`_ #12.5], based on the access certificate, as profiled in Section 5.3 of [`ETSI TS 119 472-2`_] (see :ref:`proximity-flow:mdoc Request`). A selection mechanism equivalent to the ``client_id`` prefix is not defined in [`ISO18013-5`_].

Failure Handling
^^^^^^^^^^^^^^^^

The failure of the trust evaluation under the selected framework MUST NOT be evaluated again under the other framework. During presentation flow, if a Relying Party declares the ``x509_hash`` prefix and the access certificate validation fails, the Wallet Instance MUST NOT attempt the evaluation under the National Trust Framework, and the same rule applies in the opposite direction.

At issuance, if the evaluation of the Credential Issuer or of the Wallet Instance Attestation fails under the framework selected by the catalogue, the interaction MUST NOT continue and MUST NOT be re-evaluated under the other framework. In the EUDIW Trust Framework, according to the ARF Annex 2 (`EIDAS-ARF`_), the Wallet Unit MUST validate the access certificate of the Provider and its registration before requesting the issuance and, when this verification does not succeed, it MUST display a warning to the User and MUST NOT request the issuance (ISSU_24, ISSU_24a and ISSU_24b for the PID Providers, ISSU_34, ISSU_34a and ISSU_34b for the other Providers). The Provider MUST validate the Wallet Instance Attestation through the Wallet Providers LoTE before issuing (ISSU_21, ISSU_28). Unlike the presentation case, no User choice option is foreseen at issuance. Within the National Trust Framework the same behavior applies by analogy.

When the authentication of a Relying Party fails, the Wallet Instance MUST inform the User that the identity of the Relying Party could not be verified and that the request is not trustworthy. Under the EUDIW Trust Framework this behavior is required by RPA_05 and RPA_06a of the ARF Annex 2 (`EIDAS-ARF`_). Within the National Trust Framework the same behavior applies by analogy with RPA_05.

.. include:: trust-evaluation-eudiw.rst
.. include:: trust-evaluation-oidfed.rst
.. include:: trust-override-rules.rst

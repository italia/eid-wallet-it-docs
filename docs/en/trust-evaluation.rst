.. include:: ../common/common_definitions.rst
.. include:: ../common/symbols.rst
.. Included via index.rst at title level '=' (document title).

Trust Evaluation Process
========================

Every trust evaluation process involves the following roles:

- The **Trust Evaluator** is the party that performs the evaluation.
- The **Trust Evaluated Party** is the entity, or the attestation, that is the object of the evaluation.

The same entity can act in both roles at different moments of the flows.
The framework specific sections define which entity acts in which role, when, and for which purpose.

Each process requires a validated root of trust as a precondition.
Each trust framework defines how its own root of trust is established, distributed and maintained.
In the National Trust Framework this is the Federation Trust Anchor (see :ref:`trust-evaluation:Federation Trust Anchor Distribution and Validation`).
In the EUDIW Trust Framework these are the Trust Anchors obtained from the applicable Trusted Lists and Lists of Trusted Entities (see :ref:`trust-evaluation:List of Trusted Entities Validation`).

The trust evaluation processes are the following:

  - **Authentication**.
    It asserts the cryptographic identity of a transacting entity.
    The Trust Evaluator binds the identifier of the Trust Evaluated Party to the proof of possession of a private key whose public part is trusted under the applicable root of trust.
  - **Authorization**.
    It evaluates a registration artifact to assert the entitlements of the Trust Evaluated Party, that is the specific capabilities the entity is authorized to perform, such as issuing a given Credential type or requesting a given set of attributes.
  - **Metadata Retrieval and Validation**.
    It obtains and validates the technical configuration of the Trust Evaluated Party, such as endpoints, public keys and supported algorithms.
  - **Signing Trust Anchor Validation**.
    It ingests an attestation and outputs the validated root of trust, identifier and public key, to be used for the verification of the issuer data authentication of that attestation.

The first three processes have an entity as their object.
The fourth one has an attestation as its object and this includes Digital Credentials and the Wallet Instance Attestation.

Trust Framework Selection
------------------------------------

This section describes the Trust Framework selection rules applicable to the operational flows of the Entities involved.
The two Trust Frameworks and the policy that selects them are defined in :ref:`infrastructure-trust:Infrastructure of Trust`.
A failed EUDIW evaluation MUST NOT be retried under the National Trust Framework, as specified in :ref:`trust-evaluation:Failure Handling`.

For the Signing Trust Anchor Validation there is no selection to perform: the trust anchor for the verification of an attestation is defined by the Rulebook of its Credential type, in every phase and whichever party performs the verification.
Attestations whose Rulebook anchors them to a List of Trusted Entities or to a Trusted List, such as PIDs, QEAAs and PuB-EAAs, MUST be validated against those trust anchors also when the interaction follows the National Trust Framework (see OIA_12, OIA_13, OIA_14 and OIA_15 of the ARF Annex 2, `EIDAS-ARF`_).
For example, a Relying Party that obtains a PID from a national Wallet Unit MUST validate it against the trust anchors published in the PID Providers List of Trusted Entities.

The procedure for the Credentials anchored to the National Trust Framework is defined in :ref:`trust-evaluation:Signing Trust Anchor Validation Procedure` (see also :ref:`onboarding-system:Onboarding System and Lifecycle Management`).

The table below gives a high-level view of which trust framework applies to each entity in the operational phases.
In particular, each cell indicates the applicable framework and the selection criterion, and points to the section where the corresponding procedures are defined.
A more detailed view of which procedures each entity implements, and in which role, is given in the table of each framework section (see :ref:`trust-evaluation:Trust Evaluation Processes by Context` for the National Trust Framework and the corresponding detail section of the EUDIW Trust Framework).
The onboarding paths and the artifacts obtained by each entity type are defined in :ref:`onboarding-system:Onboarding Processes`.

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
      - Not applicable as a transacting party.
        The Wallet Provider is evaluated indirectly, as the issuer of the Wallet Instance Attestation, through the framework selected by the counterpart.
      - Not applicable as a transacting party.
    * - Wallet Unit
      - Acts as Trust Evaluator toward the Credential Issuer and, at the same time, as Trust Evaluated Party toward it, since the Credential Issuer validates its Wallet Instance Attestation.
        The selection of the Trust Framework is defined in :ref:`trust-evaluation:Selection at Issuance`.
      - Acts as Trust Evaluator toward the Relying Party.
        It MUST support both EUDIW and National Trust Framework.
        In the remote flow the framework follows the ``client_id`` prefix declared by the Relying Party.
        In the proximity flow both frameworks use the mdoc reader authentication and the framework is determined by the trust anchor that validates the reader certificate (see :ref:`trust-evaluation:Selection at Presentation`).
    * - Credential Issuer
      - Acts as Trust Evaluator toward the Wallet Unit and, at the same time, as Trust Evaluated Party toward it, since the Wallet Unit validates its Authentication, Authorization and Metadata.
        The selection of the Trust Framework is defined in :ref:`trust-evaluation:Selection at Issuance`.
      - Not applicable.
    * - Relying Party
      - Not applicable.
      - Acts as Trust Evaluated Party toward the Wallet Unit.
        The selection of the Trust Framework, including the ``client_id`` prefix, is defined in :ref:`trust-evaluation:Selection at Presentation`.

.. note::
  In case of technical divergence between the configuration published through EUDIW mechanisms and the configuration published through the federation, for example different certificates for the same entity in a List of Trusted Entities and in the Trust Anchor Entity Configuration, the EUDIW configuration MUST prevail.

Selection at Issuance
^^^^^^^^^^^^^^^^^^^^^

At issuance the Wallet Unit initiates the interaction and knows the requested Credential.
The selection is driven by whether the Credential Issuer is a national entity or is of another Member State, together with the catalogue of the requested Credential (see :ref:`registry:Digital Credentials Catalog`).

For Authentication, Authorization and Metadata Retrieval and Validation of the Credential Issuer, the Wallet Unit MUST apply the EUDIW procedures when the Credential Issuer, or the requested PID, (Q)EAA or PuB-EAA, is of another Member State.
The Wallet Unit SHOULD apply the National Trust Framework procedures when the Credential Issuer is a national entity.
The National Trust Framework MUST NOT be selected for the issuance of a PID, (Q)EAA or PuB-EAA of another Member State.
This rule MUST be applied also to EAA Providers, therefore, the same Credential Issuer MAY be evaluated under different frameworks in different interactions, according to the counterpart and the Credential requested.
The headers of the signed artifacts of the Credential Issuer reflect the same selection: an ``x5c`` header carrying the access certificate for the EUDIW path, and a ``kid`` header, with the optional ``trust_chain`` header, for the National Trust Framework path.
These headers MUST be consistent with the selected framework.

For the validation of the Wallet Unit, the Credential Issuer MUST validate the Wallet Instance Attestation through the Wallet Providers List of Trusted Entities when the Wallet Unit is of another Member State.
A Credential Issuer SHOULD validate the Wallet Instance Attestation through the National Trust Framework when the Wallet Unit is national (see :ref:`trust-evaluation:Wallet Unit Authentication`).

Selection at Presentation
^^^^^^^^^^^^^^^^^^^^^^^^^

In the remote flow the selection is declared by the Relying Party through the ``client_id`` prefix of the request (see `OpenID4VP`_, Section 5.9).

The Relying Party does not authenticate the Wallet Unit and therefore cannot select the Trust Framework according to the Member State of that Wallet Unit or Wallet Solution.

A national Relying Party that offers services for interoperability outside the national audience MUST use the ``x509_hash`` Client Identifier Prefix and the EUDIW artifacts, as required by [`ETSI TS 119 472-2`_] clause 6.
A national Relying Party that does not offer those interoperable services and addresses a national audience only SHOULD use the ``openid_federation`` prefix with the federation artifacts, including when it requests a PID, (Q)EAA or PuB-EAA.

The Wallet Unit MUST support both prefixes.
It MUST process a request with the ``x509_hash`` prefix under the EUDIW procedures (see :ref:`trust-evaluation:EUDIW Authentication`).
It MUST process a request with the ``openid_federation`` prefix under the National Trust Framework procedures (see :ref:`trust-evaluation:Trust Evaluation Processes by Context`) when the Trust Chain of the Relying Party is valid under the National Trust Anchor.
If the request uses the ``openid_federation`` prefix and the Trust Chain cannot be validated under the National Trust Anchor, the Wallet Unit MUST treat the Relying Party as not trustworthy and MUST NOT evaluate the request under the National Trust Framework.
The Authentication, Authorization and Metadata Retrieval and Validation processes run under the selected framework only. Implementations MUST NOT combine the frameworks or retry a failed process under the other framework.

In the proximity flow both Trust Frameworks use the mdoc reader authentication defined in [`ISO18013-5`_ #12.5], based on an X.509 certificate provided by the Relying Party Instance in the ``x5chain`` header of the ``ReaderAuth``.

Under the EUDIW Trust Framework the certificate is the access certificate, as profiled in Section 5.3 of [`ETSI TS 119 472-2`_] (see :ref:`proximity-flow:mdoc Request`), and it is validated against the Provider of Wallet-Relying Party Access Certificate List of Trusted Entities.

Under the National Trust Framework the certificate is the Relying Party authentication certificate and it is validated against an Authentication Trust Anchor published in the Federation Trust Anchor Entity Configuration (see :ref:`trust-evaluation:Relying Party Proximity Authentication`).

A selection mechanism equivalent to the ``client_id`` prefix is not defined in [`ISO18013-5`_].

Within IT-Wallet the applicable framework is determined by the trust anchor that validates the certification path of the reader certificate.
The request is processed under the EUDIW Trust Framework when the path terminates in a trust anchor of the Provider of Wallet-Relying Party Access Certificate List of Trusted Entities, and under the National Trust Framework when it terminates in an Authentication Trust Anchor of the federation.
The Relying Party applies the same audience policy as in the remote flow, using the corresponding certificate instead of the ``client_id`` prefix.
The Wallet Unit MUST determine the applicable framework before the Authorization process and MUST run the Authorization under that framework only.

Failure Handling
^^^^^^^^^^^^^^^^

The failure of the trust evaluation under the selected framework MUST NOT be evaluated again under the other framework.
In particular, a failed EUDIW evaluation MUST NOT be retried as a National Trust Framework evaluation.

If Authentication fails, the Wallet Unit MUST inform the User that the identity of the Wallet-Relying Party could not be verified and MUST stop the interaction ([`EIDAS-ARF`_] CT_06, RPA_06a).
The same applies under the National Trust Framework: a ``NON_AUTHENTICATED`` outcome MUST stop the interaction.

If Authentication succeeds and Authorization fails, the Wallet Unit MUST apply :ref:`trust-evaluation:Authorization Decision and Override Rules`.
During presentation, a User choice to proceed is allowed only for the overridable Authorization outcomes defined there.
Authentication failure is not overridable.

During Issuance, when Authentication or Authorization does not succeed, the Wallet Unit MUST display a warning to the User and MUST NOT request the issuance ([`EIDAS-ARF`_] RPRC_22a).
No User choice is offered at issuance.

.. include:: trust-evaluation-eudiw.rst
.. include:: trust-evaluation-oidfed.rst
.. include:: trust-override-rules.rst

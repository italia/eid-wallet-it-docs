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
-------------------------

This section defines which Trust Framework applies to an interaction.
The two Trust Frameworks are described in :ref:`infrastructure-trust:Infrastructure of Trust`.
The procedures of each framework are defined in the following sections.
The onboarding paths and the artifacts of each entity type are defined in :ref:`onboarding-system:Onboarding Processes`.

The **interaction** is the authentication and authorization of the parties for one issuance or one presentation.
The Wallet Unit MUST select exactly one Trust Framework for each interaction, before Authentication, Authorization or Metadata Retrieval and Validation.
The selected Trust Framework applies to the whole interaction.
A failed evaluation is handled as specified in :ref:`trust-evaluation:Failure Handling`.

The **signing trust anchor** of an Attestation follows the Rulebook of its Credential type, in every phase and whichever party performs the verification.
A PID, a QEAA and a PuB-EAA MUST be validated against the Trust Anchors of the applicable List of Trusted Entities or Trusted List (see OIA_12, OIA_13, OIA_14 and OIA_15 of the ARF Annex 2, `EIDAS-ARF`_).
The procedure for a Credential anchored to the National Trust Framework is defined in :ref:`trust-evaluation:Signing Trust Anchor Validation Procedure`.

The onboarding declaration of a Non-Qualified EAA Provider or of a Relying Party is specified in :ref:`onboarding-system:Registration Profiles`.
At runtime the requested Credential selects the Trust Framework of the interaction.
The same Credential Issuer MAY be evaluated under different frameworks in different interactions.

Where the configuration published through the EUDIW mechanisms and the configuration published through the federation diverge, the EUDIW configuration MUST prevail.

.. _table_applicable_tf_by_entity:
.. list-table:: Applicable Trust Framework by Interaction
    :class: longtable
    :widths: 22 46 32
    :header-rows: 1

    * - **Interaction**
      - **Condition**
      - **Trust Framework**
    * - Issuance, Credential Issuer
      - The requested Credential is a PID, a QEAA or a PuB-EAA, or the Credential Issuer is of another Member State.
      - The Wallet Unit MUST use the EUDIW Trust Framework.
    * - Issuance, Credential Issuer
      - The Credential Issuer is a national entity and the requested Credential is a non-qualified Electronic Attestation of Attributes with national scope.
        The IT-Wallet ID is such a Credential (see :term:`IT-Wallet ID`).
      - The Wallet Unit MUST use the National Trust Framework.
    * - Issuance, Wallet Instance Attestation
      - The Wallet Unit is of another Member State.
      - The Credential Issuer MUST validate it through the Wallet Providers List of Trusted Entities.
    * - Issuance, Wallet Instance Attestation
      - The Wallet Unit is national.
      - The Credential Issuer MAY validate it through the National Trust Framework (see :ref:`trust-evaluation:Wallet Unit Authentication`).
    * - Presentation
      - The request includes a PID, a QEAA or a PuB-EAA, or a Credential of another Member State, or the Relying Party offers the service outside the national audience.
      - The Relying Party MUST use the EUDIW Trust Framework for the whole request.
    * - Presentation
      - The Relying Party is national and the request contains only a non-qualified Electronic Attestation of Attributes with national scope.
      - The Relying Party MUST use the National Trust Framework.

Selection at Issuance
^^^^^^^^^^^^^^^^^^^^^

At issuance the Wallet Unit initiates the interaction and knows the requested Credential (see :ref:`registry:Digital Credentials Catalog`).
The applicable row of :ref:`Applicable Trust Framework by Interaction <table_applicable_tf_by_entity>` selects the Trust Framework.

On the EUDIW path, Authentication, Authorization and Metadata Retrieval and Validation of the Credential Issuer follow :ref:`trust-evaluation:EUDIW Authentication`, :ref:`trust-evaluation:EUDIW Authorization` and :ref:`trust-evaluation:EUDIW Metadata Retrieval and Validation`.
On the National path they follow :ref:`trust-evaluation:Federation Entity Authentication`, :ref:`trust-evaluation:Authorization` and :ref:`trust-evaluation:Metadata Retrieval and Validation`.

The headers of the signed artifacts of the Credential Issuer MUST be consistent with the selected framework.
An ``x5c`` header carries the access certificate on the EUDIW path.
A ``kid`` header, with the optional ``trust_chain`` header, carries the federation key on the National path.

Selection at Presentation
^^^^^^^^^^^^^^^^^^^^^^^^^

The Relying Party does not authenticate the Wallet Unit.
It cannot select the Trust Framework according to the Member State of that Wallet Unit or Wallet Solution.
The applicable row of :ref:`Applicable Trust Framework by Interaction <table_applicable_tf_by_entity>` selects the Trust Framework.

In the remote flow the Relying Party declares that framework through the ``client_id`` prefix of the request (see `OpenID4VP`_, Section 5.9).
The prefix ``x509_hash`` selects the EUDIW Trust Framework, as required by [`ETSI TS 119 472-2`_] clause 6 (OIDFVP-HAIP_COMMON_GEN_REQ-02).
The prefix ``openid_federation`` selects the National Trust Framework.
The Wallet Unit MUST process ``x509_hash`` under :ref:`trust-evaluation:EUDIW Authentication`.
The Wallet Unit MUST process ``openid_federation`` under :ref:`trust-evaluation:Trust Evaluation Processes by Context` when the Trust Chain of the Relying Party is valid under the National Trust Anchor.
If that Trust Chain cannot be validated, the Wallet Unit MUST treat the Relying Party as not trustworthy.
The Wallet Unit MUST stop the interaction.

In the proximity flow both frameworks use the mdoc reader authentication defined in [`ISO18013-5`_ #12.5].
The Relying Party Instance provides an X.509 certificate in the ``x5chain`` header of the ``ReaderAuth``.
The Wallet Unit MUST determine the framework from the trust anchor that validates that certification path, before Authorization.
The Wallet Unit MUST run Authorization under that framework only.
The path selects the EUDIW Trust Framework when it terminates in a trust anchor of the Provider of Wallet-Relying Party Access Certificate List of Trusted Entities (see :ref:`proximity-flow:mdoc Request`).
The path selects the National Trust Framework when it terminates in an Authentication Trust Anchor of the federation (see :ref:`trust-evaluation:Relying Party Proximity Authentication`).
The Relying Party uses the certificate that corresponds to the selected row.

Failure Handling
^^^^^^^^^^^^^^^^

The failure of the trust evaluation under the selected framework MUST NOT be evaluated again under the other framework.

If Authentication fails, the Wallet Unit MUST inform the User that the identity of the Wallet-Relying Party could not be verified and MUST stop the interaction ([`EIDAS-ARF`_] RPA_06a).
The same applies under the National Trust Framework: a ``NON_AUTHENTICATED`` outcome MUST stop the interaction.

If Authentication succeeds and Authorization fails, the Wallet Unit MUST apply :ref:`trust-evaluation:Authorization Decision and Override Rules`.
During presentation, a User choice to proceed is allowed only for the overridable Authorization outcomes defined there.
Authentication failure is not overridable.

During Issuance, when Authentication or Authorization does not succeed, the Wallet Unit MUST display a warning to the User and MUST NOT request the issuance ([`EIDAS-ARF`_] RPRC_22a).
No User choice is offered at issuance.

.. include:: trust-evaluation-eudiw.rst
.. include:: trust-evaluation-oidfed.rst
.. include:: trust-override-rules.rst

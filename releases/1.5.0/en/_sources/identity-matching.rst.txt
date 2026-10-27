.. include:: ../common/common_definitions.rst


.. _identity-matching:

Identity Matching and Identity Reconciliation
=============================================

**Identity matching** is the process by which a Relying Party establishes that the person identification attributes presented in a transaction refer to the same natural person. It is the same practical approach used in any legacy authentication and authorization infrastructure. It is not a Wallet Instance feature, nor a step of the presentation protocol. Cryptographic verification of the Digital Credential remains a distinct prerequisite, and identity reconciliation is a subsequent, optional step.

After cryptographic verification of a presented Digital Credential, in remote or proximity flows, the Relying Party MUST first perform **identity matching**. Identity matching establishes that the person identification attributes presented in the current transaction refer to the same natural person. Only after a successful identity matching, the Relying Party MAY perform **identity reconciliation**, linking that natural person to a previous User session or stored User record.

If identity matching fails, the Relying Party MUST NOT perform identity reconciliation. The Relying Party MUST NOT treat the presenter as a previously known User.

This Section specifies the matching and reconciliation rules that apply to person identification Digital Credentials (PID and IT-Wallet ID). Correlation of identities during IT-Wallet ID issuance (IdP–MRTD) is specified in :ref:`credential-issuance-l2plus:eID Substantial Authentication with MRTD Verification for IT-Wallet ID Issuance` and is out of scope of this Section.

Identity Matching
-----------------

Identity matching determines whether the presented person identification attributes identify one natural person.

.. note::
  When a Relying Party needs to distinguish the User during authentication, the Relying Party MUST do so on the basis of the information contained in the Digital Credentials requested in the presentation request. The Relying Party must include the corresponding claims in the presentation request. The Relying Party distinguishes the User by evaluating the values of the claims actually presented.

  Non-normative examples are provided below.

  1. **PID or IT-Wallet ID.** The Relying Party requests the identification claims defined by the relevant data model, for example ``given_name``, ``family_name`` and ``personal_administrative_number`` for the PID, or ``tax_id_code`` for the IT-Wallet ID. See :ref:`credential-data-model-pid:PID Data Model` and :ref:`credential-data-model-it-wallet-id:IT-Wallet ID Data Model`.

     Example of a ``dcql_query`` in the remote flow (PID in SD-JWT VC format):

     .. literalinclude:: ../../examples/identity-matching-pid-dcql.json
        :language: json

     The same claims, in the proximity flow, are requested in the mdoc ``ItemsRequest``:

     .. literalinclude:: ../../examples/identity-matching-pid-items-request.json
        :language: json

  2. **Another Digital Credential from the catalog.** The Relying Party requests the claims defined by the schema of the Digital Credential published in the :ref:`registry:Digital Credentials Catalog`. The corresponding data model is defined by the related schema in the :ref:`registry:Schema Registry`.

     Example of a ``dcql_query`` in the remote flow for an mDL (``credential_type`` ``mDL``, mdoc-CBOR format, ``docType`` ``org.iso.18013.5.1.mDL``):

     .. literalinclude:: ../../examples/identity-matching-mdl-dcql.json
        :language: json

The Relying Party MUST apply the matching pattern of the presented Digital Credential type, as defined below. Different Digital Credential types MAY define different identity matching patterns. For the PID User attributes, see :ref:`credential-data-model-pid:PID Data Model`. For the IT-Wallet ID User attributes, see :ref:`credential-data-model-it-wallet-id:IT-Wallet ID Data Model`.

Identity Reconciliation
-----------------------

Identity reconciliation is the subsequent step that binds a successfully matched natural person to a Relying Party User record or session.

The Relying Party MUST NOT complete identity reconciliation unless identity matching has succeeded. Reconciliation MAY create a new User record when no stored record matches.

Matching Patterns by Digital Credential Type
--------------------------------------------

Unique National Identifier Binding
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When ``personal_administrative_number`` or ``tax_id_code`` is presented, the Relying Party MUST use it as the primary identity matching key before any identity reconciliation with a stored User record (:ref:`CI_201 <credential-issuer-testcases>`).

For the IT-Wallet ID, at least one of ``tax_id_code`` and ``personal_administrative_number`` is present. The Relying Party MUST use the unique national identifier that is presented as the primary matching key.

Attribute-Based Binding
^^^^^^^^^^^^^^^^^^^^^^^

For the PID, ``personal_administrative_number`` is OPTIONAL. Relying Parties MUST NOT assume that a unique national identifier is always available.

When ``personal_administrative_number`` is not presented, the Relying Party MUST perform *Attribute-Based Binding* by matching at least ``family_name``, ``given_name``, ``birth_date`` (or ``birthdate``) and ``place_of_birth`` after normalisation of case, whitespace and diacritics. The Relying Party MUST apply the same normalisation to the presented attributes and to the stored User record, including the string members of ``place_of_birth`` (``country``, ``region``, ``locality``). Comparison of the date of birth MUST use the ISO 8601 calendar date (``YYYY-MM-DD``), independent of display format.

The Relying Party MUST NOT complete identity matching on a subset of those attributes that would allow a person swap (:ref:`CI_202 <credential-issuer-testcases>`). In particular:

- matching only a pair of names, only a name and a date of birth, or any subset that omits ``place_of_birth``, MUST NOT be treated as a successful identity match.
- a mismatch on any attribute of the minimum set MUST fail identity matching. The Relying Party MUST NOT ignore a current-name mismatch (for example after a name change) in order to force a match.
- if Attribute-Based Binding matches more than one stored User record, the Relying Party MUST NOT complete identity matching. It MAY request a unique national identifier, or apply a supplementary binding method that uniquely identifies the person.

Supplementary Binding Methods
-----------------------------

The following methods MAY supplement Attribute-Based Binding. They MUST NOT replace the Attribute-Based Binding minimum set when no unique national identifier is presented:

- **Session-Based Binding**: the presentation occurs within an authenticated session already bound to the User.
- **Issuer-Attested Binding**: the Issuer attests that the presented attributes belong to the same subject (for example through a stable Issuer subject identifier).
- **Relying Party-Specific Identifiers**: identifiers previously issued by the Relying Party to that User after a successful identity match.
- **Cryptographic Binding**: proving that the private keys of the presented Digital Credentials are managed by the same Keystore or WSCD.

Privacy and Selective Disclosure
--------------------------------

Selective disclosure MUST be used so that identifying attributes needed only for matching are not released when not required for the specific transaction. The use is in line with Article 5a of the European Digital Identity Regulation and the privacy-preserving combined presentation principles of the ARF. Those principles are fully applicable when the IT-Wallet will be notified as an EUDIW solution.

Application to User Attribute Deletion
--------------------------------------

When the User requests deletion of presented attributes, the Relying Party MUST uniquely identify one or more Digital Credentials by applying identity matching, as specified in :ref:`user-attribute-deletion:User's Attributes Deletion`.

When the User authenticates for a data deletion request by presenting a Digital Credential from the Wallet Instance, the Relying Party MUST apply the matching patterns of this Section.

When the User authenticates for a data deletion request without using the Wallet Instance, the Relying Party MAY perform identity matching and identity reconciliation. The Relying Party uses person identification attributes obtained from a preexisting national authentication scheme (for example CieID). Those attributes uniquely identify the User in the Relying Party's records.

.. include:: ../common/common_definitions.rst


.. _identity-matching:

Identity Matching and Identity Reconciliation
=============================================

**Identity matching** is the process by which a Relying Party establishes that the person identification attributes presented in a transaction refer to the same natural person. It is the same practical approach used in any legacy authentication and authorization infrastructure. It is not a Wallet Instance feature, nor a step of the presentation protocol. Cryptographic verification of the Digital Credential remains a distinct prerequisite, and identity reconciliation is a subsequent, optional step.

After cryptographic verification of a presented Digital Credential, in remote or proximity flows, the Relying Party MUST first perform **identity matching**, to establish that the person identification attributes presented in the current transaction refer to the same natural person. Only after a successful identity matching, the Relying Party MAY perform **identity reconciliation**, linking that natural person to a previous User session or stored User record.

If identity matching fails, the Relying Party MUST NOT perform identity reconciliation and MUST NOT treat the presenter as a previously known User.

This Section specifies the matching and reconciliation rules that apply to person identification Digital Credentials (PID and IT-Wallet ID). Correlation of identities during IT-Wallet ID issuance (IdP–MRTD) is specified in :ref:`credential-issuance-l2plus:eID Substantial Authentication with MRTD Verification for IT-Wallet ID Issuance` and is out of scope of this Section.

Identity Matching
-----------------

Identity matching determines whether the presented person identification attributes identify one natural person.

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

When ``personal_administrative_number`` is not presented, the Relying Party MUST perform *Attribute-Based Binding* by matching at least ``family_name``, ``given_name`` and ``birth_date`` (or ``birthdate``) after normalisation of case, whitespace and diacritics. The Relying Party MUST apply the same normalisation to the presented attributes and to the stored User record. Comparison of the date of birth MUST use the ISO 8601 calendar date (``YYYY-MM-DD``), independent of display format.

The Relying Party MUST NOT complete identity matching on a subset of those attributes that would allow a person swap (:ref:`CI_202 <credential-issuer-testcases>`). In particular:

- matching only a pair of names, or only a name and a date of birth, MUST NOT be treated as a successful identity match;
- a mismatch on any attribute of the minimum set MUST fail identity matching; the Relying Party MUST NOT ignore a current-name mismatch (for example after a name change) in order to force a match;
- if Attribute-Based Binding matches more than one stored User record, the Relying Party MUST NOT complete identity matching. It MAY request a unique national identifier, or apply a supplementary binding method that uniquely identifies the person.

Supplementary Binding Methods
-----------------------------

The following methods MAY supplement Attribute-Based Binding. They MUST NOT replace the Attribute-Based Binding minimum set when no unique national identifier is presented:

- **Session-Based Binding**: the presentation occurs within an authenticated session already bound to the User;
- **Issuer-Attested Binding**: the Issuer attests that the presented attributes belong to the same subject (for example through a stable Issuer subject identifier);
- **Relying Party-Specific Identifiers**: identifiers previously issued by the Relying Party to that User after a successful identity match;
- **Cryptographic Binding**: proving that the private keys of the presented Digital Credentials are managed by the same Keystore or WSCD.

Privacy and Selective Disclosure
--------------------------------

Selective disclosure MUST be used so that identifying attributes needed only for matching are not released when not required for the specific transaction, in line with Article 5a of the European Digital Identity Regulation and the privacy-preserving combined presentation principles of the ARF, to be fully applicable when the IT-Wallet will be notified as an EUDIW solution.

Application to User Attribute Deletion
--------------------------------------

When the User requests deletion of presented attributes, the Relying Party MUST uniquely identify one or more Digital Credentials by applying identity matching, as specified in :ref:`user-attribute-deletion:User's Attributes Deletion`.

When the User authenticates at the Erasure Endpoint by presenting a Digital Credential from the Wallet Instance, the Relying Party MUST apply the matching patterns of this Section.

When the User authenticates at the Erasure Endpoint without using the Wallet Instance, the Relying Party MAY perform identity matching and identity reconciliation using person identification attributes obtained from a preexisting national authentication scheme (for example CieID), where those attributes uniquely identify the User in the Relying Party's records.

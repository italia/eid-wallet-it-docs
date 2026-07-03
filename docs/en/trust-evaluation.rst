.. include:: ../common/common_definitions.rst
.. include:: ../common/symbols.rst



Trust Evaluation
================

Trust evaluation is characterized through three fundamental, sequential processes. Each ingests specific artifacts and yields a validated state with, optionally, additional outputs:

- **Trust Anchor Validation**: Ingests an artifact to output a validated root of trust (identifier and public key).
- **Authentication**: Utilizing the validated TA, this process asserts the cryptographic identity of a transacting entity.
- **Authorization**: Utilizing the validated TA, this process evaluates an artifact to assert an entity's specific capabilities or cryptographic entitlements to perform an action.

.. include:: trust-evaluation-eudiw.rst
.. include:: trust-evaluation-oidfed.rst

Authorization Decision and Override Rules
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Output Model**

The Authorization Decision can be:

- **EUDIW-Authorization**:

    - `AUTHORIZED` if the condition `authz_art_state == REGISTER_VALID OR authz_art_state == CERTIFICATE_VALID AND edp_state == EDP_SATISFIED AND authz_val_state == VERIFICATION_PASSED` is satisfied; and 
    - `NOT_AUTHORIZED` otherwise. 

- **OIDFED-Authorization**:

.. warning::

    TODO

    It is easier if the state variables are aligned with the EUDIW model, since the TM is strucured in the same way it should not be a problem. In this case the section 

**Override Principles**

A `NOT_AUTHORIZED` decision can be either *non-overridable* (the Wallet Unit blocks the interaction) or *overridable* (the Wallet Unit presents the negative outcome and the User can choose to proceed).

- During **Credential Issuance** phase, all negative verification outcomes MUST be *non-overridable*: the Wallet Unit MUST NOT let the User interact with providers whose registration cannot be confirmed.

- During the **Presentation** phase, all negative verification outcomes MUST be *non-overridable*, except for the following cases:

    - **Negative scope comparison**. If `authz_art_state == REGISTER_VALID OR authz_art_state == CERTIFICATE_VALID AND edp_state == OVERASKING_DETECTED`, i.e. the Authorization Artifact Validation has had a positive outcome but the Scope Comparison finds the Relying Party requesting .
    - **Negative Embedded Disclosure Policy evaluation**. If `authz_art_state == REGISTER_VALID OR authz_art_state == CERTIFICATE_VALID AND edp_state == EDP_NOT_SATISFIED`, i.e. the Authorization Artifact Validation has had a positive outcome but the Embedded Disclosure Policy would not allow the presentation to the Relying Party.

All other presentation failures, including binding failures or intermediary binding failures, MUST NOT be overridable because they indicate an integrity problem rather than a user-facing choice.

In case of non-overridable failures, the Wallet Unit MUST clearly inform the User about the negative outcome. User-relevant information about overridable outcomes MUST be presented as advisories, and the User approval MUST be a separate step from the authorization decision.

.. note:: 
    **User opt-in**.
    The *Scope Comparison Procedure* in :ref:`trust-evaluation:Authorization Validation Procedure` is executed only if the User enabled registration verification. Override mechanisms define what happens when the procedure produces a negative result.

The following table details the override behavior for each procedure when it provides a negative outcome. Each row identifies a procedure, the phase in which it applies, the result code produced on failure, and whether the User can override that outcome.

.. list-table:: Evaluation Procedure Outcomes and Override Rules
   :header-rows: 1
   :widths: 30 15 25 30

   * - Evaluation Procedure
     - Phase
     - Negative Outcome
     - User Override
   * - Wallet-Relying Party Registration Certificate Validation
     - Both
     - ``CERTIFICATE_INVALID``
     - It triggers Register Validation* as fallback. User is not involved.
   * - Register Validation
     - Issuance
     - ``FAILED``
     - Non-overridable.
   * - Register Validation
     - Presentation
     - ``FAILED``
     - Overridable. Advisory to User.
   * - Binding Verification
     - Issuance
     - ``BINDING_FAILED``
     - Non-overridable.
   * - Binding Verification (direct RP)
     - Presentation
     - ``BINDING_FAILED``
     - Non-overridable.
   * - Binding Verification (intermediary)
     - Presentation
     - ``INTERMEDIARY_NOT_AUTHORIZED``
     - Non-overridable.
   * - Entitlement Verification
     - Issuance
     - ``WRONG_ENTITLEMENT``
     - Non-overridable.
   * - Entitlement Verification
     - Presentation
     - ``WRONG_ENTITLEMENT``
     - Overridable. Advisory to User
   * - Attestation Type Verification
     - Issuance
     - ``ATTESTATION_TYPE_NOT_REGISTERED``
     - Non-overridable.
   * - Scope Comparison
     - Presentation
     - ``OVERASKING_DETECTED``
     - Overridable. Advisory to User.
   * - Embedded Disclosure Policy (EDP) Evaluation
     - Presentation
     - ``EDP_NOT_SATISFIED``
     - Overridable. User can deny or allow.

.. warning::

    TODO

    Check the table. Some entries like wrong entitlements should be non-overridable, but the table says they are. The table is copy-paste from APTITUDE.

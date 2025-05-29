.. include:: ../common/common_definitions.rst


Digital Credential Lifecycle
============================

The Credential Issuer is responsible for creating and issuing Digital Credentials, as well as managing their lifecycle and validity status.

The Authentic Source is the entity responsible for the management and provisioning of User's attributes to Credential Issuers.
There is a relationship between the lifecycle of the attributes managed by the Authentic Source and the Digital Credential lifecycle
managed by the Credential Issuer. Indeed, one of the reasons for revocation or suspension of Digital Credentials is the update/revocation or
suspension of the attributes contained in the Digital Credential. In IT Wallet, the provisioning of User's attributes and the notification of
updates or changes in the state of the attributes are exchanged using the PDND infrastructure (see relative sections for more details).


:numref:`fig_DigitalCredential_States` shows the states and transitions for Digital Credentials.
It includes four distinct states: **Issued**, **Valid**, **Expired**, and **Revoked**. While, in case of (Q)EAAs there is an additional state: **Suspended**.
A Digital Credential in all states can be deleted (**PID/(Q)EAA DEL**) and this ends its lifecycle.

.. _fig_DigitalCredential_States:
.. plantuml:: plantuml/credential-states.puml
    :width: 80%
    :alt: The figure illustrates the Digital Credential States.
    :caption: `Digital Credential State Transactions. <https://www.plantuml.com/plantuml/svg/RP9HRzCm4CVV_IbEtSC0AIAK5Q4ze4Lh2fK6b6MRa807BxwrLXmxifsDWFZks8udjr7xLF_kVtS_dN9XBDMsRmNPSOQ0RMS7O6XgpJlBbIHMTM0Lt2jhLGkCQwm39wUGPV0H9Meg7ATRJLimTX1SRbs9c8RBZdh8y87smgwKj1N_W_1clbUiBBLOQAsUBfLG6ku5hPkZzKz8MUX_EorVSOatErut4es1UNJxJ1k4McbdQ81A1iB539XMARj3VUYeLI_PPGZ3F8VuEmL1zHPr70EQCjwRr1P6sg53w9GO_2EszIOXFzkweqIj9JvuQBou2HB-7nH2L2EY1cRk1UDp1l2Nn4pLcmubGmOdgrMnoFF8h_5HDPuktvqjpXQHbhyxhXEDwsyqbOPRhcHO_ZnwRKoFxAk-euApe30IK1e2cpaD6Ar702Tv_Zvt3Wx_UFKBCistEvjzWDXu3flrylMBRo_BelWfrrK5168jPVsaQVJHCsu729-c8V-SvA5UnjIJTDtf7kVmt5tTLfjft4NZYIQhhiixE1AEbvk4o-yRGjBAhEzSzB0vQTn-yI8fFf7O5vY4qlAznK326T974a_WBp_HN9PNvCADwrln7m00>`_


.. .. figure:: ../../images/DigitalCredential_States.svg
..     :figwidth: 100%
..     :align: center
..     :target: https://www.plantuml.com/plantuml/png/RP9HRzCm4CVV_IbEtSC0AIAK5Q4ze4Lh2fK6b6MRa807BxwrLXmxifsDWFZks8udjr7xLF_kVtS_dN9XBDMsRmNPSOQ0RMS7O6XgpJlBbIHMTM0Lt2jhLGkCQwm39wUGPV0H9Meg7ATRJLimTX1SRbs9c8RBZdh8y87smgwKj1N_W_1clbUiBBLOQAsUBfLG6ku5hPkZzKz8MUX_EorVSOatErut4es1UNJxJ1k4McbdQ81A1iB539XMARj3VUYeLI_PPGZ3F8VuEmL1zHPr70EQCjwRr1P6sg53w9GO_2EszIOXFzkweqIj9JvuQBou2HB-7nH2L2EY1cRk1UDp1l2Nn4pLcmubGmOdgrMnoFF8h_5HDPuktvqjpXQHbhyxhXEDwsyqbOPRhcHO_ZnwRKoFxAk-euApe30IK1e2cpaD6Ar702Tv_Zvt3Wx_UFKBCistEvjzWDXu3flrylMBRo_BelWfrrK5168jPVsaQVJHCsu729-c8V-SvA5UnjIJTDtf7kVmt5tTLfjft4NZYIQhhiixE1AEbvk4o-yRGjBAhEzSzB0vQTn-yI8fFf7O5vY4qlAznK326T974a_WBp_HN9PNvCADwrln7m00

..     Digital Credential Lifecycle.

.. note::
  Users MAY present a Digital Credential in any state, it is up to the Relying Party's policy to accept a not Valid Digital Credential.
  An example of this scenario is when a Relying Party needs to verify that the User is not a minor. In this case, even if the User presents an
  **Issued/Expired/Revoked** or **Suspended** Digital Credential, the age claim is still reliable.

.. note::
  While **Issued**, **Valid**, **Expired**, **Revoked** are explicitly mentioned in the ARF (see Figure 5 of ARF v1.4),
  **Suspended** is implicitly present in `EIDAS-ARF`_. This specification explicitly considers it.

Credential Transitions
----------------------

Credential Transition to Issued
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For the state machine to start, the Wallet Instance MUST be in either the **Operational** or **Valid** state, enabling Digital Credentials to be issued to it.
The state machine begins with the **Issued** state, when an issuance process is triggered and, as a result, a Digital Credential is issued to the
Wallet Instance (**PID/(Q)EAA ISS**). Please refer to :ref:`credential-issuance:Digital Credential Issuance`.

Credential Transition to Valid
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A Digital Credential changes to **Valid** state when:

  * it reaches its start date of validity;
  * an unsuspension process is triggered if the (Q)EAA has been suspended.


Credential Transition to Expired
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A Digital Credential naturally transitions to the **Expired** state when it automatically expires upon reaching its end date of validity (**PID/(Q)EAA EXP**),
indicating they are no longer valid for use.

If a Digital Credential is **Expired** the Wallet Instance SHOULD notify the User the Digital Credential has expired and the User MAY delete it (**PID/(Q)EAA DEL**).
This ends its lifecycle.

Credential Transition to Revoked
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A Digital Credential changes from **Issued**, **Valid** or **Suspended** states to **Revoked** state when it is actively revoked by the Credential Issuer
by a revocation process (**PID/(Q)EAA REV**). The Relying Parties SHOULD no longer consider usable a particular Digital Credential when it is **Revoked**, even though it is
still valid temporally and contains a valid Credential Issuer signature. Revocation can occur in the following cases:

  * for technical security reasons relating to the compromise of cryptographic material;
  * in case of explicit User requests;
  * as a consequence of an attribute update by Authentic Sources;
  * in case of a revocation of the attributes contained in the Digital Credential notified by the Authentic Source;
  * death of the User;
  * revocation of Wallet Instance to which the Digital Credential was issued;
  * illegal activities of the User reported by Judicial or Supervisory Bodies.

In the case of PID only, the following cases are in addition to those listed above:

  * detection of a breach of the digital identity issued by an Identity Provider and used to authenticate the User during the PID Issuance;
  * as a result of obtaining a new PID on a new Wallet Instance from the same Wallet Provider that has provided the Wallet Instance containing a PID previously issued.

.. note::
  A (Q)EAA Provider MAY revoke a (Q)EAA in case of PID revocation.

When a Digital Credential is **Revoked** it cannot transition back to **Valid**, the Wallet Instance SHOULD notify the User the Digital Credential
has been revoked and the User MAY delete it (**PID/(Q)EAA DEL**). This ends its lifecycle.

Credential Transition to Suspended
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A (Q)EAA changes from **Issued** or **Valid** states to **Suspended** state when it is suspended by the Credential Issuer (**(Q)EAA SUSP**).
The (Q)EAA remains **Suspended** until it is restored to the **Issued** or **Valid** state (**(Q)EAA UNSUSP**) depending on the previous state, i.e.
the conditions leading to its suspension are resolved, or it changes in **Revoked**, **Expired** or it is deleted. The suspension of a (Q)EAA MAY be:

  * Use case driven, based on the validity status of the attributes contained in the (Q)EAA. In this case, an Authentic Source MUST notify the Credential Issuer of any changes in the state of the attributes attested by the (Q)EAA.
  * Explicitly requested by the User.

Credential Lifecycle Management
-------------------------------

While :numref:`fig_DigitalCredential_States` shows the different states a Digital Credential may acquire during its lifecycle,
:numref:`fig_DigitalCredential_Lifecycle` shows the point of view of Wallet Instances and Credential Issuers in managing the Digital Credential lifecycle
and the effect on their local storage.

.. _fig_DigitalCredential_Lifecycle:
.. plantuml:: plantuml/credential-lifecycle.puml
    :width: 99%
    :alt: The figure illustrates the Digital Credential Lifecycle.
    :caption: `Digital Credential Lifecycle Management. <https://www.plantuml.com/plantuml/svg/ZLHTRnCn47pthnYUQAMqLA9FAOM6faYH2gf2IeLQ5BbtUuc5OmVlNjBowucT3-LYABc7ABPdzcCywmiM7QIUMFNAkCBM9U7TvUcRozDXzzdfYIdUAwKIHZalX616Or5tOtBGw9gH4Mrn6QWa9qPREAAI8HwFX7fQQg6o1HdJDgR7N5DWVEvy1vCheU6ycCeKMentaHqPjqm1DHitWaQWaM6XG2LyBKU-EdhKhaJX9vFQhOd5M3j7zbZ5eB5SfTefYf-IOznfQqdGSopQ5NIcbAbmqAUPN_4d52COdk31uHnVHKlDk3Oi-708YKqVF1CVAYW0xJv9C3IZ1d3WVv93vKE4WCK7AhUQvxEqdxIqL4bQzUbNRI9k7bCuZvcsfan7UMXwCYoS3ZTjnaNiPKla5T4ut9yydRnjOV5x-cEdZVYHPSA1yuTGsFvO_5HXbSPKge5LSPahq66c4ANa_HI8RjfFWaRilqdmWWRdw7tvrhdkTVFkrwHYGnfo8WrB4ctiSLmHZDkWxszlkft1LGkTmQ3V-tWxk1ekTt9jzvIteV3Urx7yRJJHAGfYNjaawPULjFdo-Xh7oy6e0l5ultX0Uw5s43HPdwoVB-_xfNoP7i368ZjxM6RH3excwIM9eungaMSNEJSoJe_8QqQdZdNB-g7OWcPpbDz9ljhyYSyBkZV-1WtnnIEiHcC3ZVNc3-PQdCoxlFPkdDiMVC23-uzBppDF_lk-sd7WY2K9bEJnmVnEwfnjup9NDF34knaoJ_X0iVMivHVya3aYkuECk6_6dQbfTycI4AQ1PiRNtE2eLC35Wb9Fx1y0>`_

.. .. figure:: ../../images/DigitalCredential_Lifecycle.svg
..     :figwidth: 100%
..     :target: https://www.plantuml.com/plantuml/svg/XP91Yzim48Nl_XMgsOC3sVMbfq9WKzjq0sbZR8UbK0YoDIW2MV9AetL3wN-lvBPkIbro2T7JzvxVY7cqI0swNaPlXEgaOq3EY8DzbwQ6ZWzSuDcrpeBfj49G-D3fFXqaLS5pRv59qQRPs_ioICUF-xId5i5uwPHv1nKApCCGyfzsUN6gcw8g3itdiaXMKLG_7PvFPL7LXq-dyb0rrNRN17tBM0MoeJo9MHkloHt2Lyoqr6OJQqCLXo1AdxqerdYHG3Oaf_OCRE-LPELJtskd63MNnBLh4ZzJAG79JbcagWFo-pPUaMyHYGYfBnQXJsZtukbSS85Kaim00uN2_zrsBqvOWKAhs1Fnwe-7WLpsv23Xok0TyoFbRJ9Qr6OTr_wNSfX3e-_HLVakbB-At5dhmFnTVox2GIqN-G0A35tgRk1rsLB1g-ucI_f5rSuEe6mu79MT3tFOzLZJL6GUwnya6LoupobIKZh3XU8JjBwpWn48czZeLgCtXOUeGFxi-2lsMERRfWY6QL4ejvkmDAi0XkGPp8jzyL-GWvh1h2gM4oToseVn5Xh8QGl6Mr-Vvnbl3VG8YhbU_W00

..     Digital Credential Lifecycle Management.

A User, through the Wallet Instance, is able to acquire a new Digital Credential (**Credential Acquisition**) performing the **PID/(Q)EAA ISS** process. This MUST result in the storage of a
Digital Credential in the **Issued/Valid** state, and delete it when it is not needed anymore or it is **Expired/Revoked** (**Credential Deletion**).
Until the **Credential Deletion**, a Digital Credential can be presented to Relying Parties, this operation will not affect its lifecycle.

A Credential Issuer instead is responsible for:

  * **Digital Credential Generation**: the Digital Credential is generated as a consequence of an issuance request and MUST be added to the local storage of the Credential Issuer after the successful issuance.
  * **Digital Credential Revocation/Suspension/Unsuspension** (**PID/(Q)EAA REV** and **(Q)EAA SUSP/UNSUSP**): for technical security reasons or triggered by external entities (e.g., Users and Authentic Sources) the Digital Credential state MUST be locally updated.
  * **Data Purging**: after reaching the **Expired** state, and based on the Credential Issuer retention policies, Digital Credentials MUST be removed from the local storage of the Credential Issuer.

Digital Credential Revocation and Suspension
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section describes the flows to request a Digital Credential status update (i.e. revocation or suspension), involved entities, and validation mechanisms for Digital Credentials in the IT-Wallet system.

As highlighted in Section :ref:`credential-revocation:Digital Credential Lifecycle`, a Digital Credential's lifecycle is affected by:

  - The lifecycle of its storing Wallet Instance
  - The validity of Attributes managed by Authentic Sources
  - For PIDs only, the status of the Digital Identity used for User authentication

External user-related factors can also influence a Digital Credential's lifecycle, such as:

  - Explicit request from the Digital Credential holder
  - User's death
  - Illegal activities

Entities Involved
^^^^^^^^^^^^^^^^^

While the Credential Issuer MUST directly manage the validity status of Digital Credentials it has issued, other actors MAY trigger the Digital Credential revocation/suspension process:

  - Users, through:
  
    - Their Wallet Instance
    - Web service provided by the Issuer
  
  - The Authentic Source when Credential attributes are updated or change validity status
  - The Wallet Provider when revoking a Wallet Instance
  - The Identity Provider if the Digital Identity used for PID issuance is stolen or compromised
  - Legal authorities or the Supervisory Body in cases of proven illegal activities

The following figure shows an entity relationships diagram relating to the Update Flow status.

.. _fig_entity-relation-credential-revocation:
.. plantuml:: plantuml/credential-revocation-entities.puml
    :width: 99%
    :alt: The figure illustrates the Entities involved in Credential Revocation Flow.
    :caption: `Entities involved in Credential Revocation Flow. <https://www.plantuml.com/plantuml/svg/RPJDZjCm4CVlUOgX5ne9QIzxH6ZPR1150gfs4U8KkV5GHgHsv8-KW7XtngcJXhYLAjUJcVd_vYDzi4uOvqyDbCgH8xH0gjDDXv9_G65G8ZyG3UomqxLmf1MyQ_GvUq6gRhn4U5tStnNtLQ5FhLRi_2RBtc-Uoch_NExApy_VjkKwpx8j6glLsbiqhs3rXOyLduDe3_giI1r1qf4SIzMJgbrnwAFsIWhJhy-YQT1LjhSEJnpzTRZ3VhYlSlYJ0NycaD6V51UfQhn6RA8b88JlHw744Iq4kfSMdY97CUUudRirkYF9DOsfjz4mfevt2mjf44h26G_0aXtL61J-PjbLG7Zt8uZNbTNU3FHlHnFi1rEY4TeAmZb31-_uxZHm16oizMW6nLEiD9WxqP0CxMSYvmF0f5wLlou4sj1lbDL1opu0J9PfNKQ6lMz38LQR_d5m_k0brM5nOf1ZsqRYPU1Jb_9voJHmSh9huoFxg3BSx7-LfCCQ7iV1s6MFPt9ntQhhkh52ccxKBhHoWfITDpWefMtCiXqsSTMNUmAhy2BzH5YkOfu6pHRt2Tc0SwgvVspSbFj64Va5Ai59fMxpsIYO-4_QdxIZx_sjUSW0Jrg552b3cc8X3MRwwubb92z7ccCs9DzA4SurJyhpgSroPdaaIpP-cNN3OCUmqxMZxhB_aIXwfZirTVHkxssBIdB40n_-rFm3>`_


.. .. figure:: ../../images/entity-involved-credential-revocation.svg
..   :figwidth: 100%
..   :align: center
..   :target: https://www.plantuml.com/plantuml/svg/RPFFRjGm4CRlUOfXBsmasbmuSIhTHc8HXLMt5U8KUMEpjN3io1xl4X3lpjXrcYZUI9NhgUVxVlEdDmwPHT-fedWZTQiy5_2CsBiFLMNP-VeeyTaVl1EsDHg5nklMT5Mlc0v9LmwvaeTgy_vg5q9Fzr-gZZaKbaBDndIzqI6dZmQVjdTrit-i7-flZpzszReiYfsmpkXrq7y7goSwLdJM6YKEOCvQwYDmIH1CGMi59p79b5jHwgtncZCxhCzCAO6D6yYte-plyGxxU5-LyBS0-bvXnlTIEsIw5LF6DaK2GlYvPveTXOD0zzR1NUBOp3akQ_VMd2IdcaRfNGgCqkdkO64DJ7CuYmEGvKcs8ZZyAuh9W7by3kPjuuotaVxZ689z36KUeQt04AqyUAGx6g0Cs3hdXOsENQeqX4zCIHxQJqJe2M1oR-hVBmJ6oZ-2DmV3XmWmHY1EJWetCknz7mfnnWwtyV5dpsKhcOAKX1JRSX47FdMfd9Si8oU9JOrFxADBlBbP9PU65V-S1kEMFPxPfNLhfdKZXrnkzDuOZKngDszmSChRM1GFGgLLN-u9h1x4oVmIi5p5SfQKB-wTe82OKytVXyRDjIyKKRv0PJYvrMK-bmoNxoVlhmRbp-7IF7Y0bqO7YPmXarXQWoMYbYM5897zSsGQyo7vdhDmhcbIdavZbpCh4rcsyKlLBO4TmqwtA4zn_qUYz3BVgTUELdllUg5vo0ZV3VtkE_KV

..   Entities involved in Credential Revocation Flow


Status Update Flows
^^^^^^^^^^^^^^^^^^^

This section describes the main flows for managing Digital Credential Status Updates by the Issuer, in particular Status Update:

  - related to the User;
  - triggered by a Wallet Instance;
  - triggered by a Wallet Provider;
  - triggered by an Authentic Source.

.. note::
  Detailed Status Update Flows for Identity Providers, legal authorities, and the Supervisory Body will be covered in future versions of the technical specification.

Status Update related to the User
"""""""""""""""""""""""""""""""""

Users MAY change their Digital Credential validity status by:

  1. Deleting the Digital Credential from their Wallet Instance: the Wallet Instance MUST use the Notification Endpoint provided by the Issuer as described in Section :ref:`credential-revocation:Status Update by Wallet Instance`.
  2. Using the Issuer's web portal:

    a. Users MAY access a secure area with at least the same Level of Assurance used during the issuance phase.
    b. The Issuer MUST allow Users to:

      - View all their Digital Credentials contained in the Issuer's database.
      - Verify data authenticity.
      - View and update validity status (revoke their Digital Credentials and, if it is supported by the Issuer, suspend them).

.. note::
  If the User activates another Wallet Instance from the same Wallet Provider and using the same Wallet Solution and obtains a new PID, the previous PID MUST be revoked, and the previous Wallet Instance MUST transition to operational status.

In case of the death of the User, Issuers and Wallet Provider MUST ensure that Digital Credentials and Wallet Instances owned by the User are revoked.
The User's death triggers a change in the validity status of the User's identification attributes contained in the public registry (ANPR). The User's death MUST produce the PID revocation. Therefore, the Authentic Source of the PID (ANPR) MUST notify the PID Provider that the User's attributes are no longer valid due to the death of the User. The Authentic Source and the PID Provider MUST use the mechanisms provided in the Section :ref:`credential-revocation:Status Update by Authentic Sources`.

.. note::
  Future versions of this technical specification will define how the information to (Q)EAA Issuers and Wallet Providers are propagated, according to national regulation. Moreover, automated procedures for Credential revocation due to illegal activities will be defined in future specifications.

Status Update by Wallet Instance
""""""""""""""""""""""""""""""""

When the User deletes a Digital Credential from the Wallet Instance, the Wallet Instance MUST notify this event to the Credential Issuer and the Credential Issuer MUST revoke the Digital Credential. To notify this event, the Wallet Instance MUST use the *Notification Endpoint* described in Section :ref:`credential-issuance-endpoint:Notification Endpoint` using the parameter ``event`` set with the value ``credential_deleted``.

When the revoked Credential is the PID, the Credential Issuer MUST send a notification of this event to the User within 24 hours.
For any other Credential different from the PID, the Credential Issuer SHOULD send a notification of this event to the User. The notification to the User might be implemented in several ways, such as using a User's email address, telephone number, or any other verified and secure communication channel, and MUST include all the information about the Credential revocation status. The method used for the notification to the User is out of scope of the current technical implementation profile. When the revocation occurs, the Credential Issuer MUST update the status of the Digital Credential accordingly. When the Notification Response sent by the Credential Issuer is succesfully received by the Wallet Instance, the Wallet Instance MUST delete the Digital Credential.

Status Update by Wallet Providers
"""""""""""""""""""""""""""""""""

In addition to what already defined in :ref:`credential-revocation:Digital Credential Lifecycle`, the Credential Issuer MUST provide a web service (Wallet Instance Revocation endpoint) defined using PDND, as specified in the Section :ref:`credential-issuer-endpoint:e-Service PDND Credential Issuer Catalogue`.
The Wallet Provider that for any reason revokes a Wallet Instance MUST send a notification to Issuers using this endpoint.

Status Update by Authentic Sources
""""""""""""""""""""""""""""""""""

Authentic Sources manage attributes separately from Digital Credentials, which verify authenticity like physical documents. Losing a physical document doesn't mean losing the privileges it represents; it just means the User can't prove them. However, if a User loses privileges due to a serious infraction, the Authentic Source will revoke the related attributes. In such cases, when a User's attributes are updated, Authentic Sources MUST notify Credential Issuers to update the validity status of any Digital Credential containing those attributes.

Credential Issuers MUST provide a web service available via PDND for Credential update notification and validity status as defined in Section :ref:`credential-issuer-endpoint:e-Service PDND Credential Issuer Catalogue`. For the protocol flow, please refer to the Section :ref:`e-service-pdnd:e-Service PDND`.
Authentic Sources MUST use this notification service in the following cases:

  - The value of one or more Attributes contained in the Authentic Source's database has changed.
  - The validity status of the Attributes is updated (revocation or suspension).


Validity Verification Mechanisms
--------------------------------

For the verification of the validity status of a long-lived Digital Credential the OAuth Status List (`TOKEN-STATUS-LIST`_) MUST be supported for both the remote and proximity scenario. In the remote scenario, the Credential Issuer, Wallet Instance and Relying Party MAY support OAuth Status Assertions (`OAUTH-STATUS-ASSERTION`_). The following table sums up the required revocation mechanisms for verifying the status of long-lived Digital Credentials.

.. _table_revocation_mechanisms:
.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Flow**
    - **Revocation Mechanism**
    - **Reference**
  * - Remote
    -
      - [OPTIONAL] OAuth Status Assertion,
      - [REQUIRED] OAuth Status Lists.
    - `OAUTH-STATUS-ASSERTION`_, `TOKEN-STATUS-LIST`_.
  * - Proximity
    - [REQUIRED] OAuth Status Lists.
    - `TOKEN-STATUS-LIST`_.

OAuth Status Assertions
^^^^^^^^^^^^^^^^^^^^^^^

A Status Assertion is a signed document serving as proof of a Digital Credential's current validity status. The Credential Issuer provides these assertions to Users who can present them to Relying Parties together with the corresponding Digital Credentials.

The Status Assertions have the following features:

  - automated issuance, as the User authentication is not required for the provisioning of the Status Assertion;
  - verification of the Digital Credential validity status in both online and offline scenarios;
  - privacy-preserving, according to the following evidences:

    - the Relying Party can check the validity of the Credential during the presentation phase. It is not able to check the validity of a given Digital Credential related to the User over time and out of the scope of the User authentication;
    - the Credential Issuers is not able to know to which Relying Party the Digital Credential or the Status Assertion will be presented;
    - it doesn't reveal any information about the Users or the content of their Digital Credentials.

  - MUST have a validity period not greater than 24 hours.

.. note::
  This specification only support JWT format and the Status Assertion uses ``credential_status_type`` claim instead of ``credential_status_validity``.

The following sections describe how the Digital Credential validation mechanism works through its key phases.


Handling Credential Status with OAuth Status Assertion
""""""""""""""""""""""""""""""""""""""""""""""""""""""

Credential Issuers, once a Digital Credential has been generated and successfully issued, MUST:

  - Store it locally with minimum set of data required to manage its lifecycle, including the validity status of that Digital Credential;
  - Include a specified hash algorithm in the Digital Credential using the ``credential_hash_alg`` claim within the ``status_assertion`` JSON member of the status claim.

Moreover, Credential Issuers MUST add the following parameters within their Metadata:

  - ``status_assertion_endpoint``
  - ``credential_hash_alg_supported``


Wallet Instance Checking Credentials Statuses
"""""""""""""""""""""""""""""""""""""""""""""

A Wallet Instance MUST check periodically the validity status of the Digital Credential that is stored in it, requesting a Status Assertion for each Digital Credential. In this case, the Wallet Instance MUST send a *Status Assertion Request* to the Credential Issuer according to "OAuth Status Assertion Specification" (see `OAUTH-STATUS-ASSERTION`_ for more details) and it is depicted in the following diagram.

.. _fig_entity-relation-credential-revocation-2:
.. plantuml:: plantuml/status-assertion-flow.puml
    :width: 80%
    :alt: The figure illustrates the Status Assertion Flow.
    :caption: `Status Assertion Flow. <https://www.plantuml.com/plantuml/svg/TOv1IyD048Nl-oiUYyUQ7z23L4Im9uiDU50fOpk7XSqapioIl--IQ27GdERmllU-sPcJUkboeEAzbEwRDGoadivf8774TygP7Nkff9mvWWnZMZ9FoXSMJvInDoki4vL261Fk7v2sEBmUMnoTl1WUpRYMUy5BsnxmnZ-5pV4fY3OH9_edJZg75h75HoM0ktdbEl9NtqnXqpJrVeKGghYQnwfUizhGY_6QTaujhcjdukhTtCIULNjT_hPZkPGk_m80>`_


.. .. figure:: ../../images/High-Level-Flow-Status-Assertion-Request.svg
..     :figwidth: 100%
..     :align: center
..     :target: https://www.plantuml.com/plantuml/svg/TOv1IyD048Nl-oiUYyUQ7z23L4Im9uiDU50fOpk7XSqapioIl--IQ27GdERmllU-sPcJUkboeEAzbEwRDGoadivf8774TygP7Nkff9mvWWnZMZ9FoXSMJvInDoki4vL261Fk7v2sEBmUMnoTl1WUpRYMUy5BsnxmnZ-5pV4fY3OH9_edJZg75h75HoM0ktdbEl9NtqnXqpJrVeKGghYQnwfUizhGY_6QTaujhcjdukhTtCIULNjT_hPZkPGk_m80

..     Status Assertion Flow


**Step 1 (Status Assertion Request)**: The Wallet Instance sends the Status Assertion Request to the Credential Issuer, where:

  - The request MUST contain the base64url encoded hash value of the Digital Credential's Issuer signed part, such as the Issuer Signed JWT using :ref:`credential-data-model:SD-JWT-VC Credential Format`, or the Mobile Security Object using :ref:`credential-data-model:mdoc-CBOR Credential Format`, and enveloped in a signed Status Assertion Request object.
  - The Status Assertion Request object MUST be signed with the private key corresponding to the confirmation claim contained within the Digital Credential.

The Status Assertion HTTP request can be sent to a single Credential Issuer regarding multiple Digital Credentials, and MUST contain a JSON object with the member `status_assertion_requests` as described in Section :ref:`credential-revocation:HTTP Status Assertion Request`.

The Credential Issuer that receives the Status Assertion Request object MUST:

  - validate that the Wallet Instance making the request is authorized to request Status Assertions. If errors occur during this check, the Credential Issuer MUST provide a Status Assertion Error Response according to Section :ref:`credential-revocation:HTTP Status Assertion Response`;
  - verify the compliance of all elements in the `status_assertion_requests` object using the confirmation method contained within the Digital Credential where the Status Assertion Request object is referred to. In case of errors, a Status Assertion Error Response MUST be provided (see Section :ref:`credential-revocation:HTTP Status Assertion Response`);
  - verify that it is the legitimate Issuer of the Digital Credential to which each Status Assertion Request object refers;
  - check the validity status for the requested Credentials;
  - creates the corresponding Status Assertion.


**Step 2 (Status Assertion Response)**: The *status_assertion_responses* MUST be an array of strings containing the *StatusAssertionResponse* and/or the *StatusAssertionErrors* JSON Objects related to the request made by the Wallet Instance.

The Wallet Instance MUST:

  - validate the HTTP Status Assertion Response;
  - extract and validate the signatures of each JSON Object within the *status_assertion_responses* JSON Array;
  - present a valid Status Assertion to a Relying Party which request it for the status verification of a Digital Credential (see Section below for more details);
  - inform the User in case of a validity state update of a Digital Credential.

.. note::
  Status Assertion Errors JSON Object MAY have the *alg header parameter* set to *none*. If the Credential Issuer signs the Status Assertion Errors the Wallet Instance MUST validate the signature. Moreover, Status Assertion Errors MUST not be presented to Relying Parties.

Technical details about the HTTP Status Assertion Response is provided in the Section :ref:`credential-revocation:HTTP Status Assertion Response`.

HTTP Status Assertion Request
.............................

The *Status Assertion endpoint* MUST be provided by the Credential Issuer within its Metadata.
The requests to the *Status Assertion endpoint* MUST be HTTP with method POST, using the mandatory parameters listed below within the HTTP request message body. These MUST be encoded in ``application/json`` format.

.. _table_revocation_request_params:
.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Claim**
    - **Description**
    - **Reference**
  * - **status_assertion_requests**
    - It MUST be an array of strings, where each represents a *Status Assertion Request object*. Each element MUST contain a signed JWT, encoded as a series of base64url-encoded values (some of which may be the empty string) separated by period ('.') characters, as a cryptographic proof of possession of the Digital Credential for which the Status Assertion is being requested, according with the Status Assertion Request described in Section 7 of `OAUTH-STATUS-ASSERTION`_. See the :ref:`Table <table_status_assertion_req_obj>` below for more details.
    - This Specification.

Below a non-normative example representing a Status Assertion Request array with Status Assertion Request objects in JWT format.

.. code::

  POST /status HTTP/1.1
  Host: issuer.example.org
  Content-Type: application/json

	{
		"status_assertion_requests" : [
      $status_assertion_request,
      $status_assertion_request,
      ...
    ]
	}

The **Status Assertion Request object** MUST be a JWT that MUST contain the parameters (Header and Payload) in the following table.

.. _table_status_assertion_req_obj:
.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Header**
    - **Description**
    - **Reference**
  * - **typ**
    - It MUST be set to ``status-assertion-request+jwt``.
    - :rfc:`7516#section-4.1.1`.
  * - **alg**
    - A digital signature algorithm identifier such as per IANA "JSON Web Signature and Encryption Algorithms" registry. It MUST be one of the supported algorithms listed in the Section :ref:`algorithms:Cryptographic Algorithms` and MUST NOT be set to ``none`` or any symmetric algorithm (MAC) identifier.
    - :rfc:`7516#section-4.1.1`.


.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Payload**
    - **Description**
    - **Reference**
  * - **iss**
    - Thumbprint of the JWK in the ``cnf`` parameter of the Wallet Attestation.
    - :rfc:`9126` and :rfc:`7519`.
  * - **aud**
    - It MUST be set to the URL string of Credential Issuer Status Assertion endpoint.
    - :rfc:`9126` and :rfc:`7519`.
  * - **exp**
    - UNIX Timestamp with the expiry time of the JWT. It MUST be greater than the value set for `iat`.
    - :rfc:`9126` and :rfc:`7519`.
  * - **iat**
    - UNIX Timestamp with the time of JWT issuance.
    - :rfc:`9126` and :rfc:`7519`.
  * - **jti**
    - Unique identifier for the proof of possession JWT. The value SHOULD be set using a *UUID v4* value according to [:rfc:`4122`].
    - :rfc:`7519#section-4.1.7`.
  * - **credential_hash**
    - It MUST contain the hash value of the Digital Credential's Issuer signed part the Status Assertion is bound to.
    - `OAUTH-STATUS-ASSERTION`_.
  * - **credential_hash_alg**
    - It MUST contain the Algorithm used for hashing the Digital Credential. The value SHOULD be set to `sha-256`.
    - `OAUTH-STATUS-ASSERTION`_.

Below, is given a non-normative example of a single *Status Assertion Request object* with decoded JWT header and payload and without signature for better readability:

.. code-block:: json

  {
    "alg": "ES256",
    "typ": "status-assertion-request+jwt"
  }
  
.. code-block:: json

  {
    "iss": "0b434530-e151-4c40-98b7-74c75a5ef760",
    "aud": "https://pid-provider.example.org/status",
    "iat": 1698744039,
    "exp": 1698744139,
    "jti": "6f204f7e-e453-4dfd-814e-9d155319408c",
    "credential_hash": "$Issuer-Signed-JWT-Hash",
    "credential_hash_alg": "sha-256"
  }

HTTP Status Assertion Response
..............................

In case of succesfully Status Assertion Request validation, the *Credential Issuer* MUST return an HTTP response with the status code set to *200 OK*. If the *Credential Issuer* is able to provide a valid Status Assertion for a requested Credential, the response MUST contain a Status Assertion object within a JSON Array. Otherwise, a Status Assertion Errors related to that Credential MUST be included in the Response JSON Array as an entry.

If the HTTP Status Assertion Request fails (e.g. invalid request, server unavailability, etc.), an HTTP Error Status Code MUST be provided within the Status Assertion Response.

In the following table are listed HTTP Status Codes that MUST be supported:

.. list-table::
  :class: longtable
  :widths: 20 20 60
  :header-rows: 1

  * - **Status Code**
    - **Body**
    - **Description**
  * - *200 Ok*
    - Revocation Response
    - The Revocation Response has been successfully created.
  * - *400 Bad Request*
    - Error code and description
    - The Credential Issuer cannot fulfill the request because of invalid parameters.
  * - *500 Internal Server Error*
    -
    - The Credential Issuer encountered an internal problem. (:rfc:`6749#section-5.2`).
  * - *503 Service Unavailable*
    -
    - The Credential Issuer is temporary unavailable. (:rfc:`6749#section-5.2`).

The HTTP response MUST:

- Include a JSON object with a member named `status_assertion_responses`. It MUST be an array of strings, where each represents a *Status Assertion Response object*. Each element MUST contain a signed JWT, encoded as a series of base64url-encoded values (some of which may be the empty string) separated by period ('.') characters. The *Status Assertion Response object* MUST contain a Status Assertion Response and Status Assertion Error in analogy with Sections 8 and 9 of `OAUTH-STATUS-ASSERTION`_ for more details.

- Be encoded in ``application/json`` format.

A non-normative example of a HTTP Status Assertion Response is given below.

.. code::

    HTTP/1.1 200 Ok
    Content-Type: application/json
    {
      "status_assertion_responses": [
        $status_assertion_response,
        $status_assertion_response,
        ...
      ]
    }

The Status Assertion MUST contain the parameters and claims defined below

.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Header**
    - **Description**
    - **Reference**
  * - **alg**
    - A digital signature algorithm identifier such as per IANA "JSON Web Signature and Encryption Algorithms" registry. It MUST be one of the supported algorithms in Section :ref:`Cryptographic Algorithms <algorithms:Cryptographic Algorithms>` and MUST NOT be set to ``none`` or to a symmetric algorithm (MAC) identifier.
    - [:rfc:`7515`], [:rfc:`7517`].
  * - **typ**
    - It MUST be set to `status-assertion+jwt`.
    - [:rfc:`7515`], [:rfc:`7517`], `OAUTH-STATUS-ASSERTION`_.
  * - **kid**
    - Unique identifier of the Issuer JWK. It is REQUIRED when ``x5c`` is not used.
    - [:rfc:`7515`], `OAUTH-STATUS-ASSERTION`_.
  * - **x5c**
    -  X.509 certificate chain about the Issuer. It is REQUIRED when ``kid`` is not used.
    - [:rfc:`7515`], `OAUTH-STATUS-ASSERTION`_.

.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Payload**
    - **Description**
    - **Reference**
  * - **iss**
    - It MUST be set to the identifier of the Credential Issuer.
    - :rfc:`9126` and :rfc:`7519`.
  * - **iat**
    - UNIX Timestamp with the time of JWT issuance.
    - :rfc:`9126` and :rfc:`7519`.
  * - **exp**
    - UNIX Timestamp with the expiry time of the JWT. It MUST be greater than the value set for `iat`.
    - :rfc:`9126` and :rfc:`7519`.
  * - **credential_hash**
    - Hash value of the Credential the Status Assertion is bound to.
    - `OAUTH-STATUS-ASSERTION`_.
  * - **credential_hash_alg**
    - The Algorithm used for hashing the Credential to which the Status Assertion is bound. The value SHOULD be set to ``sha-256``.
    - `OAUTH-STATUS-ASSERTION`_.
  * - **credential_status_type** [#]_
    - Numerical value indicating the validity of the Credential linked to the Status Assertion describing its state. All values taken from IANA "OAuth Status Types" registry for Status List values (see Section 7 of `TOKEN-STATUS-LIST`_) MAY be supported. Values from ``0x00`` to ``0x02`` MUST be supported with the following meaning:

      - ``0x00 - VALID``: The status of the Digital Credential is valid, correct or legal.
      - ``0x01 - INVALID``: The status of the Digital Credential is revoked, annulled, taken back, or cancelled. This state is irreversible.
      - ``0x02 - SUSPENDED``: The status of the Digital Credential is temporarily invalid, hanging. This state is reversible.

    - This Specification, `TOKEN-STATUS-LIST`_ .
  * - **credential_status_detail**
    - REQUIRED only if **credential_status_type** is not set to `0x00`. Object containing detailed information about the status of the Credential. It contains:

        - **state**: (REQUIRED). String value of the Credential status. It is used to convey a more granular representation of a Digital Credential status, for example "revoked", "annulled", "debarred", etc. or in case of application specific Credential states. The Credential Issuer MUST provide a list of status supported for the issued Credential in the Credential Issuer Metadata.
        - **description**: (REQUIRED). String containing the description of the Credential status.
    - `OAUTH-STATUS-ASSERTION`_.
  * - **cnf**
    - JSON object containing confirmation methods. The sub-member contained within `cnf` member, such as `jwk` for JWT, MUST match with the one provided within the related Digital Credential. Other confirmation methods can be utilized when the referenced Digital Credential supports them, in accordance with the relevant standards.
    - Section 3.1 of :rfc:`7800` and Section 3.1 of :rfc:`8747`.

.. warning::
  .. [#] This specification uses ``credential_status_type`` instead of ``credential_status_validity`` currently supported in `OAUTH-STATUS-ASSERTION`_ as the value is semantically a status type and not a boolean.

Below a non-normative example of a Status Assertion Response object in JWT format, with the headers and payload represented in JSON and without applying the signature.

.. code::

  {
    "alg": "ES256",
    "typ": "status-assertion+jwt",
    "kid": "Issuer-JWK-KID"
  }
 .
  {
    "iss": "https://issuer.example.org",
    "jti": "6f204f7e-e453-4dfd-814e-9d155319408c"
    "credential_hash": $CREDENTIAL-HASH,
    "credential_hash_alg": "sha-256",
    "credential_status_type": 0x01,
    "credential_status_detail": {
      "state": "revoked",
      "description": "The Credential is no longer usable as it has been revoked. This state is irreversible"
    },
    "cnf": {
      "jwk": {
        "kty": "EC",
        "crv": "P-256",
        "x": "_2ySUmWFjwmraNlo15r6dIBXerVdy_NpJuwAKJMFdoc",
        "y": "MV3C88MhhEMba6oyMBWuGeB3dKHP4YADJmGyJwwILsk"
      }
    }
  }

The Status Assertion Error object MUST contain the following claims:

.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Header**
    - **Description**
    - **Reference**
  * - **alg**
    - A digital signature algorithm identifier such as per IANA "JSON Web Signature and Encryption Algorithms" registry. It MUST be one of the supported algorithms in Section :ref:`Cryptographic Algorithms <algorithms:Cryptographic Algorithms>` and MUST NOT be set to ``none`` or to a symmetric algorithm (MAC) identifier.
    - Section 4.1.1 of [:rfc:`7516`].
  * - **typ**
    - It MUST be set to `status-assertion+jwt`.
    - Section 4.1.11 of [:rfc:`7516`].

.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Payload**
    - **Description**
    - **Reference**
  * - **iss**
    - It MUST be set to the identifier of the Credential Issuer.
    - :rfc:`9126` and :rfc:`7519`.
  * - **jti**
    - Unique identifier for the JWT.
    - :rfc:`9126` and :rfc:`7519`.
  * - **credential_hash**
    - Hash value of the Credential the Status Assertion Error is bound to, it MUST match the one contained in the Status Assertion Request.
    - `OAUTH-STATUS-ASSERTION`_.
  * - **credential_hash_alg**
    - The Algorithm used for hashing the Credential to which the Status Assertion Error is bound, it MUST match the one contained in the Status Assertion Request. The value SHOULD be set to ``sha-256``.
    - `OAUTH-STATUS-ASSERTION`_.
  * - **error**
    - The error code, as registered in the table below.
    - Section 4.1.7 of :rfc:`7519`.
  * - **error_description**
    - Text providing further details to clarify the nature of the error encountered.
    - Section 4.1.7 of :rfc:`7519`.

Errors are meant to provide additional information about the failure so that the User can be informed and take the appropriate action.
The `error` claim for the Status Assertion Error object MUST be set with one of the values defined in the table below, in addition to the values specified in :rfc:`6749#section-5.2`:

.. list-table::
    :class: longtable
    :widths: 20 80
    :header-rows: 1

    * - **Error Code**
      - **Description**
    * - ``invalid_request``
      - The request is not valid due to the lack or incorrectness of one or more parameters. (:rfc:`6749#section-5.2`).
    * - ``invalid_request_signature``
      - The Status Assertion Request signature validation has failed. This error type is used when the proof of possession of the Digital Credential is found not valid within the Revocation Assertion Request. (Section 9.2 of `OAUTH-STATUS-ASSERTION`_).
    * - ``credential_not_found``
      - The `credential_hash` value provided in the Status Assertion Request doesn't match with any active Digital Credential. (Section 9.2 of `OAUTH-STATUS-ASSERTION`_).
    * - ``unsupported_hash_alg``
      - The hash algorithm set in `credential_hash_alg` is not supported. (Section 9.2 of `OAUTH-STATUS-ASSERTION`_).

Below a non-normative example of a Status Assertion Error object in JWT format, with the headers and payload represented in JSON and without applying the signature.

.. code::

  {
    "alg": "ES256",
    "typ": "status-assertion-error+jwt",
    "kid": "Issuer-JWK-KID"
  }
  .
  {
    "iss": "https://issuer.example.org",
    "jti": "6f204f7e-e453-4dfd-814e-9d155319408c"
    "credential_hash": $CREDENTIAL-HASH,
    "credential_hash_alg": "sha-256",
    "error": "unsupported_hash_alg",
    "error_description": "The hash algorithm is not supported"
  }

Relying Party Checking Credential Status
""""""""""""""""""""""""""""""""""""""""

During the presentation flow, if a Status Assertion related to a Digital Credential is available, the Wallet Instance MUST include it along with the related Digital Credential in the ``vp_token`` JSON Array.
The Relying Party who wants to rely on the mechanism provided by Status Assertion MUST extract the Status Assertion from the ``vp_token`` Array, and, in addition to the checks required in the Presentation Flow described in the Section :ref:`remote-flow:Remote Flow`, the Relying Party MUST check the presence of ``status.status_assertion`` claim in the Digital Credential. If true, the Relying Parties MUST:

  - validate the signature of the Status Assertion;
  - decode the Status Assertion provided in the presentation, by matching the JWS Header parameter typ set to ``status-assertion+jwt`` and looking for the ``credential_hash`` value that matches with the hash of the Digital Credential's Issuer signed part using the hashing algorithm configured in ``status.status_assertion.credential_hash_alg``;
  - evaluate the Status Assertion by checking the following items:

    - the ``iss`` claim value MUST match the one in the Digital Credential;
    - the ``iat`` claim value MUST be equal to or later than the ``iat`` claim value in the Digital Credential;
    - the ``exp`` value MUST be later than the current time;
    - the ``nbf`` claim value, if present, MUST be less than or equal to the current time;
    - the ``cnf`` JSON Object MUST match the one included in the related Digital Credential;
    - the ``credential_status_type`` and ``credential_status_detail`` values.


OAuth Status Lists
------------------

This section defines a Status List data structure, which is used to convey information regarding the individual statuses of multiple Digital Credentials. Digital Credentials may be of any format, such as SD-JWTs or ISO/IEC 18013-5 mdocs. A Status List describes the status of the Digital Credentials by encoding their status validity in a bit array. Each Digital Credential is allocated an index during issuance; this index represents its position within the bit array. The value of the bit(s) at this index corresponds to the Digital Credentials' status. A Status List is provided within a cryptographically signed Status List Token in JWT format. For details, see `TOKEN-STATUS-LIST`_.

In this specification, the roles of Credential Issuer and Status Issuer (i.e., the entity that issues the Status List Token about the status information of the Digital Credential) coincide, whereas the Status Provider (i.e., the entity that provides the Status List Token on a public endpoint) MAY be the Credential Issuer itself or another entity.

Status Lists Creation
^^^^^^^^^^^^^^^^^^^^^

The Issuer of the Digital Credentials MUST

  - define a number of bits, k, (either 1, 2, 4, 8) that represents the amount of bits used to describe the status of each Digital Credential within this Status List. The Credential Issuer MUST configure the number of bits. Each Credential will therefore have 2^k (where k is the number of bits chosen) possible states.
  - create a byte array of size = (amount of Digital Credentials) * k / 8 or greater. Depending on k, each byte in the array corresponds to 8/k statuses (8 if k=1, 4 if k=2, 2 if k=1, or 1 if k=8). Each time a Digital Credential is issued the Credential Issuer assigns it to a position in the array.
  - set the status values for all issued Digital Credentials within the byte array. The status of each Digital Credential is identified using an index that maps to one or more specific bits within the byte array. The index starts counting at 0 and ends with (amount of Digital Credential) - 1 (being the last valid entry). The bits within an array are counted from the least significant bit ("0") to the most significant bit ("7"). All bits of the byte array at a particular index are set to a status value.
  - compress the byte array using DEFLATE [:rfc:`1951`] with the ZLIB [:rfc:`1950`] data format. Implementations are RECOMMENDED to use the highest compression level available.
  - make available to Relying Parties, and Wallet Instances, an endpoint to request Status Lists.

The Issuer of a Digital Credential MUST use the following values for possible Statuses of the issued Digital Credentials:

  - 0x00 - ``VALID`` - The Digital Credential is valid.
  - 0x01 - ``INVALID`` - The Digital Credential is revoked.
  - 0x02 - ``SUSPENDED`` - The Digital Credential is temporarily invalid, hanging. This state is reversible.
  - 0x03 - ``UPDATE`` - The Digital Credential metadata parameters have changed.
  - 0x04 - ``ATTRIBUTE_UPDATE`` - The Digital Credential attributes have changed.

For example, if five states for a certain Digital Credential are possible, then k=4. If the Credential Issuer creates an array to store the statuses of 6 Digital Credentials, whose validity statuses are 0, 0, 0, 4, 1, 2, respectively; it will:

  - create the bite array ``[0, 0, 0, 0, 0, 0, 0, 0; 0, 1, 0, 0, 0, 0, 0, 0; 0, 0, 1, 0, 0, 0, 0, 1]`` which in exadecimal notation generates the byte array ``[0x00, 0x40, 0x21]``.
  - compress the array using DEFLATE.

.. note::
  When the Credental Issuer choses the number of bits for conveying statuses of the Digital Credentials it issues, it MAY add other states besides those described above. The addition of many different states for the lifecycle of a Digital Credential has however to be carefully pondered for it discloses information to Relying Parties.

.. note::
  The main privacy consideration for a Status List is to prevent the Issuer from tracking the usage of the Digital Credential when the status is being checked. If a Credential Issuer offers status information by referencing a specific token, this would enable the Credential Issuer to create a profile for the issued token by correlating the date and identity of Relying Parties, that are requesting the status. Implementations MUST therefore integrate the status information of many Digital Credentials into the same list. As a result, the Issuer does not learn for which Digital Credential the Relying Party is requesting the Status List. The privacy of the User is protected by the anonymity within the set of Digital Credential in the Status List, this limits the possibilities of tracking by the Issuer.
  This herd privacy effect depends on the number of entities within the Status List. A larger amount of Digial Credentials referenced therein results in better privacy but also impacts the performance as more data has to be transferred to read the Status List. Depending on the Status List parameters (e.g. the amounts of bits designating the Credential values), Credential Issuers have to strike an appropriate balance between privacy and performance.

Once the Relying Party receives a Digital Credential, this enables it to request the Status List to validate its status through the provided URI parameter and look up the corresponding index. However, the Relying Party is able to store the URI and index of the Digital Credential to request the Status List again at a later time. By doing so regularly, the Relying Party may create a profile of the Digital Credential's validity status. This behaviour might also be abused in cases where this is not intended and unknown to the User, e.g. profiling the suspension of a driving license. This behaviour could be mitigated e.g., by regular re-issuance of the Digital Credential.

Status List Token
"""""""""""""""""

The Status List Token is available at the Status List Endpoint and contains the following parameters.

.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Header**
    - **Description**
    - **Reference**
  * - **alg**
    - REQUIRED. A digital signature algorithm identifier such as per IANA "JSON Web Signature and Encryption Algorithms" registry. It MUST be one of the supported algorithms in Section :ref:`algorithms:Cryptographic Algorithms` and MUST NOT be set to ``none`` or to a symmetric algorithm (MAC) identifier.
    - [:rfc:`7515`], [:rfc:`7517`].
  * - **typ**
    - REQUIRED. It MUST be set to ``statuslist+jwt``.
    - `TOKEN-STATUS-LIST`_
  * - **kid**
    - REQUIRED. Unique identifier of the Credential Issuer's public key which signs the Status Token.
    - :rfc:`7638#section_3`.
  * - **x5c**
    - REQUIRED. X.509 public key certificate or certificate chain corresponding to the key used to sign the Status List Token.
    - :rfc:`5280`

.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Payload**
    - **Description**
    - **Reference**
  * - **sub**
    - REQUIRED. The subject claim MUST specify the URI of the Status List Token. The value MUST be equal to that of the uri claim contained in the status_list claim of the Digital Credential.
    - [:rfc:`7519`]
  * - **iat**
    - REQUIRED. The issued at claim MUST specify the time at which the Status List Token was issued.
    - [:rfc:`7519`]
  * - **exp**
    - REQUIRED. The expiration time claim, if present, MUST specify the time at which the Status List Token is considered expired by the Credential Issuer.
    - [:rfc:`7519`]
  * - **ttl**
    - OPTIONAL. The time to live claim, if present, MUST specify the maximum amount of time, in seconds, that the Status List Token can be cached by a consumer before a fresh copy SHOULD be retrieved. The value of the claim MUST be a positive number encoded in JSON as a number. This amount of time SHOULD NOT exceed the expiration time defined in **exp** claim.
    - `TOKEN-STATUS-LIST`_
  * - **status_list**
    - REQUIRED. JSON Object that contains a Status List.
    - `TOKEN-STATUS-LIST`_

.. note::
  It is RECOMMENDED that the Credential Issuer sets the ``exp`` claim so that the Status List Token is short-lived. Typically, this involves the ``exp`` claim not to exeed the ``iat`` claim by more than 24 hours.

A JSON-encoded Status List has the following structure:

.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Parameter**
    - **Description**
    - **Reference**
  * - **bits**
    - REQUIRED. JSON Integer specifying the number of bits per Digital Credential in the compressed byte array (`lst`). The allowed values for bits are 1,2,4 and 8.
    - `TOKEN-STATUS-LIST`_
  * - **lst**
    - REQUIRED. JSON String that contains the status values for all the Digital Credentials it conveys statuses for. The value MUST be the base64url-encoded compressed byte array.
    - `TOKEN-STATUS-LIST`_
  * - **aggregation_uri**
    - OPTIONAL. JSON String that contains a URI to retrieve the Status List Aggregation for this type of Digital Credential or Issuer.
    - `TOKEN-STATUS-LIST`_

The following is an example of Status List Token before applying signature and encoding:

.. code::

  {
    "alg": "ES256",
    "kid": "$KID",
    "typ": "statuslist+jwt"
  }
  .
  {
    "exp": 2291720170,
    "iat": 1686920170,
    "status_list": {
      "bits": 1,
      "lst": "eNrbuRgAAhcBXQ"
    },
    "sub": "https://example-issuer.com/statuslists/",
    "ttl": 43200
  }
 
 
Handling Credential Status with Status List Token
"""""""""""""""""""""""""""""""""""""""""""""""""

Credential Issuers, once a Digital Credential has been generated, MUST:

  - Store it locally with minimum set of data required to manage its lifecycle, including the validity status of that Digital Credential;
  - Include a ``status_list`` claim within the JSON Object value of the ``status`` claim of the Digital Credential.

The value of the claim ``status_list`` MUST be itself a JSON Object with the following parameters

.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Parameter**
    - **Description**
    - **Reference**
  * - **idx**
    - REQUIRED. The idx (index) claim MUST specify an Integer that represents the index to check for status information in the Status List for the current Digital Credential. The value of idx MUST be a non-negative number, containing a value of zero or greater.
    - `TOKEN-STATUS-LIST`_
  * - **uri**
    - REQUIRED. The uri (URI) claim MUST specify a String value that identifies the Status List Token containing the status information for the Digital Credential. The value of uri MUST be a URI conforming to [:rfc:`3986`].
    - `TOKEN-STATUS-LIST`_


Checking Credentials Statuses
"""""""""""""""""""""""""""""

The fetching, processing and verifying of a Status List Token may be done by either the Wallet Instance or a Relying Party. Below it is described for the Relying Party, however, the same rules would also apply to the Wallet Instance.

.. _fig_entity-relation-credential-revocation-SL:
.. plantuml:: plantuml/status-list-flow.puml
    :width: 80%
    :alt: The figure illustrates the Status List Flow.
    :caption: `Status List Flow. <https://www.plantuml.com/plantuml/svg/RS-n2i8m4CRnFKzn15TVm44AWbfm42suk9pj3OVf9UOkvFMDEXMS_p_u-3erp5Rc05T3AmedLeDzYDLXiIXbVb1sgHaUEQ4O-1k6G0QzgA6Cv04LAY_DBjD4Oem1UjL2-QlOkSgmtW9lu42sc3mEmnakz2gavXfggZRsXsYAeWHt0R_wvKyTufF4kuvaQc_U>`_


.. .. figure:: ../../images/High-Level-Flow-Status-List.svg
..   :figwidth: 100%
..   :align: center
..   :target: https:https://www.plantuml.com/plantuml/svg/TOv1IyD048Nl-oiUYyUQ7z23L4Im9uiDU50fOpk7XSqapioIl--IQ27GdERmllU-sPcJUkboeEAzbEwRDGoadivf8774TygP7Nkff9mvWWnZMZ9FoXSMJvInDoki4vL261Fk7v2sEBmUMnoTl1WUpRYMUy5BsnxmnZ-5pV4fY3OH9_edJZg75h75HoM0ktdbEl9NtqnXqpJrVeKGghYQnwfUizhGY_6QTaujhcjdukhTtCIULNjT_hPZkPGk_m80

..   Status List Flow

HTTP Status Lists Request
.........................

To obtain the Status List Token, the Relying Party MUST send an HTTP GET request to the ``status.status_list.uri`` value provided within the Digital Credential.

The Relying Party SHOULD send the ``application/statuslist+jwt`` Accept-Header to indicate that the requested response type for Status List Token is the JWT format.

The following is a non-normative example of a request for a Status List Token:

.. code::

  GET /statuslists HTTP/1.1
  Host: example-issuer.com
  Accept: application/statuslist+jwt


HTTP Status Lists Response
..........................

The Status List Endpoint responds with a Status List Token and MUST use an HTTP status code in the 2xx range. In the successful response, the Status Provider MUST use content-type ``application/statuslist+jwt`` for Status List Token in JWT format.

The HTTP response SHOULD use gzip Content-Encoding as defined in [:rfc:`9110`].

If caching-related HTTP headers are present in the HTTP response, Relying Parties SHOULD prioritize the ``exp`` and ``ttl`` claims within the Status List Token over the HTTP headers for determining caching behavior.

The following is a non-normative example of a response for a Status List Token with type ``application/statuslist+jwt``:

.. code::

  HTTP/1.1 200 OK
  Content-Type: application/statuslist+jwt

  eyJhbGciOiJFUzI1NiIsImtpZCI6IjEyIiwidHlwIjoic3RhdHVzbGlzdCtqd3QifQ.eyJleHAiOjIyOTE3MjAxNzAsImlhdCI6MTY4NjkyMDE3MCwiaXNzIjoiaHR0cHM6Ly9leGFtcGxlLmNvbSIsInN0YXR1c19saXN0Ijp7ImJpdHMiOjEsImxzdCI6ImVOcmJ1UmdBQWhjQlhRIn0sInN1YiI6Imh0dHBzOi8vZXhhbXBsZS5jb20vc3RhdHVzbGlzdHMvMSIsInR0bCI6NDMyMDB9.SSdg3AnTHsyRtCHziLy-QnXg-YRldMEXkdEgDXgE_ZvIvjM0eULQlzEbLBLfCeGhlqKJSReC-m85K79CTjJDzg

Upon receiving a Digital Credential, a Relying Party MUST first perform the validation of the Digital Credential itself (e.g., checking for expected attributes, valid signature and expiration time). If this validation is not successful, the Digital Credential MUST be rejected. If the validation was successful, the Relying Party MUST perform the following validation steps to evaluate the status of the Digital Credential:
 
- Check for the existence of a ``status`` claim, check for the existence of a ``status_list`` claim within the ``status`` claim and validate that the content of ``status_list`` adheres to the rules defined in Section :ref:`credential-revocation:Handling Credential Status with Status List Token`.
- Resolve the Status List Token from the provided URI.
- Validate the Status List Token:

  - Validate the Status List Token's signature by following the rules defined in section 7.2 of [:rfc:`7519`]. This step requires the resolution of a public key as described in :ref:`trust:The Infrastructure of Trust`.

  - Check for the existence of the required claims as defined in Section :ref:`credential-revocation:Status List Token`.

- All existing claims in the Status List Token MUST be checked according to :ref:`credential-revocation:Status List Token`.

  - The subject claim of the Status List Token MUST be equal to the `uri` claim in the `status_list` object of the Digital Credental.
  - If the Relying Party has custom policies regarding the freshness of the Status List Token, it SHOULD check the `iat` claim.
  - If the expiration time is defined, it MUST be checked if the Status List Token is expired.
  - If the Relying Party is using a system for caching the Status List Token, it SHOULD check the `ttl` claim of the Status List Token and retrieve a fresh copy if (time status was resolved + `ttl` < current time).

- Decompress the Status List with a decompressor that is compatible with DEFLATE [:rfc:`1951`] and ZLIB [:rfc:`1950`].
- Retrieve the status value of the index specified in the Digital Credential as described in :ref:`credential-revocation:Status Lists Creation`. Fail if the provided index is out of bounds of the Status List.
- Check the status value as described in :ref:`credential-revocation:Status Lists Creation`.

If any of these checks fails, no statement about the status of the Digital Credential can be made and the Digital Credential SHOULD be rejected.

If for example, the decompressed byte array is ``[0x00, 0x40, 0x21]``, it corresponds to the bit array ``[0, 0, 0, 0, 0, 0, 0, 0; 0, 1, 0, 0, 0, 0, 0, 0; 0, 0, 1, 0, 0, 0, 0, 1]``. The Status of the Digital Credential whose ``idx`` claim value is ``5`` in this array refers to the last 4-bit pair (i.e., ``[0, 0, 1, 0] = 0x02``) whose status value is ``SUSPENDED``.

In case any error occurs when the Status Token Endpoint generates the response, following HTTP Status Codes MUST be supported:

.. list-table::
  :class: longtable
  :widths: 20 80
  :header-rows: 1

  * - **Status Code**
    - **Description**
  * - *500 Internal Server Error* [REQUIRED]
    - The Status List Provider encountered an internal problem.
  * - *503 Service Unavailable* [REQUIRED]
    - The Status List Provider is temporary unavailable.
  * - *504 Gateway Timeout* [OPTIONAL]
    - The Status List Provider cannot fulfill the request within the defined time interval.


















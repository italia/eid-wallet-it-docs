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


Digital Credential Lifecycle in a Batch
---------------------------------------

For Digital Credentials issued in a single batch, each Credential shares the same lifecycle state machine. All state transitions (Issued → Valid → Expired/Suspended/Revoked) occur for the entire batch.


Credential Lifecycle Management
-------------------------------

While :numref:`fig_DigitalCredential_States` shows the different states a Digital Credential may acquire during its lifecycle,
:numref:`fig_DigitalCredential_Lifecycle` shows the point of view of Wallet Instances and Credential Issuers in managing the Digital Credential lifecycle
and the effect on their local storage.

.. _fig_DigitalCredential_Lifecycle:
.. plantuml:: plantuml/credential-lifecycle.puml
    :width: 99%
    :alt: The figure illustrates the Digital Credential Lifecycle.
    :caption: `Digital Credential Lifecycle Management. <https://www.plantuml.com/plantuml/svg/ZLDTRnCn47pthnYUQAKMAj6db8z6YP0gWLG5K8KGGkxTNix2iODtdRJyUcmdENB82FRXPCixExExSzSiEaXSMVN4kCR6bl1oTlbyTlbj_kZqoZIlbL8bHpalX62MlQYxdXmqvcPfH5lC0hNanAIZ8sePud5FYEjM2xLda9wESswO8mN6--bdCBaM6iwBwKoZnNW7yGNnYIaWid5BQ0HQ6XPAHU2ZdFlk_5udPEDNg-WEmARNpf5zfdBHB5UfIQdYr-GOTzfQ4jmu5kqQkb9G02OBac1eG_WWMYBZdM71H_-T73eVSWfOV68-we4J62WSiDH9kIteHpGvRvl7upmssfesFrLAqqCwStaSrEQBwN3oc-S0D0vVBXukNfmXVI-_lZc5P8wJH-BJ0WDP9fmuVmg5us3nQuKzZUdKy9g9far3p7j5HMsbyZxoPSGqUYxb5jG5ulx_wW6Jr5mGZ55lhT_kXblZgtTMOjY7mZXsBDh1qRPuBoyVNUBvCtDhf2-sUygOngnR3jOQfuvNLc8OSFqs7B8XCR_rjnWDNpp2teT3Qj9R-SLsmwbOXNTMULKiylUvJx9DYQKqMjhqmVmiNLxLzZrGZVA9QmoZtVf0fOMQzFfUwviTPba7_fknvlx9d2m9OHreOtpa4KOL0TS94bVs5m00>`_

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

  1. Deleting the Digital Credential from their Wallet Instance: the Wallet Instance SHOULD prompt the User to be optionally notify the Credential Issuer about the User's intention to revoke the Digital Credential. When the User uses this functionality, the notification to be sent to the Credential Issuer MUST use the Notification Endpoint provided by the Issuer, as described in Section :ref:`credential-revocation:Status Update by Wallet Instance`.
  2. Using the Issuer's web portal:

    a. Users MAY access a secure area with at least the same Level of Assurance used during the issuance phase.
    b. The Issuer MUST allow Users to:

      - View all their Digital Credentials contained in the Issuer's database.
      - Verify data authenticity.
      - View and update validity status (revoke their Digital Credentials and, if it is supported by the Issuer, suspend them).

In addition, when Users detect incorrect data in an issued Digital Credential, the Wallet Instance SHOULD initiate a data correction request via the Notification Endpoint as specified in :ref:`notification-data-correction`. Upon confirmation of the discrepancy, the Issuer SHOULD follow the :ref:`credential-issuance-low-level:Re-Issuance Flow`.

.. note::
  If the User activates another Wallet Instance from the same Wallet Provider and using the same Wallet Solution and obtains a new PID, the previous PID MUST be revoked, and the previous Wallet Instance MUST transition to operational status.

In case of the death of the User, Issuers MUST ensure that Digital Credentials and Wallet Instances owned by the User are revoked.
The User's death triggers a change in the validity status of the User's identification attributes contained in the public registry (ANPR). The User's death MUST produce the PID revocation. Therefore, the Authentic Source of the PID (ANPR) MUST notify the PID Provider that the User's attributes are no longer valid due to the death of the User. The Authentic Source and the PID Provider MUST use the mechanisms provided in the Section :ref:`credential-revocation:Status Update by Authentic Sources`.

.. note::
  Future versions of this technical specification will define how the information to (Q)EAA Issuers are propagated, according to national regulation. Moreover, automated procedures for Credential revocation due to illegal activities will be defined in future specifications.

Status Update by Wallet Instance
""""""""""""""""""""""""""""""""

When the User deletes a Digital Credential from the Wallet Instance, the Wallet Instance by default SHALL NOT notify the Credential Issuer of this deletion event. Deleting a Digital Credential from the Wallet Instance only removes the local copy and does not change the validity status at the Issuer.

The Wallet Instance MAY inform the User, prior to deletion, that deletion is a local action and does not imply revocation at the Issuer, and MAY implement, under the User's explicit consent at deletion time, a notification feature to inform the Credential Issuer of the User's intention to revoke the Digital Credential.

If the User wants the Issuer to revoke a Digital Credential, the User SHOULD explicitly confirm this intention via the Wallet Instance's deletion prompt (when available), which SHALL then notify the Credential Issuer; alternatively, the User MAY use the Issuer's web portal or other Issuer-provided channels.

When the revoked Credential is the PID, the Credential Issuer MUST send a notification of this event to the User within 24 hours.
For any other Credential different from the PID, the Credential Issuer SHOULD send a notification of this event to the User. The notification to the User MAY be implemented in several ways, such as using a User's email address, telephone number, or any other verified and secure communication channel. The notification to the User MUST also include all the information about the Credential revocation status. The method used for the notification to the User is out of scope of the current technical implementation profile. When the revocation occurs, the Credential Issuer MUST update the status of the Digital Credential accordingly. When the Notification Response sent by the Credential Issuer is successfully received by the Wallet Instance, the Wallet Instance MUST delete the Digital Credential.

Status Update by Wallet Providers
"""""""""""""""""""""""""""""""""

The Wallet Provider that, for any reason, revokes a Wallet Instance MUST ensure that the updated status is reflected in the status list of the related the Wallet Unit Attestation. 
In addition to what already defined in :ref:`credential-revocation:Digital Credential Lifecycle`, the Credential Issuer MUST implement a monitoring mechanism of the current statuses of all the Wallet Unit Attestations related to the Wallet Instances to which the Credentials were issued.
Afterwards the revocation of the Wallet Unit Attestation, the Credential Issuer proceeds with the revocation of all the Credentials issued to the Wallet Instance.

Status Update by Authentic Sources
""""""""""""""""""""""""""""""""""

Authentic Sources manage attributes separately from Digital Credentials, which verify authenticity like physical documents. Losing a physical document doesn't mean losing the privileges it represents; it just means the User can't prove them. However, if a User loses privileges due to a serious infraction, the Authentic Source will revoke the related attributes. In such cases, when a User's attributes are updated, Authentic Sources MUST notify Credential Issuers to update the validity status of any Digital Credential containing those attributes.

Authentic Sources that use Signal Hub MUST deposit a Signal through the :ref:`signal-hub-endpoint:Signal Collection e-Service` in the following cases:

  - The value of one or more Attributes contained in the Authentic Source's database has changed; 
  - The validity status of the Attributes is updated (revocation or suspension).

In both cases, the Signal MUST have ``signalType`` set to ``UPDATE``.

Credential Issuers MUST check the PDND Signal Hub :ref:`signal-hub-endpoint:Signal Distribution e-Service` periodically for new Signals. For the Signal processing flow, please refer to the Section :ref:`signal-hub-endpoint:Signals Processing`. The Credential Issuer is able to identify the nature of the ``UPDATE`` Signal by quering the Authentic Source `get attribute` API and inspecting the response payload, as described in Section :ref:`authentic-source-endpoint:Get Attribute Claims`.

The following diagram illustrates the high-level status update process for Authentic Sources.

.. only:: format_html

  .. figure:: ./images/svg/status-update-as.svg
    :alt: Status update process for Authentic Sources
    :width: 100%

    Status update process of Authentic Sources

.. only:: format_latex

  .. figure:: ./images/pdf/status-update-as.pdf
    :alt: Status update process process Authentic Sources
    :width: 100%

The process starts with data or data validity changes that occur in the Authentic Source data. Changes can also be initiated by third-party entities other than the Authentic Source, such as when law enforcement agencies report illegal activities.

Once the data changes, the Authentic Source notifies the Credential Issuers who received the original data using the Signal Hub. The Authentic Source deposits a Signal in the Signal Collection e-Service. :ref:`signal-hub-endpoint:Signal Collection e-Service`.

The Credential Issuer periodically queries the Signal Hub :ref:`signal-hub-endpoint:Signal Distribution e-Service` for new Signals. When a new Signal is found, the Credential Issuer retrieves it and processes it as described in :ref:`signal-hub-endpoint:Signals Processing`. Then, the Credential Issuer updates the Credential Status according to the validity mechanism's defined mode. The Credential Issuer MAY notify the User through a registered out-of-band communication channel.

The Wallet instance, following periodic checks of the validity status of the stored Digital Credentials, receives the updated status. When the Credential Status is changed to INVALID, the Credential Issuer MUST inform the User about this change. In case the Credential status is modified to UPDATE (resp. 0x03) or ATTRIBUTE_UPDATE (resp. 0x04), the Wallet Instance SHOULD proceed to the re-issuance of the Digital Credential, as described in :ref:`credential-issuance-low-level:Re-Issuance Flow`.


Batch Credential Lifecycle Management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When multiple Digital Credentials are issued together in a single batch, their lifecycle is shared:

  * **Grouped updates**: regardless of the actor that triggers a batch status update (e.g. the Wallet Instance via Notification Endpoint with ``event=credential_deleted``, Wallet Provider via updating Wallet Unit Attestation status list) the status updating is handled by changing a single status indicator (for example, flipping its status-list bit to ``INVALID`` or ``SUSPENDED``) related to the entire batch. By default, a Wallet Instance SHALL NOT trigger batch status updates when the User deletes local Credentials. Upon deletion, the Wallet Instance MAY, under the User's explicit consent, notify the Credential Issuer of the User's intention to revoke the affected Credential(s).

.. note::
  As the Wallet UI typically surfaces a batch as one Credential (e.g., 3 uses remaining), a User-driven deletion in the Wallet removes the entire batch locally. By default it does not request revocation at the Issuer. The Wallet MAY offer the User an optional prompt to request revocation at the Issuer as part of the deletion flow.



Validity Verification Mechanisms
--------------------------------

For the verification of the validity status of a long-lived Digital Credential the Token Status List (`TOKEN-STATUS-LIST`_) MUST be supported for both the remote and proximity scenario. The following table sums up the required revocation mechanisms for verifying the status of long-lived Digital Credentials.

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
      - [REQUIRED] Token Status List.
    - `TOKEN-STATUS-LIST`_.
  * - Proximity
    - [REQUIRED] Token Status List.
    - `TOKEN-STATUS-LIST`_.


Token Status Lists
^^^^^^^^^^^^^^^^^^

This section defines a Status List data structure, which is used to convey information regarding the individual statuses of multiple Digital Credentials. Digital Credentials may be of any format, such as SD-JWTs or ISO/IEC 18013-5 mdocs. A Status List describes the status of the Digital Credentials by encoding their status validity in a bit array. Each Digital Credential is allocated an index during issuance; this index represents its position within the bit array. The value of the bit(s) at this index corresponds to the Digital Credentials' status. A Status List is provided within a cryptographically signed Status List Token in JWT format. For details, see `TOKEN-STATUS-LIST`_.

In this specification, the roles of Credential Issuer and Status Issuer (i.e., the entity that issues the Status List Token about the status information of the Digital Credential) coincide, whereas the Status Provider (i.e., the entity that provides the Status List Token on a public endpoint) MAY be the Credential Issuer itself or another entity.

The Issuer of the Digital Credentials MUST

  - define a number of bits, k, (either 1, 2, 4, 8) that represents the amount of bits used to describe the status of each Digital Credential within this Status List. The Credential Issuer MUST configure the number of bits. Each Credential will therefore have 2^k (where k is the number of bits chosen) possible states.
  - create a byte array of size = (amount of Digital Credentials) * k / 8 or greater. Depending on k, each byte in the array corresponds to 8/k statuses (8 if k=1, 4 if k=2, 2 if k=1, or 1 if k=8). Each time a Digital Credential is issued the Credential Issuer assigns it to a position in the array.
  - set the status values for all issued Digital Credentials within the byte array. The status of each Digital Credential is identified using an index that maps to one or more specific bits within the byte array. The index starts counting at 0 and ends with (amount of Digital Credential) - 1 (being the last valid entry). The bits within an array are counted from the least significant bit ("0") to the most significant bit ("7"). All bits of the byte array at a particular index are set to a status value.
  - compress the byte array using DEFLATE [:rfc:`1951`] with the ZLIB [:rfc:`1950`] data format. Implementations are RECOMMENDED to use the highest compression level available.
  - make available to Relying Parties, and Wallet Instances, an endpoint to request Status Lists.

The Issuer of a Digital Credential MUST use the following values for possible Statuses of the issued Digital Credentials:

  - 0x00 - ``VALID`` - The Digital Credential is valid.
  - 0x01 - ``INVALID`` - The Digital Credential is revoked.
  - 0x02 - ``SUSPENDED`` - The Digital Credential is temporarily invalid, hanging. This state is usually temporary.
  - 0x03 - ``UPDATE`` - The Digital Credential metadata parameters have changed.
  - 0x0B - ``ATTRIBUTE_UPDATE`` - The Digital Credential attributes have changed.

For example, if five states for a certain Digital Credential are possible, then k=4. If the Credential Issuer creates an array to store the statuses of 6 Digital Credentials, whose validity statuses are 0, 0, 0, 3, 1, 2, respectively; it will:

  - create the bit array ``[0, 0, 0, 0, 0, 0, 0, 0; 0, 0, 1, 1, 0, 0, 0, 0; 0, 0, 1, 0, 0, 0, 0, 1]`` which in exadecimal notation generates the byte array ``[0x00, 0x30, 0x21]``.
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


.. _table_status_list_endpoint_parameters:
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
    - REQUIRED. The subject claim MUST specify the URI of the Status List Token. The value MUST be equal to that of the ``uri`` claim contained in the ``status_list`` claim of the Digital Credential.
    - [:rfc:`7519`]
  * - **iat**
    - REQUIRED. The issued at claim MUST specify the time at which the Status List Token was issued.
    - [:rfc:`7519`]
  * - **exp**
    - RECOMMENDED. The expiration time claim, if present, MUST specify the time at which the Status List Token is considered expired by the Credential Issuer.
    - [:rfc:`7519`]
  * - **ttl**
    - RECOMMENDED. The time to live claim, if present, MUST specify the maximum amount of time, in seconds, that the Status List Token can be cached by a consumer before a fresh copy SHOULD be retrieved. The value of the claim MUST be a positive number encoded in JSON as a number. This amount of time SHOULD NOT exceed the expiration time defined in **exp** claim.
    - `TOKEN-STATUS-LIST`_
  * - **status_list**
    - REQUIRED. JSON Object that contains a Status List.
    - `TOKEN-STATUS-LIST`_

.. note::
  It is RECOMMENDED that the Credential Issuer sets the ``exp`` claim so that the Status List Token is short-lived. Typically, this involves the ``exp`` claim not to exeed the ``iat`` claim by more than 24 hours.

A JSON-encoded Status List has the following structure:

.. _table_status_list_structure:
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

.. code-block:: json

  {
    "alg": "ES256",
    "kid": "$KID",
    "typ": "statuslist+jwt",
    "x5c": [
      "MIIDqjCCApKgAwIBAgIESLNEvDA ...",
      "MIICwzCCAasCCQCKVy9eKjvi+jA ...",
      "MIIDTDCCAjSgAwIBAgIJAPlnQYH..."
    ]
  }

.. code-block:: json

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

.. _table_status_list_parameters:
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

HTTP Status List Request
.........................

To obtain the Status List Token, the Relying Party MUST send an HTTP GET request to the ``status.status_list.uri`` value provided within the Digital Credential.

The Relying Party SHOULD send the ``application/statuslist+jwt`` Accept-Header to indicate that the requested response type for Status List Token is the JWT format.

The following is a non-normative example of a request for a Status List Token:

.. code-block:: http

  GET /statuslists HTTP/1.1
  Host: example-issuer.com
  Accept: application/statuslist+jwt


HTTP Status List Response
..........................

The Status List Endpoint responds with a Status List Token and MUST use an HTTP status code in the 2xx range. In the successful response, the Status Provider MUST use content-type ``application/statuslist+jwt`` for Status List Token in JWT format.

The HTTP response SHOULD use gzip Content-Encoding as defined in [:rfc:`9110`].

If caching-related HTTP headers are present in the HTTP response, Relying Parties SHOULD prioritize the ``exp`` and ``ttl`` claims within the Status List Token over the HTTP headers for determining caching behavior.

The following is a non-normative example of a response for a Status List Token with type ``application/statuslist+jwt``:

.. code-block:: http

  HTTP/1.1 200 OK
  Content-Type: application/statuslist+jwt

  eyJhbGciOiJFUzI1NiIsImtpZCI6IjEyIiwidHlwIjoic3RhdHVzbGlzdCtqd3QifQ.eyJleHAiOjIyOTE3MjAxNzAsImlhdCI6MTY4NjkyMDE3MCwiaXNzIjoiaHR0cHM6Ly9leGFtcGxlLmNvbSIsInN0YXR1c19saXN0Ijp7ImJpdHMiOjEsImxzdCI6ImVOcmJ1UmdBQWhjQlhRIn0sInN1YiI6Imh0dHBzOi8vZXhhbXBsZS5jb20vc3RhdHVzbGlzdHMvMSIsInR0bCI6NDMyMDB9.SSdg3AnTHsyRtCHziLy-QnXg-YRldMEXkdEgDXgE_ZvIvjM0eULQlzEbLBLfCeGhlqKJSReC-m85K79CTjJDzg

Upon receiving a Digital Credential, a Relying Party MUST first perform the validation of the Digital Credential itself (e.g., checking for expected attributes, valid signature and expiration time). If this validation is not successful, the Digital Credential MUST be rejected. If the validation was successful, the Relying Party MUST perform the following validation steps to evaluate the status of the Digital Credential:
 
- Check for the existence of a ``status`` claim, check for the existence of a ``status_list`` claim within the ``status`` claim and validate that the content of ``status_list`` adheres to the rules defined in Section :ref:`credential-revocation:Handling Credential Status with Status List Token`.
- Resolve the Status List Token from the provided URI.
- Validate the Status List Token:

  - Validate the Status List Token's signature by following the rules defined in section 7.2 of [:rfc:`7519`]. This step requires the resolution of a public key as described in :ref:`trust-infrastructure:The Infrastructure of Trust`.

  - Check for the existence of the required claims as defined in Section :ref:`credential-revocation:Status List Token`.

- All existing claims in the Status List Token MUST be checked according to :ref:`credential-revocation:Status List Token`.

  - The subject claim of the Status List Token MUST be equal to the ``uri`` claim in the ``status_list`` object of the Digital Credental.
  - If the Relying Party has custom policies regarding the freshness of the Status List Token, it SHOULD check the ``iat`` claim.
  - If the expiration time is defined, it MUST be checked if the Status List Token is expired.
  - If the Relying Party is using a system for caching the Status List Token, it SHOULD check the ``ttl`` claim of the Status List Token and retrieve a fresh copy if (time status was resolved + ``ttl`` < current time).

- Decompress the Status List with a decompressor that is compatible with DEFLATE [:rfc:`1951`] and ZLIB [:rfc:`1950`].
- Retrieve the status value of the index specified in the Digital Credential as described in :ref:`credential-revocation:Checking Credentials Statuses`. Fail if the provided index is out of bounds of the Status List.
- Check the status value as described in :ref:`credential-revocation:Checking Credentials Statuses`.

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


















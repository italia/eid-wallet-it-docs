.. include:: ../common/common_definitions.rst
.. Included via infrastructure-trust.rst at title level '-' (level 1).

PKI Architecture
----------------

The Trust Artifacts of both Trust Frameworks are signed with keys whose public part is certified by a Certification Authority. This section provides the architectural view of these Certification Authorities. It defines which of them are operated within IT-Wallet, which certificates each one issues, and which Trust Anchor is derived from each one and through which channel that Trust Anchor is distributed.

The content of the certificates is not defined here. The common requirements are defined in :ref:`infrastructure-trust:X.509 Certificate Profile` and the specific requirements of each certificate are defined together with the artifact that uses it. The issuance of the certificates is part of the onboarding (see :ref:`onboarding-procedure:The Onboarding Processes`). The use of the Trust Anchors at runtime is defined in :ref:`trust-evaluation:EUDIW Trust Anchor Validation` for the EUDIW Trust Framework and in :ref:`trust-evaluation:Signing Trust Anchor Distribution` and :ref:`trust-evaluation:Authentication Trust Anchor Distribution` for the National Trust Framework.

Certification Hierarchies
^^^^^^^^^^^^^^^^^^^^^^^^^

Within IT-Wallet a single national Root Certification Authority is operated. It issues the certificates of the subordinate Certification Authorities and it is not used for any other purpose. Each subordinate Certification Authority serves one service, and its certificate is the Trust Anchor published for that service.

.. _fig_pki_architecture:
.. plantuml:: plantuml/pki-architecture.puml
    :width: 99%
    :align: center
    :alt: The figure illustrates the certification hierarchies of the IT-Wallet ecosystem and the publication channel of the Trust Anchor derived from each Certification Authority.
    :caption: `PKI Architecture of the IT-Wallet Ecosystem. <https://www.plantuml.com/plantuml/svg/dLVTRnev47z7udyOjG-y772DxgIxFbJTyD5oILEo474FaIgpQy3AOaUsbuYh-h_VZEs5tOLDei03iMVcDn_-pTZvR2pJDjzcC9bt5opBk8KkJAyc4Eba8onFRAvvkzM10TTMh4J2h50IDe9hHXhS09CfFERBh90b6oObpq2jm6uuf5oB7KzXhdDZ8PB9HcdJQxVQBVCWv2FJR0jcmrBr9EGQLYmpl2nA-OhbcHqhQM_ObiDNdksuHLyDIZFn7uSF5sLffBLw6gXCQNZ_X_kKfHfpP7ATSVZPRW5SikHXhLKkKs-ne2euWTAOIWtcLndf4KtPkW7d_JYYxmdIN-v3sovwkyT0bYfB7NQxbV6L1Qj0Y_N6GYeeMYmoYGftxsvStLb6v_OEc86RQ4v14EWnkwDQh9I5GNGl-tsrMcL2yjz0vTQ8bBiJsx5CfFui7vdTzFiEDFx-VNw2EPqCOQhL3aqrpCHQzcSSFNZm9k61ITm4x47q0vLdDV30nqRyP-HdNIocvA3c94eIRan0P7wHbCo9njvHD-RP7ZbwBwVOCmNpoqcMVSNJQD1q056EPPQsQ1ZlEw03WU-1LLMIimb5T_ElzPh5qtXmKYc3QyAk9qQdVIWV9KhMbIJYUX8nNmjZiVbFd9oLd8qx7drfAiqeYaw0Xoh9jrWC9y10pnS3BKFF71hZDaSchyHX-CoutedacB8plPtFfhvbI_4SBNq8jnJNgubsM--I_BBR1E0xvHc5yzroTrbFTdGtd2n2ecCSH_n9wGUdZygZkvCKAyIzbzTuTaG11u1vZv1yH7A7S4tj-NntlWpXs--PihmY2agxYb7O1lf6WvVZEDEQTPZuLJ3DpV6YzMaBVEFR9PsynPC-M14A4IH24YIeTN51c7moZ6Q13DS_vjTrAXowgO4DuNwek1zpJDyFc_9DVIzTu7iOABaIwzoh1C_ZaIE5L9RkB6lLbfO0Snmh9Ro0SCNtE38rzuy5iy7q4EMVnPKt4jADetFkJ8yWzyuOdS6_lJz__zjRLIOQpUD2HnYJeuSbMbNVBjwEHh3IwAb7Quw6BWi8fQJB3hhTJyURgRn3JAwiFQFAMtuqrvJYcf8ZGNd3pR1sApY5NkzJqNhEQzWWztu651hK5aKSXPAFgRPxm7BNn44pzfeOJzXpaT4a2slYMCWgxE3PmqT0PbOlgZ9t-drdH2rUjPc5wwYkJE_C4fc8wfwj97W3hJflebNdZRJgr6ZLET3AF-JMj3osoKpXAmjnyMtwqSCQ5sd9TN55cto9JqOXQQlw3g_IUCXy-XwJB1kqAqw4gPQkV2fOFaJ6m7tubCXd_CL_6EZF_m40>`_

The following table lists the Certification Authorities, the certificates that are issued by each of them, and the channel through which the derived Trust Anchor is distributed. The Lists of Trusted Entities and the Trusted Lists named in the table are defined in :ref:`infrastructure-trust:Trusted List, Lists of Trusted Lists, and Lists of Trusted Entities`.

.. _table_pki_certification_authorities:
.. list-table:: Certification Authorities and Derived Trust Anchors
    :class: longtable
    :widths: 24 38 38
    :header-rows: 1

    * - **Certification Authority**
      - **Issued Certificates**
      - **Trust Anchor Distribution**

    * - PID Provider Sign/Seal CA
      - :ref:`infrastructure-trust:PID Provider Sign/Seal Certificate`
      - PID Providers LoTE.

    * - Wallet Provider Sign/Seal CA
      - :ref:`infrastructure-trust:Wallet Provider Sign/Seal Certificate`
      - Wallet Providers LoTE.

    * - Access CA
      - Access certificates following the :ref:`infrastructure-trust:Wallet-Relying Party Access Certificate (WRPAC) Profile`, issued to the Wallet-Relying Parties and to the PID Providers.
      - Providers of WRPAC LoTE. The same Trust Anchor is also published in the PID Providers LoTE, because the trust anchors of the Access Certification Authorities for PID Providers are notified within the PID Provider notification, separately from the ones for the Wallet-Relying Parties (see [`EIDAS-ARF`_], Topic 31).

    * - National Authentication CA
      - Relying Party authentication certificates used in the Proximity Flow. They follow the same profile as the Wallet-Relying Party Access Certificate.
      - Entity Configuration of the Federation Trust Anchor, as Authentication Trust Anchor (see :ref:`trust-evaluation:Authentication Trust Anchor Distribution`).

    * - WRPRC Sign/Seal CA
      - The signing certificate of the Provider of WRPRC (see :ref:`infrastructure-trust:Wallet-Relying Party Registration Certificate (WRPRC) Profile`).
      - Providers of WRPRC LoTE.

    * - Registrar Sign/Seal CA
      - :ref:`infrastructure-trust:Registrar Sign/Seal Certificate Profile`
      - Registrar LoTE.

    * - National EAA Sign/Seal CA
      - :ref:`infrastructure-trust:(Q)EAA Provider Sign/Seal Certificate`, for the Digital Credentials anchored to the National Trust Framework.
      - Entity Configuration of the Federation Trust Anchor, as Signing Trust Anchor (see :ref:`trust-evaluation:Signing Trust Anchor Distribution`). For an EAA issued in the EUDIW Trust Framework the Trust Anchor is referenced in the Attestation Rulebook, as described in :ref:`infrastructure-trust:Trust Anchor Certificate Profile`.

    * - Qualified CA of the QEAA Provider
      - :ref:`infrastructure-trust:(Q)EAA Provider Sign/Seal Certificate`, for the QEAA.
      - Member State Trusted List, published in accordance with Article 22 of [`EIDAS`_].

    * - PuB-EAA Provider Sign/Seal CA
      - :ref:`infrastructure-trust:PuB-EAA Provider Sign/Seal Certificate`, the qualified certificate supporting the qualified electronic seal of the public sector body (Article 45f(1)(b) of [`EIDAS`_]).
      - PuB-EAA Providers LoTE.

The Qualified CA of the QEAA Provider and the PuB-EAA Provider Sign/Seal CA are not subordinate to the national Root Certification Authority. Both belong to the perimeter of a Qualified Trust Service Provider and follow its own supervision and publication regime. 
The sign/seal certificate of a PuB-EAA Provide is a qualified electronic seal issued by a Qualified Trust Service Provider (Article 45f of [`EIDAS`_]).

.. note::
  The Certification Authority that issues the Wallet-Relying Party Access Certificates and the Certification Authority that issues the Relying Party authentication certificates of the National Trust Framework use the same certificate profile.

.. note::
  The Federation Entity Keys are not certified by the Certification Authorities described in this section. The binding between a Federation Entity and its keys is provided by the Entity Configuration and by the Subordinate Statement issued by its superior, which are validated through the Federation Trust Chain and not with a certification path (see :ref:`infrastructure-trust:National Trust Artifacts`). The Entity Configuration of the Federation Trust Anchor is used as a distribution channel for the Trust Anchors of the X.509 hierarchies.

Design Principles
^^^^^^^^^^^^^^^^^

The hierarchies described above follow the principles listed below.

- **One Sign/Seal Certification Authority per notified role.** Each role that signs or seals an artifact has a distinct Sign/Seal Certification Authority.
- **A single Access Certification Authority.** Within IT-Wallet the access certificates are issued by a single Certification Authority, both to the Wallet-Relying Parties and to the PID Providers, as they follow the same profile and certificate policy. The Relying Party authentication certificates of the National Trust Framework are issued by a distinct Certification Authority.
- **No Trust Anchor without a consumer.** Within IT-Wallet a Trust Anchor is published in a distribution channel only when a trust evaluation procedure defined in this specification obtains it from that channel.
- **The Root Certification Authority is outside the validation path.** The Trust Anchor certificate is the trust termination point of the path validation (see :ref:`infrastructure-trust:Trust Anchor Certificate Profile`), therefore the Root Certification Authority is never evaluated at runtime and its certificate is not published in any List. It provides a common governance to the subordinate Certification Authorities and no trust relationship by itself. A compromise of the Root Certification Authority is not detected by the ordinary path validation, and within IT-Wallet it is managed by re-issuing and re-notifying the affected Trust Anchors.
- **Only end entities below a published Trust Anchor.** Within IT-Wallet the published Trust Anchor is the subordinate Certification Authority of the service, and no further Certification Authority layer is issued below it. This is consistent with the ``pathLenConstraint`` recommendation of :ref:`infrastructure-trust:Trust Anchor Certificate Profile`.
- **Separation of the keys by purpose.** A Trust Anchor published for one purpose is not used to certify the artifacts of another purpose. A verifying entity has to be able to distinguish which Trust Anchors are usable for which category of Attestation, as required by [`EIDAS-ARF`_].

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
    :caption: `PKI Architecture of the IT-Wallet Ecosystem. <https://www.plantuml.com/plantuml/svg/dLTDR-Cs4BqRy7yOx1vygUqsQ85s3ujL7BkR9iqwaWFt4611IvHDH2O3adBW5llVTuQaR4d-o3R98H0vy-RDyCsG-MGiqxPS5t0zwyzPKN0BVPZUN4EaqvMmFBMbvjrE3qPSMv6Bb5cX9Am4rumik04cCtWk5qMrbwwObBm0bODTSSYu5XkUmKoNna8aqvNIPj3jT3lcISXdfjaQp8fbwaN89UIiCBo-bV6SbOMTA6dls9h3PrvikCLO9umIyI-7Noxgkv7MwcMa2gNX_Q_kfxwhCKScbmM7_xeTW4kMFYsrAcNcFUPK1RUXDARIWlbMHtf6LxOyWVD-4j7l0TBlxeUM7NkxHI8BLMGEkzifU6x1Aj1YkRAG2MABHQQjAjoxErTtLj2vlGDcu2wQ4Ga2tMUtDukLiZ2A7kLmgFAy49B_1AgqHcJSdTY65IBpP_dCx6euTA3nbo-p0ypfzHLCjTgWguP4BEKmuHZ1Wv_Qt2c9cu0zYhwYSN8EF4fJRan0diVJQ5G9h6xM18nQW47W9mcVsJ_AUJvjCoul--CeEbEICmR7o_9msKx2vNwa3fvzF-R5bZffYeqj6cp9-9GceX8XfArwsCFNeRR0cYRfKRxHm-pp8U5uT509Wz-4NOVPdMXL7VnsteqaudOICLyAOt4U7GGvkdEKTpp-yrHfwBpQm5SgBTTO3BU1H8yN0pr36-zwzRx4vih5RXucN6z4ka_PkTxFagcV8ZK-UqzFuVv_wUY-JMJyS7Kz3oGcEBtuYz9FpXebDtuu2D_eiaTvYtMbut40o6cCmY2vEOHRQhxplVSwnAlDzGCi3ffdvnka5OrUvt6aRTemyG_1d1Rkgzw7yloRhnTqxXRFUUT5AAID22MGejN51M5od8H9aCBjrzbjMmexfPzGGxXE6k4d7DFtWw1-iJzAHtmB8oLpiIozIOWy6JjHI6NfYhDMhUaJO8OjNyCB23TyYsyBpVtRmgmmFKJvQtxZdOHqe-9OE3CWoArpnc3mp-2td__mNerfGm-NoaOOKsA41NerdphUZyQZqXXfGDyS7LqM44f9ToFq-n_t5rbh9MgkaBOR5YJKXe4NNNt9JzQMKTmoSZgfBxWHrEq4NZ0OVAowCn1hBSsdOO4eUcQL1N6ig5L6dcR5PRyQ-rMa4zOSCPf3uPjK698AAwWE-02etUOrKrVNSEYSQ0WqVP9mcRIDwU5QanirWzSpRRn1UBqt2Q_tHk7rMiBhxOJdNuPB-jmtKgBmsOQu-DZzu66DOreBNLsmfbpW6rH8Mce-x9j2ls8-VOz9dYUi6q64QPQkVYfOFaH6ufu-9V89_-9_8DtETm00>`_

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

    * - PID Provider Access CA
      - :ref:`infrastructure-trust:Wallet-Relying Party Access Certificate (WRPAC) Profile`, issued to the PID Providers.
      - PID Providers LoTE. It is distinct from the Trust Anchor of the Providers of WRPAC, because a PID Provider is not a Wallet-Relying Party in the sense of [`CIR2025/848`_].

    * - Wallet Provider Sign/Seal CA
      - :ref:`infrastructure-trust:Wallet Provider Sign/Seal Certificate`
      - Wallet Providers LoTE.

    * - PuB-EAA Provider Sign/Seal CA
      - :ref:`infrastructure-trust:PuB-EAA Provider Sign/Seal Certificate`
      - PuB-EAA Providers LoTE.

    * - WRPAC CA
      - :ref:`infrastructure-trust:Wallet-Relying Party Access Certificate (WRPAC) Profile`, issued to the Wallet-Relying Parties.
      - Providers of WRPAC LoTE.

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

The Qualified CA is not subordinate to the national Root Certification Authority. When the QEAA Provider is a Qualified Trust Service Provider, that Certification Authority belongs to the perimeter of the Qualified Trust Service Provider and follows its own supervision and publication regime.

.. note::
  The Certification Authority that issues the Wallet-Relying Party Access Certificates and the Certification Authority that issues the Relying Party authentication certificates of the National Trust Framework use the same certificate profile.

.. note::
  The Federation Entity Keys are not certified by the Certification Authorities described in this section. The binding between a Federation Entity and its keys is provided by the Entity Configuration and by the Subordinate Statement issued by its superior, which are validated through the Federation Trust Chain and not with a certification path (see :ref:`infrastructure-trust:National Trust Artifacts`). The Entity Configuration of the Federation Trust Anchor is used as a distribution channel for the Trust Anchors of the X.509 hierarchies.

Design Principles
^^^^^^^^^^^^^^^^^

The hierarchies described above follow the principles listed below.

- **One Certification Authority for each published Trust Anchor.** Within IT-Wallet a Trust Anchor is not shared between two services. Two services that need two independent Trust Anchors are served by two Certification Authorities, also when they use the same certificate profile and the same certificate policy.
- **No Trust Anchor without a consumer.** Within IT-Wallet a Trust Anchor is published in a distribution channel only when a trust evaluation procedure defined in this specification obtains it from that channel.
- **The Root Certification Authority is outside the validation path.** The Trust Anchor certificate is the trust termination point of the path validation (see :ref:`infrastructure-trust:Trust Anchor Certificate Profile`), therefore the Root Certification Authority is never evaluated at runtime and its certificate is not published in any List. It provides a common governance to the subordinate Certification Authorities and no trust relationship by itself. A compromise of the Root Certification Authority is not detected by the ordinary path validation, and within IT-Wallet it is managed by re-issuing and re-notifying the affected Trust Anchors.
- **Only end entities below a published Trust Anchor.** Within IT-Wallet the published Trust Anchor is the subordinate Certification Authority of the service, and no further Certification Authority layer is issued below it. This is consistent with the ``pathLenConstraint`` recommendation of :ref:`infrastructure-trust:Trust Anchor Certificate Profile`.
- **Separation of the keys by purpose.** A Trust Anchor published for one purpose is not used to certify the artifacts of another purpose. A verifying entity has to be able to distinguish which Trust Anchors are usable for which category of Attestation, as required by [`EIDAS-ARF`_].

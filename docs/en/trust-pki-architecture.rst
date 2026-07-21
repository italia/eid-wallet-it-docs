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
    :caption: `PKI Architecture of the IT-Wallet Ecosystem. <https://www.plantuml.com/plantuml/svg/dLTDRziu4BqRy7yOj0TVrlOss0LsUoYg-AFr9fiwiWFl8K11IxHDH2O3adBW5ltldI4fMPBjf9la48YSUVDc-6R8V3IMQPjlCvZCkmkMPTn25wPN4uXqiX6M9pRNlDtgm81hArOYOLOe2Hl1DICBRe3951xpPLRi9Hic9Sz0hS1kEAHSYnrFOQvpOo6IoKPfqsktsYtp8EGZqsmBPiDIzIJa6bOiCxowbV8LopCxLjBUi2s7pppRSOknpXZDn3SExowgkv7MwccWCgNXxH_kfxghCKScrnc7x-qMm2LB7jPQvJBr7WkgWjjG6bDfmFoe8ZsYArkVmNaxZkZt2EalzqFBZhtT8v6bobA7tMvbV6N1Aj1YlR6G2cABHQQj8joR6rTtbj6vlG5cu2QQ4ma2FMHtC8kLiZ28xcM_hrQhJ4Z-6wZS6f5oTs8xbedKd-KZivj-tu76NxxCZp2dao5CjTgXguQPMCl-Z6C43tvkirGIDm5x47r5ura3FEZnBFup-oT3BAPDzlbbTnH5psJmZC7fBEuk6p6Y9E7613pcFvAABxM9JwGRysoFFN0lfzYJHMTLYrZD9Pv6WtC77ELuZD8M3UbZ1tGWy3smkaboCfleRlwvUIRnD1uSrSdWDs4t4oCrbRMZHCcxbaJSJ2BcQs4i3fUZ82TtJlAEHv_EbOPEimayL4c-nMAu3IHwkXZe6NgoRBpR73jb9ShXDkDw9v93oixrTZwR-f5GuNFmz1Hk_vVARfj4HdV3oIAG6ECeuazAFpXh5EJexYXyJLJtyXhhIiVZ093J28L10dG8rzIQptVcon0ljjuli3XghT8tI2iQlCpZHDiqOU9VWZalt1UzZ-NvBzykwTmjddFfHIYaZGWbaA3LnGLXyiamcWKfN7-TNpUbK2hzZ1h2tL0BF-QOlXy4rLlwNZhYUnWekHBht9k4oEEH4uLKbkuhQzMMFW7csF8Ll81mnVSupZJt3mMpmVGGvP_5bNSIqesAK-5CZo3tpXc3mN-zFt__stlLfWtDoi9669DZX2LwrTyjte_6ez8OgKVV71rT5X1AIHSTTBiV3hTITOMKNBCWMTOClCIgItwEDepYXf5JHNN13PnsAx20Nkz3qOkEHbWWFfv6OK642Xw5aUVKM2snt4mlBMDlYNp2ccD6OoTya-X2Lc45nG3l0QLQlrMgOkhtdHFrVDrd5kwEfZ4zEYlg8krx-TB6AtJMUPNEEg_KMQUXiqwfC_-gMzFdeMzc2fzSY8iFrVSUrZYcbT35VMho9RuVXQIb-gEyhkiXy-bxJF8yOrqB8aozTDLJmV8XCXBtz2cHZ_WN_tjejtu2>`_

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

    * - PuB-EAA Provider Sign/Seal CA
      - :ref:`infrastructure-trust:PuB-EAA Provider Sign/Seal Certificate`
      - PuB-EAA Providers LoTE.

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

The Qualified CA is not subordinate to the national Root Certification Authority. When the QEAA Provider is a Qualified Trust Service Provider, that Certification Authority belongs to the perimeter of the Qualified Trust Service Provider and follows its own supervision and publication regime.

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

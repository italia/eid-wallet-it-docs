.. include:: ../common/common_definitions.rst
.. include:: ../common/symbols.rst
.. Included via index.rst at title level '=' (document title).

Infrastructure of Trust
=======================

This chapter specifies Trust Artifacts, certificate profiles, and their lifecycle.
The trust decision that uses those artifacts is specified in :ref:`trust-evaluation:Trust Evaluation Process`.
Registration and publication of entities are specified in :ref:`onboarding-system:Onboarding System and Lifecycle Management`.

The IT-Wallet ecosystem operates within a federated trust infrastructure where participating entities establish cryptographic trust relationships and maintain compliance with common security standards.
This infrastructure provides the foundation for secure Digital Credential operations across the ecosystem participants.

Two trust frameworks coexist in IT-Wallet.
The Trust Framework of each interaction is selected as specified in :ref:`trust-evaluation:Trust Framework Selection`.

  - The **EUDIW Trust Framework** is defined by the eIDAS2 Regulation (`EU_2024_1183`_), its Implementing Regulations and the ARF (`EIDAS-ARF`_).
    A Wallet Unit that implements only the EUDIW procedures MUST be able to request, present and verify a PID, a (Q)EAA or a PuB-EAA of another Member State.
    That Wallet Unit MUST be able to authenticate a Wallet-Relying Party of another Member State.
    PID Providers, QEAA Providers and PuB-EAA Providers MUST support the EUDIW Trust Framework.
  - The **National Trust Framework** is a national overlay based on OpenID Federation (`OID-FED`_) combined with an X.509 PKI for Digital Credentials anchored to that framework.
    It is **out of the ARF**.
    It provides registration, onboarding and discovery for entities that operate within the national boundary.
    Discovery through the National Trust Framework MAY include entities anchored to the EUDIW Trust Framework.
    That discovery doesn't replace EUDIW registration, notification or the EUDIW trust path.

This section provides first an overview of the entities and processes involved in the trust infrastructure (:ref:`infrastructure-trust:Overview`).
Then, it defines the general :ref:`infrastructure-trust:X.509 Certificate Profile` and the :ref:`infrastructure-trust:Common Trust Artifacts` shared by both frameworks, followed by the framework-specific artifacts (:ref:`infrastructure-trust:EUDIW Trust Artifacts` and :ref:`infrastructure-trust:National Trust Artifacts`).
Finally, it describes the related lifecycle (:ref:`infrastructure-trust:Trust Management and Lifecycle`).

Overview
--------

To perform a trust evaluation, entities first onboard in the ecosystem (see :ref:`onboarding-system:Onboarding System and Lifecycle Management`).
A Non-Qualified EAA Provider and a Relying Party declare the Trust Framework of each role there, as specified in :ref:`onboarding-system:Registration Profiles`.

Onboarding and, where applicable, European notification release or update the trust artifacts (see :ref:`infrastructure-trust:Common Trust Artifacts`, :ref:`infrastructure-trust:EUDIW Trust Artifacts` and :ref:`infrastructure-trust:National Trust Artifacts`).
Trust evaluation then uses those artifacts (see :ref:`trust-evaluation:Trust Evaluation Process`).


.. include:: trust-pki-architecture.rst
.. include:: x509-certificate-profile.rst
.. include:: trust-artifact-common.rst
.. include:: trust-artifact-eudiw.rst
.. include:: trust-artifact-oidfed.rst
.. include:: trust-management.rst



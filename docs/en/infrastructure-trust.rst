.. include:: ../common/common_definitions.rst
.. include:: ../common/symbols.rst

Infrastructure of Trust
=======================

The IT-Wallet ecosystem operates within a federated trust infrastructure where participating entities establish cryptographic trust relationships and maintain compliance with common security standards. This infrastructure provides the foundation for secure Digital Credential operations across the ecosystem participants.

Two trust frameworks coexist in IT-Wallet.

  - The **EUDIW Trust Framework** is defined by the eIDAS2 Regulation (`EU_2024_1183`_), its Implementing Regulations and the ARF (`EIDAS-ARF`_). It is mandatory and authoritative for the notified entities and for cross-border interoperability.
  - The **National Trust Framework** is based on OpenID Federation (`OID-FED`_) combined with an X.509 PKI dedicated to the signature of Digital Credentials. It is the registration and onboarding layer for all the entities of the ecosystem, and it provides trust evaluation mechanisms for the operational phases where the EUDIW Trust Framework is not required.

This section provides first an overview of the entities and processes involved in the trust infrastructure (:ref:`infrastructure-trust:Overview`). Then, it defines the general :ref:`x509-certificate-profile:X.509 Certificate Profile` and the :ref:`trust-artifact-common:Common Trust Artifacts` shared by both frameworks, followed by the framework-specific artifacts (:ref:`trust-artifact-eudiw:EUDIW Trust Artifacts` and :ref:`trust-artifact-oidfed:National Trust Artifacts`). Finally, it describes the related lifecycle (:ref:`trust-management:Trust Management and Lifecycle`).

Overview
--------

The IT-Wallet ecosystem operates on a federated trust infrastructure, requiring participating entities to establish mutual trust before engaging in any interaction involving User attributes.
To be able to perform a trust evaluation process, entities first need to onboard in the ecosystem (see :ref:`onboarding-procedure:Onboarding Procedure`).
During this phase, Non-Qualified EAA Providers and Relying Parties MUST declare whether they need to interoperate with European entities or they operate only within the national boundary.
This choice affects both the onboarding and the trust evaluation procedures. If only the national boundary is requested, the infrastructure of trust complies with the National Trust Framework. Otherwise, the EUDIW Trust Framework is necessary.

.. note::
    As the Wallet cannot know in advance whether it will be used to interact with national or European services, both the National and the EUDIW Trust Frameworks MUST be supported.
    PID Providers, QEAA Providers and PuB-EAA Providers MUST support the EUDIW Trust Framework, as they issue Credentials regulated by eIDAS 2.0.

In both cases, the onboarding and, eventually, European notification processes result in the release or update of different trust artifacts (detailed in sections :ref:`trust-artifact-common:Common Trust Artifacts`, :ref:`trust-artifact-eudiw:EUDIW Trust Artifacts` and :ref:`trust-artifact-oidfed:National Trust Artifacts`), then used during the trust evaluation processes (detailed in section :ref:`trust-evaluation:Trust Evaluation Process`).

.. toctree::
  :caption: Infrastructure of Trust Table of Contents
  :maxdepth: 3

  trust-pki-architecture.rst
  x509-certificate-profile.rst
  trust-artifact-common.rst
  trust-artifact-eudiw.rst
  trust-artifact-oidfed.rst
  trust-management.rst



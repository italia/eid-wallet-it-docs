.. include:: ../common/common_definitions.rst
.. include:: ../common/symbols.rst



Infrastructure of Trust
=======================

The IT-Wallet ecosystem operates within a federated trust infrastructure where participating entities establish cryptographic trust relationships and maintain compliance with common security standards. This infrastructure provides the foundation for secure Digital Credential operations across the ecosystem participants.

This section provides first an overview of the entities and processes involved in the trust infrastructure (:ref:`infrastructure-trust:Overview`). Then, it defines the essential trust artifacts (:ref:`infrastructure-trust:EUDIW Trust Artifacts` and :ref:`infrastructure-trust:OID FED Trust Artifacts`). Finally, it describes the related lifecycle (:ref:`infrastructure-trust:Trust Management and Lifecycle`).

.. warning::
    DA CAPIRE: parliamo ancora di IT-Wallet ecosystem?
   
    TODO: add ref `CIR2025/848`_, `CIR2025/848-Amendment`_, `TS05`_, `ETSITS119411-8`_, `ETSITS119475`_

Overview
--------

The IT-Wallet ecosystem operates on a federated trust infrastructure, requiring participating entities to establish mutual trust before engaging in any interactions involving User attribute.
To be able to perform a trust evaluation process, entities first needs to onboard in the ecosystem (see :ref:`onboarding-procedure:Onboarding Procedure`). 
During this phase, the entity performing the onboarding specifies whether it requires to be interoperable with European entities or it operates only in the national boundary. 
This choice will affect both the onboarding and the trust evaluation procedures. If only the national boundary is requested, the infrastructure of trust complies with OpenID Federation 1.0 (`OID-FED`_). Otherwise, the EUDI Wallet (EUDIW) trust infrastructure defined in `ARF`_ is necessary.

.. note::
    As the Wallet cannot know in advance whether it will be used to interact with national or European services, both `OID-FED`_ and EUDIW trust mechanisms MUST be supported.
    Credential Issuers and Relying Parties can instead decide based on their business logic.


In both cases, the onboarding and, eventually, European notification processes result in the release or update of different trust artifacts (detailed in sections :ref:`infrastructure-trust:EUDIW Trust Artifacts` and :ref:`infrastructure-trust:OID FED Trust Artifacts`), then used during the trust evalution processes (detailed in section :ref:`trust-evaluation:Trust Evaluation`).

.. warning::
    TODO: fare figura con entities e cosa gestiscono? Registrar / Federation Auhtority / WRPAC Provider... 

    A Registrar is the designated body that:

    - Manages the WRP registration lifecycle (onboarding, update, suspension, cancellation),
    - Ensures the integrity and publication of registration information,
    - Ensures interoperability by exposing WRP registration data via a national website and a single common REST API.

.. warning::
    TODO: fare figura con i vari livelli dell pki per la distribuzione dei certificati come doc di Francesco.

.. include:: trust-artifact-eudiw.rst
.. include:: trust-artifact-oidfed.rst

Trust Management and Lifecycle
------------------------------

.. warning::
  TODO: concordare struttura e contenuto
 
State Machine for Entities
^^^^^^^^^^^^^^^^^^^^^^^^^^

EUDIW Trust Management Process
""""""""""""""""""""""""""""""

OID FED Trust Management Process
""""""""""""""""""""""""""""""""

Revocation Mechanisms
^^^^^^^^^^^^^^^^^^^^^

CRL
"""

OCSP
""""

Token SL
""""""""








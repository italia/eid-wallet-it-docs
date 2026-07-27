.. include:: ../common/common_definitions.rst
.. Included via onboarding-system.rst at title level '-' (level 1).
 
Overview
--------
 
This Section introduces the actors that take part in onboarding, the components and services of the Onboarding System that realize them, and the way the two Trust Frameworks combine.
It gives the reader the context needed to follow the registration model, the processes and the lifecycle described in the Sections that follow.
 
System Actors and Roles
^^^^^^^^^^^^^^^^^^^^^^^
 
Two families of actors take part in onboarding, the entities that are onboarded, and the trust-infrastructure entities that operate the onboarding itself.
The trust-infrastructure roles are realized by the components and services of the Onboarding System, described in the next subsection.
 
**Entities being onboarded**
 
  - **Authentic Sources**: onboard to make their data available to the Credential Issuers, so that the data can be included in the Attestations.
  - **Wallet-Relying Parties**: onboard to be authorized to rely on the Wallet Units and to obtain the Trust Artifacts they need to operate. They are further split into:
 
    - **Credential Issuers**, that onboard to be authorized to issue the Credential types they declare;
    - **Relying Parties** and **Relying Party Intermediaries**, that onboard to be authorized to request User attributes from the Wallet Units.
 
  - **Wallet Providers**: onboard to have their Wallet Solution recognized in the ecosystem and to be notified.
 
**Trust-infrastructure entities**
 
  - **Supervisory Body**: during the onboarding it verifies the eligibility and the compliance of the entities, avails itself of the Registrar for technical registration, and acts as the national single point of contact for the notification to the European Commission.
  - **Registrar** and **Register**: the Registrar performs the technical registration of the Wallet-Relying Parties and writes their records into the **Register** as defined by [`CIR2025/848`_].
  - **Provider of WRPAC** and **Provider of WRPRC**: issue, respectively, the WRPAC and the WRPRC.
  - **National Federation Authorities**: the **Federation Trust Anchor** and its **Federation Intermediates**, that register Federation Entities and apply the metadata policies. Each Federation Authority issues the X.509 certificates and the Trust Marks for the Federation Entities it registers, while the registration Trust Mark is issued only by the Federation Trust Anchor, as described in :ref:`infrastructure-trust:Trust Mark registration-entity`.
    In IT-Wallet the National Trust Anchor also operates the root Certification Authority of the national X.509 signing PKI, whose root certificate and its distribution are described in :ref:`infrastructure-trust:PKI Architecture`.
 
.. note::
   A single organization may perform several of these functions at once.
 
Wallet Instances are not Federation Entities and are not onboarded directly.
A Wallet Instance is registered indirectly, through its Wallet Provider, see :ref:`wallet-instance-registration:Wallet Instance Initialization and Registration`, and it is deemed reliable through a Wallet Instance Attestation issued and signed by that Wallet Provider, see :ref:`wallet-instance-attestation-issuance:Wallet Instance Attestation Issuance`.
 
The notification of a notified entity is a Member State process defined by [`CIR2024/2980`_], described in :ref:`onboarding-system:Notification and Publication`.
 
System Components and Services
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 
The trust-infrastructure roles are realized, within the Onboarding System, by a set of components, each providing one or more services.
An onboarding entity interacts with the system through a single entry point, the Onboarding UI, that orchestrates the flow and routes each request to the responsible component, and that is therefore not shown as a separate component in the diagram below.
 
The table below lists the components, the services each of them provides, and the onboarding process that each service realizes.
 
.. list-table:: Components, Services and Processes
   :class: longtable
   :widths: 24 30 46
   :header-rows: 1
 
   * - **Component**
     - **Services**
     - **Realized process**
   * - Supervisory Body
     - Eligibility and compliance verification, approval of claims, schemas and Credential types
     - Precondition to every registration, see :ref:`onboarding-system:Eligibility and Compliance Preconditions`
   * - National Federation Management
     - Federation registration, issuance of Trust Marks, publication of the signed registries
     - :ref:`onboarding-system:Entity Registration`
   * - EUDIW Registration Management
     - Verification and registration of the Wallet-Relying Parties in the Register
     - :ref:`onboarding-system:Entity Registration`
   * - X.509 Certificate Management
     - Issuance and update of WRPAC, WRPRC, Sign/Seal and National Authentication certificates
     - :ref:`onboarding-system:Certificate and Trust Artifact Issuance`
   * - EU Notification Management
     - Signature of the EU Member State Trusted List and notification to the European Commission
     - :ref:`onboarding-system:Notification and Publication`
   * - Authentic Source Management
     - Registration of the Authentic Sources in the AS Registry
     - :ref:`onboarding-system:Authentic Source Registration`
   * - Claims and Schema Management
     - Registration of the claims and provisioning of the schemas
     - :ref:`onboarding-system:Attestation Onboarding`
   * - Catalog Management
     - Registration, activation and versioning of the Credential types in the Digital Credentials Catalog
     - :ref:`onboarding-system:Attestation Onboarding`
 
The components write the national registries and data stores described in :ref:`registry:Registry Infrastructure`, and interact, at EU level, with the European Commission for the notification and the alignment of the Catalogs.
Two data stores are kept separate on purpose, the Register, that holds the Wallet-Relying Party registration records defined by [`CIR2025/848`_] and drives the issuance of the certificates, and the notification dataset, that holds the notifiable information defined by [`CIR2024/2980`_] and feeds the Publication Service.
They overlap only in the identification data, so the split keeps the registration distinct from the notification.
 
The diagram below shows the components, the actors that interact with them and the data stores they write.
The Authentic Sources register in the AS Registry only, without a Register record and without Trust Artifacts, since they are neither Wallet-Relying Parties nor Federation Entities.
The Credential Issuers, instead, register as Entities and also declare the Credential types they issue, and they are added to the issuers of the types they declare in the Digital Credentials Catalog.

.. plantuml:: plantuml/onboarding-system-overview.puml
    :width: 99%
    :caption: `IT-Wallet Onboarding System. <https://www.plantuml.com/plantuml/svg/bLPHRnit37xNho3iXsr6x3RhqhLzA6exPo05rcLpXkp1B_8TVHQiamwIBeatzB-Fr9slYkEac0pO9v7yIF4ZUVxaWtIXgJHStOnlfTOOu7Upjj8LofImtFk0bT2u2H0iE5Lk0nJAOHwKDSBlbAcbanNuhIpiFPjifFQOI0hSo4Q76tm8KwrAKw49aDCNkaIhblbEbhWCUut0yDAKEeMPEcVlvrPR1yEtSHqB5zQ4fVe7uVmy4MbbCEnh1El2rYO2OmlqMCFvk-JGIRFZmrykqiD3E3Fh2dHT46_YIjLiOugvTGOTf9Y5378j_NUiPHwiEwKYeWG6owP6TwUyTNkOsM8_0Eb15XKCi_DPblqgH9T36Bn0vG3-5GAWLvs6W5G2p6QY7B7hNIb3WE7YWZza1xJwNC1WD9esOKj4gXoMjd4vZaQmCgFHRz8GDlCy6gtCPB8onug-3TvN9Trp_YvxEt__57skfQf8onImpBTOoVy9x_Fjo_Z4YxObWy19LArXxh1WP4dzuNs3heNEPNWC_VLHKZEo2FiJ-UJIVo6VNo8Fv6j1NbrBokcueWVLNNI3nVEtpFwwlBg5Fx5KFZmB-VIQPsIYzrmtrpGVoDFPogGdUxZY3gwmKDAHU6Li7KCckJBGUbrpHqZNbgh34eQpsMMsc9tW0id9Hb5Udo-YpxStiHZ-dboyVayjJmRK6cqA7lXek5XahsS_7-WuIWDyiPsBqpculhg4L_17DftIptKp6_FJjRDtgk1yh4pNKlrHIsgpxc-Lba2NSCfCZFcIQWsMrCSTPLGBF1QEYk4mAM1mg0HYUtaWh-ju7nEPqFtK2hhMURKoRUSmnEGCRkI3DRRg-NZp7PoqC3nq_N9eW6Ti8_DSAnmpkgXzx-fZzfyOF6A7q-KnH6F3WiJsgo1sSssRuj7q8fUDnhMrk_PsH4iMrq4tQnoLg2J5kQqgvJqPHLNCUrNn0unfWKzcxPfcBT0a92PP9dZaZiSV3-Fn0zWxAWPiYLwPahV6fshSzHy0wUMdrahpP8YQkQrghQJ9iVVhkYiGEHjqIABM9zrcCldOZPrUcm6iONHwDNikBlZntYcAzASkr3XWEOfODQARY7p0x8jkZF6U7WLpnCyjNO9BcxUHWBZZ633_vlzRqmBbiv5zl3oHs9JRieUD6z7b8wQcMGln2Kr1Vp_4Vm00>`_



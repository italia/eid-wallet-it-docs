.. include:: ../common/common_definitions.rst


Template e-Service PDND
=======================

The PDND provides a specialized tool that enhances API co-design processes by optimizing e-service publication and reuse. This functionality is defined in this document.

    - "Linee Guida sull'infrastruttura tecnologica della Piattaforma Digitale Nazionale Dati per l'interoperabilità dei sistemi informativi e delle basi di dati" (`PDND`_).

The template e-service serves as a standardized blueprint containing all necessary technical and descriptive metadata for an e-service. API Managers, who can be either Providers or Consumers within the PDND ecosystem, MAY create and maintain these templates.

Once a template e-service is published, it is accessible through the PDND Template Catalog, a centralized repository that facilitates discovery and reuse. This catalog enables any authorized PDND Participant to browse available templates and instantiate new e-services based on existing designs.


PDND Template e-service definition and guidelines
-------------------------------------------------

The PDND infrastructure supports the lifecycle management of Template E-Services, similar to that of traditional e-services. The lifecycle states include: **Draft**, **Active**, **Suspended**, and **Deprecated**. As with traditional e-services, PDND enforces role-based access control to govern status transitions.

Templates e-service Management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Template E-Service Creation
"""""""""""""""""""""""""""
Participants are enabled to create Templates E-Service via a guided wizard accessible through the PDND Web GUI (APIs will be available in the future). The creation workflow closely mirrors that of standard e-service creation, with the following distinctions:

    - An additional field identifies the intended recipient of the template.
    - The "Audience" field is omitted.
    - Thresholds are optional and serve as recommendations for Participants implementing the template.

Participants are prohibited from creating multiple templates with the same name: template names MUST be unique per participant. Upon creation, a template is initially set to the Draft state. Templates can then be published to the Template Catalogue, thereby making them accessible to all Participants.

Template E-Service Modification
"""""""""""""""""""""""""""""""
Participants who have created a template may edit it. The scope of editable fields depends on the template’s lifecycle state:

    - If the template is in Draft state, all fields are editable.
    - For templates in other states, only a restricted subset of fields can be modified directly.
    - Fields that cannot be modified in published templates require the creation of a new template version to apply changes.

Template versioning operates similarly to that of e-services, given that changes to the blueprint can impact instantiated services and then the Participants who consume that instance.

The following fields may be edited without triggering a new template version:

    - Name
    - Intended Recipient
    - Description
    - Voucher Time Limit
    - Documentation (excluding the OpenAPI specification)
    - Attributes

Template E-Service Suspension
"""""""""""""""""""""""""""""
Templates, like e-services, can be Suspended. When suspended:

    - The template is removed from the templates public catalogue.
    - Instantiation of new instances from the suspended template is disabled.
    - Previously instantiated instances remain unaffected.
    - Templates may be reactivated at any time.
    - Templates cannot be deleted.

Template E-Service Instantiation
""""""""""""""""""""""""""""""""
Participants may instantiate a Template E-Service by browsing the Template Catalogue and selecting a template. This process generates a new e-service.

Instantiation constraints include:

    - Only templates in the Active state are eligible for instantiation.
    - The instantiation is facilitated through a guided wizard in the PDND Web GUI.
    - Due to the standardization objective of templates, most fields are pre-populated and immutable during instantiation.
    - The following information cannot be modified during instantiation:

        - Documentation upload
        - Token expiration time
        - Name, description, and attributes

Instead, the following fields must be specified during instantiation:

    - Audience
    - Thresholds
    - Automatic/Manual Approval Policy

Additionally, although the OpenAPI specification is fixed, the following metadata fields can be provided so that PDND can automatically update the YAML specification:

    - Contacts (name, email, URL, Terms and Conditions URL)
    - Server URLs

Each instantiated e-service maintains an independent lifecycle analogous to standard e-services.

Version Management
^^^^^^^^^^^^^^^^^^
Template versioning follows a controlled process:

    - Publishing a new template version sets it to Active.
    - The previously Active version is automatically transitioned to Deprecated.
    - Only one Active version per template is allowed at any time.
    - Templates may also have a single Draft version coexisting with the Active version.

Instances derived from templates maintain independent versioning since Participants may update instance-specific fields (e.g., server URLs) multiple times, while the instance remains linked to the originating template version.

Consequently, template versions and instance versions are independent and not directly correlated.

Participants instantiating a template may then update either the specific instance or, if available, upgrade to a newer template version.

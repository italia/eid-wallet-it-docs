.. include:: ../common/common_definitions.rst


Digital Credentials Catalogue
=============================

The Digital Credentials Catalogue is the registry of all available Digital Credentials recognized within the IT-Wallet ecosystem. It is published by the Trust Anchor and publicly available by all Entities through a specialized Federation endpoint. It acts as a single reference point for all actors involved in the process of issuing, verifying and using Digital Credentials.

The Digital Credential Catalogue aims to:

  1. Facilitate Digital Credential discovery for Users.
  2. Standardize the technical and functional description of Digital Credentials.
  3. Enable interoperability between different Issuers and Relying Parties.
  4. Simplify the integration process for Wallet Providers and Relying Parties.
  5. Ensure trust in the ecosystem through certified information.
  6. Provide transparency on the ecosystem of available Digital Credentials.


The main Entities involved in the Digital Credential Catalogue are:

  - **Trust Anchor**: It manages and maintains the Digital Credential Catalogue, guaranteeing its authenticity and integrity.
  - **Supervisory Body**: It interacts with the Trust Anchor and the Digital Credential Catalogue to monitor the registration phase ensuring security and privacy according to national/European regulations, keeping all the information reliable and updated.
  - **Digital Credential Issuers**: The entities authorized to issue Digital Credentials, registering them in the Catalogue.
  - **Relying Parties**: They use the Digital Credential Catalogue to gather all the information needed about the Digital Credentials they intend to request during the presentation phase.
  - **Wallet Providers**: They access the Digital Credential Catalogue to identify the available Digital Credentials and to retrieve all necessary information for integrating them into their Wallet Solutions.
  - **Users**: The citizens who indirectly use the Digital Credentials Catalogue through their Wallet Instances to discover and request Digital Credentials.
  - **Authentic Sources**: The Entities that hold the original data that is attested in the Digital Credentials. They provide support to Issuers in registering the Digital Credentials in the Catalogue.


.. _fig_catalogue.svg:
.. plantuml:: plantuml/credential-catalogue-entities.puml
    :width: 99%
    :alt: The figure illustrates the Digital Credential Entities.
    :caption: `Entity-Relationship diagram of Digital Credential Catalogue. <https://www.plantuml.com/plantuml/svg/ZLJ1Rkis4BpxAxP6WQP00X-QtjeWgPEsFXGmuXGz6ZIvbeb8fCfTEbM__YrDELAUb6ST34khuSnmESjxOXKuLYKysiAoAc4PqA1ZcnwL57mH4Pwam1Pfzfrrkem6uPVbxM9vkrtwglPEy7UpsG_mY7lh43RhvzNBqwO7vbWh4tvQQ5zLtjsDVDbxnpVg3SbNUFFpGcDWkxTQCKv06p6wKpG5MdhzEW4M2GDDyUcBAJ1XEsAO07p5PgAx2J1hjbe5Cm69_-c3SWLkLSbJ-etqohwUW7nJPOaNAHVM4LkER5CuPhFtL5tfSmIlOJvCA7KHdGlW6GjB79hql1H4471eQ-3t85v07PKjrQv46A6JXTzJ7IpZh_DpfkO_Yg4r1lBkAlLTkF-MlvE6PVi_EeAtWmTZINivP53EYEg_4OalQIG-uU-soo4IFpXzy4dd9Rr1VarwwVUNSgf0EgbKoZgM7m4Vy9i3t1ULY8dcfY76wefYBT6qv4FpcpUD26ow2gJIITGxopxGkPig7HJK1qK8w2W6wmeWrFB0pScQQ1sLRlgwlP7kz2rHn42Zfmkh_34vU8WiJP1k6y3sBf9DAuP4SF4isq7eP0EMZNXUgv2OKdHo0ThAF9_ogQ_l4GJsK2Wf1R1kxqELsw1sFZBeSUN-O7NoUIhMmH-joRl_vrI1jjJkMMia6dgmZh48Yh4lcgeUCl471xdKQIlfP5gZDpu64KX2vnAqjQJ-foyD-22DTTBOD0sWc54uZ6XTx7Wtq6c0fBqVijrjg8lqTPVd7A6uAoqTiflVHQMD7JfJUm4Ahz0E4_nnXbQEPQ5c6LBBX_4rVJkVXZtuT1gPe8jjVs6-VZ2CzGQiQvSE-tyc6pSxo6fVyezFuZXc8TCDizVnTP7pO4_BzatlmjG3hdmV3XZJw12qaLuvOkKqGfq11dPDNhvzR0dw3bREs82Qo-RzHgN-bKfVsRYNECIg_080>`_


.. .. figure:: ../../images/catalogue.svg
..     :figwidth: 100%
..     :align: center
..     :target: https://www.plantuml.com/plantuml/svg/ZLHDZnit3BtxLp16WMw1E3wqlHGeaDJR3mD9Qwopw751I_HOM8qq5JdhJdzzAMkyCnixs3aOy53aUq_aezwpO9AszhCtBXZVMeA3ICC_BPS9Z-yg9uTsrp8b4uDGa7Scril6OyWr2nRhtMwv-c6noQ7xJn-NDR9Gqj33AjPD3BccoVYpR-6MzYuGR3Ttwy-_RcTlRFbUh_xwy_xkumHYQHkqwVj1WDFJnLup5jma9yGz_t2R7dofvNKCHSh5uGa1ZyInfiMFIqD9tDuP59fMO55mXpmnsqVpE2qptvydQexLn4p5VA8qBVUHkkbAfsKw-s0msMd9zAyvOAZe0RrC70NneyHcMl8HlQSfm4iNM9oquiuUcisU_NrZKD37ggMtCBzrbTClM2MoUkRGCwpEvtDDkAFAiQGk_rzfHjBarCSWxa4b0JwXyxZp15VWjF2RulQVvsVZpRzJGHjA7CDD7eLYtpEb4uSJzny5XkCXWdLieauVC5Xb_QSbbjSuCfxY3zULrB9y2EOGCy_d_0NbC_FbtoSCM16VM6fqGVJ788ThzncwCoPLuoddjcEX-eRRHZthEARkbsWx9TWE4SYX4saCJcBYSpSn3mkQ0p811MwJ2nKm6VqZtKcQSZsXwSQyezKV-1rpIuclJXVMvJ0h-D2ADa6xRI4VYgDyQHJ80A_Eib-CWJQHxrJp1bD6ojOf0UWZypBbKr-VBGWIeK8D9N1X7rDTse2xs0gOwypZBHleot9iKdnojjp-xrC4-b1_PsE8-LA32q9LGg4nQOv6AC0l59JGm8tQoLnZjh5DIf29pY7eOvdzZ-WjnAID3UWXRmEW22c6LQvNEpuiTLuWRUyBRmyN6YpzTl1piL2xyuuFHSrlojBRZe9jeYOghi9UElZb3gs3QA4HXgEJm_MQiPolcZt5F8q2CDXsN5YU7qhNUWCkzAMN_J-3NHTxuTKnvUzVi-CL2GNkqdi3tc2v2EvKjkz63wQvm2hluGLYNXs6tjBhm8B143GbmSAkA-KFjpt0MC4wM9V8YE-UNrGUFwdyXOpt56nR-_y1


The following table summarizes the main information that MUST be provided by the Digital Credential Catalogue:

.. list-table:: Digital Credential Catalogue - Main information
   :class: longtable
   :widths: 30 70
   :header-rows: 1

   * - Information related to
     - Description
   * - Digital Credential Metadata
     - Essential identifying information and characteristics of the Digital Credential, including:

       - **Credential Unique identifier**: A unique identifier string of each Digital Credential.
       - **User authentication methods**: User authentication mechanisms used to request the Digital Credential, if required by Issuers or Authentic Sources.
       - **Minimum Level of Assurance**: The minimum Level of Assurance required for the Digital Credential's reliability. It MUST take into account the Level of Assurance of User authentication, when applicable, and Wallet Instance.
       - **Additional display characteristics**: Visual and formatting specifications, such as a background reference image, logo, etc.
   * - Digital Credential Issuers
     - Details about the organization authorized to issue the Digital Credential, such as:

       - **Issuer identifiers**: Unique identifier for the Digital Credential issuer.
       - **Issuer type**: Classification as PID, (Q)EAA, or Pub-EAA Provider.
       - **Additional information**: Organizational details including name, code, and contact information.
   * - Authentic Sources
     - Information about the authoritative data source, such as:

       - **Authentic Source identifiers**: Unique identifier for the Digital Credential's authoritative source.
       - **Authentic Source type**: Classification as Public or Private entity.
       - **Additional information**: Organizational details including name, code, and contact information.
   * - Technical Specification
     - Technical details, including:

       - **Digital Credential schemes**: Framework and structure specifications.
       - **Digital Credential formats**: Data format and encoding standards.
       - **Authentication policy**: Methods and requirements for verification.
   * - Terms of Use
     - Conditions and limitations for Digital Credential usage, such as:

       - **Credential validity**: Time period during which the Digital Credential is valid and, when applicable, mechanisms and technical details for invalidating Digital Credentials (revocation/suspension methods).
       - **Restriction policy**: If applicable, rules governing the Digital Credential's use and limitations according to national regulations. It is used, for example, to specify if only specific legal type Entities, for example Pub-EAA Provider and public Wallet Solutions, are allowed to issue and obtain the Digital Credential.
       - **Pricing policy**: Information related to pricing models of Digital Credential, such as `free`, `issuance_based`, `verification_based`.
       - **Digital Credential purposes**: Information related to the allowed purposes for which the Digital Credential can be used. Each Digital Credential type can be used for multiple purposes.
   * - Claims and Taxonomy References
     - Content and classification information:

       - **List of displayed claims**: Specific Digital Credential content displayed to the User.
       - **Structured taxonomy references**: Classification systems and controlled vocabularies used.


The Trust Anchor MUST publish and keep up to date all the information at the Digital Credential Catalogue `.well-known` endpoint ensuring data reliability, authenticity and integrity. In particular, the Digital Credential Catalogue, claims and taxonomy MUST be available through the ``.well-known/credential-catalogue`` endpoint.

Digital Credentials Categories
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Digital Credentials recognized within the IT-Wallet ecosystem are hierarchically classified and standardized according to the following main domains and categories. Additional categories MAY be added as the IT-Wallet ecosystem grows.

.. list-table:: Digital Credential Domains and Categories
   :class: longtable
   :header-rows: 1
   :widths: 20 30 50

   * - **Domain**
     - **Category**
     - **Description**
   * - *IDENTITY*
     - * PERSON_IDENTIFICATION
       * ELECTRONIC_RESIDENCY
     - Credentials that establish or verify the identity of a person, including physical and digital identity documents legally recognized by national laws.
   * - *AUTHORIZATION*
     - * DRIVING_LICENSE
       * PROFESSIONAL_LICENSE
       * TRAVEL_DOCUMENT
       * ACCESS_PERMIT
     - Credentials that grant specific permissions, rights or authorizations to perform certain activities or access restricted areas.
   * - *EDUCATION*
     - * ACADEMIC_DEGREE
       * CERTIFICATE
       * TRAINING_RECOGNITION
     - Credentials related to educational achievements, qualifications, and professional training recognition.
   * - *HEALTH*
     - * INSURANCE_CARD
       * DISABILITY_CARD
       * MEDICAL_PRESCRIPTION
     - Credentials related to healthcare access, medical history, insurance coverage, and health-related documents.
   * - *FINANCIAL*
     - * INCOME_CERTIFICATE
       * TAX_STATEMENT
       * FAMILY_ECONOMIC_STATUS
     - Credentials that attest to financial status, income levels, taxation, or economic situation of individuals or families.
   * - *MEMBERSHIP*
     - * ASSOCIATION
       * LOYALTY_PROGRAM
       * CLUB_MEMBERSHIP
     - Credentials that confirm affiliation with organizations, participation in programs, or membership status.
   * - *ATTESTATION*
     - * PUBLIC_STATEMENT
       * CIVIL_STATUS
       * CERTIFICATION
     - Credentials that provide official statements, confirmations of status, or certifications issued by authorities.


Digital Credentials Catalogue Structure
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Digital Credentials Catalogue contents is secured in a JWS that contains the following JOSE header parameters:

.. _table_catalogue_parameters:
.. list-table::
   :class: longtable
   :header-rows: 1
   :widths: 25 50 25

   * - JOSE header
     - Description
     - Reference
   * - **typ**
     - REQUIRED. It MUST be set to ``JOSE``.
     - [:rfc:`7515` Section 4.1.9].
   * - **alg**
     - REQUIRED. A digital signature algorithm identifier such as per IANA "JSON Web Signature and Encryption Algorithms" registry. It MUST be one of the supported algorithms in Section :ref:`Cryptographic Algorithms <algorithms:Cryptographic Algorithms>` and MUST NOT be set to ``none`` or with a symmetric algorithm (MAC) identifier.
     - [:rfc:`7515` Section 4.1.1].
   * - **kid**
     - REQUIRED. Unique identifier of the public key.
     - [:rfc:`7515` Section 4.1.4].
   * - **x5c**
     - OPTIONAL. Contains the X.509 public key Certificate or Certificate chain [:rfc:`5280`] corresponding to the key used to digitally sign the JWS. When the header parameter `kid` value is present, it MUST refer to the same leaf's cryptographic public key used with the X.509 Certificate.
     - [:rfc:`7515` Section 4.1.6.].
   * - **cty**
     - REQUIRED. It MUST be set to ``application/json``.
     - [:rfc:`7515` Section 4.1.6.].

The JWS payload contains the following parameters:

.. list-table:: First-level Fields of the Catalog
   :class: longtable
   :header-rows: 1
   :widths: 30 70

   * - Field Name
     - Description
   * - **catalog_version**
     - REQUIRED. Version of the Digital Credential Catalogue format.
   * - **iss**
     - REQUIRED. Issuer identifier of the Digital Credential Catalogue.
   * - **last_modified**
     - REQUIRED. Timestamp of the last modification to the Digital Credential Catalogue.
   * - **taxonomy_uri**
     - REQUIRED. URI of the claims taxonomy reference document.
   * - **taxonomy_uri#integrity**
     - OPTIONAL. Cryptographic digest of the taxonomy document for integrity verification.
   * - **credentials**
     - REQUIRED. Array containing Digital Credential definitions.

Each element of the ``credentials`` array contains at least the following information:

.. list-table:: First-level Fields of Each Credential Entry
   :class: longtable
   :header-rows: 1
   :widths: 30 70

   * - Field Name
     - Description
   * - **version**
     - REQUIRED. Version of the Digital Credential definition.
   * - **credential_type**
     - REQUIRED. Unique identifier of the Digital Credential type.
   * - **legal_type**
     - REQUIRED. Legal classification of the Credential (e.g., ``pub-eaa``, ``qeaa``, ``eaa``).
   * - **localization**
     - OPTIONAL. Localization settings, including:

       * **default_locale**: Default language for text.
       * **available_locales**: List of supported languages.
       * **base_uri**: Base URI for localization resources.
       * **version**: Version of the localization files.
   * - **name**
     - REQUIRED. Human-readable name of the Digital Credential. A suffix ``_l10n_id`` MAY be added for content localisation management.
   * - **description**
     - REQUIRED. Human-readable Digital Credential description. A suffix ``_l10n_id`` MAY be added for content localisation management.
   * - **restriction_policy**
     - OPTIONAL. Legal restrictions on Wallet Solutions and/or Credential Issuers allowed to request/issue the Digital Credential.

       * **allowed_wallet_ids**: List of allowed Wallet Solutions identifiers.
       * **allowed_issuer_ids**: List of allowed Credential Issuers identifiers. If present, it represents a whitelist of Credential Issuers that may be added by the Trust Anchor in the **issuers** field of the corresponding Digital Credential.
   * - **pricing_policy**
     - OPTIONAL. Information about Digital Credential pricing, including:

       * **models**: REQUIRED. Array of pricing models applicable to the Digital Credential, each containing:

         - **pricing_type**: Type of pricing model, such as ``issuance_based``, ``verification_based``, ``subscription_based``, ``other``.
         - **price**: Cost associated with the model.
         - **currency**: Currency of the price.

       * **pricing_model_uri**: URI to the detailed pricing model documentation.
   * - **validity_info**
     - Information about Digital Credential validity, including at least:

       * **max_validity_days**: Maximum validity period in days.
       * **status_methods**: Supported status verification methods (e.g. ``status_list``).
       * **allowed_states**: Allowed Digital Credential states (e.g. ``valid``, ``revoked``, ``suspended``).
   * - **authentication**
     - REQUIRED. Digital Credential authentication requirements

       * **user_auth_required**: REQUIRED. Flag indicating if User authentication is required during the issuance of the Digital Credential.
       * **min_loa**: REQUIRED. Minimum Level of Assurance required for Digital Credential authentication. It MUST include the Level of Assurance of the User authentication and the Wallet Instance requesting the Digital Credential.
       * **supported_eid_schemes**: REQUIRED if ``user_auth_required`` is ``true``. Supported digital identity authentication schemes.
   * - **purposes**
     - REQUIRED. Array of usage purposes for which the Digital Credential can be used, defining specific usage contexts and required claims for each purpose, such as:

       * **id**: Unique identifier for the purpose (e.g., "driving-authorization", "person-identification").
       * **description**: Human-readable purpose description with a suffix ``_l10n_id`` for content localisation.
       * **category**: Main category in the Credential taxonomy (e.g., ``AUTHORIZATION``, ``IDENTITY``).
       * **subcategory**: Subcategory within the taxonomy (e.g., ``DRIVING_LICENSE``, ``PERSON_IDENTIFICATION``).
       * **claims_required**: Array of claim identifiers that are required when using the Credential for this purpose.
       * **claims_recommended**: Array of claim identifiers that are recommended but not mandatory for this purpose.
   * - **issuers**
     - REQUIRED. Array of relevant information about authorized Credential Issuers, including administrative and technical data such as Organization name, a reference to the API specification document and supported issuance mechanisms (for example the deferred flow support).
   * - **authentic_sources**
     - REQUIRED. Array of relevant information about authorized Authentic Sources, including administrative and technical data related the provisioning of data to the Credential Issuers.
   * - **formats**
     - REQUIRED. Array of supported technical formats of Digital Credentials.
   * - **display_properties**
     - REQUIRED. Visual presentation properties of Digital Credentials, e.g.:

       * **templates**: Visual templates for the Credential, e.g. `svg` template.
       * **background_color**: Background color in hexadecimal format.
       * **text_color**: Text color in hexadecimal format.
       * **logo_uri**: URI to the Digital Credential logo.
   * - **claims**
     - REQUIRED. Array of claims contained in the Digital Credential.


The corresponding example of Digital Credentials Catalogue as decoded in JSON for both header and payload is the following:

.. literalinclude:: ../../examples/catalogue-example-header.json
  :language: JSON

.. literalinclude:: ../../examples/catalogue-example-payload.json
  :language: JSON

.. note::
  For a better and more efficient management of the localisation of the information contained in the Digital Credentials Catalogue, an Entity consulting it SHOULD:

    - Download the basic version of the Digital Credentials Catalogue (compact, without localisations) using the ``.well-known/credential-catalogue`` endpoint.
    - Determine the User's preferred language.
    - Download only the necessary localisation bundles.
    - Dynamically merge localised content with the Digital Credentials Catalogue structure.

  A non-normative example of a localisation bundle output is given below:

    .. code-block:: json

      {
        "driving_license.name": "Patente di Guida",
        "driving_license.description": "Patente di guida ufficiale valida in Italia e nell'UE",
        "purpose.driving_authorization.name": "Abilitazione alla guida",
        "purpose.driving_authorization.description": "Verifica di Abilitazione alla guida",
        "claims.given_name.name": "Nome",
        "...": "..."
      }

  Localization bundles MUST be available at the URI specified in the **localization_info.bundles_base_uri** claim of the Digital Credentials Catalogue. Each locale bundle MUST be accessible following the naming pattern **{locale_code}.json**, where **{locale_code}** is replaced with the corresponding locale code from the **available_locales** array.

  A non-normative example of the Italian localization URI for the mDL bundle would be **https://trust-registry.eid-wallet.example.it/.well-known/l10n/mdl/it.json**.

  Entities SHOULD verify the integrity of downloaded localization bundles using the digest method and values specified in the **localization_info.integrity** claim. This ensures that the localization data has not been tampered with during transmission.


Claims Taxonomy
^^^^^^^^^^^^^^^^

The Digital Credential Catalogue, MUST include also a reference URI to Claim Taxonomy providing, in a single resource, the semantic information of all registered and available claims within the IT-Wallet ecosystem. It MUST be Credential format neutral and has the aim of facilitating Digital Credentials integrations in the IT-Wallet Technical Solutions.

A non-normative example of the Claim Taxonomy is given below.

.. literalinclude:: ../../examples/catalogue-claims-taxonomy.json
  :language: JSON


Digital Credentials Catalogue Endpoint
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The Digital Credentials Catalogue Endpoint MUST be a well-known HTTPS URI [:rfc:`8615`] that provides public access to information related to the Credentials available in IT-Wallet.

Digital Credentials Catalogue Request
---------------------------------------

The Digital Credentials Catalogue Request MUST be an HTTP GET using the application/jose media type as in the following non-normative example.

.. code-block:: http

    GET /.well-known/credential-catalogue HTTP/1.1
    Host: www.trust-registry.eid-wallet.example.it
    Content-Type: application/jose

.. note::
  As a future enhancement, the Trust Anchor MAY implement a dynamic endpoint that enables filtering credentials by type, while offering pagination capabilities, to support more efficient and flexible browsing of the Digital Credentials Catalogue.


Digital Credentials Catalogue Response
----------------------------------------

The Digital Credentials Catalogue Response MUST be a JWS that contains the parameters listed in the :ref:`table of Digital Credentials Catalogue parameters <table_catalogue_parameters>`.

A non-normative example of the response is provided below.

.. literalinclude:: ../../examples/catalogue-example-jws.txt
  :language: text

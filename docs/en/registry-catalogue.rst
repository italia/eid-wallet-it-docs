.. include:: ../common/common_definitions.rst


Registry and Digital Credentials Catalogue
+++++++++++++++++++++++++++++++++++++++++++

The catalogue of attributes provides information regarding the formats and schemes of the Digital Credentials, the claims they contain, and details about Issuers and Authentic Sources. Furthermore, the catalogue includes additional information to facilitate the verification of the authenticity and reliability of its contents.
The catalogue must be used by all technical solutions that operate within the IT-wallet system for the retrieval of information relating to the PID/(Q)EAA contained in the catalogue, in particular:

  - Wallet Providers MUST access the catalogue to identify the Digital Credentials available within the Wallet ecosystem, and MUST use it to retrieved all necessary information for integrating the needed Digital Credentials into their own Wallet Solution.
  - The Authentic Sources MUST participate in the processes of the registration and maintenance related to the informations necessary for the Issuance of the Digital Credentials.
  - Credential Issuers MUST consult the Catalogue for the Attributes provided by the Authentic Sources and that MUST be included in the Digital Credentials.
  - Relying Parties MUST use the catalogue to gather all the information needed about the Digital Credentials they intend to support during the presentation phase.

In accordance with the Italian IT-Wallet Guidelines, the Catalogue lists all available Digital Credentials, specifying if the Digital Credential are Public or not and if their availability is exclusively on Public Wallets in the case they are issued pursuant to Presidential Decree No. 445 of December 28, 2000.

In the case of Public Authentic Sources, the Catalogue provides information from the PDND e-service Catalogue, specifically for Attribute retrieval, the Attributes themselves, and any associated User Authentication requirements with their Levels of Assurance.

The Catalogue lists the Issuers authorized to issue each Digital Credential.

The Catalogue is published and maintained within the registry in JSON format. It is accessible for consultation by anyone at the following endpoint: “https://example.com”.

Digital Credentials Catalogue parameters
----------------------------------------
The catalogue contains the following parameters.

.. list-table::
   :header-rows: 1
   :widths: 25 50 25

   * - Claim
     - Description
     - Reference
   * - **credentials_catalogue_version**
     - REQUIRED. Version number of the catalogue.
     - IT-Wallet National Guidelines
   * - **credentials_catalogue**
     - REQUIRED. Array containing the registered Digital Credential.
     - IT-Wallet National Guidelines
   * - **version**
     - REQUIRED. Version number of the Digital Credential.
     - IT-Wallet National Guidelines
   * - **unique_identifier**
     - REQUIRED. String representing the unique indentifier value of the Digital Credential.
     - IT-Wallet National Guidelines
   * - **name**
     - REQUIRED. String representing the name of the Digital Credential.
     - IT-Wallet National Guidelines
   * - **description**
     - REQUIRED. String representing the description of the Digital Credential.
     - IT-Wallet National Guidelines
   * - **is_pub**
     - REQUIRED. Boolean value set to ``true`` if the Digital Credential is a Public Electronic Attestation of Attribute.
     - IT-Wallet National Guidelines
   * - **is_qeaa**
     - REQUIRED. Boolean value set to ``true`` if the Digital Credential is a Qualified Electronic Attestation of Attribute.
     - IT-Wallet National Guidelines
   * - **is_eaa**
     - REQUIRED. Boolean value set to ``true`` if the Digital Credential is a non-qualified Electronic Attestation of Attribute.
     - IT-Wallet National Guidelines
   * - **is_proof_of_identity**
     - REQUIRED only if ``is_pub`` is set to true. Boolean value set to ``true`` if the Digital Credential is an identification document pursuant to Presidential Decree No. 445 of December 28, 2000.
     - IT-Wallet National Guidelines
   * - **is_public_wallet_restricted**
     - REQUIRED. Boolean value set to ``true`` if the Digital Credential is enabled only for public wallet solutions.
     - IT-Wallet National Guidelines
   * - **wallet_solutions_restriction**
     - REQUIRED. JSON Object containing restriction information about the wallets enabled to receive the Digital Credentials. It contains:
       
       - **is_public_restricted**: REQUIRED. Boolean value set to ``true`` if the Digital Credentials is restricted to public wallet solutions.
       - **providers_enabled**: REQUIRED only if ``is_public_restricted`` is set to ``true``. Array containing the list of wallet solutions enabled to receive the Digital Credential.
     - IT-Wallet National Guidelines
   * - **validity_days**
     - REQUIRED. Numerical value representing the Credential's lifespan in days.
     - IT-Wallet National Guidelines
   * - **issuers**
     - REQUIRED. JSON Object containing required information about the issuers. It MUST contain:
       
       - **iss**: URL string representing the Credential Issuer unique identifier.
       - **organization_name**: String representing the name of the administrative authority that has issued the credential.
       - **organization_country**: String representing Alpha-2 country code, as specified in ISO 3166-1, of the country or territory of the credential issuer.
       - **credential_formats**: Array containing Credential formats supported.
       - **authentication_required**: REQUIRED. JSON Object containing information on the need to present the PID to obtain the Credential, it contains:
         
         - **is_required**: REQUIRED. Boolean value set to ``true`` if the PID is requested to obtain the Credential.
         - **loa_level**: REQUIRED only if **is_required** is set to ``true``. String identifying the Level Of Assurance requested during the User authentication.
       
       - **update_status**: REQUIRED. JSON Object containing information about the status of the Credential, it MUST contain:
         
         - **type**: String representing the verification method of the Credential validity status. The supported values are: ``status_assertion`` and ``status_list``.
       
       - **credentials_required**: OPTIONAL. Array containing one or more ``unique_identifier`` related to Credentials requested for the issuance of the Digital Credential.
       - **data_source**: REQUIRED. JSON Object containing information about the credential data origin, it MUST contain:
         
         - **organization_name**: String representing the name of the Authentic Source.
         - **organization_country**: String representing Alpha-2 country code, as specified in ISO 3166-1, of the country or territory of the Authentic Source.
         - **authentication_required**: JSON Object containing information on the need to demonstrate User authentication to obtain the User Attributes, it contains:
           
           - **is_required**: REQUIRED. Boolean value is set to ``true`` if the User authentication proof is requested to obtain the credential.
           - **loa_level**: REQUIRED only if ``is_required`` is set to ``true``. String identifying the Level Of Assurance requested during the User authentication.
        
         - **trust_framework**: REQUIRED. JSON Object containing information about the trust framework used by Authentic Source to expose its services.
           
           - **type**: REQUIRED. String representing the type of trust framework, for public Authentic Sources it MUST be set to ``PDND``.
           - **issuing_service**: REQUIRED. JSON Object containing information about the service that provides the Credential Issuer with all attribute claims necessary for the issuance of a Digital Credential, it MUST contain:
             
             - **version**: Version number representing the version of the service.
             - **name**: String representing the name of the service.
             - **description**: String representing the description of the service.
             - **provider**: String representing the name of the service provider, in case of ``type`` is set to ``PDND`` Trust Framework, the value corresponds to the name of the provider defined in *PDND* infrastucture.
           
           - **update_status_service**: REQUIRED. JSON Object containing information about the service that allows to notify the Credential Issuer of a change of status and/or value of a specific attribute, it MUST contain:
             
             - **version**: Version number representing the version of the trust framework service for the status update of the credential.
             - **name**: String representing the name of the service.
             - **description**: String representing the description of the service.
             - **provider**: String representing the name of the service provider, in case of ``type`` is set to ``PDND`` Trust Framework, the value corresponds to the name of the provider defined in *PDND* infrastucture.
     - IT-Wallet National Guidelines
   * - **formats**
     - REQUIRED. Object containing the available Credential formats, it MUST contain:
       
       - **credential_configuration_id**: String representing a unique identifier of a Credential in a specific format. Its value MUST be mapped by the Credential Issuer in its ``credential_configurations_supported`` metadata claim.
       - **format**: String representing the Credential Format Identifier as described in Appendix A of ``OpenID4VCI``.
       - **is_proximity_enabled**: Boolean set to ``true`` if proximity presentation is enabled.
       - **is_remote_enabled**: Boolean set to ``true`` if the remote presentation is enabled.
       - **vct**: Credential type value MUST be an HTTPS **URL String** and it MUST be set using one of the values obtained from the PID/(Q)EAA Issuer metadata. It is the identifier of the SD-JWT VC type and it MUST be set with a collision-resistant value as defined in Section 2 of RFC 7515. It MUST contain also the number of version of the Credential type (for instance: https://issuer.example.org/v1.0/personidentificationdata). As defined in Section 3.2.2.2 [SD-JWT-VC]
       - **schema_uri**: URL of the Credential schema.
       - **schema_uri#integrity**: the value MUST be an "integrity metadata" string.
     - IT-Wallet National Guidelines
   * - **schema**
     - REQUIRED. JSON Object containing information about the credential schema. It MUST contain:
       
       - **schema_version**: **Number** representing the version of the credential schema
       - **user_attributes**: **Object** containing the attributes of the credential, including the name and description of every attribute
     - IT-Wallet National Guidelines

A non-normative example of Digital Credentials Catalogue is provided below.

.. literalinclude:: ../../examples/catalogue-example.json
  :language: JSON
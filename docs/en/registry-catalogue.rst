.. include:: ../common/common_definitions.rst


Registry and Digital Credentials Catalogue
+++++++++++++++++++++++++++++++++++++++++++

The catalogue of attributes provides information regarding the formats and schemes of the Digital Credentials, the claims they contain, and details about Issuers and Authentic Sources. Furthermore, the catalogue includes additional information to facilitate the verification of the authenticity and reliability of its contents.
The catalogue must be used by all technical solutions that operate within the IT-wallet system for the retrieval of information relating to the PID/(Q)EAA contained in the catalogue, in particular:

  - Wallet Providers MUST access the catalogue to identify the Digital Credentials available within the Wallet ecosystem, and MUST use it to acquire all necessary information for integrating the needed Digital Credentials into their own Wallet Solution.
  - The Authentic Sources MUST participate in the processes of the registration and maintenance related to the informations necessary for the Issuance of the Digital Credentials.
  - Credential Issuers MUST consult the Catalogue for the Attributes provided by the Authentic Sources and that MUST be included in the Digital Credentials.
  - Relying Parties MUST use the catalogue to gather all the information needed about the Digital Credentials they intend to support during the presentation phase.

In accordance with the Italian IT-Wallet Guidelines, the Catalogue lists all available Digital Credentials, indicating if the Digital Credential are Public or not and if their availability is exclusively on Public Wallets in the case they are issued pursuant to Presidential Decree No. 445 of December 28, 2000.

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
     - Version number of the catalogue
     - IT-Wallet Guidance Policy
   * - **credentials_catalogue**
     - Array containing the registered Digital Credential
     - IT-Wallet Guidance Policy
   * - **version**
     - Version number of the Digital Credential
     - IT-Wallet Guidance Policy
   * - unique_identifier
     - **String** representing the unique indentifier of the Digital Credential
     - IT-Wallet Guidance Policy
   * - name
     - **String** representing the name of the Digital Credential
     - IT-Wallet Guidance Policy
   * - description
     - **String** representing the description of the Digital Credential
     - IT-Wallet Guidance Policy
   * - is_pub
     - **Boolean** value set to true if the Digital Credential is a Public Electronic Attestation of Attribute
     - IT-Wallet Guidance Policy
   * - is_qeaa
     - **Boolean** value set to true if the Digital Credential is a Qualified Electronic Attestation of Attribute
     - IT-Wallet Guidance Policy
   * - is_eaa
     - **Boolean** value set to true if the Digital Credential is a non-qualified Electronic Attestation of Attribute
     - IT-Wallet Guidance Policy
   * - is_proof_of_identity
     - CONDITIONAL. REQUIRED if is_pub set to true. **Boolean** value set to true if the Digital Credential is an identification document pursuant to Presidential Decree No. 445 of December 28, 2000
     - IT-Wallet Guidance Policy
   * - is_public_wallet_restricted
     - **Boolean** value set to true if the Digital Credential is enable only for public wallet solutions
     - IT-Wallet Guidance Policy
   * - wallet_solutions_restriction
     - **Object** containing information about the wallet enabled to receive the Digital Credentials
     
       - **is_public_restricted**: **Boolean** value set to true if the Digital Credentials is restricted to public wallet solutions.
       - **providers_enabled**: **Array** containing the list of wallet solutions enabled to use the Digital Credential
     - IT-Wallet Guidance Policy
   * - validity_days
     - **Number** value representing the lifespan of the credential in days
     - IT-Wallet Guidance Policy
   * - issuers
     - **Object** containing required information about the issuers.
     
       - **iss**: **URL string** representing the credential issuer unique identifier as defined in *RFC7519, Section 4.1.1*
       - **organization_name**: **String** representing the name of the administrative authority that has issued the credential, as defined in *Commission Implementing Regulation EU_2024/2977*.
       - **organization_country**: **String** representing Alpha-2 country code, as specified in ISO 3166-1, of the country or territory of the credential issuer, as defined in *Commission Implementing Regulation EU_2024/2977*
       - **authentication_required**: **Object** containing information on the need to present the PID to obtain the certification, according to *IT-Wallet Guidance Policy* it must contain two sub-values:
       
         - **is_required**: **Boolean** value set to true if the PID is requested to obtain the credential.
         - **loa_level**: CONDITIONAL, REQUIRED if required set to true. **Number** value set to 1 if the Level Of Assurance requested is low, value set to 2 if the Levele Of Assurance requested is substantial, value set to 3 if the assurance level requested is high
       
       - **update_status**: **Object** containing information about the status of the credential, according to *IT-Wallet Guidance Policy* it must contains two values:
       
         - **type**: **String** representing the name of the type of proof of a credential's current validity status.
         - **endpoint**: **String** representing the endpoint of the type of proof used.
       
       - **credentials_required**: **Array** containing the credentials needed to obtain the credential
       - **data_source**: **Object** containing information about the credential data origin, as defined in the *IT-Wallet Guidance Policy* it MUST contains:
         - **organization_name**: **String** representing the name of the administrative authority that has issued the credential, as defined in *Commission Implementing Regulation EU_2024/2977*.
         - **authentication_required**: **Object** containing information on the need to present the PID to obtain the certification, according to *IT-Wallet Guidance Policy* it must contain two sub-values:
       
           - **is_required**: **Boolean** value set to true if the PID is requested to obtain the credential.
           - **loa_level**: CONDITIONAL, REQUIRED if required set to true. **Number** value set to 1 if the Level Of Assurance requested is low, value set to 2 if the Levele Of Assurance requested is substantial, value set to 3 if the assurance level requested is high
        
         - **trust_framework**: **Object** containing information about the trust framework
         
           - **type**: **String** representing the type of trust framework, for public credentials PDND MUST be the trust framework used, according to *LLGG*
           - **issuing_service**: **Object** containing information about the trust framework service, it must contain three sub-value:
           
             - **version**: **Number** representing the version of the trust framework service.
             - **name**: **String** representing the name of the trust framework service.
             - **description**: **String** representing the description of the trust framework service.
             - **provider**: **String** representing the name of the provider, as defined in *PDND*
           
           - **update_status_service**: **Object** containing information about the trust framework service for the status update of the credential. it must contain three sub-value:
           
             - **version**: **Number** representing the version of the trust framework service for the status update of the credential.
             - **name**: **String** representing the name of the trust framework service.
             - **description**: **String** representing the description of the trust framework service.
             - **provider**: **String** representing the name of the provider as defined in *PDND*.

     - IT-Wallet Guidance Policy
   * - formats
     - **Object** containing the different formats supported by the credential, according to the *IT-Wallet Guidance Policy* it MUST contain:
     
       - **configuration_id**: **String** representing a unique identifier of the credential format.
       - **format**: **String** representing the name of the credential id format.
       - **is_proximity_enabled** : **Boolean** set to true if proximity presentation is enabled, according to *IT-Wallet Guidance Policy*
       - **is_remote_enabled**: **Boolean** set to true if the remote presentation is enabled, according to *IT-Wallet Guidance Policy*
       - **vct**: Credential type value MUST be an HTTPS **URL String** and it MUST be set using one of the values obtained from the PID/(Q)EAA Issuer metadata. It is the identifier of the SD-JWT VC type and it MUST be set with a collision-resistant value as defined in Section 2 of RFC 7515. It MUST contain also the number of version of the Credential type (for instance: https://issuer.example.org/v1.0/personidentificationdata). As defined in Section 3.2.2.2 [SD-JWT-VC]
       - **schema_uri**: CONDITIONAL. REQUIRED if schema is not present, as defined in [SD-JWT-VC] Section 6.2.
       - **schema_uri#integrity**: CONDITIONAL. REQUIRED if schema_uri is present, as defined in *[SD-JWT-VC] Section 6.2.*
     - IT-Wallet Guidance Policy
   * - schema
     - **Object** containing information about the credential schema
     - IT-Wallet Guidance Policy
   * - schema_version
     - **Number** representing the version of the credential schema
     - IT-Wallet Guidance Policy
   * - user_attributes
     - **Object** containing the attributes of the credential, including the name and description of every attribute
     - IT-Wallet Guidance Policy

A non-normative example of Digital Credentials Catalogue is provided below.

.. literalinclude:: ../../examples/catalogue-example.json
  :language: JSON
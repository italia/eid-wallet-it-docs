.. include:: ../common/common_definitions.rst


Overview
--------

The template e-service functionality is employed to standardize data transmission from Authentic Sources to Credential Issuers.
The template e-service SHOULD be published within PDND by the Credential Issuer and is accessible through the PDND Template Catalogue.

Template Parameters
-------------------

The template e-service **MUST** adhere to the following specifications:

    - **Name**: IT Wallet - Authentic Source - <``Credential name``>
    - **Intended Recipients**: IT Wallet - Authentic Source - <``Authentic Source domain``>
    - **Description**: Provide the Credential Issuer with a new credential <``Credential name``>
    - **Technology**: REST
    - **Data variation via Signal Hub**: True
    - **Version changelog**: Authentic Source e-service via template implementation
    - **Voucher Time Limit**: 20
    - **Suggest custom threshold**: False
    - **Suggest manual agreement approval policy**: False
    - **Attributes**: <``Offcial name of the Credential Issuer Public Authority``>

Template Instantiation
----------------------

Each Authentic Source **SHOULD** instantiate the *IT Wallet - Authentic Source* template e-service in PDND.  
The instantiation process will result in a new e-service that **MUST** satisfy the following requirements:

    - **Signal Hub**: True
    - **Manual agreement approval policy**: False
    - **Daily API calls threshold for each provider**: greater than 10000
    - **Daily API calls threshold**: greater than 10000

Additional information required during the creation process is provider-dependent.

Authentic Source PDND OpenAPI Specification
---------------------------------------------

Below is the complete Open API Specification for the Authentic Source PDND e-services:

.. literalinclude:: ./oas3/OAS3-PDND-AS.yaml
    :language: yaml
    :linenos:

.. include:: ../common/common_definitions.rst
.. include:: ../common/symbols.rst

OID FED Trust Artifacts
-----------------------

This section defines the required trust artifacts and their conceptual roles in OpenID Federation 1.0 as for `OID-FED`_,  including :ref:`infrastructure-trust:Federation API Endpoints`, :ref:`infrastructure-trust:Entity Configuration`  and :ref:`infrastructure-trust:Subordinate Statements`, and :ref:`infrastructure-trust:Trust Marks`.

.. warning::

    TODO: chiarire relazione ruoli Wallet Providers, WRPs, Trust Anchors and Federation Intermediaries.. con Federation Entity 
    e dettagliare quali entità invece non lo sono (es Authentic Source, Schema Provider...)
    + capire se introdurre nome diverso per Trust Anchor e Federation Intermediaries -> Federation Authorities / Registration Body? VS  Leaves
    + come rientrano Trust Mark issuer
    + mettere nota che chiarisce cosa sono Federation intermediaries vs RP Intermediaries
    + decidere nome Federation Intermediates?

Federation API Endpoints
^^^^^^^^^^^^^^^^^^^^^^^^

OpenID Federation 1.0 uses RESTful Web Services secured over HTTPs. 
All the endpoints listed below are defined in the `OID-FED`_ specs.

Wallet Providers, WRPs, Trust Anchors and Federation Intermediaries MUST make publicly available the following endpoint.

.. list-table::
   :class: longtable
   :widths: 20 20 20
   :header-rows: 1

   * - Endpoint Name
     - HTTP Request
     - Scope
   * - federation metadata
     - **GET** .well-known/openid-federation
     - Metadata that an Entity publishes about itself, verifiable with a trusted third party (Superior Entity). It's called Entity Configuration.
 
Only Trust Anchors and Federation Intermediaries MUST additionally make publicly available the following endpoints.

.. warning::
    6.14.4. Federation Subordinate Events Endpoint da capire dove e se inserire questi dettagli / veniva fatto rimando in subordinate events: See the section Federation Subordinate Events Endpoint for more details.

.. list-table::
   :class: longtable
   :widths: 20 20 20
   :header-rows: 1

   * - Endpoint Name
     - HTTP Request
     - Scope
   * - subordinate list endpoint
     - **GET** /list
     - Lists the Subordinates. See `OID-FED`_ Section 8.2
   * - fetch endpoint
     - **GET** /federation_fetch_endpoint?sub=https://rp.example.org
     - Returns a signed JWT about a specific subject, its Subordinate. It's called Subordinate Statement. See `OID-FED`_ Section 8.1
   * - trust mark status
     - **POST** /trust_mark_status
     - Returns the status of the issuance (validity) of a Trust Mark related to a specific subject. See `OID-FED`_ Section 8.4
   * - trust mark list
     - **GET** /trust_mark_listing?trust_mark_type=...
     - Lists all entities for which Trust Marks have been issued and are still valid. See `OID-FED`_ Section 8.5
   * - trust mark
     - **GET** /trust_mark?trust_mark_type=...
     - Returns the Trust Mark related to a specific subject. See `OID-FED`_ Section 8.6
   * - historical keys
     - **GET** /federation_historical_keys
     - Lists the expired and revoked keys, with the motivation of the revocation. See `OID-FED`_ Section 8.7
   * - subordinate events
     - **GET** /federation_subordinate_events_endpoint?sub=https://rp.example.org
     - Returns a historical track of registration events about Immediate Subordinates, such as registration, revocation, and updates of their Federation Entity Keys. 

All the responses of the federation endpoints are in the form of signed JWT, with the exception of the Subordinate Listing endpoint and the Trust Mark Status endpoint that are served as plain JSON by default. 
The Federation Subordinate Events Endpoint also returns signed JWTs with the content type ``application/entity-events-statement+jwt``.


Entity Configuration
^^^^^^^^^^^^^^^^^^^^

The Entity Configuration is the verifiable document that each Federation Entity MUST publish on its own behalf, in the **.well-known/openid-federation** endpoint.

The Entity Configuration HTTP Response MUST set the media type to `application/entity-statement+jwt`.

The Entity Configuration MUST be cryptographically signed. The public part of this key MUST be provided in the Entity Configuration and within the Subordinate Statement issued by a immediate superior and related to its subordinate Federation Entity.

The Entity Configuration MAY also contain one or more Trust Marks.

**Role in Onboarding**: New entities publish their Entity Configuration as part of their registration process, declaring their capabilities, supported protocols, and compliance status to the federation. The configuration serves as the entity's initial declaration of its technical readiness and operational scope, enabling other participants to discover and validate its registration status.

.. warning::
    lascierei questo dettaglio anche qui, va poi ripreso in on-boarding per tutte le entità (anche EUDIW) in quanto meccanismo utilizzato per condividere WRP data e configurazioni

**Role in Operations**: During Credential operations, Entity Configurations are retrieved by Wallets, Credential Issuers, and Relying Parties to verify the current operational status, supported capabilities, and compliance attestations of other entities. This enables dynamic discovery of service endpoints, cryptographic keys, and protocol versions required for secure Credential exchange.

Technical details about Entity Configuration of Wallet Provider, Credential Issuer and Relying Party are given in Section :ref:`wallet-provider-entity-configuration:Wallet Provider Entity Configuration`, :ref:`credential-issuer-entity-configuration:Credential Issuer Entity Configuration` and :ref:`relying-party-entity-configuration:Relying Party Entity Configuration` respectively.

.. note::
  **Entity Configuration Signature**

  All the signature-check operations regarding the Entity Configurations, Subordinate Statements and Trust Marks, are carried out with the Federation public keys. For the supported algorithms refer to Section :ref:`algorithms:Cryptographic Algorithms`.

Entity Configurations Common Parameters
"""""""""""""""""""""""""""""""""""""""

The Entity Configurations of all the participants in the federation MUST have in common the parameters listed below.

.. list-table::
   :class: longtable
   :widths: 20 60
   :header-rows: 1

   * - **Claim**
     - **Description**
   * - **iss**
     - String. Identifier of the issuing Entity.
   * - **sub**
     - String. Identifier of the Entity to which it is referred. It MUST be equal to ``iss``.
   * - **iat**
     - UNIX Timestamp with the time of generation of the JWT, coded as NumericDate as indicated at :rfc:`7519`.
   * - **exp**
     - UNIX Timestamp with the expiry time of the JWT, coded as NumericDate as indicated at :rfc:`7519`.
   * - **jwks**
     - A JSON Web Key Set (JWKS) :rfc:`7517` that represents the public part of the signing keys of the Entity at issue. Each JWK in the JWK set MUST have a key ID (claim ``kid``) and MAY have a ``x5c`` parameter, as defined in :rfc:`7517`. It contains the Federation Entity Keys required for the operations of Trust Evaluation.

       **x5c**: The ``x5c`` parameter included in Entity Configuration's ``jwks`` parameter MUST only contain the self-issued X.509 Certificate about the corresponding ``jwk``.
   * - **metadata**
     - JSON Object. Each key of the JSON Object represents a metadata type identifier containing JSON Object representing the metadata, according to the metadata schema of that type. An Entity Configuration MAY contain more metadata statements, but only one for each type of metadata (<**entity_type**>). the metadata types are defined in the section `Metadata Types <Metadata Types>`_.


Entity Configuration Trust Anchor
"""""""""""""""""""""""""""""""""

The Trust Anchor Entity Configuration, in addition to the common parameters listed above, MUST use the following parameters:

.. list-table::
   :class: longtable
   :widths: 20 60
   :header-rows: 1

   * - **Claim**
     - **Description**
   * - **trust_mark_issuers**
     - JSON Array that defines which Federation authorities are considered trustworthy for issuing specific Trust Marks, assigned with their unique identifiers.


Entity Configuration Leaves and Federation Intermediates
""""""""""""""""""""""""""""""""""""""""""""""""""""""""

In addition to the previously defined claims, the Entity Configuration of the Leaves and of the Federation Intermediate Entities MUST use the following parameters:

.. list-table::
   :class: longtable
   :widths: 20 60
   :header-rows: 1

   * - **Claim**
     - **Description**
   * - **authority_hints**
     - Array of URLs (String). It contains a list of URLs of the immediate superior entities, such as the Trust Anchor or an Intermediate, that issues an Subordinate Statement related to this subject.
   * - **trust_marks**
     - A JSON Array containing the Trust Marks.


Entity Type Identifiers and Metadata
""""""""""""""""""""""""""""""""""""

In this section are defined the main Entity Type Identifiers mapped to the roles of the ecosystem, giving the references of the metadata protocol for each of these.

.. note::
  The entries that don't have any reference to a known draft or standard are intended to be defined in this technical reference.

.. list-table::
   :class: longtable
   :widths: 20 20 60
   :header-rows: 1

   * - Entity
     - Metadata Type
     - References
   * - Trust Anchor
     - ``federation_entity``
     - `OID-FED`_
   * - Federation Intermediate
     - ``federation_entity``
     - `OID-FED`_
   * - Wallet Provider
     - ``federation_entity``, ``wallet_solution``
     - --
   * - Credential Issuer
     - ``federation_entity``, ``openid_credential_issuer``, [``oauth_authorization_server``]
     - `OPENID4VCI`_
   * - Relying Party
     - ``federation_entity``, ``openid_credential_verifier``
     - `OID-FED`_, `OpenID4VP`_
   * - Relying Party Intermediary
     - ``federation_entity``, ``openid_credential_verifier``
     - `OID-FED`_, `OpenID4VP`_

.. warning::
    TO CHEKC: ho cambiato modificato questa tabella. Rimosso OpenID Entity / EUDI Entity e introdotto Relying Party Intermediary

.. note::
  In instances where a PID/EAA Provider implements both the Credential Issuer and the Authorization Server, it MUST incorporate both ``oauth_authorization_server`` and ``openid_credential_issuer`` within its metadata types.
  Other implementations may divide the Credential Issuer from the Authorization Server, when this happens the Credential Issuer metadata MUST contain the `authorization_servers` parameters, including the Authorization Server unique identifier.
  Furthermore, should there be a necessity for User Authentication by the Credential Issuer, it could be necessary to include the relevant metadata type, either ``openid_relying_party`` or ``openid_credential_verifier``.

The *federation_entity* metadata for Leaves contain the following claims.

.. list-table::
  :class: longtable
  :widths: 20 60
  :header-rows: 1

  * - **Claim**
    - **Description**
  * - **organization_name**
    - REQUIRED. See `OID-FED`_ Section 5.2.2
  * - **homepage_uri**
    - REQUIRED. See `OID-FED`_ Section 5.2.2
  * - **policy_uri**
    - REQUIRED. See `OID-FED`_ Section 5.2.2
  * - **logo_uri**
    - REQUIRED. URL of the entity's logo; it MUST be in SVG format. See `OID-FED`_ Section 5.2.2
  * - **contacts**
    - REQUIRED. Institutional verified email address (PEC) of the entity. See `OID-FED`_ Section 5.2.2
  * - **federation_resolve_endpoint**
    - OPTIONAL. See `OID-FED`_ Section 8.3
  * - **tos_uri**
    - OPTIONAL. URL string that points to a human-readable terms of service document for the client that describes a contractual relationship between the end-user and the client that the end-user accepts when authorizing the client. See `OID-FED`_.

Metadata about Wallet Provider, Credential Issuer and Relying Party are given in Section :ref:`wallet-solution-metadata:Wallet Solution Metadata`, :ref:`credential-issuer-solution:Credential Issuer Metadata` and :ref:`relying-party-metadata:Relying Party Metadata` respectively.

Subordinate Statements
^^^^^^^^^^^^^^^^^^^^^^

Trust Anchors and Federation Intermediates publish Subordinate Statements related to their immediate Subordinates.
The Subordinate Statement MAY contain a metadata policy and the Trust Marks related to a Subordinate.

The metadata policy, when applied, makes one or more changes to the final metadata of the Leaf. The final metadata of a Leaf is derived from the Trust Chain that contains all the statements, starting from the Entity Configuration up to the Subordinate Statement issued by the Trust Anchor.

Trust Anchors and Federation Intermediates MUST expose the Federation Fetch endpoint, where the Subordinate Statements are requested to validate the Leaf's Entity Configuration signature.

.. note::
  The Federation Fetch endpoint MAY also publish X.509 Certificates for each of the public keys of the Subordinate. Making the distribution of the issued X.509 Certificates via a RESTful service.

**Role in Onboarding**: During entity registration, Trust Anchors and Federation Intermediates issue Subordinate Statements to formally attest the registration and capabilities of new entities. These statements establish the hierarchical trust relationship and apply any required metadata policies that constrain or enhance the entity's declared capabilities based on federation policies.

.. warning::
   TO CHECK: 
   
   1. questo avviene solo se entity ha scelto national boundary, giusto? se solo EUDIW non serve. Se cosi' specificarlo qui e dopo nella procedura di onboarding

   2. constraints e required? se sì allora va messo nell'esempio

**Role in Operations**: During Credential operations, Subordinate Statements are retrieved to validate Trust Chains and apply current metadata policies. They enable real-time verification of an entity's registration status and ensure that operational capabilities comply with federation-wide policies and the entity's authorized scope.


The Subordinate Statement issued by Trust Anchors and Intermediates contains the following attributes:

.. list-table::
   :class: longtable
   :widths: 20 60
   :header-rows: 1

   * - **Claim**
     - **Description**
   * - **iss**
     - REQUIRED. See `OID-FED`_ Section 3 for further details.
   * - **sub**
     - REQUIRED. See `OID-FED`_ Section 3 for further details.
   * - **iat**
     - REQUIRED. See `OID-FED`_ Section 3 for further details.
   * - **exp**
     - REQUIRED. See `OID-FED`_ Section 3 for further details.
   * - **jwks**
     - REQUIRED. Federation JWKS of the *sub* entity. See `OID-FED`_ Section 3 for further details.
   * - **metadata_policy**
     - OPTIONAL. JSON Object that describes the Metadata policy. Each key of the JSON Object represents an identifier of the metadata type and each value MUST be a JSON Object that represents the metadata policy according to that metadata type. Please refer to the `OID-FED`_ specifications, Section 6.1, for the implementation details.
   * - **trust_marks**
     - OPTIONAL. JSON Array containing the Trust Marks issued by itself for the subordinate subject.
   * - **constraints**
     - REQUIRED. It MAY contain the **allowed_leaf_entity_types**, that restricts what types of metadata the subject is allowed to publish. It MAY contain the maximum number of Intermediates allowed between a itself and the Leaf (**max_path_length**)

.. note::
  **Subordinate Statement Signature**

  The same considerations and requirements made for the Entity Configuration and in relation to the signature mechanisms MUST be applied for the Subordinate Statements.


Below there is a non-normative example of an Subordinate Statement issued by a Trust Anchor or its Federation Intermediate in relation to one of its Subordinates.

.. code-block:: json

    {
        "alg": "ES256",
        "kid": "em3cmnZgHIYFsQ090N6B3Op7LAAqj8rghMhxGmJstqg",
        "typ": "entity-statement+jwt"
    }

.. code-block:: json

    {
        "exp": 1649623546,
        "iat": 1649450746,
        "iss": "https://intermediate.example.org",
        "sub": "https://rp.example.it",
        "jwks": {
            "keys": [ // keys about the Subordinate
                {
                    "kty": "EC",
                    "kid": "2HnoFS3YnC9tjiCaivhWLVUJ3AxwGGz_98uRFaqMEEs",
                    "crv": "P-256",
                    "x": "1kNR9Ar3MzMokYTY8BRvRIue85NIXrYX4XD3K4JW7vI",
                    "y": "slT14644zbYXYF-xmw7aPdlbMuw3T1URwI4nafMtKrY",
                    "x5c": [ 
                      // <X.509 certificate about the Subordinate>
                      ]
                }
            ]
        },
        "metadata_policy": {
            "openid_credential_verifier": {
                "scope": {
                    "subset_of": [
                         "eu.europa.ec.eudiw.pid.1",
                         "given_name",
                         "family_name",
                         "email"
                      ]
                },
                "vp_formats": {
                    "dc+sd-jwt": {
                        "sd-jwt_alg_values": [
                            "ES256",
                            "ES384"
                        ],
                        "kb-jwt_alg_values": [
                            "ES256",
                            "ES384"
                        ]
                    }
                }
            }
         }
    }



Trust Marks
^^^^^^^^^^^

As a result of a successful onboarding completion, entities receive IT-Wallet Federation Trust Marks. Trust Marks are issued by the Federation Authority (Trust Anchor for direct onboarding, Intermediate for mediated onboarding) through the Federation Trust Mark Endpoint and serve as verifiable attestations about compliance with IT-Wallet technical profiles and or authorization policies.

Trust Mark Types and Schema
"""""""""""""""""""""""""""

Entities MAY receive multiple Trust Marks for different purposes. Trust Mark identifiers MUST follow a hierarchical schema that reflects the authorization scope:

``https://<federation_authority_domain>/trust_marks/<purpose>/<entity_type>``

Where:

  - ``<federation_authority_domain>``: The domain of the issuing Federation Authority.
  - ``<purpose>``: The Trust Mark purpose. The ``federation-entity`` purpose is **REQUIRED** for all entities. Additional Trust Mark purposes MAY be supported, such as ``authorization_policy`` for granular operational scope definitions.
  - ``<entity_type>``: The recipient entity type (e.g., ``credential-issuer``, ``relying-party``, ``wallet-provider``).

Trust Mark Structure
""""""""""""""""""""

Trust Marks in Entity Configuration MUST be represented as JSON objects containing the following claims:

.. list-table:: Trust Mark Object Claims (in Entity Configuration)
   :class: longtable
   :header-rows: 1
   :widths: 20 80

   * - **Claim**
     - **Description**
   * - **trust_mark_type**
     - REQUIRED. Identifier for the type of Trust Mark following the schema: ``https://<federation_authority_domain>/trust_marks/<purpose>/<entity_type>``.
   * - **trust_mark**
     - REQUIRED. A signed JSON Web Token representing the Trust Mark issued by the Federation Authority.

The Trust Mark JWT (contained in the ``trust_mark`` claim above) includes the following claims:

.. warning::
    DA CAPIRE 
    
    1. se allinearlo con campi di WRPRC

    2. nell'esempio ci sono anche claim "authorized_claims", "authorized_credential_types", "scope_restrictions" che nono sono descritte in tabella


.. list-table:: Trust Mark JWT Claims
   :class: longtable
   :header-rows: 1
   :widths: 20 80

   * - **Claim**
     - **Description**
   * - **iss**
     - REQUIRED. Federation Authority issuing the Trust Mark (immediate superior: Trust Anchor or Intermediate).
   * - **sub**
     - REQUIRED. Federation Entity Identifier of the subject.
   * - **trust_mark_type**
     - REQUIRED. Unique Trust Mark identifier, MUST match the ``trust_mark_type`` claim.
   * - **iat**
     - REQUIRED. Trust Mark issuance timestamp.
   * - **exp**
     - REQUIRED. Trust Mark expiration timestamp.
   * - **organization_type**
     - REQUIRED. Entity organization type (``public`` or ``private``).
   * - **vat_number**
     - RECOMMENDED. VAT number of the entity (typically for private organizations).
   * - **legal_identifier**
     - RECOMMENDED. Legal registration number or identifier of the entity (e.g., business registration number, tax code).
   * - **ipa_code**
     - RECOMMENDED. IPA (Indice delle Pubbliche Amministrazioni) code for public sector entities.
   * - **organization_name**
     - RECOMMENDED. Full name of the Organizational Entity.
   * - **email**
     - RECOMMENDED. Institutional or PEC email of the organization.
   * - **logo_uri**
     - REQUIRED. URL pointing to the :ref:`brand-identity:Trust Mark` for UI/UX purposes.
   * - **ref**
     - OPTIONAL. URL with additional web information about the Trust Mark.

The following non-normative examples illustrate different Trust Mark JWT contents for federation membership and different authorization policies:

.. code-block:: json

   {
     "iss": "https://trust-anchor.eid-wallet.example.it",
     "sub": "https://ci.public-authority.gov.example",
     "trust_mark_type": "https://trust-anchor.eid-wallet.example.it/trust_marks/federation-entity/credential-issuer",
     "iat": 1718207217,
     "exp": 1749743216,
     "organization_type": "public",
     "ipa_code": "pub_001",
     "legal_identifier": "12345678901",
     "organization_name": "Public Authority Services",
     "email": "registry@public-authority.gov.example"
   }

.. code-block:: json

   {
     "iss": "https://trust-anchor.eid-wallet.example.it",
     "sub": "https://rental.cars.example.com",
     "trust_mark_type": "https://trust-anchor.eid-wallet.example.it/trust_marks/authorization_policy/relying-party",
     "iat": 1718207217,
     "exp": 1749743216,
     "organization_type": "private",
     "vat_number": "IT12345678901",
     "legal_identifier": "12345678901",
     "organization_name": "Premium Car Rental Services Ltd",
     "email": "compliance@rental.cars.example.com",
     "authorized_claims": ["given_name", "family_name", "driving_privileges"],
     "authorized_credential_types": ["mobile-driving-license"],
     "scope_restrictions": {
       "domains": ["MOBILITY_TRAVEL"],
       "purposes": ["DRIVING_RIGHTS_VERIFICATION"]
     }
   }

.. code-block:: json

   {
     "iss": "https://trust-anchor.eid-wallet.example.it",
     "sub": "https://private-badge.ci.example.com",
     "trust_mark_type": "https://trust-anchor.eid-wallet.example.it/trust_marks/authorization_policy/credential-issuer",
     "iat": 1718207217,
     "exp": 1749743216,
     "organization_type": "private",
     "vat_number": "IT98765432101",
     "legal_identifier": "98765432101",
     "organization_name": "Badge Services Ltd",
     "email": "compliance@rprivate-badge.ci.example.com",
     "authorized_claims": ["given_name", "family_name", "company_id"],
     "authorized_credential_types": ["example-company-badge"],
     "scope_restrictions": {
       "domains": ["EMPLOYMENT"],
       "purposes": ["ACCESS_PERMIT"]
     }
   }

Federation Entities MUST integrate Trust Marks in their Entity Configuration using the ``trust_marks`` claim as specified in :ref:`infrastructure-trust:Entity Configuration Leaves and Federation Intermediates`. 
Entities MAY receive multiple Trust Marks for different authorization scopes.

.. code-block:: json

   {
     "iss": "https://credentials.example.gov",
     "sub": "https://credentials.example.gov",
     "jwks": { 
      // jwks content
     },
     "authority_hints": ["https://trust-anchor.eid-wallet.example.it"],
     "trust_marks": [
       {
         "trust_mark_type": "https://trust-anchor.eid-wallet.example.it/trust_marks/federation-entity/credential-issuer",
         "trust_mark": "eyJhbGciOiJFUzI1NiIsImtpZCI6IlRydXN0QW5jaG9yS2V5SWQiLCJ0eXAiOiJKV1QifQ..."
       }
     ],
     "metadata": { 
      // Metadata content
     }
   }


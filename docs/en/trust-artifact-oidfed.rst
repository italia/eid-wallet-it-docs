.. include:: ../common/common_definitions.rst
.. include:: ../common/symbols.rst

OID FED Trust Artifacts
-----------------------

This section defines the required trust artifacts and their conceptual roles in OpenID Federation 1.0 as for `OID-FED`_,  including 

- :ref:`infrastructure-trust:Federation API Endpoints`;
- :ref:`infrastructure-trust:Entity Configuration`;
- :ref:`infrastructure-trust:Subordinate Statements`;
- :ref:`infrastructure-trust:Trust Marks`.

Before entering into the details, Figure :ref:`fig_OID-FED_roles` maps each wallet ecosystem entity onto the corresponding OpenID Federation role the entity plays: WRPs and Wallet Providers are Federation Entities that MUST be registered by a Federation Authority (a Trust Anchor or an Intermediate). The registration process establishes the participant's position in the trust hierarchy (as Leaf Entities, i.e entities with no Subordinate Entities)  and enables them to participate in credential operations as they proved their eligibility and received authorization to perform their designated functions. 

In the IT Wallet ecosystem, both Trust Anchor and Intermediates play the role of Trust Mark Issuer.

.. _fig_OID-FED_roles:
.. plantuml:: plantuml/oid-fed-roles.puml
    :width: 70%
    :alt: The roles within the Federation, where the Trust Anchor oversees its subordinates, which include one or more Intermediates and Leaves.
    :caption: `OID-FED Roles <https://www.plantuml.com/plantuml/svg/ROv1IyD044Rl-ol6UWvIBUf1IaDgGF1GHF0eq-maBjtCXjdPXYB-TsiY9HLlE-pxU6yL5KLJwys5uyedI_1GBAwAnNiHMD4noTAOk7FSeM0BMwnsZOJ4jWW-2AWWnmw5M2TKBXBw4TZwuy8O8rGfSkC9PYLP4bGN6FAa7q6SEeepm0WrdhHmMT-KT-ivV1g0oVfLKbJ8kJeEXuqYd1DFh2GjMOTA0-5Ovs2-pYAU2VU_KazOnudtyRwyNj_-zRwXzwImaR1tbaPrty5_KFP2_k2uWGsA7aPIkg70_3oor6NBeMfoAfgXytJran-p8hQfzTy0>`_

.. note:: 
  Wallet Instances are not Federation Entities as they are End-User's personal devices authenticated by their Wallet Provider. 


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

Trust Mark identifiers MUST follow a hierarchical schema that reflects the authorization scope:

``https://<federation_authority_domain>/trust_marks/<purpose>/<entity_type>``

Where:

  - ``<federation_authority_domain>``: The domain of the issuing Federation Authority.
  - ``<purpose>``: The Trust Mark purpose. The ``registration-entity`` purpose is **REQUIRED** for all entities as a result of the onboarding process. Additional Trust Mark purposes MAY be defined for future needs, but they are not required for the authorization processes defined in :ref:`trust-evaluation-oidfed:Authorization`.
  - ``<entity_type>``: The Entity Type Identifier of the subject, among those defined in :ref:`trust-artifact-oidfed:Entity Type Identifiers and Metadata` (for example ``openid_credential_issuer`` or ``openid_credential_verifier``), and ``intermediate`` for a Relying Party Intermediary.

Trust Mark registration-entity
"""""""""""""""""""""""""""""""

Within IT-Wallet the ``registration-entity`` Trust Mark is the registration Trust Mark of an entity. The only Trust MArk issuer MUST be the Federation TA. It attests the registration and carries the authorization data of the entity, that is its entitlements and, where applicable, the Credentials and the attributes it is authorized to issue or to request. This registration Trust Mark is the functional analogue of the Wallet-Relying Party Registration Certificate (WRPRC) of the EUDIW Trust Framework. An entity receives one registration Trust Mark for each role it holds, with the ``<entity_type>`` component of the identifier set accordingly. 

A Relying Party Intermediary receives its registration Trust Mark with the ``intermediate`` ``<entity_type>`` in the identifier. Differently from the EUDIW Trust Framework, where the intermediary relationship is expressed in the registration data of the intermediated Relying Party, in the National Trust Framework the relationship is expressed through the federation hierarchy as the Intermediary is a Federation Intermediate that publishes the Subordinate Statements of its affiliated Relying Parties, and each affiliated Relying Party sets its ``authority_hints`` to the Intermediary. The registration Trust Mark of each affiliated Relying Party is also issued by the Federation Trust Anchor. For this reason no dedicated intermediary field is present in the Trust Mark. The onboarding of the Intermediary is defined in :ref:`onboarding-procedure:Relying Party Intermediaries`.

**Trust Mark Structure**

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

.. list-table:: Trust Mark JWT Claims
   :class: longtable
   :header-rows: 1
   :widths: 22 78

   * - **Claim**
     - **Description**
   * - **iss**
     - REQUIRED. The Federation Trust Anchor that issues the Trust Mark.
   * - **sub**
     - REQUIRED. Federation Entity Identifier of the subject.
   * - **trust_mark_type**
     - REQUIRED. Unique Trust Mark identifier. It MUST match the ``trust_mark_type`` claim of the Trust Mark Object.
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
   * - **entitlements**
     - REQUIRED. Array of entitlement URIs identifying the role of the subject, as defined in `ETSI_TS_119_475`_ Annex A.2 (e.g. ``Service_Provider``, ``PID_Provider``, ``QEAA_Provider``, ``PUB_EAA_Provider``, ``Non_Q_EAA_Provider``).
   * - **provides_attestations**
     - REQUIRED for a Credential Issuer, MUST NOT be present otherwise. Array of the Credential types the subject is authorized to issue. Each entry contains ``format``, ``meta`` to identify the Credential type, and an optional ``claim`` array.
   * - **credentials**
     - REQUIRED for a Relying Party that requests Credentials, MUST NOT be present otherwise. Array of the Credential queries the subject is authorized to request, used for the Overasking Check. Each entry contains ``format``, ``meta`` (e.g. ``vct_values`` or ``doctype_value``) and a ``claim`` array of the authorized attribute paths.
   * - **purpose**
     - REQUIRED for a Relying Party that requests Credentials, MUST NOT be present otherwise. Multilingual list describing the data processing associated with the intended use. Each entry contains ``lang`` and ``value``.
   * - **privacy_policy**
     - REQUIRED for a Relying Party that requests Credentials, MUST NOT be present otherwise. URL of the subject privacy policy.
   * - **supervisory_authority**
     - REQUIRED. Data Protection Authority information, with ``uri``, ``email`` and ``phone``.
   * - **logo_uri**
     - REQUIRED. URL pointing to the :ref:`brand-identity:Trust Mark` for UI/UX purposes.
   * - **ref**
     - OPTIONAL. URL with additional web information about the Trust Mark.

.. note::
  The claims that carry the authorization data (``entitlements``, ``provides_attestations``, ``credentials``, ``purpose``, ``privacy_policy``, ``supervisory_authority``) are defined in analogy with the EUDIW Wallet-Relying Party Registration Certificate (`ETSI_TS_119_475`_), so that a Trust Evaluator can reuse the same authorization logic for both artifacts. The identity and branding claims are specific to the IT-Wallet federation.

.. note::
  The revocation status of a Trust Mark is verified through the Federation Trust Mark Status endpoint (`OID-FED`_ Section 8.4), not through a status list carried in the token. This is the difference with the WRPRC, whose ``status`` claim points to a status list: the Trust Mark relies on the federation native revocation mechanism. The consumption of these claims by the Trust Evaluator is defined in :ref:`trust-evaluation-oidfed:Authorization`.

The following non-normative examples illustrate the registration Trust Mark JWT content for a Credential Issuer, a public non-qualified EAA Provider issuing an Employee Badge, for a Relying Party requesting that Employee Badge, and for a Relying Party Intermediary.

Credential Issuer, a public non-qualified EAA Provider issuing the Employee Badge:

.. code-block:: json

   {
     "iss": "https://trust-anchor.eid-wallet.example.it",
     "sub": "https://badge-issuer.example.it",
     "trust_mark_type": "https://trust-anchor.eid-wallet.example.it/trust_marks/registration-entity/openid_credential_issuer",
     "iat": 1718207217,
     "exp": 1749743216,
     "organization_type": "public",
     "ipa_code": "c_h501",
     "legal_identifier": "80012345678",
     "organization_name": "Comune di Example",
     "email": "protocollo@comune.example.it",
     "entitlements": ["Non_Q_EAA_Provider"],
     "provides_attestations": [
       {
         "format": "dc+sd-jwt",
         "meta": {
           "vct_values": ["urn:it-wallet:badge:1"]
         },
         "claim": [
           {"path": ["document_number"]},
           {"path": ["works_for"]},
           {"path": ["given_name"]},
           {"path": ["family_name"]},
           {"path": ["job_title"]}
         ]
       }
     ],
     "logo_uri": "https://badge-issuer.example.it/logo.svg"
   }

Relying Party, a private organization requesting the Employee Badge for physical access control:

.. code-block:: json

   {
     "iss": "https://trust-anchor.eid-wallet.example.it",
     "sub": "https://access.privatecompany.example.com",
     "trust_mark_type": "https://trust-anchor.eid-wallet.example.it/trust_marks/registration-entity/openid_credential_verifier",
     "iat": 1718207217,
     "exp": 1749743216,
     "organization_type": "private",
     "vat_number": "IT12345678901",
     "legal_identifier": "12345678901",
     "organization_name": "Private Company S.p.A.",
     "email": "compliance@privatecompany.example.com",
     "entitlements": ["Service_Provider"],
     "credentials": [
       {
         "format": "dc+sd-jwt",
         "meta": {
           "vct_values": ["urn:it-wallet:badge:1"]
         },
         "claim": [
           {"path": ["given_name"]},
           {"path": ["family_name"]},
           {"path": ["works_for"]},
           {"path": ["job_title"]}
         ]
       }
     ],
     "purpose": [
       {"lang": "en", "value": "Employee verification for physical access control"},
       {"lang": "it", "value": "Verifica del dipendente per il controllo dell'accesso fisico"}
     ],
     "privacy_policy": "https://access.privatecompany.example.com/privacy",
     "supervisory_authority": {
       "uri": "https://www.dpa.example.it/report",
       "email": "reports@dpa.example.it",
       "phone": "+390612345678"
     },
     "logo_uri": "https://access.privatecompany.example.com/logo.svg"
   }

Relying Party Intermediary. It declares no intended use of its own, so its registration Trust Mark carries no ``credentials`` and no ``purpose``. It is a Federation Intermediate, and its affiliated Relying Parties set their ``authority_hints`` to it.

.. code-block:: json

   {
     "iss": "https://trust-anchor.eid-wallet.example.it",
     "sub": "https://intermediary.example.com",
     "trust_mark_type": "https://trust-anchor.eid-wallet.example.it/trust_marks/registration-entity/openid_credential_verifier",
     "iat": 1718207217,
     "exp": 1749743216,
     "organization_type": "private",
     "vat_number": "IT98765432109",
     "legal_identifier": "98765432109",
     "organization_name": "Intermediary S.r.l.",
     "email": "info@intermediary.example.com",
     "entitlements": ["Service_Provider"],
     "logo_uri": "https://intermediary.example.com/logo.svg"
   }


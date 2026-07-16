.. include:: ../common/common_definitions.rst

OID-FED Trust Artifacts
-----------------------

This section defines the trust artifacts of the National Trust Framework that are defined in the following specifications of the OpenID Federation family, each within its own scope:

- OpenID Federation 1.0 (`OID-FED`_), the core framework. It defines the main artifacts including the Entity Statements, the federation endpoints and the Trust Marks.
- OpenID Federation for Wallet Architectures, the wallet profile of OpenID Federation. It defines the Entity Type Identifiers of the Entities used in this section.
- OpenID Federation Subordinate Events, that defines the Subordinate Events endpoint, used to obtain the registration history of an Immediate Subordinate.

Figure :ref:`fig_OID-FED_roles` maps each wallet ecosystem entity onto the OpenID Federation role it plays. Wallet-Relying Parties and Wallet Providers are Federation Entities that MUST be registered by a Federation Authority, that is a Federation TA or Intermediate.

.. _fig_OID-FED_roles:
.. plantuml:: plantuml/oid-fed-roles.puml
    :width: 70%
    :alt: The roles within the Federation, where the Trust Anchor oversees its subordinates, which include one or more Intermediates and Leaves.
    :caption: `OID-FED Roles <https://www.plantuml.com/plantuml/svg/ROv1IyD044Rl-ol6UWvIBUf1IaDgGF1GHF0eq-maBjtCXjdPXYB-TsiY9HLlE-pxU6yL5KLJwys5uyedI_1GBAwAnNiHMD4noTAOk7FSeM0BMwnsZOJ4jWW-2AWWnmw5M2TKBXBw4TZwuy8O8rGfSkC9PYLP4bGN6FAa7q6SEeepm0WrdhHmMT-KT-ivV1g0oVfLKbJ8kJeEXuqYd1DFh2GjMOTA0-5Ovs2-pYAU2VU_KazOnudtyRwyNj_-zRwXzwImaR1tbaPrty5_KFP2_k2uWGsA7aPIkg70_3oor6NBeMfoAfgXytJran-p8hQfzTy0>`_

.. note::
  Wallet Instances are not Federation Entities, they are the End-User personal devices authenticated by their Wallet Provider.


Federation API Endpoints
^^^^^^^^^^^^^^^^^^^^^^^^^

OpenID Federation 1.0 uses RESTful web services secured over HTTPS. All Federation Entities MUST publish their own **Entity Configuration** at the ``.well-known/openid-federation`` endpoint according to `OID-FED`_ Section 9. Federation TA and Intermediates additionally expose the federation endpoints used to build and validate the Trust Chains and to support the Trust Marks.

The Federation Entity properties supported in the IT-Wallet specification profile are defined in `OID-FED`_ Section 5.1.1. The table below lists the federation endpoints, the Entity Types that MUST expose each of them, the request parameters used within IT-Wallet with their REQUIRED or OPTIONAL status, and the response returned by each endpoint. The request parameters follow `OID-FED`_ Section 8: they are sent as query parameters for GET requests and in the body for POST requests. The responses follow the OID-FED response formats referenced in the table.

.. list-table::
   :class: longtable
   :widths: 26 36 38
   :header-rows: 1

   * - Endpoint
     - Request parameters
     - Response
   * - **fetch** (``/fetch``). REQUIRED for Federation TA and Intermediates.
     - **GET**. ``sub`` REQUIRED.
     - The requested Subordinate Statement, as a signed JWT (``application/entity-statement+jwt``). `OID-FED`_ Section 8.1.2
   * - **list** (``/list``). REQUIRED for Federation TA and Intermediates.
     - **GET**. ``entity_type``, ``trust_marked``, ``trust_mark_type`` and ``intermediate``, all OPTIONAL.
     - A JSON array of the Entity Identifiers of the Immediate Subordinates (``application/json``). `OID-FED`_ Section 8.2.2
   * - **resolve** (``/resolve``). REQUIRED for Federation TA and Intermediates.
     - **GET**. ``sub`` and ``trust_anchor`` REQUIRED, ``entity_type`` OPTIONAL.
     - The Resolve Response with the Resolved Metadata, the Trust Chain and the verified Trust Marks, as a signed JWT (``application/resolve-response+jwt``). `OID-FED`_ Section 8.3.2
   * - **trust mark status** (``/trust_mark_status``). REQUIRED only for Federation TA.
     - **POST**. ``trust_mark`` REQUIRED.
     - The Trust Mark Status Response, that is the validity of the Trust Mark, as a signed JWT (``application/trust-mark-status-response+jwt``). `OID-FED`_ Section 8.4.2
   * - **trust mark list** (``/trust_mark_list``). REQUIRED only for Federation TA.
     - **GET**. ``trust_mark_type`` REQUIRED, ``sub`` OPTIONAL.
     - A JSON array of the Entity Identifiers for which the Trust Mark is issued and still valid (``application/json``). `OID-FED`_ Section 8.5.2
   * - **trust mark** (``/trust_mark``). REQUIRED only for Federation TA.
     - **GET**. ``trust_mark_type`` and ``sub`` REQUIRED.
     - The requested Trust Mark, as a signed JWT (``application/trust-mark+jwt``). `OID-FED`_ Section 8.6.2
   * - **historical keys** (``/historical_keys``). REQUIRED for Federation TA and Intermediates.
     - **GET**. No request parameters.
     - A signed JWK Set with the historical keys, as a signed JWT (``application/jwk-set+jwt``). `OID-FED`_ Section 8.7.2
   * - **subordinate events** (``/subordinate_events``). REQUIRED for Federation TA and OPTIONAL for Intermediates.
     - **GET**. ``sub`` REQUIRED.
     - A signed JWT with the history of the registration events. See the Subordinate Events specification Section 2.3.

The **Subordinate Events** (``/subordinate_events``) endpoint is defined in `OpenID Federation Subordinate Events <https://openid.net/specs/openid-federation-subordinate-events-1_0.html>`_. Its purpose is to give a verifiable, historical track of the registration events concerning an Immediate Subordinate, such as its registration, the update of its Federation Entity Keys and its revocation. For the request format, the response format and the event types refer to `OpenID Federation Subordinate Events <https://openid.net/specs/openid-federation-subordinate-events-1_0.html>`_ Section 2.2 and 2.3.

.. note::
  Within IT-Wallet the **resolve** (``/resolve``) endpoint MUST respond to unauthenticated requests only with cached information about Entities, if available, and the collection and assessment of a Trust Chain MUST NOT be the default action of the resolve endpoint, as described in `OID-FED`_ Section 18.1.

Entity Statements
^^^^^^^^^^^^^^^^^^^^^^^
The **Entity Configuration** is the Entity Statement that each Federation Entity issues about itself and publishes at the ``.well-known/openid-federation`` path (`OID-FED`_ Section 3). Its ``iss`` and ``sub`` are the Federation Entity Identifier of the Entity itself, and it is signed with a Federation Entity Key. The HTTP response sets the media type to ``application/entity-statement+jwt``. The Entity Configuration MAY also contain one or more Trust Marks.

A **Subordinate Statement** is the Entity Statement that a Trust Anchor or a Federation Intermediate issues about its Immediate Subordinate (`OID-FED`_ Section 3). Its ``iss`` is the issuer, its ``sub`` is the Subordinate, and it carries the Federation Entity Keys of the Subordinate, so it is the statement that binds the Subordinate keys under its superior. It MAY also carry a metadata policy and the Trust Marks about the Subordinate.

Entity Configuration
"""""""""""""""""""""""

In the IT-Wallet ecosystem the Entity Configuration is published during the onboarding of the Entity (see :ref:`onboarding-procedure:The Onboarding Processes`) and is retrieved and validated during the trust evaluation, as defined in :ref:`trust-evaluation-oidfed:Federation Entity Authentication` and :ref:`trust-evaluation-oidfed:Metadata Retrieval and Validation`.

Technical details about the Entity Configuration of Wallet Provider, Credential Issuer and Relying Party are given in Section :ref:`wallet-provider-entity-configuration:Wallet Provider Entity Configuration`, :ref:`credential-issuer-entity-configuration:Credential Issuer Entity Configuration` and :ref:`relying-party-entity-configuration:Relying Party Entity Configuration` respectively.

.. note::
  All the signature checks on the Entity Configurations, the Subordinate Statements and the Trust Marks are carried out with the Federation Entity Keys. For the supported algorithms refer to Section :ref:`algorithms:Cryptographic Algorithms`.

Subordinate Statements
"""""""""""""""""""""""

Trust Anchors and Federation Intermediates serve their Subordinate Statements through the **fetch** (``/fetch``) endpoint (`OID-FED`_ Section 8.1), where a Trust Evaluator retrieves them to validate the Entity Configuration signature of the Subordinate and to build the Trust Chain. The metadata policy, when present, changes the final metadata of the Leaf. The final metadata is derived from the whole Trust Chain, from the Entity Configuration up to the Subordinate Statement issued by the Trust Anchor, as defined in :ref:`trust-evaluation-oidfed:Metadata Retrieval and Validation`. The revocation of a Subordinate is expressed by the absence of a valid Subordinate Statement about it, as defined in :ref:`trust-evaluation-oidfed:Federation Trust Chain`.

Within IT-Wallet the Subordinate Statements are issued during the onboarding of the Subordinate (see :ref:`onboarding-procedure:The Onboarding Processes`).

Entity Statement Parameters
"""""""""""""""""""""""""""""""""""""""

In addition to the REQUIRED common parameters ``iss``, ``sub``, ``iat``, ``exp`` and ``jwks`` as defined in `OID-FED`_ Section 3.1.1, within IT-Wallet specification profile the following parameters apply.

In Entity Configuration (`OID-FED`_ Section 3.1.2):

- **metadata** (``metadata``): JSON Object where each key is a metadata type identifier and its value is the metadata of that type. All Entities MUST include at least one metadata for ``federation_entity`` in their Entity Configurations, and it MAY include more than one metadata statement, but only one for each metadata type. The metadata types are defined in :ref:`trust-artifact-oidfed:Entity Type Identifiers and Metadata`.
- **trust_marks** (``trust_marks``): REQUIRED for Leaves and Federation Intermediates. JSON Array of the Trust Marks of the subject. The registration Trust Mark is defined in :ref:`trust-artifact-oidfed:Trust Mark registration-entity`.
- **trust_mark_issuers** (``trust_mark_issuers``): REQUIRED only for Federation TA and MUST NOT be included otherwise. JSON Object that declares, for each Trust Mark type, the Federation Authorities that are trusted to issue it, given by their Federation Entity Identifiers. Within IT-Wallet the registration Trust Mark is issued only by the Federation Trust Anchor, so it MUST contain at least the Federation TA identifier.

In Subordinate Statement (`OID-FED`_ Section 3.1.3):

- **metadata_policy** (``metadata_policy``): OPTIONAL in `OID-FED`_. Metadata policy bound to a specific metadata type and applied to the subtree, resolved by combining the ``metadata_policy`` Claims along the Trust Chain, as defined in `OID-FED`_ Section 6.1.4. Within IT-Wallet the Subordinate Statement about a Leaf MUST carry a ``metadata_policy`` that binds the protocol metadata of the Leaf to the values approved at onboarding. Using the metadata policy operators of `OID-FED`_ Section 6.1.3, it MUST fix the protocol signature keys (``jwks``) and, when present in the metadata type, the service endpoints and the request, response and redirect URIs (for example the ``request_uris``, ``response_uris`` and ``redirect_uris`` of the ``openid_credential_verifier``). This Subordinate Statement is issued by the immediate superior that registered the Leaf, that is the Federation TA for the Leaves it registers directly and a Federation Intermediate for its affiliated Relying Parties. The Subordinate Statement about a Federation Intermediate does not carry a ``metadata_policy``, because the Intermediate has no protocol metadata and its affiliated Relying Parties are bound by the Intermediate itself. A superior MAY further restrict the metadata policy set by its own superiors, but MUST NOT relax it, as defined in `OID-FED`_ Section 6.1.1.
- **constraints** (``constraints``): REQUIRED only for Federation TA. It carries the constraints applied to the subtree below the issuer. It MUST contain ``allowed_entity_types``, that restricts the metadata Entity Types the Subordinates in the subtree are allowed to publish, and ``max_path_length``, that limits the number of Intermediates between the issuer and the Trust Chain subject. The ``federation_entity`` Entity Type is always allowed and MUST NOT be listed in ``allowed_entity_types``. See `OID-FED`_ Section 6.2.

All other optional parameters defined in `OID-FED`_ Section 3 that are not recognized within IT-Wallet specification profile MUST be ignored during the evaluation of an Entity Statement.

.. note::
  Within IT-Wallet the Federation Entity Keys carried in the ``jwks`` of an Entity Configuration or of a Subordinate Statement are used to sign the federation statements and are validated through the Federation Trust Chain, not through X.509. The X.509 signing PKI, whose certificates are used to sign the Attestations, is a separate trust relationship. The Signing Trust Anchors of this PKI are distributed in the Entity Configuration of the Federation Trust Anchor. Each one is provided in the ``x5c`` parameter (:rfc:`7517` Section 4.7) of a dedicated JWK within the ``jwks``, distinct from the Federation Entity Keys, which do not carry ``x5c``, as defined in :ref:`trust-evaluation-oidfed:Signing Trust Anchor Distribution`. The Document Signer certificates of the Credential Issuers are not carried in the ``jwks`` of the Entity Statements: they are included in the signed Attestations, in the ``x5chain`` header for the mdoc format and in the ``x5c`` header for the JOSE format, and are validated as defined in :ref:`trust-evaluation-oidfed:X.509 Certificate Chain Validation`. The issuance of these X.509 Certificates and the operation of the signing PKI are defined in the onboarding (see :ref:`onboarding-procedure:The Onboarding Processes`).

Entity Type Identifiers and Metadata
""""""""""""""""""""""""""""""""""""

The Entity Type Identifiers of the ecosystem roles are defined in OpenID Federation for Wallet Architectures, section Wallet Architecture Entity Types, which is the wallet profile of OpenID Federation. Each role declares in its Entity Configuration one or more metadata types, whose parameters follow the protocol specification of that metadata type. The table below maps the roles of the ecosystem to their Entity Type Identifiers and gives the reference of the metadata protocol for each of them.

.. warning::
  Within IT-Wallet the Wallet Provider metadata type MUST be ``wallet_solution``. This is a deviation from OpenID Federation for Wallet Architectures, that names the corresponding Entity Type Identifier ``openid_wallet_provider``.

.. list-table::
   :class: longtable
   :widths: 25 75
   :header-rows: 1

   * - Entity
     - Metadata Type
   * - Trust Anchor
     - ``federation_entity``
   * - Federation Intermediate
     - ``federation_entity``
   * - Wallet Provider
     - ``federation_entity``, ``wallet_solution``
   * - Credential Issuer
     - ``federation_entity``, ``openid_credential_issuer``, [``oauth_authorization_server``]
   * - Relying Party
     - ``federation_entity``, ``openid_credential_verifier``
   * - Relying Party Intermediary
     - ``federation_entity``

.. note::
  A Relying Party Intermediary is a Federation Intermediate. As an intermediary it is not involved in the protocol flows, so it does not publish a protocol metadata of its own, only the ``federation_entity`` metadata. It publishes the Subordinate Statements of its affiliated Relying Parties, and each affiliated Relying Party sets its ``authority_hints`` to the Intermediary. Its registration Trust Mark uses the ``intermediate`` Entity Type Identifier in the Trust Mark type, as defined in :ref:`trust-artifact-oidfed:Trust Mark Types and Schema`.

.. note::
  When a PID or EAA Provider implements both the Credential Issuer and the Authorization Server within the same Entity, it MUST include both ``openid_credential_issuer`` and ``oauth_authorization_server`` in its metadata types. When the Authorization Server is a separate Entity, the Credential Issuer metadata MUST contain the ``authorization_servers`` parameter with the identifier of the Authorization Server. According to `OPENID4VCI`_ the Authorization Server MAY be external to the Entity that implements the Credential Endpoint, therefore the use of ``oauth_authorization_server`` is OPTIONAL. Furthermore, should there be a necessity for User Authentication by the Credential Issuer, it could be necessary to include the relevant metadata type ``openid_credential_verifier``.

The ``federation_entity`` metadata carries the informational parameters below together with the federation endpoint parameters. The federation endpoint parameters (``federation_fetch_endpoint``, ``federation_list_endpoint``, ``federation_resolve_endpoint`` and the others) are published only by the Federation TA and the Intermediates, according to their obligations defined in the Federation API Endpoints section above, and a Leaf does not expose them. The informational parameters below are OPTIONAL in `OID-FED`_; IT-Wallet specification profile supports the claims in the following table.

.. list-table::
  :class: longtable
  :widths: 25 75
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
    - REQUIRED. URL of the entity logo, in SVG format. See `OID-FED`_ Section 5.2.2
  * - **contacts**
    - REQUIRED. Within IT-Wallet it is the institutional verified email address (PEC) of the entity. See `OID-FED`_ Section 5.2.2
  * - **tos_uri**
    - OPTIONAL. URL of the terms of service of the entity. See `OID-FED`_ Section 5.2.2

Metadata about Wallet Provider, Credential Issuer and Relying Party are given in Section :ref:`wallet-solution-metadata:Wallet Solution Metadata`, :ref:`credential-issuer-solution:Credential Issuer Metadata` and :ref:`relying-party-metadata:Relying Party Metadata` respectively.

Entity Statement Examples
^^^^^^^^^^^^^^^^^^^^^^^^^

The following sections provide non-normative examples of Entity Statements, both for the direct onboarding under the Federation TA and for the intermediated onboarding under a Federation Intermediate. All the statements are signed JWTs with the JOSE header ``alg``, ``kid`` and ``typ`` set to ``entity-statement+jwt``, and only the payloads are shown. The protocol metadata and the pinned key sets are truncated (``{ ... }``) as their full definition is given in the metadata sections referenced above.

Entity Configuration of a Federation TA
"""""""""""""""""""""""""""""""""""""""

The Federation TA is the root of the Trust Chain. Its Entity Configuration has no ``authority_hints`` and no registration Trust Mark, it declares in ``trust_mark_issuers`` that itself is the only issuer of the registration Trust Marks, and its ``jwks`` carries, in addition to the Federation Entity Keys, the Signing Trust Anchors of the X.509 signing PKI as dedicated JWKs with ``x5c``.

.. code-block:: json

   {
     "iss": "https://trust-anchor.eid-wallet.example.it",
     "sub": "https://trust-anchor.eid-wallet.example.it",
     "iat": 1718207217,
     "exp": 1749743216,
     "jwks": {
       "keys": [
         {
           "kty": "EC",
           "crv": "P-256",
           "kid": "yRnq6oEvrxcZ1zYStADzTLX-qSw3Pb7E6mqJGNqnygA",
           "x": "xrk5H1nEWrNYRb7FBamuSRHHf-XWjv1k-uZCSVCSAnc",
           "y": "FM5YI7GvkTB8xxTiMTTSycDL0nguRowbibgfyqKjB0k"
         },
         {
           "kty": "EC",
           "crv": "P-256",
           "use": "sig",
           "kid": "signing-trust-anchor-01",
           "x": "B0sj_kZRT4A-oP9Y57dinEiDFTG-tjuPu7MiiQHHQ_g",
           "y": "iMDCuatE53HiX2VTDJ_q7LbQ-A7fgjXZpJsW-eZzge0",
           "x5c": [
             "<Signing Trust Anchor X.509 certificate>"
           ]
         }
       ]
     },
     "metadata": {
       "federation_entity": {
         "organization_name": "IT-Wallet Federation Trust Anchor",
         "homepage_uri": "https://trust-anchor.eid-wallet.example.it",
         "policy_uri": "https://trust-anchor.eid-wallet.example.it/policy",
         "logo_uri": "https://trust-anchor.eid-wallet.example.it/logo.svg",
         "contacts": [
           "trust-anchor@pec.example.it"
         ],
         "federation_fetch_endpoint": "https://trust-anchor.eid-wallet.example.it/fetch",
         "federation_list_endpoint": "https://trust-anchor.eid-wallet.example.it/list",
         "federation_resolve_endpoint": "https://trust-anchor.eid-wallet.example.it/resolve",
         "federation_trust_mark_status_endpoint": "https://trust-anchor.eid-wallet.example.it/trust_mark_status",
         "federation_trust_mark_endpoint": "https://trust-anchor.eid-wallet.example.it/trust_mark",
         "federation_trust_mark_list_endpoint": "https://trust-anchor.eid-wallet.example.it/trust_mark_list",
         "federation_historical_keys_endpoint": "https://trust-anchor.eid-wallet.example.it/historical_keys"
       }
     },
     "trust_mark_issuers": {
       "https://trust-anchor.eid-wallet.example.it/trust_marks/registration-entity/wallet_solution": [
         "https://trust-anchor.eid-wallet.example.it"
       ],
       "https://trust-anchor.eid-wallet.example.it/trust_marks/registration-entity/openid_credential_issuer": [
         "https://trust-anchor.eid-wallet.example.it"
       ],
       "https://trust-anchor.eid-wallet.example.it/trust_marks/registration-entity/openid_credential_verifier": [
         "https://trust-anchor.eid-wallet.example.it"
       ],
       "https://trust-anchor.eid-wallet.example.it/trust_marks/registration-entity/intermediate": [
         "https://trust-anchor.eid-wallet.example.it"
       ]
     }
   }

Entity Subordinate of Leaf issued by the Federation TA
""""""""""""""""""""""""""""""""""""""""""""""""""""""

The Federation TA issues a Subordinate Statement about each Leaf it registers directly. The statement carries the Federation Entity Keys of the Leaf, the ``metadata_policy`` that fixes the protocol keys and, when present, the service endpoints and the URIs of the Leaf to the values approved at onboarding, and the ``constraints`` of the subtree.

**Wallet Provider**

.. code-block:: json

   {
     "iss": "https://trust-anchor.eid-wallet.example.it",
     "sub": "https://wallet-provider.example.it",
     "iat": 1718207217,
     "exp": 1749743216,
     "jwks": {
       "keys": [
         {
           "kty": "EC",
           "crv": "P-256",
           "kid": "LqZSJoAEybT9V3jUQfZYUjVV-U5jV34sgbhIsIXltSY",
           "x": "38k73K5mw7Ev34lMwJhMBy5L2PnP9ayGfnMMtk4UZAw",
           "y": "4ohTh7joeKLhRfPRSXQvnu-OMqUIn9lzoJAp_ztuv1A"
         }
       ]
     },
     "metadata_policy": {
       "wallet_solution": {
         "jwks": {
           "value": { "... the Wallet Provider protocol keys registered at onboarding ..." }
         }
       }
     },
     "constraints": {
       "allowed_entity_types": [
         "wallet_solution"
       ],
       "max_path_length": 0
     }
   }

**Relying Party**

.. code-block:: json

   {
     "iss": "https://trust-anchor.eid-wallet.example.it",
     "sub": "https://access.privatecompany.example.com",
     "iat": 1718207217,
     "exp": 1749743216,
     "jwks": {
       "keys": [
         {
           "kty": "EC",
           "crv": "P-256",
           "kid": "cwdtstHkIOqwWD8UeXjY_NdKfB-d1bzIx7XKBQNVbsg",
           "x": "y8ahuTA-G4oLpTFYp7YrTd99kLPSlNoLPmwGJcXvWY8",
           "y": "HNRLc-1ennbeBtF3LbtBdq_0c7EX4samlHnwXilH_i0"
         }
       ]
     },
     "metadata_policy": {
       "openid_credential_verifier": {
         "jwks": {
           "value": { "... the Relying Party protocol keys registered at onboarding ..." }
         },
         "request_uris": {
           "value": [
             "https://access.privatecompany.example.com/openid4vp/request"
           ]
         },
         "response_uris": {
           "value": [
             "https://access.privatecompany.example.com/openid4vp/response"
           ]
         },
         "redirect_uris": {
           "value": [
             "https://access.privatecompany.example.com/openid4vp/callback"
           ]
         }
       }
     },
     "constraints": {
       "allowed_entity_types": [
         "openid_credential_verifier"
       ],
       "max_path_length": 0
     }
   }

**Credential Issuer**

.. code-block:: json

   {
     "iss": "https://trust-anchor.eid-wallet.example.it",
     "sub": "https://badge-issuer.example.it",
     "iat": 1718207217,
     "exp": 1749743216,
     "jwks": {
       "keys": [
         {
           "kty": "EC",
           "crv": "P-256",
           "kid": "r6KG1Jbgcv0iNW1y0ERO_X2Jw926V2UHRJH8d-GcDEI",
           "x": "26w7G_Myczl2-S8n0m1lMIjo3IzgZky-yNVdwaKOmhQ",
           "y": "2WMnoyCXqS4FUdv9e4JEAJKyhRIODi5xGfFdnA6cnVM"
         }
       ]
     },
     "metadata_policy": {
       "openid_credential_issuer": {
         "jwks": {
           "value": { "... the Credential Issuer protocol keys registered at onboarding ..." }
         },
         "credential_endpoint": {
           "value": "https://badge-issuer.example.it/credential"
         }
       }
     },
     "constraints": {
       "allowed_entity_types": [
         "openid_credential_issuer",
         "oauth_authorization_server"
       ],
       "max_path_length": 0
     }
   }

Entity Subordinate of an Intermediate
"""""""""""""""""""""""""""""""""""""

The Federation TA issues a Subordinate Statement about the Federation Intermediate. The ``constraints`` restrict the subtree of the Intermediate to the Relying Parties it can intermediate, and ``max_path_length`` is set to 1 to allow the single level of intermediation between the Federation TA and the affiliated Relying Parties. It carries no ``metadata_policy``: the affiliated Relying Parties are bound by the Intermediate in the Subordinate Statements it issues about them.

.. code-block:: json

   {
     "iss": "https://trust-anchor.eid-wallet.example.it",
     "sub": "https://intermediary.example.com",
     "iat": 1718207217,
     "exp": 1749743216,
     "jwks": {
       "keys": [
         {
           "kty": "EC",
           "crv": "P-256",
           "kid": "EycKTxHbR_s_aZB46j_1ObHG3n2QEQ0sU0-gRGdBWv0",
           "x": "4sAmMPyNl21DjQ_i6C4y0erHz3IVsVETYpH4kOoKFb8",
           "y": "B5nPVnBVBss55KGCJG8_EyT72PJKU8n_k8SMZdPUIaE"
         }
       ]
     },
     "constraints": {
       "allowed_entity_types": [
         "openid_credential_verifier"
       ],
       "max_path_length": 1
     }
   }

Entity Subordinate of Leaf issued by a Federation Intermediate
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

The Federation Intermediate issues a Subordinate Statement about each affiliated Relying Party. It carries the ``metadata_policy`` that binds the protocol metadata of the affiliated Relying Party to the values approved at onboarding, exactly as the Federation TA does for the Leaves it registers directly. The ``constraints`` of the subtree are set by the Federation TA in the statement about the Intermediate. In the National Trust Framework an Intermediary intermediates only Relying Parties.

.. code-block:: json

   {
     "iss": "https://intermediary.example.com",
     "sub": "https://rp.affiliated.example.com",
     "iat": 1718207217,
     "exp": 1749743216,
     "jwks": {
       "keys": [
         {
           "kty": "EC",
           "crv": "P-256",
           "kid": "n47zfejmk3V14aKUQCEcA7sTKi-SXMw7E1MFnpQCL-0",
           "x": "H3_bMVOWJoDSBenUzelAbAj4vanmXNJ3KT2Vk_OaehI",
           "y": "aMoXkKSssBtMHwSCR-hY8mmFQFs3Hf5iQ0zFWMHAQfc"
         }
       ]
     },
     "metadata_policy": {
       "openid_credential_verifier": {
         "jwks": {
           "value": { "... the affiliated Relying Party protocol keys registered at onboarding ..." }
         },
         "request_uris": {
           "value": [
             "https://rp.affiliated.example.com/openid4vp/request"
           ]
         },
         "response_uris": {
           "value": [
             "https://rp.affiliated.example.com/openid4vp/response"
           ]
         },
         "redirect_uris": {
           "value": [
             "https://rp.affiliated.example.com/openid4vp/callback"
           ]
         }
       }
     }
   }

Entity Configuration of a Federation Intermediate
"""""""""""""""""""""""""""""""""""""""""""""""""

The Federation Intermediate is a ``federation_entity`` only. Its Entity Configuration points to the Federation TA through ``authority_hints`` and carries its registration Trust Mark with the ``intermediate`` Entity Type Identifier. It exposes the fetch and list endpoints used to serve the Subordinate Statements of its affiliated Relying Parties.

.. code-block:: json

   {
     "iss": "https://intermediary.example.com",
     "sub": "https://intermediary.example.com",
     "iat": 1718207217,
     "exp": 1749743216,
     "authority_hints": [
       "https://trust-anchor.eid-wallet.example.it"
     ],
     "jwks": {
       "keys": [
         {
           "kty": "EC",
           "crv": "P-256",
           "kid": "EycKTxHbR_s_aZB46j_1ObHG3n2QEQ0sU0-gRGdBWv0",
           "x": "4sAmMPyNl21DjQ_i6C4y0erHz3IVsVETYpH4kOoKFb8",
           "y": "B5nPVnBVBss55KGCJG8_EyT72PJKU8n_k8SMZdPUIaE"
         }
       ]
     },
     "metadata": {
       "federation_entity": {
         "organization_name": "Intermediary S.r.l.",
         "homepage_uri": "https://intermediary.example.com",
         "policy_uri": "https://intermediary.example.com/policy",
         "logo_uri": "https://intermediary.example.com/logo.svg",
         "contacts": [
           "intermediary@pec.example.com"
         ],
         "federation_fetch_endpoint": "https://intermediary.example.com/fetch",
         "federation_list_endpoint": "https://intermediary.example.com/list"
       }
     },
     "trust_marks": [
       {
         "trust_mark_type": "https://trust-anchor.eid-wallet.example.it/trust_marks/registration-entity/intermediate",
         "trust_mark": "<signed Trust Mark JWT>"
       }
     ]
   }

Entity Configuration of a Leaf
""""""""""""""""""""""""""""""

Each Leaf publishes its own Entity Configuration, pointing to its immediate superior through ``authority_hints`` and carrying its registration Trust Mark. The examples below report the main claims, the protocol metadata is referenced to its metadata section.

**Wallet Provider**

.. code-block:: json

   {
     "iss": "https://wallet-provider.example.it",
     "sub": "https://wallet-provider.example.it",
     "iat": 1718207217,
     "exp": 1749743216,
     "authority_hints": [
       "https://trust-anchor.eid-wallet.example.it"
     ],
     "jwks": {
       "keys": [
         {
           "kty": "EC",
           "crv": "P-256",
           "kid": "LqZSJoAEybT9V3jUQfZYUjVV-U5jV34sgbhIsIXltSY",
           "x": "38k73K5mw7Ev34lMwJhMBy5L2PnP9ayGfnMMtk4UZAw",
           "y": "4ohTh7joeKLhRfPRSXQvnu-OMqUIn9lzoJAp_ztuv1A"
         }
       ]
     },
     "metadata": {
       "federation_entity": {
         "organization_name": "Example Wallet Provider",
         "homepage_uri": "https://wallet-provider.example.it",
         "policy_uri": "https://wallet-provider.example.it/policy",
         "logo_uri": "https://wallet-provider.example.it/logo.svg",
         "contacts": [
           "wallet-provider@pec.example.it"
         ]
       },
       "wallet_solution": { ".. as defined in the Wallet Solution Metadata section ..." }
     },
     "trust_marks": [
       {
         "trust_mark_type": "https://trust-anchor.eid-wallet.example.it/trust_marks/registration-entity/wallet_solution",
         "trust_mark": "<signed Trust Mark JWT>"
       }
     ]
   }

**Relying Party**

.. code-block:: json

   {
     "iss": "https://access.privatecompany.example.com",
     "sub": "https://access.privatecompany.example.com",
     "iat": 1718207217,
     "exp": 1749743216,
     "authority_hints": [
       "https://trust-anchor.eid-wallet.example.it"
     ],
     "jwks": {
       "keys": [
         {
           "kty": "EC",
           "crv": "P-256",
           "kid": "cwdtstHkIOqwWD8UeXjY_NdKfB-d1bzIx7XKBQNVbsg",
           "x": "y8ahuTA-G4oLpTFYp7YrTd99kLPSlNoLPmwGJcXvWY8",
           "y": "HNRLc-1ennbeBtF3LbtBdq_0c7EX4samlHnwXilH_i0"
         }
       ]
     },
     "metadata": {
       "federation_entity": {
         "organization_name": "Private Company S.p.A.",
         "homepage_uri": "https://access.privatecompany.example.com",
         "policy_uri": "https://access.privatecompany.example.com/policy",
         "logo_uri": "https://access.privatecompany.example.com/logo.svg",
         "contacts": [
           "compliance@pec.privatecompany.example.com"
         ]
       },
       "openid_credential_verifier": { "... as defined in the Relying Party Metadata section ..." }
     },
     "trust_marks": [
       {
         "trust_mark_type": "https://trust-anchor.eid-wallet.example.it/trust_marks/registration-entity/openid_credential_verifier",
         "trust_mark": "<signed Trust Mark JWT>"
       }
     ]
   }

**Credential Issuer**

.. code-block:: json

   {
     "iss": "https://badge-issuer.example.it",
     "sub": "https://badge-issuer.example.it",
     "iat": 1718207217,
     "exp": 1749743216,
     "authority_hints": [
       "https://trust-anchor.eid-wallet.example.it"
     ],
     "jwks": {
       "keys": [
         {
           "kty": "EC",
           "crv": "P-256",
           "kid": "r6KG1Jbgcv0iNW1y0ERO_X2Jw926V2UHRJH8d-GcDEI",
           "x": "26w7G_Myczl2-S8n0m1lMIjo3IzgZky-yNVdwaKOmhQ",
           "y": "2WMnoyCXqS4FUdv9e4JEAJKyhRIODi5xGfFdnA6cnVM"
         }
       ]
     },
     "metadata": {
       "federation_entity": {
         "organization_name": "Comune di Example",
         "homepage_uri": "https://badge-issuer.example.it",
         "policy_uri": "https://badge-issuer.example.it/policy",
         "logo_uri": "https://badge-issuer.example.it/logo.svg",
         "contacts": [
           "protocollo@pec.comune.example.it"
         ]
       },
       "openid_credential_issuer": { "... as defined in the Credential Issuer Metadata section ..." }
     },
     "trust_marks": [
       {
         "trust_mark_type": "https://trust-anchor.eid-wallet.example.it/trust_marks/registration-entity/openid_credential_issuer",
         "trust_mark": "<signed Trust Mark JWT>"
       }
     ]
   }

Trust Marks
^^^^^^^^^^^

As a result of a successful onboarding completion, entities receive IT-Wallet Federation Trust Marks. Trust Marks are issued by the Federation Authority (Trust Anchor for direct onboarding, Intermediate for mediated onboarding) through the Federation Trust Mark Endpoint and serve as verifiable attestations about compliance with IT-Wallet technical profiles and/or authorization policies.

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

Within IT-Wallet the ``registration-entity`` Trust Mark is the registration Trust Mark of an entity. The only Trust Mark issuer MUST be the Federation TA. It attests the registration and carries the authorization data of the entity, that is its entitlements and, where applicable, the Credentials and the attributes it is authorized to issue or to request. This registration Trust Mark is the functional analogue of the Wallet-Relying Party Registration Certificate (WRPRC) of the EUDIW Trust Framework. An entity receives one registration Trust Mark for each role it holds, with the ``<entity_type>`` component of the identifier set accordingly.

A Relying Party Intermediary receives its registration Trust Mark with the ``intermediate`` ``<entity_type>`` in the identifier. Unlike the EUDIW Trust Framework, where the intermediary relationship is expressed in the registration data of the intermediated Relying Party, in the National Trust Framework the relationship is expressed through the federation hierarchy as the Intermediary is a Federation Intermediate that publishes the Subordinate Statements of its affiliated Relying Parties, and each affiliated Relying Party sets its ``authority_hints`` to the Intermediary. The registration Trust Mark of each affiliated Relying Party is also issued by the Federation Trust Anchor. For this reason no dedicated intermediary field is present in the Trust Mark. The onboarding of the Intermediary is defined in :ref:`onboarding-procedure:Relying Party Intermediaries`.

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
   :widths: 25 75

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
   * - **public_body**
     - REQUIRED. Boolean indicating whether the entity is a public sector body.
   * - **vat_number**
     - REQUIRED when ``public_body`` is ``false``. VAT number of the entity. It MAY also be present when ``public_body`` is ``true``.
   * - **legal_identifier**
     - RECOMMENDED. Legal registration number or identifier of the entity (e.g., business registration number, tax code).
   * - **ipa_code**
     - REQUIRED when ``public_body`` is ``true``, MUST NOT be present otherwise. IPA (Indice delle Pubbliche Amministrazioni) code of the public sector entity.
   * - **organization_name**
     - REQUIRED. Full name of the Organizational Entity.
   * - **email**
     - REQUIRED. Institutional or PEC email of the organization.
   * - **support_uri**
     - REQUIRED. URL or email address to be used for requests related to the entity, such as data deletion or portability.
   * - **srv_description**
     - REQUIRED. Multilingual description of the service provided by the entity. Each entry contains ``lang`` and ``value``.
   * - **entitlements**
     - REQUIRED. Array of entitlement URIs identifying the role of the subject, as defined in `ETSI TS 119 475`_ Annex A.2 (e.g. ``Service_Provider``, ``PID_Provider``, ``QEAA_Provider``, ``PUB_EAA_Provider``, ``Non_Q_EAA_Provider``).
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
  The claims that carry the authorization data (``entitlements``, ``provides_attestations``, ``credentials``, ``purpose``, ``privacy_policy``, ``supervisory_authority``) and the identity and transparency claims aligned with the WRPRC (``public_body``, ``support_uri``, ``srv_description``) are defined in analogy with the EUDIW Wallet-Relying Party Registration Certificate (`ETSI TS 119 475`_), so that a Trust Evaluator can reuse the same authorization logic for both artifacts.

.. note::
  The revocation status of a Trust Mark is verified through the **trust mark status** (``/trust_mark_status``) endpoint (`OID-FED`_ Section 8.4), not through a status list carried in the token. This is the difference with the WRPRC, whose ``status`` claim points to a status list: the Trust Mark relies on the federation native revocation mechanism. The consumption of these claims by the Trust Evaluator is defined in :ref:`trust-evaluation-oidfed:Authorization`.

The following non-normative examples illustrate the registration Trust Mark JWT content for a Credential Issuer, a public non-qualified EAA Provider issuing an Employee Badge, for a Relying Party requesting that Employee Badge, and for a Relying Party Intermediary.

Credential Issuer, a public non-qualified EAA Provider issuing the Employee Badge:

.. code-block:: json

   {
     "iss": "https://trust-anchor.eid-wallet.example.it",
     "sub": "https://badge-issuer.example.it",
     "trust_mark_type": "https://trust-anchor.eid-wallet.example.it/trust_marks/registration-entity/openid_credential_issuer",
     "iat": 1718207217,
     "exp": 1749743216,
     "public_body": true,
     "ipa_code": "c_h501",
     "legal_identifier": "80012345678",
     "organization_name": "Comune di Example",
     "email": "protocollo@comune.example.it",
     "support_uri": "https://badge-issuer.example.it/support",
     "srv_description": [
       {"lang": "it", "value": "Servizio di emissione del badge dipendente"},
       {"lang": "en", "value": "Employee Badge issuance service"}
     ],
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
     "supervisory_authority": {
       "uri": "https://www.dpa.example.it/report",
       "email": "reports@dpa.example.it",
       "phone": "+390612345678"
     },
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
     "public_body": false,
     "vat_number": "IT12345678901",
     "legal_identifier": "12345678901",
     "organization_name": "Private Company S.p.A.",
     "email": "compliance@privatecompany.example.com",
     "support_uri": "https://access.privatecompany.example.com/support",
     "srv_description": [
       {"lang": "it", "value": "Servizio di controllo dell'accesso fisico"},
       {"lang": "en", "value": "Physical access control service"}
     ],
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
     "trust_mark_type": "https://trust-anchor.eid-wallet.example.it/trust_marks/registration-entity/intermediate",
     "iat": 1718207217,
     "exp": 1749743216,
     "public_body": false,
     "vat_number": "IT98765432109",
     "legal_identifier": "98765432109",
     "organization_name": "Intermediary S.r.l.",
     "email": "info@intermediary.example.com",
     "support_uri": "https://intermediary.example.com/support",
     "srv_description": [
       {"lang": "it", "value": "Servizio di intermediazione per Relying Party"},
       {"lang": "en", "value": "Intermediation service for Relying Parties"}
     ],
     "entitlements": ["Service_Provider"],
     "supervisory_authority": {
       "uri": "https://www.dpa.example.it/report",
       "email": "reports@dpa.example.it",
       "phone": "+390612345678"
     },
     "logo_uri": "https://intermediary.example.com/logo.svg"
   }

   
.. include:: ../common/common_definitions.rst


.. role:: raw-html(raw)
  :format: html

Authentic Source Endpoints
--------------------------

e-Service PDND Authentic Source Catalog
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Public Authentic Sources MUST provide the following e-Service through PDND to provide the Credential Issuer with User's attributes required to the issuance of a Digital Credential.

.. only:: html

  .. note::
    A complete OpenAPI Specification is available :raw-html:`<a href="OAS3-PDND-AS.html" target="_blank">here</a>`.

.. only:: latex

  .. note::
    A complete OpenAPI Specification is available :ref:`e-service-pdnd-template:Authentic Source PDND OpenAPI Specification`.

Get Attribute Claims
""""""""""""""""""""

.. _authentic-source-endpoint-get-attribute-claims:
.. list-table::
  :class: longtable
  :widths: 20 80
  :stub-columns: 1

  * - **Description**
    - This e-Service provides the Credential Issuer with all attribute claims necessary for the issuance of a Digital Credential.
  * - **Provider**
    - Authentic Source
  * - **Consumer**
    - Credential Issuer

.. note::
  The Authentic Source and the Credential Issuer MUST implement the necessary logic to keep track of the requests and responses exchanged via this e-Service, in order to be able to correlate them with the related issuance of a Digital Credential. In particular,
    - both MUST save the ``jti`` value in the Agid-JWT-Signature payload of the request to manage Signals related to the deffered issuance of a Digital Credential (see :ref:`signal-hub-endpoint:Signals Processing`);
    - the Authentic Source MUST record the datetime value provided within the ``last_updated`` parameter, which indicates the last time the User's attributes were updated in the Authentic Source's database;
    - the Credential Issuer MUST read the ``last_updated`` value received in the response to be able to check if the User's attributes have changed since the last issuance of a Digital Credential.

Example of Authentic Source response
"""""""""""""""""""""""""""""""""""""

The endpoint response MUST use the HTTP Content-Type set to ``application/json``. Below is a concrete example with fictitious data to clarify the expected shape and content.

.. literalinclude:: ../../examples/credential-claims-response-example.json
  :language: json
  :caption: Example of the response JSON payload (Get Attribute Claims)

In summary:

- **userClaims**: user identity data (first name, family name, date/place of birth, tax id or personal administrative number). At least one of ``tax_id_code`` and ``personal_administrative_number`` is required when providing user claims.
- **attributeClaims**: array of datasets; each element **MUST** contain ``object_id``, ``status`` (VALID | INVALID | SUSPENDED), ``last_updated`` (ISO 8601 format), plus any dataset-specific attributes (e.g. ``nationality``, ``residence_address``).
- **metadataClaims**: array of metadata per dataset (``object_id`` required; ``issuance_date`` and ``expiry_date`` optional).
- **interval**: required when the request does not include a ``claims`` parameter; indicates the number of seconds to wait before repeating the request (e.g. 864000 = 10 days).

Dataset Status and Digital Credential Lifecycle
''''''''''''''''''''''''''''''''''''''''''''''''''

The Authentic Source manages the validity of the User's attributes (datasets); the Credential Issuer manages the Digital Credential lifecycle. When the Credential Issuer receives an UPDATE Signal or queries the Get Attribute Claims endpoint, it inspects the ``status`` of each dataset and updates the corresponding Digital Credential accordingly:

.. list-table::
  :header-rows: 1

  * - Dataset status
    - Typical dataset condition
    - Effect on Digital Credential (Credential Issuer action)
  * - VALID
    - Dataset not revoked/suspended (includes Issued and Expired; expiry verified via metadata)
    - Credential may remain Valid (expiry checked via expiry_date, nbf/exp)
  * - INVALID
    - Dataset actively revoked by the Authentic Source
    - Credential status updated to Revoked (Status List: INVALID)
  * - SUSPENDED
    - Temporarily invalid (e.g. under review)
    - Credential status updated to Suspended (Status List: SUSPENDED)

Issued and Expired datasets fall within VALID; the Credential Issuer verifies expiry via metadata claims (e.g. ``expiry_date``, ``nbf``/``exp``). For full details on the status update flow, see :ref:`credential-revocation:Status Update by Authentic Sources`.

The successful response (HTTP 200) returns a ``CredentialClaimsResponse`` object formatted as a **Payload JSON**.

Signature Verification and Key Management
'''''''''''''''''''''''''''''''''''''''''

As the response token is signed, the Credential Issuer (Consumer) MUST verify the signature to ensure the integrity and authenticity of the data received from the Authentic Source.

The signature verification and key retrieval process MUST strictly follow the standard pattern defined for **PDND e-Services**.
Please refer to the Technical Appendix (Section :ref:`e-service-pdnd:e-Service PDND`) for details on JWT validation and specifications for retrieving the Provider's public key via the Interoperability API.

.. warning::
  Alternative mechanisms for distributing cryptographic material (e.g., public ``.well-known`` endpoints directly exposed by the Authentic Source or *out-of-band* distribution) are not allowed. Trust management MUST remain centralized within the perimeter of the PDND infrastructure as described in the references cited above.

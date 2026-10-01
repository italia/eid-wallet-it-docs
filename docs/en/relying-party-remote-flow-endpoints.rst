.. include:: ../common/common_definitions.rst
.. Included via relying-party-endpoints.rst at title level '"' (level 3).

The Relying Party MUST expose the endpoints required by the selected remote presentation path. The National Trust Framework path uses Federation discovery and redirect endpoints.

.. note::

  The Relying Party makes explicit its trust framework for the remote flow as follows: 
  - the National Trust Framework requires the ``client_id`` prefix in the be ``openid_federation``.
  - the EUDIW Trust Framework requires the ``client_id`` prefix in the signed Request Object to be valued with ``x509_hash``.

.. note::
  Tests related to Relying Party remote flow endpoints are defined in the remote presentation test matrix (:ref:`test-plans-remote-presentation:Remote Credential Verifier Test Matrix`).


Federation Endpoint
"""""""""""""""""""""""

For the National Trust Framework path, the Relying Party MUST provide its Entity Configuration through the ``/.well-known/openid-federation`` endpoint, according to Section :ref:`infrastructure-trust:Entity Configuration`. This endpoint enables trust establishment and discovery of the Relying Party's capabilities.

Technical details are provided in Section :ref:`relying-party-entity-configuration:Relying Party Entity Configuration`.


OpenID4VP Remote Flow Endpoints
"""""""""""""""""""""""""""""""

The following endpoints are required for OpenID4VP 1.0 remote presentation flows as described in :ref:`remote-flow:Remote Flow`. They support both Same Device and Cross Device flows.

Request URI Endpoint
....................

The Request URI Endpoint is where the Relying Party provides the signed Request Object by reference (OIDFVP-HAIP-REDIRECTS-04 in `ETSI TS 119 472-2`_) to the Wallet Instance. This endpoint supports GET and, when requested by ``request_uri_method``, POST as defined in the OpenID4VP 1.0 specification.

For detailed implementation requirements, see :ref:`remote-flow:Request URI Request` and :ref:`remote-flow:Request URI Response`.


Response URI Endpoint
.....................

The Response URI Endpoint receives the Authorization Response from the Wallet Instance containing the Verifiable Presentation. This endpoint processes the presentation and validates the credentials.

For detailed implementation requirements, see :ref:`remote-flow:Authorization Response` and :ref:`remote-flow:Relying Party Response`.


Status Endpoint (Optional)
..........................

The Status Endpoint is an optional endpoint that allows the user-agent to monitor the progress of the presentation flow. This endpoint is particularly useful for Same Device flows where the user-agent needs to know when the Wallet Instance has completed the presentation.

For detailed implementation requirements, see :ref:`remote-flow:Status Endpoint` and :ref:`remote-flow:Status Endpoint Errors`.


Data Deletion Request
"""""""""""""""""""""

The Wallet Instance initiates a data deletion request through the Relying Party support contact, as specified in :ref:`user-attribute-deletion:User's Attributes Deletion` and in `EUDI-TS 7`_.


Security Considerations
"""""""""""""""""""""""

All Relying Party endpoints MUST implement appropriate security measures:

- **HTTPS Only**: All endpoints MUST be accessible only over HTTPS
- **Endpoint Mix-up Protection**: Endpoint URLs MUST be attested by trusted third parties through the respective National or EUDIW Trust Framework.
- **Input Validation**: All endpoints MUST validate input parameters and reject malformed requests
- **Rate Limiting**: Endpoints SHOULD implement rate limiting to prevent abuse
- **Audit Logging**: All endpoint interactions SHOULD be logged for security monitoring

For detailed security requirements, see :ref:`remote-flow:Remote Flow` and the relevant test cases in :ref:`test-plans-remote-presentation:Remote Credential Verifier Test Matrix`.


Implementation Notes
""""""""""""""""""""

- The specific implementation details for most endpoints are left to the Relying Party's discretion
- Endpoints MUST comply with the OpenID4VP 1.0 specification for remote flows
- Proximity flow endpoints MUST support the lifecycle management of Verifier Apps
- For a Relying Party operating in the National Trust Framework, its endpoints MUST be discoverable through the Relying Party's Entity Configuration. For a Relying Party operating in the EUDIW Trust Framework, its endpoints are carried in the signed Request Object which is authenticated by the WRPAC according to :ref:`trust-evaluation:EUDIW Authentication`.
- Error responses MUST follow the standard HTTP status codes and include appropriate error descriptions

For comprehensive implementation guidance, refer to the individual endpoint sections and the test matrices for validation requirements.

Credential Issuance Test Matrix
---------------------------------

This section provides the set of test cases for verifying conformance of a Credential Issuance implementations to the technical rules defined in the IT-Wallet ecosystem.
Tests related to Credential Issuer are related to the issuance of Credential of Public Interest, as published within the Credential Catalogue.

.. note::
  References about official OpenID4VCI test plans will update this section in future releases.

- PID/EAA Issuance


.. list-table::
  :class: longtable
  :widths: 15 15 35 35
  :header-rows: 1

  * - Test Case ID
    - Purpose
    - Description
    - Expected Result
  * - ISS-001
    - Setup
    - Validate Wallet Instance Setup
    - Wallet Instance is set up with a valid Wallet Attestation. Ensure the public key is valid and correctly bound to a secure element.
  * - ISS-002
    - Discovery
    - Credential Issuer Discovery
    - Wallet Instance successfully discovers trusted Digital Credential Issuers using the Credential Catalogue and their configuration compliance and policies with Federation API.
  * - ISS-003
    - Metadata
    - Credential Issuer Metadata Retrieval
    - Wallet Instance retrieves and validates Credential Issuer metadata. Metadata includes PID formats, supported algorithms, and interoperability parameters.
  * - ISS-004
    - Authorization, Authentication
    - Credential Request using Authorization Code Flow
    - Wallet Instance successfully requests Credential using Authorization Code Flow. Validate PKCE use with a code verifier of 43-128 characters.
  * - ISS-005
    - Authentication
    - User Authentication with PID Provider
    - User is authenticated with LoA 3 (High) by the PID Provider. Validate the use of the digital identity scheme CieID and ensure that User consent is obtained.
  * - ISS-006
    - Issuance
    - Credential Issuance
    - Credential is issued and bound to the Wallet Instance's key material. Validate the binding process and ensure the integrity and the compliance to data model of the issued Credential.
  * - ISS-007
    - Authentication
    - User Authentication with (Q)EAA Provider
    - User is authenticated by presenting a valid PID. The presentation request, the PID is valid and previously obtained.
  * - ISS-008
    - Security
    - Pushed Authorization Request (PAR) Validation
    - Credential Issuer validates the PAR request successfully.
  * - ISS-009
    - Security
    - Token Request Validation
    - Credential Issuer validates the token request and issues tokens. Validate the DPoP proof and ensure the authorization code is valid and not reused.
  * - ISS-010
    - Security
    - Credential Request Validation
    - Credential Issuer validates the Credentials request and issues Credentials. Validate the proof of possession and ensure the credential type matches the request.
  * - ISS-011
    - Deferred Issuance
    - Deferred Issuance Flow
    - Wallet Instance handles deferred issuance correctly and retrieves credentials later. Validate the use of transaction unique identifier (`transaction_id`) and ensure the Credential is issued after the specified lead time.
  * - ISS-012
    - Notification
    - Notification Handling
    - Wallet Instance sends and receives notifications correctly. Validate the use of `notification_id` and ensure the event type is correctly reported.
  * - ISS-013
    - Credential Issuance
    - (Q)EAA Provider offers Credentials to Holder
    - Wallet Instances evaluate the offer and start the authorization flow after having evaluated the trust with the (Q)EAA Provider.
  * - ISS-014
    - Security
    - Validate `client_id` in PAR Request
    - Ensure the `client_id` in the request body matches the `client_id` claim in the Request Object.
  * - ISS-015
    - Security
    - Validate `iss` Claim in Request Object
    - Ensure the `iss` claim in the Request Object matches the `client_id` claim.
  * - ISS-016
    - Security
    - Validate `aud` Claim in Request Object
    - Ensure the `aud` claim in the Request Object is equal to the identifier of the Credential Issuer.
  * - ISS-017
    - Security
    - Reject PAR Request with `request_uri`
    - Ensure the PAR request is rejected if it contains the `request_uri` parameter.
  * - ISS-018
    - Security
    - Validate Mandatory Parameters in Request Object
    - Ensure the Request Object contains all mandatory parameters and values are validated.
  * - ISS-019
    - Security
    - Validate `OAuth-Client-Attestation-PoP`
    - Ensure the `OAuth-Client-Attestation-PoP` parameter is validated.
  * - ISS-020
    - Authorization
    - Validate `request_uri` in Authorization Request
    - Ensure `request_uri` values are treated as one-time use and expired requests are rejected.
  * - ISS-021
    - Authorization
    - Identify Request from Submitted PAR
    - Ensure the request is identified as a result of the submitted PAR.
  * - ISS-022
    - Authorization
    - Reject Authorization Requests without `request_uri`
    - Ensure all Authorization Requests without `request_uri` are rejected.
  * - ISS-023
    - Security
    - Validate Authorization Response Parameters
    - Ensure the Authorization Response contains all defined parameters.
  * - ISS-024
    - Security
    - Validate `state` Parameter in Authorization Response
    - Ensure the `state` parameter in the response matches the value sent in the Request Object.
  * - ISS-025
    - Security
    - Validate `iss` Parameter in Authorization Response
    - Ensure the `iss` parameter matches the intended Credential Issuer.
  * - ISS-026
    - Security
    - Validate DPoP Proof for Token Endpoint
    - Ensure the DPoP Proof JWT is valid and binds the Access Token to the Wallet Instance.
  * - ISS-027
    - Security
    - Validate Token Request Parameters
    - Ensure the token request includes `code`, `code_verifier`, and valid OAuth 2.0 Attestation.
  * - ISS-028
    - Security
    - Validate Authorization Code in Token Request
    - Ensure the Authorization `code` is valid and not reused.
  * - ISS-029
    - Security
    - Validate `redirect_uri` in Token Request
    - Ensure the `redirect_uri` matches the value in the previous Request Object.
  * - ISS-030
    - Security
    - Validate DPoP Proof JWT in Token Request
    - Ensure the DPoP Proof JWT is validated according to the specification.
  * - ISS-031
    - Security
    - Validate Nonce Request
    - Ensure the Nonce Request is sent correctly and a fresh `c_nonce` is obtained.
  * - ISS-032
    - Security
    - Validate Nonce Response
    - Ensure the `c_nonce` in the Nonce Response is unpredictable and used correctly.
  * - ISS-033
    - Security
    - Validate DPoP Proof for Credential Endpoint
    - Ensure the DPoP Proof JWT for the Credential Endpoint is valid and binds the Credential to the Wallet Instance.
  * - ISS-034
    - Security
    - Validate Credential Request Parameters
    - Ensure the Credential Request includes Access Token, DPoP Proof JWT, and valid proof of possession.
  * - ISS-035
    - Security
    - Validate JWT Proof in Credential Request
    - Ensure the JWT proof includes all required claims and is signed correctly.
  * - ISS-036
    - Security
    - Validate `c_nonce` in Credential Request
    - Ensure the `c_nonce` in the JWT matches the value provided by the server.
  * - ISS-037
    - Security
    - Validate Credential Response Parameters
    - Ensure the Credential Response contains all mandatory parameters and values are validated.
  * - ISS-038
    - Security
    - Validate Credential Integrity
    - Ensure the integrity of the issued Credential by verifying the signature.
  * - ISS-039
    - Security
    - Validate Credential Type and Schema
    - Ensure the issued Credential matches the requested type and complies with the schema.
  * - ISS-040
    - Security
    - Validate Trust Chain in Credential
    - Ensure the Trust Chain in the Credential header verifies the Credential Issuer's trust at time of issuance.
  * - ISS-041
    - Security
    - Validate Deferred Issuance Parameters
    - Ensure the Deferred Issuance parameters are used correctly and the Credential is issued after the specified lead time.
  * - ISS-042
    - Security
    - Validate Notification Request Parameters
    - Ensure the Notification Request includes `notification_id` and valid event type.
  * - ISS-043
    - Security
    - Validate Notification Response
    - Ensure the Notification Response is received with the correct status code.
  * - ISS-044
    - Security
    - Validate Refresh Token Flow
    - Ensure the Refresh Token flow is used correctly and tokens are bound to the DPoP key.
  * - ISS-045
    - Security
    - Validate Refresh Token Expiry
    - Ensure the Refresh Token is not expired and is used within the allowed timeframe.
  * - ISS-046
    - Security
    - Validate Sender-Constrained Tokens
    - Ensure Refresh Tokens are cryptographically bound to the Wallet Instance.
  * - ISS-047
    - Security
    - Validate Limiting Use of Refresh Token
    - Ensure the use of Refresh Tokens is limited and complies with the specification.
  * - ISS-048
    - Revocation
    - Validate life time of Wallet Attestations
    - Ensure Wallet Attestations are short-lived or provided with Status List if long-lived.
  * - ISS-049
    - Security
    - Validate Re-Issuance Flow
    - Ensure the Re-Issuance flow is used correctly and complies with the specification.
  * - ISS-050
    - Security
    - Validate Data Model/Format Update
    - Ensure the Data Model/Format update is handled correctly during Re-Issuance.
  * - ISS-051
    - Security
    - Validate User Attribute Set Update
    - Ensure User attribute set updates are handled correctly during Re-Issuance.
  * - ISS-052
    - Security
    - Validate Credential Expiry in Re-Issuance
    - Ensure the newly issued Credential has the same expiry date as the previous one.
  * - ISS-053
    - Security
    - Validate User Authentication in Re-Issuance
    - Ensure User authentication is required for Re-Issuance after Credential expiration.
  * - ISS-054
    - Security
    - Validate Deferred Endpoint Parameters
    - Ensure the Deferred Endpoint parameters are used correctly and the Credential is issued after the specified lead time.
  * - ISS-055
    - Security
    - Validate Deferred Credential Request
    - Ensure the Deferred Credential Request is sent correctly and the Credential is issued.
  * - ISS-056
    - Security
    - Validate Deferred Credential Response
    - Ensure the Deferred Credential Response contains all mandatory parameters and values are validated.
  * - ISS-057
    - Security
    - Validate Notification Endpoint Parameters
    - Ensure the Notification Endpoint parameters are used correctly and the event is reported.
  * - ISS-058
    - Security
    - Validate Error Handling in Notification Endpoint
    - Ensure errors in the Notification Endpoint are handled correctly and reported.
  * - ISS-059
    - Security
    - Validate Error Handling in Credential Endpoint
    - Ensure errors in the Credential Endpoint are handled correctly and reported.
  * - ISS-060
    - Security
    - Validate Error Handling in Token Endpoint
    - Ensure errors in the Token Endpoint are handled correctly and reported.
  * - ISS-061
    - Security
    - Validate Error Handling in Authorization Endpoint
    - Ensure errors in the Authorization Endpoint are handled correctly and reported.
  * - ISS-062
    - Error Handling
    - Validate Error Handling in PAR Endpoint
    - Ensure errors in the PAR Endpoint are handled correctly and reported.
  * - ISS-063
    - Error Handling
    - Validate Error Handling in Nonce Endpoint
    - Ensure errors in the Nonce Endpoint are handled correctly and reported.
  * - ISS-064
    - Error Handling
    - Validate Error Handling in Deferred Endpoint
    - Ensure errors in the Deferred Endpoint are handled correctly and reported.
  * - ISS-065
    - Error Handling
    - Validate Error Handling in Re-Issuance Flow
    - Ensure errors in the Re-Issuance Flow are handled correctly and reported.
  * - ISS-066
    - Error Handling
    - Validate Error Handling in Refresh Token Flow
    - Ensure errors in the Refresh Token Flow are handled correctly and reported.
  * - ISS-067
    - Error Handling
    - Validate Error Handling in Credential Issuance
    - Ensure errors in the Credential Issuance process are handled correctly and reported.
  * - ISS-068
    - Error Handling
    - Validate Error Handling in Credential Request
    - Ensure errors in the Credential Request process are handled correctly and reported.
  * - ISS-069
    - Error Handling
    - Validate Error Handling in Credential Response
    - Ensure errors in the Credential Response process are handled correctly and reported.
  * - ISS-070
    - Error Handling
    - Validate Error Handling in Credential Validation
    - Ensure errors in the Credential Validation process are handled correctly and reported.
  * - ISS-071
    - Error Handling
    - Validate Error Handling in Credential Integrity
    - Ensure errors in the Credential Integrity process are handled correctly and reported.
  * - ISS-072
    - Error Handling
    - Validate Error Handling in Credential Type and Schema
    - Ensure errors in the Credential Type and Schema process are handled correctly and reported.
  * - ISS-073
    - Error Handling
    - Validate Error Handling in Trust Chain Validation
    - Ensure errors in the Trust Chain Validation process are handled correctly and reported.
  * - ISS-074
    - Error Handling
    - Validate Error Handling in Deferred Issuance
    - Ensure errors in the Deferred Issuance process are handled correctly and reported.
  * - ISS-075
    - Error Handling
    - Validate Error Handling in Notification Handling
    - Ensure errors in the Notification Handling process are handled correctly and reported.
  * - ISS-076
    - Error Handling
    - Validate Error Handling in User Authentication
    - Ensure errors in the User Authentication process are handled correctly and reported.
  * - ISS-077
    - Error Handling
    - Validate Error Handling in User Consent
    - Ensure errors in the User Consent process are handled correctly and reported.
  * - ISS-078
    - Error Handling
    - Validate Error Handling in User Notification
    - Ensure errors in the User Notification Process are handled correctly and reported.
  * - ISS-079
    - Error Handling
    - Validate Error Handling in User Attribute Set Update
    - Ensure errors in the User Attribute Set Update process are handled correctly and reported.
  * - ISS-080
    - Error Handling
    - Validate Error Handling in Data Model/Format Update
    - Ensure errors in the Data Model/Format Update process are handled correctly and reported.
  * - ISS-081
    - Error Handling
    - Validate Error Handling in Credential Expiry
    - Ensure errors in the Credential Expiry process are handled correctly and reported.
  * - ISS-082
    - Error Handling
    - Validate Error Handling in Credential Re-Issuance
    - Ensure errors in the Credential Re-Issuance process are handled correctly and reported.
  * - ISS-083
    - Error Handling
    - Validate Error Handling in Credential Binding
    - Ensure errors in the Credential Binding process are handled correctly and reported.
  * - ISS-084
    - Error Handling
    - Validate Error Handling in Credential Trust Evaluation
    - Ensure errors in the Credential Trust Evaluation process are handled correctly and reported.
  * - ISS-085
    - Error Handling
    - Validate Error Handling in Credential Metadata Retrieval
    - Ensure errors in the Credential Metadata Retrieval process are handled correctly and reported.
  * - ISS-086
    - Error Handling
    - Validate Error Handling in Credential Discovery
    - Ensure errors in the Credential Discovery process are handled correctly and reported.
  * - ISS-087
    - Error Handling
    - Validate Error Handling in Credential Offer Evaluation
    - Ensure errors in the Credential Offer Evaluation process are handled correctly and reported.
  * - ISS-088
    - Error Handling
    - Validate Error Handling in Credential Offer Acceptance
    - Ensure errors in the Credential Offer Acceptance process are handled correctly and reported.
  * - ISS-089
    - Error Handling
    - Validate Error Handling in Credential Offer Rejection
    - Ensure errors in the Credential Offer Rejection process are handled correctly and reported.
  * - ISS-090
    - Error Handling
    - Validate Error Handling in Credential Offer Revocation
    - Ensure errors in the Credential Offer Revocation process are handled correctly and reported.
  * - ISS-091
    - Error Handling
    - Validate Error Handling in Credential Offer Expiry
    - Ensure errors in the Credential Offer Expiry process are handled correctly and reported.
  * - ISS-092
    - Error Handling
    - Validate Error Handling in Credential Offer Renewal
    - Ensure errors in the Credential Offer Renewal process are handled correctly and reported.
  * - ISS-093
    - Error Handling
    - Validate Error Handling in Credential Offer Update
    - Ensure errors in the Credential Offer Update process are handled correctly and reported.
  * - ISS-094
    - Error Handling
    - Validate Error Handling in Credential Offer Validation
    - Ensure errors in the Credential Offer Validation process are handled correctly and reported.
  * - ISS-095
    - Error Handling
    - Validate Error Handling in Credential Offer Verification
    - Ensure errors in the Credential Offer Verification process are handled correctly and reported.
  * - ISS-096
    - Error Handling
    - Validate Error Handling in Credential Offer Confirmation
    - Ensure errors in the Credential Offer Confirmation process are handled correctly and reported.
  * - ISS-097
    - Error Handling
    - Validate Error Handling in Credential Offer Notification
    - Ensure errors in the Credential Offer Notification Process are handled correctly and reported.
  * - ISS-098
    - Error Handling
    - Validate Error Handling in Credential Offer Communication
    - Ensure errors in the Credential Offer Communication process are handled correctly and reported.
  * - ISS-099
    - Error Handling
    - Validate Error Handling in Credential Offer Transmission
    - Ensure errors in the Credential Offer Transmission process are handled correctly and reported.
  * - ISS-100
    - Error Handling
    - Validate Error Handling in Credential Offer Reception
    - Ensure errors in the Credential Offer Reception process are handled correctly and reported.
  * - ISS-101
    - Error Handling
    - Validate Error Handling in Credential Offer Processing
    - Ensure errors in the Credential Offer Processing process are handled correctly and reported.
  * - ISS-102
    - Error Handling
    - Validate Error Handling in Credential Offer Handling
    - Ensure errors in the Credential Offer Handling process are handled correctly and reported.
  * - ISS-103
    - Error Handling
    - Validate Error Handling in Credential Offer Management
    - Ensure errors in the Credential Offer Management process are handled correctly and reported.
  * - ISS-104
    - Error Handling
    - Validate Error Handling in Credential Offer Administration
    - Ensure errors in the Credential Offer Administration process are handled correctly and reported.
  * - ISS-105
    - Error Handling
    - Validate Error Handling in Credential Offer Control
    - Ensure errors in the Credential Offer Control process are handled correctly and reported.
  * - ISS-106
    - Error Handling
    - Validate Error Handling in Credential Offer Oversight
    - Ensure errors in the Credential Offer Oversight process are handled correctly and reported.
  * - ISS-107
    - Error Handling
    - Validate Error Handling in Credential Offer Supervision
    - Ensure errors in the Credential Offer Supervision process are handled correctly and reported.
  * - ISS-108
    - Error Handling
    - Validate Error Handling in Credential Offer Monitoring
    - Ensure errors in the Credential Offer Monitoring process are handled correctly and reported.
  * - ISS-109
    - Error Handling
    - Validate Error Handling in Credential Offer Evaluation
    - Ensure errors in the Credential Offer Evaluation process are handled correctly and reported.
  * - ISS-110
    - Error Handling
    - Validate Error Handling in Credential Offer Assessment
    - Ensure errors in the Credential Offer Assessment process are handled correctly and reported.

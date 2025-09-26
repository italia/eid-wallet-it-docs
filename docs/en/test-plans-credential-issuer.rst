.. include:: ../common/common_definitions.rst

Credential Issuer Test Matrix
---------------------------------

This section provides the set of test cases designed for technical implementers and development teams responsible for creating and deploying Credential Issuer solutions. It is also intended for assessment bodies inspecting and validating the implementations of Credential Issuer solutions.



.. list-table::
  :class: longtable
  :widths: 15 15 35 35
  :header-rows: 1

  * - Test Case ID
    - Purpose
    - Description
    - Expected Result
  * - CI_001
    - Trust, Security
    - Entity Configuration publication
    - Federation Entity publishes its own Entity Configuration in the .well-known/openid-federation endpoint.
  * - CI_002
    - Trust, Interoperability
    - Entity Configuration response media type check
    - The Entity Configuration HTTP Response is set to media type to application/entity-statement+jwt.
  * - CI_003
    - Trust, Security
    - Entity Configuration cryptography
    - The Entity Configuration is cryptographically signed
  * - CI_004
    - Trust, Security
    - Public Key inclusion in Entity Configuration and Subordinate Statement
    - The Entity Configuration and the Subordinate Statement issued by the immediate superior both include the public part of the key.
  * - CI_005
    - Trust, Security
    - Entity Configuration's Trust Marks
    - The Entity Configuration contains one or more Trust Marks.
  * - CI_006
    - Trust, Interoperability
    - Entity Configurations parameters
    - Entity Configurations have in common these parameters: iss, sub, iat, exp, jwks, metadata.
  * - CI_007
    - Trust, Security
    - Credential Issuer Discovery
    - The Credential Issuer exposes a well-known endpoint hosting its Entity Configuration.
  * - CI_008
    - Trust, Interoperability
    - Credential Issuer metadata
    - Credential Issuer successfully provides the following metadata types: federation_entity, Oauth_authorization_server and openVCI_credential_issuer
  * - CI_009
    - Trust, Interoperability
    - Inclusion of openVCI_credential_verifier Metadata in User Authentication via Wallet
    - When the (Q)EAA Providers authenticate users through their Wallet Instance, the openVCI_credential_verifier metadata is included in addition to the required metadata parameters.
  * - CI_010
    - Issuance, Interoperability
    - Credential Offer URI Structure
    - Credential Issuer generates a Credential Offer consisting of a single URI query parameter named "credential_offer"ensuring the URL is well-formed and contains only this parameter for the offer data.
  * - CI_011
    - Issuance, Interoperability
    - Credential Offer Delivery Methods
    - Credential Offer URL is successfully embedded in QR codes or included as clickable href buttons in HTML pages.
  * - CI_012
    - Issuance, Interoperability
    - Credential Offer Mandatory Parameters
    - Credential Offer contains all three mandatory parameters (credential_issuer, credential_configuration_ids, and grants) with valid values
  * - CI_013
    - Issuance, Interoperability
    - Credential Offer Grants Parameter Structure
    - The grants parameter successfully contains an authorization_code object that includes both required sub-parameters (issuer_state and authorization_server) with appropriate values
  * - CI_014
    - Issuance, Interoperability
    - Credential Object Compilation
    - Credential Issuer ensures the Credential Object is properly compiled with all required fields, correct formatting, and valid data structures before delivery
  * - CI_015
    - Issuance, Security
    - PAR Request Object Signature Validation
    - Credential Issuer successfully validates the Request Object signature
  * - CI_015a
    - Issuance, Security
    - PAR Request Object Algorithm Header Processing
    - Credential Issuer uses the algorithm specified in the alg header parameter (:rfc:`9126`/:rfc:`9101`) to validate the Request Object Signature
  * - CI_015b
    - Issuance, Security
    - PAR Wallet Attestation Public Key Retrieval
    - Credential Issuer successfully retrieves the public key from the Wallet Attestation's cnf.jwk claim
  * - CI_015c
    - Issuance, Security
    - PAR JWT Key Identifier Reference
    - The Credential Issuer successfully references the correct key via the kid JWT header parameter
  * - CI_015d
    - Issuance, Security
    - PAR Cryptographic Signature Integrity Validation
    - The Credential Issuer successfully complete cryptographic signature integrity before proceeding with any further validations
  * - CI_016
    - Issuance, Interoperability
    - PAR HTTP POST Parameter Encoding
    - Credential Issuer successfully processes HTTP POST requests with message body parameters encoded in application/x-www-form-urlencoded format;
  * - CI_017
    - Issuance, Interoperability
    - PAR Scope and Authorization Details Interpretation
    - When a request contains both scope value and authorization_details parameter, Credential Issuer processes each parameter independently
  * - CI_017a
    - Issuance, Interoperability
    - PAR Authorization Details
    - When both scope and authorization_details request the same Credential type, Credential Issuer follows the specifications given by the authorization_details object
  * - CI_018
    - Issuance, Security
    - PAR Request Object Signature Validation
    - Credential Issuer successfully validates the Request Object signature using the algorithm from the alg header parameter and the public key from the Wallet Attestation's cnf.jwk claim (referenced by kid), confirming signature integrity (:rfc:`9126`/:rfc:`9101`)
  * - CI_019
    - Issuance, Security
    - PAR Algorithm Compliance Check
    - Credential Issuer verifies the signing algorithm in the alg header matches one of the approved algorithms listed in the Cryptographic Algorithms section; rejects requests with non-compliant algorithms and returns appropriate error.
  * - CI_020
    - Issuance, Security
    - PAR Client ID Consistency Validation
    - Credential Issuer confirms the client_id in the PAR request body exactly matches the client_id claim in the Request Object; mismatched values trigger request rejection with clear error message.
  * - CI_021
    - Issuance, Security
    - Issuer-Client ID Matching in the PAR request
    - Credential Issuer validates that the iss claim in the Request Object matches the client_id claim within the same Request Object (:rfc:`9126`/:rfc:`9101`); discrepancies result in request denial.
  * - CI_022
    - Issuance, Security
    - PAR Audience Claim Verification
    - Credential Issuer confirms the aud claim in the Request Object equals the Credential Issuer's own identifier (:rfc:`9126`/:rfc:`9101`); incorrect audience values cause immediate request rejection.
  * - CI_023
    - Issuance, Security
    - PAR Request URI Parameter Rejection
    - Credential Issuer detects and rejects any PAR request containing the request_uri parameter (:rfc:`9126`), returning an appropriate error response indicating the parameter is not supported.
  * - CRFCI_024
    - Issuance, Security
    - PAR Mandatory Parameters Validation
    - Credential Issuer verifies all mandatory HTTP parameters are present in the Request Object and validates their values against the defined Table specifications (derived from :rfc:`9126`); missing or invalid parameters trigger structured error responses.
  * - CI_025
    - Issuance, Security
    - PAR Token Expiration Check
    - Credential Issuer validates the Request Object has not expired by checking the exp claim against current time; expired tokens are rejected with timestamp-related error messages.
  * - CI_026
    - Issuance, Security
    - PAR Token Issuance Time Validation
    - Credential Issuer confirms the iat claim represents a past timestamp
  * - CI_026a
    - Issuance, Security
    - Recommended PAR Token Issuance Time rejection
    - Credential Issuer reject requests where iat is more than 5 minutes from current time (:rfc:`9126`); timing violations result in "invalid_request" errors.
  * - CI_027
    - Issuance, Security
    - PAR Replay Attack Prevention
    - Credential Issuer successfully checks that the jti claim in the Request Object has not been used before by the Wallet Instance identified by the client_id.
  * - CI_028
    - Issuance, Security, Interoperability
    - OAuth Client Attestation PoP Validation
    - .Credential Issuer successfully validates the OAuth-Client-Attestation-PoP parameter according to Section 4 of [`OAUTH-ATTESTATION-CLIENT-AUTH`_], confirming proof-of-possession and rejecting invalid attestations with detailed error responses.
  * - CI_029
    - Issuance, Trust
    - Wallet Instance Trustworthiness Verification
    - Credential Issuer successfully verifies the trustworthiness and indirect Federation membership of the Wallet Instance through comprehensive Wallet Attestation validation
  * - CI_030
    - Issuance, Trust
    - Wallet Provider Federation Membership Validation
    - Credential Issuer confirms the Wallet Provider (issuer of the Wallet Attestation) is a recognized and trusted Federation member by checking Federation registries and trust lists;
  * - CI_031
    - Issuance, Security
    - Wallet Attestation Cryptographic Signature Validation
    - Credential Issuer successfully validates the cryptographic signature of the Wallet Attestation using the Wallet Provider's public key, ensuring signature integrity and authenticity;
  * - CI_032
    - Issuance, Security
    - Wallet Attestation Expiration Check
    - Credential Issuer verifies the Wallet Attestation has not expired at verification time by checking timestamp claims against current time
  * - CI_033
    - Issuance, Security
    - Wallet Attestation Attested Cryptographic Key Acceptance
    - Credential Issuer accepts and uses only cryptographic keys that are properly derived from the attested Wallet Instance during the credential issuance process;
  * - CI_034
    - Issuance, Security
    - Wallet Attestation Device Security and Compliance Verification
    - Credential Issuer relies on Wallet Attestation claims to confirm the Wallet Instance operates on a secure, trusted device that meets the Issuer's required security standards;
  * - CI_035
    - Issuance, Trust
    - Wallet Provider Trust Chain Evaluation
    - Credential Issuer successfully evaluates the complete Trust Chain of the Wallet Attestation's issuer (Wallet Provider)
  * - CI_036
    - Issuance, Trust, Interoperability
    - Federation Metadata Retrieval
    - Credential Issuer successfully uses Federation API endpoints (.well-known/openid-federation, /fetch) to retrieve current metadata and configurations of Federation participants, including Wallet Providers
  * - CI_037
    - Issuance, Trust, Interoperability
    - Wallet Provider Trust Establishment
    - Credential Issuer establishes trust in the Wallet Provider as an authorized Federation entity by querying Federation API endpoints (e.g., .well-known/openid-federation, /fetch) and validating the provider's federation status through official channels and trust verification processes.
  * - CI_038
    - Issuance, Interoperability
    - One-Time Request URI Provision in the PAR response
    - Credential Issuer generates and provides a unique, one-time use request_uri value
  * - CI_039
    - Issuance, Security
    - Request URI Client Binding in the PAR response
    - Issued request_uri value is cryptographically bound to the specific client_id provided in the Request Object
  * - CI_040
    - Issuance, Security
    - Recommended PAR Response Request URI Validity Duration
    - request_uri validity time is set to less than one minute
  * - CI_041
    - Issuance, Security
    - PAR response Request URI Cryptographic Random Value Integration
    - Generated request_uri includes a cryptographic random value of at least 128 bits
  * - CI_042
    - Issuance, Security
    - Recommended PAR response Request URI Length Limitation
    - Complete request_uri doesn't exceed 512 ASCII characters
  * - CI_043
    - Issuance, Interoperability
    - PAR Response Successful Verification Response
    - When verification is successful, Credential Issuer returns an HTTP response with 201 status code
  * - CI_044
    - Issuance, Interoperability
    - JSON PAR Response Structure
    - HTTP response message body uses application/json media type (:rfc:`8259`) and includes the required top-level parameters
  * - CI_044a
    - Issuance, Security
    - PAR Response request_uri Parameter
    - HTTP response includes request_uri parameter containing the generated one-time authorization URI
  * - CI_044b
    - Issuance, Security
    - PAR Response expires_in Parameter
    - HTTP response includes expires_in parameter specifying the validity duration in seconds
  * - CI_045
    - Issuance, Interoperability
    - PAR Response HTTP Status Code table
    - When PAR request processing encounters errors, the Credential Issuer responds as defined in :rfc:`9126`, according to the HTTP Status Codes
  * - CI_046
    - Issuance, Security and Privacy
    - User Identity Verification during authorization request
    - Authorization Server successfully verifies the identity of the User who owns the credential through appropriate authentication mechanisms, confirming user ownership before proceeding with credential authorization
  * - CI_047
    - Issuance, Security
    - Request URI One-Time Use and Expiration in the Authorization Request
    - Credential Issuer treats each request_uri value as single-use only and successfully rejects any expired requests
  * - CI_048
    - Issuance, Security
    - Optional Duplicate Request Tolerance in the Authorization Request
    - Credential Issuer allow duplicate requests when they result from User reloading or refreshing their user-agent (derived from :rfc:`9126`)
  * - CI_049
    - Issuance, Security
    - PAR Request Identification in the Authorization Request
    - Credential Issuer successfully identifies and correlates each authorization request as a direct result of a previously submitted PAR (derived from :rfc:`9126`)
  * - CI_050
    - Issuance, Security
    - Request URI Parameter Requirement of the Authorization Request
    - Credential Issuer rejects all Authorization Requests that do not contain the request_uri parameter, since PAR is the exclusive method for passing Authorization Requests from the Wallet Instance (derived from :rfc:`9126`).
  * - CI_051
    - Issuance, Security
    - CieID High-Level Authentication
    - PID Provider successfully performs User authentication based on CieID scheme with LoAHigh (CIE L3)
  * - CI_052
    - Issuance, Security and Privacy
    - User Consent for PID Issuance
    - PID Provider obtains explicit User consent before proceeding with PID issuance
  * - CI_053
    - Issuance, Privacy
    - Optional Contact Details Collection
    - PID Provider MAY request User's contact details (email, phone number) for sending notifications about the issued PID
  * - CI_054
    - Presentation, Issuance Security
    - PID-Based User Authentication
    - (Q)EAA Provider successfully performs User authentication by requesting and validating a valid PID from the Wallet Instance
  * - CI_055
    - Presentation, Issuance, Interoperability
    - OpenID4VP Protocol Usage
    - (Q)EAA Provider uses OpenID4VP protocol to request PID presentation from the Wallet Instance
  * - CI_056
    - Presentation, Issuance, Security
    - Presentation Request Delivery
    - (Q)EAA Provider successfully provides the presentation request to the Wallet
  * - CI_057
    - Issuance, Privacy
    - Optional Contact Details Collection for Credentials
    - Credential Issuers request User's contact details (email, phone number) for sending notifications about issued Digital Credential(s)
  * - CI_058
    - Issuance, Interoperability
    - Authorization Response parameters validation
    - Credential Issuer successfully sends an authorization code response to the Wallet Instance that includes all three required parameters
  * - CI_058a
    - Issuance, Security
    - Authorization Response code parameter validation
    - Authorization code response includes the authorization code parameter
  * - CI_058b
    - Issuance, Security
    - Authorization Response state parameter validation
    - Authorization code response includes the state parameter matching the original request
  * - CI_058c
    - Issuance, Security
    - Authorization Response iss parameter validation
    - Authorization code response includes the iss parameter identifying the issuer
  * - CI_059
    - Issuance, Interoperability
    - Authorization Response HTTP Status Code table
    - When Authorization Response encounter errors, the Authorization Server redirects the User to the redirect_uri HTTP status code 302 according to the HTTP Status Code table
  * - CI_060
    - Issuance, Security
    - Authorization Code Issuance Verification of the Token request
    - Credential Issuer ensures the Authorization code is issued to the authenticated Wallet Instance (:rfc:`6749`) and has not been replayed
  * - CI_061
    - Issuance, Security
    - Authorization Code Validity and Usage Check of the Token Request
    - Credential Issuer verifies the Authorization code is valid and has not been previously used (:rfc:`6749`).
  * - CI_062
    - Issuance, Security
    - Redirect URI Matching Validation of the Token Request
    - Credential Issuer confirms the redirect_uri exactly matches the value included in the previous Request Object (see Section 3.1.3.1. of [`OIDC`_]).
  * - CI_063
    - Issuance, Security
    - DPoP Proof JWT Validation of the Token Request
    - Credential Issuer successfully validates the DPoP Proof JWT, according to (:rfc:`9449`) Section 4.3.
  * - CI_064
    - Issuance, Interoperability
    - Access Token Provision in the token response
    - Credential Issuer provides the Wallet Instance with a valid Access Token upon successful authorization
  * - CI_065
    - Issuance, Interoperability
    - Optional Refresh Token Provision
    - If supported by the Credential Issuer, a Refresh Token is provided to the Wallet Instance
  * - CI_066
    - Issuance, Security
    - DPoP Key Binding for Access Token and Refresh Token
    - Both Access Token and Refresh Token (when issued) are cryptographically bound to the DPoP key
  * - CI_067
    - Issuance, Interoperability
    - Token Response HTTP Status Code table
    - When any errors occur during the validation of the Token Request, the Authorization Server return an error response as defined in :rfc:`6749`, according to the HTTP Status Code Table
  * - CI_068
    - Issuance, Interoperability
    - c_nonce Provision
    - Credential Issuer provides a c_nonce value to the Wallet Instance
  * - CI_069
    - Issuance, Security
    - C_nonce Format and Security
    - The c_nonce parameter is provided as a string value with sufficient unpredictability to prevent guessing attacks, serving as a cryptographic challenge that the Wallet Instance uses to create proof of possession of the key (proof claim)
  * - CI_070
    - Issuance, Security
    - C_nonce Reusability and Renewal
    - The received c_nonce value can be reused by the Wallet Instance to create multiple proofs until the Credential Issuer provides a new c_nonce value
  * - CI_071
    - Issuance, Interoperability
    - JWT Proof Required Claims Validation
    - JWT proof successfully includes all required claims as specified in the Token Request table
  * - CI_072
    - Issuance, Security
    - Batch JWT Proof Required Claims Validation
    - Credential Issuer successfully verify that the jwk attribute in each key proof is unique
  * - CI_073
    - Issuance, Interoperability
    - Credential Request Key Proof Type Declaration
    - Key proof is explicitly typed using appropriate header parameters defined for the respective proof type
  * - CI_074
    - Issuance, Security
    - Asymmetric Algorithm Requirement in the Credential Request
    - The header parameter alg indicates a registered asymmetric digital signature algorithm and is never set to none
  * - CI_075
    - Issuance, Security
    - Credential Request Public Key Signature Verification
    - Signature on the key proof is successfully verified using the public key specified in the header parameter
  * - CI_076
    - Issuance, Security
    - Private Key Header Exclusion in the Credential Request
    - Header parameters do not contain any private key material
  * - CI_077
    - Issuance, Security
    - c_nonce Matching in the Credential Request
    - When a c_nonce value was previously provided by the server, the nonce claim in the JWT exactly matches this c_nonce value
  * - CI_078
    - Issuance, Security
    - JWT Temporal Validity in the Credential Request
    - The creation time of the JWT (via iat claim or server-managed timestamp through nonce claim) falls within the server's acceptable time window
  * - CI_079
    - Issuance, Interoperability
    - Credential Registration for Revocation
    - Credential Issuer registers all issued Credentials in a revocation registry for potential future revocation needs
  * - CI_080
    - Issuance, Interoperability
    - Recommended Fresh Cryptographic Key Generation in the Credential Request
    - Credential Issuer registers all issued Credentials in a revocation registry for potential future revocation needs
  * - CI_081
    - Issuance, Security
    - Recommended Deferred Flow support
    - When the requested Credential cannot be issued immediately and requires more time, the Credential Issuer supports the Deferred Flow
  * - CI_081a
    - Issuance, Security
    - Deferred Flow batch issuance consistency
    - When using the Deferred Flow for batch issuance, the same transaction_id allows retrieval of all Credentials requested in the batch.
  * - CI_082
    - Issuance, Security
    - DPoP JWT Proof and Access Token Validation in the Credential Response
    - Credential Issuer successfully validates the DPoP JWT Proof based on the steps defined in Section 4.3 of (:rfc:`9449`) procedures and confirms the Access Token is valid and suitable for the requested Credent
  * - CI_083
    - Issuance, Security
    - Key Material Proof of Possession Validation in the Credential Response
    - Credential Issuer validates the proof of possession for the key material to which the new Credential will be bound, according to `OpenID4VCI`_ Section 8.2.2.
  * - CI_084
    - Issuance, Security
    - Credential Creation and Binding in the Credential Response
    - When all validation checks succeed, Credential Issuer creates a new Credential cryptographically bound to the validated key material and provides it to the Wallet Instance
  * - CI_084a
    - Issuance, Security
    - Credential type check
    - Credential Issuer ensure the credential type matches the request before issuing the new Credential
  * - CI_085
    - Issuance, Interoperability
    - Credential Response Table of HTTP Status Codes
    - When the Credential Request does not contain a valid Access Token, the Credential Endpoint returns an error response such as defined in Section 3 of [:rfc:`6750`], according to the Table of HTTP Status Codes
  * - CI_086
    - Issuance, Interoperability
    - Unified Notification ID for Batch Operations
    - For batch-issued Digital Credentials, a single notification_id covers the entire batch-issued Credentials. The notification response applies to all Credentials, any partial failure is treated as a batch failure.
  * - CI_087
    - Issuance, Interoperability
    - Notification Response Table of HTTP Status Codes
    - When the Notification Request does not contain a valid Access Token, the Notification Endpoint returns an error response such as defined in Section 3 of [:rfc:`6750`], according to the Table of HTTP Status Codes
  * - CI_088
    - Issuance, Security
    - Access Token Scope Restriction
    - Access Token obtained through a Refresh Token flow is successfully limited to three specific endpoints: Deferred endpoint, Notification endpoint and Credential endpoint
  * - CI_088a
    - Issuance, Security
    - Deferred Endpoint Access Authorization
    - Access Token allows access to Deferred endpoint for obtaining new Digital Credentials after lead_time or readiness notification
  * - CI_088b
    - Issuance, Security
    - Notification Endpoint Access Authorization
    - Access Token allows access to Notification endpoint for notifying Digital Credential deletion to the Credential Issuer
  * - CI_089c
    - Issuance, Security
    - Credential Endpoint Access Authorization
    - Access Token allows access to Credential endpoint for Digital Credential refresh/re-issuance of existing credentials
  * - CI_090
    - Issuance, Security
    - DPoP-Bound Refresh Token Security
    - Refresh Tokens are bound to DPoP keys to mitigate stolen token impact
  * - CI_091
    - Issuance,Interoperability
    - OAuth Client Attestation PoP Validation for Refresh
    - Credential Issuer successfully validates the OAuth-Client-Attestation-PoP parameter based on Section 4 of [OAUTH-ATTESTATION-CLIENT-AUTH]
  * - CI_092
    - Issuance, Security
    - DPoP Proof JWT Validation for Refresh
    - Credential Issuer validates the DPoP Proof JWT according to (:rfc:`6949`) Section 4.3.
  * - CI_093
    - Issuance, Security
    - Refresh Token Validity and Key Binding Check
    - Credential Issuer verifies the Refresh Token is not expired, not revoked, and is bound to the same DPoP keys used in the DPoP Proof JWT
  * - CI_094
    - Issuance, Security
    - Access Token Generation and Bound
    - When all validation checks succeed, Credential Issuer generates new Access Token and new Refresh Token, both bound to the DPoP key
  * - CI_095
    - Issuance, Security
    - Successful Refresh Token Response
    - Both the Access Token and the Refresh Token are sent back to the Wallet Instance
  * - CI_096
    - Issuance, Security
    - Invalid Refresh Token Error Handling
    - When the Refresh Token is expired or invalid, Credential Issuer issues an error response with error type member set to invalid_grant
  * - CI_097
    - Issuance, Security
    - Refresh Token Confidentiality Protection
    - Confidentiality of Refresh Tokens is guaranteed both in transit and storage through appropriate encryption and secure handling mechanisms
  * - CI_098
    - Issuance, Security
    - TLS-Protected Refresh Token Transmission
    - All token transmissions use TLS-protected connections, ensuring encrypted communication channels for token exchange
  * - CI_099
    - Issuance, Security
    - Refresh Token Security Properties
    - Refresh tokens are generated with unguessable values and protected from modification through cryptographic integrity mechanisms
  * - CI_100
    - Issuance, Security
    - Cryptographic Refresh Token Binding
    - Authorization Servers cryptographically bind Refresh Tokens to the Wallet Instance according to :rfc:`9449` specifications
  * - CI_101
    - Issuance, Security
    - Consistent DPoP Key Binding between Refresh and Access token
    - Access Tokens and Refresh Tokens are bound to the same DPoP key
  * - CI_102
    - Issuance, Security
    - DPoP Proof Requirement for Refresh Token
    - DPoP Proof is required for all refresh token operations to obtain new Access Tokens
  * - CI_103
    - Issuance, Security
    - Consistent DPoP Key Usage for Refresh Token
    - The same DPoP key is used to generate Access Token DPoP Proofs across all Credential Requests
  * - CI_104
    - Issuance, Security
    - Refresh Token Usage Duration Management
    - Credential Issuers manage and limit the duration for which refresh tokens can be used to refresh credentials versus requiring complete re-issuance flow restart. As specified in `OPENID4VC-HAIP`_
  * - CI_105
    - Issuance, Security
    - Recommended Re-issued Credential Expiration Alignment
    - New Digital Credentials obtained through re-issuance flow maintain the same expiration as the refreshed credential
  * - CI_106
    - Issuance, Security
    - Post-Expiration Issuance Requirement
    - Once a Digital Credential expires, Users complete the entire issuance process again to obtain new Digital Credentials
  * - CI_107
    - Issuance, Security
    - Consistent Issuer Requirement for Re-Issuance
    - New Digital Credentials are issued exclusively by the same Credential Issuers that originally provided the existing credentials to the same Wallet Instance
  * - CI_108
    - Issuance, Security
    - Refresh Token Scope Limitation for Re-issuance
    - Access Tokens obtained through Refresh Token flows are restricted from issuing Digital Credentials not already present in the Wallet Instance (first-time-issuance)
  * - CI_109
    - Issuance, Security
    - Re-issuance Process Scope Limitation
    - The re-issuance process is limited to two specific update types: Data model/format technical updates and User's attribute set updates
  * - CI_110
    - Issuance, Security
    - Not Recommended Technical Update User Interaction
    - For data model/format technical updates, the replacement and storage of Digital Credentials don't require direct user involvement
  * - CI_111
    - Issuance, Security and Privacy
    - Attribute Update User Authorization
    - For User's attribute set updates, the Wallet Instance informs the User about attribute data set changes and requests explicit User authorization before storing the new Digital Credential
  * - CI_112
    - Issuance, Security
    - Expiry Date Consistency for Re-Issuance
    - Newly issued Digital Credentials maintain the same expiry date as the previous credential version
  * - CI_113
    - Issuance, Privacy
    - Optional Out-of-Band Re-Issuance Update Notification
    - When a Digital Credential requires updating, Credential Issuers send notifications to Users through registered out-of-band communication channels (email, SMS, push notifications)
  * - CI_114
    - Issuance, Security
    - First-Time Issuance Restriction for Refresh Tokens
    - Access Tokens obtained through Refresh Token flows are prohibited from being used for first-time issuance of Digital Credentials
  * - CI_115
    - Issuance, Security
    - Mandatory Expiry Date Consistency after Re-Issuance
    - Credential Issuer sets the same expiry date for re-issued Digital Credentials as the previous credential version
  * - CI_116
    - Issuance, Privacy
    - User Consent for Attribute-Based Re-issuance
    - For re-issuance processes triggered by attribute changes, User consent is obtained before storing the new Digital Credential


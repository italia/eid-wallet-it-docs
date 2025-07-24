Remote Credential Presentation Test Matrix
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section defines the test cases about the remote presentation flow.

.. note::
  References about official OpenID4VP test plans will update this section in future releases.

.. list-table::
  :class: longtable
  :widths: 15 15 35 35
  :header-rows: 1

  * - Test Case ID
    - Purpose
    - Description
    - Expected Result
  * - RPR-01
    - Same Device Flow
    - Verify HTTP redirect (302) URL.
    - Wallet Instance receives correct URL.
  * - RPR-02
    - Cross Device Flow
    - Verify QR Code generation for Wallet Instance.
    - Wallet Instance scans QR Code successfully.
  * - RPR-03
    - Cross Device Flow
    - Verify QR Code contains correct URL parameters.
    - Wallet Instance retrieves URL with parameters.
  * - RPR-04
    - Cross Device Flow
    - Test QR Code scanning in low light.
    - QR Code is scanned successfully.
  * - RPR-05
    - Cross Device Flow
    - Verify QR Code error correction level.
    - QR Code remains readable if damaged.
  * - RPR-06
    - Cross Device Flow
    - Test QR Code scanning with different devices.
    - QR Code is scanned successfully.
  * - RPR-07
    - Request URI Method
    - Test `request_uri_method` as `post`.
    - Wallet Instance sends metadata via POST.
  * - RPR-08
    - Request URI Method
    - Test `request_uri_method` as `get`.
    - Wallet Instance fetches Request Object via GET.
  * - RPR-09
    - Request URI Method
    - Test absence of `request_uri_method`.
    - Wallet Instance defaults to GET method.
  * - RPR-10
    - Metadata
    - Verify parameters match openid credential verifier metadata.
    - Only allowed parameters will be considered.
  * - RPR-11
    - User Consent
    - Test eligibility of a credential verifier in requesting user attributes.
    - User can modify data selection about optional attributes.
  * - RPR-12
    - Authorization Response
    - Test sending of Presentation Response.
    - Relying Party receives and validates response with state and nonce.
  * - RPR-13
    - Authorization Response
    - Verify response encryption.
    - Response is encrypted using Relying Party's public key.
  * - RPR-14
    - Error Handling
    - Test invalid Request Object handling.
    - Authorization Error Response is sent.
  * - RPR-15
    - Error Handling
    - Verify error logging by Wallet Instance.
    - Errors are logged appropriately.
  * - RPR-16
    - Error Handling
    - Test recovery from `server_error`.
    - User prompted to retry or scan new QR code.
  * - RPR-17
    - Relying Party Response
    - Verify successful Response handling.
    - User session is updated, redirect URI provided.
  * - RPR-18
    - Relying Party Response
    - Test absence of `redirect_uri`.
    - Error response is returned.
  * - RPR-19
    - Redirect URI
    - Test redirection to Relying Party's endpoint.
    - User is redirected correctly.
  * - RPR-20
    - Redirect URI
    - Verify handling of invalid `redirect_uri`.
    - Error response is returned.
  * - RPR-21
    - User Consent
    - Verify display of Relying Party's identity.
    - Identity is displayed clearly to Holder.
  * - RPR-22
    - User Consent
    - Test user consent revocation.
    - User can revoke consent before submission.
  * - RPR-23
    - Credential Presentation
    - Verify response format compliance.
    - Each Credential adheres to specified format.
  * - RPR-24
    - Authorization Response
    - Test handling of response timeouts.
    - Retries must be successful unless response is acquired.
  * - RPR-25
    - Error Handling
    - Verify handling of malformed claims in presentation payload.
    - Authorization Error Response is sent.
  * - RPR-26
    - Error Handling
    - Verify handling of malformed claims in presented credentials.
    - Authorization Error Response is sent.
  * - RPR-27
    - Error Handling
    - Test handling of expired requests.
    - Holder is notified of expiration.
  * - RPR-28
    - Relying Party Response
    - Verify inclusion of response code.
    - Response code is cryptographically random.
  * - RPR-29
    - Relying Party Response
    - Test handling of invalid response codes.
    - Error response is returned.
  * - RPR-30
    - Status Endpoint
    - Verify handling of unauthorized access.
    - Unauthorized access is denied.
  * - RPR-31
    - Status Endpoint
    - Test handling of invalid session IDs.
    - Error response is returned.
  * - RPR-32
    - Redirect URI
    - Verify handling of expired sessions.
    - Error response is returned.
  * - RPR-33
    - Redirect URI
    - Test handling of server errors.
    - Error response is returned.
  * - RPR-34
    - Same Device Flow
    - Verify handling of slow network conditions.
    - Wallet Instance retries or notifies user.
  * - RPR-35
    - Request URI Method
    - Test handling of large metadata payloads.
    - Metadata is sent successfully.
  * - RPR-36
    - Presentation Response
    - Verify handling of large response payloads.
    - Response is sent successfully.
  * - RPR-37
    - Presentation Response
    - Test handling of response encryption failures.
    - Error response is returned.
  * - RPR-38
    - Error Handling
    - Verify handling of invalid signatures.
    - Authorization Error Response is sent.
  * - RPR-39
    - Error Handling
    - Test handling of invalid nonce values.
    - Error response is returned.
  * - RPR-40
    - Relying Party Response
    - Verify handling of malformed responses.
    - Error response is returned.
  * - RPR-41
    - Relying Party Response
    - Test handling of missing response parameters.
    - Error response is returned.
  * - RPR-42
    - Status Endpoint
    - Verify handling of session timeouts.
    - Error response is returned.
  * - RPR-43
    - Status Endpoint
    - Test handling of invalid status codes.
    - Error response is returned.
  * - RPR-44
    - Redirect URI
    - Verify handling of invalid user sessions.
    - Error response is returned.
  * - RPR-45
    - Redirect URI
    - Test handling of unavailable services.
    - Error response is returned.
  * - RPR-46
    - Same Device Flow
    - Verify handling of user cancellations.
    - User can cancel the process.
  * - RPR-47
    - Cross Device Flow
    - Test QR Code scanning with different apps.
    - QR Code is scanned successfully.
  * - RPR-48
    - Cross Device Flow
    - Verify QR Code scanning with different lighting.
    - QR Code is scanned successfully.
  * - RPR-49
    - Request URI Method
    - Test handling of unsupported content types.
    - Error response is returned.
  * - RPR-50
    - User Consent
    - Verify user notification of consent changes.
    - User is informed about consent changes.
  * - RPR-51
    - User Consent
    - Test user consent for sensitive data.
    - User can consent to sensitive data.
  * - RPR-52
    - Authorization Response
    - Verify handling of response decryption failures.
    - Error response is returned.
  * - RPR-53
    - Authorization Response
    - Test handling of response integrity checks.
    - Response integrity is verified.
  * - RPR-54
    - Relying Party Response
    - Verify handling of response validation failures.
    - Error response is returned.
  * - RPR-55
    - Relying Party Response
    - Test handling of response processing errors.
    - Error response is returned.
  * - RPR-56
    - Protected Resource Endpoint
    - Verify handling of unauthorized session access.
    - Unauthorized access is denied.
  * - RPR-57
    - Redirect URI
    - Verify handling of invalid redirect parameters.
    - Error response is returned.
  * - RPR-58
    - Redirect URI
    - Test handling of redirect failures.
    - Error response is returned.
  * - RPR-59
    - Same Device Flow
    - Verify handling of user interruptions.
    - User can resume or cancel the process.
  * - RPR-60
    - Request URI Method
    - Test handling of invalid HTTP methods.
    - Error response is returned.
  * - RPR-61
    - User Consent
    - Verify user notification of consent revocation.
    - User is informed about consent revocation.
  * - RPR-62
    - User Consent
    - Test user consent for optional data.
    - User can consent to optional data.
  * - RPR-63
    - Authorization Response
    - Verify handling of response signature failures.
    - Error response is returned.
  * - RPR-64
    - Authorization Response
    - Test handling of response format errors.
    - Error response is returned.
  * - RPR-65
    - Error Handling
    - Verify handling of invalid JWT signatures.
    - Authorization Error Response is sent.
  * - RPR-66
    - Error Handling
    - Test handling of invalid JWT claims.
    - Error response is returned.
  * - RPR-67
    - Relying Party Response
    - Verify handling of response parsing errors.
    - Error response is returned.
  * - RPR-68
    - Relying Party Response
    - Test handling of response timeout errors.
    - Error response is returned.
  * - RPR-69
    - Status Endpoint
    - Verify handling of session expiration.
    - Error response is returned.
  * - RPR-70
    - Status Endpoint
    - Test handling of session renewal errors.
    - Error response is returned.
  * - RPR-71
    - Redirect URI
    - Verify handling of redirect loop errors.
    - Error response is returned.
  * - RPR-72
    - Redirect URI
    - Test handling of redirect security errors.
    - Error response is returned.
  * - RPR-73
    - Same Device Flow
    - Verify handling of user timeouts.
    - User is notified of timeout.
  * - RPR-74
    - Cross Device Flow
    - Test QR Code scanning with different devices.
    - QR Code is scanned successfully.
  * - RPR-75
    - Cross Device Flow
    - Verify QR Code scanning with different apps.
    - QR Code is scanned successfully.
  * - RPR-76
    - Request URI Method
    - Test handling of unsupported HTTP methods.
    - Error response is returned.

.. include:: ../common/common_definitions.rst


Signature Evaluation Test Matrix
------------------------------------------

.. _signature-evaluation-testcases:

This section provides the common set of test cases for Wallet Solutions, Relying Parties and Credential Issuers evaluating any signed statements, be these assertions, requests, attestation or Credentials.

.. list-table::
  :class: longtable
  :widths: 15 15 35 35
  :header-rows: 1

  * - Test Case ID
    - Purpose
    - Description
    - Expected Result
  * - ATT-001
    - Discovery, Security
    - Evaluation of the issuer
    - Entities evaluating signed statements establish trust with the issuer and assess its compliance. Undiscoverable Issuers within the federation or unlinkable to any known Trust Anchor, halt any protocol communications.
  * - ATT-002
    - Discovery, Security
    - Evaluation of the signature
    - Entities evaluate signed statements by verifying the signature with the issuer's cryptographic material, provided it is trusted through a well-known Trust Anchor. Any untrusted cryptographic material or invalid signatures halt protocol communications.
  * - ATT-003
    - Algorithm Verification
    - Verify that the algorithm specified in the header matches the one used for cryptographic operations.
    - The algorithm in the header must match the cryptographic operation.
  * - ATT-004
    - Appropriate Algorithms
    - Ensure only algorithms listed as MUST or RECOMMENDED in :ref:`algorithms:Cryptographic Algorithms` are used. Algorithms listed as MUST NOT (including ``none``) are rejected. Cipher suites and hash functions not profiled in that section follow the ACN *Linee guida funzioni crittografiche*. Edwards-curve and post-quantum algorithms are not required by the current profile.
    - Only approved algorithms are accepted; deprecated or unlisted algorithms are rejected.
  * - ATT-005
    - Signature Validation
    - Validate all cryptographic operations and reject if any fail.
    - All signatures must be valid; any failure results in rejection.
  * - ATT-006
    - Key Entropy
    - Cryptographic keys and fresh secrets provide at least 128 bits of security strength as defined in NIST SP 800-57 Part 1. Asymmetric keys used with ES256/ESP256 are P-256 keys generated inside the Keystore or WSCD CSPRNG. Nonces, ``jti``, ``state`` and similar values are CSPRNG output of at least 128 bits and are not sequential.
    - Keys and secrets meet the entropy minima; weak, undersized, sequential or software-forged keys are rejected. A third party verifies key type and length and, where the platform exposes it, that the key is inside secure hardware (Android ``KeyInfo.isInsideSecureHardware`` / iOS Secure Enclave token).
  * - ATT-006a
    - Key Entropy
    - PKCE ``code_verifier``
    - The ``code_verifier`` is 43 to 128 unreserved characters as required by :rfc:`7636`, generated with a CSPRNG.
  * - ATT-006b
    - Key Entropy
    - MRTD and challenge nonces
    - Challenge identifiers and MRTD PoP nonces have at least 128 bits of entropy, as required for eID Substantial Authentication with MRTD Verification.
  * - ATT-006c
    - Key Entropy
    - No imported weak keys
    - The Wallet Provider rejects Key Attestations for keys that were imported into the Keystore, generated outside the Keystore/WSCD, or whose length does not match the algorithm (for example ES256 with a non-P-256 key).
  * - ATT-007
    - Issuer Validation
    - Validate that the cryptographic keys belong to the issuer.
    - Keys must be verified as belonging to the issuer.
  * - ATT-008
    - Audience Validation
    - Validate the audience claim to ensure the token is used by the intended party.
    - Audience claim must match the intended recipient.
  * - ATT-009
    - Claim Trust
    - Do not trust received claims without validation.
    - Claims must be validated; untrusted claims are rejected.
  * - ATT-010
    - Explicit Typing
    - Use explicit typing to prevent COSE/JOSE confusion.
    - Typing must be explicit and validated.
  * - ATT-011
    - Cross-JWT Confusion
    - Prevent COSE/JOSE from being used in unintended contexts.
    - COSE/JOSE must be contextually validated to prevent misuse.
  * - ATT-012
    - Substitution Attacks
    - Ensure COSE/JOSE are not substituted across different contexts.
    - COSE/JOSE must be validated for context-specific use.
  * - ATT-013
    - Issued At Validation
    - Verify that the `issued at` parameter is set to the current time, allowing a grace period not exceeding 120 seconds.
    - The `issued at` value must be within 120 seconds of the current time.
  * - ATT-014
    - Expiration Validation
    - Ensure the `expiration` time is greater than the `issued at` time.
    - The `expiration` time must be later than the `issued at` time.
  * - ATT-015
    - Data Model validation
    - Ensure JOSE/COSE type matches with the defined data model.
    - The parameters or claims, their values and the schema used to represent them are compliant with the data model.



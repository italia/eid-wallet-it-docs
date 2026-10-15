.. include:: ../common/common_definitions.rst
.. Included via wallet-instance-functionalities.rst at title level '=' (document title).


Key Attestation Issuance
=================================

This section describes how the Wallet Provider issues Key Attestations.

Use of the :term:`Key Attestation APIs (OEM)` is defined in :ref:`wallet-solution-requirements:Use of Key Attestation APIs (OEM)`.

.. plantuml:: plantuml/wallet-attestation-issuance.puml
    :width: 99%
    :alt: The figure illustrates the Sequence Diagram for Key Attestations acquisition.
    :caption: `Sequence Diagram for Key Attestations acquisition. <https://www.plantuml.com/plantuml/svg/fLNVRoCr47xtNp7oFP1AUvL0WeTAe8jAQIlG4Ltlu86WQ7OzoLhPZ1VRcrB-UcntcztwN7GLBr7i_UR7VDzuvftpQFrmw0GEtl1mgCcALYk2hJ6-DdyByTKg87IZUsJl13RUM92V75a9w61mmQ2V421_nwuZ3xSSN7D32OLz3yzHFzC3BBsd0FBQC2nNjov1z-WTl76zrRpRMI9-RlSZ7NL3mRkddTN-0Ux8nfl90POTPEcjh3bgHHPgRFR4AfdMpLw8MD7R7qB65_21_Xh8UK1WkWVJatrCrhVersp3Lst90K9UJQH97z5Jh5o8y3Dwl6ofsOFUmgLzwBtPMUnRtS0DMdMFbfAZDN_47IoaRCVRpPuUDXvtKfvLK2Ak0cG5EJNf4qIlU4JTOTtHF9LhubWFEJ1CO2mWrEYR5imM6akAs6li8CI67hLTk3Fm1ce2JD59WUOycvXrJBOVwitNKbOm7gq-flFv-Na54uGp28SAXR1iF84vaetiLK4KUFFBxVNDn-iFLrVlnIE5kOpQGPGv9kzRWfz8ZM8bQapjKJDex-107XLw5CGgHHev2M4cmQLa4tjNJaActWW_2JcnDuEchoEvqwsYPovA2WHqqsbYluc9RLfqhKpzU7Up_ERRxnOdPnNyCP5NvlFFCoY6-8z-MvdLccVTvlIEqGys18Jl8PuMYrA65PHRDB-EqeRxfxJGkujonLjZvzth7Dcee8Wce-6SC_q4tU0JLCerrsPW5LiraGR9UfAbQ9GYPtChfDlv-5ANhApH2jv-rkpRpjmdKyAcFJqKCVLCd6LZsVkKVMFf9RqdHwEQGaIRO9dN7R_Zc4QnvcWvrLmmW5E7GExPRRmPmLAEwXSyLEbkabPHLZHrZY9x-jUxaJdy4kPIMg-cwlzrI1B_q_9B6oLYNqrWvgr88h4gZuUyxyOfTI7bpDaOwiLOXUmgAB_w2gQ9i-RI8vyDdSV3VNey6sUw8SRRQ5M-Fv9rftpw3dqWz12ApwYO9l8TiO9PeVb8Vd_Q5U5KGNbPw6t-ka4xqApZXjF_a4fBuXZ-Ap4upJlul6Pn5I1iFCstm6_HvDaMA7_CcO_nfY6yVnp2PTEYccLeISiYSj8knarD7Kr2uMj-gTjcZYuj5TfIp1TWmOlh3JiI-KAS7OEXU4UiXaFtBm00>`_


.. .. figure:: ../../images/wallet_instance_acquisition.svg
..   :figwidth: 100%
..   :align: center
..   :target: https://www.plantuml.com/plantuml/svg/XLHDRnCn4BtxLupS0waKBaXmg0HgL4fRWL3K5hX4YYRhoUue6tknPxU4Nu-zJRFRui1b5TjlFjwRUJaFWbxQRQsm5MVRxOgygjWGh9sJbVkbNZKHm0KtQ4KfBCHvqDy2UGqOe0qHFqA0_e5rJG8tDWZQWdeKDWqyHtsaZWkAAA7Ii-pWZdn_CvlVXCSOb00deV5ioz8JsMoPkNST6_Ammc93rlIXgsAZb4gjlVuGIv_1BVriAGWWM7e0rv17OMT1AfI5zV6LFGL0s6UTnNvd8XIanoNMtA5G8g9K_EppNbHKR83NSE5tZRZIOrDn0TVepGDwWi-qWuMznn8cMbVxs-M6Tal1KkjJu03O8TUugacDCr-HJKscfYnGKz4s7ck8eT0W-vJlSDidRDgLrbFuwzfp5mifvQqJ0jUHJoIcKI8u-N9pTNr_TNjv-LKzCdafAWT8eeDRWrG4dyWyAOVMW5i9iWMM05iID2Yeo9fKwK0crXdarzgwj19w4BGVLVpqo84sh3s5QXJGO_RQ3BU6neco0aPqKJDPMQR-bXM6IlTBSdSzU_FstUIGR0fPIK-pIVynxxcRB-nese5BYz9wYcNVGpfD9hcUff1TaV7rCD6XBPHmbkMeqjCW6JyvROaXa4z3r3hBBU-1mn0VMAfZ-QQG9pw5GUQ5pV4yedwl5vc-wCW6-IqVRTmTMVCV8iztSB17EkRjaOp-ujyjEOGj2sFDlydqjkZYRwFQmBRCZdJmoB3ttrCC2WqwPH_pgkUXkJdaaJdTunQFm1UUZc_6o9h79G-Diu5U6dPyZl7gdAnfj_KV

..   Sequence Diagram for Wallet App Attestation acquisition

**Step 1**: The User initiates a new operation that necessitates the acquisition of a Key Attestation.

**Steps 2-3**: The Wallet Instance MUST:

  1. Verify the existence of Cryptographic Hardware Keys. If none exist, Wallet Instance re-initialization is required (:ref:`WP_140a <wallet-instance-optional-testcases>`).
  2. Verify the Wallet Provider's federation membership and retrieve its metadata (:ref:`WP_023 <wallet-instance-testcases>`).

**Steps 4-6 (Nonce Retrieval)**: The Wallet Instance requests a ``nonce`` value from the :ref:`wallet-provider-endpoint:Wallet Solution Nonce Endpoint` of the Wallet Provider Backend (:ref:`WP_140b <wallet-instance-optional-testcases>`). The ``nonce`` is required to be unpredictable and serves as the main defense against replay attacks.

The ``nonce`` MUST ensure single-use within a predetermined time frame.

Upon a successful request, the Wallet Provider generates and returns the nonce value to the Wallet Instance.

**Steps 7-9 (Credential key generation)**: The Wallet Instance MUST generate one or a batch of asymmetric Credential key pairs to be attested (``key_pub_1``, ``key_priv_1``, ..., ``key_pub_n``, ``key_priv_n``) only after the ``nonce`` is available.

On Android, the Wallet Instance MUST generate each key pair through the Key Attestation API. It MUST set the attestation challenge to the UTF-8 octets of the ``nonce``. The API returns the public key and a signed ``key_attestation`` for that key. The Wallet Instance MUST NOT use ``client_data_hash`` as that challenge. ``client_data_hash`` depends on the JWK thumbprint of the key, and the platform binds the challenge at key generation time.

On iOS, the Wallet Instance MUST generate each key pair in the Secure Enclave. The integrity assertion for each key is requested after ``client_data_hash`` has been computed.

**Step 10**: The Wallet Instance performs the following actions (:ref:`WP_140c <wallet-instance-optional-testcases>`):

* Creates ``client_data``, a JSON object that includes the ``nonce`` and a ``jwk_thumbprints`` field containing a JSON array of the JWK thumbprints corresponding to the public keys ``(key_pub_1,...,key_pub_n)``.
* Computes ``client_data_hash`` by applying the ``SHA256`` algorithm to the ``client_data``.

Below is a non-normative example of the ``client_data`` JSON object.

.. code-block:: json

  {
    "nonce": "i4ThI2Jhbu81i8mqyWEuDG5t",
    "jwk_thumbprints": ["vbeXJksM45xphtANnCiG6mCyuU4jfGNzopGuKvogg9c"]
  }


**Steps 11-12**: The Wallet Instance produces a ``hardware_signature`` value by signing the ``client_data_hash`` with the Wallet Hardware's private key, serving as a proof of possession for the Cryptographic Hardware Keys (:ref:`WP_140d <wallet-instance-optional-testcases>`).

The Key Attestation Request MUST NOT include a top-level ``integrity_assertion``. The Wallet Provider checks the revocation status of the Wallet Instance Attestation before issuing a Key Attestation. On iOS, the per-key integrity assertion is carried inside ``keys_to_attest``, because that platform does not provide a key attestation API.

**Steps 13-16**: The Wallet Instance constructs ``keys_to_attest`` as a JSON array of JWTs. The header and claims of each JWT are defined in :ref:`wallet-provider-endpoint:Key Attestation Element`.

* On Android, when Key Attestation APIs (OEM) are used, each JWT carries the ``key_attestation`` obtained at key generation in ``wscd_key_attestation.attestation``.
* On iOS, the Wallet Instance requests from the Device Integrity Service an ``integrity_assertion`` for each key, bound to ``client_data_hash``, and places that value in ``wscd_key_attestation.integrity_assertion``.

Each JWT MUST be signed with the private key of the Credential key pair it attests.

**Steps 17-18 (Key Attestation Issuance Request)**: The Wallet Instance:

* Constructs the Key Attestation Request in the form of a JWT. This JWT includes ``keys_to_attest``, ``hardware_signature``, ``nonce``, ``hardware_key_tag``, ``cnf``, ``platform`` and other configuration related parameters (see :ref:`Table of the Key Attestation Request Body <table_ka_request_claim>`). The Key Attestation Request MUST be signed using the private key related to the public key included in the request, using the ``cnf`` parameter (first element of ``keys_to_attest``) (:ref:`WP_140–141 <wallet-instance-optional-testcases>`).
* Submits the Key Attestation Request to the :ref:`wallet-provider-endpoint:Key Attestation Issuance Endpoint` of the Wallet Provider Backend.

The Wallet Instance MUST send the signed Key Attestation Request JWT as an ``assertion`` parameter in the body of an HTTP request to the Wallet Provider's :ref:`wallet-provider-endpoint:Key Attestation Issuance Endpoint` (:ref:`WP_142 <wallet-instance-optional-testcases>`).

**Steps 19-24**: The Wallet Provider Backend evaluates the Key Attestation Request and MUST perform the following checks (:ref:`WP_143 <wallet-instance-optional-testcases>`):

  1. The request MUST include all required HTTP header parameters as defined in :ref:`wallet-provider-endpoint:Key Attestation Issuance Request` (:ref:`WP_143a <wallet-instance-optional-testcases>`).
  2. The signature of the Key Attestation Request MUST be valid and verifiable using the provided ``jwk`` (:ref:`WP_143b <wallet-instance-optional-testcases>`).
  3. The ``nonce`` value MUST have been generated by the Wallet Provider and not previously used (:ref:`WP_143c <wallet-instance-optional-testcases>`).
  4. A valid and currently registered Wallet Instance associated with the provided ``hardware_key_tag`` MUST exist (:ref:`WP_143d <wallet-instance-optional-testcases>`). The Wallet Provider MUST reject the request when the Wallet Instance Attestation of that Wallet Instance is revoked.
  5. The signature of each JWT in ``keys_to_attest`` MUST be validated using the ``jwk`` of that element. If ``wscd_key_attestation.attestation`` is present, the Wallet Provider MUST validate it according to the device manufacturer's guidelines, as defined in :ref:`wallet-solution-requirements:Use of Key Attestation APIs (OEM)` (:ref:`WP_143h <wallet-instance-optional-testcases>`). The challenge embedded in that attestation MUST be equal to the UTF-8 octets of the ``nonce``. The attested public key MUST match the ``cnf`` JWK of the same element. If ``wscd_key_attestation.integrity_assertion`` is present, the Wallet Provider MUST validate it according to the device manufacturer's guidelines.
  6. The ``client_data`` MUST be reconstructed using the ``nonce`` and their respective thumbprint JWKs ``[key_pub_1,...,key_pub_n]``. The ``hardware_signature`` parameter value is then validated using the registered Cryptographic Hardware Key's public key associated with the Wallet Instance (:ref:`WP_143e <wallet-instance-optional-testcases>`).
  7. The device in use MUST be free of known security flaws and meet the minimum security requirements defined by the Wallet Provider.
  8. The URL in the ``iss`` parameter MUST match the Wallet Provider's URL identifier (:ref:`WP_143g <wallet-instance-optional-testcases>`).

Upon successful completion of all checks, the Wallet Provider issues a Key Attestation valid for at least one month.

**Step 25 (Key Attestation Issuance Response)**: Upon successful completion, the Wallet Provider MUST return a confirmation response using status code set with ``200`` and Content-Type ``application/json``. The response MUST contain the Key Attestations signed by the Wallet Provider using the JWT format. The Wallet Instance MUST perform security and integrity verification of the Key Attestations received, along with the trust verification already evaluated about the Issuer (:ref:`WP_030–031 <wallet-instance-testcases>`).


Below is a non-normative example of the response.

.. code-block:: http

  HTTP/1.1 200 OK
  Content-Type: application/json

  {
    "key_attestation": "omppc3N1ZXJBdXRohEOhASaiBE...dElEAnFlbGVtZW50SWRl"
  }



.. include:: ../common/common_definitions.rst


Wallet App and Wallet Unit Attestation Issuance
===============================================

This section describes how the Wallet Provider issues a Wallet App and a Wallet Unit Attestations.

.. plantuml:: plantuml/wallet-attestation-issuance.puml
    :width: 99%
    :alt: The figure illustrates the Sequence Diagram for Wallet App and Wallet Unit Attestations acquisition.
    :caption: `Sequence Diagram for Wallet App and Wallet Unit Attestations acquisition. <https://www.plantuml.com/plantuml/svg/fLPDR-Cs4BtpLmouXoQ0SYdG7WAqM2DDaw35rjYicui1OoIEBS8ogPAKq_JNbwF84ItJsnHx2KBgpSUyUJFqHn_GXMxN2Eo2DTsk92TghGZMreRI_Yt4T_E8q9LkqGGli0hMWLnuSXBGG-UZGJiYG3vXqr201nDTcufw5BOj7AD-enUOXK0H5BGrC9i_-1wwnU3XWs-TDfkD8pB7Th_GNbSKlGVQE1rUu94StumESEeWczxSsRrMvA34Qaj6zQPbjHM2AxhwEMPy3P_fhuvy00H3ps1RSg_9XXh3qhZuLJloy3IR0He5JuiPC45wZu6uPY7Ydy7NJKtL5lGQRjnB6-p6OLlh2kxHgMTq14p8qdp13Ln8MG-tgoszh09kfBmi84TPqGS-8OK_0Nl5FUe6ouRILEx8S2KK8L0vKcI2nWPYB6XHEmWMIWBiGv42RM0WRM5qI5FWL3d3jYkbB60uEBsF-URZ6Q2sfXsvDDxQklvGsiweGwnPsqv3lPckqg39THfUE6C3WTsJurOKiRVmuVU7k_ilTvzlRp-9rtvCrQ0zi5h0hY7K1B-IElISURPbG6r01myx2gWme22ZEDA1u1Xcr8sKnl88o54LlSJYdnuvKfD0-wy3S-EjecCN6NeZkceqcR3Yn5Or-dhrtA7ifVruF_l-XnyltXmMaBJkaglBckDvyrmxBhDvVKNnSpjVcaJlNcyCXix54F0JyEdYubnPnTcC2yYFK78zQcLC6eE_plYKaXNAKouOSW0cjEl3uAtGUtAi5ocNvbNFmK9F6lJMOsTpHcCaWKtWRJ4pobcjuEfa_DUDVMRuP8J5g3LUfKDjs_-eRH4ZCeQHa-AOA3p4pHN6bcDX6GDu4mKSUJvi6Ew5b4ExC_R5yM8HYYObKkE9oT9_F0v4uRk8Ua_N5z_OTNOoEdgN01ZxlpZB-ChmHaPbzmRhxOf33clhMih4oJY5NnLiSP9R0VcvBc3S8akJ6zHpowKuj-l7pVj8Ha6I_tJrVZgy2Nmg8Fiei98cFs90Uz16itJqFwJwTRcF_olHUMqsS5g4k8qGVXVIRVydcnnj--p72P4SBTtMl3JpTjaEvQ6vpkIHAUNv36uSCJJv6IJILopHbs-jyIIchrboZ0RY8ndLxPf_0G00>`_


.. .. figure:: ../../images/wallet_instance_acquisition.svg
..   :figwidth: 100%
..   :align: center
..   :target: https://www.plantuml.com/plantuml/svg/XLHDRnCn4BtxLupS0waKBaXmg0HgL4fRWL3K5hX4YYRhoUue6tknPxU4Nu-zJRFRui1b5TjlFjwRUJaFWbxQRQsm5MVRxOgygjWGh9sJbVkbNZKHm0KtQ4KfBCHvqDy2UGqOe0qHFqA0_e5rJG8tDWZQWdeKDWqyHtsaZWkAAA7Ii-pWZdn_CvlVXCSOb00deV5ioz8JsMoPkNST6_Ammc93rlIXgsAZb4gjlVuGIv_1BVriAGWWM7e0rv17OMT1AfI5zV6LFGL0s6UTnNvd8XIanoNMtA5G8g9K_EppNbHKR83NSE5tZRZIOrDn0TVepGDwWi-qWuMznn8cMbVxs-M6Tal1KkjJu03O8TUugacDCr-HJKscfYnGKz4s7ck8eT0W-vJlSDidRDgLrbFuwzfp5mifvQqJ0jUHJoIcKI8u-N9pTNr_TNjv-LKzCdafAWT8eeDRWrG4dyWyAOVMW5i9iWMM05iID2Yeo9fKwK0crXdarzgwj19w4BGVLVpqo84sh3s5QXJGO_RQ3BU6neco0aPqKJDPMQR-bXM6IlTBSdSzU_FstUIGR0fPIK-pIVynxxcRB-nese5BYz9wYcNVGpfD9hcUff1TaV7rCD6XBPHmbkMeqjCW6JyvROaXa4z3r3hBBU-1mn0VMAfZ-QQG9pw5GUQ5pV4yedwl5vc-wCW6-IqVRTmTMVCV8iztSB17EkRjaOp-ujyjEOGj2sFDlydqjkZYRwFQmBRCZdJmoB3ttrCC2WqwPH_pgkUXkJdaaJdTunQFm1UUZc_6o9h79G-Diu5U6dPyZl7gdAnfj_KV

..   Sequence Diagram for Wallet App Attestation acquisition

**Step 1**: The User initiates a new operation that necessitates the acquisition of a Wallet App and Wallet Unit Attestations.

**Steps 2-4**: The Wallet Instance MUST:

  1. Verify the existence of Cryptographic Hardware Keys. If none exist, Wallet Instance re-initialization is required (:ref:`WP_140a <wallet-instance-optional-testcases>`).
  2. Generate an asymmetric credential key pair to be attested in Wallet Unit Attestation (``key_pub``, ``key_priv``).
  3. Generate an ephemeral asymmetric key pair for Wallet App Attestation (``ephemeral_key_pub``, ``ephemeral_key_priv``), linking the public key to the attestation  (:ref:`WP_026 <wallet-instance-testcases>`).
  4. Verify the Wallet Provider's federation membership and retrieve its metadata (:ref:`WP_023 <wallet-instance-testcases>`).

**Steps 5-7 (Nonce Retrieval)**: The Wallet Instance requests a ``nonce`` value from the :ref:`wallet-provider-endpoint:Wallet Solution Nonce Endpoint` of the Wallet Provider Backend (:ref:`WP_140b <wallet-instance-optional-testcases>`). The ``nonce`` is required to be unpredictable and serves as the main defense against replay attacks. 

The ``nonce`` MUST ensures single-use within a predetermined time frame.

Upon a successful request, the Wallet Provider generates and returns the nonce value to the Wallet Instance.

**Step 8**: The Wallet Instance performs the following actions (:ref:`WP_140c <wallet-instance-optional-testcases>`):

* Creates two JSON objects ``client_data_waa``, and ``client_data_wua`` each containing the ``nonce`` and the thumbprint of their respective JWKs (``ephemeral_key_pub``, ``key_pub``).
* Computes the corresponding hashes, ``client_data_hash_waa``, and ``client_data_hash_wua``  by applying the ``SHA256`` algorithm to the ``client_data_waa``, and ``client_data_wua``.

Below is a non-normative example of the ``client_data_waa`` JSON object.

.. code-block:: json

  {
    "nonce": "i4ThI2Jhbu81i8mqyWEuDG5t",
    "jwk_thumbprint": "vbeXJksM45xphtANnCiG6mCyuU4jfGNzopGuKvogg9c"
  }


**Steps 9-12**: The Wallet Instance:

* produces an ``hardware_signature`` value by signing the ``client_data_hash_waa`` and ``client_data_hash_wua`` with the Wallet Hardware's private key, serving as a proof of possession for the Cryptographic Hardware Keys (:ref:`WP_140d <wallet-instance-optional-testcases>`).
* requests the Device Integrity Service to create an ``integrity_assertion`` value for Wallet App Attestation linked to the ``client_data_hash_waa``.
* receives a signed ``integrity_assertion`` value for Wallet App Attestation from the Device Integrity Service, authenticated by the OEM (:ref:`WP_140e <wallet-instance-optional-testcases>`).

.. note:: 
  ``integrity_assertion`` is a custom payload generated by Device Integrity Service, signed by device OEM and encoded in base64 to have uniformity between different devices.

.. note::
   In the case of Android OS, the flow continues based on **Steps 13-16**, otherwise for the case of iOS, the flow continues based on **Steps 17-20**.

**Steps 13-16**: The Wallet Instance:

*  requests the Key Attestation API to create an ``key_attestation`` value linked to the ``client_data_hash_wua``.
*  receives a signed ``key_attestation`` value from the Key Attestation API, authenticated by the OEM.
*  generate ``attested_key`` value by signing the ``key_attestation`` using the private key of the initially generated credential key pair (``priv_key``). 

**Steps 17-20**: The Wallet Instance:

*  requests the Device Integrity Service to create an ``integrity_assertion`` value linked to the ``client_data_hash_wua``.
*  receives a signed ``integrity_assertion`` value for the Wallet Unit Attestation from the Device Integrity Service, authenticated by the OEM.
*  generate ``attested_key`` value by signing the ``integrity_assertion`` that is obtained for the Wallet Unit Attestation using the private key of the initially generated credential key pair (``priv_key``). 

**Steps 21-22 (Wallet App and Wallet Unit Attestation Issuance Request)**: The Wallet Instance:

* Constructs the Wallet App and Wallet Unit Attestation Request in the form of a JWT. This JWT includes the ``integrity_assertion`` for Wallet App Attestation, ``attested_key``, ``hardware_signature``, ``nonce``, ``hardware_key_tag``, ``cnf`` and other configuration related parameters (see :ref:`Table of the Wallet App and Wallet Unit Attestation Request Body <table_waa_wua_request_claim>`) and is signed using the private key of the initially generated ephemeral key pair (:ref:`WP_140–141 <wallet-instance-optional-testcases>`).
* Submits the Wallet App and Wallet Unit Attestation Request to the :ref:`wallet-provider-endpoint:Wallet App and Wallet Unit Attestation Issuance Endpoint` of the Wallet Provider Backend.

.. note:: 
  ``attested_key`` contains a ``key_attestation`` object in case of Android and ``integrity_assertion`` in case of iOS.

The Wallet Instance MUST send the signed Wallet App and Wallet Unit Attestation Request JWT as an ``assertion`` parameter in the body of an HTTP request to the Wallet Provider's :ref:`wallet-provider-endpoint:Wallet App and Wallet Unit Attestation Issuance Endpoint` (:ref:`WP_142 <wallet-instance-optional-testcases>`).

**Steps 23-28**: The Wallet Provider Backend evaluates the Wallet App and Wallet unit Attestation Request and MUST perform the following checks (:ref:`WP_143 <wallet-instance-optional-testcases>`):

  1. The request MUST include all required HTTP header parameters as defined in :ref:`wallet-provider-endpoint:Wallet App and Wallet Unit Attestation Issuance Request` (:ref:`WP_143a <wallet-instance-optional-testcases>`).
  2. The signature of the Wallet App and Wallet Unit Attestation Request MUST be valid and verifiable using the provided ``jwk`` (:ref:`WP_143b <wallet-instance-optional-testcases>`).
  3. The ``nonce`` value MUST have been generated by the Wallet Provider and not previously used (:ref:`WP_143c <wallet-instance-optional-testcases>`).
  4. A valid and currently registered Wallet Instance associated with the provided MUST exist (:ref:`WP_143d <wallet-instance-optional-testcases>`).
  5. The signature of the ``attested_key`` parameter Must be first validated using the provided ``jwk`` and its value (``key_attestation`` in case of Android or ``integrity_assertion`` in case of iOS) MUST be validated according to the device manufacturer's guidelines.
  6. The ``client_data_waa`` MUST be reconstructed using the ``nonce`` and the ``jwk`` public key. The ``hardware_signature`` parameter value is then validated using the registered Cryptographic Hardware Key's public key associated with the Wallet Instance (:ref:`WP_143e <wallet-instance-optional-testcases>`).
  7. The ``integrity_assertion`` for Wallet App Attestation MUST be validated according to the device manufacturer's guidelines. The specific checks performed by the Wallet Provider are detailed in the operating system manufacturer's documentation (:ref:`WP_143f <wallet-instance-optional-testcases>`).
  8. The device in use MUST be free of known security flaws and meet the minimum security requirements defined by the Wallet Provider.
  9. The URL in the ``iss`` parameter MUST match the Wallet Provider's URL identifier (:ref:`WP_143g <wallet-instance-optional-testcases>`).

Upon successful completion of all checks, the Wallet Provider issues a Wallet App Attestation valid for less than 24 hours (:ref:`WP_144 <wallet-instance-optional-testcases>`), and a Wallet Unit Attestation valid for at least one month.

**Step 29 (Wallet App and Wallet Unit Attestation Issuance Response)**: Upon successful completion, the Wallet Provider MUST return a confirmation response using status code 200 and Content-Type ``application/json``, containing the Wallet App and Wallet Unit Attestations signed by the Wallet Provider. The Wallet provider MUST return the Wallet App Attestation in at least three formats: JWT, SD-JWT and mdoc. The Wallet Instance will then perform security and integrity verification of the Wallet App and Wallet Unit Attestations received in addition to trust verification of its Issuer (:ref:`WP_030–031 <wallet-instance-testcases>`).


Below is a non-normative example of the response.

.. code-block:: http

  HTTP/1.1 200 OK
  Content-Type: application/json

  {
    "wallet_attestations": [
      "wallet_app_attestations": [
        {
          "format": "jwt",
          "wallet_app_attestation": "ey..."
        },
        {
          "format": "dc+sd-jwt",
          "wallet_app_attestation": "ey..."
        },
        {
          "format": "mso_mdoc",
          "wallet_app_attestation": "omppc3N1ZXJBdXRohEOhASahG...ArQwggKwMIICVqADAgEC"
        }
      ],

      "wallet_unit_attestation": "omppc3N1ZXJBdXRohEOhASahG...ArQwggKwMIICVqADAgEC"
    ]
  }

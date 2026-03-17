.. include:: ../common/common_definitions.rst


Wallet Unit Attestation Issuance
=================================

This section describes how the Wallet Provider issues a Wallet Unit Attestations.

.. plantuml:: plantuml/wallet-attestation-issuance.puml
    :width: 99%
    :alt: The figure illustrates the Sequence Diagram for Wallet Unit Attestations acquisition.
    :caption: `Sequence Diagram for Wallet Unit Attestations acquisition. <https://www.plantuml.com/plantuml/svg/fLNVRzis47xdNt5W7-O0Qe0Ds1u2RAYHPKcmeJEQPdkO1-4adYt2yb4ZAMVPNp-IKIrPfRiMUp5CyRiVztt7kpVEe_NzlXNOUyFzlY8h6gq8DiRuolmjn5UhWD2rxf2z4rXxOq4-Eh8Iq47lWa4t8a3-ZcrB7kuvkEQQ4Wgx3avHFzCpBBsd0FBQC2nNzov1T-WTl7ATrRpTMY8-jVkH3hgcuDtJrch_30zauvVH0UOTpD9RMNFGYYnKME-8LJAjwfqGiQBNFuICh-0T_TMJyu30z0Ic8_kIh6_Ghzc6Mst90SBWz96rFwagqgKFw2ao84Ju6JnVDrJlG6_WsZvttcmjTeskuGwjUa9B4EbPytlSmaBAPlXQxkYvzBYLygA0784582kOKvIk87h50-eMgvQcgTmInxh8WM42Om6XGbytO3PGMrB4NcCB8JPqgEt2NO0tK15WYauAD9yZ86OVa-xwglnQoWA6ezM7TBwyl2nWXF0Cmg5I8ImRJs0EP2EBHH09NlroVtlt_lRTpSrRyKBbN5Rj8CeUY_0DmK-a1l4IHQRog1cqTx0dZmez2cAL8WtSX31Z0qZ99lQo70LDlH9-4d9aSG9DjmF9urT59ovoIWHqtMfYNyR4oWPT8rD_Fjmjl_dskyNHMG5_ZEJb-Vpp0d8XFjLtAxDQywJhdDuo-jw6WF0znDDYaSkmW7ohpZz7QQEmGrhetLM-uesnqovsZcnKK4IJmN3AcVu0BV43LCerLwPd5LisaGR9UfGbQvGYp-POIBVrySKkMLcZ5Rp-w0bkMlEKJ0dhvlXWnDWpSRODPUzIzhMbStgFZWOrXOWsqN9MTxp78OripT5oh3bZ0CSEWRbdLtepWAKSrCzuAAGyaLRHh6Xg7KNszAyF0tFuESobjBwSgl_L8Kdyn-NdDah4VY616MyP4ebLTZoS7RR3jBgISk9q27asPYRB0lAllu1nygmvzzWdm-Vby9HIBPrf-nYlr2h__K3M7VFfMlI1s7qWOKR9E9aVY1LC2fsFvhV7dH5E1UINXjxCNpbe1vfrt7Zw7r9fMHp2VoLwftaB7zSiRWA4ZQVfDlWjcfniWynbXlaORnp6kvTXd3VDgfc7vhJC8aVjOjpKtD4a5Bxc_-gwYSDhIvzeKt6o6CzxTPrXHsA-C2V7u42y8LRzllqN>`_


.. .. figure:: ../../images/wallet_instance_acquisition.svg
..   :figwidth: 100%
..   :align: center
..   :target: https://www.plantuml.com/plantuml/svg/XLHDRnCn4BtxLupS0waKBaXmg0HgL4fRWL3K5hX4YYRhoUue6tknPxU4Nu-zJRFRui1b5TjlFjwRUJaFWbxQRQsm5MVRxOgygjWGh9sJbVkbNZKHm0KtQ4KfBCHvqDy2UGqOe0qHFqA0_e5rJG8tDWZQWdeKDWqyHtsaZWkAAA7Ii-pWZdn_CvlVXCSOb00deV5ioz8JsMoPkNST6_Ammc93rlIXgsAZb4gjlVuGIv_1BVriAGWWM7e0rv17OMT1AfI5zV6LFGL0s6UTnNvd8XIanoNMtA5G8g9K_EppNbHKR83NSE5tZRZIOrDn0TVepGDwWi-qWuMznn8cMbVxs-M6Tal1KkjJu03O8TUugacDCr-HJKscfYnGKz4s7ck8eT0W-vJlSDidRDgLrbFuwzfp5mifvQqJ0jUHJoIcKI8u-N9pTNr_TNjv-LKzCdafAWT8eeDRWrG4dyWyAOVMW5i9iWMM05iID2Yeo9fKwK0crXdarzgwj19w4BGVLVpqo84sh3s5QXJGO_RQ3BU6neco0aPqKJDPMQR-bXM6IlTBSdSzU_FstUIGR0fPIK-pIVynxxcRB-nese5BYz9wYcNVGpfD9hcUff1TaV7rCD6XBPHmbkMeqjCW6JyvROaXa4z3r3hBBU-1mn0VMAfZ-QQG9pw5GUQ5pV4yedwl5vc-wCW6-IqVRTmTMVCV8iztSB17EkRjaOp-ujyjEOGj2sFDlydqjkZYRwFQmBRCZdJmoB3ttrCC2WqwPH_pgkUXkJdaaJdTunQFm1UUZc_6o9h79G-Diu5U6dPyZl7gdAnfj_KV

..   Sequence Diagram for Wallet App Attestation acquisition

**Step 1**: The User initiates a new operation that necessitates the acquisition of a Wallet Unit Attestation.

**Steps 2-3**: The Wallet Instance MUST:

  1. Verify the existence of Cryptographic Hardware Keys. If none exist, Wallet Instance re-initialization is required (:ref:`WP_140a <wallet-instance-optional-testcases>`).
  2. Generate one or batch of asymmetric credential key pair(s) to be attested in Wallet Unit Attestation (``key_pub_1``, ``key_priv_1``, ..., ``key_pub_n``, ``key_priv_n``).
  3. Verify the Wallet Provider's federation membership and retrieve its metadata (:ref:`WP_023 <wallet-instance-testcases>`).

**Steps 4-6 (Nonce Retrieval)**: The Wallet Instance requests a ``nonce`` value from the :ref:`wallet-provider-endpoint:Wallet Solution Nonce Endpoint` of the Wallet Provider Backend (:ref:`WP_140b <wallet-instance-optional-testcases>`). The ``nonce`` is required to be unpredictable and serves as the main defense against replay attacks. 

The ``nonce`` MUST ensure single-use within a predetermined time frame.

Upon a successful request, the Wallet Provider generates and returns the nonce value to the Wallet Instance.

**Step 7**: The Wallet Instance performs the following actions (:ref:`WP_140c <wallet-instance-optional-testcases>`):

* Creates ``client_data``, a JSON object that includes the ``nonce`` and a ``jwk_thumbprints`` field containing a JSON array of the JWK thumbprints corresponding to the public keys ``(key_pub_1,...,key_pub_n)`` .
* Computes ``client_data_hash`` by applying the ``SHA256`` algorithm to the ``client_data``.

Below is a non-normative example of the ``client_data`` JSON object.

.. code-block:: json

  {
    "nonce": "i4ThI2Jhbu81i8mqyWEuDG5t",
    "jwk_thumbprints": ["vbeXJksM45xphtANnCiG6mCyuU4jfGNzopGuKvogg9c"]
  }


**Steps 8-11**: The Wallet Instance:

* produces an ``hardware_signature`` value by signing the ``client_data_hash``  with the Wallet Hardware's private key, serving as a proof of possession for the Cryptographic Hardware Keys (:ref:`WP_140d <wallet-instance-optional-testcases>`).
* requests the Device Integrity Service to create an ``integrity_assertion`` value linked to the ``client_data_hash``.
* receives a signed ``integrity_assertion`` value for Wallet Instance from the Device Integrity Service, authenticated by the OEM (:ref:`WP_140e <wallet-instance-optional-testcases>`).

.. note:: 
  ``integrity_assertion`` is a custom payload generated by Device Integrity Service, signed by device OEM and encoded in base64 to have uniformity between different devices.

.. note::
   In the case of Android OS, the flow continues based on **Steps 12-15**, otherwise for the case of iOS, the flow continues based on **Steps 16-19**.

**Steps 12-15**: The Wallet Instance:

*  requests the Key Attestation API to create an ``key_attestation`` value for each ``client_data_hash`` per each ``key_pub``.
*  receives a signed ``key_attestation`` value from the Key Attestation API, authenticated by the OEM.
*  generate ``keys_to_attest`` value by signing the ``key_attestation`` using the private key of the initially generated credential key pair (``priv_key``). 

**Steps 16-19**: The Wallet Instance:

*  requests the Device Integrity Service to create an ``key_attestation`` value for each ``client_data_hash`` per each ``key_pub``.
*  receives a signed ``integrity_assertion`` value from the Device Integrity Service, authenticated by the OEM.
*  generate ``keys_to_attest`` value by signing the ``integrity_assertion`` that is obtained for the Wallet Unit Attestation using the private key of the initially generated credential key pair (``priv_key``). 

**Steps 20-21 (Wallet Unit Attestation Issuance Request)**: The Wallet Instance:

* Constructs the Wallet Unit Attestation Request in the form of a JWT. This JWT includes the ``integrity_assertion``, ``keys_to_attest``, ``hardware_signature``, ``nonce``, ``hardware_key_tag``, ``cnf``, ``platform``, ``wallet_solution_id``, ``wallet_solution_version`` and other configuration related parameters (see :ref:`Table of the Wallet Unit Attestation Request Body <table_wua_request_claim>`) and is signed using the private key that it is public key illustrated in the request through ``cnf`` (first element of ``keys_to_attest``) (:ref:`WP_140–141 <wallet-instance-optional-testcases>`).
* Submits the Wallet Unit Attestation Request to the :ref:`wallet-provider-endpoint:Wallet Unit Attestation Issuance Endpoint` of the Wallet Provider Backend.

.. note:: 
  ``keys_to_attest`` contains a ``key_attestation`` object in case of Android and ``integrity_assertion`` in case of iOS.

The Wallet Instance MUST send the signed Wallet Unit Attestation Request JWT as an ``assertion`` parameter in the body of an HTTP request to the Wallet Provider's :ref:`wallet-provider-endpoint:Wallet Unit Attestation Issuance Endpoint` (:ref:`WP_142 <wallet-instance-optional-testcases>`).

**Steps 22-27**: The Wallet Provider Backend evaluates the Wallet unit Attestation Request and MUST perform the following checks (:ref:`WP_143 <wallet-instance-optional-testcases>`):

  1. The request MUST include all required HTTP header parameters as defined in :ref:`wallet-provider-endpoint:Wallet Unit Attestation Issuance Request` (:ref:`WP_143a <wallet-instance-optional-testcases>`).
  2. The signature of the Wallet Unit Attestation Request MUST be valid and verifiable using the provided ``jwk`` (:ref:`WP_143b <wallet-instance-optional-testcases>`).
  3. The ``nonce`` value MUST have been generated by the Wallet Provider and not previously used (:ref:`WP_143c <wallet-instance-optional-testcases>`).
  4. A valid and currently registered Wallet Instance associated with the provided ``hardware_key_tag`` MUST exist (:ref:`WP_143d <wallet-instance-optional-testcases>`).
  5. The signature of the ``keys_to_attest`` parameter Must be first validated using the provided ``jwk`` and its value (``key_attestation`` in case of Android or ``integrity_assertion`` in case of iOS) MUST be validated according to the device manufacturer's guidelines.
  6. The ``client_data`` MUST be reconstructed using the ``nonce`` and their respective thumbprint JWKs ``[key_pub_1,...,key_pub_n]``. The ``hardware_signature`` parameter value is then validated using the registered Cryptographic Hardware Key's public key associated with the Wallet Instance (:ref:`WP_143e <wallet-instance-optional-testcases>`).
  7. The ``integrity_assertion`` MUST be validated according to the device manufacturer's guidelines. The specific checks performed by the Wallet Provider are detailed in the operating system manufacturer's documentation (:ref:`WP_143f <wallet-instance-optional-testcases>`).
  8. The device in use MUST be free of known security flaws and meet the minimum security requirements defined by the Wallet Provider.
  9. The URL in the ``iss`` parameter MUST match the Wallet Provider's URL identifier (:ref:`WP_143g <wallet-instance-optional-testcases>`).

Upon successful completion of all checks, the Wallet Provider issues a Wallet Unit Attestation valid for at least one month.

**Step 28 (Wallet Unit Attestation Issuance Response)**: Upon successful completion, the Wallet Provider MUST return a confirmation response using status code 200 and Content-Type ``application/json``, containing the Wallet Unit Attestations signed by the Wallet Provider in the JWT format. The Wallet Instance will then perform security and integrity verification of the Wallet Unit Attestations received in addition to trust verification of its Issuer (:ref:`WP_030–031 <wallet-instance-testcases>`).


Below is a non-normative example of the response.

.. code-block:: http

  HTTP/1.1 200 OK
  Content-Type: application/json

  {
    "wallet_unit_attestation": "omppc3N1ZXJBdXRohEOhASaiBE...dElEAnFlbGVtZW50SWRl"
  }

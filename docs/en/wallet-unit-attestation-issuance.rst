.. include:: ../common/common_definitions.rst


Wallet Unit Attestation Issuance
================================

This section describes how the Wallet Provider issues a Wallet Unit Attestation.

.. plantuml:: plantuml/wallet-unit-attestation-issuance.puml
    :width: 99%
    :alt: The figure illustrates the Sequence Diagram for Wallet Unit Attestation acquisition.
    :caption: `Sequence Diagram for Wallet Unit App Attestation acquisition. <https://www.plantuml.com/plantuml/svg/jPH1Rziy38Rl-XM4UlXImDzbm7OeiA51rxN5XYreskqI8A1jrXRYI9v4fyk_d-IwjHmetM5O3e4jltf9FgHqxXWjTzj6OCT6TzkShAXLIV1W3EVcbn3_BRn25Qf5pKvWmSQ2l7Ta9Q23pZ-8TbI0_85DGmmtsblhWdeLjYrCLPzf3tDcyY9MHiDySUDwwGRPmObhhT9LPOdqTDz7sgc2l3jJPHNlOKash8m6c3OuI6zXpSwNQI77OaEwxBVcnKQ8KD7_7tp6Pt1BFpjo30YQ7i6qP9-IvHfvfQt_gYmvG1XCxxNYkAf0I-sGAG0GmlyDnXSr5HjG3t1XzosRoc9RgmAkqPQFQ0a2dPM-mmfcKjR3wdf3-pLZ9ULf1Yb-6Q0kuP1G_mc2A-vGDPWt5AToHJgKrPVX0q2BoeQe8LZRvL9cCBnOjVEXXR3QC87PaGrbPHuQd7ovkRg-kxgzlFmgdcexnAmSX3Q0UV3q23vHES3iSpOvezAWsC6M64ja5AJBFjAGh0ypDaHARS9ioP5mtpl_rol7iY9f_tMeUbmjQMAHGkFLHQD8ypeajgxHrRAVb-Nr_CtRTxCNimmYRgSfgzSQlZ2BbOxQxLIbaJlhZU4zXBVPB9L91iaPcIx73SI6m-pDFM2ZIZ4o36Tlo3eydYKB5o9y6nGnen03nv6KSgLpq-aIs40FQDWv84biWBWRGPj2UEomlGp7e-8wvPv16cu6OmDNEi5osjU-4rH6OGQoGb3ZA91LtvRFcH_7Y3r5FAIedi_j6fqZUuGanY3JU_u2NTBld-CZNOhui2_zmfyodfx_-0BuZeqgfnV0uU0dn8cnYRkQtfB6JpeP8GqnhHoXBSmYabnOUgMROdBJ7GVeMgCTYOCRC7xr1YBypdqjtRRv3G00>`_


.. .. figure:: ../../images/wallet_instance_acquisition.svg
..   :figwidth: 100%
..   :align: center
..   :target: https://www.plantuml.com/plantuml/svg/VLHFRnC_4BtxKupSmo-LyhiWmQ4Ig5LLsWg4ehR09L8qkvxiMjcC5tisfNnwx4s9jy7qiehjDt_UcpSv3u9UXcsdS137mxOYhrfh2DREIUL-gl_w2B2rxP55AQp5UT1V0taD66084Jz1WFwENKS2jnm4kQOHXNqFBr6Vw0akH2Y2n3g6YyLjs4DH0fo4tbjk6a_4nUmBxtRMa8SAwmsn6KEhUgEKIXtz_o5MF8Cx-Z5G441WUWJNazyNanPboJw-May14FPPfmqbedQ7GgbtfUBdEUTbI_K6x1ek_LClhl7OjxQ66_Jc4Jr18hRa1snWfdNxVBlQqDDAiD7w56m0tA7jiEf8JJDV4wS6KqCCrBUqZSSEOYZqQ7tATxWT4_P3fVKS_hhsTXSBAUNP2O7RaKyavb4UEFbyUttpS7rtTVL5xPaS2se39C71hK5QWeza_gY6RC1LWfR1Ie0j2HeKLCGcLJgGYNMoz5gpIoxGMT1nJF4p8ZDjM7iARGxOOvwroRU6fecA0aPqtLbYMQN-LYs6Ley6kR-vUFFstUoGR0v5IK-BIL-Pzy8jbZoPTh0Demm-be3ta4wpMQcdEHGjChtE4yrjeOIp8aULdh9aAHIpfRKkyIfu_p2yHojjASySocJdaALTSedRFnGVDIApBvYjNtRsn6NtnEOL0YyzbzSX7Slha1Rxw0yiROHbAnOx-ulCk0Qx-Dke8LXkYYFCEv5z_Yt5e53MgF1OKBi4A-fVH9RrJewTW2yzbPqmMS6opA5t7EXuAQVd6AlEYSsmxNu3

..   Sequence Diagram for Wallet App Attestation acquisition

**Step 1**: The User initiates a new operation that necessitates the acquisition of a Wallet Unit Attestation.

**Steps 2-3**: The Wallet Instance MUST:

  1. Verify the existence of Cryptographic Hardware Keys, Key Attestation API, and Device Integrity API. If Cryptographic Hardware Keys do not exist, Wallet Instance re-initialization is required.
  2. Generate an asymmetric key pair to be attested in the Wallet Unit Attestation (``key_pub``, ``key_priv``).
  3. Verify the Wallet Provider's federation membership and retrieve its metadata.

**Steps 4-6 (Nonce Retrieval)**: The Wallet Instance solicits a ``nonce`` from the :ref:`wallet-provider-endpoint:Wallet Solution Nonce Endpoint` of the Wallet Provider Backend. This ``nonce`` is required to be unpredictable and serves as the main defense against replay attacks. 

The ``nonce`` MUST be produced in a manner that ensures its single-use within a predetermined time frame.

Upon a successful request, the Wallet Provider generates and returns the nonce value to the Wallet Instance.

**Steps 7-8**: The Wallet Instance performs the following actions:

* Creates ``client_data``, a JSON object that includes the ``nonce`` and the thumbprint of ``key_pub`` JWK.
* Computes ``client_data_hash`` by applying the ``SHA256`` algorithm to the ``client_data``.
* Produces an ``hardware_signature`` value by signing the ``client_data_hash`` with the Wallet Hardware's private key, serving as a proof of possession for the Cryptographic Hardware Keys.

Below is a non-normative example of the ``client_data`` JSON object.

.. code-block:: json

  {
    "nonce": "i4ThI2Jhbu81i8mqyWEuDG5t",
    "jwk_thumbprint": "vbeXJksM45xphtANnCiG6mCyuU4jfGNzopGuKvogg9c"
  }

.. note::
   In the case of Android OS, the flow continues based on **Steps 9-12**, otherwise for the case of iOS, the flow continues based on **Steps 13-16**.



**Steps 9-12**: The Wallet Instance:

*  requests the Key Attestation API to create an ``key_attestation`` value linked to the ``client_data_hash``.
*  receives a signed ``key_attestation`` value from the Key Attestation API, authenticated by the OEM.
*  Constructs the Wallet Unit Attestation Request in the form of a JWT. This JWT includes the ``key_attestation``, ``hardware_signature``, ``nonce``, ``hardware_key_tag``, ``cnf`` and other configuration related parameters (see :ref:`Table of the Wallet App Attestation Request Body <table_key_binding_request_claim>`) and is signed using the private key of the initially generated ephemeral key pair.

**Steps 13-16**: The Wallet Instance:

*  requests the Device Integrity Service to create an ``integrity_assertion`` value linked to the ``client_data_hash``.
*  receives a signed ``integrity_assertion`` value from the Device Integrity Service, authenticated by the OEM.
*  Constructs the Wallet Unit Attestation Request in the form of a JWT. This JWT includes the ``integrity_assertion``, ``hardware_signature``, ``nonce``, ``hardware_key_tag``, ``cnf`` and other configuration related parameters (see :ref:`Table of the Wallet App Attestation Request Body <table_key_binding_request_claim>`) and is signed using the private key of the initially generated ephemeral key pair.

**Step 17 (Wallet Unit Attestation Issuance Request)**: The Wallet Instance submits the Wallet Unit Attestation Request to the :ref:`wallet-provider-endpoint:Wallet Attestation Issuance endpoint` of the Wallet Provider Backend.

The Wallet Instance MUST send the signed Wallet Unit Attestation Request JWT as an ``assertion`` parameter in the body of an HTTP request to the Wallet Provider's :ref:`wallet-provider-endpoint:Wallet App Attestation Issuance endpoint`.

**Steps 18-23**: The Wallet Provider Backend evaluates the Wallet Unit Attestation Request and MUST perform the following checks:

  1. The request MUST include all required HTTP header parameters as defined in :ref:`wallet-provider-endpoint:Wallet App Attestation Issuance Request`.
  2. The signature of the Wallet Unit Attestation Request MUST be valid and verifiable using the provided ``jwk``.
  3. The ``nonce`` value MUST have been generated by the Wallet Provider and not previously used.
  4. A valid and currently registered Wallet Instance associated with the provided MUST exist.
  5. The ``client_data`` MUST be reconstructed using the ``nonce`` and the ``jwk`` public key. The ``hardware_signature`` parameter value is then validated using the registered Cryptographic Hardware Key's public key associated with the Wallet Instance.
  6. In the case of Android flow, the ``key_attestation`` MUST be validated according to the device manufacturer's guidelines. The specific checks performed by the Wallet Provider are detailed in the operating system manufacturer's documentation.
  7. In the case of iOS flow, the ``integrity_assertion`` MUST be validated according to the device manufacturer's guidelines. The specific checks performed by the Wallet Provider are detailed in the operating system manufacturer's documentation.
  8. The device in use MUST be free of known security flaws and meet the minimum security requirements defined by the Wallet Provider.
  9. The URL in the ``iss`` parameter MUST match the Wallet Provider's URL identifier.

Upon successful completion of all checks, the Wallet Provider issues a Wallet Unit Attestation valid for at least one month.

**Step 18 (Wallet Unit Attestation Issuance Response)**: Upon successful completion, the Wallet Provider MUST return a confirmation response using status code 200 and Content-Type ``application/json``, containing the Wallet Unit Attestation signed by the Wallet Provider. The Wallet Instance will then perform security and integrity verification of the Wallet Unit Attestation received in addition to trust verification of its Issuer.


Below is a non-normative example of the response.

.. code-block:: http

  HTTP/1.1 200 OK
  Content-Type: application/json

  {
    "wallet_unit_attestation": "omppc3N1ZXJBdXRohEOhASahG...ArQwggKwMIICVqADAgEC"
  }

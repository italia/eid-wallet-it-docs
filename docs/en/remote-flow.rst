.. include:: ../common/common_definitions.rst
.. Included via credential-presentation.rst at title level '=' (document title).


Remote Flow
===========

Remote presentation uses [`OpenID4VP`_]. The EUDIW path is profiled by clause 6 of [`ETSI TS 119 472-2`_] and by the applicable requirements of [`OPENID4VC-HAIP`_], as required by [`CIR2024/2982`_]. The ``client_id`` prefix selects the complete trust path: ``x509_hash`` selects the EUDIW path and ``openid_federation`` selects the National Trust Framework extension (see :ref:`trust-evaluation:Selection at Presentation`). ETSI clause 6 prevails over HAIP where the two sources differ. Implementations MUST NOT combine the paths or retry a failed path under the other framework.

The Relying Party and Wallet Instance MUST support both of the following device topologies (:ref:`RPR-84 <test-plans-remote-presentation:Remote Credential Verifier Test Matrix>`):

* **Same Device**: the flow MUST invoke the Wallet Instance using an HTTP redirect (``302``) or an HTML href (:ref:`RPR-01 <test-plans-remote-presentation:Remote Credential Verifier Test Matrix>`).
* **Cross Device**: the Relying Party MUST provide a ``QR Code`` which the User frames with the device camera or with the Wallet Instance (:ref:`RPR-03 <test-plans-remote-presentation:Remote Credential Verifier Test Matrix>`).

To invoke the correct Wallet Instance, the Relying Party SHOULD trigger the Wallet Instance installed on the User's device the User wishes to use. This information SHOULD be provided by the User using the Selection Page described in :ref:`functionalities:User Experience Design`.
- If the Selection Page is supported, the User selects the Wallet, and then the Relying Party retrieves the Wallet metadata as described in :ref:`wallet-metadata-retrieval:Wallet Metadata Retrieval Flow`. The content of the HTML href or QR Code depends on the ``authorization_endpoint`` parameter in the Wallet metadata:

  - If ``authorization_endpoint`` is available and contains an HTTPS URL (Universal Link), the Relying Party SHOULD use that endpoint.
  - Otherwise, the Relying Party MUST use one of the custom URL schemes: ``openid4vp://`` (as defined in Section 13.1.2 of [`OpenID4VP`_]) or ``haip-vp://`` (as defined in Section 5.1 of [`OPENID4VC-HAIP`_]) or ``eu-eaap://`` (as defined in [`ETSI TS 119 472-2`_]). The Wallet Instance MUST support both custom URL schemes.

- In the case when the Relying Party does not support the Selection Page, or the retrieval of the Wallet metadata may fail for some reason, the Relying Party invokes the Wallet Instance using the custom URL scheme described above.

After invocation, the Wallet Instance establishes trust with the Relying Party and evaluates the request under the selected path. If valid, it asks the User to consent to disclosure of the requested Digital Credentials.

.. note:: "Custom URL Interoperability"

    If a Relying Party in EUDIW interoperability invokes the Wallet via a custom URL then it should use ``eu-eaap://`` in order to be sure that the Wallet Unit receiving the Presentation Request supports the URL as required by OIDFVP-HAIP-REDIRECTS-03 of [`ETSI TS 119 472-2`_].

.. _fig_High-Level-Flow-Presentation:
.. plantuml:: plantuml/credential-presentation-remote-high-level-flow.puml
    :width: 99%
    :alt: The figure illustrates the High Level Remote Protocol Flow.
    :caption: `High Level Remote Protocol Flow. <https://www.plantuml.com/plantuml/svg/TP9FJy904CNl-oacN9GcslZVS30OGWmdQeLmCI5BEz2LTNVTtThKJ-yEGcqndffqthptU-qCdUVMb--IcV0KcJ1SUUWjk9JeOQB2M6NO0-wWwafIbBLG6qZ2otedi8OnQ-3i0Qe1N9n353sMlj1MV74lj88KFqfqFeh05rQNcm8ivi9Yva5RU4uXqpc2oxW2huC6NnN4yG_AYOEksLZbHWlbuvWnBZs8zS4VfgitybpLmN-D5aC1nYhYicO0bmHsaCxJIGlhz6ay8vHa-ZBhxna2GPg4zFP6ExifVFNNrncj799nTGJNPmnLlgSAozUql9Z0gC1iwyB6x-Y6HdE75aRafWYqLUUMnWJS_Jv7wPzcwVKMrL6hHlLFBGgus_LAscXDvtkQTGwXawiDeN0fQwYQVxqihUYpOQWVhkuR>`_


.. .. figure:: ../../images/High-Level-Flow-Presentation.svg
..     :figwidth: 100%
..     :align: center
..     :target: https://www.plantuml.com/plantuml/svg/TL9TJy8m57tlhpZXHLcYYz-61uCXnF34d11UJCZS6bQPRMtlRF3NspB0JUBJidlEFH-v7LhA3DKV5TF-AtAXCqdeBRAgueI9zB3CUG-PXUjIKbvjX5mXySFDbc0qOqRZx05kW8jpHD5ZJQKouZiZeIHI_bbpIr64KmVJ_2nh8_gWqgXwLVfX8GpF2ShWEKMk2WwRPnAlafHdSSHn4-t4eYi-beLMGb8SC-P21gC7k0mXThQOfvDsXAVnBDWaqvTP7mVrDF7AxOssxg7SrR6krKfQtdJR8zEtTr-cpvZRxLs7lSK4evBdQ-l9lz1DWEQM6uo2a2IFjfhS1ZXa_LExQ_obbwJMN1uNQbZ_D0e6TzjAIJlQeUvzm3htxlWg7QBuispWzYTi3ilOaCl2lwuV

..     High Level Remote Protocol Flow


A High-Level description of the remote flow, from the User's perspective, is given below and shown in :ref:`fig_High-Level-Flow-Presentation`:

  1. *Authorization Request*: the Wallet Instance obtains a URL in the Same Device flow or a QR Code in the Cross Device flow. The URL contains ``client_id`` and the required ``request_uri``; the signed Request Object is always retrieved by reference. The ``request`` parameter MUST NOT be used as detailed in `OPENID4VC-HAIP`_.

  2. *Request URI Request*: the Wallet Instance reads ``client_id``, ``request_uri``, and optional ``request_uri_method`` from the outer Authorization Request before retrieving the Request Object.

     * If ``request_uri_method`` is provided and set with the value ``post``, the Wallet Instance SHOULD transmit its metadata to the Relying Party's ``request_uri`` endpoint using the ``HTTP POST`` method.
    * If ``request_uri_method`` is set with the value ``get`` or not present, the Wallet Instance MUST fetch the signed Request Object using an ``HTTP`` request with method ``GET`` to the endpoint provided in the ``request_uri`` parameter (:ref:`RPR-08 <test-plans-remote-presentation:Remote Credential Verifier Test Matrix>`).

  3. *Request URI Response*: the Relying Party returns a signed Request Object to the Wallet Instance.
  4. *WI Checks*: the Wallet Instance selects exactly one trust path from the ``client_id`` prefix, verifies the Request Object under that path, and checks the identity, metadata, authorization artifact, endpoint bindings, and requested scope. 
    
    * For ``x509_hash``, these checks follow :ref:`trust-evaluation:EUDIW Authentication`, :ref:`trust-evaluation:EUDIW Authorization`, and :ref:`trust-evaluation:EUDIW Metadata Retrieval and Validation`; 
    * for ``openid_federation``, they follow :ref:`trust-evaluation:Federation Entity Authentication`, :ref:`trust-evaluation:Authorization`, and :ref:`trust-evaluation:Metadata Retrieval and Validation`. 
  
   It MUST NOT use evidence from the unselected path or fall back to it.

   The following checks MUST be then performed:

    a. verifies the signature of the signed Request Object using the selected path's authenticated public key (:ref:`WP_085 <wallet-credential-presentation-testcases>`).
    b. verifies that the ``client_id`` contained in the Request Object issuer (Relying Party) matches with the one obtained at the Step 2:

       * If ``client_id`` uses the ``openid_federation`` prefix, it MUST match the final policy-processed Federation metadata identity within the validated Trust Chain (:ref:`WP_086 <wallet-credential-presentation-testcases>`).
       * If ``client_id`` uses the ``x509_hash`` prefix, the Wallet Instance MUST verify that the leaf certificate hash in the WRPAC ``x5c`` chain matches the hash in ``client_id``.

     c. evaluates the eligibility of the Relying Party in the presesntation context. 
     
       * For ``x509_hash``, authorization is based on the validated WRPRC in ``verifier_info.registration_cert`` and follows :ref:`trust-evaluation:EUDIW Authorization`; 
        * for ``openid_federation``, authorization is based on the validated ``registration-entity`` Trust Mark and follows :ref:`trust-evaluation:Authorization`. 
       
       The Wallet Instance MUST perform exact, case-sensitive entitlement and DCQL scope checks (:ref:`WP_087 <wallet-credential-presentation-testcases>`).

  5. *Authorization Response*: the Wallet Instance presents the requested information using ``direct_post.jwt``.
  6. *RP Checks*: The Relying Party validates the encrypted response and presented Credentials. Trust in each Credential Issuer is governed by that Credential Issuer's Trust Framework and is independent of the selected Relying Party trust path.
  7. *Relying Party Response*: the Wallet Instance informs the User about the successful authentication with the Relying Party, and the User continues the navigation.

Below is a sequence diagram that details the interactions between all the involved parties.

.. plantuml:: plantuml/credential-presentation-remote-flow.puml
    :width: 99%
    :alt: The figure illustrates the Remote Protocol Flow.
    :caption: `Remote Protocol Flow. <https://www.plantuml.com/plantuml/svg/fLPDRnit4BtpLmpKGssWIPCU3RX8eXgnaxHMBIM-630exaXYJP5RSYX5BVBVEuFHhZwK5W6gcxGpxyrxyx5wLSXcgijWRAKKwtAAsHZpsb7ACFXOC0_05gZ6JDDd_U7x0h_WoZii0_ZkWvylw4seQ5h6ySwtDX8Cxcq8I70J6Juw50nO7uPKXdfcvnX96Qp1s02pRAdkC6nydCE8apR_pdGGzX3FRbzNMi0mU0O-5sHO7MLmILGBC5kR_9QzOC_E7-l8homXowxmx6UezWBkSGfZpA8RebtvkIMVubweDGtk9rh9NE45tE6V5Gl1A2T2HzZmBoNLxD2Ooql-6Gj6iW87euKj29UNFQvKly8EYlri6G9stW5jMdo8bA11GGUNKodyHGg5bA7O9UfN1L8r2re6Q1a1rfxj-lrkc1e9XqN66RZ4zVWejj82eUO0lJWjoMprrGiOBz9QmZeGGHKa5xnxaWUAEQr4AHvuP7SgryRCSwej3BdyRhuWnR0nQ-5PCu-paJb0IAHPHdgZZpuaPmF8R8Ajp1Z9EsrFdtsrig4A4-LQI5Lpf5J9uO-UuMmWyBE-NRVJFyJFwGQuVCmOsK3WppOiQzXZpVvnYRH83NYPeotsw7OyCQ2VTTS-de2LRn2ssy5fjh5aWPBKiW_PJsU7iMy-w6St5ZjnYnwSq4KljZZRsgaFdZmMISLGy1i4lBsQI1TZ8cXrGa_aT4u9Q_7pY4q72adDc-Mq_4zfA7rKBThB3kYm2qORVZI3fyqzE0RmQ-UlZGsqANWd5dH9dp3xsGQ4prBD26dMAJajO9TbWsVCNX57VXgTbNCDg3jJPYdB7ebnH_T4WOOfpdnUOdDuDdfpPO10RbdA_Yyz3dmsMa64XwWzMhMFb9um_W1oq_3aQ9nEXwhsTXhmyF2GuEmblIOI5SECZQoJ3N1JIiKC4zcVXoYUxinuTp-1SMUaedG3xx0KtRGUofWS4sUb5MOEuzD-y_PwylRkwkety_MC2mFFOBX0FYZNAJISzXutyCR7HhejfN1UcaaBHwaK1X1DjSXJaFaIkBPEWtVmn9dJL3d7H_bzNoCbhaV6GhqQgItFZT1VVQPidKvxuuiBgM03bYZxQIKi86KugL6souRG3xvd0j11p0XsPNsG1ZoNeHOdqEnPzh5jjhtIWzQ9ENCfFNc4Ai-nEJVTnHpBWTU3gLF1RCpeI9RDx1RhUZ8P_VZo-KluwSKBk7tFBVnxi1ywaBS2jKNEVGUay_RevAv_sOwuvHgB5dZ0j7VNHTZN3te-AJTL-iQAznTbVNGBz6rKs3zunmQFNVOjQJSkZju9kYkoGsT2q2soIbQJptTY2fgY1LNxlptyeYTi1wr67VnNKB3kbT3s_nco_cSuMVAkjD5fvD7Bzj2nLqnTb-4V>`_


.. .. figure:: ../../images/cross_same_device_auth_seq_diagram.svg
..     :figwidth: 100%
..     :align: center
..     :target: https://www.plantuml.com/plantuml/svg/fLPDRnit4BtpLmpKGssWIPCU3RX8eXgnaxHMBIM-630exaXYJP5RSYX5BVBVEuFHhZwK5W6gcxGpxyrxyx5wLSXcgijWRAKKwtAAsHZpsb7ACFXOC0_05gZ6JDDd_U7x0h_WoZii0_ZkWvylw4seQ5h6ySwtDX8Cxcq8I70J6Juw50nO7uPKXdfcvnX96Qp1s02pRAdkC6nydCE8apR_pdGGzX3FRbzNMi0mU0O-5sHO7MLmILGBC5kR_9QzOC_E7-l8homXowxmx6UezWBkSGfZpA8RebtvkIMVubweDGtk9rh9NE45tE6V5Gl1A2T2HzZmBoNLxD2Ooql-6Gj6iW87euKj29UNFQvKly8EYlri6G9stW5jMdo8bA11GGUNKodyHGg5bA7O9UfN1L8r2re6Q1a1rfxj-lrkc1e9XqN66RZ4zVWejj82eUO0lJWjoMprrGiOBz9QmZeGGHKa5xnxaWUAEQr4AHvuP7SgryRCSwej3BdyRhuWnR0nQ-5PCu-paJb0IAHPHdgZZpuaPmF8R8Ajp1Z9EsrFdtsrig4A4-LQI5Lpf5J9uO-UuMmWyBE-NRVJFyJFwGQuVCmOsK3WppOiQzXZpVvnYRH83NYPeotsw7OyCQ2VTTS-de2LRn2ssy5fjh5aWPBKiW_PJsU7iMy-w6St5ZjnYnwSq4KljZZRsgaFdZmMISLGy1i4lBsQI1TZ8cXrGa_aT4u9Q_7pY4q72adDc-Mq_4zfA7rKBThB3kYm2qORVZI3fyqzE0RmQ-UlZGsqANWd5dH9dp3xsGQ4prBD26dMAJajO9TbWsVCNX57VXgTbNCDg3jJPYdB7ebnH_T4WOOfpdnUOdDuDdfpPO10RbdA_Yyz3dmsMa64XwWzMhMFb9um_W1oq_3aQ9nEXwhsTXhmyF2GuEmblIOI5SECZQoJ3N1JIiKC4zcVXoYUxinuTp-1SMUaedG3xx0KtRGUofWS4sUb5MOEuzD-y_PwylRkwkety_MC2mFFOBX0FYZNAJISzXutyCR7HhejfN1UcaaBHwaK1X1DjSXJaFaIkBPEWtVmn9dJL3d7H_bzNoCbhaV6GhqQgItFZT1VVQPidKvxuuiBgM03bYZxQIKi86KugL6souRG3xvd0j11p0XsPNsG1ZoNeHOdqEnPzh5jjhtIWzQ9ENCfFNc4Ai-nEJVTnHpBWTU3gLF1RCpeI9RDx1RhUZ8P_VZo-KluwSKBk7tFBVnxi1ywaBS2jKNEVGUay_RevAv_sOwuvHgB5dZ0j7VNHTZN3te-AJTL-iQAznTbVNGBz6rKs3zunmQFNVOjQJSkZju9kYkoGsT2q2soIbQJptTY2fgY1LNxlptyeYTi1wr67VnNKB3kbT3s_nco_cSuMVAkjD5fvD7Bzj2nLqnTb-4V

..     Remote Protocol Flow


The details of each step shown in the previous picture are described below.

**Steps 1-2**: The User requests to access to a protected resource of the Relying Party.

**Step 3**: The Relying Party creates a fresh, cryptographically random state value with sufficient entropy, binds it to the user-agent session (e.g., using an HTTP secured cookie), and stores it server-side with a short expiration time. It then inspects the user-agent to determine whether the flow occurs on the same device as the user-agent.

**Steps 4-7 (Authorization Request)**: For a redirect flow, the Relying Party provides the user-agent with a JavaScript page inspecting the status endpoint and the Wallet Instance with a URL containing the Authorization Request. The Request Object is passed by reference only: the URL MUST contain ``client_id`` and ``request_uri`` and MUST NOT contain ``request`` `OPENID4VC-HAIP`_.

  In the **Cross Device Flow**, the Authorization Request is presented as a QR Code displayed to the User. The User scans the QR Code using the Wallet Instance and retrieves a URL.
  Below is represented a non-normative example of a QR Code issued by the Relying Party.

  .. only:: format_html

    .. figure:: ./images/svg/verifier_qr_code.svg
      :figwidth: 50%
      :align: center

  .. only:: format_latex

    .. figure:: ./images/pdf/verifier_qr_code.pdf
      :width: 50%
      :align: center

  .. note::
    The *error correction level* chosen for the QR Code MUST be Q (Quartily - up to 25%), since it offers a good balance between error correction capability and data density/space. This level of quality and error correction allows the QR Code to remain readable even if it is damaged or partially obscured (:ref:`RPR-77 <test-plans-remote-presentation:Remote Credential Verifier Test Matrix>`).

  The URL inside the QR Code contains ``client_id``, ``request_uri``, and optional ``request_uri_method`` parameters (:ref:`WP_076–077 <wallet-credential-presentation-testcases>`).
  Below is represented a non-normative example of the QR Code raw payload with Request Object by reference:

  .. code-block:: text

    https://wallet-solution.example.org/authorization?client_id=openid_federation%3Ahttps%3A%2F%2Frelying-party.example.org&request_uri=https%3A%2F%2Frelying-party.example.org%2Frequest&request_uri_method=post

  An official, self-contained HTML template for this **Cross Device** QR code page—including header, footer, accessibility, multilingual copy, and a configurable demonstrative payload—is provided in the :ref:`official-resources:HTML Components` section (**IT-Wallet Presentation QR Code Page**). It is linked from the wallet cards on the **IT-Wallet Selection Page** in the same section.

  Conversely, in the **Same Device Flow**, the Relying Party uses an HTTP response redirect (with status code set to 302) or an HTML page with an href button (:ref:`WP_076–077 <wallet-credential-presentation-testcases>`).
  
    * For the EUDIW path, the URL uses ``client_id`` with the ``x509_hash`` prefix, ``eu-eaap://`` invocation, and ``request_uri``. 
    * For the National path it uses the ``openid_federation`` prefix.
  
  Below is a non-normative example with Request Object by reference:

  .. code-block:: http

    HTTP/1.1 302 Found
    Location: eu-eaap://authorize?client_id=x509_hash%3AAbCdEfGhIjKlMnOp&request_uri=https%3A%2F%2Frelying-party.example.org%2Frequest_uri&request_uri_method=post


**Step 8**: The Wallet Instance evaluates the trust with the Relying Party using exactly the framework selected by the ``client_id`` prefix (:ref:`WP_078–080 <wallet-credential-presentation-testcases>`). 

* For ``x509_hash``, it follows :ref:`trust-evaluation:EUDIW Authentication`, :ref:`trust-evaluation:EUDIW Authorization`, and :ref:`trust-evaluation:EUDIW Metadata Retrieval and Validation`; 
* for ``openid_federation``, it follows :ref:`trust-evaluation:Federation Entity Authentication`, :ref:`trust-evaluation:Authorization`, and :ref:`trust-evaluation:Metadata Retrieval and Validation`.

**Steps 9-11 (Request URI Request)**: The Wallet Instance reads ``request_uri_method`` from the outer Authorization Request before retrieving the signed Request Object (:ref:`WP_083 <wallet-credential-presentation-testcases>`).

  - If it is provided and is equal to ``post``, the Wallet Instance SHOULD provide its metadata to the Relying Party. The Relying Party updates the Request Object according with the Wallet technical capabilities.

    The following is a non-normative example of an HTTP request made by the Wallet Instance to the Relying Party.

    .. code-block:: http

      POST /request HTTP/1.1
      Host: client.example.org
      Content-Type: application/x-www-form-urlencoded
      Accept: application/oauth-authz-req+jwt

      wallet_metadata=%7B%22vp_formats_supported%22%3A%20%7B%22dc%2Bsd-jwt%22%3A%20%7B%22sd-jwt_alg_values%22%3A%20%5B%22ES256%22%2C%20%22ES384%22%5D%7D%2C%22mso_mdoc%22%3A%7B%22issuerauth_alg_values%22%3A%5B-9%2C-51%5D%2C%22deviceauth_alg_values%22%3A%5B-9%2C-51%5D%7D%7D%2C%22request_object_signing_alg_values_supported%22%3A%20%5B%22ES256%22%5D%2C%22client_id_prefixes_supported%22%3A%5B%22openid_federation%22%2C%22x509_hash%22%5D%7D&wallet_nonce=qPmxiNFCR3QTm19POc8u
    
    Where the body of the request prior to being encoded in `application/x-www-form-urlencoded` by the Wallet corresponds to:

    .. code-block:: json

      {
        "wallet_metadata": {
          "vp_formats_supported": {
            "dc+sd-jwt": {
                "sd-jwt_alg_values": ["ES256", "ES384"]
            },
            "mso_mdoc": {
                "issuerauth_alg_values": [-9, -51],
                "deviceauth_alg_values": [-9, -51]
            }
          },
          "request_object_signing_alg_values_supported": ["ES256"],
          "client_id_prefixes_supported": ["openid_federation", "x509_hash"]
        },
        "wallet_nonce": "qPmxiNFCR3QTm19POc8u"
      }

  - When the Wallet Instance capabilities discovery is not supported by Relying Party, the Wallet Instance requests the signed Request Object using the HTTP method GET (:ref:`WP_082 <wallet-credential-presentation-testcases>`).

**Step 12 (Request URI Response)**: The Relying Party issues the Request Object by signing it with one of its cryptographic private keys. 

* For ``openid_federation``, the Wallet Instance validates the Trust Chain, derives final policy-processed ``openid_credential_verifier`` metadata, and verifies the signature with the key identified by ``kid`` in that metadata, as defined in :ref:`trust-evaluation:Federation Entity Authentication` and :ref:`trust-evaluation:Metadata Retrieval and Validation`. 
* For ``x509_hash``, it verifies the leaf certificate hash against ``client_id``, validates the WRPAC path and SCT against the Providers of WRPAC LoTE, and verifies the signature with the WRPAC key, as defined in :ref:`trust-evaluation:EUDIW Authentication`. 

The Wallet Instance MUST NOT switch paths or retry verification with evidence from the other path (:ref:`WP_084 <wallet-credential-presentation-testcases>`).

  Below is a non-normative example of the Redirect URI Response:

  .. code-block:: http

    HTTP/1.1 200 OK
    Content-Type: application/oauth-authz-req+jwt

    eyJhbGciOiJFUzI1NiIs...9t2LQ

**Steps 13-15 (WI Checks)**: The Wallet Instance verifies the Request Object, which is in the form of a signed JWT, and checks that the outer-request and signed-request ``client_id``, ``iss``, and Relying Party identity are consistent under the selected prefix (:ref:`WP_085–086 <wallet-credential-presentation-testcases>`).

  The following are non-normative examples of Request Objects in the form of decoded headers and payloads. Each example uses exactly one trust framework.

  **EUDIW ``x509_hash`` example**

  .. code-block:: json

    {
      "alg": "ES256",
      "typ": "oauth-authz-req+jwt",
      "x5c": [
        "<WRPAC-leaf-base64url>",
        "<WRPAC-intermediate-base64url>"
      ],
      "iat": 1770000000
    }

  .. code-block:: json

    {
      "client_id": "x509_hash:AbCdEfGhIjKlMnOp",
      "response_mode": "direct_post.jwt",
      "response_type": "vp_token",
      "dcql_query": {
         "credentials": [
          {
             "id": "personal id data",
             "format": "dc+sd-jwt",
             "trusted_authorities": [{"type": "etsi_tl", "values": ["https://trusted-list.example.org"]}],
            "meta": {
              "vct_values": [ "urn:eudi:pid:it:1" ]
            },
            "claims": [
              {"path": ["given_name"]},
              {"path": ["family_name"]},
              {"path": ["birthdate"]}
            ]
          },
          {
             "id": "mobile driving license",
             "format": "mso_mdoc",
             "trusted_authorities": [{"type": "etsi_tl", "values": ["https://trusted-list.example.org"]}],
            "meta": {
              "doctype_value": "org.iso.18013.5.1.mDL"
            },
            "claims": [
              {"path": ["org.iso.18013.5.1", "given_name"]},
              {"path": ["org.iso.18013.5.1", "family_name"]},
              {"path": ["org.iso.18013.5.1", "document_number"]}
            ]
          }
        ]
      },
      "verifier_info": [
        {
          "registrar_dataset": {
            "data": {
              "identifier": "https://relying-party.example.org",
              "srvDescription": [{"lang": "en", "value": "Example service"}],
              "registryURI": "https://registrar.example.org",
              "intendedUseIdentifier": "https://example.org/use/presentation",
              "purpose": [{"lang": "en", "value": "Identity verification"}],
              "policyURI": "https://example.org/policy"
            }
          }
        },
        {
          "registration_cert": {
            "data": "<WRPRC-base64url>"
          }
        }
      ],
      "response_uri": "https://relying-party.example.org/response_uri",
      "aud": "https://wallet.example.org",
      "nonce": "2c128e4d-fc91-4cd3-86b8-18bdea0988cb",
      "wallet_nonce": "qPmxiNFCR3QTm19POc8u",
      "client_metadata": {
          "jwks": {
            "keys": [
              {
                "kty": "EC",
                "use": "enc",
                "crv": "P-256",
                "x": "f83OJ3D2xF1Bg8vub9tLe1gHMzV76e8Tus9uPHvRVEU",
                "y": "x_FEzRu9m36HLN_tue659LNpXW6pCyStikYjKIWI5a0",
                "kid": "20260202-abc123",
                "alg": "ECDH-ES"
              }
            ]
          },
          "encrypted_response_alg_values_supported": ["ECDH-ES"],
          "encrypted_response_enc_values_supported": ["A128GCM", "A256GCM"]
      },
      "state": "3be39b69-6ac1-41aa-921b-3e6c07ddcb03",
      "iss": "x509_hash:AbCdEfGhIjKlMnOp",
      "iat": 1672418465,
      "exp": 1672422065
    }

  **National ``openid_federation`` example**

  .. code-block:: json

    {
      "alg": "ES256",
      "typ": "oauth-authz-req+jwt",
      "kid": "national-signing-key",
      "trust_chain": ["<entity-statement-base64url>"]
    }

  .. code-block:: json

    {
      "client_id": "openid_federation:https://relying-party.example.org",
      "response_mode": "direct_post.jwt",
      "response_type": "vp_token",
      "dcql_query": {"credentials": [{"id": "pid", "format": "dc+sd-jwt", "meta": {"vct_values": ["urn:eudi:pid:it:1"]}}]},
      "response_uri": "https://relying-party.example.org/response_uri",
      "client_metadata": {
         "jwks": {"keys": [{"kty": "EC", "use": "enc", "crv": "P-256", "x": "f83OJ3D2xF1Bg8vub9tLe1gHMzV76e8Tus9uPHvRVEU", "y": "x_FEzRu9m36HLN_tue659LNpXW6pCyStikYjKIWI5a0", "kid": "20260202-abc123", "alg": "ECDH-ES"}]},
        "encrypted_response_enc_values_supported": ["A128GCM", "A256GCM"]
      },
      "state": "3be39b69-6ac1-41aa-921b-3e6c07ddcb03",
      "iss": "openid_federation:https://relying-party.example.org",
      "iat": 1672418465,
      "exp": 1672422065
    }

* For ``x509_hash``, the Wallet Instance authenticates the WRPAC, validates the WRPRC, and binds the direct or intermediated Relying Party identity to the WRPAC, WRPRC, and ``registrar_dataset.identifier``. It checks the Service Provider entitlement and the exact, case-sensitive DCQL scope. If the WRPRC is missing or invalid, it MAY query the Register. 

* For ``openid_federation``, it validates the registration Trust Mark, its entitlements, and its exact, case-sensitive scope, and MUST NOT treat WRPAC or WRPRC material as National trust evidence. 

A failed evaluation terminates processing and MUST NOT trigger a retry under the other framework (:ref:`WP_087 <wallet-credential-presentation-testcases>`).

**Steps 16-17 (User Consent)**: Before disclosure, the Wallet Instance MUST display the verified Relying Party and Service, the intended use or purpose, and the requested Credentials and attributes from the authoritative authorization artifact. In the National path, it MUST additionally display both the Relying Party and the Federation Intermediate when applicable. In an EUDIW intermediated flow, it MUST display the intermediated Relying Party and Service and MUST NOT display Intermediary trade names. The User authorizes and consents to presentation by selecting the data to release (:ref:`WP_088 <wallet-credential-presentation-testcases>`).

**Step 18 (Authorization Response)**: The Wallet Instance provides the encrypted Authorization Response to the Relying Party using an HTTP POST with response mode ``direct_post.jwt``.

  Below is a non-normative example of the Authorization Response:

  .. code-block:: http

      POST /response_uri HTTP/1.1
      HOST: relying-party.example.org
      Content-Type: application/x-www-form-urlencoded

      response=eyJhbGciOiJFQ0RILUVTIiwiZW5jIjoiQTI1NkdDTSIsImtpZCI6ImVwaGVtZXJhbC0yMDI2MDIwMi1hYmMxMjMiLCJlcGsiOnsi...fX0..5vL9d2X8fQ..dGhpcy1pcy1hLXNhbXBsZS1jaXBoZXJ0ZXh0.ABCDEFGHIJKLMNOPQRS

  Below is a non-normative example showing the decrypted JWE protected header and the payload of the JWT contained in the response, before base64url encoding. The ``vp_token`` parameter value corresponds to the format used when the DCQL query language is used in the presentation request.

  .. code-block:: json

      {
        "alg": "ECDH-ES",
        "enc": "A256GCM",
        "kid": "20260202-abc123",
        "epk": {
          "kty": "EC",
          "crv": "P-256",
          "x": "f83OJ3D2xF1Bg8vub9tLe1gHMzV76e8Tus9uPHvRVEU",
          "y": "x_FEzRu9m36HLN_tue659LNpXW6pCyStikYjKIWI5a0"
        }
      }

  .. code-block:: json

      {
        "state": "3be39b69-6ac1-41aa-921b-3e6c07ddcb03",
        "vp_token": {
          "personal id data": ["eyJhbGciOiJFUzI1NiIs...PT0iXX0"],
          "mobile driving license": ["o2Nkb2N0eXBlb3Jzby4xO...Nib3JfZHVtbXk"]
        }
      }

.. note::
  When returning a requested Credential in ``mso_mdoc`` format in the ``vp_token``, the Wallet MUST cryptographically bind the resulting mdoc presentation to the current OpenID4VP transaction. To achieve this, the Wallet builds the ISO ``SessionTranscript`` used for mdoc device authentication and applies the OpenID4VP profiling rules by setting ``DeviceEngagementBytes`` to ``null`` and ``EReaderKeyBytes`` to ``null``, and sets its ``Handover`` field to an OpenID4VP-defined structure (``OpenID4VPHandover``) derived from the Authorization Request parameters. The Wallet then computes the mdoc device authentication (device signature) over data that includes this ``SessionTranscript``, such that the resulting mdoc presentation is valid only for that specific OpenID4VP transaction. For the normative definition of ``OpenID4VPHandover`` and the corresponding ``SessionTranscript`` profiling rules, see `OpenID4VP`_ Appendix B.2.

**Steps 19-22 (RP Checks)**: The Relying Party verifies the encrypted Authorization Response, extracts the ``vp_token``, and validates its overall format and each presentation against the DCQL query. 

For SD-JWT VC, issuer-key resolution MUST use the X.509 ``x5c`` chain excluding the trust anchor and a non-self-signed signing certificate; the Relying Party MUST validate a status list when present, the issuer and holder signatures, and the proof of possession. 

Presentation-signature validation MUST support at least ES256 on P-256 with SHA-256, and hash validation MUST support SHA-256. 

Trust in each presented Credential is governed by that Credential's Rulebook and is independent of the Relying Party trust path; selecting ``x509_hash`` MUST NOT imply Federation-based Credential Issuer trust. 

If all verifications succeed, the Relying Party updates the User session.

**Steps 23-24 or 25 (Relying Party Response)**: The Relying Party provides to the Wallet Instance the response about the presentation, which informs the User.

  Upon receiving and validating the Authorization Response at the Response Endpoint, the Relying Party returns to the Wallet Instance an HTTP 200 OK. In particular, in the Same Device Flow, the Relying Party MUST also pass the ``redirect_uri`` parameter in the response to the Wallet Instance. Upon receiving the ``redirect_uri``, the Wallet Instance MUST perform a redirect to the URL specified by the ``redirect_uri``. This redirect allows the Relying Party to seamlessly resume interaction with the User on the device which initiated the flow. When the response does not contain the ``redirect_uri`` parameter, the Wallet Instance is not required to perform any further step. The User should manually close the Wallet Instance and open the user-agent to continue the flow (:ref:`RPR-83 <test-plans-remote-presentation:Remote Credential Verifier Test Matrix>`).

  The following is a non-normative example of the response in the Same Device Flow.

.. code-block:: http

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
      "redirect_uri": "https://relying-party.example.org/cb?response_code=091535f699ea575c7937fa5f0f454aee"
    }

**Steps 26-27**: The JavaScript page is inspecting the status endpoint.

  Below is a non-normative example of the HTTP Request to the status endpoint, where the parameter ``id`` contains an opaque and random value:

  .. code-block:: http

      GET /session-state?id=3be39b69-6ac1-41aa-921b-3e6c07ddcb03 HTTP/1.1
      HOST: relying-party.example.org

  When the Wallet Instance has provided the presentation to the Relying Party's **response_uri** endpoint and, in the Same Device Flow, the user-agent has successfully returned via ``redirect_uri`` within the same user session, the User authentication is successful. The Relying Party updates the session cookie allowing the user-agent to access to the protected resource. A redirect URL is provided carrying the location where the user-agent is intended to navigate.
  The following is a non-normative example of the response with the ``redirect_uri`` from the Relying Party to the user-agent.

  .. code-block:: http

      HTTP/1.1 200 OK
      Content-Type: application/json

      {
        "redirect_uri": "https://relying-party.example.org/cb?response_code=091535f699ea575c7937fa5f0f454aee"
      }

**Steps 28-29**: The user-agent is redirected to the redirect URI to continue the navigation with the protected resource made available to the User (:ref:`WP_094 <wallet-credential-presentation-testcases>`). The Relying Party MUST consider the transaction completed only if the redirect back is received in the same user session in which the flow was initiated; otherwise it MUST reject the presentation.

.. note::
    During each credential presentation transaction executed through the remote flow, the Wallet Instance MUST create and maintain a corresponding transaction record in the transaction log (see :ref:`wallet-instance-dashboard:Wallet Instance Dashboard and Transaction Logging`).

    The transaction record MUST be created once the Wallet Instance has accepted the presentation request for processing (i.e., after request validation and Relying Party trust/policy checks, Steps 13–15). At this point, the record MUST include the transaction metadata and the request context available at that stage (e.g., the requested Credential type(s) and the identifier(s) of the requested attributes), without logging any attribute values.

    The record MUST be updated as the transaction progresses to reflect the evolving transaction state and result context (e.g., what was actually presented after User consent and response preparation/sending, Steps 16–18), without logging any attribute values.

    The record MUST be finalized when the transaction ends, indicating the outcome (e.g., completed, failed, or aborted; Steps 23–29).


Authorization Request
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The URL parameters contained in the Relying Party Authorization Request are described in the table below.

.. list-table::
  :class: longtable
  :widths: 25 50
  :header-rows: 1

  * - **Name**
    - **Description**
  * - **client_id**
    - REQUIRED. Unique identifier of the Relying Party. The value MUST use one of the following Client Identifier Prefixes (as defined in `OpenID4VP`_, Section 5.9): ``openid_federation`` (Relying Party’s Entity Identifier in a Trust Chain) or ``x509_hash`` (base64url-encoded SHA-256 hash of the Relying Party’s X.509 certificate).
   * - **request_uri**
     - REQUIRED. The HTTPS URL where the Relying Party provides the signed Request Object to the Wallet Instance. The Request Object MUST be retrieved by reference.
  * - **request_uri_method**
    - OPTIONAL only if ``request_uri`` is specified, otherwise MUST NOT be present. The HTTP method MUST be set with ``get`` or ``post`` (:ref:`RPR-07 <test-plans-remote-presentation:Remote Credential Verifier Test Matrix>`, :ref:`RPR-08 <test-plans-remote-presentation:Remote Credential Verifier Test Matrix>`, :ref:`RPR-09 <test-plans-remote-presentation:Remote Credential Verifier Test Matrix>`). The Wallet Instance should use this method to obtain the signed Request Object from the ``request_uri``. If not provided or equal to ``get``, the Wallet Instance SHOULD use the HTTP method ``get``. Otherwise, the Wallet Instance SHOULD provide its metadata within the HTTP POST body encoded in ``application/x-www-form-urlencoded``.

.. note::
The value corresponding to the ``request_uri`` endpoint SHOULD be randomized, according to `RFC 9101, The OAuth 2.0 Authorization Framework: JWT-Secured Authorization Request (JAR) <https://www.rfc-editor.org/rfc/rfc9101.html#section-5.2.1>`_ Section 5.2.1.

.. _endpoint-mix-up-protection:

Endpoint Mix-Up Protection
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. warning::
   For redirect flows, to prevent endpoint mix-up attacks, the values of ``request_uri``, ``response_uri`` and ``redirect_uri`` MUST each be attested by a trusted third party.
  Under the National Trust Framework they MUST match the corresponding ``request_uris``, ``response_uris`` and ``redirect_uris`` parameters in the final policy-processed ``openid_credential_verifier`` metadata obtained from the Trust Chain, as defined in :ref:`trust-evaluation:Metadata Retrieval and Validation`.
  Under the EUDIW Trust Framework they MUST satisfy the WRPAC/WRPRC identity and endpoint binding, as specified in :ref:`trust-evaluation:EUDIW Authentication` and :ref:`trust-evaluation:EUDIW Authorization`. Evidence from the unselected framework MUST NOT authorize an endpoint.

  This requirement applies to ``request_uri`` as specified in :ref:`WP_081 <wallet-credential-presentation-testcases>` and :ref:`RPR-85 <test-plans-remote-presentation:Remote Credential Verifier Test Matrix>`.


Request URI Request
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Relying Party SHOULD provide the POST method with its ``request_uri`` endpoint allowing the Wallet Instance to inform the Relying Party about its technical capabilities.

This feature can be useful when, for example, the Wallet Instance supports a restricted set of features, supported algorithms or a specific url for its ``authorization_endpoint``, and any other information that it deems necessary to provide to the Relying Party for interoperability.

.. warning::
  The Wallet Instance, when providing its technical capabilities to the Relying Party, MUST NOT include any User information or other explicit (:ref:`RPR-86 <test-plans-remote-presentation:Remote Credential Verifier Test Matrix>`) information regarding the hardware used or usage preferences of its User (:ref:`RPR-86 <test-plans-remote-presentation:Remote Credential Verifier Test Matrix>`).

If both the Relying Party and the Wallet Instance support the ``request_uri_method`` with HTTP POST, the Wallet Instance capabilities (metadata) MUST be provided using an HTTP request to the ``request_uri`` endpoint of the Relying Party, with the method POST and content type set to ``application/x-www-form-urlencoded`` (:ref:`WP_083 <wallet-credential-presentation-testcases>`).
The request and its parameters are defined in Section 5 (Authorization Request) of `OpenID4VP`_. Below are the normative details and references about the parameters to be used by the Wallet Instance in the request (:ref:`WP_083a–083c <wallet-credential-presentation-testcases>`).

.. list-table:: Request URI Endpoint Parameters
   :class: longtable
   :widths: 20 80
   :header-rows: 1

   * - **Parameter**
     - **Description**
   * - `wallet_metadata`
     - OPTIONAL. JSON object with metadata parameters. See `OpenID4VP`_, Section 10.1 and the table below, "Wallet Metadata Parameters".
   * - `wallet_nonce`
     - RECOMMENDED. String used by Wallet Instance to prevent replay of the Relying Party's responses.


.. _table_wallet_metadata_parameters:
.. list-table:: Wallet Metadata Parameters
   :class: longtable
   :widths: 20 80
   :header-rows: 1

   * - **Parameter**
     - **Description**
   * - `vp_formats_supported`
     - REQUIRED. Object containing a list of name/value pairs, where the name is a Credential Format Identifier and the value defines format-specific parameters that a Wallet supports. See `OpenID4VP`_ Appendix B. Wallet Instances MUST support the Credential Format Identifiers required by `OPENID4VC-HAIP`_ (including ``dc+sd-jwt`` and ``mso_mdoc``).
   * - `client_id_prefixes_supported`
     - REQUIRED. A non-empty array of the Client Identifier Prefixes that the Wallet Instance supports. Wallet Instances MUST include both ``x509_hash`` (EUDIW / [`OPENID4VC-HAIP`_]) and ``openid_federation`` (National Trust Framework).
   * - `request_object_signing_alg_values_supported`
     - OPTIONAL. See OpenID Connect Discovery.


.. note::
  In the IT Wallet, legacy Relying Parties using an ``https`` URI as ``client_id`` are treated as using the ``openid_federation`` prefix for backward compatibility. Their trust is established and validated through Trust Chain resolution; this does not define a third client identifier path or a ``pre-registered`` default.

.. note::
  The ``wallet_nonce`` parameter is RECOMMENDED for Wallet Instances that want to prevent reply of their http requests to the Relying Parties.
  When present, the Relying Party MUST evaluate it (:ref:`RPR-81 <test-plans-remote-presentation:Remote Credential Verifier Test Matrix>`).


Request URI Response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Relying Party issues the signed Request Object using the content type set to ``application/oauth-authz-req+jwt``. For the content of the Request Object see Section :ref:`remote-flow:Request Object`.

Request URI Endpoint Errors
----------------------------

When the Relying Party encounters errors while issuing the Request Object from the ``request_uri`` endpoint, it MUST return an error response with ``application/json`` as the content type and MUST include the following parameters:

* ``error``: The error code.
* ``error_description``: Text in human-readable form providing further details to clarify the nature of the error encountered.

The following table lists the HTTP Status Codes and related error codes that MUST be supported for the error response:

.. list-table::
    :class: longtable
    :widths: 20 20 60
    :header-rows: 1

    * - **Status Code**
      - **Error Code**
      - **Description**
    * - ``400 Bad Request``
      - ``invalid_request``
      - The Request Object could not be retrieved due to an invalid or malformed request at the ``request_uri`` endpoint. (:rfc:`6749#section-4.1.2.1`).
    * - ``500 Internal Server Error``
      - ``server_error``
      - The request cannot be fulfilled because the Request URI Endpoint encountered an internal problem. (:rfc:`6749#section-4.1.2.1`).
    * - ``503 Service Unavailable``
      - ``temporarily_unavailable``
      - The request cannot be fulfilled because the Request URI Endpoint is temporarily unavailable (e.g., due to maintenance or overload). (:rfc:`6749#section-4.1.2.1`).


The following is an example of an error response from ``request_uri`` endpoint:

.. code-block:: http

  HTTP/1.1 500 Internal Server Error
  Content-Type: application/json

  {
    "error": "server_error",
    "error_description": "The Request Object cannot be retrieved due to an internal server error."
  }

Upon receiving an error response, the Wallet Instance SHOULD inform the User of the error condition in an appropriate manner (:ref:`WP_089 <wallet-credential-presentation-testcases>`). The Wallet Instance SHOULD log the error and MAY attempt to recover from certain errors if feasible, but recovery MUST remain within the selected transport and trust path (:ref:`WP_089a <wallet-credential-presentation-testcases>`). A new QR code MAY be offered where applicable (:ref:`WP_089b <wallet-credential-presentation-testcases>`).

Request Object
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The JWT header parameters are described below:

.. list-table::
  :class: longtable
  :widths: 25 50
  :header-rows: 1

  * - **Name**
    - **Description**
  * - **alg**
    - REQUIRED. Algorithm used to sign the JWT, according to [:rfc:`7516#section-4.1.1`]. It MUST be one of the supported algorithms in Section :ref:`algorithms:Cryptographic Algorithms` and MUST NOT be set to ``none`` or to a symmetric algorithm (MAC) identifier. For signed presentation-request validation, implementations MUST support at least ES256 using P-256 and SHA-256 (:ref:`RPR-88 <test-plans-remote-presentation:Remote Credential Verifier Test Matrix>`).
  * - **typ**
    - REQUIRED. Media Type of the JWT, as defined in [:rfc:`7519`] and [:rfc:`9101`]. It SHOULD be set to the value ``oauth-authz-req+jwt`` (:ref:`RPR-89 <test-plans-remote-presentation:Remote Credential Verifier Test Matrix>`).
  * - **kid**
    - NATIONAL PATH ONLY. REQUIRED when ``client_id`` uses the ``openid_federation`` prefix. It identifies the public key in the final policy-processed Federation metadata, as defined in [:rfc:`7517`]. It is not EUDIW authentication evidence.
  * - **trust_chain**
    - NATIONAL PATH ONLY. OPTIONAL sequence of Entity Statements composing the Relying Party Trust Chain, as defined in `OID-FED`_ Section 4.3 *Trust Chain Header Parameter*. It is not EUDIW authentication evidence.
  * - **x5c**
    - EUDIW PATH ONLY. REQUIRED when ``client_id`` uses the ``x509_hash`` prefix. It contains the WRPAC first, followed by its certification path up to but excluding the trust anchor. The WRPAC MUST be used to verify the JWT signature; the chain MUST validate and its SCT MUST be valid against the Providers of WRPAC LoTE. The WRPAC binds the Relying Party identity and applicable presentation endpoints. It is not National authentication evidence.

.. note::
   For ``x509_hash``, the ``x5c`` header MUST contain the WRPAC first and MUST NOT include the trust anchor as required by `OPENID4VC-HAIP`_. The chain MUST validate to a trust anchor obtained from the Providers of WRPAC LoTE; see Section :ref:`infrastructure-trust:X.509 Certificate Profile` for background on X.509 certificate chain validation.

The JWT payload parameters are described herein:

.. list-table::
  :class: longtable
  :widths: 25 50
  :header-rows: 1

  * - **Name**
    - **Description**
  * - **client_id**
    - REQUIRED. Unique Identifier of the Relying Party. It MUST use the same prefix-qualified value as the Authorization Request and MUST identify the same Relying Party as ``iss`` and the selected trust evidence.
  * - **client_metadata**
    - REQUIRED for both paths. A JSON object containing the Relying Party metadata values defined in Section 5.1 of `OpenID4VP`_. It contains the following parameters:
    
      - ``jwks``. REQUIRED by [`ETSI TS 119 472-2`_]. Contains the request-specific ephemeral response-encryption public key and the applicable response-encryption capabilities. Every key MUST have ``kid`` and ``use``; each ``kid`` MUST identify exactly one key. The Verifier metadata MUST list both ``A128GCM`` and ``A256GCM``. For ``x509_hash``, applicable RP metadata is carried here.
      - **vp_formats_supported**. Used by the Wallet Instance to determine the supported Verifiable Presentation formats.
      - **client_name** and **logo_uri**. OPTIONAL. Used for user consent display and to show the Relying Party identity in the Wallet Instance interface.
  * - **response_mode**
    - REQUIRED. It MUST be ``direct_post.jwt`` (:ref:`RPR-90 <test-plans-remote-presentation:Remote Credential Verifier Test Matrix>`).
  * - **aud**
    - REQUIRED on the EUDIW path. It MUST identify the intended Wallet audience and be consistent with the selected ``client_id`` and Relying Party identity.
  * - **dcql_query**
    - REQUIRED. Object representing a request for a presentation of Credentials, according to the DCQL query language defined in Section 6 of `OpenID4VP`_. On the EUDIW path, each applicable query MUST use the ETSI Trusted Lists Authority Key Identifier mechanism with ``trusted_authorities`` type ``etsi_tl``.
  * - **verifier_info**
    - REQUIRED on the EUDIW path [`ETSI TS 119 472-2`_]. An array containing a ``registrar_dataset`` object and a separate ``registration_cert`` object. 
    
    It MUST NOT contain ``credential_ids`` [`ETSI TS 119 472-2`_]. 
      
      - The ``registrar_dataset`` object MUST contain non-empty object ``data`` and the registered ``identifier``, ``srvDescription``, ``registryURI``, ``intendedUseIdentifier``, ``purpose``, and ``policyURI`` members; ``srvDescription`` and ``purpose`` MUST use registered ``MultiLangString`` values. 
      - The ``registration_cert`` object's ``data`` MUST be the base64url serialization of the WRPRC. 
      
    These objects are not required for ``openid_federation``, whose equivalent authorization and transparency data comes from the validated registration Trust Mark (see :ref:`trust-evaluation:Metadata Retrieval and Validation`).
  * - **transaction_data**
    - OPTIONAL. Non-empty array of JSON objects, each describing a transaction that the Relying Party requests the User to authorize. Each transaction object includes:
        - **type**.  String that identifies the transaction data type.
        - **credential_ids**. Array referencing one or more Credentials from the ``dcql_query`` that can authorize the transaction.
  * - **transaction_data_hashes_alg**
    - OPTIONAL. Array of strings, each representing a hash algorithm identifier, corresponding to a hash algorithm name listed in the `IANA <https://www.iana.org/assignments/named-information/named-information.xhtml#hash-alg>`_.  One of these algorithms MUST be used to calculate the hashes in the ``transaction_data_hashes`` response parameter.  If omitted, the default hash algorithm is ``sha-256``.
  * - **response_type**
    - REQUIRED. It MUST be set to ``vp_token`` (:ref:`RPR-91 <test-plans-remote-presentation:Remote Credential Verifier Test Matrix>`).
  * - **wallet_nonce**
    - REQUIRED if previously provided by Wallet Instance (:ref:`RPR-81 <test-plans-remote-presentation:Remote Credential Verifier Test Matrix>`). String value used to mitigate replay attacks of the response, as defined in Section 5.10 (Request URI Method) of `OpenID4VP`_.
  * - **response_uri**
    - REQUIRED. The Response URI to which the Wallet Instance MUST send the Authorization Response using an HTTP request using the method POST (:ref:`RPR-92 <test-plans-remote-presentation:Remote Credential Verifier Test Matrix>`).
  * - **nonce**
    - REQUIRED. Fresh cryptographically random number with sufficient entropy, which length MUST be at least 32 digits (:ref:`RPR-93 <test-plans-remote-presentation:Remote Credential Verifier Test Matrix>`).
  * - **state**
    - RECOMMENDED. Unique identifier of the Authorization Request, its value SHOULD be opaque to the Wallet Instance.
  * - **iss**
    - REQUIRED. The entity that has issued the JWT. It MUST equal the prefix-qualified ``client_id`` and the Authorization Request issuer's identity.
  * - **iat**
    - REQUIRED. Unix Timestamp, representing the time at which the JWT was issued.
  * - **exp**
    - REQUIRED. Unix Timestamp, representing the expiration time on or after which the JWT MUST NOT be valid anymore (:ref:`RPR-94 <test-plans-remote-presentation:Remote Credential Verifier Test Matrix>`).

.. warning::
  The ``response_uri`` parameter is subject to :ref:`endpoint-mix-up-protection` (:ref:`WP_091a <wallet-credential-presentation-testcases>` and :ref:`RPR-95 <test-plans-remote-presentation:Remote Credential Verifier Test Matrix>`).

.. note::
  The ``transaction_data`` parameter is intended for use cases where the Wallet Instance MUST authorize a specific transaction, such as payment initiation or digital signing. In these high-sensitivity scenarios, the goal is to bind the transaction details to the Authorization Response so that integrity is preserved and the User’s approval can be proven afterwards (non-repudiation).

  The binding mechanism depends on the Credential Format:

  - **dc+sd-jwt**: the Wallet binds the transaction data by returning ``transaction_data_hashes`` (and, when applicable, ``transaction_data_hashes_alg``) inside the Key Binding JWT (KB-JWT). See `OpenID4VP`_, Appendix B.3.3 for further details.
  - **mso_mdoc**: transaction data is bound through mdoc device authentication. For this format, the Wallet MUST check that the requested transaction data ``type`` is supported by the document type and authorized by the issuer (KeyAuthorizations). If it is not authorized, the Wallet MUST reject the request due to an unsupported transaction data type. See `OpenID4VP`_, Appendix B.2.1 for further details.

.. note::
  The ``state`` parameter in an OAuth request is optional, but it is highly recommended. It is primarily used to prevent Cross-Site Request Forgery (CSRF) attacks by including a unique and unpredictable value that the Relying Party can verify upon receiving the response. Additionally, it helps maintain the state between the request and response, such as session information or other data the Relying Party needs after the authorization process.

.. note::
  
  ``client_metadata`` and ``client_metadata.jwks`` are required for both profiled paths because every request supplies a request-specific ephemeral response-encryption public key [`ETSI TS 119 472-2`_].

Authorization Response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
After obtaining the User authorization and consent for the presentation of the Digital Credentials, the Wallet Instance sends the Authorization Response to the Relying Party ``response_uri`` endpoint using an HTTP POST (:ref:`WP_091 <wallet-credential-presentation-testcases>`). 

Every successful response MUST be encrypted using the mandatory, request-specific ephemeral public key selected from ``client_metadata.jwks`` by its unique ``kid`` and MUST use ``direct_post.jwt`` (:ref:`WP_092 <wallet-credential-presentation-testcases>`). The Verifier MUST support both ``A128GCM`` and ``A256GCM``; the Wallet MUST support at least one and SHOULD prefer ``A256GCM`` when both are available [`ETSI TS 119 472-2`_].

.. note::
    **Why the response is encrypted?**

    The response sent from the Wallet Instance to the Relying Party is encrypted to prevent a malicious agent from gaining access to the plaintext information transmitted within the Relying Party's network. This is only possible if the network environment of the Relying Party employs `TLS termination <https://www.f5.com/glossary/ssl-termination>`_. Such technique employs a termination proxy that acts as an intermediary between the client and the webserver and handles all TLS-related operations. In this manner, the proxy deciphers the transmission's content and either forwards it in plaintext or by negotiates an internal TLS session with the actual webserver's intended target. In the first scenario, any malicious actor within the network segment could intercept the transmitted data and obtain sensitive information, such as an unencrypted response, by sniffing the transmitted data.

Where the following parameters are used (:ref:`WP_093 <wallet-credential-presentation-testcases>`):

.. list-table::
  :class: longtable
  :widths: 25 50
  :header-rows: 1

  * - **Name**
    - **Description**
   * - **vp_token**

    - This object MUST contain the presented Digital Credential(s), keyed by the Credential ``id`` values from the ``dcql_query`` in the Authorization Request.

      The ``vp_token`` MUST be a JSON Object where each key corresponds to a requested Credential id, and each value is either a single presentation or an array of one or more presentations for that Credential. The encoding of each presentation depends on the Credential format, for example:

       - **dc+sd-jwt**: a compact-serialized SD-JWT VC string. The Wallet MUST append a KB-JWT whenever the presentation is cryptographically holder-bound (:ref:`WP_093a <wallet-credential-presentation-testcases>`).
      - **mso_mdoc**: a base64url-encoded CBOR ``DeviceResponse`` corresponding to the requested mdoc presentation (see `OpenID4VP`_ Appendix B.2). When multiple mdoc presentations are returned, each MUST be carried in a separate ``DeviceResponse`` aligned with the corresponding DCQL query item; in this case, the ``vp_token`` value for that Credential id MUST be an array of ``DeviceResponse`` values.

  * - **state**
    - Unique identifier provided by the Relying Party within the Authorization Request.

SD-JWT defines how a Holder can present a Digital Credential to a Relying Party, proving the legitimate possession of the Digital Credential. To do this, the Holder MUST include the ``KB-JWT`` in the SD-JWT by appending the ``KB-JWT`` at the end of the SD-JWT (:ref:`WP_093b <wallet-credential-presentation-testcases>`), as represented in the example below

.. code-block:: text

  <Issuer-Signed-JWT>~<Disclosure 1>~<Disclosure 2>~...~<Disclosure N>~<KB-JWT>

To validate the signature on the Key Binding JWT, the Relying Party MUST use the key material included in the Issuer-Signed-JWT. The Key Binding JWT (KB-JWT) signature validation MUST use the public key included in the SD-JWT, using the cnf parameter contained in the Issuer-Signed-JWT.

When an SD-JWT is presented, its KB-JWT MUST contain the following parameters in the JWT header (:ref:`WP_093c <wallet-credential-presentation-testcases>`):

.. list-table::
  :class: longtable
  :widths: 25 50
  :header-rows: 1

  * - **Claim**
    - **Description**
  * - **typ**
    - REQUIRED. MUST be ``kb+jwt``, which explicitly types the Key Binding JWT as recommended in Section 3.11 of :rfc:`8725`.
  * - **alg**
    - REQUIRED. Signature Algorithm using one of the specified in the Section :ref:`algorithms:Cryptographic Algorithms`.

When an SD-JWT is presented, the KB-JWT signature MUST be verified by the same public key included in the SD-JWT within the `cnf` parameter. The KB-JWT MUST contain the following parameters in the JWT payload:

.. list-table::
  :class: longtable
  :widths: 25 50
  :header-rows: 1

  * - **Claim**
    - **Description**
  * - **iat**
    - REQUIRED. The value of this claim MUST be the time at which the Key Binding JWT was issued, using the syntax defined in :rfc:`7519`.
  * - **aud**
    - REQUIRED. The intended receiver of the Key Binding JWT. The value of this parameter MUST match the Relying Party unique entity identifier.
  * - **nonce**
    - REQUIRED. Ensures the freshness of the signature. The value type of this claim MUST be a string. The value MUST match with the one provided in the request object.
  * - **sd_hash**
    - REQUIRED. The base64url-encoded hash digest over the Issuer-signed JWT and the selected disclosures.
  * - **transaction_data_hashes**
    - CONDITIONAL. REQUIRED when the request includes ``transaction_data``. Non-empty array of base64url-encoded hashes. Each hash is computed over the exact string value of the corresponding ``transaction_data`` item.
  * - **transaction_data_hashes_alg**
    - CONDITIONAL. REQUIRED only if the request included ``transaction_data_hashes_alg``. String naming the hash algorithm actually used to compute ``transaction_data_hashes``; if that parameter was not provided, the hash function MUST be ``sha-256``.


Authorization Response Errors
-----------------------------

There are cases where the Wallet Instance cannot validate the Request Object or the Request Object results invalid. This error occurs if the Request Object is successfully fetched from the url provided in the parameter ``request_uri`` but fails the validation checks. This could be due to incorrect signatures, malformed claims, or other validation failures, such as the revocation of the Relying Party.

If the Wallet Instance encounters an error during evaluation, it MUST send an Authorization Error Response only after the selected trust path has authenticated the applicable ``response_uri``. If the request or endpoint has not been authenticated, the Wallet Instance MUST terminate locally, notify the User appropriately, and MUST NOT disclose Wallet or Credential availability (:ref:`WP_090 <wallet-credential-presentation-testcases>`).
For an authenticated redirect flow, the Wallet Instance sends the Authorization Error Response to the Relying Party ``response_uri`` endpoint using an HTTP POST request. The error response MAY be unencrypted only where `OpenID4VP`_ permits it; a successful response MUST always be encrypted (:ref:`WP_090 <wallet-credential-presentation-testcases>`).
The Authorization Error Response MUST be encoded in the request body using the format defined by the ``application/x-www-form-urlencoded`` content type.

Below is a non-normative example of an Authorization Error Response.

.. code-block:: http

  POST /response_uri HTTP/1.1
  HOST: relying-party.example.org
  Content-Type: application/x-www-form-urlencoded

  state=3be39b69-6ac1-41aa-921b-3e6c07ddcb03&
  error=invalid_request&
  error_description=...

.. warning::
  The Wallet Instance MUST NOT send an error to an unauthenticated endpoint or reveal whether a Wallet or Credential is available. An error from one trust path MUST NOT trigger retry under the other path.

In the following table are listed error codes and descriptions that are supported for the Authorization Error Response:

.. list-table::
   :class: longtable
   :widths: 20 60
   :header-rows: 1

   * - **Error Code**
     - **Description**
   * - ``invalid_request_uri``
     - The `request_uri` in the authorization request returns an error, contains invalid data, or is otherwise malformed. :rfc:`9101`
   * - ``vp_formats_not_supported``
     - The Wallet Instance does not support any of the vp formats required by the Relying Party. `OpenID4VP`_
   * - ``invalid_request_uri_method``
     - The value of the ``request_uri_method`` parameter is neither ``get`` nor ``post``. `OpenID4VP`_
   * - ``invalid_request``
     - The request is malformed or inconsistent (e.g., it uses the ``vp_token`` Response Type but it does not include a ``dcql_query`` parameter), the Client Identifier Prefix is unsupported, or requirements of a prefix are violated (e.g., ``client_id`` with the ``x509_hash`` prefix without the required ``client_metadata``). `OpenID4VP`_
   * - ``access_denied``
     - The Wallet did not have the requested credential, the User did not consent, or the Wallet failed to authenticate the User. `OpenID4VP`_
    * - ``invalid_client``
      - The selected Relying Party trust path cannot authenticate or authorize the Relying Party. The Wallet Instance MUST NOT retry the other path. `OID-FED`_ and `OpenID4VP`_
   * - ``invalid_transaction_data``
     - One or more objects in the ``transaction_data`` structure are invalid. For instance, those objects contain unknown or unsupported types, malformed (e.g., it is an object of a known type but containing unknown fields or contains fields of the wrong type for the transaction data type) or missing fields, invalid values (e.g., the ``credential_ids`` does not match), or references to unavailable Credentials. `OpenID4VP`_

Relying Party Response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As defined in Section 8.2. (Response Mode ``direct_post``) of the `OpenID4VP`_ specification, if the Response URI has successfully processed the Authorization Response or Authorization Error Response, it MUST respond with an HTTP status code of 200 with ``Content-Type`` of ``application/json`` and a JSON object in the response body.

In every successful redirect-based **Same Device Flow**, the Relying Party MUST add the ``redirect_uri`` parameter to the JSON object in the response body. Upon receiving the ``redirect_uri``, the Wallet Instance MUST perform a redirect to the URL specified by the ``redirect_uri``. The Relying Party MUST reject an absent ``redirect_uri`` or a return in a different initiating user session.
This redirect allows the Relying Party to seamlessly resume interaction with the User on the device which initiated the flow, after the Wallet Instance has transmitted the Authorization Response to the designated ``response_uri``.

The Relying Party MUST include a response code within the ``redirect_uri``. The response code is a fresh, cryptographically random number used to ensure only the receiver of the redirect can fetch and process the Authorization Response. The number could be added as a path component, as a parameter or as a fragment to the URL. It is RECOMMENDED to use a cryptographic random value of 128 bits or more at the time of the writing of this specification.
Even if an adversary manages to steal the random value used in the request to the status endpoint, their user-agent would be rejected due to the missing cookie in the request.

.. warning::
  The ``redirect_uri`` parameter is subject to :ref:`endpoint-mix-up-protection` (:ref:`WP_094a <wallet-credential-presentation-testcases>`).

Relying Party Response Errors
--------------------------------

If any validation check, performed by the Relying Party on the Authorization Response from the Wallet Instance, fails; the Response URI endpoint MUST return an error response. The structure of this error response should be determined by the specific nature of the error encountered. The response MUST use ``application/json`` as the content type and MUST include the following parameters:

* ``error``: The error code.
* ``error_description``: Text in human-readable form providing further details to clarify the nature of the error encountered.

The following table lists the HTTP Status Codes and related error codes that MUST be supported for the error response:

.. list-table::
    :class: longtable
    :widths: 20 20 60
    :header-rows: 1

    * - **Status Code**
      - **Error Code**
      - **Description**
    * - ``400 Bad Request``
      - ``invalid_request``
      - The response cannot be processed because it is missing required parameters, contains invalid parameters or is otherwise malformed.
    * - ``400 Bad Request``
      - ``invalid_request``
      - The Credentials presented are malformed, invalid or revoked.
    * - ``400 Bad Request``
      - ``invalid_request``
      - The credential presentation, contained in the ``vp_token`` object, is malformed, doesn't have the required parameters or is incorrectly formatted.
    * - ``400 Bad Request``
      - ``invalid_request``
      - The "sd-jwt" returned is malformed, missing required parameters or incorrectly formatted.
    * - ``403 Forbidden``
      - ``invalid_request``
      - The signature of the KB-JWT is invalid or does not match the associated public key (JWK) referenced in the Issuer signed SD-JWT.
    * - ``403 Forbidden``
      - ``invalid_request``
      - The nonce value provided is incorrect or otherwise malformed.
    * - ``403 Forbidden``
      - ``invalid_request``
      - Trust could not be established with the Credential Issuer.
    * - ``500 Internal Server Error``
      - ``server_error``
      - The request cannot be fulfilled because the Response URI Endpoint encountered an internal problem.
    * - ``503 Service Unavailable``
      - ``temporarily_unavailable``
      - The request cannot be fulfilled because the Response URI Endpoint is temporarily unavailable (e.g., due to maintenance or overload).

Below there are two examples of HTTP responses using ``application/json`` that include both the ``error`` and ``error_description`` members:

.. code-block:: http

  HTTP/1.1 403 Forbidden
  Content-Type: application/json

  {
    "error": "invalid_request",
    "error_description": "Trust cannot be established with the issuer: https://issuer.example.com"
  }


.. code-block:: http

  HTTP/1.1 400 Bad Request
  Content-Type: application/json

  {
    "error": "invalid_request",
    "error_description": "The vp_token is malformed, missing required parameters or incorrectly formatted"
  }


Status Endpoint
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This specification introduces the Relying Party Status Endpoint for implementations that choose to use it. This endpoint is an internal security feature of the implementation and is not required for interoperability.

Whether the flow is Same Device or Cross Device, the user-agent needs to check the session status at the endpoint made available by the Relying Party (status endpoint).
This check MAY be implemented in the form of JavaScript code, within the page that shows the QRCode or the href button pointing to the request URL.
The JavaScript code makes the user-agent check the status endpoint using either a polling strategy (in seconds) or a push strategy (e.g., WebSocket).

Since the HTML page and the status endpoint are implemented by the Relying Party, the implementation details of this solution are the responsibility of the Relying Party, as this is related to the Relying Party's internal API. However, the text below describes an example implementation.

The Relying Party binds the request of the user-agent, with a session cookie marked as ``Secure`` and ``HttpOnly``, with the issued request.
The request url SHOULD include a parameter with a random value. The HTTP response returned by this status endpoint MAY contain the HTTP status codes listed below:

* **201 Created**. The signed Request Object was issued by the Relying Party that waits to be downloaded by the Wallet Instance at the ``request_uri`` endpoint.
* **202 Accepted**. This response is given when the signed Request Object was obtained by the Wallet Instance.
* **200 OK**. The Wallet Instance has provided the presentation to the Relying Party's ``response_uri`` endpoint and the User authentication is successful. The Relying Party updates the session cookie allowing the user-agent to access to the protected resource. A redirect URL is provided carrying the location where the user-agent is intended to navigate.

Status Endpoint Errors
------------------------

If instead any validation check performed by the Relying Party fails, the QRCode page SHOULD be updated with an error message. Moreover, the status endpoint MUST return an error response, whose structure depends on the nature of the error. The response MUST use ``application/json`` as the content type and MUST include the following parameters:

* ``error``: The error code.
* ``error_description``: Text in human-readable form providing further details to clarify the nature of the error encountered.

The following table lists the HTTP Status Codes and related error codes that MUST be supported for the error response:

.. list-table::
    :class: longtable
    :widths: 20 20 60
    :header-rows: 1

    * - **Status Code**
      - **Error Code**
      - **Description**
    * - ``401 Unauthorized``
      - ``authentication_failed``
      - The Wallet Instance or its User have rejected the request, the request is expired, or other errors prevented the authentication.
    * - ``403 Forbidden``
      - ``invalid_session``
      - Either the session id provided in the request is invalid.


Redirect URI
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The ``redirect_uri`` value MUST be used with an HTTP method GET by the user-agent to redirect the User to a specific Relying Party's endpoint in order to complete the process.


Redirect URI Errors
-----------------------------

When the user-agent is redirected to the Redirect URI provided by the Relying Party, several errors may occur that prevent the successful completion of the process. These errors are critical as they directly impact the User experience by hindering the seamless flow of information between the Wallet Instance and the Relying Party. Handling these errors requires clear communication to the User within the returned navigation web page. Relying Party MUST implement the error handling and validation mechanisms for Redirect URIs defined in this specification. Below are potential errors related to the Redirect URI, the error response MUST use ``application/json`` as the content type and MUST include the following parameters:

    - ``error``: The error code.
    - ``error_description``: Text in human-readable form providing further details to clarify the nature of the error encountered.

The following table lists the HTTP Status Codes and related error codes that MUST be supported for the error response:

.. list-table::
    :class: longtable
    :widths: 20 20 60
    :header-rows: 1

    * - **Status Code**
      - **Error Code**
      - **Description**
    * - ``403 Forbidden``
      - ``invalid_request``
      - The Redirect URI provided by the Relying Party does not match any of the URIs linked with the User session. (:rfc:`6749#section-4.1.2.1`)
    * - ``403 Forbidden``
      - ``invalid_request``
      - The User session is invalid or expired.
    * - ``500 Internal Server Error``
      - ``server_error``
      - The request cannot be fulfilled due to an internal server error. (:rfc:`6749#section-4.1.2.1`).
    * - ``503 Service Unavailable``
      - ``temporarily_unavailable``
      - The request cannot be fulfilled because the service is temporarily unavailable (e.g., due to maintenance or overload). (:rfc:`6749#section-4.1.2.1`).

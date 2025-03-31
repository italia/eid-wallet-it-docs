.. include:: ../common/common_definitions.rst

.. _proximity_flow.rst:

Proximity Flow
==============

This section describes how a Relying Party Instance requests the presentation of an *mdoc-CBOR* Credential to a Wallet Instance according to the *ISO 18013-5 Specification*. 

The high-level presentation phase is structured into three broad sub-phases as depicted in the following figure: 

.. figure:: ../../images/high-level-presentation-proximity.svg
    :figwidth: 100%
    :align: center
    :target: https://www.plantuml.com/plantuml/svg/TL9DYzim4BthLqnpoa8JquzJJqjt3IbigKbsAJq5HHeiKLboDUEaflI_T-ma9WrPNuIVvhrvyqRtn3fprmJrnaSJEelWc5lwL1HP7vQrPzVjEi9iKcICl3IfATgWuy1P4DlWTyN3nqKrG2zVduf64sCMQFkGcZR5WTCE-chrvR7SRfxBTVdj-KTLpk-KOiy1ORRojLiyuHu3L1b9A9fzYb0vJJXJgi9CASu76szXzYB7JCx69WCk1Ik_egK-fovQdVjvUw6nRGSDgRuXV0T_5CWt6PrRt7k3Muorhh4HH8Zlbl0umb1EyD1-WwRB2EHIvaNMiKQGZ2AQiSCE-O0OuRiE0HbqjB36qFjOGwKpzuD2IQntmPD30XyzUns0Zgh6QP4ACXV8T-MIa6WO3S_yazFtIzWShs2IFhijeybzosWlJHuyEo2diy1qOlx4_ZWT4tJjsG-Uw5FTRMScDKqNlHbJ5fKFIxcyW61npdADd3tkTVZVtBZJZByw92uoakWI0lusRWnux_LrGa9VIRe1wSAarQmdbbZzgvIaltqyFQ5RQpukW96aVAXTtteChoKVK5i2JXFtbSBhV33AxTXIgNkCjcl2Fm00
    
    High-Level Presentation Flow in proximity
 
The sub-phases are described below:

  1. **Device Engagement**: This subphase begins when the User is prompted to disclose certain attributes from the mdoc(s). The objective of this subphase is to establish a secure communication channel between the Wallet Instance and the Relying Party Instance, so that the mdoc requests and responses can be exchanged during the communication subphase.
  The messages exchanged in this subphase are transmitted through short-range technologies to limit the possibility of interception and eavesdropping.

  2. **Session establishment**: During the session establishment phase, the Relying Party Instance sets up a secure connection. All data transmitted over this connection is encrypted using a session key, which is known to both the Wallet Instance and the Relying Party Instance at this stage.
  The established session MAY be terminated based on the conditions as detailed in [`ISO18013-5`_ #9.1.1.4].

  3. **Communication - Device Retrieval**: The Relying Party Instance encrypts the mdoc request with the appropriate session key and sends it to the Wallet Instance together with its public key in a session establishment message. The mdoc uses the data from the session establishment message to derive the session key and decrypt the mdoc request.
  During the communication subphase, the Relying Party Instance has the option to request information from the Wallet Instance using mdoc requests and responses. The primary mode of communication is the secure channel established during the session setup. The Wallet Instance encrypts the mdoc response using the session key and transmits it to the mobile Relying Party via a session data message. 



Relying Party and Wallet Instances registered in the IT-Wallet ecosystem MUST support at least:

  - *Supervised Device Retrieval flow* where a human Relying Party is overseeing the verification process in person, in contrast with *unsupervised flow* where verification might happen through automated systems without human oversight.
  - *Device Engagement* based on QR Code.
  - *RP Instance Authentication* following the mechanisms defined in the `ISO18013-5`_ for the *reader authentication*.
  - *Device Retrieval* mechanism based on Bluetooth Low Energy (BLE) for the communication sub-phase. *Server Retrieval* mechanism MUST NOT be supported.
  - Domestic *Document Type* and *Namespaces* defined in this technical specification in addition to those already defined in the `ISO18013-5`_ for the mDL (see Section :ref:`MDOC-CBOR` for more details).
  - *Wallet Instance validation* through the Wallet Attestation.


The following figure illustrates the low-level flow compliant with ISO 18013-5 for proximity flow.

.. _fig_High-Level-Flow-ITWallet-Presentation-ISO-updated:
.. figure:: ../../images/High-Level-Flow-ITWallet-Presentation-ISO-updated.svg
    :figwidth: 100%
    :align: center
    :target: https://www.plantuml.com/plantuml/svg/ZLF1RXD13BtdAwmzKQdXmB52LQ694094IQXwuUBCECcekvx1uyrg_nxlxZHAH8FOGwJCFB_t_EovougYRLFFiDN8RRCXcSt0FdGQ1Hup2M26TZmRVv8L11SIiaBrX7LD2eySj1fmtT-GrGDyPfDXHoFaCF6ty_djRNS3tnCnw9vWeZfY9z3xkM6AYzPGRBoe8J9i-jUg8CfmW_2qlb-y2DqUEJfpb44Z9A5iPD3uw60HTa6nXdiXFoXWdSVAc1I-8NlKA3s4BQoLqlmTX0mS5HB9Daf3tXGdFR2lCyljHSj76B6Vu9ExJyGag0HC7L3QKqDYZfwfXuH1u1U_gQhbWWx1qHVgtpv8E5JLDPmVjfkgkYgqndkuWVK-TcDEFrPm7pr1O5UtFl3EIgVA9UzmPtgiLJNM7ifarWxvjBPS6k__-8N1y8hGavmRBeVdXWklwJIfLO9CEOV80s7PlFATWX-44We1GWux9W_87eYTz4c7VweIDiPcReH-jvHrCBMUg9TPSLE7l9ywBowcpY-181v8uEFN9MHohH2uFJ9JVJh9InsKwmMDzYvB33sOIjZs43IFdQ6Qrf74bcjLki6K91wm1jl3bvKUHfkf9dSMGRws45na9JRIk0MXNSWgqs8w4WtROKtfzCbyAFIJT5aeOdyfS3EG8cSwINc1YXQkYNT1zr36SERidw6MIP-dTkIzVZMfuR7uSRLX4tZOzQl1gF6IUvvUl3KLVD3--69Dep33Jv8cy1ZCx8xOjqtz1m00
    
    High-Level Proximity Flow


**Step 1**: The User opens the Wallet Instance initiating the process.

**Step 2**: The User authenticates itself to the Wallet Instance. This can be done by the Wallet Instance or a Wallet Secure Cryptographic Device (WSCD). It is a prerequisite for accessing sensitive data and presenting attributes.

**Step 3**: The User explicitly indicates their intention to present their mdoc Digital Credentials.

**Step 4**: [Optional] If the initial authentication in Step 2 was not done through WSCD, a separate authentication via WSCD might be required before presenting sensitive credentials like the mdoc.

**Step 5**: The Wallet Instance generates a new ephemeral Elliptic Curve key pair for secure communication. The public key (``EDeviceKey.Pub``) will be used for session encryption. This is part of the device engagement process.

**Step 6**: The Wallet Instance presents a QR Code to the Relying Party Instance. This QR code contains the `DeviceEngagement data`, which includes the ``EDeviceKey.Pub`` and information about supported copter suits.

Below an example of a device engagement structure that utilizes QR for device engagement and Bluetooth Low Energy (BLE) for data retrieval.

CBOR data represented in AF Binary format:

.. code-block:: 

  a26776657273696f6e63312e3...

The same content shown above using the diagnostic notation:

.. code-block::

  {
    0: "1.1", % Version (Updated to 1.1 because Capabilities and OriginInfos are present)
    1: % Security
    [
      1, % defines the cipher suite , which contains only EC curves
      24(<< % embedded CBOR data item
        {
          1: 2, % kty:EC2 (Elliptic curves with x and y coordinate pairs)
          -1: 1, % crv:p256
          -2:h'5A88D182BCE5F42EFA59943F33359D2E8A968FF289D93E5FA444B624343167FE', % x-coordinate
          -3:h'B16E8CF858DDC7690407BA61D4C338237A8CFCF3DE6AA672FC60A557AA32FC67' % y-coordinate
        }
      >>)
    ],
    2: % DeviceRetrievalMethods (Device engagement using QR code with BLE for retrieval)
    [
      [
        2, % BLE
        1, % Version
        { % BLE options
          0: false, % no support for mdoc peripheral server mode
          1: true,  % support for mdoc central client mode
          11: h'45EFEF742B2C4837A9A3B0E1D05A6917' % UUID of mdoc client central mode
        }
      ]
    ],
    5: % OriginInfos (Required because Capabilities is present)
    [],
    6: % Capabilities (Defines supported features)
    {
      2: false, % HandoverSessionEstablishmentSupport (Supports negotiated handover)
      3: true % ReaderAuthAllSupport (Supports reader authentication)
    }
  }

**Step 7**: The verifier uses its Relying Party Instance to scan the QR code and retrieve the DeviceEngagement data from the mdoc.

**Step 8**: The Relying Party Instance generates its ephemeral key pair (``EReaderKey.Priv``, ``EReaderKey.Pub``). The private key (``EReaderKey.Priv``) MUST be kept secret, and the public key (``EReaderKey.Pub``) MUST be used in establishing the session.

**Step 9**: The Wallet Instance and Relying Party Instance independently MUST derive the session keys using their private ephemeral key and the other party's public ephemeral key through a key agreement protocol. This ensures session encryption. In this particular step, the Relying Party Instance MUST compute its session key.

**Step 10**: The RP Instance MUST prepares a `SessionEstablishment` message. This message MUST be signed by the Relying Party Instance (mdoc reader authentication as specified in [`ISO18013-5`_ #9.1.1.4]) and encrypted using the session keys derived in the previous step. The `SessionEstablishment` message MUST include the ``EReaderKey.Pub`` and a request for specific attribute(s).

The mdoc request MUST contain a Wallet Attestation (WA) request along with other requests for Digital Credentials, and MUST be encoded in CBOR, as demonstrated in the following non-normative example.

CBOR data in AF Binary format: 

.. code-block::

  a36776657273696f6e63312e306b646f63...


The above CBOR data is represented in diagnostic notation as follows:

.. code-block::

  {
    "version": "1.0",  % Version
    "docRequests": 
    [
      {
        "itemsRequest": 
        24(<<  % Embedded CBOR data item
          {
            "docType": "org.iso.18013.5.1.mDL",
            "nameSpaces": 
            {
              "org.iso.18013.5.1": 
              {
                "family_name": true,
                "document_number": true,
                "driving_privileges": true,
                "issue_date": true,
                "expiry_date": true,
                "portrait": false
              }
            }
          }
        >>)
      },
      {
        "itemsRequest": 24(<<  % Embedded CBOR data item
          {
            "docType": "org.iso.18013.5.1.it.WalletAttestation",
            "nameSpaces": {
              "org.iso.18013.5.1.it": {
                "iss": true,
                "sub": true,
                "wallet_name": true,
                "wallet_link": true
              }
            }
          }
        >>)
      }
    ],
    "readerAuthAll": [
      h'a10126', % COSE_Sign1 authentication header
      {
        33: h'308201253081cda00302010202012a300a06082a8648ce3d0403023020311e301c06035504030c15536f6d652052656164657220417574686f72697479301e170d3233313132343130323832325a170d3238313132323130323832325a301a3118301606035504030c0f536f6d6520526561646572204b65793059301306072a8648ce3d020106082a8648ce3d03010703420004aa1092fb59e26ddd182cfdbc85f1aa8217a4f0fae6a6a5536b57c5ef7be2fb6d0dfd319839e6c24d087cd26499ec4f87c8c766200ba4c6218c74de50cd1243b'
      },
      null, % No additional reader authentication
      h'58a0d421a7e53b7db0412a196fea50ca6d4c8a530a47dd84d88588ab145374bd0ab2a724cf2ed2facf32c7184591c5969efd53f5aba63194105440bc1904e1b9'  % Reader authentication signature
    ]
  }

**Step 11**: The Relying Party Instance MUST transmit the encrypted and signed `SessionEstablishment` message to the Wallet Instance over a secure BLE connection that was established based on the device engagement information.

**Step 12**: The Wallet Instance MUST compute the session key, as described in Step 9.

**Step 13**: Upon receiving the `SessionEstablishment` message, the Wallet Instance MUST decrypt it using the shared session key and MUST verify the Relying Party instance's signature (mdoc reader authentication as specified in [`ISO18013-5`_ #9.1.1.4]) to ensure its authenticity.

**Step 14**: The Wallet Instance MUST decrypt the attribute request and MUST prompt the user for their consent to share the requested attributes. It MUST also display the contents of the Relying Party's registration certificate to ensure transparency about the requested data and its registered purpose.

**Step 15**: The user reviews the request and the Relying Party's registration information and then approves the presentation of the requested attributes. 

**Step 16**: After receiving user approval, the Wallet Instance MUST retrieve the requested mdoc Digital Credentials. It then MUST prepare a `SessionData` message containing these Digital Credentials, and it MUST sign it (mdoc authentication as specified in [`ISO18013-5`_ #9.1.3]). It MUST encrypt it using the established session keys before transmitting it to the Relying Party Instance over the secure BLE channel. The signing ensures device binding and data integrity.

The mdoc response MUST be encoded in CBOR, with its structure outlined in [`ISO18013-5`_ #8.3.2.1.2.2].

CBOR Data:

.. code-block::

  a26776657273696f6e63312e3069646f637...

In diagnostic notation:

.. code-block::

  {
    "version": "1.0",
    "documents": 
    [
      {
        "docType": "org.iso.18013.5.1.mDL",
        "issuerSigned": 
        {
          "nameSpaces": 
          {
            "org.iso.18013.5.1": 
            [
              24(<<
                {
                    "digestID": 0,
                    "random": h'87986C20E9',
                    "elementIdentifier": "family_name",
                    "elementValue": "Doe"
                }
              >>),
              24(<<
                {
                    "digestID": 3,
                    "random": h'B23F6244615D',
                    "elementIdentifier": "issue_date",
                    "elementValue": "2019-10-20"
                }
              >>),
              24(<<
                {
                    "digestID": 4,
                    "random": h'C7FFA30E9ABAF',
                    "elementIdentifier": "expiry_date",
                    "elementValue": "2024-10-20"
                }
              >>),
              24(<<
                {
                    "digestID": 7,
                    "random": h'26052A4F5B5F9E68',
                    "elementIdentifier": "document_number",
                    "elementValue": "123456789"
                }
              >>),
              24(<<
                {
                    "digestID": 9,
                    "random": h'4599F81BEAA2CDB2AB2CE4',
                    "elementIdentifier": "driving_privileges",
                    "elementValue": [
                        {
                            "vehicle_category_code": "A",
                            "issue_date": "2018-08-09",
                            "expiry_date": "2024-10-20"
                        },
                    ],
                }
              >>)
            ]
          },
          "issuerAuth": 
          [
            << {1: -7} >>,
            {
              33: h'308201EF30943BF5AE82C0943BF5AE943BF943BF5AE5A943BF5AEED3A68D943BF5AE'
            },
            <<
              24(<<
                {
                  "version": "1.0",
                  "digestAlgorithm": "SHA-256",
                  "docType": "org.iso.18013.5.1.mDL",
                  "valueDigests": {
                    "org.iso.18013.5.1": 
                    {
                      0: h'751ADCEBF',
                      1: h'67E5394571',
                      2: h'33943BF5AE',
                      3: h'2E35613D55',
                      4: h'EA5C330D59',
                      5: h'FAE487AA1D',
                      6: h'7D83E7533',
                      7: h'F05498936',
                      8: h'B68C87F66',
                      9: h'0B35D6E0C',
                      10: h'C98A14881',
                      11: h'B57DDA948',
                      12: h'651F812DA'
                    }
                  },
                  "deviceKeyInfo": {
                    "deviceKey": {
                      1: 2, 
                      -1: 1, 
                      -2: h'9631F9A',
                      -3: h'1FB3C3D6'
                    }
                  },
                  "validityInfo": {
                    "signed": "2020-10-01T13:30:02Z",
                    "validFrom": "2020-10-01T13:30:02Z",
                    "validUntil": "2021-10-01T13:30:02Z"
                  },
                  "status": {
                    "status_list": {
                      "idx": 1340,
                      "uri": "https://statusprovider.example.org//statuslists/1"                           
                    }
                  }
                }
              >>)
            >>,
            h'59E64205DF1E766AEFF13CB2E'
          ]
        },
        "deviceSigned": 
        {
          "nameSpaces": 24(<< {} >>),
          "deviceAuth": 
          {
            "deviceSignature": 
            [
              << {1: -7} >>,
              {},
              null,
              h'E99521A85AD75943BF5AEAE68943BF5AE249943BF5AE943BF5AE43BF5AED'
            ]
          }
        }
      },
      {
        "docType": "org.iso.18013.5.1.it.WalletAttestation",
        "issuerSigned": 
        {
          "nameSpaces": 
          {
            "org.iso.18013.5.1.it": 
            [
              24(<<
                {
                  "digestID": 0,
                  "random": h'37986C20A9',
                  "elementIdentifier": "wallet_name",
                  "elementValue": "Wallet_Hobbiton_v1"
                }
              >>),
              24(<<
                {
                  "digestID": 1,
                  "random": h'37986C20A9',
                  "elementIdentifier": "wallet_link",
                  "elementValue": "https://example.com/wallet/detail_info.html"
                }
              >>),
              24(<<
                {
                  "digestID": 2,
                  "random": h'37986C20A9',
                  "elementIdentifier": "sub",
                  "elementValue": "vbeXJksM45xphtANnCiG6mCyuU4jfGNzopGuKvogg9c"
                }
              >>),
              24(<<
                {
                  "digestID": 3,
                  "random": h'37986C20A9',
                  "elementIdentifier": "aal",
                  "elementValue": "https://trust-list.eu/aal/high"
                }
              >>)
            ]
          },
          "issuerAuth": 
          [
            << {1: -7} >>,
            {
              33: h'308201EF3943BF5AE0943BF5AE82C0943943BF5AEBF5AED3A943BF5AE68D'
            },
            <<
              24(<<
                {
                  "version": "1.0",
                  "digestAlgorithm": "SHA-256",
                  "docType": "org.iso.18013.5.1.it.WalletAttestation",
                  "valueDigests": {
                    "org.iso.18013.5.1.it": {
                      0: h'0F1571A988FCDF2929…',
                      1: h'0CDFE0774A2B596C90…',
                      2: h'E23821492558984395…',
                      3: h'BBC77E6CCE544EDF86…'
                    }
                  },
                  "deviceKeyInfo": {
                    "deviceKey": {
                      1: 2,
                      -1: 1,
                      -2: h'B820963964E5…',
                      -3: h'0A6DA0AF437E…'
                    }
                  },
                  "validityInfo": {
                    "signed": "2020-10-01T13:30:02Z",
                    "validFrom": "2020-10-01T13:30:02Z",
                    "validUntil": "2021-10-01T13:30:02Z"
                  }
                }
              >>)
            >>,
            h'59E64205DF1E766AEFF13CB2E'
          ]
        },
        "deviceSigned": 
        {
          "nameSpaces": 24(<< {} >>),
          "deviceAuth": 
          {
            "deviceSignature": 
            [
              << {1: -7} >>,
              {},
              null,
              h'E42521A85A...'
            ]
          }
        }
      }
    ],
    "status": 0
  }

**Step 17**: The Relying Party Instance receives the SessionData, then it MUST decrypt it, and it MUST verify the Wallet Instance's signature to ensure the data's integrity and that it originates from the expected device (device binding). It also MUST check the validity of the mdoc, including its issuer's signature. In case of long-lived Digital Credentials, it SHOULD also check the revocation status using :ref:`OAuth Status List`.

**Step 18**: Once the data exchange is complete, either party can terminate the session. If BLE is used, this can involve sending a status code for session termination or the “End” command. In this scenario, the GATT Client (Relying Party Instance) MUST unsubscribe from characteristics and disconnect from the GATT server (Wallet Instance). 

**Final Consideration**: The presentation flow focused on the technical data exchange in proximity settings. It is crucial to recognise that supervised proximity flows involving a human verifier play a vital role in many use cases (e.g., age verification at a store, identity check by law enforcement). The human element adds a layer of identity verification through visual inspection and comparison, contributing to User Binding and overall authentication assurance aspects not fully captured in a purely technical presentation flow.

.. note::

  During proximity presentation the Wallet Instance might not be able to fetch a fresh Wallet Attestation, in this case, the Wallet Instance SHOULD send the latest version of the Wallet Attestation. It is left up to the Relying Party to determine whether a presentation with a valid but expired Wallet Attestation is valid or not.

Device Engagement
-----------------

The Device Engagement structure MUST be have at least the following components:

  - **Version**: *tstr*. Version of the data structure being used.
  - **Security**: an array that contains two mandatory values
  
    - the cipher identifier: see Table 22 of `ISO18013-5`_
    - the public ephemeral key generated by the Wallet Instance and required by the Relying Party Instance to derive the Session Key. The public ephemeral key MUST be of a type allowed by the indicated cipher suite.
  - **transferMethod**: an array that contains one or more `transferMethod` arrays when performing device engagement using the QR code. This array is for offline data retrieval methods. A `transferMethod` array holds two mandatory values (``type`` and ``version``). Only the BLE option MUST be supported by this technical implementation profile, then the type value MUST be set to ``2``. 
  - **BleOptions**: this elements MUST provide options for the BLE connection such as Peripheral Server or Central Client Mode, and the device UUID. Only Central Client Mode MUST be supported by this technical implementation profile.


mdoc Request
------------

The messages in the mdoc Request MUST be encoded using CBOR. The resulting CBOR byte string for the mdoc Request MUST be encrypted with the Session Key obtained after the Device Engagement phase and MUST be transmitted using the BLE protocol.
The mdoc Request, including identifier and format of the data elements, MUST be compliant to the following structure: 

  - **version**: (tstr). Version of the data structure.
  - **docRequests**: Requested DocType, NameSpace and data elements.

    - **itemsRequest**: #6.24(bstr .cbor ItemsRequest).

      - **docType**: (tstr). The DocType element contains the type of document requested. See Section :ref:`MDOC-CBOR`.
      - **nameSpaces**: (tstr). See Section :ref:`MDOC-CBOR` for more details.

        - **dataElements**: (tstr). Requested data elements, it MUST contain the *Intent to Retain* value for each requested element.

          - **IntentToRetain**: (bool). It indicates that the Relying Party intends to retain the received data element.  
    - **readerAuth**: *COSE_Sign1*. It is required for the Relying Party Instance authentication. 


mdoc Response
-------------

The messages in the mdoc Response MUST be encoded using CBOR and MUST be encrypted with the Session Key obtained after the Device Engagement phase.
The details on the structure of mdoc Response are provided below. 

  - **version**: (tstr). Version of the data structure.
  - **documents**: Returned *DocType*, and *ResponseData*.

    - **docType**: (tstr). The DocType element contains the type of document returned. See Section :ref:`MDOC-CBOR`.
    - **ResponseData**:

      - **IssuerSigned**: It MUST contain the `Namespaces` and `Mobile Security Object` as specified in Section :ref:`MDOC-CBOR`.
      - **DeviceSigned**: Responded data elements signed by the Wallet Instance.

        - **NameSpaces**: #6.24(bstr .cbor DeviceNameSpaces). The DeviceNameSpaces structure MAY be an empty structure. DeviceNameSpaces contains the data element identifiers and values. It is returned as part of the corresponding namespace in DeviceNameSpace.

          - **DataItemName**: (tstr). The identifier of the element.
          - **DataItemValue**: (any). The value of the element.
        - **DeviceAuth**:  The DeviceAuth structure MUST contain the DeviceSignature elements.

          - **DeviceSignature**: It MUST contain the device signature for the Wallet Instance authentication. 
  - **status**: It contains a status code. For detailed description and action required refer to to Table 8 (ResponseStatus) of the `ISO18013-5`_


Session Termination
-------------------

The session MUST be terminated if at least one of the following conditions occur. 

  - After a time-out of no activity of receiving or sending session establishment or session data messages occurs. The time-out for no activity implemented by the Wallet Instance and the Relying Party Instance SHOULD be no less than 300 seconds.
  - When the Wallet Instance doesn't accept any more requests.
  - When the Relying Party Instance does not send any further requests. 

If the Wallet Instance and the Relying Party Instance does not send or receive any further requests, the session termination MUST be initiated as follows. 

 - Send the status code for session termination, or
 - dispatch the "End" command as outlined in [`ISO18013-5`_ #8.3.3.1.1.5].

When a session is terminated, the Wallet Instance and the Relying Party Instance MUST perform at least the following actions: 

  - destruction of session keys and related ephemeral key material; 
  - closure of the communication channel used for data retrieval.




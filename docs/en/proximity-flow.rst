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
    :target: https://www.plantuml.com/plantuml/svg/ZLF1RXCn4BtdAqPxebBBWME5K4iR8GI8a53rmiMn9udLtR6nnxlaxndR6yaHZSGUejYUUU_Dy_DTP1Ku3Vr29NQKXYs6nGBaKvfTWAU80LI4LFRAZvS6gwrNnD0zgxv7XYUotEMwwT-IzGe-az2Gnb8oLlnqys6wXUyU2VY0C0ETAayIxAWOPzJqlhHKIKcQI4WKMqUmFRu60Yxa4mNFcuVxXhL2HEnHSooDFhW_Th1yb7yO1RZ2xXBf_4VrSbJwdMVufiWeCUS8TWSRHW_lm4OWn-0nx5mOq0XlPGNv9X6UBWXlof1CBIyQFo5XoCCJJe3-W8CiUtX1qQXiW5_qfkkMZpXQZL_m-7OLxDXrrt2-cRPTTtL27MzXSt1JcVZ76XwSGR2a-sGixQMnzYrfh_R2HjnrvzSmbkLuK_HjjA8MgPu9oVz8XwnzZSfWQBMtcuts2YiiWq-26Z76x9tWdL9PlwPs5L12YA0WsZsX0KK6a7GuUiuhvc2t0YPQ0lvE63bBsbJaPMIrxMqyL1Eksh4l5O4RCS37hqk8g9CmwuCYmhwvqKlww-aZ5d6N2V84mc5taZkEPIx5mZHZb8YjvrcKbqIFuhcayHHfkUCvywq1yLeiq8uOIK3T3WBkRUHGuwaniDtbi6BpVEvdz3PNIEQIsKBl7KLi77vKhCHOePui7w1UmRckIuOsbznOri9UlsfJVZ2c11osbdBYhx9EWKNz0eDn6cGaQ-fBhuzME6Pa-8bXi5HSASS6ssTnlZ4jxf1C6lg_
    
    High-Level Proximity Flow


**Step 1**: The User opens the Wallet Instance initiating the process.

**Step 2**: The User authenticates itself to the Wallet Instance. This can be done by the Wallet Instance or a Wallet Secure Cryptographic Application (WSCA). It is a prerequisite for accessing sensitive data and presenting attributes.

**Step 3**: The User selects the proximity presentation functionality.

**Step 4**: [Optional] If the initial authentication in Step 2 was not done through WSCA, a separate authentication via WSCA MAY be required.

**Step 5**: The Wallet Instance generates a new ephemeral Elliptic Curve key pair for secure communication. The public key (``EDeviceKey.Pub``) will be used for session encryption. This is part of the device engagement process.

**Step 6**: The Wallet Instance presents a QR Code to the Relying Party Instance. This QR code contains the ``DeviceEngagement`` data, which includes the ``EDeviceKey.Pub`` and information about supported cipher suites.

Below a non-normative example using the diagnostic notation of a CBOR-encoded ``DeviceEngagement`` that utilizes QR for device engagement and Bluetooth Low Energy (BLE) for data retrieval.

.. literalinclude:: ../../examples/iso-device-engagement.txt
  :language: text

**Step 7**: The verifier uses its Relying Party Instance to scan the QR code and retrieve the ``DeviceEngagement`` data from the mdoc.

**Step 8**: The Relying Party Instance generates its ephemeral key pair (``EReaderKey.Priv``, ``EReaderKey.Pub``). The private key (``EReaderKey.Priv``) MUST be kept secret, and the public key (``EReaderKey.Pub``) MUST be used in establishing the session.

**Step 9**: The Wallet Instance and Relying Party Instance independently MUST derive the session keys using their private ephemeral key and the other party's public ephemeral key through a key agreement protocol. This ensures session encryption. In this particular step, the Relying Party Instance MUST compute its session key.

**Step 10**: The RP Instance MUST prepare a ``SessionEstablishment`` message. This message MUST be signed by the Relying Party Instance (mdoc reader authentication as specified in [`ISO18013-5`_ #9.1.1.4]) and encrypted using the session keys derived in the previous step. The ``SessionEstablishment`` message MUST include the ``EReaderKey.Pub`` and a request for specific attribute(s).

Below a non-normative example using the diagnostic notation of a CBOR-encoded ``SessionEstablishment`` that contains the mdoc request of a Wallet Attestation along with an mDL Digital Credential.

.. literalinclude:: ../../examples/iso-session-establishment.txt
  :language: text

**Step 11**: The Relying Party Instance MUST transmit the encrypted and signed ``SessionEstablishment`` message to the Wallet Instance over a secure BLE connection that was established based on the device engagement information.

**Step 12**: The Wallet Instance MUST compute the session key, as described in Step 9.

**Step 13**: Upon receiving the ``SessionEstablishment`` message, the Wallet Instance MUST decrypt it using the shared session key and MUST verify the Relying Party Instance's signature (mdoc reader authentication as specified in [`ISO18013-5`_ #9.1.1.4]) to ensure its authenticity.

**Step 14**: The Wallet Instance MUST decrypt the attribute request and MUST prompt the User for their consent to share the requested attributes. It MUST also display the contents of the Relying Party's registration certificate to ensure transparency about the requested data and its registered purpose.

**Step 15**: The User reviews the request and the Relying Party's registration information and then approves the presentation of the requested attributes. 

**Step 16**: After receiving User approval, the Wallet Instance MUST retrieve the requested mdoc Digital Credentials. It then MUST prepare a `SessionData` message containing these Digital Credentials, and it MUST sign it (mdoc authentication as specified in [`ISO18013-5`_ #9.1.3]). It MUST encrypt it using the established session keys before transmitting it to the Relying Party Instance over the secure BLE channel. The signing ensures device binding and data integrity. The mdoc response MUST be encoded in CBOR, with its structure outlined in [`ISO18013-5`_ #8.3.2.1.2.2].

Below a non-normative example using the diagnostic notation of a CBOR-encoded ``SessionData`` that contains the mdoc response of a Wallet Attestation and an mDL.

.. literalinclude:: ../../examples/iso-session-data.txt
  :language: text

**Step 17**: The Relying Party Instance receives the ``SessionData``, then it MUST decrypt it, and it MUST verify the Wallet Instance's signature to ensure the data's integrity and that it originates from the expected device (device binding). It also MUST check the validity of the mdoc, including its Issuer's signature. In case of long-lived Digital Credentials, it SHOULD also check the revocation status using :ref:`OAuth Status List`.

**Step 18**: Once the data exchange is complete, either party can terminate the session. If BLE is used, this can involve sending a status code for session termination or the “End” command. In this scenario, the GATT Client (Relying Party Instance) MUST unsubscribe from characteristics and disconnect from the GATT server (Wallet Instance). 

**Final Consideration**: The presentation flow focused on the technical data exchange in proximity settings. It is crucial to recognise that supervised proximity flows involving a human verifier play a vital role in many use cases (e.g., age verification at a store, identity check by law enforcement). The human element adds a layer of identity verification through visual inspection and comparison, contributing to User Binding and overall authentication assurance aspects not fully captured in a purely technical presentation flow.

.. note::

  During proximity presentation the Wallet Instance might not be able to fetch a fresh Wallet Attestation, in this case, the Wallet Instance SHOULD send the latest version of the Wallet Attestation. It is left up to the Relying Party to determine whether a presentation with a valid but expired Wallet Attestation is valid or not.

Device Engagement
-----------------

The Device Engagement structure MUST have at least the following components:

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
- **status**: It contains a status code. For detailed description and action required refer to to Table 8 (ResponseStatus) of the `ISO18013-5`_.


Session Termination
-------------------

The session MUST be terminated if at least one of the following conditions occur:

- after a time-out of no activity of receiving or sending session establishment or session data messages occurs. The time-out for no activity implemented by the Wallet Instance and the Relying Party Instance SHOULD be no less than 300 seconds;
- when the Wallet Instance does not accept any more requests;
- when the Relying Party Instance does not send any further requests. 

If the Wallet Instance and the Relying Party Instance does not send or receive any further requests, the session termination MUST be initiated as follows: 

- send the status code for session termination, or
- dispatch the "End" command as outlined in [`ISO18013-5`_ #8.3.3.1.1.5].

When a session is terminated, the Wallet Instance and the Relying Party Instance MUST perform at least the following actions: 

- destruction of session keys and related ephemeral key material; 
- closure of the communication channel used for data retrieval.




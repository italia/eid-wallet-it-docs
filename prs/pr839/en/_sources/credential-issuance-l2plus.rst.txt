.. include:: ../common/common_definitions.rst

eID Substantial Authentication with MRTD Verification for PID Issuance
=======================================================================

This Section defines an eID Substantial Authentication with MRTD Verification protocol that integrates within the PID issuance flow as defined in the Section :ref:`credential-issuance-low-level:Credential Issuance Low-Level Flows` extending OAuth 2.0 flows to include:

	- Electronic identification with Level of Assurance "Substantial" (LoA3).
	- Electronic document verification as an additional identity verification layer.
	- Session correlation and security binding between authentication steps.
	- Integration with Credential issuance flows.

While CIEid with LoA High authentication remains the primary method for Wallet activation and PID issuance, the eID Substantial Authentication with MRTD Verification mechanism defined in this Section provides an alternative approach to enhance service accessibility and usability, without compromising the overall security of the IT-Wallet ecosystem.

.. note::
  This Section currently only supports the CIE id card for the MRTD verification protocol, the protocol described in this Section MAY be extended to support other MRTD Documents such as Electronic Passports.

Design Principles
-----------------

The protocol adheres to the following design principles:

	- **Standard Compatibility**: Extends existing authorization frameworks without breaking changes to the standard OAuth 2.0 Authorization Framework.
	- **Multi-Step Authentication**: Implement progressive enforcement of authentication with MRTD verification.
	- **Session Integrity**: Maintains secure session correlation across authentication steps.
	- **Unified Flow**: Integrates multiple authentication factors in a single authorization session.

System Architecture
-------------------

The system architecture comprises the following main components:

	- **Wallet Instance:** It handles the PID request according to IT-Wallet Specification, supporting additional cryptographic capabilities for MRTD/IAS Electronic Document reading according to `ICAO 9303`_ and `BSI-03110`_ specifications.
	- **eID Substantial Authentication with MRTD Verification System:** Orchestrates the authentication flow, integrating LoA3 Identity Providers, Electronic Document Verification Service, and performing all the identity correlation checks to guarantee that the User requesting a PID mathes with the authenticated one.

		- **PID Authorization Server:** Handles the authorization flow for PID Issuance, coordinating the User authentication and the remote identity proofing.
		- **MRTD PoP Service:** Handles electronic document proof of possession with cryptographic document validation.

	- **LoA3 Identity Provider:** Provides Electronic Identification Schemes with eIDAS LoA3 compliance (CIEid and SPID).
	- **CIE National Registry:** Provides privacy-preserved evidence of the binding between NIS and User's Tax payer's identification number required for the MRTD verification and, optionally, the MRZ data (document number, date of birth, expiry date, citizenship and gender) to improve the User experience. It also provides information related to the validity status of the document. It acts as the authoritative source for the CIE.

.. _fig_eID_MRTD_System_Architecture:
.. plantuml:: plantuml/l2plus-system-architecture.puml
    :width: 99%
    :alt: The figure illustrates the eID Substantial Authentication with MRTD Verification System Architecture.
    :caption: `eID Substantial Authentication with MRTD Verification System Architecture. <https://www.plantuml.com/plantuml/svg/ZLJlRzis4Fskl-9g38ZZHNDQPnysT44LMri4v8TXUIqw311eyXmJbKIDfEowG__t7IbRLPGKYv4F2dbyz-xTktjdBDEsBlBWv9NTO870KTSviZ9KjSrbYS4hMVAy5WXlfnVZwKKsLKMbIYpjPN2TpE8iNSQB-7xvSHuFJuEJc-ZZ_P_Bx4EolCvkuZ_YkncT1YSmmpM1GJfV9CiuxO3Qkc92JyPS5OKgBv-vMQlIXco7HXKO_ZmMpB8LC_Y2K8DwY_e5WL9ad6dnWiWTotEq_nSubgMnqjPMkf82-imHRjxy2BTrRcMOMgmWgkr6QVc5kI28DDz8YzpM6eEWrJYBFzjXa_CC1X_y1oG4pagE0pgwLIj9s55LkV-kMIboD31FPg3ndngD1QUL04f1_OLa6Hv0ADUcLBbws8D34rI---2VVg8WgBJQIa58en7N-ygg1ysgZUJ0MSKeexIIBjTAm-rYEKwY5EASo6jLKinCyReWyaI12La-Z4OmJARHFVmoEP-SmLMQXEUJrw_FJmTdFvXAKzc_3PeQ1-ILArKxDlkXDAP6JLMvQkOD8JquXNy3e5yRLZX9CqEIPema_K8FlgjokgUumYbrJtgJEffPggFmyGu270HHbxnviCxL3aWTq5WeYo25kxHx9v1QKsqj7_ThspQif6ZOP8q7AMEFYJ_sJDp5cnxHtpKhSAVq9v_yFfbTl9yct-cm3s7jyvOsLqgJ_FwaetH3Y9H-obeedbMgyfmbHqf7tINjrTppbOtbthDS2e_QEMs9uJSVYACFl5X0VvKo1ernJtVIRg3hhKxyrcVeyJxCw87ur-1hVqnonIQP51MHkL7H199Zhrhlq0qcCpAhlwTFICa5XUT_239T8pS8wwCPcc03msaII-5bJwaFNHjtvfw8zWXoYPd61qcssrD6Ge4xZynoM1pE1uUBMRFb7bEZ95l6zs6bqNTH0BgBagCJzov98OGb-mmLswC-CI0Vyo_hOeKQLh9qK-dvgwh9d-zfaFy2GLbf_cqx_tvf-7P8wnU5hGtbyiTjkuOQjwh9qTNYkAYT40lCspNMdurs1XhR_btIMl7-JcW17FVSbLOx2W_zDkiZFlNjxB7rJBqgfFUTmuhcYKFeyu2tuMKV2dw5mMZKEkcMMRxn6stW6MHNj32V6VQE5TFezcPC0ppjhPPdYseXdrJKyquaX6mwrzssERCeV1E_bVaEIr4N-Ny0>`_

High-Level Flow
---------------

The protocol consists of the following sequential phases:

1. **OAuth Authorization Request**: PAR and authorization request with eID Substantial Authentication with MRTD Verification.
2. **Primary Authentication**: LoA3 electronic identification (SPID/CIEid L2).
3. **MRTD Proof of Possession (PoP) Validation**: Electronic document reading and cryptographic verification (Proof of Possession, integrity, and authenticity checks).
4. **OAuth Authorization Response**: Final authorization code issuance.

.. _fig_eID_MRTD_High_Level_Flow:
.. plantuml:: plantuml/l2plus-high-level-flow.puml
    :width: 99%
    :alt: The figure illustrates the eID Substantial Authentication with MRTD Verification High-Level Flow.
    :caption: `eID Substantial Authentication with MRTD Verification High-Level Flow. <https://www.plantuml.com/plantuml/png/ZPHnY-984CN_zrFKUGSp0piuYN6Lmv4Tr6M5MLPK5kulwQGhiRbETwwxCfxxwJUTQ2QACW4HxRp-zUkgb_fYYHdAKma_NdBQmVTSadXS4sRW_gCY4J4IMi4taUmUN_4D9NoLUj_vGwX8vXnXF0rwqs0xrMcc5IgQTBujPlFjUZDVpNzi_bdExnyQOiepnas_5sj5ZsoFLgVuEEZb5itaOrcgGo5nooIr4DkTGCbRYl_5GmjLtFxq20s9s5KFMwWv8nOoYst0Eh4jP89l8sPu2oN-7-sOIjfURC-an0-5FQ4i2SfTTYQTpXrCSqiw1Ki7YS0n5aguPnPYRI0k4WNPZbcqdHVEvn9JLBHXoNstNFMwd-2lC9bggSrpzq_F-pmAkLjpHnvNzpj1MEgquMXEsgSm68s2xiDLhd_E7OO-7s4xxe1vyUTHmRsx1kwVW_cmFtZosu7PapzyyWfm2sxiZU92sueRUSEdczpWdElp0VE7xRWUzhaN5jmE2PBO6Lln2__sHfDnEC753DPvQ8af4anUpfIzS2DdjPd1JpGYFYwFU-5at7EKoGaMJ1hZPsaqwKWNFyh0dAIeE5GEEdSIOmBIO8fT15mOZ1pPvN3ceeTG-801f4oeO-w0MSZGW51PJc0pZ6f3dNgstLTf_0JTycnmfUzMazDzQID-LJTRuNyvMkewvSiAcEB0pWIc4bGbICkfQztKZNRkzL89bWfXoZvPLtMR6K7ut7qVQswLM6AVgnwwtbvQzMkhVkd5Y9IPmqKVt9DN_T87b1YHqKf483WggYi0z-lbOjQRBkQ2mwl_qFHJJCuB8xupSdVXf5yxwRlpflKz6wMQwIXtzuNCQ1r3yScqjMYjiz2eH_FuuvoxiD1t5cuxE3jigPVmaqd1wsBCt-l0Jog3Z0kLbAsCp24ZdHYMxGh9MoExLvrzP2oeZGMtysIB7HRTywz2CNaHfqXp165jpbI4jzBIz16KFOArAtxrRfOpE4JQ8whJB5wXtAxgqBydokW8aGFfAqdwVYtCvRHdXBpxq80wMDsQHPauEXnd0N87snYH96Y0DvjLOztqRT3wHrhGxEwgYar9MnCp5UAjxdV1k85evABQxjecaR1P-nBm1HNFK_aR>`_

Session Management
------------------

The Authorization Server MUST maintain a unified session across all authentication steps, ensuring:

	- **Session Continuity**: Single session identifier throughout the authentication flow.
	- **State Correlation**: Authentication results from each step are correlated.
	- **Security Binding**: Binding between authentication steps.

Since the PID Authorization Server and the MRTD PoP Service operate within the PID Provider boundary implementation, it is RECOMMENDED that the OAuth 2.0 session and the nonces used within the protocol flow are properly handled by both components seamlessly.

When both services operate within the same trust boundary, the following mechanisms are available for session correlation:

	- Direct memory access to shared session stores.
	- Internal service-to-service authentication using pre-shared keys.
	- Synchronized nonce validation without external communication overhead.
	- Unified audit logging and security event correlation.

When the PID Authorization Server or MRTD PoP Service is deployed outside the PID Provider boundary implementation, the :ref:`credential-issuance-l2plus:Security Considerations` MUST be taken into account to harden the User authentication sessions management. These measures include but are not limited to secure session token handling, distributed session validation, and enhanced audit trail mechanisms.

Low-Level Flow
--------------

This section provides technical details about the PID Issuance using Level of Assurance Substantial and remote identity proofing through verification of the electronic document using a MRTD Verification service.

.. _fig_eID_MRTD_Detailed_Flow:
.. plantuml:: plantuml/l2plus-detailed-flow.puml
    :width: 99%
    :alt: The figure illustrates the eID Substantial Authentication with MRTD Verification Detailed Flow.
    :caption: `eID Substantial Authentication with MRTD Verification Detailed Flow. <https://www.plantuml.com/plantuml/svg/nLPjRnf74Fw-lsBgAAbDV13R-L2X4EU2NqoLs2V0YTgwGilT0DiikzVTFMpwwxkpTnmlAL6aLgg44DmzC_FCCxCp-yuwRbmnb-p77zmCvmWfca8YLv4kd1GA6I-SLiLyZ8Rb7YjIaNFbuE3UeZa0Rk5--_bdBYKww2dlMgKO8F4sfDkx38-xRAoV00wItWKaHYz4HYwVVH3JcNil2zos8bHSk9asuY_kX5OmGBEeICI3RV37_j3xr4d0Y8h6HNAN31Yg37pShoZ1RV3A9VHnAgmpos3qiNUx3Lt17bGlG-M4MzRaWq7l8c6C-USI0Jtd3pe-2yG9d9RCNuB1kNO8OkKYDrfFX9g2KD0RHfMAb7FFseAKX2kf7ncxX-Wjn6tuJ6IS1fuwiU0EmGU0okn15PPyKVX1CQPAEC4bF0etWo3D9pHYKh5XhDFfG3BZ5k6a3NV4TKVfFlvPe7NGwR0un1z06vAuNxyu14YbGEL68Zi6Kpwz6_-1gJloTA0C7Ln7tG2COkSyflJFLRRtPKHb52haTuFSoqnmyjbe1Azya-eeGyU51BVC4Gw46ydJbvbEYpbn2o8VD1gC-GGYogDEm-PQMOJ3YlgeCE8Oy2aN1kr8gADLtcsgoHvrYDFrvH1QAqPuNelIQJQRBpQSqt_2tsZhsf2BBCgh9chY4v_d4flQJ3TBS-f36p7dPhdRJL4eD1t8tJUa3pNWLXTG4GUKZU_KDfbkMzNvCFyUtf1Cz-tIEz_jufH4Km5PohF7NwdkPZPdRQZFw2SkHHQWDJVgy9lXC6cTD4_WxDKfNEaY5Fs3BfssOUPSRjkjLXXXpSVG-PlQjT8PFLDJF6yqviPbPVaxRzQ_Hpz_7huDxK0XmtXe-wwgYLL2D1eFAhaR-C9YfjCecBQ44gwcw8bzkv0Fwhyy08pft34029n9BnfJRV24dH6uGA_jhzvaeiqyk20iGI1QvxaBGPKnLlcZ0cmhKPMGfAZhSkhh4gSfvWwpAi5IMvsFb5Of7aDTWsDVhuA-vY7NGvsNKrGkZm8JNt_E69SEUfEIcWMb7V055vAF9OBJGO6T_H8oYo4qwQfU11MUh77GZMy3OZKrU-l7A2s2g8FfiUD2OGRSmS1X3YSdjM-ol7noXgSk48M9qNCoB4MR6btarTxw1QKVqt1xrVMn7999VH29VZX7NdIug8OI9DHEu3-9jXQjzN1wvdIgPPZvn695vRTdKuEeVdyBNQWB5EUvNC-29EvUKfdwo3Euk3uvfY__FRYx614ykEf2LFiAO_2VaC3sXUt5WyseTRZRtk0OOZhvKYlQG4anzY3uWilIBHdk8V3zjjk4sbj6GNJ5vSuCUb0sN1RM3Rc7HNyGHwUlNly4LamLTuL1AertjRQaekyT6UjPzitfiQ3zk_pVvWS0svuSH6H5cDgJgX5rh-11fTeOb6MKT8RfbtBxBYXFkhXGaC9M8ddyQjdIAbteTCFmYB6T4RGnILx1tPVzusUjwdTF8eEPC9Y6PKkKoz7aQQ_7KoXY24N5_WOWbFYzqOyMJJJc5ZEu4jHaNQqcmiphG-2tVxsNzfMobOxFlmur8WgOlT2qOqVL72Wl2OTkPdGndS6uP72qkKTVxxkmbIfjBTH6W-ukUu11jE2fgxEWxh_Sl-SUdNfNPHBmWXgb_YEixGG7py_YvwTN_hF_2cIKTWYQJczy70_yeErTtmol-vUNjsmuGvZGZ4orSa8LQ86dgJOPpGAdjo_G0SWjP3W9axuw4-lhjiqnNL-BKMKXD7ldVnLp-JS0>`_

Phase 1: OAuth Authorization Request
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Wallet Instance initiates the eID Substantial Authentication with MRTD Verification flow by submitting a Pushed Authorization Request (PAR), using a JWT-secured Authorization Request (JAR) and Rich Authorization Requests (RAR) as specified below.

Authorization Details
"""""""""""""""""""""

The JWT Request Object MUST contain the same parameters as defined in :ref:`credential-issuance-endpoint:Pushed Authorization Request Endpoint`. When the User requests a PID using eID Substantial Authentication with MRTD Verification, the Wallet Instance MUST include an additional **Authorization Details Object** in the ``authorization_details`` parameter, with the structure and claims as defined in the Table of the JWT Request parameters of Section :ref:`credential-issuance-endpoint:Pushed Authorization Request Endpoint`

Below a non-normative example of PAR:

.. code-block:: http

    POST /as/par HTTP/1.1
    Host: pid-provider.example.org
    Content-Type: application/x-www-form-urlencoded
    OAuth-Client-Attestation: eyJhbGciOiJFUzI1NiIsImtp…
    OAuth-Client-Attestation-PoP: eyJhbGciOiJFUz…

    request=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL3dhbGxldC5leGFtcGxlLm9yZy9pbnN0YW5jZS8xMjM0NSIsImF1ZCI6Imh0dHBzOi8vcGlkLXByb3ZpZGVyLmV4YW1wbGUub3JnIiwibmJmIjoxNzUzNTU1NDAwLCJleHAiOjE3NTM1NTU3MDAsImlhdCI6MTc1MzU1NTQwMCwianRpIjoiYWFjNDVkZGMtY2ZiOC00OTNlLWI2NmItZTQ5ZDY4ZDVhNzVhIiwiY2xpZW50X2lkIjoiaHR0cHM6Ly93YWxsZXQuZXhhbXBsZS5vcmcvaW5zdGFuY2UvMTIzNDUiLCJyZXNwb25zZV90eXBlIjoiY29kZSIsInJlc3BvbnNlX21vZGUiOiJxdWVyeSIsInJlZGlyZWN0X3VyaSI6Imh0dHBzOi8vd2FsbGV0LmV4YW1wbGUub3JnL2NhbGxiYWNrIiwic3RhdGUiOiJhMWIyYzNkNGU1ZjY3ODkwIiwiY29kZV9jaGFsbGVuZ2UiOiJxampqUDdmaC1FdEFWcjJMWGU2ZzZwZi1LYVRGeDl6WmhIVGFHN3VIYnBvIiwiY29kZV9jaGFsbGVuZ2VfbWV0aG9kIjoiUzI1NiIsImF1dGhvcml6YXRpb25fZGV0YWlscyI6W3sidHlwZSI6Im9wZW5pZF9jcmVkZW50aWFsIiwiY3JlZGVudGlhbF9jb25maWd1cmF0aW9uX2lkIjoiZGNfc2Rfand0X1BJRF9hbHQyIiwiY3JlZGVudGlhbF9kZWZpbml0aW9uIjp7InR5cGUiOlsiVmVyaWZpYWJsZUNyZWRlbnRpYWwiLCJQZXJzb25JZGVudGlmaWNhdGlvbkRhdGEiXSwiY3JlZGVudGlhbFN1YmplY3QiOnt9fX0seyJ0eXBlIjoiaXRfbDIrZG9jdW1lbnRfcHJvb2YiLCJpZHBoaW50aW5nIjoiaHR0cHM6Ly9pZHAuZXhhbXBsZS5vcmciLCJjaGFsbGVuZ2VfbWV0aG9kIjoibXJ0ZCtpYXMiLCJjaGFsbGVuZ2VfcmVkaXJlY3RfdXJpIjoiaHR0cHM6Ly93YWxsZXQuZXhhbXBsZS5vcmcvbDJwbHVzLWNhbGxiYWNrIn1dfQ.signature

Phase 2: Primary Authentication
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Upon successful processing of the PAR, the Authorization Server redirects the User Agent to the configured LoA3 Identity Provider for primary authentication. The User completes the LoA3 authentication flow (SPID or CIEid Substantial) and the Authorization Server correlates the authenticated identity with the active OAuth session.

The PID Authorization Server MUST ensure that the ``mrtd_auth_session`` parameter is maintained throughout this phase for proper session correlation with subsequent authentication steps.

Phase 3: MRTD PoP Validation Flow
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Following successful primary authentication, the Authorization Server initiates the electronic document proof of possession flow by providing the Wallet Instance with the necessary parameters for MRTD validation.

MRTD Proof JWT
""""""""""""""

The Authorization Server MUST provide a signed JWT containing the challenge requirements for document validation. The JWT structure is defined as follows:

.. _table_eID_MRTD_Proof_JWT_Header:
.. list-table:: MRTD Proof JWT Header
   :widths: 20 15 65
   :header-rows: 1

   * - **Parameter**
     - **Type**
     - **Description**
   * - **alg**
     - string
     - REQUIRED. Signature algorithm.
   * - **typ**
     - string
     - REQUIRED. It MUST be ``mrtd+ias+jwt``.
   * - **kid**
     - string
     - REQUIRED. Identifier of the PID Provider's key that MUST be used to verify the signature of this JWT.

.. _table_eID_MRTD_Proof_JWT_Payload:
.. list-table:: MRTD Proof JWT Payload
   :widths: 20 15 65
   :header-rows: 1

   * - **Parameter**
     - **Type**
     - **Description**
   * - **iss**
     - string
     - REQUIRED. PID Provider identifier.
   * - **aud**
     - string
     - REQUIRED. Wallet Instance identifier.
   * - **iat**
     - integer
     - REQUIRED. Issuance time (Unix timestamp).
   * - **exp**
     - integer
     - REQUIRED. Expiration time (Unix timestamp).
   * - **status**
     - string
     - REQUIRED. Challenge status. MUST be ``require_interaction``.
   * - **type**
     - string
     - REQUIRED. Type of the required interaction. It MUST be set to ``mrtd+ias``.
   * - **mrtd_auth_session**
     - string
     - REQUIRED. Session identifier.
   * - **state**
     - string
     - REQUIRED. MUST be the same value as in the initial Request Object.
   * - **mrtd_pop_jwt_nonce**
     - string
     - REQUIRED. Nonce value for replay protection. It MUST be obtained by the MRTD PoP Service that MUST have direct control over this value.
   * - **htu**
     - string
     - REQUIRED. HTTP URI of the MRTD PoP initialization endpoint.
   * - **htm**
     - string
     - REQUIRED. HTTP method for the MRTD PoP initialization request. MUST be ``POST``.

The Wallet Instance MUST:

	- Validate the JWT signature using the PID Provider's public key obtained through trust evaluation.
	- Verify that the ``status`` field is set to "require_interaction".
	- Verify the authentication type matches the expected value ``mrtd+ias``.
	- Extract HTTP target URI (``htu``) and method (``htm``) for the next step.
	- Handle JWT validation and network errors, and provide user feedback with appropriate retry mechanisms.

MRTD PoP Request
""""""""""""""""

The Wallet Instance MUST send an HTTP POST Request to the MRTD PoP Service initialization endpoint with ``application/json`` as content type, including Wallet Attestation and Wallet Attestation JWT PoP in the header according to `OAUTH-ATTESTATION-CLIENT-AUTH`_. The payload of the Request contains the following parameters:

.. _table_eID_MRTD_PoP_Request:
.. list-table:: MRTD PoP Request Parameters
   :widths: 20 15 65
   :header-rows: 1

   * - **Parameter**
     - **Type**
     - **Description**
   * - **mrtd_auth_session**
     - string
     - REQUIRED. Session identifier for session binding.
   * - **mrtd_pop_jwt_nonce**
     - string
     - REQUIRED. Nonce value obtained from the MRTD Proof JWT.

Below a non-normative example of an MRTD PoP Request:

.. code-block:: http

    POST /edoc-proof/init HTTP/1.1
    Host: pid-provider.example.org
    Content-Type: application/json
    OAuth-Client-Attestation: eyJhbGciOiJFUzI1NiIsImtp…
    OAuth-Client-Attestation-PoP: eyJhbGciOiJFUz…

    {
      "mrtd_auth_session": "wxroVrBY2MCq4dDNGXACS",
      "mrtd_pop_jwt_nonce": "f42cccb7f1c8269f9d4aeefe339c6b13"
    }

**The Wallet Instance MUST:**

	- Validate the MRTD Proof JWT signature using the PID Provider's public key.
	- Verify the JWT ``aud`` claim matches its ``client_id``.
	- Ensure the JWT ``exp`` claim indicates the token has not expired.
	- Extract the ``mrtd_auth_session`` and ``mrtd_pop_jwt_nonce`` values for correlation.
	- Include valid Wallet Attestation according to `OAUTH-ATTESTATION-CLIENT-AUTH`_.
	- Handle network errors and implement appropriate retry mechanisms.

**The MRTD PoP Service MUST:**

	- Validate the Wallet Attestation according to `OAUTH-ATTESTATION-CLIENT-AUTH`_.
	- Verify the ``mrtd_auth_session`` parameter matches an active session.
	- Validate the ``mrtd_pop_jwt_nonce`` parameter corresponds to the one issued at the previous step.

The MRTD PoP Service MAY request the MRZ information (document number, date of birth, expiry date, citizenship and gender) directly to the CIE National Registry using the Tax payer's identification number of the authenticated User. In this case, the MRTD PoP Service is able to check if the authenticated User owns a valid CIE and If this is not the case, it MUST send an HTTP Error Response with HTTP Error code ``access_denied``.

MRTD PoP Response
"""""""""""""""""

If the HTTP Request is successfully processed, the MRTD PoP Service MUST send a HTTP Response with code *202 Accepted* and ``application/jwt`` as content type. The JWT structure is defined as follows:

.. _table_eID_MRTD_PoP_Response_Header:
.. list-table:: MRTD PoP Response Parameters
   :widths: 20 15 65
   :header-rows: 1

   * - **Parameter**
     - **Type**
     - **Description**
   * - **alg**
     - string
     - REQUIRED. Signature algorithm.
   * - **typ**
     - string
     - REQUIRED. It MUST be ``mrtd-ias-pop+jwt``.
   * - **kid**
     - string
     - REQUIRED. Identifier of the PID Provider's key that MUST be used to verify the signature of this JWT.

.. _table_eID_MRTD_PoP_Response_Payload:
.. list-table:: MRTD PoP Response Parameters
   :widths: 20 15 65
   :header-rows: 1

   * - **Parameter**
     - **Type**
     - **Description**
   * - **iss**
     - string
     - REQUIRED. PID Provider identifier.
   * - **aud**
     - string
     - REQUIRED. Wallet Instance identifier.
   * - **iat**
     - integer
     - REQUIRED. Issuance time (Unix timestamp).
   * - **exp**
     - integer
     - REQUIRED. Expiration time (Unix timestamp).
   * - **challenge**
     - string
     - REQUIRED. Challenge data for cryptographic document validation. It SHOULD be the SHA-256 hash value of a random value with the ``mrtd_auth_session`` and timestamp for cryptographic binding.
   * - **mrtd_pop_nonce**
     - string
     - REQUIRED. Unique nonce value for the next step, preventing replay attacks.
   * - **mrz**
     - string
     - OPTIONAL. Machine Readable Zone information including document number, date of birth, expiry date, citizenship and gender.
   * - **htu**
     - string
     - REQUIRED. HTTP URI of the MRTD PoP validation endpoint.
   * - **htm**
     - string
     - REQUIRED. HTTP method for the MRTD PoP validation request. MUST be ``POST``.

Below a non-normative example of an MRTD PoP Response:

.. code-block:: http

    HTTP/1.1 202 Accepted
    Content-Type: application/jwt; charset=utf-8
    {
      "alg":"ES256",
      "typ":"mrtd-ias-pop+jwt",
      "kid":"b3f1a6c2e9d54a8f9c3e7d1a2f4b6c78"
    }
    .
    {
      "iss":"https://pid-provider.example.org",
      "aud":"https://wallet.example.org/instance/12345",
      "iat": 1753555800,
      "exp": 1753556000,
      "mrtd_pop_nonce":"9f2c4a7e3b1d8c9a6e5f4b2a1c3d7e8f",
      "mrz":"...",
      "challenge":"...",
      "htu":"...",
      "htm":"..."
    }

**The MRTD PoP Service MUST:**

	- Generate cryptographically secure challenge data for ``MRTD+IAS`` validation with sufficient entropy (to be used in Anti-Cloning Internal Authentication protocol by the Wallet Instance), storing it with an appropriate expiration time. Moreover, the MRTD PoP Service MUST ensure challenge uniqueness to prevent reuse attacks.
	- Create a new unique ``mrtd_pop_nonce`` for the next step to prevent replay attacks.
	- Validate session continuity by ensuring the ``mrtd_auth_session`` parameter corresponds to an active session.
	- Return HTTP *202 Accepted* status to indicate asynchronous processing initiation.
	- Include proper Content-Type header (``application/json; charset=utf-8``).
	- Handle service errors and return appropriate error responses.
	- Extract and validate MRZ information if provided from external registry services.

**The Wallet Instance MUST:**

	- Validate HTTP response status (*202 Accepted*) and content type.
	- Parse JSON response and validate required parameters (``challenge``, ``mrtd_pop_nonce``).
	- Extract challenge data for cryptographic document validation.
	- Store new ``mrtd_pop_nonce`` value securely for subsequent validation requests.
	- Validate optional MRZ information if present in the response.
	- Handle errors, providing relative user feedback.
	- Store challenge data temporarily.
	- Prepare NFC reading session.

The Wallet Instance performs NFC-based electronic document reading and validation, then submits the evidence to the PID Provider for final verification and identity correlation with the LoA3 authentication result.

MRTD PoP Validation Request
"""""""""""""""""""""""""""

Upon all the evidence has been collected through NFC interaction with the Electronic Document, the Wallet Instance MUST send all data to the PID Provider Authorization Server for the final validation and identity cross checks. The Wallet Instance MUST send a HTTP POST Request with ``application/json`` as content type, including Wallet Attestation and Wallet Attestation JWT PoP in the header according to `OAUTH-ATTESTATION-CLIENT-AUTH`_. The payload of the Request contains the following parameters.

.. _table_eID_MRTD_PoP_Validation_Request:
.. list-table:: MRTD PoP Validation Request Parameters
   :widths: 20 15 65
   :header-rows: 1

   * - **Parameter**
     - **Type**
     - **Description**
   * - **mrtd_validation_jwt**
     - string
     - REQUIRED. JWT containing document evidence, cryptographic proofs, Data Groups (DGs), and validation results.
   * - **mrtd_auth_session**
     - string
     - REQUIRED. Session identifier for session binding.
   * - **mrtd_pop_nonce**
     - string
     - REQUIRED. MUST match the value obtained from the MRTD PoP Response.

Validation JWT Structure
""""""""""""""""""""""""

The Validation JWT (``mrtd_validation_jwt``) structure is given in the following table.

.. _table_eID_MRTD_Validation_JWT_Header:
.. list-table:: Validation JWT Header Parameters
   :widths: 20 15 65
   :header-rows: 1

   * - **Header Parameter**
     - **Type**
     - **Description**
   * - **alg**
     - string
     - REQUIRED. Signature algorithm.
   * - **typ**
     - string
     - REQUIRED. It MUST be ``mrtd+ias+jwt``.
   * - **kid**
     - string
     - REQUIRED. Identifier of the Wallet Instance's key that MUST be used to verify the signature of this JWT.

.. _table_eID_MRTD_Validation_JWT_Payload:
.. list-table:: Validation JWT Payload Parameters
   :widths: 20 15 65
   :header-rows: 1

   * - **Payload Parameter**
     - **Type**
     - **Description**
   * - **iss**
     - string
     - REQUIRED. Wallet Instance identifier.
   * - **aud**
     - string
     - REQUIRED. PID Provider identifier.
   * - **iat**
     - integer
     - REQUIRED. Issuance time (Unix timestamp).
   * - **exp**
     - integer
     - REQUIRED. Expiration time (Unix timestamp).
   * - **document_type**
     - string
     - REQUIRED. Type of document validated. MUST be set to ``cie``.
   * - **mrtd**
     - JSON Object
     - REQUIRED. MRTD validation data containing Data Groups and SOD.
   * - **ias**
     - JSON Object
     - REQUIRED. IAS validation data containing NIS, Anti-Cloning Public Key, and SOD.

MRTD Object Structure
"""""""""""""""""""""

The ``mrtd`` object contains the following fields:

.. _table_eID_MRTD_Object:
.. list-table:: MRTD Object Structure
   :widths: 20 15 65
   :header-rows: 1

   * - **Field**
     - **Type**
     - **Description**
   * - **dg1**
     - string
     - REQUIRED. Base64-encoded Data Group 1 (MRZ information:document number, date of birth, expiry date, citizenship and gender).
   * - **dg11**
     - string
     - REQUIRED. Base64-encoded Data Group 11 (additional personal data).
   * - **sod_mrtd**
     - string
     - REQUIRED. Base64-encoded Security Object of Document for MRTD.

IAS Object Structure
""""""""""""""""""""

The ``ias`` object contains the following fields:

.. _table_eID_MRTD_IAS_Object:
.. list-table:: IAS Object Structure
   :widths: 20 15 65
   :header-rows: 1

   * - **Field**
     - **Type**
     - **Description**
   * - **nis**
     - string
     - REQUIRED. NIS (Service Identification Number) value.
   * - **ias_pk**
     - string
     - REQUIRED. Base64-encoded IAS public key in DER format.
   * - **sod_ias**
     - string
     - REQUIRED. Base64-encoded Security Object of Document for IAS.
   * - **challenge_signed**
     - string
     - REQUIRED. Base64-encoded signed challenge response.

Below a non-normative example of an MRTD PoP Validation Request:

.. code-block:: http

    POST /edoc-proof/verify HTTP/1.1
    Host: pid-provider.example.org
    Content-Type: application/json
    OAuth-Client-Attestation: eyJhbGciOiJFUzI1NiIsImtp…
    OAuth-Client-Attestation-PoP: eyJhbGciOiJFUz…

    {
      "mrtd_validation_jwt":"eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL3dhbGxldC5leGFtcGxlLm9yZy9pbnN0YW5jZS8xMjM0NSIsImF1ZCI6Imh0dHBzOi8vcGlkLXByb3ZpZGVyLmV4YW1wbGUub3JnIiwiaWF0IjoxNzUzNTU1NDAwLCJleHAiOjE3NTM1NTU3MDAsImRvY3VtZW50X3R5cGUiOiJjaWUiLCJtcnRkIjp7ImRnMSI6IlVEeEpWRUU4VTAxSlZFZzhQRXBQU0U0OFBFcFBTRTRnVTAxSlZFZzhQREU1T0RBME1UVThUVDxQTnpjM056SXpNUT09IiwiZGcxMSI6Ik1USXpORFUyTnpnNVFVSkRSRVZHUjBoSlNrdE1UVTVQVUVGT1IxSlRWRlZXV0ZsYVUwRkVSVVU9Iiwic29kX21ydGQiOiJNSUlGempDQ0JMYWdBd0lCQWdJSVFPWTJLSkdGVFVJd0RRWUpLb1pJaHZjTkFRRUxCUUF3WHpFTE1Baz0ifSwiaWFzIjp7Im5pcyI6IklUMTIzNDU2Nzg5MDEyMzQiLCJpYXNfcGsiOiJNSUlCSWpBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE4QU1JSUJDZ0tDQVFFQXoxMjM0NTY3ODkwPSIsInNvZF9pYXMiOiJNSUlGYURDQ0JGQ2dBd0lCQWdJSkFMMktKR0ZUVUl3RFFZSktvWklodmNOQVFFTEJRQXdYekVMTUE9PSIsImNoYWxsZW5nZV9zaWduZWQiOiJhMWIyYzNkNGU1ZjY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTBhYmNkZWYxMjM0NTY3ODkwYWJjZGVmPT0ifX0.xyz456abc789def012ghi345jkl678mno901pqr234stu567vwx890yz123",
      "mrtd_auth_session":"wxroVrBY2MCq4dDNGXACS",
      "mrtd_pop_nonce":"9f2c4a7e3b1d8c9a6e5f4b2a1c3d7e8f"
    }

**The Wallet Instance MUST:**

	- Perform `ICAO 9303`_ compliant NFC document reading (PACE,etc.).
	- Validate document cryptographic signatures and certificate chains.
	- Extract identity attributes (DG1 and DG11), NIS, Anti-Cloning Public Key from document data groups, and SODs (form MRTD and IAS Applications).
	- Perform the Anti-Cloning Internal Authentication.
	- Generate validation evidence in the JWT.
	- Authenticate using a valid Wallet Instance Attestation.
	- Include the exact ``mrtd_auth_session`` and ``mrtd_pop_nonce`` from the init response.
	- Sign the ``mrtd_validation_jwt`` with its private key.
	- Handle document reading errors and provide appropriate feedback.

**The MRTD PoP Service MUST:**

	- Validate Wallet Instance Attestation according to IT-Wallet specifications.
	- Verify OAuth-Client-Attestation-PoP signature.
	- Validate the ``mrtd_auth_session`` parameter matches an active session.
	- Verify the ``mrtd_pop_nonce`` matches the value sent in the previous response.
	- Parse and validate the ``mrtd_validation_jwt`` signature and structure.
	- Validate document authenticity using `ICAO 9303`_ standards.
	- Verify Anti-Cloning challenge response.
	- Check document validity (non revocation status).
	- Check the binding between NIS obtained from IAS Application and Tax payer's identification number of the User read from the MRTD Application in order to ensure that both values are coming from the same chip.

MRTD PoP Validation Response
""""""""""""""""""""""""""""

Upon successful completion of all checks by the MRTD PoP Service, it MUST send to the Wallet Instance an HTTP Response with code *202 Accepted* including the following parameters:

.. _table_eID_MRTD_PoP_Validation_Response:
.. list-table:: MRTD PoP Validation Response Parameters
   :widths: 20 15 65
   :header-rows: 1

   * - **Parameter**
     - **Type**
     - **Description**
   * - **status**
     - string
     - REQUIRED. It MUST be `require_interaction`.
   * - **type**
     - string
     - REQUIRED. It MUST be `redirect_to_web`.
   * - **mrtd_val_pop_nonce**
     - string
     - REQUIRED. New nonce for final confirmation.
   * - **redirect_uri**
     - string
     - REQUIRED. Browser redirect URI for completion of the Authorization Flow.

Below a non-normative example of an MRTD PoP Validation Response:

.. code-block:: http

    HTTP/1.1 202 Accepted
    Content-Type: application/json; charset=utf-8

    {
      "status": "require_interaction",
 	    "type": "redirect_to_web",
      "mrtd_val_pop_nonce": "0f2bff024317345b6927ce17e776361d",
      "redirect_uri":"https://pid-provider.example.org/cb"
    }

Browser-based Final Confirmation
"""""""""""""""""""""""""""""""""

Upon successful MRTD PoP validation, the Wallet Instance MUST redirect the User Agent to the ``challenge_redirect_uri`` specified in the initial Authorization Details Object, including the ``mrtd_val_pop_nonce`` as a query parameter:

.. code-block:: text

    https://pid-provider.example.org/l2plus-callback?mrtd_val_pop_nonce=0f2bff024317345b6927ce17e776361d_signed&mrtd_auth_session=wxroVrBY2MCq4dDNGXACS

The Wallet Instance MUST validate that the ``mrtd_val_pop_nonce`` matches the value received from the MRTD PoP Validation Response.

Phase 4: OAuth Authorization Response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Upon successful completion of all authentication steps and identity matching, the Authorization Server MUST issue the final OAuth Authorization Response. If all validation checks have been passed, the Authorization Server MUST redirect the User Agent to the Wallet Instance with an OAuth Authorization Response including the authorization code as defined in steps 6-7 of :ref:`credential-issuance-low-level:Low-Level Issuance Flow`, and in Section :ref:`credential-issuance-endpoint:Authorization Response`. The Authorization Server MUST use the ``redirect_uri`` included in the initial Request Object by the Wallet Instance.

Error Management
----------------

The error management MUST follow the same rules as defined in the Section :ref:`credential-issuer-endpoint:Credential Issuance Endpoints`, regarding the formats and the related standard references.

During the MRTD PoP Validation flow, when recoverable errors occur, the MRTD PoP Service MAY generate and return a fresh nonce to enable the User to retry attempts while maintaining session security and preventing replay attacks.

In addition to the error codes already defined in the Section :ref:`credential-issuer-endpoint:Credential Issuance Endpoints`, at least the following error codes MUST be supported.

MRTD PoP Response Errors
^^^^^^^^^^^^^^^^^^^^^^^^

.. _table_eID_MRTD_PoP_Response_Errors:
.. list-table:: MRTD PoP Response Error Codes
   :widths: 30 70
   :header-rows: 1

   * - **Error Code**
     - **Description**
   * - **temporarily_unavailable**
     - Document validation service or CIE Registry service is temporarily unavailable.

MRTD PoP Validation Response Errors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _table_eID_MRTD_PoP_Validation_Response_Errors:
.. list-table:: MRTD PoP Validation Response Error Codes
   :widths: 30 70
   :header-rows: 1

   * - **Error Code**
     - **Description**
   * - **invalid_client**
     - Wallet Instance authentication failed.
   * - **invalid_request**
     - HTTP Validation Request or Validation JWT is invalid or malformed (due to a malformed structure, missing data, signature failure, request timeout, etc.).
   * - **access_denied**
     - User authentication or document validation failed.

HTTP Status Code Mapping
^^^^^^^^^^^^^^^^^^^^^^^^^

Error responses MUST use appropriate HTTP status codes:

	- **400 Bad Request**: For ``invalid_request`` errors.
	- **401 Unauthorized**: For ``invalid_client`` errors.
	- **403 Forbidden**: For ``access_denied`` errors.
	- **503 Service Unavailable**: For ``temporarily_unavailable`` errors.

Security Considerations
-----------------------

Secure Session Management
^^^^^^^^^^^^^^^^^^^^^^^^^

The ``mrtd_auth_session`` parameter serves as the primary correlation mechanism between authentication steps. Implementations MUST ensure this identifier has sufficient entropy (minimum 128 bits) and is cryptographically secure. The session identifier MUST be validated at each step to prevent session fixation attacks.


.. _fig_eID_MRTD_Security_Controls:
.. plantuml:: plantuml/l2plus-security-controls.puml
    :width: 99%
    :alt: The figure illustrates the eID Substantial Authentication with MRTD Verification Security Controls.
    :caption: `eID Substantial Authentication with MRTD Verification Security Controls. <https://www.plantuml.com/plantuml/svg/nLT_Rzis4FsVd-AMebtYHacJT6rdr4bLvqSyj8aHEoksPJ1ewMnpfKcDf9nadtuyIfPbfmuoRC00Wx2b-_7ktV6H_c0TDowVIlRzTsw2KuG4JIwHgqZdJWg5ZETEgtmwHCCoRoiIaN7bOEFQeja0Rk5w-VaNBYKww2WVMYKOJE9batRd93nkiw6-0zZeTewXQ_HCf1JosISndhYFCiTbBxAASpVHHlp5dT0AUcXc9OYujspy-QhlO-fki14bZEFkPRV7KANWypw011SXAfTmXMDXdRaFJfyx5ykcSxCRrKbHEU7k5-39eNFSPOpvvn81FUPFEZu8mCauAP2_18DJxH34F4Hcj1u9DGQXeDEFIXQfvewrEJ49frBVCdODqI74JVX2O9m6dZWnumx19u3IxKRbbc9DS-b4P1rcm9S1JD4JcJBMQhMWE-4MOQy9buHoXUCh_3D7ww3LOd78t8CcTEEhwiKcG2A53pqGwJQOukdby0zCt9O70d0htAG87RM3OHGxvssA-5obQrz6r42XGcNdo3t1P4un6uqGbTUX3b9qN4Xmznd2Xd03kVyorKa-9Mo1ter6Wp5VG4HrL6NOJ2kBi5b27-H6R0FUPSAW7GYrDQ-xITrOmmvXEZlfm-uS4HvLfBHsTdPUr8BJRx8_rzOr8HDfb9NZiuDtV9f9tD5cN6_Dlazjn9IR-zKvYiA4qLPSVKFyqEX1Bn_IJdI2IsgYKJHsUaOUFR_N-0oLJ-stcvsmNlk0jaUm2KGTqZGtASbo_Afovj_3UoBqkbdWuAkJdX2zgh0CHAw9L_JXwG3h31qqeThnFtCfqY8e3Mslt2_d_NvtTszd3mvUxSEfpccGF455-YPCdCjiStSt2EBERTX7zNxi9XDwfiPur6XCZKkBaMgzNtmV_FIbVqWZLY_XOGLlQnNGQ1MorFGpNPLGajjetAZkPS-F5Vf1ZaAINQ64guhn9Jm-HZVglzn-zT8As0_BUxCDlVOxMdwi5Qepnm2WSF95awmsmHVgZC0P-kxzwbEDj9c6r6HB9X1L_AoQK736odZKuZg3rJWHXLNdzttduoJ1p65Q4bDqJsS3fLM2sr1rEJ2pgRD2w-NzLiYVSiSPuz91PrG0ik0B13xZGlAXH70wyBLo2ePwOYYsITbTCXKUed7GZY-2nLpREul7A2s2g9BfeUD2OGhSGOzqVM-lYasU9tVEyCG5e30oUagE1LLZe_EiF5r_GIdrBLoSjdqkX-HIYGR13plPKmt7fO12buOF_AUhhKLhlJazSphHCfnCX68EvRTdOuEeVZ-4DbHjYRDCBdIh6xTFg3bNo5CuFjlRfiMllSlZ0PbJAEyTBMAHP7_B4jYwj9suLyzQfRlezBOX9ksHMj4vsSs7tWY-udqHbXpN07YwxpAWPjsf85rnkQA2DzHtsblL6Av1STMBe_rNhz-15MF5NMwGMkD3BJofwMi5Pg6HZsgDXo96z_-RsW3yCxsXnKy6y-j--7uGrjSr7LhM7ofiJW2DEtKtQf_2ZKgqCIWBrCa4aw_5pMD6lD5rZK3djYJTsyyl6dIDcEcavhZ5s8gGrVJe5Ln-VOgexlqGAdaJrhTXVVUmAfA0DMr-iY0QJ8N19DnKgEP28NtT2vLaRAusD7sF68IP-sZqhKKJ3Rd554u5JNrRgv4mqsfN-gjJTG2lcwtTP7WKehSU9XmG44nVQBfy34fv2lSkwXCMDwvDDp4w7qzWM23QMZwe7n-jRzuwNg-xCXTKrwuVH0JT7jSOteeoY6ScBLhqxsuhHzuwqMbPEInee1_2sbO8yFmWVhv_wZ_hE5zcQ3jmr3axxvzTdPnSiFu4OKJAdsZbXChH0ayIRL9IEAVhVrvAGsuXnH6TN-LEh_tLiHacObGAuOBk3_vRFfL_0m00>`_

Cryptographic Challenge Generation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The MRTD PoP Service MUST generate cryptographically secure challenges with sufficient entropy for document validation. Challenge values MUST be unique and MUST NOT be reused across different sessions or authentication attempts. The challenge generation algorithm SHOULD incorporate the ``mrtd_auth_session`` identifier and timestamp to ensure proper cryptographic binding.

Nonce Lifecycle Management
^^^^^^^^^^^^^^^^^^^^^^^^^^

Each step in the eID Substantial Authentication with MRTD Verification flow MUST use unique nonce values to prevent replay attacks. Nonce values MUST have appropriate expiration times and MUST be invalidated after successful use. The PID Authorization Server and MRTD PoP Service MUST maintain synchronized nonce validation to ensure session integrity.

Security Controls
^^^^^^^^^^^^^^^^^

The following security controls MUST be implemented in the protocol:

.. _table_eID_MRTD_Security_Controls:
.. list-table:: eID Substantial Authentication with MRTD Verification Security Controls
   :widths: 10 60 30
   :header-rows: 1

   * - **#**
     - **Description**
     - **Phase**
   * - **SC1**
     - The network communication channels are protected by using TLS with secure ciphers (at the time of this release, it is at least TLS v1.2).
     - All
   * - **SC2**
     - The Wallet Instance ensures the authenticity of the PID Provider and the eID Identity Provider by pinning the leaf certificate of each server.
     - All
   * - **SC3**
     - The PID Authorization Server verifies that the eID Identity Provider used within the *eID LoA3* phase is trustworthy.
     - Phase 2
   * - **SC4**
     - The PID Authorization Server verifies the authenticity and integrity of the data extracted from the *eID LoA3* assertion, by checking the digital signature.
     - Phase 2
   * - **SC5**
     - The challenge value and all nonce values are generated with safeguards to prevent bruteforce or guessing attacks.
     - Phase 3
   * - **SC6**
     - The PID Provider verifies all the nonce values to detect replay attacks.
     - Phase 3
   * - **SC7**
     - The Wallet Instance verifies that ``challenge_info`` is properly signed by the PID Authorization Server. Moreover, it checks that ``challenge_info`` contains: an ``iss`` value corresponding to the value of the PID Authorization Server; an ``aud`` value equal to the ``client_id`` of the Wallet Instance; and a ``state`` value equal to the one in the PAR request, to be sure that the response is bound to the initial request that is made by the Wallet Instance in Step 2. Therefore the information provided as part of ``challenge_info``, in particular the ``htu`` that corresponds to the redirect url to follow for the *MRTD PoP*, is not tampered with.
     - Phase 3
   * - **SC8**
     - The PID Provider checks that the ``mrtd_auth_session`` is associated with the same Wallet Instance in all the requests within the *MRTD PoP* phase. Therefore the PID Provider can be sure that the Wallet Instance performing the *MRTD PoP* phase: is trusted; is always the same across the protocol; and has previously started the PID issuance (PAR request). This can be implemented by requesting the Wallet Instance to perform a proof of possession of its private key (e.g., within OAuth-Client-Attestation or by signing a nonce value).
     - Phase 3
   * - **SC9**
     - The PID Provider checks that the ``mrtd_auth_session`` is not expired (validity timeout typically of 5 minutes), i.e., that the operation has been concluded within a certain amount of time.
     - Phase 3
   * - **SC10**
     - The integrity and confidentiality of the channel between the *physical CIE* and the *physical device_wallet* is secured with the PACE protocol (via the algorithm and key derivation functions supported by the card).
     - Phase 3
   * - **SC11**
     - The MRTD PoP Service verifies the authenticity and integrity of the ``mrtd_validation_jwt`` by checking that it is signed with the Wallet Instance private key associated with the ``mrtd_auth_session``.
     - Phase 3
   * - **SC12**
     - The MRTD PoP Service verifies that challenge_signed contained in ``mrtd_validation_jwt`` corresponds to the original challenge signed with the CIE AntiClone private key (``SDO.Servizi_Int_Kpriv``). This demonstrates the Wallet Instance and the CIE performed the Internal Authentication (in line with Sec. 5.2.3.5.1 in IAS ECC, but with randomness value ``RND.IFD`` provided by the MRTD PoP Service instead of generating it in the Wallet Instance).
     - Phase 3
   * - **SC13**
     - The MRTD PoP Service verifies the authenticity of the data extracted from the CIE by checking the SOD elements (both IAS and MRTD) and the related signature certificate chains.
     - Phase 3
   * - **SC14**
     - The MRTD PoP Service verifies the integrity of the data extracted from the CIE by checking the SOD elements (both IAS and MRTD) and the related hashes.
     - Phase 3

Additional implementation requirements:

	- **Rate limiting**: Protection against automated attacks and brute force attempts.
	- **Session timeout**: Automatic cleanup of incomplete authentication sessions.
	- **Audit logging**: Comprehensive logging of all authentication events with correlation identifiers.
	- **Error handling**: Secure error responses that do not leak sensitive information.
	- **Cryptographic material cleanup**: Secure deletion of temporary keys and challenges.

Implementation Considerations
-----------------------------

Implementations SHOULD incorporate rate-limiting mechanisms to protect against automated attacks and resource exhaustion, and a timeout configuration balancing user experience and security posture, accommodating the variability inherent in NFC-based document reading.

PID Provider SHOULD implement session timeouts approach with proper cleanup mechanisms, ensuring session resources are released and temporary cryptographic material is securely deleted when sessions expire.

All security-relevant events throughout the eID Substantial Authentication with MRTD Verification flow MUST be logged with sufficient detail for auditing purposes while preserving the privacy of the User, ensuring that personally identifiable information, when stored, is appropriately hashed. The audit logs SHOULD have consistent correlation identifiers, enabling end-to-end tracing across all protocol phases, with cryptographic integrity protection to prevent tampering.




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
	- **CIE National Registry:** Acts as the authoritative source for the CIE. Provides information related to the validity status of the document. It also optionally provides the MRZ data (document number, date of birth, expiry date, citizenship and gender) to improve the User experience.

.. _fig_eID_MRTD_System_Architecture:
.. plantuml:: plantuml/l2plus-system-architecture.puml
    :width: 99%
    :alt: The figure illustrates the eID Substantial Authentication with MRTD Verification System Architecture.
    :caption: `eID Substantial Authentication with MRTD Verification System Architecture. <https://www.plantuml.com/plantuml/png/dLJlRzis4Ftkl-9g38ZZnN5QPnysT44Tsri4n8rXUIaw311eyXmJfKIDF-8wG__t7Ib5TTGC2shaWt8yFhwxz-xUMSUCyxc2wpS_mjmh9mUfmnB6tcsraG_CILt0sF2jTCYTDzWvUkMsc2DmD5uXAmRQEoKBxBoI1LTU8BoTd0ydvzb4vwKki70NdQjaEilIrMmvkrbzNCnwnvsZw_77cpzMsOTaTPLTptwVlPzIj7C4KzmG6AIBPRAQfGUWpfTCcD6GwppNnSKp9njTk07ReTKv3duQ2kROcbbyGQf5Su_c1ObIP9mPyOBC7LCAtVyb3cLXdNJUoL1IXpuLHYqmcKBgrwHFuIHJKH2aJrufifDk2_FbQWgtQEGcXjj2THe1ijbdrwi8dK3tG_o0f0ZW7BiKckkrf8V7PHd-ksA5K6XXGHmC_ktHEWYD541F40r8LeCQXDxQ5bhfkpq4D46z2H_yqoabGMdqlHI4rEzpio-TlZEit4eEd9MCNfHEqk56cr3AC1cdC5D4tkY2SgQQ-vp84mKcP77NxqClcOnluEVHsUW4BjDaS3Pw_Vhik7loWosDTFXhjwgnIqQwr3wmsVUajHuDLHMgMLI4JFSO_ka0_PgqF7W_imxBZ56h7-Z2zqcGxWaa3ssy8J7GEiCSMeZuWu0Fx2dEHkaTKEl0OAuTWXJXqEr3z_I62c_8Xb-ZQQ-KegAQLUwb5vzERHh3aKauUDCQwjyCot6dpQVu-4qoFR-T9FyXVqnXpVM6DjVQa3OnSY1394HDVeQrq3mhTHavIuxqN6pXGYyYNrdvyPOfAIBgGRGXXbzD8XvD4fi5z5TgQz7QHg6dnclox-CBBTxrTDV4ltI-j6T8QJRAf2Y9pBKUZo1vrAenLkKRSd8yZnOY5-IHVvra3rqU4HhtrCaMUfDa9aLiUqew77hyO6CGqHP1BZ4pU2UjCtjwaL3WVKHc2fPrl5iVJAlz6AcDkRF0R9pkMcT7z-uHhFQ6OnZIU4WNJw4fH1OKpolg1XLpAC3fc1WRB5tS2yvRaYQ46m5eFpXWochGPSLFxPjz4JFdopyXh73eDQ8LFb-JqKCO0-1Q6hSz0VnSIhEFqHFWqia7BEnMbh5zTrYGBiU1bip30nZHlKKJBgAHM70yFMYmgFiIkhj4rIpEzi0rWrNDmb-X5t5e4clzusQzD7f7wOEuFzk8tmx3zAcVhL_dCfevYhH80aAR1xmTNBIXu1VezlkDFUVCyMtSeTt88Bka5VtC1ZdmTpgUNmzfAqnQ--hPeXh8Rofg6N8iXApjs9HQ6oUA_RNCTwIRpzM_>`_

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
    :caption: `eID Substantial Authentication with MRTD Verification Detailed Flow. <https://www.plantuml.com/plantuml/png/nLPjRnf74Fw-lsBgAAbDV13R-L2X4EU2NqoLs2V0YTgwGilT0DiikzVTFMpwwxkpTnmlAL6aLgg44DpDopFFp3wpxwpZnXLpoNxymSrmZf2YAIHo5Ud2IQ6GyS9fLSp7Q5ZkRKKgSguS7DnRD0V0BTnlF__CfKG7FUL3gnI3IRnjqkrTXiTTDjPF00T9xm8IenSYev3FFeZfpBsN1MvxaLLSk9asuY_kX5OmGBEeGCI3RUEF_Q6FgPDW8oeO5ybTCc2eCl1vlu84jo4gbz37gR3EB8FJnzxjjkdAx47rCbHEk6KDFZZqBXB6c7yk4T1Z_g3Zim2SZDCI-KimEDSEGQn2v4RhYL1J40fwmwXYaMhkMLiGat0bzIDZzn2zXRWDdmcCqy1J9nRS8VW4KBazgC9IB4e_ACRK2IUuX4VXPX2e-OH6J2eqZ7Kw7KXct2ASjE6EiEumtSS_2xGEEXqMX_m3Q4CIz-iNXm2f5AZSI6J7OCgdT-C_C7L77Ww4r6Neg1iCezWvRrF6vohR-pAYDWeLwhj1xcacSuhPQ8IeV1FgA4F7XGItp14EX1l9qvUPJeivOGia7pGQZFa28ggZBiFcMbc4mmhwg33Y6F0f5mRjIAYZLTrjwiaUTWZJzUKGMYj4U5wJqcascoysWjD_ih_HrhKX5rcKLqFKn2S-poKsjPbkjkRKfpPYpiroTvgYq6WwaBjlY1yQmAqfe2OEg1e_gMrotVQgws7-FRmXckxRPNI-EyKfaQPAoq3FddWbkvlLdBMXFgEVk1HPCAsnqOJV38T9wwHv0cUlJk5A5zHqNqmPj0qpvtBRRhM2X3KVm-HlSjTAP_HCJV6yqPWRbvNjxxnP_nxz_7duDem3fGpoqFPJLGEhY6Wq7bHoD_2DnKodKN1j2ILS3T43-tOZ7zH_UG0OqxbZ010m4ryaKstmW9qHk43FxQ_UPQBDF8GWMpA1gAvpruHqaR4g7ZLWaucwXKH5tPTJtvSuJJ5tc5K5bjpgVAIqIl4OwXuS-tuLz3KFjHxgl5HHkJmAI7p_EMDSEkXDIcWMb7R05rn8FfO8JWS6TlPBg2o6CAIhVf6fy62DWsvy6onMgjbRFqPf4KITJ8yT5mepu0u63dCuEQbZa-VbapCyTG4eJ8oUasD9sjJe8g_srYyelKp3xLNNvt98BlL19FZX77dIuQ8I9KXedC1_4cqjMalc_fdJgPP1ymd52iflpwO6KVt-5hfGDoZESxdMWYJkNbAR-iWpkBW-EQOl_psuknYHUGZLXQYE5MJmdoo1xKlRYmURMUjqCHrwgHKjdwGO-_Vm1PTbHFBPa_jxt7PWR3i5gXMNEyhpe6ou8gp7S0-0_Y2EJb-z_Wcic2hk2eFK4EfNxKcjtYiKQmNxfcOiQEik_pVL063RUa50Le33K2we3hgEK932haXuKAiLIWjoKKcmvmRJBqUCxGZBXZwyWhil-qLbpTftwul1J1XCmmeDvGV1yR3NeXEQ559HCxzX45hutkX7YoOQSuiPN0aQegvM4s7czMZxdLvlctsjQgNZywzJZGW2PYyqRSvHTRhBrN_ePaONqncCImH7czlnzRvhMCdInfga6kX6iiSma1OYTNKMsFsNM_NSMwS-L5a4lA11gVy8QpiXmFEp-FdfbV_ilzWOfHs2fjCP7yS3Bv-zwvlXTV_oyfODPmWJKhvKAoTKWHPuccgJqLbtUljQ70ovXGmdfD-hcLzVecsEwVgoYoeBgTax_wkOoxy1>`_

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

    client_id=47b982369791d08003a7283f059cb0d1&
    request=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJmODU1NWNlYi1jNjVjLTQwMjUtOTM3OC1iNjY3MmI2MTQ5YWYiLCJhdWQiOiJodHRwczovL3BpZC1wcm92aWRlci5leGFtcGxlLm9yZyIsImlhdCI6MTcxNTg0MjU2MCwiZXhwIjoxNzE1ODQyODYwLCJyZXNwb25zZV90eXBlIjoiY29kZSIsInJlc3BvbnNlX21vZGUiOiJmb3JtX3Bvc3Quand0IiwiY2xpZW50X2lkIjoiNDdiOTgyMzY5NzkxZDA4MDAzYTcyODNmMDU5Y2IwZDEiLCJpc3MiOiI0N2I5ODIzNjk3OTFkMDgwMDNhNzI4M2YwNTljYjBkMSIsInN0YXRlIjoiZnlaaU9MOUxmMkNlS3VOVDJKenhpTFJEaW5rMHVQY2QiLCJjb2RlX2NoYWxsZW5nZSI6IkU5TWVsaG9hMk93dkZyRU1USmd1Q0hhb2VLMXQ4VVJXYnVHSlNzdHctY00iLCJjb2RlX2NoYWxsZW5nZV9tZXRob2QiOiJTMjU2Iiwic2NvcGUiOiJwaWQiLCJhdXRob3JpemF0aW9uX2RldGFpbHMiOlt7InR5cGUiOiJvcGVuaWRfY3JlZGVudGlhbCIsImNyZWRlbnRpYWxfY29uZmlndXJhdGlvbl9pZCI6ImRjX3NkX2p3dF9waWQifSx7InR5cGUiOiJpdF9sMitkb2N1bWVudF9wcm9vZiIsIm11bHRpX3N0ZXBfbWV0aG9kIjoibXJ0ZCtpYXMiLCJpZHBoaW50aW5nIjoiaHR0cHM6Ly9pZHAuZXhhbXBsZS5vcmciLCJtdWx0aV9zdGVwX3JlZGlyZWN0X3VyaSI6Imh0dHBzOi8vc3RhcnQud2FsbGV0LmV4YW1wbGUub3JnL2NoYWxsZW5nZSJ9XSwicmVkaXJlY3RfdXJpIjoiaHR0cHM6Ly9zdGFydC53YWxsZXQuZXhhbXBsZS5vcmcifQ.AuthRequestSign456_NoKidJWTSignature-abc123def456ghi789jkl012mno345pqr678stu901vwx234yz567

When the ``it_l2+document_proof`` object is not present in the authorization_details array, the PID Provider MUST authenticate the User with CIEid LoA High.
The PAR Response and the Authorization Request are the same as in the IT-Wallet Specification.

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
     - REQUIRED. It MUST be ``mrtd-ias+jwt``.
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

A non-normative example is provided below:

.. code-block:: http

    HTTP/1.1 302 Found
    Location: https://start.wallet.example.org/challenge?challenge_info=eyJhbGciOiJFUzI1NiIsInR5cCI6Im1ydGQtaWFzK2p3dCIsImtpZCI6ImQ0ZjhlMDJlZWJhMDdhNTM3MmUxOGVjYzU4NzA5ZDA2In0.eyJpc3MiOiJodHRwczovL3BpZC1wcm92aWRlci5leGFtcGxlLm9yZyIsImF1ZCI6IjQ3Yjk4MjM2OTc5MWQwODAwM2E3MjgzZjA1OWNiMGQxIiwiaWF0IjoxNzUzNTU1MzU4LCJleHAiOjE3NTM1NTU2NTgsInN0YXR1cyI6InJlcXVpcmVfaW50ZXJhY3Rpb24iLCJ0eXBlIjoibXJ0ZCtpYXMiLCJtcnRkX2F1dGhfc2Vzc2lvbiI6Ind4cm9WckJZMk1DcTRkRE5HWEFDUyIsInN0YXRlIjoiZnlaaU9MOUxmMkNlS3VOVDJKenhpTFJEaW5rMHVQY2QiLCJtcnRkX3BvcF9qd3Rfbm9uY2UiOiJub25jZTEiLCJodHUiOiJodHRwczovL2Vkb2MtcHJvb2YvaW5pdCIsImh0bSI6IlBPU1QifQ.i6p_FN7qNNawyL4KnOV1r8FrNVjzd-7Ve1wEGASHNnlXwuJ1f216v0Ml_KpVrq9yXkmOo_M2xZwih2SlHVfrzkuG3Pn7LWRL7dsyCtqEY2e58rFHjCa2miBnnKr0NU4wcBMMYe2_qKCOkA7SOa7usNTBluBLMQ28GfiMbr3tcpfpM4rD0POKQcfijvNkNbh-VdOxM8GdHb6IQO_xfpsaSzd8cc0k5yIYCWjDTeINVKebIz4m9Rm2JStvRrWUq8OCqkv-8dTJH9q-JXx0PzJC998RMwe6tqSL-kkE3dZLWwCJdP8Z7bITtowU49rEe-AkrGxVma4ANPq317umEfUwmw

The Authorization Server MUST:

- Generate a unique challenge identifier with sufficient entropy (minimum 128 bits) for cryptographic security.
- Create MRTD Proof JWT with proper header (``alg``, ``typ``, ``kid``) and payload parameters (as defined in the table above).
- Sign the MRTD Proof JWT using its private key with the cryptographic algorithm chosen. See Section :ref:`algorithms:Cryptographic Algorithms`.
- Construct a secure redirect URL with proper encoding to the Wallet Instance universal link.
- Set the redirect timeout to prevent indefinite waiting and handle timeout scenarios
- Optionally request MRZ information directly from the CIE National Registry using the authenticated User's taxpayer identification number.
- Maintain session correlation between the LoA High result and the document proof challenge

The Wallet Instance MUST:

- Validate the JWT signature using the PID Provider's public key obtained through trust evaluation.
- Verify ``aud`` claim matches its ``client_id``.
- Verify ``iat`` and ``exp`` claims indicate the token has a correct issuance date and has not expired.
- Verify that the ``status`` field is set to "require_interaction".
- Verify the authentication type matches the expected value ``mrtd+ias``.
- Extract HTTP target URI (``htu``) and method (``htm``) for the next step.
- Handle JWT validation and network errors, and provide user feedback with appropriate retry mechanisms.
- Extract correlation parameters (``mrtd_auth_session``, ``state``, ``mrtd_pop_jwt_nonce``) for subsequent requests.

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
    
    eyJhbGciOiJFUzI1NiIsInR5cCI6Im1ydGQtaWFzLXBvcCtqd3QiLCJraWQiOiJiM2YxYTZjMmU5ZDU0YThmOWMzZTdkMWEyZjRiNmM3OCJ9.eyJpc3MiOiJodHRwczovL3BpZC1wcm92aWRlci5leGFtcGxlLm9yZyIsImF1ZCI6Imh0dHBzOi8vd2FsbGV0LmV4YW1wbGUub3JnL2luc3RhbmNlLzEyMzQ1IiwiaWF0IjoxNzUzNTU1ODAwLCJleHAiOjE3NTM1NTYwMDAsIm1ydGRfcG9wX25vbmNlIjoiOWYyYzRhN2UzYjFkOGM5YTZlNWY0YjJhMWMzZDdlOGYiLCJtcnoiOiIuLi4iLCJjaGFsbGVuZ2UiOiIuLi4iLCJodHUiOiIuLi4iLCJodG0iOiIuLi4ifQ.signature

JWT decoded header:

.. code-block:: json

    {
      "alg":"ES256",
      "typ":"mrtd-ias-pop+jwt",
      "kid":"b3f1a6c2e9d54a8f9c3e7d1a2f4b6c78"
    }

JWT decoded body;

.. code-block:: json

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

- Generate cryptographically secure challenge data with sufficient entropy (to be used in Anti-Cloning Internal Authentication protocol by the Wallet Instance), storing it with an appropriate expiration time. Moreover, the MRTD PoP Service MUST ensure challenge uniqueness to prevent reuse attacks.
- Create a new unique ``mrtd_pop_nonce`` for the next step to prevent replay attacks.
- Validate session continuity by ensuring the ``mrtd_auth_session`` parameter corresponds to an active session.
- Return HTTP *202 Accepted* status to indicate asynchronous processing initiation.
- Include proper Content-Type header (``application/jwt; charset=utf-8``).
- Handle service errors and return appropriate error responses.
- Extract and validate MRZ information if provided from external registry services.

**The Wallet Instance MUST:**

- Validate HTTP response status (*202 Accepted*) and content type.
- Parse JSON response and validate required parameters (``challenge``, ``mrtd_pop_nonce``).
- Extract challenge data for cryptographic document validation.
- Store new ``mrtd_pop_nonce`` value securely for subsequent validation requests.
- Validate optional MRZ information if present in the response.
- Extract HTTP target URI (htu) and method (htm) for the next step.
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
     - REQUIRED. It MUST be ``mrtd-ias+jwt``.
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
     - REQUIRED. IAS validation data containing Anti-Cloning Public Key, and SOD.

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
      "mrtd_validation_jwt":"eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL3dhbGxldC5leGFtcGxlLm9yZy9pbnN0YW5jZS8xMjM0NSIsImF1ZCI6Imh0dHBzOi8vcGlkLXByb3ZpZGVyLmV4YW1wbGUub3JnIiwiaWF0IjoxNzUzNTU1NDAwLCJleHAiOjE3NTM1NTU3MDAsImRvY3VtZW50X3R5cGUiOiJjaWUiLCJtcnRkIjp7ImRnMSI6IlVEeEpWRUU4VTAxSlZFZzhQRXBQU0U0OFBFcFBTRTRnVTAxSlZFZzhQREU1T0RBME1UVThUVDxQTnpjM056SXpNUT09IiwiZGcxMSI6Ik1USXpORFUyTnpnNVFVSkRSRVZHUjBoSlNrdE1UVTVQVUVGT1IxSlRWRlZXV0ZsYVUwRkVSVVU9Iiwic29kX21ydGQiOiJNSUlGempDQ0JMYWdBd0lCQWdJSVFPWTJLSkdGVFVJd0RRWUpLb1pJaHZjTkFRRUxCUUF3WHpFTE1Baz0ifSwiaWFzIjp7Imlhc19wayI6Ik1JSUJJakFOQmdrcWhraUc5dzBCQVFFRkFBT0NBUThBTUlJQkNnS0NBUUVBejEyMzQ1Njc4OTA9Iiwic29kX2lhcyI6Ik1JSUZhRENDQkZDZ0F3SUJBZ0lKQUwyS0pHRlRVSXdEUVlKS29aSWh2Y05BUUVMQlFBd1h6RUxNQT09IiwiY2hhbGxlbmdlX3NpZ25lZCI6ImExYjJjM2Q0ZTVmNjc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MGFiY2RlZjEyMzQ1Njc4OTBhYmNkZWY9PSJ9fQ.xyz456abc789def012ghi345jkl678mno901pqr234stu567vwx890yz123",
      "mrtd_auth_session":"wxroVrBY2MCq4dDNGXACS",
      "mrtd_pop_nonce":"9f2c4a7e3b1d8c9a6e5f4b2a1c3d7e8f"
    }

**The Wallet Instance MUST:**

- Perform `ICAO 9303`_ compliant NFC document reading (PACE,etc.).
- Validate document cryptographic signatures and certificate chains.
- Extract identity attributes (DG1 and DG11), Anti-Cloning Public Key from document data groups, and SODs (form MRTD and IAS Applications).
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
- Parse and validate the ``mrtd_validation_jwt`` signature (using Wallet Instance's public key) and structure.
- Extract and verify document evidence from the ``mrtd_validation_jwt``.
- Validate document authenticity using `ICAO 9303`_ standards.
- Verify Anti-Cloning challenge response.
- Validate document cryptographic proofs and certificate chains.
- Perform identity correlation between document data and LoA3 result.
- Check document validity (non revocation status).
- Verify the binding between IAS and MRTD applications by checking that the NUN extracted from DG1 is present (as hashed value) in the IAS SOD, and the DG1 itself is present (as hashed value) in the MRTD SOD. This dual verification ensures both applications reside on the same physical chip.

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

**The MRTD PoP Service MUST:**

- Generate a new nonce  ``mrtd_val_pop_nonce`` for browser-based final confirmation. 
- Return HTTP 202 status to indicate async processing completion.

**The Wallet Instance MUST:**

- Validate the response.
- Extracts the parameters nonce  ``mrtd_val_pop_nonce`` and  ``redirect_uri`` to prepare the next browser-based GET Request.

Browser-based Final Confirmation
"""""""""""""""""""""""""""""""""

Upon successful MRTD PoP validation, the Wallet Instance MUST redirect the User Agent to the ``challenge_redirect_uri`` specified in the initial Authorization Details Object, including the ``mrtd_val_pop_nonce`` and ``mrtd_auth_session`` as a query parameter:

.. code-block:: text

    https://pid-provider.example.org/l2plus-callback?mrtd_val_pop_nonce=0f2bff024317345b6927ce17e776361d_signed&mrtd_auth_session=wxroVrBY2MCq4dDNGXACS

The Wallet Instance MUST validate that the ``mrtd_val_pop_nonce`` matches the value received from the MRTD PoP Validation Response.

**The Authorization Server MUST:**

- Validate the ``mrtd_val_pop_nonce`` matches the value sent in the verification response, and that it is signed using the Wallet Instance’s private key.
- Verify the ``mrtd_auth_session`` parameter matches an active session.
- Verify all authentication steps (LoA3 + MRTD PoP) have been completed successfully (including the identity correlation between LoA3 and document evidence). 
- Generate the final authorization code.

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
   * - **invalid_client**
     - Wallet Instance authentication failed.
   * - **invalid_request**
     - HTTP Request is invalid or malformed (malformed structure, missing data, etc.) or required session parameters are missing or invalid.
   * - **access_denied**
     - User is not eligible for eID Substantial Authentication with MRTD Verification mechanism (e.g. CIE not found in the CIE Registry)
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
   * - **invalid_document**
     - Document cryptographic validation failed (SOD validation, IAS/MRTD binding, revocation status, etc.).
   * - **id_matching_failed**
     - The matching between the identity obtained during primary authentication (eID LoA3) and the one obtained from the PoP of the Electronic Document failed.
   * - **temporarily_unavailable**
     - Document validation service or CIE Registry service is temporarily unavailable.

HTTP Status Code Mapping
^^^^^^^^^^^^^^^^^^^^^^^^^

Error responses MUST use appropriate HTTP status codes:

- **400 Bad Request**: For ``invalid_request`` errors.
- **401 Unauthorized**: For ``invalid_client`` errors.
- **403 Forbidden**: For ``access_denied`` errors.
- **422 Unprocessable Entity**: For ``invalid_document`` or ``id_matching_failed`` errors.
- **503 Service Unavailable**: For ``temporarily_unavailable`` errors.

Security Considerations
-----------------------

Secure Session Management
^^^^^^^^^^^^^^^^^^^^^^^^^

The ``mrtd_auth_session`` parameter serves as the primary correlation mechanism between authentication steps. Implementations MUST ensure this identifier has sufficient entropy (minimum 128 bits) and is cryptographically secure. The session identifier MUST be validated at each step to prevent session fixation attacks.

Each authentication step MUST be cryptographically bound to the OAuth session through signed JWT validation to prevent session fixation, session confusion, and identity substitution attacks. The Authorization Server MUST maintain the correlation between the LoA3 identity and the document proof within a single session context.

In particular, each authentication step MUST validate the correlation between:

- Session identifier consistency across all protocol phases.
- LoA3 identity attributes binding to the session context.
- Document evidence correlation with authenticated identity.
- Temporal sequence validation to prevent out-of-order attacks.

When components operate outside the PID Provider boundary, the following additional security measures MUST be implemented:

- Secure Inter-Service Communication (for example, through Certificate pinning, mutual TLS, etc.).
- Encryption and integrity of sensitive session data and/or personal identity information (for example, using JWE/JWS tokens).
- Distributed locks for session state updates. 

.. _fig_eID_MRTD_Security_Controls:
.. plantuml:: plantuml/l2plus-security-controls.puml
    :width: 99%
    :alt: The figure illustrates the eID Substantial Authentication with MRTD Verification Security Controls.
    :caption: `eID Substantial Authentication with MRTD Verification Security Controls. <https://www.plantuml.com/plantuml/png/nLT_Rzl84Vr_FyNKGL9RCUt8JjjKYEmmyW-hI6p1aXkqTI6io96q3RNBxYvb-pxzxOmeIfHFWGztm046GIzdPzwycNqx-kIyjBwOPUBFV_9Jd24aQ8iCfOvCuJEbKSZ26rtCHcX57cnLedAfFUpSERGx81tSrTU_oIn33rqTNEi4sIIkctIwvxpS4IFp2B3Jwvv1pvgvIidbgozgClMVimBhkyWgBlpKMFMJzCfewAETbo3YVjtuw-qW-3Gzjb4bZBFUJQylKASGuZw31DViLMPmYnFbl7tYJL-xrtNJfTczxgQelV9F5NZUq3th2I72UeQ00VCN4nypS39E5iZVWiMPyGXgwIAtneoLde3Iq1r49OkKSzUvWfY4Yymy2747qGd4BVX6OBm1cNWrbnuX181osxqk7FcQ5PbNaVEOWwm3c64WCXMYtMv3RoeTGhC5DuHoW-DR_7-1paExBMAEt8SMzEBRwiCkG9Afu7geqdsmYzMRqVymyNi12C232axPTTHXmoZsFjWi_4kTRlqOKG6LviokK0Q2oPnyDXhiLQv37QRefSh0F-K8EyeFiwEtgKcA6M5ZUdSQ3I520X7bKQNXSgCTmcu9VLXOjG_uc2kBRgZqtZBl5bLZ2pk4wV9y08TBH7XQaT8-E3Xui-QS_YVxA-Dy2tALHddPFWVuA6TvXWV6JjPBSnH2MpMJzccpZoBkC3gAcr-87sezw1SZEebUoOoAQ3MrdPdJZduuQtAEEeGEnyrDHRzpJCU3RPYe4-hc5WMf-wyo5-4xV2H2xreB77ApqnEYLxFbaiZd_gewl1pWEaF7BQXE_3zbfb9soatRBy_BrM3GEsmUDE7utH5Sc88RwOjPX6_1rFlSjGuFMH0F7lWShTVZC9dIcfxWQQCnipvTj5Jxu-fz-8zlWvFGOhKKdcVmjxKCkBLObbgXfwiKId8RZNlTk-c7jiBGo147ELHQ-IgPaCAFs-XU_vx7hvOQmtwUtb_teT_vG8-_hoLgSYy0W3THHKXMMn0IzLRX74Fr_Xr2ZOsTSMYo9HE8AdusJSYv4AK_Ad6TmRATYCAgyaUXyd6IOEunBObPLC_aGsrqWljGLPcPsJNvGkkpfpsEdqelXP2PX-vu0SX1I13aNAfCZZ84RvYlZLkGyuc1ZycokcIg0aJheHDViyLIsxkhPSmSWgg2cP6NIcCAqaEVTBtPh7pJplD7RsNY6IYChPdHnWLL4skAlBnT_uLPk4pW-g8JOdcaBPLe47m-oO5gE2i557hKV13-UiOvT2wOqvetYSduPY8KIoZ_UJMnYFg_9z21gYnndcShtUh5dNCgpYtA5Cukc_lq2C_-pTcGpDbL1wBA5qlsBrc2s1Qs6_VNerRXOfATp6Yw8dl5A7o7x_Yqy4XxjiH-qROwZFecfZfqquRstMl7Wyog-RO0kEt7qT6xzn_0gOcMlh181GckLZkfr5jbPQMCFrIO04MDd_umZG7uTIf3Zz0F8ZoF-FsOd-_NrAUkEfJOaW1kyZdnGaCOWIhSajHxlHmVQ3YObrT5u1gJxtj2RCZJcigyWvllBv7AvbyOAUVIN5qBsrLjLS0N2vp5L5bCUFBWIh3YXOnNgYT4gHxSLpymu6xwRCs3GnkDfCCKBXJrSyVeiRApwfI5KQYwKBTrpM4oEcNlxUS1XmG4qpU6XebXAJSyHr65S351xVgfDSLa2gC5ehtwnVlYgsarHRpVCWANLDV6YKQ3fi4jXimyU-gOb4lq6wUFqs2TcBJC7DPfW3VAkJOxU7qSlpww27_REAypjCySTI-l1fUtv-VNOZ1569EI9qPxfGjq89F4s9IqovlwZn4sb0vI7FDzL9xXrKyNbsEYngN4hUZ-5DwAMVOp>`_

Cryptographic Challenge Generation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The MRTD PoP Service MUST generate cryptographically secure challenges with sufficient entropy (minimum 256 bits) for document validation. Challenge values MUST be unique and MUST NOT be reused across different sessions (cryptographically bound to the specific OAuth session context) or authentication attempts. The challenge generation algorithm SHOULD incorporate the ``mrtd_auth_session`` identifier and timestamp to ensure proper cryptographic binding.

Nonce Lifecycle Management
^^^^^^^^^^^^^^^^^^^^^^^^^^

Each step in the eID Substantial Authentication with MRTD Verification flow MUST use unique nonce values (minimum 128 bits) to prevent replay attacks. Nonce values MUST have appropriate expiration times and MUST be invalidated after successful use. The PID Authorization Server and MRTD PoP Service MUST maintain synchronized nonce validation to ensure session integrity.

Moreover, each nonce serves a specific security purpose.
- ``mrtd_pop_jwt_nonce`` MUST be correlated with the MRTD Proof JWT.
- ``mrtd_pop_nonce`` MUST:

- Be cryptographically independent from ``mrtd_pop_jwt_nonce``.
- Incorporate the ``mrtd_pop_jwt_nonce`` as input to maintain the chain of trust.
- Use a different entropy source to prevent correlation attacks.

 - ``mrtd_val_pop_nonce`` MUST:
 
- Be signed by the Wallet Instance private key.
- Include anti-replay timestamp validation.
- Be verified against the entire nonce chain for integrity.

PID Provider Metadata
^^^^^^^^^^^^^^^^^^^^^^

In addition to the ``trust_frameworks_supported`` values defined in section :ref:`credential-issuer-metadata:Metadata for openid_credential_issuer`, the PID Provider Metadata for ``openid_credential_issuer`` MUST also support the value ``it_l2+document_proof`` indicating the multi-step Authentication protocol described in this Specification.

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
   * - **SC15**
     - The MRTD PoP Service verifies that the binding between IAS and MRTD applications by checking that the NUN extracted from DG1 is present (as hashed value) in the IAS SOD, and the DG1 itself is present (as hashed value) in the MRTD SOD. This dual verification ensures both applications reside on the same physical chip.
     - Phase 3
   * - **SC16**
     - The MRTD PoP Service verifies that the identity proven during the eID LoA3 phase is correlated with the identity proven during the MRTD PoP phase.
     - Phase 3
   * - **SC17**
     - The MRTD PoP Service verifies that the CIE used during the MRTD PoP phase has not expired and not revoked by interacting with the CIE National Registry.
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


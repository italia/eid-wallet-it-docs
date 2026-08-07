.. include:: ../common/common_definitions.rst


Autenticazione eID Substantial con Verifica MRTD per Emissione IT-Wallet ID
===========================================================================

Questa Sezione definisce un protocollo di Autenticazione eID Substantial con Verifica MRTD che si integra nel flusso di emissione dell'IT-Wallet ID come definito nella Sezione :ref:`credential-issuance-low-level:Flussi Dettagliati per l'Emissione di Attestati Elettronici` estendendo i flussi OAuth 2.0 per includere:

	- Identificazione elettronica con Livello di Garanzia "Substantial" (LoA3) come step di autenticazione primaria.
	- Verifica di documento elettronico come livello aggiuntivo di verifica dell'identità.
	- Correlazione di sessione e binding di sicurezza tra gli step di autenticazione.
	- Integrazione con i flussi di emissione Attestati Elettronici.

Mentre l'autenticazione CIEid con LoA High rimane il metodo primario per l'attivazione Wallet e l'emissione dell'IT-Wallet ID, il meccanismo di Autenticazione eID Substantial con Verifica MRTD definito in questa Sezione fornisce un approccio alternativo per migliorare l'accessibilità e l'usabilità del servizio, senza compromettere la sicurezza complessiva dell'ecosistema IT-Wallet.

.. note::
  Questa Sezione attualmente supporta solo la carta d'identità CIE per il protocollo di verifica MRTD, ma il protocollo descritto in questa Sezione PUÒ essere esteso per supportare altri Documenti MRTD come i Passaporti Elettronici.

Principi di Progettazione
-------------------------

Il protocollo aderisce ai seguenti principi di progettazione:

	- **Compatibilità con Standard**: Estende i framework di autorizzazione esistenti senza modifiche che rompano la compatibilità con il framework OAuth Authorization standard.
	- **Autenticazione Multi-Step**: Implementa l'applicazione progressiva dell'autenticazione con verifica MRTD.
	- **Integrità di Sessione**: Mantiene correlazione sicura di sessione attraverso gli step di autenticazione.
	- **Flusso Unificato**: Integra fattori di autenticazione multipli in una singola sessione di autorizzazione.

Architettura di Sistema
-----------------------

L'architettura di sistema comprende i seguenti componenti principali:

	- **Istanza del Wallet:** Gestisce la richiesta IT-Wallet ID secondo le Specifiche IT-Wallet, supportando capacità crittografiche aggiuntive per la lettura di Documenti Elettronici MRTD/IAS secondo le specifiche `ICAO 9303`_ e `BSI-03110`_.
	- **Sistema di Autenticazione eID Substantial con Verifica MRTD:** Orchestra il flusso di autenticazione, integrando Provider di Identità LoA3, Servizio di Verifica di Documento Elettronico, ed eseguendo tutti i controlli di correlazione di identità per garantire che l'Utente che richiede un IT-Wallet ID sia lo stesso Utente autenticato.

		- **Server di Autorizzazione EAA:** Gestisce il flusso di autorizzazione per l'Emissione IT-Wallet ID, coordinando l'autenticazione Utente e l'identity proofing remoto.
		- **Servizio MRTD PoP:** Gestisce il proof of possession di documento elettronico con validazione crittografica del documento.

	- **Provider di Identità LoA3:** Fornisce Schemi di Identificazione Elettronica con conformità eIDAS LoA3 (CIEid e SPID).
	- **Registro Nazionale CIE:** Agisce come fonte autentica per la CIE. Fornisce informazioni relative allo stato di validità del documento. Fornisce anche opzionalmente i dati MRZ (numero documento, data di nascita, data di scadenza, cittadinanza e genere) per migliorare l'esperienza utente.

.. _fig_eID_MRTD_System_Architecture:
.. plantuml:: plantuml/l2plus-system-architecture.puml
    :width: 99%
    :alt: La figura illustra l'Architettura del Sistema di Autenticazione eID Substantial con Verifica MRTD.
    :caption: `Architettura del Sistema di Autenticazione eID Substantial con Verifica MRTD. <https://www.plantuml.com/plantuml/svg/dLHXRzis4FtkNt4r1iJnuZYjimyRkg2AhIq2uiQml1GT1WWqUOw9KgH6dk8wG__xICfH7JT0Wnhvm1nFZ-_klRjtZfYbkbHm_UPdcDQAv20dh22fQMsiV60aZOR4yhKav5HRx1ozeZMM21njhP3fWQb9IOsTLr9pLGk4j-FpuVYy69koCXerNNIkiabQv8jqdjuiFixItd7dw3hvUFFNelYGBQwAw_JFzFt4Hpj7CC6L1uDyDiyMQRu7IdN5X1qDkIbBeo-UkLaPJGEsGMTA7Fmo58pOaZbyGQf3Uu_s1ObI59nPyOBC3LCAwNk9GwaTIQf9Xf8w_gWmQe7P1F9wwOXfaan5GT0VUQF8Hj8QflF516xHofNapmZLQGKeqi_KQmYTGFT3F42c0pZ7hWzDpL8gXAIgmdzNJ0k53hB5u35t0XR_hT4HX8uAC1eydxqCGhxMHfcxBGHOmQm81_xf53A2offxAT11ly_jjY9pPrcrbXmugvX_MfBqbojZGqt3BCaXLSZ96krp9eRN9Me2Yqn8VTVlGoyR9pVmw-XiT0ANUJOu6xr-VNRSFVd9LLOI_jvjYkrwHrsQEh3PzgHpDLfVNfeaC6i8sUun_DS1_slJoZ04XIEi2kPx_k0_-34jygq7AKC_RxmgwCWoGWSHVn3mWJt5MIcp0QO5M2mD8KWHBcaRkcTMll2MRFYrulQGiOPg4MqSIdmwldaCHoRXuit1TFzXMOaROp_5ns-ooVdjEFkk3q8kQt5Q_jmOAwIEaJqzN4FX-1dwml2YCbKaBpdwTsClPsOMYSl6eRTCIH5Hs-WUG_pg5h5pIzCry7-LSGwTQwLwwi0s_pwySCXxD-yxubywNmwdIXasAgIeF9bhaumWUnIjTLXZ86_fU1-znCC23HUx9BTlzmQXjL6JxA0tpb8fOjlpMJRPD_lU3l543mXoYON5E-d8RlsB7WNUHsIcOBwBTtSNasPZHce99mVCnJ7VwKoCv3s2CxNb6ASrNFeFJw4jH6eVBnlg5XKZ540c9iO6IueBWchdfGdXLe2uA9Xo1apLy5FRTd74pEdyRmXB7NgjQBekbzxn8Om1S2ajhKy0FrVIRcFq1BWa-O3QhMKLstU7Mg0z3hHa6Hx0Y5uxjE53j18rnzEz1ejTNq9tvwZQLNeuUUs4DRFmJ-Z5q-d9dAiVb-wbDHk7TX0twY7qjrCnUMfiLozB6LqTrPfb0U6G4BmTN1n2mM_GxVTRdquPyNNSgjt8eBZqI_kPdR9dz3oPNW_zdXWVRB1dYseXlwdem9c94BBHlTtuhOE205_BV8TQrANw7m00>`_

Flusso High-Level
-----------------

Il protocollo consiste nelle seguenti fasi sequenziali:

1. **Richiesta di Autorizzazione OAuth**: PAR e richiesta di autorizzazione con requisiti di Autenticazione eID Substantial con Verifica MRTD.
2. **Autenticazione Primaria**: Identificazione elettronica LoA3 (SPID/CIEid L2).
3. **Validazione MRTD Proof of Possession (PoP)**: Lettura di documento elettronico e verifica crittografica (controlli di Proof of Possession, integrità e autenticità).
4. **Risposta di Autorizzazione OAuth**: Emissione finale del codice di autorizzazione.

.. _fig_eID_MRTD_High_Level_Flow:
.. plantuml:: plantuml/l2plus-high-level-flow.puml
    :width: 99%
    :alt: La figura illustra il Flusso High-Level di Autenticazione eID Substantial con Verifica MRTD.
    :caption: `Flusso High-Level di Autenticazione eID Substantial con Verifica MRTD. <https://www.plantuml.com/plantuml/png/ZPHnY-984CN_zrFKUGSp0piuYN6Lmv4Tr6M5MLPK5kulwQGhiRbETwwxCfxxwJUTQ2QACW4HxRp-zUkgb_fYYHdAKma_NdBQmVTSadXS4sRW_gCY4J4IMi4taUmUN_4D9NoLUj_vGwX8vXnXF0rwqs0xrMcc5IgQTBujPlFjUZDVpNzi_bdExnyQOiepnas_5sj5ZsoFLgVuEEZb5itaOrcgGo5nooIr4DkTGCbRYl_5GmjLtFxq20s9s5KFMwWv8nOoYst0Eh4jP89l8sPu2oN-7-sOIjfURC-an0-5FQ4i2SfTTYQTpXrCSqiw1Ki7YS0n5aguPnPYRI0k4WNPZbcqdHVEvn9JLBHXoNstNFMwd-2lC9bggSrpzq_F-pmAkLjpHnvNzpj1MEgquMXEsgSm68s2xiDLhd_E7OO-7s4xxe1vyUTHmRsx1kwVW_cmFtZosu7PapzyyWfm2sxiZU92sueRUSEdczpWdElp0VE7xRWUzhaN5jmE2PBO6Lln2__sHfDnEC753DPvQ8af4anUpfIzS2DdjPd1JpGYFYwFU-5at7EKoGaMJ1hZPsaqwKWNFyh0dAIeE5GEEdSIOmBIO8fT15mOZ1pPvN3ceeTG-801f4oeO-w0MSZGW51PJc0pZ6f3dNgstLTf_0JTycnmfUzMazDzQID-LJTRuNyvMkewvSiAcEB0pWIc4bGbICkfQztKZNRkzL89bWfXoZvPLtMR6K7ut7qVQswLM6AVgnwwtbvQzMkhVkd5Y9IPmqKVt9DN_T87b1YHqKf483WggYi0z-lbOjQRBkQ2mwl_qFHJJCuB8xupSdVXf5yxwRlpflKz6wMQwIXtzuNCQ1r3yScqjMYjiz2eH_FuuvoxiD1t5cuxE3jigPVmaqd1wsBCt-l0Jog3Z0kLbAsCp24ZdHYMxGh9MoExLvrzP2oeZGMtysIB7HRTywz2CNaHfqXp165jpbI4jzBIz16KFOArAtxrRfOpE4JQ8whJB5wXtAxgqBydokW8aGFfAqdwVYtCvRHdXBpxq80wMDsQHPauEXnd0N87snYH96Y0DvjLOztqRT3wHrhGxEwgYar9MnCp5UAjxdV1k85evABQxjecaR1P-nBm1HNFK_aR>`_

Gestione Sessione
-----------------

Il Server di Autorizzazione DEVE mantenere una sessione unificata attraverso tutti gli step di autenticazione, assicurando:

	- **Continuità di Sessione**: Identificatore di sessione singolo durante tutto il flusso di autenticazione.
	- **Correlazione di Stato**: I risultati di autenticazione da ogni step sono correlati.
	- **Binding di Sicurezza**: Binding tra gli step di autenticazione.

Poiché il Server di Autorizzazione EAA e il Servizio MRTD PoP operano all'interno dell'implementazione dei confini del Provider EAA, è RACCOMANDATO che la sessione OAuth 2.0 e i nonce utilizzati nel flusso del protocollo siano gestiti correttamente da entrambi i componenti.

Quando entrambi i servizi operano all'interno dello stesso confine di fiducia, i seguenti meccanismi sono disponibili per la correlazione di sessione:

	- Accesso diretto alla memoria agli store di sessione condivisi.
	- Autenticazione interna service-to-service utilizzando chiavi pre-condivise.
	- Validazione nonce sincronizzata senza overhead di comunicazione esterna.
	- Logging di audit unificato e correlazione di eventi di sicurezza.

Quando il Server di Autorizzazione EAA o il Servizio MRTD PoP sono erogati al di fuori dell'implementazione dei confini del Provider EAA, le :ref:`credential-issuance-l2plus:Considerazioni di Sicurezza` DEVONO essere prese in considerazione per rafforzare la gestione delle sessioni di autenticazione Utente. Queste misure includono ma non sono limitate alla gestione sicura dei token di sessione, validazione di sessione distribuita, e meccanismi di audit trail migliorati.

Flusso Low-Level
----------------

Questa sezione fornisce dettagli tecnici sull'Emissione dell'IT-Wallet ID utilizzando Livello di Garanzia Substantial e identity proofing remoto attraverso verifica del documento elettronico utilizzando un servizio di Verifica MRTD.

.. _fig_eID_MRTD_Detailed_Flow:
.. plantuml:: plantuml/l2plus-detailed-flow.puml
    :width: 99%
    :alt: La figura illustra il Flusso Dettagliato di Autenticazione eID Substantial con Verifica MRTD.
    :caption: `Flusso Dettagliato di Autenticazione eID Substantial con Verifica MRTD. <https://www.plantuml.com/plantuml/svg/nLPjRnf74Fw-lsBgAAbDV13R-L2X4ES2sAPAx1FWH6rTeULkW6sEtUlk7ZRzzTtPEuwNzA98hLG98RYRbsUUcNrctndBjSsNAVln1xl09KACEa-Hoq3bDXKI6S-jalboYffbpbR48kFImj6zGNq4tC3z_lFFF4tHma2wq396RnBkctG7VV-uowRg2U2e7uOGQRKI2OLyza7C5_PzckE-5rc5kLqeBVxYLYW98zIh4aGusZV-E1pt85AHjn4bZ5vq5uqOoWHStgyWmQsFobCOubmOgzVUwUFWTjzqO_OW1mbAA-ow0kyT1hs8CUQUfmWuwC475Lvuu6GS5yXVWiQbiWXY4oBJIis4d8EGC1W76nPxC30c9oBXAbMFZDr3y1R2DdmcB5O1ZwrOSOlWuaFfzI1pGw4e-oYVKYEiu2ay2hi0pymdr69MWc6iq-b0jE06uQmDTmJrWEWX_fcZiT3fiD3d7q4Red1OlJW6Y5E1qav4SWgwU7et_GDZU-BWG97QXmwwtZ08hNKsHNmkazgN0NLHI5_V3NB7CfbJp4R3H-MxK2S9MYvIiEiCuKZOINh-Cb5nlYHidkEZHeCnLq10TLHbc4n9Wt1SGf_aMfm2FcL2eva8URAfkxtNd1gQ2DnrVmoj3JIyhDZfD9lD5pjPw3_PtoXZsu2S1ravJ4ryuiiinQRIyzqUdJlCMYovNXzELU0xJWVpy0qHHOEuDmxKpP4hYoQsJQxxNbKzpBs7DyJNVRk8pW-dEIRsP67fUQg9Lz2yMyr56wgp-ecd8l6c5JOQzPlnE6gTDS_WujKvNAdST_-3AeAsOM5jPjgjbfUovgFlpIvthNX1p-GSBnkDfRP9CGUTDzlVavy_Zz_wkQ2KNYRQRhmgO2KHZSQ3ZEv6hh6Og3ZmhYqXXQqWEc3VRkI3_2zF0cCgimm0F6RYY-Ig3GwmrG9NwBZzrRdCb5xw46HB9X1iwpmqGPamLiQZ1kmpKRQGgAZwSkxw4iOnPXQJii22MvLDf98ndaBLWrFNhvo-bhxMOvKLQfgkJpmIrt_E64yj36O5D0DIMU0hBb8-JH6iyWmSx1bVMGX-I3Vz8bFXm6eBtV3MMspaSx1zZAb145KoDRLSI4o0MnXPpE3ih8fDdlqdgtbiFL2OQRKanuAqkLPvLkwlNp1rUWstLrsNooAvL0UHuFjpv4Y7NgbE4D4uWVj4oXWqnfdJCwjYbNhn9nGRAByzcsj4-VjRw4BLe33BqgqMH66tJsqQ8a-WTtrsIb_kUtJNcv2v3zM5e8hbzV2VB87LfHs4ezsiLRgG3dsg96sXA9-wz_05rqL4ygd9_Lrk-p3sdJpLagS7olCWZRygRCUm1i1m50Rdhrx_14RC9RUvHcg82xNrf5RN2iLMmRwf6IjQl-l_JJK0sBvU490DO3-KAwg3hYKK93SR4XxaPfVIfboL4koumVZB2MC7mhAZ3w_Wxakzg6nP-svzqPW8ZR5VeRvyBpWEzbPqg4a-bM_cDmny2zzhzMXG1rDkC84hGKFKLN8czB8QRRVJgsrJrwfMFBtyEjM4863oGj7cd9IdkrZzntQXLJvVmBH0SBAx7L_NtSSAbhPhqXDQVpNPUdZsVCYkIZpD_tAzNZhhs8Kgge4ND37L7s5CnmTuVX4-Fxzod_eRZfRA8YWwfk5fE78wEhY-6LyF-_rRDbuWp4W2OoMja3aQu76iT4A7tggQ6xFtu0OId7b5Bq_1rjXa66_lmIWJZu6zSx_oPVet>`_

Fase 1: Richiesta di Autorizzazione OAuth
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

L'Istanza del Wallet inizia il flusso di Autenticazione eID Substantial con Verifica MRTD inviando una Pushed Authorization Request (PAR) contenente una JWT-secured Authorization Request (JAR) con requisiti di autenticazione specificati tramite Rich Authorization Requests (RAR).

Authorization Details
"""""""""""""""""""""

Il JWT Request Object DEVE contenere gli stessi parametri come definiti in :ref:`credential-issuance-endpoint:Pushed Authorization Request Endpoint`. Quando l'Utente richiede un IT-Wallet ID utilizzando Autenticazione eID Substantial con Verifica MRTD, l'Istanza del Wallet DEVE includere un **Authorization Details Object** aggiuntivo nel parametro ``authorization_details``, con la struttura e i claim come definiti nella Tabella dei parametri JWT Request della Sezione :ref:`credential-issuance-endpoint:Pushed Authorization Request Endpoint`

Di seguito un esempio non normativo di PAR:

.. code-block:: http

    POST /as/par HTTP/1.1
    Host: eaa-provider.example.org
    Content-Type: application/x-www-form-urlencoded
    OAuth-Client-Attestation: eyJhbGciOiJFUzI1NiIsImtp…
    OAuth-Client-Attestation-PoP: eyJhbGciOiJFUz…

    client_id=47b982369791d08003a7283f059cb0d1&
    request=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJmODU1NWNlYi1jNjVjLTQwMjUtOTM3OC1iNjY3MmI2MTQ5YWYiLCJhdWQiOiJodHRwczovL3BpZC1wcm92aWRlci5leGFtcGxlLm9yZyIsImlhdCI6MTcxNTg0MjU2MCwiZXhwIjoxNzE1ODQyODYwLCJyZXNwb25zZV90eXBlIjoiY29kZSIsInJlc3BvbnNlX21vZGUiOiJmb3JtX3Bvc3Quand0IiwiY2xpZW50X2lkIjoiNDdiOTgyMzY5NzkxZDA4MDAzYTcyODNmMDU5Y2IwZDEiLCJpc3MiOiI0N2I5ODIzNjk3OTFkMDgwMDNhNzI4M2YwNTljYjBkMSIsInN0YXRlIjoiZnlaaU9MOUxmMkNlS3VOVDJKenhpTFJEaW5rMHVQY2QiLCJjb2RlX2NoYWxsZW5nZSI6IkU5TWVsaG9hMk93dkZyRU1USmd1Q0hhb2VLMXQ4VVJXYnVHSlNzdHctY00iLCJjb2RlX2NoYWxsZW5nZV9tZXRob2QiOiJTMjU2Iiwic2NvcGUiOiJwaWQiLCJhdXRob3JpemF0aW9uX2RldGFpbHMiOlt7InR5cGUiOiJvcGVuaWRfY3JlZGVudGlhbCIsImNyZWRlbnRpYWxfY29uZmlndXJhdGlvbl9pZCI6ImRjX3NkX2p3dF9waWQifSx7InR5cGUiOiJpdF9sMitkb2N1bWVudF9wcm9vZiIsIm11bHRpX3N0ZXBfbWV0aG9kIjoibXJ0ZCtpYXMiLCJpZHBoaW50aW5nIjoiaHR0cHM6Ly9pZHAuZXhhbXBsZS5vcmciLCJtdWx0aV9zdGVwX3JlZGlyZWN0X3VyaSI6Imh0dHBzOi8vc3RhcnQud2FsbGV0LmV4YW1wbGUub3JnL2NoYWxsZW5nZSJ9XSwicmVkaXJlY3RfdXJpIjoiaHR0cHM6Ly9zdGFydC53YWxsZXQuZXhhbXBsZS5vcmcifQ.AuthRequestSign456_NoKidJWTSignature-abc123def456ghi789jkl012mno345pqr678stu901vwx234yz567

Quando l'oggetto ``it_l2+document_proof`` non è presente nell'array authorization_details, il Provider EAA DEVE autenticare l'Utente con CIEid LoA High.
La Risposta PAR e la Richiesta di Autorizzazione sono le stesse delle Specifiche IT-Wallet.

Fase 2: Autenticazione Primaria
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Dopo l'elaborazione con successo del PAR, il Server di Autorizzazione reindirizza l'User Agent al Provider di Identità LoA3 configurato per l'autenticazione primaria. L'Utente completa il flusso di autenticazione LoA3 (SPID o CIEid Substantial) e il Server di Autorizzazione correla l'identità autenticata con la sessione OAuth attiva.

Il Server di Autorizzazione EAA DEVE assicurare che il parametro ``mrtd_auth_session`` sia mantenuto durante questa fase per la correlazione appropriata di sessione con gli step di autenticazione successivi.

.. note::
  Nel caso in cui l'Utente dovesse eseguire un'autenticazione LoA High, la successiva fase 3 DEVE essere saltata.

Fase 3: Flusso di Validazione MRTD PoP
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Dopo l'autenticazione primaria con successo, il Server di Autorizzazione inizia il flusso di proof of possession del documento elettronico fornendo all'Istanza del Wallet i parametri necessari per la validazione MRTD.

JWT di Prova MRTD
"""""""""""""""""

Il Server di Autorizzazione DEVE fornire un JWT firmato contenente i requisiti di challenge per la validazione del documento. La struttura JWT è definita come segue:

.. _table_eID_MRTD_Proof_JWT_Header:
.. list-table:: Header JWT di Prova MRTD
   :widths: 20 15 65
   :header-rows: 1

   * - **Parametro**
     - **Tipo**
     - **Descrizione**
   * - **alg**
     - string
     - OBBLIGATORIO. Algoritmo di firma.
   * - **typ**
     - string
     - OBBLIGATORIO. DEVE essere ``mrtd-ias+jwt``.
   * - **kid**
     - string
     - OBBLIGATORIO. Identificatore della chiave del Provider EAA che DEVE essere utilizzata per verificare la firma di questo JWT.

.. _table_eID_MRTD_Proof_JWT_Payload:
.. list-table:: Payload JWT di Prova MRTD
   :widths: 20 15 65
   :header-rows: 1

   * - **Parametro**
     - **Tipo**
     - **Descrizione**
   * - **iss**
     - string
     - OBBLIGATORIO. Identificatore Provider EAA.
   * - **aud**
     - string
     - OBBLIGATORIO. Identificatore Istanza del Wallet.
   * - **iat**
     - integer
     - OBBLIGATORIO. Tempo di emissione (Unix timestamp).
   * - **exp**
     - integer
     - OBBLIGATORIO. Tempo di scadenza (Unix timestamp).
   * - **status**
     - string
     - OBBLIGATORIO. Stato del challenge. DEVE essere ``require_interaction``.
   * - **type**
     - string
     - OBBLIGATORIO. Tipo di interazione richiesta. DEVE essere impostato a ``mrtd+ias``.
   * - **mrtd_auth_session**
     - string
     - OBBLIGATORIO. Identificatore di sessione.
   * - **state**
     - string
     - OBBLIGATORIO. DEVE essere lo stesso valore del Request Object iniziale.
   * - **mrtd_pop_jwt_nonce**
     - string
     - OBBLIGATORIO. Valore nonce per protezione replay. DEVE essere ottenuto dal Servizio MRTD PoP che DEVE avere controllo diretto su questo valore.
   * - **htu**
     - string
     - OBBLIGATORIO. URI HTTP dell'endpoint di inizializzazione MRTD PoP.
   * - **htm**
     - string
     - OBBLIGATORIO. Metodo HTTP per la richiesta di inizializzazione MRTD PoP. DEVE essere ``POST``.

Un esempio non normativo è riportato di seguito:

.. code-block:: http

    HTTP/1.1 302 Found
    Location: https://start.wallet.example.org/challenge?challenge_info=eyJhbGciOiJFUzI1NiIsInR5cCI6Im1ydGQtaWFzK2p3dCIsImtpZCI6ImQ0ZjhlMDJlZWJhMDdhNTM3MmUxOGVjYzU4NzA5ZDA2In0.eyJpc3MiOiJodHRwczovL3BpZC1wcm92aWRlci5leGFtcGxlLm9yZyIsImF1ZCI6IjQ3Yjk4MjM2OTc5MWQwODAwM2E3MjgzZjA1OWNiMGQxIiwiaWF0IjoxNzUzNTU1MzU4LCJleHAiOjE3NTM1NTU2NTgsInN0YXR1cyI6InJlcXVpcmVfaW50ZXJhY3Rpb24iLCJ0eXBlIjoibXJ0ZCtpYXMiLCJtcnRkX2F1dGhfc2Vzc2lvbiI6Ind4cm9WckJZMk1DcTRkRE5HWEFDUyIsInN0YXRlIjoiZnlaaU9MOUxmMkNlS3VOVDJKenhpTFJEaW5rMHVQY2QiLCJtcnRkX3BvcF9qd3Rfbm9uY2UiOiJub25jZTEiLCJodHUiOiJodHRwczovL2Vkb2MtcHJvb2YvaW5pdCIsImh0bSI6IlBPU1QifQ.i6p_FN7qNNawyL4KnOV1r8FrNVjzd-7Ve1wEGASHNnlXwuJ1f216v0Ml_KpVrq9yXkmOo_M2xZwih2SlHVfrzkuG3Pn7LWRL7dsyCtqEY2e58rFHjCa2miBnnKr0NU4wcBMMYe2_qKCOkA7SOa7usNTBluBLMQ28GfiMbr3tcpfpM4rD0POKQcfijvNkNbh-VdOxM8GdHb6IQO_xfpsaSzd8cc0k5yIYCWjDTeINVKebIz4m9Rm2JStvRrWUq8OCqkv-8dTJH9q-JXx0PzJC998RMwe6tqSL-kkE3dZLWwCJdP8Z7bITtowU49rEe-AkrGxVma4ANPq317umEfUwmw

Il server di autorizzazione DEVE:

- Generare un identificativo univoco della challenge con entropia sufficiente (minimo 128 bit) per la sicurezza crittografica.
- Creare un MRTD Proof JWT con header (``alg``, ``typ``, ``kid``) e parametri di payload appropriati (come definiti nella tabella sopra).
- Firmare MRTD proof JWT utilizzando la sua chiave privata con l'algoritmo crittografico scelto. Vedere la sezione :ref:`algorithms:Algoritmi Crittografici`.
- Generare una URL di reindirizzamento, che punta ad una universal link dell'istanza del wallet.
- Impostare il timeout di reindirizzamento per evitare attese indefinite e gestire gli scenari di timeout.
- Richiedere opzionalmente le informazioni MRZ direttamente al Registro Nazionale CIE utilizzando il codice identificativo fiscale dell'utente autenticato.
- Mantenere la correlazione di sessione tra il risultato LoA3 e la verifica di verifica del documento.

L'Istanza del Wallet DEVE:

- Validare la firma JWT utilizzando la chiave pubblica del Provider EAA ottenuta tramite valutazione di fiducia.
- Verificare che il claim ``aud`` corrisponda al suo ``client_id``.
- Verificare che i claim ``iat`` ed ``exp`` indichino che il token abbia una data di emissione corretta e non sia scaduto.
- Verificare che il campo ``status`` sia impostato a "require_interaction".
- Verificare che il tipo di autenticazione corrisponda al valore atteso ``mrtd+ias``.
- Estrarre HTTP target URI (``htu``) e metodo (``htm``) per lo step successivo.
- Gestire errori di validazione JWT e di rete, e fornire feedback utente con meccanismi di retry appropriati.
- Estrarre i parametri di correlazione (``mrtd_auth_session``, ``state``, ``mrtd_pop_jwt_nonce``) per le richieste successive.

Richiesta MRTD PoP
""""""""""""""""""

L'Istanza del Wallet DEVE inviare una Richiesta HTTP POST all'endpoint di inizializzazione del Servizio MRTD PoP con ``application/json`` come content type, includendo Wallet Attestation e Wallet Attestation JWT PoP nell'header secondo `OAUTH-ATTESTATION-CLIENT-AUTH`_. Il payload della Richiesta contiene i seguenti parametri:

.. _table_eID_MRTD_PoP_Request:
.. list-table:: Parametri Richiesta MRTD PoP
   :widths: 20 15 65
   :header-rows: 1

   * - **Parametro**
     - **Tipo**
     - **Descrizione**
   * - **mrtd_auth_session**
     - string
     - OBBLIGATORIO. Identificatore di sessione per binding di sessione.
   * - **mrtd_pop_jwt_nonce**
     - string
     - OBBLIGATORIO. Valore nonce ottenuto dal JWT di Prova MRTD.

Di seguito un esempio non normativo di una Richiesta MRTD PoP:

.. code-block:: http

    POST /edoc-proof/init HTTP/1.1
    Host: eaa-provider.example.org
    Content-Type: application/json
    OAuth-Client-Attestation: eyJhbGciOiJFUzI1NiIsImtp…
    OAuth-Client-Attestation-PoP: eyJhbGciOiJFUz…

    {
      "mrtd_auth_session": "wxroVrBY2MCq4dDNGXACS",
      "mrtd_pop_jwt_nonce": "f42cccb7f1c8269f9d4aeefe339c6b13"
    }

**L'Istanza del Wallet DEVE:**

- Validare la firma JWT di Prova MRTD utilizzando la chiave pubblica del Provider EAA.
- Verificare che il claim JWT ``aud`` corrisponda al suo ``client_id``.
- Assicurare che il claim JWT ``exp`` indichi che il token non è scaduto.
- Estrarre i valori ``mrtd_auth_session`` e ``mrtd_pop_jwt_nonce`` per correlazione.
- Includere Wallet Attestation valida secondo `OAUTH-ATTESTATION-CLIENT-AUTH`_.
- Gestire errori di rete e implementare meccanismi di retry appropriati.

**Il Servizio MRTD PoP DEVE:**

- Validare la Wallet Attestation secondo `OAUTH-ATTESTATION-CLIENT-AUTH`_.
- Verificare che il parametro ``mrtd_auth_session`` corrisponda a una sessione attiva.
- Validare che il parametro ``mrtd_pop_jwt_nonce`` corrisponda a quello emesso nello step precedente.

Il Servizio MRTD PoP PUÒ richiedere le informazioni MRZ (numero documento, data di nascita, data di scadenza, cittadinanza e genere) direttamente al Registro Nazionale CIE utilizzando il codice fiscale dell'Utente autenticato. In questo caso, il Servizio MRTD PoP è in grado di verificare se l'Utente autenticato possiede una CIE valida e se non è il caso, DEVE inviare una Risposta di Errore HTTP con codice di errore HTTP ``access_denied``.

Risposta MRTD PoP
"""""""""""""""""

Se la Richiesta HTTP è elaborata con successo, il Servizio MRTD PoP DEVE inviare una Risposta HTTP con codice *202 Accepted* e ``application/jwt`` come content type. La struttura JWT è definita come segue:

.. _table_eID_MRTD_PoP_Response_Header:
.. list-table:: MRTD PoP Response Parameters
   :widths: 20 15 65
   :header-rows: 1

   * - **Parameter**
     - **Type**
     - **Description**
   * - **alg**
     - string
     - OBBLIGATORIO. Algoritmo di firma.
   * - **typ**
     - string
     - OBBLIGATORIO. DEVE essere ``mrtd-ias-pop+jwt``.
   * - **kid**
     - string
     - OBBLIGATORIO. Identificatore della chiave del Provider EAA che DEVE essere utilizzata per verificare la firma di questo JWT.

.. _table_eID_MRTD_PoP_Response_Payload:
.. list-table:: Parametri Risposta MRTD PoP
   :widths: 20 15 65
   :header-rows: 1

   * - **Parametro**
     - **Tipo**
     - **Descrizione**
   * - **iss**
     - string
     - OBBLIGATORIO. Identificatore Provider EAA.
   * - **aud**
     - string
     - OBBLIGATORIO. Identificatore Istanza del Wallet.
   * - **iat**
     - integer
     - OBBLIGATORIO. Tempo di emissione (Unix timestamp).
   * - **exp**
     - integer
     - OBBLIGATORIO. Tempo di scadenza (Unix timestamp).
   * - **challenge**
     - string
     - OBBLIGATORIO. Dati di challenge per validazione crittografica del documento. DOVREBBE essere il valore hash SHA-256 di un valore casuale con ``mrtd_auth_session`` e timestamp per binding crittografico.
   * - **mrtd_pop_nonce**
     - string
     - OBBLIGATORIO. Valore nonce unico per lo step successivo, prevenendo attacchi replay.
   * - **mrz**
     - string
     - OPZIONALE. Informazioni Machine Readable Zone inclusi numero documento, data di nascita, data di scadenza, cittadinanza e genere.
   * - **htu**
     - string
     - OBBLIGATORIO. URI HTTP dell'endpoint di validazione MRTD PoP.
   * - **htm**
     - string
     - OBBLIGATORIO. Metodo HTTP per la richiesta di validazione MRTD PoP. DEVE essere ``POST``.

Di seguito un esempio non normativo di una Risposta MRTD PoP:

.. code-block:: http

    HTTP/1.1 202 Accepted
    Content-Type: application/jwt; charset=utf-8

    eyJhbGciOiJFUzI1NiIsInR5cCI6Im1ydGQtaWFzLXBvcCtqd3QiLCJraWQiOiJiM2YxYTZjMmU5ZDU0YThmOWMzZTdkMWEyZjRiNmM3OCJ9.eyJpc3MiOiJodHRwczovL3BpZC1wcm92aWRlci5leGFtcGxlLm9yZyIsImF1ZCI6Imh0dHBzOi8vd2FsbGV0LmV4YW1wbGUub3JnL2luc3RhbmNlLzEyMzQ1IiwiaWF0IjoxNzUzNTU1ODAwLCJleHAiOjE3NTM1NTYwMDAsIm1ydGRfcG9wX25vbmNlIjoiOWYyYzRhN2UzYjFkOGM5YTZlNWY0YjJhMWMzZDdlOGYiLCJtcnoiOiIuLi4iLCJjaGFsbGVuZ2UiOiIuLi4iLCJodHUiOiIuLi4iLCJodG0iOiIuLi4ifQ.signature

Header JWT decodificato:

.. code-block:: json

    {
      "alg":"ES256",
      "typ":"mrtd-ias-pop+jwt",
      "kid":"b3f1a6c2e9d54a8f9c3e7d1a2f4b6c78"
    }

Body JWT decodificato:

.. code-block:: json

    {
      "iss":"https://eaa-provider.example.org",
      "aud":"https://wallet.example.org/instance/12345",
      "iat": 1753555800,
      "exp": 1753556000,
      "mrtd_pop_nonce":"9f2c4a7e3b1d8c9a6e5f4b2a1c3d7e8f",
      "mrz":"...",
      "challenge":"...",
      "htu":"...",
      "htm":"..."
    }

**Il Servizio MRTD PoP DEVE:**

- Generare dati di challenge crittograficamente sicuri per validazione ``MRTD+IAS`` con entropia sufficiente (da utilizzare nel protocollo Anti-Cloning Internal Authentication dall'Istanza del Wallet), memorizzandoli con tempo di scadenza appropriato. Inoltre, il Servizio MRTD PoP DEVE assicurare unicità del challenge per prevenire attacchi di riutilizzo.
- Creare un nuovo ``mrtd_pop_nonce`` unico per lo step successivo per prevenire attacchi replay.
- Validare continuità di sessione assicurando che il parametro ``mrtd_auth_session`` corrisponda a una sessione attiva.
- Restituire stato HTTP *202 Accepted* per indicare iniziazione di elaborazione asincrona.
- Includere header Content-Type appropriato (``application/jwt; charset=utf-8``).
- Gestire errori di servizio e restituire risposte di errore appropriate.
- Estrarre e validare informazioni MRZ se fornite da servizi di registro esterni.

**L'Istanza del Wallet DEVE:**

- Validare stato risposta HTTP (*202 Accepted*) e content type.
- Analizzare risposta JSON e validare parametri richiesti (``challenge``, ``mrtd_pop_nonce``).
- Estrarre dati di challenge per validazione crittografica del documento.
- Memorizzare nuovo valore ``mrtd_pop_nonce`` in modo sicuro per richieste di validazione successive.
- Validare informazioni MRZ opzionali se presenti nella risposta.
- Estrarre HTTP target URI (``htu``) e metodo (``htm``) per lo step successivo.
- Gestire errori, fornendo feedback utente relativo.
- Memorizzare dati di challenge temporaneamente in memoria sicura (non storage persistente).
- Preparare sessione di lettura NFC.

L'Istanza del Wallet esegue lettura e validazione di documento elettronico basata su NFC, poi invia l'evidenza al Provider EAA per verifica finale e correlazione di identità con il risultato di autenticazione LoA3.

Richiesta di Validazione MRTD PoP
"""""""""""""""""""""""""""""""""

Dopo che tutte le evidenze sono state raccolte tramite interazione NFC con il Documento Elettronico, l'Istanza del Wallet DEVE inviare tutti i dati al Server di Autorizzazione del Provider EAA per la validazione finale e controlli incrociati di identità. L'Istanza del Wallet DEVE inviare una Richiesta HTTP POST con ``application/json`` come content type, includendo Wallet Attestation e Wallet Attestation JWT PoP nell'header secondo `OAUTH-ATTESTATION-CLIENT-AUTH`_. Il payload della Richiesta contiene i seguenti parametri.

.. _table_eID_MRTD_PoP_Validation_Request:
.. list-table:: Parametri Richiesta di Validazione MRTD PoP
   :widths: 20 15 65
   :header-rows: 1

   * - **Parametro**
     - **Tipo**
     - **Descrizione**
   * - **mrtd_validation_jwt**
     - string
     - OBBLIGATORIO. JWT contenente evidenza del documento, proof crittografici, Data Groups (DGs), e risultati di validazione.
   * - **mrtd_auth_session**
     - string
     - OBBLIGATORIO. Identificatore di sessione per binding di sessione.
   * - **mrtd_pop_nonce**
     - string
     - OBBLIGATORIO. DEVE corrispondere al valore ottenuto dalla Risposta MRTD PoP.

Struttura JWT di Validazione
""""""""""""""""""""""""""""

La struttura del JWT di Validazione (``mrtd_validation_jwt``) è data nella seguente tabella.

.. _table_eID_MRTD_Validation_JWT_Header:
.. list-table:: Parametri Header JWT di Validazione
   :widths: 20 15 65
   :header-rows: 1

   * - **Parametro Header**
     - **Tipo**
     - **Descrizione**
   * - **alg**
     - string
     - OBBLIGATORIO. Algoritmo di firma.
   * - **typ**
     - string
     - OBBLIGATORIO. DEVE essere ``mrtd-ias+jwt``.
   * - **kid**
     - string
     - OBBLIGATORIO. Identificatore della chiave dell'Istanza del Wallet che DEVE essere utilizzata per verificare la firma di questo JWT.

.. _table_eID_MRTD_Validation_JWT_Payload:
.. list-table:: Parametri Payload JWT di Validazione
   :widths: 20 15 65
   :header-rows: 1

   * - **Parametro Payload**
     - **Tipo**
     - **Descrizione**
   * - **iss**
     - string
     - OBBLIGATORIO. Identificatore Istanza del Wallet.
   * - **aud**
     - string
     - OBBLIGATORIO. Identificatore Provider EAA.
   * - **iat**
     - integer
     - OBBLIGATORIO. Tempo di emissione (Unix timestamp).
   * - **exp**
     - integer
     - OBBLIGATORIO. Tempo di scadenza (Unix timestamp).
   * - **document_type**
     - string
     - OBBLIGATORIO. Tipo di documento validato. DEVE essere impostato a ``cie``.
   * - **mrtd**
     - JSON Object
     - OBBLIGATORIO. Dati di validazione MRTD contenenti Data Groups e SOD.
   * - **ias**
     - JSON Object
     - OBBLIGATORIO. Dati di validazione IAS contenenti Anti-Cloning Public Key, e SOD.

Struttura Oggetto MRTD
""""""""""""""""""""""

L'oggetto ``mrtd`` contiene i seguenti campi:

.. _table_eID_MRTD_Object:
.. list-table:: Struttura Oggetto MRTD
   :widths: 20 15 65
   :header-rows: 1

   * - **Campo**
     - **Tipo**
     - **Descrizione**
   * - **dg1**
     - string
     - OBBLIGATORIO. Data Group 1 codificato Base64 (informazioni MRZ: numero documento, data di nascita, data di scadenza, cittadinanza e genere).
   * - **dg11**
     - string
     - OBBLIGATORIO. Data Group 11 codificato Base64 (dati personali aggiuntivi).
   * - **sod_mrtd**
     - string
     - OBBLIGATORIO. Security Object of Document per MRTD codificato Base64.

Struttura Oggetto IAS
"""""""""""""""""""""

L'oggetto ``ias`` contiene i seguenti campi:

.. _table_eID_MRTD_IAS_Object:
.. list-table:: Struttura Oggetto IAS
   :widths: 20 15 65
   :header-rows: 1

   * - **Campo**
     - **Tipo**
     - **Descrizione**
   * - **ias_pk**
     - string
     - OBBLIGATORIO. Chiave pubblica IAS codificata Base64 in formato DER.
   * - **sod_ias**
     - string
     - OBBLIGATORIO. Security Object of Document per IAS codificato Base64.
   * - **challenge_signed**
     - string
     - OBBLIGATORIO. Risposta di challenge firmata codificata Base64.

Di seguito un esempio non normativo di una Richiesta di Validazione MRTD PoP:

.. code-block:: http

    POST /edoc-proof/verify HTTP/1.1
    Host: eaa-provider.example.org
    Content-Type: application/json
    OAuth-Client-Attestation: eyJhbGciOiJFUzI1NiIsImtp…
    OAuth-Client-Attestation-PoP: eyJhbGciOiJFUz…

    {
      "mrtd_validation_jwt":"eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL3dhbGxldC5leGFtcGxlLm9yZy9pbnN0YW5jZS8xMjM0NSIsImF1ZCI6Imh0dHBzOi8vcGlkLXByb3ZpZGVyLmV4YW1wbGUub3JnIiwiaWF0IjoxNzUzNTU1NDAwLCJleHAiOjE3NTM1NTU3MDAsImRvY3VtZW50X3R5cGUiOiJjaWUiLCJtcnRkIjp7ImRnMSI6IlVEeEpWRUU4VTAxSlZFZzhQRXBQU0U0OFBFcFBTRTRnVTAxSlZFZzhQREU1T0RBME1UVThUVDxQTnpjM056SXpNUT09IiwiZGcxMSI6Ik1USXpORFUyTnpnNVFVSkRSRVZHUjBoSlNrdE1UVTVQVUVGT1IxSlRWRlZXV0ZsYVUwRkVSVVU9Iiwic29kX21ydGQiOiJNSUlGempDQ0JMYWdBd0lCQWdJSVFPWTJLSkdGVFVJd0RRWUpLb1pJaHZjTkFRRUxCUUF3WHpFTE1Baz0ifSwiaWFzIjp7Imlhc19wayI6Ik1JSUJJakFOQmdrcWhraUc5dzBCQVFFRkFBT0NBUThBTUlJQkNnS0NBUUVBejEyMzQ1Njc4OTA9Iiwic29kX2lhcyI6Ik1JSUZhRENDQkZDZ0F3SUJBZ0lKQUwyS0pHRlRVSXdEUVlKS29aSWh2Y05BUUVMQlFBd1h6RUxNQT09IiwiY2hhbGxlbmdlX3NpZ25lZCI6ImExYjJjM2Q0ZTVmNjc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MGFiY2RlZjEyMzQ1Njc4OTBhYmNkZWY9PSJ9fQ.xyz456abc789def012ghi345jkl678mno901pqr234stu567vwx890yz123",
      "mrtd_auth_session":"wxroVrBY2MCq4dDNGXACS",
      "mrtd_pop_nonce":"9f2c4a7e3b1d8c9a6e5f4b2a1c3d7e8f"
    }

**L'Istanza del Wallet DEVE:**

- Eseguire lettura documento NFC conforme `ICAO 9303`_ (PACE, ecc.).
- Validare firme crittografiche del documento e catene di certificati.
- Estrarre attributi di identità (DG1 e DG11), Anti-Cloning Public Key dai data groups del documento, e SODs (dalle Applicazioni MRTD e IAS).
- Eseguire l'Anti-Cloning Internal Authentication.
- Generare evidenza di validazione nel JWT.
- Autenticare utilizzando una Wallet Instance Attestation valida.
- Includere esatti ``mrtd_auth_session`` e ``mrtd_pop_nonce`` dalla risposta init.
- Firmare il ``mrtd_validation_jwt`` con la sua chiave privata.
- Gestire errori di lettura documento e fornire feedback appropriato.

**Il Servizio MRTD PoP DEVE:**

- Validare Wallet Instance Attestation secondo le specifiche IT-Wallet.
- Verificare firma OAuth-Client-Attestation-PoP.
- Validare che il parametro ``mrtd_auth_session`` corrisponda a una sessione attiva.
- Verificare che il ``mrtd_pop_nonce`` corrisponda al valore inviato nella risposta precedente.
- Analizzare e validare la firma (utilizzando la chiave pubblica dell'istanza del Wallet) e la struttura del ``mrtd_validation_jwt``.
- Estrarre e verificare le evidence del documento dal ``mrtd_validation_jwt``.
- Validare autenticità del documento utilizzando standard `ICAO 9303`_.
- Verificare risposta challenge Anti-Cloning.
- Convalida delle prove crittografiche e delle catene di certificati del documento.
- Eseguire la correlazione dell'identità tra i dati del documento e il risultato dell'autenticazione LoA3.
- Controllare validità del documento (stato non di revoca).
- Verificare il binding tra le applicazioni IAS e MRTD controllando che il NUN estratto da DG1 sia presente (come valore hash) nell'IAS SOD, e che il DG1 stesso sia presente (come valore hash) nell'MRTD SOD. Questa doppia verifica assicura che entrambe le applicazioni risiedano sullo stesso chip fisico.

Risposta di Validazione MRTD PoP
""""""""""""""""""""""""""""""""

Dopo completamento con successo di tutti i controlli da parte del Servizio MRTD PoP, DEVE inviare all'Istanza del Wallet una Risposta HTTP con codice *202 Accepted* includendo i seguenti parametri:

.. _table_eID_MRTD_PoP_Validation_Response:
.. list-table:: Parametri Risposta di Validazione MRTD PoP
   :widths: 20 15 65
   :header-rows: 1

   * - **Parametro**
     - **Tipo**
     - **Descrizione**
   * - **status**
     - string
     - OBBLIGATORIO. DEVE essere valorizzato con `require_interaction`.
   * - **type**
     - string
     - OBBLIGATORIO. DEVE essere valorizzato con `redirect_to_web`.
   * - **mrtd_val_pop_nonce**
     - string
     - OBBLIGATORIO. Nonce di conferma finale per callback basato su browser.
   * - **redirect_uri**
     - string
     - OBBLIGATORIO. URI di redirect del browser per il completamento del flusso autorizzativo.

Di seguito un esempio non normativo di una Risposta di Validazione MRTD PoP:

.. code-block:: http

    HTTP/1.1 202 Accepted
    Content-Type: application/json; charset=utf-8

    {
      "status": "require_interaction",
 	    "type": "redirect_to_web",
      "mrtd_val_pop_nonce": "0f2bff024317345b6927ce17e776361d",
      "redirect_uri":"https://eaa-provider.example.org/cb"
    }

**Il servizio MRTD PoP DEVE:**

- Generare un nuovo nonce ``mrtd_val_pop_nonce`` per la conferma finale basata su browser.
- Restituire lo stato HTTP 202 per indicare il completamento dell'elaborazione asincrona.

**L'istanza Wallet DEVE:**

- Validare la response.
- Estrarre i parametri ``mrtd_val_pop_nonce`` e ``redirect_uri`` per preparare la successiva richiesta GET basata su browser.

Conferma Finale Basata su Browser
"""""""""""""""""""""""""""""""""

Dopo validazione MRTD PoP con successo, l'Istanza del Wallet DEVE reindirizzare l'User Agent al ``challenge_redirect_uri`` specificato nell'Authorization Details Object iniziale, includendo il ``mrtd_val_pop_nonce`` e ``mrtd_auth_session`` come parametri query:

.. code-block:: text

    https://eaa-provider.example.org/l2plus-callback?mrtd_val_pop_nonce=0f2bff024317345b6927ce17e776361d_signed&mrtd_auth_session=wxroVrBY2MCq4dDNGXACS

L'Istanza del Wallet DEVE validare che il ``mrtd_val_pop_nonce`` corrisponda al valore ricevuto dalla Risposta di Validazione MRTD PoP.

**Il server di autorizzazione DEVE:**

- Verificare che ``mrtd_val_pop_nonce`` corrisponda al valore inviato nella verification response e che sia firmato utilizzando la chiave privata dell'istanza Wallet.
- Verificare che il parametro ``mrtd_auth_session`` corrisponda a una sessione attiva.
- Verificare che tutti gli step di autenticazione (LoA3 + MRTD PoP) siano stati completati correttamente (inclusa la correlazione di identità recuparata tramite autenticazione LoA3 e quella presente nel documento).
- Generare l'authorization code finale.

Fase 4: Risposta di Autorizzazione OAuth
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Dopo completamento con successo di tutti gli step di autenticazione e correlazione di identità, il Server di Autorizzazione DEVE emettere la Risposta di Autorizzazione OAuth finale. Se tutti i controlli di validazione sono stati superati, il Server di Autorizzazione DEVE reindirizzare l'User Agent nuovamente all'Istanza del Wallet con una Risposta di Autorizzazione OAuth includendo il codice di autorizzazione come definito negli step 6-7 di :ref:`credential-issuance-low-level:Issuance Flow`, e nella Sezione :ref:`credential-issuance-endpoint:Pushed Authorization Request (PAR) Response`. Il Server di Autorizzazione DEVE utilizzare il ``redirect_uri`` incluso nel Request Object iniziale dall'Istanza del Wallet.

Gestione Errori
---------------

La gestione errori DEVE seguire le stesse regole come definite nella Sezione :ref:`credential-issuer-endpoint:Endpoint di Rilascio degli Attestati Elettronici`, riguardo ai formati e i riferimenti standard correlati.

Durante il flusso di Validazione MRTD PoP, quando si verificano errori recuperabili, il Servizio MRTD PoP PUÒ generare e restituire un nonce fresco per abilitare l'Utente a tentare nuovamente mantenendo sicurezza di sessione e prevenendo attacchi replay.

In aggiunta ai codici di errore già definiti nella Sezione :ref:`credential-issuer-endpoint:Endpoint di Rilascio degli Attestati Elettronici`, almeno i seguenti codici di errore DEVONO essere supportati.

Errori Risposta MRTD PoP
^^^^^^^^^^^^^^^^^^^^^^^^

.. _table_eID_MRTD_PoP_Response_Errors:
.. list-table:: Codici Errore Risposta MRTD PoP
   :widths: 30 70
   :header-rows: 1

   * - **Codice Errore**
     - **Descrizione**
   * - **invalid_client**
     - Autenticazione Istanza del Wallet fallita.
   * - **invalid_request**
     - L'HTTP request non è valida o è malformata (struttura non corretta, dati mancanti, ecc.) oppure i parametri di sessione richiesti sono mancanti o non validi.
   * - **access_denied**
     - L'utente non è idoneo per l'autenticazione eID Substantial con il meccanismo di verifica MRTD (ad esempio, CIE non trovata nel registro CIE)
   * - **temporarily_unavailable**
     - Servizio di validazione documento o servizio Registro CIE è temporaneamente non disponibile.

Errori Risposta di Validazione MRTD PoP
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _table_eID_MRTD_PoP_Validation_Response_Errors:
.. list-table:: Codici Errore Risposta di Validazione MRTD PoP
   :widths: 30 70
   :header-rows: 1

   * - **Codice Errore**
     - **Descrizione**
   * - **invalid_client**
     - Autenticazione Istanza del Wallet fallita.
   * - **invalid_request**
     - Richiesta di Validazione HTTP o JWT di Validazione è invalida o malformata (dovuto a struttura malformata, dati mancanti, fallimento firma, timeout richiesta, ecc.).
   * - **access_denied**
     - Autenticazione utente o validazione documento fallita.
   * - **invalid_document**
     - La convalida crittografica del documento non è riuscita (convalida SOD, verifica binding IAS/MRTD, stato di revoca, ecc.).
   * - **id_matching_failed**
     - La corrispondenza tra l'identità ottenuta durante l'autenticazione primaria (eID LoA3) e quella ottenuta dalla PoP del Documento Elettronico non è riuscita.
   * - **temporarily_unavailable**
     - Il servizio di validazione dei documenti o il servizio di registro CIE sono temporaneamente non disponibili.

Mappatura Codici di Stato HTTP
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Le risposte di errore DEVONO utilizzare codici di stato HTTP appropriati:

- **400 Bad Request**: Per errori ``invalid_request``.
- **401 Unauthorized**: Per errori ``invalid_client``.
- **403 Forbidden**: Per errori ``access_denied``.
- **422 Unprocessable Entity**: Per errori ``invalid_document`` o ``id_matching_failed``.
- **503 Service Unavailable**: Per errori ``temporarily_unavailable``.

Considerazioni di Sicurezza
---------------------------

Gestione Sicura di Sessione
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Il parametro ``mrtd_auth_session`` serve come meccanismo di correlazione primario tra gli step di autenticazione. Le implementazioni DEVONO assicurare che questo identificatore abbia entropia sufficiente (minimo 128 bit) e sia crittograficamente sicuro. L'identificatore di sessione DEVE essere validato a ogni step per prevenire attacchi di session fixation.

Ogni step di autenticazione DEVE essere crittograficamente legato alla sessione OAuth tramite validazione JWT firmata per prevenire attacchi di session fixation, session confusion, e sostituzione di identità. Il Server di Autorizzazione DEVE mantenere la correlazione tra l'identità LoA3 e il proof del documento all'interno di un singolo contesto di sessione.

In particolare, ogni fase di autenticazione DEVE convalidare la correlazione tra:

- Coerenza dell'identificativo di sessione in tutte le fasi del protocollo.
- Attributi di identità LoA3 associati al contesto della sessione.
- Correlazione delle prove documentali con l'identità autenticata.
- Validazione della sequenza temporale per prevenire attacchi fuori ordine.

Quando i componenti operano al di fuori dei confini del Provider EAA, DEVONO essere implementate le seguenti misure di sicurezza aggiuntive:

- Comunicazione sicura tra servizi (ad esempio, tramite pinning del certificato, TLS reciproco, ecc.).
- Crittografia e integrità dei dati sensibili della sessione e/o delle informazioni di identità personale (ad esempio, utilizzando token JWE/JWS).
- Lock distribuiti per gli aggiornamenti dello stato di sessione

.. _fig_eID_MRTD_Security_Controls:
.. plantuml:: plantuml/l2plus-security-controls.puml
    :width: 99%
    :alt: La figura illustra i Controlli di Sicurezza per Autenticazione eID Substantial con Verifica MRTD.
    :caption: `Controlli di Sicurezza per Autenticazione eID Substantial con Verifica MRTD. <https://www.plantuml.com/plantuml/svg/nLTzRzks4_vVd-9-ATfVuiP9dNHRPzH9LJil7jh4Y9mMsp8Oj7IskSgaHb9Eiay_tacMxAGkCcp004EmgNjvxdcEH_gTTSAuV9u6__-Vc-4S8KQJfoXKK-SkbGe3aJkjylaOJP1vMndBJ2W7MzSMpHO82zVhwvz5cgA3llAXLOni4gwRTFidlDmDnleEOEia365Wz48c5FBP1pcTkVTfZkjUP1NcRgQD_5CugHL4Q1ObY31QD_vuDUp1G0_OHfOmUeFBGHIWIi3dVGG9BZYgIE4Afz8wSyzE7_iNwwPBinlLJr0vwUvhyEJGxms28F3hAGBsU_11XuSCd8pZ0lbBC3ZN3a4kGsH6wubKKv0A-iFcaiKUzAtDYKWuJVLj45n3ymZ2DdmcB4w3Y9rS28VWuqFfTQDoIw4eUvIFIGWdHVeGnArqCs2YFg6Hat8v23gT3WncmYAqsd19JWzuly8_ShGEEfqWP3WHj64GNbKljW7YLA9o8vdiWYbMByU_O-nsF3eeKdFePfSDcw5ptgQ8BrIoyMMJH9MAopr7uKadSuhPQ71KiGfrbA0JCWLtdo5iIJTA3rucEixdX8qftseqWi0NqAGwgZ9iffL5s2wXZt8ZTm7lCcdGZgJQMTRTNjDg0qq4xkna2FjBQ7XSiTFPszjxiPA5VfFzkRQk3IX4CojxQm_ln3nBSK-RwQf61nwpaNDXxX_gs-G6e7twDUMfBrUxWzGqYdfIByWZyXjHB53vr7ulsbaGTGzfxx0DCtP4hTwc9Elngye3_nxU4hFNxGA7UBWDOk9PiMN1w8PuXI1F1xZAq64Rgd7mIQGouQ3SlL6vcyw7my5-Qwy5XwyEu5Jdt54VT96-3JFdCjlUt-TfkNVBUg_giH_FQ4rDyRZHc1kN5BtLULj_7_tqUNX4lRPQmkCAVbYfW7kCPrRRDtTLGabket6Z1fUHRojCTDpa9FjIILSLuqluTXlTg7zp7wwLnh0Vb_VzBaJTD_JuSQLGdRa00DY95A6PsmPVg3CI5-ZL-mMaccWpvzHaIoRGhFXvQ4B1Ww2CHnAlCbYr4r5OAN_WbG_Z63E7IKbCePxEHagh67UXKfcPsTPPSH2azpkSFn5E18587VGd1I0BIZiG2o5JCKuHd6Q-7XoHN4y8l4sMwfAfz12DWsvumHRBoT-lbp6r2B9AfiTEI8K920UHmmnQhIesUPxSEIDYnq1XOlIS70kgfaRdMNdq_eofFshWuhJhSpaabsfe47pUoPvgw9MJ50RKVE0_0sqjMalcVitfMATyRX6A9PHVdqqDelhj2BfGoH9cMLhFhK7OFI5nhb0aq3jhxTB3FwFBteZCELGNcdKicjrViuHWKzf-6ArchTA5D7PIhUW07UHZ_nw-u7qHaNmsv7wIspgCTIUcMZqwfM-KvLjEtNmR05n5OVFWrUitOELK2PSR945ygDgJfDuuLkh9-Cq9iw2hmlr_DcC0_jwKeOVlXy0_3_Zx8JzVhqoVzQb3XIq9u2PV42zqGoDGkLsIUgEMzmYw9IpAey9pZV6NdI1uC9vMfimhkFpob57P-ewHSYsj-bZOFDLg0Pyyu0mcqc3CDmzMWYUUhxYUUjmld8hwwXi6t4tlZRwrQ9fZOJ61KqdztDLg8isyscLq5LeUg9kwPZyU7tFqpkE48mA2oGjDbubHEMxu7aKAON63sdOpe_Ff3CO5eftrW_V9HrDzYtYzwIvSK5rV9rYLpTV2seCbu91TdR1M__0QSkojOvsK543D1_sGrdOumFF3yFd1gVzi8d-TgbqcgtzsFZoxEZcv28OpX0cDz5Wh9rME5aGSQvFG47DwmvyNzX0M4fpG2RNSrRMnpJ2k_eFK0hppt_9v-XS0>`_

Generazione Challenge Crittografico
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Il Servizio MRTD PoP DEVE generare challenge crittograficamente sicuri con entropia sufficiente (minimo 256 bits) per la validazione del documento. I valori di challenge DEVONO essere unici e NON DEVONO essere riutilizzati attraverso sessioni diverse (vincolata crittograficamente al contesto specifico della sessione OAuth) o tentativi di autenticazione. L'algoritmo di generazione challenge DOVREBBE incorporare l'identificatore ``mrtd_auth_session`` e timestamp per assicurare binding crittografico appropriato.

Gestione Ciclo di Vita Nonce
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Ogni step nel flusso di Autenticazione eID Substantial con Verifica MRTD DEVE utilizzare valori nonce unici per prevenire attacchi replay. I valori nonce DEVONO avere tempi di scadenza appropriati e DEVONO essere invalidati dopo uso con successo. Il Server di Autorizzazione EAA e il Servizio MRTD PoP DEVONO mantenere validazione nonce sincronizzata per assicurare integrità di sessione.

Inoltre, ogni nonce ha uno scopo di sicurezza specifico:
- ``mrtd_pop_jwt_nonce`` DEVE essere correlato con il JWT di prova MRTD.
- ``mrtd_pop_nonce`` DEVE:

 - Essere crittograficamente indipendente da ``mrtd_pop_jwt_nonce``.
 - Incorporare ``mrtd_pop_jwt_nonce`` come input per mantenere la catena di fiducia.
 - Utilizzare una diversa sorgente di entropia per prevenire attacchi di correlazione.

- ``mrtd_val_pop_nonce`` DEVE:

 - Essere firmato dalla chiave privata dell'istanza del wallet.
 - Includere la convalida del timestamp anti-replay.
 - Essere verificato rispetto all'intera catena di nonce per verificarne l'integrità.

Metadati del Provider EAA
^^^^^^^^^^^^^^^^^^^^^^^^^

In aggiunta ai valori ``trust_frameworks_supported`` definiti nella sezione :ref:`credential-issuer-metadata:Metadata per openid_credential_issuer`, i Metadati del Provider EAA per ``openid_credential_issuer`` DEVONO anche supportare il valore ``it_l2+document_proof`` indicante il protocollo di Autenticazione multi-step descritto in questa Specifica.

Controlli di Sicurezza
^^^^^^^^^^^^^^^^^^^^^^

I seguenti controlli di sicurezza DEVONO essere implementati nel protocollo:

.. _table_eID_MRTD_Security_Controls:
.. list-table:: Controlli di Sicurezza per Autenticazione eID Substantial con Verifica MRTD
   :widths: 10 60 30
   :header-rows: 1

   * - **#**
     - **Descrizione**
     - **Fase**
   * - **SC1**
     - I canali di comunicazione di rete sono protetti utilizzando TLS v1.2+ con cifrari sicuri.
     - Tutte
   * - **SC2**
     - L'Istanza del Wallet assicura l'autenticità del Provider EAA e del Provider di Identità eID tramite pinning del certificato leaf di ogni server.
     - Tutte
   * - **SC3**
     - Il Server di Autorizzazione EAA verifica che il Provider di Identità eID utilizzato nella fase *eID LoA3* sia accreditato.
     - Fase 2
   * - **SC4**
     - Il Server di Autorizzazione EAA verifica l'autenticità e integrità dei dati estratti dall'asserzione *eID LoA3*, controllando la firma digitale.
     - Fase 2
   * - **SC5**
     - Il valore challenge e tutti i valori nonce sono generati con protezioni per prevenire attacchi bruteforce o di indovinamento.
     - Fase 3
   * - **SC6**
     - Il Provider EAA verifica tutti i valori nonce per rilevare attacchi replay.
     - Fase 3
   * - **SC7**
     - L'Istanza del Wallet verifica che ``challenge_info`` sia firmato appropriatamente dal Server di Autorizzazione EAA. Inoltre, controlla che ``challenge_info`` contenga: un valore ``iss`` corrispondente al valore del Server di Autorizzazione EAA; un valore aud uguale al ``client_id`` dell'Istanza del Wallet; e un valore ``state`` uguale a quello nella richiesta PAR, per essere sicuri che la risposta sia legata alla richiesta iniziale fatta dall'Istanza del Wallet nello Step 2. Quindi le informazioni fornite come parte di ``challenge_info``, in particolare l'``htu`` che corrisponde all'url di redirect da seguire per il *MRTD PoP*, non sono manomesse.
     - Fase 3
   * - **SC8**
     - Il Provider EAA controlla che l'``mrtd_auth_session`` sia associata alla stessa Istanza del Wallet in tutte le richieste nella fase *MRTD PoP*. Quindi il Provider EAA può essere sicuro che l'Istanza del Wallet che esegue la fase *MRTD PoP*: sia fidata; sia sempre la stessa attraverso il protocollo; e abbia precedentemente iniziato l'emissione IT-Wallet ID (richiesta PAR). Questo può essere implementato richiedendo all'Istanza del Wallet di eseguire un proof of possession della sua chiave privata (es., all'interno di OAuth-Client-Attestation o firmando un valore nonce).
     - Fase 3
   * - **SC9**
     - Il Provider EAA controlla che l'``mrtd_auth_session`` non sia scaduta (timeout di validità tipicamente di 5 minuti), cioè che l'operazione sia stata conclusa entro una certa quantità di tempo.
     - Fase 3
   * - **SC10**
     - L'integrità e riservatezza del canale tra la *CIE fisica* e il *device_wallet fisico* è protetta con il protocollo PACE (tramite l'algoritmo e le funzioni di derivazione chiave supportate dalla carta).
     - Fase 3
   * - **SC11**
     - Il Servizio MRTD PoP verifica l'autenticità e integrità del ``mrtd_validation_jwt`` controllando che sia firmato con la chiave privata dell'Istanza del Wallet associata all'``mrtd_auth_session``.
     - Fase 3
   * - **SC12**
     - Il Servizio MRTD PoP verifica che challenge_signed contenuto in ``mrtd_validation_jwt`` corrisponda al challenge originale firmato con la chiave privata CIE AntiClone (``SDO.Servizi_Int_Kpriv``). Questo dimostra che l'Istanza del Wallet e la CIE hanno eseguito l'Internal Authentication (in linea con Sec. 5.2.3.5.1 in IAS ECC, ma con valore di casualità ``RND.IFD`` fornito dal Servizio MRTD PoP invece di generarlo nell'Istanza del Wallet).
     - Fase 3
   * - **SC13**
     - Il Servizio MRTD PoP verifica l'autenticità dei dati estratti dalla CIE controllando gli elementi SOD (sia IAS che MRTD) e le catene di certificati di firma correlate.
     - Fase 3
   * - **SC14**
     - Il Servizio MRTD PoP verifica l'integrità dei dati estratti dalla CIE controllando gli elementi SOD (sia IAS che MRTD) e gli hash correlati.
     - Fase 3
   * - **SC15**
     - Il Servizio MRTD PoP verifica il binding tra le applicazioni IAS e MRTD controllando che il NUN estratto da DG1 sia presente (come valore hash) nell'IAS SOD, e che il DG1 stesso sia presente (come valore hash) nell'MRTD SOD. Questa doppia verifica assicura che entrambe le applicazioni risiedano sullo stesso chip fisico.
     - Fase 3
   * - **SC16**
     - Il Servizio MRTD PoP verifica che l'identità dimostrata durante la fase eID LoA3 sia correlata con l'identità dimostrata durante la fase MRTD PoP.
     - Fase 3
   * - **SC17**
     - Il Servizio MRTD PoP verifica che la CIE utilizzata durante la fase MRTD PoP non sia scaduta e non sia revocata interagendo con il Registro Nazionale CIE.
     - Fase 3

Requisiti implementativi aggiuntivi:

	- **Rate limiting**: Protezione contro attacchi automatizzati e tentativi bruteforce.
	- **Session timeout**: Pulizia automatica di sessioni di autenticazione incomplete.
	- **Audit logging**: Logging completo di tutti gli eventi di autenticazione con identificatori di correlazione.
	- **Error handling**: Risposte di errore sicure che non fanno trapelare informazioni sensibili.
	- **Cryptographic material cleanup**: Eliminazione sicura di chiavi temporanee e challenge.

Considerazioni Implementative
-----------------------------

Le implementazioni DOVREBBERO incorporare meccanismi di rate-limiting per proteggere contro attacchi automatizzati ed esaurimento risorse, e una configurazione di timeout che bilanci esperienza utente e postura di sicurezza, accomodando la variabilità inerente nella lettura di documenti basata su NFC.

Il Provider EAA DOVREBBE implementare un approccio di timeout di sessione con meccanismi di pulizia appropriati, assicurando che le risorse di sessione siano rilasciate e il materiale crittografico temporaneo sia eliminato in modo sicuro quando le sessioni scadono.

Tutti gli eventi rilevanti per la sicurezza durante il flusso di Autenticazione eID Substantial con Verifica MRTD DEVONO essere loggati con dettaglio sufficiente per scopi di auditing preservando la privacy dell'Utente, assicurando che le informazioni di identificazione personale, quando memorizzate, siano hashate appropriatamente. I log di audit DOVREBBERO avere identificatori di correlazione consistenti, abilitando tracciamento end-to-end attraverso tutte le fasi del protocollo, con protezione di integrità crittografica per prevenire manomissioni.



.. include:: ../common/common_definitions.rst

Autenticazione eID Substantial con Verifica MRTD per Emissione PID
==================================================================

Questa Sezione definisce un protocollo di Autenticazione eID Substantial con Verifica MRTD che si integra nel flusso di emissione PID come definito nella Sezione :ref:`credential-issuance-low-level:Flussi Dettagliati per l'Emissione di Attestati Elettronici` estendendo i flussi OAuth 2.0 per includere:

	- Identificazione elettronica con Livello di Garanzia "Substantial" (LoA3) come step di autenticazione primaria.
	- Verifica di documento elettronico come livello aggiuntivo di verifica dell'identità.
	- Correlazione di sessione e binding di sicurezza tra gli step di autenticazione.
	- Integrazione con i flussi di emissione Attestati Elettronici.

Mentre l'autenticazione CIEid con LoA High rimane il metodo primario per l'attivazione Wallet e l'emissione PID, il meccanismo di Autenticazione eID Substantial con Verifica MRTD definito in questa Sezione fornisce un approccio alternativo per migliorare l'accessibilità e l'usabilità del servizio, senza compromettere la sicurezza complessiva dell'ecosistema IT-Wallet.

.. note::
  Questa Sezione attualmente supporta solo la carta d'identità CIE per il protocollo di verifica MRTD, ma il protocollo descritto in questa Sezione può essere esteso per supportare altri Documenti MRTD come i Passaporti Elettronici.

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

	- **Istanza del Wallet:** Gestisce la richiesta PID secondo le Specifiche IT-Wallet, supportando capacità crittografiche aggiuntive per la lettura di Documenti Elettronici MRTD/IAS secondo le specifiche `ICAO 9303`_ e `BSI-03110`_.
	- **Sistema di Autenticazione eID Substantial con Verifica MRTD:** Orchestra il flusso di autenticazione, integrando Provider di Identità LoA3, Servizio di Verifica di Documento Elettronico, ed eseguendo tutti i controlli di correlazione di identità per garantire che l'Utente che richiede un PID sia lo stesso Utente autenticato.

		- **Server di Autorizzazione PID:** Gestisce il flusso di autorizzazione per l'Emissione PID, coordinando l'autenticazione Utente e l'identity proofing remoto.
		- **Servizio MRTD PoP:** Gestisce il proof of possession di documento elettronico con validazione crittografica del documento.

	- **Provider di Identità LoA3:** Fornisce Schemi di Identificazione Elettronica con conformità eIDAS LoA3 (CIEid e SPID).
	- **Registro Nazionale CIE:** Fornisce evidenza privacy-preserving del binding tra NIS e codice fiscale dell'Utente richiesto per la verifica MRTD e, opzionalmente, i dati MRZ (numero documento, data di nascita, data di scadenza, cittadinanza e genere) per migliorare l'esperienza utente. Fornisce anche informazioni relative allo stato di validità del documento. Agisce come fonte autentica per la CIE.

.. _fig_eID_MRTD_System_Architecture:
.. plantuml:: plantuml/l2plus-system-architecture.puml
    :width: 99%
    :alt: La figura illustra l'Architettura del Sistema di Autenticazione eID Substantial con Verifica MRTD.
    :caption: `Architettura del Sistema di Autenticazione eID Substantial con Verifica MRTD. <https://www.plantuml.com/plantuml/svg/ZLJlRzis4Fskl-9g38ZZHNDQPnysT44LMri4v8TXUIqw311eyXmJbKIDfEowG__t7IbRLPGKYv4F2dbyz-xTktjdBDEsBlBWv9NTO870KTSviZ9KjSrbYS4hMVAy5WXlfnVZwKKsLKMbIYpjPN2TpE8iNSQB-7xvSHuFJuEJc-ZZ_P_Bx4EolCvkuZ_YkncT1YSmmpM1GJfV9CiuxO3Qkc92JyPS5OKgBv-vMQlIXco7HXKO_ZmMpB8LC_Y2K8DwY_e5WL9ad6dnWiWTotEq_nSubgMnqjPMkf82-imHRjxy2BTrRcMOMgmWgkr6QVc5kI28DDz8YzpM6eEWrJYBFzjXa_CC1X_y1oG4pagE0pgwLIj9s55LkV-kMIboD31FPg3ndngD1QUL04f1_OLa6Hv0ADUcLBbws8D34rI---2VVg8WgBJQIa58en7N-ygg1ysgZUJ0MSKeexIIBjTAm-rYEKwY5EASo6jLKinCyReWyaI12La-Z4OmJARHFVmoEP-SmLMQXEUJrw_FJmTdFvXAKzc_3PeQ1-ILArKxDlkXDAP6JLMvQkOD8JquXNy3e5yRLZX9CqEIPema_K8FlgjokgUumYbrJtgJEffPggFmyGu270HHbxnviCxL3aWTq5WeYo25kxHx9v1QKsqj7_ThspQif6ZOP8q7AMEFYJ_sJDp5cnxHtpKhSAVq9v_yFfbTl9yct-cm3s7jyvOsLqgJ_FwaetH3Y9H-obeedbMgyfmbHqf7tINjrTppbOtbthDS2e_QEMs9uJSVYACFl5X0VvKo1ernJtVIRg3hhKxyrcVeyJxCw87ur-1hVqnonIQP51MHkL7H199Zhrhlq0qcCpAhlwTFICa5XUT_239T8pS8wwCPcc03msaII-5bJwaFNHjtvfw8zWXoYPd61qcssrD6Ge4xZynoM1pE1uUBMRFb7bEZ95l6zs6bqNTH0BgBagCJzov98OGb-mmLswC-CI0Vyo_hOeKQLh9qK-dvgwh9d-zfaFy2GLbf_cqx_tvf-7P8wnU5hGtbyiTjkuOQjwh9qTNYkAYT40lCspNMdurs1XhR_btIMl7-JcW17FVSbLOx2W_zDkiZFlNjxB7rJBqgfFUTmuhcYKFeyu2tuMKV2dw5mMZKEkcMMRxn6stW6MHNj32V6VQE5TFezcPC0ppjhPPdYseXdrJKyquaX6mwrzssERCeV1E_bVaEIr4N-Ny0>`_

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

Questa specifica assume che il Server di Autorizzazione PID e il Servizio MRTD PoP operino all'interno dell'architettura dei confini del Provider PID. Questa assunzione architetturale è RACCOMANDATA per assicurare che la sessione OAuth e i nonce rilevanti utilizzati nel flusso del protocollo siano gestiti appropriatamente da entrambi i componenti senza introdurre complessità aggiuntiva nella sincronizzazione dello stato di sessione.

Quando entrambi i servizi operano all'interno dello stesso confine di fiducia, i seguenti meccanismi sono disponibili per la correlazione di sessione:

	- Accesso diretto alla memoria agli store di sessione condivisi.
	- Autenticazione interna service-to-service utilizzando chiavi pre-condivise.
	- Validazione nonce sincronizzata senza overhead di comunicazione esterna.
	- Logging di audit unificato e correlazione di eventi di sicurezza.

Quando il Server di Autorizzazione PID o il Servizio MRTD PoP sono dispiegati al di fuori dell'architettura dei confini del Provider PID, gli implementatori DEVONO fare riferimento alle :ref:`credential-issuance-l2plus:Considerazioni di Sicurezza` per misure di sicurezza aggiuntive che DEVONO essere prese per assicurare la gestione appropriata delle sessioni di autenticazione Utente. Queste misure includono ma non sono limitate a scambio sicuro di token di sessione, validazione di sessione distribuita, e meccanismi di audit trail migliorati.

Flusso Low-Level
----------------

Questa sezione fornisce dettagli tecnici su come richiedere l'Emissione PID attraverso la combinazione di identificazione elettronica con Livello di Garanzia Substantial e identity proofing remoto attraverso verifica del documento elettronico. Il servizio di Verifica MRTD gestisce lettura sicura del documento e validazione come parte di un processo di Autenticazione eID Substantial con Verifica MRTD iniziato dal Server di Autorizzazione PID.

.. _fig_eID_MRTD_Detailed_Flow:
.. plantuml:: plantuml/l2plus-detailed-flow.puml
    :width: 99%
    :alt: La figura illustra il Flusso Dettagliato di Autenticazione eID Substantial con Verifica MRTD.
    :caption: `Flusso Dettagliato di Autenticazione eID Substantial con Verifica MRTD. <https://www.plantuml.com/plantuml/svg/nLV_Rjis4FvVJt5BqJPnewH9-iTWr4rLEquqj8aH9IssUJ1ewUpSHf4QHQLjdcZliHSRURBymvcm3Him810ayxkxxxux7fctfHN6LhaCddzZxp17ID5K4eKATMKbAGn4PRMgyYcQe71OIgaGoiBEhKLbSGT42RURAx5pgXu4V19IecL4j8densVySp-OwYy0EoEZxob30wDui0DFtjFyphwJ5MvQ9MZk7IPoX0mzF8W7qWhPX4CaZz7a8F3X-cO08prYr61qDKe2L1cuo9i6rpYdqXeDb-nPI8I6vuVuSXFR41whE4DboOgL5Ll4Wr4G16v1eYViCUc2CCO3UA-Z4tW1L1j_XS9eFICr1uEvjXeKIXZAgYmrdELKbasc4D-4jQn1S0lX6uYwyB7I4a5OI_V2891S20zZLPL2PPeZ9jNKbyMIa91g1H_HqCnnOdc2eDVhmL2K24TTkARqZj2XjwM-SjztqEi54OTEO1qxYgvX5o2LXCfEADi7WxzMRkbg-ZEcTi_H0OxCNi8-uyB8MczjoIrWwrBeokSraSylKFW-GU-iq_7kX3Fn91auoT0Aac2_5WWxP2Vo-4Mcqohtd5ZadKud21prq6V02PI5Nl9VK9vKXlO1lnHai9oGscioRXU7g-DPdP_Tm6532a-NUlGE3WwUhVdttnv_uQ9teQ0iB1PDTO1VH5v8FD1clbQPu-vs9uqCvSAGW71xXJSdjnfBxjfjlG6uX8dFoBNfPahRdHeu1BpsOjq-2izV22zyY19LgHcyq8brRV6vokd4jQ-Gb2qMcwtQ4EJ-lhYv6HqU7Hp1oSjZ6EfAPMEVKSe5xyATjKNPFJpaINRmcLj_NS73zCx_fkPuskdancPr7_HUhzudttswUSDzuKFoYEYwxbhfql3gTCPgT9Mu0cEcqv2D3qcHNP8Sgxyew5ZzHtiW27HX0m1WmYoM6rDTW6jCgmAD058pRNAMbbmAFp3OOI1SPHblOr1bGR3moFgp45pBJHsMPJbsPOdI50kBMPrThQmk9agh5FTXMO5zLwtAFt90sDL5FJ7zviGzo8IjAGH2MaZGluFp0B__1fbde6XAVj8v2JQF64wCQtUxtiqP0QaI3Hc4VdJ9g6PenhnGflKAoXA1PXpHHTFMeggiTg4WiLZ0qL4JWetFIci4Cc7tMCasDxeg5iVNzoYb_kpYM3IBxhuSzdatokUBxLcWQQRyo6YhKoqbl-ePkB-HBalasG-3nGpJ3OyVdymDelhf3VJ1boWg2adf-ZOAOHJrptobtkDyJZ0uFzht3_TChWOJZs5dVGXNtdWa_XdoRyMDesGLxp9Ezg5_H-8UeQYcKm-3o4y2gHMfUUtScRIm-6VsczGUZIekWzgm7wjbMqB9DuiM8aCokO3h90gFNxxw5ZAKguRckhUEZUtHrZf2N72QVVrVXiZcy5XoPoxSeCpDQ--36eEowUOu2Vj3Vn9xtnhkVR9a1GiqLbdJiR2xz63mNgTYBmYsXj3QA7a9Lx-qpvysGTjd4HZCo63AHovWFPeSrTLuul9ne1aNkXt1rUrhDKEF6n9V4T-9KbW1PGNlZFvSel5y_1sWEPVQQdYOJayVnvgKD5UOFTF-1Z5PRF_wgh1hZSZ98aphG7jhv-YhrO7RVcbBO4FGbZkC5wslCqeHl2NB--zEu5E7JdM6THhmpFVByeFAiiSEdfv4Ju-7xg_zAcIKjWYQ_mdOZn8tQUFpYvlpwxEpoo2MCEDHwXEmf2e19RhNJ0FnqkExTAfpX0ndfAY-SajdKs3ApRfsqqQLSUJWhNkhSla7>`_

Fase 1: Richiesta di Autorizzazione OAuth
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

L'Istanza del Wallet inizia il flusso di Autenticazione eID Substantial con Verifica MRTD inviando una Pushed Authorization Request (PAR) contenente una JWT-secured Authorization Request (JAR) con requisiti di autenticazione specificati tramite Rich Authorization Requests (RAR).

Authorization Details
"""""""""""""""""""""

Il JWT Request Object DEVE contenere gli stessi parametri come definiti in :ref:`credential-issuance-endpoint:Endpoint di Pushed Authorization Request`. Quando l'Utente richiede un PID utilizzando Autenticazione eID Substantial con Verifica MRTD, l'Istanza del Wallet DEVE includere un **Authorization Details Object** aggiuntivo nel parametro ``authorization_details``, con la struttura e i claim come definiti nella Tabella dei parametri JWT Request della Sezione :ref:`credential-issuance-endpoint:Endpoint di Pushed Authorization Request`

Di seguito un esempio non normativo di PAR:

.. code-block:: http

    POST /as/par HTTP/1.1
    Host: pid-provider.example.org
    Content-Type: application/x-www-form-urlencoded
    OAuth-Client-Attestation: eyJhbGciOiJFUzI1NiIsImtp…
    OAuth-Client-Attestation-PoP: eyJhbGciOiJFUz…

    request=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL3dhbGxldC5leGFtcGxlLm9yZy9pbnN0YW5jZS8xMjM0NSIsImF1ZCI6Imh0dHBzOi8vcGlkLXByb3ZpZGVyLmV4YW1wbGUub3JnIiwibmJmIjoxNzUzNTU1NDAwLCJleHAiOjE3NTM1NTU3MDAsImlhdCI6MTc1MzU1NTQwMCwianRpIjoiYWFjNDVkZGMtY2ZiOC00OTNlLWI2NmItZTQ5ZDY4ZDVhNzVhIiwiY2xpZW50X2lkIjoiaHR0cHM6Ly93YWxsZXQuZXhhbXBsZS5vcmcvaW5zdGFuY2UvMTIzNDUiLCJyZXNwb25zZV90eXBlIjoiY29kZSIsInJlc3BvbnNlX21vZGUiOiJxdWVyeSIsInJlZGlyZWN0X3VyaSI6Imh0dHBzOi8vd2FsbGV0LmV4YW1wbGUub3JnL2NhbGxiYWNrIiwic3RhdGUiOiJhMWIyYzNkNGU1ZjY3ODkwIiwiY29kZV9jaGFsbGVuZ2UiOiJxampqUDdmaC1FdEFWcjJMWGU2ZzZwZi1LYVRGeDl6WmhIVGFHN3VIYnBvIiwiY29kZV9jaGFsbGVuZ2VfbWV0aG9kIjoiUzI1NiIsImF1dGhvcml6YXRpb25fZGV0YWlscyI6W3sidHlwZSI6Im9wZW5pZF9jcmVkZW50aWFsIiwiY3JlZGVudGlhbF9jb25maWd1cmF0aW9uX2lkIjoiZGNfc2Rfand0X1BJRF9hbHQyIiwiY3JlZGVudGlhbF9kZWZpbml0aW9uIjp7InR5cGUiOlsiVmVyaWZpYWJsZUNyZWRlbnRpYWwiLCJQZXJzb25JZGVudGlmaWNhdGlvbkRhdGEiXSwiY3JlZGVudGlhbFN1YmplY3QiOnt9fX0seyJ0eXBlIjoiaXRfbDIrZG9jdW1lbnRfcHJvb2YiLCJpZHBoaW50aW5nIjoiaHR0cHM6Ly9pZHAuZXhhbXBsZS5vcmciLCJjaGFsbGVuZ2VfbWV0aG9kIjoibXJ0ZCtpYXMiLCJjaGFsbGVuZ2VfcmVkaXJlY3RfdXJpIjoiaHR0cHM6Ly93YWxsZXQuZXhhbXBsZS5vcmcvbDJwbHVzLWNhbGxiYWNrIn1dfQ.signature

Fase 2: Autenticazione Primaria
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Dopo l'elaborazione con successo del PAR, il Server di Autorizzazione reindirizza l'User Agent al Provider di Identità LoA3 configurato per l'autenticazione primaria. L'Utente completa il flusso di autenticazione LoA3 (SPID o CIEid Substantial) e il Server di Autorizzazione correla l'identità autenticata con la sessione OAuth attiva.

Il Server di Autorizzazione PID DEVE assicurare che il parametro ``mrtd_auth_session`` sia mantenuto durante questa fase per la correlazione appropriata di sessione con gli step di autenticazione successivi.

Fase 3: Flusso di Validazione MRTD PoP
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Dopo l'autenticazione primaria con successo, il Server di Autorizzazione inizia il flusso di proof of possession del documento elettronico fornendo all'Istanza del Wallet i parametri necessari per la validazione MRTD.

JWT di Prova MRTD
""""""""""""""""""

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
     - OBBLIGATORIO. DEVE essere ``mrtd+ias+jwt``.
   * - **kid**
     - string
     - OBBLIGATORIO. Identificatore della chiave del Provider PID che DEVE essere utilizzata per verificare la firma di questo JWT.

.. _table_eID_MRTD_Proof_JWT_Payload:
.. list-table:: Payload JWT di Prova MRTD
   :widths: 20 15 65
   :header-rows: 1

   * - **Parametro**
     - **Tipo**
     - **Descrizione**
   * - **iss**
     - string
     - OBBLIGATORIO. Identificatore Provider PID.
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

L'Istanza del Wallet DEVE:

	- Validare la firma JWT utilizzando la chiave pubblica del Provider PID ottenuta tramite valutazione di fiducia.
	- Verificare che il campo ``status`` sia impostato a "require_interaction".
	- Verificare che il tipo di autenticazione corrisponda al valore atteso ``mrtd+ias``.
	- Estrarre HTTP target URI (``htu``) e metodo (``htm``) per lo step successivo.
	- Gestire errori di validazione JWT e di rete, e fornire feedback utente con meccanismi di retry appropriati.

Richiesta MRTD PoP
"""""""""""""""""""

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
    Host: pid-provider.example.org
    Content-Type: application/json
    OAuth-Client-Attestation: eyJhbGciOiJFUzI1NiIsImtp…
    OAuth-Client-Attestation-PoP: eyJhbGciOiJFUz…

    {
      "mrtd_auth_session": "wxroVrBY2MCq4dDNGXACS",
      "mrtd_pop_jwt_nonce": "f42cccb7f1c8269f9d4aeefe339c6b13"
    }

**L'Istanza del Wallet DEVE:**

	- Validare la firma JWT di Prova MRTD utilizzando la chiave pubblica del Provider PID.
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
""""""""""""""""""

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
     - OBBLIGATORIO. Identificatore della chiave del Provider PID che DEVE essere utilizzata per verificare la firma di questo JWT.

.. _table_eID_MRTD_PoP_Response_Payload:
.. list-table:: Parametri Risposta MRTD PoP
   :widths: 20 15 65
   :header-rows: 1

   * - **Parametro**
     - **Tipo**
     - **Descrizione**
   * - **iss**
     - string
     - OBBLIGATORIO. Identificatore Provider PID.
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

**Il Servizio MRTD PoP DEVE:**

	- Generare dati di challenge crittograficamente sicuri per validazione ``MRTD+IAS`` con entropia sufficiente (da utilizzare nel protocollo Anti-Cloning Internal Authentication dall'Istanza del Wallet), memorizzandoli con tempo di scadenza appropriato. Inoltre, il Servizio MRTD PoP DEVE assicurare unicità del challenge per prevenire attacchi di riutilizzo.
	- Creare un nuovo ``mrtd_pop_nonce`` unico per lo step successivo per prevenire attacchi replay.
	- Validare continuità di sessione assicurando che il parametro ``mrtd_auth_session`` corrisponda a una sessione attiva.
	- Restituire stato HTTP *202 Accepted* per indicare iniziazione di elaborazione asincrona.
	- Includere header Content-Type appropriato (``application/json; charset=utf-8``).
	- Gestire errori di servizio e restituire risposte di errore appropriate.
	- Estrarre e validare informazioni MRZ se fornite da servizi di registro esterni.

**L'Istanza del Wallet DEVE:**

	- Validare stato risposta HTTP (*202 Accepted*) e content type.
	- Analizzare risposta JSON e validare parametri richiesti (``challenge``, ``mrtd_pop_nonce``).
	- Estrarre dati di challenge per validazione crittografica del documento.
	- Memorizzare nuovo valore ``mrtd_pop_nonce`` in modo sicuro per richieste di validazione successive.
	- Validare informazioni MRZ opzionali se presenti nella risposta.
	- Gestire errori, fornendo feedback utente relativo.
	- Memorizzare dati di challenge temporaneamente in memoria sicura (non storage persistente).
	- Preparare sessione di lettura NFC.

L'Istanza del Wallet esegue lettura e validazione di documento elettronico basata su NFC, poi invia l'evidenza al Provider PID per verifica finale e correlazione di identità con il risultato di autenticazione LoA3.

Richiesta di Validazione MRTD PoP
""""""""""""""""""""""""""""""""""

Dopo che tutte le evidenze sono state raccolte tramite interazione NFC con il Documento Elettronico, l'Istanza del Wallet DEVE inviare tutti i dati al Server di Autorizzazione del Provider PID per la validazione finale e controlli incrociati di identità. L'Istanza del Wallet DEVE inviare una Richiesta HTTP POST con ``application/json`` come content type, includendo Wallet Attestation e Wallet Attestation JWT PoP nell'header secondo `OAUTH-ATTESTATION-CLIENT-AUTH`_. Il payload della Richiesta contiene i seguenti parametri.

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
"""""""""""""""""""""""""""""

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
     - OBBLIGATORIO. DEVE essere ``mrtd+ias+jwt``.
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
     - OBBLIGATORIO. Identificatore Provider PID.
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
     - OBBLIGATORIO. Dati di validazione IAS contenenti NIS, Anti-Cloning Public Key, e SOD.

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
   * - **nis**
     - string
     - OBBLIGATORIO. Valore NIS (Service Identification Number).
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
    Host: pid-provider.example.org
    Content-Type: application/json
    OAuth-Client-Attestation: eyJhbGciOiJFUzI1NiIsImtp…
    OAuth-Client-Attestation-PoP: eyJhbGciOiJFUz…

    {
      "mrtd_validation_jwt":"eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL3dhbGxldC5leGFtcGxlLm9yZy9pbnN0YW5jZS8xMjM0NSIsImF1ZCI6Imh0dHBzOi8vcGlkLXByb3ZpZGVyLmV4YW1wbGUub3JnIiwiaWF0IjoxNzUzNTU1NDAwLCJleHAiOjE3NTM1NTU3MDAsImRvY3VtZW50X3R5cGUiOiJjaWUiLCJtcnRkIjp7ImRnMSI6IlVEeEpWRUU4VTAxSlZFZzhQRXBQU0U0OFBFcFBTRTRnVTAxSlZFZzhQREU1T0RBME1UVThUVDxQTnpjM056SXpNUT09IiwiZGcxMSI6Ik1USXpORFUyTnpnNVFVSkRSRVZHUjBoSlNrdE1UVTVQVUVGT1IxSlRWRlZXV0ZsYVUwRkVSVVU9Iiwic29kX21ydGQiOiJNSUlGempDQ0JMYWdBd0lCQWdJSVFPWTJLSkdGVFVJd0RRWUpLb1pJaHZjTkFRRUxCUUF3WHpFTE1Baz0ifSwiaWFzIjp7Im5pcyI6IklUMTIzNDU2Nzg5MDEyMzQiLCJpYXNfcGsiOiJNSUlCSWpBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE4QU1JSUJDZ0tDQVFFQXoxMjM0NTY3ODkwPSIsInNvZF9pYXMiOiJNSUlGYURDQ0JGQ2dBd0lCQWdJSkFMMktKR0ZUVUl3RFFZSktvWklodmNOQVFFTEJRQXdYekVMTUE9PSIsImNoYWxsZW5nZV9zaWduZWQiOiJhMWIyYzNkNGU1ZjY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTBhYmNkZWYxMjM0NTY3ODkwYWJjZGVmPT0ifX0.xyz456abc789def012ghi345jkl678mno901pqr234stu567vwx890yz123",
      "mrtd_auth_session":"wxroVrBY2MCq4dDNGXACS",
      "mrtd_pop_nonce":"9f2c4a7e3b1d8c9a6e5f4b2a1c3d7e8f"
    }

**L'Istanza del Wallet DEVE:**

	- Eseguire lettura documento NFC conforme `ICAO 9303`_ (PACE, ecc.).
	- Validare firme crittografiche del documento e catene di certificati.
	- Estrarre attributi di identità (DG1 e DG11), NIS, Anti-Cloning Public Key dai data groups del documento, e SODs (dalle Applicazioni MRTD e IAS).
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
	- Analizzare e validare la firma e struttura ``mrtd_validation_jwt``.
	- Validare autenticità del documento utilizzando standard `ICAO 9303`_.
	- Verificare risposta challenge Anti-Cloning.
	- Controllare validità del documento (stato non di revoca).
	- Controllare il binding tra NIS ottenuto dall'Applicazione IAS e codice fiscale dell'Utente letto dall'Applicazione MRTD per assicurare che entrambi i valori provengano dallo stesso chip.

Risposta di Validazione MRTD PoP
"""""""""""""""""""""""""""""""""

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
     - REQUIRED. DEVE essere valorizzato con `require_interaction`.
   * - **type**
     - string
     - REQUIRED. DEVE essere valorizzato con `redirect_to_web`.
   * - **mrtd_val_pop_nonce**
     - string
     - OBBLIGATORIO. Nonce di conferma finale per callback basato su browser.
   * - **redirect_uri**
     - string
     - REQUIRED. URI di redirect del browser per il completamento del flusso autorizzativo.

Di seguito un esempio non normativo di una Risposta di Validazione MRTD PoP:

.. code-block:: http

    HTTP/1.1 202 Accepted
    Content-Type: application/json; charset=utf-8

    {
      "status": "require_interaction",
 	    "type": "redirect_to_web",
      "mrtd_val_pop_nonce": "0f2bff024317345b6927ce17e776361d",
      "redirect_uri":"https://pid-provider.example.org/cb"
    }

Conferma Finale Basata su Browser
""""""""""""""""""""""""""""""""""

Dopo validazione MRTD PoP con successo, l'Istanza del Wallet DEVE reindirizzare l'User Agent al ``challenge_redirect_uri`` specificato nell'Authorization Details Object iniziale, includendo il ``mrtd_val_pop_nonce`` come parametro query:

.. code-block:: text

    https://pid-provider.example.org/l2plus-callback?mrtd_val_pop_nonce=0f2bff024317345b6927ce17e776361d_signed&mrtd_auth_session=wxroVrBY2MCq4dDNGXACS

L'Istanza del Wallet DEVE validare che il ``mrtd_val_pop_nonce`` corrisponda al valore ricevuto dalla Risposta di Validazione MRTD PoP.

Fase 4: Risposta di Autorizzazione OAuth
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Dopo completamento con successo di tutti gli step di autenticazione e correlazione di identità, il Server di Autorizzazione DEVE emettere la Risposta di Autorizzazione OAuth finale. Se tutti i controlli di validazione sono stati superati, il Server di Autorizzazione DEVE reindirizzare l'User Agent nuovamente all'Istanza del Wallet con una Risposta di Autorizzazione OAuth includendo il codice di autorizzazione come definito negli step 6-7 di :ref:`credential-issuance-low-level:Issuance Flow`, e nella Sezione :ref:`credential-issuance-endpoint:Risposta di Autorizzazione`. Il Server di Autorizzazione DEVE utilizzare il ``redirect_uri`` incluso nel Request Object iniziale dall'Istanza del Wallet.

Gestione Errori
---------------

La gestione errori DEVE seguire le stesse regole come definite nella Sezione :doc:`credential-issuance-endpoint`, riguardo ai formati e i riferimenti standard correlati.

Durante il flusso di Validazione MRTD PoP, quando si verificano errori recuperabili, il Servizio MRTD PoP PUÒ generare e restituire un nonce fresco per abilitare l'Utente a tentare nuovamente mantenendo sicurezza di sessione e prevenendo attacchi replay.

In aggiunta ai codici di errore già definiti nella Sezione :doc:`credential-issuance-endpoint`, almeno i seguenti codici di errore DEVONO essere supportati.

Errori Risposta MRTD PoP
^^^^^^^^^^^^^^^^^^^^^^^^^

.. _table_eID_MRTD_PoP_Response_Errors:
.. list-table:: Codici Errore Risposta MRTD PoP
   :widths: 30 70
   :header-rows: 1

   * - **Codice Errore**
     - **Descrizione**
   * - **temporarily_unavailable**
     - Servizio di validazione documento o servizio Registro CIE è temporaneamente non disponibile.

Errori Risposta di Validazione MRTD PoP
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

Mappatura Codici di Stato HTTP
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Le risposte di errore DEVONO utilizzare codici di stato HTTP appropriati:

	- **400 Bad Request**: Per errori ``invalid_request``.
	- **401 Unauthorized**: Per errori ``invalid_client``.
	- **403 Forbidden**: Per errori ``access_denied``.
	- **503 Service Unavailable**: Per errori ``temporarily_unavailable``.

Considerazioni di Sicurezza
---------------------------

Gestione Sicura di Sessione
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Il parametro ``mrtd_auth_session`` serve come meccanismo di correlazione primario tra gli step di autenticazione. Le implementazioni DEVONO assicurare che questo identificatore abbia entropia sufficiente (minimo 128 bit) e sia crittograficamente sicuro. L'identificatore di sessione DEVE essere validato a ogni step per prevenire attacchi di session fixation.

Ogni step di autenticazione DEVE essere crittograficamente legato alla sessione OAuth tramite validazione JWT firmata per prevenire attacchi di session fixation, session confusion, e sostituzione di identità. Il Server di Autorizzazione DEVE mantenere la correlazione tra l'identità LoA3 e il proof del documento all'interno di un singolo contesto di sessione.

.. _fig_eID_MRTD_Security_Controls:
.. plantuml:: plantuml/l2plus-security-controls.puml
    :width: 99%
    :alt: La figura illustra i Controlli di Sicurezza per Autenticazione eID Substantial con Verifica MRTD.
    :caption: `Controlli di Sicurezza per Autenticazione eID Substantial con Verifica MRTD. <https://www.plantuml.com/plantuml/svg/nLT_Rzis4FsVd-AMebtYHacJT6rdr4bLvqSyj8aHEoksPJ1ewMnpfKcDf9nadtuyIfPbfmuoRC00Wx2b-_7ktV6H_c0TDowVIlRzTsw2KuG4JIwHgqZdJWg5ZETEgtmwHCCoRoiIaN7bOEFQeja0Rk5w-VaNBYKww2WVMYKOJE9batRd93nkiw6-0zZeTewXQ_HCf1JosISndhYFCiTbBxAASpVHHlp5dT0AUcXc9OYujspy-QhlO-fki14bZEFkPRV7KANWypw011SXAfTmXMDXdRaFJfyx5ykcSxCRrKbHEU7k5-39eNFSPOpvvn81FUPFEZu8mCauAP2_18DJxH34F4Hcj1u9DGQXeDEFIXQfvewrEJ49frBVCdODqI74JVX2O9m6dZWnumx19u3IxKRbbc9DS-b4P1rcm9S1JD4JcJBMQhMWE-4MOQy9buHoXUCh_3D7ww3LOd78t8CcTEEhwiKcG2A53pqGwJQOukdby0zCt9O70d0htAG87RM3OHGxvssA-5obQrz6r42XGcNdo3t1P4un6uqGbTUX3b9qN4Xmznd2Xd03kVyorKa-9Mo1ter6Wp5VG4HrL6NOJ2kBi5b27-H6R0FUPSAW7GYrDQ-xITrOmmvXEZlfm-uS4HvLfBHsTdPUr8BJRx8_rzOr8HDfb9NZiuDtV9f9tD5cN6_Dlazjn9IR-zKvYiA4qLPSVKFyqEX1Bn_IJdI2IsgYKJHsUaOUFR_N-0oLJ-stcvsmNlk0jaUm2KGTqZGtASbo_Afovj_3UoBqkbdWuAkJdX2zgh0CHAw9L_JXwG3h31qqeThnFtCfqY8e3Mslt2_d_NvtTszd3mvUxSEfpccGF455-YPCdCjiStSt2EBERTX7zNxi9XDwfiPur6XCZKkBaMgzNtmV_FIbVqWZLY_XOGLlQnNGQ1MorFGpNPLGajjetAZkPS-F5Vf1ZaAINQ64guhn9Jm-HZVglzn-zT8As0_BUxCDlVOxMdwi5Qepnm2WSF95awmsmHVgZC0P-kxzwbEDj9c6r6HB9X1L_AoQK736odZKuZg3rJWHXLNdzttduoJ1p65Q4bDqJsS3fLM2sr1rEJ2pgRD2w-NzLiYVSiSPuz91PrG0ik0B13xZGlAXH70wyBLo2ePwOYYsITbTCXKUed7GZY-2nLpREul7A2s2g9BfeUD2OGhSGOzqVM-lYasU9tVEyCG5e30oUagE1LLZe_EiF5r_GIdrBLoSjdqkX-HIYGR13plPKmt7fO12buOF_AUhhKLhlJazSphHCfnCX68EvRTdOuEeVZ-4DbHjYRDCBdIh6xTFg3bNo5CuFjlRfiMllSlZ0PbJAEyTBMAHP7_B4jYwj9suLyzQfRlezBOX9ksHMj4vsSs7tWY-udqHbXpN07YwxpAWPjsf85rnkQA2DzHtsblL6Av1STMBe_rNhz-15MF5NMwGMkD3BJofwMi5Pg6HZsgDXo96z_-RsW3yCxsXnKy6y-j--7uGrjSr7LhM7ofiJW2DEtKtQf_2ZKgqCIWBrCa4aw_5pMD6lD5rZK3djYJTsyyl6dIDcEcavhZ5s8gGrVJe5Ln-VOgexlqGAdaJrhTXVVUmAfA0DMr-iY0QJ8N19DnKgEP28NtT2vLaRAusD7sF68IP-sZqhKKJ3Rd554u5JNrRgv4mqsfN-gjJTG2lcwtTP7WKehSU9XmG44nVQBfy34fv2lSkwXCMDwvDDp4w7qzWM23QMZwe7n-jRzuwNg-xCXTKrwuVH0JT7jSOteeoY6ScBLhqxsuhHzuwqMbPEInee1_2sbO8yFmWVhv_wZ_hE5zcQ3jmr3axxvzTdPnSiFu4OKJAdsZbXChH0ayIRL9IEAVhVrvAGsuXnH6TN-LEh_tLiHacObGAuOBk3_vRFfL_0m00>`_

Generazione Challenge Crittografico
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Il Servizio MRTD PoP DEVE generare challenge crittograficamente sicuri con entropia sufficiente per la validazione del documento. I valori di challenge DEVONO essere unici e NON DEVONO essere riutilizzati attraverso sessioni diverse o tentativi di autenticazione. L'algoritmo di generazione challenge DOVREBBE incorporare l'identificatore ``mrtd_auth_session`` e timestamp per assicurare binding crittografico appropriato.

Gestione Ciclo di Vita Nonce
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Ogni step nel flusso di Autenticazione eID Substantial con Verifica MRTD DEVE utilizzare valori nonce unici per prevenire attacchi replay. I valori nonce DEVONO avere tempi di scadenza appropriati e DEVONO essere invalidati dopo uso con successo. Il Server di Autorizzazione PID e il Servizio MRTD PoP DEVONO mantenere validazione nonce sincronizzata per assicurare integrità di sessione.

Controlli di Sicurezza
^^^^^^^^^^^^^^^^^^^^^^^

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
     - L'Istanza del Wallet assicura l'autenticità del Provider PID e del Provider di Identità eID tramite pinning del certificato leaf di ogni server.
     - Tutte
   * - **SC3**
     - Il Server di Autorizzazione PID verifica che il Provider di Identità eID utilizzato nella fase *eID LoA3* sia accreditato.
     - Fase 2
   * - **SC4**
     - Il Server di Autorizzazione PID verifica l'autenticità e integrità dei dati estratti dall'asserzione *eID LoA3*, controllando la firma digitale.
     - Fase 2
   * - **SC5**
     - Il valore challenge e tutti i valori nonce sono generati con protezioni per prevenire attacchi bruteforce o di indovinamento.
     - Fase 3
   * - **SC6**
     - Il Provider PID verifica tutti i valori nonce per rilevare attacchi replay.
     - Fase 3
   * - **SC7**
     - L'Istanza del Wallet verifica che ``challenge_info`` sia firmato appropriatamente dal Server di Autorizzazione PID. Inoltre, controlla che ``challenge_info`` contenga: un valore ``iss`` corrispondente al valore del Server di Autorizzazione PID; un valore aud uguale al ``client_id`` dell'Istanza del Wallet; e un valore ``state`` uguale a quello nella richiesta PAR, per essere sicuri che la risposta sia legata alla richiesta iniziale fatta dall'Istanza del Wallet nello Step 2. Quindi le informazioni fornite come parte di ``challenge_info``, in particolare l'``htu`` che corrisponde all'url di redirect da seguire per il *MRTD PoP*, non sono manomesse.
     - Fase 3
   * - **SC8**
     - Il Provider PID controlla che l'``mrtd_auth_session`` sia associata alla stessa Istanza del Wallet in tutte le richieste nella fase *MRTD PoP*. Quindi il Provider PID può essere sicuro che l'Istanza del Wallet che esegue la fase *MRTD PoP*: sia fidata; sia sempre la stessa attraverso il protocollo; e abbia precedentemente iniziato l'emissione PID (richiesta PAR). Questo può essere implementato richiedendo all'Istanza del Wallet di eseguire un proof of possession della sua chiave privata (es., all'interno di OAuth-Client-Attestation o firmando un valore nonce).
     - Fase 3
   * - **SC9**
     - Il Provider PID controlla che l'``mrtd_auth_session`` non sia scaduta (timeout di validità tipicamente di 5 minuti), cioè che l'operazione sia stata conclusa entro una certa quantità di tempo.
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

Requisiti implementativi aggiuntivi:

	- **Rate limiting**: Protezione contro attacchi automatizzati e tentativi bruteforce.
	- **Session timeout**: Pulizia automatica di sessioni di autenticazione incomplete.
	- **Audit logging**: Logging completo di tutti gli eventi di autenticazione con identificatori di correlazione.
	- **Error handling**: Risposte di errore sicure che non fanno trapelare informazioni sensibili.
	- **Cryptographic material cleanup**: Eliminazione sicura di chiavi temporanee e challenge.

Considerazioni Implementative
-----------------------------

Le implementazioni DOVREBBERO incorporare meccanismi di rate-limiting per proteggere contro attacchi automatizzati ed esaurimento risorse, e una configurazione di timeout che bilanci esperienza utente e postura di sicurezza, accomodando la variabilità inerente nella lettura di documenti basata su NFC.

Il Provider PID DOVREBBE implementare un approccio di timeout di sessione con meccanismi di pulizia appropriati, assicurando che le risorse di sessione siano rilasciate e il materiale crittografico temporaneo sia eliminato in modo sicuro quando le sessioni scadono.

Tutti gli eventi rilevanti per la sicurezza durante il flusso di Autenticazione eID Substantial con Verifica MRTD DEVONO essere loggati con dettaglio sufficiente per scopi di auditing preservando la privacy dell'Utente, assicurando che le informazioni di identificazione personale, quando memorizzate, siano hashate appropriatamente. I log di audit DOVREBBERO avere identificatori di correlazione consistenti, abilitando tracciamento end-to-end attraverso tutte le fasi del protocollo, con protezione di integrità crittografica per prevenire manomissioni.


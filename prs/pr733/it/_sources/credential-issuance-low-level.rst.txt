.. include:: ../common/common_definitions.rst

Flussi Dettagliati per l'Emissione di Attestati Elettronici
============================================================

Issuance Flow
--------------

Il flusso di emissione degli Attestati Elettronici (Issuance Flow) è basato su [`OpenID4VCI`_] e i seguenti standard/specifiche di riferimento principali DEVONO essere supportati in aggiunta a `OpenID4VCI`_:

  * **The OAuth 2.0 Authorization Framework** [:rfc:`6749`], come raccomandato nella Sezione 3 di [`OpenID4VCI`_].
  * **Pushed Authorization Requests** (PAR) [:rfc:`9126`], come raccomandato nella Sezione 5 di [`OpenID4VCI`_].
  * **Proof Key for Code Exchange** (PKCE) [:rfc:`7636`], come raccomandato nella Sezione 5 di [`OpenID4VCI`_].
  * **JWT Authorization Requests** (JAR) [:rfc:`9101`].
  * **JWT Authorization Response Modes** (JARM) [`JARM`_].
  * **Rich Authorization Requests** (RAR) [:rfc:`9396`].
  * **OAuth 2.0 Attestation-Based Client Authentication** [`OAUTH-ATTESTATION-CLIENT-AUTH`_].
  * **OpenID Federation 1.0** [`OID-FED`_].

Il Credential Issuer DEVE utilizzare un *OAuth 2.0 Authorization Server* basato su :rfc:`6749` per autorizzare l'Utente a ottenere un Attestato Elettronico. I Credential Issuer DEVONO supportare:

  * **Authorization Code Flow**: Il Credential Issuer richiede l'autenticazione dell'Utente e il consenso all'Authorization Endpoint prima di raccogliere le informazioni dell'Utente per creare e rilasciare un Attestato Elettronico.
  * **Wallet Initiated Flow**: La richiesta dell'Istanza del Wallet viene inviata al Credential Issuer senza alcun input dal Credential Issuer.
  * **Immediate Issuance Flow**: Il Credential Issuer rilascia l'Attestato Elettronico direttamente in risposta alla Credential Request.

In aggiunta, i Credential Issuer POSSONO supportare:

  * **Issuer Initiated Flow**: L'Istanza del Wallet invia la sua richiesta al Credential Issuer in base all'input fornito dal Credential Issuer.

    * **Same-device Issuance Flow**: L'Utente riceve l'Attestato Elettronico sullo stesso dispositivo utilizzato per avviare il flusso.
    * **Cross-device Issuance Flow**: L'Utente riceve l'Attestato Elettronico su un dispositivo diverso da quello su cui ha avviato il flusso.

  * **Refresh Token Flow**: L'Istanza del Wallet richiede un nuovo Access Token al Token Endpoint del PID/(Q)EEA Provider.
  * **Re-issuance Flow**: A seguito di aggiornamenti ad un Attestato Elettronico già memorizzato, l'Istanza del Wallet richiede un aggiornamento dell'Attestato Elettronico al Credential Endpoint del Credential Issuer.
  * **Deferred Issuance Flow**: Il Credential Issuer potrebbe impiegare del tempo per emettere l'Attestato Elettronico richiesto, a causa delle regole di provisioning dei dati delle Fonti Autentiche, e consente al Wallet di recuperare l'Attestato Elettronico richiesto in futuro.

L'intero Issuance Flow può essere suddiviso in due sotto-flussi:

  - **Flusso di Richiesta dell'Utente**, che descrive le modalità attraverso le quali l'Utente può richiedere l'Attestato Elettronico. Può essere:

      1. Su iniziativa dell'Utente (**Wallet Initiated**).

      2. Su proposta del Credential Issuer (**Issuer Initiated**).

  - **Flusso di Emissione**, che descrive le interazioni tra l'Istanza del Wallet e il Credential Issuer.

Il seguente diagramma mostra il *flusso di richiesta dell'Utente*.

.. _fig_Low-Level-Flow-ITWallet-PID-QEAA-User-Request:
.. plantuml:: plantuml/credential-user-request-flow.puml
    :width: 99%
    :alt: La figura illustra il flusso di richiesta dell'Attestato Elettronico da parte dell'Utente.
    :caption: `Richiesta dell'Attestato Elettronico da parte dell'Utente - Flusso dettagliato. <https://www.plantuml.com/plantuml/svg/hP9FJzj04CNlyob6uT3sG14zve20XAgHAWKA5PTUrkknFMAzQ-sV6BvzPpTkapHLAoGkLkJClFTxptCPel8nzGPKYiwclYAFvn_F0GPvpve7PIFElWVoCrG14q3bdhSltWKClKmDdRCqmvElt7RnsYGwtBtsRlorNld3_nwLCHHnPGN3QYep8v2jKLmEhUWvahVAO4qRrjblxPLj_sb6Ewc3gOMdccnaKLk5aAPv1b0c8ZVu6ujb9bADduqR0HAUNk0un_L05cD7-0S-gc7uOOtJefk40gNJBlje5TbPK3hoHlGaufYbqXnT5HLRV779uv9RZhAweykEMyiN2W3UEbbs6r4UyUJno-hX1jP5eD0O3X5TKtu_-1Go-57Ia2ifGW3ZwOKWQ6SRzdrP2sH8PrRHETu5I88ZDEu9eAQzE40ca3Gt3HurjtTSd_9nbIPvQl9sjJnxV_VXxERg2c-zst2T0r8LM23vDKNnLDJq6HVUXO3BSYyJI96hFCsnYxt1GRM2px73ksyBLrCk8_kmRVVZhvj6qilQ17FVkJ7tDMqLcOpmjkSnYf5MLammkm3iQhvNFVqrs56kpbFpdrHJA6rOFnNkibEb60KAtZHNFhxjur8UgJS_0G00>`_

**Passi 1.1-1.4 (Flusso Avviato dal Wallet):** L'Utente, utilizzando l'Istanza del Wallet, seleziona il Credential Issuer tra quelli elencati nella lista delle entità affidabili.

**Passi 2.1-2.3 (Flusso Avviato dall'Issuer):** L'Utente, mentre naviga sul sito web del Credential Issuer, trova un link per ottenere un Attestato Elettronico.

**Passi 2.4-2.7 (Cross-Device):** La Credential Offer viene presentata come un codice QR mostrato all'Utente. L'Utente scansiona il codice QR utilizzando l'Istanza del Wallet, che recupera i parametri definiti nella :ref:`Tabella dei parametri della Credential Offer <table_credential_offer_claim>`.

**Passi 2.8-2.10 (Same-Device):** La Credential Offer viene presentata come un pulsante href contenente l'URL che consente all'Utente di invocare l'Istanza del Wallet utilizzando il Credential Offer Endpoint.

Di seguito un esempio non normativo di un URL relativo a una Credential Offer che può essere incluso in un codice QR o in una pagina HTML con un pulsante href:

.. code-block:: text

  openid-credential-offer://?credential_offer%3D%7B%22credential_issuer%22%3A%22https%3A%2F%2Feaa-provider.example.org%22%2C%22credential_configuration_ids%22%3A%5B%22dc_sd_jwt_EuropeanDisabilityCard%22%5D%2C%22grants%22%3A%7B%22authorization_code%22%3A%7B%22issuer_state%22%3A%22oaKazRN8I0IbtZ0C7JuMn5%22%7D%7D%7D


Il seguente diagramma mostra il *flusso di emissione*.

.. _fig_Low-Level-Flow-ITWallet-PID-QEAA-Issuance:
.. plantuml:: plantuml/credential-issuance-flow.puml
    :width: 99%
    :alt: La figura illustra il flusso dettagliato per l'emissione degli Attestati Elettronici.
    :caption: `Emissione degli Attestati Elettronici - Flusso dettagliato. <https://www.plantuml.com/plantuml/svg/hLPVRo8t47_tfnZb7XeaKAgsJoTTTOJG2sgKq9HJNYeXnpl0A8kzjSTmwQUlFLdmGaYhg9MYxAxd_-ytC-PpOEqvhckb8piRru_ebMhI6Hbgj6Ku-nhGdu4E49LwTDzU3huB4DP9gravYsVmuOQMAxwi8nxQNdgttPlhGzc3hcjacDZ0sXeKdQr2Mq6ASfJ3o6E5badNC0aXjXv9AMyT8xWDUjZsAUKn-N8z-t8_7j-gqGhD4xoo10gGVODR0AyGVabohvcS1PrYkqVMP84um1fPLvfrpadYABM5mS-mXOzWF6f6cFuw6eDn5KBAW1Q4Nfmy30TJDstLAQbFX_TmZtz630pdVrW0KnDQdbFLpr_-HTI3_B4bNi7TCF9gC1AjmP0vIKkERmbpK20hPLsZJdLryJc5Jil1rBiDLV-8JMiGQ6arHu-joix3KOg2tqRNL14_GmT0HJ0G27UOXCRPW73UGZ2Fdlg0tnho6EPaUqfGJ2PHVuHSj_FqbyGfW1OmeUEcfw8MItgteT8rTpldqoUOJguEmEn7-F1mFPcDLGoPzHGWAvkN2CBXY71o1JTk2DTfEk3yviUUO6DonJQ5TqrMJW0-fxC4es6oIuWoNbcBjU7GA-XX7V0ehVFVUkFXiFVUr58r_p4LM-suZ1gE0IwqvjdeG-wCzA0GzgHitsLK1c-95dqIm5LkzYTyVbFMUESMdN64XVCdrW6x9xIGwcaSMLQTePqbIMaMmQtZMCPuwRNbEJytA7ES4YylyzrAQ4Uy8ez66apc_7yTSqM2GKbwZwKs1aEOIvMvonSUmshtAGz9_t3c2WQtpXhSOt0zcqrXUlVx32vi5fIuEyN2uLmqUgzsPWjV-cjS21W2ENkeVgHVC7-3GRC_AJIM2eh-2Igxw0ZcNOABtpd9Y-ntrmquDyukQ1cz42EBH8nVhn0Ae3UQQlrO8wW2N5Ude5SYX3vObqERNOWkf6cEBrvMGDcsgGoPdHZ0v9tTgiUahiEJO9XlyDtigzWwsnq0EmZiF4g3bKnAM14VYKh3b6HFzarNVdvKMXzmWrRkmGv9Go7ffRFLgHljykRhMDtZaWAdKrtNHvaFFDQQiG95DfM_bd02HFAoZt_XSUFQnCgLLPWwAArm9RNzyFrFIGmZPpb3MZPrOV_sRbOwu5_ehr5NSwOrze6zja6R7VVTycEVr2mLUlH3gWzw8JXOq6iNhTpcsHc41arkuWeUds4VGnfckq8Bx6cvH2_o3A7qYInYpq4E5hNRWbvgieTNmUVqBwxhlm40>`_

Una volta completato il *flusso di richiesta dell'Utente*, l'Istanza del Wallet elabora i Metadata del Credential Issuer come definito nella Sezione :ref:`trust:Meccanismo di Valutazione della Fiducia`.

.. note::
  **Controllo della Federazione:** L'Istanza del Wallet deve verificare se il Credential Issuer è membro della Federazione, ottenendo i suoi Metadata specifici per il protocollo. Un esempio non normativo di una risposta dall'Endpoint **.well-known/openid-federation** con la **Entity Configuration** e i **Metadata** del Credential Issuer è rappresentato nella sezione :ref:`credential-issuer-entity-configuration:Entity Configuration del Fornitore di Attestati Elettronici`.

Nel caso del flusso avviato dall'Issuer, oltre al controllo della federazione definito sopra, l'Istanza del Wallet DEVE eseguire i seguenti controlli sui parametri della Credential Offer:

  * Per ogni identificativo di Attestato Elettronico contenuto nell'array ``credential_configuration_ids``, verificare se è supportato dal Credential Issuer.
  * L'identificativo dell'Authorization Server (se presente) è contenuto nel parametro ``authorization_servers`` dei Metadata del Credential Issuer.


**Passi 1-2 (`PAR Request`)**: L'Istanza del Wallet:

  * Crea un nuovo `PKCE code verifier`, una prova di possesso dell'Attestato di Unità di Wallet e un parametro ``state`` per la *Pushed Authorization Request*.
  * Fornisce al PAR Endpoint del Credential Issuer i parametri precedentemente elencati, utilizzando il parametro ``request`` (di seguito `Request Object`) secondo la Sezione 3 di :rfc:`9126` per prevenire l'attacco di scambio del `Request URI`. La Pushed Authorization Request consente l'autenticazione del client prima di qualsiasi interazione dell'Utente. Questo passaggio permette il rifiuto anticipato di richieste illegittime, prevenendo efficacemente attacchi di spoofing, manomissione e uso improprio delle richieste di autorizzazione.
  * DEVE creare il ``code_verifier`` con una stringa casuale con sufficiente entropia utilizzando i caratteri non riservati con una lunghezza minima di 43 caratteri e una lunghezza massima di 128 caratteri, rendendo impraticabile per un attaccante indovinarne il valore. Il valore DEVE essere generato seguendo la raccomandazione nella Sezione 4.1 di :rfc:`7636`.
  * Firma questa richiesta utilizzando la chiave privata creata durante la fase di configurazione per ottenere l'Attestato di Unità di Wallet. La relativa chiave pubblica attestata dal Fornitore di Wallet viene fornita all'interno del claim ``cnf.jwk`` dell'Attestato di Unità di Wallet.
  * DEVE utilizzare i parametri ``OAuth-Client-Attestation`` e ``OAuth-Client-Attestation-PoP`` secondo OAuth 2.0 Attestation-based Client Authentication [`OAUTH-ATTESTATION-CLIENT-AUTH`_], poiché in questo flusso il Pushed Authorization Endpoint è un endpoint protetto.
  * Specifica i tipi di credenziali richieste utilizzando il parametro ``authorization_details`` [RAR :rfc:`9396`] e/o il parametro ``scope``.

Il Credential Issuer esegue i seguenti controlli alla ricezione della `PAR Request`:

    1. DEVE validare la firma del `Request Object` utilizzando l'algoritmo specificato nel parametro ``alg`` dell'header (:rfc:`9126`, :rfc:`9101`) e la chiave pubblica recuperata dall'Attestato di Unità di Wallet (``cnf.jwk``) referenziato nel `Request Object`, utilizzando il parametro ``kid`` dell'header JWT.
    2. DEVE verificare che l'algoritmo utilizzato per firmare la richiesta nell'header ``alg`` sia uno di quelli elencati nella Sezione :ref:`algorithms:Algoritmi Crittografici`.
    3. DEVE verificare che il ``client_id`` nel body della `PAR Request` corrisponda al claim ``client_id`` incluso nel `Request Object`.
    4. DEVE verificare che il claim ``iss`` nel `Request Object` corrisponda al claim ``client_id`` nel `Request Object` (:rfc:`9126`, :rfc:`9101`).
    5. DEVE verificare che il claim ``aud`` nel `Request Object` sia uguale all'identificativo del Credential Issuer (:rfc:`9126`, :rfc:`9101`).
    6. DEVE rifiutare la `PAR Request`, se contiene il parametro ``request_uri`` (:rfc:`9126`).
    7. DEVE verificare che il `Request Object` contenga tutti i parametri obbligatori i cui valori sono validati secondo la :ref:`Tabella dei parametri HTTP <table_request_object_claim>` [derivata da :rfc:`9126`].
    8. DEVE verificare che il `Request Object` non sia scaduto, controllando il claim ``exp``.
    9. DEVE verificare che il `Request Object` sia stato emesso in un momento precedente al valore esposto nel claim ``iat``. DOVREBBE rifiutare la richiesta se il claim ``iat`` è lontano dall'ora corrente (:rfc:`9126`) di più di `5` minuti.
    10. DEVE verificare che il claim ``jti`` nel `Request Object` non sia stato utilizzato in precedenza dall'Istanza del Wallet identificata dal ``client_id``. Ciò consente al Credential Issuer di mitigare gli attacchi di replay (:rfc:`7519`).
    11. DEVE validare il parametro ``OAuth-Client-Attestation-PoP`` in base alla Sezione 4 di [`OAUTH-ATTESTATION-CLIENT-AUTH`_].

Di seguito un esempio non normativo di `PAR Request`.

.. code-block:: http

    POST /as/par HTTP/1.1
    Host: eaa-provider.example.org
    Content-Type: application/x-www-form-urlencoded
    OAuth-Client-Attestation: eyJhbGciOiJFUzI1NiIsImtpZCI6IjBiNDk4ZGRlMDkxNzJhZGE3MDFkMDdlYjZmOTg2N2FkIiwidHlwIjoid2FsbGV0LWF0dGVzdGF0aW9uK2p3dCJ9.eyJpc3MiOiJodHRwczovL3dhbGxldC1wcm92aWRlci5leGFtcGxlLm9yZyIsInN1YiI6InZiZVhKa3NNNDV4cGh0QU5uQ2lHNm1DeXVVNGpmR056b3BHdUt2b2dnOWMiLCJhYWwiOiJodHRwczovL3RydXN0LWxpc3QuZXUvYWFsL2hpZ2giLCJjbmYiOnsiandrIjp7ImNydiI6IlAtMjU2Iiwia3R5IjoiRUMiLCJ4IjoiNEhOcHRJLXhyMnBqeVJKS0dNbno0V21kblFEX3VKU3E0Ujk1Tmo5OGI0NCIsInkiOiJMSVpuU0IzOXZGSmhZZ1MzazdqWEU0cjMtQ29HRlF3WnRQQklScXBObHJnIn19LCJhdXRob3JpemF0aW9uX2VuZHBvaW50IjoiaHR0cHM6Ly93YWxsZXQtc29sdXRpb24uZGlnaXRhbC1zdHJhdGVneS5ldXJvcGEuZXUvYXV0aG9yaXphdGlvbiIsInJlc3BvbnNlX3R5cGVzX3N1cHBvcnRlZCI6WyJ2cF90b2tlbiJdLCJyZXNwb25zZV9tb2Rlc19zdXBwb3J0ZWQiOlsiZm9ybV9wb3N0Lmp3dCJdLCJ2cF9mb3JtYXRzX3N1cHBvcnRlZCI6eyJkYytzZC1qd3QiOnsic2Qtand0X2FsZ192YWx1ZXMiOlsiRVMyNTYiLCJFUzM4NCJdfX0sInJlcXVlc3Rfb2JqZWN0X3NpZ25pbmdfYWxnX3ZhbHVlc19zdXBwb3J0ZWQiOlsiRVMyNTYiXSwicHJlc2VudGF0aW9uX2RlZmluaXRpb25fdXJpX3N1cHBvcnRlZCI6ZmFsc2UsImNsaWVudF9pZF9zY2hlbWVzX3N1cHBvcnRlZCI6WyJlbnRpdHlfaWQiXSwiaWF0IjoxNzQwMTU4MDQ3LCJleHAiOjE3NDAxNTgxNjd9.paU3FOET8nraQxuesBXD9gw57DL5HfDzkeboKAOinyh5L2MmLwqvRtrSWK8S7qMRWYmdzR-gHMpmebIH7gGE5w
    OAuth-Client-Attestation-PoP: eyJhbGciOiJFUzI1NiIsInR5cCI6Im9hdXRoLWNsaWVudC1hdHRlc3RhdGlvbi1wb3Arand0In0.eyJpc3MiOiIgaHR0cHM6Ly9jbGllbnQuZXhhbXBsZS5jb20iLCJhdWQiOiJodHRwczovL2FzLmV4YW1wbGUuY29tIiwianRpIjoiZDI1ZDAwYWItNTUyYi00NmZjLWFlMTktOThmNDQwZjI1MDY0IiwiaWF0IjoxNzQwMTU4NjE3LCJleHAiOjE3NDAxNTg3Mzd9.B0KOkGi9vMxf3H2Y8rrF-mdLNsuluTvAUbjFfL1Hi-gdaPW7-8ziS9uVh7aTnSAHKWzMfkZLv5q-bxhkglR4PA

    client_id=$thumprint-of-the-jwk-in-the-cnf-wallet-attestation$&
    request=$SIGNED-JWT

Di seguito un esempio non normativo dell'header e del body della prova di possesso dell'Attestato di Unità di Wallet (WIA-PoP):

.. literalinclude:: ../../examples/wa-pop-header.json
  :language: JSON

.. literalinclude:: ../../examples/wa-pop-payload.json
  :language: JSON


Di seguito un esempio non normativo del `Request Object` firmato senza codifica e firma applicata:

.. literalinclude:: ../../examples/request-object-header.json
  :language: JSON

.. literalinclude:: ../../examples/request-object-payload.json
  :language: JSON


.. note::
  **Controllo della Federazione**: Il Credential Issuer DEVE verificare che il Fornitore di Wallet faccia parte della federazione.


.. note::
  Il Credential Issuer DEVE validare la firma dell'Attestato di Unità di Wallet e che non sia scaduto.

**Passo 3 (`PAR Response`)**: Il Credential Issuer fornisce un valore ``request_uri`` monouso. Il valore ``request_uri`` emesso DEVE essere vincolato all'identificativo del client (``client_id``) che è stato fornito nel `Request Object`.


.. note::
  L'entropia del ``request_uri`` DEVE essere sufficientemente grande. L'adeguata brevità della validità e l'entropia del ``request_uri`` dipendono dal calcolo del rischio basato sul valore della risorsa protetta. Il tempo di validità DOVREBBE essere inferiore a un minuto e il ``request_uri`` DEVE includere un valore casuale crittografico di 128 bit o più (:rfc:`9101`). L'intero ``request_uri`` NON DOVREBBE superare i 512 caratteri ASCII per i seguenti due motivi principali (:rfc:`9101`):

    1. Molti telefoni sul mercato ancora non accettano payload di grandi dimensioni. La restrizione è tipicamente di 512 o 1024 caratteri ASCII.
    2. Su una connessione lenta come una connessione mobile 2G, un URL grande causerebbe una risposta lenta; pertanto, l'uso di tale URL non è consigliabile dal punto di vista dell'esperienza utente.

Il Credential Issuer restituisce il ``request_uri`` emesso all'Istanza del Wallet. Un esempio non normativo della risposta è mostrato di seguito.

.. code-block:: http

  HTTP/1.1 201 Created
  Cache-Control: no-cache, no-store
  Content-Type: application/json

.. literalinclude:: ../../examples/par-response.json
  :language: JSON

**Passi 4-5 (`Authorization Request`)**: L'Istanza del Wallet invia una richiesta di autorizzazione all'Authorization Endpoint del Credential Issuer. Poiché parti del contenuto di questa `Authorization Request`, ad esempio il valore del parametro ``code_challenge``, sono unici per una particolare `Authorization Request`, l'Istanza del Wallet DEVE utilizzare un valore ``request_uri`` una sola volta (:rfc:`9126`). Il Credential Issuer esegue i seguenti controlli alla ricezione della `Authorization Request`:

    1. DEVE trattare i valori ``request_uri`` come monouso e DEVE rifiutare una richiesta scaduta. Tuttavia, PUÒ consentire richieste duplicate causate da un Utente che ricarica/aggiorna il proprio user-agent (derivato da :rfc:`9126`).
    2. DEVE identificare la richiesta come risultato del PAR inviato (derivato da :rfc:`9126`).
    3. DEVE rifiutare tutte le `Authorization Request` che non contengono il parametro ``request_uri``, poiché il PAR è l'unico modo per passare la `Authorization Request` dall'Istanza del Wallet (derivato da :rfc:`9126`).


.. code-block:: http

    GET /authorize?client_id=$thumprint-of-the-jwk-in-the-cnf-wallet-attestation$&request_uri=urn%3Aietf%3Aparams%3Aoauth%3Arequest_uri%3Abwc4JK-ESC0w8acc191e-Y1LTC2 HTTP/1.1
    Host: eaa-provider.example.org


.. note::
   **Autenticazione dell'Utente e Consenso**: Il PID Provider esegue l'autenticazione dell'Utente basata sullo schema CieID con Livello di Garanzia Alto (CIE L3) e richiede il consenso dell'Utente per l'emissione del PID.
   Il (Q)EAA Provider esegue l'autenticazione dell'Utente richiedendo un PID valido all'Istanza del Wallet. Il (Q)EAA Provider DEVE utilizzare [`OpenID4VP`_] per richiedere la presentazione del PID. In questa circostanza, il (Q)EAA Provider agisce come una Relying Party, fornendo la richiesta di presentazione all'Istanza del Wallet. L'Istanza del Wallet DEVE avere un PID valido, ottenuto in precedenza, per avviare la transazione con il (Q)EAA Provider. Durante questo passaggio, i Credential Issuer POSSONO chiedere i dettagli di contatto dell'Utente (ad esempio, il loro indirizzo email) per inviare notifiche sugli Attestati Elettronici emessi.



**Passi 6-7 (`Authorization Response`)**: Il Credential Issuer invia un ``code`` di autorizzazione insieme ai parametri ``state`` e ``iss`` all'Istanza del Wallet. L'Istanza del Wallet esegue i seguenti controlli sulla `Authorization Response`:

    1. DEVE verificare che la `Authorization Response` contenga tutti i parametri definiti secondo la :ref:`Tabella dei parametri della Risposta HTTP <table_http_response_claim>`.
    2. DEVE verificare che il valore restituito dal Credential Issuer per il parametro ``state`` sia uguale al valore inviato dall'Istanza del Wallet nel `Request Object` (:rfc:`6749`).
    3. DEVE verificare che l'URL del Credential Issuer nel parametro ``iss`` sia uguale all'identificativo URL previsto del Credential Issuer con cui l'Istanza del Wallet ha iniziato la comunicazione (:rfc:`9027`).

.. note::
    L'URI di reindirizzamento dell'Istanza del Wallet è un `universal link` o `app link`` registrato con il sistema operativo locale, quindi quest'ultimo lo risolverà e passerà la risposta all'Istanza del Wallet.

.. code-block:: http

    HTTP/1.1 302 Found
    Location: https://start.wallet.example.org?code=SplxlOBeZQQYbYS6WxSbIA&state=fyZiOL9Lf2CeKuNT2JzxiLRDink0uPcd&iss=https%3A%2F%2Feaa-provider.example.org

**Passi 8-9 (`DPoP Proof` per il Token Endpoint)**: L'Istanza del Wallet DEVE creare una nuova coppia di chiavi e un nuovo JWT di `DPoP proof` seguendo le istruzioni fornite nella Sezione 4 di (:rfc:`9449`) per la richiesta di token al Credential Issuer. Il JWT di `DPoP proof` è firmato utilizzando la chiave privata per DPoP creata dall'Istanza del Wallet per questo scopo. DPoP associa l'Access Token, e opzionalmente il Refresh Token, a una determinata Istanza del Wallet (:rfc:`9449`) e mitiga l'uso improprio di token persi o rubati al Credential Endpoint.

**Passo 10 (`Token Request`):** L'Istanza del Wallet invia una richiesta di token al Token Endpoint del Credential Issuer con un JWT di *DPoP proof* e i parametri: ``code``, ``code_verifier`` e OAuth 2.0 Attestation based Client Authentication (``OAuth-Client-Attestation`` e ``OAuth-Client-Attestation-PoP``).

L'``OAuth-Client-Attestation`` è firmato utilizzando la chiave privata associata all'Istanza del Wallet. La relativa chiave pubblica attestata dal Fornitore di Wallet è fornita all'interno dell'Attestato di Unità di Wallet (claim ``cnf.jwk``). Il Credential Issuer esegue i seguenti controlli sulla `Token Request`:

   1. DEVE assicurarsi che il ``code`` di autorizzazione sia emesso per l'Istanza del Wallet autenticata (:rfc:`6749`) e non sia stato replicato.
   2. DEVE assicurarsi che il ``code`` di autorizzazione sia valido e non sia stato utilizzato in precedenza (:rfc:`6749`).
   3. DEVE assicurarsi che il ``redirect_uri`` corrisponda al valore incluso nel precedente `Request Object` (vedi Sezione 3.1.3.1. di [`OIDC`_]).
   4. DEVE validare il JWT di `DPoP proof`, secondo la Sezione 4.3 di (:rfc:`9449`).

.. code-block:: http

    POST /token HTTP/1.1
    Host: eaa-provider.example.org
    Content-Type: application/x-www-form-urlencoded
    DPoP: eyJ0eXAiOiJkcG9wK2p3dCIsImFsZyI6IkVTMjU2IiwiandrIjp7Imt0eSI6IkVDIiwieCI6IjR2dDhNdEFISmlsMzBDNnpUTmt2c0VVcnlHTEUtQW5BNkc5LV8xa3l5Rk0iLCJ5IjoiTWdiNTFfbjNSRjNtbHNtS3dMd0xtRUFqVmlJM3Q1bTVWNTI2MFA5MzR3RSIsImNydiI6IlAtMjU2In19.eyJqdGkiOiItQndDM0VTYzZhY2MybFRjIiwiaHRtIjoiR0VUIiwiaHR1IjoiaHR0cHM6Ly9yZXNvdXJjZS5leGFtcGxlLm9yZy9wcm90ZWN0ZWRyZXNvdXJjZSIsImlhdCI6MTU2MjI2MjYxOH0.3Tp1ZlZ05PQYeZUHhiZwaQ1etqnwYwoiJHFR_JHb32381lMJL-8o2rE3VZ8X3yuqrGFfCVeP90Ln4J5r8ASIBg
    OAuth-Client-Attestation: eyJhbGciOiJFUzI1NiIsImtpZCI6IjBiNDk4ZGRlMDkxNzJhZGE3MDFkMDdlYjZmOTg2N2FkIiwidHlwIjoid2FsbGV0LWF0dGVzdGF0aW9uK2p3dCJ9.eyJpc3MiOiJodHRwczovL3dhbGxldC1wcm92aWRlci5leGFtcGxlLm9yZyIsInN1YiI6InZiZVhKa3NNNDV4cGh0QU5uQ2lHNm1DeXVVNGpmR056b3BHdUt2b2dnOWMiLCJhYWwiOiJodHRwczovL3RydXN0LWxpc3QuZXUvYWFsL2hpZ2giLCJjbmYiOnsiandrIjp7ImNydiI6IlAtMjU2Iiwia3R5IjoiRUMiLCJ4IjoiNEhOcHRJLXhyMnBqeVJKS0dNbno0V21kblFEX3VKU3E0Ujk1Tmo5OGI0NCIsInkiOiJMSVpuU0IzOXZGSmhZZ1MzazdqWEU0cjMtQ29HRlF3WnRQQklScXBObHJnIn19LCJhdXRob3JpemF0aW9uX2VuZHBvaW50IjoiaHR0cHM6Ly93YWxsZXQtc29sdXRpb24uZGlnaXRhbC1zdHJhdGVneS5ldXJvcGEuZXUvYXV0aG9yaXphdGlvbiIsInJlc3BvbnNlX3R5cGVzX3N1cHBvcnRlZCI6WyJ2cF90b2tlbiJdLCJyZXNwb25zZV9tb2Rlc19zdXBwb3J0ZWQiOlsiZm9ybV9wb3N0Lmp3dCJdLCJ2cF9mb3JtYXRzX3N1cHBvcnRlZCI6eyJkYytzZC1qd3QiOnsic2Qtand0X2FsZ192YWx1ZXMiOlsiRVMyNTYiLCJFUzM4NCJdfX0sInJlcXVlc3Rfb2JqZWN0X3NpZ25pbmdfYWxnX3ZhbHVlc19zdXBwb3J0ZWQiOlsiRVMyNTYiXSwicHJlc2VudGF0aW9uX2RlZmluaXRpb25fdXJpX3N1cHBvcnRlZCI6ZmFsc2UsImNsaWVudF9pZF9zY2hlbWVzX3N1cHBvcnRlZCI6WyJlbnRpdHlfaWQiXSwiaWF0IjoxNzQwMTU4MDQ3LCJleHAiOjE3NDAxNTgxNjd9.paU3FOET8nraQxuesBXD9gw57DL5HfDzkeboKAOinyh5L2MmLwqvRtrSWK8S7qMRWYmdzR-gHMpmebIH7gGE5w
    OAuth-Client-Attestation-PoP: eyJhbGciOiJFUzI1NiIsInR5cCI6Im9hdXRoLWNsaWVudC1hdHRlc3RhdGlvbi1wb3Arand0In0.eyJpc3MiOiIgaHR0cHM6Ly9jbGllbnQuZXhhbXBsZS5jb20iLCJhdWQiOiJodHRwczovL2FzLmV4YW1wbGUuY29tIiwianRpIjoiZDI1ZDAwYWItNTUyYi00NmZjLWFlMTktOThmNDQwZjI1MDY0IiwiaWF0IjoxNzQwMTU4NjE3LCJleHAiOjE3NDAxNTg3Mzd9.B0KOkGi9vMxf3H2Y8rrF-mdLNsuluTvAUbjFfL1Hi-gdaPW7-8ziS9uVh7aTnSAHKWzMfkZLv5q-bxhkglR4PA

    grant_type=authorization_code
    &code=SplxlOBeZQQYbYS6WxSbIA
    &code_verifier=dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk
    &redirect_uri=https://start.wallet.example.org/cb

**Passo 11 (`Token Response`)**: Il Credential Issuer valida la richiesta. In caso di successo, l'Issuer fornisce all'Istanza del Wallet un Access Token e, opzionalmente, un Refresh Token, entrambi associati alla chiave DPoP.

.. code-block:: http

    HTTP/1.1 200 OK
    Content-Type: application/json
    Cache-Control: no-store

.. literalinclude:: ../../examples/token-response.json
  :language: JSON

Un esempio non normativo dell'Access Token DPoP è fornito di seguito.

.. literalinclude:: ../../examples/at-dpop-header.json
  :language: JSON

.. literalinclude:: ../../examples/at-dpop-payload.json
  :language: JSON

Un esempio non normativo del Refresh Token DPoP è fornito di seguito.

.. literalinclude:: ../../examples/rt-dpop-header.json
  :language: JSON

.. literalinclude:: ../../examples/rt-dpop-payload.json
  :language: JSON

**Passo 12 (`Nonce Request`)**: Secondo la Sezione 7.1 di [`OpenID4VCI`_], l'Istanza del Wallet invia una richiesta HTTP POST al Nonce Endpoint per ottenere un nuovo ``c_nonce`` che può essere utilizzato per creare la prova di possesso del materiale crittografico per la successiva richiesta al Credential Endpoint.

Di seguito è riportato un esempio non normativo di una `Nonce Request`:

.. code-block:: http

    POST /nonce HTTP/1.1
    Host: eaa-provider.example.org
    Content-Length: 0

**Passo 13 (`Nonce Response`)**: Il Credential Issuer fornisce il ``c_nonce`` all'Istanza del Wallet. Il parametro ``c_nonce`` è una stringa, che DEVE essere imprevedibile e viene utilizzata successivamente dall'Istanza del Wallet nel Passo 16 per creare la prova di possesso della chiave (claim ``proof``) ed è la principale contromisura contro l'attacco di replay della prova della chiave.
Si noti che il valore ``c_nonce`` ricevuto può essere utilizzato per creare la prova finché l'Issuer
fornisce all'Istanza del Wallet un nuovo valore ``c_nonce``.

Di seguito è riportato un esempio non normativo di una `Nonce Response`:

.. code-block:: http

    HTTP/1.1 200 OK
    Content-Type: application/json
    Cache-Control: no-store

.. literalinclude:: ../../examples/nonce-response.json
  :language: JSON


**Passi 14-15 (`DPoP Proof` per il Credential Endpoint)**: Per richiedere l'Attestato Elettronico, l'Istanza del Wallet crea una prova di possesso con ``c_nonce`` ottenuto nel **Passo 13** e utilizzando la chiave privata utilizzata per il DPoP, firmando un JWT di `DPoP proof` secondo la Sezione 4 di (:rfc:`9449`). Il valore ``jwk`` nel parametro ``proof`` DEVE essere uguale alla chiave pubblica referenziata nel DPoP.

**Passo 16 (`Credential Request`)**: L'Istanza del Wallet invia una richiesta per l'Attestato Elettronico al Credential Endpoint. Questa richiesta DEVE includere l'Access Token, il JWT di `DPoP proof`, il tipo di Attestato Elettronico, la prova (che dimostra il possesso del materiale crittografico). Il parametro ``proof`` DEVE essere un oggetto che contiene la prova di possesso del materiale crittografico a cui sarà associato l'Attestato Elettronico emesso. Per verificare la prova, il Credential Issuer conduce i seguenti controlli al Credential Endpoint:

 1. La prova JWT DEVE includere tutti i claim richiesti come specificato nella tabella della Sezione :ref:`credential-issuance-endpoint:Token Request`.
 2. La prova della chiave DEVE essere esplicitamente tipizzata utilizzando i parametri dell'header come definito per il rispettivo tipo di prova.
 3. Il parametro dell'header ``alg`` DEVE indicare un algoritmo di firma digitale asimmetrica registrato e NON DEVE essere impostato su `none`.
 4. La firma sulla prova della chiave DEVE essere verificata utilizzando la chiave pubblica specificata nel parametro dell'header.
 5. Il parametro dell'header NON DEVE contenere una chiave privata.
 6. Se un valore ``c_nonce`` è stato precedentemente fornito dal server, il claim ``nonce`` nel JWT DEVE corrispondere a questo valore ``c_nonce``. Inoltre, l'istante di creazione del JWT, come indicato dal claim ``iat`` o da un timestamp gestito dal server tramite il claim ``nonce``, DEVE essere all'interno di una finestra temporale accettabile come determinato dal server.


.. note::
  Il Credential Issuer DEVE registrare tutti gli Attestati Elettronici emessi per la loro successiva revoca, se necessario.


.. note::
  È RACCOMANDATO che la chiave pubblica contenuta nel ``jwt_proof`` sia generata specificamente per l'Attestato Elettronico richiesto (nuova chiave crittografica) per garantire che diversi Attestati Elettronici emessi non condividano la stessa chiave pubblica, rimanendo così non collegabili tra loro.


Un esempio non normativo della `Credential Request` è fornito di seguito.


.. code-block:: http

  POST /credential HTTP/1.1
    Host: eaa-provider.example.org
  Content-Type: application/json
  Authorization: DPoP Kz~8mXK1EalYznwH-LC-1fBAo.4Ljp~zsPE_NeO.gxU
  DPoP: eyJ0eXAiOiJkcG9wK2p3dCIsImFsZyI6IkVTMjU2IiwiandrIjp7Imt0eSI6Ik
      VDIiwieCI6Imw4dEZyaHgtMzR0VjNoUklDUkRZOXpDa0RscEJoRjQyVVFVZldWQVdCR
      nMiLCJ5IjoiOVZFNGpmX09rX282NHpiVFRsY3VOSmFqSG10NnY5VERWclUwQ2R2R
      1JEQSIsImNydiI6IlAtMjU2In19.eyJqdGkiOiJlMWozVl9iS2ljOC1MQUVCIiwiaHRtIj
      oiR0VUIiwiaHR1IjoiaHR0cHM6Ly9yZXNvdXJjZS5leGFtcGxlLm9yZy9wcm90ZWN0Z
      WRyZXNvdXJjZSIsImlhdCI6MTU2MjI2MjYxOCwiYXRoIjoiZlVIeU8ycjJaM0RaNTNF
      c05yV0JiMHhXWG9hTnk1OUlpS0NBcWtzbVFFbyJ9.2oW9RP35yRqzhrtNP86L-Ey71E
      OptxRimPPToA1plemAgR6pxHF8y6-yqyVnmcw6Fy1dqd-jfxSYoMxhAJpLjA

.. literalinclude:: ../../examples/credential-request.json
  :language: JSON

Dove un esempio non normativo del contenuto decodificato del parametro ``jwt`` è rappresentato di seguito, senza codifica e firma.

.. literalinclude:: ../../examples/credential-jwt-proof-header.json
  :language: JSON

.. literalinclude:: ../../examples/credential-jwt-proof-payload.json
  :language: JSON

**Passi 17-21 (`Credential Response`)**: Il Credential Issuer DEVE validare il JWT di *DPoP proof* in base ai passaggi definiti nella Sezione 4.3 di (:rfc:`9449`) e se l'Access Token è valido e adatto per l'Attestato Elettronico richiesto. Il Credential Issuer DEVE validare la prova di possesso per il materiale crittografico a cui il nuovo Attestato Elettronico DEVE essere vincolato, secondo la Sezione 8.2.2 di `OpenID4VCI`_. Se tutti i controlli hanno successo, il Credential Issuer crea un nuovo Attestato Elettronico vincolato al materiale crittografico e lo fornisce all'Istanza del Wallet. L'Istanza del Wallet DEVE eseguire i seguenti controlli prima di procedere con l'archiviazione sicura dell'Attestato Elettronico:

    1. DEVE verificare che il PID/(Q)EAA contenuto nella `Credential Response` contenga tutti i parametri obbligatori e i valori siano validati secondo la :ref:`Tabella dei parametri della Credential Response <table_credential_response_claim>`.
    2. DEVE verificare l'integrità dell'Attestato Elettronico verificando la firma utilizzando l'algoritmo specificato nel parametro dell'header ``alg`` di SD-JWT (:ref:`credential-data-model:Modello di Dati degli Attestati Elettronici`) e la chiave pubblica che è identificata utilizzando l'header ``kid`` dell'SD-JWT.
    3. DEVE verificare che l'Attestato Elettronico ricevuto (nel claim ``credential``) corrisponda al tipo di Attestato Elettronico richiesto e sia conforme allo schema specifico di quell'Attestato Elettronico definito in :ref:`credential-data-model:Modello di Dati degli Attestati Elettronici`.
    4. DEVE elaborare e verificare l'Attestato Elettronico nel formato SD-JWT VC (secondo la Sezione 5 di `SD-JWT`_) o nel formato mdoc-CBOR.
    5. DEVE verificare la Trust Chain nell'header dell'SD-JWT VC per verificare che il Credential Issuer sia affidabile.

Se i controlli sopra hanno successo, l'Istanza del Wallet richiede il consenso dell'Utente per memorizzare l'Attestato Elettronico. Dopo aver ricevuto il consenso, l'Istanza del Wallet memorizza in modo sicuro l'Attestato Elettronico.

Di seguito è riportato un esempio non normativo di una risposta di successo contenente un Attestato Elettronico nel formato SD-JWT VC.

.. code-block:: http

    HTTP/1.1 200 OK
    Content-Type: application/json
    Cache-Control: no-store
    Pragma: no-cache

.. literalinclude:: ../../examples/sd-jwt-credential-response.json
  :language: JSON

Di seguito è riportato un esempio non normativo di una risposta di successo contenente un Attestato Elettronico nel formato mdoc.

.. code-block:: http

    HTTP/1.1 200 OK
    Content-Type: application/json
    Cache-Control: no-store
    Pragma: no-cache

.. literalinclude:: ../../examples/mdoc-credential-response.json
  :language: JSON


.. note::
  Se l'Attestato Elettronico richiesto non può essere emesso immediatamente e richiede più tempo, il Credential Issuer DOVREBBE supportare il Deferred Flow (Passo 24) come specificato nella Sezione :ref:`credential-issuance-endpoint:Deferred Endpoint`.

**Passo 22 (`Notification Request`)**: Secondo la Sezione 10.1 di [`OpenID4VCI`_], il Wallet invia una richiesta HTTP POST al Notification Endpoint utilizzando il tipo di media *application/json*, come nel seguente esempio non normativo.

.. code-block:: http

  POST /notification HTTP/1.1
  Host: eaa-provider.example.org
  Content-Type: application/json
  Authorization: DPoP Kz~8mXK1EalYznwH-LC-1fBAo.4Ljp~zsPE_NeO.gxU
  DPoP: eyJ0eXAiOiJkcG9wK2p3dCIsImFsZyI6IkVTMjU2IiwiandrIjp7Imt0eSI6Ik
      VDIiwieCI6Imw4dEZyaHgtMzR0VjNoUklDUkRZOXpDa0RscEJoRjQyVVFVZldWQVdCR
      nMiLCJ5IjoiOVZFNGpmX09rX282NHpiVFRsY3VOSmFqSG10NnY5VERWclUwQ2R2R
      1JEQSIsImNydiI6IlAtMjU2In19.eyJqdGkiOiJlMWozVl9iS2ljOC1MQUVCIiwiaHRtIj
      oiR0VUIiwiaHR1IjoiaHR0cHM6Ly9yZXNvdXJjZS5leGFtcGxlLm9yZy9wcm90ZWN0Z
      WRyZXNvdXJjZSIsImlhdCI6MTU2MjI2MjYxOCwiYXRoIjoiZlVIeU8ycjJaM0RaNTNF
      c05yV0JiMHhXWG9hTnk1OUlpS0NBcWtzbVFFbyJ9.2oW9RP35yRqzhrtNP86L-Ey71E
      OptxRimPPToA1plemAgR6pxHF8y6-yqyVnmcw6Fy1dqd-jfxSYoMxhAJpLjA
.. literalinclude:: ../../examples/notification-request.json
  :language: JSON


**Passo 23 (`Notification Response`)**: Quando il Credential Issuer ha ricevuto con successo la `Notification Request` dal Wallet, DEVE rispondere con un codice di stato HTTP *204* come raccomandato nella Sezione 10.2 di [`OpenID4VCI`_]. Di seguito è riportato un esempio non normativo di risposta a una `Notification Request` riuscita:

.. code-block:: http

  HTTP/1.1 204 No Content


Refresh Token Flow
-------------------

Per utilizzare gli Endpoint Deferred, Credential Request e Notification, l'Istanza del Wallet DEVE presentare un Access Token DPoP valido al Credential Issuer. Tuttavia, quando questi endpoint sono utilizzati nel Deferred Flow, per la riemissione o la notifica dell'eliminazione di un Attestato Elettronico, l'Access Token potrebbe scadere, poiché è progettato per avere una breve durata e queste azioni POSSONO verificarsi giorni dopo. Per affrontare questo problema, la specifica RACCOMANDA l'uso dei Refresh Token.

Un Access Token ottenuto come risultato di un Refresh Token Flow DEVE essere limitato al:

  - Deferred Endpoint, per ottenere un nuovo Attestato Elettronico dopo il tempo impostato nel parametro ``lead_time`` o quando viene notificato come pronto per essere emesso;
  - Notification Endpoint, per notificare l'eliminazione di un Attestato Elettronico al Credential Issuer;
  - Credential Endpoint, per aggiornare un Attestato Elettronico che è già presente nell'Istanza del Wallet (chiamato anche riemissione dell'Attestato Elettronico, vedi sezione :ref:`credential-issuance-low-level:Re-issuance Flow`).

Per mitigare l'impatto di un Refresh Token rubato, i Refresh Token DEVONO essere DPoP. Questi aspetti sono dettagliati e discussi nella Sezione :ref:`credential-issuance-low-level:Considerazioni di Sicurezza`.

La figura seguente mostra come ottenere un nuovo Access Token DPoP e un nuovo Refresh Token DPoP dal Token Endpoint.

.. _fig_refresh_token_flow:
.. plantuml:: plantuml/pid-issuance-high-level-flow.puml
    :width: 99%
    :alt: La figura illustra il Refresh Token Flow.
    :caption: `Refresh Token Flow. <https://www.plantuml.com/plantuml/svg/TPBDQkim48NtUef3xYQ1cEpleYIaXMRLK0BP588gZ-EXpiYLnhXz-yfoJ1jAbvwVpzySj8vgWtQNnjXElNINLmh6jAd6ZbihYjdHDWqfTf96nT4CDgA_7Ta6AacKRODTZ1s5FCJ6z2ZkqEC_pYGKh1BkztwFDdXVmKg9uwOO2fKF-0M1-ZSIa9IjPz4hZHFja1lFzDvHLFIizK_k_4M0Sx2Y9_riQJby1ge2nVgKaGkaKjvwsdHQ5zk6IRJOg2QSLVQItVvgPcCMQ4seoPP3OZmTEgd5raiapArp5EFut-Mjnd8yS9G4VRISUYUMXJ6rU2LO5toC-7Tyt1qU4hecL8tluRmeIxfzFC8YN9DGdwLAgYW4AbU9mXMxRBrot_bEaKun34j2_HZYQ3owcNKQJQ_Z2m00>`_

.. note::
  L'aggiornamento di un Token può essere attivato da diverse azioni (ad esempio, l'eliminazione di un Attestato Elettronico da parte dell'Utente). In ogni caso, si suppone che le Istanze del Wallet siano in esecuzione e che il relativo materiale crittografico sia sbloccato.

**Passo 1**: L'Istanza del Wallet DEVE creare un nuovo JWT di `DPoP proof` e una nuova prova di possesso dell'Attestato di Unità di Wallet per la richiesta di token del Credential Issuer.

**Passo 2**: Per aggiornare un Access Token vincolato a DPoP, l'Istanza del Wallet invia una richiesta di token utilizzando il parametro ``grant_type`` impostato su ``refresh_token``, includendo l'header DPoP e gli header di OAuth Client Attestation.
Un esempio non normativo della richiesta di token per un Access Token DPoP utilizzando un Refresh Token è mostrato di seguito.

.. code::

  POST /token HTTP/1.1
  Host: eaa-provider.example.org
  Content-Type: application/x-www-form-urlencoded
  DPoP: eyJ0eXAiOiJkcG9wK2p3dCIsImFsZyI6IkVTMjU2IiwiandrIjp7Imt0eSI6IkVDIiwieCI6IjR2dDhNdEFISmlsMzBDNnpUTmt2c0VVcnlHTEUtQW5BNkc5LV8xa3l5Rk0iLCJ5IjoiTWdiNTFfbjNSRjNtbHNtS3dMd0xtRUFqVmlJM3Q1bTVWNTI2MFA5MzR3RSIsImNydiI6IlAtMjU2In19.eyJqdGkiOiItQndDM0VTYzZhY2MybFRjIiwiaHRtIjoiR0VUIiwiaHR1IjoiaHR0cHM6Ly9yZXNvdXJjZS5leGFtcGxlLm9yZy9wcm90ZWN0ZWRyZXNvdXJjZSIsImlhdCI6MTU2MjI2MjYxOH0.3Tp1ZlZ05PQYeZUHhiZwaQ1etqnwYwoiJHFR_JHb32381lMJL-8o2rE3VZ8X3yuqrGFfCVeP90Ln4J5r8ASIBg
  OAuth-Client-Attestation: eyJhbGciOiJFUzI1NiIsImtpZCI6IjBiNDk4ZGRlMDkxNzJhZGE3MDFkMDdlYjZmOTg2N2FkIiwidHlwIjoid2FsbGV0LWF0dGVzdGF0aW9uK2p3dCJ9.eyJpc3MiOiJodHRwczovL3dhbGxldC1wcm92aWRlci5leGFtcGxlLm9yZyIsInN1YiI6InZiZVhKa3NNNDV4cGh0QU5uQ2lHNm1DeXVVNGpmR056b3BHdUt2b2dnOWMiLCJhYWwiOiJodHRwczovL3RydXN0LWxpc3QuZXUvYWFsL2hpZ2giLCJjbmYiOnsiandrIjp7ImNydiI6IlAtMjU2Iiwia3R5IjoiRUMiLCJ4IjoiNEhOcHRJLXhyMnBqeVJKS0dNbno0V21kblFEX3VKU3E0Ujk1Tmo5OGI0NCIsInkiOiJMSVpuU0IzOXZGSmhZZ1MzazdqWEU0cjMtQ29HRlF3WnRQQklScXBObHJnIn19LCJhdXRob3JpemF0aW9uX2VuZHBvaW50IjoiaHR0cHM6Ly93YWxsZXQtc29sdXRpb24uZGlnaXRhbC1zdHJhdGVneS5ldXJvcGEuZXUvYXV0aG9yaXphdGlvbiIsInJlc3BvbnNlX3R5cGVzX3N1cHBvcnRlZCI6WyJ2cF90b2tlbiJdLCJyZXNwb25zZV9tb2Rlc19zdXBwb3J0ZWQiOlsiZm9ybV9wb3N0Lmp3dCJdLCJ2cF9mb3JtYXRzX3N1cHBvcnRlZCI6eyJkYytzZC1qd3QiOnsic2Qtand0X2FsZ192YWx1ZXMiOlsiRVMyNTYiLCJFUzM4NCJdfX0sInJlcXVlc3Rfb2JqZWN0X3NpZ25pbmdfYWxnX3ZhbHVlc19zdXBwb3J0ZWQiOlsiRVMyNTYiXSwicHJlc2VudGF0aW9uX2RlZmluaXRpb25fdXJpX3N1cHBvcnRlZCI6ZmFsc2UsImNsaWVudF9pZF9zY2hlbWVzX3N1cHBvcnRlZCI6WyJlbnRpdHlfaWQiXSwiaWF0IjoxNzQwMTU4MDQ3LCJleHAiOjE3NDAxNTgxNjd9.paU3FOET8nraQxuesBXD9gw57DL5HfDzkeboKAOinyh5L2MmLwqvRtrSWK8S7qMRWYmdzR-gHMpmebIH7gGE5w
  OAuth-Client-Attestation-PoP: eyJhbGciOiJFUzI1NiIsInR5cCI6Im9hdXRoLWNsaWVudC1hdHRlc3RhdGlvbi1wb3Arand0In0.eyJpc3MiOiIgaHR0cHM6Ly9jbGllbnQuZXhhbXBsZS5jb20iLCJhdWQiOiJodHRwczovL2FzLmV4YW1wbGUuY29tIiwianRpIjoiZDI1ZDAwYWItNTUyYi00NmZjLWFlMTktOThmNDQwZjI1MDY0IiwiaWF0IjoxNzQwMTU4NjE3LCJleHAiOjE3NDAxNTg3Mzd9.B0KOkGi9vMxf3H2Y8rrF-mdLNsuluTvAUbjFfL1Hi-gdaPW7-8ziS9uVh7aTnSAHKWzMfkZLv5q-bxhkglR4PA

  grant_type=refresh_token
  &refresh_token=eyJ0eXAiOiJydCtqd3QiLCJhbGciOiJFUzI1NiIsImtpZCI6ImM5NTBjMGU2ZmRlYjVkZTUwYTUwMDk2YjI0N2FmMDNjIn0.eyJpc3MiOiJodHRwczovL2VhYS1wcm92aWRlci53YWxsZXQuaXB6cy5pdCIsImNsaWVudF9pZCI6IjQ3Yjk4MjM2OTc5MWQwODAwM2E3MjgzZjA1OWNiMGQxIiwiYXVkIjoiaHR0cHM6Ly9lYWEtcHJvdmlkZXIud2FsbGV0LmlwenMuaXQiLCJpYXQiOjE3Mzk5NTI5NDgsIm5iZiI6MTczOTk1MzU0OCwiZXhwIjoxNzQyMzcyNzQ4LCJhdGgiOiJmVUh5TzJyMlozRFo1M0VzTnJXQmIweFdYb2FOeTU5SWlLQ0Fxa3NtUUVvIiwianRpIjoiYzY5NTVjZWItYzY1Zi00MDI1LTkzNzgtYjY2NzJiNjE0NWNmIiwiY25mIjp7ImprdCI6Ijk1MTU3NGFlZTFiYjc5MDdhZTFlYzMxMDlkYjJiMjI1In19.qiGM6E-7zci2-3Nnk4OMD7Tv_leUcRPsFsqaBHDHxEEzsGXLNh9qDbLIBk9sujZGVT9xs-28jZhwD6VT-MGTGw

**Passaggio 3**: Il Credential Issuer valida la richiesta sulla base dei seguenti controlli:

  - DEVE validare il parametro OAuth-Client-Attestation-PoP in base alla Sezione 4 di [OAUTH-ATTESTATION-CLIENT-AUTH].
  - DEVE validare il JWT di `DPoP proof`, secondo la Sezione 4.3 di (RFC 9449).
  - DEVE verificare che il Refresh Token non sia scaduto, non sia revocato e sia associato allo stesso set di chiavi DPoP di quelle utilizzate nel JWT di `DPoP proof`.

Se i controlli della richiesta hanno successo, il Credential Issuer genera un nuovo Access Token e un nuovo Refresh Token e questi DEVONO essere entrambi associati alla chiave DPoP. Sia l'Access Token che il Refresh Token vengono quindi inviati all'Istanza del Wallet.

Un esempio non normativo di una risposta di successo è mostrato di seguito.

.. code::

  HTTP/1.1 200 OK
  Content-Type: application/json
  Cache-Control: no-store
  {
      "access_token": "eyJ0eXAiOiJhdCtqd3QiLCJhbGciOiJFU..",
      "refresh_token": "eyC3fiLdCtqd3QiLCJhbGciOiCL3..",
      "token_type": "DPoP",
      "expires_in": 3600,
  }

Se il Refresh Token è scaduto o non valido, il Credential Issuer DEVE emettere un errore, utilizzando il claim `error type` impostato su ``invalid_grant``. Pertanto, per ottenere l'Attestato Elettronico è necessario un flusso di emissione che autentichi l'Utente, come definito nella Sezione :ref:`credential-issuance-low-level:Issuance Flow`.

Considerazioni di Sicurezza
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Per mitigare i rischi di compromissione del Refresh Token, sono richieste le seguenti protezioni:

  - La **riservatezza** dei Refresh Token DEVE essere garantita in transito e archiviazione.
  - Per la trasmissione dei token, DEVONO essere utilizzate connessioni **protette da TLS**.
  - I Refresh Token DEVONO essere **non indovinabili e sicuri da modifiche**.
  - Gli Authorization Server DEVONO implementare il seguente meccanismo per **rilevare gli attacchi di replay**:

    - **Sender-Constrained Tokens**: Vincolare crittograficamente il Refresh Token all'Istanza del Wallet secondo :rfc:`9449`. Gli Access Token e i Refresh Token DEVONO essere vincolati alla stessa chiave DPoP. La `DPoP proof` del Refresh Token è richiesta per aggiornare un Access Token. La stessa chiave DPoP DEVE essere utilizzata per generare le `DPoP proof` dell'Access Token in tutte le `Credential Request`.

  - **Limitazione dell'uso del Refresh Token**: Come specificato in `OPENID4VC-HAIP`_: "Credential Issuers should be mindful of how long the usage of the refresh token is allowed to refresh a Credential, as opposed to starting the issuance flow from the beginning. For example, if the User is trying to refresh a Credential more than a year after its original issuance, the usage of the refresh tokens is NOT RECOMMENDED." In questa specifica, un nuovo Attestato Elettronico ottenuto eseguendo il Re-issuance Flow DOVREBBE avere la stessa scadenza di quello aggiornato. Pertanto, questa specifica non consente l'aggiornamento infinito dell'Attestato Elettronico con un Refresh Token. Una volta che un Attestato Elettronico scade, l'Utente DEVE completare nuovamente l'intero processo di emissione per ottenere un nuovo Attestato Elettronico. Questa specifica raccomanda di impostare una durata di scadenza del Refresh Token, in base alla sensibilità del grant associato.

.. note::
  *Attestati di Unità di Wallet e DPoP di breve durata*: Seguendo la bozza di specifica *OAuth 2.0 Attestation Based Client Authentication* (`OAUTH-ATTESTATION-CLIENT-AUTH`_), l'Authorization Server DEVE associare il Refresh Token alla Client Instance. Per dimostrare questa associazione, la Client Instance DEVE utilizzare il meccanismo di Client Attestation quando aggiorna l'Access Token e la Client Instance DEVE utilizzare la stessa chiave che è stata presentata nel claim ``cnf.jwk`` della Client Attestation che è stata utilizzata quando il Refresh Token è stato emesso. Tuttavia, ciò richiede che tutti le Client Attestation emesse DEVONO essere associati alla stessa chiave, aprendo così a problemi di non collegabilità. In questa specifica, sia `OAUTH-ATTESTATION-CLIENT-AUTH`_ che *OAuth 2.0 Demonstrating Proof of Possession (DPoP)* (:rfc:`9449`) DEVONO essere utilizzati. L'uso di DPoP garantisce l'associazione del Refresh Token con la Client Instance come indicato nella sezione 5 di :rfc:`9449` *"the Refresh Token MUST be bound to the respective public key [...] a Client MUST present a DPoP proof for the same key that was used to obtain the Refresh Token each time that Refresh Token is used to obtain a new Access Token"*. DPoP garantisce che il Refresh Token sia associato all'Istanza del Wallet.


Re-issuance Flow
-----------------

La riemissione comporta la sostituzione degli Attestato Elettronici già memorizzati in un'Istanza del Wallet con nuovi dello stesso tipo di documento. I nuovi Attestati Elettronici DEVONO essere emessi dagli stessi Credential Issuer che hanno originariamente fornito quelli esistenti alla stessa Istanza del Wallet.

Per facilitare questo, in particolare in scenari in cui l'autenticazione dell'Utente non è strettamente richiesta, PUÒ essere utilizzato un Refresh Token Flow (RT) (vedi Sezione :ref:`credential-issuance-low-level:Refresh Token Flow` per maggiori dettagli). Un Access Token ottenuto come risultato di un Refresh Token Flow NON DEVE essere utilizzato per emettere un Attestato Elettronico che non è presente nell'Istanza del Wallet (prima emissione). Il meccanismo del Refresh Token consente la sostituzione automatica degli Attestati Elettronici, semplificando il processo sia per il Credential Issuer che per l'Utente.

Il Re-issuance Flow delineato in questa sezione è limitato ai seguenti scenari:

  - Aggiornamento tecnico del modello/formato dei dati;
  - Aggiornamento dell'insieme di attributi dell'Utente.

Nel primo caso, l'insieme di attributi dell'Utente del nuovo Attestato Elettronico corrisponderà a quello originale. Ad esempio, un Credential Issuer potrebbe dover aggiornare i Metadata dell'Attestato Elettronico o il formato dei dati senza modificare l'insieme di attributi dell'Utente. In questo caso, il coinvolgimento diretto dell'Utente non è obbligatorio per la sostituzione e l'archiviazione di un Attestato Elettronico.

Nel secondo caso, i Credential Issuer potrebbero anche dover modificare uno o più valori degli attributi dell'Utente durante la riemissione. In questo caso, l'Istanza del Wallet DEVE informare l'Utente che l'insieme di dati degli attributi è stato modificato e DEVE quindi richiedere l'autorizzazione dell'Utente per memorizzare il nuovo Attestato Elettronico.

In entrambi i casi, l'Attestato Elettronico appena emesso DEVE avere la stessa data di scadenza di quello precedente.

La riemissione dopo la scadenza dell'Attestato Elettronico DEVE sempre richiedere l'autenticazione dell'Utente.

Il seguente diagramma descrive il Re-issuance Flow dell'Attestato Elettronico.

.. _fig_reissuance_flow:
.. plantuml:: plantuml/credential-reissuance-flow.puml
    :width: 99%
    :alt: La figura illustra il Re-issuance Flow.
    :caption: `Re-issuance Flow. <https://www.plantuml.com/plantuml/svg/ZLHTRnCn47pthnYUQAMqLA9FAOM6faYH2gf2IeLQ5BbtUuc5OmVlNjBowucT3-LYABc7ABPdzcCywmiM7QIUMFNAkCBM9U7TvUcRozDXzzdfYIdUAwKIHZalX616Or5tOtBGw9gH4Mrn6QWa9qPREAAI8HwFX7fQQg6o1HdJDgR7N5DWVEvy1vCheU6ycCeKMentaHqPjqm1DHitWaQWaM6XG2LyBKU-EdhKhaJX9vFQhOd5M3j7zbZ5eB5SfTefYf-IOznfQqdGSopQ5NIcbAbmqAUPN_4d52COdk31uHnVHKlDk3Oi-708YKqVF1CVAYW0xJv9C3IZ1d3WVv93vKE4WCK7AhUQvxEqdxIqL4bQzUbNRI9k7bCuZvcsfan7UMXwCYoS3ZTjnaNiPKla5T4ut9yydRnjOV5x-cEdZVYHPSA1yuTGsFvO_5HXbSPKge5LSPahq66c4ANa_HI8RjfFWaRilqdmWWRdw7tvrhdkTVFkrwHYGnfo8WrB4ctiSLmHZDkWxszlkft1LGkTmQ3V-tWxk1ekTt9jzvIteV3Urx7yRJJHAGfYNjaawPULjFdo-Xh7oy6e0l5ultX0Uw5s43HPdwoVB-_xfNoP7i368ZjxM6RH3excwIM9eungaMSNEJSoJe_8QqQdZdNB-g7OWcPpbDz9ljhyYSyBkZV-1WtnnIEiHcC3ZVNc3-PQdCoxlFPkdDiMVC23-uzBppDF_lk-sd7WY2K9bEJnmVnEwfnjup9NDF34knaoJ_X0iVMivHVya3aYkuECk6_6dQbfTycI4AQ1PiRNtE2eLC35Wb9Fx1y0>`_

**Passo 1**: Il flusso inizia quando l'Utente apre l'Istanza del Wallet: questo passaggio PUÒ essere attivato da una notifica inviata dal Credential Issuer (utilizzando ad esempio uno dei contatti di comunicazione out-of-band registrati durante il flusso di emissione).

**Passo 2**: Indipendentemente dal meccanismo di revoca dell'Attestato Elettronico supportato, se l'Istanza del Wallet.

   - supporta solo Status List e non ha un Token di Stato valido per un Attestato Elettronico memorizzata, l'Istanza del Wallet DEVE recuperarne uno nuovo seguendo il flusso descritto nella Sezione :ref:`credential-revocation:OAuth Status Lists`. Se qualsiasi Attestato Elettronico ha lo stato impostato su ``0x03`` - ``UPDATE`` o ``0x04`` - ``ATTRIBUTE_UPDATE``; oppure
   - insieme al Credential Issuer supporta anche Status Assertion e l'Istanza del Wallet non ha una Status Assertion valida per un Attestato Elettronico memorizzato, l'Istanza del Wallet PUÒ recuperarne una nuova seguendo il flusso descritto nella Sezione :ref:`credential-revocation:OAuth Status Assertions`. Se qualsiasi Attestato Elettronico ha il ``credential_status_type`` impostato su ``INVALID``, l'Istanza del Wallet DEVE verificare il claim ``credential_status_detail.state``. Se questo claim è impostato su ``UPDATE`` o ``ATTRIBUTE_UPDATE``, allora

     l'Istanza del Wallet DEVE verificare se i relativi Access Token sono ancora validi. Se l'Access Token è valido, allora il passaggio 3 PUÒ essere saltato.

**Passo 3**: Se l'Access Token è scaduto e l'Istanza del Wallet ha ancora un Refresh Token valido, l'Istanza del Wallet DEVE ottenere un nuovo Access Token avviando un Refresh Token Flow, secondo la Sezione :ref:`credential-issuance-low-level:Refresh Token Flow`. Il Refresh Token Flow consente all'Istanza del Wallet di ottenere un nuovo Refresh Token e un nuovo Access Token DPoP per aggiornare l'Attestato Elettronico. Se il Refresh Token è scaduto, è necessario un nuovo flusso di emissione che autentichi l'Utente.

**Passo 4**: L'Istanza del Wallet DEVE utilizzare un Access Token DPoP valido per recuperare il nuovo Attestato Elettronico, richiedendolo al Credential Endpoint seguendo i passi da 12 a 22 della Figura 9 nella Sezione :ref:`credential-issuance-low-level:Issuance Flow`. Quando il nuovo Attestato Elettronico è memorizzato con successo nel secure storage, l'Istanza del Wallet DEVE eliminare quella precedente.

.. note::
  Indipendentemente dal meccanismo di revoca dell'Attestato Elettronico supportato, se lo stato dell'Attestato Elettronico è impostato su ``ATTRIBUTE_UPDATE`` (utilizzando la revoca OAuth Status List) o ``credential_status_detail.state`` è impostato su ``ATTRIBUTE_UPDATE`` (utilizzando la revoca OAuth Status List), l'insieme di attributi dell'Utente, nell'Attestato Elettronico aggiornato, non corrisponde a quello nell'Attestato Elettronico memorizzato. In questo caso, l'Istanza del Wallet DEVE richiedere l'autorizzazione dell'Utente per memorizzare il nuovo Attestato Elettronico aggiornato.
  
  Se invece, lo stato dell'Attestato Elettronico è impostato su ``UPDATE`` (utilizzando la revoca OAuth Status List) o ``credential_status_detail.state`` è impostato su ``UPDATE`` (utilizzando la revoca OAuth Status List), solo i parametri dei Metadata dell'Attestato Elettronico sono cambiati. In questo caso, l'Istanza del Wallet DOVREBBE memorizzare il nuovo Attestato Elettronico senza richiedere l'autorizzazione e il consenso espliciti dell'utente.


Re-issuance Flow: Considerazioni di Sicurezza
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Per garantire l'integrità e la sicurezza del Re-issuance Flow, si applicano le seguenti considerazioni di sicurezza.

  - Limitazioni dell'Access Token: Un Access Token ottenuto come risultato di un Refresh Token Flow NON DEVE essere utilizzato per l'emissione per la prima volta di un Attestato Elettronico. Ciò garantisce che vengano aggiornati solo gli Attestati Elettronici esistenti nell'Istanza del Wallet.
  - Scadenza dell'Attestato Elettronico: Il Credential Issuer DEVE impostare per l'Attestato Elettronico riemesso la stessa data di scadenza del precedente. Ciò impedisce rinnovi indefiniti dell'Attestato Elettronico senza una corretta autenticazione dell'Utente.
  - Consenso dell'Utente: Per i Re-issuance Flow attivati da modifiche agli attributi, il consenso dell'Utente DEVE essere ottenuto prima di memorizzare il nuovo Attestato Elettronico. Ciò garantisce che l'Utente sia consapevole e accetti le informazioni aggiornate.
  - Refresh Token vincolato al mittente: I Refresh Token DEVONO essere crittograficamente vincolati all'Istanza del Wallet utilizzando il protocollo DPoP. Ciò mitiga il rischio di uso improprio del token, garantendo che solo l'Istanza del Wallet prevista (la stessa che ha originariamente ottenuto l'Attestato Elettronico) possa utilizzare quel Refresh Token.

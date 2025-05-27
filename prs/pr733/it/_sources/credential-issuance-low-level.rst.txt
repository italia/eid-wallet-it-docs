.. include:: ../common/common_definitions.rst

Flussi di Basso Livello per il Rilascio di Credenziali
======================================================

Flusso di Rilascio di Basso Livello
-----------------------------------

Il flusso di Rilascio delle Credenziali è basato su [`OpenID4VCI`_] e i seguenti standard/specifiche di riferimento principali DEVONO essere supportati in aggiunta a `OpenID4VCI`_:

  * **The OAuth 2.0 Authorization Framework** [:rfc:`6749`], come raccomandato nella Sezione 3 di [`OpenID4VCI`_].
  * **Pushed Authorization Requests** (PAR) [:rfc:`9126`], come raccomandato nella Sezione 5 di [`OpenID4VCI`_].
  * **Proof Key for Code Exchange** (PKCE) [:rfc:`7636`], come raccomandato nella Sezione 5 di [`OpenID4VCI`_].
  * **JWT Authorization Requests** (JAR) [:rfc:`9101`].
  * **JWT Authorization Response Modes** (JARM) [`JARM`_].
  * **Rich Authorization Requests** (RAR) [:rfc:`9396`].
  * **OAuth 2.0 Attestation-Based Client Authentication** [`OAUTH-ATTESTATION-CLIENT-AUTH`_].
  * **OpenID Federation 1.0** [`OID-FED`_].

Il Credential Issuer DEVE utilizzare un *OAuth 2.0 Authorization Server* basato su :rfc:`6749` per autorizzare l'Utente a ottenere una Credenziale. I Credential Issuer DEVONO supportare:

  * **Authorization Code Flow**: Il Credential Issuer richiede l'autenticazione dell'Utente e il consenso all'Endpoint di Autorizzazione prima di raccogliere le informazioni dell'Utente per creare e fornire una Credenziale.
  * **Wallet Initiated Flow**: La richiesta dall'Istanza del Wallet viene inviata al Credential Issuer senza alcun input dal Credential Issuer.
  * **Immediate Issuance flow**: Il Credential Issuer rilascia la Credenziale direttamente in risposta alla Richiesta di Credenziale.

Inoltre, i Credential Issuer POSSONO supportare:

  * **Issuer Initiated Flow**: L'Istanza del Wallet invia la sua richiesta al Credential Issuer in base all'input fornito dal Credential Issuer.

    * **Same-device Issuance flow**: L'Utente riceve la Credenziale sullo stesso dispositivo utilizzato per avviare il flusso.
    * **Cross-device Issuance flow**: L'Utente riceve la Credenziale su un dispositivo diverso da quello che ha avviato il flusso.

  * **Refresh Token flow**: L'Istanza del Wallet richiede un nuovo Access Token all'Endpoint Token del PID/(Q)EEA.
  * **Re-issuance flow**: A seguito di aggiornamenti a una Credenziale Elettronica già memorizzata, l'Istanza del Wallet richiede un aggiornamento della Credenziale Elettronica all'Endpoint Credential del Credential Issuer.
  * **Deferred Issuance flow**: Il Credential Issuer potrebbe richiedere tempo per emettere la Credenziale Elettronica richiesta, a causa delle regole di provisioning dei dati delle Fonti Autentiche, e consente al Wallet di recuperare la Credenziale richiesta in futuro.

L'intero flusso di Rilascio può essere suddiviso in due sotto-flussi:

  - **Flusso di Richiesta dell'Utente**, che descrive le modalità attraverso le quali l'Utente può richiedere la Credenziale. Può essere:

      **1)** Su iniziativa dell'Utente (**Wallet Initiated**).

      **2)** Su proposta del Credential Issuer (**Issuer Initiated**).

  - **Flusso di Rilascio**, che descrive le interazioni tra l'Istanza del Wallet e il Credential Issuer.

Il seguente diagramma mostra il *flusso di richiesta dell'Utente*.

.. _fig_Low-Level-Flow-ITWallet-PID-QEAA-User-Request:
.. plantuml:: plantuml/credential-user-request-flow.puml
    :width: 99%
    :alt: La figura illustra il Flusso di Richiesta della Credenziale da parte dell'Utente.
    :caption: `Flusso di Richiesta della Credenziale da parte dell'Utente. <https://www.plantuml.com/plantuml/svg/hP9FJzj04CNlyob6uT3sG14zve20XAgHAWKA5PTUrkknFMAzQ-sV6BvzPpTkapHLAoGkLkJClFTxptCPel8nzGPKYiwclYAFvn_F0GPvpve7PIFElWVoCrG14q3bdhSltWKClKmDdRCqmvElt7RnsYGwtBtsRlorNld3_nwLCHHnPGN3QYep8v2jKLmEhUWvahVAO4qRrjblxPLj_sb6Ewc3gOMdccnaKLk5aAPv1b0c8ZVu6ujb9bADduqR0HAUNk0un_L05cD7-0S-gc7uOOtJefk40gNJBlje5TbPK3hoHlGaufYbqXnT5HLRV779uv9RZhAweykEMyiN2W3UEbbs6r4UyUJno-hX1jP5eD0O3X5TKtu_-1Go-57Ia2ifGW3ZwOKWQ6SRzdrP2sH8PrRHETu5I88ZDEu9eAQzE40ca3Gt3HurjtTSd_9nbIPvQl9sjJnxV_VXxERg2c-zst2T0r8LM23vDKNnLDJq6HVUXO3BSYyJI96hFCsnYxt1GRM2px73ksyBLrCk8_kmRVVZhvj6qilQ17FVkJ7tDMqLcOpmjkSnYf5MLammkm3iQhvNFVqrs56kpbFpdrHJA6rOFnNkibEb60KAtZHNFhxjur8UgJS_0G00>`_

**Passaggi 1.1-1.4 (Flusso Avviato dal Wallet):** L'Utente, utilizzando l'Istanza del Wallet, seleziona il Credential Issuer tra quelli elencati nella lista delle entità affidabili.

**Passaggi 2.1-2.3 (Flusso Avviato dall'Issuer):** L'Utente, mentre naviga sul sito web del Credential Issuer, trova un link per ottenere una Credenziale Elettronica.

**Passaggi 2.4-2.7 (Cross-Device):** L'Offerta di Credenziale viene presentata come un Codice QR mostrato all'Utente. L'Utente scansiona il Codice QR utilizzando l'Istanza del Wallet che recupera i parametri definiti nella :ref:`Tabella dei parametri dell'Offerta di Credenziale <table_credential_offer_claim>`.

**Passaggi 2.8-2.10 (Same-Device):** L'Offerta di Credenziale viene presentata come un pulsante href contenente l'URL che consente all'Utente di invocare l'Istanza del Wallet utilizzando l'Endpoint dell'Offerta di Credenziale.

Di seguito un esempio non normativo di un URL relativo a un'Offerta di Credenziale che può essere incluso in un Codice QR o in una pagina html con un pulsante href:

.. code-block:: text

  openid-credential-offer://?credential_offer%3D%7B%22credential_issuer%22%3A%22https%3A%2F%2Feaa-provider.example.org%22%2C%22credential_configuration_ids%22%3A%5B%22dc_sd_jwt_EuropeanDisabilityCard%22%5D%2C%22grants%22%3A%7B%22authorization_code%22%3A%7B%22issuer_state%22%3A%22oaKazRN8I0IbtZ0C7JuMn5%22%7D%7D%7D


Il seguente diagramma mostra il *flusso di rilascio*.

.. _fig_Low-Level-Flow-ITWallet-PID-QEAA-Issuance:
.. plantuml:: plantuml/credential-issuance-flow.puml
    :width: 99%
    :alt: La figura illustra il Flusso di Basso Livello per il Rilascio delle Credenziali.
    :caption: `Rilascio delle Credenziali - Flusso dettagliato. <https://www.plantuml.com/plantuml/svg/hLPVRo8t47_tfnZb7XeaKAgsJoTTTOJG2sgKq9HJNYeXnpl0A8kzjSTmwQUlFLdmGaYhg9MYxAxd_-ytC-PpOEqvhckb8piRru_ebMhI6Hbgj6Ku-nhGdu4E49LwTDzU3huB4DP9gravYsVmuOQMAxwi8nxQNdgttPlhGzc3hcjacDZ0sXeKdQr2Mq6ASfJ3o6E5badNC0aXjXv9AMyT8xWDUjZsAUKn-N8z-t8_7j-gqGhD4xoo10gGVODR0AyGVabohvcS1PrYkqVMP84um1fPLvfrpadYABM5mS-mXOzWF6f6cFuw6eDn5KBAW1Q4Nfmy30TJDstLAQbFX_TmZtz630pdVrW0KnDQdbFLpr_-HTI3_B4bNi7TCF9gC1AjmP0vIKkERmbpK20hPLsZJdLryJc5Jil1rBiDLV-8JMiGQ6arHu-joix3KOg2tqRNL14_GmT0HJ0G27UOXCRPW73UGZ2Fdlg0tnho6EPaUqfGJ2PHVuHSj_FqbyGfW1OmeUEcfw8MItgteT8rTpldqoUOJguEmEn7-F1mFPcDLGoPzHGWAvkN2CBXY71o1JTk2DTfEk3yviUUO6DonJQ5TqrMJW0-fxC4es6oIuWoNbcBjU7GA-XX7V0ehVFVUkFXiFVUr58r_p4LM-suZ1gE0IwqvjdeG-wCzA0GzgHitsLK1c-95dqIm5LkzYTyVbFMUESMdN64XVCdrW6x9xIGwcaSMLQTePqbIMaMmQtZMCPuwRNbEJytA7ES4YylyzrAQ4Uy8ez66apc_7yTSqM2GKbwZwKs1aEOIvMvonSUmshtAGz9_t3c2WQtpXhSOt0zcqrXUlVx32vi5fIuEyN2uLmqUgzsPWjV-cjS21W2ENkeVgHVC7-3GRC_AJIM2eh-2Igxw0ZcNOABtpd9Y-ntrmquDyukQ1cz42EBH8nVhn0Ae3UQQlrO8wW2N5Ude5SYX3vObqERNOWkf6cEBrvMGDcsgGoPdHZ0v9tTgiUahiEJO9XlyDtigzWwsnq0EmZiF4g3bKnAM14VYKh3b6HFzarNVdvKMXzmWrRkmGv9Go7ffRFLgHljykRhMDtZaWAdKrtNHvaFFDQQiG95DfM_bd02HFAoZt_XSUFQnCgLLPWwAArm9RNzyFrFIGmZPpb3MZPrOV_sRbOwu5_ehr5NSwOrze6zja6R7VVTycEVr2mLUlH3gWzw8JXOq6iNhTpcsHc41arkuWeUds4VGnfckq8Bx6cvH2_o3A7qYInYpq4E5hNRWbvgieTNmUVqBwxhlm40>`_

Una volta completato il *flusso di richiesta dell'Utente*, l'Istanza del Wallet elabora i Metadati del Credential Issuer come definito nella Sezione :ref:`trust:Meccanismo di Valutazione della Fiducia`.

.. note::
  **Controllo della Federazione:** L'Istanza del Wallet deve verificare se il Credential Issuer è membro della Federazione, ottenendo i suoi Metadati specifici del protocollo. Un esempio non normativo di una risposta dall'endpoint **.well-known/openid-federation** con la **Configurazione dell'Entità** e i **Metadati** del Credential Issuer è rappresentato nella sezione :ref:`credential-issuer-entity-configuration:Configurazione dell'Entità Fornitore di Credenziale`.

Nel caso del flusso Avviato dall'Issuer, oltre al Controllo della Federazione definito sopra, l'Istanza del Wallet DEVE eseguire i seguenti controlli sui parametri dell'Offerta di Credenziale:

  * Per ogni identificatore di Credenziale contenuto nell'array ``credential_configuration_ids``, verificare se è supportato dal Credential Issuer.
  * L'identificatore dell'Authorization Server (se presente) è contenuto nel parametro dei metadati ``authorization_servers`` del Credential Issuer.


**Passaggi 1-2 (Richiesta PAR)**: L'Istanza del Wallet:

  * crea un nuovo code verifier PKCE, una Prova di Possesso dell'Attestato del Wallet e un parametro ``state`` per la *Pushed Authorization Request*.
  * fornisce all'endpoint PAR del Credential Issuer i parametri precedentemente elencati, utilizzando il parametro ``request`` (di seguito Oggetto Richiesta) secondo la Sezione 3 di :rfc:`9126` per prevenire l'attacco di scambio dell'URI di Richiesta. La Pushed Authorization Request consente l'autenticazione del client prima di qualsiasi interazione dell'Utente. Questo passaggio permette il rifiuto anticipato di richieste illegittime, prevenendo efficacemente attacchi di spoofing, manomissione e uso improprio delle richieste di autorizzazione.
  * DEVE creare il ``code_verifier`` con una stringa casuale con sufficiente entropia utilizzando i caratteri non riservati con una lunghezza minima di 43 caratteri e una lunghezza massima di 128 caratteri, rendendo impraticabile per un attaccante indovinarne il valore. Il valore DEVE essere generato seguendo la raccomandazione nella Sezione 4.1 di :rfc:`7636`.
  * firma questa richiesta utilizzando la chiave privata creata durante la fase di configurazione per ottenere l'Attestato del Wallet. La relativa chiave pubblica attestata dal Fornitore di Wallet viene fornita all'interno del claim ``cnf.jwk`` dell'Attestato del Wallet.
  * DEVE utilizzare i parametri ``OAuth-Client-Attestation`` e ``OAuth-Client-Attestation-PoP`` secondo OAuth 2.0 Attestation-based Client Authentication [`OAUTH-ATTESTATION-CLIENT-AUTH`_], poiché in questo flusso l'Endpoint di Pushed Authorization è un endpoint protetto.
  * specifica i tipi di credenziali richieste utilizzando il parametro ``authorization_details`` [RAR :rfc:`9396`] e/o il parametro scope.

Il Credential Issuer esegue i seguenti controlli alla ricezione della richiesta PAR:

    1. DEVE validare la firma dell'Oggetto Richiesta utilizzando l'algoritmo specificato nel parametro dell'header ``alg`` (:rfc:`9126`, :rfc:`9101`) e la chiave pubblica recuperata dall'Attestato del Wallet (``cnf.jwk``) referenziato nell'Oggetto Richiesta, utilizzando il parametro dell'header JWT ``kid``.
    2. DEVE verificare che l'algoritmo utilizzato per firmare la richiesta nell'header ``alg`` sia uno di quelli elencati nella Sezione :ref:`algorithms:Algoritmi Crittografici`.
    3. DEVE verificare che il ``client_id`` nel corpo della richiesta PAR corrisponda al claim ``client_id`` incluso nell'Oggetto Richiesta.
    4. DEVE verificare che il claim ``iss`` nell'Oggetto Richiesta corrisponda al claim ``client_id`` nell'Oggetto Richiesta (:rfc:`9126`, :rfc:`9101`).
    5. DEVE verificare che il claim ``aud`` nell'Oggetto Richiesta sia uguale all'identificatore del Credential Issuer (:rfc:`9126`, :rfc:`9101`).
    6. DEVE rifiutare la richiesta PAR, se contiene il parametro ``request_uri`` (:rfc:`9126`).
    7. DEVE verificare che l'Oggetto Richiesta contenga tutti i parametri obbligatori i cui valori sono validati secondo la :ref:`Tabella dei parametri HTTP <table_request_object_claim>` [derivata da :rfc:`9126`].
    8. DEVE verificare che l'Oggetto Richiesta non sia scaduto, controllando il claim ``exp``.
    9. DEVE verificare che l'Oggetto Richiesta sia stato emesso in un momento precedente al valore esposto nel claim ``iat``. DOVREBBE rifiutare la richiesta se il claim ``iat`` è lontano dall'ora corrente (:rfc:`9126`) di più di `5` minuti.
    10. DEVE verificare che il claim ``jti`` nell'Oggetto Richiesta non sia stato utilizzato in precedenza dall'Istanza del Wallet identificata dal ``client_id``. Ciò consente al Credential Issuer di mitigare gli attacchi di replay (:rfc:`7519`).
    11. DEVE validare il parametro ``OAuth-Client-Attestation-PoP`` in base alla Sezione 4 di [`OAUTH-ATTESTATION-CLIENT-AUTH`_].

Di seguito un esempio non normativo del PAR.

.. code-block:: http

    POST /as/par HTTP/1.1
    Host: eaa-provider.example.org
    Content-Type: application/x-www-form-urlencoded
    OAuth-Client-Attestation: eyJhbGciOiJFUzI1NiIsImtpZCI6IjBiNDk4ZGRlMDkxNzJhZGE3MDFkMDdlYjZmOTg2N2FkIiwidHlwIjoid2FsbGV0LWF0dGVzdGF0aW9uK2p3dCJ9.eyJpc3MiOiJodHRwczovL3dhbGxldC1wcm92aWRlci5leGFtcGxlLm9yZyIsInN1YiI6InZiZVhKa3NNNDV4cGh0QU5uQ2lHNm1DeXVVNGpmR056b3BHdUt2b2dnOWMiLCJhYWwiOiJodHRwczovL3RydXN0LWxpc3QuZXUvYWFsL2hpZ2giLCJjbmYiOnsiandrIjp7ImNydiI6IlAtMjU2Iiwia3R5IjoiRUMiLCJ4IjoiNEhOcHRJLXhyMnBqeVJKS0dNbno0V21kblFEX3VKU3E0Ujk1Tmo5OGI0NCIsInkiOiJMSVpuU0IzOXZGSmhZZ1MzazdqWEU0cjMtQ29HRlF3WnRQQklScXBObHJnIn19LCJhdXRob3JpemF0aW9uX2VuZHBvaW50IjoiaHR0cHM6Ly93YWxsZXQtc29sdXRpb24uZGlnaXRhbC1zdHJhdGVneS5ldXJvcGEuZXUvYXV0aG9yaXphdGlvbiIsInJlc3BvbnNlX3R5cGVzX3N1cHBvcnRlZCI6WyJ2cF90b2tlbiJdLCJyZXNwb25zZV9tb2Rlc19zdXBwb3J0ZWQiOlsiZm9ybV9wb3N0Lmp3dCJdLCJ2cF9mb3JtYXRzX3N1cHBvcnRlZCI6eyJkYytzZC1qd3QiOnsic2Qtand0X2FsZ192YWx1ZXMiOlsiRVMyNTYiLCJFUzM4NCJdfX0sInJlcXVlc3Rfb2JqZWN0X3NpZ25pbmdfYWxnX3ZhbHVlc19zdXBwb3J0ZWQiOlsiRVMyNTYiXSwicHJlc2VudGF0aW9uX2RlZmluaXRpb25fdXJpX3N1cHBvcnRlZCI6ZmFsc2UsImNsaWVudF9pZF9zY2hlbWVzX3N1cHBvcnRlZCI6WyJlbnRpdHlfaWQiXSwiaWF0IjoxNzQwMTU4MDQ3LCJleHAiOjE3NDAxNTgxNjd9.paU3FOET8nraQxuesBXD9gw57DL5HfDzkeboKAOinyh5L2MmLwqvRtrSWK8S7qMRWYmdzR-gHMpmebIH7gGE5w
    OAuth-Client-Attestation-PoP: eyJhbGciOiJFUzI1NiIsInR5cCI6Im9hdXRoLWNsaWVudC1hdHRlc3RhdGlvbi1wb3Arand0In0.eyJpc3MiOiIgaHR0cHM6Ly9jbGllbnQuZXhhbXBsZS5jb20iLCJhdWQiOiJodHRwczovL2FzLmV4YW1wbGUuY29tIiwianRpIjoiZDI1ZDAwYWItNTUyYi00NmZjLWFlMTktOThmNDQwZjI1MDY0IiwiaWF0IjoxNzQwMTU4NjE3LCJleHAiOjE3NDAxNTg3Mzd9.B0KOkGi9vMxf3H2Y8rrF-mdLNsuluTvAUbjFfL1Hi-gdaPW7-8ziS9uVh7aTnSAHKWzMfkZLv5q-bxhkglR4PA

    client_id=$thumprint-of-the-jwk-in-the-cnf-wallet-attestation$&
    request=$SIGNED-JWT

Di seguito un esempio non normativo dell'header e del corpo della Prova di Possesso dell'Attestato del Wallet (WIA-PoP):

.. literalinclude:: ../../examples/wa-pop-header.json
  :language: JSON

.. literalinclude:: ../../examples/wa-pop-payload.json
  :language: JSON


Di seguito un esempio non normativo dell'Oggetto Richiesta firmato senza codifica e firma applicata:

.. literalinclude:: ../../examples/request-object-header.json
  :language: JSON

.. literalinclude:: ../../examples/request-object-payload.json
  :language: JSON


.. note::
  **Controllo della Federazione**: Il Credential Issuer DEVE verificare che il Fornitore di Wallet faccia parte della federazione.


.. note::
  Il Credential Issuer DEVE validare la firma dell'Attestato del Wallet e che non sia scaduto.

**Passaggio 3 (Risposta PAR)**: Il Credential Issuer fornisce un valore ``request_uri`` monouso. Il valore ``request_uri`` emesso DEVE essere vincolato all'identificatore del client (``client_id``) che è stato fornito nell'Oggetto Richiesta.


.. note::
  L'entropia del ``request_uri`` DEVE essere sufficientemente grande. L'adeguata brevità della validità e l'entropia del ``request_uri`` dipendono dal calcolo del rischio basato sul valore della risorsa protetta. Il tempo di validità DOVREBBE essere inferiore a un minuto, e il ``request_uri`` DEVE includere un valore casuale crittografico di 128 bit o più (:rfc:`9101`). L'intero ``request_uri`` NON DOVREBBE superare i 512 caratteri ASCII per i seguenti due motivi principali (:rfc:`9101`):

    1. Molti telefoni sul mercato ancora non accettano payload di grandi dimensioni. La restrizione è tipicamente di 512 o 1024 caratteri ASCII.
    2. Su una connessione lenta come una connessione mobile 2G, un URL grande causerebbe una risposta lenta; pertanto, l'uso di tale URL non è consigliabile dal punto di vista dell'esperienza utente.

Il Credential Issuer restituisce il ``request_uri`` emesso all'Istanza del Wallet. Un esempio non normativo della risposta è mostrato di seguito.

.. code-block:: http

  HTTP/1.1 201 Created
  Cache-Control: no-cache, no-store
  Content-Type: application/json

.. literalinclude:: ../../examples/par-response.json
  :language: JSON

**Passaggi 4-5 (Richiesta di Autorizzazione)**: L'Istanza del Wallet invia una richiesta di autorizzazione all'Endpoint di Autorizzazione del Credential Issuer. Poiché parti del contenuto di questa Richiesta di Autorizzazione, ad esempio il valore del parametro ``code_challenge``, sono unici per una particolare Richiesta di Autorizzazione, l'Istanza del Wallet DEVE utilizzare un valore ``request_uri`` una sola volta (:rfc:`9126`); Il Credential Issuer esegue i seguenti controlli alla ricezione della Richiesta di Autorizzazione:

    1. DEVE trattare i valori ``request_uri`` come monouso e DEVE rifiutare una richiesta scaduta. Tuttavia, PUÒ consentire richieste duplicate a causa di un utente che ricarica/aggiorna il proprio user-agent (derivato da :rfc:`9126`).
    2. DEVE identificare la richiesta come risultato del PAR inviato (derivato da :rfc:`9126`).
    3. DEVE rifiutare tutte le Richieste di Autorizzazione che non contengono il parametro ``request_uri`` poiché il PAR è l'unico modo per passare la Richiesta di Autorizzazione dall'Istanza del Wallet (derivato da :rfc:`9126`).


.. code-block:: http

    GET /authorize?client_id=$thumprint-of-the-jwk-in-the-cnf-wallet-attestation$&request_uri=urn%3Aietf%3Aparams%3Aoauth%3Arequest_uri%3Abwc4JK-ESC0w8acc191e-Y1LTC2 HTTP/1.1
    Host: eaa-provider.example.org


.. note::
   **Autenticazione dell'Utente e Consenso**: Il Fornitore di Attestati Elettronici di Dati di Identificazione Personale esegue l'autenticazione dell'Utente basata sullo schema CieID con LoA High (CIE L3) e richiede il consenso dell'Utente per il rilascio del PID.
   Il Fornitore di Attestati Elettronici di Attributi (Qualificati) esegue l'autenticazione dell'Utente richiedendo un PID valido all'Istanza del Wallet. Il Fornitore di Attestati Elettronici di Attributi (Qualificati) DEVE utilizzare [`OpenID4VP`_] per richiedere la presentazione del PID. In questa circostanza, il Fornitore di Attestati Elettronici di Attributi (Qualificati) agisce come una Relying Party, fornendo la richiesta di presentazione all'Istanza del Wallet. L'Istanza del Wallet DEVE avere un PID valido, ottenuto in precedenza, per avviare la transazione con il Fornitore di Attestati Elettronici di Attributi (Qualificati). Durante questo passaggio, i Credential Issuer POSSONO chiedere i dettagli di contatto dell'Utente (ad esempio, il loro indirizzo email) per inviare notifiche sulle Credenziali Elettroniche emesse.



**Passaggi 6-7 (Risposta di Autorizzazione)**: Il Credential Issuer invia un ``code`` di autorizzazione insieme ai parametri ``state`` e ``iss`` all'Istanza del Wallet. L'Istanza del Wallet esegue i seguenti controlli sulla Risposta di Autorizzazione:

    1. DEVE verificare che la Risposta di Autorizzazione contenga tutti i parametri definiti secondo la :ref:`Tabella dei parametri della Risposta HTTP <table_http_response_claim>`.
    2. DEVE verificare che il valore restituito dal Credential Issuer per il parametro ``state`` sia uguale al valore inviato dall'Istanza del Wallet nell'Oggetto Richiesta (:rfc:`6749`).
    3. DEVE verificare che l'URL del Credential Issuer nel parametro ``iss`` sia uguale all'identificatore URL del Credential Issuer previsto con cui l'Istanza del Wallet ha iniziato la comunicazione (:rfc:`9027`).

.. note::
    L'URI di reindirizzamento dell'Istanza del Wallet è un link universale o app registrato con il sistema operativo locale, quindi quest'ultimo lo risolverà e passerà la risposta all'Istanza del Wallet.

.. code-block:: http

    HTTP/1.1 302 Found
    Location: https://start.wallet.example.org?code=SplxlOBeZQQYbYS6WxSbIA&state=fyZiOL9Lf2CeKuNT2JzxiLRDink0uPcd&iss=https%3A%2F%2Feaa-provider.example.org

**Passaggi 8-9 (Prova DPoP per l'Endpoint Token)**: L'Istanza del Wallet DEVE creare una nuova coppia di chiavi per il DPoP e un nuovo JWT di Prova DPoP seguendo le istruzioni fornite nella Sezione 4 di (:rfc:`9449`) per la richiesta di token al Credential Issuer. Il JWT di Prova DPoP è firmato utilizzando la chiave privata per DPoP creata dall'Istanza del Wallet per questo scopo. DPoP vincola l'Access Token, e opzionalmente il Refresh Token, a una determinata Istanza del Wallet (:rfc:`9449`) e mitiga l'uso improprio di token persi o rubati all'Endpoint Credential.

**Passaggio 10 (Richiesta Token):** L'Istanza del Wallet invia una richiesta di token all'Endpoint Token del Credential Issuer con un *JWT di Prova DPoP* e i parametri: ``code``, ``code_verifier`` e OAuth 2.0 Attestation based Client Authentication (``OAuth-Client-Attestation`` e ``OAuth-Client-Attestation-PoP``).

L'``OAuth-Client-Attestation`` è firmato utilizzando la chiave privata vincolata all'Istanza del Wallet. La relativa chiave pubblica attestata dal Fornitore di Wallet è fornita all'interno dell'Attestato del Wallet (claim ``cnf.jwk``). Il Credential Issuer esegue i seguenti controlli sulla Richiesta di Token:

   1. DEVE assicurarsi che il ``code`` di Autorizzazione sia emesso per l'Istanza del Wallet autenticata (:rfc:`6749`) e non sia stato replicato.
   2. DEVE assicurarsi che il ``code`` di Autorizzazione sia valido e non sia stato utilizzato in precedenza (:rfc:`6749`).
   3. DEVE assicurarsi che il ``redirect_uri`` corrisponda al valore incluso nel precedente Oggetto Richiesta (vedi Sezione 3.1.3.1. di [`OIDC`_]).
   4. DEVE validare il JWT di Prova DPoP, secondo la Sezione 4.3 di (:rfc:`9449`).

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

**Passaggio 11 (Risposta Token)**: Il Credential Issuer valida la richiesta. In caso di successo, l'Issuer fornisce all'Istanza del Wallet un Access Token e, opzionalmente, un Refresh Token, entrambi vincolati alla chiave DPoP.

.. code-block:: http

    HTTP/1.1 200 OK
    Content-Type: application/json
    Cache-Control: no-store

.. literalinclude:: ../../examples/token-response.json
  :language: JSON

L'esempio non normativo dell'Access Token DPoP è fornito di seguito.

.. literalinclude:: ../../examples/at-dpop-header.json
  :language: JSON

.. literalinclude:: ../../examples/at-dpop-payload.json
  :language: JSON

L'esempio non normativo del Refresh Token DPoP è fornito di seguito.

.. literalinclude:: ../../examples/rt-dpop-header.json
  :language: JSON

.. literalinclude:: ../../examples/rt-dpop-payload.json
  :language: JSON

**Passaggio 12 (Richiesta Nonce)**: Secondo la Sezione 7.1 di [`OpenID4VCI`_], l'Istanza del Wallet invia una richiesta HTTP POST all'Endpoint Nonce per ottenere un nuovo ``c_nonce`` che può essere utilizzato per creare la prova di possesso del materiale chiave per la successiva richiesta all'Endpoint Credential.

Di seguito è riportato un esempio non normativo di una Richiesta Nonce:

.. code-block:: http

    POST /nonce HTTP/1.1
    Host: eaa-provider.example.org
    Content-Length: 0

**Passaggio 13 (Risposta Nonce)**: Il Credential Issuer fornisce il `c_nonce` all'Istanza del Wallet. Il parametro `c_nonce` è un valore stringa, che DEVE essere imprevedibile e viene utilizzato successivamente dall'Istanza del Wallet nel Passaggio 16 per creare la prova di possesso della chiave (claim *proof*) ed è la principale contromisura contro l'attacco di replay della prova della chiave.
Si noti che il valore `c_nonce` ricevuto può essere utilizzato per creare la prova finché l'Issuer
fornisce all'Istanza del Wallet un nuovo valore `c_nonce`.

Di seguito è riportato un esempio non normativo di una Risposta Nonce:

.. code-block:: http

    HTTP/1.1 200 OK
    Content-Type: application/json
    Cache-Control: no-store

.. literalinclude:: ../../examples/nonce-response.json
  :language: JSON


**Passaggi 14-15 (Prova DPoP per l'Endpoint Credential)**: L'Istanza del Wallet per richiedere la Credenziale Elettronica crea una prova di possesso con ``c_nonce`` ottenuto nel **Passaggio 13** e utilizzando la chiave privata utilizzata per il DPoP, firmando un JWT di Prova DPoP secondo la Sezione 4 di (:rfc:`9449`). Il valore ``jwk`` nel parametro ``proof`` DEVE essere uguale alla chiave pubblica referenziata nel DPoP.

**Passaggio 16 (Richiesta Credenziale)**: L'Istanza del Wallet invia una richiesta per la Credenziale Elettronica all'endpoint Credential. Questa richiesta DEVE includere l'Access Token, il JWT di Prova DPoP, il tipo di credenziale, la prova (che dimostra il possesso del materiale chiave crittografico). Il parametro proof DEVE essere un oggetto che contiene la prova del possesso del materiale chiave crittografico a cui sarà vincolata la Credenziale Elettronica emessa. Per verificare la prova, il Credential Issuer conduce i seguenti controlli all'endpoint Credential:

 1. la prova JWT DEVE includere tutti i claim richiesti come specificato nella tabella della Sezione :ref:`credential-issuance-endpoint:Richiesta di Token`;
 2. La prova della chiave DEVE essere esplicitamente tipizzata utilizzando i parametri dell'header come definito per il rispettivo tipo di prova;
 3. Il parametro dell'header alg DEVE indicare un algoritmo di firma digitale asimmetrica registrato e NON DEVE essere impostato su `none`;
 4. La firma sulla prova della chiave DEVE essere verificata utilizzando la chiave pubblica specificata nel parametro dell'header;
 5. Il parametro dell'header NON DEVE contenere una chiave privata;
 6. Se un valore `c_nonce` è stato precedentemente fornito dal server, il claim nonce nel JWT DEVE corrispondere a questo valore `c_nonce`. Inoltre, il tempo di creazione del JWT, come indicato dal claim `iat` o da un timestamp gestito dal server tramite il claim nonce, DEVE essere all'interno di una finestra temporale accettabile come determinato dal server.


.. note::
  **Registrazione dello Schema e dello Stato della Credenziale**: Il Credential Issuer DEVE registrare tutte le Credenziali emesse per la loro successiva revoca, se necessario.


.. note::
  Si RACCOMANDA che la chiave pubblica contenuta nel ``jwt_proof`` sia generata specificamente per la Credenziale richiesta (chiave crittografica fresca) per garantire che diverse Credenziali emesse non condividano la stessa chiave pubblica, rimanendo così non collegabili tra loro.


Un esempio non normativo della Richiesta di Credenziale è fornito di seguito.


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

Dove un esempio non normativo del contenuto decodificato del parametro ``jwt`` è rappresentato di seguito,
senza codifica e firma. L'header JWT:

.. literalinclude:: ../../examples/credential-jwt-proof-header.json
  :language: JSON

.. literalinclude:: ../../examples/credential-jwt-proof-payload.json
  :language: JSON

**Passaggi 17-21 (Risposta Credenziale)**: Il Credential Issuer DEVE validare la *Prova JWT DPoP* in base ai passaggi definiti nella Sezione 4.3 di (:rfc:`9449`) e se l'*Access Token* è valido e adatto per la Credenziale richiesta. Il Credential Issuer DEVE validare la prova di possesso per il materiale chiave a cui la nuova Credenziale SARÀ vincolata, secondo la Sezione 8.2.2 di `OpenID4VCI`_. Se tutti i controlli hanno successo, il Credential Issuer crea una nuova Credenziale vincolata al materiale chiave e la fornisce all'Istanza del Wallet. L'Istanza del Wallet DEVE eseguire i seguenti controlli prima di procedere con l'archiviazione sicura della Credenziale:

    1. DEVE verificare che il PID/(Q)EAA contenuto nella Risposta Credenziale contenga tutti i parametri obbligatori e i valori siano validati secondo la :ref:`Tabella dei parametri della risposta Credenziale <table_credential_response_claim>`.
    2. DEVE verificare l'integrità della credenziale verificando la firma utilizzando l'algoritmo specificato nel parametro dell'header ``alg`` di SD-JWT (:ref:`credential-data-model:Modello di Dati delle Credenziali Elettroniche`) e la chiave pubblica che è identificata utilizzando l'header ``kid`` dell'SD-JWT.
    3. DEVE verificare che la Credenziale Elettronica ricevuta (nel claim credential) corrisponda al tipo di credenziale richiesto e sia conforme allo schema specifico di quella Credenziale definito in :ref:`credential-data-model:Modello di Dati delle Credenziali Elettroniche`.
    4. DEVE elaborare e verificare la Credenziale nel formato SD-JWT VC (secondo la Sezione 5 di `SD-JWT`_) o nel formato mdoc-CBOR.
    5. DEVE verificare la Catena di Trust nell'header dell'SD-JWT VC per verificare che il Credential Issuer sia affidabile.

Se i controlli sopra hanno successo, l'Istanza del Wallet richiede il consenso dell'Utente per memorizzare la Credenziale Elettronica. Dopo aver ricevuto il consenso, l'Istanza del Wallet memorizza in modo sicuro la Credenziale Elettronica.

Di seguito è riportato un esempio non normativo di una risposta di successo contenente una Credenziale nel formato SD-JWT VC.

.. code-block:: http

    HTTP/1.1 200 OK
    Content-Type: application/json
    Cache-Control: no-store
    Pragma: no-cache

.. literalinclude:: ../../examples/sd-jwt-credential-response.json
  :language: JSON

Di seguito è riportato un esempio non normativo di una risposta di successo contenente una Credenziale nel formato mdoc.

.. code-block:: http

    HTTP/1.1 200 OK
    Content-Type: application/json
    Cache-Control: no-store
    Pragma: no-cache

.. literalinclude:: ../../examples/mdoc-credential-response.json
  :language: JSON


.. note::
  Se la Credenziale richiesta non può essere emessa immediatamente e richiede più tempo, il Credential Issuer DOVREBBE supportare il Flusso Differito (passaggio 24) come specificato nella Sezione :ref:`credential-issuance-endpoint:Endpoint Differito`.

**Passaggio 22 (Richiesta di Notifica)**: Secondo la Sezione 10.1 di [`OpenID4VCI`_], il Wallet invia una richiesta HTTP POST all'Endpoint di Notifica utilizzando il tipo di media *application/json* come nel seguente esempio non normativo.

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


**Passaggio 23 (Risposta di Notifica)**: Quando il Credential Issuer ha ricevuto con successo la Richiesta di Notifica dal Wallet, DEVE rispondere con un codice di stato HTTP *204* come raccomandato nella Sezione 10.2 di [`OpenID4VCI`_]. Di seguito è riportato un esempio non normativo di risposta a una Richiesta di Notifica riuscita:

.. code-block:: http

  HTTP/1.1 204 No Content


Flusso del Refresh Token
------------------------

Per utilizzare gli endpoint Deferred, Credential Request e Notification, l'Istanza del Wallet DEVE presentare un Access Token DPoP valido al Credential Issuer. Tuttavia, quando questi endpoint sono utilizzati nel Flusso Differito, per il ri-rilascio o la notifica dell'eliminazione di una Credenziale Elettronica, l'Access Token potrebbe scadere, poiché è progettato per avere una breve durata e queste azioni POSSONO verificarsi giorni dopo. Per affrontare questo problema, la specifica RACCOMANDA l'uso dei Refresh Token.

Un Access Token ottenuto come risultato di un flusso di Refresh Token DEVE essere limitato a:

  - l'endpoint Deferred per ottenere una nuova Credenziale Elettronica dopo il tempo impostato nel parametro ``lead_time`` o quando viene notificato come pronto per essere emesso;
  - l'endpoint Notification, per notificare l'eliminazione di una Credenziale Elettronica al Credential Issuer;
  - l'endpoint Credential, per aggiornare una Credenziale Elettronica che è già presente nell'Istanza del Wallet (chiamato anche ri-rilascio della Credenziale Elettronica, vedi sezione :ref:`credential-issuance-low-level:Flusso di Ri-Rilascio`).

Per mitigare l'impatto di un Refresh Token rubato, i Refresh Token DEVONO essere DPoP. Questi aspetti sono dettagliati e discussi nella Sezione :ref:`credential-issuance-low-level:Considerazioni di Sicurezza`.

La figura seguente mostra come ottenere un nuovo Access Token DPoP e un nuovo Refresh Token DPoP all'Endpoint Token.

.. _fig_refresh_token_flow:
.. plantuml:: plantuml/pid-issuance-high-level-flow.puml
    :width: 99%
    :alt: La figura illustra il Flusso del Refresh Token.
    :caption: `Flusso del Refresh Token. <https://www.plantuml.com/plantuml/svg/TPBDQkim48NtUef3xYQ1cEpleYIaXMRLK0BP588gZ-EXpiYLnhXz-yfoJ1jAbvwVpzySj8vgWtQNnjXElNINLmh6jAd6ZbihYjdHDWqfTf96nT4CDgA_7Ta6AacKRODTZ1s5FCJ6z2ZkqEC_pYGKh1BkztwFDdXVmKg9uwOO2fKF-0M1-ZSIa9IjPz4hZHFja1lFzDvHLFIizK_k_4M0Sx2Y9_riQJby1ge2nVgKaGkaKjvwsdHQ5zk6IRJOg2QSLVQItVvgPcCMQ4seoPP3OZmTEgd5raiapArp5EFut-Mjnd8yS9G4VRISUYUMXJ6rU2LO5toC-7Tyt1qU4hecL8tluRmeIxfzFC8YN9DGdwLAgYW4AbU9mXMxRBrot_bEaKun34j2_HZYQ3owcNKQJQ_Z2m00>`_

.. note::
  L'aggiornamento di un Token può essere attivato da diverse azioni (ad esempio, l'eliminazione di una Credenziale Elettronica da parte dell'Utente). In ogni caso, si suppone che le Istanze del Wallet siano in esecuzione e che il relativo materiale crittografico sia sbloccato.

**Passaggio 1.** L'Istanza del Wallet DEVE creare un nuovo JWT di Prova DPoP e una nuova prova di possesso dell'Attestato del Wallet per la richiesta di token del Credential Issuer.

**Passaggio 2.** Per aggiornare un Access Token vincolato a DPoP, l'Istanza del Wallet invia una richiesta di token utilizzando il parametro ``grant_type`` impostato su ``refresh_token``, includendo l'header DPoP e gli header di OAuth Client Attestation.
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

**Passaggio 3.** Il Credential Issuer valida la richiesta secondo i seguenti controlli:

  - DEVE validare il parametro OAuth-Client-Attestation-PoP in base alla Sezione 4 di [OAUTH-ATTESTATION-CLIENT-AUTH].
  - DEVE validare il JWT di Prova DPoP, secondo la Sezione 4.3 di (RFC 9449).
  - DEVE verificare che il Refresh Token non sia scaduto, non sia revocato e sia vincolato allo stesso set di chiavi DPoP di quelle utilizzate nel JWT di Prova DPoP.

Se i controlli della richiesta hanno successo, il Credential Issuer genera un nuovo Access Token e un nuovo Refresh Token e questi DEVONO essere entrambi vincolati alla chiave DPoP. Sia l'Access Token che il Refresh Token vengono quindi inviati all'Istanza del Wallet.

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

Se il Refresh Token è scaduto o non valido, il Credential Issuer DEVE emettere un errore, utilizzando il membro del tipo di errore impostato su ``invalid_grant``. Pertanto, per ottenere la Credenziale Elettronica è necessario un flusso di rilascio che autentichi l'Utente, come definito nella Sezione :ref:`credential-issuance-low-level:Flusso di Rilascio di Basso Livello`.

Considerazioni di Sicurezza
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Per mitigare i rischi di compromissione del Refresh Token, sono richieste le seguenti protezioni:

  - La **riservatezza** dei Refresh Token DEVE essere garantita in transito e archiviazione.
  - Le connessioni **protette da TLS** DEVONO essere utilizzate per la trasmissione dei token.
  - I Refresh Token DEVONO essere **non indovinabili e sicuri da modifiche**.
  - I Server di Autorizzazione DEVONO implementare il seguente meccanismo per **rilevare gli attacchi di replay**:

    - **Token vincolati al mittente**: Vincolare crittograficamente il Refresh Token all'Istanza del Wallet secondo :rfc:`9449`. Gli Access Token e i Refresh Token DEVONO essere vincolati alla stessa chiave DPoP. La Prova DPoP del Refresh Token è richiesta per aggiornare un Access Token. La stessa chiave DPoP DEVE essere utilizzata per generare le Prove DPoP dell'Access Token in tutte le Richieste di Credenziale.

  - **Limitazione dell'uso del Refresh Token**: Come specificato in `OPENID4VC-HAIP`_: "I Credential Issuer dovrebbero essere consapevoli di quanto tempo è consentito l'uso del Refresh Token per aggiornare una Credenziale, rispetto all'avvio del flusso di rilascio dall'inizio. Ad esempio, se l'Utente sta cercando di aggiornare una Credenziale più di un anno dopo il suo rilascio originale, l'uso dei Refresh Token NON È RACCOMANDATO." In questa specifica, una nuova Credenziale Elettronica ottenuta eseguendo il flusso di ri-rilascio DOVREBBE avere la stessa scadenza di quella aggiornata. Pertanto, questa specifica non consente l'aggiornamento infinito della Credenziale Elettronica con un Refresh Token. Una volta che una Credenziale Elettronica scade, l'Utente DEVE completare nuovamente l'intero processo di rilascio per ottenere una nuova Credenziale Elettronica. Questa specifica raccomanda di impostare una durata di scadenza del Refresh Token, in base alla sensibilità della concessione associata.

.. note::
  *Attestati del Wallet e DPoP di breve durata*: Seguendo la bozza di specifica *OAuth 2.0 Attestation Based Client Authentication* (`OAUTH-ATTESTATION-CLIENT-AUTH`_), l'Authorization Server DEVE vincolare il Refresh Token all'Istanza del Client. Per dimostrare questo vincolo, l'Istanza del Client DEVE utilizzare il meccanismo di Attestazione del Client quando aggiorna l'Access Token e l'Istanza del Client DEVE utilizzare la stessa chiave che è stata presentata nel claim ``cnf.jwk`` dell'Attestazione del Client che è stata utilizzata quando il Refresh Token è stato emesso. Tuttavia, ciò richiede che tutti gli Attestati del Client emessi DEVONO essere vincolati alla stessa chiave, aprendo così a problemi di non collegabilità. In questa specifica, sia `OAUTH-ATTESTATION-CLIENT-AUTH`_ che *OAuth 2.0 Demonstrating Proof of Possession (DPoP)* (:rfc:`9449`) DEVONO essere utilizzati. L'uso di DPoP garantisce il vincolo del Refresh Token con l'Istanza del Client come indicato nella sezione 5 di :rfc:`9449` *"il Refresh Token DEVE essere vincolato alla rispettiva chiave pubblica [...] un Client DEVE presentare una prova DPoP per la stessa chiave che è stata utilizzata per ottenere il Refresh Token ogni volta che quel Refresh Token viene utilizzato per ottenere un nuovo Access Token"*. DPoP garantisce che il Refresh Token sia vincolato all'Istanza del Wallet.


Flusso di Ri-Rilascio
---------------------

Il ri-rilascio comporta la sostituzione delle Credenziali Elettroniche già memorizzate in un'Istanza del Wallet con nuove dello stesso tipo di documento. Le nuove Credenziali Elettroniche DEVONO essere emesse dagli stessi Credential Issuer che hanno originariamente fornito quelle esistenti alla stessa Istanza del Wallet.

Per facilitare questo, in particolare in scenari in cui l'autenticazione dell'Utente non è strettamente richiesta, PUÒ essere utilizzato un flusso di Refresh Token (RT) (vedi Sezione :ref:`credential-issuance-low-level:Flusso del Refresh Token` per maggiori dettagli). Un Access Token ottenuto come risultato di un flusso di Refresh Token NON DEVE essere utilizzato per emettere una Credenziale Elettronica che non è presente nell'Istanza del Wallet (rilascio per la prima volta). Il meccanismo del Refresh Token consente la sostituzione automatica della Credenziale, semplificando il processo sia per il Credential Issuer che per l'Utente.

Il processo di ri-rilascio delineato in questa sezione è limitato ai seguenti scenari:

  - Aggiornamento tecnico del modello/formato dei dati;
  - Aggiornamento del set di attributi dell'Utente.

Nel primo caso, il set di attributi dell'Utente della nuova Credenziale Elettronica corrisponderà a quello originale. Ad esempio, un Credential Issuer potrebbe dover aggiornare i metadati della Credenziale Elettronica o il formato dei dati senza modificare il set di attributi dell'Utente. In questo caso, il coinvolgimento diretto dell'Utente non è obbligatorio per la sostituzione e l'archiviazione di una Credenziale Elettronica.

Nel secondo caso, i Credential Issuer potrebbero anche dover modificare uno o più valori degli attributi dell'Utente durante il ri-rilascio. In questo caso, l'Istanza del Wallet DEVE informare l'Utente che il set di dati degli attributi è stato modificato e DEVE quindi richiedere l'autorizzazione dell'Utente per memorizzare la nuova Credenziale Elettronica.

In entrambi i casi, la Credenziale Elettronica appena emessa DEVE avere la stessa data di scadenza di quella precedente.

Il ri-rilascio dopo la scadenza della Credenziale Elettronica DEVE sempre richiedere l'autenticazione dell'Utente.

Il seguente diagramma descrive il flusso di ri-rilascio della Credenziale Elettronica.

.. _fig_reissuance_flow:
.. plantuml:: plantuml/credential-reissuance-flow.puml
    :width: 99%
    :alt: La figura illustra il Diagramma del Flusso di Ri-Rilascio.
    :caption: `Diagramma del Flusso di Ri-Rilascio. <https://www.plantuml.com/plantuml/svg/ZLHTRnCn47pthnYUQAMqLA9FAOM6faYH2gf2IeLQ5BbtUuc5OmVlNjBowucT3-LYABc7ABPdzcCywmiM7QIUMFNAkCBM9U7TvUcRozDXzzdfYIdUAwKIHZalX616Or5tOtBGw9gH4Mrn6QWa9qPREAAI8HwFX7fQQg6o1HdJDgR7N5DWVEvy1vCheU6ycCeKMentaHqPjqm1DHitWaQWaM6XG2LyBKU-EdhKhaJX9vFQhOd5M3j7zbZ5eB5SfTefYf-IOznfQqdGSopQ5NIcbAbmqAUPN_4d52COdk31uHnVHKlDk3Oi-708YKqVF1CVAYW0xJv9C3IZ1d3WVv93vKE4WCK7AhUQvxEqdxIqL4bQzUbNRI9k7bCuZvcsfan7UMXwCYoS3ZTjnaNiPKla5T4ut9yydRnjOV5x-cEdZVYHPSA1yuTGsFvO_5HXbSPKge5LSPahq66c4ANa_HI8RjfFWaRilqdmWWRdw7tvrhdkTVFkrwHYGnfo8WrB4ctiSLmHZDkWxszlkft1LGkTmQ3V-tWxk1ekTt9jzvIteV3Urx7yRJJHAGfYNjaawPULjFdo-Xh7oy6e0l5ultX0Uw5s43HPdwoVB-_xfNoP7i368ZjxM6RH3excwIM9eungaMSNEJSoJe_8QqQdZdNB-g7OWcPpbDz9ljhyYSyBkZV-1WtnnIEiHcC3ZVNc3-PQdCoxlFPkdDiMVC23-uzBppDF_lk-sd7WY2K9bEJnmVnEwfnjup9NDF34knaoJ_X0iVMivHVya3aYkuECk6_6dQbfTycI4AQ1PiRNtE2eLC35Wb9Fx1y0>`_

1. Il flusso inizia quando l'Utente apre l'Istanza del Wallet: questo passaggio PUÒ essere attivato da una notifica inviata dal Credential Issuer (utilizzando ad esempio uno dei contatti di comunicazione fuori banda registrati durante il flusso di Rilascio).
2. Indipendentemente dal meccanismo di revoca della Credenziale Elettronica supportato, se l'Istanza del Wallet.

   - supporta solo Status List e non ha un Token di Stato valido per una Credenziale Elettronica memorizzata, l'Istanza del Wallet DEVE recuperarne uno nuovo seguendo il flusso descritto nella Sezione :ref:`credential-revocation:OAuth Status Lists`. Se qualsiasi Credenziale Elettronica ha lo stato impostato su ``0x03`` - ``UPDATE`` o ``0x04`` - ``ATTRIBUTE_UPDATE``; oppure
   - insieme al Credential Issuer supporta anche Status Assertion e l'Istanza del Wallet non ha una Status Assertion valida per una Credenziale Elettronica memorizzata, l'Istanza del Wallet PUÒ recuperarne una nuova seguendo il flusso descritto nella Sezione :ref:`credential-revocation:OAuth Status Assertions`. Se qualsiasi Credenziale Elettronica ha il ``credential_status_type`` impostato su ``INVALID``, l'Istanza del Wallet DEVE verificare il claim ``credential_status_detail.state``. Se questo claim è impostato su ``UPDATE`` o ``ATTRIBUTE_UPDATE``, allora

     l'Istanza del Wallet DEVE verificare se i relativi Access Token sono ancora validi. Se l'Access Token è valido, allora il passaggio 3 PUÒ essere saltato.

3. Se l'Access Token è scaduto e l'Istanza del Wallet ha ancora un Refresh Token valido, l'Istanza del Wallet DEVE ottenere un nuovo Access Token avviando un Flusso di Refresh Token, secondo la Sezione :ref:`credential-issuance-low-level:Flusso del Refresh Token`. Il Flusso di Refresh Token consente all'Istanza del Wallet di ottenere un nuovo Refresh Token e un nuovo Access Token DPoP per aggiornare la Credenziale Elettronica. Se il Refresh Token è scaduto, è necessario un nuovo Flusso di Rilascio che autentichi l'Utente.
4. L'Istanza del Wallet DEVE utilizzare un Access Token DPoP valido per recuperare la nuova Credenziale Elettronica richiedendola all'endpoint Credential seguendo i passaggi da 12 a 22 della Figura 9 nella Sezione :ref:`credential-issuance-low-level:Flusso di Rilascio di Basso Livello`. Quando la nuova Credenziale Elettronica è memorizzata con successo nell'archivio sicuro, l'Istanza del Wallet DEVE eliminare quella precedente.

.. note::
  Indipendentemente dal meccanismo di revoca della Credenziale Elettronica supportato, se lo stato della Credenziale Elettronica è impostato su ``ATTRIBUTE_UPDATE`` (utilizzando la revoca OAuth Status List) o ``credential_status_detail.state`` è impostato su ``ATTRIBUTE_UPDATE`` (utilizzando la revoca OAuth Status List), il set di attributi dell'Utente, nella Credenziale Elettronica aggiornata, non corrisponde a quello nella Credenziale Elettronica memorizzata. In questo caso, l'Istanza del Wallet DEVE richiedere l'autorizzazione dell'Utente per memorizzare la nuova Credenziale Elettronica aggiornata.
  
  Se invece, lo stato della Credenziale Elettronica è impostato su ``UPDATE`` (utilizzando la revoca OAuth Status List) o ``credential_status_detail.state`` è impostato su ``UPDATE`` (utilizzando la revoca OAuth Status List), solo i parametri dei metadati della Credenziale sono cambiati. In questo caso, l'Istanza del Wallet DOVREBBE memorizzare la nuova Credenziale Elettronica senza richiedere l'autorizzazione e il consenso espliciti dell'utente.


Flusso di Ri-Rilascio: Considerazioni di Sicurezza
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Per garantire l'integrità e la sicurezza del processo di ri-rilascio, si applicano le seguenti considerazioni di sicurezza.

  - Limitazioni dell'Access Token: Un Access Token ottenuto come risultato di un flusso di Refresh Token NON DEVE essere utilizzato per il rilascio per la prima volta di una Credenziale Elettronica. Ciò garantisce che vengano aggiornate solo le Credenziali esistenti nell'Istanza del Wallet.
  - Scadenza della Credenziale: Il Credential Issuer DEVE impostare la stessa data di scadenza per la Credenziale Elettronica ri-emessa come quella precedente. Ciò impedisce rinnovi indefiniti della Credenziale senza una corretta autenticazione dell'Utente.
  - Consenso dell'Utente: Per i processi di ri-rilascio attivati da modifiche agli attributi, il consenso dell'Utente DEVE essere ottenuto prima di memorizzare la nuova Credenziale Elettronica. Ciò garantisce che l'Utente sia consapevole e accetti le informazioni aggiornate.
  - Refresh Token vincolato al mittente: I Refresh Token DEVONO essere crittograficamente vincolati all'Istanza del Wallet utilizzando il protocollo DPoP. Ciò mitiga il rischio di uso improprio del token garantendo che solo l'Istanza del Wallet prevista (la stessa che ha originariamente ottenuto la Credenziale Elettronica) possa utilizzare quel Refresh Token.

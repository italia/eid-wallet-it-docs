.. include:: ../common/common_definitions.rst

Metadati della Relying Party
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

I metadati *openid_credential_verifier* DEVONO contenere i seguenti parametri.

.. list-table::
  :class: longtable
  :widths: 20 60
  :header-rows: 1

  * - **Claim**
    - **Descrizione**
  * - **client_id**
    - DEVE contenere un URL HTTPS che identifica in modo univoco la RP. Vedi :rfc:`7591#section-3.2.1` e `OpenID Connect Dynamic Client Registration 1.0 <https://openid.net/specs/openid-connect-registration-1_0.html>`_ Sezione 3.2.
  * - **client_name**
    - Stringa leggibile dall'uomo che rappresenta il nome della RP. Vedi :rfc:`7591#section-2`.
  * - **application_type**
    - Stringa che indica il tipo di applicazione. DEVE essere impostata al valore "*web*". Vedi `OpenID Connect Dynamic Client Registration 1.0 <https://openid.net/specs/openid-connect-registration-1_0.html>`_ Sezione 2.
  * - **request_uris**
    - Array JSON di valori *request_uri* che sono pre-registrati dalla RP. Questi URL DEVONO utilizzare lo schema *https*. Vedi `OpenID Connect Dynamic Client Registration 1.0 <https://openid.net/specs/openid-connect-registration-1_0.html>`_ Sezione 2.
  * - **response_uris**
    - Array JSON di stringhe URI di risposta a cui l'Istanza del Wallet DEVE inviare la Risposta di Autorizzazione utilizzando una richiesta HTTP POST come definito dalle Modalità di Risposta ``direct_post`` e ``direct_post.jwt`` (vedi `OpenID4VP`_ Draft 20 Sezioni 6.2 e 6.3).
  * - **authorization_signed_response_alg**
    - Stringa che rappresenta l'algoritmo di firma [:rfc:`7515`] *alg* che DEVE essere utilizzato per firmare le risposte di autorizzazione. L'algoritmo "*none*" NON DEVE essere utilizzato. Vedi `JARM`_.
  * - **authorization_encrypted_response_alg**
    - Algoritmo utilizzato per crittografare la risposta di autorizzazione. Specifica all'Istanza del Wallet l'algoritmo di crittografia asimmetrica. Vedi `JARM`_.
  * - **authorization_encrypted_response_enc**
    - Algoritmo di crittografia utilizzato per la risposta di autorizzazione. Specifica all'Istanza del Wallet l'algoritmo di crittografia simmetrica. Vedi `JARM`_.
  * - **vp_formats**
    - Oggetto JSON che definisce i formati e i tipi di prova delle Presentazioni Verificabili e delle Credenziali Verificabili supportate dalla RP. Consiste in un elenco di coppie nome/valore, dove ogni nome identifica in modo univoco un tipo supportato. La RP DEVE supportare almeno "*dc+sd-jwt*". Il valore associato a ciascuna coppia nome/valore DEVE essere un oggetto JSON "**sd-jwt_alg_values**" che DEVE contenere un array JSON contenente identificatori di algoritmi crittografici che la RP supporta per la protezione di un SD-JWT. L'intestazione JOSE *alg* (come definito in :rfc:`7515`) dell'SD-JWT presentato DEVE corrispondere a uno dei valori dell'array. Vedi anche `OpenID4VP`_ Draft 20 Sezione 9.1.
  * - **jwks**
    - Documento JSON Web Key Set, passato per valore, contenente le chiavi specifiche del protocollo per la Relying Party. Vedi `JARM`_ Sezione 3, `OID-FED`_ Draft 41 Sezione 5.2.1 e `JWK`_.
  * - **erasure_endpoint**
    - [CONDIZIONALE] Stringa JSON che rappresenta l'URI a cui l'Istanza del Wallet può richiedere la cancellazione degli attributi degli Utenti. Questo URL DEVE utilizzare lo schema *https*. Questo endpoint DEVE essere presente ogni volta che le Relying Party richiedono attributi che possono identificare in modo univoco gli Utenti, come il claim tax_id_code del PID.


.. note::
  I parametri **response_uris** e **erasure_endpoint** sono introdotti in questa specifica.

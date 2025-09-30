.. include:: ../common/common_definitions.rst

Metadati della Relying Party
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

I metadata *openid_credential_verifier* DEVONO contenere i seguenti parametri.

.. list-table::
  :class: longtable
  :widths: 20 60
  :header-rows: 1

  * - **Claim**
    - **Descrizione**
  * - **client_id**
    - DEVE contenere un URL HTTPS che identifica in modo univoco la RP. Vedi :rfc:`7591#section-3.2.1` e `OpenID Connect Dynamic Client Registration 1.0 <https://openid.net/specs/openid-connect-registration-1_0.html>`_ Sezione 3.2.
  * - **client_name**
    - Stringa leggibile che rappresenta il nome della RP. Vedi :rfc:`7591#section-2`.
  * - **application_type**
    - Stringa che indica il tipo di applicazione. DEVE essere impostata al valore "*web*". Vedi `OpenID Connect Dynamic Client Registration 1.0 <https://openid.net/specs/openid-connect-registration-1_0.html>`_ Sezione 2.
  * - **request_uris**
    - JSON Array di valori ``request_uri`` che sono pre-registrati dalla RP. Questi URL DEVONO utilizzare lo schema *https*. Vedi `OpenID Connect Dynamic Client Registration 1.0 <https://openid.net/specs/openid-connect-registration-1_0.html>`_ Sezione 2.
  * - **response_uris**
    - JSON Array di stringhe URI di risposta a cui l'Istanza del Wallet DEVE inviare la Risposta di Autorizzazione utilizzando una richiesta HTTP POST come definito dalle Modalità di Risposta ``direct_post`` e ``direct_post.jwt`` (vedi `OpenID4VP`_ Draft 20 Sezioni 6.2 e 6.3).
  * - **encrypted_response_enc_values_supported**
    - Array JSON degli algoritmi di cifratura dei contenuti che il Verifier supporta per cifrare la risposta di autorizzazione quando si utilizza la modalità di risposta ``direct_post.jwt``. Vedi `OpenID4VP`_ §5.1 e §8.3.1.
  * - **vp_formats_supported**
    - Oggetto JSON che definisce i formati e i tipi di prova delle Verifiable Presentations e delle Verifiable Credentials supportati dalla RP. È composto da una lista di coppie nome/valore, dove ogni nome identifica in modo univoco un tipo supportato. La RP DEVE supportare almeno ``dc+sd-jwt``. Per le SD-JWT VC, il valore associato a ciascuna coppia nome/valore DEVE includere ``sd-jwt_alg_values_supported`` che elenca gli algoritmi di firma accettati; per mdoc, includere ``alg_values_supported``. Gli header JOSE/COSE degli artefatti presentati DEVONO corrispondere a uno dei valori dichiarati. Vedi `OpenID4VP`_ §11 e Appendice B.
  * - **jwks**
    - Documento JSON Web Key Set, passato per valore, contenente le chiavi specifiche del protocollo per la Relying Party. Vedi `JARM`_ Sezione 3, `OID-FED`_ Draft 41 Sezione 5.2.1 e `JWK`_.
  * - **erasure_endpoint**
    - [CONDIZIONALE] Stringa JSON che rappresenta l'URI a cui l'Istanza del Wallet può richiedere la cancellazione degli attributi degli Utenti. Questo URL DEVE utilizzare lo schema ``https``. Questo endpoint DEVE essere presente ogni volta che le Relying Party richiedono attributi che possono identificare in modo univoco gli Utenti, come il claim ``tax_id_code`` del PID.


.. note::
  I parametri ``response_uris`` e ``erasure_endpoint`` sono introdotti in questa specifica.

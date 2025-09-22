.. include:: ../common/common_definitions.rst

Metadati della Relying Party
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

I metadata *openid_credential_verifier* DEVONO contenere i seguenti parametri (:ref:`test-plans-remote-presentation:Matrice di Test per la Presentazione di Credenziali Remota`).

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
    - JSON Array di valori ``request_uri`` che sono pre-registrati dalla RP. Questi URL DEVONO utilizzare lo schema *https*. Vedi `OpenID Connect Dynamic Client Registration 1.0 <https://openid.net/specs/openid-connect-registration-1_0.html>`_ Sezione 2 (:ref:`test-plans-remote-presentation:RPR-07`, :ref:`test-plans-remote-presentation:RPR-08`, :ref:`test-plans-remote-presentation:RPR-09`, :ref:`test-plans-remote-presentation:RPR-35`, :ref:`test-plans-remote-presentation:RPR-49`, :ref:`test-plans-remote-presentation:RPR-60`, :ref:`test-plans-remote-presentation:RPR-76`).
  * - **response_uris**
    - JSON Array di stringhe URI di risposta a cui l'Istanza del Wallet DEVE inviare la Risposta di Autorizzazione utilizzando una richiesta HTTP POST come definito dalle Modalità di Risposta ``direct_post`` e ``direct_post.jwt`` (vedi `OpenID4VP`_ Draft 20 Sezioni 6.2 e 6.3) (:ref:`test-plans-remote-presentation:RPR-12`, :ref:`test-plans-remote-presentation:RPR-13`, :ref:`test-plans-remote-presentation:RPR-17`, :ref:`test-plans-remote-presentation:RPR-18`, :ref:`test-plans-remote-presentation:RPR-19`, :ref:`test-plans-remote-presentation:RPR-20`, :ref:`test-plans-remote-presentation:RPR-24`, :ref:`test-plans-remote-presentation:RPR-28`, :ref:`test-plans-remote-presentation:RPR-29`, :ref:`test-plans-remote-presentation:RPR-32`, :ref:`test-plans-remote-presentation:RPR-33`, :ref:`test-plans-remote-presentation:RPR-36`, :ref:`test-plans-remote-presentation:RPR-37`, :ref:`test-plans-remote-presentation:RPR-40`, :ref:`test-plans-remote-presentation:RPR-41`, :ref:`test-plans-remote-presentation:RPR-44`, :ref:`test-plans-remote-presentation:RPR-45`, :ref:`test-plans-remote-presentation:RPR-52`, :ref:`test-plans-remote-presentation:RPR-53`, :ref:`test-plans-remote-presentation:RPR-54`, :ref:`test-plans-remote-presentation:RPR-55`, :ref:`test-plans-remote-presentation:RPR-57`, :ref:`test-plans-remote-presentation:RPR-58`, :ref:`test-plans-remote-presentation:RPR-63`, :ref:`test-plans-remote-presentation:RPR-64`, :ref:`test-plans-remote-presentation:RPR-67`, :ref:`test-plans-remote-presentation:RPR-68`, :ref:`test-plans-remote-presentation:RPR-71`, :ref:`test-plans-remote-presentation:RPR-72`).
  * - **authorization_signing_alg_values_supported**
    - JSON Array che contiene la lista degli algoritmi di firma [:rfc:`7515`] *alg* che DEVONO essere utilizzati per firmare le authorization response. L'algoritmo ``none`` NON DEVE essere utilizzato. Vedi `OIDC-RP-Metadata`_.
  * - **authorization_encryption_alg_values_supported**
    - JSON Array che contiene la lista degli algoritmi utilizzati per crittografare le authorization response. Questo parametro specifica alla Wallet Instance gli algoritmi di crittografia asimmetrica supportati. Vedi `OIDC-RP-Metadata`_.
  * - **authorization_encryption_enc_values_supported**
    - JSON Array che contiene la lista  degli algoritmi di crittografia utilizzati per le authorization response. Questo parametro pecifica alla Wallet Instance gli algoritmi di crittografia simmetrica supportati. Vedi `OIDC-RP-Metadata`_.
  * - **vp_formats**
    - JSON Object che definisce i formati e i tipi di prova delle Presentazioni Verificabili e delle Credenziali Verificabili supportate dalla RP. Consiste in un elenco di coppie nome/valore, dove ogni nome identifica in modo univoco un tipo supportato. La RP DEVE supportare almeno ``dc+sd-jwt``. Il valore associato a ciascuna coppia nome/valore DEVE essere un oggetto JSON ``sd-jwt_alg_values`` che DEVE contenere un array JSON contenente identificatori di algoritmi crittografici che la RP supporta per la protezione di un SD-JWT. L'intestazione JOSE ``alg`` (come definito in :rfc:`7515`) dell'SD-JWT presentato DEVE corrispondere a uno dei valori dell'array. Vedi anche `OpenID4VP`_ Draft 20 Sezione 9.1 (:ref:`test-plans-remote-presentation:RPR-10`, :ref:`test-plans-remote-presentation:RPR-23`).
  * - **jwks**
    - Documento JSON Web Key Set, passato per valore, contenente le chiavi specifiche del protocollo per la Relying Party. Vedi `JARM`_ Sezione 3, `OID-FED`_ Draft 41 Sezione 5.2.1 e `JWK`_.
  * - **erasure_endpoint**
    - [CONDIZIONALE] Stringa JSON che rappresenta l'URI a cui l'Istanza del Wallet può richiedere la cancellazione degli attributi degli Utenti. Questo URL DEVE utilizzare lo schema ``https``. Questo endpoint DEVE essere presente ogni volta che le Relying Party richiedono attributi che possono identificare in modo univoco gli Utenti, come il claim tax_id_code del PID.


.. note::
  I parametri ``response_uris`` e ``erasure_endpoint`` sono introdotti in questa specifica.

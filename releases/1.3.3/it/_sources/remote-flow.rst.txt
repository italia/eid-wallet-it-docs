.. include:: ../common/common_definitions.rst


Flusso Remoto
=============

A seconda di come l'Utente stia interagendo con il frontend dell'App di Verifica Web, usando cioè il dispositivo in cui risiede l'Unità Wallet (**Same Device**) oppure un altro dispositivo (**Cross Device**), la Relying Party DEVE supportare i seguenti flussi remoti (:ref:`RPR-84 <test-plans-remote-presentation:Matrice di Test per il Verificatore di Credenziali in Remoto>`):

* **Same Device**: essa DEVE fornire un indirizzo ``HTTP`` all'Istanza del Wallet utilizzando un *redirect* (``302``) o un href HTML nella pagina web (:ref:`RPR-01 <test-plans-remote-presentation:Matrice di Test per il Verificatore di Credenziali in Remoto>`);
* **Cross Device**: essa DEVE fornire un indirizzo ``HTTP`` tramite un Codice QR che l'Utente scansiona con la fotocamera del proprio dispositivo oppure con l'Istanza del Wallet (:ref:`RPR-03 <test-plans-remote-presentation:Matrice di Test per il Verificatore di Credenziali in Remoto>`).

Per richiamare l'Istanza del Wallet corretta, la Relying Party DOVREBBE invocare l'Istanza del Wallet installata sul dispositivo dell'Utente che l'Utente desidera utilizzare. 
Queste informazioni DOVREBBERO essere fornite dall'Utente utilizzando la Selection Page descritta in :ref:`functionalities:Design dell'Esperienza Utente`. 

-  Se la Selection Page è disponibile, l'utente seleziona l'Istanza del Wallet, quindi la Relying Party recupera i Wallet metadata come descritto in :ref:`wallet-metadata-retrieval:Flusso di Recupero dei Wallet Metadata`. Il contenuto del HTML href o del QR Code dipende dal parametro ``authorization_endpoint`` nei Wallet metadata:

  - Se ``authorization_endpoint`` è disponibile e contiene un URL HTTPS (Universal Link), la Relying Party DOVREBBE utilizzare quell'endpoint.
  - Altrimenti, la Relying Party DEVE utilizzare uno degli schemi URL personalizzati: ``openid4vp://`` (come definito nella Sezione 13.1.2 di [`OpenID4VP`_]) o ``haip-vp://`` (come definito nella Sezione 5.1 di [`OPENID4VC-HAIP`_]). L'Istanza del Wallet DEVE supportare entrambi gli schemi URL personalizzati.

-  Nel caso in cui la Relying Party non supporti la Selection Page o il recupero dei Wallet metadata fallisce per qualche motivo, la Relying Party richiamerà l'Istanza del Wallet utilizzando uno degli schemi URL personalizzati descritti precedentemente.

Successivamente all'invocazione dell'Istanza del Wallet, l'Istanza del Wallet valida la trust con la Relying Party e ne valuta la richiesta. Se valida e l'Utente fornisce il consenso per la divulgazione dei propri Attestati Elettronici, li invia sotto forma di Verifiable Presentation.

.. _fig_High-Level-Flow-Presentation:
.. plantuml:: plantuml/credential-presentation-remote-high-level-flow.puml
    :width: 99%
    :alt: La figura illustra il Flusso Remoto ad Alto Livello.
    :caption: `Flusso di Protocollo Remoto di Alto Livello. <https://www.plantuml.com/plantuml/svg/TP9FJy904CNl-oacN9GcslZVS30OGWmdQeLmCI5BEz2LTNVTtThKJ-yEGcqndffqthptU-qCdUVMb--IcV0KcJ1SUUWjk9JeOQB2M6NO0-wWwafIbBLG6qZ2otedi8OnQ-3i0Qe1N9n353sMlj1MV74lj88KFqfqFeh05rQNcm8ivi9Yva5RU4uXqpc2oxW2huC6NnN4yG_AYOEksLZbHWlbuvWnBZs8zS4VfgitybpLmN-D5aC1nYhYicO0bmHsaCxJIGlhz6ay8vHa-ZBhxna2GPg4zFP6ExifVFNNrncj799nTGJNPmnLlgSAozUql9Z0gC1iwyB6x-Y6HdE75aRafWYqLUUMnWJS_Jv7wPzcwVKMrL6hHlLFBGgus_LAscXDvtkQTGwXawiDeN0fQwYQVxqihUYpOQWVhkuR>`_


.. .. figure:: ../../images/High-Level-Flow-Presentation.svg
..     :figwidth: 100%
..     :align: center
..     :target: https://www.plantuml.com/plantuml/svg/TL9TJy8m57tlhpZXHLcYYz-61uCXnF34d11UJCZS6bQPRMtlRF3NspB0JUBJidlEFH-v7LhA3DKV5TF-AtAXCqdeBRAgueI9zB3CUG-PXUjIKbvjX5mXySFDbc0qOqRZx05kW8jpHD5ZJQKouZiZeIHI_bbpIr64KmVJ_2nh8_gWqgXwLVfX8GpF2ShWEKMk2WwRPnAlafHdSSHn4-t4eYi-beLMGb8SC-P21gC7k0mXThQOfvDsXAVnBDWaqvTP7mVrDF7AxOssxg7SrR6krKfQtdJR8zEtTr-cpvZRxLs7lSK4evBdQ-l9lz1DWEQM6uo2a2IFjfhS1ZXa_LExQ_obbwJMN1uNQbZ_D0e6TzjAIJlQeUvzm3htxlWg7QBuispWzYTi3ilOaCl2lwuV

..     High Level Remote Protocol Flow


Una descrizione ad alto livello del flusso remoto, dal punto di vista dell'Utente, è fornita di seguito e mostrata in :ref:`fig_High-Level-Flow-Presentation`:

  1. *Authorization Request*: l'Istanza del Wallet ottiene un ``URL`` nel flusso Same Device o un Codice QR nel flusso Cross Device contenente direttamente il Request Object firmato (Request Object by value) oppure un puntatore a dove il Request Object firmato è disponibile per il download (Request Object by reference). Se Request Object by reference, vengono eseguiti anche i passaggi 2 e 3.
  2. *Richiesta URI Request*: l'Istanza del Wallet estrae dal payload i seguenti parametri: ``client_id``, ``request_uri``, ``request_uri_method``.

    * Se ``request_uri_method`` è fornito e impostato con il valore ``post``, l'Istanza del Wallet DOVREBBE trasmettere i suoi metadata all'endpoint ``request_uri`` della Relying Party utilizzando il metodo HTTP ``POST``.
    * Se ``request_uri_method`` è impostato con il valore ``get`` o non è presente, l'Istanza del Wallet DEVE recuperare il Request Object firmato utilizzando una richiesta HTTP con metodo ``GET`` all'endpoint fornito nel parametro ``request_uri`` (:ref:`RPR-78 <test-plans-remote-presentation:Matrice di Test per il Verificatore di Credenziali in Remoto>`).

  3. *URI Request Response*: la Relying Party restituisce un Request Object firmato all'Istanza del Wallet.
  4. *Controlli Istanza di Wallet*: l'Istanza del Wallet:

    a. verifica la firma del Request Object firmato utilizzando la chiave pubblica identificata nell'intestazione JWT del Request Object. Utilizzando tale riferimento, l'Istanza del Wallet è in grado di selezionare la corretta chiave pubblica della Relying Party per la verifica della firma (:ref:`WP_085 <wallet-credential-presentation-testcases>`).
    b. verifica che il ``client_id`` contenuto nel Request Object (Relying Party) corrisponda a quello ottenuto al passaggio 2:
    
       * Se ``client_id`` utilizza il prefisso ``openid_federation``, DEVE corrispondere al parametro ``sub`` contenuto nella Entity Configuration della Relying Party all'interno della Trust Chain (:ref:`WP_086 <wallet-credential-presentation-testcases>`).
       * Se ``client_id`` utilizza il prefisso ``x509_hash``, l'Istanza del Wallet DEVE verificare che l'hash del certificato X.509 della Relying Party (nell'intestazione ``x5c`` della richiesta) corrisponda all'hash contenuto in ``client_id`` del passaggio 2 (come definito in `OpenID4VP`_, Sezione 5.9.3).

    c. valuta gli Attestati Elettronici richiesti e verifica l'idoneità della Relying Party nel richiedere questi ultimi. Ad esempio, applicando le politiche relative a quella specifica Relying Party ottenute con la Trust Chain (:ref:`WP_087 <wallet-credential-presentation-testcases>`).

  5. *Risposta di Autorizzazione POST*: l'Istanza del Wallet presenta le informazioni richieste alla Relying Party.
  6. *Controlli RP*: La Relying Party convalida le Credenziali presentate verificando la fiducia con i loro Fornitori di Attestati Elettronici e controlla i rispettivi stati di validità.
  7. *Risposta della Relying Party*: l'Istanza del Wallet informa l'Utente dell'autenticazione riuscita con la Relying Party, e l'Utente continua la navigazione.

Di seguito è riportato un diagramma di sequenza che dettaglia le interazioni tra tutte le parti coinvolte.

.. plantuml:: plantuml/credential-presentation-remote-flow.puml
    :width: 99%
    :alt: La figura illustra il Flusso Remoto.
    :caption: `Flusso di Protocollo Remoto. <https://www.plantuml.com/plantuml/svg/fLPDRnit4BtpLmpKGssWIPCU3RX8eXgnaxHMBIM-630exaXYJP5RSYX5BVBVEuFHhZwK5W6gcxGpxyrxyx5wLSXcgijWRAKKwtAAsHZpsb7ACFXOC0_05gZ6JDDd_U7x0h_WoZii0_ZkWvylw4seQ5h6ySwtDX8Cxcq8I70J6Juw50nO7uPKXdfcvnX96Qp1s02pRAdkC6nydCE8apR_pdGGzX3FRbzNMi0mU0O-5sHO7MLmILGBC5kR_9QzOC_E7-l8homXowxmx6UezWBkSGfZpA8RebtvkIMVubweDGtk9rh9NE45tE6V5Gl1A2T2HzZmBoNLxD2Ooql-6Gj6iW87euKj29UNFQvKly8EYlri6G9stW5jMdo8bA11GGUNKodyHGg5bA7O9UfN1L8r2re6Q1a1rfxj-lrkc1e9XqN66RZ4zVWejj82eUO0lJWjoMprrGiOBz9QmZeGGHKa5xnxaWUAEQr4AHvuP7SgryRCSwej3BdyRhuWnR0nQ-5PCu-paJb0IAHPHdgZZpuaPmF8R8Ajp1Z9EsrFdtsrig4A4-LQI5Lpf5J9uO-UuMmWyBE-NRVJFyJFwGQuVCmOsK3WppOiQzXZpVvnYRH83NYPeotsw7OyCQ2VTTS-de2LRn2ssy5fjh5aWPBKiW_PJsU7iMy-w6St5ZjnYnwSq4KljZZRsgaFdZmMISLGy1i4lBsQI1TZ8cXrGa_aT4u9Q_7pY4q72adDc-Mq_4zfA7rKBThB3kYm2qORVZI3fyqzE0RmQ-UlZGsqANWd5dH9dp3xsGQ4prBD26dMAJajO9TbWsVCNX57VXgTbNCDg3jJPYdB7ebnH_T4WOOfpdnUOdDuDdfpPO10RbdA_Yyz3dmsMa64XwWzMhMFb9um_W1oq_3aQ9nEXwhsTXhmyF2GuEmblIOI5SECZQoJ3N1JIiKC4zcVXoYUxinuTp-1SMUaedG3xx0KtRGUofWS4sUb5MOEuzD-y_PwylRkwkety_MC2mFFOBX0FYZNAJISzXutyCR7HhejfN1UcaaBHwaK1X1DjSXJaFaIkBPEWtVmn9dJL3d7H_bzNoCbhaV6GhqQgItFZT1VVQPidKvxuuiBgM03bYZxQIKi86KugL6souRG3xvd0j11p0XsPNsG1ZoNeHOdqEnPzh5jjhtIWzQ9ENCfFNc4Ai-nEJVTnHpBWTU3gLF1RCpeI9RDx1RhUZ8P_VZo-KluwSKBk7tFBVnxi1ywaBS2jKNEVGUay_RevAv_sOwuvHgB5dZ0j7VNHTZN3te-AJTL-iQAznTbVNGBz6rKs3zunmQFNVOjQJSkZju9kYkoGsT2q2soIbQJptTY2fgY1LNxlptyeYTi1wr67VnNKB3kbT3s_nco_cSuMVAkjD5fvD7Bzj2nLqnTb-4V>`_


.. .. figure:: ../../images/cross_same_device_auth_seq_diagram.svg
..     :figwidth: 100%
..     :align: center
..     :target: https://www.plantuml.com/plantuml/svg/fLPDRnit4BtpLmpKGssWIPCU3RX8eXgnaxHMBIM-630exaXYJP5RSYX5BVBVEuFHhZwK5W6gcxGpxyrxyx5wLSXcgijWRAKKwtAAsHZpsb7ACFXOC0_05gZ6JDDd_U7x0h_WoZii0_ZkWvylw4seQ5h6ySwtDX8Cxcq8I70J6Juw50nO7uPKXdfcvnX96Qp1s02pRAdkC6nydCE8apR_pdGGzX3FRbzNMi0mU0O-5sHO7MLmILGBC5kR_9QzOC_E7-l8homXowxmx6UezWBkSGfZpA8RebtvkIMVubweDGtk9rh9NE45tE6V5Gl1A2T2HzZmBoNLxD2Ooql-6Gj6iW87euKj29UNFQvKly8EYlri6G9stW5jMdo8bA11GGUNKodyHGg5bA7O9UfN1L8r2re6Q1a1rfxj-lrkc1e9XqN66RZ4zVWejj82eUO0lJWjoMprrGiOBz9QmZeGGHKa5xnxaWUAEQr4AHvuP7SgryRCSwej3BdyRhuWnR0nQ-5PCu-paJb0IAHPHdgZZpuaPmF8R8Ajp1Z9EsrFdtsrig4A4-LQI5Lpf5J9uO-UuMmWyBE-NRVJFyJFwGQuVCmOsK3WppOiQzXZpVvnYRH83NYPeotsw7OyCQ2VTTS-de2LRn2ssy5fjh5aWPBKiW_PJsU7iMy-w6St5ZjnYnwSq4KljZZRsgaFdZmMISLGy1i4lBsQI1TZ8cXrGa_aT4u9Q_7pY4q72adDc-Mq_4zfA7rKBThB3kYm2qORVZI3fyqzE0RmQ-UlZGsqANWd5dH9dp3xsGQ4prBD26dMAJajO9TbWsVCNX57VXgTbNCDg3jJPYdB7ebnH_T4WOOfpdnUOdDuDdfpPO10RbdA_Yyz3dmsMa64XwWzMhMFb9um_W1oq_3aQ9nEXwhsTXhmyF2GuEmblIOI5SECZQoJ3N1JIiKC4zcVXoYUxinuTp-1SMUaedG3xx0KtRGUofWS4sUb5MOEuzD-y_PwylRkwkety_MC2mFFOBX0FYZNAJISzXutyCR7HhejfN1UcaaBHwaK1X1DjSXJaFaIkBPEWtVmn9dJL3d7H_bzNoCbhaV6GhqQgItFZT1VVQPidKvxuuiBgM03bYZxQIKi86KugL6souRG3xvd0j11p0XsPNsG1ZoNeHOdqEnPzh5jjhtIWzQ9ENCfFNc4Ai-nEJVTnHpBWTU3gLF1RCpeI9RDx1RhUZ8P_VZo-KluwSKBk7tFBVnxi1ywaBS2jKNEVGUay_RevAv_sOwuvHgB5dZ0j7VNHTZN3te-AJTL-iQAznTbVNGBz6rKs3zunmQFNVOjQJSkZju9kYkoGsT2q2soIbQJptTY2fgY1LNxlptyeYTi1wr67VnNKB3kbT3s_nco_cSuMVAkjD5fvD7Bzj2nLqnTb-4V

..     Remote Protocol Flow


I dettagli di ogni passaggio mostrato nell'immagine precedente sono descritti di seguito.

**Passaggi 1-2**: L'Utente richiede di accedere a una risorsa protetta della Relying Party.

**Passaggio 3**: La Relying Party crea un valore *state* legato allo user-agent (ad esempio, utilizzando un cookie HTTP contrassegnato *Secure* e *HttpOnly*) e ispeziona lo user-agent dell'utente per determinare se il flusso avviene sullo stesso dispositivo dello user-agent.

**Passaggi 4-7 (Authorization Request)**: La Relying Party fornisce allo user-agent una pagina JavaScript che ispeziona lo *state endpoint* e all'Istanza del Wallet un URL contenente l'Authorization Request. 

  Nel **Flusso Cross Device**, l'URI dell'Authorization Request viene presentato attraverso un Codice QR mostrato all'Utente. L'Utente scansiona il Codice QR utilizzando l'Istanza del Wallet e recupera un URL.
  Di seguito è rappresentato un esempio non normativo di un Codice QR emesso dalla Relying Party.

  .. only:: format_html

    .. figure:: ./images/svg/verifier_qr_code.svg
      :figwidth: 50%
      :align: center

  .. only:: format_latex

    .. figure:: ./images/pdf/verifier_qr_code.pdf
      :width: 50%
      :align: center

  .. note::
    Il *livello di correzione degli errori* scelto per il Codice QR DEVE essere Q (Quartile - fino al 25%), poiché offre un buon equilibrio tra capacità di correzione degli errori e densità/spazio dei dati. Questo livello di qualità e correzione degli errori consente al Codice QR di rimanere leggibile anche se è danneggiato o parzialmente oscurato (:ref:`RPR-77 <test-plans-remote-presentation:Matrice di Test per il Verificatore di Credenziali in Remoto>`).

  Se il Request Object viene passato per valore (by value), l'URL all'interno del codice QR contiene i parametri ``client_id`` e ``request``. 
  Di seguito è rappresentato un esempio non normativo del contenuto del Codice QR per un Request Object by value:

  .. code-block:: text

    https://wallet-solution.example.org/authorization?client_id=openid_federation%3A%2F%2Frelying-party.example.org&request=eyJhbGciOiJFUzI1NiIs...9t2LQ

  Se invece il Request Object viene passato per riferimento (by reference), l'URL all'interno del codice QR contiene i parametri ``client_id``, ``request_uri`` e ``request_uri_method`` (:ref:`WP_076–077 <wallet-credential-presentation-testcases>`).
  Di seguito è riportato un esempio non normativo del contenuto del codice QR per un Request Object by reference:

  .. code-block:: text

    https://wallet-solution.example.org/authorization?client_id=openid_federation%3A%2F%2Frelying-party.example.org&request_uri=https%3A%2F%2Frelying-party.example.org&request_uri_method=post

  Mentre, nel **Flusso Same Device**, la Relying Party risponde tramite HTTP Response Redirect (con codice di stato impostato a ``302``) o mostra all'utente una pagina html con un pulsante href, aventi l'URL che fornisce le stesse informazioni del Flusso Cross Device (:ref:`WP_076–077 <wallet-credential-presentation-testcases>`). 
  Di seguito è riportato un esempio non normativo per un Request Object by reference:

  .. code-block:: http

    HTTP/1.1 302 Found
    Location: https://wallet-solution.digital-strategy.europa.eu?client_id=openid_federation%3A%2F%2Frelying-party.example.org%2Fcb&request_uri=https%3A%2F%2Frelying-party.example.org%2Frequest_uri&request_uri_method=post


**Passaggio 8**: L'Istanza del Wallet valuta la trust con la Relying Party (:ref:`WP_078–080 <wallet-credential-presentation-testcases>`).

**Passaggi 9-11 (Richiesta URI Request)**: L'Istanza del Wallet verifica se la Relying Party ha fornito il request_uri_method all'interno del suo Request Object firmato (:ref:`WP_083 <wallet-credential-presentation-testcases>`).

  - Se è fornito ed è uguale a post, l'Istanza del Wallet DOVREBBE fornire i suoi metadata alla Relying Party. La Relying Party aggiorna il Request Object in base alle capacità tecniche del Wallet.

    Di seguito è riportato un esempio non normativo di una richiesta HTTP effettuata dall'Istanza del Wallet alla Relying Party.

    .. code-block:: http

      POST /request HTTP/1.1
      Host: client.example.org
      Content-Type: application/x-www-form-urlencoded
      Accept: application/oauth-authz-req+jwt

      wallet_metadata=%7B%22authorization_endpoint%22%3A%20%22eudiw%3A%22%2C%20%22response_types_supported%22%3A%20%5B%22vp_token%22%5D%2C%20%22response_modes_supported%22%3A%20%5B%22query%22%5D%2C%20%22vp_formats_supported%22%3A%20%7B%22dc%2Bsd-jwt%22%3A%20%7B%22sd-jwt_alg_values%22%3A%20%5B%22ES256%22%2C%20%22ES384%22%5D%7D%7D%2C%20%22request_object_signing_alg_values_supported%22%3A%20%5B%22ES256%22%5D%7D%2C&wallet_nonce=%22qPmxiNFCR3QTm19POc8u%22

    Dove il corpo della richiesta prima di essere codificato in ``application/x-www-form-urlencoded`` dal Wallet corrisponde a:

    .. code-block:: json

      {
        "wallet_metadata": {
          "authorization_endpoint": "https://wallet-solution.digital-strategy.europa.eu/authorization",
          "response_types_supported": [
            "vp_token"
          ],
          "response_modes_supported": [
            "query"
          ],
          "vp_formats_supported": {
            "dc+sd-jwt": {
                "sd-jwt_alg_values": [
                  "ES256",
                  "ES384"
                ]
            }
          },
          "request_object_signing_alg_values_supported": [
            "ES256"
          ],
          "client_id_prefixes_supported": ["openid_federation", "x509_hash"],
        },
        "wallet_nonce": "qPmxiNFCR3QTm19POc8u"
      }

  - Quando la Relying Party non supporta ``request_uri_method`` con valore ``post``, l'Istanza del Wallet richiede il Request Object firmato utilizzando il metodo HTTP GET (:ref:`WP_082 <wallet-credential-presentation-testcases>`).

**Passaggio 12 (URI Request Response)**: La Relying Party emette il Request Object firmandolo utilizzando una delle sue chiavi crittografiche private, le cui corrispondenti chiavi pubbliche sono state pubblicate all'interno della sua Entity Configuration (`metadata.openid_credential_verifier.jwks`) come estratto dall'Istanza del Wallet per :ref:`WP_084 <wallet-credential-presentation-testcases>`. L'Istanza del Wallet ottiene il Request Object firmato.

  Di seguito è riportato un esempio non normativo della Risposta URI di Reindirizzamento:

  .. code-block:: http

    HTTP/1.1 200 OK
    Content-Type: application/oauth-authz-req+jwt

    eyJhbGciOiJFUzI1NiIs...9t2LQ

  Un esempio non normativo di un Oggetto di Richiesta sotto forma di intestazione e payload decodificati è mostrato di seguito:

  .. code-block:: json

    {
      "alg": "ES256",
      "typ": "oauth-authz-req+jwt",
      "kid": "9tjiCaivhWLVUJ3AxwGGz_9",
      "trust_chain": [
        "MIICajCCAdOgAwIBAgIC...awz",
        "MIICajCCAdOgAwIBAgIC...2w3",
        "MIICajCCAdOgAwIBAgIC...sf2"
      ],
      "x5c": [
        "MIIDqjCCApKgAwIBAgIESLNEvDA ...",
        "MIICwzCCAasCCQCKVy9eKjvi+jA ...",
        "MIIDTDCCAjSgAwIBAgIJAPlnQYH..."
      ]
    }

  .. code-block:: json

    {
      "client_id": "openid_federation:https://relying-party.example.org",
      "response_mode": "direct_post.jwt",
      "response_type": "vp_token",
      "dcql_query": {
        "credentials": [
          {
            "id": "personal id data",
            "format": "dc+sd-jwt",
            "meta": {
              "vct_values": [ "urn:eudi:pid:it:1" ]
            },
            "claims": [
              {"path": ["given_name"]},
              {"path": ["family_name"]},
              {"path": ["personal_administrative_number"]}
            ]
          }
        ]
      },
      "response_uri": "https://relying-party.example.org/response_uri",
      "nonce": "2c128e4d-fc91-4cd3-86b8-18bdea0988cb",
      "wallet_nonce": "qPmxiNFCR3QTm19POc8u",
      "state": "3be39b69-6ac1-41aa-921b-3e6c07ddcb03",
      "iss": "https://relying-party.example.org",
      "iat": 1672418465,
      "exp": 1672422065
    }

**Passaggi 13-15 (Controlli WI)**: L'Istanza del Wallet verifica l'Oggetto di Richiesta, che è sotto forma di JWT firmato (:ref:`WP_085–086 <wallet-credential-presentation-testcases>`). Quindi elabora i metadati della Relying Party e applica le politiche pertinenti per determinare quali Credenziali Elettroniche e dati dell'Utente la Relying Party è autorizzata a richiedere (:ref:`WP_087 <wallet-credential-presentation-testcases>`).

**Passaggi 16-17 (Consenso dell'Utente)**: L'Istanza del Wallet richiede il consenso dell'Utente per divulgare gli Attetstati Elettronici richiesti mostrando l'identità della Relying Party e gli attributi richiesti. L'Utente autorizza e acconsente alla presentazione degli Attributi Elettronici selezionando e o deselezionando i dati personali da rilasciare (:ref:`WP_088 <wallet-credential-presentation-testcases>`).

**Passaggio 18 (Authorization Response)**: L'Istanza del Wallet fornisce la Authorization Response alla Relying Party utilizzando una richiesta HTTP con il metodo POST (modalità di risposta ``direct_post.jwt``).

  Di seguito è riportato un esempio non normativo della Authorization Response:

  .. code-block:: http

      POST /response_uri HTTP/1.1
      HOST: relying-party.example.org
      Content-Type: application/x-www-form-urlencoded

      response=eyJhbGciOiJFUzI1NiIs...9t2LQ

  Di seguito è riportato un esempio non normativo del payload decifrato del JWT contenuto nel parametro response, prima della codifica base64url. Il valore del parametro ``vp_token`` corrisponde al formato utilizzato quando il linguaggio di query DCQL viene utilizzato nella richiesta di presentazione.

  .. code-block:: json

      {
        "state": "3be39b69-6ac1-41aa-921b-3e6c07ddcb03",
        "vp_token": {
          "personal id data": ["eyJhbGciOiJFUzI1NiIs...PT0iXX0"]
        }
      }

**Passaggi 19-22 (Controlli RP)**: La Relying Party verifica la Risposta di Autorizzazione, estrae la Wallet Attestation per stabilire la fiducia con la Soluzione Wallet. Quindi estrae il ``vp_token`` che contiene una o più presentazioni di Attestati Elettronici di Attributi, e ne valida il formato complessivo.  Per ogni presentazione di un Attestato, la Relying Party ne verifica l’integrità secondo i criteri della query DCQL definiti nella Richiesta di Autorizzazione. La Relying Party DEVE anche attestare la fiducia con il relativo Fornitore di Attestati Elettronici e verificare la prova di possesso dell'Istanza del Wallet per ogni Attestato presentato. Infine, la Relying Party verifica lo stato di revoca di ogni Attestato presentato come descritto in :ref:`credential-revocation:Revoca e Sospensione degli Attestati Elettronici`. Se tutte le verifiche precedenti hanno dato esito positivo, la Relying Party aggiorna la sessione dell'Utente.

**Passaggi 23-24 o 25 (Risposta della Relying Party)**: La Relying Party fornisce all'Istanza del Wallet la risposta sulla presentazione, che a sua volta informa l'Utente.

  Dopo aver ricevuto e convalidato la Authorization Response al Response Endpoint, la Relying Party restituisce all'Istanza del Wallet un codice HTTP 200 OK. In particolare, nel Flusso Same Device, la Relying Party DOVREBBE anche passare il ``redirect_uri`` all'Istanza del Wallet. Dopo aver ricevuto il ``redirect_uri``, l'Istanza del Wallet DEVE eseguire un reindirizzamento all'URL specificato dal ``redirect_uri``. Questo reindirizzamento consente alla Relying Party di riprendere senza problemi l'interazione con l'Utente sul dispositivo che ha avviato il flusso. Quando la risposta non contiene il parametro ``redirect_uri``, l'Istanza del Wallet non è tenuta a eseguire ulteriori passaggi. L'Utente dovrebbe chiudere manualmente l'Istanza del Wallet e aprire lo user-agent per continuare il flusso (:ref:`RPR-83 <test-plans-remote-presentation:Matrice di Test per il Verificatore di Credenziali in Remoto>`).

  Di seguito è riportato un esempio non normativo della risposta nel Flusso Same Device.

.. code-block:: http

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
      "redirect_uri": "https://relying-party.example.org/cb?response_code=091535f699ea575c7937fa5f0f454aee"
    }

**Passaggi 26-27**: La pagina JavaScript continua ad ispezionare lo Status Endpoint.

  Di seguito è riportato un esempio non normativo della Richiesta HTTP allo Status Endpoint, dove il parametro ``id`` contiene un valore opaco e casuale:

  .. code-block:: http

      GET /session-state?id=3be39b69-6ac1-41aa-921b-3e6c07ddcb03 HTTP/1.1
      HOST: relying-party.example.org

  Quando l'Istanza del Wallet ha fornito la presentazione all'endpoint **response_uri** della Relying Party e l'autenticazione dell'Utente ha avuto successo. La Relying Party aggiorna il cookie di sessione consentendo all'user-agent di accedere alla risorsa protetta. Viene fornito un URL di reindirizzamento che trasporta la posizione in cui l'user-agent deve navigare.
  Di seguito è riportato un esempio non normativo della risposta con il redirect_uri dalla Relying Party all'user-agent.

  .. code-block:: http

      HTTP/1.1 200 OK
      Content-Type: application/json

      {
        "redirect_uri": "https://relying-party.example.org/cb?response_code=091535f699ea575c7937fa5f0f454aee"
      }

**Passaggi 28-29**: Lo user-agent viene reindirizzato al ``redirect_uri`` per continuare la navigazione con la risorsa protetta resa disponibile all'Utente (:ref:`WP_094 <wallet-credential-presentation-testcases>`).



Authorization Request
^^^^^^^^^^^^^^^^^^^^^^^^^

I parametri URL contenuti nella Authorization Request della Relying Party sono descritti nella tabella seguente.

.. list-table::
  :class: longtable
  :widths: 25 50
  :header-rows: 1

  * - **Nome**
    - **Descrizione**
  * - **client_id**
    - OBBLIGATORIO. Identificatore univoco della Relying Party. Il valore DEVE utilizzare uno dei seguenti prefissi di identificatore del Client (come definito in OpenID4VP_, Sezione 5.9): ``openid_federation`` (identificatore dell’entità della Relying Party in una catena di fiducia) oppure ``x509_hash`` (hash SHA-256 codificato in base64url del certificato X.509 della Relying Party).
  * - **request**
    - CONDIZIONALE. OBBLIGATORIO a meno che ``request_uri`` non sia presente. Contiene il Request Object firmato e codificato in base64url. Per il contenuto dell'oggetto Request, vedere la Sezione :ref:`remote-flow:Request Object`.
  * - **request_uri**
    - CONDIZIONALE. OBBLIGATORIO a meno che ``request`` non sia presente. L'URL HTTP dove la Relying Party fornisce il Request Object firmato all'Istanza del Wallet.
  * - **request_uri_method**
    - OPZIONALE solo se ``request_uri`` è presente. Il metodo HTTP DEVE essere impostato con ``get`` o ``post``. L'Istanza del Wallet dovrebbe utilizzare questo metodo per ottenere il Request Object firmato all'indirizzo fornito dal ``request_uri``. Se non fornito o uguale a ``get``, l'Istanza del Wallet DEVE utilizzare il metodo HTTP ``get``. Altrimenti, l'Istanza del Wallet DOVREBBE fornire i suoi metadata all'interno del body della richiesta HTTP POST codificati in ``application/x-www-form-urlencoded``.

.. note::
  Le specifiche IT Wallet raccomandano l'uso di ``request_uri``, ovvero Request Object by reference.

.. warning::
  Per motivi di sicurezza e per prevenire attacchi di tipo endpoint mix-up, il valore contenuto nel parametro ``request_uri`` DEVE essere uno di quelli attestati da una terza parte fidata, come quelli forniti nei metadata ``openid_credential_verifier`` all'interno del parametro ``request_uris``, ottenuti dalla Trust Chain relativa alla Relying Party (:ref:`WP_081 <wallet-credential-presentation-testcases>` and :ref:`RPR-99 <test-plans-remote-presentation:Matrice di Test per il Verificatore di Credenziali in Remoto>`).

Il valore corrispondente all'endpoint ``request_uri`` DOVREBBE essere casuale, secondo quanto prescritto da `RFC 9101, The OAuth 2.0 Authorization Framework: JWT-Secured Authorization Request (JAR) <https://www.rfc-editor.org/rfc/rfc9101.html#section-5.2.1>`_ Sezione 5.2.1.


Richiesta all'Endpoint URI Request
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

La Relying Party DOVREBBE abilitare il metodo POST nel suo Endpoint ``request_uri`` consentendo all'Istanza del Wallet di informare la Relying Party sulle sue capacità tecniche.

Questa funzionalità può essere utile quando, ad esempio, l'Istanza del Wallet supporta un insieme ristretto di funzionalità, algoritmi o un URL specifico per il suo ``authorization_endpoint``, e qualsiasi altra informazione che ritiene necessario fornire alla Relying Party per l'interoperabilità.

.. warning::
  L'Istanza del Wallet, quando fornisce le sue capacità tecniche alla Relying Party, NON DEVE includere alcuna informazione dell'Utente o altre informazioni esplicite riguardanti l'hardware utilizzato o le preferenze di utilizzo del suo Utente.

Se sia la Relying Party che l'Istanza del Wallet supportano il ``request_uri_method`` con HTTP POST, le capacità (metadata) dell'Istanza del Wallet DEVONO essere fornite utilizzando una richiesta HTTP all'endpoint ``request_uri`` della Relying Party, con il metodo POST e il tipo di contenuto impostato su `application/x-www-form-urlencoded` (:ref:`RPR-101 <test-plans-remote-presentation:Matrice di Test per il Verificatore di Credenziali in Remoto>` and :ref:`WP_083 <wallet-credential-presentation-testcases>`).
La richiesta e i suoi parametri sono definiti nella Sezione 5 (Authorization Request) di `OpenID4VP`_. Di seguito sono riportati i dettagli normativi e i riferimenti sui parametri da utilizzare dall'Istanza del Wallet nella Richiesta URI Request (:ref:`WP_083a–083c <wallet-credential-presentation-testcases>`).

.. list-table:: Parametri dell'Endpoint URI Request
   :class: longtable
   :widths: 20 80
   :header-rows: 1

   * - Parametro
     - Descrizione
   * - `wallet_metadata`
     - OPZIONALE. JSON Object con parametri di metadata. Vedi `OpenID4VP`_, Sezione 10.1 e la tabella seguente, "Parametri dei metadata del Wallet".
   * - `wallet_nonce`
     - RACCOMANDATO. Stringa utilizzata dall'Istanza del Wallet per prevenire il replay delle risposte della Relying Party. 


.. _table_wallet_metadata_parameters:
.. list-table:: Parametri dei metadata del Wallet
   :class: longtable
   :widths: 20 80
   :header-rows: 1

   * - Parametro
     - Descrizione
   * - `vp_formats_supported`
     - OBBLIGATORIO. Oggetto con identificatori di formato degli Attestati Elettronici. Vedi `OpenID4VP`_ Appendice B.
   * - `alg_values_supported`
     - OPZIONALE. Array di suite crittografiche supportate. Vedi `OpenID4VP`_ Appendice B.
   * - `client_id_prefixes_supported`
     - RACCOMANDATO. Un array non vuoto dei prefissi dell’identificatore del Client supportati dall’Istanza del Wallet. I valori validi includono ``openid_federation`` e ``x509_hash``; se omesso, il valore predefinito è pre-registrato.
   * - `authorization_endpoint`
     - URL dell'endpoint del server di autorizzazione, vedi `OAUTH2`_. L'utilizzo di un link universale è preferibile per una sicurezza migliorata e supporto di fallback, *URL schems* personalizzati possono anche essere utilizzati se necessario.
   * - `response_types_supported`
     - OPZIONALE. Array JSON di valori "response_type" di OAuth 2.0. Se presente DEVE essere impostato su `vp_token`. Il valore predefinito è `vp_token`.
   * - `response_modes_supported`
     - OPZIONALE. Array JSON di valori "response_mode" di OAuth 2.0 come specificato in `OAUTH-MULT-RESP-TYPE`_. Il valore supportato DEVE essere *query*.
   * - `request_object_signing_alg_values_supported`
     - OPZIONALE. Vedi OpenID Connect Discovery.

.. note::
   Nell’IT Wallet, le Relying Party legacy che utilizzano un URI ``https`` come ``client_id`` seguono implicitamente il prefisso dell’identificatore del client previsto da OpenID Federation (``openid_federation``).  La loro fiducia è stabilita e validata tramite la risoluzione della catena di fiducia, che è considerata equivalente a quella dei client fidati staticamente (``pre-registered``), come definito in [:rfc:`6749`], per garantire la compatibilità con le versioni precedenti.

.. note::
   Anche se il campo ``response_modes_supported`` fa riferimento a `JARM`_ per garantire l’interoperabilità a livello JARM della Authorization Response, mantenendo un formato basato su JWT per i reindirizzamenti front-channel come ``form_post.jwt`` nel Flusso Same Device, la Relying Party adotta invece ``direct_post.jwt`` nel Flusso Cross Device, che si basa su una consegna back-channel tramite una richiesta HTTP POST alla Relying Party. L’effettivo utilizzo di ``direct_post.jwt`` è descritto di seguito in :ref:`request-uri-response`, dove la Relying Party imposta il ``response_mode`` per la transazione.

.. note::
  Il parametro ``wallet_nonce`` è RACCOMANDATO per le Istanze del Wallet che vogliono prevenire il *replay* delle loro richieste HTTP alle Relying Party da parte di avversari. Quando presente, la Relying Party DEVE Controllarlo.

.. note::
  Per l'``authorization_endpoint`` l'uso di *univarsal link* è preferito rispetto a *URL scheme* personalizzati perché, quando configurati correttamente utilizzando Assetlinks JSON per Android e Apple App Site Association per iOS, forniscono una sicurezza migliorata riducendo il rischio di dirottamento degli URL.
  Inoltre, gli *univarsal link* offrono meccanismi di fallback, consentendo al flusso di continuare senza problemi in un browser anche se l'Istanza del Wallet non è installata, garantendo un'esperienza Utente più fluida. Per garantire l'interoperabilità, il supporto degli *URL scheme* personalizzati è anche RACCOMANDATO secondo il profilo di interoperabilità OpenID4VC High Assurance Interoperability Profile (HAIP) `OPENID4VC-HAIP`_, e in particolare utilizzando l'url personalizzato ``haip://``.

.. _request-uri-response:

Risposta dell'Endpoint URI Request
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

La Relying Party emette il Request Object firmato utilizzando il tipo di contenuto impostato su ``application/oauth-authz-req+jwt``. Per il contenuto dell'oggetto Request, vedere la Sezione :ref:`remote-flow:Request Object`.

Errori dell'Endpoint URI Request
--------------------------------

Quando la Relying Party incontra errori durante l'emissione del Request Object dall'endpoint ``request_uri``, DEVE restituire una *Error Response* con ``application/json`` come tipo di contenuto e DEVE includere i seguenti parametri:

* ``error``: Il codice di errore.
* ``error_description``: Testo in forma leggibile che fornisce ulteriori dettagli per chiarire la natura dell'errore incontrato.

La seguente tabella elenca gli *HTTP Status Code* e i relativi *Error codes* che DEVONO essere supportati per la *Error Response*:

.. list-table::
    :class: longtable
    :widths: 20 20 60
    :header-rows: 1

    * - **Codice di Stato**
      - **Codice di Errore**
      - **Descrizione**
    * - ``400 Bad Request``  
      - ``invalid_request``  
      - L'Oggetto di Richiesta non può essere recuperato a causa di una richiesta non valida o malformata all’endpoint ``request_uri``. (:rfc:`6749#section-4.1.2.1`)
    * - ``500 Internal Server Error``
      - ``server_error``
      - La richiesta non può essere soddisfatta perché l'Endpoint URI Request ha incontrato un problema interno. (:rfc:`6749#section-4.1.2.1`).
    * - ``503 Service Unavailable``
      - ``temporarily_unavailable``
      - La richiesta non può essere soddisfatta perché l'Endpoint URI Request è temporaneamente non disponibile (ad esempio, a causa di manutenzione o sovraccarico). (:rfc:`6749#section-4.1.2.1`).


Di seguito è riportato un esempio di *Error Response* dall'endpoint ``request_uri``:

.. code-block:: http

  HTTP/1.1 500 Internal Server Error
  Content-Type: application/json

  {
    "error": "server_error",
    "error_description": "The Request Object cannot be retrieved due to an internal server error."
  }

Dopo aver ricevuto una *Error Response*, l'Istanza del Wallet DOVREBBE informare l'Utente della condizione di errore in modo appropriato (:ref:`WP_089 <wallet-credential-presentation-testcases>`). L'Istanza del Wallet DOVREBBE registrare l'errore e PUÒ tentare di recuperare da determinati errori se fattibile (:ref:`WP_089a <wallet-credential-presentation-testcases>`). Ad esempio, se l'errore è ``server_error``, l'Istanza del Wallet DOVREBBE chiedere all'Utente di reinserire o scansionare un nuovo codice QR, se possibile (:ref:`WP_089b <wallet-credential-presentation-testcases>`).

Request Object
^^^^^^^^^^^^^^

I parametri dell'header JWT sono descritti di seguito:

.. list-table::
  :class: longtable
  :widths: 25 50
  :header-rows: 1

  * - **Nome**
    - **Descrizione**
  * - **alg**
    - OBBLIGATORIO. Algoritmo utilizzato per firmare il JWT, secondo [:rfc:`7516#section-4.1.1`]. DEVE essere uno degli algoritmi supportati nella Sezione :ref:`algorithms:Algoritmi Crittografici` e NON DEVE essere impostato su ``none`` o su un identificatore di algoritmo simmetrico (MAC) (:ref:`RPR-104 <test-plans-remote-presentation:Matrice di Test per il Verificatore di Credenziali in Remoto>`).
  * - **typ**
    - OBBLIGATORIO. Media Type del JWT, come definito in [:rfc:`7519`] e [:rfc:`9101`]. DOVREBBE essere impostato sul valore ``oauth-authz-req+jwt`` (:ref:`RPR-105 <test-plans-remote-presentation:Matrice di Test per il Verificatore di Credenziali in Remoto>`).
  * - **kid**
    - OBBLIGATORIO. ID della chiave della chiave pubblica necessaria per verificare la firma JWT, come definito in [:rfc:`7517`].
  * - **trust_chain**
    - OPZIONALE. È una sequenza di Entity Statement che compongono la Trust Chain relativa alla Relying Party, come definito in `OID-FED`_ Sezione 4.3 *Trust Chain Header Parameter*.
  * - **x5c**
    - OBBLIGATORIO. Contiene il certificato X.509 foglia della Relying Party (e opzionalmente i certificati intermedi), utilizzato per verificare la firma JWT con la chiave pubblica nel certificato della Relying Party come definito in :rfc:`7515`. Il certificato della Relying Party in ``x5c`` DEVE attestare informazioni di identità della Relying Party sufficienti per vincolare gli endpoint di rete referenziati dal flusso di presentazione. In particolare, gli endpoint utilizzati nella Authorization Request e Authorization Response (ad esempio, ``response_uri``, ``redirect_uri``) DEVONO corrispondere alle informazioni di identità contenute nel certificato della Relying Party (ad esempio, un SAN di tipo URI per il matching completo dell'URI o un DNS Name SAN per il matching del nome host).

.. note::
   L'intestazione ``x5c`` NON DEVE includere il certificato radice, come richiesto da `OPENID4VC-HAIP`_. La catena di certificati ``x5c`` DEVE validare a un certificato radice preconfigurato; vedere la Sezione :ref:`trust-infrastructure:X.509 PKI` per informazioni di base sulla validazione della catena di certificati X.509.


I parametri del payload JWT sono descritti qui:

.. list-table::
  :class: longtable
  :widths: 25 50
  :header-rows: 1

  * - **Nome**
    - **Descrizione**
  * - **client_id**
    - OBBLIGATORIO. Identificatore univoco della Relying Party.
  * - **client_metadata**
    - OPZIONALE. Un oggetto JSON contenente i valori dei metadata della Relying Party, che DOVREBBE includere i seguenti parametri:
        - **vp_formats_supported**. Utilizzato dall'Istanza del Wallet per determinare i formati di Verifiable Presentation supportati.
        - **encrypted_response_enc_values_supported**. Array JSON che elenca gli algoritmi JWE ``enc`` supportati per le Authorization Response cifrate in ``direct_post.jwt``.
        - **jwks**. JSON Web Key Set utilizzato dall'Istanza del Wallet per cifrare la Authorization Response o per l'accordo delle chiavi. Le chiavi contenute in questo set sono specifiche della richiesta e identificate dal loro valore ``kid``.
        - **client_name** e **logo_uri**. OPZIONALE. Utilizzati per la visualizzazione del consenso dell'utente e per mostrare l'identità della Relying Party nell'interfaccia dell'Istanza del Wallet.
  * - **response_mode**
    - OBBLIGATORIO. DEVE essere impostato su ``direct_post.jwt`` (:ref:`RPR-106 <test-plans-remote-presentation:Matrice di Test per il Verificatore di Credenziali in Remoto>`).
  * - **dcql_query**
    - OBBLIGATORIO. Oggetto che rappresenta una richiesta di presentazione di Credenziali, secondo il linguaggio di query DCQL definito nella Sezione 6 di `OpenID4VP`_.
  * - **transaction_data**  
    - OPZIONALE. Un array non vuoto di oggetti JSON, ognuno dei quali descrive una transazione che la Relying Party richiede all’Utente di autorizzare.  Ogni oggetto di transazione include:  
        - **type**. Stringa che identifica il tipo di dati della transazione.
        - **credential_ids**. Array che fa riferimento a una o più Credenziali provenienti dalla ``dcql_query`` che possono autorizzare la transazione.
  * - **transaction_data_hashes_alg**  
    - OPZIONALE. Un array di stringhe, ciascuna delle quali rappresenta un identificatore di algoritmo di hash, corrispondente a un nome di algoritmo di hash elencato nel registro `IANA <https://www.iana.org/assignments/named-information/named-information.xhtml#hash-alg>`_. Uno di questi algoritmi DEVE essere utilizzato per calcolare gli hash nel parametro di risposta ``transaction_data_hashes``. Se omesso, l’algoritmo di hash predefinito è sha-256.
  * - **response_type**
    - OBBLIGATORIO. DEVE essere impostato su ``vp_token`` (:ref:`RPR-107 <test-plans-remote-presentation:Matrice di Test per il Verificatore di Credenziali in Remoto>`).
  * - **wallet_nonce**
    - OBBLIGATORIO se precedentemente fornito dall'Istanza del Wallet (:ref:`RPR-94 <test-plans-remote-presentation:Matrice di Test per il Verificatore di Credenziali in Remoto>`). Valore stringa utilizzato per mitigare gli attacchi di replay della Request URI Response, come definito nella Sezione 5.10 (Request URI Method) di `OpenID4VP`_.
  * - **response_uri**
    - OBBLIGATORIO. L'URI di Risposta a cui l'Istanza del Wallet DEVE inviare la Authorization Response utilizzando una HTTP Request con il metodo POST (:ref:`RPR-112 <test-plans-remote-presentation:Matrice di Test per il Verificatore di Credenziali in Remoto>`).
  * - **nonce**
    - OBBLIGATORIO. Numero unico e casuale con sufficiente entropia, la cui lunghezza DEVE essere di almeno 32 cifre (:ref:`RPR-110 <test-plans-remote-presentation:Matrice di Test per il Verificatore di Credenziali in Remoto>`)..
  * - **state**
    - RACCOMANDATO. Identificatore univoco della Authorization Request, il suo valore DOVREBBE essere opaco per l’Istanza del Wallet.
  * - **iss**
    - OBBLIGATORIO. L'entità che ha emesso il JWT. Sarà popolato con il ``client_id`` della Relying Party.
  * - **iat**
    - OBBLIGATORIO. Timestamp Unix, che rappresenta l'ora in cui il JWT è stato emesso.
  * - **exp**
    - OBBLIGATORIO. Timestamp Unix, che rappresenta l'ora di scadenza in cui o dopo la quale il JWT NON DEVE più essere valido (:ref:`RPR-111 <test-plans-remote-presentation:Matrice di Test per il Verificatore di Credenziali in Remoto>`).

.. warning::
  Per motivi di sicurezza e per prevenire attacchi di tipo endpoint mix-up, il valore contenuto nel parametro ``response_uri`` DEVE essere uno di quelli attestati da una terza parte fidata, come quelli forniti nei metadata ``openid_credential_verifier`` all'interno del parametro ``response_uris``, ottenuti dalla Trust Chain relativa alla Relying Party (:ref:`WP_091a <wallet-credential-presentation-testcases>` and :ref:`RPR-112 <test-plans-remote-presentation:Matrice di Test per il Verificatore di Credenziali in Remoto>`).

.. note::
   Il parametro ``transaction_data`` è destinato ai casi d’uso in cui l’Istanza del Wallet DEVE autorizzare una transazione specifica, come l’inizio di un pagamento o la firma digitale.  In questi scenari ad alta sensibilità, i dati della transazione possono essere collegati crittograficamente alla Risposta di Autorizzazione tramite ``transaction_data_hashes`` all’interno del Key Binding JWT, garantendo integrità e non ripudio.  Per ulteriori dettagli, consultare `OpenID4VP`_, Sezione 8.4.

.. note::
  Il parametro ``state`` in una richiesta OAuth è opzionale, ma è altamente RACCOMANDATO. Viene utilizzato principalmente per prevenire attacchi Cross-Site Request Forgery (CSRF) includendo un valore unico e imprevedibile che la Relying Party può verificare al momento della ricezione della risposta. Inoltre, aiuta a mantenere lo stato tra Request e Response, come le informazioni di sessione o altri dati di cui la Relying Party ha bisogno dopo il processo di autorizzazione.

.. note::
  L'utilizzo del parametro ``client_metadata`` è condizionale. Se ``client_id`` utilizza il prefisso ``x509_hash``, tutti i metadata della Relying Party, oltre alla sua chiave pubblica utilizzata per firmare il Request Object, DEVONO essere forniti in ``client_metadata``. Tuttavia, se è presente e ``client_id`` utilizza il prefisso ``openid_federation``, l'Istanza del Wallet DEVE ignorarlo e ottenere i metadata attraverso la Trust Chain OpenID Federation (:ref:`RPR-113 <test-plans-remote-presentation:Matrice di Test per il Verificatore di Credenziali in Remoto>`).


Authorization Response
^^^^^^^^^^^^^^^^^^^^^^^^

Dopo aver ottenuto l'autorizzazione e il consenso dell'Utente per la presentazione degli Attestati Elettronici, l'Istanza del Wallet invia la Authorization Response all'endpoint ``response_uri`` della Relying Party utilizzando una richiesta HTTP con il metodo POST (:ref:`WP_091 <wallet-credential-presentation-testcases>`), il contenuto DOVREBBE essere cifrato secondo `OpenID4VP`_ Sezione 8.3, utilizzando la chiave pubblica della Relying Party (:ref:`WP_092 <wallet-credential-presentation-testcases>`).

.. note::
    **Perché la risposta è cifrata?**

    La risposta inviata dall'Istanza del Wallet alla Relying Party è cifrata per impedire a un avversario di sfruttare possibili vulnerabilità per accedere alle informazioni trasmesse in chiaro all'interno della rete della Relying Party. Per esempio, ciò è possibile se l'ambiente di rete della Relying Party impiega un proxy per le operazioni di `TLS Termination <https://www.f5.com/glossary/ssl-termination>`_, il quale agisce come intermediario tra il client e il backend web server della Relying Party e gestisce tutte le operazioni relative a TLS. In questo caso specifico, il proxy decifra il contenuto della trasmissione, in seguito lo inoltra al backend web server della Relying Party. Questa operazione può avvenire in chiaro oppure negoziando una ulteriore sessione TLS con il web server della Relying Party (sempre raccomandato). Nel primo caso, trasmissione dei dati TLS in chiaro, qualsiasi avversario all'interno del segmento di rete fra proxy e web server backend che intercettasse i dati trasmessi, potrebbe ottenere informazioni sensibili; se però la risposta è cifrata, la fattispece descritta viene mitigata anche mandando i dati in chiaro.

Nella Authorization Response vengono utilizzati i seguenti parametri (:ref:`WP_093 <wallet-credential-presentation-testcases>`):

.. list-table::
  :class: longtable
  :widths: 25 50
  :header-rows: 1

  * - **Nome**
    - **Descrizione**
  * - **vp_token**
    - Questo array DEVE contenere gli Attestati Elettronici richiesti nel formato SD-JWT VC (:ref:`WP_093a <wallet-credential-presentation-testcases>`).

      Il formato ``vp_token`` è un JSON Object le cui chiavi corrispondono agli id degli Attestati Elettronici richieste nel ``dcql_query`` utilizzato nella richiesta, e i valori sono degli array contenenti il(gli) Attestato(i) Elettronico(i) presentato(i).

  * - **state**
    - Identificatore univoco fornito dalla Relying Party all'interno della Authorization Request.

.. note:: 
    Sebbene `OpenID4VP`_ prenda in considerazione la bozza -10 della specifica SD-JWT VC, la specifica IT Wallet considera la bozza -11 (`SD-JWT-VC`_) in linea con la versione identificata in `OpenID4VCI`_.

SD-JWT definisce come un *Holder* può presentare una Attestato Elettronico a una Relying Party, dimostrando il legittimo possesso dell'Attestato Elettronico. Per fare ciò, l'*Holder* DEVE includere il ``KB-JWT`` nell'SD-JWT aggiungendo il ``KB-JWT`` alla termine della stringa contenente l'SD-JWT (:ref:`WP_093b <wallet-credential-presentation-testcases>`), come rappresentato nell'esempio seguente

.. code-block:: text

  <Issuer-Signed-JWT>~<Disclosure 1>~<Disclosure 2>~...~<Disclosure N>~<KB-JWT>

Per convalidare la firma sul Key Binding JWT, la Relying Party DEVE utilizzare il materiale crittografico incluso nell'*Issuer-Signed-JWT*. La convalida della firma del Key Binding JWT (KB-JWT) DEVE utilizzare la chiave pubblica inclusa nell'SD-JWT contenuta nel parametro ``cnf`` contenuto nell'*Issuer-Signed-JWT*.

Quando viene presentato un SD-JWT, il suo KB-JWT DEVE contenere i seguenti parametri nell'intestazione JWT (:ref:`WP_093c <wallet-credential-presentation-testcases>`):

.. list-table::
  :class: longtable
  :widths: 25 50
  :header-rows: 1

  * - **Claim**
    - **Descrizione**
  * - **typ**
    - OBBLIGATORIO. DEVE essere ``kb+jwt``, che caratterizza esplicitamente il Key Binding JWT come raccomandato nella Sezione 3.11 di :rfc:`8725`.
  * - **alg**
    - OBBLIGATORIO. Algoritmo di Firma utilizzando uno di quelli specificati nella Sezione :ref:`algorithms:Algoritmi Crittografici`.

Quando viene presentato un SD-JWT, la firma KB-JWT DEVE essere verificata dalla stessa chiave pubblica inclusa nell'SD-JWT all'interno del parametro ``cnf``. Il KB-JWT DEVE contenere i seguenti parametri nel payload JWT:

.. list-table::
  :class: longtable
  :widths: 25 50
  :header-rows: 1

  * - **Claim**
    - **Descrizione**
  * - **iat**
    - OBBLIGATORIO. Il valore di questa *claim* DEVE essere l'ora in cui è stato emesso il Key Binding JWT, utilizzando la sintassi definita in :rfc:`7519`.
  * - **aud**
    - OBBLIGATORIO. Il ricevitore previsto del Key Binding JWT. Il valore di questo parametro DEVE corrispondere all'identificatore di entità (``client_id``) univoco della Relying Party.
  * - **nonce**
    - OBBLIGATORIO. Garantisce l'unicità della firma. Il valore di questa *claim* DEVE essere una stringa e deve corrispondere a quello fornito nel Request Object.
  * - **sd_hash**
    - OBBLIGATORIO. Il digest codificato in base64url del JWT firmato dal Fornitore di Attestati Elettronici (SD-JWT) e le *selective disclosures* selezionate dall'Utente.
  * - **transaction_data_hashes**  
    - CONDIZIONALE. OBBLIGATORIO quando la richiesta include ``transaction_data``. Array non vuoto di hash codificati in base64url. Ogni hash è calcolato sul valore esatto della stringa corrispondente all’elemento ``transaction_data``.
  * - **transaction_data_hashes_alg**  
    - CONDIZIONALE. OBBLIGATORIO solo se la richiesta includeva ``transaction_data_hashes_alg``. Stringa che indica l’algoritmo di hash effettivamente utilizzato per calcolare ``transaction_data_hashes``; se tale parametro non è stato fornito, la funzione di hash DEVE essere ``sha-256``.  


Errori della Authorization Response
---------------------------------------

Ci sono casi in cui l'Istanza del Wallet non può convalidare il Request Object o il Request Object risulta non valido. Questo errore si verifica se il Request Object viene recuperato con successo dall'url fornito nel parametro ``request_uri`` ma non supera i controlli di convalida. Ciò potrebbe essere dovuto a firme errate, claim non conformim o altri errori di convalida, come la revoca della trust per la specifica Relying Party che lo ha emesso.

Se l'Istanza del Wallet incontra tali errori durante la valutazione della Authorization Request, DEVE notificare alla Relying Party inviando una *Error Response* nella *Autorization Response* (:ref:`WP_090 <wallet-credential-presentation-testcases>`). 
L'Istanza del Wallet invia la *Error Response* nella *Autorization Response* all'endpoint ``response_uri`` della Relying Party utilizzando una richiesta HTTP POST (:ref:`WP_090 <wallet-credential-presentation-testcases>`). Questa *Error Response* DEVE essere codificata nel corpo della richiesta utilizzando il formato definito dal tipo di contenuto ``application/x-www-form-urlencoded``.

Di seguito è riportato un esempio non normativo di una *Error Response* nella *Autorization Response*.

.. code-block:: http

  POST /response_uri HTTP/1.1
  HOST: relying-party.example.org
  Content-Type: application/x-www-form-urlencoded

  state=3be39b69-6ac1-41aa-921b-3e6c07ddcb03&
  error=invalid_request&
  error_description=...

.. warning::
  L'attuale specifica OpenID4VP delinea varie risposte di errore che un'Istanza del Wallet può restituire alla Relying Party in caso di *Authorization Request* errata. Per migliorare la privacy, le Istanze del Wallet NON DOVREBBERO notificare alla Relying Party le richieste errate qualora un uso improprio delle risposte di errore potrebbe portare a raccogliere informazioni lesive della privacy dell'Utente (ad esempio, se l'Utente decide di non voler presentare l'Attestato Elettronico richiesto).

Nella seguente tabella sono elencati gli *Error codes* e le descrizioni che sono supportati per la *Error Response* nella *Autorization Response*:

.. list-table::
   :class: longtable
   :widths: 20 60
   :header-rows: 1

   * - **Codice di Errore**
     - **Descrizione**
   * - ``invalid_request_uri``
     - Il `request_uri` nella Authorization Request restituisce un errore, contiene dati non validi o è altrimenti malformato. :rfc:`9101`
   * - ``vp_formats_not_supported``
     - L'Istanza del Wallet non supporta nessuno dei formati vp richiesti dalla Relying Party. `OpenID4VP`_
   * - ``invalid_request_uri_method``  
     - Il valore del parametro ``request_uri_method`` non è né ``get`` né ``post``.  `OpenID4VP`_
   * - ``invalid_request``
     - La richiesta è malformata o incoerente (ad esempio utilizza il Response Type ``vp_token`` ma non include il parametro ``dcql_query``), il prefisso dell'identificatore del Client non è supportato oppure i requisiti del prefisso non sono rispettati (ad esempio, ``client_id`` con il prefisso ``x509_hash`` senza il ``client_metadata`` richiesto). `OpenID4VP`_
   * - ``access_denied``
     - Il Wallet non aveva l'Attestato Elettronico richiesto, l'Utente non ha dato il consenso o il Wallet non è riuscito ad autenticare l'Utente. `OpenID4VP`_
   * - ``invalid_client``
     - - I metadata della Relying Party sono stati risolti basandosi sull'Identificatore del Client (utilizzando il prefisso ``openid_federation`` o ``x509_hash``), ma la Relying Party non può essere autorizzata a causa di errori nella verifica della trust oppure dal fatto che non è stata riconosciuta come entità valida della federazione. `OID-FED`_ e `OpenID4VP`_
       - Il parametro ``client_metadata`` è presente, ma il Wallet riconosce l'identificativo del client e conosce i metadati ad esso associati. `OpenID4VP`_
       - I metadati pre-registrati del Relying Party sono stati trovati in base all'identificativo del client, ma è presente anche il parametro ``client_metadata``. `OpenID4VP`_
   * - ``invalid_transaction_data``  
     - Uno o più oggetti nella struttura ``transaction_data`` non sono validi. Ad esempio, tali oggetti contengono tipi sconosciuti o non supportati, campi malformati (ad esempio è un oggetto di tipo noto ma contiene campi sconosciuti o campi di tipo errato per il tipo di transaction data) o mancanti, valori non validi (ad esempio il campo ``credential_ids`` non corrisponde) oppure riferimenti a Credenziali non disponibili. `OpenID4VP`_

Risposta della Relying Party
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Come definito nella Sezione 8.2. (*Response mode* "direct_post") della specifica `OpenID4VP`_, se l'Endpoint di Risposta della Relaying Party ha elaborato con successo la *Authorization Response* o la *Error Response* fornita dall'Istanza del Wallet, DEVE rispondere con un codice di stato HTTP 200 con ``Content-Type`` di ``application/json`` e un JSON Object nel corpo della risposta.

Nel **Flusso Same Device**, la Relying Party DOVREBBE aggiungere il parametro ``redirect_uri`` all'JSON Object nel corpo della risposta. Dopo aver ricevuto il ``redirect_uri``, l'Istanza del Wallet DEVE eseguire un reindirizzamento all'URL specificato dal ``redirect_uri``.
Questo reindirizzamento consente alla Relying Party di riprendere senza problemi l'interazione con l'Utente sul dispositivo che ha avviato il flusso, dopo che l'Istanza del Wallet ha trasmesso la Authorization Response al ``response_uri`` designato.

La Relying Party DEVE includere un codice di risposta all'interno del ``redirect_uri``. Il codice di risposta è un numero fresco, crittograficamente casuale utilizzato per garantire che solo il ricevitore del reindirizzamento possa recuperare ed elaborare la Authorization Response. Il numero potrebbe essere aggiunto come componente del path, come parametro o come frammento all'URL. È RACCOMANDATO utilizzare un valore casuale crittografico di 128 bit o più al momento della scrittura di questa specifica.
Anche se un avversario riesce a rubare il valore casuale utilizzato nella richiesta allo Status Endpoint, il suo user-agent verrebbe rifiutato a causa del cookie mancante nella richiesta.

.. warning::
  Per motivi di sicurezza e per prevenire attacchi di tipo endpoint mix-up, il valore contenuto nel parametro ``redirect_uri`` DEVE essere uno di quelli attestati da una terza parte fidata, come quelli forniti nei metadata ``openid_credential_verifier`` all'interno del parametro ``redirect_uris``, ottenuti dalla Trust Chain relativa alla Relying Party (:ref:`WP_094a <wallet-credential-presentation-testcases>`).

Errori della Risposta della Relying Party
-----------------------------------------

Se qualsiasi controllo di convalida, eseguito dalla Relying Party sulla Authorization Response dall'Istanza del Wallet, fallisce; l'endpoint URI di Risposta DEVE restituire una *Error Response*. La struttura di questa *Error Response* dovrebbe essere determinata dalla natura specifica dell'errore incontrato. La risposta DEVE utilizzare ``application/json`` come tipo di contenuto e DEVE includere i seguenti parametri:

* ``error``: Il codice di errore.
* ``error_description``: Testo in forma leggibile che fornisce ulteriori dettagli per chiarire la natura dell'errore incontrato.

La seguente tabella elenca gli Status Code HTTP e i relativi *Error codes* che DEVONO essere supportati per la *Error Response*:

.. list-table::
    :class: longtable
    :widths: 20 20 60
    :header-rows: 1

    * - **Codice di Stato**
      - **Codice di Errore**
      - **Descrizione**
    * - ``400 Bad Request``
      - ``invalid_request``
      - La risposta non può essere elaborata perché mancano parametri obbligatori, contiene parametri non validi o è non conforme agli standard.
    * - ``400 Bad Request``
      - ``invalid_request``
      - Gli Attestati Elettronici presentati sono non conformi agli standard, non valide o revocate.
    * - ``400 Bad Request``
      - ``invalid_request``
      - La presentazione degli Attestati Elettronici, contenuta nell'oggetto ``vp_token``, non è conforme agli standard, non ha i parametri richiesti o è formattata in modo errato.
    * - ``400 Bad Request``
      - ``invalid_request``
      - L'"sd-jwt" restituito non è conforme agli standard, mancano parametri obbligatori o è formattato in modo errato.
    * - ``403 Forbidden``
      - ``invalid_request``
      - La firma del KB-JWT non è valida o non corrisponde alla chiave pubblica associata (JWK) referenziata nell'SD-JWT firmato dall'Emittente.
    * - ``403 Forbidden``
      - ``invalid_request``
      - Il valore del nonce fornito è errato o altrimenti non conforme agli standard.
    * - ``403 Forbidden``
      - ``invalid_request``
      - La trust non può essere stabilita con il Fornitore di Attestati Elettronici.
    * - ``500 Internal Server Error``
      - ``server_error``
      - La richiesta non può essere soddisfatta perché il Response Endpoint ha incontrato un problema interno.
    * - ``503 Service Unavailable``
      - ``temporarily_unavailable``
      - La richiesta non può essere soddisfatta perché il Response Endpoint è temporaneamente non disponibile (ad esempio, a causa di manutenzione o sovraccarico).

Di seguito ci sono due esempi di risposte HTTP che utilizzano ``application/json`` che includono sia i membri ``error`` che ``error_description``:

.. code-block:: http

  HTTP/1.1 403 Forbidden
  Content-Type: application/json

  {
    "error": "invalid_request",
    "error_description": "Trust cannot be established with the issuer: https://issuer.example.com"
  }


.. code-block:: http

  HTTP/1.1 400 Bad Request
  Content-Type: application/json

  {
    "error": "invalid_request",
    "error_description": "The vp_token is malformed, missing required parameters or incorrectly formatted"
  }


Status Endpoint
^^^^^^^^^^^^^^^^^^

Questa specifica introduce lo Status Endpoint della Relying Party per le implementazioni che scelgono di utilizzarlo. Questo Endpoint è una funzionalità di sicurezza interna dell'implementazione e non è richiesto per l'interoperabilità.

Sia he il flusso sia Same Device o Cross Device, l'user-agent deve controllare lo stato della sessione all'endpoint reso disponibile dalla Relying Party (endpoint di stato). Questo controllo PUÒ essere implementato sotto forma di codice JavaScript, all'interno della pagina che mostra il Codice QR o il tramite pulsante href che punta all'URL di richiesta. Il codice JavaScript fa sì che l'user-agent controlli lo Status Endpoint utilizzando una strategia di polling (in secondi) o una strategia push (ad esempio, WebSocket).

Poiché la pagina HTML e lo Status Endpoint sono implementati dalla Relying Party, i dettagli di implementazione di questa soluzione sono responsabilità della Relying Party, in quanto sono relativi alle API interne della Relying Party. Tuttavia, il testo seguente descrive un'implementazione di esempio.

La Relying Party lega la richiesta dello user-agent, con un cookie di sessione contrassegnato come ``Secure`` e ``HttpOnly``, con la richiesta emessa. L'URL della richiesta DOVREBBE includere un parametro con un valore casuale. La risposta HTTP restituita da questo endpoint di stato PUÒ contenere gli Status Code HTTP elencati di seguito:

* **201 Created**; quando il Request Object firmato è stato emesso dalla Relying Party che attende di essere scaricato dall'Istanza del Wallet all'endpoint ``request_uri``.
* **202 Accepted**; quando il Request Object firmato è stato ottenuto dall'Istanza del Wallet.
* **200 OK**; quando l'Istanza del Wallet ha fornito la presentazione all'endpoint ``response_uri`` della Relying Party e l'autenticazione dell'Utente ha avuto successo. La Relying Party aggiorna il cookie di sessione consentendo allo user-agent di accedere alla risorsa protetta. Viene fornito un ``redirect_uri`` che trasporta lo user-agent alla pagina in cui l'Utente deve navigare.

Errori dello Status Endpoint
-----------------------------

Se invece qualsiasi controllo di convalida eseguito dalla Relying Party fallisce, la pagina del Codice QR DOVREBBE essere aggiornata con un messaggio di errore. Inoltre, lo Status Endpoint DEVE restituire una *Error Response*, la cui struttura dipende dalla natura dell'errore. La risposta DEVE utilizzare ``application/json`` come tipo di contenuto e DEVE includere i seguenti parametri:

* ``error``: Il codice di errore.
* ``error_description``: Testo in forma leggibile che fornisce ulteriori dettagli per chiarire la natura dell'errore incontrato.

La seguente tabella elenca gli Status Code HTTP e i relativi *Error codes* che DEVONO essere supportati per la *Error Response*:

.. list-table::
    :class: longtable
    :widths: 20 20 60
    :header-rows: 1

    * - **Codice di Stato**
      - **Codice di Errore**
      - **Descrizione**
    * - ``401 Unauthorized``
      - ``authentication_failed``
      - L'Istanza del Wallet o il suo Utente hanno rifiutato la richiesta, la richiesta è scaduta o altri errori hanno impedito l'autenticazione.
    * - ``403 Forbidden``
      - ``invalid_session``
      - L'id di sessione fornito nella richiesta non è valido.


URI di Reindirizzamento
^^^^^^^^^^^^^^^^^^^^^^^^
Il valore ``redirect_uri`` DEVE essere utilizzato con un metodo HTTP GET dall'user-agent per reindirizzare l'Utente a un endpoint specifico della Relying Party al fine di completare il processo.


Errori dell'URI di Reindirizzamento
-----------------------------------

Quando l'user-agent viene reindirizzato all'URI di Reindirizzamento fornito dalla Relying Party, possono verificarsi diversi errori che impediscono il completamento con successo del processo. Questi errori sono critici in quanto influenzano direttamente l'esperienza dell'Utente ostacolando il flusso fluido di informazioni tra l'Istanza del Wallet e la Relying Party. La gestione di questi errori richiede una comunicazione chiara all'Utente all'interno della pagina web di navigazione restituita. La Relying Party DEVE implementare i meccanismi di gestione degli errori e di convalida per gli URI di Reindirizzamento definiti in questa specifica. Di seguito sono riportati potenziali errori relativi all'URI di Reindirizzamento, la *Error Response* DEVE utilizzare ``application/json`` come tipo di contenuto e DEVE includere i seguenti parametri:

    - ``error``: Il codice di errore.
    - ``error_description``: Testo in forma leggibile che fornisce ulteriori dettagli per chiarire la natura dell'errore incontrato.

La seguente tabella elenca gli Status Code HTTP e i relativi *Error codes* che DEVONO essere supportati per la *Error Response*:

.. list-table::
    :class: longtable
    :widths: 20 20 60
    :header-rows: 1

    * - **Codice di Stato**
      - **Codice di Errore**
      - **Descrizione**
    * - ``403 Forbidden``
      - ``invalid_request``
      - L'URI di Reindirizzamento fornito dalla Relying Party non corrisponde a nessuno degli URI collegati alla sessione dell'Utente. (:rfc:`6749#section-4.1.2.1`)
    * - ``403 Forbidden``
      - ``invalid_request``
      - La sessione dell'Utente non è valida o è scaduta.
    * - ``500 Internal Server Error``
      - ``server_error``
      - La richiesta non può essere soddisfatta a causa di un errore interno del server. (:rfc:`6749#section-4.1.2.1`).
    * - ``503 Service Unavailable``
      - ``temporarily_unavailable``
      - La richiesta non può essere soddisfatta perché il servizio è temporaneamente non disponibile (ad esempio, a causa di manutenzione o sovraccarico). (:rfc:`6749#section-4.1.2.1`).


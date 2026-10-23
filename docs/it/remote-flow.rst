.. include:: ../common/common_definitions.rst


Flusso Remoto
=============

Questa sezione descrive la presentazione remota di un Attestato Elettronico da un'Istanza del Wallet a un'Istanza di Relying Party web.

La presentazione remota utilizza [`OpenID4VP`_], profilato da [`OPENID4VC-HAIP`_] e [`ETSI TS 119 472-2`_], come richiesto da [`CIR2024/2982`_].
Il Trust Framework è selezionato tramite il prefisso ``client_id``, come specificato in :ref:`trust-evaluation:Selection at Presentation`.
La clausola 6 di [`ETSI TS 119 472-2`_] prevale su [`OPENID4VC-HAIP`_] ove le due fonti differiscono.

Il flusso remoto ha due forme. Nel flusso Same Device lo user-agent e l'Istanza del Wallet sono sullo stesso dispositivo. Nel flusso Cross Device sono su dispositivi diversi. Le regole normative di invocazione sono specificate nei Passaggi 4-7.

.. _fig_High-Level-Flow-Presentation:
.. plantuml:: plantuml/credential-presentation-remote-high-level-flow.puml
    :width: 99%
    :alt: La figura illustra il Flusso Remoto ad Alto Livello.
    :caption: `Flusso di Protocollo Remoto di Alto Livello. <https://www.plantuml.com/plantuml/svg/TP9FJy904CNl-oacN9GcslZVS30OGWmdQeLmCI5BEz2LTNVTtThKJ-yEGcqndffqthptU-qCdUVMb--IcV0KcJ1SUUWjk9JeOQB2M6NO0-wWwafIbBLG6qZ2otedi8OnQ-3i0Qe1N9n353sMlj1MV74lj88KFqfqFeh05rQNcm8ivi9Yva5RU4uXqpc2oxW2huC6NnN4yG_AYOEksLZbHWlbuvWnBZs8zS4VfgitybpLmN-D5aC1nYhYicO0bmHsaCxJIGlhz6ay8vHa-ZBhxna2GPg4zFP6ExifVFNNrncj799nTGJNPmnLlgSAozUql9Z0gC1iwyB6x-Y6HdE75aRafWYqLUUMnWJS_Jv7wPzcwVKMrL6hHlLFBGgus_LAscXDvtkQTGwXawiDeN0fQwYQVxqihUYpOQWVhkuR>`_


.. .. Figure:: ../../images/High-Level-Flow-Presentation.svg
..     :figwidth: 100%
..     :align: center
..     :target: https://www.plantuml.com/plantuml/svg/TL9TJy8m57tlhpZXHLcYYz-61uCXnF34d11UJCZS6bQPRMtlRF3NspB0JUBJidlEFH-v7LhA3DKV5TF-AtAXCqdeBRAgueI9zB3CUG-PXUjIKbvjX5mXySFDbc0qOqRZx05kW8jpHD5ZJQKouZiZeIHI_bbpIr64KmVJ_2nh8_gWqgXwLVfX8GpF2ShWEKMk2WwRPnAlafHdSSHn4-t4eYi-beLMGb8SC-P21gC7k0mXThQOfvDsXAVnBDWaqvTP7mVrDF7AxOssxg7SrR6krKfQtdJR8zEtTr-cpvZRxLs7lSK4evBdQ-l9lz1DWEQM6uo2a2IFjfhS1ZXa_LExQ_obbwJMN1uNQbZ_D0e6TzjAIJlQeUvzm3htxlWg7QBuispWzYTi3ilOaCl2lwuV

..     High Level Remote Protocol Flow


Una descrizione ad alto livello del flusso remoto, dal punto di vista dell'Utente, è fornita di seguito e mostrata in :ref:`fig_High-Level-Flow-Presentation`:

  1. *Authorization Request*: l'Istanza del Wallet ottiene un URL nel flusso Same Device o un Codice QR nel flusso Cross Device. L'URL contiene ``client_id`` e ``request_uri``. Il contenuto normativo dell'URL è specificato nei Passaggi 4-7.

  2. *Richiesta URI Request*: l'Istanza del Wallet legge ``client_id``, ``request_uri`` e, se presente, ``request_uri_method`` dall'Authorization Request esterna prima di recuperare il Request Object. Il recupero è specificato nei Passaggi 9-11.

  3. *URI Request Response*: la Relying Party restituisce un Request Object firmato all'Istanza del Wallet.
  4. *Controlli Istanza di Wallet*: l'Istanza del Wallet seleziona esattamente un percorso di fiducia dal prefisso ``client_id`` e verifica il Request Object su quel percorso, come specificato in :ref:`trust-evaluation:Selection at Presentation` e nei Passaggi 12-15.

  5. *Risposta di Autorizzazione POST*: l'Istanza del Wallet presenta le informazioni richieste alla Relying Party.
  6. *Controlli RP*: La Relying Party convalida la risposta cifrata e le Credenziali presentate. La fiducia in ciascuna Credenziale presentata segue :ref:`trust-evaluation:Trust Framework Selection` ed è indipendente dal Trust Framework della Relying Party.
  7. *Risposta della Relying Party*: l'Istanza del Wallet informa l'Utente dell'autenticazione riuscita con la Relying Party, e l'Utente continua la navigazione.

Di seguito è riportato un diagramma di sequenza che dettaglia le interazioni tra tutte le parti coinvolte.

.. plantuml:: plantuml/credential-presentation-remote-flow.puml
    :width: 99%
    :alt: La figura illustra il Flusso Remoto.
    :caption: `Flusso di Protocollo Remoto. <https://www.plantuml.com/plantuml/svg/fLPDRnit4BtpLmpKGssWIPCU3RX8eXgnaxHMBIM-630exaXYJP5RSYX5BVBVEuFHhZwK5W6gcxGpxyrxyx5wLSXcgijWRAKKwtAAsHZpsb7ACFXOC0_05gZ6JDDd_U7x0h_WoZii0_ZkWvylw4seQ5h6ySwtDX8Cxcq8I70J6Juw50nO7uPKXdfcvnX96Qp1s02pRAdkC6nydCE8apR_pdGGzX3FRbzNMi0mU0O-5sHO7MLmILGBC5kR_9QzOC_E7-l8homXowxmx6UezWBkSGfZpA8RebtvkIMVubweDGtk9rh9NE45tE6V5Gl1A2T2HzZmBoNLxD2Ooql-6Gj6iW87euKj29UNFQvKly8EYlri6G9stW5jMdo8bA11GGUNKodyHGg5bA7O9UfN1L8r2re6Q1a1rfxj-lrkc1e9XqN66RZ4zVWejj82eUO0lJWjoMprrGiOBz9QmZeGGHKa5xnxaWUAEQr4AHvuP7SgryRCSwej3BdyRhuWnR0nQ-5PCu-paJb0IAHPHdgZZpuaPmF8R8Ajp1Z9EsrFdtsrig4A4-LQI5Lpf5J9uO-UuMmWyBE-NRVJFyJFwGQuVCmOsK3WppOiQzXZpVvnYRH83NYPeotsw7OyCQ2VTTS-de2LRn2ssy5fjh5aWPBKiW_PJsU7iMy-w6St5ZjnYnwSq4KljZZRsgaFdZmMISLGy1i4lBsQI1TZ8cXrGa_aT4u9Q_7pY4q72adDc-Mq_4zfA7rKBThB3kYm2qORVZI3fyqzE0RmQ-UlZGsqANWd5dH9dp3xsGQ4prBD26dMAJajO9TbWsVCNX57VXgTbNCDg3jJPYdB7ebnH_T4WOOfpdnUOdDuDdfpPO10RbdA_Yyz3dmsMa64XwWzMhMFb9um_W1oq_3aQ9nEXwhsTXhmyF2GuEmblIOI5SECZQoJ3N1JIiKC4zcVXoYUxinuTp-1SMUaedG3xx0KtRGUofWS4sUb5MOEuzD-y_PwylRkwkety_MC2mFFOBX0FYZNAJISzXutyCR7HhejfN1UcaaBHwaK1X1DjSXJaFaIkBPEWtVmn9dJL3d7H_bzNoCbhaV6GhqQgItFZT1VVQPidKvxuuiBgM03bYZxQIKi86KugL6souRG3xvd0j11p0XsPNsG1ZoNeHOdqEnPzh5jjhtIWzQ9ENCfFNc4Ai-nEJVTnHpBWTU3gLF1RCpeI9RDx1RhUZ8P_VZo-KluwSKBk7tFBVnxi1ywaBS2jKNEVGUay_RevAv_sOwuvHgB5dZ0j7VNHTZN3te-AJTL-iQAznTbVNGBz6rKs3zunmQFNVOjQJSkZju9kYkoGsT2q2soIbQJptTY2fgY1LNxlptyeYTi1wr67VnNKB3kbT3s_nco_cSuMVAkjD5fvD7Bzj2nLqnTb-4V>`_


.. .. Figure:: ../../images/cross_same_device_auth_seq_diagram.svg
..     :figwidth: 100%
..     :align: center
..     :target: https://www.plantuml.com/plantuml/svg/fLPDRnit4BtpLmpKGssWIPCU3RX8eXgnaxHMBIM-630exaXYJP5RSYX5BVBVEuFHhZwK5W6gcxGpxyrxyx5wLSXcgijWRAKKwtAAsHZpsb7ACFXOC0_05gZ6JDDd_U7x0h_WoZii0_ZkWvylw4seQ5h6ySwtDX8Cxcq8I70J6Juw50nO7uPKXdfcvnX96Qp1s02pRAdkC6nydCE8apR_pdGGzX3FRbzNMi0mU0O-5sHO7MLmILGBC5kR_9QzOC_E7-l8homXowxmx6UezWBkSGfZpA8RebtvkIMVubweDGtk9rh9NE45tE6V5Gl1A2T2HzZmBoNLxD2Ooql-6Gj6iW87euKj29UNFQvKly8EYlri6G9stW5jMdo8bA11GGUNKodyHGg5bA7O9UfN1L8r2re6Q1a1rfxj-lrkc1e9XqN66RZ4zVWejj82eUO0lJWjoMprrGiOBz9QmZeGGHKa5xnxaWUAEQr4AHvuP7SgryRCSwej3BdyRhuWnR0nQ-5PCu-paJb0IAHPHdgZZpuaPmF8R8Ajp1Z9EsrFdtsrig4A4-LQI5Lpf5J9uO-UuMmWyBE-NRVJFyJFwGQuVCmOsK3WppOiQzXZpVvnYRH83NYPeotsw7OyCQ2VTTS-de2LRn2ssy5fjh5aWPBKiW_PJsU7iMy-w6St5ZjnYnwSq4KljZZRsgaFdZmMISLGy1i4lBsQI1TZ8cXrGa_aT4u9Q_7pY4q72adDc-Mq_4zfA7rKBThB3kYm2qORVZI3fyqzE0RmQ-UlZGsqANWd5dH9dp3xsGQ4prBD26dMAJajO9TbWsVCNX57VXgTbNCDg3jJPYdB7ebnH_T4WOOfpdnUOdDuDdfpPO10RbdA_Yyz3dmsMa64XwWzMhMFb9um_W1oq_3aQ9nEXwhsTXhmyF2GuEmblIOI5SECZQoJ3N1JIiKC4zcVXoYUxinuTp-1SMUaedG3xx0KtRGUofWS4sUb5MOEuzD-y_PwylRkwkety_MC2mFFOBX0FYZNAJISzXutyCR7HhejfN1UcaaBHwaK1X1DjSXJaFaIkBPEWtVmn9dJL3d7H_bzNoCbhaV6GhqQgItFZT1VVQPidKvxuuiBgM03bYZxQIKi86KugL6souRG3xvd0j11p0XsPNsG1ZoNeHOdqEnPzh5jjhtIWzQ9ENCfFNc4Ai-nEJVTnHpBWTU3gLF1RCpeI9RDx1RhUZ8P_VZo-KluwSKBk7tFBVnxi1ywaBS2jKNEVGUay_RevAv_sOwuvHgB5dZ0j7VNHTZN3te-AJTL-iQAznTbVNGBz6rKs3zunmQFNVOjQJSkZju9kYkoGsT2q2soIbQJptTY2fgY1LNxlptyeYTi1wr67VnNKB3kbT3s_nco_cSuMVAkjD5fvD7Bzj2nLqnTb-4V

..     Remote Protocol Flow


I dettagli di ogni passaggio mostrato nell'immagine precedente sono descritti di seguito.

**Passaggi 1-2**: L'Utente richiede di accedere a una risorsa protetta della Relying Party.

**Passaggio 3**: La Relying Party crea un valore *state* fresco, crittograficamente casuale e con entropia sufficiente, lo associa alla sessione dello user-agent (ad esempio, utilizzando un cookie HTTP protetto) e lo memorizza lato server con un tempo di scadenza breve. Quindi ispeziona lo user-agent per determinare se il flusso avviene sullo stesso dispositivo dello user-agent.

**Passaggi 4-7 (Authorization Request)**: La Relying Party invoca l'Istanza del Wallet e passa l'Authorization Request per riferimento.

La Relying Party DEVE supportare i seguenti flussi remoti (:ref:`RPR-84 <test-plans-remote-presentation:Matrice di Test per il Verificatore di Credenziali in Remoto>`):

* **Same Device**: la Relying Party DEVE fornire un indirizzo HTTP all'Istanza del Wallet utilizzando un *redirect* (``302``) o un href HTML nella pagina web (:ref:`RPR-01 <test-plans-remote-presentation:Matrice di Test per il Verificatore di Credenziali in Remoto>`).
* **Cross Device**: la Relying Party DEVE fornire un Codice QR che l'Utente inquadra con la fotocamera del proprio dispositivo oppure con l'Istanza del Wallet (:ref:`RPR-03 <test-plans-remote-presentation:Matrice di Test per il Verificatore di Credenziali in Remoto>`).

La Relying Party DOVREBBE invocare l'Istanza del Wallet della Soluzione Wallet scelta dall'Utente.
L'Utente DOVREBBE indicare la Soluzione Wallet sulla Selection Page descritta in :ref:`functionalities:Design dell'Esperienza Utente`.

Quando la Selection Page è supportata, l'Utente seleziona la Soluzione Wallet. La Relying Party recupera quindi i metadata del Wallet come descritto in :ref:`wallet-metadata-retrieval:Flusso di Recupero dei Wallet Metadata`.

Quando ``authorization_endpoint`` è presente nei metadata del Wallet e il suo valore è un URL HTTPS, quell'URL è un link universale. Il sistema operativo associa quell'URL all'Istanza del Wallet installata e avvia quell'Istanza del Wallet quando l'Utente lo apre. La Relying Party DOVREBBE inserire quell'URL nell'href HTML del flusso Same Device o nel Codice QR del flusso Cross Device.

Quando ``authorization_endpoint`` è assente, oppure quando il suo valore non è un URL HTTPS, sul percorso EUDIW la Relying Party DEVE utilizzare ``eu-eaap://``.
L'Istanza del Wallet DEVE supportare ``eu-eaap://`` per il proprio ``authorization_endpoint`` ([`ETSI TS 119 472-2`_] clausola 6.4.1, OIDFVP-HAIP-REDIRECTS-03).
L'Istanza del Wallet DEVE supportare ``openid4vp://``. ``openid4vp://`` è definito nella Sezione 13.1.2 di [`OpenID4VP`_].
L'Istanza del Wallet DEVE supportare ``haip-vp://``. ``haip-vp://`` è definito nella Sezione 5.1 di [`OPENID4VC-HAIP`_].
Quando ``authorization_endpoint`` è assente, oppure quando il suo valore non è un URL HTTPS, sul percorso nazionale la Relying Party DEVE utilizzare uno tra ``openid4vp://``, ``haip-vp://`` e ``eu-eaap://``.

Quando la Relying Party non supporta la Selection Page, o quando il recupero dei metadata del Wallet non riesce, la Relying Party DEVE invocare l'Istanza del Wallet con lo schema richiesto sopra per quel percorso.

La Relying Party fornisce allo user-agent una pagina JavaScript che ispeziona lo *state endpoint* e all'Istanza del Wallet un URL contenente l'Authorization Request. Il Request Object è passato solo per riferimento. L'URL DEVE contenere ``client_id`` e ``request_uri``. L'URL NON DEVE contenere ``request``, come dettagliato in `OPENID4VC-HAIP`_. 

  Nel **Flusso Cross Device**, l'URI dell'Authorization Request viene presentato attraverso un Codice QR mostrato all'Utente. L'Utente scansiona il Codice QR utilizzando l'Istanza del Wallet e recupera un URL.
  Di seguito è rappresentato un esempio non normativo di un Codice QR emesso dalla Relying Party.

  .. only:: format_html

    .. figure:: ./images/svg/verifier_qr_code.svg
      :figwidth: 50%
      :align: center
      :alt: Codice QR mostrato dalla Relying Party nel flusso cross-device.

  .. only:: format_latex

    .. figure:: ./images/pdf/verifier_qr_code.pdf
      :width: 50%
      :align: center
      :alt: Codice QR mostrato dalla Relying Party nel flusso cross-device.

  .. note::
    Il *livello di correzione degli errori* scelto per il Codice QR DEVE essere Q (Quartile - fino al 25%), poiché offre un buon equilibrio tra capacità di correzione degli errori e densità/spazio dei dati. Questo livello di qualità e correzione degli errori consente al Codice QR di rimanere leggibile anche se è danneggiato o parzialmente oscurato (:ref:`RPR-77 <test-plans-remote-presentation:Matrice di Test per il Verificatore di Credenziali in Remoto>`).

  L'URL all'interno del Codice QR contiene ``client_id``, ``request_uri`` e, se presente, ``request_uri_method`` (:ref:`WP_076–077 <wallet-credential-presentation-testcases>`).
  Di seguito è riportato un esempio non normativo del contenuto del Codice QR per un Request Object per riferimento:

  .. code-block:: text

    https://wallet-solution.example.org/authorization?client_id=openid_federation%3A%2F%2Frelying-party.example.org&request_uri=https%3A%2F%2Frelying-party.example.org&request_uri_method=post

  Un template HTML ufficiale e autoconsistente per questa pagina QR **Cross Device**—con header, footer, accessibilità, testi multilingua e payload dimostrativo configurabile—è disponibile nella sezione :ref:`official-resources:Componenti HTML` (**IT-Wallet Presentation QR Code Page**). È raggiungibile dalle card della **IT-Wallet Selection Page** nella stessa sezione.

  Mentre, nel **Flusso Same Device**, la Relying Party risponde tramite HTTP Response Redirect (con codice di stato impostato a ``302``) o mostra all'utente una pagina html con un pulsante href, aventi l'URL che fornisce le stesse informazioni del Flusso Cross Device (:ref:`WP_076–077 <wallet-credential-presentation-testcases>`). 
  Di seguito è riportato un esempio non normativo per un Request Object by reference:

  .. code-block:: http

    HTTP/1.1 302 Found
    Location: https://wallet-solution.digital-strategy.europa.eu?client_id=openid_federation%3A%2F%2Frelying-party.example.org%2Fcb&request_uri=https%3A%2F%2Frelying-party.example.org%2Frequest_uri&request_uri_method=post


**Passaggio 8**: L'Istanza del Wallet valuta la trust con la Relying Party (:ref:`WP_078–080 <wallet-credential-presentation-testcases>`).

**Passaggi 9-11 (Richiesta URI Request)**: L'Istanza del Wallet verifica se la Relying Party ha fornito il request_uri_method all'interno del suo Request Object firmato (:ref:`WP_083 <wallet-credential-presentation-testcases>`).

  - Se è fornito ed è uguale a ``post``, l'Istanza del Wallet DEVE fornire i suoi metadata alla Relying Party con una richiesta HTTP POST e tipo di contenuto ``application/x-www-form-urlencoded``. La Relying Party aggiorna il Request Object in base alle capacità tecniche dell'Istanza del Wallet.

    Di seguito è riportato un esempio non normativo di una richiesta HTTP effettuata dall'Istanza del Wallet alla Relying Party.

    .. code-block:: http

      POST /request HTTP/1.1
      Host: client.example.org
      Content-Type: application/x-www-form-urlencoded
      Accept: application/oauth-authz-req+jwt

      wallet_metadata=%7B%22vp_formats_supported%22%3A%7B%22dc%2Bsd-jwt%22%3A%7B%22sd-jwt_alg_values%22%3A%5B%22ES256%22%2C%22ES384%22%5D%7D%2C%22mso_mdoc%22%3A%7B%22issuerauth_alg_values%22%3A%5B-9%2C-51%5D%2C%22deviceauth_alg_values%22%3A%5B-9%2C-51%5D%7D%7D%2C%22request_object_signing_alg_values_supported%22%3A%5B%22ES256%22%5D%2C%22client_id_prefixes_supported%22%3A%5B%22openid_federation%22%2C%22x509_hash%22%5D%7D&wallet_nonce=qPmxiNFCR3QTm19POc8u

    Dove il corpo della richiesta prima di essere codificato in ``application/x-www-form-urlencoded`` dal Wallet corrisponde a:

    .. code-block:: json

      {
        "wallet_metadata": {
          "vp_formats_supported": {
            "dc+sd-jwt": {
              "sd-jwt_alg_values": ["ES256","ES384"]
            },
            "mso_mdoc": {
              "issuerauth_alg_values": [-9,-51],
              "deviceauth_alg_values": [-9,-51]
            }
          },
          "request_object_signing_alg_values_supported": ["ES256"],
          "client_id_prefixes_supported": ["openid_federation","x509_hash"]
        },
        "wallet_nonce": "qPmxiNFCR3QTm19POc8u"
      }

  - Se ``request_uri_method`` è uguale a ``get`` o non è presente, l'Istanza del Wallet DEVE richiedere il Request Object firmato con il metodo HTTP GET (:ref:`WP_082 <wallet-credential-presentation-testcases>`).

**Passaggio 12 (URI Request Response)**: La Relying Party emette il Request Object firmandolo con una delle sue chiavi private crittografiche.

* Per ``openid_federation``, la Wallet Unit DEVE valutare la fiducia usando la Federation Entity Authentication e l'Authorization nazionale (:ref:`trust-evaluation:Federation Entity Authentication` e :ref:`trust-evaluation:Authorization`). La Wallet Unit DEVE ottenere i metadata ``openid_credential_verifier`` tramite :ref:`trust-evaluation:Metadata Retrieval and Validation`. La Wallet Unit DEVE verificare la firma con la chiave identificata da ``kid`` in quei metadata.
* Per ``x509_hash``, la Wallet Unit DEVE verificare l'hash del certificato foglia rispetto a ``client_id``. La Wallet Unit DEVE validare il percorso del WRPAC rispetto alla LoTE dei Provider of WRPAC. La Wallet Unit DEVE verificare la firma con la chiave del WRPAC, come definito in :ref:`trust-evaluation:EUDIW Authentication`.

L'Istanza del Wallet NON DEVE cambiare percorso (:ref:`WP_084 <wallet-credential-presentation-testcases>`).
L'Istanza del Wallet NON DEVE ripetere la verifica con evidenze dell'altro percorso.

  Di seguito è riportato un esempio non normativo della Risposta URI di Reindirizzamento:

  .. literalinclude:: ../../examples/shared/remote-flow-1.http
     :language: http

**Passaggi 13-15 (Controlli WI)**: L'Istanza del Wallet verifica il Request Object, che ha la forma di un JWT firmato. Controlla che ``client_id``, ``iss`` e l'identità della Relying Party della richiesta esterna e della richiesta firmata siano coerenti rispetto al prefisso selezionato (:ref:`WP_085–086 <wallet-credential-presentation-testcases>`).

  Di seguito sono riportati esempi non normativi di Request Object sotto forma di intestazioni e payload decodificati. Ciascun esempio usa esattamente un Trust Framework.

  L'esempio non normativo seguente è il Request Object EUDIW che usa ``x509_hash``.

  .. literalinclude:: ../../examples/shared/remote-flow-2.json
     :language: json

  .. literalinclude:: ../../examples/shared/remote-flow-3.json
     :language: json

  L'esempio non normativo seguente è il Request Object nazionale che usa ``openid_federation``.

  .. literalinclude:: ../../examples/shared/remote-flow-4.json
     :language: json

  .. literalinclude:: ../../examples/shared/remote-flow-5.json
     :language: json

* Per ``x509_hash``, l'Istanza del Wallet autentica il WRPAC e valida il WRPRC. Vincola l'identità della Relying Party diretta o intermediata al WRPAC, al WRPRC e al membro ``data.identifier`` dell'elemento ``verifier_info`` il cui ``format`` è ``registrar_dataset``, secondo :ref:`trust-evaluation:EUDIW Authentication` e :ref:`trust-evaluation:EUDIW Authorization`. Controlla l'entitlement di Service Provider e lo scope DCQL esatto e sensibile alle maiuscole.

* Per ``openid_federation``, l'Istanza del Wallet valida il Trust Mark di registrazione, i suoi entitlement e il suo scope esatto e sensibile alle maiuscole. L'Istanza del Wallet NON DEVE trattare il materiale WRPAC o WRPRC come evidenza di fiducia del Trust Framework Nazionale.

Una valutazione fallita termina l'elaborazione. L'Istanza del Wallet NON DEVE innescare un nuovo tentativo nell'ambito dell'altro framework (:ref:`WP_087 <wallet-credential-presentation-testcases>`).

**Passaggi 16-17 (Consenso dell'Utente)**: Prima della divulgazione, l'Istanza del Wallet DEVE mostrare la Relying Party verificata. L'Istanza del Wallet DEVE mostrare il Service verificato. L'Istanza del Wallet DEVE mostrare l'uso previsto o lo scopo. L'Istanza del Wallet DEVE mostrare le Credenziali richieste tratte dall'artifact di autorizzazione autorevole. L'Istanza del Wallet DEVE mostrare gli attributi richiesti tratti dall'artifact di autorizzazione autorevole. Nel percorso nazionale, l'Istanza del Wallet DEVE mostrare anche il Federation Intermediate, ove applicabile. In un flusso EUDIW intermediato, l'Istanza del Wallet DEVE mostrare la Relying Party intermediata. L'Istanza del Wallet NON DEVE mostrare le denominazioni commerciali dell'Intermediario. L'Utente autorizza e acconsente alla presentazione selezionando i dati da rilasciare (:ref:`WP_088 <wallet-credential-presentation-testcases>`).

**Passaggio 18 (Authorization Response)**: L'Istanza del Wallet fornisce la Authorization Response alla Relying Party utilizzando una richiesta HTTP con il metodo POST utilizzando modalità di risposta ``direct_post.jwt``.

  Di seguito è riportato un esempio non normativo della Authorization Response:

  .. literalinclude:: ../../examples/shared/remote-flow-6.http
     :language: http

  Di seguito è riportato un esempio non normativo che mostra l'intestazione protetta del JWE decifrata e il payload del JWT contenuto nel parametro ``response``, prima della codifica base64url. Il valore del parametro ``vp_token`` corrisponde al formato utilizzato quando il linguaggio di query DCQL è utilizzato nella richiesta di presentazione.

  .. literalinclude:: ../../examples/shared/remote-flow-jwe-protected-header.json
     :language: json

.. literalinclude:: ../../examples/shared/remote-flow-7.json
   :language: json

.. note::
  Quando restituisce una Credenziale richiesta nel formato ``mso_mdoc`` all'interno di ``vp_token``, l'Istanza del Wallet DEVE vincolare crittograficamente la presentazione mdoc alla transazione OpenID4VP corrente, come definito nell'Appendice B.2 di `OpenID4VP`_.

**Passaggi 19-22 (Controlli RP)**: La Relying Party verifica la Authorization Response cifrata, estrae il ``vp_token`` e ne valida il formato complessivo e ciascuna presentazione rispetto alla query DCQL.

Per SD-JWT VC, la risoluzione della chiave dell'emittente DEVE usare la catena X.509 ``x5c``, esclusi il trust anchor e un certificato di firma non auto-firmato.
La Relying Party DEVE validare la firma dell'emittente.
La Relying Party DEVE validare la firma del titolare.
La Relying Party DEVE validare la prova di possesso.
Il controllo di stato è specificato in :ref:`credential-revocation:Verifica degli Stati degli Attestati Elettronici`.

La validazione della firma di presentazione DEVE supportare almeno ES256 su P-256 con SHA-256.
La validazione dell'hash DEVE supportare SHA-256.

La fiducia in ciascuna Credenziale presentata è governata dal Rulebook di quella Credenziale ed è indipendente dal percorso di fiducia della Relying Party.
Selezionare ``x509_hash`` NON DEVE implicare fiducia federata nel Fornitore di Attestati Elettronici.

Se tutte le verifiche riescono, la Relying Party aggiorna la sessione dell'Utente.

**Passaggi 23-24 o 25 (Risposta della Relying Party)**: La Relying Party fornisce all'Istanza del Wallet la risposta sulla presentazione, che a sua volta informa l'Utente.

  Dopo aver ricevuto e convalidato la Authorization Response al Response Endpoint, la Relying Party restituisce all'Istanza del Wallet un codice di stato HTTP 200 OK.
  Nel Flusso Same Device, la Relying Party DEVE includere il parametro ``redirect_uri`` nella risposta all'Istanza del Wallet (:ref:`RPR-83 <test-plans-remote-presentation:Matrice di Test per il Verificatore di Credenziali in Remoto>`).
  Dopo aver ricevuto il ``redirect_uri``, l'Istanza del Wallet DEVE eseguire un reindirizzamento all'URL specificato dal ``redirect_uri``.
  Nel Flusso Cross Device, la risposta non contiene ``redirect_uri``.
  L'Istanza del Wallet non esegue il reindirizzamento.

  Di seguito è riportato un esempio non normativo della risposta nel Flusso Same Device.

.. literalinclude:: ../../examples/shared/remote-flow-8.http
   :language: http

**Passaggi 26-27**: La pagina JavaScript continua ad ispezionare lo Status Endpoint.

  Di seguito è riportato un esempio non normativo della Richiesta HTTP allo Status Endpoint, dove il parametro ``id`` contiene un valore opaco e casuale:

  .. literalinclude:: ../../examples/shared/remote-flow-9.http
     :language: http

  Quando l'Istanza del Wallet ha fornito la presentazione all'endpoint **response_uri** della Relying Partye, nel Flusso Same Device, lo user-agent è ritornato correttamente tramite ``redirect_uri`` all'interno della stessa sessione utente, e l'autenticazione dell'Utente ha avuto successo. La Relying Party aggiorna il cookie di sessione consentendo all'user-agent di accedere alla risorsa protetta. Viene fornito un URL di reindirizzamento che trasporta la posizione in cui l'user-agent deve navigare.
  Di seguito è riportato un esempio non normativo della risposta con il redirect_uri dalla Relying Party all'user-agent.

  .. literalinclude:: ../../examples/shared/remote-flow-10.http
     :language: http

**Passaggi 28-29**: Nel Flusso Same Device, lo user-agent viene reindirizzato al ``redirect_uri`` per continuare la navigazione con la risorsa protetta resa disponibile all'Utente (:ref:`WP_094 <wallet-credential-presentation-testcases>`). La Relying Party DEVE considerare la transazione completata solo se il reindirizzamento di ritorno viene ricevuto nella stessa sessione utente in cui il flusso è stato avviato. In caso contrario, la Relying Party DEVE rifiutare la presentazione.
Nel Flusso Cross Device, il completamento non dipende da quel reindirizzamento.

.. note::
    Durante ciascuna transazione di presentazione di Credenziali eseguita tramite il flusso remoto, l'Istanza del Wallet DEVE creare e mantenere un corrispondente record di transazione nel registro delle transazioni (vedere :ref:`wallet-instance-dashboard:Dashboard dell’Istanza del Wallet e Registrazione delle Transazioni`).

    Il record di transazione DEVE essere creato una volta che l'Istanza del Wallet ha accettato la richiesta di presentazione per l’elaborazione (ossia, dopo la validazione della richiesta e i controlli di trust/policy della Relying Party, Passaggi 13–15). A questo punto, il record DEVE includere i metadati della transazione e il contesto della richiesta disponibile in quella fase (ad esempio, il/i tipo/i di Credenziale richiesti e l’/gli identificativo/i degli attributi richiesti), senza registrare alcun valore degli attributi.

    Il record DEVE essere aggiornato man mano che la transazione procede, in modo da riflettere l’evoluzione dello stato della transazione e il contesto del risultato (ad esempio, quanto effettivamente presentato dopo il consenso dell’Utente e la preparazione/invio della risposta, Passaggi 16–18), senza registrare alcun valore degli attributi.

    Il record DEVE essere finalizzato al termine della transazione, indicando l’esito (ad esempio, completata, fallita o interrotta. Passaggi 23–29).


Authorization Request
^^^^^^^^^^^^^^^^^^^^^

I parametri URL contenuti nella Authorization Request della Relying Party sono descritti nella tabella seguente.

.. list-table::
  :class: longtable
  :widths: 25 50
  :header-rows: 1

  * - **Nome**
    - **Descrizione**
  * - **client_id**
    - OBBLIGATORIO. Identificatore univoco della Relying Party. Il valore DEVE utilizzare uno dei seguenti prefissi di identificatore del Client (come definito in OpenID4VP_, Sezione 5.9): ``openid_federation`` (identificatore dell’entità della Relying Party in una catena di fiducia) oppure ``x509_hash`` (hash SHA-256 codificato in base64url del certificato X.509 della Relying Party).
  * - **request_uri**
    - OBBLIGATORIO. URL HTTPS dove la Relying Party fornisce il Request Object firmato all'Istanza del Wallet. Il Request Object DEVE essere recuperato per riferimento.
  * - **request_uri_method**
    - OPZIONALE solo se ``request_uri`` è presente. Altrimenti NON DEVE essere presente. Il valore DEVE essere ``get`` o ``post`` (:ref:`RPR-07 <test-plans-remote-presentation:Matrice di Test per il Verificatore di Credenziali in Remoto>`, :ref:`RPR-08 <test-plans-remote-presentation:Matrice di Test per il Verificatore di Credenziali in Remoto>`, :ref:`RPR-09 <test-plans-remote-presentation:Matrice di Test per il Verificatore di Credenziali in Remoto>`). Se non è fornito o è uguale a ``get``, l'Istanza del Wallet DEVE recuperare il Request Object con il metodo HTTP ``GET``. Se è uguale a ``post``, l'Istanza del Wallet DEVE fornire i suoi metadata nel corpo della richiesta HTTP POST, codificati in ``application/x-www-form-urlencoded``.

Il valore corrispondente all'endpoint ``request_uri`` DOVREBBE essere casuale, secondo quanto prescritto da :rfc:`9101#section-5.2.1`.

.. _endpoint-mix-up-protection:

Protezione da Endpoint Mix-Up
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. warning::
  Per prevenire attacchi di tipo endpoint mix-up, i valori di ``request_uri``, ``response_uri`` e ``redirect_uri`` DEVONO ciascuno essere attestati da una terza parte fidata.
  Sotto il Trust Framework Nazionale DEVONO corrispondere ai parametri ``request_uris``, ``response_uris`` e ``redirect_uris`` nei metadata ``openid_credential_verifier`` ottenuti dalla Trust Chain.
  Sotto il Trust Framework EUDIW DEVONO corrispondere all'identità vincolata al Wallet-Relying Party Access Certificate e al Wallet-Relying Party Registration Certificate, come specificato in :ref:`trust-evaluation:Selection at Presentation`.

  Questo requisito si applica a ``request_uri`` come specificato in :ref:`WP_081 <wallet-credential-presentation-testcases>` e :ref:`RPR-85 <test-plans-remote-presentation:Matrice di Test per il Verificatore di Credenziali in Remoto>`.


Richiesta all'Endpoint URI Request
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

La Relying Party DOVREBBE abilitare il metodo POST nel suo Endpoint ``request_uri`` consentendo all'Istanza del Wallet di informare la Relying Party sulle sue capacità tecniche.

Questa funzionalità può essere utile quando, ad esempio, l'Istanza del Wallet supporta un insieme ristretto di funzionalità, algoritmi o un URL specifico per il suo ``authorization_endpoint``, e qualsiasi altra informazione che ritiene necessario fornire alla Relying Party per l'interoperabilità.

.. warning::
  L'Istanza del Wallet, quando fornisce le sue capacità tecniche alla Relying Party, NON DEVE includere alcuna informazione dell'Utente o altre informazioni esplicite riguardanti l'hardware utilizzato o le preferenze di utilizzo del suo Utente (:ref:`RPR-86 <test-plans-remote-presentation:Matrice di Test per il Verificatore di Credenziali in Remoto>`).

Quando ``request_uri_method`` è ``post``, l'Istanza del Wallet fornisce i metadata come specificato nei Passaggi 9-11 (:ref:`WP_083 <wallet-credential-presentation-testcases>`).
La richiesta e i suoi parametri sono definiti nella Sezione 5 (Authorization Request) di `OpenID4VP`_. Di seguito sono riportati i dettagli normativi e i riferimenti sui parametri da utilizzare dall'Istanza del Wallet nella Richiesta URI Request (:ref:`WP_083a–WP_083c <wallet-credential-presentation-testcases>`).

.. list-table:: Parametri dell'Endpoint URI Request
   :class: longtable
   :widths: 20 80
   :header-rows: 1

   * - Parametro
     - Descrizione
   * - `wallet_metadata`
     - OBBLIGATORIO nel corpo della richiesta quando ``request_uri_method`` è ``post``. JSON Object con parametri di metadata. Vedi `OpenID4VP`_, Sezione 10.1 e la tabella seguente, "Parametri dei metadata del Wallet".
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
     - OBBLIGATORIO. Oggetto contenente un elenco di coppie nome/valore, in cui il nome è un identificatore di formato di Credenziale e il valore definisce i parametri specifici del formato supportati da un Wallet. Vedere `OpenID4VP`_ Appendice B. Le Istanze del Wallet DEVONO supportare gli identificatori di formato di Credenziale richiesti da `OPENID4VC-HAIP`_ (inclusi ``dc+sd-jwt`` e ``mso_mdoc``).
   * - `client_id_prefixes_supported`
     - OBBLIGATORIO. Un array non vuoto dei prefissi dell’identificatore del Client supportati dall’Istanza del Wallet. Le Istanze del Wallet DEVONO includere sia ``x509_hash`` (EUDIW / [`OPENID4VC-HAIP`_]) sia ``openid_federation`` (Trust Framework Nazionale).
   * - `request_object_signing_alg_values_supported`
     - OPZIONALE. Vedi OpenID Connect Discovery.


.. note::
   Nell’IT Wallet, le Relying Party legacy che utilizzano un URI ``https`` come ``client_id`` seguono implicitamente il prefisso dell’identificatore del client previsto da OpenID Federation (``openid_federation``).  La loro fiducia è stabilita e validata tramite la risoluzione della catena di fiducia, che è considerata equivalente a quella dei client fidati staticamente (``pre-registered``), come definito in [:rfc:`6749`], per garantire la compatibilità con le versioni precedenti.

.. note::
  Il parametro ``wallet_nonce`` è RACCOMANDATO per le Istanze del Wallet che vogliono prevenire il *replay* delle
  loro richieste HTTP alle Relying Party da parte di avversari. Quando presente, la Relying Party DEVE controllarlo (:ref:`RPR-81 <test-plans-remote-presentation:Matrice di Test per il Verificatore di Credenziali in Remoto>`).


Risposta dell'Endpoint URI Request
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

La Relying Party emette il Request Object firmato utilizzando il tipo di contenuto impostato su ``application/oauth-authz-req+jwt``. Per il contenuto dell'oggetto Request, vedere la Sezione :ref:`remote-flow:Request Object`.

Errori dell'Endpoint URI Request
--------------------------------

Quando la Relying Party incontra errori durante l'emissione del Request Object dall'endpoint ``request_uri``, DEVE restituire una *Error Response* con ``application/json`` come tipo di contenuto.
La risposta DEVE includere i seguenti parametri:

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

.. literalinclude:: ../../examples/shared/remote-flow-11.http
   :language: http

Dopo aver ricevuto una *Error Response*, l'Istanza del Wallet DOVREBBE informare l'Utente della condizione di errore in modo appropriato (:ref:`WP_089 <wallet-credential-presentation-testcases>`).
L'Istanza del Wallet DOVREBBE registrare l'errore (:ref:`WP_089a <wallet-credential-presentation-testcases>`).
L'Istanza del Wallet PUÒ tentare di recuperare da determinati errori, se fattibile.
Il recupero DEVE restare sul trasporto e sul percorso di fiducia già selezionati.
Un nuovo Codice QR PUÒ essere offerto ove applicabile (:ref:`WP_089b <wallet-credential-presentation-testcases>`).

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
    - OBBLIGATORIO. Algoritmo utilizzato per firmare il JWT, secondo [:rfc:`7516#section-4.1.1`]. DEVE essere uno degli algoritmi supportati nella Sezione :ref:`algorithms:Algoritmi Crittografici`. NON DEVE essere impostato su ``none`` o su un identificatore di algoritmo simmetrico (MAC) (:ref:`RPR-88 <test-plans-remote-presentation:Matrice di Test per il Verificatore di Credenziali in Remoto>`).
  * - **typ**
    - OBBLIGATORIO. Media Type del JWT, come definito in [:rfc:`7519`] e [:rfc:`9101`]. Il valore DEVE essere ``oauth-authz-req+jwt`` (:ref:`RPR-89 <test-plans-remote-presentation:Matrice di Test per il Verificatore di Credenziali in Remoto>`).
  * - **kid**
    - Solo sul percorso nazionale. OBBLIGATORIO quando ``client_id`` utilizza il prefisso ``openid_federation``. Identifica la chiave pubblica nei metadata di Federazione ottenuti dopo :ref:`trust-evaluation:Federation Entity Authentication` e :ref:`trust-evaluation:Metadata Retrieval and Validation`, come definito in [:rfc:`7517`]. Non è evidenza di autenticazione EUDIW.
  * - **trust_chain**
    - Solo sul percorso nazionale. OPZIONALE. Sequenza di Entity Statement che compongono la Trust Chain della Relying Party, come definito in `OID-FED`_ Sezione 4.3 *Trust Chain Header Parameter*. Non è evidenza di autenticazione EUDIW.
  * - **x5c**
    - Solo sul percorso EUDIW. OBBLIGATORIO quando ``client_id`` utilizza il prefisso ``x509_hash``. Contiene prima il WRPAC, poi la catena crittografica fino al trust anchor escluso. Il WRPAC DEVE essere usato per verificare la firma del JWT. La catena DEVE essere valida rispetto alla LoTE dei Provider of WRPAC, come definito in :ref:`trust-evaluation:EUDIW Authentication`. Il WRPAC vincola l'identità della Relying Party e gli endpoint di presentazione applicabili secondo :ref:`trust-evaluation:EUDIW Authorization`. Non è evidenza di autenticazione nazionale.

.. note::
   Per ``x509_hash``, l'intestazione ``x5c`` DEVE contenere prima il WRPAC. L'intestazione ``x5c`` NON DEVE includere il trust anchor, come richiesto da `OPENID4VC-HAIP`_. La catena DEVE validare verso un trust anchor ottenuto dalla LoTE dei Provider of WRPAC secondo :ref:`trust-evaluation:EUDIW Authentication`. Vedere la Sezione :ref:`infrastructure-trust:X.509 Certificate Profile` per informazioni di base sulla validazione della catena di certificati X.509.

I parametri del payload JWT sono descritti qui:

.. list-table::
  :class: longtable
  :widths: 25 50
  :header-rows: 1

  * - **Nome**
    - **Descrizione**
  * - **client_id**
    - OBBLIGATORIO. Identificatore univoco della Relying Party. DEVE usare lo stesso valore qualificato dal prefisso dell'Authorization Request. DEVE identificare la stessa Relying Party di ``iss`` e dell'evidenza di fiducia selezionata.
  * - **client_metadata**
    - OBBLIGATORIO su entrambi i percorsi. Oggetto JSON che contiene i valori dei metadata della Relying Party definiti nella sezione 5.1 di `OpenID4VP`_. Contiene i parametri seguenti:

      - ``jwks``. OBBLIGATORIO secondo [`ETSI TS 119 472-2`_]. Contiene la chiave pubblica effimera di cifratura della risposta, specifica della richiesta, e le capacità di cifratura della risposta applicabili. Ogni chiave DEVE avere ``kid`` e ``use``. Ciascun ``kid`` DEVE identificare esattamente una chiave. I metadata del verificatore DEVONO elencare sia ``A128GCM`` sia ``A256GCM``. Per ``x509_hash``, i metadata applicabili della Relying Party sono trasportati qui.
      - **vp_formats_supported**. Utilizzato dall'Istanza del Wallet per determinare i formati di Verifiable Presentation supportati.
      - **client_name** e **logo_uri**. OPZIONALE. Utilizzati per la visualizzazione del consenso dell'utente e per mostrare l'identità della Relying Party nell'interfaccia dell'Istanza del Wallet.
  * - **verifier_info**
    - OBBLIGATORIO sul percorso EUDIW [`ETSI TS 119 472-2`_]. Array di oggetti, come richiesto da :ref:`trust-evaluation:EUDIW Authorization`.

      Ciascun oggetto DEVE contenere ``format`` e ``data``.
      L'array DEVE contenere un oggetto il cui ``format`` è ``registrar_dataset``.
      Il suo ``data`` DEVE essere un oggetto non vuoto contenente i membri registrati ``identifier``, ``srvDescription``, ``registryURI``, ``intendedUseIdentifier``, ``purpose`` e ``policyURI``.
      ``srvDescription`` e ``purpose`` DEVONO usare valori ``MultiLangString`` registrati.
      L'array DEVE contenere un oggetto il cui ``format`` è ``registration_cert``.
      Il suo ``data`` DEVE essere la serializzazione base64url del WRPRC.
      L'array NON DEVE contenere ``credential_ids`` [`ETSI TS 119 472-2`_].
      Questi oggetti non sono richiesti per ``openid_federation``, i cui dati equivalenti di autorizzazione e trasparenza provengono dal Trust Mark di registrazione validato (vedi :ref:`trust-evaluation:Metadata Retrieval and Validation`).
  * - **response_mode**
    - OBBLIGATORIO. DEVE essere impostato su ``direct_post.jwt`` sia nel Flusso Same Device sia nel Flusso Cross Device (:ref:`RPR-90 <test-plans-remote-presentation:Matrice di Test per il Verificatore di Credenziali in Remoto>`).
  * - **dcql_query**
    - OBBLIGATORIO. Oggetto che rappresenta una richiesta di presentazione di Credenziali, secondo il linguaggio di query DCQL definito nella Sezione 6 di `OpenID4VP`_.
  * - **transaction_data**
    - OPZIONALE. Array non vuoto di stringhe. Ciascuna stringa è un oggetto JSON codificato in base64url che descrive una transazione che la Relying Party richiede all’Utente di autorizzare, come definito nella Sezione 5.1 di `OpenID4VP`_. L’oggetto decodificato include:
        - **type**. Stringa che identifica il tipo di dati della transazione.
        - **credential_ids**. Array che fa riferimento a una o più Credenziali provenienti dalla ``dcql_query`` che possono autorizzare la transazione.
        - **transaction_data_hashes_alg**. OPZIONALE, e solo per ``dc+sd-jwt``. Array di stringhe, ciascuna delle quali rappresenta un identificatore di algoritmo di hash elencato nel registro IANA. Uno di questi algoritmi DEVE essere utilizzato per calcolare gli hash nel parametro ``transaction_data_hashes`` del Key Binding JWT. Se omesso, l’algoritmo di hash DEVE essere ``sha-256``. Vedere `OpenID4VP`_, Appendice B.3.3.
  * - **response_type**
    - OBBLIGATORIO. DEVE essere impostato su ``vp_token`` (:ref:`RPR-91 <test-plans-remote-presentation:Matrice di Test per il Verificatore di Credenziali in Remoto>`).
  * - **wallet_nonce**
    - OBBLIGATORIO se precedentemente fornito dall'Istanza del Wallet (:ref:`RPR-81 <test-plans-remote-presentation:Matrice di Test per il Verificatore di Credenziali in Remoto>`). Valore stringa utilizzato per mitigare gli attacchi di replay della Request URI Response, come definito nella Sezione 5.10 (Request URI Method) di `OpenID4VP`_.
  * - **response_uri**
    - OBBLIGATORIO. L'URI di Risposta a cui l'Istanza del Wallet DEVE inviare la Authorization Response utilizzando una HTTP Request con il metodo POST (:ref:`RPR-92 <test-plans-remote-presentation:Matrice di Test per il Verificatore di Credenziali in Remoto>`).
  * - **nonce**
    - OBBLIGATORIO. Numero unico e casuale con sufficiente entropia, la cui lunghezza DEVE essere di almeno 32 cifre (:ref:`RPR-93 <test-plans-remote-presentation:Matrice di Test per il Verificatore di Credenziali in Remoto>`).
  * - **state**
    - RACCOMANDATO. Identificatore univoco della Authorization Request, il suo valore DOVREBBE essere opaco per l’Istanza del Wallet.
  * - **iss**
    - OBBLIGATORIO. L'entità che ha emesso il JWT. DEVE essere uguale al ``client_id`` qualificato dal prefisso e all'identità dell'emittente dell'Authorization Request.
  * - **iat**
    - OBBLIGATORIO. Timestamp Unix, che rappresenta l'ora in cui il JWT è stato emesso.
  * - **exp**
    - OBBLIGATORIO. Timestamp Unix, che rappresenta l'ora di scadenza in cui o dopo la quale il JWT NON DEVE più essere valido (:ref:`RPR-94 <test-plans-remote-presentation:Matrice di Test per il Verificatore di Credenziali in Remoto>`).

.. warning::
  Il parametro ``response_uri`` è soggetto a :ref:`endpoint-mix-up-protection` (:ref:`WP_091a <wallet-credential-presentation-testcases>` e :ref:`RPR-95 <test-plans-remote-presentation:Matrice di Test per il Verificatore di Credenziali in Remoto>`).

.. note::
  Quando ``transaction_data`` è presente, l'Istanza del Wallet vincola i dettagli della transazione alla Authorization Response con il meccanismo del formato della Credenziale.

  - **dc+sd-jwt**: l'Istanza del Wallet DEVE restituire ``transaction_data_hashes`` e, quando applicabile, ``transaction_data_hashes_alg`` all'interno del Key Binding JWT (KB-JWT). Vedere `OpenID4VP`_ Appendice B.3.3.
  - **mso_mdoc**: l'Istanza del Wallet DEVE vincolare i dati tramite l'autenticazione del dispositivo mdoc, come definito in `OpenID4VP`_ Appendice B.2.1. Se il ``type`` non è supportato dal tipo di documento o non è autorizzato dall'emittente (KeyAuthorizations), l'Istanza del Wallet DEVE rifiutare la richiesta.

.. note::
  Il parametro ``state`` lega la Authorization Request alla risposta e consente alla Relying Party di riconoscere la sessione. Serve a prevenire attacchi Cross-Site Request Forgery (CSRF) includendo un valore unico e imprevedibile.

.. note::

  ``client_metadata`` e ``client_metadata.jwks`` sono richiesti su entrambi i percorsi profilati, perché ogni richiesta fornisce una chiave pubblica effimera di cifratura della risposta, specifica della richiesta [`ETSI TS 119 472-2`_].
  Sul percorso nazionale, la Wallet Unit DEVE ottenere i metadata del verificatore dalla Trust Chain (:ref:`RPR-96 <test-plans-remote-presentation:Matrice di Test per il Verificatore di Credenziali in Remoto>`).
  ``client_metadata`` NON DEVE sostituire quei metadata.
  ``client_metadata.jwks`` e i parametri di cifratura della risposta trasportano la chiave effimera specifica della richiesta.

Authorization Response
^^^^^^^^^^^^^^^^^^^^^^
Dopo aver ottenuto l'autorizzazione e il consenso dell'Utente per la presentazione degli Attestati Elettronici, l'Istanza del Wallet invia la Authorization Response all'endpoint ``response_uri`` della Relying Party utilizzando una richiesta HTTP con il metodo POST (:ref:`WP_091 <wallet-credential-presentation-testcases>`).

Quando l'Istanza del Wallet utilizza Credenziali ottenute in batch, l'Istanza del Wallet DOVREBBE implementare una logica di selezione delle Credenziali, ad esempio basata sulla prima in scadenza. L'Istanza del Wallet DEVE contrassegnare la Credenziale selezionata come consumata. Al termine del flusso, l'Istanza del Wallet DEVE ridurre il numero di Credenziali disponibili nel batch. In base a quel numero, l'Istanza del Wallet può verificare se è il momento di richiedere un nuovo batch di Credenziali.

Ogni risposta riuscita DEVE essere cifrata con la chiave pubblica effimera specifica della richiesta, selezionata da ``client_metadata.jwks`` tramite il suo ``kid`` (:ref:`WP_092 <wallet-credential-presentation-testcases>`).
Ogni risposta riuscita DEVE usare ``direct_post.jwt``.
Il verificatore DEVE supportare sia ``A128GCM`` sia ``A256GCM``.
L'Istanza del Wallet DEVE supportare almeno uno tra ``A128GCM`` e ``A256GCM``.
L'Istanza del Wallet DOVREBBE preferire ``A256GCM`` quando entrambi sono disponibili [`ETSI TS 119 472-2`_].

.. note:: Perché la risposta è cifrata?

    La risposta inviata dall'Istanza del Wallet alla Relying Party è cifrata per impedire a un avversario di sfruttare possibili vulnerabilità per accedere alle informazioni trasmesse in chiaro all'interno della rete della Relying Party. Per esempio, ciò è possibile se l'ambiente di rete della Relying Party impiega un proxy per le operazioni di `TLS Termination <https://www.f5.com/glossary/ssl-termination>`_, il quale agisce come intermediario tra il client e il backend web server della Relying Party e gestisce tutte le operazioni relative a TLS. In questo caso specifico, il proxy decifra il contenuto della trasmissione, in seguito lo inoltra al backend web server della Relying Party. Questa operazione può avvenire in chiaro oppure negoziando una ulteriore sessione TLS con il web server della Relying Party (sempre raccomandato). Nel primo caso, trasmissione dei dati TLS in chiaro, qualsiasi avversario all'interno del segmento di rete fra proxy e web server backend che intercettasse i dati trasmessi, potrebbe ottenere informazioni sensibili. Se però la risposta è cifrata, la fattispece descritta viene mitigata anche mandando i dati in chiaro.

Nella Authorization Response vengono utilizzati i seguenti parametri (:ref:`WP_093 <wallet-credential-presentation-testcases>`):

.. list-table::
  :class: longtable
  :widths: 25 50
  :header-rows: 1

  * - **Nome**
    - **Descrizione**
  * - **vp_token**

    - Questo oggetto DEVE contenere gli Attestati Elettronici presentati, indicizzati in base ai valori ``id`` delle Credenziali presenti nella ``dcql_query`` della Authorization Request.

      Il ``vp_token`` DEVE essere un oggetto JSON in cui ogni chiave corrisponde all'identificativo di una Credenziale richiesta e ogni valore è una singola presentazione oppure un array contenente una o più presentazioni relative a quella Credenziale. La codifica di ciascuna presentazione dipende dal formato della Credenziale, ad esempio:

      - **dc+sd-jwt**: una stringa SD-JWT VC (incluso il Key Binding JWT aggiunto in coda) (:ref:`WP_093a <wallet-credential-presentation-testcases>`).
      - **mso_mdoc**: un ``DeviceResponse`` CBOR codificato in base64url corrispondente alla presentazione mdoc richiesta (vedere `OpenID4VP`_ Appendice B.2). Quando vengono restituite più presentazioni mdoc, ciascuna DEVE essere trasportata in un ``DeviceResponse`` separato, allineato al corrispondente elemento della query DCQL. In tal caso, il valore di ``vp_token`` per quell'identificativo di Credenziale DEVE essere un array di valori ``DeviceResponse``.
  
  * - **state**
    - Identificatore univoco fornito dalla Relying Party all'interno della Authorization Request.

.. note::
    Sebbene `OpenID4VP`_ prenda in considerazione la bozza -10 della specifica SD-JWT VC, la specifica IT Wallet considera la bozza -13 (`SD-JWT-VC`_) in linea con la versione identificata in `OpenID4VCI`_.

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
    - OBBLIGATORIO. Il ricevitore previsto del Key Binding JWT. Il valore DEVE essere il Client Identifier (``client_id``) della Relying Party, incluso il prefisso del Client Identifier (``openid_federation`` o ``x509_hash``). Ad esempio, ``openid_federation:https://relying-party.example.org``.
  * - **nonce**
    - OBBLIGATORIO. Garantisce l'unicità della firma. Il valore di questa *claim* DEVE essere una stringa. Il valore DEVE corrispondere a quello fornito nel Request Object.
  * - **sd_hash**
    - OBBLIGATORIO. Il digest codificato in base64url del JWT firmato dal Fornitore di Attestati Elettronici (SD-JWT) e le *selective disclosures* selezionate dall'Utente.
  * - **transaction_data_hashes**  
    - OBBLIGATORIO quando la richiesta include ``transaction_data``. Array non vuoto di hash codificati in base64url. Ogni hash è calcolato sul valore esatto della stringa corrispondente all’elemento ``transaction_data``.
  * - **transaction_data_hashes_alg**
    - OBBLIGATORIO solo quando l’oggetto ``transaction_data`` corrispondente include ``transaction_data_hashes_alg``. Stringa che indica l’algoritmo di hash effettivamente utilizzato per calcolare ``transaction_data_hashes``. Se tale parametro non è stato fornito, la funzione di hash DEVE essere ``sha-256``.


Errori della Authorization Response
-----------------------------------

Ci sono casi in cui l'Istanza del Wallet non può convalidare il Request Object o il Request Object risulta non valido. Questo errore si verifica se il Request Object viene recuperato con successo dall'url fornito nel parametro ``request_uri`` ma non supera i controlli di convalida. Ciò potrebbe essere dovuto a firme errate, claim non conformim o altri errori di convalida, come la revoca della trust per la specifica Relying Party che lo ha emesso.

Se l'Istanza del Wallet incontra un errore durante la valutazione, DEVE inviare una *Authorization Error Response* solo dopo che il percorso di fiducia selezionato ha autenticato il ``response_uri`` applicabile.
Se la richiesta o l'endpoint non sono stati autenticati, l'Istanza del Wallet DEVE terminare in locale.
L'Istanza del Wallet DEVE informare l'Utente.
L'Istanza del Wallet NON DEVE rivelare la disponibilità del Wallet o della Credenziale (:ref:`WP_090 <wallet-credential-presentation-testcases>`).
Per un flusso di reindirizzamento autenticato, l'Istanza del Wallet invia la *Authorization Error Response* all'endpoint ``response_uri`` della Relying Party con una richiesta HTTP POST.
La risposta di errore PUÒ non essere cifrata solo dove `OpenID4VP`_ lo consente (:ref:`WP_090 <wallet-credential-presentation-testcases>`).
Questa *Error Response* DEVE essere codificata nel corpo della richiesta utilizzando il formato definito dal tipo di contenuto ``application/x-www-form-urlencoded``.

Di seguito è riportato un esempio non normativo di una *Error Response* nella *Authorization Response*.

.. literalinclude:: ../../examples/shared/remote-flow-12.http
   :language: http

.. warning::
  Un errore di un percorso di fiducia è gestito come specificato in :ref:`trust-evaluation:Failure Handling`.

Nella seguente tabella sono elencati gli *Error codes* e le descrizioni che sono supportati per la *Error Response* nella *Authorization Response*:

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
   * - ``invalid_transaction_data``  
     - Uno o più oggetti nella struttura ``transaction_data`` non sono validi. Ad esempio, tali oggetti contengono tipi sconosciuti o non supportati, campi malformati (ad esempio è un oggetto di tipo noto ma contiene campi sconosciuti o campi di tipo errato per il tipo di transaction data) o mancanti, valori non validi (ad esempio il campo ``credential_ids`` non corrisponde) oppure riferimenti a Credenziali non disponibili. `OpenID4VP`_

Risposta della Relying Party
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Come definito nella Sezione 8.2. (*Response mode* "direct_post") della specifica `OpenID4VP`_, se l'Endpoint di Risposta della Relaying Party ha elaborato con successo la *Authorization Response* o la *Error Response* fornita dall'Istanza del Wallet, DEVE rispondere con un codice di stato HTTP 200 con ``Content-Type`` di ``application/json`` e un JSON Object nel corpo della risposta.

Nel **Flusso Same Device** basato su reindirizzamento, la Relying Party DEVE aggiungere il parametro ``redirect_uri`` all'oggetto JSON nel corpo della risposta. Dopo aver ricevuto il ``redirect_uri``, l'Istanza del Wallet DEVE eseguire un reindirizzamento all'URL specificato dal ``redirect_uri``. La Relying Party DEVE rifiutare un ``redirect_uri`` assente. La Relying Party DEVE rifiutare un ritorno in una sessione utente iniziale diversa.
Questo reindirizzamento consente alla Relying Party di riprendere l'interazione con l'Utente sul dispositivo che ha avviato il flusso, dopo che l'Istanza del Wallet ha trasmesso la Authorization Response al ``response_uri`` designato.

La Relying Party DEVE includere un codice di risposta all'interno del ``redirect_uri``. Il codice di risposta è un numero fresco, crittograficamente casuale utilizzato per garantire che solo il ricevitore del reindirizzamento possa recuperare ed elaborare la Authorization Response. Il numero potrebbe essere aggiunto come componente del path, come parametro o come frammento all'URL. È RACCOMANDATO utilizzare un valore casuale crittografico di 128 bit o più al momento della scrittura di questa specifica.
Anche se un avversario riesce a rubare il valore casuale utilizzato nella richiesta allo Status Endpoint, il suo user-agent verrebbe rifiutato a causa del cookie mancante nella richiesta.

.. warning::
  Il parametro ``redirect_uri`` è soggetto a :ref:`endpoint-mix-up-protection` (:ref:`WP_094a <wallet-credential-presentation-testcases>`).

Errori della Risposta della Relying Party
-----------------------------------------

Se qualsiasi controllo di convalida, eseguito dalla Relying Party sulla Authorization Response dall'Istanza del Wallet, fallisce, l'endpoint URI di Risposta DEVE restituire una *Error Response*. La struttura di questa *Error Response* dipende dalla natura specifica dell'errore incontrato. La risposta DEVE utilizzare ``application/json`` come tipo di contenuto.
La risposta DEVE includere i seguenti parametri:

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

.. literalinclude:: ../../examples/shared/remote-flow-13.http
   :language: http


.. literalinclude:: ../../examples/shared/remote-flow-14.http
   :language: http


Status Endpoint
^^^^^^^^^^^^^^^

Questa specifica introduce lo Status Endpoint della Relying Party per le implementazioni che scelgono di utilizzarlo. Questo Endpoint è una funzionalità di sicurezza interna dell'implementazione e non è richiesto per l'interoperabilità.

Quando la Relying Party espone lo Status Endpoint, il controllo della sessione PUÒ essere implementato sotto forma di codice JavaScript, all'interno della pagina che mostra il Codice QR o il pulsante href che punta all'URL di richiesta.
Il codice JavaScript fa sì che l'user-agent controlli lo Status Endpoint utilizzando una strategia di polling (in secondi) o una strategia push (ad esempio, WebSocket).

Poiché la pagina HTML e lo Status Endpoint sono implementati dalla Relying Party, i dettagli di implementazione di questa soluzione sono responsabilità della Relying Party, in quanto sono relativi alle API interne della Relying Party. Tuttavia, il testo seguente descrive un'implementazione di esempio.

La Relying Party lega la richiesta dello user-agent, con un cookie di sessione contrassegnato come ``Secure`` e ``HttpOnly``, con la richiesta emessa. L'URL
della richiesta DOVREBBE includere un parametro con un valore casuale. La risposta HTTP restituita da questo endpoint di stato PUÒ contenere gli Status Code HTTP elencati di seguito:

* **201 Created**. Quando il Request Object firmato è stato emesso dalla Relying Party che attende di essere scaricato dall'Istanza del Wallet all'endpoint ``request_uri``.
* **202 Accepted**. Quando il Request Object firmato è stato ottenuto dall'Istanza del Wallet.
* **200 OK**. Quando l'Istanza del Wallet ha fornito la presentazione all'endpoint ``response_uri`` della Relying Party e l'autenticazione dell'Utente ha avuto successo. La Relying Party aggiorna il cookie di sessione consentendo allo user-agent di accedere alla risorsa protetta. Viene fornito un ``redirect_uri`` che trasporta lo user-agent alla pagina in cui l'Utente deve navigare.

Errori dello Status Endpoint
----------------------------

Se invece qualsiasi controllo di convalida eseguito dalla Relying Party fallisce, la pagina del Codice QR DOVREBBE essere aggiornata con un messaggio di errore. Inoltre, lo Status Endpoint DEVE restituire una *Error Response*, la cui struttura dipende dalla natura dell'errore. La risposta DEVE utilizzare ``application/json`` come tipo di contenuto.
La risposta DEVE includere i seguenti parametri:

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
^^^^^^^^^^^^^^^^^^^^^^^
Il valore ``redirect_uri`` DEVE essere utilizzato con un metodo HTTP GET dall'user-agent per reindirizzare l'Utente a un endpoint specifico della Relying Party al fine di completare il processo.


Errori dell'URI di Reindirizzamento
-----------------------------------

Quando l'user-agent viene reindirizzato all'URI di Reindirizzamento fornito dalla Relying Party, possono verificarsi diversi errori che impediscono il completamento con successo del processo. Questi errori sono critici in quanto influenzano direttamente l'esperienza dell'Utente ostacolando il flusso fluido di informazioni tra l'Istanza del Wallet e la Relying Party. La gestione di questi errori richiede una comunicazione chiara all'Utente all'interno della pagina web di navigazione restituita. La Relying Party DEVE implementare i meccanismi di gestione degli errori e di convalida per gli URI di Reindirizzamento definiti in questa specifica. Di seguito sono riportati potenziali errori relativi all'URI di Reindirizzamento. La *Error Response* DEVE utilizzare ``application/json`` come tipo di contenuto.
La risposta DEVE includere i seguenti parametri:

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



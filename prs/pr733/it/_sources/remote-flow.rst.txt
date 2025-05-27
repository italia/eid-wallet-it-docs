.. include:: ../common/common_definitions.rst


Flusso Remoto
=============

A seconda che l'Utente stia utilizzando un dispositivo mobile o una workstation, la Relying Party DEVE supportare i seguenti flussi remoti:

* **Stesso Dispositivo**, la Relying Party DEVE fornire una posizione HTTP all'Istanza del Wallet utilizzando un reindirizzamento (302) o un href HTML in una pagina web;
* **Dispositivo Diverso**, la Relying Party DEVE fornire un Codice QR che l'Utente inquadra con l'Istanza del Wallet.

Una volta che l'Istanza del Wallet stabilisce la fiducia con la Relying Party e valuta la richiesta, l'Utente fornisce il consenso per la divulgazione delle Credenziali Elettroniche, sotto forma di Presentazione Verificabile.

.. _fig_High-Level-Flow-Presentation:
.. plantuml:: plantuml/credential-presentation-remote-high-level-flow.puml
    :width: 99%
    :alt: La figura illustra il Flusso di Protocollo Remoto di Alto Livello.
    :caption: `Flusso di Protocollo Remoto di Alto Livello. <https://www.plantuml.com/plantuml/svg/TL9TQ-em6BxFhtZmvXmBvvJpVV1YECHjmi2kKxmPIDU-sCoOP4bgSRz-YLNNAhjids_U3AtBZAis0dTyLUAUjYIGqaOvGcAKKxaIk16gPjhpUCvr9XrwYqm8SfX8BvSvzP1Pd55I4ZikLqZypzsUO3HZHkFR5Ue1Vdn755rNhbI6lsMEA-bZNokoBehmjOPfFfQLuNsuqgZArpDKS4EvWp9uI96hWc3pJE99EkLPX3Xkgdsnw9gFPQ4LbowE6Qj31wC7-1bA768nJoVj2hVZMOX9fe-pFaxkQUATsugsxsdShqjVgvMqr6mx8jFd5p-cprXzqFqEkiK4evBojVNa3-XFWEQM34R1I3gFjfRy3N3eUZQx6xpLIwVM92y7DQnF5eM0V_j9IRlQQUx_W7NktSbLEbJ9XDYXFfwmEImRaYpyuti7>`_


.. .. figure:: ../../images/High-Level-Flow-Presentation.svg
..     :figwidth: 100%
..     :align: center
..     :target: https://www.plantuml.com/plantuml/svg/TL9TJy8m57tlhpZXHLcYYz-61uCXnF34d11UJCZS6bQPRMtlRF3NspB0JUBJidlEFH-v7LhA3DKV5TF-AtAXCqdeBRAgueI9zB3CUG-PXUjIKbvjX5mXySFDbc0qOqRZx05kW8jpHD5ZJQKouZiZeIHI_bbpIr64KmVJ_2nh8_gWqgXwLVfX8GpF2ShWEKMk2WwRPnAlafHdSSHn4-t4eYi-beLMGb8SC-P21gC7k0mXThQOfvDsXAVnBDWaqvTP7mVrDF7AxOssxg7SrR6krKfQtdJR8zEtTr-cpvZRxLs7lSK4evBdQ-l9lz1DWEQM6uo2a2IFjfhS1ZXa_LExQ_obbwJMN1uNQbZ_D0e6TzjAIJlQeUvzm3htxlWg7QBuispWzYTi3ilOaCl2lwuV

..     High Level Remote Protocol Flow


Una descrizione di alto livello del flusso remoto, dal punto di vista dell'Utente, è fornita di seguito e mostrata in :ref:`fig_High-Level-Flow-Presentation`:

  1. *Richiesta di Autorizzazione*: l'Istanza del Wallet ottiene un URL nel flusso Stesso Dispositivo o un Codice QR contenente l'URL nel flusso Dispositivo Diverso dove l'oggetto di richiesta firmato è disponibile per il download.
  2. *Richiesta URI Request*: l'Istanza del Wallet estrae dal payload i seguenti parametri: ``client_id``, ``request_uri``, ``state``, ``request_uri_method``.

    * Se ``request_uri_method`` è fornito e impostato con il valore ``post``, l'Istanza del Wallet DOVREBBE trasmettere i suoi metadati all'endpoint ``request_uri`` della Relying Party utilizzando il metodo HTTP POST.
    * Se ``request_uri_method`` è impostato con il valore ``get`` o non è presente, l'Istanza del Wallet DEVE recuperare l'Oggetto di Richiesta firmato utilizzando una richiesta HTTP con metodo GET all'endpoint fornito nel parametro ``request_uri``.

  3. *Risposta URI Request*: la Relying Party restituisce un Oggetto di Richiesta firmato all'Istanza del Wallet.
  4. *Controlli WI*: l'Istanza del Wallet:

    a. verifica la firma dell'Oggetto di Richiesta firmato utilizzando la chiave pubblica identificata nell'intestazione JWT dell'Oggetto di Richiesta. Utilizzando tale riferimento, l'Istanza del Wallet è in grado di selezionare la corretta chiave pubblica della Relying Party per la verifica della firma.
    b. verifica che il ``client_id`` contenuto nell'emittente dell'Oggetto di Richiesta (Relying Party) corrisponda a quello ottenuto al passaggio numero 2 e al parametro ``sub`` contenuto nella Configurazione dell'Entità della Relying Party all'interno della Catena di Fiducia.
    c. valuta le Credenziali Elettroniche richieste e verifica l'idoneità della Relying Party nel richiedere queste applicando le politiche relative a quella specifica Relying Party, ottenute con la Catena di Fiducia.

  5. *Consenso dell'Utente*: l'Istanza del Wallet chiede la divulgazione e il consenso dell'Utente mostrando l'identità della Relying Party e gli attributi richiesti.
  6. *Risposta di Autorizzazione POST*: l'Istanza del Wallet presenta le informazioni richieste alla Relying Party, insieme all'Attestato di Wallet se richiesto.
  7. *Controlli RP*: La Relying Party convalida le Credenziali presentate verificando la fiducia con i loro Fornitori di Credenziale e controlla l'Attestato di Wallet per garantire che il Fornitore di Wallet sia affidabile.
  8. *Risposta della Relying Party*: l'Istanza del Wallet informa l'Utente dell'autenticazione riuscita con la Relying Party, e l'Utente continua la navigazione.

Di seguito è riportato un diagramma di sequenza che dettaglia le interazioni tra tutte le parti coinvolte.

.. plantuml:: plantuml/credential-presentation-remote-flow.puml
    :width: 99%
    :alt: La figura illustra il Flusso di Protocollo Remoto.
    :caption: `Flusso di Protocollo Remoto. <https://www.plantuml.com/plantuml/svg/fLPFRnkt4xtpKmpqE_ni87QJ7WsuYACwjXEtLYqbFjI5G7574kiLkIM7gwX5ldk7v6hDjHqWG0rVTfVptfitVwYtdgIZiAdXscwFhh756cvnOmbXuYnPPMjuNzkja86i2Pi5EY74cIBhOFJ9enk1z124MDWl-SN_FVoChLReH_2_QxrQqxiwe6YOHYlTI4CmkfDrZGHNXjcDmeIn7Hu937KaLsWeCqY1fW9cwQXkiTvfiu891-s-oJGyTcyERiu2hM5SQmO-JCZjamYMHC43ipLMT-mUUtR-aufqAmaXY017Fx6s4xZ31KpHnRp1o5Ql96bhYgDIL5W6oXZPuWcx_LT0JybkL8GLl_4sE8L2d9xoQ_IiDS71P2qzmkbfZnlLjxY76ZkCxoHuIjyast5l5ZQmThBmQ2aeQn_q2w4kYva7fy5b6UKfBbZ36aiasZNCmUWLHlcWdFMU7v8Jre6N6yoF6IZRjIRkk8OHOAkv7h_TZcsLZgyTBbaT9woDNW6j4OAhqwbxerBPvhfwLGfzbTDz1RyNB-SRfBMj_c3NIwz4PtmuWUdQRXD-9izgM06Jg8Vq8MbP129h1iMJZ_PlXLWv6nhsp_fzuuCrzKvi8y-MUPGqp05Cahf8nAR9dwwjaZN4eG4PcD6GLhbl-kZpMCJ8H2vuIZuaRRqLGiYQG2_XUVAWO-TsGPERwKm006ptnUI6QtM5q0qZnyXAaWIoYQ70wuSX0HH-fkU-FGgnwnwMK1aTqrIoaGjTQzBe1TOUlqFqnVaibiHOWYRFWKWP34SdqNczCbZj0S4k_epTk7Hsy-riKZLQxChnCiIp1dfMcS6AWL_sDafJGMEvcJJwFkWpEhtS9IP9mI7OPQ6-J-WcK_THijPLCPvyylFam1_c0-7HY6NiNskIKSCjbO76rYorss0rN4QzeR5986v8w_JVgHCPsZSH4UvDhadRpCa-eEd7hYasrDo7nKPx7tkujEtb7ibsQBceSRZd4a4VL1XGDDOP4Vfy_fZ5vSVoGDVVZeLh3t77xzr-Z_mwHV8thbCVLTn979Fwpc7BOghZGar7DNOCOqZB6gwy3-XW5cUqW-mbVxYRmNHVxmA5vIdqFazp3oM4OrO4swBZOtolNLrSpYvkpyz_5Iz7d0WuWl4QUMbTshhYi8-uWtVQLDoKIGh7SUByFx7UOoeE11-_WW18S4rOSAV20qVcwqARzBx8aIoqkNjJvIQvICSYqfz_8ITLTh_INjNMOmMIoEb58FH9XaeQzHBOw7ucDHD0dXU785kfwzWEnt4sanEYiEnJqpT1MfhxP0xoTGOXVQyEnNuhJ-K6zqivDI-pCQDAUw2O_ClPRFB3c-CtyEFhrt3paKlupwWyEeet5ZM-lul0TMCnLxP2-DfDecIDFWaSCfLt1oVsygNXdicrWRvJSJdFs-7Awcuyp_x11pPugfnkA5VZvCczaqOwZVf19EXNOKevctpuc8n7uREW8F-pXry5oowXir637qePR7z1DVqFflwNod3bzD8cpqyEB_GdZhrbwh2f_mK0>`_


.. .. figure:: ../../images/cross_same_device_auth_seq_diagram.svg
..     :figwidth: 100%
..     :align: center
..     :target: https://www.plantuml.com/plantuml/svg/fLPDRnit4BtpLmpKGst0TfCU3RY8uxgsaxHMBIK-r8L0SKSIwnMv9OTIr2B_lJEWbgPa1mXGtPRalFVuE1zw4qa7IijMwKJUfUKKWrBgt90FCFWOCGn0HqXAJVtdlF1zX9znPGt60NptmSuNzBPDg3h6iSPssX4CxdNR8i6DOtXdK31WlNiaCTIndgEZpA0LkWQOPKjrX-t6kZaCEMZpTQQTOm_kuFOyqG8kMil0Xu8Cgxq8baGf0hDrtcxP8nPs_cb3TgK98Qa4np-njbEunocCCCYzmUcLdMkotbL7jMgm3jGIkS9JkCE_4qQ2OV24Xh3XbUXJCAZKsHalOsIjMk1WkD0HuUoiu8hw5VPG5m5bJKCaBNkQxNXmKvzOEtbuiXICzu_sXT2GnKnIi12oZEgKF5Z76ciasdJCmUWDacoPu6Fa3t42V82ebvW_Cr2sQq7B5Zf6WBMb1Vn-T-4REGwBW3DMvqXRP-T02uGKMf1J3yx8iz74DaUrqADytIFuergSB94MllcpSbsyKblZqocC5duj-3svg145J68UPIDhcIOYxsgOf9_iNoir3pvrx9-FVUA3T-r6hOLdpJn6E-O08P4iKf8qUUk3Dxe5AHhGYHaTMPFpfaHVoYCA4uKKARibseeLIkcMmCxW-UN1IkPkWuQtex42_gtxn-I4Mza6OLkC7ACRJHh82qEDLuf10A3sKxvBUbHY5mMMq3WhrpIwqrFRMh8O5ROHlq7qrULOdiHvWYxNWIetg4f7wAATEsnwGF3JloGRPy4lltgR_1eYFtlz8iH-0Zr_cPqM0x_sDchNGESvcIp64lG9WvrjG9WqfO3WPvNwSg7RJ5sYT6kRgZpvvAVXGJpC1zAJ4JCVf7Z4gBqkbO4kl9lPiCHcjnaLGoL9G3ga3_QVt7BkC7Q220yklycgcv1_H5VAhgiwr2IcwTB6A3bSs_PoZcGxh9wskDldI0XAK6L0bLZdH1Zp-HCMbp-h0tr-1nPk8qYFxzt-1NbPIoJlQTUKg6ecIOpaNS0LYsbEAZMPIbfc8oMhMxY9CM60iTJe5h98VdS_Xb7_tXKAopCOOwxc0gLKO5O4lyB0ntYktLnTZw_kBYz_Koz7d2euXei5SjEwzct3OUzn0s-jQoGfHGh7-PdSVUXZP01nE4NP1IadWUlIb3CL7ZaoZmlhPBs-8tdM8zcRNswO7-b42VtbPmhQPFSR6qth8pQWYOAT9i8eCi28HYbwDhhKf6K2oFKI4FHAsrRIuKHgKvn0LLdsiUkJ83VD_Z87UPn1adri3bNVbKSoV79JpidBRCneIFf0LVdNu_7mXzSdh-77Lw_WzZq_uR-3-kX09XPriSmY2Dkoc1YP7L-sbQXPOym2TvYgsI4NUtbeX6ToVQ9lL5pNytglPUM95za_UCS6Zqom7UNNEDsRExcafTGFXA3lD_dAsUH3LR0ZgfW59Vs_FVoYH7O5dOtQ-QEKmVe1rPK_JEMVocxBATA6pq_k3VHTnzumTLgs_m40

..     Remote Protocol Flow


I dettagli di ogni passaggio mostrato nell'immagine precedente sono descritti di seguito.

**Passaggi 1-2**: L'Utente richiede di accedere a una risorsa protetta della Relying Party.

**Passaggi 3-5**: La Relying Party crea un valore di stato legato all'user-agent (ad esempio, utilizzando un cookie HTTP sicuro), l'Oggetto di Richiesta disponibile per il download nella posizione ``request_uri``. Quindi ispeziona l'user-agent per determinare se il flusso avviene sullo stesso dispositivo dell'user-agent.

**Passaggi 6-9 (Richiesta di Autorizzazione)**: La Relying Party fornisce all'user-agent una pagina JavaScript che ispeziona l'endpoint di stato e all'Istanza del Wallet un URL contenente la Richiesta di Autorizzazione.

  Nel **Flusso Dispositivo Diverso**, l'URI di Richiesta viene presentato come un Codice QR mostrato all'Utente. L'Utente scansiona il Codice QR utilizzando l'Istanza del Wallet e recupera un URL con i parametri ``client_id``, ``request_uri``, ``state`` e ``request_uri_method``.

  Di seguito è rappresentato un esempio non normativo di un Codice QR emesso dalla Relying Party.

.. only:: format_html

  .. figure:: ./images/svg/verifier_qr_code.svg
    :figwidth: 50%
    :align: center

.. only:: format_latex

  .. figure:: ./images/pdf/verifier_qr_code.pdf
    :width: 50%
    :align: center


  Di seguito è rappresentato un esempio non normativo del payload grezzo del Codice QR:

.. code-block:: text

  https://wallet-solution.example.org/authorization?client_id=https%3A%2F%2Frelying-party.example.org&request_uri=https%3A%2F%2Frelying-party.example.org&request_uri_method=post

.. note::
  Il *livello di correzione degli errori* scelto per il Codice QR DEVE essere Q (Quartile - fino al 25%), poiché offre un buon equilibrio tra capacità di correzione degli errori e densità/spazio dei dati. Questo livello di qualità e correzione degli errori consente al Codice QR di rimanere leggibile anche se è danneggiato o parzialmente oscurato.

Al contrario, nel **Flusso Stesso Dispositivo**, la Relying Party utilizza un reindirizzamento di risposta HTTP (con codice di stato impostato a 302) o una pagina html con un pulsante href, contenente l'URL che fornisce le stesse informazioni del Flusso Dispositivo Diverso. Di seguito è riportato un esempio non normativo:

.. code-block:: http

  HTTP/1.1 302 Found
  Location: https://wallet-solution.digital-strategy.europa.eu?client_id=https%3A%2F%2Frelying-party.example.org%2Fcb&request_uri=https%3A%2F%2Frelying-party.example.org%2Frequest_uri&request_uri_method=post


**Passaggio 10**: L'Istanza del Wallet valuta la fiducia con la Relying Party.

**Passaggi 11-13 (Richiesta URI Request)**: L'Istanza del Wallet verifica se la Relying Party ha fornito il ``request_uri_method`` all'interno del suo Oggetto di Richiesta firmato.

  - Se è fornito ed è uguale a ``post``, l'Istanza del Wallet DOVREBBE fornire i suoi metadati alla Relying Party. La Relying Party aggiorna l'Oggetto di Richiesta in base alle capacità tecniche del Wallet.

    Di seguito è riportato un esempio non normativo di una richiesta HTTP effettuata dall'Istanza del Wallet alla Relying Party.
    
    .. code-block:: http
    
      POST /request HTTP/1.1
      Host: client.example.org
      Content-Type: application/x-www-form-urlencoded
      Accept: application/oauth-authz-req+jwt
    
      wallet_metadata=%7B%22authorization_endpoint%22%3A%20%22eudiw%3A%22%2C%20%22response_types_supported%22%3A%20%5B%22vp_token%22%5D%2C%20%22response_modes_supported%22%3A%20%5B%22form_post.jwt%22%5D%2C%20%22vp_formats_supported%22%3A%20%7B%22dc%2Bsd-jwt%22%3A%20%7B%22sd-jwt_alg_values%22%3A%20%5B%22ES256%22%2C%20%22ES384%22%5D%7D%7D%2C%20%22request_object_signing_alg_values_supported%22%3A%20%5B%22ES256%22%5D%7D%2C&wallet_nonce=%22qPmxiNFCR3QTm19POc8u%22
    
    Dove il corpo della richiesta prima di essere codificato in `application/x-www-form-urlencoded` dal Wallet corrisponde a:
    
    .. code:: json
    
      {
        "wallet_metadata": {
          "authorization_endpoint": "https://wallet-solution.digital-strategy.europa.eu/authorization",
          "response_types_supported": [
            "vp_token"
          ],
          "response_modes_supported": [
            "form_post.jwt"
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
          "client_id_schemes_supported": ["https"],
        },
        "wallet_nonce": "qPmxiNFCR3QTm19POc8u"
      }

  - Quando la scoperta delle capacità dell'Istanza del Wallet non è supportata dalla Relying Party, l'Istanza del Wallet richiede l'Oggetto di Richiesta firmato utilizzando il metodo HTTP GET.

**Passaggio 14 (Risposta URI Request)**: La Relying Party emette l'Oggetto di Richiesta firmandolo utilizzando una delle sue chiavi private crittografiche, le cui parti pubbliche sono state pubblicate all'interno della sua Configurazione dell'Entità (`metadata.openid_credential_verifier.jwks`). L'Istanza del Wallet ottiene l'Oggetto di Richiesta firmato.

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
      ]
    }
  
  .. code-block:: json
  
    {
      "client_id": "https://relying-party.example.org",
      "response_mode": "direct_post.jwt",
      "response_type": "vp_token",
      "dcql_query": {
        "credentials": [
          {
            "id": "personal id data",
            "format": "dc+sd-jwt",
            "meta": {
              "vct_values": [ "https://trust-registry.eid-wallet.example.it/credentials/v1.0/personidentificationdata" ]
            },
            "claims": [
              {"path": ["given_name"]},
              {"path": ["family_name"]},
              {"path": ["personal_administrative_number"]}
            ]
          },
          {
            "id": "wallet attestation",
            "format": "dc+sd-jwt",
            "meta": {
              "vct_values": ["https://itwallet.registry.example.it/WalletAttestation"]
            },
            "claims": [
              {"path": ["wallet_link"]},
              {"path": ["wallet_name"]}
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
      "exp": 1672422065,
      "request_uri_method": "post"
    }
  
**Passaggi 15-17 (Controlli WI)**: L'Istanza del Wallet verifica l'Oggetto di Richiesta, che è sotto forma di JWT firmato. Quindi elabora i metadati della Relying Party e applica le politiche pertinenti per determinare quali Credenziali Elettroniche e dati dell'Utente la Relying Party è autorizzata a richiedere.

**Passaggi 18-19 (Consenso dell'Utente)**: L'Istanza del Wallet richiede il consenso dell'Utente per divulgare le Credenziali richieste mostrando l'identità della Relying Party e gli attributi richiesti. L'Utente autorizza e acconsente alla presentazione delle Credenziali selezionando/deselezionando i dati personali da rilasciare.

**Passaggio 20 (Risposta di Autorizzazione)**: L'Istanza del Wallet fornisce la Risposta di Autorizzazione alla Relying Party utilizzando una richiesta HTTP con il metodo POST (modalità di risposta "direct_post.jwt").

  Di seguito è riportato un esempio non normativo della Risposta di Autorizzazione:

  .. code-block:: http
  
      POST /response_uri HTTP/1.1
      HOST: relying-party.example.org
      Content-Type: application/x-www-form-urlencoded
  
      response=eyJhbGciOiJFUzI1NiIs...9t2LQ
  
  Di seguito è riportato un esempio non normativo del payload decifrato del JWT contenuto nel parametro ``response``, prima della codifica base64url. Il valore del parametro ``vp_token`` corrisponde al formato utilizzato quando il linguaggio di query DCQL viene utilizzato nella richiesta di presentazione.
  
  .. code-block:: json
  
      {
        "state": "3be39b69-6ac1-41aa-921b-3e6c07ddcb03",
        "vp_token": {
          "personal id data": "eyJhbGciOiJFUzI1NiIs...PT0iXX0",
          "wallet attestation": "eyJhbGciOiJFUzI1NiIs...NTi0XG"
        }
      }

**Passaggi 21-25 (Controlli RP)**: La Relying Party verifica la Risposta di Autorizzazione, estrae l'Attestato di Wallet per stabilire la fiducia con la Soluzione Wallet. Quindi estrae le Credenziali Elettroniche e attesta la fiducia con il Fornitore di Credenziale e la prova di possesso dell'Istanza del Wallet delle Credenziali Elettroniche presentate. Infine, la Relying Party verifica lo stato di revoca delle Credenziali Elettroniche presentate come descritto in :ref:`credential-revocation:Revoca e Sospensione delle Credenziali`. Se tutte le verifiche precedenti hanno dato esito positivo, la Relying Party aggiorna la sessione dell'Utente.

**Passaggi 26-27 o 28 (Risposta della Relying Party)**: La Relying Party fornisce all'Istanza del Wallet la risposta sulla presentazione, che informa l'Utente.

  Dopo aver ricevuto e convalidato la Risposta di Autorizzazione all'Endpoint di Risposta, la Relying Party restituisce all'Istanza del Wallet un HTTP 200 OK. In particolare, nel Flusso Stesso Dispositivo, la Relying Party DOVREBBE anche passare il ``redirect_uri`` all'Istanza del Wallet. Dopo aver ricevuto il ``redirect_uri``, l'Istanza del Wallet DEVE eseguire un reindirizzamento all'URL specificato dal ``redirect_uri``. Questo reindirizzamento consente alla Relying Party di riprendere senza problemi l'interazione con l'Utente sul dispositivo che ha avviato il flusso. Quando la risposta non contiene il parametro ``redirect_uri``, l'Istanza del Wallet non è tenuta a eseguire ulteriori passaggi. L'Utente dovrebbe chiudere manualmente l'Istanza del Wallet e aprire l'user-agent per continuare il flusso.

  Di seguito è riportato un esempio non normativo della risposta nel Flusso Stesso Dispositivo.

.. code-block:: http

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
      "redirect_uri": "https://relying-party.example.org/cb?response_code=091535f699ea575c7937fa5f0f454aee"
    }

**Passaggi 29-30**: La pagina JavaScript sta ispezionando l'endpoint di stato.

  Di seguito è riportato un esempio non normativo della Richiesta HTTP all'endpoint di stato, dove il parametro ``id`` contiene un valore opaco e casuale:

  .. code-block:: http

      GET /session-state?id=3be39b69-6ac1-41aa-921b-3e6c07ddcb03 HTTP/1.1
      HOST: relying-party.example.org

  Quando l'Istanza del Wallet ha fornito la presentazione all'endpoint **response_uri** della Relying Party e l'autenticazione dell'Utente ha avuto successo. La Relying Party aggiorna il cookie di sessione consentendo all'user-agent di accedere alla risorsa protetta. Viene fornito un URL di reindirizzamento che trasporta la posizione in cui l'user-agent deve navigare.
  Di seguito è riportato un esempio non normativo della risposta con il ``redirect_uri`` dalla Relying Party all'user-agent.
  
  .. code-block:: http
  
      HTTP/1.1 200 OK
      Content-Type: application/json
  
      {
        "redirect_uri": "https://relying-party.example.org/cb?response_code=091535f699ea575c7937fa5f0f454aee"
      }

**Passaggi 31-32**: L'user-agent viene reindirizzato all'URI di reindirizzamento per continuare la navigazione con la risorsa protetta resa disponibile all'Utente.



Richiesta di Autorizzazione
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

I parametri URL contenuti nella Richiesta di Autorizzazione della Relying Party, che includono il ``request_uri`` dove l'Oggetto di Richiesta firmato può essere scaricato, sono descritti nella tabella seguente.

.. list-table::
  :class: longtable
  :widths: 25 50
  :header-rows: 1

  * - **Nome**
    - **Descrizione**
  * - **client_id**
    - OBBLIGATORIO. Identificatore univoco della Relying Party.
  * - **request_uri**
    - OBBLIGATORIO. L'URL HTTP dove la Relying Party fornisce l'Oggetto di Richiesta firmato all'Istanza del Wallet.
  * - **state**
    - RACCOMANDATO. Un identificatore univoco per la transazione corrente generato dalla Relying Party. Il valore DOVREBBE essere opaco per l'Istanza del Wallet.
  * - **request_uri_method**
    - OPZIONALE. Il metodo HTTP DEVE essere impostato con ``get`` o ``post``. L'Istanza del Wallet dovrebbe utilizzare questo metodo per ottenere l'Oggetto di Richiesta firmato dal ``request_uri``. Se non fornito o uguale a ``get``, l'Istanza del Wallet DOVREBBE utilizzare il metodo HTTP ``get``. Altrimenti, l'Istanza del Wallet DOVREBBE fornire i suoi metadati all'interno del corpo HTTP POST codificato in ``application/x-www-form-urlencoded``.

.. warning::
  Per motivi di sicurezza e per prevenire attacchi di tipo endpoint mix-up, il valore contenuto nel parametro ``request_uri`` DEVE essere uno di quelli attestati da una terza parte fidata, come quelli forniti nei metadati ``openid_credential_verifier`` all'interno del parametro ``request_uris``, ottenuti dalla Catena di Fiducia relativa alla Relying Party.

.. note::
  Il parametro ``state`` in una richiesta OAuth è opzionale, ma è altamente raccomandato. Viene utilizzato principalmente per prevenire attacchi Cross-Site Request Forgery (CSRF) includendo un valore unico e imprevedibile che la Relying Party può verificare al momento della ricezione della risposta. Inoltre, aiuta a mantenere lo stato tra la richiesta e la risposta, come le informazioni di sessione o altri dati di cui la Relying Party ha bisogno dopo il processo di autorizzazione.

Il valore corrispondente all'endpoint ``request_uri`` DOVREBBE essere randomizzato, secondo `RFC 9101, The OAuth 2.0 Authorization Framework: JWT-Secured Authorization Request (JAR) <https://www.rfc-editor.org/rfc/rfc9101.html#section-5.2.1>`_ Sezione 5.2.1.


Richiesta URI Request
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

La Relying Party DOVREBBE fornire il metodo POST con il suo endpoint ``request_uri`` consentendo all'Istanza del Wallet di informare la Relying Party sulle sue capacità tecniche.

Questa funzionalità può essere utile quando, ad esempio, l'Istanza del Wallet supporta un insieme ristretto di funzionalità, algoritmi supportati o un URL specifico per il suo ``authorization_endpoint``, e qualsiasi altra informazione che ritiene necessario fornire alla Relying Party per l'interoperabilità.

.. warning::
  L'Istanza del Wallet, quando fornisce le sue capacità tecniche alla
  Relying Party, NON DEVE includere alcuna informazione dell'Utente o altre informazioni
  esplicite riguardanti l'hardware utilizzato o le preferenze di utilizzo del suo Utente.

Se sia la Relying Party che l'Istanza del Wallet supportano il ``request_uri_method`` con HTTP POST, le capacità (metadati) dell'Istanza del Wallet DEVONO essere fornite utilizzando una richiesta HTTP all'endpoint `request_uri` della Relying Party, con il metodo POST e il tipo di contenuto impostato su `application/x-www-form-urlencoded`.
La richiesta e i suoi parametri sono definiti nella Sezione numero 5 (Richiesta di Autorizzazione) di `OpenID4VP`_. Di seguito sono riportati i dettagli normativi e i riferimenti sui parametri da utilizzare dall'Istanza del Wallet nella richiesta.

.. list-table:: Parametri dell'Endpoint URI Request
   :class: longtable
   :widths: 20 80
   :header-rows: 1

   * - Parametro
     - Descrizione
   * - `wallet_metadata`
     - OPZIONALE. Oggetto JSON con parametri di metadati. Vedi `OpenID4VP`_, Sezione 9.1 e la tabella seguente, "Parametri dei Metadati del Wallet".
   * - `wallet_nonce`
     - RACCOMANDATO. Stringa utilizzata dall'Istanza del Wallet per prevenire il replay delle risposte della Relying Party. Vedi `OpenID4VP`_, Sezione 9.


.. list-table:: Parametri dei Metadati del Wallet
   :class: longtable
   :widths: 20 80
   :header-rows: 1

   * - Parametro
     - Descrizione
   * - `vp_formats_supported`
     - OBBLIGATORIO. Oggetto con identificatori di formato delle Credenziali. Vedi `OpenID4VP`_ Appendice B.
   * - `alg_values_supported`
     - OPZIONALE. Array di suite crittografiche supportate. Vedi `OpenID4VP`_ Appendice B.
   * - `client_id_schemes_supported`
     - RACCOMANDATO. Array di schemi di Identificatore Client. Il valore predefinito è `entity_id`.
   * - `authorization_endpoint`
     - URL dell'endpoint del server di autorizzazione, vedi `OAUTH2`_. L'utilizzo di un link universale è preferibile per una sicurezza migliorata e supporto di fallback, gli schemi url personalizzati possono anche essere utilizzati se necessario.
   * - `response_types_supported`
     - OPZIONALE. Array JSON di valori "response_type" di OAuth 2.0. Se presente DEVE essere impostato su `vp_token`. Il valore predefinito è `vp_token`.
   * - `response_modes_supported`
     - OPZIONALE. Array JSON di valori "response_mode" di OAuth 2.0. Vedi `JARM`_.
   * - `request_object_signing_alg_values_supported`
     - OPZIONALE. Vedi OpenID Connect Discovery.

.. note::
  Il parametro ``wallet_nonce`` è RACCOMANDATO per le Istanze del Wallet che vogliono prevenire la replica delle loro richieste http alle Relying Party.
  Quando presente, la Relying Party DEVE valutarlo.

.. note::
  Per l'``authorization_endpoint`` l'uso di link universali è preferito rispetto agli schemi url personalizzati perché, quando configurati correttamente utilizzando Assetlinks JSON per Android e Apple App Site Association per iOS, forniscono una sicurezza migliorata riducendo il rischio di dirottamento degli URL.
  Inoltre, i link universali offrono meccanismi di fallback, consentendo al flusso di continuare senza problemi in un browser anche se l'Istanza del Wallet non è installata, garantendo un'esperienza Utente più fluida. Per garantire l'interoperabilità, il supporto degli schemi url personalizzati è anche RACCOMANDATO secondo il profilo di interoperabilità OpenID4VC High Assurance Interoperability Profile (HAIP) `OPENID4VC-HAIP`_, e in particolare utilizzando l'url personalizzato ``haip://``.


Risposta URI Request
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

La Relying Party emette l'Oggetto di Richiesta firmato utilizzando il tipo di contenuto impostato su ``application/oauth-authz-req+jwt``.

I parametri dell'intestazione JWT sono descritti di seguito:

.. list-table::
  :class: longtable
  :widths: 25 50
  :header-rows: 1

  * - **Nome**
    - **Descrizione**
  * - **alg**
    - Algoritmo utilizzato per firmare il JWT, secondo [:rfc:`7516#section-4.1.1`]. DEVE essere uno degli algoritmi supportati nella Sezione :ref:`algorithms:Algoritmi Crittografici` e NON DEVE essere impostato su ``none`` o su un identificatore di algoritmo simmetrico (MAC).
  * - **typ**
    - Tipo di Media del JWT, come definito in [:rfc:`7519`] e [:rfc:`9101`]. DOVREBBE essere impostato sul valore ``oauth-authz-req+jwt``.
  * - **kid**
    - ID della chiave della chiave pubblica necessaria per verificare la firma JWT, come definito in [:rfc:`7517`]. OBBLIGATORIO quando viene utilizzato ``trust_chain``.
  * - **trust_chain**
    - Sequenza di Entity Statement che compongono la Catena di Fiducia relativa alla Relying Party, come definito in `OID-FED`_ Sezione 4.3 *Trust Chain Header Parameter*.


I parametri del payload JWT sono descritti qui:

.. list-table::
  :class: longtable
  :widths: 25 50
  :header-rows: 1

  * - **Nome**
    - **Descrizione**
  * - **client_id**
    - Identificatore univoco della Relying Party.
  * - **response_mode**
    - DEVE essere impostato su ``direct_post.jwt``.
  * - **dcql_query**
    - Oggetto che rappresenta una richiesta di presentazione di Credenziali, secondo il linguaggio di query DCQL definito nella Sezione 6 di `OpenID4VP`_.
  * - **response_type**
    - DEVE essere impostato su ``vp_token``.
  * - **wallet_nonce**
    - Valore stringa utilizzato per mitigare gli attacchi di replay della risposta, come definito nella Sezione 5.11 (Request URI Method) di `OpenID4VP`_. DEVE essere presente se precedentemente fornito dall'Istanza del Wallet.
  * - **response_uri**
    - L'URI di Risposta a cui l'Istanza del Wallet DEVE inviare la Risposta di Autorizzazione utilizzando una richiesta HTTP con il metodo POST.
  * - **nonce**
    - Numero crittograficamente casuale fresco con sufficiente entropia, la cui lunghezza DEVE essere di almeno 32 cifre.
  * - **state**
    - Identificatore univoco della Richiesta di Autorizzazione.
  * - **iss**
    - L'entità che ha emesso il JWT. Sarà popolato con l'id client della Relying Party.
  * - **iat**
    - Timestamp Unix, che rappresenta l'ora in cui il JWT è stato emesso.
  * - **exp**
    - Timestamp Unix, che rappresenta l'ora di scadenza in cui o dopo la quale il JWT NON DEVE più essere valido.
  * - **request_uri_method**
    - Stringa che determina il metodo HTTP da utilizzare con l'endpoint `request_uri` per fornire i metadati dell'Istanza del Wallet alla Relying Party. Il valore non fa distinzione tra maiuscole e minuscole e può essere impostato su: `get` o `post`. Il metodo GET, come definito in [@RFC9101], prevede che l'Istanza del Wallet invii una richiesta GET per recuperare un Oggetto di Richiesta. Il metodo POST prevede che l'Istanza del Wallet richieda la creazione di un nuovo Oggetto di Richiesta inviando una richiesta HTTP POST, con i suoi metadati, all'URI di richiesta della Relying Party.

.. warning::
  Per motivi di sicurezza e per prevenire attacchi di tipo endpoint mix-up, il valore contenuto nel parametro ``response_uri`` DEVE essere uno di quelli attestati da una terza parte fidata, come quelli forniti nei metadati ``openid_credential_verifier`` all'interno del parametro ``response_uris``, ottenuti dalla Catena di Fiducia relativa alla Relying Party.

.. note::
  I seguenti parametri, anche se definiti in [OID4VP], non sono menzionati nel precedente esempio non normativo, poiché il loro utilizzo è condizionale e potrebbe cambiare in future versioni di questa documentazione.

  - ``presentation_definition``: Oggetto JSON secondo `Presentation Exchange <https://identity.foundation/presentation-exchange/spec/v2.0.0/>`_. Questo parametro NON DEVE essere presente quando ``presentation_definition_uri`` o ``scope`` sono presenti.
  - ``presentation_definition_uri``: Non supportato. Stringa contenente un URL HTTPS che punta a una risorsa dove può essere recuperato un oggetto JSON Presentation Definition. Questo parametro DEVE essere presente quando il parametro ``presentation_definition`` o un valore ``scope`` che rappresenta una Presentation Definition non è presente.
  - ``client_metadata``: Un oggetto JSON contenente i valori dei metadati della Relying Party. Se il parametro ``client_metadata`` è presente, l'Istanza del Wallet DEVE ignorarlo e considerare i metadati del client ottenuti attraverso la Catena di Fiducia OpenID Federation.


Errori dell'Endpoint URI Request
--------------------------------

Quando la Relying Party incontra errori durante l'emissione dell'Oggetto di Richiesta dall'endpoint ``request_uri``, DEVE restituire una risposta di errore con ``application/json`` come tipo di contenuto e DEVE includere i seguenti parametri:

* ``error``: Il codice di errore.
* ``error_description``: Testo in forma leggibile dall'uomo che fornisce ulteriori dettagli per chiarire la natura dell'errore incontrato.

La seguente tabella elenca i Codici di Stato HTTP e i relativi codici di errore che DEVONO essere supportati per la risposta di errore:

.. list-table::
    :class: longtable
    :widths: 20 20 60
    :header-rows: 1

    * - **Codice di Stato**
      - **Codice di Errore**
      - **Descrizione**
    * - ``500 Internal Server Error``
      - ``server_error``
      - La richiesta non può essere soddisfatta perché l'Endpoint URI Request ha incontrato un problema interno. (:rfc:`6749#section-4.1.2.1`).
    * - ``503 Service Unavailable``
      - ``temporarily_unavailable``
      - La richiesta non può essere soddisfatta perché l'Endpoint URI Request è temporaneamente non disponibile (ad esempio, a causa di manutenzione o sovraccarico). (:rfc:`6749#section-4.1.2.1`).


Di seguito è riportato un esempio di risposta di errore dall'endpoint ``request_uri``:

.. code-block:: http

  HTTP/1.1 500 Internal Server Error
  Content-Type: application/json

  {
    "error": "server_error",
    "error_description": "The Request Object cannot be retrieved due to an internal server error."
  }

Dopo aver ricevuto una risposta di errore, l'Istanza del Wallet DOVREBBE informare l'Utente della condizione di errore in modo appropriato. L'Istanza del Wallet DOVREBBE registrare l'errore e PUÒ tentare di recuperare da determinati errori se fattibile. Ad esempio, se l'errore è ``server_error``, l'Istanza del Wallet DOVREBBE chiedere all'Utente di reinserire o scansionare un nuovo codice QR, se applicabile.



Risposta di Autorizzazione
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Dopo aver ottenuto l'autorizzazione e il consenso dell'Utente per la presentazione delle Credenziali Elettroniche, l'Istanza del Wallet invia la Risposta di Autorizzazione all'endpoint ``response_uri`` della Relying Party utilizzando una richiesta HTTP con il metodo POST, il contenuto DOVREBBE essere crittografato secondo `OpenID4VP`_ Sezione 7.3, utilizzando la chiave pubblica della Relying Party.

.. note::
    **Perché la risposta è crittografata?**

    La risposta inviata dall'Istanza del Wallet alla Relying Party è crittografata per impedire a un agente malevolo di accedere alle informazioni in chiaro trasmesse all'interno della rete della Relying Party. Questo è possibile solo se l'ambiente di rete della Relying Party impiega la `terminazione TLS <https://www.f5.com/glossary/ssl-termination>`_. Tale tecnica impiega un proxy di terminazione che agisce come intermediario tra il client e il webserver e gestisce tutte le operazioni relative a TLS. In questo modo, il proxy decifra il contenuto della trasmissione e lo inoltra in chiaro o negozia una sessione TLS interna con il target previsto del webserver effettivo. Nel primo scenario, qualsiasi attore malevolo all'interno del segmento di rete potrebbe intercettare i dati trasmessi e ottenere informazioni sensibili, come una risposta non crittografata, sniffando i dati trasmessi.


Dove vengono utilizzati i seguenti parametri:

.. list-table::
  :class: longtable
  :widths: 25 50
  :header-rows: 1

  * - **Nome**
    - **Descrizione**
  * - **vp_token**
    - Ci DEVONO essere almeno due presentazioni firmate in questo Array:

      - La Credenziale Elettronica richiesta (una o più, in formato SD-JWT VC)
      - L'Attestato di Wallet (in formato SD-JWT VC)

      Quando viene utilizzato `presentation_definition`, il valore ``vp_token`` è un Array JSON contenente la/e Presentazione/i Verificabile/i e il parametro `presentation_submission` DEVE essere presente anche all'interno della risposta.

      Quando viene utilizzato il linguaggio di query DCQL, il formato ``vp_token`` è un Oggetto JSON le cui chiavi corrispondono agli id delle credenziali richieste nel ``dcql_query`` utilizzato nella richiesta, e i valori a ciascuna Credenziale Elettronica presentata.

  * - **state**
    - Identificatore univoco fornito dalla Relying Party all'interno della Richiesta di Autorizzazione.


SD-JWT definisce come un Titolare può presentare una Credenziale Elettronica a una Relying Party, dimostrando il legittimo possesso della Credenziale Elettronica. Per fare ciò, il Titolare DEVE includere il ``KB-JWT`` nell'SD-JWT aggiungendo il ``KB-JWT`` alla fine dell'SD-JWT, come rappresentato nell'esempio seguente

.. code-block:: text

  <Issuer-Signed-JWT>~<Disclosure 1>~<Disclosure 2>~...~<Disclosure N>~<KB-JWT>

Per convalidare la firma sul Key Binding JWT, la Relying Party DEVE utilizzare il materiale chiave incluso nell'Issuer-Signed-JWT. La convalida della firma del Key Binding JWT (KB-JWT) DEVE utilizzare la chiave pubblica inclusa nell'SD-JWT, utilizzando il parametro ``cnf`` contenuto nell'Issuer-Signed-JWT.

Quando viene presentato un SD-JWT, il suo KB-JWT DEVE contenere i seguenti parametri nell'intestazione JWT:

.. list-table::
  :class: longtable
  :widths: 25 50
  :header-rows: 1

  * - **Claim**
    - **Descrizione**
  * - **typ**
    - OBBLIGATORIO. DEVE essere ``kb+jwt``, che tipizza esplicitamente il Key Binding JWT come raccomandato nella Sezione 3.11 di [RFC8725].
  * - **alg**
    - OBBLIGATORIO. Algoritmo di Firma utilizzando uno di quelli specificati nella Sezione :ref:`algorithms:Algoritmi Crittografici`. 

Quando viene presentato un SD-JWT, la firma KB-JWT DEVE essere verificata dalla stessa chiave pubblica inclusa nell'SD-JWT all'interno del parametro `cnf`. Il KB-JWT DEVE contenere i seguenti parametri nel payload JWT:

.. list-table::
  :class: longtable
  :widths: 25 50
  :header-rows: 1

  * - **Claim**
    - **Descrizione**
  * - **iat**
    - OBBLIGATORIO. Il valore di questo claim DEVE essere l'ora in cui è stato emesso il Key Binding JWT, utilizzando la sintassi definita in [RFC7519].
  * - **aud**
    - OBBLIGATORIO. Il ricevitore previsto del Key Binding JWT. Il valore di questo parametro DEVE corrispondere all'identificatore di entità univoco della Relying Party.
  * - **nonce**
    - OBBLIGATORIO. Garantisce la freschezza della firma. Il tipo di valore di questo claim DEVE essere una stringa. Il valore DEVE corrispondere a quello fornito nell'oggetto di richiesta.
  * - **sd_hash**
    - OBBLIGATORIO. Il digest hash codificato in base64url sul JWT firmato dall'Emittente e le divulgazioni selezionate.


Errori della Risposta di Autorizzazione
---------------------------------------

Ci sono casi in cui l'Istanza del Wallet non può convalidare l'Oggetto di Richiesta o l'Oggetto di Richiesta risulta non valido. Questo errore si verifica se l'Oggetto di Richiesta viene recuperato con successo dall'url fornito nel parametro ``request_uri`` ma non supera i controlli di convalida. Ciò potrebbe essere dovuto a firme errate, claim malformati o altri errori di convalida, come la revoca della Relying Party.

Se l'Istanza del Wallet incontra tali errori durante la valutazione della Richiesta di Autorizzazione, DEVE notificare alla Relying Party inviando una Risposta di Errore di Autorizzazione.
L'Istanza del Wallet invia la Risposta di Errore di Autorizzazione all'endpoint ``response_uri`` della Relying Party utilizzando una richiesta HTTP POST.
La Risposta di Errore di Autorizzazione DEVE essere codificata nel corpo della richiesta utilizzando il formato definito dal tipo di contenuto ``application/x-www-form-urlencoded``.

Di seguito è riportato un esempio non normativo di una Risposta di Errore di Autorizzazione.

.. code-block:: http

  POST /response_uri HTTP/1.1
  HOST: relying-party.example.org
  Content-Type: application/x-www-form-urlencoded

  state=3be39b69-6ac1-41aa-921b-3e6c07ddcb03&
  error=invalid_request&
  error_description=...

.. warning::
  L'attuale specifica OpenID4VP delinea varie risposte di errore che un'Istanza del Wallet può restituire alla Relying Party (Verificatore) in caso di richieste errate. Per migliorare la privacy, le Istanze del Wallet NON DOVREBBERO notificare alla Relying Party le richieste errate in determinati scenari. Questo è per prevenire qualsiasi potenziale uso improprio delle risposte di errore che potrebbero portare a raccogliere informazioni che potrebbero essere sfruttate.

Nella seguente tabella sono elencati i codici di errore e le descrizioni che sono supportati per la Risposta di Errore di Autorizzazione:

.. list-table::
   :class: longtable
   :widths: 20 60
   :header-rows: 1

   * - **Codice di Errore**
     - **Descrizione**
   * - ``invalid_request_object``
     - L'Oggetto di Richiesta contiene parametri non validi o è altrimenti malformato. :rfc:`9101`
   * - ``invalid_request_uri``
     - Il `request_uri` nella richiesta di autorizzazione restituisce un errore, contiene dati non validi o è altrimenti malformato. :rfc:`9101`
   * - ``vp_formats_not_supported``
     - L'Istanza del Wallet non supporta nessuno dei formati vp richiesti dalla Relying Party. `OpenID4VP`_
   * - ``invalid_request``
     - L'Istanza del Wallet non supporta nessuno degli algoritmi di firma richiesti dalla Relying Party. `OpenID4VP`_
   * - ``access_denied``
     - Il Wallet non aveva la credenziale richiesta, l'Utente non ha dato il consenso o il Wallet non è riuscito ad autenticare l'Utente. `OpenID4VP`_
   * - ``invalid_client``
     - La Relying Party non può essere autorizzata a causa di errori di convalida della fiducia o non è un partecipante valido della federazione. `OID-FED`_


Risposta della Relying Party
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Come definito nella Sezione 7.2. (Modalità di Risposta "direct_post") della specifica `OpenID4VP`_, se l'URI di Risposta ha elaborato con successo la Risposta di Autorizzazione o la Risposta di Errore di Autorizzazione, DEVE rispondere con un codice di stato HTTP 200 con ``Content-Type`` di ``application/json`` e un oggetto JSON nel corpo della risposta.

Nel **Flusso Stesso Dispositivo**, la Relying Party DOVREBBE aggiungere il parametro ``redirect_uri`` all'oggetto JSON nel corpo della risposta. Dopo aver ricevuto il ``redirect_uri``, l'Istanza del Wallet DEVE eseguire un reindirizzamento all'URL specificato dal ``redirect_uri``.
Questo reindirizzamento consente alla Relying Party di riprendere senza problemi l'interazione con l'Utente sul dispositivo che ha avviato il flusso, dopo che l'Istanza del Wallet ha trasmesso la Risposta di Autorizzazione al ``response_uri`` designato.

La Relying Party DEVE includere un codice di risposta all'interno del ``redirect_uri``. Il codice di risposta è un numero fresco, crittograficamente casuale utilizzato per garantire che solo il ricevitore del reindirizzamento possa recuperare ed elaborare la Risposta di Autorizzazione. Il numero potrebbe essere aggiunto come componente del percorso, come parametro o come frammento all'URL. È RACCOMANDATO utilizzare un valore casuale crittografico di 128 bit o più al momento della scrittura di questa specifica.
Anche se un avversario riesce a rubare il valore casuale utilizzato nella richiesta all'endpoint di stato, il suo user-agent verrebbe rifiutato a causa del cookie mancante nella richiesta.

.. warning::
  Per motivi di sicurezza e per prevenire attacchi di tipo endpoint mix-up, il valore contenuto nel parametro ``redirect_uri`` DEVE essere uno di quelli attestati da una terza parte fidata, come quelli forniti nei metadati ``openid_credential_verifier`` all'interno del parametro ``redirect_uris``, ottenuti dalla Catena di Fiducia relativa alla Relying Party.

Errori della Risposta della Relying Party
-----------------------------------------

Se qualsiasi controllo di convalida, eseguito dalla Relying Party sulla Risposta di Autorizzazione dall'Istanza del Wallet, fallisce; l'endpoint URI di Risposta DEVE restituire una risposta di errore. La struttura di questa risposta di errore dovrebbe essere determinata dalla natura specifica dell'errore incontrato. La risposta DEVE utilizzare ``application/json`` come tipo di contenuto e DEVE includere i seguenti parametri:

* ``error``: Il codice di errore.
* ``error_description``: Testo in forma leggibile dall'uomo che fornisce ulteriori dettagli per chiarire la natura dell'errore incontrato.

La seguente tabella elenca i Codici di Stato HTTP e i relativi codici di errore che DEVONO essere supportati per la risposta di errore:

.. list-table::
    :class: longtable
    :widths: 20 20 60
    :header-rows: 1

    * - **Codice di Stato**
      - **Codice di Errore**
      - **Descrizione**
    * - ``400 Bad Request``
      - ``invalid_request``
      - La risposta non può essere elaborata perché mancano parametri obbligatori, contiene parametri non validi o è altrimenti malformata.
    * - ``400 Bad Request``
      - ``invalid_request``
      - Le Credenziali presentate sono malformate, non valide o revocate.
    * - ``400 Bad Request``
      - ``invalid_request``
      - La presentazione della credenziale, contenuta nell'oggetto ``vp_token``, è malformata, non ha i parametri richiesti o è formattata in modo errato.
    * - ``400 Bad Request``
      - ``invalid_request``
      - L'"sd-jwt" restituito è malformato, mancano parametri obbligatori o è formattato in modo errato.
    * - ``403 Forbidden``
      - ``invalid_request``
      - La firma del KB-JWT non è valida o non corrisponde alla chiave pubblica associata (JWK) referenziata nell'SD-JWT firmato dall'Emittente.
    * - ``403 Forbidden``
      - ``invalid_request``
      - Il valore del nonce fornito è errato o altrimenti malformato.
    * - ``403 Forbidden``
      - ``invalid_request``
      - La firma dell'Attestato di Wallet non è valida o la fiducia non può essere stabilita con il suo Emittente.
    * - ``403 Forbidden``
      - ``invalid_request``
      - La fiducia non può essere stabilita con il Fornitore di Credenziale.
    * - ``500 Internal Server Error``
      - ``server_error``
      - La richiesta non può essere soddisfatta perché l'Endpoint URI di Risposta ha incontrato un problema interno.
    * - ``503 Service Unavailable``
      - ``temporarily_unavailable``
      - La richiesta non può essere soddisfatta perché l'Endpoint URI di Risposta è temporaneamente non disponibile (ad esempio, a causa di manutenzione o sovraccarico).

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




Endpoint di Stato
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Questa specifica introduce l'Endpoint di Stato della Relying Party per le implementazioni che scelgono di utilizzarlo. Questo endpoint è una funzionalità di sicurezza interna dell'implementazione e non è richiesto per l'interoperabilità.

Sia che il flusso sia Stesso Dispositivo o Dispositivo Diverso, l'user-agent deve controllare lo stato della sessione all'endpoint reso disponibile dalla Relying Party (endpoint di stato).
Questo controllo PUÒ essere implementato sotto forma di codice JavaScript, all'interno della pagina che mostra il Codice QR o il pulsante href che punta all'URL di richiesta.
Il codice JavaScript fa sì che l'user-agent controlli l'endpoint di stato utilizzando una strategia di polling (in secondi) o una strategia push (ad esempio, WebSocket).

Poiché la pagina HTML e l'endpoint di stato sono implementati dalla Relying Party, i dettagli di implementazione di questa soluzione sono responsabilità della Relying Party, in quanto sono relativi all'API interna della Relying Party. Tuttavia, il testo seguente descrive un'implementazione di esempio.

La Relying Party lega la richiesta dell'user-agent, con un cookie di sessione contrassegnato come ``Secure`` e ``HttpOnly``, con la richiesta emessa.
L'URL della richiesta DOVREBBE includere un parametro con un valore casuale. La risposta HTTP restituita da questo endpoint di stato PUÒ contenere i codici di stato HTTP elencati di seguito:

* **201 Created**. L'Oggetto di Richiesta firmato è stato emesso dalla Relying Party che attende di essere scaricato dall'Istanza del Wallet all'endpoint ``request_uri``.
* **202 Accepted**. Questa risposta viene data quando l'Oggetto di Richiesta firmato è stato ottenuto dall'Istanza del Wallet.
* **200 OK**. L'Istanza del Wallet ha fornito la presentazione all'endpoint ``response_uri`` della Relying Party e l'autenticazione dell'Utente ha avuto successo. La Relying Party aggiorna il cookie di sessione consentendo all'user-agent di accedere alla risorsa protetta. Viene fornito un URL di reindirizzamento che trasporta la posizione in cui l'user-agent deve navigare.

Errori dell'Endpoint di Stato
-----------------------------

Se invece qualsiasi controllo di convalida eseguito dalla Relying Party fallisce, la pagina del Codice QR DOVREBBE essere aggiornata con un messaggio di errore. Inoltre, l'endpoint di stato DEVE restituire una risposta di errore, la cui struttura dipende dalla natura dell'errore. La risposta DEVE utilizzare ``application/json`` come tipo di contenuto e DEVE includere i seguenti parametri:

* ``error``: Il codice di errore.
* ``error_description``: Testo in forma leggibile dall'uomo che fornisce ulteriori dettagli per chiarire la natura dell'errore incontrato.

La seguente tabella elenca i Codici di Stato HTTP e i relativi codici di errore che DEVONO essere supportati per la risposta di errore:

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

Quando l'user-agent viene reindirizzato all'URI di Reindirizzamento fornito dalla Relying Party, possono verificarsi diversi errori che impediscono il completamento con successo del processo. Questi errori sono critici in quanto influenzano direttamente l'esperienza dell'Utente ostacolando il flusso fluido di informazioni tra l'Istanza del Wallet e la Relying Party. La gestione di questi errori richiede una comunicazione chiara all'Utente all'interno della pagina web di navigazione restituita. La Relying Party DEVE implementare i meccanismi di gestione degli errori e di convalida per gli URI di Reindirizzamento definiti in questa specifica. Di seguito sono riportati potenziali errori relativi all'URI di Reindirizzamento, la risposta di errore DEVE utilizzare ``application/json`` come tipo di contenuto e DEVE includere i seguenti parametri:

    - ``error``: Il codice di errore.
    - ``error_description``: Testo in forma leggibile dall'uomo che fornisce ulteriori dettagli per chiarire la natura dell'errore incontrato.

La seguente tabella elenca i Codici di Stato HTTP e i relativi codici di errore che DEVONO essere supportati per la risposta di errore:

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

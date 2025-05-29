.. include:: ../common/common_definitions.rst


Emissione dell'Attestato di Wallet
==================================

Questa sezione descrive come il Fornitore di Wallet emette un Attestato di Wallet.

.. plantuml:: plantuml/wallet-attestation-issuance.puml
    :width: 99%
    :alt: La figura illustra il Diagramma di Sequenza per l'acquisizione dell'Attestato di Wallet.
    :caption: `Diagramma di Sequenza per l'acquisizione dell'Attestato di Wallet. <https://www.plantuml.com/plantuml/svg/VLHDRnCn4BtxLupS0waKBaXmg0HgLKfRWL3K5hX4YcRNazrHDlPYpsu9lnvxcsQtnUrb5TjlFjwRUJaDWbwwRQEm4sUxRK5UrMm8riv9uVweDsq4SCajMb4AIt4Uz8z0NWC6w4B4Jn2WVs7JaC2r3OAsf065RGjFKP-fvv8YIgZoB3ku9J_Sd2skmqCCIe2Zq7gsLUM9RBRCmhkU3NaeiDoGDKDeKMwKKgcrjvzYwHEueTyT1G44I_VWMl8ex2n8ZRAqFhwofm08-wnd8X4-O19Zxb4eaL0gVlOvpsigDy1hEFUxLbpbiQsvX2lqvXuzmLVQmTBUOGKphUlzxMf3kvLWfVKnS03iaHii6bBJp9TaKuEf8GlKrhIDnmPYABJ8FkKxt0u9swxGUWx_NNlkOo6bl7L2u7hoYSGyoWD7twulh-ukRouklgi79iy5vG19S71ha9hW2vb7rT0QS8KWMs09i2L1WuAAh4cL3cHYdL5whQrBww17GOSnnS-076d3sbEe9m43Pg_DU6jecYWhO4IN3PELLUflLMEezR0WjrTdxzv_c1sIpI4hwN4kwMlpNhZ5qawc7RYoA9sF9U0ZfDDibkjf3jaLcLwF4ntRGWadMOugFOsIyQFBLXW2-JH4hNFSClj_6E0zI_rIhZdaISzXb7XfSnnVK7xGYinGT6A1_8PFjksMh7c5nDFT6ssHZdbR98C_-qTBpc3BmjZmNpA37VhuswWkiAsoenozCUxxpnI3GgD6-SUiudbeRWPvP4xpkBqJyBcd_4PCxPYLEhJE1dfkqEavngfJigRRDly0>`_


.. .. figure:: ../../images/wallet_instance_acquisition.svg
..   :figwidth: 100%
..   :align: center
..   :target: https://www.plantuml.com/plantuml/svg/VLHFRnC_4BtxKupSmo-LyhiWmQ4Ig5LLsWg4ehR09L8qkvxiMjcC5tisfNnwx4s9jy7qiehjDt_UcpSv3u9UXcsdS137mxOYhrfh2DREIUL-gl_w2B2rxP55AQp5UT1V0taD66084Jz1WFwENKS2jnm4kQOHXNqFBr6Vw0akH2Y2n3g6YyLjs4DH0fo4tbjk6a_4nUmBxtRMa8SAwmsn6KEhUgEKIXtz_o5MF8Cx-Z5G441WUWJNazyNanPboJw-May14FPPfmqbedQ7GgbtfUBdEUTbI_K6x1ek_LClhl7OjxQ66_Jc4Jr18hRa1snWfdNxVBlQqDDAiD7w56m0tA7jiEf8JJDV4wS6KqCCrBUqZSSEOYZqQ7tATxWT4_P3fVKS_hhsTXSBAUNP2O7RaKyavb4UEFbyUttpS7rtTVL5xPaS2se39C71hK5QWeza_gY6RC1LWfR1Ie0j2HeKLCGcLJgGYNMoz5gpIoxGMT1nJF4p8ZDjM7iARGxOOvwroRU6fecA0aPqtLbYMQN-LYs6Ley6kR-vUFFstUoGR0v5IK-BIL-Pzy8jbZoPTh0Demm-be3ta4wpMQcdEHGjChtE4yrjeOIp8aULdh9aAHIpfRKkyIfu_p2yHojjASySocJdaALTSedRFnGVDIApBvYjNtRsn6NtnEOL0YyzbzSX7Slha1Rxw0yiROHbAnOx-ulCk0Qx-Dke8LXkYYFCEv5z_Yt5e53MgF1OKBi4A-fVH9RrJewTW2yzbPqmMS6opA5t7EXuAQVd6AlEYSsmxNu3

..   Sequence Diagram for Wallet Attestation acquisition

**Passo 1**: L'Utente avvia una nuova operazione che richiede l'acquisizione di un Attestato di Wallet.

**Passi 2-3**: L'Istanza del Wallet DEVE:

  1. Verificare l'esistenza delle Cryptographic Hardware Keys. Se non esistono, è necessaria la reinizializzazione dell'Istanza del Wallet.
  2. Generare una coppia di chiavi asimmetriche effimere per l'Attestato di Wallet (``ephemeral_key_pub``, ``ephemeral_key_priv``), collegando la chiave pubblica all'attestato.
  3. Verificare l'appartenenza del Fornitore di Wallet alla federazione e recuperare i suoi metadati.

**Passi 4-6 (Recupero del Nonce)**: L'Istanza del Wallet richiede un ``nonce`` dall'endpoint :ref:`wallet-provider-endpoint:Endpoint Nonce della Soluzione Wallet` del Backend del Fornitore del Wallet. Questo ``nonce`` deve essere imprevedibile e serve come principale difesa contro gli attacchi di replay.

Il ``nonce`` DEVE essere prodotto in modo da garantire il suo utilizzo singolo entro un periodo di tempo predeterminato.

In caso di richiesta riuscita, il Fornitore di Wallet genera e restituisce il valore del nonce all'Istanza del Wallet.

**Passo 7**: L'Istanza del Wallet esegue le seguenti azioni:

* Crea ``client_data``, un oggetto JSON che include il ``nonce`` e l'impronta digitale della JWK ``ephemeral_key_pub``.
* Calcola ``client_data_hash`` applicando l'algoritmo ``SHA256`` al ``client_data``.

Di seguito è riportato un esempio non normativo dell'oggetto JSON ``client_data``.

.. code-block:: json

  {
    "nonce": "i4ThI2Jhbu81i8mqyWEuDG5t",
    "jwk_thumbprint": "vbeXJksM45xphtANnCiG6mCyuU4jfGNzopGuKvogg9c"
  }

**Passi 8-10**: L'Istanza del Wallet:

* produce un valore ``hardware_signature`` firmando il ``client_data_hash`` con la chiave privata dell'Hardware del Wallet, servendo come prova di possesso delle Cryptographic Hardware Keys.
* richiede al Servizio di Integrità del Dispositivo di creare un valore ``integrity_assertion`` collegato al ``client_data_hash``.
* riceve un valore firmato ``integrity_assertion`` dal Servizio di Integrità del Dispositivo, autenticato dall'OEM.

.. note:: 
  ``integrity_assertion`` è un payload personalizzato generato dal Servizio di Integrità del Dispositivo, firmato dall'OEM del dispositivo e codificato in base64 per avere uniformità tra diversi dispositivi.

**Passi 11-12 (Richiesta di Emissione dell'Attestato di Wallet)**: L'Istanza del Wallet:

* Costruisce la Richiesta di Attestato di Wallet sotto forma di JWT. Questo JWT include ``integrity_assertion``, ``hardware_signature``, ``nonce``, ``hardware_key_tag``, ``cnf`` e altri parametri relativi alla configurazione (vedi :ref:`Tabella del Corpo della Richiesta di Attestato di Wallet <table_key_binding_request_claim>`) ed è firmato utilizzando la chiave privata della coppia di chiavi effimere generata inizialmente.
* Invia la Richiesta di Attestato di Wallet all'endpoint :ref:`wallet-provider-endpoint:Endpoint di Emissione dell'Attestato di Wallet` del Backend del Fornitore del Wallet.

L'Istanza del Wallet DEVE inviare il JWT firmato della Richiesta di Attestato di Wallet come parametro ``assertion`` nel corpo di una richiesta HTTP all'endpoint :ref:`wallet-provider-endpoint:Endpoint di Emissione dell'Attestato di Wallet` del Fornitore di Wallet.

**Passi 13-17**: Il Backend del Fornitore del Wallet valuta la Richiesta di Attestato di Wallet e DEVE eseguire i seguenti controlli:

  1. La richiesta DEVE includere tutti i parametri dell'intestazione HTTP richiesti come definito in :ref:`wallet-provider-endpoint:Richiesta di Emissione dell'Attestato di Wallet`.
  2. La firma della Richiesta di Attestato di Wallet DEVE essere valida e verificabile utilizzando la ``jwk`` fornita.
  3. Il valore ``nonce`` DEVE essere stato generato dal Fornitore di Wallet e non essere stato utilizzato in precedenza.
  4. DEVE esistere un'Istanza del Wallet valida e attualmente registrata associata a quella fornita.
  5. Il ``client_data`` DEVE essere ricostruito utilizzando il ``nonce`` e la chiave pubblica ``jwk``. Il valore del parametro ``hardware_signature`` viene quindi convalidato utilizzando la chiave pubblica della Cryptographic Hardware Key registrata associata all'Istanza del Wallet.
  6. L'``integrity_assertion`` DEVE essere convalidato secondo le linee guida del produttore del dispositivo. I controlli specifici eseguiti dal Fornitore di Wallet sono dettagliati nella documentazione del produttore del sistema operativo.
  7. Il dispositivo in uso DEVE essere privo di difetti di sicurezza noti e soddisfare i requisiti minimi di sicurezza definiti dal Fornitore di Wallet.
  8. L'URL nel parametro ``iss`` DEVE corrispondere all'identificatore URL del Fornitore di Wallet.

Dopo il completamento con successo di tutti i controlli, il Fornitore di Wallet emette un Attestato di Wallet valido per un massimo di 24 ore.

**Passo 18 (Risposta di Emissione dell'Attestato di Wallet)**: Al completamento con successo, il Fornitore di Wallet DEVE restituire una risposta di conferma utilizzando il codice di stato 200 e Content-Type ``application/json``, contenente gli Attestati di Wallet firmati dal Fornitore di Wallet. Il Fornitore di Wallet DEVE restituire l'Attestato di Wallet in almeno tre formati: JWT, SD-JWT e mdoc. L'Istanza del Wallet eseguirà quindi la verifica di sicurezza e integrità degli Attestati di Wallet ricevuti oltre alla verifica di fiducia del suo Fornitore di Credenziale.


Di seguito è riportato un esempio non normativo della risposta.

.. code-block:: http

  HTTP/1.1 200 OK
  Content-Type: application/json

  {
    "wallet_attestations": [
      {
        "format": "jwt",
        "wallet_attestation": "ey..."
      },
      {
        "format": "dc+sd-jwt",
        "wallet_attestation": "ey..."
      },
      {
        "format": "mso_mdoc",
        "wallet_attestation": "omppc3N1ZXJBdXRohEOhASahG...ArQwggKwMIICVqADAgEC"
      }
    ]
  }

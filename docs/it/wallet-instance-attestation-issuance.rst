.. include:: ../common/common_definitions.rst


Emissione della Wallet Instance Attestation
===========================================

Questa sezione descrive come il Fornitore di Wallet emette una Wallet Instance Attestation.

.. plantuml:: plantuml/wallet-attestation-issuance.puml
    :width: 99%
    :alt: La figura illustra il Diagramma di Sequenza per l'acquisizione della Wallet Instance Attestation.
    :caption: `Diagramma di Sequenza per l'acquisizione della Wallet Instance Attestation. <https://www.plantuml.com/plantuml/svg/ZLHFJni_4BtxKupCuHUa_2wLsWDIAn2bW5fL4T3s4YcQh2UxespihJsxQVhfQsyWku2XlQpYyVFyUMzUJeEWbtPJAsp5sNQp9AygDWGhvsJfVYdrNnCHN723LXGMuZpeRu6y1WpGXeWV0K3_mBecWMiR16r1FGgR1XwZFbB71KMKKEbPTd1Ble-SpQx3_WrAWAFGUBPbwObijipCkuuDULXYiIPh-gVBOgsKIgtz_o6MFe4R-jbI442mj0NNa4TXPq4gbBdryPOz1K1uqZoSYL2G7fn6vmw5qZHAnSzzylEAYZNm2ixzhX5NUcmgBk0AlTcY9_XCEvZREonXedLr7rsiQRSGBBK-1Ww07NADovhKEFCbsTHfwim2DHLjuh66-1GQP9_o7Q9zmgPTQZs5Ps7FNIoabBTE25n7FWqnZJp1qPVhowkxovkBYwzgFybJPZb0OXxS2gGY-4JcWJwq1jnIa2sm1DYGe451HTQaIeTXOfr10wsjItkX1q9xlUAdHmvZmyfJg8O7UymzDqFKq3XHbi28BcecAulKtwB2KEb-KswlpjwyVJSv99j2bjBZRD9Nz9wvsToEr0vSMfJMnnBm7j9fCidrD8NiYep3Ww93MoZX93kZIbS3PVnWjmM6G3w9g7LsjbUCS51oorAzb7GA-UcdC70zjxbXynBquQP6MJc_sP-sVOkBuEesrLomoSSxyg7l2UOsTK9ct_bWgBnVHhjxIzRy2oMFLtfmMpg-u3PUFKlC0TYoCDRycqpliYx-DgeDRCliXWoM6spqFRr1eO7np6LUlomqgsWMcLSmcM84FlVqbqKRs_rryaFZRA1d_mIZSqoYJicQTbF_0G00>`_


**Passo 1**: L'Utente avvia una nuova operazione che richiede l'acquisizione di una Wallet Instance Attestation.

**Passi 2-3**: L'Istanza del Wallet DEVE:

  1. Verificare l'esistenza delle Cryptographic Hardware Keys. Se non esistono, è necessaria la reinizializzazione dell'Istanza del Wallet (:ref:`WP_140a <wallet-instance-optional-testcases>`).
  2. Generare una coppia di chiavi asimmetriche effimere per la Wallet Instance Attestation (``ephemeral_key_pub``, ``ephemeral_key_priv``), collegando la chiave pubblica all'attestazione (:ref:`WP_026 <wallet-instance-testcases>`). 
  3. Verificare l'appartenenza del Fornitore di Wallet alla federazione e recuperare i suoi metadati (:ref:`WP_023 <wallet-instance-testcases>`).

**Passi 4-6 (Recupero del Nonce)**: L'Istanza del Wallet richiede un ``nonce`` all'endpoint :ref:`wallet-provider-endpoint:Endpoint Nonce della Soluzione Wallet` del Backend del Fornitore del Wallet (:ref:`WP_140b <wallet-instance-optional-testcases>`). Il ``nonce`` deve essere imprevedibile e funge da principale difesa contro gli attacchi di replay.

Il ``nonce`` DEVE garantire un utilizzo singolo entro un intervallo di tempo predeterminato.

In caso di richiesta riuscita, il Fornitore di Wallet genera e restituisce il valore del nonce all'Istanza del Wallet.

**Passo 7**: L'Istanza del Wallet esegue le seguenti azioni (:ref:`WP_140c <wallet-instance-optional-testcases>`):

* Crea ``client_data``, un oggetto JSON che include il ``nonce`` e la thumbprint JWK di ``ephemeral_key_pub``.
* Calcola i corrispondenti hash, ``client_data_hash`` applicando l'algoritmo SHA256 a ``client_data``.

Di seguito è riportato un esempio non normativo dell'oggetto JSON ``client_data``.

.. code-block:: json

  {
    "nonce": "i4ThI2Jhbu81i8mqyWEuDG5t",
    "jwk_thumbprint": "vbeXJksM45xphtANnCiG6mCyuU4jfGNzopGuKvogg9c"
  }


**Passi 8-10**: L'Istanza del Wallet:

* produce un valore ``hardware_signature`` firmando ``client_data_hash`` con la chiave privata dell'Hardware del Wallet, servendo come prova di possesso delle Cryptographic Hardware Keys (:ref:`WP_140d <wallet-instance-optional-testcases>`).
* richiede al Servizio di Integrità del Dispositivo di creare un valore ``integrity_assertion`` collegato al ``client_data_hash``.
* riceve un valore ``integrity_assertion`` firmato per l'Istanza del Wallet dal Servizio di Integrità del Dispositivo, autenticato dall'OEM (:ref:`WP_140e <wallet-instance-optional-testcases>`).

.. note::
  ``integrity_assertion`` è un payload personalizzato generato dal Servizio di Integrità del Dispositivo, firmato dall'OEM del dispositivo e codificato in base64 per avere uniformità tra diversi dispositivi.


**Passi 11-12 (Richiesta di Emissione della Wallet Instance Attestation)**: L'Istanza del Wallet:

* Costruisce la Wallet Instance Attestation Request sotto forma di JWT. Questo JWT include l'``integrity_assertion``, ``hardware_signature``, ``nonce``, ``hardware_key_tag``, ``cnf``, ``platform``, ``wallet_solution_id``, ``wallet_solution_version``  e altri parametri relativi alla configurazione (vedi :ref:`Tabella del Corpo della Richiesta di Wallet Instance Attestation <table_wia_request_claim>`) ed è firmato utilizzando la chiave privata la cui chiave pubblica è indicata nella richiesta tramite ``cnf`` (:ref:`WP_140–141 <wallet-instance-optional-testcases>`).
* Invia la Wallet Instance Attestation Request all'endpoint :ref:`wallet-provider-endpoint:Endpoint di Emissione della Wallet Instance Attestation` del Backend del Fornitore del Wallet.


L'Istanza del Wallet DEVE inviare il JWT firmato della Richiesta di Wallet Instance Attestation come parametro ``assertion`` nel corpo di una richiesta HTTP all'endpoint :ref:`wallet-provider-endpoint:Endpoint di Emissione della Wallet Instance Attestation` del Fornitore di Wallet (:ref:`WP_142 <wallet-instance-optional-testcases>`).

**Passi 13-17**: Il Backend del Fornitore del Wallet valuta la Richiesta di Wallet Instance Attestation e DEVE eseguire i seguenti controlli (:ref:`WP_143 <wallet-instance-optional-testcases>`):

  1. La richiesta DEVE includere tutti i parametri dell'intestazione HTTP richiesti come definito in :ref:`wallet-provider-endpoint:Richiesta di Emissione della Wallet Instance Attestation` (:ref:`WP_143a <wallet-instance-optional-testcases>`).
  2. La firma della Richiesta di Wallet Instance Attestation DEVE essere valida e verificabile utilizzando la ``jwk`` fornita (:ref:`WP_143b <wallet-instance-optional-testcases>`).
  3. Il valore ``nonce`` DEVE essere stato generato dal Fornitore di Wallet e non essere stato utilizzato in precedenza (:ref:`WP_143c <wallet-instance-optional-testcases>`).
  4. DEVE esistere un'Istanza del Wallet valida e attualmente registrata associata al ``hardware_key_tag`` (:ref:`WP_143d <wallet-instance-optional-testcases>`).
  5. Il ``client_data`` DEVE essere ricostruito utilizzando il ``nonce`` e la chiave pubblica ``jwk``. Il valore del parametro ``hardware_signature`` viene quindi convalidato utilizzando la chiave pubblica della Cryptographic Hardware Key registrata associata all'Istanza del Wallet (:ref:`WP_143e <wallet-instance-optional-testcases>`).
  6. L'``integrity_assertion`` DEVE essere convalidato secondo le linee guida del produttore del dispositivo. I controlli specifici eseguiti dal Fornitore di Wallet sono dettagliati nella documentazione del produttore del sistema operativo  (:ref:`WP_143f <wallet-instance-optional-testcases>`).
  7. Il dispositivo in uso DEVE essere privo di difetti di sicurezza noti e soddisfare i requisiti minimi di sicurezza definiti dal Fornitore di Wallet.
  8. L'URL nel parametro ``iss`` DEVE corrispondere all'identificatore URL del Fornitore di Wallet  (:ref:`WP_143g <wallet-instance-optional-testcases>`).

Al completamento con successo di tutte le verifiche, il Fornitore di Wallet emette una Wallet Instance Attestation valida per meno di 24 ore (:ref:`WP_144 <wallet-instance-optional-testcases>`).

**Passo 18 (Risposta di Emissione della Wallet Instance Attestation)**: Al completamento con successo, il Fornitore di Wallet DEVE restituire una risposta di conferma utilizzando il codice di stato 200 e il Content-Type ``application/json``, contenente la Wallet Instance Attestations firmate dal Fornitore di Wallet. Il Fornitore di Wallet DEVE restituire la Wallet Instance Attestation in formato ``JWT``. L'Istanza del Wallet eseguirà quindi la verifica di sicurezza e integrità della Wallet Instance Attestations ricevute, oltre alla verifica di fiducia del relativo emittente (:ref:`WP_030–031 <wallet-instance-testcases>`).


Di seguito è riportato un esempio non normativo della risposta.

.. code-block:: http

  HTTP/1.1 200 OK
  Content-Type: application/json

  {
    "wallet_instance_attestation": "omppc3N1ZXJBdXRohEOhASaiBE...dElEAnFlbGVtZW50SWRl"
  }



.. include:: ../common/common_definitions.rst


Emissione della Key Attestation
========================================

Questa sezione descrive come il Fornitore di Wallet emette una Key Attestation.

.. plantuml:: plantuml/wallet-attestation-issuance.puml
    :width: 99%
    :alt: La figura illustra il Diagramma di Sequenza per l'acquisizione della Key Attestation.
    :caption: `Diagramma di Sequenza per l'acquisizione della Key Attestation. <https://www.plantuml.com/plantuml/svg/fLNVRoCr47xtNp7oFP1AUvL0WeTAe8jAQIlG4Ltlu86WQ7OzoLhPZ1VRcrB-UcntcztwN7GLBr7i_UR7VDzuvftpQFrmw0GEtl1mgCcALYk2hJ6-DdyByTKg87IZUsJl13RUM92V75a9w61mmQ2V421_nwuZ3xSSN7D32OLz3yzHFzC3BBsd0FBQC2nNjov1z-WTl76zrRpRMI9-RlSZ7NL3mRkddTN-0Ux8nfl90POTPEcjh3bgHHPgRFR4AfdMpLw8MD7R7qB65_21_Xh8UK1WkWVJatrCrhVersp3Lst90K9UJQH97z5Jh5o8y3Dwl6ofsOFUmgLzwBtPMUnRtS0DMdMFbfAZDN_47IoaRCVRpPuUDXvtKfvLK2Ak0cG5EJNf4qIlU4JTOTtHF9LhubWFEJ1CO2mWrEYR5imM6akAs6li8CI67hLTk3Fm1ce2JD59WUOycvXrJBOVwitNKbOm7gq-flFv-Na54uGp28SAXR1iF84vaetiLK4KUFFBxVNDn-iFLrVlnIE5kOpQGPGv9kzRWfz8ZM8bQapjKJDex-107XLw5CGgHHev2M4cmQLa4tjNJaActWW_2JcnDuEchoEvqwsYPovA2WHqqsbYluc9RLfqhKpzU7Up_ERRxnOdPnNyCP5NvlFFCoY6-8z-MvdLccVTvlIEqGys18Jl8PuMYrA65PHRDB-EqeRxfxJGkujonLjZvzth7Dcee8Wce-6SC_q4tU0JLCerrsPW5LiraGR9UfAbQ9GYPtChfDlv-5ANhApH2jv-rkpRpjmdKyAcFJqKCVLCd6LZsVkKVMFf9RqdHwEQGaIRO9dN7R_Zc4QnvcWvrLmmW5E7GExPRRmPmLAEwXSyLEbkabPHLZHrZY9x-jUxaJdy4kPIMg-cwlzrI1B_q_9B6oLYNqrWvgr88h4gZuUyxyOfTI7bpDaOwiLOXUmgAB_w2gQ9i-RI8vyDdSV3VNey6sUw8SRRQ5M-Fv9rftpw3dqWz12ApwYO9l8TiO9PeVb8Vd_Q5U5KGNbPw6t-ka4xqApZXjF_a4fBuXZ-Ap4upJlul6Pn5I1iFCstm6_HvDaMA7_CcO_nfY6yVnp2PTEYccLeISiYSj8knarD7Kr2uMj-gTjcZYuj5TfIp1TWmOlh3JiI-KAS7OEXU4UiXaFtBm00>`_

.. .. figure:: ../../images/wallet_instance_acquisition.svg
..   :figwidth: 100%
..   :align: center
..   :target: https://www.plantuml.com/plantuml/svg/VLHFRnC_4BtxKupSmo-LyhiWmQ4Ig5LLsWg4ehR09L8qkvxiMjcC5tisfNnwx4s9jy7qiehjDt_UcpSv3u9UXcsdS137mxOYhrfh2DREIUL-gl_w2B2rxP55AQp5UT1V0taD66084Jz1WFwENKS2jnm4kQOHXNqFBr6Vw0akH2Y2n3g6YyLjs4DH0fo4tbjk6a_4nUmBxtRMa8SAwmsn6KEhUgEKIXtz_o5MF8Cx-Z5G441WUWJNazyNanPboJw-May14FPPfmqbedQ7GgbtfUBdEUTbI_K6x1ek_LClhl7OjxQ66_Jc4Jr18hRa1snWfdNxVBlQqDDAiD7w56m0tA7jiEf8JJDV4wS6KqCCrBUqZSSEOYZqQ7tATxWT4_P3fVKS_hhsTXSBAUNP2O7RaKyavb4UEFbyUttpS7rtTVL5xPaS2se39C71hK5QWeza_gY6RC1LWfR1Ie0j2HeKLCGcLJgGYNMoz5gpIoxGMT1nJF4p8ZDjM7iARGxOOvwroRU6fecA0aPqtLbYMQN-LYs6Ley6kR-vUFFstUoGR0v5IK-BIL-Pzy8jbZoPTh0Demm-be3ta4wpMQcdEHGjChtE4yrjeOIp8aULdh9aAHIpfRKkyIfu_p2yHojjASySocJdaALTSedRFnGVDIApBvYjNtRsn6NtnEOL0YyzbzSX7Slha1Rxw0yiROHbAnOx-ulCk0Qx-Dke8LXkYYFCEv5z_Yt5e53MgF1OKBi4A-fVH9RrJewTW2yzbPqmMS6opA5t7EXuAQVd6AlEYSsmxNu3

..   Sequence Diagram for Wallet Attestation acquisition

**Passo 1**: L'Utente avvia una nuova operazione che richiede l'acquisizione di una Key Attestation.

**Passi 2-3**: L'Istanza del Wallet DEVE:

  1. Verificare l'esistenza delle Cryptographic Hardware Keys. Se non esistono, è necessaria la reinizializzazione dell'Istanza del Wallet (:ref:`WP_140a <wallet-instance-optional-testcases>`).
  2. Generare una o più coppie di chiavi asimmetriche delle Credenziali da attestare nella Key Attestation (``key_pub_1``, ``key_priv_1``, ..., ``key_pub_n``, ``key_priv_n``).
  3. Verificare l'appartenenza del Fornitore di Wallet alla federazione e recuperare i suoi metadati (:ref:`WP_023 <wallet-instance-testcases>`).

**Passi 4-6 (Recupero del Nonce)**: L'Istanza del Wallet richiede un ``nonce`` all'endpoint :ref:`wallet-provider-endpoint:Endpoint Nonce della Soluzione Wallet` del Backend del Fornitore del Wallet (:ref:`WP_140b <wallet-instance-optional-testcases>`). Il ``nonce`` deve essere imprevedibile e funge da principale difesa contro gli attacchi di replay.

Il ``nonce`` DEVE garantire un utilizzo singolo entro un intervallo di tempo predeterminato.

In caso di richiesta riuscita, il Fornitore di Wallet genera e restituisce il valore del nonce all'Istanza del Wallet.

**Passo 7**: L'Istanza del Wallet esegue le seguenti azioni (:ref:`WP_140c <wallet-instance-optional-testcases>`):

* Crea ``client_data``, un oggetto JSON che include il ``nonce`` e un campo ``jwk_thumbprints`` contenente un array JSON delle impronte JWK corrispondenti alle chiavi pubbliche (``key_pub_1``, ..., ``key_pub_n``).
* Calcola i corrispondenti hash, ``client_data_hash`` applicando l'algoritmo SHA256 a ``client_data``.

Di seguito è riportato un esempio non normativo dell'oggetto JSON ``client_data``.

.. code-block:: json

  {
    "nonce": "i4ThI2Jhbu81i8mqyWEuDG5t",
    "jwk_thumbprints": ["vbeXJksM45xphtANnCiG6mCyuU4jfGNzopGuKvogg9c"]
  }


**Passi 8-11**: L'Istanza del Wallet:

* produce un valore ``hardware_signature`` firmando ``client_data_hash`` con la chiave privata dell'Hardware del Wallet, servendo come prova di possesso delle Cryptographic Hardware Keys (:ref:`WP_140d <wallet-instance-optional-testcases>`).
* richiede al Servizio di Integrità del Dispositivo di creare un valore ``integrity_assertion`` collegato al ``client_data_hash``.
* riceve un valore ``integrity_assertion`` firmato per l'Istanza del Wallet dal Servizio di Integrità del Dispositivo, autenticato dall'OEM (:ref:`WP_140e <wallet-instance-optional-testcases>`).

.. note::
  ``integrity_assertion`` è un payload personalizzato generato dal Servizio di Integrità del Dispositivo, firmato dall'OEM del dispositivo e codificato in base64 per avere uniformità tra diversi dispositivi.

.. note::
   Nel caso del sistema operativo Android, il flusso prosegue in base con i **Passi 12-15**, mentre per il caso di iOS, il flusso prosegue con i **Passi 16-19**.

**Passi 12-15**: L'Istanza del Wallet:

* richiede all'API di Key Attestation di creare un valore ``key_attestation`` collegato per ogni ``client_data_hash`` per ciascuna ``key_pub``.
* riceve un valore ``key_attestation`` firmato dall'API di Key Attestation, autenticato dall'OEM.
* genera un valore ``keys_to_attest`` firmando il ``key_attestation`` utilizzando la chiave privata della coppia di chiavi di credenziale generata inizialmente (``priv_key``).

**Passi 16-19**: L'Istanza del Wallet:

* richiede al Servizio di Integrità del Dispositivo di creare un valore ``integrity_assertion`` collegato per ogni ``client_data_hash`` per ogni ``key_pub``.
* riceve un valore ``integrity_assertion`` firmato per la Key Attestation dal Servizio di Integrità del Dispositivo, autenticato dall'OEM.
* genera un valore ``keys_to_attest`` firmando l'``integrity_assertion`` ottenuto per la key Attestation utilizzando la chiave privata della coppia di chiavi di credenziale generata inizialmente (``priv_key``).

**Passi 20-21 (Richiesta di Emissione della Key Attestation)**: L'Istanza del Wallet:

* Costruisce la Key Attestation Request sotto forma di JWT. Questo JWT include l'``integrity_assertion``, ``keys_to_attest``, ``hardware_signature``, ``nonce``, ``hardware_key_tag``, ``cnf``, ``platform``, ``wallet_solution_id``, ``wallet_solution_version``  e altri parametri relativi alla configurazione (vedi :ref:`Tabella del Corpo della Richiesta di Key Attestation <table_ka_request_claim>`). La Key Attestation Request DEVE essere firmata utilizzando la chiave privata corrispondente alla chiave pubblica inclusa nella richiesta, tramite il parametro ``cnf`` (primo elemento di ``keys_to_attest``) (:ref:`WP_140–141 <wallet-instance-optional-testcases>`).
* Invia la Key Attestation Request all'endpoint :ref:`wallet-provider-endpoint:Endpoint di Emissione della Key Attestation` del Backend del Fornitore del Wallet.

.. note::
  ``keys_to_attest`` contiene un oggetto ``key_attestation`` nel caso di Android e un oggetto ``integrity_assertion`` nel caso di iOS.

L'Istanza del Wallet DEVE inviare il JWT firmato della Richiesta di Key Attestation come parametro ``assertion`` nel corpo di una richiesta HTTP all'endpoint :ref:`wallet-provider-endpoint:Endpoint di Emissione della Key Attestation` del Fornitore di Wallet (:ref:`WP_142 <wallet-instance-optional-testcases>`).

**Passi 22-27**: Il Backend del Fornitore del Wallet valuta la Richiesta di Key Attestation e DEVE eseguire i seguenti controlli (:ref:`WP_143 <wallet-instance-optional-testcases>`):

  1. La richiesta DEVE includere tutti i parametri dell'intestazione HTTP richiesti come definito in :ref:`wallet-provider-endpoint:Richiesta di Emissione della Key Attestation` (:ref:`WP_143a <wallet-instance-optional-testcases>`).
  2. La firma della Richiesta di Key Attestation DEVE essere valida e verificabile utilizzando la ``jwk`` fornita (:ref:`WP_143b <wallet-instance-optional-testcases>`).
  3. Il valore ``nonce`` DEVE essere stato generato dal Fornitore di Wallet e non essere stato utilizzato in precedenza (:ref:`WP_143c <wallet-instance-optional-testcases>`).
  4. DEVE esistere un'Istanza del Wallet valida e attualmente registrata associata al ``hardware_key_tag`` (:ref:`WP_143d <wallet-instance-optional-testcases>`).
  5. La firma del parametro ``keys_to_attest`` deve essere prima validata utilizzando la ``jwk`` fornita, e il suo valore (``key_attestation`` nel caso di Android o ``integrity_assertion`` nel caso di iOS) DEVE essere validato secondo le linee guida del produttore del dispositivo.
  6. Il ``client_data`` DEVE essere ricostruito utilizzando il ``nonce`` e le rispettive thumbprint JWKs ``[key_pub_1,...,key_pub_n]``. Il valore del parametro ``hardware_signature`` viene quindi convalidato utilizzando la chiave pubblica della Cryptographic Hardware Key registrata associata all'Istanza del Wallet (:ref:`WP_143e <wallet-instance-optional-testcases>`).
  7. L'``integrity_assertion`` DEVE essere convalidato secondo le linee guida del produttore del dispositivo. I controlli specifici eseguiti dal Fornitore di Wallet sono dettagliati nella documentazione del produttore del sistema operativo  (:ref:`WP_143f <wallet-instance-optional-testcases>`).
  8. Il dispositivo in uso DEVE essere privo di difetti di sicurezza noti e soddisfare i requisiti minimi di sicurezza definiti dal Fornitore di Wallet.
  9. L'URL nel parametro ``iss`` DEVE corrispondere all'identificatore URL del Fornitore di Wallet  (:ref:`WP_143g <wallet-instance-optional-testcases>`).

Al completamento con successo di tutte le verifiche, il Fornitore di Wallet emette una Key Attestation valida per almeno un mese (:ref:`WP_144 <wallet-instance-optional-testcases>`).

**Passo 28 (Risposta di Emissione della Key Attestation)**: Al completamento con successo, il Fornitore di Wallet DEVE restituire una risposta di conferma con codice di stato ``200`` e Content-Type ``application/json``. La risposta DEVE contenere le Key Attestations firmate dal Fornitore di Wallet in formato JWT. L'Istanza del Wallet DEVE eseguire la verifica di sicurezza e integrità delle Key Attestations ricevute, insieme alla verifica di fiducia già valutata sull'Emittente (:ref:`WP_030–031 <wallet-instance-testcases>`).


Di seguito è riportato un esempio non normativo della risposta.

.. code-block:: http

  HTTP/1.1 200 OK
  Content-Type: application/json

  {
    "key_attestation": "omppc3N1ZXJBdXRohEOhASaiBE...dElEAnFlbGVtZW50SWRl"
  }



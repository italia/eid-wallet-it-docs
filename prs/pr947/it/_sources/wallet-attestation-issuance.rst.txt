.. include:: ../common/common_definitions.rst


Emissione della Wallet App e Wallet Unit Attestation
=====================================================

Questa sezione descrive come il Fornitore di Wallet emette una Wallet App Attestation e una Wallet Unit Attestation.

.. plantuml:: plantuml/wallet-attestation-issuance.puml
    :width: 99%
    :alt: La figura illustra il Diagramma di Sequenza per l'acquisizione della Wallet App e Wallet Unit Attestation.
    :caption: `Diagramma di Sequenza per l'acquisizione della Wallet App e Wallet Unit Attestation. <https://www.plantuml.com/plantuml/svg/fLPDR-Cs4BtpLmouXoQ0SYdG7WAqM2DDaw35rjYicui1OoIEBS8ogPAKq_JNbwF84ItJsnHx2KBgpSUyUJFqHn_GXMxN2Eo2DTsk92TghGZMreRI_Yt4T_E8q9LkqGGli0hMWLnuSXBGG-UZGJiYG3vXqr201nDTcufw5BOj7AD-enUOXK0H5BGrC9i_-1wwnU3XWs-TDfkD8pB7Th_GNbSKlGVQE1rUu94StumESEeWczxSsRrMvA34Qaj6zQPbjHM2AxhwEMPy3P_fhuvy00H3ps1RSg_9XXh3qhZuLJloy3IR0He5JuiPC45wZu6uPY7Ydy7NJKtL5lGQRjnB6-p6OLlh2kxHgMTq14p8qdp13Ln8MG-tgoszh09kfBmi84TPqGS-8OK_0Nl5FUe6ouRILEx8S2KK8L0vKcI2nWPYB6XHEmWMIWBiGv42RM0WRM5qI5FWL3d3jYkbB60uEBsF-URZ6Q2sfXsvDDxQklvGsiweGwnPsqv3lPckqg39THfUE6C3WTsJurOKiRVmuVU7k_ilTvzlRp-9rtvCrQ0zi5h0hY7K1B-IElISURPbG6r01myx2gWme22ZEDA1u1Xcr8sKnl88o54LlSJYdnuvKfD0-wy3S-EjecCN6NeZkceqcR3Yn5Or-dhrtA7ifVruF_l-XnyltXmMaBJkaglBckDvyrmxBhDvVKNnSpjVcaJlNcyCXix54F0JyEdYubnPnTcC2yYFK78zQcLC6eE_plYKaXNAKouOSW0cjEl3uAtGUtAi5ocNvbNFmK9F6lJMOsTpHcCaWKtWRJ4pobcjuEfa_DUDVMRuP8J5g3LUfKDjs_-eRH4ZCeQHa-AOA3p4pHN6bcDX6GDu4mKSUJvi6Ew5b4ExC_R5yM8HYYObKkE9oT9_F0v4uRk8Ua_N5z_OTNOoEdgN01ZxlpZB-ChmHaPbzmRhxOf33clhMih4oJY5NnLiSP9R0VcvBc3S8akJ6zHpowKuj-l7pVj8Ha6I_tJrVZgy2Nmg8Fiei98cFs90Uz16itJqFwJwTRcF_olHUMqsS5g4k8qGVXVIRVydcnnj--p72P4SBTtMl3JpTjaEvQ6vpkIHAUNv36uSCJJv6IJILopHbs-jyIIchrboZ0RY8ndLxPf_0G00>`_


.. .. figure:: ../../images/wallet_instance_acquisition.svg
..   :figwidth: 100%
..   :align: center
..   :target: https://www.plantuml.com/plantuml/svg/VLHFRnC_4BtxKupSmo-LyhiWmQ4Ig5LLsWg4ehR09L8qkvxiMjcC5tisfNnwx4s9jy7qiehjDt_UcpSv3u9UXcsdS137mxOYhrfh2DREIUL-gl_w2B2rxP55AQp5UT1V0taD66084Jz1WFwENKS2jnm4kQOHXNqFBr6Vw0akH2Y2n3g6YyLjs4DH0fo4tbjk6a_4nUmBxtRMa8SAwmsn6KEhUgEKIXtz_o5MF8Cx-Z5G441WUWJNazyNanPboJw-May14FPPfmqbedQ7GgbtfUBdEUTbI_K6x1ek_LClhl7OjxQ66_Jc4Jr18hRa1snWfdNxVBlQqDDAiD7w56m0tA7jiEf8JJDV4wS6KqCCrBUqZSSEOYZqQ7tATxWT4_P3fVKS_hhsTXSBAUNP2O7RaKyavb4UEFbyUttpS7rtTVL5xPaS2se39C71hK5QWeza_gY6RC1LWfR1Ie0j2HeKLCGcLJgGYNMoz5gpIoxGMT1nJF4p8ZDjM7iARGxOOvwroRU6fecA0aPqtLbYMQN-LYs6Ley6kR-vUFFstUoGR0v5IK-BIL-Pzy8jbZoPTh0Demm-be3ta4wpMQcdEHGjChtE4yrjeOIp8aULdh9aAHIpfRKkyIfu_p2yHojjASySocJdaALTSedRFnGVDIApBvYjNtRsn6NtnEOL0YyzbzSX7Slha1Rxw0yiROHbAnOx-ulCk0Qx-Dke8LXkYYFCEv5z_Yt5e53MgF1OKBi4A-fVH9RrJewTW2yzbPqmMS6opA5t7EXuAQVd6AlEYSsmxNu3

..   Sequence Diagram for Wallet Attestation acquisition

**Passo 1**: L'Utente avvia una nuova operazione che richiede l'acquisizione di una Wallet App e Wallet Unit Attestation.

**Passi 2-4**: L'Istanza del Wallet DEVE:

  1. Verificare l'esistenza delle Cryptographic Hardware Keys. Se non esistono, è necessaria la reinizializzazione dell'Istanza del Wallet (:ref:`WP_140a <wallet-instance-optional-testcases>`).
  2. Generare una coppia di chiavi asimmetriche di credenziale da attestare per la Wallet Unit Attestation (``key_pub``, ``key_priv``).
  3. Generare una coppia di chiavi asimmetriche effimere per la Wallet App Attestation (``ephemeral_key_pub``, ``ephemeral_key_priv``), collegando la chiave pubblica all'attestato (:ref:`WP_026 <wallet-instance-testcases>`).
  4. Verificare l'appartenenza del Fornitore di Wallet alla federazione e recuperare i suoi metadati (:ref:`WP_023 <wallet-instance-testcases>`).

**Passi 5-7 (Recupero del Nonce)**: L'Istanza del Wallet richiede un ``nonce`` all'endpoint :ref:`wallet-provider-endpoint:Endpoint Nonce della Soluzione Wallet` del Backend del Fornitore del Wallet (:ref:`WP_140b <wallet-instance-optional-testcases>`). Il ``nonce`` deve essere imprevedibile e funge da principale difesa contro gli attacchi di replay.

Il ``nonce`` DEVE garantire un utilizzo singolo entro un intervallo di tempo predeterminato.

In caso di richiesta riuscita, il Fornitore di Wallet genera e restituisce il valore del nonce all'Istanza del Wallet.

**Passo 8**: L'Istanza del Wallet esegue le seguenti azioni (:ref:`WP_140c <wallet-instance-optional-testcases>`):

* Crea due oggetti JSON, ``client_data_waa`` e ``client_data_wua``, ciascuno contenente il ``nonce`` e l'impronta digitale (thumbprint) delle rispettive JWK (``ephemeral_key_pub``, ``key_pub``).
* Calcola i corrispondenti hash, ``client_data_hash_waa`` e ``client_data_hash_wua``, applicando l'algoritmo SHA256 a ``client_data_waa`` e ``client_data_wua``.

Di seguito è riportato un esempio non normativo dell'oggetto JSON ``client_data_waa``.

.. code-block:: json

  {
    "nonce": "i4ThI2Jhbu81i8mqyWEuDG5t",
    "jwk_thumbprint": "vbeXJksM45xphtANnCiG6mCyuU4jfGNzopGuKvogg9c"
  }

**Passi 9-12**: L'Istanza del Wallet:

* produce un valore ``hardware_signature`` firmando ``client_data_hash_waa`` e ``client_data_hash_wua`` con la chiave privata dell'Hardware del Wallet, servendo come prova di possesso delle Cryptographic Hardware Keys (:ref:`WP_140d <wallet-instance-optional-testcases>`).
* richiede al Servizio di Integrità del Dispositivo di creare un valore ``integrity_assertion`` collegato al ``client_data_hash_waa``.
* riceve un valore ``integrity_assertion`` firmato per la Wallet App Attestation dal Servizio di Integrità del Dispositivo, autenticato dall'OEM (:ref:`WP_140e <wallet-instance-optional-testcases>`).

.. note::
  ``integrity_assertion`` è un payload personalizzato generato dal Servizio di Integrità del Dispositivo, firmato dall'OEM del dispositivo e codificato in base64 per avere uniformità tra diversi dispositivi.

.. note::
   Nel caso del sistema operativo Android, il flusso prosegue in base con i **Passi 13-16**, mentre per il caso di iOS, il flusso prosegue con i **Passi 17-20**.

**Passi 13-16**: L'Istanza del Wallet:

* richiede all'API di Key Attestation di creare un valore ``key_attestation`` collegato a ``client_data_hash_wua``.
* riceve un valore ``key_attestation`` firmato dall'API di Key Attestation, autenticato dall'OEM.
* genera un valore ``attested_key`` firmando il ``key_attestation`` utilizzando la chiave privata della coppia di chiavi di credenziale generata inizialmente (``priv_key``).

**Passi 17-20**: L'Istanza del Wallet:

* richiede al Servizio di Integrità del Dispositivo di creare un valore ``integrity_assertion`` collegato a ``client_data_hash_wua``.
* riceve un valore ``integrity_assertion`` firmato per la Wallet Unit Attestation dal Servizio di Integrità del Dispositivo, autenticato dall'OEM.
* genera un valore ``attested_key`` firmando l'``integrity_assertion`` ottenuto per la Wallet Unit Attestation utilizzando la chiave privata della coppia di chiavi di credenziale generata inizialmente (``priv_key``).

**Passi 21-22 (Richiesta di Emissione della Wallet App e Wallet Unit Attestation)**: L'Istanza del Wallet:

* Costruisce la Wallet App e la Wallet Unit Attestation Request sotto forma di JWT. Questo JWT include l'``integrity_assertion`` per la Wallet App Attestation, ``attested_key``, ``hardware_signature``, ``nonce``, ``hardware_key_tag``, ``cnf`` e altri parametri relativi alla configurazione (vedi :ref:`Tabella del Corpo della Richiesta di Wallet App e Wallet Unit Attestation <_table_waa_wua_request_claim>`) ed è firmato utilizzando la chiave privata della coppia di chiavi effimere generata inizialmente (:ref:`WP_140–141 <wallet-instance-optional-testcases>`).
* Invia la Wallet App e la Wallet Unit Attestation Request all'endpoint :ref:`wallet-provider-endpoint:Endpoint di Emissione della Wallet App e Wallet Unit Attestation` del Backend del Fornitore del Wallet.

.. note:: 
  ``attested_key`` contiene un oggetto ``key_attestation`` nel caso di Android e un oggetto ``integrity_assertion`` nel caso di iOS.

L'Istanza del Wallet DEVE inviare il JWT firmato della Richiesta di Wallet App e Wallet Unit Attestation come parametro ``assertion`` nel corpo di una richiesta HTTP all'endpoint :ref:`wallet-provider-endpoint:Endpoint di Emissione della Wallet App e Wallet Unit Attestation` del Fornitore di Wallet (:ref:`WP_142 <wallet-instance-optional-testcases>`).

**Passi 23-28**: Il Backend del Fornitore del Wallet valuta la Richiesta di Wallet App e Wallet Unit Attestation e DEVE eseguire i seguenti controlli (:ref:`WP_143 <wallet-instance-optional-testcases>`):

  1. La richiesta DEVE includere tutti i parametri dell'intestazione HTTP richiesti come definito in :ref:`wallet-provider-endpoint:Richiesta di Emissione della Wallet App e Wallet Unit Attestation` (:ref:`WP_143a <wallet-instance-optional-testcases>`).
  2. La firma della Richiesta di Wallet App e Wallet Unit Attestation DEVE essere valida e verificabile utilizzando la ``jwk`` fornita (:ref:`WP_143b <wallet-instance-optional-testcases>`).
  3. Il valore ``nonce`` DEVE essere stato generato dal Fornitore di Wallet e non essere stato utilizzato in precedenza (:ref:`WP_143c <wallet-instance-optional-testcases>`).
  4. DEVE esistere un'Istanza del Wallet valida e attualmente registrata associata a quella fornita (:ref:`WP_143d <wallet-instance-optional-testcases>`).
  5. La firma del parametro ``attested_key`` deve essere prima validata utilizzando la ``jwk`` fornita, e il suo valore (``key_attestation`` nel caso di Android o ``integrity_assertion`` nel caso di iOS) DEVE essere validato secondo le linee guida del produttore del dispositivo.
  6. Il ``client_data_waa`` DEVE essere ricostruito utilizzando il ``nonce`` e la chiave pubblica ``jwk``. Il valore del parametro ``hardware_signature`` viene quindi convalidato utilizzando la chiave pubblica della Cryptographic Hardware Key registrata associata all'Istanza del Wallet (:ref:`WP_143e <wallet-instance-optional-testcases>`).
  7. L'``integrity_assertion`` DEVE essere convalidato secondo le linee guida del produttore del dispositivo. I controlli specifici eseguiti dal Fornitore di Wallet sono dettagliati nella documentazione del produttore del sistema operativo  (:ref:`WP_143f <wallet-instance-optional-testcases>`).
  8. Il dispositivo in uso DEVE essere privo di difetti di sicurezza noti e soddisfare i requisiti minimi di sicurezza definiti dal Fornitore di Wallet.
  9. L'URL nel parametro ``iss`` DEVE corrispondere all'identificatore URL del Fornitore di Wallet  (:ref:`WP_143g <wallet-instance-optional-testcases>`).

Al completamento con successo di tutte le verifiche, il Fornitore di Wallet emette una Wallet App Attestation valida per meno di 24 ore (:ref:`WP_144 <wallet-instance-optional-testcases>`) e una Wallet Unit Attestation valida per almeno un mese.

**Passo 29 (Risposta di Emissione della Wallet App e Wallet Unit Attestation)**: Al completamento con successo, il Fornitore di Wallet DEVE restituire una risposta di conferma utilizzando il codice di stato 200 e il Content-Type ``application/json``, contenente le Wallet App e Wallet Unit Attestations firmate dal Fornitore di Wallet. Il Fornitore di Wallet DEVE restituire la Wallet App Attestation in formato ``JWT``. L'Istanza del Wallet eseguirà quindi la verifica di sicurezza e integrità delle Wallet App e Wallet Unit Attestations ricevute, oltre alla verifica di fiducia del relativo emittente (:ref:`WP_030–031 <wallet-instance-testcases>`).


Di seguito è riportato un esempio non normativo della risposta.

.. code-block:: http

  HTTP/1.1 200 OK
  Content-Type: application/json

  {
    "wallet_attestations": [
      "wallet_app_attestation": "omppc3N1ZXJBdXRohEOhASaiBE...dElEAnFlbGVtZW50SWRl",
      "wallet_unit_attestation": "omppc3N1ZXJBdXRohEOhASahG...ArQwggKwMIICVqADAgEC"
    ]
  }

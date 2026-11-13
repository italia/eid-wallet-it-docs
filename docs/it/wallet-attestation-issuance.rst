.. include:: ../common/common_definitions.rst


Emissione della Key Attestation
========================================

Questa sezione descrive come il Fornitore di Wallet emette una Key Attestation.

L'uso delle :term:`Key Attestation APIs (OEM)` è definito in :ref:`wallet-solution-requirements:Uso delle API di Key Attestation (OEM)`.

.. plantuml:: plantuml/wallet-attestation-issuance.puml
    :width: 99%
    :alt: La figura illustra il Diagramma di Sequenza per l'acquisizione della Key Attestation.
    :caption: `Diagramma di Sequenza per l'acquisizione della Key Attestation. <https://www.plantuml.com/plantuml/svg/lLVVRzis47xNNt7G7fPWIGOCs304w52ZwPQi6nB4IVDYmA75iyHO8ZNoPCVxwtUKs8YM5IF0jZwqaIdUTzzzzuFKUqV2KbELy0ctC252NY1bD5mvrmYTOL8eYR0qXXRcEKc-lU7zAbErqEGIaP6naDuxj2a81mq_97M_0z87KPP8SAKTURHsbwZhtKr3tvERAzVkN0boy8shhT9vRX7rhjq5hbM634wOMqLRcABrAps0E0pmCFqm-VuMAqC8_7pHscnS9iPjueXkh5cpCXOM8bkXbgtf8bibYHVXz1SEyXnkyQ-6em816ZTWQhHTW5G8ccdBRvL5Phcdlj0I5DkL5eNSWbcGK1ebY9c69PiKyFYOpRLXIHyVUSLKZ8dmmQ94JKgKRVxGdlaKgRKWR5LF-Bz0xJDQjTosJDXiMvF9hQWBbS6bi78ZB7fI3l1PEUPwbAP5M9-lS3idaQVfyHbSirkxKGx1ugdIoljMV-Ee9uIXTakKNoIfi5gWTOMgPvgZ3o6p28vVaP22H01baNjbqxGL8KtxG7qI-5_O-1jgxmAZdVvbuDOlIjm1I4H9dG0Bqp0TCY3WGkMAH1dBR7pyNaNT1dXpTT6PJhIqHicaf-LhkGl0FqN4s74HGxAyK0jbPtgZg00HbKLMU05rZl0Exkz-FVqPJ4R84fbb58h7xmFqsQgRHPhweWg_8ymuz40omT8XgEjfdCKtq5MT1bFC6elmKMUbM2EZQHaWXtgoMi65xxcX3txx0Wu1E-hLnDkCXDawZ9aprox_MQcOyzoNKffsJHD42-9u3xy_VEA_JRNm_K_kPAPvLUzQpmlX2hPv1zFBoGy__dGqm3wEtKUDurIk1R4uhQt_TJI6UmA3PcCgQqRz3ukohcFXt9nCg8aqPGNk_BeIr571vxfxoFII7sPSCYozdEyL4d0qZemLESvfMsDdjRFbcCrzt2Z15pU_xkFRhplV9-FAButjYeJD4x5JxogS1apEERITtrwmCRYlfySulyEwlAs33h6VwTVfmsliPvf57ZRTIKlFD0JN7_-4IX1QBhY-X_l1_5BhO9QUH9Xc7YyprgAhZPPAvssRrpQC7zpkjFNq2qWKuuHLgnObGj1hFEQzAJ0yOGDFlzVdQILERRVotTE6E26TQCvvYVRL2tCZ23cFVWp9d8mEW50tmoDra9Yw5CH9g4AQsiDpxapP-0ZcIewlhz6wDeF_RbxKTPG4ltv0mYYxSIu7cIRJRbWgoqOXp8DrVRYg_ZzERov1DWrbU8X8MulHtMMAxK7Sj__WyXBTNZwBKab1dQVBkxiRA518jEwrFNPFg1SHGdJyzscpIjCHXEWuF5B-_YXXCNfnEu56DmxbSGHoYxboX9QD1fV-TbgF5VlPJD_Y4sO4QWcAt9vXBAXoO75jLYZ7cFl3OAJxXZgmaw23TnxEm_FXAHNTirXEKJhM81A7BVcGEeTrS3u-rDjzNCVdeCtkj8mromp7QfkCzkudGil8m-WCYP32fr25I6xqgkqmQpn125yT5RkAgoWCEyyoAt0Su_xs3r3jq5Wgj95nk68DUg0hv5Vdh-z1XyEBz_Y7my0wIckujuNl7M0j7IKnA4Cbxr7BfYh_0G00>`_


.. .. figure:: ../../images/wallet_instance_acquisition.svg
..   :figwidth: 100%
..   :align: center
..   :target: https://www.plantuml.com/plantuml/svg/VLHFRnC_4BtxKupSmo-LyhiWmQ4Ig5LLsWg4ehR09L8qkvxiMjcC5tisfNnwx4s9jy7qiehjDt_UcpSv3u9UXcsdS137mxOYhrfh2DREIUL-gl_w2B2rxP55AQp5UT1V0taD66084Jz1WFwENKS2jnm4kQOHXNqFBr6Vw0akH2Y2n3g6YyLjs4DH0fo4tbjk6a_4nUmBxtRMa8SAwmsn6KEhUgEKIXtz_o5MF8Cx-Z5G441WUWJNazyNanPboJw-May14FPPfmqbedQ7GgbtfUBdEUTbI_K6x1ek_LClhl7OjxQ66_Jc4Jr18hRa1snWfdNxVBlQqDDAiD7w56m0tA7jiEf8JJDV4wS6KqCCrBUqZSSEOYZqQ7tATxWT4_P3fVKS_hhsTXSBAUNP2O7RaKyavb4UEFbyUttpS7rtTVL5xPaS2se39C71hK5QWeza_gY6RC1LWfR1Ie0j2HeKLCGcLJgGYNMoz5gpIoxGMT1nJF4p8ZDjM7iARGxOOvwroRU6fecA0aPqtLbYMQN-LYs6Ley6kR-vUFFstUoGR0v5IK-BIL-Pzy8jbZoPTh0Demm-be3ta4wpMQcdEHGjChtE4yrjeOIp8aULdh9aAHIpfRKkyIfu_p2yHojjASySocJdaALTSedRFnGVDIApBvYjNtRsn6NtnEOL0YyzbzSX7Slha1Rxw0yiROHbAnOx-ulCk0Qx-Dke8LXkYYFCEv5z_Yt5e53MgF1OKBi4A-fVH9RrJewTW2yzbPqmMS6opA5t7EXuAQVd6AlEYSsmxNu3

..   Sequence Diagram for Wallet Attestation acquisition

**Passo 1**: L'Utente avvia un'operazione di richiesta di una Credenziale Digitale che richiede l'acquisizione di una Key Attestation, avendo già ottenuto un nuovo ``c_nonce`` dal Credential Issuer.

**Passi 2-3**: L'Istanza del Wallet DEVE:

  1. Verificare l'esistenza delle Cryptographic Hardware Keys. Se non esistono, è necessaria la reinizializzazione dell'Istanza del Wallet (:ref:`WP_140a <wallet-instance-optional-testcases>`).
  2. Verificare l'appartenenza del Fornitore di Wallet alla federazione e recuperare i suoi metadati (:ref:`WP_023 <wallet-instance-testcases>`).

**Passi 4-6 (Recupero del Nonce)**: L'Istanza del Wallet richiede un ``nonce`` all'endpoint :ref:`wallet-provider-endpoint:Endpoint Nonce della Soluzione Wallet` del Backend del Fornitore del Wallet (:ref:`WP_140b <wallet-instance-optional-testcases>`). Il ``nonce`` deve essere imprevedibile e funge da principale difesa contro gli attacchi di replay.

Il ``nonce`` DEVE garantire un utilizzo singolo entro un intervallo di tempo predeterminato.

In caso di richiesta riuscita, il Fornitore di Wallet genera e restituisce il valore del nonce all'Istanza del Wallet.

**Passi 7-9 (Generazione delle chiavi di Credenziale)**: L'Istanza del Wallet DEVE generare una o più coppie di chiavi asimmetriche delle Credenziali da attestare (``key_pub_1``, ``key_priv_1``, ..., ``key_pub_n``, ``key_priv_n``) solo dopo che il ``nonce`` è disponibile.

Su Android, l'Istanza del Wallet DEVE generare ciascuna coppia di chiavi tramite l'API di Key Attestation. DEVE impostare il challenge di attestazione agli ottetti UTF-8 del ``nonce``. L'API restituisce la chiave pubblica e un ``key_attestation`` firmato per quella chiave. L'Istanza del Wallet NON DEVE usare ``client_data_hash`` come challenge. ``client_data_hash`` dipende dall'impronta JWK della chiave, e la piattaforma vincola il challenge al momento della generazione della chiave.

Su iOS, l'Istanza del Wallet DEVE generare ciascuna coppia di chiavi nel Secure Enclave. L'asserzione di integrità per ciascuna chiave è richiesta dopo il calcolo di ``client_data_hash``.

**Passo 10**: L'Istanza del Wallet esegue le seguenti azioni (:ref:`WP_140c <wallet-instance-optional-testcases>`):

* Crea ``client_data``, un oggetto JSON che include il ``nonce`` e un campo ``jwk_thumbprints`` contenente un array JSON delle impronte JWK corrispondenti alle chiavi pubbliche (``key_pub_1``, ..., ``key_pub_n``).
* Calcola ``client_data_hash`` applicando l'algoritmo SHA256 a ``client_data``.

Di seguito è riportato un esempio non normativo dell'oggetto JSON ``client_data``.

.. literalinclude:: ../../examples/shared/wallet-attestation-issuance-1.json
   :language: json


**Passi 11-12**: L'Istanza del Wallet produce un valore ``hardware_signature`` firmando ``client_data_hash`` con la chiave privata dell'Hardware del Wallet, come prova di possesso delle Cryptographic Hardware Keys (:ref:`WP_140d <wallet-instance-optional-testcases>`).

La Key Attestation Request NON DEVE includere un ``integrity_assertion`` di primo livello. Il Fornitore di Wallet controlla lo stato di revoca della Wallet Instance Attestation prima di emettere una Key Attestation. Su iOS, l'asserzione di integrità di ciascuna chiave è trasportata dentro ``keys_to_attest``, perché quella piattaforma non fornisce un'API di key attestation.

**Passi 13-16**: L'Istanza del Wallet costruisce ``keys_to_attest`` come array JSON di JWT. L'header e i claim di ciascun JWT sono definiti in :ref:`wallet-provider-endpoint:Elemento di Key Attestation`.

* Su Android, quando sono usate le API di Key Attestation (OEM), ciascun JWT trasporta il ``key_attestation`` ottenuto alla generazione della chiave in ``wscd_key_attestation.attestation``.
* Su iOS, l'Istanza del Wallet richiede al Servizio di Integrità del Dispositivo un ``integrity_assertion`` per ciascuna chiave, vincolato a ``client_data_hash``, e inserisce quel valore in ``wscd_key_attestation.integrity_assertion``.

Ciascun JWT DEVE essere firmato con la chiave privata della coppia di chiavi di Credenziale che attesta.

**Passi 17-18 (Richiesta di Emissione della Key Attestation)**: L'Istanza del Wallet:

* Costruisce la Key Attestation Request sotto forma di JWT. Questo JWT include ``keys_to_attest``, ``hardware_signature``, ``nonce``, ``c_nonce``, ``hardware_key_tag``, ``cnf``, ``platform``, ``wallet_solution_id``, ``wallet_solution_version`` e altri parametri relativi alla configurazione (vedi :ref:`Tabella del Corpo della Richiesta di Key Attestation <table_ka_request_claim>`). Il claim ``nonce`` contiene il valore ottenuto dal Wallet Provider. Quando richiede una Key Attestation per l'emissione di una Credenziale Digitale, l'Istanza del Wallet DEVE includere anche un claim ``c_nonce`` separato, impostato al valore ricevuto dal Credential Issuer nel Passo 13 del Flusso di Emissione della Credenziale Digitale. La Key Attestation Request DEVE essere firmata utilizzando la chiave privata corrispondente alla chiave pubblica inclusa nella richiesta, tramite il parametro ``cnf`` (primo elemento di ``keys_to_attest``) (:ref:`WP_140–141 <wallet-instance-optional-testcases>`).
* Invia la Key Attestation Request all'endpoint :ref:`wallet-provider-endpoint:Endpoint di Emissione della Key Attestation` del Backend del Fornitore del Wallet.

L'Istanza del Wallet DEVE inviare il JWT firmato della Richiesta di Key Attestation come parametro ``assertion`` nel corpo di una richiesta HTTP all'endpoint :ref:`wallet-provider-endpoint:Endpoint di Emissione della Key Attestation` del Fornitore di Wallet (:ref:`WP_142 <wallet-instance-optional-testcases>`).

**Passi 19-24**: Il Backend del Fornitore del Wallet valuta la Richiesta di Key Attestation e DEVE eseguire i seguenti controlli (:ref:`WP_143 <wallet-instance-optional-testcases>`):

  1. La richiesta DEVE includere tutti i parametri dell'intestazione HTTP richiesti come definito in :ref:`wallet-provider-endpoint:Richiesta di Emissione della Key Attestation` (:ref:`WP_143a <wallet-instance-optional-testcases>`).
  2. La firma della Richiesta di Key Attestation DEVE essere valida e verificabile utilizzando la ``jwk`` fornita (:ref:`WP_143b <wallet-instance-optional-testcases>`).
  3. Il valore ``nonce`` DEVE essere stato generato dal Fornitore di Wallet e non essere stato utilizzato in precedenza (:ref:`WP_143c <wallet-instance-optional-testcases>`).
  4. DEVE esistere un'Istanza del Wallet valida e attualmente registrata associata al ``hardware_key_tag`` (:ref:`WP_143d <wallet-instance-optional-testcases>`). Il Fornitore di Wallet DEVE rifiutare la richiesta quando la Wallet Instance Attestation di quell'Istanza del Wallet è revocata.
  5. La firma di ciascun JWT in ``keys_to_attest`` DEVE essere validata utilizzando la ``jwk`` di quell'elemento. Se ``wscd_key_attestation.attestation`` è presente, il Fornitore di Wallet DEVE validarlo secondo le linee guida del produttore del dispositivo, come definito in :ref:`wallet-solution-requirements:Uso delle API di Key Attestation (OEM)` (:ref:`WP_143h <wallet-instance-optional-testcases>`). Il challenge incorporato in quell'attestazione DEVE essere uguale agli ottetti UTF-8 del ``nonce``. La chiave pubblica attestata DEVE corrispondere alla JWK ``cnf`` dello stesso elemento. Se ``wscd_key_attestation.integrity_assertion`` è presente, il Fornitore di Wallet DEVE validarlo secondo le linee guida del produttore del dispositivo.
  6. Il ``client_data`` DEVE essere ricostruito utilizzando il ``nonce`` e le rispettive thumbprint JWK ``[key_pub_1,...,key_pub_n]``. Il valore del parametro ``hardware_signature`` viene quindi convalidato utilizzando la chiave pubblica della Cryptographic Hardware Key registrata associata all'Istanza del Wallet (:ref:`WP_143e <wallet-instance-optional-testcases>`).
  7. Il dispositivo in uso DEVE essere privo di difetti di sicurezza noti e soddisfare i requisiti minimi di sicurezza definiti dal Fornitore di Wallet.
  8. L'URL nel parametro ``iss`` DEVE corrispondere all'identificatore URL del Fornitore di Wallet (:ref:`WP_143g <wallet-instance-optional-testcases>`).

Al completamento con successo di tutte le verifiche, il Fornitore di Wallet emette una Key Attestation valida per almeno un mese (:ref:`WP_144 <wallet-instance-optional-testcases>`).

**Passo 25 (Risposta di Emissione della Key Attestation)**: Al completamento con successo, il Fornitore di Wallet DEVE restituire una risposta di conferma con codice di stato ``200`` e Content-Type ``application/json``. La risposta DEVE contenere le Key Attestations firmate dal Fornitore di Wallet in formato JWT. L'Istanza del Wallet DEVE eseguire la verifica di sicurezza e integrità delle Key Attestations ricevute, insieme alla verifica di fiducia già valutata sull'Emittente (:ref:`WP_030–031 <wallet-instance-testcases>`).


Di seguito è riportato un esempio non normativo della risposta.

.. literalinclude:: ../../examples/shared/wallet-attestation-issuance-2.http
   :language: http



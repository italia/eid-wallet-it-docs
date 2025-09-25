.. include:: ../common/common_definitions.rst


Flusso di Prossimità
====================

Questa sezione descrive come un'Istanza di Relying Party richiede la presentazione di una Credenziale *mdoc-CBOR* a un'Istanza del Wallet come specificato nella *Specifica ISO 18013-5*.

La fase di presentazione di alto livello è strutturata in tre ampie sotto-fasi come illustrato nella figura seguente:

.. plantuml:: plantuml/credential-presentation-high-level-flow.puml
    :width: 90%
    :alt: La figura illustra il Flusso di Presentazione di Alto Livello in prossimità.
    :caption: `Flusso di Presentazione di Alto Livello in prossimità. <https://www.plantuml.com/plantuml/svg/VLBHYjim47pNLsppv8CcHzjxBELeOaYXK9DSANqoEccmHMN9bUHSJUc_T-qanWr9zIAyEpCxE_9ZJ3Aahh6qDLMz_8m3B1K14Ix9PBoZefOHufLnodOQz7xzSBz-ADU-QRrZq0SXjfysURb_odVvbwVlHPxT2P5Cig35VpKNGXG8qRkiYmYlQV6LhmNVZVQAQcyrVxAM-EWxfsNeitQcKRQ31gEl2D_HRq5y9fEPni4eb72LhD1mXOblLhGPovHFvM7y7geBe5Zxa9P1kWgal7DGuuHdf1V0qJTfBH99fsa7snjNKS59zeD2pg4-MnDhH3BE92CjnQEggYLBMTwB-5ouZ8XnM0rd_idfsnNjZotAvwrnbbEXRnFqtEIBIJKl80ENJwBq0_rnknIfQyz-CD5FkElEb6-QpXarfimgxrRSd9LeUSvoXnGC3jB-Qsvyqu2V7MAw3uYi6q7ufUenu8EHbmanVSlfMiIPIIsJd5XizOyGd7wvEVr2rvxv-009aU43TfTTGTrAtaBgICbFt1l0otpWk3kEV8JJNMF_0W00>`_

Le sotto-fasi sono descritte di seguito:

  1. **Device Engagement**: Questa sottofase inizia quando l'Utente viene invitato a divulgare attributi specifici dagli mdoc. L'obiettivo di questa sottofase è stabilire un canale di comunicazione sicuro tra l'Istanza del Wallet e l'Istanza di Relying Party, in modo che le richieste e le risposte mdoc possano essere scambiate durante la sottofase di comunicazione.
  I messaggi scambiati in questa sottofase sono trasmessi attraverso tecnologie a corto raggio per limitare la possibilità di intercettazione e intercettazione. I dati di Device Engagement possono essere trasferiti utilizzando tecnologie QR code o NFC.

  2. **Stabilimento della Sessione**: Durante la fase di stabilimento della sessione, l'Istanza di Relying Party configura una connessione sicura. Tutti i dati trasmessi su questa connessione sono crittografati utilizzando una chiave di sessione, che è nota sia all'Istanza del Wallet che all'Istanza di Relying Party in questa fase.
  La sessione stabilita PUÒ essere successivamente terminata in base alle condizioni dettagliate in [`ISO18013-5`_ #12.2.4].

  3. **Comunicazione - Device Retrieval**: L'Istanza di Relying Party crittografa la richiesta mdoc con la chiave di sessione appropriata e la invia all'Istanza del Wallet insieme alla sua chiave pubblica in un messaggio di stabilimento della sessione. L'Istanza del Wallet utilizza i dati dal messaggio di stabilimento della sessione per derivare la chiave di sessione e quindi per decrittografare la richiesta mdoc.
  Durante la sottofase di comunicazione, l'Istanza di Relying Party ha l'opzione di richiedere informazioni dall'Istanza del Wallet utilizzando richieste e risposte mdoc. La modalità principale di comunicazione è il canale sicuro stabilito durante la configurazione della sessione. L'Istanza del Wallet crittografa la risposta mdoc utilizzando la chiave di sessione e la trasmette all'Istanza di Relying Party mobile tramite un messaggio di dati di sessione.


Le Istanze di Relying Party e Wallet registrate nell'ecosistema IT-Wallet DEVONO supportare almeno:

- *Flusso di Device Retrieval supervisionato* dove una Relying Party umana supervisiona il processo di verifica di persona, o *flusso non supervisionato* dove la verifica potrebbe avvenire attraverso sistemi automatizzati senza supervisione umana.
- *Autenticazione dell'Istanza di Relying Party* seguendo i meccanismi definiti nella `ISO18013-5`_ per l'*autenticazione del lettore*.
- *Document Type* e *Namespaces* domestici definiti in questa specifica tecnica in aggiunta a quelli già definiti nella `ISO18013-5`_ per l'mDL (vedere :ref:`credential-data-model:mdoc-CBOR Credential Format` per maggiori dettagli).
- *Validazione dell'Istanza del Wallet* attraverso l'Attestato del Wallet.

La tabella seguente mostra le tecnologie di Device Engagement supportate, specificando quali sono obbligatorie.

.. list-table::
   :class: longtable
   :widths: 20 15 15 25 25
   :header-rows: 2

   * - **Tecnologia di trasmissione**
     - **ISO 18013-5**
     - **ISO 18013-5**
     - **IT Wallet**
     - **IT Wallet**
   * -
     - **Istanza del Wallet**
     - **Istanza RP**
     - **Istanza del Wallet**
     - **Istanza RP**
   * - **QR code**
     - C\ :sup:`a`
     - M
     - DEVE
     - C – DEVE se il dispositivo è dotato di una fotocamera o lettore QR code e BLE.
   * - **NFC**
     - C\ :sup:`a`
     - M
     - RACCOMANDATO
     - C – DEVE se il dispositivo è dotato di un lettore NFC.

Legenda: C = Condizionale | M = Obbligatorio | :sup:`a`\ Il supporto per almeno uno di questi metodi è obbligatorio

La tabella seguente mostra le tecnologie di Device Retrieval supportate, specificando quali sono obbligatorie.

.. list-table::
   :header-rows: 2
   :widths: 20 15 15 25 25
   :class: longtable

   * - **Tecnologia di trasmissione**
     - **ISO 18013-5**
     - **ISO 18013-5**
     - **IT Wallet**
     - **IT Wallet**
   * - 
     - **Istanza del Wallet**
     - **Istanza RP**
     - **Istanza del Wallet**
     - **Istanza RP**
   * - **BLE**
     - C\ :sup:`a`
     - M
     - DEVE
     - C – DEVE se il dispositivo è dotato di una fotocamera o lettore QR code e BLE.
   * - **NFC**
     - C\ :sup:`a`
     - M
     - RACCOMANDATO
     - C – DEVE se il dispositivo è dotato di un lettore NFC.
 
Legenda: C = Condizionale | M = Obbligatorio | :sup:`a`\ Il supporto per almeno uno di questi metodi è obbligatorio

.. note::
   Dalla seconda edizione, versione 3, `ISO18013-5`_ non definisce o supporta Server Retrieval come opzione di trasporto. Sono specificati solo metodi di recupero di prossimità (NFC, BLE e opzionalmente Wi-Fi Aware). Pertanto, Server Retrieval non è considerato in questo flusso.


La figura seguente illustra il flusso di basso livello conforme a ISO 18013-5 per il flusso di prossimità.

.. _fig_High-Level-Flow-ITWallet-Presentation-ISO-updated:
.. plantuml:: plantuml/credential-presentation-flow.puml
    :width: 99%
    :alt: La figura illustra il Flusso di Presentazione di Basso Livello in prossimità.
    :caption: `Flusso di Presentazione di Basso Livello in prossimità. <https://www.plantuml.com/plantuml/svg/ZLJBRjim4BppAnRgfGQS5kYn28muZki6JTFKJf1BBXIrjeb8IvKFAVxxBacvTLe7oKtIScTsPeSwSrvQ7vfQoE0DXQP4AuHKtbYuSsX1EWX2j7n8AzrAyb3Soxf63tUaVH7h_VFoyWOkYM59OIftGeIJIVyPVhH8uBS80y3-LAJJdVJ8IE4q7StKWGyJ0qkl3K6vEzOCF2XN9DolPjCzKsftMAFoBZMrrZpfHliTFw5Zq0ov3gJYWwov94phuRkaIhBu7UWrh3osy0cq0p8UMhHhOnki8bzYwtdOyEAmwGXI9KIVXbeWeOqg2Nl0TeiDlzRmY3oKr1OUw7rHp2-mqmg_uUx3ZTLTKOpX-STG5iL82CiJiVQEcVjn1--kBXTVRnVB-VnQd9QJwUZqOpdXpjmufutSC1tveW2M9m6Vr5RIPa3ukGHbgcJbzPTPd3d1Yx-BuHrs9vFkhIAMA2kq_uWu-9X5PCIPQTh0W0wTYyunr9xinY8d2tcvJc-8ZUVb09AokzR7D--jBcFl0rdy5T1vOFPL1ffpFifQkstM_QfdvtlFZlT3mv_PnJ_MLHdf_6e--COALE1fOvcmFh1n2C0nfRboWKdJo-HHEBFfDUUI8ntja9x98dJAu7BGBrkEUiSRuQZkiwvfCro6GzFSc6rJXZoVS63MO76ZdRSvlmhvHgzZcd6uKzC1-JKVPzd75Sj_QN4yLcl8uS6sBZYLl2GGlVPR6BRvRDnCADzaU8xFVwvcal5H9sDogtHReDHKiMUZDBNQedg4fZ8AMBokueyYNNmc663X5csZAHadAZouD0SllJZZ-VX7-ni0>`_


**Passo 1**: L'Utente apre l'Istanza del Wallet avviando il processo.

**Passo 2**: L'Utente si autentica all'Istanza del Wallet. Questo può essere fatto dall'Istanza del Wallet o da un'Applicazione Crittografica Sicura per il Portafoglio (WSCA). È un prerequisito per accedere ai dati sensibili e presentare attributi.

**Passo 3**: L'Utente seleziona la funzionalità di presentazione di prossimità.

**Passo 4**: [Opzionale] Se l'autenticazione iniziale nel Passo 2 non è stata effettuata tramite WSCA, PUÒ essere richiesta un'autenticazione separata tramite WSCA.

**Passo 5**: L'Istanza del Wallet genera una nuova coppia di chiavi a Curva Ellittica effimera per la comunicazione sicura. La chiave pubblica (``EDeviceKey.Pub``) sarà scambiata con l'Istanza di Relying Party per derivare una chiave di sessione condivisa, che viene poi utilizzata per la crittografia della sessione. Questo fa parte del processo di device engagement.

.. admonition:: Box A

   L'Istanza del Wallet e l'Istanza di Relying Party scambiano dati di *Device Engagement* tramite QR code o tramite NFC Connection Handover.  

   Fare riferimento a:

   - Sez 8.2.2.1 per ``DeviceEngagement`` tramite QR code
   - Sez 8.2.2.2 per ``DeviceEngagement`` tramite NFC

**Passo 6**: L'Istanza di Relying Party genera la sua coppia di chiavi effimera (``EReaderKey.Priv``, ``EReaderKey.Pub``). La chiave privata (``EReaderKey.Priv``) DEVE essere mantenuta segreta, e la chiave pubblica (``EReaderKey.Pub``) DEVE essere utilizzata nello stabilimento della sessione.

**Passo 7**: L'Istanza del Wallet e l'Istanza di Relying Party DEVONO derivare indipendentemente le chiavi di sessione utilizzando la loro chiave effimera privata e la chiave effimera pubblica dell'altra parte attraverso un protocollo di accordo delle chiavi. Questo garantisce la crittografia della sessione. In questo particolare passo, l'Istanza di Relying Party DEVE calcolare la sua chiave di sessione.

**Passo 8**: L'Istanza di Relying Party DEVE preparare un messaggio ``SessionEstablishment``. Questo messaggio DEVE essere firmato dall'Istanza di Relying Party (autenticazione del lettore mdoc come specificato in [`ISO18013-5`_ #12.5]) e crittografato utilizzando le chiavi di sessione derivate nel passo precedente. Il messaggio ``SessionEstablishment`` DEVE includere la ``EReaderKey.Pub`` e una richiesta per attributi specifici.

Di seguito è riportato un esempio non normativo utilizzando la notazione diagnostica di un messaggio ``SessionEstablishment`` codificato CBOR che contiene una richiesta mdoc per un Attestato del Wallet insieme a una Credenziale Digitale mDL.

.. literalinclude:: ../../examples/iso-session-establishment.txt
  :language: text

.. admonition:: Box B

   L'Istanza di Relying Party DEVE trasmettere il messaggio ``SessionEstablishment`` crittografato e firmato all'Istanza del Wallet tramite una connessione sicura NFC o BLE che è stata stabilita basandosi sulle informazioni di device engagement.
   Fare riferimento a:

   - Sez 8.2.2.3 per ``SessionEstablishment`` tramite BLE, e
   - Sez 8.2.2.5 per ``SessionEstablishment`` tramite NFC

**Passo 9**: L'Istanza del Wallet DEVE calcolare la chiave di sessione, come descritto nel Passo 7.

**Passo 10**: Al ricevimento del messaggio ``SessionEstablishment``, l'Istanza del Wallet DEVE decrittografarlo utilizzando la chiave di sessione condivisa e DEVE verificare la firma dell'Istanza di Relying Party (autenticazione del lettore mdoc come specificato in [`ISO18013-5`_ #12.5]) per garantire la sua autenticità.

**Passo 11**: L'Istanza del Wallet DEVE decrittografare la richiesta di attributi e DEVE richiedere il consenso dell'Utente per rilasciare gli attributi richiesti. DEVE anche visualizzare i contenuti del Certificato di Registrazione della Relying Party per garantire trasparenza riguardo agli attributi richiesti e al suo scopo registrato.

**Passo 12**: L'Utente esamina la richiesta e le informazioni di registrazione della Relying Party e quindi approva la presentazione degli attributi richiesti.

.. admonition:: Box C

   Dopo aver ricevuto l'approvazione dell'Utente, l'Istanza del Wallet DEVE recuperare le Credenziali Digitali mdoc richieste. Deve quindi preparare un messaggio ``SessionData`` contenente queste Credenziali Digitali, e DEVE firmare i dati di autenticazione richiesti (come parte del processo di autenticazione mdoc, come specificato in [`ISO18013-5`_ #12.4]). DEVE crittografarlo utilizzando le chiavi di sessione stabilite prima di trasmetterlo all'Istanza di Relying Party tramite il canale BLE sicuro. La firma garantisce il binding del dispositivo e l'integrità dei dati. La risposta mdoc DEVE essere codificata in CBOR, con la sua struttura delineata in [`ISO18013-5`_ #10.3].
   Fare riferimento a:

   - Sez 8.2.2.4 per ``SessionData`` tramite BLE, e
   - Sez 8.2.2.5 per ``SessionData`` tramite NFC

Di seguito è riportato un esempio non normativo utilizzando la notazione diagnostica di un ``SessionData`` codificato CBOR che contiene la risposta mdoc di un Attestato del Wallet e una Credenziale Digitale mDL.

.. literalinclude:: ../../examples/iso-session-data.txt
  :language: text

**Passo 13**: L'Istanza di Relying Party riceve il ``SessionData``, quindi DEVE decrittografarlo, e DEVE verificare la firma dell'Istanza del Wallet per garantire l'integrità dei dati e che provenga dal dispositivo previsto (binding del dispositivo). DEVE anche controllare la validità dell'mdoc, inclusa la firma del suo Fornitore di Credenziale. Nel caso di Credenziali Digitali di lunga durata, DOVREBBE anche controllare lo stato di revoca utilizzando il `TOKEN-STATUS-LIST`_.

**Passo 14**: Una volta completato lo scambio di dati, una delle parti può terminare la sessione. La sessione può essere terminata inviando il codice di stato per la terminazione della sessione in un messaggio ``SessionData``; questo può essere inviato insieme a una richiesta o risposta mdoc [`ISO18013-5`_ #12.2.4]. Se viene utilizzato BLE, questo può comportare l'invio di un codice di stato per la terminazione della sessione o il comando "End". In questo scenario, il Client GATT (Istanza di Relying Party) DEVE annullare l'iscrizione dalle caratteristiche e disconnettersi dal server GATT (Istanza del Wallet).

**Considerazione Finale**: Il flusso di presentazione si è concentrato sullo scambio tecnico di dati in contesti di prossimità. È cruciale riconoscere che i flussi di prossimità supervisionati che coinvolgono un verificatore umano svolgono un ruolo vitale in molti casi d'uso (ad esempio, verifica dell'età in un negozio, controllo dell'identità da parte delle forze dell'ordine). L'elemento umano aggiunge un livello di verifica dell'identità attraverso l'ispezione visiva e il confronto, contribuendo agli aspetti di User Binding e garanzia di autenticazione complessiva non completamente catturati in un flusso di presentazione puramente tecnico.

.. note::
   Durante la presentazione di prossimità l'Istanza del Wallet potrebbe non essere in grado di recuperare un Attestato del Wallet aggiornato, in questo caso, l'Istanza del Wallet DOVREBBE inviare l'ultima versione dell'Attestato del Wallet. È lasciato alla Relying Party determinare se una presentazione con un Attestato del Wallet valido ma scaduto è valida o meno.

.. _sec-deviceengagement-qr:

``DeviceEngagement`` tramite QR Code
-------------------------------------
La figura seguente illustra il flusso di basso livello conforme a ISO 18013-5 per ``DeviceEngagement`` tramite QR Code corrispondente al Box A nella Figura :ref:`fig_High-Level-Flow-ITWallet-Presentation-ISO-updated`.

.. _fig_DeviceEngagement-QR:
.. plantuml:: plantuml/device-engagement-over-qr-code.puml
    :width: 90%
    :alt: La figura illustra il Flusso di Presentazione Device Engagement tramite QR Code in prossimità.
    :caption: `Device Engagement tramite QR Code. <https://www.plantuml.com/plantuml/svg/PP0n3i8m34NtdCBAtWimL4Z0m0P5YDaaLcifTQlMIQvFbAK5F5Zoz__Fae-hug9n30QZJXB7Doq6IjKsbnqxdb4Kx0j388Mdi5h05VA_fRl1LGfH75LBCXiBdN92fPghIcxQT837C6NGWU3UmMdo12mkHC_IWxLdIkpe8ZtsD9AejT-iLCVKD6qk98Uo9sstFVqaTa8sHn9VFl01>`_

**Passo 1**: L'Istanza del Wallet presenta un QR Code all'Istanza di Relying Party. Il QR code DEVE contenere un URI con "mdoc:" come schema e la struttura ``DeviceEngagement`` specificata nella Sezione 9.1 codificata utilizzando base64url-without-padding, secondo RFC 4648, come percorso.

Esempio Non Normativo con BLE come Device Retrieval
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Di seguito è riportato un esempio non normativo utilizzando la notazione diagnostica di un ``DeviceEngagement`` codificato CBOR che utilizza QR per il device engagement e Bluetooth Low Energy (BLE) per il recupero dei dati.

 .. literalinclude:: ../../examples/iso-device-engagement-BLE.txt
  :language: text

Esempio Non Normativo con NFC come Device Retrieval
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Di seguito è riportato un esempio non normativo utilizzando la notazione diagnostica di un ``DeviceEngagement`` codificato CBOR che utilizza QR per il device engagement e NFC per il recupero dei dati.

 .. literalinclude:: ../../examples/iso-device-engagement-NFC.txt
  :language: text

**Passo 2**: Il verificatore utilizza la sua Istanza di Relying Party per scansionare il QR code e recuperare i dati ``DeviceEngagement`` dall'mdoc. DEVE selezionare una delle tecnologie di trasmissione tra quelle fornite nella struttura ``DeviceEngagement``.

.. _sec-deviceengagement-nfc:

``DeviceEngagement`` tramite NFC
---------------------------------
La figura seguente illustra il flusso di basso livello conforme a ISO 18013-5 per ``DeviceEngagement`` tramite NFC corrispondente al Box A nella Figura :ref:`fig_High-Level-Flow-ITWallet-Presentation-ISO-updated`. 

.. _fig_DeviceEngagement-NFC:
.. plantuml:: plantuml/device-engagement-over-nfc.puml
    :width: 90%
    :alt: La figura illustra il Flusso di Presentazione Device Engagement tramite NFC in prossimità.
    :caption: `Device Engagement tramite NFC. <https://www.plantuml.com/plantuml/img/dLDDJ-Cm4BtFhtZoXUOGJfooAaA28hWKr7QrPpSUWYNNpjfEilpxdPIIRRLKIEGG9NdpFkObkKbPnzpj7Eak1z_jjXo9g9M7jhQjzXdgbtQECtvwcnLqmd0Ahvxnw4N6rxo7Uo9TPzlhp38wNVPqWR8iiRo_XU7UrWpsZMvunw8o4m6HH8Zmt8HiXMAAaK3Ry0VgKvOYGBkCzJltLNiJUiaFEVgol1ugh5WRF1m0hDbnBMQRjvPnXOrk2XbcbnZBoVLKPn2Tlf8DhQ0Eoxl5FRGHDDl4QPf5uhXFDrDTz9L_gQlagmzK5OTCOwGfpOf_Tvp6tRks3N6qhdMCbcCg3jwZzN_fbRhRDx7uLuI2qLaND6xZ3O7a32bENkN5V0wbrfoI3NuXDM-TJQyVh2vQtnmlFxdDGfk5eLs1-Pn8xhuZ8_vuykuDzWN3-tSqjMTmM1pMuxEbVc2pN3nFrTg4JbYNrAEyXZJvrB8_7JcNSAAinsA-dBfr8PqNEx6aiMeYmqSV-j7DG3U2o__r5m00>`_

``DeviceEngagement`` tramite NFC è basato sulla Specifica Tecnica NFC Forum Connection Handover, Versione 1.5. È supportata solo la modalità Reader/Writer utilizzando un Tag di Tipo 4. Il protocollo Connection Handover è sempre avviato dall'Istanza di Relying Party, che assume il ruolo di Handover Requester. L'Istanza del Wallet agisce come NFC Tag Device e l'Istanza di Relying Party come NFC Reader Device. L'Istanza del Wallet DEVE utilizzare Static Handover o Negotiated Handover:
- **Static Handover**: L'Istanza di Relying Party recupera un messaggio Handover Select direttamente dal Tag di Tipo 4 dell'Istanza del Wallet. Questo messaggio contiene almeno un Alternative Carrier Record, ognuno indicante un metodo di recupero supportato dall'Istanza del Wallet. L'Istanza di Relying Party DEVE selezionare una di queste tecnologie di trasmissione. (vedere Passo 1)
- **Negotiated Handover**: L'Istanza del Wallet include il servizio ``urn:nfc:sn:handover`` in un Service Parameter Record del messaggio NDEF (NFC Data Exchange Format) iniziale. Selezionando questo servizio, l'Istanza di Relying Party invia una Handover Request con un Alternative Carrier Record per ogni carrier che supporta. L'Istanza del Wallet risponde con un messaggio Handover Select contenente esattamente un carrier selezionato. (Vedere Passi 2-4)

**Passo 1**: L'Istanza di Relying Party legge il Tag NFC di Tipo 4 del Wallet per ottenere un messaggio Handover Select, che include: 
- Alternative Carrier Record è un record NDEF all'interno di un messaggio Handover Select o Handover Request. Punta a una possibile tecnologia di comunicazione (chiamata "carrier"), come NFC o BLE. Informa il lettore sul carrier supportato e un puntatore (Auxiliary Data Reference) a informazioni più dettagliate. L'Alternative Carrier Record per la tecnologia di trasmissione device retrieval NFC deve fare riferimento al Carrier Configuration Record con il riferimento ID "nfc".
- Carrier Configuration Record fornisce i parametri tecnici necessari per utilizzare effettivamente quel carrier. Per la tecnologia di trasmissione device retrieval NFC, DEVE avere il tipo "iso.org:18013:nfc" e il riferimento ID "nfc". Il contenuto binario del Carrier Configuration Record DEVE essere codificato secondo la Tabella 1 di [`ISO18013-5`_ #9.2.2].

Per esempio:
Per NFC, questo definisce le lunghezze massime di comando/risposta APDU (Application Protocol Data Unit); 
Per BLE, definisce l'UUID del servizio dell'Istanza del Wallet, gli UUID delle caratteristiche, la dimensione MTU (Maximum Transmission Unit) e parametri di connessione opzionali; 
Se è supportato il ``SessionEstablishment`` anticipato, elenca anche il nome del servizio TNEP (Tag NDEF Exchange Protocol) utilizzato per inviare il messaggio ``SessionEstablishment`` durante l'handover.

.. note::
   Per la tecnologia di trasmissione device retrieval NFC, i contenuti dell'Alternative Carrier Record e del/dei Carrier Configuration Record DEVONO essere conformi a [`ISO18013-5`_ #9.2.2]. Per la tecnologia di trasmissione device retrieval BLE, i contenuti dell'Alternative Carrier Record e del/dei Carrier Configuration Record devono essere conformi a [`ISO18013-5`_ #11.1.2].

- Auxiliary Data Record DEVE trasportare la struttura DeviceEngagement dall'Istanza del Wallet all'Istanza di Relying Party come parte del record NDEF ausiliario nel messaggio Handover Select. Questo record ha il tipo ``iso.org:18013:deviceengagement``, il riferimento ID "mdoc", e utilizza il formato di tipo esterno del forum NFC (``0x04``). Per ogni record Alternative Carrier, l'Auxiliary Data Reference DEVE puntare al record NDEF contenente la Struttura ``DeviceEngagement``. 

**Passo 2**: L'Istanza di Relying Party legge il messaggio NDEF (NFC Data Exchange Format) Iniziale dell'Istanza del Wallet, che contiene un service parameter record per ``urn:nfc:sn:handover``, indicando che il Wallet supporta Negotiated Handover. 

**Passo 3**: L'Istanza di Relying Party invia una Handover Request all'Istanza del Wallet elencando i carrier supportati. 

**Passo 4**: L'Istanza del Wallet restituisce Handover Select costruito in risposta al messaggio Handover Request ricevuto. I contenuti del messaggio Handover Select sono gli stessi del Passo 1.

.. note::
   L'uso di Negotiated Handover per il device engagement consente la negoziazione dei metodi di trasferimento. Per BLE, consente inoltre la negoziazione delle chiavi utilizzate dal livello di trasmissione. Questo fornisce un'esperienza utente migliorata e migliora la sicurezza della trasmissione dei dati [`ISO18013-5`_ #9.2.1].

.. note::
   Procedere solo se le Capabilities di ``DeviceEngagement`` includono ``HandoverSessionEstablishmentSupport`` impostato su ``true``. Altrimenti, saltare il ``SessionEstablishment`` anticipato. Il ``SessionEstablishment`` anticipato viene inviato tramite un servizio TNEP dedicato; lo stesso ``SessionEstablishment`` DEVE anche essere inviato nuovamente durante il device retrieval e DEVE corrispondere. Se non corrisponde, l'Istanza del Wallet termina. Se il ``SessionEstablishment`` anticipato non riesce a essere inviato, procedere normalmente.

**Passo 5**: [Opzionale] L'Istanza di Relying Party apre il servizio TNEP denominato [urn:placeholder] con l'Istanza del Wallet durante l'handover negoziato per consegnare il messaggio ``SessionEstablishment`` anticipato.

**Passo 6**: L'Istanza di Relying Party invia ``SessionEstablishment`` (ad esempio, ``EReaderKey`` + ``DeviceRequest`` crittografato). L'Istanza del Wallet lo elabora; il device retrieval non è ancora iniziato.

**Passo 7**: L'Istanza di Relying Party chiude il servizio TNEP.

.. note::
   Supponiamo che un messaggio ``SessionEstablishment`` opzionale venga inviato durante Negotiated Handover (Passo 5). In tal caso, l'Istanza del Wallet DEVE verificare che corrisponda al messaggio ``SessionEstablishment`` ricevuto durante Device Retrieval (utilizzando BLE o canale sicuro NFC). Questa verifica è richiesta per garantire un corretto Session Binding.

Esempio Non Normativo
^^^^^^^^^^^^^^^^^^^^^^
Di seguito è riportato un esempio non normativo di una struttura ``DeviceEngagement`` per Device Retrieval tramite BLE e NFC.
  .. literalinclude:: ../../examples/iso-device-engagement-NFC-BLE.txt
   :language: text

``SessionEstablishment`` tramite BLE
-------------------------------------
La figura seguente illustra il flusso di basso livello conforme a `ISO18013-5`_ per ``SessionEstablishment`` tramite BLE corrispondente ai Box B nella Figura 8.10.

.. _fig_SessionEstablishment-BLE:
.. plantuml:: plantuml/session-establishment-over-ble.puml
    :width: 90%
    :alt: La figura illustra il Flusso di Presentazione Session Establishment tramite BLE in prossimità.
    :caption: `Session Establishment tramite BLE. <https://www.plantuml.com/plantuml/svg/ZLHDRzim3BthLn2-r3aaG3PWXs8RYYu15c0PXcRfBhimCki8ioLDakNq5-r_x9UDabitmVeL184Zak_nFLA-y05TwDf6O1UCxjeTEI4idocfBEe0nGzi6WgmrIeKW1xwq_3LDrXfHj6ISZWAWJAeY84uTNpaupFuyDI7OvTVbY2DriGLHWCnvAvHVjyIivGtphImtQuMu4YIYbI1qh2Wg2J1KjTOKqgSF4iYTkO0HIBo53eBfJCDJR7MnhEUII40ullfn_uSblViC6JBpX78FN9xZI1T0IEz9EYQdBgvPKsEMmvWYHn4XR2gaY86SsmEvoHkAF_-cSzdyzdRsPldDMG9zn0aVq7PLaP2J6IAF8GzZPIEi2ANTV7Ns01N-MHeJKbCJdEapve_cTPsF2awM2vcWpFB48xdkVJntYCs7Pt08BirpccewLNOZz0ZCamFmDZbaBDMliKWznFuJgvLEktDwLfm3RlFl_0mXPXfYs93tdFAydXnYW8CM_FO54Nouwu6BfMkbAx5866TcdWQiULZthS7XLNdk1X-QlXAjGaAatkVKLUPEojFO_clZZTu4yZ2Ep4QiRxBUOKLoGXnDWndazn0yAhMZClCR9DqjpOruiXRepr1EIfQOC2Yc737kJb7lpk-Rwao1ATsl0L-z4s8YevkyT6VNbmmBRyx_W40>`_
    
**Passo 1**: L'Istanza del Wallet e l'Istanza di Relying Party stabiliscono una connessione BLE sicura [`ISO18013-5`_ #11.1]. L'Istanza di Relying Party (central) si connette all'Istanza del Wallet (peripheral) utilizzando l'UUID del servizio dell'Istanza del Wallet fornito da DeviceEngagement, quindi scopre servizi/caratteristiche e abilita le notifiche secondo necessità.

**Passi 2-5**: [Opzionale] L'Istanza del Wallet avvia la verifica preparandosi a controllare l'identità della Relying Party tramite la caratteristica Ident, che è una caratteristica BLE GATT che trasporta un valore identificatore come descritto in [`ISO18013-5`_ #11.1.3.2]. L'Istanza del Wallet deriva il valore Ident atteso e legge la caratteristica Ident della Relying Party, confrontandola con l'Ident atteso, e terminando la connessione BLE se può verificarsi una mancata corrispondenza.

.. note::
   Lo scopo della caratteristica Ident è solo verificare se l'Istanza del Wallet è connessa all'Istanza di Relying Party corretta prima di iniziare il device retrieval. Se l'Istanza del Wallet è connessa all'Istanza di Relying Party sbagliata, lo stabilimento della sessione fallirà. Connettersi e disconnettersi a un'Istanza di Relying Party richiede una quantità relativamente grande di tempo; pertanto, è più veloce implementare metodi per identificare l'Istanza di Relying Party corretta [`ISO18013-5`_ #11.1.3.1].

**Passo 6**: L'Istanza di Relying Party invia il messaggio ``SessionEstablishment`` crittografato (include ``EReaderKey`` e ``DeviceRequest`` crittografato) tramite la connessione BLE stabilita.

**Passi 7-8**: [Opzionale] Se l'Unità di Wallet riceve il messaggio ``SessionEstablishment`` durante Negotiated Handover, l'Unità di Wallet DEVE verificare se questo messaggio ``SessionEstablishment`` corrisponde al messaggio ``SessionEstablishment`` ricevuto durante la fase di device retrieval (cioè, Passo 6). In caso di mancata corrispondenza, l'Unità di Wallet deve terminare la connessione BLE [`ISO18013-5`_ #9.2.3].

``SessionData`` tramite BLE
----------------------------
La figura seguente illustra il flusso di basso livello conforme a `ISO18013-5`_ per ``SessionData`` tramite BLE corrispondente ai Box C nella Figura 8.10.

.. _fig_SessionData-BLE:
.. plantuml:: plantuml/session-data-over-ble.puml
    :width: 90%
    :alt: La figura illustra il Flusso di Presentazione Session Data tramite BLE in prossimità.
    :caption: `Session Data tramite BLE. <https://www.plantuml.com/plantuml/svg/LO-n3i8m34JtV8ML2GP-W05L20Oa1aI5M5ZSr898hLjYfn5_Zs50PRjtT_B9bIWcpNtdCEl0kMyeEJUQ5qCSaHNy5RkE52uSrGCAbF_uV883snKEz8qdvp1ed539gZzfTbbjfZNKn2qWIBmpcJ0W3kargb4Y6GSMWeNtDOd4WNUewFqIRboYFgpnp2IVBggcs6GbWM6Y1DlZthcMPeCpAAwoMNlp3G00>`_

**Passo 1**: L'Istanza del Wallet invia l'APDU finale contenente l'ultimo blocco DeviceResponse (con attributi richiesti) o un codice di stato, dopo il quale la sessione può terminare o continuare con una nuova richiesta.


``SessionEstablishment`` tramite NFC
-------------------------------------
.. note::
   Se il device engagement viene avviato tramite un QR code, l'Istanza di Relying Party non ha un modo standardizzato per segnalare la sua intenzione di utilizzare NFC per il successivo trasferimento di dati. Questo potrebbe portare a una scarsa esperienza utente, poiché l'Utente potrebbe non essere consapevole di dover utilizzare NFC. Questo problema viene evitato quando NFC viene utilizzato per il device engagement, poiché stabilisce implicitamente il metodo di trasferimento dati [`ISO18013-5`_ #8.2.5].

.. note::
   A causa della velocità di trasferimento dati limitata di NFC, se è richiesta una grande quantità di dati per una transazione, potrebbe non essere né pratico né ragionevole per un Utente mantenere il dispositivo all'interno del campo RF dell'Istanza di Relying Party per la durata della transazione. Inoltre, a causa della perdita di segnale quando un dispositivo lascia il campo RF, qualsiasi interazione dell'Utente con l'Istanza del Wallet, causando l'uscita dell'Istanza del Wallet dal campo RF, richiede l'avvio di una nuova transazione. Questo può essere evitato facendo sì che tutte le interazioni dell'Utente con l'Istanza del Wallet vengano effettuate mentre l'Istanza del Wallet rimane nel campo, o se l'Istanza del Wallet non richiede alcuna interazione dell'Utente mentre è nel campo RF [`ISO18013-5`_ #8.2.5].

   La figura seguente illustra il flusso di basso livello conforme a `ISO18013-5`_ per ``SessionEstablishment`` tramite NFC corrispondente al Box B nella Figura 8.10.

.. _fig_SessionEstablishment-NFC:
.. plantuml:: plantuml/session-establishment-over-nfc.puml
    :width: 90%
    :alt: La figura illustra il Flusso di Presentazione Session Establishment tramite NFC in prossimità.
    :caption: `Session Establishment tramite NFC. <https://www.plantuml.com/plantuml/svg/ZP9BJyCm383l-HLMJzjX9pWX3G6b20HxYF6uSCbIRutKE25nM_ZtE6n2GsWIjyJv77-ESv5OH-vSgtJ7dZgtngXKa9WrDcXYA5vrsoB3Crc6qVAkBCS5w0J3R-fn2NSabv51eShh7TGhfGtRNZDAmizImjCfWAkzWSiGMciqMq-mmXRDzsewLJrCpc4uWqL0sg7w07sZLVLGbKzWl7EQQZLal3-3lQxnjB7H9G57Ytlm4IpLEHaJE1yHQiqQsCC6sJJZRw6YM65ASdibZQnRcng7n4LnQ5EHYP-1iJvEHtplCF4RLVENwc6nh8uvHap1Kvt-g-W3mxucN6MMjcgOd8lLJ0jntCX9M6zH2XgqlRZNNPHaUHkOuzQprRcXMr7qFKOOB3V03VxDip8ZnW0dazFSp4TkPZJRKpERNFOOmnD6PobFUdvJvb7GRgmAvH5KZGT_uc3Jgmivbx_u1G00>`_

Definizioni (Acronimi e Comandi)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::
   :class: longtable
   :widths: 15 85
   :header-rows: 1

   * - **Acronimo/Comando**
     - **Descrizione**

   * - **PICC**
     - Proximity Integrated Circuit Card, implementata dalle Unità di Wallet che agiscono come tag NFC.

   * - **PCD**
     - Proximity Coupling Device, implementato dalle istanze di Relying Party utilizzando scambi `APDU`.

   * - **AID**
     - Application Identifier, ID univoco utilizzato nel comando SELECT `APDU` per coinvolgere l'Istanza del Wallet.

   * - **APDU**
     - Application Protocol Data Unit, un formato di messaggio standard per la comunicazione tra Istanza di Relying Party (PCD) e Wallet (PICC) costituito da Command APDU (ad esempio, `SELECT`, `ENVELOPE`, `GET RESPONSE`) dal lettore e Response `APDU` dal wallet, che includono scambio di dati e fine scambio utilizzando status words (`SW1/SW2`).

   * - **SELECT APDU**
     - Comando che apre l'Istanza del Wallet tramite `AID`. La risposta include File Control Information (FCI) e Status Word (`SW1/SW2`).
  
   * - **ENVELOPE APDU**
     - Comando che trasporta messaggi di sessione (ad esempio, ``SessionEstablishment``). La risposta indica lo stato di elaborazione (`OK` o `più dati`).

   * - **GET RESPONSE APDU**
     - Comando che recupera dati di risposta aggiuntivi quando il Wallet segnala che "più dati" sono disponibili (`SW1=61`).

   * - **SW1/SW2**
     - `SW1/SW2` (Status Words) — Codice di stato a due byte alla fine di ogni risposta. Valori comuni: `90 00 = successo`, `61 XX = più dati`, `6A 82 = file/applicazione non trovata`.


**Passo 1**: L'Istanza di Relying Party (PCD) invia un comando SELECT `APDU` con l'Application Identifier (`AID: A0 00 00 02 48 04 00`) per coinvolgere l'Istanza del Wallet.


**Passo 2**: L'Istanza del Wallet (PICC) risponde con File Control Information (FCI) e status words (SW1/SW2), confermando il successo (`90 00`) o indicando che ci sono più dati (`61 XX`).


**Passo 3**: L'Istanza di Relying Party invia un ENVELOPE `APDU` che trasporta il messaggio ``SessionEstablishment``, che contiene il ``DeviceRequest`` crittografato e la sua chiave pubblica effimera per la configurazione della sessione.


**Passo 4**: L'Istanza del Wallet elabora ``SessionEstablishment`` e restituisce una risposta `APDU` con `SW1/SW2` (`OK` o `più dati` da recuperare), confermando l'inizio del contesto di sessione sicura.


**Passi 5-6**: [Opzionale] L'Istanza del Wallet riceve il messaggio ``SessionEstablishment`` durante Negotiated Handover, l'Istanza del Wallet DEVE verificare che questo messaggio ``SessionEstablishment`` corrisponda allo stesso messaggio ricevuto durante la fase di device retrieval (cioè, Passi 3-4). In caso di mancata corrispondenza, l'Istanza del Wallet DEVE terminare la connessione NFC [`ISO18013-5`_ #9.2.3].


``SessionData`` tramite NFC
----------------------------
La figura seguente illustra il flusso di basso livello conforme a `ISO18013-5`_ per ``SessionData`` tramite NFC corrispondente al Box C nella Figura 8.10.

.. _fig_SessionData-NFC:
.. plantuml:: plantuml/session-data-over-nfc.puml
    :width: 90%
    :alt: La figura illustra il Flusso di Presentazione Session Data tramite NFC in prossimità.
    :caption: `Session Data tramite NFC. <https://www.plantuml.com/plantuml/svg/PP3DJiD038Jl-nIZN4WEl42be4ffGBr0b81wuU8afbrfVyAkavItPn6YAkhDjkORZMSRXOBCrYYQnRlPzXoKcj9D3teY9yWEP0mBtfmMvCs-geeC5B7-LxKDzYwPkO6JgjhzYXQbQ12za702BcCwgxkoH9Pr7AFsRaT2MORwF9p87HbbgOpt4mudRHZM1yQO9D0Hj90sr1jMm8Bx1wmRjFmvSnGuFWi-0XqjfqnuTtYgNz7MNVFotDKOlBNanWIkF-2okGbmONDsG_YQXCT2SKB-W4VjoDnWEOa4tS_24JuWrI1pB9GQ-UhxgsLHssIQMly6>`_

**Passi 1-2**: Finché l'Istanza del Wallet segnala che più dati sono disponibili (`61 XX`), l'Istanza di Relying Party emette `GET RESPONSE APDU` per richiedere il blocco successivo. L'Istanza del Wallet restituisce frammenti ``SessionData`` crittografati fino a quando tutti i dati sono consegnati.


**Passo 3**: L'Istanza del Wallet invia l'`APDU` finale contenente l'ultimo blocco DeviceResponse (con attributi richiesti) o un codice di stato, dopo il quale la sessione può terminare o continuare con una nuova richiesta.

Device Engagement
------------------

La struttura Device Engagement DEVE essere codificata CBOR e avere almeno i seguenti componenti:

.. list-table::
   :class: longtable
   :widths: 30 70
   :header-rows: 1

   * - **Componente**
     - **Descrizione**

   * - **Version**
     - *(tstr)*. Versione della struttura device engagement.

   * - **Security**
     - *(array)*. Contiene due valori obbligatori:

       - *(int)*. Identificatore della suite di cifratura. Vedere Tabella 22 di `ISO18013-5`_.
       - *(bstr)*. Chiave pubblica effimera generata dall'Istanza del Wallet, utilizzata dall'Istanza di Relying Party per derivare la Chiave di Sessione. La chiave DEVE essere di un tipo consentito dalla suite di cifratura selezionata.

   * - **DeviceRetrievalMode-BLEOptions**
     - *(map)*. Fornisce opzioni per la connessione BLE, come modalità Peripheral Server o Central Client, e l'UUID del dispositivo. Vedere Tabella 2 di `ISO18013-5`_ per la mappatura dettagliata.
       
       Se l'Istanza del Wallet indica durante il device engagement che supporta entrambe le modalità, l'Istanza di Relying Party DOVREBBE selezionare la modalità mdoc central client [`ISO18013-5`_ #11.1.3.1].
       
       Presente solo quando si esegue device engagement utilizzando il QR code. Assente quando si utilizza NFC per eseguire Device Engagement.


   * - **DeviceRetrievalMode-NFCOptions**
     - *(map)*. Fornisce opzioni per le connessioni NFC, incluso il ruolo supportato (PICC o PCD) e le dimensioni massime di comando/risposta PDU. Vedere Tabella 2 di `ISO18013-5`_ per la mappatura dettagliata.
        
       Nel caso in cui NFC venga utilizzato per Device Retrieval, l'Istanza del Wallet DEVE supportare la modalità PICC e l'Istanza di Relying Party DEVE supportare la modalità PCD [`ISO18013-5`_ #11.2].
        
       Presente solo quando si esegue device engagement utilizzando il QR code. Assente quando si utilizza NFC per eseguire Device Engagement.
  
   * - **Capabilities**
     - *(map)*. Dichiara le capacità opzionali supportate dall'mdoc, che sono:

       - **HandoverSessionEstablishmentSupport** *(bool)*. Se presente, DEVE essere impostato su `true`. Indica il supporto per ricevere il messaggio `SessionEstablishment` durante Negotiated Handover, come definito in [`ISO18013-5`_ #9.2.3].

       - **ReaderAuthAllSupport** *(bool)*. Se presente, DEVE essere impostato su `true`. Indica il supporto per ricevere la struttura `ReaderAuthAll` nella richiesta mdoc, come definito in [`ISO18013-5`_ #10.2.6].

   * - **OriginInfos**
     - *(array)*. Descrive l'interfaccia utilizzata per ricevere e consegnare la struttura di engagement.
     
       `OriginInfos` PUÒ essere un array vuoto.


Richiesta mdoc
^^^^^^^^^^^^^^

I messaggi nella Richiesta mdoc DEVONO essere codificati utilizzando CBOR. La stringa di byte CBOR risultante per la Richiesta mdoc DEVE essere crittografata con la Chiave di Sessione ottenuta dopo la fase di Device Engagement e DEVE essere trasmessa utilizzando il protocollo BLE o NFC.
Ogni Richiesta mdoc DEVE essere conforme alla seguente struttura, e DEVE includere i seguenti componenti, salvo diversa specifica:

.. list-table::
   :class: longtable
   :widths: 30 70
   :header-rows: 1

   * - **Componente**
     - **Descrizione**

   * - **version**
     - *(tstr)*. Versione della struttura Richiesta mdoc. Abilita la gestione della compatibilità tra diverse versioni o profili di implementazione.

   * - **docRequests**
     - *(array)*. Ogni voce è una `DocRequest` contenente:

       - **itemsRequest**. Struttura `ItemsRequest` codificata CBOR, formattata come:

         - **docType** *(tstr)*. Il tipo di documento richiesto. Vedere :ref:`credential-data-model:mdoc-CBOR Credential Format`.

         - **nameSpaces** *(map)*. Una mappa di identificatori di namespace a *DataElements* richiesti.

           Ogni voce in `DataElements` include:

           - **DataElementIdentifier** *(tstr)*. L'identificatore dell'elemento dati richiesto.
           - **IntentToRetain** *(bool)*. Indica se la Relying Party intende conservare il valore dell'elemento dati.

       - **readerAuth** *(COSE_Sign1, CONDIZIONALE)*. Utilizzato per autenticare l'Istanza di Relying Party per ogni `DocRequest`. La firma è calcolata sui dati `ReaderAuthentication`, come definito in [`ISO18013-5`_ #12.5].

         Questo componente DEVE essere presente solo se `readerAuthAll` non viene utilizzato.

   * - **readerAuthAll**
     - *(COSE_Sign1, CONDIZIONALE)*. Utilizzato per autenticare la Relying Party una volta per tutte le `DocRequest`. La firma è calcolata sui dati `ReaderAuthenticationAll`, come definito in [`ISO18013-5`_ #12.5].

       Questo componente DEVE essere presente solo se `ReaderAuthAllSupport` è impostato su `true` nella struttura DeviceEngagement, e i campi `readerAuth` individuali non vengono utilizzati.

.. note::
    **Richiesta dell'Attestato del Wallet**

    La Relying Party che richiede un Attestato del Wallet DEVE aggiungere un oggetto nell'array **docRequest** avendo il ``docType`` impostato su ``{Trust Anchor reverse domain}.{WalletAttestation}`` come descritto in :ref:`registry-catalogue:Digital Credentials Catalogue Structure`. La Relying Party NON DEVE includere il parametro ``nameSpaces`` nella richiesta.

Risposta mdoc
^^^^^^^^^^^^^

I messaggi nella Risposta mdoc DEVONO essere codificati utilizzando CBOR e DEVONO essere crittografati con la Chiave di Sessione ottenuta dopo la fase di Device Engagement.
Ogni Risposta mdoc DEVE essere conforme alla seguente struttura, e DEVE includere i seguenti componenti, salvo diversa specifica:

.. _table-mdoc-attributes:
.. list-table::
   :class: longtable
   :widths: 25 75
   :header-rows: 1

   * - **Componente**
     - **Descrizione**

   * - **version**
     - *(tstr)*. Versione della struttura Risposta mdoc. Abilita il tracciamento delle modifiche e il mantenimento della compatibilità tra versioni dello standard o profili di implementazione.

   * - **documents**
     - *(array of Documents, OPZIONALE)*. Collezione codificata CBOR di documenti restituiti in risposta alla richiesta. Ogni documento include componenti `issuerSigned` e `deviceSigned`, e segue la struttura definita in [`ISO18013-5`_ #10.3.3].

   * - **documentErrors**
     - *(map, OPZIONALE)*. Una mappa di codici di errore per documenti non restituiti, come definito in [`ISO18013-5`_ #10.3.6]. Ogni chiave è un `docType`, e ogni valore è un `ErrorCode` (int) che indica il motivo per cui il documento non è stato restituito.

   * - **status**
     - *(uint)*. Codice di stato che indica l'esito della richiesta. Ad esempio, `"status": 0` significa elaborazione riuscita. Per dettagli, vedere Tabella 3 (ResponseStatus) di [`ISO18013-5`_ #10.3.5].


Ogni documento in **documents** DEVE essere conforme alla seguente struttura, e DEVE includere i seguenti componenti, salvo diversa specifica:

.. _table-mdoc-documents-attributes:
.. list-table::
   :class: longtable
   :widths: 30 70
   :header-rows: 1

   * - **Componente**
     - **Descrizione**

   * - **docType**
     - *(tstr)*. Identificatore del tipo di documento. Ad esempio, per un mDL, il valore DEVE essere ``org.iso.18013.5.1.mDL``.

   * - **issuerSigned**
     - *(bstr)*. Contiene la struttura `IssuerNameSpaces`, che include elementi dati firmati dal Fornitore di Credenziale, e la struttura `issuerAuth`, che garantisce la loro autenticità e integrità utilizzando il Mobile Security Object (MSO). Vedere :ref:`credential-data-model:mdoc-CBOR Credential Format`.

   * - **deviceSigned**
     - *(bstr)*. Contiene la struttura `DeviceNameSpaces` (elementi dati firmati dall'Istanza del Wallet), e la struttura `deviceAuth`, che include i dati di autenticazione firmati dall'Istanza del Wallet. Vedere la tabella sottostante per dettagli.

   * - **errors**
     - *(map, OPZIONALE)*. Una mappa di codici di errore per ogni elemento dati non restituito raggruppato per namespace. Ogni chiave rappresenta un namespace, e ogni valore è una mappa di identificatori di elementi dati ai corrispondenti codici di errore. Vedere [`ISO18013-5`_ #10.3.6] per dettagli sulla struttura degli errori.



Una struttura dati **deviceSigned** DEVE essere conforme alla seguente struttura, e DEVE includere i seguenti componenti:

.. list-table::
   :class: longtable
   :widths: 25 75
   :header-rows: 1

   * - **Componente**
     - **Descrizione**

   * - **nameSpaces**
     - *(bstr)*. Contiene la struttura `DeviceNameSpaces`. PUÒ essere una struttura vuota. `DeviceNameSpaces` mappa identificatori di namespace a un insieme di elementi dati firmati dall'Istanza del Wallet.

       Ogni namespace contiene uno o più `DeviceSignedItem`, dove ogni elemento include:

       - **DataItemName** *(tstr)*. L'identificatore dell'elemento dati.
       - **DataItemValue** *(any)*. Il valore dell'elemento dati.

   * - **deviceAuth**
     - *(COSE_Sign1)*. Contiene la struttura `DeviceAuth`, che DEVE includere la **deviceSignature** per l'autenticazione dell'Istanza del Wallet. La firma è calcolata sui dati `DeviceAuthentication`, che lega gli elementi restituiti alla sessione e alla richiesta. Vedere [`ISO18013-5`_ #12.4] per dettagli sulla struttura di autenticazione.

.. note::
    **Presentazione dell'Attestato del Wallet**

    L'Istanza del Wallet DEVE includere l'Attestato del Wallet se richiesto dalla Relying Party nella richiesta mdoc. L'Istanza del Wallet DOVREBBE includere tutte le divulgazioni disponibili per l'Attestato del Wallet e DEVE includere il claim ``aal`` come divulgazione. Inoltre, durante la presentazione, l'Istanza del Wallet NON DEVE richiedere il consenso dell'utente alla divulgazione degli attributi dell'Attestato del Wallet che sono dati tecnici non trasparenti all'utente.

Terminazione della Sessione
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

La sessione DEVE essere terminata se si verifica almeno una delle seguenti condizioni:

- Dopo un timeout di nessuna attività di ricezione o invio di messaggi di stabilimento della sessione o dati di sessione. Il timeout per nessuna attività implementato dall'Istanza del Wallet e dall'Istanza di Relying Party DOVREBBE essere non inferiore a 300 secondi;
- Quando l'Istanza del Wallet non accetta più richieste;
- Quando l'Istanza di Relying Party non invia ulteriori richieste.

Se l'Istanza del Wallet e l'Istanza di Relying Party non inviano o ricevono ulteriori richieste, la terminazione della sessione DEVE essere avviata come segue:

- Inviare il codice di stato per la terminazione della sessione, o
- Inviare il comando "End" come delineato in [`ISO18013-5`_ #11.1.3.3].

Quando una sessione viene terminata, l'Istanza del Wallet e l'Istanza di Relying Party DEVONO eseguire almeno le seguenti azioni:

- Distruzione delle chiavi di sessione e del materiale di chiavi effimere correlato;
- Chiusura del canale di comunicazione utilizzato per il device retrieval.

.. note::
  Vedere :ref:`credential-data-model:mdoc-CBOR Credential Format` per il significato degli acronimi di tipo CBOR.

.. include:: ../common/common_definitions.rst


Flusso di Prossimità
====================

Questa sezione descrive come un'Istanza di Relying Party richiede la presentazione di un Attestato Elettronico *mdoc-CBOR* a un'Istanza del Wallet come dettagliato nella *Specifica ISO 18013-5*.

La fase di presentazione di alto livello è strutturata in tre ampie sotto-fasi come illustrato nella figura seguente:

.. plantuml:: plantuml/credential-presentation-high-level-flow.puml
    :width: 90%
    :alt: La figura illustra il Flusso di Presentazione di Alto Livello in prossimità.
    :caption: `Flusso di Presentazione di Alto Livello in prossimità. <https://www.plantuml.com/plantuml/svg/VLBHYjim47pNLsppv8CcHzjxBELeOaYXK9DSANqoEccmHMN9bUHSJUc_T-qanWr9zIAyEpCxE_9ZJ3Aahh6qDLMz_8m3B1K14Ix9PBoZefOHufLnodOQz7xzSBz-ADU-QRrZq0SXjfysURb_odVvbwVlHPxT2P5Cig35VpKNGXG8qRkiYmYlQV6LhmNVZVQAQcyrVxAM-EWxfsNeitQcKRQ31gEl2D_HRq5y9fEPni4eb72LhD1mXOblLhGPovHFvM7y7geBe5Zxa9P1kWgal7DGuuHdf1V0qJTfBH99fsa7snjNKS59zeD2pg4-MnDhH3BE92CjnQEggYLBMTwB-5ouZ8XnM0rd_idfsnNjZotAvwrnbbEXRnFqtEIBIJKl80ENJwBq0_rnknIfQyz-CD5FkElEb6-QpXarfimgxrRSd9LeUSvoXnGC3jB-Qsvyqu2V7MAw3uYi6q7ufUenu8EHbmanVSlfMiIPIIsJd5XizOyGd7wvEVr2rvxv-009aU43TfTTGTrAtaBgICbFt1l0otpWk3kEV8JJNMF_0W00>`_

Le sotto-fasi sono descritte di seguito:

  1. **Device Engagement**: Questa sottofase inizia quando l'Utente viene invitato a divulgare attributi specifici dagli mdoc. L'obiettivo di questa sottofase è stabilire un canale di comunicazione sicuro tra l'Istanza del Wallet e l'Istanza di Relying Party, in modo che le richieste e le risposte mdoc possano essere scambiate durante la sottofase di comunicazione.
  I messaggi scambiati in questa sottofase sono trasmessi attraverso tecnologie a corto raggio per limitare la possibilità di monitorarli o intercettarli da parte di terzi. I dati di *Device Engagement* possono essere trasferiti utilizzando QR code o NFC.

  2. **Session Establishment**: Durante la fase di *Session Establishment*, l'Istanza di Relying Party configura una connessione sicura. Tutti i dati trasmessi su questa connessione sono cifrati utilizzando una chiave di sessione, che è nota sia all'Istanza del Wallet che all'Istanza di Relying Party.
  La sessione stabilita PUÒ essere successivamente terminata in base alle condizioni dettagliate in [`ISO18013-5`_ #12.2.4].

  1. **Comunicazione - Device Retrieval**: L'Istanza di Relying Party cifra la Richiesta mdoc con la chiave di sessione appropriata e la invia all'Istanza del Wallet insieme alla sua chiave pubblica nel messaggio di *Session Establishment*. L'Istanza del Wallet utilizza i dati del messaggio di *Session Establishment* per derivare la chiave di sessione e quindi per decifrare la Richiesta mdoc.
  Durante la sottofase di comunicazione, l'Istanza di Relying Party ha l'opzione di richiedere informazioni dall'Istanza del Wallet utilizzando richieste e risposte mdoc. La modalità principale di comunicazione è il canale sicuro stabilito durante la configurazione della sessione. L'Istanza del Wallet cifra la Risposta mdoc utilizzando la chiave di sessione e la trasmette all'Istanza di Relying Party mobile tramite un messaggio di *Session Data*.


Le Istanze di Relying Party e Wallet registrate nell'ecosistema IT-Wallet DEVONO supportare almeno:

- *Flusso di Recupero del Dispositivo Supervisionato* dove un supervisore umano supervisiona il processo di verifica in persona, in contrasto con il *flusso non supervisionato* dove la verifica potrebbe avvenire attraverso sistemi automatizzati senza supervisione umana (:ref:`WP_095 <wallet-credential-presentation-testcases>`).
- *Autenticazione dell'Istanza di Relying Party* seguendo i meccanismi definiti nella `ISO18013-5`_ per il *reader authentication* (:ref:`WP_098 <wallet-credential-presentation-testcases>`).
- *Tipo di Documento* domestico e *Namespace* definiti in questa specifica tecnica in aggiunta a quelli già definiti nell'`ISO18013-5`_ per l'mDL (vedi :ref:`credential-data-model:Attestato Elettronico in formato mdoc-CBOR` per maggiori dettagli) (:ref:`WP_099 <wallet-credential-presentation-testcases>`).

La tabella seguente mostra le tecnologie di *Device Engagement* supportate  (:ref:`WP_097 <wallet-credential-presentation-testcases>`), specificando quali sono obbligatorie.

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
     - **Istanza di Relying Party**
     - **Istanza del Wallet**
     - **Istanza di Relying Party**
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

Legenda: C = Condizionale | M = Obbligatorio | :sup:`a`\  Il supporto per almeno uno di questi metodi è obbligatorio  (:ref:`WP_097a <wallet-credential-presentation-testcases>`)

La tabella seguente mostra le tecnologie di *Device Retrieval* supportate, specificando quali sono obbligatorie.

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
     - **Istanza di Relying Party**
     - **Istanza del Wallet**
     - **Istanza di Relying Party**
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
 
Legenda: C = Condizionale | M = Obbligatorio | :sup:`a`\  Il supporto per almeno uno di questi metodi è obbligatorio (:ref:`WP_096b <wallet-credential-presentation-testcases>`)

.. note::
   Dalla seconda edizione, versione 3, `ISO18013-5`_ non definisce o supporta *Server Retrieval* come opzione di trasporto. Sono specificati solo metodi di recupero di prossimità (NFC, BLE e opzionalmente Wi-Fi Aware) (:ref:`WP_096 <wallet-credential-presentation-testcases>`). Pertanto, *Server Retrieval* non è considerato in questo flusso (:ref:`WP_096a <wallet-credential-presentation-testcases>` and :ref:`PPR-023 <test-plans-proximity-presentation:Matrice di Test per il Verificatore di Credenziali in Prossimità>`).


La figura seguente illustra il flusso di basso livello conforme a ISO 18013-5 per il flusso di prossimità.

.. _fig_High-Level-Flow-ITWallet-Presentation-ISO-updated:
.. plantuml:: plantuml/credential-presentation-flow.puml
    :width: 99%
    :alt: La figura illustra il Flusso di Presentazione di Basso Livello in prossimità.
    :caption: `Flusso di Presentazione di Basso Livello in prossimità. <https://www.plantuml.com/plantuml/svg/ZLJBRjim4BppAnRgfGQS5kYn28muZki6JTFKJf1BBXIrjeb8IvKFAVxxBacvTLe7oKtIScTsPeSwSrvQ7vfQoE0DXQP4AuHKtbYuSsX1EWX2j7n8AzrAyb3Soxf63tUaVH7h_VFoyWOkYM59OIftGeIJIVyPVhH8uBS80y3-LAJJdVJ8IE4q7StKWGyJ0qkl3K6vEzOCF2XN9DolPjCzKsftMAFoBZMrrZpfHliTFw5Zq0ov3gJYWwov94phuRkaIhBu7UWrh3osy0cq0p8UMhHhOnki8bzYwtdOyEAmwGXI9KIVXbeWeOqg2Nl0TeiDlzRmY3oKr1OUw7rHp2-mqmg_uUx3ZTLTKOpX-STG5iL82CiJiVQEcVjn1--kBXTVRnVB-VnQd9QJwUZqOpdXpjmufutSC1tveW2M9m6Vr5RIPa3ukGHbgcJbzPTPd3d1Yx-BuHrs9vFkhIAMA2kq_uWu-9X5PCIPQTh0W0wTYyunr9xinY8d2tcvJc-8ZUVb09AokzR7D--jBcFl0rdy5T1vOFPL1ffpFifQkstM_QfdvtlFZlT3mv_PnJ_MLHdf_6e--COALE1fOvcmFh1n2C0nfRboWKdJo-HHEBFfDUUI8ntja9x98dJAu7BGBrkEUiSRuQZkiwvfCro6GzFSc6rJXZoVS63MO76ZdRSvlmhvHgzZcd6uKzC1-JKVPzd75Sj_QN4yLcl8uS6sBZYLl2GGlVPR6BRvRDnCADzaU8xFVwvcal5H9sDogtHReDHKiMUZDBNQedg4fZ8AMBokueyYNNmc663X5csZAHadAZouD0SllJZZ-VX7-ni0>`_


**Passo 1**: L'Utente apre l'Istanza del Wallet avviando il processo.

**Passo 2**: L'Utente si autentica all'Istanza del Wallet. Questo può essere fatto dall'Istanza del Wallet o da un *Wallet Secure Cryptographic Application* (WSCA). È un prerequisito per accedere ai dati sensibili e presentare attributi  (:ref:`WP_100 <wallet-credential-presentation-testcases>`).

**Passo 3**: L'Utente seleziona la funzionalità di presentazione di prossimità.

**Passo 4**: [Opzionale] Se l'autenticazione iniziale nel Passo 2 non è stata effettuata tramite WSCA, PUÒ essere richiesta un'autenticazione separata tramite WSCA (:ref:`WP_100 <wallet-credential-presentation-testcases>`).

**Passo 5**: L'Istanza del Wallet genera una nuova coppia di chiavi effimera per la comunicazione sicura (:ref:`WP_101 <wallet-credential-presentation-testcases>`). La chiave pubblica (``EDeviceKey.Pub``) sarà scambiata con l'Istanza di Relying Party per derivare una chiave di sessione condivisa, successivamente utilizzata per cifrare la sessione (processo di *Device Engagement*).

.. admonition:: Box A

   L'Istanza del Wallet e l'Istanza di Relying Party scambiano dati di *Device Engagement* tramite QR code o tramite NFC Connection Handover (:ref:`WP_097 <wallet-credential-presentation-testcases>`).  

   Fare riferimento a:

   - Sez 8.2.2.1 per ``DeviceEngagement`` tramite QR code
   - Sez 8.2.2.2 per ``DeviceEngagement`` tramite NFC


**Passo 6**: L'Istanza di Relying Party genera la sua coppia di chiavi effimera (``EReaderKey.Priv``, ``EReaderKey.Pub``). La chiave privata (``EReaderKey.Priv``) DEVE essere mantenuta segreta, e la chiave pubblica (``EReaderKey.Pub``) DEVE essere utilizzata nel *Session Establishment* (:ref:`PPR-002 <test-plans-proximity-presentation:Matrice di Test per il Verificatore di Credenziali in Prossimità>`).

**Passo 7**: L'Istanza del Wallet e l'Istanza di Relying Party DEVONO derivare indipendentemente le chiavi di sessione utilizzando la loro chiave effimera privata e la chiave effimera pubblica dell'altra parte attraverso un Key Agreement Protocol opportuno. Questo garantisce lo scambio di messaggi cifrati nella sessione. In questo particolare passo, l'Istanza di Relying Party DEVE calcolare la sua chiave di sessione (:ref:`PPR-002 <test-plans-proximity-presentation:Matrice di Test per il Verificatore di Credenziali in Prossimità>` and :ref:`WP_097 <wallet-credential-presentation-testcases>`).

**Passo 8**: L'Istanza di Relying Party DEVE preparare il ``SessionEstablishment``. Questo messaggio DEVE essere firmato dall'Istanza di Relying Party (autenticazione dell'*mdoc reader* come specificato in [`ISO18013-5`_ #12.5]) e cifrato utilizzando la chiave di sessione derivata nel passo precedente. Il messaggio ``SessionEstablishment`` DEVE includere la ``EReaderKey.Pub`` e una richiesta per specifici attributi (:ref:`PPR-002 <test-plans-proximity-presentation:Matrice di Test per il Verificatore di Credenziali in Prossimità>`).

Di seguito è riportato un esempio non normativo nella notazione diagnostica di un messaggio ``SessionEstablishment`` CBOR che contiene una Richiesta mdoc per un Attestato Elettronico mDL.

.. literalinclude:: ../../examples/iso-session-establishment.txt
  :language: text

.. admonition:: Box B

   L'Istanza di Relying Party DEVE trasmettere il messaggio ``SessionEstablishment`` cifrato e firmato all'Istanza del Wallet su una connessione NFC o BLE sicura stabilita sulla base delle informazioni contenute nel Device Engagement (:ref:`PPR-003 <test-plans-proximity-presentation:Matrice di Test per il Verificatore di Credenziali in Prossimità>`).
   Fare riferimento a:

   - Sez 8.2.2.3 per ``SessionEstablishment`` tramite BLE, e
   - Sez 8.2.2.5 per ``SessionEstablishment`` tramite NFC

**Passo 9**: L'Istanza del Wallet DEVE calcolare la chiave di sessione, come descritto nel Passo 7 (:ref:`PPR-002 <test-plans-proximity-presentation:Matrice di Test per il Verificatore di Credenziali in Prossimità>`).

**Passo 10**: Al ricevimento del ``SessionEstablishment``, l'Istanza del Wallet DEVE decifrarlo utilizzando la chiave di sessione calcolata al Passo 9 e DEVE verificare la firma dell'Istanza di Relying Party (come specificato in [`ISO18013-5`_ #12.5 *mdoc reader authentication*]) per garantire l'autenticità del messaggio (:ref:`PPR-002 <test-plans-proximity-presentation:Matrice di Test per il Verificatore di Credenziali in Prossimità>` and :ref:`WP_105–106 <wallet-credential-presentation-testcases>`).

**Passo 11**: L'Istanza del Wallet DEVE decifrare la richiesta di attributi e DEVE chiedere all'Utente il consenso per il rilascio degli attributi richiesti (:ref:`WP_107 <wallet-credential-presentation-testcases>`). DEVE inoltre visualizzare il contenuto del Certificato di Registrazione della Relying Party per garantire l'autenticità, la trasparenza sui dati richiesti e sul suo scopo registrato (:ref:`WP_107a <wallet-credential-presentation-testcases>`).

**Passo 12**: L'Utente esamina la richiesta e le informazioni di registrazione della Relying Party e quindi approva la presentazione degli attributi richiesti.

.. admonition:: Box C

   Dopo aver ricevuto l'approvazione dell'Utente, l'Istanza del Wallet DEVE recuperare gli Attestati Elettronici mdoc richiesti (:ref:`PPR-006 <test-plans-proximity-presentation:Matrice di Test per il Verificatore di Credenziali in Prossimità>` and :ref:`WP_108 <wallet-credential-presentation-testcases>`). Deve quindi preparare un messaggio ``SessionData`` contenente questi Attestati Elettronici Digitali, e DEVE firmare i dati di autenticazione richiesti (come parte del processo di autenticazione mdoc, come specificato in [`ISO18013-5`_ #12.4]) come specificato in (:ref:`WP_109–110 <wallet-credential-presentation-testcases>`). L'Istanza del Wallet DEVE cifrare il ``SessionData`` utilizzando la chiave di sessione stabilita prima di trasmetterlo all'Istanza di Relying Party tramite il canale sicuro (:ref:`WP_111 <wallet-credential-presentation-testcases>`). La firma garantisce il binding del dispositivo e l'integrità dei dati. La risposta mdoc DEVE essere codificata in CBOR, con la sua struttura delineata in [`ISO18013-5`_ #10.3] (:ref:`PPR-029 <test-plans-proximity-presentation:Matrice di Test per il Verificatore di Credenziali in Prossimità>`, :ref:`PPR-030 <test-plans-proximity-presentation:Matrice di Test per il Verificatore di Credenziali in Prossimità>`, and :ref:`WP_112 <wallet-credential-presentation-testcases>`).
   Fare riferimento a (:ref:`WP_112a–112b <wallet-credential-presentation-testcases>`):

   - Sez 8.2.2.4 per ``SessionData`` tramite BLE, e
   - Sez 8.2.2.5 per ``SessionData`` tramite NFC

Di seguito è riportato un esempio non normativo di ``SessionData`` nella notazione diagnostica che contiene la Risposta mdoc di un Attestato Elettronico mDL.

.. literalinclude:: ../../examples/iso-session-data.txt
  :language: text

**Passo 13**: L'Istanza di Relying Party riceve il ``SessionData``, quindi DEVE decifrarlo e DEVE verificare la firma dell'Istanza del Wallet per garantire l'integrità dei dati e che provengano dal dispositivo previsto (device binding). DEVE anche controllare la validità dell'mdoc, inclusa la firma del suo Fornitore di Attestati Elettronici. In caso di Attestati Elettronici Digitali di lunga durata, DOVREBBE anche controllare lo stato di revoca utilizzando il `TOKEN-STATUS-LIST`_.

**Passo 14**: Una volta completato lo scambio di dati, una delle parti può terminare la sessione. La sessione può essere terminata inviando lo status code per la *Session Termination* in un messaggio ``SessionData``; questo può essere inviato insieme a una la Richiesta mdoc o Risposta mdoc [`ISO18013-5`_ #12.2.4] (:ref:`WP_113c <wallet-credential-presentation-testcases>`). Se viene utilizzato BLE, questo può comportare l'invio di uno *status code* per la *Session Termination* o il comando "End". In questo scenario, il Client GATT (Istanza di Relying Party) DEVE annullare l'iscrizione dalle caratteristiche e disconnettersi dal server GATT (Istanza del Wallet) (:ref:`PPR-007 <test-plans-proximity-presentation:Matrice di Test per il Verificatore di Credenziali in Prossimità>`, :ref:`WP_113b <wallet-credential-presentation-testcases>`, and :ref:`WP_114 <wallet-credential-presentation-testcases>`).

**Considerazione Finale**: Il flusso di presentazione si è concentrato sullo scambio tecnico di dati in contesti di prossimità. È cruciale riconoscere che i flussi di prossimità supervisionati che coinvolgono un verificatore umano svolgono un ruolo vitale in molti casi d'uso (ad esempio, verifica dell'età in un negozio, controllo dell'identità da parte delle forze dell'ordine). L'elemento umano aggiunge un livello di verifica dell'identità attraverso l'ispezione visiva e il confronto, contribuendo agli aspetti di User Binding e garanzia di autenticazione complessiva non completamente catturati in un flusso di presentazione puramente tecnico.

.. _sec-deviceengagement-qr:

``DeviceEngagement`` tramite QR Code
-------------------------------------
La figura seguente illustra il flusso di basso livello conforme a ISO 18013-5 per ``DeviceEngagement`` tramite QR Code corrispondente al Box A nella Figura :ref:`fig_High-Level-Flow-ITWallet-Presentation-ISO-updated`.

.. _fig_DeviceEngagement-QR:
.. plantuml:: plantuml/device-engagement-over-qr-code.puml
    :width: 90%
    :alt: La figura illustra il Flusso di Presentazione *Device Engagement* tramite QR Code in prossimità.
    :caption: `Device Engagement tramite QR Code. <https://www.plantuml.com/plantuml/svg/PP0n3i8m34NtdCBAtWimL4Z0m0P5YDaaLcifTQlMIQvFbAK5F5Zoz__Fae-hug9n30QZJXB7Doq6IjKsbnqxdb4Kx0j388Mdi5h05VA_fRl1LGfH75LBCXiBdN92fPghIcxQT837C6NGWU3UmMdo12mkHC_IWxLdIkpe8ZtsD9AejT-iLCVKD6qk98Uo9sstFVqaTa8sHn9VFl01>`_

**Passo 1**: L'Istanza del Wallet presenta un QR Code all'Istanza di Relying Party. Il QR code DEVE contenere un URI con "mdoc:" come schema e la struttura ``DeviceEngagement`` specificata nella Sezione 9.1 codificata utilizzando, come percorso, base64url-without-padding, secondo `RFC 4648`_  (:ref:`WP_102a <wallet-credential-presentation-testcases>`).

Esempio Non Normativo con BLE come Device Retrieval
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Di seguito è riportato un esempio non normativo di``DeviceEngagement`` nella notazione diagnostica che utilizza QR per il *Device Engagement* e Bluetooth Low Energy (BLE) per il recupero dei dati.

 .. literalinclude:: ../../examples/iso-device-engagement-BLE.txt
  :language: text

Esempio Non Normativo con NFC come Device Retrieval
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Di seguito è riportato un esempio non normativo di ``DeviceEngagement`` nella notazione diagnostica che utilizza QR per il *Device Engagement* e NFC per il recupero dei dati.

 .. literalinclude:: ../../examples/iso-device-engagement-NFC.txt
  :language: text

**Passo 2**: Il verificatore utilizza la sua Istanza di Relying Party per scansionare il QR code e recuperare i dati ``DeviceEngagement`` dall'mdoc. Esso DEVE selezionare una delle tecnologie di trasmissione tra quelle fornite nella struttura ``DeviceEngagement``.

.. _sec-deviceengagement-nfc:

``DeviceEngagement`` tramite NFC
---------------------------------
La figura seguente illustra il flusso di basso livello conforme a ISO 18013-5 per ``DeviceEngagement`` tramite NFC corrispondente al Box A nella Figura :ref:`fig_High-Level-Flow-ITWallet-Presentation-ISO-updated` (:ref:`WP_103 <wallet-credential-presentation-testcases>`). 

.. _fig_DeviceEngagement-NFC:
.. plantuml:: plantuml/device-engagement-over-nfc.puml
    :width: 90%
    :alt: La figura illustra il Flusso di Presentazione *Device Engagement* tramite NFC in prossimità.
    :caption: `Device Engagement tramite NFC. <https://www.plantuml.com/plantuml/img/dLDDJ-Cm4BtFhtZoXUOGJfooAaA28hWKr7QrPpSUWYNNpjfEilpxdPIIRRLKIEGG9NdpFkObkKbPnzpj7Eak1z_jjXo9g9M7jhQjzXdgbtQECtvwcnLqmd0Ahvxnw4N6rxo7Uo9TPzlhp38wNVPqWR8iiRo_XU7UrWpsZMvunw8o4m6HH8Zmt8HiXMAAaK3Ry0VgKvOYGBkCzJltLNiJUiaFEVgol1ugh5WRF1m0hDbnBMQRjvPnXOrk2XbcbnZBoVLKPn2Tlf8DhQ0Eoxl5FRGHDDl4QPf5uhXFDrDTz9L_gQlagmzK5OTCOwGfpOf_Tvp6tRks3N6qhdMCbcCg3jwZzN_fbRhRDx7uLuI2qLaND6xZ3O7a32bENkN5V0wbrfoI3NuXDM-TJQyVh2vQtnmlFxdDGfk5eLs1-Pn8xhuZ8_vuykuDzWN3-tSqjMTmM1pMuxEbVc2pN3nFrTg4JbYNrAEyXZJvrB8_7JcNSAAinsA-dBfr8PqNEx6aiMeYmqSV-j7DG3U2o__r5m00>`_

``DeviceEngagement`` tramite NFC è basato su *NFC Forum Connection Handover Technical Specification*, Versione 1.5. È supportata solo la modalità Reader/Writer utilizzando un Tag di Tipo 4. Il protocollo Connection Handover è sempre avviato dall'Istanza di Relying Party, che assume il ruolo di *Handover Requester*. L'Istanza del Wallet agisce come NFC Tag Device e l'Istanza di Relying Party come NFC Reader Device. L'Istanza del Wallet DEVE utilizzare Static Handover o *Negotiated Handover*:
- **Static Handover**: L'Istanza di Relying Party recupera un messaggio *Handover Select* direttamente dal Tag di Tipo 4 dell'Istanza del Wallet. Questo messaggio contiene almeno un Alternative Carrier Record, ognuno indicante un metodo di recupero supportato dall'Istanza del Wallet  (:ref:`WP_103a <wallet-credential-presentation-testcases>`). L'Istanza di Relying Party DEVE selezionare una di queste tecnologie di trasmissione. (vedere Passo 1)
- **Negotiated Handover**: L'Istanza del Wallet include il servizio ``urn:nfc:sn:handover`` in un Service Parameter Record del messaggio NDEF (NFC Data Exchange Format) iniziale  (:ref:`WP_103b <wallet-credential-presentation-testcases>`). Selezionando questo servizio, l'Istanza di Relying Party invia una *Handover Request* con un Alternative Carrier Record per ogni carrier che supporta. L'Istanza del Wallet risponde con un messaggio *Handover Select* contenente esattamente un carrier selezionato. (Vedere Passi 2-4)

**Passo 1**: L'Istanza di Relying Party legge il Tag NFC di Tipo 4 del Wallet per ottenere un messaggio *Handover Select*, che include: 
- Alternative Carrier Record: un record NDEF all'interno di un messaggio *Handover Select* o *Handover Request*. Punta a una possibile tecnologia di comunicazione (chiamata "carrier"), come NFC o BLE. Informa il lettore sul carrier supportato e un puntatore (Auxiliary Data Reference) a informazioni più dettagliate. L'Alternative Carrier Record per la tecnologia di trasmissione *Device Retrieval* NFC deve fare riferimento al Carrier Configuration Record con il riferimento ID "nfc".
- Carrier Configuration Record: fornisce i parametri tecnici necessari per utilizzare effettivamente quel carrier. Per la tecnologia di trasmissione *Device Retrieval NFC*, DEVE avere il tipo "iso.org:18013:nfc" e il riferimento ID "nfc". Il contenuto binario del Carrier Configuration Record DEVE essere codificato secondo la Tabella 1 di [`ISO18013-5`_ #9.2.2] (:ref:`WP_103d <wallet-credential-presentation-testcases>`).

Per esempio:
Per NFC, questo definisce le lunghezze massime di comando/risposta APDU (Application Protocol Data Unit); 
Per BLE, definisce l'UUID del servizio dell'Istanza del Wallet, gli UUID delle caratteristiche, la dimensione MTU (Maximum Transmission Unit) e parametri di connessione opzionali; 
Se è supportato il ``SessionEstablishment`` anticipato, elenca anche il nome del servizio TNEP (Tag NDEF Exchange Protocol) utilizzato per inviare il messaggio ``SessionEstablishment`` durante l'handover.

.. note::
   Per la tecnologia di trasmissione *Device Retrieval NFC*, i contenuti dell'Alternative Carrier Record e del/dei Carrier Configuration Record DEVONO essere conformi a [`ISO18013-5`_ #9.2.2]. Per la tecnologia di trasmissione *Device Retrieval BLE*, i contenuti dell'Alternative Carrier Record e del/dei Carrier Configuration Record devono essere conformi a [`ISO18013-5`_ #11.1.2].

- Auxiliary Data Record DEVE trasportare la struttura ``DeviceEngagement`` dall'Istanza del Wallet all'Istanza di Relying Party come parte del record NDEF ausiliario nel messaggio *Handover Select*. Questo record ha il tipo ``iso.org:18013:deviceengagement``, il riferimento ID "mdoc", e utilizza il formato di tipo esterno del forum NFC (``0x04``). Per ogni record Alternative Carrier, l'Auxiliary Data Reference DEVE puntare al record NDEF contenente la Struttura ``DeviceEngagement`` (:ref:`WP_103e <wallet-credential-presentation-testcases>`). 

**Passo 2**: L'Istanza di Relying Party legge il messaggio NDEF (NFC Data Exchange Format) Iniziale dell'Istanza del Wallet, che contiene un service parameter record per ``urn:nfc:sn:handover``, indicando che il Wallet supporta *Negotiated Handover*. 

**Passo 3**: L'Istanza di Relying Party invia una *Handover Request* all'Istanza del Wallet elencando i carrier supportati. 

**Passo 4**: L'Istanza del Wallet restituisce *Handover Select* costruito in risposta al messaggio *Handover Request* ricevuto. I contenuti del messaggio *Handover Select* sono gli stessi del Passo 1 (:ref:`WP_103f <wallet-credential-presentation-testcases>`).

.. note::
    L'uso di *Negotiated Handover* per il *Device Engagement* consente la negoziazione dei metodi di trasferimento. Per BLE, consente inoltre la negoziazione delle chiavi utilizzate dal livello di trasmissione. Questo fornisce un'esperienza utente migliorata e migliora la sicurezza della trasmissione dei dati [`ISO18013-5`_ #9.2.1].

.. note::
    Procedere solo se le Capabilities di ``DeviceEngagement`` includono ``HandoverSessionEstablishmentSupport`` impostato su ``true``  (:ref:`WP_103c <wallet-credential-presentation-testcases>`). Altrimenti, saltare il ``SessionEstablishment`` anticipato. Il ``SessionEstablishment`` anticipato viene inviato tramite un servizio TNEP dedicato; lo stesso ``SessionEstablishment`` DEVE anche essere inviato nuovamente durante il *Device Retrieval* e DEVE corrispondere. Se non corrisponde, l'Istanza del Wallet termina (:ref:`WP_103g <wallet-credential-presentation-testcases>`). Se il ``SessionEstablishment`` anticipato non riesce a essere inviato, procedere normalmente (:ref:`WP_103h <wallet-credential-presentation-testcases>`).

**Passo 5**: [Opzionale] L'Istanza di Relying Party apre il servizio TNEP denominato [urn:placeholder] con l'Istanza del Wallet durante l'handover negoziato per consegnare il messaggio ``SessionEstablishment`` anticipato.

**Passo 6**: L'Istanza di Relying Party invia ``SessionEstablishment`` (ad esempio, ``EReaderKey`` + ``DeviceRequest`` cifrato). L'Istanza del Wallet lo elabora; il *Device Retrieval* non è ancora iniziato.

**Passo 7**: L'Istanza di Relying Party chiude il servizio TNEP.

.. note::
    Se un messaggio ``SessionEstablishment`` opzionale viene inviato durante *Negotiated Handover* (Passo 5), l'Istanza del Wallet DEVE verificare che corrisponda al messaggio ``SessionEstablishment`` ricevuto durante *Device Retrieval* (utilizzando BLE o canale sicuro NFC). Questa verifica è richiesta per garantire un corretto Session Binding.

Esempio Non Normativo
^^^^^^^^^^^^^^^^^^^^^^
Di seguito è riportato un esempio non normativo di una struttura ``DeviceEngagement`` per *Device Retrieval* tramite BLE e NFC.
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
    
**Passo 1**: L'Istanza del Wallet e l'Istanza di Relying Party stabiliscono una connessione BLE sicura [`ISO18013-5`_ #11.1]. L'Istanza di Relying Party (central) si connette all'Istanza del Wallet (peripheral) utilizzando l'UUID del servizio dell'Istanza del Wallet fornito da DeviceEngagement, individua servizi/caratteristiche e abilita le notifiche secondo necessità (:ref:`WP_112c <wallet-credential-presentation-testcases>`).

**Passi 2-5**: [Opzionale] L'Istanza del Wallet avvia la verifica preparandosi a controllare l'identità della Relying Party tramite la caratteristica Ident, che è una caratteristica BLE GATT che trasporta un valore identificatore come descritto in [`ISO18013-5`_ #11.1.3.2]. L'Istanza del Wallet deriva il valore Ident atteso e legge la caratteristica Ident della Relying Party, confrontandola con l'Ident atteso, e terminando la connessione BLE qualora non vi sia corrispondenza (:ref:`WP_112d <wallet-credential-presentation-testcases>`).

.. note::
    Lo scopo della caratteristica Ident è unicamente di verificare se l'Istanza del Wallet è connessa all'Istanza di Relying Party corretta prima di iniziare il *Device Retrieval*. Se l'Istanza del Wallet è connessa all'Istanza di Relying Party sbagliata, il *Session Establishment* fallirà. Connettersi e disconnettersi a un'Istanza di Relying Party richiede una quantità relativamente grande di tempo; pertanto, è più veloce implementare metodi per identificare l'Istanza di Relying Party corretta [`ISO18013-5`_ #11.1.3.1].

**Passo 6**: L'Istanza di Relying Party invia il messaggio ``SessionEstablishment`` cifrato (includendo ``EReaderKey`` e ``DeviceRequest`` cifrato) tramite la connessione BLE stabilita.

**Passi 7-8**: [Opzionale] Se l'Istanza del Wallet riceve il messaggio ``SessionEstablishment`` durante *Negotiated Handover*, l'Istanza del Wallet DEVE verificare se questo messaggio ``SessionEstablishment`` corrisponde al messaggio ``SessionEstablishment`` ricevuto durante la fase di *Device Retrieval* (cioè, Passo 6). In caso di mancata corrispondenza, l'Istanza del Wallet deve terminare la connessione BLE [`ISO18013-5`_ #9.2.3].

``SessionData`` tramite BLE
----------------------------
La figura seguente illustra il flusso di basso livello conforme a `ISO18013-5`_ per ``SessionData`` tramite BLE corrispondente ai Box C nella Figura 8.10.

.. _fig_SessionData-BLE:
.. plantuml:: plantuml/session-data-over-ble.puml
    :width: 90%
    :alt: La figura illustra il Flusso di Presentazione *Session Data* tramite BLE in prossimità.
    :caption: `Session Data tramite BLE. <https://www.plantuml.com/plantuml/svg/LO-n3i8m34JtV8ML2GP-W05L20Oa1aI5M5ZSr898hLjYfn5_Zs50PRjtT_B9bIWcpNtdCEl0kMyeEJUQ5qCSaHNy5RkE52uSrGCAbF_uV883snKEz8qdvp1ed539gZzfTbbjfZNKn2qWIBmpcJ0W3kargb4Y6GSMWeNtDOd4WNUewFqIRboYFgpnp2IVBggcs6GbWM6Y1DlZthcMPeCpAAwoMNlp3G00>`_

**Passo 1**: L'Istanza del Wallet invia l'APDU finale contenente l'ultimo blocco DeviceResponse (con attributi richiesti) o uno status code, dopo il quale la sessione può terminare o continuare con una nuova richiesta.


``SessionEstablishment`` tramite NFC
-------------------------------------
.. note::
    Se il *Device Engagement* viene avviato tramite un QR code, l'Istanza di Relying Party non ha un modo standardizzato per segnalare la sua intenzione di utilizzare NFC per il successivo trasferimento di dati. Questo potrebbe portare a una peggiore esperienza utente, poiché l'Utente potrebbe non essere consapevole di dover utilizzare NFC. Questo problema viene evitato quando NFC viene utilizzato per il *Device Engagement*, poiché stabilisce implicitamente il metodo di trasferimento dati [`ISO18013-5`_ #8.2.5].

.. note::
    A causa della velocità di trasferimento dati limitata di NFC, se è richiesta una grande quantità di dati per una transazione, potrebbe non essere né pratico né ragionevole per un Utente mantenere il dispositivo all'interno del campo RF dell'Istanza di Relying Party per la durata della transazione. Inoltre, quando un dispositivo lascia il campo RF il segnale viene perso necessitando l'avvio di una nuova transazione. Questo può essere evitato facendo sì che tutte le interazioni dell'Utente con l'Istanza del Wallet vengano effettuate mentre l'Istanza del Wallet rimane nel campo RF oppure, se non sono richieste interazioni dell'Utente durante la fase di trasmissione [`ISO18013-5`_ #8.2.5].

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
     - Proximity Integrated Circuit Card, implementata dalle Istanze di Wallet che agiscono come tag NFC.

   * - **PCD**
     - Proximity Coupling Device, implementato dalle Istanze di Relying Party utilizzando scambi `APDU`.

   * - **AID**
     - Application Identifier, ID univoco utilizzato nel comando SELECT `APDU` per coinvolgere l'Istanza del Wallet.

   * - **APDU**
     - Application Protocol Data Unit, un formato di messaggio standard per la comunicazione tra Istanza di Relying Party (PCD) e Wallet (PICC) costituito da Command APDU (ad esempio, `SELECT`, `ENVELOPE`, `GET RESPONSE`) dal lettore e Response `APDU` dal wallet, che includono scambio di dati e fine scambio utilizzando status words (`SW1/SW2`).

   * - **SELECT APDU**
     - Comando che apre l'Istanza del Wallet tramite `AID`. La risposta include File Control Information (FCI) e Status Word (`SW1/SW2`).
  
   * - **ENVELOPE APDU**
     - Comando che trasporta messaggi di sessione (ad esempio, ``SessionEstablishment``). La risposta indica lo stato di elaborazione (`OK` o `more data`).

   * - **GET RESPONSE APDU**
     - Comando che recupera dati di risposta aggiuntivi quando il Wallet segnala che "più dati" sono disponibili (`SW1=61`).

   * - **SW1/SW2**
     - `SW1/SW2` (Status Words) — status code a due byte alla fine di ogni risposta. Valori comuni: `90 00 = successo`, `61 XX = more data`, `6A 82 = file/applicazione non trovata`.


**Passo 1**: L'Istanza di Relying Party (PCD) invia un comando SELECT `APDU` con l'Application Identifier (`AID: A0 00 00 02 48 04 00`) per coinvolgere l'Istanza del Wallet.


**Passo 2**: L'Istanza del Wallet (PICC) risponde con File Control Information (FCI) e status words (SW1/SW2), confermando il successo (`90 00`) o indicando che ci sono più dati (`61 XX`) (:ref:`WP_112e <wallet-credential-presentation-testcases>`).


**Passo 3**: L'Istanza di Relying Party invia un ENVELOPE `APDU` che trasporta il messaggio ``SessionEstablishment``, che contiene il ``DeviceRequest`` cifrato e la sua chiave pubblica effimera per la configurazione della sessione.


**Passo 4**: L'Istanza del Wallet elabora ``SessionEstablishment`` e restituisce una risposta `APDU` con `SW1/SW2` (`OK` o `more data` da recuperare), confermando l'inizio del contesto di sessione sicura (:ref:`WP_112f <wallet-credential-presentation-testcases>`).


**Passi 5-6**: [Opzionale] L'Istanza del Wallet riceve il messaggio ``SessionEstablishment`` durante *Negotiated Handover*, l'Istanza del Wallet DEVE verificare che questo messaggio ``SessionEstablishment`` corrisponda allo stesso messaggio ricevuto durante la fase di *Device Retrieval* (cioè, Passi 3-4). In caso di mancata corrispondenza, l'Istanza del Wallet DEVE terminare la connessione NFC [`ISO18013-5`_ #9.2.3].


``SessionData`` tramite NFC
----------------------------
La figura seguente illustra il flusso di basso livello conforme a `ISO18013-5`_ per ``SessionData`` tramite NFC corrispondente al Box C nella Figura 8.10.

.. _fig_SessionData-NFC:
.. plantuml:: plantuml/session-data-over-nfc.puml
    :width: 90%
    :alt: La figura illustra il Flusso di Presentazione *Session Data* tramite NFC in prossimità.
    :caption: `Session Data tramite NFC. <https://www.plantuml.com/plantuml/svg/PP3DJiD038Jl-nIZN4WEl42be4ffGBr0b81wuU8afbrfVyAkavItPn6YAkhDjkORZMSRXOBCrYYQnRlPzXoKcj9D3teY9yWEP0mBtfmMvCs-geeC5B7-LxKDzYwPkO6JgjhzYXQbQ12za702BcCwgxkoH9Pr7AFsRaT2MORwF9p87HbbgOpt4mudRHZM1yQO9D0Hj90sr1jMm8Bx1wmRjFmvSnGuFWi-0XqjfqnuTtYgNz7MNVFotDKOlBNanWIkF-2okGbmONDsG_YQXCT2SKB-W4VjoDnWEOa4tS_24JuWrI1pB9GQ-UhxgsLHssIQMly6>`_

**Passi 1-2**: Finché l'Istanza del Wallet segnala che più dati sono disponibili (`61 XX`), l'Istanza di Relying Party emette `GET RESPONSE APDU` per richiedere il blocco successivo. L'Istanza del Wallet restituisce frammenti ``SessionData`` cifrati fino a quando tutti i dati sono consegnati.


**Passo 3**: L'Istanza del Wallet invia l'`APDU` finale contenente l'ultimo blocco DeviceResponse (con attributi richiesti) o un status code, dopo il quale la sessione può terminare o continuare con una nuova richiesta.

Device Engagement
------------------

La struttura del Device Engagement DEVE essere codificata in CBOR e avere almeno le seguenti componenti (:ref:`PPR-001 <test-plans-proximity-presentation:Matrice di Test per il Verificatore di Credenziali in Prossimità>`, :ref:`PPR-021 <test-plans-proximity-presentation:Matrice di Test per il Verificatore di Credenziali in Prossimità>`, :ref:`PPR-022 <test-plans-proximity-presentation:Matrice di Test per il Verificatore di Credenziali in Prossimità>`, and :ref:`WP_102 <wallet-credential-presentation-testcases>`):

.. list-table::
   :class: longtable
   :widths: 30 70
   :header-rows: 1

   * - **Componente**
     - **Descrizione**

   * - **Version**
     - *(tstr)*. Versione della struttura *Device Engagement*.

   * - **Security**
     - *(array)*. Contiene due valori obbligatori:

       - *(int)*. Identificatore della suite di cifratura. Vedere Tabella 22 di `ISO18013-5`_.
       - *(bstr)*. Chiave pubblica effimera generata dall'Istanza del Wallet, utilizzata dall'Istanza di Relying Party per derivare la chiave di sessione. La chiave DEVE essere di un tipo consentito dalla suite di cifratura selezionata (:ref:`PPR-022 <test-plans-proximity-presentation:Matrice di Test per il Verificatore di Credenziali in Prossimità>`).

   * - **DeviceRetrievalMode-BLEOptions**
     - *(map)*. Fornisce opzioni per la connessione BLE, come modalità Peripheral Server o Central Client, e l'UUID del dispositivo. Vedere Tabella 2 di `ISO18013-5`_ per la mappatura dettagliata.
       
       Se l'Istanza del Wallet indica durante il *Device Engagement* che supporta entrambe le modalità, l'Istanza di Relying Party DOVREBBE selezionare la modalità mdoc central client [`ISO18013-5`_ #11.1.3.1].
       
       Presente solo quando si esegue *Device Engagement* utilizzando il QR code. Assente quando si utilizza NFC per eseguire *Device Engagement*.

   * - **DeviceRetrievalMode-NFCOptions**
     - *(map)*. Fornisce opzioni per le connessioni NFC, incluso il ruolo supportato (PICC o PCD) e le dimensioni massime di comando/risposta PDU. Vedere Tabella 2 di `ISO18013-5`_ per la mappatura dettagliata.
        
       Nel caso in cui NFC venga utilizzato per *Device Retrieval*, l'Istanza del Wallet DEVE supportare la modalità PICC e l'Istanza di Relying Party DEVE supportare la modalità PCD [`ISO18013-5`_ #11.2].
        
       Quest'ultima è presente solo quando si esegue *Device Engagement* utilizzando il QR code, mentre è assente quando si utilizza NFC per eseguire *Device Engagement*.
  
   * - **Capabilities**
     - *(map)*. Dichiara le capacità opzionali supportate dall'mdoc, che sono:

       - **HandoverSessionEstablishmentSupport** *(bool)*. Se presente, DEVE essere impostato su `true`. Indica il supporto per ricevere il messaggio `SessionEstablishment` durante *Negotiated Handover*, come definito in [`ISO18013-5`_ #9.2.3] (:ref:`PPR-024 <test-plans-proximity-presentation:Matrice di Test per il Verificatore di Credenziali in Prossimità>`).

       - **ReaderAuthAllSupport** *(bool)*. Se presente, DEVE essere impostato su `true`. Indica il supporto per ricevere la struttura `ReaderAuthAll` nella la Richiesta mdoc, come definito in [`ISO18013-5`_ #10.2.6]  (:ref:`PPR-025 <test-plans-proximity-presentation:Matrice di Test per il Verificatore di Credenziali in Prossimità>`).

   * - **OriginInfos**
     - *(array)*. Descrive l'interfaccia utilizzata per ricevere e consegnare la struttura di engagement.
     
       `OriginInfos` PUÒ essere un array vuoto.


Richiesta mdoc
^^^^^^^^^^^^^^

I messaggi nella Richiesta mdoc DEVONO essere codificati utilizzando CBOR. La stringa di byte CBOR risultante per la Richiesta mdoc DEVE essere cifrata con la Chiave di Sessione ottenuta dopo la fase di Device Engagement e DEVE essere trasmessa utilizzando il protocollo BLE o NFC (:ref:`PPR-026 <test-plans-proximity-presentation:Matrice di Test per il Verificatore di Credenziali in Prossimità>`, :ref:`PPR-027 <test-plans-proximity-presentation:Matrice di Test per il Verificatore di Credenziali in Prossimità>`, :ref:`PPR-028 <test-plans-proximity-presentation:Matrice di Test per il Verificatore di Credenziali in Prossimità>`).
Ogni Richiesta mdoc DEVE essere conforme alla seguente struttura e DEVE includere i seguenti componenti, a meno che non sia specificato diversamente:

.. list-table::
   :class: longtable
   :widths: 30 70
   :header-rows: 1

   * - **Componente**
     - **Descrizione**

   * - **version**
     - *(tstr)*. Versione della struttura della Richiesta mdoc. Abilita la gestione della compatibilità tra diverse versioni o profili di implementazione.

   * - **docRequests**
     - *(array)*. Ogni voce è una `DocRequest` contenente:

       - **itemsRequest**. Struttura `ItemsRequest` codificata CBOR, formattata come:

         - **docType** *(tstr)*. Il tipo di documento richiesto. Vedere :ref:`credential-data-model:Attestato Elettronico in formato mdoc-CBOR`.

         - **nameSpaces** *(map)*. Una mappa di identificatori di namespace a *DataElements* richiesti.

           Ogni voce in `DataElements` include:

           - **DataElementIdentifier** *(tstr)*. L'identificatore dell'elemento dati richiesto.
           - **IntentToRetain** *(bool)*. Indica se la Relying Party intende conservare il valore dell'elemento dati.

       - **readerAuth** *(COSE_Sign1, CONDIZIONALE)*. Utilizzato per autenticare l'Istanza di Relying Party per ogni `DocRequest`. La firma è calcolata sui dati `ReaderAuthentication`, come definito in [`ISO18013-5`_ #12.5].

         Questo componente DEVE essere presente solo se ``readerAuthAll`` non viene utilizzato (:ref:`PPR-025 <test-plans-proximity-presentation:Matrice di Test per il Verificatore di Credenziali in Prossimità>`).

   * - **readerAuthAll**
     - *(COSE_Sign1, CONDIZIONALE)*. Utilizzato per autenticare la Relying Party una volta per tutte le `DocRequest`. La firma è calcolata sui dati `ReaderAuthenticationAll`, come definito in [`ISO18013-5`_ #12.5].

       Questo componente DEVE essere presente solo se ``ReaderAuthAllSupport`` è impostato su ``true`` nel messaggio di DeviceEngagement, e i campi individuali ``readerAuth`` non vengono utilizzati (:ref:`PPR-025 <test-plans-proximity-presentation:Matrice di Test per il Verificatore di Credenziali in Prossimità>`).


Risposta mdoc
^^^^^^^^^^^^^^


I messaggi nella Risposta mdoc DEVONO essere codificati utilizzando CBOR e DEVONO essere cifrati con la Chiave di Sessione ottenuta dopo la fase di Device Engagement (:ref:`PPR-029 <test-plans-proximity-presentation:Matrice di Test per il Verificatore di Credenziali in Prossimità>`, :ref:`PPR-030 <test-plans-proximity-presentation:Matrice di Test per il Verificatore di Credenziali in Prossimità>`).

Ogni Risposta mdoc DEVE essere conforme alla seguente struttura e DEVE includere i seguenti componenti, a meno che non sia specificato diversamente:

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
     - *(uint)*. Status code che indica l'esito della richiesta. Ad esempio, `"status": 0` significa elaborazione riuscita. Per dettagli, vedere Tabella 3 (ResponseStatus) di [`ISO18013-5`_ #10.3.5].


Ogni elemento in **documents** DEVE essere conforme alla seguente struttura e DEVE includere i seguenti componenti, a meno che non sia specificato diversamente (:ref:`PPR-029 <test-plans-proximity-presentation:Matrice di Test per il Verificatore di Credenziali in Prossimità>`):

.. _table-mdoc-documents-attributes:
.. list-table::
   :class: longtable
   :widths: 30 70
   :header-rows: 1

   * - **Componente**
     - **Descrizione**

   * - **docType**
     - *(tstr)*. identificativo del tipo di documento. Ad esempio, per un mDL, il valore DEVE essere ``org.iso.18013.5.1.mDL`` (:ref:`PPR-010 <test-plans-proximity-presentation:Matrice di Test per il Verificatore di Credenziali in Prossimità>`).

   * - **issuerSigned**
     - *(bstr)*. Contiene la struttura `IssuerNameSpaces`, che include elementi dati firmati dal Fornitore di Attestati Elettronici, e la struttura `issuerAuth`, che garantisce la loro autenticità e integrità utilizzando il Mobile Security Object (MSO). Vedere :ref:`credential-data-model:Attestato Elettronico in formato mdoc-CBOR`.

   * - **deviceSigned**
     - *(bstr)*. Contiene la struttura `DeviceNameSpaces` (elementi dati firmati dall'Istanza del Wallet), e la struttura `deviceAuth`, che include i dati di autenticazione firmati dall'Istanza del Wallet. Vedere la tabella sottostante per dettagli.

   * - **errors**
     - *(map, OPZIONALE)*. Una mappa di codici di errore per ogni elemento dati non restituito raggruppato per namespace. Ogni chiave rappresenta un namespace, e ogni valore è una mappa di identificatori di elementi dati ai corrispondenti codici di errore. Vedere [`ISO18013-5`_ #10.3.6] per dettagli sulla struttura degli errori.



Una struttura di dati **deviceSigned** DEVE essere conforme alla seguente struttura e DEVE includere i seguenti componenti (:ref:`WP_111a <wallet-credential-presentation-testcases>`):

.. list-table::
   :class: longtable
   :widths: 25 75
   :header-rows: 1

   * - **Componente**
     - **Descrizione**

   * - **nameSpaces**
     - *(bstr)*. Contiene la struttura `DeviceNameSpaces`. PUÒ essere una struttura vuota. `DeviceNameSpaces` mappa identificatori di namespace verso un insieme di elementi dati firmati dall'Istanza del Wallet.

       Ogni namespace contiene uno o più `DeviceSignedItem`, dove ogni elemento include:

       - **DataItemName** *(tstr)*. L'identificatore dell'elemento dati.
       - **DataItemValue** *(any)*. Il valore dell'elemento dati.

   * - **deviceAuth**

     - *(COSE_Sign1)*. Contiene la struttura ``DeviceAuth``, che DEVE includere la **deviceSignature** per l'autenticazione dell'Istanza del Wallet. La firma è calcolata sui dati ``DeviceAuthentication``, che lega gli elementi restituiti alla sessione e alla richiesta. Vedi [`ISO18013-5`_ #12.4] per i dettagli sulla struttura di autenticazione (:ref:`PPR-003 <test-plans-proximity-presentation:Matrice di Test per il Verificatore di Credenziali in Prossimità>`).


Session Termination
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

La sessione DEVE chiudersi qualora si verifichi almeno una delle seguenti condizioni (:ref:`PPR-007 <test-plans-proximity-presentation:Matrice di Test per il Verificatore di Credenziali in Prossimità>` and :ref:`WP_113–113a <wallet-credential-presentation-testcases>`):

- Dopo un timeout di inattività nel quale non sono scambiati messaggi di *Session Establishment* o *Session Data*. Questo timeout di inattività viene implementato dall'Istanza del Wallet e dall'Istanza di Relying Party e DOVREBBE essere non inferiore a 300 secondi;
- Quando l'Istanza del Wallet non accetta più richieste;
- Quando l'Istanza di Relying Party non invia ulteriori richieste.

Se l'Istanza del Wallet e l'Istanza di Relying Party non inviano o ricevono ulteriori richieste, la terminazione della sessione DEVE essere avviata come segue (:ref:`PPR-007 <test-plans-proximity-presentation:Matrice di Test per il Verificatore di Credenziali in Prossimità>` and :ref:`WP_113 <wallet-credential-presentation-testcases>`):


- Inviare lo status code per la *Session Termination*, o
- Inviare il comando "End" come delineato in [`ISO18013-5`_ #11.1.3.3].

Quando una sessione viene terminata, l'Istanza del Wallet e l'Istanza di Relying Party DEVONO eseguire almeno le seguenti azioni (:ref:`WP_114 <wallet-credential-presentation-testcases>`):

- Distruzione delle chiavi di sessione e del materiale di chiavi effimere correlato;
- Chiusura del canale di comunicazione utilizzato per il *Device Retrieval*.

.. note::
  Vedere :ref:`credential-data-model:Attestato Elettronico in formato mdoc-CBOR` per il significato degli acronimi di tipo CBOR.

.. include:: ../common/common_definitions.rst


Flusso di Prossimità
====================

Questa sezione descrive come un'Istanza di Relying Party richiede la presentazione di una Credenziale *mdoc-CBOR* a un'Istanza del Wallet secondo la *Specifica ISO 18013-5*.

La fase di presentazione di alto livello è strutturata in tre ampie sotto-fasi come illustrato nella seguente figura:

.. plantuml:: plantuml/credential-presentation-high-level-flow.puml
    :width: 90%
    :alt: La figura illustra il Flusso di Presentazione di Alto Livello in prossimità.
    :caption: `Flusso di Presentazione di Alto Livello in prossimità. <https://www.plantuml.com/plantuml/svg/VLBHYjim47pNLsppv8CcHzjxBELeOaYXK9DSANqoEccmHMN9bUHSJUc_T-qanWr9zIAyEpCxE_9ZJ3Aahh6qDLMz_8m3B1K14Ix9PBoZefOHufLnodOQz7xzSBz-ADU-QRrZq0SXjfysURb_odVvbwVlHPxT2P5Cig35VpKNGXG8qRkiYmYlQV6LhmNVZVQAQcyrVxAM-EWxfsNeitQcKRQ31gEl2D_HRq5y9fEPni4eb72LhD1mXOblLhGPovHFvM7y7geBe5Zxa9P1kWgal7DGuuHdf1V0qJTfBH99fsa7snjNKS59zeD2pg4-MnDhH3BE92CjnQEggYLBMTwB-5ouZ8XnM0rd_idfsnNjZotAvwrnbbEXRnFqtEIBIJKl80ENJwBq0_rnknIfQyz-CD5FkElEb6-QpXarfimgxrRSd9LeUSvoXnGC3jB-Qsvyqu2V7MAw3uYi6q7ufUenu8EHbmanVSlfMiIPIIsJd5XizOyGd7wvEVr2rvxv-009aU43TfTTGTrAtaBgICbFt1l0otpWk3kEV8JJNMF_0W00>`_


Le sotto-fasi sono descritte di seguito:

  1. **Device Engagement**: Questa sottofase inizia quando all'Utente viene richiesto di divulgare determinati attributi dall'mdoc(s). L'obiettivo di questa sottofase è stabilire un canale di comunicazione sicuro tra l'Istanza del Wallet e l'Istanza di Relying Party, in modo che le richieste e le risposte di presentazione possano essere scambiate durante la sottofase di comunicazione.
  I messaggi scambiati in questa sottofase vengono trasmessi attraverso tecnologie a corto raggio per limitare la possibilità di intercettazione e ascolto non autorizzato.

  2. **Stabilimento della sessione**: Durante la fase di stabilimento della sessione, l'Istanza di Relying Party configura una connessione sicura. Tutti i dati trasmessi su questa connessione sono criptati utilizzando una chiave di sessione, che è nota sia all'Istanza del Wallet che all'Istanza di Relying Party in questa fase.
  La sessione stabilita PUÒ essere terminata in base alle condizioni dettagliate in [`ISO18013-5`_ #9.1.1.4].

  3. **Comunicazione - Recupero del Dispositivo**: L'Istanza di Relying Party cripta la richiesta mdoc con l'appropriata chiave di sessione e la invia all'Istanza del Wallet insieme alla sua chiave pubblica in un messaggio di stabilimento della sessione. L'mdoc utilizza i dati dal messaggio di stabilimento della sessione per derivare la chiave di sessione e decriptare la richiesta mdoc.
  Durante la sottofase di comunicazione, l'Istanza di Relying Party ha l'opzione di richiedere informazioni dall'Istanza del Wallet utilizzando richieste e risposte mdoc. La modalità principale di comunicazione è il canale sicuro stabilito durante la configurazione della sessione. L'Istanza del Wallet cripta la risposta di presentazione utilizzando la chiave di sessione e la trasmette al Relying Party mobile tramite un messaggio di dati di sessione.



Le Istanze di Relying Party e Wallet registrate nell'ecosistema IT-Wallet DEVONO supportare almeno:

- *Flusso di Recupero del Dispositivo Supervisionato* dove un Relying Party umano supervisiona il processo di verifica di persona, in contrasto con il *flusso non supervisionato* dove la verifica potrebbe avvenire attraverso sistemi automatizzati senza supervisione umana.
- *Device Engagement* basato su QR Code.
- *Autenticazione dell'Istanza RP* seguendo i meccanismi definiti nell'`ISO18013-5`_ per l'*autenticazione del lettore*.
- Meccanismo di *Recupero del Dispositivo* basato su Bluetooth Low Energy (BLE) per la sottofase di comunicazione. Il meccanismo di *Recupero del Server* NON DEVE essere supportato.
- *Tipo di Documento* domestico e *Namespace* definiti in questa specifica tecnica in aggiunta a quelli già definiti nell'`ISO18013-5`_ per l'mDL (vedi :ref:`credential-data-model:Formato Credenziale mdoc-CBOR` per maggiori dettagli).
- *Validazione dell'Istanza del Wallet* attraverso l'Attestato di Wallet.


La seguente figura illustra il flusso di basso livello conforme a ISO 18013-5 per il flusso di prossimità.

.. _fig_High-Level-Flow-ITWallet-Presentation-ISO-updated:
.. plantuml:: plantuml/credential-presentation-flow.puml
    :width: 99%
    :alt: La figura illustra il Flusso di Presentazione di Basso Livello in prossimità.
    :caption: `Flusso di Presentazione di Basso Livello in prossimità. <https://www.plantuml.com/plantuml/svg/ZLD1Qniz4BtxLmnx-WB9T-Wnb98qCQKqfQxTa4ilO-tOAx8xKgNHRltlEolP8DCOkWTZIJFllNbwkek2GTBGmvERRfvef1vMWIAne5Z7iEemqWAJE4x3bi9Y0VgX4HVWEL80Z93oNlxnYcQDzSW2pGlsFGayivLchfl-Bbclu3Eh1ZQKIyQ2dsu-JBVmpHE3T0H7e5FbIO8TKUY8cjxdbY8fQHChIHbXUtWB15oOJn1UDW_t5Mk1YDIJaPWRVN2_xM3b0BvsPfVOp7-mrwFSxxp0L-GMrPm3s1riX3oy0nk1dO2di7DXe5Pv2oleDwdmT45uLKRSblAiyHCnXNbufWd8TpJeieTNKere0_pa_vfc-KYZDVI53l-lWXsRvXhEDzEsQQvEgECjR3etvOc_h-71jGIMJPzQotjjB7rBtkDUsLYQvlmQnhmSRxA-ZK6kaSgPaloBT9YrhmbR2hNsUhFINc2LPV1922B5Q1tFUATKbg-grO1x30G8qUwPMa1kWTY4WvTv9HBiLi5KIw1VYQBCaZO5UHa5jxsDNJ7XgXxxKX6uaG9yV5f299C2WUcGcVhgHY_fBwUFbCLT9CWJA8VTQUuavhbGbEc8aIEsFiw2NXCzOW-QnbEaBU-FcQyDYDTgWN4in0hgTX1eRwE44az3GUnk3YjLp-V-Y5xdYhYzPBRIUyUHAeSVKL2DLUh9IWVb2ivrNJAqkkJQiWhs-asRvWVJve33rlAS-AkiqtHaNc5edG4ToRRbfPT7gnn7PFX1OR2SNSd7BTNFudnZMjmHjsde_m00>`_


**Passo 1**: L'Utente apre l'Istanza del Wallet avviando il processo.

**Passo 2**: L'Utente si autentica all'Istanza del Wallet. Questo può essere fatto dall'Istanza del Wallet o da un'Applicazione Crittografica Sicura per il Portafoglio (WSCA). È un prerequisito per accedere a dati sensibili e presentare attributi.

**Passo 3**: L'Utente seleziona la funzionalità di presentazione di prossimità.

**Passo 4**: [Opzionale] Se l'autenticazione iniziale nel Passo 2 non è stata effettuata tramite WSCA, PUÒ essere richiesta un'autenticazione separata tramite WSCA.

**Passo 5**: L'Istanza del Wallet genera una nuova coppia di chiavi effimere a Curva Ellittica per la comunicazione sicura. La chiave pubblica (``EDeviceKey.Pub``) sarà utilizzata per la crittografia della sessione. Questo fa parte del processo di device engagement.

**Passo 6**: L'Istanza del Wallet presenta un QR Code all'Istanza di Relying Party. Questo QR code contiene i dati ``DeviceEngagement``, che includono ``EDeviceKey.Pub`` e informazioni sulle suite di cifratura supportate.

Di seguito è riportato un esempio non normativo che utilizza la notazione diagnostica di un ``DeviceEngagement`` codificato in CBOR che utilizza QR per il device engagement e Bluetooth Low Energy (BLE) per il recupero dei dati.

.. literalinclude:: ../../examples/iso-device-engagement.txt
  :language: text

**Passo 7**: Il verificatore utilizza la sua Istanza di Relying Party per scansionare il QR code e recuperare i dati ``DeviceEngagement`` dall'mdoc.

**Passo 8**: L'Istanza di Relying Party genera la sua coppia di chiavi effimere (``EReaderKey.Priv``, ``EReaderKey.Pub``). La chiave privata (``EReaderKey.Priv``) DEVE essere mantenuta segreta, e la chiave pubblica (``EReaderKey.Pub``) DEVE essere utilizzata nello stabilimento della sessione.

**Passo 9**: L'Istanza del Wallet e l'Istanza di Relying Party DEVONO derivare indipendentemente le chiavi di sessione utilizzando la loro chiave effimera privata e la chiave effimera pubblica dell'altra parte attraverso un protocollo di accordo chiave. Questo garantisce la crittografia della sessione. In questo particolare passo, l'Istanza di Relying Party DEVE calcolare la sua chiave di sessione.

**Passo 10**: L'Istanza RP DEVE preparare un messaggio ``SessionEstablishment``. Questo messaggio DEVE essere firmato dall'Istanza di Relying Party (autenticazione del lettore mdoc come specificato in [`ISO18013-5`_ #9.1.4]) e criptato utilizzando le chiavi di sessione derivate nel passo precedente. Il messaggio ``SessionEstablishment`` DEVE includere ``EReaderKey.Pub`` e una richiesta per specifici attributi.

Di seguito è riportato un esempio non normativo che utilizza la notazione diagnostica di un ``SessionEstablishment`` codificato in CBOR che contiene la richiesta mdoc di un Attestato di Wallet insieme a una Credenziale Digitale mDL.

.. literalinclude:: ../../examples/iso-session-establishment.txt
  :language: text

**Passo 11**: L'Istanza di Relying Party DEVE trasmettere il messaggio ``SessionEstablishment`` criptato e firmato all'Istanza del Wallet su una connessione BLE sicura che è stata stabilita in base alle informazioni di device engagement.

**Passo 12**: L'Istanza del Wallet DEVE calcolare la chiave di sessione, come descritto nel Passo 9.

**Passo 13**: Dopo aver ricevuto il messaggio ``SessionEstablishment``, l'Istanza del Wallet DEVE decriptarlo utilizzando la chiave di sessione condivisa e DEVE verificare la firma dell'Istanza di Relying Party (autenticazione del lettore mdoc come specificato in [`ISO18013-5`_ #9.1.1.4]) per garantirne l'autenticità.

**Passo 14**: L'Istanza del Wallet DEVE decriptare la richiesta di attributi e DEVE chiedere all'Utente il suo consenso per rilasciare gli attributi richiesti. DEVE anche visualizzare il contenuto del Certificato di Registrazione della Relying Party per garantire la trasparenza sui dati richiesti e sul suo scopo registrato.

**Passo 15**: L'Utente esamina la richiesta e le informazioni di registrazione della Relying Party e poi approva la presentazione degli attributi richiesti.

**Passo 16**: Dopo aver ricevuto l'approvazione dell'Utente, l'Istanza del Wallet DEVE recuperare le Credenziali Digitali mdoc richieste. Quindi DEVE preparare un messaggio `SessionData` contenente queste Credenziali Digitali, e DEVE firmare i dati di autenticazione richiesti (come parte del processo di autenticazione mdoc, come specificato in [`ISO18013-5`_ #9.1.3]). DEVE criptarlo utilizzando le chiavi di sessione stabilite prima di trasmetterlo all'Istanza di Relying Party sul canale BLE sicuro. La firma garantisce il binding del dispositivo e l'integrità dei dati. La risposta mdoc DEVE essere codificata in CBOR, con la sua struttura delineata in [`ISO18013-5`_ #8.3.2.1.2.2].

Di seguito è riportato un esempio non normativo che utilizza la notazione diagnostica di un ``SessionData`` codificato in CBOR che contiene la risposta mdoc di un Attestato di Wallet e un mDL.

.. literalinclude:: ../../examples/iso-session-data.txt
  :language: text

**Passo 17**: L'Istanza di Relying Party riceve il ``SessionData``, quindi DEVE decriptarlo, e DEVE verificare la firma dell'Istanza del Wallet per garantire l'integrità dei dati e che provengano dal dispositivo previsto (device binding). DEVE anche controllare la validità dell'mdoc, inclusa la firma del suo Fornitore di Credenziale. In caso di Credenziali Digitali a lunga durata, DOVREBBE anche controllare lo stato di revoca utilizzando `TOKEN-STATUS-LIST`_.

**Passo 18**: Una volta completato lo scambio di dati, una delle parti può terminare la sessione. Se viene utilizzato BLE, questo può comportare l'invio di un codice di stato per la terminazione della sessione o il comando "End". In questo scenario, il Client GATT (Istanza di Relying Party) DEVE annullare l'iscrizione alle caratteristiche e disconnettersi dal server GATT (Istanza del Wallet).

**Considerazione Finale**: Il flusso di presentazione si è concentrato sullo scambio tecnico di dati in ambienti di prossimità. È cruciale riconoscere che i flussi di prossimità supervisionati che coinvolgono un verificatore umano svolgono un ruolo vitale in molti casi d'uso (ad esempio, verifica dell'età in un negozio, controllo dell'identità da parte delle forze dell'ordine). L'elemento umano aggiunge un livello di verifica dell'identità attraverso l'ispezione visiva e il confronto, contribuendo all'Associazione Crittografica con l'Utente e agli aspetti generali di garanzia dell'autenticazione non completamente catturati in un flusso di presentazione puramente tecnico.

.. note::
  Durante la presentazione di prossimità, l'Istanza del Wallet potrebbe non essere in grado di recuperare un Attestato di Wallet aggiornato; in questo caso, l'Istanza del Wallet DOVREBBE inviare l'ultima versione dell'Attestato di Wallet. È lasciato alla Relying Party determinare se una presentazione con un Attestato di Wallet valido ma scaduto sia valida o meno.

Device Engagement
^^^^^^^^^^^^^^^^^

La struttura del Device Engagement DEVE essere codificata in CBOR e avere almeno i seguenti componenti:

.. list-table::
   :class: longtable
   :widths: 30 70
   :header-rows: 1

   * - **Componente**
     - **Descrizione**

   * - **Version**
     - *(tstr)*. Versione della struttura di device engagement.

   * - **Security**
     - *(array)*. Contiene due valori obbligatori:

       - *(int)*. Identificatore della suite di cifratura. Vedi Tabella 22 di `ISO18013-5`_.

       - *(bstr)*. Chiave pubblica effimera generata dall'Istanza del Wallet, utilizzata dall'Istanza di Relying Party per derivare la Chiave di Sessione. La chiave DEVE essere di un tipo consentito dalla suite di cifratura selezionata.

   * - **BleOptions**
     - *(map)*. Fornisce opzioni per la connessione BLE, come la modalità Peripheral Server o Central Client, e l'UUID del dispositivo.

       Solo la `Modalità Central Client` DEVE essere supportata da questo profilo di implementazione.

   * - **Capabilities**
     - *(map)*. Dichiara le capacità opzionali supportate dall'mdoc, che sono:

       - **HandoverSessionEstablishmentSupport** *(bool)*. Se presente, DEVE essere impostato su `true`. Indica il supporto per ricevere il messaggio `SessionEstablishment` durante il Negotiated Handover, come definito in [`ISO18013-5`_ #8.2.2.4].

       - **ReaderAuthAllSupport** *(bool)*. Se presente, DEVE essere impostato su `true`. Indica il supporto per ricevere la struttura `ReaderAuthAll` nella richiesta mdoc, come definito in [`ISO18013-5`_ #8.3.2.1.2.1].

   * - **OriginInfos**
     - *(array)*. Descrive l'interfaccia utilizzata per ricevere e consegnare la struttura di engagement.

        Quando utilizzato nei flussi definiti in [`ISO18013-5`_ #6.3.2.1], `OriginInfos` PUÒ essere un array vuoto.


Richiesta mdoc
^^^^^^^^^^^^^^

I messaggi nella Richiesta mdoc DEVONO essere codificati utilizzando CBOR. La stringa di byte CBOR risultante per la Richiesta mdoc DEVE essere criptata con la Chiave di Sessione ottenuta dopo la fase di Device Engagement e DEVE essere trasmessa utilizzando il protocollo BLE.
Ogni Richiesta mdoc DEVE essere conforme alla seguente struttura e DEVE includere i seguenti componenti, a meno che non sia specificato diversamente:

.. list-table::
   :class: longtable
   :widths: 30 70
   :header-rows: 1

   * - **Componente**
     - **Descrizione**

   * - **version**
     - *(tstr)*. Versione della struttura della Richiesta mdoc. Consente la gestione della compatibilità tra diverse versioni o profili di implementazione.

   * - **docRequests**
     - *(array)*. Ogni voce è un `DocRequest` contenente:

       - **itemsRequest**. Struttura `ItemsRequest` codificata in CBOR, formattata come:

         - **docType** *(tstr)*. Il tipo di documento richiesto. Vedi :ref:`credential-data-model:Formato Credenziale mdoc-CBOR`.

         - **nameSpaces** *(map)*. Una mappa di identificatori di namespace per i *DataElements* richiesti.

           Ogni voce in `DataElements` include:

           - **DataElementIdentifier** *(tstr)*. L'identificatore dell'elemento di dati richiesto.
           - **IntentToRetain** *(bool)*. Indica se la Relying Party intende conservare il valore dell'elemento di dati.

       - **readerAuth** *(COSE_Sign1, CONDIZIONALE)*. Utilizzato per autenticare l'Istanza di Relying Party per ogni `DocRequest`. La firma è calcolata sui dati `ReaderAuthentication`, come definito in [`ISO18013-5`_ #9.1.4].

         Questo componente DEVE essere presente solo se `readerAuthAll` non viene utilizzato.

   * - **readerAuthAll**
     - *(COSE_Sign1, CONDIZIONALE)*. Utilizzato per autenticare la Relying Party una volta per tutti i `DocRequest`. La firma è calcolata sui dati `ReaderAuthenticationAll`, come definito in [`ISO18013-5`_ #9.1.4].

       Questo componente DEVE essere presente solo se `ReaderAuthAllSupport` è impostato su `true` nella struttura DeviceEngagement, e i campi individuali `readerAuth` non vengono utilizzati.

Risposta mdoc
^^^^^^^^^^^^^

I messaggi nella Risposta mdoc DEVONO essere codificati utilizzando CBOR e DEVONO essere criptati con la Chiave di Sessione ottenuta dopo la fase di Device Engagement.
Ogni Risposta mdoc DEVE essere conforme alla seguente struttura e DEVE includere i seguenti componenti, a meno che non sia specificato diversamente:

.. _table-mdoc-attributes:
.. list-table::
   :class: longtable
   :widths: 25 75
   :header-rows: 1

   * - **Componente**
     - **Descrizione**

   * - **version**
     - *(tstr)*. Versione della struttura della Risposta mdoc. Consente di tracciare le modifiche e mantenere la compatibilità tra le versioni dello standard o i profili di implementazione.

   * - **documents**
     - *(array di Documents, OPZIONALE)*. Collezione di documenti codificati in CBOR restituiti in risposta alla richiesta. Ogni documento include i componenti `issuerSigned` e `deviceSigned`, e segue la struttura definita nella tabella sottostante.

   * - **documentErrors**
     - *(map, OPZIONALE)*. Una mappa di codici di errore per i documenti non restituiti, come definito in [`ISO18013-5`_ #8.3.2.1.2.3]. Ogni chiave è un `docType`, e ogni valore è un `ErrorCode` (int) che indica il motivo per cui il documento non è stato restituito.

   * - **status**
     - *(uint)*. Codice di stato che indica l'esito della richiesta. Ad esempio, `"status": 0` significa elaborazione riuscita. Per i dettagli, vedere la Tabella 8 (ResponseStatus) di [`ISO18013-5`_ #8.3.2.1.2].


Ogni documento in **documents** DEVE essere conforme alla seguente struttura e DEVE includere i seguenti componenti, a meno che non sia specificato diversamente:

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
     - *(bstr)*. Contiene la struttura `IssuerNameSpaces`, che include elementi di dati firmati dal Fornitore di Credenziale, e la struttura `issuerAuth`, che garantisce la loro autenticità e integrità utilizzando il Mobile Security Object (MSO). Vedi :ref:`credential-data-model:Formato Credenziale mdoc-CBOR`.

   * - **deviceSigned**
     - *(bstr)*. Contiene la struttura `DeviceNameSpaces` (elementi di dati firmati dall'Istanza del Wallet), e la struttura `deviceAuth`, che include i dati di autenticazione firmati dall'Istanza del Wallet. Vedi la tabella sottostante per i dettagli.

   * - **errors**
     - *(map, OPZIONALE)*. Una mappa di codici di errore per ogni elemento di dati non restituito raggruppato per namespace. Ogni chiave rappresenta un namespace, e ogni valore è una mappa di identificatori di elementi di dati ai corrispondenti codici di errore. Vedi [`ISO18013-5`_ #8.3.2.1.2.3] per i dettagli sulla struttura degli errori.



Una struttura di dati **deviceSigned** DEVE essere conforme alla seguente struttura e DEVE includere i seguenti componenti:

.. list-table::
   :class: longtable
   :widths: 25 75
   :header-rows: 1

   * - **Componente**
     - **Descrizione**

   * - **nameSpaces**
     - *(bstr)*. Contiene la struttura `DeviceNameSpaces`. PUÒ essere una struttura vuota. `DeviceNameSpaces` mappa gli identificatori di namespace a un insieme di elementi di dati firmati dall'Istanza del Wallet.

       Ogni namespace contiene uno o più `DeviceSignedItem`, dove ogni elemento include:

       - **DataItemName** *(tstr)*. L'identificatore dell'elemento di dati.
       - **DataItemValue** *(any)*. Il valore dell'elemento di dati.

   * - **deviceAuth**
     - *(COSE_Sign1)*. Contiene la struttura `DeviceAuth`, che DEVE includere la **deviceSignature** per l'autenticazione dell'Istanza del Wallet. La firma è calcolata sui dati `DeviceAuthentication`, che lega gli elementi restituiti alla sessione e alla richiesta. Vedi [`ISO18013-5`_ #9.1.3] per i dettagli sulla struttura di autenticazione.


Terminazione della Sessione
^^^^^^^^^^^^^^^^^^^^^^^^^^^

La sessione DEVE essere terminata se si verifica almeno una delle seguenti condizioni:

- Dopo un timeout di inattività nel ricevere o inviare messaggi di stabilimento della sessione o dati della sessione. Il timeout per l'inattività implementato dall'Istanza del Wallet e dall'Istanza di Relying Party DOVREBBE essere non inferiore a 300 secondi;
- Quando l'Istanza del Wallet non accetta più richieste;
- Quando l'Istanza di Relying Party non invia ulteriori richieste.

Se l'Istanza del Wallet e l'Istanza di Relying Party non inviano o ricevono ulteriori richieste, la terminazione della sessione DEVE essere avviata come segue:

- Inviare il codice di stato per la terminazione della sessione, o
- Inviare il comando "End" come delineato in [`ISO18013-5`_ #8.3.3.1.1.5].

Quando una sessione viene terminata, l'Istanza del Wallet e l'Istanza di Relying Party DEVONO eseguire almeno le seguenti azioni:

- Distruzione delle chiavi di sessione e del relativo materiale di chiave effimero;
- Chiusura del canale di comunicazione utilizzato per il recupero dei dati.

.. note::
  Vedi :ref:`credential-data-model:Formato Credenziale mdoc-CBOR` per il significato degli acronimi dei tipi CBOR.

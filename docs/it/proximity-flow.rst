.. include:: ../common/common_definitions.rst


Flusso di Prossimità
====================

Questa sezione descrive come un'App di Verifica richiede la presentazione di un Attestato Elettronico in formto  *mdoc-CBOR* a un'Istanza del Wallet secondo la *Specifica ISO 18013-5*.

La fase di presentazione è strutturata in tre ampie sotto-fasi come illustrato nella seguente figura:

.. plantuml:: plantuml/credential-presentation-high-level-flow.puml
    :width: 90%
    :alt: La figura illustra il Flusso di Presentazione in prossimità ad Alto Livello.
    :caption: `Flusso di Presentazione di Alto Livello in prossimità. <https://www.plantuml.com/plantuml/svg/VLBHYjim47pNLsppv8CcHzjxBELeOaYXK9DSANqoEccmHMN9bUHSJUc_T-qanWr9zIAyEpCxE_9ZJ3Aahh6qDLMz_8m3B1K14Ix9PBoZefOHufLnodOQz7xzSBz-ADU-QRrZq0SXjfysURb_odVvbwVlHPxT2P5Cig35VpKNGXG8qRkiYmYlQV6LhmNVZVQAQcyrVxAM-EWxfsNeitQcKRQ31gEl2D_HRq5y9fEPni4eb72LhD1mXOblLhGPovHFvM7y7geBe5Zxa9P1kWgal7DGuuHdf1V0qJTfBH99fsa7snjNKS59zeD2pg4-MnDhH3BE92CjnQEggYLBMTwB-5ouZ8XnM0rd_idfsnNjZotAvwrnbbEXRnFqtEIBIJKl80ENJwBq0_rnknIfQyz-CD5FkElEb6-QpXarfimgxrRSd9LeUSvoXnGC3jB-Qsvyqu2V7MAw3uYi6q7ufUenu8EHbmanVSlfMiIPIIsJd5XizOyGd7wvEVr2rvxv-009aU43TfTTGTrAtaBgICbFt1l0otpWk3kEV8JJNMF_0W00>`_


Le sotto-fasi sono descritte di seguito:

  1. **Device Engagement**: Questa sottofase inizia quando all'Utente viene richiesto di divulgare determinati attributi dall'mdoc(s). L'obiettivo di questa sottofase è stabilire un canale di comunicazione sicuro tra l'Istanza del Wallet e l'App di Verifica, in modo che le richieste e le risposte mdoc possano essere scambiate durante la sottofase di comunicazione.
  I messaggi scambiati in questa sottofase vengono trasmessi attraverso tecnologie a corto raggio per limitare la possibilità di intercettazione e ascolto non autorizzato.

  2. **Session Establishment**: Durante la fase di Session Establishment, l'App di Verifica configura una connessione sicura. In questa fase, tutti i dati trasmessi su questa connessione sono cifrati utilizzando una chiave di sessione che è nota sia all'Istanza del Wallet che all'App di Verifica.
  La sessione stabilita PUÒ essere terminata in base alle condizioni dettagliate in [`ISO18013-5`_ #9.1.1.4].

  3. **Comunicazione e Recupero del Dispositivo**: L'App di Verifica cripta la richiesta mdoc con l'appropriata chiave di sessione e la invia all'Istanza del Wallet insieme alla sua chiave pubblica in un messaggio di Session Establishment. L'mdoc utilizza i dati dal messaggio di Session Establishment per derivare la chiave di sessione e decifrare la richiesta mdoc.
  Durante la sottofase di comunicazione, l'App di Verifica ha l'opzione di richiedere informazioni dall'Istanza del Wallet utilizzando richieste e risposte mdoc. La modalità principale di comunicazione è il canale sicuro stabilito durante la configurazione della sessione. L'Istanza del Wallet cripta la risposta mdoc utilizzando la chiave di sessione e la trasmette al Relying Party mobile tramite una risposta mdoc contenente i Session Data.



Le App di Verifica e le Istanze Wallet registrate nell'ecosistema IT-Wallet DEVONO soddisfare almeno i seguenti requisiti:

- *Flusso di Recupero del Dispositivo Supervisionato* dove un supervisore umano supervisiona il processo di verifica in persona, in contrasto con il *flusso non supervisionato* dove la verifica potrebbe avvenire attraverso sistemi automatizzati senza supervisione umana.
- *Device Engagement* basato su QR Code.
- *Autenticazione dell'Istanza RP* seguendo i meccanismi definiti nell'`ISO18013-5`_ per l'*autenticazione del lettore*.
- Meccanismo di *Recupero del Dispositivo* basato su Bluetooth Low Energy (BLE) per la sottofase di comunicazione. Il meccanismo di *Recupero del Server* NON DEVE essere supportato.
- *Tipo di Documento* domestico e *Namespace* definiti in questa specifica tecnica in aggiunta a quelli già definiti nell'`ISO18013-5`_ per l'mDL (vedi :ref:`credential-data-model:Formato Credenziale mdoc-CBOR` per maggiori dettagli).
- *Validazione dell'Istanza del Wallet* attraverso la Wallet Attestation.

La seguente figura illustra il flusso di prossimità a basso livello conforme ad ISO 18013-5.

.. _fig_High-Level-Flow-ITWallet-Presentation-ISO-updated:
.. plantuml:: plantuml/credential-presentation-flow.puml
    :width: 99%
    :alt: La figura illustra il Flusso di Presentazione in prossimità a Basso Livello.
    :caption: `Flusso di Presentazione di Basso Livello in prossimità. <https://www.plantuml.com/plantuml/svg/ZLD1Qniz4BtxLmnx-WB9T-Wnb98qCQKqfQxTa4ilO-tOAx8xKgNHRltlEolP8DCOkWTZIJFllNbwkek2GTBGmvERRfvef1vMWIAne5Z7iEemqWAJE4x3bi9Y0VgX4HVWEL80Z93oNlxnYcQDzSW2pGlsFGayivLchfl-Bbclu3Eh1ZQKIyQ2dsu-JBVmpHE3T0H7e5FbIO8TKUY8cjxdbY8fQHChIHbXUtWB15oOJn1UDW_t5Mk1YDIJaPWRVN2_xM3b0BvsPfVOp7-mrwFSxxp0L-GMrPm3s1riX3oy0nk1dO2di7DXe5Pv2oleDwdmT45uLKRSblAiyHCnXNbufWd8TpJeieTNKere0_pa_vfc-KYZDVI53l-lWXsRvXhEDzEsQQvEgECjR3etvOc_h-71jGIMJPzQotjjB7rBtkDUsLYQvlmQnhmSRxA-ZK6kaSgPaloBT9YrhmbR2hNsUhFINc2LPV1922B5Q1tFUATKbg-grO1x30G8qUwPMa1kWTY4WvTv9HBiLi5KIw1VYQBCaZO5UHa5jxsDNJ7XgXxxKX6uaG9yV5f299C2WUcGcVhgHY_fBwUFbCLT9CWJA8VTQUuavhbGbEc8aIEsFiw2NXCzOW-QnbEaBU-FcQyDYDTgWN4in0hgTX1eRwE44az3GUnk3YjLp-V-Y5xdYhYzPBRIUyUHAeSVKL2DLUh9IWVb2ivrNJAqkkJQiWhs-asRvWVJve33rlAS-AkiqtHaNc5edG4ToRRbfPT7gnn7PFX1OR2SNSd7BTNFudnZMjmHjsde_m00>`_


**Passo 1**: L'Utente apre l'Istanza del Wallet avviando il processo.

**Passo 2**: L'Utente si autentica all'Istanza del Wallet. Questo può essere fatto dall'Istanza del Wallet o da un'Applicazione Crittografica Sicura (WSCA) del dispositivo Utente. È un prerequisito per accedere a dati sensibili e presentare attributi.

**Passo 3**: L'Utente seleziona la funzionalità di presentazione di prossimità.

**Passo 4**: [Opzionale] Se l'autenticazione iniziale nel Passo 2 non è stata effettuata tramite WSCA, PUÒ essere richiesta un'autenticazione separata tramite WSCA.

**Passo 5**: L'Istanza del Wallet genera una nuova coppia di chiavi crittografiche effimere per la comunicazione sicura. La chiave pubblica (``EDeviceKey.Pub``) sarà utilizzata per la crittografia della sessione. Questo fa parte del processo di Device Engagement.

**Passo 6**: L'Istanza del Wallet presenta un QR Code all'App di Verifica. Questo QR code contiene i dati ``DeviceEngagement``, che includono ``EDeviceKey.Pub`` e informazioni sulle suite di cifratura supportate.

Di seguito è riportato un esempio non normativo che utilizza ``DeviceEngagement`` codificato in CBOR che utilizza QR per il device engagement e Bluetooth Low Energy (BLE) per il recupero dei dati.

.. literalinclude:: ../../examples/iso-device-engagement.txt
  :language: text

**Passo 7**: Il verificatore utilizza la sua App di Verifica per scansionare il QR code e recuperare i dati ``DeviceEngagement`` dall'mdoc.

**Passo 8**: L'App di Verifica genera la sua coppia di chiavi effimere (``EReaderKey.Priv``, ``EReaderKey.Pub``). La chiave privata (``EReaderKey.Priv``) DEVE essere mantenuta segreta, e la chiave pubblica (``EReaderKey.Pub``) DEVE essere utilizzata nel Session Establishment.

**Passo 9**: L'Istanza del Wallet e l'App di Verifica DEVONO derivare indipendentemente le chiavi di sessione utilizzando la loro chiave effimera privata e la chiave effimera pubblica dell'altra parte attraverso un Key Agreement Protocol opportuno. Questo garantisce la cifratura della sessione. In questo passo, l'App di Verifica DEVE calcolare la sua chiave di sessione.

**Passo 10**: L'App di Verifica DEVE preparare un messaggio ``SessionEstablishment``. Questo messaggio DEVE essere firmato dall'App di Verifica (come specificato in [`ISO18013-5`_ #9.1.4 *mdoc reader authentication*]) e cifrato utilizzando le chiavi di sessione derivate nel passo precedente. Il messaggio di ``SessionEstablishment`` DEVE includere sia ``EReaderKey.Pub`` che una richiesta per specifici attributi.

Di seguito è riportato un esempio non normativo che utilizza la notazione diagnostica di un ``SessionEstablishment`` codificato in CBOR che contiene la richiesta mdoc di una Wallet Attestation insieme a una Credenziale Digitale mDL.

.. literalinclude:: ../../examples/iso-session-establishment.txt
  :language: text

**Passo 11**: L'App di Verifica DEVE trasmettere il messaggio ``SessionEstablishment`` cifrato e firmato all'Istanza del Wallet su una connessione BLE sicura stabilita sulla base delle informazioni contenute nel Device Engagement.

**Passo 12**: L'Istanza del Wallet DEVE calcolare la chiave di sessione, come descritto nel Passo 9.

**Passo 13**: Dopo aver ricevuto il messaggio ``SessionEstablishment``, l'Istanza del Wallet DEVE decifrarlo utilizzando la chiave di sessione condivisa e DEVE verificare la firma dell'App di Verifica (come specificato in [`ISO18013-5`_ #9.1.1.4 *mdoc reader authentication*]) per garantirne l'autenticità.

**Passo 14**: L'Istanza del Wallet DEVE decifrare la richiesta di attributi e DEVE chiedere all'Utente il consenso per il rilascio degli attributi richiesti. DEVE inoltre visualizzare il contenuto del Certificato di Registrazione dell'App di Verifica per garantire l'autenticità, la trasparenza sui dati richiesti e sul suo scopo registrato.

**Passo 15**: L'Utente esamina la richiesta e le informazioni di registrazione della Relying Party e poi approva la presentazione degli attributi richiesti.

**Passo 16**: Dopo aver ricevuto l'approvazione dell'Utente, l'Istanza del Wallet DEVE recuperare le Credenziali Digitali mdoc richieste. Quindi DEVE preparare un messaggio `SessionData` contenente queste Credenziali Digitali, e DEVE firmare i dati di autenticazione richiesti (come parte del processo di autenticazione mdoc, come specificato in [`ISO18013-5`_ #9.1.3]). DEVE criptarlo utilizzando le chiavi di sessione stabilite prima di trasmetterlo all'App di Verifica sul canale BLE sicuro. La firma garantisce il binding del dispositivo e l'integrità dei dati. La risposta mdoc DEVE essere codificata in CBOR, con la sua struttura delineata in [`ISO18013-5`_ #8.3.2.1.2.2].

Di seguito è riportato un esempio non normativo che utilizza la notazione diagnostica di un ``SessionData`` codificato in CBOR che contiene la risposta mdoc di una Wallet Attestation e un mDL.

.. literalinclude:: ../../examples/iso-session-data.txt
  :language: text

**Passo 17**: L'App di Verifica che riceve il ``SessionData`` DEVE decifrarlo, quindi verificare la firma dell'Istanza del Wallet per garantire sia l'integrità dei dati che la provenienza di essi dal dispositivo previsto (device binding). Essa DEVE anche controllare la validità dell'mdoc, inclusa la firma del suo Fornitore di Attestati Elettronici. In caso di Attestati Elettronici a lunga durata, DOVREBBE anche controllare lo stato di revoca utilizzando `TOKEN-STATUS-LIST`_.

**Passo 18**: Una volta completato lo scambio di dati, una delle parti può terminare la sessione. Se viene utilizzato BLE, questo può comportare l'invio di uno Stat Code per la terminazione della sessione o il comando ``End``. In questo scenario, il Client GATT (App di Verifica) DEVE disconnettersi dal Server GATT (Istanza del Wallet).

**Considerazione Finale**: Questo flusso di presentazione descrive lo scambio di dati in prossimità. È cruciale riconoscere che i flussi di prossimità supervisionati che coinvolgono un verificatore umano svolgono un ruolo vitale in molti casi d'uso (ad esempio, verifica dell'età in un negozio, controllo dell'identità da parte delle forze dell'ordine). L'elemento umano aggiunge un ulteriore livello di sicurezza riguardo l'identità dell'utente attraverso l'ispezione visiva e il confronto degli Attributi Elettronici presentati, contribuendo agli aspetti generali di garanzia dell'autenticazione non completamente catturati in un flusso di presentazione puramente tecnico.

.. note::
  Durante la presentazione di prossimità, l'Istanza del Wallet potrebbe non essere in grado di recuperare una Wallet Attestation aggiornato; in questo caso, l'Istanza del Wallet DOVREBBE inviare l'ultima versione della Wallet Attestation. È lasciato alla Relying Party determinare se una presentazione con una Wallet Attestation valido ma scaduto sia valida o meno.

Device Engagement
^^^^^^^^^^^^^^^^^

La struttura del Device Engagement DEVE essere codificata in CBOR e avere almeno le seguenti componenti:

.. list-table::
   :class: longtable
   :widths: 30 70
   :header-rows: 1

   * - **Componente**
     - **Descrizione**

   * - **Version**
     - *(tstr)*. Versione della struttura di Device Engagement.

   * - **Security**
     - *(array)*. Contiene due valori obbligatori:

       - *(int)*. Identificativo della suite di cifratura. Vedi Tabella 22 di `ISO18013-5`_.

       - *(bstr)*. Chiave pubblica effimera generata dall'Istanza del Wallet, utilizzata dall'App di Verifica per derivare la Chiave di Sessione. La chiave DEVE essere del tipo consentito dalla suite di cifratura selezionata.

   * - **BleOptions**
     - *(map)*. Fornisce opzioni per la connessione BLE, come la modalità Peripheral Server o Central Client, e l'UUID del dispositivo.

       Solo la `Modalità Central Client` DEVE essere supportata da questo profilo di implementazione.

   * - **Capabilities**
     - *(map)*. Dichiara le capacità opzionali supportate dall'mdoc, che sono:

       - **HandoverSessionEstablishmentSupport** *(bool)*. Se presente, DEVE essere impostato su `true`. Indica se sia possibile ricevere il messaggio `SessionEstablishment` durante il Negotiated Handover, come definito in [`ISO18013-5`_ #8.2.2.4].

       - **ReaderAuthAllSupport** *(bool)*. Se presente, DEVE essere impostato su `true`. Indica se sia possibile ricevere l'oggetto `ReaderAuthAll` nella richiesta mdoc, come definito in [`ISO18013-5`_ #8.3.2.1.2.1].

   * - **OriginInfos**
     - *(array)*. Descrive l'interfaccia utilizzata per ricevere e consegnare il messaggio di Device Engagement.

        Quando utilizzato nei flussi definiti in [`ISO18013-5`_ #6.3.2.1], `OriginInfos` PUÒ essere un array vuoto.


Richiesta mdoc
^^^^^^^^^^^^^^^

I messaggi nella Richiesta mdoc DEVONO essere codificati utilizzando CBOR. La stringa di byte CBOR risultante per la Richiesta mdoc DEVE essere cifrata con la Chiave di Sessione ottenuta dopo la fase di Device Engagement e DEVE essere trasmessa utilizzando il protocollo BLE.
Ogni Richiesta mdoc DEVE essere conforme alla seguente struttura e DEVE includere i seguenti componenti, a meno che non sia specificato diversamente:

.. list-table::
   :class: longtable
   :widths: 30 70
   :header-rows: 1

   * - **Componente**
     - **Descrizione**

   * - **version**
     - *(tstr)*. Versione della struttura della Richiesta mdoc. Consente di gestire la compatibilità tra diverse versioni o profili di implementazione.

   * - **docRequests**
     - *(array)*. Ogni voce è un oggetto `DocRequest` contenente:

       - **itemsRequest**. Oggetto `ItemsRequest` codificata in CBOR, formattata come:

         - **docType** *(tstr)*. Il tipo di documento richiesto. Vedi :ref:`credential-data-model:Attestato Elettronico in formato mdoc-CBOR`.

         - **nameSpaces** *(map)*. Una mappa di identificatori del *namespace* per i *DataElements* richiesti.

           Ogni voce in `DataElements` include:

           - **DataElementIdentifier** *(tstr)*. L'identificativo dell'elemento di dati richiesto.
           - **IntentToRetain** *(bool)*. Indica se la Relying Party intende conservare il valore dell'elemento di dati.

       - **readerAuth** *(COSE_Sign1, CONDIZIONALE)*. Utilizzato per autenticare l'App di Verifica per ogni `DocRequest`. La firma è calcolata sui dati `ReaderAuthentication`, come definito in [`ISO18013-5`_ #9.1.4].

         Questo componente DEVE essere presente solo se `readerAuthAll` non viene utilizzato.

   * - **readerAuthAll**
     - *(COSE_Sign1, CONDIZIONALE)*. Utilizzato per autenticare l'App di Verifica una volta per tutte le richieste in `DocRequest`. La firma è calcolata sui dati `ReaderAuthenticationAll`, come definito in [`ISO18013-5`_ #9.1.4].

       Questo componente DEVE essere presente solo se `ReaderAuthAllSupport` è impostato su `true` nel messaggio di DeviceEngagement, in questo caso, i campi individuali `readerAuth` non vengono utilizzati.

Risposta mdoc
^^^^^^^^^^^^^^

I messaggi nella Risposta mdoc DEVONO essere codificati utilizzando CBOR e DEVONO essere cifrati con la Chiave di Sessione ottenuta dopo la fase di Device Engagement.
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
     - *(array di Documents, OPZIONALE)*. Collezione di documenti codificati in CBOR restituiti in risposta alla richiesta mdoc. Ogni documento include i componenti `issuerSigned` e `deviceSigned`, e segue la struttura definita nella tabella sottostante.

   * - **documentErrors**
     - *(map, OPZIONALE)*. Una mappa di codici di errore per i documenti non restituiti, come definito in [`ISO18013-5`_ #8.3.2.1.2.3]. Ogni chiave è un `docType`, e ogni valore è un `ErrorCode` (int) che indica il motivo per cui il documento non è stato restituito.

   * - **status**
     - *(uint)*. Status Code che indica l'esito della richiesta. Ad esempio, `"status": 0` significa elaborazione riuscita. Per i dettagli, vedere la Tabella 8 (ResponseStatus) di [`ISO18013-5`_ #8.3.2.1.2].


Ogni elemento in **documents** DEVE essere conforme alla seguente struttura e DEVE includere i seguenti componenti, a meno che non sia specificato diversamente:

.. _table-mdoc-documents-attributes:
.. list-table::
   :class: longtable
   :widths: 30 70
   :header-rows: 1

   * - **Componente**
     - **Descrizione**

   * - **docType**
     - *(tstr)*. identificativo del tipo di documento. Ad esempio, per un mDL, il valore DEVE essere ``org.iso.18013.5.1.mDL``.

   * - **issuerSigned**
     - *(bstr)*. Contiene la struttura `IssuerNameSpaces`, che include elementi di dati firmati dal Fornitore di Attestati Elettronici, e la struttura `issuerAuth`, che garantisce la loro autenticità e integrità utilizzando il Mobile Security Object (MSO). Vedi :ref:`credential-data-model:Attestato Elettronico in formato mdoc-CBOR`.

   * - **deviceSigned**
     - *(bstr)*. Contiene la struttura `DeviceNameSpaces` (elementi di dati firmati dall'Istanza del Wallet), e la struttura `deviceAuth`, che include i dati di autenticazione firmati dall'Istanza del Wallet. Vedi la tabella sottostante per i dettagli.

   * - **errors**
     - *(map, OPZIONALE)*. Una mappa di codici di errore per ogni elemento di dati non restituito raggruppati per *namespace*. Ogni chiave rappresenta un namespace specifico, e ogni valore è una mappa di identificativi di elementi di dati ai corrispondenti codici di errore. Vedi [`ISO18013-5`_ #8.3.2.1.2.3] per i dettagli sulla struttura degli errori.



Una struttura di dati **deviceSigned** DEVE essere conforme alla seguente struttura e DEVE includere i seguenti componenti:

.. list-table::
   :class: longtable
   :widths: 25 75
   :header-rows: 1

   * - **Componente**
     - **Descrizione**

   * - **nameSpaces**
     - *(bstr)*. Contiene la struttura `DeviceNameSpaces`. PUÒ essere una struttura vuota. `DeviceNameSpaces` mappa l'identificativo del namespace a un insieme di elementi di dati firmati dall'Istanza del Wallet.

       Ogni namespace contiene uno o più elementi `DeviceSignedItem`, dove ciascun elemento include:

       - **DataItemName** *(tstr)*. L'identificativo dell'elemento di dati.
       - **DataItemValue** *(any)*. Il valore dell'elemento di dati.

   * - **deviceAuth**
     - *(COSE_Sign1)*. Contiene la struttura `DeviceAuth`, che DEVE includere la **deviceSignature** per l'autenticazione dell'Istanza del Wallet. La firma è calcolata sui dati `DeviceAuthentication`, che lega gli elementi restituiti alla sessione e alla richiesta. Vedi [`ISO18013-5`_ #9.1.3] per i dettagli sulla struttura di autenticazione.


Chiusura della Sessione
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

La sessione DEVE chiudersi qualora si verifichi almeno una delle seguenti condizioni:

- Dopo un timeout di inattività nel ricevere o inviare messaggi di Session Establishment o di SessionData. Il timeout per l'inattività implementato dall'Istanza del Wallet e dall'App di Verifica DOVREBBE essere non inferiore a 300 secondi;
- Quando l'Istanza del Wallet non accetta più richieste;
- Quando l'App di Verifica non invia ulteriori richieste.

Se l'Istanza del Wallet e l'App di Verifica non inviano o ricevono ulteriori richieste, la terminazione della sessione DEVE essere avviata come segue:

- Inviare il codice di stato per la terminazione della sessione, o
- Inviare il comando "End" come delineato in [`ISO18013-5`_ #8.3.3.1.1.5].

Quando una sessione viene terminata, l'Istanza del Wallet e l'App di Verifica DEVONO eseguire almeno le seguenti azioni:

- Distruzione delle chiavi di sessione e del relativo materiale di chiave effimero;
- Chiusura del canale di comunicazione utilizzato per il recupero dei dati.

.. note::
  Vedi :ref:`credential-data-model:Attestato Elettronico in formato mdoc-CBOR` per il significato degli acronimi dei tipi CBOR.

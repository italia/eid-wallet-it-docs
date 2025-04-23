Funzionalità
#############

Il Sistema IT-Wallet offre all’utente un’esperienza più semplice, veloce e sicura di accesso ai servizi. Tale servizio si concretizza per l’Utente nella possibilità di utilizzare una Soluzione IT-Wallet, la cui esperienza di fruizione è scandita in tre macro-fasi: pre-utilizzo, utilizzo e post-utilizzo. 

.. figure:: ../../images/UX-phases-usage-ITA.svg
   :name: Fasi dell’Esperienza Utente di utilizzo di una Istanza IT-Wallet 
   :alt: Fasi dell’Esperienza Utente di utilizzo di una Istanza IT-Wallet 
   :width: 100%

Le sezioni a seguire si focalizzano sulle macro-fasi di utilizzo e post-utilizzo. Esse definiscono i requisiti funzionali a supporto dell’Esperienza Utente relativi alle fasi di attivazione ottenimento, presentazione, gestione e disattivazione, unitamente ai requisiti di interazione con il servizio in termini di gestione degli errori, richiesta di assistenza e raccolta feedback. 

Le Risorse Ufficiali descrivono le modalità di interazione Utente - Istanza IT-Wallet e le buone pratiche di progettazione al fine di promuovere coerenza tra le diverse Soluzioni IT-Wallet, in termini di modalità di fruizione delle funzionalità. 

Attivazione dell’Istanza IT-Wallet 
************************************

L'attivazione è il passaggio necessario per abilitare l'Utente all'utilizzo delle funzionalità della Soluzione IT-Wallet per l’ottenimento, la presentazione e la gestione dei propri Attestati Elettronici in modo sicuro. Il processo di attivazione consiste in un’operazione di Autenticazione dell'Utente sull’Istanza IT-Wallet tramite la propria identità digitale che consente la generazione del PID.  

Di seguito i requisiti funzionali e di Esperienza Utente che il Wallet Provider DEVE garantire attraverso la propria Soluzione IT-Wallet: 

- l'Utente scarica la Soluzione IT-Wallet sul suo dispositivo così da generare la propria Istanza IT-Wallet; 
- l'Utente imposta un metodo di sblocco per la sua Istanza IT-Wallet se non è già stato impostato in precedenza nell’app. In aggiunta al PIN, l’Utente può decidere di usare il metodo di sblocco usato per il dispositivo e gestito a livello di sistema operativo (e.g. autenticazione biometrica) come alternativa al PIN. L’Utente utilizza il metodo di sblocco ogni qual volta è richiesta un’autorizzazione a garanzia della sicurezza e della protezione delle proprie informazioni; 
- l’Utente prende visione di tutte le informazioni rilevanti sull’attivazione e sulle modalità di utilizzo del servizio. L’Utente inoltre prende visione di eventuali informative del Fornitore di Soluzione IT-Wallet e del Fornitore di Dati di Identificazione Personale e/o termini e condizioni d’uso del servizio. L’Utente dà il proprio consenso per proseguire oppure lo nega per annullare l’operazione; 
- l’Utente sceglie una tra le modalità di Autenticazione disponibili; 
- l‘Utente conclude il flusso di Autenticazione sul servizio del National Identity Provider; 
- l’Utente riceve conferma dell’esito del processo di Autenticazione e, se positivo, visualizza l'anteprima del proprio PID. L'Utente conferma le informazioni mostrate in anteprima per procedere all’attivazione dell’Istanza IT-Wallet oppure annulla l’operazione; 
- l’Utente autorizza l’operazione utilizzando la modalità di sblocco precedentemente impostata; 
- l’Utente visualizza l’esito positivo dell’avvenuta attivazione dell’Istanza IT-Wallet. 

Il Fornitore di Soluzione IT-Wallet DEVE permettere all’Utente in ogni momento di rimuovere il PID ottenuto durante la fase di Attivazione. Inoltre, il Fornitore di Dati di Identificazione Personale DOVREBBE permettere all’Utente di revocare il PID ottenuto, tramite uno specifico Touchpoint. Il Fornitore di Soluzione IT-Wallet DEVE permettere all’Utente di richiedere la disattivazione della propria Istanza IT-Wallet, anche in assenza del dispositivo su cui è stata installata. Per approfondimenti si rimanda alle sezioni :ref:`Disattivazione dell’Istanza IT-Wallet` e :ref:`Gestione degli Attestati Elettronici`. 

In caso di errori nell’utilizzo della Istanza IT-Wallet, il Fornitore di Soluzione IT-Wallet DEVE garantire all’Utente la visualizzazione di messaggi coerenti che lo informino e guidino alla loro risoluzione. Per approfondimenti si rimanda alla sezione :ref:`Gestione errori`.

Ottenimento degli Attestati Elettronici di Attributi 
#####################################################

Ad attivazione conclusa, l'Utente PUÒ ottenere uno o più Attestati Elettronici di Attributi all'interno della sua Istanza IT-Wallet. 

A seconda delle specifiche esigenze dell’Utente, della tipologia di Attestato Elettronico di Attributi e delle disponibilità offerte dal Fornitore di Soluzione IT-Wallet, dal Fornitore di Attestati Elettronici di Attributi e dal Titolare di Fonte Autentica, l’ottenimento degli Attestati Elettronici di Attributi può avvenire attraverso due modalità: 

- **dal Catalogo dell’Istanza IT-Wallet**: l’Utente esplora l’elenco degli Attestati Elettronici di Attributi messi a disposizione dalla Soluzione IT-Wallet, seleziona quello di suo interesse e avvia la procedura di richiesta che si conclude con l’ottenimento dell’Attestato Elettronico di Attributi nell’Istanza IT-Wallet; 

- **da un Touchpoint del Titolare di Fonte Autentica** (o del Fornitore di Attestati Elettronici di Attributi qualora coincida con il Titolare di Fonte Autentica): l’Utente interagisce col servizio digitale del Titolare di Fonte Autentica che gli permette di ottenere nella sua Istanza IT-Wallet uno specifico Attestato Elettronico di Attributi tramite un Pulsante di Ingaggio.  

Nonostante le modalità di avvio della richiesta siano diverse, i flussi di ottenimento condividono una struttura e un processo simili. Di seguito, sono illustrati i requisiti funzionali a supporto dell’Esperienza Utente del flusso di ottenimento di un Attestato Elettronico di Attributi dal Catalogo che il Fornitore di Soluzione IT-Wallet DEVE garantire attraverso la propria Soluzione IT-Wallet: 

- l’Utente accede alla propria Istanza IT-Wallet utilizzando la modalità di sblocco precedentemente impostata; 
- l’Utente seleziona l’Attestato Elettronico di Attributi che intende aggiungere alla sua Istanza IT-Wallet scegliendo tra quelli disponibili nel Catalogo; 
- l’Utente prende visione dei dati del PID, qualora richiesti dal Titolare di Fonte Autentica per l'ottenimento dell’Attestato Elettronico di Attributi, il nome del relativo Fornitore di Attestati Elettronici di Attributi e di eventuali informative.  L’Utente dà il proprio consenso per poter proseguire presentando i dati del PID o altri Attributi al Fornitore di Attestati Elettronici di Attributi oppure annulla l’operazione; 
- l’Utente visualizza l'anteprima dell’Attestato Elettronico di Attributi. L'Utente conferma i dati mostrati in anteprima per procedere all’ottenimento oppure annulla l’operazione; 
- l’Utente autorizza l’operazione utilizzando la modalità di sblocco precedentemente impostata; 
- l’Utente visualizza l’esito positivo dell’ottenimento avvenuto; 
- l’Utente visualizza i dettagli dell’Attestato Elettronico di Attributi ottenuto ovvero: i dati in esso contenuti, il nome del Fornitore di Attestati Elettronici di Attributi che ha emesso l'Attestato Elettronico di Attributi e il nome del Titolare di Fonte Autentica; 
- l’Utente ha evidenza di tutti gli Attestati Elettronici ottenuti navigando la sua Istanza IT-Wallet. 

Il Fornitore di Soluzione IT-Wallet DEVE permettere all’Utente di rimuovere un Attestato Elettronico di Attributi dalla sua Istanza IT-Wallet in ogni momento. In caso di assenza del dispositivo su cui è stata attivata l’Istanza IT-Wallet, il Fornitore di Soluzione IT-Wallet DEVE permettere all’Utente di disattivare l’intera Istanza IT-Wallet tramite un Touchpoint dedicato. Inoltre, i Fornitori di Attestati Elettronici di Attributi DOVREBBERO permettere all’Utente la revoca degli Attestati Elettronici ottenuti, tramite specifici Touchpoint. Per approfondimenti si rimanda alle sezioni Disattivazione dell’Istanza IT-Wallet e Gestione degli Attestati Elettronici. 

In caso di problemi di comunicazione tra i sistemi del Fornitore di Attestati Elettronici di Attributi e del Titolare di Fonte Autentica o in presenza di processi amministrativi o tecnici che non consentono di fornire immediatamente l’Attestato Elettronico di Attributi, gli attori coinvolti POSSONO gestire il flusso di ottenimento in modalità differita. In questo caso, il Fornitore di Soluzione IT-Wallet DEVE garantire che: 

- l’Utente, giunto all’ultimo step del processo, visualizzi un messaggio che lo invita ad attendere il momento in cui l’Attestato Elettronico di Attributi potrà essere rilasciato; 
- l’Utente venga informato dal Fornitore di Attestati Elettronici di Attributi non appena l’Attestato Elettronico di Attributi è disponibile. 

In caso di dati errati all’interno di un Attestato Elettronico di Attributi già ottenuto o in fase di ottenimento, il Fornitore di Soluzione IT-Wallet DOVREBBE garantire all’Utente un’adeguata assistenza attraverso la propria Istanza IT-Wallet. Per approfondimenti si rimanda alla sezione :ref:`Assistenza Utente`. 

In caso di errori nell’utilizzo della Istanza IT-Wallet, il Fornitore di Soluzione IT-Wallet DEVE garantire all’Utente la visualizzazione di messaggi coerenti che lo informino e guidino alla loro risoluzione. Per approfondimenti si rimanda alla sezione :ref:`Gestione degli errori`. 

Qualora un Titolare di Fonte Autentica (o un Fornitore di Attestati Elettronici di Attributi qualora coincida con il Titolare di Fonte Autentica) intendesse implementare un Pulsante di Ingaggio per permettere l’avvio del processo di ottenimento da un proprio Touchpoint, questo DEVE garantire il rispetto dei requisiti relativi all’aspetto grafico e alle modalità di implementazione del Pulsante di Ingaggio, descritti nella sezione :ref:`Brand Identity del Sistema IT-Wallet`. 

Layout degli Attestati Elettronici 
===================================

Gli Attestati Elettronici ottenuti in un’Istanza IT-Wallet DOVREBBERO essere visualizzati in lista all’interno di una Vista di Anteprima. In tal caso, gli Attestati Elettronici DEVONO garantire un alto livello di riconoscibilità e accessibilità [RIF_ACCESSIBILITÀ] delle informazioni contenute. Di seguito i requisiti relativi alle modalità di visualizzazione di un’Attestato Elettronico che ogni Fornitore di Soluzione IT-Wallet DEVE rispettare per garantire un’esperienza di consultazione e fruizione coerente e accessibile: 
 
- l’Attestato Elettronico DEVE essere visualizzato correttamente su qualsiasi dispositivo, garantendo un'esperienza uniforme su schermi di diverse dimensioni; 
- il nome dell’Attestato Elettronico DEVE essere chiaramente indicato e sempre visibile sia nella Vista di Dettaglio che nella Vista di Anteprima; 
- l’Attestato Elettronico, sia nella Vista di Anteprima che nella Vista di Dettaglio, DEVE mostrare lo stato se diverso da valido e PUÒ mostrarlo se valido. La Vista di Anteprima PUÒ includere alcuni Attributi per migliorarne l’esperienza di utilizzo e di gestione; PUÒ, ad esempio, includere il nome o il logo del Fornitore di Attestati Elettronici di Attributi o del Fornitore di Dati di Identificazione Personale; 
- il layout degli elementi nella Vista di Anteprima dell’Attestato Elettronico DEVE essere ottimizzato considerando il principio di scalabilità e usabilità, soprattutto in presenza di più Attestati Elettronici nella stessa schermata; 
- l’Attestato Elettronico PUÒ assumere un formato a card, in linea con gli approcci già adottati da altri Wallet sul mercato, per richiamare l'aspetto di un eventuale documento fisico corrispondente. Quando possibile, PUÒ essere dichiarata la natura digitale del documento, ad esempio riportando nel layout la dicitura “versione digitale”; 
- l’Attestato Elettronico DEVE includere nella Vista di Dettaglio gli stessi dati mostrati nella Vista di Anteprima e PUÒ includerne altri; 
- l’Attestato Elettronico DEVE prevedere nella Vista di Dettaglio la presenza di Pulsanti di Azione per garantirne la gestione, come descritto nella sezione :ref:`Gestione degli Attestati Elettronici`. 

Presentazione degli Attestati Elettronici 
******************************************
  
Il processo di presentazione permette all’Utente di accedere a un servizio o di dimostrare la titolarità di un dato o la sua idoneità a effettuare una determinata azione. La presentazione degli Attestati Elettronici e la loro conseguente verifica, prevede l'interazione tra due soggetti, l'Utente e il Verificatore di Attestati Elettronici, e può avvenire in due modalità principali a seconda delle circostanze e del contesto di interazione: 

- **Presentazione in prossimità**: l'Utente presenta il PID e/o un set di Attributi contenuti in uno o più Attestati Elettronici tramite l'Istanza IT-Wallet direttamente a un Verifier o a un dispositivo del Verificatore di Attestati Elettronici preposto alla verifica in presenza; 

- **Presentazione da remoto**: l'Utente presenta il PID e/o un set di Attributi contenuti in uno o più Attestati Elettronici tramite l'Istanza IT-Wallet ad un Verificatore di Attestati Elettronici predisposto per la verifica online al fine, ad esempio, di Autenticarsi e fruire dei servizi erogati. 

Presentazione in prossimità 
****************************

La presentazione in prossimità consente all'Utente di esibire il PID e/o un set di Attributi contenuti in uno o più Attestati Elettronici tramite la propria Istanza IT-Wallet, secondo due diverse modalità: 

- **Modalità supervisionata**: l'Utente, tramite l’Istanza IT-Wallet, presenta il PID e/o uno o più Attestati Elettronici di Attributi, a un Verificatore di Attestati Elettronici dotato di un’apposita app o sistema di verifica (e.g. agente delle forze dell’ordine, farmacista, etc.); 

- **Modalità non supervisionata**: l’Utente, tramite l’Istanza IT-Wallet, presenta il PID e/o un set di Attributi contenuti in uno o più Attestati Elettronici a un dispositivo preposto (e.g. tornello, ATM, etc.). 

Di seguito i requisiti funzionali a supporto dell’Esperienza Utente relativi a entrambe le modalità che il Fornitore di Soluzione IT-Wallet DEVE garantire attraverso la propria Soluzione IT-Wallet. 

**Modalità supervisionata** 

- L’Utente accede alla propria Istanza IT-Wallet utilizzando la modalità di sblocco precedentemente impostata; 
- l'Utente accede alla funzionalità dedicata alla generazione del QR Code; 
- l'Utente mostra il QR Code generato al soggetto che opera per conto del Verificatore di Attestati Elettronici, il quale provvede a scansionarlo tramite apposita app o sistema di verifica; 
- l’Utente prende visione dei dati del PID e/o degli Attributi richiesti per la presentazione, del nome del Verificatore di Attestati Elettronici che li richiede e delle relative eventuali informative. L’Utente sceglie se presentare o meno eventuali dati del PID o Attributi non obbligatori ai fini della presentazione (Divulgazione Selettiva). L’Utente dà il proprio consenso per poter proseguire oppure annulla l’operazione; 
- l’Utente autorizza l’operazione utilizzando la modalità di sblocco precedentemente impostata; 
- l’Utente visualizza l’esito positivo della presentazione avvenuta. 

In caso di errori nell’utilizzo dell’Istanza IT-Wallet, il Fornitore di Soluzione IT-Wallet DEVE garantire all’Utente la visualizzazione di messaggi coerenti che lo informino e guidino alla loro risoluzione. Per approfondimenti si rimanda alla sezione :ref:`Gestione degli errori`. 

**Modalità non supervisionata** 

- L’Utente accede alla propria Istanza IT-Wallet utilizzando la modalità di sblocco precedentemente impostata; 
- l'Utente accede alla funzionalità dedicata alla generazione del QR Code; 
- l'Utente mostra il QR Code generato al dispositivo preposto (ad esempio un tornello) del Verificatore di Attestati Elettronici per permetterne la scansione;  
- l’Utente prende visione dei dati del PID e/o gli Attributi richiesti per la presentazione, del nome del Verificatore di Attestati Elettronici che li richiede e delle relative eventuali informative. L’Utente sceglie se presentare o meno eventuali dati del PID o degli Attributi non obbligatori ai fini della presentazione (Divulgazione Selettiva). L’Utente dà il proprio consenso per poter proseguire oppure annulla l’operazione; 
- l’Utente autorizza l’operazione utilizzando la modalità di sblocco precedentemente impostata; 
- l’Utente visualizza l’esito positivo della presentazione avvenuta. 

In caso di errori nell’utilizzo dell’Istanza IT-Wallet, il Fornitore di Soluzione IT-Wallet DEVE garantire all’Utente la visualizzazione di messaggi coerenti che lo informino e guidino alla loro risoluzione. Per approfondimenti si rimanda alla sezione :ref:`Gestione degli errori`. 

Presentazione da remoto 
========================

La presentazione da remoto consente all'Utente di esibire il PID e/o un set di Attributi contenuti in uno o più Attestati Elettronici, facendo interagire la propria Istanza IT-Wallet con il Touchpoint di un Verificatore di Attestati Elettronici, tramite un apposito Pulsante di Ingaggio.  

Tale presentazione può avvenire in due diverse modalità, sulla base del tipo di dispositivo utilizzato per accedere al servizio di interesse: 

- **Stesso dispositivo**: nel caso in cui l’Utente voglia accedere a un servizio digitale online utilizzando lo stesso dispositivo su cui ha installato l’Istanza IT-Wallet; 
- **Cross-dispositivo**: nel caso in cui l'Utente voglia accedere a un servizio digitale utilizzando un dispositivo differente rispetto a quello in cui ha installato l’Istanza IT-Wallet. 

Di seguito i requisiti funzionali a supporto dell’Esperienza Utente relativi a entrambe le modalità che il Fornitore di Soluzione IT-Wallet DEVE garantire attraverso la propria Soluzione IT-Wallet. 

**Stesso dispositivo** 

L'Utente clicca sul Pulsante di Ingaggio reso disponibile nel Touchpoint del Verificatore di attestati elettronici; 

- l’Utente accede alla propria Istanza IT-Wallet utilizzando la modalità di sblocco precedentemente impostata; 
- l’Utente prende visione dei dati del PID e/o gli Attributi richiesti per la presentazione, del nome del Verificatore di Attestati Elettronici che li richiede e delle relative eventuali informative. L’Utente sceglie se presentare o meno eventuali dati del PID e/o Attributi non obbligatori ai fini della presentazione (Divulgazione Selettiva). L’Utente dà il proprio consenso per poter proseguire oppure annulla l’operazione; 
- l’Utente autorizza l’operazione utilizzando la modalità di sblocco precedentemente impostata; 
- l’Utente visualizza nell’Istanza IT-Wallet l’esito positivo della presentazione avvenuta; 
- l’Utente torna al flusso nel Touchpoint del Verificatore di Attestati Elettronici su cui DEVE visualizzare l’esito della presentazione completata. 

In caso di errori nell’utilizzo dell’Istanza IT-Wallet, il Fornitore di Soluzione IT-Wallet DEVE garantire all’Utente la visualizzazione di messaggi coerenti che lo informino e guidino alla loro risoluzione. Per approfondimenti si rimanda alla sezione :ref:`Gestione degli errori`. 


**Cross-dispositivo** 

- L’Utente clicca il Pulsante di Ingaggio reso disponibile nel Touchpoint del Verificatore di Attestati Elettronici che l’Utente sta navigando da un dispositivo diverso da quello su cui è installata l’Istanza IT-Wallet; 
- l’Utente accede all’Istanza IT-Wallet che desidera utilizzare dal dispositivo su cui è installata utilizzando la modalità di sblocco precedentemente impostata; 
- l’Utente inquadra il QR Code reso disponibile dal Verificatore di Attestati Elettronici, utilizzando la sua Istanza IT-Wallet; 
- l’Utente prende visione dei dati del PID e/o degli Attributi richiesti per la presentazione, del nome del Verificatore di Attestati Elettronici che li richiede e delle relative eventuali informative. L’Utente sceglie se presentare o meno eventuali dati del PID e/o Attributi non obbligatori ai fini della presentazione (Divulgazione Selettiva). L’Utente dà il proprio consenso per poter proseguire oppure annulla l’operazione; 
- l’Utente autorizza l’operazione utilizzando la modalità di sblocco precedentemente impostata; 
- l’Utente visualizza nell’Istanza IT-Wallet l’esito positivo della presentazione avvenuta; 
- l'Utente torna sul Touchpoint del Verificatore di Attestati Elettronici e visualizza l'esito della presentazione completata. 

In caso di errori nell’utilizzo dell’Istanza IT-Wallet, il Fornitore di Soluzione IT-Wallet DEVE garantire all’Utente la visualizzazione di messaggi coerenti che lo informino e guidino alla loro risoluzione. Per approfondimenti si rimanda alla sezione :ref:`Gestione degli errori`. 

Autenticazione 
...............

L'Autenticazione è un caso d’uso specifico della presentazione remota e consente all’Utente di accedere in modo sicuro ai servizi resi disponibili da Verificatori di Attestati Elettronici pubblici e privati, presentando il PID ed eventualmente un set di Attributi contenuti negli Attestati Elettronici di Attributi ottenuti. Questo garantisce all’Utente il pieno controllo sui propri dati e la possibilità di condividere anche i soli dati strettamente necessari alla verifica da parte del Verificatore di Attestati Elettronici garantendo a quest’ultimo l’affidabilità, l’autenticità e la validità dei dati presentati. 

Il processo di Autenticazione può avvenire in entrambe le modalità stesso dispositivo e cross-dispositivo descritte sopra. Per quanto riguarda i requisiti funzionali a supporto dell’Esperienza Utente, si DEVONO rispettare gli stessi requisiti previsti per la presentazione in remoto nelle due modalità (stesso dispositivo e cross-dispositivo). 

Infatti, a livello di Esperienza Utente, il processo di Autenticazione si distingue da un generico flusso di presentazione principalmente per le modalità di avvio del processo, in questo caso reso possibile a partire da uno specifico pulsante, il Pulsante di Autenticazione. 

Al fine di garantire un processo di Autenticazione adeguato e coerente tra tutti i Verificatori di Attestati Elettronici, ciascun Verificatore di Attestati Elettronici DEVE rispettare i requisiti relativi all’aspetto grafico e all’Esperienza Utente descritti di seguito e DOVREBBE utilizzare le Risorse Ufficiali open source. 

Qualora i Verificatori di Attestati Elettronici non intendano utilizzare tali risorse open source, POSSONO sviluppare in autonomia le Soluzioni Tecniche abilitanti il flusso di Autenticazione ma DEVONO rispettare i requisiti sotto dettagliati, unitamente al rispetto di [RIF_ACCESSIBILITÀ] e, nel caso di enti pubblici, delle [LG_DESIGN].   
 
I Verificatori di Attestati Elettronici, in ogni caso, DEVONO abilitare il processo di Autenticazione rendendo disponibili le seguenti pagine: 

- **Discovery Page**: ha l’obiettivo di mostrare all’Utente tutti i metodi di Autenticazione disponibili; 
- **QR code page** (*solo per modalità cross-dispositivo*): ha lo scopo di invitare l’Utente a inquadrare il codice QR;  
- **waiting page** (*solo per modalità cross-dispositivo*): ha lo scopo di invitare l’Utente a continuare il processo di Autenticazione sulla propria Istanza IT-Wallet; 
- **thank you page**: ha lo scopo di comunicare all’Utente l'avvenuta Autenticazione; 
- **error page**: ha lo scopo di comunicare all’Utente eventuali errori legati al flusso di Autenticazione. 

Tali pagine DEVONO prevedere elementi trasversali ricorrenti, in continuità con l’Identità Visiva del Touchpoint del Verificatore di Attestati Elettronici, in particolare: 

- un **header e/o un subheader**, che permette all'Utente di tornare alla pagina precedente; 
- un **footer** che include l’informativa privacy, le note legali e la Dichiarazione di Accessibilità, ove previsto da normativa. 

Di seguito invece gli elementi specifici caratteristici delle diverse pagine. 

**Discovery Page** 

Per garantire l’Autenticazione tramite il Sistema IT-Wallet, il Verificatore di Attestati Elettronici PUÒ aggiornare la propria Discovery Page con quella resa disponibile nelle Risorse Ufficiali. In alternativa, il Verificatore di Attestati Elettronici PUÒ mantenere la propria Discovery Page, ma DEVE in ogni caso integrare il Pulsante di Autenticazione, come da indicazioni presenti nella sezione :ref:`Pulsante di Autenticazione`. In ogni caso: 

- la pagina DEVE presentare tutte le modalità di Autenticazione attraverso l’identità digitale tra cui la modalità di Autenticazione del Sistema IT-Wallet, quindi tramite il Pulsante di Autenticazione; 
- la pagina PUÒ presentare anche modalità di Autenticazione alternative, se disponibili; 
- la pagina DOVREBBE garantire informazioni minime a supporto, per permettere all’Utente di compiere una scelta consapevole e informata. 

Nel caso l’Utente stia navigando la pagina del Verificatore di Attestati Elettronici da un Touchpoint diverso da quello su cui ha attivato l’Istanza IT-Wallet (modalità cross-dispositivo), la scelta di Autenticazione tramite il Sistema IT-Wallet DEVE condurre l’Utente alla QR code page. 

Nel caso in cui invece l’Utente stia navigando la pagina del Verificatore di Attestati Elettronici dallo stesso Touchpoint su cui ha attivato l’Istanza IT-Wallet (modalità stesso dispositivo) tale pagina DEVE condurre l’Utente all’apertura della propria Istanza IT-Wallet. 

 

**QR code page** (*solo per modalità cross-dispositivo*) 

La QR code page è la pagina su cui atterra l’Utente che ha scelto l’Autenticazione tramite il Sistema IT-Wallet in un flusso cross-dispositivo, e ha lo scopo di invitare l’Utente a scannerizzare, con la propria Istanza IT-Wallet, il codice QR generato. 

Il Verificatore di Attestati Elettronici DOVREBBE implementare la QR code page resa disponibile nelle Risorse Ufficiali. In ogni caso: 

- la pagina DEVE includere gli elementi propri dell'Identità Visiva del Sistema IT-Wallet, tra cui il Logo; 
- la pagina DEVE esporre il codice QR e un testo sintetico e chiaro che inviti l'Utente a scannerizzarlo con la propria Istanza IT-Wallet; 
- la pagina DEVE includere un testo sintetico e chiaro che permetta all’Utente di conoscere la validità temporale del codice QR;  
- la pagina DEVE includere una Call to Action che, in caso di timeout, permetta all’Utente di generare un nuovo codice QR; 
- la pagina DEVE includere una Call to Action che permetta all’Utente di annullare l’operazione e tornare alla Discovery Page. 

Per garantire la leggibilità del codice QR: 

- si DEVENO rispettare le dimensioni minime raccomandate per garantire una scansione efficace. Una misura di 150x150 pixel è generalmente adeguata, ma per codici con alta densità di dati (e.g. URL lunghi o numerosi caratteri), è consigliabile aumentarla a 300x300 pixel o più; 
- si DEVE mantenere un contrasto adeguato tra il codice QR e lo sfondo (la condizione ideale prevede uno sfondo bianco con un codice QR nero); 
- si DEVONO evitare inversioni di colore tra sfondo e codice QR; 
- si DEVE limitare la presenza a un solo codice QR per pagina; 
- il codice QR DEVE essere nitido e di alta qualità (si consiglia il formato SVG); 
- non gli si DEVE sovrapporre testo o altri elementi che lo possano nascondere parzialmente. 

**Waiting page** (*solo per modalità cross-dispositivo*) 

La waiting page è la pagina che invita l’Utente a proseguire il processo di Autenticazione sulla propria Istanza IT-Wallet, a valle della scansione del codice QR. 

Il Verificatore di Attestati Elettronici DOVREBBE implementare la waiting page (cross-dispositivo) resa disponibile nelle Risorse Ufficiali. In ogni caso: 

- la pagina DEVE includere gli elementi propri dell'Identità Visiva del Sistema IT-Wallet, tra cui il Logo e un’icona o altro elemento grafico che aiuti a veicolare il messaggio della pagina; 
- la pagina DEVE prevedere un testo sintetico e chiaro che lo inviti a proseguire sulla sua Istanza IT-Wallet. 

**Thank you page** 

La thank you page è la pagina sui cui l’Utente atterra una volta concluso il processo di Autenticazione attraverso la propria Istanza IT-Wallet e ha l’obiettivo di invitare l’Utente a proseguire nell’area riservata.  

Il Verificatore di Attestati Elettronici DOVREBBE implementare la thank you page resa disponibile nelle Risorse Ufficiali. In ogni caso: 

- la pagina DEVE includere gli elementi propri dell'Identità Visiva del Sistema IT-Wallet, tra cui il Logo e un’icona o altro elemento grafico che aiuti a veicolare il messaggio della pagina; 
- la pagina DEVE prevedere un testo sintetico e chiaro che spieghi all’Utente che il processo di Autenticazione si è concluso con successo; 
- la pagina DEVE prevedere una Call to Action che inviti l’Utente a proseguire nell’area riservata del Verificatore di Attestati Elettronici. 

**Error page** 
La pagina di errore rappresenta quella tipologia di pagina su cui l'Utente atterra in caso di errori nel corso del flusso di Autenticazione, e ha lo scopo di comunicare all'Utente la natura di tali errori (es. errore tecnico, assenza di rete, malfunzionamento dell’Istanza IT-Wallet, consenso alla presentazione dei dati negato etc.) e di presentare le azioni che l’Utente può intraprendere. Per approfondimenti sulle casistiche di errore si rimanda alla sezione :ref:`Gestione degli errori`. 
 
Il Verificatore di Attestati Elettronici DOVREBBE implementare la error page resa disponibile nelle Risorse Ufficiali. In ogni caso: 

- la pagina DEVE includere gli elementi propri dell'Identità Visiva del Sistema IT-Wallet, tra cui il Logo e un’icona o altro elemento grafico che aiuti a veicolare la natura dell'errore; 
- la pagina DEVE prevedere un testo sintetico e chiaro che spieghi all’Utente la natura dell’errore, il codice errore e una sua spiegazione semplice; 
- la pagina DEVE prevedere una o più Call to Action che invitino l’Utente a intraprendere le azioni previste (es. riprova, contatta l'assistenza, etc.). 
 

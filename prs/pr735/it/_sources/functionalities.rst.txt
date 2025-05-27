.. include:: ../common/common_definitions.rst
  

Funzionalità
============

Il Sistema IT-Wallet offre all'utente un'esperienza più semplice, veloce e sicura di accesso ai servizi. Tale servizio si concretizza per l'Utente nella possibilità di utilizzare una Soluzione IT-Wallet, la cui esperienza di fruizione è scandita in tre macro-fasi: pre-utilizzo, utilizzo e post-utilizzo. 

.. only:: format_html

  .. figure:: ./images/svg/UX-phases-usage.svg
    :alt: Fasi dell'Esperienza Utente di utilizzo di una Istanza IT-Wallet 
    :width: 100%

    Fasi dell'Esperienza Utente di utilizzo di una Istanza IT-Wallet 

.. only:: format_latex

  .. figure:: ./images/pdf/UX-phases-usage.pdf
    :alt: Fasi dell'Esperienza Utente di utilizzo di una Istanza IT-Wallet 
    :width: 100%

    Fasi dell'Esperienza Utente di utilizzo di una Istanza IT-Wallet 

Le sezioni a seguire si focalizzano sulle macro-fasi di utilizzo e post-utilizzo. Esse definiscono i requisiti funzionali a supporto dell'Esperienza Utente relativi alle fasi di attivazione ottenimento, presentazione, gestione e disattivazione, unitamente ai requisiti di interazione con il servizio in termini di gestione degli errori, richiesta di assistenza e raccolta feedback. 

Le Risorse Ufficiali descrivono le modalità di interazione Utente - Istanza IT-Wallet e le buone pratiche di progettazione al fine di promuovere coerenza tra le diverse Soluzioni IT-Wallet, in termini di modalità di fruizione delle funzionalità. 

Attivazione dell'Istanza IT-Wallet 
----------------------------------

L'attivazione è il passaggio necessario per abilitare l'Utente all'utilizzo delle funzionalità della Soluzione IT-Wallet per l'ottenimento, la presentazione e la gestione dei propri Attestati Elettronici in modo sicuro. Il processo di attivazione consiste in un'operazione di Autenticazione dell'Utente sull'Istanza IT-Wallet tramite la propria identità digitale che consente la generazione del PID.  

Di seguito i requisiti di Esperienza Utente che il Wallet Provider DEVE garantire attraverso la propria Soluzione IT-Wallet: 

- l'Utente scarica la Soluzione IT-Wallet sul suo dispositivo così da generare la propria Istanza IT-Wallet; 
- l'Utente imposta un metodo di sblocco per la sua Istanza IT-Wallet se non è già stato impostato in precedenza nell'app. In aggiunta al PIN, l'Utente può decidere di usare il metodo di sblocco usato per il dispositivo e gestito a livello di sistema operativo (e.g. autenticazione biometrica) come alternativa al PIN. L'Utente utilizza il metodo di sblocco ogni qual volta è richiesta un'autorizzazione a garanzia della sicurezza e della protezione delle proprie informazioni; 
- l'Utente prende visione di tutte le informazioni rilevanti sull'attivazione e sulle modalità di utilizzo del servizio. L'Utente inoltre prende visione di eventuali informative del Fornitore di Soluzione IT-Wallet e del Fornitore di Dati di Identificazione Personale e/o termini e condizioni d'uso del servizio. L'Utente dà il proprio consenso per proseguire oppure lo nega per annullare l'operazione; 
- l'Utente sceglie una tra le modalità di Autenticazione disponibili; 
- l‘Utente conclude il flusso di Autenticazione sul servizio del National Identity Provider; 
- l'Utente riceve conferma dell'esito del processo di Autenticazione e, se positivo, visualizza l'anteprima del proprio PID. L'Utente conferma le informazioni mostrate in anteprima per procedere all'attivazione dell'Istanza IT-Wallet oppure annulla l'operazione; 
- l'Utente autorizza l'operazione utilizzando la modalità di sblocco precedentemente impostata; 
- l'Utente visualizza l'esito positivo dell'avvenuta attivazione dell'Istanza IT-Wallet. 

Il Fornitore di Soluzione IT-Wallet DEVE permettere all'Utente in ogni momento di rimuovere il PID ottenuto durante la fase di Attivazione. Inoltre, il Fornitore di Dati di Identificazione Personale DOVREBBE permettere all'Utente di revocare il PID ottenuto, tramite uno specifico Touchpoint. Il Fornitore di Soluzione IT-Wallet DEVE permettere all'Utente di richiedere la disattivazione della propria Istanza IT-Wallet, anche in assenza del dispositivo su cui è stata installata. Per approfondimenti si rimanda alle sezioni :ref:`functionalities:Disattivazione dell'Istanza IT-Wallet` e :ref:`functionalities:Gestione degli Attestati Elettronici`. 

In caso di errori nell'utilizzo della Istanza IT-Wallet, il Fornitore di Soluzione IT-Wallet DEVE garantire all'Utente la visualizzazione di messaggi coerenti che lo informino e guidino alla loro risoluzione. Per approfondimenti si rimanda alla sezione :ref:`functionalities:Gestione degli errori`.

Focus sul PID – Dati di Identificazione della Persona
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Il PID (Person Identification Data) si riferisce a un set minimo verificato di informazioni sull'identità dell'Utente (vedere :ref:`credential-data-model:Modello di Dati delle Credenziali Elettroniche`) emesso come risultato del processo di attivazione e reso disponibile nell'Istanza Wallet.
Di seguito sono riportati i requisiti per la visualizzazione e l'utilizzo del PID a cui ogni Fornitore Wallet DEVE aderire, al fine di fornire un'esperienza di consultazione e utilizzo coerente e accessibile:

- Il PID DEVE essere visualizzato correttamente su tutti i dispositivi, garantendo un'esperienza coerente su schermi di dimensioni diverse;
- Il PID DEVE essere denominato come definito dal Fornitore PID;
- Il PID DEVE visualizzare il suo stato se diverso da valido per fornire trasparenza sul suo ciclo di vita e PUÒ visualizzarlo se valido. Dettagli specifici sullo stato del PID, se non valido, POSSONO essere forniti (ad esempio, il motivo per cui il PID è stato revocato);
- Il PID DEVE includere Pulsanti di Ingaggio per consentire la gestione del ciclo di vita e permettere all'Utente di revocare il PID, quindi l'intera Istanza Wallet con tutte le EAA emesse, o di aggiornare il PID in qualsiasi momento (vedere :ref:`functionalities:Gestione degli Attestati Elettronici`);
- Il PID DEVE essere un elemento interattivo, affinché l'Utente possa essere autenticato da un Relying Party in un contesto digitale (vedere :ref:`functionalities:Autenticazione`), per accedere ai servizi in contesti di prossimità e per richiedere l'emissione di ulteriori EAA (vedere :ref:`functionalities:Ottenimento degli Attestati Elettronici di Attributi`);
- Il PID DEVE visualizzare un metodo di assistenza da parte del Fornitore PID (vedere :ref:`functionalities:Assistenza Utente`);
- Il PID DEVE essere riconoscibile dall'Utente e distinguibile da altri EAA;
- Il PID DEVE essere denominato con la convenzione di denominazione che sarà definita nella versione futura di questo documento, evitando termini personalizzati o tecnici come "Person Identification Data" o il suo acronimo "PID";
- La rappresentazione del PID DEVE aderire a un insieme definito di specifiche fornite dal Fornitore PID per garantire riconoscibilità, coerenza e omogeneità tra diverse Soluzioni Wallet.

Il Fornitore PID DEVE:

- Implementare un nome/convenzione di denominazione per riferirsi al PID, per garantire coerenza tra tutte le Soluzioni Wallet;
- Definire un insieme chiaro di specifiche per il PID per garantire l'identificazione e la rappresentazione coerenti del PID tra diverse Soluzioni Wallet, in termini di format, struttura e standard di aspetto (ad esempio colore, immagine di sfondo, ecc.).

Ottenimento degli Attestati Elettronici di Attributi 
----------------------------------------------------

Ad attivazione conclusa, l'Utente PUÒ ottenere uno o più Attestati Elettronici di Attributi all'interno della sua Istanza IT-Wallet. 

A seconda delle specifiche esigenze dell'Utente, della tipologia di Attestato Elettronico di Attributi e delle disponibilità offerte dal Fornitore di Soluzione IT-Wallet, dal Fornitore di Attestati Elettronici di Attributi e dal Titolare di Fonte Autentica, l'ottenimento degli Attestati Elettronici di Attributi può avvenire attraverso due modalità: 

- **dal Catalogo dell'Istanza IT-Wallet**: l'Utente esplora l'elenco degli Attestati Elettronici di Attributi messi a disposizione dalla Soluzione IT-Wallet, seleziona quello di suo interesse e avvia la procedura di richiesta che si conclude con l'ottenimento dell'Attestato Elettronico di Attributi nell'Istanza IT-Wallet (vedi :ref:`registry-catalogue:Catalogo degli Attestati Elettronici`); 

- **da un Touchpoint del Titolare di Fonte Autentica** (o del Fornitore di Attestati Elettronici di Attributi qualora coincida con il Titolare di Fonte Autentica): l'Utente interagisce col servizio digitale del Titolare di Fonte Autentica che gli permette di ottenere nella sua Istanza IT-Wallet uno specifico Attestato Elettronico di Attributi tramite un Pulsante di Ingaggio (vedi :ref:`registry-catalogue:Catalogo degli Attestati Elettronici`).  

Nonostante le modalità di avvio della richiesta siano diverse, i flussi di ottenimento condividono una struttura e un processo simili. Di seguito, sono illustrati i requisiti dell'Esperienza Utente del flusso di ottenimento di un Attestato Elettronico di Attributi dal Catalogo che il Fornitore di Soluzione IT-Wallet DEVE garantire attraverso la propria Soluzione IT-Wallet: 

- l'Utente accede alla propria Istanza IT-Wallet utilizzando la modalità di sblocco precedentemente impostata; 
- l'Utente seleziona l'Attestato Elettronico di Attributi che intende aggiungere alla sua Istanza IT-Wallet scegliendo tra quelli disponibili nel Catalogo; 
- l'Utente prende visione dei dati del PID, qualora richiesti dal Titolare di Fonte Autentica per l'ottenimento dell'Attestato Elettronico di Attributi, il nome del relativo Fornitore di Attestati Elettronici di Attributi e di eventuali informative.  L'Utente dà il proprio consenso per poter proseguire presentando i dati del PID o altri Attributi al Fornitore di Attestati Elettronici di Attributi oppure annulla l'operazione; 
- l'Utente visualizza l'anteprima dell'Attestato Elettronico di Attributi. L'Utente conferma i dati mostrati in anteprima per procedere all'ottenimento oppure annulla l'operazione; 
- l'Utente autorizza l'operazione utilizzando la modalità di sblocco precedentemente impostata; 
- l'Utente visualizza l'esito positivo dell'ottenimento avvenuto; 
- l'Utente visualizza i dettagli dell'Attestato Elettronico di Attributi ottenuto ovvero: i dati in esso contenuti, il nome del Fornitore di Attestati Elettronici di Attributi che ha emesso l'Attestato Elettronico di Attributi e il nome del Titolare di Fonte Autentica; 
- l'Utente ha evidenza di tutti gli Attestati Elettronici ottenuti navigando la sua Istanza IT-Wallet. 

Il Fornitore di Soluzione IT-Wallet DEVE permettere all'Utente di rimuovere un Attestato Elettronico di Attributi dalla sua Istanza IT-Wallet in ogni momento. In caso di assenza del dispositivo su cui è stata attivata l'Istanza IT-Wallet, il Fornitore di Soluzione IT-Wallet DEVE permettere all'Utente di disattivare l'intera Istanza IT-Wallet tramite un Touchpoint dedicato. Inoltre, i Fornitori di Attestati Elettronici di Attributi DOVREBBERO permettere all'Utente la revoca degli Attestati Elettronici ottenuti, tramite specifici Touchpoint. Per approfondimenti si rimanda alle sezioni :ref:`functionalities:Disattivazione dell'Istanza IT-Wallet` e :ref:`functionalities:Gestione degli Attestati Elettronici`. 

In caso di problemi di comunicazione tra i sistemi del Fornitore di Attestati Elettronici di Attributi e del Titolare di Fonte Autentica o in presenza di processi amministrativi o tecnici che non consentono di fornire immediatamente l'Attestato Elettronico di Attributi, gli attori coinvolti POSSONO gestire il flusso di ottenimento in modalità differita. In questo caso, il Fornitore di Soluzione IT-Wallet DEVE garantire che: 

- l'Utente, giunto all'ultimo step del processo, visualizzi un messaggio che lo invita ad attendere il momento in cui l'Attestato Elettronico di Attributi potrà essere rilasciato; 
- l'Utente venga informato dal Fornitore di Attestati Elettronici di Attributi non appena l'Attestato Elettronico di Attributi è disponibile. 

In caso di dati errati all'interno di un Attestato Elettronico di Attributi già ottenuto o in fase di ottenimento, il Fornitore di Soluzione IT-Wallet DOVREBBE garantire all'Utente un'adeguata assistenza attraverso la propria Istanza IT-Wallet. Per approfondimenti si rimanda alla sezione :ref:`functionalities:Assistenza Utente`. 

In caso di errori nell'utilizzo della Istanza IT-Wallet, il Fornitore di Soluzione IT-Wallet DEVE garantire all'Utente la visualizzazione di messaggi coerenti che lo informino e guidino alla loro risoluzione. Per approfondimenti si rimanda alla sezione :ref:`functionalities:Gestione degli errori`. 

Qualora un Titolare di Fonte Autentica (o un Fornitore di Attestati Elettronici di Attributi qualora coincida con il Titolare di Fonte Autentica) intendesse implementare un Pulsante di Ingaggio per permettere l'avvio del processo di ottenimento da un proprio Touchpoint, questo DEVE garantire il rispetto dei requisiti relativi all'aspetto grafico e alle modalità di implementazione del Pulsante di Ingaggio, descritti nella sezione :ref:`brand-identity:Brand Identity del Sistema IT-Wallet`. 

Focus sulle Attestazioni Elettroniche di Attributi
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Le Attestazioni Elettroniche di Attributi (EAA) ottenute all'interno dell'Istanza Wallet DOVREBBERO essere visualizzate in un elenco all'interno di una Vista Anteprima. In questo caso, ogni EAA DEVE garantire un elevato livello di riconoscibilità e accessibilità [REF_ACCESSIBILITY] delle informazioni contenute. Di seguito sono riportati i requisiti per la visualizzazione dell'EAA a cui ogni Fornitore Wallet DEVE aderire per fornire un'esperienza di consultazione e utilizzo coerente e accessibile:

- L'EAA DEVE essere visualizzata correttamente su tutti i dispositivi, garantendo un'esperienza coerente su schermi di dimensioni diverse;
- Il nome dell'EAA DEVE essere chiaramente visibile e sempre visualizzato sia nella Vista Dettagliata che nella Vista Anteprima;
- L'EAA, sia nella Vista Anteprima che nella Vista Dettagliata, DEVE visualizzare il suo stato se diverso da valido per fornire trasparenza sul suo ciclo di vita e PUÒ visualizzarlo se valido. La Vista Anteprima PUÒ anche includere Attributi aggiuntivi per migliorare l'Esperienza Utente e la gestione; ad esempio, PUÒ visualizzare il nome o il logo del Fornitore di Attestazioni Elettroniche di Attributi o del Fornitore PID. La Vista Dettagliata PUÒ fornire dettagli specifici sullo stato se non valido (ad esempio, il motivo per cui l'EAA è revocata);
- L'EAA DEVE includere Pulsanti d'Azione nella Vista Dettagliata per consentire la gestione del ciclo di vita e permettere all'Utente di revocare o aggiornare un'EAA in qualsiasi momento (vedere :ref:`functionalities:Gestione degli Attestati Elettronici`);
- L'EAA DEVE essere un elemento interattivo, affinché l'Utente possa accedere ai servizi forniti dai Relying Party in contesti digitali e di prossimità (vedere :ref:`functionalities:Presentazione degli Attestati Elettronici`);
- L'EAA PUÒ essere visualizzata in formato tessera nella sua Vista Anteprima, in linea con gli approcci già utilizzati da altri portafogli digitali nel mercato, per rispecchiare l'aspetto di un documento fisico corrispondente. Quando applicabile, la natura digitale del documento PUÒ essere indicata, ad esempio etichettandolo come "versione digitale" nel layout;
- L'EAA DEVE visualizzare le stesse informazioni nella Vista Dettagliata come mostrato nella Vista Anteprima e PUÒ includere dettagli aggiuntivi;
- L'EAA DEVE visualizzare un metodo di assistenza (vedere :ref:`functionalities:Assistenza Utente`);
- Il layout dell'EAA nella Vista Anteprima DEVE essere ottimizzato per scalabilità e usabilità, specialmente quando più EAA vengono visualizzate sulla stessa schermata;
- La rappresentazione dell'EAA DEVE aderire a un insieme definito di specifiche fornite dal Fornitore di Attestazioni Elettroniche di Attributi per garantire riconoscibilità, coerenza e omogeneità tra diverse Soluzioni Wallet.

Il Fornitore di Attestazioni Elettroniche di Attributi:

- DEVE definire un nome/convenzione di denominazione per riferirsi agli EAA emessi, per garantire coerenza tra tutte le Soluzioni Wallet; il nome dell'EAA DEVE essere comprensibile e user-friendly evitando termini tecnici o acronimi quando possibile;
- DEVE definire un insieme chiaro di specifiche per l'EAA per garantire un'identificazione e rappresentazione coerente dell'EAA tra diverse Soluzioni Wallet, in termini di formato, struttura e standard di aspetto (ad es. colore, immagine di sfondo, ecc.).

Presentazione degli Attestati Elettronici 
-----------------------------------------
  
Il processo di presentazione permette all'Utente di accedere a un servizio o di dimostrare la titolarità di un dato o la sua idoneità a effettuare una determinata azione. La presentazione degli Attestati Elettronici e la loro conseguente verifica, prevede l'interazione tra due soggetti, l'Utente e il Verificatore di Attestati Elettronici, e può avvenire in due modalità principali a seconda delle circostanze e del contesto di interazione: 

- **Presentazione in prossimità**: l'Utente presenta il PID e/o un set di Attributi contenuti in uno o più Attestati Elettronici tramite l'Istanza IT-Wallet direttamente a un Verifier o a un dispositivo del Verificatore di Attestati Elettronici preposto alla verifica in presenza; 

- **Presentazione da remoto**: l'Utente presenta il PID e/o un set di Attributi contenuti in uno o più Attestati Elettronici tramite l'Istanza IT-Wallet ad un Verificatore di Attestati Elettronici predisposto per la verifica online al fine, ad esempio, di Autenticarsi e fruire dei servizi erogati. 

Presentazione in prossimità 
^^^^^^^^^^^^^^^^^^^^^^^^^^^

La presentazione in prossimità consente all'Utente di esibire il PID e/o un set di Attributi contenuti in uno o più Attestati Elettronici tramite la propria Istanza IT-Wallet, secondo due diverse modalità: 

- **Modalità supervisionata**: l'Utente, tramite l'Istanza IT-Wallet, presenta il PID e/o uno o più Attestati Elettronici di Attributi, a un Verificatore di Attestati Elettronici dotato di un'apposita app o sistema di verifica (e.g. agente delle forze dell'ordine, farmacista, etc.); 

- **Modalità non supervisionata**: l'Utente, tramite l'Istanza IT-Wallet, presenta il PID e/o un set di Attributi contenuti in uno o più Attestati Elettronici a un dispositivo preposto (e.g. tornello, ATM, etc.). 

Di seguito i requisiti dell'Esperienza Utente relativi a entrambe le modalità che il Fornitore di Soluzione IT-Wallet DEVE garantire attraverso la propria Soluzione IT-Wallet. 

**Modalità supervisionata** 

- L'Utente accede alla propria Istanza IT-Wallet utilizzando la modalità di sblocco precedentemente impostata; 
- L'Utente accede alla funzionalità dedicata alla generazione del QR Code; 
- L'Utente mostra il QR Code generato al soggetto che opera per conto del Verificatore di Attestati Elettronici, il quale provvede a scansionarlo tramite apposita app o sistema di verifica; 
- L'Utente prende visione dei dati del PID e/o degli Attributi richiesti per la presentazione, del nome del Verificatore di Attestati Elettronici che li richiede e delle relative eventuali informative. L'Utente sceglie se presentare o meno eventuali dati del PID o Attributi non obbligatori ai fini della presentazione (Divulgazione Selettiva). L'Utente dà il proprio consenso per poter proseguire oppure annulla l'operazione; 
- L'Utente autorizza l'operazione utilizzando la modalità di sblocco precedentemente impostata; 
- L'Utente visualizza l'esito positivo della presentazione avvenuta. 

In caso di errori nell'utilizzo dell'Istanza IT-Wallet, il Fornitore di Soluzione IT-Wallet DEVE garantire all'Utente la visualizzazione di messaggi coerenti che lo informino e guidino alla loro risoluzione. Per approfondimenti si rimanda alla sezione :ref:`functionalities:Gestione degli errori`. 

**Modalità non supervisionata** 

- L'Utente accede alla propria Istanza IT-Wallet utilizzando la modalità di sblocco precedentemente impostata; 
- L'Utente accede alla funzionalità dedicata alla generazione del QR Code; 
- L'Utente mostra il QR Code generato al dispositivo preposto (ad esempio un tornello) del Verificatore di Attestati Elettronici per permetterne la scansione;  
- L'Utente prende visione dei dati del PID e/o gli Attributi richiesti per la presentazione, del nome del Verificatore di Attestati Elettronici che li richiede e delle relative eventuali informative. L'Utente sceglie se presentare o meno eventuali dati del PID o degli Attributi non obbligatori ai fini della presentazione (Divulgazione Selettiva). L'Utente dà il proprio consenso per poter proseguire oppure annulla l'operazione; 
- L'Utente autorizza l'operazione utilizzando la modalità di sblocco precedentemente impostata; 
- L'Utente visualizza l'esito positivo della presentazione avvenuta. 

In caso di errori nell'utilizzo dell'Istanza IT-Wallet, il Fornitore di Soluzione IT-Wallet DEVE garantire all'Utente la visualizzazione di messaggi coerenti che lo informino e guidino alla loro risoluzione. Per approfondimenti si rimanda alla sezione :ref:`functionalities:Gestione degli errori`. 

Presentazione da remoto 
^^^^^^^^^^^^^^^^^^^^^^^

La presentazione da remoto consente all'Utente di esibire il PID e/o un set di Attributi contenuti in uno o più Attestati Elettronici, facendo interagire la propria Istanza IT-Wallet con il Touchpoint di un Verificatore di Attestati Elettronici, tramite un apposito Pulsante di Ingaggio.  

Tale presentazione può avvenire in due diverse modalità, sulla base del tipo di dispositivo utilizzato per accedere al servizio di interesse: 

- **Same-device**: nel caso in cui l'Utente voglia accedere a un servizio digitale online utilizzando lo stesso dispositivo su cui ha installato l'Istanza IT-Wallet; 
- **Cross-device**: nel caso in cui l'Utente voglia accedere a un servizio digitale utilizzando un dispositivo differente rispetto a quello in cui ha installato l'Istanza IT-Wallet. 

Di seguito i requisiti dell'Esperienza Utente relativi a entrambe le modalità che il Fornitore di Soluzione IT-Wallet DEVE garantire attraverso la propria Soluzione IT-Wallet. 

**Same-device** 

- L'Utente clicca sul Pulsante di Ingaggio reso disponibile nel Touchpoint del Verificatore di attestati elettronici; 
- L'Utente accede alla propria Istanza IT-Wallet utilizzando la modalità di sblocco precedentemente impostata; 
- L'Utente prende visione dei dati del PID e/o gli Attributi richiesti per la presentazione, del nome del Verificatore di Attestati Elettronici che li richiede e delle relative eventuali informative. L'Utente sceglie se presentare o meno eventuali dati del PID e/o Attributi non obbligatori ai fini della presentazione (Divulgazione Selettiva). L'Utente dà il proprio consenso per poter proseguire oppure annulla l'operazione; 
- L'Utente autorizza l'operazione utilizzando la modalità di sblocco precedentemente impostata; 
- L'Utente visualizza nell'Istanza IT-Wallet l'esito positivo della presentazione avvenuta; 
- L'Utente torna al flusso nel Touchpoint del Verificatore di Attestati Elettronici su cui DEVE visualizzare l'esito della presentazione completata. 

In caso di errori nell'utilizzo dell'Istanza IT-Wallet, il Fornitore di Soluzione IT-Wallet DEVE garantire all'Utente la visualizzazione di messaggi coerenti che lo informino e guidino alla loro risoluzione. Per approfondimenti si rimanda alla sezione :ref:`functionalities:Gestione degli errori`. 

**Cross-device** 

- L'Utente clicca il Pulsante di Ingaggio reso disponibile nel Touchpoint del Verificatore di Attestati Elettronici che l'Utente sta navigando da un dispositivo diverso da quello su cui è installata l'Istanza IT-Wallet; 
- L'Utente accede all'Istanza IT-Wallet che desidera utilizzare dal dispositivo su cui è installata utilizzando la modalità di sblocco precedentemente impostata; 
- L'Utente inquadra il QR Code reso disponibile dal Verificatore di Attestati Elettronici, utilizzando la sua Istanza IT-Wallet; 
- L'Utente prende visione dei dati del PID e/o degli Attributi richiesti per la presentazione, del nome del Verificatore di Attestati Elettronici che li richiede e delle relative eventuali informative. L'Utente sceglie se presentare o meno eventuali dati del PID e/o Attributi non obbligatori ai fini della presentazione (Divulgazione Selettiva). L'Utente dà il proprio consenso per poter proseguire oppure annulla l'operazione; 
- L'Utente autorizza l'operazione utilizzando la modalità di sblocco precedentemente impostata; 
- L'Utente visualizza nell'Istanza IT-Wallet l'esito positivo della presentazione avvenuta; 
- L'Utente torna sul Touchpoint del Verificatore di Attestati Elettronici e visualizza l'esito della presentazione completata. 

In caso di errori nell'utilizzo dell'Istanza IT-Wallet, il Fornitore di Soluzione IT-Wallet DEVE garantire all'Utente la visualizzazione di messaggi coerenti che lo informino e guidino alla loro risoluzione. Per approfondimenti si rimanda alla sezione :ref:`functionalities:Gestione degli errori`. 

Autenticazione 
""""""""""""""

L'Autenticazione è un caso d'uso specifico della presentazione remota e consente all'Utente di accedere in modo sicuro ai servizi resi disponibili da Verificatori di Attestati Elettronici pubblici e privati, presentando il PID ed eventualmente un set di Attributi contenuti negli Attestati Elettronici di Attributi ottenuti. Questo garantisce all'Utente il pieno controllo sui propri dati e la possibilità di condividere anche i soli dati strettamente necessari alla verifica da parte del Verificatore di Attestati Elettronici. 

Il processo di Autenticazione può avvenire in entrambe le modalità same-device e cross-device descritte sopra. Per quanto riguarda i requisiti funzionali a supporto dell'Esperienza Utente, si DEVONO rispettare gli stessi requisiti previsti per la presentazione in remoto nelle due modalità (same-device e cross-device).

Infatti, a livello di Esperienza Utente, il processo di Autenticazione si distingue da un generico flusso di presentazione principalmente per le modalità di avvio del processo, in questo caso reso possibile a partire da uno specifico pulsante, il Pulsante di Autenticazione. 

Al fine di garantire un processo di Autenticazione adeguato e coerente tra tutti i Verificatori di Attestati Elettronici, ciascun Verificatore di Attestati Elettronici DEVE rispettare i requisiti relativi all'aspetto grafico e all'Esperienza Utente descritti di seguito, unitamente al rispetto di [RIF_ACCESSIBILITÀ] e, nel caso di enti pubblici, delle [LG_DESIGN].

I Verificatori di Attestati Elettronici DOVREBBERO utilizzare le Risorse Ufficiali open source. Qualora non intendano utilizzare tali risorse open source, i Verificatori di Attestati Elettronici POSSONO sviluppare in autonomia le Soluzioni Tecniche abilitanti il flusso di Autenticazione.
 
I Verificatori di Attestati Elettronici, in ogni caso, DEVONO abilitare il processo di Autenticazione rendendo disponibili le seguenti pagine: 

- **Discovery Page**: ha l'obiettivo di mostrare all'Utente tutti i metodi di Autenticazione disponibili; 
- **QR code page** (*solo per modalità cross-device*): ha lo scopo di invitare l'Utente a inquadrare il codice QR;  
- **waiting page** (*solo per modalità cross-device*): ha lo scopo di invitare l'Utente a continuare il processo di Autenticazione sulla propria Istanza IT-Wallet; 
- **thank you page**: ha lo scopo di comunicare all'Utente l'avvenuta Autenticazione; 
- **error page**: ha lo scopo di comunicare all'Utente eventuali errori legati al flusso di Autenticazione. 

Tali pagine DEVONO prevedere i seguenti elementi trasversali ricorrenti, in continuità con l'Identità Visiva del Touchpoint del Verificatore di Attestati Elettronici:

- un **header e/o un subheader**, che permette all'Utente di tornare alla pagina precedente; 
- un **footer** che include l'informativa privacy, le note legali e la Dichiarazione di Accessibilità, ove previsto da normativa. 

Di seguito invece gli elementi specifici caratteristici delle diverse pagine. 

**Discovery Page** 

Per garantire l'Autenticazione tramite il Sistema IT-Wallet, il Verificatore di Attestati Elettronici PUÒ aggiornare la propria Discovery Page con quella resa disponibile nelle Risorse Ufficiali. 

In alternativa, il Verificatore di Attestati Elettronici PUÒ mantenere la propria Discovery Page, ma DEVE in ogni caso integrare il Pulsante di Autenticazione, come da indicazioni presenti nella sezione :ref:`brand-identity:Pulsante di Autenticazione`.

In ogni caso, nella pagina, il Verificatore di Attestati Elettronici:

- DEVE garantire la presenza di tutte le modalità di Autenticazione attraverso l'identità digitale tra cui la modalità di Autenticazione del Sistema IT-Wallet, quindi tramite il Pulsante di Autenticazione; 
- PUÒ presentare anche modalità di Autenticazione alternative, se disponibili; 
- DOVREBBE garantire informazioni minime a supporto, per permettere all'Utente di compiere una scelta consapevole e informata. 

Nel caso l'Utente stia navigando la pagina del Verificatore di Attestati Elettronici da un Touchpoint diverso da quello su cui ha attivato l'Istanza IT-Wallet (modalità cross-device), la scelta di Autenticazione tramite il Sistema IT-Wallet DEVE condurre l'Utente alla QR code page. 

Nel caso in cui invece l'Utente stia navigando la pagina del Verificatore di Attestati Elettronici dallo stesso Touchpoint su cui ha attivato l'Istanza IT-Wallet (modalità same-device) tale pagina DEVE condurre l'Utente all'apertura della propria Istanza IT-Wallet. 

**QR code page (*solo per modalità cross-device*)** 

La QR code page è la pagina su cui atterra l'Utente che ha scelto l'Autenticazione tramite il Sistema IT-Wallet in un flusso cross-device, e ha lo scopo di invitare l'Utente a scannerizzare, con la propria Istanza IT-Wallet, il codice QR generato. 

Il Verificatore di Attestati Elettronici DOVREBBE implementare la QR code page (flusso cross-device) resa disponibile nelle Risorse Ufficiali. Il Verificatore di Attestati Elettronici che implementa la pagina:

- DEVE includere gli elementi propri dell'Identità Visiva del Sistema IT-Wallet, tra cui il Logo; 
- DEVE esporre il codice QR e un testo sintetico e chiaro che inviti l'Utente a scannerizzarlo con la propria Istanza IT-Wallet; 
- DEVE includere un testo sintetico e chiaro che permetta all'Utente di conoscere la validità temporale del codice QR;  
- DEVE includere una Call to Action che, in caso di timeout, permetta all'Utente di generare un nuovo codice QR; 
- DEVE includere una Call to Action che permetta all'Utente di annullare l'operazione e tornare alla Discovery Page. 

Inoltre, nei rispetto di [RIF_ACCESSIBILITÁ], relativamente al codice QR, il Verificatore di Attestati Elettronici: 

- DEVE rispettare le dimensioni minime raccomandate per garantire una scansione efficace. Una misura di 150x150 pixel è generalmente adeguata, ma per codici con alta densità di dati (e.g. URL lunghi o numerosi caratteri), è consigliabile aumentarla a 300x300 pixel o più; 
- DEVE garantire un contrasto minimo tra il codice QR e lo sfondo (la condizione ideale prevede uno sfondo bianco con un codice QR nero); 
- DEVE evitare inversioni di colore tra sfondo e codice QR; 
- DEVE limitare la presenza a un solo codice QR per pagina; 
- DEVE garantire nitidezza e alta qualità; 
- DEVE garantire il formato SVG; 
- DEVE garantire che non venga parzialmente nascosto da testo o altri elementi.

**Waiting page (*solo per modalità cross-device*)** 

La waiting page è la pagina che invita l'Utente a proseguire il processo di Autenticazione sulla propria Istanza IT-Wallet, a valle della scansione del codice QR. 

Il Verificatore di Attestati Elettronici DOVREBBE implementare la waiting page (cross-device) resa disponibile nelle Risorse Ufficiali. Il Verificatore di Attestati Elettronici che implementa la pagina: 

- DEVE includere gli elementi propri dell'Identità Visiva del Sistema IT-Wallet, tra cui il Logo e un'icona o altro elemento grafico che aiuti a veicolare il messaggio della pagina; 
- DEVE prevedere un testo sintetico e chiaro che lo inviti a proseguire sulla sua Istanza IT-Wallet. 

**Thank you page** 

La thank you page è la pagina sui cui l'Utente atterra una volta concluso il processo di Autenticazione attraverso la propria Istanza IT-Wallet e ha l'obiettivo di invitare l'Utente a proseguire nell'area riservata.  

Il Verificatore di Attestati Elettronici DOVREBBE implementare la thank you page resa disponibile nelle Risorse Ufficiali. Il Verificatore di Attestati Elettronici che implementa la pagina: 

- DEVE includere gli elementi propri dell'Identità Visiva del Sistema IT-Wallet, tra cui il Logo e un'icona o altro elemento grafico che aiuti a veicolare il messaggio della pagina; 
- DEVE prevedere un testo sintetico e chiaro che spieghi all'Utente che il processo di Autenticazione si è concluso con successo; 
- DEVE prevedere una Call to Action che inviti l'Utente a proseguire nell'area riservata del Verificatore di Attestati Elettronici. 

**Error page** 

La pagina di errore rappresenta quella tipologia di pagina su cui l'Utente atterra in caso di errori nel corso del flusso di Autenticazione, e ha lo scopo di comunicare all'Utente la natura di tali errori (es. errore tecnico, assenza di rete, malfunzionamento dell'Istanza IT-Wallet, consenso alla presentazione dei dati negato etc.) e di presentare le azioni che l'Utente può intraprendere. Per approfondimenti sulle casistiche di errore si rimanda alla sezione :ref:`functionalities:Gestione degli errori`. 
 
Il Verificatore di Attestati Elettronici DOVREBBE implementare la error page resa disponibile nelle Risorse Ufficiali. Il Verificatore di Attestati Elettronici che implementa la pagina: 

- DEVE includere gli elementi propri dell'Identità Visiva del Sistema IT-Wallet, tra cui il Logo e un'icona o altro elemento grafico che aiuti a veicolare la natura dell'errore; 
- DEVE prevedere un testo sintetico e chiaro che spieghi all'Utente la natura dell'errore, il codice errore e una sua spiegazione semplice; 
- DEVE prevedere una o più Call to Action che invitino l'Utente a intraprendere le azioni previste (es. riprova, contatta l'assistenza, etc.). 

Gestione degli Attestati Elettronici
------------------------------------

Il Fornitore di Soluzione IT-Wallet, attraverso la propria Soluzione IT-Wallet, e il Fornitore di Dati di Identificazione Personale o il Fornitore di Attestati Elettronici di Attributi, attraverso Touchpoint dedicati, DEVONO dare all'Utente la possibilità di gestire in ogni momento i propri Attestati Elettronici.  

In questa sezione sono illustrate tre diverse categorie di requisiti per la gestione del ciclo di vita di ogni Attestato Elettronico e nello specifico per la gestione: 

- **del suo stato**: per consentire all'Utente di appurare la condizione di validità o invalidità di un Attestato Elettronico; 
- **dei suoi utilizzi**: per consentire all'Utente di visualizzare e gestire lo storico delle transazioni effettuate utilizzando un Attestato Elettronico; 
- **dei suoi dati**: per consentire all'Utente di archiviare e ripristinare ogni Attestato Elettronico di Attributi in linea col principio di *data portability*. 

Di seguito i principali aspetti che impattano e determinano l'Esperienza Utente nell'ambito della gestione degli Attestati Elettronici per mezzo di un'Istanza IT-Wallet e i requisiti funzionali riferiti a ciascuna categoria. 

Stato degli Attestati Elettronici 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Per garantire l'affidabilità e promuovere il corretto utilizzo della propria Soluzione IT-Wallet, il Fornitore di Soluzione IT-Wallet DEVE dare all'Utente visibilità dello stato degli Attestati Elettronici ottenuti nella propria Istanza IT-Wallet sulla base delle informazioni ricevute dal Fornitore di Attestati Elettronici, gestore del loro ciclo di vita.  

Ogni Attestato Elettronico può assumere lo stato valido o non valido, con conseguenti impatti circa le sue possibilità di utilizzo, in particolare: 

- **valido**: gli Attestati Elettronici validi DEVONO essere utilizzabili quindi presentabili. Tra questi rientrano anche gli Attestati Elettronici in scadenza. Qualora un Attestato Elettronico fosse in scadenza, l'Istanza IT-Wallet DOVREBBE informare l'Utente con un adeguato preavviso utile ad avviare per tempo una richiesta di ri-ottenimento o, se necessario, di revoca; 

- **non valido**: gli Attestati Elettronici non validi NON DEVONO essere utilizzabili quindi presentabili. Rientrano in questa categoria gli Attestati Elettronici scaduti o revocati. In questi casi l'Istanza IT-Wallet DEVE essere informare l'Utente circa lo stato di non validità e DOVREBBE dare evidenza della motivazione. Qualora l'Attestato Elettronico non fosse più valido, e non fosse quindi più possibile alcuno scenario di utilizzo, l'Istanza IT-Wallet PUÒ prevedere dei meccanismi per inibire la Vista di Dettaglio di tale Attestato Elettronico, al fine di incoraggiare l'Utente ad aggiornarlo o cancellarlo tramite apposito testo informativo e Call To Action. 

Revoca degli Attestati Elettronici 
""""""""""""""""""""""""""""""""""

La revoca si configura come quel meccanismo che determina il passaggio di un Attestato Elettronico da uno stato valido a uno stato non valido. La revoca può avvenire in modalità attiva o passiva: 

- **Revoca attiva**: ovvero la revoca di un Attestato Elettronico su richiesta dell'Utente. Tale processo comporta la sola revoca dell'Attestato Elettronico e non del corrispettivo documento fisico, se esistente. Di seguito un elenco esemplificativo di scenari in cui il Fornitore di Soluzione IT-Wallet DEVE dare possibilità all'Utente di richiedere la revoca di un Attestato Elettronico:  

   - l'Utente decide di non voler più possedere uno specifico Attestato Elettronico;
   - l'Utente decide di disattivare la propria Istanza IT-Wallet e, di conseguenza, tutti gli Attestati Elettronici precedentemente ottenuti; 
   - l'Utente non è più in possesso del dispositivo su cui è installata la propria Istanza IT-Wallet a causa di uno smarrimento o un furto. 

- **Revoca passiva**: ovvero la revoca di un Attestato Elettronico gestita dal relativo Fornitore di Attestati Elettronici per conto del Titolare di Fonte Autentica. In questo caso l'Istanza IT-Wallet DEVE informare l'Utente del cambiamento di stato dell'Attestato Elettronico e, in aggiunta, il Fornitore di Attestati Elettronici PUÒ informare l'Utente attraverso altri Touchpoint. Di seguito un elenco esemplificativo di scenari che porterebbero alla revoca di un Attestato Elettronico: 

   - il documento fisico corrispondente all'Attestato Elettronico è stato dichiarato smarrito o danneggiato da parte dell'Utente tramite apposito canale/ Touchpoint; 
   - il documento fisico corrispondente all'Attestato Elettronico è stato revocato dalle autorità competenti; 
   - non sussistono più i requisiti minimi di sicurezza e/o affidabilità di una o più delle parti coinvolte; 
   - il dispositivo dell'Utente non soddisfa più i requisiti minimi di sicurezza (dispositivo rootato o jailbroken). 
 
Storico degli Attestati Elettronici 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Al fine di garantire i principi di visibilità e trasparenza, il Fornitore di Soluzione IT-Wallet DEVE permettere all'Utente di visualizzare lo storico di tutte le transazioni effettuate, ovvero l'utilizzo degli Attestati Elettronici di Attributi tramite l'Istanza IT-Wallet. In particolare: 

- l'Istanza IT-Wallet DEVE mostrare all'Utente con quali Verificatori di Attestati Elettronici ha interagito e quali Attestati Elettronici sono stati oggetto di presentazione e verifica; 
- l'Istanza IT-Wallet DEVE permettere all'Utente di richiedere facilmente al Verificatore di Attestati Elettronici la cancellazione delle proprie informazioni oggetto delle precedenti presentazioni. 

Archiviazione e ripristino degli Attestati Elettronici di Attributi 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Con l'obiettivo di garantire il principio di data portability, la Soluzione IT-Wallet DEVE garantire all'Utente l'accesso a specifiche funzionalità per: 

- richiedere l'archiviazione, quindi il salvataggio, degli Attestati Elettronici di Attributi ottenuti su una specifica Istanza IT-Wallet; 
- richiedere il ripristino dei propri Attestati Elettronici di Attributi su un'altra Istanza IT-Wallet. 

Disattivazione dell'Istanza IT-Wallet 
-------------------------------------

La disattivazione dell'Istanza IT-Wallet è la funzionalità che rende l'Istanza IT-Wallet disattiva e quindi non più operativa. La disattivazione dell'Istanza IT-Wallet può essere scatenata da attori differenti a seconda delle circostanze, in particolare: 

- da parte dell'Utente nel caso in cui, ad esempio: 

   - il dispositivo sia stato smarrito o rubato; 
   - il dispositivo risulti compromesso; 
   - il dispositivo sia stato resettato alle impostazioni di fabbrica. 

- da parte di un ente terzo titolato nel caso in cui, ad esempio: 

   - la Soluzione IT-Wallet non rispetti più i requisiti minimi di sicurezza. 
 
Il Fornitore di Soluzione IT-Wallet DEVE, quindi, garantire all'Utente la possibilità di disattivare volontariamente la propria Istanza IT-Wallet tramite: 

- l'Istanza IT-Wallet stessa; 
- un Touchpoint (e.g. un sito web) fornito dal Fornitore di Soluzione IT-Wallet; 
- l'app store del proprio dispositivo, disinstallando l'Istanza IT-Wallet. 

Di seguito i requisiti funzionali a supporto dell'Esperienza Utente relativi alla disattivazione dell'Istanza IT-Wallet che il Fornitore di Soluzione IT-Wallet DEVE garantire attraverso la propria Soluzione IT-Wallet: 

- l'Utente accede alla propria Istanza IT-Wallet utilizzando la modalità di sblocco precedentemente impostata oppure si Autentica presso il Touchpoint reso disponibile dal Fornitore di Soluzione IT-Wallet; 
- l'Utente seleziona la funzionalità di disattivazione dell'Istanza IT-Wallet; 
- l'Utente viene informato che la disattivazione dell'Istanza IT-Wallet renderà non più utilizzabili gli Attestati Elettronici precedentemente ottenuti; 
- l'Utente conferma l'azione per procedere con la disattivazione oppure annulla l'operazione; 
- l'Utente visualizza l'esito positivo della disattivazione avvenuta; 
- l'Utente, in caso di nuovo accesso, prende visione del fatto che l'Istanza IT-Wallet è disattiva; 
- l'Utente ha la possibilità di riattivare l'Istanza IT-Wallet riscaricando l'app dall'app store, in caso di cancellazione, e/o ripercorrendo il processo di attivazione. Per approfondimenti si rimanda alla sezione :ref:`functionalities:Attivazione dell'Istanza IT-Wallet`. 

Una volta riattivata l'Istanza IT-Wallet, gli Attestati Elettronici di Attributi potranno essere ri-ottenuti avviando nuovamente il processo di ottenimento o di ripristino. Per approfondimenti si rimanda rispettivamente alle sezioni :ref:`functionalities:Ottenimento degli Attestati Elettronici di Attributi` e :ref:`functionalities:Archiviazione e ripristino degli Attestati Elettronici di Attributi`. 

In caso di errori nell'utilizzo dell'Istanza IT-Wallet, il Fornitore di Soluzione IT-Wallet DEVE garantire all'Utente la visualizzazione di messaggi coerenti che lo informino e guidino alla loro risoluzione. Per approfondimenti si rimanda alla sezione :ref:`functionalities:Gestione degli errori`. 

Gestione degli errori 
---------------------

Il Sistema IT-Wallet prevede l'interazione di una molteplicità di servizi erogati da diversi attori. È quindi importante che venga definito un modello di gestione degli errori efficace, con l'obiettivo di migliorare la percezione e il senso di affidabilità dell'interno ecosistema e permettere all'Utente di sentirsi guidato nell'interazione con le diverse Soluzioni Tecniche e nella gestione consapevole di eventuali criticità durante la fruizione del servizio. 

Una comunicazione efficace in caso di errore determina un vantaggio anche per gli attori coinvolti, in quanto concorre alla riduzione delle richieste di assistenza e, quindi, alla minimizzazione dell'impatto sui sistemi.  

Di seguito vengono presentati i requisiti e le principali buone pratiche di gestione dell'errore, riferite alle modalità di interazione tra l'Utente e la propria Istanza IT-Wallet. Ciascun Attore Primario deve implementare una corretta gestione degli errori, in conformità alle attuali regole tecniche, al fine di comunicarli, direttamente o indirettamente, all'Utente e tramite l'Istanza IT-Wallet. Gli errori possono essere declinati, sulla base della loro natura, come segue: 

- **la fase dell'Esperienza Utente** in cui l'errore può verificarsi: attivazione o disattivazione dell'Istanza IT-Wallet, ottenimento, presentazione o gestione degli Attestati Elettronici; 
- **la tipologia di errore**: di sistema, di comunicazione tra attori, etc.; 
- **l'attore responsabile dell'errore**: Fornitore di Soluzione IT-Wallet, Fornitore di Dati di Identificazione Personale, Fornitore di Attestati Elettronici di Attributi, Titolare di Fonte Autentica; 
- **la modalità di restituzione dell'errore**: messaggio in pagina, banner, toast message, etc.;   
- **le azioni suggerite all'Utente per risolvere l'errore**: suggerimento di attesa, richiesta di effettuare un nuovo tentativo, rimando alle domande frequenti e/o al servizio di assistenza, etc.; 
- **le modalità di presa in carico dell'errore**: apertura di una richiesta di assistenza tramite l'Istanza IT-Wallet, rimando ad altri canali di approfondimento, etc. Per approfondimenti si rimanda alla sezione Assistenza Utente. 

Di seguito, una lista non esaustiva delle principali casistiche di errore, con riferimento all'attore responsabile della loro gestione, per ciascuna fase dell'Esperienza Utente.  

Errori di Attivazione dell'Istanza IT-Wallet 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 
.. list-table::
   :widths: 80 20
   :header-rows: 1

   * - Tipologia di errore
     - Attore responsabile 
   * - Il dispositivo non supporta la Soluzione IT-Wallet (e.g. assenza dei requisiti minimi di sicurezza o tecnologici)
     - Fornitore di Soluzione IT-Wallet 
   * - I servizi del Fornitore di Soluzione IT-Wallet non rispondono (e.g. errori tecnici o assenza connessione) 
     - Fornitore di Soluzione IT-Wallet 
   * - I servizi del Fornitore di Dati di Identificazione Personale non rispondono (e.g. errori tecnici) 
     - Fornitore di Dati di Identificazione Personale
   * - Il processo di Autenticazione sul servizio del National Identity Provider non è andato a buon fine (e.g. errori tecnici, identità non riconosciuta, etc.)
     - National Identity Provider 

Errori di ottenimento degli Attestati Elettronici di Attributi
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 80 20
   :header-rows: 1

   * - Tipologia di errore
     - Attore responsabile 
   * - L'Istanza IT-Wallet e/o il PID non risultano attivi 
     - Fornitore di Soluzione IT-Wallet
   * - Il servizio di ottenimento di un Attestato Elettronico di Attributi non è disponibile (e.g. errori tecnici) 
     - Fornitore di Attestati Elettronici di Attributi, Titolare di Fonte Autentica
   * - L'Utente non riesce ad ottenere nella propria Istanza IT-Wallet un certo Attestato Elettronico di Attributi (e.g. assenza di titolarità, versione fisica non valida o scaduta, etc.) 
     - Titolare di Fonte Autentica  

Errori di presentazione degli Attestati Elettronici
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 80 20
   :header-rows: 1

   * - Tipologia di errore
     - Attore responsabile 
   * - L'Utente non possiede all'interno della propria Istanza IT-Wallet gli Attributi contenuti in uno o più Attestati Elettronici richiesti per la fruizione di un determinato servizio 
     - Fornitore di Soluzione IT-Wallet 
   * - I servizi del Fornitore di Soluzione IT-Wallet e/o del Verificatore di Attestati Elettronici non rispondono (e.g. errori tecnici o assenza connessione) 
     - Fornitore di Soluzione IT-Wallet, Verificatore di Attestati Elettronici 

Errori di gestione degli Attestati Elettronici
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 80 20
   :header-rows: 1

   * - Tipologia di errore
     - Attore responsabile
   * - Il servizio di revoca / archiviazione/ ripristino di un Attestato Elettronico di Attributi non è disponibile (e.g. errori tecnici) 
     - Fornitore di Attestati Elettronici di Attributi 
   * - Il servizio di revoca del PID non è disponibile (e.g. errori tecnici) 
     - Fornitore di Dati di Identificazione Personale 

Errori di disattivazione dell'Istanza IT-Wallet
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 80 20
   :header-rows: 1

   * - Tipologia di errore
     - Attore responsabile
   * - Il servizio di disattivazione dell'Istanza IT-Wallet non è disponibile (e.g. errori tecnici) 
     - Fornitore di Soluzione IT-Wallet 

Oltre alla gestione degli errori, DEVE essere garantita da parte di tutti gli Attori Primari anche la gestione di esiti negativi dovuti alla volontà dell'Utente di abbandonare o annullare un flusso (es. attivazione, ottenimento, presentazione, etc.). In questi casi DEVE essere previsto un feedback che dia conferma all'Utente della scelta intrapresa e che PUÒ includere una Call to Action per proseguire.

Assistenza Utente 
-----------------

Per un'efficace gestione degli errori e di eventuali altre problematiche, gli Attori Primari DEVONO garantire un'adeguata assistenza all'Utente, strutturando un modello di assistenza semplice ed efficace basato sui seguenti principi: 

- **Risoluzione autonoma**: permettere all'Utente di consultare domande frequenti (FAQ) sui contenuti e sulle funzionalità dell'Istanza IT-Wallet, al fine di risolvere eventuali casistiche di errore o problematiche in maniera autonoma. 

- **Apertura guidata di una segnalazione**: guidare l'Utente all'eventuale apertura di una segnalazione, in modo da circoscrivere la problematica e facilitare la sua gestione. 

- **Collaborazione tra attori**: rendere possibile un adeguato coordinamento tra tutti gli attori coinvolti (Fornitore di Soluzione IT-Wallet, Fornitore di Attestati Elettronici di Attributi, Fornitore di Dati di Identificazione Personale e Titolare di Fonte Autentica) in base al proprio ruolo e alle modalità operative specifiche. 

- **Comunicazione efficiente**: garantire all'Utente la possibilità di monitorare lo stato aggiornato della propria richiesta durante tutte le fasi di lavorazione, attraverso una comunicazione chiara, continua e coordinata.  

Per applicare queste buone pratiche, gli attori coinvolti DOVREBBERO implementare i seguenti livelli di assistenza gerarchici: 

	1. **I Livello – Gestione autonoma**: il Fornitore di Soluzione IT-Wallet DOVREBBE permettere all'Utente di disporre di una sezione di domande frequenti (FAQ) all'interno della propria Istanza IT-Wallet per chiarire dubbi e risolvere in autonomia alcune problematiche. Ogni attore DOVREBBE formulare delle domande frequenti e relative risposte specifiche rispetto a dati e funzionalità messe a disposizione al Fornitore di Soluzione IT-Wallet o nei propri Touchpoint. Per alcune casistiche di errore, il Fornitore di Soluzione IT-Wallet DOVREBBE rendere direttamente disponibile il canale di assistenza di un altro attore, per facilitare una gestione tempestiva ed evitare l'apertura di una richiesta di assistenza nell'Istanza IT-Wallet. 

	2. **II Livello – Richiesta di assistenza al Fornitore di Soluzione IT-Wallet**: se il I livello non fosse sufficiente, il Fornitore di Soluzione IT-Wallet DOVREBBE permettere all'Utente di aprire una o più richieste di assistenza, effettuare una diagnosi e procedere alla risoluzione della problematica, se di sua competenza. Tali richieste DOVREBBERO essere gestite tramite l'Istanza IT-Wallet o altri Touchpoint del Fornitore di Soluzione IT-Wallet.

	3. **III Livello – Inoltro della richiesta all'attore responsabile della problematica**: se il II livello non fosse sufficiente, il Fornitore di Soluzione IT-Wallet DOVREBBE garantire che la richiesta sia inoltrata all'attore responsabile (Fornitore di Attestati Elettronici di Attributi, Fornitore di Dati di Identificazione Personale e Titolare di Fonte Autentica) che si fa carico della risoluzione della problematica e comunicare l'esito all'Utente. 

Di seguito i requisiti di Esperienza Utente che il Fornitore di Soluzione IT-Wallet DEVE garantire attraverso la propria Soluzione IT-Wallet: 

- l'Utente ha accesso a modalità di assistenza in ogni momento dell'Esperienza Utente, attraverso una chiara indicazione del punto di accesso;  
- l'Utente ha la possibilità di aprire una richiesta di assistenza tramite la propria Istanza IT-Wallet o altri Touchpoint messi a disposizione dal Fornitore di Soluzione IT-Wallet;  
- nel caso di apertura di una richiesta di assistenza, l'Utente riceve conferma tempestiva dell'avvenuta presa in carico;  
- l'Utente è informato preventivamente nel caso in cui sia necessario condividere i propri dati con soggetti terzi;  
- l'Utente è informato nei casi in cui la richiesta di assistenza debba essere gestita al di fuori della propria Istanza IT-Wallet, quindi su canali terzi; 
- l'Utente monitora l'esito della richiesta in ogni momento attraverso funzionalità che DEVONO essere messe a disposizione dagli attori che hanno preso in carico la richiesta. 

Feedback Utente 
---------------

La raccolta dei feedback degli Utenti permette di monitorare l'Esperienza Utente, identificare le aree per una possibile ottimizzazione e misurare l'efficacia del servizio in maniera continuativa. Ogni Fornitore di Soluzione IT-Wallet DOVREBBE predisporre un sistema strutturato di raccolta feedback, per monitorare e migliorare l'Esperienza Utente. 

Tale sistema di feedback POTREBBE essere alimentato da due diverse tipologie di raccolta feedback: 

- **feedback transazionali** (Customer Effort Score, Customer Satisfaction): raccolta contestuale ad azioni specifiche, come l'aggiunta di un Attestato Elettronico o il completamento di un'operazione di presentazione e verifica;  
- **feedback relazionali** (Net Promoter Score): raccolta non contestuale ad azioni specifiche, per la misurazione della percezione generale dell'Utente, in termini di soddisfazione, fedeltà e possibile raccomandazione ad Utenti terzi. 

Di seguito, le indicazioni proposte per l'implementazione di tali tipologie di feedback: 

**Raccolta di feedback transazionale** 

- **Customer Effort Score (CES)**: per misurare la facilità di utilizzo delle funzionalità POSSONO essere predisposti questionari, ad esempio tramite componenti quali modali o pop-up nell'Istanza IT-Wallet, al termine di azioni specifiche o specifici processi, ad esempio: 

   - a conclusione del processo di ottenimento di un Attestato Elettronico;  
   - a conclusione del processo di Autenticazione, se positivo; 
   - a conclusione del processo di presentazione, in particolare a conclusione della prima occasione di presentazione e non più di una volta ogni 6 mesi; 
   - a conclusione dei processi di revoca e disattivazione, per approfondirne le motivazioni. 

- **Customer Satisfaction Survey (CSAT)**: per misurare la soddisfazione generale dell'Utente dopo un periodo prolungato di utilizzo dell'Istanza IT-Wallet POSSONO essere predisposti questionari, ad esempio tramite componenti quali modali o pop-up nell'Istanza IT-Wallet. Si consiglia di utilizzare il CSAT ad intervalli non inferiori a sei mesi e come alternativa al CES, per evitare di somministrare questionari con troppa frequenza. 

**Raccolta di feedback relazionale** 

- **Net Promoter Score (NPS)**: per misurare la fedeltà dell'Utente e la probabilità di raccomandazione ad Utenti terzi, si PUÒ richiedere di esprimere una valutazione una o due volte l'anno attraverso lo stesso canale di erogazione del servizio (e.g. l'Istanza IT-Wallet) o canali esterni, quali e-mail o SMS, e comunque in linea con la strategia di raccolta feedback adottata.

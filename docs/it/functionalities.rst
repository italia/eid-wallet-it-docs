.. include:: ../common/common_definitions.rst
  

Design dell'Esperienza Utente
=============================

.. toctree::
  :caption: Indice di Design dell’Esperienza Utente 
  :maxdepth: 3 

.. include:: design.rst 


Panoramica delle funzionalità
------------------------------


Il Sistema IT-Wallet offre all'utente un'esperienza più semplice, veloce e sicura di accesso ai servizi. Tale servizio si concretizza per l'Utente nella possibilità di utilizzare una Soluzione Wallet, la cui esperienza di fruizione è scandita in tre macro-fasi: pre-utilizzo, utilizzo e post-utilizzo. 

.. only:: format_html

  .. figure:: ./images/svg/UX-phases-usage.svg
    :alt: Fasi dell'Esperienza Utente di utilizzo di un'Istanza del Wallet 
    :width: 100%

    Fasi dell'Esperienza Utente di utilizzo di un'Istanza del Wallet 

.. only:: format_latex

  .. figure:: ./images/pdf/UX-phases-usage.pdf
    :alt: Fasi dell'Esperienza Utente di utilizzo di un'Istanza del Wallet 
    :width: 100%

    Fasi dell'Esperienza Utente di utilizzo di un'Istanza del Wallet 

Le sezioni a seguire si focalizzano sulle macro-fasi di utilizzo e post-utilizzo. Esse definiscono i requisiti funzionali a supporto dell'Esperienza Utente relativi alle fasi di attivazione ottenimento, presentazione, gestione e disattivazione, unitamente ai requisiti di interazione con il servizio in termini di gestione degli errori, richiesta di assistenza e raccolta feedback. 

La documentazione e le risorse aggiuntive sono rese disponibili nella sezione :ref:`official-resources:Risorse Ufficiali`. 

Le Risorse Ufficiali descrivono le modalità di interazione Utente-Istanza del Wallet e le buone pratiche di progettazione al fine di promuovere coerenza tra le diverse Soluzioni Wallet, in termini di modalità di fruizione delle funzionalità. 

Per garantire un’implementazione corretta e coerente, gli Attori Primari: 

* DEVONO utilizzare esclusivamente le Risorse Ufficiali e DEVONO rispettare le tutte le relative specifiche di utilizzo fornite; 

* POSSONO scegliere quale configurazione implementare, tra quelle rese disponibili, ma DEVONO comunque garantire il corretto utilizzo dei componenti atomici come i Pulsanti di Ingaggio;  

* DEVONO garantire il costante aggiornamento delle risorse utilizzate, in linea con l'ultima versione resa disponibile. 

Attivazione dell'Istanza del Wallet 
-----------------------------------

L'attivazione è il passaggio necessario per abilitare l'Utente all'utilizzo delle funzionalità della Soluzione Wallet per l'ottenimento, la presentazione e la gestione dei propri Attestati Elettronici in modo sicuro. Il processo di attivazione consiste in un'operazione di Autenticazione dell'Utente sull'Istanza del Wallet tramite la propria identità digitale che consente la generazione del PID.

Di seguito i requisiti di Esperienza Utente che il Wallet Provider DEVE garantire attraverso la propria Soluzione Wallet: 

- l'Utente scarica la Soluzione Wallet sul suo dispositivo così da generare la propria Istanza del Wallet; 
- l'Utente imposta un metodo di sblocco per la sua Istanza del Wallet se non è già stato impostato in precedenza nell'app. In aggiunta al PIN, l'Utente può decidere di usare il metodo di sblocco usato per il dispositivo e gestito a livello di sistema operativo (e.g. autenticazione biometrica) come alternativa al PIN. L'Utente utilizza il metodo di sblocco ogni qual volta è richiesta un'autorizzazione a garanzia della sicurezza e della protezione delle proprie informazioni; 
- l'Utente prende visione di tutte le informazioni rilevanti sull'attivazione e sulle modalità di utilizzo del servizio. L'Utente inoltre prende visione di eventuali informative del Fornitore di Wallet e del PID Provider e/o termini e condizioni d'uso del servizio. L'Utente dà il proprio consenso per proseguire oppure lo nega per annullare l'operazione; 
- l'Utente sceglie una tra le modalità di Autenticazione disponibili; 
- l‘Utente conclude il flusso di Autenticazione sul servizio del National Identity Provider; 
- l'Utente riceve conferma dell'esito del processo di Autenticazione e, se positivo, visualizza l'anteprima del proprio PID. L'Utente conferma le informazioni mostrate in anteprima per procedere all'attivazione dell'Istanza del Wallet oppure annulla l'operazione; 
- l'Utente autorizza l'operazione utilizzando la modalità di sblocco precedentemente impostata; 
- l'Utente visualizza l'esito positivo dell'avvenuta attivazione dell'Istanza del Wallet. 

Il Fornitore di Wallet DEVE permettere all'Utente in ogni momento di rimuovere il PID ottenuto durante la fase di Attivazione. Inoltre, il PID Provider DOVREBBE permettere all'Utente di revocare il PID ottenuto, tramite uno specifico Touchpoint. Il Fornitore di Wallet DEVE permettere all'Utente di richiedere la disattivazione della propria Istanza del Wallet, anche in assenza del dispositivo su cui è stata installata. Per approfondimenti si rimanda alle sezioni :ref:`functionalities:Disattivazione dell'Istanza del Wallet` e :ref:`functionalities:Gestione degli Attestati Elettronici`. 

In caso di errori nell'utilizzo della Istanza del Wallet, il Fornitore di Wallet DEVE garantire all'Utente la visualizzazione di messaggi coerenti che lo informino e guidino alla loro risoluzione. Per approfondimenti si rimanda alla sezione :ref:`functionalities:Gestione degli errori`.

Focus sul PID – Dati di Identificazione della Persona
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Il PID (Person Identification Data) si riferisce a un set minimo verificato di informazioni sull'identità dell'Utente (vedere :ref:`credential-data-model:Modello di Dati degli Attestati Elettronici`) emesso come risultato del processo di attivazione e reso disponibile nell'Istanza del Wallet.
Di seguito sono riportati i requisiti per la visualizzazione e l'utilizzo del PID a cui ogni Fornitore di Wallet DEVE aderire, al fine di fornire un'esperienza di consultazione e utilizzo coerente e accessibile:

- Il PID DEVE essere visualizzato correttamente su tutti i dispositivi, garantendo un'esperienza coerente su schermi di dimensioni diverse;
- Il PID DEVE essere denominato come definito dal Fornitore PID;
- Il PID DEVE visualizzare il suo stato se diverso da valido per fornire trasparenza sul suo ciclo di vita e PUÒ visualizzarlo se valido. Dettagli specifici sullo stato del PID, se non valido, POSSONO essere forniti (ad esempio, il motivo per cui il PID è stato revocato);
- Il PID DEVE includere Pulsanti di Ingaggio per consentire la gestione del ciclo di vita e permettere all'Utente di revocare il PID, quindi l'intera Istanza del Wallet con tutte le EAA emesse, o di aggiornare il PID in qualsiasi momento (vedere :ref:`functionalities:Gestione degli Attestati Elettronici`);
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

Ad attivazione conclusa, l'Utente PUÒ ottenere uno o più Attestati Elettronici di Attributi all'interno della sua Istanza del Wallet. 

A seconda delle specifiche esigenze dell'Utente, della tipologia di Attestato Elettronico di Attributi e delle disponibilità offerte dal Fornitore di Wallet, dal Fornitore di Attestati Elettronici di Attributi e dalla Fonte Autentica, l'ottenimento degli Attestati Elettronici di Attributi può avvenire attraverso due modalità: 

- **dal Catalogo dell'Istanza del Wallet**: l'Utente esplora l'elenco degli Attestati Elettronici di Attributi messi a disposizione dalla Soluzione Wallet, seleziona quello di suo interesse e avvia la procedura di richiesta che si conclude con l'ottenimento dell'Attestato Elettronico di Attributi nell'Istanza del Wallet); 

- **da un Touchpoint della Fonte Autentica** (o del Fornitore di Attestati Elettronici di Attributi qualora coincida con la Fonte Autentica): l'Utente interagisce col servizio digitale della Fonte Autentica che gli permette di ottenere nella sua Istanza del Wallet uno specifico Attestato Elettronico di Attributi tramite un Pulsante di Ingaggio.

Nonostante le modalità di avvio della richiesta siano diverse, i flussi di ottenimento condividono una struttura e un processo simili. 

Ottenimento dal Catalogo dell'Istanza del Wallet 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Di seguito, sono illustrati i requisiti dell'Esperienza Utente del flusso di ottenimento di un Attestato Elettronico di Attributi dal Catalogo che il Fornitore di Wallet DEVE garantire attraverso la propria Soluzione Wallet: 

- l'Utente accede alla propria Istanza del Wallet utilizzando la modalità di sblocco precedentemente impostata; 
- l'Utente seleziona l'Attestato Elettronico di Attributi che intende aggiungere alla sua Istanza del Wallet scegliendo tra quelli disponibili nel Catalogo; 
- l’Utente seleziona da quale Fornitore di Attestati Elettronici vuole ottenere l’Attestato Elettronico di Attributi, se presente più di uno; 
- l’Utente visualizza eventuali informazioni aggiuntive sui requisiti e/o limitazioni relative all’ottenimento dell’Attestato Elettronico di Attributi, se previste dalla Fonte Autentica; 
- l'Utente prende visione dei dati del PID, qualora richiesti dalla Fonte Autentica per l'ottenimento dell'Attestato Elettronico di Attributi, il nome del relativo Fornitore di Attestati Elettronici di Attributi e di eventuali informative. L'Utente dà il proprio consenso per poter proseguire presentando i dati del PID o altri Attributi al Fornitore di Attestati Elettronici di Attributi oppure annulla l'operazione; 
- l’Utente visualizza eventuali informazioni aggiuntive sui requisiti e/o limitazioni relative all’ottenimento dell’Attestato Elettronico di Attributi, provenienti dalla Fonte Autentica;  
- l'Utente visualizza l'anteprima dell'Attestato Elettronico di Attributi. L'Utente conferma i dati mostrati in anteprima per procedere all'ottenimento oppure annulla l'operazione; 
- l'Utente autorizza l'operazione utilizzando la modalità di sblocco precedentemente impostata; 
- l'Utente visualizza l'esito positivo dell'ottenimento avvenuto; 
- l'Utente visualizza i dettagli dell'Attestato Elettronico di Attributi ottenuto ovvero: i dati in esso contenuti, il nome del Fornitore di Attestati Elettronici di Attributi che ha emesso l'Attestato Elettronico di Attributi e il nome della Fonte Autentica; 
- l'Utente ha evidenza di tutti gli Attestati Elettronici ottenuti navigando la sua Istanza del Wallet. 

Qualora la Fonte Autentica lo ritenesse utile, PUÒ fornire all’Utente delle informazioni aggiuntive relative a un Attestato Elettronico di Attributi. Tali informazioni DEVONO essere mostrate dal Fornitore di Wallet all’Utente nell’Istanza del Wallet prima di avviare l’effettivo flusso di ottenimento dell’Attestato Elettronico di Attributi. Al fine di redigere correttamente questo contenuto informativo, la Fonte Autentica: 

- DEVE utilizzare un linguaggio chiaro (e.g. evitare termini tecnici o complessi), essenziale (es. evitare testi eccessivamente lunghi o articolati) e inclusivo (es. evitare i verbi abilisti) seguendo le buone pratiche di scrittura, linguaggio e tono di voce descritte nelle [RIF_ACCESSIBILITÀ] e, nel caso di enti pubblici, nelle [LG_DESIGN]; 

- DEVE attenersi allo scopo specifico del testo, ossia quello di comunicare informazioni utili all’Utente prima di intraprendere il processo di ottenimento (es. elencare i prerequisiti o dichiarare delle limitazioni che potrebbero influenzare il buon esito della procedura di ottenimento); 

- DEVE garantire l’aggiornamento costante delle informazioni; 

DEVE prevedere un titolo e un testo all’interno del quale PUÒ includere il riferimento a canali esterni per indirizzare verso una procedura, approfondire un determinato argomento e/o aprire richieste di supporto. 

Segue un esempio di testo informativo: 

**Titolo:** Hai già il documento fisico? 

**Testo:** Per ottenere la versione digitale del [Nome documento] devi aver già ottenuto il relativo documento fisico. Se vuoi avere maggiori dettagli, [leggi più informazioni] (URL). 

Per approfondimenti si rimanda alla sezione :ref:`registry-catalogue:Catalogo degli Attestati Elettronici` (vedi claim “``user_information``”). 

Il Fornitore di Wallet DEVE permettere all'Utente di rimuovere un Attestato Elettronico di Attributi dalla sua Istanza del Wallet in ogni momento. In caso di assenza del dispositivo su cui è stata attivata l'Istanza del Wallet, il Fornitore di Wallet DEVE permettere all'Utente di disattivare l'intera Istanza del Wallet tramite un Touchpoint dedicato. Inoltre, i Fornitori di Attestati Elettronici di Attributi DOVREBBERO permettere all'Utente la revoca degli Attestati Elettronici ottenuti, tramite specifici Touchpoint. Per approfondimenti si rimanda alle sezioni :ref:`functionalities:Disattivazione dell'Istanza del Wallet` e :ref:`functionalities:Gestione degli Attestati Elettronici`. 

In caso di problemi di comunicazione tra i sistemi del Fornitore di Attestati Elettronici di Attributi e della Fonte Autentica o in presenza di processi amministrativi o tecnici che non consentono di fornire immediatamente l'Attestato Elettronico di Attributi, gli attori coinvolti POSSONO gestire il flusso di ottenimento in modalità differita. In questo caso, il Fornitore di Wallet DEVE garantire che: 

- l'Utente, giunto all'ultimo step del processo, visualizzi un messaggio che lo invita ad attendere il momento in cui l'Attestato Elettronico di Attributi potrà essere rilasciato; 
- l'Utente venga informato dal Fornitore di Attestati Elettronici di Attributi non appena l'Attestato Elettronico di Attributi è disponibile. 

In caso di dati errati all'interno di un Attestato Elettronico di Attributi già ottenuto o in fase di ottenimento, il Fornitore di Wallet DOVREBBE garantire all'Utente un'adeguata assistenza attraverso la propria Istanza del Wallet. Per approfondimenti si rimanda alla sezione :ref:`functionalities:Assistenza Utente`. 

In caso di errori nell'utilizzo della Istanza del Wallet, il Fornitore di Wallet DEVE garantire all'Utente la visualizzazione di messaggi coerenti che lo informino e guidino alla loro risoluzione. Per approfondimenti si rimanda alla sezione :ref:`functionalities:Gestione degli errori`. 

Ottenimento dal Touchpoint della Fonte Autentica
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Di seguito sono illustrati i requisiti dell'Esperienza Utente del flusso di ottenimento di un Attestato Elettronico di Attributi dal Touchpoint della Fonte Autentica che questa DEVE garantire attraverso il proprio Touchpoint:  

- L’Utente interagisce con il Pulsante di Ingaggio chiaramente esposto nell’interfaccia del Touchpoint; 
- L’Utente seleziona la Soluzione Wallet con la quale procedere, attraverso un’interfaccia che DOVREBBE seguire le indicazioni e le funzionalità previste per la Selection Page descritta nella sezione :ref:functionalities:Autenticazione; 
- (*solo cross-device*) L’Utente scansiona un QR code che invoca l’apertura dell’Istanza del Wallet prescelta, attraverso un’interfaccia che DOVREBBE seguire le indicazioni e le funzionalità previste per la QR code page descritta nella sezione :ref:functionalities:Autenticazione; 
- (*solo cross-device*) L’Utente visualizza un messaggio di invito a continuare sulla propria Istanza del Wallet, attraverso un’interfaccia che DOVREBBE seguire le indicazioni e le funzionalità previste per la waiting page descritta nella sezione :ref:functionalities:Autenticazione; 
- l'Utente accede alla propria Istanza del Wallet utilizzando la modalità di sblocco precedentemente impostata; 
- L’Utente visualizza eventuali informazioni aggiuntive sui requisiti e/o limitazioni relative all’ottenimento dell’Attestato Elettronico di Attributi, provenienti dalla Fonte Autentica;
- l'Utente prende visione dei dati del PID, qualora richiesti dalla Fonte Autentica per l'ottenimento dell'Attestato Elettronico di Attributi, il nome del relativo Fornitore di Attestati Elettronici di Attributi e di eventuali informative. L'Utente dà il proprio consenso per poter proseguire presentando i dati del PID o altri Attributi al Fornitore di Attestati Elettronici di Attributi oppure annulla l'operazione;    

- l'Utente visualizza l'anteprima dell'Attestato Elettronico di Attributi. L'Utente conferma i dati mostrati in anteprima per procedere all'ottenimento oppure annulla l'operazione;  

- l'Utente autorizza l'operazione utilizzando la modalità di sblocco precedentemente impostata;  

- l'Utente visualizza l'esito positivo dell'ottenimento avvenuto;  

- l'Utente visualizza i dettagli dell'Attestato Elettronico di Attributi ottenuto ovvero: i dati in esso contenuti, il nome del Fornitore di Attestati Elettronici di Attributi che ha emesso l'Attestato Elettronico di Attributi e il nome della Fonte Autentica. 

In caso di errori nell'ottenimento dell'Attestato Elettronico di Attributi, la Fonte Autentica DEVE garantire all'Utente la visualizzazione di messaggi coerenti che lo informino e guidino alla loro risoluzione. Per approfondimenti si rimanda alla sezione :ref:functionalities:Gestione degli errori. 


Focus sugli Attestati Elettronici di Attributi
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gli Attestati Elettronici di Attributi (EAA) ottenuti all'interno dell'Istanza del Wallet DOVREBBERO essere visualizzate in un elenco all'interno di una Vista Anteprima. In questo caso, ogni EAA DEVE garantire un elevato livello di riconoscibilità e accessibilità [RIF_ACCESSIBILITÀ] delle informazioni contenute. Di seguito sono riportati i requisiti per la visualizzazione dell'EAA a cui ogni Fornitore di Wallet DEVE aderire per fornire un'esperienza di consultazione e utilizzo coerente e accessibile:

- L'EAA DEVE essere visualizzata correttamente su tutti i dispositivi, garantendo un'esperienza coerente su schermi di dimensioni diverse;
- Il nome dell'EAA DEVE essere chiaramente visibile e sempre visualizzato sia nella Vista Dettagliata che nella Vista Anteprima;
- L'EAA, sia nella Vista Anteprima che nella Vista Dettagliata, DEVE visualizzare il suo stato se diverso da valido per fornire trasparenza sul suo ciclo di vita e PUÒ visualizzarlo se valido. La Vista Anteprima PUÒ anche includere Attributi aggiuntivi per migliorare l'Esperienza Utente e la gestione; ad esempio, PUÒ visualizzare il nome o il logo del Fornitore di Attestati Elettronici di Attributi o del Fornitore PID. La Vista Dettagliata PUÒ fornire dettagli specifici sullo stato se non valido (ad esempio, il motivo per cui l'EAA è revocata);
- L'EAA DEVE includere Pulsanti d'Azione nella Vista Dettagliata per consentire la gestione del ciclo di vita e permettere all'Utente di revocare o aggiornare un'EAA in qualsiasi momento (vedere :ref:`functionalities:Gestione degli Attestati Elettronici`);
- L'EAA DEVE essere un elemento interattivo, affinché l'Utente possa accedere ai servizi forniti dai Verificatori di Attestati Elettronici in contesti digitali e di prossimità (vedere :ref:`functionalities:Presentazione degli Attestati Elettronici`);
- L'EAA PUÒ essere visualizzata in formato tessera nella sua Vista Anteprima, in linea con gli approcci già utilizzati da altri portafogli digitali nel mercato, per rispecchiare l'aspetto di un documento fisico corrispondente. Quando applicabile, la natura digitale del documento PUÒ essere indicata, ad esempio etichettandolo come "versione digitale" nel layout;
- L'EAA DEVE visualizzare le stesse informazioni nella Vista Dettagliata come mostrato nella Vista Anteprima e PUÒ includere dettagli aggiuntivi;
- L'EAA DEVE visualizzare un metodo di assistenza (vedere :ref:`functionalities:Assistenza Utente`);
- Il layout dell'EAA nella Vista Anteprima DEVE essere ottimizzato per scalabilità e usabilità, specialmente quando più EAA vengono visualizzate sulla stessa schermata;
- La rappresentazione dell'EAA DEVE aderire a un insieme definito di specifiche fornite dal Fornitore di Attestati Elettronici di Attributi per garantire riconoscibilità, coerenza e omogeneità tra diverse Soluzioni Wallet.

Il Fornitore di Attestati Elettronici di Attributi:

- DEVE definire un nome/convenzione di denominazione per riferirsi agli EAA emessi, per garantire coerenza tra tutte le Soluzioni Wallet; il nome dell'EAA DEVE essere comprensibile e user-friendly evitando termini tecnici o acronimi quando possibile;
- DEVE definire un insieme chiaro di specifiche per l'EAA per garantire un'identificazione e rappresentazione coerente dell'EAA tra diverse Soluzioni Wallet, in termini di formato, struttura e standard di aspetto (ad es. colore, immagine di sfondo, ecc.).

Presentazione degli Attestati Elettronici 
-----------------------------------------

Il processo di presentazione permette all'Utente di accedere a un servizio oppure di dimostrare la titolarità di un dato o l'idoneità a effettuare una determinata azione. La presentazione degli Attestati Elettronici e la loro conseguente verifica, prevede l'interazione tra un'Istanza del Wallet, gestita dall'Utente, e un'Istanza di Relying Party (o App di Verifica). A seconda delle circostanze e del contesto di interazione si possono delineare i seguenti scenari: 

- **Presentazione in prossimità**: l'Utente presenta il PID e/o un set di Attributi contenuti in uno o più Attestati Elettronici tramite l'Istanza del Wallet direttamente a un Verificatore di Attestati Elettronici o a un dispositivo preposti alla verifica in presenza; 

- **Presentazione da remoto**: l'Utente presenta il PID e/o un set di Attributi contenuti in uno o più Attestati Elettronici tramite l'Istanza del Wallet ad un Verificatore di Attestati Elettronici predisposto per la verifica online al fine, ad esempio, di Autenticarsi e fruire dei servizi erogati. 

Presentazione in prossimità 
^^^^^^^^^^^^^^^^^^^^^^^^^^^

La presentazione in prossimità consente all'Utente di esibire il PID e/o un set di Attributi contenuti in uno o più Attestati Elettronici tramite la propria Istanza del Wallet, secondo due diverse modalità: 

- **Modalità supervisionata**: l'Utente, tramite l'Istanza del Wallet, presenta il PID e/o uno o più Attestati Elettronici di Attributi, a un Verificatore di Attestati Elettronici (e.g. agente delle forze dell'ordine, operatore di sportello, etc.) dotato di un apposito sistema di verifica (:ref:relying-party-instance:App di Verifica Mobile); 

- **Modalità non supervisionata**: l'Utente, tramite l'Istanza del Wallet, presenta il PID e/o un set di Attributi contenuti in uno o più Attestati Elettronici a un dispositivo preposto (e.g. tornello, totem, etc.) dotato di un apposito sistema di verifica (App di Verifica Embedded). 

Di seguito i requisiti dell'Esperienza Utente relativi a entrambe le modalità che il Fornitori di Wallet DEVE garantire attraverso la propria Soluzione Wallet. 

**Modalità supervisionata** 

- L'Utente accede alla propria Istanza del Wallet utilizzando la modalità di sblocco precedentemente impostata; 
- L'Utente accede alla funzionalità dedicata alla generazione del QR Code; 
- L'Utente mostra il QR Code generato al soggetto che opera per conto del Verificatore di Attestati Elettronici, il quale provvede a scansionarlo tramite apposita app o sistema di verifica; 
- L'Utente prende visione dei dati del PID e/o degli Attributi richiesti per la presentazione, del nome del Verificatore di Attestati Elettronici che li richiede e delle relative eventuali informative. L'Utente sceglie se presentare o meno eventuali dati del PID o Attributi non obbligatori ai fini della presentazione (Divulgazione Selettiva). L'Utente dà il proprio consenso per poter proseguire oppure annulla l'operazione; 
- L'Utente autorizza l'operazione utilizzando la modalità di sblocco precedentemente impostata; 
- L'Utente visualizza l'esito positivo della presentazione avvenuta. 

In caso di errori nell'utilizzo dell'Istanza del Wallet, il Fornitore di Wallet DEVE garantire all'Utente la visualizzazione di messaggi coerenti che lo informino e guidino alla loro risoluzione. Per approfondimenti si rimanda alla sezione :ref:`functionalities:Gestione degli errori`. 

**Modalità non supervisionata** 

- L'Utente accede alla propria Istanza del Wallet utilizzando la modalità di sblocco precedentemente impostata; 
- L'Utente accede alla funzionalità dedicata alla generazione del QR Code; 
- L'Utente mostra il QR Code generato al dispositivo preposto (ad esempio un tornello) del Verificatore di Attestati Elettronici per permetterne la scansione;
- L'Utente prende visione dei dati del PID e/o gli Attributi richiesti per la presentazione, del nome del Verificatore di Attestati Elettronici che li richiede e delle relative eventuali informative. L'Utente sceglie se presentare o meno eventuali dati del PID o degli Attributi non obbligatori ai fini della presentazione (Divulgazione Selettiva). L'Utente dà il proprio consenso per poter proseguire oppure annulla l'operazione; 
- L'Utente autorizza l'operazione utilizzando la modalità di sblocco precedentemente impostata; 
- L'Utente visualizza l'esito positivo della presentazione avvenuta. 

In caso di errori nell'utilizzo dell'Istanza del Wallet, il Fornitore di Wallet DEVE garantire all'Utente la visualizzazione di messaggi coerenti che lo informino e guidino alla loro risoluzione. Per approfondimenti si rimanda alla sezione :ref:`functionalities:Gestione degli errori`. 

Presentazione da remoto 
^^^^^^^^^^^^^^^^^^^^^^^

La presentazione da remoto consente all'Utente di esibire il PID e/o un set di Attributi contenuti in uno o più Attestati Elettronici, facendo interagire la propria Istanza del Wallet con il Touchpoint di un Verificatore di Attestati Elettronici, tramite un apposito Pulsante di Ingaggio. 

Tale presentazione può avvenire in due diverse modalità, sulla base del tipo di dispositivo utilizzato per accedere al servizio di interesse: 

- **Same-device**: nel caso in cui l'Utente voglia accedere a un servizio digitale online integrato con un apposito sistema di verifica (:ref:relying-party-instance:App di Verifica Web) utilizzando lo stesso dispositivo su cui ha installato l'Istanza del Wallet; 
- **Cross-device**: nel caso in cui l'Utente voglia accedere a un servizio digitale integrato con un apposito sistema di verifica (:ref:relying-party-instance:App di Verifica Web) utilizzando un dispositivo differente rispetto a quello in cui ha installato l'Istanza del Wallet.  

Di seguito i requisiti dell'Esperienza Utente relativi a entrambe le modalità che il Fornitore di Wallet DEVE garantire attraverso la propria Soluzione Wallet. 

**Same-device** 

- L'Utente clicca sul Pulsante di Ingaggio reso disponibile nel Touchpoint del Verificatore di Attestati Elettronici; 
- L'Utente accede alla propria Istanza del Wallet utilizzando la modalità di sblocco precedentemente impostata; 
- L'Utente prende visione dei dati del PID e/o gli Attributi richiesti per la presentazione, del nome del Verificatore di Attestati Elettronici che li richiede e delle relative eventuali informative. L'Utente sceglie se presentare o meno eventuali dati del PID e/o Attributi non obbligatori ai fini della presentazione (Divulgazione Selettiva). L'Utente dà il proprio consenso per poter proseguire oppure annulla l'operazione; 
- L'Utente autorizza l'operazione utilizzando la modalità di sblocco precedentemente impostata; 
- L'Utente visualizza nell'Istanza del Wallet l'esito positivo della presentazione avvenuta; 
- L'Utente torna al flusso nel Touchpoint del Verificatore di Attestati Elettronici su cui DEVE visualizzare l'esito della presentazione completata. 

In caso di errori nell'utilizzo dell'Istanza del Wallet, il Fornitore di Wallet DEVE garantire all'Utente la visualizzazione di messaggi coerenti che lo informino e guidino alla loro risoluzione. Per approfondimenti si rimanda alla sezione :ref:`functionalities:Gestione degli errori`. 

**Cross-device** 

- L'Utente clicca il Pulsante di Ingaggio reso disponibile nel Touchpoint del Verificatore di Attestati Elettronici che l'Utente sta navigando da un dispositivo diverso da quello su cui è installata l'Istanza del Wallet; 
- L'Utente accede all'Istanza del Wallet che desidera utilizzare dal dispositivo su cui è installata utilizzando la modalità di sblocco precedentemente impostata; 
- L'Utente inquadra il QR Code reso disponibile dal Verificatore di Attestati Elettronici, utilizzando la sua Istanza del Wallet; 
- L'Utente prende visione dei dati del PID e/o degli Attributi richiesti per la presentazione, del nome del Verificatore di Attestati Elettronici che li richiede e delle relative eventuali informative. L'Utente sceglie se presentare o meno eventuali dati del PID e/o Attributi non obbligatori ai fini della presentazione (Divulgazione Selettiva). L'Utente dà il proprio consenso per poter proseguire oppure annulla l'operazione; 
- L'Utente autorizza l'operazione utilizzando la modalità di sblocco precedentemente impostata; 
- L'Utente visualizza nell'Istanza del Wallet l'esito positivo della presentazione avvenuta; 
- L'Utente torna sul Touchpoint del Verificatore di Attestati Elettronici e visualizza l'esito della presentazione completata. 

In caso di errori nell'utilizzo dell'Istanza del Wallet, il Fornitore di Wallet DEVE garantire all'Utente la visualizzazione di messaggi coerenti che lo informino e guidino alla loro risoluzione. Per approfondimenti si rimanda alla sezione :ref:`functionalities:Gestione degli errori`. 

Autenticazione 
""""""""""""""

L'Autenticazione è un caso d'uso specifico della presentazione remota e consente all'Utente di accedere in modo sicuro ai servizi resi disponibili da Verificatori di Attestati Elettronici pubblici e privati, presentando il PID ed eventualmente un set di Attributi contenuti negli Attestati Elettronici di Attributi ottenuti. Questo garantisce all'Utente il pieno controllo sui propri dati e la possibilità di condividere anche i soli dati strettamente necessari alla verifica da parte del Verificatore di Attestati Elettronici. 

Il processo di Autenticazione può avvenire in entrambe le modalità same-device e cross-device descritte sopra. Per quanto riguarda i requisiti funzionali a supporto dell'Esperienza Utente, si DEVONO rispettare gli stessi requisiti previsti per la presentazione in remoto nelle due modalità (same-device e cross-device).

Infatti, a livello di Esperienza Utente, il processo di Autenticazione si distingue da un generico flusso di presentazione principalmente per le modalità di avvio del processo, in questo caso reso possibile a partire da uno specifico pulsante, il Pulsante di Autenticazione. 

Al fine di garantire un processo di Autenticazione adeguato e coerente tra tutti i Verificatori di Attestati Elettronici, ciascun Verificatore di Attestati Elettronici DEVE rispettare i requisiti relativi all'aspetto grafico e all'Esperienza Utente descritti di seguito, unitamente al rispetto di [RIF_ACCESSIBILITÀ] e, nel caso di enti pubblici, delle [LG_DESIGN].

I Verificatori di Attestati Elettronici DOVREBBERO utilizzare le :ref:`official-resources:Risorse Ufficiali` per la progettazione. Qualora non intendano utilizzare tali risorse open source, i Verificatori di Attestati Elettronici POSSONO sviluppare in autonomia le Soluzioni Tecniche abilitanti il flusso di Autenticazione.

.. note::
  Le immagini presenti in questa sezione sono da considerarsi esemplificative in quanto oggetto di evolutive di interfaccia (UI), in attesa della definizione del branding del Sistema IT-Wallet. 
 
I Verificatori di Attestati Elettronici, in ogni caso, DEVONO abilitare il processo di Autenticazione rendendo disponibili le seguenti pagine: 

- **Discovery Page**: ha l'obiettivo di mostrare all'Utente tutti i metodi di Autenticazione disponibili; 
- **Selection Page**: ha lo scopo di mostrare all’Utente tutte le Soluzioni Wallet presenti nel Registro e permettere di scegliere con quale continuare il processo di Autenticazione; 
- **QR code page** (*solo per modalità cross-device*): ha lo scopo di invitare l'Utente a inquadrare il codice QR; 
- **waiting page** (*solo per modalità cross-device*): ha lo scopo di invitare l'Utente a continuare il processo di Autenticazione sulla propria Istanza del Wallet; 
- **thank you page**: ha lo scopo di comunicare all'Utente l'avvenuta Autenticazione; 
- **error page**: ha lo scopo di comunicare all'Utente eventuali errori legati al flusso di Autenticazione. 

Tali pagine DEVONO prevedere i seguenti elementi trasversali ricorrenti, in continuità con l'Identità Visiva del Touchpoint del Verificatore di Attestati Elettronici:

- un **header e/o un subheader**, che permette all'Utente di tornare alla pagina precedente; 
- un **footer** che include l'informativa privacy, le note legali e la Dichiarazione di Accessibilità, ove previsto da normativa. 

Di seguito invece gli elementi specifici caratteristici delle diverse pagine. 

**Discovery Page** 

Per garantire l'Autenticazione tramite il Sistema IT-Wallet, il Verificatore di Attestati Elettronici PUÒ aggiornare la propria Discovery Page con quella resa disponibile nelle Risorse Ufficiali. 

.. only:: format_html

  .. figure:: ./images/svg/discovery-page.svg
    :alt: Modello di layout di Discovery Page a griglia
    :width: 100%

    Modello di layout di Discovery Page a griglia  

.. only:: format_latex  

  .. figure:: ./images/pdf/discovery-page.pdf
    :alt: Modello di layout di Discovery Page a griglia 
    :width: 100% 

     Modello di layout di Discovery Page a griglia 


In alternativa, il Verificatore di Attestati Elettronici PUÒ mantenere la propria Discovery Page, ma DEVE in ogni caso integrare il Pulsante di Autenticazione, come da indicazioni presenti nella sezione :ref:`brand-identity:Pulsante di Autenticazione`.

In ogni caso, nella pagina, il Verificatore di Attestati Elettronici:

- DEVE garantire la presenza di tutte le modalità di Autenticazione attraverso l'identità digitale tra cui la modalità di Autenticazione del Sistema IT-Wallet, quindi tramite il Pulsante di Autenticazione; 
- PUÒ presentare anche modalità di Autenticazione alternative, se disponibili; 
- DOVREBBE garantire informazioni minime a supporto, per permettere all'Utente di compiere una scelta consapevole e informata. 

Nel caso l'Utente stia navigando la pagina del Verificatore di Attestati Elettronici da un Touchpoint diverso da quello su cui ha attivato l'Istanza del Wallet (modalità cross-device), la scelta di Autenticazione tramite il Sistema IT-Wallet DEVE condurre l'Utente alla QR code page. 

Nel caso in cui invece l'Utente stia navigando la pagina del Verificatore di Attestati Elettronici dallo stesso Touchpoint su cui ha attivato l'Istanza del Wallet (modalità same-device) tale pagina DEVE condurre l'Utente all'apertura della propria Istanza del Wallet. 

**Selection Page** 

La Selection Page è la pagina su cui atterra l'Utente dopo che ha scelto di Autenticarsi tramite il Sistema IT-Wallet, e ha lo scopo di presentare all'Utente le Soluzioni Wallet disponibili per effettuare l’Autenticazione.  

Il Verificatore di Attestati Elettronici DOVREBBE implementare la Selection Page resa disponibile nelle Risorse Ufficiali.

.. only:: format_html 

  .. figure:: ./images/svg/selection-page.svg
    :alt: Selection Page
    :width: 100%

     Selection Page 

.. only:: format_latex  

  .. figure:: ./images/svg/selection-page.pdf
    :alt: Selection Page
    :width: 100%

     Selection Page 

In ogni caso, il Verificatore di Attestati Elettronici che implementa la pagina: 

- DEVE includere gli elementi propri dell'Identità Visiva del Sistema IT-Wallet, tra cui il Logo affiancandolo al proprio logo secondo le indicazioni fornite nella sezione 2.1.2 Identità Visiva;  

- DOVREBBE assicurare che i copy presenti nella pagina rispecchino quelli riportati nelle Risorse Ufficiali; 

- DEVE presentare ogni Soluzione Wallet presente nel Registro attraverso un componente modulare che mostra il logo e il nome per esteso; 

- DEVE presentare le Soluzioni Wallet in un layout dinamico che si adatta al numero di Soluzioni Wallet disponibili: quando inferiore a 3 DEVE distribuirle in una griglia a 2 colonne, quando inferiore a 2 DEVE utilizzare un layout ad una colonna centrale; in ogni caso DEVE essere garantito un ordinamento randomico; 

- PUÒ inserire un componente testuale per promuovere la modalità di Autenticazione tramite IT-Wallet, che rimandi al sito ufficiale del Sistema, come rappresentato nelle Risorse Ufficiali; 

- DEVE permettere all’Utente di cercare una Soluzione Wallet attraverso una funzionalità di filtro per nome, quando presenti più di 5 Soluzioni Wallet;  

- DEVE permettere all'Utente di scoprire, in caso di necessità, quali sono le Soluzioni Wallet presenti nel Registro, predisponendo un rimando al sito ufficiale del Sistema IT-Wallet; 

- DEVE includere una Call to Action che permetta all'Utente di interrompere l’operazione e tornare alla Discovery Page. 

**QR code page (*solo per modalità cross-device*)** 

La QR code page è la pagina su cui atterra l'Utente che ha scelto l'Autenticazione tramite il Sistema IT-Wallet in un flusso cross-device, e ha lo scopo di invitare l'Utente a scannerizzare, con la propria Istanza del Wallet, il codice QR generato. 

Il Verificatore di Attestati Elettronici DOVREBBE implementare la QR code page (flusso cross-device) resa disponibile nelle Risorse Ufficiali. 

.. only:: format_html 

  .. figure:: ./images/svg/QR-page.svg
    :alt: QR code page
    :width: 100%

     QR code page 

.. only:: format_latex  

  .. figure:: ./images/svg/QR-page.pdf
    :alt: QR code page
    :width: 100%

     QR code page 

Il Verificatore di Attestati Elettronici che implementa la pagina:

- DEVE includere gli elementi propri dell'Identità Visiva del Sistema IT-Wallet, tra cui il Logo; 
- DOVREBBE assicurare che i copy presenti nella pagina rispecchino quelli riportati nelle Risorse Ufficiali; 
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

La waiting page è la pagina che invita l'Utente a proseguire il processo di Autenticazione sulla propria Istanza del Wallet, a valle della scansione del codice QR. 

Il Verificatore di Attestati Elettronici DOVREBBE implementare la waiting page (cross-device) resa disponibile nelle Risorse Ufficiali. 

.. only:: format_html 

  .. figure:: ./images/svg/waiting-page.svg
    :alt: Waiting page
    :width: 100%

     Waiting page 

.. only:: format_latex 
  .. figure:: ./images/svg/waiting-page.pdf
    :alt: Waiting page
    :width: 100%

     Waiting page 

Il Verificatore di Attestati Elettronici che implementa la pagina: 

- DEVE includere gli elementi propri dell'Identità Visiva del Sistema IT-Wallet, tra cui il Logo e un'icona o altro elemento grafico che aiuti a veicolare il messaggio della pagina; 
- DOVREBBE assicurare che i copy presenti nella pagina rispecchino quelli riportati nelle Risorse Ufficiali.  

**Thank you page** 

La thank you page è la pagina sui cui l'Utente atterra una volta concluso il processo di Autenticazione attraverso la propria Istanza del Wallet e ha l'obiettivo di invitare l'Utente a proseguire nell'area riservata. 

Il Verificatore di Attestati Elettronici DOVREBBE implementare la thank you page resa disponibile nelle Risorse Ufficiali. 

.. only:: format_html 

  .. figure:: ./images/svg/thank-you-page.svg
    :alt: Thank you page
    :width: 100%

     Thank you page 

.. only:: format_latex  

  .. figure:: ./images/svg/thank-you-page.pdf
    :alt: Thank you page
    :width: 100%

     Thank you page 

Il Verificatore di Attestati Elettronici che implementa la pagina: 

- DEVE includere gli elementi propri dell'Identità Visiva del Sistema IT-Wallet, tra cui il Logo e un'icona o altro elemento grafico che aiuti a veicolare il messaggio della pagina; 
- DOVREBBE assicurare che i copy presenti nella pagina rispecchino quelli riportati nelle Risorse Ufficiali;  
- DEVE prevedere una Call to Action che inviti l'Utente a proseguire nell'area riservata del Verificatore di Attestati Elettronici. 

**Error page** 

La pagina di errore rappresenta quella tipologia di pagina su cui l'Utente atterra in caso di errori nel corso del flusso di Autenticazione, e ha lo scopo di comunicare all'Utente la natura di tali errori (es. errore tecnico, assenza di rete, malfunzionamento dell'Istanza del Wallet, consenso alla presentazione dei dati negato etc.) e di presentare le azioni che l'Utente può intraprendere. Per approfondimenti sulle casistiche di errore si rimanda alla sezione :ref:`functionalities:Gestione degli errori`. 
 
Il Verificatore di Attestati Elettronici DOVREBBE implementare la error page resa disponibile nelle Risorse Ufficiali. 

.. only:: format_html 

  .. figure:: ./images/svg/error-page.svg
    :alt: Error page
    :width: 100%

     Error page 

.. only:: format_latex  

  .. figure:: ./images/svg/error-page.pdf
    :alt: Error page
    :width: 100%

     Error page 


Il Verificatore di Attestati Elettronici che implementa la pagina: 

- DEVE includere gli elementi propri dell'Identità Visiva del Sistema IT-Wallet, tra cui il Logo e un'icona o altro elemento grafico che aiuti a veicolare la natura dell'errore; 
- DOVREBBE assicurare che i copy presenti nella pagina rispecchino quelli riportati nelle Risorse Ufficiali;  
- DEVE prevedere una o più Call to Action che invitino l'Utente a intraprendere le azioni previste (es. riprova, contatta l'assistenza, etc.). 

Pulsante di Autenticazione 
~~~~~~~~~~~~~~~~~~~~~~~~~~

Il Pulsante di Autenticazione "Entra con IT-Wallet" funge da Pulsante di Ingaggio, fornendo agli Utenti un modo standardizzato per Autenticarsi utilizzando il proprio portafoglio digitale.

I Verificatori di Attestati Elettronici DEVONO rendere disponibile il Pulsante di Autenticazione all'interno della Discovery Page delle proprie Soluzioni Tecniche per permettere all'Utente di Autenticarsi ai propri servizi tramite un'Istanza del Wallet. 

Il Pulsante di Autenticazione è caratterizzato dai seguenti requisiti: 

- il Pulsante di Autenticazione DEVE essere implementato utilizzando esclusivamente quanto reso disponibile nelle Risorse Ufficiali, e NON DEVE essere ricostruito ad hoc;  

- il Pulsante di Autenticazione DEVE essere utilizzato esclusivamente nelle forme, colori e proporzioni stabilite e NON DEVE essere alterato, distorto o nascosto;  

- il Pulsante di Autenticazione DEVE adattarsi a tutte le risoluzioni di schermo e DEVE essere integrato nella Discovery Page in modo da garantirne i requisiti minimi di usabilità e accessibilità; 

- Gli attori che intendono integrare il Pulsante di Autenticazione nella propria Soluzione Tecnica DEVONO garantirne la traduzione in altre lingue, almeno quella inglese; 

- il Pulsante di Autenticazione DEVE mantenere una distanza minima da altri elementi (``quiet zone``) di almeno 24px; 

- Il Pulsante di Autenticazione DEVE riportare la dicitura “Entra con IT-Wallet"; 

- il Pulsante di Autenticazione DOVREBBE essere sempre accompagnato da un link esterno (ad es. “Scopri di più”) che rimanda al sito ufficiale del Sistema IT-Wallet ``www.wallet.gov.it``; 

- Qualora lo spazio a disposizione lo consenta e/o il contesto lo richieda, il Pulsante di Autenticazione DOVREBBE essere accompagnato da un testo descrittivo, ad esempio “IT-Wallet è il Sistema di portafoglio digitale italiano che ti dà pieno controllo sulle tue informazioni, senza che l’ente che le ha rilasciate venga a conoscenza di quando e come vengono usate” oppure “Accedi tramite un’app IT-Wallet, il Sistema di portafoglio digitale italiano che semplifica le interazioni tra cittadini, pubbliche amministrazioni e soggetti privati, nel mondo fisico e in quello digitale.  Con IT-Wallet hai il pieno controllo sulle tue informazioni, condividendole solo quando necessario e in modo sicuro, senza che l’ente che le ha rilasciate venga a conoscenza di quando e come vengono usate.”; 

Di seguito alcuni esempi non normativi di layout del Pulsante di Autenticazione:  

.. only:: format_html 
  .. figure:: ./images/svg/authentication-button-layout.svg  
    :alt: Varianti del Pulsante di Autenticazione
    :width: 100% 

 Varianti del Pulsante di Autenticazione 

.. only:: format_latex  
  .. figure:: ./images/pdf/authentication-button-layout.pdf 
    :alt: Varianti del Pulsante di Autenticazione 
    :width: 100% 

 Varianti del Pulsante di Autenticazione 

Le modalità di integrazione del Pulsante di Autenticazione nella Discovery Page possono essere molteplici a seconda del layout della pagina stessa. Di seguito alcuni esempi illustrativi e non esaustivi di Discovery Page, rispettivamente con struttura a griglia, a tab e in lista. 

.. only:: format_html

  .. figure:: ./images/svg/discovery-page-layouts.svg
    :alt: Esempi di layout di Discovery Page a griglia, a tab e in lista
    :width: 100%

    Esempi di layout di Discovery Page a griglia, a tab e in lista

.. only:: format_latex 
  
  .. figure:: ./images/pdf/discovery-page-layouts.pdf
    :alt: Esempi di layout di Discovery Page a griglia, a tab e in lista
    :width: 100%

    Esempi di layout di Discovery Page a griglia, a tab e in lista

Per maggiori dettagli sull'utilizzo del Pulsante di Autenticazione vedi la sezione :ref:`functionalities:Autenticazione`.

**Pulsante "Entra con IT-Wallet" - codice html** 

Il pulsante è disponibile in 3 varianti (default / M / L ) ed in formato "get" (chiamata ad una pagina esterna) e "post" (form interna al pulsante). Il sistema richiede Jquery 1.8+. Di seguito il codice html: 

``TBD``

**Pulsante “Entra con IT-Wallet" - svg**

<svg width="267" height="49" viewBox="0 0 267 49" fill="none" xmlns="http://www.w3.org/2000/svg"> 

<rect x="0.945312" y="0.537109" width="266" height="48" rx="4" fill="#0066CC"/> 

<path d="M25.0053 23.3771L29.4253 18.9571L25.0053 14.5371L20.5853 18.9571L25.0053 23.3771ZM30.6453 29.0171L35.0653 24.5971L30.6453 20.1771L26.2253 24.5971L30.6453 29.0171ZM19.3653 29.0171L23.7853 24.5971L19.3653 20.1771L14.9453 24.5971L19.3653 29.0171ZM25.0053 34.6571L29.4253 30.2371L25.0053 25.8171L20.5853 30.2371L25.0053 34.6571Z" fill="white"/> 

<path d="M48.9453 4.53711V44.5371" stroke="white" stroke-linejoin="round"/> 

<path d="M93.6624 30.5371V19.5771H100.574V21.1291H95.4384V24.2331H99.6144V25.7691H95.4384V28.9691H100.574V30.5371H93.6624ZM104.042 30.5371H102.298V22.5371H104.026V23.0331C104.805 22.5851 105.541 22.3611 106.234 22.3611C107.301 22.3611 108.026 22.6651 108.41 23.2731C108.805 23.8704 109.002 24.8624 109.002 26.2491V30.5371H107.274V26.2971C107.274 25.4331 107.178 24.8198 106.986 24.4571C106.805 24.0944 106.426 23.9131 105.85 23.9131C105.306 23.9131 104.784 24.0198 104.282 24.2331L104.042 24.3291V30.5371ZM115.337 24.0251H113.129V27.5451C113.129 28.1958 113.177 28.6278 113.273 28.8411C113.369 29.0544 113.614 29.1611 114.009 29.1611L115.321 29.1131L115.401 30.5051C114.686 30.6438 114.142 30.7131 113.769 30.7131C112.862 30.7131 112.238 30.5051 111.897 30.0891C111.566 29.6731 111.401 28.8891 111.401 27.7371V24.0251H110.377V22.5371H111.401V20.2171H113.129V22.5371H115.337V24.0251ZM116.767 30.5371V22.5371H118.495V23.4971C119.402 22.9104 120.308 22.5318 121.215 22.3611V24.1051C120.298 24.2864 119.514 24.5211 118.863 24.8091L118.511 24.9531V30.5371H116.767ZM128.468 25.0011V28.6491C128.479 28.8838 128.538 29.0598 128.644 29.1771C128.762 29.2838 128.938 29.3531 129.172 29.3851L129.124 30.7131C128.207 30.7131 127.498 30.5158 126.996 30.1211C126.143 30.5158 125.284 30.7131 124.42 30.7131C122.831 30.7131 122.036 29.8651 122.036 28.1691C122.036 27.3584 122.25 26.7718 122.676 26.4091C123.114 26.0464 123.78 25.8278 124.676 25.7531L126.74 25.5771V25.0011C126.74 24.5744 126.644 24.2758 126.452 24.1051C126.271 23.9344 125.999 23.8491 125.636 23.8491C124.954 23.8491 124.1 23.8918 123.076 23.9771L122.564 24.0091L122.5 22.7771C123.663 22.4998 124.73 22.3611 125.7 22.3611C126.682 22.3611 127.386 22.5744 127.812 23.0011C128.25 23.4171 128.468 24.0838 128.468 25.0011ZM124.884 26.9851C124.148 27.0491 123.78 27.4491 123.78 28.1851C123.78 28.9211 124.106 29.2891 124.756 29.2891C125.29 29.2891 125.855 29.2038 126.452 29.0331L126.74 28.9371V26.8091L124.884 26.9851ZM137.165 22.3611C137.731 22.3611 138.397 22.4358 139.165 22.5851L139.565 22.6651L139.501 24.0411C138.659 23.9558 138.035 23.9131 137.629 23.9131C136.819 23.9131 136.275 24.0944 135.997 24.4571C135.72 24.8198 135.581 25.5024 135.581 26.5051C135.581 27.5078 135.715 28.2011 135.981 28.5851C136.248 28.9691 136.803 29.1611 137.645 29.1611L139.517 29.0331L139.565 30.4251C138.488 30.6171 137.677 30.7131 137.133 30.7131C135.917 30.7131 135.059 30.3878 134.557 29.7371C134.067 29.0758 133.821 27.9984 133.821 26.5051C133.821 25.0118 134.083 23.9504 134.605 23.3211C135.128 22.6811 135.981 22.3611 137.165 22.3611ZM141.605 23.4011C142.16 22.7078 143.077 22.3611 144.357 22.3611C145.637 22.3611 146.549 22.7078 147.093 23.4011C147.648 24.0944 147.925 25.1344 147.925 26.5211C147.925 27.9078 147.659 28.9531 147.125 29.6571C146.592 30.3611 145.669 30.7131 144.357 30.7131C143.045 30.7131 142.123 30.3611 141.589 29.6571C141.056 28.9531 140.789 27.9078 140.789 26.5211C140.789 25.1344 141.061 24.0944 141.605 23.4011ZM142.917 28.6011C143.163 29.0278 143.643 29.2411 144.357 29.2411C145.072 29.2411 145.552 29.0278 145.797 28.6011C146.043 28.1744 146.165 27.4758 146.165 26.5051C146.165 25.5344 146.032 24.8464 145.765 24.4411C145.509 24.0358 145.04 23.8331 144.357 23.8331C143.675 23.8331 143.2 24.0358 142.933 24.4411C142.677 24.8464 142.549 25.5344 142.549 26.5051C142.549 27.4758 142.672 28.1744 142.917 28.6011ZM151.402 30.5371H149.658V22.5371H151.386V23.0331C152.164 22.5851 152.9 22.3611 153.594 22.3611C154.66 22.3611 155.386 22.6651 155.77 23.2731C156.164 23.8704 156.362 24.8624 156.362 26.2491V30.5371H154.634V26.2971C154.634 25.4331 154.538 24.8198 154.346 24.4571C154.164 24.0944 153.786 23.9131 153.21 23.9131C152.666 23.9131 152.143 24.0198 151.642 24.2331L151.402 24.3291V30.5371ZM162.116 30.5371V19.5771H163.892V30.5371H162.116ZM165.356 21.1611V19.5771H173.356V21.1611H170.268V30.5371H168.476V21.1611H165.356ZM173.593 27.0171V25.4331H178.377V27.0171H173.593ZM179.47 19.5771H181.342L182.91 29.0011H183.246L185.326 19.6091H187.406L189.486 29.0011H189.838L191.406 19.5771H193.278L191.118 30.5371H188.254L186.366 21.7531L184.494 30.5371H181.614L179.47 19.5771ZM200.406 25.0011V28.6491C200.416 28.8838 200.475 29.0598 200.582 29.1771C200.699 29.2838 200.875 29.3531 201.11 29.3851L201.062 30.7131C200.144 30.7131 199.435 30.5158 198.934 30.1211C198.08 30.5158 197.222 30.7131 196.358 30.7131C194.768 30.7131 193.974 29.8651 193.974 28.1691C193.974 27.3584 194.187 26.7718 194.614 26.4091C195.051 26.0464 195.718 25.8278 196.614 25.7531L198.678 25.5771V25.0011C198.678 24.5744 198.582 24.2758 198.39 24.1051C198.208 23.9344 197.936 23.8491 197.574 23.8491C196.891 23.8491 196.038 23.8918 195.014 23.9771L194.502 24.0091L194.438 22.7771C195.6 22.4998 196.667 22.3611 197.638 22.3611C198.619 22.3611 199.323 22.5744 199.75 23.0011C200.187 23.4171 200.406 24.0838 200.406 25.0011ZM196.822 26.9851C196.086 27.0491 195.718 27.4491 195.718 28.1851C195.718 28.9211 196.043 29.2891 196.694 29.2891C197.227 29.2891 197.792 29.2038 198.39 29.0331L198.678 28.9371V26.8091L196.822 26.9851ZM202.691 30.5371V19.2091H204.435V30.5371H202.691ZM206.738 30.5371V19.2091H208.482V30.5371H206.738ZM216.385 29.0971L216.833 29.0491L216.865 30.3451C215.649 30.5904 214.571 30.7131 213.633 30.7131C212.449 30.7131 211.595 30.3878 211.073 29.7371C210.561 29.0864 210.305 28.0464 210.305 26.6171C210.305 23.7798 211.462 22.3611 213.777 22.3611C216.017 22.3611 217.137 23.5824 217.137 26.0251L217.025 27.2731H212.065C212.075 27.9344 212.219 28.4198 212.497 28.7291C212.774 29.0384 213.291 29.1931 214.049 29.1931C214.806 29.1931 215.585 29.1611 216.385 29.0971ZM215.425 25.9291C215.425 25.1398 215.297 24.5904 215.041 24.2811C214.795 23.9611 214.374 23.8011 213.777 23.8011C213.179 23.8011 212.742 23.9664 212.465 24.2971C212.198 24.6278 212.059 25.1718 212.049 25.9291H215.425ZM223.118 24.0251H220.91V27.5451C220.91 28.1958 220.958 28.6278 221.054 28.8411C221.15 29.0544 221.395 29.1611 221.79 29.1611L223.102 29.1131L223.182 30.5051C222.467 30.6438 221.923 30.7131 221.55 30.7131C220.643 30.7131 220.019 30.5051 219.678 30.0891C219.347 29.6731 219.182 28.8891 219.182 27.7371V24.0251H218.158V22.5371H219.182V20.2171H220.91V22.5371H223.118V24.0251Z" fill="white"/> 

</svg>

Gestione degli Attestati Elettronici
------------------------------------

Il Fornitore di Wallet, attraverso la propria Soluzione Wallet, e il PID Provider o il Fornitore di Attestati Elettronici di Attributi, attraverso Touchpoint dedicati, DEVONO dare all'Utente la possibilità di gestire in ogni momento i propri Attestati Elettronici. 

In questa sezione sono illustrate tre diverse categorie di requisiti per la gestione del ciclo di vita di ogni Attestato Elettronico e nello specifico per la gestione: 

- **del suo stato**: per consentire all'Utente di appurare la condizione di validità o invalidità di un Attestato Elettronico; 
- **dei suoi utilizzi**: per consentire all'Utente di visualizzare e gestire lo storico delle transazioni effettuate utilizzando un Attestato Elettronico; 
- **dei suoi dati**: per consentire all'Utente di archiviare e ripristinare ogni Attestato Elettronico di Attributi in linea col principio di *data portability*. 

Di seguito i principali aspetti che impattano e determinano l'Esperienza Utente nell'ambito della gestione degli Attestati Elettronici per mezzo di un'Istanza del Wallet e i requisiti funzionali riferiti a ciascuna categoria. 

Stato degli Attestati Elettronici 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Per garantire l'affidabilità e promuovere il corretto utilizzo della propria Soluzione Wallet, il Fornitore di Wallet DEVE dare all'Utente visibilità dello stato degli Attestati Elettronici ottenuti nella propria Istanza del Wallet sulla base delle informazioni ricevute dal Fornitore di Attestati Elettronici, gestore del loro ciclo di vita. 

Ogni Attestato Elettronico può assumere lo stato valido o non valido, con conseguenti impatti circa le sue possibilità di utilizzo, in particolare: 

- **valido**: gli Attestati Elettronici validi DEVONO essere utilizzabili quindi presentabili. Tra questi rientrano anche gli Attestati Elettronici in scadenza. Qualora un Attestato Elettronico fosse in scadenza, l'Istanza del Wallet DOVREBBE informare l'Utente con un adeguato preavviso utile ad avviare per tempo una richiesta di ri-ottenimento o, se necessario, di revoca; 

- **non valido**: gli Attestati Elettronici non validi NON DEVONO essere utilizzabili quindi presentabili. Rientrano in questa categoria gli Attestati Elettronici scaduti o revocati. In questi casi l'Istanza del Wallet DEVE essere informare l'Utente circa lo stato di non validità e DOVREBBE dare evidenza della motivazione. Qualora l'Attestato Elettronico non fosse più valido, e non fosse quindi più possibile alcuno scenario di utilizzo, l'Istanza del Wallet PUÒ prevedere dei meccanismi per inibire la Vista di Dettaglio di tale Attestato Elettronico, al fine di incoraggiare l'Utente ad aggiornarlo o cancellarlo tramite apposito testo informativo e Call To Action. 

Revoca degli Attestati Elettronici 
""""""""""""""""""""""""""""""""""

La revoca si configura come quel meccanismo che determina il passaggio di un Attestato Elettronico da uno stato valido a uno stato non valido. La revoca può avvenire in modalità attiva o passiva: 

- **Revoca attiva**: ovvero la revoca di un Attestato Elettronico su richiesta dell'Utente. Tale processo comporta la sola revoca dell'Attestato Elettronico e non del corrispettivo documento fisico, se esistente. Di seguito un elenco esemplificativo di scenari in cui il Fornitore di Wallet DEVE dare possibilità all'Utente di richiedere la revoca di un Attestato Elettronico: 

   - l'Utente decide di non voler più possedere uno specifico Attestato Elettronico;
   - l'Utente decide di disattivare la propria Istanza del Wallet e, di conseguenza, tutti gli Attestati Elettronici precedentemente ottenuti; 
   - l'Utente non è più in possesso del dispositivo su cui è installata la propria Istanza del Wallet a causa di uno smarrimento o un furto. 

- **Revoca passiva**: ovvero la revoca di un Attestato Elettronico gestita dal relativo Fornitore di Attestati Elettronici per conto della Fonte Autentica. In questo caso l'Istanza del Wallet DEVE informare l'Utente del cambiamento di stato dell'Attestato Elettronico e, in aggiunta, il Fornitore di Attestati Elettronici PUÒ informare l'Utente attraverso altri Touchpoint. Di seguito un elenco esemplificativo di scenari che porterebbero alla revoca di un Attestato Elettronico: 

   - il documento fisico corrispondente all'Attestato Elettronico è stato dichiarato smarrito o danneggiato da parte dell'Utente tramite apposito canale/ Touchpoint; 
   - il documento fisico corrispondente all'Attestato Elettronico è stato revocato dalle autorità competenti; 
   - non sussistono più i requisiti minimi di sicurezza e/o affidabilità di una o più delle parti coinvolte; 
   - il dispositivo dell'Utente non soddisfa più i requisiti minimi di sicurezza (dispositivo rootato o jailbroken). 
 
Storico degli Attestati Elettronici 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Al fine di garantire i principi di visibilità e trasparenza, il Fornitore di Wallet DEVE permettere all'Utente di visualizzare lo storico di tutte le transazioni effettuate, ovvero l'utilizzo degli Attestati Elettronici di Attributi tramite l'Istanza del Wallet. In particolare: 

- l'Istanza del Wallet DEVE mostrare all'Utente con quali Verificatori di Attestati Elettronici ha interagito e quali Attestati Elettronici sono stati oggetto di presentazione e verifica; 
- l'Istanza del Wallet DEVE permettere all'Utente di richiedere facilmente al Verificatore di Attestati Elettronici la cancellazione delle proprie informazioni oggetto delle precedenti presentazioni. 

Archiviazione e ripristino degli Attestati Elettronici di Attributi 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Con l'obiettivo di garantire il principio di data portability, la Soluzione Wallet DEVE garantire all'Utente l'accesso a specifiche funzionalità per: 

- richiedere l'archiviazione, quindi il salvataggio, degli Attestati Elettronici di Attributi ottenuti su una specifica Istanza del Wallet; 
- richiedere il ripristino dei propri Attestati Elettronici di Attributi su un'altra Istanza del Wallet. 

Disattivazione dell'Istanza del Wallet 
--------------------------------------

La disattivazione dell'Istanza del Wallet è la funzionalità che rende l'Istanza del Wallet disattiva e quindi non più operativa. La disattivazione dell'Istanza del Wallet può essere scatenata da attori differenti a seconda delle circostanze, in particolare: 

- da parte dell'Utente nel caso in cui, ad esempio: 

   - il dispositivo sia stato smarrito o rubato; 
   - il dispositivo risulti compromesso; 
   - il dispositivo sia stato resettato alle impostazioni di fabbrica. 

- da parte di un ente terzo titolato nel caso in cui, ad esempio: 

   - la Soluzione Wallet non rispetti più i requisiti minimi di sicurezza. 
 
Il Fornitore di Wallet DEVE, quindi, garantire all'Utente la possibilità di disattivare volontariamente la propria Istanza del Wallet tramite: 

- l'Istanza del Wallet stessa; 
- un Touchpoint (e.g. un sito web) fornito dal Fornitore di Wallet; 
- l'app store del proprio dispositivo, disinstallando l'Istanza del Wallet. 

Di seguito i requisiti funzionali a supporto dell'Esperienza Utente relativi alla disattivazione dell'Istanza del Wallet che il Fornitore di Wallet DEVE garantire attraverso la propria Soluzione Wallet: 

- l'Utente accede alla propria Istanza del Wallet utilizzando la modalità di sblocco precedentemente impostata oppure si Autentica presso il Touchpoint reso disponibile dal Fornitore di Wallet; 
- l'Utente seleziona la funzionalità di disattivazione dell'Istanza del Wallet; 
- l'Utente viene informato che la disattivazione dell'Istanza del Wallet renderà non più utilizzabili gli Attestati Elettronici precedentemente ottenuti; 
- l'Utente conferma l'azione per procedere con la disattivazione oppure annulla l'operazione; 
- l'Utente visualizza l'esito positivo della disattivazione avvenuta; 
- l'Utente, in caso di nuovo accesso, prende visione del fatto che l'Istanza del Wallet è disattiva; 
- l'Utente ha la possibilità di riattivare l'Istanza del Wallet riscaricando l'app dall'app store, in caso di cancellazione, e/o ripercorrendo il processo di attivazione. Per approfondimenti si rimanda alla sezione :ref:`functionalities:Attivazione dell'Istanza del Wallet`. 

Una volta riattivata l'Istanza del Wallet, gli Attestati Elettronici di Attributi potranno essere ri-ottenuti avviando nuovamente il processo di ottenimento o di ripristino. Per approfondimenti si rimanda rispettivamente alle sezioni :ref:`functionalities:Ottenimento degli Attestati Elettronici di Attributi` e :ref:`functionalities:Archiviazione e ripristino degli Attestati Elettronici di Attributi`. 

In caso di errori nell'utilizzo dell'Istanza del Wallet, il Fornitore di Wallet DEVE garantire all'Utente la visualizzazione di messaggi coerenti che lo informino e guidino alla loro risoluzione. Per approfondimenti si rimanda alla sezione :ref:`functionalities:Gestione degli errori`. 

Gestione degli errori 
---------------------

Il Sistema IT-Wallet prevede l'interazione di una molteplicità di servizi erogati da diversi attori. È quindi importante che venga definito un modello di gestione degli errori efficace, con l'obiettivo di migliorare la percezione e il senso di affidabilità dell'interno ecosistema e permettere all'Utente di sentirsi guidato nell'interazione con le diverse Soluzioni Tecniche e nella gestione consapevole di eventuali criticità durante la fruizione del servizio. 

Una comunicazione efficace in caso di errore determina un vantaggio anche per gli attori coinvolti, in quanto concorre alla riduzione delle richieste di assistenza e, quindi, alla minimizzazione dell'impatto sui sistemi.

Di seguito vengono presentati i requisiti e le principali buone pratiche di gestione dell'errore, riferite alle modalità di interazione tra l'Utente e la propria Istanza del Wallet. È fondamentale che ciascun Attore Primario implementi una corretta gestione degli errori, in conformità alle attuali Specifiche Tecniche, al fine di comunicarli, direttamente o indirettamente, all'Utente e tramite l'Istanza del Wallet. Gli errori possono essere declinati, sulla base della loro natura, come segue: 

- **la fase dell'Esperienza Utente** in cui l'errore può verificarsi: attivazione o disattivazione dell'Istanza del Wallet, ottenimento, presentazione o gestione degli Attestati Elettronici; 
- **la tipologia di errore**: di sistema, di comunicazione tra attori, etc.; 
- **l'attore responsabile dell'errore**: Fornitore di Wallet, PID Provider, Fornitore di Attestati Elettronici di Attributi, Fonte Autentica; 
- **la modalità di restituzione dell'errore**: messaggio in pagina, banner, toast message, etc.; 
- **le azioni suggerite all'Utente per risolvere l'errore**: suggerimento di attesa, richiesta di effettuare un nuovo tentativo, rimando alle domande frequenti e/o al servizio di assistenza, etc.; 
- **le modalità di presa in carico dell'errore**: apertura di una richiesta di assistenza tramite l'Istanza del Wallet, rimando ad altri canali di approfondimento, etc. Per approfondimenti si rimanda alla sezione Assistenza Utente. 

Di seguito, una lista non esaustiva delle principali casistiche di errore, con riferimento all'attore responsabile della loro gestione, per ciascuna fase dell'Esperienza Utente. La lista dettagliata degli errori da gestire per ogni endpoint di interazione con l'Utente è disponibile nelle sottosezioni dedicate agli errori all'interno di :ref:`Endpoints`.

Errori di Attivazione dell'Istanza del Wallet 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 
.. list-table::
   :widths: 80 20
   :header-rows: 1

   * - Tipologia di errore
     - Attore responsabile 
   * - Il dispositivo non supporta la Soluzione Wallet (e.g. assenza dei requisiti minimi di sicurezza o tecnologici)
     - Fornitore di Wallet 
   * - I servizi del Fornitore di Wallet non rispondono (e.g. errori tecnici o assenza connessione) 
     - Fornitore di Wallet 
   * - I servizi del PID Provider non rispondono (e.g. errori tecnici) 
     - PID Provider
   * - Il processo di Autenticazione sul servizio del National Identity Provider non è andato a buon fine (e.g. errori tecnici, identità non riconosciuta, etc.)
     - National Identity Provider 

Errori di ottenimento degli Attestati Elettronici di Attributi
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 80 20
   :header-rows: 1

   * - Tipologia di errore
     - Attore responsabile 
   * - L'Istanza del Wallet e/o il PID non risultano attivi 
     - Fornitore di Wallet
   * - Il servizio di ottenimento di un Attestato Elettronico di Attributi non è disponibile (e.g. errori tecnici) 
     - Fornitore di Attestati Elettronici di Attributi, Fonte Autentica
   * - L'Utente non riesce ad ottenere nella propria Istanza del Wallet un certo Attestato Elettronico di Attributi (e.g. assenza di titolarità, versione fisica non valida o scaduta, etc.) 
     - Fonte Autentica  

Errori di presentazione degli Attestati Elettronici
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 80 20
   :header-rows: 1

   * - Tipologia di errore
     - Attore responsabile 
   * - L'Utente non possiede all'interno della propria Istanza del Wallet gli Attributi contenuti in uno o più Attestati Elettronici richiesti per la fruizione di un determinato servizio 
     - Fornitore di Wallet 
   * - I servizi del Fornitore di Wallet e/o del Verificatore di Attestati Elettronici non rispondono (e.g. errori tecnici o assenza connessione) 
     - Fornitore di Wallet, Verificatore di Attestati Elettronici 

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
     - PID Provider 

Errori di disattivazione dell'Istanza del Wallet
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 80 20
   :header-rows: 1

   * - Tipologia di errore
     - Attore responsabile
   * - Il servizio di disattivazione dell'Istanza del Wallet non è disponibile (e.g. errori tecnici) 
     - Fornitore di Wallet 

Oltre alla gestione degli errori, DEVE essere garantita da parte di tutti gli Attori Primari anche la gestione di esiti negativi dovuti alla volontà dell'Utente di abbandonare o annullare un flusso (es. attivazione, ottenimento, presentazione, etc.). In questi casi DEVE essere previsto un feedback che dia conferma all'Utente della scelta intrapresa e che PUÒ includere una Call to Action per proseguire.

Assistenza Utente 
-----------------

Per un'efficace gestione degli errori e di eventuali altre problematiche, gli Attori Primari DEVONO garantire un'adeguata assistenza all'Utente, strutturando un modello di assistenza semplice ed efficace basato sui seguenti principi: 

- **Risoluzione autonoma**: permettere all'Utente di consultare domande frequenti (FAQ) sui contenuti e sulle funzionalità dell'Istanza del Wallet, al fine di risolvere eventuali casistiche di errore o problematiche in maniera autonoma. 

- **Apertura guidata di una segnalazione**: guidare l'Utente all'eventuale apertura di una segnalazione, in modo da circoscrivere la problematica e facilitare la sua gestione. 

- **Collaborazione tra attori**: rendere possibile un adeguato coordinamento tra tutti gli attori coinvolti (Fornitore di Wallet, Fornitore di Attestati Elettronici di Attributi, PID Provider e Fonte Autentica) in base al proprio ruolo e alle modalità operative specifiche. 

- **Comunicazione efficiente**: garantire all'Utente la possibilità di monitorare lo stato aggiornato della propria richiesta durante tutte le fasi di lavorazione, attraverso una comunicazione chiara, continua e coordinata. 

Per applicare queste buone pratiche, gli attori coinvolti DOVREBBERO implementare i seguenti livelli di assistenza gerarchici: 

	1. **I Livello – Gestione autonoma**: il Fornitore di Wallet DOVREBBE permettere all'Utente di disporre di una sezione di domande frequenti (FAQ) all'interno della propria Istanza del Wallet per chiarire dubbi e risolvere in autonomia alcune problematiche. Ogni attore DOVREBBE formulare delle domande frequenti e relative risposte specifiche rispetto a dati e funzionalità messe a disposizione al Fornitore di Wallet o nei propri Touchpoint. Per alcune casistiche di errore, il Fornitore di Wallet DOVREBBE rendere direttamente disponibile il canale di assistenza di un altro attore, per facilitare una gestione tempestiva ed evitare l'apertura di una richiesta di assistenza nell'Istanza del Wallet. 

	2. **II Livello – Richiesta di assistenza al Fornitore di Wallet**: se il I livello non fosse sufficiente, il Fornitore di Wallet DOVREBBE permettere all'Utente di aprire una o più richieste di assistenza, effettuare una diagnosi e procedere alla risoluzione della problematica, se di sua competenza. Tali richieste DOVREBBERO essere gestite tramite l'Istanza del Wallet o altri Touchpoint del Fornitore di Wallet.

	3. **III Livello – Inoltro della richiesta all'attore responsabile della problematica**: se il II livello non fosse sufficiente, il Fornitore di Wallet DOVREBBE garantire che la richiesta sia inoltrata all'attore responsabile (Fornitore di Attestati Elettronici di Attributi, PID Provider e Fonte Autentica) che si fa carico della risoluzione della problematica e comunicare l'esito all'Utente. 

Di seguito i requisiti di Esperienza Utente che il Fornitore di Wallet DEVE garantire attraverso la propria Soluzione Wallet: 

- l'Utente ha accesso a modalità di assistenza in ogni momento dell'Esperienza Utente, attraverso una chiara indicazione del punto di accesso; 
- l'Utente ha la possibilità di aprire una richiesta di assistenza tramite la propria Istanza del Wallet o altri Touchpoint messi a disposizione dal Fornitore di Wallet; 
- nel caso di apertura di una richiesta di assistenza, l'Utente riceve conferma tempestiva dell'avvenuta presa in carico; 
- l'Utente è informato preventivamente nel caso in cui sia necessario condividere i propri dati con soggetti terzi; 
- l'Utente è informato nei casi in cui la richiesta di assistenza debba essere gestita al di fuori della propria Istanza del Wallet, quindi su canali terzi; 
- l'Utente monitora l'esito della richiesta in ogni momento attraverso funzionalità che DEVONO essere messe a disposizione dagli attori che hanno preso in carico la richiesta. 

Feedback Utente 
---------------

La raccolta dei feedback degli Utenti permette di monitorare l'Esperienza Utente, identificare le aree per una possibile ottimizzazione e misurare l'efficacia del servizio in maniera continuativa. Ogni Fornitore di Wallet DOVREBBE predisporre un sistema strutturato di raccolta feedback, per monitorare e migliorare l'Esperienza Utente. 

Tale sistema di feedback POTREBBE essere alimentato da due diverse tipologie di raccolta feedback: 

- **feedback transazionali** (Customer Effort Score, Customer Satisfaction): raccolta contestuale ad azioni specifiche, come l'aggiunta di un Attestato Elettronico o il completamento di un'operazione di presentazione e verifica;  
- **feedback relazionali** (Net Promoter Score): raccolta non contestuale ad azioni specifiche, per la misurazione della percezione generale dell'Utente, in termini di soddisfazione, fedeltà e possibile raccomandazione ad Utenti terzi. 

Di seguito, le indicazioni proposte per l'implementazione di tali tipologie di feedback: 

**Raccolta di feedback transazionale** 

- **Customer Effort Score (CES)**: per misurare la facilità di utilizzo delle funzionalità POSSONO essere predisposti questionari, ad esempio tramite componenti quali modali o pop-up nell'Istanza del Wallet, al termine di azioni specifiche o specifici processi, ad esempio: 

   - a conclusione del processo di ottenimento di un Attestato Elettronico;  
   - a conclusione del processo di Autenticazione, se positivo; 
   - a conclusione del processo di presentazione, in particolare a conclusione della prima occasione di presentazione e non più di una volta ogni 6 mesi; 
   - a conclusione dei processi di revoca e disattivazione, per approfondirne le motivazioni. 

- **Customer Satisfaction Survey (CSAT)**: per misurare la soddisfazione generale dell'Utente dopo un periodo prolungato di utilizzo dell'Istanza del Wallet POSSONO essere predisposti questionari, ad esempio tramite componenti quali modali o pop-up nell'Istanza del Wallet. Si consiglia di utilizzare il CSAT ad intervalli non inferiori a sei mesi e come alternativa al CES, per evitare di somministrare questionari con troppa frequenza. 

**Raccolta di feedback relazionale** 

- **Net Promoter Score (NPS)**: per misurare la fedeltà dell'Utente e la probabilità di raccomandazione ad Utenti terzi, si PUÒ richiedere di esprimere una valutazione una o due volte l'anno attraverso lo stesso canale di erogazione del servizio (e.g. l'Istanza del Wallet) o canali esterni, quali e-mail o SMS, e comunque in linea con la strategia di raccolta feedback adottata.

# Manuale per il Titolare di Fonte Autentica  

### Guida operativa per la messa a disposizione dei dati per l’emissione di Attestati Elettronici di Attributi sulle soluzioni IT-Wallet 


## Indice dei contenuti 

* [Introduzione e contesto](#Introduzione-e-contesto)
* [Scopo e ambito di applicazione](#Scopo-e-ambito-di-applicazione)
* [Ruoli e responsabilità del Titolare di Fonte Autentica](#Ruoli-e-responsabilità-del-Titolare-di-Fonte-Autentica)
* [Come diventare Titolare di Fonte Autentica](#Come-diventare-Titolare-di-Fonte-Autentica)
    * [Step 1 | Progettazione EAA](#step-1--progettazione-eaa) 
    * [Step 2 | Pubblicazione in collaudo](#step-2--pubblicazione-in-collaudo) 
    * [Step 3 | Test in collaudo](#step-3--Test-in-collaudo)
    * [Step 4 | Pubblicazione in produzione](#step-4--Pubblicazione-in-produzione) 
    * [Step 5 | Test in produzione](#step-5--Test-in-produzione)
    * [Step 6 | Pianificazione rilascio EAA](#step-6--Pianificazione-rilascio-eaa)
    * [Step 7 | Manutenzione e assistenza](#step-7--Manutenzione-e-assistenza)
* [Documenti da compilare](#Documenti-da-compilare)
* [Template PDND Data Model](#Template-PDND-Data-Model)
* [Riferimenti utili](#Riferimenti-utili)
* [Come contribuire](#Come-contribuire)
 

## Introduzione e contesto 

Il presente manuale rappresenta una **guida per gli Enti pubblici e privati che sono interessati a svolgere il ruolo di Titolari di Fonte Autentica nel Sistema IT-Wallet** e a **esporre dati per l’emissione di Attestati Elettronici di Attributi (Electronic Attestation of Attributes - EAA) nelle soluzioni IT-Wallet**, tra cui l’IT-Wallet pubblico reso disponibile da PagoPA S.p.A. all’interno di app IO, l’app dei servizi pubblici. 

Il Sistema di portafoglio digitale italiano (Sistema IT-Wallet) è stato istituito con la pubblicazione del decreto-legge 2 marzo 2024, n. 19 convertito, con modificazioni, dalla L. 29 aprile 2024, n. 56 ed in particolare, con l’art. 20, comma 1, lettera e), che ha introdotto l’[art. 64-quater del Codice dell’Amministrazione Digitale (CAD)](https://www.normattiva.it/eli/id/2005/05/16/005G0104/CONSOLIDATED/20250429). 

La novità normativa si inquadra nella più ampia iniziativa europea introdotta dal [Regolamento (UE) 2024/1183 del Parlamento europeo e del Consiglio dell’11 aprile 2024](http://data.europa.eu/eli/reg/2024/1183/oj) – c.d. eIDAS 2 – che modifica il [Regolamento (UE) n. 910/2014](https://eur-lex.europa.eu/eli/reg/2014/910/oj) per quanto riguarda l’istituzione del quadro europeo relativo all’identità digitale.  

Per la piena attuazione del Sistema IT-Wallet, all’articolo istitutivo del CAD seguono due decreti attuativi, di cui uno di adozione delle Linee Guida proposte da AgID, che vengono completate dalle Specifiche tecniche. La versione di riferimento di tali specifiche è la **[versione 1.4.0](https://https://italia.github.io/eid-wallet-it-docs/releases/1.4.0/it/)** ([versione inglese](https://italia.github.io/eid-wallet-it-docs/versione-corrente/en/)), e le sue successive release correttive e compatibili (1.4.x).



## Scopo e ambito di applicazione 

Questo manuale, che sovrascrive e supera i manuali in formato .pdf precedentemente condivisi, ha lo scopo di: 

* fornire indicazioni sul processo per la messa disposizione dei dati per la creazione di Attestati Elettronici di Attributi; 
* fornire riferimenti, risorse e strumenti pratici a supporto delle azioni richieste agli Enti nel corso di tale processo; 
* facilitare l’aderenza alle Specifiche Tecniche e alla normativa vigente. 

Il presente manuale è da intendersi anche come uno strumento aperto alla condivisione e alla collaborazione tra gli Enti interessati. 

## Ruoli e responsabilità del Titolare di Fonte Autentica 

Il Titolare di Fonte Autentica (Authentic Source - AS) è il soggetto che, nel Sistema IT-Wallet, detiene i dati da cui vengono creati gli Attestati Elettronici di Attributi rilasciati nelle soluzioni IT-Wallet. Ad esempio, per la Patente di Guida il Titolare di Fonte Autentica è la Direzione Generale di Motorizzazione del Ministero delle Infrastrutture e dei Trasporti. 


L'Ente che fornisce i dati, in quanto Titolare di Fonte Autentica, è l’unico soggetto che può definire mezzi e finalità di uso degli stessi. L'Ente rimarrà sempre il "proprietario" del dato e sarà responsabile del ciclo di vita del dato quindi di eventuali modifiche o cambiamenti di stato. Il Sistema IT-Wallet è concepito in modo che l'Ente possa continuare a gestire il dato in modo autonomo e conforme alle proprie politiche e alle normative vigenti. 

 

Di seguito rappresentato il ruolo del Titolare di Fonte Autentica e delle altre entità nel Sistema IT-Wallet. 


![Figura 1](https://github.com/user-attachments/assets/e23b1cd0-b547-408e-8354-58131e0977b4)



Figura 1: Ruolo del Titolare di Fonte Autentica nel Sistema IT-Wallet

> *NB: Nel Sistema IT-Wallet IPZS (Istituto Poligrafico e Zecca dello Stato) è l’unico Fornitore di Attestati Elettronici di Attributi di Interesse Pubblico, coerentemente con la normativa.  

> **NB: Nel Sistema IT-Wallet PagoPA S.p.A. è l’unico fornitore di soluzione pubblica di IT-Wallet, ospitata all’interno dell’app IO, l’app dei servizi pubblici per la PA.  

 
Di seguito il ruolo del Titolare di Fonte Autentica nel contesto del flusso di richiesta ed emissione di un EAA. 

![Figura 2](https://github.com/user-attachments/assets/9223e9fa-9830-4e1d-b1ac-6354554ef2ce)

Figura 2: Flusso di richiesta ed emissione di un EAA nel Sistema IT-Wallet 
 
> *NB: Nel Sistema IT-Wallet IPZS (Istituto Poligrafico e Zecca dello Stato) è l’unico Fornitore di Attestati Elettronici di Attributi di Interesse Pubblico, coerentemente con la normativa.

> **NB: Nel Sistema IT-Wallet PagoPA S.p.A. è l’unico fornitore di soluzione pubblica di IT-Wallet, ospitata all’interno dell’app IO, l’app dei servizi pubblici per la PA.  



## Come diventare Titolare di Fonte Autentica 

Per assumere il ruolo di Titolare di Fonte Autentica, e quindi mettere a disposizione i propri dati per la creazione di Attestati Elettronici di Attributi per gli utenti che ne fanno richiesta, ciascun Ente interessato deve attenersi al seguente processo di onboarding tecnico, da considerarsi valido fino alla pubblicazione del Regolamento IT-Wallet e alla disponibilità del Portale di Onboarding, del Registro delle Fonti Autentiche e del Catalogo degli Attestati Elettronici. In particolare, il processo prevede i seguenti step: 


* **Step 1 | Progettazione EAA**: l’Ente approfondisce le Specifiche Tecniche del Sistema IT-Wallet ([versione 1.4.0](https://italia.github.io/eid-wallet-it-docs/versione-corrente/it/index.html)) e definisce le caratteristiche del proprio Attestato Elettronico di Attributi, ovvero le modalità di scoperta e ottenimento dell’EAA, i casi d’uso, il data model e le modalità di gestione di errori e stati, al fine di garantire una corretta emissione, utilizzo e gestione dell’EAA nel tempo. [Vai allo Step 1](#Step-1--Progettazione-EAA)

* **Step 2 | Pubblicazione in collaudo**: l'Ente effettua l’onboarding nella Piattaforma Digitale Nazionale Dati (PDND), se non lo ha già fatto, rilascia l’e-service in ambiente di collaudo su PDND, e attiva il relativo servizio Signal Hub in ambiente di collaudo per la gestione del ciclo di vita dell’EAA nel tempo. Infine, l’Ente notifica al Fornitore di Attestati Elettronici di Attributi, configurato come fruitore dell’e-service, l'avvenuta pubblicazione. [Vai allo Step 2](#Step-2--Pubblicazione-in-collaudo)

* **Step 3 | Test in collaudo**: l'Ente, in ambiente di collaudo PDND, esegue i test di integrazione e di gestione del ciclo di vita dell'EAA con il Fornitore di Attestati Elettronici di Attributi indicato come fruitore dell’e-service e, se ritenuto necessario, con il Fornitore di Wallet per verificare anche gli aspetti relativi alla UX/UI dell’EAA. [Vai allo Step 3](#Step-3--Test-in-collaudo)

* **Step 4 | Pubblicazione in produzione**: l'Ente rilascia l’e-service in ambiente di produzione su PDND e attiva il relativo servizio Signal Hub in ambiente di produzione per la gestione del ciclo di vita dell’EAA nel tempo. Infine, l’Ente notifica al Fornitore di Attestati Elettronici di Attributi, configurato come fruitore dell’e-service, l'avvenuta pubblicazione. [Vai allo Step 4](#Step-4--Pubblicazione-in-produzione) 

* **Step 5 | Test in produzione**: l’Ente, in ambiente di produzione, esegue i test di integrazione, di carico, di long run e di gestione del ciclo dell’EAA con il Fornitore di Attestati Elettronici di Attributi e, se possibile, con il Fornitore di Wallet per testare anche gli aspetti relativi alla UX/UI. [Vai allo Step 5](#Step-5--Test-in-produzione)  

* **Step 6 | Pianificazione rilascio dell’EAA**: a valle del buon esito dei test in collaudo e in produzione, l’Ente concorda con il Fornitore di Attestati Elettronici di Attributi e il Fornitore di Wallet la data di rilascio dell’EAA, quindi la possibilità di ottenimento dell’EAA da parte degli utenti. Inoltre, l’Ente può valutare attività di comunicazione, in sinergia con gli altri attori interessati. [Vai allo Step 6](#Step-6--Pianificazione-rilascio-dell-EAA)

* **Step 7 | Manutenzione e assistenza**: l’Ente effettua eventuali attività di gestione e manutenzione dell’e-service e contribuisce alla risoluzione di problematiche e segnalazioni, per le tematiche e i processi di competenza, secondo il modello di assistenza del Sistema IT-Wallet. [Vai allo Step 7](#Step-7--Manutenzione-e-assistenza) 


## Step 1 | Progettazione EAA

Questo step ha l’obiettivo di definire l'esperienza utente di scoperta, ottenimento, utilizzo e gestione dell’Attestato Elettronico di Attributi. Le attività previste in questa fase sono di piena responsabilità dell’Ente e determinano l’aspetto grafico, e più in generale la qualità del servizio, per l’utente finale (es. numerosità e valore aggiunto dei casi d’uso, facilità di lettura e comprensione degli attributi, l’efficacia dell’assistenza, le condizioni di validità dell’EAA, etc.). In questo step, l’Ente interessato deve: 


### **Approfondire le Specifiche Tecniche del Sistema IT-Wallet**
Le Specifiche Tecniche di riferimento sono rappresentate dalla [versione 1.4.0](https://italia.github.io/eid-wallet-it-docs/versione-corrente/it/). Si raccomanda l’approfondimento, in particolare, delle sezioni: 

* [Design dell’Esperienza Utente ](https://italia.github.io/eid-wallet-it-docs/versione-corrente/it/functionalities.html)
* [Fonti Autentiche](https://italia.github.io/eid-wallet-it-docs/versione-corrente/it/authentic-sources.html)  
* [Endpoint delle Fonti Autentiche](https://italia.github.io/eid-wallet-it-docs/versione-corrente/it/authentic-source-endpoint.html#:~:text=20.%20Appendice-,13.4.%20Endpoint%20delle%20Fonti%20Autentiche,-%C2%B6) 
* [Algoritmi Crittografici](https://italia.github.io/eid-wallet-it-docs/versione-corrente/it/algorithms.html#:~:text=20.%20Appendice-,14.%20Algoritmi%20Crittografici,%C2%B6,-I%20seguenti%20algoritmi) 
* [e-Service PDND](https://italia.github.io/eid-wallet-it-docs/versione-corrente/it/e-service-pdnd.html#:~:text=di%20Wallet%20PDND-,20.2.%20e%2DService%20PDND,%C2%B6,-Il%20framework%20EIDAS) 
* [Soluzione del Fornitore di Attestati Elettronici](https://italia.github.io/eid-wallet-it-docs/versione-corrente/it/credential-issuer-solution.html#:~:text=20.%20Appendice-,10.2.%20Soluzione%20del%20Fornitore%20di%20Attestati%20Elettronici,-%C2%B6)
* [Gestione degli Attestati Elettronici](https://italia.github.io/eid-wallet-it-docs/versione-corrente/it/digital-credential-management.html#:~:text=20.%20Appendice-,11.%20Gestione%20degli%20Attestati%20Elettronici,-%C2%B6)

### **Definire i momenti di discovery dell’EAA**
Il Sistema IT-Wallet rende possibili diverse modalità per scoprire, richiedere e ottenere un EAA tra quelli disponibili. In particolare: 

* l'utente può avviare il flusso di ottenimento: 
    * **attraverso una sezione “catalogo” della soluzione IT-Wallet**, soluzione indicata per EAA di interesse nazionale o, comunque, rivolti ad un’ampia percentuale di popolazione (es. Tessera Sanitaria, Patente di guida, etc.). Per approfondimenti vai alle Specifiche Tecniche, sezioni [Ottenimento dal Catalogo dell'Istanza del Wallet](https://italia.github.io/eid-wallet-it-docs/versione-corrente/it/functionalities.html#ottenimento-dal-catalogo-dell-istanza-del-wallet) e [Issuance Flow](https://italia.github.io/eid-wallet-it-docs/versione-corrente/it/credential-issuance-low-level.html#issuance-flow);
    * **attraverso uno dei touchpoint del Titolare di Fonte Autentica** (es. sito web), soluzione indicata per EAA di interesse locale o rivolte a un pubblico specifico (es. certificati, prenotazioni, etc.). Questo flusso può affiancarsi o sostituire il precedente a seconda del tipo di EAA. Per approfondimento vai alle Specifiche Tecniche, sezione [Ottenimento dal Touchpoint della Fonte Auntentica](https://italia.github.io/eid-wallet-it-docs/versione-corrente/it/functionalities.html#ottenimento-dal-touchpoint-della-fonte-autentica) e [Credential Offer](https://italia.github.io/eid-wallet-it-docs/versione-corrente/it/credential-issuance-low-level.html#flusso-credential-offer);
* l’Ente può rispondere alla richiesta di emissione in: 
    * **modalità sincrona**, che consente l’ottenimento immediato dell’EAA da parte dell’utente e si configura come l’opzione preferibile;
    * **modalità differita**, che consente all’utente di ottenere l'EAA non contestualmente al momento della richiesta e si configura come l’opzione non preferibile. 

È necessario quindi che l’Ente definisca a monte le modalità di scoperta dell’EAA che intende mettere a disposizione attraverso il Sistema IT-Wallet, sulla base di determinati parametri: a chi si rivolge l’EAA (a tutta la popolazione o solo a una nicchia di persone?); cosa deve fare l’utente per ottenere l’EAA (è necessario essere in possesso di specifici prerequisiti? deve effettuare un processo di richiesta/ adesione/ pagamento? etc.), tramite quali canali potrà richiedere l'EAA e quando potrà ottenerlo (contestualmente o non contestualmente alla richiesta).  

### **Definire i casi d'uso di utilizzo dell’EAA**
IT-Wallet consente all'utente di utilizzare i propri EAA: 

* **da remoto**(online), tramite flussi **cross-device**, cioè utilizzando due diversi device, tramite l’inquadramento di un QR code esposto dal Verificatore su loro property (es. sito) o in flussi **same-device**, cioè utilizzando solo lo smartphone, tramite appositi bottoni dedicati esposti dal Verificatore su loro property (es. sito o app). Per approfondimenti vai alle Specifiche Tecniche, sezione [Presentazione da remoto](https://italia.github.io/eid-wallet-it-docs/versione-corrente/it/functionalities.html#presentazione-da-remoto) e [Flusso remoto](https://italia.github.io/eid-wallet-it-docs/versione-corrente/it/remote-flow.html);
* **in prossimità** (in presenza), tramite flussi **supervisionati**, ovvero mostrando un QR code che il Verificatore potrà verificare tramite apposita app di verifica o **non supervisionati**, ovvero tramite strumenti di verifica automatica (tornelli, totem, etc.) con l’utilizzo di tecnologie sicure come il Bluetooth o NFC. er approfondimenti vai alle Specifiche Tecniche, sezione [Presentazione in prossimità](https://italia.github.io/eid-wallet-it-docs/versione-corrente/it/functionalities.html#presentazione-in-prossimita:~:text=Presentazione%20in%20prossimit%C3%A0-,%C2%B6,-La%20presentazione%20in) e [Flusso di prossimità](https://italia.github.io/eid-wallet-it-docs/versione-corrente/it/proximity-flow.html). 

La definizione dei casi d'uso è fondamentale per: 

* **progettare un'esperienza d'uso che apporti valore reale** sia a cittadini che ai verificatori, è utile definire a monte quali potranno essere le occasioni d’uso del futuro Attestato Elettronico di Attributi, a partire dall’analisi dell’esperienza attuale di fruizione del corrispettivo documento fisico, se esistente (es. si pensi alla modalità di presentazione del codice a barre per l'uso della Tessera Sanitaria o del QR code per la verifica della Carta Europea della Disabilità); 
* **determinare il tipo di formato con cui verrà emessa la EAA** da parte del Fornitore di Attestati Elettronici di Attributi (SD-JWT-VC per scenari in remoto e mdoc-CBOR per scenari in prossimità).

A tal fine, l’Ente deve compilare il documento [**Casi d’uso EAA.docx**](Casi-d-uso-EAA.docx), seguendo le istruzioni riportate al suo interno. 

### **Definire il Data Model dell’EAA**

IT-Wallet consente all’utente di ottenere in formato digitale i propri documenti, titoli e certificati sotto forma di EAA. Ciascun EAA consta di un elenco strutturato di dati.  
L’Ente deve definire quali dati caratterizzeranno i propri EAA e in quale ordine, affinché siano adeguati all’utilizzo in versione digitale e subito comprensibili all’utente. 
 

A tal fine, l'Ente deve compilare il foglio **01- Data Model** del documento [**e-service EAA.xlsx**](e-service-EAA.xlsx) dell’Attestato Elettronico di Attributi, seguendo le istruzioni riportate al suo interno, dichiarando i dettagli sui dati che verranno messi a disposizione (es. tipologia, obbligatorietà, formato, lunghezza massima consentita, ordinamento, etc.).  
Nella sezione [Template PDND Data Model](#Template-PDND-Data-Model) sono riportati i riferimenti dei template Data Model pubblicati su PDND relativi ad alcune tipologie di Attestati Elettronici di Attributi, che l’Ente dovrebbe prendere a riferimento per assicurare massima aderenza e compliance alle Specifiche Tecniche.

In conclusione, un’adeguata definizione del Data Model pone le basi per una corretta implementazione dell’e-service da pubblicare su PDND (vedi [Step 2](#Step-2-|-Pubblicazione-in-collaudo)) ma è altresì importante considerare e rispettare i seguenti requisiti tecnici: 

* **Identificativo utente**: Qualora fosse necessario identificare l’utente, il Codice Fiscale (CF) rappresenta l’identificativo univoco da utilizzare per le chiamate all‘e-service; 
* **Completezza base di dati**: Ogni e-service pubblicato su PDND dovrà esporre un set di dati completo nel contenuto e negli attributi. È ammessa la pubblicazione di basi dati parziali relative a periodi temporali limitati. 

### **Definire le casistiche di errore** 
La fase di emissione dell’EAA nell’IT-Wallet deve prevedere e gestire specifiche situazioni di errore. 

A tal fine, l'Ente deve prendere visione e compilare il foglio **02 - Mappatura degli errori** del documento [**e-service EAA.xlsx**](e-service-EAA.xlsx) per l’implementazione tecnica, seguendo le istruzioni riportate al suo interno. La mappatura descrive le risposte che il servizio messo a disposizione dovrà obbligatoriamente gestire per garantire una **corretta informazione all'utente in caso di errori**. 

### **Definire la gestione degli stati del ciclo vita dell’EAA** 

IT-Wallet supporta dei meccanismi per l’aggiornamento dello stato e la gestione del ciclo di vita dell’EAA.  
Si precisa che, pur essendo strettamente correlato, **il ciclo di vita dell’EAA non è completamente sovrapponibile a quello della versione fisica**. In particolare: 

* Se il documento fisico viene invalidato dal Titolare di Fonte Autentica, l’EAA viene anch'essa invalidata;  
* Se l’EAA viene invalidato o rimosso dal portafoglio da parte dell’utente, questo non si ripercuote sul corrispettivo eventuale documento fisico.  Per ragioni di sicurezza, l’EAA ha in generale una **durata massima di un anno** (vedi sotto approfondimento su scadenza tecnica), ma in casi d’uso specifici tale durata potrebbe essere ulteriormente ridotta e solo in casi specifici questo ha ricadute sulla validità del corrispettivo documento fisico (come, ad esempio, per attestati che vengono utilizzati una sola volta ad esempio biglietti del treno, cinema, ecc). Trascorso l'anno, l’utente dovrà richiedere nuovamente l’EAA. 

Gli stati ammissibili per un Attestato Elettronico di Attributi sono i seguenti: 

* **Valido**: EAA emesso, nessun segnale di modifica su uno dei suoi attributi o sul suo stato, entro la data di scadenza. L’utente può utilizzarlo in ogni scenario d’uso;
* **Sospeso**: EAA temporaneamente non valido, in uno stato di reversibilità. L’utente deve aspettare che lo stato torni ad essere valido (es. Patente ritirata);
* **Non Valido**: EAA non più valido, in uno stato di irreversibilità. L’utente può solo eliminarlo e/o richiedere l’emissione di nuovo EAA che sovrascriva il precedente (es. Patente annullata).

Oltre agli stati sopra elencati, è bene specificare che lo stato di un Attestato Elettronico può essere influenzato anche dalla **scadenza amministrativa** e/o dalla **scadenza tecnica**. Rispettivamente l’EAA può, quindi, assumere anche i seguenti stati: 

* **Scaduto**: EAA con data di scadenza amministrativa superata. La scadenza amministrativa può essere definita dal Titolare di Fonte Autentica e, se ritenuta utile o necessaria, deve essere inclusa come attributo all’interno del data model dell’EAA per garantire messaggi informativi all’interno della soluzione IT-Wallet (es. La tua Patente scade tra 30 giorni);
* **Da aggiornare**: EAA con data di scadenza tecnica superata. La scadenza tecnica è definita del Fornitore di Attestati Elettronici di Attributi ed è impostata generalmente a 1 anno o comunque a un valore inferiore o uguale alla data di scadenza amministrativa. Tale scadenza ha l’obiettivo di richiedere un’azione di riemissione esplicita all’utente e mitigare rischi di sicurezza. 

Per approfondimenti vai alle Specifiche Tecniche, sezione [Ciclo di Vita degli Attestati Elettronici](https://italia.github.io/eid-wallet-it-docs/versione-corrente/it/credential-revocation.html). 

A tal fine, l’Ente deve compilare il foglio **03 - Stati** del documento [**e-service EAA.xlsx**](e-service-EAA.xlsx), e seguire le istruzioni riportate al suo interno per definire i dettagli sugli stati relativi al ciclo di vita dell’EAA, ovvero dichiarare la condizione di applicabilità dei tre stati sopracitati e l’eventuale relativo messaggio informativo da esporre all’utente.

*Nota: 
Per ottimizzare l’esperienza d’uso dell’IT-Wallet pubblico, il Titolare di Fonte Autentica può anche valutare l’**integrazione con app IO per l'invio di messaggi informativi al cittadino**, quali ad esempio: comunicare il cambio di stato del documento (come, ad esempio, un reminder sulla scadenza), informarlo che il nuovo documento è pronto per essere ritirato o novità legate ai servizi offerti (opzionale ma consigliato).* 

### **Definire i contenuti per l’informazione e l’assistenza all’utente**  
L’Ente deve contribuire al [modello di assistenza](https://italia.github.io/eid-wallet-it-docs/versione-corrente/it/functionalities.html#assistenza-utente) del Sistema IT-Wallet rendendo disponibili contenuti utili alla predisposizione di nuove Domande Frequenti e/o testi informativi in app, e fornendo i recapiti necessari per la gestione dell’assistenza agli utenti.  
A tal fine, l’Ente deve compilare il documento [**Assistenza EAA.docx**](Assistenza-EAA.docx). 

 

### **Definire le caratteristiche grafiche dell’EAA** 
La rappresentazione grafica di un EAA nell’IT-Wallet può dipendere, per specifici aspetti, da parametri definiti delle Specifiche Tecniche, sezione [Focus sugli Attestati Elettronici di Attributi](https://italia.github.io/eid-wallet-it-docs/versione-corrente/it/functionalities.html#focus-sugli-attestati-elettronici-di-attributi). 
L’Ente interessato a personalizzare il proprio EAA, deve trasmettere i propri materiali come documentazione allegata all’e-service su PDND.  


## Step 2 | Pubblicazione in collaudo 

Questo step ha l’obiettivo di rilasciare in collaudo su PDND l’e-service dell’EAA di interesse e di attivare il relativo servizio Signal Hub per la gestione dei dati nel tempo. Inoltre, l’Ente può rilasciare in collaudo il Credential Offer se ritenuto utile per il proprio EAA. A tale scopo, l’Ente deve: 
 
### **Aderire alla Piattaforma Digitale Nazionale Dati (PDND)**
Per effettuare l’onboarding alla PDND, qualora l’Ente ancora non abbia aderito, consultare la [Guida all'adesione](https://docs.pagopa.it/interoperabilita-1/manuale-operativo/guida-alladesione). 

### **Pubblicare l’e-service su PDND in collaudo** 
L’Ente deve sviluppare e rilasciare in collaudo un e-service coerente con il Data Model precedentemente definito, in linea con le informazioni presenti nella Guida all’adesione di PDND, con particolare riferimento alla [sezione e-service](https://docs.pagopa.it/interoperabilita-1/manuale-operativo/e-service), e in linea con le Specifiche Tecniche italiane, in particolare la sezione dedicata al [Titolare di Fonte Autentica](https://italia.github.io/eid-wallet-it-docs/versione-corrente/it/authentic-sources.html). 

Contestualmente al flusso di pubblicazione dell’e-service, l’Ente deve allegare il documento **[Casi d’uso EAA.docx]**(Casi-d-uso-EAA.docx), il documento [**e-service EAA.xlsx**](e-service-EAA.xlsx) e il documento [**Assistenza EAA.docx**](Assistenza-EAA.docx), precedentemente compilati in ogni loro foglio. 
Nel caso di EAA di interesse pubblico, l’Ente deve abilitare IPZS alla fruizione dell’e-service, se possibile con abilitazione automatica. 

Si consiglia di nominare l’e-service in “Creazione EAA [Nome / Nome tipologia EAA] – IT-Wallet” (es. “Creazione EAA Patente di guida – IT-Wallet” oppure “Creazione EAA Titoli di studio – IT-Wallet") e di predisporre una descrizione in linea con la [Guida alla nomenclatura degli e-service PDND](https://italia.github.io/pdnd-guida-nomenclatura-eservice/index.html)referenziata nella Guida all’adesione PDND. 

### **Attivare il servizio Signal Hub in collaudo** 
L’Ente deve attivare in collaudo il servizio [Signal Hub](https://developer.pagopa.it/pdnd-interoperabilita/guides/manuale-operativo-pdnd-interoperabilita/v1.0/riferimenti-tecnici/signal-hub) di PDND per il relativo e-service, in coerenza con quanto definito dalle [Specifiche Tecniche](https://italia.github.io/eid-wallet-it-docs/versione-corrente/it/signal-hub-endpoint.html) per la gestione degli stati, precedentemente mappati all’interno del foglio **03 - Stati** del documento [**e-service EAA.xlsx**](e-service-EAA.xlsx). 
 
### **Sviluppare il Credential Offer (opzionale)** 
L’Ente, se ritenuto necessario e/o utile per ingaggiare l’utente nel flusso di ottenimento dell’EAA, deve provvedere in questo step agli sviluppi e all’integrazione del Credential Offer all’interno delle proprie soluzioni.  
 
### **Notificare l’avvenuto rilascio in collaudo** 
L’Ente deve notificare il Fornitore di Attestati di Attributi circa l’avvenuto rilascio dell’e-service in collaudo su PDND, dei servizi di Signal Hub in produzione e, se previsto, del Credential Offer. In caso di EAA di interesse pubblico, l’Ente deve notificare IPZS inviando una mail all'indirizzo XX e, in caso di EAA disponibile nella soluzione pubblica di IT-Wallet, l’Ente deve notificare PagoPA inviando una mail all’indirizzo XX.

## Step 3 | Test in collaudo 

Questo step, suggerito ma non vincolante per le fasi successive, ha l’obiettivo di eseguire i test propedeutici al rilascio in produzione. In caso di disponibilità da parte del Fornitore di Attestati Elettronici di Attributi, l’Ente può: 

### **Eseguire i test in collaudo** 
L’Ente **può** testare in collaudo la corretta erogazione dei dati tramite l’e-service in PDND, la corretta fruizione del servizio Signal Hub di PDND per la gestione del ciclo di vita dell’EAA e, se previsto, il Credential Offer con il Fornitore di Attestati Elettronici di Attributi (e.g. IPZS, nel caso di Attestati Elettronici di interesse pubblico).  

Infine, se ritenuto necessario, l’Ente può verificare la resa grafica dell’EAA di interesse con il Fornitore di Wallet (e.g. PagoPA, nel caso di soluzione pubblica di IT-Wallet).

Una volta superati i test in collaudo, se eseguiti, l’Ente può proseguire con la fase successiva.
 
## Step 4 | Pubblicazione in produzione 

Questo step ha l’obiettivo di rilasciare in produzione l’e-service dell'EAA di interesse e di attivare relativo il servizio Signal Hub per la gestione dei dati nel tempo. Inoltre, l’Ente può rilasciare in produzione il Credential Offer se ritenuto utile per il proprio EAA. A tale scopo, l’Ente deve: 

### **Pubblicare l’e-service su PDND in produzione** 
L’Ente deve rilasciare l’e-service su PDND in produzione. Nel caso di EAA di interesse pubblico, l’Ente deve abilitare IPZS alla fruizione del servizio, se possibile con abilitazione automatica. 

### **Attivare il servizio Signal Hub in produzione** 
L’Ente deve attivare in produzione il servizio Signal Hub di PDND per il relativo e-service, in coerenza con quanto definito dalle [Specifiche Tecniche](https://italia.github.io/eid-wallet-it-docs/versione-corrente/it/signal-hub-endpoint.html) per la gestione degli stati, precedentemente mappati all’interno del foglio **03 - Stati** del documento [**e-service EAA.xlsx**](e-service-EAA.xlsx). 

### **Portare in produzione il Credential Offer (opzionale)** 
L’Ente, se precedentemente sviluppato in collaudo, deve provvedere in questo step al rilascio in produzione del Credential Offer all’interno delle proprie soluzioni.  

### **Notificare l’avvenuto rilascio in produzione** 
L’Ente deve notificare il Fornitore di Attestati di Attributi circa l’avvenuto rilascio dell’e-service in produzione su PDND, dei servizi di Signal Hub in produzione e, se previsto, del Credential Offer. In caso di EAA di interesse pubblico, l’Ente deve notificare IPZS inviando una mail all'indirizzo XX e, in caso di EAA disponibile nella soluzione pubblica di IT-Wallet, l’Ente deve notificare PagoPA inviando una mail all’indirizzo XX. 
 
 
## Step 5 | Test in produzione 

Questo step ha l’obiettivo di eseguire i test necessari a un adeguato funzionamento di quanto rilasciato in produzione. A tale scopo, l’Ente deve: 

### **Effettuare i test in produzione** 
L’Ente deve eseguire i test di tutte le componenti sviluppate, prevedendo anche i test di carico per la corretta gestione di eventuali picchi di richieste di emissione e gestione dell’EAA sui Wallet (si consiglia di effettuare il test un mese prima del go-live). In particolare, il servizio esposto per il recupero dei dati della EAA dovrà supportare 300 richieste al secondo per almeno 60 minuti, con tempi di risposta inferiori a 500 millisecondi.  

Inoltre, deve essere eseguito anche un test di “long run” di 150 richieste al secondo per almeno 12 ore consecutive con tempi di risposta inferiori a 500 millisecondi.  

Una volta superati i test in produzione, l’Ente può proseguire con la fase successiva. 

## Step 6 | Pianificazione rilascio EAA 

Questo step ha l’obiettivo di pianificare e gestire le attività di rilascio e promozione dell’EAA agli utenti. A tale scopo, l’Ente deve: 

### **Pianificare il go-live** 
A valle del buon esito dei test in collaudo e in produzione, l’Ente concorda con il Fornitore di Attestati Elettronici di Attributi e il Fornitore di Wallet la data di rilascio dell’EAA, quindi la possibilità di ottenimento dell’EAA da parte degli utenti. L’Ente dovrà in ogni caso effettuare la registrazione amministrativa, non appena disponibile, secondo quanto definito dal Regolamento IT-Wallet.

### **Valutare attività di comunicazione**  
L'Ente può prevedere attività di comunicazione finalizzata ad informare gli utenti della possibilità di ottenere e utilizzare il nuovo EAA all'interno di IT-Wallet. Per approfondimento, vai alle Specifiche Tecniche, sezione [Brand Identity](https://italia.github.io/eid-wallet-it-docs/versione-corrente/it/brand-identity.html) del Sistema IT-Wallet. 

## Step 7 | Manutenzione e assistenza  

Una volta reso disponibile l’EAA agli utenti finali, l’Ente Titolare di Fonte Autentica deve mantenere l’e-service e mantenere un ruolo attivo sia nella gestione del ciclo di vita dell’EAA che nell’assistenza agli utenti, per le tematiche o i processi di pertinenza. In particolare, l’Ente deve: 

### **Garantire la gestione e manutenzione dell’e-service** 
L’Ente deve garantire il corretto funzionamento dell’e-service nel tempo, programmare adeguate azioni di monitoraggio e aggiornamento se richieste, ad esempio, da cambiamenti normativi o procedurali (es. nuovi dati, stati, casistiche di errore, etc.). 

### **Gestire problematiche e fornire assistenza agli utenti** 
L’Ente deve garantire un costante aggiornamento delle informazioni riportate nel documento [**Assistenza EAA.docx**](Assistenza-EAA.docx), al fine di: 

* **Contribuire alla risoluzione di bug** 
Il referente dell’ambito sistemistico e il referente dell’ambito applicativo, così come definito dall’Ente nel documento [**Assistenza EAA.docx**](Assistenza-EAA.docx), devono contribuire alla diagnosi congiunta delle segnalazioni ricevute da Fornitore di Attestati Elettronici di Attributi (IPZS, nel caso di EAA di interesse pubblico) e Fornitori di Wallet (PagoPA, nel caso della soluzione pubblica IT-Wallet) e relativa risoluzione, secondo quanto definito dal modello di assistenza del Sistema IT-Wallet. 
* **Garantire il supporto agli utenti** 
Il referente per l’ambito assistenza ed almeno un canale di contatto dedicato agli utenti finali (es. indirizzo e-mail, numero telefonico, etc.), così come definito dall’Ente nel documento [**Assistenza EAA.docx**](Assistenza-EAA.docx), devono sempre essere disponibili per gestire eventuali problemi relativi all’EAA, come ad esempio la segnalazione di dati errati o di errori nella fase di ottenimento dell’EAA da parte dell’utente. 

## Documenti da compilare 

Di seguito l'elenco dei documenti da scaricare, compilare e condividere secondo le modalità definite durante lo [Step 1](#Step-1-|-Progettazione-EAA) e [Step 2](#Step-2-|-Pubblicazione-in-collaudo):

* [Casi d’uso EAA.docx](Casi-d-uso-EAA.docx)  
* [e-service EAA.xlsx](e-service-EAA.xlsx) 
* [Assistenza EAA.docx](Assistenza-EAA.docx)

## Template PDND Data Model 

Di seguito si condividono i data model di EAA già definiti o contenuti nella soluzione pubblica IT-Wallet, che l’Ente dovrebbe prendere a riferimento, qualora intenda rendere disponibili dati di EAA appartenenti alle stesse categorie semantico-funzionali. In particolare: 

* EAA di affiliazione ad un ente o organizzazione 
* EAA di patenti o patentini 
* EAA di titoli o qualifiche 
* EAA di iscrizioni o frequenze 


## Riferimenti utili 

* Specifiche Tecniche IT-Wallet, versione 1.4.0 e successive release correttive e compatibili: [italiano](https://italia.github.io/eid-wallet-it-docs/versione-corrente/it/index.html), [inglese](https://italia.github.io/eid-wallet-it-docs/versione-corrente/en/index.html) 
* [Guida all’adesione PDND](https://docs.pagopa.it/interoperabilita-1/manuale-operativo/guida-alladesione) 


## Come contribuire 

Il manuale è da intendersi anche come uno strumento aperto alla condivisione e alla collaborazione tra gli Enti interessati.  

Nella sezione Discussion è possibile iniziare o partecipare a discussioni, aprire segnalazioni o inviare contributi a beneficio di alti Enti interessati ad assumere il ruolo di Titolari di Fonte Autentica. 

Si raccomanda di consultare il [Codice di condotta](https://github.com/italia/bootstrap-italia/blob/main/CODE_OF_CONDUCT.md) della community legata ai progetti dell'organizzazione Italia su GitHub, strumento utile a mantenere un ambiente di collaborazione inclusivo e propositivo.  
 

 

.. include:: ../common/common_definitions.rst

Progettazione dell'Esperienza dell'Utente
==========================================


.. include:: design.rst 


Panoramica delle Funzionalità
------------------------------

Il Sistema IT-Wallet fornisce agli Utenti un modo più semplice, veloce e sicuro per accedere ai servizi. Questo servizio viene erogato attraverso l'uso di una Soluzione Wallet, la cui Esperienza dell'Utente è strutturata in tre fasi principali: pre-uso, uso e post-uso.

.. only:: format_html

  .. figure:: ./images/svg/UX-phases-usage.svg
    :alt: Fasi dell'Esperienza dell'Utente nell'utilizzo del Wallet
    :width: 100%

    Fasi dell'Esperienza dell'Utente nell'utilizzo del Wallet

.. only:: format_latex

  .. figure:: ./images/pdf/UX-phases-usage.pdf
    :alt: Fasi dell'Esperienza dell'Utente nell'utilizzo del Wallet
    :width: 100%

    Fasi dell'Esperienza dell'Utente nell'utilizzo del Wallet

Le sezioni seguenti si concentrano sulle fasi di utilizzo e post-utilizzo. Definiscono i requisiti funzionali che supportano l'Esperienza dell'Utente per le fasi di attivazione, acquisizione, presentazione, gestione e disattivazione, insieme ai requisiti di interazione relativi alla gestione degli errori, alle richieste di assistenza e alla raccolta di feedback.

Documentazione aggiuntiva e risorse sono fornite nella sezione :ref:`official-resources:Risorse Ufficiali`.  

Le Official Resources includono raccomandazioni sulle interazioni richieste tra Utente e Istanza del Wallet e le migliori pratiche di progettazione che promuovono coerenza tra diverse Soluzioni Wallet in termini di come le funzionalità vengono accessibili e utilizzate.

Per garantire un'implementazione corretta e coerente, gli Attori Primari: 

- DEVONO utilizzare le Official Resources e DEVONO rispettare tutte le specifiche di utilizzo correlate fornite; 

- POSSONO scegliere tra le configurazioni disponibili fornite. Gli Attori Primari DEVONO garantire l'uso corretto dei componenti atomici, come gli Engagement Button; 

- DEVONO mantenere aggiornate le risorse utilizzate, in linea con l'ultima versione disponibile delle Official Resources. 

Attivazione dell'Istanza del Wallet
------------------------------------

L'attivazione consente all'Utente di accedere alle funzionalità della Soluzione Wallet per ottenere, presentare e gestire in modo sicuro i propri Attestati Elettronici. Il processo di attivazione coinvolge l'Autenticazione dell'Utente con l'Istanza del Wallet utilizzando la propria identità digitale, che consente la generazione del PID.

Di seguito sono riportati i requisiti dell'Esperienza dell'Utente che il Fornitore di Wallet DEVE garantire tramite la propria Soluzione Wallet:

- L'Utente scarica la Soluzione Wallet sul proprio dispositivo per generare la propria Istanza del Wallet;
- L'Utente imposta un PIN di sblocco per la propria Istanza del Wallet se non è stato precedentemente impostato nell'app. Oltre al PIN, l'Utente può decidere di utilizzare il proprio meccanismo di sblocco utilizzato all'interno del dispositivo e gestito a livello del sistema operativo (ad esempio, autenticazione biometrica) come alternativa al PIN. L'Utente utilizza il metodo di sblocco ogni volta che è richiesta un'autorizzazione per garantire sicurezza e proteggere le proprie informazioni;
- L'Utente esamina tutte le informazioni pertinenti riguardanti il processo di attivazione e l'utilizzo del servizio. Inoltre, l'Utente legge qualsiasi policy del Fornitore e del Fornitore di Attestati Elettronici di Dati di Identificazione Personale e/o i termini e le condizioni del servizio. L'Utente dà il proprio consenso per procedere o rifiuta per annullare l'operazione;
- L'Utente seleziona un'opzione di Autenticazione tra quelle disponibili;
- L'Utente completa il flusso di Autenticazione con il servizio del Gestore di Identità DIgitale;
- L'Utente riceve conferma dell'esito del processo di Autenticazione. Se ha successo, l'Utente visualizza un'anteprima del proprio PID. L'Utente conferma le informazioni visualizzate in anteprima per procedere con l'attivazione dell'Istanza del Wallet, o annulla l'operazione;
- L'Utente autorizza l'operazione utilizzando il metodo di sblocco precedentemente impostato;
- L'Utente riceve conferma dell'attivazione riuscita dell'Istanza del Wallet.

Il Fornitore di Wallet DEVE consentire all'Utente di rimuovere il PID rilasciato durante la fase di attivazione. Inoltre, il Fornitore di Attestati Elettronici di Dati di Identificazione Personale DOVREBBE consentire all'Utente di revocare il PID rilasciato attraverso un Touchpoint specifico. Il Fornitore di Wallet DEVE consentire all'Utente di avere sempre l'opzione di richiedere la disattivazione della propria Istanza del Wallet, anche in assenza del dispositivo su cui è stata installata. Per ulteriori dettagli, si prega di fare riferimento alle sezioni `Disattivazione dell'Istanza del Wallet`_ e `Gestione degli Attestati Elettronici`_.

In caso di errori nell'utilizzo dell'Istanza del Wallet, il Fornitore di Wallet DEVE garantire che l'Utente riceva messaggi coerenti che lo informino e lo guidino verso la risoluzione del problema. Per ulteriori dettagli, si prega di fare riferimento alla sezione :ref:`functionalities:Gestione degli Errori`.

Focus sul PID – Dati di Identificazione Personale
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Il PID (Dati di Identificazione Personale) si riferisce al set minimo verificato di informazioni sull'identità dell'Utente (vedere :ref:`credential-data-model:Modello di Dati degli Attestati Elettronici`) rilasciato come risultato del processo di attivazione e reso disponibile nell'Istanza del Wallet.
Di seguito sono riportati i requisiti per la visualizzazione e l'utilizzo del PID che ogni Fornitore di Wallet DEVE rispettare, al fine di fornire un'esperienza di consultazione e utilizzo coerente e accessibile: 

- Il PID DEVE essere visualizzato correttamente su tutti i dispositivi, garantendo un'esperienza coerente su schermi di dimensioni diverse; 
- Il PID DEVE essere denominato come definito dal Fornitore di Attestati Elettronici di Dati di Identificazione Personale;
- Il PID DEVE visualizzare il proprio stato se diverso da valido per fornire trasparenza sul suo ciclo di vita e PUÒ visualizzarlo se valido. Dettagli specifici sullo stato del PID, se non valido, POSSONO essere forniti (ad esempio, il motivo per cui il PID è revocato); 
- Il PID DEVE includere Pulsanti di Azione per abilitare la gestione del ciclo di vita e consentire all'Utente di revocare il PID, quindi l'intera Istanza del Wallet con tutti gli EAA rilasciati, o di aggiornare il PID in qualsiasi momento (vedere :ref:`functionalities:Gestione degli Attestati Elettronici`); 
- Il PID DEVE essere un elemento interattivo, per consentire all'Utente di essere autenticato da una Relying Party in un contesto digitale (vedere :ref:`functionalities:Autenticazione`), per accedere ai servizi in contesti di prossimità e per richiedere il rilascio di EAA aggiuntivi (vedere :ref:`functionalities:Rilascio di Attestati Elettronici di Attributi`);
- Il PID DEVE visualizzare un metodo di assistenza da parte del Fornitore di Attestati Elettronici di Dati di Identificazione Personale (vedere :ref:`functionalities:Assistenza all'Utente`); 
- Il PID DEVE essere riconoscibile dall'Utente e distinguibile da altri EAA; 
- Il PID DEVE essere denominato con la convenzione di denominazione che sarà definita nella versione futura di questo documento, evitando termini personalizzati o tecnici come "Dati di Identificazione Personale" o il suo acronimo "PID"; 
- La rappresentazione del PID DEVE aderire a un set definito di specifiche fornite dal Fornitore di Attestati Elettronici di Dati di Identificazione Personale per garantire riconoscibilità, coerenza e omogeneità tra diverse Soluzioni Wallet. 

Il Fornitore di Attestati Elettronici di Dati di Identificazione Personale DEVE: 

- Implementare un nome/convenzione di denominazione per riferirsi al PID, per garantire coerenza tra tutte le Soluzioni Wallet;
- Definire un set chiaro di specifiche per il PID per garantire identificazione e rappresentazione coerenti del PID tra diverse Soluzioni Wallet, in termini di formato, struttura e standard di aspetto (ad esempio colore, immagine di sfondo, ecc.). 

Rilascio di Attestati Elettronici di Attributi
-----------------------------------------------

Una volta completata l'attivazione, l'Utente PUÒ ottenere uno o più Attestati Elettronici di Attributi all'interno della propria Istanza del Wallet.

A seconda delle esigenze specifiche dell'Utente, del tipo di Attestato Elettronico di Attributi e delle offerte disponibili dal Fornitore di Wallet, dal Fornitore di Attestati Elettronici di Attributi e dalla Fonte Autentica, la richiesta di Attestati Elettronici di Attributi può avvenire in due modi:

- **dal Catalogo dell'Istanza del Wallet**: l'Utente esplora l'elenco degli Attestati Elettronici di Attributi forniti dalla Soluzione Wallet, seleziona quello di interesse e avvia il processo di richiesta, concludendo con il rilascio dell'Attestato Elettronico di Attributi nell'Istanza del Wallet. Questo percorso è disponibile per i tipi di credenziale idonei per la discovery pubblica come determinato dalle politiche dell'organismo di supervisione durante il processo di onboarding (vedere :ref:`registry:Catalogo degli Attestati Elettronici`).

- **da un Touchpoint della Fonte Autentica** (o del Fornitore di Attestati Elettronici di Attributi se coincide con la Fonte Autentica): l'Utente interagisce con il servizio digitale della Fonte Autentica, consentendogli di ottenere un Attestato Elettronico di Attributi specifico nella propria Istanza del Wallet tramite un Engagement Button. Questo percorso consente l'accesso sia alle credenziali pubblicate nel catalogo che alle credenziali private non idonee per la discovery pubblica (vedere :ref:`registry:Catalogo degli Attestati Elettronici`).

Sebbene i metodi per avviare la richiesta siano diversi, i flussi di rilascio condividono una struttura e un processo simili. 

Rilascio dal Catalogo dell'Istanza del Wallet
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Di seguito sono illustrati i requisiti dell'Esperienza dell'Utente per il rilascio di un Attestato Elettronico di Attributi dal Catalogo che il Fornitore della Soluzione Wallet DEVE garantire attraverso la propria Soluzione Wallet:

- L'Utente accede alla propria Istanza del Wallet utilizzando il metodo di sblocco precedentemente impostato;
- L'Utente seleziona l'Attestato Elettronico di Attributi che desidera richiedere dalle opzioni disponibili nel Catalogo;
- L'Utente seleziona da quale Fornitore di Attestati Elettronici vuole ottenere l'Attestato Elettronico di Attributi, se ce n'è più di uno; 
- L'Utente visualizza eventuali informazioni aggiuntive sui requisiti e/o limitazioni relative all'ottenimento dell'Attestato Elettronico di Attributi dalla Fonte Autentica; 
- L'Utente visualizza i dati del PID, se richiesti dalla Fonte Autentica per la richiesta dell'Attestato Elettronico di Attributi, il nome del relativo Fornitore di Attestati Elettronici di Attributi e qualsiasi policy informativa correlata. L'Utente dà il proprio consenso per procedere, presentando i propri dati PID al Fornitore di Attestati Elettronici di Attributi, o annulla l'operazione;
- L'Utente visualizza eventuali informazioni aggiuntive sui requisiti e/o limitazioni relative all'ottenimento dell'Attestato Elettronico di Attributi dalla Fonte Autentica;
- L'Utente visualizza un'anteprima dell'Attestato Elettronico di Attributi. L'Utente conferma i dati mostrati nell'anteprima per procedere con la richiesta o annulla l'operazione;
- L'Utente autorizza l'operazione utilizzando il metodo di sblocco precedentemente impostato;
- L'Utente visualizza l'esito positivo della richiesta;
- L'Utente visualizza i dettagli dell'Attestato Elettronico di Attributi richiesto, inclusi: i dati contenuti in esso, il nome del Fornitore di Attestati Elettronici di Attributi che ha rilasciato l'Attestato e il nome della Fonte Autentica;
- L'Utente ha accesso a tutti gli Attestati Elettronici rilasciati navigando nell'Istanza del Wallet.

La Fonte Autentica PUÒ fornire informazioni aggiuntive relative a un Attestato Elettronico di Attributi. Queste informazioni DEVONO essere visualizzate dall'Istanza del Wallet all'Utente, prima di avviare il processo di rilascio dell'Attestato Elettronico di Attributi. Al fine di redigere correttamente questo contenuto informativo, la Fonte Autentica: 

- DEVE utilizzare un linguaggio chiaro (ad esempio evitare termini tecnici o complessi), essere concisa (ad esempio evitare testi eccessivamente lunghi o elaborati) e inclusiva (ad esempio evitare verbi basati sulle abilità), seguendo le migliori pratiche per la scrittura, il linguaggio e il tono di voce descritte in [REF_ACCESSIBILITY] e, nel caso di enti pubblici, in [GL_DESIGN]; 

- DEVE aderire allo scopo specifico del testo, comunicando informazioni utili all'Utente prima di impegnarsi nel processo di rilascio (ad esempio elencando prerequisiti o dichiarando limitazioni che potrebbero influenzare l'esito positivo della procedura); 

- DEVE garantire che le informazioni siano costantemente aggiornate; 

- DEVE includere un titolo e un testo in cui PUÒ includere riferimenti a canali esterni per indirizzare gli Utenti a una procedura, esplorare un argomento specifico e/o aprire richieste di supporto. 

Segue un esempio di testo informativo: 

**Titolo:** Hai già il documento fisico? 

**Testo:** Per ottenere la versione digitale di [Nome del documento], assicurati di aver già ottenuto il corrispondente documento fisico. Per maggiori dettagli, [leggi ulteriori informazioni] (URL). 

Per ulteriori informazioni, si prega di fare riferimento alla sezione :ref:`registry:Catalogo degli Attestati Elettronici` (vedere claim ``user_information``). 

Il Fornitore di Wallet DEVE consentire all'Utente di rimuovere un Attestato Elettronico di Attributi attraverso la propria Istanza del Wallet in qualsiasi momento. In caso di assenza del dispositivo dove è stata attivata l'Istanza del Wallet, il Fornitore di Wallet DEVE consentire all'Utente di disattivare l'intera Istanza del Wallet attraverso un Touchpoint specifico. Inoltre, i Fornitori di Attestati Elettronici di Attributi DOVREBBERO consentire all'Utente di revocare le Attestati Elettronici rilasciate attraverso Touchpoint specifici. Per maggiori dettagli, si prega di fare riferimento alle sezioni `Disattivazione dell'Istanza del Wallet`_ e `Gestione degli Attestati Elettronici`_.

Nel caso di problemi di comunicazione tra i sistemi del Fornitore di Attestati Elettronici di Attributi e la Fonte Autentica, o se processi amministrativi o tecnici impediscono il rilascio immediato dell'Attestato Elettronico di Attributi, gli attori coinvolti POSSONO supportare un processo di rilascio differito. In questo caso il Fornitore di Wallet DEVE garantire che:

- Al raggiungimento del passaggio finale del processo, l'Utente visualizzi un messaggio che lo invita ad attendere fino a quando l'Attestato Elettronico di Attributi può essere rilasciato.
- L'Utente viene informato dal Fornitore di Attestati Elettronici di Attributi una volta che l'Attestato Elettronico di Attributi diventa disponibile.

Se l'Utente incontra dati errati in un Attestato Elettronico di Attributi già ottenuto o in corso, il Fornitore di Wallet DOVREBBE garantire all'Utente un'assistenza appropriata tramite la propria Istanza del Wallet. Per maggiori informazioni, si prega di fare riferimento alla sezione :ref:`functionalities:Assistenza all'Utente`.

In caso di errori nell'utilizzo dell'Istanza del Wallet, il Fornitore di Wallet DEVE garantire che l'Utente riceva messaggi coerenti che lo informino e lo guidino verso la risoluzione del problema. Per ulteriori dettagli, si prega di fare riferimento alla sezione :ref:`functionalities:Gestione degli Errori`.

Rilascio da un Touchpoint della Fonte Autentica 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Di seguito sono illustrati i requisiti dell'Esperienza dell'Utente per il rilascio di un Attestato Elettronico di Attributi dal Catalogo che il Fornitore della Soluzione Wallet DEVE garantire attraverso la propria Soluzione Wallet: 

- L'Utente interagisce con l'Engagement Button chiaramente visualizzato nell'interfaccia del Touchpoint; 
- L'Utente seleziona la Soluzione Wallet con cui procedere, attraverso un'interfaccia che DOVREBBE seguire le indicazioni e le funzionalità descritte per la *Pagina di Selezione* nella sezione :ref:`functionalities:Autenticazione`; 
- (*solo cross-device*) l'Utente scansiona il codice QR che invoca l'apertura della propria Istanza del Wallet scelta, attraverso un'interfaccia che DOVREBBE seguire le indicazioni e le funzionalità descritte per la *Pagina del Codice QR* nella sezione :ref:`functionalities:Autenticazione`; 
- (*solo cross-device*) l'Utente visualizza un messaggio che lo invita a continuare sulla propria Istanza del Wallet scelta, attraverso un'interfaccia che DOVREBBE seguire le indicazioni e le funzionalità descritte per la *Pagina di Attesa* nella sezione :ref:`functionalities:Autenticazione`; 
- L'Utente accede alla propria Istanza del Wallet utilizzando il metodo di sblocco precedentemente impostato; 
- L'Utente visualizza i dati del PID, se richiesti per la richiesta dell'Attestato Elettronico di Attributi, il nome del relativo Fornitore di Attestati Elettronici di Attributi e qualsiasi policy informativa correlata. L'Utente dà il proprio consenso per procedere, presentando i propri dati PID al Fornitore di Attestati Elettronici di Attributi, o annulla l'operazione; 
- L'Utente visualizza eventuali informazioni aggiuntive sui requisiti e/o limitazioni relative all'ottenimento dell'Attestato Elettronico di Attributi; 
- L'Utente visualizza un'anteprima dell'Attestato Elettronico di Attributi. L'Utente conferma i dati mostrati nell'anteprima per procedere con la richiesta o annulla l'operazione; 
- L'Utente autorizza l'operazione utilizzando il metodo di sblocco precedentemente impostato; 
- L'Utente visualizza l'esito positivo della richiesta; 
- L'Utente visualizza i dettagli dell'Attestato Elettronico di Attributi richiesto, inclusi: i dati contenuti in esso, il nome del Fornitore di Attestati Elettronici di Attributi che ha rilasciato l'Attestato e i nomi delle Fonti Autentiche. 

In caso di errori durante il rilascio dell'Attestato Elettronico di Attributi, la Fonte Autentica DEVE garantire che l'Utente riceva messaggi coerenti che lo informino e lo guidino verso la risoluzione del problema. Per ulteriori dettagli, si prega di fare riferimento alla sezione :ref:`functionalities:Gestione degli Errori`. 


Focus sugli Attestati Elettronici di Attributi
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gli EAA ottenuti all'interno dell'Istanza del Wallet DOVREBBERO essere visualizzati in un elenco all'interno di una Visualizzazione in anteprima. In questo caso, ogni EAA DEVE garantire un alto livello di riconoscibilità e accessibilità [REF_ACCESSIBILITY] delle informazioni contenute. Di seguito sono riportati i requisiti per la visualizzazione dell'EAA che ogni Fornitore di Wallet DEVE rispettare al fine di fornire un'esperienza di consultazione e utilizzo coerente e accessibile:

- L'EAA DEVE essere visualizzato correttamente su tutti i dispositivi, garantendo un'esperienza coerente su schermi di dimensioni diverse;
- Il nome dell'EAA DEVE essere chiaramente visibile e sempre visualizzato sia nella Vista di Dettaglio che nella Visualizzazione in anteprima;
- L'EAA, sia nella Visualizzazione in anteprima che nella Vista di Dettaglio, DEVE visualizzare il proprio stato se diverso da valido per fornire trasparenza sul suo ciclo di vita e PUÒ visualizzarlo se valido. La Visualizzazione in anteprima PUÒ anche includere Attributi aggiuntivi per migliorare l'Esperienza dell'Utente e la gestione; ad esempio, PUÒ visualizzare il nome o il logo del Fornitore di Attestati Elettronici di Attributi o del Fornitore di Attestati Elettronici di Dati di Identificazione Personale. La Vista di Dettaglio PUÒ fornire dettagli specifici sullo stato se non valido (ad esempio, il motivo per cui l'EAA è revocato);
- L'EAA DEVE includere Pulsanti di Azione nella Vista di Dettaglio per abilitare la gestione del ciclo di vita e consentire all'Utente di revocare o aggiornare un EAA in qualsiasi momento (vedere :ref:`functionalities:Gestione degli Attestati Elettronici`); 
- L'EAA DEVE essere un elemento interattivo, per consentire all'Utente di accedere ai servizi forniti dalle Relying Party in contesti digitali e di prossimità (vedere :ref:`functionalities:Presentazione di Attestati Elettronici`); 
- L'EAA PUÒ essere visualizzato in formato carta nella propria Visualizzazione in anteprima, in linea con approcci già utilizzati da altri portafogli digitali sul mercato, per rispecchiare l'aspetto di un documento fisico corrispondente. Quando applicabile, la natura digitale del documento PUÒ essere indicata, ad esempio etichettandolo come "versione digitale" nel layout; 
- L'EAA DEVE visualizzare le stesse informazioni nella Vista di Dettaglio come mostrato nella Visualizzazione in anteprima e PUÒ includere dettagli aggiuntivi; 
- L'EAA DEVE visualizzare un metodo di assistenza (vedere :ref:`functionalities:Assistenza all'Utente`); 
- Il layout dell'EAA nella Visualizzazione in anteprima DEVE essere ottimizzato per scalabilità e usabilità, specialmente quando più EAA sono visualizzati sulla stessa schermata; 
- La rappresentazione dell'EAA DEVE aderire a un set definito di specifiche fornite dal Fornitore di Attestati Elettronici di Attributi per garantire riconoscibilità, coerenza e omogeneità tra diverse Soluzioni Wallet. 

Il Fornitore di Attestati Elettronici di Attributi: 

- DEVE definire un nome/convenzione di denominazione per riferirsi agli EAA rilasciati, per garantire coerenza tra tutte le Soluzioni Wallet; il nome dell'EAA DEVE essere comprensibile e user-friendly evitando termini tecnici o acronimi quando possibile; 
- DEVE definire un set chiaro di specifiche per l'EAA per garantire identificazione e rappresentazione coerenti dell'EAA tra diverse Soluzioni Wallet, in termini di formato, struttura e standard di aspetto (ad esempio colore, immagine di sfondo, ecc.). 

Presentazione di Attestati Elettronici
---------------------------------------

Il processo di presentazione consente all'Utente di accedere a un servizio o dimostrare la proprietà di determinati dati o la propria idoneità a svolgere un'azione specifica. La presentazione di Attestati Elettronici e la loro successiva verifica coinvolge l'interazione tra l'Istanza del Wallet, gestita dall'Utente, e un'Istanza di Relying Party. A seconda delle circostanze e del contesto dell'interazione, possono essere delineati i seguenti scenari: 

- **Presentazione di Prossimità**: l'Utente presenta i dati del PID e/o dell'EAA attraverso l'Istanza del Wallet, direttamente a un Verificatore di Attestati Elettronici o a un dispositivo designato per la verifica di persona.

- **Presentazione Remota**: l'Utente presenta i dati del PID e/o dell'EAA attraverso l'Istanza del Wallet, a una Relying Party configurata per la verifica online, ad esempio, per Autenticarsi e accedere ai servizi offerti.

Presentazione di Prossimità
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

La presentazione di prossimità consente all'Utente di presentare i dati del PID e/o dell'EAA tramite la propria Istanza del Wallet, utilizzando uno di due metodi:

- **Modalità supervisionata**: l'Utente presenta i dati del PID e/o dell'EAA attraverso l'Istanza del Wallet a un Verificatore di Attestati Elettronici (ad esempio, agente delle forze dell'ordine, operatore di sportello) dotato di un sistema di verifica dedicato (:ref:`relying-party-instance:App di Verifica Mobile`). 

- **Modalità non supervisionata**: l'Utente presenta i dati del PID e/o dell'EAA attraverso l'Istanza del Wallet a un dispositivo designato (ad esempio, tornello, totem) fornito di un sistema di verifica dedicato (Embedded Relying Party Instance).

Di seguito sono riportati i requisiti dell'Esperienza dell'Utente relativi a entrambi i metodi che il Fornitore di Wallet DEVE garantire tramite la propria Soluzione Wallet.

**Modalità Supervisionata**

- L'Utente accede alla propria Istanza del Wallet utilizzando il metodo di sblocco precedentemente impostato;
- L'Utente naviga alla funzionalità dedicata alla generazione del codice QR;
- L'Utente presenta il codice QR generato al Verificatore di Attestati Elettronici che agisce per conto della Relying Party, che lo scansiona utilizzando l'app o il sistema di verifica designato;
- L'Utente esamina i dati del PID e/o dell'EAA richiesti, il nome del Fornitore di Servizi richiedente e qualsiasi policy correlata. L'Utente decide se presentare eventuali dati del PID e/o dell'EAA non obbligatori (Divulgazione Selettiva). L'Utente fornisce il consenso per procedere o annulla l'operazione;
- L'Utente autorizza l'operazione utilizzando il metodo di sblocco precedentemente impostato;
- L'Utente riceve conferma della presentazione riuscita.

In caso di errori nell'utilizzo dell'Istanza del Wallet, il Fornitore di Wallet DEVE garantire che l'Utente riceva messaggi coerenti che lo informino e lo guidino verso la risoluzione del problema. Per ulteriori dettagli, si prega di fare riferimento alla sezione `Gestione degli Errori`_.

**Modalità Non Supervisionata**

- L'Utente accede alla propria Istanza del Wallet utilizzando il metodo di sblocco precedentemente impostato;
- L'Utente naviga alla funzionalità dedicata alla generazione del codice QR;
- L'Utente presenta il codice QR generato al dispositivo designato (ad esempio, un tornello) della Relying Party per la scansione;
- L'Utente esamina i dati del PID e/o dell'EAA richiesti, il nome della Relying Party richiedente e qualsiasi policy correlata. L'Utente decide se presentare eventuali PID e/o EAA non obbligatori (Divulgazione Selettiva). L'Utente fornisce il consenso per procedere o annulla l'operazione;
- L'Utente autorizza l'operazione utilizzando il metodo di sblocco precedentemente impostato;
- L'Utente riceve conferma della presentazione riuscita.

In caso di errori nell'utilizzo dell'Istanza del Wallet, il Fornitore di Wallet DEVE garantire che l'Utente riceva messaggi coerenti che lo informino e lo guidino verso la risoluzione del problema. Per ulteriori dettagli, si prega di fare riferimento alla sezione :ref:`functionalities:Gestione degli Errori`.

Presentazione Remota
^^^^^^^^^^^^^^^^^^^^^

La presentazione remota consente all'Utente di presentare i dati del PID e/o dell'EAA interagendo con un Touchpoint di una Relying Party attraverso un Engagement Button designato.

Questa presentazione può avvenire in due modalità diverse, a seconda del tipo di dispositivo utilizzato per accedere al servizio:

- **Modalità same-device**: quando l'Utente accede a un servizio digitale online integrato con un sistema di verifica speciale (:ref:`relying-party-instance:App di Verifica Web`) utilizzando lo stesso dispositivo su cui è installata l'Istanza del Wallet;
- **Modalità cross-device**: quando l'Utente accede a un servizio digitale integrato con un sistema di verifica speciale (:ref:`relying-party-instance:App di Verifica Web`) utilizzando un dispositivo diverso da quello dove è installata l'Istanza del Wallet.

Di seguito sono riportati i requisiti dell'Esperienza dell'Utente relativi a entrambi i metodi che il Fornitore di Wallet DEVE garantire tramite la propria Soluzione Wallet.

**Modalità Same-Device**

- L'Utente clicca l'Engagement Button fornito sul Touchpoint della Relying Party;
- L'Utente accede alla propria Istanza del Wallet utilizzando il metodo di sblocco precedentemente impostato;
- L'Utente esamina i dati del PID e/o dell'EAA richiesti, il nome della Relying Party richiedente e qualsiasi policy correlata. L'Utente decide se presentare eventuali dati del PID e/o dell'EAA non obbligatori (Divulgazione Selettiva). L'Utente fornisce il consenso per procedere o annulla l'operazione;
- L'Utente autorizza l'operazione utilizzando il metodo di sblocco precedentemente impostato;
- L'Utente riceve conferma della presentazione riuscita all'interno dell'Istanza del Wallet;
- L'Utente torna al Touchpoint della Relying Party, dove vede la conferma della presentazione completata.

In caso di errori nell'utilizzo dell'Istanza del Wallet, il Fornitore di Wallet DEVE garantire che l'Utente riceva messaggi coerenti che lo informino e lo guidino verso la risoluzione del problema. Per ulteriori dettagli, si prega di fare riferimento alla sezione `Gestione degli Errori`_.

**Modalità Cross-Device**

- L'Utente clicca l'Engagement Button fornito sul Touchpoint della Relying Party mentre accede al servizio da un dispositivo diverso da quello dove è installata l'Istanza del Wallet;
- L'Utente accede all'Istanza del Wallet desiderata dal dispositivo dove è installata, utilizzando il metodo di sblocco precedentemente impostato;
- L'Utente scansiona il codice QR fornito dalla Relying Party utilizzando la propria Istanza del Wallet;
- L'Utente esamina i dati del PID e/o dell'EAA richiesti, il nome della Relying Party richiedente e qualsiasi policy correlata. L'Utente decide se presentare eventuali dati personali non obbligatori (Divulgazione Selettiva). L'Utente fornisce il consenso per procedere o annulla l'operazione.
- L'Utente autorizza l'operazione utilizzando il metodo di sblocco precedentemente impostato;
- L'Utente riceve conferma della presentazione riuscita all'interno dell'Istanza del Wallet;
- L'Utente torna al Touchpoint della Relying Party e visualizza la conferma della presentazione completata.

In caso di errori nell'utilizzo dell'Istanza del Wallet, il Fornitore di Wallet DEVE garantire che l'Utente riceva messaggi coerenti che lo informino e lo guidino verso la risoluzione del problema. Per ulteriori dettagli, si prega di fare riferimento alla sezione `Gestione degli Errori`_.

Autenticazione
"""""""""""""""

L'Autenticazione è un caso d'uso specifico della presentazione remota che consente all'Utente di accedere in modo sicuro ai servizi forniti da Relying Party sia pubbliche che private. Questo viene ottenuto presentando il PID e, se necessario, un set di Attributi contenuti negli Attestati Elettronici di Attributi ottenuti. Questo processo garantisce che l'Utente mantenga il controllo sui propri dati, inclusa la capacità di presentare solo le informazioni strettamente necessarie per la verifica da parte delle Relying Party.

Il processo di Autenticazione può essere eseguito utilizzando sia le modalità same-device che cross-device descritte sopra. Per i requisiti funzionali dell'Esperienza dell'Utente che DEVONO essere affrontati, si prega di fare riferimento ai requisiti funzionali per la `presentazione remota`_ nelle modalità same-device e cross-device.

Dal punto di vista dell'Esperienza dell'Utente, il processo di Autenticazione differisce dal processo di Presentazione solo nel modo in cui viene avviato, che è attraverso un `Pulsante per l'autenticazione`_ dedicato.

Per garantire un processo di Autenticazione coerente e senza interruzioni tra tutte le Relying Party, ogni Relying Party DEVE seguire i requisiti visivi e dell'Esperienza dell'Utente delineati di seguito, insieme alla conformità con [REF_ACCESSIBILITY] e, nel caso di enti pubblici, con [GL_DESIGN]

Le Relying Party DOVREBBERO utilizzare le :ref:`official-resources:Risorse Ufficiali` per la progettazione e lo sviluppo. Se una Relying Party non intende utilizzare tali risorse open source, PUÒ sviluppare indipendentemente le Soluzioni Tecniche che abilitano il flusso di Autenticazione, garantendo che segua le specifiche qui fornite.

.. note::
  Le immagini in questa sezione devono essere considerate illustrative in quanto sono soggette a evoluzioni dell'interfaccia (UI), in attesa della definizione del branding del Sistema IT-Wallet. 

Le Relying Party DEVONO implementare e fornire le seguenti pagine come parte del processo di Autenticazione:

- **Discovery Page**: elenca tutti i metodi di Autenticazione disponibili;
- **Pagina di Selezione**: mostra all'Utente tutte le Soluzioni Wallet disponibili nel Registro e gli consente di scegliere con quale continuare il processo di Autenticazione; 
- **Pagina del Codice QR** (*solo cross-device*): invita l'Utente a scansionare un codice QR;
- **Pagina di Attesa** (*solo cross-device*): istruisce l'Utente a continuare il processo di Autenticazione sulla propria Istanza del Wallet;
- **Pagina di Ringraziamento**: conferma l'Autenticazione riuscita;
- **Pagina di Errore**: visualizza messaggi di errore relativi al processo di Autenticazione.

Ognuna di queste pagine DEVE includere i seguenti elementi ricorrenti, in linea con l'Identità Visiva del Touchpoint della Relying Party:

- Un **header e/o subheader** che consente agli Utenti di navigare indietro alla pagina precedente.
- Un **footer** che include la privacy policy, l'avviso legale e la dichiarazione di accessibilità, dove richiesto dalle normative vigenti.

I requisiti specifici per ogni singola pagina sono dettagliati di seguito.

**Discovery Page**

Per abilitare l'Autenticazione tramite il Sistema IT-Wallet, la Relying Party PUÒ sostituire la propria Discovery Page esistente con la versione fornita nelle :ref:`official-resources:Risorse Ufficiali`.

.. only:: format_html

  .. figure:: ./images/svg/discovery-page.svg
     :alt: Modello di Layout della Discovery Page in griglia
     :width: 100%

     Modello di Layout della Discovery Page in griglia  

.. only:: format_latex  

  .. figure:: ./images/pdf/discovery-page.pdf
     :alt: Modello di Layout della Discovery Page in griglia 
     :width: 100% 

     Modello di Layout della Discovery Page in griglia 

In alternativa, la Relying Party PUÒ mantenere la propria Discovery Page ma DEVE integrare il Pulsante per l'autenticazione come specificato nella sezione `Pulsante per l'autenticazione`_.

La Relying Party che implementa la pagina:

- DEVE visualizzare tutti i metodi di Autenticazione dell'Identità Digitale disponibili, inclusa l'Autenticazione del Sistema IT-Wallet attraverso il Pulsante per l'autenticazione;
- PUÒ anche presentare metodi di Autenticazione alternativi, se disponibili; 
- DOVREBBE fornire informazioni di supporto essenziali per aiutare l'Utente a fare una scelta informata e consapevole.

Se l'Utente accede alla Discovery Page da un Touchpoint diverso da quello dove è attivata l'Istanza del Wallet (cross-device), selezionare l'Autenticazione del Sistema IT-Wallet DEVE reindirizzare l'Utente alla Pagina del Codice QR.

Se l'Utente accede alla Discovery Page dallo stesso Touchpoint dove è attivata l'Istanza del Wallet (same-device), la selezione DEVE attivare l'apertura dell'Istanza del Wallet dell'Utente.

**Pagina di Selezione**

La Pagina di Selezione è la pagina su cui l'Utente atterra dopo aver scelto di Autenticarsi tramite il Sistema IT-Wallet, ed è destinata a presentare all'Utente le Soluzioni Wallet disponibili per eseguire l'Autenticazione. 

La Relying Party DEVE implementare la Pagina di Selezione resa disponibile nelle :ref:`official-resources:Risorse Ufficiali`. 

.. only:: format_html 

  .. figure:: ./images/svg/selection-page.svg
     :alt: Pagina di Selezione
     :width: 100%

     Pagina di Selezione 

.. only:: format_latex  

  .. figure:: ./images/pdf/selection-page.pdf
     :alt: Pagina di Selezione
     :width: 100%

     Pagina di Selezione 

La Relying Party che implementa la pagina: 

- DEVE includere gli elementi propri dell'Identità Visiva del Sistema IT-Wallet, incluso il Logo posizionandolo accanto al proprio logo secondo le indicazioni fornite nella sezione :ref:`brand-identity:Identità Visiva`; 

- DEVE garantire che il copy sulla pagina rispecchi quello riportato nelle :ref:`official-resources:Risorse Ufficiali`; 

- DEVE presentare ogni Soluzione Wallet nel Registro IT-Wallet attraverso un componente modulare che visualizza il logo e il nome per intero; 

- DEVE presentare le Soluzioni Wallet in un layout dinamico che si adatta al numero di Soluzioni Wallet disponibili: quando meno di 3 DEVE distribuirle in una griglia a 2 colonne, quando meno di 2 DEVE utilizzare un layout a colonna centrale; in tutti i casi DEVE essere garantito un ordinamento casuale; 

- DEVE consentire all'Utente di cercare una Soluzione Wallet attraverso una funzionalità di filtro per nome, quando sono presenti più di 5 Soluzioni Wallet; 

- DEVE consentire all'Utente di scoprire, quando necessario, quali Soluzioni Wallet sono disponibili nel Registro preparando un riferimento incrociato al sito ufficiale del Sistema IT-Wallet; 

- DEVE includere una Call to Action che consente all'Utente di interrompere l'operazione e tornare alla Discovery Page. 

La Relying Party PUÒ anche includere un componente di testo sulla Pagina di Selezione per promuovere la modalità di Autenticazione tramite IT-Wallet, che rimanda al sito web ufficiale del Sistema IT-Wallet, come rappresentato nelle :ref:`official-resources:Risorse Ufficiali`. 

**Pagina del Codice QR (solo cross-device)**

La Pagina del Codice QR viene presentata all'Utente che seleziona l'Autenticazione del Sistema IT-Wallet all'interno di un processo cross-device. Il suo scopo è invitare l'Utente a scansionare il codice QR generato utilizzando la propria Istanza del Wallet.

Le Relying Party DEVONO implementare la Pagina del Codice QR (cross-device) fornita nelle :ref:`official-resources:Risorse Ufficiali`. 

.. only:: format_html 

  .. figure:: ./images/svg/QR-page.svg
     :alt: Pagina del Codice QR
     :width: 100%

     Pagina del Codice QR 
 
.. only:: format_latex  

  .. figure:: ./images/pdf/QR-page.pdf
     :alt: Pagina del Codice QR
     :width: 100%

     Pagina del Codice QR 

La Relying Party che implementa la pagina:

- DEVE includere gli elementi dell'Identità Visiva del Sistema IT-Wallet, incluso il logo;
- DEVE garantire che il copy sulla pagina rispecchi quello riportato nelle :ref:`official-resources:Risorse Ufficiali`; 
- DEVE includere una Call To Action che consente all'Utente di generare un nuovo codice QR in caso di timeout;
- DEVE includere una Call To Action che consente all'Utente di annullare l'operazione e tornare alla Discovery Page.

Inoltre, in conformità con [REF_ACCESSIBILITY], riguardo al codice QR, le Relying Party:

- DEVONO rispettare le dimensioni minime raccomandate per garantire una scansione efficace. Una dimensione di 150x150 pixel è generalmente adeguata, ma per codici con alta densità di dati (ad esempio URL lunghi o numerosi caratteri), è consigliabile aumentarla a 300x300 pixel o più;
- DEVONO garantire il contrasto minimo tra il codice QR e lo sfondo (la condizione ideale prevede uno sfondo bianco con un codice QR nero);
- DEVONO evitare inversioni di colore tra sfondo e codice QR;
- DEVONO limitare la presenza a un solo codice QR per pagina;
- DEVONO garantire nitidezza e alta qualità;
- DEVONO garantire formato SVG;
- DEVONO garantire che non sia parzialmente nascosto da testo o altri elementi.

**Pagina di Attesa (solo cross-device)**

La Pagina di Attesa viene mostrata dopo che il codice QR è stato scansionato e invita l'Utente a continuare il processo di Autenticazione all'interno della propria Istanza del Wallet.

Le Relying Party DEVONO implementare la Pagina di Attesa (cross-device) fornita nelle :ref:`official-resources:Risorse Ufficiali`. 

.. only:: format_html 

  .. figure:: ./images/svg/waiting-page.svg
     :alt: Pagina di Attesa
     :width: 100%

     Pagina di Attesa 
 
.. only:: format_latex  

  .. figure:: ./images/pdf/waiting-page.pdf
     :alt: Pagina di Attesa
     :width: 100%

     Pagina di Attesa 

La Relying Party che implementa la pagina:

- DEVE includere gli elementi dell'Identità Visiva del Sistema IT-Wallet, incluso il logo e un'icona o elemento grafico che consolida il messaggio;
- DEVE garantire che il copy sulla pagina rispecchi quello riportato nelle :ref:`official-resources:Risorse Ufficiali`.

**Pagina di Ringraziamento**

La Pagina di Ringraziamento viene visualizzata dopo che l'Utente completa il processo di Autenticazione tramite la propria Istanza del Wallet. Il suo scopo è invitare l'Utente a procedere all'area autenticata del Touchpoint della Relying Party.

Le Relying Party DEVONO implementare la Pagina di Ringraziamento fornita nelle :ref:`official-resources:Risorse Ufficiali`. 

.. only:: format_html 

  .. figure:: ./images/svg/thank-you-page.svg
     :alt: Pagina di Ringraziamento
     :width: 100%

     Pagina di Ringraziamento 
 
.. only:: format_latex  

  .. figure:: ./images/pdf/thank-you-page.pdf
     :alt: Pagina di Ringraziamento
     :width: 100%

     Pagina di Ringraziamento 

La Relying Party che implementa la pagina:

- DEVE includere gli elementi dell'Identità Visiva del Sistema IT-Wallet, incluso il logo e un'icona o elemento grafico che consolida il messaggio;
- DEVE garantire che il copy sulla pagina rispecchi quello riportato nelle :ref:`official-resources:Risorse Ufficiali`;
- DEVE includere una Call To Action che invita l'Utente a procedere all'area autenticata del Touchpoint.

**Pagina di Errore**

La Pagina di Errore viene visualizzata quando si verifica un problema durante il processo di Autenticazione. Il suo scopo è informare l'Utente sulla natura dell'errore (ad esempio, problema tecnico, problemi di rete, malfunzionamento dell'Istanza del Wallet, condivisione dati negata, ecc.) e presentare i passaggi successivi disponibili. Per ulteriori dettagli, fare riferimento alla sezione :ref:`functionalities:Gestione degli Errori`.

Le Relying Party DEVONO implementare la Pagina di Errore fornita nelle :ref:`official-resources:Risorse Ufficiali`. 

.. only:: format_html 

  .. figure:: ./images/svg/error-page.svg
     :alt: Pagina di Errore
     :width: 100%

     Pagina di Errore 
 
.. only:: format_latex  

  .. figure:: ./images/pdf/error-page.pdf
     :alt: Pagina di Errore
     :width: 100%

     Pagina di Errore 

La Relying Party che implementa la pagina:

- DEVE includere gli elementi dell'Identità Visiva del Sistema IT-Wallet, incluso il logo e un'icona o elemento grafico che trasmette il tipo di errore;
- DEVE garantire che il copy sulla pagina rispecchi quello riportato nelle :ref:`official-resources:Risorse Ufficiali`;
- DEVE includere una o più Call To Action che guidano l'Utente verso il passaggio successivo appropriato (ad esempio, riprova, contatta il supporto, ecc.).

Pulsante per l'autenticazione
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Il Pulsante per l'autenticazione "Accedi con IT-Wallet" funge da Engagement Button, fornendo agli Utenti un modo standardizzato per Autenticarsi utilizzando il proprio Wallet digitale.

Le Relying Party DEVONO rendere disponibile il Pulsante per l'autenticazione all'interno della Discovery Page delle proprie Soluzioni Tecniche per consentire all'Utente di autenticarsi nei propri servizi utilizzando l'Istanza del Wallet sotto il proprio controllo.

Il Pulsante per l'autenticazione ha i seguenti requisiti:

- Il Pulsante per l'autenticazione DEVE essere utilizzato esattamente come delineato nelle :ref:`official-resources:Risorse Ufficiali` e NON DEVE essere riprogettato ad hoc;

- Il Pulsante per l'autenticazione DEVE essere utilizzato solo nelle forme, colori e proporzioni definite e NON DEVE essere alterato, distorto o nascosto;

- Il Pulsante per l'autenticazione DEVE essere responsivo a tutte le risoluzioni dello schermo e DEVE essere integrato nella Discovery Page per soddisfare i requisiti minimi di usabilità e accessibilità;

- Gli attori che desiderano integrare il Pulsante per l'autenticazione nella propria Soluzione Tecnica DEVONO garantire che sia tradotto in altre lingue, almeno in inglese; 

- Il Pulsante per l'autenticazione DEVE mantenere una distanza minima da altri elementi (``quiet zone``) di almeno 24px; 

- Il Pulsante per l'autenticazione DEVE riportare "Accedi con IT-Wallet";

- Il Pulsante per l'autenticazione DOVREBBE sempre essere accompagnato da un link esterno (ad esempio, "Scopri di più") che rimanda al sito web ufficiale del Sistema IT-Wallet ``www.wallet.gov.it``; 

- Dove lo spazio lo consente e/o il contesto lo richiede, il Pulsante per l'autenticazione DOVREBBE essere accompagnato da un testo descrittivo, ad esempio, "IT-Wallet è il Sistema di Portafoglio Digitale Italiano che ti dà il pieno controllo sulle tue informazioni, senza che l'entità emittente sia a conoscenza di quando e come viene utilizzato" o "Accedi attraverso un'app IT-Wallet, il Sistema di Portafoglio Digitale Italiano che semplifica le interazioni tra cittadini, pubbliche amministrazioni ed entità private, nel mondo fisico e digitale. Con IT-Wallet hai il pieno controllo sulle tue informazioni, condividendole solo quando necessario e in modo sicuro, senza che l'entità emittente sappia quando e come vengono utilizzate.". 


Di seguito sono riportati alcuni esempi non obbligatori di layout del Pulsante per l'autenticazione: 

 
.. only:: format_html 

  .. figure:: ./images/svg/authentication-button-layout.svg
     :alt: Varianti del Pulsante per l'autenticazione 
     :width: 100% 

     Varianti del Pulsante per l'autenticazione 

.. only:: format_latex  

  .. figure:: ./images/pdf/authentication-button-layout.pdf 
     :alt: Varianti del Pulsante per l'autenticazione 
     :width: 100% 

     Varianti del Pulsante per l'autenticazione 

L'integrazione del Pulsante per l'autenticazione all'interno della Discovery Page può variare a seconda del layout della pagina. Di seguito sono riportati esempi illustrativi, non esaustivi, di Discovery Page utilizzando layout a griglia, schede e elenco, rispettivamente.

.. only:: format_html

  .. figure:: ./images/svg/discovery-page-layouts.svg
     :alt: Esempi di layout della Discovery Page: griglia, schede ed elenco
     :width: 100%

     Esempi di layout della Discovery Page: griglia, schede ed elenco

.. only:: format_latex 

  .. figure:: ./images/pdf/discovery-page-layouts.pdf
     :alt: Esempi di layout della Discovery Page: griglia, schede ed elenco
     :width: 100%

     Esempi di layout della Discovery Page: griglia, schede ed elenco

Per ulteriori dettagli sull'uso del Pulsante per l'autenticazione, si prega di fare riferimento alla sezione :ref:`functionalities:Autenticazione`.

**Pulsante "Accedi con IT-Wallet" - codice html**  

Il pulsante è disponibile in 3 varianti (default / M / L ) e nei formati "get" (chiamata a una pagina esterna) e "post" (form all'interno del pulsante). 
I riferimenti al codice html e all'Identità del Marchio saranno inclusi nelle prossime versioni delle presenti specifiche.
 

**Pulsante "Accedi con IT-Wallet" – svg**
Di seguito un esempio non normativo del Pulsante per l'autenticazione. I riferimenti all'Identità del Marchio saranno inclusi nelle prossime versioni delle presenti specifiche.

.. literalinclude:: ../../examples/authentication_button.svg
  :language: xml 

Gestione degli Attestati Elettronici
-------------------------------------

Il Fornitore di Wallet, tramite la propria Soluzione Wallet, e il fornitore di PID o Fornitore di Attestati Elettronici di Attributi, tramite Touchpoint dedicati, DEVONO consentire all'Utente di gestire i propri Attestati Elettronici in qualsiasi momento.

Questa sezione delinea tre diverse categorie di requisiti per la gestione di ogni Attestato Elettronico, specificamente riguardo a:

- **Il suo stato**: per consentire all'Utente di verificare se un Attestato Elettronico è valido o non valido;
- **Il suo utilizzo**: per consentire all'Utente di visualizzare e gestire la cronologia delle presentazioni effettuate con un Attestato Elettronico;
- **I suoi dati**: per consentire all'Utente di eseguire il backup e ripristinare ogni Attestato Elettronico di Attributi in conformità al principio di portabilità dei dati.

Di seguito sono riportati gli aspetti chiave che impattano e definiscono l'Esperienza dell'Utente nella gestione degli Attestati Elettronici attraverso l'Istanza del Wallet, insieme ai requisiti funzionali associati a ogni categoria.

Stato degli Attestati Elettronici
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Per garantire affidabilità e promuovere l'uso corretto di una Soluzione Wallet, il Fornitore di Wallet DEVE garantire all'Utente di avere sempre visibilità dello stato degli Attestati Elettronici memorizzati all'interno della propria Istanza del Wallet, basandosi sulle informazioni ricevute dal Fornitore di Attestati Elettronici, che gestisce il loro ciclo di vita.

Ogni Attestato Elettronico può essere valido o non valido, con impatti corrispondenti sulle sue opportunità di utilizzo:

- **Valido**: Gli Attestati Elettronici validi DEVONO essere utilizzabili e quindi presentabili. Questa categoria include anche Attestati Elettronici che stanno per scadere. Se un Attestato Elettronico sta per scadere, l'Istanza del Wallet DOVREBBE informare l'Utente con adeguato preavviso per consentire tempo sufficiente per richiederne la riemissione o, se necessario, revocarlo.

- **Non valido**: Gli Attestati Elettronici non validi NON DEVONO essere utilizzabili o presentabili. Questa categoria include Attestati Elettronici scaduti o revocati. In tali casi, l'Istanza del Wallet DEVE informare l'Utente dello stato non valido e DOVREBBE fornire il motivo. Se un Attestato Elettronico non è più valido e non può essere utilizzato in nessuno scenario, la Soluzione Wallet PUÒ implementare meccanismi per limitare l'accesso alla Vista di Dettaglio di quell'Attestato Elettronico. Questo è inteso per incoraggiare l'Utente ad aggiornare o eliminare l'Attestato Elettronico fornendo testo informativo appropriato e una Call to Action.

Revoca degli Attestati Elettronici
"""""""""""""""""""""""""""""""""""

La revoca è la procedura che trasforma un Attestato Elettronico da uno stato valido a uno stato non valido. La revoca può avvenire in modalità attiva o passiva:

- **Revoca attiva**: Si riferisce alla revoca di un Attestato Elettronico su richiesta dell'Utente. Questo processo riguarda solo l'Attestato Elettronico e non il suo documento fisico corrispondente, se esistente. Di seguito è riportato un elenco illustrativo di scenari in cui il Fornitore di Wallet DEVE dare all'Utente la capacità di richiedere la revoca di un Attestato Elettronico:

	- L'Utente decide di non voler più utilizzare un Attestato Elettronico specifico;
	- L'Utente decide di disattivare la propria Istanza del Wallet, revocando così tutti gli Attestati Elettronici precedentemente ottenuti;
	- L'Utente non ha più possesso del dispositivo su cui è installata la propria Istanza del Wallet a causa di perdita o furto.

- **Revoca passiva**: Si riferisce alla revoca di un Attestato Elettronico gestita dal rispettivo Fornitore di Attestati Elettronici per conto della Fonte Autentica. In questo caso, l'Istanza del Wallet DEVE informare l'Utente del cambiamento di stato dell'Attestato Elettronico e il Fornitore di Attestati Elettronici PUÒ inoltre notificare l'Utente tramite altri Touchpoint. Di seguito è riportato un elenco illustrativo di scenari che potrebbero portare alla revoca di un Attestato Elettronico:

	- Il documento fisico corrispondente all'Attestato Elettronico è stato segnalato come perso o danneggiato dall'Utente attraverso il canale/Touchpoint appropriato;
	- Il documento fisico corrispondente all'Attestato Elettronico è stato revocato dalle autorità competenti;
	- I requisiti minimi di sicurezza e/o affidabilità per una o più parti coinvolte non sono più soddisfatti.
	- Il dispositivo dell'Utente non soddisfa più i requisiti minimi di sicurezza (rooted o jailbroken).

Cronologia degli Attestati Elettronici
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Per garantire i principi di visibilità e trasparenza, il Fornitore di Wallet DEVE garantire all'Utente di visualizzare la cronologia di tutte le presentazioni di Attestati Elettronici eseguite utilizzando la propria Istanza del Wallet. In particolare:

- L'Istanza del Wallet DEVE mostrare all'Utente con quale Relying Party ha interagito e quali Attestati Elettronici sono stati presentati e verificati;
- L'Istanza del Wallet DEVE consentire all'Utente di richiedere facilmente alla Relying Party di eliminare le proprie informazioni relative a presentazioni precedenti.

Backup e Ripristino di Attestati Elettronici di Attributi
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Con l'obiettivo di garantire il principio di portabilità dei dati, la Soluzione Wallet DEVE garantire all'Utente di avere accesso a funzionalità specifiche, in particolare per:

- Richiedere il backup e l'archiviazione di Attestati Elettronici di Attributi ottenuti attraverso la propria Istanza del Wallet;
- Richiedere il ripristino dei propri Attestati Elettronici di Attributi su un'altra Istanza del Wallet.

Disattivazione dell'Istanza del Wallet
---------------------------------------

La disattivazione dell'Istanza del Wallet è la funzionalità che rende l'Istanza del Wallet inattiva e quindi non più operativa. Il processo di disattivazione può essere attivato da diversi attori a seconda delle circostanze, specificamente:

- Dall'Utente, in casi come:

	- Il dispositivo è stato perso o rubato;
	- Il dispositivo è stato compromesso;
	- Il dispositivo è stato ripristinato alle impostazioni di fabbrica.

- Da una terza parte autorizzata, in casi come:

	- La Soluzione Wallet non soddisfa più i requisiti minimi di sicurezza.

Il Fornitore di Wallet DEVE garantire all'Utente la capacità di disattivare volontariamente la propria Istanza del Wallet attraverso:

- L'Istanza del Wallet stessa;
- Un Touchpoint (ad esempio, un sito web) fornito dal Fornitore di Wallet;
- L'app store del dispositivo, disinstallando l'Istanza del Wallet.

Di seguito sono riportati i requisiti funzionali e dell'Esperienza dell'Utente che il Fornitore di Wallet DEVE garantire tramite la propria Soluzione Wallet:

- L'Utente accede alla propria Istanza del Wallet utilizzando il metodo di sblocco precedentemente configurato o si Autentica al Touchpoint fornito dal Fornitore di Wallet;
- L'Utente seleziona la funzionalità di disattivazione dell'Istanza del Wallet;
- L'Utente viene informato che disattivare l'Istanza del Wallet invaliderà gli Attestati Elettronici precedentemente ottenuti;
- L'Utente conferma l'azione per procedere con la disattivazione, o annulla l'operazione;
- L'Utente riceve conferma della disattivazione riuscita;
- L'Utente viene notificato che l'Istanza del Wallet è inattiva quando accede nuovamente;
- L'Utente ha la capacità di riattivare l'Istanza del Wallet scaricando nuovamente l'app dall'app store (se disinstallata) e/o seguendo nuovamente il processo di attivazione. Per ulteriori dettagli, si prega di fare riferimento alla sezione `Attivazione dell'Istanza del Wallet`_.

Una volta che l'Istanza del Wallet è riattivata, gli Attestati Elettronici di Attributi possono essere riottenuti avviando nuovamente il processo di rilascio o ripristino. Per maggiori dettagli, si prega di fare riferimento alle sezioni `Rilascio di Attestati Elettronici di Attributi`_ e `Backup e Ripristino di Attestati Elettronici di Attributi`_.

In caso di errori nell'utilizzo dell'Istanza del Wallet, il Fornitore di Wallet DEVE garantire che l'Utente riceva messaggi coerenti che lo informino e lo guidino verso la risoluzione del problema. Per maggiori dettagli, si prega di fare riferimento alla sezione `Gestione degli Errori`_.

Gestione degli Errori
----------------------

Il Sistema IT-Wallet coinvolge l'interazione di più servizi forniti da diversi attori. È quindi importante definire un modello efficace di gestione degli errori con l'obiettivo di migliorare la percezione e l'affidabilità dell'intero ecosistema e consentire all'Utente di sentirsi guidato durante le interazioni con le varie Soluzioni Tecniche e di gestire consapevolmente eventuali problemi durante l'utilizzo del servizio.

Una comunicazione efficace in caso di errore fornisce anche benefici per gli attori coinvolti, in quanto contribuisce alla riduzione delle richieste di assistenza e, quindi, alla minimizzazione dell'impatto sui sistemi di supporto.

Ogni Attore Primario DEVE implementare una gestione degli errori appropriata, in conformità alle presenti Specifiche Tecniche, al fine di comunicare errori ed eccezioni all'Utente e attraverso l'Istanza IT-Wallet. Gli errori possono essere categorizzati, in base alla loro natura, come segue: 

- **La fase dell'Esperienza dell'Utente** dove l'errore può verificarsi: attivazione o disattivazione dell'Istanza del Wallet, ottenimento, presentazione o gestione di Attestati Elettronici di Attributi;
- **Il tipo di errore**: errore di sistema, errore di comunicazione tra attori, ecc.;
- **L'attore responsabile** dell'errore: Fornitore di Wallet, Fornitore di Attestati Elettronici di Dati di Identificazione Personale, Fornitore di Attestati Elettronici di Attributi, Fonte Autentica;
- **Il modo in cui l'errore viene visualizzato**: messaggio sulla pagina, banner, messaggio toast, e così via;
- **Azioni suggerite per l'Utente** per risolvere l'errore: suggerimento di attendere, richiesta di riprovare, riferimento a FAQ e/o assistenza clienti, ecc.;
- **Il metodo per la gestione degli errori**: apertura di una richiesta di assistenza attraverso l'Istanza del Wallet, collegamento ad altri canali dettagliati, e così via. Per ulteriori dettagli, si prega di fare riferimento alla sezione :ref:`functionalities:Assistenza all'Utente`.

Di seguito è riportato un elenco non esaustivo dei principali casi di errore, con riferimento all'attore responsabile della loro gestione, per ogni fase dell'Esperienza dell'Utente. L'elenco dettagliato degli errori da gestire per ogni endpoint di interazione con l'Utente è disponibile nelle sezioni dedicate agli errori all'interno di :ref:`Endpoints`.

Errori di Attivazione dell'Istanza del Wallet
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
  :widths: 80 20
  :header-rows: 1

  * - Tipo di errore
    - Attore responsabile
  * - Il dispositivo non supporta la Soluzione Wallet (ad esempio assenza di requisiti minimi di sicurezza o tecnologici)
    - Fornitore di Wallet
  * - I servizi del Fornitore di Wallet non rispondono (ad esempio errori tecnici o mancanza di connessione)
    - Fornitore di Wallet
  * - I servizi del Fornitore di Attestati Elettronici di Dati di Identificazione Personale non rispondono (ad esempio errori tecnici)
    - Fornitore di Attestati Elettronici di Dati di Identificazione Personale
  * - Il processo di Autenticazione sul servizio del Gestore di Identità DIgitale non è riuscito (ad esempio errori tecnici, identità non riconosciuta, ecc.)
    - Gestore di Identità DIgitale

Errori di Rilascio di Attestati Elettronici di Attributi
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
  :widths: 80 20
  :header-rows: 1

  * - Tipo di errore
    - Attore responsabile
  * - L'Istanza del Wallet e/o il PID non sono attivi
    - Fornitore di Wallet
  * - Il servizio per ottenere un Attestato Elettronico di Attributi non è disponibile (ad esempio errori tecnici)
    - Fornitore di Attestati Elettronici di Attributi, Fonte Autentica
  * - L'Utente non è in grado di ottenere un Attestato Elettronico di Attributi specifico nella propria Istanza del Wallet (ad esempio nessuna idoneità, versione fisica non valida o scaduta, ecc.)
    - Fonte Autentica

Errori di Presentazione di Attestati Elettronici
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
  :widths: 80 20
  :header-rows: 1

  * - Tipo di errore
    - Attore responsabile
  * - L'Utente non possiede gli Attributi richiesti contenuti in uno o più Attestati Elettronici all'interno della propria Istanza del Wallet per accedere a un servizio specifico
    - Fornitore di Wallet
  * - I servizi del Fornitore di Wallet o i servizi della Relying Party non rispondono (ad esempio errori tecnici o mancanza di connessione)
    - Fornitore di Wallet, Relying Party

Errori di Gestione degli Attestati Elettronici
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
  :widths: 80 20
  :header-rows: 1

  * - Tipo di errore
    - Attore responsabile
  * - Il servizio per revoca/backup/ripristino di un Attestato Elettronico di Attributi non è disponibile (ad esempio errori tecnici)
    - Fornitore di Attestati Elettronici di Attributi
  * - Il servizio per revoca del PID non è disponibile (ad esempio errori tecnici)
    - Fornitore di Attestati Elettronici di Dati di Identificazione Personale

Errori di Disattivazione dell'Istanza del Wallet
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
  :widths: 80 20
  :header-rows: 1

  * - Tipo di errore
    - Attore responsabile
  * - Il servizio per disattivare l'Istanza del Wallet non è disponibile (ad esempio errori tecnici)
    - Fornitore di Wallet

Oltre alla gestione degli errori, tutti gli Attori Primari DEVONO anche gestire il feedback negativo risultante dalla decisione dell'Utente di abbandonare o annullare un flusso (ad esempio Attivazione, Acquisizione, Presentazione, ecc.). In tali casi, DEVE essere fornito feedback per confermare la scelta dell'Utente, e PUÒ includere una Call to Action per continuare.

Assistenza all'Utente
----------------------

Per una gestione efficace degli errori e la risoluzione di qualsiasi altro problema, gli Attori Primari DEVONO garantire un supporto adeguato all'Utente strutturando un modello di assistenza semplice ed efficace basato sui seguenti principi:

- **Auto-risoluzione**: per consentire all'Utente di consultare le domande frequenti (FAQ) sui contenuti e le funzionalità dell'Istanza del Wallet, al fine di risolvere eventuali casi di errore o problemi in modo indipendente.

- **Segnalazione guidata dei problemi**: per guidare l'Utente attraverso il processo di apertura di un ticket di assistenza, al fine di definire chiaramente il problema e facilitarne la risoluzione.

- **Collaborazione tra attori**: per consentire il coordinamento tra ogni attore coinvolto (Fornitore di Wallet, Fornitore di Attestati Elettronici di Attributi, Fornitore di Attestati Elettronici di Dati di Identificazione Personale e Fonte Autentica), secondo i loro ruoli specifici e le procedure operative.

- **Comunicazione efficiente**: per consentire all'Utente di tracciare lo stato aggiornato della propria richiesta durante tutte le fasi di elaborazione, con comunicazione chiara, continua e coordinata.

Per applicare queste migliori pratiche, gli attori coinvolti DOVREBBERO implementare i seguenti livelli di supporto gerarchici:

	1. **Livello I | Auto-gestione**: il Fornitore di Wallet DOVREBBE consentire all'Utente di accedere a una sezione Domande Frequenti (FAQ) all'interno della propria Istanza del Wallet per chiarire dubbi e risolvere determinati problemi in modo indipendente. Ogni attore DOVREBBE creare FAQ specifiche e risposte corrispondenti riguardo ai dati e alle funzionalità che forniscono al Fornitore di Wallet o nei loro Touchpoint. Per determinati casi di errore, il Fornitore di Wallet DOVREBBE fornire il canale di supporto diretto di un altro attore per facilitare la gestione tempestiva ed evitare l'apertura di una richiesta di assistenza all'interno dell'Istanza del Wallet.

	2. **Livello II | Richiesta di assistenza** dal Fornitore di Wallet: se il Livello I è insufficiente, il Fornitore di Wallet DOVREBBE dare all'Utente la possibilità di aprire una o più richieste di assistenza, eseguire una diagnosi e procedere con la risoluzione del problema, se di loro competenza. Queste richieste DOVREBBERO essere gestite attraverso l'Istanza del Wallet o altri Touchpoint del Fornitore di Wallet. Il Fornitore di Wallet DEVE diagnosticare e risolvere il problema se rientra nella loro responsabilità.

	3. **Livello III | Inoltro della richiesta all'attore responsabile**: se il Livello II è insufficiente, il Fornitore di Wallet DOVREBBE garantire che la richiesta sia inoltrata all'attore responsabile (Fornitore di Attestati Elettronici di Attributi, Fornitore di Attestati Elettronici di Dati di Identificazione Personale o Fonte Autentica), che garantisce la disponibilità di canali back-office dedicati per risolvere il problema e comunicare l'esito all'Utente.

Di seguito sono riportati i requisiti dell'Esperienza dell'Utente che il Fornitore della Soluzione Wallet DEVE garantire attraverso la propria Soluzione Wallet:

- L'Utente accede alle opzioni di assistenza in qualsiasi punto durante l'Esperienza dell'Utente, con una chiara indicazione di come accedervi;
- L'Utente apre una richiesta di assistenza attraverso la propria Istanza del Wallet o altri Touchpoint forniti dal Fornitore di Wallet;
- Quando una richiesta di supporto è aperta, l'Utente riceve conferma tempestiva che la richiesta è stata riconosciuta;
- L'Utente viene informato in anticipo se è necessario presentare i propri dati con terze parti;
- L'Utente viene informato quando una richiesta di assistenza deve essere gestita al di fuori della propria Istanza del Wallet, come su canali di terze parti;
- L'Utente traccia lo stato della richiesta in qualsiasi momento attraverso funzionalità che DEVONO essere rese disponibili dagli attori che gestiscono la richiesta.

Feedback dell'Utente
---------------------

La raccolta di feedback dell'Utente consente di monitorare l'Esperienza dell'Utente, identificare potenziali aree di ottimizzazione e misurare continuamente l'efficacia del servizio. Ogni Fornitore di Wallet DOVREBBE stabilire un sistema strutturato di raccolta feedback per monitorare e migliorare l'Esperienza dell'Utente.

Questo sistema di feedback PUÒ essere alimentato da due diversi tipi di raccolta feedback:

- **Feedback Transazionale** (Customer Effort Score, Customer Satisfaction): raccolto in risposta ad azioni specifiche, come l'aggiunta di un Attestato Elettronico o il completamento di un processo di presentazione e verifica;
- **Feedback Relazionale** (Net Promoter Score): non in connessione con azioni specifiche, raccolto per misurare la percezione complessiva dell'Utente in termini di soddisfazione, fedeltà e probabilità di raccomandare il servizio a utenti terzi.

Ecco alcuni suggerimenti per implementare questi tipi di strumenti di feedback:

**Raccolta Feedback Transazionale**

- **Customer Effort Score (CES)**: Per misurare la facilità d'uso delle funzionalità, POSSONO essere forniti sondaggi, ad esempio, attraverso componenti come modali o pop-up all'interno dell'Istanza del Wallet, attivati alla conclusione di azioni o processi specifici. Gli esempi includono:

	- Dopo aver completato il processo di ottenimento di un Attestato Elettronico;
	- Dopo il processo di Autenticazione, se positivo;
	- Dopo il processo di presentazione, in particolare alla fine della prima opportunità di presentazione e non più di una volta ogni 6 mesi;
	- Dopo i processi di revoca e disattivazione, per esplorare le ragioni dietro queste azioni.

- **Sondaggio di Soddisfazione del Cliente (CSAT)**: Per misurare la soddisfazione complessiva dell'Utente dopo un periodo prolungato di utilizzo dell'Istanza del Wallet, POSSONO essere forniti sondaggi, ad esempio, attraverso modali o pop-up all'interno dell'Istanza del Wallet. Si raccomanda di utilizzare il CSAT a intervalli di non meno di sei mesi e come alternativa al CES, per evitare di sovraccaricare gli Utenti con sondaggi troppo frequenti.

**Raccolta Feedback Relazionale**

- **Net Promoter Score (NPS)**: Per misurare la fedeltà dell'Utente e la probabilità di raccomandare il servizio ad altri, una valutazione PUÒ essere richiesta all'Utente una o due volte all'anno, sia attraverso lo stesso canale di erogazione del servizio (ad esempio l'Istanza del Wallet) o canali esterni come email o SMS. Questo dovrebbe essere allineato con la strategia complessiva di raccolta feedback.

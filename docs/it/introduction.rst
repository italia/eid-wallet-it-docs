.. include:: ../common/common_definitions.rst


Introduzione
============

.. include:: introduction-lead.rst

Grazie al Sistema IT-Wallet, le persone fisiche e giuridiche possono fornire direttamente, tramite il proprio Wallet, le informazioni necessarie per accedere ai servizi offerti da enti pubblici e privati sotto forma di Attestati Elettronici.
Analogamente a un portafoglio fisico, un'Istanza del Wallet può contenere dati relativi all'identità o ai documenti, come la patente di guida o la tessera sanitaria, nonché una vasta gamma di informazioni digitali verificabili, come una qualifica professionale, un diploma di istruzione, una licenza o un attributo certificato.

I principali ruoli nell'ecosistema Wallet sono elencati di seguito:

- **Fornitore di Attestati Elettronici**: soggetti che rilasciano Attestati Elettronici agli Utenti.
- **Verificatori di Attestati Elettronici (Relying Party)**: soggetti che richiedono all'Utente presentazioni di Attestati Elettronici, per finalità di Autenticazione e autorizzazione.
- **Utenti**: individui che possiedono un'Istanza del Wallet e hanno il controllo sugli Attestati Elettronici che possono richiedere, acquisire, memorizzare e presentare alle Relying Party.

In questo modello, il Fornitore di Attestati Elettronici (ad esempio, un'istituzione educativa) fornisce Attestati Elettronici all'Utente, che può memorizzarle nella propria Istanza del Wallet.
L'Istanza del Wallet è tipicamente fornita come applicazione mobile sullo smartphone dell'Utente.

Ciò che distingue questo nuovo approccio dai precedenti sistemi di gestione dell'accesso all'identità è che gli Attestati Elettronici si riferiscono a caratteristiche, qualità o proprietà, già autenticate alla fonte. Questi Attestati Elettronici possono essere utilizzati dall'Utente senza che i Fornitori di Attestati Elettronici siano a conoscenza del loro utilizzo. Durante l'uso degli Attestati Elettronici, nessuna informazione sull'utilizzo viene rilasciata a terze parti poiché la relazione è esclusiva tra l'Utente e la Relying Party, in modo trasparente e informato.
Lo sviluppo del Sistema IT-Wallet include un processo di sperimentazione graduale, finalizzato a testare il Wallet e valutarne l'impatto in contesti reali. Questo processo è progettato per validare componenti tecniche, elementi di esperienza utente e meccanismi di interoperabilità, garantendo al contempo un'adozione progressiva e controllata del Sistema. Inoltre, supporta il miglioramento continuo del Sistema IT-Wallet e il suo graduale allineamento con il Portafoglio Europeo di Identità Digitale (EUDI Wallet), sia in termini di architettura che di conformità con le specifiche europee in evoluzione.

Altri elementi chiave che caratterizzano questo nuovo paradigma di Portafoglio di Identità Digitale includono:

- **Riservatezza e controllo**: i Wallet consentono agli individui di mantenere il controllo sulle informazioni fornite all'interno degli Attestati Elettronici presentate. Possono scegliere quali attributi o Attestati Elettronici presentare e a chi.
- **Sicurezza**: i Wallet sfruttano meccanismi crittografici per l'integrità e la sicurezza dei dati scambiati. Ciò evita il furto di identità, le frodi e gli accessi non autorizzati.
- **Interoperabilità**: i Wallet promuovono l'interoperabilità consentendo a diversi sistemi e organizzazioni di riconoscere e verificare le identità, abilitando interazioni affidabili tra individui, organizzazioni e persino oltre i confini.
- **Efficienza e riduzione dei costi**: gli individui possono gestire facilmente i propri Attestati Elettronici, evitare di gestire più token di identità e ridurre i processi ripetitivi di verifica dell'identità.

Ambito
------

Queste Specifiche Tecniche saranno periodicamente aggiornate, ove necessario, alla luce dei risultati della fase di sperimentazione, dell'adozione di nuovi atti legislativi nazionali o europei e dei requisiti in evoluzione in termini di sicurezza e interoperabilità. Queste Specifiche Tecniche perseguono due obiettivi principali e rappresentano una componente fondamentale del quadro di implementazione per il Sistema IT-Wallet.

Il primo obiettivo è quello di fornire un insieme chiaro e strutturato di raccomandazioni, risorse e requisiti di progettazione relativi agli elementi del Sistema IT-Wallet che impattano sull'Esperienza dell'Utente.
Il documento, distinguendo tra aspetti normativi obbligatori e buone pratiche progettuali e implementative, mira a fornire agli enti pubblici e privati interessati a partecipare al Sistema IT-Wallet quanto necessario per:

- facilitare la comprensione e l'adozione del Modello di Servizio, aumentando il numero di potenziali servizi e opportunità di utilizzo per l'Utente.
- adottare l'Identità Visiva del Sistema IT-Wallet al fine di migliorarne l'affidabilità e la riconoscibilità per l'Utente.
- garantire la coerenza di progettazione tra macro-funzionalità e singole interazioni tra l'Utente e i Touchpoint del servizio.
- mantenere un adeguato livello di qualità, promuovendo i principi di usabilità, accessibilità e inclusività.


Il secondo focus è definire l'architettura tecnica e il quadro di riferimento che servirà da linea guida per tutte le parti coinvolte nello sviluppo delle Soluzioni Tecniche del Sistema IT-Wallet.

La documentazione, gli strumenti e le risorse aggiuntive - di seguito definite Risorse Ufficiali - per la progettazione e lo sviluppo delle Soluzioni Tecniche del Sistema IT-Wallet saranno presto disponibili nella sezione :ref:`official-resources:Risorse Ufficiali`: e saranno aggiornate periodicamente.

Linguaggio Normativo e Convenzioni
----------------------------------

Le parole chiave "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY" e "OPTIONAL" in questo documento devono essere interpretate come descritto in BCP 14 [RFC2119] [RFC8174] quando, e solo quando, appaiono in maiuscolo, come mostrato qui.
Nel testo italiano, le forme interamente in maiuscolo elencate in :ref:`defined-terms:Linguaggio Normativo e Convenzioni` hanno lo stesso significato delle parole chiave inglesi corrispondenti.

.. include:: how-to-read-spec.rst



.. include:: ../common/common_definitions.rst


Introduzione
============

In Italia, il Decreto-Legge n. 19 del 2 marzo 2024, convertito, con modificazioni, dalla Legge n. 56 del 29 aprile 2024, ha introdotto l'articolo 64-quater del Decreto Legislativo n. 82 del 7 marzo 2005, istituendo il Sistema di Portafoglio Digitale Italiano - Sistema IT-Wallet. Il Sistema IT-Wallet consente a **cittadini e imprese** di accedere a servizi pubblici e privati attraverso la presentazione sicura di Attestati Elettronici, attestanti diritti, deleghe, caratteristiche, licenze o qualifiche. L'articolo 64-quater prevede inoltre l'adozione di uno o più decreti attuativi per definire le regole che disciplinano il funzionamento del Sistema IT-Wallet, compresi i ruoli delle entità coinvolte, i requisiti tecnici e di sicurezza, e i principi di sostenibilità economica, di cui queste Specifiche Tecniche – redatte attraverso un processo aperto e collaborativo – costituiscono parte integrante.

Grazie al Sistema IT-Wallet, **cittadini e imprese** possono fornire, tramite il proprio Wallet, le informazioni necessarie per accedere ai servizi offerti da enti pubblici e privati sotto forma di Attestati Elettronici. Analogamente a un portafoglio fisico, un'Istanza del Wallet può contenere dati relativi all'identità o ai documenti, come la patente di guida o la tessera sanitaria, nonché una vasta gamma di informazioni digitali verificabili, come una qualifica professionale, un diploma di istruzione, una licenza o un attributo certificato.

I principali ruoli nell'ecosistema Wallet sono elencati di seguito:

- **Credential Issuer**: enti che rilasciano Attestati Elettronici agli Utenti;
- **Relying Party**: enti che richiedono all'Utente la presentazione di Attestati Elettronici per finalità di Autenticazione e autorizzazione;
- **Utente**: persona che possiede un'Istanza del Wallet e controlla gli Attestati Elettronici che può richiedere, acquisire, memorizzare e presentare alle Relying Party.

In questo modello, il Credential Issuer (ad esempio, un'istituzione educativa) fornisce Attestati Elettronici all'Utente, che può memorizzarli nella propria Istanza del Wallet.
L'Istanza del Wallet è tipicamente fornita come applicazione mobile sullo smartphone dell'Utente.

Ciò che distingue questo nuovo approccio dai precedenti sistemi di gestione dell'accesso all'identità è che gli Attestati Elettronici si riferiscono a caratteristiche, qualità o proprietà, già autenticate alla fonte. Questi Attestati Elettronici possono essere utilizzati dall'Utente senza che i Credential Issuer siano a conoscenza del loro utilizzo. Durante l'uso degli Attestati Elettronici, nessuna informazione sull'utilizzo viene rilasciata a terze parti poiché la relazione è esclusiva tra l'Utente e la Relying Party, in modo trasparente e informato.
Un processo di sperimentazione graduale valida componenti tecniche, esperienza utente e interoperabilità e sostiene l'allineamento progressivo con il Portafoglio Europeo di Identità Digitale (EUDI Wallet).

Altri elementi chiave che caratterizzano questo nuovo paradigma di Portafoglio di Identità Digitale includono:

- **Privacy e controllo**: i Wallet consentono agli individui di mantenere il controllo sulle informazioni fornite all'interno degli Attestati Elettronici presentati. Possono scegliere quali attributi o Attestati Elettronici presentare e a chi;
- **Sicurezza**: i Wallet sfruttano meccanismi crittografici per l'integrità e la sicurezza dei dati scambiati. Ciò evita il furto di identità, le frodi e gli accessi non autorizzati;
- **Interoperabilità**: i Wallet promuovono l'interoperabilità consentendo a diversi sistemi e organizzazioni di riconoscere e verificare le identità, abilitando interazioni affidabili tra individui, organizzazioni e persino oltre i confini;
- **Efficienza e riduzione dei costi**: gli individui possono gestire facilmente i propri Attestati Elettronici, evitare di gestire più token di identità e ridurre i processi ripetitivi di verifica dell'identità.

Ambito
------

Queste Specifiche Tecniche completano le Linee Guida previste dall'articolo 64-quater del Decreto Legislativo n. 82/2005 (CAD). Una volta formalmente adottate, entrano nel quadro normativo del Sistema IT-Wallet e vengono aggiornate con l'avanzare della sperimentazione, della legislazione e dei requisiti.

Indipendentemente dal ruolo, chi implementa dovrebbe tenere presente quanto segue:

- **Allineamento normativo**: le Specifiche attuano il quadro nazionale ed europeo applicabile e DEVONO essere considerate nello sviluppo delle Soluzioni Tecniche IT-Wallet.
- **Documento aperto e vivo**: le Specifiche sono sviluppate in modo collaborativo, pubblicate come documentazione aperta e riviste con l'evolversi dell'ecosistema.
- **Obblighi e buone pratiche**: il testo distingue prescrizioni obbligatorie da raccomandazioni, anche in materia di **Sicurezza**, **Privacy** e **Interoperabilità**.

Le Specifiche integrano anche raccomandazioni di Esperienza Utente, risorse di progettazione e l'architettura tecnica per gli Attori Primari. Le Risorse Ufficiali sono in :ref:`official-resources:Risorse Ufficiali` e vengono aggiornate nel tempo.

Per percorsi di lettura per ruolo, vedere :ref:`introduction:Come leggere le Specifiche`. 

Linguaggio Normativo e Convenzioni
----------------------------------

Le parole chiave "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY" e "OPTIONAL" in questo documento devono essere interpretate come descritto in BCP 14 [RFC2119] [RFC8174] quando, e solo quando, appaiono in maiuscolo, come mostrato qui.

.. include:: how-to-read-spec.rst

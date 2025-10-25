# **Linee Guida Sistema IT-Wallet**

ai sensi dell'articolo 64-quater, comma 3 del CAD

**per la fase di sperimentazione**

Versione 1.0 del XX.XX.2025

| Versione | Data | Tipologia<br>modifica |
|----------|------|-----------------------|
|----------|------|-----------------------|

| 1.0 | XX.XX.2025 | Prima emissione. |
|-----|------------|------------------|
|-----|------------|------------------|

# Sommario

| 1.   | Int   | roduzione                                                                                 | . 1 |
|------|-------|-------------------------------------------------------------------------------------------|-----|
| 1.1. | ]     | Normativa di riferimento                                                                  | . 1 |
| 1.2. | ]     | Finalità                                                                                  | . 2 |
| 1.3. |       | Soggetti Destinatari                                                                      | . 2 |
| 1.4. | ]     | Note di lettura                                                                           | . 2 |
| 1.5. | (     | Glossario                                                                                 | .3  |
| 1.6. | (     | Gruppo di lavoro                                                                          | .7  |
| 2.   | 11 \$ | Sistema IT-Wallet                                                                         | .7  |
| 2.1. | ]     | Principi generali                                                                         | .7  |
| 2.2. | ]     | Ruoli nel Sistema IT-Wallet                                                               | . 8 |
| 2.2  | 2.1.  | Utente                                                                                    | . 8 |
| 2.2  | 2.2.  | Fornitori di Soluzione IT-Wallet                                                          | . 8 |
| 2.2  | 2.3.  | Fornitore di Attestati Elettronici di Dati di Identificazione Personale                   | .9  |
| 2.2  | 2.4.  | Fornitori di Attestati Elettronici di Attributi                                           | .9  |
| 2.2  | 2.5.  | Titolari di Fonte Autentica                                                               | 10  |
| 2.2  | 2.6.  | Fornitore del Registro IT-Wallet                                                          | 10  |
| 2.2  | 2.7.  | Verificatori di Attestati Elettronici                                                     | 11  |
| 3.   | Fu    | nzionalità primarie                                                                       | 12  |
| 3.1. |       | Attivazione Istanza IT-Wallet                                                             | 12  |
| 3.2. | (     | Ottenimento di Attestati Elettronici di Dati di Identificazione Personale                 | 13  |
| 3.3. | (     | Ottenimento Attestati Elettronici di Attributi                                            | 14  |
| 3.4. | ]     | Revoca e sospensione                                                                      | 14  |
| 3.4  | 4.1.  |                                                                                           |     |
| 3.5. | L     | Archiviazione e ripristino degli Attestati Elettronici di Attributi e Storico Transazioni |     |
| 3.6. |       | Presentazione e verifica di Attestati Elettronici                                         |     |
| 3.   | 6.1.  |                                                                                           |     |
|      | 6.2.  |                                                                                           |     |
| 3.7. |       | Richiesta Cancellazione Dati di Identificazione Personali e Attributi presentati          |     |
| 4.   |       | chitettura e requisiti del Sistema IT-Wallet                                              |     |

| 4.1. | Requisiti<br>delle<br>Soluzioni<br>IT-Wallet                                                                                               | 20 |
|------|--------------------------------------------------------------------------------------------------------------------------------------------|----|
| 4.2. | Requisiti<br>delle<br>soluzioni<br>del<br>Fornitore<br>di<br>Attestati<br>Elettronici<br>di<br>Dati<br>di Identificazione<br>Personale<br> | 22 |
| 4.3. | Requisiti<br>delle<br>soluzioni<br>dei<br>Fornitori<br>di<br>Attestati<br>Elettronici<br>di<br>Attributi<br>                               | 23 |
| 4.4. | Requisiti<br>delle<br>soluzioni<br>dei<br>Verificatori<br>di<br>Attestati<br>Elettronici                                                   | 24 |
| 4.5. | Requisiti<br>delle<br>soluzioni<br>dei<br>Titolari<br>di<br>Fonti<br>Autentiche<br>                                                        | 25 |
| 4.6. | Registro<br>del<br>Sistema<br>IT-Wallet<br>                                                                                                | 26 |

## <span id="page-4-0"></span>**1. Introduzione**

Nell'ultimo decennio, la digitalizzazione ha trasformato radicalmente le modalità con cui cittadini e imprese interagiscono con servizi pubblici e privati, introducendo nuove forme di accesso ai servizi, sicure, accessibili e di facile utilizzo.

In Italia, con il Decreto-Legge 2 marzo 2024, n. 19, convertito, con modificazioni, dalla legge 29 aprile 2024, n. 56 è stato introdotto l'articolo 64-quater del decreto legislativo 7 marzo 2005, n. 82 che ha istituito il *Sistema di portafoglio digitale italiano - Sistema IT-Wallet*. Il Sistema IT-Wallet consente alle persone fisiche o giuridiche di accedere a servizi pubblici e privati grazie alla presentazione sicura dei propri dati relativi a prerogative, deleghe, caratteristiche, licenze o qualità sotto forma di Attestati Elettronici.

Mediante il Sistema IT-Wallet le persone fisiche e giuridiche possono fornire direttamente, tramite il loro portafoglio digitale, le informazioni richieste per l'Autenticazione sotto forma di Attestati Elettronici. Analogamente a un portafoglio fisico, l'IT-Wallet può contenere informazioni relative all'identità o a documenti, come ad esempio la patente di guida o la tessera sanitaria, e una vasta gamma di informazioni digitali verificabili, come ad esempio una qualifica professionale, un titolo di studio, una licenza o una qualità personale.

L'elemento distintivo del Sistema IT-Wallet rispetto ai precedenti sistemi di Autenticazione, è che gli Attestati Elettronici si riferiscono a caratteristiche, qualità o proprietà, già autenticate alla fonte. Questi Attestati Elettronici possono essere utilizzati dall'Utente senza che gli emettitori degli Attestati Elettronici vengano a conoscenza dell'utilizzo di questi. Durante l'utilizzo degli Attestati Elettronici, non viene rilasciata alcuna informazione d'uso a terze parti in quanto il rapporto è esclusivo tra l'Utente e la parte a cui vengono presentati gli Attestati Elettronici in maniera consapevole e trasparente per l'Utente stesso.

#### <span id="page-4-1"></span>**1.1. Normativa di riferimento**

Sono riportati di seguito gli atti normativi e i rispettivi acronimi contenuti nelle presenti Linee Guida:

• [CAD] Decreto legislativo 7 marzo 2005 n. 82 e ss. mm. ii., recante "Codice dell'amministrazione digitale";

- [LG INTEROP] Linee guida sull'interoperabilità tecnica delle Pubbliche Amministrazioni;
- [LG PDND] Linee guida sull'infrastruttura tecnologica della Piattaforma Digitale Nazionale Dati per l'interoperabilità dei sistemi informativi e delle basi di dati;

## <span id="page-5-0"></span>**1.2. Finalità**

Le presenti Linee Guida forniscono un quadro di riferimento per l'implementazione del Sistema IT-Wallet nel periodo di sperimentazione, delineando principi generali e indirizzi operativi per la sua adozione da parte dei Soggetti Pubblici e Privati partecipanti alla sperimentazione.

Le Linee Guida sono integrate da Specifiche Tecniche di dettaglio, elaborate in modalità aperta e collaborativa, che definiscono i requisiti per l'interoperabilità, la sicurezza e il design del Sistema IT-Wallet e rappresentano il riferimento per gli operatori che intendono utilizzarlo, in linea con l'evoluzione attuale degli standard riconosciuti. Tali Specifiche Tecniche sono pubblicate separatamente sul sito istituzionale [www.wallet.gov.it,](http://www.wallet.gov.it/) garantendo trasparenza e accessibilità agli operatori interessati.

Esse costituiscono un primo riferimento operativo e saranno aggiornate progressivamente in funzione dell'evoluzione normativa e tecnologica, in vista del pieno adeguamento alle disposizioni del Regolamento (UE) n. 910/2014 del Parlamento Europeo e del Consiglio. L'aggiornamento avverrà in coordinamento con le istituzioni nazionali ed europee, assicurando l'integrazione del Sistema IT-Wallet con le infrastrutture di identità digitale dell'Unione Europea.

### <span id="page-5-1"></span>**1.3. Soggetti Destinatari**

I soggetti destinatari delle presenti Linee Guida sono:

- la società di cui all'articolo 1 del decreto legislativo 21 aprile 1999, n. 116;
- la società di cui all'articolo 8, comma 2, del decreto-legge 14 dicembre 2018, n. 135, convertito, con modificazioni, dalla legge 11 febbraio 2019, n. 12;
- i Soggetti Pubblici e i Soggetti Privati interessati alla sperimentazione del Sistema IT-Wallet.

#### <span id="page-5-2"></span>**1.4. Note di lettura**

Conformemente alla RFC 2119 per la stesura dei documenti tecnici le presenti Linee Guida e i documenti tecnici ad essa allegati utilizzeranno le parole chiave «DEVE», «DEVONO», «NON

DEVE», «NON DEVONO», «DOVREBBE», «NON DOVREBBE», «PUÒ», «POSSONO» e «OPZIONALE», la cui interpretazione è descritta di seguito:

- DEVE o DEVONO, indicano un requisito obbligatorio per rispettare la linea guida;
- NON DEVE o NON DEVONO, indicano un assoluto divieto delle specifiche;
- DOVREBBE o NON DOVREBBE, indicano che le implicazioni devono essere comprese e attentamente pesate prima di scegliere approcci alternativi;
- PUÒ, POSSONO o l'aggettivo OPZIONALE, indica che il lettore può scegliere di applicare o meno senza alcun tipo di implicazione la specifica.

#### <span id="page-6-0"></span>**1.5. Glossario**

Di seguito si riporta il glossario dei termini definiti dalle presenti Linee Guida insieme all'acronimo utilizzato, ove presente. Per i termini che non sono definiti in questo glossario e nelle Specifiche Tecniche (ad esempio Portafoglio Europeo di Identità Digitale, Mezzo di Identificazione Elettronica, etc.), si rimanda al termine corrispondente definito dal Regolamento eIDAS.

| Termine                                     | Definizione                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|---------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Attestato<br>Elettronico                    | Un<br>insieme<br>di<br>Dati<br>di<br>Identificazione<br>Personale<br>o<br>Attributi<br>firmato digitalmente, resistente alla manomissione e non<br>ripudiabile da chi lo ha emesso.                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Attestato<br>Elettronico<br>di<br>Attributi | Un Attestato Elettronico che permette di Autenticare le<br>caratteristiche,<br>le<br>qualità,<br>i<br>diritti<br>o<br>le<br>autorizzazioni<br>di<br>una<br>persona<br>fisica<br>o<br>giuridica<br>o<br>di<br>un<br>oggetto<br>o<br>anche<br>una<br>sola<br>di queste informazioni.                                                                                                                                                                                                                                                                                                                          |
|                                             | Un<br>Attestato Elettronico di<br>Attributi PUÒ essere definito<br>Attestato Elettronico di Attributi Pubblici quando<br>contiene<br>Attributi derivanti da una Fonte<br>Autentica il cui<br>Titolare di Fonte Autentica è un Soggetto Pubblico e<br>Attestato Elettronico di Interesse Pubblico quando<br>contiene<br>Attributi destinati ad<br>attestare<br>il rilascio, da<br>parte<br>dello Stato o di altre pubbliche amministrazioni, di<br>autorizzazioni,<br>certificazioni,<br>abilitazioni,<br>documenti<br>di<br>identità<br>e<br>riconoscimento,<br>ricevute<br>di<br>introiti,<br>ovvero<br>ad |

|                                                                           | assumere un valore fiduciario e di tutela della fede<br>pubblica<br>in<br>seguito<br>alla<br>loro<br>emissione<br>o<br>alle<br>scritturazioni<br>su<br>di<br>essi<br>effettuate<br>e,<br>in<br>generale,<br>quando<br>sono<br>considerati<br>carte valori ai sensi dell'articolo 2, comma 10-bis, della<br>legge 13 luglio 1966, n. 559.                                                   |
|---------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Attestato<br>Elettronico<br>di<br>Dati<br>di<br>Identificazione Personale | Un<br>Attestato<br>Elettronico<br>che<br>consente<br>di<br>Autenticare<br>il<br>soggetto a cui i Dati di Identificazione Personale sono<br>riferiti.                                                                                                                                                                                                                                       |
| Attori<br>Primari                                                         | L'insieme dei Soggetti Pubblici e Soggetti Privati che<br>realizzano<br>le Soluzioni<br>Tecniche per il<br>funzionamento<br>del<br>Sistema IT-Wallet.                                                                                                                                                                                                                                      |
| Attributi                                                                 | Un<br>insieme<br>di<br>caratteristiche,<br>qualità,<br>diritti<br>o<br>autorizzazioni di una persona fisica o giuridica o di un<br>oggetto o anche una sola di queste informazioni.                                                                                                                                                                                                        |
| Autenticazione                                                            | Ai sensi dell'articolo<br>3,<br>paragrafo<br>1,<br>n.<br>5<br>del Regolamento<br>eIDAS,<br>un<br>processo<br>elettronico<br>che<br>consente<br>di<br>confermare l'Identificazione Elettronica di una persona<br>fisica o giuridica, oppure l'origine e l'integrità di dati in<br>forma elettronica (nel contesto delle Linee Guida, ad<br>esempio, gli Attributi)                          |
| Catalogo<br>degli<br>Attestati Elettronici                                | Un<br>catalogo<br>elettronico<br>contenente<br>informazioni<br>relative<br>ai<br>formati e agli schemi degli<br>Attestati Elettronici, ai dati in<br>essi<br>contenuti<br>e<br>alle<br>Fonti<br>Autentiche.<br>Il<br>Catalogo<br>contiene<br>informazioni<br>aggiuntive<br>che<br>consentono<br>di<br>stabilire<br>l'autenticità e l'affidabilità delle informazioni in esso<br>contenute. |
| Dati<br>di<br>Identificazione<br>Personale                                | Un insieme di dati rilasciato conformemente alle presenti<br>Linee Guida che consente di stabilire l'identità di una<br>persona fisica o giuridica, o di una persona fisica che<br>rappresenta<br>un'altra<br>persona<br>fisica<br>o<br>una<br>persona<br>giuridica.                                                                                                                       |
| Divulgazione<br>Selettiva                                                 | Funzionalità che consente all'Utente di presentare un<br>sottoinsieme<br>di<br>Dati<br>di<br>Identificazione<br>Personale<br>o<br>Attributi inclusi in uno o più Attestati Elettronici.                                                                                                                                                                                                    |

| Fonte<br>Autentica                                                                     | Un archivio o un sistema, tenuto sotto la responsabilità di<br>un Titolare di Fonte Autentica, che è considerato fonte<br>primaria per gli Attributi o per i Dati di Identificazione<br>Personale<br>e<br>la<br>cui<br>autenticità<br>è<br>riconosciuta<br>conformemente al diritto unionale o<br>nazionale, inclusa la<br>prassi amministrativa.                                                                                                     |
|----------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Fornitore<br>del<br>Registro<br>IT-Wallet                                              | Soggetto<br>responsabile<br>della<br>realizzazione<br>e<br>gestione<br>dell'infrastruttura tecnologica del Registro IT-Wallet ai<br>sensi dell'articolo 64-quater del CAD                                                                                                                                                                                                                                                                             |
| Fornitore<br>di<br>Attestati<br>Elettronici<br>di<br>Attributi                         | Soggetto<br>Pubblico<br>o<br>Soggetto<br>Privato<br>che<br>rilascia<br>Attestati<br>Elettronici di Attributi, secondo la normativa, inclusi i<br>Fornitori Qualificati di<br>Attestati Elettronici di<br>Attributi ai<br>sensi del Regolamento eIDAS.                                                                                                                                                                                                 |
|                                                                                        | Il<br>Fornitore<br>di<br>Attestati<br>Elettronici<br>di<br>Attributi<br>PUÒ<br>essere<br>definito Fornitore di Attestati Elettronici di Interesse<br>Pubblico per il soggetto designato dalla normativa per il<br>rilascio di Attestati Elettronici di Interesse Pubblico ai<br>sensi dell'articolo 64-quater del CAD.                                                                                                                                |
| Fornitore<br>di<br>Attestati<br>Elettronici<br>di<br>Dati di Identificazione Personale | Soggetto<br>responsabile<br>dell'emissione<br>di<br>Attestati<br>Elettronici di Dati di Identificazione Personale designato<br>dalla normativa per il rilascio di Attestati Elettronici di<br>Dati di Identificazione Personale ai sensi dell'articolo 64-<br>quater del CAD.                                                                                                                                                                         |
| Fornitore<br>di<br>Soluzione<br>IT-Wallet                                              | Soggetto Pubblico o Soggetto Privato che fornisce una<br>Soluzione IT-Wallet.<br>Il Fornitore di Soluzione IT-Wallet PUÒ essere definito<br>Fornitore di Soluzione IT-Wallet Pubblica per la<br>Soluzione<br>IT-Wallet<br>di<br>cui<br>all'articolo<br>64-quater,<br>comma<br>2,<br>del<br>CAD<br>o<br>Fornitore<br>di<br>Soluzione<br>IT-Wallet<br>Privata<br>per<br>le<br>Soluzioni<br>IT-Wallet<br>rese<br>disponibile<br>dai<br>Soggetti Privati. |
| Istanza<br>IT-Wallet                                                                   | Un'istanza<br>della<br>Soluzione<br>IT-Wallet<br>controllata<br>dall'Utente che consente l'ottenimento e la gestione degli<br>Attestati Elettronici riferiti all'Utente stesso.                                                                                                                                                                                                                                                                       |
| Livello<br>di Garanzia                                                                 | Indicatore del grado di affidabilità dell'Autenticazione,<br>determinato in conformità all' all'articolo 8 del<br>Regolamento eIDAS secondo i seguenti livelli: Livello di<br>Garanzia<br>Basso,<br>Livello<br>di<br>Garanzia<br>Significativo,<br>Livello<br>di Garanzia Elevato.                                                                                                                                                                    |

| Piattaforma<br>Digitale<br>Nazionale<br>Dati (PDND) | La piattaforma di cui al comma 2, articolo 50-ter del<br>CAD,<br>d.lgs.<br>7<br>marzo<br>2005<br>n.<br>82,<br>regolamentata<br>dalle<br>[LG<br>PDND].                                                                                                                                                                                                                                                                                                                                                                  |  |  |  |  |
|-----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|--|--|
| Registro<br>del<br>Sistema<br>IT-Wallet             | Registro<br>contenente<br>l'elenco<br>dei<br>Soggetti<br>Pubblici<br>e<br>Soggetti Privati che sono registrati al Sistema IT-Wallet.                                                                                                                                                                                                                                                                                                                                                                                   |  |  |  |  |
| Soggetti<br>Aggregatori                             | Soggetti<br>Pubblici<br>o<br>Soggetti<br>Privati,<br>registrati<br>nel<br>Registro<br>IT-Wallet,<br>che<br>offrono<br>e<br>gestiscono,<br>in<br>nome<br>e<br>per<br>conto<br>di<br>un Verificatore di Attestati Elettronici, le Soluzioni<br>Tecniche per la verifica da remoto o in prossimità di<br>Attestati Elettronici.                                                                                                                                                                                           |  |  |  |  |
| Soggetti<br>Privati                                 | Soggetti<br>diversi<br>dai<br>Soggetti<br>Pubblici.                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |  |  |  |  |
| Soggetti<br>Pubblici                                | Soggetti<br>di<br>cui<br>all'articolo<br>2,<br>comma<br>2,<br>del<br>CAD.                                                                                                                                                                                                                                                                                                                                                                                                                                              |  |  |  |  |
| Soluzione<br>IT-Wallet                              | Insieme<br>delle<br>Soluzioni<br>Tecniche<br>necessarie<br>per<br>il<br>corretto<br>funzionamento delle Istanze IT-Wallet, realizzate ai sensi<br>dell'articolo 64-quater del CAD.<br>La<br>Soluzione<br>IT-Wallet<br>PUÒ<br>essere<br>definita<br>Soluzione<br>IT<br>Wallet Pubblica per la Soluzione IT-Wallet di cui<br>all'articolo<br>64-quater,<br>comma<br>2,<br>del<br>CAD<br>o<br>Soluzioni<br>IT<br>Wallet<br>Private<br>per<br>le<br>Soluzioni<br>IT-Wallet<br>rese<br>disponibile<br>dai Soggetti Privati. |  |  |  |  |
| Soluzioni<br>Tecniche                               | Insieme<br>dei<br>sistemi<br>hardware<br>e<br>software<br>e<br>dei<br>servizi<br>realizzati dai Fornitori di Soluzioni IT-Wallet, dal<br>Fornitore di<br>Attestati Elettronici di Dati di Identificazione<br>Personale,<br>dai<br>Fornitori<br>di<br>Attestati<br>Elettronici<br>di<br>Attributi,<br>dai<br>Verificatori<br>di<br>Attestati<br>Elettronici<br>e<br>dai<br>Soggetti<br>Aggregatori.                                                                                                                     |  |  |  |  |
| Titolare<br>di<br>Fonte<br>Autentica                | Soggetto<br>Pubblico<br>o<br>Soggetto<br>Privato<br>responsabile<br>della<br>Fonte<br>Autentica.                                                                                                                                                                                                                                                                                                                                                                                                                       |  |  |  |  |
| Utente                                              | Una persona fisica o giuridica, o una persona fisica che<br>rappresenta<br>un'altra<br>persona<br>fisica<br>o<br>una<br>persona<br>giuridica,<br>che utilizza il Sistema IT-Wallet ed è titolare di almeno<br>un'Istanza IT-Wallet.                                                                                                                                                                                                                                                                                    |  |  |  |  |
| Verificatore<br>di<br>Attestati<br>Elettronici      | Soggetto Pubblico o Soggetto Privato che si affida al<br>Sistema<br>IT-Wallet<br>per<br>l'Autenticazione<br>dei<br>Dati<br>di<br>Identificazione Personale e degli Attributi degli Utenti.<br>In questo contesto, il termine "Verificatore di Attestati<br>Elettronici"<br>identifica<br>anche<br>i<br>fornitori<br>di<br>servizi<br>digitali<br>e,                                                                                                                                                                    |  |  |  |  |

| in<br>generale,<br>letteralmente            | le<br>quali | cosiddette<br>"Parte | Relying<br>facente | Party<br>affidamento | (tradotto<br>sulla |
|---------------------------------------------|-------------|----------------------|--------------------|----------------------|--------------------|
| certificazione"                             | o           | "Parte               | facente            | affidamento          | sul                |
| Portafoglio"), di cui al Regolamento eIDAS. |             |                      |                    |                      |                    |

#### <span id="page-10-0"></span>**1.6. Gruppo di lavoro**

La redazione del presente documento è stata curata dall'Agenzia per l'Italia Digitale, dal Dipartimento per la trasformazione digitale della Presidenza del Consiglio dei ministri e dall'Agenzia per la Cybersicurezza Nazionale.

## <span id="page-10-1"></span>**2. Il Sistema IT-Wallet**

## <span id="page-10-2"></span>**2.1. Principi generali**

Il Sistema IT-Wallet introduce modalità e tecnologie innovative per l'Autenticazione delle persone fisiche e giuridiche.

Nell'ambito del Sistema IT-Wallet, una Istanza IT-Wallet contiene Attestati Elettronici di un Utente di cui un Verificatore di Attestati Elettronici può avvalersi per l'Autenticazione dei Dati di Identificazione Personale e degli Attributi dell'Utente.

Il Sistema IT-Wallet implementa un modello federativo nel quale l'Utente interagisce tramite la propria Istanza IT-Wallet direttamente con i Verificatori di Attestati Elettronici senza alcuna intermediazione da parte di soggetti terzi. A tal fine l'Utente dispone di una Istanza IT-Wallet mediante la quale:

- richiede e ottiene Attestati Elettronici che possono contenere Dati di Identificazione Personale o Attributi;
- presenta gli Attestati Elettronici ai Verificatori di Attestati Elettronici per l'Autenticazione dei Dati di Identificazione Personale e degli Attributi.

Il Sistema IT-Wallet si basa sui seguenti principi:

• la confidenzialità, integrità, disponibilità e autenticità dei dati conservati, trasmessi o elaborati a riposo e delle comunicazioni tra gli Attori Primari del Sistema IT-Wallet;

- la non ripudiabilità delle interazioni tra gli Attori Primari del Sistema IT-Wallet;
- il controllo esclusivo da parte degli Utenti, la non manomissione e non duplicazione degli Attestati Elettronici e del materiale crittografico;
- l'accessibilità e l'usabilità delle Soluzioni IT-Wallet in conformità alla normativa nazionale in materia di accessibilità degli strumenti informatici.

## <span id="page-11-0"></span>**2.2. Ruoli nel Sistema IT-Wallet**

Il Sistema IT-Wallet coinvolge diversi Attori Primari, ciascuno dei quali con specifici ruoli e responsabilità, coinvolti direttamente durante le fasi di interazione con l'Utente. Tali Attori Primari operano sotto la supervisione delle autorità pubbliche competenti, incaricate di garantire l'affidabilità degli stessi e la sicurezza delle Soluzioni Tecniche da essi sviluppate.

#### <span id="page-11-1"></span>**2.2.1. Utente**

L'Utente svolge un ruolo centrale nel Sistema IT-Wallet. Mediante una Istanza IT-Wallet, l'Utente interagisce direttamente con il Fornitore della Soluzione IT-Wallet per gestire la propria Istanza IT-Wallet o per richiedere assistenza, con il Fornitore di Attestati Elettronici di Dati di Identificazione Personale e con i Fornitori di Attestati Elettronici di Attributi, al fine di richiedere e ottenere gli Attestati Elettronici e con i Verificatori di Attestati Elettronici per la presentazione di tali Attestati Elettronici finalizzata all'Autenticazione dei Dati di Identificazione Personale e degli Attributi.

In virtù del ruolo centrale che l'Utente svolge nel Sistema IT-Wallet, l'Utente DEVE attivare, accedere e gestire la propria istanza IT-Wallet sotto il suo esclusivo controllo.

#### <span id="page-11-2"></span>**2.2.2. Fornitori di Soluzione IT-Wallet**

I Fornitori di Soluzione IT-Wallet hanno la responsabilità della realizzazione, della conduzione operativa e della manutenzione della Soluzione IT-Wallet da essi fornita e dell'infrastruttura a supporto.

In particolare, i Fornitori di Soluzione IT-Wallet DEVONO assicurare:

• l'affidabilità e l'operatività della Soluzione IT-Wallet, comprese le Istanze IT-Wallet degli Utenti, nonché delle Soluzioni Tecniche a supporto;

- la conformità di sicurezza dei dispositivi e dell'Istanza IT-Wallet sotto il controllo degli Utenti;
- l'accessibilità e l'usabilità della Soluzione IT-Wallet che comprende sia l'Istanza IT-Wallet che le Soluzioni Tecniche a supporto degli Utenti.

#### <span id="page-12-0"></span>**2.2.3. Fornitore di Attestati Elettronici di Dati di Identificazione Personale**

Il Fornitore di Attestati Elettronici di Dati di Identificazione Personale ha la responsabilità dell'emissione e del ciclo di vita degli Attestati Elettronici di Dati di Identificazione Personale. Il Fornitore di Attestati Elettronici di Dati DEVE assicurare che i Dati di Identificazione Personale rappresentino in modo univoco l'Utente e l'associazione tra l'Istanza IT-Wallet e l'Utente che ha effettuato la richiesta.

Il Fornitore di Attestati Elettronici di Dati di Identificazione Personale realizza e gestisce l'infrastruttura tecnologica nonché le Soluzioni Tecniche necessarie per l'emissione e la gestione del ciclo di vita dei Dati di Identificazione Personale. Il Fornitore di Attestati Elettronici di Dati di Identificazione Personale DEVE assicurare il Livello di Garanzia dell'Autenticazione propedeutica alla fase di emissione degli Attestati Elettronici secondo la normativa.

Il Fornitore di Attestati Elettronici di Dati di Identificazione Personale, in qualità di responsabile dell'infrastruttura di emissione e delle Soluzioni Tecniche a supporto, DEVE assicurare la continuità operativa garantendo il rispetto dei requisiti previsti dal Sistema IT-Wallet.

#### <span id="page-12-1"></span>**2.2.4. Fornitori di Attestati Elettronici di Attributi**

I Fornitori di Attestati Elettronici di Attributi hanno la responsabilità dell'emissione e del ciclo di vita degli Attestati Elettronici di Attributi.

I Fornitori di Attestati Elettronici di Attributi realizzano e gestiscono l'infrastruttura tecnologica e le Soluzioni Tecniche a supporto della emissione dei propri Attestati Elettronici, in accordo con quanto previsto dal Sistema IT-Wallet.

Per garantire l'interoperabilità e la sicurezza dei dati all'interno del Sistema IT-Wallet, i Fornitori di Attestati Elettronici di Attributi DEVONO interagire con i Titolari delle Fonti Autentiche conformandosi ai meccanismi di accesso e aggiornamento dei dati previsti dalla PDND secondo la normativa vigente.

I Fornitori di Attestati Elettronici di Attributi DEVONO garantire che gli Attributi contenuti negli Attestati Elettronici di Attributi siano costantemente aggiornati, in conformità con le variazioni e lo stato di validità comunicati dai Titolari delle Fonti Autentiche, nel rispetto degli standard di interoperabilità e sicurezza stabiliti per il Sistema IT-Wallet.

Il Titolare di Fonte Autentica PUÒ richiedere al Fornitore di Attestati Elettronici di Attributi una prova di Autenticazione dell'Utente per il rilascio degli Attributi a questo riferiti. In questo caso per l'emissione degli Attestati Elettronici di Attributi, il Fornitore di Attestati Elettronici di Attributi, DEVE Autenticare, mediante i suoi Dati di Identificazione Personale, l'Utente sulla base del Livello di Garanzia richiesto dal Titolare di Fonte Autentica.

#### <span id="page-13-0"></span>**2.2.5. Titolari di Fonte Autentica**

Il Titolare di Fonte Autentica DEVE:

- partecipare alla registrazione e mantenimento, nel Catalogo degli Attestati Elettronici del Registro IT-Wallet, delle informazioni necessarie all'emissione degli Attestati Elettronici;
- realizzare le Soluzioni Tecniche rese disponibili ai Fornitori di Attestati Elettronici, conformandosi ai meccanismi di accesso e aggiornamento dei dati previsti dalla PDND secondo la normativa vigente, per permettere loro di recuperare gli Attributi e i dati anagrafici richiesti per l'emissione degli Attestati Elettronici;
- rendere disponibile ai Fornitori di Attestati Elettronici le informazioni relative alla variazione degli Attributi rilasciati e dei dati anagrafici nonché allo stato di validità degli stessi, conformandosi ai meccanismi di accesso e aggiornamento dei dati previsti dalla PDND secondo la normativa vigente;
- garantire l'affidabilità delle Soluzioni Tecniche ai Fornitori di Attestati Elettronici nel pieno rispetto dei requisiti del Sistema IT-Wallet.

#### <span id="page-13-1"></span>**2.2.6. Fornitore del Registro IT-Wallet**

Il Fornitore del Registro del Sistema IT-Wallet DEVE garantire l'affidabilità dell'infrastruttura e la disponibilità delle Soluzioni Tecniche erogate per tutti gli Attori Primari del Sistema IT-Wallet, nel pieno rispetto dei requisiti del Sistema IT-Wallet.

Il Fornitore del Registro IT-Wallet DEVE mettere a disposizione un sistema per collaudare le soluzioni di tutti gli Attori primari del Sistema IT-Wallet, compresi i Soggetti Aggregatori, al fine della registrazione.

Le Soluzioni Tecniche che agiscono all'interno del Sistema IT-Wallet DEVONO utilizzare il Registro del Sistema IT-Wallet:

- per le finalità di Autenticazione e autorizzazione dei soggetti che sono registrati al Sistema IT-Wallet;
- per il recupero delle informazioni relative agli Attestati Elettronici contenute nel Catalogo degli Attestati Elettronici.

#### <span id="page-14-0"></span>**2.2.7. Verificatori di Attestati Elettronici**

I Verificatori di Attestati Elettronici interagiscono con l'Istanza IT-Wallet ai fini di Autenticazione dei Dati di Identificazione Personale e degli Attributi.

I Verificatori di Attestati Elettronici POSSONO richiedere uno o più Attributi presenti all'interno dei dati anagrafici contenuti nell'Attestato Elettronico di Dati di Identificazione Personale o uno o più Attributi presenti in uno o più Attestati Elettronici.

I Verificatori di Attestati Elettronici DEVONO Autenticare i Dati di Identificazione Personale e gli Attributi ricevuti e DOVREBBERO verificare lo stato di validità come da [Capitolo 3.4.1] degli stessi (ad esempio, si pensi ad un Attestato Elettronico che ancora può dimostrare la maggiore età seppur questo risulti essere temporalmente scaduto).

I Verificatori di Attestati Elettronici DEVONO definire e aggiornare nel Registro IT-Wallet gli Attributi necessari per l'erogazione delle proprie Soluzioni Tecniche, relative ai Dati di Identificazione Personale e gli Attributi.

Per l'Autenticazione degli Utenti, i Verificatori di Attestati Elettronici utilizzano i Dati di Identificazione Personale eventualmente in congiunzione con gli Attestati Elettronici di Attributi nel caso in cui la verifica sia richiesta su Attributi di Utenti Autenticati.

I Verificatori di Attestati Elettronici POSSONO avvalersi delle Soluzioni Tecniche dei Soggetti Aggregatori per la verifica da remoto o in prossimità di Attestati Elettronici. Gli accordi tra Verificatori di Attestati Elettronici e Soggetti Aggregatori POSSONO essere concordati autonomamente sulla base di accordi o contratti bilaterali.

# <span id="page-15-0"></span>**3. Funzionalità primarie**

Nei paragrafi che seguono sono descritte le funzionalità primarie delle Soluzioni IT-Wallet nel Sistema IT-Wallet, vale a dire le funzionalità essenziali delle Soluzioni IT-Wallet, riportate nella figura seguente.

![](_page_15_Figure_2.jpeg)

*Figura 2 - Funzionalità primarie del Sistema IT-Wallet*

## <span id="page-15-1"></span>**3.1. Attivazione Istanza IT-Wallet**

Lo stato di un'Istanza IT-Wallet può essere:

- installato;
- operativo;
- attivo (o valido).

L'Utente per configurare l'Istanza IT-Wallet nello stato installato DEVE recuperare il pacchetto di installazione mediante i canali predisposti dalla Soluzione IT-Wallet e in conformità alle Specifiche Tecniche.

L'Utente per configurare l'Istanza IT-Wallet nello stato operativo DEVE accettare termini e condizioni d'uso della Soluzione IT-Wallet e ottenere la conformità di sicurezza del dispositivo e dell'Istanza IT-Wallet secondo quanto previsto dalle Specifiche Tecniche.

L'Utente per configurare l'Istanza IT-Wallet nello stato attivo DEVE richiedere e ottenere un Attestato Elettronico di Dati di Identificazione Personale.

Un Utente con una Istanza IT-Wallet attiva PUÒ:

- richiedere l'emissione di Attestati Elettronici di Attributi;
- presentare ai Verificatori di Attestati Elettronici gli Attestati Elettronici presenti all'interno della stessa Istanza IT-Wallet.

Un Utente con un'Istanza IT-Wallet nello stato operativo PUÒ:

- richiedere l'emissione dell'Attestato Elettronico di Dati di Identificazione Personale;
- presentare ai Verificatori di Attestati Elettronici gli Attestati Elettronici presenti nella stessa Istanza IT-Wallet, solo nel caso in cui il Verificatore di Attestati Elettronici non richieda la presentazione di Attestati Elettronici di Dati di Identificazione Personale;
- richiedere l'emissione di Attestati Elettronici di Attributi che non richiedono la presentazione dell'Attestato Elettronico di Dati di Identificazione Personale.

L'Utente PUÒ attivare una sola Istanza IT-Wallet per ciascun Fornitore di Soluzione IT-Wallet.

L'Utente PUÒ scegliere di attivare più Istanze IT-Wallet a condizione che ciascuna Istanza provenga da un diverso Fornitore di Soluzioni IT-Wallet secondo quanto previsto dalle Specifiche Tecniche.

### <span id="page-16-0"></span>**3.2. Ottenimento di Attestati Elettronici di Dati di Identificazione Personale**

L'Utente, per il tramite della propria Istanza IT-Wallet, PUÒ avviare il processo di richiesta dell'Attestato Elettronico di Dati di Identificazione Personale a seguito di Autenticazione presso il Fornitore di Attestati Elettronici di Dati di Identificazione Personale, unicamente mediante il Livello di Garanzia Elevato del Sistema CIEid.

Successivamente all'Autenticazione, il Fornitore di Dati di Identificazione Personale emette l'Attestato Elettronico di Dati di Identificazione Personale richiesto dall'Utente, in conformità ai profili e requisiti di sicurezza dei dispositivi e dell'Istanza IT-Wallet sotto il controllo degli utenti.

L'Utente PUÒ utilizzare il proprio Attestato Elettronico di Dati di Identificazione Personale, tramite la propria Istanza IT-Wallet, per l'Autenticazione di livello di Garanzia Significativo, presso i Verificatori di Attestati Elettronici.

Il Sistema IT-Wallet NON DEVE consentire ad un Utente di ottenere simultaneamente più Attestati Elettronici di Dati di Identificazione Personale dal Fornitore di Attestati Elettronici di Dati di Identificazione Personale sulla medesima Istanza IT-Wallet, in conformità alle Specifiche Tecniche.

## <span id="page-17-0"></span>**3.3. Ottenimento Attestati Elettronici di Attributi**

La richiesta di emissione di un Attestato Elettronico di Attributi è realizzata da un Utente per il tramite di un'Istanza IT-Wallet.

Il Sistema IT-Wallet NON DEVE consentire ad un Utente di ottenere simultaneamente, sulla medesima Istanza IT-Wallet, più di un Attestato Elettronico di Attributi contenente i medesimi Attributi, tenuto conto che:

- l'ottenimento di un nuovo Attestato Elettronico di Attributi sulla medesima Istanza IT-Wallet DEVE comportare la cancellazione e la revoca del precedente Attestato Elettronico di Attributi contenente i medesimi attributi;
- l'ottenimento di un nuovo Attestato Elettronico di Attributi su una Istanza IT-Wallet diversa da quella precedentemente usata NON DEVE comportare la modifica dello stato di validità dell'Attestato Elettronico di Attributi precedentemente ottenuto contenente i medesimi Attributi.

#### <span id="page-17-1"></span>**3.4. Revoca e sospensione**

Il Sistema IT-Wallet prevede meccanismi per:

- la revoca delle Istanze IT-Wallet;
- la revoca degli Attestati Elettronici di Dati di Identificazione Personale;

• la revoca o la sospensione degli Attestati Elettronici di Attributi.

I Fornitori di Soluzioni IT-Wallet in qualità di responsabili dell'implementazione, gestione e manutenzione delle Soluzioni IT-Wallet DEVONO revocare una Istanza IT-Wallet nei casi di:

- eventuali vulnerabilità di sicurezza emerse nel corso del ciclo di vita dell'Istanza IT-Wallet fornita;
- richieste provenienti dall'Organismo di Vigilanza;
- richiesta esplicita degli Utenti per il tramite:
  - della propria Istanza IT-Wallet;
  - delle Soluzioni Tecniche rese disponibili dallo stesso Fornitore di Soluzioni IT-Wallet, previa Autenticazione dell'Utente almeno allo stesso Livello di Garanzia richiesto per l'attivazione delle Istanze IT-Wallet;
- decesso dell'Utente dell'Istanza IT-Wallet;
- attività illecite segnalate dall'Organismo di Vigilanza.

Il Fornitore di Attestazioni Elettroniche di Dati di Identificazione Personale DEVE revocare gli Attestati Elettronici di Dati di Identificazione Personale in caso di:

- comprovati incidenti di sicurezza riguardanti le Soluzioni Tecniche dello stesso Fornitore di Attestati Elettronici di Dati di Identificazione Personale.
- richiesta esplicita dell'Utente tramite:
  - la propria Istanza IT-Wallet in conformità alle Specifiche Tecniche;
  - le Soluzioni Tecniche rese disponibili dallo stesso Fornitore di Attestati Elettronici di Dati di Identificazione Personale, previa Autenticazione dell'Utente almeno allo stesso Livello di Garanzia richiesto per l'emissione degli Attestati Elettronici di Dati di Identificazione Personale;
- aggiornamento dei dati anagrafici, allineati secondo la normativa, contenuti nell'Attestato Elettronico dei Dati di Identificazione Personale emesso in conformità delle Specifiche Tecniche.
- decesso dell'Utente per cui l'Attestato Elettronico di Dati di Identificazione Personale è stato emesso;
- compromissione dell'identità digitale utilizzata per l'Autenticazione dell'Utente in fase di ottenimento dell'Attestazione Elettronica di Dati di Identificazione Personale;

- ottenimento di un nuovo Attestato Elettronico di Dati di Identificazione Personale per la stessa Istanza IT-Wallet;
- revoca dell'Istanza IT-Wallet per cui l'Attestato Elettronico di Dati di Identificazione Personale è stato emesso;
- attività illecite segnalate dall'Organismo di Vigilanza IT-Wallet.

I Fornitori di Attestati Elettronici di Attributi DEVONO revocare gli Attestati Elettronici di Attributi nei seguenti casi:

- comprovati incidenti di sicurezza delle soluzioni dello stesso Fornitore di Attestati Elettronici di Attributi;
- su richiesta esplicita dell'Utente per tramite:
  - della propria Istanza IT-Wallet in conformità alle Specifiche Tecniche;
  - delle Soluzioni Tecniche rese disponibili dallo stesso Fornitore di Attestati Elettronici di Attributi, previa Autenticazione dell'Utente, almeno allo stesso Livello di Garanzia richiesto per l'attivazione delle Istanze IT-Wallet;
- aggiornamento degli Attributi, da parte del Titolare della Fonte Autentica degli stessi contenuti negli Attestati Elettronici di Attributi emessi;
- decesso dell'Utente per cui gli Attestati Elettronici di Attributi sono stati emessi in conformità alle Specifiche Tecniche;
- revoca dell'Istanza IT-Wallet per cui gli Attestati Elettronici di Attributi sono stati emessi;
- ottenimento di un equivalente Attestato Elettronico di Attributi sulla stessa Istanza IT-Wallet;
- attività illecite segnalate dall'Organismo di Vigilanza IT-Wallet;
- compromissione dell'identità digitale utilizzata per l'Autenticazione dell'Utente in fase di ottenimento dell'Attestazione Elettronica di Dati di Identificazione Personale;

I Fornitori di Attestati Elettronici di Attributi POSSONO revocare o sospendere gli Attestati Elettronici di Attributi emessi nel caso di revoca dell'Attestato Elettronico di Dati di Identificazione Personale.

I Fornitori di Attestati Elettronici di Attributi e il Fornitore di Attestati Elettronici di Dati di Identificazione Personale, avendo la responsabilità tecnica e amministrativa del ciclo di vita degli Attestati Elettronici, DEVONO garantire la revoca o sospensione degli Attestati Elettronici sulla base delle richieste provenienti:

• dai Titolari di Fonte Autentiche;

- dall'Utente;
- dall'Organismo di Vigilanza.

#### <span id="page-20-0"></span>**3.4.1. Ciclo di vita degli Attestati Elettronici**

Gli Attestati Elettronici seguono un ciclo di vita che ne attesta la propria validità:

- al momento del rilascio lo stato è valido;
- di norma lo stato di validità ha una durata predefinita, tale durata è definita nelle Specifiche Tecniche;
- è possibile, nelle circostanze indicate nel [Capitolo 3.4], che tali Attestati Elettronici vengano revocati prima della loro naturale scadenza, cambiandone lo stato in non valido.

Per i soli Attestati Elettronici di Attributi è possibile, inoltre, avere uno stato di sospensione che ne preclude la validità per un periodo limitato di tempo.

# <span id="page-20-1"></span>**3.5. Archiviazione e ripristino degli Attestati Elettronici di Attributi e Storico Transazioni**

L'Utente, per il tramite della propria Istanza IT-Wallet, PUÒ effettuare l'archiviazione dei riferimenti dei propri Attestati Elettronici di Attributi e dello storico delle transazioni realizzate con la stessa Istanza IT-Wallet.

L'archiviazione dei riferimenti e il ripristino degli Attestati Elettronici di Attributi e dello storico delle transazioni DEVE essere realizzato in conformità alle Specifiche Tecniche.

L'Istanza IT-Wallet NON DEVE consentire l'archiviazione e il conseguente ripristino degli Attestati Elettronici di Dati di Identificazione Personale.

L'Utente PUÒ effettuare il ripristino degli Attestati Elettronici di Attributi su qualsiasi Istanza IT-Wallet in conformità alle Specifiche Tecniche.

## <span id="page-20-2"></span>**3.6. Presentazione e verifica di Attestati Elettronici**

L'Utente, per il tramite della propria Istanza IT-Wallet, PUÒ presentare i propri Attestati Elettronici ai Verificatori di Attestati Elettronici, nelle seguenti modalità:

- in prossimità: consente la presentazione degli Attestati Elettronici da parte dell'Utente fisicamente presente nel luogo dove avviene la presentazione;
- da remoto: consente la presentazione degli Attestati Elettronici da parte dell'Utente non fisicamente presente nel luogo dove avviene la presentazione.

La verifica PUÒ essere effettuata tramite:

- Soluzioni Tecniche di verifica degli Attestati Elettronici;
- Soluzioni Tecniche specifiche delle Istanze IT-Wallet.

#### <span id="page-21-0"></span>**3.6.1. Presentazione Attestati Elettronici di Dati di Identificazione Personale**

Il Verificatore di Attestati Elettronici che, nell'ambito dei servizi che eroga o le funzioni che svolge, necessita di Autenticare l'Utente, richiede all'Utente, per il tramite dell'Istanza IT-Wallet, la presentazione dei Dati di Identificazione Personale contenuti nell'Attestato Elettronico di Dati di Identificazione Personale memorizzato nella sua Istanza IT-Wallet.

Se contestualmente alla richiesta dei Dati di Identificazione Personale sono richiesti, dal Verificatore di Attestati Elettronici, ulteriori Attributi contenuti negli Attestati Elettronici di Attributi memorizzati sulla Istanza IT-Wallet, questi NON DEVONO essere utilizzati per l'Autenticazione dell'Utente.

#### <span id="page-21-1"></span>**3.6.2. Presentazione Attestati Elettronici di Attributi**

Per dare seguito all'attribuzione di deleghe, caratteristiche, licenze o qualità agli Utenti, il Verificatore di Attestati Elettronici richiede all'Utente, per il tramite dell'Istanza IT-Wallet, la presentazione di uno o più Attributi contenuti negli Attestati Elettronici di Attributi memorizzati sull'Istanza IT-Wallet.

# <span id="page-21-2"></span>**3.7. Richiesta Cancellazione Dati di Identificazione Personali e Attributi presentati**

L'Utente PUÒ richiedere al Verificatore di Attestati Elettronici la cancellazione dei propri Dati di Identificazione Personale e Attributi precedentemente presentati.

Tale funzionalità DEVE essere resa disponibile:

- dall'Istanza IT-Wallet dell'Utente;
  - dal Verificatore di Attestati Elettronici.

## <span id="page-22-0"></span>**4. Architettura e requisiti del Sistema IT-Wallet**

In questo capitolo viene presentata l'architettura tecnologica di alto livello del Sistema IT-Wallet, delineando le Soluzioni Tecniche che compongono il sistema e i relativi requisiti funzionali delle soluzioni che compongono ilsistema, vale a dire quei requisiti che descrivono le specifiche operazioni e comportamenti che l'insieme dei servizi, applicazioni, componenti tecnologiche e processi DEVONO o POSSONO eseguire in conformità al Sistema IT-Wallet.

La figura che segue illustra l'architettura tecnologica di alto livello e le Soluzioni Tecniche del Sistema IT-Wallet.

![](_page_22_Figure_3.jpeg)

*Figura 4 - Architettura del Sistema ITWallet*

L'architettura tecnologica del Sistema IT-Wallet DEVE assicurare:

- controllo: le Istanze IT-Wallet DEVONO essere nella sola disponibilità degli Utenti:
  - consentendogli di mantenere il controllo sui propri Attestati Elettronici;
    - permettendogli di scegliere quali Attributi presentare, a chi e per quale scopo;
- sicurezza: nell'ambito del Sistema IT-Wallet DEVONO essere garantite l'integrità, la disponibilità e la confidenzialità degli Attributi Elettronici interscambiati tra le Soluzioni Tecniche;
- interoperabilità: il Sistema IT-Wallet DEVE assicurare l'interoperabilità tra le Soluzioni Tecniche, permettendo alle stesse di:
  - Autenticare gli Attributi Elettronici interscambiati;
  - garantire le interazioni affidabili e senza soluzione di continuità;

- efficienza e riduzione dei costi: gli Utenti POSSONO gestire i propri Attestati Elettronici in un'unica modalità, riducendo l'entropia determinata da esperienze utente differenti per servizi digitali differenti;
- accessibilità e usabilità: le Soluzioni IT-Wallet DEVONO essere implementate, tramite un approccio incentrato sull'Utente, in conformità con le normative unionali e nazionali in materia di accessibilità digitale.

Le Specifiche Tecniche forniscono il dettaglio dell'architettura tecnica, il quadro implementativo e i requisiti di design relativi all'esperienza utente, stabilendo i criteri di interoperabilità e conformità necessari per l'integrazione delle Soluzioni Tecniche con il Sistema IT-Wallet. Le Soluzioni Tecniche adottate dagli operatori che intendono interoperare con il Sistema IT-Wallet DEVONO rispettare tali criteri, basati per quanto possibile su standard esistenti e su modelli in evoluzione, al fine di assicurare un ambiente sicuro e tecnicamente armonizzato con gli sviluppi normativi e tecnologici a livello nazionale ed europeo.

In quanto segue sono riportati i requisiti assicurati dagli Attori Primari relativamente alla Soluzioni Tecniche dagli stessi implementate.

#### <span id="page-23-0"></span>**4.1. Requisiti delle Soluzioni IT-Wallet**

I Fornitori di Soluzioni IT-Wallet in qualità di responsabili dell'implementazione, gestione e manutenzione delle Soluzioni IT-Wallet, DEVONO:

- Autenticare, per il tramite del Registro IT-Wallet, le soluzioni dei Fornitori di Attestati Elettronici e le soluzioni dei Verificatori di Attestati Elettronici prima dell'avvio di interazioni con le stesse;
- relativamente alle Istanze IT-Wallet attivate dagli Utenti:
  - assicurare che la Soluzione IT-Wallet sviluppata sia distribuita in modo sicuro e possa essere attivata dagli Utenti solo su dispositivi affidabili e conformi ai profili e ai requisiti di sicurezza richiesti;
  - assicurare l'autenticità, l'integrità e la validità delle Istanze IT-Wallet installate sui dispositivi degli Utenti;
  - mantenere le Istanze IT-Wallet aggiornate, garantendo che siano installate solo versioni funzionanti e sicure;
  - Autenticare gli Attestati Elettronici ottenuti dal Fornitore di Attestati Elettronici;

- consentire ai Fornitori di Attestati Elettronici e ai Verificatori di Attestati Elettronici di verificare lo stato di attivazione delle Istanze IT-Wallet degli Utenti nelle fasi di ottenimento e presentazione di Attestati Elettronici;
- relativamente alle funzionalità assicurate dalle Istanze IT-Wallet agli Utenti:
  - garantire che gli Utenti mantengano il pieno controllo sugli Attestati Elettronici
  - consentire agli Utenti di presentare in Divulgazione Selettiva, in prossimità e da remoto, alle soluzioni dei Verificatori di Attestati Elettronici, in conformità alle Specifiche Tecniche, i Dati di Identificazione Personale e gli Attributi presenti negli Attestati Elettronici memorizzati sulle proprie Istanze IT-Wallet;
  - consentire agli Utenti di richiedere la cancellazione degli Attributi Elettronici emessi dai Fornitori di Attestati Elettronici, in conformità alle Specifiche Tecniche;
  - consentire agli Utenti di richiedere la cancellazione ai Verificatori di Attestati Elettronici, in conformità alle Specifiche Tecniche, degli Attributi Elettronici precedentemente presentati;
  - consentire agli Utenti di visualizzare lo storico delle interazioni avvenute con i Verificatori di Attestati Elettronici e i Fornitori di Attestati Elettronici per il tramite delle proprie Istanze IT-Wallet;
  - consentire agli Utenti di archiviare e ripristinare, in conformità alle Specifiche Tecniche i riferimenti degli Attestati Elettronici memorizzati sulle proprie Istanze IT-Wallet;
  - ricevere le notifiche di revoca degli Attestati Elettronici in conformità alle Specifiche Tecniche;
- richiedere agli Utenti, mediante le proprie Istanze IT-Wallet, esplicito consenso alla:
  - memorizzazione nelle Istanze IT-Wallet degli Attestati Elettronici emessi dai Fornitori di Attestati Elettronici;
  - presentazione dei Dati di Identificazione Personale e gli Attributi alle soluzioni dei Verificatori di Attestati Elettronici.
- revocare una Istanza IT-Wallet nei casi previsti al [Capitolo 3.4]
- monitorare costantemente il funzionamento della Soluzione IT-Wallet e delle relative Istanze IT-Wallet al fine di risolvere tempestivamente eventuali problematiche di funzionamento e sicurezza;

- assistere l'Utente nella risoluzione di eventuali problematiche che si dovessero presentare in relazione all'utilizzo e alla gestione dell'Istanza IT-Wallet;
- assicurare le funzionalità descritte nelle Specifiche Tecniche.

## <span id="page-25-0"></span>**4.2. Requisiti delle soluzioni del Fornitore di Attestati Elettronici di Dati di Identificazione Personale**

Il Fornitore di Attestazioni Elettroniche di Dati di Identificazione Personale DEVE:

- rilasciare gli Attestati Elettronici di Dati di Identificazione Personale secondo i formati e le modalità tecniche definite dalle Specifiche Tecniche;
- rilasciare gli Attestati Elettronici di Dati di Identificazione Personale esclusivamente sulle Soluzioni IT-Wallet che sono registrate nel Registro IT-Wallet;
- Autenticare, per il tramite del Registro IT-Wallet, le Soluzioni IT-Wallet prima dell'avvio di interazioni con queste ultime;
- Autenticare l'Utente prima dell'emissione dell'Attestato Elettronico di Dati di Identificazione Personale, assicurando la correttezza ed esattezza dei dati anagrafici anche avvalendosi della relativa Fonte Autentica secondo la normativa;
- rendere disponibili informazioni utili alla verifica dello stato di validità degli Attestati Elettronici di Dati di Identificazione Personale alle Istanze IT-Wallet e ai Verificatori di
  - Attestati Elettronici interessati;
- revocare gli Attestati Elettronici di Dati di Identificazione Personale nei casi previsti al [Capitolo 3.4] e notificare la revoca degli Attestati Elettronici di Dati di Identificazione Personale agli Utenti cui i Dati di Identificazione Personale si riferiscono in conformità alle Specifiche Tecniche;
- rendere disponibile Soluzioni Tecniche che consentono agli Utenti, previa Autenticazione di questi ultimi, almeno allo stesso Livello di Garanzia richiesto per l'emissione degli Attestati Elettronici di Dati di Identificazione Personale, per:
  - richiedere la revoca di uno o più Attestati Elettronici di Dati di Identificazione Personale;

- visionare i Dati di Identificazione Personale validi e lo storico di quelli ottenuti in precedenza;
- verificare l'autenticità dei Dati di Identificazione Personale.
- assistere l'Utente nella risoluzione di eventuali problematiche che si dovessero presentare in relazione al ciclo vita degli Attestati Elettronici di Dati di Identificazione Personale emessi;
- prevedere, con le modalità e le tempistiche definite nelle Specifiche Tecniche, i tracciati delle emissioni di Attestati Elettronici di Attributi di Dati di Identificazione Personale nell'ambito del Sistema IT-Wallet.
- assicurare le funzionalità descritte nelle Specifiche Tecniche.

## <span id="page-26-0"></span>**4.3. Requisiti delle soluzioni dei Fornitori di Attestati Elettronici di Attributi**

I Fornitori di Attestati Elettronici di Attributi DEVONO:

- rilasciare gli Attestati Elettronici di Attributi secondo i formati e le modalità tecniche definite dalle Specifiche Tecniche;
- Autenticare, per il tramite del Registro IT-Wallet:
  - le Soluzioni IT-Wallet prima dell'avvio di interazioni con queste ultime;
  - il Fornitore di Attestati Elettronici di Dati di Identificazione Personale, qualora sia richiesta l'Autenticazione dell'Utente da parte dei Titolari di Fonte Autentiche interessati all'emissione di un Attestato Elettronico di Attributi;
- richiedere all'Utente, per il tramite delle proprie Istanze IT-Wallet, la presentazione dell'Attestazione Elettronica di Dati di Identificazione Personale da inoltrare ai Titolari di Fonte Autentiche nel caso in cui, questi ultimi, richiedano l'Autenticazione dell'Utente;
- interrogare il Catalogo degli Attestati Elettronici relativamente alle Fonti Autentiche da consultare e agli Attributi da richiedere alle stesse per l'emissione degli Attestati Elettronici di Attributi;
- recuperare gli Attributi dell'Utente presso le soluzioni delle Fonti Autentiche, conformandosi ai meccanismi di accesso e aggiornamento dei dati previsti dalla PDND secondo la normativa vigente;
- rendere disponibili le informazioni utili alla verifica di validità degli Attestati Elettronici di Attributi alle Istanze IT-Wallet e ai Verificatori di Attestazioni Elettroniche interessati;

- revocare gli Attestati Elettronici di Attributi nei casi previsti al [Capitolo 3.4] e notificare la revoca degli Attestati Elettronici di Attributi emessi agli Utenti a cui gli Attestati Elettronici di Attributi si riferiscono in conformità alle Specifiche Tecniche;
- rendere disponibili Soluzioni Tecniche che consentono agli Utenti, previa Autenticazione di questi ultimi almeno allo stesso Livello di Garanzia richiesto per l'ottenimento dell'Attestato
  - Elettronico per cui richiede la revoca, la visione e la verifica;
  - assistere l'Utente nella risoluzione di eventuali problematiche che si dovessero presentare in relazione al ciclo vita degli Attestati Elettronici di Attributi emessi;
- implementare, con le modalità definite nelle Specifiche Tecniche, i tracciati relativi alle emissioni degli Attestati Elettronici di Attributi nell'ambito del Sistema IT-Wallet.
- assicurare le funzionalità descritte nelle Specifiche Tecniche.

## <span id="page-27-0"></span>**4.4. Requisiti delle soluzioni dei Verificatori di Attestati Elettronici**

Le Soluzioni dei Verificatori di Attestati Elettronici DEVONO:

- mantenere aggiornato l'elenco dei servizi erogati e per ognuno di essi:
  - mantenere aggiornato l'elenco dei Dati di Identificazione Personali e degli Attributi richiesti;
  - assicurare la pertinenza e non eccedenza dei Dati di Identificazione Personale e Attributi richiesti;
- Autenticare, per il tramite del Registro IT-Wallet:
  - le Soluzioni IT-Wallet prima dell'avvio di interazioni con queste ultime;
  - i Fornitori di Attestati Elettronici per l'Autenticazione dei Dati di Identificazione Personale e Attributi presentati dagli Utenti per il tramite delle Istanze IT-Wallet;
- prevedere formati e modalità tecniche per la richiesta di presentazione degli Attestati Elettronici secondo quanto definito nelle Specifiche Tecniche;
- garantire la sicurezza dei Dati di Identificazione Personale e degli Attributi presentati dagli Utenti e utilizzare gli stessi in conformità alle normative e per gli scopi per cui sono stati richiesti;

- consentire all'Utente di richiedere la cancellazione dei Dati di Identificazione Personale presentati e degli Attributi, per il tramite:
  - della propria Istanza IT-Wallet in conformità alle Specifiche Tecniche;
  - delle Soluzioni Tecniche rese disponibili dallo stesso Fornitore di Servizi, previa Autenticazione dell'Utente almeno allo stesso Livello di Garanzia richiesto per l'attivazione delle Istanze IT-Wallet;
- Autenticare l'Utente verificando il Livello di Garanzia dell'Attestato Elettronico di Dati di Identificazione Personale conformemente alle Specifiche Tecniche
- assistere l'Utente nella risoluzione di eventuali problematiche che si dovessero verificare nel corso della presentazione degli Attestati Elettronici;
- implementare, con le modalità definite nelle Specifiche Tecniche, i tracciati relativi alle verifiche di Attestati Elettronici di Attributi nell'ambito del Sistema IT-Wallet.
- assicurare le funzionalità descritte nelle Specifiche Tecniche.

### <span id="page-28-0"></span>**4.5. Requisiti delle soluzioni dei Titolari di Fonti Autentiche**

I Titolari di Fonti Autentiche DEVONO:

- registrare e mantenere, nel Catalogo degli Attestati Elettronici del Registro IT-Wallet, le informazioni di propria competenza necessarie all'emissione degli Attestati Elettronici a cui forniscono i dati anagrafici o gli Attributi;
- conformarsi ai meccanismi di accesso e aggiornamento dei dati previsti dalla PDND secondo la normativa vigente pubblicare al fine di rendere disponibili ai Fornitori di Attestati Elettronici i servizi per accedere ai dati anagrafici o agli Attributi necessari all'emissione degli Attestati Elettronici, a seguito della richiesta dell'Utente tramite l'Istanza Wallet;
- abilitare i Fornitori di Attestati Elettronici alla fruizione dei rispettivi servizi;
- in relazione ai servizi di cui al precedente punto: implementare i servizi nel rispetto delle [LG INTEROP] e, in ogni caso, applicando le indicazioni previste dalle Specifiche Tecniche;
- conformandosi ai meccanismi di accesso e aggiornamento dei dati previsti dalla PDND secondo la normativa vigente per notificare ai Fornitori di Attestati Elettronici le variazioni

dei dati anagrafici o degli Attributi utilizzati per l'emissione degli Attestati Elettronici secondo quanto previsto dalle Specifiche Tecniche;

- garantire la qualità dei dati anagrafici o Attributi erogati, anche attivando canali di comunicazione diretta con gli Utenti interessati;
- implementare le modalità di comunicazione previste dalle Specifiche Tecniche;
- fornire supporto ai Fornitori di Attestati Elettronici per la risoluzione di eventuali problematiche che dovessero verificarsi in relazione agli Attributi contenuti negli Attestati Elettronici di loro competenza.

## <span id="page-29-0"></span>**4.6. Registro del Sistema IT-Wallet**

Il Registro del Sistema IT-Wallet DEVE:

- contenere l'elenco dei Soggetti Pubblici e Soggetti Privati che sono registrati al Sistema IT-Wallet e le pertinenti informazioni che li riguardano;
- gestire il Catalogo degli Attestati Elettronici collegato al Catalogo degli e-service di PDND;
- aggiornare le informazioni in esso contenute in accordo con le Specifiche Tecniche;
- consentire il libero accesso e la pubblica consultazione delle informazioni in esso contenute;
- permettere l'Autenticazione delle informazioni in esso contenute.

Il Catalogo degli Attestati Elettronici DEVE contenere le informazioni relative a:

- formati e schemi degli Attestati Elettronici;
- Titolari di Fonti Autentiche e per essi:
  - Attributi da essi forniti con eventuale richiesta di Autenticazione degli Utenti e relativo Livello di Garanzia;
  - le soluzioni dagli stessi implementate per fruire degli Attributi.
- la natura dell'Attestato, in particolare se Attestato Elettronico di Attributi Pubblici o se Attestato Elettronico di Interesse Pubblico;
- la categoria dell'Attestato, ad esempio se documento di riconoscimento ai sensi del decreto del Presidente della Repubblica 28 dicembre 2000, n. 445;
- il Fornitore di Attestati Elettronici legittimato al rilascio delle Attestazioni Elettroniche di
  - Attributi;
  - i Fornitori di Soluzioni IT Wallet abilitati a ottenere l'Attestato.

• le eventuali ulteriori informazioni disciplinate nelle Specifiche Tecniche.

Il dettaglio delle informazioni contenute nel Registro del Sistema IT-Wallet e le modalità di consultazione dello stesso sono definite nelle Specifiche Tecniche.
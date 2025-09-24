.. include:: ../common/common_definitions.rst


Riferimenti Normativi
=====================

Di seguito i riferimenti normativi e i rispettivi acronimi inclusi in queste Specifiche Tecniche:

[CAD]

Decreto Legislativo n. 82 del 7 marzo 2005, come modificato, contenente il 'Codice dell'Amministrazione Digitale'.

[REF_ACCESSIBILITY]

Linee Guida per l'Accessibilità degli Strumenti Informatici come da Articolo 11 della Legge 4/2004.
Direttiva (UE) 2019/882 del Parlamento Europeo e del Consiglio del 17 aprile 2019 sui requisiti di accessibilità per prodotti e servizi.

[GL_DESIGN]

Linee Guida di Design per siti web e servizi digitali forniti dalle pubbliche amministrazioni, ai sensi dell'Articolo 53, comma 1-ter del Decreto Legislativo n. 82 del 7 marzo 2005, come modificato.


Termini Definiti e Acronimi
===========================

Questa sezione allinea la terminologia del Sistema IT-Wallet con le definizioni fornite in ARF 1.10 (vedi `ARF Annex 1 <https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/annexes/annex-1/annex-1-definitions.md>`_). Per ogni termine, la definizione IT-Wallet è confrontata e mappata alla definizione ARF, con note su eventuali differenze o chiarimenti.

I termini *Utente*, *Servizio di Trust*, *Trust Model*, *Trusted List*, *Trust Framework*, *Attributi*, *Fornitore di Attestati Elettronici di Attributi* o *Fornitore di Servizi di Trust (TSP)*, *Attestato Elettronico di Dati di Identificazione Personale*, *Lista di Revoca*, *Fornitore di Attestati Elettronici di Attributi Qualificati* o *Fornitore Qualificato di Servizi di Trust (QTSP)*, *Attestato Elettronico di Attributi*, sono definiti in `EIDAS-ARF`_.

Di seguito è riportata la descrizione di acronimi e definizioni utili per ulteriori approfondimenti su argomenti che completano il Sistema IT-Wallet e i componenti che interagiscono.

.. glossary::
    :sorted:

    **Processo di Accreditamento**
      Processo eseguito dall'Ente Nazionale di Accreditamento per accreditare i CAB, risultando in un certificato di accreditamento.
      Non presente in ARF 1.10; specifico per IT-Wallet.

    **Attributi**
    **Attributi dell'Utente**
      Un insieme di caratteristiche, qualità, diritti o permessi di una persona o oggetto, o una singola informazione di tale tipo.
      Allineato con ARF 1.10.

    **Autenticazione**
      Processo elettronico che conferma l'identità di una persona o l'origine/integrità dei dati.
      Allineato con ARF 1.10.

    **Fonte Autentica**
      Entità pubblica o privata responsabile di un repository/sistema considerato fonte primaria per Attributi o PID.
      Allineato con ARF 1.10.

    **Processo di Certificazione**
      Processo da parte degli Organismi di Valutazione della Conformità per certificare la Soluzione Wallet, incluse valutazioni tecniche periodiche.
      Non presente in ARF 1.10; specifico per IT-Wallet.

    **Organismo di Valutazione della Conformità**
      Organismo accreditato competente per valutare/certificare Soluzioni Wallet o fornitori di servizi di trust.
      Allineato con ARF 1.10.

    **Credential Issuer**
    **Fornitore di Credenziale**
      Entità Organizzativa che fornisce Credenziali Digitali agli Utenti (può essere Fornitore di Attestati Elettronici di Dati di Identificazione Personale o Fornitore di (Q)EAA).
      ARF 1.10 usa termini simili; IT-Wallet unisce i Fornitori PID e (Q)EAA sotto questo termine.

    **Credential Status Assertion**
    **Status Assertion**
      Documento firmato che prova lo stato di validità corrente di una Credenziale Digitale.
      Non presente in ARF 1.10; specifico per IT-Wallet.

    **Asset Critici**
      Asset (ad es., chiavi crittografiche) la cui perdita avrebbe un impatto serio sull'Unità di Wallet.
      Allineato con ARF 1.10.

    **Cryptographic Hardware Key Tag**
      Identificatore unico per Cryptographic Hardware Keys, utilizzato per accedere alla chiave privata nell'hardware.
      Non presente in ARF 1.10.

    **Cryptographic Hardware Keys**
      Coppia di chiavi generata dall'Istanza del Wallet, valida per la sua durata.
      Non presente in ARF 1.10.

    **Servizio di Integrità del Dispositivo**
      Servizio dei produttori di dispositivi per verificare l'integrità dell'app e l'archiviazione sicura delle chiavi.
      Non presente in ARF 1.10.

    **Credenziale Digitale**
    **Credenziale**
     Insieme firmato di Attributi in un formato specifico (ad es., mDoc-CBOR, SD-JWT VC), può essere PID o (Q)EAA.
     ARF 1.10 si limita a mDoc-CBOR e SD-JWT VC; IT-Wallet nota che la definizione dovrebbe essere neutrale rispetto al formato.

    **Autorità di Federazione**
      Entità di governance pubblica che emette linee guida, regole e gestisce liste di trust e stato dei partecipanti.
      Non presente in ARF 1.10.

    **Titolare**
      Persona o entità che riceve, gestisce e presenta Credenziali Digitali tramite l'Istanza del Wallet.
      Non presente in ARF 1.10; specifico per IT-Wallet.

    **Associazione Crittografica con l'Utente**
      Capacità del Titolare di dimostrare il possesso della chiave privata attestata da una Terza Parte Fidata.
      Non presente in ARF 1.10.

    **Identity and Access Management (IAM)**
      Framework per gestire identità digitali e accesso alle informazioni.
      Non presente in ARF 1.10.

    **Sistema IT-Wallet**
      Insieme di Soluzioni Tecniche che implementano il Sistema di Portafoglio Digitale Italiano.
      Non presente in ARF 1.10; specifico per IT-Wallet.

    **Registro del Sistema IT-Wallet**
      Registro delle entità che partecipano al Sistema IT-Wallet.
      Non presente in ARF 1.10; specifico per IT-Wallet.

    **Key Attestation**
      Attestazione dal produttore OEM del dispositivo riguardo l'archiviazione sicura delle chiavi nel keystore supportato da hardware.
      Non presente in ARF 1.10.

    **Livello di Garanzia**
      Grado di fiducia nella verifica dell'identità e nella presentazione delle credenziali.
      Non presente in ARF 1.10.

    **Metadato**
      Artefatto digitale con informazioni su un'Entità Organizzativa (endpoint, chiavi pubbliche, ecc.).
      Non presente in ARF 1.10.

    **Ente Nazionale di Accreditamento**
      Organismo che esegue l'accreditamento sotto autorità di uno Stato Membro.
      Allineato con ARF 1.10.

    **Gestore di Identità Digitale**
      Sistemi di identità preesistenti (ad es. CIE) notificati a eIDAS.
      Non presente in ARF 1.10.

    **Processo di Notifica**
      Processo per trasferire informazioni alla CE e inclusione nella Trusted List.
      Allineato con ARF 1.10.

    **Entità Organizzativa**
      Persona giuridica (organizzazione o entità pubblica) riconosciuta per operare un ruolo nell'ecosistema IT-Wallet.
      Non presente in ARF 1.10; specifico per IT-Wallet.

    **Dati di Identificazione Personale**
      Un insieme di dati che permettono di stabilire l'identità di una persona fisica o giuridica, o di una persona fisica che rappresenta un'altra persona fisica o giuridica.
      Allineato con ARF 1.10.

    **Fornitore di Attestati Elettronici di Dati di Identificazione Personale**
      Credential Issuer responsabile dell'emissione/revoca di PID, garantendo il binding crittografico all'Unità di Wallet.
      Allineato con ARF 1.10.

    **Policy Language**
      Linguaggio formale per definire politiche di sicurezza, privacy e gestione dell'identità.
      Non presente in ARF 1.10; specifico per IT-Wallet.

    **Attori Primari**
      Entità che implementano Soluzioni Tecniche per il Sistema IT-Wallet.
      Non presente in ARF 1.10; specifico per IT-Wallet.

    **Pseudonimo**
      Identificatore alternativo per privacy/anonimato, che consente autenticazione/autorizzazione.
      Allineato con ARF 1.10.

    **Attestato Elettronico di Attributi Qualificati**
      Attestazione digitalmente verificabile emessa da un QTSP, che sostanzia il possesso di attributi.
      Allineato con ARF 1.10.
    
    **Attestato Elettronico di Attributi**
      Attestazione digitalmente verificabile in forma elettronica, che sostanzia il possesso di attributi.
      Allineato con ARF 1.10.
    
    **Attestato Elettronico di Attributi rilasciato da o per conto di un ente pubblico**
    **Attestato Elettronico Pubblico di Attributi**
      Attestato Elettronico di Attributi che contiene Attributi derivanti da una Fonte Autentica pubblica.
      Allineato con ARF 1.10.

    **Attestato Elettronico di Interesse Pubblico**
    **Credenziale Elettronica di Interesse Pubblico**
      Attestato Elettronico di Attributi che contiene Attributi destinati a certificare il rilascio, da parte dello Stato o di altre pubbliche amministrazioni, di autorizzazioni, certificazioni, qualificazioni, documenti di identità e riconoscimento, ricevute di entrate, o ad assumere valore fiduciario e protezione della fede pubblica dopo la loro emissione o le annotazioni fatte su di essi e, in generale, quando sono considerati documenti di sicurezza ai sensi dell'Articolo 2, comma 10-bis, Legge 13 luglio 1966, n. 559.
      Non presente in ARF 1.10; specifico per IT-Wallet.
      
    **Attestato Elettronico di Dati di Identificazione Personale**
      Attestazione Elettronica che consente l'autenticazione del soggetto a cui si riferiscono i Dati di Identificazione Personale.
      Allineato con ARF 1.10.

    **Fornitore di Attestati Elettronici di Attributi Qualificati**
      Entità Organizzativa che fornisce QEAA.
      Allineato con ARF 1.10.

    **Fornitore di Attestati Elettronici di Attributi**
    **Fornitore di Attestati Elettronici**
      Entità Organizzativa che fornisce EAA.
      Allineato con ARF 1.10.

    **Fornitore Qualificato di Firme Elettroniche**
      Fornitore di Servizi di Trust che emette certificati di Firma Elettronica Qualificata.
      Allineato con ARF 1.10.

    **Registration Authority**
    **Registrar**
      Parte responsabile della registrazione delle Entità Organizzative emettendo Trust Assertion.
      Allineato con ARF 1.10.

    **Processo di Registrazione**
      Processo per verificare l'idoneità e la conformità delle Entità Organizzative.
      Allineato con ARF 1.10.

    **Relying Party**
      Entità che si basa sull'identificazione elettronica o sul Servizio di Trust da un'Istanza del Wallet.
      Allineato con ARF 1.10.

    **Soluzione di Relying Party**
      Prodotto (software/hardware/cloud) che abilita presentazioni di Credenziali in vari contesti.
      Non presente in ARF 1.10; specifico per IT-Wallet.

    **Backend della Relying Party**
      Infrastruttura remota con componenti lato server gestiti da un fornitore di Soluzione di Relying Party.
      Non presente in ARF 1.10; specifico per IT-Wallet.

    **Istanza di Relying Party**
    **App di Verifica**
      Distribuzione specifica di un'applicazione o dispositivo Relying Party.
      Allineato con ARF 1.10.

    **Divulgazione Selettiva**
      Funzionalità che consente all'Utente di inviare un sottoinsieme di Dati delle Credenziali Digitali.
      Allineato con ARF 1.10.

    **Self-Sovereign Identity (SSI)**
      Approccio che dà agli individui il controllo sulle loro informazioni di identità digitale.
      Non presente in ARF 1.10.

    **Signal Hub**
      Una piattaforma PDND gestita dal Gestore PDND che abilita la raccolta e distribuzione di Segnali. Consiste di due e-Service PDND: Raccolta Segnali e Distribuzione Segnali.

    **Segnale (Signal Hub)**
      Un segnale digitale propagato attraverso il PDND Signal Hub. È utilizzato dalle Fonti Autentiche per notificare ai Credential Issuer aggiornamenti su stati e/o informazioni all'interno di un dominio gestito dalla Fonte Autentica stessa.

    **Processo di Supervisione**
      Processo da parte di un Organismo di Supervisione per rivedere e garantire il corretto funzionamento del Fornitore di Wallet e altri.
      Non presente in ARF 1.10; specifico per IT-Wallet.

    **Soluzioni Tecniche**
      Sistemi e servizi hardware/software implementati dai Fornitori di Soluzioni Wallet, Fornitore di Attestati Elettronici di Dati di Identificazione Personale, ecc.
      Non presente in ARF 1.10; specifico per IT-Wallet.

    **Specifiche Tecniche**
      Specifiche che forniscono architettura tecnica, framework di implementazione e requisiti di design.
      Allineato con ARF 1.10.

    **Trust**
      Fiducia nella sicurezza, affidabilità e integrità delle entità e delle loro azioni.
      Non presente in ARF 1.10.

    **Trust Attestation**
      Attestazione elettronica di conformità al framework normativo, crittograficamente verificabile.
      Non presente in ARF 1.10.

    **Trust Evaluation**
      Processo di verifica dell'affidabilità delle Entità Organizzative registrate.
      Non presente in ARF 1.10.

    **Trust Framework**
      Insieme di regole e accordi legalmente applicabili per un sistema multi-parte.
      Non presente in ARF 1.10.

    **Trust Layer**
      Componente architetturale che consente ai partecipanti di stabilire trust.
      Non presente in ARF 1.10.

    **Trust Model**
      Raccolta di regole che garantiscono la legittimità di componenti/entità nell'ecosistema IT-Wallet.
      Non presente in ARF 1.10.

    **Trust Relationship**
      Relazione affidabile tra Entità Organizzative dopo la Trust Evaluation.
      Non presente in ARF 1.10.

    **Certificato di Accesso**
      Certificato che autentica e convalida la (Wallet-) Relying Party.
      Allineato con ARF 1.10.

    **Certificato di Registrazione**
      Oggetto dati che indica gli attributi che la Relying Party ha registrato per richiedere agli Utenti.
      Allineato con ARF 1.10.

    **Certificate Signing Request (CSR)**
      Richiesta inviata a una CA contenente la chiave pubblica e le informazioni identificative per un certificato digitale.
      Non presente in ARF 1.10.

    **Trusted List**
      Repository di informazioni su entità autorevoli e il loro stato.
      Allineato con ARF 1.10.

    **Utente**
      Persona fisica o giuridica che utilizza servizi di trust o mezzi di identificazione elettronica.
      Allineato con ARF 1.10.

    **Verificatore di Attestati Elettronici**
    **Verificatore di Credenziale**
      Una persona o entità che utilizza un'Istanza di Relying Party.
      Non presente in ARF 1.10; specifico per IT-Wallet.

    **Istanza del Wallet**
      Applicazione installata sul dispositivo di un Utente, parte dell'Unità di Wallet, che fornisce interfacce utente.
      Allineato con ARF 1.10.

    **Fornitore di Wallet**
      Entità Organizzativa responsabile della gestione e fornitura di una Soluzione Wallet.
      Allineato con ARF 1.10.

    **Backend del Fornitore del Portafoglio**
      Infrastruttura tecnica e componenti lato server gestiti da un Fornitore di Wallet.
      Allineato con ARF 1.10.

    **Applicazione Crittografica Sicura per il Portafoglio**
      Applicazione che gestisce Asset Critici utilizzando funzioni crittografiche fornite dal WSCD.
      Allineato con ARF 1.10.

    **Dispositivo Crittografico Sicuro per il Portafoglio**
      Dispositivo resistente alle manomissioni che fornisce un ambiente per il WSCA per proteggere gli Asset Critici.
      Allineato con ARF 1.10.

    **Soluzione Wallet**
      Insieme di Soluzioni Tecniche per il corretto funzionamento delle Istanze IT-Wallet.
      Allineato con ARF 1.10.

    **Unità di Wallet**
      Configurazione unica di una Soluzione Wallet per un singolo Utente, incluse le funzionalità di sicurezza.
      Allineato con ARF 1.10.

    **Attestato di Unità di Portafoglio**
    **Attestato del Wallet**
    **Attestato dell'Istanza del Wallet**
      Oggetto dati emesso da un Fornitore di Wallet che descrive i componenti dell'Unità di Wallet.
      Allineato con ARF 1.10.

    **Catalogo degli Attestati Elettronici**
      Catalogo elettronico contenente informazioni sui formati e schemi delle Credenziali Digitali, i dati contenuti e le Fonti Autentiche. Il Catalogo contiene informazioni aggiuntive che consentono di stabilire l'autenticità e l'affidabilità delle informazioni in esso contenute.
      Non presente in ARF 1.10; specifico per IT-Wallet.

    **Intermediario**
      Entità Intermedia come definita in `OID-FED`_ Sezione 1.2, ad esempio in IT-Wallet potrebbe essere un intermediario Relying Party che offre e gestisce, per conto della Relying Party, le Soluzioni Tecniche per la verifica remota o di prossimità degli Attestati Elettronici.
      Allineato con ARF 1.10.

.. note::
   Per qualsiasi termine non presente in ARF 1.10, la definizione IT-Wallet è fornita come autorevole per il contesto italiano.

Di seguito sono riportati i principali termini definiti e le definizioni relative agli aspetti dell'Esperienza dell'Utente:

.. glossary::
    :sorted:

    **Pulsante per l'autenticazione**
      L'Engagement Button che consente all'Utente di accedere al processo di Autenticazione e utilizzare i servizi forniti dai Verificatori di Attestati Elettronici.
  
    **Identità del Marchio**
      Raccolta di elementi visivi, verbali e strategici che un servizio, un prodotto o un'entità utilizza per presentarsi all'Utente e distinguersi dagli altri.
    
    **Catalogo**
      Sezione dell'Istanza del Wallet che visualizza l'elenco di tutte le Credenziali Digitali disponibili che possono essere ottenute tramite l'Istanza IT-Wallet, e da cui è possibile avviare il processo di emissione.
    
    **Call To Action**
      Un suggerimento chiaro e diretto che incoraggia gli utenti a compiere un'azione specifica. Può essere un pulsante, un link o un altro elemento che guida l'utente verso un obiettivo particolare.
    
    **Vista di Dettaglio**
      Modalità di visualizzazione estesa delle Credenziali Digitali, che mostra tutti gli Attributi inclusi.
    
    **Discovery Page**
      È la pagina del Touchpoint della Relying Party dove l'Utente atterra per accedere alla propria area autenticata, e ha l'obiettivo di mostrare all'Utente tutti i metodi di Autenticazione disponibili.
  
    **Engagement Button**
      Elemento interattivo dell'Interfaccia che consente all'Utente di attivare un processo (ad es. per Autenticarsi, per richiedere l'emissione di una Credenziale Digitale, ecc.).
  
    **Modello di Interazione**
      Un insieme di caratteristiche che definiscono come l'Utente interagisce con l'Interfaccia di uno o più Touchpoint per completare un compito o operazione e raggiungere un obiettivo specifico.
    
    **Interfaccia**
      L'insieme di elementi grafici, tipografici e interattivi attraverso i quali l'Utente interagisce con il/i Touchpoint responsabili della consegna di un prodotto o servizio, in conformità con [GL_DESIGN].
    
    **Visualizzazione in anteprima**
      Modalità di visualizzazione compatta della Credenziale Digitale che consente di riconoscerla e distinguerla in un elenco di Attestati Elettronici grazie alla presenza di dati o elementi minimi.
    
    **Modello di Servizio**
      Insieme di interazioni tra attori e touchpoint necessarie per la consegna e fruizione del servizio.
    
    **Touchpoint**
      Punto di contatto (digitale e non) tra l'Utente e il prodotto o servizio.
    
    **Trust Mark**
      Un elemento grafico che evidenzia la partecipazione degli Attori Primari al Sistema IT-Wallet e garantisce così l'aderenza ai suoi standard.
    
    **Esperienza dell'Utente**
      L'insieme delle percezioni e reazioni delle persone risultanti dall'uso e/o dall'aspettativa di uso di un prodotto, sistema o servizio.
      Allineato con ISO 9241-210:2010.

    **Identità Visiva**
      Insieme coerente di elementi grafici e tipografici che rappresentano visivamente un prodotto o servizio e lo rendono distinguibile e riconoscibile.

Acronimi
--------

Di seguito sono riportati i principali acronimi utilizzati nel documento:

.. list-table::
  :class: longtable
  :widths: 20 80
  :header-rows: 1

  * - **Acronimo**
    - **Descrizione**
  * - **AAL**
    - Authenticator Assurance Level come definito in `<https://csrc.nist.gov/glossary/term/authenticator_assurance_level>`_
  * - **ANPR**
    - Anagrafe Nazionale della Popolazione Residente
  * - **API**
    - Application Programming Interface
  * - **CAB**
    - Organismo di Valutazione della Conformità
  * - **CIE**
    - Carta di Identità Elettronica
  * - **EAA**
    - Attestato Elettronico di Attributi
  * - **IAM**
    - Identity and Access Management
  * - **LoA**
    - Livello di Garanzia
  * - **NAB**
    - Ente Nazionale di Accreditamento
  * - **OID4VP**
    - OpenID for Verifiable Presentation
  * - **PDND**
    - Piattaforma Digitale Nazionale Dati
  * - **PID**
    - Attestato Elettronico di Dati di Identificazione Personale
  * - **PII**
    - Informazioni Personalmente Identificabili
  * - **QEAA**
    - Attestato Elettronico di Attributi Qualificati
  * - **Pub-EAA**
    - Attestato Elettronico di Attributi rilasciato da o per conto di un ente pubblico
  * - **SSI**
    - Self Sovereign Identity
  * - **VC**
    - Verifiable Credential
  * - **VP**
    - Verifiable Presentation
  * - **WSCA**
    - Applicazione Crittografica Sicura per il Portafoglio
  * - **WSCD**
    - Dispositivo Crittografico Sicuro per il Portafoglio

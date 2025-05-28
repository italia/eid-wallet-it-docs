.. include:: ../common/common_definitions.rst


Riferimenti Normativi
=====================

[CAD]

Decreto Legislativo del 7 marzo 2005, n. 82 e successive modificazioni, recante il 'Codice dell'Amministrazione Digitale'.

[REF_ACCESSIBILITY]

Linee guida per l'accessibilità degli strumenti informatici ai sensi dell'articolo 11 della legge del 9 Gennaio 2004 n. 4. Direttiva UE 2019/882 del Parlamento Europeo e del Consiglio, del 17 aprile 2019, sui requisiti di accessibilità per prodotti e servizi.

[GL_DESIGN]

Linee guida per la progettazione dei siti web e dei servizi digitali forniti dalle pubbliche amministrazioni, ai sensi dell'articolo 53, comma 1-ter, del decreto legislativo del 7 marzo 2005, n. 82, e successive modificazioni.

Definizioni e Acronimi
=======================

Questa sezione mira ad uniformare la terminologia del Sistema IT-Wallet alle definizioni fornite in ARF 1.10 (vedere `ARF Annex 1 <https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/blob/main/docs/annexes/annex-1/annex-1-definitions.md>`_). Per ciascun termine, la definizione di IT-Wallet è stata confrontata e mappata con quella di ARF, includendo note su eventuali differenze o chiarimenti.

Le definizioni di *Utente*, *Servizio Fiduciario*, *Trust Model*, *Trusted List*, *Trust Framework*, *Attributo*, *Fornitore di Attestati Elettronici di Attributi* o *Fornitore di servizi fiduciari (TSP)*, *Person Identification Data (PID)*, *Lista di Revoca*, *Fornitore di Attestati Elettronici di Attributi qualificati* o *Fornitore di servizi fiduciari qualificati (QTSP)*, *Attestato Elettronico di Attributi (EAA)*, sono definite nel documento `EIDAS-ARF`_.

Di seguito le descrizioni di acronimi e definizioni, correlati al presente documento utili ad approfondimenti su tematiche inerenti l' IT-Wallet e i componenti con i quali interagisce.

.. glossary::
    :sorted:

    **Processo di Accreditamento**
      Procedura svolta dall'Ente di Accreditamento Nazionale per accreditare gli Organismi di Valutazione della conformità (CABs), che si conclude con il rilascio di un certificato di accreditamento.
      Non presente in ARF 1.10; specifico di IT-Wallet.

    **Attributi**
    **Attributi dell'Utente**
      Un insieme di caratteristiche, qualità, diritti o autorizzazioni di una persona fisica o giuridica o di un oggetto o anche una sola di queste informazioni. 
      Conforme con ARF 1.10.

    **Autenticazione**
      Processo elettronico che consente di confermare l'Identificazione di una persona fisica o giuridica, oppure l'origine/integrità dei dati.
      Conforme con ARF 1.10.

    **Fonte Autentica**
      Soggetto pubblico o privato responsabile di un archivio o sistema che è considerato fonte primaria per gli Attributi o per i Dati di Identificazione Personale.
      Conforme con ARF 1.10.    

    **Processo di Certificazione**
      Procedura svolta dagli Organismi di Valutazione della conformità (CABs) per certificare le Soluzioni Wallet, che comprende anche le valutazioni tecniche periodiche.
      Non presente in ARF 1.10; specifico di IT-Wallet.

    **Organismo di Valutazione della Conformità**
      Organismo accreditato valuta e certifica le Soluzioni di Portafogli o i Fornitori di Servizi Fiduciari.
      Conforme con ARF 1.10.

    **Fornitore di Attestati Elettronici**
      Soggetto pubblico o privato che fornisce Attestati Elettronici agli Utenti (può essere un fornitore di PID oppure un fornitore di (Q)EAA).
      ARF 1.10 utilizza definizioni similari; IT-Wallet aggrega sotto questo termine sia il fornitore di PID che di (Q)EAA .

    **Credential Status Assertion**
    **Status Assertion**
      Documento firmato attestante lo stato di validità attuale di un Attestato Elettronico.
      Non presente in ARF 1.10; specifico di IT-Wallet.

    **Asset Critici**
      Asset (ad esempio, le chiavi crittografiche) la cui perdita avrebbe gravi ripercussioni sulla Unità di Wallet.
      Conforme con ARF 1.10.

    **Cryptographic Hardware Key Tag**
      Identificativo univoco per le Cryptographic Hardware Keys, utilizzato per accedere alla chiave privata dell'hardware.
      Non presente in ARF 1.10.

    **Cryptographic Hardware Keys**
      Coppia di chiavi generata dall'Istanza del Wallet, valida per tutta la sua durata.
      Non presente in ARF 1.10.

    **Servizio di Integrità del Dispositivo**
      Servizio fornito dai produttori di dispositivi per verificare l'integrità delle app e l'archiviazione sicura delle chiavi.
      Service by device manufacturers to verify app integrity and secure key storage.
      Non presente in ARF 1.10.

    **Attestato Elettronico**
      Un set firmato di Attributi in un formato specifico (ad esempio mDoc-CBOR, SD-JWT VC), può essere un PID oppure una (Q)EAA.
      ARF 1.10 restringe la definizione ai soli formati mDoc-CBOR e SD-JWT VC; IT-Wallet sottolinea che la definizione è indipendente dal formato.

    **Autorità di Federazione**
      Ente di governance pubblica che emana linee guida, regole e gestisce Elenchi di Fiducia e lo stato dei partecipanti.
      Non presente in ARF 1.10.

    **Titolare**
    **Holder**
      Persona fisica o giuridica che riceve, gestisce e presenta Attestati Elettronici tramite l'Istanza del Wallet.
      Non presente in ARF 1.10; specifico di IT-Wallet.

    **Associazione Crittografica con l'Utente**
    **Holder Key Binding**
      Capacità del Titolare di dimostrare il possesso della chiave privata attestata da una terza parte di fiducia.
      Non presente in ARF 1.10.

    **Identity and Access Management (IAM)**
      Framework per la gestione delle identità digitali e dell'accesso alle informazioni.
      Non presente in ARF 1.10.

    **Sistema IT-Wallet**
      Insieme di Soluzioni Tecniche che implementano il Sistema di Wallet Digitale Italiano.
      Non presente in ARF 1.10; specifico di IT-Wallet.

    **Registro del Sistema IT-Wallet**
      Registro delle entità partecipanti al Sistema IT-Wallet.
      Non presente in ARF 1.10; specifico di IT-Wallet.

    **Key Attestation**
      Attestazione dell'OEM del dispositivo sull'archiviazione sicura delle chiavi nell' hardware-backed keystore.
      Non presente in ARF 1.10.

    **Livello di Garanzia**
      Grado di sicurezza della verifica dell'identità e nella presentazione degli Attestati Elettronici.
      Non presente in ARF 1.10.

    **Metadato**
      Artefatto digitale contenente informazioni su un'entità organizzativa (endpoint, chiavi pubbliche, ecc.).
      Conforme con ARF 1.10.

    **Ente Nazionali di Accreditamento**
      Organismo che esegue l'accreditamento sotto l'autorità di uno Stato membro.
      Conforme con ARF 1.10.

    **Gestore di Identità Digitale**
      Sistemi di identità preesistenti (ad esempio CIE) notificati eIDAS.
      Non presente in ARF 1.10.

    **Processo di Notifica**
      Procedura per l'invio delle informazioni alla Commissione Europea e l'inserimento all'interno delle Trusted List.
      Conforme con ARF 1.10.

    **Entità Organizzativa**
      Persona giuridica (pubblica o privata) riconosciuta per svolgere un ruolo nell'ecosistema IT-Wallet.
      Non presente in ARF 1.10; specifico di IT-Wallet.

    **Dati di Identificazione Personale**
      Insieme di dati che permettono di stabilire l'identità di una persona fisica o giuridica, o di una persona fisica che rappresenta un'altra persona fisica o giuridica.
      Conforme con ARF 1.10.

    **Fornitore di Attestati Elettronici di Dati di Identificazione Personale**
    **PID Provider**
      Fornitore di Attestato Elettronico responsabile dell'emissione/revoca del PID, garantendo l'associazione crittografica con l'Unità di Wallet.
      Conforme con ARF 1.10.

    **Policy Language**
      Linguaggio formale per la definizione di policy di sicurezza, privacy e gestione dell'identità.
      Non presente in ARF 1.10; specifico di IT-Wallet.

    **Attori Primari**
      Entità che realizzano le Soluzioni Tecniche per il funzionamento del Sistema IT-Wallet.
      Non presente in ARF 1.10; specifico di IT-Wallet.

    **Pseudonimo**
      Identificativo alternativo anonimo che consente l'autenticazione e l'autorizzazione da parte di un entità.
      Conforme con ARF 1.10.

    **Attestato Elettronico di Attributi Qualificati**
      Attestazione verificabile digitalmente emessa da un QTSP, che comprova il possesso di attributi.
      Conforme con ARF 1.10.
    
    **Attestato Elettronico di Attributi**
      Attestazione verificabile digitalmente in forma elettronica, comprovante il possesso di attributi.
      Conforme con ARF 1.10.
    
    **Attestato Elettronico di Attributi rilasciato da o per conto di un ente pubblico**
    **Attestato Elettronico Pubblico di Attributi**
      Attestato Elettronico di Attributi che contiene Attributi forniti da una Fonte Autentica pubblica.
      Conforme con ARF 1.10.

    **Attestato Elettronico di Interesse Pubblico**
      Attestato Elettronico di Attributi che contiene Attributi destinati ad attestare il rilascio, da parte dello Stato o di altre pubbliche amministrazioni, di autorizzazioni, certificazioni, abilitazioni, documenti di identità e riconoscimento, ricevute di introiti, ovvero ad assumere un valore fiduciario e di tutela della fede pubblica in seguito alla loro emissione o alle scritturazioni su di essi effettuate e, in generale, quando sono considerati carte valori ai sensi dell'articolo 2, comma 10-bis, della legge 13 luglio 1966, n. 559.
      Non presente in ARF 1.10; specifico di IT-Wallet.
      
    **Attestato Elettronico di Dati di Identificazione Personale**  
      Attestazione Elettronica che consente di autenticare il soggetto a cui si riferiscono i Dati Personali Identificativi.
      Conforme con ARF 1.10.

    **Fornitore di Attestati Elettronici di Attributi Qualificati**
      Entità Organizzativa che fornisce QEAAs.
      Conforme con ARF 1.10.

    **Fornitore di Attestati Elettronici di Attributi**
      Entità Organizzativa che fornisce EAAs.
      Conforme con ARF 1.10.

    **Fornitore Qualificato di Firme Elettroniche**
      Fornitore di Servizi Fiduciari che rilascia certificati di Firma Elettronica Qualificata.
      Conforme con ARF 1.10.

    **Registration Authority**
    **Registrar**
      Soggetto responsabile della registrazione delle Entità Organizzative mediante l'emissione di Attestati di Fiducia.
      Conforme con ARF 1.10.

    **Processo di Registrazione**
      Procedura per la verifica dell'idoneità e della conformità delle Entità Organizzative.
      Conforme con ARF 1.10.

    **Relying Party**
      Entità che si affida all'identificazione elettronica o al Servizio Fiduciario di un'Istanza del Wallet.
      Conforme con ARF 1.10.

    **Soluzione di Relying Party**
      Prodotto (software/hardware/cloud) che consente la presentazione degli Attestati Elettronici in vari contesti.
      Non presente in ARF 1.10; specifico di IT-Wallet.

    **Backend della Relying Party**
      Infrastruttura remota composta da componenti server gestiti da un fornitore di Soluzioni di Relying Party.
      Non presente in ARF 1.10; specifico di IT-Wallet.

    **Istanza di Relying Party**
    **App di Verifica**
      Istanza specifica di un'applicazione oppure dispositivo in dotazione ad una Relying Party.
      Conforme con ARF 1.10.

    **Divulgazione Selettiva**
      Funzionalità che consente all'Utente di inviare un sottoinsieme di dati contenuti in Attestati Elettronici.
      Conforme con ARF 1.10.

    **Self-Sovereign Identity (SSI)**
      Approccio che concede agli individui di avere il pieno controllo sulle informazioni relative alla propria identità digitale.
      Non presente in ARF 1.10.

    **Processo di Supervisione**
      Procedimento svolto da parte di un Organismo di Vigilanza per esaminare e garantire il corretto funzionamento del Fornitore di Wallet e di altre entità.
      Non presente in ARF 1.10; specifico di IT-Wallet.

    **Soluzioni Tecniche**
      Insieme dei sistemi hardware/software e dei servizi realizzati dai Fornitori di Wallet, Fornitori di Attestati Elettronici di Dati di Identificazione Personale, ecc.
      Non presente in ARF 1.10; specifico di IT-Wallet.

    **Specifiche Tecniche**
      Specifiche che forniscono l'architettura tecnica, il quadro implementativo e i requisiti di progettazione.
      Conforme con ARF 1.10.

    **Trust**
      Fiducia nell'affidabilità, sicurezza e integrità delle entità e delle loro azioni.
      Non presente in ARF 1.10.

    **Trust Attestation**
      Attestazione elettronica di conformità al quadro normativo, verificabile crittograficamente.
      Non presente in ARF 1.10.

    **Trust Evaluation**
      Processo di verifica dell'affidabilità delle Entità Organizzative registrate.
      Non presente in ARF 1.10.

    **Trust Framework**
      Insieme di regole e accordi giuridicamente vincolanti per un sistema composto da più attori.
      Non presente in ARF 1.10.

    **Trust Layer**
      Componente architetturale che consente ai partecipanti di stabilire un rapporto di fiducia.
      Non presente in ARF 1.10.

    **Trust Model**
      Insieme di regole che garantiscono la legittimità dei componenti/entità nell'ecosistema IT-Wallet.
      Non presente in ARF 1.10.

    **Trust Relationship**
      Affidabilità tra Entità Organizzative verificata in seguito alla Trust Evaluation.
      Non presente in ARF 1.10.

    **Certificato di Accesso**
      Certificato di autenticazione e convalida della (Wallet-) Relying Party.
      Conforme con ARF 1.10.

    **Certificato di Registrazione**
      Oggetto che indica gli Attributi che la Relying Party ha registrato al fine di richiederli agli Utenti.
      Conforme con ARF 1.10.

    **Certificate Signing Request (CSR)**
      Richiesta inviata a una CA contenente la chiave pubblica e le informazioni identificative utili all'emissione un certificato digitale.
      Non presente in ARF 1.10.

    **Trusted List**
      Archivio di informazioni sugli enti eutoritativi e sul loro stato.
      Conforme con ARF 1.10.

    **Utente**
      Persona fisica o giuridica che utilizza servizi fiduciari o mezzi di identificazione elettronica.
      Conforme con ARF 1.10.

    **Verificatore di Attestati Elettronici**
      Una persona o entità che utilizza un'istanza di Relying Party.
      Non presente in ARF 1.10; specifico di IT-Wallet.

    **Istanza del Wallet**
      Applicazione installata sul dispositivo di un Utente, parte di un'Unità di Wallet, che fornisce interfacce utente.
      Conforme con ARF 1.10.

    **Fornitore di Wallet**
      Entità organizzativa responsabile della gestione e della fornitura di una Soluzione Wallet.
      Conforme con ARF 1.10.

    **Backend del Fornitore di Wallet**
      Infrastruttura tecnica e componenti server gestiti da un Fornitore di Wallet.
      Conforme con ARF 1.10.

    **Applicazione Crittografica Sicura per il Wallet**
      Applicazione che gestisce gli Asset critici utilizzando le funzioni crittografiche fornite dal WSCD. Conforme con ARF 1.10.

    **Dispositivo Crittografico Sicuro per il Wallet**
      Dispositivo antimanomissione che fornisce un ambiente in cui la WSCA può proteggere gli Asset critici.
      Conforme con ARF 1.10.

    **Soluzione Wallet**
      Insieme di Soluzioni Tecniche al fine di garantire il corretto funzionamento delle istanze di IT-Wallet.
      Conforme con ARF 1.10.

    **Unità di Wallet**
      Configurazione unica di una Soluzione Wallet per un singolo Utente, incluse tutte le funzionalità di sicurezza.
      Conforme con ARF 1.10.

    **Attestato di Unità di Wallet**
      Oggetto emesso da un Fornitore di Wallet che descrive le caretteristiche e i componenti della Unità di Wallet.
      Conforme con ARF 1.10.

    **Catalogo degli Attestati Elettronici**
      Catalogo elettronico contenente informazioni relative ai formati e agli schemi degli Attestati Elettronici, ai dati in essi contenuti e alle Fonti Autentiche. Il Catalogo contiene informazioni aggiuntive che consentono di stabilire l'autenticità e l'affidabilità delle informazioni in esso contenute.
      Non presente in ARF 1.10; specifico di IT-Wallet.

    **Intermediario**
      Intermediario come definito nella Sezione 1.2 di `OID-FED`_, ad esempio in IT-Wallet potrebbe esistere intermediari della Relying Party, ovvero coloro che offrono e gestiscono, per conto della Relying Party, le Soluzioni Tecniche per la verifica remota o di prossimità delle Attestazioni Elettroniche.
      Conforme con ARF 1.10.

.. note::
   Qualora un termine non è presente nell'ARF 1.10, la definizione fornita in IT-Wallet è da ritenersi valida per il solo contesto italiano.

Di seguito sono riportati i principali termini e definizioni relativi agli aspetti della User Experience:

.. glossary::
    :sorted:

    **Authentication Button**
      Pulsante che consente all'Utente di avviare il processo di Autenticazione e di utilizzare i servizi forniti dai Verificatori di Attestati Elettronici.
  
    **Identità del Marchio**
      Insieme di elementi visivi, verbali e strategici che un servizio, un prodotto o un'entità utilizza per presentarsi all'Utente e per distinguersi dagli altri.

    **Catalogo**
      Funzionalità dell'Istanza del Wallet in cui viene visualizzato l'elenco di tutti gli Attestati Elettronici disponibili e ottenibili tramite l'istanza IT-Wallet, e dalle quali è possibile avviare il processo di emissione.
    
    **Call To Action**
      Suggerimento chiaro e diretto che incoraggia gli Utenti a intraprendere un'azione specifica. Può essere un pulsante, un link o un altro elemento che guida l'Utente verso un obiettivo specifico.
    
    **Vista di Dettaglio**
      Modalità di visualizzazione estesa degli Attestati Elettronici, che mostra tutti gli Attributi contenuti.
    
    **Discovery Page**
      È la pagina che rappresenta il Touchpoint con la Relying Party dove l'Utente atterra per accedere alla propria area autenticata e ha lo scopo di mostrare all'Utente tutti i metodi di Autenticazione disponibili.
  
    **Engagement Button**
      Elemento interattivo dell'interfaccia che consente all'Utente di avviare un processo (ad esempio per autenticarsi, per richiedere il rilascio di un attestato elettronico, ecc.).
  
    **Modello di Interazione**
      Insieme di caratteristiche che definiscono le modalità con cui l'Utente interagisce con l'Interfaccia di uno o più Touchpoint per completare un'attività o un'operazione e conseguire un determinato scopo.
    
    **Interfaccia**
      L'insieme degli elementi grafici, tipografici e interattivi attraverso i quali l'Utente interagisce con il/i Touchpoint preposto/i all'erogazione di un prodotto o servizio, nel rispetto di [GL_DESIGN].
    
    **Visualizzazione in Anteprima**
      Modalità di visualizzazione compatta dell'Attestato Elettronico Digitale che consente di riconoscerla e distinguerla in un elenco di Attestazioni Elettroniche mediante la presenza di dati o elementi minimi.

    **Modello di Servizio**
      Insieme di interazioni tra attori e Touchpoint necessari per l'erogazione e la fruizione del servizio.
    
    **Touchpoint**
      Punto di contatto (digitale e non) tra l'Utente e il prodotto o servizio.
    
    **Trust Mark**
      Un elemento grafico che fornisce la prova della partecipazione degli Attori Primari al sistema IT-Wallet e garantisce quindi il rispetto dei suoi standard.

    **Esperienza dell'Utente**
      L'insieme delle percezioni e delle reazioni delle persone derivanti dall'uso e/o dalle aspettative d'uso di un prodotto, sistema o servizio.
      In linea con la norma ISO 9241-210:2010.

    **Identità Visiva**
      Insieme coerente di elementi grafici e tipografici che rappresentano visivamente un prodotto o un servizio e lo rendono distinguibile e riconoscibile.

Acronimi
--------

Di seguito gli acronimi usati più di frequente nel documento:

.. list-table::
  :class: longtable
  :widths: 20 80
  :header-rows: 1

  * - **Acronimo**
    - **Description**
  * - **AAL**
    - Authenticator Assurance Level come definito `<https://csrc.nist.gov/glossary/term/authenticator_assurance_level>`_ (Livello di Garanzia dell'Autenticatore)
  * - **ANPR**
    - Anagrafe Nazionale della Popolazione Residente (Italian National Registry of the Resident Population)
  * - **API**
    - Application Programming Interface. Insieme componenti previsti per semplificare gli scenari di integrazione di uno specifico Sistema.
  * - **CAB**
    - Conformity Assessment Body (Organismo di Valutazione della Conformità)
  * - **CIE**
    - Carta di Identità Elettronica
  * - **EAA**
    - Electronic Attestation of Attributes (Attestato Elettronico di Attributi)
  * - **NAB**
    - National Accreditation Body (Ente Nazionale di Accreditamento)
  * - **IAM**
    - Identity and Access Management (Gestione dell'Identità e degli Accessi)
  * - **LoA**
    - Level of Assurance (Livello di Garanzia)
  * - **OID4VP**
    - OpenID for Verifiable Presentation
  * - **PDND**
    - Piattaforma Digitale Nazionale Dati
  * - **PID**
    - Person Identification Data (Attestato Elettronico di Dati di Identificazione Personale)
  * - **PII**
    - Personally Identifiable Information (Informazioni di Identificazione Personale)
  * - **QEAA**
    - Qualified Electronic Attestation of Attributes (Attestato Elettronico di Attributi Qualificati)
  * - **Pub-EAA**
    - Electronic Attestation of Attributes issued by or on behalf of a public sector body (Attestato Elettronico di Attributi rilasciato da o per conto di un ente pubblico)
  * - **SSI**
    - Self Sovereign Identity
  * - **VC**
    - Verifiable Credential
  * - **VP**
    - Verifiable Presentation
  * - **WSCA**
    - Wallet Secure Cryptographic Application (Applicazione Crittografica Sicura per il Wallet)
  * - **WSCD**
    - Wallet Secure Cryptographic Device (Dispositivo Crittografico Sicuro per il Wallet)

Linguaggio Normativo e Convenzioni
==================================

Conformemente agli RFC 2119 e 8174 le seguenti parole chiave solamente quando appaiono con tutte le lettere in maiuscolo assumono i significati di seguito riportati:

  - DEVE/DEVONO: indicano un requisito che è necessario soddisfare.
  - NON DEVE/NON DEVONO: indicano un divieto assoluto.
  - PUO'/POSSONO: indicano un requisito opzionale, ovvero si può scegliere di soddisfarlo o meno senza alcun tipo di implicazione. 
  - DOVREBBE/DOVREBBERO/RACCOMANDATO: indicano un requisito consigliato/raccomandato, ovvero si devono tenere in considerazione tutte le implicazioni derivanti da una eventuale scelta alternativa.
  - NON DOVREBBE/NON DOVREBBERO/NON RACCOMANDATO: indicano un requisito che non è consigliato/raccomandato, ovvero si devono tenere in considerazione tutte le implicazioni derivanti dalla eventuale scelta di applicare comunque il requisito.
  - OBBLIGATORIO: necessario
  - OPZIONALE: facoltativo




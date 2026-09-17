.. include:: ../common/common_definitions.rst
.. Incluso tramite trust-evaluation.rst al livello di titolo '-' (livello 1).

Trust Evaluation in the National Trust Framework
-----------------------------------------------------

Questa sezione definisce le procedure di trust evaluation del Trust Framework Nazionale.
Gli Entity Type Identifier e i metadata di ciascun ruolo, usati durante queste procedure, sono definiti in :ref:`infrastructure-trust:Entity Type Identifiers and Metadata`, secondo tale profilo.
Le regole di selezione che definiscono quando queste procedure si applicano sono dettagliate in :ref:`trust-evaluation:Trust Framework Selection`.
Queste procedure si applicano quando la Trust Evaluated Party è autenticata sotto il Trust Framework Nazionale.

I Trust Artifact usati durante queste procedure, cioè l'Entity Configuration, i Subordinate Statement, i Trust Mark, sono definiti in :ref:`infrastructure-trust:National Trust Artifacts`.

Le procedure definite in questa sezione sono eseguite all'interno dei flussi operativi di Emissione e Presentazione (vedi :ref:`digital-credential-flows:Flussi relativi agli Attestati Elettronici`).
I parametri su cui operano, come il Request Object firmato, la mdoc Request, i Metadata di tutte le Entità coinvolte e il modello dati degli Attestati Elettronici ricevuti, sono definiti nelle rispettive sezioni (vedi :ref:`entities:Entità`, :ref:`remote-flow:Request Object` per il Remote Flow, e :ref:`credential-data-model:Formato Attestato Elettronico SD-JWT-VC` e :ref:`credential-data-model:Formato Attestato Elettronico mdoc-CBOR` per i formati degli Attestati Elettronici).

Trust Evaluation Processes by Context
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Le procedure sono definite in forma generale, con un **Trust Evaluator** e una **Trust Evaluated Party** e la tabella seguente definisce quale entità agisce in quale ruolo, quando e per quale scopo.

.. _table_national_tf_roles:
.. list-table:: Processi di Trust Evaluation per Entità e Contesto nel Trust Framework Nazionale
    :class: longtable
    :widths: 12 20 40 28
    :header-rows: 1

    * - **Entità**
      - **Contesto**
      - **In qualità di Trust Evaluator, implementa**
      - **In qualità di Trust Evaluated Party, fornisce**
    * - Wallet Unit
      - Emissione di una Credenziale esclusivamente nazionale
      - Sul Credential Issuer:

        - :ref:`trust-evaluation:Federation Entity Authentication`
        - :ref:`trust-evaluation:Authorization`
        - :ref:`trust-evaluation:Metadata Retrieval and Validation`

        Sull'Attestato ricevuto:

        - :ref:`trust-evaluation:Signing Trust Anchor Validation Procedure`
      - La Wallet Instance Attestation con la prova di possesso della chiave attestata, validata come definito in :ref:`trust-evaluation:Wallet Unit Authentication`.
    * - Wallet Unit
      - Presentazione remota, prefisso ``openid_federation``
      - Sulla Relying Party:

        - :ref:`trust-evaluation:Federation Entity Authentication`
        - :ref:`trust-evaluation:Authorization`, incluso l'Overasking Check
        - :ref:`trust-evaluation:Metadata Retrieval and Validation`
      - Nessun artifact a livello di entità è richiesto dalla Wallet Unit.
    * - Wallet Unit
      - Presentazione in prossimità
      - Sulla Relying Party:

        - :ref:`trust-evaluation:Relying Party Proximity Authentication`
        - :ref:`trust-evaluation:Authorization`, incluso l'Overasking Check, sul Trust Mark di registrazione fornito per valore nel ``requestInfo`` dell'ISO ``DeviceRequest``
      - Nessun artifact a livello di entità è richiesto dalla Wallet Unit.
    * - Credential Issuer
      - Emissione di Credenziali esclusivamente nazionali
      - Sulla Wallet Unit:

        - :ref:`trust-evaluation:Wallet Unit Authentication`
      - L'Entity Configuration (:ref:`infrastructure-trust:Entity Configuration`) con i Trust Mark di registrazione (:ref:`infrastructure-trust:Trust Mark registration-entity`), e gli artifact di emissione firmati con chiavi risolvibili attraverso la federazione, validati come definito in :ref:`trust-evaluation:Federation Entity Authentication`.
        Per il formato mdoc, il certificato Document Signer nell'header ``x5chain``, validato come definito in :ref:`trust-evaluation:X.509 Certificate Chain Validation`.
    * - Relying Party
      - Presentazione remota, prefisso ``openid_federation``
      - Sugli Attestati ricevuti:

        - :ref:`trust-evaluation:Signing Trust Anchor Validation Procedure`

        Sul Wallet Provider, per invocare il Wallet attraverso il meccanismo di discovery nazionale (vedi la nota di seguito):

        - :ref:`trust-evaluation:Metadata Retrieval and Validation`
      - L'Entity Configuration (:ref:`infrastructure-trust:Entity Configuration`) con i Trust Mark di registrazione (:ref:`infrastructure-trust:Trust Mark registration-entity`), e il Request Object firmato con chiavi risolvibili attraverso la federazione, incluso l'header ``trust_chain`` quando è attesa una validazione offline, validati come definito in :ref:`trust-evaluation:Federation Entity Authentication` e :ref:`trust-evaluation:Authorization`.
    * - Relying Party Intermediary
      - Presentazione remota, in qualità di Federation Intermediate di una Relying Party affiliata
      - Non agisce come Trust Evaluator nei flussi operativi.
      - L'Entity Configuration (:ref:`infrastructure-trust:Entity Configuration`) con il Trust Mark di registrazione ``intermediate`` (vedi :ref:`infrastructure-trust:Trust Mark Types and Schema`), e i Subordinate Statement delle sue Relying Party affiliate.
        L'Intermediary è validato come parte della Trust Chain della Relying Party affiliata, i cui ``authority_hints`` puntano a esso.
        La Wallet Unit DEVE verificare che la Trust Chain della Relying Party affiliata sia validata attraverso un Intermediary riconosciuto o direttamente attraverso il Federation Trust Anchor, e informa l'Utente come definito in :ref:`trust-evaluation:User Transparency`.

.. note::
  Nel remote flow la Relying Party invoca il Wallet attraverso app link (universal link) invece di custom URL scheme.
  Questa scelta di IT-Wallet richiede che la Relying Party ottenga e validi preventivamente i metadata del Wallet Provider, costruendo la Trust Chain relativa al Wallet Provider (Metadata Retrieval and Validation), come parte del Wallet Metadata Retrieval Flow (vedi :ref:`wallet-metadata-retrieval:Flusso di Recupero dei Wallet Metadata` e la Selection Page in :ref:`functionalities:Design dell'Esperienza Utente`).
  Questo meccanismo è specifico del remote flow e non si applica al proximity flow.


Federation Trust Anchor Distribution and Validation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Federation Trust Anchor Distribution
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

La configurazione della federazione è pubblicata dal Federation Trust Anchor all'interno della sua Entity Configuration, disponibile al path web well-known **.well-known/openid-federation**.
Tutte le Entità DEVONO ottenere la configurazione della federazione prima di entrare nella fase operativa e DEVONO mantenerla aggiornata.
La configurazione della federazione contiene le chiavi pubbliche del Federation Trust Anchor per le operazioni di firma e gli endpoint di federazione (vedi :ref:`infrastructure-trust:Entity Configuration`).

Il Federation Trust Anchor DEVE distribuire le proprie Federation Public Keys attraverso meccanismi sicuri out-of-band.
Quando è richiesta una validazione del Federation Trust Anchor, tutte le Entità DEVONO confrontare le chiavi pubbliche del Federation Trust Anchor con quelle ottenute dall'Entity Configuration del Federation Trust Anchor, e DEVONO scartare qualsiasi chiave che non corrisponda.

.. note::
  All'interno di IT-Wallet il canale out-of-band è il canale di contatto stabilito con l'Entità durante il processo di registrazione (vedi :ref:`onboarding-system:Entity Registration`).

Le Entità POSSONO inoltre effettuare il pinning delle chiavi pubbliche del Federation Trust Anchor, nella loro configurazione locale.
Una configurazione pinnata PUÒ essere usata solo finché è valida e DEVE essere aggiornata quando si verifica una rotazione di chiave.

L'Entity Configuration del Federation Trust Anchor fornisce inoltre i Signing Trust Anchor della PKI di firma X.509, usati per verificare le Credenziali ancorate a questo framework, e i National Wallet Trust Anchor usati per verificare le Wallet Unit Attestation e le Key Attestation.
La loro distribuzione e validazione sono definite in :ref:`trust-evaluation:Signing Trust Anchor Distribution` e :ref:`trust-evaluation:Wallet Trust Anchor Distribution`, rispettivamente, in quanto concernono la verifica di un'attestation e non la validazione del Federation Trust Anchor.

Federation Trust Anchor Validation
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Input**

- Il Federation Entity Identifier del Federation Trust Anchor.
- Le chiavi pubbliche del Federation Trust Anchor ottenute out-of-band, oppure una configurazione pinnata.

**Esito**

- L'insieme validato delle Federation Public Keys del Federation Trust Anchor.
- La configurazione della federazione, inclusi gli endpoint di federazione.

**Processo**

La verifica dell'Entity Configuration è la validazione dell'Entity Statement definita in `OID-FED`_ Sezione 3.2, applicata all'Entity Configuration self-issued del Federation Trust Anchor e completata, all'interno di IT-Wallet, con il confronto out-of-band delle chiavi.

1. Recuperare l'Entity Configuration dall'endpoint well-known del Federation Trust Anchor, servita con il media type ``application/entity-statement+jwt``.
2. Verificare che l'Entity Configuration sia un JWT firmato con ``iss`` e ``sub`` uguali all'identificatore del Federation Trust Anchor, e verificare la sua firma con una delle chiavi contenute nel suo ``jwks``.
   Gli algoritmi di firma supportati sono definiti in :ref:`algorithms:Algoritmi Crittografici`.
3. Confrontare le chiavi in ``jwks`` con le chiavi ottenute out-of-band o pinnate, scartando le chiavi che non corrispondono.
4. Controllare la validità temporale dell'Entity Configuration attraverso i claim ``iat`` e ``exp``.
5. Estrarre gli endpoint di federazione dai metadata ``federation_entity``, e il claim ``trust_mark_issuers`` (vedi :ref:`infrastructure-trust:Entity Configuration`).

Se un qualsiasi passo fallisce, la configurazione della federazione NON DEVE essere usata.

Federation Trust Anchor Key Rotation and Historical Verification
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Quando è richiesto di validare una Trust Chain nel tempo, anche se il Federation Trust Anchor ha cambiato le proprie chiavi crittografiche per la firma digitale, l'endpoint Federation Historical Keys rende sempre disponibili le chiavi non più usate per le verifiche storiche delle firme.
Questa proprietà supporta la non ripudiabilità delle attestation a lunga durata.

Quando il Federation Trust Anchor ruota le proprie chiavi, le nuove chiavi sono distribuite con lo stesso meccanismo out-of-band usato per la distribuzione iniziale.
Le Entità che effettuano il pinning delle chiavi del Federation Trust Anchor DEVONO aggiornare di conseguenza il materiale pinnato.

Trust Chain Validation
^^^^^^^^^^^^^^^^^^^^^^^^

La Trust Chain Validation è una procedura tecnica usata dai processi di trust evaluation definiti in questa sezione per scopi diversi.
A seconda che un'entità stia valutando una dichiarazione di federazione o che un artifact rechi la catena di certificati X.509 usata per la sua firma, si applicano due procedure diverse di Trust Chain Validation.

Federation Trust Chain
"""""""""""""""""""""""""

La Trust Chain è una sequenza di dichiarazioni verificate che valida la conformità di un'Entità alla federazione.
Ha una data di scadenza, oltre la quale DEVE essere rinnovata per ottenere metadata freschi e aggiornati.
La data di scadenza della Trust Chain è determinata dal timestamp di scadenza più precoce tra tutte le dichiarazioni.
Nessuna Entità può forzare la data di scadenza della Trust Chain a essere superiore a quella configurata dal Federation Trust Anchor.

Questa procedura verifica la Trust Chain.
La derivazione dei metadata finali del subject, ottenuta applicando le metadata policy recate dalle dichiarazioni della Trust Chain, è definita in :ref:`trust-evaluation:Metadata Retrieval and Validation`.
Secondo `OID-FED`_, la verifica della catena e la derivazione dei metadata finali è indicata come la **resolution of a Trust Chain**.

La Trust Chain è costruita attraverso il processo di **Federation Entity Discovery** definito in `OID-FED`_:

- Il Trust Evaluator recupera l'Entity Configuration del subject.
- Segue gli ``authority_hints`` per raccogliere i Subordinate Statement emessi dalle entità superiori.
- Continua fino a raggiungere il Federation Trust Anchor.

La Trust Chain PUÒ anche essere mantenuta valida con il **fast renewal method** definito in `OID-FED`_ Sezione 3.1.3, che evita un processo di discovery completo recuperando i Subordinate Statement direttamente attraverso il loro claim ``source_endpoint``.

La Trust Chain PUÒ anche essere fornita staticamente dal subject all'interno di un artifact firmato, usando il parametro di header JOSE ``trust_chain`` definito in `OID-FED`_ Sezione 4.3.
All'interno di IT-Wallet l'header ``trust_chain`` è recato nel Request Object del flusso di presentazione (vedi :ref:`remote-flow:Request Object`) e negli artifact firmati del flusso di emissione (`OPENID4VCI`_ Appendice F.1 e Sezione 12.2.3).
Una Trust Chain fornita staticamente richiede di essere aggiornata solo quando è disponibile una connessione internet, mentre DEVE essere aggiornata quando risulta scaduta.

La revoca di un'Entità è realizzata con l'indisponibilità del Subordinate Statement a essa relativo.
Se il Federation Trust Anchor o il suo Intermediate non pubblica un Subordinate Statement valido, o se ne pubblica uno scaduto o non valido, il subject del Subordinate Statement DEVE essere inteso come non valido o revocato.
Per il Trust Evaluator, questo controllo in tempo reale dello status di revoca è possibile solo online, recuperando il Subordinate Statement al momento della verifica.

Le Trust Chain possono anche essere verificate offline, usando una delle chiavi pubbliche del Federation Trust Anchor.
In questo caso il controllo in tempo reale della revoca non è disponibile, e si fa affidamento sulla freshness della Trust Chain.

La validità massima di una Trust Chain può essere imposta dal Federation Trust Anchor, che la imposta attraverso la scadenza delle proprie dichiarazioni, come descritto sopra.
Indipendentemente da tale validità, ai fini dello status di revoca delle Entità una Trust Chain costruita più di 24 ore prima del momento della verifica NON DOVREBBE essere considerata valida.
Quando è necessario fare affidamento sullo status di revoca di un'Entità e un controllo online in tempo reale non è disponibile, una Trust Chain più vecchia di 24 ore DOVREBBE essere rinnovata prima che l'interazione possa procedere.
Questo limite di 24 ore si applica all'età della Trust Chain, calcolata dalla sua costruzione, ed è indipendente dalla sua data di scadenza.

**Input**

- Il Federation Entity Identifier del subject, oppure una Trust Chain fornita staticamente.
- Le Federation Public Keys del Federation Trust Anchor validate (vedi :ref:`trust-evaluation:Federation Trust Anchor Distribution`).

**Esito**

- Una Trust Chain validata, cioè l'insieme ordinato di dichiarazioni verificate, con la sua data di scadenza.

**Processo**

I passi seguenti verificano una Trust Chain secondo `OID-FED`_, con il puntatore alla parte rilevante della specifica per ciascun passo:

1. Ottenere l'Entity Configuration del subject, oppure prendere il primo elemento della Trust Chain fornita staticamente.
2. Raccogliere i Subordinate Statement seguendo gli ``authority_hints`` fino al Federation Trust Anchor, oppure prenderli dalla Trust Chain statica.
   I Subordinate Statement sono ottenuti dal fetch endpoint (`OID-FED`_ Sezione 8.1).
3. Validare ciascuna dichiarazione come Entity Statement secondo `OID-FED`_ Sezione 3.2, cioè verificarne la firma, la coerenza dei claim ``iss`` e ``sub``, e la sua validità temporale.
   Ciascun Subordinate Statement è verificato con le Federation Entity Keys del suo issuer, attestate dalla dichiarazione superiore.

   - La dichiarazione emessa dal Federation Trust Anchor è verificata con le chiavi validate del Federation Trust Anchor.
   - L'Entity Configuration del subject è verificata con le chiavi attestate nel Subordinate Statement a essa relativo.

4. Applicare i vincoli recati nei Subordinate Statement lungo la catena, come definito in `OID-FED`_ Sezione 6.2.
   In particolare, verificare che i metadata Entity Type pubblicati dal subject siano all'interno degli ``allowed_entity_types``, considerando che l'Entity Type ``federation_entity`` è sempre consentito, e che il numero di Intermediate non ecceda il ``max_path_length`` impostato dai superiori.
5. Calcolare la scadenza della Trust Chain come il valore ``exp`` più precoce tra le dichiarazioni.

Se una qualsiasi verifica fallisce, la Trust Chain DEVE essere considerata non valida e il subject NON DEVE essere considerato fidato sulla sua base.

X.509 Certificate Chain Validation
"""""""""""""""""""""""""""""""""""""

Questa variante si applica quando un artifact è fornito insieme alla catena di certificati X.509 usata per la firma.
Per gli artifact in formato JOSE la catena è recata nel parametro di header ``x5c``, come definito in :rfc:`7515` e usato in IT-Wallet nel Request Object del flusso di presentazione (vedi :ref:`remote-flow:Request Object`).
Per le Credenziali in formato mdoc la catena è recata nell'unprotected header ``x5chain`` (elemento 33) del Mobile Security Object, come definito in :rfc:`9360` e in :ref:`credential-data-model:Mobile Security Object`.
La catena contiene il certificato Document Signer e qualsiasi certificato intermedio.
NON DEVE contenere il certificato Signing Trust Anchor, che è distribuito come definito in :ref:`trust-evaluation:Signing Trust Anchor Distribution`.

La validazione del certification path è la path validation X.509 standard definita in :rfc:`5280#section-6`, con il controllo dello status di revoca definito in :rfc:`5280` e :rfc:`6960`.
Il ciclo di vita dei certificati e i meccanismi di revoca, inclusa la CRL, sono definiti in :ref:`infrastructure-trust:Revocation Mechanisms`.
Questa è la stessa validazione del certification path usata nel Trust Framework EUDIW (vedi :ref:`trust-evaluation:X509 Certificate Chain Validation Algorithm`); l'unica differenza è l'origine del trust anchor e l'estrazione aggiuntiva del Federation Entity Identifier.
In questa sezione, per il Trust Framework Nazionale, i dettagli dell'algoritmo non sono ridefiniti.

All'interno del Trust Framework Nazionale si applica quanto segue.

  - Il trust anchor della path validation è il Signing Trust Anchor applicabile, ottenuto come definito in :ref:`trust-evaluation:Signing Trust Anchor Distribution`.
  - Il certificato end-entity reca l'OpenID Federation Entity Identifier del subject nell'URI ``subjectAltName``.
    Questo è l'elemento che collega la firma X.509 all'identità di federazione del firmatario.
    Pertanto, la validazione estrae questo identificatore in modo che il processo chiamante possa verificare che il certificato che ha firmato l'artifact appartenga all'entità OpenID Federation attesa per quell'artifact.
    Il confronto rispetto all'identificatore atteso, per esempio l'``iss`` della Credenziale, è eseguito dal processo chiamante (vedi :ref:`trust-evaluation:Signing Trust Anchor Validation Procedure`).
    Questa variante produce solo l'identificatore e non stabilisce di per sé quale identificatore sia atteso.

.. note::
  L'emissione di questi Certificati X.509 e l'operazione della PKI di firma sono definite nella procedura di onboarding e sono fuori dallo scope di questa sezione (vedi :ref:`onboarding-system:Onboarding Processes`).

**Input**

- La catena di certificati estratta dall'header dell'artifact, cioè il certificato Document Signer e qualsiasi certificato intermedio.
- Il certificato Signing Trust Anchor applicabile, ottenuto come definito in :ref:`trust-evaluation:Signing Trust Anchor Distribution`.

**Esito**

- Il certificato end-entity validato.
- L'OpenID Federation Entity Identifier del firmatario, estratto dall'URI ``subjectAltName``, da abbinare rispetto all'issuer atteso da parte del processo chiamante.

**Processo**

1. Costruire il certification path dal certificato end-entity al certificato Signing Trust Anchor.
2. Eseguire la path validation definita in :rfc:`5280#section-6`, usando il Signing Trust Anchor come input trust anchor dell'algoritmo.
3. Verificare lo status di revoca dei certificati nel path, secondo :rfc:`5280` e :rfc:`6960`.
4. Estrarre l'OpenID Federation Entity Identifier dall'URI ``subjectAltName`` del certificato end-entity, e restituirlo al processo chiamante per l'abbinamento rispetto all'issuer atteso.

Se un qualsiasi passo fallisce, la firma dell'artifact NON DEVE essere verificata con la catena di certificati presentata.

Signing Trust Anchor Distribution and Validation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Questo processo fornisce e valida la root of trust per la verifica dell'issuer data authentication di un'attestation.

Il Signing Trust Anchor è la root of trust della PKI X.509 usata per firmare gli Attestati Elettronici i cui Rulebook li ancorano al Trust Framework Nazionale.

È distinto dal Federation Trust Anchor di :ref:`trust-evaluation:Federation Trust Anchor Distribution` in quanto il Federation Trust Anchor è la root delle dichiarazioni di federazione, mentre un Signing Trust Anchor è la root di un certification path che valida la firma di un'attestation.
Il Federation Trust Anchor e un Signing Trust Anchor POSSONO essere operati dalla stessa organizzazione, ma sono relazioni di fiducia diverse, con cicli di vita diversi e canali di revoca diversi.

POSSONO esserci più di un Signing Trust Anchor.
Ciascun Credential Issuer che firma Credenziali in questo framework usa un Signing Trust Anchor come root dei propri certificati Document Signer.
Credential Issuer diversi POSSONO fare affidamento su Signing Trust Anchor diversi.

Signing Trust Anchor Distribution
"""""""""""""""""""""""""""""""""

I Signing Trust Anchor sono distribuiti attraverso l'Entity Configuration del Federation Trust Anchor.
Ciascun certificato Signing Trust Anchor è fornito nel parametro ``x5c`` di una JWK dedicata, distinta dalle Federation Entity Keys usate per firmare le dichiarazioni di federazione.
Questo meccanismo di distribuzione è un'implementazione specifica di IT-Wallet e non è definito da `OID-FED`_.

Le Entità POSSONO effettuare il pinning di un Signing Trust Anchor nella loro configurazione locale.
Un Signing Trust Anchor pinnato PUÒ essere usato solo finché è valido e DEVE essere aggiornato quando il Signing Trust Anchor è ruotato.

Il risultato di questa distribuzione è, per ciascun Trust Evaluator, l'insieme dei certificati Signing Trust Anchor validati, ciascuno associato al Federation Entity Identifier dei Credential Issuer che vi fanno affidamento.
Questo insieme è il materiale di trust anchor consumato dalla procedura di validazione seguente.

.. note::
  L'emissione dei certificati Document Signer e l'operazione della PKI di firma sono definite nella procedura di onboarding e non sono nello scope di questa sezione (vedi :ref:`onboarding-system:Onboarding Processes`).

Signing Trust Anchor Validation Procedure
"""""""""""""""""""""""""""""""""""""""""

La procedura dipende dal formato dell'attestation.

Per le attestation in formato JOSE, come gli Attestati Elettronici in formato SD-JWT VC e la Wallet Instance Attestation, l'issuer è identificato dal claim ``iss`` e la chiave di verifica della firma è referenziata dal parametro di header ``kid``.
La chiave DEVE essere risolta all'interno dei metadata finali dell'issuer, ottenuti attraverso la Federation Trust Chain.
L'artifact PUÒ recare l'header JOSE ``trust_chain`` per consentire la validazione senza un nuovo processo di discovery.

Per le Credenziali in formato mdoc il Mobile Security Object reca il certificato Document Signer nell'header ``x5chain``.
La firma è verificata con tale certificato.
Il Signing Trust Anchor dell'issuer è validato estraendo l'OpenID Federation Entity Identifier dall'URI ``subjectAltName`` e validando il certification path rispetto al Signing Trust Anchor applicabile ottenuto come definito in :ref:`trust-evaluation:Signing Trust Anchor Distribution`.

**Input**

- L'attestation firmata.
- La configurazione validata del Federation Trust Anchor e il Signing Trust Anchor applicabile.

**Esito**

- Il trust anchor validato e la chiave o il certificato di firma per l'attestation.
- La conferma che la chiave di firma appartiene all'issuer dell'attestation.

**Processo**

1. Per gli artifact JOSE, derivare i metadata finali dell'issuer dalla Federation Trust Chain (vedi :ref:`trust-evaluation:Federation Trust Chain` e :ref:`trust-evaluation:Metadata Retrieval and Validation`) e selezionare la chiave referenziata dall'header ``kid``.
2. Per gli artifact mdoc, validare l'``x5chain`` come definito in :ref:`trust-evaluation:X.509 Certificate Chain Validation` e verificare che l'OpenID Federation Entity Identifier nell'URI ``subjectAltName`` corrisponda all'issuer atteso.
3. Verificare la firma dell'attestation con la chiave o il certificato selezionato.

.. note::
  Quando richiesto, l'endpoint Federation Historical Keys e le CRL pubblicate DEVONO essere usati per assicurare che l'attestation fosse valida al momento dell'emissione o della presentazione (vedi :ref:`trust-evaluation:Federation Trust Anchor Key Rotation and Historical Verification` per maggiori dettagli).

Il ciclo di vita dei certificati di firma DEVE essere mantenuto allineato all'insieme di configurazione di federazione delle chiavi dell'issuer.
Quando una chiave di firma è ruotata o non è più valida, la JWK corrispondente DEVE essere rimossa dall'Entity Configuration o ruotata, e il certificato correlato DEVE essere revocato di conseguenza.
All'interno di IT-Wallet, quando la configurazione di federazione e lo status del certificato divergono, DEVE prevalere lo stato più restrittivo, e pertanto una chiave revocata in una delle due viste DEVE essere considerata revocata.

Wallet Trust Anchor Distribution and Validation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Questo processo stabilisce e valida il National Wallet Trust Anchor usato per validare le Wallet Instance Attestation e le Key Attestation emesse da un Wallet Provider nel Trust Framework Nazionale.

Il National Wallet Trust Anchor è la root della PKI X.509 usata dal Wallet Provider per firmare le Wallet Unit Attestation. È distinto dal Federation Trust Anchor, che è la root delle dichiarazioni di federazione, e dal Signing Trust Anchor usato da un Credential Issuer per gli Attestati Elettronici.

Wallet Trust Anchor Validation
""""""""""""""""""""""""""""""""""""""

Per una Wallet Instance Attestation o una Key Attestation che reca una catena di certificati di firma X.509, il Trust Evaluator DEVE validare la catena rispetto al National Wallet Trust Anchor applicabile prima di accettare la firma dell'attestation.

**Input**

- La Wallet Instance Attestation o Key Attestation firmata e la sua catena di certificati di firma.
- La Trust Chain validata del Wallet Provider.
- Il National Wallet Trust Anchor applicabile ottenuto come definito in :ref:`trust-evaluation:Wallet Trust Anchor Distribution`.

**Esito**

- Il certificato di firma del Wallet Provider e l'attestation validati.
- La conferma che il certificato di firma appartiene al Wallet Provider identificato dalla Trust Chain validata.

**Processo**

1. Validare la Trust Chain del Wallet Provider e derivarne i metadata finali come definito in :ref:`trust-evaluation:Federation Trust Chain` e :ref:`trust-evaluation:Metadata Retrieval and Validation`.
2. Estrarre la catena di certificati di firma dall'header JOSE ``x5c`` della Wallet Instance Attestation o Key Attestation. Il National Wallet Trust Anchor NON DEVE essere incluso in questa catena.
3. Validare la catena di certificati rispetto al National Wallet Trust Anchor applicabile come definito in :ref:`trust-evaluation:X.509 Certificate Chain Validation`.
4. Verificare la firma dell'attestation con il certificato end-entity validato.
5. Verificare che il Federation Entity Identifier estratto dal certificato end-entity corrisponda al Wallet Provider identificato dalla Trust Chain.
6. Controllare la validità temporale e lo status di revoca dell'attestation come richiesto dal profilo di attestation applicabile.

Se un qualsiasi passo fallisce, la Wallet Instance Attestation o Key Attestation NON DEVE essere considerata emessa da un Wallet Provider fidato.

Wallet Trust Anchor Distribution
""""""""""""""""""""""""""""""""

Il National Wallet Trust Anchor DEVE essere distribuito attraverso l'Entity Configuration del Federation Trust Anchor. DEVE essere rappresentato da una JWK dedicata il cui parametro ``x5c`` contiene il certificato National Wallet Trust Anchor. La JWK dedicata DEVE essere distinta dalle Federation Entity Keys usate per firmare le dichiarazioni di federazione.

Il Trust Evaluator DEVE validare l'Entity Configuration del Federation Trust Anchor e la Trust Chain del Wallet Provider prima di accettare il National Wallet Trust Anchor. La configurazione risultante DEVE associare il National Wallet Trust Anchor al Federation Entity Identifier del Wallet Provider.

Le Entità POSSONO effettuare il pinning del National Wallet Trust Anchor nella loro configurazione locale. Un National Wallet Trust Anchor pinnato PUÒ essere usato solo finché è valido e DEVE essere aggiornato quando il National Wallet Trust Anchor è ruotato.

Quando un Wallet Provider opera sia nel Trust Framework Nazionale sia nel Trust Framework EUDIW, il National Wallet Trust Anchor DEVE essere lo stesso certificato del Trust Anchor notificato alla Commissione europea e pubblicato nella LoTE dei Wallet Provider sotto il ``ServiceDigitalIdentity`` del Wallet Provider.

Authentication Trust Anchor Distribution
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gli Authentication Trust Anchor sono distribuiti attraverso l'Entity Configuration del Federation Trust Anchor con lo stesso meccanismo usato per i Signing Trust Anchor.
Ciascun certificato Authentication Trust Anchor è fornito nel parametro ``x5c`` di una JWK dedicata, distinta dalle Federation Entity Keys.

Un Authentication Trust Anchor è la root della PKI di autenticazione X.509 che emette i certificati di autenticazione della Relying Party usati nel Proximity Flow.
Questi certificati seguono lo stesso profilo del Wallet-Relying Party Access Certificate (vedi :ref:`infrastructure-trust:Wallet-Relying Party Access Certificate (WRPAC) Profile`).

.. note::
  L'emissione dei certificati di autenticazione della Relying Party e l'operazione della PKI di autenticazione sono definite nella procedura di onboarding e non sono nello scope di questa sezione (vedi :ref:`onboarding-system:Onboarding Processes`).

Authentication
^^^^^^^^^^^^^^^^^^^^

Il processo di Authentication ha lo scopo di affermare l'identità della Trust Evaluated Party.
Sono definite tre procedure:

- Federation Entity Authentication si applica alle entità che pubblicano un'Entity Configuration, nel Remote Flow.
- Wallet Unit Authentication si applica alla Wallet Unit, che non è una Federation Entity.
- Relying Party Proximity Authentication si applica alla Relying Party nel Proximity Flow.

Federation Entity Authentication
"""""""""""""""""""""""""""""""""""

L'identità della Trust Evaluated Party e le sue chiavi sono stabilite attraverso la Trust Chain.
La Trust Evaluated Party autentica se stessa in una data interazione firmando l'artifact di protocollo di tale interazione con una chiave privata la cui parte pubblica è pubblicata nei suoi metadata finali, ottenuti risolvendo la Trust Chain.
Il parametro di header ``kid``, come definito in :rfc:`7515`, referenzia una chiave contenuta nei metadata finali della Trust Evaluated Party.
L'insieme completo dei parametri di header di ciascun artifact firmato è definito nella corrispondente sezione di protocollo.

**Input**

- L'artifact di protocollo firmato.
- Il Federation Entity Identifier dichiarato dalla Trust Evaluated Party.
- Una Trust Chain relativa alla Trust Evaluated Party, fornita staticamente o costruita attraverso la discovery.

**Esito**

Il Trust Evaluator DEVE produrre ``AUTHENTICATED`` o ``NON_AUTHENTICATED``.
Nel secondo caso la Trust Evaluated Party NON DEVE essere considerata autenticata e l'interazione NON DEVE continuare.
La notifica all'Utente e il divieto di retry cross scheme sono definiti in :ref:`trust-evaluation:Failure Handling`.

**Processo**

1. Validare la Trust Chain relativa alla Trust Evaluated Party e derivarne i metadata finali (vedi :ref:`trust-evaluation:Federation Trust Chain` e :ref:`trust-evaluation:Metadata Retrieval and Validation`).
2. Verificare che l'identificatore di entità recato dall'artifact, per esempio il claim ``client_id`` o ``iss``, corrisponda al subject della Trust Chain.
3. Selezionare all'interno dei metadata finali la chiave pubblica referenziata dall'header ``kid``.
4. Verificare la firma dell'artifact con la chiave selezionata.

La verifica con successo fornisce sia l'autenticazione della Trust Evaluated Party sia la prova di possesso della sua chiave privata.

Wallet Unit Authentication
"""""""""""""""""""""""""""""""""""

La Wallet Instance Attestation convoglia la chiave pubblica della Wallet Unit che è usata per validare la firma sulla Wallet Instance Attestation.
Il formato e il flusso di emissione sono definiti in :ref:`wallet-instance-attestation-issuance:Emissione della Wallet Instance Attestation`.

La valutazione DEVE seguire il modello definito in OpenID Federation for Wallet Architectures.
La Wallet Unit si autentica con un meccanismo di Client authentication che fornisce la Wallet Instance Attestation emessa dal suo Wallet Provider, insieme alla prova di possesso della chiave attestata.
Nel flusso di emissione questo è realizzato con OAuth 2.0 Attestation-Based Client Authentication, cioè i parametri ``OAuth-Client-Attestation`` e ``OAuth-Client-Attestation-PoP`` (`OAUTH-ATTESTATION-CLIENT-AUTH`_), come descritto in `OPENID4VCI`_.
Per stabilire la fiducia nella Wallet Unit, il Trust Evaluator DEVE:

- Stabilire la fiducia nel Wallet Provider che ha emesso la Wallet Instance Attestation.
- Validare la Wallet Instance Attestation come definito in :ref:`trust-evaluation:Wallet Trust Anchor Validation` usando il National Wallet Trust Anchor.

**Input**

- La Wallet Instance Attestation presentata dalla Wallet Unit.
- La prova di possesso della chiave attestata nella Wallet Instance Attestation.
- Una Trust Chain relativa al Wallet Provider.

**Esito**

Il Trust Evaluator DEVE produrre ``AUTHENTICATED`` o ``NON_AUTHENTICATED`` per la Wallet Unit.

**Processo**

1. Validare la Trust Chain relativa al Wallet Provider che ha emesso la Wallet Instance Attestation e derivarne i metadata finali (vedi :ref:`trust-evaluation:Federation Trust Chain` e :ref:`trust-evaluation:Metadata Retrieval and Validation`).
2. Validare la Wallet Instance Attestation come definito in :ref:`trust-evaluation:Wallet Trust Anchor Validation` usando il National Wallet Trust Anchor.
3. Controllare la validità temporale e lo status di revoca della Wallet Instance Attestation.
4. Verificare la prova di possesso della chiave attestata, secondo il protocollo in uso.

Relying Party Proximity Authentication
"""""""""""""""""""""""""""""""""""""""

Nel Proximity Flow la Relying Party è autenticata attraverso l'mdoc reader authentication definita in [`ISO18013-5`_].
La Relying Party firma il session transcript con la chiave privata del suo certificato di autenticazione e fornisce la catena di certificati nell'header ``x5chain`` del ``ReaderAuth``.
Il certification path termina in un Authentication Trust Anchor distribuito come definito in :ref:`trust-evaluation:Authentication Trust Anchor Distribution`.

**Input**

- Il ``ReaderAuth`` firmato dalla Relying Party, con la catena del certificato di autenticazione nell'header ``x5chain``.
- L'Authentication Trust Anchor applicabile.

**Esito**

Il Trust Evaluator DEVE produrre ``AUTHENTICATED`` o ``NON_AUTHENTICATED``.
Nel secondo caso la Relying Party NON DEVE essere considerata autenticata e l'interazione NON DEVE continuare.

**Processo**

1. Estrarre la catena di certificati dall'header ``x5chain`` del ``ReaderAuth``.
2. Validare il certification path rispetto all'Authentication Trust Anchor applicabile come definito in :ref:`trust-evaluation:X.509 Certificate Chain Validation`.
3. Verificare la firma del ``ReaderAuth`` sul session transcript con il certificato di autenticazione validato.

La verifica con successo fornisce sia l'autenticazione della Relying Party sia la prova di possesso della chiave privata del suo certificato di autenticazione.

Authorization
^^^^^^^^^^^^^^^^^^

I dati di autorizzazione di un'entità sono forniti dal Trust Mark di registrazione emesso dal Registrar attraverso la Federation Authority.
Il Trust Mark di registrazione è funzionalmente analogo al Wallet-Relying Party Registration Certificate del Trust Framework EUDIW, e riutilizza gli stessi nomi di campo per i dati di autorizzazione.
Attesta la registrazione dell'entità e reca le sue ``entitlements`` e, ove applicabile, le ``provides_attestations`` o le ``credentials`` che è autorizzata a emettere o a richiedere.
La sua struttura è definita in :ref:`infrastructure-trust:Trust Mark registration-entity` e lo schema degli identificatori in :ref:`infrastructure-trust:Trust Mark Types and Schema`.

Il processo di Authorization è composto dalle seguenti procedure:

1. Trust Mark Validation, che stabilisce la validità del Trust Mark di registrazione.
   Si applica a tutte le Entità registrate.
2. Entitlement Check, che verifica che il ruolo e, in emissione, i tipi di Credenziale della Trust Evaluated Party siano autorizzati.
   Si applica a tutte le Wallet-Relying Party, cioè Credential Issuer e Relying Party.
3. Overasking Check, che verifica in presentazione che una Relying Party richieda solo gli Attestati Elettronici e gli attributi che è autorizzata a richiedere.
   Si applica alle Relying Party.

L'autorizzazione di ruolo comune a entrambe le fasi è eseguita dall'Entitlement Check; i controlli specifici di fase sono il controllo del tipo di Credenziale in emissione, all'interno dell'Entitlement Check, e l'Overasking Check a livello di attributo in presentazione.

Il Trust Evaluator DEVE eseguire il processo di Authorization solo dopo che la Trust Evaluated Party è stata autenticata con successo.

Trust Mark Validation
"""""""""""""""""""""""

**Input**

- Il Trust Mark *registration-entity*, ottenuto nel Remote Flow dal claim ``trust_marks`` dell'Entity Configuration o dall'endpoint Federation Trust Mark (`OID-FED`_ Sezione 8.6), oppure fornito per valore nel ``requestInfo`` dell'ISO ``DeviceRequest`` nel Proximity Flow.
- La configurazione validata del Federation Trust Anchor.

**Esito**

Il Trust Evaluator DEVE produrre ``TRUST_MARK_VALID`` o ``TRUST_MARK_INVALID``.
Un esito ``TRUST_MARK_INVALID`` sul Trust Mark di registrazione significa che l'entità non è autorizzata a operare.
In questo caso il Trust Evaluator DEVE trattare l'entità come non autorizzata e NON DEVE procedere con l'Entitlement Check.

**Processo**

1. Verificare che l'issuer del Trust Mark sia autorizzato per quel ``trust_mark_type``, secondo il claim ``trust_mark_issuers`` dell'Entity Configuration del Federation Trust Anchor.
   Il Trust Mark di registrazione, cioè un Trust Mark il cui ``trust_mark_type`` ha lo scopo ``registration-entity``, è soggetto a due controlli aggiuntivi.
   La Trust Mark Validation verifica che il ``trust_mark_type`` corrisponda all'identificatore di registrazione atteso per il ruolo del subject, e che l'issuer sia il Federation Trust Anchor, poiché il Trust Mark di registrazione DEVE essere emesso solo dal Federation Trust Anchor (vedi :ref:`infrastructure-trust:Trust Mark Types and Schema`).
2. Verificare la firma del Trust Mark con le Federation Entity Keys del suo issuer, ottenute attraverso la Trust Chain quando l'issuer non è il Federation Trust Anchor.
3. Controllare la validità temporale del Trust Mark attraverso i claim ``iat`` e ``exp``.
4. Quando online, controllare lo status del Trust Mark attraverso l'endpoint Federation Trust Mark Status (`OID-FED`_ Sezione 8.4).

Entitlement Check
"""""""""""""""""""""

Le entitlement definiscono ciò che l'entità è autorizzata a fare, come i tipi di Credenziale che può emettere o gli attributi che può richiedere.
All'interno di IT-Wallet questi dati di autorizzazione sono recati nel Trust Mark di registrazione, nei claim ``entitlements``, ``provides_attestations`` e ``credentials`` definiti in :ref:`infrastructure-trust:Trust Mark Types and Schema`, e NON DEVONO essere derivati dai soli metadata.

**Input**

- I Trust Mark validati della Trust Evaluated Party.
- Il ruolo della Trust Evaluated Party e l'azione attesa nell'interazione corrente.
  In emissione, il tipo di Credential Issuer e i tipi di Credenziale che dichiara di emettere.
  In presentazione, gli Attestati Elettronici e gli attributi richiesti dalla Relying Party.

**Esito**

Il Trust Evaluator DEVE produrre ``ENTITLEMENT_VALID`` o ``WRONG_ENTITLEMENT``.

**Processo**

1. Estrarre le ``entitlements`` dai Trust Mark validati e verificare che corrispondano al ruolo atteso nell'interazione corrente, per esempio che un'entità che agisce come Credential Issuer detenga un'entitlement di emissione di `ETSI TS 119 475`_ Allegato A.2.
2. Durante l'emissione, verificare che il tipo di Credenziale offerto sia presente nelle ``provides_attestations`` del Trust Mark, confrontando il ``format`` e il ``meta`` della Credenziale offerta rispetto alle entry autorizzate.
3. Durante la presentazione, il controllo a livello di attributo rispetto alle ``credentials`` del Trust Mark è eseguito dall'Overasking Check seguente.

Overasking Check
"""""""""""""""""

**Input**

- La richiesta di presentazione.
- Le ``credentials`` recate nel Trust Mark validato, cioè le query di Credenziale che la Relying Party è autorizzata a richiedere.

**Esito**

La Wallet Unit DEVE produrre ``VERIFICATION_PASSED`` o ``OVERASKING_DETECTED``, identificando gli attributi o gli Attestati Elettronici non registrati.
Su ``OVERASKING_DETECTED`` la Wallet Unit NON DEVE divulgare gli attributi che non sono autorizzati e DEVE informare l'Utente dell'overasking rilevato.

**Processo**

1. Estrarre gli Attestati Elettronici e gli attributi richiesti dalla richiesta, dalla query DCQL definita in `OpenID4VP`_ nel remote flow, oppure dai namespace richiesti nel proximity flow.
2. Per ciascuna Credenziale richiesta, selezionare nelle ``credentials`` del Trust Mark l'entry autorizzata con lo stesso ``format`` e ``meta``, per esempio gli stessi ``vct_values`` o ``doctype_value``.
3. Verificare che ogni attributo richiesto sia presente nei path ``claim`` dell'entry autorizzata selezionata.
   Se la richiesta contiene una Credenziale o un attributo senza una corrispondente entry autorizzata, l'output è ``OVERASKING_DETECTED``.
4. L'abbinamento DEVE essere esatto e case sensitive.

User Transparency
"""""""""""""""""

Oltre ai controlli automatici precedenti, il Trust Mark di registrazione fornisce claim che non sono valutati come regola decisionale ma sono presentati all'Utente per trasparenza, a supporto della decisione di procedere con l'interazione prima che qualsiasi attributo sia divulgato.
Prima della disclosure, la Wallet Unit DEVE informare l'Utente dell'identità della Relying Party e degli Attestati Elettronici e attributi richiesti, e presenta i claim di trasparenza aggiuntivi del Trust Mark a supporto della decisione informata.
Questo è coerente con l'approvazione dell'Utente che conclude la presentazione, come definito in :ref:`trust-evaluation:Authorization Decision and Override Rules`.

I claim di trasparenza recati nel Trust Mark sono i seguenti:

- ``organization_name``, la denominazione legale dell'entità;
- ``srv_description``, la descrizione del servizio fornito dall'entità;
- ``purpose``, le finalità di trattamento dei dati, per una Relying Party che richiede Credenziali;
- ``privacy_policy``, l'URL della privacy policy, per una Relying Party che richiede Credenziali;
- ``supervisory_authority``, l'Autorità di protezione dei dati a cui l'Utente può segnalare anomalie;
- ``public_body``, se l'entità è un organismo del settore pubblico;
- ``support_uri``, il contatto per le richieste relative all'entità, come la cancellazione o la portabilità dei dati.

Le loro definizioni sono fornite in :ref:`infrastructure-trust:Trust Mark Types and Schema`.

Quando la Relying Party opera attraverso un Relying Party Intermediary nel **National Trust Framework**, la Wallet Unit DEVE inoltre informare l'Utente che la Relying Party opera attraverso tale Intermediary, visualizzando l'identità di entrambi.
L'Intermediary è il Federation Intermediate nella Trust Chain della Relying Party, registrato con il Trust Mark ``intermediate`` (vedi :ref:`infrastructure-trust:Trust Mark Types and Schema`), ed è pertanto identificabile dalla Trust Chain validata senza artifact aggiuntivi.

Quando la stessa presentazione è valutata nel **EUDIW Trust Framework**, la Wallet Unit NON DEVE visualizzare i trade name dell'Intermediary o del Servizio dell'Intermediary ([`EIDAS-ARF`_] RPI_07).
Visualizza la Relying Party intermediata e il suo Servizio, come definito in :ref:`trust-evaluation:EUDIW Authorization`.

Metadata Retrieval and Validation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

I metadata di una Federation Entity DEVONO essere consumati solo nella loro forma finale, cioè i metadata risultanti dall'applicazione delle metadata policy ai metadata pubblicati nell'Entity Configuration, lungo la Trust Chain validata (vedi :ref:`trust-evaluation:Federation Trust Chain`).
I metadata pubblicati nell'Entity Configuration NON DEVONO essere usati senza questa elaborazione.

I tipi di metadata e i loro parametri sono definiti in :ref:`infrastructure-trust:Entity Type Identifiers and Metadata` e nelle specifiche di protocollo ivi referenziate.

La configurazione della Wallet Unit è fornita dal Wallet Provider all'interno dei suoi metadata come definito in :ref:`wallet-solution-metadata:Metadati della Soluzione Wallet`.

**Input**

- Una Trust Chain validata relativa al subject (vedi :ref:`trust-evaluation:Federation Trust Chain`).

**Esito**

- I metadata finali del subject, per ciascun tipo di metadata rilevante per l'interazione.

**Processo**

1. Applicare la ``metadata_policy`` delle dichiarazioni superiori ai metadata pubblicati nell'Entity Configuration del subject, lungo la Trust Chain, secondo `OID-FED`_ Sezione 6.1, ottenendo i metadata finali.
2. Selezionare il tipo di metadata corrispondente al ruolo del subject nell'interazione.
3. Verificare la presenza dei parametri che sono OBBLIGATORI per quel tipo di metadata.
4. Usare gli endpoint, le chiavi e gli algoritmi solo dai metadata finali.

Quando i metadata sono ottenuti attraverso una Trust Chain fornita staticamente, DEVONO essere aggiornati quando la Trust Chain scade, come definito in :ref:`trust-evaluation:Federation Trust Chain`.

.. note::
  All'interno di IT-Wallet la ``metadata_policy`` copre solo i parametri di configurazione tecnica, come endpoint, chiavi crittografiche e algoritmi supportati.
  Le entitlement e le policy di autorizzazione NON DEVONO essere espresse attraverso metadata policy; sono recate dai Trust Mark, come definito in :ref:`trust-evaluation:Authorization`.

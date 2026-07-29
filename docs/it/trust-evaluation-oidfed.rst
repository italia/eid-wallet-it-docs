.. include:: ../common/common_definitions.rst
.. Included via trust-evaluation.rst at title level '-' (level 1).

Trust Evaluation in the National Trust Framework
-----------------------------------------------------

Questa sezione definisce le procedure di trust evaluation del Trust Framework Nazionale.
Gli Entity Type Identifiers e i metadata di ciascun ruolo, utilizzati durante queste procedure, sono definiti in :ref:`infrastructure-trust:Entity Type Identifiers and Metadata`, secondo quel profilo.
Le regole di selezione che definiscono quando si applicano queste procedure sono dettagliate in :ref:`trust-evaluation:Trust Framework Selection`.

Gli Artifact di Trust utilizzati durante queste procedure, cioè l'Entity Configuration, le Subordinate Statements, le Trust Mark, sono definiti in :ref:`infrastructure-trust:National Trust Artifacts`.

Le procedure definite in questa sezione sono eseguite all'interno dei flussi operativi di Issuance e Presentation (vedi :ref:`digital-credential-flows:Flussi relativi agli Attestati Elettronici`).
I parametri su cui operano, come il signed Request Object, l'mdoc Request, i Metadata di tutte le Entità coinvolte e il modello dati delle Digital Credentials ricevute, sono definiti nelle rispettive sezioni (vedi :ref:`entities:Entità`, :ref:`remote-flow:Request Object` per il Remote Flow, e :ref:`credential-data-model:Formato Attestato Elettronico SD-JWT-VC` e :ref:`credential-data-model:Formato Attestato Elettronico mdoc-CBOR` per i formati delle Digital Credentials).

Trust Evaluation Processes by Context
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Le procedure sono definite in forma generale, con un **Trust Evaluator** e un **Trust Evaluated Party**, e la tabella seguente definisce quale entità agisce in quale ruolo, quando e per quale scopo.

.. _table_national_tf_roles:
.. list-table:: Trust Evaluation Processes by Entity and Context in the National Trust Framework
    :class: longtable
    :widths: 12 20 40 28
    :header-rows: 1

    * - **Entity**
      - **Context**
      - **As Trust Evaluator, implements**
      - **As Trust Evaluated Party, provides**
    * - Wallet Unit
      - Issuance of a national only Credential
      - Sul Credential Issuer:

        - :ref:`trust-evaluation:Federation Entity Authentication`
        - :ref:`trust-evaluation:Authorization`
        - :ref:`trust-evaluation:Metadata Retrieval and Validation`

        Sulla Credenziale ricevuta:

        - :ref:`trust-evaluation:Signing Trust Anchor Validation Procedure`
      - La Wallet Instance Attestation con la prova di possesso della chiave attestata, convalidata come definito in :ref:`trust-evaluation:Wallet Unit Authentication`.
    * - Wallet Unit
      - Remote presentation, ``openid_federation`` prefix
      - Sul Relying Party:

        - :ref:`trust-evaluation:Federation Entity Authentication`
        - :ref:`trust-evaluation:Authorization`, incluso l'Overasking Check
        - :ref:`trust-evaluation:Metadata Retrieval and Validation`
      - Nessun artifact a livello di entità è richiesto dalla Wallet Unit.
    * - Wallet Unit
      - Proximity presentation
      - Sul Relying Party:

        - :ref:`trust-evaluation:Relying Party Proximity Authentication`
        - :ref:`trust-evaluation:Authorization`, incluso l'Overasking Check, sulla registration Trust Mark fornita by value nel ``requestInfo`` dell'ISO ``DeviceRequest``
      - Nessun artifact a livello di entità è richiesto dalla Wallet Unit.
    * - Credential Issuer
      - Issuing national only Credentials
      - Sulla Wallet Unit:

        - :ref:`trust-evaluation:Wallet Unit Authentication`
      - L'Entity Configuration (:ref:`infrastructure-trust:Entity Configuration`) con le registration Trust Mark (:ref:`infrastructure-trust:Trust Mark registration-entity`), e gli artifact di issuance firmati con chiavi risolvibili tramite la federazione, convalidati come definito in :ref:`trust-evaluation:Federation Entity Authentication`.
        Per il formato mdoc, il Document Signer certificate nell'header ``x5chain``, convalidato come definito in :ref:`trust-evaluation:X.509 Certificate Chain Validation`.
    * - Relying Party
      - Remote presentation, ``openid_federation`` prefix
      - Sulle Credenziali ricevute:

        - :ref:`trust-evaluation:Signing Trust Anchor Validation Procedure`

        Sul Wallet Provider, per invocare il Wallet tramite il meccanismo di discovery nazionale (vedi la nota di seguito):

        - :ref:`trust-evaluation:Metadata Retrieval and Validation`
      - L'Entity Configuration (:ref:`infrastructure-trust:Entity Configuration`) con le registration Trust Mark (:ref:`infrastructure-trust:Trust Mark registration-entity`), e il signed Request Object con chiavi risolvibili tramite la federazione, incluso l'header ``trust_chain`` quando è attesa la validazione offline, convalidati come definito in :ref:`trust-evaluation:Federation Entity Authentication` e :ref:`trust-evaluation:Authorization`.
    * - Relying Party Intermediary
      - Remote presentation, as the Federation Intermediate of an affiliated Relying Party
      - Non agisce come Trust Evaluator nei flussi operativi.
      - L'Entity Configuration (:ref:`infrastructure-trust:Entity Configuration`) con la registration Trust Mark ``intermediate`` (vedi :ref:`infrastructure-trust:Trust Mark Types and Schema`), e le Subordinate Statements dei Relying Party affiliati.
        L'Intermediary è convalidato come parte della Trust Chain del Relying Party affiliato, i cui ``authority_hints`` puntano ad esso.
        La Wallet Unit DEVE verificare che la Trust Chain del Relying Party affiliato sia convalidata tramite un Intermediary riconosciuto oppure direttamente tramite la Federation Trust Anchor, e informa l'Utente come definito in :ref:`trust-evaluation:User Transparency`.

.. note::
  Nel remote flow il Relying Party invoca il Wallet tramite app links (universal links) invece di custom URL schemes.
  Questa scelta IT-Wallet richiede al Relying Party di ottenere e convalidare i metadata del Wallet Provider in anticipo, costruendo la Trust Chain sul Wallet Provider (Metadata Retrieval and Validation), come parte del Wallet Metadata Retrieval Flow (vedi :ref:`wallet-metadata-retrieval:Flusso di Recupero dei Wallet Metadata` e la Selection Page in :ref:`functionalities:Design dell'Esperienza Utente`).
  Questo meccanismo è specifico del remote flow e non si applica al proximity flow.


Federation Trust Anchor Distribution and Validation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Federation Trust Anchor Distribution
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

La configurazione della federazione è pubblicata dalla Federation Trust Anchor all'interno della sua Entity Configuration, disponibile al well-known web path **.well-known/openid-federation**.
Tutte le Entità DEVONO ottenere la configurazione della federazione prima di entrare nella fase operativa e DEVONO mantenerla aggiornata.
La configurazione della federazione contiene le Federation Trust Anchor public keys per le operazioni di firma e gli endpoint della federazione (vedi :ref:`infrastructure-trust:Entity Configuration`).

La Federation Trust Anchor DEVE distribuire le sue Federation Public Keys tramite meccanismi out-of-band sicuri.
Quando è richiesta una Federation Trust Anchor validation, tutte le Entità DEVONO confrontare le Federation Trust Anchor public keys con quelle ottenute dalla Federation Trust Anchor Entity Configuration, e DEVONO scartare qualsiasi chiave che non corrisponda.

.. note::
  All'interno di IT-Wallet il canale out-of-band è il canale di contatto stabilito con l'Entità durante il processo di registrazione (vedi :ref:`onboarding-system:Entity Registration`).

Le Entità POSSONO inoltre effettuare il pin delle Federation Trust Anchor public keys nella propria configurazione locale.
Una configurazione pinned PUÒ essere utilizzata solo finché è valida e DEVE essere aggiornata quando avviene una key rotation.

La Federation Trust Anchor Entity Configuration fornisce anche le Signing Trust Anchors della signing PKI X.509, utilizzate per verificare le Credenziali ancorate a questo framework.
La loro distribuzione e validazione sono definite in :ref:`trust-evaluation:Signing Trust Anchor Distribution`, poiché riguardano la verifica di un'attestazione e non la validazione della Federation Trust Anchor.

Federation Trust Anchor Validation
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Input**

- Il Federation Entity Identifier della Federation Trust Anchor.
- Le Federation Trust Anchor public keys ottenute out-of-band, oppure una configurazione pinned.

**Outcome**

- L'insieme convalidato di Federation Trust Anchor Federation Public Keys.
- La configurazione della federazione, inclusi gli endpoint della federazione.

**Process**

La verifica dell'Entity Configuration è la Entity Statement validation definita in `OID-FED`_ Section 3.2, applicata all'Entity Configuration self-issued della Federation Trust Anchor e completata, all'interno di IT-Wallet, con il confronto out-of-band delle chiavi.

1. Recuperare l'Entity Configuration dal well-known endpoint della Federation Trust Anchor, servita con il media type ``application/entity-statement+jwt``.
2. Verificare che l'Entity Configuration sia un JWT firmato con ``iss`` e ``sub`` uguali all'identificatore della Federation Trust Anchor, e verificarne la firma con una delle chiavi contenute nel suo ``jwks``.
   Gli algoritmi di firma supportati sono definiti in :ref:`algorithms:Algoritmi Crittografici`.
3. Confrontare le chiavi in ``jwks`` con quelle ottenute out-of-band o pinned, scartando le chiavi che non corrispondono.
4. Verificare la validità temporale dell'Entity Configuration tramite i claim ``iat`` e ``exp``.
5. Estrarre gli endpoint della federazione dai metadata ``federation_entity``, e il claim ``trust_mark_issuers`` (vedi :ref:`infrastructure-trust:Entity Configuration`).

Se un passo fallisce, la configurazione della federazione NON DEVE essere utilizzata.

Federation Trust Anchor Key Rotation and Historical Verification
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Quando è necessario convalidare una Trust Chain nel tempo, anche se la Federation Trust Anchor ha cambiato le proprie chiavi crittografiche per la firma digitale, il Federation Historical Keys endpoint rende sempre disponibili le chiavi non più utilizzate per le verifiche di firma storiche.
Questa proprietà supporta la non-repudiability delle attestazioni a lunga durata.

Quando la Federation Trust Anchor ruota le proprie chiavi, le nuove chiavi sono distribuite con lo stesso meccanismo out-of-band utilizzato per la distribuzione iniziale.
Le Entità che effettuano il pin delle chiavi della Federation Trust Anchor DEVONO aggiornare di conseguenza il materiale pinned.

Trust Chain Validation
^^^^^^^^^^^^^^^^^^^^^^^^

La Trust Chain Validation è una procedura tecnica utilizzata dai processi di trust evaluation definiti in questa sezione per scopi diversi.
A seconda che un'entità stia valutando una federation statement oppure che un artifact trasporti la certificate chain X.509 utilizzata per la sua firma, si applicano due procedure distinte di Trust Chain Validation.

Federation Trust Chain
"""""""""""""""""""""""""

La Trust Chain è una sequenza di statement verificati che convalida la conformità di un'Entità alla federazione.
Ha una data di scadenza, oltre la quale DEVE essere rinnovata per ottenere metadata aggiornati e freschi.
La data di scadenza della Trust Chain è determinata dal timestamp di scadenza più anticipato tra tutti gli statement.
Nessuna Entità può imporre che la data di scadenza della Trust Chain sia superiore a quella configurata dalla Federation Trust Anchor.

Questa procedura verifica la Trust Chain.
La derivazione dei metadata finali del subject, ottenuta applicando le metadata policies trasportate dagli statement della Trust Chain, è definita in :ref:`trust-evaluation:Metadata Retrieval and Validation`.
Secondo `OID-FED`_, la verifica della catena e la derivazione dei metadata finali è indicata come **resolution of a Trust Chain**.

La Trust Chain è costruita tramite il processo **Federation Entity Discovery** definito in `OID-FED`_:

- Il Trust Evaluator recupera l'Entity Configuration del subject.
- Segue gli ``authority_hints`` per raccogliere le Subordinate Statements emesse dalle entità superiori.
- Continua fino a raggiungere la Federation Trust Anchor.

La Trust Chain PUÒ essere mantenuta valida anche con il **fast renewal method** definito in `OID-FED`_ Section 3.1.3, che evita un discovery process completo recuperando le Subordinate Statements direttamente tramite il claim ``source_endpoint``.

La Trust Chain PUÒ essere fornita staticamente dal subject all'interno di un artifact firmato, utilizzando il parametro header JOSE ``trust_chain`` definito in `OID-FED`_ Section 4.3.
All'interno di IT-Wallet l'header ``trust_chain`` è trasportato nel Request Object del presentation flow (vedi :ref:`remote-flow:Request Object`) e negli artifact firmati dell'issuance flow (`OPENID4VCI`_ Appendix F.1 e Section 12.2.3).
Una Trust Chain fornita staticamente richiede di essere rinnovata solo quando è disponibile una connessione internet, mentre DEVE essere rinnovata quando risulta scaduta.

La revoca di un'Entità avviene con l'indisponibilità della Subordinate Statement relativa ad essa.
Se la Federation Trust Anchor o il suo Intermediate non pubblica una Subordinate Statement valida, oppure se ne pubblica una scaduta o non valida, il subject della Subordinate Statement DEVE essere inteso come non valido o revocato.
Per il Trust Evaluator, questo controllo in tempo reale dello stato di revoca è possibile solo online, recuperando la Subordinate Statement al momento della verifica.

Le Trust Chain possono essere verificate anche offline, utilizzando una delle Federation Trust Anchor public keys.
In questo caso il controllo di revoca in tempo reale non è disponibile, e ci si affida alla freschezza della Trust Chain.

La validità massima di una Trust Chain può essere imposta dalla Federation Trust Anchor, che la definisce tramite la scadenza dei propri statement, come descritto sopra.
Indipendentemente da tale validità, ai fini dello stato di revoca delle Entità una Trust Chain costruita più di 24 ore prima del momento della verifica NON DOVREBBE essere considerata valida.
Quando lo stato di revoca di un'Entità deve essere considerato affidabile e un controllo online in tempo reale non è disponibile, una Trust Chain più vecchia di 24 ore DOVREBBE essere rinnovata prima che l'interazione possa proseguire.
Questo limite di 24 ore si applica all'età della Trust Chain, calcolata dalla sua costruzione, ed è indipendente dalla sua data di scadenza.

**Input**

- Il Federation Entity Identifier del subject, oppure una Trust Chain fornita staticamente.
- Le Federation Trust Anchor Federation Public Keys convalidate (vedi :ref:`trust-evaluation:Federation Trust Anchor Distribution`).

**Outcome**

- Una Trust Chain convalidata, cioè l'insieme ordinato di statement verificati, con la relativa data di scadenza.

**Process**

I passi seguenti verificano una Trust Chain secondo `OID-FED`_, con il riferimento alla parte pertinente della specifica per ciascun passo:

1. Ottenere l'Entity Configuration del subject, oppure prendere il primo elemento della Trust Chain fornita staticamente.
2. Raccogliere le Subordinate Statements seguendo gli ``authority_hints`` fino alla Federation Trust Anchor, oppure prenderle dalla Trust Chain statica.
   Le Subordinate Statements sono ottenute dal fetch endpoint (`OID-FED`_ Section 8.1).
3. Convalidare ciascuno statement come Entity Statement secondo `OID-FED`_ Section 3.2, cioè verificarne la firma, la coerenza dei claim ``iss`` e ``sub``, e la validità temporale.
   Ciascuna Subordinate Statement è verificata con le Federation Entity Keys del suo emittente, attestate dallo statement superiore.

   - Lo statement emesso dalla Federation Trust Anchor è verificato con le chiavi Federation Trust Anchor convalidate.
   - L'Entity Configuration del subject è verificata con le chiavi attestate nella Subordinate Statement che lo riguarda.

4. Applicare i vincoli trasportati nelle Subordinate Statements lungo la catena, come definito in `OID-FED`_ Section 6.2.
   In particolare, verificare che gli Entity Types dei metadata pubblicati dal subject rientrino negli ``allowed_entity_types``, considerando che l'Entity Type ``federation_entity`` è sempre consentito, e che il numero di Intermediate non ecceda il ``max_path_length`` imposto dai superiori.
5. Calcolare la scadenza della Trust Chain come il valore ``exp`` più anticipato tra gli statement.

Se una verifica fallisce, la Trust Chain DEVE essere considerata non valida e il subject NON DEVE essere considerato affidabile sulla base di essa.

X.509 Certificate Chain Validation
"""""""""""""""""""""""""""""""""""""

Questa variante si applica quando un artifact è fornito insieme alla certificate chain X.509 utilizzata per la firma.
Per gli artifact in formato JOSE la catena è trasportata nel parametro header ``x5c``, come definito in :rfc:`7515` e utilizzato in IT-Wallet nel Request Object del presentation flow (vedi :ref:`remote-flow:Request Object`).
Per le Credenziali in formato mdoc la catena è trasportata nell'unprotected header ``x5chain`` (elemento 33) del Mobile Security Object, come definito in :rfc:`9360` e in :ref:`credential-data-model:Mobile Security Object`.
La catena contiene il Document Signer certificate e qualsiasi certificato intermedio.
NON DEVE contenere il certificato Signing Trust Anchor, che è distribuito come definito in :ref:`trust-evaluation:Signing Trust Anchor Distribution`.

La validazione del certification path è la standard X.509 path validation definita in :rfc:`5280#section-6`, con il revocation status checking definito in :rfc:`5280` e :rfc:`6960`.
Il ciclo di vita del certificato e i meccanismi di revoca, inclusa la CRL, sono definiti in :ref:`infrastructure-trust:Revocation Mechanisms`.
Questa è la stessa validazione del certification path utilizzata nel Trust Framework EUDIW (vedi :ref:`trust-evaluation:X509 Certificate Chain Validation Algorithm`); l'unica differenza è l'origine della trust anchor e l'estrazione aggiuntiva del Federation Entity Identifier.
In questa sezione, per il Trust Framework Nazionale, i dettagli dell'algoritmo non sono ridefiniti.

All'interno del Trust Framework Nazionale si applica quanto segue.

  - La trust anchor della path validation è la Signing Trust Anchor applicabile, ottenuta come definito in :ref:`trust-evaluation:Signing Trust Anchor Distribution`.
  - Il certificato end-entity trasporta l'OpenID Federation Entity Identifier del subject nell'URI ``subjectAltName``.
    Questo è l'elemento che collega la firma X.509 all'identità di federazione del firmatario.
    Pertanto, la validazione estrae questo identificatore affinché il processo chiamante possa verificare che il certificato che ha firmato l'artifact appartenga all'entità OpenID Federation attesa per quell'artifact.
    Il confronto con l'identificatore atteso, ad esempio l'``iss`` della Credenziale, è eseguito dal processo chiamante (vedi :ref:`trust-evaluation:Signing Trust Anchor Validation Procedure`).
    Questa variante produce solo l'identificatore e non stabilisce da sola quale identificatore sia atteso.

.. note::
  L'emissione di questi certificati X.509 e l'operatività della signing PKI sono definite nella procedura di onboarding e sono fuori dallo scope di questa sezione (vedi :ref:`onboarding-system:Onboarding Processes`).

**Input**

- La certificate chain estratta dall'header dell'artifact, cioè il Document Signer certificate e qualsiasi certificato intermedio.
- Il certificato Signing Trust Anchor applicabile, ottenuto come definito in :ref:`trust-evaluation:Signing Trust Anchor Distribution`.

**Outcome**

- Il certificato end-entity convalidato.
- L'OpenID Federation Entity Identifier del firmatario, estratto dall'URI ``subjectAltName``, da confrontare con l'emittente atteso dal processo chiamante.

**Process**

1. Costruire il certification path dal certificato end-entity al certificato Signing Trust Anchor.
2. Eseguire la path validation definita in :rfc:`5280#section-6`, utilizzando la Signing Trust Anchor come input trust anchor dell'algoritmo.
3. Verificare lo stato di revoca dei certificati nel percorso, secondo :rfc:`5280` e :rfc:`6960`.
4. Estrarre l'OpenID Federation Entity Identifier dall'URI ``subjectAltName`` del certificato end-entity, e restituirlo al processo chiamante per il confronto con l'emittente atteso.

Se un passo fallisce, la firma dell'artifact NON DEVE essere verificata con la certificate chain presentata.

Signing Trust Anchor Distribution and Validation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Questo processo fornisce e convalida la root of trust per la verifica dell'issuer data authentication di un'attestazione.

La Signing Trust Anchor è la root of trust della PKI X.509 utilizzata per firmare le Digital Credentials il cui Rulebook le ancora al Trust Framework Nazionale.

È distinta dalla Federation Trust Anchor di :ref:`trust-evaluation:Federation Trust Anchor Distribution`, poiché la Federation Trust Anchor è la root delle federation statement, mentre una Signing Trust Anchor è la root di un certification path che convalida la firma di un'attestazione.
La Federation Trust Anchor e una Signing Trust Anchor POSSONO essere operate dalla stessa organizzazione, ma sono relazioni di trust diverse, con cicli di vita e canali di revoca diversi.

PUÒ esserci più di una Signing Trust Anchor.
Ciascun Credential Issuer che firma Credenziali in questo framework utilizza una Signing Trust Anchor come root dei propri Document Signer certificates.
Credential Issuer diversi POSSONO basarsi su Signing Trust Anchor diverse.

Signing Trust Anchor Distribution
"""""""""""""""""""""""""""""""""

Le Signing Trust Anchors sono distribuite tramite la Federation Trust Anchor Entity Configuration.
Ciascun certificato Signing Trust Anchor è fornito nel parametro ``x5c`` di una JWK dedicata, distinta dalle Federation Entity Keys utilizzate per firmare le federation statement.
Questo meccanismo di distribuzione è un'implementazione specifica IT-Wallet e non è definito da `OID-FED`_.

Le Entità POSSONO effettuare il pin di una Signing Trust Anchor nella propria configurazione locale.
Una Signing Trust Anchor pinned PUÒ essere utilizzata solo finché è valida e DEVE essere aggiornata quando la Signing Trust Anchor viene ruotata.

Il risultato di questa distribuzione è, per ciascun Trust Evaluator, l'insieme di certificati Signing Trust Anchor convalidati, ciascuno associato al Federation Entity Identifier dei Credential Issuer che vi fanno affidamento.
Questo insieme è il materiale trust anchor consumato dalla procedura di validazione di seguito.

.. note::
  L'emissione dei Document Signer certificates e l'operatività della signing PKI sono definite nella procedura di onboarding e non rientrano nello scope di questa sezione (vedi :ref:`onboarding-system:Onboarding Processes`).

Signing Trust Anchor Validation Procedure
"""""""""""""""""""""""""""""""""""""""""

La procedura dipende dal formato dell'attestazione.

Per le attestazioni in formato JOSE, come le Digital Credentials in formato SD-JWT VC e la Wallet Instance Attestation, l'emittente è identificato dal claim ``iss`` e la chiave di verifica della firma è referenziata dal parametro header ``kid``.
La chiave DEVE essere risolta all'interno dei metadata finali dell'emittente, ottenuti tramite la Federation Trust Chain.
L'artifact PUÒ trasportare l'header JOSE ``trust_chain`` per consentire la validazione senza un nuovo discovery process.

Per le Credenziali in formato mdoc il Mobile Security Object trasporta il Document Signer certificate nell'header ``x5chain``.
La firma è verificata con quel certificato.
La Signing Trust Anchor dell'emittente è convalidata estraendo l'OpenID Federation Entity Identifier dall'URI ``subjectAltName`` e convalidando il certification path rispetto alla Signing Trust Anchor applicabile ottenuta come definito in :ref:`trust-evaluation:Signing Trust Anchor Distribution`.

**Input**

- L'attestazione firmata.
- La configurazione Federation Trust Anchor convalidata e la Signing Trust Anchor applicabile.

**Outcome**

- La trust anchor convalidata e la chiave o il certificato di firma per l'attestazione.
- La conferma che la chiave di firma appartiene all'emittente dell'attestazione.

**Process**

1. Per gli artifact JOSE, derivare i metadata finali dell'emittente dalla Federation Trust Chain (vedi :ref:`trust-evaluation:Federation Trust Chain` e :ref:`trust-evaluation:Metadata Retrieval and Validation`) e selezionare la chiave referenziata dall'header ``kid``.
2. Per gli artifact mdoc, convalidare ``x5chain`` come definito in :ref:`trust-evaluation:X.509 Certificate Chain Validation` e verificare che l'OpenID Federation Entity Identifier nell'URI ``subjectAltName`` corrisponda all'emittente atteso.
3. Verificare la firma dell'attestazione con la chiave o il certificato selezionato.

.. note::
  Quando necessario, il Federation Historical Keys endpoint e le CRL pubblicate DEVONO essere utilizzati per assicurare che l'attestazione fosse valida al momento dell'emissione o della presentazione (vedi :ref:`trust-evaluation:Federation Trust Anchor Key Rotation and Historical Verification` per maggiori dettagli).

Il ciclo di vita dei certificati di firma DEVE restare allineato con la federation configuration set delle chiavi dell'emittente.
Quando una chiave di firma viene ruotata o non è più valida, la corrispondente JWK DEVE essere rimossa dall'Entity Configuration oppure ruotata, e il relativo certificato DEVE essere revocato di conseguenza.
All'interno di IT-Wallet, quando la federation configuration e lo stato del certificato divergono, DEVE prevalere lo stato più restrittivo; pertanto una chiave revocata in una delle due viste DEVE essere considerata revocata.

Authentication Trust Anchor Distribution
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Le Authentication Trust Anchors sono distribuite tramite la Federation Trust Anchor Entity Configuration con lo stesso meccanismo utilizzato per le Signing Trust Anchors.
Ciascun certificato Authentication Trust Anchor è fornito nel parametro ``x5c`` di una JWK dedicata, distinta dalle Federation Entity Keys.

Un'Authentication Trust Anchor è la root della authentication PKI X.509 che emette i Relying Party authentication certificates utilizzati nel Proximity Flow.
Questi certificati seguono lo stesso profilo del Wallet-Relying Party Access Certificate (vedi :ref:`infrastructure-trust:Wallet-Relying Party Access Certificate (WRPAC) Profile`).

.. note::
  L'emissione dei Relying Party authentication certificates e l'operatività della authentication PKI sono definite nella procedura di onboarding e non rientrano nello scope di questa sezione (vedi :ref:`onboarding-system:Onboarding Processes`).

Authentication
^^^^^^^^^^^^^^^^^^^^

Il processo Authentication ha lo scopo di asserire l'identità del Trust Evaluated Party.
Sono definite tre procedure:

- Federation Entity Authentication si applica alle entità che pubblicano un'Entity Configuration, nel Remote Flow.
- Wallet Unit Authentication si applica alla Wallet Unit, che non è una Federation Entity.
- Relying Party Proximity Authentication si applica al Relying Party nel Proximity Flow.

Federation Entity Authentication
"""""""""""""""""""""""""""""""""""

L'identità del Trust Evaluated Party e le sue chiavi sono stabilite tramite la Trust Chain.
Il Trust Evaluated Party si autentica in una data interazione firmando l'artifact di protocollo di quella interazione con una chiave privata la cui parte pubblica è pubblicata nei suoi metadata finali, ottenuti risolvendo la Trust Chain.
Il parametro header ``kid``, come definito in :rfc:`7515`, referenzia una chiave contenuta nei metadata finali del Trust Evaluated Party.
L'insieme completo dei parametri header di ciascun artifact firmato è definito nella sezione di protocollo corrispondente.

**Input**

- L'artifact di protocollo firmato.
- Il Federation Entity Identifier dichiarato dal Trust Evaluated Party.
- Una Trust Chain sul Trust Evaluated Party, fornita staticamente oppure costruita tramite discovery.

**Outcome**

Il Trust Evaluator DEVE produrre ``AUTHENTICATED`` oppure ``NON_AUTHENTICATED``.
Nel secondo caso il Trust Evaluated Party NON DEVE essere considerato autenticato e l'interazione NON DEVE proseguire.
La notifica all'Utente e il divieto di cross scheme retry sono definiti in :ref:`trust-evaluation:Failure Handling`.

**Process**

1. Convalidare la Trust Chain sul Trust Evaluated Party e derivarne i metadata finali (vedi :ref:`trust-evaluation:Federation Trust Chain` e :ref:`trust-evaluation:Metadata Retrieval and Validation`).
2. Verificare che l'entity identifier trasportato dall'artifact, ad esempio il claim ``client_id`` o ``iss``, corrisponda al subject della Trust Chain.
3. Selezionare nei metadata finali la chiave pubblica referenziata dall'header ``kid``.
4. Verificare la firma dell'artifact con la chiave selezionata.

La verifica con esito positivo fornisce sia l'autenticazione del Trust Evaluated Party sia la prova di possesso della sua chiave privata.

Wallet Unit Authentication
"""""""""""""""""""""""""""""""""""

La Wallet Instance Attestation trasporta la chiave pubblica della Wallet Unit utilizzata per convalidare la firma sulla Wallet Instance Attestation.
Il formato e il flusso di emissione sono definiti in :ref:`wallet-instance-attestation-issuance:Emissione della Wallet Instance Attestation`.

La valutazione DEVE seguire il modello definito in OpenID Federation for Wallet Architectures.
La Wallet Unit si autentica con un meccanismo di Client authentication che fornisce la Wallet Instance Attestation emessa dal suo Wallet Provider, insieme alla prova di possesso della chiave attestata.
Nel issuance flow ciò è realizzato con l'OAuth 2.0 Attestation-Based Client Authentication, cioè i parametri ``OAuth-Client-Attestation`` e ``OAuth-Client-Attestation-PoP`` (`OAUTH-ATTESTATION-CLIENT-AUTH`_), come descritto in `OPENID4VCI`_.
Per stabilire il trust nella Wallet Unit, il Trust Evaluator DEVE:

- Stabilire il trust nel Wallet Provider che ha emesso la Wallet Instance Attestation.
- Convalidare l'attestazione con le chiavi del Wallet Provider ottenute tramite la Federation Trust Chain.

**Input**

- La Wallet Instance Attestation presentata dalla Wallet Unit.
- La prova di possesso della chiave attestata nella Wallet Instance Attestation.
- Una Trust Chain sul Wallet Provider.

**Outcome**

Il Trust Evaluator DEVE produrre ``AUTHENTICATED`` oppure ``NON_AUTHENTICATED`` per la Wallet Unit.

**Process**

1. Convalidare la Trust Chain sul Wallet Provider che ha emesso la Wallet Instance Attestation e derivarne i metadata finali (vedi :ref:`trust-evaluation:Federation Trust Chain` e :ref:`trust-evaluation:Metadata Retrieval and Validation`).
2. Verificare la firma della Wallet Instance Attestation con una delle chiavi del Wallet Provider pubblicate nei metadata finali.
3. Verificare la validità temporale e lo stato di revoca della Wallet Instance Attestation.
4. Verificare la prova di possesso della chiave attestata, secondo il protocollo in uso.

Relying Party Proximity Authentication
"""""""""""""""""""""""""""""""""""""""

Nel Proximity Flow il Relying Party è autenticato tramite l'mdoc reader authentication definita in [`ISO18013-5`_].
Il Relying Party firma il session transcript con la chiave privata del suo authentication certificate e fornisce la certificate chain nell'header ``x5chain`` del ``ReaderAuth``.
Il certification path termina in un'Authentication Trust Anchor distribuita come definito in :ref:`trust-evaluation:Authentication Trust Anchor Distribution`.

**Input**

- Il ``ReaderAuth`` firmato dal Relying Party, con la authentication certificate chain nell'header ``x5chain``.
- L'Authentication Trust Anchor applicabile.

**Outcome**

Il Trust Evaluator DEVE produrre ``AUTHENTICATED`` oppure ``NON_AUTHENTICATED``.
Nel secondo caso il Relying Party NON DEVE essere considerato autenticato e l'interazione NON DEVE proseguire.

**Process**

1. Estrarre la certificate chain dall'header ``x5chain`` del ``ReaderAuth``.
2. Convalidare il certification path rispetto all'Authentication Trust Anchor applicabile come definito in :ref:`trust-evaluation:X.509 Certificate Chain Validation`.
3. Verificare la firma del ``ReaderAuth`` sul session transcript con l'authentication certificate convalidato.

La verifica con esito positivo fornisce sia l'autenticazione del Relying Party sia la prova di possesso della chiave privata del suo authentication certificate.

Authorization
^^^^^^^^^^^^^^^^^^

I dati di autorizzazione di un'entità sono forniti dalla registration Trust Mark emessa dal Registrar tramite la Federation Authority.
La registration Trust Mark è funzionalmente analoga al Wallet-Relying Party Registration Certificate del Trust Framework EUDIW, e riutilizza gli stessi nomi di campo per i dati di autorizzazione.
Attesta la registrazione dell'entità e trasporta i suoi ``entitlements`` e, ove applicabile, ``provides_attestations`` oppure ``credentials`` che è autorizzata a emettere o a richiedere.
La sua struttura è definita in :ref:`infrastructure-trust:Trust Mark registration-entity` e lo schema degli identificatori in :ref:`infrastructure-trust:Trust Mark Types and Schema`.

Il processo Authorization è composto dalle seguenti procedure:

1. Trust Mark Validation, che stabilisce la validità della registration Trust Mark.
   Si applica a tutte le Entità registrate.
2. Entitlement Check, che verifica che il ruolo e, in emissione, i tipi di Credenziale del Trust Evaluated Party siano autorizzati.
   Si applica a tutti i Wallet-Relying Party, cioè Credential Issuer e Relying Party.
3. Overasking Check, che verifica in presentazione che un Relying Party richieda solo le Digital Credentials e gli attributi che è autorizzato a richiedere.
   Si applica ai Relying Party.

L'autorizzazione di ruolo comune a entrambe le fasi è eseguita dall'Entitlement Check; i controlli specifici di fase sono il controllo del tipo di Credenziale in emissione, all'interno dell'Entitlement Check, e l'Overasking Check a livello di attributo in presentazione.

Il Trust Evaluator DEVE eseguire il processo Authorization solo dopo che il Trust Evaluated Party è stato autenticato con successo.

Trust Mark Validation
"""""""""""""""""""""""

**Input**

- La Trust Mark *registration-entity*, ottenuta nel Remote Flow dal claim ``trust_marks`` dell'Entity Configuration oppure dal Federation Trust Mark endpoint (`OID-FED`_ Section 8.6), oppure fornita by value nel ``requestInfo`` dell'ISO ``DeviceRequest`` nel Proximity Flow, tramite il membro ``euWrprc`` come definito nel Trust Framework EUDIW.
- La configurazione Federation Trust Anchor convalidata.

**Outcome**

Il Trust Evaluator DEVE produrre ``TRUST_MARK_VALID`` oppure ``TRUST_MARK_INVALID``.
Un esito ``TRUST_MARK_INVALID`` sulla registration Trust Mark significa che l'entità non è autorizzata a operare.
In questo caso il Trust Evaluator DEVE trattare l'entità come non autorizzata e NON DEVE proseguire con l'Entitlement Check.

**Process**

1. Verificare che l'emittente della Trust Mark sia autorizzato per quel ``trust_mark_type``, secondo il claim ``trust_mark_issuers`` della Federation Trust Anchor Entity Configuration.
   La registration Trust Mark, cioè una Trust Mark il cui ``trust_mark_type`` ha lo scopo ``registration-entity``, è soggetta a due controlli aggiuntivi.
   La Trust Mark Validation verifica che il ``trust_mark_type`` corrisponda all'identificatore di registrazione atteso per il ruolo del subject, e che l'emittente sia la Federation Trust Anchor, poiché la registration Trust Mark DEVE essere emessa solo dalla Federation Trust Anchor (vedi :ref:`infrastructure-trust:Trust Mark Types and Schema`).
2. Verificare la firma della Trust Mark con le Federation Entity Keys del suo emittente, ottenute tramite la Trust Chain quando l'emittente non è la Federation Trust Anchor.
3. Verificare la validità temporale della Trust Mark tramite i claim ``iat`` e ``exp``.
4. Quando online, verificare lo stato della Trust Mark tramite il Federation Trust Mark Status endpoint (`OID-FED`_ Section 8.4).

Entitlement Check
"""""""""""""""""""""

Gli entitlements definiscono ciò che l'entità è autorizzata a fare, come i tipi di Credenziale che può emettere o gli attributi che può richiedere.
All'interno di IT-Wallet questi dati di autorizzazione sono trasportati nella registration Trust Mark, nei claim ``entitlements``, ``provides_attestations`` e ``credentials`` definiti in :ref:`infrastructure-trust:Trust Mark Types and Schema`, e NON DEVONO essere derivati dai soli metadata.

**Input**

- Le Trust Mark convalidate del Trust Evaluated Party.
- Il ruolo del Trust Evaluated Party e l'azione attesa nell'interazione corrente.
  In emissione, il tipo di Credential Issuer e i tipi di Credenziale che dichiara di emettere.
  In presentazione, le Digital Credentials e gli attributi richiesti dal Relying Party.

**Outcome**

Il Trust Evaluator DEVE produrre ``ENTITLEMENT_VALID`` oppure ``WRONG_ENTITLEMENT``.

**Process**

1. Estrarre gli ``entitlements`` dalle Trust Mark convalidate e verificare che corrispondano al ruolo atteso nell'interazione corrente, ad esempio che un'entità che agisce come Credential Issuer possieda un issuing entitlement di `ETSI TS 119 475`_ Annex A.2.
2. Durante l'emissione, verificare che il tipo di Credenziale offerto sia presente in ``provides_attestations`` della Trust Mark, confrontando ``format`` e ``meta`` della Credenziale offerta con le voci autorizzate.
3. Durante la presentazione, il controllo a livello di attributo rispetto a ``credentials`` della Trust Mark è eseguito dall'Overasking Check di seguito.

Overasking Check
"""""""""""""""""

**Input**

- La presentation request.
- I ``credentials`` trasportati nella Trust Mark convalidata, cioè le Credential query che il Relying Party è autorizzato a richiedere.

**Outcome**

La Wallet Unit DEVE produrre ``VERIFICATION_PASSED`` oppure ``OVERASKING_DETECTED``, identificando gli attributi o le Digital Credentials non registrati.
In caso di ``OVERASKING_DETECTED`` la Wallet Unit NON DEVE divulgare gli attributi non autorizzati e DEVE informare l'Utente dell'overasking rilevato.

**Process**

1. Estrarre le Digital Credentials e gli attributi richiesti dalla richiesta, dalla DCQL query definita in `OpenID4VP`_ nel remote flow, oppure dai namespace richiesti nel proximity flow.
2. Per ciascuna Credenziale richiesta, selezionare in ``credentials`` della Trust Mark la voce autorizzata con lo stesso ``format`` e ``meta``, ad esempio gli stessi ``vct_values`` o ``doctype_value``.
3. Verificare che ogni attributo richiesto sia presente nei percorsi ``claim`` della voce autorizzata selezionata.
   Se la richiesta contiene una Credenziale o un attributo senza una voce autorizzata corrispondente, l'output è ``OVERASKING_DETECTED``.
4. Il confronto DEVE essere esatto e case sensitive.

User Transparency
"""""""""""""""""

Oltre ai controlli automatizzati sopra, la registration Trust Mark fornisce claim che non sono valutati come regola decisionale ma sono presentati all'Utente per trasparenza, per supportare la decisione di proseguire con l'interazione prima che venga divulgato qualsiasi attributo.
Prima della disclosure, la Wallet Unit DEVE informare l'Utente dell'identità del Relying Party e delle Digital Credentials e degli attributi richiesti, e presenta i claim di trasparenza aggiuntivi della Trust Mark per supportare una decisione informata.
Ciò è coerente con l'approvazione dell'Utente che conclude la presentazione, come definito in :ref:`trust-evaluation:Authorization Decision and Override Rules`.

I claim di trasparenza trasportati nella Trust Mark sono i seguenti:

- ``organization_name``, la ragione sociale dell'entità;
- ``srv_description``, la descrizione del servizio erogato dall'entità;
- ``purpose``, le finalità del trattamento dei dati, per un Relying Party che richiede Credenziali;
- ``privacy_policy``, l'URL della privacy policy, per un Relying Party che richiede Credenziali;
- ``supervisory_authority``, l'Autorità Garante alla quale l'Utente può segnalare anomalie;
- ``public_body``, se l'entità è un ente del settore pubblico;
- ``support_uri``, il contatto per richieste relative all'entità, come cancellazione o portabilità dei dati.

Le loro definizioni sono fornite in :ref:`infrastructure-trust:Trust Mark Types and Schema`.

Quando il Relying Party opera tramite un Relying Party Intermediary, la Wallet Unit DEVE informare l'Utente che il Relying Party opera tramite quell'Intermediary, mostrando l'identità di entrambi.
Nel Trust Framework Nazionale l'Intermediary è il Federation Intermediate nella Trust Chain del Relying Party, registrato con la Trust Mark ``intermediate`` (vedi :ref:`infrastructure-trust:Trust Mark Types and Schema`), ed è quindi identificabile dalla Trust Chain convalidata senza artifact aggiuntivi.

Metadata Retrieval and Validation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

I metadata di una Federation Entity DEVONO essere consumati solo nella loro forma finale, cioè i metadata risultanti dall'applicazione delle metadata policies ai metadata pubblicati nell'Entity Configuration, lungo la Trust Chain convalidata (vedi :ref:`trust-evaluation:Federation Trust Chain`).
I metadata pubblicati nell'Entity Configuration NON DEVONO essere utilizzati senza questa elaborazione.

I tipi di metadata e i relativi parametri sono definiti in :ref:`infrastructure-trust:Entity Type Identifiers and Metadata` e nelle specifiche di protocollo ivi referenziate.

La configurazione della Wallet Unit è fornita dal Wallet Provider all'interno dei suoi metadata come definito in :ref:`wallet-solution-metadata:Metadati della Soluzione Wallet`.

**Input**

- Una Trust Chain convalidata sul subject (vedi :ref:`trust-evaluation:Federation Trust Chain`).

**Outcome**

- I metadata finali del subject, per ciascun metadata type rilevante per l'interazione.

**Process**

1. Applicare la ``metadata_policy`` degli statement superiori ai metadata pubblicati nell'Entity Configuration del subject, lungo la Trust Chain, secondo `OID-FED`_ Section 6.1, ottenendo i metadata finali.
2. Selezionare il metadata type corrispondente al ruolo del subject nell'interazione.
3. Verificare la presenza dei parametri REQUIRED per quel metadata type.
4. Utilizzare endpoint, chiavi e algoritmi solo dai metadata finali.

Quando i metadata sono ottenuti tramite una Trust Chain fornita staticamente, DEVONO essere aggiornati quando la Trust Chain scade, come definito in :ref:`trust-evaluation:Federation Trust Chain`.

.. note::
  All'interno di IT-Wallet la ``metadata_policy`` copre solo i parametri di configurazione tecnica, come endpoint, chiavi crittografiche e algoritmi supportati.
  Entitlements e policy di autorizzazione NON DEVONO essere espressi tramite metadata policies; sono trasportati dalle Trust Mark, come definito in :ref:`trust-evaluation:Authorization`.

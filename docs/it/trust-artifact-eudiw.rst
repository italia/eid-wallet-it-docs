.. include:: ../common/common_definitions.rst
.. Incluso tramite infrastructure-trust.rst al livello di titolo '-' (livello 1).

.. role:: raw-html(raw)
  :format: html

EUDIW Trust Artifacts
---------------------

Questa sezione definisce i trust artifact richiesti e i loro ruoli concettuali nell'ecosistema EUDIW secondo `EIDAS-ARF`_, inclusi:

- :ref:`infrastructure-trust:Register of WRPs`;
- :ref:`infrastructure-trust:Wallet-Relying Party Access Certificate (WRPAC) Profile`;
- :ref:`infrastructure-trust:Registrar Sign/Seal Certificate Profile`;
- :ref:`infrastructure-trust:Wallet-Relying Party Registration Certificate (WRPRC) Profile`;
- :ref:`infrastructure-trust:Trusted List, Lists of Trusted Lists, and Lists of Trusted Entities`;
- :ref:`infrastructure-trust:Embedded Disclosure Policy (EDP)`.

Il modello dati di questi Trust Artifact profila le seguenti specifiche esterne.

- `ETSI TS 119 602`_, che definisce il modello dati delle List of Trusted Entities e i profili delle list EUDIW.
- `ETSI TS 119 411-8`_, che definisce il Wallet-Relying Party Access Certificate.
- `ETSI TS 119 475`_, che definisce il Wallet-Relying Party Registration Certificate insieme alle sue entitlement.
- `ETSI EN 319 412-1`_, che definisce gli attributi del subject dei certificati.
- `ETSI TS 119 182-1`_, che definisce il formato JAdES della firma di una List of Trusted Entities.
- `ETSI EN 319 132-1`_, che definisce il formato XAdES della firma di Trusted List e List of Trusted List.

Register of WRPs
^^^^^^^^^^^^^^^^

Il Register of WRPs nazionale è il sistema accessibile pubblicamente (dataset + API) che fornisce dichiarazioni di registrazione firmate/sigillate relative alle WRP, ai loro **Services**, e alle loro autorizzazioni/usi dichiarati.
Questa sezione documenta un profilo allineato a `EUDI-TS 5`_ versione 1.5 (2026-08-20) che soddisfa l'Allegato II di `CIR2025/848`_ come modificato da [`CIR2026/1730`_].

Una Wallet-Relying Party che opera nel Trust Framework EUDIW DEVE registrare uno o più **Relying Party Services** nell'array ``services`` dell'oggetto ``WalletRelyingParty`` (`EUDI-TS 5`_, ``WalletRelyingPartyService``).
Ciascun Service ha un ``serviceTradeName`` idoneo a essere presentato all'Utente ([`EIDAS-ARF`_] Reg_10a, Reg_34).
``serviceIdentifier`` è univoco all'interno dell'entità quando registrato. DEVE essere registrato se il Service si affida a un Intermediary (`EUDI-TS 5`_ v1.5) e DEVE essere registrato quando un WRPAC è emesso per quel Service ([`EIDAS-ARF`_] Reg_33, RPRC_07a).
Usi previsti, entitlement, attestation fornite e relazioni di intermediario sono vincolati a un Service, non alla root dell'entità ([`EIDAS-ARF`_] Reg_10d).
Un Intermediary Service puro NON DEVE registrare un'entitlement (`EUDI-TS 5`_ v1.5). Un Intermediary Service DEVE elencare gli identificatori di Service che serve in ``servedWRPServices`` ([`CIR2026/1730`_], Allegato I).

Register Dataset
""""""""""""""""

Il formato dati per le informazioni disponibili attraverso l'API aperta fornita dal Register of WRPs nazionale DEVE essere conforme agli schemi dati descritti nelle Tabelle 1-11 dell'Allegato VI di [`CIR2025/848`_] come modificato da [`CIR2026/1730`_], codificati come JSON Schema ``WalletRelyingParty`` di `EUDI-TS 5`_ versione 1.5.
Di seguito alcuni esempi non normativi di oggetti ``WalletRelyingParty`` memorizzati nel Register.

Una banca registrata come Relying Party che richiede PID per procedure know-your-customer, con un Relying Party Service.

.. literalinclude:: ../../examples/register-wrp-rp.json
  :language: JSON

Una banca registrata sia come Relying Party che richiede PID sia come QEAA Provider (che emette attestation di conto bancario al Wallet).
Registra due Service: un Service con ``intendedUses`` e un Service con ``providesAttestations``.

.. literalinclude:: ../../examples/register-wrp-rp-ap.json
  :language: JSON

Un'entità registrata come Intermediary designato che agisce per conto di WRP durante le interazioni con il Wallet.
Ciascun suo elemento ``services[]`` ha ``isIntermediary: true``, non dichiara ``intendedUses`` o entitlement, e elenca i Service serviti in ``servedWRPServices``.

.. literalinclude:: ../../examples/register-wrp-rp-intermediary.json
  :language: JSON


Register Open APIs
""""""""""""""""""

I metodi di lettura API comuni (GET) DEVONO essere aperti all'accesso pubblico (nessuna autenticazione preventiva), restituire dichiarazioni firmate JWS,
e fornire metodi per la ricerca e l'interrogazione di insiemi di dati completi di WRP registrate corrispondenti ai parametri di query forniti.

- **GET /wrp**: Ottenere un elenco di WRP con filtraggio e paginazione opzionali, come definito nella Sezione 3.2 di `EUDI-TS 5`_ versione 1.5.
  I parametri di filtro sono ``identifier``, ``legalname``, ``tradename``, ``serviceidentifier``, ``policy``, ``entitlement``, ``providedattestation``, ``usesintermediary``, ``isintermediary``, ``intendeduseidentifier``, ``claimpath``, ``credentialmeta`` e ``credentialformat``.
  Una risposta di successo (``200``) DEVE essere un body di risposta firmato JWS.
  Il payload decodificato DEVE contenere un array di oggetti ``WalletRelyingParty`` corrispondenti alla query e, ove rilevante, accompagnati da informazioni di history WRPAC nella statement/profile usata dallo Stato membro.
  Quando la query usa ``serviceidentifier``, la risposta DEVE includere solo il ``WalletRelyingPartyService`` corrispondente nell'array ``services`` di ciascun ``WalletRelyingParty`` corrispondente.
  L'elenco di tutte le WRP registrate è restituito quando non sono forniti parametri di query.
- **GET /wrp/{identifier}**: Recuperare l'oggetto ``WalletRelyingParty`` corrispondente all'identificatore dato.
  Una risposta di successo (``200``) DEVE essere un oggetto firmato JWS.
- **GET /wrp/{identifier}/services/{serviceidentifier}**: Recuperare l'oggetto ``WalletRelyingParty`` padre con l'array ``services`` ridotto al Service corrispondente.
  Una risposta di successo (``200``) DEVE essere un oggetto firmato JWS.
- **GET /wrp/check-intended-use**: Un endpoint dedicato di controllo dell'uso previsto per effettuare query ristrette relative all'uso previsto dal Register.
  Una risposta di successo (``200``) DEVE fornire una risposta booleana ``true`` o ``false`` firmata JWS, determinata dai parametri interrogati nelle informazioni di Intended use del Registrar.
  Se la richiesta è non valida o incompleta l'endpoint DEVE rispondere con codice di errore ``400``. Se la WRP data non è trovata, DEVE rispondere con codice di errore ``404``.

.. note::
    La vista API pubblicata esclude solo ``postalAddress`` ([`CIR2025/848`_] come modificato da [`CIR2026/1730`_], Allegato I, punto 4).
    Tutti gli altri campi, inclusi i claim di credenziale dell'uso previsto, sono pubblicati come registrati.
    Le Register Open APIs restano per pubblicazione e trasparenza ([`EIDAS-ARF`_] Reg_03, Reg_06).
    La Wallet Unit NON DEVE usarle come sostituto di un Wallet-Relying Party Registration Certificate mancante o non valido durante la Presentazione di Credenziali o l'Emissione di Credenziali, come specificato in :ref:`trust-evaluation:EUDIW Authorization`.

Il file YAML della specifica OpenAPI descritta nella Sezione 3 di `EUDI-TS 5`_ versione 1.5 è disponibile come `EUDI-TS 5 OpenAPI`_.
Lo JSON Schema dell'oggetto ``WalletRelyingParty``, incluso l'array ``services`` di ``WalletRelyingPartyService``, è disponibile come `EUDI-TS 5 JSON Schema`_.
Il profilo di lettura nazionale di tale API è disponibile :raw-html:`<a href="OAS3-Register-API-READ.html" target="_blank">qui</a>`.

Wallet-Relying Party Access Certificate (WRPAC) Profile
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Questa sezione estende il :ref:`infrastructure-trust:X.509 Certificate Profile` generale e specifica un **Certificate Profile** per i **Wallet-Relying Party Access Certificates (WRPACs)**.

Secondo l'Articolo 2 di [`CIR2025/848`_], un WRPAC è un certificato per sigilli o firme elettronici che autentica e valida la WRP quando interagisce con l'EUDI Wallet.
Per maggiori dettagli sul processo di autenticazione, vedi :ref:`trust-evaluation:EUDIW Authentication`.

La sospensione o la cancellazione dei servizi della WRP comporta la revoca di tutti i WRPAC validi da parte dell'autorità emittente rilevante, in modo che la WRP non sia più in grado di interagire con le Wallet Unit.
Per maggiori dettagli sui processi di Trust Management, vedi :ref:`infrastructure-trust:Trust Management and Lifecycle`.

L'Allegato IV di [`CIR2025/848`_] afferma inoltre che i WRPAC sono destinati a effettuare firme o sigilli elettronici e che DEVONO essere conformi almeno ai requisiti della Normalised Certificate Policy (NCP) specificati negli standard ETSI.
Tenendo conto di questi requisiti minimi, sono possibili diversi scenari specificati nelle clausole seguenti: certificati emessi a persone fisiche o giuridiche, a supporto di firme/sigilli avanzati o anche di firme/sigilli qualificati.
I requisiti condizionali sono definiti in base al caso specifico in cui ricadono i WRPAC.

I requisiti specifici per i WRPAC sono specificati in `ETSI TS 119 411-8`_.

La tabella seguente definisce l'insieme completo di estensioni applicabili al profilo di certificato.
Le estensioni non elencate nella tabella NON DEVONO essere presenti.

.. list-table:: Estensioni del Wallet-Relying Party Access Certificate
   :class: longtable
   :header-rows: 1
   :widths: 25 75

   * - **Extension**
     - **Descrizione**

   * - ``authorityKeyIdentifier``
     - OBBLIGATORIO. Il valore del campo ``keyIdentifier`` DOVREBBE essere derivato dalla chiave pubblica usando i metodi definiti in :rfc:`5280#section-4.2.1.1`.

   * - ``subjectKeyIdentifier``
     - OPZIONALE. Se presente, il suo valore DOVREBBE essere derivato dalla chiave pubblica del subject usando i metodi definiti in :rfc:`5280#section-4.2.1.2`.

   * - ``keyUsage``
     - OBBLIGATORIO. DEVE contenere uno (e uno solo) dei key-usage settings *Type A*, *Type B*, o *Type F*. *Type A* DOVREBBE essere usato secondo LEG-4.3.1-4 nella Clausola 4.3.1 [`ETSI EN 319 412-3`_]. Per dettagli aggiuntivi, vedi Clausola 4.3.2 [`ETSI EN 319 412-2`_] e Clausola 4.3.1 [`ETSI EN 319 412-3`_].

   * - ``certificatePolicies``
     - OBBLIGATORIO. DEVE includere una struttura ``PolicyInformation`` con ``policyIdentifier`` impostato a uno dei seguenti valori (definiti in `ETSI TS 119 411-8`_):

       * ``0.4.0.194118.1.1`` (``NCP-n-eudiwrp``);
       * ``0.4.0.194118.1.2`` (``NCP-l-eudiwrp``);
       * ``0.4.0.194118.1.3`` (``QCP-n-eudiwrp``);
       * ``0.4.0.194118.1.4`` (``QCP-l-eudiwrp``)

       e ``policyQualifiers`` contenente un ``cpsURI`` che referenzia un URL in cui è situata la CPS del Provider of WRPAC.

   * - ``subjectAltName``
     - OBBLIGATORIO. DEVE includere una struttura ``GeneralName`` con uno dei seguenti parametri definiti per fornire informazioni di contatto valide della WRP:
     
       * ``uniformResourceIdentifier``, per fornire l'URI di un sito web per questioni di helpdesk/supporto;
       * ``otherName`` con ``type-id`` impostato a ``2.5.4.20`` (``id-at-telephoneNumber``), per fornire un numero di telefono per questioni di registrazione/uso della WRP;
       * ``rfc822Name``, per fornire un indirizzo email per questioni di registrazione/uso della WRP.

       Inoltre, DEVE includere un ``uniformResourceIdentifier`` il cui ultimo segmento di path è l'identificatore del Relying Party Service di questo certificato (``services[].serviceIdentifier`` nel Register).
       Tale URI DEVE essere univoco all'interno dell'entità e DEVE essere identico al ``srv_id`` di ogni WRPRC emesso per lo stesso Service della stessa entità ([`EIDAS-ARF`_] Reg_33, RPRC_07a).
       Fino a quando [`ETSI TS 119 411-8`_] non definisce un attributo dedicato per l'identificatore del Service, questo URI ``subjectAltName`` è la codifica IT-Wallet di Reg_33.

       Se il subject è un Intermediary che presenta per conto di una Relying Party intermediata, il certificato DEVE includere inoltre un secondo ``uniformResourceIdentifier`` della forma ``{registryURI}/wrp/{intermediatedRpIdentifier}/services/{intermediatedServiceIdentifier}``, dove ``intermediatedRpIdentifier`` è l'identificatore univoco a livello UE di quella Relying Party ([`EIDAS-ARF`_] Reg_32) e ``intermediatedServiceIdentifier`` è l'identificatore del Relying Party Service intermediato ([`EIDAS-ARF`_] Reg_33).
       Fino a quando [`ETSI TS 119 411-8`_] non definisce un attributo dedicato per questa associazione, tale URI è la codifica IT-Wallet di [`EIDAS-ARF`_] Reg_34a.

   * - ``cRLDistributionPoints``
     - CONDIZIONALE. **OBBLIGATORIO SE:** il certificato non include alcuna access location di un responder OCSP o l'estensione validity assured come definita in `ETSI EN 319 412-1`_.
     
       Se presente, DEVE contenere almeno un riferimento a una CRL pubblicamente disponibile.

   * - ``authorityInfoAccess``
     - OBBLIGATORIO. DEVE includere una struttura ``AccessDescription`` con ``accessMethod`` impostato a ``1.3.6.1.5.5.7.48.2`` (``id-ad-caIssuers``) e ``accessLocation`` che specifica almeno una access location di un certificato CA valido della CA emittente.

       Se l'OCSP è supportato dalla CA emittente, l'estensione DEVE includere una struttura ``AccessDescription`` con ``accessMethod`` impostato a ``1.3.6.1.5.5.7.48.1`` (``id-ad-ocsp``) e ``accessLocation`` che specifica almeno un responder OCSP autorevole a fornire informazioni di status del certificato per il certificato, come descritto in :ref:`infrastructure-trust:Online Certificate Status Protocol (OCSP)`.

   * - ``qcStatements``
     - OPZIONALE. PUÒ contenere strutture `QCStatement` tra quelle definite nella Clausola 4.2 di [ETSI EN 319 412-5].
       In ogni caso, NON DEVE contenere una struttura ``QCStatement`` con ``statementId`` impostato a ``0.4.0.1862.1.7`` (``id-etsi-qcs-QcCClegislation``), indicato come ``esi4-qcStatement-7``.

   * - ``signedCertificateTimestampList``
     - OBBLIGATORIO. Estensione X.509 non critica con object identifier ``1.3.6.1.4.1.11129.2.4.5`` (``id-ct-v2-sctList``) come specificato in :rfc:`9162`.
       DEVE contenere almeno un Signed Certificate Timestamp per questo certificato ([`EIDAS-ARF`_] CT_04).
       Certificate Transparency versione 2.0 si applica solo ai Wallet-Relying Party Access Certificate; non si applica al Wallet-Relying Party Registration Certificate.

.. note::
    **Considerazioni di Dipendenza**: Gli attributi del WRPAC DEVONO essere derivati dalle informazioni detenute nel Register come specificato nella clausola 5.1.2 di `ETSI TS 119 475`_.
    Ciò implica inoltre che per alcuni attributi specifici nel WRPAC lo stesso valore DEVE essere incontrato nel WRPRC corrispondente.

    Un'entità in registrazione DEVE ricevere almeno un WRPAC per ciascun Service registrato ([`EIDAS-ARF`_] Reg_10a).
    Un Intermediary DEVE ricevere un insieme separato di WRPAC per ciascuna Relying Party intermediata, un WRPAC per ciascun Relying Party Service intermediato che serve ([`EIDAS-ARF`_] Reg_34a).
    Il ``subject.organizationName`` (persona giuridica) o gli attributi di nome della persona fisica DEVONO identificare l'entità e DEVONO essere idonei a essere presentati all'Utente ([`EIDAS-ARF`_] Reg_31).
    Il ``subject.organizationIdentifier`` (persona giuridica) o ``subject.serialNumber`` (persona fisica) DEVE essere l'identificatore univoco a livello UE dell'entità ([`EIDAS-ARF`_] Reg_32).
    Il ``subject.commonName`` DEVE essere il ``serviceTradeName`` del Service che questo certificato autentica ([`EIDAS-ARF`_] Reg_34).
    L'identificatore del Service DEVE essere presente in ``subjectAltName`` come specificato sopra ([`EIDAS-ARF`_] Reg_33).
    Se il subject è un Intermediary, ``subjectAltName`` DEVE anche recare l'associazione alla Relying Party intermediata come specificato sopra ([`EIDAS-ARF`_] Reg_34a).

    Il Provider of WRPAC DEVE registrare ogni WRPAC emesso in un log Certificate Transparency secondo :rfc:`9162` ([`EIDAS-ARF`_] CT_01) e DEVE descrivere tale registrazione nella propria Certification Practice Statement, referenziata dal ``cpsURI`` sopra ([`EIDAS-ARF`_] CT_02, Allegato IV, punto 3(j) di [`CIR2025/848`_], `ETSI TS 119 411-8`_ OVR-6.4.5-02).
    Fino a quando un log Certificate Transparency per i certificati di accesso non è designato a livello di Unione, il Provider of WRPAC DEVE operare o usare un log idoneo per i WRPAC in modo che ciascun certificato possa recare almeno un Signed Certificate Timestamp ([`EIDAS-ARF`_] CT_04).
    Quando un log Certificate Transparency per i certificati di accesso è disponibile, il Provider of WRPAC DEVE agire come monitor nell'ecosistema Certificate Transparency e DOVREBBE continuare a monitorare durante l'indisponibilità temporanea del log ([`EIDAS-ARF`_] CT_03).

Di seguito un esempio di WRPAC per persone giuridiche secondo la NCP.

.. literalinclude:: ../../examples/wrpac-ncp.txt
  :language: text

Registrar Sign/Seal Certificate Profile
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Questa sezione estende il :ref:`infrastructure-trust:X.509 Certificate Profile` generale e specifica un **Certificate Profile** per i **Registrar Sign/Seal Certificates**.

La tabella seguente definisce l'insieme completo di estensioni applicabili al profilo di certificato.
Le estensioni non elencate nella tabella NON DEVONO essere presenti.

.. list-table:: Estensioni del Registrar Sign/Seal Certificate
   :class: longtable
   :header-rows: 1
   :widths: 25 75

   * - **Extension**
     - **Descrizione**

   * - ``authorityKeyIdentifier``
     - OBBLIGATORIO. Il valore DOVREBBE essere derivato dalla chiave pubblica usando i metodi definiti in :rfc:`5280#section-4.2.1.1`.

   * - ``subjectKeyIdentifier``
     - OPZIONALE. Se presente, il campo ``keyIdentifier`` DOVREBBE essere derivato dalla chiave pubblica del subject usando i metodi definiti in :rfc:`5280#section-4.2.1.2`.

   * - ``keyUsage``
     - OBBLIGATORIO. DEVE contenere uno (e uno solo) dei key-usage settings *Type A*, *Type B*, o *Type F*. *Type A* DOVREBBE essere usato secondo LEG-4.3.1-4 nella Clausola 4.3.1 [`ETSI EN 319 412-3`_]. Per dettagli aggiuntivi, vedi Clausola 4.3.2 [`ETSI EN 319 412-2`_] e Clausola 4.3.1 [`ETSI EN 319 412-3`_].

   * - ``certificatePolicies``
     - OBBLIGATORIO. DEVE includere una struttura ``PolicyInformation`` rilevante per le pratiche della CA emittente.

   * - ``subjectAltName``
     - OBBLIGATORIO.

   * - ``cRLDistributionPoints``
     - CONDIZIONALE. **OBBLIGATORIO SE:** il certificato non include alcuna access location di un responder OCSP o l'estensione validity assured come definita in `ETSI EN 319 412-1`_.

   * - ``authorityInfoAccess``
     - OBBLIGATORIO. DEVE includere una struttura ``AccessDescription`` con ``accessMethod`` impostato a ``1.3.6.1.5.5.7.48.2`` (``id-ad-caIssuers``) e ``accessLocation`` che specifica almeno una access location di un certificato CA valido della CA emittente.

       Se l'OCSP è supportato dalla CA emittente, l'estensione DEVE includere una struttura ``AccessDescription`` con ``accessMethod`` impostato a ``1.3.6.1.5.5.7.48.1`` (``id-ad-ocsp``) e ``accessLocation`` che specifica almeno un responder OCSP autorevole a fornire informazioni di status del certificato per il certificato, come descritto in :ref:`infrastructure-trust:Online Certificate Status Protocol (OCSP)`.

Di seguito un esempio non normativo di Registrar Sign/Seal Certificate per persone giuridiche (non self-signed).

.. literalinclude:: ../../examples/registrar-sign-seal.txt
  :language: text


Wallet-Relying Party Registration Certificate (WRPRC) Profile
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Questa sezione definisce il Wallet-Relying Party Registration Certificate (WRPRC), come descritto in `EIDAS-ARF`_ e `ETSI TS 119 475`_.
Questo Trust Artifact fornisce informazioni dettagliate sul profilo di Authorization del Credential Issuer e della Relying Party, inclusi:

- attributi di identificazione core (clausola 5.1 `ETSI TS 119 475`_),
- attributi di descrizione del servizio (clausola 5.2.4 `ETSI TS 119 475`_), incluso l'identificatore e il trade name del Relying Party Service ([`EIDAS-ARF`_] RPRC_07a),
- attributi di entitlement (vedi Allegato A.2 `ETSI TS 119 475`_),
- attributi dell'autorità di vigilanza (clausola 5.2.4 `ETSI TS 119 475`_),
- attributi della Relying Party (clausola 5.2.4 `ETSI TS 119 475`_),
- attributi del Credential Issuer (clausola 5.2.4 `ETSI TS 119 475`_),
- attributi dell'Intermediary; cioè, se il Relying Party Service si affida a un Intermediary per richiedere Attestati Elettronici (clausola 5.2.4 `ETSI TS 119 475`_).

Ciascun WRPRC è vincolato a un singolo Relying Party Service.
Il Provider of WRPRC emette i WRPRC automaticamente come definito in :ref:`onboarding-system:Wallet-Relying Party Registration Certificate Issuance`.
Il claim ``name`` DEVE essere uguale al ``serviceTradeName`` di quel Service e, per una presentazione non intermediata, DEVE essere identico al ``subject.commonName`` del WRPAC dello stesso Service della stessa entità ([`EIDAS-ARF`_] Reg_34, RPRC_07a).
Il claim ``srv_id`` DEVE essere uguale al ``serviceIdentifier`` di quel Service e, per una presentazione non intermediata, DEVE essere identico all'identificatore del Service codificato nel ``subjectAltName`` del WRPAC ([`EIDAS-ARF`_] Reg_33, RPRC_07a).
L'oggetto ``intermediary`` del WRPRC DEVE identificare l'Intermediary e l'Intermediary Service ([`EIDAS-ARF`_] RPRC_04).
La Wallet Unit valuta la presentazione intermediata, inclusa l'associazione ``subjectAltName`` del WRPAC di [`EIDAS-ARF`_] Reg_34a, come specificato in :ref:`trust-evaluation:EUDIW Authorization`.
ETSI TS 119 475 v1.2.1 non definisce ancora ``srv_id``; questa specifica lo profila per implementare RPRC_07a fino a quando tale standard non è aggiornato. Il claim è una stringa JSON (JWT) o una text string CBOR (CWT) e DEVE essere identico a ``services[].serviceIdentifier`` nel Register.

Il Wallet-Relying Party Registration Certificate DEVE essere formattato come JSON Web Token (JWT) firmato o come CBOR Web Token (CWT) :rfc:`8392`.
DEVE essere conforme ai requisiti sintattici e semantici specificati nell'Allegato V paragrafo 3 del CIR (UE) 2025/848 e in `ETSI TS 119 475`_.

Il Wallet-Relying Party Registration Certificate DEVE essere firmato con la chiave privata del Provider of Wallet-Relying Party Registration Certificates.
In particolare:

- Il JWT DEVE essere firmato con una JSON Advanced Electronic Signature con il profilo B-B come definito in `ETSI TS 119 182-1`_.
- Il CWT DEVE essere firmato con una Advanced Electronic Signature seguendo la struttura come definita in :rfc:`9052` e :rfc:`9360`.

Di seguito un esempio non normativo di header e payload WRPRC per una Relying Party.

.. literalinclude:: ../../examples/wrprc-jwt-header.json
  :language: json

.. literalinclude:: ../../examples/wrprc-payload-ci.json
  :language: json

Di seguito un esempio non normativo di payload WRPRC per una Relying Party intermediata.

.. literalinclude:: ../../examples/wrprc-payload-rpi.json
  :language: json

.. warning::

  `ETSI TS 119 475`_, Tabella 10 definisce il subfield del nome dell'intermediario come ``sname``.
  L'esempio nell'Allegato C dello stesso standard usa invece ``name``.
  Questa specifica segue la Tabella 10 normativa e usa ``sname``.

  Il claim identificatore del Service ``srv_id`` è profilato da questa specifica per implementare [`EIDAS-ARF`_] RPRC_07a fino a quando `ETSI TS 119 475`_ definisce un membro equivalente.

Trusted List, Lists of Trusted Lists, and Lists of Trusted Entities
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Questa sezione descrive il formato e i contenuti di tre tipi di Trust Artifact, ciascuno dei quali convoglia un elenco di Trust Anchor correnti e storici (contenitori di materiali crittografici e identificatori appartenenti a Entità fidate).

Le Entità dell'ecosistema utilizzano queste list per:

- **Validare l'affidabilità a runtime**: Verificare un Trust Anchor (vedi :ref:`infrastructure-trust:Trust Anchor Certificate Profile`) per autenticare, autorizzare o validare un'entità o un artifact durante le operazioni live.
- **Eseguire la validazione storica**: Validare le informazioni contenute nella list per scopi di audit storico.

I tre tipi distinti di trust list sono:

- Trusted Lists (TLs): Stabilite ai sensi del Capitolo II dell'Allegato I di `CID2015/1505`_, come modificato da `CID2025/2164`_, e specificate in `ETSI TS 119 612`_.
  Ciascuno Stato membro pubblica una TL in formato XML.
  È firmata dallo Stato membro rispettivo con una firma digitale XAdES al livello di conformità baseline B (come definito in `ETSI EN 319 132-1`_).
  Le TL sono pubblicate in un formato machine-readable a endpoint specificati all'interno della LOTL.
  Queste List detengono informazioni correnti e storiche sull'accreditamento dei trust service provider, referenziando:

  - Qualified Trust Service Providers (QTSP), come Qualified Certificates Issuing e meccanismi di revoca, QEAA Provider, servizi di archiviazione elettronica qualificata.
  - Trust Service non qualificati come gli EAA Provider.
  - Altri Trust Service definiti a livello nazionale, come l'archiviazione.

   All'interno di eIDAS, le TL sono mantenute dagli Stati membri, che sono responsabili di tenere traccia dei trust service provider sotto la rispettiva giurisdizione.
   Sono numerate e rinnovate periodicamente, e pubblicate in un sito web per il download non ristretto.
   Per proteggerne l'integrità e assicurarne l'autenticità, sono inoltre firmate con certificati fidati contenuti nella LOTL.

- List of Trusted Lists (LOTL): Stabilita ai sensi del Capitolo II dell'Allegato I di `CID2015/1505`_, come modificato da `CID2025/2164`_, e specificata in `ETSI TS 119 612`_.
  Esiste una sola LOTL, che è pubblicata in formato XML e firmata dalla Commissione europea (CE).
  Utilizza una firma digitale XAdES al livello di conformità baseline B (secondo `ETSI EN 319 132-1`_) e referenzia i certificati fidati di ciascuna National Trusted List.
  Per facilitare la rotazione delle chiavi e gli aggiornamenti continui, la LOTL implementa un pivoting mechanism.
  È pubblicata in un formato machine-readable a un endpoint specificato all'interno della Gazzetta ufficiale dell'Unione europea (`OJEU`_).

  Lo schema XML sia per le Trusted List sia per la List of Trusted Lists, contenente nome e descrizione dei parametri, è disponibile all'indirizzo ``https://forge.etsi.org/rep/esi/x19_612_trusted_lists/-/raw/v2.4.1/19612_xsd.xsd``. Attualmente, la versione machine-readable della LOTL e delle TL nazionali è pubblicata in `EUMS-LOTL`_.

- Lists of Trusted Entities (LoTE): Stabilite ai sensi degli Articoli 4 e 5 di `CIR2024/2980`_ e specificate in `ETSI TS 119 602`_.
  Sono disponibili in formato XML o JSON e sono firmate con una firma digitale AdES al livello di conformità baseline B (secondo `ETSI TS 119 182-1`_).
  Per facilitare gli aggiornamenti continui, la LoTE implementa un pivoting mechanism ed è pubblicata in un formato machine-readable a un endpoint specificato all'interno della `OJEU`_.
  I tipi di LoTE possono essere uno dei seguenti, come definito nell'allegato C.2:

  - PID Provider;
  - Wallet Provider;
  - Provider of Wallet Relying Party Access Certificates;
  - Providers of Wallet Relying Party Registration Certificates;
  - Public sector bodies issuing Electronic Attestations of Attributes;
  - List of Registrars and Registers.

  Il repository seguente fornisce gli schemi JSON e XML normativi richiesti per implementare la List of Trusted Entities (`ETSI-LOTE-SCHEMAS`_).

La tabella seguente fornisce una panoramica completa dell'architettura delle trust list eIDAS, con riferimenti incrociati alla base giuridica, agli standard tecnici di governo, ai formati dati espliciti, ai profili di firma e alle dinamiche di pubblicazione per le Trusted List (TL), la List of Trusted Lists (LOTL) e le varie List of Trusted Entities (LoTE) specifiche per categoria.

.. list-table:: Profili dell'Ecosistema delle Trust List eIDAS
   :class: longtable
   :widths: 14 20 16 16 18 16
   :header-rows: 1

   * - **List Type**
     - **Base giuridica**
     - **Standard di governo e Formato**
     - **Signature Profile**
     - **Scope e Firmatario**
     - **Meccanismo di pubblicazione e aggiornamento**
   * - **Trusted Lists (TL)**
     - `CID2015/1505`_ (Allegato I, Capitolo II), modificato da `CID2025/2164`_.
     - `ETSI TS 119 612`_; formato ``XML``.
     - Firma digitale XAdES, baseline B (`ETSI EN 319 132-1`_).
     - Scope di Stato membro; una list per Stato membro, firmata da tale Stato membro.
     - Endpoint machine-readable specificato all'interno della LOTL.
   * - **List of Trusted Lists (LOTL)**
     - `CID2015/1505`_ (Allegato I, Capitolo II), modificato da `CID2025/2164`_.
     - `ETSI TS 119 612`_; formato ``XML``.
     - Firma digitale XAdES, baseline B (`ETSI EN 319 132-1`_).
     - Scope dell'Unione europea; una singola list globale firmata dalla Commissione europea (CE) che ancora le National Trusted List.
     - Endpoint machine-readable specificato all'interno della `OJEU`_.
       Implementa un pivoting mechanism per gestire gli aggiornamenti continui.
   * - **LoTE: PID Provider Lists**
     - Articoli 4 e 5 di `CIR2024/2980`_.
     - `ETSI TS 119 602`_ Allegato D; formato ``JSON``.
     - Firma digitale AdES, baseline B (`ETSI TS 119 182-1`_).
     - Scope dell'Unione europea; una list per tipo specifico di entità dell'ecosistema.
     - Endpoint machine-readable specificato all'interno della `OJEU`_.
       Implementa un pivoting mechanism per gestire gli aggiornamenti continui.
   * - **LoTE: Wallet Provider (WP) Lists**
     - Articoli 4 e 5 di `CIR2024/2980`_.
     - `ETSI TS 119 602`_ Allegato E; formato ``JSON``.
     - Firma digitale AdES, baseline B (`ETSI TS 119 182-1`_).
     - Scope dell'Unione europea; una list per tipo specifico di entità dell'ecosistema.
     - Endpoint machine-readable specificato all'interno della `OJEU`_.
       Implementa un pivoting mechanism per gestire gli aggiornamenti continui.
   * - **LoTE: Provider of WRPAC Lists**
     - Articoli 4 e 5 di `CIR2024/2980`_.
     - `ETSI TS 119 602`_ Allegato F; formato ``JSON``.
     - Firma digitale AdES, baseline B (`ETSI TS 119 182-1`_).
     - Scope dell'Unione europea; una list per tipo specifico di entità dell'ecosistema (Wallet Relying Party Access Certificate).
     - Endpoint machine-readable specificato all'interno della `OJEU`_.
       Implementa un pivoting mechanism per gestire gli aggiornamenti continui.
   * - **LoTE: Provider of WRPRC Lists**
     - Articoli 4 e 5 di `CIR2024/2980`_.
     - `ETSI TS 119 602`_ Allegato G; formato ``JSON``.
     - Firma digitale AdES, baseline B (`ETSI TS 119 182-1`_).
     - Scope dell'Unione europea; una list per tipo specifico di entità dell'ecosistema (Wallet Relying Party Registration Certificate).
     - Endpoint machine-readable specificato all'interno della `OJEU`_.
       Implementa un pivoting mechanism per gestire gli aggiornamenti continui.
   * - **LoTE: PuB-EAA Provider Lists**
     - Articoli 4 e 5 di `CIR2024/2980`_.
     - `ETSI TS 119 602`_ Allegato H; formato ``JSON`` o ``XML``.
     - Firma digitale AdES, baseline B (`ETSI TS 119 182-1`_).
     - Scope dell'Unione europea; le list notificano i PuB-EAA Provider e i loro Sign/Seal Trust Anchor.
     - Endpoint machine-readable specificato all'interno della `OJEU`_.
       Implementa un pivoting mechanism per gestire gli aggiornamenti continui.
   * - **LoTE: Registrar and Register Provider Lists**
     - Articoli 4 e 5 di `CIR2024/2980`_.
     - `ETSI TS 119 602`_ Allegato I; formato ``JSON``.
     - Firma digitale AdES, baseline B (`ETSI TS 119 182-1`_).
     - Scope dell'Unione europea; una list per tipo specifico di entità dell'ecosistema.
     - Endpoint machine-readable specificato all'interno della `OJEU`_.
       Implementa un pivoting mechanism per gestire gli aggiornamenti continui.

.. note::
  
  Come suggerito in `EIDAS-ARF`_, per efficienza, le implementazioni POSSONO controllare routinariamente i Trust Anchor nelle List of Trusted Entities o nelle Trusted List e memorizzarli localmente. Questo consente, per esempio, alle Relying Party Instance in esecuzione su app mobili di facilitare le presentazioni offline.
  
L'esempio seguente mostra un esempio non normativo di payload di una List of Trusted Entities per PID Provider.

.. literalinclude:: ../../examples/lote-pid.json
  :language: json

Embedded Disclosure Policy (EDP)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Un'Embedded Disclosure Policy (EDP) è definita nell'Articolo 2(9) di [`CIR2024/2979`_] come: *"A set of rules, embedded in an electronic attestation of attributes by its provider, that indicates the conditions that a wallet-relying party has to meet to access the electronic attestation of attributes"*.

Gli Attestation Provider (cioè, tutti i Credential Issuer eccetto il PID Provider) possono opzionalmente esprimere un'EDP che consente di indicare quali Relying Party possono accedere a specifici Attestati Elettronici.
L'Articolo 10 di [`CIR2024/2979`_] stabilisce che i Wallet Provider DEVONO assicurare che le Attestation con EDP comuni (come elencate nell'Allegato III di [`CIR2024/2979`_]) possano essere elaborate dalle loro Wallet Unit.

Le EDP sono applicabili a QEAA, PuB-EAA ed EAA.
NON DEVONO essere applicabili ai PID.

L'EDP è distribuita attraverso i Metadata del Credential Issuer al momento dell'emissione.
L'Attestation Provider DEVE includere l'EDP (se presente) per valore nei Metadata del Credential Issuer, all'interno del parametro ``credential_configurations_supported``, in conformità con `OpenID4VCI`_ o l'estensione di esso specificata in `ETSI TS 119 472-3`_.
Se disponibile, la Wallet Unit DEVE memorizzare l'EDP localmente e associarla alla specifica Attestation per cui è stata recuperata.
La Wallet Unit NON DEVE rivelare l'EDP alla Relying Party attraverso il protocollo di presentazione secondo `ETSI TS 119 472-3`_, Sezione 4.2.5.1.

Le Embedded Disclosure Policy sono usate per:

- Implementare il controllo di accesso settoriale (ad es., solo RP del settore pubblico o solo RP sanitarie).
- Implementare il controllo di accesso specifico per Stato membro (ad es., solo RP registrate all'interno di uno Stato membro specifico).

L'Allegato III di [`CIR2024/2979`_] definisce tre tipi comuni di EDP.
La Wallet Unit li valuta come specificato in :ref:`trust-evaluation:EUDIW Authorization`.

- **No Policy.** Nessuna EDP è presente, oppure l'EDP indica esplicitamente che non si applicano restrizioni (ISS-MDATA-EBD-4.2.5.2-06).

- **Authorized Relying Parties Only.** L'EDP contiene un elenco di coppie di identificatori autorizzati, ciascuna un identificatore univoco a livello UE della Relying Party insieme a un identificatore di Service ([`EIDAS-ARF`_] EDP_02, Reg_32, Reg_33).
  Secondo `ETSI TS 119 472-3`_ (ISS-MDATA-EBD-4.2.5.2-07), tale elenco PUÒ anche recare un subject distinguished name, in forma di stringa LDAP come definito in :rfc:`4514`, oppure un URI di entitlement.

  - Per le persone giuridiche, gli attributi DN rilevanti sono ``commonName``, ``organizationName``, ``organizationIdentifier``, e ``countryName``.
  - Per le persone fisiche: ``commonName``, ``givenName``, ``surname``, ``serialNumber``, e ``countryName``.
    Il tipo di attributo ``organizationIdentifier`` è rappresentato dalla stringa LDAP "ORGID"; il tipo di attributo ``serialNumber`` è rappresentato da "SN" (secondo `ETSI TS 119 472-3`_ NOTE 1 e NOTE 2 a ISS-MDATA-EBD-4.2.5.2-07).

- **Specific Root of Trust.** L'EDP contiene un elenco di certificati root o intermedi fidati usati per firmare i Wallet-Relying Party Registration Certificate ([`EIDAS-ARF`_] EDP_03).
  Solo le RP il cui signing path del WRPRC contiene uno di questi certificati sono autorizzate ad accedere all'Attestation.
  Secondo `ETSI TS 119 472-3`_ (ISS-MDATA-EBD-4.2.5.2-08/09), ciascuna root o intermedio autorizzato è identificato dal suo issuer distinguished name in forma di stringa LDAP come definito in RFC 4514 e dal serial number del certificato dell'issuer.

.. note::

  L'HLR EDP_02 di `EIDAS-ARF`_ richiede coppie di identificatori prese dal WRPRC nella richiesta (``sub`` e ``srv_id``), non dal WRPAC, anche in una presentazione **diretta**.
  `ETSI TS 119 472-3`_ (ISS-MDATA-EBD-4.2.5.2-07) codifica inoltre le parti autorizzate per subject DN o per URI di entitlement.
  Il parametro ``subject_dn`` è quella codifica ETSI; non è un input di valutazione rispetto al WRPAC.
  Il parametro ``entitlement_uri`` è abbinato rispetto alle entitlement detenute nel WRPRC.
  L'Allegato A.3 di `ETSI TS 119 475`_ definisce sub-entitlement per i Service Provider, attualmente per i Payment Service Provider (ad es. ``https://uri.etsi.org/19475/SubEntitlement/psp/psp-ai``).
  Per una presentazione **intermediata** il WRPRC nella richiesta è quello della Relying Party *intermediata* ([`EIDAS-ARF`_] RPRC_19).

Embedded Disclosure Policy Data Model
""""""""""""""""""""""""""""""""""""""

La tabella seguente fornisce una panoramica completa del modello dati dell'Embedded Disclosure Policy, inclusi i nomi dei parametri, i tipi di dati, le descrizioni e le clausole specifiche in `ETSI TS 119 472-3`_ in cui ciascun parametro è definito.

.. warning::
  I nomi dei parametri sono definiti in questa sezione e non si basano su una specifica ETSI normativa. La Sezione 4.2.5.2 di `ETSI TS 119 472-3`_ definisce i requisiti di alto livello per il modello dati, ma lo schema JSON finale sarà pubblicato separatamente da ETSI. La struttura definita qui è un profilo di implementazione basato sui requisiti del modello dati ETSI, e i nomi dei parametri POSSONO cambiare quando lo schema ETSI è pubblicato.

.. list-table:: Parametri dell'Embedded Disclosure Policy
   :class: longtable
   :header-rows: 1
   :widths: 20 60 20

   * - **Parameter**
     - **Descrizione**
     - **Riferimento**

   * - ``policy_uri``
     - OBBLIGATORIO. string (URI).
       Identificatore univoco dell'Embedded Disclosure Policy (EDP).

       L'associazione dell'EDP con una EAA DEVE essere stabilita includendo questo URI univoco.
       L'AP DEVE o includere l'URI insieme all'insieme completo dei dati della policy, oppure fornire solo l'URI se l'insieme dei dati della policy è già stato precaricato nella Wallet Unit.
       L'EDP PUÒ essere accessibile attraverso questo URI.
     - Clausola 4.2.5.2 di [`ETSI TS 119 472-3`_] (ISS-MDATA-EBD-4.2.5.2-01, ISS-MDATA-EBD-4.2.5.2-02, ISS-MDATA-EBD-4.2.5.2-03)

   * - ``policy_type``
     - OBBLIGATORIO. string.
       Classificazione del tipo di policy.
       Valori validi:

       * ``"no_policy"``: Indica che non si applicano restrizioni di policy per la EAA associata.
       * ``"authorized_rp_only"``: L'accesso è ristretto a un elenco esplicito di Relying Party consentite.
       * ``"specific_root_of_trust"``: L'accesso è ristretto alle Relying Party il cui signing path del WRPRC contiene un certificato root o intermedio fidato specificato.
     - Clausola 4.2.5.2 di [`ETSI TS 119 472-3`_] (ISS-MDATA-EBD-4.2.5.2-06, ISS-MDATA-EBD-4.2.5.2-07, ISS-MDATA-EBD-4.2.5.2-08)

   * - ``description``
     - OPZIONALE. string.
       Descrizione dell'applicabilità della policy a una particolare comunità e/o classe di applicazione che condivide requisiti di sicurezza comuni.
     - Clausola 4.2.5.2 di [`ETSI TS 119 472-3`_] (ISS-MDATA-EBD-4.2.5.2-04)

   * - ``policy_authority``
     - OPZIONALE. string.
       Identificatore dell'autorità o dell'entità responsabile della policy.
     - Clausola 4.2.5.2 di [`ETSI TS 119 472-3`_] (ISS-MDATA-EBD-4.2.5.2-05)

   * - ``policy_info_url``
     - OPZIONALE. string (URL).
       Collegamento a un sito web dell'Attestation Provider (AP) che spiega le linee guida della disclosure policy in termini comprensibili.
     - Clausola 4.2.5.2 di [`ETSI TS 119 472-3`_] (ISS-MDATA-EBD-4.2.5.2-13, EDP_05)

   * - ``authorized_parties``
     - OBBLIGATORIO. array of objects. se ``policy_type`` è ``"authorized_rp_only"``.
       Contiene un elenco di coppie di identificatori autorizzati (identificatore univoco a livello UE della Relying Party e identificatore di Service) autorizzate ad accedere all'Attestation.
     - Clausola 4.2.5.2 di [`ETSI TS 119 472-3`_] (ISS-MDATA-EBD-4.2.5.2-07)

   * - ``authorized_parties[].identifier``
     - OBBLIGATORIO. string.
       Identificatore univoco a livello UE della Relying Party autorizzata, come specificato in [`EIDAS-ARF`_] Reg_32.
       DEVE corrispondere al ``sub`` del WRPRC nella richiesta.
     - [`EIDAS-ARF`_] EDP_02

   * - ``authorized_parties[].service_identifier``
     - OBBLIGATORIO. string.
       Identificatore del Relying Party Service autorizzato, come specificato in [`EIDAS-ARF`_] Reg_33.
       DEVE corrispondere al ``srv_id`` del WRPRC nella richiesta.
     - [`EIDAS-ARF`_] EDP_02

   * - ``authorized_parties[].subject_dn``
     - OPZIONALE. string.
       Subject Distinguished Name (DN) della Relying Party, formattato come stringa LDAP conforme a :rfc:`4514`.
       Questa è la codifica ETSI di ISS-MDATA-EBD-4.2.5.2-07.
       Non è un input di valutazione: la Wallet Unit NON DEVE abbinarlo rispetto al WRPAC, e la valutazione EDP_02 usa la coppia di identificatori dal WRPRC, come specificato in :ref:`trust-evaluation:EUDIW Authorization`.
     - Clausola 4.2.5.2 di [`ETSI TS 119 472-3`_] (ISS-MDATA-EBD-4.2.5.2-07)

   * - ``authorized_parties[].entitlement_uri``
     - OPZIONALE. string (URI).
       Entitlement o sub-entitlement codificata come URI come specificato nell'Allegato A di [`ETSI TS 119 475`_], detenuta all'interno del Wallet-Relying Party Registration Certificate (WRPRC).
     - Clausola 4.2.5.2 di [`ETSI TS 119 472-3`_] (ISS-MDATA-EBD-4.2.5.2-07)

   * - ``trusted_roots``
     - OBBLIGATORIO. array of objects. se ``policy_type`` è ``"specific_root_of_trust"``.
       Definisce un elenco preciso di certificati root o intermedi fidati usati per firmare i WRPRC.
       Solo le RP il cui signing path del WRPRC contiene uno di questi certificati sono autorizzate all'accesso.
     - Clausola 4.2.5.2 di [`ETSI TS 119 472-3`_] (ISS-MDATA-EBD-4.2.5.2-08)

   * - ``trusted_roots[].issuer_dn``
     - OBBLIGATORIO. string.
       Issuer Distinguished Name (DN) in forma di stringa LDAP conforme a :rfc:`4514`.
     - Clausola 4.2.5.2 di [`ETSI TS 119 472-3`_] (ISS-MDATA-EBD-4.2.5.2-09)

   * - ``trusted_roots[].serial_number``
     - OBBLIGATORIO. string.
       Serial number del certificato corrispondente all'issuer definito.
     - Clausola 4.2.5.2 di [`ETSI TS 119 472-3`_] (ISS-MDATA-EBD-4.2.5.2-09)

   * - ``extensions``
     - OPZIONALE. array of objects.
       Contenitore per strutture di estensione EDP supplementari.

       Queste strutture POSSONO essere ignorate dalla Wallet Unit, ma la Wallet Unit DOVREBBE elaborare con successo i restanti dati EDP anche se sono presenti estensioni non riconosciute.
       Le estensioni POSSONO essere usate per fornire regole di policy alternative applicate ad attributi specifici all'interno di una EAA soggetta a Selective Disclosure.
     - Clausola 4.2.5.2 di [`ETSI TS 119 472-3`_] (ISS-MDATA-EBD-4.2.5.2-10, ISS-MDATA-EBD-4.2.5.2-11, ISS-MDATA-EBD-4.2.5.2-12)

Di seguito esempi non normativi di EDP con i tipi di policy Authorized Relying Parties Only e Specific Root of Trust.

.. literalinclude:: ../../examples/edp-authorized-rps.json
  :language: json

.. literalinclude:: ../../examples/edp-specific-root.json
  :language: json

Embedded Disclosure Policy Lifecycle
""""""""""""""""""""""""""""""""""""

L'EDP memorizzata localmente DEVE restare valida finché l'Attestation a cui è associata è valida e non revocata.
L'EDP NON DEVE avere uno status di validità indipendente o un meccanismo di revoca separato dall'Attestation.

Se un Attestation Provider aggiunge, modifica o cancella un'EDP per un Attestato Elettronico che emette, l'Attestation Provider DEVE revocare tale Attestato Elettronico.
La Wallet Unit rileva il cambiamento di EDP indirettamente attraverso il normale meccanismo di controllo dello status dell'Attestation (Status List), che riporterà l'Attestato Elettronico come revocato.
L'EDP memorizzata localmente è quindi implicitamente invalidata insieme all'Attestato Elettronico.
L'Utente deve richiedere una nuova emissione per ottenere l'Attestato Elettronico con l'EDP aggiornata.

Anche una modifica minore della policy (ad es., l'aggiunta di una singola RP all'elenco autorizzato) richiede la revoca e la riemissione.
Il momento del rilevamento dipende da quando la Wallet Unit controlla lo status dell'Attestato Elettronico: se la Wallet Unit controlla solo al momento della presentazione, un cambiamento di policy non sarà rilevato fino al successivo tentativo di presentazione.

.. warning::

    **Proactive refresh**.
    L'Attestation Provider PUÒ fornire l'EDP attraverso il suo URI.
    In questo caso, la Wallet Unit PUÒ recuperare proattivamente il contenuto dell'EDP all'``policy_uri`` per verificare aggiornamenti, senza attendere un segnale di revoca dell'Attestato Elettronico.
    Tuttavia, questo meccanismo NON DOVREBBE essere usato in questa specifica per il seguente motivo:

    - Consente all'Attestation Provider di modificare unilateralmente un'EDP, e può introdurre rischi per la privacy e overhead di gestione (come indicato nel Discussion Topic D)
    - I dettagli tecnici di questo meccanismo non sono definiti all'interno dello standard ETSI.

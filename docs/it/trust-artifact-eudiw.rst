.. include:: ../common/common_definitions.rst
.. Included via infrastructure-trust.rst at title level '-' (level 1).

EUDIW Trust Artifacts
---------------------

Questa sezione definisce gli artifact di trust richiesti e i relativi ruoli concettuali nell'ecosistema EUDIW secondo `EIDAS-ARF`_, tra cui:

- :ref:`infrastructure-trust:Register of WRPs`;
- :ref:`infrastructure-trust:Wallet-Relying Party Access Certificate (WRPAC) Profile`;
- :ref:`infrastructure-trust:Registrar Sign/Seal Certificate Profile`;
- :ref:`infrastructure-trust:Wallet-Relying Party Registration Certificate (WRPRC) Profile`;
- :ref:`infrastructure-trust:Trusted List, Lists of Trusted Lists, and Lists of Trusted Entities`;
- :ref:`infrastructure-trust:Embedded Disclosure Policy (EDP)`.

Il modello dati di questi Trust Artifacts profila le seguenti specifiche esterne.

- `ETSI TS 119 602`_, che definisce il modello dati delle Lists of Trusted Entities e i profili delle liste EUDIW.
- `ETSI TS 119 411-8`_, che definisce il Wallet-Relying Party Access Certificate.
- `ETSI TS 119 475`_, che definisce il Wallet-Relying Party Registration Certificate insieme ai relativi entitlements.
- `ETSI EN 319 412-1`_, che definisce gli attributi del subject dei certificati.
- `ETSI TS 119 182-1`_, che definisce il formato JAdES della firma di una List of Trusted Entities.
- `ETSI EN 319 132-1`_, che definisce il formato XAdES della firma di Trusted List e List of Trusted Lists.

Register of WRPs
^^^^^^^^^^^^^^^^

Il Register of WRPs nazionale è il sistema pubblicamente accessibile (dataset + API) che fornisce dichiarazioni di registrazione firmate/sigillate sulle WRP e sulle relative autorizzazioni/declared usage.
Questa sezione documenta un profilo allineato a `EUDI-TS 5`_ che soddisfa i vincoli dell'Annex II di `CIR2025/848`_ e `CIR2025/848-Amendment`_.

Register Dataset
""""""""""""""""

Il formato dati per le informazioni disponibili tramite l'open API fornita dal Register of WRPs nazionale DEVE conformarsi agli schemi dati descritti nelle Tables 1-11 dell'Annex VI di `CIR2025/848-Amendment`_.
Di seguito alcuni esempi non normativi di oggetti ``WalletRelyingParty`` memorizzati nel Register.

Una banca registrata come Relying Party che richiede PID per procedure know-your-customer.

.. literalinclude:: ../../examples/register-wrp-rp.json
  :language: JSON

Una banca registrata sia come Relying Party che richiede PID sia come QEAA Provider (che emette attestazioni di conto bancario al Wallet).
Ha sia ``intendedUse`` sia ``providesAttestations``.

.. literalinclude:: ../../examples/register-wrp-rp-ap.json
  :language: JSON

Un'entità registrata come Intermediary designato che agisce per conto delle WRP durante le interazioni con il Wallet.
Ha ``isIntermediary: true`` e non dichiara ``intendedUse`` (non richiesto quando la registrazione avviene esclusivamente come Intermediary).

.. literalinclude:: ../../examples/register-wrp-rp-intermediary.json
  :language: JSON


Register Open APIs
""""""""""""""""""

I metodi di lettura comuni dell'API (GET) DEVONO essere aperti all'accesso pubblico (senza autenticazione preventiva), restituire statement firmati JWS
e fornire metodi per la ricerca e l'interrogazione di dataset completi di WRP registrate corrispondenti ai parametri di query forniti.

- **GET /wrp**: Ottiene un elenco di WRP con filtraggio opzionale (definito nell'Annex VI di `CIR2025/848-Amendment`_) e paginazione.
  Una risposta con esito positivo (``200``) DEVE essere un response body firmato JWS.
  Il payload decodificato DEVE contenere un array di oggetti ``WalletRelyingParty`` corrispondenti alla query e, ove rilevante, accompagnato da informazioni storiche WRPAC nello statement/profilo utilizzato dallo Stato membro.
  L'elenco di tutte le WRP registrate viene restituito quando non sono forniti parametri di query.
- **GET /wrp/check-intended-use**: Endpoint dedicato al controllo dell'intended use per eseguire query mirate relative all'intended use dal Register.
  Una risposta con esito positivo (``200``) DEVE fornire una risposta booleana ``true`` o ``false`` firmata JWS, determinata dal parametro interrogato nelle informazioni di intended use del Registrar per la specifica WRP.
  Se la richiesta è invalida/incompleta o la WRP indicata non è trovata, l'endpoint DEVE rispondere rispettivamente con codice di errore ``400`` e ``401``.

.. note::
    La vista API pubblicata esclude solo ``postalAddress`` (`CIR2025/848-Amendment`_, Annex I, point 4).
    Tutti gli altri campi, inclusi i credential claim di intended use, sono pubblicati come registrati.

Il file YAML della specifica OpenAPI descritta nella Section 3 di `EUDI-TS 5`_ v1.3 è disponibile all'indirizzo https://github.com/eu-digital-identity-wallet/eudi-doc-standards-and-technical-specifications/blob/main/docs/technical-specifications/api/ts5-openapi31-registrar-api.yml.

.. warning::
  Oltre al parametro di filtraggio nel file YAML sopra, questa specifica richiede il supporto del parametro ``providesattestation`` per interrogare le WRP che forniscono il tipo di attestation interrogato, come previsto in `CIR2025/848-Amendment`_.

Wallet-Relying Party Access Certificate (WRPAC) Profile
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Questa sezione estende il generale :ref:`infrastructure-trust:X.509 Certificate Profile` e specifica un **Certificate Profile** per i **Wallet-Relying Party Access Certificates (WRPACs)**.

Secondo l'Article 2 di [`CIR2025/848`_], un WRPAC è un certificato per sigilli o firme elettroniche che autentica e valida la WRP quando interagisce con l'EUDI Wallet.
Per ulteriori dettagli sul processo di autenticazione, vedere :ref:`trust-evaluation:EUDIW Authentication`.

La sospensione o la cancellazione dei servizi WRP comporta la revoca di tutti i WRPAC validi da parte dell'autorità emittente competente, in modo che la WRP non possa più interagire con le Wallet Unit.
Per ulteriori dettagli sui processi di Trust Management, vedere :ref:`infrastructure-trust:Trust Management and Lifecycle`.

L'Annex IV di [`CIR2025/848`_] stabilisce inoltre che i WRPAC sono destinati all'esecuzione di firme o sigilli elettronici e che DEVONO conformarsi almeno ai requisiti della Normalised Certificate Policy (NCP) specificati negli standard ETSI.
Tenendo conto di questi requisiti minimi, sono possibili diversi scenari, specificati nelle clausole seguenti: certificati emessi a natural persons o legal persons, a supporto di advanced signatures/seals o anche qualified signature/seals.
I requisiti condizionali sono definiti in base al caso specifico in cui rientrano i WRPAC.

I requisiti specifici per i WRPAC sono specificati in `ETSI TS 119 411-8`_.

La tabella seguente definisce l'insieme completo delle extensions applicabili al certificate profile.
Le extensions non elencate nella tabella NON DEVONO essere presenti.

.. list-table:: Wallet-Relying Party Access Certificate Extensions
   :class: longtable
   :header-rows: 1
   :widths: 25 75

   * - **Extension**
     - **Description**

   * - ``authorityKeyIdentifier``
     - REQUIRED. Il valore DOVREBBE essere derivato dalla chiave pubblica utilizzando i metodi definiti in :rfc:`5280#section-4.2.1.1`.

   * - ``subjectKeyIdentifier``
     - OPTIONAL. Se presente, il campo ``keyIdentifier`` DOVREBBE essere derivato dalla chiave pubblica del subject utilizzando i metodi definiti in :rfc:`5280#section-4.2.1.2`.

   * - ``keyUsage``
     - REQUIRED. DEVE contenere una (e una sola) delle impostazioni key-usage *Type A*, *Type B* o *Type F*. *Type A* DOVREBBE essere utilizzato secondo LEG-4.3.1-4 nella Clause 4.3.1 [`ETSI EN 319 412-3`_]. Per ulteriori dettagli, vedere Clause 4.3.2 [`ETSI EN 319 412-2`_] e Clause 4.3.1 [`ETSI EN 319 412-3`_].

   * - ``certificatePolicies``
     - REQUIRED. DEVE includere una struttura ``PolicyInformation`` con ``policyIdentifier`` impostato a uno dei seguenti valori (definiti in `ETSI TS 119 411-8`_):

       * ``0.4.0.194118.1.1`` (``NCP-n-eudiwrp``);
       * ``0.4.0.194118.1.2`` (``NCP-l-eudiwrp``);
       * ``0.4.0.194118.1.3`` (``QCP-n-eudiwrp``);
       * ``0.4.0.194118.1.4`` (``QCP-l-eudiwrp``).

       e ``policyQualifiers`` contenente un ``cpsURI`` che referenzia un URL dove si trova la CPS del Provider of WRPAC.

   * - ``subjectAltName``
     - REQUIRED.

   * - ``cRLDistributionPoints``
     - CONDITIONAL. **REQUIRED IF:** il certificato non include alcuna access location di un OCSP responder o l'extension validity assured definita in `ETSI EN 319 412-1`_.

   * - ``authorityInfoAccess``
     - REQUIRED. DEVE includere una struttura ``AccessDescription`` con ``accessMethod`` impostato a ``1.3.6.1.5.5.7.48.2`` (``id-ad-caIssuers``) e ``accessLocation`` che specifichi almeno una access location di un certificato CA valido della CA emittente.

       Se l'OCSP è supportato dalla CA emittente, l'extension DEVE includere una struttura ``AccessDescription`` con ``accessMethod`` impostato a ``1.3.6.1.5.5.7.48.1`` (``id-ad-ocsp``) e ``accessLocation`` che specifichi almeno un OCSP responder autorizzato a fornire informazioni sullo stato del certificato, come descritto in :ref:`infrastructure-trust:Online Certificate Status Protocol (OCSP)`.

.. note::
    **Dependency Considerations**: Gli attributi WRPAC DEVONO essere derivati dalle informazioni detenute nel Register come specificato nella clause 5.1.2 di `ETSI TS 119 475`_.
    Ciò implica anche che per alcuni attributi specifici nel WRPAC lo stesso valore DEVE essere presente nel corrispondente WRPRC, se presente.

Di seguito un esempio di WRPAC per legal persons conforme alla NCP.

.. literalinclude:: ../../examples/wrpac-ncp.txt
  :language: text

Registrar Sign/Seal Certificate Profile
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Questa sezione estende il generale :ref:`infrastructure-trust:X.509 Certificate Profile` e specifica un **Certificate Profile** per i **Registrar Sign/Seal Certificates**.

La tabella seguente definisce l'insieme completo delle extensions applicabili al certificate profile.
Le extensions non elencate nella tabella NON DEVONO essere presenti.

.. list-table:: Registrar Sign/Seal Certificate Extensions
   :class: longtable
   :header-rows: 1
   :widths: 25 75

   * - **Extension**
     - **Description**

   * - ``authorityKeyIdentifier``
     - REQUIRED. Il valore DOVREBBE essere derivato dalla chiave pubblica utilizzando i metodi definiti in :rfc:`5280#section-4.2.1.1`.

   * - ``subjectKeyIdentifier``
     - OPTIONAL. Se presente, il campo ``keyIdentifier`` DOVREBBE essere derivato dalla chiave pubblica del subject utilizzando i metodi definiti in :rfc:`5280#section-4.2.1.2`.

   * - ``keyUsage``
     - REQUIRED. DEVE contenere una (e una sola) delle impostazioni key-usage *Type A*, *Type B* o *Type F*. *Type A* DOVREBBE essere utilizzato secondo LEG-4.3.1-4 nella Clause 4.3.1 [`ETSI EN 319 412-3`_]. Per ulteriori dettagli, vedere Clause 4.3.2 [`ETSI EN 319 412-2`_] e Clause 4.3.1 [`ETSI EN 319 412-3`_].

   * - ``certificatePolicies``
     - REQUIRED. DEVE includere una struttura ``PolicyInformation`` rilevante per le pratiche della CA emittente.

   * - ``subjectAltName``
     - REQUIRED.

   * - ``cRLDistributionPoints``
     - CONDITIONAL. **REQUIRED IF:** il certificato non include alcuna access location di un OCSP responder o l'extension validity assured definita in `ETSI EN 319 412-1`_.

   * - ``authorityInfoAccess``
     - REQUIRED. DEVE includere una struttura ``AccessDescription`` con ``accessMethod`` impostato a ``1.3.6.1.5.5.7.48.2`` (``id-ad-caIssuers``) e ``accessLocation`` che specifichi almeno una access location di un certificato CA valido della CA emittente.

       Se l'OCSP è supportato dalla CA emittente, l'extension DEVE includere una struttura ``AccessDescription`` con ``accessMethod`` impostato a ``1.3.6.1.5.5.7.48.1`` (``id-ad-ocsp``) e ``accessLocation`` che specifichi almeno un OCSP responder autorizzato a fornire informazioni sullo stato del certificato, come descritto in :ref:`infrastructure-trust:Online Certificate Status Protocol (OCSP)`.

Di seguito un esempio non normativo di Registrar Sign/Seal Certificate per legal persons (non self-signed).

.. literalinclude:: ../../examples/registrar-sign-seal.txt
  :language: text


Wallet-Relying Party Registration Certificate (WRPRC) Profile
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Questa sezione definisce il Wallet-Relying Party Registration Certificate (WRPRC), come descritto in `EIDAS-ARF`_ e `ETSI TS 119 475`_.
Questo Trust Artifact fornisce informazioni dettagliate sul profilo di Authorization del Credential Issuer e della Relying Party, tra cui:

- attributi di identificazione core (clause 5.1 `ETSI TS 119 475`_),
- attributi di descrizione del servizio (clause 5.2.4 `ETSI TS 119 475`_),
- attributi di entitlement (vedere Annex A.2 `ETSI TS 119 475`_),
- attributi dell'autorità di supervisione (clause 5.2.4 `ETSI TS 119 475`_),
- attributi della Relying Party (clause 5.2.4 `ETSI TS 119 475`_),
- attributi del Credential Issuer (clause 5.2.4 `ETSI TS 119 475`_),
- attributi dell'Intermediary; cioè se la Relying Party si affida a un Intermediary per richiedere Credenziali Digitali (clause 5.2.4 `ETSI TS 119 475`_).

Il Wallet-Relying Party Registration Certificate DEVE essere formattato come signed JSON Web Token (JWT) o CBOR Web Token (CWT) :rfc:`8392`.
DEVE conformarsi ai requisiti sintattici e semantici specificati nell'Annex V paragraph 3 del CIR (EU) 2025/848 e in `ETSI TS 119 475`_.

Il Wallet-Relying Party Registration Certificate DEVE essere firmato con la chiave privata del Provider of the Wallet-Relying Party Registration Certificates.
In particolare:

- Il JWT DEVE essere firmato con una JSON Advanced Electronic Signature con profilo B-B come definito in `ETSI TS 119 182-1`_.
- Il CWT DEVE essere firmato con una Advanced Electronic Signature conforme alla struttura definita in :rfc:`9052` e :rfc:`9360`.

Di seguito un esempio non normativo di header e payload WRPRC per una Relying Party.

.. literalinclude:: ../../examples/wrprc-jwt-header.json
  :language: json

.. literalinclude:: ../../examples/wrprc-payload-ci.json
  :language: json

Di seguito un esempio non normativo di payload WRPRC per una Relying Party Intermediary.

.. literalinclude:: ../../examples/wrprc-payload-rpi.json
  :language: json

.. warning::

  `ETSI TS 119 475`_, Table 10 definisce il subfield del nome dell'intermediary come ``sname``.
  L'esempio nell'Annex C dello stesso standard utilizza invece ``name``.
  Questa specifica segue la Table 10 normativa e utilizza ``sname``.

Trusted List, Lists of Trusted Lists, and Lists of Trusted Entities
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Questa sezione descrive il formato e il contenuto di tre tipi di Trust Artifacts, ciascuno dei quali trasporta un elenco di Trust Anchor correnti e storici (contenitori di materiali crittografici e identificatori appartenenti a Entità affidabili).

Le Entità dell'ecosistema utilizzano queste liste per:

- **Validare l'affidabilità a runtime**: verificare un Trust Anchor (vedere :ref:`infrastructure-trust:Trust Anchor Certificate Profile`) per autenticare, autorizzare o validare un'entità o un artifact durante le operazioni live.
- **Eseguire la validazione storica**: validare le informazioni contenute nella lista a fini di audit storico.

I tre tipi distinti di trust list sono:

- Trusted Lists (TL): istituite ai sensi del Chapter II dell'Annex I di `CID2015/1505`_, come modificato da `CID2025/2164`_, e specificate in `ETSI TS 119 612`_.
  Ciascuno Stato membro pubblica una TL in formato XML.
  È firmata dal rispettivo Stato membro con una firma digitale XAdES a livello di conformità baseline B (come definito in `ETSI EN 319 132-1`_).
  Le TL sono pubblicate in formato machine-readable presso endpoint specificati nella LOTL.
  Queste Liste contengono informazioni correnti e storiche sull'accreditamento dei trust service provider, con riferimento a:

  - Qualified Trust Service Provider (QTSP), quali meccanismi di emissione e revoca di Qualified Certificates, QEAA Provider, qualified electronic archiving services.
  - Non-Qualified Trust Services quali EAA Provider.
  - Altri Trust Service definiti a livello nazionale, quali l'archiviazione.

   Nell'ambito di eIDAS, le TL sono mantenute dagli Stati membri, responsabili della tenuta dei record dei trust service provider sotto la rispettiva giurisdizione.
   Sono numerate e rinnovate periodicamente e pubblicate su un sito web per il download senza restrizioni.
   Per proteggerne l'integrità e garantirne l'autenticità, sono altresì firmate con certificati affidabili contenuti nella LOTL.

- List of Trusted Lists (LOTL): istituita ai sensi del Chapter II dell'Annex I di `CID2015/1505`_, come modificato da `CID2025/2164`_, e specificata in `ETSI TS 119 612`_.
  Esiste una sola LOTL, pubblicata in formato XML e firmata dalla European Commission (EC).
  Utilizza una firma digitale XAdES a livello di conformità baseline B (secondo `ETSI EN 319 132-1`_) e referenzia i certificati affidabili di ciascuna National Trusted List.
  Per facilitare la rotazione delle chiavi e gli aggiornamenti continui, la LOTL implementa un meccanismo di pivoting.
  È pubblicata in formato machine-readable presso un endpoint specificato nell'Official Journal of the European Union (`OJEU`_).

  Lo schema XML per Trusted Lists e List of Trusted Lists, con nome e descrizione dei parametri, è disponibile all'indirizzo ``https://forge.etsi.org/rep/esi/x19_612_trusted_lists/-/raw/v2.4.1/19612_xsd.xsd``. Attualmente la versione machine-readable della LOTL e delle National TLs è pubblicata su `EUMS-LOTL`_.

- Lists of Trusted Entities (LoTE): istituite ai sensi degli Articles 4 e 5 di `CIR2024/2980`_ e specificate in `ETSI TS 119 602`_.
  Sono disponibili in formato XML o JSON e sono firmate con una firma digitale AdES a livello di conformità baseline B (secondo `ETSI TS 119 182-1`_).
  Per facilitare gli aggiornamenti continui, la LoTE implementa un meccanismo di pivoting ed è pubblicata in formato machine-readable presso un endpoint specificato nell'`OJEU`_.
  I tipi di LoTE possono essere uno dei seguenti, come definito nell'annex C.2:

  - PID Provider;
  - Wallet Provider;
  - Provider of Wallet Relying Party Access Certificates;
  - Providers of Wallet Relying Party Registration Certificates;
  - Public sector bodies issuing Electronic Attestations of Attributes;
  - List of Registrars and Registers.

  Il repository seguente fornisce gli schemi JSON e XML normativi richiesti per l'implementazione della List of Trusted Entities (`ETSI-LOTE-SCHEMAS`_).

La tabella seguente fornisce una panoramica completa dell'architettura delle trust list eIDAS, con riferimenti incrociati a base giuridica, standard tecnici di riferimento, formati dati espliciti, profili di firma e dinamiche di pubblicazione per Trusted Lists (TL), List of Trusted Lists (LOTL) e le varie Lists of Trusted Entities (LoTE) per categoria.

.. list-table:: eIDAS Trust List Ecosystem Profiles
   :class: longtable
   :widths: 14 20 16 16 18 16
   :header-rows: 1

   * - **List Type**
     - **Legal Basis**
     - **Governing Standard & Format**
     - **Signature Profile**
     - **Scope & Signer**
     - **Publication & Update Mechanism**
   * - **Trusted Lists (TL)**
     - `CID2015/1505`_ (Annex I, Chapter II), amended by `CID2025/2164`_.
     - `ETSI TS 119 612`_; ``XML`` format.
     - XAdES digital signature, baseline B (`ETSI EN 319 132-1`_).
     - Member State scope; one list per Member State, signed by that Member State.
     - Machine-readable endpoint specified within the LOTL.
   * - **List of Trusted Lists (LOTL)**
     - `CID2015/1505`_ (Annex I, Chapter II), amended by `CID2025/2164`_.
     - `ETSI TS 119 612`_; ``XML`` format.
     - XAdES digital signature, baseline B (`ETSI EN 319 132-1`_).
     - European Union scope; a single global list signed by the European Commission (EC) that anchors the National Trusted Lists.
     - Machine-readable endpoint specified within the `OJEU`_.
       Implements a pivoting mechanism to handle continuous updates.
   * - **LoTE: PID Provider Lists**
     - Articles 4 and 5 of `CIR2024/2980`_.
     - `ETSI TS 119 602`_ Annex D; ``JSON`` format.
     - AdES digital signature, baseline B (`ETSI TS 119 182-1`_).
     - European Union scope; one list per specific ecosystem entity type.
     - Machine-readable endpoint specified within the `OJEU`_.
       Implements a pivoting mechanism to handle continuous updates.
   * - **LoTE: Wallet Provider (WP) Lists**
     - Articles 4 and 5 of `CIR2024/2980`_.
     - `ETSI TS 119 602`_ Annex E; ``JSON`` format.
     - AdES digital signature, baseline B (`ETSI TS 119 182-1`_).
     - European Union scope; one list per specific ecosystem entity type.
     - Machine-readable endpoint specified within the `OJEU`_.
       Implements a pivoting mechanism to handle continuous updates.
   * - **LoTE: Provider of WRPAC Lists**
     - Articles 4 and 5 of `CIR2024/2980`_.
     - `ETSI TS 119 602`_ Annex F; ``JSON`` format.
     - AdES digital signature, baseline B (`ETSI TS 119 182-1`_).
     - European Union scope; one list per specific ecosystem entity type (Wallet Relying Party Access Certificate).
     - Machine-readable endpoint specified within the `OJEU`_.
       Implements a pivoting mechanism to handle continuous updates.
   * - **LoTE: Provider of WRPRC Lists**
     - Articles 4 and 5 of `CIR2024/2980`_.
     - `ETSI TS 119 602`_ Annex G; ``JSON`` format.
     - AdES digital signature, baseline B (`ETSI TS 119 182-1`_).
     - European Union scope; one list per specific ecosystem entity type (Wallet Relying Party Registration Certificate).
     - Machine-readable endpoint specified within the `OJEU`_.
       Implements a pivoting mechanism to handle continuous updates.
   * - **LoTE: PuB-EAA Provider Lists**
     - Articles 4 and 5 of `CIR2024/2980`_.
     - `ETSI TS 119 602`_ Annex H; ``JSON`` or ``XML`` format.
     - AdES digital signature, baseline B (`ETSI TS 119 182-1`_).
     - European Union scope; one list per specific ecosystem entity type.
     - Machine-readable endpoint specified within the `OJEU`_.
       Implements a pivoting mechanism to handle continuous updates.
   * - **LoTE: Registrar and Register Provider Lists**
     - Articles 4 and 5 of `CIR2024/2980`_.
     - `ETSI TS 119 602`_ Annex I; ``JSON`` format.
     - AdES digital signature, baseline B (`ETSI TS 119 182-1`_).
     - European Union scope; one list per specific ecosystem entity type.
     - Machine-readable endpoint specified within the `OJEU`_.
       Implements a pivoting mechanism to handle continuous updates.

L'esempio seguente mostra un esempio non normativo del payload di una List of Trusted Entities per PID Providers.

.. literalinclude:: ../../examples/lote-pid.json
  :language: json

Embedded Disclosure Policy (EDP)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Un Embedded Disclosure Policy (EDP) è definito nell'Article 2(9) del CIR 2024/2979 come: *"A set of rules, embedded in an electronic attestation of attributes by its provider, that indicates the conditions that a wallet-relying party has to meet to access the electronic attestation of attributes"*.

Gli Attestation Provider (cioè tutti i Credential Issuer tranne il PID Provider) possono esprimere opzionalmente un EDP per indicare quali Relying Party possono accedere a specifiche Credenziali Digitali.
L'Article 10 del CIR 2024/2979 stabilisce che i Wallet Provider DEVONO garantire che le Attestation con EDP comuni (come elencati nell'Annex III del CIR 2024/2979) possano essere elaborate dalle rispettive Wallet Unit.

Gli EDP sono applicabili a QEAAs, PuB-EAAs ed EAAs.
NON DEVONO essere applicabili ai PID.

L'EDP è distribuito tramite il Credential Issuer Metadata al momento dell'issuance.
L'Attestation Provider DEVE includere l'EDP (se presente) by value nel Credential Issuer Metadata, all'interno del parametro ``credential_configurations_supported``, in conformità con `OpenID4VCI`_ o l'estensione di esso specificata in `ETSI TS 119 472-3`_.
Se disponibile, la Wallet Unit DEVE memorizzare l'EDP localmente e associarlo alla specifica Attestation per cui è stato recuperato.
La Wallet Unit NON DEVE rivelare l'EDP alla Relying Party tramite il protocollo di presentation secondo `ETSI TS 119 472-3`_, Section 4.2.5.1.

Gli Embedded Disclosure Policy sono utilizzati per:

- Implementare access control settoriale (ad es. solo RP del settore pubblico o solo RP sanitarie).
- Implementare access control specifico per Stato membro (ad es. solo RP registrate in uno specifico Stato membro).

L'Annex III di [CIR 2024/2979] definisce tre tipi comuni di EDP:

- **No Policy.** Nessun EDP è presente, oppure l'EDP indica esplicitamente che non si applicano restrizioni (ISS-MDATA-EBD-4.2.5.2-06).

- **Authorized Relying Parties Only.** L'EDP contiene un elenco di RP autorizzate ad accedere all'Attestation.
  Secondo `ETSI TS 119 472-3`_ (ISS-MDATA-EBD-4.2.5.2-07), le RP autorizzate sono identificate dal subject distinguished name come riportato nel Wallet-Relying Party Access Certificate, in forma di stringa LDAP come definito in :rfc:`4514`.

  - Per legal persons, gli attributi DN rilevanti sono ``commonName``, ``organizationName``, ``organizationIdentifier`` e ``countryName``.
  - Per natural persons: ``commonName``, ``givenName``, ``surname``, ``serialNumber`` e ``countryName``.
    L'attribute type ``organizationIdentifier`` è rappresentato dalla stringa LDAP "ORGID"; l'attribute type ``serialNumber`` è rappresentato da "SN" (secondo `ETSI TS 119 472-3`_ NOTE 1 e NOTE 2 a ISS-MDATA-EBD-4.2.5.2-07).

- **Specific Root of Trust.** L'EDP contiene un elenco di trusted root o certificati intermediate.
  Solo le RP il cui Wallet-Relying Party Access Certificate fa chain a una di queste root è autorizzata ad accedere all'Attestation.
  Secondo `ETSI TS 119 472-3`_ (ISS-MDATA-EBD-4.2.5.2-08/09), ciascuna root autorizzata è identificata dal issuer distinguished name in forma di stringa LDAP come definito in RFC 4514 e dal certificate serial number dell'issuer.

.. note::

  `ETSI TS 119 472-3`_ (ISS-MDATA-EBD-4.2.5.2-07) consente anche di identificare le RP autorizzate mediante entitlements URI-encoded come specificato in `ETSI TS 119 475`_, riportati nel Wallet-Relying Party Registration Certificate.
  L'Annex A.3 di `ETSI TS 119 475`_ definisce sub-entitlements per Service Provider, attualmente per Payment Service Provider (ad es. ``https://uri.etsi.org/19475/SubEntitlement/psp/psp-ai``).
  Versioni future possono includere ulteriori sub-entitlements settoriali a livello nazionale o UE.
  Questa specifica supporta sia il meccanismo di identificazione mediante subject DN sia quello mediante entitlement URI.

.. note::

  `EIDAS-ARF`_ HLR EDP_02 fa riferimento agli *EU-wide unique identifiers*, come definiti in Reg_32, per l'elenco delle RP autorizzate.
  `ETSI TS 119 472-3`_ (ISS-MDATA-EBD-4.2.5.2-07) identifica le RP autorizzate mediante il subject DN dal Wallet-Relying Party Access Certificate.
  L'attributo ``organizationIdentifier`` all'interno del DN ha la stessa semantica dell'identificatore indicato in `EIDAS-ARF`_ HLR Reg_32.
  Questa specifica è allineata alla formulazione di `ETSI TS 119 472-3`_.

Embedded Disclosure Policy Data Model
""""""""""""""""""""""""""""""""""""""

La tabella seguente fornisce una panoramica completa del data model dell'Embedded Disclosure Policy, inclusi nomi dei parametri, tipi di dati, descrizioni e le specifiche clauses in `ETSI TS 119 472-3`_ in cui ciascun parametro è definito.

.. warning::
  I nomi dei parametri sono definiti in questa sezione e non si basano su una specifica ETSI normativa. La Section 4.2.5.2 di `ETSI TS 119 472-3`_ definisce i requisiti di alto livello per il data model, ma lo schema JSON finale sarà pubblicato separatamente da ETSI. La struttura definita qui è un profilo di implementazione basato sui requisiti del data model ETSI, e i nomi dei parametri POSSONO cambiare quando lo schema ETSI sarà pubblicato.

.. list-table:: Embedded Disclosure Policy Parameters
   :class: longtable
   :header-rows: 1
   :widths: 20 60 20

   * - **Parameter**
     - **Description**
     - **Reference**

   * - ``policy_uri``
     - REQUIRED. string (URI).
       Identificatore univoco dell'Embedded Disclosure Policy (EDP).

       L'associazione dell'EDP con un EAA DEVE essere stabilita includendo questo URI univoco.
       L'AP DEVE includere l'URI insieme al dataset completo della policy, oppure fornire solo l'URI se il dataset della policy è già stato pre-caricato nella Wallet Unit.
       L'EDP PUÒ essere accessibile tramite questo URI.
     - Clause 4.2.5.2 of [`ETSI TS 119 472-3`_] (ISS-MDATA-EBD-4.2.5.2-01, ISS-MDATA-EBD-4.2.5.2-02, ISS-MDATA-EBD-4.2.5.2-03)

   * - ``policy_type``
     - REQUIRED. string.
       Classificazione del tipo di policy.
       Valori validi:

       * ``"no_policy"``: Indica che non si applicano restrizioni di policy per l'EAA associato.
       * ``"authorized_rp_only"``: L'accesso è limitato a un elenco esplicito di Relying Party consentite.
       * ``"specific_root_of_trust"``: L'accesso è limitato alle Relying Party che fanno chain alle trusted root specificate.
     - Clause 4.2.5.2 of [`ETSI TS 119 472-3`_] (ISS-MDATA-EBD-4.2.5.2-06, ISS-MDATA-EBD-4.2.5.2-07, ISS-MDATA-EBD-4.2.5.2-08)

   * - ``description``
     - OPTIONAL. string.
       Descrizione dell'applicabilità della policy a una particolare comunità e/o classe di applicazione che condivide requisiti di sicurezza comuni.
     - Clause 4.2.5.2 of [`ETSI TS 119 472-3`_] (ISS-MDATA-EBD-4.2.5.2-04)

   * - ``policy_authority``
     - OPTIONAL. string.
       Identificatore dell'autorità o dell'entità responsabile della policy.
     - Clause 4.2.5.2 of [`ETSI TS 119 472-3`_] (ISS-MDATA-EBD-4.2.5.2-05)

   * - ``policy_info_url``
     - OPTIONAL. string (URL).
       Link a un sito web dell'Attestation Provider (AP) che spiega le linee guida della disclosure policy in termini comprensibili.
     - Clause 4.2.5.2 of [`ETSI TS 119 472-3`_] (ISS-MDATA-EBD-4.2.5.2-13, EDP_05)

   * - ``authorized_parties``
     - REQUIRED. array of objects. if ``policy_type`` is ``"authorized_rp_only"``.
       Contiene un elenco di Relying Party autorizzate ad accedere all'Attestation.
     - Clause 4.2.5.2 of [`ETSI TS 119 472-3`_] (ISS-MDATA-EBD-4.2.5.2-07)

   * - ``authorized_parties[].subject_dn``
     - OPTIONAL. string.
       Subject Distinguished Name (DN) della Relying Party estratto dal Wallet-Relying Party Access Certificate (WRPAC), formattato come stringa LDAP conforme a :rfc:`4514`.
       Almeno uno tra ``subject_dn`` o ``entitlement_uri`` DEVE essere presente in ciascun elemento.
     - Clause 4.2.5.2 of [`ETSI TS 119 472-3`_] (ISS-MDATA-EBD-4.2.5.2-07)

   * - ``authorized_parties[].entitlement_uri``
     - OPTIONAL. string (URI).
       Entitlement o sub-entitlement URI-encoded come specificato nell'Annex A di [`ETSI TS 119 475`_], riportati nel Wallet-Relying Party Registration Certificate (WRPRC).
       Almeno uno tra ``subject_dn`` o ``entitlement_uri`` DEVE essere presente in ciascun elemento.
     - Clause 4.2.5.2 of [`ETSI TS 119 472-3`_] (ISS-MDATA-EBD-4.2.5.2-07)

   * - ``trusted_roots``
     - REQUIRED. array of objects. if ``policy_type`` is ``"specific_root_of_trust"``.
       Definisce un elenco preciso di certificati trusted root o intermediate.
       Solo le RP i cui WRPAC fanno chain con successo a una di queste root sono autorizzate all'accesso.
     - Clause 4.2.5.2 of [`ETSI TS 119 472-3`_] (ISS-MDATA-EBD-4.2.5.2-08)

   * - ``trusted_roots[].issuer_dn``
     - REQUIRED. string.
       Issuer Distinguished Name (DN) in forma di stringa LDAP conforme a :rfc:`4514`.
     - Clause 4.2.5.2 of [`ETSI TS 119 472-3`_] (ISS-MDATA-EBD-4.2.5.2-09)

   * - ``trusted_roots[].serial_number``
     - REQUIRED. string.
       Certificate serial number corrispondente all'issuer definito.
     - Clause 4.2.5.2 of [`ETSI TS 119 472-3`_] (ISS-MDATA-EBD-4.2.5.2-09)

   * - ``extensions``
     - OPTIONAL. array of objects.
       Contenitore per strutture di extension EDP supplementari.

       Queste strutture POSSONO essere ignorate dalla Wallet Unit, ma la Wallet Unit DOVREBBE elaborare con successo i restanti dati EDP anche se sono presenti extension non riconosciute.
       Le extension POSSONO essere utilizzate per fornire regole di policy alternative applicate a specifici attributi all'interno di un EAA soggetto a Selective Disclosure.
     - Clause 4.2.5.2 of [`ETSI TS 119 472-3`_] (ISS-MDATA-EBD-4.2.5.2-10, ISS-MDATA-EBD-4.2.5.2-11, ISS-MDATA-EBD-4.2.5.2-12)

Di seguito esempi non normativi di EDP con policy type Authorized Relying Parties Only e Specific Root of Trust.

.. literalinclude:: ../../examples/edp-authorized-rps.json
  :language: json

.. literalinclude:: ../../examples/edp-specific-root.json
  :language: json

Embedded Disclosure Policy Lifecycle
""""""""""""""""""""""""""""""""""""

L'EDP memorizzato localmente DEVE restare valido finché l'Attestation a cui è associato è valida e non revocata.
L'EDP NON DEVE avere uno stato di validità indipendente o un meccanismo di revoca separato dall'Attestation.

Se un Attestation Provider aggiunge, modifica o elimina un EDP per una Credenziale Digitale che emette, l'Attestation Provider DEVE revocare tale Credenziale Digitale.
La Wallet Unit rileva la modifica dell'EDP indirettamente tramite il normale meccanismo di controllo dello stato dell'Attestation (Status List), che segnalerà la Credenziale Digitale come revocata.
L'EDP memorizzato localmente risulta quindi implicitamente invalidato insieme alla Credenziale Digitale.
L'Utente deve richiedere una nuova issuance per ottenere la Credenziale Digitale con l'EDP aggiornato.

Anche una modifica minima della policy (ad es. aggiunta di una singola RP all'elenco autorizzato) richiede revoca e re-issuance.
La tempistica del rilevamento dipende da quando la Wallet Unit controlla lo stato della Credenziale Digitale: se la Wallet Unit controlla solo al momento della presentation, una modifica della policy non sarà rilevata fino al successivo tentativo di presentation.

.. warning::

    **Proactive refresh**.
    L'Attestation Provider PUÒ fornire l'EDP tramite il proprio URI.
    In tal caso, la Wallet Unit PUÒ recuperare proattivamente il contenuto dell'EDP all'indirizzo ``policy_uri`` per verificare aggiornamenti, senza attendere un segnale di revoca della Credenziale Digitale.
    Tuttavia, questo meccanismo NON DOVREBBE essere utilizzato in questa specifica per i seguenti motivi:

    - Consente all'Attestation Provider di modificare unilateralmente un EDP e può introdurre rischi per la privacy e overhead gestionale (come indicato nel Discussion Topic D)
    - I dettagli tecnici di questo meccanismo non sono definiti nello standard ETSI.



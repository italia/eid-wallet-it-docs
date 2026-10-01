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
Il dataset e l'API di lettura del Register sono `EUDI-TS 5`_, oggetti ``WalletRelyingParty`` e ``WalletRelyingPartyService``, e soddisfano l'Allegato II di `CIR2025/848`_ come modificato da [`CIR2026/1730`_].

.. note::
    **Deviazione di profilo.** L'identificatore del Relying Party Service, e l'emissione di più di un Wallet-Relying Party Access Certificate o di un Wallet-Relying Party Registration Certificate per Wallet-Relying Party ([`EIDAS-ARF`_] Reg_10a, Reg_10d, Reg_33, Reg_34a e RPRC_07a), non sono requisiti di questa specifica finché ETSI e le Technical Specification dell'ARF non ne definiscono l'implementazione.
    `EUDI-TS 5`_ marca ``serviceIdentifier`` come ``[0..1]``.
    `ETSI TS 119 411-8`_ non definisce ancora un attributo per tale identificatore, e `ETSI TS 119 475`_ non definisce ancora ``srv_id``.
    Fino ad allora, questa specifica non richiede ``serviceIdentifier``, un'entità ottiene un solo WRPAC, e il Provider of WRPRC emette un solo WRPRC per quell'entità.

Register Dataset
""""""""""""""""

Il formato dati per le informazioni disponibili attraverso l'API aperta fornita dal Register of WRPs nazionale MUST essere conforme agli schemi dati descritti nelle Tabelle 1-11 dell'Allegato VI di [`CIR2025/848`_] come modificato da [`CIR2026/1730`_], codificati come JSON Schema ``WalletRelyingParty`` di `EUDI-TS 5`_.
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

I metodi di lettura sono la Sezione 3 di `EUDI-TS 5`_.
Metodi, parametri di filtro, codici di risposta e la riduzione di ``services`` quando si usa ``serviceidentifier`` sono definiti lì.

.. note::
    La vista API pubblicata esclude solo ``postalAddress`` ([`CIR2025/848`_] come modificato da [`CIR2026/1730`_], Allegato I, punto 4).
    Tutti gli altri campi, inclusi i claim di credenziale dell'uso previsto, sono pubblicati come registrati.
    Le Register Open APIs restano per pubblicazione e trasparenza ([`EIDAS-ARF`_] Reg_03, Reg_06).
    La Wallet Unit MUST NOT usarle come sostituto di un Wallet-Relying Party Registration Certificate mancante o non valido durante la Presentazione di Credenziali o l'Emissione di Credenziali, come specificato in :ref:`trust-evaluation:EUDIW Authorization`.

Il file YAML della specifica OpenAPI descritta nella Sezione 3 di `EUDI-TS 5`_ è disponibile come `EUDI-TS 5 OpenAPI`_.
Lo JSON Schema dell'oggetto ``WalletRelyingParty``, incluso l'array ``services`` di ``WalletRelyingPartyService``, è disponibile come `EUDI-TS 5 JSON Schema`_.
Il profilo di lettura nazionale di tale API è disponibile :raw-html:`<a href="OAS3-Register-API-READ.html" target="_blank">qui</a>`.

Wallet-Relying Party Access Certificate (WRPAC) Profile
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Questa sezione estende il :ref:`infrastructure-trust:X.509 Certificate Profile` generale e specifica un **Certificate Profile** per i **Wallet-Relying Party Access Certificates (WRPACs)**.

Il WRPAC è il certificato definito nell'Articolo 2 e nell'Allegato IV di [`CIR2025/848`_].
Il suo profilo è `ETSI TS 119 411-8`_.
Le estensioni non specificate da quel documento MUST NOT essere presenti.
Gli attributi del subject sono [`EIDAS-ARF`_] Reg_31, Reg_32 e Reg_34, e `ETSI TS 119 411-8`_.
L'autenticazione è specificata in :ref:`trust-evaluation:EUDIW Authentication`.
La revoca in caso di sospensione o cancellazione dei servizi della WRP è specificata in :ref:`infrastructure-trust:Trust Management and Lifecycle`.
L'identificatore del Relying Party Service e un WRPAC per Service sono rinviati come specificato in :ref:`infrastructure-trust:Register of WRPs`.

.. note::
    Gli attributi del WRPAC MUST essere derivati dal Register come specificato nella clausola 5.1.2 di `ETSI TS 119 475`_.

    **Deviazione di profilo.** La Certificate Transparency ([`EIDAS-ARF`_] CT_01 a CT_06) non è un requisito di questa specifica finché le Technical Specification dell'ARF non la rendono pienamente disponibile e chiara per le implementazioni.
    Il profilo del WRPAC non include un Signed Certificate Timestamp, il Provider of WRPAC non è tenuto a registrare i WRPAC emessi, e la Wallet Unit non è tenuta a verificare la Certificate Transparency durante l'Autenticazione.

Di seguito un esempio di WRPAC per persone giuridiche secondo la NCP.

.. literalinclude:: ../../examples/wrpac-ncp.txt
  :language: text

Registrar Sign/Seal Certificate Profile
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Questa sezione estende il :ref:`infrastructure-trust:X.509 Certificate Profile` generale e specifica un **Certificate Profile** per i **Registrar Sign/Seal Certificates**.

La tabella seguente definisce l'insieme completo di estensioni applicabili al profilo di certificato.
Le estensioni non elencate nella tabella MUST NOT essere presenti.

.. list-table:: Estensioni del Registrar Sign/Seal Certificate
   :class: longtable
   :header-rows: 1
   :widths: 25 75

   * - **Extension**
     - **Descrizione**

   * - ``authorityKeyIdentifier``
     - REQUIRED. Il valore SHOULD essere derivato dalla chiave pubblica usando i metodi definiti in :rfc:`5280#section-4.2.1.1`.

   * - ``subjectKeyIdentifier``
     - OPTIONAL. Se presente, il campo ``keyIdentifier`` SHOULD essere derivato dalla chiave pubblica del subject usando i metodi definiti in :rfc:`5280#section-4.2.1.2`.

   * - ``keyUsage``
     - REQUIRED. MUST contenere uno (e uno solo) dei key-usage settings *Type A*, *Type B*, o *Type F*. *Type A* SHOULD essere usato secondo LEG-4.3.1-4 nella Clausola 4.3.1 [`ETSI EN 319 412-3`_]. Per dettagli aggiuntivi, vedi Clausola 4.3.2 [`ETSI EN 319 412-2`_] e Clausola 4.3.1 [`ETSI EN 319 412-3`_].

   * - ``certificatePolicies``
     - REQUIRED. MUST includere una struttura ``PolicyInformation`` rilevante per le pratiche della CA emittente.

   * - ``subjectAltName``
     - REQUIRED.

   * - ``cRLDistributionPoints``
     - CONDITIONAL. **REQUIRED IF:** il certificato non include alcuna access location di un responder OCSP o l'estensione validity assured come definita in `ETSI EN 319 412-1`_.

   * - ``authorityInfoAccess``
     - REQUIRED. MUST includere una struttura ``AccessDescription`` con ``accessMethod`` impostato a ``1.3.6.1.5.5.7.48.2`` (``id-ad-caIssuers``) e ``accessLocation`` che specifica almeno una access location di un certificato CA valido della CA emittente.

       Se l'OCSP è supportato dalla CA emittente, l'estensione MUST includere una struttura ``AccessDescription`` con ``accessMethod`` impostato a ``1.3.6.1.5.5.7.48.1`` (``id-ad-ocsp``) e ``accessLocation`` che specifica almeno un responder OCSP autorevole a fornire informazioni di status del certificato per il certificato, come descritto in :ref:`infrastructure-trust:Online Certificate Status Protocol (OCSP)`.

Di seguito un esempio non normativo di Registrar Sign/Seal Certificate per persone giuridiche (non self-signed).

.. literalinclude:: ../../examples/registrar-sign-seal.txt
  :language: text


Wallet-Relying Party Registration Certificate (WRPRC) Profile
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Questa sezione profila il Wallet-Relying Party Registration Certificate (WRPRC) definito in `EIDAS-ARF`_ e in `ETSI TS 119 475`_.
I suoi contenuti sono la clausola 5.1, la clausola 5.2.4 e l'Allegato A.2 di `ETSI TS 119 475`_, e l'Allegato V paragrafo 3 di [`CIR2025/848`_].
È un JWT firmato o un CWT (:rfc:`8392`), firmato con la chiave privata del Provider of Wallet-Relying Party Registration Certificates.
La firma JWT è una firma JAdES con il profilo B-B (`ETSI TS 119 182-1`_).
La firma CWT segue :rfc:`9052` e :rfc:`9360`.

Il Provider of WRPRC emette un solo WRPRC per l'entità, automaticamente, come definito in :ref:`onboarding-system:Wallet-Relying Party Registration Certificate Issuance`.
Il vincolo di tale certificato a un identificatore di Relying Party Service, e l'emissione di più di un WRPRC per entità, sono rinviati come specificato in :ref:`infrastructure-trust:Register of WRPs`.

L'oggetto ``intermediary`` è la clausola 5.2.4 di `ETSI TS 119 475`_ e [`EIDAS-ARF`_] RPRC_04.
La Wallet Unit valuta la presentazione intermediata come specificato in :ref:`trust-evaluation:EUDIW Authorization`.

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

Trusted List, Lists of Trusted Lists, and Lists of Trusted Entities
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Questa sezione descrive il formato e i contenuti di tre tipi di Trust Artifact, ciascuno dei quali convoglia un elenco di Trust Anchor correnti e storici (contenitori di materiali crittografici e identificatori appartenenti a Entità fidate).

Le Entità dell'ecosistema utilizzano queste list per:

- **Validare l'affidabilità a runtime**: Verificare un Trust Anchor (vedi :ref:`infrastructure-trust:Trust Anchor Certificate Profile`) per autenticare, autorizzare o validare un'entità o un artifact durante le operazioni live.
- **Eseguire la validazione storica**: Validare le informazioni contenute nella list per scopi di audit storico.

La tabella seguente mappa ciascuna list alla sua base giuridica, allo standard di governo, al formato e alla pubblicazione.
Lo schema XML delle Trusted List e della List of Trusted Lists è pubblicato all'indirizzo ``https://forge.etsi.org/rep/esi/x19_612_trusted_lists/-/raw/v2.4.1/19612_xsd.xsd``.
La List of Trusted Lists machine-readable e le Trusted List nazionali sono pubblicate in `EUMS-LOTL`_.
Gli schemi JSON e XML normativi delle List of Trusted Entities sono pubblicati in `ETSI-LOTE-SCHEMAS`_.


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
  
  Come suggerito in `EIDAS-ARF`_, per efficienza, le implementazioni MAY controllare routinariamente i Trust Anchor nelle List of Trusted Entities o nelle Trusted List e memorizzarli localmente. Questo consente, per esempio, alle Relying Party Instance in esecuzione su app mobili di facilitare le presentazioni offline.
  
L'esempio seguente mostra un esempio non normativo di payload di una List of Trusted Entities per PID Provider.

.. literalinclude:: ../../examples/lote-pid.json
  :language: json

Embedded Disclosure Policy (EDP)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Un'Embedded Disclosure Policy (EDP) è definita nell'Articolo 2(9) di [`CIR2024/2979`_].
Applicabilità e i tre tipi comuni di policy sono l'Articolo 10 e l'Allegato III di [`CIR2024/2979`_], codificati nella Sezione 4.2.5.2 di `ETSI TS 119 472-3`_ (ISS-MDATA-EBD-4.2.5.2-06, ISS-MDATA-EBD-4.2.5.2-07, ISS-MDATA-EBD-4.2.5.2-08 e ISS-MDATA-EBD-4.2.5.2-09).
Un'EDP MUST NOT essere applicata a un PID.
La Wallet Unit valuta i tipi comuni come specificato in :ref:`trust-evaluation:EUDIW Authorization`.
La non divulgazione verso la Relying Party è la Sezione 4.2.5.1 di `ETSI TS 119 472-3`_.

L'Attestation Provider MUST includere l'EDP, se presente, come membro ``embedded_disclosure_policy`` di ``credential_metadata`` all'interno di ``credential_configurations_supported``, in conformità con `OpenID4VCI`_ o l'estensione di esso specificata in `ETSI TS 119 472-3`_.
Il membro MUST contenere un ``policy_uri``.
Il membro MAY contenere i dati completi della policy in ``policy_data``.
La Wallet Unit MAY ricevere solo ``policy_uri`` quando la policy esatta identificata da tale URI è già precaricata.
Altrimenti l'URI e i dati della policy MUST essere forniti insieme.
Un URI non risolto MUST far fallire l'associazione e la divulgazione interessata.
La Wallet Unit MUST NOT recuperare il contenuto della policy da ``policy_uri``.

.. note::

  L'HLR EDP_02 di `EIDAS-ARF`_ richiede una coppia di identificatori presa dal WRPRC nella richiesta (``sub`` e un identificatore di Service), non dal WRPAC, anche in una presentazione **diretta**.
  L'identificatore di Service è rinviato come specificato in :ref:`infrastructure-trust:Register of WRPs`.
  Fino ad allora, la Wallet Unit confronta l'identificatore univoco a livello UE (``sub``) e, ove presente, l'URI di entitlement.
  `ETSI TS 119 472-3`_ (ISS-MDATA-EBD-4.2.5.2-07) codifica inoltre le parti autorizzate per subject DN o per URI di entitlement.
  Il parametro ``subject_dn`` è quella codifica ETSI; non è un input di valutazione rispetto al WRPAC.
  Il parametro ``entitlement_uri`` è abbinato rispetto alle entitlement detenute nel WRPRC.
  L'Allegato A.3 di `ETSI TS 119 475`_ definisce sub-entitlement per i Service Provider, attualmente per i Payment Service Provider (ad es. ``https://uri.etsi.org/19475/SubEntitlement/psp/psp-ai``).
  Per una presentazione **intermediata** il WRPRC nella richiesta è quello della Relying Party *intermediata* ([`EIDAS-ARF`_] RPRC_19).

Embedded Disclosure Policy Data Model
""""""""""""""""""""""""""""""""""""""

La tabella seguente fornisce una panoramica completa del modello dati dell'Embedded Disclosure Policy, inclusi i nomi dei parametri, i tipi di dati, le descrizioni e le clausole specifiche in `ETSI TS 119 472-3`_ in cui ciascun parametro è definito.

.. warning::
  I nomi dei parametri sono definiti in questa sezione e non si basano su una specifica ETSI normativa. La Sezione 4.2.5.2 di `ETSI TS 119 472-3`_ definisce i requisiti di alto livello per il modello dati, ma lo schema JSON finale sarà pubblicato separatamente da ETSI. La struttura definita qui è un profilo di implementazione basato sui requisiti del modello dati ETSI, e i nomi dei parametri MAY cambiare quando lo schema ETSI è pubblicato.

.. list-table:: Parametri dell'Embedded Disclosure Policy
   :class: longtable
   :header-rows: 1
   :widths: 20 60 20

   * - **Parameter**
     - **Descrizione**
     - **Riferimento**

   * - ``policy_uri``
     - REQUIRED. string (URI).
       Identificatore univoco dell'Embedded Disclosure Policy (EDP).

       L'associazione dell'EDP con una EAA MUST essere stabilita includendo questo URI univoco.
       La risoluzione dell'URI, inclusa la proibizione di recuperare il contenuto della policy da esso, è specificata sopra in :ref:`infrastructure-trust:Embedded Disclosure Policy (EDP)`.
     - Clausola 4.2.5.2 di [`ETSI TS 119 472-3`_] (ISS-MDATA-EBD-4.2.5.2-01, ISS-MDATA-EBD-4.2.5.2-02, ISS-MDATA-EBD-4.2.5.2-03)

   * - ``policy_type``
     - REQUIRED. string.
       Classificazione del tipo di policy.
       Valori validi:

       * ``"no_policy"``: Indica che non si applicano restrizioni di policy per la EAA associata.
       * ``"authorized_rp_only"``: L'accesso è ristretto a un elenco esplicito di Relying Party consentite.
       * ``"specific_root_of_trust"``: L'accesso è ristretto alle Relying Party il cui signing path del WRPRC contiene un certificato root o intermedio fidato specificato.
     - Clausola 4.2.5.2 di [`ETSI TS 119 472-3`_] (ISS-MDATA-EBD-4.2.5.2-06, ISS-MDATA-EBD-4.2.5.2-07, ISS-MDATA-EBD-4.2.5.2-08)

   * - ``description``
     - OPTIONAL. string.
       Descrizione dell'applicabilità della policy a una particolare comunità e/o classe di applicazione che condivide requisiti di sicurezza comuni.
     - Clausola 4.2.5.2 di [`ETSI TS 119 472-3`_] (ISS-MDATA-EBD-4.2.5.2-04)

   * - ``policy_authority``
     - OPTIONAL. string.
       Identificatore dell'autorità o dell'entità responsabile della policy.
     - Clausola 4.2.5.2 di [`ETSI TS 119 472-3`_] (ISS-MDATA-EBD-4.2.5.2-05)

   * - ``policy_info_url``
     - OPTIONAL. string (URL).
       Collegamento a un sito web dell'Attestation Provider (AP) che spiega le linee guida della disclosure policy in termini comprensibili.
     - Clausola 4.2.5.2 di [`ETSI TS 119 472-3`_] (ISS-MDATA-EBD-4.2.5.2-13, EDP_05)

   * - ``authorized_parties``
     - REQUIRED. array of objects. se ``policy_type`` è ``"authorized_rp_only"``.
       Contiene un elenco di Relying Party autorizzate ad accedere all'Attestation, identificate dall'identificatore univoco a livello UE. L'identificatore di Service di EDP_02 è rinviato come specificato in :ref:`infrastructure-trust:Register of WRPs`.
     - Clausola 4.2.5.2 di [`ETSI TS 119 472-3`_] (ISS-MDATA-EBD-4.2.5.2-07)

   * - ``authorized_parties[].identifier``
     - REQUIRED. string.
       Identificatore univoco a livello UE della Relying Party autorizzata, come specificato in [`EIDAS-ARF`_] Reg_32.
       MUST corrispondere al ``sub`` del WRPRC nella richiesta.
     - [`EIDAS-ARF`_] EDP_02

   * - ``authorized_parties[].subject_dn``
     - OPTIONAL. string.
       Subject Distinguished Name (DN) della Relying Party, formattato come stringa LDAP conforme a :rfc:`4514`.
       Questa è la codifica ETSI di ISS-MDATA-EBD-4.2.5.2-07.
       Non è un input di valutazione: la Wallet Unit MUST NOT abbinarlo rispetto al WRPAC, e la valutazione EDP_02 usa l'identificatore univoco a livello UE dal WRPRC, come specificato in :ref:`trust-evaluation:EUDIW Authorization`.
     - Clausola 4.2.5.2 di [`ETSI TS 119 472-3`_] (ISS-MDATA-EBD-4.2.5.2-07)

   * - ``authorized_parties[].entitlement_uri``
     - OPTIONAL. string (URI).
       Entitlement o sub-entitlement codificata come URI come specificato nell'Allegato A di [`ETSI TS 119 475`_], detenuta all'interno del Wallet-Relying Party Registration Certificate (WRPRC).
       Tale URI MUST essere confrontato in modo esatto.
     - Clausola 4.2.5.2 di [`ETSI TS 119 472-3`_] (ISS-MDATA-EBD-4.2.5.2-07)

   * - ``trusted_roots``
     - REQUIRED. array of objects. se ``policy_type`` è ``"specific_root_of_trust"``.
       Definisce un elenco preciso di certificati root o intermedi fidati usati per firmare i WRPRC.
       Solo le RP il cui signing path del WRPRC contiene uno di questi certificati sono autorizzate all'accesso.
     - Clausola 4.2.5.2 di [`ETSI TS 119 472-3`_] (ISS-MDATA-EBD-4.2.5.2-08)

   * - ``trusted_roots[].issuer_dn``
     - REQUIRED. string.
       Issuer Distinguished Name (DN) in forma di stringa LDAP conforme a :rfc:`4514`.
     - Clausola 4.2.5.2 di [`ETSI TS 119 472-3`_] (ISS-MDATA-EBD-4.2.5.2-09)

   * - ``trusted_roots[].serial_number``
     - REQUIRED. string.
       Serial number del certificato corrispondente all'issuer definito.
     - Clausola 4.2.5.2 di [`ETSI TS 119 472-3`_] (ISS-MDATA-EBD-4.2.5.2-09)

   * - ``extensions``
     - OPTIONAL. array of objects.
       Contenitore per strutture di estensione EDP supplementari.

       Queste strutture MAY essere ignorate dalla Wallet Unit.
       La Wallet Unit MUST elaborare con successo le regole riconosciute anche se sono presenti estensioni non riconosciute.
       L'estensione IT-Wallet è un oggetto con un identificatore di estensione, un claim ``path`` nel formato della Credenziale e una regola EDP comune alternativa.
       La policy di base disciplina la Credenziale.
       La regola di estensione corrispondente disciplina tale attributo.
       Ogni attributo divulgato MUST soddisfare la regola applicabile.
       La codifica dell'estensione MUST essere serializzabile nell'EDP.
       La codifica dell'estensione MUST NOT cambiare il risultato per gli attributi senza un path corrispondente.
     - Clausola 4.2.5.2 di [`ETSI TS 119 472-3`_] (ISS-MDATA-EBD-4.2.5.2-10, ISS-MDATA-EBD-4.2.5.2-11, ISS-MDATA-EBD-4.2.5.2-12)

Di seguito esempi non normativi di EDP con i tipi di policy Authorized Relying Parties Only e Specific Root of Trust.

.. literalinclude:: ../../examples/edp-authorized-rps.json
  :language: json

.. literalinclude:: ../../examples/edp-specific-root.json
  :language: json

Embedded Disclosure Policy Lifecycle
""""""""""""""""""""""""""""""""""""

L'EDP memorizzata localmente MUST restare valida finché l'Attestation a cui è associata è valida e non revocata.
L'EDP MUST NOT avere uno status di validità indipendente o un meccanismo di revoca separato dall'Attestation.

Se un Attestation Provider aggiunge, modifica o cancella un'EDP per un Attestato Elettronico che emette, l'Attestation Provider MUST revocare tale Attestato Elettronico.
La Wallet Unit rileva il cambiamento di EDP indirettamente attraverso il normale meccanismo di controllo dello status dell'Attestation (Status List), che riporterà l'Attestato Elettronico come revocato.
L'EDP memorizzata localmente è quindi implicitamente invalidata insieme all'Attestato Elettronico.
L'Utente deve richiedere una nuova emissione per ottenere l'Attestato Elettronico con l'EDP aggiornata.

Anche una modifica minore della policy (ad es., l'aggiunta di una singola RP all'elenco autorizzato) richiede la revoca e la riemissione.
Il momento del rilevamento dipende da quando la Wallet Unit controlla lo status dell'Attestato Elettronico: se la Wallet Unit controlla solo al momento della presentazione, un cambiamento di policy non sarà rilevato fino al successivo tentativo di presentazione.

.. warning::

    **Proactive refresh**.
    Questa specifica non usa il refresh proattivo di un'Embedded Disclosure Policy.
    La proibizione di recuperare il contenuto della policy da ``policy_uri``, e la revoca dell'Attestato Elettronico quando un'EDP cambia, sono specificate sopra in questa sezione.
    Il refresh proattivo è escluso perché consentirebbe a un Attestation Provider di modificare unilateralmente un'EDP, con le conseguenze di privacy e di gestione descritte nel Discussion Topic D, e perché i suoi dettagli tecnici non sono definiti nello standard ETSI.

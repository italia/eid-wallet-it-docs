.. include:: ../common/common_definitions.rst
.. Included via index.rst at title level '=' (document title).

Registry Infrastructure
=======================

L'ecosistema IT-Wallet opera tramite un'infrastruttura di registro che fornisce definizioni di dati standardizzate e capacità di discovery delle Credenziali. Il sistema di registro è costituito da più componenti interconnessi che supportano l'intero ciclo di vita delle operazioni sugli Attestati Elettronici, dall'onboarding delle entità alla presentazione dell'Attestato Elettronico.
L'architettura del registro affronta i requisiti di standardizzazione semantica e di discovery delle Credenziali tramite componenti di registro specializzati che assicurano interoperabilità e conformità nell'ecosistema.

A livello UE la Commissione Europea mantiene due cataloghi EUDIW che sono le controparti transfrontaliere dei registri semantici nazionali a cui i registri nazionali si allineano, definiti in ARF TS11 (`EUDI-TS 11`_) (Interfaces and formats for the Catalogue of Attributes and the Catalogue of Schemes):

 - **Catalogue of Attributes** è il catalogo a livello UE delle definizioni e dei namespace di attributi standardizzati utilizzati negli Attestati.
 - **Catalogue of Schemes** è il catalogo a livello UE degli schema di Attestato (``SchemaMeta``): i metadata machine-readable che vincolano un tipo di Attestato al proprio Rulebook e schema.

I registri e i cataloghi utilizzati all'interno dell'ecosistema IT-Wallet hanno finalità e ambiti diversi. I registri il cui contenuto è evidenza di una decisione di trust, quali il **Register of WRPs** operato da un Registrar nazionale ai sensi di `CIR2025/848`_ e i **Federation API Endpoints** del National Trust Framework, sono specificati in :ref:`infrastructure-trust:Infrastructure of Trust`.
I registri per la definizione semantica e la discovery dei dati sono dettagliati in questa Sezione.

In particolare, questa sezione fornisce innanzitutto una panoramica dell'infrastruttura di registro IT-Wallet (:ref:`registry:Registries and Catalogues of the Ecosystem`) e del suo meccanismo di discovery (:ref:`registry:Registry Discovery Endpoint`).
Quindi, ne dettaglia i componenti: :ref:`registry:Taxonomy`, :ref:`registry:Claims Registry`, :ref:`registry:Authentic Source Registry`, :ref:`registry:Schema Registry` e :ref:`registry:Digital Credentials Catalog`.
Infine, descrive le loro relazioni (:ref:`registry:Registry Integration and Cross-References`) e i journey di utilizzo (:ref:`registry:Registry Infrastructure Usage Journeys`).

Registries and Catalogues of the Ecosystem
-------------------------------------------

L'ecosistema IT-Wallet utilizza diversi registri e cataloghi, a livello nazionale e a livello UE, e essi servono due finalità diverse.

- **Finalità di trust**: il contenuto del registro è consumato da un Trust Evaluator per accettare o rifiutare un'entità o un artifact.
  Questi registri sono Trust Artifact, sono definiti in :ref:`infrastructure-trust:Infrastructure of Trust` e il modo in cui sono consumati è definito in :ref:`trust-evaluation:Trust Evaluation Process`.
- **Finalità semantica e di discovery**: il contenuto del registro definisce gli attributi, gli schema e i tipi di Credenziale, o li rende scopribili. Questi registri sono definiti in questa Sezione.

.. note::
  La distinzione tra registri di trust e registri semantici/di discovery è sulla finalità e non sul contenuto. Ad esempio, un registro con finalità semantica e di discovery può recare un parametro che punta a un trust framework, come fa ``trustedAuthorities`` del Digital Credentials Catalog, ma tale parametro identifica il trust framework applicabile e non è di per sé l'evidenza di una decisione di trust.

.. _table_registries_and_catalogues:
.. list-table:: Registries and Catalogues of the Ecosystem
   :class: longtable
   :widths: 32 18 26 24
   :header-rows: 1

   * - **Registry or Catalogue**
     - **Purpose**
     - **Maintained by**
     - **Specified in**
   * - Taxonomy, Claims Registry, Schema Registry, Authentic Source Registry, Digital Credentials Catalog
     - Semantica e discovery
     - Federation Trust Anchor, sotto l'Organismo di Supervisione
     - Questa Sezione
   * - Register of WRPs
     - Trust
     - Registrar
     - :ref:`infrastructure-trust:Register of WRPs`
   * - Federation API Endpoints, Entity Statements and Trust Marks
     - Trust
     - Federation Trust Anchor e Federation Intermediate
     - :ref:`infrastructure-trust:National Trust Artifacts`
   * - Catalogue of Attributes and Catalogue of Schemes
     - Semantica e discovery
     - Commissione Europea
     - [`EUDI-TS 11`_]. L'allineamento dei registri nazionali è descritto in :ref:`registry:Registry Integration and Cross-References`
   * - Lists of Trusted Entities, Trusted Lists and List of Trusted Lists
     - Trust
     - Commissione Europea e Stati membri
     - :ref:`infrastructure-trust:Trusted List, Lists of Trusted Lists, and Lists of Trusted Entities`

.. note::
  I meccanismi che pubblicano lo stato di un certificato o di un Attestato, quali le Certificate Revocation List, i responder OCSP e le Token Status List, non sono registri e non sono elencati nella tabella precedente.
  Sono descritti in :ref:`infrastructure-trust:Revocation Mechanisms`.

Cinque registri nazionali semantici e di discovery forniscono le definizioni standardizzate e i dati di discovery:

1. **Taxonomy**: Sistema di classificazione gerarchica che organizza le Credenziali per dominio e scopo.
2. **Claims Registry**: Definizioni semantiche standardizzate per i singoli attributi delle Credenziali e i tipi di dato.
3. **Authentic Source Registry**: Fonti Autentiche (AS) registrate con le loro capacità dichiarate, i claim disponibili e gli endpoint di verifica.
4. **Schema Registry**: Elenco autorevole degli Schema delle Credenziali.
5. **Digital Credentials Catalog**: Tipi di Credenziale disponibili con i relativi metadata e le informazioni di emissione.

I registri nazionali sono mantenuti dal Federation Trust Anchor sotto l'Organismo di Supervisione per assicurare coerenza, sicurezza e conformità normativa.
Sono popolati dai processi di onboarding descritti in :ref:`onboarding-system:Onboarding Processes`, e sono letti sia durante l'onboarding sia durante le fasi operative.

Le Entità che **forniscono** le informazioni sono le seguenti:

  - l'Attestation Scheme Provider, per la definizione di un tipo di Credenziale e del suo schema;
  - le Fonti Autentiche, per le loro capacità dati dichiarate;
  - le Wallet-Relying Party e i Fornitori di Wallet, per i loro dati di registrazione.

Questi ruoli sono descritti in :ref:`onboarding-system:System Actors and Roles`.

Nessuna di queste Entità scrive direttamente in un registro. Forniscono le informazioni tramite i processi di onboarding, che le verificano e le scrivono.
Ciascun registro è poi firmato e pubblicato dal Federation Trust Anchor per i registri nazionali e per gli statement di federazione, dal Registrar per il Register of WRPs, e dalla Commissione Europea per i cataloghi e le liste UE.

.. note::
  Non tutto il contenuto di un registro è fornito da un'Entità. Parte di esso è impostato dal Sistema di Onboarding stesso, quale lo stato di un tipo di Credenziale nel Digital Credentials Catalog, che deriva dalle condizioni della voce versionata. I componenti interni del Sistema di Onboarding e il processo che ciascuno di essi realizza sono descritti in :ref:`onboarding-system:System Components and Services`.

.. note::
  Un'Entità che fornisce un'informazione non è necessariamente l'Entità che la decide, perché le decisioni su un tipo di Credenziale sono assunte nel suo Attestation Rulebook, che è un input del Sistema di Onboarding.

La Figura :ref:`fig_registry_infrastructure` mostra l'insieme completo dei registri e dei cataloghi, raggruppati per finalità e per livello, con le Entità che ne forniscono il contenuto e le autorità che li pubblicano.

.. _fig_registry_infrastructure:
.. plantuml:: plantuml/registry-infrastructure.puml
    :width: 99%
    :caption: `Registries and Catalogues of the Ecosystem <https://www.plantuml.com/plantuml/svg/ZLL1R-D63xthLymNV41J8DaSkhq4RR1U9mK2T1T6d6AF1YFHDh6Z6M589UiM-zyx6bhMoEiqyaaUyZqEoKVE1nO8qjQs-1-vqhOLcj_cxw_cxrTpNpVUePERelZ9tEAQ79hbuk7-yMwPEKlRG1L-kIfzNNjtSyAozaukuGNPrtZvwrM9GMXD9GXEyAv0u0buYkjNt4tmecfLGgWcUBw0jIWJ7F5RkGMtmHNOAUvhibDTUKjegudEBMFWj_okoB6Gj49TiugFldKLXDsv0ranrk24oWjpzXaw1x3c0JV44WZvmYptTWEkChV4fN_6i3EBDZIUyUndyqzn4Csvm3VlVBsBP8_xpxCBytzk0Wd-VgPzxL0PfhH0zIfeo0uvxmwulyJR15nkiOQSOPbEfZC0v-XPArjCAIzz6qgSpbF6G-itBKQMMzfG_6Vc0QkE3IoRUMz_XUbxSTGS2ItBQvrvx8olD4BJmH2n2i5W_DfyULXm7dkGsYYFDSQpXYBu3wmmfE1cjhWtTwvgF3dXY_Wf93kp512iCHubWUYTFa7u-dgSxrcIsAuiFgEDeUx-6kgZP7yI2-U9QObN81BegHNa23jWklnc1ykKNgsISdvaIVAPG66zOCIcQqQS9e-LbcPe4MecGqxgErZ-irJBNVIhpxbjC3mJ-x3xwAiayk74T4SvIRPk8ykUGhDT1FzC5GRkb2w2BDfUJTeSp3bTlxm6BkXdH4U4JupDY25RG97aqFwNq4JabxHpBn_GxiXjp0A246hZz-68kSN09yVAtAjn54xt_N3VeDnAtV4S1yl0msRN7lGS-ZJazTEBdwwPUe_qagPvvigj3-FHqgbHIyuH7xSHmNv9mJ3MyVlDldUFD377GDsKjS4t2CxC3wSvGNfE8ZG-_fVnPrwstZIQ7XlPeYcz4tIIhCMHekBXZSdVbEk-D0bQuPeSfOJzsa3UGjarcCQ3X8tky-9OOc-m-x01HtzhGScjVQZrEz9gU10m9JJmH3QDPn7LTo1DlHapxgkjB1swsCimWGwx_jhSOcaXA6YSb1PjPnAm60j8QVQhTXmv7c8UzsZuJrHYrdHTEkgHR44CiUaV0wnECWtwk3QVVQUVFG_kzrXiL_hlr5XrkUF6XsWQ2OLfutJBDUsJ9TuYgquouP-u-_97M8x8otJQkM-KklRPdlOTaatE_VjpRJu1EG4Q0x84mKQs-Y3zF0NpxbtED3juzdNhN-zX0hZuWAvgQ_il>`_

La Figura :ref:`fig_registry_discovery` mostra, per i registri definiti in questa Sezione, la fase di onboarding o operativa in cui ciascuno di essi è letto e da chi. Maggiori dettagli sono forniti in ciascuna sezione.
Il modo in cui i registri con finalità di trust sono letti è descritto in :ref:`trust-evaluation:Trust Evaluation Process`.

.. _fig_registry_discovery:
.. plantuml:: plantuml/registry-discovery.puml
    :width: 99%
    :alt: The figure illustrates who reads the national semantic and discovery registries and in which phase.
    :caption: `Discovery on the Registry Infrastructure <https://www.plantuml.com/plantuml/svg/dLR1Rjim3BtxAxXWm58WQGxhBiDMT4jtw6K8cWux1ep4909ioPFafCQmVnybnucIEassNcfJvECZ-IZdpdcqlYhoB7kZjCWhIV1fV3CQtyp6fYYD9krli-mTtDD2QOBfvF7XwTiqSVPLYTA-7mbJ54RVTfmiZFP3t90p1Gq_Z2HwdAEZ2rmhH_O2DoLd0gsym9EUnGhracQO-mlSDvZdTDPnfBJpobTUXVgphwRI4ctTr-XdZWhKNea1zBvZSC0S7ccfdBUAt02cstD0BU5UEM7MP6kOLBOqZdfNy3lRpQ7lyTbeKzGCzhHzx0tWhIkjylIvrpQsTvN4Y1nLCRDDoX0v3WRNaZWFW2wD_bBv5KN2KrDPGPVZEB7YMbEiQRHSZY3Oc9jbHHnxhvQAts1iIGO-c3iOj-SdaFvasOIiCxeVTCKWF_XVwXlCx3UjdQUYhvohsBqp6JmqXsdqLeLx04jvhVHomWiMPzrxR0omjQJ1gJ3t2DXskscswnZ08OMz4FSWZOWdrgoLREhv6IsmCwKGZJT7yyuF-GysAmEMK3gGbGtiEJyOFJTSQtWjhM4MBZfdnuHXM9N3MpWKuSUTq2DMc108B76kSXNw0drSeyfndbCJwQx06t1CUM7iYVodKhSxSpwfqfwq90bbitmNPJsSSLjkAyGagT8B0tswNbuFaWIl8B_U_v9iUvsWy6hTr11d45JCJzqqzftjsA0iEzBA_y74ga8tbmt7y6m2RMLXAxsfoQDANMV6ewlYQ7JDAPX5VElAp_PwHu3uwLJoRBlZ9-iC6SGEUURhak9D7U9Gy_LdwLUbB1NiuDhn5lWyMsEkfFBrJ6BDSsQos47r8F-bLNS1mKRv5PyirPhqCUF3Ai-k8a-lG1_BbE6Zh-8CER6c84p-iW5w_dpDAq_k6kuRLIOAZbkJa_0HyyM5DMY5l6iY1v1sbULUyrIO6FitN2oLbXo_HY4T599ybv8gDYibLYzoXWmCxNbLObqhiuaYnRZUeQUxWhBkbJuzd7InryAFf15FtFJzRgSLx6xBm899HPa4ZNPjO_VTScf-aSS_vKoBlkEhB_mA_0i0>`_


Registry Discovery Endpoint
---------------------------

Il Federation Trust Anchor DEVE fornire un meccanismo di discovery per i componenti del registro tramite endpoint *well-known* standardizzati che forniscono metadata e informazioni di discovery REST API per gestire operazioni complesse quali paginazione e filtraggio.

Il Federation Trust Anchor DEVE pubblicare i metadata di discovery del registro all'endpoint ``.well-known/it-wallet-registry`` con supporto alla content negotiation:

- **Default Content-Type**: ``application/jwt`` (JWT firmato che assicura autenticità e integrità)
- **Alternative Content-Type**: ``application/json`` (JSON in chiaro per finalità di sviluppo/debug)

Di seguito è fornito un esempio non normativo.

.. code-block:: http

    GET /.well-known/it-wallet-registry HTTP/1.1
    Host: trust-anchor.eid-wallet.example.it
    Accept: application/jwt

    HTTP/1.1 200 OK
    Content-Type: application/jwt

    eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...

.. code-block:: http

    GET /.well-known/it-wallet-registry HTTP/1.1
    Host: trust-anchor.eid-wallet.example.it
    Accept: application/json

    HTTP/1.1 200 OK
    Content-Type: application/json

Registry Discovery Endpoint Parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Il payload JWT della risposta del Registry Discovery DEVE contenere i seguenti parametri:

.. list-table:: Registry Discovery Endpoint JWT Payload Parameters
   :class: longtable
   :widths: 30 70
   :header-rows: 1

   * - **Field Name**
     - **Description**
   * - **id**
     - OBBLIGATORIO. Identificativo univoco del documento Registry Discovery (ad es., ``urn:it-wallet-registry:it-wallet``).
   * - **version**
     - OBBLIGATORIO. La versione del documento Registry Discovery (ad es., ``1.0.0``).
   * - **last_modified**
     - OBBLIGATORIO. Il timestamp che indica quando l'elenco è stato aggiornato l'ultima volta (ad es., ``2025-03-15T12:00:00Z``).
   * - **endpoints**
     - OBBLIGATORIO. Oggetto JSON contenente gli URI di tutti i componenti del registro. Le seguenti chiavi di endpoint DEVONO essere presenti:

       * **claims_registry**: URI dell'API del Claims Registry.
       * **authentic_sources**: URI dell'API dell'Authentic Source Registry.
       * **credential_catalog**: URI dell'endpoint well-known del Digital Credentials Catalog.
       * **taxonomy**: URI della risorsa Taxonomy.
       * **schema_registry**: URI dell'API dello Schema Registry.
   * - **content_negotiation**
     - OBBLIGATORIO. Array dei content type supportati dall'endpoint di discovery (ad es., ``["application/json", "application/jwt"]``).

Struttura del payload JWT (quando decodificato):

.. code-block:: json

  {
    "id": "urn:it-wallet-registry:it-wallet",
    "version": "1.0.0",
    "last_modified": "2024-03-15T10:30:00Z",
    "endpoints": {
      "claims_registry": "https://trust-anchor.eid-wallet.example.it/api/v1/claims",
      "authentic_sources": "https://trust-anchor.eid-wallet.example.it/api/v1/authentic-sources",
      "credential_catalog": "https://trust-anchor.eid-wallet.example.it/api/v1/.well-known/credential-catalog",
      "taxonomy": "https://trust-anchor.eid-wallet.example.it/api/v1/taxonomy",
      "schema_registry": "https://trust-anchor.eid-wallet.example.it/api/v1/schemas"
    },
    "content_negotiation": ["application/json", "application/jwt"]
  }

Content Negotiation and Signed Representation
---------------------------------------------

Ogni endpoint della Registry Infrastructure DEVE supportare la content negotiation e servire il proprio contenuto in due rappresentazioni:

- **Default Content-Type**: ``application/jwt`` (JWT firmato che fornisce autenticità e integrità)
- **Alternative Content-Type**: ``application/json`` (JSON in chiaro per sviluppo e debug)

Entrambe le rappresentazioni sono servite allo stesso URL di endpoint, non come risorse o path distinti. Il client seleziona la rappresentazione con l'header di richiesta ``Accept``, e il Federation Trust Anchor indica la rappresentazione restituita nell'header di risposta ``Content-Type``. Se la richiesta non chiede un tipo supportato (``Accept`` assente, ``*/*``, o solo tipi non supportati), l'endpoint DEVE restituire la rappresentazione ``application/jwt``.

Questo requisito si applica a tutti gli endpoint della Registry Infrastructure elencati nella tabella seguente:

.. _table_registry_content_negotiation:
.. list-table:: Registry endpoints supporting content negotiation
   :class: longtable
   :header-rows: 1
   :widths: 40 60

   * - **Registry component**
     - **How the endpoint is located**
   * - Registry Discovery
     - Path well-known fisso ``.well-known/it-wallet-registry``.
   * - Claims Registry
     - URL assoluto pubblicato sotto la chiave ``claims_registry`` del documento di discovery.
   * - Authentic Source Registry
     - URL assoluto pubblicato sotto la chiave ``authentic_sources`` del documento di discovery.
   * - Schema Registry
     - URL assoluto pubblicato sotto la chiave ``schema_registry`` del documento di discovery.
   * - Taxonomy
     - URL assoluto pubblicato sotto la chiave ``taxonomy`` del documento di discovery.
   * - Digital Credentials Catalog
     - URL assoluto pubblicato sotto la chiave ``credential_catalog`` del documento di discovery.

Il Registry Discovery Endpoint è l'unico a un path well-known fisso. Un client lo legge per primo per ottenere l'URL di ogni altro componente dal suo oggetto ``endpoints`` firmato (si veda :ref:`registry:Registry Discovery Endpoint`). Un client NON DEVE assumere un path fisso per gli altri componenti. La content negotiation si applica all'endpoint di discovery e a ogni URL di componente che pubblica.

Tutti questi endpoint gestiscono la content negotiation allo stesso modo: la stessa richiesta, gli stessi due valori di ``Content-Type`` e la stessa rappresentazione firmata.

La rappresentazione firmata è un JWT in compact serialization, servito come ``application/jwt``. Il suo header DEVE contenere i parametri nella tabella seguente.

.. _table_catalog_parameters:
.. list-table:: JWT header parameters of the signed representation
   :class: longtable
   :header-rows: 1
   :widths: 25 50 25

   * - **Header parameter**
     - **Description**
     - **Reference**
   * - **typ**
     - OBBLIGATORIO. DEVE essere impostato a ``JWT``.
     - [:rfc:`7515` Section 4.1.9].
   * - **alg**
     - OBBLIGATORIO. Un identificativo di algoritmo di firma digitale come da registro IANA "JSON Web Signature and Encryption Algorithms". DEVE essere uno degli algoritmi supportati nella Sezione :ref:`algorithms:Algoritmi Crittografici` e NON DEVE essere impostato a ``none`` o con un identificativo di algoritmo simmetrico (MAC).
     - [:rfc:`7515` Section 4.1.1].
   * - **kid**
     - OBBLIGATORIO. Identificativo univoco della chiave pubblica.
     - [:rfc:`7515` Section 4.1.4].
   * - **x5c**
     - OPZIONALE. Contiene il certificato a chiave pubblica X.509 o la catena di certificati [:rfc:`5280`] corrispondente alla chiave utilizzata per firmare digitalmente il JWT. Quando il valore del parametro di header `kid` è presente, DEVE fare riferimento alla stessa chiave pubblica crittografica della foglia utilizzata con il certificato X.509.
     - [:rfc:`7515` Section 4.1.6.].
   * - **cty**
     - OBBLIGATORIO. DEVE essere impostato a ``application/json``.
     - [:rfc:`7515` Section 4.1.6.].

La rappresentazione in chiaro è lo stesso contenuto, servito come oggetto JSON in chiaro anziché come JWT firmato.

L'esempio non normativo seguente richiede entrambe le rappresentazioni dall'endpoint del Digital Credentials Catalog. L'URL è quello risolto dal documento di discovery, qui accorciato per leggibilità.

.. code-block:: http

    GET /.well-known/credential-catalog HTTP/1.1
    Host: trust-anchor.eid-wallet.example.it
    Accept: application/jwt

    HTTP/1.1 200 OK
    Content-Type: application/jwt

    eyJhbGciOiJSUzI1NiIsImtpZCI6ImV4YW1w...

.. code-block:: http

    GET /.well-known/credential-catalog HTTP/1.1
    Host: trust-anchor.eid-wallet.example.it
    Accept: application/json

    HTTP/1.1 200 OK
    Content-Type: application/json

Taxonomy
--------

La **Taxonomy** è il vocabolario autorevole che organizza le Credenziali nell'ecosistema IT-Wallet, ed è il fondamento semantico della loro interoperabilità. È indipendente dal formato della Credenziale.

In una singola risorsa, definisce la gerarchia di Domain, Class e Purpose che i tipi di Credenziale referenziano, a supporto della valutazione delle policy di autorizzazione e della standardizzazione a livello di ecosistema.

L'URL dell'endpoint Taxonomy è pubblicato sotto la chiave ``taxonomy`` del documento Registry Discovery. L'endpoint supporta la content negotiation e la rappresentazione firmata comuni a tutti gli endpoint della Registry Infrastructure (si veda :ref:`registry:Content Negotiation and Signed Representation`).

**Taxonomy Objectives:**

1. **Fondamento semantico**: Stabilire un vocabolario standardizzato per i domain e i purpose nell'ecosistema
2. **Framework di policy**: Abilitare decisioni di autorizzazione strutturate basate sulla classificazione gerarchica
3. **Interoperabilità**: Assicurare un'interpretazione coerente delle classificazioni delle Credenziali
4. **Estensibilità**: Supportare l'evoluzione dell'ecosistema con nuovi Domain, Class, tipi di Credenziale e Purpose
5. **Conformità transfrontaliera**: Allinearsi ai requisiti regolamentari UE e agli standard internazionali


Taxonomy Usage
^^^^^^^^^^^^^^

- **Authentic Source Registry**: Le Fonti Autentiche dichiarano le capacità utilizzando le classificazioni della taxonomy
- **Digital Credentials Catalog**: I tipi di Credenziale specificano Domain, Class e Purpose
- **Policy di autorizzazione**: La valutazione delle policy sfrutta la struttura della taxonomy per le decisioni di controllo degli accessi


Digital Credentials Hierarchy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gli Attestati Elettronici riconosciuti all'interno dell'ecosistema IT-Wallet sono classificati e standardizzati secondo il seguente modello gerarchico a più livelli, progettato per migliorare la chiarezza semantica, la discovery delle Credenziali e la compatibilità sia con i workflow di verifica specifici della Credenziale sia con quelli basati sui claim.

La gerarchia è definita come segue:

**Domain**

Un **Domain** rappresenta un'area tematica di alto livello che raggruppa famiglie di Credenziali relative allo stesso contesto ampio (ad es., Identity, Health, Education, Mobility).
I Domain forniscono uno strato organizzativo di primo livello.

**Credential Class**

Una **Credential Class** rappresenta una famiglia di Credenziali che condividono natura, funzione o struttura simili (ad es., Identification Documents, Civil Status Certificates).

Ciascuna Class DOVREBBE definire:

- un identificativo di Class stabile (URI),
- la semantica attesa della Credential Family.

Le Class consentono alle Relying Party e alle Soluzioni Wallet di richiedere o abbinare Credenziali in base alla loro categoria di tipo.

**Credential Type**

Un **Credential Type** rappresenta una Credenziale specifica all'interno di una Class (ad es. Digital Travel Credential, Birth Certificate, Mobile Driving License).
Ciascun Credential Type DEVE includere:

- un identificativo univoco,
- l'identificativo del Credential Issuer,
- l'insieme di Attributi che possono essere inclusi nelle presentazioni.

I Credential Type consentono un targeting preciso per i flussi di verifica guidati dalla conformità o imposti dalla regolamentazione.

**Purpose (Verification Intent)**

Un **Purpose (Verification Intent)** descrive *perché* una Credenziale può essere richiesta da una Relying Party (ad es., Identity Verification, Age Verification, Eligibility for specific services).
I Purpose DEVONO descrivere **esiti di verifica**.
Ciascun Credential Type DEVE dichiarare il proprio Domain, la propria Class e i Purpose supportati.

Le tabelle seguenti forniscono esempi non esaustivi che illustrano le relazioni tra Domain, Credential Class e Credential Type, seguiti dalla loro mappatura sui Purpose di verifica.
Domain, Class, Credenziali specifiche e Purpose di verifica aggiuntivi **POSSONO** essere aggiunti nel tempo con l'evoluzione dell'ecosistema IT-Wallet.

.. list-table:: Digital Credential Taxonomy: Hierarchy and Classification
   :class: longtable
   :header-rows: 1
   :widths: 15 25 30 30

   * - **Domain**
     - **Description**
     - **Credential Class**
     - **Credential Type**

   * - *IDENTITY*
     - Credenziali che instaurano o confermano l'identità legale di una persona e lo stato personale, civile o giuridico.
     -
       * Identification Documents
       * Civil Registry and Personal Status Certificates
       * Economic and Legal Status
     -
       * Digital Travel Credential
       * Mobile Driving License (Italy only)
       * Tax Code / Health Insurance Card
       * Age Certification
       * Birth Certificate
       * Residence Certificate
       * Family Status Certificate
       * Marriage Certificate
       * Citizenship Certificate
       * ISEE (Equivalent Economic Situation Indicator)
       * Residence Permit
       * Certificate of Pending Charges
       * Criminal Record Certificate

   * - *HOME AND FAMILY*
     - Credenziali che attestano la composizione del nucleo familiare, la residenza e i rapporti giuridici o fiscali relativi all'abitazione.
     -
       * Property and Cadastral Documents
       * Family Documents
       * Local Tax Documents
     -
       * Deed of Sale
       * Cadastral Survey
       * Cadastral Floor Plan
       * Cadastral Certificate
       * Children's Tax Code / Health Card
       * Birth Certificate
       * Family Status Certificate
       * IMU (Property Tax)
       * TARI (Waste Tax)

   * - *EDUCATION*
     - Credenziali che attestano i risultati formativi, i titoli accademici e la formazione professionale.
     -
       * Educational Qualifications
       * Professional Certifications
     -
       * Lower Secondary School Diploma
       * Upper Secondary School Diploma
       * Bachelor's Degree
       * Master's Degree
       * University Master
       * PhD
       * Professional Licenses (e.g. architect, lawyer)
       * Vocational Training Certificates
       * Language Certifications (e.g. IELTS)
       * Academic Qualifications (e.g. Europass)

   * - *HEALTH*
     - Credenziali relative alla copertura sanitaria, allo stato medico e alle certificazioni sanitarie.
     -
       * Certifications and Eligibility
       * Medical Records
     -
       * Health Insurance Card (TEAM)
       * European Health Card (CED)
       * Disability Certificate
       * Vaccination Certificate
       * Sports Fitness Certificate
       * Work Fitness Certificate
       * Medical Prescriptions
       * Digital Medical Report

   * - *FINANCIAL*
     - Credenziali relative agli strumenti di pagamento, alle autorizzazioni finanziarie e alla prova dei pagamenti.
     -
       * Payment Instruments
       * Payment Credentials and Authorisations
       * Public Payments and Fees
       * Recurring Payments and Subscriptions
     -
       * Digital Payment Card (debit / credit / prepaid)
       * Virtual Card
       * Bank Account (IBAN)
       * Strong Customer Authentication (SCA) Credential
       * Payment Receipt
       * Digital Stamp Duty (Bollo digitale)
       * Tax and Fee Payment Certificate
       * Subscription Mandate
       * Recurring Payment Credential

   * - *CULTURE AND LEISURE*
     - Credenziali che attestano l'appartenenza, l'affiliazione o la partecipazione a programmi culturali o ricreativi.
     -
       * Cultural Cards and Benefits
       * Membership and Loyalty Programs
     -
       * Culture Card
       * Annual Museum Passes
       * Cinema Card
       * Museum Card
       * Association Membership Cards
       * Library Card
       * City Pass

   * - *EMPLOYMENT*
     - Credenziali che attestano i rapporti di lavoro, lo stato professionale e i contributi.
     -
       * Employment Documents
       * Employment Status
       * Employment Affiliation
     -
       * Digital Employment Contract
       * Curriculum Vitae (CV)
       * Residence Permit
       * Employment Status Certificate
       * INPS Contribution Record
       * Physical Access Badge

   * - *MOBILITY AND TRAVEL*
     - Credenziali che attestano i diritti di mobilità, lo stato relativo al veicolo e i diritti connessi al viaggio.
     -
       * Licenses and Authorizations
       * Vehicle Documents
       * Transport Subscriptions
       * Travel Documents
       * Travel Insurance
       * Bookings
       * Discounts and Benefits
     -
       * Mobile Driving License
       * Boating License
       * Vehicle Registration Certificate
       * Digital RCA Insurance
       * Vehicle Inspection Certificate
       * Green Card / International Insurance
       * Public Transport Pass
       * Road Charging Subscription
       * Digital Travel Credential
       * Travel Tickets (air, train, etc.)
       * Travel Insurance Policy
       * Hotel Reservation
       * Discount Cards
       * Tourist Benefits

   * - *BONUSES*
     - Credenziali che attestano il diritto a benefici economici, incentivi o voucher.
     -
       * Economic Benefits and Allowances
       * Incentives and Vouchers
       * Health and Wellbeing Bonuses
     -
       * Family Allowance Credential
       * Unemployment Benefit Credential
       * Digital Voucher
       * Purchase Incentive Credential
       * Cashback Eligibility Credential
       * Healthcare Bonus Credential
       * Mental Health Support Voucher
       * Sports and Physical Activity Bonus

.. list-table:: Mapping between Credential Classes and Purposes
   :class: longtable
   :header-rows: 1
   :widths: 40 60

   * - **Credential Class**
     - **Supported Purposes**

   * - Identification Documents
     -
       * Identity verification
       * Age verification
       * Person identification
   * - Civil Registry and Personal Status Certificates
     -
       * Civil status verification
       * Right of residence
       * Household composition verification
   * - Economic and Legal Status
     -
       * Eligibility for services or benefits
       * Legal status verification
       * Criminal record check
   * - Property and Cadastral Documents
     -
       * Residence and household verification
       * Property ownership verification
       * Real estate compliance
   * - Family Documents
     -
       * Household composition verification
       * Eligibility for family-based social services
   * - Local Tax Documents
     -
       * Compliance with local tax obligations
       * Verification of property tax status
   * - Educational Qualifications
     -
       * Qualification and degree verification
       * Eligibility for education pathways
   * - Professional Certifications
     -
       * Professional license verification
       * Skills assessment for work
   * - Certifications and Eligibility
     -
       * Verification of vaccination status
       * Verification of fitness status
       * Access to health-restricted areas
   * - Medical Records
     -
       * Access to healthcare services
       * Sharing of medical records
       * Medical history validation
   * - Payment Instruments
     -
       * Payment authorization
       * Payment execution
       * Proof of payment
   * - Payment Credentials and Authorisations
     -
       * Management of financial authorizations
       * Strong Customer Authentication (SCA)
   * - Public Payments and Fees
     -
       * Proof of tax payment
       * Proof of fee payment
       * Digital stamp duty validation
   * - Recurring Payments and Subscriptions
     -
       * Management of recurring payments
       * Subscription mandate verification
   * - Cultural Cards and Benefits
     -
       * Access to cultural services
       * Access to leisure services
       * Application of member discounts
   * - Membership and Loyalty Programs
     -
       * Verification of affiliation
       * Verification of participation
       * Use of loyalty benefits
   * - Employment Documents
     -
       * Employment status verification
       * Professional profile validation
   * - Employment Status
     -
       * Verification of contribution records
       * Eligibility for employment-related benefits
   * - Licenses and Authorizations
     -
       * Driving rights verification
       * Navigation rights verification
       * Law enforcement controls
   * - Vehicle Documents
     -
       * Vehicle registration verification
       * Vehicle inspection verification
       * Insurance status check
   * - Transport Subscriptions
     -
       * Access to transport services
       * Public transport pass verification
   * - Travel Documents
     -
       * Right to travel or circulate
       * Cross-border mobility identity check
   * - Travel Insurance and Bookings
     -
       * Verification of travel insurance coverage
       * Accommodation reservation check
       * Transport reservation check
   * - Discounts and Benefits
     -
       * Application of member discounts
       * Access to tourist benefits
   * - Economic Benefits and Allowances
     -
       * Eligibility verification for family benefits
       * Eligibility verification for unemployment benefits
       * Allocation of economic support
   * - Incentives and Vouchers
     -
       * Use of digital vouchers
       * Use of purchase incentives
       * Cashback eligibility verification
   * - Health and Wellbeing Bonuses
     -
       * Access to healthcare bonuses
       * Use of mental health vouchers
       * Use of sports vouchers
   * - Employment Affiliation
     -
       * Access permit verification

Ciascuna Credenziale DEVE specificare domain, class e purpose per abilitare sia gli **scenari specifici della Credenziale** sia gli **scenari agnostici rispetto alla Credenziale** secondo i requisiti della Relying Party e i pattern di richiesta di presentazione, come definito nelle tabelle di mappatura precedenti.

  1. **Scenari specifici della Credenziale** (primari per i settori governativi/regolamentati): le RP richiedono tipi di Credenziale specifici per requisiti di conformità e audit, inclusi ad esempio:

    - **Servizi governativi**: ``"credential_type":"pid"`` per la verifica di identità specifica del PID o ``"credential_type":"eid"`` per la verifica di identità specifica dell'IT-Wallet ID.
    - **Controlli di polizia**: ``"credential_type":"mDL"`` per la verifica della patente di guida.
    - **KYC bancario**: tipi di Credenziale specifici imposti dalla regolamentazione finanziaria.
    - **Servizi sanitari**: ``"credential_type":"european_disability_card"`` per l'accesso ai benefici di disabilità conformi all'UE.

  2. **Scenari agnostici rispetto alla Credenziale** (tipici per le attività private): le RP richiedono claim specifici indipendentemente dalla fonte della Credenziale per l'efficienza operativa, quali:

    - **Consegna e-commerce**: qualsiasi Credenziale, tra quelle a cui è autorizzato ad accedere, contenente ``given_name``, ``family_name``, ``address`` per la spedizione.
    - **Abbonamenti**: qualsiasi Credenziale, tra quelle a cui è autorizzato ad accedere, con ``given_name``, ``email`` per la personalizzazione.
    - **Personalizzazione del servizio**: applicazioni business che richiedono dati personali di base senza requisiti stringenti sulla fonte.

Questo approccio consente:

  - **Autorizzazione basata su policy** utilizzando le mappature **Domain / Class / Credential Type / Purpose**.
  - **Registrazione flessibile delle RP** a supporto sia delle esigenze di conformità governativa sia dei requisiti operativi business.

Taxonomy Structure
^^^^^^^^^^^^^^^^^^

La taxonomy mantiene una struttura gerarchica a quattro livelli, ossia i Domain, le Class, i Credential Type e i Purpose definiti in :ref:`registry:Digital Credentials Hierarchy` sopra.

.. note::
  Il Credential Type è un concetto definito a livello di Digital Credentials Catalog, non all'interno della Taxonomy. La Taxonomy fornisce il vocabolario di classificazione (Domain, Class, Purpose) che i Credential Type nel Catalog referenziano.

**Supporto alla localizzazione:**

La taxonomy supporta ambienti multilingue tramite il pattern di suffisso ``_l10n_id``, consentendo una gestione efficiente della localizzazione per le interfacce utente e le implementazioni transfrontaliere.


**Struttura JSON della Taxonomy:**

.. list-table:: First-level Fields of the Taxonomy
   :class: longtable
   :widths: 30 70
   :header-rows: 1

   * - **Field Name**
     - **Description**
   * - **id**
     - OBBLIGATORIO. Identificativo univoco della Taxonomy (ad es., ``urn:taxonomy:it-wallet``).
   * - **version**
     - OBBLIGATORIO. La versione della Taxonomy (ad es., ``1.0.0``).
   * - **last_modified**
     - OBBLIGATORIO. Il timestamp che indica quando l'elenco è stato aggiornato l'ultima volta (ad es., ``2025-03-15T12:00:00Z``).
   * - **name_l10n_id**
     - OBBLIGATORIO. Chiave di localizzazione che referenzia il nome leggibile della Taxonomy (ad es., ``taxonomy.name``).
   * - **description_l10n_id**
     - OBBLIGATORIO. Chiave di localizzazione che referenzia la descrizione leggibile della Taxonomy (ad es., ``taxonomy.description``).
   * - **localization**
     - OBBLIGATORIO. Oggetto di configurazione della localizzazione contenente:

       * **default_locale**: Codice locale predefinito (ad es., ``it``).
       * **available_locales**: Array dei codici locale supportati (ad es., ``["en", "it"]``).
       * **base_uri**: URI di base per il recupero dei bundle di localizzazione (ad es., ``https://trust-registry.eid-wallet.example.it/.well-known/l10n/taxonomy/``).
       * **version**: Versione del formato del bundle di localizzazione.
   * - **domains**
     - OBBLIGATORIO. Array di oggetti Domain, ciascuno contenente:

       * **id**: Identificativo univoco del Domain in SCREAMING_SNAKE_CASE (ad es., ``IDENTITY``).
       * **name_l10n_id**: Chiave di localizzazione per il nome del domain (ad es., ``domain.identity.name``).
       * **description_l10n_id**: Chiave di localizzazione per la descrizione del domain (ad es., ``domain.identity.description``).
       * **classes**: Array di oggetti Class. Ciascuna class contiene ``id``, ``name_l10n_id`` e ``supported_purposes`` (array di stringhe ID di purpose).
   * - **purposes**
     - OBBLIGATORIO. Array piatto di tutti gli oggetti Purpose definiti nella taxonomy, ciascuno contenente:

       * **id**: Identificativo univoco del Purpose in SCREAMING_SNAKE_CASE (ad es., ``IDENTITY_VERIFICATION``, ``ACCESS_PERMIT``).
       * **name_l10n_id**: Chiave di localizzazione per il nome del purpose (ad es., ``purpose.identity_verification.name``).

Di seguito è fornito un esempio non normativo della struttura della Taxonomy:

.. literalinclude:: ../../examples/taxonomy-example.json
  :language: JSON

.. note::
  Per una gestione migliore e più efficiente della localizzazione della Taxonomy, un'Entità che la consulta DOVREBBE:

  - Scaricare la versione di base della Taxonomy (compatta, senza localizzazioni) utilizzando l'endpoint ``.well-known/taxonomy``.
  - Determinare la lingua preferita dell'Utente.
  - Scaricare solo i bundle di localizzazione necessari.
  - Unire dinamicamente il contenuto localizzato con la struttura della Taxonomy.

Di seguito è fornito un esempio non normativo dell'output di un bundle di localizzazione:

.. code-block:: json

  {
    "taxonomy.name": "IT-Wallet Taxonomy",
    "taxonomy.description": "Hierarchical classification system for Digital Credentials in the IT-Wallet ecosystem",
    "domain.identity.name": "Identity",
    "domain.identity.description": "Credentials that establish or confirm a person's legal identity and personal, civil or legal status.",
    "class.identification_documents.name": "Identification Documents",
    "purpose.identity_verification.name": "Identity verification",
    "domain.authentication.name": "Authentication",
    "domain.authentication.description": "Credentials that attest authorisation to access restricted physical or digital spaces, services or resources.",
    "class.access.name": "Access",
    "purpose.access_permit.name": "Access permit verification",
    "...": "..."
  }

I bundle di localizzazione DEVONO essere disponibili all'URI composto concatenando il codice locale e ``.json`` al valore ``localization.base_uri`` definito nella taxonomy. Ciascun bundle di locale DEVE essere accessibile seguendo il pattern di naming **{locale_code}.json**, dove **{locale_code}** è sostituito con il corrispondente codice locale dell'array **available_locales**.

Un esempio non normativo dell'URI di localizzazione italiana per il bundle sarebbe **https://trust-registry.eid-wallet.example.it/.well-known/l10n/taxonomy/it.json**.

Claims Registry
---------------

L'URL dell'endpoint Claims Registry è pubblicato sotto la chiave ``claims_registry`` del documento Registry Discovery. L'endpoint supporta la content negotiation e la rappresentazione firmata comuni a tutti gli endpoint della Registry Infrastructure (si veda :ref:`registry:Content Negotiation and Signed Representation`).

Il Claims Registry DEVE contenere:

  - **Claim standardizzati**: Definizioni semantiche per tutti gli attributi delle Credenziali con tipi di dato e regole di validazione.
  - **Mapping di interoperabilità**: Definizioni di alias per i claim che utilizzano una terminologia diversa tra gli standard (ad es., ISO18013-5 ``place_of_birth`` mappato sul canonico ``birth_place``).
  - **Formati di dati**: Tipi di dato standardizzati (string, date, numeric, boolean, email, url, image, array, object) con pattern di validazione.

Il Claims Registry DEVE assicurare:

  - **Coerenza semantica**: Previene i conflitti tra claim duplicati o sovrapposti nell'ecosistema.
  - **Interoperabilità transfrontaliera**: Assicura la conformità UE e un'interpretazione coerente dei claim.
  - **Validazione dello schema**: Fornisce definizioni autorevoli per la validazione dei claim in tutti gli scenari di Credenziale.
  - **Allineamento regolamentare**: Si coordina con il quadro regolamentare nazionale e UE.
  - **Scenari agnostici rispetto alla Credenziale**: Supporta gli scenari in cui la **convenienza dell'utente** e l'**efficienza operativa business** sono prioritarie rispetto alla **conformità regolamentare** e alle **piste di audit**.

.. note::
  Il Claims Registry definisce le proprietà semantiche dei singoli attributi, ma NON DEVE specificare le capacità di selective disclosure. La selective disclosure dipende dalle implementazioni del formato della Credenziale (SD-JWT, mDocs), dalle configurazioni tecniche dell'issuer e dal contesto di presentazione. Queste capacità sono specificate a livello di tipo di Credenziale all'interno del Digital Credentials Catalog e implementate durante i flussi di presentazione delle Credenziali.

Claims Registry Usage
^^^^^^^^^^^^^^^^^^^^^

Come mostrato nella Figura :ref:`fig_registry_infrastructure` e nella Figura :ref:`fig_registry_discovery`, il Claims Registry DEVE supportare l'intero ciclo di vita dell'ecosistema:

**Durante il processo di Onboarding**:

  - **Registrazione AS**: Le Fonti Autentiche dichiarano i claim disponibili dal registro standardizzato durante la registrazione delle capacità.
  - **Registrazione CI**: I Credential Issuer selezionano le entità Fonte Autentica in base ai claim richiesti. I tipi di Credenziale che utilizzano tali claim sono registrati nel catalogo dall'Attestation Scheme Provider, si veda :ref:`onboarding-system:Credential Type Registration`.
  - **Registrazione RP**: Le Relying Party specificano i requisiti di autorizzazione utilizzando domain/purpose per attributi specifici dell'Utente.

**Durante le attività operative**:

  - **Emissione delle Credenziali**: Le definizioni dei claim assicurano una rappresentazione coerente dei dati tra tipi di Credenziale diversi.
  - **Richieste di presentazione**: Le Relying Party referenziano i claim per la validazione dello schema e la verifica dell'autorizzazione sia negli scenari specifici della Credenziale sia in quelli agnostici rispetto alla Credenziale.

Claims Registry Structure
^^^^^^^^^^^^^^^^^^^^^^^^^

Il Claims Registry mantiene definizioni tecniche language-neutral per la coerenza semantica nell'ecosistema. Le localizzazioni rivolte all'utente per i nomi e le descrizioni dei claim sono fornite tramite bundle di localizzazione dedicati referenziati tramite il campo ``localization.base_uri``, consentendo un supporto multilingue efficiente senza compromettere l'integrità strutturale del registro.

.. list-table:: First-level Fields of the Claims Registry
   :class: longtable
   :widths: 30 70
   :header-rows: 1

   * - **Field Name**
     - **Description**
   * - **id**
     - OBBLIGATORIO. Identificativo univoco del Claims Registry (ad es., ``urn:claims:it-wallet``).
   * - **version**
     - OBBLIGATORIO. La versione del Claims Registry (ad es., ``1.0.0``).
   * - **last_modified**
     - OBBLIGATORIO. Il timestamp che indica quando l'elenco è stato aggiornato l'ultima volta (ad es., ``2025-03-15T12:00:00Z``).
   * - **localization**
     - OBBLIGATORIO. Oggetto di configurazione della localizzazione contenente:

       * **default_locale**: Codice locale predefinito (ad es., ``it``).
       * **available_locales**: Array dei codici locale supportati (ad es., ``["en", "it"]``).
       * **base_uri**: URI di base per il recupero dei bundle di localizzazione (ad es., ``https://trust-registry.eid-wallet.example.it/.well-known/l10n/claims/``).
       * **version**: Versione del formato del bundle di localizzazione.
   * - **claims**
     - OBBLIGATORIO. Un oggetto JSON in cui ciascuna chiave è un nome di claim e ciascun valore è un oggetto JSON che descrive tale claim. Ciascun oggetto claim contiene i parametri definiti nella tabella "Claim Entry Parameters" seguente.

.. list-table:: Claim Entry Parameters
   :class: longtable
   :widths: 30 70
   :header-rows: 1

   * - **Field Name**
     - **Description**
   * - **description_l10n_id**
     - OBBLIGATORIO. Chiave di localizzazione che referenzia la descrizione leggibile del claim nel bundle di localizzazione (ad es., ``claim.given_name.description``).
   * - **type**
     - OBBLIGATORIO. Tipo di dato del claim. Valori supportati: ``string``, ``boolean``, ``array``, ``object``.
   * - **format**
     - OPZIONALE. Qualificatore di formato semantico per i tipi string (ad es., ``date`` per le date ISO 8601, ``uri``, ``data`` per il binario codificato in Base64).
   * - **encoding**
     - OPZIONALE. Encoding applicato al valore (ad es., ``base64``). Presente quando ``format`` è ``data``.
   * - **aliases**
     - OPZIONALE. Array di nomi di claim alternativi utilizzati in altri standard che mappano su questo claim canonico (ad es., ``["birthdate"]`` per ``birth_date``, ``["date_of_expiry"]`` per ``expiry_date``).
   * - **nested_claims**
     - OPZIONALE. Array di nomi di claim che formano le proprietà di un claim di tipo ``object`` (ad es., ``["country", "locality", "region"]`` per ``place_of_birth``).
   * - **nested_item_claims**
     - OPZIONALE. Array di nomi di claim che rappresentano le proprietà di ciascun elemento in un claim di tipo ``array`` (ad es., ``["vehicle_category_code", "issue_date", "expiry_date", "codes"]`` per ``driving_privileges``).
   * - **items**
     - OPZIONALE. Oggetto JSON che descrive lo schema di ciascun elemento in un claim di tipo ``array`` semplice (ad es., ``{"type": "string"}`` per ``nationalities``).

Di seguito è fornito un esempio non normativo della struttura del Claims Registry:

.. literalinclude:: ../../examples/claims-registry-example.json
  :language: JSON

.. note::
  Per una gestione migliore e più efficiente della localizzazione delle informazioni contenute nel Claims Registry, un'Entità che lo consulta DOVREBBE:

  - Scaricare la versione di base del Claims Registry (compatta, senza localizzazioni) utilizzando l'endpoint ``.well-known/claims``.
  - Determinare la lingua preferita dell'Utente.
  - Scaricare solo i bundle di localizzazione necessari.
  - Unire dinamicamente il contenuto localizzato con la struttura del Claims Registry.

Di seguito è fornito un esempio non normativo dell'output di un bundle di localizzazione:

.. code-block:: json

  {
    "claim.given_name.description": "Person's given name(s) as they appear on official documents.",
    "claim.birth_date.description": "Date of birth, in ISO 8601 format (YYYY-MM-DD). Also known as birthdate.",
    "claim.driving_privileges.description": "Array of authorized vehicle categories with details.",
    "...": "..."
  }

I bundle di localizzazione DEVONO essere disponibili all'URI composto concatenando il codice locale e ``.json`` al valore ``localization.base_uri`` (ad es., ``https://trust-registry.eid-wallet.example.it/.well-known/l10n/claims/it.json``).

Authentic Source Registry
-------------------------

L'URL dell'endpoint Authentic Source Registry è pubblicato sotto la chiave ``authentic_sources`` del documento Registry Discovery. L'endpoint supporta la content negotiation e la rappresentazione firmata comuni a tutti gli endpoint della Registry Infrastructure (si veda :ref:`registry:Content Negotiation and Signed Representation`).

L'Authentic Source Registry DEVE contenere almeno:

  - **Informazioni sull'organizzazione**: Dettagli della persona giuridica, status regolamentare e ruolo autorevole all'interno di domain specifici.
  - **Capacità dati**: Disponibilità dei claim dichiarati con riferimento alle definizioni standardizzate del Claims Registry con le corrispondenti classificazioni della Taxonomy.
  - **Metodi di integrazione**: Meccanismi tecnici di accesso (PDND).
  - **Scopi previsti**: Tipi di Credenziale supportati e contesti business per il coordinamento AS-CI.
  - **Assicurazione della qualità dei dati**: Status autorevole, frequenza di aggiornamento e capacità di pista di audit.

L'Authentic Source Registry DEVE assicurare:

  - **Accesso coordinato ai dati**: Consente al CI la discovery dei dati appropriati dalle Fonti Autentiche per l'emissione delle Credenziali.
  - **Integrazione AS-CI**: Gli endpoint tecnici e i metodi di accesso consentono una comunicazione AS-CI standardizzata. Facilita i workflow di approvazione e il coordinamento dell'accesso ai dati tra le entità.
  - **Conformità regolamentare**: Supporta i requisiti di trasparenza della pubblica amministrazione e di coordinamento del settore privato.

.. note::
   L'Authentic Source Registry è un registro pubblico che fornisce al Credential Issuer indicazioni per il provisioning delle Credenziali.

Authentic Source Registry Usage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Come mostrato nella Figura :ref:`fig_registry_infrastructure` e nella Figura :ref:`fig_registry_discovery`, l'Authentic Source Registry supporta il coordinamento dell'ecosistema durante l'intero ciclo di vita operativo:

**Durante il processo di Onboarding**:
  - **Auto-dichiarazione AS**: Le Fonti Autentiche registrano le capacità prima che esistano tipi di Credenziale nel catalogo.
  - **Discovery CI**: I Credential Issuer cercano entità Fonte Autentica in base ai claim richiesti e ai tipi di Credenziale previsti.

**Durante le attività operative**:
  - **Emissione delle Credenziali**: I sistemi del Credential Issuer referenziano l'Authentic Source Registry per l'accesso ai dati in tempo reale durante l'emissione delle Credenziali.

Authentic Source Registry Structure
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Durante la registrazione, le Fonti Autentiche dichiarano le proprie capacità prima che esistano tipi di Credenziale nel catalogo. Questa dichiarazione costituisce il fondamento per la successiva registrazione dei CI e la creazione dei tipi di Credenziale.

**Schema dell'identificativo univoco della Fonte Autentica**

A ciascuna Fonte Autentica DEVE essere assegnato un identificativo univoco che segue lo schema URL HTTPS definito di seguito. Questo identificativo è utilizzato per referenziare le entità AS nel sistema di registro e nel Digital Credentials Catalog, assicurando coerenza con i pattern di identificazione delle entità OpenID Federation.

*Schema dell'identificativo AS:*

.. code-block:: text

  https://{organization_domain}[/{optional_path}]

*Componenti dello schema:*

- **organization_domain**: Dominio DNS controllato dall'organizzazione
- **optional_path**: Componente di path aggiuntivo per servizi o dipartimenti specifici

L'identificativo AS DEVE seguire queste regole normative:

1. **Protocollo HTTPS**: DEVE utilizzare lo schema HTTPS per la verifica di sicurezza e trust
2. **Titolarità del dominio**: L'organizzazione DEVE controllare il dominio DNS utilizzato nell'identificativo
3. **Univocità**: Garantita tramite l'univocità del namespace DNS
4. **Stabilità**: DOVREBBE rimanere stabile nel tempo per evitare la rottura dei riferimenti
5. **Risolvibilità**: L'URL DOVREBBE essere risolvibile (sebbene non sia richiesto che serva contenuto)

*Esempi di identificativi AS conformi:*

- ``https://motorizzazione.gov.example``: Pubblico - Ministero dei Trasporti, Dip. Motorizzazione
- ``https://registry.anpr.example``: Pubblico - Anagrafe Nazionale della Popolazione Residente
- ``https://api.bank.example/auth-source``: Privato - Servizi finanziari Banca Esempio

**Parametri dell'Authentic Source Registry**

L'Authentic Source Registry DEVE contenere i seguenti parametri per ciascuna Fonte Autentica registrata:

.. list-table:: First-level Fields of the Authentic Source Registry
   :class: longtable
   :widths: 30 70
   :header-rows: 1

   * - **Field Name**
     - **Description**
   * - **id**
     - OBBLIGATORIO. Identificativo univoco dell'Authentic Source Registry (ad es., ``urn:authentic-sources:it-wallet``).
   * - **version**
     - OBBLIGATORIO. La versione dell'Authentic Source Registry (ad es., ``1.0.0``).
   * - **last_modified**
     - OBBLIGATORIO. Il timestamp che indica quando l'elenco è stato aggiornato l'ultima volta (ad es., ``2025-03-15T12:00:00Z``).
   * - **localization**
     - OBBLIGATORIO. Oggetto di configurazione della localizzazione contenente:

       * **default_locale**: Codice locale predefinito (ad es., ``it``).
       * **available_locales**: Array dei codici locale supportati (ad es., ``["en", "it"]``).
       * **base_uri**: URI di base per il recupero dei bundle di localizzazione (ad es., ``https://trust-registry.eid-wallet.example.it/.well-known/l10n/authentic-sources/``).
       * **version**: Versione del formato del bundle di localizzazione.
   * - **authentic_sources**
     - OBBLIGATORIO. Un array JSON in cui ciascuna voce è un oggetto JSON che rappresenta un'entità Fonte Autentica. Ciascun oggetto contiene i parametri definiti nella tabella "Authentic Sources Parameters" seguente, compresi identificazione dell'entità, informazioni organizzative, capacità dati e metodi di integrazione.

.. list-table:: Authentic Sources Parameters
   :class: longtable
   :widths: 25 15 60
   :header-rows: 1

   * - **Parameter**
     - **Type**
     - **Description**
   * - **entity_id**
     - string
     - OBBLIGATORIO. Identificativo univoco che segue lo schema normativo: ``https://{organization_domain}[/{optional_path}]``.
   * - **organization_info**
     - JSON object
     - OBBLIGATORIO. Dettagli della persona giuridica e metadata organizzativi.
   * - **organization_info.organization_name_l10n_id**
     - string
     - OBBLIGATORIO. Chiave di localizzazione che referenzia il nome localizzato dell'organizzazione nel bundle di localizzazione (ad es., ``authentic_source1.name``).
   * - **organization_info.organization_type**
     - string
     - OBBLIGATORIO. Classificazione dell'entità: ``"public"`` o ``"private"``.
   * - **organization_info.ipa_code**
     - string
     - OBBLIGATORIO solo per AS pubbliche. Codice di registrazione IPA per le entità governative.
   * - **organization_info.legal_identifier**
     - string
     - OBBLIGATORIO. Identificativo di registrazione legale (Codice Fiscale/Partita IVA, o identificativo nazionale equivalente per le entità estere).
   * - **organization_info.homepage_uri**
     - string
     - OBBLIGATORIO. URL che punta alla homepage dell'organizzazione.
   * - **organization_info.contacts**
     - String Array
     - OBBLIGATORIO. Array di indirizzi e-mail di contatto per almeno un supporto utente, un'applicazione e uno specialista di sistemi.
   * - **organization_info.dpa_contact**
     - string
     - OBBLIGATORIO. Un indirizzo e-mail del DPA della Fonte Autentica.
   * - **organization_info.policy_uri**
     - string
     - OBBLIGATORIO. URL del documento di informativa sulla privacy.
   * - **organization_info.tos_uri**
     - string
     - OPZIONALE. URL del documento dei termini di servizio.
   * - **organization_info.organization_country**
     - string
     - OBBLIGATORIO. Codice paese ISO 3166-1 alpha-2 a due lettere dell'organizzazione.
   * - **organization_info.logo_uri**
     - string
     - OPZIONALE. URL dell'immagine del logo dell'organizzazione.
   * - **organization_info.logo_uri#integrity**
     - string
     - CONDIZIONALE. Digest crittografico della risorsa immagine del logo per la verifica di integrità. OBBLIGATORIO se ``logo_uri`` è presente. Formato: ``{digest_method}-{digest_value}`` (ad es., ``"sha-256-abc123..."``).
   * - **organization_info.logo_alt_text_l10n_id**
     - string
     - OPZIONALE. Testo alternativo per l'immagine del logo dell'organizzazione.
   * - **organization_info.logo_extended_uri**
     - string
     - OPZIONALE. URL dell'immagine del logo esteso dell'organizzazione.
   * - **organization_info.logo_extended_uri#integrity**
     - string
     - CONDIZIONALE. Digest crittografico della risorsa immagine del logo esteso per la verifica di integrità. OBBLIGATORIO se ``logo_extended_uri`` è presente. Formato: ``{digest_method}-{digest_value}`` (ad es., ``"sha-256-abc123..."``).
   * - **organization_info.logo_extended_alt_text_l10n_id**
     - string
     - OPZIONALE. Testo alternativo per l'immagine del logo esteso dell'organizzazione.
   * - **data_capabilities**
     - JSON Objects Array
     - OBBLIGATORIO. Array contenente le specifiche delle capacità dati.
   * - **data_capabilities[].dataset_id**
     - string
     - OBBLIGATORIO. Il :term:`Dataset_id` nell'ambito della Fonte Autentica, che PUÒ essere utilizzato come parametro di query per il servizio ``GetAttributeClaims``.
   * - **data_capabilities[].data_origin_l10n_id**
     - string
     - OBBLIGATORIO. Chiave di localizzazione che referenzia il nome leggibile dell'origine dei dati o del dipartimento che fornisce i dati (ad es., ``authentic_source1.dataset1.origin``).
   * - **data_capabilities[].intended_purposes**
     - String Array
     - OBBLIGATORIO. Scopi business serviti, utilizzando gli identificativi di purpose della taxonomy (ad es., ``["IDENTITY_VERIFICATION", "DRIVING_RIGHTS_VERIFICATION"]``).
   * - **data_capabilities[].available_claims**
     - String Array
     - OBBLIGATORIO. Claim disponibili da questa capacità dati.
   * - **data_capabilities[].available_claims.claim_name**
     - string
     - OBBLIGATORIO. Contiene il nome del claim.
   * - **data_capabilities[].available_claims.order**
     - number
     - OBBLIGATORIO. Definisce l'ordine in cui le informazioni sarebbero mostrate.
   * - **data_capabilities[].available_claims.mandatory**
     - boolean
     - OBBLIGATORIO. Definisce se un claim è sempre disponibile o meno.
   * - **data_capabilities[].integration_method**
     - string
     - OBBLIGATORIO. Framework di autorizzazione utilizzato per l'accesso ai dati. DEVE essere ``"pdnd"``.
   * - **data_capabilities[].integration_endpoint**
     - string
     - OPZIONALE. Punto di accesso al servizio (endpoint PDND).
   * - **data_capabilities[].api_specification**
     - string
     - OPZIONALE. URL del documento di specifica `OAS3`_ per questa capacità dati.
   * - **data_capabilities[].data_provision**
     - JSON object
     - OPZIONALE. Capacità di fornitura dei dati e specifiche di tempistica.
   * - **data_capabilities[].data_provision.immediate_flow**
     - boolean
     - OBBLIGATORIO. Indica se la Fonte Autentica supporta la fornitura immediata dei dati.
   * - **data_capabilities[].data_provision.deferred_flow**
     - boolean
     - OBBLIGATORIO. Indica se la Fonte Autentica supporta la fornitura differita dei dati.
   * - **data_capabilities[].data_provision.max_response_time_minutes**
     - integer
     - CONDIZIONALE. Tempo massimo in minuti per la Fonte Autentica per rispondere a una richiesta di fornitura dati differita. OBBLIGATORIO se ``deferred_flow`` è ``true``.
   * - **data_capabilities[].data_provision.notification_methods**
     - String Array
     - CONDIZIONALE. Array dei metodi di notifica supportati dalla Fonte Autentica per la fornitura dati differita, quali ``"push"``, ``"poll"``. OBBLIGATORIO se ``deferred_flow`` è ``true``.
   * - **data_capabilities[].user_information_l10n_id**
     - string
     - OPZIONALE. Chiave di localizzazione che referenzia una stringa formattata in Markdown con informazioni leggibili sulla capacità dati rilevanti per l'Utente (ad es., ``authentic_source1.dataset1.userinfo``). Questa stringa DEVE essere fornita dalla Fonte Autentica al Trust Anchor durante l'onboarding. La formattazione Markdown può essere testo in chiaro o una combinazione di testo e link. Ad esempio, se il database della Fonte Autentica contiene solo dati registrati *dopo* una data specifica, questa informazione DEVE essere veicolata tramite questa chiave.
   * - **data_capabilities[].service_documentation_uri**
     - string
     - OPZIONALE. URL che punta alla documentazione del servizio della Fonte Autentica.
   * - **data_capabilities[].update_frequency**
     - string
     - OPZIONALE. Indica con quale frequenza la Fonte Autentica aggiorna i propri dati. Valori possibili: ``"real_time"`` (aggiornamenti quasi in tempo reale, tipicamente entro minuti), ``"daily"``, ``"weekly"``, ``"monthly"``, ``"on_demand"``.
   * - **data_capabilities[].logo_uri**
     - string
     - OPZIONALE. URL dell'immagine del logo relativa ai dati.
   * - **data_capabilities[].logo_uri#integrity**
     - string
     - CONDIZIONALE. Digest crittografico della risorsa immagine del logo per la verifica di integrità. OBBLIGATORIO se ``logo_uri`` è presente. Formato: ``{digest_method}-{digest_value}`` (ad es., ``"sha-256-abc123..."``).
   * - **data_capabilities[].logo_alt_text_l10n_id**
     - string
     - OPZIONALE. Testo alternativo per l'immagine del logo dell'organizzazione.
   * - **data_capabilities[].background_color**
     - string
     - OPZIONALE. Valore stringa del colore di sfondo da visualizzare insieme ai dati.
   * - **data_capabilities[].contacts**
     - String Array
     - OPZIONALE. Array di contatti del servizio clienti o canali di supporto utente (ad es., indirizzo e-mail).
   * - **data_capabilities[].verification_endpoint**
     - JSON object
     - OPZIONALE. Presente solo per gli attributi dell'Annex VI che fanno affidamento su una Fonte Autentica del settore pubblico e che sono esportati nel EUDIW Catalogue of Attributes. Descrive l'interfaccia di verifica transfrontaliera esposta ai Qualified Trust Service Provider, distinta dall'e-Service PDND nazionale e conforme a ETSI TS 119 478. Contiene ``method`` (uno tra ``oots_edelivery`` per l'interfaccia ISO 15000/eDelivery di ETSI TS 119 478 Section 6.2, o ``rest_oauth2`` per l'interfaccia REST + OAuth 2.0 di ETSI TS 119 478 Section 6.1) e ``endpoint`` (l'identificativo party eDelivery o l'endpoint REST). L'interfaccia PUÒ essere esposta dalla Fonte Autentica direttamente o da un intermediario nazionale designato (ad es. un access point OOTS).

.. note::
  Per ulteriori dettagli sulle funzionalità richieste e sull'esito atteso in termini di esperienza utente, si veda la Sezione :ref:`functionalities:Ottenimento dal Catalogo dell'Istanza del Wallet` per il parametro `data_capabilities.user_information` e la Sezione :ref:`functionalities:Focus sugli Attestati Elettronici di Attributi` per i parametri `organization_info.logo_uri`, `organization_info.logo_extended_uri`, `data_capabilities.logo_uri`, `data_capabilities.background_color` e `data_capabilities.available_claims.order`.

**Esempio di Authentic Source Registry**

Di seguito è fornito un esempio non normativo della struttura dell'AS Registry:

.. literalinclude:: ../../examples/as-registry-example.json
  :language: JSON

.. note::
  Per una gestione migliore e più efficiente della localizzazione delle informazioni contenute nell'Authentic Source Registry, un'Entità che lo consulta DOVREBBE:

  - Scaricare la versione di base dell'Authentic Source Registry (compatta, senza localizzazioni) utilizzando l'endpoint ``.well-known/authentic-sources``.
  - Determinare la lingua preferita dell'Utente.
  - Scaricare solo i bundle di localizzazione necessari.
  - Unire dinamicamente il contenuto localizzato con la struttura dell'Authentic Source Registry.

Di seguito è fornito un esempio non normativo dell'output di un bundle di localizzazione:

.. code-block:: json

  {
    "authentic_source1.name": "Ministero delle infrastrutture e dei trasporti",
    "authentic_source1.dataset1.origin": "MIT -- Direzione Generale per la Motorizzazione",
    "authentic_source1.dataset1.userinfo": "###### Patente di Guida\nSono disponibili le patenti rilasciate dopo il 1° gennaio 2020. Per le patenti più vecchie, contattare l'ufficio motorizzazione locale.",
    "authentic_source2.name": "Banca Esempio SpA",
    "authentic_source2.dataset1.origin": "Esempio origine dei dati 1",
    "authentic_source2.dataset1.userinfo": "###### Informazioni sulla disponibilità dei dati\nL'accesso ai dati finanziari richiede il consenso del cliente ed è soggetto alla normativa PSD2. Le informazioni sui conti sono disponibili solo per i conti attivi.",
    "...": "..."
  }

I bundle di localizzazione DEVONO essere disponibili all'URI composto concatenando il codice locale e ``.json`` al valore ``localization.base_uri`` definito nel registro. Ciascun bundle di locale DEVE essere accessibile seguendo il pattern di naming **{locale_code}.json**, dove **{locale_code}** è sostituito con il corrispondente codice locale dell'array **available_locales**.

Un esempio non normativo dell'URI di localizzazione italiana per il bundle sarebbe **https://trust-registry.eid-wallet.example.it/.well-known/l10n/authentic-sources/it.json**.

Schema Registry
---------------

Lo **Schema Registry** è l'inventario autorevole di tutti gli **Schema delle Credenziali** noti e accettati (JSON Schema per SD-JWT, CBOR Schema per mDOC) all'interno dell'ecosistema IT-Wallet.

**Schema Registry Objectives:**

1. **Centralizzazione degli schema**: Fornire un punto di accesso centralizzato per tutti gli schema tecnici utilizzati dagli Attestati Elettronici.
2. **Integrità e autenticità**: Assicurare l'integrità e l'autenticità dei documenti di schema tramite digest crittografici.
3. **Interoperabilità**: Facilitare l'integrazione senza soluzione di continuità dei Fornitori di Wallet e delle Relying Party fornendo versioni di schema coerenti.
4. **Supporto al ciclo di vita delle Credenziali**: Agire come punto di riferimento verificabile per la validazione dello schema durante l'emissione e la presentazione.


Schema Registry Usage
^^^^^^^^^^^^^^^^^^^^^

Come mostrato nella Figura :ref:`fig_registry_infrastructure` e nella Figura :ref:`fig_registry_discovery`, le principali Entità che interagiscono con lo Schema Registry sono:

  - **Attestation Scheme Provider**: Forniscono lo schema di un tipo di Credenziale, o il suo allineamento allo schema di un Rulebook esterno, e il Sistema di Onboarding lo registra con il suo digest di integrità durante lo :ref:`onboarding-system:Schema Provisioning`.
  - **Credential Issuer**: Utilizzano lo Schema Registry per costruire i propri metadata e per emettere gli Attestati Elettronici secondo lo schema registrato.
  - **Relying Party**: Utilizzano lo Schema Registry per raccogliere tutte le informazioni necessarie sugli Attestati Elettronici che intendono richiedere durante la fase di presentazione.
  - **Fornitori di Wallet**: Accedono allo Schema Registry per recuperare tutte le informazioni necessarie per integrarli nelle proprie Soluzioni Wallet.

Schema Registry Structure
^^^^^^^^^^^^^^^^^^^^^^^^^

L'URL dell'endpoint Schema Registry è pubblicato sotto la chiave ``schema_registry`` del documento Registry Discovery. L'endpoint supporta la content negotiation e la rappresentazione firmata comuni a tutti gli endpoint della Registry Infrastructure (si veda :ref:`registry:Content Negotiation and Signed Representation`).
Consente la discovery degli URI degli schema e dei relativi controlli crittografici di integrità.

.. list-table:: First-level Fields of the Schema Registry
   :class: longtable
   :widths: 30 70
   :header-rows: 1

   * - **Field Name**
     - **Description**
   * - **id**
     - OBBLIGATORIO. Identificativo univoco dello Schema Registry (ad es., ``urn:schemas:it-wallet``).
   * - **version**
     - OBBLIGATORIO. La versione dello Schema Registry (ad es., ``1.0.0``).
   * - **last_modified**
     - OBBLIGATORIO. Il timestamp che indica quando l'elenco è stato aggiornato l'ultima volta (ad es., ``2025-03-15T12:00:00Z``).
   * - **schemas**
     - OBBLIGATORIO. Un array JSON in cui ciascuna voce è un oggetto JSON che rappresenta una definizione di Schema di Credenziale. Ciascun oggetto contiene i parametri definiti nella tabella "Schema Definition Parameters" seguente, compresi identificazione dello schema, specifiche di formato, URI e dati di verifica di integrità.

.. list-table:: Schema Definition Parameters
   :widths: 25 75
   :header-rows: 1

   * - **Field Name**
     - **Description**
   * - **id**
     - OBBLIGATORIO. L'identificativo univoco dello schema (ad es., ``mDL+mso_mdoc+org.iso.18013.5.1.mDL``).
   * - **version**
     - OBBLIGATORIO. La versione della definizione dello schema (ad es., ``1.0.0``).
   * - **credential_type**
     - OBBLIGATORIO. L'identificativo univoco del tipo di Attestato Elettronico (ad es., ``mDL``, ``pid``, ``eid``).
   * - **format**
     - OBBLIGATORIO. Il formato tecnico dello schema (ad es., ``mso_mdoc``, ``dc+sd-jwt``).
   * - **vct**
     - CONDIZIONALE. È OBBLIGATORIO se il ``format`` è ``dc+sd-jwt``, indicando il Verifiable Credential Type (ad es., ``urn:eudi:mDL:it:1``).
   * - **docType**
     - CONDIZIONALE. È OBBLIGATORIO se il ``format`` è ``mso_mdoc``, indicando il tipo di documento utilizzato (ad es., ``org.iso.18013.5.1.mDL``).
   * - **schema_uri**
     - OBBLIGATORIO. L'URI da cui il documento di schema può essere recuperato (ad es., ``https://trust-registry.it-wallet.example.it/.well-known/schemas/mdoc/mDL``).
   * - **schema_uri#integrity**
     - OBBLIGATORIO. Digest crittografico del documento di schema per la verifica di integrità. Formato: ``{digest_method}-{digest_value}`` (ad es., ``sha256-c8b708728e4c5756e35c03aeac257ca878d1f717d7b61f621be4d36dbd9b9c16``).
   * - **description**
     - OPZIONALE. Una descrizione leggibile dello schema, che può essere localizzata (ad es., "Schema tecnico per la mobile Driving License in formato mdoc.").

**Esempio di Schema Registry:**

Un esempio non normativo del payload dello Schema Registry:

.. literalinclude:: ../../examples/schema-registry-example-payload.json
  :language: JSON

Digital Credentials Catalog
---------------------------

Il Digital Credentials Catalog è il registro di tutti gli Attestati Elettronici disponibili riconosciuti all'interno dell'ecosistema IT-Wallet. Agisce come singolo punto di riferimento per tutti gli attori coinvolti nel processo di emissione, verifica e utilizzo degli Attestati Elettronici.
Il Digital Credential Catalog DEVE contenere almeno:

.. list-table:: Digital Credential Catalog - Main information
   :class: longtable
   :widths: 30 70
   :header-rows: 1

   * - **Information related to**
     - **Description**
   * - Digital Credential Metadata
     - Informazioni identificative essenziali e caratteristiche dell'Attestato Elettronico, compresi:

       - **Identificativo univoco della Credenziale**: Una stringa identificativa univoca di ciascun Attestato Elettronico.
       - **Metodi di autenticazione dell'Utente**: Meccanismi di autenticazione dell'Utente utilizzati per richiedere l'Attestato Elettronico, se richiesto dagli Issuer o dalle Fonti Autentiche.
       - **Livello di Garanzia minimo**: Il Livello di Garanzia minimo richiesto per l'affidabilità dell'Attestato Elettronico. DEVE tenere conto del Livello di Garanzia dell'autenticazione dell'Utente, quando applicabile, e dell'Istanza del Wallet.
   * - Digital Credential Issuers
     - Dettagli sull'organizzazione autorizzata a emettere l'Attestato Elettronico, quali:

       - **Identificativi dell'Issuer**: Identificativo univoco dell'issuer dell'Attestato Elettronico.
       - **Tipo di Issuer**: Classificazione come PID, (Q)EAA o Pub-EAA Provider.
       - **Informazioni aggiuntive**: Dettagli organizzativi compresi nome, codice e informazioni di contatto.
   * - Authentic Sources
     - Informazioni sulla fonte dati autorevole.
   * - Technical Specification
     - Dettagli tecnici, compresi:

       - **Schema dell'Attestato Elettronico**: Specifiche di framework e struttura.
       - **Formati dell'Attestato Elettronico**: Standard di formato dati e encoding.
       - **Policy di autenticazione**: Metodi e requisiti per la verifica.
   * - Terms of Use
     - Condizioni e limitazioni per l'utilizzo dell'Attestato Elettronico, quali:

       - **Validità della Credenziale**: Periodo di tempo durante il quale l'Attestato Elettronico è valido e, quando applicabile, meccanismi e dettagli tecnici per invalidare gli Attestati Elettronici (metodi di revoca/sospensione).
       - **Restriction policy**: Se applicabile, regole che governano l'uso e le limitazioni dell'Attestato Elettronico secondo la regolamentazione nazionale. È utilizzata, ad esempio, per specificare se solo Entità di un determinato legal type, ad esempio Pub-EAA Provider e Soluzioni Wallet pubbliche, sono autorizzate a emettere e ottenere l'Attestato Elettronico.
       - **Pricing policy**: Informazioni relative ai modelli di prezzo dell'Attestato Elettronico, quali `free`, `issuance_based`, `verification_based`.
       - **Scopi dell'Attestato Elettronico**: Informazioni relative agli scopi consentiti per i quali l'Attestato Elettronico può essere utilizzato. Ciascun tipo di Attestato Elettronico può essere utilizzato per più scopi.

Il Digital Credential Catalog DEVE assicurare di:

  1. Facilitare la discovery degli Attestati Elettronici per gli Utenti.
  2. Standardizzare la descrizione tecnica e funzionale degli Attestati Elettronici.
  3. Abilitare l'interoperabilità tra Issuer e Relying Party diversi.
  4. Semplificare il processo di integrazione per i Fornitori di Wallet e le Relying Party.
  5. Assicurare la trust nell'ecosistema tramite informazioni verificabili e affidabili.
  6. Fornire trasparenza sull'ecosistema degli Attestati Elettronici disponibili.

Digital Credentials Catalog Usage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Come mostrato nella Figura :ref:`fig_registry_infrastructure` e nella Figura :ref:`fig_registry_discovery`, le principali Entità coinvolte nel Digital Credential Catalog sono:

  - **Attestation Scheme Provider**: Le Entità che possiedono l'Attestation Rulebook di un Attestato Elettronico e che richiedono la registrazione della corrispondente voce versionata, si veda Attestation Scheme Provider.
  - **Digital Credential Issuer**: Sono aggiunti al campo ``issuers`` di una voce versionata come risultato degli Attestati Elettronici che dichiarano nei propri dati di registrazione.
  - **Relying Party**: Utilizzano il Digital Credential Catalog per raccogliere tutte le informazioni necessarie sugli Attestati Elettronici che intendono richiedere durante la fase di presentazione.
  - **Fornitori di Wallet**: Accedono al Digital Credential Catalog per identificare gli Attestati Elettronici disponibili e per recuperare tutte le informazioni necessarie per integrarli nelle proprie Soluzioni Wallet.
  - **Utenti**: Gli Utenti che utilizzano indirettamente il Digital Credentials Catalog tramite le proprie Istanze del Wallet per scoprire e richiedere Attestati Elettronici.
  - **Fonti Autentiche**: Sono referenziate dalla voce versionata come sua fonte dati e agiscono come Attestation Scheme Provider quando possiedono l'Attestation Rulebook.

Una voce versionata non è fornita da una singola Entità.
I suoi campi provengono da fonti diverse e sono scritti in fasi di onboarding diverse, come sintetizzato nella tabella seguente.
I Data Identifier che recano queste informazioni attraverso l'onboarding, e la loro mappatura sui campi della voce, sono definiti in :ref:`onboarding-system:Registration Data Model`.

.. _table_catalog_entry_provision:
.. list-table:: Provision of a Versioned Entry of the Digital Credentials Catalog
   :class: longtable
   :widths: 40 32 28
   :header-rows: 1

   * - **Fields**
     - **Provided by**
     - **Process**
   * - ``credential_type``, ``version``, ``credential_name_l10n_id``, ``legal_type``, ``domains``, ``classes``, ``purposes``, ``authentication``, ``validity_info``, ``restriction_policy``, ``pricing_policy``, ``rulebookURI``, ``bindingType``, ``attestationLoS``, ``trustedAuthorities``
     - L'Attestation Scheme Provider, che trae i valori dall'Attestation Rulebook che possiede
     - :ref:`onboarding-system:Credential Type Registration`
   * - ``authentic_sources`` or ``parent_credentials``
     - L'Attestation Scheme Provider, referenziando le voci dell':ref:`registry:Authentic Source Registry` o un tipo di Credenziale già registrato
     - :ref:`onboarding-system:Credential Type Registration`
   * - ``schema_uri``, ``format``, ``vct``, ``docType``
     - L'Attestation Scheme Provider, tramite lo schema che rende disponibile nello :ref:`registry:Schema Registry`
     - :ref:`onboarding-system:Schema Provisioning`
   * - ``issuers``
     - Ciascun elemento deriva dagli Attestati Elettronici che un Credential Issuer dichiara nei propri dati di registrazione, con le capacità di emissione che offre per ciascuno di essi
     - :ref:`onboarding-system:Entity Registration` e :ref:`onboarding-system:Entity Update`
   * - ``state``
     - Non fornito. Deriva dalle condizioni della voce versionata
     - :ref:`onboarding-system:Credential Type Activation and Deactivation`

La registrazione della voce versionata è approvata dall'Organismo di Supervisione, come descritto in :ref:`onboarding-system:Eligibility and Compliance Preconditions`, è scritta dal Sistema di Onboarding ed è pubblicata dal Federation Trust Anchor con il resto del catalogo.

.. note::
  Lo schema è la definizione machine-readable di un tipo di Attestato, che a livello UE è registrata nel Catalogue of Schemes e che a livello nazionale corrisponde alla voce versionata del Digital Credentials Catalog.
  Il Credential Schema è lo JSON Schema o lo CBOR Schema che valida la struttura dell'Attestato Elettronico, ed è registrato nello :ref:`registry:Schema Registry`.
  L'Attestation Scheme Provider possiede il primo e fornisce il secondo come parte della specifica tecnica del tipo di Credenziale.

Digital Credentials Catalog Structure
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

L'URL dell'endpoint Digital Credentials Catalog è pubblicato sotto la chiave ``credential_catalog`` del documento Registry Discovery. L'endpoint supporta la content negotiation e la rappresentazione firmata comuni a tutti gli endpoint della Registry Infrastructure (si veda :ref:`registry:Content Negotiation and Signed Representation`).
La sua rappresentazione firmata è un JWT. I parametri di header DEVONO essere come definiti nella :ref:`corresponding table <table_catalog_parameters>`, e il payload contiene i seguenti parametri:

.. list-table:: First-level Fields of the Digital Credentials Catalog
   :class: longtable
   :header-rows: 1
   :widths: 30 70

   * - **Field Name**
     - **Description**
   * - **id**
     - OBBLIGATORIO. Identificativo univoco del Digital Credentials Catalog (ad es., ``urn:credential-catalog:it-wallet``).
   * - **version**
     - OBBLIGATORIO. La versione del Digital Credentials Catalog (ad es., ``1.0.0``).
   * - **last_modified**
     - OBBLIGATORIO. Il timestamp che indica quando l'elenco è stato aggiornato l'ultima volta (ad es., ``2025-03-15T12:00:00Z``).
   * - **iss**
     - OBBLIGATORIO. Identificativo dell'issuer del Digital Credential Catalog.
   * - **localization**
     - OBBLIGATORIO. Oggetto di configurazione della localizzazione contenente:

       * **default_locale**: Codice locale predefinito (ad es., ``it``).
       * **available_locales**: Array dei codici locale supportati (ad es., ``["en", "it"]``).
       * **base_uri**: URI di base per il recupero dei bundle di localizzazione (ad es., ``https://trust-registry.eid-wallet.example.it/.well-known/l10n/credential-catalog/``).
       * **version**: Versione del formato del bundle di localizzazione.
   * - **credentials**
     - OBBLIGATORIO. Array contenente le definizioni degli Attestati Elettronici.

Ciascun elemento dell'array ``credentials`` contiene almeno le seguenti informazioni:

.. _table_catalog_parameters_first_level:
.. list-table:: First-level Fields of Each Credential Entry
  :class: longtable
  :header-rows: 1
  :widths: 30 70

  * - **Field Name**
    - **Description**
  * - **version**
    - OBBLIGATORIO. Versione della definizione dell'Attestato Elettronico.
  * - **credential_type**
    - OBBLIGATORIO. Identificativo univoco del tipo di Attestato Elettronico. Per il PID DEVE essere ``pid`` e per l'IT-Wallet ID DEVE essere ``eid``.
  * - **state**
    - OBBLIGATORIO. Stato di questa voce versionata del tipo di Credenziale. DEVE essere uno tra:

      * ``ACTIVE``: il tipo di Credenziale può essere emesso da questa voce versionata. Una voce può essere ``ACTIVE`` solo finché almeno un Credential Issuer è elencato nel campo **issuers**, la Fonte Autentica o il tipo di Credenziale padre referenziato è disponibile, e lo schema è registrato per almeno un formato supportato.
      * ``INACTIVE``: il tipo di Credenziale NON DEVE essere emesso da questa voce versionata. Una voce è ``INACTIVE`` quando è stata appena registrata, quando una delle condizioni per lo stato ``ACTIVE`` cessa di valere, o quando è stata sostituita da una versione più recente.

      Una sola voce versionata dello stesso ``credential_type`` DEVE essere ``ACTIVE`` in un dato momento.
  * - **credential_name_l10n_id**
    - OBBLIGATORIO. Chiave di localizzazione che referenzia il nome leggibile dell'Attestato Elettronico nel bundle di localizzazione (ad es., ``mDL.name``).
  * - **legal_type**
    - OBBLIGATORIO. Classificazione legale della Credenziale (ad es., ``pub-eaa``, ``qeaa``, ``eaa``).
  * - **restriction_policy**
    - OPZIONALE. Restrizioni legali sulle Soluzioni Wallet e/o sui Credential Issuer autorizzati a richiedere/emettere l'Attestato Elettronico.

      * **allowed_wallet_ids**: Elenco degli identificativi delle Soluzioni Wallet consentite.
      * **allowed_issuer_ids**: Elenco degli identificativi dei Credential Issuer consentiti. Se presente, rappresenta una whitelist di Credential Issuer che possono essere aggiunti al campo **issuers** del corrispondente Attestato Elettronico, come descritto in :ref:`onboarding-system:Credential Type Registration`.
      * **presentation_flows**: Tipo di flussi di presentazione supportati; flusso remoto e/o di prossimità.
  * - **pricing_policy**
    - OPZIONALE. Informazioni sul prezzo dell'Attestato Elettronico, comprese:

      * **models**: OBBLIGATORIO. Array di modelli di prezzo applicabili all'Attestato Elettronico, ciascuno contenente

        - **pricing_type**: Tipo di modello di prezzo, quale ``issuance_based``, ``verification_based``, ``subscription_based``, ``other``.
        - **price**: Costo associato al modello.
        - **currency**: Valuta del prezzo.

      * **pricing_model_uri**: URI della documentazione dettagliata del modello di prezzo.
  * - **validity_info**
    - Informazioni sulla validità dell'Attestato Elettronico, comprese almeno:

      * **max_validity_days**: Periodo massimo di validità in giorni.
      * **status_methods**: Metodi di verifica dello stato supportati (ad es. ``status_list``).
      * **allowed_states**: Array di oggetti che rappresentano gli stati consentiti dell'Attestato Elettronico. Ciascun oggetto contiene un codice di stato esadecimale (ad es., ``0x00`` per ``VALID``, ``0x01`` per ``INVALID``, ``0x02`` per ``SUSPENDED``, ``0x03`` per ``UPDATE``, ``0x0F`` per ``ATTRIBUTE_UPDATE``), una chiave di localizzazione ``title_l10n_id`` e una chiave di localizzazione ``description_l10n_id`` per la visualizzazione in UI.
      * **administrative_expiration_user_info**: OPZIONALE. Oggetto contenente le chiavi ``title_l10n_id`` e ``description_l10n_id`` per visualizzare all'Utente le informazioni sulla scadenza amministrativa.
  * - **authentication**
    - OBBLIGATORIO. Requisiti di autenticazione dell'Attestato Elettronico.

      * **user_auth_required**: OBBLIGATORIO. Flag che indica se l'autenticazione dell'Utente è richiesta durante l'emissione dell'Attestato Elettronico.
      * **min_loa**: OBBLIGATORIO. Livello di Garanzia minimo richiesto per l'autenticazione dell'Attestato Elettronico. DEVE includere il Livello di Garanzia dell'autenticazione dell'Utente e dell'Istanza del Wallet che richiede l'Attestato Elettronico.
      * **supported_schemes**: OBBLIGATORIO se ``user_auth_required`` è ``true``. Schemi di autenticazione di identità digitale supportati (ad es., ``["it_wallet"]``).
  * - **domains**
    - OBBLIGATORIO. Array di ID di domain a cui l'Attestato Elettronico appartiene (ad es., ``"IDENTITY"``, ``"MOBILITY_TRAVEL"``).
  * - **classes**
    - OBBLIGATORIO. Array di ID di class a cui l'Attestato Elettronico appartiene (ad es., ``"IDENTIFICATION_DOCUMENTS"``, ``"LICENSES_AUTHORIZATIONS"``).
  * - **purposes**
    - OBBLIGATORIO. Array di ID di scopo di utilizzo per i quali l'Attestato Elettronico può essere utilizzato, che definiscono contesti di utilizzo specifici e i claim richiesti per ciascun purpose (ad es., ``"IDENTITY_VERIFICATION"``, ``"AGE_VERIFICATION"``, ``"DRIVING_RIGHTS_VERIFICATION"``).
  * - **issuers**
    - CONDIZIONALE. È OBBLIGATORIO solo se **state** è ``ACTIVE``. Array di informazioni rilevanti sui Credential Issuer autorizzati, compresi dati amministrativi e tecnici quali il nome dell'organizzazione, un riferimento al documento di specifica API e i meccanismi di emissione supportati. Ciascun elemento dell'array contiene:

       * **entity_id**: OBBLIGATORIO. Stringa. Identificativo univoco del Credential Issuer. DEVE coincidere con il valore contenuto nel parametro ``iss`` dell'Entity Configuration del Credential Issuer.
       * **organization_name_l10n_id**: OBBLIGATORIO. Stringa. Chiave di localizzazione che referenzia il nome localizzato dell'organizzazione nel bundle di localizzazione (ad es., ``issuer1.name``).
       * **organization_code**: OBBLIGATORIO. Stringa. Codice IPA del Credential Issuer per le entità governative o partita IVA per le entità private.
       * **organization_country**: OBBLIGATORIO. Stringa. Codice paese ISO 3166-1 alpha-2 a due lettere dell'organizzazione.
       * **contacts**: OBBLIGATORIO. Stringa. Array di indirizzi e-mail di contatto per almeno un supporto utente, un'applicazione e uno specialista di sistemi.
       * **legal_type**: OBBLIGATORIO. Stringa. Classificazione legale del Credential Issuer (ad es., pub-eaa, qeaa, eaa).
       * **homepage_uri**: OBBLIGATORIO. Stringa. URL che punta alla homepage dell'organizzazione.
       * **logo_uri**: OPZIONALE. Stringa. URL dell'immagine del logo dell'organizzazione.
       * **policy_uri**: OBBLIGATORIO. Stringa. URL del documento di informativa sulla privacy.
       * **tos_uri**: OPZIONALE. Stringa. URL del documento dei termini di servizio.
       * **service_documentation_uri**: OPZIONALE. Stringa. URL che punta alla documentazione del servizio del Credential Issuer.
       * **issuance_flows**: OBBLIGATORIO. Oggetto. Contiene i seguenti parametri:

          * **deferred_flow**: OBBLIGATORIO. Boolean. Indica se l'emissione differita è supportata.
          * **immediate_flow**: OBBLIGATORIO. Boolean. Indica se l'emissione immediata è supportata.
          * **wallet_initiated**: OBBLIGATORIO. Boolean. Indica se il flusso Wallet-Initiated è supportato.
          * **issuer_initiated**: OBBLIGATORIO. Boolean. Indica se l'emissione del flusso Issuer-Initiated è supportata (Third Party Initiated Flow).
          * **max_deferred_issuance_time_minutes**: CONDIZIONALE. Integer. Tempo massimo in minuti per la disponibilità dell'emissione della Credenziale. OBBLIGATORIO se ``deferred_flow`` è ``true``.
          * **notification_methods**: CONDIZIONALE. String Array. Contiene i metodi di notifica supportati dal Credential Issuer per l'emissione differita, quali ``"push"``, ``"polling"``. OBBLIGATORIO se ``deferred_flow`` è ``true``.

  * - **authentic_sources**
    - CONDIZIONALE. È OBBLIGATORIO solo se ``parent_credentials`` è assente. Array di oggetti JSON Fonte Autentica che referenziano le Fonti Autentiche autorizzate. Ciascun oggetto DEVE contenere l'identificativo dell'entità AS e l'identificativo della specifica capacità dati:

      * **id**: Identificativo stringa che referenzia l'entity_id della Fonte Autentica come registrato nell':ref:`registry:Authentic Source Registry`.
      * **dataset_id**: Identificativo stringa della specifica capacità dati/dataset utilizzato dall'Issuer dalla AS.
  * - **parent_credentials**
    - CONDIZIONALE. È OBBLIGATORIO solo se ``authentic_sources`` è assente. Array di identificativi ``credential_type`` corrispondenti alle Credenziali designate come fonti dati. Ciascun elemento identifica una Credenziale che agisce come Fonte Autentica durante il processo di emissione dell'Attestato Elettronico.
  * - **trustedAuthorities**
    - OBBLIGATORIO. Array di oggetti JSON che risolvono i trust anchor applicabili, contenenti:

       * **frameworkType**: tipo del trust model applicabile. Una stringa dall'insieme di ``etsi_tl`` o ``openid_federation``.
       * **value**: identificativo in formato URI standard per la Trusted List (per il tipo ``etsi_tl``) o Entity Identifier (per il tipo ``openid_federation``).
       * **isLoTE**: un valore boolean che DEVE essere TRUE quando il tipo di trust framework applicabile è una ETSI Trusted List (``etsi_tl``) ma la trusted list dietro l'URI del valore è una list of trusted entities (LoTE) secondo ETSI TS 119 602. Il valore DEVE essere FALSE se la specifica della trusted list applicabile è ETSI TS 119 612. L'attributo NON DEVE essere utilizzato con altri tipi di framework.

      Il ``frameworkType`` applicabile segue :ref:`infrastructure-trust:Infrastructure of Trust`. Per un PID, (Q)EAA o PuB-EAA di un altro Stato membro il trust model è basato sulle Lists of Trusted Lists e sulle Lists of Trusted Entities gestite dalla Commissione Europea.

      .. note::
        L'uso di ``isLoTE`` diventerà superfluo e dovrà essere deprecato una volta che OpenID4VCI specificherà una nuova enumerazione per le Lists of Trusted Entities secondo ETSI TS 119 602; l'enumerazione tentata è ``etsi_lote``.

  * - **rulebookURI**
    - OBBLIGATORIO. URI dell'Attestation Rulebook in forma leggibile che definisce tutti gli aspetti non machine-readable del tipo di Attestato Elettronico.
  * - **bindingType**
    - OBBLIGATORIO. Indica il tipo di associazione crittografica della chiave richiesto per l'emissione dell'Attestato Elettronico. Il valore consentito è una stringa dall'insieme di: ``claim`` (associazione a un claim crittografico presentato dall'Utente), ``key`` (associazione a una chiave posseduta dall'Utente), ``biometric`` (associazione ai biometrici presentati dell'Utente) o ``none`` (nessuna associazione crittografica).
  * - **attestationLoS**
    - OBBLIGATORIO. Livello di sicurezza (LoS) a cui l'Attestato Elettronico deve essere fornito. Il valore consentito è una stringa dall'insieme di: ``iso_18045_high``, ``iso_18045_moderate``, ``iso_18045_enhanced-basic`` o ``iso_18045_basic`` (si veda l'Annex D.2 di `OpenID4VCI`_ per maggiori dettagli).

.. note::
  Mentre ``min_loa`` nel claim ``authentication`` specifica i requisiti di autenticazione dell'Attestato Elettronico con riferimento al livello di garanzia del mezzo di identificazione elettronica richiesto durante l'autenticazione dell'utente nel processo di emissione, il claim ``attestationLoS`` integra questo requisito specificando la resistenza al potenziale di attacco sia per l'autenticazione dell'utente sia per l'archiviazione delle chiavi.

.. note::
  L'unione di ``credential_type`` e ``version`` DEVE essere univoca nel Credential Catalog.

L'esempio corrispondente del Digital Credentials Catalog come decodificato in JSON sia per l'header sia per il payload è il seguente:

.. literalinclude:: ../../examples/catalog-example-header.json
  :language: JSON

.. literalinclude:: ../../examples/catalog-example-payload.json
  :language: JSON

.. note::
  Per una gestione migliore e più efficiente della localizzazione delle informazioni contenute nel Digital Credentials Catalog, un'Entità che lo consulta DOVREBBE:

  - Scaricare la versione di base del Digital Credentials Catalog (compatta, senza localizzazioni) utilizzando l'endpoint ``.well-known/credential-catalog``.
  - Determinare la lingua preferita dell'Utente.
  - Scaricare solo i bundle di localizzazione necessari.
  - Unire dinamicamente il contenuto localizzato con la struttura del Digital Credentials Catalog.

Di seguito è fornito un esempio non normativo dell'output di un bundle di localizzazione:

.. code-block:: json

  {
    "mDL.name": "Patente di Guida",
    "mDL.issuer1.name": "Esempio di Credential Issuer",
    "...": "..."
  }

I bundle di localizzazione DEVONO essere disponibili all'URI composto concatenando il codice locale e ``.json`` al valore ``localization.base_uri`` definito nel catalogo. Ciascun bundle di locale DEVE essere accessibile seguendo il pattern di naming **{locale_code}.json**, dove **{locale_code}** è sostituito con il corrispondente codice locale dell'array **available_locales**.

Un esempio non normativo dell'URI di localizzazione italiana per il bundle sarebbe **https://trust-registry.eid-wallet.example.it/.well-known/l10n/credential-catalog/it.json**.

Decentralization of Display and Claim Information
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

La fonte canonica per le caratteristiche di visualizzazione e la struttura dei claim è determinata dai **Metadata del Credential Issuer**.

La logica complessiva per presentare un Attestato Elettronico è la seguente:

1. A seconda del Trust Framework richiesto, il Wallet o la Relying Party recupera il :ref:`registry:Digital Credentials Catalog` (per entrambi gli Attestati Elettronici gestiti da Credential Issuer ancorati nel National o nel Trust Framework EUDIW) per scoprire i `credential_type` disponibili e l'`entity_id` dei loro Credential Issuer.
2. Recupera i Metadata completi del Credential Issuer (si veda :ref:`credential-issuer-solution:Metadata per openid_credential_issuer`) come descritto nella Section 12.2.2 di `OpenID4VCI`_.
3. I Metadata del Credential Issuer DEVONO contenere le caratteristiche di visualizzazione complete (loghi, colori) e le informazioni dettagliate di schema (tramite link ai Type Metadata appropriati o direttamente nella configurazione). L'Issuer costruisce questi metadata sulla base dei suggerimenti forniti dalla Fonte Autentica (tramite l'AS Registry) e delle specifiche di schema standard (tramite lo Schema Registry).

Registry Integration and Cross-References
------------------------------------------

Come mostrato nella Figura :ref:`fig_registry_relationships`, i componenti del registro sono interconnessi e collaborano per supportare l'intero ecosistema delle Credenziali:

1. **AS Registry** ↔ **Taxonomy**: Le Fonti Autentiche dichiarano le capacità utilizzando le classificazioni della taxonomy per una categorizzazione standardizzata.
2. **AS Registry** ↔ **Claims Registry**: Le Fonti Autentiche dichiarano le capacità sui claim disponibili utilizzando il Claim Registry.
3. **AS Registry** ↔ **DC Catalog**: I tipi di Credenziale referenziano le capacità AS per la validazione della fonte dati.
4. **DC Catalog** ↔ **Taxonomy**: Le voci di Credenziale specificano domain e purpose dalla taxonomy per la discovery e l'autorizzazione.
5. **Schema Registry** ↔ **DC Catalog**: I tipi di Credenziale fanno riferimento allo Schema Registry per la discovery e la validazione dei dati.

.. _fig_registry_relationships:
.. plantuml:: plantuml/registry-relationships.puml
    :width: 99%
    :alt: The figure illustrates the national registry relationships.
    :caption: `Relationships between National Registries <https://www.plantuml.com/plantuml/svg/ZL9BRzD04BxxLmmH4gtKg0VAfOAenUNG2q9DxzLaT-oCj0zhPpQG8luxVZJM4a3DoTRiVe_lsxaHnQJPk-eD1-Eo9VXONrtMLqzrz5qC57HLLU_WZXeE1Ejl3_UFNzR5PSqTslJ-qaJlOrZzuwI9GPVudIHwMdwujAYuGQ6UzdFCmMBQdmLKZW7TKwAMHTF-0XPVNsRmy3A3-z0axF-oqPneSGu_gzdacK555zjCFVIEMzOUMIUo59JH2TI7yyK5l9KkiTAdnS7BuhnWGYbjt6RT3Xm6rZ4dGxETLtd4RCbZoRKU9wSp68ViIu9w6CZf18e_OeX-W3vEl__3_Agg8ZSiLt30NiDn1G86EzomOsKIi6GS9hAGXKCxuw2VYd33Pdn8WIOc4CNXnIq_amM3IcrC_3nUEDR_C_ohBc80t24xt3YQi7yxsnAC3Su5LbKrxmqiSzVB5YwkYmK2tNSaaAYXHC4GtAvB_IdTq2V8j2OxT6odOAL6udQhPRkbHlz90vTqPBZPWuqUEGXWiD3br4KPX5BqGvIPOf9cCN57QJzUngpRgTXZVKVD83_jvcb9DOvoHyix1pwIBdFVKB3Pkzy0>`_

La Figura :ref:`fig_eudiw_national_registry_relationships` mostra invece la mappatura tra i cataloghi EUDIW e le controparti nazionali:

- **EUDIW Catalogue of Attributes** corrisponde al **Claims Registry** nazionale per la definizione semantica degli attributi e all'**Authentic Source Registry** per la discovery del punto di verifica. Si noti che le definizioni nazionali degli attributi si allineano al catalogo a livello UE per l'interoperabilità transfrontaliera.
- **EUDIW Catalogue of Schemes** corrisponde allo **Schema Registry** nazionale per la discovery degli schema di attestazione e al **Digital Credentials Catalog** per la discovery dei requisiti di emissione e presentazione. Si noti che i registri nazionali contengono tutte le informazioni fornite in quello EUDIW più informazioni aggiuntive (ad es., modello di prezzo e informazioni di validità).

.. _fig_eudiw_national_registry_relationships:
.. plantuml:: plantuml/eudiw-national-registry-relationships.puml
    :width: 99%
    :alt: The figure illustrates the relationships between National Registries and EUDIW Catalogues.
    :caption: `Relationships between National Registries and EUDIW Catalogues <https://www.plantuml.com/plantuml/svg/bL9DRnCn4BtxLmm1YI8QHOHoer7BfeTS46f0712Afkj9OiaVmH-AAjJ_pcIJBXEBY7OFQy-RcUVtxBbA6MCkpgeNnhUsQ8AFpSMekLWqmMs29vydIhs6AIsD9vX_kPrzlPcBubmsgEFxKHkS2txoZymo-3p4BQNWQFXXf37Z7IPYsa-XU8tn_inZDi6ZNKHQcPJZ_JaCFXymk3rWCFFBYBmhRIwH1c_Wj-f5dc6IpTSbhnarBSn3YItr98DpU9KsqMIw71oKC9FWQIqQ9wcQ7P2UJh2n9RtZlhT7Q6hNv53opZla6S8Oj65LY7kdPcKuWYQItjb4cw1vp3z9uVYWy4691FqgQ7VQBpbJmUCzB1wDYZPRwUZcstJs_Q-ELB_GGbheoo0iuJhdQEvAflHVyUaqItUZ9oaUrBErxtg4QXZ2_eRKVk7uU5hKSSZvRXXKz-T8p2XKp3fi_O-NspMh_ZcSW71PazQbrMGfJAThUzBUGLNGmMEbL9BY7k7zmd5zfeY5yN5ddEl5kVnTaTV5sJy0>`_

.. note::
  Come specificato in `EIDAS-ARF`_, la registrazione di uno schema di attestazione nel EUDIW Catalogue of Schemes non crea alcun obbligo di accettazione del relativo tipo di attestazione da parte di qualsiasi attore dell'ecosistema EUDI Wallet. Né implica automaticamente il riconoscimento transfrontaliero del tipo di attestazione. È utilizzato per scoprire il corrispondente trust framework.

Registry Infrastructure Usage Journeys
--------------------------------------

I componenti della Registry Infrastructure sono progettati per supportare diverse fasi operative dell'ecosistema IT-Wallet, ciascuna delle quali coinvolge interazioni specifiche tra le entità.
I principali Journey seguenti illustrano le interazioni operative che leggono la Registry Infrastructure.
Il journey complementare che popola i registri è la registrazione di onboarding, che registra le entità, le Fonti Autentiche, i claim, gli schema e i tipi di Credenziale, come mostrato nella Figura :ref:`fig_registry_infrastructure` e descritto in :ref:`onboarding-system:Onboarding Processes`.

Catalog Browsing
^^^^^^^^^^^^^^^^

Questo journey di *Catalog Browsing* supporta gli Utenti (sia utenti umani tramite un'**Istanza del Wallet** sia sistemi automatizzati quali **Relying Party** o portali web) nella discovery e nella selezione degli Attestati Elettronici disponibili.

1.  **Accesso al Discovery Endpoint**: L'entità (ad es., un Fornitore di Wallet o un portale informativo) accede al `Registry Discovery Endpoint` (``.well-known/it-wallet-registry``) per ottenere l'URI del **Digital Credentials Catalog** e della **Taxonomy**.

2.  **Navigazione e selezione**:

    * **Discovery delle Credenziali**: L'entità sfoglia l'elenco delle Credenziali (campo ``credentials``) per identificare i tipi di Credenziale rilevanti (ad es., ``pid``, ``eid``, ``mDL``) e, se necessario, utilizza le informazioni sulla **Taxonomy** per navigarne la gerarchia e per fornire localizzazioni diverse.
    * **Metadata dell'Issuer**: L'entità estrae i Metadata del Credential Issuer (si veda :ref:`credential-issuer-solution:Metadata per openid_credential_issuer`) come descritto nella Section 12.2.2 di `OpenID4VCI`_.
    * **Consultazione di dettaglio**: Per ottenere informazioni complete e requisiti tecnici specifici, l'entità accede all'**Entity Configuration** utilizzando l'identificativo recuperato.

3.  **Azione finale**: L'entità può quindi utilizzare i metadata per visualizzare le informazioni del catalogo a un Utente, o utilizzarli in altri modi.

Credential Issuance
^^^^^^^^^^^^^^^^^^^

Questo journey definisce come un Credential Issuer utilizza la Registry Infrastructure per preparare e emettere un Attestato Elettronico conforme.

1.  **Identificazione dei requisiti**: Il Credential Issuer consulta il **Digital Credentials Catalog** per i requisiti tecnici del tipo di Credenziale da emettere (ad es., ``max_validity_days``, ``min_loa``).

2.  **Risoluzione di schema e claim**:

  Il Credential Issuer consulta:

    * il EUDIW Catalogue of Schemes per ottenere lo schema dell'Attestato Elettronico ancorato a EUDIW ricercato (``schemaURIs``), o
    * :ref:`registry:Schema Registry` per ottenere lo schema dell'Attestato Elettronico ancorato a livello nazionale ricercato (``schema_uri``).

  e, in entrambi i casi, ne verifica l'integrità. Quindi, a seconda del Trust Framework che ancora l'Attestato Elettronico, accede al EUDIW Catalogue of Attributes o al :ref:`registry:Claims Registry` per recuperare le definizioni semantiche standardizzate e i formati di dato degli attributi (claim) necessari.

3.  **Recupero dei dati autentici**:

  * Il Credential Issuer consulta l'**Authentic Source (AS) Registry** per identificare la **Fonte Autentica** (AS) autorizzata per il dataset richiesto. L'AS Registry fornisce l'``entity_id`` dell'AS e i dettagli tecnici dell'interfaccia (`integration_endpoint`, `integration_method`).
  * Il Credential Issuer consulta la specifica dell'endpoint AS per implementare l'integrazione necessaria a recuperare i dati dell'Utente richiesti per popolare l'Attestato Elettronico.

4.  **Emissione della Credenziale**: Il Credential Issuer utilizza i dati recuperati, gli schema validati e i formati specificati per generare e firmare l'Attestato Elettronico nel formato corretto (ad es., SD-JWT o mDOC).

Credential Presentation and Verification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Questo journey descrive come un'**Istanza del Wallet** e una **Relying Party (RP)** interagiscono con la Registry Infrastructure quando un Attestato Elettronico deve essere presentato da un Utente.

1.  **Autorizzazione e selezione della Wallet Unit**:

  * La Wallet Unit riceve una Presentation Request dalla RP. La Wallet Unit DEVE valutare la trust con la RP che emette la Presentation Request come segue:

    * **(EUDIW Trust Framework)**:

      * La Wallet Unit valida la firma della Presentation Request e valuta la trust con la Relying Party che la produce come descritto in :ref:`trust-evaluation:EUDIW Authentication`.
      * La Wallet Unit valida se la RP è titolata a questa presentazione come descritto in :ref:`trust-evaluation:EUDIW Authorization`.

    * **(National Trust Framework)**:

      * La Wallet Unit valida la firma della Presentation Request e valuta la trust con la Relying Party che la produce come descritto in :ref:`trust-evaluation:Authentication`.
      * La Wallet Unit valida se la RP è titolata a questa presentazione come descritto in :ref:`trust-evaluation:Authorization`.

   Indipendentemente dal Trust Framework, la decisione finale su se la RP è Authorized durante la presentazione è assunta secondo :ref:`trust-evaluation:Authorization Decision and Override Rules`.

  * L'Utente autorizza il rilascio degli attributi selezionati, oggetto di selective disclosure. Il Wallet quindi impacchetta e presenta l'Attestato Elettronico alla RP.

2.  **Discovery e integrità**:

  * La RP riceve l'Attestato Elettronico dall'Utente.
  * A seconda del trust framework a cui la RP aderisce (ossia, il National o il Trust Framework EUDIW):

    * **(EUDIW Trust Framework)**:

      * La RP valida la firma dell'Attestato Elettronico e valuta la trust con il suo issuer come descritto in :ref:`trust-evaluation:EUDIW Attestation Signature Validation`.
      * La RP consulta il EUDIW Catalogue of Schemes per scaricare lo schema della Credenziale presentata (`schema_uri`), verificandone l'integrità (`schema_uri#integrity`) ove applicabile.

    * **(National Trust Framework)**:

      * La RP valida la firma dell'Attestato Elettronico e valuta la trust con il suo issuer come descritto in :ref:`trust-evaluation:Signing Trust Anchor Validation Procedure`.
      * La RP consulta lo :ref:`registry:Schema Registry` per scaricare lo schema della Credenziale presentata (`schema_uri`), verificandone l'integrità (`schema_uri#integrity`).

3.  **Validazione dello schema e della policy finale**:

  * La RP utilizza lo schema recuperato per validare la struttura della Credenziale e i tipi di dato degli attributi rivelati.
  * La RP esegue il controllo finale per assicurare che gli attributi presentati siano conformi ai requisiti specifici della richiesta iniziale e della policy di autorizzazione.

4.  **Accettazione o rifiuto**: Sulla base della validazione crittografica, della conformità allo schema e dell'autorizzazione basata su policy, la RP accetta o rifiuta l'Attestato Elettronico per l'accesso al servizio.

Cross-border Attribute Verification by a QTSP
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Questo journey descrive come un Qualified Trust Service Provider (QTSP), eventualmente stabilito in un altro Stato membro, verifica il valore di un attributo dell'Annex VI rispetto a una Fonte Autentica italiana del settore pubblico per emettere una QEAA.
Esercita il EUDIW Catalogue of Attributes e il ``verification_endpoint`` dell':ref:`registry:Authentic Source Registry`, e non utilizza la valutazione di trust OpenID Federation nazionale né l'e-Service PDND nazionale.

1.  **Discovery del punto di verifica**: Il QTSP interroga il EUDIW Catalogue of Attributes per l'attributo richiesto e risolve la voce ``Attribute`` italiana responsabile, ottenendo l'``authenticSources[].DataService.endpointURL`` (l'interfaccia di verifica ETSI TS 119 478 dichiarata nel ``verification_endpoint`` dell'AS Registry), la ``legalBasis`` e la descrizione di come avviare la richiesta di verifica. La controparte nazionale del Catalogue of Attributes è la coppia Claims Registry, per la semantica, e Authentic Source Registry, per il punto di verifica, si veda :ref:`registry:Registry Integration and Cross-References`.

2.  **Selezione dell'interfaccia**: A seconda di ``verification_endpoint.method``, il QTSP utilizza l'interfaccia ISO 15000/eDelivery (``oots_edelivery``) o l'interfaccia REST + OAuth 2.0 (``rest_oauth2``) di ETSI TS 119 478 Section 6.

3.  **Richiesta di verifica**: Il QTSP presenta la richiesta di verifica all'endpoint, esposto dalla Fonte Autentica o dall'intermediario nazionale designato, che restituisce la conferma autentica del valore dell'attributo per l'Utente. Come previsto dall'Articolo 45e di [`EIDAS`_], questa è una verifica di autenticità dell'attributo e non un accesso ai dati sottostanti.

4.  **Emissione**: Il QTSP emette la QEAA secondo il proprio Rulebook e i propri trust anchor, ossia le EUDIW Trusted Lists. L'ancoraggio di trust della QEAA risultante non deriva dalla presenza di alcun schema nel Catalogue of Schemes, si veda la nota in :ref:`registry:Registry Integration and Cross-References`.

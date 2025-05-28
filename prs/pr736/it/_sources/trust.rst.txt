.. include:: ../common/common_definitions.rst
.. include:: ../common/symbols.rst



L'Infrastruttura di Trust
=========================

Questa sezione delinea l'implementazione del Modello di Trust in un'infrastruttura conforme a OpenID Federation 1.0 `OID-FED`_. Questa infrastruttura prevede un'API RESTful per la distribuzione di metadati, policy di metadati, trust mark, chiavi pubbliche crittografiche e certificati X.509, e lo stato di revoca dei partecipanti, chiamati anche Entità di Federazione.

L'Infrastruttura di trust facilita l'applicazione di un meccanismo di valutazione della fiducia tra le parti definite nell'`EIDAS-ARF`_.

.. plantuml:: plantuml/trust-roles.puml
   :width: 99%
   :alt: La figura illustra i ruoli di trust.
   :caption: `I ruoli all'interno della Federazione, dove il Trust Anchor supervisiona i suoi subordinati, che includono uno o più Intermediari e Foglie. <https://www.plantuml.com/plantuml/png/XT1VIyD0303mz_iKSJuFiOpXWuoDJc7Wmn31HybwSHwxvaekvnZYTtTjjUrWpBVy-LsuP1uLHLFfpPNZmYTBS9zFRlB9MnvOqJ79p9YuSroXO0aRB7PR2Obj7dmGK46EnnQn3jH29EnRiF775yO85OgyzGIZ5qbHOS75Hv0HO0H5k5vE7-uUinEtOYKfoJfKQfnZlUtaFp0xE_A9y3qsnDVHSLfDbjCB9klC1TJTwW_3bm4O-5p84gj33wiO4xMB5wxxvOb-HUz9OItXqzbVkw_EssVo1yTRMAFeeP7IoszZ2WVZL8rde6ZsLHitbpGoo3BJ7cJORzSVchhSJwjBVMRcn3QL_WS0>`_

In questa rappresentazione, sia il Trust Anchor che gli Intermediari assumono il ruolo di Registration Authority.

Ruoli della Federazione
-----------------------

Tutti i partecipanti sono Entità di Federazione che DEVONO essere registrati da un Organismo di Registrazione,
ad eccezione delle Istanze del Wallet che sono dispositivi personali dell'Utente finale autenticati dal loro Fornitore di Wallet.

.. note::
  L'Istanza del Wallet, come dispositivo personale, è considerata affidabile attraverso un attestato verificabile emesso e firmato da una terza parte fidata.

  Questo è chiamato *Wallet Attestation* ed è documentato nella sezione dedicata :ref:`wallet-attestation-issuance:Emissione dell'Attestato di Wallet`.

Di seguito la tabella con il riepilogo dei ruoli delle Entità di Federazione, mappati sui corrispondenti ruoli del Wallet EUDI, come definiti nell'`EIDAS-ARF`_.

.. list-table::
   :class: longtable
   :widths: 20 20 60
   :header-rows: 1

   * - Ruolo EUDI
     - Ruolo nella Federazione
     - Note
   * - Public Key Infrastructure (PKI)
     - Trust Anchor
     - La Federazione ha capacità PKI. L'Entità che configura l'intera infrastruttura è il Trust Anchor.
   * - Qualified Trust Service Provider (QTSP)
     - Leaf
     -
   * - Person Identification Data Provider
     - Leaf
     -
   * - Qualified Electronic Attestations of Attributes Provider
     - Leaf
     -
   * - Electronic Attestations of Attributes Provider
     - Leaf
     -
   * - Relying Party
     - Leaf
     -
   * - Trust Service Provider (TSP)
     - Leaf
     -
   * - Trusted List
     - Trust Anchor
     - L'endpoint di listing, l'endpoint di stato del trust mark e l'endpoint di fetch DEVONO essere esposti sia dai Trust Anchor che dagli Intermediari, rendendo la Trusted List distribuita su più Entità di Federazione, dove ciascuna di queste è responsabile dei propri subordinati registrati. Altri endpoint che utilizzano formati di dati diversi POSSONO essere implementati per facilitare l'interoperabilità con sistemi che non supportano OpenID Federation 1.0. In tali casi, le stesse informazioni sulle entità di federazione DEVONO essere sincronizzate tra questi endpoint, garantendo la disponibilità coerente delle informazioni attraverso diversi canali.
   * - Wallet Provider
     - Leaf
     -

Proprietà Generali
------------------

L'architettura dell'infrastruttura di trust è costruita sui seguenti principi fondamentali:

.. list-table::
   :class: longtable
   :widths: 20 20 80
   :header-rows: 1

   * - Identificatore
     - Proprietà
     - Descrizione
   * - P1
     - **Sicurezza**
     - Incorpora meccanismi per garantire l'integrità, la riservatezza e l'autenticità delle Relazioni di Trust e delle interazioni all'interno della federazione.
   * - P2
     - **Privacy**
     - Progettata per rispettare e proteggere la privacy delle entità e degli individui coinvolti, la divulgazione minima fa parte di questo.
   * - P3
     - **Interoperabilità**
     - Supporta l'interazione senza soluzione di continuità e l'instaurazione della fiducia tra diversi sistemi ed entità all'interno della federazione.
   * - P4
     - **Trust Transitivo**
     - Trust stabilito indirettamente attraverso una catena di relazioni fidate, consentendo alle entità di fidarsi l'una dell'altra sulla base di autorità comuni e intermediari fidati.
   * - P5
     - **Delega**
     - Capacità/funzionalità tecnica di delegare autorità o responsabilità ad altre entità, consentendo un meccanismo di trust distribuito.
   * - P6
     - **Scalabilità**
     - Progettata per gestire in modo efficiente un numero crescente di entità o interazioni senza un significativo aumento della complessità di gestione della fiducia.
   * - P7
     - **Flessibilità**
     - Adattabile a varie esigenze operative e organizzative, consentendo alle entità di definire e regolare le proprie Relazioni di Trust e politiche.
   * - P8
     - **Autonomia**
     - Pur facendo parte di un ecosistema federato, ogni entità mantiene il controllo sulle proprie definizioni e configurazioni.
   * - P9
     - **Decentralizzazione**
     - A differenza dei tradizionali sistemi centralizzati, l'infrastruttura di trust dovrebbe consentire un approccio decentralizzato.


Requisiti dell'Infrastruttura di Trust
--------------------------------------

Questa sezione include i requisiti necessari per l'implementazione e il funzionamento di successo dell'infrastruttura di trust.

.. list-table:: Requisiti Funzionali
   :class: longtable
   :widths: 20 80
   :header-rows: 1

   * - ID
     - Descrizione
   * - FR1
     - **Stabilimento della Fiducia nella Federazione**: il sistema deve essere in grado di stabilire la fiducia tra diverse entità (Credential Issuer, Relying Party, ecc.) all'interno di una federazione, utilizzando firme crittografiche per lo scambio sicuro di informazioni sui partecipanti nell'ecosistema.
   * - FR2
     - **Autenticazione delle Entità**: il sistema deve implementare meccanismi per l'autenticazione delle entità all'interno della federazione, garantendo la conformità alle regole condivise.
   * - FR3
     - **Convalida della Firma**: il sistema deve supportare la creazione, la verifica e la convalida delle firme elettroniche e fornire meccanismi standard e sicuri per ottenere le chiavi pubbliche crittografiche necessarie per la convalida della firma.
   * - FR4
     - **Marcatura Temporale**: gli artefatti firmati devono contenere marcature temporali per garantire l'integrità e la non ripudiabilità delle transazioni nel tempo, grazie alle interfacce, ai servizi, al modello di archiviazione e agli approcci definiti all'interno della federazione.
   * - FR5
     - **Convalida dei Certificati**: il sistema richiede la trasmissione confidenziale, protetta tramite TLS su HTTP, e la convalida dei certificati per l'autenticazione del sito web.
   * - FR6
     - **Interoperabilità e Conformità agli Standard**: garantire l'interoperabilità tra i membri della federazione aderendo a standard tecnici, facilitando le transazioni elettroniche transfrontaliere.
   * - FR7
     - **Protezione dei Dati e Privacy**: implementare misure di protezione dei dati in conformità con le normative GDPR, garantendo la privacy e la sicurezza dei dati personali trattati all'interno della federazione.
   * - FR8
     - **Risoluzione delle Controversie e Responsabilità**: stabilire procedure chiare per la risoluzione delle controversie e definire la responsabilità tra i membri della federazione.
   * - FR9
     - **Servizi di Emergenza e Revoca**: implementare meccanismi per la revoca immediata dei partecipanti in caso di violazioni della sicurezza o altre emergenze.
   * - FR10
     - **Infrastruttura di Trust Scalabile**: il sistema deve supportare meccanismi di stabilimento della fiducia scalabili, sfruttando approcci e soluzioni tecniche che complementano gli approcci transitivi di delega per gestire in modo efficiente le Relazioni di Trust man mano che la federazione cresce, rimuovendo i registri centrali che potrebbero fallire tecnicamente o amministrativamente.
   * - FR11
     - **Scalabilità Efficiente dello Storage**: implementare una soluzione di storage che si scala orizzontalmente per adattarsi a volumi di dati crescenti, minimizzando lo storage centrale e i costi amministrativi. Il sistema dovrebbe consentire ai membri di archiviare e presentare in modo indipendente attestazioni di fiducia storiche e artefatti firmati durante la risoluzione delle controversie, con l'infrastruttura della federazione che mantiene solo un registro delle chiavi storiche per convalidare i dati storici, archiviati e forniti dai partecipanti.
   * - FR12
     - **Attestazione Verificabile (Trust Mark)**: incorporare un meccanismo per l'emissione e la verifica di attestazioni verificabili che servono come prova di conformità a specifici profili o standard. Ciò consente alle entità all'interno della federazione di dimostrare l'aderenza a standard di sicurezza, privacy e operativi concordati.
   * - FR13
     - **Meccanismo Decentralizzato di Risoluzione delle Controversie**: progettare un meccanismo decentralizzato per la risoluzione delle controversie che consenta ai membri della federazione di verificare in modo indipendente lo stabilimento storico della fiducia e gli artefatti firmati, riducendo la dipendenza dalle autorità centrali e semplificando il processo di risoluzione.
   * - FR14
     - **Interoperabilità tra Federazioni**: garantire che il sistema sia in grado di interoperare con altre federazioni o Trust Framework, facilitando le transazioni tra federazioni e lo stabilimento della fiducia senza compromettere la sicurezza o la conformità.
   * - FR15
     - **Organismi di Registrazione Autonomi**: il sistema deve facilitare l'integrazione di organismi di registrazione autonomi che operano in conformità con le regole della federazione. Questi organismi hanno il compito di valutare e registrare le entità all'interno della federazione, secondo le regole prestabilite e la loro conformità che deve essere periodicamente attestata.
   * - FR16
     - **Audit Periodico degli Organismi di Registrazione e delle Entità**: implementare meccanismi per l'audit periodico e il monitoraggio dello stato di conformità sia degli organismi di registrazione che delle loro entità registrate.
   * - FR17
     - **Attestazione di Conformità per Dispositivi Personali**: organismi fidati, sotto forma di entità di federazione, dovrebbero emettere attestazioni di conformità e fornire prove firmate di tale conformità per l'hardware dei dispositivi personali utilizzati all'interno della federazione. Queste attestazioni dovrebbero essere attestate e periodicamente rinnovate per garantire che i dispositivi soddisfino gli standard di sicurezza attuali.
   * - FR18
     - **Monitoraggio Automatizzato della Conformità**: il sistema dovrebbe includere strumenti automatizzati per monitorare la conformità delle entità agli standard della federazione. Questa automazione aiuta nella rilevazione precoce di potenziali problemi di conformità.
   * - FR19
     - **Associazione Sicura delle Capacità del Protocollo**: il protocollo sicuro deve consentire lo scambio di dati sulle capacità specifiche del protocollo come metadati crittograficamente vincolati allegati a un'identità specifica. Questi metadati dovrebbero definire le capacità tecniche associate all'identità, garantendo una prova verificabile e un'associazione a prova di manomissione per un solido stabilimento della fiducia e controllo degli accessi.


Endpoint API della Federazione
------------------------------

OpenID Federation 1.0 utilizza Servizi Web RESTful protetti su
HTTPs. OpenID Federation 1.0 definisce quali sono gli endpoint web che i partecipanti DEVONO rendere
pubblicamente disponibili. La tabella seguente riassume gli endpoint e i loro scopi.

Tutti gli endpoint elencati di seguito sono definiti nelle specifiche `OID-FED`_.

.. list-table::
   :class: longtable
   :widths: 20 20 20 20
   :header-rows: 1

   * - nome endpoint
     - richiesta http
     - scopo
     - richiesto per
   * - federation metadata
     - **GET** .well-known/openid-federation
     - Metadati che un'Entità pubblica su se stessa, verificabili con una terza parte fidata (Entità Superiore). È chiamata Entity Configuration.
     - Trust Anchor, Intermediate, Wallet Provider, Relying Party, Credential Issuer
   * - subordinate list endpoint
     - **GET** /list
     - Elenca i Subordinati.
     - Trust Anchor, Intermediate
   * - fetch endpoint
     - **GET** /fetch?sub=https://rp.example.org
     - Restituisce un JWT firmato su un soggetto specifico, il suo Subordinato. È chiamato Subordinate Statement.
     - Trust Anchor, Intermediate
   * - trust mark status
     - **POST** /status?sub=...&trust_mark_id=...
     - Restituisce lo stato dell'emissione (validità) di un Trust Mark relativo a un soggetto specifico.
     - Trust Anchor, Intermediate
   * - historical keys
     - **GET** /historical-jwks
     - Elenca le chiavi scadute e revocate, con la motivazione della revoca.
     - Trust Anchor, Intermediate


Tutte le risposte degli endpoint della federazione sono sotto forma di JWT firmati, ad eccezione dell'**endpoint di Listing dei Subordinati** e dell'**endpoint di Stato del Trust Mark** che vengono serviti come JSON semplice di default.


Configurazione della Federazione
--------------------------------

La configurazione della federazione è pubblicata dal Trust Anchor all'interno della sua Entity Configuration, è disponibile al percorso web noto corrispondente a **.well-known/openid-federation**.

Tutti i partecipanti alla federazione DEVONO ottenere la configurazione della federazione prima di entrare nella fase operativa, e
DEVONO mantenerla aggiornata. La configurazione della federazione è l'Entity Configuration del Trust Anchor, contiene le
chiavi pubbliche per le operazioni di firma.

Di seguito un esempio non normativo di Entity Configuration di un Trust Anchor, dove ogni parametro è documentato nella specifica `OpenID Federation <OID-FED>`_:

.. code-block:: text

    {
        "alg": "ES256",
        "kid": "FifYx03bnosD8m6gYQIfNHNP9cM_Sam9Tc5nLloIIrc",
        "typ": "entity-statement+jwt"
    }
    .
    {
        "exp": 1649375259,
        "iat": 1649373279,
        "iss": "https://trust-registry.eid-wallet.example.it",
        "sub": "https://trust-registry.eid-wallet.example.it",
        "jwks": {
            "keys": [
                {

                    "kty": "EC",
                    "kid": "X2ZOMHNGSDc4ZlBrcXhMT3MzRmRZOG9Jd3o2QjZDam51cUhhUFRuOWd0WQ",
                    "crv": "P-256",
                    "x": "1kNR9Ar3MzMokYTY8BRvRIue85NIXrYX4XD3K4JW7vI",
                    "y": "slT14644zbYXYF-xmw7aPdlbMuw3T1URwI4nafMtKrY"
                }
            ]
        },
        "metadata": {
            "federation_entity": {
                "organization_name": "example TA",
                "contacts":[
                    "tech@eid.trust-anchor.example.eu"
                ],
                "homepage_uri": "https://trust-registry.eid-wallet.example.it",
                "logo_uri":"https://trust-registry.eid-wallet.example.it/static/svg/logo.svg",
                "federation_fetch_endpoint": "https://trust-registry.eid-wallet.example.it/fetch",
                "federation_resolve_endpoint": "https://trust-registry.eid-wallet.example.it/resolve",
                "federation_list_endpoint": "https://trust-registry.eid-wallet.example.it/list",
                "federation_trust_mark_status_endpoint": "https://trust-registry.eid-wallet.example.it/trust_mark_status"
            }
        },
        "trust_mark_issuers": {
            "https://trust-registry.eid-wallet.example.it/openid_relying_party/public": [
                "https://trust-registry.eid-wallet.example.it",
                "https://public.intermediary.other.org"
            ],
            "https://trust-registry.eid-wallet.example.it/openid_relying_party/private": [
                "https://private.other.intermediary.org"
            ]
        }
    }


Entity Configuration
--------------------

L'Entity Configuration è il documento verificabile che ogni Entità di Federazione DEVE pubblicare per proprio conto, nell'endpoint **.well-known/openid-federation**.

La risposta HTTP dell'Entity Configuration DEVE impostare il tipo di media a `application/entity-statement+jwt`.

L'Entity Configuration DEVE essere firmata crittograficamente. La parte pubblica di questa chiave DEVE essere fornita nell'
Entity Configuration e all'interno del Subordinate Statement emesso da un superiore immediato e relativo alla sua Entità di Federazione subordinata.

L'Entity Configuration PUÒ anche contenere uno o più Trust Mark.

I dettagli tecnici sull'Entity Configuration del Fornitore di Wallet, del Credential Issuer e della Relying Party sono forniti rispettivamente nelle Sezioni :ref:`wallet-provider-entity-configuration:Configurazione dell'Entità del Fornitore di Wallet`, :ref:`credential-issuer-entity-configuration:Configurazione dell'Entità Fornitore di Credenziale` e :ref:`relying-party-entity-configuration:Configurazione dell'Entità Relying Party`.


.. note::
  **Firma dell'Entity Configuration**

  Tutte le operazioni di verifica della firma riguardanti le Entity Configuration, i Subordinate Statement e i Trust Mark, sono effettuate con le chiavi pubbliche della Federazione. Per gli algoritmi supportati fare riferimento alla Sezione `Cryptografic Algorithm`.

Parametri Comuni delle Entity Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Le Entity Configuration di tutti i partecipanti alla federazione DEVONO avere in comune i parametri elencati di seguito.


.. list-table::
   :class: longtable
   :widths: 20 60
   :header-rows: 1

   * - **Claim**
     - **Descrizione**
   * - **iss**
     - String. Identificatore dell'Entità emittente.
   * - **sub**
     - String. Identificatore dell'Entità a cui si riferisce. DEVE essere uguale a ``iss``.
   * - **iat**
     - Timestamp UNIX con l'ora di generazione del JWT, codificato come NumericDate come indicato in :rfc:`7519`.
   * - **exp**
     - Timestamp UNIX con l'ora di scadenza del JWT, codificato come NumericDate come indicato in :rfc:`7519`.
   * - **jwks**
     - Un JSON Web Key Set (JWKS) :rfc:`7517` che rappresenta la parte pubblica delle chiavi di firma dell'Entità in questione. Ogni JWK nel set JWK DEVE avere un ID chiave (claim kid) e PUÒ avere un parametro `x5c`, come definito in :rfc:`7517`. Contiene le Chiavi dell'Entità di Federazione necessarie per le operazioni di Valutazione della Fiducia.
   * - **metadata**
     - JSON Object. Ogni chiave dell'Oggetto JSON rappresenta un identificatore di tipo di metadati
       contenente un Oggetto JSON che rappresenta i metadati, secondo lo schema di metadati
       di quel tipo. Un'Entity Configuration PUÒ contenere più dichiarazioni di metadati, ma solo una per ogni tipo di
       metadati (<**entity_type**>). i tipi di metadati sono definiti nella sezione `Tipi di Metadati <Metadata Types>`_.


Entity Configuration Trust Anchor
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

L'Entity Configuration del Trust Anchor, oltre ai parametri comuni elencati sopra, utilizza i seguenti parametri:

.. list-table::
   :class: longtable
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Descrizione**
     - **Richiesto**
   * - **trust_mark_issuers**
     - Array JSON che definisce quali autorità della Federazione sono considerate affidabili
       per l'emissione di specifici Trust Mark, assegnati con i loro identificatori unici.
     - |uncheck-icon|
   * - **trust_mark_owners**
     - Array JSON che elenca quali entità sono considerate proprietarie di
       specifici Trust Mark.
     - |uncheck-icon|


Entity Configuration Foglie e Intermediari
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Oltre ai claim precedentemente definiti, l'Entity Configuration delle Foglie e delle Entità Intermediarie utilizza i seguenti parametri:


.. list-table::
   :class: longtable
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Descrizione**
     - **Richiesto**
   * - **authority_hints**
     - Array di URL (String). Contiene un elenco di URL delle entità superiori immediate, come il Trust Anchor o
       un Intermediario, che emette un Subordinate Statement relativo a questo soggetto.
     - |check-icon|
   * - **trust_marks**
     - Un Array JSON contenente i Trust Mark.
     - |uncheck-icon|


Tipi di Metadati
^^^^^^^^^^^^^^^^

In questa sezione sono definiti i principali tipi di metadati mappati ai ruoli dell'ecosistema,
fornendo i riferimenti del protocollo di metadati per ciascuno di essi.


.. note::
  Le voci che non hanno alcun riferimento a una bozza o standard noto sono intese come definite in questo riferimento tecnico.

.. list-table::
   :class: longtable
   :widths: 20 20 20 60
   :header-rows: 1

   * - Entità OpenID
     - Entità EUDI
     - Tipo di Metadati
     - Riferimenti
   * - Trust Anchor
     - Trust Anchor
     - ``federation_entity``
     - `OID-FED`_
   * - Intermediate
     - Intermediate
     - ``federation_entity``
     - `OID-FED`_
   * - Wallet Provider
     - Wallet Provider
     - ``federation_entity``, ``wallet_provider``
     - --
   * - Authorization Server
     -
     - ``federation_entity``, ``oauth_authorization_server``
     - `OPENID4VCI`_
   * - Credential Issuer
     - PID Provider, (Q)EAA Provider
     - ``federation_entity``, ``openid_credential_issuer``, [``oauth_authorization_server``]
     - `OPENID4VCI`_
   * - Relying Party
     - Relying Party
     - ``federation_entity``, ``openid_credential_verifier``
     - `OID-FED`_, `OpenID4VP`_


.. note::
  I metadati del Fornitore di Wallet sono definiti nella sezione seguente.

  :ref:`wallet-solution:Soluzione Wallet`.


.. note::
  Nei casi in cui un Fornitore di PID/EAA implementi sia il Credential Issuer che l'Authorization Server,
  DEVE incorporare sia
  ``oauth_authorization_server`` che ``openid_credential_issuer`` all'interno dei suoi tipi di metadati.
  Altre implementazioni possono dividere il Credential Issuer dall'Authorization Server, quando ciò accade i metadati del Credential Issuer DEVONO contenere i parametri `authorization_servers`, incluso l'identificatore unico dell'Authorization Server.
  Inoltre, qualora ci fosse la necessità di Autenticazione dell'Utente da parte del Credential Issuer,
  potrebbe essere necessario includere il tipo di metadati pertinente, sia ``openid_relying_party``
  che ``openid_credential_verifier``.


Metadati delle Foglie federation_entity
---------------------------------------

I metadati *federation_entity* per le Foglie DEVONO contenere i seguenti claim.


.. list-table::
  :class: longtable
  :widths: 20 60
  :header-rows: 1

  * - **Claim**
    - **Descrizione**
  * - **organization_name**
    - Vedi `OID-FED`_ Draft 41 Sezione 5.2.2
  * - **homepage_uri**
    - Vedi `OID-FED`_ Draft 41 Sezione 5.2.2
  * - **policy_uri**
    - Vedi `OID-FED`_ Draft 41 Sezione 5.2.2
  * - **logo_uri**
    - URL del logo dell'entità; DEVE essere in formato SVG. Vedi `OID-FED`_ Draft 36 Sezione 5.2.2
  * - **contacts**
    - Indirizzo email certificato istituzionale (PEC) dell'entità. Vedi `OID-FED`_ Draft 36 Sezione 5.2.2
  * - **federation_resolve_endpoint**
    - Vedi `OID-FED`_ Draft 41 Sezione 5.1.1


Subordinate Statements
----------------------

Trust Anchor e Intermediari pubblicano Subordinate Statement relativi ai loro Subordinati immediati.
Il Subordinate Statement PUÒ contenere una policy di metadati e i Trust Mark relativi a un Subordinato.

La policy di metadati, quando applicata, apporta una o più modifiche ai metadati finali della Foglia. I metadati finali di una Foglia derivano dalla Trust Chain che contiene tutte le dichiarazioni, a partire dall'Entity Configuration fino al Subordinate Statement emesso dal Trust Anchor.

Trust Anchor e Intermediari DEVONO esporre l'endpoint Federation Fetch, dove i Subordinate Statement sono richiesti per convalidare la firma dell'Entity Configuration della Foglia.

.. note::
  L'endpoint Federation Fetch PUÒ anche pubblicare certificati X.509 per ciascuna delle chiavi pubbliche del Subordinato. Rendendo la distribuzione dei certificati X.509 emessi tramite un servizio RESTful.

Di seguito c'è un esempio non normativo di un Subordinate Statement emesso da un Organismo di Registrazione (come il Trust Anchor o il suo Intermediario) in relazione a uno dei suoi Subordinati.

.. code-block:: text

    {
        "alg": "ES256",
        "kid": "em3cmnZgHIYFsQ090N6B3Op7LAAqj8rghMhxGmJstqg",
        "typ": "entity-statement+jwt"
    }
    .
    {
        "exp": 1649623546,
        "iat": 1649450746,
        "iss": "https://intermediate.example.org",
        "sub": "https://rp.example.it",
        "jwks": {
            "keys": [
                {
                    "kty": "EC",
                    "kid": "2HnoFS3YnC9tjiCaivhWLVUJ3AxwGGz_98uRFaqMEEs",
                    "crv": "P-256",
                    "x": "1kNR9Ar3MzMokYTY8BRvRIue85NIXrYX4XD3K4JW7vI",
                    "y": "slT14644zbYXYF-xmw7aPdlbMuw3T1URwI4nafMtKrY",
                    "x5c": [ <X.509 certificate> ]
                }
            ]
        },
        "metadata_policy": {
            "openid_credential_verifier": {
                "scope": {
                    "subset_of": [
                         "eu.europa.ec.eudiw.pid.1",
                         "given_name",
                         "family_name",
                         "email"
                      ]
                },
                "vp_formats": {
                    "dc+sd-jwt": {
                        "sd-jwt_alg_values": [
                            "ES256",
                            "ES384"
                        ],
                        "kb-jwt_alg_values": [
                            "ES256",
                            "ES384"
                        ]
                    }
                }
            }
         }
    }


.. note::
  **Firma del Subordinate Statement**

  Le stesse considerazioni e requisiti fatti per l'Entity Configuration
  e in relazione ai meccanismi di firma DEVONO essere applicati per i Subordinate Statement.


Subordinate Statement
^^^^^^^^^^^^^^^^^^^^^

Il Subordinate Statement emesso da Trust Anchor e Intermediari contiene i seguenti attributi:

.. list-table::
   :class: longtable
   :widths: 20 60 20
   :header-rows: 1

   * - **Claim**
     - **Descrizione**
     - **Richiesto**
   * - **iss**
     - Vedi `OID-FED`_ Sezione 3 per ulteriori dettagli.
     - |check-icon|
   * - **sub**
     - Vedi `OID-FED`_ Sezione 3 per ulteriori dettagli.
     - |check-icon|
   * - **iat**
     - Vedi `OID-FED`_ Sezione 3 per ulteriori dettagli.
     - |check-icon|
   * - **exp**
     - Vedi `OID-FED`_ Sezione 3 per ulteriori dettagli.
     - |check-icon|
   * - **jwks**
     - JWKS di Federazione dell'entità *sub*. Vedi `OID-FED`_ Sezione 3 per ulteriori dettagli.
     - |check-icon|
   * - **metadata_policy**
     - Oggetto JSON che descrive la policy dei Metadati. Ogni chiave dell'Oggetto JSON rappresenta un identificatore del tipo di metadati e ogni valore DEVE essere un Oggetto JSON che rappresenta la policy dei metadati secondo quel tipo di metadati. Si prega di fare riferimento alle specifiche `OID-FED`_, Sezione 6.1, per i dettagli di implementazione.
     - |uncheck-icon|
   * - **trust_marks**
     - Array JSON contenente i Trust Mark emessi da se stesso per il soggetto subordinato.
     - |uncheck-icon|
   * - **constraints**
     - PUÒ contenere gli **allowed_leaf_entity_types**, che limita quali tipi di metadati il soggetto è autorizzato a pubblicare. PUÒ contenere il numero massimo di Intermediari consentiti tra se stesso e la Foglia (**max_path_length**)
     - |check-icon|


Meccanismo di Valutazione della Fiducia
---------------------------------------

I Trust Anchor DEVONO distribuire le loro Chiavi Pubbliche di Federazione attraverso meccanismi sicuri fuori banda, come la pubblicazione su una pagina web verificata o l'archiviazione in un repository remoto come parte di una lista di fiducia. La logica alla base di questo requisito è che affidarsi esclusivamente ai dati forniti all'interno dell'Entity Configuration del Trust Anchor non mitiga adeguatamente i rischi associati agli attacchi di manipolazione DNS e TLS. Per garantire la sicurezza, tutti i partecipanti DEVONO ottenere le chiavi pubbliche del Trust Anchor utilizzando questi metodi fuori banda. Dovrebbero quindi confrontare queste chiavi con quelle ottenute dall'Entity Configuration del Trust Anchor, scartando qualsiasi chiave che non corrisponda. Questo processo aiuta a garantire l'integrità e l'autenticità delle chiavi pubbliche del Trust Anchor e la sicurezza complessiva della federazione.

Il Trust Anchor pubblica l'elenco dei suoi Subordinati (endpoint Federation Subordinate Listing) e le attestazioni dei loro metadati e chiavi pubbliche (Subordinate Statement).

Ogni partecipante, inclusi Trust Anchor, Intermediario, Credential Issuer, Fornitore di Wallet e Relying Party, pubblica i propri metadati e chiavi pubbliche (endpoint Entity Configuration) nella risorsa web nota **.well-known/openid-federation**.

Ciascuno di questi può essere verificato utilizzando il Subordinate Statement emesso da un superiore, come il Trust Anchor o un Intermediario.

Ogni Subordinate Statement è verificabile nel tempo e DEVE avere una data di scadenza. La revoca di ogni dichiarazione è verificabile in tempo reale e online (solo per flussi remoti) attraverso gli endpoint della federazione.

.. note::
  La revoca di un'Entità avviene con l'indisponibilità del Subordinate Statement ad essa relativo. Se il Trust Anchor o il suo Intermediario non pubblica un Subordinate Statement valido, o se pubblica un Subordinate Statement scaduto/non valido, il soggetto del Subordinate Statement DEVE essere inteso come non valido o revocato.

La concatenazione delle dichiarazioni, attraverso la combinazione di questi meccanismi di firma e il vincolo di claim e chiavi pubbliche, forma la Trust Chain.

Le Trust Chain possono anche essere verificate offline, utilizzando una delle chiavi pubbliche del Trust Anchor.

.. note::
  Poiché l'Istanza del Wallet non è un'Entità di Federazione, il Meccanismo di Valutazione della Fiducia ad essa relativo **richiede la presentazione del Wallet Attestation durante le fasi di emissione e presentazione delle Credenziali**.

  Il Wallet Attestation trasmette tutte le informazioni richieste relative all'istanza, come la sua chiave pubblica e qualsiasi altra informazione tecnica o amministrativa, senza alcun dato personale dell'Utente.


Stabilire la Fiducia con i Credential Issuer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Nel processo di emissione, la Valutazione della Fiducia garantisce l'integrità e l'autenticità delle Credenziali emesse e l'affidabilità dei loro Emittenti. Questa sezione delinea i meccanismi di Valutazione della Fiducia distinti dai flussi di protocollo, implementati dalle Istanze del Wallet e dalle Relying Party, come descritto nella sezione dedicata.

Le Valutazioni della Fiducia implementano diversi modi, come definito di seguito:

* **Scoperta dell'Entità di Federazione**: le Istanze del Wallet e le Relying Party DEVONO verificare l'identità dell'Emittente attraverso un processo di Scoperta dell'Entità di Federazione. Ciò comporta l'interrogazione di una Trusted List o directory per confermare lo stato di validità dell'Emittente e la conformità al Trust Framework.

* **Trust Chain**: le Istanze del Wallet e le Relying Party valutano le Trust Chain dell'Emittente, che possono essere fornite staticamente o costruite attraverso un processo di Scoperta dell'Entità di Federazione, per garantire che l'entità che richiede la Credenziale faccia parte di una federazione riconosciuta e fidata. Ciò comporta il controllo della Trust Chain dall'autorità root all'Emittente.

* **Valutazione dei Trust Mark**: i Trust Mark vengono valutati per garantire la continua conformità alle politiche della federazione. Questi marchi indicano l'aderenza a specifici standard e pratiche richiesti dalla federazione.

* **Valutazione delle Policy**: le Istanze del Wallet e le Relying Party DEVONO verificare che il Credential Issuer sia autorizzato all'emissione della Credenziale di loro interesse. Metadati, policy di metadati e Trust Mark sono utilizzati per l'implementazione di questi controlli.

Nel processo rappresentato nel diagramma di sequenza seguente, l'Istanza del Wallet utilizza l'API della Federazione per scoprire e raccogliere tutti i Credential Issuer abilitati all'interno della federazione. Il processo di scoperta produce la Trust Chain. Quando la Trust Chain viene fornita staticamente all'interno di una richiesta firmata o di una Credenziale, RICHIEDE di essere aggiornata solo quando la connessione internet è disponibile, mentre DEVE essere aggiornata quando la Trust Chain fornita staticamente risulta scaduta.

.. plantuml:: plantuml/trust-evaluation-flow.puml
    :width: 99%
    :alt: La figura illustra il Processo di Valutazione della Fiducia.
    :caption: `Processo di Valutazione della Fiducia. <https://www.plantuml.com/plantuml/svg/fPE_Rjmm38TtFGMHfTCrUuOWXwlJ6bs2fd-MB8n5nqHbIg2ek-JjwxFW9XUSkzIJ87_y-AD1tsH3jJ86-Aub6pHx30MDey2TnevoTWdLkEE4Ol0BGo0xkTgrW1akTagUn1W3j3aNqeiJgcrcgXKZ7Sap6btMZblfXZZHhhfXStqzEQ_WbgmRfjE738qOsmlielJyL7IEzo201XyF5CBcjyI3NCP4mdxJawUA08bFaSNShfsrjSCLV2ChAcUrIumJldasnMwAMco8Ugpvmc8PUerZJVZE4M9Cq4S5mcvuL-PWUjuqQPjbrlyUSzLyNnwZUXOqWdj3ev74ghe_0gkAvGlynC3-M6q3GLBQSomPygkgP9Qd-Utjts3BG5_f9Jz8qhXdJnvOZjpvJ8x4E_Ul07LfTWEoE8V1eEtVtW7doWAAXnz2pucL_CfSTSV9mu5jgCbFTvz2fhNQxPJV5h8Q6jMegpDiKmfC6UvYu6uwd6C-aVAUwbBrB1XW94EFXkVepsI0U-I0Zu7WzHVCC07nG7vUGiwve7JaRaXy6SCV>`_


.. .. figure:: ../../images/trust-with-ci-discovery.svg
..     :figwidth: 100%
..     :align: center
..     :target: //www.plantuml.com/plantuml/svg/fPCzRzim48Pt_ef3bavkzWn13DTfXIv1quyboqKynOTIH-9uj9D_NqQ46hkmkaGJGJtty7q5wYORgfKnk8Hgt7D2CVY58P2TR6qwm0mN6oLFOem1kfmBwSK9rMqdgXCZ7Sap6br-rv8DrjBlOgLTSyFg-hewh-2MhD_LrOSCs-gr5zX46VYfA1f7UH10Wuy72c7rM-91BcCYORyQo5D3WCIdo69kqqtQTi8LV2ChAcUr9p5cVljiYdsDMgn6VPtvKgqP1erZI_YF8yIOO8WAXBN3wPY3-XmTqctdhk-jkMo-BuzHFGiQmRsXqKXYJJrCm99Y_W8_CR1_dROTGLBQSomPyfkgP9QdwUtjts1peQ_qaXyaQTop9myi4tSsaoFnplqlGBiqcnsoE8V1e1kEzu1pOm75mm-XvyHAVgdNdSQUoCE1RNUKlEtdx2XaMffTr_msaysmLOsws66TKc3AS1S3ztLnZlb4odjgbsfWmG0Z6NeqF4T_9WFS8mTy30Hlls262iG3-UaISiu5fITtG-BB6Fu0

.. note::
  Come mostrato nella figura, il processo di Valutazione della Fiducia è completamente separato e distinto dal flusso specifico del protocollo. Opera in un flusso diverso e utilizza protocolli specializzati progettati specificamente per questo scopo.

Stabilire la Fiducia con la Relying Party
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Nel contesto della valutazione delle Relying Party, la responsabilità della Valutazione della Fiducia spetta esclusivamente all'Istanza del Wallet.
I meccanismi di Valutazione della Fiducia sono distinti dai flussi di protocollo e sono implementati dall'Istanza del Wallet, come dettagliato nella sezione dedicata.

Le Valutazioni della Fiducia sono condotte come segue:

* **Scoperta dell'Entità di Federazione**: Quando l'Istanza del Wallet riceve una richiesta firmata emessa da una Relying Party, l'Istanza del Wallet DEVE verificare l'identità della Relying Party attraverso un processo di Scoperta dell'Entità di Federazione. Ciò comporta l'interrogazione di una Trusted List o directory per confermare lo stato di validità della Relying Party e la conformità al Trust Framework e la valutazione della firma della richiesta utilizzando il materiale crittografico ottenuto dalla Trust Chain.

* **Trust Chain**: L'Istanza del Wallet valuta le Trust Chain della Relying Party, che possono essere fornite staticamente o costruite attraverso un processo di Scoperta dell'Entità di Federazione, per garantire che la Relying Party faccia parte di una federazione riconosciuta e fidata. Ciò comporta il controllo della Trust Chain dall'autorità root (Trust Anchor) alla Relying Party.

* **Valutazione dei Trust Mark**: i Trust Mark vengono valutati per garantire la continua conformità alle politiche della federazione. Questi marchi indicano l'aderenza a specifici standard e pratiche richiesti dalla federazione. Le Relying Party POSSONO includere Trust Mark nella loro Entity Configuration per segnalare proprietà amministrative e conformità a profili specifici, come le concessioni nell'interazione con utenti minorenni.

* **Valutazione delle Policy**: L'Istanza del Wallet DEVE verificare che la Relying Party sia autorizzata a richiedere la Credenziale di interesse. Metadati, policy di metadati e Trust Mark sono utilizzati per implementare questi controlli.

Nel processo illustrato nel diagramma di sequenza seguente, l'Istanza del Wallet utilizza l'API della Federazione per scoprire e raccogliere tutte le Relying Party abilitate all'interno della federazione. Il processo di scoperta produce la Trust Chain. Quando la Trust Chain viene fornita staticamente all'interno di una richiesta firmata, deve essere aggiornata solo quando è disponibile una connessione internet, ma DEVE essere aggiornata se la Trust Chain fornita staticamente è scaduta.

.. plantuml:: plantuml/trust-rp-discovery-flow.puml
    :width: 99%
    :alt: La figura illustra il Processo di Scoperta della Relying Party.
    :caption: `Valutazione della Fiducia - Processo di Scoperta della Relying Party. <https://www.plantuml.com/plantuml/svg/ZLDFRzi-3BtxKn2z_4xvzTv3qQ1_i64x16dNNGeKgaGdH6NAawYq_lPZvBbD33Tm3ev5Fpw-Hv5NIKoKt7XOe--8Dx3ISmStb6pOOUogLizagJKiyDjuZ_ATDOajWabmreTWY9qTuQyV2-Q8-XZni2o8XvYJm9BjDaGuLpR1sA0Z8yfOZSekBY-L-G8Y_iceQGRQ60IjeDDO2ZbQhBJqGe4ZoHUGQCEAin4Tif3ncen9NurGu85pikQOog4D3i6m0zmPdrLi0jdY9qbblBQcXjxUzTOG0wMzt1qvLV56iYK-p2bi781OC38AsC2CTg-j0ltDaAN_GbQ37QWgSYghL3WKaTF-FWwx_f_AoY-UBBnYbohq2Vk2qxs_Gx5RMAyqxPQ5f8Fhm3LjSYnzV68m0l-_eVUBLmvlV1vQP7AB6Xr6CzXHgaaBQvGSUPAvEgNgzbsYiMefYrhQvtuZbWHr34qHE-8w8M7Ltz6OgY_lGsYX3X7GsEq8KW1VQ7nO3fsRigOGsA30Pu-UwptusRG4lzO_1sQbcPJSCz_dbn0TiH64Uz5dWwT5ZMaU3uUcZRYZa1EaWUg9o_2KhtSVIWT3Fx1BJ_mnuFrmdz24xAggFEOhEnhbhtQiZ7xPfiputb94DtU1zEej_jlEGuibdlhTcCkrLECoPFQCjp66EDlpicqzOO9Ly6JrPKxE3KRQOJ_mDR7nqA0OPyHKLretD_ul>`_


.. .. figure:: ../../images/trust-with-rp-discovery.svg
..     :figwidth: 100%
..     :align: center
..     :target: //www.plantuml.com/plantuml/uml/ZLEnRXin3DtlAuWidTpi6O8OQOeMxM0uQRe421Y9PnEHgQj4EV7VbpxX6jku6kVXP52FZ-zHv4rMJ5eseUdiPCSTYi9l387qkzYbE0BCS553CCGkZl2tZprcIM77ieA5NUsE4G_p7l6GIbQOYrl719V6ffGsv1dL69kJihFhQsE-WaH_2baQGfUYabFo5ikn94UDbPuPy4Jo5MHUYU5S8a-YZC6IAPCeAaSPE4Thdb9vSj4Je7YWBOQ2IXbqJHya3GPhJGlLtkqQMO3pNkwMFNbuOrsp7ERqR1A1HIa9ARWeGcwlhG7xJP1bfxApu0vC5NjKwYiSYYXv_nw7NVzaiifBO0UljCiDXKpZ1MlllvAwDImNbdOdohg3soWjhqhg-_WaW0gVtoY4sQl4DxcC7GdxMKkU4WvsZ6hKmfAq91bbRiwfkdlNXCui5JLB-znlB9gXJN5JnHvpdP6mg6zqIbNBXnWxQ6C2GhS-WVI0SOqsxKFdngmP15QayD6ZvtOFViQEuTVovy1iDAEIA_DzUOd9iw0ItAjzDtHUr2dDu-7GT8cs74k6F50zIHqUkxMAWzB1q0_QvIVvD-1rkCze8l5Dqt-cApiQvV_iM1tzVfkAq7l7YVpK1RAdTqHrEmyirdYkkp6LQsx6TSYiZ7SfnJJPyxph0bE6HGpixC-Kd2-KU4jru5iM3B0XHO-ApGs9Bvlm5m00

.. note::
  Come mostrato nella figura, la connessione internet è necessaria per aggiornare la Trust Chain relativa a una RP e verificarne lo stato di revoca.

Valutazione della Fiducia con i Wallet
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Il Fornitore di Wallet emette il Wallet Attestation, certificando lo stato operativo delle sue Istanze del Wallet e includendo una delle loro chiavi pubbliche.

Il Wallet Attestation PUÒ contenere la Trust Chain che attesta l'affidabilità del suo emittente (Fornitore di Wallet) al momento dell'emissione.

L'Istanza del Wallet fornisce il suo Wallet Attestation all'interno della richiesta firmata durante la fase di emissione del PID. Il Credential Issuer DEVE valutare la Trust Chain relativa all'emittente del Wallet Attestation (formalmente, il Fornitore di Wallet).


Trust Chain
^^^^^^^^^^^

La Trust Chain è una sequenza di dichiarazioni verificate che convalida la conformità di un partecipante alla Federazione. Ha una data e ora di scadenza, oltre la quale DEVE essere rinnovata per ottenere i metadati freschi e aggiornati. La data di scadenza della Trust Chain è determinata dal timestamp di scadenza più recente tra tutti i timestamp di scadenza contenuti nelle dichiarazioni. Nessuna Entità può forzare la data di scadenza della Trust Chain ad essere superiore a quella configurata dal Trust Anchor.

Di seguito è riportata una rappresentazione astratta di una Trust Chain.

.. code-block:: python

    [
        "EntityConfiguration-as-SignedJWT-selfissued-byLeaf",
        "EntityStatement-as-SignedJWT-issued-byTrustAnchor"
    ]

Di seguito è riportato un esempio non normativo di una Trust Chain, composta da un Array JSON contenente JWT, con un Intermediario coinvolto.

.. code-block:: python

    [
      "eyJhbGciOiJFUzI1NiIsImtpZCI6Ik5GTTFXVVZpVWxZelVXcExhbWxmY0VwUFJWWTJWWFpJUmpCblFYWm1SSGhLWVVWWVVsZFRRbkEyTkEiLCJ0eXAiOiJhcHBsaWNhdGlvbi9lbnRpdHktc3RhdGVtZW50K2p3dCJ9.eyJleHAiOjE2NDk1OTA2MDIsImlhdCI6MTY0OTQxNzg2MiwiaXNzIjoiaHR0cHM6Ly9ycC5leGFtcGxlLm9yZyIsInN1YiI6Imh0dHBzOi8vcnAuZXhhbXBsZS5vcmciLCJqd2tzIjp7ImtleXMiOlt7Imt0eSI6IkVDIiwia2lkIjoiTkZNMVdVVmlVbFl6VVdwTGFtbGZjRXBQUlZZMlZYWklSakJuUVhabVJIaEtZVVZZVWxkVFFuQTJOQSIsImNydiI6IlAtMjU2IiwieCI6InVzbEMzd2QtcFgzd3o0YlJZbnd5M2x6cGJHWkZoTjk2aEwyQUhBM01RNlkiLCJ5IjoiVkxDQlhGV2xkTlNOSXo4a0gyOXZMUjROMThCa3dHT1gyNnpRb3J1UTFNNCJ9XX0sIm1ldGFkYXRhIjp7Im9wZW5pZF9yZWx5aW5nX3BhcnR5Ijp7ImFwcGxpY2F0aW9uX3R5cGUiOiJ3ZWIiLCJjbGllbnRfaWQiOiJodHRwczovL3JwLmV4YW1wbGUub3JnLyIsImNsaWVudF9yZWdpc3RyYXRpb25fdHlwZXMiOlsiYXV0b21hdGljIl0sImp3a3MiOnsia2V5cyI6W3sia3R5IjoiRUMiLCJraWQiOiJORk0xV1VWaVVsWXpVV3BMYW1sZmNFcFBSVlkyVlhaSVJqQm5RWFptUkhoS1lVVllVbGRUUW5BMk5BIiwiY3J2IjoiUC0yNTYiLCJ4IjoidXNsQzN3ZC1wWDN3ejRiUllud3kzbHpwYkdaRmhOOTZoTDJBSEEzTVE2WSIsInkiOiJWTENCWEZXbGROU05JejhrSDI5dkxSNE4xOEJrd0dPWDI2elFvcnVRMU00In1dfSwiY2xpZW50X25hbWUiOiJOYW1lIG9mIGFuIGV4YW1wbGUgb3JnYW5pemF0aW9uIiwiY29udGFjdHMiOlsib3BzQHJwLmV4YW1wbGUuaXQiXSwiZ3JhbnRfdHlwZXMiOlsicmVmcmVzaF90b2tlbiIsImF1dGhvcml6YXRpb25fY29kZSJdLCJyZWRpcmVjdF91cmlzIjpbImh0dHBzOi8vcnAuZXhhbXBsZS5vcmcvb2lkYy9ycC9jYWxsYmFjay8iXSwicmVzcG9uc2VfdHlwZXMiOlsiY29kZSJdLCJzY29wZSI6ImV1LmV1cm9wYS5lYy5ldWRpdy5waWQuMSBldS5ldXJvcGEuZWMuZXVkaXcucGlkLml0LjEgZW1haWwiLCJzdWJqZWN0X3R5cGUiOiJwYWlyd2lzZSJ9LCJmZWRlcmF0aW9uX2VudGl0eSI6eyJmZWRlcmF0aW9uX3Jlc29sdmVfZW5kcG9pbnQiOiJodHRwczovL3JwLmV4YW1wbGUub3JnL3Jlc29sdmUvIiwib3JnYW5pemF0aW9uX25hbWUiOiJFeGFtcGxlIFJQIiwiaG9tZXBhZ2VfdXJpIjoiaHR0cHM6Ly9ycC5leGFtcGxlLml0IiwicG9saWN5X3VyaSI6Imh0dHBzOi8vcnAuZXhhbXBsZS5pdC9wb2xpY3kiLCJsb2dvX3VyaSI6Imh0dHBzOi8vcnAuZXhhbXBsZS5pdC9zdGF0aWMvbG9nby5zdmciLCJjb250YWN0cyI6WyJ0ZWNoQGV4YW1wbGUuaXQiXX19LCJ0cnVzdF9tYXJrcyI6W3siaWQiOiJodHRwczovL3JlZ2lzdHJ5LmVpZGFzLnRydXN0LWFuY2hvci5leGFtcGxlLmV1L29wZW5pZF9yZWx5aW5nX3BhcnR5L3B1YmxpYy8iLCJ0cnVzdF9tYXJrIjoiZXlKaCBcdTIwMjYifV0sImF1dGhvcml0eV9oaW50cyI6WyJodHRwczovL2ludGVybWVkaWF0ZS5laWRhcy5leGFtcGxlLm9yZyJdfQ.Un315HdckvhYA-iRregZAmL7pnfjQH2APz82blQO5S0sl1JR0TEFp5E1T913g8GnuwgGtMQUqHPZwV6BvTLA8g",
      "eyJhbGciOiJFUzI1NiIsImtpZCI6IlNURkRXV2hKY0dWWFgzQjNSVmRaYWtsQ0xUTnVNa000WTNGNlFUTk9kRXRyZFhGWVlYWjJjWGN0UVEiLCJ0eXAiOiJhcHBsaWNhdGlvbi9lbnRpdHktc3RhdGVtZW50K2p3dCJ9.eyJleHAiOjE2NDk2MjM1NDYsImlhdCI6MTY0OTQ1MDc0NiwiaXNzIjoiaHR0cHM6Ly9pbnRlcm1lZGlhdGUuZWlkYXMuZXhhbXBsZS5vcmciLCJzdWIiOiJodHRwczovL3JwLmV4YW1wbGUub3JnIiwiandrcyI6eyJrZXlzIjpbeyJrdHkiOiJFQyIsImtpZCI6Ik5GTTFXVVZpVWxZelVXcExhbWxmY0VwUFJWWTJWWFpJUmpCblFYWm1SSGhLWVVWWVVsZFRRbkEyTkEiLCJjcnYiOiJQLTI1NiIsIngiOiJ1c2xDM3dkLXBYM3d6NGJSWW53eTNsenBiR1pGaE45NmhMMkFIQTNNUTZZIiwieSI6IlZMQ0JYRldsZE5TTkl6OGtIMjl2TFI0TjE4Qmt3R09YMjZ6UW9ydVExTTQifV19LCJtZXRhZGF0YV9wb2xpY3kiOnsib3BlbmlkX3JlbHlpbmdfcGFydHkiOnsic2NvcGUiOnsic3Vic2V0X29mIjpbImV1LmV1cm9wYS5lYy5ldWRpdy5waWQuMSwgIGV1LmV1cm9wYS5lYy5ldWRpdy5waWQuaXQuMSJdfSwicmVxdWVzdF9hdXRoZW50aWNhdGlvbl9tZXRob2RzX3N1cHBvcnRlZCI6eyJvbmVfb2YiOlsicmVxdWVzdF9vYmplY3QiXX0sInJlcXVlc3RfYXV0aGVudGljYXRpb25fc2lnbmluZ19hbGdfdmFsdWVzX3N1cHBvcnRlZCI6eyJzdWJzZXRfb2YiOlsiUlMyNTYiLCJSUzUxMiIsIkVTMjU2IiwiRVM1MTIiLCJQUzI1NiIsIlBTNTEyIl19fX0sInRydXN0X21hcmtzIjpbeyJpZCI6Imh0dHBzOi8vdHJ1c3QtYW5jaG9yLmV4YW1wbGUuZXUvb3BlbmlkX3JlbHlpbmdfcGFydHkvcHVibGljLyIsInRydXN0X21hcmsiOiJleUpoYiBcdTIwMjYifV19._qt5-T6DahP3TuWa_27klE8I9Z_sPK2FtQlKY6pGMPchbSI2aHXY3aAXDUrObPo4CHtqgg3J2XcrghDFUCFGEQ",
      "eyJhbGciOiJFUzI1NiIsImtpZCI6ImVXa3pUbWt0WW5kblZHMWxhMjU1ZDJkQ2RVZERSazQwUWt0WVlVMWFhRFZYT1RobFpHdFdXSGQ1WnciLCJ0eXAiOiJhcHBsaWNhdGlvbi9lbnRpdHktc3RhdGVtZW50K2p3dCJ9.eyJleHAiOjE2NDk2MjM1NDYsImlhdCI6MTY0OTQ1MDc0NiwiaXNzIjoiaHR0cHM6Ly90cnVzdC1hbmNob3IuZXhhbXBsZS5ldSIsInN1YiI6Imh0dHBzOi8vaW50ZXJtZWRpYXRlLmVpZGFzLmV4YW1wbGUub3JnIiwiandrcyI6eyJrZXlzIjpbeyJrdHkiOiJFQyIsImtpZCI6IlNURkRXV2hKY0dWWFgzQjNSVmRaYWtsQ0xUTnVNa000WTNGNlFUTk9kRXRyZFhGWVlYWjJjWGN0UVEiLCJjcnYiOiJQLTI1NiIsIngiOiJyQl9BOGdCUnh5NjhVTkxZRkZLR0ZMR2VmWU5XYmgtSzh1OS1GYlQyZkZJIiwieSI6IlNuWVk2Y3NjZnkxcjBISFhLTGJuVFZsamFndzhOZzNRUEs2WFVoc2UzdkUifV19LCJ0cnVzdF9tYXJrcyI6W3siaWQiOiJodHRwczovL3RydXN0LWFuY2hvci5leGFtcGxlLmV1L2ZlZGVyYXRpb25fZW50aXR5L3RoYXQtcHJvZmlsZSIsInRydXN0X21hcmsiOiJleUpoYiBcdTIwMjYifV19.r3uoi-U0tx0gDFlnDdITbcwZNUpy7M2tnh08jlD-Ej9vMzWMCXOCCuwIn0ZT0jS4M_sHneiG6tLxRqj-htI70g"
    ]


.. note::
  L'intera Trust Chain è verificabile possedendo solo le chiavi pubbliche del Trust Anchor.

Ci sono eventi in cui le chiavi non sono disponibili per verificare l'intera trust chain:

 - **Cambio di Chiave da parte del Credential Issuer**: Il Credential Issuer PUÒ aggiornare le sue chiavi crittografiche. Le chiavi crittografiche DEVONO essere considerate valide se valutate all'interno del loro periodo di validità originariamente designato a meno che un motivo di sicurezza non le renda inutilizzabili. Il motivo della revoca DEVE essere pubblicato. Le chiavi crittografiche storiche, cioè le chiavi crittografiche pubbliche inutilizzate o revocate, DEVONO essere pubblicate utilizzando l'Endpoint Federation Historical Keys.

 - **Modifica nei Tipi di Credenziali**: Se il Credential Issuer modifica i **tipi** di Credenziali emesse, ad esempio decidendo di non emettere più uno o più tipi di Credenziali, le relative chiavi crittografiche pubbliche DEVONO essere disponibili per il periodo di validità originariamente designato.

 - **Fusione di Credential Issuer**: Se un Credential Issuer si fonde con un altro, creando una nuova Entità Organizzativa o lavorando per conto di un'altra utilizzando un hostname o dominio diverso, la configurazione della federazione **precedentemente** disponibile e le chiavi storiche DEVONO essere mantenute disponibili agli endpoint well-known originali del Credential Issuer.

 - **Il Credential Issuer diventa inattivo**: Se un Credential Issuer diventa inattivo, la sua Entity Configuration **correlata** e l'Endpoint Federation Historical Entity DEVONO essere mantenuti disponibili.

Meccanismi di Attestazione della Fiducia Offline
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

I flussi offline non consentono la valutazione in tempo reale dello stato di un'Entità, come la sua revoca. Allo stesso tempo, l'utilizzo di Trust Chain di breve durata consente il raggiungimento di attestazioni di fiducia compatibili con i protocolli amministrativi di revoca richiesti (ad esempio, una revoca deve essere propagata in meno di 24 ore, quindi la Trust Chain non deve essere valida per più di quel periodo).


Attestazione della Fiducia del Wallet Offline
"""""""""""""""""""""""""""""""""""""""""""""

Dato che l'Istanza del Wallet non può pubblicare i suoi metadati online all'endpoint *.well-known/openid-federation*,
DEVE ottenere un Wallet Attestation emesso dal suo Fornitore di Wallet. Il Wallet Attestation DEVE contenere tutte le informazioni rilevanti riguardanti le capacità di sicurezza dell'Istanza del Wallet e la sua configurazione relativa al protocollo. DOVREBBE contenere la Trust Chain relativa al suo emittente (Fornitore di Wallet).


Metadati Offline della Relying Party
""""""""""""""""""""""""""""""""""""

Poiché la Scoperta dell'Entità di Federazione è applicabile solo in scenari online, è possibile includere la Trust Chain nelle richieste di presentazione che la Relying Party può emettere per un'Istanza del Wallet.

La Relying Party DEVE firmare la richiesta di presentazione, la richiesta DOVREBBE includere il claim `trust_chain` nei parametri dell'intestazione JWT, contenente la Trust Chain della Federazione relativa a se stessa.

L'Istanza del Wallet che verifica la richiesta emessa dalla Relying Party DEVE utilizzare le chiavi pubbliche del Trust Anchor per convalidare l'intera Trust Chain relativa alla Relying Party prima di attestarne l'affidabilità.

Inoltre, l'Istanza del Wallet applica la policy dei metadati, se presente.

Rinnovo Rapido della Trust Chain
--------------------------------

Il metodo di rinnovo rapido della Trust Chain offre un modo semplificato per mantenere la validità di una trust chain senza dover sottoporre nuovamente l'intero processo di scoperta.
È particolarmente utile per aggiornare rapidamente le Relazioni di Trust quando si verificano modifiche minori o quando la
Trust Chain è vicina alla scadenza ma la struttura complessiva della federazione non è cambiata in modo significativo.

Il processo di rinnovo rapido della Trust Chain viene avviato recuperando nuovamente l'Entity Configuration della foglia. Tuttavia, a differenza del processo di scoperta della federazione che può comportare il recupero delle Entity Configuration a partire dagli authority hints, il rinnovo rapido si concentra sull'ottenimento diretto dei Subordinate Statement. Queste dichiarazioni vengono richieste utilizzando il `source_endpoint` fornito al loro interno, che indica la posizione in cui le dichiarazioni possono essere recuperate.


Non-ripudiabilità delle Attestazioni di Lunga Durata
----------------------------------------------------

Il Trust Anchor e il suo Intermediario DEVONO esporre l'endpoint Federation Historical Keys, dove sono pubblicate tutte le parti pubbliche delle Chiavi dell'Entità di Federazione che non sono più utilizzate, sia scadute che revocate.

I dettagli di questo endpoint sono definiti nella Sezione 8.7 di `OID-FED`_.

Ogni JWT contenente una Trust Chain nelle intestazioni JWT può essere verificato nel tempo, poiché l'intera Trust Chain è verificabile utilizzando la chiave pubblica del Trust Anchor.

Anche se il Trust Anchor ha cambiato le sue chiavi crittografiche per la firma digitale, l'endpoint Federation Historical Keys rende sempre disponibili le chiavi non più utilizzate per le verifiche storiche delle firme.

X.509 PKI
---------

L'Infrastruttura a Chiave Pubblica X.509 (PKI) è un framework progettato per creare, gestire, distribuire, utilizzare, archiviare e revocare Certificati digitali X.509. Al centro della PKI X.509 c'è il concetto di Autorità di Certificazione (CA), che emette certificati digitali alle entità. Questi certificati sono necessari per stabilire comunicazioni sicure sulle reti, incluso internet, abilitando funzionalità di crittografia e firma digitale. La gerarchia PKI tipicamente coinvolge una CA root al vertice, con una o più CA subordinate al di sotto, formando una catena di fiducia. Le entità si affidano a questa catena di fiducia per verificare l'autenticità dei certificati. Gli standard X.509 definiscono il formato dei certificati a chiave pubblica.

L'integrazione di OpenID Federation 1.0 con la tradizionale PKI basata su X.509 (rfc:5280), complementata da un'API RESTful, mira a migliorare l'infrastruttura con funzionalità aggiuntive, rendendola navigabile e trasparente.

Questo approccio sfrutta la natura dinamica e flessibile di OpenID Federation insieme al requisito dei Certificati X.509 per applicazioni legacy e scopi di interoperabilità, mirando ad affrontare le esigenze in evoluzione di verifica dello stato di registrazione dei partecipanti alla federazione, la loro conformità alle regole condivise e la gestione generale e interoperabile della fiducia negli ecosistemi digitali multilaterali.

OpenID Federation e PKI basata su X.509 condividono diverse cose in comune, come elencato di seguito:

- **Approccio Gerarchico**: entrambi utilizzano un Modello di Trust gerarchico con una singola, sovrastante terza parte fidata, nota come Trust Anchor, che è fidata sopra tutte le altre.
- **Decentralizzazione con Multipli Trust Anchor e Intermediari**: nonostante un unico modello gerarchico, la possibilità di avere multipli Trust Anchor e Intermediari, sotto uno o più Trust Anchor, introduce un livello di decentralizzazione.
- **Estensioni Personalizzate**: entrambi i sistemi consentono estensioni personalizzate per soddisfare requisiti specifici o per migliorare la funzionalità. I Certificati X.509 supportano estensioni personalizzate, OpenID Federation consente la definizione di metadati specifici del protocollo personalizzati, Trust Mark e politiche utilizzando un Policy Language.
- **Trust/Certificate Chain**: si basano su una prova a catena di fiducia, dove la fiducia viene trasmessa dall'autorità root (Trust Anchor) attraverso gli Intermediari all'entità finale (Foglia).
- **Vincoli nella Catena**: possono essere applicati vincoli all'interno della Trust Chain riguardanti aspetti critici come la delega della fiducia, il numero di intermediari e i domini coinvolti.
- **Distribuzione della Chiave Pubblica**: Entrambi i sistemi comportano la distribuzione della chiave pubblica del Trust Anchor per garantire che le entità possano verificare la trust chain.
- **Registro delle Chiavi Scadute**: Mantenere un registro delle chiavi scadute è cruciale per entrambi, garantendo la non ripudiabilità delle firme passate anche quando le chiavi cambiano.


Trust Anchor della Federazione e CA X.509
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Nel contesto di OpenID Federation, il Trust Anchor svolge un ruolo simile a quello di un'Autorità di Certificazione (CA) nelle Infrastrutture a Chiave Pubblica (PKI) basate su X.509. Entrambi servono come elementi fondamentali di fiducia all'interno dei rispettivi sistemi. In questo documento, il termine "Trust Anchor" è spesso usato per comprendere entrambi i concetti. L'infrastruttura di fiducia descritta qui allinea il Trust Anchor di OpenID Federation con l'Autorità di Certificazione PKI X.509, rendendoli quindi un'unica entità che supporta sia `RFC 5280`_ che OpenID Federation 1.0.

Emissione di Certificati X.509
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In una OpenID Federation, ogni partecipante è tenuto ad auto-emettere la propria Entity Configuration, firmandola con una delle sue chiavi crittografiche che sono attestate dai Superiori Immediati.

Allo stesso modo, ogni entità di federazione ha l'autonomia di emettere una dichiarazione firmata su se stessa sotto forma di un Certificato X.509.
I partecipanti alla federazione che hanno bisogno di emettere Certificati X.509 su se stessi e per i loro scopi specifici, possono emettere e firmare Certificati X.509 utilizzando una delle loro Chiavi di Entità di Federazione attestate dalle loro Autorità di Federazione (Superiore Immediato). Questo processo allinea l'emissione di Certificati X.509 con il paradigma di delega della federazione.

Questo è fattibile perché il Certificato X.509 può essere verificato utilizzando una Catena di Certificati X.509, simile all'approccio utilizzato per le Entity Configuration in OpenID Federation.

Le Foglie della Federazione non sono Autorità di Certificazione (CA) o intermediari CA autorizzati a emettere certificati X.509 per i loro subordinati. Invece, le Foglie della Federazione agiscono come intermediari per l'emissione di certificati esclusivamente su se stesse. Questo viene realizzato applicando vincoli di denominazione appropriati per garantire che i certificati X.509 siano correttamente delimitati.
I vincoli di denominazione sono applicati dai Superiori Immediati all'interno dei certificati emessi per l'entità Foglia, specificamente riguardanti le Chiavi di Entità di Federazione della Foglia. Di conseguenza, la Foglia può emettere certificati X.509 solo su se stessa, mantenendo così l'integrità della Trust Chain.

Quando un partecipante auto-emette un Certificato X.509, aderisce ai seguenti requisiti:

1. **Nome del Soggetto**: Il nome del soggetto del Certificato X.509 DEVE corrispondere all'identità del partecipante. In particolare, il campo ``Common Name (CN)`` dovrebbe contenere il nome DNS dell'identificatore unico dell'Entità di Federazione, che è incluso nel valore **sub** (soggetto) nella sua Entity Configuration di federazione, rimuovendo ``https://`` e qualsiasi percorso web.
2. **Nome Alternativo del Soggetto (SAN)**: Il Certificato X.509 DEVE includere un ``SAN URI`` che corrisponde al valore **sub** della sua Entity Configuration di federazione.
3. **Nome DNS**: Il Certificato X.509 DEVE includere un Nome DNS nel SAN che corrisponde al nome DNS contenuto nel valore **sub** della sua Entity Configuration, rimuovendo ``https://`` e qualsiasi percorso web.
4. **Lista di Revoca dei Certificati (CRL)**: Se i Certificati X.509 emessi hanno un tempo di scadenza superiore a 24 ore, l'Emittente X.509 DEVE pubblicare una CRL per i Certificati X.509 emessi. Questa lista DEVE essere accessibile e regolarmente aggiornata per garantire che qualsiasi Certificato X.509 compromesso o non valido sia prontamente revocato con la motivazione della revoca, se presente.
5. **Vincoli di Base**: Il Certificato X.509 DEVE includere un'estensione ``Basic Constraints`` con ``CA:TRUE`` e una lunghezza massima del percorso di 1 se l'emittente del certificato è un Intermediario di Federazione, se è una Foglia, la lunghezza massima del percorso DEVE essere impostata a 0. Ciò indica che il Subordinato a cui si riferisce il certificato può emettere Certificati X.509 solo con una profondità di catena limitata.
6. **Vincoli di Nome**: Il Certificato X.509 DEVE includere ``Name Constraints`` per specificare domini e URI consentiti ed esclusi. Ad esempio:

   - Consentiti:
     - ``URI.1=https://leaf.example.com``
     - ``DNS.1=leaf.example.com``
   - Esclusi:
     - ``DNS=localhost``
     - ``DNS=localhost.localdomain``
     - ``DNS=127.0.0.1``
     - ``DNS=example.com``
     - ``DNS=example.org``
     - ``DNS=example.net``
     - ``DNS=*.example.org``

Di seguito è riportato un esempio non normativo, in formato testo semplice (formato OpenSSL), di una catena di certificati X.509 con una CA intermedia, a partire dal certificato Leaf.

.. literalinclude:: ../../examples/x5c.json
  :language: text

I partecipanti alla federazione possono garantire che i loro certificati siano coerenti, consentendo l'interoperabilità e la sicurezza in tutta la federazione. Questo approccio, che consente la delega dell'emissione di certificati X.509, introduce pratiche innovative per la gestione dei certificati utilizzando le Relazioni di Trust sottostanti stabilite all'interno di OpenID Federation.


Revoca del Certificato X.509
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Un Certificato X.509 può essere revocato dal suo Emittente.
Le liste di revoca, e/o qualsiasi altro meccanismo di controllo della revoca, sono richiesti solo per i Certificati X.509 con tempo di scadenza superiore a 24 ore, altrimenti non sono richiesti.

Quando l'emittente del Certificato X.509 è la Foglia e quindi il Certificato X.509 riguarda se stessa, se il tempo di scadenza del certificato è superiore a 24 ore dal tempo ``X509_NOT_VALID_BEFORE``, DEVE implementare una CRL relativa al certificato emesso e mantenerla aggiornata.
Quando l'emittente del Certificato X.509 è un Superiore immediato, come il Trust Anchor o un Intermediario, e revoca il certificato relativo alla Foglia, quindi il Certificato X.509 relativo a una delle Chiavi di Entità di Federazione della Foglia. Questa azione invalida l'intera Trust Chain associata a quella chiave pubblica crittografica della Foglia, rimuovendo efficacemente la sua capacità di emettere ulteriori Certificati X.509 su se stessa. Questo meccanismo di revoca gerarchico garantisce che qualsiasi compromissione o comportamento scorretto da parte di un'entità Foglia possa essere rapidamente affrontato.

Di seguito un esempio non normativo, in testo semplice, che esemplifica il contenuto di una CRL.

.. code-block:: text

    Certificate Revocation List (CRL):
    Version: 2 (0x1)
    Signature Algorithm: sha256WithRSAEncryption
    Issuer: CN=https://leaf.example.org, O=Leaf, C=IT
    Last Update: Sep 1 00:00:00 2023 GMT
    Next Update: Sep 8 00:00:00 2023 GMT
    Revoked Certificates:
        Serial Number: 987654320
            Revocation Date: Aug 25 12:00:00 2023 GMT
            CRL Entry Extensions:
                Reason Code: Key Compromise
        Serial Number: 987654321
            Revocation Date: Aug 30 15:00:00 2023 GMT
            CRL Entry Extensions:
                Reason Code: Cessation of Operation
    Signature Algorithm: sha256WithRSAEncryption
    Signature:
        5c:4f:3b:...

Utilizzando il livello sottostante stabilito con OpenID Federation 1.0, tutti i certificati X.509 sono emessi in modo adeguatamente decentralizzato utilizzando il pattern di delega.


Note sulla Privacy
------------------

- Le Istanze del Wallet NON DEVONO pubblicare i loro metadati attraverso un servizio online.
- L'infrastruttura di trust DEVE essere pubblica, con tutti gli endpoint pubblicamente accessibili senza alcuna Credenziale client che possa rivelare chi sta richiedendo l'accesso.
- Quando un'Istanza del Wallet richiede i Subordinate Statement per costruire la Trust Chain per una specifica Relying Party o convalida un Trust Mark online, emesso per una specifica Relying Party, il Trust Anchor o il suo Intermediario non sanno che una particolare Istanza del Wallet sta chiedendo informazioni su una specifica Relying Party; invece, servono solo le dichiarazioni relative a quella Relying Party come risorsa pubblica.
- I metadati dell'Istanza del Wallet NON DEVONO contenere informazioni che possano rivelare informazioni tecniche sull'hardware utilizzato.
- I metadati dell'entità Foglia, dell'Intermediario e del Trust Anchor possono includere la quantità necessaria di dati come parte delle informazioni di contatto amministrativo, tecnico e di sicurezza. Generalmente non è raccomandato utilizzare dettagli di contatto personali in tali casi. Da una prospettiva legale, la pubblicazione di tali informazioni è necessaria per il supporto operativo riguardante questioni tecniche e di sicurezza e la regolamentazione GDPR.


Considerazioni sulla Decentralizzazione
---------------------------------------

- Ci possono essere più di un singolo Trust Anchor.
- In alcuni casi, un verificatore di fiducia può fidarsi di un Intermediario, specialmente quando l'Intermediario agisce come un Trust Anchor all'interno di un perimetro specifico, come casi in cui le Foglie sono entrambe nello stesso perimetro come una giurisdizione di Stato Membro (ad esempio: una Relying Party italiana con un'Istanza del Wallet italiana può considerare l'Intermediario italiano come un Trust Anchor per gli scopi delle loro interazioni).
- Le attestazioni di fiducia (Trust Chain) dovrebbero essere incluse nel JWT emesso dai Credential Issuer, e le Richieste di Presentazione delle RP dovrebbero contenere la Trust Chain relativa a loro (emittenti delle richieste di presentazione).
- Poiché la presentazione delle Credenziali deve essere firmata, memorizzando le richieste e le risposte di presentazione firmate, che includono la Trust Chain, l'Istanza del Wallet può avere lo snapshot della configurazione della federazione (Entity Configuration del Trust Anchor nella Trust Chain) e l'affidabilità verificabile della Relying Party con cui ha interagito.
- Ogni attestazione firmata è di lunga durata poiché può essere crittograficamente convalidata anche quando la configurazione della federazione cambia o le chiavi dei suoi emittenti vengono rinnovate.
- Ogni partecipante dovrebbe essere in grado di aggiornare la propria Entity Configuration senza notificare le modifiche a terze parti. La policy dei metadati contenuta all'interno di una Trust Chain deve essere applicata per sovrascrivere qualsiasi informazione relativa ai metadati specifici del protocollo.

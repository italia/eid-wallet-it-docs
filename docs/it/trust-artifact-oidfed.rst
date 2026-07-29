.. include:: ../common/common_definitions.rst
.. Included via infrastructure-trust.rst at title level '-' (level 1).

National Trust Artifacts
------------------------

Questa sezione definisce il National Trust Framework basato su OpenID Federation (`OID-FED`_) combinato con una PKI X.509 dedicata alla firma delle Digital Credentials che richiedono X.509.
Il profilo X.509 è dettagliato negli :ref:`infrastructure-trust:Common Trust Artifacts`, mentre le sezioni seguenti definiscono i Trust Artifacts richiesti e i relativi ruoli concettuali definiti nelle specifiche della famiglia OpenID Federation, ciascuna nel proprio ambito:

- OpenID Federation 1.0 (`OID-FED`_), il framework di base.
  Definisce gli artifact principali, inclusi gli Entity Statements, gli endpoint di federazione e i Trust Mark.
- OpenID Federation for Wallet Architectures (`OID-FED-WALLET`_) il profilo di implementazione Wallet per OpenID Federation 1.0.
  Definisce gli Entity Type Identifiers delle Entity usate in questa sezione.
- OpenID Federation Subordinate Events (`OID-FED-SUBORDINATE-EVENTS`_), che definisce l'endpoint Subordinate Events, usato per ottenere la storia di registrazione di un Immediate Subordinate.

La figura :ref:`fig_OID-FED_roles` mappa ciascuna entità dell'ecosistema wallet sul ruolo OpenID Federation che svolge.
Le Wallet-Relying Party e i Wallet Provider sono Federation Entity che DEVONO essere registrate da una Federation Authority, ossia un Federation TA o Intermediate.

.. _fig_OID-FED_roles:
.. plantuml:: plantuml/oid-fed-roles.puml
    :width: 70%
    :alt: The roles within the Federation, where the Trust Anchor oversees its subordinates, which include one or more Intermediates and Leaves.
    :caption: `OID-FED Roles <https://www.plantuml.com/plantuml/svg/TOz1Q_90443l-olcypjBiPNQGn4bAWWzI2dqKYXZCjh1pMoOdLMa-DyRecYqz9OXxysy7KL3jLHwzuybzwaWUCxwTrd_CmjYo48wT2vkM2fKB669-MQj8KcH1HyKJ55Y_Ol4MjHODUoEmDBNXdDEAJUKjIVepAWWHUCWC4xs5PIDANO08wpmV1R-hnvcWqaFlXr0otxJ50t6ajTYunZ2DJ4N8osfO3Hg21RhrUjwqy7qyNRTA_azoneMgBQ73xd8kczahTZ1mHskt_12k3qrUy9LR6LFdsRtarzttj5xCbXes791n_9T1N_7dAxV8fbIGMAC7kOnfjEcd8-15NHJrHqsqUV1qELy-TQgDUnQq8YaIAN_0G00>`_

.. note::
  Le Wallet Unit non sono Federation Entity: sono i dispositivi personali dell'End-User autenticati dal proprio Wallet Provider.


Federation API Endpoints
^^^^^^^^^^^^^^^^^^^^^^^^^

OpenID Federation 1.0 utilizza servizi web RESTful protetti su HTTPS.
Tutte le Federation Entity DEVONO pubblicare la propria **Entity Configuration** all'endpoint ``.well-known/openid-federation`` secondo `OID-FED`_ Section 9.
Il Federation TA e gli Intermediate espongono inoltre gli endpoint di federazione usati per costruire e validare le Trust Chain e per supportare i Trust Mark.

Le proprietà di Federation Entity supportate nel profilo di specifica IT-Wallet sono definite in `OID-FED`_ Section 5.1.1.
La tabella seguente elenca gli endpoint di federazione, i tipi di Entity che DEVONO esporre ciascuno di essi, i parametri di richiesta usati nell'IT-Wallet con il relativo stato REQUIRED od OPTIONAL, e la risposta restituita da ciascun endpoint.
I parametri di richiesta seguono `OID-FED`_ Section 8: sono inviati come query parameters per le richieste GET e nel body per le richieste POST.
Le risposte seguono i formati di risposta OID-FED referenziati nella tabella.

.. list-table::
   :class: longtable
   :widths: 25 35 40
   :header-rows: 1

   * - **Endpoint**
     - **Request parameters**
     - **Response**
   * - **fetch** (``/fetch``).
       REQUIRED per Federation TA e Intermediate.
     - **GET**.
       ``sub`` REQUIRED.
     - Il Subordinate Statement richiesto, come JWT firmato (``application/entity-statement+jwt``).
       `OID-FED`_ Section 8.1.2
   * - **list** (``/list``).
       REQUIRED per Federation TA e Intermediate.
     - **GET**.
       ``entity_type``, ``trust_marked``, ``trust_mark_type`` e ``intermediate``, tutti OPTIONAL.
     - Un array JSON degli Entity Identifier degli Immediate Subordinate (``application/json``).
       `OID-FED`_ Section 8.2.2
   * - **resolve** (``/resolve``).
       REQUIRED per Federation TA e Intermediate.
     - **GET**.
       ``sub`` e ``trust_anchor`` REQUIRED, ``entity_type`` OPTIONAL.
     - La Resolve Response con i Resolved Metadata, la Trust Chain e i Trust Mark verificati, come JWT firmato (``application/resolve-response+jwt``).
       `OID-FED`_ Section 8.3.2
   * - **trust mark status** (``/trust_mark_status``).
       REQUIRED per Federation TA e OPTIONAL per Intermediate.
     - **POST**.
       ``trust_mark`` REQUIRED.
     - La Trust Mark Status Response, ossia la validità del Trust Mark, come JWT firmato (``application/trust-mark-status-response+jwt``).
       `OID-FED`_ Section 8.4.2
   * - **trust mark list** (``/trust_marked_list``).
       REQUIRED per Federation TA e OPTIONAL per Intermediate.
     - **GET**.
       ``trust_mark_type`` REQUIRED, ``sub`` OPTIONAL.
     - Un array JSON degli Entity Identifier per i quali il Trust Mark è emesso e ancora valido (``application/json``).
       `OID-FED`_ Section 8.5.2
   * - **trust mark** (``/trust_mark``).
       REQUIRED solo per Federation TA e OPTIONAL per Intermediate.
     - **GET**.
       ``trust_mark_type`` e ``sub`` REQUIRED.
     - Il Trust Mark richiesto, come JWT firmato (``application/trust-mark+jwt``).
       `OID-FED`_ Section 8.6.2
   * - **historical keys** (``/historical_keys``).
       REQUIRED per Federation TA e Intermediate.
     - **GET**.
       Nessun parametro di richiesta.
     - Un JWK Set firmato con le chiavi storiche, come JWT firmato (``application/jwk-set+jwt``).
       `OID-FED`_ Section 8.7.2
   * - **subordinate events** (``/subordinate_events``).
       REQUIRED per Federation TA e OPTIONAL per Intermediate.
     - **GET**.
       ``sub`` REQUIRED.
     - Un JWT firmato con la storia degli eventi di registrazione.
       Vedi la specifica Subordinate Events Section 2.3.

L'endpoint **Subordinate Events** (``/subordinate_events``) è definito in `OpenID Federation Subordinate Events <https://openid.net/specs/openid-federation-subordinate-events-1_0.html>`_.
Il suo scopo è fornire una traccia storica verificabile degli eventi di registrazione relativi a un Immediate Subordinate, quali la registrazione, l'aggiornamento delle Federation Entity Keys e la revoca.
Per il formato della richiesta, della risposta e i tipi di evento si fa riferimento a `OpenID Federation Subordinate Events <https://openid.net/specs/openid-federation-subordinate-events-1_0.html>`_ Section 2.2 e 2.3.

.. note::
  Nell'IT-Wallet l'endpoint **resolve** (``/resolve``) DEVE rispondere alle richieste non autenticate solo con informazioni cached sulle Entity, se disponibili, e la raccolta e la valutazione di una Trust Chain NON DEVE essere l'azione predefinita dell'endpoint resolve, come descritto in `OID-FED`_ Section 18.1.

Entity Statements
^^^^^^^^^^^^^^^^^^^^^^^

Un **Entity Statement** è un JWT firmato emesso da un'entità (su se stessa o su un superiore) per condividere i metadati di federazione.
Contiene le chiavi, le policy e i dettagli di configurazione necessari affinché l'entità soggetto partecipi alla federazione.

L'**Entity Configuration** è l'Entity Statement che ciascuna Federation Entity emette su se stessa e pubblica al path ``.well-known/openid-federation`` (`OID-FED`_ Section 3).
I suoi ``iss`` e ``sub`` sono il Federation Entity Identifier dell'Entity stessa, ed è firmata con una Federation Entity Key.
La risposta HTTP imposta il media type a ``application/entity-statement+jwt``.
L'Entity Configuration PUÒ anche contenere uno o più Trust Mark.

Un **Subordinate Statement** è l'Entity Statement che un Trust Anchor o un Federation Intermediate emette sul proprio Immediate Subordinate (`OID-FED`_ Section 3).
Il suo ``iss`` è l'issuer, il suo ``sub`` è il Subordinate, e trasporta le Federation Entity Keys del Subordinate, quindi è lo statement che vincola le chiavi del Subordinate sotto il proprio superiore.
PUÒ anche trasportare una metadata policy e i Trust Mark relativi al Subordinate.

Entity Configuration
"""""""""""""""""""""""

Nell'ecosistema IT-Wallet l'Entity Configuration è pubblicata durante l'onboarding dell'Entity (vedi :ref:`onboarding-system:Onboarding Processes`) e viene recuperata e validata durante la valutazione del trust, come definito in :ref:`trust-evaluation:Federation Entity Authentication` e :ref:`trust-evaluation:Metadata Retrieval and Validation`.

I dettagli tecnici sull'Entity Configuration di Wallet Provider, Credential Issuer e Relying Party sono forniti rispettivamente nella Section :ref:`wallet-provider-entity-configuration:Entity Configuration del Fornitore di Wallet`, :ref:`credential-issuer-entity-configuration:Entity Configuration del Fornitore di Attestati Elettronici` e :ref:`relying-party-entity-configuration:Entity Configuration Relying Party`.

.. note::
  Tutti i controlli di firma sulle Entity Configuration, sui Subordinate Statement e sui Trust Mark sono effettuati con le Federation Entity Keys.
  Per gli algoritmi supportati si fa riferimento alla Section :ref:`algorithms:Algoritmi Crittografici`.

Subordinate Statements
"""""""""""""""""""""""

I Trust Anchor e i Federation Intermediate servono i propri Subordinate Statement tramite l'endpoint **fetch** (``/fetch``) (`OID-FED`_ Section 8.1), dove un Trust Evaluator li recupera per validare la firma dell'Entity Configuration del Subordinate e per costruire la Trust Chain.
La metadata policy, quando presente, modifica i metadati finali del Leaf.
I metadati finali sono derivati dall'intera Trust Chain, dall'Entity Configuration fino al Subordinate Statement emesso dal Trust Anchor, come definito in :ref:`trust-evaluation:Metadata Retrieval and Validation`.
La revoca di un Subordinate è espressa dall'assenza di un Subordinate Statement valido su di esso, come definito in :ref:`trust-evaluation:Federation Trust Chain`.

Nell'IT-Wallet i Subordinate Statement sono emessi durante l'onboarding del Subordinate (vedi :ref:`onboarding-system:Onboarding Processes`).

Entity Statement Parameters
"""""""""""""""""""""""""""""""""""""""

Oltre ai parametri comuni REQUIRED ``iss``, ``sub``, ``iat``, ``exp`` e ``jwks`` come definiti in `OID-FED`_ Section 3.1.1, nel profilo di specifica IT-Wallet si applicano i seguenti parametri.

Nell'Entity Configuration (`OID-FED`_ Section 3.1.2):

- **metadata** (``metadata``): REQUIRED. Oggetto JSON in cui ciascuna chiave è un identificatore di tipo di metadati e il relativo valore è il metadata di quel tipo (vedi `OID-FED`_ Section 3.1.1).
  Tutte le Entity DEVONO includere almeno un metadata per ``federation_entity`` nelle proprie Entity Configuration, e POSSONO includere più di uno statement di metadata, ma solo uno per ciascun tipo di metadata.
  I tipi di metadata sono definiti in :ref:`infrastructure-trust:Entity Type Identifiers and Metadata`.
- **trust_marks** (``trust_marks``): REQUIRED per Leaf e Federation Intermediate.
  Array JSON dei Trust Mark del soggetto.
  Il Trust Mark di registrazione è definito in :ref:`infrastructure-trust:Trust Mark registration-entity`.
- **trust_mark_issuers** (``trust_mark_issuers``): REQUIRED solo per Federation TA e NON DEVE essere incluso altrimenti.
  Oggetto JSON che dichiara, per ciascun tipo di Trust Mark, le Federation Authority autorizzate a emetterlo, indicate tramite i rispettivi Federation Entity Identifier.
  Nell'IT-Wallet il Trust Mark di registrazione è emesso solo dal Federation Trust Anchor, quindi DEVE contenere almeno l'identificatore del Federation TA.

Nel Subordinate Statement (`OID-FED`_ Section 3.1.3):

- **metadata_policy** (``metadata_policy``): OPTIONAL in `OID-FED`_.
  Metadata policy vincolata a uno specifico tipo di metadata e applicata al sottoalbero, risolta combinando i Claim ``metadata_policy`` lungo la Trust Chain, come definito in `OID-FED`_ Section 6.1.4.
  Nell'IT-Wallet il Subordinate Statement relativo a un Leaf DEVE trasportare una ``metadata_policy`` che vincola i metadata di protocollo del Leaf ai valori approvati in fase di onboarding.
  Usando gli operatori di metadata policy di `OID-FED`_ Section 6.1.3, DEVE fissare le chiavi di firma di protocollo (``jwks``) e, quando presenti nel tipo di metadata, gli endpoint di servizio e le URI di request, response e redirect (ad esempio ``request_uris``, ``response_uris`` e ``redirect_uris`` di ``openid_credential_verifier``).
  Questo Subordinate Statement è emesso dal superiore immediato che ha registrato il Leaf, ossia il Federation TA per i Leaf che registra direttamente e un Federation Intermediate per le Relying Party affiliate.
  Il Subordinate Statement relativo a un Federation Intermediate non trasporta una ``metadata_policy``, perché l'Intermediate non ha metadata di protocollo e le Relying Party affiliate sono vincolate dall'Intermediate stesso.
  Un superiore PUÒ ulteriormente restringere la metadata policy impostata dai propri superiori, ma NON DEVE rilassarla, come definito in `OID-FED`_ Section 6.1.1.
- **constraints** (``constraints``): REQUIRED solo per Federation TA.
  Trasporta i vincoli applicati al sottoalbero sotto l'issuer.
  DEVE contenere ``allowed_entity_types``, che restringe i tipi di Entity di metadata che i Subordinate nel sottoalbero sono autorizzati a pubblicare, e ``max_path_length``, che limita il numero di Intermediate tra l'issuer e il soggetto della Trust Chain.
  Il tipo di Entity ``federation_entity`` è sempre consentito e NON DEVE essere elencato in ``allowed_entity_types``.
  Vedi `OID-FED`_ Section 6.2.

Tutti gli altri parametri opzionali definiti in `OID-FED`_ Section 3 che non sono riconosciuti nel profilo di specifica IT-Wallet DEVONO essere ignorati durante la valutazione di un Entity Statement.

.. note::
  Nell'IT-Wallet le Federation Entity Keys trasportate nei ``jwks`` di un'Entity Configuration o di un Subordinate Statement sono usate per firmare gli statement di federazione e sono validate tramite la Federation Trust Chain, non tramite X.509.
  La PKI di firma X.509, i cui certificati sono usati per firmare le Attestations, è una relazione di trust distinta.
  I Signing Trust Anchor di questa PKI sono distribuiti nell'Entity Configuration del Federation Trust Anchor.
  Ciascuno è fornito nel parametro ``x5c`` (:rfc:`7517` Section 4.7) di un JWK dedicato all'interno dei ``jwks``, distinto dalle Federation Entity Keys, che non trasportano ``x5c``, come definito in :ref:`trust-evaluation:Signing Trust Anchor Distribution`.
  I certificati Document Signer dei Credential Issuer non sono trasportati nei ``jwks`` degli Entity Statement: sono inclusi nelle Attestations firmate, nell'header ``x5chain`` per il formato mdoc e nell'header ``x5c`` per il formato JOSE, e sono validati come definito in :ref:`trust-evaluation:X.509 Certificate Chain Validation`.
  L'emissione di questi certificati X.509 e il funzionamento della PKI di firma sono definiti nell'onboarding (vedi :ref:`onboarding-system:Onboarding Processes`).

Entity Type Identifiers and Metadata
""""""""""""""""""""""""""""""""""""

Gli Entity Type Identifiers dei ruoli dell'ecosistema sono definiti in OpenID Federation for Wallet Architectures, section Wallet Architecture Entity Types, che è il profilo wallet di OpenID Federation.
Ciascun ruolo dichiara nella propria Entity Configuration uno o più tipi di metadata, i cui parametri seguono la specifica di protocollo di quel tipo di metadata.
La tabella seguente mappa i ruoli dell'ecosistema sui relativi Entity Type Identifiers e fornisce il riferimento del protocollo di metadata per ciascuno di essi.

.. warning::
  Nell'IT-Wallet il tipo di metadata del Wallet Provider DEVE essere ``wallet_solution``.
  Si tratta di una deroga rispetto a OpenID Federation for Wallet Architectures, che nomina il corrispondente Entity Type Identifier ``openid_wallet_provider``.

.. list-table::
   :class: longtable
   :widths: 25 75
   :header-rows: 1

   * - **Entity**
     - **Metadata Type**
   * - Trust Anchor
     - ``federation_entity``
   * - Federation Intermediate
     - ``federation_entity``
   * - Wallet Provider
     - ``federation_entity``, ``wallet_solution``
   * - Credential Issuer
     - ``federation_entity``, ``openid_credential_issuer``, [``oauth_authorization_server``]
   * - Relying Party
     - ``federation_entity``, ``openid_credential_verifier``
   * - Relying Party Intermediary
     - ``federation_entity``

.. note::
  Un Relying Party Intermediary è un Federation Intermediate.
  Come intermediario non è coinvolto nei flussi di protocollo, quindi non pubblica un metadata di protocollo proprio, ma solo il metadata ``federation_entity``.
  Pubblica i Subordinate Statement delle Relying Party affiliate, e ciascuna Relying Party affiliata imposta i propri ``authority_hints`` sull'Intermediary.
  Il suo Trust Mark di registrazione usa l'Entity Type Identifier ``intermediate`` nel tipo di Trust Mark, come definito in :ref:`infrastructure-trust:Trust Mark Types and Schema`.

.. note::
  Quando un PID o EAA Provider implementa sia il Credential Issuer sia l'Authorization Server all'interno della stessa Entity, DEVE includere sia ``openid_credential_issuer`` sia ``oauth_authorization_server`` nei propri tipi di metadata.
  Quando l'Authorization Server è un'Entity separata, il metadata del Credential Issuer DEVE contenere il parametro ``authorization_servers`` con l'identificatore dell'Authorization Server.
  Secondo `OPENID4VCI`_ l'Authorization Server PUÒ essere esterno all'Entity che implementa il Credential Endpoint, pertanto l'uso di ``oauth_authorization_server`` è OPTIONAL.
  Inoltre, qualora fosse necessaria l'autenticazione dell'utente da parte del Credential Issuer, potrebbe essere necessario includere il relativo tipo di metadata ``openid_credential_verifier``.

I metadata ``federation_entity`` trasportano i parametri informativi seguenti insieme ai parametri degli endpoint di federazione.
I parametri degli endpoint di federazione (``federation_fetch_endpoint``, ``federation_list_endpoint``, ``federation_resolve_endpoint`` e gli altri) sono pubblicati solo dal Federation TA e dagli Intermediate, secondo i relativi obblighi definiti nella sezione Federation API Endpoints sopra, e un Leaf non li espone.
I parametri informativi seguenti sono OPTIONAL in `OID-FED`_; il profilo di specifica IT-Wallet supporta i claim della tabella seguente.

.. list-table::
  :class: longtable
  :widths: 25 75
  :header-rows: 1

  * - **Claim**
    - **Description**
  * - **organization_name**
    - REQUIRED.
      Vedi `OID-FED`_ Section 5.2.2
  * - **homepage_uri**
    - REQUIRED.
      Vedi `OID-FED`_ Section 5.2.2
  * - **policy_uri**
    - REQUIRED.
      Vedi `OID-FED`_ Section 5.2.2
  * - **logo_uri**
    - REQUIRED.
      URL del logo dell'entità, in formato SVG.
      Vedi `OID-FED`_ Section 5.2.2
  * - **contacts**
    - REQUIRED.
      Nell'IT-Wallet è l'indirizzo email istituzionale verificato (PEC) dell'entità.
      Vedi `OID-FED`_ Section 5.2.2
  * - **tos_uri**
    - OPTIONAL.
      URL dei termini di servizio dell'entità.
      Vedi `OID-FED`_ Section 5.2.2

I metadata relativi a Wallet Provider, Credential Issuer e Relying Party sono descritti rispettivamente nella Section :ref:`wallet-solution-metadata:Metadati della Soluzione Wallet`, :ref:`credential-issuer-metadata:Metadata del Fornitore di Attestati Elettronici` e :ref:`relying-party-metadata:Metadati della Relying Party`.

Entity Statement Examples
^^^^^^^^^^^^^^^^^^^^^^^^^

Le sezioni seguenti forniscono esempi non normativi di Entity Statement, sia per l'onboarding diretto sotto il Federation TA sia per l'onboarding intermediato sotto un Federation Intermediate.
Tutti gli statement sono JWT firmati con l'header JOSE ``alg``, ``kid`` e ``typ`` impostato a ``entity-statement+jwt``, e sono mostrati solo i payload.
I metadata di protocollo e i set di chiavi fissati sono troncati (``{ ... }``) poiché la loro definizione completa è fornita nelle sezioni di metadata referenziate sopra.

Entity Configuration of a Federation TA
"""""""""""""""""""""""""""""""""""""""

Il Federation TA è la radice della Trust Chain.
La sua Entity Configuration non ha ``authority_hints``, e i suoi ``jwks`` forniscono, oltre alle Federation Entity Keys, i Signing Trust Anchor della PKI di firma X.509 e gli Authentication Trust Anchor della PKI di autenticazione X.509, come JWK dedicati con ``x5c``.
Un Signing Trust Anchor è la radice della PKI che emette i certificati Document Signer; un Authentication Trust Anchor è la radice della PKI che emette i certificati di autenticazione delle Relying Party usati per l'autenticazione del reader mdoc nel Proximity Flow.
Ciascuno di tali JWK è identificato dal proprio ``kid`` e dalle proprietà del certificato fornito nel proprio ``x5c``.

.. literalinclude:: ../../examples/oidfed-ec-federation-ta.json
  :language: JSON

Subordinate Statement of Leaf issued by the Federation TA
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Il Federation TA emette un Subordinate Statement su ciascun Leaf che registra direttamente.
Lo statement trasporta le Federation Entity Keys del Leaf, la ``metadata_policy`` che fissa le chiavi di protocollo e, quando presenti, gli endpoint di servizio e le URI del Leaf ai valori approvati in fase di onboarding, e i ``constraints`` del sottoalbero.

**Wallet Provider**

.. literalinclude:: ../../examples/oidfed-ss-ta-leaf-wallet-provider.json
  :language: JSON

**Relying Party**

.. literalinclude:: ../../examples/oidfed-ss-ta-leaf-relying-party.json
  :language: JSON

**Credential Issuer**

.. literalinclude:: ../../examples/oidfed-ss-ta-leaf-credential-issuer.json
  :language: JSON

Subordinate Statement of an Intermediate
""""""""""""""""""""""""""""""""""""""""

Il Federation TA emette un Subordinate Statement sul Federation Intermediate.
I ``constraints`` restringono il sottoalbero dell'Intermediate alle Relying Party che può intermediare, e ``max_path_length`` è impostato a 1 per consentire il singolo livello di intermediazione tra Federation TA e Relying Party affiliate.
Non trasporta ``metadata_policy``: le Relying Party affiliate sono vincolate dall'Intermediate nei Subordinate Statement che emette su di esse.

.. literalinclude:: ../../examples/oidfed-ss-intermediate.json
  :language: JSON

Subordinate Statement about a Leaf issued by a Federation Intermediate
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Il Federation Intermediate emette un Subordinate Statement su ciascuna Relying Party affiliata.
Trasporta la ``metadata_policy`` che vincola i metadata di protocollo della Relying Party affiliata ai valori approvati in fase di onboarding, esattamente come fa il Federation TA per i Leaf che registra direttamente.
I ``constraints`` del sottoalbero sono impostati dal Federation TA nello statement relativo all'Intermediate.
Nel National Trust Framework un Intermediary intermedia solo Relying Party.

.. literalinclude:: ../../examples/oidfed-ss-intermediate-leaf.json
  :language: JSON

Entity Configuration of a Federation Intermediate
"""""""""""""""""""""""""""""""""""""""""""""""""

Il Federation Intermediate è solo ``federation_entity``.
La sua Entity Configuration punta al Federation TA tramite ``authority_hints`` e trasporta il Trust Mark di registrazione con l'Entity Type Identifier ``intermediate``.
Espone gli endpoint fetch e list usati per servire i Subordinate Statement delle Relying Party affiliate.

.. literalinclude:: ../../examples/oidfed-ec-federation-intermediate.json
  :language: JSON

Entity Configuration of a Leaf
""""""""""""""""""""""""""""""

Ciascun Leaf pubblica la propria Entity Configuration, puntando al superiore immediato tramite ``authority_hints`` e trasportando il proprio Trust Mark di registrazione.
Gli esempi seguenti riportano i claim principali; i metadata di protocollo sono referenziati alla relativa sezione di metadata.

**Wallet Provider**

.. literalinclude:: ../../examples/oidfed-ec-leaf-wallet-provider.json
  :language: JSON

**Relying Party**

.. literalinclude:: ../../examples/oidfed-ec-leaf-relying-party.json
  :language: JSON

**Credential Issuer**

.. literalinclude:: ../../examples/oidfed-ec-leaf-credential-issuer.json
  :language: JSON

Trust Marks
^^^^^^^^^^^

A seguito del completamento con successo dell'onboarding, le entità ricevono IT-Wallet Federation Trust Marks.
I Trust Mark sono emessi dalla Federation Authority (Trust Anchor per l'onboarding diretto, Intermediate per l'onboarding intermediato) tramite il Federation Trust Mark Endpoint e fungono da attestazioni verificabili di conformità ai profili tecnici IT-Wallet e/o alle policy di autorizzazione.

Trust Mark Types and Schema
"""""""""""""""""""""""""""

Gli identificatori dei Trust Mark DEVONO seguire uno schema gerarchico che riflette l'ambito di autorizzazione:

``https://<federation_authority_domain>/trust_marks/<purpose>/<entity_type>``

Dove:

  - ``<federation_authority_domain>``: il dominio della Federation Authority emittente.
  - ``<purpose>``: la finalità del Trust Mark.
    La finalità ``registration-entity`` è **REQUIRED** per tutte le entità a seguito del processo di onboarding.
    Ulteriori finalità di Trust Mark POSSONO essere definite per esigenze future, ma non sono richieste per i processi di autorizzazione definiti in :ref:`trust-evaluation:Authorization`.
  - ``<entity_type>``: l'Entity Type Identifier del soggetto, tra quelli definiti in :ref:`infrastructure-trust:Entity Type Identifiers and Metadata` (ad esempio ``openid_credential_issuer`` o ``openid_credential_verifier``), e ``intermediate`` per un Relying Party Intermediary.

Trust Mark registration-entity
"""""""""""""""""""""""""""""""

Nell'IT-Wallet il Trust Mark ``registration-entity`` è il Trust Mark di registrazione di un'entità.
Il Federation TA nazionale è l'issuer di Trust Mark riconosciuto nella federazione e l'unico che può abilitare altri issuer di Trust Mark usando il parametro ``trust_mark_issuers`` nella propria Entity Configuration.
Attesta la registrazione e trasporta i dati di autorizzazione dell'entità, ossia i suoi entitlements e, ove applicabile, le Credentials e gli attributi che è autorizzata a emettere o a richiedere.
Questo Trust Mark di registrazione è l'analogo funzionale del Wallet-Relying Party Registration Certificate (WRPRC) del EUDIW Trust Framework.
Un'entità riceve un Trust Mark di registrazione per ciascun ruolo che detiene, con la componente ``<entity_type>`` dell'identificatore impostata di conseguenza.

Un Relying Party Intermediary riceve il proprio Trust Mark di registrazione con ``<entity_type>`` ``intermediate`` nell'identificatore.

Nel EUDIW Trust Framework la relazione di intermediazione è espressa nei dati di registrazione della Relying Party intermediata.
Nel National Trust Framework, invece, è espressa tramite la gerarchia di federazione: l'Intermediary è un Federation Intermediate che pubblica i Subordinate Statement delle Relying Party affiliate, e ciascuna Relying Party affiliata imposta i propri ``authority_hints`` sull'Intermediary.
Il Trust Mark di registrazione di ciascuna Relying Party affiliata è altresì emesso dal Federation Trust Anchor.
Per questo motivo nel Trust Mark non è presente un campo dedicato all'intermediario.
L'onboarding dell'Intermediary è definito in :ref:`onboarding-system:Relying Party Intermediary`.

**Trust Mark Structure**

I Trust Mark nell'Entity Configuration DEVONO essere rappresentati come oggetti JSON contenenti i seguenti claim:

.. list-table:: Trust Mark Object Claims (in Entity Configuration)
   :class: longtable
   :header-rows: 1
   :widths: 25 75

   * - **Claim**
     - **Description**
   * - **trust_mark_type**
     - REQUIRED.
       Identificatore del tipo di Trust Mark secondo lo schema: ``https://<federation_authority_domain>/trust_marks/<purpose>/<entity_type>``.
   * - **trust_mark**
     - REQUIRED.
       Un JSON Web Token firmato che rappresenta il Trust Mark emesso dalla Federation Authority.

Il Trust Mark JWT (contenuto nel claim ``trust_mark`` sopra) DEVE essere un JWT firmato che include sia un header JOSE sia un payload, come definito in `OID-FED`_ Section 7.

**Trust Mark JWT Header**

L'header JOSE del Trust Mark JWT DEVE includere i seguenti parametri:

.. list-table:: Trust Mark JWT Header Parameters
   :class: longtable
   :header-rows: 1
   :widths: 25 75

   * - **Parameter**
     - **Description**
   * - **alg**
     - REQUIRED.
       L'algoritmo crittografico usato per firmare il Trust Mark JWT.
       DEVE essere uno degli algoritmi supportati per le Federation Entity Keys (vedi :ref:`algorithms:Algoritmi Crittografici`).
   * - **kid**
     - REQUIRED.
       Key ID della Federation Entity Key usata per firmare il Trust Mark, come definito in `OID-FED`_ Section 7.
   * - **typ**
     - REQUIRED.
       Media type del Trust Mark JWT.
       DEVE essere impostato a ``trust-mark+jwt``, come definito in `OID-FED`_ Section 7, salvo che un media type più specifico sia definito dal trust framework per il particolare tipo di Trust Mark.
       I Trust Mark senza parametro di header ``typ`` o con un valore ``typ`` non riconosciuto DEVONO essere rifiutati.

Esempio non normativo di header di un Trust Mark JWT:

.. code-block:: JSON

  {
    "alg": "ES256",
    "kid": "ta-federation-key-1",
    "typ": "trust-mark+jwt"
  }

**Trust Mark JWT Payload**

Il payload del Trust Mark JWT include i seguenti claim:

.. list-table:: Trust Mark JWT Claims
   :class: longtable
   :header-rows: 1
   :widths: 25 75

   * - **Claim**
     - **Description**
   * - **iss**
     - REQUIRED.
       Il Federation Trust Anchor che emette il Trust Mark.
   * - **sub**
     - REQUIRED.
       Federation Entity Identifier del soggetto.
   * - **trust_mark_type**
     - REQUIRED.
       Identificatore univoco del Trust Mark.
       DEVE corrispondere al claim ``trust_mark_type`` dell'oggetto Trust Mark.
   * - **iat**
     - REQUIRED.
       Timestamp di emissione del Trust Mark.
   * - **exp**
     - REQUIRED.
       Timestamp di scadenza del Trust Mark.
   * - **public_body**
     - REQUIRED.
       Booleano che indica se l'entità è un ente del settore pubblico.
   * - **vat_number**
     - REQUIRED quando ``public_body`` è ``false``.
       Partita IVA dell'entità.
       PUÒ essere presente anche quando ``public_body`` è ``true``.
   * - **legal_identifier**
     - RECOMMENDED.
       Numero o identificatore di registrazione legale dell'entità (es. numero di registrazione aziendale, codice fiscale).
   * - **ipa_code**
     - REQUIRED quando ``public_body`` è ``true``, NON DEVE essere presente altrimenti.
       Codice IPA (Indice delle Pubbliche Amministrazioni) dell'ente pubblico.
   * - **organization_name**
     - REQUIRED.
       Nome completo dell'Organizational Entity.
   * - **email**
     - REQUIRED.
       Email istituzionale o PEC dell'organizzazione.
   * - **support_uri**
     - REQUIRED.
       URL o indirizzo email da usare per richieste relative all'entità, quali cancellazione o portabilità dei dati.
   * - **srv_description**
     - REQUIRED.
       Descrizione multilingue del servizio fornito dall'entità.
       Ciascuna voce contiene ``lang`` e ``value``.
   * - **entitlements**
     - REQUIRED.
       Array di URI di entitlement che identificano il ruolo del soggetto, come definito in `ETSI TS 119 475`_ Annex A.2 (es. ``Service_Provider``, ``PID_Provider``, ``QEAA_Provider``, ``PUB_EAA_Provider``, ``Non_Q_EAA_Provider``).
   * - **provides_attestations**
     - REQUIRED per un Credential Issuer, NON DEVE essere presente altrimenti.
       Array delle tipologie di Credential che il soggetto è autorizzato a emettere.
       Ciascuna voce contiene ``format``, ``meta`` per identificare la tipologia di Credential, e un array ``claim`` opzionale.
   * - **credentials**
     - REQUIRED per una Relying Party che richiede Credentials, NON DEVE essere presente altrimenti.
       Array delle query di Credential che il soggetto è autorizzato a richiedere, usato per l'Overasking Check.
       Ciascuna voce contiene ``format``, ``meta`` (es. ``vct_values`` o ``doctype_value``) e un array ``claim`` dei path di attributo autorizzati.
   * - **purpose**
     - REQUIRED per una Relying Party che richiede Credentials, NON DEVE essere presente altrimenti.
       Elenco multilingue che descrive il trattamento dei dati associato all'uso previsto.
       Ciascuna voce contiene ``lang`` e ``value``.
   * - **privacy_policy**
     - REQUIRED per una Relying Party che richiede Credentials, NON DEVE essere presente altrimenti.
       URL della privacy policy del soggetto.
   * - **supervisory_authority**
     - REQUIRED.
       Informazioni sull'Autorità di Protezione dei Dati, con ``uri``, ``email`` e ``phone``.
   * - **logo_uri**
     - REQUIRED.
       URL che punta al :ref:`brand-identity:Trust Mark` per finalità UI/UX.
   * - **ref**
     - OPTIONAL.
       URL con ulteriori informazioni web sul Trust Mark.

.. note::
  I claim che trasportano i dati di autorizzazione (``entitlements``, ``provides_attestations``, ``credentials``, ``purpose``, ``privacy_policy``, ``supervisory_authority``) e i claim di identità e trasparenza allineati al WRPRC (``public_body``, ``support_uri``, ``srv_description``) sono definiti per analogia con il EUDIW Wallet-Relying Party Registration Certificate (`ETSI TS 119 475`_), affinché un Trust Evaluator possa riusare la stessa logica di autorizzazione per entrambi gli artifact.

.. note::
  Lo stato di revoca di un Trust Mark è verificato tramite l'endpoint **trust mark status** (``/trust_mark_status``) (`OID-FED`_ Section 8.4), non tramite una status list trasportata nel token.
  Questa è la differenza rispetto al WRPRC, il cui claim ``status`` punta a una status list: il Trust Mark si basa sul meccanismo di revoca nativo della federazione.
  Il consumo di questi claim da parte del Trust Evaluator è definito in :ref:`trust-evaluation:Authorization`.

Gli esempi non normativi seguenti illustrano il contenuto del Trust Mark JWT di registrazione per un Credential Issuer, un Provider di EAA non qualificata pubblico che emette l'Employee Badge, per una Relying Party che richiede quell'Employee Badge, e per un Relying Party Intermediary.

Credential Issuer, un Provider di EAA non qualificata pubblico che emette l'Employee Badge:

.. literalinclude:: ../../examples/oidfed-trust-mark-credential-issuer.json
  :language: JSON

Relying Party, un'organizzazione privata che richiede l'Employee Badge per il controllo degli accessi fisici:

.. literalinclude:: ../../examples/oidfed-trust-mark-relying-party.json
  :language: JSON

Relying Party Intermediary.
Non dichiara un uso previsto proprio, quindi il suo Trust Mark di registrazione non trasporta ``credentials`` né ``purpose``.
È un Federation Intermediate, e le Relying Party affiliate impostano i propri ``authority_hints`` su di esso.

.. literalinclude:: ../../examples/oidfed-trust-mark-intermediate.json
  :language: JSON

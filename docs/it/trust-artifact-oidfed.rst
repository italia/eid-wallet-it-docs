.. include:: ../common/common_definitions.rst
.. Incluso tramite infrastructure-trust.rst al livello di titolo '-' (livello 1).

National Trust Artifacts
------------------------

Questa sezione definisce il Trust Framework Nazionale basato su OpenID Federation (`OID-FED`_) combinato con una PKI X.509 dedicata alla firma degli Attestati Elettronici che richiede X.509.
Il profilo X.509 è dettagliato in :ref:`infrastructure-trust:Common Trust Artifacts`, mentre le sezioni seguenti definiscono i Trust Artifact richiesti e i loro ruoli concettuali definiti nelle seguenti specifiche della famiglia OpenID Federation, ciascuna nel proprio scope:

- OpenID Federation 1.0 (`OID-FED`_), il framework core.
  Definisce gli artifact principali inclusi gli Entity Statement, gli endpoint di federazione e i Trust Mark.
- OpenID Federation for Wallet Architectures (`OID-FED-WALLET`_) il profilo di implementazione Wallet per OpenID Federation 1.0.
  Definisce gli Entity Type Identifier delle Entità usate in questa sezione.
- OpenID Federation Subordinate Events (`OID-FED-SUBORDINATE-EVENTS`_), che definisce l'endpoint Subordinate Events, usato per ottenere lo storico di registrazione di un Immediate Subordinate.

La figura :ref:`fig_OID-FED_roles` mappa ciascuna entità dell'ecosistema wallet sul ruolo OpenID Federation che svolge.
Le Wallet-Relying Party e i Wallet Provider sono Federation Entity che DEVONO essere registrate da una Federation Authority, cioè un Federation TA o Intermediate.

.. _fig_OID-FED_roles:
.. plantuml:: plantuml/oid-fed-roles.puml
    :width: 70%
    :alt: I ruoli all'interno della Federazione, dove il Trust Anchor sovrintende i suoi subordinati, che includono uno o più Intermediate e Foglie.
    :caption: `OID-FED Roles <https://www.plantuml.com/plantuml/svg/TOz1Q_90443l-olcypjBiPNQGn4bAWWzI2dqKYXZCjh1pMoOdLMa-DyRecYqz9OXxysy7KL3jLHwzuybzwaWUCxwTrd_CmjYo48wT2vkM2fKB669-MQj8KcH1HyKJ55Y_Ol4MjHODUoEmDBNXdDEAJUKjIVepAWWHUCWC4xs5PIDANO08wpmV1R-hnvcWqaFlXr0otxJ50t6ajTYunZ2DJ4N8osfO3Hg21RhrUjwqy7qyNRTA_azoneMgBQ73xd8kczahTZ1mHskt_12k3qrUy9LR6LFdsRtarzttj5xCbXes791n_9T1N_7dAxV8fbIGMAC7kOnfjEcd8-15NHJrHqsqUV1qELy-TQgDUnQq8YaIAN_0G00>`_

.. note::
  Le Wallet Unit non sono Federation Entity, sono i dispositivi personali dell'End-User autenticati dal loro Wallet Provider.


Federation API Endpoints
^^^^^^^^^^^^^^^^^^^^^^^^^

OpenID Federation 1.0 usa servizi web RESTful protetti su HTTPS.
Tutte le Federation Entity DEVONO pubblicare la propria **Entity Configuration** all'endpoint ``.well-known/openid-federation`` secondo `OID-FED`_ Sezione 9.
Il Federation TA e gli Intermediate espongono inoltre gli endpoint di federazione usati per costruire e validare le Trust Chain e per supportare i Trust Mark.

Le proprietà della Federation Entity supportate nel profilo delle specifiche IT-Wallet sono definite in `OID-FED`_ Sezione 5.1.1.
La tabella seguente elenca gli endpoint di federazione, gli Entity Type che DEVONO esporre ciascuno di essi, i parametri di richiesta usati all'interno di IT-Wallet con il loro status OBBLIGATORIO o OPZIONALE, e la risposta restituita da ciascun endpoint.
I parametri di richiesta seguono `OID-FED`_ Sezione 8: sono inviati come query parameter per le richieste GET e nel body per le richieste POST.
Le risposte seguono i formati di risposta OID-FED referenziati nella tabella.

.. list-table::
   :class: longtable
   :widths: 25 35 40
   :header-rows: 1

   * - **Endpoint**
     - **Parametri di richiesta**
     - **Risposta**
   * - **fetch** (``/fetch``).
       OBBLIGATORIO per Federation TA e Intermediate.
     - **GET**.
       ``sub`` OBBLIGATORIO.
     - Il Subordinate Statement richiesto, come JWT firmato (``application/entity-statement+jwt``).
       `OID-FED`_ Sezione 8.1.2
   * - **list** (``/list``).
       OBBLIGATORIO per Federation TA e Intermediate.
     - **GET**.
       ``entity_type``, ``trust_marked``, ``trust_mark_type`` e ``intermediate``, tutti OPZIONALI.
     - Un array JSON degli Entity Identifier degli Immediate Subordinate (``application/json``).
       `OID-FED`_ Sezione 8.2.2
   * - **resolve** (``/resolve``).
       OBBLIGATORIO per Federation TA e Intermediate.
     - **GET**.
       ``sub`` e ``trust_anchor`` OBBLIGATORI, ``entity_type`` OPZIONALE.
     - La Resolve Response con i Resolved Metadata, la Trust Chain e i Trust Mark verificati, come JWT firmato (``application/resolve-response+jwt``).
       `OID-FED`_ Sezione 8.3.2
   * - **trust mark status** (``/trust_mark_status``).
       OBBLIGATORIO per Federation TA e OPZIONALE per Intermediate.
     - **POST**.
       ``trust_mark`` OBBLIGATORIO.
     - La Trust Mark Status Response, cioè la validità del Trust Mark, come JWT firmato (``application/trust-mark-status-response+jwt``).
       `OID-FED`_ Sezione 8.4.2
   * - **trust mark list** (``/trust_marked_list``).
       OBBLIGATORIO per Federation TA e OPZIONALE per Intermediate.
     - **GET**.
       ``trust_mark_type`` OBBLIGATORIO, ``sub`` OPZIONALE.
     - Un array JSON degli Entity Identifier per i quali il Trust Mark è emesso e ancora valido (``application/json``).
       `OID-FED`_ Sezione 8.5.2
   * - **trust mark** (``/trust_mark``).
       OBBLIGATORIO solo per Federation TA e OPZIONALE per Intermediate.
     - **GET**.
       ``trust_mark_type`` e ``sub`` OBBLIGATORI.
     - Il Trust Mark richiesto, come JWT firmato (``application/trust-mark+jwt``).
       `OID-FED`_ Sezione 8.6.2
   * - **historical keys** (``/historical_keys``).
       OBBLIGATORIO per Federation TA e Intermediate.
     - **GET**.
       Nessun parametro di richiesta.
     - Un JWK Set firmato con le chiavi storiche, come JWT firmato (``application/jwk-set+jwt``).
       `OID-FED`_ Sezione 8.7.2
   * - **subordinate events** (``/subordinate_events``).
       OBBLIGATORIO per Federation TA e OPZIONALE per Intermediate.
     - **GET**.
       ``sub`` OBBLIGATORIO.
     - Un JWT firmato con lo storico degli eventi di registrazione.
       Vedi la specifica Subordinate Events Sezione 2.3.

L'endpoint **Subordinate Events** (``/subordinate_events``) è definito in `OpenID Federation Subordinate Events <https://openid.net/specs/openid-federation-subordinate-events-1_0.html>`_.
Il suo scopo è fornire una traccia storica verificabile degli eventi di registrazione concernenti un Immediate Subordinate, come la sua registrazione, l'aggiornamento delle sue Federation Entity Keys e la sua revoca.
Per il formato della richiesta, il formato della risposta e i tipi di evento si fa riferimento a `OpenID Federation Subordinate Events <https://openid.net/specs/openid-federation-subordinate-events-1_0.html>`_ Sezione 2.2 e 2.3.

.. note::
  All'interno di IT-Wallet l'endpoint **resolve** (``/resolve``) DEVE rispondere alle richieste non autenticate solo con informazioni in cache sulle Entità, se disponibili, e la raccolta e la valutazione di una Trust Chain NON DEVE essere l'azione predefinita dell'endpoint resolve, come descritto in `OID-FED`_ Sezione 18.1.

Entity Statements
^^^^^^^^^^^^^^^^^^^^^^^

Un **Entity Statement** è un JWT firmato emesso da un'entità (se stessa o un superiore) per condividere i metadata di federazione.
Contiene le chiavi, le policy e i dettagli di configurazione richiesti affinché l'entità subject partecipi alla federazione.

L'**Entity Configuration** è l'Entity Statement che ciascuna Federation Entity emette su se stessa e pubblica al path ``.well-known/openid-federation`` (`OID-FED`_ Sezione 3).
I suoi ``iss`` e ``sub`` sono il Federation Entity Identifier dell'Entità stessa, ed è firmata con una Federation Entity Key.
La risposta HTTP imposta il media type a ``application/entity-statement+jwt``.
L'Entity Configuration PUÒ anche contenere uno o più Trust Mark.

Un **Subordinate Statement** è l'Entity Statement che un Trust Anchor o un Federation Intermediate emette sul proprio Immediate Subordinate (`OID-FED`_ Sezione 3).
Il suo ``iss`` è l'issuer, il suo ``sub`` è il Subordinate, e reca le Federation Entity Keys del Subordinate, quindi è la dichiarazione che vincola le chiavi del Subordinate sotto il suo superiore.
PUÒ anche recare una metadata policy e i Trust Mark relativi al Subordinate.

Entity Configuration
"""""""""""""""""""""""

Nell'ecosistema IT-Wallet l'Entity Configuration è pubblicata durante l'onboarding dell'Entità (vedi :ref:`onboarding-system:Onboarding Processes`) ed è recuperata e validata durante la trust evaluation, come definito in :ref:`trust-evaluation:Federation Entity Authentication` e :ref:`trust-evaluation:Metadata Retrieval and Validation`.

I dettagli tecnici sull'Entity Configuration di Wallet Provider, Credential Issuer e Relying Party sono forniti nella Sezione :ref:`wallet-provider-entity-configuration:Entity Configuration del Fornitore di Wallet`, :ref:`credential-issuer-entity-configuration:Entity Configuration del Fornitore di Attestati Elettronici` e :ref:`relying-party-entity-configuration:Entity Configuration Relying Party` rispettivamente.

.. note::
  Tutti i controlli di firma sulle Entity Configuration, sui Subordinate Statement e sui Trust Mark sono eseguiti con le Federation Entity Keys.
  Per gli algoritmi supportati si fa riferimento alla Sezione :ref:`algorithms:Algoritmi Crittografici`.

Subordinate Statements
"""""""""""""""""""""""

I Trust Anchor e i Federation Intermediate servono i propri Subordinate Statement attraverso l'endpoint **fetch** (``/fetch``) (`OID-FED`_ Sezione 8.1), dove un Trust Evaluator li recupera per validare la firma dell'Entity Configuration del Subordinate e per costruire la Trust Chain.
La metadata policy, quando presente, modifica i metadata finali della Foglia.
I metadata finali sono derivati dall'intera Trust Chain, dall'Entity Configuration fino al Subordinate Statement emesso dal Trust Anchor, come definito in :ref:`trust-evaluation:Metadata Retrieval and Validation`.
La revoca di un Subordinate è espressa dall'assenza di un Subordinate Statement valido a esso relativo, come definito in :ref:`trust-evaluation:Federation Trust Chain`.

All'interno di IT-Wallet i Subordinate Statement sono emessi durante l'onboarding del Subordinate (vedi :ref:`onboarding-system:Onboarding Processes`).

Entity Statement Parameters
"""""""""""""""""""""""""""""""""""""""

In aggiunta ai parametri comuni OBBLIGATORI ``iss``, ``sub``, ``iat``, ``exp`` e ``jwks`` come definiti in `OID-FED`_ Sezione 3.1.1, all'interno del profilo delle specifiche IT-Wallet si applicano i seguenti parametri.

Nell'Entity Configuration (`OID-FED`_ Sezione 3.1.2):

- **metadata** (``metadata``): Oggetto JSON OBBLIGATORIO in cui ciascuna chiave è un identificatore di tipo di metadata e il suo valore è il metadata di tale tipo (vedi `OID-FED`_ Sezione 3.1.1).
  Tutte le Entità DEVONO includere almeno un metadata per ``federation_entity`` nelle proprie Entity Configuration, e POSSONO includere più di una dichiarazione di metadata, ma solo una per ciascun tipo di metadata.
  I tipi di metadata sono definiti in :ref:`infrastructure-trust:Entity Type Identifiers and Metadata`.
- **trust_marks** (``trust_marks``): OBBLIGATORIO per Foglie e Federation Intermediate.
  Array JSON dei Trust Mark del subject.
  Il Trust Mark di registrazione è definito in :ref:`infrastructure-trust:Trust Mark registration-entity`.
- **trust_mark_issuers** (``trust_mark_issuers``): OBBLIGATORIO solo per Federation TA e NON DEVE essere incluso altrimenti.
  Oggetto JSON che dichiara, per ciascun tipo di Trust Mark, le Federation Authority fidate a emetterlo, indicate dai loro Federation Entity Identifier.
  All'interno di IT-Wallet il Trust Mark di registrazione è emesso solo dal Federation Trust Anchor, quindi DEVE contenere almeno l'identificatore del Federation TA.

Nel Subordinate Statement (`OID-FED`_ Sezione 3.1.3):

- **metadata_policy** (``metadata_policy``): OPZIONALE in `OID-FED`_.
  Metadata policy vincolata a un tipo di metadata specifico e applicata al sottoalbero, risolta combinando i Claim ``metadata_policy`` lungo la Trust Chain, come definito in `OID-FED`_ Sezione 6.1.4.
  All'interno di IT-Wallet il Subordinate Statement relativo a una Foglia DEVE recare una ``metadata_policy`` che vincola i metadata di protocollo della Foglia ai valori approvati in onboarding.
  Usando gli operatori di metadata policy di `OID-FED`_ Sezione 6.1.3, DEVE fissare l'``organization_name`` dei metadata ``federation_entity``, le chiavi di firma di protocollo (``jwks``) e, quando presente nel tipo di metadata, gli endpoint di servizio e gli URI di request, response e redirect (per esempio i ``request_uris``, ``response_uris`` e ``redirect_uris`` di ``openid_credential_verifier``).
  Questo Subordinate Statement è emesso dal superiore immediato che ha registrato la Foglia, cioè il Federation TA per le Foglie che registra direttamente e un Federation Intermediate per le sue Relying Party affiliate.
  Il Subordinate Statement relativo a un Federation Intermediate non reca una ``metadata_policy``, perché l'Intermediate non ha metadata di protocollo e le sue Relying Party affiliate sono vincolate dall'Intermediate stesso.
  Un superiore PUÒ restringere ulteriormente la metadata policy impostata dai propri superiori, ma NON DEVE allentarla, come definito in `OID-FED`_ Sezione 6.1.1.
- **constraints** (``constraints``): OBBLIGATORIO solo per Federation TA.
  Reca i vincoli applicati al sottoalbero al di sotto dell'issuer.
  DEVE contenere ``allowed_entity_types``, che restringe i metadata Entity Type che i Subordinate nel sottoalbero sono autorizzati a pubblicare, e ``max_path_length``, che limita il numero di Intermediate tra l'issuer e il subject della Trust Chain.
  L'Entity Type ``federation_entity`` è sempre consentito e NON DEVE essere elencato in ``allowed_entity_types``.
  Vedi `OID-FED`_ Sezione 6.2.

Tutti gli altri parametri opzionali definiti in `OID-FED`_ Sezione 3 che non sono riconosciuti all'interno del profilo delle specifiche IT-Wallet DEVONO essere ignorati durante la valutazione di un Entity Statement.

.. note::
  All'interno di IT-Wallet le Federation Entity Keys recate nel ``jwks`` di un'Entity Configuration o di un Subordinate Statement sono usate per firmare le dichiarazioni di federazione e sono validate attraverso la Federation Trust Chain, non attraverso X.509.
  La PKI di firma X.509, i cui certificati sono usati per firmare le Attestation, è una relazione di fiducia separata.
  I Signing Trust Anchor di questa PKI sono distribuiti nell'Entity Configuration del Federation Trust Anchor.
  Ciascuno è fornito nel parametro ``x5c`` (:rfc:`7517` Sezione 4.7) di una JWK dedicata all'interno del ``jwks``, distinta dalle Federation Entity Keys, che non recano ``x5c``, come definito in :ref:`trust-evaluation:Signing Trust Anchor Distribution`.
  I certificati Document Signer dei Credential Issuer non sono recati nel ``jwks`` degli Entity Statement: sono inclusi nelle Attestation firmate, nell'header ``x5chain`` per il formato mdoc e nell'header ``x5c`` per il formato JOSE, e sono validati come definito in :ref:`trust-evaluation:X.509 Certificate Chain Validation`.
  L'emissione di questi Certificati X.509 e l'operazione della PKI di firma sono definite nell'onboarding (vedi :ref:`onboarding-system:Onboarding Processes`).

Entity Type Identifiers and Metadata
""""""""""""""""""""""""""""""""""""

Gli Entity Type Identifier dei ruoli dell'ecosistema sono definiti in OpenID Federation for Wallet Architectures, sezione Wallet Architecture Entity Types, che è il profilo wallet di OpenID Federation.
Ciascun ruolo dichiara nella propria Entity Configuration uno o più tipi di metadata, i cui parametri seguono la specifica di protocollo di tale tipo di metadata.
La tabella seguente mappa i ruoli dell'ecosistema sui loro Entity Type Identifier e fornisce il riferimento del protocollo di metadata per ciascuno di essi.

.. warning::
  All'interno di IT-Wallet il tipo di metadata del Wallet Provider DEVE essere ``wallet_solution``.
  Questa è una deviazione da OpenID Federation for Wallet Architectures, che nomina il corrispondente Entity Type Identifier ``openid_wallet_provider``.

.. list-table::
   :class: longtable
   :widths: 25 75
   :header-rows: 1

   * - **Entità**
     - **Metadata Type**
   * - Trust Anchor
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
  In qualità di intermediario non è coinvolto nei flussi di protocollo, quindi non pubblica un metadata di protocollo proprio, solo i metadata ``federation_entity``.
  Pubblica i Subordinate Statement delle sue Relying Party affiliate, e ciascuna Relying Party affiliata imposta i propri ``authority_hints`` sull'Intermediary.
  Il suo Trust Mark di registrazione usa l'Entity Type Identifier ``intermediate`` nel tipo di Trust Mark, come definito in :ref:`infrastructure-trust:Trust Mark Types and Schema`.

.. note::
  Quando un PID o EAA Provider implementa sia il Credential Issuer sia l'Authorization Server all'interno della stessa Entità, DEVE includere sia ``openid_credential_issuer`` sia ``oauth_authorization_server`` nei suoi tipi di metadata.
  Quando l'Authorization Server è un'Entità separata, i metadata del Credential Issuer DEVONO contenere il parametro ``authorization_servers`` con l'identificatore dell'Authorization Server.
  Secondo `OPENID4VCI`_ l'Authorization Server PUÒ essere esterno all'Entità che implementa il Credential Endpoint, pertanto l'uso di ``oauth_authorization_server`` è OPZIONALE.
  Inoltre, qualora sia necessaria l'Autenticazione dell'Utente da parte del Credential Issuer, potrebbe essere necessario includere il tipo di metadata rilevante ``openid_credential_verifier``.

I metadata ``federation_entity`` recano i parametri informativi seguenti insieme ai parametri degli endpoint di federazione.
I parametri degli endpoint di federazione (``federation_fetch_endpoint``, ``federation_list_endpoint``, ``federation_resolve_endpoint`` e gli altri) sono pubblicati solo dal Federation TA e dagli Intermediate, secondo i loro obblighi definiti nella sezione Federation API Endpoints sopra, e una Foglia non li espone.
I parametri informativi seguenti sono OPZIONALI in `OID-FED`_; il profilo delle specifiche IT-Wallet supporta i claim nella tabella seguente.

.. list-table::
  :class: longtable
  :widths: 25 75
  :header-rows: 1

  * - **Claim**
    - **Descrizione**
  * - **organization_name**
    - OBBLIGATORIO.
      Vedi `OID-FED`_ Sezione 5.2.2
  * - **homepage_uri**
    - OBBLIGATORIO.
      Vedi `OID-FED`_ Sezione 5.2.2
  * - **policy_uri**
    - OBBLIGATORIO.
      Vedi `OID-FED`_ Sezione 5.2.2
  * - **logo_uri**
    - OBBLIGATORIO.
      URL del logo dell'entità, in formato SVG.
      Vedi `OID-FED`_ Sezione 5.2.2
  * - **contacts**
    - OBBLIGATORIO.
      All'interno di IT-Wallet è l'indirizzo email verificato istituzionale (PEC) dell'entità.
      Vedi `OID-FED`_ Sezione 5.2.2
  * - **tos_uri**
    - OPZIONALE.
      URL dei termini di servizio dell'entità.
      Vedi `OID-FED`_ Sezione 5.2.2

I metadata relativi a Wallet Provider, Credential Issuer e Relying Party sono forniti nella Sezione :ref:`wallet-solution-metadata:Metadati della Soluzione Wallet`, :ref:`credential-issuer-solution:Metadata del Fornitore di Attestati Elettronici` e :ref:`relying-party-metadata:Metadati della Relying Party` rispettivamente.

Entity Statement Examples
^^^^^^^^^^^^^^^^^^^^^^^^^

Le sezioni seguenti forniscono esempi non normativi di Entity Statement, sia per l'onboarding diretto sotto il Federation TA sia per l'onboarding intermediato sotto un Federation Intermediate.
Tutte le dichiarazioni sono JWT firmati con l'header JOSE ``alg``, ``kid`` e ``typ`` impostato a ``entity-statement+jwt``, e sono mostrati solo i payload.
I metadata di protocollo e i key set pinnati sono troncati (``{ ... }``) poiché la loro definizione completa è fornita nelle sezioni di metadata referenziate sopra.

Entity Configuration of a Federation TA
"""""""""""""""""""""""""""""""""""""""

Il Federation TA è la root della Trust Chain.
La sua Entity Configuration non ha ``authority_hints``, e il suo ``jwks`` fornisce, in aggiunta alle Federation Entity Keys, i Signing Trust Anchor della PKI di firma X.509 e gli Authentication Trust Anchor della PKI di autenticazione X.509, come JWK dedicate con ``x5c``.
Un Signing Trust Anchor è la root della PKI che emette i certificati Document Signer; un Authentication Trust Anchor è la root della PKI che emette i certificati di autenticazione della Relying Party usati per l'mdoc reader authentication nel Proximity Flow.
Ciascuna tale JWK è identificata dal suo ``kid`` e dalle proprietà del certificato fornito nel suo ``x5c``.

.. literalinclude:: ../../examples/oidfed-ec-federation-ta.json
  :language: JSON

Subordinate Statement of Leaf issued by the Federation TA
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Il Federation TA emette un Subordinate Statement su ciascuna Foglia che registra direttamente.
La dichiarazione reca le Federation Entity Keys della Foglia, la ``metadata_policy`` che fissa le chiavi di protocollo e, quando presenti, gli endpoint di servizio e gli URI della Foglia ai valori approvati in onboarding, e i ``constraints`` del sottoalbero.

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
I ``constraints`` restringono il sottoalbero dell'Intermediate alle Relying Party che può intermediare, e ``max_path_length`` è impostato a 1 per consentire il singolo livello di intermediazione tra il Federation TA e le Relying Party affiliate.
Non reca ``metadata_policy``: le Relying Party affiliate sono vincolate dall'Intermediate nei Subordinate Statement che emette su di esse.

.. literalinclude:: ../../examples/oidfed-ss-intermediate.json
  :language: JSON

Subordinate Statement about a Leaf issued by a Federation Intermediate
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Il Federation Intermediate emette un Subordinate Statement su ciascuna Relying Party affiliata.
Reca la ``metadata_policy`` che vincola i metadata di protocollo della Relying Party affiliata ai valori approvati in onboarding, esattamente come fa il Federation TA per le Foglie che registra direttamente.
I ``constraints`` del sottoalbero sono impostati dal Federation TA nella dichiarazione relativa all'Intermediate.
Nel Trust Framework Nazionale un Intermediary intermedia solo Relying Party.

.. literalinclude:: ../../examples/oidfed-ss-intermediate-leaf.json
  :language: JSON

Entity Configuration of a Federation Intermediate
"""""""""""""""""""""""""""""""""""""""""""""""""

Il Federation Intermediate è solo una ``federation_entity``.
La sua Entity Configuration punta al Federation TA attraverso ``authority_hints`` e reca il suo Trust Mark di registrazione con l'Entity Type Identifier ``intermediate``.
Espone gli endpoint fetch e list usati per servire i Subordinate Statement delle sue Relying Party affiliate.

.. literalinclude:: ../../examples/oidfed-ec-federation-intermediate.json
  :language: JSON

Entity Configuration of a Leaf
""""""""""""""""""""""""""""""

Ciascuna Foglia pubblica la propria Entity Configuration, puntando al proprio superiore immediato attraverso ``authority_hints`` e recando il proprio Trust Mark di registrazione.
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

A seguito del completamento con successo dell'onboarding, le entità ricevono i Trust Mark della Federazione IT-Wallet.
I Trust Mark sono emessi dalla Federation Authority (Trust Anchor per l'onboarding diretto, Intermediate per l'onboarding mediato) attraverso il Federation Trust Mark Endpoint e servono come attestation verificabili relative alla conformità ai profili tecnici IT-Wallet e/o alle policy di autorizzazione.

Trust Mark Types and Schema
"""""""""""""""""""""""""""

Gli identificatori dei Trust Mark DEVONO seguire uno schema gerarchico che riflette lo scope di autorizzazione:

``https://<federation_authority_domain>/trust_marks/<purpose>/<entity_type>``

Dove:

  - ``<federation_authority_domain>``: Il dominio della Federation Authority emittente.
  - ``<purpose>``: Lo scopo del Trust Mark.
    Lo scopo ``registration-entity`` è **OBBLIGATORIO** per tutte le entità a seguito del processo di onboarding.
    Scopi aggiuntivi di Trust Mark POSSONO essere definiti per esigenze future, ma non sono richiesti per i processi di autorizzazione definiti in :ref:`trust-evaluation:Authorization`.
  - ``<entity_type>``: L'Entity Type Identifier del subject, tra quelli definiti in :ref:`infrastructure-trust:Entity Type Identifiers and Metadata` (per esempio ``openid_credential_issuer`` o ``openid_credential_verifier``), e ``intermediate`` per un Relying Party Intermediary.

.. note::
  Il Federation TA è l'issuer di Trust Mark riconosciuto all'interno della federazione e l'unica Entità che può abilitare altri issuer di Trust Mark usando il parametro ``trust_mark_issuers`` nella propria Entity Configuration.
  Scopi aggiuntivi di Trust Mark, quando definiti, POSSONO quindi essere emessi da altre Entità autorizzate attraverso ``trust_mark_issuers``.

Trust Mark registration-entity
"""""""""""""""""""""""""""""""

All'interno di IT-Wallet il Trust Mark ``registration-entity`` è il Trust Mark di registrazione di un'entità.
L'unico issuer di Trust Mark per il Trust Mark di registrazione DEVE essere il Federation TA.
Attesta la registrazione e reca i dati di autorizzazione dell'entità, cioè le sue entitlement e, ove applicabile, le Credenziali e gli attributi che è autorizzata a emettere o a richiedere.
Questo Trust Mark di registrazione è l'analogo funzionale del Wallet-Relying Party Registration Certificate (WRPRC) del Trust Framework EUDIW.
Un'entità riceve un Trust Mark di registrazione per ciascun ruolo che detiene, con il componente ``<entity_type>`` dell'identificatore impostato di conseguenza.

Un Relying Party Intermediary riceve il proprio Trust Mark di registrazione con l'``<entity_type>`` ``intermediate`` nell'identificatore.

Nel Trust Framework EUDIW la relazione di intermediario è espressa nei dati di registrazione della Relying Party intermediata.
Nel Trust Framework Nazionale, invece, è espressa attraverso la gerarchia di federazione: l'Intermediary è un Federation Intermediate che pubblica i Subordinate Statement delle sue Relying Party affiliate, e ciascuna Relying Party affiliata imposta i propri ``authority_hints`` sull'Intermediary.
Il Trust Mark di registrazione di ciascuna Relying Party affiliata è altresì emesso dal Federation Trust Anchor.
Per questo motivo nessun campo dedicato all'intermediario è presente nel Trust Mark.
L'onboarding dell'Intermediary è definito in :ref:`onboarding-system:Relying Party Intermediary`.

**Trust Mark Structure**

I Trust Mark nell'Entity Configuration DEVONO essere rappresentati come oggetti JSON contenenti i seguenti claim:

.. list-table:: Claim dell'Oggetto Trust Mark (nell'Entity Configuration)
   :class: longtable
   :header-rows: 1
   :widths: 25 75

   * - **Claim**
     - **Descrizione**
   * - **trust_mark_type**
     - OBBLIGATORIO.
       Identificatore per il tipo di Trust Mark che segue lo schema: ``https://<federation_authority_domain>/trust_marks/<purpose>/<entity_type>``.
   * - **trust_mark**
     - OBBLIGATORIO.
       Un JSON Web Token firmato che rappresenta il Trust Mark emesso dalla Federation Authority.

Il Trust Mark JWT (contenuto nel claim ``trust_mark`` sopra) DEVE essere un JWT firmato che include sia un header JOSE sia un payload, come definito in `OID-FED`_ Sezione 7.

**Trust Mark JWT Header**

L'header JOSE del Trust Mark JWT DEVE includere i seguenti parametri:

.. list-table:: Parametri dell'Header JWT del Trust Mark
   :class: longtable
   :header-rows: 1
   :widths: 25 75

   * - **Parameter**
     - **Descrizione**
   * - **alg**
     - OBBLIGATORIO.
       L'algoritmo crittografico usato per firmare il Trust Mark JWT.
       DEVE essere uno degli algoritmi supportati per le Federation Entity Keys (vedi :ref:`algorithms:Algoritmi Crittografici`).
   * - **kid**
     - OBBLIGATORIO.
       Key ID della Federation Entity Key usata per firmare il Trust Mark, come definito in `OID-FED`_ Sezione 7.
   * - **typ**
     - OBBLIGATORIO.
       Media type del Trust Mark JWT.
       DEVE essere impostato a ``trust-mark+jwt``, come definito in `OID-FED`_ Sezione 7, a meno che un media type più specifico non sia definito dal trust framework per il particolare tipo di Trust Mark.
       I Trust Mark senza un parametro di header ``typ`` o con un valore ``typ`` non riconosciuto DEVONO essere rifiutati.

Un esempio non normativo di un header JWT di Trust Mark:

.. code-block:: JSON

  {
    "alg": "ES256",
    "kid": "ta-federation-key-1",
    "typ": "trust-mark+jwt"
  }

**Trust Mark JWT Payload**

Il payload del Trust Mark JWT include i seguenti claim:

.. list-table:: Claim JWT del Trust Mark
   :class: longtable
   :header-rows: 1
   :widths: 25 75

   * - **Claim**
     - **Descrizione**
   * - **iss**
     - OBBLIGATORIO.
       Il Federation Trust Anchor che emette il Trust Mark.
   * - **sub**
     - OBBLIGATORIO.
       Federation Entity Identifier del subject.
   * - **trust_mark_type**
     - OBBLIGATORIO.
       Identificatore univoco del Trust Mark.
       DEVE corrispondere al claim ``trust_mark_type`` dell'Oggetto Trust Mark.
   * - **iat**
     - OBBLIGATORIO.
       Timestamp di emissione del Trust Mark.
   * - **exp**
     - OBBLIGATORIO.
       Timestamp di scadenza del Trust Mark.
   * - **public_body**
     - OBBLIGATORIO.
       Booleano che indica se l'entità è un organismo del settore pubblico.
   * - **vat_number**
     - OBBLIGATORIO quando ``public_body`` è ``false``.
       Partita IVA dell'entità.
       PUÒ essere presente anche quando ``public_body`` è ``true``.
   * - **legal_identifier**
     - RACCOMANDATO.
       Numero o identificatore di registrazione legale dell'entità (ad es., numero di registrazione dell'impresa, codice fiscale).
   * - **ipa_code**
     - OBBLIGATORIO quando ``public_body`` è ``true``, NON DEVE essere presente altrimenti.
       Codice IPA (Indice delle Pubbliche Amministrazioni) dell'entità del settore pubblico.
   * - **organization_name**
     - OBBLIGATORIO.
       Denominazione completa dell'Entità Organizzativa.
   * - **email**
     - OBBLIGATORIO.
       Email istituzionale o PEC dell'organizzazione.
   * - **support_uri**
     - OBBLIGATORIO.
       URL o indirizzo email da usare per le richieste relative all'entità, come la cancellazione o la portabilità dei dati.
   * - **srv_description**
     - OBBLIGATORIO.
       Descrizione multilingue del servizio fornito dall'entità.
       Ciascuna entry contiene ``lang`` e ``value``.
   * - **entitlements**
     - OBBLIGATORIO.
       Array di URI di entitlement che identificano il ruolo del subject, come definito in `ETSI TS 119 475`_ Allegato A.2 (ad es. ``Service_Provider``, ``PID_Provider``, ``QEAA_Provider``, ``PUB_EAA_Provider``, ``Non_Q_EAA_Provider``).
   * - **provides_attestations**
     - OBBLIGATORIO per un Credential Issuer, NON DEVE essere presente altrimenti.
       Array dei tipi di Credenziale che il subject è autorizzato a emettere.
       Ciascuna entry contiene ``format``, ``meta`` per identificare il tipo di Credenziale, e un array ``claim`` opzionale.
   * - **credentials**
     - OBBLIGATORIO per una Relying Party che richiede Credenziali, NON DEVE essere presente altrimenti.
       Array delle query di Credenziale che il subject è autorizzato a richiedere, usato per l'Overasking Check.
       Ciascuna entry contiene ``format``, ``meta`` (ad es. ``vct_values`` o ``doctype_value``) e un array ``claim`` dei path di attributo autorizzati.
   * - **purpose**
     - OBBLIGATORIO per una Relying Party che richiede Credenziali, NON DEVE essere presente altrimenti.
       Elenco multilingue che descrive il trattamento dei dati associato all'uso previsto.
       Ciascuna entry contiene ``lang`` e ``value``.
   * - **privacy_policy**
     - OBBLIGATORIO per una Relying Party che richiede Credenziali, NON DEVE essere presente altrimenti.
       URL della privacy policy del subject.
   * - **supervisory_authority**
     - OBBLIGATORIO.
       Informazioni sull'Autorità di protezione dei dati, con ``uri``, ``email`` e ``phone``.
   * - **logo_uri**
     - OBBLIGATORIO.
       URL che punta al :ref:`brand-identity:Trust Mark` per scopi UI/UX.
   * - **ref**
     - OPZIONALE.
       URL con informazioni web aggiuntive sul Trust Mark.

.. note::
  I claim che recano i dati di autorizzazione (``entitlements``, ``provides_attestations``, ``credentials``, ``purpose``, ``privacy_policy``, ``supervisory_authority``) e i claim di identità e trasparenza allineati al WRPRC (``public_body``, ``support_uri``, ``srv_description``) sono definiti in analogia con il Wallet-Relying Party Registration Certificate EUDIW (`ETSI TS 119 475`_), in modo che un Trust Evaluator possa riutilizzare la stessa logica di autorizzazione per entrambi gli artifact.

.. note::
  Lo status di revoca di un Trust Mark è verificato attraverso l'endpoint **trust mark status** (``/trust_mark_status``) (`OID-FED`_ Sezione 8.4), non attraverso una status list recata nel token.
  Questa è la differenza rispetto al WRPRC, il cui claim ``status`` punta a una status list: il Trust Mark si affida al meccanismo di revoca nativo della federazione.
  Il consumo di questi claim da parte del Trust Evaluator è definito in :ref:`trust-evaluation:Authorization`.

Gli esempi non normativi seguenti illustrano il contenuto del Trust Mark JWT di registrazione per un Credential Issuer, un EAA Provider pubblico non qualificato che emette un Employee Badge, per una Relying Party che richiede tale Employee Badge, e per un Relying Party Intermediary.

Credential Issuer, un EAA Provider pubblico non qualificato che emette l'Employee Badge:

.. literalinclude:: ../../examples/oidfed-trust-mark-credential-issuer.json
  :language: JSON

Relying Party, un'organizzazione privata che richiede l'Employee Badge per il controllo degli accessi fisici:

.. literalinclude:: ../../examples/oidfed-trust-mark-relying-party.json
  :language: JSON

Relying Party Intermediary.
Non dichiara un uso previsto proprio, quindi il suo Trust Mark di registrazione non reca ``credentials`` né ``purpose``.
È un Federation Intermediate, e le sue Relying Party affiliate impostano i propri ``authority_hints`` su di esso.

.. literalinclude:: ../../examples/oidfed-trust-mark-intermediate.json
  :language: JSON

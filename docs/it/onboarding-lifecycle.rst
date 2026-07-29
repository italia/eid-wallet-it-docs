.. include:: ../common/common_definitions.rst
.. Included via onboarding-system.rst at title level '-' (level 1).

Lifecycle Management
--------------------

Dopo l'evento di registrazione, un'Entity può essere aggiornata, sospesa, riattivata o cancellata, e un Credential type può diventare emettibile o cessare di esserlo; tali modifiche si riflettono sui Trust Artifacts e sui registri.

Questa sezione descrive gli stati e gli eventi che determinano il cambio di stato di un'entità o di un credential type. Mappa inoltre ciascun evento sui registri e sui trust artefact impattati dall'evento. (:ref:`onboarding-system:Events, Registries and Trust Artifacts`).

I formati, i parametri e gli stati dei Trust Artifacts sono definiti in :ref:`infrastructure-trust:Trust Artifacts Lifecycle State Machine`, e i meccanismi di revoca sono definiti in :ref:`infrastructure-trust:Revocation Mechanisms`.
Il lifecycle delle singole Digital Credentials emesse agli User è un tema distinto ed è definito in :ref:`credential-revocation:Ciclo di Vita degli Attestati Elettronici`.

Entity Lifecycle State Machine
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Questa sezione si applica alle Entity WRP e WP in quanto direttamente coinvolte nelle fasi operative. Come mostrato in :numref:`fig_Entity_Lifecycle_States`, un'Entity ha cinque stati distinti e mutuamente esclusivi: ``UNREGISTERED``, ``REGISTERED``, ``OPERATIONAL``, ``SUSPENDED`` e ``CANCELLED``.
Ciascuno stato determina il livello di autorizzazione e le capacità operative dell'Entity.

.. _fig_Entity_Lifecycle_States:
.. plantuml:: plantuml/entity-lifecycle-states.puml
    :width: 70%
    :alt: The figure illustrates the lifecycle states of an Entity and the transitions between them.
    :caption: `Entity Lifecycle States. <https://www.plantuml.com/plantuml/svg/TP91RiCW44Ntd6BMbNA1BgfO3geYMKva9wkq2meJ1na3Od2IthxONSHrwkKmxy-V3wmfYX3xph2BLWZO-VWD2aa6xQDsbb6hhHT1TF0bPDi4rrkLE-C2n20ifHRQEA7e8fIxQTl0MHX2nauldx1QlS6nhFZxjZxmYcyOcrPZUrA-Gi16Kve_R03ITTvWHCLcajsULzbXkokp8cbYw2b22gFFGaO2JTGdpHHwyfbhyEvrGFLXKxo0LzUc0NFN-bZlURaPzTIJHql3FSrz5h37yJ-XqmxwEeP-SispCkT5CO9IM8d6_89ptqNmh_CYnXwTWKklnzPerV13VW00>`_

**Transition from UNREGISTERED to REGISTERED**

- ``UNREGISTERED``: l'Entity non detiene una registrazione valida nell'ecosistema IT-Wallet.
  Questo è lo stato di base predefinito.
  Le Entity in questo stato sono fuori dal trust boundary e NON DEVONO partecipare ad alcuna operazione.
- ``REGISTERED``: l'Entity ha completato il processo di registrazione e la sua identità è stata verificata.

  - *EUDIW Trust Framework*: le WRP sono in stato ``REGISTERED`` quando le loro informazioni sono state aggiunte al Register.
    I Wallet Provider diventano ``REGISTERED`` quando i record di certificazione e di onboarding sono stati raccolti e verificati.
  - *National Trust Framework*: le WRP e i Wallet Provider sono in stato ``REGISTERED`` quando i record di onboarding sono stati raccolti e verificati.

**Transition from REGISTERED to OPERATIONAL**

``OPERATIONAL`` indica che l'Entity è stata autorizzata a eseguire le operazioni relative al proprio ruolo.

- *EUDIW Trust Framework*: le WRP sono ``OPERATIONAL`` se erano ``REGISTERED`` e hanno ottenuto un WRPAC, opzionalmente un WRPRC e, a seconda del ruolo, un Sign/Seal Certificate.
  Il signing Trust Anchor di tale certificato DEVE essere stato aggiunto alla LoTE o alla EUMS TL.
  I Wallet Provider sono ``OPERATIONAL`` se erano ``REGISTERED`` e hanno ottenuto un Sign/Seal Certificate il cui signing Trust Anchor è stato aggiunto alla LoTE.
- *National Trust Framework*: le WRP e i Wallet Provider sono ``OPERATIONAL`` se erano ``REGISTERED``, hanno ottenuto i Sign/Seal Certificate e i registration Trust Mark, e il loro Subordinate Statement è stato pubblicato dalla Federation Authority.

**Transition from OPERATIONAL to REGISTERED**

Un'Entity torna a ``REGISTERED`` quando non detiene più Trust Artifacts validi.
Ciò può essere innescato dalla loro scadenza o dalla loro revoca a seguito di un aggiornamento dell'Entity.
Per tornare a ``OPERATIONAL`` è richiesta una nuova emissione dei Trust Artifacts.

**Transition from REGISTERED or OPERATIONAL to SUSPENDED**

``SUSPENDED`` indica che la registrazione non è temporaneamente valida.
A differenza della cancellazione, la sospensione è reversibile.
Una WRP la cui registrazione è sospesa NON DEVE emettere Credential alle Wallet Unit né richiedere attributi da esse, e le Credential da essa emesse non sono accettate dalle Relying Party, come descritto nella Section 4.6.5 di [`EIDAS-ARF`_].

Gli eventi che portano a questo stato, e le parti abilitate a decidere, sono elencati in :ref:`onboarding-system:Registration Events and Their Governance`.

**Transition from SUSPENDED to REGISTERED**

La sospensione può essere revocata dalla stessa parte che l'ha decisa.
Poiché i Trust Artifacts interessati dalla sospensione sono stati revocati, l'Entity torna a ``REGISTERED`` e non direttamente a ``OPERATIONAL``, ed è richiesta una nuova emissione dei Trust Artifacts per tornare di nuovo ``OPERATIONAL``.

**Transition from REGISTERED, OPERATIONAL or SUSPENDED to CANCELLED**

``CANCELLED`` indica che la registrazione è terminata.
Lo stato è lo stesso sia che la cancellazione sia stata richiesta dall'Entity stessa sia che sia stata decisa dall'autorità competente; differisce solo l'evento scatenante.

- *EUDIW Trust Framework*: per le WRP comporta la revoca del WRPAC, del WRPRC e dei Sign/Seal Certificate, la rimozione della voce dal Register e l'aggiornamento dello stato del signing Trust Anchor nella LoTE o nella EUMS TL.
  Per i Wallet Provider comporta l'aggiornamento della Wallet Providers LoTE.
- *National Trust Framework*: per WRP e Wallet Provider comporta la rimozione del Subordinate Statement e del registration Trust Mark, e la revoca dei Sign/Seal Certificate.

Un'Entity DEVE rifiutare nuove interazioni o transazioni avviate da un'Entity ``CANCELLED``, e tutte le chiavi crittografiche, le attestation attive e le capacità operative associate all'Entity DEVONO essere revocate.
Le Entity POSSONO tuttavia continuare a convalidare dati storici, firme e Credential generate prima del timestamp di cancellazione, fatte salve le policy di rischio locali.
Un'Entity in stato ``CANCELLED`` che intende partecipare di nuovo all'ecosistema DEVE completare una nuova registrazione.

.. note::
  La Section 4.6.5 di [`EIDAS-ARF`_] descrive per PID Provider e Attestation Provider gli stati **Registered**, **Suspended** e **Cancelled**.
  Nell'IT-Wallet lo stato **Registered** è suddiviso in ``REGISTERED`` e ``OPERATIONAL``, per distinguere il momento in cui esiste il record di registrazione dal momento in cui l'Entity detiene tutti i Trust Artifacts necessari a operare.

.. note::
  Il lifecycle delle Authentic Sources e delle Entity dell'infrastruttura di trust, come il Registrar e i Provider of WRPACs, non è definito in questa sezione.
  Le Authentic Sources seguono il framework PDND, e gli effetti che il loro lifecycle produce nell'IT-Wallet sono descritti in :ref:`onboarding-system:Authentic Source Lifecycle and PDND Alignment`.

Registration Events and Their Governance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Ogni transizione della macchina a stati delle Entity è causata da un evento.
Per ciascun evento, questa sezione indica chi è abilitato a innescarlo, chi ne è responsabile e, ove applicabile, su quale base normativa e entro quali condizioni.
Gli eventi che riguardano i Credential types e le Authentic Sources sono descritti nelle sezioni dedicate di seguito.

.. _table_registration_events:
.. list-table:: Registration Events
   :class: longtable
   :widths: 16 26 16 22 20
   :header-rows: 1

   * - **Event**
     - **Trigger**
     - **Responsible**
     - **Normative reference**
     - **Condition**

   * - Registration
     - Richiesta dell'Entity, dopo la verifica delle condizioni di idoneità applicabili al suo ruolo.
     - Registrar, per la voce nel Register. Federation Authority, per la federation registration.
     - Articles 5 and 6 of [`CIR2025/848`_].
     - Not defined.

   * - Update
     - Modifica delle informazioni registrate. La WRP è responsabile dell'accuratezza delle proprie informazioni e le aggiorna.
     - Registrar, per la voce nel Register. Federation Authority, per il Subordinate Statement e il registration Trust Mark.
     - Article 5(2) and 5(3) of [`CIR2025/848`_].
     - Without undue delay.

   * - Suspension
     - Richiesta di un Supervisory Body, richiesta della WRP stessa, o iniziativa del Registrar nei casi elencati dopo questa tabella.
     - Registrar per il Trust Framework EUDIW, Federation Authority per il National Trust Framework.
     - Article 9(1), 9(2) and 9(3) of [`CIR2025/848`_].
     - Notification within 24 hours.

   * - Reactivation
     - Rimozione della condizione che ha causato la sospensione.
     - La stessa parte che ha deciso la sospensione.
     - Section 4.6.5 of [`EIDAS-ARF`_].
     - Not defined.

   * - Cancellation
     - Richiesta di un Supervisory Body, richiesta della WRP stessa inclusa quando non intende più fare affidamento sulle Wallet Unit, o iniziativa del Registrar nei casi elencati dopo questa tabella.
     - Registrar per il Trust Framework EUDIW, Federation Authority per il National Trust Framework.
     - Article 9(1), 9(2) and 9(3) of [`CIR2025/848`_].
     - Notification within 24 hours.

Due ruoli eseguono un evento, uno per ciascun Trust Framework.
Nel Trust Framework EUDIW il Registrar agisce sul Register e notifica i Provider dei Trust Artifacts interessati.
Nel National Trust Framework la Federation Authority agisce sul Subordinate Statement e sul registration Trust Mark, e pubblica l'evento sul Federation Subordinate Events Endpoint.
La decisione che innesca l'evento è la stessa per entrambi, ed è descritta di seguito con riferimento al Registrar, poiché gli obblighi sono imposti al Registrar da [`CIR2025/848`_].

Il Registrar DEVE sospendere o cancellare la registrazione di una WRP ove la sospensione o la cancellazione sia richiesta da un Supervisory Body, e ove sia richiesta dalla WRP stessa.
Il Registrar PUÒ sospendere o cancellare la registrazione di propria iniziativa ove:

  - la registrazione contenga informazioni inaccurate, non aggiornate o fuorvianti;
  - la WRP non sia conforme alla registration policy;
  - la WRP richieda più attributi di quelli registrati;
  - la WRP agisca altrimenti in violazione del diritto dell'Unione o nazionale in modo correlato al proprio ruolo.

Prima di sospendere o cancellare una registrazione di propria iniziativa, il Registrar DEVE condurre una proportionality assessment, tenendo conto dell'impatto sui diritti fondamentali, la privacy, la sicurezza e la riservatezza degli User dell'ecosistema, la gravità dell'interruzione causata dalla misura e i costi associati, sia per la WRP sia per l'User.

Il Registrar DEVE informare la WRP e i Provider rilevanti di WRPAC e WRPRC senza indebito ritardo, e in ogni caso entro 24 ore.
Dopo la notifica, i Provider DEVONO revocare i certificati interessati senza indebito ritardo, ove applicabile.

Il Registrar DEVE conservare i record della registrazione, dei dati di emissione e delle modifiche per 10 anni.
Nell'IT-Wallet la stessa conservazione si applica per analogia alla Federation Authority per i record del National Trust Framework.

.. note::
  Gli obblighi descritti sopra sono imposti dagli Articles 9 and 10 di [`CIR2025/848`_] e si applicano al Registrar e alla registrazione delle WRP.
  Nell'IT-Wallet l'obbligo di conservazione è esteso per analogia alla Federation Authority per i record che mantiene per il National Trust Framework, poiché [`CIR2025/848`_] non tratta il National Trust Framework.
  I Wallet Provider non sono registrati come WRP, quindi la sospensione e la cancellazione di un Wallet Provider derivano dalla certificazione della sua Wallet Solution e dalla notifica, e non dall'Article 9.

Indipendentemente dalla notifica descritta sopra, i Provider of WRPACs e i Provider of WRPRCs monitorano le modifiche nel Register in modo continuativo, e revocano o riemmettono i certificati quando le modifiche lo richiedono.
Ciò è imposto dall'Annex IV di [`CIR2025/848`_] per i Provider of WRPACs e dall'Annex V di [`CIR2025/848`_] per i Provider of WRPRCs.

Nel National Trust Framework gli eventi che modificano la registrazione di un'Entity DEVONO essere pubblicati dalla Federation Authority come eventi firmati sul Federation Subordinate Events Endpoint (``federation_subordinate_events_endpoint``), affinché gli altri partecipanti possano tracciare il lifecycle di un'Entity nel tempo.
L'endpoint e il formato della sua risposta sono descritti in :ref:`infrastructure-trust:Federation API Endpoints`.

Ciascun evento della macchina a stati DEVE essere pubblicato come oggetto dell'array ``federation_registration_events``, usando i tipi di evento definiti in [`OID-FED-SUBORDINATE-EVENTS`_].
La tabella di seguito indica, per ciascun evento, il valore del parametro ``event`` e come sono popolati i parametri dell'oggetto evento.

.. _table_subordinate_events_mapping:
.. list-table:: Mapping of the Lifecycle Events to the Subordinate Events
   :class: longtable
   :widths: 26 24 22 28
   :header-rows: 1

   * - **Lifecycle event**
     - **event**
     - **iat**
     - **event_description**

   * - Registration
     - ``registration``
     - Tempo a cui la registrazione è correlata.
     - Not used.

   * - Update of Identity Information or Technical Configuration
     - ``metadata_update``
     - Tempo a cui l'aggiornamento è correlato.
     - PUÒ essere usato per fornire ulteriori dettagli sull'aggiornamento.

   * - Key rotation/update of a Federation Entity Key
     - ``jwks_update``
     - Tempo a cui la key rotation/aggiornamento è correlato.
     - Not used.

   * - Suspension
     - ``suspension``
     - Tempo a cui la sospensione è correlata.
     - PUÒ essere usato per fornire ulteriori dettagli sulla sospensione.

   * - Cancellation
     - ``revocation``
     - Tempo a cui la cancellazione è correlata.
     - PUÒ essere usato per fornire ulteriori dettagli sulla revoca.

Quando è presente un evento ``registration``, gli eventi ``metadata_update`` e ``jwks_update`` NON DEVONO essere forniti contemporaneamente, poiché la registrazione si assume configuri lo stato iniziale dell'Entity, come specificato in [`OID-FED-SUBORDINATE-EVENTS`_].


Entity Updates and Their Effects on Trust Artifacts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Le Entity sono caratterizzate da tre categorie principali di dati registrati.

- *Identity Information*: il nome dell'organizzazione, le informazioni di contatto e le policy organizzative.
- *Technical Configuration*: il materiale crittografico, ossia le chiavi di signature and seal e le chiavi di authentication, e gli endpoint tecnici necessari alle interazioni nell'ecosistema.
- *Authorization Information*: gli entitlements dell'Entity, le Credential provision capabilities, le attribute request capabilities, le Intermediary use permissions, gli intended use, le embedded disclosure policy e la conformità agli schema di certificazione.

L'infrastruttura del Trust Framework DEVE propagare tali modifiche ai Trust Artifacts rilevanti.
Gli effetti specifici dipendono dal ruolo dell'Entity e dai Trust Artifacts che utilizza.

Le procedure che eseguono un aggiornamento, ossia ciò che l'Entity sottomette e quali passi eseguono Registrar, Federation Authority e Certificate Authorities, sono descritte nel processo Entity Update.
Questa sezione fornisce la relazione tra le categorie di dati registrati e i Trust Artifacts che li contengono.

**Registered Data and Associated Trust Artifact**

La tabella di seguito fornisce la relazione tra le categorie di dati registrati e i Trust Artifacts in cui sono contenuti, per ciascun tipo di Entity.

.. _table_entity_data_and_trust_artifacts:
.. list-table:: Entity Data and Trust Artifacts
   :class: longtable
   :widths: 18 26 28 28
   :header-rows: 1

   * - **Entity Type**
     - **Data Category**
     - **EUDIW Trust Artifacts**
     - **National Trust Artifacts**

   * - WRP (all)
     - Identity Information
     - Register, WRPAC, WRPRC, LoTE (only for PID, PuB-EAA and notified non-qualified EAA Provider)
     - Entity Configuration, registration Trust Mark

   * - WRP (all)
     - Technical Configuration (Authentication key)
     - WRPAC
     - Entity Configuration, Subordinate Statement

   * - WRP (all)
     - Authorization Information (Entitlements, Intermediary, Service descriptions, Supervision information)
     - Register, WRPRC, LoTE (only for PID, PuB-EAA and notified non-qualified EAA Provider)
     - Entity Configuration, registration Trust Mark

   * - Credential Issuer or Wallet Provider
     - Technical Configuration (Signature/Seal key)
     - X.509 Sign/Seal Certificate
     - X.509 Sign/Seal Certificate

   * - Credential Issuer or Wallet Provider
     - Technical Configuration (Metadata, Signature/Seal Trust Anchor)
     - LoTE
     - Trust Anchor Entity Configuration

   * - Credential Issuer
     - Authorization Information (RP permissions)
     - EDP in the Credential Issuer metadata
     - n/a

   * - Credential Issuer
     - Authorization Information (Credential provision capabilities)
     - Register, WRPRC
     - Subordinate Statement, registration Trust Mark

   * - Relying Party or Relying Party Intermediary
     - Authorization Information (Attribute request capabilities)
     - Register, WRPRC
     - Subordinate Statement, registration Trust Mark

   * - Wallet Provider
     - Identity Information
     - LoTE
     - Entity Configuration, registration Trust Mark

   * - Wallet Provider
     - Authorization Information (Service status)
     - LoTE
     - Subordinate Statement, registration Trust Mark

.. note::
  L'inclusione di Wallet Provider e Credential Issuer nella LoTE è un'asserzione implicita del loro ruolo e della loro autorizzazione nell'ecosistema.
  In particolare, la loro inclusione è il risultato del completamento con successo delle procedure di registrazione e notifica definite in [`CIR2025/848`_] per la registrazione delle WRP e in [`CIR2024/2980`_] per la notifica di WRP e Wallet Provider.
  Analogamente, la possibilità di recuperare il Subordinate Statement di un'Entity significa che l'Entity fa attualmente parte dell'ecosistema nazionale.

.. note::
  I QEAA sono forniti da Qualified Trust Service Provider.
  La loro identity, technical e authorization information sono disponibili nella EUMS TL dedicata.

  L'identity, technical e authorization information di Registrar, Provider of WRPAC e Provider of WRPRC sono disponibili in LoTE dedicate.


Credential Type Lifecycle
^^^^^^^^^^^^^^^^^^^^^^^^^

Un Credential type è registrato nel Digital Credentials Catalog come voce versionata.
L'unione di ``credential_type`` e ``version`` DEVE essere univoca nel catalogo, come specificato in :ref:`registry:Struttura del Catalogo degli Attestati Elettronici`, quindi diverse versioni dello stesso Credential type esistono nel catalogo come voci separate.

Per questo motivo il lifecycle si applica alla singola voce versionata, ossia alla coppia data da ``credential_type`` e ``version``, e non al Credential type nel suo insieme.
Ciascuna voce versionata ha due stati, ``ACTIVE`` e ``INACTIVE``, la cui semantica è definita in :ref:`registry:Struttura del Catalogo degli Attestati Elettronici`.
In breve, un Credential type può essere emesso da una voce versionata solo mentre quella voce è ``ACTIVE``.

.. note::
  Lo stato della voce versionata è distinto dallo stato delle singole Digital Credentials emesse agli User, definito in :ref:`credential-revocation:Ciclo di Vita degli Attestati Elettronici`.

Nell'IT-Wallet, una voce versionata è ``ACTIVE`` solo finché sono soddisfatte tutte le condizioni seguenti, e torna a ``INACTIVE`` non appena una di esse cessa di valere.

  - Almeno un Credential Issuer è elencato nel campo ``issuers`` della voce, e ciascuno di essi detiene l'entitlement corrispondente al ``legal_type`` del Credential type.
  - L'Authentic Source che fornisce i dati, o il Credential type padre, è registrata e disponibile.
    Per un'Authentic Source integrata tramite PDND, ciò significa che l'e-Service è pubblicato e che l'enrolment del Credential Issuer è stato approvato.
  - Lo schema del Credential type è registrato nello Schema Registry per almeno uno dei formati supportati.

Solo una voce versionata dello stesso Credential type è ``ACTIVE`` in un dato momento.

**Versioning**

Un Credential type non viene mai modificato in place.
Quando la sua definizione cambia, viene registrata e attivata una nuova voce versionata, e la voce della versione precedente viene spostata a ``INACTIVE``.

Le Credential già emesse dalla versione precedente mantengono il proprio stato e non sono revocate dal versioning.
Ove il Credential Issuer necessiti che gli User ottengano la nuova versione, può guidare la ri-emissione tramite lo status ``0x03`` (``UPDATE``) o ``0x0F`` (``ATTRIBUTE_UPDATE``) delle singole Digital Credentials, come descritto in :ref:`credential-revocation:Ciclo di Vita degli Attestati Elettronici`.

La registrazione di un Credential type e il suo versioning sono descritti nei processi di registrazione, e la struttura della voce del catalogo in :ref:`registry:Struttura del Catalogo degli Attestati Elettronici`.

.. note::
  Registrare prima il Credential type, in stato ``INACTIVE`` e senza Credential Issuer, rende disponibile l'identificatore del Credential type prima della registrazione del Credential Issuer, poiché quest'ultimo DEVE dichiarare al momento della registrazione i Credential types che intende emettere, e tale dichiarazione finisce nel Register e nel WRPRC.
  
  Inoltre, portare una voce versionata a ``INACTIVE`` impedisce a qualsiasi Wallet Unit di richiedere una nuova emissione da quella voce.
  Non revoca le Credential già emesse da essa, che mantengono il proprio stato.
  Ove il motivo che ha causato la disattivazione richieda anche la revoca delle Credential già emesse, la revoca è una decisione separata, presa dal Credential Issuer come descritto in :ref:`credential-revocation:Ciclo di Vita degli Attestati Elettronici`.


Claims and Schemas Lifecycle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Come descritto sopra per l'aggiornamento del credential type, i claim e gli schema registrati nei rispettivi registri non vengono rimossi, poiché le Credential già emesse continuano a referenziarli; rimuovere un claim o uno schema renderebbe impossibile interpretare quelle Credential.

Quando un claim o uno schema è deprecato, ne viene registrata una nuova versione, e i Credential types che lo usano passano a una nuova versione come descritto sopra.

Authentic Source Lifecycle and PDND Alignment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Un'Authentic Source non è una WRP e non è una Federation Entity, e il suo trust, la sua autorizzazione e i suoi aspetti operativi sono regolati dal framework PDND, come descritto in :ref:`e-service-pdnd:e-Service PDND`, e l'IT-Wallet fa affidamento su PDND per tutti essi.
Nell'IT-Wallet un'Authentic Source è registrata solo nell'Authentic Source Registry, descritto in :ref:`registry:Registro delle Fonti Autentiche`, affinché i Credential Issuer possano scoprire quali dati sono disponibili e tramite quale e-Service.

Per questo motivo il profilo di specifica IT-Wallet non definisce un lifecycle delle Authentic Sources.
Ciò che questa sezione definisce è l'effetto che il lifecycle PDND produce nell'IT-Wallet, poiché Credential types e Credential Issuer ne dipendono.

Quando un'Authentic Source cessa di fornire, tramite PDND, i dati da cui dipende un Credential type, ad esempio perché l'e-Service non è più pubblicato o perché l'enrolment del Credential Issuer è stato revocato, la condizione per l'attivazione di quel Credential type non è più soddisfatta e il Credential type DEVE essere spostato a ``INACTIVE``.
Il Credential type resta registrato e il suo identificatore rimane valido, affinché il tipo possa essere riattivato quando l'integrazione è ripristinata.

Il processo di allineamento non è automatico e funziona in entrambe le direzioni.

- Da PDND a IT-Wallet, un'Authentic Source che modifica la disponibilità di un e-Service usato da un Credential type DEVE notificare la modifica, affinché lo stato del Credential type possa essere aggiornato.
- Da IT-Wallet a PDND, un Credential Issuer la cui registrazione è sospesa o cancellata DEVE notificare la modifica all'Authentic Source, che può quindi decidere di revocare le autorizzazioni corrispondenti nel framework PDND.

.. warning::
  La sospensione o la cancellazione di una registrazione nell'IT-Wallet non produce alcun effetto all'interno di PDND.
  Fino a quando le autorizzazioni non sono revocate sul lato PDND, un Credential Issuer la cui registrazione non è più valida può ancora ottenere un Voucher e accedere all'e-Service di un'Authentic Source, anche se non può più emettere Credential alle Wallet Unit.
  Nell'IT-Wallet la notifica è pertanto un obbligo del Credential Issuer e dell'Authentic Source.

Events, Registries and Trust Artifacts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

La tabella di seguito riassume, per ciascun evento, quali registri e cataloghi sono impattati e dove sono descritti gli effetti sui Trust Artifacts.
Copre sia la registrazione iniziale sia gli eventi di lifecycle successivi.
La relazione tra un aggiornamento di Entity e i Trust Artifacts che interessa è fornita in :ref:`onboarding-system:Entity Updates and Their Effects on Trust Artifacts`, e i meccanismi tecnici che pubblicano lo stato di un Trust Artifact in :ref:`infrastructure-trust:Revocation Mechanisms`.

.. _table_events_registries_artifacts:
.. list-table:: Events and Impacted Registries
   :class: longtable
   :widths: 22 20 34 24
   :header-rows: 1

   * - **Event**
     - **Decided by**
     - **Impacted registries and catalogs**
     - **Effects on Trust Artifacts**

   * - Registration of an Entity
     - Registrar, Federation Authority
     - Register (new entry). Notification to the Commission for the notified categories.
     - The Entity obtains its Trust Artifacts, see :ref:`table_entity_data_and_trust_artifacts`.

   * - Update of an Entity
     - Registrar, Federation Authority
     - Register (updated entry).
     - Depending on the updated data category, see :ref:`table_entity_data_and_trust_artifacts`.

   * - Key rotation of an Entity
     - Certificate Authority, Provider of WRPAC, Federation Authority
     - No registry is impacted, unless the key is a Trust Anchor key, in which case the LoTE.
     - Revocation and re-issuance of the certificate holding the key, see :ref:`table_entity_data_and_trust_artifacts`.

   * - Suspension of an Entity
     - Registrar
     - Register (registration status no longer valid).
     - Revocation of the affected WRPAC, WRPRC and registration Trust Mark, and update of the Subordinate Statement.

   * - Reactivation of an Entity
     - Registrar
     - Register (registration status valid again).
     - New issuance of the Trust Artifacts revoked at suspension time.

   * - Cancellation of an Entity
     - Registrar
     - Register (entry removed). Update of the LoTE or of the EUMS TL for the notified categories.
     - Revocation of the WRPAC, WRPRC and Sign/Seal Certificates, and removal of the Subordinate Statement and of the registration Trust Mark.

   * - Registration of a Credential type version
     - Supervisory Body, published by the Federation Trust Anchor
     - Digital Credentials Catalog (new versioned entry, ``INACTIVE``). Schema Registry, for the schema of the new version.
     - None.

   * - Activation or deactivation of a Credential type version
     - Supervisory Body, published by the Federation Trust Anchor
     - Digital Credentials Catalog (state of the versioned entry).
     - None.

   * - New version of a Credential type
     - Supervisory Body, published by the Federation Trust Anchor
     - Digital Credentials Catalog (new versioned entry ``ACTIVE``, previous versioned entry ``INACTIVE``). Schema Registry.
     - None.

   * - Registration of a new claim or of a new schema
     - Supervisory Body, published by the Federation Trust Anchor
     - Claims Registry or Schema Registry (new entry). Alignment towards the Catalogue of Attributes or the Catalogue of Schemes.
     - None.

   * - Registration of an Authentic Source
     - Supervisory Body, published by the Federation Trust Anchor
     - Authentic Source Registry (new entry).
     - None.

   * - Change of availability of an Authentic Source
     - Authentic Source, through PDND
     - Authentic Source Registry. Digital Credentials Catalog, for the versioned entries that depend on it.
     - None.

.. note::
  La cancellazione di una registrazione è l'evento, mentre l'uscita completa di un'Entity dall'ecosistema, che copre entrambi i Trust Framework, è il processo Entity Removal descritto negli onboarding processes.
  L'obbligo del Registrar di conservare i record per 10 anni sopravvive alla cancellazione, quindi la rimozione della voce dal Register non è una rimozione dei record di quella registrazione.

.. note::
  Il Register è un insieme di record per WRP, quindi un evento impatta solo il record dell'Entity interessata.
  Il Digital Credentials Catalog, l'Authentic Source Registry, il Claims Registry, lo Schema Registry e la Taxonomy sono invece singoli documenti firmati, quindi ogni scrittura richiede una nuova firma e una nuova pubblicazione dell'intero documento.

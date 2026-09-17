.. include:: ../common/common_definitions.rst
.. Included via onboarding-system.rst at title level '-' (level 1).

Lifecycle Management
--------------------

Dopo l'evento di registrazione, un'Entità può essere aggiornata, sospesa, riattivata o cancellata, e un tipo di Credenziale può diventare emettibile o cessare di esserlo, e queste modifiche si riflettono sui Trust Artifact e sui registri.

Questa sezione descrive gli stati e gli eventi che causano il cambiamento di stato di un'entità o di un tipo di Credenziale.
Mappa inoltre ciascun evento sui registri e sui Trust Artifact impattati dall'evento, si veda :ref:`onboarding-system:Events, Registries and Trust Artifacts`.

I formati, i parametri e gli stati dei Trust Artifact sono definiti in :ref:`infrastructure-trust:Trust Artifacts Lifecycle State Machine`, e i meccanismi di revoca sono definiti in :ref:`infrastructure-trust:Revocation Mechanisms`.
Il ciclo di vita dei singoli Attestati Elettronici emessi agli Utenti è una materia distinta ed è definito in :ref:`credential-revocation:Digital Credential Lifecycle`.

Entity Lifecycle State Machine
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Questa sezione si applica alle WRP e ai WP in quanto direttamente coinvolti nelle fasi operative.
Come mostrato in :numref:`fig_Entity_Lifecycle_States`, un'Entità ha cinque stati distinti e mutuamente esclusivi: ``UNREGISTERED``, ``REGISTERED``, ``OPERATIONAL``, ``SUSPENDED`` e ``CANCELLED``.
Ciascuno stato determina il livello di autorizzazione e le capacità operative dell'Entità.

.. _fig_Entity_Lifecycle_States:
.. plantuml:: plantuml/entity-lifecycle-states.puml
    :width: 70%
    :alt: The figure illustrates the lifecycle states of an Entity and the transitions between them.
    :caption: `Entity Lifecycle States. <https://www.plantuml.com/plantuml/svg/TP91RiCW44Ntd6BMbNA1BgfO3geYMKva9wkq2meJ1na3Od2IthxONSHrwkKmxy-V3wmfYX3xph2BLWZO-VWD2aa6xQDsbb6hhHT1TF0bPDi4rrkLE-C2n20ifHRQEA7e8fIxQTl0MHX2nauldx1QlS6nhFZxjZxmYcyOcrPZUrA-Gi16Kve_R03ITTvWHCLcajsULzbXkokp8cbYw2b22gFFGaO2JTGdpHHwyfbhyEvrGFLXKxo0LzUc0NFN-bZlURaPzTIJHql3FSrz5h37yJ-XqmxwEeP-SispCkT5CO9IM8d6_89ptqNmh_CYnXwTWKklnzPerV13VW00>`_

**Transition from UNREGISTERED to REGISTERED**

- ``UNREGISTERED``: l'Entità non detiene una registrazione valida all'interno dell'ecosistema IT-Wallet.
  Questo è lo stato di base predefinito.
  Le Entità in questo stato sono al di fuori del perimetro di trust e NON DEVONO partecipare ad alcuna operazione.
- ``REGISTERED``: l'Entità ha completato il processo di registrazione e la sua identità è stata verificata.

  - *EUDIW Trust Framework*: le WRP sono nello stato ``REGISTERED`` quando le loro informazioni sono state aggiunte al Register.
    I Fornitori di Wallet diventano ``REGISTERED`` quando i record di certificazione e di onboarding sono stati raccolti e verificati.
  - *National Trust Framework*: le WRP e i Fornitori di Wallet sono nello stato ``REGISTERED`` quando i record di onboarding sono stati raccolti e verificati.

**Transition from REGISTERED to OPERATIONAL**

``OPERATIONAL`` indica che l'Entità è stata autorizzata a eseguire le operazioni relative al proprio ruolo.

- *EUDIW Trust Framework*: le WRP sono ``OPERATIONAL`` se erano ``REGISTERED`` e hanno ottenuto un WRPAC, i corrispondenti WRPRC e, a seconda del ruolo, un Sign/Seal Certificate.
  Il signing Trust Anchor di tale certificato DEVE essere stato aggiunto alla LoTE o alla EUMS TL.
  I Fornitori di Wallet sono ``OPERATIONAL`` se erano ``REGISTERED`` e hanno ottenuto un Sign/Seal Certificate il cui signing Trust Anchor è stato aggiunto alla LoTE.
- *National Trust Framework*: le WRP e i Fornitori di Wallet sono ``OPERATIONAL`` se erano ``REGISTERED``, hanno ottenuto i Sign/Seal Certificate e i Trust Mark di registrazione, e il loro Subordinate Statement è stato pubblicato dalla Federation Authority.

**Transition from OPERATIONAL to REGISTERED**

Un'Entità torna a ``REGISTERED`` quando non detiene più Trust Artifact validi.
Ciò può essere innescato dalla loro scadenza o revoca a seguito di un aggiornamento dell'Entità.
Per tornare a ``OPERATIONAL`` è richiesta una nuova emissione dei Trust Artifact.

**Transition from REGISTERED or OPERATIONAL to SUSPENDED**

``SUSPENDED`` indica che la registrazione non è temporaneamente valida.
A differenza della cancellazione, la sospensione è reversibile.
Una WRP la cui registrazione è sospesa NON DEVE emettere Credenziali alle Wallet Unit né richiedere attributi da esse, e le Credenziali che ha emesso non sono accettate dalle Relying Party, come descritto nella Section 4.6.5 di [`EIDAS-ARF`_].

Gli eventi che conducono a questo stato, e le parti titolate a deciderli, sono elencati in :ref:`onboarding-system:Registration Events and Their Governance`.

**Transition from SUSPENDED to REGISTERED**

La sospensione può essere revocata dalla stessa parte che l'ha decisa.
Poiché i Trust Artifact interessati dalla sospensione sono stati revocati, l'Entità torna a ``REGISTERED`` e non direttamente a ``OPERATIONAL``, ed è richiesta una nuova emissione dei Trust Artifact per tornare ``OPERATIONAL``.

**Transition from REGISTERED, OPERATIONAL or SUSPENDED to CANCELLED**

``CANCELLED`` indica che la registrazione è cessata.
Lo stato è lo stesso sia che la cancellazione sia stata richiesta dall'Entità stessa sia che sia stata decisa dall'autorità competente, e differisce solo l'evento innescante.

- *EUDIW Trust Framework*: per le WRP comporta la revoca del WRPAC, del WRPRC e, ove applicabile, dei Sign/Seal Certificate, la rimozione della voce dal Register e l'aggiornamento dello stato del signing Trust Anchor nella LoTE o nella EUMS TL.
  Per i Fornitori di Wallet comporta l'aggiornamento della Wallet Providers LoTE.
- *National Trust Framework*: sia per le WRP sia per i Fornitori di Wallet comporta la rimozione del Subordinate Statement e del Trust Mark di registrazione, e la revoca dei National X509 Certificates.

Un'Entità DEVE rifiutare nuove interazioni o transazioni avviate da un'Entità ``CANCELLED``, e tutte le chiavi crittografiche, gli attestati attivi e le capacità operative associate all'Entità DEVONO essere revocati.
Le Entità POSSONO tuttavia continuare a validare dati storici, firme e Credenziali generate prima del timestamp di cancellazione, soggette alle policy di rischio locali.
Un'Entità in stato ``CANCELLED`` che vuole partecipare nuovamente all'ecosistema DEVE completare una nuova registrazione.

.. note::
  La Section 4.6.5 di [`EIDAS-ARF`_] descrive per i PID Provider e gli Attestation Provider gli stati **Registered**, **Suspended** e **Cancelled**.
  All'interno di IT-Wallet lo stato **Registered** è suddiviso in ``REGISTERED`` e ``OPERATIONAL``, per distinguere il momento in cui il record di registrazione esiste dal momento in cui l'Entità detiene tutti i Trust Artifact di cui ha bisogno per operare.

.. note::
  Il ciclo di vita delle Fonti Autentiche e delle Entità dell'infrastruttura di trust, quali il Registrar e i Provider of WRPAC e of WRPRC, non è definito in questa sezione.
  Le Fonti Autentiche seguono il framework PDND, e gli effetti che il loro ciclo di vita produce all'interno di IT-Wallet sono descritti in :ref:`onboarding-system:Authentic Source Lifecycle and PDND Alignment`.

Registration Events and Their Governance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Ogni transizione della state machine delle Entità è causata da un evento.
Per ciascun evento, questa sezione indica chi è titolato a innescare, chi ne è responsabile e, quando applicabile, su quale base normativa e entro quali condizioni.
Gli eventi che riguardano i tipi di Credenziale e le Fonti Autentiche sono descritti nelle sezioni dedicate seguenti.

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
     - Richiesta dell'Entità, dopo la verifica delle condizioni di eleggibilità applicabili al proprio ruolo.
     - Registrar, per la voce del Register. Federation Authority, per la registrazione di federazione.
     - Articoli 5 e 6 di [`CIR2025/848`_].
     - Non definito.

   * - Update
     - Modifica delle informazioni registrate. La WRP è responsabile dell'accuratezza delle proprie informazioni e le aggiorna.
     - Registrar, per la voce del Register. Federation Authority, per il Subordinate Statement e il Trust Mark di registrazione.
     - Articolo 5(2) e 5(3) di [`CIR2025/848`_].
     - Senza indebito ritardo.

   * - Suspension
     - Richiesta di un Organismo di Supervisione, richiesta della WRP stessa, o iniziativa del Registrar nei casi elencati dopo questa tabella.
     - Registrar per il Trust Framework EUDIW, Federation Authority per il National Trust Framework.
     - Articolo 9(1), 9(2), 9(3) e 9(5) di [`CIR2025/848`_].
     - Informazione della WRP e dei Provider dei suoi certificati entro 24 ore.

   * - Reactivation
     - Rimozione della condizione che ha causato la sospensione.
     - La stessa parte che ha deciso la sospensione.
     - Section 4.6.5 di [`EIDAS-ARF`_].
     - Non definito.

   * - Cancellation
     - Richiesta di un Organismo di Supervisione, richiesta della WRP stessa compreso quando non intende più fare affidamento sulle Wallet Unit, o iniziativa del Registrar nei casi elencati dopo questa tabella.
     - Registrar per il Trust Framework EUDIW, Federation Authority per il National Trust Framework.
     - Articolo 9(1), 9(2), 9(3) e 9(5) di [`CIR2025/848`_].
     - Informazione della WRP e dei Provider dei suoi certificati entro 24 ore.

Due ruoli eseguono un evento, uno per ciascun Trust Framework.
All'interno del Trust Framework EUDIW il Registrar agisce sul Register e notifica i Provider dei Trust Artifact interessati.
All'interno del National Trust Framework la Federation Authority agisce sul Subordinate Statement e sul Trust Mark di registrazione, e pubblica l'evento sul Federation Subordinate Events Endpoint.
La decisione che innesca l'evento è la stessa per entrambi, ed è descritta di seguito con riferimento al Registrar, in quanto gli obblighi sono posti sul Registrar da [`CIR2025/848`_].

Il Registrar DEVE sospendere o cancellare la registrazione di una WRP ove la sospensione o la cancellazione sia richiesta da un Organismo di Supervisione, e ove sia richiesta dalla stessa WRP.
Il Registrar PUÒ sospendere o cancellare la registrazione di propria iniziativa ove:

  - la registrazione contenga informazioni inesatte, non aggiornate o fuorvianti;
  - la WRP non sia conforme alla policy di registrazione;
  - la WRP stia richiedendo più attributi di quelli che ha registrato;
  - la WRP stia altrimenti agendo in violazione del diritto dell'Unione o nazionale in un modo connesso al proprio ruolo.

Prima di sospendere o cancellare una registrazione di propria iniziativa, il Registrar DEVE condurre una valutazione di proporzionalità, tenendo conto dell'impatto sui diritti fondamentali, sulla privacy, sulla sicurezza e sulla riservatezza degli Utenti dell'ecosistema, della gravità della discontinuità causata dal provvedimento e dei costi associati, sia per la WRP sia per l'Utente.

Il Registrar DEVE informare la WRP e i rilevanti Provider of WRPAC e of WRPRC senza indebito ritardo, e in ogni caso non oltre 24 ore dopo la sospensione o la cancellazione, come stabilito dall'Articolo 9(5) di [`CIR2025/848`_].
L'informazione DEVE includere i motivi della sospensione o della cancellazione e i mezzi di ricorso o di appello disponibili.
Dopo la notifica, i Provider DEVONO revocare i certificati interessati senza indebito ritardo, ove applicabile, come stabilito dall'Articolo 9(6) di [`CIR2025/848`_].

Il Registrar DEVE conservare i record della registrazione, dei dati di emissione e delle modifiche per 10 anni.
All'interno di IT-Wallet la stessa conservazione si applica alla Federation Authority per i record del National Trust Framework, per analogia.

.. note::
  Gli obblighi descritti sopra sono posti dagli Articoli 9 e 10 di [`CIR2025/848`_] e si applicano al Registrar e alla registrazione delle WRP.
  All'interno di IT-Wallet l'obbligo di conservazione è esteso per analogia alla Federation Authority per i record che mantiene per il National Trust Framework, poiché [`CIR2025/848`_] non disciplina il National Trust Framework.
  I Fornitori di Wallet non sono registrati come WRP, quindi la sospensione e la cancellazione di un Fornitore di Wallet conseguono dalla certificazione della propria Soluzione Wallet e dalla notifica, e non dall'Articolo 9.

Oltre all'Organismo di Supervisione, al Registrar e all'Entità stessa, una sospensione o una cancellazione di un'Entità PUÒ inoltre essere richiesta o innescata da altre parti esterne al Sistema di Onboarding, ad esempio un'autorità giudiziaria, un'autorità amministrativa competente per l'Entità, un'autorità competente per la cybersicurezza, un organismo di valutazione della conformità che ritira una certificazione, o lo Stato membro che ritira una notifica.
In ogni caso la sospensione o la cancellazione è eseguita tramite i meccanismi descritti sopra, in cui la Federation Authority che ha registrato l'Entità agisce sul suo Subordinate Statement e sul Trust Mark di registrazione, e i Trust Artifact dell'Entità sono revocati.
Per un'Entità registrata tramite un Federation Intermediate, il Subordinate Statement è servito dall'Intermediate, che lo ritira per sospendere o cancellare l'Entità, mentre il Trust Mark di registrazione resta emesso dal Federation Trust Anchor che è responsabile di qualsiasi effetto sul ciclo di vita del Trust Mark di registrazione.
La sospensione o la cancellazione di un Federation Intermediate DEVE propagarsi alle Entità affiliate, la cui Trust Chain passa attraverso di esso, come descritto in :ref:`trust-evaluation:Federation Trust Chain`.

Indipendentemente dalla notifica descritta sopra, i Provider of WRPAC e i Provider of WRPRC monitorano le modifiche nel Register su base continua, e revocano o riemettono i certificati quando le modifiche lo richiedono.
Per un WRPRC la riemissione è automatica, come definito in :ref:`onboarding-system:Wallet-Relying Party Registration Certificate Issuance`.
Ciò è stabilito dall'Annex IV di [`CIR2025/848`_] per i Provider of WRPAC e dall'Annex V di [`CIR2025/848`_] come modificato da [`CIR2026/1730`_] per i Provider of WRPRC.

All'interno del National Trust Framework gli eventi che modificano la registrazione di un'Entità DEVONO essere pubblicati dalla Federation Authority come eventi firmati sul Federation Subordinate Events Endpoint (``federation_subordinate_events_endpoint``), in modo che gli altri partecipanti possano tracciare il ciclo di vita di un'Entità nel tempo.
L'endpoint e il formato della sua risposta sono descritti in :ref:`infrastructure-trust:Federation API Endpoints`.

Ciascun evento della state machine DEVE essere pubblicato come un oggetto dell'array ``federation_registration_events``, utilizzando i tipi di evento definiti in [`OID-FED-SUBORDINATE-EVENTS`_].
La tabella seguente fornisce, per ciascun evento, il valore del parametro ``event`` e come i parametri dell'oggetto evento sono popolati.

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
     - Orario a cui la registrazione è relativa.
     - Non utilizzato.

   * - Update of Identity Information or Technical Configuration
     - ``metadata_update``
     - Orario a cui l'aggiornamento è relativo.
     - PUÒ essere utilizzato per fornire ulteriori dettagli sull'aggiornamento.

   * - Key rotation/update of a Federation Entity Key
     - ``jwks_update``
     - Orario a cui la rotazione/aggiornamento della chiave è relativo.
     - Non utilizzato.

   * - Suspension
     - ``suspension``
     - Orario a cui la sospensione è relativa.
     - PUÒ essere utilizzato per fornire ulteriori dettagli sulla sospensione.

   * - Cancellation
     - ``revocation``
     - Orario a cui la cancellazione è relativa.
     - PUÒ essere utilizzato per fornire ulteriori dettagli sulla revoca.

Quando è presente un evento ``registration``, gli eventi ``metadata_update`` e ``jwks_update`` NON DEVONO essere forniti contemporaneamente, poiché si assume che la registrazione configuri lo stato iniziale dell'Entità, come specificato in [`OID-FED-SUBORDINATE-EVENTS`_].


Entity Updates and Their Effects on Trust Artifacts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Le Entità sono caratterizzate da tre categorie principali di dati registrati.

- *Identity Information*: il nome dell'organizzazione, le informazioni di contatto e le policy organizzative.
- *Technical Configuration*: il materiale crittografico, ossia le chiavi di firma e sigillo e le chiavi di autenticazione, e gli endpoint tecnici necessari per le interazioni nell'ecosistema.
- *Authorization Information*: gli entitlement dell'Entità, le capacità di fornitura delle Credenziali, le capacità di richiesta degli attributi, i permessi di utilizzo dell'Intermediario, gli intended use, le embedded disclosure policy e la conformità agli schemi di certificazione.

L'infrastruttura del Trust Framework DEVE propagare queste modifiche ai Trust Artifact rilevanti.
Gli effetti specifici dipendono dal ruolo dell'Entità e dai Trust Artifact che utilizza.

Le procedure che eseguono un aggiornamento, ossia ciò che l'Entità presenta e quali passi il Registrar, la Federation Authority e le Certificate Authority eseguono, sono descritte nel processo Entity Update.
Questa sezione fornisce la relazione tra le categorie di dati registrati e i Trust Artifact che li contengono.

**Registered Data and Associated Trust Artifact**

La tabella seguente fornisce la relazione tra le categorie di dati registrati e i Trust Artifact in cui sono contenuti, per ciascun tipo di Entità.

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
     - Register, WRPAC, WRPRC, LoTE (solo per PID, PuB-EAA e non-qualified EAA Provider notificati)
     - Entity Configuration, Trust Mark di registrazione

   * - WRP (all)
     - Technical Configuration (Authentication key)
     - WRPAC
     - Entity Configuration, Subordinate Statement

   * - WRP (all)
     - Authorization Information (Entitlements, Intermediary, Service descriptions, Supervision information)
     - Register, WRPRC, LoTE (solo per PID, PuB-EAA e non-qualified EAA Provider notificati)
     - Entity Configuration, Trust Mark di registrazione

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
     - EDP nei metadata del Credential Issuer
     - n/a

   * - Credential Issuer
     - Authorization Information (Credential provision capabilities)
     - Register, WRPRC
     - Subordinate Statement, Trust Mark di registrazione

   * - Relying Party or Relying Party Intermediary
     - Authorization Information (Attribute request capabilities)
     - Register, WRPRC
     - Subordinate Statement, Trust Mark di registrazione

   * - Wallet Provider
     - Identity Information
     - LoTE
     - Entity Configuration, Trust Mark di registrazione

   * - Wallet Provider
     - Authorization Information (Service status)
     - LoTE
     - Subordinate Statement, Trust Mark di registrazione

.. note::
  L'inclusione dei Fornitori di Wallet e dei Credential Issuer nella LoTE è un'asserzione implicita del loro ruolo e della loro autorizzazione all'interno dell'ecosistema.
  In particolare, la loro inclusione è il risultato del completamento con successo delle procedure di registrazione e notifica come definite in [`CIR2025/848`_] per la registrazione delle WRP e in [`CIR2024/2980`_] per la notifica delle WRP e dei Fornitori di Wallet.
  Analogamente, la possibilità di recuperare il Subordinate Statement di un'Entità significa che l'Entità fa attualmente parte dell'ecosistema nazionale.

.. note::
  Le QEAA sono fornite da Qualified Trust Service Provider.
  Le loro informazioni di identità, tecniche e di autorizzazione sono disponibili nella EUMS TL dedicata.

  Le informazioni di identità, tecniche e di autorizzazione dei Registrar, dei Provider of WRPAC e dei Provider of WRPRC sono disponibili in LoTE dedicate.


Credential Type Lifecycle
^^^^^^^^^^^^^^^^^^^^^^^^^

Un tipo di Credenziale è registrato nel Digital Credentials Catalog come voce versionata.
L'unione di ``credential_type`` e ``version`` DEVE essere univoca nel catalogo, come specificato in :ref:`registry:Digital Credentials Catalog Structure`, quindi versioni diverse dello stesso tipo di Credenziale esistono nel catalogo come voci distinte.

Per questo motivo il ciclo di vita si applica alla singola voce versionata, ossia la coppia data da ``credential_type`` e ``version``, e non al tipo di Credenziale nel suo insieme.
Ciascuna voce versionata ha due stati, ``ACTIVE`` e ``INACTIVE``, la cui semantica è definita in :ref:`registry:Digital Credentials Catalog Structure`.
In sintesi, un tipo di Credenziale può essere emesso da una voce versionata solo finché tale voce è ``ACTIVE``.

.. note::
  Lo stato della voce versionata è una cosa distinta dallo stato dei singoli Attestati Elettronici emessi agli Utenti, che è definito in :ref:`credential-revocation:Digital Credential Lifecycle`.

All'interno di IT-Wallet, una voce versionata è ``ACTIVE`` solo finché tutte le seguenti condizioni sono soddisfatte, e torna a ``INACTIVE`` non appena una di esse cessa di valere.

  - Almeno un Credential Issuer è elencato nel campo ``issuers`` della voce, e ciascuno di essi detiene l'entitlement corrispondente al ``legal_type`` del tipo di Credenziale.
  - La Fonte Autentica che fornisce i dati, o il tipo di Credenziale padre, è registrata e disponibile.
    Per una Fonte Autentica integrata tramite PDND, ciò significa che l'e-Service è pubblicato e che l'enrolment del Credential Issuer è stato approvato.
  - Lo schema del tipo di Credenziale è registrato nello Schema Registry per almeno uno dei formati supportati.

Una sola voce versionata dello stesso tipo di Credenziale è ``ACTIVE`` in un dato momento.

**Versioning**

Un tipo di Credenziale non è mai modificato in place.
Quando la sua definizione cambia, una nuova voce versionata è registrata e attivata, e la voce della versione precedente è portata a ``INACTIVE``.

Le Credenziali già emesse dalla versione precedente conservano il proprio stato e non sono revocate dal versionamento.
Ove il Credential Issuer necessiti che gli Utenti ottengano la nuova versione, può guidare la riemissione tramite lo stato ``0x03`` (``UPDATE``) o ``0x0F`` (``ATTRIBUTE_UPDATE``) dei singoli Attestati Elettronici, come descritto in :ref:`credential-revocation:Digital Credential Lifecycle`.

La registrazione di un tipo di Credenziale e il suo versionamento sono descritti nei processi di registrazione, e la struttura della voce di catalogo in :ref:`registry:Digital Credentials Catalog Structure`.

.. note::
  Registrare prima il tipo di Credenziale, nello stato ``INACTIVE`` e senza Credential Issuer, rende disponibile l'identificativo del tipo di Credenziale prima della registrazione del Credential Issuer, in quanto DEVE dichiarare in sede di registrazione i tipi di Credenziale che intende emettere, e questa dichiarazione finisce nel Register e nel WRPRC.
  
  Inoltre, il passaggio di una voce versionata a ``INACTIVE`` impedisce a qualsiasi Wallet Unit di richiedere una nuova emissione da tale voce.
  Non revoca le Credenziali già emesse da essa, che conservano il proprio stato.
  Ove il motivo che ha causato la disattivazione richieda anche la revoca delle Credenziali già emesse, la revoca è una decisione distinta, assunta dal Credential Issuer come descritto in :ref:`credential-revocation:Digital Credential Lifecycle`.


Claims and Schemas Lifecycle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Come descritto sopra per l'aggiornamento del tipo di Credenziale, i claim e gli schema registrati nei rispettivi registri non sono rimossi, poiché le Credenziali già emesse continuano a referenziarli, quindi rimuovere un claim o uno schema renderebbe tali Credenziali impossibili da interpretare.

Quando un claim o uno schema è deprecato, ne viene registrata una nuova versione, e i tipi di Credenziale che lo utilizzano passano a una nuova versione come descritto sopra.

Authentic Source Lifecycle and PDND Alignment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Una Fonte Autentica non è una WRP e non è un'Entità di Federazione, e la sua trust, la sua autorizzazione e i suoi aspetti operativi sono governati dal framework PDND, come descritto in :ref:`e-service-pdnd:e-Service PDND`, e IT-Wallet si affida a PDND per tutti essi.
All'interno di IT-Wallet una Fonte Autentica è registrata solo nell'Authentic Source Registry, descritto in :ref:`registry:Authentic Source Registry`, in modo che i Credential Issuer possano scoprire quali dati sono disponibili e tramite quale e-Service.

Per questo motivo il profilo implementativo di IT-Wallet non definisce un ciclo di vita delle Fonti Autentiche.
Quanto questa sezione definisce è l'effetto che il ciclo di vita PDND produce all'interno di IT-Wallet, perché i tipi di Credenziale e i Credential Issuer dipendono da esso.

Quando una Fonte Autentica cessa di fornire, tramite PDND, i dati da cui un tipo di Credenziale dipende, ad esempio perché l'e-Service non è più pubblicato o perché l'enrolment del Credential Issuer è stato ritirato, la condizione per l'attivazione di tale tipo di Credenziale non è più soddisfatta e il tipo di Credenziale DEVE essere portato a ``INACTIVE``.
Il tipo di Credenziale resta registrato e il suo identificativo resta valido, in modo che il tipo possa essere riattivato quando l'integrazione è ripristinata.

Il processo di allineamento non è automatico e opera in entrambe le direzioni.

- Da PDND a IT-Wallet, una Fonte Autentica che modifica la disponibilità di un e-Service utilizzato da un tipo di Credenziale DEVE notificare la modifica, in modo che lo stato del tipo di Credenziale possa essere aggiornato.
- Da IT-Wallet a PDND, un Credential Issuer la cui registrazione è sospesa o cancellata DEVE notificare la modifica alla Fonte Autentica, che potrà quindi decidere di ritirare le corrispondenti autorizzazioni all'interno del framework PDND.

.. warning::
  La sospensione o la cancellazione di una registrazione in IT-Wallet non produce alcun effetto all'interno di PDND.
  Finché le autorizzazioni non sono ritirate sul lato PDND, un Credential Issuer la cui registrazione non è più valida può ancora ottenere un Voucher e accedere all'e-Service di una Fonte Autentica, anche se non può più emettere Credenziali alle Wallet Unit.
  All'interno di IT-Wallet la notifica è pertanto un obbligo del Credential Issuer e della Fonte Autentica.

Events, Registries and Trust Artifacts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

La tabella seguente sintetizza, per ciascun evento, quali registri e cataloghi sono impattati e dove sono descritti gli effetti sui Trust Artifact.
Copre sia la registrazione iniziale sia i successivi eventi di ciclo di vita.
La relazione tra un aggiornamento di un'Entità e i Trust Artifact che incide è data in :ref:`onboarding-system:Entity Updates and Their Effects on Trust Artifacts`, e i meccanismi tecnici che pubblicano lo stato di un Trust Artifact in :ref:`infrastructure-trust:Revocation Mechanisms`.

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
     - Register (nuova voce). Notifica alla Commissione per le categorie notificate.
     - L'Entità ottiene i propri Trust Artifact, si veda :ref:`table_entity_data_and_trust_artifacts`.

   * - Update of an Entity
     - Registrar, Federation Authority
     - Register (voce aggiornata).
     - A seconda della categoria di dati aggiornata, si veda :ref:`table_entity_data_and_trust_artifacts`.

   * - Key rotation of an Entity
     - Certificate Authority, Provider of WRPAC, Federation Authority
     - Nessun registro è impattato, a meno che la chiave sia una chiave di Trust Anchor, nel qual caso la LoTE.
     - Revoca e riemissione del certificato che detiene la chiave, si veda :ref:`table_entity_data_and_trust_artifacts`.

   * - Suspension of an Entity
     - Registrar, Federation Authority
     - Register (stato di registrazione non più valido). Aggiornamento della LoTE o della EUMS TL per le categorie notificate.
     - Revoca dei WRPAC, WRPRC e Trust Mark di registrazione interessati, e aggiornamento del Subordinate Statement.

   * - Reactivation of an Entity
     - Registrar, Federation Authority
     - Register (stato di registrazione nuovamente valido). Aggiornamento della LoTE o della EUMS TL per le categorie notificate.
     - Nuova emissione dei Trust Artifact revocati al momento della sospensione.

   * - Cancellation of an Entity
     - Registrar, Federation Authority
     - Register (voce rimossa). Aggiornamento della LoTE o della EUMS TL per le categorie notificate.
     - Revoca dei WRPAC, WRPRC e Sign/Seal Certificate, e rimozione del Subordinate Statement e del Trust Mark di registrazione.

   * - Registration of a Credential type version
     - Organismo di Supervisione, pubblicato dal Federation Trust Anchor
     - Digital Credentials Catalog (nuova voce versionata, ``INACTIVE``). Schema Registry, per lo schema della nuova versione.
     - Nessuno.

   * - Activation or deactivation of a Credential type version
     - Organismo di Supervisione, pubblicato dal Federation Trust Anchor
     - Digital Credentials Catalog (stato della voce versionata).
     - Nessuno.

   * - New version of a Credential type
     - Organismo di Supervisione, pubblicato dal Federation Trust Anchor
     - Digital Credentials Catalog (nuova voce versionata ``ACTIVE``, voce versionata precedente ``INACTIVE``). Schema Registry.
     - Nessuno.

   * - Registration of a new claim or of a new schema
     - Organismo di Supervisione, pubblicato dal Federation Trust Anchor
     - Claims Registry o Schema Registry (nuova voce). Allineamento verso il Catalogue of Attributes o il Catalogue of Schemes.
     - Nessuno.

   * - Registration of an Authentic Source
     - Organismo di Supervisione, pubblicato dal Federation Trust Anchor
     - Authentic Source Registry (nuova voce).
     - Nessuno.

   * - Change of availability of an Authentic Source
     - Fonte Autentica, tramite PDND
     - Authentic Source Registry. Digital Credentials Catalog, per le voci versionate che dipendono da essa.
     - Nessuno.

.. note::
  La cancellazione di una registrazione è l'evento, mentre l'uscita completa di un'Entità dall'ecosistema, che copre entrambi i Trust Framework, è il processo Entity Removal descritto nei processi di onboarding.
  L'obbligo del Registrar di conservare i record per 10 anni sopravvive alla cancellazione, quindi la rimozione della voce dal Register non è una rimozione dei record di tale registrazione.

.. note::
  Il Register è un insieme di record per WRP, quindi un evento impatta solo il record dell'Entità interessata.
  Il Digital Credentials Catalog, l'Authentic Source Registry, il Claims Registry, lo Schema Registry e la Taxonomy sono invece singoli documenti firmati, quindi ogni scrittura richiede una nuova firma e una nuova pubblicazione dell'intero documento.

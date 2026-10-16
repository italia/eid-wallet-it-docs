.. include:: ../common/common_definitions.rst
.. Included via onboarding-system.rst at title level '^' (level 2, under Onboarding Processes).

Entity Onboarding
^^^^^^^^^^^^^^^^^

Questa sezione descrive i processi che gestiscono il ciclo di vita delle entità e delle Fonti Autentiche.
Ciascun processo è descritto con il proprio Input, il proprio Outcome e il proprio Process, mentre la governance dei corrispondenti eventi, ossia chi è titolato a decidere e entro quali condizioni, è data in :ref:`onboarding-system:Registration Events and Their Governance`.

Entity Registration
"""""""""""""""""""

Il processo Entity Registration prende in input i dati di registrazione di un'Entità, li verifica, li registra e registra l'Entità nel National Trust Framework e, ove il suo ruolo e la sua dichiarazione lo richiedano, nel EUDIW Register.
Il processo è parametrizzato dal profilo di registrazione del ruolo, e il suo esito è la transizione dell'Entità allo stato ``REGISTERED``.
Abilita i processi di :ref:`onboarding-system:Certificate and Trust Artifact Issuance`, che portano l'Entità a ``OPERATIONAL``, e, per un Credential Issuer, il :ref:`onboarding-system:Credential Type Registration`.
L'emissione dei certificati e del Trust Mark di registrazione, e la governance degli stati, sono descritte nei processi referenziati e in :ref:`onboarding-system:Lifecycle Management`.

**Input**

L'input è costituito dai dati di registrazione dell'Entità, secondo il profilo del suo ruolo definito in :ref:`onboarding-system:Registration Data Model` e in :ref:`onboarding-system:Registration Profiles`.
I dati sono organizzati nelle tre categorie di dati registrati definite in :ref:`onboarding-system:Lifecycle Management`, e per ciascuna categoria una parte è fornita dall'Entità e una parte è derivata dal Sistema di Onboarding.

- *Identity Information*, fornita dall'Entità: 

   - ``legal_name``,
   - ``identifier``, 
   - ``legal_nature``, 
   - ``contact_information``, 
   - ``service_policies``,
   - ``data_protection_authority``.
   
- *Technical Configuration*, fornita dall'Entità, in particolare il ``federation_entity_identifier`` e la ``federation_entity_key`` della propria Entity Configuration.
- *Authorization Information*, fornita dall'Entità, ossia:

   - ``entitlements``,
   - ``relying_party_services``,
   - ``intended_use``,
   - ``provided_attestations`` per un Credential Issuer,
   - ``intermediary_relationship`` ove applicabile,
   - ``conformity_assessment`` per le categorie che ne hanno bisogno.

Il record firmato, i certificati e i loro Trust Anchor non sono un input ma sono derivati dalla registrazione.
In particolare, le ``certificate_signing_requests`` non sono un input diretto di questo processo ma dei processi di :ref:`onboarding-system:Certificate and Trust Artifact Issuance`.
Per un PID Provider e un Fornitore di Wallet il ``signing_trust_anchor`` deriva dall'emissione nazionale, e per un QEAA Provider e un PuB-EAA Provider è fornito all'interno delle eIDAS Trusted Lists, quindi non è fornito come input dall'Entità.

L'eleggibilità e la conformità dell'Entità sono una precondizione e non una parte di questo processo, e sono descritte in :ref:`onboarding-system:Eligibility and Compliance Preconditions`.

**Outcome**

L'esito è l'Entità nello stato ``REGISTERED``, ossia il momento in cui il record di registrazione esiste ed è stato verificato, come definito in :ref:`onboarding-system:Lifecycle Management`.
La registrazione è registrata nei due Trust Framework secondo il ruolo e la dichiarazione dell'Entità.

- Nel National Trust Framework l'Entità è registrata nella federazione, e il suo Subordinate Statement, che reca il Trust Mark di registrazione, è pubblicato dal National Federation Management.
- Nel Trust Framework EUDIW, per le Wallet-Relying Party, un record firmato è scritto nel Register, e guida la successiva emissione del WRPAC e l'emissione automatizzata del WRPRC.

Il National Trust Framework è sempre lo strato di registrazione, mentre il Trust Framework EUDIW è aggiunto per le categorie notificate e per le Entità che dichiarano l'operatività transfrontaliera, come descritto in :ref:`infrastructure-trust:Overview`.
Il Register e il dataset di notifica sono mantenuti distinti, come descritto in :ref:`onboarding-system:Trust Artifacts Registration Outcomes`.

**Process**

1. L'eleggibilità e la conformità dell'Entità DEVONO essere state verificate, compreso l'identity proofing e la verifica degli entitlement, come descritto in :ref:`onboarding-system:Eligibility and Compliance Preconditions`.
   Questa verifica è la precondizione della registrazione.
2. Il Sistema di Onboarding raccoglie i dati di registrazione del profilo, li valida e instrada ciascuna parte al componente responsabile di essa.
3. Il National Federation Management registra l'Entità nella federazione.
   Valida l'Entity Configuration pubblicata dall'Entità, data dal ``federation_entity_identifier`` e dalla ``federation_entity_key``, e prepara la metadata policy che vincola i metadata di protocollo dell'Entità ai valori approvati in sede di onboarding.
   Invoca quindi :ref:`onboarding-system:Registration Trust Mark Issuance` per ottenere il Trust Mark di registrazione, e pubblica il Subordinate Statement sull'Entità, che reca la metadata policy e il Trust Mark.
   Quindi, l'Entità DEVE includere il Trust Mark ricevuto nella propria Entity Configuration, che punta al proprio superiore immediato tramite gli ``authority_hints``.
   Durante la stessa registrazione le chiavi pubbliche del Federation Trust Anchor sono rese disponibili all'Entità fuori banda, tramite il canale di contatto della registrazione, e questo avvia la trust dell'Entità nel Trust Anchor, si veda :ref:`trust-evaluation:Federation Trust Anchor Distribution and Validation`.
   La struttura dell'Entity Configuration e del Subordinate Statement è definita in :ref:`infrastructure-trust:National Trust Artifacts`.
4. Ove il ruolo e la dichiarazione dell'Entità richiedano il Trust Framework EUDIW, l'EUDIW Registration Management verifica l'Entità e scrive il suo record nel Register, e il Registrar lo firma o lo sigilla.
   Il record guida la successiva emissione del WRPAC e l'emissione automatizzata del WRPRC, e il suo data model e la sua API pubblica sono definiti in :ref:`infrastructure-trust:Register of WRPs`.
   Per un Credential Issuer, i ``provided_attestations`` dichiarati in sede di registrazione aggiungono il Credential Issuer al campo ``issuers`` della voce versionata di ciascun tipo di Credenziale dichiarato, come descritto in :ref:`onboarding-system:Credential Type Registration`, e la stessa dichiarazione è recata nel record e nel WRPRC.
5. Ove l'Entità appartenga a una categoria soggetta a notifica, il Notification Dataset Management raccoglie le sue informazioni notificabili nel dataset di notifica, come descritto in :ref:`onboarding-system:Notification and Publication`.
6. La registrazione produce l'evento ``registration``, che la Federation Authority pubblica sul Federation Subordinate Events Endpoint come descritto in :ref:`onboarding-system:Registration Events and Their Governance`.
   Al termine del processo l'Entità è ``REGISTERED``, il record abilita i processi di :ref:`onboarding-system:Certificate and Trust Artifact Issuance` che la portano a ``OPERATIONAL``, e, per un Credential Issuer, la dichiarazione può attivare i tipi di Credenziale dichiarati, come descritto in :ref:`onboarding-system:Credential Type Activation and Deactivation`.

.. note::
   Il Register è il registro nazionale delle Wallet-Relying Party che ciascuno Stato membro istituisce ai sensi dell'Articolo 3 di [`CIR2025/848`_] e opera tramite il Registrar.
   È distinto dai componenti semantici della Registry Infrastructure, che detengono la semantica delle Credenziali e i dati di discovery, ed è documentato come :ref:`infrastructure-trust:Register of WRPs`.

Entity Update
"""""""""""""

Il processo Entity Update modifica le informazioni registrate di un'Entità, nella sua Identity Information, nella sua Technical Configuration, compresa la rotazione e la richiesta di chiavi, e nella sua Authorization Information.
L'Entità è responsabile dell'accuratezza delle proprie informazioni e le aggiorna senza indebito ritardo.
Questo processo descrive ciò che l'Entità presenta e quali passi i componenti eseguono, mentre la relazione tra le categorie di dati registrati e i Trust Artifact è data in :ref:`onboarding-system:Entity Updates and Their Effects on Trust Artifacts`.

**Input**

I dati di registrazione aggiornati definiti in :ref:`onboarding-system:Registration Data Model`.
Per una modifica dell'Identity Information l'input è il nuovo ``legal_name``, ``identifier``, ``legal_nature``, ``contact_information``, ``service_policies`` o ``data_protection_authority``.
Per una modifica della Technical Configuration relativa al nuovo materiale crittografico, la ``federation_entity_key`` e le ``certificate_signing_requests`` sono fornite rispettivamente per l'identità di federazione e per i certificati X.509.
Per una modifica dell'Authorization Information l'input è il nuovo ``entitlements``, ``relying_party_services``, ``intended_use``, ``provided_attestations`` o ``intermediary_relationship``, a seconda del ruolo.

**Outcome**

Le informazioni registrate aggiornate dell'Entità.
Una modifica che incide sull'Authorization Information attiva la ri-verifica dell'eleggibilità, perché un nuovo entitlement non è auto-dichiarato, come descritto in :ref:`onboarding-system:Eligibility and Compliance Preconditions`.

**Process**

1. L'Entità presenta la modifica di una o più categorie dei propri dati di registrazione.
2. Per una modifica dell'Identity Information o dell'Authorization Information, l'EUDIW Registration Management aggiorna il record nel Register, il National Federation Management aggiorna il Subordinate Statement e il Trust Mark di registrazione, e l'Entità richiede la riemissione dei certificati X.509 che recano i dati modificati, come descritto in :ref:`onboarding-system:Certificate and Trust Artifact Issuance`. Il Provider of WRPRC revoca i WRPRC interessati e DEVE riemetterli automaticamente ove la registrazione resti valida. Ove l'Entità appartenga a una categoria notificata, il Notification Dataset Management aggiorna la notifica, come descritto in :ref:`onboarding-system:Notification and Publication`.
3. Per una modifica della ``federation_entity_key``, la rotazione della chiave è gestita dal National Federation Management, che riemette il Subordinate Statement attestante la nuova chiave, così che la nuova chiave diventa fidata solo quando il superiore la attesta, seguendo :ref:`infrastructure-trust:Federation Entity Key Rotation`. La rotazione delle chiavi dei certificati X.509 è una riemissione gestita dai processi di :ref:`onboarding-system:Certificate and Trust Artifact Issuance`, in cui l'Entità fornisce le nuove ``certificate_signing_requests`` nell'ordine ACME.
4. Una modifica dell'Authorization Information è soggetta alla ri-verifica dell'eleggibilità da parte dell'Organismo di Supervisione e, per un Credential Issuer, una modifica delle capacità di fornitura delle Credenziali lo aggiunge o lo rimuove dal campo ``issuers`` della voce versionata di un tipo di Credenziale, come descritto in :ref:`onboarding-system:Credential Type Registration`.
5. L'aggiornamento produce l'evento corrispondente, un ``metadata_update`` per una modifica dell'Identity Information o della Technical Configuration e un ``jwks_update`` per una rotazione di chiavi, pubblicato sul Federation Subordinate Events Endpoint come descritto in :ref:`onboarding-system:Registration Events and Their Governance`.

.. note::
   I parametri informativi dei metadata ``federation_entity``, con l'eccezione dell'``organization_name``, non sono inclusi nella ``metadata_policy`` e possono essere gestiti autonomamente dall'Entità nella propria Entity Configuration auto-firmata.
   Le chiavi di firma di protocollo (``jwks``), gli endpoint di servizio e gli URI di request, response e redirect sono invece vincolati dalla ``metadata_policy`` del Subordinate Statement ai valori approvati in sede di onboarding, come definito in :ref:`infrastructure-trust:National Trust Artifacts`, quindi una loro modifica è un Entity Update che riemette il Subordinate Statement.

.. note::
   Una modifica degli attributi di identità registrati di un'Entità è un Entity Update, compresa una modifica del suo ``legal_name``, della sua ``legal_nature`` o del suo ``identifier``, ove la persona giuridica resti la stessa.
   Ove la persona giuridica stessa cambi, come in una fusione o in una scissione, la registrazione dell'Entità precedente DEVE essere cancellata e la nuova persona giuridica DEVE essere registrata come una nuova Entità, perché l'identity proofing è vincolato alla persona giuridica.

.. note::
   La rotazione di una chiave di protocollo, quella fornita all'interno dei metadata di protocollo, è effettuata tramite l'aggiornamento della ``metadata_policy`` e DEVE seguire la prassi comune: la nuova chiave è aggiunta ai ``jwks`` fissati e coesiste con quella precedente fino a quando le Trust Chain costruite prima della rotazione sono scadute, e solo allora la chiave precedente è rimossa.
   La coesistenza copre la finestra di validità di tali Trust Chain, in modo che un verificatore che fa ancora affidamento su una Trust Chain con la vecchia chiave possa validare fino a quando non la ricostruisce.

Entity Suspension and Removal
"""""""""""""""""""""""""""""

Il processo Entity Suspension and Removal sospende, riattiva o cancella la registrazione di un'Entità, su richiesta di un Organismo di Supervisione, dell'Entità stessa o di un'altra parte esterna titolata a ciò come descritto in :ref:`onboarding-system:Registration Events and Their Governance`, nei due Trust Framework.
Questo processo descrive i passi che i componenti eseguono, mentre chi è titolato a innescare ciascun evento, su quale base normativa e entro quali condizioni, è dato in :ref:`onboarding-system:Registration Events and Their Governance`.

**Input**

La richiesta di sospensione, riattivazione o cancellazione, dall'autorità competente o dall'Entità, con il relativo motivo.

**Outcome**

L'Entità ha cambiato lo stato in ``SUSPENDED`` in caso di sospensione, torna al proprio stato precedente in caso di riattivazione e passa a ``CANCELLED`` in caso di cancellazione, come descritto in :ref:`onboarding-system:Lifecycle Management`.
Una sospensione e una cancellazione revocano i Trust Artifact dell'Entità e, per un Credential Issuer, disattivano i suoi tipi di Credenziale.

**Process**

1. La richiesta di sospensione, riattivazione o cancellazione è ricevuta dall'autorità competente o dall'Entità.
2. In caso di sospensione, l'EUDIW Registration Management sospende il record nel Register ove l'Entità sia una Wallet-Relying Party, il National Federation Management ritira il Subordinate Statement valido dell'Entità, così che i suoi Trust Artifact non siano più oggetto di affidamento, e l'Entità passa a ``SUSPENDED``.
3. In caso di riattivazione, una volta rimossa la condizione che ha causato la sospensione, la stessa parte che ha deciso la sospensione ripristina la registrazione, e l'Entità torna a ``REGISTERED``.
4. In caso di cancellazione, l'EUDIW Registration Management cancella il record nel Register ove l'Entità sia una Wallet-Relying Party, il National Federation Management ritira il Subordinate Statement, i Trust Artifact dell'Entità sono revocati, e l'Entità passa a ``CANCELLED``.
5. Per un Credential Issuer, una sospensione o una cancellazione disattiva i suoi tipi di Credenziale, e il Credential Issuer notifica le Fonti Autentiche in modo che possano ritirare le corrispondenti autorizzazioni all'interno di PDND, come descritto in :ref:`onboarding-system:Authentic Source Lifecycle and PDND Alignment`.
6. Dopo una sospensione, una riattivazione o una cancellazione, ove l'Entità appartenga a una categoria notificata, il Notification Dataset Management aggiorna la notifica, in modo che lo stato dell'Entità nella corrispondente List of Trusted Entities sia aggiornato di conseguenza, come descritto in :ref:`onboarding-system:Notification and Publication`.
7. Ciascun evento, una ``suspension`` o una ``revocation``, è pubblicato sul Federation Subordinate Events Endpoint come descritto in :ref:`onboarding-system:Registration Events and Their Governance`.

Authentic Source Registration
"""""""""""""""""""""""""""""

Il processo Authentic Source Registration scrive le informazioni della Fonte Autentica nell'AS Registry in modo che i Credential Issuer possano scoprire quali dati sono disponibili e tramite quale e-Service.
Una Fonte Autentica non è né una Wallet-Relying Party né un'Entità di Federazione, quindi non passa attraverso la registrazione di federazione né la registrazione di Wallet-Relying Party, e non ottiene alcun Trust Artifact.
La sua trust, la sua autorizzazione e i suoi aspetti operativi sono governati dal framework PDND, si veda :ref:`e-service-pdnd:e-Service PDND`, e IT-Wallet non definisce un ciclo di vita delle Fonti Autentiche, quindi questo processo non produce una transizione di stato.
Abilita il :ref:`onboarding-system:Credential Type Registration`, come fonte dati che un tipo di Credenziale referenzia, e può attivare il :ref:`onboarding-system:Claim Registration` quando un claim dichiarato non è ancora nel Claims Registry.

**Input**

L'input è costituito dai dati di registrazione della Fonte Autentica, secondo il suo profilo in :ref:`onboarding-system:Registration Data Model` e in :ref:`onboarding-system:Registration Profiles`, ossia i dati di registrazione di base e, in aggiunta, i ``provided_claims_purposes`` e la ``visual_identity``.
La Fonte Autentica seleziona dal :ref:`registry:Claims Registry` gli identificativi di claim standardizzati che fornisce, e dalla Taxonomy gli scopi che serve.
Una Fonte Autentica non fornisce i dati di federazione né le ``certificate_signing_requests``, e non ha ``entitlements``.
Da questi dati l'Authentic Source Management compone la voce della Fonte Autentica nell'AS Registry, la cui struttura è definita in :ref:`registry:Authentic Source Registry`, e genera i campi a livello di registro, ossia l'identificativo del registro, la sua versione, l'ora dell'ultima modifica e la sua configurazione di localizzazione.
L'eleggibilità della Fonte Autentica, che valida la sua posizione legale e la sua autorità sui dati e la classifica come pubblica o privata, è una precondizione ed è descritta in :ref:`onboarding-system:Eligibility and Compliance Preconditions`.

**Outcome**

Una voce nell'AS Registry, che rende la Fonte Autentica scopribile dai Credential Issuer, con le sue informazioni organizzative, le sue capacità dati dichiarate, il suo metodo di integrazione e i suoi scopi previsti.
La registrazione della Fonte Autentica è completa e indipendente dall'integrazione di qualsiasi Credential Issuer, perché una Fonte Autentica dichiara le proprie capacità prima che esista qualsiasi tipo di Credenziale.
Il processo non produce uno stato in IT-Wallet, perché la trust, l'autorizzazione e gli aspetti operativi della Fonte Autentica restano all'interno del framework PDND, e gli effetti che il ciclo di vita PDND produce all'interno di IT-Wallet sono descritti in :ref:`onboarding-system:Authentic Source Lifecycle and PDND Alignment`.

**Process**

1. L'eleggibilità e la conformità della Fonte Autentica DEVONO essere state verificate dall'Organismo di Supervisione, che valida la sua posizione legale e la sua autorità sui dati e la classifica come pubblica o privata, come descritto in :ref:`onboarding-system:Eligibility and Compliance Preconditions`.
   Questa verifica è la precondizione della registrazione.
2. La Fonte Autentica dichiara i propri dati di registrazione.
3. I claim dichiarati sono verificati rispetto al :ref:`registry:Claims Registry` e gli scopi dichiarati rispetto alla Taxonomy.
   Un claim che non è ancora nel Claims Registry attiva il :ref:`onboarding-system:Claim Registration`.
4. L'Authentic Source Management scrive la voce nell'AS Registry, la cui struttura è definita in :ref:`registry:Authentic Source Registry`.
   La Fonte Autentica diventa scopribile dai Credential Issuer.

La voce abilita il :ref:`onboarding-system:Credential Type Registration`, in quanto la Fonte Autentica è la fonte dati che un tipo di Credenziale referenzia.

.. note::
   L'integrazione tra una Fonte Autentica e un Credential Issuer avviene all'interno di PDND ed è una precondizione per l'attivazione di un tipo di Credenziale, non un processo del Sistema di Onboarding.
   Il suo effetto sul ciclo di vita del tipo di Credenziale è descritto in :ref:`onboarding-system:Authentic Source Lifecycle and PDND Alignment`.

Authentic Source Update
"""""""""""""""""""""""

L'Authentic Source Update modifica la voce di una Fonte Autentica nell'AS Registry, con effetto sulle voci versionate dei tipi di Credenziale che dipendono da essa.
Una Fonte Autentica non ha un ciclo di vita in IT-Wallet, quindi l'effetto che una modifica produce sui tipi di Credenziale è quello descritto in :ref:`onboarding-system:Authentic Source Lifecycle and PDND Alignment`.

**Input**

I dati di registrazione modificati della Fonte Autentica, ossia una modifica dei suoi ``provided_claims_purposes`` o della sua ``visual_identity``, secondo il suo profilo in :ref:`onboarding-system:Registration Data Model`.

**Outcome**

La voce della Fonte Autentica nell'AS Registry è aggiornata.
Quando la modifica riduce la disponibilità dei dati da cui un tipo di Credenziale dipende, la condizione per l'attivazione di tale tipo di Credenziale non è più soddisfatta e il tipo di Credenziale passa a ``INACTIVE``, come descritto in :ref:`onboarding-system:Authentic Source Lifecycle and PDND Alignment`.

**Process**

1. La Fonte Autentica, o la notifica tramite PDND della modifica di un e-Service, presenta la modifica della voce.
2. L'Authentic Source Management aggiorna la voce nell'AS Registry, la cui struttura è definita in :ref:`registry:Authentic Source Registry`.
3. I tipi di Credenziale che dipendono dalla Fonte Autentica sono aggiornati, e un tipo di Credenziale che perde la disponibilità dei dati da cui dipende passa a ``INACTIVE``, come descritto in :ref:`onboarding-system:Authentic Source Lifecycle and PDND Alignment`.

Authentic Source Removal
""""""""""""""""""""""""

Il processo Authentic Source Removal rimuove la voce di una Fonte Autentica dall'AS Registry, con la disattivazione delle voci versionate dei tipi di Credenziale che dipendono da essa.

**Input**

La richiesta di rimozione della Fonte Autentica.

**Outcome**

La voce della Fonte Autentica è rimossa dall'AS Registry.
I tipi di Credenziale che perdono la Fonte Autentica come propria fonte dati passano a ``INACTIVE``, e restano registrati in modo da poter essere riattivati se la fonte dati è ripristinata, come descritto in :ref:`onboarding-system:Authentic Source Lifecycle and PDND Alignment`.

**Process**

1. La richiesta di rimozione della Fonte Autentica è ricevuta.
2. L'Authentic Source Management rimuove la voce dall'AS Registry.
3. I tipi di Credenziale che dipendono dalla Fonte Autentica perdono la propria fonte dati e passano a ``INACTIVE``, e restano registrati e possono essere riattivati se l'integrazione è ripristinata, come descritto in :ref:`onboarding-system:Authentic Source Lifecycle and PDND Alignment`.

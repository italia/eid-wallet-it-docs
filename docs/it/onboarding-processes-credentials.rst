.. include:: ../common/common_definitions.rst
.. Included via onboarding-system.rst at title level '^' (level 2, under Onboarding Processes).

Attestation Onboarding
^^^^^^^^^^^^^^^^^^^^^^

Questa sezione descrive i processi che gestiscono i claim, gli schema e i tipi di Credenziale.
Ciascun processo è descritto con il proprio Input, il proprio Outcome e il proprio Process.

Claim Registration
""""""""""""""""""

Il Claim Registration aggiunge una definizione di claim standardizzata al Claims Registry, quando un claim di cui una Fonte Autentica o un tipo di Credenziale ha bisogno non è ancora disponibile.
Il Claims Registry è mantenuto dall'Organismo di Supervisione e fornisce definizioni semantiche degli attributi delle Credenziali, quali il loro tipo di dato, le loro regole di validazione e i loro mapping di interoperabilità.
Le definizioni dei claim sono allineate al :ref:`Catalogue of Attributes <registry:Registry Integration and Cross-References>`.
Questo processo abilita lo :ref:`onboarding-system:Schema Provisioning` e il :ref:`onboarding-system:Credential Type Registration` che utilizzano il claim.

**Input**

L'input è la definizione del claim da registrare, secondo i Claim Entry Parameters del :ref:`registry:Claims Registry`: il nome canonico del claim, la sua descrizione, il suo ``type`` (``string``, ``boolean``, ``array`` o ``object``), il ``format`` e l'``encoding`` utilizzati quando una stringa reca un valore qualificato, gli ``aliases`` che mappano i nomi alternativi utilizzati in altri standard sul claim canonico, e la struttura nidificata di un claim ``object`` o ``array``.
Il nome canonico e gli alias sono allineati al :ref:`Catalogue of Attributes <registry:Registry Integration and Cross-References>`.
Un claim è una definizione semantica e non un'Entità, quindi l'input non è costituito da dati di registrazione e non segue un profilo del :ref:`onboarding-system:Registration Data Model`.
I campi a livello di registro, ossia l'identificativo del registro, la sua versione, l'ora dell'ultima modifica e la sua configurazione di localizzazione, sono generati dal Claims and Schema Management.

**Outcome**

L'esito è la definizione del claim nel Claims Registry, che le Fonti Autentiche, gli schema e i tipi di Credenziale possono referenziare.
Un claim non è mai rimosso dal Claims Registry, perché le Credenziali già emesse continuano a referenziarlo, quindi un claim deprecato è sostituito da una nuova versione, come descritto in :ref:`onboarding-system:Claims and Schemas Lifecycle`.

**Process**

1. Un Attestation Scheme Provider, durante un :ref:`onboarding-system:Credential Type Registration`, o una Fonte Autentica che agisce come Attestation Scheme Provider, durante la propria :ref:`onboarding-system:Authentic Source Registration`, richiedono un nuovo claim non ancora presente nel Claims Registry.
2. La definizione del claim è stabilita con il suo nome canonico, il suo ``type``, il suo ``format``, i suoi ``aliases`` e la sua struttura nidificata, allineata al :ref:`Catalogue of Attributes <registry:Registry Integration and Cross-References>` e senza conflitti con i claim già registrati.
3. Il Claims and Schema Management registra la definizione nel Claims Registry.
4. Il claim diventa disponibile e abilita lo :ref:`onboarding-system:Schema Provisioning` e il :ref:`onboarding-system:Credential Type Registration` che lo utilizzano.

Schema Provisioning
"""""""""""""""""""

Lo Schema Provisioning rende disponibile lo schema di un tipo di Credenziale nello Schema Registry, sia generandolo dal data model per le Credenziali definite a livello nazionale, sia registrandolo in allineamento con un Rulebook o uno standard esterno.
Lo schema è uno dei requisiti per l'attivazione di un tipo di Credenziale, quindi questo processo è una precondizione di :ref:`onboarding-system:Credential Type Activation and Deactivation`.

**Input**

Lo schema del tipo di Credenziale segue i Schema Definition Parameters di :ref:`registry:Schema Registry`: il suo ``credential_type`` e ``version``, il ``format`` a cui si applica, uno JSON Schema per il formato SD-JWT VC o uno CBOR Schema per il formato mdoc-CBOR, e lo ``schema_uri`` con il suo digest di integrità.
Lo schema è fornito dall'Attestation Scheme Provider insieme alla definizione del tipo di Credenziale, ed è composto dai claim definiti in :ref:`registry:Claims Registry`. Un claim ancora mancante attiva il :ref:`onboarding-system:Claim Registration`.

**Outcome**

L'esito è lo schema nello Schema Registry, per almeno uno dei formati supportati, che il tipo di Credenziale referenzia.
Ciò soddisfa il requisito di schema dell'attivazione del tipo di Credenziale, come descritto in :ref:`onboarding-system:Credential Type Activation and Deactivation`.

**Process**

1. I claim che compongono lo schema sono disponibili nel Claims Registry, altrimenti il Claim Registration è attivato per il claim mancante.
2. Lo schema è generato dal data model per una Credenziale definita a livello nazionale, oppure è registrato in allineamento con il Rulebook esterno.
3. Il Claims and Schema Management registra lo schema nello Schema Registry, con il suo digest di integrità, per ciascun formato supportato.

Credential Type Registration
""""""""""""""""""""""""""""

Il processo Credential Type Registration crea una voce versionata di un tipo di Credenziale nel Digital Credentials Catalog, nello stato ``INACTIVE``, con la propria fonte dati e il riferimento al Rulebook applicabile.
La voce versionata è la coppia data dal ``credential_type`` e dalla ``version``, che DEVE essere univoca nel catalogo.
Il processo è richiesto dall'Attestation Scheme Provider del tipo di Credenziale, ed è indipendente dalla registrazione dei Credential Issuer, che sono aggiunti alla voce in un momento successivo.

**Input**

La definizione del tipo di Credenziale, fornita tramite la ``credential_type_declaration``, la ``credential_technical_specification``, le ``credential_policies``, il ``rulebookURI``, il ``bindingType``, l'``attestationLoS`` e i ``trustedAuthorities`` dei dati di definizione del tipo di Credenziale definiti in :ref:`onboarding-system:Registration Data Model`.
Reca il ``credential_type``, i metodi di autenticazione dell'Utente e il Livello di Garanzia minimo, il riferimento agli schema e ai formati, il riferimento al Rulebook, e la fonte dati, data da una o più ``authentic_sources`` o, quando un altro tipo di Credenziale fornisce i dati, da una o più ``parent_credentials``.
La struttura della voce versionata è definita in :ref:`registry:Digital Credentials Catalog Structure`.

L'input è fornito dall'Attestation Scheme Provider, che possiede l'Attestation Rulebook del tipo di Credenziale e ne trae i valori, si veda :ref:`onboarding-system:System Actors and Roles`.
La definizione del Rulebook è esterna al Sistema di Onboarding ed è una precondizione di questo processo, come elencato in :ref:`onboarding-system:Process Dependency Map`, quindi questo processo registra in forma strutturata ciò che il Rulebook già definisce in forma leggibile.

**Outcome**

Una voce versionata del tipo di Credenziale nel Digital Credentials Catalog, nello stato ``INACTIVE`` quando non ha ancora ``issuers``.
Abilita il :ref:`onboarding-system:Credential Type Activation and Deactivation`, la dichiarazione del tipo di Credenziale da parte di un Credential Issuer in sede di :ref:`onboarding-system:Entity Registration` e, per le categorie notificate, la :ref:`onboarding-system:Notification and Publication`.

**Process**

1. L'Attestation Scheme Provider richiede la registrazione del tipo di Credenziale e fornisce la sua definizione tratta dal Rulebook applicabile, insieme al riferimento al suo schema nello Schema Registry e alla sua fonte dati (le sue ``authentic_sources`` o le sue ``parent_credentials``).
2. L'Organismo di Supervisione verifica la richiesta e approva il tipo di Credenziale, come descritto in :ref:`onboarding-system:Eligibility and Compliance Preconditions`.
3. Il Catalog Management crea la voce versionata nel Digital Credentials Catalog nello stato ``INACTIVE``, e il Federation Trust Anchor pubblica il catalogo firmato.
4. La voce versionata è attivata quando le condizioni di :ref:`onboarding-system:Credential Type Activation and Deactivation` sono soddisfatte.

La voce versionata esiste quindi prima che qualsiasi Credential Issuer sia elencato in essa, e questo rende disponibile l'identificativo del tipo di Credenziale. Un Credential Issuer DEVE dichiarare i tipi di Credenziale che intende emettere al momento della propria :ref:`onboarding-system:Entity Registration`, e questa dichiarazione lo aggiunge al campo ``issuers`` della voce versionata.

.. note::
   Il campo ``issuers`` non è mai fornito come input di questo processo.
   Ciascuno dei suoi elementi deriva dai ``provided_attestations`` che un Credential Issuer dichiara nei propri dati di registrazione, quindi un tipo di Credenziale è registrato indipendentemente dai Credential Issuer e resta registrato quando essi cambiano.
   La fornitura dell'intera voce versionata è sintetizzata in :ref:`registry:Digital Credentials Catalog Usage`.

Credential Type Activation and Deactivation
"""""""""""""""""""""""""""""""""""""""""""

Il processo Credential Type Activation and Deactivation verifica le condizioni per l'emissione di un tipo di Credenziale e cambia la sua voce versionata tra gli stati ``ACTIVE`` e ``INACTIVE``.
Un tipo di Credenziale può essere emesso da una voce versionata solo se tale voce è ``ACTIVE``, e una sola voce versionata dello stesso ``credential_type`` DEVE essere ``ACTIVE`` in un dato momento.

**Input**

Lo stato delle tre condizioni della voce versionata, ossia i suoi ``issuers``, la sua fonte dati e il suo schema.

**Outcome**

La voce versionata è ``ACTIVE`` finché tutte e tre le condizioni sono soddisfatte, e passa a ``INACTIVE`` non appena una di esse cessa di valere, come definito in :ref:`registry:Digital Credentials Catalog Structure`.
La disattivazione impedisce una nuova emissione dalla voce versionata, ma non revoca le Credenziali già emesse da essa, che conservano il proprio stato, come descritto in :ref:`credential-revocation:Ciclo di Vita degli Attestati Elettronici`.

**Process**

1. Il Catalog Management verifica le tre condizioni della voce versionata, consultando i registri corrispondenti.

   - Almeno un Credential Issuer è elencato nel campo ``issuers``, e ciascuno di essi detiene l'entitlement corrispondente al ``legal_type`` del tipo di Credenziale.
   - La Fonte Autentica che fornisce i dati, o il tipo di Credenziale padre, è registrata e disponibile. Per una Fonte Autentica integrata tramite PDND, l'e-Service è pubblicato e l'enrolment del Credential Issuer è approvato, come descritto in :ref:`onboarding-system:Authentic Source Lifecycle and PDND Alignment`.
   - Lo schema del tipo di Credenziale è registrato nello Schema Registry per almeno uno dei formati supportati.
2. La voce versionata diventa ``ACTIVE`` quando tutte e tre le condizioni sono soddisfatte, e torna a ``INACTIVE`` non appena una di esse cessa di valere. Lo stato segue le condizioni e non è un'azione esplicita.

Credential Type Update
""""""""""""""""""""""

Il Credential Type Update pubblica una nuova versione di un tipo di Credenziale, attivando la nuova voce versionata e disattivando la precedente.
Un tipo di Credenziale non è mai modificato in place, quindi una modifica della sua definizione diventa una nuova voce versionata, con una nuova ``version``.

**Input**

La definizione aggiornata del tipo di Credenziale, fornita dall'Attestation Scheme Provider come per il :ref:`onboarding-system:Credential Type Registration`, con una nuova ``version``.

**Outcome**

Una nuova voce versionata del tipo di Credenziale, attivata quando le sue condizioni sono soddisfatte, mentre la voce versionata della versione precedente DEVE diventare ``INACTIVE``.
Le Credenziali già emesse dalla versione precedente conservano il proprio stato e non sono revocate dal versionamento, e il Credential Issuer può guidarne la riemissione, come descritto in :ref:`credential-revocation:Ciclo di Vita degli Attestati Elettronici`.

**Process**

1. L'Attestation Scheme Provider pubblica una nuova versione dell'Attestation Rulebook, o la definizione del tipo di Credenziale cambia per un altro motivo.
2. Il Catalog Management registra una nuova voce versionata, con la nuova ``version``, come nel Credential Type Registration.
3. La nuova voce versionata è attivata quando le condizioni di :ref:`onboarding-system:Credential Type Activation and Deactivation` sono soddisfatte, e la voce versionata della versione precedente passa a ``INACTIVE``.

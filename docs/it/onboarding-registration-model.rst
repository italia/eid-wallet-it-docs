.. include:: ../common/common_definitions.rst
.. Included via onboarding-system.rst at title level '-' (level 1).

Registration Model
------------------

Questa sezione fornisce la vista statica della registrazione con l'obiettivo di definire le informazioni che ciascuna entità deve fornire, le condizioni che deve soddisfare e gli artifact e le voci di registro che ottiene. È organizzata in una parte comune e in un profilo per ciascun ruolo.

Registration Data Model
^^^^^^^^^^^^^^^^^^^^^^^

Questa sezione definisce l'insieme completo dei dati che le entità forniscono al Sistema di Onboarding, con la relativa semantica e, ove applicabile, il riferimento normativo.

A seconda del ruolo, i dati sono poi codificati in un modello dati diverso: lo schema ``WalletRelyingParty`` del Register per una Wallet-Relying Party (:ref:`infrastructure-trust:Register of WRPs`), la voce dell'AS Registry per un'Authentic Source (:ref:`registry:Registro delle Fonti Autentiche`), il Digital Credentials Catalog per i Credential types (:ref:`registry:Catalogo degli Attestati Elettronici`), e il notification dataset per un Wallet Provider.

La tabella di seguito è il catalogo di riferimento dei dati, identificati da un **Data Identifier** indipendente dal formato.
Un Data Identifier può raggruppare un insieme di campi dettagliati di un modello dati di destinazione semanticamente affini e forniti insieme; in tal caso la Description elenca i campi che fornisce.
Ciascun :ref:`onboarding-system:Registration Profiles` è un'istanza di questo catalogo, che indica quali Data Identifier sono richiesti per un ruolo e come l'entità li valorizza.

.. list-table:: Registration Data Model
   :class: longtable
   :widths: 22 50 28
   :header-rows: 1

   * - **Data Identifier**
     - **Description**
     - **Normative reference**
   * - `legal_name`
     - Il nome dell'organizzazione come risulta dai registri ufficiali. Nel Register è ``legalName``, nell'AS Registry ``organization_name_l10n_id``.
     - [`CIR2025/848`_], Annex I
   * - `identifier`
     - Uno o più identificatori ufficiali dell'organizzazione. Nell'IT-Wallet il Value Added Tax Identification Number (VATIN) è richiesto per ogni entità, e un ente pubblico fornisce inoltre il proprio identificatore nazionale di tipo ``NTR``, valorizzato con il codice IPA, ossia il codice dell'Indice delle Pubbliche Amministrazioni. Gli altri tipi di identificatore della Table 2, quali EUID e LEI, sono opzionali e non sono supportati nella versione corrente. La sintassi di ``organizationIdentifier`` è definita nella clausola 5.1.4 di [`ETSI EN 319 412-1`_].
     - [`ETSI TS 119 475`_], Table 2
   * - `legal_nature`
     - Se l'entità è un ente del settore pubblico o un soggetto privato. Nel Register è il flag ``isPSB``, nell'AS Registry ``organization_type``.
     - [`CIR2025/848`_], Annex I
   * - `contact_information`
     - L'indirizzo postale, la pagina web informativa e i contatti dell'organizzazione. I contatti includono almeno un contatto istituzionale per le comunicazioni amministrative, per il quale è RACCOMANDATO un indirizzo di posta elettronica certificata (PEC), e un contatto tecnico per il supporto utenti del servizio. Nel Register il contatto di supporto è il campo ``supportURI``.
     - [`CIR2025/848`_], Annex I
   * - `service_policies`
     - I termini e le condizioni e la privacy policy del servizio, ciascuno pubblicato al proprio URL.
     - [`CIR2025/848`_], Annex I
   * - `data_protection_authority`
     - L'autorità competente per la supervisione dell'entità ai sensi della normativa sulla protezione dei dati, con le informazioni di contatto che gli User impiegano per segnalare azioni sospette. Nel Register è il campo ``supervisoryAuthority`` (:ref:`infrastructure-trust:Register of WRPs`), nell'AS Registry ``dpa_contact``.
     - Regulation (EU) 2016/679, Article 46a
   * - `entitlements`
     - Gli entitlements che l'entità richiede, che indicano i ruoli che intende svolgere nell'ecosistema e che guidano le informazioni specifiche di ruolo di seguito.
     - [`ETSI TS 119 475`_], Annex A.2
   * - `service_description`
     - Il trade name rivolto all'utente e la descrizione localizzata del servizio, forniti dalle entità che offrono un servizio alle Wallet Unit, affinché l'User possa riconoscere l'entità.
     - [`CIR2025/848`_], Annex I
   * - `intended_use`
     - Gli attributi che una Relying Party intende richiedere dalle Wallet Unit. Fornito dalle entità che richiedono attributi dalle Wallet Unit.
     - [`CIR2025/848`_], Annex I
   * - `provided_attestations`
     - I tipi di attestation che un Attestation Provider intende emettere. È dichiarato tramite la Credential type declaration, che ancora ciascun tipo al proprio Rulebook e crea o corrisponde alla voce versionata del Digital Credentials Catalog, vedi :ref:`registry:Catalogo degli Attestati Elettronici`.
     - [`CIR2025/848`_], Annex I
   * - `intermediary_relationship`
     - Per una Relying Party Intermediary, la dichiarazione di agire come intermediario. Per una Relying Party intermediata, il riferimento all'Intermediary che utilizza.
     - [`ETSI TS 119 475`_], Table 10
   * - `federation_entity_identifier`
     - L'identificatore dell'entità nel National Trust Framework, ossia ``iss`` e ``sub`` della sua Entity Configuration. Fornito da ogni Federation Entity, ossia ogni entità tranne un'Authentic Source.
     - `OID-FED`_, Section 3
   * - `federation_entity_key`
     - La chiave pubblica con cui l'entità firma i propri federation statement, fornita in formato JWK. Il resto della configurazione di federazione è pubblicato nell'Entity Configuration raggiungibile all'endpoint ``.well-known/openid-federation``.
     - `OID-FED`_, Section 3
   * - `certificate_signing_requests`
     - Un array di Certificate Signing Request in formato PKCS #10, uno per ciascun certificato X.509 che l'entità deve ottenere, ossia il WRPAC e, a seconda del ruolo, il Sign/Seal Certificate o il National Authentication Certificate. Ciascuna richiesta porta la chiave pubblica da certificare, distinta dalla Federation Entity Key.
     - :rfc:`2986`
   * - `provided_claims_purposes`
     - I claim che compongono un'Attestation, selezionati dal Claims Registry, e le finalità che serve, selezionate dalla Taxonomy, insieme alle data-provision capabilities. È memorizzato in ``data_capabilities`` della voce dell'AS Registry, ossia ``available_claims``, ``intended_purposes`` e i relativi dettagli di integrazione, vedi :ref:`registry:Registro delle Fonti Autentiche`.
     - [`CIR2025/848`_], Annex I
   * - `visual_identity`
     - Gli asset visivi di un'Authentic Source, ossia il logo dell'organizzazione e il logo e il colore di sfondo associati a un dataset fornito, ciascuno con il proprio integrity digest e il proprio testo alternativo. È memorizzato in ``organization_info`` e in ``data_capabilities`` della voce dell'AS Registry, vedi :ref:`registry:Registro delle Fonti Autentiche`. Le altre entità non lo forniscono, poiché i loro asset visivi sono contenuti nella Entity Configuration.
     - This specification
   * - `credential_type_declaration`
     - Per un Credential Issuer, i Credential types che emette, ciascuno ancorato al proprio Rulebook. Crea o corrisponde alla voce versionata del Digital Credentials Catalog e raggruppa i metadati del tipo, ossia i Digital Credential Metadata, ossia l'identificatore univoco, i metodi di autenticazione User e il minimum Level of Assurance, e il riferimento alle Authentic Sources che forniscono i propri dati, vedi :ref:`registry:Catalogo degli Attestati Elettronici`.
     - [`CIR2025/848`_], Annex I
   * - `credential_technical_specification`
     - Definizione tecnica di un Credential type, che raggruppa i campi Technical Specification del Digital Credentials Catalog, ossia gli Credential scheme, i Credential format e la authentication policy, vedi :ref:`registry:Catalogo degli Attestati Elettronici`.
     - [`CIR2025/848`_], Annex I
   * - `credential_policies`
     - Condizioni d'uso di un Credential type, che raggruppano i campi Terms of Use del Digital Credentials Catalog, ossia la Credential validity, la restriction policy, la pricing policy e i Credential purpose, vedi :ref:`registry:Catalogo degli Attestati Elettronici`.
     - [`CIR2025/848`_], Annex I
   * - `conformity_assessment`
     - L'esito della conformity assessment dell'entità. Per un PuB-EAA Provider è il conformity assessment report emesso da un conformity assessment body ai sensi dell'articolo 45f di [`EIDAS`_]. Per un Wallet Provider e un PID Provider è la valutazione eseguita nell'ambito dello schema di certificazione nazionale operato dall'Agenzia per la Cybersicurezza Nazionale (ACN). Fornito dalle categorie notificate.
     - [`EIDAS-ARF`_], Annex 2
   * - `service_supply_point`
     - L'URL presso cui una Wallet Unit avvia il processo di richiesta e ottenimento di un'Attestation dall'Issuer. Fornito dalle categorie notificate che emettono un'Attestation richiesta dalla Wallet Unit, ossia i PID Provider e i PuB-EAA Provider.
     - [`EIDAS-ARF`_], Annex 2
   * - `signing_trust_anchor`
     - Il trust anchor che supporta la validazione delle Attestation emesse dall'entità, ossia la chiave pubblica e il nome. È fornito come input dalle categorie il cui Sign/Seal Certificate non è emesso dalla root Certification Authority nazionale, ossia i QEAA Provider e i PuB-EAA Provider, la cui Qualified Certification Authority appartiene al perimetro di un Qualified Trust Service Provider, vedi :ref:`infrastructure-trust:PKI Architecture`. Per le altre categorie il trust anchor deriva dal Sign/Seal Certificate emesso tramite i Certificate Signing Request.
     - [`EIDAS-ARF`_], Annex 2

La tabella fornisce l'insieme completo.
Una data entità fornisce solo il sottoinsieme applicabile al proprio ruolo, come definito in :ref:`onboarding-system:Registration Profiles`.

Eligibility and Compliance Preconditions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Prima di qualsiasi registrazione tecnica, l'idoneità e la conformità di un'entità DEVONO essere verificate dal Supervisory Body, che si avvale del Registrar per le entità che registra e, per le categorie notificate, agisce come punto di contatto nazionale verso la Commissione europea.
Laddove un obbligo nazionale e uno EUDIW si sovrappongono, l'obbligo EUDIW è autorevole.

La verifica si applica ad Authentic Sources, Wallet Provider e Wallet-Relying Party, e il suo contenuto dipende dal ruolo.

  - **Authentic Sources**: il Supervisory Body convalida la legittimazione giuridica e l'autorità sui dati dell'organizzazione e la classifica come pubblica o privata.
    Il trust di un'Authentic Source è regolato dal framework PDND ed è al di fuori dei Trust Framework EUDIW e National Trust Framework.
  - **Wallet Providers**: l'idoneità è accertata e la conformity assessment della Wallet Solution è avviata.
    La valutazione copre la sicurezza dell'architettura del wallet, i suoi meccanismi di data protection e le sue funzionalità di user privacy, ed è la precondizione affinché la Wallet Solution sia certificata.
    La certificazione della Wallet Solution è un processo esterno, e questa fase ne usa l'esito come input.
    La certificazione segue lo schema di certificazione nazionale operato dall'Agenzia per la Cybersicurezza Nazionale (ACN), e il functional testing segue il framework di functional conformity assessment dell'UE (FCAF).
  - **PID Providers**: convalidati in base alla designazione nazionale come provider di Person Identification Data, e soggetti allo schema di certificazione nazionale operato dall'Agenzia per la Cybersicurezza Nazionale (ACN).
  - **QEAA Providers**: convalidati tramite la qualificazione e la supervisione del Qualified Trust Service Provider emittente.
  - **PuB-EAA Providers**: convalidati tramite la conformity assessment richiesta dall'articolo 45f del Regolamento eIDAS2.
  - **Non-qualified EAA Providers**: convalidati per l'idoneità all'emissione.
    Il loro trust anchor è distribuito tramite il National Trust Framework ed è definito nell'Attestation Rulebook applicabile.
  - **Relying Parties**: il Supervisory Body esegue un'autorizzazione basata su policy, valutando la tipologia organizzativa, ossia amministrazione pubblica o soggetto privato, la classificazione del settore economico e i requisiti legittimi del servizio.
  - **Relying Party Intermediaries**: dimostrano inoltre la propria idoneità ad agire per conto delle Relying Party, ai sensi dell'articolo 5b(8) del Regolamento eIDAS2 ([`EU_2024_1183`_]).
  
  .. note::
   Il Credential Issuer dichiara i Credential types che intende emettere, ciascuno ancorato al proprio Rulebook, e la sua integrazione con le Authentic Sources rilevanti è autorizzata ove necessario.

L'identity proofing delle Wallet-Relying Party DEVE essere eseguito dal Registrar secondo [`ETSI TS 119 461`_], e la verifica degli entitlements DEVE seguire l'Annex III di [`CIR2025/848`_].
Nell'IT-Wallet l'identity proofing è applicato a ogni entità che effettua l'onboarding, incluse le entità che non operano nel Trust Framework EUDIW, anche laddove non sia strettamente richiesto per esse.

Per le entità notificate le certificazioni sono un input obbligatorio all'onboarding, e in ogni caso la verifica di idoneità e conformità è una precondizione obbligatoria per la registrazione tecnica.


Registration Outcomes
^^^^^^^^^^^^^^^^^^^^^

Una registrazione riuscita produce, a seconda del ruolo e dell'ambito operativo, la voce nel Register, i Trust Artifacts e la voce nella trusted list.
Il modo in cui ciascun artifact è prodotto è descritto in :ref:`onboarding-system:Onboarding Processes`, e gli effetti delle successive modifiche in :ref:`onboarding-system:Events, Registries and Trust Artifacts`.

La tabella mostra gli artifact che variano per ruolo, ossia gli artifact EUDIW ottenuti quando l'entità si registra come Wallet-Relying Party, e gli artifact nazionali del National Trust Framework.

.. list-table:: Registration Outcomes by Entity Type
   :class: longtable
   :widths: 22 12 10 12 20 24
   :header-rows: 1

   * - **Entity type**
     - **Register record**
     - **WRPAC**
     - **WRPRC**
     - **National X.509 certificate**
     - **LoTE entry**
   * - PID Provider
     - yes
     - yes
     - yes
     - no
     - PID Providers LoTE
   * - QEAA Provider
     - yes
     - yes
     - yes
     - no
     - EUMS TL, referenced in the LOTL
   * - PuB-EAA Provider
     - yes
     - yes
     - yes
     - no
     - PuB-EAA Providers LoTE
   * - Non-qualified EAA Provider
     - yes only if it issues an Attestation published in a EU Rulebook
     - yes only if it issues an Attestation published in a EU Rulebook
     - yes only if it issues an Attestation published in a EU Rulebook
     - Sign/Seal Certificate, for the Attestations anchored to the National Trust Framework
     - None, trust anchor distribution defined in the applicable Attestation Rulebook
   * - Relying Party
     - yes
     - yes
     - yes
     - Authentication Certificate, where the Relying Party operates in the Proximity Flow
     - None
   * - Relying Party Intermediary
     - yes
     - yes
     - No
     - No
     - None
   * - Wallet Provider
     - no
     - no
     - no
     - Sign/Seal Certificate
     - Wallet Providers LoTE

.. note::
   La federation registration è comune a ogni entità e, come risultato, ogni entità ottiene un Subordinate Statement emesso dalla propria Federation Authority e un registration Trust Mark.

.. note::
   Un'entità che opera solo a livello nazionale non ottiene record nel Register, WRPAC né WRPRC.
   Detiene il proprio Entity Statement e il registration Trust Mark dalla federation registration e, ove il suo ruolo lo richieda, il proprio certificato nazionale, ossia il Sign/Seal Certificate per un Credential Issuer nazionale o l'Authentication Certificate per una Relying Party che opera nel Proximity Flow.

Registration Profiles
^^^^^^^^^^^^^^^^^^^^^

Questa Sezione descrive la registrazione di ciascun ruolo come profilo.
Un'entità può detenere più di un entitlement in un unico record di registrazione e per più di un ruolo, quindi i profili non sono mutuamente esclusivi e si compongono.
Ad esempio, un'entità può essere contemporaneamente una Relying Party e un QEAA Provider, e in tal caso il suo input è l'unione dei due profili e il suo esito è l'unione dei due.

PID Provider
""""""""""""

.. note::
   Draft. To be written.


QEAA Provider
"""""""""""""

.. note::
   Draft. To be written.


PuB-EAA Provider
""""""""""""""""

.. note::
   Draft. To be written.


Non-Qualified EAA Provider
""""""""""""""""""""""""""

.. note::
   Draft. To be written.



Relying Party
"""""""""""""

La tabella di seguito elenca i Data Identifier che una Relying Party fornisce al Sistema di Onboarding.
La semantica di ciascun Data Identifier è definita in :ref:`onboarding-system:Registration Data Model`. Salvo diversa indicazione, le informazioni seguenti sono REQUIRED.

.. list-table:: Relying Party Registration Data
   :class: longtable
   :widths: 34 66
   :header-rows: 1

   * - **Data Identifier**
     - **Values**
   * - `legal_name`
     - Il legal name della Relying Party come risulta dai registri ufficiali.
   * - `identifier`
     - Il VATIN della Relying Party. Un ente pubblico fornisce anche il proprio identificatore ``NTR`` valorizzato con il codice IPA.
   * - `legal_nature`
     - Se la Relying Party è un ente del settore pubblico o un soggetto privato.
   * - `contact_information`
     - Il contatto istituzionale (PEC) e l'indirizzo email del contatto di supporto tecnico. La pagina web informativa è fornita ove disponibile.
   * - `service_policies`
     - I termini e le condizioni e la privacy policy del servizio.
   * - `service_description`
     - La descrizione localizzata del servizio offerto dalla Relying Party, una descrizione per servizio. Il trade name rivolto all'utente è fornito ove disponibile.
   * - `data_protection_authority`
     - Il contatto della Data Protection Authority.
   * - `entitlements`
     - Gli entitlements che indicano il ruolo di Relying Party e i ruoli aggiuntivi svolti ove applicabile.
   * - `intended_use`
     - Il tipo di Attestation e, opzionalmente, gli attributi che la Relying Party intende richiedere dalle Wallet Unit, con una definizione di intended use per servizio.
   * - `intermediary_relationship`
     - REQUIRED solo ove la Relying Party opera tramite un RP Intermediary. In tal caso fa riferimento all'identificatore del proprio RP intermediary. Il lato RP intermediary è descritto in :ref:`onboarding-system:Relying Party Intermediary`.
   * - `federation_entity_identifier`
     - Il Federation Entity Identifier della Relying Party nel National Trust Framework.
   * - `federation_entity_key`
     - REQUIRED per una Relying Party che opera senza intermediario. Una Relying Party che opera tramite un RP Intermediary NON DEVE fornirlo, poiché è registrato dal proprio RP Intermediary secondo il National Trust Framework.
   * - `certificate_signing_requests`
     - Un Certificate Signing Request per ciascun certificato X.509 di cui la Relying Party ha bisogno, ossia il WRPAC quando opera nel Trust Framework EUDIW, e il National Authentication Certificate quando opera solo nel National Trust Framework e supporta il Proximity Flow.

.. note::
   Una Relying Party intermediata si registra tramite il Sistema di Onboarding solo quando opera nel Trust Framework EUDIW, per abilitare le operazioni transfrontaliere. In questo caso DEVE avere un record nel Register e DEVE ottenere il proprio WRPAC e, ove applicabile, il proprio WRPRC, emessi tramite il Sistema di Onboarding.
   Una Relying Party intermediata che opera solo a livello nazionale è registrata dal proprio RP Intermediary e non è registrata nel Register. In questo caso, quando la Relying Party intermediata è una Mobile Relying Party Instance, DEVE essere registrata tramite il Sistema di Onboarding per ottenere un Authentication X.509 Certificate.


Relying Party Intermediary
""""""""""""""""""""""""""

Nel National Trust Framework la Relying Party Intermediary è un Federation Intermediate, ossia effettua l'onboarding delle proprie Relying Party intermediate in autonomia, pubblicando i loro Subordinate Statement, come descritto in :ref:`infrastructure-trust:Trust Mark registration-entity`.
Fornisce gli stessi Data Identifier di una :ref:`onboarding-system:Relying Party`, con le differenze indicate nella tabella di seguito.
I Data Identifier non elencati qui sono forniti come per una Relying Party.

.. list-table:: Relying Party Intermediary Registration Data, differences from the Relying Party
   :class: longtable
   :widths: 34 66
   :header-rows: 1

   * - **Data Identifier**
     - **Values**
   * - `intended_use`
     - Non fornito. Una Relying Party Intermediary non richiede attributi per sé, ma per conto delle Relying Party intermediate.
   * - `intermediary_relationship`
     - Valorizzato sul lato intermediario, ossia la Relying Party dichiara di essere un intermediario designato.
   * - `federation_entity_identifier`
     - Il Federation Entity Identifier della Relying Party Intermediary nel National Trust Framework.
   * - `federation_entity_key`
     - La Federation Entity Key della Relying Party Intermediary.

.. note::
  La registrazione di una Relying Party Intermediary e la registrazione delle proprie Relying Party intermediate sono collegate: l'Intermediary dichiara di agire come intermediario, e ciascuna Relying Party intermediata lo referenzia nel proprio profilo :ref:`onboarding-system:Relying Party`.


Wallet Provider
"""""""""""""""

.. note::
   Draft. To be written.


Authentic Source
""""""""""""""""

.. note::
   Draft. To be written.


.. include:: ../common/common_definitions.rst
.. Included via onboarding-system.rst at title level '-' (level 1).

Registration Model
------------------

Questa sezione fornisce la vista statica della registrazione, con l'obiettivo di definire le informazioni che ciascuna entità deve fornire, quali condizioni deve soddisfare e quali artifact e voci di registro ottiene.
È organizzata in una parte comune e in un profilo per ciascun ruolo.

Registration Data Model
^^^^^^^^^^^^^^^^^^^^^^^

Questa sezione definisce l'insieme completo dei dati che le entità forniscono al Sistema di Onboarding, insieme ai dati che definiscono un tipo di Credenziale, con la relativa semantica e, ove applicabile, il relativo riferimento normativo.
I dati sono identificati da un **Data Identifier** indipendente dal formato.

Le tabelle seguenti forniscono:

- *Dati di registrazione di base* forniti da ogni entità, indipendentemente dal proprio ruolo.
- *Dati di registrazione estesi* forniti da un'entità in funzione del proprio ruolo, dove ciascuna istanza di :ref:`onboarding-system:Registration Profiles` specifica quali dati estesi il ruolo fornisce e come l'entità li popola.
- *Dati di definizione del tipo di Credenziale* che descrivono un tipo di Credenziale.

A seconda del ruolo, i dati di registrazione sono poi codificati in un data model diverso, lo schema ``WalletRelyingParty`` del Register per una Wallet-Relying Party (:ref:`infrastructure-trust:Register of WRPs`), la voce dell'AS Registry per una Fonte Autentica (:ref:`registry:Authentic Source Registry`), e il dataset di notifica per un'Entità notificabile.
I dati di definizione del tipo di Credenziale sono codificati nella voce versionata del Digital Credentials Catalog (:ref:`registry:Digital Credentials Catalog`).
La mappatura verso i data model di destinazione è data in :ref:`onboarding-system:Mapping to the Registry Data Models`.

.. list-table:: Base Registration Data
   :class: longtable
   :widths: 26 46 28
   :header-rows: 1

   * - **Data Identifier**
     - **Description**
     - **Normative reference**
   * - `legal_name`
     - Il nome dell'organizzazione come compare nei registri ufficiali.
     - [`CIR2025/848`_], Annex I
   * - `identifier`
     - Uno o più identificativi ufficiali dell'organizzazione. All'interno di IT-Wallet il Value Added Tax Identification Number (VATIN) è OBBLIGATORIO per ogni entità, e un ente pubblico DEVE inoltre fornire il proprio identificativo nazionale di tipo ``NTR``, valorizzato con il proprio codice IPA, ossia il codice dell'Indice delle Pubbliche Amministrazioni italiano. Un'organizzazione che possiede un European Unique Identifier (EUID) DEVE fornirlo. Gli altri tipi di identificativo della Table 2, quali il Legal Entity Identifier (LEI), sono OPZIONALI e non sono supportati nella versione corrente. Per maggiori dettagli si fa riferimento alla sintassi dell'``organizationIdentifier`` definita nella clausola 5.1.4 di [`ETSI EN 319 412-1`_].
     - [`ETSI TS 119 475`_], Table 2
   * - `legal_nature`
     - Se l'entità è un organismo del settore pubblico o un'entità privata.
     - [`CIR2025/848`_], Annex I
   * - `contact_information`
     - L'indirizzo postale, la pagina web informativa e i contatti dell'organizzazione. I contatti includono almeno un contatto istituzionale per le comunicazioni amministrative, per il quale è RACCOMANDATO un indirizzo di posta elettronica certificata (PEC), e un contatto tecnico per il supporto utente del servizio.
     - [`CIR2025/848`_], Annex I
   * - `service_policies`
     - I termini e le condizioni e l'informativa sulla privacy del servizio, ciascuno pubblicato al proprio URL.
     - [`CIR2025/848`_], Annex I
   * - `data_protection_authority`
     - L'indirizzo e-mail di contatto dell'autorità competente per la vigilanza dell'entità ai sensi della normativa sulla protezione dei dati. DEVE essere fornito per ciascun intended use della Wallet-Relying Party.
     - [`CIR2025/848`_], Annex I, in conformità al Regolamento (UE) 2016/679.

I dati di registrazione estesi sono forniti nella tabella seguente.
Una data entità fornisce solo il sottoinsieme che si applica al proprio ruolo, come definito nel corrispondente profilo in :ref:`onboarding-system:Registration Profiles`.

.. list-table:: Extended Registration Data
   :class: longtable
   :widths: 26 46 28
   :header-rows: 1

   * - **Data Identifier**
     - **Description**
     - **Normative reference**
   * - `entitlements`
     - Gli entitlement che l'entità richiede, i quali dichiarano i ruoli che intende svolgere nell'ecosistema.
     - [`ETSI TS 119 475`_], Annex A.2
   * - `service_description`
     - Il nome commerciale e la descrizione localizzata di ciascun Relying Party Service che l'entità offre alle Wallet Unit. Nel Trust Framework EUDIW questi dati sono forniti per Service, si veda `relying_party_services`.
     - [`CIR2025/848`_], Annex I; [`EIDAS-ARF`_] Reg_34
   * - `intended_use`
     - Gli attributi che una Relying Party intende richiedere dalle Wallet Unit, vincolati a uno specifico Relying Party Service. Una Relying Party DEVE dichiarare quali dei propri intended use registrati si applicano a ciascuno dei propri Service registrati ([`EIDAS-ARF`_] Reg_10d).
     - [`CIR2025/848`_], Annex I; [`EIDAS-ARF`_] Reg_10d
   * - `relying_party_services`
     - Uno o più Relying Party Service registrati dall'entità. Ciascun Service ha un nome commerciale adatto alla presentazione all'Utente (``serviceTradeName``). ``serviceIdentifier``, quando registrato, è univoco all'interno dell'entità e DEVE essere registrato se il Service si avvale di un Intermediario (`EUDI-TS 5`_ v1.5) o se un WRPAC è emesso per quel Service ([`EIDAS-ARF`_] Reg_33). Il Service reca gli intended use che si applicano a esso e, ove applicabile, la relazione di intermediazione. Un'entità in registrazione che opera nel Trust Framework EUDIW DEVE registrare almeno un Service e DEVE ricevere almeno un WRPAC per ciascun Service registrato. I corrispondenti WRPRC sono emessi automaticamente come definito in :ref:`onboarding-system:Wallet-Relying Party Registration Certificate Issuance`. Lo stesso identificativo e lo stesso nome commerciale del Service DEVONO essere copiati in ciascun WRPRC corrispondente.
     - [`EIDAS-ARF`_] Reg_10a, Reg_10d, Reg_33, Reg_34, RPRC_07a; [`CIR2026/1730`_]; `EUDI-TS 5`_, ``WalletRelyingPartyService``
   * - `provided_attestations`
     - I tipi di Attestato che un Credential Issuer intende emettere. All'interno di IT-Wallet ciascuno di essi fa riferimento a una voce versionata già presente nel Digital Credentials Catalog, e la dichiarazione aggiunge il Credential Issuer al campo ``issuers`` di tale voce, insieme alle capacità di emissione offerte per quel tipo di Credenziale (i flussi di emissione supportati, i parametri dell'emissione differita e la documentazione del servizio di emissione), si veda :ref:`registry:Digital Credentials Catalog`.
     - [`CIR2025/848`_], Annex I
   * - `intermediary_relationship`
     - Vincolato a un Relying Party Service. Per un Relying Party Service intermediato, il riferimento all'Intermediary Service che utilizza (``usesIntermediaries``). Per un Relying Party Intermediary Service, la dichiarazione che agisce come intermediario (``isIntermediary``) e gli identificativi di Service che serve (``servedWRPServices``, [`CIR2026/1730`_], Annex I). Un Intermediary Service puro NON DEVE registrare un entitlement (`EUDI-TS 5`_ v1.5).
     - [`ETSI TS 119 475`_], Table 10; [`EIDAS-ARF`_] RPRC_04, Reg_34a; `EUDI-TS 5`_
   * - `trust_framework_scope`
     - La dichiarazione del Trust Framework in cui l'entità intende operare, secondo :ref:`infrastructure-trust:Infrastructure of Trust` e :ref:`trust-evaluation:Trust Framework Selection`. La dichiarazione è fornita dai ruoli per i quali questa scelta non è già fissata dalla notifica, e determina i Trust Artifact che l'entità ottiene e il modo in cui gli altri Data Identifier del profilo sono forniti. Si applica all'entità, mentre ``trustedAuthorities`` di un tipo di Credenziale si applica alla validazione di un Attestato di quel tipo.
     - La presente specifica
   * - `federation_entity_identifier`
     - L'identificativo dell'Entità di Federazione nel National Trust Framework, ossia l'``iss`` e il ``sub`` della sua Entity Configuration.
     - `OID-FED`_, Section 3
   * - `federation_entity_key`
     - La chiave pubblica con cui l'Entità di Federazione firma la propria Entity Configuration. DEVE essere fornita in formato JWK. Il resto della configurazione di federazione è pubblicato nell'Entity Configuration raggiungibile all'endpoint ``.well-known/openid-federation``.
     - `OID-FED`_, Section 3
   * - `certificate_signing_requests`
     - Un array di Certificate Signing Request in formato PKCS #10, una per ciascun certificato X.509 che l'entità necessita di ottenere, ossia, a seconda del ruolo, il WRPAC, il Sign/Seal Certificate o il National Authentication Certificate. Per una Wallet-Relying Party che opera nel Trust Framework EUDIW DEVE esserci una Certificate Signing Request per il WRPAC per ciascun Service registrato. Per un Intermediario di Relying Party DEVE esserci una Certificate Signing Request per il WRPAC per ciascun Relying Party Service intermediato che serve ([`EIDAS-ARF`_] Reg_34a). Ciascuna richiesta reca la chiave pubblica da certificare. DEVE essere distinta dalla Federation Entity Key. Il loro profilo è definito in :ref:`onboarding-system:Certificate Signing Request Profile` e sono l'input di :ref:`onboarding-system:Certificate and Trust Artifact Issuance`, dove sono presentate nell'ordine ACME.
     - :rfc:`2986`
   * - `provided_claims_purposes`
     - I claim che compongono un Attestato, selezionati dal Claims Registry, e gli scopi che utilizza, selezionati dalla Taxonomy, insieme alle capacità di fornitura dei dati. Raggruppa i ``data_capabilities`` della voce dell'AS Registry, si veda :ref:`registry:Authentic Source Registry`.
     - La presente specifica
   * - `visual_identity`
     - Gli asset visivi di una Fonte Autentica, ossia il logo dell'organizzazione e il logo e il colore di sfondo associati a un dataset fornito, ciascuno con il proprio digest di integrità e il proprio testo alternativo.
     - La presente specifica
   * - `conformity_assessment`
     - L'esito della valutazione di conformità dell'entità, quale il Conformity Assessment Report o le valutazioni effettuate nell'ambito dello schema di certificazione nazionale operato dall'Agenzia per la Cybersicurezza Nazionale (ACN) e i test funzionali nell'ambito del EU functional conformity assessment framework (FCAF). DEVE essere fornito dalle categorie notificate.
     - [`EIDAS-ARF`_], Annex 2
   * - `service_supply_point`
     - L'URL presso cui una Wallet Unit avvia il processo di richiesta e ottenimento di un Attestato dall'Issuer. DEVE essere fornito dalle categorie notificate che emettono un Attestato richiesto dalla Wallet Unit.
     - [`EIDAS-ARF`_], Annex 2
   * - `signing_trust_anchor`
     - Il trust anchor a supporto della validazione degli Attestati che l'entità emette, ossia la chiave pubblica e il nome. DEVE essere fornito come input solo dalle categorie il cui Sign/Seal Certificate non è emesso dalla National Root Certification Authority, si veda :ref:`infrastructure-trust:PKI Architecture`. Per le altre categorie il trust anchor deriva dal Sign/Seal Certificate emesso tramite le Certificate Signing Request.
     - [`EIDAS-ARF`_], Annex 2
   * - `verification_endpoint`
     - L'interfaccia di verifica transfrontaliera esposta ai Qualified Trust Service Provider per gli attributi dell'Annex VI esportati nel EUDIW Catalogue of Attributes, conforme a ETSI TS 119 478 e dichiarata nei ``data_capabilities`` della voce dell'Authentic Source Registry, si veda :ref:`registry:Authentic Source Registry`. È fornita dalla Fonte Autentica.
     - [`EUDI-TS 11`_], Section 2.1

I dati seguenti definiscono un tipo di Credenziale e non un'entità.
Per questo motivo non sono dati di registrazione, non seguono un profilo di :ref:`onboarding-system:Registration Profiles` e sono l'input di :ref:`onboarding-system:Credential Type Registration`.
Sono forniti dall'Attestation Scheme Provider, che possiede l'Attestation Rulebook del tipo di Credenziale, e sono tratti dal Rulebook stesso.
Lo stesso criterio si applica alla definizione di un claim, registrato tramite :ref:`onboarding-system:Claim Registration`.

.. list-table:: Credential Type Definition Data
   :class: longtable
   :widths: 26 46 28
   :header-rows: 1

   * - **Data Identifier**
     - **Description**
     - **Normative reference**
   * - `credential_type_declaration`
     - Il tipo di Credenziale, ancorato al proprio Rulebook. Crea la voce versionata del Digital Credentials Catalog e raggruppa i Digital Credential Metadata del tipo (l'identificativo univoco e la versione, il nome leggibile, la classificazione per domain e class, i metodi di autenticazione dell'Utente e il Livello di Garanzia minimo), insieme al riferimento alle Fonti Autentiche, o ai tipi di Credenziale padre, che ne forniscono i dati, si veda :ref:`registry:Digital Credentials Catalog`.
     - [`CIR2025/848`_], Annex I
   * - `credential_technical_specification`
     - Definizione tecnica di un tipo di Credenziale, che raggruppa i campi Technical Specification del Digital Credentials Catalog, ossia gli schema della Credenziale, i formati della Credenziale e la policy di autenticazione, si veda :ref:`registry:Digital Credentials Catalog`.
     - [`CIR2025/848`_], Annex I
   * - `credential_policies`
     - Condizioni di uso di un tipo di Credenziale, che raggruppano i campi Terms of Use del Digital Credentials Catalog, ossia la validità della Credenziale, la restriction policy, la pricing policy e gli scopi della Credenziale, si veda :ref:`registry:Digital Credentials Catalog`.
     - [`CIR2025/848`_], Annex I
   * - `trustedAuthorities`
     - Le autorità fidate che definiscono il trust framework del tipo di Credenziale nel Digital Credentials Catalog, ossia i trust anchor su cui un verificatore fa affidamento per validare l'Attestato, si veda :ref:`registry:Digital Credentials Catalog`.
     - [`EUDI-TS 11`_], Section 4.3
   * - `rulebookURI`
     - L'URI dell'Attestation Rulebook in forma leggibile che definisce gli aspetti non machine-readable del tipo di Credenziale nel Digital Credentials Catalog, si veda :ref:`registry:Digital Credentials Catalog`.
     - [`EUDI-TS 11`_], Section 4.3
   * - `bindingType`
     - Il tipo di associazione crittografica della chiave richiesto per l'emissione del tipo di Credenziale nel Digital Credentials Catalog, uno tra ``claim``, ``key``, ``biometric`` o ``none``, si veda :ref:`registry:Digital Credentials Catalog`.
     - [`EUDI-TS 11`_], Section 4.3
   * - `attestationLoS`
     - Il livello di sicurezza (Level of Security) dell'attestazione del tipo di Credenziale nel Digital Credentials Catalog, ossia la resistenza al potenziale di attacco richiesta per l'autenticazione dell'utente e per l'archiviazione delle chiavi, si veda :ref:`registry:Digital Credentials Catalog`.
     - [`EUDI-TS 11`_], Section 4.3

.. note::
   Il `provided_attestations` resta parte dei dati di registrazione di un Credential Issuer, perché è la dichiarazione dei tipi di Credenziale che il Credential Issuer intende emettere e non la definizione di tali tipi.
   I due sono distinti: la definizione crea la voce versionata, la dichiarazione aggiunge il Credential Issuer al suo campo ``issuers``.

Mapping to the Registry Data Models
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Il Sistema di Onboarding raccoglie i dati di registrazione e i dati di definizione del tipo di Credenziale, che sono poi codificati nel data model di destinazione, che per i dati di registrazione dipende dal ruolo.
La tabella seguente mappa ciascun Data Identifier sui campi dei data model di destinazione, per i Data Identifier la cui mappatura non è uno-a-uno con un singolo campo.

.. list-table:: Mapping of the Data Identifiers to the destination data models
   :class: longtable
   :widths: 30 70
   :header-rows: 1

   * - **Data Identifier**
     - **Destination fields**
   * - `legal_name`
     - Nel Register, il ``legalName`` del ``legalPerson``. Nell'AS Registry, l'``organization_name_l10n_id``. Nel Trust Mark di registrazione, l'``organization_name``. Nel Digital Credentials Catalog, l'``organization_name_l10n_id`` dell'elemento ``issuers`` del Credential Issuer.
   * - `identifier`
     - Nel Register, l'array ``identifier``, ciascun elemento recante il proprio ``type`` e il proprio valore. Nel Trust Mark di registrazione, il ``vat_number`` per un'entità privata, l'``ipa_code`` per un ente pubblico e il ``legal_identifier``. Nel Digital Credentials Catalog, l'``organization_code`` dell'elemento ``issuers`` del Credential Issuer.
   * - `legal_nature`
     - Nel Register, il flag ``isPSB``. Nell'AS Registry, l'``organization_type``. Nel Trust Mark di registrazione, il ``public_body``.
   * - `contact_information`
     - Nel Register: 
     
         - ``postalAddress``, 
         - ``email``,
         - ``phone``,
         - ``infoURI``,
         - ``supportURI``. 
       
       Nell'AS Registry: 
         
         - ``contacts``, 
         - ``homepage_uri``.
       
       Nel Trust Mark di registrazione, l'``email`` e il ``support_uri``. Nell'Entity Configuration, i ``contacts`` e l'``homepage_uri`` dei metadata ``federation_entity``. Nel Digital Credentials Catalog, i ``contacts`` e l'``homepage_uri`` dell'elemento ``issuers`` del Credential Issuer.
   * - `service_policies`
     - Nel Register, il ``policyURI`` di ciascun elemento dell'array ``policy``, distinto dal proprio ``type``. Nel Trust Mark di registrazione, la ``privacy_policy``. Nell'Entity Configuration, il ``policy_uri`` e il ``tos_uri`` dei metadata ``federation_entity``. Nel Digital Credentials Catalog, il ``policy_uri`` e il ``tos_uri`` dell'elemento ``issuers`` del Credential Issuer.
   * - `data_protection_authority`
     - Nel Register, la ``supervisoryAuthority``. Nell'AS Registry, il ``dpa_contact``. Nel Trust Mark di registrazione, la ``supervisory_authority``.
   * - `entitlements`
     - Nel Register, l'array ``entitlements`` di ciascun elemento ``services[]``. Nel Trust Mark di registrazione, gli ``entitlements``. Nel Digital Credentials Catalog, il ``legal_type`` dell'elemento ``issuers`` del Credential Issuer.
   * - `service_description`
     - Nel Register, il ``tradeName`` a livello di entità ove presente, e per Service il ``serviceTradeName`` e la ``srvDescription`` di ciascun elemento ``services[]``. Nel WRPAC, ``subject.commonName`` DEVE coincidere con ``serviceTradeName``. Nel WRPRC, ``name`` DEVE coincidere con ``serviceTradeName``. Nel Trust Mark di registrazione, la ``srv_description``.
   * - `relying_party_services`
     - Nel Register, l'array ``services`` di oggetti ``WalletRelyingPartyService``, ciascuno recante ``serviceIdentifier``, ``serviceTradeName``, ``srvDescription``, ``intendedUses``, ``entitlements``, ``providesAttestations``, ``isIntermediary``, ``usesIntermediaries`` e ``servedWRPServices``, come definito in `EUDI-TS 5`_. Nel WRPAC, ``subject.commonName`` (Reg_34) e l'identificativo del Service in ``subjectAltName`` (Reg_33). Nel WRPRC, ``name`` e ``srv_id`` (RPRC_07a).
   * - `intended_use`
     - Nel Register, l'array ``intendedUses`` del corrispondente elemento ``services[]``, ciascun elemento recante il proprio ``intendedUseIdentifier``, ``purpose``, ``privacyPolicy`` e ``credentials``. Nel Trust Mark di registrazione, i ``credentials`` e il ``purpose``.
   * - `provided_attestations`
     - Nel Register, l'array ``providesAttestations`` del corrispondente elemento ``services[]``, ciascun ``ProvidedAttestation`` recante ``format`` e ``type`` come definito in `EUDI-TS 5`_ versione 1.5. Nel Trust Mark di registrazione, i ``provides_attestations``. Nel Digital Credentials Catalog, l'elemento dell'array ``issuers`` di ciascun tipo di Credenziale dichiarato, inclusi i suoi ``issuance_flows`` e il suo ``service_documentation_uri``.
   * - `provided_claims_purposes`
     - Nell'AS Registry, i ``data_capabilities``, ossia 
     
         - ``available_claims``, 
         - ``intended_purposes``, 
         - ``integration_method``, 
         - ``integration_endpoint``, 
         - ``api_specification``, 
         - ``data_provision``, 
         - ``update_frequency``, 
         - ``service_documentation_uri``.
   * - `visual_identity`
     - Nell'AS Registry i 
     
         - ``logo_uri`` dell'``organization_info``,
         - ``background_color`` dei ``data_capabilities``, 
       
       ciascuno con il proprio digest di integrità e il proprio testo alternativo.
   * - `credential_type_declaration`
     - Nel Digital Credentials Catalog: 
     
         - ``credential_type``, 
         - ``version``, 
         - ``credential_name_l10n_id``, 
         - ``domains``, 
         - ``classes``, 
         - ``authentication``,
       
       e le ``authentic_sources``, o le ``parent_credentials``, che forniscono i dati del tipo di Credenziale.
   * - `credential_technical_specification`
     - Nel Digital Credentials Catalog:
     
         - ``schema_uri``, 
         - ``format``, 
         - ``vct``,
         - ``docType``.
   * - `credential_policies`
     - Nel Digital Credentials Catalog:
     
         - ``validity_info``, 
         - ``restriction_policy``, 
         - ``pricing_policy``, 
         - ``purposes``, 
         - ``legal_type``.
   * - `conformity_assessment`
     - Nel dataset di notifica, il rapporto di valutazione di conformità.
   * - `service_supply_point`
     - Nel dataset di notifica, il service supply point.
   * - `signing_trust_anchor`
     - Nel dataset di notifica, il trust anchor.

Alcune informazioni sono presenti sia nei dati registrati sia nell'Entity Configuration auto-firmata dell'Entità.
Il valore registrato è autorevole, asserito dal Registrar nel Register e dal Federation Trust Anchor nel Trust Mark di registrazione, mentre i parametri informativi dei metadata ``federation_entity`` sono pubblicati sotto la responsabilità dell'Entità.
Ove il Sistema di Onboarding richieda un valore che l'Entità pubblica anche nella propria Entity Configuration, DEVE leggere l'Entity Configuration e DEVE verificarne la corrispondenza. Una mancata corrispondenza DEVE bloccare la registrazione, e dopo la registrazione DEVE essere risolta tramite un :ref:`onboarding-system:Entity Update`.
All'interno di IT-Wallet la ``metadata_policy`` del Subordinate Statement fissa l'``organization_name`` dei metadata ``federation_entity`` al valore registrato, così che il nome mostrato all'Utente non possa divergere da quello recato dal WRPAC e dal WRPRC. Gli altri parametri informativi non sono fissati.

Eligibility and Compliance Preconditions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Prima di qualsiasi registrazione tecnica, l'eleggibilità e la conformità di un'entità DEVONO essere verificate dall'Organismo di Supervisione, che si avvale del Registrar per le entità che registra e, per le categorie notificate, agisce come punto di contatto nazionale verso la Commissione Europea.
Ove un obbligo nazionale e un obbligo EUDIW si sovrappongano, l'obbligo EUDIW è autorevole.

La verifica si applica alle Fonti Autentiche, ai Fornitori di Wallet e alle Wallet-Relying Party, e il suo contenuto dipende dal ruolo.

  - **Fonti Autentiche**: l'Organismo di Supervisione valida la posizione legale e l'autorità sui dati dell'organizzazione e la classifica come pubblica o privata.
    La trust di una Fonte Autentica è governata dal framework PDND ed è al di fuori dei Trust Framework EUDIW e Nazionale.
  - **Fornitori di Wallet**: l'eleggibilità è accertata e la valutazione di conformità della Soluzione Wallet è condotta.
    La valutazione copre la sicurezza dell'architettura del wallet, i suoi meccanismi di protezione dei dati e le sue funzionalità di privacy dell'utente, ed è la precondizione affinché la Soluzione Wallet sia certificata.
    La certificazione della Soluzione Wallet è un processo esterno, e questa fase ne utilizza l'esito come input.
    La certificazione segue lo schema di certificazione nazionale operato dall'Agenzia per la Cybersicurezza Nazionale (ACN), e i test funzionali seguono il EU functional conformity assessment framework (FCAF).
  - **PID Provider**: validati per designazione nazionale come fornitori di Person Identification Data, soggetti allo schema di certificazione nazionale operato dall'Agenzia per la Cybersicurezza Nazionale (ACN) e ai test funzionali nell'ambito del EU functional conformity assessment framework (FCAF).
  - **QEAA Provider**: validati tramite la qualificazione e la vigilanza del Qualified Trust Service Provider emittente.
  - **PuB-EAA Provider**: validati tramite la valutazione di conformità richiesta dall'Articolo 45f del Regolamento eIDAS2.
  - **Non-qualified EAA Provider**: validati per l'eleggibilità a emettere.
    Il loro trust anchor è distribuito tramite il National Trust Framework ed è definito nell'Attestation Rulebook applicabile.
  - **Relying Party**: l'Organismo di Supervisione esegue un'autorizzazione basata su policy, valutando il tipo organizzativo, ossia pubblica amministrazione o entità privata, la classificazione del settore di attività e i requisiti legittimi del servizio.
  - **Intermediari di Relying Party**: dimostrano inoltre la propria eleggibilità ad agire per conto delle Relying Party, ai sensi dell'Articolo 5b(8) del Regolamento eIDAS2 ([`EU_2024_1183`_]).
  
  .. note::
   Il Credential Issuer dichiara i tipi di Credenziale che intende emettere, ciascuno ancorato al proprio Rulebook, e la sua integrazione con le Fonti Autentiche rilevanti è autorizzata ove necessario.

L'Organismo di Supervisione approva inoltre i claim, gli schema e i tipi di Credenziale prima che siano registrati nei registri, e tale approvazione è una precondizione di :ref:`onboarding-system:Claim Registration`, di :ref:`onboarding-system:Schema Provisioning` e di :ref:`onboarding-system:Credential Type Registration`.

L'identity proofing delle Wallet-Relying Party DEVE essere effettuato dal Registrar secondo [`ETSI TS 119 461`_], e la verifica degli entitlement DEVE seguire l'Annex III di [`CIR2025/848`_].
All'interno di IT-Wallet l'identity proofing è applicato a ogni entità che si onboarda, comprese le entità che non operano nel Trust Framework EUDIW, anche ove non sia strettamente richiesto per esse.

Per le entità notificate le certificazioni sono un input obbligatorio dell'onboarding, e in ogni caso la verifica di eleggibilità e conformità è una precondizione obbligatoria per la registrazione tecnica.


Trust Artifacts Registration Outcomes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Una registrazione riuscita produce, a seconda del ruolo e dell'ambito di operatività, i Trust Artifact. Per le categorie notificate, la voce in una List of Trusted Entities consegue da :ref:`onboarding-system:Notification and Publication`, che è un processo distinto.
Il modo in cui ciascun artifact è prodotto è descritto in :ref:`onboarding-system:Onboarding Processes`, e gli effetti delle modifiche successive in :ref:`onboarding-system:Events, Registries and Trust Artifacts`.

La tabella mostra gli artifact che variano per ruolo.
La colonna del certificato X.509 raggruppa i certificati X.509 che l'entità ottiene, in particolare il WRPAC, il Sign/Seal Certificate e il National Authentication Certificate, mentre il WRPRC è mostrato a parte perché non è un certificato X.509 ma un JSON Web Token o un CBOR Web Token.

.. list-table:: Trust Artifacts Registration Outcomes by Entity Type
   :class: longtable
   :widths: 20 12 10 34 24
   :header-rows: 1

   * - **Entity type**
     - **Register record**
     - **WRPRC**
     - **X.509 certificate**
     - **LoTE entry**
   * - PID Provider
     - sì
     - sì
     - il WRPAC e il Sign/Seal Certificate
     - PID Providers LoTE
   * - QEAA Provider
     - sì
     - sì
     - il WRPAC. Il Sign/Seal Certificate è il certificato qualificato emesso dal QTSP
     - EUMS TL, referenziato nella LOTL
   * - PuB-EAA Provider
     - sì
     - sì
     - il WRPAC. Il Sign/Seal Certificate è il certificato qualificato emesso dal QTSP
     - PuB-EAA Providers LoTE
   * - Non-qualified EAA Provider
     - sì solo se emette un Attestato pubblicato in un EU Rulebook
     - sì solo se emette un Attestato pubblicato in un EU Rulebook
     - il WRPAC solo se emette un Attestato pubblicato in un EU Rulebook, e il Sign/Seal Certificate
     - Nessuna, distribuzione del trust anchor definita nell'Attestation Rulebook applicabile
   * - Relying Party
     - sì, solo per RP che opera in EUDIW
     - sì, solo per RP che opera in EUDIW
     - il WRPAC se ha un record nel register, e l'Authentication Certificate ove la RP non ha un record nel register e opera nel Proximity Flow
     - Nessuna
   * - Relying Party Intermediary
     - sì
     - No
     - il WRPAC
     - Nessuna
   * - Wallet Provider
     - no
     - no
     - il Sign/Seal Certificate
     - Wallet Providers LoTE

.. note::
   La registrazione di federazione è comune a ogni entità e, come suo risultato, ogni entità ottiene un Subordinate Statement emesso dalla propria Federation Authority, e un Trust Mark di registrazione.

.. note::
   Per una Wallet-Relying Party che opera nel Trust Framework EUDIW, la colonna WRPAC è un certificato di accesso **per ciascun Service registrato** ([`EIDAS-ARF`_] Reg_10a, Reg_33, Reg_34), e per un Intermediario di Relying Party è un **insieme distinto di certificati di accesso per ciascuna Relying Party intermediata**, un WRPAC per ciascun Relying Party Service intermediato ([`EIDAS-ARF`_] Reg_34a). La colonna WRPRC è un certificato di registrazione **per ciascuna combinazione di intended use e Service** per le Relying Party e **per Service** per i PID e Attestation Provider, emesso automaticamente come definito in :ref:`onboarding-system:Wallet-Relying Party Registration Certificate Issuance`. La tabella precedente indica se il ruolo ottiene tali artifact, non la loro cardinalità.

.. note::
   Un'entità che opera solo a livello nazionale non ottiene né un record nel Register, né un WRPAC né un WRPRC.
   Detiene la propria Entity Statement e il proprio Trust Mark di registrazione dalla registrazione di federazione e, ove il proprio ruolo lo richieda, il proprio certificato X.509, ossia il Sign/Seal Certificate per un Credential Issuer nazionale o l'Authentication Certificate per una Relying Party che opera nel Proximity Flow.

Registration Profiles
^^^^^^^^^^^^^^^^^^^^^

Questa Sezione descrive la registrazione di ciascun ruolo come un profilo.
Ogni profilo fornisce i dati di registrazione di base definiti in :ref:`onboarding-system:Registration Data Model`, e ciascun profilo seguente indica solo i dati di registrazione estesi che il ruolo fornisce e come l'entità li popola, insieme a qualsiasi specializzazione dei dati di base.
Un'entità può detenere più di un entitlement in un unico record di registrazione e per più di un ruolo, quindi i profili non sono mutuamente esclusivi e si compongono.
Ad esempio, un'entità può essere contemporaneamente una Relying Party e un QEAA Provider, e in tal caso il suo input è l'unione dei due profili e il suo esito è l'unione dei due.

.. note::
   La definizione di un tipo di Credenziale non fa parte di alcun profilo di registrazione, come descritto in :ref:`onboarding-system:Registration Data Model`.
   È fornita dall'Attestation Scheme Provider, si veda :ref:`onboarding-system:System Actors and Roles`, tramite :ref:`onboarding-system:Credential Type Registration`.

PID Provider
""""""""""""

Un PID Provider è un'Entità di Federazione che è notificata e registrata nel Trust Framework EUDIW, e il suo trust anchor Sign/Seal è pubblicato nella PID Providers LoTE.
Oltre ai dati di registrazione di base, un PID Provider fornisce i seguenti dati di registrazione estesi, come definiti in :ref:`onboarding-system:Registration Data Model`:

- `entitlements`
- `service_description`
- `relying_party_services`

  - Almeno un Service, il cui ``serviceIdentifier`` è univoco all'interno del PID Provider. Il Service reca ``provided_attestations`` per il tipo PID.
- `provided_attestations`
- `federation_entity_identifier`
- `federation_entity_key`
- `certificate_signing_requests`

  - Una Certificate Signing Request per il WRPAC di ciascun Service registrato, con cui il PID Provider si autentica verso le Wallet Unit.
  - Una Certificate Signing Request per il Sign/Seal Certificate, con cui firma il PID emesso.
- `conformity_assessment`
- `service_supply_point`


QEAA Provider
"""""""""""""

Un QEAA Provider è un'Entità di Federazione che emette Qualified Electronic Attestations of Attributes, e il suo Sign/Seal Certificate è il certificato qualificato emesso dal Qualified Trust Service Provider a cui appartiene.
Oltre ai dati di registrazione di base, un QEAA Provider fornisce i seguenti dati di registrazione estesi, come definiti in :ref:`onboarding-system:Registration Data Model`:

- `entitlements`
- `service_description`
- `relying_party_services`

  - Almeno un Service, il cui ``serviceIdentifier`` è univoco all'interno del QEAA Provider. Il Service reca ``provided_attestations``.
- `provided_attestations`
- `federation_entity_identifier`
- `federation_entity_key`
- `certificate_signing_requests`

  - Una Certificate Signing Request per il WRPAC di ciascun Service registrato, con cui il QEAA Provider si autentica verso le Wallet Unit.
- `conformity_assessment`
- `service_supply_point`
- `signing_trust_anchor`

  - Fornito come input perché la Qualified Certification Authority del QEAA Provider non è subordinata alla National Root Certification Authority ma appartiene al perimetro di un Qualified Trust Service Provider.


PuB-EAA Provider
""""""""""""""""

Un PuB-EAA Provider è un'Entità di Federazione che è notificata e registrata nel Trust Framework EUDIW, e il suo trust anchor Sign/Seal è pubblicato nella PuB-EAA Providers LoTE.
Oltre ai dati di registrazione di base, un PuB-EAA Provider fornisce i seguenti dati di registrazione estesi, come definiti in :ref:`onboarding-system:Registration Data Model`:

- `entitlements`
- `service_description`
- `relying_party_services`

  - Almeno un Service, il cui ``serviceIdentifier`` è univoco all'interno del PuB-EAA Provider. Il Service reca ``provided_attestations``.
- `provided_attestations`
- `federation_entity_identifier`
- `federation_entity_key`
- `certificate_signing_requests`

  - Una Certificate Signing Request per il WRPAC di ciascun Service registrato, con cui il PuB-EAA Provider si autentica verso le Wallet Unit.
- `conformity_assessment`:

  - Il Conformity Assessment Report emesso da un Conformity Assessment Body ai sensi dell'Articolo 45f di [`EIDAS`_].
- `service_supply_point`
- `signing_trust_anchor`

  - Fornito come input perché la Qualified Certification Authority del PuB-EAA Provider non è subordinata alla National Root Certification Authority ma appartiene al perimetro di un Qualified Trust Service Provider.


Non-Qualified EAA Provider
""""""""""""""""""""""""""

Oltre ai dati di registrazione di base, un Non-Qualified EAA Provider fornisce i seguenti dati di registrazione estesi, come definiti in :ref:`onboarding-system:Registration Data Model`:

- `entitlements`
- `service_description`
- `relying_party_services`

  - OBBLIGATORIO ove il Non-Qualified EAA Provider operi nel Trust Framework EUDIW. Almeno un Service, il cui ``serviceIdentifier`` è univoco all'interno del Provider.
- `provided_attestations`
- `federation_entity_identifier`
- `federation_entity_key`
- `certificate_signing_requests`

  - Una Certificate Signing Request per il Sign/Seal Certificate, con cui il Non-Qualified EAA Provider firma l'EAA emessa.
  - Un Non-Qualified EAA Provider che opera nel Trust Framework EUDIW fornisce inoltre una Certificate Signing Request per il WRPAC di ciascun Service registrato, con cui si autentica verso le Wallet Unit.
- `service_supply_point`
- `trust_framework_scope`
  
  - Un Non-Qualified EAA Provider dichiara, in sede di onboarding, se opera nel Trust Framework EUDIW o solo all'interno del perimetro nazionale, e questa scelta incide sugli artifact che ottiene, come descritto in :ref:`infrastructure-trust:Infrastructure of Trust`. Un Non-Qualified EAA Provider che opera nel Trust Framework EUDIW ottiene il record nel Register, il WRPAC e il Sign/Seal Certificate, mentre un Non-Qualified EAA Provider che opera solo all'interno del perimetro nazionale ottiene il solo Sign/Seal Certificate, è autenticato dalla Wallet Unit tramite il National Trust Framework, e i suoi Attestati sono validati rispetto al trust anchor distribuito dall'Entity Configuration del Federation TA. L'IT-Wallet ID, l'Attestato Elettronico di Dati di Identificazione Personale di ambito nazionale, è un esempio di Attestato emesso da un Non-Qualified EAA Provider che opera all'interno del perimetro nazionale, si veda :ref:`credential-data-model-it-wallet-id:Modello di Dati dell'IT-Wallet ID` e :term:`IT-Wallet ID`. È un EAA e NON DEVE essere confuso con i Person Identification Data EUDI, che non sono un EAA.


Relying Party
"""""""""""""

Oltre ai dati di registrazione di base, una Relying Party fornisce i seguenti dati di registrazione estesi, come definiti in :ref:`onboarding-system:Registration Data Model`:

- `entitlements`
- `service_description`
- `relying_party_services`

  - OBBLIGATORIO ove la Relying Party operi nel Trust Framework EUDIW. Almeno un Service. Ciascun Service reca i propri valori ``intended_use`` (Reg_10d).
- `intended_use`:

  - Annidato in `relying_party_services`. Il tipo di Attestato e opzionalmente gli attributi che la Relying Party intende richiedere dalle Wallet Unit, con una definizione di intended use per ciascuna combinazione di Service registrata ai sensi di Reg_10d.
- `intermediary_relationship`

  - Annidato in `relying_party_services`. Nel Trust Framework EUDIW, OBBLIGATORIO ove il Relying Party Service operi tramite un RP Intermediary, e in tal caso fa riferimento all'identificativo dell'Intermediary Service (``usesIntermediaries``). Nel National Trust Framework la Relying Party non lo dichiara, perché la relazione con l'RP Intermediary è istituita tramite la federazione, in quanto la Relying Party imposta i propri ``authority_hints`` sull'RP Intermediary che la federa. Il lato dell'RP Intermediary è descritto in :ref:`onboarding-system:Relying Party Intermediary`.
- `federation_entity_identifier`
- `federation_entity_key`:

  - OBBLIGATORIO per una Relying Party che opera senza intermediario. Una Relying Party che opera tramite un RP Intermediary NON DEVE fornirlo, perché è registrata dal proprio RP Intermediary secondo il National Trust Framework.
- `certificate_signing_requests`

  - Una Certificate Signing Request per ciascun certificato X.509 di cui la Relying Party ha bisogno, ossia un WRPAC per ciascun Service registrato quando opera nel Trust Framework EUDIW, e il National Authentication Certificate quando opera solo nel National Trust Framework e supporta il Proximity Flow.
- `trust_framework_scope`

  - La Relying Party dichiara il Trust Framework in cui opera, come specificato in :ref:`infrastructure-trust:Infrastructure of Trust` e :ref:`trust-evaluation:Selection at Presentation`. Questa scelta incide sugli artifact che ottiene.

.. note::
   Una Relying Party (intermediata o meno) DEVE registrarsi tramite il Sistema di Onboarding per ottenere un Trust Mark di registrazione (si veda :ref:`infrastructure-trust:Trust Mark registration-entity`) e, nel caso di una Mobile Relying Party Instance, per ottenere un Authentication X.509 Certificate. 
   Una Relying Party che opera nel Trust Framework EUDIW DEVE avere un record nel Register of WRP, DEVE ottenere il proprio WRPAC e DEVE ricevere i propri WRPRC automaticamente, come specificato in :ref:`onboarding-system:Wallet-Relying Party Registration Certificate Issuance`.

Relying Party Intermediary
""""""""""""""""""""""""""

Un Intermediario di Relying Party dichiara di agire come intermediario sia nel National Trust Framework sia nel Trust Framework EUDIW.
Nel National Trust Framework l'Intermediario di Relying Party è un Federation Intermediate, ossia effettua l'onboarding delle Relying Party intermediate in autonomia, pubblicandone i Subordinate Statement, come descritto in :ref:`infrastructure-trust:Trust Mark registration-entity`.
Nel Trust Framework EUDIW è registrato con ``isIntermediary`` impostato, e federa le proprie Relying Party intermediate che operano in ambito transfrontaliero.
Fornisce gli stessi Data Identifier di una :ref:`onboarding-system:Relying Party`, con le differenze nella tabella seguente.
I Data Identifier non elencati qui sono forniti come per una Relying Party.

.. list-table:: Relying Party Intermediary Registration Data, differences from the Relying Party
   :class: longtable
   :widths: 34 66
   :header-rows: 1

   * - **Data Identifier**
     - **Value**
   * - `intended_use`
     - NON DEVE essere fornito. Un Intermediario di Relying Party non richiede attributi per sé, ma per conto delle Relying Party intermediate. Nel Register, ciascuno dei suoi elementi ``services[]`` ha ``isIntermediary`` impostato a ``true``, omette ``intendedUses`` e elenca in ``servedWRPServices`` gli identificativi di Service che serve ([`CIR2026/1730`_], Annex I).
   * - `entitlements`
     - NON DEVE essere fornito per un Intermediary Service puro (`EUDI-TS 5`_ v1.5).
   * - `relying_party_services`
     - OBBLIGATORIO. Almeno un Service. Ciascun Service è un Intermediary Service: ``isIntermediary`` è ``true``, ``serviceIdentifier`` è registrato e ``servedWRPServices`` elenca gli identificativi dei Relying Party Service intermediato.
   * - `certificate_signing_requests`
     - Una Certificate Signing Request per il WRPAC per ciascun Relying Party Service intermediato che l'Intermediario serve ([`EIDAS-ARF`_] Reg_34a). Ciascun WRPAC emesso autentica l'Intermediario e reca l'associazione a quella Relying Party intermediata e a quel Service.
   * - `intermediary_relationship`
     - Impostato sull'Intermediary Service, ossia la Relying Party dichiara che il Service è un intermediario designato. È dichiarato in entrambi i framework.
   * - `federation_entity_identifier`
     - Il Federation Entity Identifier dell'Intermediario di Relying Party all'interno del National Trust Framework.
   * - `federation_entity_key`
     - La Federation Entity Key dell'Intermediario di Relying Party.

.. note::
  La registrazione di un Intermediario di Relying Party e la registrazione delle sue Relying Party intermediate sono collegate, l'Intermediario dichiara di agire come intermediario e ciascuna Relying Party intermediata lo referenzia nel proprio profilo :ref:`onboarding-system:Relying Party`.


Wallet Provider
"""""""""""""""

Un Fornitore di Wallet è un'Entità di Federazione che è notificata, ma non è registrata nel Register, perché non agisce come Wallet-Relying Party.
I suoi dati di registrazione fanno parte del dataset di notifica, e il suo trust anchor Sign/Seal è pubblicato nella Wallet Providers LoTE.
Oltre ai dati di registrazione di base, un Fornitore di Wallet fornisce i seguenti dati di registrazione estesi, come definiti in :ref:`onboarding-system:Registration Data Model`:

- `entitlements`
- `service_description`
- `federation_entity_identifier`
- `federation_entity_key`
- `certificate_signing_requests`

  - Una Certificate Signing Request per il Sign/Seal Certificate, con cui il Fornitore di Wallet firma le Wallet Unit Attestation.
- `conformity_assessment`


Authentic Source
""""""""""""""""

Una Fonte Autentica è al di fuori dei Trust Framework EUDIW e Nazionale, e la sua trust è governata dal framework PDND.
Non è registrata nel Register e non è un'Entità di Federazione, quindi non fornisce i dati di federazione e non ottiene alcun Trust Artifact.
I suoi dati di registrazione sono la voce dell'AS Registry.
Oltre ai dati di registrazione di base, una Fonte Autentica fornisce i seguenti dati di registrazione estesi, come definiti in :ref:`onboarding-system:Registration Data Model`:

- `provided_claims_purposes`
- `visual_identity`
- `verification_endpoint`

  - Fornito solo ove la Fonte Autentica sia responsabile di un attributo esportato nel EUDIW Catalogue of Attributes, in modo che un Qualified Trust Service Provider di un altro Stato membro possa raggiungere la sua interfaccia di verifica.

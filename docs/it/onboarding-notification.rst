.. include:: ../common/common_definitions.rst
.. Included via onboarding-system.rst at title level '-' (level 1).

Notification and Publication
----------------------------

Questa Sezione descrive la notifica alla Commissione Europea delle entità che ne sono soggette, e la conseguente pubblicazione nelle Lists of Trusted Entities. La presentazione è un atto dello Stato membro (tramite il Single Point Of Contact) e la pubblicazione è un atto della Commissione Europea, quindi la notifica non è uno dei :ref:`onboarding-system:Onboarding Processes`. Il Sistema di Onboarding gestisce solo la raccolta e il mantenimento delle informazioni notificabili.

All'interno di IT-Wallet l'Organismo di Supervisione è il National Single Point Of Contact con la Commissione e si avvale del Registrar per le entità che il Registrar registra.
Il suo esito è l'inclusione dell'entità nella List of Trusted Entities del proprio tipo, la cui struttura e firma sono descritte in :ref:`infrastructure-trust:Trusted List, Lists of Trusted Lists, and Lists of Trusted Entities`.

Le categorie soggette a notifica secondo gli Articoli 4 e 5 di [`CIR2024/2980`_], adottato ai sensi dell'Articolo 5a(23) di [`EIDAS`_], sono le seguenti:

- Fornitori di Wallet;
- PID Provider;
- Provider of WRPAC;
- Provider of WRPRC, ove applicabile;
- Registrar delle Wallet-Relying Party, insieme ai registri.

I PuB-EAA Provider sono notificati ai sensi dell'Articolo 45f(3) di [`EIDAS`_], e le regole di dettaglio sono stabilite in [`CIR2025/1569`_].
Le Wallet-Relying Party che non appartengono a una categoria notificata non sono notificate individualmente, e sono rese disponibili tramite il loro registro.


**Input**

L'input è costituito dalle informazioni notificabili dell'entità, ossia il sottoinsieme dei suoi dati di registrazione che si applica alla categoria, definito dall'Annex II di [`CIR2024/2980`_] e, per i PuB-EAA Provider, dall'Annex III di [`CIR2025/1569`_].
Le informazioni sono una proiezione del :ref:`onboarding-system:Registration Data Model`:

- ``legal_name``
- ``identifier``
- ``contact_information``
- ``service_policies``
- ``signing_trust_anchor``
- ``conformity_assessment``

Per un PID Provider e un Fornitore di Wallet il Sign/Seal Certificate è emesso dalla PKI nazionale, quindi il ``signing_trust_anchor`` non è fornito come input dall'entità ma deriva dall'emissione descritta in :ref:`onboarding-system:Signature and Seal Certificate Issuance`.

Per un PuB-EAA Provider il Sign/Seal Certificate è un certificato qualificato emesso da un Qualified Trust Service Provider, e il suo Trust Anchor è veicolato dalle eIDAS Trusted Lists che sono al di fuori di questo processo.
Pertanto, il Sign/Seal Trust Anchor non è richiesto come input per un PuB-EAA Provider, e lo status qualificato del suo certificato è valutato nella valutazione di conformità richiesta per l'eleggibilità e la conformità, si veda :ref:`onboarding-system:Eligibility and Compliance Preconditions`.

Le informazioni notificabili sono raccolte nel dataset di notifica, che è mantenuto distinto dal Register come descritto in :ref:`onboarding-system:Trust Artifacts Registration Outcomes`.
Il dataset è scritto e mantenuto aggiornato dal Notification Dataset Management durante :ref:`onboarding-system:Entity Registration`, :ref:`onboarding-system:Entity Update` e :ref:`onboarding-system:Entity Suspension and Removal`.

.. note::
   Il Sign/Seal Trust Anchor non è il certificato che l'entità utilizza per firmare, la cui chiave pubblica è veicolata dalle ``certificate_signing_requests``.

**Outcome**

L'esito è l'inclusione dell'entità nella List of Trusted Entities del proprio tipo.
L'inclusione è l'asserzione, a livello UE, del ruolo e dell'autorizzazione dell'entità, ed è ciò che consente a una Wallet Unit o a una Wallet-Relying Party di un altro Stato membro di validare l'entità.

**Process**

1. L'entità DEVE aver completato la propria :ref:`onboarding-system:Entity Registration`, e per le categorie notificate la valutazione di conformità DEVE essere stata verificata come descritto in :ref:`onboarding-system:Eligibility and Compliance Preconditions`.
   Il completamento della registrazione è la precondizione della notifica.
2. Il Sistema di Onboarding raccoglie le informazioni notificabili della categoria dal dataset di notifica, seguendo l'Annex II di [`CIR2024/2980`_] o, per i PuB-EAA Provider, l'Annex III di [`CIR2025/1569`_].
3. L'Organismo di Supervisione, in qualità di National Single Point Of Contact, presenta le informazioni al sistema elettronico sicuro di notifica che la Commissione mette a disposizione. La presentazione DEVE essere effettuata almeno in inglese.
   Il sistema e i suoi requisiti sono definiti nell'Annex I di [`CIR2024/2980`_].
4. La Commissione PUÒ richiedere informazioni aggiuntive o chiarimenti per verificare la completezza e la coerenza delle informazioni notificate.
5. La Commissione pubblica la List of Trusted Entities che compila le informazioni notificate.
   L'entità compare nella List of Trusted Entities del proprio tipo, il cui data model, formato e firma sono descritti in :ref:`infrastructure-trust:Trusted List, Lists of Trusted Lists, and Lists of Trusted Entities`.
6. Ove la registrazione dell'entità cambi, in particolare ove sia sospesa o cancellata, il Sistema di Onboarding DEVE riflettere la modifica nel dataset di notifica.

.. note::
   Le Lists of Trusted Entities definite da [`CIR2024/2980`_] e le Trusted Lists definite da [`CID2015/1505`_] sono descritte in :ref:`infrastructure-trust:Trusted List, Lists of Trusted Lists, and Lists of Trusted Entities`.

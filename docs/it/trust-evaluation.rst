.. include:: ../common/common_definitions.rst
.. include:: ../common/symbols.rst
.. Included via index.rst at title level '=' (document title).

Trust Evaluation Process
========================

Ogni processo di trust evaluation coinvolge i seguenti ruoli:

- Il **Trust Evaluator** è la parte che esegue la valutazione.
- La **Trust Evaluated Party** è l'entità, o l'attestazione, che è oggetto della valutazione.

La stessa entità può agire in entrambi i ruoli in momenti diversi dei flussi.
Le sezioni specifiche di ciascun framework definiscono quale entità agisce in quale ruolo, quando e per quale scopo.

Ciascun processo richiede come precondizione una radice di fiducia validata.
Ciascun Trust Framework definisce come la propria radice di fiducia è istituita, distribuita e mantenuta.
Nel Trust Framework Nazionale questa è il Federation Trust Anchor (vedere :ref:`trust-evaluation:Federation Trust Anchor Distribution and Validation`).
Nel Trust Framework EUDIW queste sono i Trust Anchor ottenuti dalle Trusted List e dalle List of Trusted Entities applicabili (vedere :ref:`trust-evaluation:List of Trusted Entities Validation`).

I processi di trust evaluation sono i seguenti:

  - **Authentication**.
    Attesta l'identità crittografica di un'entità che partecipa alla transazione.
    Il Trust Evaluator vincola l'identificatore della Trust Evaluated Party alla prova di possesso di una chiave privata la cui parte pubblica è fidata rispetto alla radice di fiducia applicabile.
  - **Authorization**.
    Valuta un artifact di registrazione per attestare gli entitlement della Trust Evaluated Party, ossia le capacità specifiche che l'entità è autorizzata a eseguire, quali l'emissione di un dato tipo di Attestato o la richiesta di un dato insieme di attributi.
  - **Metadata Retrieval and Validation**.
    Ottiene e valida la configurazione tecnica della Trust Evaluated Party, quali endpoint, chiavi pubbliche e algoritmi supportati.
  - **Signing Trust Anchor Validation**.
    Prende in ingresso un'attestazione e produce la radice di fiducia validata, l'identificatore e la chiave pubblica, da utilizzare per la verifica della issuer data authentication di tale attestazione.

I primi tre processi hanno come oggetto un'entità.
Il quarto ha come oggetto un'attestazione e questo include gli Attestati Elettronici e la Wallet Instance Attestation.

Trust Framework Selection
------------------------------------

Questa sezione descrive le regole di selezione del Trust Framework applicabili ai flussi operativi delle Entità coinvolte.
I due Trust Framework e la policy che li seleziona sono definiti in :ref:`infrastructure-trust:Infrastructure of Trust`.
Una valutazione EUDIW fallita NON DEVE essere ritentata nell'ambito del Trust Framework Nazionale, come specificato in :ref:`trust-evaluation:Failure Handling`.

Per la Signing Trust Anchor Validation non vi è alcuna selezione da eseguire: il trust anchor per la verifica di un'attestazione è definito dal Rulebook del relativo tipo di Attestato, in ogni fase e qualunque sia la parte che esegue la verifica.
Le attestazioni il cui Rulebook le ancora a una List of Trusted Entities o a una Trusted List, quali i PID, le QEAA e le PuB-EAA, DEVONO essere validate rispetto a tali trust anchor anche quando l'interazione segue il Trust Framework Nazionale (vedere OIA_12, OIA_13, OIA_14 e OIA_15 dell'ARF Annex 2, `EIDAS-ARF`_).
Ad esempio, una Relying Party che ottiene un PID da una Wallet Unit nazionale DEVE validarlo rispetto ai trust anchor pubblicati nella PID Providers List of Trusted Entities.

La procedura per gli Attestati ancorati al Trust Framework Nazionale è definita in :ref:`trust-evaluation:Signing Trust Anchor Validation Procedure` (vedere anche :ref:`onboarding-system:Onboarding System and Lifecycle Management`).

La tabella seguente fornisce una vista di alto livello su quale Trust Framework si applica a ciascuna entità nelle fasi operative.
In particolare, ciascuna cella indica il framework applicabile e il criterio di selezione, e rinvia alla sezione in cui sono definite le procedure corrispondenti.
Una vista più dettagliata di quali procedure ciascuna entità implementa, e in quale ruolo, è fornita nella tabella di ciascuna sezione di framework (vedere :ref:`trust-evaluation:Trust Evaluation Processes by Context` per il Trust Framework Nazionale e la corrispondente sezione di dettaglio del Trust Framework EUDIW).
I percorsi di onboarding e gli artifact ottenuti da ciascun tipo di entità sono definiti in :ref:`onboarding-system:Onboarding Processes`.

La Signing Trust Anchor Validation non è inclusa nella tabella seguente poiché, come indicato sopra, non dipende dall'entità né dal framework selezionato.

.. _table_applicable_tf_by_entity:
.. list-table:: Trust Framework applicabile per Entità e Fase
    :class: longtable
    :widths: 16 42 42
    :header-rows: 1

    * - **Entità**
      - **Emissione**
      - **Presentazione**
    * - Wallet Provider
      - Non applicabile come parte dell'interazione.
        Il Fornitore di Wallet è valutato indirettamente, come emittente della Wallet Instance Attestation, attraverso il framework selezionato dalla controparte.
      - Non applicabile come parte dell'interazione.
    * - Wallet Unit
      - Agisce come Trust Evaluator nei confronti del Credential Issuer e, al tempo stesso, come Trust Evaluated Party nei suoi confronti, poiché il Credential Issuer valida la sua Wallet Instance Attestation.
        La selezione del Trust Framework è definita in :ref:`trust-evaluation:Selection at Issuance`.
      - Agisce come Trust Evaluator nei confronti della Relying Party.
        DEVE supportare sia il Trust Framework EUDIW sia quello Nazionale.
        Nel flusso remoto il framework segue il prefisso ``client_id`` dichiarato dalla Relying Party.
        Nel flusso di prossimità entrambi i framework utilizzano la mdoc reader authentication e il framework è determinato dal trust anchor che valida il certificato del reader (vedere :ref:`trust-evaluation:Selection at Presentation`).
    * - Credential Issuer
      - Agisce come Trust Evaluator nei confronti della Wallet Unit e, al tempo stesso, come Trust Evaluated Party nei suoi confronti, poiché la Wallet Unit valida la sua Authentication, Authorization e Metadata.
        La selezione del Trust Framework è definita in :ref:`trust-evaluation:Selection at Issuance`.
      - Non applicabile.
    * - Relying Party
      - Non applicabile.
      - Agisce come Trust Evaluated Party nei confronti della Wallet Unit.
        La selezione del Trust Framework, incluso il prefisso ``client_id``, è definita in :ref:`trust-evaluation:Selection at Presentation`.

.. note::
  In caso di divergenza tecnica tra la configurazione pubblicata attraverso i meccanismi EUDIW e la configurazione pubblicata attraverso la federazione, ad esempio certificati diversi per la stessa entità in una List of Trusted Entities e nella Trust Anchor Entity Configuration, la configurazione EUDIW DEVE prevalere.

Selection at Issuance
^^^^^^^^^^^^^^^^^^^^^

All'emissione la Wallet Unit avvia l'interazione e conosce l'Attestato richiesto.
La selezione è determinata dal fatto che il Credential Issuer sia un'entità nazionale oppure di un altro Stato membro, insieme al catalogo dell'Attestato richiesto (vedere :ref:`registry:Digital Credentials Catalog`).

Per Authentication, Authorization e Metadata Retrieval and Validation del Credential Issuer, la Wallet Unit DEVE applicare le procedure EUDIW quando il Credential Issuer, o il PID, la (Q)EAA o la PuB-EAA richiesti, è di un altro Stato membro.
La Wallet Unit DOVREBBE applicare le procedure del Trust Framework Nazionale quando il Credential Issuer è un'entità nazionale.
Il Trust Framework Nazionale NON DEVE essere selezionato per l'emissione di un PID, di una (Q)EAA o di una PuB-EAA di un altro Stato membro.
Questa regola DEVE essere applicata anche agli EAA Provider; pertanto, lo stesso Credential Issuer PUÒ essere valutato nell'ambito di framework diversi in interazioni diverse, in funzione della controparte e dell'Attestato richiesto.
Gli header degli artifact firmati del Credential Issuer riflettono la stessa selezione: un header ``x5c`` che reca il certificato di accesso per il percorso EUDIW, e un header ``kid``, con l'header ``trust_chain`` opzionale, per il percorso del Trust Framework Nazionale.
Tali header DEVONO essere coerenti con il framework selezionato.

Per la validazione della Wallet Unit, il Credential Issuer DEVE validare la Wallet Instance Attestation attraverso la Wallet Providers List of Trusted Entities quando la Wallet Unit è di un altro Stato membro.
Un Credential Issuer DOVREBBE validare la Wallet Instance Attestation attraverso il Trust Framework Nazionale quando la Wallet Unit è nazionale (vedere :ref:`trust-evaluation:Wallet Unit Authentication`).

Selection at Presentation
^^^^^^^^^^^^^^^^^^^^^^^^^

Nel flusso remoto la selezione è dichiarata dalla Relying Party attraverso il prefisso ``client_id`` della richiesta (vedere `OpenID4VP`_, Section 5.9).

La Relying Party non autentica la Wallet Unit e pertanto non può selezionare il Trust Framework in funzione dello Stato membro di quella Wallet Unit o Soluzione Wallet.

Una Relying Party nazionale che offre servizi di interoperabilità al di fuori del pubblico nazionale DEVE utilizzare il Client Identifier Prefix ``x509_hash`` e gli artifact EUDIW, come richiesto da [`ETSI TS 119 472-2`_] (OIDFVP-HAIP_COMMON_GEN_REQ-02).
Una Relying Party nazionale che non offre tali servizi interoperabili e si rivolge esclusivamente a un pubblico nazionale DOVREBBE utilizzare il prefisso ``openid_federation`` con gli artifact di federazione, anche quando richiede un PID, una (Q)EAA o una PuB-EAA.

La Wallet Unit DEVE supportare entrambi i prefissi.
DEVE processare una richiesta con il prefisso ``x509_hash`` nell'ambito delle procedure EUDIW (vedere :ref:`trust-evaluation:EUDIW Authentication`).
DEVE processare una richiesta con il prefisso ``openid_federation`` nell'ambito delle procedure del Trust Framework Nazionale (vedere :ref:`trust-evaluation:Trust Evaluation Processes by Context`) quando la Trust Chain della Relying Party è valida rispetto al National Trust Anchor.
Se la richiesta utilizza il prefisso ``openid_federation`` e la Trust Chain non può essere validata rispetto al National Trust Anchor, la Wallet Unit DEVE trattare la Relying Party come non affidabile e NON DEVE valutare la richiesta nell'ambito del Trust Framework Nazionale.
I processi di Authentication, Authorization e Metadata Retrieval and Validation sono eseguiti nell'ambito del framework selezionato.

Nel flusso di prossimità entrambi i Trust Framework utilizzano la mdoc reader authentication definita in [`ISO18013-5`_ #12.5], basata su un certificato X.509 fornito dall'Istanza della Relying Party nell'header ``x5chain`` del ``ReaderAuth``.

Nell'ambito del Trust Framework EUDIW il certificato è il certificato di accesso, come profilato nella Section 5.3 di [`ETSI TS 119 472-2`_] (vedere :ref:`proximity-flow:Richiesta mdoc`), ed è validato rispetto alla Provider of Wallet-Relying Party Access Certificate List of Trusted Entities.

Nell'ambito del Trust Framework Nazionale il certificato è il certificato di autenticazione della Relying Party ed è validato rispetto a un Authentication Trust Anchor pubblicato nella Federation Trust Anchor Entity Configuration (vedere :ref:`trust-evaluation:Relying Party Proximity Authentication`).

Un meccanismo di selezione equivalente al prefisso ``client_id`` non è definito in [`ISO18013-5`_].

Nell'IT-Wallet il framework applicabile è determinato dal trust anchor che valida il certification path del certificato del reader.
La richiesta è processata nell'ambito del Trust Framework EUDIW quando il path termina in un trust anchor della Provider of Wallet-Relying Party Access Certificate List of Trusted Entities, e nell'ambito del Trust Framework Nazionale quando termina in un Authentication Trust Anchor della federazione.
La Relying Party applica la stessa policy di audience del flusso remoto, utilizzando il certificato corrispondente al posto del prefisso ``client_id``.
La Wallet Unit DEVE determinare il framework applicabile prima del processo di Authorization e DEVE eseguire l'Authorization esclusivamente nell'ambito di tale framework.

Failure Handling
^^^^^^^^^^^^^^^^

Il fallimento della trust evaluation nell'ambito del framework selezionato NON DEVE essere valutato nuovamente nell'ambito dell'altro framework.
In particolare, una valutazione EUDIW fallita NON DEVE essere ritentata come valutazione del Trust Framework Nazionale.

Se l'Authentication fallisce, la Wallet Unit DEVE informare l'Utente che l'identità della Wallet-Relying Party non ha potuto essere verificata e DEVE interrompere l'interazione ([`EIDAS-ARF`_] CT_06, RPA_06a).
Lo stesso vale nell'ambito del Trust Framework Nazionale: un esito ``NON_AUTHENTICATED`` DEVE interrompere l'interazione.

Se l'Authentication ha successo e l'Authorization fallisce, la Wallet Unit DEVE applicare :ref:`trust-evaluation:Authorization Decision and Override Rules`.
Durante la presentazione, una scelta dell'Utente di proseguire è consentita solo per gli esiti di Authorization overridable ivi definiti.
Il fallimento dell'Authentication non è overridable.

Durante l'Emissione, quando l'Authentication o l'Authorization non ha successo, la Wallet Unit DEVE mostrare un avviso all'Utente e NON DEVE richiedere l'emissione ([`EIDAS-ARF`_] RPRC_22a).
All'emissione non è offerta alcuna scelta all'Utente.

.. include:: trust-evaluation-eudiw.rst
.. include:: trust-evaluation-oidfed.rst
.. include:: trust-override-rules.rst

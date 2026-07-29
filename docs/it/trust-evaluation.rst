.. include:: ../common/common_definitions.rst
.. include:: ../common/symbols.rst
.. Included via index.rst at title level '=' (document title).

Trust Evaluation Process
========================

Ogni processo di trust evaluation coinvolge i seguenti ruoli:

- Il **Trust Evaluator** è la parte che esegue la valutazione.
- Il **Trust Evaluated Party** è l'entità, o l'attestazione, oggetto della valutazione.

La stessa entità può agire in entrambi i ruoli in momenti diversi dei flussi.
Le sezioni specifiche del framework definiscono quale entità agisce in quale ruolo, quando e per quale scopo.

Ogni processo richiede una root of trust convalidata come precondizione.
Ogni trust framework definisce come la propria root of trust viene stabilita, distribuita e mantenuta.
Nel Trust Framework Nazionale questa è la Federation Trust Anchor (vedi :ref:`trust-evaluation:Federation Trust Anchor Distribution and Validation`).
Nel Trust Framework EUDIW queste sono le Trust Anchor ottenute dalle Trusted List e dalle List of Trusted Entities applicabili (vedi :ref:`trust-evaluation:List of Trusted Entities Validation`).

I processi di trust evaluation sono i seguenti:

  - **Authentication**.
    Asserisce l'identità crittografica di un'entità transazionante.
    Il Trust Evaluator associa l'identificatore del Trust Evaluated Party alla prova di possesso di una chiave privata la cui parte pubblica è considerata affidabile sotto la root of trust applicabile.
  - **Authorization**.
    Valuta un artifact di registrazione per asserire gli entitlements del Trust Evaluated Party, cioè le capacità specifiche che l'entità è autorizzata a svolgere, come l'emissione di un dato tipo di Credenziale o la richiesta di un dato insieme di attributi.
  - **Metadata Retrieval and Validation**.
    Ottiene e convalida la configurazione tecnica del Trust Evaluated Party, come endpoint, chiavi pubbliche e algoritmi supportati.
  - **Signing Trust Anchor Validation**.
    Acquisisce un'attestazione e produce la root of trust convalidata, l'identificatore e la chiave pubblica, da utilizzare per la verifica dell'autenticazione dei dati dell'emittente di quella attestazione.

I primi tre processi hanno un'entità come oggetto.
Il quarto ha un'attestazione come oggetto e ciò include le Digital Credentials e la Wallet Instance Attestation.

Trust Framework Selection
------------------------------------

Questa sezione descrive le regole di selezione del Trust Framework applicabili ai flussi operativi delle Entità coinvolte.

Per la Signing Trust Anchor Validation non è prevista alcuna selezione: la trust anchor per la verifica di un'attestazione è definita dal Rulebook del relativo tipo di Credenziale, in ogni fase e indipendentemente dalla parte che esegue la verifica.
Le attestazioni il cui Rulebook le ancora a una List of Trusted Entities o a una Trusted List, come PID, QEAAs e PuB-EAAs, DEVONO essere convalidate rispetto a quelle trust anchor anche quando l'interazione segue il Trust Framework Nazionale (vedi OIA_12, OIA_13, OIA_14 e OIA_15 dell'ARF Annex 2, `EIDAS-ARF`_).
Per esempio, un Relying Party che ottiene un PID da una Wallet Unit nazionale DEVE convalidarlo rispetto alle trust anchor pubblicate nella PID Providers List of Trusted Entities.

La procedura per le Credenziali ancorate al Trust Framework Nazionale è definita in :ref:`trust-evaluation:Signing Trust Anchor Validation Procedure` (vedi anche :ref:`onboarding-system:Onboarding System and Lifecycle Management`).

La tabella seguente fornisce una visione di alto livello del trust framework applicabile a ciascuna entità nelle fasi operative.
In particolare, ogni cella indica il framework applicabile e il criterio di selezione, e rimanda alla sezione in cui sono definite le procedure corrispondenti.
Una visione più dettagliata delle procedure implementate da ciascuna entità, e in quale ruolo, è fornita nella tabella di ciascuna sezione del framework (vedi :ref:`trust-evaluation:Trust Evaluation Processes by Context` per il Trust Framework Nazionale e la corrispondente sezione di dettaglio del Trust Framework EUDIW).
I percorsi di onboarding e gli artifact ottenuti da ciascun tipo di entità sono definiti in :ref:`onboarding-system:Onboarding Processes`.

La Signing Trust Anchor Validation non è inclusa nella tabella seguente, poiché, come indicato sopra, non dipende dall'entità né dal framework selezionato.

.. _table_applicable_tf_by_entity:
.. list-table:: Applicable Trust Framework by Entity and Phase
    :class: longtable
    :widths: 16 42 42
    :header-rows: 1

    * - **Entity**
      - **Issuance**
      - **Presentation**
    * - Wallet Provider
      - Non applicabile come parte transazionante.
        Il Wallet Provider è valutato indirettamente, in qualità di emittente della Wallet Instance Attestation, attraverso il framework selezionato dalla controparte.
      - Non applicabile come parte transazionante.
    * - Wallet Unit
      - Agisce come Trust Evaluator verso il Credential Issuer e, contemporaneamente, come Trust Evaluated Party verso di esso, poiché il Credential Issuer convalida la sua Wallet Instance Attestation.
        In qualità di Trust Evaluator DEVE supportare sia EUDIW sia il Trust Framework Nazionale a seconda che la Credenziale richiesta sia nel catalogo UE o solo nel catalogo nazionale (vedi :ref:`trust-evaluation:Selection at Issuance`).
      - Agisce come Trust Evaluator verso il Relying Party.
        DEVE supportare sia EUDIW sia il Trust Framework Nazionale.
        Nel remote flow il framework segue il prefisso ``client_id`` dichiarato dal Relying Party, mentre nel proximity flow entrambi i framework utilizzano l'mdoc reader authentication e il framework è determinato dalla trust anchor che convalida il certificato del reader (vedi :ref:`trust-evaluation:Selection at Presentation`).
    * - Credential Issuer
      - Agisce come Trust Evaluator verso la Wallet Unit e, contemporaneamente, come Trust Evaluated Party verso di essa, poiché la Wallet Unit convalida la sua Authentication, Authorization e Metadata.
        In qualità di Trust Evaluator DEVE supportare EUDIW quando la Credenziale in emissione è nel catalogo UE, oppure solo il Trust Framework Nazionale quando la Credenziale non è nel catalogo UE (vedi :ref:`trust-evaluation:Selection at Issuance`).
      - Non applicabile.
    * - Relying Party
      - Non applicabile.
      - Agisce come Trust Evaluated Party verso la Wallet Unit.
        DEVE supportare il Trust Framework EUDIW, con il prefisso ``x509_hash``, quando eroga servizi transfrontalieri, e il Trust Framework Nazionale, con il prefisso ``openid_federation``, quando non eroga servizi transfrontalieri e interagisce con una Wallet Unit nazionale (vedi :ref:`trust-evaluation:Selection at Presentation`).

.. note::
  In caso di divergenza tecnica tra la configurazione pubblicata tramite i meccanismi EUDIW e la configurazione pubblicata tramite la federazione, per esempio certificati diversi per la stessa entità in una List of Trusted Entities e nella Federation Trust Anchor Entity Configuration, la configurazione EUDIW DEVE prevalere.

Selection at Issuance
^^^^^^^^^^^^^^^^^^^^^

In emissione la Wallet Unit avvia l'interazione e conosce la Credenziale richiesta.
La selezione è guidata dal catalogo della Credenziale richiesta (vedi :ref:`registry:Catalogo degli Attestati Elettronici`).

Per Authentication, Authorization e Metadata Retrieval and Validation del Credential Issuer, la Wallet Unit DEVE applicare le procedure EUDIW quando la Credenziale richiesta è presente nel catalogo UE, e le procedure del Trust Framework Nazionale quando la Credenziale è presente solo nel catalogo nazionale.
Questa regola DEVE essere applicata anche agli EAA Provider; pertanto, lo stesso Credential Issuer PUÒ essere valutato sotto framework diversi in interazioni diverse, in base alla Credenziale richiesta.
Gli header degli artifact firmati del Credential Issuer riflettono la stessa selezione: un header ``x5c`` che trasporta l'access certificate per il percorso EUDIW, e un header ``kid``, con l'header opzionale ``trust_chain``, per il percorso del Trust Framework Nazionale.
Questi header DEVONO essere coerenti con il framework selezionato dal catalogo.

Per la validazione della Wallet Unit, il Credential Issuer DEVE convalidare la Wallet Instance Attestation tramite la Wallet Providers List of Trusted Entities quando la Credenziale in emissione è presente nel catalogo UE.
Un Credential Issuer PUÒ convalidare la Wallet Instance Attestation tramite il Trust Framework Nazionale solo quando la Credenziale in emissione non è presente nel catalogo UE (vedi :ref:`trust-evaluation:Wallet Unit Authentication`).

Selection at Presentation
^^^^^^^^^^^^^^^^^^^^^^^^^

Nel remote flow la selezione è dichiarata dal Relying Party tramite il prefisso ``client_id`` della richiesta (vedi `OpenID4VP`_, Section 5.9).

Un Relying Party che intende erogare servizi online transfrontalieri agli utenti opera sotto il profilo EUDIW e DEVE utilizzare il Client Identifier Prefix ``x509_hash`` e gli artifact EUDIW, come richiesto da [`ETSI TS 119 472-2`_] (OIDFVP-HAIP_COMMON_GEN_REQ-02).
Un Relying Party che non eroga servizi transfrontalieri e sa, tramite il meccanismo di wallet discovery dell'ecosistema (vedi :ref:`wallet-metadata-retrieval:Flusso di Recupero dei Wallet Metadata` e la Selection Page in :ref:`functionalities:Design dell'Esperienza Utente`), di interagire con una Wallet Unit nazionale, DEVE utilizzare il prefisso ``openid_federation`` con gli artifact della federazione.

La Wallet Unit DEVE supportare entrambi i prefissi e DEVE elaborare ciascuna richiesta secondo le procedure di trust evaluation del framework dichiarato dal prefisso.
In particolare, il prefisso ``x509_hash`` seleziona le procedure EUDIW (vedi :ref:`trust-evaluation:EUDIW Authentication`), il prefisso ``openid_federation`` seleziona le procedure del Trust Framework Nazionale (vedi :ref:`trust-evaluation:Trust Evaluation Processes by Context`).
I processi Authentication, Authorization e Metadata Retrieval and Validation vengono eseguiti sotto il framework selezionato.

Nel proximity flow entrambi i Trust Framework utilizzano l'mdoc reader authentication definita in [`ISO18013-5`_ #12.5], basata su un certificato X.509 fornito dalla Relying Party Instance nell'header ``x5chain`` del ``ReaderAuth``.

Sotto il Trust Framework EUDIW il certificato è l'access certificate, come profilato nella Section 5.3 di [`ETSI TS 119 472-2`_] (vedi :ref:`proximity-flow:Richiesta mdoc`), ed è convalidato rispetto alla Provider of Wallet-Relying Party Access Certificate List of Trusted Entities.

Sotto il Trust Framework Nazionale il certificato è il Relying Party authentication certificate ed è convalidato rispetto a un'Authentication Trust Anchor pubblicata nella Federation Trust Anchor Entity Configuration (vedi :ref:`trust-evaluation:Relying Party Proximity Authentication`).

Un meccanismo di selezione equivalente al prefisso ``client_id`` non è definito in [`ISO18013-5`_].

All'interno di IT-Wallet il framework applicabile è determinato dalla trust anchor che convalida il certification path del certificato del reader.
La richiesta è elaborata sotto il Trust Framework EUDIW quando il percorso termina in una trust anchor della Provider of Wallet-Relying Party Access Certificate List of Trusted Entities, e sotto il Trust Framework Nazionale quando termina in un'Authentication Trust Anchor della federazione.
La Wallet Unit DEVE determinare il framework applicabile prima del processo Authorization e DEVE eseguire l'Authorization solo sotto quel framework.

Failure Handling
^^^^^^^^^^^^^^^^

Il fallimento della trust evaluation sotto il framework selezionato NON DEVE essere valutato nuovamente sotto l'altro framework.

Nel Presentation Flow, in caso di fallimento, la Wallet Unit DEVE informare l'Utente che l'identità del Relying Party non ha potuto essere verificata e che la richiesta non è affidabile, e DEVE rifiutare la presentazione oppure avvisare l'utente e consentirgli di procedere comunque.
Durante l'Issuance Flow, quando questa autenticazione non ha esito positivo, la Wallet Unit DEVE mostrare un avviso all'Utente e NON DEVE richiedere l'emissione.
A differenza del caso di presentazione, in emissione non è prevista alcuna opzione di scelta per l'Utente.

Questo comportamento segue i requisiti definiti nell'ARF Annex 2 (`EIDAS-ARF`_), e si applica sia ai Trust Framework EUDIW sia a quelli Nazionali.

.. include:: trust-evaluation-eudiw.rst
.. include:: trust-evaluation-oidfed.rst
.. include:: trust-override-rules.rst

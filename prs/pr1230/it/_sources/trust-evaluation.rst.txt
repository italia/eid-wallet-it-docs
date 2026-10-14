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
-------------------------

Questa sezione definisce quale Trust Framework si applica a un'interazione.
I due Trust Framework sono descritti in :ref:`infrastructure-trust:Infrastructure of Trust`.
Le procedure di ciascun framework sono definite nelle sezioni seguenti.
I percorsi di onboarding e gli artifact di ciascun tipo di entità sono definiti in :ref:`onboarding-system:Onboarding Processes`.

L'**interazione** è l'autenticazione e l'autorizzazione delle parti per un'emissione o una presentazione.
La Wallet Unit DEVE selezionare esattamente un Trust Framework per ciascuna interazione, prima di Authentication, Authorization o Metadata Retrieval and Validation.
Il Trust Framework selezionato si applica all'intera interazione.
Una valutazione fallita è gestita come specificato in :ref:`trust-evaluation:Failure Handling`.

Il **trust anchor di firma** di un'attestazione segue il Rulebook del tipo di Attestato, in ogni fase e qualunque sia la parte che esegue la verifica.
I PID, le QEAA e le PuB-EAA DEVONO essere validati rispetto ai Trust Anchor della List of Trusted Entities o della Trusted List applicabile (vedere OIA_12, OIA_13, OIA_14 e OIA_15 dell'ARF Annex 2, `EIDAS-ARF`_).
La procedura per un Attestato ancorato al Trust Framework Nazionale è definita in :ref:`trust-evaluation:Signing Trust Anchor Validation Procedure`.

La dichiarazione resa in onboarding da un Non-Qualified EAA Provider o da una Relying Party è specificata in :ref:`onboarding-system:Registration Profiles`.
A runtime l'Attestato richiesto seleziona il Trust Framework dell'interazione.
Lo stesso Credential Issuer PUÒ essere valutato nell'ambito di framework diversi in interazioni diverse.

Ove la configurazione pubblicata attraverso i meccanismi EUDIW e la configurazione pubblicata attraverso la federazione divergono, la configurazione EUDIW DEVE prevalere.

.. _table_applicable_tf_by_entity:
.. list-table:: Trust Framework applicabile per interazione
    :class: longtable
    :widths: 22 46 32
    :header-rows: 1

    * - **Interazione**
      - **Condizione**
      - **Trust Framework**
    * - Emissione, Credential Issuer
      - L'Attestato richiesto è un PID, una QEAA o una PuB-EAA, oppure il Credential Issuer è di un altro Stato membro.
      - La Wallet Unit DEVE usare il Trust Framework EUDIW.
    * - Emissione, Credential Issuer
      - Il Credential Issuer è un'entità nazionale e l'Attestato richiesto è un Attestato Elettronico di Attributi non qualificato ad audience nazionale.
        L'IT-Wallet ID è un Attestato di questo tipo (vedere :term:`IT-Wallet ID`).
      - La Wallet Unit DEVE usare il Trust Framework Nazionale.
    * - Emissione, Wallet Instance Attestation
      - La Wallet Unit è di un altro Stato membro.
      - Il Credential Issuer DEVE validarla attraverso la Wallet Providers List of Trusted Entities.
    * - Emissione, Wallet Instance Attestation
      - La Wallet Unit è nazionale.
      - Il Credential Issuer PUÒ validarla attraverso il Trust Framework Nazionale (vedere :ref:`trust-evaluation:Wallet Unit Authentication`).
    * - Presentazione
      - La richiesta include un PID, una QEAA o una PuB-EAA, oppure un Attestato di un altro Stato membro, oppure la Relying Party offre il servizio al di fuori del pubblico nazionale.
      - La Relying Party DEVE usare il Trust Framework EUDIW per l'intera richiesta.
    * - Presentazione
      - La Relying Party è nazionale e la richiesta contiene soltanto un Attestato Elettronico di Attributi non qualificato ad audience nazionale.
      - La Relying Party DEVE usare il Trust Framework Nazionale.

Selection at Issuance
^^^^^^^^^^^^^^^^^^^^^

All'emissione la Wallet Unit avvia l'interazione e conosce l'Attestato richiesto (vedere :ref:`registry:Digital Credentials Catalog`).
La riga applicabile di :ref:`Trust Framework applicabile per interazione <table_applicable_tf_by_entity>` seleziona il Trust Framework.

Nel percorso EUDIW, Authentication, Authorization e Metadata Retrieval and Validation del Credential Issuer seguono :ref:`trust-evaluation:EUDIW Authentication`, :ref:`trust-evaluation:EUDIW Authorization` e :ref:`trust-evaluation:EUDIW Metadata Retrieval and Validation`.
Nel percorso Nazionale seguono :ref:`trust-evaluation:Federation Entity Authentication`, :ref:`trust-evaluation:Authorization` e :ref:`trust-evaluation:Metadata Retrieval and Validation`.

Gli header degli artifact firmati del Credential Issuer DEVONO essere coerenti con il framework selezionato.
Un header ``x5c`` reca il certificato di accesso nel percorso EUDIW.
Un header ``kid``, con l'header ``trust_chain`` opzionale, reca la chiave di federazione nel percorso Nazionale.

Selection at Presentation
^^^^^^^^^^^^^^^^^^^^^^^^^

La Relying Party non autentica la Wallet Unit.
Non può selezionare il Trust Framework in funzione dello Stato membro di quella Wallet Unit o Soluzione Wallet.
La riga applicabile di :ref:`Trust Framework applicabile per interazione <table_applicable_tf_by_entity>` seleziona il Trust Framework.

Nel flusso remoto la Relying Party dichiara tale framework attraverso il prefisso ``client_id`` della richiesta (vedere `OpenID4VP`_, Section 5.9).
Il prefisso ``x509_hash`` seleziona il Trust Framework EUDIW, come richiesto dalla clausola 6 di [`ETSI TS 119 472-2`_] (OIDFVP-HAIP_COMMON_GEN_REQ-02).
Il prefisso ``openid_federation`` seleziona il Trust Framework Nazionale.
La Wallet Unit DEVE elaborare ``x509_hash`` secondo :ref:`trust-evaluation:EUDIW Authentication`.
La Wallet Unit DEVE elaborare ``openid_federation`` secondo :ref:`trust-evaluation:Trust Evaluation Processes by Context` quando la Trust Chain della Relying Party è valida rispetto al National Trust Anchor.
Se tale Trust Chain non può essere validata, la Wallet Unit DEVE trattare la Relying Party come non affidabile.
La Wallet Unit DEVE interrompere l'interazione.

Nel flusso di prossimità entrambi i framework utilizzano la mdoc reader authentication definita in [`ISO18013-5`_ #12.5].
L'Istanza della Relying Party fornisce un certificato X.509 nell'header ``x5chain`` del ``ReaderAuth``.
Sul percorso EUDIW la Wallet Unit DEVE autenticare e validare il Wallet-Relying Party Access Certificate come specificato in :ref:`trust-evaluation:EUDIW Authentication`.
Sul percorso nazionale la Wallet Unit DEVE validare il certificato di reader come specificato in :ref:`trust-evaluation:Relying Party Proximity Authentication`.
La Wallet Unit DEVE eseguire l'Authorization esclusivamente nell'ambito del framework selezionato.
La Relying Party utilizza il certificato che corrisponde alla riga selezionata.

Failure Handling
^^^^^^^^^^^^^^^^

Il fallimento della trust evaluation nell'ambito del framework selezionato NON DEVE essere valutato nuovamente nell'ambito dell'altro framework.

Se l'autenticazione della Relying Party fallisce per qualsiasi motivo, la Wallet Unit DEVE informare l'Utente. Inoltre, la Wallet Unit DEVE non presentare gli attributi richiesti alla Relying Party, oppure dare all'Utente la scelta di presentare o meno gli attributi richiesti ([`EIDAS-ARF`_] RPA_06a).
Lo stesso vale nell'ambito del Trust Framework Nazionale: un esito ``NON_AUTHENTICATED`` DEVE interrompere l'interazione.

Se l'Authentication ha successo e l'Authorization fallisce, la Wallet Unit DEVE applicare :ref:`trust-evaluation:Authorization Decision and Override Rules`.
Durante la presentazione, una scelta dell'Utente di proseguire è consentita solo per gli esiti di Authorization overridable ivi definiti.
Il fallimento dell'Authentication non è overridable.

Durante l'Emissione, quando l'Authentication o l'Authorization non ha successo, la Wallet Unit DEVE mostrare un avviso all'Utente e NON DEVE richiedere l'emissione ([`EIDAS-ARF`_] RPRC_22a).
All'emissione non è offerta alcuna scelta all'Utente.

.. include:: trust-evaluation-eudiw.rst
.. include:: trust-evaluation-oidfed.rst
.. include:: trust-override-rules.rst

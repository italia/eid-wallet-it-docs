.. include:: ../common/common_definitions.rst
.. Included via trust-evaluation.rst at title level '-' (level 1).

Trust Evaluation in the EUDIW Trust Framework
------------------------------------------------

Le procedure definite in questa sezione profilano e combinano le seguenti specifiche esterne.

- `ETSI TS 119 615`_ e `ETSI TS 119 612`_, che definiscono la procedura e le strutture dati per autenticare e interpretare la List of Trusted Lists e le Member State Trusted Lists, applicate qui alle List of Trusted Entities.
- `ETSI EN 319 102-1`_ e `ETSI TS 119 182-1`_, che definiscono, rispettivamente, la validazione delle firme AdES e il formato JAdES della firma di una List of Trusted Entities.
- `ETSI TS 119 411-8`_, `ETSI TS 119 475`_ e `ETSI EN 319 412-1`_, che definiscono, rispettivamente, il Wallet-Relying Party Access Certificate, il Wallet-Relying Party Registration Certificate insieme ai relativi entitlements, e gli attributi del subject del certificato.
- `ETSI TS 119 472-2`_ e `ETSI TS 119 472-3`_, che profilano rispettivamente i protocolli di Presentation e Issuance, attraverso i quali un Wallet-Relying Party viene autenticato e le sue informazioni di registrazione sono rese disponibili alla Wallet Unit; quest'ultima definisce anche l'Embedded Disclosure Policy.
- IETF RFC 5280 (:rfc:`5280`) e IETF RFC 6960 (:rfc:`6960`), che definiscono la validazione del certification path X.509 e l'Online Certificate Status Protocol.

.. note::

    Il modello dati degli Artifact di Trust referenziati da queste procedure, insieme alle specifiche che li definiscono, è definito in :ref:`infrastructure-trust:EUDIW Trust Artifacts`.

    Le procedure definite in questa sezione sono eseguite all'interno dei flussi operativi di Issuance e Presentation (vedi :ref:`digital-credential-flows:Flussi relativi agli Attestati Elettronici`).
    I parametri su cui operano, come il signed Request Object, l'mdoc Request, i Metadata di tutte le Entità coinvolte e il modello dati delle Digital Credentials ricevute, sono definiti nelle rispettive sezioni (vedi :ref:`entities:Entità`, :ref:`remote-flow:Request Object` per il Remote Flow, :ref:`proximity-flow:Richiesta mdoc` per il Proximity Flow, e :ref:`credential-data-model:Formato Attestato Elettronico SD-JWT-VC` e :ref:`credential-data-model:Formato Attestato Elettronico mdoc-CBOR` per i formati delle Digital Credentials).

EUDIW Trust Evaluation Processes by Context
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Le procedure sono definite in forma generale, con un Trust Evaluator e un Trust Evaluated Party, e la tabella seguente definisce quale entità agisce in quale ruolo, quando e per quale scopo.

.. _table_eudiw_tf_roles:
.. list-table:: Trust Evaluation Processes by Entity and Context in the EUDIW Trust Framework
    :class: longtable
    :widths: 12 20 34 34
    :header-rows: 1

    * - **Entity**
      - **Context**
      - **As Trust Evaluator, implements**
      - **As Trust Evaluated Party, provides**
    * - Wallet Unit
      - Issuance of a Credential in the EU catalogue
      - Sul Credential Issuer:

        - :ref:`trust-evaluation:EUDIW Authentication`
        - :ref:`trust-evaluation:EUDIW Authorization`
        - :ref:`trust-evaluation:EUDIW Metadata Retrieval and Validation`

        Sulla Credenziale ricevuta:

        - :ref:`trust-evaluation:EUDIW Attestation Signature Validation`
      - La Wallet Instance Attestation, convalidata rispetto alla Wallet Providers List of Trusted Entities.
    * - Wallet Unit
      - Remote presentation, ``x509_hash`` prefix
      - Sul Relying Party:

        - :ref:`trust-evaluation:EUDIW Authentication`
        - :ref:`trust-evaluation:EUDIW Authorization`
        - :ref:`trust-evaluation:EUDIW Metadata Retrieval and Validation`
      - Nessun artifact a livello di entità è richiesto dalla Wallet Unit.
    * - Wallet Unit
      - Proximity presentation
      - Sul Relying Party:

        - :ref:`trust-evaluation:EUDIW Authentication`, basata sull'mdoc reader authentication
        - :ref:`trust-evaluation:EUDIW Authorization`
      - Nessun artifact a livello di entità è richiesto dalla Wallet Unit.
    * - Credential Issuer
      - Issuing Credentials in the EU catalogue
      - Sulla Wallet Unit:

        - :ref:`trust-evaluation:EUDIW Attestation Signature Validation`, applicata alla Wallet Instance Attestation
      - Il Wallet-Relying Party Access Certificate e la relativa registrazione, cioè la relativa voce Register e, ove emesso, il Wallet-Relying Party Registration Certificate.
    * - Relying Party
      - Remote or proximity presentation
      - Sulle Credenziali ricevute:

        - :ref:`trust-evaluation:EUDIW Attestation Signature Validation`
      - Il Wallet-Relying Party Access Certificate e la relativa registrazione, cioè la relativa voce Register e, ove emesso, il Wallet-Relying Party Registration Certificate.
    * - Relying Party Intermediary
      - Presentation, on behalf of an intermediated Relying Party
      - Non agisce come Trust Evaluator nei flussi operativi.
      - Il proprio Wallet-Relying Party Access Certificate e la registrazione del Relying Party intermediato, cioè la relativa voce Register e, ove emesso, il Wallet-Relying Party Registration Certificate.

EUDIW Trust Anchor Validation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Questa sezione specifica il **Trust Anchor Validation Process** che una Wallet Unit o un Wallet-Relying Party utilizza per stabilire l'integrità crittografica e l'autenticità di una List of Trusted Entities, o di una Trusted List, al fine di:

- convalidare l'affidabilità di una Trust Anchor (vedi :ref:`infrastructure-trust:Trust Anchor Certificate Profile`) per autenticare, autorizzare o convalidare un'entità o un artifact durante il *runtime*.
- convalidare le informazioni contenute nella List a fini *storici*.

A seconda dell'Artifact di Trust o dell'Attestazione verificata, il Trust Evaluator DEVE recuperare, scaricare e convalidare la List che referenzia la Trust Anchor appropriata:

1. La *List of Trusted Entities* DEVE essere utilizzata per recuperare le Trust Anchor per convalidare:

   - **WRPAC** nella Providers of WRPAC LoTE.
   - **WRPRC** nella Providers of WRPRC LoTE.
   - **Wallet Unit Attestation Sign/Seal Certificates** nella Wallet Providers LoTE.
   - **PID Sign/Seal Certificates** nella PID Providers LoTE.
   - **Registrar Sign/Seal Certificates** nella Registrar LoTE.
   - **PuB-EAA Sign/Seal Certificates** nella PuB-EAA Providers LoTE.
2. Le *Trusted Lists* sono utilizzate per recuperare le Trust Anchor per convalidare:

   - **QEAA Sign/Seal Certificates** nella corrispondente Member State Trusted List.

Per verificare l'autenticità delle List recuperate, l'Entità DEVE eseguire le seguenti validazioni:

- :ref:`trust-evaluation:List of Trusted Entities Validation`: convalidare la firma digitale della List of Trusted Entities verificandola rispetto al certificato del List of Trusted Entities Provider.
  Questo certificato è pubblicato nella Official Journal of the European Union.
- :ref:`trust-evaluation:Trusted List Validation`: convalidare la firma digitale della TL verificandola rispetto alle chiavi pubbliche del corrispondente Stato membro pubblicate nella List Of Trusted Lists (LOTL).
  La List Of Trusted Lists (LOTL) stessa è autenticata convalidando la sua firma digitale rispetto alla Official Journal of the European Union.

**Input**

L'Entità che convalida DEVE basare le decisioni di Trust Anchor validation solo su informazioni derivate da:

- l'Official Journal of the EU (OJEU) che ancora il trust nelle root certificate che hanno firmato le List of Trusted Entities e la List of Trusted Lists.
  La versione corrente dell'OJEU è disponibile `here <https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ:C_202601944>`_.
- una List of Trusted Entities o List of Trusted Lists convalidata e le Trusted List a livello di Stato membro.

**Outcome**

Ciascuna procedura di validazione (definita in :ref:`trust-evaluation:List of Trusted Entities Validation` e :ref:`trust-evaluation:Trusted List Validation`) restituisce un codice di esito di verifica granulare quando rileva una condizione negativa.
Questi codici alimentano la decisione finale:

- Se gli algoritmi di validazione terminano con:

    - ``LoTE-Status == LoTE_VERIFICATION_PASSED``, oppure
    - ``LOTL-Status == LOTL_VERIFICATION_PASSED``, oppure
    - ``EU-TL-Status == EU-TL_VERIFICATION_PASSED``;

    allora la List of Trusted Entities o la Trusted List è valida e i certificati Trust Anchor (vedi :ref:`infrastructure-trust:Trust Anchor Certificate Profile`) ivi contenuti DEVONO essere considerati affidabili.

- Se gli algoritmi di validazione terminano con:

    - ``LoTE-Status == LoTE_VERIFICATION_FAILED``, oppure
    - ``LOTL-Status == LOTL_VERIFICATION_FAILED``, oppure
    - ``EU-TL-Status == EU-TL_VERIFICATION_FAILED``;

    allora la List of Trusted Entities o la Trusted List non è valida e i certificati Trust Anchor (vedi :ref:`infrastructure-trust:Trust Anchor Certificate Profile`) ivi contenuti NON DEVONO essere considerati affidabili.

.. note::

    All'interno di IT-Wallet, una Wallet Unit è tenuta a memorizzare in cache le List of Trusted Lists, le List of Trusted Entities e le Trusted List degli Stati membri convalidate, in modo da non recuperarle a ogni interazione.
    La frequenza degli aggiornamenti e i tipi di liste da memorizzare in cache rappresentano un compromesso tra interoperabilità e utilizzo delle risorse.

List Key Rotation and Historical Verification
"""""""""""""""""""""""""""""""""""""""""""""

Per supportare la rotazione continua delle chiavi e gli aggiornamenti regolari, la LoTE e la LOTL implementano un *pivoting mechanism*.
Questo meccanismo consiste nel pubblicare la versione più recente della List all'URI primario referenziato nella Official Journal of the European Union, archiviando le versioni precedenti ad altri URI distinti chiamati *pivot*.
Ciascuna versione della List è firmata con una chiave pubblica referenziata nel pivot immediatamente precedente. L'ultimo pivot è firmato con la chiave referenziata nell'OJEU.
La versione più recente della List contiene esplicitamente gli URI in cui sono ospitate tutte le versioni storiche.

Un'Entità convalida questa catena di pivot dalla versione più recente alla più antica verificando che ciascun artifact successivo sia correttamente firmato dalla chiave pubblica autorizzata nella versione precedente.
La validazione finale si ottiene verificando l'affidabilità della chiave pubblica più antica, tramite lookup nell'OJEU oppure direttamente rispetto a una versione in cache, precedentemente convalidata, della List.
Ciò garantisce che un'entità in possesso dell'ultima versione valida conosciuta possa scoprire in modo affidabile la versione successiva e convalidarla tramite una catena di trust ininterrotta radicata nell'OJEU.

Sebbene il pivoting mechanism consenta aggiornamenti continui ai parametri della LoTE, determinati aggiornamenti possono richiedere l'aggiunta di un oggetto ``ServiceHistory`` alla LoTE per preservare le chiavi e le configurazioni storiche necessarie a convalidare firme legacy. Gli scenari specifici in cui un aggiornamento di Entità comporta la migrazione della sua configurazione in ``ServiceHistory`` sono dettagliati nella Section :ref:`infrastructure-trust:Trust Management and Lifecycle`.

Indipendentemente dall'obiettivo di un'Entità quando convalida la LoTE (che si tratti di recuperare una configurazione corrente o storica), il meccanismo di validazione DEVE seguire rigorosamente la Section :ref:`trust-evaluation:List of Trusted Entities Validation`.

List of Trusted Entities Validation
"""""""""""""""""""""""""""""""""""

Questa sezione definisce la validazione di una List of Trusted Entities.
La List of Trusted Entities, il suo modello dati e i tipi di List of Trusted Entities utilizzati nell'ecosistema EUDIW, uno per ciascuna categoria di provider notificato, sono definiti in :ref:`infrastructure-trust:Trusted List, Lists of Trusted Lists, and Lists of Trusted Entities`.

Una List of Trusted Entities è una lista firmata.
La sua autenticità è radicata nella Official Journal of the European Union, e supporta la rotazione continua delle chiavi tramite il *pivoting mechanism* descritto in :ref:`trust-evaluation:List Key Rotation and Historical Verification`.
Le Trust Anchor che pubblica sono fornite nel ``ServiceDigitalIdentity`` delle voci di servizio delle entità affidabili, come definito nella clause 6.6.3 di [`ETSI TS 119 602`_].

La procedura di autenticazione seguente segue la clause 4.1 di [`ETSI TS 119 615`_], che specifica l'autenticazione della EC compiled List of Trusted Lists (LOTL) con il relativo pivot mechanism.
Qui quella procedura è applicata al modello dati List of Trusted Entities di [`ETSI TS 119 602`_] e alla sua firma JAdES ([`ETSI TS 119 182-1`_]), al posto della LOTL XML.
Le variabili utilizzate di seguito sono gli analoghi List of Trusted Entities delle variabili LOTL preconfigurate nella clause 4.0 (GPR-4.0-02) di [`ETSI TS 119 615`_].
Corrispondono come segue:

- ``OJEU-LoTE-Loc`` corrisponde a ``OJEU-LOTL-Loc``;
- ``OJEU-LoTE-Certs-Set`` corrisponde a ``OJEU-LOTL-Certs-Set``;
- ``LoTESO-Cert`` corrisponde a ``LOTLSO-Cert``;
- i claim ``PointersToOtherLoTE`` e ``SchemeInformationURI`` corrispondono ai componenti *Pointers to other TSLs* (clause 6.3.13 di [`ETSI TS 119 602`_]) e *Scheme information URI* (clause 6.3.7).

**List of Trusted Entities Validation Algorithm**

L'Entità che convalida inizializza le seguenti variabili, corrispondenti ai parametri preconfigurati in GPR-4.0-02 di [`ETSI TS 119 615`_] per la LOTL.

**Input Variables**:

- ``OJEU-Loc``: URI dell'ultima pubblicazione dell'Official Journal of the European Union conosciuta.
- ``OJEU-LoTE-Loc``: URI dell'ultima List of Trusted Entities elaborata.
  Il valore predefinito è quello in ``OJEU-Loc``.
- ``OJEU-LoTE-Certs-Set``: l'insieme dei certificati affidabili dalla pubblicazione ``OJEU-Loc``.
- ``LoTE``: il JWT List of Trusted Entities attualmente in elaborazione.
  Inizializzato come ``NULL``.
- ``LoTE-Signer-Cert``: il certificato estratto dal parametro header ``x5c`` della List of Trusted Entities.
- ``LoTESO-Cert``: variabile temporanea per il certificato dello Scheme Operator in convalida.
  Inizializzata come ``NULL``.
- ``LoTESO-Certs-Set``: certificati affidabili estratti dal claim ``PointersToOtherLoTE`` (``SchemeTerritory`` ``EU``, clause 6.3.10 di [`ETSI TS 119 602`_]) di una List of Trusted Entities.

**Output Variables**:

- ``Authenticated-LoTE``: il payload JSON convalidato.
- ``LoTE-Status``: l'esito della validazione (ad esempio, ``LoTE_VERIFICATION_PASSED``).
- ``LoTE-Sub-Status``: codici di errore dettagliati.

**Process**:

La validazione DEVE eseguire i seguenti passi.
Ciascun passo indica il corrispondente requisito della clause 4.1 di [`ETSI TS 119 615`_].

1. (Initialization) Scaricare il file JWT da ``OJEU-LoTE-Loc`` e assegnarlo a ``LoTE``.
   (PRO-4.1.4-01)
2. (Parsing) Estrarre il primo certificato dall'header ``x5c`` di ``LoTE`` e assegnarlo a ``LoTE-Signer-Cert``.
   (PRO-4.1.4-02)
3. (Pivot Discovery) Iterare sui claim ``uriValue`` nel componente ``SchemeInformationURI`` (clause 6.3.7 di [`ETSI TS 119 602`_]).
   Contare il numero di URI validi che precedono l'URI corrispondente a ``OJEU-Loc`` e assegnarlo a ``n``.
   (PRO-4.1.4-03 per la ricerca di ``OJEU-Loc``, PRO-4.1.4-04 per il conteggio di ``n``)

    - Se nessun URI corrisponde a ``OJEU-Loc``: la validazione DEVE fallire con ``LoTE-Status`` impostato a ``LoTE_VERIFICATION_FAILED`` e ``LoTE-Sub-Status`` impostato a ``OJEU_LOCATION_INPUT_NOT_MATCHING_OJEU_LOCATION_IN_LoTE``.

4. (LoTE Location Conflict) Verificare la condizione ``OJEU-LoTE-Loc != LoTE Location`` AND ``LoTE != Content at LoTE Location``, dove ``LoTE Location`` è l'URI ``LoTELocation`` nel componente ``PointersToOtherLoTE`` di ``LoTE`` con ``SchemeTerritory`` ``EU`` (clause 6.3.13 di [`ETSI TS 119 602`_]).
   (PRO-4.1.4-05)

    - Se ``TRUE``: la validazione DEVE interrompersi con ``LoTE-Status`` impostato a ``LoTE_VERIFICATION_FAILED`` e ``LoTE-Sub-Status`` impostato a ``LoTE_FILE_CONFLICT``.
    - Se ``FALSE``, procedere al passo successivo.

5. (LoTE Freshness) Verificare la condizione ``OJEU-LoTE-Loc == LoTE Location`` AND ``LoTE != Content at LoTE Location``.
   (PRO-4.1.4-06)

    - Se ``TRUE``: impostare ``OJEU-LoTE-Loc`` su ``LoTE Location`` e riavviare dal Passo 1.
    - Se ``FALSE``, procedere al passo successivo.

6. (Digital Signature Validation) Convalidare la firma della ``LoTE`` corrente utilizzando la chiave pubblica di ``LoTE-Signer-Cert`` come certificato direttamente affidabile, seguendo la basic signature validation di [`ETSI EN 319 102-1`_] come richiesto da PRO-4.1.4-07.
   In particolare, i campi *Country code* e *Organization* nel Subject Distinguished Name del certificato che supporta la firma digitale AdES devono corrispondere rispettivamente al scheme territory e a uno dei valori dello scheme operator name all'interno della LoTE.
   (PRO-4.1.4-07, PRO-4.1.4-08, clause 6.8.0 di [`ETSI TS 119 602`_])

    - Se la validazione fallisce: interrompersi con ``LoTE-Status`` impostato a ``LoTE_VERIFICATION_FAILED`` e ``LoTE-Sub-Status`` impostato a ``LoTE_SIGNATURE_VERIFICATION_FAILED``.
    - Se ha esito positivo:

        - Impostare ``LoTESO-Cert`` su ``LoTE-Signer-Cert``.
        - Impostare ``LoTESO-Certs-Set`` sui certificati presenti nel claim ``PointersToOtherLoTE`` (scheme territory ``EU``) del payload ``LoTE`` corrente.
          (PRO-4.1.4-09)

7. (Intermediate Pivot Validation) (PRO-4.1.4-10 per il caso ``n = 0``, PRO-4.1.4-11 per il pivot loop)

    - Caso ``n = 0`` (No Pivots): procedere direttamente al Passo 8.
    - Caso ``n != 0`` (History Chain):

        - Iterare ``i`` da 1 a ``n`` (dal Pivot più recente al più antico).
          Sia ``Pivot`` il file scaricato dall'``i``-esimo URI.
        - (Link Check) Impostare ``Pivot-Certs-Set`` sui certificati nel claim ``PointersToOtherLoTE`` (territory ``EU``) di ``Pivot``.
          Se ``LoTESO-Cert`` (il firmatario del file precedente nella catena) non è in ``Pivot-Certs-Set``, la validazione DEVE fallire con ``LoTE-Sub-Status`` impostato a ``PIVOT_i-1_SIGNER_CERT_NOT_AUTHENTICATED_BY_PIVOT_i``.
        - (Update Signer) Impostare ``LoTESO-Cert`` sul primo certificato nel parametro header ``x5c`` di ``Pivot``.
        - (Verify Signature) Convalidare la firma di ``Pivot`` utilizzando ``LoTESO-Cert`` come descritto nel passo 6.
          (Digital Signature Validation).
          Se fallisce, la validazione DEVE fallire con ``LoTE-Status`` impostato a ``LoTE_VERIFICATION_FAILED`` e ``LoTE-Sub-Status`` impostato a ``PIVOT_i_SIGNATURE_VERIFICATION_FAILED``.
        - Il loop continua, procedendo all'indietro finché ``LoTESO-Cert`` rappresenta il firmatario del Pivot più antico.

8. (Trust Root Validation) Verificare la fine della catena.
   Se ``LoTESO-Cert`` (dall'ultimo Pivot, oppure dalla ``LoTE`` corrente quando non esiste alcun Pivot) non è in ``OJEU-LoTE-Certs-Set`` (l'insieme dei certificati affidabili), la validazione DEVE fallire con ``LoTE-Sub-Status`` impostato a ``PIVOT_n_SIGNER_CERT_NOT_AUTHENTICATED_BY_OJEU``.
   (PRO-4.1.4-12)

9. (Expiration) Se l'ora corrente è successiva al valore ``NextUpdate`` di ``LoTE``, oppure se è impostato a ``NULL`` (clause 6.3.15 di [`ETSI TS 119 602`_]), la validazione DEVE fallire.
   (PRO-4.1.4-13)

10. (Success) Impostare ``Authenticated-LoTE`` su ``LoTE`` e ``LoTE-Status`` su ``LoTE_VERIFICATION_PASSED``.
    (PRO-4.1.4-14, PRO-4.1.4-15)

11. (Update Bookmark) Se ``OJEU-LoTE-Loc`` non corrisponde al ``LoTE Location`` in ``Authenticated-LoTE`` (scheme territory ``EU``), aggiornare ``OJEU-LoTE-Loc`` a quel valore.
    (PRO-4.1.4-16)

12. (Update Trust Root) [Caution: this step modifies the Root of Trust configuration] (PRO-4.1.4-17)

    - Se ``OJEU-Loc`` non corrisponde al primo URI in ``SchemeInformationURI``, aggiornare ``OJEU-LoTE-Loc``.
    - Aggiornare ``OJEU-LoTE-Certs-Set`` secondo il nuovo insieme di certificati affidabili, sia in ``Authenticated-LoTE`` sia da una nuova pubblicazione dell'Official Journal of the European Union.

.. note::

    - I Passi 4, 5 e 11 consentono di modificare la posizione del file List of Trusted Entities senza cambiare la chiave pubblica del firmatario iniziale affidabile, purché sia la posizione vecchia sia quella nuova abbiano lo stesso contenuto; in caso contrario la validazione fallisce con ``LoTE_FILE_CONFLICT``.
      Ciò consente di recuperare la List of Trusted Entities da posizioni diverse senza influire sulla Trust Anchor validation, purché il contenuto sia lo stesso.
    - In caso di errore ``OJEU_LOCATION_INPUT_NOT_MATCHING_OJEU_LOCATION_IN_LoTE``, è probabile che la pubblicazione dell'Official Journal of the European Union sia stata aggiornata con una nuova posizione per la List of Trusted Entities.
      L'Entità che convalida DOVREBBE ripetere il processo di validazione dopo aver scaricato la versione più recente dell'Official Journal of the European Union.
    - Nel passo 8, l'Entità che convalida stabilisce il binding del certificato firmatario della ``LoTE`` con il certificato referenziato nell'Official Journal of the European Union, utilizzando effettivamente quest'ultimo come fonte di certificati affidabili.

Di seguito un flowchart che riassume i passi sopra per la validazione della List of Trusted Entities:

.. plantuml:: plantuml/lote-val-alg.puml
    :width: 99%
    :alt: La figura illustra il Flowchart of the List of Trusted Entities Validation Algorithm.
    :caption: Flowchart of the List of Trusted Entities Validation Algorithm.

Di seguito sono elencati in formato tabulare i codici di errore Sub-Status della List of Trusted Entities.

.. list-table:: List of Trusted Entities Sub-Status Error Codes
   :class: longtable
   :widths: 38 10 52
   :header-rows: 1

   * - **Code**
     - **Phase**
     - **Meaning**
   * - ``OJEU_LOCATION_INPUT_NOT_MATCHING_OJEU_LOCATION_IN_LoTE``
     - both
     - Nessun URI corrisponde all'``OJEU-Loc`` atteso all'interno del ``SchemeInformationURI`` della List of Trusted Entities.
       Ciò implica tipicamente che è disponibile una versione più recente della pubblicazione dell'Official Journal of the European Union.
   * - ``LoTE_FILE_CONFLICT``
     - both
     - Viene rilevato un conflitto di posizione in cui la posizione tracciata della List of Trusted Entities differisce da quella attiva, e il contenuto tra questi file non corrisponde.
   * - ``LoTE_SIGNATURE_VERIFICATION_FAILED``
     - both
     - La validazione della firma del file List of Trusted Entities corrente è fallita utilizzando il certificato del firmatario estratto, indicando potenziale manomissione o corruzione.
   * - ``PIVOT_i-1_SIGNER_CERT_NOT_AUTHENTICATED_BY_PIVOT_i``
     - both
     - La catena storica di trust è interrotta perché il certificato di firma del pivot o file precedente (i-1) non è presente nell'insieme di certificati affidabili del pivot successivo (i).
   * - ``PIVOT_i_SIGNATURE_VERIFICATION_FAILED``
     - both
     - La validazione della firma è fallita per un file pivot intermedio (i) all'interno della catena storica.
   * - ``PIVOT_n_SIGNER_CERT_NOT_AUTHENTICATED_BY_OJEU``
     - both
     - Il certificato finale alla radice della catena di pivot, oppure il firmatario della List of Trusted Entities corrente quando non esiste alcun pivot, non è presente nell'insieme ``OJEU-LoTE-Certs-Set`` dei certificati affidabili.

Trusted List Validation
""""""""""""""""""""""""

Questa sezione definisce la validazione della Trusted List.
Per convalidare la Trusted List, l'Entità che convalida DEVE:

1. Convalidare la EU List of Trusted Lists utilizzando l'algoritmo descritto nella section 4.1 di [`ETSI TS 119 615`_].
   Se questo fallisce, la validazione si interrompe e la Wallet Unit DEVE considerare l'Entità con cui sta interagendo come non affidabile.
   Il processo di validazione è analogo a :ref:`trust-evaluation:List of Trusted Entities Validation`, salvo che il formato LOTL è sempre XML.
2. Analizzare la EU List of Trusted Lists convalidata per individuare il certificato necessario a convalidare la Member State Trusted List pertinente.
3. Ottenere e convalidare la Trusted List pertinente come descritto nella section 4.2 di [`ETSI TS 119 615`_].

X509 Certificate Chain Validation Algorithm
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Questa procedura convalida il certification path.
È invocata da :ref:`trust-evaluation:EUDIW Authentication` e da :ref:`trust-evaluation:Authorization Artifacts Validation` per convalidare le catene del Wallet-Relying Party Access Certificate, del Wallet-Relying Party Registration Certificate e del Registrar Sign/Seal Certificate.
La Trust Anchor consumata come ``trust_anchor`` è profilata in :ref:`infrastructure-trust:Trust Anchor Certificate Profile`.

La validazione del certification path è la standard X.509 path validation definita in :rfc:`5280#section-6`, con il revocation status checking definito in :rfc:`5280` e :rfc:`6960`.
Il ciclo di vita del certificato e i meccanismi di revoca, inclusi i formati e i parametri CRL e OCSP, sono definiti in :ref:`infrastructure-trust:Revocation Mechanisms`.
I dettagli dell'algoritmo non sono ridefiniti qui.
Questa è la stessa validazione del certification path utilizzata nel Trust Framework Nazionale (vedi :ref:`trust-evaluation:X.509 Certificate Chain Validation`), dove la differenza è l'origine della trust anchor e l'estrazione aggiuntiva del Federation Entity Identifier.

All'interno del Trust Framework EUDIW si applica quanto segue.

  - Il ``trust_anchor`` è il certificato affidabile ottenuto dal componente ``ServiceDigitalIdentity`` della List of Trusted Entities o Trusted List applicabile convalidata (vedi :ref:`trust-evaluation:List of Trusted Entities Validation`) o Trusted List (vedi :ref:`trust-evaluation:Trusted List Validation`), cioè la Provider of WRPAC LoTE per il Wallet-Relying Party Access Certificate, la Provider of WRPRC LoTE per il Wallet-Relying Party Registration Certificate, e la Registrar LoTE per il Registrar Sign/Seal Certificate.
  - Il revocation status checking PUÒ essere omesso per un certificato che reca sia l'estensione ``noRevAvail`` sia l'estensione ``ETSIValAssuredCertMod`` (vedi :ref:`infrastructure-trust:Wallet-Relying Party Access Certificate (WRPAC) Profile`), il cui stato è quindi determinato esclusivamente dal periodo di validità.

**Input**

- ``path``: la sequenza di ``n`` certificati ``C_1, ..., C_n`` fornita dall'Entità, dove ``C_1`` è il primo certificato della catena e ``C_n`` è il certificato end-entity.
  Per ogni ``i`` in ``1, ..., n-1``, ``C_i`` è l'emittente di ``C_i+1``.
- ``trust_anchor``: il certificato affidabile ottenuto dal ``ServiceDigitalIdentity`` della List of Trusted Entities o Trusted List convalidata.
  DEVE contenere la chiave pubblica utilizzata per firmare ``C_1``.
  Le implementazioni DEVONO supportare sia certificati Trust Anchor self-signed sia non self-signed.
- ``current_time``: data e ora correnti.

**Outcome**

- Il certificato end-entity convalidato ``C_n``, oppure un fallimento.

**Process**

1. Costruire il certification path dal certificato end-entity ``C_n`` al ``trust_anchor``.
2. Eseguire la path validation definita in :rfc:`5280#section-6`, utilizzando il ``trust_anchor`` come input trust anchor dell'algoritmo e ``current_time`` come tempo di validazione.
3. Verificare lo stato di revoca dei certificati nel percorso secondo :rfc:`5280` e :rfc:`6960`, salvo che il controllo sia omesso come descritto sopra.

Se un passo fallisce, il certification path DEVE essere considerato non valido e la firma dell'artifact NON DEVE essere verificata con la certificate chain presentata.

EUDIW Attestation Signature Validation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Questo processo convalida la firma su un'Attestazione (Digital Credential o Wallet Instance Attestation) utilizzando il Sign/Seal Certificate appropriato come profilato in :ref:`infrastructure-trust:Entity Sign/Seal Certificate Profile`.
È invocato durante i flussi di issuance e presentation per convalidare la firma sull'Attestazione.

Il processo DEVE essere strutturato come segue:

- Se l'Attestazione la cui firma è verificata è una Digital Credential con una Trust Anchor referenziata all'interno di una LoTE o Trusted List (cioè un PID, PuB-EAA, QEAA), oppure è una Wallet Instance Attestation, allora si applica uno dei seguenti casi:

  - **Base Signature Validation**: eseguita quando l'Attestazione contiene il Sign/Seal Certificate e l'associated X.509 trust chain associata, e la Trust Anchor è presente nella LoTE pertinente (solo per PID o WIA) o Trusted List (solo per PuB-EAA o QEAA).
  
   Inoltre, in caso di un certificato PuB-EAA Sign/Seal, l'Entità che convalida la firma PUÒ convalidare la corrispondente PuB-EAA LoTE e confrontare la Trust Anchor con il corrispondente parametro nella LoTE per stabilire che il firmatario della Digital Credential è effettivamente un Authorized Pub-EAA.

  - **Fallback Signature Validation**: eseguita quando l'Attestazione non contiene il Sign/Seal Certificate, che invece è direttamente attestato come Trust Anchor nella LoTE (solo per PID o WIA).

- Se l'Attestazione la cui firma è verificata è un EAA non qualificato, le informazioni relative alla trust evaluation sono regolate dal corrispondente Rulebook.

La **Base Signature Validation** è strutturata come segue:

**Input**

- L'Attestazione ricevuta e la signer certificate chain ivi trasportata.
- Il tipo di artifact (cioè il tipo di Digital Credential o Wallet Instance Attestation) utilizzato per selezionare la List of Trusted Entities o Trusted List applicabile.

**Outcome**

- L'Attestazione convalidata, oppure un fallimento di validazione.

**Process**

Questo processo dipende dal tipo di Attestazione:

- **PID** o **WIA**.
  
  1. Verificare la firma dell'Attestazione con il certificato Sign/Seal fornito nell'Attestazione.
  2. Selezionare la List of Trusted Entities applicabile secondo il tipo dell'Attestazione ricevuta, convalidarla come definito in :ref:`trust-evaluation:List of Trusted Entities Validation`, ed estrarre la Trust Anchor appropriata dal campo ``ServiceDigitalIdentity`` dell'Entità pertinente.
  3. Estrarre la Sign/Seal certificate chain dall'Attestazione e convalidarla rispetto alla Trust Anchor ottenuta, come definito in :ref:`trust-evaluation:X509 Certificate Chain Validation Algorithm`.

- **QEAA**.

  1. Verificare la firma dell'Attestazione utilizzando il certificato Sign/Seal fornito nell'Attestazione. Per un QEAA, la qualified electronic signature o seal DEVE essere convalidata conformemente all'Article 32 di [`EIDAS`_].
  2. Recuperare la Trusted List appropriata secondo la nazionalità del Credential Issuer, convalidarla come definito in :ref:`trust-evaluation:Trusted List Validation`, ed estrarre la Trust Anchor appropriata dal campo ``ServiceDigitalIdentity`` dell'Entità pertinente.
  3. Estrarre la signer certificate chain dall'Attestazione e convalidarla rispetto alla Trust Anchor ottenuta, come definito in :ref:`trust-evaluation:X509 Certificate Chain Validation Algorithm`.

- **PuB-EAA**.

  1. Verificare la firma dell'Attestazione con il certificato Sign/Seal fornito nell'Attestazione. La qualified electronic signature o seal DEVE essere convalidata conformemente all'Article 32 di [`EIDAS`_].
  2. Selezionare la Trusted List appropriata secondo la nazionalità del Credential Issuer, recuperarla e convalidarla come definito in :ref:`trust-evaluation:Trusted List Validation`, ed estrarre la Trust Anchor appropriata dal campo ``ServiceDigitalIdentity`` dell'Entità pertinente.
  3. Estrarre la signer certificate chain dall'Attestazione e convalidarla rispetto alla Trust Anchor ottenuta, come definito in :ref:`trust-evaluation:X509 Certificate Chain Validation Algorithm`.
  4. [OPTIONAL] Recuperare la PuB-EAA LoTE, convalidarla come definito in :ref:`trust-evaluation:List of Trusted Entities Validation`, e confrontare i parametri pertinenti dell'oggetto ``TrustedEntityList`` del provider PuB-EAA (ad esempio, il campo ``SubjectDigitalIdentity``) con la Trust Anchor recuperata dalla Trusted List.

.. note:: 

  In ciascuno dei casi sopra, per un'Attestazione in formato mdoc, il Mobile Security Object trasporta il Document Signer certificate nell'header ``x5chain``, come definito in [`ISO18013-5`_]. Per un'Attestazione in formato SD-JWT VC, la issuer certificate chain è trasportata nell'header ``x5c`` della firma JOSE.

Se la **Base Signature Validation** ha esito negativo, l'Entità che convalida l'Attestazione DEVE eseguire la **Fallback Signature Validation** come segue:

.. warning::
  
  Questo processo si applica solo ai tipi di Attestazione **PID** e **WIA**.

**Input**

- L'Attestazione ricevuta.
- Il tipo di artifact (cioè il tipo di Digital Credential o Wallet Instance Attestation) utilizzato per selezionare la List of Trusted Entities applicabile.

**Outcome**

- L'Attestazione convalidata, oppure un fallimento di validazione.

**Process**

1. Recuperare la List of Trusted Entities applicabile secondo il tipo di Attestazione, convalidarla come definito in :ref:`trust-evaluation:List of Trusted Entities Validation`, ed estrarre la Trust Anchor appropriata dal campo ``ServiceDigitalIdentity`` dell'Entità pertinente.
2. Verificare la firma dell'Attestazione direttamente utilizzando la Trust Anchor convalidata come certificato firmatario.

.. warning::

   Sebbene la specifica IT Wallet richieda che i certificati Trust Anchor notificati alla Commissione e inclusi nella LoTE siano *differenti* dai Sign/Seal Certificates delle Entità correlate, la Clause 4.2 di [`ETSI TS 119 412-6`_] consente alle Trust Anchor LoTE di fungere direttamente da Sign/Seal Certificates.
   In questo caso, questi certificati NON DEVONO essere inclusi nell'Attestazione, imponendo al processo di verifica di aderire alla procedura **Fallback Signature Validation**.
   Per garantire l'interoperabilità, le implementazioni di EUDIW Attestation Signature Validation DEVONO supportare entrambi i meccanismi di validazione.

.. note::

  Quando si verificano firme o sigilli effettuati con chiavi storiche, si applica lo stesso processo, con la seguente differenza: la Trust Anchor è recuperata dall'elemento `ServiceHistory.ServiceDigitalIdentity` invece che dall'elemento `ServiceInformation.ServiceDigitalIdentity`.

Se sia la **Base Signature Validation** sia la **Fallback Signature Validation** falliscono, l'Attestazione NON DEVE essere considerata emessa da un'Entità affidabile.

EUDIW Authentication
^^^^^^^^^^^^^^^^^^^^

L'Authentication Process consente alla Wallet Unit di autenticare un Wallet-Relying Party durante un'interazione.
Stabilisce il trust convalidando la catena di certificati X.509 del Wallet-Relying Party, da un Provider of Wallet-Relying Party Access Certificate affidabile fino al Wallet-Relying Party Access Certificate presentato, e verificando che il Wallet-Relying Party possieda la corrispondente chiave privata.
Il Wallet-Relying Party Access Certificate è profilato in :ref:`infrastructure-trust:Wallet-Relying Party Access Certificate (WRPAC) Profile`.

Per la verifica dell'access certificate, la Wallet Unit DEVE accettare solo le Trust Anchor pubblicate nelle List of Trusted Entities dei Providers of Wallet-Relying Party Access Certificate notificati dagli Stati membri (vedi :ref:`trust-evaluation:List of Trusted Entities Validation`).

**Input**

L'esito dell'Authentication DEVE basarsi solo su informazioni derivate da:

- la Trust Anchor appropriata ottenuta da un'istanza valida della Provider of Wallet-Relying Party Access Certificate List of Trusted Entities;
- il certificate path X.509 che termina con il certificato end-entity Wallet-Relying Party Access Certificate;
- una firma del Wallet-Relying Party sull'artifact dell'interazione, che trasporta la prova di possesso della chiave privata referenziata nel Wallet-Relying Party Access Certificate.

**Outcome**

La Wallet Unit DEVE produrre una decisione: il Wallet-Relying Party è ``AUTHENTICATED`` oppure ``NON_AUTHENTICATED``.
Se ``AUTHENTICATED``, la Wallet Unit prosegue nel flusso di interazione.
Se ``NON_AUTHENTICATED``, la Wallet Unit DEVE informare l'Utente che l'identità del Wallet-Relying Party non ha potuto essere verificata e DEVE interrompere l'interazione, poiché l'entità non è affidabile.

**Process**

La Wallet Unit DEVE verificare l'autenticità e l'integrità del Wallet-Relying Party Access Certificate presentato come segue:

1. **Retrieve the Trust Anchor**: ottenere la voce del Provider of Wallet-Relying Party Access Certificate dalla List of Trusted Entities convalidata (vedi :ref:`trust-evaluation:List of Trusted Entities Validation`).
   Per selezionare la voce corretta, confrontare l'``issuer.organizationIdentifier`` del primo certificato della catena, la cui semantica è definita nella clause 5.1.4 di [`ETSI EN 319 412-1`_], con il ``TrustedEntitiesList[].TrustedEntity.TETradeName`` della List of Trusted Entities.
   I certificati nel campo ``TrustedEntityServices[].ServiceInformation.ServiceDigitalIdentity`` costituiscono la Trust Anchor.

2. **Construct the Certification Path**: costruire un percorso a partire dal Wallet-Relying Party Access Certificate presentato dal Wallet-Relying Party (``C_1``) e terminante con il certificato emesso dal Provider of Wallet-Relying Party Access Certificate (``C_n``).
   Il percorso più semplice consiste in un singolo certificato, dove ``n = 1``.

3. **Execute Path Validation**: convalidare il certification path come definito in :ref:`trust-evaluation:X509 Certificate Chain Validation Algorithm`, utilizzando la Trust Anchor recuperata al passo 1, come descritto in :ref:`trust-evaluation:Wallet-Relying Party Access Certificate Validation`.

4. **Verify the Signature**: utilizzare la chiave pubblica del Wallet-Relying Party Access Certificate convalidato per verificare la firma del Wallet-Relying Party sull'artifact che firma nella specifica interazione.
   La certificate chain e l'artifact firmato dipendono dal flusso:

    - **Remote Flow**: la catena è trasportata nell'header ``x5c`` del Wallet-Relying Party signed Request Object, e il Relying Party è autenticato tramite il ``x509_hash`` Client Identifier Prefix, come definito in [`OpenID4VP`_] e [`OPENID4VC-HAIP`_].
    - **Proximity Flow**: la catena è trasportata nell'mdoc reader authentication (``ReaderAuth``) firmata dal Wallet-Relying Party, nell'header COSE ``x5chain`` (label ``33``), come definito in [`ISO18013-5`_].
    - **Issuance Flow**: la catena è trasportata nell'header ``x5c`` del Wallet-Relying Party signed Credential Issuer Metadata, come definito in [`OpenID4VCI`_].

.. warning::

    Un Wallet-Relying Party DEVE distinguere tra autenticazione transitoria (ad esempio, access control) e content commitment (non-repudiation).
    Per impedire a un attaccante di mascherare un impegno legale come nonce di protocollo, il Wallet-Relying Party NON DEVE utilizzare la chiave privata del Wallet-Relying Party Access Certificate per firmare dati arbitrari che potrebbero essere controllati da una parte esterna.

Wallet-Relying Party Access Certificate Validation
"""""""""""""""""""""""""""""""""""""""""""""""""""

L'Entità che esegue la Wallet-Relying Party Access Certificate validation inizializza l'algoritmo in :ref:`trust-evaluation:X509 Certificate Chain Validation Algorithm` con il ``path`` e il ``trust_anchor`` ivi definiti.
Gli input sono i seguenti:

- ``C_n`` è il primo certificato della catena fornita dal Wallet-Relying Party;
- ``C_1`` è il Wallet-Relying Party Access Certificate;
- ``trust_anchor`` è un certificato del Provider of Wallet-Relying Party Access Certificate ottenuto dalla List of Trusted Entities.

.. warning::

  Come descritto nella Section 6.1.1 di `OPENID4VC-HAIP`_ il Trust Anchor Certificate necessario per la validazione del WRPAC NON DEVE essere incluso nella certificate chain e DEVE essere sempre recuperato nella LoTE appropriata.

EUDIW Authorization
^^^^^^^^^^^^^^^^^^^

Questa sezione specifica l'EUDIW Authorization Process che una Wallet Unit DEVE eseguire per determinare se un'interazione con un Wallet-Relying Party è consentita all'interno dell'ecosistema EUDI Wallet.
L'EUDIW Authorization Process DEVE avviarsi solo *dopo* che il Wallet-Relying Party è stato autenticato con successo secondo :ref:`trust-evaluation:EUDIW Authentication`.
Se il Wallet-Relying Party non è stato autenticato, l'EUDIW Authorization Process NON DEVE avviarsi.

I dati di autorizzazione di un Wallet-Relying Party sono trasportati dal Wallet-Relying Party Registration Certificate oppure, in modo equivalente, dal Register Response.
Entrambi sono profilati in [`ETSI TS 119 475`_] e il loro modello dati è descritto in :ref:`infrastructure-trust:Register Open APIs`.

L'EUDIW Authorization Process è suddiviso in:

- :ref:`trust-evaluation:Authorization Artifacts Validation`, che convalida integrità e autenticità dell'Artifact di Trust che trasporta i dati di autorizzazione; e
- :ref:`trust-evaluation:Authorization Validation`, che convalida il contenuto informativo dell'artifact convalidato.
  In particolare questa validazione copre:

    - **Issuance authorization**: determina se un Credential Issuer è registrato per il ruolo pertinente e autorizzato a emettere la specifica Digital Credential.
      Si applica a PID, QEAA, PuB-EAA ed EAA Provider operanti nell'ecosistema EUDIW.
    - **Presentation authorization**: determina se una richiesta del Relying Party rientra nel suo registered scope, se un'Embedded Disclosure Policy consente la disclosure, e se l'Utente approva.
      Si applica alle interazioni che coinvolgono sia Relying Party sia Relying Party Intermediaries, sia nei Remote Flow sia nei Proximity Flow.

- :ref:`trust-evaluation:Authorization Decision and Override Rules`, che produce un'*Authorization Decision* espressa come ``AUTHORIZED`` o ``NOT_AUTHORIZED`` sulla base degli esiti di Authorization Artifacts Validation e Authorization Validation.
  A seconda del tipo di Flow l'Utente PUÒ *override* l'Authorization Decision.

All'interno dell'*Authorization Validation*, la Wallet Unit DEVE distinguere tra il Wallet-Relying Party autenticato e l'*Authorization Subject*, cioè l'entità la cui autorizzazione è valutata:

- Durante l'Issuance, l'Authorization Subject è il Credential Issuer.
- Durante la presentazione *direct*, l'Authorization Subject è il Relying Party.
- Durante la presentazione *intermediated*, il Wallet-Relying Party autenticato è il Relying Party Intermediary, mentre l'Authorization Subject per la richiesta di dati è il *intermediated Relying Party*, il cui registered scope governa la richiesta.
  Il Relying Party Intermediary è a sua volta un'entità registrata, e la sua autorizzazione ad agire come intermediario è stabilita tramite il binding ``intermediary`` dichiarato nei dati di autorizzazione del Relying Party intermediato (vedi il Binding verification di seguito).

La Wallet Unit DEVE supportare la risoluzione del contesto di autorizzazione sia da un Wallet-Relying Party Registration Certificate, ove disponibile, sia dal Register, ove un Wallet-Relying Party Registration Certificate non è disponibile o non può essere considerato affidabile.
La logica sostanziale di autorizzazione NON DEVE cambiare in base alla fonte dati.
Quando entrambe le fonti sono disponibili, la Wallet Unit DEVE normalizzare entrambe nello stesso modello interno di autorizzazione prima di applicare le regole.

Authorization Artifacts Validation
"""""""""""""""""""""""""""""""""""

Gli artifact che trasportano i dati di autorizzazione di un'entità sono il Wallet-Relying Party Registration Certificate e il Register Response.
Entrambi trasportano informazioni equivalenti, nei profili JWT e CWT definiti nella Section 5.2.1 di [`ETSI TS 119 475`_].
La Wallet Unit DEVE supportare la validazione di entrambi e DEVE convalidarne almeno uno dei due.

Ciascuna procedura di validazione specifica i suoi input, la sua logica di elaborazione e il suo output, un codice di esito di verifica.
L'esito PUÒ essere overridden dall'Utente alle condizioni dettagliate in :ref:`trust-evaluation:Authorization Decision and Override Rules`.

Il flusso di validazione dipende dalla disponibilità del Wallet-Relying Party Registration Certificate nell'interazione.

- Durante il Presentation flow il Relying Party PUÒ trasmettere il Wallet-Relying Party Registration Certificate by value:

    - nel parametro ``verifier_info`` del Request Object, nel Remote Flow, come definito in [`ETSI TS 119 472-2`_] e Section 5.1 di [`OpenID4VP`_];
    - nel membro ``euWrprc`` di ``requestInfo`` nell'ISO ``DeviceRequest``, nel Proximity Flow, come definito nella Section 5.3 di [`ETSI TS 119 472-2`_] e in [`ISO18013-5`_].

- Durante l'Issuance flow il Credential Issuer trasmette i dati di autorizzazione nei Credential Issuer Metadata tramite l'array ``issuer_info``, come definito nella Section 4.2.3 di [`ETSI TS 119 472-3`_].
  L'array PUÒ contenere un elemento ``registration_cert`` con il Wallet-Relying Party Registration Certificate by value, e DEVE contenere un elemento ``registrar_dataset`` con le informazioni di registrazione.
  L'Embedded Disclosure Policy è distribuita tramite i Credential Issuer Metadata all'interno del campo ``credential_configurations_supported``, come definito in [`OpenID4VCI`_].

Se il Wallet-Relying Party Registration Certificate non è disponibile, oppure la sua validazione fallisce, la Wallet Unit DEVE interrogare il Register come descritto in :ref:`Register Query Validation <register-query-validation>`.
Il Register Response fornisce gli stessi dati rilevanti per l'autorizzazione del Wallet-Relying Party Registration Certificate.
Ciascun Registrar espone un servizio online tramite l'API descritta in :ref:`infrastructure-trust:Register Open APIs`.
Quando utilizza questo servizio la Wallet Unit DOVREBBE informare l'Utente che verrà effettuata una query esterna.

**Wallet-Relying Party Registration Certificate Validation**

Quando un Wallet-Relying Party Registration Certificate è disponibile, la Wallet Unit DEVE convalidarlo prima di basarsi su di esso:

1. **Format verification**: confermare che ``typ`` è ``rc-wrp+jwt`` nel Remote Flow, oppure ``rc-wrp+cwt`` nel Proximity Flow, come definito nella Section 5.2.1 di [`ETSI TS 119 475`_].
2. **Algorithm verification**: verificare che l'algoritmo di firma sia conforme, cioè che ``alg`` non sia né ``none`` né un algoritmo deprecato.
3. **Signature validation**: verificare che la firma del Wallet-Relying Party Registration Certificate sia valida.
4. **Trust Anchor validation**: convalidare la Providers of WRPRC List of Trusted Entities (vedi :ref:`trust-evaluation:List of Trusted Entities Validation`) e recuperare la Trust Anchor dal campo ``TrustedEntitiesList.ServiceDigitalIdentity``.
5. **Path validation**: convalidare la certificate chain del Wallet-Relying Party Registration Certificate come definito in :ref:`trust-evaluation:X509 Certificate Chain Validation Algorithm`, dove ``C_n`` è il certificato emesso dal Provider of WRPRC, ``C_1`` è il Wallet-Relying Party Registration Certificate, e il ``trust_anchor`` è la Trust Anchor ottenuta al passo precedente.
6. **Temporal validity**: verificare ``iat`` e ``exp`` se presenti.
7. **Status verification**: verificare lo stato di revoca tramite il campo ``status`` del Wallet-Relying Party Registration Certificate, come definito in [`ETSI TS 119 475`_], seguendo :ref:`credential-revocation:Verifica degli Stati degli Attestati Elettronici`.
8. **Coherence check**: verificare che il subject e i campi del Wallet-Relying Party Registration Certificate siano coerenti con l'interazione.

.. note::

  Nel Passo 5.
  **Path Validation**, il Trust Anchor Certificate necessario per la validazione del WRPRC NON DEVE essere incluso nella certificate chain e DEVE essere sempre recuperato nella LoTE appropriata.

**Outcome**

- Se tutti i passi hanno esito positivo e il Wallet-Relying Party Registration Certificate è nello stato ``VALID``, la Wallet Unit DEVE impostare ``authz_art_state`` su ``CERTIFICATE_VALID``.
- Se un passo fallisce, la Wallet Unit DEVE impostare ``authz_art_state`` su ``CERTIFICATE_INVALID``.
  Questo non è una decisione finale di autorizzazione: attiva :ref:`Register Query Validation <register-query-validation>` come fallback.

.. _register-query-validation:

**Register Query Validation**

Quando il Wallet-Relying Party Registration Certificate non è disponibile oppure la sua validazione è fallita, la Wallet Unit DEVE interrogare l'API Register:

1. **Extract the Registrar URL** dalla Presentation Request, cioè ``verifier_info`` nel Remote Flow oppure ``requestInfo`` nel Proximity Flow, oppure dai Credential Issuer Metadata, cioè ``issuer_info[].registry_uri``, durante l'Issuance.
2. **Connect** al servizio online del Registrar tramite HTTPS.
3. **Query** del servizio con l'entity identifier e, opzionalmente, l'``intended_use_id``.
   L'entity identifier è ``verifier_info[].data.identifier`` nel Remote Flow, ``docRequest.itemsRequest[].requestInfo.EUWrpRegistrarInfo.identifier`` nel Proximity Flow, oppure ``issuer_info[].data.identifier`` durante l'Issuance.
4. **Format verification**: confermare che ``typ`` è ``jwt``, come definito nella Section 5.2.1 di [`ETSI TS 119 475`_].
5. **Verify pertinence**: verificare che la risposta riguardi l'Authorization Subject pertinente e l'intended use.
6. **Verify the response signature**: verificare la firma del Registrar utilizzando il Sign/Seal Certificate trasportato nel claim ``x5c`` della risposta.
7. **Trust Anchor validation**: convalidare la Registrars List of Trusted Entities (vedi :ref:`trust-evaluation:List of Trusted Entities Validation`) e recuperare la Registrar Trust Anchor dal campo ``TrustedEntitiesList.ServiceDigitalIdentity``.
8. **Path validation**: convalidare la catena del Registrar Sign/Seal Certificate come definito in :ref:`trust-evaluation:X509 Certificate Chain Validation Algorithm`, dove ``C_1`` è il Registrar Sign/Seal Certificate, e il ``trust_anchor`` è la Trust Anchor ottenuta al passo precedente.
9. **Normalize** i dati derivati dal Register nello stesso modello interno utilizzato per il Wallet-Relying Party Registration Certificate.

.. note::

    Anche quando il Relying Party che richiede la presentazione è un Relying Party Intermediary, la Presentation Request DEVE trasportare i dati del Relying Party intermediato, come definito in [`ETSI TS 119 475`_].

**Outcome**

- Se tutti i passi hanno esito positivo, la Wallet Unit DEVE impostare ``authz_art_state`` su ``REGISTER_VALID``.
- Se un passo fallisce, la Wallet Unit DEVE impostare ``authz_art_state`` su ``FAILED``.

Durante l'Issuance solamente, i dati ``registrar_dataset`` POSSONO essere utilizzati come ulteriore fallback, solo a titolo informativo, e NON DEVONO essere presentati all'Utente come verificati.
Nel Passo 8.
**Path Validation**, il Trust Anchor Certificate necessario per la validazione del Registrar Sign/Seal Certificate NON DEVE essere incluso nella certificate chain della risposta del Register e DEVE essere sempre recuperato nella LoTE appropriata.

Authorization Validation
"""""""""""""""""""""""""""""

L'Authorization Validation DEVE seguire l'Authorization Artifacts Validation quando ``authz_art_state == REGISTER_VALID`` oppure ``authz_art_state == CERTIFICATE_VALID``.
Se ``authz_art_state == FAILED`` la Wallet Unit NON DOVREBBE eseguire alcuna Authorization Validation, poiché non può cambiare la Authorization Decision finale.

**Input**

La Wallet Unit DEVE basare l'Authorization Validation solo su:

- il Wallet-Relying Party autenticato e il contesto di interazione, autorevoli solo per l'identità del Wallet-Relying Party;
- un Authorization Artifact convalidato, cioè un Wallet-Relying Party Registration Certificate o un Register Response, autorevole per l'identità del subject, gli entitlements, l'intended use, il registered scope, le relazioni di intermediary, i dati specifici di issuance e i riferimenti alla privacy policy, come definito in [`ETSI TS 119 475`_];
- informazioni di fallback esplicitamente identificate, non autorevoli;
- un'Embedded Disclosure Policy verificata, REQUIRED quando fornita dall'Attestation Provider durante la Credential Issuance, autorevole quando presente.

Quando le fonti autorevoli sono in conflitto con quelle non autorevoli, le fonti autorevoli DEVONO prevalere.
Quando il contesto del Wallet-Relying Party autenticato è in conflitto con l'identità o il binding di intermediary nel contesto di autorizzazione verificato, la Wallet Unit DEVE produrre ``NOT_AUTHORIZED``, non overridable.
Un Registrar URL trasportato nella richiesta NON DEVE essere trattato da solo come prova sufficiente di informazioni registrate; PUÒ essere utilizzato solo come discovery hint salvo conferma da una fonte autorevole.

**Outcome**

La Wallet Unit DEVE produrre le variabili ``authz_val_state`` e ``edp_state``, entrambe inizializzate a ``none``.

**Process**

1. **Binding verification**.
   La Wallet Unit DEVE assicurare che l'entità autenticata coincida con l'entità descritta nei dati di autorizzazione.
   L'identità del Wallet-Relying Party è l'``organizationIdentifier`` del subject del Wallet-Relying Party Access Certificate (clause 5.1.4 di [`ETSI EN 319 412-1`_]; il profilo Wallet-Relying Party Access Certificate è definito in [`ETSI TS 119 411-8`_]).

    - **Credential Issuance**.
      La Wallet Unit DEVE confrontare l'identificatore del Credential Issuer con il ``sub`` del Wallet-Relying Party Registration Certificate oppure, se non è disponibile alcun Wallet-Relying Party Registration Certificate, con l'``identifier`` utilizzato nella query Register, e con l'``issuer_info.data.identifier`` dei Credential Issuer Metadata.
    - **Credential Presentation**.
      La Wallet Unit DEVE innanzitutto assumere lo scenario **direct** e confrontare l'identificatore del Relying Party con il ``sub`` del Wallet-Relying Party Registration Certificate oppure, se non disponibile, con l'``identifier`` utilizzato nella query Register, e con l'``verifier_info.data.identifier`` del Request Object nel Remote Flow oppure ``docRequest.itemsRequest[].requestInfo.EUWrpRegistrarInfo.identifier`` nel Proximity Flow.
      Se il confronto fallisce, la Wallet Unit DEVE tentare lo scenario **intermediated** e confrontare l'identificatore con il campo ``intermediary.sub`` trasportato nel Wallet-Relying Party Registration Certificate oppure nel Register Response.

    Se il Binding verification fallisce, la Wallet Unit DEVE interrompere l'Authorization Validation e impostare ``authz_val_state`` su ``BINDING_FAILED``.
    Se ha esito positivo, la Wallet Unit DEVE rendere disponibili all'Utente l'identità del Relying Party Intermediary, l'identità o la descrizione del servizio del Relying Party intermediato, e l'intended use della richiesta; il modo in cui queste informazioni sono presentate è definito nelle sezioni di interazione con l'Utente pertinenti della specifica IT-Wallet.

    .. note::

        Se la Wallet Unit ha utilizzato solo il ``sub`` del Wallet-Relying Party Registration Certificate per il Binding verification e l'esito è ``BINDING_FAILED``, il Wallet-Relying Party Registration Certificate non è valido per questo Relying Party.
        La Wallet Unit DEVE interrogare il Register, convalidare la risposta come descritto in :ref:`Register Query Validation <register-query-validation>`, e ripetere il Binding verification.

2. **Entitlement verification**.
   La Wallet Unit DEVE verificare che gli entitlements dell'Authorization Subject corrispondano al ruolo atteso.
   La Wallet Unit DEVE analizzare il campo ``entitlements`` del Wallet-Relying Party Registration Certificate o del Register Response e verificare che contenga l'entitlement URI atteso per l'interazione, tra quelli definiti nell'Annex A.2 di [`ETSI TS 119 475`_]:

    - ``https://uri.etsi.org/19475/Entitlement/PID_Provider`` per i PID Provider, durante l'emissione di PID;
    - ``https://uri.etsi.org/19475/Entitlement/QEAA_Provider`` per i QEAA Provider, durante l'emissione di QEAA;
    - ``https://uri.etsi.org/19475/Entitlement/PUB_EAA_Provider`` per i PuB-EAA Provider, durante l'emissione di PuB-EAA;
    - ``https://uri.etsi.org/19475/Entitlement/Non_Q_EAA_Provider`` per gli EAA Provider, durante l'emissione di EAA;
    - ``https://uri.etsi.org/19475/Entitlement/Service_Provider`` per i Relying Party, durante la Credential Presentation.

    Se l'entitlement atteso non è presente, la Wallet Unit DEVE impostare ``authz_val_state`` su ``WRONG_ENTITLEMENT``.

3. **Attestation Type verification**.
   Durante la Credential Issuance, la Wallet Unit DEVE verificare che il PID o l'Attestation Type in emissione sia registrato per il Credential Issuer.
   Un PID Provider che emette PID PUÒ omettere questo passo.
   Altrimenti la Wallet Unit DEVE confrontare l'array ``provides_attestations`` del Wallet-Relying Party Registration Certificate o del Register Response (definito nella Table 8 di [`ETSI TS 119 475`_]) con le chiavi ``credential_configurations_supported`` dei Credential Issuer Metadata ([`OpenID4VCI`_]).
   Il confronto DEVE essere esatto e case sensitive, su ``vct`` per SD-JWT VC e su ``docType`` per mdoc.
   Se non trovato, la Wallet Unit DEVE impostare ``authz_val_state`` su ``ATTESTATION_TYPE_NOT_REGISTERED``.

4. **Scope Comparison**.
   Durante la Credential Presentation, la Wallet Unit DEVE verificare che le Digital Credentials e gli attributi richiesti rientrino nel registered scope, trasportato nell'array ``credentials`` del Wallet-Relying Party Registration Certificate o del Register Response (definito nella Table 9 di [`ETSI TS 119 475`_]).

    - **Remote Flow**: estrarre le Digital Credentials e gli attributi richiesti dal ``dcql_query`` del Request Object ([`OpenID4VP`_]) e confrontarli con le voci ``credentials``, confrontando ``format`` e ``meta`` (``vct_values`` per SD-JWT VC) e gli attributi richiesti con i percorsi ``claim``.
    - **Proximity Flow**: estrarre ``docType`` e ``nameSpaces`` dai ``docRequests`` dell'mdoc Request ([`ISO18013-5`_]) e confrontarli rispettivamente con ``credentials[].meta.doctype_value`` e ``credentials[].claim``.

    Il confronto DEVE essere esatto e case sensitive.
    Se una Digital Credential o un attributo richiesto non è registrato, la Wallet Unit DEVE impostare ``authz_val_state`` su ``OVERASKING_DETECTED`` e identificare gli attributi o le Digital Credentials non registrati.

    Se tutti i controlli sopra applicabili all'interazione sono soddisfatti, la Wallet Unit DEVE impostare ``authz_val_state`` su ``VERIFICATION_PASSED``.

5. **Embedded Disclosure Policy evaluation**.
   Durante la Credential Presentation, per ciascuna Digital Credential corrispondente alla Presentation Request, la Wallet Unit DEVE verificare la presenza di un'Embedded Disclosure Policy memorizzata localmente.
   Se non ne esiste alcuna, questo controllo è superato.
   Altrimenti, secondo il ``policy_type`` definito nella Section 4.2.5 di [`ETSI TS 119 472-3`_]:

    - ``no_policy``: non si applica alcuna restrizione.
    - ``authorized_rp_only``: sono autorizzati solo i Relying Party nell'elenco ``authorized_parties``.
      La Wallet Unit DEVE confrontare il subject DN del Relying Party del Wallet-Relying Party Access Certificate con le voci ``subject_dn``, e gli entitlements o sub-entitlements del Relying Party del Wallet-Relying Party Registration Certificate con le voci ``entitlement_uri``.
      Un match su uno dei due criteri è sufficiente.
    - ``specific_root_of_trust``: sono autorizzati solo i Relying Party la cui catena del Wallet-Relying Party Access Certificate contiene una delle ``trusted_roots``.
      La Wallet Unit DEVE confrontare ``issuer_dn`` utilizzando il LDAP DN comparison e ``serial_number`` utilizzando il confronto intero.

    Se il controllo applicabile è soddisfatto, oppure non è presente alcuna Embedded Disclosure Policy, la Wallet Unit DEVE impostare ``edp_state`` su ``EDP_SATISFIED``; altrimenti DEVE impostare ``edp_state`` su ``EDP_NOT_SATISFIED``.

**Outcome**

Al termine dell'Authorization Validation la Wallet Unit DEVE produrre i valori ``authz_val_state`` e ``edp_state``.
La tabella seguente riassume i codici.

.. _table_authz_state_codes:
.. list-table:: Authorization Validation State Codes
   :class: longtable
   :widths: 18 26 12 44
   :header-rows: 1

   * - **Variable**
     - **Code**
     - **Phase**
     - **Meaning**
   * - ``authz_art_state``
     - ``CERTIFICATE_VALID``
     - both
     - Il formato, la firma, la trust anchor e lo stato del Wallet-Relying Party Registration Certificate sono verificati con successo.
   * - ``authz_art_state``
     - ``CERTIFICATE_INVALID``
     - both
     - Un controllo di formato, firma, trust anchor o stato fallisce sul registration certificate presentato.
   * - ``authz_art_state``
     - ``REGISTER_VALID``
     - both
     - La query online al Registrar è completata, e la firma, la pertinenza e la trust anchor della risposta hanno superato i controlli.
   * - ``authz_art_state``
     - ``FAILED``
     - both
     - La query online al Registrar o la verifica della risposta è fallita durante le procedure di fallback.
   * - ``authz_val_state``
     - ``WRONG_ENTITLEMENT``
     - both
     - Gli entitlements dell'Authorization Subject non corrispondono al ruolo atteso per il contesto attivo.
   * - ``authz_val_state``
     - ``BINDING_FAILED``
     - both
     - Il binding identitario tra il Wallet-Relying Party autenticato e i dati di autorizzazione fallisce.
   * - ``authz_val_state``
     - ``ATTESTATION_TYPE_NOT_REGISTERED``
     - issuance
     - L'Attestation Type in emissione non è presente nei profili registrati del Credential Issuer.
   * - ``authz_val_state``
     - ``OVERASKING_DETECTED``
     - presentation
     - Il Relying Party richiede Digital Credentials, formati o namespace che eccedono il suo registered scope.
   * - ``authz_val_state``
     - ``VERIFICATION_PASSED``
     - both
     - Binding identitario, entitlement verification, attestation matching e scope checking hanno superato tutti i controlli.
   * - ``edp_state``
     - ``EDP_SATISFIED``
     - presentation
     - Non si applica alcuna restrizione dell'Embedded Disclosure Policy, oppure il Relying Party soddisfa la policy locale.
   * - ``edp_state``
     - ``EDP_NOT_SATISFIED``
     - presentation
     - Il Relying Party non soddisfa alcuna Embedded Disclosure Policy memorizzata localmente.

La Authorization Decision finale, ``AUTHORIZED`` o ``NOT_AUTHORIZED``, è elaborata a partire dai valori ``authz_art_state``, ``authz_val_state`` e ``edp_state``, come definito in :ref:`trust-evaluation:Authorization Decision and Override Rules`.

.. plantuml:: plantuml/eudiw-authz-eval.puml
    :width: 99%
    :alt: Flowchart of the EUDIW Authorization Algorithm.
    :caption: Flowchart of the EUDIW Authorization Algorithm.

EUDIW Metadata Retrieval and Validation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

All'interno del Trust Framework EUDIW i metadata di un Wallet-Relying Party sono ottenuti tramite il flusso di protocollo e la loro autenticità è stabilita tramite il Wallet-Relying Party Access Certificate.
Ciò si applica alla Credential Issuance e alla Credential Presentation nel Remote Flow.
Nel Proximity Flow non viene eseguito alcun metadata retrieval separato: l'identità del Relying Party è stabilita tramite l'mdoc reader authentication (vedi :ref:`trust-evaluation:EUDIW Authentication`).

**Metadata Retrieval**

La Wallet Unit ottiene i metadata del Wallet-Relying Party secondo l'interazione:

- Durante la Credential Issuance, i Credential Issuer Metadata sono ottenuti dall'endpoint well-known metadata del Credential Issuer, come definito in [`OpenID4VCI`_] (vedi :ref:`credential-issuer-endpoint:Endpoint Metadata`).
- Durante la Credential Presentation nel Remote Flow, i metadata del Relying Party sono trasportati nel Request Object della authorization request, come definito in [`OpenID4VP`_] (vedi :ref:`remote-flow:Request Object`).

**Metadata Validation**

L'autenticità dei metadata recuperati è stabilita tramite il Wallet-Relying Party Access Certificate.
Durante la Credential Issuance, i Credential Issuer Metadata sono firmati dall'Attestation Provider come definito nella Section 12.2.3 di [`OpenID4VCI`_], fornendo la catena del Wallet-Relying Party Access Certificate nell'header ``x5c`` della firma JOSE.
Durante la Credential Presentation nel Remote Flow, il Request Object è firmato dal Relying Party e fornisce lo stesso header ``x5c``.
In entrambi i casi la Wallet Unit convalida la firma e la certificate chain come definito in :ref:`trust-evaluation:EUDIW Authentication`, e DEVE utilizzare solo i metadata la cui firma è verificata rispetto al Wallet-Relying Party Access Certificate autenticato.


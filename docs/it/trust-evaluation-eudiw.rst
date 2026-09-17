.. include:: ../common/common_definitions.rst
.. Incluso tramite trust-evaluation.rst al livello di titolo '-' (livello 1).

Trust Evaluation in the EUDIW Trust Framework
------------------------------------------------

Le procedure definite in questa sezione profilano le seguenti specifiche esterne.

- `ETSI TS 119 615`_ e `ETSI TS 119 612`_, che definiscono la procedura e le strutture dati per autenticare e interpretare la List of Trusted Lists e le Trusted List degli Stati membri, applicate qui alle List of Trusted Entities.
- `ETSI EN 319 102-1`_ e `ETSI TS 119 182-1`_, che definiscono, rispettivamente, la validazione delle firme AdES e il formato JAdES della firma di una List of Trusted Entities.
- `ETSI TS 119 411-8`_, `ETSI TS 119 475`_ e `ETSI EN 319 412-1`_, che definiscono, rispettivamente, il Wallet-Relying Party Access Certificate, il Wallet-Relying Party Registration Certificate insieme alle sue entitlement, e gli attributi del subject del certificato.
- `ETSI TS 119 472-2`_ e `ETSI TS 119 472-3`_, che profilano rispettivamente i protocolli di Presentazione e di Emissione, attraverso i quali una Wallet-Relying Party è autenticata e le sue informazioni di registrazione sono rese disponibili alla Wallet Unit; quest'ultima definisce inoltre l'Embedded Disclosure Policy.
- IETF RFC 5280 (:rfc:`5280`) e IETF RFC 6960 (:rfc:`6960`), che definiscono la validazione del certification path X.509 e l'Online Certificate Status Protocol.
- IETF RFC 9162 (:rfc:`9162`), che definisce Certificate Transparency versione 2.0 e il Signed Certificate Timestamp che una Wallet Unit verifica sul Wallet-Relying Party Access Certificate.

.. note::

    Il modello dati dei Trust Artifact referenziati da queste procedure, insieme alle specifiche che li definiscono, è definito in :ref:`infrastructure-trust:EUDIW Trust Artifacts`.

    Le procedure definite in questa sezione sono eseguite all'interno dei flussi operativi di Emissione e Presentazione (vedi :ref:`digital-credential-flows:Flussi relativi agli Attestati Elettronici`).
    I parametri su cui operano, come il Request Object firmato, la mdoc Request, i Metadata di tutte le Entità coinvolte e il modello dati degli Attestati Elettronici ricevuti, sono definiti nelle rispettive sezioni (vedi :ref:`entities:Entità`, :ref:`remote-flow:Request Object` per il Remote Flow, :ref:`proximity-flow:Richiesta mdoc` per il Proximity Flow, e :ref:`credential-data-model:Formato Attestato Elettronico SD-JWT-VC` e :ref:`credential-data-model:Formato Attestato Elettronico mdoc-CBOR` per i formati degli Attestati Elettronici).

EUDIW Trust Evaluation Processes by Context
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Le procedure sono definite in forma generale, con un Trust Evaluator e una Trust Evaluated Party, e la tabella seguente definisce quale entità agisce in quale ruolo, quando e per quale scopo.

.. _table_eudiw_tf_roles:
.. list-table:: Processi di Trust Evaluation per Entità e Contesto nel Trust Framework EUDIW
    :class: longtable
    :widths: 12 20 34 34
    :header-rows: 1

    * - **Entità**
      - **Contesto**
      - **In qualità di Trust Evaluator, implementa**
      - **In qualità di Trust Evaluated Party, fornisce**
    * - Wallet Unit
      - Emissione di una Credenziale nel catalogo UE
      - Sul Credential Issuer:

        - :ref:`trust-evaluation:EUDIW Authentication`
        - :ref:`trust-evaluation:EUDIW Authorization`
        - :ref:`trust-evaluation:EUDIW Metadata Retrieval and Validation`

        Sull'Attestato ricevuto:

        - :ref:`trust-evaluation:EUDIW Attestation Signature Validation`
      - La Wallet Instance Attestation, validata rispetto alla List of Trusted Entities dei Wallet Provider.
    * - Wallet Unit
      - Presentazione remota, prefisso ``x509_hash``
      - Sulla Relying Party:

        - :ref:`trust-evaluation:EUDIW Authentication`
        - :ref:`trust-evaluation:EUDIW Authorization`
        - :ref:`trust-evaluation:EUDIW Metadata Retrieval and Validation`
      - Nessun artifact a livello di entità è richiesto dalla Wallet Unit.
    * - Wallet Unit
      - Presentazione in prossimità
      - Sulla Relying Party:

        - :ref:`trust-evaluation:EUDIW Authentication`, basata sull'mdoc reader authentication
        - :ref:`trust-evaluation:EUDIW Authorization`
      - Nessun artifact a livello di entità è richiesto dalla Wallet Unit.
    * - Credential Issuer
      - Emissione di Credenziali nel catalogo UE
      - Sulla Wallet Unit:

        - :ref:`trust-evaluation:EUDIW Attestation Signature Validation`, applicata alla Wallet Instance Attestation
      - Il Wallet-Relying Party Access Certificate e il Wallet-Relying Party Registration Certificate del Servizio applicabile, inclusi per valore nei Metadata del Credential Issuer ([`EIDAS-ARF`_] RPRC_22).
    * - Relying Party
      - Presentazione remota o in prossimità
      - Sugli Attestati ricevuti:

        - :ref:`trust-evaluation:EUDIW Attestation Signature Validation`
      - Il Wallet-Relying Party Access Certificate e il Wallet-Relying Party Registration Certificate inclusi per valore nella richiesta di presentazione ([`EIDAS-ARF`_] RPRC_19).
    * - Relying Party Intermediary
      - Presentazione, per conto di una Relying Party intermediata
      - Non agisce come Trust Evaluator nei flussi operativi.
      - Il proprio Wallet-Relying Party Access Certificate associato a quella Relying Party intermediata ([`EIDAS-ARF`_] Reg_34a) e il Wallet-Relying Party Registration Certificate della Relying Party intermediata, inclusi per valore nella richiesta di presentazione ([`EIDAS-ARF`_] RPRC_19).

EUDIW Trust Anchor Validation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Questa sezione specifica il **Trust Anchor Validation Process** che una Wallet Unit o una Wallet-Relying Party utilizza per stabilire l'integrità crittografica e l'autenticità di una List of Trusted Entities, o di una Trusted List, al fine di:

- validare l'affidabilità di un Trust Anchor (vedi :ref:`infrastructure-trust:Trust Anchor Certificate Profile`) per autenticare, autorizzare o validare un'entità o un artifact durante il *runtime*.
- validare le informazioni contenute nella List per *scopi storici*.

A seconda del Trust Artifact o dell'Attestation in verifica, il Trust Evaluator DEVE recuperare, scaricare e validare la List che referenzia il Trust Anchor appropriato:

1. La *List of Trusted Entities* DEVE essere usata per recuperare i Trust Anchor per validare:

   - **WRPAC** nella LoTE dei Provider of WRPAC.
   - **WRPRC** nella LoTE dei Provider of WRPRC.
   - **Wallet Unit Attestation Sign/Seal Certificates** nella LoTE dei Wallet Provider.
   - **PID Sign/Seal Certificates** nella LoTE dei PID Provider.
   - **PuB-EAA Sign/Seal Certificates** nella LoTE dei PuB-EAA Provider.
   - **Registrar Sign/Seal Certificates** nella LoTE dei Registrar.

2. Le *Trusted List* sono usate per recuperare i Trust Anchor per validare:

   - **QEAA Sign/Seal Certificates** nella Trusted List dello Stato membro corrispondente.

3. Per i **PuB-EAA Sign/Seal Certificates**, la Trusted List dello Stato membro corrispondente DEVE essere usata per stabilire lo status qualificato della CA emittente e del certificato. NON DEVE sostituire l'inserimento del Trust Anchor nella LoTE dei PuB-EAA Provider.

Per verificare l'autenticità delle List recuperate, l'Entità DEVE eseguire le seguenti validazioni:

- :ref:`trust-evaluation:List of Trusted Entities Validation`: Validare la firma digitale della List of Trusted Entities verificandola rispetto al certificato del List of Trusted Entities Provider.
  Questo certificato è pubblicato nella Gazzetta ufficiale dell'Unione europea.
- :ref:`trust-evaluation:Trusted List Validation`: Validare la firma digitale della TL verificandola rispetto alle chiavi pubbliche dello Stato membro corrispondente pubblicate nella List Of Trusted Lists (LOTL).
  La List Of Trusted Lists (LOTL) stessa è autenticata validando la sua firma digitale rispetto alla Gazzetta ufficiale dell'Unione europea.

**Input**

L'Entità che valida DEVE basare le decisioni di validazione del Trust Anchor solo su informazioni derivate da:

- La Gazzetta ufficiale dell'UE (OJEU) che ancora la fiducia nei certificati root che hanno firmato le List of Trusted Entities e la List of Trusted Lists.
  La versione corrente dell'OJEU è disponibile `qui <https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ:C_202601944>`_.
- Una List of Trusted Entities o una List of Trusted Lists e le Trusted List a livello di Stato membro validate.

**Esito**

Ciascuna procedura di validazione (definita in :ref:`trust-evaluation:List of Trusted Entities Validation` e :ref:`trust-evaluation:Trusted List Validation`) produce un codice di risultato di verifica granulare quando rileva una condizione negativa.
Questi codici confluiscono nella decisione finale:

- Se gli algoritmi di validazione terminano con:

    - ``LoTE-Status == LoTE_VERIFICATION_PASSED``, o
    - ``LOTL-Status == LOTL_VERIFICATION_PASSED``, o
    - ``EU-TL-Status == EU-TL_VERIFICATION_PASSED``;

    Allora la List of Trusted Entities o la Trusted List è valida e i certificati Trust Anchor (vedi :ref:`infrastructure-trust:Trust Anchor Certificate Profile`) ivi contenuti DEVONO essere considerati affidabili.

- Se gli algoritmi di validazione terminano con:

    - ``LoTE-Status == LoTE_VERIFICATION_FAILED``, o
    - ``LOTL-Status == LOTL_VERIFICATION_FAILED``, o
    - ``EU-TL-Status == EU-TL_VERIFICATION_FAILED``;

    Allora la List of Trusted Entities o la Trusted List non è valida e i certificati Trust Anchor (vedi :ref:`infrastructure-trust:Trust Anchor Certificate Profile`) ivi contenuti NON DEVONO essere considerati affidabili.

.. note::

    All'interno di IT-Wallet, una Wallet Unit è attesa a mettere in cache le List of Trusted Lists, le List of Trusted Entities e le Trusted List degli Stati membri validate, in modo da non recuperarle a ogni interazione.
    La frequenza degli aggiornamenti e i tipi di list da mettere in cache rappresentano un compromesso tra interoperabilità e utilizzo delle risorse.

List Key Rotation and Historical Verification
"""""""""""""""""""""""""""""""""""""""""""""

Per supportare la rotazione continua delle chiavi e gli aggiornamenti regolari, la LoTE e la LOTL implementano un *pivoting mechanism*.
Questo meccanismo consiste nel pubblicare la versione più recente della List all'URI primario referenziato nella Gazzetta ufficiale dell'Unione europea, archiviando le versioni precedenti ad altri URI distinti chiamati *pivot*.
Ciascuna versione della List è firmata con una chiave pubblica referenziata all'interno del pivot immediatamente precedente.
L'ultimo pivot è firmato con la chiave referenziata nell'OJEU.
La versione più recente della List contiene esplicitamente gli URI in cui sono ospitate tutte le versioni storiche.

Un'Entità valida questa catena di pivot dalla versione più recente a quella più vecchia verificando che ciascun artifact successivo sia correttamente firmato dalla chiave pubblica autorizzata nella versione precedente.
La validazione finale è ottenuta verificando l'affidabilità della chiave pubblica più vecchia, tramite una ricerca nell'OJEU oppure direttamente rispetto a una versione della List in cache, precedentemente validata.
Questo assicura che un'entità in possesso dell'ultima versione valida nota possa scoprire in modo affidabile la versione successiva e validarla tramite una catena di fiducia ininterrotta radicata nell'OJEU.

Sebbene il pivoting mechanism consenta aggiornamenti continui dei parametri della LoTE, alcuni aggiornamenti possono richiedere l'aggiunta di un oggetto ``ServiceHistory`` alla LoTE per preservare le chiavi e le configurazioni storiche necessarie a validare le firme legacy.
Gli scenari specifici in cui un aggiornamento di un'Entità innesca una migrazione della sua configurazione in ``ServiceHistory`` sono dettagliati in :ref:`infrastructure-trust:Trust Management and Lifecycle`.

Indipendentemente dall'obiettivo di un'Entità quando valida la LoTE (sia che recuperi una configurazione corrente o storica), il meccanismo di validazione DEVE seguire rigorosamente la Sezione :ref:`trust-evaluation:List of Trusted Entities Validation`.

List of Trusted Entities Validation
"""""""""""""""""""""""""""""""""""

Questa sezione definisce la validazione di una List of Trusted Entities.
La List of Trusted Entities, il suo modello dati e i tipi di List of Trusted Entities usati all'interno dell'ecosistema EUDIW, uno per ciascuna categoria di provider notificato, sono definiti in :ref:`infrastructure-trust:Trusted List, Lists of Trusted Lists, and Lists of Trusted Entities`.

Una List of Trusted Entities è una list firmata.
La sua autenticità è radicata nella Gazzetta ufficiale dell'Unione europea e supporta la rotazione continua delle chiavi attraverso il *pivoting mechanism* descritto in :ref:`trust-evaluation:List Key Rotation and Historical Verification`.
I Trust Anchor che pubblica sono forniti nel ``ServiceDigitalIdentity`` delle sue entry di servizio delle entità fidate, come definito nella clausola 6.6.3 di [`ETSI TS 119 602`_].

La procedura di autenticazione seguente segue la clausola 4.1 di [`ETSI TS 119 615`_], che specifica l'autenticazione della List of Trusted Lists compilata dalla CE (LOTL) con il suo meccanismo di pivot.
Qui tale procedura è applicata al modello dati della List of Trusted Entities di [`ETSI TS 119 602`_] e alla sua firma JAdES ([`ETSI TS 119 182-1`_]), al posto della LOTL XML.
Le variabili usate di seguito sono gli analoghi della List of Trusted Entities delle variabili LOTL preconfigurate nella clausola 4.0 (GPR-4.0-02) di [`ETSI TS 119 615`_].
Corrispondono come segue:

- ``OJEU-LoTE-Loc`` corrisponde a ``OJEU-LOTL-Loc``;
- ``OJEU-LoTE-Certs-Set`` corrisponde a ``OJEU-LOTL-Certs-Set``;
- ``LoTESO-Cert`` corrisponde a ``LOTLSO-Cert``;
- i claim ``PointersToOtherLoTE`` e ``SchemeInformationURI`` corrispondono ai componenti *Pointers to other TSLs* (clausola 6.3.13 di [`ETSI TS 119 602`_]) e *Scheme information URI* (clausola 6.3.7).

**List of Trusted Entities Validation Algorithm**

L'Entità che valida inizializza le seguenti variabili, corrispondenti ai parametri preconfigurati in GPR-4.0-02 di [`ETSI TS 119 615`_] per la LOTL.

**Variabili di Input**:

- ``OJEU-Loc``: URI dell'ultima pubblicazione nota della Gazzetta ufficiale dell'Unione europea.
- ``OJEU-LoTE-Loc``: URI dell'ultima List of Trusted Entities elaborata.
  Il valore predefinito è quello in ``OJEU-Loc``.
- ``OJEU-LoTE-Certs-Set``: l'insieme dei certificati fidati dalla pubblicazione ``OJEU-Loc``.
- ``LoTE``: il JWT della List of Trusted Entities attualmente in elaborazione.
  Inizializzato come ``NULL``.
- ``LoTE-Signer-Cert``: il certificato estratto dal parametro di header ``x5c`` della List of Trusted Entities.
- ``LoTESO-Cert``: variabile temporanea per il certificato del Scheme Operator in validazione.
  Inizializzata come ``NULL``.
- ``LoTESO-Certs-Set``: certificati fidati estratti dal claim ``PointersToOtherLoTE`` (``SchemeTerritory`` ``EU``, clausola 6.3.10 di [`ETSI TS 119 602`_]) di una List of Trusted Entities.

**Variabili di Output**:

- ``Authenticated-LoTE``: il payload JSON validato.
- ``LoTE-Status``: il risultato della validazione (ad es., ``LoTE_VERIFICATION_PASSED``).
- ``LoTE-Sub-Status``: codici di errore dettagliati.

**Processo**:

La validazione DEVE eseguire i seguenti passi.
Ciascun passo indica il requisito corrispondente della clausola 4.1 di [`ETSI TS 119 615`_].

1. (Inizializzazione) Scaricare il file JWT da ``OJEU-LoTE-Loc`` e assegnarlo a ``LoTE``.
   (PRO-4.1.4-01)
2. (Parsing) Estrarre il primo certificato dall'header ``x5c`` di ``LoTE`` e assegnarlo a ``LoTE-Signer-Cert``.
   (PRO-4.1.4-02)
3. (Pivot Discovery) Iterare sui claim ``uriValue`` nel componente ``SchemeInformationURI`` (clausola 6.3.7 di [`ETSI TS 119 602`_]).
   Contare il numero di URI validi che precedono l'URI corrispondente a ``OJEU-Loc`` e assegnarlo a ``n``.
   (PRO-4.1.4-03 per la ricerca di ``OJEU-Loc``, PRO-4.1.4-04 per il conteggio di ``n``)

    - Se nessun URI corrisponde a ``OJEU-Loc``: la validazione DEVE fallire con ``LoTE-Status`` impostato a ``LoTE_VERIFICATION_FAILED`` e ``LoTE-Sub-Status`` impostato a ``OJEU_LOCATION_INPUT_NOT_MATCHING_OJEU_LOCATION_IN_LoTE``.

4. (LoTE Location Conflict) Verificare la condizione ``OJEU-LoTE-Loc != LoTE Location`` AND ``LoTE != Content at LoTE Location``, dove ``LoTE Location`` è l'URI ``LoTELocation`` nel componente ``PointersToOtherLoTE`` di ``LoTE`` con ``SchemeTerritory`` ``EU`` (clausola 6.3.13 di [`ETSI TS 119 602`_]).
   (PRO-4.1.4-05)

    - Se ``TRUE``: la validazione DEVE interrompersi con ``LoTE-Status`` impostato a ``LoTE_VERIFICATION_FAILED`` e ``LoTE-Sub-Status`` impostato a ``LoTE_FILE_CONFLICT``.
    - Se ``FALSE``, procedere al passo successivo.

5. (LoTE Freshness) Verificare la condizione ``OJEU-LoTE-Loc == LoTE Location`` AND ``LoTE != Content at LoTE Location``.
   (PRO-4.1.4-06)

    - Se ``TRUE``: impostare ``OJEU-LoTE-Loc`` a ``LoTE Location`` e ricominciare dal Passo 1.
    - Se ``FALSE``, procedere al passo successivo.

6. (Digital Signature Validation) Validare la firma della ``LoTE`` corrente usando la chiave pubblica da ``LoTE-Signer-Cert`` come certificato direttamente fidato, seguendo la validazione di firma di base di [`ETSI EN 319 102-1`_] come richiesto da PRO-4.1.4-07.
   In particolare, i campi *Country code* e *Organization* nel Subject Distinguished Name del certificato che supporta la firma digitale AdES devono corrispondere rispettivamente al scheme territory e a uno dei valori del scheme operator name all'interno della LoTE.
   (PRO-4.1.4-07, PRO-4.1.4-08, clausola 6.8.0 di [`ETSI TS 119 602`_])

    - Se la validazione fallisce: interrompere con ``LoTE-Status`` impostato a ``LoTE_VERIFICATION_FAILED`` e ``LoTE-Sub-Status`` impostato a ``LoTE_SIGNATURE_VERIFICATION_FAILED``.
    - Se ha successo:

        - Impostare ``LoTESO-Cert`` a ``LoTE-Signer-Cert``.
        - Impostare ``LoTESO-Certs-Set`` ai certificati trovati nel claim ``PointersToOtherLoTE`` (scheme territory ``EU``) del payload della ``LoTE`` corrente.
          (PRO-4.1.4-09)

7. (Intermediate Pivot Validation) (PRO-4.1.4-10 per il caso ``n = 0``, PRO-4.1.4-11 per il ciclo sui pivot)

    - Caso ``n = 0`` (Nessun Pivot): procedere direttamente al Passo 8.
    - Caso ``n != 0`` (Catena Storica):

        - Iterare ``i`` da 1 a ``n`` (dal Pivot più recente al più vecchio).
          Sia ``Pivot`` il file scaricato dall'``i``-esimo URI.
        - (Link Check) Impostare ``Pivot-Certs-Set`` ai certificati nel claim ``PointersToOtherLoTE`` (territory ``EU``) di ``Pivot``.
          Se ``LoTESO-Cert`` (il firmatario del file precedente nella catena) non è in ``Pivot-Certs-Set``, la validazione DEVE fallire con ``LoTE-Sub-Status`` impostato a ``PIVOT_i-1_SIGNER_CERT_NOT_AUTHENTICATED_BY_PIVOT_i``.
        - (Update Signer) Impostare ``LoTESO-Cert`` al primo certificato nel parametro di header ``x5c`` di ``Pivot``.
        - (Verify Signature) Validare la firma di ``Pivot`` usando ``LoTESO-Cert`` come descritto nel passo 6.
          (Digital Signature Validation).
          Se fallisce, la validazione DEVE fallire con ``LoTE-Status`` impostato a ``LoTE_VERIFICATION_FAILED`` e ``LoTE-Sub-Status`` impostato a ``PIVOT_i_SIGNATURE_VERIFICATION_FAILED``.
        - Il ciclo continua, procedendo a ritroso fino a quando ``LoTESO-Cert`` rappresenta il firmatario del Pivot più vecchio.

8. (Trust Root Validation) Verificare la fine della catena.
   Se ``LoTESO-Cert`` (dall'ultimo Pivot, o dalla ``LoTE`` corrente quando non esiste alcun Pivot) non è in ``OJEU-LoTE-Certs-Set`` (l'insieme dei certificati fidati), la validazione DEVE fallire con ``LoTE-Sub-Status`` impostato a ``PIVOT_n_SIGNER_CERT_NOT_AUTHENTICATED_BY_OJEU``.
   (PRO-4.1.4-12)

9. (Expiration) Se l'ora corrente è maggiore del valore ``NextUpdate`` di ``LoTE``, oppure è impostato a ``NULL`` (clausola 6.3.15 di [`ETSI TS 119 602`_]), la validazione DEVE fallire.
   (PRO-4.1.4-13)

10. (Success) Impostare ``Authenticated-LoTE`` a ``LoTE`` e ``LoTE-Status`` a ``LoTE_VERIFICATION_PASSED``.
    (PRO-4.1.4-14, PRO-4.1.4-15)

11. (Update Bookmark) Se ``OJEU-LoTE-Loc`` non corrisponde alla ``LoTE Location`` in ``Authenticated-LoTE`` (scheme territory ``EU``), aggiornare ``OJEU-LoTE-Loc`` a tale valore.
    (PRO-4.1.4-16)

12. (Update Trust Root) [Attenzione: questo passo modifica la configurazione del Root of Trust] (PRO-4.1.4-17)

    - Se ``OJEU-Loc`` non corrisponde al primo URI in ``SchemeInformationURI``, aggiornare ``OJEU-LoTE-Loc``.
    - Aggiornare ``OJEU-LoTE-Certs-Set`` in base al nuovo insieme di certificati fidati, sia in ``Authenticated-LoTE`` sia da una nuova pubblicazione della Gazzetta ufficiale dell'Unione europea.

.. note::

    - I passi 4, 5 e 11 consentono di modificare la location del file della List of Trusted Entities senza cambiare la chiave pubblica del firmatario fidato iniziale, purché sia la vecchia sia la nuova location abbiano lo stesso contenuto, altrimenti la validazione fallisce con ``LoTE_FILE_CONFLICT``.
      Questo consente di recuperare la List of Trusted Entities da location diverse senza influire sulla validazione del Trust Anchor, purché il contenuto sia lo stesso.
    - In caso di errore ``OJEU_LOCATION_INPUT_NOT_MATCHING_OJEU_LOCATION_IN_LoTE``, è probabile che la pubblicazione della Gazzetta ufficiale dell'Unione europea sia stata aggiornata con una nuova location per la List of Trusted Entities.
      L'Entità che valida DOVREBBE ripetere il processo di validazione dopo aver scaricato la versione più recente della Gazzetta ufficiale dell'Unione europea.
    - Nel passo 8, l'Entità che valida stabilisce il binding del certificato firmatario della ``LoTE`` con il certificato referenziato nella Gazzetta ufficiale dell'Unione europea, usando di fatto quest'ultima come fonte di certificati fidati.

Di seguito un diagramma di flusso che sintetizza i passi precedenti per la validazione della List of Trusted Entities:

.. plantuml:: plantuml/lote-val-alg.puml
    :width: 99%
    :alt: La figura illustra il diagramma di flusso dell'algoritmo di validazione della List of Trusted Entities.
    :caption: Diagramma di flusso dell'algoritmo di validazione della List of Trusted Entities.

Di seguito sono elencati i codici di errore Sub-Status della List of Trusted Entities in formato tabellare.

.. list-table:: Codici di Errore Sub-Status della List of Trusted Entities
   :class: longtable
   :widths: 38 10 52
   :header-rows: 1

   * - **Code**
     - **Fase**
     - **Significato**
   * - ``OJEU_LOCATION_INPUT_NOT_MATCHING_OJEU_LOCATION_IN_LoTE``
     - both
     - Nessun URI corrisponde all'``OJEU-Loc`` atteso all'interno del ``SchemeInformationURI`` della List of Trusted Entities.
       Ciò implica tipicamente che è disponibile una versione più recente della pubblicazione della Gazzetta ufficiale dell'Unione europea.
   * - ``LoTE_FILE_CONFLICT``
     - both
     - È rilevato un conflitto di location in cui la location tracciata della List of Trusted Entities differisce da quella attiva, e il contenuto di questi file non corrisponde.
   * - ``LoTE_SIGNATURE_VERIFICATION_FAILED``
     - both
     - La validazione della firma del file corrente della List of Trusted Entities è fallita usando il certificato firmatario estratto, indicando un potenziale manomissione o corruzione.
   * - ``PIVOT_i-1_SIGNER_CERT_NOT_AUTHENTICATED_BY_PIVOT_i``
     - both
     - La catena storica di fiducia è interrotta perché il certificato di firma del pivot o file precedente (i-1) non è trovato nell'insieme di certificati fidati del pivot successivo (i).
   * - ``PIVOT_i_SIGNATURE_VERIFICATION_FAILED``
     - both
     - La validazione della firma è fallita per un file pivot intermedio (i) all'interno della catena storica.
   * - ``PIVOT_n_SIGNER_CERT_NOT_AUTHENTICATED_BY_OJEU``
     - both
     - Il certificato finale alla radice della catena di pivot, o il firmatario della List of Trusted Entities corrente quando non esiste alcun pivot, non è trovato nell'insieme di certificati fidati ``OJEU-LoTE-Certs-Set``.

Trusted List Validation
""""""""""""""""""""""""

Questa sezione definisce la validazione della Trusted List.
Per validare la Trusted List, l'Entità che valida DEVE:

1. Validare la List of Trusted Lists dell'UE usando l'algoritmo descritto nella sezione 4.1 di [`ETSI TS 119 615`_].
   Se questo fallisce, la validazione si interrompe e la Wallet Unit DEVE considerare l'Entità con cui sta interagendo come non fidata.
   Il processo di validazione è analogo a :ref:`trust-evaluation:List of Trusted Entities Validation` eccetto per il formato della LOTL che è sempre XML.
2. Analizzare la List of Trusted Lists dell'UE validata per scoprire il certificato necessario a validare la Trusted List dello Stato membro rilevante.
3. Ottenere e validare la Trusted List rilevante come descritto nella sezione 4.2 di [`ETSI TS 119 615`_].

X509 Certificate Chain Validation Algorithm
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Questa procedura valida il certification path.
È invocata da :ref:`trust-evaluation:EUDIW Authentication` e da :ref:`trust-evaluation:Authorization Artifacts Validation` per validare le catene del Wallet-Relying Party Access Certificate, del Wallet-Relying Party Registration Certificate e del Registrar Sign/Seal Certificate.
Il Trust Anchor consumato come ``trust_anchor`` è profilato in :ref:`infrastructure-trust:Trust Anchor Certificate Profile`.

La validazione del certification path è la path validation X.509 standard definita in :rfc:`5280#section-6`, con il controllo dello status di revoca definito in :rfc:`5280` e :rfc:`6960`.
Il ciclo di vita dei certificati e i meccanismi di revoca, inclusi i formati e i parametri di CRL e OCSP, sono definiti in :ref:`infrastructure-trust:Revocation Mechanisms`.
I dettagli dell'algoritmo non sono ridefiniti qui.
Questa è la stessa validazione del certification path usata nel Trust Framework Nazionale (vedi :ref:`trust-evaluation:X.509 Certificate Chain Validation`), dove la differenza è l'origine del trust anchor e l'estrazione aggiuntiva del Federation Entity Identifier.

All'interno del Trust Framework EUDIW si applica quanto segue.

  - Il ``trust_anchor`` è il certificato fidato ottenuto dal componente ``ServiceDigitalIdentity`` della List of Trusted Entities (vedi :ref:`trust-evaluation:List of Trusted Entities Validation`) o della Trusted List (vedi :ref:`trust-evaluation:Trusted List Validation`) applicabile e validata, cioè la LoTE dei Provider of WRPAC per il Wallet-Relying Party Access Certificate, la LoTE dei Provider of WRPRC per il Wallet-Relying Party Registration Certificate, e la LoTE dei Registrar per il Registrar Sign/Seal Certificate.
  - Il controllo dello status di revoca PUÒ essere omesso per un certificato che reca entrambe le estensioni ``noRevAvail`` e ``ETSIValAssuredCertMod`` (vedi :ref:`infrastructure-trust:Wallet-Relying Party Access Certificate (WRPAC) Profile`), il cui status è allora determinato unicamente dal suo periodo di validità.

.. note::

  Come definito in :ref:`infrastructure-trust:Revocation Trust Anchors`, il Trust Anchor recuperato dalla LoTE o dalla Trusted List applicabile è il Trust Anchor notificato per la catena di certificati corrispondente. Lo stesso Trust Anchor DEVE essere usato per validare le firme delle CRL o delle risposte OCSP usate per il controllo di revoca, come specificato in :rfc:`5280#section-6` e :rfc:`6960`.

**Input**

- ``path``: la sequenza di ``n`` certificati ``C_1, ..., C_n`` fornita dall'Entità, dove ``C_1`` è il primo certificato della catena e ``C_n`` è il certificato end-entity.
  Per ogni ``i`` in ``1, ..., n-1``, ``C_i`` è l'issuer di ``C_i+1``.
- ``trust_anchor``: il certificato fidato ottenuto dal ``ServiceDigitalIdentity`` della List of Trusted Entities o della Trusted List validata.
  DEVE contenere la chiave pubblica usata per firmare ``C_1``.
  Le implementazioni DEVONO supportare sia certificati Trust Anchor self-signed sia non self-signed.
- ``current_time``: la data e l'ora correnti.

**Esito**

- Il certificato end-entity validato ``C_n``, oppure un fallimento.

**Processo**

1. Costruire il certification path dal certificato end-entity ``C_n`` al ``trust_anchor``.
2. Eseguire la path validation definita in :rfc:`5280#section-6`, usando il ``trust_anchor`` come input trust anchor dell'algoritmo e ``current_time`` come tempo di validazione.
3. Verificare lo status di revoca dei certificati nel path secondo :rfc:`5280` e :rfc:`6960`, a meno che il controllo non sia omesso come descritto sopra.

Se un qualsiasi passo fallisce, il certification path DEVE essere considerato non valido e la firma dell'artifact NON DEVE essere verificata con la catena di certificati presentata.

EUDIW Attestation Signature Validation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Questo processo valida la firma su un'Attestation (Attestato Elettronico o Wallet Instance Attestation) usando il Sign/Seal Certificate appropriato come profilato in :ref:`infrastructure-trust:Entity Sign/Seal Certificate Profile`.
È invocato durante i flussi di emissione e presentazione per validare la firma sull'Attestation.

Il processo DEVE essere strutturato come segue:

- Se l'Attestation la cui firma è in verifica è un Attestato Elettronico avente un Trust Anchor referenziato all'interno di una LoTE o di una Trusted List (cioè un PID, una PuB-EAA, una QEAA), oppure è una Wallet Instance Attestation, allora si applica uno dei seguenti casi:

  - **Base Signature Validation**: Eseguita quando l'Attestation contiene il Sign/Seal Certificate e la catena di fiducia X.509 associata, e il Trust Anchor è presente nella LoTE rilevante (solo per PID, WIA o PuB-EAA) o nella Trusted List (solo per QEAA).

  - **Fallback Signature Validation**: Eseguita quando l'Attestation non contiene il Sign/Seal Certificate, che è invece attestato direttamente come Trust Anchor nella LoTE (solo per PID o WIA).

- Se l'Attestation la cui firma è in verifica è una EAA non qualificata, allora le informazioni relative alla trust evaluation sono governate dal Rulebook corrispondente.

La **Base Signature Validation** è strutturata come segue:

**Input**

- L'Attestation ricevuta e la catena di certificati del firmatario ivi contenuta.
- Il tipo di artifact (cioè, il tipo di Attestato Elettronico o Wallet Instance Attestation) usato per selezionare la List of Trusted Entities o la Trusted List applicabile.

**Esito**

- L'Attestation validata, oppure un fallimento di validazione.

**Processo**

Questo processo dipende dal tipo di Attestation:

- **PID** o **WIA**.
  
  1. Verificare la firma dell'Attestation con il certificato Sign/Seal fornito nell'Attestation.
  2. Selezionare la List of Trusted Entities applicabile in base al tipo dell'Attestation ricevuta, validarla come definito in :ref:`trust-evaluation:List of Trusted Entities Validation`, ed estrarre il Trust Anchor appropriato dal campo ``ServiceDigitalIdentity`` dell'Entità rilevante.
  3. Estrarre la catena del certificato Sign/Seal dall'Attestation e validarla rispetto al Trust Anchor ottenuto, come definito in :ref:`trust-evaluation:X509 Certificate Chain Validation Algorithm`.

- **QEAA**.

  1. Verificare la firma dell'Attestation usando il certificato Sign/Seal fornito nell'Attestation. Per una QEAA, la firma o il sigillo elettronico qualificato DEVE essere validato in conformità all'Articolo 32 di [`EIDAS`_].
  2. Recuperare la Trusted List appropriata in base alla nazionalità del Credential Issuer, validarla come definito in :ref:`trust-evaluation:Trusted List Validation`, ed estrarre il Trust Anchor appropriato dal campo ``ServiceDigitalIdentity`` dell'Entità rilevante.
  3. Estrarre la catena di certificati del firmatario dall'Attestation e validarla rispetto al Trust Anchor ottenuto, come definito in :ref:`trust-evaluation:X509 Certificate Chain Validation Algorithm`.

- **PuB-EAA**.

  1. Verificare la firma dell'Attestation con il Sign/Seal Certificate fornito nell'Attestation. Una firma elettronica qualificata DEVE essere validata in conformità all'Articolo 32 di [`EIDAS`_]; ove il Provider sia una persona giuridica che usa un sigillo elettronico, si applicano gli Articoli 37 e 40.
  2. Recuperare e validare la LoTE dei PuB-EAA Provider come definito in :ref:`trust-evaluation:List of Trusted Entities Validation`, abbinare il Provider e il suo Sign/Seal Certificate con l'oggetto ``TrustedEntityList`` rilevante, ed estrarre il suo Trust Anchor.
  3. Estrarre la catena di certificati del firmatario dall'Attestation e validarla rispetto al Trust Anchor ottenuto dalla LoTE, come definito in :ref:`trust-evaluation:X509 Certificate Chain Validation Algorithm`.
  4. Recuperare la Trusted List dello Stato membro corrispondente alla CA emittente, validarla come definito in :ref:`trust-evaluation:Trusted List Validation`, e stabilire lo status qualificato della CA emittente e del Sign/Seal Certificate.

.. note:: 

  In ciascuno dei casi precedenti, per un'Attestation in formato mdoc, il Mobile Security Object reca il certificato Document Signer nell'header ``x5chain``, come definito in [`ISO18013-5`_]. Per un'Attestation in formato SD-JWT VC, la catena di certificati dell'issuer è recata nell'header ``x5c`` della firma JOSE.

Se la **Base Signature Validation** risulta in un fallimento, l'Entità che valida l'Attestation DEVE eseguire la **Fallback Signature Validation** come segue:

.. warning::
  
  Questo processo si applica solo ai tipi di Attestation **PID** e **WIA**.

**Input**

- L'Attestation ricevuta.
- Il tipo di artifact (cioè, il tipo di Attestato Elettronico o Wallet Instance Attestation) usato per selezionare la List of Trusted Entities applicabile.

**Esito**

- L'Attestation validata, oppure un fallimento di validazione.

**Processo**

1. Recuperare la List of Trusted Entities applicabile in base al tipo di Attestation, validarla come definito in :ref:`trust-evaluation:List of Trusted Entities Validation`, ed estrarre il Trust Anchor appropriato dal campo ``ServiceDigitalIdentity`` dell'Entità rilevante.
2. Verificare la firma dell'Attestation direttamente usando il Trust Anchor validato che agisce come certificato firmatario.

.. warning::

   Sebbene la specifica IT Wallet richieda che i certificati Trust Anchor notificati alla Commissione e inclusi nella LoTE siano *diversi* dai Sign/Seal Certificate delle Entità correlate, la Clausola 4.2 di [`ETSI TS 119 412-6`_] consente ai Trust Anchor della LoTE di servire direttamente come Sign/Seal Certificate.
   In questo caso, tali certificati NON DEVONO essere inclusi nell'Attestation, costringendo il processo di verifica ad attenersi alla procedura di **Fallback Signature Validation**.
   Per assicurare l'interoperabilità, le implementazioni di EUDIW Attestation Signature Validation DEVONO supportare entrambi i meccanismi di validazione.

.. note::

  Quando si verificano firme o sigilli realizzati da chiavi storiche, si applica lo stesso processo con la seguente differenza: il Trust Anchor è recuperato dall'elemento `ServiceHistory.ServiceDigitalIdentity` invece che dall'elemento `ServiceInformation.ServiceDigitalIdentity`.

Se sia la **Base Signature Validation** sia la **Fallback Signature Validation** falliscono, l'Attestation NON DEVE essere considerata emessa da un'Entità fidata.

EUDIW Authentication
^^^^^^^^^^^^^^^^^^^^

Il Processo di Autenticazione consente alla Wallet Unit di autenticare una Wallet-Relying Party durante un'interazione.
Stabilisce la fiducia validando la catena di certificati X.509 della Wallet-Relying Party, da un Provider of Wallet-Relying Party Access Certificate fidato fino al Wallet-Relying Party Access Certificate presentato, verificando che il certificato di accesso includa almeno un Signed Certificate Timestamp valido, e verificando che la Wallet-Relying Party possieda la corrispondente chiave privata.
Il Wallet-Relying Party Access Certificate è profilato in :ref:`infrastructure-trust:Wallet-Relying Party Access Certificate (WRPAC) Profile`.

Per la verifica del certificato di accesso, la Wallet Unit DEVE accettare solo i Trust Anchor pubblicati nelle List of Trusted Entities dei Provider of Wallet-Relying Party Access Certificate notificati dagli Stati membri (vedi :ref:`trust-evaluation:List of Trusted Entities Validation`).

**Input**

L'esito dell'Autenticazione DEVE basarsi solo su informazioni derivate da:

- il Trust Anchor appropriato ottenuto da un'istanza valida della List of Trusted Entities dei Provider of Wallet-Relying Party Access Certificate;
- il path di certificati X.509 che termina con il certificato end-entity del Wallet-Relying Party Access Certificate;
- almeno un Signed Certificate Timestamp incorporato in tale certificato e verificato come specificato in :rfc:`9162`;
- una firma della Wallet-Relying Party sull'artifact dell'interazione, recante la prova di possesso della chiave privata referenziata nel Wallet-Relying Party Access Certificate.

**Esito**

La Wallet Unit DEVE produrre una decisione: la Wallet-Relying Party è ``AUTHENTICATED`` oppure ``NON_AUTHENTICATED``.
Se ``AUTHENTICATED``, la Wallet Unit procede nel flusso di interazione.
Se ``NON_AUTHENTICATED``, la Wallet Unit DEVE informare l'Utente che l'identità della Wallet-Relying Party non ha potuto essere verificata e DEVE interrompere l'interazione, poiché l'entità non è affidabile.

**Processo**

La Wallet Unit DEVE verificare l'autenticità e l'integrità del Wallet-Relying Party Access Certificate presentato come segue:

1. **Retrieve the Trust Anchor**: ottenere l'entry del Provider of Wallet-Relying Party Access Certificate dalla List of Trusted Entities validata (vedi :ref:`trust-evaluation:List of Trusted Entities Validation`).
   Per selezionare l'entry corretta, abbinare l'``issuer.organizationIdentifier`` del primo certificato della catena, la cui semantica è definita nella clausola 5.1.4 di [`ETSI EN 319 412-1`_], con il ``TrustedEntitiesList[].TrustedEntity.TETradeName`` della List of Trusted Entities.
   I certificati nel campo ``TrustedEntityServices[].ServiceInformation.ServiceDigitalIdentity`` costituiscono il Trust Anchor.

2. **Construct the Certification Path**: costruire un path a partire dal Wallet-Relying Party Access Certificate presentato dalla Wallet-Relying Party (``C_1``) e terminante con il certificato emesso dal Provider of Wallet-Relying Party Access Certificate (``C_n``).
   Il path più semplice consiste in un singolo certificato, dove ``n = 1``.

3. **Execute Path Validation**: validare il certification path come definito in :ref:`trust-evaluation:X509 Certificate Chain Validation Algorithm`, usando il Trust Anchor recuperato al passo 1, come descritto in :ref:`trust-evaluation:Wallet-Relying Party Access Certificate Validation`.

4. **Verify Certificate Transparency**: verificare che il Wallet-Relying Party Access Certificate validato includa almeno un Signed Certificate Timestamp valido come specificato in :rfc:`9162` ([`EIDAS-ARF`_] CT_05).
   Questa verifica si applica quando si autentica una Wallet-Relying Party durante l'emissione di PID o attestation e durante la presentazione.
   Se il certificato non include un Signed Certificate Timestamp valido, la Wallet Unit DEVE produrre ``NON_AUTHENTICATED`` e DEVE interrompere l'interazione ([`EIDAS-ARF`_] CT_06, RPA_06a).

5. **Verify the Signature**: usare la chiave pubblica del Wallet-Relying Party Access Certificate validato per verificare la firma della Wallet-Relying Party sull'artifact che firma nella specifica interazione.
   La catena di certificati e l'artifact firmato dipendono dal flusso:

    - **Remote Flow**: la catena è recata nell'header ``x5c`` del Request Object firmato dalla Wallet-Relying Party, e la Relying Party è autenticata attraverso il Client Identifier Prefix ``x509_hash``, come definito in [`OpenID4VP`_] e [`OPENID4VC-HAIP`_].
    - **Proximity Flow**: la catena è recata nell'mdoc reader authentication (``ReaderAuth``) firmata dalla Wallet-Relying Party, nell'header COSE ``x5chain`` (label ``33``), come definito in [`ISO18013-5`_].
    - **Issuance Flow**: la catena è recata nell'header ``x5c`` dei Metadata del Credential Issuer firmati dalla Wallet-Relying Party, come definito in [`OpenID4VCI`_].

.. warning::

    Una Wallet-Relying Party DEVE distinguere tra autenticazione transitoria (ad es., controllo di accesso) e impegno sul contenuto (non ripudio).
    Per impedire a un attaccante di mascherare un impegno legale come un nonce di protocollo, la Wallet-Relying Party NON DEVE usare la chiave privata del Wallet-Relying Party Access Certificate per firmare dati arbitrari che potrebbero essere controllati da una parte esterna.

Wallet-Relying Party Access Certificate Validation
"""""""""""""""""""""""""""""""""""""""""""""""""""

L'Entità che esegue la validazione del Wallet-Relying Party Access Certificate inizializza l'algoritmo in :ref:`trust-evaluation:X509 Certificate Chain Validation Algorithm` con il ``path`` e il ``trust_anchor`` ivi definiti.
Gli input sono i seguenti:

- ``C_n`` è il primo certificato della catena fornita dalla Wallet-Relying Party;
- ``C_1`` è il Wallet-Relying Party Access Certificate;
- ``trust_anchor`` è un certificato del Provider of Wallet-Relying Party Access Certificate ottenuto dalla List of Trusted Entities.

.. warning::

  Come descritto nella Sezione 6.1.1 di `OPENID4VC-HAIP`_ il Trust Anchor Certificate necessario per la validazione del WRPAC NON DEVE essere incluso nella catena di certificati e DEVE essere sempre recuperato nella LoTE appropriata.

EUDIW Authorization
^^^^^^^^^^^^^^^^^^^

Questa sezione specifica il Processo di Autorizzazione EUDIW che una Wallet Unit DEVE eseguire per determinare se un'interazione con una Wallet-Relying Party è consentita all'interno dell'ecosistema EUDI Wallet.
Il Processo di Autorizzazione EUDIW DEVE iniziare solo *dopo* che la Wallet-Relying Party è stata autenticata con successo secondo :ref:`trust-evaluation:EUDIW Authentication`.
Se la Wallet-Relying Party non è stata autenticata, il Processo di Autorizzazione EUDIW NON DEVE iniziare.

I dati di autorizzazione di una Wallet-Relying Party sono recati dal Wallet-Relying Party Registration Certificate.
Durante la Presentazione di Credenziali il Wallet-Relying Party Registration Certificate DEVE essere incluso per valore nella richiesta ([`EIDAS-ARF`_] RPRC_19) ed è l'unica fonte autorevole per l'autorizzazione alla presentazione ([`EIDAS-ARF`_] RPRC_17, RPRC_21).
Durante l'Emissione di Credenziali un PID Provider o un Attestation Provider DEVE includere il Wallet-Relying Party Registration Certificate del Servizio applicabile per valore nei Metadata del Credential Issuer ([`EIDAS-ARF`_] RPRC_22).

Il Processo di Autorizzazione EUDIW è suddiviso in:

- :ref:`trust-evaluation:Authorization Artifacts Validation`, che valida l'integrità e l'autenticità del Trust Artifact recante i dati di autorizzazione; e
- :ref:`trust-evaluation:Authorization Validation`, che valida il contenuto informativo dell'artifact validato.
  In particolare questa validazione copre:

    - **Autorizzazione all'emissione**: determina se un Credential Issuer è registrato per il ruolo rilevante e autorizzato a emettere lo specifico Attestato Elettronico.
      Questo si applica ai PID, QEAA, PuB-EAA e EAA Provider che operano all'interno dell'ecosistema EUDIW.
    - **Autorizzazione alla presentazione**: determina se una richiesta di Relying Party ricade nel suo ambito registrato, se un'Embedded Disclosure Policy consente la disclosure, e se l'Utente approva.
      Questo si applica alle interazioni che coinvolgono sia Relying Party sia Relying Party Intermediary, sia nel Remote Flow sia nel Proximity Flow.

- :ref:`trust-evaluation:Authorization Decision and Override Rules`, che produce una *Authorization Decision* espressa come ``AUTHORIZED`` o ``NOT_AUTHORIZED`` sulla base dei risultati di Authorization Artifacts Validation e Authorization Validation.
  A seconda del tipo di Flow l'Utente PUÒ *sovrascrivere* la Authorization Decision.

All'interno della *Authorization Validation*, la Wallet Unit DEVE distinguere tra la Wallet-Relying Party autenticata e l'*Authorization Subject*, cioè l'entità la cui autorizzazione è in valutazione:

- Durante l'Emissione, l'Authorization Subject è il Credential Issuer.
- Durante la presentazione *diretta*, l'Authorization Subject è la Relying Party.
- Durante la presentazione *intermediata*, la Wallet-Relying Party autenticata è il Relying Party Intermediary, mentre l'Authorization Subject per la richiesta di dati è la *Relying Party intermediata*, il cui ambito registrato governa la richiesta.
  Il Relying Party Intermediary è esso stesso un'entità registrata, e la sua autorizzazione ad agire come intermediario è stabilita attraverso il binding ``intermediary`` dichiarato nei dati di autorizzazione della Relying Party intermediata (vedi la Binding verification di seguito).

La Wallet Unit DEVE supportare la risoluzione del contesto di autorizzazione dal Wallet-Relying Party Registration Certificate incluso nell'interazione.
La Wallet Unit NON DEVE interrogare il Register come sostituto di un Wallet-Relying Party Registration Certificate mancante o non valido durante la Presentazione di Credenziali ([`EIDAS-ARF`_] RPRC_16, RPRC_18 e RPRC_19a sono vuoti) o durante l'Emissione di Credenziali ([`EIDAS-ARF`_] RPRC_22 e RPRC_22a).

Authorization Artifacts Validation
"""""""""""""""""""""""""""""""""""

Il Wallet-Relying Party Registration Certificate reca i dati di autorizzazione di un'entità, nei profili JWT e CWT definiti nella Sezione 5.2.1 di [`ETSI TS 119 475`_].

Ciascuna procedura di validazione specifica i propri input, la propria logica di elaborazione e il proprio output, un codice di risultato di verifica.
Il risultato PUÒ essere sovrascritto dall'Utente alle condizioni dettagliate in :ref:`trust-evaluation:Authorization Decision and Override Rules`.

Il flusso di validazione dipende dall'interazione.

- Durante il flusso di Presentazione la Relying Party DEVE convogliare il Wallet-Relying Party Registration Certificate per valore ([`EIDAS-ARF`_] RPRC_19):

    - come elemento ``registration_cert`` del parametro ``verifier_info`` del Request Object, nel Remote Flow, come definito in [`ETSI TS 119 472-2`_] e nella Sezione 5.1 di [`OpenID4VP`_];
    - nel membro ``euWrprc`` di ``requestInfo`` nell'ISO ``DeviceRequest``, nel Proximity Flow, come definito nella Sezione 5.3 di [`ETSI TS 119 472-2`_] e in [`ISO18013-5`_].

  Un elemento ``registrar_dataset`` PUÒ essere presente per pubblicazione e trasparenza. NON DEVE essere usato come sostituto del Wallet-Relying Party Registration Certificate durante la presentazione ([`EIDAS-ARF`_] RPRC_19a è vuoto).

- Durante il flusso di Emissione un PID Provider o un Attestation Provider DEVE convogliare il Wallet-Relying Party Registration Certificate per valore nei Metadata del Credential Issuer ([`EIDAS-ARF`_] RPRC_22), attraverso l'array ``issuer_info``, come definito nella Sezione 4.2.3 di [`ETSI TS 119 472-3`_].
  L'array DEVE contenere un elemento ``registration_cert`` con il Wallet-Relying Party Registration Certificate per valore, e DEVE contenere un elemento ``registrar_dataset`` con le informazioni di registrazione.
  Il ``registrar_dataset`` PUÒ essere usato solo come informazione consultiva. NON DEVE essere presentato all'Utente come verificato e NON DEVE essere usato come sostituto del Wallet-Relying Party Registration Certificate ([`EIDAS-ARF`_] RPRC_22).
  L'Embedded Disclosure Policy è distribuita attraverso i Metadata del Credential Issuer all'interno del campo ``credential_configurations_supported``, come definito in [`OpenID4VCI`_].

Durante la Presentazione di Credenziali, se il Wallet-Relying Party Registration Certificate non è disponibile o la sua validazione fallisce, la Wallet Unit DEVE impostare ``authz_art_state`` a ``CERTIFICATE_INVALID`` e DEVE avvisare l'Utente ([`EIDAS-ARF`_] RPRC_17).
La Wallet Unit NON DEVE interrogare il Register come fallback ([`EIDAS-ARF`_] RPRC_16 e RPRC_18 sono vuoti).

Durante l'Emissione di Credenziali, se il Wallet-Relying Party Registration Certificate non è disponibile o la sua validazione fallisce, la Wallet Unit DEVE impostare ``authz_art_state`` a ``CERTIFICATE_INVALID``, DEVE avvisare l'Utente che non ha potuto ottenere o validare le informazioni registrate, e NON DEVE richiedere l'emissione di un PID o di un'attestation ([`EIDAS-ARF`_] RPRC_22a).
La Wallet Unit NON DEVE interrogare il Register come fallback ([`EIDAS-ARF`_] RPRC_22).

**Wallet-Relying Party Registration Certificate Validation**

Quando un Wallet-Relying Party Registration Certificate è disponibile, la Wallet Unit DEVE validarlo prima di farvi affidamento:

1. **Format verification**: confermare che ``typ`` è ``rc-wrp+jwt`` nel Remote Flow e durante l'Emissione di Credenziali, oppure ``rc-wrp+cwt`` nel Proximity Flow, come definito nella Sezione 5.2.1 di [`ETSI TS 119 475`_].
2. **Algorithm verification**: verificare che l'algoritmo di firma sia conforme, cioè che ``alg`` non sia né ``none`` né un algoritmo deprecato.
3. **Signature validation**: verificare che la firma del Wallet-Relying Party Registration Certificate sia valida.
4. **Trust Anchor validation**: validare la LoTE dei Provider of WRPRC (vedi :ref:`trust-evaluation:List of Trusted Entities Validation`) e recuperare il Trust Anchor dal suo campo ``TrustedEntitiesList.ServiceDigitalIdentity``.
5. **Path validation**: validare la catena del Wallet-Relying Party Registration Certificate come definito in :ref:`trust-evaluation:X509 Certificate Chain Validation Algorithm`, usando il ``trust_anchor`` ottenuto nel passo precedente. Per il WRPRC, il Trust Anchor usato per la validazione della firma, la validazione del certificate path e il controllo di revoca DEVE essere recuperato dall'entry di servizio applicabile nella LoTE dei Provider of WRPRC (cioè, sotto il ``ServiceDigitalIdentity`` corrispondente al ``ServiceTypeIdentifier`` con valore ``http://uri.etsi.org/19602/SvcType/WRPRC/Issuance``).
6. **Temporal validity**: controllare ``iat`` e ``exp`` se presenti.
7. **Status verification**: controllare lo status di revoca attraverso il campo ``status`` del Wallet-Relying Party Registration Certificate, come definito in [`ETSI TS 119 475`_]:

   - recuperare la SLT (vedi :ref:`infrastructure-trust:Token Status List (WRPRC Profile)`) all'URI specificato dal membro ``status.status_list.uri`` del WRPRC;
   - validare la catena del certificato di firma della SLT come definito in :ref:`trust-evaluation:X509 Certificate Chain Validation Algorithm`, usando il Trust Anchor recuperato dall'entry di servizio applicabile nella LoTE dei Provider of WRPRC (cioè, sotto il ``ServiceDigitalIdentity`` corrispondente al ``ServiceTypeIdentifier`` con valore ``http://uri.etsi.org/19602/SvcType/WRPRC/Revocation`` per il servizio fornito dal Provider of WRPRC);
   - validare la firma della SLT usando la catena del certificato di firma validata, seguendo :ref:`trust-evaluation:EUDIW Attestation Signature Validation`;
   - validare il modello dati della SLT secondo :ref:`infrastructure-trust:Token Status List (WRPRC Profile)`;
   - decomprimere il valore ``status_list.lst``, recuperare l'entry a un bit corrispondente al membro ``status.status_list.idx`` del WRPRC, e interpretare ``0x00`` come ``VALID`` e ``0x01`` come ``INVALID``.

8. **Consistency check**: verificare che il subject e i campi del Wallet-Relying Party Registration Certificate siano coerenti con l'interazione.

.. note::

   Nel Passo 5 (**Path validation**), il Trust Anchor Certificate necessario per validare il WRPRC NON DEVE essere incluso nella catena di certificati e DEVE essere sempre recuperato dalla LoTE appropriata.

**Esito**

- Se tutti i passi hanno successo e il Wallet-Relying Party Registration Certificate è nello stato ``VALID``, la Wallet Unit DEVE impostare ``authz_art_state`` a ``CERTIFICATE_VALID``.
- Se un qualsiasi passo fallisce, o se nessun Wallet-Relying Party Registration Certificate è incluso, la Wallet Unit DEVE impostare ``authz_art_state`` a ``CERTIFICATE_INVALID``.
  Durante la Presentazione di Credenziali la Wallet Unit DEVE avvisare l'Utente ([`EIDAS-ARF`_] RPRC_17) e NON DEVE interrogare il Register.
  Durante l'Emissione di Credenziali la Wallet Unit DEVE avvisare l'Utente e NON DEVE richiedere l'emissione ([`EIDAS-ARF`_] RPRC_22a). La Wallet Unit NON DEVE interrogare il Register come fallback ([`EIDAS-ARF`_] RPRC_22).

.. note::

    Durante la Presentazione di Credenziali la richiesta DEVE recare per valore il Wallet-Relying Party Registration Certificate dell'Authorization Subject, anche quando la Wallet-Relying Party autenticata è un Relying Party Intermediary ([`EIDAS-ARF`_] RPRC_19).
    Tale certificato identifica la Relying Party intermediata.

Authorization Validation
"""""""""""""""""""""""""""""

La Authorization Validation DEVE seguire la Authorization Artifacts Validation quando ``authz_art_state == CERTIFICATE_VALID``.
Se ``authz_art_state == CERTIFICATE_INVALID``, la Wallet Unit NON DOVREBBE eseguire alcuna Authorization Validation, poiché non può modificare la Authorization Decision finale.

**Input**

La Wallet Unit DEVE basare la Authorization Validation solo su:

- la Wallet-Relying Party autenticata e il contesto di interazione, autorevoli solo per l'identità della Wallet-Relying Party;
- un Authorization Artifact validato, cioè un Wallet-Relying Party Registration Certificate, autorevole per l'identità del subject, le entitlement, l'uso previsto, l'ambito registrato, le relazioni di intermediario, i dati specifici dell'emissione e i riferimenti alla privacy policy, come definito in [`ETSI TS 119 475`_];
- un'Embedded Disclosure Policy verificata, OBBLIGATORIA quando fornita dall'Attestation Provider durante l'Emissione di Credenziali, autorevole quando presente.

Ove il contesto della Wallet-Relying Party autenticata sia in conflitto con l'identità o il binding di intermediario nel contesto di autorizzazione verificato, la Wallet Unit DEVE produrre ``NOT_AUTHORIZED``, non sovrascrivibile.

**Esito**

La Wallet Unit DEVE produrre le variabili ``authz_val_state`` e ``edp_state``, entrambe inizializzate a ``none``.

**Processo**

1. **Binding verification**.
   La Wallet Unit DEVE assicurare che l'entità autenticata sia la stessa entità descritta nei dati di autorizzazione.
   L'identità della Wallet-Relying Party è l'``organizationIdentifier`` del subject del Wallet-Relying Party Access Certificate (clausola 5.1.4 di [`ETSI EN 319 412-1`_]; il profilo del Wallet-Relying Party Access Certificate è definito in [`ETSI TS 119 411-8`_]).

    - **Credential Issuance**.
      La Wallet Unit DEVE abbinare l'identificatore del Credential Issuer con il ``sub`` del Wallet-Relying Party Registration Certificate e con l'``issuer_info.data.identifier`` dei Metadata del Credential Issuer ([`EIDAS-ARF`_] RPRC_22b).
    - **Credential Presentation**.
      La Wallet Unit DEVE prima assumere lo scenario **diretto** e abbinare l'identificatore della Relying Party nel Wallet-Relying Party Access Certificate (``organizationIdentifier`` o ``serialNumber``) con il ``sub`` del Wallet-Relying Party Registration Certificate, e con il ``verifier_info.data.identifier`` del Request Object nel Remote Flow oppure il ``docRequest.itemsRequest[].requestInfo.EUWrpRegistrarInfo.identifier`` nel Proximity Flow.
      Se l'abbinamento fallisce, la Wallet Unit DEVE tentare lo scenario **intermediato** ([`EIDAS-ARF`_] RPRC_17a):
      il subject del WRPAC è l'Intermediary, il WRPRC identifica una Relying Party diversa, l'oggetto ``intermediary`` del WRPRC identifica questo Intermediary ([`EIDAS-ARF`_] RPRC_04), e il ``subjectAltName`` del WRPAC reca l'associazione a quella Relying Party e a quel Servizio ([`EIDAS-ARF`_] Reg_34a).

    Se la Binding verification fallisce, la Wallet Unit DEVE interrompere la Authorization Validation e impostare ``authz_val_state`` a ``BINDING_FAILED``.
    Se lo scenario **diretto** ha successo, la Wallet Unit DEVE rendere disponibili all'Utente l'identità e il Servizio della Relying Party, e l'uso previsto della richiesta.
    Se lo scenario **intermediato** ha successo, la Wallet Unit DEVE rendere disponibili all'Utente l'identità e il Servizio della Relying Party *intermediata* e l'uso previsto della richiesta.
    NON DEVE visualizzare i trade name dell'Intermediary o del Servizio dell'Intermediary ([`EIDAS-ARF`_] RPI_07).
    Le modalità di presentazione di queste informazioni sono definite nelle sezioni rilevanti di interazione Utente della specifica IT-Wallet.
    Non è prevista una lookup opzionale da parte dell'Utente nel Registrar della relazione di intermediario ([`EIDAS-ARF`_] RPI_07a è vuoto).

2. **Entitlement verification**.
   La Wallet Unit DEVE verificare che le entitlement dell'Authorization Subject corrispondano al ruolo atteso.
   La Wallet Unit DEVE analizzare il campo ``entitlements`` del Wallet-Relying Party Registration Certificate e controllare che contenga l'URI di entitlement atteso per l'interazione, tra quelli definiti nell'Allegato A.2 di [`ETSI TS 119 475`_]:

    - ``https://uri.etsi.org/19475/Entitlement/PID_Provider`` per i PID Provider, durante l'Emissione di PID;
    - ``https://uri.etsi.org/19475/Entitlement/QEAA_Provider`` per i QEAA Provider, durante l'Emissione di QEAA;
    - ``https://uri.etsi.org/19475/Entitlement/PUB_EAA_Provider`` per i PuB-EAA Provider, durante l'Emissione di PuB-EAA;
    - ``https://uri.etsi.org/19475/Entitlement/Non_Q_EAA_Provider`` per gli EAA Provider, durante l'Emissione di EAA;
    - ``https://uri.etsi.org/19475/Entitlement/Service_Provider`` per le Relying Party, durante la Presentazione di Credenziali.

    Se l'entitlement attesa non è presente, la Wallet Unit DEVE impostare ``authz_val_state`` a ``WRONG_ENTITLEMENT``.

3. **Attestation Type verification**.
   Durante l'Emissione di Credenziali, la Wallet Unit DEVE verificare che il PID o il Tipo di Attestation in emissione sia registrato per il Credential Issuer.
   Un PID Provider che emette PID PUÒ omettere questo passo.
   Altrimenti la Wallet Unit DEVE abbinare l'array ``provides_attestations`` del Wallet-Relying Party Registration Certificate (definito nella Tabella 8 di [`ETSI TS 119 475`_]; [`EIDAS-ARF`_] RPRC_23) rispetto alle chiavi ``credential_configurations_supported`` dei Metadata del Credential Issuer ([`OpenID4VCI`_]).
   L'abbinamento DEVE essere esatto e case sensitive, su ``vct`` per SD-JWT VC e su ``docType`` per mdoc.
   Se non trovato, la Wallet Unit DEVE impostare ``authz_val_state`` a ``ATTESTATION_TYPE_NOT_REGISTERED``.

4. **Scope Comparison**.
   Durante la Presentazione di Credenziali, la Wallet Unit DEVE verificare che gli Attestati Elettronici e gli attributi richiesti ricadano nell'ambito registrato, recato nell'array ``credentials`` del Wallet-Relying Party Registration Certificate incluso nella richiesta (definito nella Tabella 9 di [`ETSI TS 119 475`_]; [`EIDAS-ARF`_] RPRC_21).

    - **Remote Flow**: estrarre gli Attestati Elettronici e gli attributi richiesti dalla ``dcql_query`` del Request Object ([`OpenID4VP`_]) e abbinarli rispetto alle entry ``credentials``, confrontando ``format`` e ``meta`` (``vct_values`` per SD-JWT VC) e gli attributi richiesti rispetto ai path ``claim``.
    - **Proximity Flow**: estrarre il ``docType`` e i ``nameSpaces`` dai ``docRequests`` della mdoc Request ([`ISO18013-5`_]) e abbinarli rispettivamente rispetto a ``credentials[].meta.doctype_value`` e ``credentials[].claim``.

    L'abbinamento DEVE essere esatto e case sensitive.
    Se un qualsiasi Attestato Elettronico o attributo richiesto non è registrato, la Wallet Unit DEVE impostare ``authz_val_state`` a ``OVERASKING_DETECTED`` e identificare gli attributi o gli Attestati Elettronici non registrati.

    Se tutti i controlli precedenti applicabili all'interazione sono soddisfatti, la Wallet Unit DEVE impostare ``authz_val_state`` a ``VERIFICATION_PASSED``.

5. **Embedded Disclosure Policy evaluation**.
   Durante la Presentazione di Credenziali, per ciascun Attestato Elettronico che corrisponde alla Presentation Request, la Wallet Unit DEVE verificare la presenza di un'Embedded Disclosure Policy memorizzata localmente.
   Se non ne esiste alcuna, questo controllo è superato.
   Altrimenti, secondo il ``policy_type`` definito nella Sezione 4.2.5 di [`ETSI TS 119 472-3`_]:

    - ``no_policy``: non si applica alcuna restrizione.
    - ``authorized_rp_only``: solo le Relying Party nell'elenco ``authorized_parties`` sono autorizzate.
      La Wallet Unit DEVE recuperare l'identificatore univoco a livello UE e l'identificatore del Servizio dal WRPRC nella richiesta (``sub`` e ``srv_id``) e confrontare tale coppia con l'elenco autorizzato ([`EIDAS-ARF`_] EDP_02, Reg_32, Reg_33).
      Ove un elemento ``authorized_parties`` identifichi la parte tramite ``entitlement_uri``, la Wallet Unit DEVE abbinare tale URI rispetto alle entitlement o sub-entitlement dello stesso WRPRC.
      Un abbinamento sulla coppia di identificatori o su ``entitlement_uri`` è sufficiente.
      Se nessuno dei due corrisponde, la Wallet Unit DEVE considerare fallita la valutazione EDP.
      La Wallet Unit NON DEVE usare identificatori dal WRPAC, incluso il subject DN della Relying Party di un Wallet-Relying Party Access Certificate.
      Se ``authorized_parties[].subject_dn`` è presente, è la codifica ETSI definita in :ref:`infrastructure-trust:Embedded Disclosure Policy (EDP)` e NON DEVE essere usato come sostituto della coppia di identificatori.
      In una presentazione **intermediata** il WRPRC nella richiesta è quello della Relying Party intermediata.
    - ``specific_root_of_trust``: solo le Relying Party il cui Wallet-Relying Party Registration Certificate è firmato sotto uno dei ``trusted_roots`` sono autorizzate ([`EIDAS-ARF`_] EDP_03).
      La Wallet Unit DEVE abbinare ciascuna entry ``trusted_roots`` per ``issuer_dn`` usando il confronto LDAP DN e ``serial_number`` usando il confronto intero.
      DEVE confrontare tutti i certificati nel signing path del WRPRC con quei certificati root o intermedi autorizzati.
      Il path comprende i certificati presentati con il WRPRC e il Trust Anchor recuperato dalla LoTE dei Provider of WRPRC.
      Se nessuno di questi certificati è incluso nell'elenco, la Wallet Unit DEVE considerare fallita la valutazione EDP.
      In una presentazione **intermediata** la Wallet Unit NON DEVE confrontare la catena WRPAC dell'Intermediary.
      DEVE usare il signing path del WRPRC della Relying Party intermediata incluso nella richiesta.

    Se il controllo applicabile è soddisfatto, o non è presente alcuna Embedded Disclosure Policy, la Wallet Unit DEVE impostare ``edp_state`` a ``EDP_SATISFIED``; altrimenti DEVE impostare ``edp_state`` a ``EDP_NOT_SATISFIED``.

**Esito**

Al termine della Authorization Validation la Wallet Unit DEVE produrre i valori ``authz_val_state`` e ``edp_state``.
La tabella seguente sintetizza i codici.

.. _table_authz_state_codes:
.. list-table:: Codici di Stato della Authorization Validation
   :class: longtable
   :widths: 18 26 12 44
   :header-rows: 1

   * - **Variabile**
     - **Code**
     - **Fase**
     - **Significato**
   * - ``authz_art_state``
     - ``CERTIFICATE_VALID``
     - both
     - Il formato, la firma, il trust anchor e lo status del Wallet-Relying Party Registration Certificate sono verificati con successo.
   * - ``authz_art_state``
     - ``CERTIFICATE_INVALID``
     - both
     - Un controllo di formato, firma, trust anchor o status fallisce sul certificato di registrazione presentato, oppure nessun Wallet-Relying Party Registration Certificate è incluso. Durante la presentazione la Wallet Unit DEVE avvisare l'Utente ([`EIDAS-ARF`_] RPRC_17) e NON DEVE interrogare il Register. Durante l'emissione la Wallet Unit DEVE avvisare l'Utente e NON DEVE richiedere l'emissione ([`EIDAS-ARF`_] RPRC_22a). La Wallet Unit NON DEVE interrogare il Register come fallback ([`EIDAS-ARF`_] RPRC_22).
   * - ``authz_val_state``
     - ``WRONG_ENTITLEMENT``
     - both
     - Le entitlement dell'Authorization Subject non corrispondono al ruolo atteso per il contesto attivo.
   * - ``authz_val_state``
     - ``BINDING_FAILED``
     - both
     - Il binding di identità tra la Wallet-Relying Party autenticata e i dati di autorizzazione fallisce.
   * - ``authz_val_state``
     - ``ATTESTATION_TYPE_NOT_REGISTERED``
     - issuance
     - Il Tipo di Attestation in emissione non è trovato nei profili registrati del Credential Issuer.
   * - ``authz_val_state``
     - ``OVERASKING_DETECTED``
     - presentation
     - La Relying Party richiede Attestati Elettronici, formati o namespace che eccedono il suo ambito registrato.
   * - ``authz_val_state``
     - ``VERIFICATION_PASSED``
     - both
     - Il binding di identità, la verifica delle entitlement, l'abbinamento delle attestation e il controllo dell'ambito sono tutti superati.
   * - ``edp_state``
     - ``EDP_SATISFIED``
     - presentation
     - Non si applica alcuna restrizione di Embedded Disclosure Policy, oppure la Relying Party soddisfa la policy locale.
   * - ``edp_state``
     - ``EDP_NOT_SATISFIED``
     - presentation
     - La Relying Party non soddisfa alcuna Embedded Disclosure Policy memorizzata localmente.

La Authorization Decision finale, ``AUTHORIZED`` o ``NOT_AUTHORIZED``, è elaborata dai valori ``authz_art_state``, ``authz_val_state`` e ``edp_state``, come definito in :ref:`trust-evaluation:Authorization Decision and Override Rules`.

.. plantuml:: plantuml/eudiw-authz-eval.puml
    :width: 99%
    :alt: Diagramma di flusso dell'algoritmo di Autorizzazione EUDIW.
    :caption: Diagramma di flusso dell'algoritmo di Autorizzazione EUDIW.

EUDIW Metadata Retrieval and Validation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

All'interno del Trust Framework EUDIW i metadata di una Wallet-Relying Party sono ottenuti attraverso il flusso di protocollo e la loro autenticità è stabilita attraverso il Wallet-Relying Party Access Certificate.
Questo si applica all'Emissione di Credenziali e alla Presentazione di Credenziali nel Remote Flow.
Nel Proximity Flow non è eseguito un recupero di metadata separato: l'identità della Relying Party è stabilita attraverso l'mdoc reader authentication (vedi :ref:`trust-evaluation:EUDIW Authentication`).

**Metadata Retrieval**

La Wallet Unit ottiene i metadata della Wallet-Relying Party in base all'interazione:

- Durante l'Emissione di Credenziali, i Metadata del Credential Issuer sono ottenuti dall'endpoint well-known dei metadata del Credential Issuer, come definito in [`OpenID4VCI`_] (vedi :ref:`credential-issuer-endpoint:Endpoint Metadata`).
- Durante la Presentazione di Credenziali nel Remote Flow, i metadata della Relying Party sono recati nel Request Object della richiesta di autorizzazione, come definito in [`OpenID4VP`_] (vedi :ref:`remote-flow:Request Object`).

**Metadata Validation**

L'autenticità dei metadata recuperati è stabilita attraverso il Wallet-Relying Party Access Certificate.
Durante l'Emissione di Credenziali, i Metadata del Credential Issuer sono firmati dall'Attestation Provider come definito nella Sezione 12.2.3 di [`OpenID4VCI`_], fornendo la catena del Wallet-Relying Party Access Certificate nell'header ``x5c`` della firma JOSE.
Durante la Presentazione di Credenziali nel Remote Flow, il Request Object è firmato dalla Relying Party e fornisce lo stesso header ``x5c``.
In entrambi i casi la Wallet Unit valida la firma e la catena di certificati come definito in :ref:`trust-evaluation:EUDIW Authentication`, e DEVE usare solo i metadata la cui firma è verificata rispetto al Wallet-Relying Party Access Certificate autenticato.

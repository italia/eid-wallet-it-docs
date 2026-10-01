.. include:: ../common/common_definitions.rst
.. Incluso tramite infrastructure-trust.rst al livello di titolo '-' (livello 1).

Common Trust Artifacts
----------------------

Questa sezione dettaglia gli artifact comuni coinvolti sia nel Trust Framework EUDIW sia in quello Nazionale, inclusi:

- :ref:`infrastructure-trust:Entity Sign/Seal Certificate Profile`;
- :ref:`infrastructure-trust:Trust Anchor Certificate Profile`.

Entity Sign/Seal Certificate Profile
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Questa sezione estende il :ref:`infrastructure-trust:X.509 Certificate Profile` generale e specifica un **Certificate Profile** per gli **Entity Sign/Seal Certificates**, che sono usati per firmare e sigillare varie Attestation.
Questo profilo è originariamente definito in `ETSI TS 119 412-6`_.

.. warning::

  I profili Entity Sign/Seal Certificate definiti in questa specifica assumono che gli Entity Sign/Seal Certificate siano emessi da una CA e non siano self-signed.
  Un certificato self-signed destinato ad agire come Trust Anchor MAY essere usato in interoperabilità.
  I National Sign/Seal Certificate MUST essere conformi ai requisiti definiti in :ref:`infrastructure-trust:Trust Anchor Certificate Profile` e :ref:`infrastructure-trust:Certification Hierarchies`, che richiedono che i National Trust Anchor siano vincolati a una root comune.

PID Provider Sign/Seal Certificate
""""""""""""""""""""""""""""""""""

I requisiti specifici per i PID Provider Sign/Seal Certificate sono specificati nella Clausola 4 di [`ETSI TS 119 412-6`_].

La tabella seguente definisce l'insieme completo di estensioni applicabili al profilo di certificato.
Le estensioni non elencate nella tabella MUST NOT essere presenti.

.. list-table:: Estensioni del PID Provider Sign/Seal Certificate
   :class: longtable
   :header-rows: 1
   :widths: 25 75

   * - **Extension**
     - **Descrizione**

   * - ``authorityKeyIdentifier``
     - REQUIRED. Il valore del campo ``keyIdentifier`` SHOULD essere derivato dalla chiave pubblica usando i metodi definiti in :rfc:`5280#section-4.2.1.1`.

   * - ``subjectKeyIdentifier``
     - REQUIRED. Il suo valore SHOULD essere derivato dalla chiave pubblica del subject usando i metodi definiti in :rfc:`5280#section-4.2.1.2`.

   * - ``keyUsage``
     - REQUIRED. MUST contenere uno (e uno solo) dei key-usage settings *Type A*, *Type B*, *Type C* o *Type F*.
       Per dettagli aggiuntivi, vedi Clausola 4.4.1 [`ETSI TS 119 412-6`_], Clausola 4.3.2 [`ETSI EN 319 412-2`_] e Clausola 4.3.1 [`ETSI EN 319 412-3`_].

   * - ``certificatePolicies``
     - REQUIRED. MUST includere una struttura ``PolicyInformation`` con ``policyIdentifier`` impostato all'OID di una certificate policy che include almeno i requisiti per *NCP+*, definiti in `ETSI EN 319 411-1`_, per essere conforme al requisito `EIDAS-ARF`_ ``AS-AP-10-098``.

   * - ``subjectAltName``
     - REQUIRED.

   * - ``cRLDistributionPoints``
     - CONDITIONAL. **REQUIRED IF:** il certificato non include alcuna access location di un responder OCSP o l'estensione validity assured come definita in `ETSI EN 319 412-1`_.

       Se presente, MUST contenere almeno un riferimento a una CRL pubblicamente disponibile.

   * - ``authorityInfoAccess``
     - REQUIRED. MUST includere una struttura ``AccessDescription`` con ``accessMethod`` impostato a ``1.3.6.1.5.5.7.48.2`` (``id-ad-caIssuers``) e ``accessLocation`` che specifica almeno una access location di un certificato CA valido della CA emittente.
       
       Se l'OCSP è supportato dalla CA emittente, l'estensione MUST includere una struttura ``AccessDescription`` con ``accessMethod`` impostato a ``1.3.6.1.5.5.7.48.1`` (``id-ad-ocsp``) e ``accessLocation`` che specifica almeno un responder OCSP autorevole a fornire informazioni di status del certificato per il certificato, come descritto in :ref:`infrastructure-trust:Online Certificate Status Protocol (OCSP)`.

   * - ``qcStatements``
     - REQUIRED. MUST contenere una struttura ``QCStatement`` con ``statementId`` impostato a ``0.4.0.1862.1.6`` (``id-etsi-qcs-QcType``). Il corrispondente ``statementInfo`` MUST contenere una struttura ``QcType`` che include esattamente un object identifier, cioè ``0.4.0.194126.1.1`` (``id-etsi-qct-pid``), come definito nella Clausola 4.5 di [`ETSI TS 119 412-6`_].
     
       MAY contenere strutture ``QCStatement`` aggiuntive tra quelle definite nella Clausola 4.2 di [`ETSI EN 319 412-5`_]. In ogni caso, MUST NOT contenere una struttura ``QCStatement`` con ``statementId`` impostato a ``0.4.0.1862.1.7`` (``id-etsi-qcs-QcCClegislation``), indicato come ``esi4-qcStatement-7``.

Di seguito un esempio non normativo di PID Provider Sign/Seal Certificate per persone giuridiche.

.. literalinclude:: ../../examples/pid-sign-seal.txt
  :language: text

Wallet Provider Sign/Seal Certificate
"""""""""""""""""""""""""""""""""""""

I requisiti specifici per i Wallet Provider Sign/Seal Certificate sono specificati nella Clausola 5 di [`ETSI TS 119 412-6`_].

La tabella seguente definisce l'insieme completo di estensioni applicabili al profilo di certificato.
Le estensioni non elencate nella tabella MUST NOT essere presenti.

.. list-table:: Estensioni del Wallet Provider Sign/Seal Certificate
   :class: longtable
   :header-rows: 1
   :widths: 25 75

   * - **Extension**
     - **Descrizione**

   * - ``authorityKeyIdentifier``
     - REQUIRED. Il valore del ``keyIdentifier`` SHOULD essere derivato dalla chiave pubblica usando i metodi definiti in :rfc:`5280#section-4.2.1.1`.

   * - ``subjectKeyIdentifier``
     - REQUIRED. Il suo valore SHOULD essere derivato dalla chiave pubblica del subject usando i metodi definiti in :rfc:`5280#section-4.2.1.2`.

   * - ``keyUsage``
     - REQUIRED. MUST contenere uno (e uno solo) dei key-usage settings *Type A*, *Type B*, *Type C* o *Type F*.
       Per dettagli aggiuntivi, vedi Clausola 4.4.1 [`ETSI TS 119 412-6`_], Clausola 4.3.2 [`ETSI EN 319 412-2`_] e Clausola 4.3.1 [`ETSI EN 319 412-3`_].

   * - ``certificatePolicies``
     - REQUIRED. MUST includere una struttura ``PolicyInformation`` con ``policyIdentifier`` impostato all'OID di una certificate policy che include almeno (secondo il requisito `EIDAS-ARF`_ ``EW-DM-38-001``):

       * I requisiti per *NCP*, definiti in `ETSI EN 319 411-1`_, per KA che descrivono un keystore.
       * I requisiti per *NCP+*, definiti in `ETSI EN 319 411-1`_, per KA che descrivono una WSCA/WSCD.

   * - ``subjectAltName``
     - REQUIRED.

   * - ``cRLDistributionPoints``
     - CONDITIONAL. **REQUIRED IF:** il certificato non include alcuna access location di un responder OCSP o l'estensione validity assured come definita in `ETSI EN 319 412-1`_.

       Se presente, MUST contenere almeno un riferimento a una CRL pubblicamente disponibile.

   * - ``authorityInfoAccess``
     - REQUIRED. MUST includere una struttura ``AccessDescription`` con ``accessMethod`` impostato a ``1.3.6.1.5.5.7.48.2`` (``id-ad-caIssuers``) e ``accessLocation`` che specifica almeno una access location di un certificato CA valido della CA emittente.

       Se l'OCSP è supportato dalla CA emittente, l'estensione MUST includere una struttura ``AccessDescription`` con ``accessMethod`` impostato a ``1.3.6.1.5.5.7.48.1`` (``id-ad-ocsp``) e ``accessLocation`` che specifica almeno un responder OCSP autorevole a fornire informazioni di status del certificato per il certificato, come descritto in :ref:`infrastructure-trust:Online Certificate Status Protocol (OCSP)`.

   * - ``qcStatements``
     - REQUIRED. MUST contenere una struttura ``QCStatement`` con ``statementId`` impostato a ``0.4.0.1862.1.6`` (``id-etsi-qcs-QcType``). Il corrispondente ``statementInfo`` MUST contenere una struttura ``QcType`` che include esattamente un object identifier, cioè ``0.4.0.194126.1.2`` (``id-etsi-qct-wal``), come definito nella Clausola 5.2 di [`ETSI TS 119 412-6`_].
     
       MAY contenere strutture ``QCStatement`` aggiuntive tra quelle definite nella Clausola 4.2 di [`ETSI EN 319 412-5`_]. In ogni caso, MUST NOT contenere una struttura ``QCStatement`` con ``statementId`` impostato a ``0.4.0.1862.1.7`` (``id-etsi-qcs-QcCClegislation``), indicato come ``esi4-qcStatement-7``.

Di seguito un esempio non normativo di Wallet Provider Sign/Seal Certificate per persone giuridiche.

.. literalinclude:: ../../examples/wp-sign-seal.txt
  :language: text

(Q)EAA Provider Sign/Seal Certificate
"""""""""""""""""""""""""""""""""""""

I requisiti specifici per i Sign/Seal Certificate di EAA Provider e QEAA Provider sono specificati rispettivamente nelle Clausole 6 e 7 di [`ETSI TS 119 412-6`_].

La tabella seguente definisce l'insieme completo di estensioni applicabili al profilo di certificato.
Le estensioni non elencate nella tabella MUST NOT essere presenti.

.. list-table:: Estensioni del (Q)EAA Provider Sign/Seal Certificate
   :class: longtable
   :header-rows: 1
   :widths: 25 75

   * - **Extension**
     - **Descrizione**

   * - ``authorityKeyIdentifier``
     - REQUIRED. Il valore del campo ``keyIdentifier`` SHOULD essere derivato dalla chiave pubblica usando i metodi definiti in :rfc:`5280#section-4.2.1.1`.

   * - ``subjectKeyIdentifier``
     - OPTIONAL. Se presente, il suo valore SHOULD essere derivato dalla chiave pubblica del subject usando i metodi definiti in :rfc:`5280#section-4.2.1.2`.

   * - ``keyUsage``
     - REQUIRED. MUST contenere uno (e uno solo) dei key-usage settings *Type A*, *Type B*, *Type C*, o *Type F*.
       Per dettagli aggiuntivi, vedi Clausola 4.3.2 [`ETSI EN 319 412-2`_] e Clausola 4.3.1 [`ETSI EN 319 412-3`_].

   * - ``certificatePolicies``
     - REQUIRED (solo per QEAA). Come descritto nella Clausola 6.6.1 di [`ETSI EN 319 411-2`_].

   * - ``subjectAltName``
     - REQUIRED.

   * - ``cRLDistributionPoints``
     - CONDITIONAL. **REQUIRED IF:** il certificato non include alcuna access location di un responder OCSP o l'estensione validity assured come definita in `ETSI EN 319 412-1`_.

       Se presente, MUST contenere almeno un riferimento a una CRL pubblicamente disponibile.

   * - ``authorityInfoAccess``
     - REQUIRED (solo per QEAA). MUST includere una struttura ``AccessDescription`` con ``accessMethod`` impostato a ``1.3.6.1.5.5.7.48.2`` (``id-ad-caIssuers``) e ``accessLocation`` che specifica almeno una access location di un certificato CA valido della CA emittente.

       Se l'OCSP è supportato dalla CA emittente, l'estensione MUST includere una struttura ``AccessDescription`` con ``accessMethod`` impostato a ``1.3.6.1.5.5.7.48.1`` (``id-ad-ocsp``) e ``accessLocation`` che specifica almeno un responder OCSP autorevole a fornire informazioni di status del certificato per il certificato, come descritto in :ref:`infrastructure-trust:Online Certificate Status Protocol (OCSP)`.

   * - ``qcStatements``
     - REQUIRED (QEAA), OPTIONAL (EAA).
     
       Per **QEAA**: MUST contenere una struttura ``QCStatement`` con ``statementId`` impostato a ``0.4.0.1862.1.1`` (``id-etsi-qcs-QcCompliance``), indicato come ``esi4-qcStatement-1``.
            
       Per **entrambi**:
       
       * MAY contenere strutture ``QCStatement`` aggiuntive tra quelle definite nella Clausola 4.2 di [`ETSI EN 319 412-5`_].
       * In ogni caso, MUST NOT contenere una struttura ``QCStatement`` con ``statementId`` impostato a ``0.4.0.1862.1.7`` (``id-etsi-qcs-QcCClegislation``), indicato come ``esi4-qcStatement-7``.

Sia per i QEAA sia per gli EAA Provider, se gestiscono il ciclo di vita degli Attestati Elettronici che emettono e usano liste di revoca firmate come Token Status List, MUST usare lo stesso Sign/Seal Certificate per firmare/sigillare la lista di revoca.

Di seguito un esempio non normativo di QEAA Provider Sign/Seal Certificate per persone giuridiche.

.. literalinclude:: ../../examples/qeaa-sign-seal.txt
  :language: text

PuB-EAA Provider Sign/Seal Certificate
""""""""""""""""""""""""""""""""""""""

.. warning::

    Sebbene i requisiti specifici per i PuB-EAA Provider Sign/Seal Certificate specificati nella Clausola 8 di [`ETSI TS 119 412-6`_] non richiedano che questo profilo sia qualificato, l'Art. 45f(1)(b) di [`EU_2024_1183`_] richiede che le Attestation di tipo PuB-EAA siano firmate con un certificato qualificato. Per soddisfare entrambi i requisiti, sebbene non dichiarato né in [`EIDAS-ARF`_] né in [`ETSI TS 119 412-6`_], questo profilo unisce i profili QEAA e PuB-EAA Provider Sign/Seal Certificate specificati nelle Clausole 7 e 8 di [`ETSI TS 119 412-6`_].

La tabella seguente definisce l'insieme completo di estensioni applicabili al profilo di certificato.
Le estensioni non elencate nella tabella MUST NOT essere presenti.

.. list-table:: Estensioni del PuB-EAA Provider Sign/Seal Certificate
   :class: longtable
   :header-rows: 1
   :widths: 25 75

   * - **Extension**
     - **Descrizione**

   * - ``authorityKeyIdentifier``
     - REQUIRED. Il valore del campo ``keyIdentifier`` SHOULD essere derivato dalla chiave pubblica usando i metodi definiti in :rfc:`5280#section-4.2.1.1`.

   * - ``subjectKeyIdentifier``
     - OPTIONAL. Se presente, il suo valore SHOULD essere derivato dalla chiave pubblica del subject usando i metodi definiti in :rfc:`5280#section-4.2.1.2`.

   * - ``keyUsage``
     - REQUIRED.

   * - ``certificatePolicies``
     - REQUIRED. Come descritto nella Clausola 6.6.1 di [`ETSI EN 319 411-2`_].

   * - ``subjectAltName``
     - REQUIRED.

   * - ``cRLDistributionPoints``
     - CONDITIONAL. **REQUIRED IF:** il certificato non include alcuna access location di un responder OCSP o l'estensione validity assured come definita in `ETSI EN 319 412-1`_.

       Se presente, MUST contenere almeno un riferimento a una CRL pubblicamente disponibile.

   * - ``authorityInfoAccess``
     - REQUIRED. MUST includere una struttura ``AccessDescription`` con ``accessMethod`` impostato a ``1.3.6.1.5.5.7.48.2`` (``id-ad-caIssuers``) e ``accessLocation`` che specifica almeno una access location di un certificato CA valido della CA emittente.

       Se l'OCSP è supportato dalla CA emittente, l'estensione MUST includere una struttura ``AccessDescription`` con ``accessMethod`` impostato a ``1.3.6.1.5.5.7.48.1`` (``id-ad-ocsp``) e ``accessLocation`` che specifica almeno un responder OCSP autorevole a fornire informazioni di status del certificato per il certificato, come descritto in :ref:`infrastructure-trust:Online Certificate Status Protocol (OCSP)`.

   * - ``qcStatements``
     - REQUIRED. MUST contenere:
     
       * Una struttura ``QCStatement`` con ``statementId`` impostato a ``0.4.0.1862.1.1`` (``id-etsi-qcs-QcCompliance``), indicato come ``esi4-qcStatement-1``.
       * Una struttura ``QCStatement`` con ``statementId`` impostato all'OID corrispondente a ``id-etsi-qcs-QcPSB``. Il corrispondente ``statementInfo`` MUST contenere una struttura ``QcPSB`` che include i campi definiti nella Clausola 8.3 di [`ETSI TS 119 412-6`_].
       
       MAY contenere strutture ``QCStatement`` aggiuntive tra quelle definite nella Clausola 4.2 di [`ETSI EN 319 412-5`_]. In ogni caso, MUST NOT contenere una struttura ``QCStatement`` con ``statementId`` impostato a ``0.4.0.1862.1.7`` (``id-etsi-qcs-QcCClegislation``), indicato come ``esi4-qcStatement-7``.

.. warning::

  L'Allegato A di [`ETSI TS 119 412-6`_] non definisce l'OID specifico dell'identificatore di statement ``id-etsi-qcs-QcPSB``.

Di seguito un esempio non normativo di PuB-EAA Provider Sign/Seal Certificate per persone giuridiche.

.. literalinclude:: ../../examples/pubeaa-sign-seal.txt
  :language: text

Trust Anchor Certificate Profile
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Questa sezione estende il :ref:`infrastructure-trust:X.509 Certificate Profile` generale e specifica un **Certificate Profile** per i **Trust Anchors**.
Un Trust Anchor è una chiave pubblica fidata (e i dati associati) usata come input per :ref:`trust-evaluation:X509 Certificate Chain Validation Algorithm`.
In questo profilo, il Trust Anchor MUST essere rappresentato e distribuito come un **certificato X.509**, che MAY essere self-signed.

Le Relying Party, i Credential Issuer e le Wallet Unit validano un Access, Registration o Sign/Seal Certificate presentato costruendo un certification path che MUST terminare con un certificato firmato dal subject di un certificato Trust Anchor.
Il certificato Trust Anchor è usato come punto di terminazione della fiducia per il processo di path validation (cioè, è il valore della variabile ``trust_anchor`` in :ref:`trust-evaluation:X509 Certificate Chain Validation Algorithm`).
Le implementazioni MUST supportare la validazione sia di certificati Trust Anchor self-signed sia non self-signed.

.. note::
  **Trust Anchor Location.**
  La location del Trust Anchor Certificate è determinata dal Trust Framework specifico selezionato (vedi :ref:`trust-evaluation:EUDIW Trust Anchor Validation` e :ref:`trust-evaluation:Federation Trust Anchor Validation`).

La tabella seguente definisce i requisiti specifici del profilo per i campi del certificato.
I campi non elencati nella tabella restano soggetti ai requisiti definiti nel :ref:`infrastructure-trust:X.509 Certificate Profile` comune.

.. list-table:: Campi del Trust Anchor Certificate
   :class: longtable
   :header-rows: 1
   :widths: 30 70

   * - **Field**
     - **Requisiti aggiuntivi**

   * - ``issuer``
     - Se il certificato è self-signed, il distinguished name dell'issuer MUST essere identico al distinguished name del subject.
       Altrimenti, il distinguished name dell'issuer MUST identificare l'entità che ha firmato ed emesso il certificato e MAY differire dal distinguished name del subject.

   * - ``subject``
     - Il distinguished name MUST contenere un attributo ``organizationName`` che identifica tale entità.


.. list-table:: Estensioni del Trust Anchor Certificate
   :class: longtable
   :header-rows: 1
   :widths: 25 75

   * - **Extension**
     - **Descrizione**

   * - ``authorityKeyIdentifier``
     - CONDITIONAL. **REQUIRED IF:** il certificato non è self-signed.
       Per i certificati self-signed, è RECOMMENDED.
       Se l'estensione è presente, il valore del campo ``keyIdentifier`` SHOULD essere derivato dalla chiave pubblica usando i metodi definiti in :rfc:`5280#section-4.2.1.1`.

   * - ``subjectKeyIdentifier``
     - REQUIRED. Fornisce un key identifier per la chiave pubblica del Trust Anchor.
       Il suo valore SHOULD essere derivato dalla chiave pubblica del subject usando i metodi definiti in :rfc:`5280#section-4.2.1.2`.
       Questa estensione SHOULD supportare una Certificate Path construction affidabile e l'abbinamento dei certificati nei deployment basati su LoTE o TL.

   * - ``keyUsage``
     - REQUIRED. MUST asserire il bit ``keyCertSign``.
       MAY asserire il bit ``cRLSign`` se il certificato Trust Anchor è usato dalla CA per firmare le CRL.
       SHOULD essere limitato a usi coerenti con il ruolo CA del certificato Trust Anchor.

   * - ``certificatePolicies``
     - OPTIONAL. MAY includere una struttura ``PolicyInformation`` rilevante per le pratiche della CA emittente.

   * - ``basicConstraints``
     - REQUIRED. Il campo ``cA`` MUST essere impostato a ``TRUE``, segnalando la capacità CA per la path validation X.509.
       Il ``pathLenConstraint`` MAY essere presente.
       In tal caso, esso MUST limitare il numero di certificati CA intermedi non self-issued al di sotto di questo Trust Anchor.
       È RECOMMENDED impostare ``pathLenConstraint`` a 0 per impedire strati CA subordinati, a meno che non esista una necessità operativa documentata di supportare ulteriori livelli CA intermedi.

   * - ``cRLDistributionPoints``
     - OPTIONAL. MAY includere URI di CRL distribution point, quando è usata la revoca basata su CRL.

   * - ``authorityInfoAccess``
     - OPTIONAL. Se applicabile, MAY includere una struttura ``AccessDescription`` con ``accessMethod`` impostato a ``1.3.6.1.5.5.7.48.2`` (``id-ad-caIssuers``) e un ``accessLocation`` che specifica almeno una access location di un certificato CA valido della CA emittente.

       MAY anche includere una struttura ``AccessDescription`` con ``accessMethod`` impostato a ``1.3.6.1.5.5.7.48.1`` (``id-ad-ocsp``) e ``accessLocation`` che specifica almeno un responder OCSP autorevole a fornire informazioni di status del certificato per il certificato, quando è usata la revoca basata su OCSP.

   * - ``qcStatements``
     - OPTIONAL. MAY contenere strutture ``QCStatement`` tra quelle definite nella Clausola 4.2 di [`ETSI EN 319 412-5`_].
     
       In ogni caso, MUST NOT contenere una struttura ``QCStatement`` con ``statementId`` impostato a ``0.4.0.1862.1.7`` (``id-etsi-qcs-QcCClegislation``), indicato come ``esi4-qcStatement-7``.

.. note::
  **Trust Anchor Signature.**
  Un certificato Trust Anchor MAY essere self-signed (rappresentando una root CA) o non self-signed (rappresentando una CA intermedia designata come Trust Anchor per policy).
  Le Relying Party MUST NOT richiedere un issuer aggiuntivo al di sopra di un Trust Anchor recuperato come specificato dal Trust Framework applicabile, anche se non è self-signed, perché il Trust Anchor è un input autorevole all'algoritmo di path validation designato per policy.

.. note::

  Come descritto nella Sezione 4.3.1 di [`EUDI-TS 12`_], il Trust Anchor di un EAA Sign/Seal Certificate è referenziato nell'attributo ``trustedAuthority`` dell'Attestation Rulebook machine-readable per la specifica EAA.

Di seguito un esempio non normativo di Trust Anchor Certificate.

.. literalinclude:: ../../examples/trust-anchor-cert.txt
  :language: text

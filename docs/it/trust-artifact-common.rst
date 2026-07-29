.. include:: ../common/common_definitions.rst
.. Included via infrastructure-trust.rst at title level '-' (level 1).

Common Trust Artifacts
----------------------

Questa sezione dettaglia gli artifact comuni coinvolti sia nel EUDIW Trust Framework sia nel National Trust Framework, tra cui:

- :ref:`infrastructure-trust:Entity Sign/Seal Certificate Profile`;
- :ref:`infrastructure-trust:Trust Anchor Certificate Profile`.

Entity Sign/Seal Certificate Profile
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Questa sezione estende il generale :ref:`infrastructure-trust:X.509 Certificate Profile` e specifica un **Certificate Profile** per gli **Entity Sign/Seal Certificates**, utilizzati per firmare e sigillare varie Attestation.
Questo profilo è originariamente definito in `ETSI TS 119 412-6`_.

.. warning::

  Gli Entity Sign/Seal Certificate Profile definiti in questa specifica assumono che gli Entity Sign/Seal Certificates siano emessi da una CA e non siano self-signed.
  Un certificato self-signed destinato ad agire come Trust Anchor PUÒ essere utilizzato per l'interoperabilità; tuttavia, i National Sign/Seal Certificates DEVONO conformarsi ai requisiti definiti in :ref:`infrastructure-trust:Trust Anchor Certificate Profile` e :ref:`infrastructure-trust:Certification Hierarchies`, che richiedono che i National Trust Anchors siano vincolati a una root comune.

PID Provider Sign/Seal Certificate
""""""""""""""""""""""""""""""""""

I requisiti specifici per i PID Provider Sign/Seal Certificates sono specificati nella Clause 4 di [`ETSI TS 119 412-6`_].

La tabella seguente definisce l'insieme completo delle extensions applicabili al certificate profile.
Le extensions non elencate nella tabella NON DEVONO essere presenti.

.. list-table:: PID Provider Sign/Seal Certificate Extensions
   :class: longtable
   :header-rows: 1
   :widths: 25 75

   * - **Extension**
     - **Description**

   * - ``authorityKeyIdentifier``
     - REQUIRED. Il valore DOVREBBE essere derivato dalla chiave pubblica utilizzando i metodi definiti in :rfc:`5280#section-4.2.1.1`.

   * - ``subjectKeyIdentifier``
     - REQUIRED. Il campo ``keyIdentifier`` DOVREBBE essere derivato dalla chiave pubblica del subject utilizzando i metodi definiti in :rfc:`5280#section-4.2.1.2`.

   * - ``keyUsage``
     - REQUIRED. DEVE contenere una (e una sola) delle impostazioni key-usage *Type A*, *Type B*, *Type C* o *Type F*.
       Per ulteriori dettagli, vedere Clause 4.4.1 [`ETSI TS 119 412-6`_], Clause 4.3.2 [`ETSI EN 319 412-2`_] e Clause 4.3.1 [`ETSI EN 319 412-3`_].

   * - ``certificatePolicies``
     - REQUIRED. DEVE includere una struttura ``PolicyInformation`` con ``policyIdentifier`` impostato all'OID di una certificate policy che includa almeno i requisiti per *NCP+*, definiti in `ETSI EN 319 411-1`_, per conformarsi al requisito `EIDAS-ARF`_ ``AS-AP-10-098``.

   * - ``subjectAltName``
     - REQUIRED.

   * - ``cRLDistributionPoints``
     - CONDITIONAL. **REQUIRED IF:** il certificato non include alcuna access location di un OCSP responder o l'extension validity assured definita in `ETSI EN 319 412-1`_.

   * - ``authorityInfoAccess``
     - REQUIRED. DEVE includere una struttura ``AccessDescription`` con ``accessMethod`` impostato a ``1.3.6.1.5.5.7.48.2`` (``id-ad-caIssuers``) e ``accessLocation`` che specifichi almeno una access location di un certificato CA valido della CA emittente.
       Se l'OCSP è supportato dalla CA emittente, l'extension DEVE includere una struttura ``AccessDescription`` con ``accessMethod`` impostato a ``1.3.6.1.5.5.7.48.1`` (``id-ad-ocsp``) e ``accessLocation`` che specifichi almeno un OCSP responder autorizzato a fornire informazioni sullo stato del certificato, come descritto in :ref:`infrastructure-trust:Online Certificate Status Protocol (OCSP)`.

   * - ``qcStatements``
     - REQUIRED. DEVE contenere una struttura ``QCStatement`` con ``statementId`` impostato a ``0.4.0.1862.1.6`` (``id-etsi-qcs-QcType``).
       Il corrispondente ``statementInfo`` DEVE contenere una struttura ``QcType`` che includa esattamente un object identifier, vale a dire ``0.4.0.194126.1.1`` (``id-etsi-qct-pid``), come definito nella Clause 4.5 di [`ETSI TS 119 412-6`_].

Di seguito un esempio non normativo di PID Provider Sign/Seal Certificate per legal persons.

.. literalinclude:: ../../examples/pid-sign-seal.txt
  :language: text

Wallet Provider Sign/Seal Certificate
"""""""""""""""""""""""""""""""""""""

I requisiti specifici per i Wallet Provider Sign/Seal Certificates sono specificati nella Clause 5 di [`ETSI TS 119 412-6`_].

La tabella seguente definisce l'insieme completo delle extensions applicabili al certificate profile.
Le extensions non elencate nella tabella NON DEVONO essere presenti.

.. list-table:: Wallet Provider Sign/Seal Certificate Extensions
   :class: longtable
   :header-rows: 1
   :widths: 25 75

   * - **Extension**
     - **Description**

   * - ``authorityKeyIdentifier``
     - REQUIRED. Il valore DOVREBBE essere derivato dalla chiave pubblica utilizzando i metodi definiti in :rfc:`5280#section-4.2.1.1`.

   * - ``subjectKeyIdentifier``
     - OPTIONAL. Se presente, il campo ``keyIdentifier`` DOVREBBE essere derivato dalla chiave pubblica del subject utilizzando i metodi definiti in :rfc:`5280#section-4.2.1.2`.

   * - ``keyUsage``
     - REQUIRED. DEVE contenere una (e una sola) delle impostazioni key-usage *Type A*, *Type B*, *Type C* o *Type F*.
       Per ulteriori dettagli, vedere Clause 4.4.1 [`ETSI TS 119 412-6`_], Clause 4.3.2 [`ETSI EN 319 412-2`_] e Clause 4.3.1 [`ETSI EN 319 412-3`_].

   * - ``certificatePolicies``
     - REQUIRED. DEVE includere una struttura ``PolicyInformation`` con ``policyIdentifier`` impostato all'OID di una certificate policy che includa almeno (secondo il requisito `EIDAS-ARF`_ ``EW-DM-38-001``):
       * i requisiti per *NCP*, definiti in `ETSI EN 319 411-1`_, per le KA che descrivono un keystore;
       * i requisiti per *NCP+*, definiti in `ETSI EN 319 411-1`_, per le KA che descrivono un WSCA/WSCD.

   * - ``subjectAltName``
     - REQUIRED.

   * - ``cRLDistributionPoints``
     - CONDITIONAL. **REQUIRED IF:** il certificato non include alcuna access location di un OCSP responder o l'extension validity assured definita in `ETSI EN 319 412-1`_.

   * - ``authorityInfoAccess``
     - REQUIRED. DEVE includere una struttura ``AccessDescription`` con ``accessMethod`` impostato a ``1.3.6.1.5.5.7.48.2`` (``id-ad-caIssuers``) e ``accessLocation`` che specifichi almeno una access location di un certificato CA valido della CA emittente.

       Se l'OCSP è supportato dalla CA emittente, l'extension DEVE includere una struttura ``AccessDescription`` con ``accessMethod`` impostato a ``1.3.6.1.5.5.7.48.1`` (``id-ad-ocsp``) e ``accessLocation`` che specifichi almeno un OCSP responder autorizzato a fornire informazioni sullo stato del certificato, come descritto in :ref:`infrastructure-trust:Online Certificate Status Protocol (OCSP)`.

   * - ``qcStatements``
     - REQUIRED. DEVE contenere una struttura ``QCStatement`` con ``statementId`` impostato a ``0.4.0.1862.1.6`` (``id-etsi-qcs-QcType``).
       Il corrispondente ``statementInfo`` DEVE contenere una struttura ``QcType`` che includa esattamente un object identifier, vale a dire ``0.4.0.194126.1.2`` (``id-etsi-qct-wal``), come definito nella Clause 5.2 di [`ETSI TS 119 412-6`_].

Di seguito un esempio non normativo di Wallet Provider Sign/Seal Certificate per legal persons.

.. literalinclude:: ../../examples/wp-sign-seal.txt
  :language: text

(Q)EAA Provider Sign/Seal Certificate
"""""""""""""""""""""""""""""""""""""

I requisiti specifici per gli EAA Provider e QEAA Provider Sign/Seal Certificates sono specificati rispettivamente nelle Clauses 6 e 7 di [`ETSI TS 119 412-6`_].

La tabella seguente definisce l'insieme completo delle extensions applicabili al certificate profile.
Le extensions non elencate nella tabella NON DEVONO essere presenti.

.. list-table:: (Q)EAA Provider Sign/Seal Certificate Extensions
   :class: longtable
   :header-rows: 1
   :widths: 25 75

   * - **Extension**
     - **Description**

   * - ``authorityKeyIdentifier``
     - REQUIRED. Il valore DOVREBBE essere derivato dalla chiave pubblica utilizzando i metodi definiti in :rfc:`5280#section-4.2.1.1`.

   * - ``subjectKeyIdentifier``
     - OPTIONAL. Se presente, il campo ``keyIdentifier`` DOVREBBE essere derivato dalla chiave pubblica del subject utilizzando i metodi definiti in :rfc:`5280#section-4.2.1.2`.

   * - ``keyUsage``
     - REQUIRED. DEVE contenere una (e una sola) delle impostazioni key-usage *Type A*, *Type B* o *Type F*.
       Per ulteriori dettagli, vedere Clause 4.3.2 [`ETSI EN 319 412-2`_] e Clause 4.3.1 [`ETSI EN 319 412-3`_].

   * - ``certificatePolicies``
     - REQUIRED. TBD.

   * - ``subjectAltName``
     - REQUIRED.

   * - ``cRLDistributionPoints``
     - CONDITIONAL. **REQUIRED IF:** il certificato non include alcuna access location di un OCSP responder o l'extension validity assured definita in `ETSI EN 319 412-1`_.

   * - ``authorityInfoAccess``
     - REQUIRED (solo per QEAA). DEVE includere una struttura ``AccessDescription`` con ``accessMethod`` impostato a ``1.3.6.1.5.5.7.48.2`` (``id-ad-caIssuers``) e ``accessLocation`` che specifichi almeno una access location di un certificato CA valido della CA emittente.

       Se l'OCSP è supportato dalla CA emittente, l'extension DEVE includere una struttura ``AccessDescription`` con ``accessMethod`` impostato a ``1.3.6.1.5.5.7.48.1`` (``id-ad-ocsp``) e ``accessLocation`` che specifichi almeno un OCSP responder autorizzato a fornire informazioni sullo stato del certificato, come descritto in :ref:`infrastructure-trust:Online Certificate Status Protocol (OCSP)`.

   * - ``qcStatements``
     - REQUIRED (solo per QEAA). DEVE contenere una struttura ``QCStatement`` tra quelle definite nella Clause 4.2 di [`ETSI EN 319 412-5`_].

Per entrambi i QEAA ed EAA Provider, se gestiscono il lifecycle delle Credenziali Digitali che emettono e utilizzano signed revocation list quali Token Status List, DEVONO utilizzare lo stesso Sign/Seal Certificate per firmare/sigillare la revocation list.

Di seguito un esempio non normativo di QEAA Provider Sign/Seal Certificate per legal persons.

.. literalinclude:: ../../examples/qeaa-sign-seal.txt
  :language: text

PuB-EAA Provider Sign/Seal Certificate
""""""""""""""""""""""""""""""""""""""

.. warning::

  Sebbene i requisiti specifici per i PuB-EAA Provider Sign/Seal Certificates specificati nella Clause 8 di [`ETSI TS 119 412-6`_] non richiedano che questo profilo sia qualified, l'art. 45f(1)(b) di [`EU_2024_1183`_] richiede che le Attestation di tipo PuB-EAA siano firmate con un certificato qualificato. Per soddisfare entrambi i requisiti, sebbene non sia indicato né nell'[`EIDAS-ARF`_] né in [`ETSI TS 119 412-6`_], questo profilo unisce i profili QEAA e PuB-EAA Provider Sign/Seal Certificate specificati nelle Clauses 6, 7 e 8 di [`ETSI TS 119 412-6`_].

La tabella seguente definisce l'insieme completo delle extensions applicabili al certificate profile.
Le extensions non elencate nella tabella NON DEVONO essere presenti.

.. list-table:: PuB-EAA Provider Sign/Seal Certificate Extensions
   :class: longtable
   :header-rows: 1
   :widths: 25 75

   * - **Extension**
     - **Description**

   * - ``authorityKeyIdentifier``
     - REQUIRED. Il valore DOVREBBE essere derivato dalla chiave pubblica utilizzando i metodi definiti in :rfc:`5280#section-4.2.1.1`.

   * - ``subjectKeyIdentifier``
     - OPTIONAL. Se presente, il campo ``keyIdentifier`` DOVREBBE essere derivato dalla chiave pubblica del subject utilizzando i metodi definiti in :rfc:`5280#section-4.2.1.2`.

   * - ``keyUsage``
     - REQUIRED.

   * - ``certificatePolicies``
     - REQUIRED. DEVE includere una struttura ``PolicyInformation`` con ``policyIdentifier`` impostato all'OID di una certificate policy che includa almeno i requisiti per *NCP+*, definiti in `ETSI EN 319 411-1`_, per conformarsi al requisito `EIDAS-ARF`_ ``AS-AP-10-103``.

   * - ``subjectAltName``
     - REQUIRED.

   * - ``cRLDistributionPoints``
     - CONDITIONAL. **REQUIRED IF:** il certificato non include alcuna access location di un OCSP responder o l'extension validity assured definita in `ETSI EN 319 412-1`_.

   * - ``authorityInfoAccess``
     - REQUIRED. DEVE includere una struttura ``AccessDescription`` con ``accessMethod`` impostato a ``1.3.6.1.5.5.7.48.2`` (``id-ad-caIssuers``) e ``accessLocation`` che specifichi almeno una access location di un certificato CA valido della CA emittente.

       Se l'OCSP è supportato dalla CA emittente, l'extension DEVE includere una struttura ``AccessDescription`` con ``accessMethod`` impostato a ``1.3.6.1.5.5.7.48.1`` (``id-ad-ocsp``) e ``accessLocation`` che specifichi almeno un OCSP responder autorizzato a fornire informazioni sullo stato del certificato, come descritto in :ref:`infrastructure-trust:Online Certificate Status Protocol (OCSP)`.

   * - ``qcStatements``
     - REQUIRED. DEVE contenere le seguenti strutture ``QCStatement``:
        
        - una con ``statementId`` impostato all'OID corrispondente a ``id-etsi-qcs-QcPSB``. Il corrispondente ``statementInfo`` DEVE contenere una struttura ``QcPSB`` che includa i campi definiti nella Clause 8.3 di [`ETSI TS 119 412-6`_].
        - una come definita nella Clause 4.2 di [`ETSI EN 319 412-5`_].

.. warning::

  L'Annex A di [`ETSI TS 119 412-6`_] non definisce l'OID specifico dell'identificatore di statement ``id-etsi-qcs-QcPSB``.

Di seguito un esempio non normativo di PuB-EAA Provider Sign/Seal Certificate per legal persons.

.. literalinclude:: ../../examples/pubeaa-sign-seal.txt
  :language: text

Trust Anchor Certificate Profile
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Questa sezione estende il generale :ref:`infrastructure-trust:X.509 Certificate Profile` e specifica un **Certificate Profile** per i **Trust Anchors**.
Un Trust Anchor è una chiave pubblica affidabile (e dati associati) utilizzata come input dell':ref:`trust-evaluation:X509 Certificate Chain Validation Algorithm`.
In questo profilo, il Trust Anchor DEVE essere rappresentato e distribuito come **certificato X.509**, che PUÒ essere self-signed.

Le Relying Party, i Credential Issuer e le Wallet Unit validano un Access, Registration o Sign/Seal Certificate presentato costruendo un certification path che DEVE terminare con un certificato firmato dal subject di un certificato Trust Anchor.
Il certificato Trust Anchor è utilizzato come trust termination point per il processo di path validation (cioè è il valore della variabile ``trust_anchor`` in :ref:`trust-evaluation:X509 Certificate Chain Validation Algorithm`).
Le implementazioni DEVONO supportare la validazione sia di certificati Trust Anchor self-signed sia non self-signed.

.. note::
  **Trust Anchor Location.**
  La posizione del Trust Anchor Certificate è determinata dal Trust Framework specifico selezionato (vedere :ref:`trust-evaluation:EUDIW Trust Anchor Validation` e :ref:`trust-evaluation:Federation Trust Anchor Validation`).


La tabella seguente definisce i requisiti specifici del profilo per i campi del certificato.
I campi non elencati nella tabella restano soggetti ai requisiti definiti nel comune :ref:`infrastructure-trust:X.509 Certificate Profile`.

.. list-table:: Trust Anchor Certificate Fields
   :class: longtable
   :header-rows: 1
   :widths: 30 70

   * - **Field**
     - **Additional Requirements**

   * - ``issuer``
     - Se il certificato è self-signed, l'issuer DN DEVE essere identico al subject DN.
       Altrimenti, l'issuer DN DEVE identificare l'entità che ha firmato ed emesso il certificato e PUÒ differire dal subject DN.

   * - ``subject``
     - Il subject DN DEVE identificare l'entità associata alla chiave pubblica del Trust Anchor in modo chiaro e non ambiguo.
       Se il Trust Anchor rappresenta un'entità legale o organizzativa, il subject DN DEVE contenere un attributo ``organizationName`` che identifichi tale entità.


.. list-table:: Trust Anchor Certificate Extensions
   :class: longtable
   :header-rows: 1
   :widths: 25 75

   * - **Extension**
     - **Description**

   * - ``authorityKeyIdentifier``
     - CONDITIONAL. **REQUIRED IF:** il certificato non è self-signed.
       Per i certificati self-signed, è RECOMMENDED.
       Se presente, il valore DOVREBBE essere derivato dalla chiave pubblica utilizzando i metodi definiti in :rfc:`5280#section-4.2.1.1`.

   * - ``subjectKeyIdentifier``
     - REQUIRED. Fornisce un key identifier per la chiave pubblica del Trust Anchor.
       Il campo ``keyIdentifier`` DOVREBBE essere derivato dalla chiave pubblica del subject utilizzando i metodi definiti in :rfc:`5280#section-4.2.1.2`.

   * - ``keyUsage``
     - REQUIRED. DEVE asserire il bit ``keyCertSign``.
       PUÒ asserire il bit ``cRLSign`` se il certificato Trust Anchor è utilizzato dalla CA per firmare le CRL.
       DOVREBBE essere limitato agli usi coerenti con il ruolo CA del certificato Trust Anchor.

   * - ``certificatePolicies``
     - OPTIONAL. PUÒ includere una struttura ``PolicyInformation`` rilevante per le pratiche della CA emittente.

   * - ``basicConstraints``
     - REQUIRED. Il campo ``cA`` DEVE essere impostato a ``TRUE``, segnalando la capacità CA per la X.509 path validation.
       Il ``pathLenConstraint`` PUÒ essere presente; in tal caso, DEVE limitare il numero di certificati intermediate CA non self-issued al di sotto di questo Trust Anchor.
       Si RACCOMANDA di impostare ``pathLenConstraint`` a 0 per prevenire livelli subordinate CA aggiuntivi, salvo documentata esigenza operativa di supportare ulteriori livelli intermediate CA.

   * - ``cRLDistributionPoints``
     - OPTIONAL. PUÒ includere URI di CRL distribution point, quando è utilizzata la revoca basata su CRL.

   * - ``authorityInfoAccess``
     - CONDITIONAL. **REQUIRED IF:** il certificato contiene ``basicConstraints`` con ``pathLenConstraint`` > 0.
       Se presente, DEVE includere una struttura ``AccessDescription`` con ``accessMethod`` impostato a ``1.3.6.1.5.5.7.48.2`` (``id-ad-caIssuers``) e un ``accessLocation`` che DEVE utilizzare lo schema ``http://`` e NON DEVE utilizzare lo schema ``https://``.

       PUÒ anche includere una struttura ``AccessDescription`` con ``accessMethod`` impostato a ``1.3.6.1.5.5.7.48.1`` (``id-ad-ocsp``) e ``accessLocation`` che specifichi almeno un OCSP responder autorizzato a fornire informazioni sullo stato del certificato, quando è utilizzata la revoca basata su OCSP.

.. note::
  **Trust Anchor Revocation.**
  I certificati Trust Anchor non sono soggetti a revoca, poiché il loro trust è stabilito per policy mediante la loro inclusione formale e pubblicazione come specificato dal Trust Framework applicabile.
  Di conseguenza, non sono richieste informazioni sullo stato di revoca, quali CRL o OCSP response, per i certificati Trust Anchor.

  Inoltre, le entità di validazione che utilizzano certificati Trust Anchor recuperati come specificato dal Trust Framework applicabile POSSONO omettere i controlli sullo stato di revoca per tali certificati.

.. note::
  **Trust Anchor Signature.**
  Un certificato Trust Anchor PUÒ essere self-signed (rappresentando una root CA) o non self-signed (rappresentando una intermediate CA designata come Trust Anchor per policy).
  Le Relying Party NON DEVONO richiedere un issuer aggiuntivo al di sopra di un Trust Anchor recuperato come specificato dal Trust Framework applicabile, anche se non è self-signed, poiché il Trust Anchor è un input autorevole all'algoritmo di path validation designato per policy.

.. note::

  Come descritto nella Section 4.3.1 di [`EUDI-TS 12`_], il Trust Anchor di un EAA Sign/Seal Certificate è referenziato nell'attributo ``trustedAuthority`` dell'Attestation Rulebook machine-readable per lo specifico EAA.

Di seguito un esempio non normativo di Trust Anchor Certificate.

.. literalinclude:: ../../examples/trust-anchor-cert.txt
  :language: text

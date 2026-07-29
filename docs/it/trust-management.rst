.. include:: ../common/common_definitions.rst
.. Included via infrastructure-trust.rst at title level '-' (level 1).

Trust Management and Lifecycle
------------------------------
Questa sezione descrive il ciclo di vita dei Trust Artifacts (:ref:`infrastructure-trust:Trust Artifacts Lifecycle State Machine`) e i meccanismi usati per gestirne lo stato (:ref:`infrastructure-trust:Revocation Mechanisms`).
Il ciclo di vita delle Entity, gli eventi che modificano la loro registrazione e gli effetti che tali eventi producono sui Trust Artifacts sono descritti in :ref:`onboarding-system:Lifecycle Management`.

Trust Artifacts Lifecycle State Machine
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Le State Machine per i Trust Artifacts sono descritte di seguito:

- Per WRPAC, WRPRC e Sign/Seal Certificates, gli stati del ciclo di vita sono ``VALID`` e ``REVOKED``.
  La transizione da ``VALID`` a ``REVOKED`` è innescata dalla revoca del Trust Artifact, che può essere avviata dal corrispondente provider del Trust Artifact per vari motivi, quali compromissione delle chiavi, cambiamenti organizzativi o non conformità alle policy del framework.
  Una volta che un Trust Artifact è nello stato ``REVOKED``, NON DEVE essere considerato attendibile per alcun uso operativo nell'ecosistema, e qualsiasi Entity che vi faccia affidamento DEVE rifiutarlo per autenticazione, autorizzazione o qualsiasi altra operazione relativa al trust.

  - Un WRPAC nello stato ``VALID`` NON DEVE essere presente nella CRL designata e/o DEVE restituire uno stato ``good`` nella risposta OCSP.
    Un WRPAC nello stato ``REVOKED`` DEVE essere presente nella CRL designata e/o DEVE restituire uno stato ``revoked`` nella risposta OCSP.
  - Un WRPRC nello stato ``VALID`` DEVE restituire uno stato ``0x00`` nel corrispondente Status List Token.
    Un WRPRC nello stato ``REVOKED`` DEVE avere valore di stato ``0x01`` nel corrispondente Status List Token.
- Per le Trust List (LoTE, LOTL, EUMS TL), gli stati del ciclo di vita sono ``CURRENT`` e ``HISTORICAL``.
  La transizione da ``CURRENT`` a ``HISTORICAL`` è innescata dalla pubblicazione di una nuova versione della Trust List che sostituisce la versione precedente.
  Una volta che una Trust List è nello stato ``HISTORICAL``, NON DEVE essere usata per alcun uso operativo nell'ecosistema.
  Si applicano due eccezioni: la validazione dell'attendibilità della Trust List tramite il pivoting mechanism, e la validazione delle operazioni storiche tramite il componente ``ServiceHistory`` della Trust List.
- Trust Marks: lo stato di un Trust Mark è ``ACTIVE``, ``EXPIRED``, ``REVOKED``.
  Lo stato può essere verificato usando l'endpoint Trust Mark Status (vedi Section 8.4 di `OID-FED`_).

.. note::
  Register, Entity Configurations e Subordinate Statements sono semplicemente pubblicati o non pubblicati.
  Durante la loro pubblicazione possono essere aggiornati.

Il diagramma :numref:`fig_Trust_Artifacts_States` evidenzia la state machine dei Trust Artifacts sopra menzionati:

.. _fig_Trust_Artifacts_States:
.. plantuml:: plantuml/trust-artifacts-states.puml
    :width: 90%
    :caption: `Trust Artifacts States. <https://www.plantuml.com/plantuml/svg/PL5TRzCm57tFhpZQquOwyRu7j2eBB29RgyGK942Rbzmr5aaSNTk52l7ViLENj28lbdFl-JZ7jyPAjgxlabOr1Ef7kqT3fcOrMgM79F4Bbd2H4blrgcf_CRZyNAwNwGB-AFrHgUqWhMDwMv7ihYuW3SB-1zPknEy4mDSttt5z_GwRPP7VuGQvCKuEDVbP_1UcPRPPVSp2lAIThcLm0C5gkoN6j-4oBOi5LccrNa0pAkj53Gfbx5K2HFI1AUZTG13tQf3Tj4h9dtzf13jZ9wGFKsYHBL2iX2SNnMJVdxFvsRqedj9FPPaz2a--TY-TYXxrArB7J8F5XjY4uW8kgaLC93vI98XV0fmo1w7xl1AhCa-NXHUgtEWvgQ46Btiyqi-ZHgX4j0JTDT03GHb8hbkryvjMuxaYtgcQxdrCpVldKD8fS-pflreU9Fym1xCFnnQIEKsiEIuynUlf8ozJaM-o-P4XXmRZULqIivZ7Him4pxwiypAxkq78Hhz6nGUKLVsKaKdMBJNdgDbA1BwdXY9mwMohMTczBuofrrC_BPqxE24uRUQMXiRrtLy0>`_


Revocation Mechanisms
^^^^^^^^^^^^^^^^^^^^^

Questa sezione descrive gli artifact impiegati in :ref:`infrastructure-trust:Trust Artifacts Lifecycle State Machine` per gestire lo stato di certificati ed entità, dettagliando i rispettivi formati e parametri.
La distinzione principale è la seguente:

- Per gestire i Wallet-Relying Party Access Certificates e i Sign/Seal Certificates, le entità che agiscono come Trust Anchor per questi certificati DEVONO:

  - rendere disponibile almeno un meccanismo di revoca tra :ref:`infrastructure-trust:Certificate Revocation List (CRL)` e :ref:`infrastructure-trust:Online Certificate Status Protocol (OCSP)`;
  - emettere WRPAC e Sign/Seal Certificates con almeno un'estensione corrispondente al meccanismo di revoca fornito.

- Per gestire i Wallet-Relying Party Registration Certificates, ciascun Provider di Wallet Relying Party Registration Certificates DEVE:

  - rendere disponibile un endpoint per richiedere :ref:`infrastructure-trust:Status List Token (SLT)`;
  - emettere WRPRC con l'appropriato parametro ``status`` come descritto in :ref:`infrastructure-trust:Wallet-Relying Party Registration Certificate (WRPRC) Profile`.

.. note::
  `ETSI EN 319 411-1`_ raccomanda il supporto di OCSP, vedi clause CSS-6.3.10-06 e Note 2.

Certificate Revocation List (CRL)
"""""""""""""""""""""""""""""""""

Le **Certificate Revocation Lists (CRL)** sono usate per verificare lo stato di revoca di un certificato X509.
Una CRL è un elenco firmato digitalmente di certificati revocati emessi da una CA.
La CRL è pubblicata e resa disponibile a qualsiasi entità tramite una URI pubblicamente accessibile.
La CRL DEVE essere firmata digitalmente dal **CRL issuer**.

Le CRL POSSONO essere usate per i seguenti tipi di certificati:

- Wallet Relying Party Access Certificates includendo l'estensione ``cRLDistributionPoints`` nel certificato, come descritto in `:ref:trust-artifact-eudiw:Wallet-Relying Party Access Certificate`.
- Sign/Seal Certificates includendo l'estensione ``cRLDistributionPoints`` nel certificato, come descritto in `:ref:trust-artifact-eudiw:Sign/Seal Certificate`.

Se una CRL è usata per gestire lo stato dei certificati, il CRL issuer DEVE essere l'entità referenziata nel campo ``subject`` del certificato Trust Anchor.

Il CRL issuer PUÒ anche generare delta CRL.
Una delta CRL elenca solo i certificati, nel proprio ambito, il cui stato di revoca è cambiato dall'emissione di una CRL completa referenziata.
La CRL completa referenziata è indicata come base CRL.
L'ambito di una delta CRL DEVE essere lo stesso della base CRL a cui fa riferimento.

Se supportata dalla CA, la CRL DEVE essere disponibile all'URI specificato nella struttura ``cRLDistributionPoints.distributionPoint`` *[0] CHOICE* all'interno del Wallet Relying Party Access Certificate (WRPAC).

Una CRL X.509 v2 è rappresentata come codifica ASN.1 DER della SEQUENCE ``CertificateList``.
La codifica ASN.1 DER è un sistema di codifica tag, length e value rigorosamente definito per ciascun elemento.
I byte finali trasmessi rappresentano la codifica DER della SEQUENCE di livello superiore contenente i campi della tabella seguente:

.. list-table:: Top-Level CertificateList Structure
   :class: longtable
   :widths: 20 60 20
   :header-rows: 1

   * - **Parameter**
     - **Description**
     - **Reference**

   * - ``tbsCertList``
     - REQUIRED. *SEQUENCE*. Contiene le informazioni principali della CRL, inclusi il nome dell'issuer, la data di emissione, la data del prossimo aggiornamento, l'elenco opzionale dei certificati revocati e le estensioni CRL opzionali.
     - :rfc:`5280`, clause 5.1.1.1

   * - ``signatureAlgorithm``
     - REQUIRED. *SEQUENCE*. Contiene l'identificatore dell'algoritmo usato dal CRL issuer per firmare il ``CertificateList``.
       La selezione DOVREBBE allinearsi agli standard rilevanti (es. [ETSI TS 119 312]).
     - :rfc:`5280`, clause 5.1.1.2

   * - ``signatureAlgorithm.algorithm``
     - REQUIRED. *OBJECT IDENTIFIER*. L'OID dell'algoritmo di firma.
     - [:rfc:`5280`, clause 4.1.1.2]

   * - ``signatureAlgorithm.parameters``
     - OPTIONAL. *ANY*. Parametri specifici dell'algoritmo, dipendenti dall'algoritmo di firma usato.
     - [:rfc:`5280`, clause 4.1.1.2]

   * - ``signatureValue``
     - REQUIRED. *BIT STRING*. Contiene la firma digitale calcolata sulla codifica ASN.1 DER del ``tbsCertList``.
     - [:rfc:`5280`, clause 5.1.1.3]

Certificate List Content
.........................

Il ``tbsCertList`` (To Be Signed Certificate List) è una SEQUENCE ASN.1 contenente diversi campi ed estensioni.
La tabella seguente elenca tutti tali campi ed estensioni richiesti in una CRL o condizionalmente richiesti.

.. list-table:: tbsCertList Fields and Extensions
   :class: longtable
   :widths: 20 60 20
   :header-rows: 1

   * - **Parameter**
     - **Description**
     - **Reference**

   * - ``version``
     - OPTIONAL. *INTEGER*. Descrive la versione della CRL codificata.
       Quando sono usate estensioni (come da prassi standard), questo campo DEVE essere presente e DEVE specificare la versione 2 (il valore intero è ``1``).
     - [:rfc:`5280`, clause 5.1.2.1]

   * - ``signature``
     - REQUIRED. *SEQUENCE*. L'identificatore dell'algoritmo usato per firmare la CRL.
     - [:rfc:`5280`, clause 5.1.2.2]

   * - ``signature.algorithm``
     - REQUIRED. *OBJECT IDENTIFIER*. L'OID dell'algoritmo di firma.
       DEVE corrispondere al campo ``signatureAlgorithm`` nella sequence ``CertificateList`` padre.
     - [:rfc:`5280`, clause 4.1.1.2]

   * - ``signature.parameters``
     - OPTIONAL. *ANY*. Parametri specifici dell'algoritmo, dipendenti dall'algoritmo usato.
     - [:rfc:`5280`, clause 4.1.1.2]

   * - ``issuer``
     - REQUIRED. *Name*. Identifica l'entità che ha firmato ed emesso la CRL.
       DEVE contenere un distinguished name (DN) X.500 non vuoto composto da sequence ``AttributeType`` (OID) e ``AttributeValue``.
     - [:rfc:`5280`, clause 5.1.2.3]

   * - ``thisUpdate``
     - REQUIRED. *UTCTime* o *GeneralizedTime*. Indica la data di emissione di questa CRL.
       Le date fino al 2049 DEVONO usare ``UTCTime``; le date nel 2050 o successive DEVONO usare ``GeneralizedTime``.
     - [:rfc:`5280`, clause 5.1.2.4]

   * - ``nextUpdate``
     - REQUIRED. *UTCTime* o *GeneralizedTime*. Indica la data entro cui sarà emessa la prossima CRL.
       Le date fino al 2049 DEVONO usare ``UTCTime``; le date nel 2050 o successive DEVONO usare ``GeneralizedTime``.
     - [:rfc:`5280`, clause 5.1.2.5]

   * - ``revokedCertificates``
     - OPTIONAL. *SEQUENCE OF*. Una sequence di certificati revocati.
       Quando non ci sono certificati revocati, questo campo DEVE essere assente.
     - [:rfc:`5280`, clause 5.1.2.6]

   * - ``revokedCertificates.userCertificate``
     - REQUIRED. *INTEGER*. Il ``CertificateSerialNumber`` del certificato revocato.
     - [:rfc:`5280`, clause 5.1.2.6]

   * - ``revokedCertificates.revocationDate``
     - REQUIRED. *UTCTime* o *GeneralizedTime*. La data in cui è avvenuta la revoca.
     - [:rfc:`5280`, clause 5.1.2.6]

   * - ``revokedCertificates.crlEntryExtensions``
     - OPTIONAL. *SEQUENCE OF*. Estensioni specifiche per questa voce di certificato revocato.
       Se presente, la ``version`` della CRL DEVE essere ``v2``.
     - [:rfc:`5280`, clause 5.1.2.6]

   * - ``crlExtensions``
     - OPTIONAL. *[0] EXPLICIT SEQUENCE OF*. Una sequence di una o più estensioni CRL.
       Se presente, la ``version`` della CRL DEVE essere ``v2``.
     - [:rfc:`5280`, clause 5.1.2.7]

Il campo ``crlExtensions`` PUÒ contenere varie estensioni.
Le estensioni standard rilevanti includono:

.. list-table:: Notable crlExtensions
   :class: longtable
   :widths: 20 60 20
   :header-rows: 1

   * - **Parameter**
     - **Description**
     - **Reference**

   * - ``authorityKeyIdentifier``
     - REQUIRED. *SEQUENCE*. Fornisce un mezzo per identificare la chiave pubblica corrispondente alla chiave privata usata per firmare la CRL.
       Contiene ``keyIdentifier`` (OCTET STRING), ``authorityCertIssuer`` o ``authorityCertSerialNumber``.
     - :rfc:`5280`, clause 5.2.1

   * - ``cRLNumber``
     - REQUIRED. *INTEGER*. Un'estensione non critica che trasmette un numero di sequence monotonicamente crescente per un dato ambito CRL e issuer.
       Sia le base CRL sia le delta CRL condividono la stessa sequence monotonicamente crescente; il numero della delta CRL DEVE essere maggiore del numero della base CRL a cui fa riferimento.
     - :rfc:`5280`, clause 5.2.3

   * - ``deltaCRLIndicator``
     - REQUIRED per le delta CRL; NON DEVE comparire nelle base CRL. *INTEGER* (``BaseCRLNumber``). Un'estensione **critica** che contrassegna la CRL come delta CRL e identifica la base CRL a cui è relativa.
       Il valore intero è il ``cRLNumber`` della base CRL su cui questa delta è costruita.
       Una relying party che non comprende questa estensione DEVE rifiutare la CRL.
       La base CRL DEVE essere ancora raggiungibile (in cache o recuperabile) affinché la delta sia utile.
       Se questa estensione è assente, la CRL è una CRL completa (base).
     - :rfc:`5280`, clause 5.2.4

   * - ``freshestCRL`` (a.k.a.
       *CRL Distribution Points* on a CRL)
     - OPTIONAL; RECOMMENDED sulle base CRL nei deployment che emettono delta CRL. *SEQUENCE OF DistributionPointName*. Un'estensione non critica che indica dove può essere recuperata la delta CRL più recentemente emessa per lo stesso ambito.
       Ciascun ``DistributionPointName`` trasporta una o più URI (tipicamente ``uniformResourceIdentifier``).
       Quando presente su una base CRL, DEVE puntare alla location di distribuzione della delta CRL; quando presente su una delta CRL, punta alla delta CRL successiva.
       Una relying party lo usa per scoprire le delta senza configurazione aggiuntiva out-of-band.
     - :rfc:`5280`, clause 5.2.6

   * - ``issuingDistributionPoint``
     - OPTIONAL; REQUIRED quando l'ambito della CRL è ristretto (es. only-CA, only-end-entity, only-some-reasons) o quando la CRL è indiretta. *SEQUENCE* (``IssuingDistributionPoint``). Un'estensione **critica** che descrive l'ambito della CRL.
       Contiene i flag ``distributionPoint``, ``onlyContainsUserCerts``, ``onlyContainsCACerts``, ``onlySomeReasons``, ``indirectCRL`` e ``onlyContainsAttributeCerts``.
       Per i deployment delta-CRL, il bit ``indirectCRL`` è impostato a TRUE quando la delta è firmata da un CRL issuer diverso dalla Certificate Authority che ha emesso i certificati (comune quando è usato un servizio di revoca delegato), e ``onlySomeReasons`` PUÒ restringere la delta CRL a specifici motivi di revoca (es. solo ``keyCompromise``).
       La base CRL e le corrispondenti delta CRL DEVONO condividere lo stesso ambito (stessi flag ``onlyContains*`` e ``distributionPoint``).
     - :rfc:`5280`, clause 5.2.5

Online Certificate Status Protocol (OCSP)
""""""""""""""""""""""""""""""""""""""""""""

L'Online Certificate Status Protocol (OCSP) (:rfc:`6960`) consente alle applicazioni di determinare lo stato esatto di revoca dei certificati identificati.
Fornisce informazioni di revoca più tempestive di quanto sia tipicamente possibile con le CRL e PUÒ anche essere usato per ottenere informazioni di stato aggiuntive.

Un client OCSP emette una richiesta di stato a un OCSP responder e DEVE sospendere l'accettazione dei certificati in questione finché il responder non fornisce una risposta valida.

Se supportato dalla Certificate Authority, l'URI a cui può essere invocato l'OCSP Responder DEVE essere presente nell'estensione ``authorityInfoAccess.accessLocation`` del Wallet Relying Party Access Certificate (WRPAC).

Questo protocollo specifica i dati che DEVONO essere scambiati tra il client OCSP (che verifica lo stato di uno o più certificati) e il server OCSP (che fornisce lo stato corrispondente).

La tabella seguente riassume i ruoli del client e del server OCSP nell'ecosistema EUDIW.

.. list-table:: OCSP roles in the EUDIW ecosystem
   :class: longtable
   :widths: 28 28 44
   :header-rows: 1

   * - **OCSP Client**
     - **OCSP Server**
     - **Use case**
   * - Wallet Unit
     - WRPAC Provider
     - WRPAC Status Check
   * - Wallet Unit or Relying Party
     - PID Provider Trust Anchor
     - PID Sign/Seal Certificate Status Check
   * - Wallet Unit or Relying Party
     - PuB-EAA Provider Trust Anchor
     - PuB-EAA Sign/Seal Certificate Status Check
   * - Wallet Unit or Relying Party
     - (Q)EAA Provider Trust Anchor
     - (Q)EAA Sign/Seal Certificate Status Check

.. note::
    Il controllo di stato sui Sign/Seal Certificates è necessario solo nel caso in cui il Sign/Seal Certificate non sia referenziato direttamente come Trust Anchor Certificate, nel qual caso è considerato attendibile a priori e non necessita di un controllo di stato separato.

Online Certificate Status Protocol Request Format
....................................................

La richiesta OCSP DEVE essere la codifica ASN.1 DER della SEQUENCE ``OCSPRequest``, che contiene il ``tbsRequest`` (To-Be-Signed Request) e una firma opzionale.
La tabella seguente elenca i parametri presenti nella struttura ``tbsRequest``.

.. list-table:: tbsRequest Structure Parameters
   :class: longtable
   :widths: 20 60 20
   :header-rows: 1

   * - **Parameter**
     - **Description**
     - **Reference**

   * - ``version``
     - OPTIONAL. *[0] EXPLICIT INTEGER*. Indica la versione del protocollo.
       Se omesso, il valore predefinito è ``v1`` (0).
     - [:rfc:`6960`, clause 4.1.1]

   * - ``requestList``
     - REQUIRED. *SEQUENCE OF*. Contiene una o più richieste di stato di singoli certificati.
     - [:rfc:`6960`, clause 4.1.1]

   * - ``requestList.reqCert``
     - REQUIRED. *SEQUENCE*. La struttura ``CertID`` che trasporta l'identificatore di un certificato target.
     - [:rfc:`6960`, clause 4.1.1]

   * - ``requestList.singleRequestExtensions``
     - OPTIONAL. *[0] EXPLICIT SEQUENCE*. Include estensioni applicabili a questa singola richiesta di stato del certificato.
     - [:rfc:`6960`, clause 4.1.1]

   * - ``requestExtensions``
     - OPTIONAL. *[2] EXPLICIT SEQUENCE*. Include estensioni applicabili alle richieste complessive presenti nel ``requestList``.
     - [:rfc:`6960`, clause 4.1.1]

Il parametro ``reqCert`` utilizza la struttura ``CertID``, DEVE essere una *SEQUENCE* ASN.1 contenente i seguenti parametri:

.. list-table:: CertID Structure Parameters
   :class: longtable
   :widths: 20 60 20
   :header-rows: 1

   * - **Parameter**
     - **Description**
     - **Reference**

   * - ``hashAlgorithm``
     - REQUIRED. *SEQUENCE*. Identifica l'algoritmo di hash usato per generare gli hash del nome dell'issuer e della chiave.
     - [:rfc:`6960`, clause 4.1.1]

   * - ``hashAlgorithm.algorithm``
     - REQUIRED. *OBJECT IDENTIFIER*. L'OID della funzione di hash (es. SHA-256, a seconda del profilo).
     - [:rfc:`6960`, clause 4.1.1]

   * - ``hashAlgorithm.parameters``
     - OPTIONAL. *ANY*. Parametri specifici dell'algoritmo, dipendenti dall'algoritmo di hash usato.
     - [:rfc:`6960`, clause 4.1.1]

   * - ``issuerNameHash``
     - REQUIRED. *OCTET STRING*. L'hash del distinguished name (DN) dell'issuer, calcolato sulla codifica DER del campo name dell'issuer.
     - [:rfc:`6960`, clause 4.1.1]

   * - ``issuerKeyHash``
     - REQUIRED. *OCTET STRING*. L'hash della chiave pubblica dell'issuer, calcolato sul valore (esclusi tag e length) del campo subject public key.
     - [:rfc:`6960`, clause 4.1.1]

   * - ``serialNumber``
     - REQUIRED. *INTEGER*. Il serial number del certificato target per il quale è richiesto lo stato.
     - [:rfc:`6960`, clause 4.1.1]

Le strutture ``requestExtensions`` e ``singleRequestExtensions`` POSSONO contenere varie estensioni.
La tabella seguente elenca quelle richieste:

.. list-table:: OCSP Nonce Extension
   :class: longtable
   :widths: 20 60 20
   :header-rows: 1

   * - **Parameter**
     - **Description**
     - **Reference**

   * - ``nonce``
     - REQUIRED. *OCTET STRING*. Valore crittograficamente fresh usato per vincolare una richiesta e una risposta al fine di prevenire replay attack.
       L'identificatore OID è ``id-pkix-ocsp-nonce``.
     - [:rfc:`6960`, clause 4.4.1]

Quando inviata su HTTP usando POST, il body di questa richiesta DEVE contenere la codifica DER grezza di questa SEQUENCE ``OCSPRequest`` e DEVE avere MIME type ``application/ocsp-request``.

Di seguito un esempio non normativo di richiesta OCSP:

.. literalinclude:: ../../examples/ocsp-request.txt
  :language: text

Online Certificate Status Protocol Response Format
...................................................

Una risposta OCSP DEVE essere la codifica ASN.1 DER della *SEQUENCE* ``OCSPResponse``.
Quando trasportata su HTTP, il body della risposta HTTP DEVE contenere la codifica DER grezza di questo ``OCSPResponse``, con MIME type ``application/ocsp-response``.
La *SEQUENCE* ``OCSPResponse`` contiene i seguenti parametri:

.. list-table:: OCSPResponse Structure Parameters
   :class: longtable
   :widths: 20 60 20
   :header-rows: 1

   * - **Parameter**
     - **Description**
     - **Reference**

   * - ``responseStatus``
     - REQUIRED. *ENUMERATED*. Indica lo stato di elaborazione della richiesta precedente.
       I valori supportati sono: ``successful`` (0), ``malformedRequest`` (1), ``internalError`` (2), ``tryLater`` (3), ``sigRequired`` (5) e ``unauthorized`` (6).
     - [:rfc:`6960`, clause 4.2.1]

   * - ``responseBytes``
     - OPTIONAL. *[0] EXPLICIT SEQUENCE*. Presente solo quando ``responseStatus`` è ``successful`` (0).
       Contiene il tipo di risposta e i dati di risposta codificati.
     - [:rfc:`6960`, clause 4.2.1]

   * - ``responseBytes.responseType``
     - REQUIRED. *OBJECT IDENTIFIER*. Identificatore del tipo di risposta.
       Per un OCSP responder di base, questo valore DEVE essere ``id-pkix-ocsp-basic``.
     - [:rfc:`6960`, clause 4.2.1]

   * - ``responseBytes.response``
     - REQUIRED. *OCTET STRING*. Contiene la codifica DER della sintassi di risposta identificata da ``responseType`` (es. la struttura ``BasicOCSPResponse``).
     - [:rfc:`6960`, clause 4.2.1]

.. note::
   Gli OCSP responder DEVONO essere in grado di produrre risposte del tipo ``id-pkix-ocsp-basic``.
   Di conseguenza, gli OCSP client DEVONO essere in grado di ricevere ed elaborare risposte del tipo ``id-pkix-ocsp-basic``.

``BasicOCSPResponse`` è una SEQUENCE ASN.1 contenente i seguenti parametri:

.. list-table:: BasicOCSPResponse Structure Parameters
   :class: longtable
   :widths: 20 60 20
   :header-rows: 1

   * - **Parameter**
     - **Description**
     - **Reference**

   * - ``tbsResponseData``
     - REQUIRED. *SEQUENCE*. Contiene i dati di risposta principali da firmare dal responder.
     - [:rfc:`6960`, clause 4.2.1]

   * - ``tbsResponseData.version``
     - OPTIONAL. *[0] EXPLICIT INTEGER*. La versione della sintassi di risposta.
       Se omesso, il valore predefinito è ``v1`` (0).
     - [:rfc:`6960`, clause 4.2.1]

   * - ``tbsResponseData.responderID``
     - REQUIRED. *CHOICE*. Identifica l'OCSP responder.
       DEVE contenere ``byName`` o ``byKey``.
     - [:rfc:`6960`, clause 4.2.1]

   * - ``tbsResponseData.responderID.byName``
     - OPTIONAL. *[1] EXPLICIT Name*. Il ``Name`` dal subject del certificato del responder.
     - [:rfc:`6960`, clause 4.2.1]

   * - ``tbsResponseData.responderID.byKey``
     - OPTIONAL. *[2] EXPLICIT OCTET STRING*. L'hash SHA-1 del ``subjectPublicKey`` del responder (esclusi i campi tag e length).
     - [:rfc:`6960`, clause 4.2.1]

   * - ``tbsResponseData.producedAt``
     - REQUIRED. *GeneralizedTime*. L'ora in cui è stata generata la risposta OCSP.
     - [:rfc:`6960`, clause 4.2.1]

   * - ``tbsResponseData.responses``
     - REQUIRED. *SEQUENCE OF*. Una sequence di strutture ``SingleResponse``, che forniscono lo stato di ciascun certificato richiesto.
     - [:rfc:`6960`, clause 4.2.1]

   * - ``tbsResponseData.responseExtensions``
     - OPTIONAL. *[1] EXPLICIT SEQUENCE OF*. Contiene estensioni applicabili alla risposta OCSP complessiva.
     - [:rfc:`6960`, clause 4.2.1]

   * - ``signatureAlgorithm``
     - REQUIRED. *SEQUENCE*. Identifica l'algoritmo crittografico usato per firmare la risposta.
     - [:rfc:`5280`, clause 4.1.1.2]

   * - ``signatureAlgorithm.algorithm``
     - REQUIRED. *OBJECT IDENTIFIER*. L'OID dell'algoritmo di firma.
       La selezione DOVREBBE allinearsi agli standard rilevanti (es. [ETSI TS 119 312]).
     - [:rfc:`5280`, clause 4.1.1.2]

   * - ``signatureAlgorithm.parameters``
     - OPTIONAL. *ANY*. Parametri specifici dell'algoritmo, dipendenti dall'OID definito in ``algorithm``.
     - [:rfc:`5280`, clause 4.1.1.2]

   * - ``signature``
     - REQUIRED. *BIT STRING*. La firma digitale calcolata sull'hash del ``tbsResponseData`` codificato in DER.
     - [:rfc:`6960`, clause 4.2.1]

   * - ``certs``
     - OPTIONAL. *[0] EXPLICIT SEQUENCE OF*. Catena di certificati per aiutare il client a verificare la firma del responder.
       Se non sono inclusi certificati, questo campo DOVREBBE essere assente.
     - [:rfc:`6960`, clause 4.2.1]

La struttura ``responseExtensions`` PUÒ contenere varie estensioni.
La tabella seguente elenca quelle richieste:

.. list-table:: Response Extensions Nonce
   :class: longtable
   :widths: 20 60 20
   :header-rows: 1

   * - **Parameter**
     - **Description**
     - **Reference**

   * - ``nonce``
     - REQUIRED. *OCTET STRING*. Valore crittograficamente fresh usato per vincolare una richiesta e una risposta al fine di prevenire replay attack.
       Se incluso nella richiesta, i responder DOVREBBERO includerlo nella risposta.
       L'identificatore OID è ``id-pkix-ocsp-nonce``.
     - [:rfc:`6960`, clause 4.4.1]

Nella risposta OCSP DEVE esserci almeno un ``SingleResponse`` per ciascun ``CertID`` nella richiesta.
Ciascun ``SingleResponse`` è una *SEQUENCE* ASN.1 che trasporta i seguenti parametri:

.. list-table:: SingleResponse Structure Parameters
   :class: longtable
   :widths: 20 60 20
   :header-rows: 1

   * - **Parameter**
     - **Description**
     - **Reference**

   * - ``certID``
     - REQUIRED. *SEQUENCE*. Identificatore del certificato il cui stato è determinato in ``certStatus``.
     - [:rfc:`6960`, clause 4.2.1]

   * - ``certStatus``
     - REQUIRED. *CHOICE*. Il valore dello stato del certificato.
       DEVE essere esattamente uno tra: ``good``, ``revoked`` o ``unknown``.
     - [:rfc:`6960`, clause 4.2.1]

   * - ``certStatus.good``
     - OPTIONAL. *[0] IMPLICIT NULL*. Indica che il certificato è valido.
     - [:rfc:`6960`, clause 4.2.1]

   * - ``certStatus.revoked``
     - OPTIONAL. *[1] IMPLICIT SEQUENCE*. Indica che il certificato è stato revocato.
       Contiene la struttura ``RevokedInfo``.
     - [:rfc:`6960`, clause 4.2.1]

   * - ``certStatus.revoked.revocationTime``
     - REQUIRED. *GeneralizedTime*. L'ora in cui il certificato è stato revocato.
     - [:rfc:`6960`, clause 4.2.1]

   * - ``certStatus.revoked.revocationReason``
     - OPTIONAL. *[0] EXPLICIT ENUMERATED*. Contiene il ``CRLReason`` che indica perché il certificato è stato revocato.
     - [:rfc:`6960`, clause 4.2.1]

   * - ``certStatus.unknown``
     - OPTIONAL. *[2] IMPLICIT NULL*. Indica che il responder non conosce lo stato del certificato.
     - [:rfc:`6960`, clause 4.2.1]

   * - ``thisUpdate``
     - REQUIRED. *GeneralizedTime*. Indica la data e l'ora di emissione di questa risposta OCSP.
     - [:rfc:`6960`, clause 4.2.1]

   * - ``nextUpdate``
     - OPTIONAL. *[0] EXPLICIT GeneralizedTime*. Indica la data e l'ora entro cui il prossimo aggiornamento del database dell'OCSP Responder sarà disponibile.
     - [:rfc:`6960`, clause 4.2.1]

   * - ``singleExtensions``
     - OPTIONAL. *[1] EXPLICIT SEQUENCE*. Include estensioni applicabili a questa singola risposta di stato del certificato.
     - [:rfc:`6960`, clause 4.2.1]

Di seguito un esempio non normativo di risposta OCSP con un singolo stato ``good``.


.. literalinclude:: ../../examples/ocsp-response.txt
  :language: text

Token Status List (TSL)
""""""""""""""""""""""""

Questa sezione definisce una struttura dati Status List, usata per trasmettere informazioni relative agli stati individuali di più WRPRC.
Una Status List descrive lo stato dei WRPRC codificando la loro validità in un bit array.
Ciascun WRPRC viene allocato un indice durante l'emissione; questo indice rappresenta la sua posizione all'interno del bit array.
Il valore del bit (o dei bit) a questo indice corrisponde allo stato del WRPRC.

Una Status List è fornita all'interno di un Status List Token firmato crittograficamente in formato JWT.
Il formato, le strutture di richiesta e risposta sono descritti in :ref:`credential-revocation:Token Status Lists`.

In questa specifica, i ruoli del Provider di WRPRC e dello Status Issuer (ossia l'entità che emette lo Status List Token sulle informazioni di stato del WRPRC) DEVONO coincidere.
Inoltre, lo Status Provider (ossia l'entità che fornisce lo Status List Token su un endpoint pubblico) DEVE essere il Provider di WRPRC stesso.

Il Provider di WRPRC DEVE usare i seguenti valori per i possibili stati dei WRPRC emessi:

- ``0x00`` - ``VALID`` - Il WRPRC è valido.
- ``0x01`` - ``INVALID`` - Il WRPRC è revocato.


Una volta che la Wallet Unit riceve un WRPRC, può richiedere la Status List per validarne lo stato tramite l'URI parameter fornito e cercare l'indice corrispondente nell'elenco.

Status List Token (SLT)
........................

Lo **Status List Token** è disponibile allo Status List Endpoint.
È formattato come JSON Web Token (JWT) firmato dal Provider di WRPRC e contiene i parametri descritti in :ref:`credential-revocation:Token di Status List`.
L'unica differenza è il claim ``status_list``, che è un oggetto JSON contenente i seguenti parametri:

.. _table_wrprc_status_list_structure:
.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Parameter**
    - **Description**
    - **Reference**
  * - **bits**
    - REQUIRED.
      JSON Integer che specifica il numero di bit per WRPRC nell'array di byte compresso (``lst``).
      I valori consentiti per bits sono 1, 2, 4 e 8.
    - `TOKEN-STATUS-LIST`_
  * - **lst**
    - REQUIRED.
      JSON String che contiene i valori di stato per tutti i WRPRC di cui trasmette gli stati.
      Il valore DEVE essere l'array di byte compresso codificato in base64url.
    - `TOKEN-STATUS-LIST`_
  * - **aggregation_uri**
    - OPTIONAL.
      JSON String che contiene una URI per recuperare la Status List Aggregation per questo tipo di WRPRC o Issuer.
    - `TOKEN-STATUS-LIST`_



.. include:: ../common/common_definitions.rst
.. Incluso tramite infrastructure-trust.rst al livello di titolo '-' (livello 1).

Trust Management and Lifecycle
------------------------------
Questa sezione descrive il ciclo di vita dei Trust Artifact (:ref:`infrastructure-trust:Trust Artifacts Lifecycle State Machine`) e i meccanismi usati per gestirne lo status (:ref:`infrastructure-trust:Revocation Mechanisms`).
Il ciclo di vita delle Entità, gli eventi che modificano la loro registrazione e gli effetti che tali eventi producono sui Trust Artifact sono descritti in :ref:`onboarding-system:Lifecycle Management`.

Trust Artifacts Lifecycle State Machine
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Le State Machine per i Trust Artifact sono descritte di seguito:

- Per WRPAC, WRPRC e Sign/Seal Certificate, gli stati del ciclo di vita sono ``VALID`` e ``REVOKED``.
  La transizione da ``VALID`` a ``REVOKED`` è innescata dalla revoca del Trust Artifact, che può essere avviata dal corrispondente Trust Artifact provider per varie ragioni quali compromissione di chiave, cambiamenti organizzativi, o non conformità alle policy del framework.
  Una volta che un Trust Artifact è nello stato ``REVOKED``, MUST NOT essere considerato fidato per qualsiasi uso operativo all'interno dell'ecosistema, e qualsiasi Entità che vi fa affidamento MUST rifiutarlo per autenticazione, autorizzazione o qualsiasi altra operazione relativa alla fiducia.

  - Un WRPAC nello stato ``VALID`` MUST NOT essere presente nella CRL designata e/o MUST restituire uno status ``good`` nella risposta OCSP.
    Un WRPAC nello stato ``REVOKED`` MUST essere presente nella CRL designata e/o MUST restituire uno status ``revoked`` nella risposta OCSP.
  - Un WRPRC nello stato ``VALID`` MUST restituire uno status ``0x00`` nel corrispondente Status List Token.
    Un WRPRC nello stato ``REVOKED`` MUST avere valore di status ``0x01`` all'interno del corrispondente Status List Token.
- Per le Trust List (LoTE, LOTL, EUMS TL), gli stati del ciclo di vita sono ``CURRENT`` e ``HISTORICAL``.
  La transizione da ``CURRENT`` a ``HISTORICAL`` è innescata dalla pubblicazione di una nuova versione della Trust List che sostituisce la versione precedente.
  Una volta che una Trust List è nello stato ``HISTORICAL``, MUST NOT essere usata per qualsiasi uso operativo all'interno dell'ecosistema.
  Si applicano due eccezioni: la validazione dell'affidabilità della Trust List tramite il pivoting mechanism, e la validazione di operazioni storiche tramite il componente ``ServiceHistory`` della Trust List.
- Trust Mark: gli status di un Trust Mark sono ``ACTIVE``, ``EXPIRED``, ``REVOKED``.
  Lo status può essere controllato usando l'endpoint Trust Mark Status (vedi Sezione 8.4 di `OID-FED`_).

.. note::
  Register, Entity Configuration e Subordinate Statement sono semplicemente pubblicati o non pubblicati.
  Durante la loro pubblicazione possono essere aggiornati.

Il diagramma :numref:`fig_Trust_Artifacts_States` evidenzia la state machine dei Trust Artifact sopra menzionati:

.. _fig_Trust_Artifacts_States:
.. plantuml:: plantuml/trust-artifacts-states.puml
    :width: 90%
    :caption: `Trust Artifacts States. <https://www.plantuml.com/plantuml/svg/PL5TRzCm57tFhpZQquOwyRu7j2eBB29RgyGK942Rbzmr5aaSNTk52l7ViLENj28lbdFl-JZ7jyPAjgxlabOr1Ef7kqT3fcOrMgM79F4Bbd2H4blrgcf_CRZyNAwNwGB-AFrHgUqWhMDwMv7ihYuW3SB-1zPknEy4mDSttt5z_GwRPP7VuGQvCKuEDVbP_1UcPRPPVSp2lAIThcLm0C5gkoN6j-4oBOi5LccrNa0pAkj53Gfbx5K2HFI1AUZTG13tQf3Tj4h9dtzf13jZ9wGFKsYHBL2iX2SNnMJVdxFvsRqedj9FPPaz2a--TY-TYXxrArB7J8F5XjY4uW8kgaLC93vI98XV0fmo1w7xl1AhCa-NXHUgtEWvgQ46Btiyqi-ZHgX4j0JTDT03GHb8hbkryvjMuxaYtgcQxdrCpVldKD8fS-pflreU9Fym1xCFnnQIEKsiEIuynUlf8ozJaM-o-P4XXmRZULqIivZ7Him4pxwiypAxkq78Hhz6nGUKLVsKaKdMBJNdgDbA1BwdXY9mwMohMTczBuofrrC_BPqxE24uRUQMXiRrtLy0>`_


Federation Entity Key Rotation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

La Federation Entity Key di un'Entità è attestata dal Subordinate Statement che il suo superiore immediato pubblica su di essa, e l'Entity Configuration dell'Entità MUST essere firmata con una chiave che il Subordinate Statement attesta.
Una nuova Federation Entity Key diventa fidata solo quando il superiore la attesta nel Subordinate Statement.

La rotazione della Federation Entity Key MUST essere eseguita come definito nei passi seguenti:

- L'Entità aggiunge la nuova chiave al ``jwks`` della propria Entity Configuration e MUST continuare a firmare l'Entity Configuration con la chiave precedente, che è ancora attestata.
- Nel processo di Entity Update (vedi :ref:`onboarding-system:Entity Update`) il superiore MUST leggere il ``jwks`` dall'Entity Configuration, MUST verificare che l'Entity Configuration sia firmata con una chiave attestata, e MUST riemettere il Subordinate Statement attestando la nuova chiave.
- La chiave precedente e la nuova chiave coesistono quindi fino a quando le Trust Chain costruite con il Subordinate Statement precedente sono scadute, e durante la coesistenza l'Entità continua a firmare con la chiave precedente, in modo che sia il Subordinate Statement precedente sia quello nuovo validino la sua Entity Configuration.
- Una volta che le finestre di validità della Trust Chain sono scadute, l'Entità MAY firmare la propria Entity Configuration con la nuova chiave 
- Poi, quando l'Entità vuole rimuovere la chiave precedente, MAY rimuoverla dal ``jwks`` notificando questo cambiamento al superiore attraverso il processo di Entity Update (vedi :ref:`onboarding-system:Entity Update`), e il superiore MUST rimuoverla dal Subordinate Statement.
- Il superiore MUST registrare l'evento come un ``jwks_update`` pubblicato sul Federation Subordinate Events Endpoint.


Revocation Mechanisms
^^^^^^^^^^^^^^^^^^^^^

Questa sezione descrive gli artifact impiegati in :ref:`infrastructure-trust:Trust Artifacts Lifecycle State Machine` per gestire lo status di certificati ed entità, dettagliando i rispettivi formati e parametri.
La distinzione principale è la seguente:

- Per gestire i Wallet-Relying Party Access Certificate e i Sign/Seal Certificate, le entità che agiscono come Trust Anchor per questi certificati MUST:

  - rendere disponibile almeno un meccanismo di revoca tra :ref:`infrastructure-trust:Certificate Revocation List (CRL)` e :ref:`infrastructure-trust:Online Certificate Status Protocol (OCSP)`;
  - emettere WRPAC e Sign/Seal Certificate con almeno un'estensione corrispondente al meccanismo di revoca fornito.

- Per gestire i Wallet-Relying Party Registration Certificate, ciascun Provider of Wallet Relying Party Registration Certificates MUST:

  - rendere disponibile un endpoint per richiedere :ref:`infrastructure-trust:Token Status List (WRPRC Profile)`;
  - emettere WRPRC con il parametro appropriato ``status`` come descritto in :ref:`infrastructure-trust:Wallet-Relying Party Registration Certificate (WRPRC) Profile`.

.. note::
  `ETSI EN 319 411-1`_ raccomanda il supporto di OCSP, vedi clausola CSS-6.3.10-06 e Nota 2.

Certificate Revocation List (CRL)
"""""""""""""""""""""""""""""""""

Le **Certificate Revocation Lists (CRLs)** sono usate per controllare lo status di revoca di un certificato X509.
Una CRL è un elenco firmato digitalmente di certificati revocati che sono stati emessi da una CA.
La CRL è pubblicata e resa disponibile a qualsiasi entità tramite un URI accessibile pubblicamente.
La CRL MUST essere firmata digitalmente dal **CRL issuer**.

Le CRL MAY essere usate per i seguenti tipi di certificati:

- Wallet Relying Party Access Certificate includendo l'estensione ``cRLDistributionPoints`` nel certificato, come descritto in :ref:`infrastructure-trust:Wallet-Relying Party Access Certificate (WRPAC) Profile`.
- Sign/Seal Certificate includendo l'estensione ``cRLDistributionPoints`` nel certificato, come descritto in :ref:`infrastructure-trust:Entity Sign/Seal Certificate Profile`.

Se una CRL è usata per gestire lo status dei certificati, il CRL issuer MUST essere l'entità referenziata nel campo ``subject`` del certificato Trust Anchor.

Il CRL issuer MAY anche generare delta CRL.
Una delta CRL elenca solo quei certificati, all'interno del proprio scope, il cui status di revoca è cambiato dall'emissione di una CRL completa referenziata.
La CRL completa referenziata è indicata come base CRL.
Lo scope di una delta CRL MUST essere lo stesso della base CRL che referenzia.

Se supportata dalla CA, la CRL MUST essere disponibile all'URI specificato nella struttura ``cRLDistributionPoints.distributionPoint`` *[0] CHOICE* all'interno del Wallet Relying Party Access Certificate (WRPAC).

Una CRL X.509 v2 è rappresentata come la codifica ASN.1 DER della SEQUENCE ``CertificateList``.
La codifica ASN.1 DER è un sistema di encoding tag, length e value strettamente definito per ciascun elemento.
I byte finali trasmessi rappresentano la codifica DER della SEQUENCE di livello superiore contenente i campi nella tabella seguente:

.. list-table:: Struttura CertificateList di Livello Superiore
   :class: longtable
   :widths: 20 60 20
   :header-rows: 1

   * - **Parameter**
     - **Descrizione**
     - **Riferimento**

   * - ``tbsCertList``
     - REQUIRED. *SEQUENCE*. Contiene le informazioni core della CRL inclusi il nome dell'issuer, la data di emissione, la data del prossimo aggiornamento, l'elenco opzionale dei certificati revocati, e le estensioni CRL opzionali.
     - :rfc:`5280`, clausola 5.1.1.1

   * - ``signatureAlgorithm``
     - REQUIRED. *SEQUENCE*. Contiene l'identificatore di algoritmo per l'algoritmo usato dal CRL issuer per firmare la ``CertificateList``.
       La selezione SHOULD allinearsi agli standard rilevanti (ad es., [ETSI TS 119 312]).
     - :rfc:`5280`, clausola 5.1.1.2

   * - ``signatureAlgorithm.algorithm``
     - REQUIRED. *OBJECT IDENTIFIER*. L'OID dell'algoritmo di firma.
     - [:rfc:`5280`, clausola 4.1.1.2]

   * - ``signatureAlgorithm.parameters``
     - OPTIONAL. *ANY*. Parametri specifici dell'algoritmo, dipendenti dall'algoritmo di firma usato.
     - [:rfc:`5280`, clausola 4.1.1.2]

   * - ``signatureValue``
     - REQUIRED. *BIT STRING*. Contiene la firma digitale calcolata sulla ``tbsCertList`` codificata ASN.1 DER.
     - [:rfc:`5280`, clausola 5.1.1.3]

Certificate List Content
.........................

La ``tbsCertList`` (To Be Signed Certificate List) è una SEQUENCE ASN.1 contenente diversi campi ed estensioni.
La tabella seguente elenca tutti tali campi ed estensioni che sono richiesti in una CRL o condizionalmente richiesti.

.. list-table:: Campi ed Estensioni tbsCertList
   :class: longtable
   :widths: 20 60 20
   :header-rows: 1

   * - **Parameter**
     - **Descrizione**
     - **Riferimento**

   * - ``version``
     - OPTIONAL. *INTEGER*. Descrive la versione della CRL codificata.
       Quando sono usate le estensioni (come è prassi standard), questo campo MUST essere presente e MUST specificare la versione 2 (il valore intero è ``1``).
     - [:rfc:`5280`, clausola 5.1.2.1]

   * - ``signature``
     - REQUIRED. *SEQUENCE*. L'identificatore di algoritmo per l'algoritmo usato per firmare la CRL.
     - [:rfc:`5280`, clausola 5.1.2.2]

   * - ``signature.algorithm``
     - REQUIRED. *OBJECT IDENTIFIER*. L'OID dell'algoritmo di firma.
       MUST corrispondere al campo ``signatureAlgorithm`` nella sequence ``CertificateList`` padre.
     - [:rfc:`5280`, clausola 4.1.1.2]

   * - ``signature.parameters``
     - OPTIONAL. *ANY*. Parametri specifici dell'algoritmo, dipendenti dall'algoritmo usato.
     - [:rfc:`5280`, clausola 4.1.1.2]

   * - ``issuer``
     - REQUIRED. *Name*. Identifica l'entità che ha firmato ed emesso la CRL.
       MUST contenere un distinguished name (DN) X.500 non vuoto composto da sequence ``AttributeType`` (OID) e ``AttributeValue``.
     - [:rfc:`5280`, clausola 5.1.2.3]

   * - ``thisUpdate``
     - REQUIRED. *UTCTime* o *GeneralizedTime*. Indica la data di emissione di questa CRL.
       Le date fino al 2049 MUST usare ``UTCTime``.
       Le date nel 2050 o successive MUST usare ``GeneralizedTime``.
     - [:rfc:`5280`, clausola 5.1.2.4]

   * - ``nextUpdate``
     - REQUIRED. *UTCTime* o *GeneralizedTime*. Indica la data entro cui sarà emessa la successiva CRL.
       Le date fino al 2049 MUST usare ``UTCTime``.
       Le date nel 2050 o successive MUST usare ``GeneralizedTime``.
     - [:rfc:`5280`, clausola 5.1.2.5]

   * - ``revokedCertificates``
     - OPTIONAL. *SEQUENCE OF*. Una sequence di certificati revocati.
       Quando non vi sono certificati revocati, questo campo MUST essere assente.
     - [:rfc:`5280`, clausola 5.1.2.6]

   * - ``revokedCertificates.userCertificate``
     - REQUIRED. *INTEGER*. Il ``CertificateSerialNumber`` del certificato revocato.
     - [:rfc:`5280`, clausola 5.1.2.6]

   * - ``revokedCertificates.revocationDate``
     - REQUIRED. *UTCTime* o *GeneralizedTime*. La data in cui è avvenuta la revoca.
     - [:rfc:`5280`, clausola 5.1.2.6]

   * - ``revokedCertificates.crlEntryExtensions``
     - OPTIONAL. *SEQUENCE OF*. Estensioni specifiche per questa entry di certificato revocato.
       Se presente, la ``version`` della CRL MUST essere ``v2``.
     - [:rfc:`5280`, clausola 5.1.2.6]

   * - ``crlExtensions``
     - OPTIONAL. *[0] EXPLICIT SEQUENCE OF*. Una sequence di una o più estensioni CRL.
       Se presente, la ``version`` della CRL MUST essere ``v2``.
     - [:rfc:`5280`, clausola 5.1.2.7]

Il campo ``crlExtensions`` MAY contenere varie estensioni.
Le estensioni standard notevoli includono:

.. list-table:: crlExtensions Notevoli
   :class: longtable
   :widths: 20 60 20
   :header-rows: 1

   * - **Parameter**
     - **Descrizione**
     - **Riferimento**

   * - ``authorityKeyIdentifier``
     - REQUIRED. *SEQUENCE*. Fornisce un mezzo per identificare la chiave pubblica corrispondente alla chiave privata usata per firmare la CRL.
       Contiene ``keyIdentifier`` (OCTET STRING), ``authorityCertIssuer``, o ``authorityCertSerialNumber``.
     - :rfc:`5280`, clausola 5.2.1

   * - ``cRLNumber``
     - REQUIRED. *INTEGER*. Un'estensione non critica che convoglia un numero di sequence monotonicamente crescente per un dato scope e issuer di CRL.
       Sia le base CRL sia le delta CRL condividono la stessa sequence monotonicamente crescente.
       Il numero della delta CRL MUST essere maggiore del numero della base CRL che referenzia.
     - :rfc:`5280`, clausola 5.2.3

   * - ``deltaCRLIndicator``
     - REQUIRED per le delta CRL.
       MUST NOT comparire nelle base CRL.
       *INTEGER* (``BaseCRLNumber``). Un'estensione **critica** che marca la CRL come delta CRL e identifica la base CRL rispetto a cui è relativa.
       Il valore intero è il ``cRLNumber`` della base CRL su cui questa delta è costruita.
       Una relying party che non comprende questa estensione MUST rifiutare la CRL.
       La base CRL MUST restare raggiungibile (in cache o recuperabile) affinché la delta sia utile.
       Se questa estensione è assente, la CRL è una CRL completa (base).
     - :rfc:`5280`, clausola 5.2.4

   * - ``freshestCRL`` (a.k.a.
       *CRL Distribution Points* su una CRL)
     - OPTIONAL; RECOMMENDED sulle base CRL nei deployment che emettono delta CRL. *SEQUENCE OF DistributionPointName*. Un'estensione non critica che indica dove può essere recuperata la delta CRL più recentemente emessa per lo stesso scope.
       Ciascun ``DistributionPointName`` reca uno o più URI (tipicamente ``uniformResourceIdentifier``).
       Quando presente su una base CRL, MUST puntare alla location di distribuzione della delta CRL; quando presente su una delta CRL, punta alla delta CRL successiva.
       Una relying party usa questo per scoprire le delta senza configurazione out-of-band aggiuntiva.
     - :rfc:`5280`, clausola 5.2.6

   * - ``issuingDistributionPoint``
     - OPTIONAL; REQUIRED quando lo scope della CRL è ristretto (ad es., only-CA, only-end-entity, only-some-reasons) o quando la CRL è indiretta. *SEQUENCE* (``IssuingDistributionPoint``). Un'estensione **critica** che descrive lo scope della CRL.
       Contiene i flag ``distributionPoint``, ``onlyContainsUserCerts``, ``onlyContainsCACerts``, ``onlySomeReasons``, ``indirectCRL``, e ``onlyContainsAttributeCerts``.
       Per i deployment delta-CRL, il bit ``indirectCRL`` è impostato a TRUE quando la delta è firmata da un CRL issuer diverso dalla Certificate Authority che ha emesso i certificati (comune quando è usato un servizio di revoca delegato), e ``onlySomeReasons`` MAY restringere la delta CRL a specifiche ragioni di revoca (ad es., solo ``keyCompromise``).
       La base CRL e le delta CRL corrispondenti MUST condividere lo stesso scope (stessi flag ``onlyContains*`` e ``distributionPoint``).
     - :rfc:`5280`, clausola 5.2.5

Online Certificate Status Protocol (OCSP)
""""""""""""""""""""""""""""""""""""""""""""

L'Online Certificate Status Protocol (OCSP) (:rfc:`6960`) consente alle applicazioni di determinare lo stato esatto di revoca di certificati identificati.
Fornisce informazioni di revoca più tempestive di quanto tipicamente possibile con le CRL e MAY anche essere usato per ottenere informazioni di status aggiuntive.

Un client OCSP emette una richiesta di status a un responder OCSP e MUST sospendere l'accettazione dei certificati in questione fino a quando il responder fornisce una risposta valida.

Se supportato dalla Certificate Authority, l'URI a cui il Responder OCSP può essere invocato MUST essere presente nell'estensione ``authorityInfoAccess.accessLocation`` del Wallet Relying Party Access Certificate (WRPAC).

Questo protocollo specifica i dati che MUST essere scambiati tra il client OCSP (che controlla lo status di uno o più certificati) e il server OCSP (che fornisce lo status corrispondente).

La tabella seguente sintetizza i ruoli del client e del server OCSP nell'ecosistema EUDIW.

.. list-table:: Ruoli OCSP nell'ecosistema EUDIW
   :class: longtable
   :widths: 28 28 44
   :header-rows: 1

   * - **OCSP Client**
     - **OCSP Server**
     - **Use case**
   * - Wallet Unit
     - WRPAC Provider
     - Controllo Status WRPAC
   * - Wallet Unit o Relying Party
     - PID Provider Trust Anchor
     - Controllo Status del PID Sign/Seal Certificate
   * - Wallet Unit o Relying Party
     - PuB-EAA Provider Trust Anchor
     - Controllo Status del PuB-EAA Sign/Seal Certificate
   * - Wallet Unit o Relying Party
     - (Q)EAA Provider Trust Anchor
     - Controllo Status del (Q)EAA Sign/Seal Certificate

.. note::
    Il controllo di Status sui Sign/Seal Certificate è necessario solo nel caso in cui il Sign/Seal Certificate non sia referenziato direttamente come Trust Anchor Certificate, nel qual caso è fidato a priori e non necessita di un controllo di status separato.

Online Certificate Status Protocol Request Format
....................................................

La richiesta OCSP MUST essere la codifica ASN.1 DER della SEQUENCE ``OCSPRequest``, che contiene la ``tbsRequest`` (To-Be-Signed Request) e una firma opzionale.
La tabella seguente elenca i parametri trovati all'interno della struttura ``tbsRequest``.

.. list-table:: Parametri della Struttura tbsRequest
   :class: longtable
   :widths: 20 60 20
   :header-rows: 1

   * - **Parameter**
     - **Descrizione**
     - **Riferimento**

   * - ``version``
     - OPTIONAL. *[0] EXPLICIT INTEGER*. Indica la versione del protocollo.
       Se omesso, il valore predefinito è ``v1`` (0).
     - [:rfc:`6960`, clausola 4.1.1]

   * - ``requestList``
     - REQUIRED. *SEQUENCE OF*. Contiene una o più richieste di status di singolo certificato.
     - [:rfc:`6960`, clausola 4.1.1]

   * - ``requestList.reqCert``
     - REQUIRED. *SEQUENCE*. La struttura ``CertID`` recante l'identificatore di un certificato target.
     - [:rfc:`6960`, clausola 4.1.1]

   * - ``requestList.singleRequestExtensions``
     - OPTIONAL. *[0] EXPLICIT SEQUENCE*. Include estensioni applicabili a questa richiesta di status di singolo certificato.
     - [:rfc:`6960`, clausola 4.1.1]

   * - ``requestExtensions``
     - OPTIONAL. *[2] EXPLICIT SEQUENCE*. Include estensioni applicabili alle richieste complessive trovate all'interno della ``requestList``.
     - [:rfc:`6960`, clausola 4.1.1]

Il parametro ``reqCert`` utilizza la struttura ``CertID``, MUST essere una *SEQUENCE* ASN.1 contenente i seguenti parametri:

.. list-table:: Parametri della Struttura CertID
   :class: longtable
   :widths: 20 60 20
   :header-rows: 1

   * - **Parameter**
     - **Descrizione**
     - **Riferimento**

   * - ``hashAlgorithm``
     - REQUIRED. *SEQUENCE*. Identifica l'algoritmo di hash usato per generare gli hash del nome e della chiave dell'issuer.
     - [:rfc:`6960`, clausola 4.1.1]

   * - ``hashAlgorithm.algorithm``
     - REQUIRED. *OBJECT IDENTIFIER*. L'OID della funzione di hash (ad es., SHA-256, a seconda del profilo).
     - [:rfc:`6960`, clausola 4.1.1]

   * - ``hashAlgorithm.parameters``
     - OPTIONAL. *ANY*. Parametri specifici dell'algoritmo, dipendenti dall'algoritmo di hash usato.
     - [:rfc:`6960`, clausola 4.1.1]

   * - ``issuerNameHash``
     - REQUIRED. *OCTET STRING*. L'hash del distinguished name (DN) dell'issuer, calcolato sulla codifica DER del campo name dell'issuer.
     - [:rfc:`6960`, clausola 4.1.1]

   * - ``issuerKeyHash``
     - REQUIRED. *OCTET STRING*. L'hash della chiave pubblica dell'issuer, calcolato sul valore (esclusi tag e length) del campo subject public key.
     - [:rfc:`6960`, clausola 4.1.1]

   * - ``serialNumber``
     - REQUIRED. *INTEGER*. Il serial number del certificato target per cui è richiesto lo status.
     - [:rfc:`6960`, clausola 4.1.1]

Le strutture ``requestExtensions`` e ``singleRequestExtensions`` MAY contenere varie estensioni.
La tabella seguente elenca quelle richieste:

.. list-table:: Estensione Nonce OCSP
   :class: longtable
   :widths: 20 60 20
   :header-rows: 1

   * - **Parameter**
     - **Descrizione**
     - **Riferimento**

   * - ``nonce``
     - REQUIRED. *OCTET STRING*. Valore crittograficamente fresco usato per vincolare una richiesta e una risposta al fine di prevenire attacchi di replay.
       L'identificatore OID è ``id-pkix-ocsp-nonce``.
     - [:rfc:`6960`, clausola 4.4.1]

Quando inviata su HTTP usando POST, il body di questa richiesta MUST contenere la codifica DER raw di questa SEQUENCE ``OCSPRequest`` e MUST avere MIME type ``application/ocsp-request``.

Di seguito un esempio non normativo di una richiesta OCSP:

.. literalinclude:: ../../examples/ocsp-request.txt
  :language: text

Online Certificate Status Protocol Response Format
...................................................

Una risposta OCSP MUST essere la codifica ASN.1 DER della *SEQUENCE* ``OCSPResponse``.
Quando trasportata su HTTP, il body della risposta HTTP MUST contenere la codifica DER raw di questa ``OCSPResponse``, con il MIME type ``application/ocsp-response``.
La *SEQUENCE* ``OCSPResponse`` contiene i seguenti parametri:

.. list-table:: Parametri della Struttura OCSPResponse
   :class: longtable
   :widths: 20 60 20
   :header-rows: 1

   * - **Parameter**
     - **Descrizione**
     - **Riferimento**

   * - ``responseStatus``
     - REQUIRED. *ENUMERATED*. Indica lo status di elaborazione della richiesta precedente.
       I valori supportati sono: ``successful`` (0), ``malformedRequest`` (1), ``internalError`` (2), ``tryLater`` (3), ``sigRequired`` (5), e ``unauthorized`` (6).
     - [:rfc:`6960`, clausola 4.2.1]

   * - ``responseBytes``
     - OPTIONAL. *[0] EXPLICIT SEQUENCE*. Presente solo quando il ``responseStatus`` è ``successful`` (0).
       Contiene il tipo di risposta e i dati di risposta codificati.
     - [:rfc:`6960`, clausola 4.2.1]

   * - ``responseBytes.responseType``
     - REQUIRED. *OBJECT IDENTIFIER*. Identificatore per il tipo di risposta.
       Per un responder OCSP basic, questo valore MUST essere ``id-pkix-ocsp-basic``.
     - [:rfc:`6960`, clausola 4.2.1]

   * - ``responseBytes.response``
     - REQUIRED. *OCTET STRING*. Contiene la codifica DER della sintassi di risposta identificata da ``responseType`` (ad es., la struttura ``BasicOCSPResponse``).
     - [:rfc:`6960`, clausola 4.2.1]

.. note::
   I responder OCSP MUST essere in grado di produrre risposte del tipo di risposta ``id-pkix-ocsp-basic``.
   Corrispondentemente, i client OCSP MUST essere in grado di ricevere ed elaborare risposte del tipo di risposta ``id-pkix-ocsp-basic``.

``BasicOCSPResponse`` è una SEQUENCE ASN.1 contenente i seguenti parametri:

.. list-table:: Parametri della Struttura BasicOCSPResponse
   :class: longtable
   :widths: 20 60 20
   :header-rows: 1

   * - **Parameter**
     - **Descrizione**
     - **Riferimento**

   * - ``tbsResponseData``
     - REQUIRED. *SEQUENCE*. Contiene i dati core della risposta da firmare da parte del responder.
     - [:rfc:`6960`, clausola 4.2.1]

   * - ``tbsResponseData.version``
     - OPTIONAL. *[0] EXPLICIT INTEGER*. La versione della sintassi di risposta.
       Se omesso, il valore predefinito è ``v1`` (0).
     - [:rfc:`6960`, clausola 4.2.1]

   * - ``tbsResponseData.responderID``
     - REQUIRED. *CHOICE*. Identifica il responder OCSP.
       MUST contenere o ``byName`` o ``byKey``.
     - [:rfc:`6960`, clausola 4.2.1]

   * - ``tbsResponseData.responderID.byName``
     - OPTIONAL. *[1] EXPLICIT Name*. Il ``Name`` dal subject del certificato del responder.
     - [:rfc:`6960`, clausola 4.2.1]

   * - ``tbsResponseData.responderID.byKey``
     - OPTIONAL. *[2] EXPLICIT OCTET STRING*. L'hash SHA-1 del ``subjectPublicKey`` del responder (esclusi i campi tag e length).
     - [:rfc:`6960`, clausola 4.2.1]

   * - ``tbsResponseData.producedAt``
     - REQUIRED. *GeneralizedTime*. L'ora in cui la risposta OCSP è stata generata.
     - [:rfc:`6960`, clausola 4.2.1]

   * - ``tbsResponseData.responses``
     - REQUIRED. *SEQUENCE OF*. Una sequence di strutture ``SingleResponse``, che forniscono lo status di ciascun certificato richiesto.
     - [:rfc:`6960`, clausola 4.2.1]

   * - ``tbsResponseData.responseExtensions``
     - OPTIONAL. *[1] EXPLICIT SEQUENCE OF*. Contiene estensioni applicabili alla risposta OCSP complessiva.
     - [:rfc:`6960`, clausola 4.2.1]

   * - ``signatureAlgorithm``
     - REQUIRED. *SEQUENCE*. Identifica l'algoritmo crittografico usato per firmare la risposta.
     - [:rfc:`5280`, clausola 4.1.1.2]

   * - ``signatureAlgorithm.algorithm``
     - REQUIRED. *OBJECT IDENTIFIER*. L'OID dell'algoritmo di firma.
       La selezione SHOULD allinearsi agli standard rilevanti (ad es., [ETSI TS 119 312]).
     - [:rfc:`5280`, clausola 4.1.1.2]

   * - ``signatureAlgorithm.parameters``
     - OPTIONAL. *ANY*. Parametri specifici dell'algoritmo, dipendenti dall'OID definito in ``algorithm``.
     - [:rfc:`5280`, clausola 4.1.1.2]

   * - ``signature``
     - REQUIRED. *BIT STRING*. La firma digitale calcolata sull'hash della ``tbsResponseData`` codificata DER.
     - [:rfc:`6960`, clausola 4.2.1]

   * - ``certs``
     - OPTIONAL. *[0] EXPLICIT SEQUENCE OF*. Catena di certificati per aiutare il client a verificare la firma del responder.
       Se non sono inclusi certificati, questo campo SHOULD essere assente.
     - [:rfc:`6960`, clausola 4.2.1]

La struttura ``responseExtensions`` MAY contenere varie estensioni.
La tabella seguente elenca quelle richieste:

.. list-table:: Estensioni di Risposta Nonce
   :class: longtable
   :widths: 20 60 20
   :header-rows: 1

   * - **Parameter**
     - **Descrizione**
     - **Riferimento**

   * - ``nonce``
     - REQUIRED. *OCTET STRING*. Valore crittograficamente fresco usato per vincolare una richiesta e una risposta al fine di prevenire attacchi di replay.
       Se incluso nella richiesta, i responder SHOULD includerlo nella risposta.
       L'identificatore OID è ``id-pkix-ocsp-nonce``.
     - [:rfc:`6960`, clausola 4.4.1]

Nella Risposta OCSP MUST esserci almeno una ``SingleResponse`` per ciascun ``CertID`` nella richiesta.
Ciascuna ``SingleResponse`` è una *SEQUENCE* ASN.1 che reca i seguenti parametri:

.. list-table:: Parametri della Struttura SingleResponse
   :class: longtable
   :widths: 20 60 20
   :header-rows: 1

   * - **Parameter**
     - **Descrizione**
     - **Riferimento**

   * - ``certID``
     - REQUIRED. *SEQUENCE*. Identificatore del certificato il cui status è determinato in ``certStatus``.
     - [:rfc:`6960`, clausola 4.2.1]

   * - ``certStatus``
     - REQUIRED. *CHOICE*. Il valore dello status del certificato.
       MUST essere esattamente uno tra: ``good``, ``revoked``, o ``unknown``.
     - [:rfc:`6960`, clausola 4.2.1]

   * - ``certStatus.good``
     - OPTIONAL. *[0] IMPLICIT NULL*. Indica che il certificato è valido.
     - [:rfc:`6960`, clausola 4.2.1]

   * - ``certStatus.revoked``
     - OPTIONAL. *[1] IMPLICIT SEQUENCE*. Indica che il certificato è stato revocato.
       Contiene la struttura ``RevokedInfo``.
     - [:rfc:`6960`, clausola 4.2.1]

   * - ``certStatus.revoked.revocationTime``
     - REQUIRED. *GeneralizedTime*. L'ora in cui il certificato è stato revocato.
     - [:rfc:`6960`, clausola 4.2.1]

   * - ``certStatus.revoked.revocationReason``
     - OPTIONAL. *[0] EXPLICIT ENUMERATED*. Contiene il ``CRLReason`` che indica perché il certificato è stato revocato.
     - [:rfc:`6960`, clausola 4.2.1]

   * - ``certStatus.unknown``
     - OPTIONAL. *[2] IMPLICIT NULL*. Indica che il responder non conosce lo status del certificato.
     - [:rfc:`6960`, clausola 4.2.1]

   * - ``thisUpdate``
     - REQUIRED. *GeneralizedTime*. Indica la data e l'ora di emissione di questa Risposta OCSP.
     - [:rfc:`6960`, clausola 4.2.1]

   * - ``nextUpdate``
     - OPTIONAL. *[0] EXPLICIT GeneralizedTime*. Indica la data e l'ora entro cui il successivo aggiornamento al database del Responder OCSP sarà in vigore.
     - [:rfc:`6960`, clausola 4.2.1]

   * - ``singleExtensions``
     - OPTIONAL. *[1] EXPLICIT SEQUENCE*. Include estensioni applicabili a questa risposta di status di singolo certificato.
     - [:rfc:`6960`, clausola 4.2.1]

Di seguito un esempio non normativo di una risposta OCSP con un singolo status ``good``.

.. literalinclude:: ../../examples/ocsp-response.txt
  :language: text

Token Status List (WRPRC Profile)
""""""""""""""""""""""""""""""""""

Questa sezione profila il meccanismo Token Status List (TSL) di `TOKEN-STATUS-LIST`_ per i Wallet-Relying Party Registration Certificate (WRPRC). Una TSL convoglia lo status corrente di molti WRPRC in un Status List Token (SLT) compatto e firmato.

Lo SLT Provider MAY essere il Provider of WRPRC o un'entità designata.

**Status List**

Una Status List contiene un array di byte compresso le cui entry rappresentano gli status di molti WRPRC. Il Provider of WRPRC MUST assegnare un valore ``idx`` distinto, non negativo a ciascun WRPRC emesso e includerlo, insieme all'``uri`` della SLT, nel membro ``status.status_list`` del WRPRC. Per un WRPRC codificato JWT, ``idx`` è un intero JSON e ``uri`` è una stringa JSON.
Per un WRPRC codificato CWT, ``idx`` è un intero non firmato CBOR e ``uri`` è una text string CBOR. In entrambi i casi, ``uri`` MUST essere un URI conforme a :rfc:`3986`.

Secondo l'ARF e [`ETSI TS 119 475`_], lo status del WRPRC è ``VALID`` o ``INVALID``.
Il Provider of WRPRC MUST impostare il parametro ``bits`` nell'oggetto ``status_list`` della SLT a ``1``. Il valore ``0x00`` rappresenta ``VALID``, e ``0x01`` rappresenta ``INVALID``.

Lo SLT Provider MUST impacchettare le entry a partire dal bit meno significativo di ciascun byte, comprimere l'array di byte usando DEFLATE con il formato dati ZLIB, e pubblicare la Status List risultante nella SLT.

**Status List Token**

Lo SLT Provider MUST agire sia come Status Issuer sia come Status Provider. MUST rendere ciascuna SLT disponibile via HTTP GET all'URI specificato dal membro ``status.status_list.uri`` del WRPRC, usando ``application/statuslist+jwt`` per una SLT JWT o ``application/statuslist+cwt`` per una SLT CWT. Il formato della SLT MAY essere un JWT o un CWT e MUST essere protetto da una firma crittografica.

Una SLT JWT MUST essere formattata come descritto nella Sezione 5.1, e una SLT CWT come descritto nella Sezione 5.2, di `TOKEN-STATUS-LIST`_.

Indipendentemente dal formato, lo SLT Provider per i WRPRC MUST firmare ciascuna SLT usando un certificato X.509 valido la cui catena di fiducia termina al Trust Anchor pubblicato nella LoTE dei Provider of WRPRC.

Per una SLT JWT, la catena del certificato di firma MUST essere recata nell'header JOSE ``x5c``.
Per una SLT CWT, essa MUST essere recata nell'header COSE ``x5chain`` (label ``33``).

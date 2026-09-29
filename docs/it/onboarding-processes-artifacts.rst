.. include:: ../common/common_definitions.rst
.. Included via onboarding-system.rst at title level '^' (level 2, under Onboarding Processes).

Certificate and Trust Artifact Issuance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Questa sezione descrive i processi che emettono i Trust Artifact.
Ciascun processo copre sia la prima emissione sia la riemissione, ad esempio dopo una rotazione di chiavi o una richiesta di chiavi aggiuntive, ed è descritto con il proprio Input, il proprio Outcome e il proprio Process.

Issuance of the X.509 Certificates through ACME and OpenID Federation
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Il WRPAC, il Signature/Seal Certificate e il National Authentication Certificate sono emessi tramite ACME :rfc:`8555` con il profilo OpenID Federation di [`ACME-OIDFED`_].

L'Entità si autentica presso la Certification Authority con la propria Federation Trust Chain, tramite la challenge ``openid-federation-01``.
L'autenticazione riusa la valutazione di trust del National Trust Framework, quindi la validazione della Trust Chain e l'autenticazione dell'Entità seguono :ref:`trust-evaluation:Trust Chain Validation` e :ref:`trust-evaluation:Federation Entity Authentication`.

Una volta autenticata l'Entità, la Certification Authority applica la propria policy e legge gli entitlement e i valori di profilo innanzitutto dal record dell'Entità nel Register, tramite le :ref:`infrastructure-trust:Register Open APIs`, e, quando l'Entità non ha un record ivi, dal Trust Mark di registrazione incluso nei Resolved Metadata della Trust Chain.
Entrambe le fonti forniscono i dati di autorizzazione con la stessa logica di [`ETSI TS 119 475`_].

L'emissione di questi certificati è un processo a sé stante, distinto dalla registrazione e eseguito machine-to-machine, quindi l'Entità presenta le proprie ``certificate_signing_requests`` nell'ordine ACME solo dopo che il processo di registrazione è stato completato con successo.

Un servizio ACME distinto è fornito per ciascuna finalità, quindi il tipo del certificato è determinato dal servizio, e il profilo di ciascun certificato è fissato dal suo tipo.

All'interno di IT-Wallet il ciclo di vita di questi certificati è mantenuto distinto dal ciclo di vita della Trust Chain.
Un certificato ha i propri ``notBefore`` e ``notAfter`` ed è governato dalla revoca X.509, quindi la perdita dell'appartenenza alla federazione di un'Entità è riflessa dalla revoca dei suoi certificati, si veda :ref:`onboarding-system:Entity Suspension and Removal`, e non dalla scadenza della Trust Chain.

Il Wallet-Relying Party Registration Certificate e il Trust Mark di registrazione non certificano chiavi, quindi non sono emessi tramite ACME. Il Trust Mark di registrazione è emesso durante la registrazione dell'Entità. Il Wallet-Relying Party Registration Certificate è emesso automaticamente come definito in :ref:`onboarding-system:Wallet-Relying Party Registration Certificate Issuance`.

.. plantuml:: plantuml/acme-oidfed-x509-issuance.puml
   :width: 99%
   :caption: `Issuance of an X.509 certificate through ACME and the OpenID Federation profile. <https://www.plantuml.com/plantuml/svg/VLDDRzH03BtdLrZbiaWiAa95eeUg8GgSAggb1muhLMx6IKOxwmaUfqlxw_5aFqXLH0vHD7xFx_cDSvqKHSTjADB6yu22MtZ0PjD97DbLCKG15UHa9MATeLAFBkuyTz1YI3IhE6fn37f7lxKClkEj4Q6n5yaCLOh4tLxWpQVfcHLlpPHl_82iNw8uaWFmu_JCkpGQvVyGXueFcEXVg08p7sfMhq-02UfY-2iDPsLrKqCYUVGDGMn1UrfpHOPeVOFg8qCvQX_5w6UPNvN5KGzMrFbaG-VpLVsjA6fONXa2Be5fzpsxWOLt5enriszz6ana8FPksP9L9u6tXJ6MHgoDzwgwFFy0JOyX47Uq5yYuPB5dix0X6slly7aYh7ddjGTam6PBzqA_Haev0qFE39vwWb0Q8jiuYzmKTHGojeCx6PD2rQC_M3mm7p5uYu0c-HbepOkl9zl7n7DuUVvcDkfL3iiQ2Q63NDH0UONI93j8R7sWWgD9YEzwpVSoAP_oRhqaVRTccGuEYdihDoYRV1-sio7l-Ojmfnl9ilCaMiysqRFDN_rOlRYCd-ylpZ_ROX-tWOfhOfV_fJy0>`_
   

Certificate Signing Request Profile
"""""""""""""""""""""""""""""""""""

Questa sezione definisce il profilo che le ``certificate_signing_requests`` DEVONO seguire, si veda :ref:`onboarding-system:Registration Data Model`.
L'Entità fornisce una Certificate Signing Request per ciascun certificato X.509 di cui ha bisogno, ossia, a seconda del ruolo, il WRPAC, il Sign/Seal Certificate o il National Authentication Certificate, e presenta ciascuna di esse nell'ordine ACME del servizio corrispondente.
Il Wallet-Relying Party Registration Certificate e il Trust Mark di registrazione non certificano una chiave, quindi non sono richiesti tramite una Certificate Signing Request, si veda :ref:`onboarding-system:Wallet-Relying Party Registration Certificate Issuance` e :ref:`onboarding-system:Registration Trust Mark Issuance`.

Una Certificate Signing Request reca la chiave pubblica da certificare, prova il possesso della corrispondente chiave privata e richiede i valori dei campi del certificato forniti dall'Entità.
Non determina il contenuto del certificato emesso: la Certification Authority DEVE validare i valori richiesti rispetto ai dati di registrazione e al profilo di certificato applicabile, e DEVE aggiungere o determinare i valori dipendenti dall'emittente richiesti da tale profilo.

La Certificate Signing Request DEVE essere una ``CertificationRequest`` come definita in :rfc:`2986` (PKCS #10), codificata in DER, ed è recata nell'ordine ACME come richiesto da :rfc:`8555#section-7.4`.

.. list-table:: Certificate Signing Request Fields
   :class: longtable
   :header-rows: 1
   :widths: 20 60 20

   * - **Field**
     - **Description**
     - **Reference**

   * - ``certificationRequestInfo``
     - OBBLIGATORIO. Contiene la versione, il subject, la chiave pubblica e gli attributi della richiesta.
     - :rfc:`2986#section-4.1`

   * - ``version``
     - OBBLIGATORIO. DEVE essere ``0``, che denota una richiesta PKCS #10 versione 1.
     - :rfc:`2986#section-4.1`

   * - ``subject``
     - OBBLIGATORIO. I suoi attributi DEVONO essere coerenti con i dati di registrazione dell'Entità e con [`ETSI EN 319 412-2`_] per le persone fisiche o [`ETSI EN 319 412-3`_] per le persone giuridiche.
       Il subject non è autorevole, quindi la Certification Authority PUÒ sostituirlo con il valore derivato dal record dell'Entità nel Register o, in sua assenza, dal Trust Mark di registrazione.
     - :rfc:`2986#section-4.1`, [`ETSI EN 319 412-2`_], [`ETSI EN 319 412-3`_]

   * - ``subjectPKInfo``
     - OBBLIGATORIO. Reca la chiave pubblica da certificare.
       La chiave DEVE utilizzare uno degli algoritmi a chiave pubblica definiti in :ref:`algorithms:Algoritmi Crittografici`.
       DEVE essere distinta dalla Federation Entity Key, e una chiave distinta DEVE essere utilizzata per ciascun certificato richiesto.
     - :rfc:`2986#section-4.1`

   * - ``attributes``
     - OBBLIGATORIO. DEVE contenere esattamente un attributo ``extensionRequest``. Altri attributi POSSONO essere inclusi solo quando supportati dal profilo di certificato applicabile.
     - :rfc:`2986#section-4.1`, :rfc:`2985#section-5.4.2`

   * - ``extensionRequest``
     - OBBLIGATORIO all'interno di ``attributes``. DEVE avere l'object identifier ``1.2.840.113549.1.9.14`` e un singolo valore di tipo ``Extensions``. Le estensioni richieste DEVONO essere coerenti con il profilo di certificato applicabile e con i dati di registrazione autorevoli.
     - :rfc:`2985#section-5.4.2`

   * - ``signatureAlgorithm``
     - OBBLIGATORIO. DEVE essere compatibile con la chiave privata corrispondente a ``subjectPKInfo`` e DEVE essere uno degli algoritmi di firma definiti in :ref:`algorithms:Algoritmi Crittografici`.
     - :rfc:`2986#section-4.2`

   * - ``signature``
     - OBBLIGATORIO. La richiesta DEVE essere firmata con la chiave privata corrispondente a ``subjectPKInfo``, il che prova il possesso di tale chiave.
     - :rfc:`2986#section-4.2`

La tabella seguente definisce i valori di estensione richiesti dall'Entità e i valori di estensione determinati dalla Certification Authority.
La criticità di ciascuna estensione richiesta DEVE seguire il profilo di certificato applicabile.

.. list-table:: Certificate Signing Request Extension Fields
   :class: longtable
   :header-rows: 1
   :widths: 25 55 20

   * - **Extension**
     - **Description**
     - **Reference**

   * - ``extensions``
     - OBBLIGATORIO come valore di ``extensionRequest``. DEVE contenere i campi di estensione richiesti come sequenza ``Extensions`` codificata in DER.
       DEVE includere ``keyUsage`` e ``subjectAltName`` e, quando richiesto dal profilo di certificato applicabile, ``certificatePolicies``.
       Le estensioni i cui valori dipendono dalla Certification Authority emittente DOVREBBERO essere omesse dalla richiesta.
     - :rfc:`2985#section-5.4.2`, :rfc:`5280#section-4.2`

   * - ``keyUsage``
     - OBBLIGATORIO. DEVE essere marcato critical e DEVE contenere esattamente una delle impostazioni di key-usage consentite dal profilo di certificato applicabile.
        Per un WRPAC, un National Authentication Certificate o un Registrar Sign/Seal Certificate, DEVE contenere uno (e uno solo) tra *Type A*, *Type B* o *Type F*.
        Per un Entity Sign/Seal Certificate, DEVE contenere uno (e uno solo) tra *Type A*, *Type B*, *Type C* o *Type F*.
        Per un WRPAC, *Type A* DOVREBBE essere utilizzato come da LEG-4.3.1-4 nella Clausola 4.3.1 [`ETSI EN 319 412-3`_].
     - :rfc:`5280#section-4.2.1.3`, :ref:`infrastructure-trust:Wallet-Relying Party Access Certificate (WRPAC) Profile`, :ref:`infrastructure-trust:Registrar Sign/Seal Certificate Profile`, :ref:`infrastructure-trust:Entity Sign/Seal Certificate Profile`

   * - ``subjectAltName``
     - OBBLIGATORIO. DEVE essere marcato non-critical e DEVE contenere almeno un ``GeneralName`` consentito dal profilo di certificato applicabile.
       Per un WRPAC o un National Authentication Certificate, DEVE contenere almeno uno dei seguenti valori di contatto: un ``uniformResourceIdentifier`` per un sito web di helpdesk/supporto, un ``otherName`` con ``type-id`` impostato a ``2.5.4.20`` (``id-at-telephoneNumber``), o un ``rfc822Name`` per un indirizzo e-mail di registrazione/utilizzo.
       Per un WRPAC, DEVE inoltre contenere l'URI dell'identificativo del Service definito in :ref:`infrastructure-trust:Wallet-Relying Party Access Certificate (WRPAC) Profile`.
     - :rfc:`5280#section-4.2.1.6`, :ref:`infrastructure-trust:Wallet-Relying Party Access Certificate (WRPAC) Profile`

Le estensioni non applicabili, o non elencate, nel profilo di certificato applicabile NON DEVONO essere incluse nel certificato emesso, indipendentemente da qualsiasi valore richiesto nella Certificate Signing Request.

.. note::
   La Certificate Signing Request certifica una chiave distinta dalla Federation Entity Key.
   La Federation Entity Key è vincolata all'Entità tramite l'Entity Configuration e il Subordinate Statement, validati tramite la Federation Trust Chain e non tramite un certification path, si veda :ref:`infrastructure-trust:PKI Architecture`.

Di seguito un esempio non normativo di una Certificate Signing Request per un WRPAC, con dati di test.

.. literalinclude:: ../../examples/csr-wrpac.txt
  :language: text

Wallet-Relying Party Access Certificate Issuance
""""""""""""""""""""""""""""""""""""""""""""""""

Il processo Wallet-Relying Party Access Certificate Issuance emette il WRPAC, definito nel :ref:`infrastructure-trust:Wallet-Relying Party Access Certificate (WRPAC) Profile`, tramite il meccanismo di :ref:`onboarding-system:Issuance of the X.509 Certificates through ACME and OpenID Federation`.
Il WRPAC appartiene al Trust Framework EUDIW, quindi i suoi attributi DEVONO sempre essere derivati dal Register, come richiesto dalla clausola 5.1.2 di [`ETSI TS 119 475`_], e il fallback al Trust Mark non si applica a esso.
L'Entità ottiene almeno un WRPAC per ciascun Service registrato ([`EIDAS-ARF`_] Reg_10a).
Un Intermediario ottiene un insieme distinto di WRPAC per ciascuna Relying Party intermediata, un WRPAC per ciascun Relying Party Service intermediato che serve ([`EIDAS-ARF`_] Reg_34a).

**Input**

Le ``certificate_signing_requests`` dell'Entità per il WRPAC di un dato Service, e la Federation Trust Chain utilizzata nella challenge ``openid-federation-01``.
Gli attributi del certificato provengono dal corrispondente elemento ``services[]`` del record dell'Entità nel Register.
Per un Intermediario provengono inoltre dal Relying Party Service intermediato a cui questo certificato è associato ([`EIDAS-ARF`_] Reg_34a).

**Outcome**

Il WRPAC di tale Service, emesso dalla WRPAC Certification Authority, che l'Entità utilizza per autenticarsi verso le Wallet Unit per tale Service.
Per un Intermediario, il WRPAC dell'associazione a un dato Relying Party Service intermediato.

**Process**

1. L'Entità richiede il WRPAC al servizio ACME della WRPAC Certification Authority, presentando le ``certificate_signing_requests`` del Service e autenticandosi con la propria Federation Trust Chain, validata come in :ref:`trust-evaluation:Federation Entity Authentication`.
2. La Certification Authority verifica che l'Entità abbia un record nel Register, che il Service richiesto esista in ``services[]``, e deriva gli attributi del certificato da tale Service (``serviceTradeName`` in ``subject.commonName``, ``serviceIdentifier`` in ``subjectAltName``).
   Per un Intermediario codifica inoltre in ``subjectAltName`` l'identificativo univoco e l'identificativo del Service della Relying Party intermediata ([`EIDAS-ARF`_] Reg_34a).
3. La Certification Authority registra il certificato in un log di Certificate Transparency secondo :rfc:`9162` ([`EIDAS-ARF`_] CT_01) e incorpora almeno un Signed Certificate Timestamp nell'estensione ``signedCertificateTimestampList`` ([`EIDAS-ARF`_] CT_04).
4. La Certification Authority emette il WRPAC e l'Entità lo recupera.

Wallet-Relying Party Registration Certificate Issuance
""""""""""""""""""""""""""""""""""""""""""""""""""""""

Il Wallet-Relying Party Registration Certificate Issuance emette il WRPRC, descritto nel :ref:`infrastructure-trust:Wallet-Relying Party Registration Certificate (WRPRC) Profile`.
Il Provider of WRPRC DEVE emettere il WRPRC automaticamente e senza indebito ritardo, senza una richiesta dell'Entità, una volta che l'Entità ha un record con uno stato di registrazione valido nel Register e un WRPAC valido del Service, come richiesto da [`EIDAS-ARF`_] RPRC_09 e RPRC_13 e dall'Annex V, punto 3(c) di [`CIR2025/848`_] come modificato da [`CIR2026/1730`_].
Il Provider of WRPRC monitora il Register, secondo [`CIR2025/848`_], revoca il WRPRC quando la registrazione dell'Entità o di tale Service cambia, e DEVE riemettere automaticamente un nuovo WRPRC ove la registrazione resti valida.

Per una Relying Party il Provider DEVE emettere un WRPRC distinto per ciascuna combinazione di intended use e Relying Party Service ([`EIDAS-ARF`_] RPRC_09, Reg_10d).
Per un PID Provider, un QEAA Provider, un PuB-EAA Provider o un non-qualified EAA Provider il Provider DEVE emettere un WRPRC distinto per ciascun Service registrato ([`EIDAS-ARF`_] RPRC_13).
Un Relying Party Intermediary Service che non dichiara intended use non riceve un WRPRC proprio; la Wallet Unit fa affidamento sul WRPRC del Relying Party Service intermediato.

**Input**

Il record firmato dell'Entità nel Register, che identifica il Relying Party Service e, per una Relying Party, ciascun intended use di tale Service, e il WRPAC valido di tale Service.
Gli attributi del certificato provengono dal corrispondente elemento ``services[]`` del record.

**Outcome**

Il WRPRC di tale Service (e intended use, ove applicabile), firmato dal Provider of WRPRC con il proprio Sign/Seal Certificate ed emesso all'Entità, che l'Entità presenta alle Wallet Unit insieme ai propri dati di registrazione.

**Process**

1. Il Provider of WRPRC è invocato senza una richiesta dell'Entità quando un WRPAC valido del Service diventa disponibile, o quando il record del Register di tale Service o intended use cambia dopo che il WRPRC precedente è stato revocato.
2. Il Provider of WRPRC verifica che l'Entità abbia un record con uno stato di registrazione valido nel Register, che il Service esista in ``services[]``, che le informazioni recate dal certificato siano coerenti con tale Service, e che il WRPAC di tale Service sia valido, come richiesto dall'Annex V, punto 3(c) di [`CIR2025/848`_].
3. Il Provider of WRPRC costruisce il WRPRC da tale elemento ``services[]`` (``name`` da ``serviceTradeName``, ``srv_id`` da ``serviceIdentifier``) e, per una Relying Party, dal corrispondente intended use, e lo firma con il proprio Sign/Seal Certificate, emesso dalla WRPRC Sign/Seal Certification Authority.
4. Il Provider of WRPRC emette il WRPRC all'Entità.
5. Il Provider of WRPRC monitora qualsiasi modifica del Register in modo automatizzato e revoca il WRPRC ove la registrazione dell'Entità o di tale Service sia modificata, sospesa o cancellata, o ove il contenuto del certificato non sia più coerente con il record, come richiesto dall'Annex V, punto 3(d) di [`CIR2025/848`_]. La revoca è pubblicata tramite la :ref:`infrastructure-trust:Token Status List (WRPRC Profile)`. Ove la registrazione resti valida, il Provider DEVE riemettere un nuovo WRPRC senza indebito ritardo.

Signature and Seal Certificate Issuance
"""""""""""""""""""""""""""""""""""""""

Il Signature and Seal Certificate Issuance copre i certificati emessi dalla PKI nazionale, ossia il Sign/Seal Certificate del PID Provider, del Fornitore di Wallet e dell'EAA Provider, tramite il meccanismo di :ref:`onboarding-system:Issuance of the X.509 Certificates through ACME and OpenID Federation`.
Il Sign/Seal Certificate di un QEAA Provider e di un PuB-EAA Provider è un certificato qualificato emesso da un Qualified Trust Service Provider, al di fuori della National Root e al di fuori di questo processo, e il suo status qualificato è valutato nell'eleggibilità, si veda :ref:`onboarding-system:Eligibility and Compliance Preconditions`.

**Input**

Le ``certificate_signing_requests`` dell'Entità per il Sign/Seal Certificate, e la Federation Trust Chain utilizzata nella challenge ``openid-federation-01``.
Gli attributi del certificato provengono dal record dell'Entità nel Register o, in sua assenza, dal Trust Mark di registrazione.

**Outcome**

Il Sign/Seal Certificate, emesso dalla Certification Authority del ruolo dell'Entità, che l'Entità utilizza per firmare o sigillare gli Attestati che emette.

**Process**

1. L'Entità richiede il Sign/Seal Certificate al servizio ACME della Certification Authority del proprio ruolo, presentando le proprie ``certificate_signing_requests`` e autenticandosi con la propria Federation Trust Chain, validata come in :ref:`trust-evaluation:Federation Entity Authentication`.
2. La Certification Authority applica la propria policy, leggendo gli attributi dal record nel Register o, in sua assenza, dal Trust Mark di registrazione.
3. La Certification Authority emette il Sign/Seal Certificate e l'Entità lo recupera.

National Authentication Certificate Issuance
""""""""""""""""""""""""""""""""""""""""""""

Il processo National Authentication Certificate Issuance emette il certificato X.509 che una Relying Party utilizza per autenticarsi nel Proximity Flow, tramite l'mdoc reader authentication di [`ISO18013-5`_].
Il certificato segue lo stesso profilo del WRPAC, eccetto per la Certificate Transparency, che si applica solo ai Wallet-Relying Party Access Certificate nel Trust Framework EUDIW, ed è emesso dalla National Authentication Certification Authority, tramite il meccanismo di :ref:`onboarding-system:Issuance of the X.509 Certificates through ACME and OpenID Federation`.

**Input**

Le ``certificate_signing_requests`` dell'Entità per il National Authentication Certificate, e la Federation Trust Chain utilizzata nella challenge ``openid-federation-01``.

**Outcome**

Il National Authentication Certificate, emesso dalla National Authentication Certification Authority, che l'Entità utilizza per autenticarsi nel Proximity Flow.

**Process**

1. L'Entità richiede il certificato al servizio ACME della National Authentication Certification Authority, presentando le proprie ``certificate_signing_requests`` e autenticandosi con la propria Federation Trust Chain, validata come in :ref:`trust-evaluation:Federation Entity Authentication`.
2. La Certification Authority applica la propria policy, leggendo gli attributi dal record nel Register o, in sua assenza, dal Trust Mark di registrazione.
3. La Certification Authority emette il National Authentication Certificate e l'Entità lo recupera.

Registration Trust Mark Issuance
""""""""""""""""""""""""""""""""

Il Registration Trust Mark Issuance emette il Trust Mark di registrazione, definito in :ref:`infrastructure-trust:Trust Mark registration-entity`.
Il Trust Mark è emesso durante la registrazione dell'Entità e non tramite ACME, ed è invocato dall'Entity Registration al completamento della registrazione di federazione.

**Input**

I dati di autorizzazione dell'Entità: i suoi entitlement e, ove applicabile, le Credenziali e gli attributi che è autorizzata a emettere o a richiedere, seguendo la logica di [`ETSI TS 119 475`_].

**Outcome**

Il Trust Mark di registrazione, emesso dal Federation Trust Anchor e recato nel Subordinate Statement sull'Entità.
Rende l'Entità riconoscibile come partecipante registrato del National Trust Framework, ed è la fonte dei dati di autorizzazione quando l'Entità non ha un record nel Register.

**Process**

1. Al completamento della registrazione di federazione, il National Federation Management costruisce il Trust Mark di registrazione con i dati di autorizzazione dell'Entità.
2. Il Federation Trust Anchor firma il Trust Mark, che è recato nel Subordinate Statement, come descritto in :ref:`onboarding-system:Entity Registration`.

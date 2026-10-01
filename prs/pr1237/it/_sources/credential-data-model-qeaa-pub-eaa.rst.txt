.. include:: ../common/common_definitions.rst
.. Included via digital-credential-management.rst at title level '=' (document title).


Modello di Dati QEAA e PuB-EAA
==============================

Questa sezione profila un Qualified Electronic Attestation of Attributes (QEAA) e un Electronic Attestation of Attributes rilasciato da o per conto di un organismo pubblico responsabile di una fonte autentica (PuB-EAA).

Si applica quando la voce del Catalogo delle Credenziali ha ``legal_type`` impostato a ``qeaa`` o ``pub-eaa``.
Si applicano le regole generiche in :ref:`credential-data-model:Modello di Dati degli Attestati Elettronici`.
Questa sezione aggiunge le regole di [`ETSI TS 119 472-1`_] per queste due classificazioni legali.

Un QEAA o un PuB-EAA MUST essere codificato come SD-JWT VC, la realizzazione al capitolo 5 di [`ETSI TS 119 472-1`_], oppure come mdoc-CBOR, la realizzazione al capitolo 6 di [`ETSI TS 119 472-1`_].
La realizzazione JSON-LD W3C VC al capitolo 7 di [`ETSI TS 119 472-1`_] e la realizzazione con certificati di attributo X.509 al capitolo 8 di [`ETSI TS 119 472-1`_] sono fuori da questa specifica.

L'emissione di questi attestati segue [`ETSI TS 119 472-3`_].
La presentazione di questi attestati segue [`ETSI TS 119 472-2`_].
La registrazione dei provider e i trust anchor restano quelli specificati per un QEAA Provider e un PuB-EAA Provider in :ref:`onboarding-system:QEAA Provider` e :ref:`onboarding-system:PuB-EAA Provider`.

Ambito
------

Gli attributi dell'Utente di un QEAA o di un PuB-EAA dipendono dal tipo di credenziale registrato nel Catalogo delle Credenziali.
Questa sezione specifica i metadati che [`ETSI TS 119 472-1`_] richiede per ogni tipo di questo genere.

L'Allegato V di [`EU_2024_1183`_] stabilisce il contenuto di un QEAA.
L'Allegato VII di [`EU_2024_1183`_] stabilisce il contenuto di un PuB-EAA.
Dove quegli allegati richiedono il nome dell'emittente, il paese, un periodo di validità o l'ubicazione del certificato di firma, la codifica è quella di questa sezione.

Categoria
---------

Il valore ``category`` identifica la classificazione legale all'interno dell'attestato.

.. _table_qeaa_pub_eaa_category:
.. list-table::
    :class: longtable
    :widths: 20 40 40
    :header-rows: 1

    * - **legal_type**
      - **Claim SD-JWT VC ``category``**
      - **Elemento mdoc ``category``**
    * - ``qeaa``
      - REQUIRED. Il valore MUST essere ``urn:etsi:esi:eaa:eu:qualified``.
      - REQUIRED. Il valore MUST essere ``urn:etsi:esi:eaa:eu:qualified``.
    * - ``pub-eaa``
      - REQUIRED. Il valore MUST essere ``urn:etsi:esi:eaa:eu:pub``.
      - REQUIRED. Il valore MUST essere ``urn:etsi:esi:eaa:eu:pub``.

Il claim e l'elemento realizzano [`ETSI TS 119 472-1`_] QEAA-5.2.2.2-02, PuB-EAA-5.2.2.3-02, QEAA-6.2.2.2-02 e PuB-EAA-6.2.2.3-02.
In mdoc l'elemento ``category`` MUST essere collocato nel namespace ``org.etsi.01947201.010101``.
Un attestato il cui ``legal_type`` è ``eaa`` MUST NOT contenere ``category`` ([`ETSI TS 119 472-1`_] EAA-5.2.2.1-01 e EAA-6.2.2.1-01).

Identificazione dell'Issuer
---------------------------

Il certificato del firmatario MUST essere un certificato qualificato.
Un QEAA usa il profilo in :ref:`infrastructure-trust:(Q)EAA Provider Sign/Seal Certificate`.
Un PuB-EAA usa il profilo in :ref:`infrastructure-trust:PuB-EAA Provider Sign/Seal Certificate`.
La firma MUST essere una firma elettronica qualificata o un sigillo elettronico qualificato ([`ETSI TS 119 472-1`_] QEAA-5.6.2-01, PuB-EAA-5.6.3-01, QEAA-6.6.2-01 e PuB-EAA-6.6.3-01).

L'identificativo di registrazione in quel certificato MUST seguire il capitolo 5.1.4 di [`ETSI EN 319 412-1`_] ([`ETSI TS 119 472-1`_] QEAA-5.2.4.2-04, PuB-EAA-5.2.4.3-04, QEAA-6.2.4.2-02 e PuB-EAA-6.2.4.3-02).
I claim ``issuing_authority`` e ``issuing_country`` restano quelli specificati in :ref:`credential-data-model:Attributi Metadata degli Attestati Elettronici SD-JWT` e in [`EU_2024/2977`_].
Il valore di ``issuing_authority`` MUST essere uguale al nome dell'issuer nel certificato qualificato.
Il valore di ``issuing_country`` MUST essere uguale al paese nel certificato qualificato.
Il claim o l'elemento ``iss_reg_id`` MUST NOT essere presente quando il certificato qualificato contiene già l'identificativo di registrazione ([`ETSI TS 119 472-1`_] EAA-5.2.4.1-11 e EAA-6.2.4.1-13).

Identità dell'Attestato
-----------------------

Il codice di identità dell'attestato identifica un attestato emesso.

In SD-JWT VC il codice di identità dell'attestato è il claim ``jti`` ([`ETSI TS 119 472-1`_] EAA-5.2.3-01).
``jti`` MAY essere presente.
Quando ``jti`` è presente, il suo valore MUST identificare in modo univoco quell'attestato.

In mdoc il codice di identità dell'attestato è l'elemento ``document_number`` ([`ETSI TS 119 472-1`_] EAA-6.2.3-01).
``document_number`` MUST essere presente.
Per una mDL, ``document_number`` MUST usare il namespace ``org.iso.18013.5.1``.
Per un mdoc che non è una mDL, ``document_number`` MUST usare il namespace ``org.iso.23220.1``.

Soggetto
--------

Ogni attributo di un QEAA o di un PuB-EAA MUST riferirsi a un solo soggetto ([`ETSI TS 119 472-1`_] QEAA-5.2.5.5-01, PuB-EAA-5.2.5.6-01, QEAA-6.2.5.5-01 e PuB-EAA-6.2.5.6-01).
Un QEAA o un PuB-EAA MUST NOT contenere ``subAttrs``.
Un QEAA o un PuB-EAA MUST NOT contenere un valore ``SubAttr``.

In SD-JWT VC, ``sub`` segue :ref:`credential-data-model:Attributi Metadata degli Attestati Elettronici SD-JWT`.
``also_known_as`` è lo pseudonimo del soggetto ([`ETSI TS 119 472-1`_] EAA-5.2.5.2-01).
``also_known_as`` MUST essere una stringa quando è presente.
Un PuB-EAA in SD-JWT VC MUST contenere esattamente uno tra ``sub`` e ``also_known_as`` ([`ETSI TS 119 472-1`_] PuB-EAA-4.2.6.8-01).
Un QEAA in SD-JWT VC MAY contenere ``sub``.
Un QEAA in SD-JWT VC MAY contenere ``also_known_as``.
Un QEAA in SD-JWT VC MUST NOT contenere sia ``sub`` sia ``also_known_as``.

In mdoc, il soggetto è identificato da ``also_known_as`` oppure dall'insieme ``given_name``, ``family_name`` e ``document_number`` ([`ETSI TS 119 472-1`_] EAA-6.2.5.1-02 e EAA-6.2.5.1-05).
L'attestato MUST contenere una di queste due identificazioni.
L'attestato MUST NOT contenerle entrambe.
``also_known_as`` MUST essere una stringa di testo nel namespace ``org.etsi.01947201.010101``.
Per una mDL, ``given_name`` e ``family_name`` MUST usare il namespace ``org.iso.18013.5.1``.
Per un mdoc che non è una mDL, ``given_name`` e ``family_name`` MUST usare il namespace ``org.iso.23220.1`` ([`ISO-IEC-23220-2`_] e [`ETSI TS 119 472-1`_] EAA-6.1-03).

Validità Tecnica e Amministrativa
---------------------------------

La validità tecnica è l'intervallo in cui l'attestato codificato e la sua firma sono validi.
La validità amministrativa è l'intervallo in cui gli attributi attestati restano validi, ad esempio la scadenza di una licenza.

In SD-JWT VC, la validità tecnica MUST essere espressa da ``nbf`` e ``exp``, già richiesti per un EAA in :ref:`credential-data-model:Attributi Metadata degli Attestati Elettronici SD-JWT` ([`ETSI TS 119 472-1`_] EAA-5.2.7.1-01 e EAA-5.2.7.1-03).
La validità amministrativa MUST essere espressa da ``issuance_date`` e ``date_of_expiry`` quando il tipo di credenziale li definisce.
Un QEAA o un PuB-EAA MUST NOT contenere ``adm_nbf``.
Un QEAA o un PuB-EAA MUST NOT contenere ``adm_exp``.

In mdoc, la validità tecnica MUST essere espressa da ``validFrom`` e ``validUntil`` all'interno di ``validityInfo`` ([`ETSI TS 119 472-1`_] EAA-6.2.7.1-01 e EAA-6.2.7.1-02).
``validFrom`` MUST essere presente.
``validUntil`` MUST essere presente.
Entrambi i valori MUST essere tempi UTC.
Entrambi i valori MUST avere la precisione del secondo intero.
Entrambi i valori MUST omettere le frazioni di secondo ([`ETSI TS 119 472-1`_] EAA-6.2.7.1-03, EAA-6.2.7.1-04 e EAA-6.2.7.1-05).
La validità amministrativa MUST essere espressa da ``issue_date`` e ``expiry_date`` nel namespace del documento ([`ETSI TS 119 472-1`_] EAA-6.2.6-01 e EAA-6.2.7.2-01).

Stato e Attestati a Vita Breve
------------------------------

Il segnale di vita breve indica che il periodo di validità è abbastanza corto da non richiedere un controllo di revoca ([`ETSI TS 119 472-1`_] EAA-4.2.13-02).

In SD-JWT VC il segnale di vita breve è il claim ``shortLived`` con valore JSON null ([`ETSI TS 119 472-1`_] EAA-5.2.12-02).
In mdoc il segnale di vita breve è l'elemento ``shortLived`` impostato a ``true`` nel namespace ``org.etsi.01947201.010101`` ([`ETSI TS 119 472-1`_] EAA-6.2.12-04).
``shortLived`` MAY essere presente.

Quando il segnale di vita breve è assente, ``status`` MUST essere presente ([`ETSI TS 119 472-1`_] QEAA-5.2.10.2-01, PuB-EAA-5.2.10.3-01, QEAA-6.2.10.2-01 e PuB-EAA-6.2.10.3-01).
Quel valore di ``status`` MUST seguire :ref:`credential-data-model:Attributi Metadata degli Attestati Elettronici SD-JWT` per SD-JWT VC.
Quel valore di ``status`` MUST seguire :ref:`credential-data-model:Mobile Security Object` per mdoc.
Token Status List, già richiesto da quelle sezioni, è il servizio di stato EAA di [`ETSI TS 119 472-1`_] capitolo 5.2.10 e capitolo 6.2.10.

Un QEAA o un PuB-EAA MAY contenere ``oneTime``.
In SD-JWT VC, un claim ``oneTime`` presente MUST avere il valore JSON null ([`ETSI TS 119 472-1`_] EAA-5.2.8.2-05).
In mdoc, ``oneTime`` MUST essere un booleano nel namespace ``org.etsi.01947201.010101`` ([`ETSI TS 119 472-1`_] EAA-6.2.8.2-03).
Quando ``oneTime`` è presente in SD-JWT VC, la Wallet Unit MUST presentare l'attestato una sola volta.
Quando ``oneTime`` è ``true`` in mdoc, la Wallet Unit MUST presentare l'attestato una sola volta.

Componenti Non Utilizzati
-------------------------

Un QEAA o un PuB-EAA MUST NOT contenere un componente audience ([`ETSI TS 119 472-1`_] EAA-5.2.8.1-01 e EAA-6.2.8.1-01).
Le restrizioni verso le Relying Party per questi attestati usano la :ref:`infrastructure-trust:Embedded Disclosure Policy (EDP)`.
Un QEAA o un PuB-EAA MUST NOT contenere un componente di servizio di rinnovo ([`ETSI TS 119 472-1`_] EAA-5.2.11-01 e EAA-6.2.11-01).
Un QEAA o un PuB-EAA in SD-JWT VC MUST NOT contenere un claim ``evidence``.
Un QEAA o un PuB-EAA in mdoc MUST NOT contenere un elemento di evidenza degli attributi ([`ETSI TS 119 472-1`_] EAA-6.2.9-01).

Profilo SD-JWT VC
-----------------

La disclosure selettiva, ``vct``, ``vct#integrity``, ``_sd`` e ``_sd_alg`` restano quelli specificati in :ref:`credential-data-model:Formato Attestato Elettronico SD-JWT-VC`.
Il valore ``vct`` MUST identificare una voce del Catalogo delle Credenziali il cui ``legal_type`` è ``qeaa`` o ``pub-eaa``.

Header Protetto
^^^^^^^^^^^^^^^

Il protected header JOSE MUST contenere ``x5u`` ([`ETSI TS 119 472-1`_] QEAA-5.6.2-02 e PuB-EAA-5.6.3-02).
Il protected header JOSE MUST contenere ``x5t#S256`` ([`ETSI TS 119 472-1`_] QEAA-5.6.2-02 e PuB-EAA-5.6.3-02).
``x5u`` MUST essere un URI HTTPS presso il quale il certificato del firmatario è disponibile gratuitamente.
``x5c`` resta REQUIRED come specificato in :ref:`credential-data-model:Attributi Metadata degli Attestati Elettronici SD-JWT`.
Il certificato end-entity in ``x5c`` MUST essere il certificato identificato da ``x5u`` e ``x5t#S256``.

Claim del Payload
^^^^^^^^^^^^^^^^^

I claim seguenti si applicano in aggiunta a :ref:`credential-data-model:Attributi Metadata degli Attestati Elettronici SD-JWT`.

.. _table_qeaa_pub_eaa_sdjwt_claims:
.. list-table::
    :class: longtable
    :widths: 20 55 25
    :header-rows: 1

    * - **Claim**
      - **Descrizione**
      - **Riferimento**
    * - ``category``
      - REQUIRED. Stringa. I valori sono specificati in :ref:`credential-data-model-qeaa-pub-eaa:Categoria`.
      - [`ETSI TS 119 472-1`_] capitolo 5.2.2
    * - ``jti``
      - OPTIONAL. Stringa. Codice di identità dell'attestato. Vedere :ref:`credential-data-model-qeaa-pub-eaa:Identità dell'Attestato`.
      - [`ETSI TS 119 472-1`_] EAA-5.2.3-02
    * - ``also_known_as``
      - CONDITIONAL. Vedere :ref:`credential-data-model-qeaa-pub-eaa:Soggetto`.
      - [`ETSI TS 119 472-1`_] EAA-5.2.5.2-02
    * - ``shortLived``
      - OPTIONAL. JSON null. Vedere :ref:`credential-data-model-qeaa-pub-eaa:Stato e Attestati a Vita Breve`.
      - [`ETSI TS 119 472-1`_] EAA-5.2.12-02
    * - ``oneTime``
      - OPTIONAL. JSON null. Vedere :ref:`credential-data-model-qeaa-pub-eaa:Stato e Attestati a Vita Breve`.
      - [`ETSI TS 119 472-1`_] EAA-5.2.8.2-05

Profilo mdoc-CBOR
-----------------

Un QEAA o un PuB-EAA che è una mDL MUST recare gli elementi mDL nel namespace ``org.iso.18013.5.1`` ([`ISO18013-5`_] e [`ETSI TS 119 472-1`_] EAA-6.1-02).
Un QEAA o un PuB-EAA che non è una mDL MUST recare gli elementi del documento nel namespace ``org.iso.23220.1`` ([`ISO-IEC-23220-2`_] e [`ETSI TS 119 472-1`_] EAA-6.1-03).
Gli elementi definiti da [`ETSI TS 119 472-1`_] MUST usare il namespace ``org.etsi.01947201.010101`` ([`ETSI TS 119 472-1`_] EAA-6.1-04).

Header del Mobile Security Object
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Per un QEAA o un PuB-EAA il protected header di ``issuerAuth`` è specificato in questa sezione.
La regola che limita il protected header all'algoritmo di firma si applica solo agli altri Attestati Elettronici, come indicato in :ref:`credential-data-model:Mobile Security Object`.

Il protected header MUST contenere l'algoritmo di firma, label ``1``.
Il protected header MUST contenere ``x5u``, label ``35``, come specificato in :rfc:`9360` ([`ETSI TS 119 472-1`_] QEAA-6.6.2-02 e PuB-EAA-6.6.3-02).
Il protected header MUST contenere ``x5t``, label ``34``, come specificato in :rfc:`9360` ([`ETSI TS 119 472-1`_] QEAA-6.6.2-02 e PuB-EAA-6.6.3-02).
L'algoritmo di hash dentro ``x5t`` MUST essere SHA-256 ([`ETSI TS 119 472-1`_] QEAA-6.6.2-03 e PuB-EAA-6.6.3-03).
``x5u`` MUST essere un URI HTTPS presso il quale il certificato del firmatario è disponibile gratuitamente.

L'unprotected header MUST contenere ``x5chain``, label ``33``, come specificato in :ref:`credential-data-model:Mobile Security Object`.
La Wallet Unit MUST recuperare il certificato del firmatario da ``x5u``.
La Wallet Unit MUST rifiutare l'attestato quando l'impronta SHA-256 di quel certificato differisce da ``x5t``.
La Wallet Unit MUST rifiutare l'attestato quando il certificato end-entity in ``x5chain`` differisce dal certificato recuperato da ``x5u``.

Namespace org.etsi.01947201.010101
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _table_qeaa_pub_eaa_mdoc_etsi_namespace:
.. list-table::
    :class: longtable
    :widths: 22 53 25
    :header-rows: 1

    * - **Elemento**
      - **Descrizione**
      - **Riferimento**
    * - ``category``
      - REQUIRED. Stringa di testo. I valori sono specificati in :ref:`credential-data-model-qeaa-pub-eaa:Categoria`.
      - [`ETSI TS 119 472-1`_] capitolo 6.2.2
    * - ``also_known_as``
      - CONDITIONAL. Stringa di testo. Vedere :ref:`credential-data-model-qeaa-pub-eaa:Soggetto`.
      - [`ETSI TS 119 472-1`_] EAA-6.2.5.2-01
    * - ``iss_reg_id``
      - Vedere :ref:`credential-data-model-qeaa-pub-eaa:Identificazione dell'Issuer`. Stringa di testo quando è presente.
      - [`ETSI TS 119 472-1`_] EAA-6.2.4.1-13
    * - ``shortLived``
      - OPTIONAL. Booleano. Vedere :ref:`credential-data-model-qeaa-pub-eaa:Stato e Attestati a Vita Breve`.
      - [`ETSI TS 119 472-1`_] EAA-6.2.12-03
    * - ``oneTime``
      - OPTIONAL. Booleano. Vedere :ref:`credential-data-model-qeaa-pub-eaa:Stato e Attestati a Vita Breve`.
      - [`ETSI TS 119 472-1`_] EAA-6.2.8.2-03

Verifica
--------

La Wallet Unit MUST rifiutare un QEAA il cui ``category`` differisce da ``urn:etsi:esi:eaa:eu:qualified``.
La Wallet Unit MUST rifiutare un PuB-EAA il cui ``category`` differisce da ``urn:etsi:esi:eaa:eu:pub``.
La Wallet Unit MUST validare la firma qualificata o il sigillo qualificato.
La Wallet Unit MUST validare il percorso del certificato dell'issuer come specificato in :ref:`trust-evaluation:Trust Evaluation Process`.
Un percorso QEAA termina sulla Trusted List del Qualified Trust Service Provider.
Un percorso PuB-EAA termina sulla List of Trusted Entities dei PuB-EAA Provider.
La Wallet Unit MUST rifiutare l'attestato fuori dalla sua validità tecnica.
Quando il segnale di vita breve è assente, la Wallet Unit MUST rifiutare l'attestato quando la Token Status List lo riporta come non valido.

La presentazione remota MUST usare [`OpenID4VP`_] come profilato da [`OPENID4VC-HAIP`_].
La presentazione in prossimità di un mdoc MUST usare [`ISO18013-5`_].

Esempi Non Normativi
--------------------

Gli esempi seguenti sono non normativi.

Protected header SD-JWT VC per un QEAA:

.. literalinclude:: ../../examples/qeaa-sd-jwt-profile-header.json
    :language: JSON

Claim SD-JWT VC aggiunti da questa sezione, mostrati senza la codifica di disclosure selettiva:

.. literalinclude:: ../../examples/qeaa-sd-jwt-profile-claims.json
    :language: JSON

Gli stessi claim per un PuB-EAA, con ``category`` impostato a ``urn:etsi:esi:eaa:eu:pub``:

.. literalinclude:: ../../examples/pub-eaa-sd-jwt-profile-claims.json
    :language: JSON

Elementi mdoc nel namespace ``org.etsi.01947201.010101`` per un QEAA, mostrati in JSON diagnostico e non come CBOR codificato:

.. literalinclude:: ../../examples/qeaa-mdoc-etsi-namespace.json
    :language: JSON

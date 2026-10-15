.. include:: ../common/common_definitions.rst
.. Included via digital-credential-management.rst at title level '=' (document title).


Modello di Dati QEAA e PuB-EAA
==============================

Questa sezione profila un Qualified Electronic Attestation of Attributes (QEAA) e un Electronic Attestation of Attributes rilasciato da o per conto di un organismo pubblico responsabile di una fonte autentica (PuB-EAA).

Si applica quando la voce del Catalogo delle Credenziali ha ``legal_type`` impostato a ``qeaa`` o ``pub-eaa``.
Si applicano le regole generiche in :ref:`credential-data-model:Modello di Dati degli Attestati Elettronici`.
Questa sezione aggiunge le regole di [`ETSI TS 119 472-1`_] per queste due classificazioni legali.

Un QEAA o un PuB-EAA DEVE essere codificato come SD-JWT VC, la realizzazione al capitolo 5 di [`ETSI TS 119 472-1`_], oppure come mdoc-CBOR, la realizzazione al capitolo 6 di [`ETSI TS 119 472-1`_].
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
      - OBBLIGATORIO. Il valore DEVE essere ``urn:etsi:esi:eaa:eu:qualified``.
      - OBBLIGATORIO. Il valore DEVE essere ``urn:etsi:esi:eaa:eu:qualified``.
    * - ``pub-eaa``
      - OBBLIGATORIO. Il valore DEVE essere ``urn:etsi:esi:eaa:eu:pub``.
      - OBBLIGATORIO. Il valore DEVE essere ``urn:etsi:esi:eaa:eu:pub``.

Il claim e l'elemento realizzano [`ETSI TS 119 472-1`_] QEAA-5.2.2.2-02, PuB-EAA-5.2.2.3-02, QEAA-6.2.2.2-02 e PuB-EAA-6.2.2.3-02.
In mdoc l'elemento ``category`` DEVE essere collocato nel namespace ``org.etsi.01947201.010101``.
Un attestato il cui ``legal_type`` è ``eaa`` NON DEVE contenere ``category`` ([`ETSI TS 119 472-1`_] EAA-5.2.2.1-01 e EAA-6.2.2.1-01).

Identificazione dell'Issuer
---------------------------

Il certificato del firmatario DEVE essere un certificato qualificato.
Un QEAA usa il profilo in :ref:`infrastructure-trust:(Q)EAA Provider Sign/Seal Certificate`.
Un PuB-EAA usa il profilo in :ref:`infrastructure-trust:PuB-EAA Provider Sign/Seal Certificate`.
La firma DEVE essere una firma elettronica qualificata o un sigillo elettronico qualificato ([`ETSI TS 119 472-1`_] QEAA-5.6.2-01, PuB-EAA-5.6.3-01, QEAA-6.6.2-01 e PuB-EAA-6.6.3-01).

L'identificativo di registrazione in quel certificato DEVE seguire il capitolo 5.1.4 di [`ETSI EN 319 412-1`_] ([`ETSI TS 119 472-1`_] QEAA-5.2.4.2-04, PuB-EAA-5.2.4.3-04, QEAA-6.2.4.2-02 e PuB-EAA-6.2.4.3-02).
In SD-JWT VC il certificato qualificato a supporto della firma è incorporato nel parametro di header ``x5c``, come richiesto in :ref:`credential-data-model-qeaa-pub-eaa:Header Protetto`.
Un QEAA o un PuB-EAA in SD-JWT VC NON DEVE contenere ``issuing_authority`` ([`ETSI TS 119 472-1`_] EAA-5.2.4.1-03).
Un QEAA o un PuB-EAA in SD-JWT VC NON DEVE contenere ``issuing_country`` ([`ETSI TS 119 472-1`_] EAA-5.2.4.1-07).
Un QEAA o un PuB-EAA in SD-JWT VC NON DEVE contenere ``iss_reg_id`` ([`ETSI TS 119 472-1`_] EAA-5.2.4.1-11).
In mdoc il certificato qualificato a supporto della firma è incorporato nell'header ``x5chain``, come richiesto in :ref:`credential-data-model-qeaa-pub-eaa:Header del Mobile Security Object`.
Un QEAA o un PuB-EAA in mdoc NON DEVE contenere ``iss_reg_id`` ([`ETSI TS 119 472-1`_] EAA-6.2.4.1-13).

Identità dell'Attestato
-----------------------

Il codice di identità dell'attestato identifica un attestato emesso.

In SD-JWT VC il codice di identità dell'attestato è il claim ``jti`` ([`ETSI TS 119 472-1`_] EAA-5.2.3-01).
``jti`` PUÒ essere presente.
Quando ``jti`` è presente, il suo valore DEVE identificare in modo univoco quell'attestato.

In mdoc il codice di identità dell'attestato è l'elemento ``document_number`` ([`ETSI TS 119 472-1`_] EAA-6.2.3-01).
``document_number`` DEVE essere presente.
Per una mDL, ``document_number`` DEVE usare il namespace ``org.iso.18013.5.1``.
Per un mdoc che non è una mDL, ``document_number`` DEVE usare il namespace ``org.iso.23220.1``.

Soggetto
--------

Ogni attributo di un QEAA o di un PuB-EAA DEVE riferirsi a un solo soggetto ([`ETSI TS 119 472-1`_] QEAA-5.2.5.5-01, PuB-EAA-5.2.5.6-01, QEAA-6.2.5.5-01 e PuB-EAA-6.2.5.6-01).
Un QEAA o un PuB-EAA NON DEVE contenere ``subAttrs``.
Un QEAA o un PuB-EAA NON DEVE contenere un valore ``SubAttr``.

In SD-JWT VC, ``sub`` segue :ref:`credential-data-model:Attributi Metadata degli Attestati Elettronici SD-JWT`.
``also_known_as`` è lo pseudonimo del soggetto ([`ETSI TS 119 472-1`_] EAA-5.2.5.2-01).
``also_known_as`` DEVE essere una stringa quando è presente.
Un PuB-EAA in SD-JWT VC DEVE contenere esattamente uno tra ``sub`` e ``also_known_as`` ([`ETSI TS 119 472-1`_] PuB-EAA-4.2.6.8-01).
Un QEAA in SD-JWT VC PUÒ contenere ``sub``.
Un QEAA in SD-JWT VC PUÒ contenere ``also_known_as``.
Un QEAA in SD-JWT VC NON DEVE contenere sia ``sub`` sia ``also_known_as``.

In mdoc, il soggetto è identificato da ``also_known_as`` oppure dall'insieme ``given_name``, ``family_name`` e ``document_number`` ([`ETSI TS 119 472-1`_] EAA-6.2.5.1-02 e EAA-6.2.5.1-05).
L'attestato DEVE contenere una di queste due identificazioni.
L'attestato NON DEVE contenerle entrambe.
``also_known_as`` DEVE essere una stringa di testo nel namespace ``org.etsi.01947201.010101``.
Per una mDL, ``given_name`` e ``family_name`` DEVONO usare il namespace ``org.iso.18013.5.1``.
Per un mdoc che non è una mDL, ``given_name`` e ``family_name`` DEVONO usare il namespace ``org.iso.23220.1`` ([`ISO-IEC-23220-2`_] e [`ETSI TS 119 472-1`_] EAA-6.1-03).

Validità Tecnica e Amministrativa
---------------------------------

La validità tecnica è l'intervallo in cui l'attestato codificato e la sua firma sono validi.
La validità amministrativa è l'intervallo in cui gli attributi attestati restano validi, ad esempio la scadenza di una licenza.

In SD-JWT VC, la validità tecnica DEVE essere espressa da ``nbf`` e ``exp``, già richiesti per un EAA in :ref:`credential-data-model:Attributi Metadata degli Attestati Elettronici SD-JWT` ([`ETSI TS 119 472-1`_] EAA-5.2.7.1-01 e EAA-5.2.7.1-03).
La validità amministrativa DEVE essere espressa da ``issuance_date`` e ``date_of_expiry`` quando il tipo di credenziale li definisce.
Un QEAA o un PuB-EAA NON DEVE contenere ``adm_nbf``.
Un QEAA o un PuB-EAA NON DEVE contenere ``adm_exp``.

In mdoc, la validità tecnica DEVE essere espressa da ``validFrom`` e ``validUntil`` all'interno di ``validityInfo`` ([`ETSI TS 119 472-1`_] EAA-6.2.7.1-01 e EAA-6.2.7.1-02).
``validFrom`` DEVE essere presente.
``validUntil`` DEVE essere presente.
Entrambi i valori DEVONO essere tempi UTC.
Entrambi i valori DEVONO avere la precisione del secondo intero.
Entrambi i valori DEVONO omettere le frazioni di secondo ([`ETSI TS 119 472-1`_] EAA-6.2.7.1-03, EAA-6.2.7.1-04 e EAA-6.2.7.1-05).
La validità amministrativa DEVE essere espressa da ``issue_date`` e ``expiry_date`` nel namespace del documento ([`ETSI TS 119 472-1`_] EAA-6.2.6-01 e EAA-6.2.7.2-01).

Stato e Attestati a Vita Breve
------------------------------

Il segnale di vita breve indica che il periodo di validità è abbastanza corto da non richiedere un controllo di revoca ([`ETSI TS 119 472-1`_] EAA-4.2.13-02).

In SD-JWT VC il segnale di vita breve è il claim ``shortLived`` con valore JSON null ([`ETSI TS 119 472-1`_] EAA-5.2.12-02).
In mdoc il segnale di vita breve è l'elemento ``shortLived`` impostato a ``true`` nel namespace ``org.etsi.01947201.010101`` ([`ETSI TS 119 472-1`_] EAA-6.2.12-04).
``shortLived`` PUÒ essere presente.

Quando il segnale di vita breve è assente, ``status`` DEVE essere presente ([`ETSI TS 119 472-1`_] QEAA-5.2.10.2-01, PuB-EAA-5.2.10.3-01, QEAA-6.2.10.2-01 e PuB-EAA-6.2.10.3-01).
Quel valore di ``status`` DEVE seguire :ref:`credential-data-model:Attributi Metadata degli Attestati Elettronici SD-JWT` per SD-JWT VC.
Quel valore di ``status`` DEVE seguire :ref:`credential-data-model:Mobile Security Object` per mdoc.
Quando ``status`` è presente in un QEAA o in un PuB-EAA in SD-JWT VC, DEVE contenere ``status_list`` con ``idx`` e ``uri``.
Quando ``status`` è presente in un QEAA o in un PuB-EAA in SD-JWT VC, DEVE contenere ``type`` con valore ``TokenStatusList`` ([`ETSI TS 119 472-1`_] EAA-5.2.10.1-04 e EAA-5.2.10.1-05).
Quando ``status`` è presente in un QEAA o in un PuB-EAA in SD-JWT VC, DEVE contenere ``purpose`` con valore ``revocation``.
Quando ``status`` è presente in un QEAA o in un PuB-EAA in SD-JWT VC, DEVE contenere ``index`` e ``uri`` ([`ETSI TS 119 472-1`_] EAA-5.2.10.1-08 e EAA-5.2.10.1-10).
Il valore di ``index`` DEVE essere uguale al valore di ``status_list.idx``.
Il valore di ``uri`` DEVE essere uguale al valore di ``status_list.uri``.
Token Status List, già richiesto da quelle sezioni, è il servizio di stato EAA di [`ETSI TS 119 472-1`_] capitolo 5.2.10 e capitolo 6.2.10.

.. warning::
  **Oggetto status in SD-JWT**

  Il capitolo 5.2.10 di [`ETSI TS 119 472-1`_] colloca ``type``, ``purpose``, ``index`` e ``uri`` sull'oggetto ``status`` di SD-JWT.
  La Sezione 6.2 di [`TOKEN-STATUS-LIST`_] colloca il riferimento in ``status.status_list``.
  Entrambe le forme sono presenti e identificano la stessa status list.
  Il capitolo 6.2.10 di [`ETSI TS 119 472-1`_] usa il membro ``status_list`` per mdoc (EAA-6.2.10.1-03).

Un QEAA o un PuB-EAA PUÒ contenere ``oneTime``.
In SD-JWT VC, un claim ``oneTime`` presente DEVE avere il valore JSON null ([`ETSI TS 119 472-1`_] EAA-5.2.8.2-05).
In mdoc, ``oneTime`` DEVE essere un booleano nel namespace ``org.etsi.01947201.010101`` ([`ETSI TS 119 472-1`_] EAA-6.2.8.2-03).
Quando ``oneTime`` è presente in SD-JWT VC, la Wallet Unit DEVE presentare l'attestato una sola volta ([`ETSI TS 119 472-1`_] EAA-5.2.8.2-03).
Quando ``oneTime`` è presente in SD-JWT VC, la Wallet Unit NON DEVE conservare l'attestato per un uso futuro ([`ETSI TS 119 472-1`_] EAA-5.2.8.2-03).
Quando ``oneTime`` è ``true`` in mdoc, la Wallet Unit DEVE presentare l'attestato una sola volta ([`ETSI TS 119 472-1`_] EAA-6.2.8.2-04).
Quando ``oneTime`` è ``true`` in mdoc, la Wallet Unit NON DEVE conservare l'attestato per un uso futuro ([`ETSI TS 119 472-1`_] EAA-6.2.8.2-04).

Componenti Non Utilizzati
-------------------------

Un QEAA o un PuB-EAA NON DEVE contenere un componente audience ([`ETSI TS 119 472-1`_] EAA-5.2.8.1-01 e EAA-6.2.8.1-01).
Le restrizioni verso le Relying Party per questi attestati usano la :ref:`infrastructure-trust:Embedded Disclosure Policy (EDP)`.
Un QEAA o un PuB-EAA NON DEVE contenere un componente di servizio di rinnovo ([`ETSI TS 119 472-1`_] EAA-5.2.11-01 e EAA-6.2.11-01).
Un QEAA o un PuB-EAA in SD-JWT VC NON DEVE contenere un claim ``evidence``.
Un QEAA o un PuB-EAA in mdoc NON DEVE contenere un elemento di evidenza degli attributi ([`ETSI TS 119 472-1`_] EAA-6.2.9-01).

Profilo SD-JWT VC
-----------------

La disclosure selettiva, ``vct``, ``vct#integrity``, ``_sd`` e ``_sd_alg`` restano quelli specificati in :ref:`credential-data-model:Formato Attestato Elettronico SD-JWT-VC`.
Il valore ``vct`` DEVE identificare una voce del Catalogo delle Credenziali il cui ``legal_type`` è ``qeaa`` o ``pub-eaa``.

Header Protetto
^^^^^^^^^^^^^^^

Il protected header JOSE DEVE contenere ``x5u`` ([`ETSI TS 119 472-1`_] QEAA-5.6.2-02 e PuB-EAA-5.6.3-02).
Il protected header JOSE DEVE contenere ``x5t#S256`` ([`ETSI TS 119 472-1`_] QEAA-5.6.2-02 e PuB-EAA-5.6.3-02).
``x5t#S256`` è il digest SHA-256, codificato in base64url, della codifica DER del certificato di firma, come specificato in :rfc:`7515`.
``x5u`` DEVE essere un URI HTTPS presso il quale il certificato del firmatario è disponibile gratuitamente.
``x5c`` resta OBBLIGATORIO come specificato in :ref:`credential-data-model:Attributi Metadata degli Attestati Elettronici SD-JWT`.
Il certificato end-entity in ``x5c`` DEVE essere il certificato identificato da ``x5u`` e ``x5t#S256``.

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
      - OBBLIGATORIO. Stringa. I valori sono specificati in :ref:`credential-data-model-qeaa-pub-eaa:Categoria`.
      - [`ETSI TS 119 472-1`_] capitolo 5.2.2
    * - ``jti``
      - OPZIONALE. Stringa. Codice di identità dell'attestato. Vedere :ref:`credential-data-model-qeaa-pub-eaa:Identità dell'Attestato`.
      - [`ETSI TS 119 472-1`_] EAA-5.2.3-02
    * - ``also_known_as``
      - CONDIZIONALE. Vedere :ref:`credential-data-model-qeaa-pub-eaa:Soggetto`.
      - [`ETSI TS 119 472-1`_] EAA-5.2.5.2-02
    * - ``shortLived``
      - OPZIONALE. JSON null. Vedere :ref:`credential-data-model-qeaa-pub-eaa:Stato e Attestati a Vita Breve`.
      - [`ETSI TS 119 472-1`_] EAA-5.2.12-02
    * - ``oneTime``
      - OPZIONALE. JSON null. Vedere :ref:`credential-data-model-qeaa-pub-eaa:Stato e Attestati a Vita Breve`.
      - [`ETSI TS 119 472-1`_] EAA-5.2.8.2-05

Profilo mdoc-CBOR
-----------------

Un QEAA o un PuB-EAA che è una mDL DEVE recare gli elementi mDL nel namespace ``org.iso.18013.5.1`` ([`ISO18013-5`_] e [`ETSI TS 119 472-1`_] EAA-6.1-02).
Un QEAA o un PuB-EAA che non è una mDL DEVE recare gli elementi del documento nel namespace ``org.iso.23220.1`` ([`ISO-IEC-23220-2`_] e [`ETSI TS 119 472-1`_] EAA-6.1-03).
Gli elementi definiti da [`ETSI TS 119 472-1`_] DEVONO usare il namespace ``org.etsi.01947201.010101`` ([`ETSI TS 119 472-1`_] EAA-6.1-04).

Header del Mobile Security Object
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Per un Attestato Elettronico che non è un QEAA o un PuB-EAA, ``issuerAuth`` è un ``COSE_Sign1`` il cui protected header contiene solo l'algoritmo di firma, come specificato in :ref:`credential-data-model:Mobile Security Object`.
Per un QEAA o un PuB-EAA in mdoc, ``issuerAuth`` DEVE essere una firma digitale CB-AdES ([`ETSI TS 119 472-1`_] EAA-6.6.1-01).
Il protected header di quella firma CB-AdES è specificato in questa sezione.

.. warning::
  **Firma issuerAuth in mdoc**

  Gli altri Attestati Elettronici in mdoc usano un ``COSE_Sign1`` il cui protected header contiene solo l'algoritmo di firma.
  [`ETSI TS 119 472-1`_] EAA-6.6.1-01 richiede una firma digitale CB-AdES.
  QEAA-6.6.2-02 e PuB-EAA-6.6.3-02 collocano ``x5u`` e ``x5t`` in quel protected header.
  QEAA-6.6.2-04 e PuB-EAA-6.6.3-04 collocano ``x5chain`` in quel protected header come indicazione DOVREBBE.
  Questa specifica usa CB-AdES per un QEAA o un PuB-EAA in mdoc.
  Il protected header contiene l'algoritmo di firma, ``x5u`` e ``x5t``.
  ``x5chain`` resta nell'unprotected header, come richiesto per ogni mdoc in :ref:`credential-data-model:Mobile Security Object`.
  Gli altri Attestati Elettronici in mdoc restano un ``COSE_Sign1``.

Il protected header DEVE contenere l'algoritmo di firma, label ``1``.
Il protected header DEVE contenere ``x5u``, label ``35``, come specificato in :rfc:`9360` ([`ETSI TS 119 472-1`_] QEAA-6.6.2-02 e PuB-EAA-6.6.3-02).
Il protected header DEVE contenere ``x5t``, label ``34``, come specificato in :rfc:`9360` ([`ETSI TS 119 472-1`_] QEAA-6.6.2-02 e PuB-EAA-6.6.3-02).
L'algoritmo di hash dentro ``x5t`` DEVE essere SHA-256 ([`ETSI TS 119 472-1`_] QEAA-6.6.2-03 e PuB-EAA-6.6.3-03).
``x5u`` DEVE essere un URI HTTPS presso il quale il certificato del firmatario è disponibile gratuitamente.

L'unprotected header DEVE contenere ``x5chain``, label ``33``, come specificato in :ref:`credential-data-model:Mobile Security Object`.
La Wallet Unit DEVE recuperare il certificato del firmatario da ``x5u``.
La Wallet Unit DEVE rifiutare l'attestato quando il digest SHA-256 della codifica DER di quel certificato differisce da ``x5t``.
La Wallet Unit DEVE rifiutare l'attestato quando il certificato end-entity in ``x5chain`` differisce dal certificato recuperato da ``x5u``.

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
      - OBBLIGATORIO. Stringa di testo. I valori sono specificati in :ref:`credential-data-model-qeaa-pub-eaa:Categoria`.
      - [`ETSI TS 119 472-1`_] capitolo 6.2.2
    * - ``also_known_as``
      - CONDIZIONALE. Stringa di testo. Vedere :ref:`credential-data-model-qeaa-pub-eaa:Soggetto`.
      - [`ETSI TS 119 472-1`_] EAA-6.2.5.2-01
    * - ``iss_reg_id``
      - NON DEVE essere presente. Vedere :ref:`credential-data-model-qeaa-pub-eaa:Identificazione dell'Issuer`.
      - [`ETSI TS 119 472-1`_] EAA-6.2.4.1-13
    * - ``shortLived``
      - OPZIONALE. Booleano. Vedere :ref:`credential-data-model-qeaa-pub-eaa:Stato e Attestati a Vita Breve`.
      - [`ETSI TS 119 472-1`_] EAA-6.2.12-03
    * - ``oneTime``
      - OPZIONALE. Booleano. Vedere :ref:`credential-data-model-qeaa-pub-eaa:Stato e Attestati a Vita Breve`.
      - [`ETSI TS 119 472-1`_] EAA-6.2.8.2-03

Verifica
--------

La Wallet Unit DEVE rifiutare un QEAA il cui ``category`` differisce da ``urn:etsi:esi:eaa:eu:qualified``.
La Wallet Unit DEVE rifiutare un PuB-EAA il cui ``category`` differisce da ``urn:etsi:esi:eaa:eu:pub``.
La Wallet Unit DEVE validare la firma qualificata o il sigillo qualificato.
La Wallet Unit DEVE rifiutare un QEAA o un PuB-EAA in SD-JWT VC quando ``x5t#S256`` differisce dal digest del certificato end-entity in ``x5c`` specificato in :ref:`credential-data-model-qeaa-pub-eaa:Header Protetto`.
La Wallet Unit DEVE rifiutare un QEAA o un PuB-EAA in SD-JWT VC quando ``x5t#S256`` differisce da quel digest del certificato recuperato da ``x5u``.
Per un mdoc, la Wallet Unit DEVE applicare il confronto già richiesto per ``x5t`` in :ref:`credential-data-model-qeaa-pub-eaa:Header del Mobile Security Object`.
La Wallet Unit DEVE validare il percorso del certificato dell'issuer come specificato in :ref:`trust-evaluation:Trust Evaluation Process`.
Un percorso QEAA termina sulla Trusted List del Qualified Trust Service Provider.
Un percorso PuB-EAA termina sulla List of Trusted Entities dei PuB-EAA Provider.
La Wallet Unit DEVE rifiutare l'attestato fuori dalla sua validità tecnica.
Quando il segnale di vita breve è assente, la Wallet Unit DEVE rifiutare l'attestato quando la Token Status List lo riporta come non valido.

La presentazione remota DEVE usare [`OpenID4VP`_] come profilato da [`OPENID4VC-HAIP`_].
La presentazione in prossimità di un mdoc DEVE usare [`ISO18013-5`_].

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

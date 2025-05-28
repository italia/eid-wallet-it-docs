.. include:: ../common/common_definitions.rst
  

Modello di Dati degli Attestati Elettronici
==============================================

Il Modello di Dati degli Attestati Elettronici struttura gli Attestati ELettronici per un uso sicuro e interoperabile. Gli elementi chiave includono:

    - Soggetto dell'Attestato Elettronico: L'individuo o l'entità che riceve l'Attestato Elettronico.
    - Fornitore di Attestato Elettronico: il soggetto che emette e firma l'Attestato Elettronico.
    - Metadata: Dettagli sull'Attestato Elettronico, come tipologia e validità.
    - Attributi dell'Utente: Informazioni sul soggetto, come identità o titoli/qualifiche.
    - Elementi crittografici: Verifica crittografica dell'autenticità e della legittimità di possesso.

L'Attestato Elettronico di Dati di Identificazione Personale (PID) è rilasciato dal Fornitore di Attestati Elettronici di Dati di Identificazione Personale secondo le leggi nazionali. Lo scopo principale del PID è consentire alle persone fisiche di essere autenticate per accedere a un servizio o a una risorsa protetta.
Gli attributi dell'Utente forniti all'interno del PID italiano sono quelli elencati di seguito:

    - Cognome
    - Nome
    - Data di Nascita
    - Codice fiscale

Gli Attestati Elettronici di Attributi (Qualificati) ((Q)EAA) sono rilasciati dai Fornitori di Attestati Elettronici di Attributi (Qualificati) ((Q)EAA) a un'Istanza del Wallet e DEVONO essere forniti in formato SD-JWT-VC o mdoc-CBOR.

Il formato dei dati dell'Attestato Elettronico e il meccanismo attraverso il quale un Attestato Elettronico viene rilasciato all'Istanza del Wallet e presentato a una Relying Party sono descritti nelle sezioni seguenti.

Attestato Elettronico in formato SD-JWT-VC
------------------------------------------

Il PID/(Q)EAA è rilasciato sotto forma di Attestato Elettronico. Il formato dell'Attestato Elettronico in `SD-JWT`_ segue le specifiche di `SD-JWT-VC`_.

SD-JWT DEVE essere firmato utilizzando la chiave privata del Fornitore di Attestati Elettronici. SD-JWT DEVE essere fornito insieme a un *Type Metadata* relativo all'Attestato Elettronico rilasciato secondo quanto indicato nelle Sezioni 6 e 6.3 di [`SD-JWT-VC`_]. Il payload DEVE contenere il claim **_sd_alg** descritto nella Sezione 4.1.1 `SD-JWT`_ e gli altri claim specificati in questa sezione.

Il claim **_sd_alg** indica l'algoritmo di hash utilizzato dal Fornitore di Attestati Elettronici per generare i digest come descritto nella Sezione 4.1.1 di `SD-JWT`_. **_sd_alg** DEVE essere valorizzato con uno degli algoritmi specificati nella Sezione :ref:`Cryptographic Algorithms <algorithms:Algoritmi Crittografici>`.

I claim che non sono divulgabili selettivamente DEVONO essere inclusi nel SD-JWT così come sono. I digest delle disclosure, insieme a eventuali decoy digest se presenti, DEVONO essere contenuti nell'array **_sd**, come specificato nella Sezione 4.2.4.1 di `SD-JWT`_.

Ogni valore di digest, calcolato applicando una funzione di hash sulle disclosure, verifica l'integrità e corrisponde a una specifica disclosure. Ogni disclosure include:

  - un *salt* casuale,
  - il nome del claim (solo quando il claim è un object element),
  - il valore del claim.

In caso di oggetti annidati (nested object) nel payload SD-JWT, ogni claim di ogni livello del JSON dovrebbe essere individualmente contrassegnato come divulgabile selettivamente o meno. Pertanto il claim **_sd** contenente i digest PUÒ apparire più volte nei diversi livelli del SD-JWT.

Per ogni claim che è un elemento di un array, i digest delle rispettive disclosure e i decoy digest vengono aggiunti all'array nella stessa posizione dei valori del claim originali come specificato nella Sezione 4.2.4.2 di `SD-JWT`_.

In caso di elementi di un array, i valori di digest vengono calcolati applicando una funzione di hash sulle disclosure, contenenti:

  - un *salt* casuale,
  - l'elemento dell'array.

In presenza di più elementi in un array, il Fornitore di Attestati Elettronici può nascondere il valore dell'intero array oppure di qualsiasi elemento contenuta all'interno dell'array, il Titolare può divulgare sia l'intero array che qualsiasi singola voce all'interno dell'array, come definito nella Sezione 4.2.6 di `SD-JWT`_.

Le disclosure vengono fornite al Titolare insieme al SD-JWT nel *Combined Format for Issuance* che è una serie ordinata di valori codificati in base64url, ciascuno separato dal successivo da un singolo carattere tilde ('~') come segue:

.. code-block:: text

  <Issuer-Signed-JWT>~<Disclosure 1>~<Disclosure 2>~...~<Disclosure N>


Vedere `SD-JWT-VC`_ e `SD-JWT`_ per ulteriori dettagli.


Parametri SD-JWT della Credenziale
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Il JOSE Header contiene i seguenti parametri obbligatori:

.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Claim**
    - **Descrizione**
    - **Riferimento**
  * - **typ**
    - OBBLIGATORIO. DEVE essere valorizzato con ``dc+sd-jwt`` come definito in `SD-JWT-VC`_.
    - :rfc:`7515` Sezione 4.1.9.
  * - **alg**
    - OBBLIGATORIO. Algoritmo di firma.
    - :rfc:`7515` Sezione 4.1.1.
  * - **kid**
    - OBBLIGATORIO. Identificativo univoco della chiave pubblica.
    - :rfc:`7515` Sezione 4.1.8.
  * - **trust_chain**
    - OPZIONALE. Array JSON contenente la catena di fiducia che dimostra l'affidabilità di chi emette il JWT.
    - [`OID-FED`_] Sezione 4.3.
  * - **x5c**
    - OPZIONALE. Contiene il certificato della chiave pubblica X.509 o la catena di certificati [:rfc:`5280`] corrispondente alla chiave utilizzata per firmare digitalmente il JWT.
    - :rfc:`7515` Sezione 4.1.8 e [`SD-JWT-VC`_] Sezione 3.5.
  * - **vctm**
    - OPZIONALE. Array JSON di documenti JSON di *Type Metadata* codificati in base64url. In caso di *Type Metadata* che ne estende un altro, questo claim contiene l'intera catena di documenti JSON.
    - [`SD-JWT-VC`_] Sezione 6.3.5.

Il payload JWT contiene i seguenti claim. Alcuni di questi claim possono essere divulgati, questi sono elencati nelle seguenti tabelle che specificano se un claim è divulgabile selettivamente [SD] o meno [NSD].

.. _table_sd-jwt-vc_parameters:
.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Descrizione**
      - **Riferimento**
    * - **iss**
      - [NSD]. OBBLIGATORIO. Stringa URL che rappresenta l'identificativo univoco del Fornitore di Attestati Elettronici.
      - `[RFC7519, Sezione 4.1.1] <https://www.iana.org/go/rfc7519>`_.
    * - **sub**
      - [NSD]. OBBLIGATORIO. L'identificativo del soggetto dell'Attestato Elettronico, l'Utente, DEVE essere un valore opaco e NON DEVE corrispondere a nessun dato anagrafico o essere derivato dai dati anagrafici dell'Utente tramite pseudonimizzazione. Inoltre, due diversi Attestati Elettronici emessi NON DEVONO utilizzare lo stesso valore di ``sub``.
      - `[RFC7519, Sezione 4.1.2] <https://www.iana.org/go/rfc7519>`_.
    * - **iat**
      - [SD]. OBBLIGATORIO. Timestamp UNIX con l'orario di emissione del JWT, codificato come NumericDate come indicato in :rfc:`7519`.
      - `[RFC7519, Sezione 4.1.6] <https://www.iana.org/go/rfc7519>`_.
    * - **exp**
      - [NSD]. OBBLIGATORIO. Timestamp UNIX con l'orario di scadenza del JWT, codificato come NumericDate come indicato in :rfc:`7519`.
      - `[RFC7519, Sezione 4.1.4] <https://www.iana.org/go/rfc7519>`_.
    * - **nbf**
      - [NSD]. OPZIONALE. Timestamp UNIX con l'orario di inizio validità del JWT, codificato come NumericDate come indicato in :rfc:`7519`.
      - `[RFC7519, Sezione 4.1.4] <https://www.iana.org/go/rfc7519>`_.
    * - **issuing_authority**
      - [NSD]. OBBLIGATORIO. Nome dell'autorità amministrativa che ha emesso l'Attestato Elettronico.
      - Regolamento di esecuzione della Commissione `EU_2024/2977`_.
    * - **issuing_country**
      - [NSD]. OBBLIGATORIO. Codice paese Alpha-2, come specificato in ISO 3166-1, del paese o territorio del Fornitore di Attestati Elettronici.
      - Regolamento di esecuzione della Commissione `EU_2024/2977`_.
    * - **status**
      - [NSD]. OBBLIGATORIO solo se l'Attestato Elettronico ha una durata superiore alle 24 ore (long-lived). Oggetto JSON contenente le informazioni su come leggere lo stato dell'Attestato Elettronico. DEVE contenere l'oggetto JSON *status_assertion* o *status_list*.
      - Sezione 3.2.2.2 `SD-JWT-VC`_ e Sezione 11 `OAUTH-STATUS-ASSERTION`_.
    * - **cnf**
      - [NSD]. OBBLIGATORIO. Oggetto JSON contenente il materiale crittografico da utilizzare come prova di possesso. L'inclusione del claim **cnf** (confirmation) in un JWT, permette al soggetto che emette il JWT di dichiarare che il Titolare ha il controllo della chiave privata relativa a quella pubblica definita nel parametro **cnf**. Il destinatario DEVE verificare crittograficamente che il Titolare abbia effettivamente il controllo di quella chiave.
      - `[RFC7800, Sezione 3.1] <https://www.iana.org/go/rfc7800>`_ e Sezione 3.2.2.2 `SD-JWT-VC`_.
    * - **vct**
      - [NSD]. OBBLIGATORIO. Il valore del tipo di Attestato Elettronico DEVE essere una stringa URL HTTPS e DEVE essere valorizzata utilizzando uno dei valori ottenuti dai metadata del Fornitore di Attestati Elettronici. È l'identificativo del tipo di SD-JWT VC e DEVE essere resistente alle collisioni come definito nella Sezione 2 di :rfc:`7515`. DEVE contenere anche il numero di versione dell'Attestato Elettronico (ad esempio: ``https://trust-registry.eid-wallet.example.it/credentials/v1.0/personidentificationdata``).
      - Sezione 3.2.2.2 `SD-JWT-VC`_.
    * - **vct#integrity**
      - [NSD]. OBBLIGATORIO. Il valore DEVE essere una stringa "integrity metadata" come definito nella Sezione 3 di [`W3C-SRI`_]. *SHA-256*, *SHA-384* e *SHA-512* DEVONO essere supportati come funzioni crittografiche di hash. *MD5* e *SHA-1* NON DEVONO essere utilizzati. Questo claim DEVE essere verificato in base a quanto indicato nella la Sezione 3.3.5 di [`W3C-SRI`_].
      - Sezione 6.1 `SD-JWT-VC`_, [`W3C-SRI`_]
    * - **verification**
      - [SD]. CONDIZIONALE. OBBLIGATORIO se il tipo di Attestato Elettronico è `PersonIdentificationData`, altrimenti è OPZIONALE. Oggetto contenente informazioni sull'autenticazione dell'Utente e sulla verifica dei dati dell'Utente. Se presente DEVE includere il seguente parametri:

          * ``trust_framework``: Stringa che identifica il trust framework utilizzato per l'autenticazione dell'Utente. DEVE essere valorizzato con uno dei valori descritti nel `trust_frameworks_supported` fornito nei Metadata del Fornitore di Attestati Elettronici.
          * ``assurance_level``: Stringa che identifica il Livello di Garanzia dell'identità garantito durante il processo di autenticazione dell'Utente.
          * ``evidence``: Ogni voce dell'array DEVE contenere i seguenti parametri:

            - ``type``: Rappresenta il tipo di evidenza. DEVE essere valorizzato con ``vouch``.
            - ``time``: Timestamp UNIX con l'orario dell'autenticazione o della verifica.
            - ``attestation``: DEVE contenere i seguenti parametri:

                - ``type``: DEVE essere valorizzato con ``digital_attestation``.
                - ``reference_number``: identificativo della risposta di autenticazione o verifica.
                - ``date_of_issuance``: data di emissione dell'attestazione.
                - ``voucher``: DEVE contenere il claim ``organization``.

      - `OIDC-IDA`.
    * - **_sd**
      - [NSD]. OBBLIGATORIO. Array di stringhe, dove ogni stringa rappresenta un digest di una disclosure.
      - 4.2.4.1 `SD-JWT`_
    * - **_sd_alg**
      - [NSD]. OBBLIGATORIO. Algoritmo di hash utilizzato dal Fornitore di Attestati Elettronici per generare i digest.
      - 4.1.1 `SD-JWT`_

Se il parametro ``status`` è valorizzato con ``status_list``, l'oggetto JSON contiene i seguenti sub parametri:

.. list-table::
   :class: longtable
   :widths: 20 60 20
   :header-rows: 1

   * - **Parametro**
     - **Descrizione**
     - **Riferimento**
   * - **idx**
     - OBBLIGATORIO. Il claim idx (index) DEVE contenere un numero intero che rappresenta l'indice da controllare per recuperare le informazioni relative allo stato nella Status List per l'Attestato Elettronico corrente. Il valore di idx DEVE essere un numero non negativo, contenente un valore uguale o superiore a zero.
     - TOKEN-STATUS-LIST_
   * - **uri**
     - OBBLIGATORIO. Il claim ``uri`` (URI) DEVE contenere una stringa che identifica la Status List Token contenente le informazioni dello stato per l'Attestato Elettronico. Il valore di ``uri`` DEVE essere un URI conforme a [:rfc:`3986`].
     - TOKEN-STATUS-LIST_


Se il parametro ``status`` è valorizzato con ``status_assertion``, l'oggetto JSON contiene il claim *credential_hash_alg* che indica l'algoritmo utilizzato per l'hashing dell'Attestato Elettronico a cui è associato la Status Assertion. Si RACCOMANDA di utilizzare *sha-256*.


.. note::
  Il documento JSON di *Type Metadata* dell'Attestato Elettronico PUÒ essere recuperato direttamente dall'URL contenuto nel claim **vct**, utilizzando il metodo GET HTTP o utilizzando il parametro di header ``vctm`` se presente. A differenza di quanto specificato nella Sezione 6.3.1 di `SD-JWT-VC`_ l'endpoint **.well-known** non è incluso nell'attuale profilo di implementazione. Gli implementatori possono comunque decidere di utilizzarlo ai fini di interoperabilità con gli altri sistemi.


Type Metadata dell'Attestato Elettronico
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Il documento di *Type Metadata* DEVE essere un oggetto JSON che contiene i seguenti parametri.

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Descrizione**
      - **Riferimento**
    * - **name**
      - OBBLIGATORIO. Nome human-readable del tipo di Attestato Elettronico. In casistiche multilingua, i tag di lingua vengono aggiunti al nome del claim, delimitandoli con il carattere `#` come definito in :rfc:`5646` (ad es. *name#it-IT*).
      - [`SD-JWT-VC`_] Sezione 6.2 e [`OIDC`_] Sezione 5.2.
    * - **description**
      - OBBLIGATORIO. Una descrizione leggibile del tipo di Attestato Elettronico. In casistiche multilingua, i tag di lingua vengono aggiunti al nome del claim, delimitandoli da un carattere `#` come definito in :rfc:`5646`.
      - [`SD-JWT-VC`_] Sezione 6.2 e [`OIDC`_] Sezione 5.2.
    * - **extends**
      - OPZIONALE. Stringa identificativa di un documento *Type Metadata* che ne estende un altro.
      - [`SD-JWT-VC`_] Sezione 6.2.
    * - **extends#integrity**
      - CONDIZIONALE. OBBLIGATORIO se **extends** è presente.
      - [`SD-JWT-VC`_] Sezione 6.2.
    * - **schema**
      - CONDIZIONALE. OBBLIGATORIO se **schema_uri** non è presente.
      - [`SD-JWT-VC`_] Sezione 6.2.
    * - **schema_uri**
      - CONDIZIONALE. OBBLIGATORIO se **schema** non è presente.
      - [`SD-JWT-VC`_] Sezione 6.2.
    * - **schema_uri#integrity**
      - CONDIZIONALE. OBBLIGATORIO se **schema_uri** è presente.
      - [`SD-JWT-VC`_] Sezione 6.2.
    * - **data_source**
      - OBBLIGATORIO. Oggetto contenente informazioni sull'origine dei dati. DEVE contenere l'oggetto ``verification`` con il seguente sub parametro:

          * ``trust_framework``: DEVE contenere il trust framework utilizzato per l'autenticazione digitale verso il sistema della Fonte Autentica.
          * ``authentic_source``: DEVE contenere i seguenti claim relativi alle informazioni sulla Fonte Autentica:

               * ``organization_name`` nome della Fonte Autentica.
               * ``organization_code`` codice identificativo della Fonte Autentica.
               * ``homepage_uri`` uri che punta alla homepage della Fonte Autentica.
               * ``contacts`` elenco dei contatti per informazioni e assistenza.
               * ``logo_uri`` URI che punta all'immagine del logo.

      - Questa specifica
    * - **display**
      - OBBLIGATORIO. Array di oggetti, uno per ogni lingua supportata, contenente informazioni di visualizzazione per il tipo di Attestato Elettronico. Contiene per ogni oggetto le seguenti proprietà:

          * ``lang``: tag di lingua come definito in :rfc:`5646` Sezione 2. [OBBLIGATORIO].
          * ``name``: nome human-readable del tipo di Attestato Elettronico. [OBBLIGATORIO].
          * ``description``: descrizione human-readable per il tipo di Attestato Elettronico. [OBBLIGATORIO].
          * ``rendering``: oggetto contenente i metodi di rendering supportati dal tipo di Attestato Elettronico. [OBBLIGATORIO]. Il metodo di rendering `svg_template` DEVE essere supportato.
            
            L'array ``svg_templates`` di oggetti contiene per ogni template SVG supportato le seguenti proprietà:

                * ``uri``: URI che punta al template SVG. [OBBLIGATORIO].
                * ``uri#integrity``: "integrity metadata" come definito nella Sezione 3 di `W3C-SRI`_. [OBBLIGATORIO].
                * ``properties``: oggetto contenente le proprietà del template SVG. Questa proprietà è OBBLIGATORIA se è presente più di un template SVG. L'oggetto DEVE contenere almeno una delle proprietà definite in `SD-JWT-VC`_ Sezione 8.1.2.1.

            Se è supportato anche il metodo di rendering `simple`, l'oggetto ``simple`` contiene le seguenti proprietà:

                * ``logo``: oggetto contenente informazioni sul logo da visualizzare. Questa proprietà è OBBLIGATORIA. L'oggetto contiene i seguenti sotto-valori:

                    * ``uri``: URI che punta all'immagine del logo. [OBBLIGATORIO]
                    * ``uri#integrity``: "integrity metadata" come definito nella Sezione 3 di `W3C-SRI`_. [OBBLIGATORIO].
                    * ``alt_text``: stringa contenente del testo alternativo da visualizzare al posto dell'immagine del logo. [OPZIONALE].

                * ``background_color``: valore del colore in RGB come definito in `W3C.CSS-COLOR`_ per lo sfondo dell'Attestato Elettronico. [OPZIONALE].
                * ``text_color``: valore del colore in RGB come definito in `W3C.CSS-COLOR`_ per il testo dell'Attestato Elettronico. [OPZIONALE].

          .. note::
            L'uso del template SVG è RACCOMANDATO per tutte le applicazioni che lo supportano.

      - [`SD-JWT-VC`_] Sezione 8.
    * - **claims**
      - OBBLIGATORIO. Array di oggetti contenenti informazioni per la visualizzazione e la convalida dei claim dell'Attestato Elettronico. Contiene per ogni claim dell'Attestato Elettronico le seguenti proprietà:

          * ``path``: array che indica i/il claim a cui ci si riferisce. [OBBLIGATORIO].
          * ``display``: array contenente informazioni di visualizzazione sul claim indicato nel ``path``. L'array contiene un oggetto per ogni lingua supportata dal tipo di Attestato Elettronico. Questa proprietà è OBBLIGATORIA. Contiene i seguenti parametri:
             * ``lang``: tag di lingua come definito in :rfc:`5646` Sezione 2. [OBBLIGATORIO].
             * ``label``: etichetta human-readable per il claim. [OBBLIGATORIO].
             * ``description``: descrizione human-readable per il claim. [OBBLIGATORIO].
          * ``sd``: stringa che indica se il claim è divulgabile selettivamente. DEVE essere impostato su `always` se il claim è divulgabile selettivamente o `never` se non lo è. [OBBLIGATORIO].
          * ``svg_id``: stringa alfanumerica contenente l'ID del claim referenziato nel template SVG come definito in [`SD-JWT-VC`_] Sezione 9. [OBBLIGATORIO].
      - [`SD-JWT-VC`_] Sezione 9.


Un esempio non normativo di *Type Metadata* dell'Attestato Elettronico è fornito di seguito.

.. literalinclude:: ../../examples/vc-metadata-type.json
  :language: JSON

Attributi PID dell'Utente
^^^^^^^^^^^^^^^^^^^^^^^^^

A seconda del tipo di Attestato Elettronico **vct**, possono essere aggiunti dei claim aggiuntivi, il PID supporta i seguenti:

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Descrizione**
      - **Riferimento**
    * - **given_name**
      - [SD]. OBBLIGATORIO. Nome. (*Stringa*)
      - Sezione 5.1 di `OIDC`_ e Regolamento di esecuzione della Commissione `EU_2024/2977`_
    * - **family_name**
      - [SD]. OBBLIGATORIO. Cognome. (*Stringa*)
      - Sezione 5.1 di `OIDC`_ e Regolamento di esecuzione della Commissione `EU_2024/2977`_
    * - **birth_date**
      - [SD]. OBBLIGATORIO. Data di Nascita. (*Stringa, formato [ISO8601‑1] YYYY-MM-DD*)
      - Regolamento di esecuzione della Commissione `EU_2024/2977`_
    * - **birth_place**
      - [SD]. OBBLIGATORIO. Luogo di Nascita. (*Stringa*)
      - Regolamento di esecuzione della Commissione `EU_2024/2977`_
    * - **nationalities**
      - [SD]. OBBLIGATORIO. Uno o più codici paese alpha-2 come specificato in ISO 3166-1. (*Array di stringhe*)
      - Regolamento di esecuzione della Commissione `EU_2024/2977`_
    * - **personal_administrative_number**
      - [SD]. CONDIZIONALE. OBBLIGATORIO se ``tax_id_code`` non è presente. Identificativo univoco nazionale di una persona fisica generato da ANPR. (*Stringa*)
      - Regolamento di esecuzione della Commissione `EU_2024/2977`_
    * - **tax_id_code**
      - [SD]. CONDIZIONALE. OBBLIGATORIO se ``personal_administrative_number`` non è presente. Codice di identificazione fiscale nazionale della persona fisica. DEVE essere conforme a ETSI EN 319 412-1. Ad esempio ``TINIT-<ItalianTaxIdentificationNumber>``. (*Stringa*)
      -


Esempi Non Normativi di PID
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Di seguito, l'esempio non normativo del payload di un PID rappresentato in formato JSON.

.. literalinclude:: ../../examples/pid-json-example-payload.json
  :language: JSON

La versione SD-JWT corrispondente per il PID è data da

.. literalinclude:: ../../examples/pid-sd-jwt-example-header.json
  :language: JSON

.. literalinclude:: ../../examples/pid-sd-jwt-example-payload.json
  :language: JSON

L'elenco delle disclosure è presentato di seguito.

**Claim** ``iat``:

- Hash SHA-256: ``Yrc-s-WSr4exEYtqDEsmRl7spoVfmBxixP12e4syqNE``
- Disclosure:
   ``WyIyR0xDNDJzS1F2ZUNmR2ZyeU5STjl3IiwgImlhdCIsIDE2ODMwMDAwMDBd``
- Contenuto: ``["2GLC42sKQveCfGfryNRN9w", "iat", 1683000000]``

**Claim** ``verification``:

- Hash SHA-256: ``h7Egl5H9gTPC_FCU845aadvsC--dTjy9Nrstxh-caRo``
- Disclosure:
   ``WyJlbHVWNU9nM2dTTklJOEVZbnN4QV9BIiwgInZlcmlmaWNhdGlvbiIsIHsi``
   ``dHJ1c3RfZnJhbWV3b3JrIjogIml0X2NpZSIsICJhc3N1cmFuY2VfbGV2ZWwi``
   ``OiAiaGlnaCIsICJldmlkZW5jZSI6IHsidHlwZSI6ICJ2b3VjaCIsICJ0aW1l``
   ``IjogIjIwMjAtMDMtMTlUMTI6NDJaIiwgImF0dGVzdGF0aW9uIjogeyJ0eXBl``
   ``IjogImRpZ2l0YWxfYXR0ZXN0YXRpb24iLCAicmVmZXJlbmNlX251bWJlciI6``
   ``ICI2NDg1LTE2MTktMzk3Ni02NjcxIiwgImRhdGVfb2ZfaXNzdWFuY2UiOiAi``
   ``MjAyMC0wMy0xOVQxMjo0M1oiLCAidm91Y2hlciI6IHsib3JnYW5pemF0aW9u``
   ``IjogIk1pbmlzdGVybyBkZWxsJ0ludGVybm8ifX19fV0``
- Contenuto: ``["eluV5Og3gSNII8EYnsxA_A", "verification",``
   ``{"trust_framework": "it_cie", "assurance_level": "high", "evidence": {"type": "vouch",``
   ``"time": "2020-03-19T12:42Z", "attestation": {"type":``
   ``"digital_attestation", "reference_number":``
   ``"6485-1619-3976-6671", "date_of_issuance":``
   ``"2020-03-19T12:43Z", "voucher": {"organization": "Ministero``
   ``dell'Interno"}}}}]``

**Claim** ``given_name``:

- Hash SHA-256: ``zVdghcmClMVWlUgGsGpSkCPkEHZ4u9oWj1SlIBlCc1o``
- Disclosure:
   ``WyI2SWo3dE0tYTVpVlBHYm9TNXRtdlZBIiwgImdpdmVuX25hbWUiLCAiTWFy``
   ``aW8iXQ``
- Contenuto: ``["6Ij7tM-a5iVPGboS5tmvVA", "given_name", "Mario"]``

**Claim** ``family_name``:

- Hash SHA-256: ``VQI-S1mT1Kxfq2o8J9io7xMMX2MIxaG9M9PeJVqrMcA``
- Disclosure:
   ``WyJlSThaV205UW5LUHBOUGVOZW5IZGhRIiwgImZhbWlseV9uYW1lIiwgIlJv``
   ``c3NpIl0``
- Contenuto: ``["eI8ZWm9QnKPpNPeNenHdhQ", "family_name", "Rossi"]``

**Claim** ``birth_date``:

- Hash SHA-256: ``s1XK5f2pM3-aFTauXhmvd9pyQTJ6FMUhc-JXfHrxhLk``
- Disclosure:
   ``WyJRZ19PNjR6cUF4ZTQxMmExMDhpcm9BIiwgImJpcnRoX2RhdGUiLCAiMTk4``
   ``MC0wMS0xMCJd``
- Contenuto: ``["Qg_O64zqAxe412a108iroA", "birth_date", "1980-01-10"]``

**Claim** ``birth_place``:

- Hash SHA-256: ``tSL-e1nLdWOU9sFMTCUu5P1tCzxA-TW-VWbHGzYtU7E``
- Disclosure:
  ``WyJBSngtMDk1VlBycFR0TjRRTU9xUk9BIiwgImJpcnRoX3BsYWNlIiwgIlJv``
  ``bWEiXQ``
- Contenuto: ``["AJx-095VPrpTtN4QMOqROA", "birth_place", "Roma"]``

**Claim** ``personal_administrative_number``:

- Hash SHA-256: ``6WLNc09rBr-PwEtnWzxGKdzImjrpDxbr4qoIx838a88``
- Disclosure:
   ``WyJHMDJOU3JRZmpGWFE3SW8wOXN5YWpBIiwgInBlcnNvbmFsX2FkbWluaXN0``
   ``cmF0aXZlX251bWJlciIsICJYWDAwMDAwWFgiXQ``
- Contenuto: ``["G02NSrQfjFXQ7Io09syajA", "personal_administrative_number",``
   ``"XX00000XX"]``

**Claim** ``tax_id_code``:

- Hash SHA-256: ``LqrtU2rlA51U97cMiYhqwa-is685bYiOJImp8a5KGNA``
- Disclosure:
   ``WyJsa2x4RjVqTVlsR1RQVW92TU5JdkNBIiwgInRheF9pZF9jb2RlIiwgIlRJ``
   ``TklULVhYWFhYWFhYWFhYWFhYWFgiXQ``
- Contenuto: ``["lklxF5jMYlGTPUovMNIvCA", "tax_id_code",``
   ``"TINIT-XXXXXXXXXXXXXXXX"]``

**Voce Array** di ``nationalities``:

- Hash SHA-256: ``yKeP1CWTQK8Sd9BeNvFhkLXgEu/1G3QQz4CWSlqEOFw``
- Disclosure: ``WyJQYzMzSk0yTGNoY1VfbEhnZ3ZfdWZRIiwgIklUIl0``
- Contenuto: ``["Pc33JM2LchcU_lHggv_ufQ", "IT"]``

Il *combined format* per l'emissione del PID è dato da:

.. code-block:: text

  eyJhbGciOiAiRVMyNTYiLCAidHlwIjogImRjK3NkLWp3dCIsICJraWQiOiAiZEI2N2dM
  N2NrM1RGaUlBZjdONl83U0h2cWswTURZTUVRY29HR2xrVUFBdyJ9.ewogICJfc2QiOiB
  bCiAgICAiNldMTmMwOXJCci1Qd0V0bld6eEdLZHpJbWpycER4YnI0cW9JeDgzOGE4OCI
  sCiAgICAiTHFydFUycmxBNTFVOTdjTWlZaHF3YS1pczY4NWJZaU9KSW1wOGE1S0dOQSI
  sCiAgICAiVlFJLVMxbVQxS3hmcTJvOEo5aW83eE1NWDJNSXhhRzlNOVBlSlZxck1jQSI
  sCiAgICAiWXJjLXMtV1NyNGV4RVl0cURFc21SbDdzcG9WZm1CeGl4UDEyZTRzeXFORSI
  sCiAgICAiaDdFZ2w1SDlnVFBDX0ZDVTg0NWFhZHZzQy0tZFRqeTlOcnN0eGgtY2FSbyI
  sCiAgICAiczFYSzVmMnBNMy1hRlRhdVhobXZkOXB5UVRKNkZNVWhjLUpYZkhyeGhMayI
  sCiAgICAidFNMLWUxbkxkV09VOXNGTVRDVXU1UDF0Q3p4QS1UVy1WV2JIR3pZdFU3RSI
  sCiAgICAielZkZ2hjbUNsTVZXbFVnR3NHcFNrQ1BrRUhaNHU5b1dqMVNsSUJsQ2MxbyI
  KICBdLAogICJleHAiOiAxODgzMDAwMDAwLAogICJpc3MiOiAiaHR0cHM6Ly9waWRwcm9
  2aWRlci5leGFtcGxlLm9yZyIsCiAgInN1YiI6ICJOemJMc1hoOHVEQ2NkN25vV1hGWkF
  mSGt4WnNSR0M5WHMiLAogICJpc3N1aW5nX2F1dGhvcml0eSI6ICJJc3RpdHV0byBQb2x
  pZ3JhZmljbyBlIFplY2NhIGRlbGxvIFN0YXRvIiwKICAiaXNzdWluZ19jb3VudHJ5Ijo
  gIklUIiwKICAic3RhdHVzIjogewogICAgInN0YXR1c19hc3NlcnRpb24iOiB7CiAgICA
  gICJjcmVkZW50aWFsX2hhc2hfYWxnIjogInNoYS0yNTYiCiAgICB9CiAgfSwKICAibmF
  0aW9uYWxpdGllcyI6IFsKCXsKICAgICAgIi4uLiI6ICJ5S2VQMUNXVFFLOFNkOUJlTnZ
  GaGtMWGdFdS8xRzNRUXo0Q1dTbHFFT0Z3IgogICAgfQogIF0sCiAgInZjdCI6ICJodHR
  wczovL3RydXN0LXJlZ2lzdHJ5LmVpZC13YWxsZXQuZXhhbXBsZS5pdC9jcmVkZW50aWF
  scy92MS4wL3BlcnNvbmlkZW50aWZpY2F0aW9uZGF0YSIsCiAgInZjdCNpbnRlZ3JpdHk
  iOiAiYzVmNzNlMjUwZmU4NjlmMjRkMTUxMThhY2NlMjg2YzliYjU2YjYzYTQ0M2RjODV
  hZjY1M2NkNzNmNjA3OGIxZiIsCiAgIl9zZF9hbGciOiAic2hhLTI1NiIsCiAgImNuZiI
  6IHsKICAgICJqd2siOiB7CiAgICAgICJrdHkiOiAiRUMiLAogICAgICAiY3J2IjogIlA
  tMjU2IiwKICAgICAgIngiOiAiVENBRVIxOVp2dTNPSEY0ajRXNHZmU1ZvSElQMUlMaWx
  EbHM3dkNlR2VtYyIsCiAgICAgICJ5IjogIlp4amlXV2JaTVFHSFZXS1ZRNGhiU0lpcnN
  WZnVlY0NFNnQ0alQ5RjJIWlEiCiAgICB9CiAgfQp9.ISeLw-Tqpmcos9ms7KQTfUhSm4
  srAtGOMNQe3M-toaYhCcT4JnvZANmtBb8rOXdJ60oTtya4krCOjFNirEg3-g~WyIyR0x
  DNDJzS1F2ZUNmR2ZyeU5STjl3IiwgImlhdCIsIDE2ODMwMDAwMDBd~WyJlbHVWNU9nM2
  dTTklJOEVZbnN4QV9BIiwgInZlcmlmaWNhdGlvbiIsIHsidHJ1c3RfZnJhbWV3b3JrIj
  ogIml0X2NpZSIsICJhc3N1cmFuY2VfbGV2ZWwiOiAiaGlnaCIsICJldmlkZW5jZSI6IH
  sidHlwZSI6ICJ2b3VjaCIsICJ0aW1lIjogIjIwMjAtMDMtMTlUMTI6NDJaIiwgImF0dG
  VzdGF0aW9uIjogeyJ0eXBlIjogImRpZ2l0YWxfYXR0ZXN0YXRpb24iLCAicmVmZXJlbm
  NlX251bWJlciI6ICI2NDg1LTE2MTktMzk3Ni02NjcxIiwgImRhdGVfb2ZfaXNzdWFuY2
  UiOiAiMjAyMC0wMy0xOVQxMjo0M1oiLCAidm91Y2hlciI6IHsib3JnYW5pemF0aW9uIj
  ogIk1pbmlzdGVybyBkZWxsJ0ludGVybm8ifX19fV0~WyI2SWo3dE0tYTVpVlBHYm9TNX
  RtdlZBIiwgImdpdmVuX25hbWUiLCAiTWFyaW8iXQ~WyJlSThaV205UW5LUHBOUGVOZW5
  IZGhRIiwgImZhbWlseV9uYW1lIiwgIlJvc3NpIl0~WyJRZ19PNjR6cUF4ZTQxMmExMDh
  pcm9BIiwgImJpcnRoX2RhdGUiLCAiMTk4MC0wMS0xMCJd~WyJBSngtMDk1VlBycFR0Tj
  RRTU9xUk9BIiwgImJpcnRoX3BsYWNlIiwgIlJvbWEiXQ~WyJQYzMzSk0yTGNoY1VfbEh
  nZ3ZfdWZRIiwgIklUIl0~WyJHMDJOU3JRZmpGWFE3SW8wOXN5YWpBIiwgInBlcnNvbmF
  sX2FkbWluaXN0cmF0aXZlX251bWJlciIsICJYWDAwMDAwWFgiXQ~WyJsa2x4RjVqTVls
  R1RQVW92TU5JdkNBIiwgInRheF9pZF9jb2RlIiwgIlRJTklULVhYWFhYWFhYWFhYWFhY
  WFgiXQ~

Esempi Non Normativi di (Q)EAA
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Di seguito è riportato un esempio non normativo di (Q)EAA in JSON.

.. literalinclude:: ../../examples/qeaa-json-example-payload.json
  :language: JSON

Il corrispondente SD-JWT è rappresentato di seguito, con header e payload decodificati in JSON.

.. literalinclude:: ../../examples/qeaa-sd-jwt-example-header.json
  :language: JSON

.. literalinclude:: ../../examples/qeaa-sd-jwt-example-payload.json
  :language: JSON

Di seguito è riportato l'elenco delle disclosure:

**Claim** ``iat``:

- Hash SHA-256: ``Yrc-s-WSr4exEYtqDEsmRl7spoVfmBxixP12e4syqNE``
- Disclosure:
   ``WyIyR0xDNDJzS1F2ZUNmR2ZyeU5STjl3IiwgImlhdCIsIDE2ODMwMDAwMDBd``
- Contenuto: ``["2GLC42sKQveCfGfryNRN9w", "iat", 1683000000]``

**Claim** ``document_number``:

- Hash SHA-256: ``Dx-6hjvrcxNzF0slU6ukNmzHoL-YvBN-tFa0T8X-bY0``
- Disclosure:
   ``WyJlbHVWNU9nM2dTTklJOEVZbnN4QV9BIiwgImRvY3VtZW50X251bWJlciIs``
   ``ICJYWFhYWFhYWFhYIl0``
- Contenuto:
   ``["eluV5Og3gSNII8EYnsxA_A", "document_number", "XXXXXXXXXX"]``

**Claim** ``given_name``:

- Hash SHA-256: ``zVdghcmClMVWlUgGsGpSkCPkEHZ4u9oWj1SlIBlCc1o``
- Disclosure:
   ``WyI2SWo3dE0tYTVpVlBHYm9TNXRtdlZBIiwgImdpdmVuX25hbWUiLCAiTWFy``
   ``aW8iXQ``
- Contenuto: ``["6Ij7tM-a5iVPGboS5tmvVA", "given_name", "Mario"]``

**Claim** ``family_name``:

- Hash SHA-256: ``VQI-S1mT1Kxfq2o8J9io7xMMX2MIxaG9M9PeJVqrMcA``
- Disclosure:
   ``WyJlSThaV205UW5LUHBOUGVOZW5IZGhRIiwgImZhbWlseV9uYW1lIiwgIlJv``
   ``c3NpIl0``
- Contenuto: ``["eI8ZWm9QnKPpNPeNenHdhQ", "family_name", "Rossi"]``

**Claim** ``birth_date``:

- Hash SHA-256: ``s1XK5f2pM3-aFTauXhmvd9pyQTJ6FMUhc-JXfHrxhLk``
- Disclosure:
   ``WyJRZ19PNjR6cUF4ZTQxMmExMDhpcm9BIiwgImJpcnRoX2RhdGUiLCAiMTk4``
   ``MC0wMS0xMCJd``
- Contenuto: ``["Qg_O64zqAxe412a108iroA", "birth_date", "1980-01-10"]``

**Claim** ``expiry_date``:

- Hash SHA-256: ``aBVdfcnxT0Z5RrwdxZSUhuUxz3gM2vcEZLeYIj61Kas``
- Disclosure:
   ``WyJBSngtMDk1VlBycFR0TjRRTU9xUk9BIiwgImV4cGlyeV9kYXRlIiwgIjIw``
   ``MjQtMDEtMDEiXQ``
- Contenuto: ``["AJx-095VPrpTtN4QMOqROA", "expiry_date", "2024-01-01"]``

**Claim** ``personal_administrative_number``:

- Hash SHA-256: ``o1cHG8JbEEYv0HeJINYKbFLd-TnEDUuNzI1XpzV32aU``
- Disclosure:
   ``WyJQYzMzSk0yTGNoY1VfbEhnZ3ZfdWZRIiwgInBlcnNvbmFsX2FkbWluaXN0``
   ``cmF0aXZlX251bWJlciIsICJYWDAwMDAwWFgiXQ``
- Contenuto: ``["Pc33JM2LchcU_lHggv_ufQ", "personal_administrative_number",``
   ``"XX00000XX"]``

**Claim** ``constant_attendance_allowance``:

- Hash SHA-256: ``GE3Sjy_zAT34f8wa5DUkVB0FslaSJRAAc8I3lN11Ffc``
- Disclosure:
   ``WyJHMDJOU3JRZmpGWFE3SW8wOXN5YWpBIiwgImNvbnN0YW50X2F0dGVuZGFu``
   ``Y2VfYWxsb3dhbmNlIiwgdHJ1ZV0``
- Contenuto:
   ``["G02NSrQfjFXQ7Io09syajA", "constant_attendance_allowance",``
   ``true]``


Il *combined format* per l'emissione del (Q)EAA è rappresentato di seguito:

.. code-block:: text

  eyJhbGciOiAiRVMyNTYiLCAidHlwIjogImRjK3NkLWp3dCIsICJraWQiOiAiZDEyNmE2
  YTg1NmY3NzI0NTYwNDg0ZmE5ZGM1OWQxOTUifQ.eyJfc2QiOiBbIkR4LTZoanZyY3hOe
  kYwc2xVNnVrTm16SG9MLVl2Qk4tdEZhMFQ4WC1iWTAiLCAiR0UzU2p5X3pBVDM0Zjh3Y
  TVEVWtWQjBGc2xhU0pSQUFjOEkzbE4xMUZmYyIsICJWUUktUzFtVDFLeGZxMm84Sjlpb
  zd4TU1YMk1JeGFHOU05UGVKVnFyTWNBIiwgIllyYy1zLVdTcjRleEVZdHFERXNtUmw3c
  3BvVmZtQnhpeFAxMmU0c3lxTkUiLCAiYUJWZGZjbnhUMFo1UnJ3ZHhaU1VodVV4ejNnT
  TJ2Y0VaTGVZSWo2MUthcyIsICJvMWNIRzhKYkVFWXYwSGVKSU5ZS2JGTGQtVG5FRFV1T
  npJMVhwelYzMmFVIiwgInMxWEs1ZjJwTTMtYUZUYXVYaG12ZDlweVFUSjZGTVVoYy1KW
  GZIcnhoTGsiLCAielZkZ2hjbUNsTVZXbFVnR3NHcFNrQ1BrRUhaNHU5b1dqMVNsSUJsQ
  2MxbyJdLCAiZXhwIjogMTg4MzAwMDAwMCwgImlzcyI6ICJodHRwczovL2lzc3Vlci5le
  GFtcGxlLm9yZyIsICJzdWIiOiAiTnpiTHNYaDh1RENjZDdub1dYRlpBZkhreFpzUkdDO
  VhzIiwgImlzc3VpbmdfYXV0aG9yaXR5IjogIklzdGl0dXRvIFBvbGlncmFmaWNvIGUgW
  mVjY2EgZGVsbG8gU3RhdG8iLCAiaXNzdWluZ19jb3VudHJ5IjogIklUIiwgInN0YXR1c
  yI6IHsic3RhdHVzX2Fzc2VydGlvbiI6IHsiY3JlZGVudGlhbF9oYXNoX2FsZyI6ICJza
  GEtMjU2In19LCAidmN0IjogImh0dHBzOi8vdHJ1c3QtcmVnaXN0cnkuZWlkLXdhbGxld
  C5leGFtcGxlLml0L2NyZWRlbnRpYWxzL3YxLjAvRXVyb3BlYW5EaXNhYmlsaXR5Q2FyZ
  CIsICJ2Y3QjaW50ZWdyaXR5IjogIjJlNDBiY2Q2Nzk5MDA4MDg1ZmZiMWExZjM1MTdlZ
  mVlMzM1Mjk4ZmQ5NzZiM2U2NTViZmIzZjRlYWExMWQxNzEiLCAiX3NkX2FsZyI6ICJza
  GEtMjU2IiwgImNuZiI6IHsiandrIjogeyJrdHkiOiAiRUMiLCAiY3J2IjogIlAtMjU2I
  iwgIngiOiAiVENBRVIxOVp2dTNPSEY0ajRXNHZmU1ZvSElQMUlMaWxEbHM3dkNlR2VtY
  yIsICJ5IjogIlp4amlXV2JaTVFHSFZXS1ZRNGhiU0lpcnNWZnVlY0NFNnQ0alQ5RjJIW
  lEifX19.2Dt5a6CFNv-YAmfewZGERmlIOdYybaNtZP6Va1zHZ_IqZAGM8S6M4mcTU-RO
  3X4cU4j20xif2Ocf1jvd2L5CRQ~WyIyR0xDNDJzS1F2ZUNmR2ZyeU5STjl3IiwgImlhd
  CIsIDE2ODMwMDAwMDBd~WyJlbHVWNU9nM2dTTklJOEVZbnN4QV9BIiwgImRvY3VtZW50
  X251bWJlciIsICJYWFhYWFhYWFhYIl0~WyI2SWo3dE0tYTVpVlBHYm9TNXRtdlZBIiwg
  ImdpdmVuX25hbWUiLCAiTWFyaW8iXQ~WyJlSThaV205UW5LUHBOUGVOZW5IZGhRIiwgI
  mZhbWlseV9uYW1lIiwgIlJvc3NpIl0~WyJRZ19PNjR6cUF4ZTQxMmExMDhpcm9BIiwgI
  mJpcnRoX2RhdGUiLCAiMTk4MC0wMS0xMCJd~WyJBSngtMDk1VlBycFR0TjRRTU9xUk9B
  IiwgImV4cGlyeV9kYXRlIiwgIjIwMjQtMDEtMDEiXQ~WyJQYzMzSk0yTGNoY1VfbEhnZ
  3ZfdWZRIiwgInBlcnNvbmFsX2FkbWluaXN0cmF0aXZlX251bWJlciIsICJYWDAwMDAwW
  FgiXQ~WyJHMDJOU3JRZmpGWFE3SW8wOXN5YWpBIiwgImNvbnN0YW50X2F0dGVuZGFuY2
  VfYWxsb3dhbmNlIiwgdHJ1ZV0~

Attestato Elettronico in formato mdoc-CBOR
------------------------------------------

Il modello dati mdoc si basa sullo standard ISO/IEC 18013-5.
I dati in mdoc DEVONO essere codificati in CBOR come definito in :rfc:`8949`.

Questo modello dati struttura gli Attestati Elettronici in componenti distinti: namespaces (**nameSpaces**) e prova crittografica (**issuerAuth**).
I namespace categorizzano e strutturano i dati (o attributi, vedi :ref:`credential-data-model:Attribute Namespaces`). Mentre la prova crittografica garantisce integrità e autenticità attraverso il Mobile Security Object (MSO).

L'MSO memorizza in modo sicuro i digest crittografici degli attributi all'interno dei `nameSpaces`. Ciò consente alle Relying Party di convalidare gli attributi divulgati rispetto ai valori **digestID** corrispondenti senza rivelare l'intero Attestato Elettronico.
Vedere :ref:`credential-data-model:Mobile Security Object` per i dettagli.

Un Attestato Elettronico in formato mdoc-CBOR DEVE avere la seguente struttura:

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Parametro**
      - **Descrizione**
      - **Riferimento**
    * - **nameSpaces**
      - *(map)*. All'interno dei ``namespaces`` vengono definiti i dati. Un Attestato Elettronico PUÒ includere più namespace. Gli attributi mDL obbligatori utilizzano il namespace standard `org.iso.18013.5.1`. Tuttavia, PUÒ avere anche un namespace domestico definito a livello nazionale, come `org.iso.18013.5.1.IT`, per includere attributi aggiuntivi definiti nel profilo di implementazione corrente. Ogni namespace all'interno di `nameSpaces` DEVE condividere lo stesso valore del tipo di documento emesso (`docType`), che identifica la natura dell'Attestato Elettronico, come definito in `issuerAuth`.
      - [ISO 18013-5#8.3.2.1.2]
    * - **issuerAuth**
      - *(COSE_Sign1)*. Contiene *Mobile Security Object* (MSO), un documento COSE Sign1, emesso dal Fornitore di Attestati Elettronici.
      - [ISO 18013-5#9.1.2.4]

La struttura di una Credenziale in formato mdoc-CBOR è ulteriormente descritta nelle sezioni seguenti.

Attributi dei Namespaces
^^^^^^^^^^^^^^^^^^^^^^^^

**nameSpaces** contiene una o più voci *nameSpace*, ciascuna identificata da un nome. All'interno di ogni **nameSpace**, sono inclusi uno o più *IssuerSignedItemBytes*, ciascuno codificato in una stringa di byte codificata in CBOR con Tag 24 (#6.24(bstr .cbor)), che appare come 24(<<... >>) nella notazione diagnostica. Essa rappresenta le informazioni da divulgare, una per ogni digest presente all'interno del `Mobile Security Object` e DEVE contenere i seguenti attributi:

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Nome**
      - **Descrizione**
      - **Riferimento**
    * - **digestID**
      - *(uint)*. Valore identificativo di uno dei ``ValueDigests`` forniti nel *Mobile Security Object*.
      - [ISO 18013-5#9.1.2.5]
    * - **random**
      - *(bstr)*. Valore di byte casuale utilizzato come *salt* per la funzione di hash. Questo valore DEVE essere diverso per ogni *IssuerSignedItem* e DEVE avere una lunghezza minima di 16 byte.
      - [ISO 18013-5#9.1.2.5]
    * - **elementIdentifier**
      - *(tstr)*. Nome identificativo del dato.
      - [ISO 18013-5#8.3.2.1.2.3]
    * - **elementValue**
      - *(any)*. Valore del dato.
      - [ISO 18013-5#8.3.2.1.2.3]

Attributi
^^^^^^^^^

I seguenti **elementIdentifiers** DEVONO essere inclusi in un Attestato Elettronico codificato in mdoc-CBOR all'interno del rispettivo *nameSpace*, se non diversamente specificato:

.. list-table::
   :class: longtable
   :widths: 20 60 20
   :header-rows: 1

   * - **Element Identifier**
     - **Descrizione**
     - **Riferimento**

   * - **issuing_country**
     - *(tstr)*. Codice paese Alpha-2 come definito in [ISO 3166-1], che rappresenta il paese o territorio di emissione.
     - [ISO 18013-5#7.2]

   * - **issuing_authority**
     - *(tstr)*. Nome dell'autorità amministrativa che ha emesso l'mDL.
       Il valore deve contenere solo caratteri Latin1b e deve avere una lunghezza massima di 150 caratteri.
     - [ISO 18013-5#7.2]

   * - **sub**
     - *(uuid)*. Identifica il soggetto dell'Attestato Elettronico (l'Utente).
       L'identificativo DEVE essere opaco, NON DEVE corrispondere a nessun dato anagrafico e NON DEVE essere derivato dai dati anagrafici dell'Utente attraverso la pseudonimizzazione. Inoltre, diversi Attestati Elettronici emessi allo stesso Utente NON DEVONO riutilizzare lo stesso valore `sub`.
     -

   * - **verification**
     - *(map, OPZIONALE)*. Contiene dettagli di autenticazione e verifica dell'Utente. Ha la stessa struttura logica e scopo di quanto riportato nella :ref:`Tabella dei parametri SD-JWT <table_sd-jwt-vc_parameters>`.
     -

.. note::
  Gli attributi specifici dell'Utente dell'Attestato Elettronico sono definiti nel Catalogo degli Attestati Elettronici.
  Gli attributi specifici dell'Utente per gli Attestati Elettronici in formato mdoc come quelli del PID o mDL sono inclusi facendo riferimento agli corrispettivi `elementIdentifiers` definiti in ISO/IEC 18013-5 o nella specifica `EIDAS-ARF`_.

Mobile Security Object
^^^^^^^^^^^^^^^^^^^^^^

L'**issuerAuth** rappresenta il `Mobile Security Object` che è un `Documento COSE Sign1` definito in :rfc:`9052`. Ha la seguente struttura di dati:

   * protected header
   * unprotected header
   * payload
   * signature

Il **protected header** DEVE contenere il seguente parametro codificato in formato CBOR:

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Elemento**
      - **Descrizione**
      - **Riferimento**
    * - **1**
      - *(int)*. Algoritmo utilizzato per verificare la firma crittografica dell'Attestato Elettronico in formato mdoc.
      - :rfc:`9053`

.. note::
  Solo l'algoritmo di firma DEVE essere presente nel protected header, altri elementi NON DOVREBBERO essere presenti.

L'**unprotected header** DEVE contenere i seguenti parametri, se non diversamente specificato:

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Elemento**
      - **Descrizione**
      - **Riferimento**
    * - **4**
      - *(tstr, OPZIONALE)*. Identificativo univoco del JWK dell'Emittente. Richiesto quando l'Emittente del documento mdoc utilizza OpenID Federation.
      - :ref:`trust:L'Infrastruttura di Trust`
    * - **33**
      - *(array)*. Catena di certificati X.509 relativa all'Emittente. Obbligatorio se l'autenticazione è basata su certificato X.509.
      - :rfc:`9360`

.. note::
  `x5chain` è incluso nell'unprotected header con lo scopo di consentire al Titolare di aggiornare la catena di certificati X.509, relativa all'emittente del `Mobile Security Object`, senza invalidare la firma.

Il **payload** DEVE contenere il *MobileSecurityObject*, senza il parametro di header COSE Sign `content-type` e codificato come una *byte string* (bstr) utilizzando il *CBOR Tag* 24.

Il `MobileSecurityObject` DEVE avere i seguenti attributi, se non diversamente specificato:

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Elemento**
      - **Descrizione**
      - **Riferimento**
    * - **docType**
      - *(tstr)*. Definisce il tipo di Attestato Elettronico in formato mdoc. Ad esempio, per un mDL, il valore DEVE essere ``org.iso.18013.5.1.mDL``. Specifici `docType` POSSONO essere definiti per Attestati Elettronici diversi da mDL.
      - [ISO 18013-5#9.1.2.4]
    * - **version**
      - *(tstr)*. Versione del `MobileSecurityObject`.
      - [ISO 18013-5#9.1.2.4]
    * - **validityInfo**
      - *(map)*. Contiene le date e gli orari di emissione e scadenza del `MobileSecurityObject`. DEVE contenere i seguenti sub parametri:

          * **signed** *(tdate)*. Il timestamp che indica quando il `MobileSecurityObject` è stato firmato.
          * **validFrom** *(tdate)*. Timestamp prima del quale il `MobileSecurityObject` non è considerato valido. DEVE essere uguale o successivo a `signed`.
          * **validUntil** *(tdate)*. Timestamp dopo il quale il `MobileSecurityObject` non è più considerato valido.

      - [ISO 18013-5#9.1.2.4]
    * - **digestAlgorithm**
      - *(tstr)*. Identificativo dell'algoritmo di digest, che DEVE corrispondere all'algoritmo definito nel protected header.
      - [ISO 18013-5#9.1.2.4]
    * - **valueDigests**
      - *(map)*. Associa ogni namespace a un insieme di digest, dove ogni digest è indicizzato da un `digestID` univoco e contiene il valore del digest.
      - [ISO 18013-5#9.1.2.4]
    * - **deviceKeyInfo**
      - *(map)*. Contiene le informazioni relative alla chiave pubblica dell'Istanza del Wallet. DEVE includere i seguenti sub parametri, se non diversamente specificato:

          * **deviceKey** *(COSE_Key)*. Contiene i parametri relativi alla chiave pubblica.
          * **keyAuthorizations** *(map, OPZIONALE)*. Definisce le autorizzazioni per gli interi namespaces o per i singoli dati.
          * **keyInfo** *(map, OPZIONALE)*. Contiene metadati aggiuntivi della chiave.

      - [ISO 18013-5#9.1.2.4]
    * - **status**
      - *(map, CONDIZIONALE)*. OBBLIGATORIO solo se l'Attestato Elettronico ha durata maggiore di 24 ore (long-lived). Contiene le informazioni relative allo stato di revoca del MSO. Se presente, include una *status_list* basata sul meccanismo TOKEN-STATUS-LIST_. Questo meccanismo utilizza un array di bit per contrassegnare gli MSO revocati in base alla loro posizione di indice.
        La `status_list` DEVE contenere i seguenti sub parametri:

          * **idx**. Indice di posizione nella status list.
          * **uri**. URI che punta alla status list.
      - [ISO 18013-5#9.1.2.6]

.. note::
  La chiave privata relativa alla chiave pubblica memorizzata nel `deviceKey` viene utilizzata per firmare i `DeviceSignedItems` e per dimostrare il possesso dell'Attestato Elettronico durante la fase di presentazione (vedere la fase di presentazione con mdoc-CBOR).

Esempi mdoc-CBOR
^^^^^^^^^^^^^^^^

Un esempio non normativo di un mDL codificato in CBOR è mostrato di seguito in codifica binaria.

.. literalinclude:: ../../examples/mDL-cbor-encoded-example.txt
  :language: text

La Notazione Diagnostica del mDL codificato in CBOR è riportata di seguito.

.. literalinclude:: ../../examples/mDL-mdoc-cbor-example.txt
  :language: text

Acronimi CBOR
^^^^^^^^^^^^^

.. list-table::
   :class: longtable
   :widths: 20 80
   :header-rows: 1

   * - **Acronimo**
     - **Significato**
   * - `tstr`
     - Text String (Stringa di Testo)
   * - `bstr`
     - Byte String (Stringa di Byte)
   * - `int`
     - Signed Integer (Intero con Segno)
   * - `uint`
     - Unsigned Integer (Intero Senza Segno)
   * - `uuid`
     - Universally Unique Identifier (Identificativo Univoco Universale)
   * - `bool`
     - Boolean (Booleano) (vero/falso)
   * - `tdate`
     - Tagged Date (ad esempio, il Tag `0` è usato per indicare una stringa di data/ora in formato RFC 3339)

Mappatura dei Parametri degli Attestati Elettronici tra i vari Formati
----------------------------------------------------------------------

La seguente tabella fornisce una mappatura comparativa tra le strutture dati degli Attestati Elettronici nei formati SD-JWT-VC e mdoc-CBOR.
Essa riporta gli elementi e i parametri chiave utilizzati in ciascun formato, evidenziando sia le somiglianze che le differenze.
In particolare, evidenzia come i concetti fondamentali - come le informazioni sul Fornitore di Attestati Elettronici, la validità, l'Associazione Crittografica e le disclosure - sono rappresentati nei vari formati possibili di un Attestato Elettronico.

Per SD-JWT-VC, i parametri sono contrassegnati con `(hdr)` se si trovano nell'header JOSE e con `(pld)` se appaiono nel payload del JWT. In mdoc-CBOR, questi parametri sono identificati all'interno delle strutture issuerAuth o nameSpaces.

.. list-table::
   :class: longtable
   :widths: 20 40 40
   :header-rows: 1

   * - **Informazioni Relative A**
     - **Parametri SD-JWT-VC**
     - **Parametri mdoc-CBOR**
   * - Definizione della Tipologia di Attestato Elettronico
     - vct (pld)
     - | issuerAuth.doctype
       | issuerAuth.version
   * - Metadata della Credenziale Elettronica
     - | vctm.name (hdr)
       | vctm.description (hdr)
       | vctm.extends (hdr)
       | vctm.schema (hdr)
       | vctm.schema_uri (hdr)
       | vctm.data_source (hdr)
       | vctm.display (hdr)
       | vctm.claims (hdr)
     - | -
       | -
       | -
       | -
       | -
       | -
       | -
       | nameSpaces
   * - Emittente
     - | iss (pld)
       | issuing_authority (pld)
       | issuing_country (pld)
     - | -
       | nameSpaces.elementIdentifier.issuing_authority
       | nameSpaces.elementIdentifier.issuing_country
   * - Soggetto
     - sub (pld)
     - nameSpaces.elementIdentifier.sub
   * - Periodo di validità
     - | iat (pld)
       | exp (pld)
       | nbf (pld)
     - | issuerAuth.validityInfo.signed
       | issuerAuth.validityInfo.validUntil
       | issuerAuth.validityInfo.validFrom
   * - Meccanismo di verifica dello stato
     - | status_assertion (pld)
       | status_list (pld)
     - | -
       | issuerAuth.status_list
   * - Firma
     - | alg (hdr)
       | kid (hdr)
     - | issuerAuth.1 (alg)
       | issuerAuth.4 (kid)
   * - Trust Anchors
     - | trust_chain (OID-FED) (hdr)
       | x5c (hdr)
     - | -
       | issuerAuth.33 (x5chain)
   * - Associazione Crittografica
     - cnf.jwk (pld)
     - issuerAuth.deviceKeyInfo.deviceKey
   * - Divulgazione Selettiva
     - | _sd_alg (pld)
       | _sd (pld)
     - | issuerAuth.digestAlgorithm
       | issuerAuth.valueDigests
   * - Integrità
     - | vct#integrity (pld)
       | vctm.extends#integrity (hdr)
       | vctm.schema_uri#integrity (hdr)
     - |
       | -
       |
   * - Formato dell'Attestato Elettronico
     - typ (hdr)
     - -
   * - Verificabilità dell'Attestato Elettronico
     - verification (pld)
     - nameSpaces.elementIdentifier.verification
   * - Disclosure
     - | salt
       | claim name
       | claim value
     - |
       | nameSpaces
       |

.. note::
  - Nel formato mdoc-CBOR, la versione dell'Attestato Elettronico non è definita esplicitamente; è disponibile solo per l'IssuerAuth. Al contrario, il formato SD-JWT include informazioni sulla versione tramite l'URL `vct`.
  - `Disclosures`, `_sd` e `_sd_alg` abilitano la Divulgazione Selettiva dei claim SD-JWT. I parametri `_sd` e `_sd_alg` fanno parte del payload SD-JWT, mentre le `Disclosures` vengono inviate separatamente in un *Combined Format* insieme al SD-JWT.
  - Il parametro `vctm.claims` in SD-JWT e la struttura `nameSpaces` in mdoc-CBOR sono funzionalmente equivalenti, poiché entrambi definiscono i nomi dei claim e la loro struttura. Le `Disclosures` SD-JWT per gli attributi divulgati corrispondono esattamente ai `nameSpaces`, inclusi nomi e valori degli attributi, e i valori dei *salt*.
  - Un namespace domestico accoglie attributi come `verification` e `sub`, che non sono definiti negli elementIdentifiers standard ISO per gli Attestati Elettronici in formato mdoc-CBOR.

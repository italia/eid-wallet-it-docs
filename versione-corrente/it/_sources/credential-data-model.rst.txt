.. include:: ../common/common_definitions.rst
  

Modello di Dati delle Credenziali Elettroniche
==============================================

Il Modello di Dati delle Credenziali Elettroniche struttura le Credenziali Elettroniche per un uso sicuro e interoperabile. Gli elementi chiave includono:

    - Soggetto della Credenziale: L'individuo o l'entità che riceve la Credenziale.
    - Fornitore di Credenziale: Il Credential Issuer che emette e firma la Credenziale.
    - Metadati: Dettagli sulla Credenziale, come tipo e validità.
    - Attributi dell'Utente: Informazioni sul soggetto, come identità o qualifiche.
    - Prova: Verifica crittografica dell'autenticità e della legittima proprietà.

L'Attestato Elettronico di Dati di Identificazione Personale (PID) è rilasciato dal Fornitore di Attestati Elettronici di Dati di Identificazione Personale secondo le leggi nazionali. Lo scopo principale del PID è consentire alle persone fisiche di essere autenticate per l'accesso a un servizio o a una risorsa protetta.
Gli attributi dell'Utente forniti all'interno del PID italiano sono quelli elencati di seguito:

    - Cognome Attuale
    - Nome Attuale
    - Data di Nascita
    - Codice fiscale

Gli Attestati Elettronici di Attributi (Qualificati) ((Q)EAA) sono rilasciati dai Fornitori di Attestati Elettronici di Attributi (Qualificati) ((Q)EAA) a un'Istanza del Wallet e DEVONO essere forniti in formato dati SD-JWT-VC o mdoc-CBOR.

Il formato dei dati della Credenziale Elettronica e il meccanismo attraverso il quale una Credenziale Elettronica viene rilasciata all'Istanza del Wallet e presentata a una Relying Party sono descritti nelle sezioni seguenti.

Formato Credenziale SD-JWT-VC
-----------------------------

Il PID/(Q)EAA è rilasciato sotto forma di Credenziale Elettronica. Il formato della Credenziale Elettronica è `SD-JWT` come specificato in `SD-JWT-VC`.

SD-JWT DEVE essere firmato utilizzando la chiave privata del Fornitore di Credenziale. SD-JWT DEVE essere fornito insieme a un Metadato di Tipo relativo alla Credenziale Elettronica rilasciata secondo le Sezioni 6 e 6.3 di [`SD-JWT-VC`]. Il payload DEVE contenere il claim **_sd_alg** descritto nella Sezione 4.1.1 `SD-JWT` e altri claim specificati in questa sezione.

Il claim **_sd_alg** indica l'algoritmo di hash utilizzato dal Fornitore di Credenziale per generare i digest come descritto nella Sezione 4.1.1 di `SD-JWT`. **_sd_alg** DEVE essere impostato su uno degli algoritmi specificati nella Sezione :ref:`Cryptographic Algorithms <algorithms:Algoritmi Crittografici>`.

I claim che non sono divulgabili selettivamente DEVONO essere inclusi nel SD-JWT così come sono. I digest delle divulgazioni, insieme a eventuali esche se presenti, DEVONO essere contenuti nell'array **_sd**, come specificato nella Sezione 4.2.4.1 di `SD-JWT`.

Ogni valore di digest, calcolato utilizzando una funzione di hash sulle divulgazioni, verifica l'integrità e corrisponde a una specifica Divulgazione. Ogni divulgazione include:

  - un salt casuale,
  - il nome del claim (solo quando il claim è un elemento oggetto),
  - il valore del claim.

In caso di oggetti annidati in un payload SD-JWT, ogni claim a ogni livello del JSON dovrebbe essere contrassegnato individualmente come divulgabile selettivamente o meno. Pertanto il claim **_sd** contenente i digest PUÒ apparire più volte a diversi livelli nel SD-JWT.

Per ogni claim che è un elemento array, i digest delle rispettive divulgazioni e i digest esca vengono aggiunti all'array nella stessa posizione dei valori del claim originali come specificato nella Sezione 4.2.4.2 di `SD-JWT`.

In caso di elementi array, i valori di digest vengono calcolati utilizzando una funzione di hash sulle divulgazioni, contenenti:

  - un salt casuale,
  - l'elemento array.

In caso di più elementi array, il Fornitore di Credenziale può nascondere il valore dell'intero array o qualsiasi voce contenuta all'interno dell'array, il Titolare può divulgare sia l'intero array che qualsiasi singola voce all'interno dell'array, come definito nella Sezione 4.2.6 di `SD-JWT`.

Le Divulgazioni vengono fornite al Titolare insieme al SD-JWT nel *Formato Combinato per l'Emissione* che è una serie ordinata di valori codificati in base64url, ciascuno separato dal successivo da un singolo carattere tilde ('~') come segue:

.. code-block:: text

  <Issuer-Signed-JWT>~<Disclosure 1>~<Disclosure 2>~...~<Disclosure N>


Vedere `SD-JWT-VC` e `SD-JWT` per ulteriori dettagli.


Parametri SD-JWT della Credenziale
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

L'intestazione JOSE contiene i seguenti parametri obbligatori:

.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Claim**
    - **Descrizione**
    - **Riferimento**
  * - **typ**
    - OBBLIGATORIO. DEVE essere impostato su ``dc+sd-jwt`` come definito in `SD-JWT-VC`.
    - :rfc:`7515` Sezione 4.1.9.
  * - **alg**
    - OBBLIGATORIO. Algoritmo di firma.
    - :rfc:`7515` Sezione 4.1.1.
  * - **kid**
    - OBBLIGATORIO. Identificatore univoco della chiave pubblica.
    - :rfc:`7515` Sezione 4.1.8.
  * - **trust_chain**
    - OPZIONALE. Array JSON contenente la catena di fiducia che dimostra l'affidabilità dell'emittente del JWT.
    - [`OID-FED`] Sezione 4.3.
  * - **x5c**
    - OPZIONALE. Contiene il certificato della chiave pubblica X.509 o la catena di certificati [:rfc:`5280`] corrispondente alla chiave utilizzata per firmare digitalmente il JWT.
    - :rfc:`7515` Sezione 4.1.8 e [`SD-JWT-VC`] Sezione 3.5.
  * - **vctm**
    - OPZIONALE. Array JSON di documenti JSON di Metadati di Tipo codificati in base64url. In caso di metadati di tipo esteso, questo claim contiene l'intera catena di documenti JSON.
    - [`SD-JWT-VC`] Sezione 6.3.5.

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
      - [NSD]. OBBLIGATORIO. Stringa URL che rappresenta l'identificatore univoco del Credential Issuer.
      - `[RFC7519, Sezione 4.1.1] <https://www.iana.org/go/rfc7519>`_.
    * - **sub**
      - [NSD]. OBBLIGATORIO. L'identificatore del soggetto della Credenziale Elettronica, l'Utente, DEVE essere opaco e NON DEVE corrispondere a nessun dato anagrafico o essere derivato dai dati anagrafici dell'Utente tramite pseudonimizzazione. Inoltre, è richiesto che due diverse Credenziali emesse NON DEVONO utilizzare lo stesso valore ``sub``.
      - `[RFC7519, Sezione 4.1.2] <https://www.iana.org/go/rfc7519>`_.
    * - **iat**
      - [SD]. OBBLIGATORIO. Timestamp UNIX con l'ora di emissione del JWT, codificato come NumericDate come indicato in :rfc:`7519`.
      - `[RFC7519, Sezione 4.1.6] <https://www.iana.org/go/rfc7519>`_.
    * - **exp**
      - [NSD]. OBBLIGATORIO. Timestamp UNIX con l'ora di scadenza del JWT, codificato come NumericDate come indicato in :rfc:`7519`.
      - `[RFC7519, Sezione 4.1.4] <https://www.iana.org/go/rfc7519>`_.
    * - **nbf**
      - [NSD]. OPZIONALE. Timestamp UNIX con l'ora di inizio validità del JWT, codificato come NumericDate come indicato in :rfc:`7519`.
      - `[RFC7519, Sezione 4.1.4] <https://www.iana.org/go/rfc7519>`_.
    * - **issuing_authority**
      - [NSD]. OBBLIGATORIO. Nome dell'autorità amministrativa che ha emesso la Credenziale.
      - Regolamento di esecuzione della Commissione `EU_2024/2977`.
    * - **issuing_country**
      - [NSD]. OBBLIGATORIO. Codice paese Alpha-2, come specificato in ISO 3166-1, del paese o territorio del Credential Issuer.
      - Regolamento di esecuzione della Commissione `EU_2024/2977`.
    * - **status**
      - [NSD]. OBBLIGATORIO solo se la Credenziale Elettronica ha una lunga durata. Oggetto JSON contenente le informazioni su come leggere lo stato della Credenziale Verificabile. DEVE contenere il membro JSON *status_assertion* o *status_list*.
      - Sezione 3.2.2.2 `SD-JWT-VC` e Sezione 11 `OAUTH-STATUS-ASSERTION`.
    * - **cnf**
      - [NSD]. OBBLIGATORIO. Oggetto JSON contenente i materiali chiave di prova di possesso. Includendo un claim **cnf** (conferma) in un JWT, l'emittente del JWT dichiara che il Titolare ha il controllo della chiave privata relativa a quella pubblica definita nel parametro **cnf**. Il destinatario DEVE verificare crittograficamente che il Titolare abbia il controllo di quella chiave.
      - `[RFC7800, Sezione 3.1] <https://www.iana.org/go/rfc7800>`_ e Sezione 3.2.2.2 `SD-JWT-VC`.
    * - **vct**
      - [NSD]. OBBLIGATORIO. Il valore del tipo di Credenziale DEVE essere una stringa URL HTTPS e DEVE essere impostato utilizzando uno dei valori ottenuti dai metadati del Credential Issuer. È l'identificatore del tipo SD-JWT VC e DEVE essere impostato con un valore resistente alle collisioni come definito nella Sezione 2 di :rfc:`7515`. DEVE contenere anche il numero di versione del tipo di Credenziale (ad esempio: ``https://trust-registry.eid-wallet.example.it/credentials/v1.0/personidentificationdata``).
      - Sezione 3.2.2.2 `SD-JWT-VC`.
    * - **vct#integrity**
      - [NSD]. OBBLIGATORIO. Il valore DEVE essere una stringa "integrity metadata" come definito nella Sezione 3 di [`W3C-SRI`]. *SHA-256*, *SHA-384* e *SHA-512* DEVONO essere supportati come funzioni di hash crittografico. *MD5* e *SHA-1* NON DEVONO essere utilizzati. Questo claim DEVE essere verificato secondo la Sezione 3.3.5 di [`W3C-SRI`].
      - Sezione 6.1 `SD-JWT-VC`, [`W3C-SRI`]
    * - **verification**
      - [SD]. CONDIZIONALE. OBBLIGATORIO se il tipo di Credenziale è impostato su `PersonIdentificationData`, altrimenti è OPZIONALE. Oggetto contenente informazioni sull'autenticazione dell'Utente e sulla verifica dei dati dell'Utente. Se presente DEVE includere il seguente sotto-valore:

          * ``trust_framework``: Stringa che identifica il trust framework utilizzato per l'autenticazione dell'Utente. DEVE essere impostato utilizzando uno dei valori descritti nella mappa `trust_frameworks_supported` fornita nei Metadati del Credential Issuer.
          * ``assurance_level``: Stringa che identifica il livello di garanzia dell'identità garantito durante il processo di autenticazione dell'Utente.
          * ``evidence``: Ogni voce dell'array DEVE contenere i seguenti membri:

            - ``type``: Rappresenta il tipo di evidenza. DEVE essere impostato su ``vouch``.
            - ``time``: Timestamp UNIX con l'ora dell'autenticazione o della verifica.
            - ``attestation``: DEVE contenere i seguenti membri:

                - ``type``: DEVE essere impostato su ``digital_attestation``.
                - ``reference_number``: identificatore della risposta di autenticazione o verifica.
                - ``date_of_issuance``: data di emissione dell'attestazione.
                - ``voucher``: DEVE contenere il claim ``organization``.

      - `OIDC-IDA`.
    * - **_sd**
      - [NSD]. OBBLIGATORIO. Array di stringhe, dove ogni stringa rappresenta un digest di una Divulgazione.
      - 4.2.4.1 `SD-JWT`
    * - **_sd_alg**
      - [NSD]. OBBLIGATORIO. Algoritmo di hash utilizzato dal Fornitore di Credenziale per generare i digest.
      - 4.1.1 `SD-JWT`

Se il parametro ``status`` è impostato su ``status_list``, è un oggetto JSON contenente i seguenti sotto-parametri:

.. list-table::
   :class: longtable
   :widths: 20 60 20
   :header-rows: 1

   * - **Parametro**
     - **Descrizione**
     - **Riferimento**
   * - **idx**
     - OBBLIGATORIO. Il claim idx (indice) DEVE specificare un intero che rappresenta l'indice da controllare per le informazioni di stato nella Status List per la Credenziale Elettronica corrente. Il valore di idx DEVE essere un numero non negativo, contenente un valore di zero o superiore.
     - TOKEN-STATUS-LIST_
   * - **uri**
     - OBBLIGATORIO. Il claim uri (URI) DEVE specificare un valore String che identifica il Token della Status List contenente le informazioni di stato per la Credenziale Elettronica. Il valore di uri DEVE essere un URI conforme a [:rfc:`3986`].
     - TOKEN-STATUS-LIST_


Se il parametro ``status`` è impostato su ``status_assertation``, è un oggetto JSON contenente il claim *credential_hash_alg* che indica l'algoritmo utilizzato per l'hashing della Credenziale Elettronica a cui è associato lo Status Assertion. Si RACCOMANDA di utilizzare *sha-256*.


.. note::
  Il documento JSON di Metadati del Tipo di Credenziale PUÒ essere recuperato direttamente dall'URL contenuto nel claim **vct**, utilizzando il metodo HTTP GET o utilizzando il parametro di intestazione vctm se fornito. A differenza di quanto specificato nella Sezione 6.3.1 di `SD-JWT-VC` l'endpoint **.well-known** non è incluso nel profilo di implementazione corrente. Gli implementatori possono decidere di utilizzarlo per l'interoperabilità con altri sistemi.


Tipo di Metadati della Credenziale Elettronica
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Il documento del tipo di Metadati DEVE essere un oggetto JSON e contiene i seguenti parametri.

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Descrizione**
      - **Riferimento**
    * - **name**
      - OBBLIGATORIO. Nome leggibile del tipo di Credenziale Elettronica. In caso di più lingue, i tag di lingua vengono aggiunti al nome del membro, delimitati con il carattere ``#`` come definito in :rfc:`5646` (ad es. *name#it-IT*).
      - [`SD-JWT-VC`] Sezione 6.2 e [`OIDC`] Sezione 5.2.
    * - **description**
      - OBBLIGATORIO. Una descrizione leggibile del tipo di Credenziale Elettronica. In caso di più lingue, i tag di lingua vengono aggiunti al nome del membro, delimitati da un carattere # come definito in :rfc:`5646`.
      - [`SD-JWT-VC`] Sezione 6.2 e [`OIDC`] Sezione 5.2.
    * - **extends**
      - OPZIONALE. Identificatore di stringa di un documento di tipo metadati esteso.
      - [`SD-JWT-VC`] Sezione 6.2.
    * - **extends#integrity**
      - CONDIZIONALE. OBBLIGATORIO se **extends** è presente.
      - [`SD-JWT-VC`] Sezione 6.2.
    * - **schema**
      - CONDIZIONALE. OBBLIGATORIO se **schema_uri** non è presente.
      - [`SD-JWT-VC`] Sezione 6.2.
    * - **schema_uri**
      - CONDIZIONALE. OBBLIGATORIO se **schema** non è presente.
      - [`SD-JWT-VC`] Sezione 6.2.
    * - **schema_uri#integrity**
      - CONDIZIONALE. OBBLIGATORIO se **schema_uri** è presente.
      - [`SD-JWT-VC`] Sezione 6.2.
    * - **data_source**
      - OBBLIGATORIO. Oggetto contenente informazioni sull'origine dei dati. DEVE contenere l'oggetto ``verification`` con il seguente sotto-valore:

          * ``trust_framework``: DEVE contenere il trust framework utilizzato per l'autenticazione digitale verso il sistema della Fonte Autentica.
          * ``authentic_source``: DEVE contenere i seguenti claim relativi alle informazioni sulla Fonte Autentica:

               * ``organization_name`` nome della Fonte Autentica.
               * ``organization_code`` codice identificativo della Fonte Autentica.
               * ``homepage_uri`` uri che punta alla homepage della Fonte Autentica.
               * ``contacts`` elenco dei contatti per informazioni e assistenza.
               * ``logo_uri`` URI che punta all'immagine del logo.

      - Questa specifica
    * - **display**
      - OBBLIGATORIO. Array di oggetti, uno per ogni lingua supportata, contenente informazioni di visualizzazione per il tipo di Credenziale Elettronica. Contiene per ogni oggetto le seguenti proprietà:

          * ``lang``: tag di lingua come definito in :rfc:`5646` Sezione 2. [OBBLIGATORIO].
          * ``name``: etichetta leggibile per il tipo di Credenziale Elettronica. [OBBLIGATORIO].
          * ``description``: descrizione leggibile per il tipo di Credenziale Elettronica. [OBBLIGATORIO].
          * ``rendering``: oggetto contenente i metodi di rendering supportati dal tipo di Credenziale Elettronica. [OBBLIGATORIO]. Il metodo di rendering `svg_template` DEVE essere supportato.
            
            L'array ``svg_templates`` di oggetti contiene per ogni modello SVG supportato le seguenti proprietà:

                * ``uri``: URI che punta al modello SVG. [OBBLIGATORIO].
                * ``uri#integrity``: metadati di integrità come definito nella Sezione 3 di `W3C-SRI`. [OBBLIGATORIO].
                * ``properties``: oggetto contenente le proprietà del modello SVG. Questa proprietà è OBBLIGATORIA se è presente più di un modello SVG. L'oggetto DEVE contenere almeno una delle proprietà definite in `SD-JWT-VC` Sezione 8.1.2.1.

            Se è supportato anche il metodo di rendering `simple`, l'oggetto ``simple`` contiene le seguenti proprietà:

                * ``logo``: oggetto contenente informazioni sul logo da visualizzare. Questa proprietà è OBBLIGATORIA. L'oggetto contiene i seguenti sotto-valori:

                    * ``uri``: URI che punta all'immagine del logo. [OBBLIGATORIO]
                    * ``uri#integrity``: metadati di integrità come definito nella Sezione 3 di `W3C-SRI`. [OBBLIGATORIO].
                    * ``alt_text``: Una stringa contenente testo alternativo da visualizzare al posto dell'immagine del logo. [OPZIONALE].

                * ``background_color``: valore di colore RGB come definito in `W3C.CSS-COLOR` per lo sfondo della Credenziale Elettronica. [OPZIONALE].
                * ``text_color``: valore di colore RGB come definito in `W3C.CSS-COLOR` per il testo della Credenziale Elettronica. [OPZIONALE].

          .. note::
            L'uso del modello SVG è RACCOMANDATO per tutte le applicazioni che lo supportano.

      - [`SD-JWT-VC`] Sezione 8.
    * - **claims**
      - OBBLIGATORIO. Array di oggetti contenenti informazioni per la visualizzazione e la convalida dei claim della Credenziale Elettronica. Contiene per ogni claim della Credenziale le seguenti proprietà:

          * ``path``: array che indica il claim o i claim che vengono indirizzati. [OBBLIGATORIO].
          * ``display``: array contenente informazioni di visualizzazione sul claim indicato nel ``path``. L'array contiene un oggetto per ogni lingua supportata dal tipo di Credenziale Elettronica. Questa proprietà è OBBLIGATORIA. Contiene i seguenti membri:
             * ``lang``: tag di lingua come definito in :rfc:`5646` Sezione 2. [OBBLIGATORIO].
             * ``label``: etichetta leggibile per il claim. [OBBLIGATORIO].
             * ``description``: descrizione leggibile per il claim. [OBBLIGATORIO].
          * ``sd``: stringa che indica se il claim è divulgabile selettivamente. DEVE essere impostato su `always` se il claim è divulgabile selettivamente o `never` se non lo è. [OBBLIGATORIO].
          * ``svg_id``: stringa alfanumerica contenente l'ID del claim referenziato nel modello SVG come definito in [`SD-JWT-VC`] Sezione 9. [OBBLIGATORIO].
      - [`SD-JWT-VC`] Sezione 9.


Un tipo di metadati di Credenziale Elettronica non normativo è fornito di seguito.

.. literalinclude:: ../../examples/vc-metadata-type.json
  :language: JSON

Attributi dell'Utente PID
^^^^^^^^^^^^^^^^^^^^^^^^^

A seconda del tipo di Credenziale Elettronica **vct**, possono essere aggiunti dati di claim aggiuntivi. Il PID supporta i seguenti dati:

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Descrizione**
      - **Riferimento**
    * - **given_name**
      - [SD]. OBBLIGATORIO. Nome Attuale. (*String*)
      - Sezione 5.1 di `OIDC` e Regolamento di esecuzione della Commissione `EU_2024/2977`
    * - **family_name**
      - [SD]. OBBLIGATORIO. Cognome Attuale. (*String*)
      - Sezione 5.1 di `OIDC` e Regolamento di esecuzione della Commissione `EU_2024/2977`
    * - **birth_date**
      - [SD]. OBBLIGATORIO. Data di Nascita. (*String, formato [ISO8601‑1] YYYY-MM-DD*)
      - Regolamento di esecuzione della Commissione `EU_2024/2977`
    * - **birth_place**
      - [SD]. OBBLIGATORIO. Luogo di Nascita. (*String*)
      - Regolamento di esecuzione della Commissione `EU_2024/2977`
    * - **nationalities**
      - [SD]. OBBLIGATORIO. Uno o più codici paese alpha-2 come specificato in ISO 3166-1. (*Array di stringhe*)
      - Regolamento di esecuzione della Commissione `EU_2024/2977`
    * - **personal_administrative_number**
      - [SD]. CONDIZIONALE. OBBLIGATORIO se ``tax_id_code`` non è presente. Identificatore univoco nazionale di una persona fisica generato da ANPR in formato stringa. (*String*)
      - Regolamento di esecuzione della Commissione `EU_2024/2977`
    * - **tax_id_code**
      - [SD]. CONDIZIONALE. OBBLIGATORIO se ``personal_administrative_number`` non è presente. Codice di identificazione fiscale nazionale della persona fisica in formato String. DEVE essere impostato secondo ETSI EN 319 412-1. Ad esempio ``TINIT-<ItalianTaxIdentificationNumber>``. (*String*)
      -


Esempi Non Normativi PID
^^^^^^^^^^^^^^^^^^^^^^^^

Di seguito, l'esempio non normativo del payload di un PID rappresentato in formato JSON.

.. literalinclude:: ../../examples/pid-json-example-payload.json
  :language: JSON

La versione SD-JWT corrispondente per PID è data da

.. literalinclude:: ../../examples/pid-sd-jwt-example-header.json
  :language: JSON

.. literalinclude:: ../../examples/pid-sd-jwt-example-payload.json
  :language: JSON

L'elenco delle divulgazioni è presentato di seguito.

**Claim** ``iat``:

- Hash SHA-256: ``Yrc-s-WSr4exEYtqDEsmRl7spoVfmBxixP12e4syqNE``
- Divulgazione:
   ``WyIyR0xDNDJzS1F2ZUNmR2ZyeU5STjl3IiwgImlhdCIsIDE2ODMwMDAwMDBd``
- Contenuti: ``["2GLC42sKQveCfGfryNRN9w", "iat", 1683000000]``

**Claim** ``verification``:

- Hash SHA-256: ``h7Egl5H9gTPC_FCU845aadvsC--dTjy9Nrstxh-caRo``
- Divulgazione:
   ``WyJlbHVWNU9nM2dTTklJOEVZbnN4QV9BIiwgInZlcmlmaWNhdGlvbiIsIHsi``
   ``dHJ1c3RfZnJhbWV3b3JrIjogIml0X2NpZSIsICJhc3N1cmFuY2VfbGV2ZWwi``
   ``OiAiaGlnaCIsICJldmlkZW5jZSI6IHsidHlwZSI6ICJ2b3VjaCIsICJ0aW1l``
   ``IjogIjIwMjAtMDMtMTlUMTI6NDJaIiwgImF0dGVzdGF0aW9uIjogeyJ0eXBl``
   ``IjogImRpZ2l0YWxfYXR0ZXN0YXRpb24iLCAicmVmZXJlbmNlX251bWJlciI6``
   ``ICI2NDg1LTE2MTktMzk3Ni02NjcxIiwgImRhdGVfb2ZfaXNzdWFuY2UiOiAi``
   ``MjAyMC0wMy0xOVQxMjo0M1oiLCAidm91Y2hlciI6IHsib3JnYW5pemF0aW9u``
   ``IjogIk1pbmlzdGVybyBkZWxsJ0ludGVybm8ifX19fV0``
- Contenuti: ``["eluV5Og3gSNII8EYnsxA_A", "verification",``
   ``{"trust_framework": "it_cie", "assurance_level": "high", "evidence": {"type": "vouch",``
   ``"time": "2020-03-19T12:42Z", "attestation": {"type":``
   ``"digital_attestation", "reference_number":``
   ``"6485-1619-3976-6671", "date_of_issuance":``
   ``"2020-03-19T12:43Z", "voucher": {"organization": "Ministero``
   ``dell'Interno"}}}}]``

**Claim** ``given_name``:

- Hash SHA-256: ``zVdghcmClMVWlUgGsGpSkCPkEHZ4u9oWj1SlIBlCc1o``
- Divulgazione:
   ``WyI2SWo3dE0tYTVpVlBHYm9TNXRtdlZBIiwgImdpdmVuX25hbWUiLCAiTWFy``
   ``aW8iXQ``
- Contenuti: ``["6Ij7tM-a5iVPGboS5tmvVA", "given_name", "Mario"]``

**Claim** ``family_name``:

- Hash SHA-256: ``VQI-S1mT1Kxfq2o8J9io7xMMX2MIxaG9M9PeJVqrMcA``
- Divulgazione:
   ``WyJlSThaV205UW5LUHBOUGVOZW5IZGhRIiwgImZhbWlseV9uYW1lIiwgIlJv``
   ``c3NpIl0``
- Contenuti: ``["eI8ZWm9QnKPpNPeNenHdhQ", "family_name", "Rossi"]``

**Claim** ``birth_date``:

- Hash SHA-256: ``s1XK5f2pM3-aFTauXhmvd9pyQTJ6FMUhc-JXfHrxhLk``
- Divulgazione:
   ``WyJRZ19PNjR6cUF4ZTQxMmExMDhpcm9BIiwgImJpcnRoX2RhdGUiLCAiMTk4``
   ``MC0wMS0xMCJd``
- Contenuti: ``["Qg_O64zqAxe412a108iroA", "birth_date", "1980-01-10"]``

**Claim** ``birth_place``:

- Hash SHA-256: ``tSL-e1nLdWOU9sFMTCUu5P1tCzxA-TW-VWbHGzYtU7E``
- Divulgazione:
  ``WyJBSngtMDk1VlBycFR0TjRRTU9xUk9BIiwgImJpcnRoX3BsYWNlIiwgIlJv``
  ``bWEiXQ``
- Contenuti: ``["AJx-095VPrpTtN4QMOqROA", "birth_place", "Roma"]``

**Claim** ``personal_administrative_number``:

- Hash SHA-256: ``6WLNc09rBr-PwEtnWzxGKdzImjrpDxbr4qoIx838a88``
- Divulgazione:
   ``WyJHMDJOU3JRZmpGWFE3SW8wOXN5YWpBIiwgInBlcnNvbmFsX2FkbWluaXN0``
   ``cmF0aXZlX251bWJlciIsICJYWDAwMDAwWFgiXQ``
- Contenuti: ``["G02NSrQfjFXQ7Io09syajA", "personal_administrative_number",``
   ``"XX00000XX"]``

**Claim** ``tax_id_code``:

- Hash SHA-256: ``LqrtU2rlA51U97cMiYhqwa-is685bYiOJImp8a5KGNA``
- Divulgazione:
   ``WyJsa2x4RjVqTVlsR1RQVW92TU5JdkNBIiwgInRheF9pZF9jb2RlIiwgIlRJ``
   ``TklULVhYWFhYWFhYWFhYWFhYWFgiXQ``
- Contenuti: ``["lklxF5jMYlGTPUovMNIvCA", "tax_id_code",``
   ``"TINIT-XXXXXXXXXXXXXXXX"]``

**Voce Array** di ``nationalities``:

- Hash SHA-256: ``yKeP1CWTQK8Sd9BeNvFhkLXgEu/1G3QQz4CWSlqEOFw``
- Divulgazione: ``WyJQYzMzSk0yTGNoY1VfbEhnZ3ZfdWZRIiwgIklUIl0``
- Contenuti: ``["Pc33JM2LchcU_lHggv_ufQ", "IT"]``

Il formato combinato per l'emissione del PID è dato da:

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

Esempi Non Normativi (Q)EAA
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Di seguito è riportato un esempio non normativo di (Q)EAA in JSON.

.. literalinclude:: ../../examples/qeaa-json-example-payload.json
  :language: JSON

Il corrispondente SD-JWT per i dati precedenti è rappresentato come segue, come JSON decodificato sia per l'intestazione che per il payload.

.. literalinclude:: ../../examples/qeaa-sd-jwt-example-header.json
  :language: JSON

.. literalinclude:: ../../examples/qeaa-sd-jwt-example-payload.json
  :language: JSON

Di seguito è riportato l'elenco delle divulgazioni:

**Claim** ``iat``:

- Hash SHA-256: ``Yrc-s-WSr4exEYtqDEsmRl7spoVfmBxixP12e4syqNE``
- Divulgazione:
   ``WyIyR0xDNDJzS1F2ZUNmR2ZyeU5STjl3IiwgImlhdCIsIDE2ODMwMDAwMDBd``
- Contenuti: ``["2GLC42sKQveCfGfryNRN9w", "iat", 1683000000]``

**Claim** ``document_number``:

- Hash SHA-256: ``Dx-6hjvrcxNzF0slU6ukNmzHoL-YvBN-tFa0T8X-bY0``
- Divulgazione:
   ``WyJlbHVWNU9nM2dTTklJOEVZbnN4QV9BIiwgImRvY3VtZW50X251bWJlciIs``
   ``ICJYWFhYWFhYWFhYIl0``
- Contenuti:
   ``["eluV5Og3gSNII8EYnsxA_A", "document_number", "XXXXXXXXXX"]``

**Claim** ``given_name``:

- Hash SHA-256: ``zVdghcmClMVWlUgGsGpSkCPkEHZ4u9oWj1SlIBlCc1o``
- Divulgazione:
   ``WyI2SWo3dE0tYTVpVlBHYm9TNXRtdlZBIiwgImdpdmVuX25hbWUiLCAiTWFy``
   ``aW8iXQ``
- Contenuti: ``["6Ij7tM-a5iVPGboS5tmvVA", "given_name", "Mario"]``

**Claim** ``family_name``:

- Hash SHA-256: ``VQI-S1mT1Kxfq2o8J9io7xMMX2MIxaG9M9PeJVqrMcA``
- Divulgazione:
   ``WyJlSThaV205UW5LUHBOUGVOZW5IZGhRIiwgImZhbWlseV9uYW1lIiwgIlJv``
   ``c3NpIl0``
- Contenuti: ``["eI8ZWm9QnKPpNPeNenHdhQ", "family_name", "Rossi"]``

**Claim** ``birth_date``:

- Hash SHA-256: ``s1XK5f2pM3-aFTauXhmvd9pyQTJ6FMUhc-JXfHrxhLk``
- Divulgazione:
   ``WyJRZ19PNjR6cUF4ZTQxMmExMDhpcm9BIiwgImJpcnRoX2RhdGUiLCAiMTk4``
   ``MC0wMS0xMCJd``
- Contenuti: ``["Qg_O64zqAxe412a108iroA", "birth_date", "1980-01-10"]``

**Claim** ``expiry_date``:

- Hash SHA-256: ``aBVdfcnxT0Z5RrwdxZSUhuUxz3gM2vcEZLeYIj61Kas``
- Divulgazione:
   ``WyJBSngtMDk1VlBycFR0TjRRTU9xUk9BIiwgImV4cGlyeV9kYXRlIiwgIjIw``
   ``MjQtMDEtMDEiXQ``
- Contenuti: ``["AJx-095VPrpTtN4QMOqROA", "expiry_date", "2024-01-01"]``

**Claim** ``personal_administrative_number``:

- Hash SHA-256: ``o1cHG8JbEEYv0HeJINYKbFLd-TnEDUuNzI1XpzV32aU``
- Divulgazione:
   ``WyJQYzMzSk0yTGNoY1VfbEhnZ3ZfdWZRIiwgInBlcnNvbmFsX2FkbWluaXN0``
   ``cmF0aXZlX251bWJlciIsICJYWDAwMDAwWFgiXQ``
- Contenuti: ``["Pc33JM2LchcU_lHggv_ufQ", "personal_administrative_number",``
   ``"XX00000XX"]``

**Claim** ``constant_attendance_allowance``:

- Hash SHA-256: ``GE3Sjy_zAT34f8wa5DUkVB0FslaSJRAAc8I3lN11Ffc``
- Divulgazione:
   ``WyJHMDJOU3JRZmpGWFE3SW8wOXN5YWpBIiwgImNvbnN0YW50X2F0dGVuZGFu``
   ``Y2VfYWxsb3dhbmNlIiwgdHJ1ZV0``
- Contenuti:
   ``["G02NSrQfjFXQ7Io09syajA", "constant_attendance_allowance",``
   ``true]``


Il formato combinato per l'emissione del (Q)EAA è rappresentato di seguito:

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

Formato Credenziale mdoc-CBOR
-----------------------------

Il modello di dati mdoc si basa sullo standard ISO/IEC 18013-5.
Gli elementi dati mdoc DEVONO essere codificati in CBOR come definito in :rfc:`8949`.

Questo modello di dati struttura le Credenziali Elettroniche mdoc in componenti distinti: spazi dei nomi (**nameSpaces**) e prova crittografica (**issuerAuth**).
Gli spazi dei nomi categorizzano e strutturano gli elementi di dati (o attributi, vedi :ref:`credential-data-model:Attribute Namespaces`). Mentre la prova crittografica garantisce integrità e autenticità attraverso il Mobile Security Object (MSO).

L'MSO memorizza in modo sicuro i digest crittografici degli attributi all'interno dei `nameSpaces`. Ciò consente alle Relying Party di convalidare gli attributi divulgati rispetto ai valori **digestID** corrispondenti senza rivelare l'intera Credenziale.
Vedere :ref:`credential-data-model:Mobile Security Object` per i dettagli.

Una Credenziale Elettronica mdoc-CBOR DEVE essere conforme alla seguente struttura:

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Parametro**
      - **Descrizione**
      - **Riferimento**
    * - **nameSpaces**
      - *(map)*. Gli spazi dei nomi all'interno dei quali sono definiti gli elementi di dati. Una Credenziale Elettronica PUÒ includere più spazi dei nomi. Gli attributi mDL obbligatori utilizzano lo spazio dei nomi standard `org.iso.18013.5.1`. Tuttavia, PUÒ avere uno spazio dei nomi nazionale, come `org.iso.18013.5.1.IT`, per includere attributi aggiuntivi definiti in questo profilo di implementazione. Ogni spazio dei nomi all'interno di `nameSpaces` DEVE condividere lo stesso valore del tipo di documento emesso (`docType`), che identifica la natura della Credenziale Elettronica, come definito in `issuerAuth`.
      - [ISO 18013-5#8.3.2.1.2]
    * - **issuerAuth**
      - *(COSE_Sign1)*. Contiene *Mobile Security Object* (MSO), un documento COSE Sign1, emesso dal Credential Issuer.
      - [ISO 18013-5#9.1.2.4]

La struttura di una Credenziale mdoc-CBOR è ulteriormente elaborata nelle sezioni seguenti.

Attribute Namespaces
^^^^^^^^^^^^^^^^^^^^

Il **nameSpaces** contiene una o più voci *nameSpace*, ciascuna identificata da un nome. All'interno di ogni **nameSpace**, include uno o più *IssuerSignedItemBytes*, ciascuno codificato come una stringa di byte CBOR con Tag 24 (#6.24(bstr .cbor)), che appare come 24(<<... >>) in notazione diagnostica. Rappresenta le informazioni di divulgazione per ogni digest all'interno del `Mobile Security Object` e DEVE contenere i seguenti attributi:

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Nome**
      - **Descrizione**
      - **Riferimento**
    * - **digestID**
      - *(uint)*. Valore di riferimento a uno dei ``ValueDigests`` forniti nel *Mobile Security Object*.
      - [ISO 18013-5#9.1.2.5]
    * - **random**
      - *(bstr)*. Valore di byte casuale utilizzato come sale per la funzione di hash. Questo valore DEVE essere diverso per ogni *IssuerSignedItem* e DEVE avere una lunghezza minima di 16 byte.
      - [ISO 18013-5#9.1.2.5]
    * - **elementIdentifier**
      - *(tstr)*. Identificatore dell'elemento di dati.
      - [ISO 18013-5#8.3.2.1.2.3]
    * - **elementValue**
      - *(any)*. Valore dell'elemento di dati.
      - [ISO 18013-5#8.3.2.1.2.3]

Attributi
^^^^^^^^^

I seguenti **elementIdentifiers** DEVONO essere inclusi in una Credenziale Elettronica codificata in mdoc-CBOR all'interno del rispettivo *nameSpace*, se non diversamente specificato:

.. list-table::
   :class: longtable
   :widths: 20 60 20
   :header-rows: 1

   * - **Identificatore Elemento**
     - **Descrizione**
     - **Riferimento**

   * - **issuing_country**
     - *(tstr)*. Codice paese Alpha-2 come definito in [ISO 3166-1], che rappresenta il paese o territorio di emissione.
     - [ISO 18013-5#7.2]

   * - **issuing_authority**
     - *(tstr)*. Nome dell'autorità amministrativa che ha emesso l'mDL.
       Il valore deve utilizzare solo caratteri Latin1b e deve avere una lunghezza massima di 150 caratteri.
     - [ISO 18013-5#7.2]

   * - **sub**
     - *(uuid)*. Identifica il soggetto della Credenziale Elettronica mdoc (l'Utente).
       L'identificatore DEVE essere opaco, NON DEVE corrispondere a nessun dato anagrafico e NON DEVE essere derivato dai dati anagrafici dell'Utente attraverso la pseudonimizzazione. Inoltre, diverse Credenziali emesse allo stesso Utente NON DEVONO riutilizzare lo stesso valore `sub`.
     -

   * - **verification**
     - *(map, OPZIONALE)*. Contiene dettagli di autenticazione e verifica dell'Utente. Ha la stessa struttura logica e scopo di quanto riportato nella :ref:`Tabella dei parametri SD-JWT <table_sd-jwt-vc_parameters>`.
     -

.. note::
  Gli attributi specifici dell'Utente della Credenziale Elettronica sono definiti nel Catalogo degli Attestati Elettronici.
  Gli attributi specifici dell'Utente per le Credenziali Elettroniche mdoc come quelli utilizzati in mDL o PID sono inclusi anche facendo riferimento agli appropriati `elementIdentifiers` definiti in ISO/IEC 18013-5 o nella specifica `EIDAS-ARF`.

Mobile Security Object
^^^^^^^^^^^^^^^^^^^^^^

L'**issuerAuth** rappresenta il `Mobile Security Object` che è un `Documento COSE Sign1` definito in :rfc:`9052`. Ha la seguente struttura di dati:

   * intestazione protetta
   * intestazione non protetta
   * payload
   * firma.

L'**intestazione protetta** DEVE contenere il seguente parametro codificato in formato CBOR:

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Elemento**
      - **Descrizione**
      - **Riferimento**
    * - **1**
      - *(int)*. Algoritmo utilizzato per verificare la firma crittografica della Credenziale Elettronica mdoc.
      - :rfc:`9053`

.. note::
  Solo l'algoritmo di firma DEVE essere presente nell'intestazione protetta, altri elementi NON DOVREBBERO essere presenti nell'intestazione protetta.

L'**intestazione non protetta** DEVE contenere i seguenti parametri, se non diversamente specificato:

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Elemento**
      - **Descrizione**
      - **Riferimento**
    * - **4**
      - *(tstr, OPZIONALE)*. Identificatore univoco del JWK dell'Emittente. Richiesto quando l'Emittente di mdoc utilizza OpenID Federation.
      - :ref:`trust:L'Infrastruttura di Trust`
    * - **33**
      - *(array)*. Catena di certificati X.509 sull'Emittente. Richiesto per l'autenticazione basata su certificato X.509.
      - :rfc:`9360`

.. note::
  L'`x5chain` è incluso nell'intestazione non protetta con lo scopo di consentire al Titolare di aggiornare la catena di certificati X.509, relativa all'emittente del `Mobile Security Object`, senza invalidare la firma.

Il **payload** DEVE contenere il *MobileSecurityObject*, senza il parametro di intestazione COSE Sign `content-type` e codificato come una *stringa di byte* (bstr) utilizzando il *CBOR Tag* 24.

Il `MobileSecurityObject` DEVE avere i seguenti attributi, se non diversamente specificato:

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Elemento**
      - **Descrizione**
      - **Riferimento**
    * - **docType**
      - *(tstr)*. Definisce il tipo di Credenziale Elettronica mdoc che viene emessa. Ad esempio, per un mDL, il valore DEVE essere ``org.iso.18013.5.1.mDL``. Specifici `docType` POSSONO essere definiti per Credenziali Elettroniche diverse da mDL.
      - [ISO 18013-5#9.1.2.4]
    * - **version**
      - *(tstr)*. Versione del `MobileSecurityObject`.
      - [ISO 18013-5#9.1.2.4]
    * - **validityInfo**
      - *(map)*. Contiene i datetime di emissione e scadenza del `MobileSecurityObject`. DEVE contenere il seguente sotto-valore:

          * **signed** *(tdate)*. Il timestamp che indica quando il `MobileSecurityObject` è stato firmato.
          * **validFrom** *(tdate)*. Timestamp prima del quale il `MobileSecurityObject` non è considerato valido. DEVE essere uguale o successivo al tempo `signed`.
          * **validUntil** *(tdate)*. Timestamp dopo il quale il `MobileSecurityObject` non è più considerato valido.

      - [ISO 18013-5#9.1.2.4]
    * - **digestAlgorithm**
      - *(tstr)*. Identificatore dell'algoritmo di digest, che DEVE corrispondere all'algoritmo definito nell'intestazione protetta.
      - [ISO 18013-5#9.1.2.4]
    * - **valueDigests**
      - *(map)*. Mappa ogni identificatore di spazio dei nomi a un insieme di digest, dove ogni digest è indicizzato da un `digestID` univoco e contiene il valore del digest.
      - [ISO 18013-5#9.1.2.4]
    * - **deviceKeyInfo**
      - *(map)*. Contiene metadati sulla chiave pubblica dell'Istanza del Wallet. DEVE includere i seguenti sotto-campi, se non diversamente specificato:

          * **deviceKey** *(COSE_Key)*. Contiene i parametri della chiave pubblica.
          * **keyAuthorizations** *(map, OPZIONALE)*. Definisce le autorizzazioni per spazi dei nomi completi o singoli elementi di dati.
          * **keyInfo** *(map, OPZIONALE)*. Contiene metadati aggiuntivi sulla chiave.

      - [ISO 18013-5#9.1.2.4]
    * - **status**
      - *(map, CONDIZIONALE)*. OBBLIGATORIO solo se la Credenziale Elettronica ha una lunga durata. Contiene le informazioni di revoca MSO. Se presente, include una *status_list* basata sul meccanismo TOKEN-STATUS-LIST_. Questo meccanismo utilizza un array di bit per contrassegnare gli MSO revocati in base alla loro posizione di indice.
        La `status_list` DEVE contenere il seguente sotto-valore:

          * **idx**. Indice di posizione nella lista di stato.
          * **uri**. URI che punta alla risorsa della lista di stato.
      - [ISO 18013-5#9.1.2.6]

.. note::
  La chiave privata relativa alla chiave pubblica memorizzata nella mappa `deviceKey` viene utilizzata per firmare gli `DeviceSignedItems` e per dimostrare il possesso della Credenziale Elettronica durante la fase di presentazione (vedere la fase di presentazione con mdoc-CBOR).

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
     - Stringa di Testo
   * - `bstr`
     - Stringa di Byte
   * - `int`
     - Intero con Segno
   * - `uint`
     - Intero Senza Segno
   * - `uuid`
     - Identificatore Univoco Universale
   * - `bool`
     - Booleano (vero/falso)
   * - `tdate`
     - Data Taggata (ad esempio, il Tag `0` è usato per indicare una stringa di data/ora in formato RFC 3339)

Mappatura dei Parametri delle Credenziali tra Formati
-----------------------------------------------------

La seguente tabella fornisce una mappatura comparativa tra le strutture di dati delle Credenziali Elettroniche SD-JWT-VC e mdoc-CBOR.
Delinea gli elementi e i parametri di dati chiave utilizzati in ciascun formato, evidenziando sia le somiglianze che le differenze.
In particolare, mostra come i concetti fondamentali - come le informazioni sul Credential Issuer, la validità, l'Associazione Crittografica e le divulgazioni - sono rappresentati in questi formati di Credenziale.

Per SD-JWT-VC, i parametri sono contrassegnati con `(hdr)` se si trovano nell'intestazione JOSE e con `(pld)` se appaiono nel payload del JWT. In mdoc-CBOR, questi parametri sono identificati all'interno delle strutture issuerAuth o nameSpaces.

.. list-table::
   :class: longtable
   :widths: 20 40 40
   :header-rows: 1

   * - **Informazioni Relative A**
     - **Parametri SD-JWT-VC**
     - **Parametri mdoc-CBOR**
   * - Definizione della Credenziale Elettronica
     - vct (pld)
     - | issuerAuth.doctype
       | issuerAuth.version
   * - Metadati della Credenziale Elettronica
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
   * - Fornitore di Credenziale
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
   * - Meccanismo di stato
     - | status_assertation (pld)
       | status_list (pld)
     - | -
       | issuerAuth.status_list
   * - Firma
     - | alg (hdr)
       | kid (hdr)
     - | issuerAuth.1 (alg)
       | issuerAuth.4 (kid)
   * - Ancore di fiducia
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
   * - Formato della Credenziale Elettronica
     - typ (hdr)
     - -
   * - Verificabilità della Credenziale Elettronica
     - verification (pld)
     - nameSpaces.elementIdentifier.verification
   * - Divulgazioni
     - | salt
       | claim name
       | claim value
     - |
       | nameSpaces
       |

.. note::
  - Nel formato mdoc-CBOR, la versione della Credenziale Elettronica non è definita esplicitamente; è disponibile solo per l'IssuerAuth. Al contrario, il formato SD-JWT include informazioni sulla versione tramite l'URL `vct`.
  - `Disclosures`, `_sd` e `_sd_alg` abilitano la Divulgazione Selettiva dei claim SD-JWT. I parametri `_sd` e `_sd_alg` fanno parte del payload SD-JWT, mentre le `Disclosures` vengono inviate separatamente in un Formato Combinato insieme al SD-JWT.
  - Il parametro `vctm.claims` in SD-JWT e la struttura `nameSpaces` in mdoc-CBOR sono funzionalmente equivalenti, poiché entrambi definiscono i nomi dei claim e la loro struttura. Le `Disclosures` SD-JWT per gli attributi divulgati corrispondono direttamente a `nameSpaces`, inclusi nomi di attributi, valori e valori di sale.
  - Uno spazio dei nomi nazionale accoglie attributi come `verification` e `sub`, che non sono definiti negli elementIdentifiers standard ISO per le Credenziali Elettroniche mdoc-CBOR.

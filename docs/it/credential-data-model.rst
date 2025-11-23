.. include:: ../common/common_definitions.rst
  

Modello di Dati degli Attestati Elettronici
==============================================

Un modello di dati dell'Attestato Elettronico ha la seguente struttura:

- **Attributi di metadati**:
  - **Format-Agnostic**: Sono attributi di metadati di alto livello che descrivono l'Attestato Elettronico indipendentemente dal suo formato di codifica. Rappresentano le informazioni semantiche sulla credenziale (ad esempio, credential_type, issuing_authority, expiry_date) e rimangono concettualmente coerenti tra i diversi formati. Quando una credenziale viene codificata, questi attributi di metadati comuni vengono mappati a parametri tecnici specifici del formato secondo le regole di codifica di ciascun formato (SD-JWT-VC o mdoc-CBOR).
  - **Format-Specific**: Sono parametri di metadati intrinseci al formato di codifica specifico e servono a scopi tecnici relativi al modello di sicurezza e ai requisiti di protocollo del formato.
- **Attributi dell'Utente**: Informazioni sull'Utente, come identità o qualifiche.

L'Attestato Elettronico di Dati di Identificazione Personale (PID) è rilasciato dal Fornitore di Attestati Elettronici di Dati di Identificazione Personale secondo le leggi nazionali e DEVE essere fornito in formato SD-JWT-VC e mdoc-CBOR. Lo scopo principale del PID è consentire alle persone fisiche di essere autenticate per accedere a un servizio o a una risorsa protetta.
Il PID DEVE essere fornito secondo i requisiti del modello dati definiti in `EU_2024/2977`_ e **Sezione 2 dell'ARF PID Rulebook v1.3** [`EIDAS-ARF`_], gli attributi dell'Utente forniti all'interno del PID italiano sono quelli elencati di seguito:

- Cognome attuale
- Nome attuale
- Data di Nascita
- Luogo di Nascita
- Nazionalità
- Codice di identificazione fiscale

In aggiunta agli attributi dell'Utente elencati sopra, il PID include anche le seguenti informazioni (`EU_2024/2977`_ e **Sezione 2 dell'ARF PID Rulebook v1.3** [`EIDAS-ARF`_]):

- Autorità emittente
- Paese emittente
- Data di scadenza
- Informazioni sullo stato di validità
- Informazioni di verifica dell'identità e dei dati

Alcuni attributi di dati, come il *codice di identificazione fiscale* e le *informazioni di verifica dell'identità e dei dati*, sono forniti come **estensioni domestiche** definite dalla specifica IT-Wallet italiana. NON fanno parte dell'ARF PID Rulebook (Annex 3.01, PID Rulebook v1.3), ma sono **permessi dal requisito ARF PID_06**, che consente agli Stati Membri di definire attributi domestici aggiuntivi oltre a quelli specificati nel Regolamento di Esecuzione della Commissione (CIR) 2024/2977 (`EU_2024/2977`_). In particolare, le informazioni di verifica dell'identità sono OBBLIGATORIE per i PID italiani per garantire:

- Tracciabilità del metodo di autenticazione dell'Utente.
- Conformità al livello di garanzia dell'identity proofing durante il processo di enrollment (LoA come definito dal Regolamento eIDAS).
- Verificabilità dei processi di verifica dell'identità e degli attributi dell'Utente.

Gli attributi che sono **estensioni domestiche** DEVONO essere inclusi nei **namespace domestici** che sono definiti nella Sezione :ref:`credential-data-model:Modello Dati PID in formato SD-JWT-VC` e Sezione :ref:`credential-data-model:Modello Dati PID in formato mdoc-CBOR` per i PID SD-JWT-VC e mdoc-CBOR rispettivamente.

Gli Attestati Elettronici di Attributi (Qualificati) ((Q)EAA) sono rilasciati dai Fornitori di (Q)EAA a un'Istanza del Wallet e DEVONO essere forniti in formato SD-JWT-VC o mdoc-CBOR.
Mentre il modello dati (Q)EAA è guidato dal caso d'uso e può includere diversi attributi dell'Utente, gli attributi di metadati specifici per ciascun formato dati sono forniti nelle sezioni seguenti.

Attributi di Metadati Format-Agnostic dell'Attestato Elettronico
-----------------------------------------------------------------

La seguente tabella definisce gli attributi di metadati comuni che sono applicabili agli Attestati Elettronici indipendentemente dal loro formato di codifica. Questi attributi rappresentano le informazioni semantiche sulla credenziale.

.. _table_format_agnostic_attributes:
.. list-table::
  :class: longtable
  :widths: 20 60
  :header-rows: 1

  * - **Identificatore Dati**
    - **Descrizione**
  * - **credential_type_identifier**
    - OBBLIGATORIO. Identificatore unico e resistente alle collisioni che specifica il tipo e lo schema dell'Attestato Elettronico. Definisce l'insieme di claim/attributi che l'Attestato Elettronico contiene e la loro struttura.
  * - **issuing_authority**
    - OBBLIGATORIO. Nome dell'autorità amministrativa che ha emesso l'Attestato Elettronico.
  * - **issuing_country**
    - OBBLIGATORIO. Codice paese Alpha-2, come specificato in ISO 3166-1, del paese o territorio del Fornitore di Attestati Elettronici.
  * - **issuance_date**
    - OPZIONALE. Data (e se possibile ora) in cui l'Attestato Elettronico è stato emesso e/o in cui è iniziato il periodo di validità amministrativa dell'Attestato Elettronico.
  * - **expiry_date**
    - OPZIONALE. Data (e se possibile ora) di scadenza dell'Attestato Elettronico.
  * - **location_status**
    - OPZIONALE. La posizione delle informazioni sullo stato di validità dell'Attestato Elettronico dove il Fornitore di Attestati Elettronici revoca l'Attestato Elettronico.
  * - **cryptographic_binding**
    - OPZIONALE. Oggetto contenente il materiale crittografico per la prova di possesso.
  * - **verification**
    - OPZIONALE. Oggetto contenente informazioni di Identity proofing e verifica dei dati dell'Utente.

Le sezioni seguenti forniscono gli attributi specifici del formato e una mappatura degli attributi di metadati sopra indicati ai parametri tecnici specifici del formato quando la credenziale è codificata in formato SD-JWT-VC o mdoc-CBOR.

Formato Attestato Elettronico SD-JWT-VC
----------------------------------------

Quando gli Attestati Elettronici sono emessi in formato SD-JWT-VC, DEVONO essere conformi alle specifiche `SD-JWT`_ e `SD-JWT-VC`_.

SD-JWT DEVE essere firmato utilizzando la chiave privata del Fornitore di Attestati Elettronici. SD-JWT DEVE essere fornito insieme a un Type Metadata relativo all'Attestato Elettronico emesso secondo le Sezioni 6 e 6.3 di [`SD-JWT-VC`_]. Il payload DEVE contenere il claim **_sd_alg** descritto nella Sezione 4.1.1 `SD-JWT`_ e gli altri claim specificati in questa sezione.

Il claim **_sd_alg** indica l'algoritmo di hash utilizzato dal Fornitore di Attestati Elettronici per generare i digest come descritto nella Sezione 4.1.1 di `SD-JWT`_. **_sd_alg** DEVE essere impostato su uno degli algoritmi specificati nella Sezione :ref:`Cryptographic Algorithms <algorithms:Algoritmi Crittografici>`.

I claim che non sono divulgabili selettivamente DEVONO essere inclusi nell'SD-JWT così come sono. I digest delle disclosure, insieme a eventuali decoy se presenti, DEVONO essere contenuti nell'array **_sd**, come specificato nella Sezione 4.2.4.1 di `SD-JWT`_.

Le Disclosure vengono fornite al Titolare insieme all'SD-JWT nel *Combined Format for Issuance* che è una serie ordinata di valori codificati in base64url, ciascuno separato dal successivo da un singolo carattere tilde ('~') come segue:

.. code-block:: text

  <Issuer-Signed-JWT>~<Disclosure 1>~<Disclosure 2>~...~<Disclosure N>

Vedere `SD-JWT-VC`_ e `SD-JWT`_ per ulteriori dettagli.


Parametri SD-JWT dell'Attestato Elettronico
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Il JOSE Header contiene i seguenti parametri obbligatori:

.. _table_sd-jwt-vc_jose_header:
.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Claim**
    - **Descrizione**
    - **Riferimento**
  * - **typ**
    - OBBLIGATORIO. DEVE essere valorizzato con ``dc+sd-jwt`` come definito in `SD-JWT-VC`_. NON DEVE essere valorizzato con ``none``.
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
    - OBBLIGATORIO. Contiene il certificato della chiave pubblica X.509 o la catena di certificati [:rfc:`5280`] corrispondente alla chiave utilizzata per firmare digitalmente il JWT.
    - :rfc:`7515` Sezione 4.1.8 e [`SD-JWT-VC`_] Sezione 3.5.

Il payload JWT contiene i seguenti claim. Salvo diversamente specificato, i seguenti claim NON DEVONO essere divulgabili selettivamente.


.. _table_sd-jwt-vc_parameters:
.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Descrizione**
      - **Riferimento**
    * - **iss**
      - OBBLIGATORIO. *Stringa*. Stringa URL che rappresenta l'identificativo univoco del Fornitore di Attestati Elettronici.
      - `[RFC7519, Sezione 4.1.1] <https://www.iana.org/go/rfc7519>`_.
    * - **sub**
      - OPZIONALE. *Stringa*. L'identificativo del soggetto dell'Attestato Elettronico, l'Utente, DEVE essere un valore opaco e NON DEVE corrispondere a nessun dato anagrafico o essere derivato dai dati anagrafici dell'Utente tramite pseudonimizzazione. Inoltre, è richiesto che due diverse Credenziali emesse NON DEVONO utilizzare lo stesso valore di ``sub``.
      - `[RFC7519, Sezione 4.1.2] <https://www.iana.org/go/rfc7519>`_.
    * - **iat**
      - OPZIONALE. Timestamp UNIX con l'orario di emissione del JWT, codificato come NumericDate come indicato in :rfc:`7519`.
      - `[RFC7519, Sezione 4.1.6] <https://www.iana.org/go/rfc7519>`_.
    * - **exp**
      - OBBLIGATORIO. Timestamp UNIX con l'orario di scadenza del JWT, codificato come NumericDate come indicato in :rfc:`7519`.
      - `[RFC7519, Sezione 4.1.4] <https://www.iana.org/go/rfc7519>`_.
    * - **nbf**
      - OPZIONALE. Timestamp UNIX con l'orario di inizio validità del JWT, codificato come NumericDate come indicato in :rfc:`7519`.
      - `[RFC7519, Sezione 4.1.4] <https://www.iana.org/go/rfc7519>`_.
    * - **issuing_authority**
      - OBBLIGATORIO. *Stringa*. Identificatore dati `issuing_authority` codificato nel formato come definito nella Sezione :ref:`credential-data-model:Attributi di Metadati Format-Agnostic dell'Attestato Elettronico`.
      - Regolamento di esecuzione della Commissione `EU_2024/2977`_.
    * - **issuing_country**
      - OBBLIGATORIO. *Stringa*. Identificatore dati `issuing_country` codificato nel formato come definito nella Sezione :ref:`credential-data-model:Attributi di Metadati Format-Agnostic dell'Attestato Elettronico`.
      - Regolamento di esecuzione della Commissione `EU_2024/2977`_.
    * - **date_of_expiry**
      - OPZIONALE. *Stringa*. Identificatore dati `expiry_date` codificato nel formato come definito nella Sezione :ref:`credential-data-model:Attributi di Metadati Format-Agnostic dell'Attestato Elettronico`. Questo attributo si riferisce al periodo di validità amministrativa dell'Attestato Elettronico, che è tipicamente diverso dal periodo di validità tecnica espresso dal claim JWT ``exp``.
      - Regolamento di esecuzione della Commissione `EU_2024/2977`_.
    * - **status**
      - OBBLIGATORIO solo se l'Attestato Elettronico è long-lived. *Oggetto JSON*. Identificatore dati `location_status` codificato nel formato come definito nella Sezione :ref:`credential-data-model:Attributi di Metadati Format-Agnostic dell'Attestato Elettronico`. DEVE contenere il membro JSON `status_assertion` o `status_list`.
      - Sezione 3.2.2.2 `SD-JWT-VC`_ e Sezione 11 `OAUTH-STATUS-ASSERTION`_.
    * - **cnf**
      - OBBLIGATORIO. *Oggetto JSON*. Identificatore dati `cryptographic_binding` codificato nel formato come definito nella Sezione :ref:`credential-data-model:Attributi di Metadati Format-Agnostic dell'Attestato Elettronico`, contenente il materiale crittografico per la prova di possesso. Includendo un claim **cnf** (confirmation) in un JWT, il Fornitore del JWT dichiara che il Titolare ha il controllo della chiave privata relativa a quella pubblica definita nel parametro **cnf**. Il destinatario DEVE verificare crittograficamente che il Titolare abbia effettivamente il controllo di quella chiave.
      - `[RFC7800, Sezione 3.1] <https://www.iana.org/go/rfc7800>`_ e Sezione 3.2.2.2 `SD-JWT-VC`_.
    * - **vct**
      - OBBLIGATORIO. *Stringa*. Identificatore dati `credential_type_identifier` codificato nel formato come definito nella Sezione :ref:`credential-data-model:Attributi di Metadati Format-Agnostic dell'Attestato Elettronico`. Il valore del tipo di Attestato Elettronico DEVE essere una URN e DEVE essere impostato utilizzando uno dei valori ottenuti dai metadata del Fornitore di Attestati Elettronici, il confronto dei caratteri letterali inclusi in questa URN DEVE essere eseguito in modo case-sensitive. È l'identificativo del tipo di SD-JWT VC e DEVE essere impostato con un valore resistente alle collisioni come definito nella Sezione 2 di :rfc:`7515`. DEVE contenere anche il numero di versione del tipo di Attestato Elettronico. A meno che non sia diversamente specificato da `EIDAS-ARF`_ e dagli EUDI Rulebook, il ``vct`` DOVREBBE seguire una struttura come ``urn:it-wallet:{credential_type}:{credential_type_version}``.
      - Sezione 3.2.2.2 `SD-JWT-VC`_.
    * - **vct#integrity**
      - OBBLIGATORIO. *Stringa*. Il valore DEVE essere una stringa "integrity metadata" come definito nella Sezione 3 di [`W3C-SRI`_]. *SHA-256*, *SHA-384* e *SHA-512* DEVONO essere supportati come funzioni crittografiche di hash. *MD5* e *SHA-1* NON DEVONO essere utilizzati. Questo claim DEVE essere verificato in base a quanto indicato nella Sezione 3.3.5 di [`W3C-SRI`_].
      - Sezione 6.1 `SD-JWT-VC`_, [`W3C-SRI`_]
    * - **verification**
      - OPZIONALE. *Oggetto JSON*. Identificatore dati `verification` codificato nel formato come definito nella Sezione :ref:`credential-data-model:Attributi di Metadati Format-Agnostic dell'Attestato Elettronico`.
        Include i seguenti sotto-valori:

          * ``trust_framework``: OBBLIGATORIO. *Stringa* che identifica il trust framework utilizzato per l'autenticazione dell'Utente. DEVE essere impostato utilizzando uno dei valori descritti nella mappa `trust_frameworks_supported` fornita nei Metadata del Fornitore di Attestati Elettronici.
          * ``assurance_level``: OBBLIGATORIO. *Stringa* che identifica il livello di garanzia dell'identità garantito durante il processo di autenticazione dell'Utente.
          * ``evidence``: OPZIONALE. Ogni voce dell'array DEVE contenere i seguenti membri:

            - ``type``: OPZIONALE. *Stringa*. Rappresenta il tipo di evidenza. DEVE essere impostato a ``vouch``.
            - ``time``: OPZIONALE. *Timestamp UNIX* con l'orario dell'autenticazione o della verifica.
            - ``attestation``: OPZIONALE. Contiene i seguenti membri:

                - ``type``: OPZIONALE. *Stringa* DEVE essere impostato a ``digital_attestation``.
                - ``reference_number``: OPZIONALE. *Stringa.* identificativo della risposta di autenticazione o verifica.
                - ``date_of_issuance``: OPZIONALE. *Stringa*. data di emissione dell'attestazione.
                - ``voucher``: OPZIONALE. *Oggetto JSON*. DEVE contenere il claim ``organization`` in formato Stringa leggibile.

      - Estensione domestica.
    * - **_sd**
      - OBBLIGATORIO. *Array di stringhe*, dove ogni stringa rappresenta un digest di una Disclosure.
      - 4.2.4.1 `SD-JWT`_
    * - **_sd_alg**
      - OBBLIGATORIO. *Stringa*. Algoritmo di hash utilizzato dal Fornitore di Attestati Elettronici per generare i digest.
      - 4.1.1 `SD-JWT`_

.. note::
  I claim JWT standard ``nbf`` e ``exp`` sono utilizzati per esprimere il periodo di validità tecnica di un Attestato Elettronico conforme a SD-JWT VC.

Se il parametro ``status`` è valorizzato con ``status_list``, è un Oggetto JSON contenente i seguenti sotto-parametri:

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


Se il parametro ``status`` è valorizzato con ``status_assertion``, è un Oggetto JSON contenente il claim *credential_hash_alg* che indica l'algoritmo utilizzato per l'hashing dell'Attestato Elettronico a cui è associata la Status Assertion. Si RACCOMANDA di utilizzare *sha-256*.


Modello Dati PID in formato SD-JWT-VC
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Per il PID SD-JWT-VC definito in questa specifica, il valore ``vct`` DEVE essere ``urn:eudi:pid:it:1`` in conformità ai requisiti dell'ARF PID Rulebook v1.3 per le estensioni domestiche PID (requisito **PID_14**, Sezione 4.2, estendendo il tipo base ``urn:eudi:pid:``).

.. note::
   **Fase Transitoria:**

   Durante la fase transitoria prima della piena operatività EUDIW, le implementazioni nazionali POSSONO utilizzare il valore ``vct`` ``urn:it-wallet:pid:1``. Una volta raggiunta la piena interoperabilità EUDIW, tutte le implementazioni DEVONO transitare all'identificatore conforme EUDI ``urn:eudi:pid:it:1`` specificato sopra.

In base a `EU_2024/2977`_ e alla **Sezione 4 dell'ARF PID Rulebook v1.3** [`EIDAS-ARF`_], il PID in formato SD-JWT-VC DEVE supportare i seguenti Attributi Utente:

.. _table_sd-jwt-vc_pid_parameters:
.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Descrizione**
      - **Riferimento**
    * - **given_name**
      - OBBLIGATORIO. *Stringa*. Nome attuale.
      - Sezione 5.1 di `OIDC`_ e Regolamento di esecuzione della Commissione `EU_2024/2977`_
    * - **family_name**
      - OBBLIGATORIO. *Stringa*. Cognome attuale.
      - Sezione 5.1 di `OIDC`_ e Regolamento di esecuzione della Commissione `EU_2024/2977`_
    * - **birthdate**
      - OBBLIGATORIO. *Stringa*. Data di Nascita. DEVE essere impostata secondo ISO8601-1 (formato YYYY-MM-DD).
      - Regolamento di esecuzione della Commissione `EU_2024/2977`_
    * - **place_of_birth**
      - OBBLIGATORIO. *Oggetto JSON*. Luogo di Nascita. Almeno uno tra `country`, `region`, `locality` DEVE essere presente.
      - Regolamento di esecuzione della Commissione `EU_2024/2977`_
    * - **nationalities**
      - OBBLIGATORIO. *Array di stringhe*. Uno o più codici paese alpha-2 come specificato in ISO 3166-1.
      - Regolamento di esecuzione della Commissione `EU_2024/2977`_
    * - **personal_administrative_number**
      - OBBLIGATORIO se ``tax_id_code`` non è presente, altrimenti OPZIONALE. *Stringa*. Identificativo univoco nazionale di una persona fisica generato da ANPR in formato stringa.
      - Regolamento di esecuzione della Commissione `EU_2024/2977`_
    * - **tax_id_code**
      - OBBLIGATORIO se ``personal_administrative_number`` non è presente, altrimenti OPZIONALE. *Stringa*. Codice di identificazione fiscale nazionale della persona fisica in formato Stringa. DEVE essere impostato secondo ETSI EN 319 412-1. Ad esempio ``TINIT-<ItalianTaxIdentificationNumber>``.
      - Estensione domestica

Tutti gli attributi Utente elencati sopra DEVONO essere divulgabili selettivamente.
Oltre agli attributi di metadati obbligatori definiti nella :ref:`Tabella Parametri SD-JWT <table_sd-jwt-vc_jose_header>` e nella :ref:`Tabella Parametri SD-JWT <table_sd-jwt-vc_parameters>`, i seguenti attributi di metadati sono OBBLIGATORI per un PID:

  - **date_of_expiry**
  - **sub**
  - **iat**
  - **verification**


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

**Claim** ``given_name``:

 * Hash SHA-256: ``Jkbj8aLr-z2_c-HVxCbiw6YXFNHiyLSv1xGjN8lRogI``
 * Disclosure:
   ``WyJrZ2h0ZTVNRE5IYlFmZEpIcDg4cENBIiwgImdpdmVuX25hbWUiLCAiTWFy``
   ``aW8iXQ``
 * Contenuto:
   ``["kghte5MDNHbQfdJHp88pCA", "given_name", "Mario"]``


**Claim** ``family_name``:

 * Hash SHA-256: ``MWJufQz_DFWc9cR4yxq8XqmTZfglkg2D2Sxa3UFN4Qk``
 * Disclosure:
   ``WyJoWDFURXpfejg3N19YQXRyM0NPYVdnIiwgImZhbWlseV9uYW1lIiwgIlJv``
   ``c3NpIl0``
 * Contenuto:
   ``["hX1TEz_z877_XAtr3COaWg", "family_name", "Rossi"]``


**Claim** ``birthdate``:

 * Hash SHA-256: ``uIapUlDTKsB5wN7BF6xuBNTtl74gl5iCu_aQ5nj3YL8``
 * Disclosure:
   ``WyJZV3RJMDZ4RGRDeXZUYWxjSW5URTNBIiwgImJpcnRoZGF0ZSIsICIxOTgw``
   ``LTAxLTEwIl0``
 * Contenuto:
   ``["YWtI06xDdCyvTalcInTE3A", "birthdate", "1980-01-10"]``


**Claim** ``tax_id_code``:

 * Hash SHA-256: ``_C7hoKFt0kV190v2GXIwLUIiDbc_7LcyofQmgDfute8``
 * Disclosure:
   ``WyItejM0Y0oxZ0M1VUJQQ0l4OE9oTmlRIiwgInRheF9pZF9jb2RlIiwgIlRJ``
   ``TklULVhYWFhYWFhYWFhYWFhYWFgiXQ``
 * Contenuto:
   ``["-z34cJ1gC5UBPCIx8OhNiQ", "tax_id_code",``
   ``"TINIT-XXXXXXXXXXXXXXXX"]``


**Claim** ``place_of_birth``:

 * Hash SHA-256: ``tI5s2A_Ez6oZv6plZzUPjYAL-SJGiAUFyRbhzLsluGU``
 * Disclosure:
   ``WyJYY1hsUFZDcWpITnZlQkNubFZQWWdBIiwgInBsYWNlX29mX2JpcnRoIiwg``
   ``eyJsb2NhbGl0eSI6ICJSb21hIn1d``
 * Contenuto:
   ``["XcXlPVCqjHNveBCnlVPYgA", "place_of_birth", {"locality":``
   ``"Roma"}]``


**Claim** ``nationalities``:

 * Hash SHA-256: ``GHYjuGUthjtB4q4Oz_ZSGPmCokLOpv2kpFNzz1LfFUY``
 * Disclosure:
   ``WyJLTmM1LUdrOUNRaF9UZEdicUJLSTdBIiwgIm5hdGlvbmFsaXRpZXMiLCBb``
   ``IklUIl1d``
 * Contenuto:
   ``["KNc5-Gk9CQh_TdGbqBKI7A", "nationalities", ["IT"]]``

Il formato combinato per l'emissione del PID è dato da:

.. literalinclude:: ../../examples/pid-sd-jwt-example-combined.txt
  :language: text

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

**Claim** ``document_number``:

 * Hash SHA-256: ``D4VkWjnA0WON7HdCGFtU869MSvORHPf8p5fQRD5gNj0``
 * Disclosure:
   ``WyJrZ2h0ZTVNRE5IYlFmZEpIcDg4cENBIiwgImRvY3VtZW50X251bWJlciIs``
   ``ICJYWFhYWFhYWFhYIl0``
 * Contenuto:
   ``["kghte5MDNHbQfdJHp88pCA", "document_number", "XXXXXXXXXX"]``


**Claim** ``given_name``:

 * Hash SHA-256: ``qbRtUHp9Oax9dm5GeKnw_W12Yu1E2DoU6wrFPee7aBo``
 * Disclosure:
   ``WyJoWDFURXpfejg3N19YQXRyM0NPYVdnIiwgImdpdmVuX25hbWUiLCAiTWFy``
   ``aW8iXQ``
 * Contenuto:
   ``["hX1TEz_z877_XAtr3COaWg", "given_name", "Mario"]``


**Claim** ``family_name``:

 * Hash SHA-256: ``Q7TX7kL8CNUp3BFBKP5xxIuPu5gRgkO6HplM3E1iMIc``
 * Disclosure:
   ``WyJZV3RJMDZ4RGRDeXZUYWxjSW5URTNBIiwgImZhbWlseV9uYW1lIiwgIlJv``
   ``c3NpIl0``
 * Contenuto:
   ``["YWtI06xDdCyvTalcInTE3A", "family_name", "Rossi"]``


**Claim** ``birth_date``:

 * Hash SHA-256: ``oF2qeWAbKO_qWGQ5z-HGKeifl2PMIEMbJe8L-PJ-wko``
 * Disclosure:
   ``WyItejM0Y0oxZ0M1VUJQQ0l4OE9oTmlRIiwgImJpcnRoX2RhdGUiLCAiMTk4``
   ``MC0wMS0xMCJd``
 * Contenuto:
   ``["-z34cJ1gC5UBPCIx8OhNiQ", "birth_date", "1980-01-10"]``


**Claim** ``expiry_date``:

 * Hash SHA-256: ``_ckhwGvTwFceg8jAFrQwqbw978ZHsaLJE_hs-rqV9lQ``
 * Disclosure:
   ``WyJYY1hsUFZDcWpITnZlQkNubFZQWWdBIiwgImV4cGlyeV9kYXRlIiwgIjIw``
   ``MjQtMDEtMDEiXQ``
 * Contenuto:
   ``["XcXlPVCqjHNveBCnlVPYgA", "expiry_date", "2024-01-01"]``


**Claim** ``tax_id_code``:

 * Hash SHA-256: ``Wq3gFfmC0I9Lefw1mh-Bk5XPRtoSCg9aE23uOhxakas``
 * Disclosure:
   ``WyJLTmM1LUdrOUNRaF9UZEdicUJLSTdBIiwgInRheF9pZF9jb2RlIiwgIlRJ``
   ``TklULVhYWFhYWFhYWFhYWFhYWFgiXQ``
 * Contenuto:
   ``["KNc5-Gk9CQh_TdGbqBKI7A", "tax_id_code",``
   ``"TINIT-XXXXXXXXXXXXXXXX"]``


**Claim** ``constant_attendance_allowance``:

 * Hash SHA-256: ``JOQk0kuBSVk80rFlv9VGY-yiIzsfzEJKk3d4RROfzkM``
 * Disclosure:
   ``WyIyaFFtWXBIeVgtbVpKaHoyeHNVWWNRIiwgImNvbnN0YW50X2F0dGVuZGFu``
   ``Y2VfYWxsb3dhbmNlIiwgdHJ1ZV0``
 * Contenuto:
   ``["2hQmYpHyX-mZJhz2xsUYcQ", "constant_attendance_allowance",``
   ``true]``


Il formato combinato per l'emissione del (Q)EAA è rappresentato di seguito:

.. literalinclude:: ../../examples/qeaa-sd-jwt-example-combined.txt
  :language: text

Type Metadata dell'Attestato Elettronico
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Il documento di *Type Metadata* DEVE essere un *JSON object* e contiene i seguenti parametri.

.. _table_metadata_type_json_obj:
.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Descrizione**
      - **Riferimento**
    * - **name**
      - OBBLIGATORIO. Nome *human-readable* del tipo di Attestato Elettronico. In casistiche multilingua, i tag di lingua vengono aggiunti al nome del claim, delimitandoli con il carattere `#` come definito in :rfc:`5646` (ad es. *name#it-IT*).
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
          * ``name``: nome *human-readable* del tipo di Attestato Elettronico. [OBBLIGATORIO].
          * ``description``: descrizione *human-readable* per il tipo di Attestato Elettronico. [OBBLIGATORIO].
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
                * ``background_image``: Oggetto contenente informazioni sull'immagine di sfondo da visualizzare per l'Attestato Elettronico. Questa proprietà è OPZIONALE [Allineato con SD-JWT-VC Draft 12]. L'oggetto contiene i seguenti sottovalori:

                    * ``uri``: URI che punta all'immagine di sfondo. [OBBLIGATORIO]
                    * ``uri#integrity``: "integrity metadata" come definito nella Sezione 3 di `W3C-SRI`_. [OBBLIGATORIO].

                * ``text_color``: valore del colore in RGB come definito in `W3C.CSS-COLOR`_ per il testo dell'Attestato Elettronico. [OPZIONALE].

          .. note::
            L'uso del template SVG è RACCOMANDATO per tutte le applicazioni che lo supportano.

      - [`SD-JWT-VC`_] Sezione 8.
    * - **claims**
      - OBBLIGATORIO. Array di oggetti contenenti informazioni per la visualizzazione e la validazione dei claim dell'Attestato Elettronico. Ogni oggetto contiene le seguenti proprietà:

          * ``path``: array che indica i/il claim a cui ci si riferisce. [OBBLIGATORIO].
          * ``display``: array contenente informazioni di visualizzazione sul claim indicato nel ``path``. L'array contiene un oggetto per ogni lingua supportata dal tipo di Attestato Elettronico. Questa proprietà è OBBLIGATORIA. Contiene i seguenti parametri:
             * ``lang``: tag di lingua come definito in :rfc:`5646` Sezione 2. [OBBLIGATORIO].
             * ``label``: etichetta *human-readable* per il claim. [OBBLIGATORIO].
             * ``description``: descrizione *human-readable* per il claim. [OBBLIGATORIO].
          * ``sd``: stringa che indica se il claim è divulgabile selettivamente. DEVE essere impostato su `always` se il claim è divulgabile selettivamente o `never` se non lo è. [OBBLIGATORIO].
          * ``svg_id``: stringa alfanumerica contenente l'ID del claim referenziato nel template SVG come definito in [`SD-JWT-VC`_] Sezione 9. [OBBLIGATORIO].
      - [`SD-JWT-VC`_] Sezione 9.


Un esempio non normativo di *Type Metadata* dell'Attestato Elettronico è fornito di seguito.

.. literalinclude:: ../../examples/vc-metadata-type.json
  :language: JSON


Recupero del Type Metadata della Credenziale Digitale
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In conformità con la Sezione 6.3.3 di `SD-JWT-VC`_, il documento JSON del *Type Metadata* PUÒ essere recuperato tramite un *well-known* endpoint.
Questo endpoint, fornito dal Fornitore di Attestati Elettronici, DEVE avere il seguente formato: ``https://{Dominio Credential Issuer}/.well-known/vct/{vct}``.
L'endpoint restituisce un codice di stato ``200 OK`` e supporta ``application/json`` e ``application/jwt`` come content type.

Di seguito è riportato un esempio non normativo.

.. code-block:: http

    GET /.well-known/vct/urn:eudi:pid:it:1 HTTP/1.1
    Host: issuer.example.it
    Accept: application/jwt

    HTTP/1.1 200 OK
    Content-Type: application/jwt

    eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...

.. code-block:: http

    GET /.well-known/vct/urn:eudi:pid:it:1 HTTP/1.1
    Host: issuer.example.it
    Accept: application/json

    HTTP/1.1 200 OK
    Content-Type: application/json

    {	
      "name": "...",
      "description": "...",
      ...
    }


Formato Attestato Elettronico mdoc-CBOR
------------------------------------------

Gli Attestati Elettronici emessi in formato mdoc-CBOR DEVONO essere basati sullo standard ISO/IEC 18013-5.
I dati in mdoc DEVONO essere codificati in CBOR come definito in :rfc:`8949`.

Questo modello dati struttura gli Attestati Elettronici in componenti distinti: namespaces (**nameSpaces**) e prova crittografica (**issuerAuth**).
I namespace categorizzano e strutturano i dati (o attributi, vedi :ref:`credential-data-model:Attributi dei Namespaces`). Mentre la prova crittografica garantisce integrità e autenticità attraverso il Mobile Security Object (MSO).

L'MSO memorizza in modo sicuro i digest crittografici degli attributi all'interno dei `nameSpaces`. Ciò consente alle Relying Party di convalidare gli attributi divulgati rispetto ai valori **digestID** corrispondenti senza rivelare l'intero Attestato Elettronico.
Vedere :ref:`credential-data-model:Mobile Security Object` per i dettagli.

Un Attestato Elettronico in formato mdoc-CBOR DEVE avere la seguente struttura:

.. _table_mdoc_structure:
.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Parametro**
      - **Descrizione**
      - **Riferimento**
    * - **nameSpaces**
      - *(map)*. I namespace all'interno dei quali sono definiti i dati. Un Attestato Elettronico PUÒ includere più namespace.
      - [ISO 18013-5#8.3.2.1.2]
    * - **issuerAuth**
      - *(COSE_Sign1)*. Contiene il *Mobile Security Object* (MSO), un documento COSE Sign1, emesso dal Fornitore di Attestati Elettronici.
      - [ISO 18013-5#9.1.2.4]


.. note::
  Gli attributi mDL obbligatori utilizzano il namespace standard `org.iso.18013.5.1`. Tuttavia, PUÒ avere anche un namespace domestico, come `org.iso.18013.5.1.IT`, per includere attributi aggiuntivi definiti in questo profilo di implementazione. Ogni namespace all'interno di `nameSpaces` DEVE condividere lo stesso valore del tipo di documento emesso (`docType`), che identifica la natura dell'Attestato Elettronico, come definito in `issuerAuth`.

La struttura di una Credenziale in formato mdoc-CBOR è ulteriormente descritta nelle sezioni seguenti.

Mobile Security Object
^^^^^^^^^^^^^^^^^^^^^^

L'**issuerAuth** rappresenta il `Mobile Security Object` che è un `Documento COSE Sign1` definito in :rfc:`9052`. Ha la seguente struttura di dati:

   * protected header
   * unprotected header
   * payload
   * signature

Il **protected header** DEVE contenere il seguente parametro codificato in formato CBOR:

.. _table_protected_headers_mdoc:
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

.. _table_unprotected_headers_mdoc:
.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Elemento**
      - **Descrizione**
      - **Riferimento**
    * - **4**
      - *(tstr, OPZIONALE)*. Identificativo univoco del JWK dell'Emittente. Richiesto quando l'Emittente del documento mdoc utilizza OpenID Federation.
      - :ref:`trust-infrastructure:L'Infrastruttura di Trust`
    * - **33**
      - *(array)*. Catena di certificati X.509 relativa all'Emittente. Obbligatorio se l'autenticazione è basata su certificato X.509.
      - :rfc:`9360`

.. note::
  `x5chain` è incluso nell'unprotected header con lo scopo di consentire al Titolare di aggiornare la catena di certificati X.509, relativa all'emittente del `Mobile Security Object`, senza invalidare la firma.

Il **payload** DEVE contenere il *MobileSecurityObject*, senza il parametro di header COSE Sign `content-type` e codificato come una *byte string* (bstr) utilizzando il *CBOR Tag* 24.

Il `MobileSecurityObject` DEVE avere i seguenti attributi, se non diversamente specificato:

.. _table_MobileSecurityObject_attributes:
.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Elemento**
      - **Descrizione**
      - **Riferimento**
    * - **docType**
      - *(tstr)*. Codifica formato dell'identificatore dati `credential_type_identifier` come definito nella Sezione :ref:`credential-data-model:Attributi di Metadati Format-Agnostic dell'Attestato Elettronico`. Definisce il tipo di Attestato Elettronico in formato mdoc. DEVE essere una stringa nella forma:

          - definito a livello europeo, DEVE essere una stringa della forma ``eu.europa.ec.{credential_type}.{version}`` (ad es., ``eu.europa.ec.eudi.pid.1``).
          - definito a livello nazionale, DEVE essere una stringa della forma ``{Trust Anchor reverse domain}.{credential_type}.{version}`` (ad es., ``it-wallet.trust-registry.pid.1``).

      - [ISO 18013-5#9.1.2.4]
    * - **version**
      - *(tstr)*. Versione del `MobileSecurityObject`.
      - [ISO 18013-5#9.1.2.4]
    * - **validityInfo**
      - *(map, REQUIRED)*. Contiene le date e gli orari di emissione e scadenza del `MobileSecurityObject`. Include i seguenti sub-valori:

          * **signed** *(tdate, OPTIONAL)*. Il timestamp che indica quando il `MobileSecurityObject` è stato firmato.
          * **validFrom** *(tdate, OPTIONAL)*. Timestamp prima del quale il `MobileSecurityObject` non è considerato valido. Quando presente, DEVE essere uguale o successivo a `signed`.
          * **validUntil** *(tdate, REQUIRED)*. Timestamp dopo il quale il `MobileSecurityObject` non è più considerato valido.

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

Attributi dei Namespaces
^^^^^^^^^^^^^^^^^^^^^^^^

**nameSpaces** contiene una o più voci *nameSpace*, ciascuna identificata da un nome. All'interno di ogni **nameSpace**, sono inclusi uno o più *IssuerSignedItemBytes*, ciascuno codificato in una stringa di byte codificata in CBOR con Tag 24 (#6.24(bstr .cbor)), che appare come 24(<<... >>) nella notazione diagnostica. Essa rappresenta le informazioni da divulgare, una per ogni digest presente all'interno del `Mobile Security Object` e DEVE contenere i seguenti attributi:

.. _table_attribute_namespaces:
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

Attributi Metadata degli Attestati Elettronici mdoc-CBOR
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

I seguenti **elementIdentifiers** che rappresentano attributi metadata format-encoded sono definiti per gli Attestati Elettronici in formato mdoc-CBOR all'interno del rispettivo *nameSpace*:

.. _table_element_identifiers_mdoc:
.. list-table::
   :class: longtable
   :widths: 20 60 20
   :header-rows: 1

   * - **Element Identifier**
     - **Descrizione**
     - **Riferimento**

   * - **issuing_country**
     - *(tstr, OBBLIGATORIO)*. Identificatore dati format-encoded `issuing_country` come definito nella Sezione :ref:`credential-data-model:Format-Agnostic Credential Metadata Attributes`. Codice paese Alpha-2 come definito in [ISO 3166-1].
     - [ISO 18013-5#7.2]

   * - **issuing_authority**
     - *(tstr, OBBLIGATORIO)*. Identificatore dati format-encoded `issuing_authority` come definito nella Sezione :ref:`credential-data-model:Format-Agnostic Credential Metadata Attributes`. Il valore DEVE contenere solo caratteri Latin1b e deve avere una lunghezza massima di 150 caratteri.
     - [ISO 18013-5#7.2]

   * - **expiry_date**
     - *(tdate o full-date, OPZIONALE)*. Identificatore dati format-encoded `expiry_date` come definito nella Sezione :ref:`credential-data-model:Format-Agnostic Credential Metadata Attributes`. DEVE essere conforme al formato ISO 8601-1 YYYY-MM-DD.
     - Sezione 3 dell'ARF PID Rulebook v1.3 [`EIDAS-ARF`_]

   * - **sub**
     - *(uuid, OPZIONALE)*. Identifica il soggetto dell'Attestato Elettronico mdoc (l'Utente). L'identificativo DEVE essere opaco, NON DEVE corrispondere a nessun dato anagrafico e NON DEVE essere derivato dai dati anagrafici dell'Utente attraverso la pseudonimizzazione. Inoltre, Attestati Elettronici diversi emessi allo stesso Utente o a Utenti diversi NON DEVONO utilizzare lo stesso valore `sub`.
     - Estensione domestica.

   * - **verification**
     - *(map, OPZIONALE)*. Identificatore dati format-encoded `verification` come definito nella Sezione :ref:`credential-data-model:Format-Agnostic Credential Metadata Attributes`. La CBOR map include i seguenti membri:

         * ``trust_framework`` *(tstr, OBBLIGATORIO)*: trust framework utilizzato per l'autenticazione dell'Utente.
         * ``assurance_level`` *(tstr, OBBLIGATORIO)*: livello di garanzia dell'identità garantito durante l'autenticazione dell'Utente.
         * ``evidence`` *(array, OPZIONALE)*: ogni voce contiene:

           - ``type`` *(tstr, OPZIONALE)*: tipo di evidenza (es., ``vouch``).
           - ``time`` *(tdate, OPZIONALE)*: timestamp dell'autenticazione o verifica.
           - ``attestation`` *(map, OPZIONALE)*: contiene:

             - ``type`` *(tstr, OPZIONALE)*: tipo di attestazione (es., ``digital_attestation``).
             - ``reference_number`` *(tstr, OPZIONALE)*: identificativo della risposta di autenticazione/verifica.
             - ``date_of_issuance`` *(tdate, OPZIONALE)*: data di emissione dell'attestazione.
             - ``voucher`` *(map, OPZIONALE)*: contiene ``organization`` *(tstr)*.

     - Estensione domestica.

.. note::
  Gli attributi specifici dell'Utente dell'Attestato Elettronico sono definiti nel Catalogo degli Attestati Elettronici.
  Gli attributi specifici dell'Utente per gli Attestati Elettronici in formato mdoc come quelli del PID o mDL sono inclusi facendo riferimento agli corrispettivi `elementIdentifiers` definiti in ISO/IEC 18013-5 o nella specifica `EIDAS-ARF`_.

.. note::

  Indipendentemente dal tipo di Attestato Elettronico, il valore di ``sub`` NON DEVE essere mostrato all'Utente, in quanto non è un attributo dello stesso. È utilizzato per scopi di identificazione dagli Emittenti di Credenziali.

Modello Dati PID in formato mdoc-CBOR
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Il PID in formato mdoc-CBOR DEVE utilizzare il **docType** ``eu.europa.ec.eudi.pid.it.1`` in conformità al requisito ARF **PID_06** per le estensioni domestiche PID (estendendo il tipo base ``eu.europa.ec.eudi.pid.1`` definito in **PID_04**).

Gli attributi PID DEVONO essere codificati come specificato nella **Sezione 3 dell'ARF PID Rulebook v1.3** [`EIDAS-ARF`_] e organizzati nei seguenti namespace:

- **Attributi PID standard ARF**: namespace ``eu.europa.ec.eudi.pid.1``
- **Estensioni domestiche italiane**: namespace ``eu.europa.ec.eudi.pid.it.1``

.. note::
   **Fase Transitoria:**

   Durante la fase transitoria prima della piena operatività EUDIW, le implementazioni nazionali POSSONO utilizzare il **docType** ``it.wallet.trust-registry.pid.1`` con un unico namespace nazionale ``it.wallet.trust-registry.pid.1`` per tutti gli attributi. Una volta raggiunta la piena interoperabilità EUDIW, tutte le implementazioni DEVONO transitare al **docType** e alla struttura di namespace conformi EUDI specificati sopra.

La Sezione 3 dell'ARF PID Rulebook v1.3 definisce:

- Identificatori degli attributi e formati di codifica (Sezione 3.1.1)
- Regole di codifica specifiche per ``nationality`` (Sezione 3.1.2), ``birth_date`` (Sezione 3.1.4), e ``place_of_birth`` (Sezione 3.1.5)
- Requisiti di codifica canonica CBOR (:RFC:`8949` Sezione 4.2)

.. note::
   **Differenze chiave rispetto alla codifica SD-JWT:**

   L'ARF PID Rulebook v1.3 utilizza nomi diversi tra i formati SD-JWT e mdoc-CBOR:

   - mdoc usa ``birth_date`` (non ``birthdate`` come in SD-JWT)
   - mdoc usa ``expiry_date`` (non ``date_of_expiry`` come in SD-JWT)
   - Entrambi i formati usano ``place_of_birth`` con la stessa struttura CBOR map

   Vedere Sezione 3.1.1 (codifica mdoc) e Sezione 4.1.1 (codifica SD-JWT) dell'ARF PID Rulebook v1.3 per la mappatura completa.

In base a `EU_2024/2977`_ e alla **Sezione 3 dell'ARF PID Rulebook v1.3** [`EIDAS-ARF`_], il PID in formato mdoc-CBOR DEVE supportare i seguenti Attributi Utente nel namespace ``eu.europa.ec.eudi.pid.1``:

.. _table_mdoc-cbor_pid_attributes:
.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **elementIdentifier**
      - **Descrizione**
      - **Riferimento**
    * - **given_name**
      - OBBLIGATORIO. *(tstr)*. Nome attuale.
      - Sezione 3.1.1 dell'ARF PID Rulebook v1.3 [`EIDAS-ARF`_] e Regolamento di esecuzione della Commissione `EU_2024/2977`_
    * - **family_name**
      - OBBLIGATORIO. *(tstr)*. Cognome attuale.
      - Sezione 3.1.1 dell'ARF PID Rulebook v1.3 [`EIDAS-ARF`_] e Regolamento di esecuzione della Commissione `EU_2024/2977`_
    * - **birth_date**
      - OBBLIGATORIO. *(full-date)*. Data di Nascita. DEVE essere codificata come stringa full-date secondo :rfc:`8949`.
      - Sezione 3.1.4 dell'ARF PID Rulebook v1.3 [`EIDAS-ARF`_] e Regolamento di esecuzione della Commissione `EU_2024/2977`_
    * - **place_of_birth**
      - OBBLIGATORIO. *(map)*. Luogo di Nascita. Almeno uno tra ``country``, ``region``, ``locality`` DEVE essere presente.
      - Sezione 3.1.5 dell'ARF PID Rulebook v1.3 [`EIDAS-ARF`_] e Regolamento di esecuzione della Commissione `EU_2024/2977`_
    * - **nationality**
      - OBBLIGATORIO. *(tstr)*. Codice paese alpha-2 come specificato in ISO 3166-1. Per nazionalità multiple, DEVONO essere incluse istanze multiple di questo attributo.
      - Sezione 3.1.2 dell'ARF PID Rulebook v1.3 [`EIDAS-ARF`_] e Regolamento di esecuzione della Commissione `EU_2024/2977`_
    * - **personal_administrative_number**
      - OBBLIGATORIO se ``tax_id_code`` non è presente, altrimenti OPZIONALE. *(tstr)*. Identificativo univoco nazionale di una persona fisica generato da ANPR.
      - Sezione 2.2 dell'ARF PID Rulebook v1.3 [`EIDAS-ARF`_] e Regolamento di esecuzione della Commissione `EU_2024/2977`_

**Requisiti per i PID italiani:**

Per i PID italiani si applicano i seguenti requisiti:

- L'attributo ``verification`` (definito in :ref:`Attributes <table_element_identifiers_mdoc>`) è OBBLIGATORIO (mentre è OPZIONALE per altri tipi di credenziali).
- Almeno uno dei seguenti identificatori DEVE essere presente:

  - ``personal_administrative_number`` (attributo ARF standard, namespace ``eu.europa.ec.eudi.pid.1``)
  - ``tax_id_code`` (estensione domestica italiana, namespace ``eu.europa.ec.eudi.pid.it.1``)

Oltre agli attributi di metadati obbligatori definiti nella :ref:`Tabella MobileSecurityObject <table_MobileSecurityObject_attributes>` e nella :ref:`Tabella Attributi Metadata mdoc-CBOR <table_element_identifiers_mdoc>`, i seguenti attributi di metadati sono OBBLIGATORI per un PID:

  - **expiry_date**
  - **sub**
  - **verification**

**Estensioni Domestiche (requisito ARF PID_06):**

Il seguente attributo domestico è definito per i PID italiani e DEVE essere inserito nel namespace domestico ``eu.europa.ec.eudi.pid.it.1``:

.. list-table::
   :class: longtable
   :widths: 20 20 60
   :header-rows: 1

   * - **elementIdentifier**
     - **Codifica**
     - **Descrizione**
   * - **tax_id_code**
     - ``tstr``
     - Codice Fiscale italiano. Formato: ETSI EN 319 412-1 (es., ``TINIT-RSSMRA80A10H501U``). Lunghezza massima: 150 caratteri.

**Esempio non normativo:**

Un esempio non normativo di un PID in formato mdoc-CBOR (notazione diagnostica) è mostrato di seguito:

.. literalinclude:: ../../examples/pid-mdoc-cbor-example.txt
  :language: text

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
     - Tagged Date (ad esempio, il Tag `0` è usato per indicare una stringa di data/ora in formato :RFC:`3339`)

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
     - | Type_Metadata.name (hdr)
       | Type_Metadata.description (hdr)
       | Type_Metadata.extends (hdr)
       | Type_Metadata.data_source (hdr)
       | Type_Metadata.display (hdr)
       | Type_Metadata.claims (hdr)
     - | -
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
       | Type_Metadata.extends#integrity (hdr)
     - |
       | -
   * - Formato dell'Attestato Elettronico
     - typ (hdr)
     - |
       | -
       |
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
  - Nel formato mdoc-CBOR, la versione dell'Attestato Elettronico non è definita esplicitamente; è disponibile solo per l'IssuerAuth. Al contrario, il formato SD-JWT include informazioni sulla versione tramite l'URN `vct`.
  - `Disclosures`, `_sd` e `_sd_alg` abilitano la Divulgazione Selettiva dei claim SD-JWT. I parametri `_sd` e `_sd_alg` fanno parte del payload SD-JWT, mentre le `Disclosures` vengono inviate separatamente in un *Combined Format* insieme al SD-JWT.
  - Il parametro `Type_Metadata.claims` in SD-JWT e la struttura `nameSpaces` in mdoc-CBOR sono funzionalmente equivalenti, poiché entrambi definiscono i nomi dei claim e la loro struttura. Le `Disclosures` SD-JWT per gli attributi divulgati corrispondono esattamente ai `nameSpaces`, inclusi nomi e valori degli attributi, e i valori dei *salt*.
  - Un namespace domestico accoglie attributi come `verification` e `sub`, che non sono definiti negli elementIdentifiers standard ISO per gli Attestati Elettronici in formato mdoc-CBOR.

.. include:: ../common/common_definitions.rst

Modello di Dati del PID
==============================================

L'Attestato Elettronico di Dati di Identificazione Personale (PID) è rilasciato dal Fornitore di Attestati Elettronici di Dati di Identificazione Personale secondo le leggi nazionali e DEVE essere fornito in formato SD-JWT-VC e mdoc-CBOR. Lo scopo principale del PID è consentire alle persone fisiche di essere autenticate per accedere a un servizio o a una risorsa protetta.
Il PID DEVE essere fornito secondo i requisiti del modello dati definiti in `EU_2024/2977`_ e **Sezione 2 dell'ARF PID Rulebook v1.3** [`EIDAS-ARF`_], gli attributi dell'Utente forniti all'interno del PID italiano sono quelli elencati di seguito:

- Cognome attuale
- Nome attuale
- Data di Nascita
- Luogo di Nascita
- Nazionalità
- Numero di identificazione dell'Utente nei servizi delle Relying Party pubbliche (ad esempio il *codice fiscale*)

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

Gli attributi che sono **estensioni domestiche** DEVONO essere inclusi nei **namespace domestici** che sono definiti nella Sezione :ref:`credential-data-model-pid:Modello Dati PID in formato SD-JWT-VC` e Sezione :ref:`credential-data-model-pid:Modello Dati PID in formato mdoc-CBOR` per i PID SD-JWT-VC e mdoc-CBOR rispettivamente.

Modello Dati PID in formato SD-JWT-VC
---------------------------------------

Per il PID SD-JWT-VC definito in questa specifica, il valore ``vct`` DEVE essere ``urn:eudi:pid:it:1`` in conformità ai requisiti dell'ARF PID Rulebook v1.3 per le estensioni domestiche PID (requisito **PID_14**, Sezione 4.2, estendendo il tipo base ``urn:eudi:pid:``).

.. note::
   **Fase Transitoria:**

   Durante la fase transitoria prima della piena operatività EUDIW, le implementazioni nazionali POSSONO utilizzare il valore ``vct`` ``urn:it-wallet:pid:1``. Una volta raggiunta la piena interoperabilità EUDIW, tutte le implementazioni DEVONO transitare all'identificatore conforme EUDI ``urn:eudi:pid:it:1`` specificato sopra.

In base a `EU_2024/2977`_ e alla **Sezione 4 dell'ARF PID Rulebook v1.3** [`EIDAS-ARF`_], il PID in formato SD-JWT-VC include i seguenti Attributi Utente:

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
Oltre agli attributi di metadati obbligatori definiti nella :ref:`Tabella Parametri di header JOSE SD-JWT <table_sd-jwt-vc_jose_header>` e nella :ref:`Tabella Parametri SD-JWT <table_sd-jwt-vc_parameters>`, i seguenti attributi di metadati sono OBBLIGATORI per un PID:

  - **date_of_expiry**
  - **sub** (estensione domestica)
  - **iat**
  - **cnf**
  - **status**
  - **verification** (estensione domestica)

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

Modello Dati PID in formato mdoc-CBOR
--------------------------------------

Il PID in formato mdoc-CBOR DEVE utilizzare il **docType** ``eu.europa.ec.eudi.pid.1`` in conformità al requisito ARF **PID_04**.

Gli attributi PID DEVONO essere codificati come specificato nella **Sezione 3 dell'ARF PID Rulebook v1.3** [`EIDAS-ARF`_] e organizzati nei seguenti namespace:

- **Attributi PID standard ARF**: namespace ``eu.europa.ec.eudi.pid.1``
- **Estensioni domestiche italiane**: namespace ``eu.europa.ec.eudi.pid.it.1``

.. note::
   **Fase Transitoria:**

   Durante la fase transitoria prima della piena operatività EUDIW, le implementazioni nazionali POSSONO utilizzare il **docType** ``{Trust Anchor reverse domain}.pid.1`` con un unico namespace nazionale ``{Trust Anchor reverse domain}.pid.1`` per tutti gli attributi. Una volta raggiunta la piena operatività EUDIW, tutte le implementazioni DEVONO transitare al **docType** e alla struttura di namespace conformi EUDI specificati sopra.

In base a `EU_2024/2977`_ e alla **Sezione 3 dell'ARF PID Rulebook v1.3** [`EIDAS-ARF`_], il PID in formato mdoc-CBOR include i seguenti Attributi Utente:

.. _table_mdoc-cbor_pid_attributes:
.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **elementIdentifier**
      - **Descrizione**
      - **Namespace**
    * - **given_name**
      - OBBLIGATORIO. *(tstr)*. Nome attuale.
      - ``eu.europa.ec.eudi.pid.1``
    * - **family_name**
      - OBBLIGATORIO. *(tstr)*. Cognome attuale.
      - ``eu.europa.ec.eudi.pid.1``
    * - **birth_date**
      - OBBLIGATORIO. *(full-date)*. Data di Nascita. DEVE essere codificata come stringa full-date secondo :rfc:`8949`.
      - ``eu.europa.ec.eudi.pid.1``
    * - **place_of_birth**
      - OBBLIGATORIO. *(map)*. Luogo di Nascita. Almeno uno tra ``country``, ``region``, ``locality`` DEVE essere presente.
      - ``eu.europa.ec.eudi.pid.1``
    * - **nationality**
      - OBBLIGATORIO. *(array di tstr)*. Uno o più codici paese alpha-2 come specificato in ISO 3166-1. Codificato come tipo CDDL ``nationalities`` (array di codici paese).
      - ``eu.europa.ec.eudi.pid.1``
    * - **personal_administrative_number**
      - OBBLIGATORIO se ``tax_id_code`` non è presente, altrimenti OPZIONALE. *(tstr)*. Identificativo univoco nazionale di una persona fisica generato da ANPR.
      - ``eu.europa.ec.eudi.pid.1``
    * - **tax_id_code**
      - OBBLIGATORIO se ``personal_administrative_number`` non è presente, altrimenti OPZIONALE. *(tstr)*. Codice Fiscale italiano. Formato: ETSI EN 319 412-1 (es., ``TINIT-RSSMRA80A10H501U``). Lunghezza massima: 150 caratteri.
      - ``eu.europa.ec.eudi.pid.it.1``

Oltre agli attributi di metadati obbligatori definiti nella :ref:`Tabella MobileSecurityObject <table_MobileSecurityObject_attributes>` e nella :ref:`Tabella Attributi Metadata mdoc-CBOR <table_element_identifiers_mdoc>`, i seguenti attributi di metadati sono OBBLIGATORI per un PID:

.. list-table::
    :class: longtable
    :widths: 50 50
    :header-rows: 1

    * - **elementIdentifier**
      - **Namespace**
    * - **expiry_date**
      - ``eu.europa.ec.eudi.pid.1``
    * - **sub**
      - ``eu.europa.ec.eudi.pid.it.1``
    * - **validityInfo.signed**
      - ``eu.europa.ec.eudi.pid.1``
    * - **verification**
      - ``eu.europa.ec.eudi.pid.it.1``

.. note::
   **Differenze chiave rispetto alla codifica SD-JWT:**

   L'ARF PID Rulebook v1.3 utilizza nomi di claim diversi tra i formati SD-JWT e mdoc-CBOR:

   - mdoc usa ``birth_date`` (non ``birthdate`` come in SD-JWT)
   - mdoc usa ``expiry_date`` (non ``date_of_expiry`` come in SD-JWT)
   - mdoc usa ``nationality`` (non ``nationalities`` come in SD-JWT). Nota: entrambi i formati codificano il valore come array di codici paese.

   Vedere la Sezione 3.1.1 (codifica mdoc) e la Sezione 4.1.1 (codifica SD-JWT) dell'ARF PID Rulebook v1.3 per la mappatura completa.


Esempio non normativo del PID in mdoc-CBOR
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Un esempio non normativo di un PID in formato mdoc-CBOR (notazione diagnostica) è mostrato di seguito:

.. literalinclude:: ../../examples/pid-mdoc-cbor-example.txt
  :language: text
  
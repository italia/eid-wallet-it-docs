.. include:: ../common/common_definitions.rst


Modello di Dati dell'IT-Wallet ID
=================================

L'**IT-Wallet ID** (*Attestato Elettronico di Dati di Identificazione Personale di ambito nazionale*) è un Attestato Elettronico di Attributi (EAA) rilasciato dall'EAA Provider secondo le leggi nazionali. È fornito in formato SD-JWT VC.

L'IT-Wallet ID è destinato **esclusivamente all'uso nazionale** con Relying Party che operano nell'ambito della giurisdizione nazionale per l'accesso ai servizi online. NON DEVE essere utilizzato per interazioni cross-border e **non** costituisce un PID ai sensi del quadro europeo di Identità Digitale.

Lo scopo principale dell'IT-Wallet ID è consentire alle persone fisiche di essere autenticate per l'accesso a un servizio o a una risorsa protetta nell'ambito della giurisdizione nazionale.
Gli attributi dell'Utente forniti all'interno dell'IT-Wallet ID sono quelli elencati di seguito:

- Cognome attuale
- Nome attuale
- Data di Nascita
- Luogo di Nascita
- Nazionalità
- Numero di identificazione dell'Utente nei servizi delle Relying Party pubbliche (ad esempio il *codice fiscale*)

In aggiunta agli attributi dell'Utente elencati sopra, l'IT-Wallet ID include anche i seguenti attributi di metadati:

- Autorità emittente
- Paese emittente
- Data di scadenza
- Informazioni sullo stato di validità
- Informazioni di verifica dell'identità e dei dati

Le informazioni di identity proofing sono OBBLIGATORIE per l'IT-Wallet ID al fine di garantire:

- La valutazione del metodo di autenticazione dell'Utente utilizzato.
- La conformità al livello di garanzia dell'identity proofing durante il processo di iscrizione (*enrollment*), secondo il LoA definito dal Regolamento eIDAS.
- L'auditabilità dei processi di verifica degli attributi dell'Utente.

Modello di Dati dell'IT-Wallet ID in formato SD-JWT VC
------------------------------------------------------

L'IT-Wallet ID SD-JWT VC definito in questa specifica DEVE utilizzare il valore del claim ``vct`` impostato a ``urn:it-wallet:eid:1``, dove ``eid`` è il ``credential_type`` di catalogo dell'IT-Wallet ID.

L'IT-Wallet ID in formato SD-JWT VC include i seguenti Attributi Utente:

.. _table_sd-jwt-vc_it-wallet-id_parameters:
.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Claim**
      - **Descrizione**
      - **Riferimento**
    * - **given_name**
      - OBBLIGATORIO. *Stringa*. Nome attuale.
      - Sezione 5.1 di `OIDC`_ e Regolamento di Esecuzione della Commissione `EU_2024/2977`_
    * - **family_name**
      - OBBLIGATORIO. *Stringa*. Cognome attuale.
      - Sezione 5.1 di `OIDC`_ e Regolamento di Esecuzione della Commissione `EU_2024/2977`_
    * - **birthdate**
      - OBBLIGATORIO. *Stringa*. Data di Nascita. DEVE essere impostata secondo ISO8601-1 (formato YYYY-MM-DD).
      - Regolamento di Esecuzione della Commissione `EU_2024/2977`_
    * - **place_of_birth**
      - OBBLIGATORIO. *Oggetto JSON*. Luogo di Nascita. Almeno uno tra `country`, `region`, `locality` DEVE essere presente.
      - Regolamento di Esecuzione della Commissione `EU_2024/2977`_
    * - **nationalities**
      - OBBLIGATORIO. *Array di stringhe*. Uno o più codici paese alpha-2 come specificato in ISO 3166-1.
      - Regolamento di Esecuzione della Commissione `EU_2024/2977`_
    * - **personal_administrative_number**
      - OBBLIGATORIO se ``tax_id_code`` non è presente, OPZIONALE altrimenti. *Stringa*. Identificativo nazionale univoco di una persona fisica generato da ANPR in formato stringa.
      - Regolamento di Esecuzione della Commissione `EU_2024/2977`_
    * - **tax_id_code**
      - OBBLIGATORIO se ``personal_administrative_number`` non è presente, OPZIONALE altrimenti. *Stringa*. Codice fiscale nazionale della persona fisica in formato stringa. DEVE essere impostato secondo ETSI EN 319 412-1. Ad esempio ``TINIT-<ItalianTaxIdentificationNumber>``.
      - Estensione domestica

.. note::
   **Identity Matching**

   Per l'IT-Wallet ID, la Relying Party DEVE prima effettuare l'identity matching utilizzando ``tax_id_code``. Solo dopo un identity matching andato a buon fine, la Relying Party PUÒ effettuare l'identity reconciliation, collegando quella persona fisica a una precedente sessione Utente o a un record Utente memorizzato.

Tutti gli attributi dell'Utente elencati sopra DEVONO essere divulgabili selettivamente (*selectively disclosable*).
In aggiunta agli attributi di metadati obbligatori definiti nella :ref:`Tabella Parametri di header JOSE SD-JWT <table_sd-jwt-vc_jose_header>` e nella :ref:`Tabella Parametri SD-JWT <table_sd-jwt-vc_parameters>`, i seguenti attributi di metadati sono OBBLIGATORI per un IT-Wallet ID:

  - **date_of_expiry**
  - **sub** (estensione domestica)
  - **iat**
  - **cnf**
  - **status**
  - **verification** (estensione domestica)

Esempio Non Normativo di IT-Wallet ID in SD-JWT-VC
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Di seguito, l'esempio non normativo del payload di un IT-Wallet ID rappresentato in formato JSON.

.. literalinclude:: ../../examples/pid-json-example-payload.json
  :language: JSON

La corrispondente versione SD-JWT per l'IT-Wallet ID è data da

.. literalinclude:: ../../examples/pid-sd-jwt-example-header.json
  :language: JSON

.. literalinclude:: ../../examples/pid-sd-jwt-example-payload.json
  :language: JSON

L'elenco delle disclosure è presentato di seguito.

**Claim** ``given_name``:

 * SHA-256 Hash: ``Jkbj8aLr-z2_c-HVxCbiw6YXFNHiyLSv1xGjN8lRogI``
 * Disclosure:
   ``WyJrZ2h0ZTVNRE5IYlFmZEpIcDg4cENBIiwgImdpdmVuX25hbWUiLCAiTWFy``
   ``aW8iXQ``
 * Contents:
   ``["kghte5MDNHbQfdJHp88pCA", "given_name", "Mario"]``


**Claim** ``family_name``:

 * SHA-256 Hash: ``MWJufQz_DFWc9cR4yxq8XqmTZfglkg2D2Sxa3UFN4Qk``
 * Disclosure:
   ``WyJoWDFURXpfejg3N19YQXRyM0NPYVdnIiwgImZhbWlseV9uYW1lIiwgIlJv``
   ``c3NpIl0``
 * Contents:
   ``["hX1TEz_z877_XAtr3COaWg", "family_name", "Rossi"]``


**Claim** ``birthdate``:

 * SHA-256 Hash: ``uIapUlDTKsB5wN7BF6xuBNTtl74gl5iCu_aQ5nj3YL8``
 * Disclosure:
   ``WyJZV3RJMDZ4RGRDeXZUYWxjSW5URTNBIiwgImJpcnRoZGF0ZSIsICIxOTgw``
   ``LTAxLTEwIl0``
 * Contents:
   ``["YWtI06xDdCyvTalcInTE3A", "birthdate", "1980-01-10"]``


**Claim** ``tax_id_code``:

 * SHA-256 Hash: ``_C7hoKFt0kV190v2GXIwLUIiDbc_7LcyofQmgDfute8``
 * Disclosure:
   ``WyItejM0Y0oxZ0M1VUJQQ0l4OE9oTmlRIiwgInRheF9pZF9jb2RlIiwgIlRJ``
   ``TklULVhYWFhYWFhYWFhYWFhYWFgiXQ``
 * Contents:
   ``["-z34cJ1gC5UBPCIx8OhNiQ", "tax_id_code",``
   ``"TINIT-XXXXXXXXXXXXXXXX"]``


**Claim** ``place_of_birth``:

 * SHA-256 Hash: ``tI5s2A_Ez6oZv6plZzUPjYAL-SJGiAUFyRbhzLsluGU``
 * Disclosure:
   ``WyJYY1hsUFZDcWpITnZlQkNubFZQWWdBIiwgInBsYWNlX29mX2JpcnRoIiwg``
   ``eyJsb2NhbGl0eSI6ICJSb21hIn1d``
 * Contents:
   ``["XcXlPVCqjHNveBCnlVPYgA", "place_of_birth", {"locality":``
   ``"Roma"}]``


**Claim** ``nationalities``:

 * SHA-256 Hash: ``GHYjuGUthjtB4q4Oz_ZSGPmCokLOpv2kpFNzz1LfFUY``
 * Disclosure:
   ``WyJLTmM1LUdrOUNRaF9UZEdicUJLSTdBIiwgIm5hdGlvbmFsaXRpZXMiLCBb``
   ``IklUIl1d``
 * Contents:
   ``["KNc5-Gk9CQh_TdGbqBKI7A", "nationalities", ["IT"]]``

Il formato combinato per l'emissione dell'IT-Wallet ID è dato da:

.. literalinclude:: ../../examples/pid-sd-jwt-example-combined.txt
  :language: text

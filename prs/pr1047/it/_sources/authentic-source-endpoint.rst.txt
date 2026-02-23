.. include:: ../common/common_definitions.rst


.. role:: raw-html(raw)
  :format: html

Endpoint delle Fonti Autentiche
-------------------------------

Catalogo degli e-Service PDND delle Fonti Autentiche
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Le Fonti Autentiche pubbliche DEVONO realizzare e rendere disponibile tramite PDND il seguente e-service al fine di rilasciare al Fornitore di Attestati Elettronici gli Attributi dell'Utente necessari per l'emissione di un Attestato Elettronico.

L'e-service è descritto tramite una specifica OpenAPI in cui sono dettagliati i messaggi di richiesta, risposta ed errore.

.. only:: html

  .. note::
    La Specifica OpenAPI è disponibile :raw-html:`<a href="OAS3-PDND-AS.html" target="_blank">qui</a>`.
    Questa specifica OpenAPI può essere estesa dalle Fonti Autentiche, infatti, l'array ``attributeClaims`` PUÒ contenere proprietà aggiuntive specifiche di una particolare Credenziale. Queste proprietà aggiuntive, così come definito nella specifica OpenAPI, saranno inserite nella Credenziale dal Credential Issuer.

.. only:: latex

  .. note::
    La Specifica OpenAPI è disponibile :ref:`e-service-pdnd-template:Specifica OpenAPI della Fonte Autentica PDND`.
    Questa specifica OpenAPI può essere estesa dalle Fonti Autentiche, infatti, l'array ``attributeClaims`` PUÒ contenere proprietà aggiuntive specifiche di una particolare Credenziale. Queste proprietà aggiuntive, così come definito nella specifica OpenAPI, saranno inserite nella Credenziale dal Credential Issuer.

Get Attribute Claims
"""""""""""""""""""""""""""""""""""

.. _authentic-source-endpoint-get-attribute-claims:
.. list-table::
  :class: longtable
  :widths: 20 80
  :stub-columns: 1

  * - **Descrizione**
    - Questo servizio fornisce al Fornitore di Attestati Elettronici tutti gli attributi dell'Utente necessari per il rilascio di un Attestato Elettronico.
  * - **Erogatore**
    - Fonte Autentica
  * - **Fruitore**
    - Fornitore di Attestato Elettronico

.. note::
  La Fonte Autentica e il Credential Issuer DEVONO implementare la logica necessaria per tenere traccia delle richieste e delle risposte scambiate tramite questo e-Service, al fine di essere in grado di correlarle con la relativa emissione di un Attestato Elettronico. In particolare,
    - entrambi DEVONO salvare il valore ``jti`` contenuto nel payload del token Agid-JWT-Signature della richiesta per gestire i Segnali relativi alla disponibilità degli Attributi utili all'emissione in *deferred* di un Attestato Elettronico (vedere :ref:`signal-hub-endpoint:Elaborazione dei Segnali`);
    - la Fonte Autentica DEVE registrare il valore datetime fornito all'interno del parametro ``last_updated``, che indica data e orario dell'ultima volta che gli Attributi dell'Utente sono stati aggiornati nel database della Fonte Autentica;
    - il Credential Issuer DEVE leggere il valore ``last_updated`` ricevuto nella risposta per essere in grado di verificare se gli Attributi dell'Utente sono cambiati dall'ultima emissione di un Attestato Elettronico.

Mapping degli Stati del Ciclo di Vita degli Attestati Elettronici
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Per garantire la coerenza tra il "Ciclo di Vita degli Attestati Elettronici" documentato in :ref:`credential-revocation:Ciclo di Vita degli Attestati Elettronici` e l'Enum status delle OpenAPI, la seguente mappatura e logica operativa DEVE essere applicata per il campo ``status`` negli ``attributeClaims``.

**Direzionalità e Responsabilità:**
I cambiamenti di stato di un Attestato Elettronico a livello di Fornitore di Attestati Elettronici NON implicano un cambiamento presso la Fonte Autentica. Al contrario, qualsiasi cambiamento di stato di un dataset presso la Fonte Autentica DEVE essere elaborato dal Fornitore di Attestati Elettronici per aggiornare lo stato tecnico dell'Attestato Elettronico.

**Guida Operativa:**

* **Validità Tecnica vs Amministrativa**: Gli Attestati Elettronici distinguono tra una **validità tecnica** stabilita dal Fornitore di Attestati Elettronici (claim ``iat`` ed ``exp``) e una **validità amministrativa** determinata dalla Fonte Autentica (claim ``issuance_date`` ed ``expiry_date``).
* **Gerarchia delle Scadenze**: La scadenza tecnica (``exp``) NON DEVE essere successiva alla scadenza amministrativa (``expiry_date``). Per esempio, una patente di guida può essere amministrativamente valida per 10 anni, mentre l'Attestato Elettronico emesso può avere una scadenza tecnica di 1 anno.
* **Riemissione**: Se un Attestato Elettronico raggiunge la sua scadenza tecnica (``exp``) ma il dataset è ancora amministrativamente valido, lo stato OpenAPI rimane ``VALID``, consentendo all'Attestato Elettronico di essere riemesso più volte entro l'arco temporale amministrativo.
* **Verifica dei Metadati**: Il Fornitore di Attestati Elettronici DEVE verificare l'effettiva usabilità controllando sia i claim tecnici che le date amministrative.
* **Irreversibilità**: Dopo una transizione a ``INVALID``, l'Attestato Elettronico non può tornare a uno stato ``VALID``. È richiesta una nuova emissione per un nuovo dataset. Questo si applica sia alla revoca esplicita che alla scadenza amministrativa.
* **Elaborazione dei Segnali**: I Segnali DEVONO essere elaborati sequenzialmente. Se un Segnale invalida un Attestato Elettronico, i successivi Segnali di correzione per lo stesso oggetto vengono ignorati.

**Mapping degli Stati e Logica dei Casi:**

Il Fornitore di Attestati Elettronici DEVE aggiornare lo ``status`` dell'Attestato Elettronico in base ai Segnali ricevuti dalla Fonte Autentica via Signal Hub (``signalType=UPDATE``):

* **Revoca**: Se un dataset viene revocato presso la Fonte Autentica (stato ``INVALID``), il Fornitore di Attestati Elettronici DEVE revocare gli Attestati Elettronici che utilizzano quel dataset (transizione di stato da ``VALID/SUSPENDED`` a ``INVALID``).
* **Sospensione**: Se un dataset viene sospeso presso la Fonte Autentica (stato ``SUSPENDED``), il Fornitore di Attestati Elettronici DEVE sospendere gli Attestati Elettronici (transizione di stato da ``VALID`` a ``SUSPENDED``).
* **Ripristino**: Se un dataset sospeso torna a essere ``VALID`` presso la Fonte Autentica, il Fornitore di Attestati Elettronici DEVE ripristinare la validità dell'Attestato Elettronico (transizione di stato da ``SUSPENDED`` a ``VALID``).
* **Modifica**: Se un dataset viene modificato ma rimane ``VALID`` presso la Fonte Autentica, il Fornitore di Attestati Elettronici — rilevando il cambiamento tramite il campo ``last_updated`` — assegna lo stato tecnico ``ATTRIBUTE_UPDATE`` all'Attestato Elettronico. Questo avvia un flusso di riemissione quando l'Istanza del Wallet controlla lo stato.
* **Scadenza Amministrativa**:
    * **Scenario A (Basato sui metadati)**: Se ``expiry_date`` è stata condivisa con il Fornitore di Attestati Elettronici nei metadati, la Fonte Autentica NON invia Segnali alla scadenza; il Fornitore di Attestati Elettronici gestisce il ciclo di vita in modo indipendente garantendo che l'``exp`` tecnico sia <= ``expiry_date``.
    * **Scenario B (Basato sui segnali)**: Se ``expiry_date`` NON è presente nei metadati e il dataset scade, la Fonte Autentica DEVE impostare il suo stato su ``INVALID`` e inviare un Segnale via Signal Hub; il Fornitore di Attestati Elettronici revoca quindi gli Attestati Elettronici (transizione di stato a ``INVALID``).

Esempio di risposta della Authentic Source
""""""""""""""""""""""""""""""""""""""""""

La risposta ha come HTTP Content-Type ``application/jwt``. mDi seguito un esempio concreto con dati fittizi per chiarire forma e contenuto attesi.

.. literalinclude:: ../../examples/credential-claims-response-example.json
  :language: json
  :caption: Esempio di payload JSON di risposta (Get Attribute Claims)

In sintesi:

- **userClaims**: dati anagrafici dell'utente (nome, cognome, data/luogo di nascita, codice fiscale o numero di identificazione). Almeno uno tra ``tax_id_code`` e ``personal_administrative_number`` è richiesto se si forniscono user claims.
- **attributeClaims**: array di dataset; ogni elemento **DEVE** contenere ``object_id``, ``status`` (VALID | INVALID | SUSPENDED), ``last_updated`` (formato ISO 8601), più eventuali attributi aggiuntivi specifici del dataset (es. ``nationality``, ``residence_address``).
- **metadataClaims**: array di metadati per dataset (``object_id`` obbligatorio; ``issuance_date`` e ``expiry_date`` opzionali).
- **interval**: obbligatorio se non è presente il parametro ``claims`` nella richiesta; indica i secondi da attendere prima di ripetere la richiesta (es. 864000 = 10 giorni).

La risposta in caso di successo (HTTP 200) restituisce un oggetto ``CredentialClaimsResponse`` formattato come **Payload JSON**.

Verifica della Firma e Gestione Chiavi
''''''''''''''''''''''''''''''''''''''

Essendo il token di risposta firmato, il Credential Issuer (Fruitore) DEVE verificare la firma per garantire l'integrità e l'autenticità dei dati ricevuti dalla Fonte Autentica.

Il processo di verifica e recupero delle chiavi DEVE seguire rigorosamente il pattern standard definito per gli **e-Service PDND**.
Si rimanda all'Appendice tecnica (Sezione :ref:`e-service-pdnd:e-Service PDND`) per i dettagli sulla validazione del JWT e per le specifiche sul recupero della chiave pubblica dell'Erogatore tramite API di Interoperabilità.

.. warning::
  Non sono ammessi meccanismi alternativi di distribuzione del materiale crittografico (es. endpoint ``.well-known`` pubblici esposti direttamente dalla Fonte Autentica o distribuzione *out-of-band*). La gestione del trust DEVE rimanere centralizzata all'interno del perimetro dell'infrastruttura PDND come descritto nei riferimenti sopra citati.

.. include:: ../common/common_definitions.rst


.. role:: raw-html(raw)
  :format: html

Endpoint delle Fonti Autentiche
-------------------------------

Catalogo degli e-Service PDND delle Fonti Autentiche
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Le Fonti Autentiche pubbliche DEVONO realizzare e rendere disponibile tramite PDND il seguente e-service al fine di rilasciare al Fornitore di Attestati Elettronici gli Attributi dell'Utente necessari per l'emissione di un Attestato Elettronico.

.. only:: html

  .. note::
    La Specifica OpenAPI completa è disponibile :raw-html:`<a href="OAS3-PDND-AS.html" target="_blank">qui</a>`.

.. only:: latex

  .. note::
    La Specifica OpenAPI completa è disponibile :ref:`e-service-pdnd-template:Specifica OpenAPI della Fonte Autentica PDND`.

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

Esempio di risposta della Authentic Source
""""""""""""""""""""""""""""""""""""""""""

La risposta dell'endpoint è un JWT (``application/jwt``). Decodificando il payload di tale JWT, il Fornitore di Attestati Elettronici riceve una struttura come la seguente. I campi obbligatori sono ``iss``, ``aud``, ``exp``, ``iat``, ``jti``; gli altri campi sono opzionali o condizionati al tipo di attestato/dataset. Di seguito un esempio concreto con dati fittizi per chiarire forma e contenuto attesi.

.. literalinclude:: ../../examples/credential-claims-response-example.json
  :language: json
  :caption: Esempio di payload del JWT di risposta (Get Attribute Claims) dopo decodifica

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

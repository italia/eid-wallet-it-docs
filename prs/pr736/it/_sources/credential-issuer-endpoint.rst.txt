.. include:: ../common/common_definitions.rst

.. "included" file, so we start with '-' title level

.. role:: raw-html(raw)
  :format: html


Endpoint del Credential Issuer
------------------------------

Endpoint di Federazione
^^^^^^^^^^^^^^^^^^^^^^^

I Credential Issuer DEVONO fornire una Entity Configuration attraverso l'endpoint ``/.well-known/openid-federation``, secondo la Sezione :ref:`trust:Entity Configuration`. I dettagli tecnici sono forniti nella Sezione :ref:`credential-issuer-entity-configuration:Configurazione dell'Entità Fornitore di Credenziale`.

Endpoint di Emissione delle Credenziali
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: credential-issuance-endpoint.rst

Catalogo e-Service PDND del Credential Issuer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

I Credential Issuer DEVONO fornire i seguenti e-service attraverso PDND per:

  - gestire le notifiche di disponibilità dei dati e gli aggiornamenti degli attributi provenienti da una Fonte Autentica;
  - revocare le Credenziali Elettroniche emesse per un'Istanza del Wallet revocata
  - fornire statistiche sulle Credenziali emesse

.. only:: html

  .. note::
    Una Specifica OpenAPI completa è disponibile :raw-html:`<a href="OAS3-PDND-Issuer.html" target="_blank">qui</a>`.

.. only:: latex

  .. note::
    Una Specifica OpenAPI completa è disponibile :ref:`appendix-oas-pdnd-issuer:Credential Issuer PDND OpenAPI Specification`.

Notifica Credenziale Disponibile
""""""""""""""""""""""""""""""""

.. list-table::
  :class: longtable
  :widths: 20 80
  :stub-columns: 1

  * - **Descrizione**
    - Questo servizio informa gli Utenti quando una specifica Credenziale è diventata
      disponibile per essere inserita nel Wallet
  * - **Fornitore**
    - Fornitore di Credenziale
  * - **Consumatore**
    - Fonte Autentica

Notifica Aggiornamento Credenziale
""""""""""""""""""""""""""""""""""

.. list-table::
  :class: longtable
  :widths: 20 80
  :stub-columns: 1

  * - **Descrizione**
    - Il servizio è progettato per ricevere dalla Fonte Autentica (AS), tramite PDND,
      la notifica di un cambiamento di stato e/o valore di un attributo specifico (es. MDL)
      con cui è associato un documento digitale emesso dal Fornitore di Credenziale.
  * - **Fornitore**
    - Fornitore di Credenziale
  * - **Consumatore**
    - Fonte Autentica


Notifica Revoca Istanza del Wallet
""""""""""""""""""""""""""""""""""

.. list-table::
  :class: longtable
  :widths: 20 80
  :stub-columns: 1
  
  * - **Descrizione**
    - Questo servizio revoca tutte le Credenziali Elettroniche associate a uno specifico Utente.
  * - **Fornitore**
    - Fornitore di Credenziale
  * - **Consumatore**
    - Fornitore di Wallet


Ottieni Statistiche
"""""""""""""""""""

.. list-table::
  :class: longtable
  :widths: 20 80
  :stub-columns: 1

  * - **Descrizione**
    - Questo servizio restituisce dati statistici sulle Credenziali Elettroniche emesse.
  * - **Fornitore**
    - Fornitore di Credenziale
  * - **Consumatore**
    - Terza Parte Autorizzata

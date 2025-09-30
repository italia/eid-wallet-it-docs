.. include:: ../common/common_definitions.rst

.. "included" file, so we start with '-' title level

.. role:: raw-html(raw)
  :format: html


Endpoint del Credential Issuer
------------------------------

Endpoint di Federazione
^^^^^^^^^^^^^^^^^^^^^^^

I Credential Issuer DEVONO fornire una Entity Configuration attraverso l'endpoint ``/.well-known/openid-federation``, in accordo alla Sezione :ref:`trust:Entity Configuration`. I dettagli tecnici sono forniti nella Sezione :ref:`credential-issuer-entity-configuration:Entity Configuration del Fornitore di Attestati Elettronici`.

Endpoint relativi all'Emissione delgli Attestati Elettronici
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: credential-issuance-endpoint.rst

Catalogo e-Service PDND del Credential Issuer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

I Credential Issuer DEVONO fornire i seguenti e-service attraverso PDND per:

  - gestire le notifiche relative alla disponibilità dei dati e gli aggiornamenti degli attributi provenienti da una Fonte Autentica;
  - revocare gli Attestati Elettronici emessi per un'Istanza del Wallet revocata
  - fornire statistiche sugli Attestati Elettronici emessi

.. only:: html

  .. note::
    La specifica OpenAPI completa è disponibile :raw-html:`<a href="OAS3-PDND-Issuer.html" target="_blank">qui</a>`.

.. only:: latex

  .. note::
    La specifica OpenAPI completa è disponibile :ref:`appendix-oas-pdnd-issuer:Specifica OpenAPI del Credential Issuer PDND`.

Notify Available Credential
""""""""""""""""""""""""""""""""

.. list-table::
  :class: longtable
  :widths: 20 80
  :stub-columns: 1

  * - **Descrizione**
    - Questo servizio informa gli Utenti quando uno specifico Attestato Elettronico è
      disponibile per essere inserito nel Wallet
  * - **Fornitore**
    - Fornitore di Attestato Elettronico
  * - **Consumatore**
    - Fonte Autentica

Notify Update Credential
""""""""""""""""""""""""""""""""""

.. list-table::
  :class: longtable
  :widths: 20 80
  :stub-columns: 1

  * - **Descrizione**
    - Il servizio è progettato per ricevere dalla Fonte Autentica (AS), tramite PDND,
      la notifica di un cambiamento di stato e/o valore di un attributo specifico (es. MDL)
      a cui è associato un documento digitale emesso dal Fornitore di Attestato Elettronico.
  * - **Fornitore**
    - Fornitore di Attestato Elettronico
  * - **Consumatore**
    - Fonte Autentica


Notify Wallet Instance Revocation
""""""""""""""""""""""""""""""""""

.. list-table::
  :class: longtable
  :widths: 20 80
  :stub-columns: 1
  
  * - **Descrizione**
    - Questo servizio revoca tutti gli Attestati Elettronici associati a uno specifico Utente.
  * - **Fornitore**
    - Fornitore di Attestato Elettronico
  * - **Consumatore**
    - Fornitore di Wallet


Get Statistics
"""""""""""""""""""

.. list-table::
  :class: longtable
  :widths: 20 80
  :stub-columns: 1

  * - **Descrizione**
    - Questo servizio restituisce dati statistici sugli Attestati Elettronici emessi.
  * - **Fornitore**
    - Fornitore di Attestati Elettronici
  * - **Consumatore**
    - Terza Parte Autorizzata

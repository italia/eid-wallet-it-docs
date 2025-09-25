.. include:: ../common/common_definitions.rst

.. "included" file, so we start with '-' title level

.. role:: raw-html(raw)
  :format: html


Endpoint del Credential Issuer
-------------------------------

Endpoint di Federazione
^^^^^^^^^^^^^^^^^^^^^^^

I Credential Issuer DEVONO fornire una Entity Configuration attraverso l'endpoint ``/.well-known/openid-federation``, secondo la Sezione :ref:`trust:Entity Configuration`. I dettagli tecnici sono forniti nella Sezione :ref:`credential-issuer-entity-configuration:Entity Configuration del Fornitore di Attestati Elettronici`.

Endpoint di Rilascio degli Attestati Elettronici
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: credential-issuance-endpoint.rst

Catalogo degli e-Service PDND del Credential Issuer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

I Credential Issuer DEVONO fornire i seguenti e-service attraverso PDND per:

  - gestire le notifiche di disponibilità dei dati e gli aggiornamenti degli Attributi provenienti da una Fonte Autentica;
  - revocare gli Attestati Elettronici emessi per un'Istanza del Wallet revocata
  - fornire statistiche sugli Attestati Elettronici emessi

.. only:: html

  .. note::
    Lna Specifica OpenAPI completa è disponibile :raw-html:`<a href="OAS3-PDND-Issuer.html" target="_blank">qui</a>`.

.. only:: latex

  .. note::
    Lna Specifica OpenAPI completa è disponibile :ref:`appendix-oas-pdnd-issuer:Specifica OpenAPI del Credential Issuer PDND`.


Notify Wallet Instance Revocation
""""""""""""""""""""""""""""""""""

.. list-table::
  :class: longtable
  :widths: 20 80
  :stub-columns: 1
  
  * - **Descrizione**
    - Questo servizio revoca tutti gli Attestati Elettronici associati a uno specifico Utente.
  * - **Erogatore**
    - Fornitore di Attestato Elettronico
  * - **fruitore**
    - Fornitore di Wallet


Get Statistics
""""""""""""""

.. list-table::
  :class: longtable
  :widths: 20 80
  :stub-columns: 1

  * - **Descrizione**
    - Questo servizio restituisce dati statistici sugli Attestati Elettronici emessi.
  * - **Erogatore**
    - Credential Issuer
  * - **Fruitore**
    - Terza Parte Autorizzata

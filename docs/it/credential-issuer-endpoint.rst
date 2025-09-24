.. include:: ../common/common_definitions.rst

.. "included" file, so we start with '-' title level

.. role:: raw-html(raw)
  :format: html


Endpoint del Credential Issuer
-------------------------------

Endpoint di Federazione
^^^^^^^^^^^^^^^^^^^^^^^

I Credential Issuer DEVONO fornire una Entity Configuration attraverso l'endpoint ``/.well-known/openid-federation``, secondo la Sezione :ref:`trust:Entity Configuration`. I dettagli tecnici sono forniti nella Sezione :ref:`credential-issuer-entity-configuration:Entity Configuration del Fornitore di Attestati Elettronici`.

Endpoint di Rilascio delle Credenziali
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: credential-issuance-endpoint.rst

Catalogo del Credential Issuer e-Service PDND
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

I Credential Issuer DEVONO fornire i seguenti e-service attraverso PDND per:

  - gestire le notifiche di disponibilità dei dati e gli aggiornamenti degli Attributi provenienti da una Fonte Autentica;
  - revocare le Credenziali Elettroniche rilasciate a un'Istanza del Wallet revocata
  - fornire statistiche sulle Credenziali rilasciate

.. only:: html

  .. note::
    Una Specifica OpenAPI completa è disponibile :raw-html:`<a href="OAS3-PDND-Issuer.html" target="_blank">qui</a>`.

.. only:: latex

  .. note::
    Una Specifica OpenAPI completa è disponibile :ref:`appendix-oas-pdnd-issuer:Specifica OpenAPI del Credential Issuer PDND`.


Notifica Revoca Istanza del Wallet
""""""""""""""""""""""""""""""""""

.. list-table::
  :class: longtable
  :widths: 20 80
  :stub-columns: 1
  
  * - **Descrizione**
    - Questo servizio revoca tutte le Credenziali Elettroniche associate a un Utente specifico.
  * - **Fornitore**
    - Credential Issuer
  * - **Consumatore**
    - Fornitore di Wallet


Ottieni Statistiche
"""""""""""""""""""

.. list-table::
  :class: longtable
  :widths: 20 80
  :stub-columns: 1

  * - **Descrizione**
    - Questo servizio restituisce dati statistici sulle Credenziali Elettroniche rilasciate.
  * - **Fornitore**
    - Credential Issuer
  * - **Consumatore**
    - Terza Parte Autorizzata

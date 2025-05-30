.. include:: ../common/common_definitions.rst


.. role:: raw-html(raw)
  :format: html

Endpoint delle Fonti Autentiche
-------------------------------

e-Service Catalogo delle Fonti Autentiche PDND
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Le Fonti Autentiche pubbliche DEVONO fornire il seguente e-service attraverso PDND per fornire al Fornitore di Credenziale gli attributi dell'Utente necessari per il rilascio di un Attestato Elettronico.

.. only:: html

  .. note::
    Una specifica OpenAPI di esempio è disponibile :raw-html:`<a href="OAS3-PDND-AS.html" target="_blank">qui</a>`.

.. only:: latex

  .. note::
    Una specifica OpenAPI di esempio è disponibile :ref:`appendix-oas-pdnd-as:Specifica OpenAPI della Fonte Autentica PDND`.

Ottieni Attributi dell'Utente
"""""""""""""""""""""""""""""

.. list-table::
  :class: longtable
  :widths: 20 80
  :stub-columns: 1

  * - **Descrizione**
    - Questo servizio fornisce al Fornitore di Credenziale tutti gli attributi dell'Utente necessari per il rilascio di un Attestato Elettronico.
  * - **Fornitore**
    - Fonte Autentica
  * - **Consumatore**
    - Fornitore di Credenziale

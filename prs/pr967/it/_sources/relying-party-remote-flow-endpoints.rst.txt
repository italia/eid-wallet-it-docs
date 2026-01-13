.. include:: ../common/common_definitions.rst

.. _relying-party-remote-flow-endpoints-endpoint-per-flussi-remoti-della-relying-party:

.. "included" file, so we start with '-' title level

La Relying Party DEVE esporre una serie di endpoint per supportare i flussi di presentazione remoti come definiti in OpenID4VP 1.0. Questi endpoint abilitano la verifica sicura delle credenziali, l'instaurazione della fiducia e l'autenticazione dell'utente per modelli di interazione cross-device e same-device.

.. note::
  I test relativi agli endpoint per flussi remoti della Relying Party sono definiti nella matrice di test per presentazione remota (:ref:`test-plans-remote-presentation:Matrice di Test per il Verificatore di Credenziali in Remoto`).


Endpoint di Federazione
"""""""""""""""""""""""

La Relying Party DEVE fornire la propria Entity Configuration attraverso l'endpoint ``/.well-known/openid-federation``, secondo la Sezione :ref:`trust-infrastructure:Entity Configuration`. Questo endpoint abilita l'instaurazione della fiducia e la scoperta delle capacità della Relying Party.

I dettagli tecnici sono forniti nella Sezione :ref:`relying-party-entity-configuration:Entity Configuration Relying Party`.


Endpoint per Flussi Remoti OpenID4VP
""""""""""""""""""""""""""""""""""""

I seguenti endpoint sono richiesti per i flussi di presentazione remota OpenID4VP 1.0 come descritto in :ref:`remote-flow:Flusso Remoto`. Questi endpoint supportano sia i flussi Same Device che Cross Device:

Endpoint Request URI
....................

L'Endpoint Request URI è dove la Relying Party fornisce il Request Object firmato all'Istanza del Wallet. Questo endpoint supporta sia i metodi GET che POST come definito nella specifica OpenID4VP 1.0.

Per i requisiti di implementazione dettagliati, vedere :ref:`remote-flow-endpoint-uri-request` e :ref:`remote-flow:Richiesta all'Endpoint URI Request`.


Endpoint Response URI
.....................

L'Endpoint Response URI riceve l'Authorization Response dall'Istanza del Wallet contenente la Verifiable Presentation. Questo endpoint elabora la presentazione e convalida le credenziali.

Per i requisiti di implementazione dettagliati, vedere :ref:`remote-flow:Authorization Response` e :ref:`remote-flow:Risposta della Relying Party`.


Endpoint Status (Opzionale)
...........................

L'Endpoint Status è un endpoint opzionale che consente all'user-agent di monitorare il progresso del flusso di presentazione. Questo endpoint è particolarmente utile per i flussi Same Device dove l'user-agent deve sapere quando l'Istanza del Wallet ha completato la presentazione.

Per i requisiti di implementazione dettagliati, vedere :ref:`remote-flow:Status Endpoint` e :ref:`remote-flow-errori-status-endpoint`.


Endpoint di Gestione Dati Utente
""""""""""""""""""""""""""""""""

Il seguente endpoint supporta la gestione dei dati utente e i requisiti di conformità alla privacy per i flussi remoti:

Endpoint di Cancellazione della Relying Party
.............................................

L'Endpoint di Cancellazione, che è descritto in :ref:`relying-party-metadata:Metadati della Relying Party`, consente alle Istanze di Wallet di richiedere la cancellazione degli attributi presentati alla Relying Party. La Relying Party DEVE richiedere l'autenticazione dell'Utente prima di procedere con la cancellazione degli attributi.

.. _relying-party-remote-flow-endpoints-richiesta-di-cancellazione:

Richiesta di Cancellazione
..........................

La Richiesta di Cancellazione DEVE essere una richiesta GET all'Endpoint di Cancellazione. L'Istanza di Wallet DEVE anche supportare un meccanismo di callback che consenta allo User-Agent di notificare lo stato della richiesta all'Istanza di Wallet (e quindi all'Utente) una volta che viene restituita la Risposta di Cancellazione.

Di seguito è riportato un esempio non normativo di una Richiesta di Cancellazione in cui l'URL di callback viene passato come parametro di query.

.. code-block:: http

  GET /erasure-endpoint?callback_url=https://wallet-instance/erasure_response HTTP/1.1
  Host: relying-party.example.org

.. _relying-party-remote-flow-endpoints-risposta-di-cancellazione:

Risposta di Cancellazione
.........................

Se la cancellazione di tutti gli attributi associati all'Utente è avvenuta con successo, la Risposta di Cancellazione DEVE restituire un Status Code HTTP 204.

Se invece la procedura di cancellazione degli attributi fallisce per qualsiasi circostanza, la Relying Party DEVE restituire una risposta di errore con ``application/json`` come tipo di contenuto e DEVE includere i seguenti parametri:

    - ``error``: Il codice di errore.
    - ``error_description``: Testo in forma leggibile che fornisce ulteriori dettagli per chiarire la natura dell'errore riscontrato.

La seguente tabella elenca gli Status Code HTTP e i relativi Error Codes che DEVONO essere supportati per la Error Response:

.. list-table::
    :class: longtable
    :widths: 20 20 60
    :header-rows: 1

    * - **Codice di Stato**
      - **Codice di Errore**
      - **Descrizione**
    * - ``400 Bad Request``
      - ``bad_request``
      - La richiesta è malformata, mancano parametri richiesti (ad esempio, parametri di intestazione o asserzione di integrità), o include parametri non validi e sconosciuti.
    * - ``401 Unauthorized``
      - ``unauthorized``
      - La richiesta non può essere soddisfatta in quanto l'autenticazione da parte dell'Utente risulta fallita o non valida.
    * - ``500 Internal Server Error``
      - ``server_error``
      - La richiesta non può essere soddisfatta perché l'Endpoint di Cancellazione ha riscontrato un problema interno. (:rfc:`6749#section-4.1.2.1`).
    * - ``503 Service Unavailable``
      - ``temporarily_unavailable``
      - La richiesta non può essere soddisfatta perché l'Endpoint di Cancellazione è temporaneamente non disponibile (ad esempio, a causa di manutenzione o sovraccarico). (:rfc:`6749#section-4.1.2.1`).


Di seguito è riportato un esempio di Error Response dall'Endpoint di Cancellazione:

.. code-block:: http

  HTTP/1.1 500 Internal Server Error
  Content-Type: application/json

  {
   "error": "server_error",
   "error_description": "The request cannot be fulfilled due to an internal server error."
  }

Alla ricezione di una Error Response, l'Istanza di Wallet che ha effettuato la Richiesta di Cancellazione DEVE informare l'Utente della condizione di errore in modo appropriato.


.. _relying-party-remote-flow-endpoints-considerazioni-di-sicurezza:

Considerazioni di Sicurezza
"""""""""""""""""""""""""""

Tutti gli endpoint della Relying Party DEVONO implementare appropriate misure di sicurezza:

- **Solo HTTPS**: Tutti gli endpoint DEVONO essere accessibili solo tramite HTTPS
- **Protezione Endpoint Mix-up**: Gli URL degli endpoint DEVONO essere attestati da terze parti fidate attraverso la Trust Chain
- **Validazione Input**: Tutti gli endpoint DEVONO convalidare i parametri di input e rifiutare richieste malformate
- **Rate Limiting**: Gli endpoint DOVREBBERO implementare rate limiting per prevenire abusi
- **Audit Logging**: Tutte le interazioni degli endpoint DOVREBBERO essere registrate per il monitoraggio della sicurezza

Per i requisiti di sicurezza dettagliati, vedere :ref:`relying-party-remote-flow-endpoints-considerazioni-di-sicurezza` e i casi di test pertinenti in :ref:`test-plans-remote-presentation:Matrice di Test per il Verificatore di Credenziali in Remoto`.


Note di Implementazione
"""""""""""""""""""""""

- I dettagli di implementazione specifici per la maggior parte degli endpoint sono lasciati alla discrezione della Relying Party
- Gli endpoint DEVONO essere conformi alla specifica OpenID4VP 1.0 per i flussi remoti
- Gli endpoint per flussi di prossimità DEVONO supportare la gestione del ciclo di vita delle App di Verifica
- Tutti gli endpoint DEVONO essere scopribili attraverso l'Entity Configuration della Relying Party
- Le risposte di errore DEVONO seguire i codici di stato HTTP standard e includere appropriate descrizioni degli errori

Per una guida di implementazione completa, fare riferimento alle sezioni degli endpoint individuali e alle matrici di test per i requisiti di validazione.

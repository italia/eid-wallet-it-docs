.. include:: ../common/common_definitions.rst
.. Incluso tramite relying-party-endpoints.rst al livello di titolo '"' (livello 3).

La Relying Party DEVE esporre una serie di endpoint per supportare i flussi di presentazione remoti come definiti in OpenID4VP 1.0. Questi endpoint abilitano la verifica sicura delle credenziali, l'instaurazione della fiducia e l'autenticazione dell'utente per modelli di interazione cross-device e same-device.

.. note::
  I test relativi agli endpoint per flussi remoti della Relying Party sono definiti nella matrice di test per presentazione remota (:ref:`test-plans-remote-presentation:Matrice di Test per il Verificatore di Credenziali in Remoto`).


Endpoint di Federazione
"""""""""""""""""""""""

La Relying Party DEVE fornire la propria Entity Configuration attraverso l'endpoint ``/.well-known/openid-federation``, secondo la Sezione :ref:`infrastructure-trust:Entity Configuration`. Questo endpoint abilita l'instaurazione della fiducia e la scoperta delle capacità della Relying Party.

I dettagli tecnici sono forniti nella Sezione :ref:`relying-party-entity-configuration:Entity Configuration Relying Party`.


Endpoint per Flussi Remoti OpenID4VP
""""""""""""""""""""""""""""""""""""

I seguenti endpoint sono richiesti per i flussi di presentazione remota OpenID4VP 1.0 come descritto in :ref:`remote-flow:Flusso Remoto`. Questi endpoint supportano sia i flussi Same Device che Cross Device:

Endpoint Request URI
....................

L'Endpoint Request URI è dove la Relying Party fornisce il Request Object firmato all'Istanza del Wallet. Questo endpoint supporta sia i metodi GET che POST come definito nella specifica OpenID4VP 1.0.

Per i requisiti di implementazione dettagliati, vedere :ref:`remote-flow:Richiesta all'Endpoint URI Request` e :ref:`remote-flow:Risposta dell'Endpoint URI Request`.


Endpoint Response URI
.....................

L'Endpoint Response URI riceve l'Authorization Response dall'Istanza del Wallet contenente la Verifiable Presentation. Questo endpoint elabora la presentazione e convalida le credenziali.

Per i requisiti di implementazione dettagliati, vedere :ref:`remote-flow:Authorization Response` e :ref:`remote-flow:Risposta della Relying Party`.


Endpoint Status (Opzionale)
...........................

L'Endpoint Status è un endpoint opzionale che consente all'user-agent di monitorare il progresso del flusso di presentazione. Questo endpoint è particolarmente utile per i flussi Same Device dove l'user-agent deve sapere quando l'Istanza del Wallet ha completato la presentazione.

Per i requisiti di implementazione dettagliati, vedere :ref:`remote-flow:Status Endpoint` e :ref:`remote-flow:Errori dello Status Endpoint`.


Richiesta di Cancellazione dei Dati
"""""""""""""""""""""""""""""""""""

L'Istanza del Wallet avvia una richiesta di cancellazione dei dati tramite il contatto di supporto della Relying Party, come specificato in :ref:`user-attribute-deletion:Eliminazione degli Attributi dell'Utente` e in `EUDI-TS 7`_.


Considerazioni di Sicurezza
"""""""""""""""""""""""""""

Tutti gli endpoint della Relying Party DEVONO implementare appropriate misure di sicurezza:

- **Solo HTTPS**: Tutti gli endpoint DEVONO essere accessibili solo tramite HTTPS
- **Protezione Endpoint Mix-up**: Gli URL degli endpoint DEVONO essere attestati da terze parti fidate attraverso la Trust Chain
- **Validazione Input**: Tutti gli endpoint DEVONO convalidare i parametri di input e rifiutare richieste malformate
- **Rate Limiting**: Gli endpoint DOVREBBERO implementare rate limiting per prevenire abusi
- **Audit Logging**: Tutte le interazioni degli endpoint DOVREBBERO essere registrate per il monitoraggio della sicurezza

Per i requisiti di sicurezza dettagliati, vedere :ref:`remote-flow:Flusso Remoto` e i casi di test pertinenti in :ref:`test-plans-remote-presentation:Matrice di Test per il Verificatore di Credenziali in Remoto`.


Note di Implementazione
"""""""""""""""""""""""

- I dettagli di implementazione specifici per la maggior parte degli endpoint sono lasciati alla discrezione della Relying Party
- Gli endpoint DEVONO essere conformi alla specifica OpenID4VP 1.0 per i flussi remoti
- Gli endpoint per flussi di prossimità DEVONO supportare la gestione del ciclo di vita delle App di Verifica
- Tutti gli endpoint DEVONO essere scopribili attraverso l'Entity Configuration della Relying Party
- Le risposte di errore DEVONO seguire i codici di stato HTTP standard e includere appropriate descrizioni degli errori

Per una guida di implementazione completa, fare riferimento alle sezioni degli endpoint individuali e alle matrici di test per i requisiti di validazione.



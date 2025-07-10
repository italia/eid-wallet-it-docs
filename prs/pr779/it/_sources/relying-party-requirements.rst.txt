.. include:: ../common/common_definitions.rst

Requisiti della Soluzione di Relying Party
------------------------------------------

Questa sezione elenca i requisiti che devono essere soddisfatti dalle Relying Party e dalle Soluzioni di Relying Party.

La seguente tabella elenca i requisiti con un identificatore univoco.

.. list-table::
    :class: longtable
    :widths: 20 80
    :header-rows: 1

    * - **ID**
      - **Requisito**

    * - RP-1
      - La Relying Party DEVE registrarsi presso l'Autorità di Federazione per ottenere sia il Certificato di Accesso che il Certificato di Registrazione.
    * - RP-2
      - La Relying Party DEVE implementare meccanismi sicuri per la gestione e l'elaborazione delle Credenziali Elettroniche ricevute, garantendo l'integrità e la riservatezza della Soluzione di Relying Party.
    * - RP-3
      - La Relying Party DEVE esporre un endpoint per la cancellazione degli attributi personali presentati dagli Utenti ogni volta che gli Attestati Elettronici richiesti dalla Relying Party includono un identificativo univoco dell'Utente (ad esempio, l'attributo "tax_id_code" dell'Attestato Elettronico di Dati di Identificazione Personale).
    * - RP-4
      - La Soluzione di Relying Party DEVE implementare procedure adeguate di revoca per le App di Verifica compromesse o dismesse.
    * - RP-5
      - La Soluzione di Relying Party DEVE mantenere una traccia di audit delle verifiche eseguite sugli Attestati Elettronici che le sono stati presentati nel rispetto dei requisiti di privacy e delle normative sulla protezione dei dati.
    * - RP-6
      - La Soluzione di Relying Party DEVE consentire l'uso della Divulgazione Selettiva durante la fase di presentazione degli attributi negli Attestati Elettronici.
    * - RP-7
      - Il Backend della Relying Party DEVE fornire un insieme di API RESTful per la registrazione delle App di Verifica e il rilascio dei Certificati di Accesso.
    * - RP-8
      - L'App di Verifica DEVE periodicamente ristabilire la trust con la Relying Party attraverso controlli di integrità e procedure di rinnovo del Certificato di Accesso.
    * - RP-9
      - L'App di Verifica DEVE fornire sia un Certificato di Registrazione che un Certificato di Accesso alle Istanze del Wallet durante la loro interazione per dimostrare la legittimità e l'autorizzazione delle sue richieste.
    * - RP-10
      - L'App di Verifica DEVE comunicare agli Utenti quali attributi vengono richiesti e per quale scopo durante qualsiasi flusso di presentazione degli Attestati Elettronici.
    * - RP-11
      - Le App di Verifica Mobile DEVONO essere compatibili e funzionali sia sui sistemi operativi Android che iOS e disponibili rispettivamente sul Play Store e sull'App Store.
    * - RP-12
      - Le App di Verifica Mobile DEVONO gestire scenari di presentazione sia online che offline, con misure di sicurezza e notifiche utente appropriate.

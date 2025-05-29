.. include:: ../common/common_definitions.rst

Requisiti della Soluzione di Relying Party
------------------------------------------

Questa sezione elenca i requisiti che devono essere soddisfatti dalle Relying Party e dalle Soluzioni di Relying Party.

- La Relying Party DEVE registrarsi presso l'Autorità di Federazione per ottenere sia il Certificato di Accesso che il Certificato di Registrazione.
- La Relying Party DEVE implementare meccanismi sicuri per la gestione e l'elaborazione delle Credenziali Elettroniche ricevute, garantendo l'integrità e la riservatezza della Soluzione di Relying Party.
- La Relying Party DEVE esporre un endpoint per la cancellazione degli attributi personali presentati dagli Utenti ogni volta che gli Attestati Elettronici richiesti dalla Relying Party includono un identificativo univoco dell'Utente (ad esempio, l'attributo "tax_id_code" dell'Attestato Elettronico di Dati di Identificazione Personale).
- La Soluzione di Relying Party DEVE implementare procedure adeguate di revoca per le App di Verifica compromesse o dismesse.
- La Soluzione di Relying Party DEVE mantenere una traccia di audit delle verifiche eseguite sigli Attestati Elettronici che le sono stati presentati nel rispetto dei requisiti di privacy e delle normative sulla protezione dei dati.
- La Soluzione di Relying Party DEVE consentire l'uso della Divulgazione Selettiva durante la fase di presentazione degli attributi negli Attestati Elettronici .
- Il Backend della Relying Party DEVE fornire un insieme di API RESTful per la registrazione delle App di Verifica e il rilascio dei Certificati di Accesso.
- L'App di Verifica DEVE periodicamente ristabilire la trust con la Relying Party attraverso controlli di integrità e procedure di rinnovo del Certificato di Accesso.
- L'App di Verifica DEVE fornire sia un Certificato di Registrazione che un Certificato di Accesso alle Istanze del Wallet durante la loro interazione per dimostrare la legittimità e l'autorizzazione delle sue richieste.
- L'App di Verifica DEVE comunicare agli Utenti quali attributi vengono richiesti e per quale scopo durante qualsiasi flusso di presentazione degli Attestati Elettronici.
- Le App di Verifica Mobile DEVONO essere compatibili e funzionali sia sui sistemi operativi Android che iOS e disponibili rispettivamente sul Play Store e sull'App Store.
- Le App di Verifica Mobile DEVONO gestire scenari di presentazione sia online che offline, con misure di sicurezza e notifiche utente appropriate.

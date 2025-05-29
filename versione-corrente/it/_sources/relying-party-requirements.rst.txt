.. include:: ../common/common_definitions.rst

Requisiti della Soluzione di Relying Party
------------------------------------------

Questa sezione elenca i requisiti che devono essere soddisfatti dalle Relying Party e dalle Soluzioni di Relying Party.

- La Relying Party DEVE registrarsi presso l'Autorità di Federazione per ottenere sia il Certificato di Accesso che il Certificato di Registrazione.
- La Relying Party DEVE implementare meccanismi sicuri per la gestione e l'elaborazione delle Credenziali Elettroniche ricevute, garantendo l'integrità e la riservatezza della Soluzione di Relying Party.
- La Relying Party DEVE esporre un endpoint per la cancellazione degli attributi personali presentati dagli Utenti ogni volta che gli attributi richiesti dalla Relying Party includono un identificativo univoco dell'Utente (ad esempio, l'attributo "tax_id_code" dell'Attestato Elettronico di Dati di Identificazione Personale).
- La Soluzione di Relying Party DEVE implementare procedure adeguate di revoca per le istanze compromesse o dismesse.
- La Soluzione di Relying Party DEVE mantenere una traccia di audit delle verifiche delle Credenziali nel rispetto dei requisiti di privacy e delle normative sulla protezione dei dati.
- La Soluzione di Relying Party DEVE consentire meccanismi di Divulgazione Selettiva durante gli scenari di presentazione.
- Il Backend della Relying Party DEVE fornire un insieme di servizi RESTful per la registrazione delle Istanze di Relying Party e il rilascio dei Certificati di Accesso.
- L'Istanza di Relying Party DEVE periodicamente ristabilire la fiducia con la Relying Party attraverso controlli di integrità e procedure di rinnovo del Certificato.
- L'Istanza di Relying Party DEVE fornire sia un Certificato di Registrazione che un Certificato di Accesso alle Istanze del Wallet durante la loro interazione per dimostrare la legittimità e l'autorizzazione delle sue richieste.
- L'Istanza di Relying Party DEVE comunicare agli Utenti quali attributi vengono richiesti e per quale scopo durante qualsiasi flusso di presentazione della Credenziale.
- Le Istanze di Relying Party Mobile DEVONO essere compatibili e funzionali sia sui sistemi operativi Android che iOS e disponibili rispettivamente sul Play Store e sull'App Store.
- Le Istanze di Relying Party Mobile DEVONO gestire scenari di presentazione sia online che offline, con misure di sicurezza e notifiche utente appropriate.

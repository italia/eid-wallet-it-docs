Operazioni di Gestione dei Certificati X.509
=============================================

Questa sezione definisce le procedure operative per la gestione dei Certificati X.509 all'interno della federazione IT-Wallet, coprendo l'analisi delle catene di Certificati X.509, le procedure di validazione e la verifica di revoca. Queste procedure completano i processi di onboarding della federazione e supportano la gestione continua del ciclo di vita dei Certificati X.509 per tutti i partecipanti.

Per l'infrastruttura PKI X.509 fondamentale e le procedure di emissione dei certificati, vedere :ref:`trust-infrastructure-pki-x509`.

Architettura PKI della Federazione
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

La federazione IT-Wallet opera con un'infrastruttura a chiave pubblica gerarchica dove:

	- **Trust Anchor**: Agisce come Autorità di Certificazione X.509 Root dove i Certificati X.509 CA NON DEVONO superare il **periodo di validità di 5 anni**.
	- **Certificato X.509 dell'Entità Federata**: Ogni partecipante della federazione riceve un certificato X.509 che opera come sub-CA limitata dove i Certificati X.509 NON DEVONO superare il **periodo di validità di 2 anni**.
	- **Certificati X.509 del Protocollo**: Certificati X.509 auto-emessi per servizi interni dove i Certificati X.509 NON DOVREBBERO superare il **periodo di validità di 1 anno**.

Ogni entità federata DEVE esporre il proprio Certificato X.509 dell'Entità Federata su un endpoint pubblicamente accessibile. La chiave privata dell'Entità Federata serve a scopi duali:

	1. Auto-emissione di Certificati X.509 del Protocollo per operazioni crittografiche interne (capacità sub-CA limitata).
	2. Agire come Chiave dell'Entità Federata per la firma delle Dichiarazioni dell'Entità.

.. note:: 
  Le Foglie della Federazione possono SOLO emettere Certificati X.509 su se stesse e per scopi specifici dell'applicazione. Le Foglie della Federazione NON DEVONO emettere Certificati X.509 per altre entità federate, come limitato dalle loro Autorità Federali utilizzando l'estensione X.509 Name Constraints.

Per i Certificati X.509 specifici del protocollo, con periodi di validità superiori a 24 ore, l'entità emittente DEVE pubblicare e aggiornare regolarmente una Lista di Revoca dei Certificati X.509 (CRL) su un endpoint pubblicamente accessibile.

Struttura e Analisi della Catena di Certificati X.509
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Le entità federate ricevono catene di Certificati X.509 durante il processo di onboarding. Le entità federate DEVONO validare queste catene su se stesse.


Visualizzazione della Catena di Certificati X.509
"""""""""""""""""""""""""""""""""""""""""""""""""""

Il seguente script consente alle entità federate di:

	- Estrarre i dettagli dei certificati X.509 per la verifica.
	- Analizzare le estensioni e i vincoli dei certificati X.509.
	- Verificare la gerarchia e le relazioni dei certificati X.509

.. literalinclude:: ../../utils/certificate-chain-analysis.sh
   :language: bash
   :caption: Script di analisi della catena di Certificati X.509


Validazione della Catena di Certificati X.509
"""""""""""""""""""""""""""""""""""""""""""""

Le entità federate DEVONO validare le catene di certificati X.509 per garantire l'instaurazione corretta della fiducia e verificare la conformità con i requisiti PKI della federazione.

Un esempio non normativo della procedura di validazione della catena di Certificati X.509 è fornito di seguito:

.. literalinclude:: ../../utils/certificate-chain-validation.sh
   :language: bash
   :caption: Script di validazione della catena di Certificati X.509


Le entità federate DOVREBBERO verificare:

	1. **Firme dei Certificati X.509**: Ogni Certificato X.509 DEVE essere correttamente firmato dal suo emittente.
	2. **Integrità della Catena di Certificati X.509**: Le relazioni Emittente-Soggetto DEVONO essere valide in tutta la catena di Certificati X.509.
	3. **Periodi di Validità dei Certificati X.509**: Tutti i Certificati X.509 DEVONO essere entro i loro periodi di validità e DEVONO conformarsi ai limiti della federazione.
	4. **Estensioni dei Certificati X.509**: I Vincoli di Base e l'Uso della Chiave DEVONO conformarsi ai requisiti della federazione:

		- Certificati X.509 dell'Entità Federata: ``CA:TRUE, pathlen:0`` (può solo emettere certificati su se stessa).
		- Certificati X.509 del Protocollo: ``CA:FALSE`` (non può emettere certificati).

Gestione della Revoca dei Certificati X.509
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Le entità federate DEVONO implementare la verifica di revoca dei Certificati X.509 per garantire la validazione continua della fiducia e la conformità con i requisiti di sicurezza della federazione.

Distribuzione e Accesso CRL
""""""""""""""""""""""""""""

Le autorità federali pubblicano Liste di Revoca dei Certificati X.509 (CRL) su endpoint pubblicamente accessibili. Le entità federate DEVONO essere in grado di accedere e processare queste distribuzioni CRL per la verifica di revoca.

La seguente procedura consente alle entità federate di:

	- Localizzare gli endpoint di distribuzione CRL dai Certificati X.509.
	- Scaricare le liste di revoca correnti.
	- Analizzare il contenuto CRL e i periodi di validità.

.. literalinclude:: ../../utils/crl-analysis.sh
   :language: bash


Verifica della Revoca dei Certificati X.509
"""""""""""""""""""""""""""""""""""""""""""

Le entità federate DEVONO verificare lo stato di revoca dei certificati X.509 controllando i numeri seriali dei certificati X.509 contro le Liste di Revoca dei Certificati X.509 correnti.

Le entità federate DOVREBBERO implementare controlli di revoca automatizzati per:

	- **Certificati X.509 dell'Entità Federata**: Verificare periodicamente lo stato del proprio certificato X.509.
	- **Certificati X.509 delle Entità Peer**: Validare i Certificati X.509 di altri partecipanti della federazione.
	- **Validazione della Catena di Fiducia**: Garantire che intere catene di certificati X.509 rimangano valide.

Di seguito è fornito un esempio non normativo di script bash per la verifica dello stato di revoca dei certificati X.509:

.. literalinclude:: ../../utils/certificate-revocation-verification.sh
   :language: bash


Migliori Pratiche per la Gestione dei Certificati X.509
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Integrazione della Validazione dei Certificati X.509
"""""""""""""""""""""""""""""""""""""""""""""""""""""

Le entità federate DOVREBBERO integrare le procedure di validazione dei Certificati X.509 nelle loro operazioni standard della federazione:

	1. **Aggiornamenti della Configurazione dell'Entità**: Verificare le catene di Certificati X.509 quando si processano gli authority hints e gli aggiornamenti dei Certificati X.509.
	2. **Costruzione della Catena di Fiducia**: Validare tutti i Certificati X.509 durante le procedure di costruzione della catena di fiducia.
	3. **Operazioni PKI X.509**: Eseguire controlli di revoca dei Certificati X.509 utilizzando gli endpoint CRL.
	4. **Gestione dei Certificati del Protocollo**: Validare il Certificato X.509 specifico del protocollo auto-emesso per i servizi interni.
	5. **Validazione Periodica**: Implementare programmi regolari di validazione dei Certificati X.509 e CRL.

Diagnostica e Risoluzione dei Problemi
"""""""""""""""""""""""""""""""""""""""

Le entità federate DEVONO implementare procedure diagnostiche per identificare e risolvere problemi relativi ai Certificati X.509:

  - **Validazione dei Certificati X.509**, inclusi:

    - **Discrepanze dell'Identificatore della Chiave dell'Autorità**: L'Identificatore della Chiave dell'Autorità CRL non corrisponde all'Identificatore della Chiave del Soggetto del Trust Anchor.
    - **Rotazione del Certificato X.509 del Trust Anchor**: Certificato X.509 del Trust Anchor obsoleto che causa fallimenti di validazione.
    - **Problemi del Formato del Numero Seriale**: Problemi di normalizzazione del numero seriale nel controllo di revoca.

  - **Fallimento della Validazione CRL**: Quando la validazione CRL fallisce, le entità federate DOVREBBERO:

    1. **Verificare il Certificato X.509 del Trust Anchor**: Garantire che venga utilizzato il certificato X.509 del Trust Anchor corrente.
    2. **Controllare l'Identificatore della Chiave dell'Autorità**: Confrontare l'Identificatore della Chiave dell'Autorità CRL con l'Identificatore della Chiave del Soggetto del Trust Anchor.
    3. **Validare la Firma CRL**: Verificare che la CRL sia correttamente firmata dall'autorità emittente prevista.
    4. **Aggiornare il Certificato X.509 del Trust Anchor**: Scaricare il certificato X.509 del Trust Anchor aggiornato se è avvenuta una rotazione.

  - **Verifica dell'Accessibilità degli Endpoint**: Le entità federate DOVREBBERO implementare test di connettività per gli endpoint dell'infrastruttura dei certificati.


Il seguente esempio non normativo fornisce uno script per il test di connettività dell'infrastruttura dei certificati X.509 della Federazione:

.. literalinclude:: ../../utils/federation-connectivity-test.sh
   :language: bash


Coordinamento del Ciclo di Vita dei Certificati X.509
"""""""""""""""""""""""""""""""""""""""""""""""""""""

Le entità federate DEVONO coordinare la gestione dei Certificati X.509 con le procedure del ciclo di vita della federazione seguendo i periodi di validità stabiliti:

- **Rinnovo dei Certificati X.509**: Allineare i rinnovi dei certificati X.509 con gli aggiornamenti della Configurazione dell'Entità e i cicli di aggiornamento dei Trust Mark, secondo i limiti della federazione definiti in :ref:`x5c-evaluation:Architettura PKI della Federazione`.
- **Rotazione delle Chiavi**: Coordinare la rotazione della Chiave dell'Entità Federata con le procedure di rinnovo dei certificati X.509.
- **Gestione CRL**: Per i Certificati X.509 del Protocollo con validità > 24 ore, mantenere la pubblicazione CRL corrente.
- **Uscita dalla Federazione**: Garantire la revoca corretta dei Certificati X.509 durante l'uscita volontaria o avviata dall'organo di supervisione dalla federazione.


Procedure di Rotazione delle Chiavi
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Le entità federate DEVONO implementare meccanismi di rotazione delle chiavi per mantenere la postura di sicurezza e rispondere agli eventi di sicurezza. Questa sezione definisce le procedure operative per rilevare e rispondere alle rotazioni delle chiavi superiori e per il rinnovo delle chiavi subordinate.

Rotazione delle Chiavi Superiori
"""""""""""""""""""""""""""""""""""""

Le entità subordinate DEVONO eseguire la verifica periodica della propria Trust Chain per rilevare le rotazioni delle chiavi superiori e garantire la continuità dell'appartenenza alla federazione.

**Requisiti di Verifica**

I Subordinati della federazione DEVONO:

1. Recuperare il proprio Subordinate Statement dal superiore immediato ogni 24 ore utilizzando il fetch endpoint definito in :ref:`trust-infrastructure-endpoint-delle-api-della-federazione`. Ciò DOVREBBE essere fatto entro un intervallo di tempo non superiore a 24 ore.
2. Verificare lo stato di revoca o sospensione.
3. Aggiornare il proprio Entity Configuration quando cambiano i certificati superiori.

**Meccanismi di Rilevamento**

I Subordinati POSSONO utilizzare uno o più dei seguenti meccanismi per rilevare le modifiche:

- **Verifica CRL/OCSP**: Monitorare le Certificate Revocation List o le risposte del protocollo Online Certificate Status Protocol per rilevare la revoca dei certificati superiori come definito in :ref:`trust-infrastructure-revoca-dei-certificati-x509`. La revoca del certificato indica che è in corso la rotazione della chiave superiore.
- **Fetch Endpoint**: Recuperare il Subordinate Statement tramite ``GET {superiore}/fetch?sub={entity_id_subordinato}`` per ottenere i certificati correnti.
- **Events Endpoint**: Monitorare ``GET {superiore}/federation_subordinate_events_endpoint?sub={entity_id_subordinato}`` per gli eventi ``jwks_update``. Il Federation Subordinate Events endpoint restituisce la traccia storica degli eventi di registrazione come definito in :ref:`trust-infrastructure-endpoint-delle-api-della-federazione`.

I Subordinati DOVREBBERO implementare la pianificazione automatizzata per:

- Operazioni di fetch giornaliere per recuperare il Subordinate Statement corrente.
- Validazione della catena di certificati X.509 dopo ogni fetch.
- Aggiornamenti automatici dell'Entity Configuration quando vengono rilevate modifiche ai certificati.
- Monitoraggio degli eventi per il rilevamento proattivo delle modifiche.

Quando un'entità superiore (Trust Anchor o Intermediate) ruota la propria Chiave dell'Entità Federata, tutti i certificati X.509 Subordinati DEVONO essere riemessi.

**Procedura di Rotazione**

1. **Revoca della Chiave**: Il superiore pubblica la Certificate Revocation List (CRL) o la voce Historical Keys (HK) revocando la vecchia chiave come definito in :ref:`trust-infrastructure-revoca-dei-certificati-x509`.
2. **Aggiornamento Entity Configuration**: Il superiore pubblica la nuova Entity Configuration firmata con la nuova Chiave dell'Entità Federata.
3. **Riemissione Certificati X.509**: Il superiore riemette i certificati X.509 a tutti i Subordinati utilizzando la nuova chiave.
4. **Pubblicazione Certificati**: Il superiore rende disponibili i nuovi certificati sul fetch endpoint.
5. **Rilevamento Subordinato**: I Subordinati rilevano la modifica al successivo fetch programmato (al massimo entro 24 ore dalla pubblicazione della modifica).
6. **Aggiornamento Certificati**: I Subordinati aggiornano il campo ``x5c`` nella propria Entity Configuration con il nuovo certificato.

**Priorità dei Certificati**

Quando esistono più certificati X.509 per la stessa chiave pubblica subordinata, il certificato nel Subordinate Statement DEVE avere priorità sul certificato nella Entity Configuration del subordinato.

.. note::
  Un'entità superiore non può avviare autonomamente un processo di rotazione delle Chiavi Subordinate. Il meccanismo di rotazione delle Chiavi Subordinate è sempre avviato dall'entità Subordinata, vedi Sezione :ref:`x5c-evaluation:Rotazione delle Chiavi Subordinate`.

Rotazione delle Chiavi Subordinate
"""""""""""""""""""""""""""""""""""

I Subordinati ruotano le proprie Chiavi dell'Entità Federata inviando Certificate Signing Request al proprio superiore immediato seguendo la stessa procedura dell'onboarding iniziale.

**Procedura di Rotazione**

1. **Generazione Nuova Chiave**: Il subordinato genera una nuova coppia di Chiavi dell'Entità Federata.
2. **Generazione CSR**: Il subordinato genera un Certificate Signing Request PKCS #10 per la nuova chiave come definito in :ref:`entity-onboarding:Onboarding delle Entità`.
3. **Invio CSR**: Il subordinato invia il CSR all'entità superiore utilizzando lo stesso endpoint di onboarding.
4. **Emissione Certificato**: Il superiore valida il CSR ed emette un nuovo certificato X.509.
5. **Pubblicazione Certificato**: Il superiore rende disponibile il nuovo certificato sul fetch endpoint.
6. **Recupero Certificato**: Il subordinato recupera il Subordinate Statement aggiornato contenente il nuovo certificato.
7. **Aggiornamento Entity Configuration**: Il subordinato aggiunge la nuova JWK con il nuovo certificato all'array ``jwks`` della Entity Configuration.

.. note::
   Durante la rotazione delle chiavi, i Subordinati DOVREBBERO mantenere sia le chiavi vecchie che quelle nuove per garantire la continuità del servizio. La vecchia chiave DOVREBBE essere rimossa solo dopo aver confermato la corretta propagazione della nuova chiave in tutta la federazione.


Gestione del Ciclo di Vita dell'Entità
--------------------------------------

Questa sezione fornisce le procedure di implementazione tecnica per la gestione del ciclo di vita dell'entità. Per i concetti di alto livello del ciclo di vita e i processi aziendali, vedere :ref:`onboarding-high-level:Gestione del Ciclo di Vita delle Entità`.

Mentre l'aggiornamento dei dati amministrativi DEVE seguire processi di governance che sono fuori dall'ambito di questa specifica tecnica, gli aggiornamenti della configurazione tecnica sono descritti nelle seguenti sezioni.

Aggiornamenti della Configurazione Tecnica
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gli aggiornamenti tecnici che influenzano le operazioni del protocollo della federazione DEVONO seguire procedure specifiche per:

  - **Rinnovo dei Certificati X.509**

    1. **Preparazione Pre-rinnovo**: L'Entità DEVE generare un nuovo CSR con informazioni aggiornate del certificato X.509.
    2. **Richiesta di Rinnovo**: L'Entità DEVE inviare la richiesta di rinnovo con il nuovo CSR seguendo la stessa procedura tecnica dell'onboarding iniziale.
    3. **Integrazione del Certificato X.509**: L'Entità DEVE aggiornare la sua Configurazione dell'Entità con la nuova catena di certificati X.509 nel parametro ``x5c``.
    4. **Validazione della Catena di Fiducia**: L'Entità DEVE verificare la Catena di Fiducia aggiornata attraverso l'endpoint ``/resolve``.
    5. **Aggiornamento del Registro**: L'Entità DOVREBBE confermare le informazioni dell'entità aggiornate nell'endpoint ``/list`` del Trust Anchor.

  - **Rotazione delle Chiavi**

    1. **Attivazione della Chiave**: In caso di incidente o rotazione pianificata, l'Entità DEVE attivare una Chiave dell'Entità di Federazione alternativa per le operazioni di firma.
    2. **Generazione di Nuova Chiave**: L'Entità DEVE generare una nuova coppia di Chiave Pubblica dell'Entità di Federazione per servire come chiave aggiuntiva.
    3. **Pubblicazione Parallela delle Chiavi**: L'Entità DEVE pubblicare tutte le chiavi disponibili nella claim ``jwks`` della Configurazione dell'Entità durante il periodo di transizione.
    4. **Richiesta di Certificato X.509**: L'Entità DEVE richiedere un nuovo certificato X.509 per la nuova chiave seguendo la procedura standard.
    5. **Migrazione Graduale**: L'Entità DEVE aggiornare la Configurazione dell'Entità per utilizzare la chiave attivata per la firma mantenendo tutte le chiavi per la verifica.
    6. **Deprecazione della Chiave Vecchia**: L'Entità DEVE rimuovere la vecchia chiave dalla Configurazione dell'Entità dopo il periodo di validazione, mantenendo la chiave alternativa e la nuova chiave.

  - **Aggiornamenti dei Metadati**

    - **Modifiche degli Endpoint**: L'Entità PUÒ aggiornare gli endpoint di servizio nei metadati specifici dell'entità.
    - **Aggiornamenti delle Capacità**: L'Entità PUÒ modificare i protocolli supportati, gli algoritmi o le capacità di servizio entro i vincoli definiti da questo profilo di implementazione IT-Wallet.



Tutti gli aggiornamenti tecnici DEVONO essere validati attraverso:

  1. **Validazione della Configurazione dell'Entità**: L'Entità DEVE verificare la struttura e il contenuto della EC aggiornata.
  2. **Risoluzione della Catena di Fiducia**: L'Entità DEVE confermare che l'endpoint ``/resolve`` restituisca una Catena di Fiducia valida.
  3. **Stato della Federazione**: L'Entità DEVE verificare lo stato operativo dell'entità nel registro della federazione.
  4. **Test di Integrazione**: L'Entità DOVREBBE testare le operazioni del protocollo della federazione con la configurazione aggiornata.

Procedure Tecniche di Uscita dalla Federazione
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Per il contesto aziendale sui processi di uscita dalla federazione, vedere :ref:`onboarding-high-level:Processi di Uscita e Rimozione dalla Federazione`. Questa sezione copre le procedure di implementazione tecnica.

Uscita Volontaria - Disattivazione Tecnica
""""""""""""""""""""""""""""""""""""""""""""

  1. **Richiesta di Revoca del Certificato X.509**: L'Entità DEVE inviare una richiesta di revoca del Certificato X.509 all'Autorità Federata con il motivo della revoca. La richiesta DEVE essere firmata con la Chiave Privata dell'Entità Federata corrispondente al Certificato X.509 che viene revocato per dimostrare la legittimità della richiesta di revoca.
  2. **Verifica dell'Aggiornamento CRL**: L'Autorità Federata DEVE revocare il Certificato X.509 dell'Entità e l'Entità DEVE verificare che appaiano nella Lista di Revoca dei Certificati X.509 aggiornata.
  3. **Rimozione della Dichiarazione Subordinata**: L'Autorità Federata DEVE rimuovere completamente la Dichiarazione Subordinata dell'Entità dal Registro della Federazione per prevenire qualsiasi validazione del rapporto di fiducia, e quindi rimuovere qualsiasi riferimento a quella Entità nell'endpoint di elenco, endpoint di risoluzione o endpoint di elenco con trust mark.
  4. **Disattivazione della Configurazione dell'Entità**: L'Entità DEVE disattivare la sua Configurazione dell'Entità. L'Entità PUÒ:

     a. Rimuovere completamente la Configurazione dell'Entità dall'endpoint ``/.well-known/openid-federation`` (restituendo HTTP 404), OPPURE
     b. Mantenere la Configurazione dell'Entità come scaduta (con la claim ``exp`` nel passato). Pertanto NON DEVE aggiornarla con timestamp freschi.

  5. **Aggiornamento dello Stato del Registro**: L'Entità DOVREBBE verificare la rimozione dal Registro della Federazione, verificando anche lo stato del Trust Mark utilizzando l'endpoint dello Stato del Trust Mark. 

Esempio non normativo di richiesta di revoca del Certificato X.509 seguendo il formato :rfc:`3280`:

.. code-block:: text

   Richiesta di Revoca del Certificato X.509:
   Soggetto: CN=credentials.example.gov, OU=Digital Credentials, O=Example Organization, L=Roma, ST=Lazio, C=IT, emailAddress=technical@credentials.example.gov
   Numero Seriale del Certificato X.509: 987654321
   Motivo della Revoca: cessation_of_operation (5)
   Data di Revoca: 2025-12-31T23:59:59Z

   Richiesta firmata con la Chiave Privata dell'Entità Federata corrispondente a:
   Algoritmo della Chiave Pubblica: id-ecPublicKey
   OID ASN1: prime256v1
   CURVA NIST: P-256
   ID Chiave: NsXymfIILEPR5Y0t

   Nota: La CRR DEVE essere firmata con la stessa chiave privata che corrisponde al
   certificato X.509 che viene revocato per autenticare la richiesta di revoca.

Esempio CRR in formato DER (codificato Base64):

.. code-block:: text

   -----BEGIN CERTIFICATE REVOCATION REQUEST-----
   MIIBVjCB/wIBADBpMQswCQYDVQQGEwJJVDEOMAwGA1UECAwFTGF6aW8xDTALBgNV
   BAcMBFJvbWExGjAYBgNVBAoMEUV4YW1wbGUgT3JnYW5pemF0aW9uMR8wHQYDVQQD
   DBZjcmVkZW50aWFscy5leGFtcGxlLmdvdjBZMBMGByqGSM49AgEGCCqGSM49AwEH
   A0IABIBgZ4HBgUCNXwY5LJSlKzm7gXY4FApFJCj91Gpb1K9GEIouTq2X3L0K64Iq
   0ob4l_gslT14644zbYXYF-xmw7aPdlbMuw3T1URwI4nafMtKrYwDQYJKoZIhvcNAQ
   kEAwIJrRLl1VR987654321gBgJKwYBBQUHAgEWHGh0dHBzOi8vZXhhbXBsZS5vcmcv
   cG9saWN5MAoGCCqGSM49BAMCA0gAMEUCIQC9h3Y6hFgd7zUzZyBrQ3jJ8HmVF2Qa
   -----END CERTIFICATE REVOCATION REQUEST-----

Rimozione da Parte dell'Organo di Supervisione - Implementazione Tecnica
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

  1. **Revoca di Emergenza del Certificato X.509**: L'Autorità Federata DEVE revocare immediatamente il Certificato X.509 con il codice di motivo appropriato (ad es., "Key Compromise", "Cessation of Operation").
  2. **Aggiornamento di Emergenza CRL**: Il Trust Anchor DEVE pubblicare la CRL aggiornata entro il tempo di emergenza.
  3. **Rimozione della Dichiarazione Subordinata**: L'Autorità Federata DEVE interrompere immediatamente l'emissione delle Dichiarazioni Subordinate dell'Entità utilizzando l'endpoint fetch, e/o qualsiasi riferimento a quella Entità utilizzando l'endpoint di elenco, o l'endpoint di elenco con trust mark, o l'endpoint di risoluzione.
  4. **Invalidazione della Configurazione dell'Entità**: La Configurazione dell'Entità in ``/.well-known/openid-federation`` diventa invalida a causa della revoca del Certificato X.509 (la verifica della firma fallisce).
  5. **Invalidazione della Catena di Fiducia**: La risoluzione della Catena di Fiducia DEVE restituire uno stato di errore per l'entità interessata.
  6. **Isolamento degli Endpoint di Servizio**: L'infrastruttura della federazione DEVE bloccare l'accesso agli endpoint di servizio della federazione.

Esempio di verifica di revoca di emergenza:

.. code-block:: bash

   # Controlla l'aggiornamento di emergenza CRL
   curl -o emergency.crl https://trust-anchor.eid-wallet.example.it/pki/ta-sub.crl
   openssl crl -in emergency.crl -text -noout | grep "Last Update"
   
   # Verifica che la risoluzione della Catena di Fiducia fallisca
   curl "https://trust-anchor.eid-wallet.example.it/resolve?sub=https%3A//suspended-entity.example.it&trust_anchor=https%3A//trust-registry.eid-wallet.example.it"
   # Previsto: HTTP 404 o risposta di errore specifica

**Modifiche Tecniche a Livello di Componente**

Componenti tecnici specifici POSSONO essere modificati mantenendo l'appartenenza alla federazione:

.. code-block:: json

   {
     "iss": "https://ci.example.it",
     "sub": "https://ci.example.it",
     "jwks": { 
       // contenuto jwks
     },
     "metadata": {
       "openid_credential_issuer": {
         "credential_endpoint": "https://ci.example.it/credential",
         "credentials_supported": [ ]
         // rimosso: "batch_credential_endpoint" per manutenzione
       }
     }
   }

L'Entità DEVE seguire questi passaggi per le modifiche dei componenti:

1. **Aggiornamento della Configurazione dell'Entità**: L'Entità DEVE modificare i metadati per riflettere le modifiche dei componenti.
2. **Rivalidazione della Catena di Fiducia**: L'Entità DEVE verificare la configurazione aggiornata attraverso l'endpoint ``/resolve``.
3. **Test del Servizio**: L'Entità DOVREBBE testare le operazioni del protocollo della federazione rimanenti.
4. **Verifica del Registro**: L'Entità DOVREBBE confermare le capacità aggiornate nel registro della federazione.

**Obblighi Tecnici Post-Uscita**

Le entità che escono dalla federazione DEVONO mantenere quanto segue per la conformità normativa:

1. **Configurazione Storica dell'Entità**: L'Entità DEVE mantenere l'accessibilità dell'endpoint ``/.well-known/openid-federation`` per scopi di audit.
2. **Archivio della Catena di Certificati X.509**: L'Entità DEVE mantenere le catene di Certificati X.509 accessibili per la verifica delle Credenziali esistenti (minimo 7 anni).
3. **Conservazione dei Log di Audit**: L'Entità DEVE archiviare i log del protocollo della federazione per i requisiti normativi.

.. include:: ../common/common_definitions.rst

Come leggere le Specifiche
--------------------------

Questa specifica è progettata per soddisfare i requisiti di molteplici stakeholder all'interno dell'ecosistema IT-Wallet. Ogni ruolo ha responsabilità e ambiti diversi e diverse esigenze informative. Questa sezione fornisce percorsi di lettura personalizzati per aiutare il lettore a navigare in modo efficiente verso i contenuti più rilevanti per gli obiettivi di implementazione.

Panoramica della Struttura delle Specifiche
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

La specifica è organizzata nelle seguenti sezioni principali:

**Sezione** :ref:`introduction:Introduzione`: 
  Stabilisce l'ambito e il linguaggio normativo per l'ecosistema IT-Wallet.

**Sezione** :ref:`architecture-overview:Panoramica dell'Architettura`:
  Fornisce una visione di alto livello dell'Architettura, in termini di governance e processi operativi abilitati.

**Sezione** :ref:`brand-identity:Brand Identity`:
  Fornisce i requisiti relativi alla Brand Identity del Sistema IT-Wallet, le indicazioni relative al naming e all'applicazione degli elementi visivi che identificano l'ecosistema.

**Sezione** :ref:`functionalities:Design dell'Esperienza Utente`: 
  Fornisce i principi di design e i requisiti funzionali di alto livello per garantire un’Esperienza Utente di qualità in tutte le fasi di interazione tra l’Utente e il servizio. 

**Sezione** :ref:`trust-infrastructure:L'Infrastruttura di Trust`:
  Definisce il modello di trust basato sulla federazione, le relazioni tra entità e i meccanismi di valutazione della fiducia che proteggono l'intero ecosistema.

**Sezione** :ref:`entities:Entità`: 
  Requisiti di implementazione completi per ogni partecipante all'ecosistema: Soluzioni Wallet, Fornitori di Credenziali, Relying Party e Fonti Autentiche, inclusi i loro componenti, modelli di interazione e requisiti di configurazione.

**Sezione** :ref:`digital-credential-management:Gestione degli Attestati Elettronici`: 
  Copre i modelli di dati e i formati delle Credenziali Elettroniche, la gestione del ciclo di vita, la verifica della validità e la struttura del catalogo delle Credenziali.

**Sezione** :ref:`digital-credential-flows:Flussi relativi agli Attestati Elettronici`:
  Guida dettagliata all'implementazione per i flussi di emissione e presentazione delle Credenziali Elettroniche, inclusi i flussi di interazione remota e di prossimità.

**Sezione** :ref:`endpoints:Endpoints`: 
  Specifiche tecniche per tutti gli endpoint API esposti da ciascun tipo di entità, inclusi gli endpoint di federazione e le integrazioni di servizi specializzati.

**Sezione** :ref:`algorithms:Algoritmi Crittografici`, :ref:`security-privacy-considerations:Considerazioni di Sicurezza e Privacy`, e :ref:`log-retention-policy:Politiche Generali di Conservazione dei Log` (**Supporto all'Implementazione**): 
  Requisiti crittografici, considerazioni sulla sicurezza e sulla privacy, e politiche di conservazione dei log essenziali per implementazioni conformi.

**Sezione** :ref:`defined-terms-and-references:Termini Definiti e Riferimenti`, :ref:`official-resources:Risorse Ufficiali`, :ref:`contribute:Come contribuire`, e :ref:`open-source:Rilasci Open Source` (**Terminologia e Riferimenti**):
  Terminologia completa, riferimenti normativi, documentazione, risorse e strumenti aggiuntivi, linee guida per i contributi.

**Sezione** :ref:`appendix:Appendice`: 
  Fornisce dettagli tecnici supplementari, modelli di implementazione e framework di test, inclusa la gestione delle istanze di applicazioni mobili, specifiche di integrazione della piattaforma nazionale e matrici di test complete per la validazione dell'ecosistema.


Percorsi rapidi per obiettivo
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Da usare quando si conosce già il compito da svolgere; le sezioni per ruolo sotto approfondiscono ciascun percorso.

**Fornitore di Wallet** — *Realizzare la Soluzione Wallet:* :ref:`wallet-solution:Soluzione Wallet`, :ref:`wallet-provider-endpoint:Endpoint del Fornitore di Wallet`; *far circolare gli attestati:* :ref:`digital-credential-flows:Flussi relativi agli Attestati Elettronici`; *federazione e crittografia:* :ref:`trust-infrastructure:L'Infrastruttura di Trust`, :ref:`algorithms:Algoritmi Crittografici`; *sicurezza e privacy:* :ref:`security-privacy-considerations:Considerazioni di Sicurezza e Privacy`.

**Credential Issuer** — *Emettere attestati:* :ref:`credential-issuer-solution:Soluzione del Fornitore di Attestati Elettronici`, :ref:`credential-issuance:Emissione di Attestati Elettronici`, :ref:`credential-issuer-endpoint:Endpoint del Credential Issuer`; *dati da Fonti Autentiche:* :ref:`authentic-sources:Fonti Autentiche`; *se si autentica l'Utente:* :ref:`credential-presentation:Presentazione dell'Attestato Elettronico`; *sicurezza:* :ref:`security-privacy-considerations:Considerazioni di Sicurezza e Privacy`.

**Fonte Autentica** — *Erogare dati autorevoli:* :ref:`authentic-sources:Fonti Autentiche`, :ref:`authentic-source-endpoint:Endpoint delle Fonti Autentiche`; *integrità e piattaforme nazionali:* :ref:`algorithms:Algoritmi Crittografici`, :ref:`e-service-pdnd:e-Service PDND`.

**Relying Party** — *Verificare le credenziali presentate:* :ref:`relying-party-solution:Soluzione di Relying Party`, :ref:`credential-presentation:Presentazione dell'Attestato Elettronico`, :ref:`relying-party-endpoints:Endpoint della Relying Party`; *formati e validità:* :ref:`digital-credential-management:Gestione degli Attestati Elettronici`; *sicurezza:* :ref:`security-privacy-considerations:Considerazioni di Sicurezza e Privacy`.


Lettura per ruolo
^^^^^^^^^^^^^^^^^

Per un accesso semplificato agli argomenti di queste specifiche, di seguito viene presentato un percorso di lettura per ruoli che tiene conto della fase in cui si trovano a operare all’interno del sistema IT-Wallet con un rimando preciso alla sezione di interesse del documento. 

FONTI AUTENTICHE (AUTHENTIC SOURCE)  
"""""""""""""""""""""""""""""""""""

L’Authentic Source è il proprietario del dato. Il suo ruolo è garantire che le informazioni originali siano trasmesse correttamente e rese disponibili ai sistemi di emissione in modo sicuro e sempre aggiornato.  
Focus: disponibilità del dato, correttezza delle informazioni trasmesse, allineamento costante tra il database originale e le credenziali emesse.  

**Fase 1: Discovery**

**Obiettivo**: conoscere il contesto di riferimento, i requisiti tecnici e la normativa per entrare a far parte della Trust Chain (catena di fiducia) su cui si fonda tutto il sistema.  

- **Introduzione**: per comprendere l’ambito e il linguaggio normativo dell'ecosistema IT-Wallet. 

- **:ref:`architecture-overview: Panoramica dell’Architettura`**: per conoscere l’Architettura del sistema IT-Wallet, in termini di governance e processi operativi abilitati. 

- **:ref:`trust-infrastructure: Infrastruttura di Trust`**: per conoscere i requisiti chiave della Trust Chain e come essere registrati nella Trust List per poter operare sia a livello nazionale che europeo.  

- Cap. 17: Termini e riferimenti: per conoscere i riferimenti normativi, i termini definiti e gli standard tecnici per consentire un'interoperabilità sicura e corretta tra tutti i partecipanti (puoi ricorrere a questa sezione per ogni dubbio su terminologia, standard di riferimento, acronimi...) 

* **Sezione** :ref:`credential-issuer-solution:Soluzione del Fornitore di Attestati Elettronici`: Comprensione delle interazioni e dei requisiti del Fornitore di Credenziali.
* **Sezione** :ref:`relying-party-solution:Soluzione di Relying Party`: Comprensione delle interazioni con le Relying Party e dei protocolli di presentazione.


Fornitore di Credenziali
""""""""""""""""""""""""

Per i lettori interessati all'implementazione di una Soluzione di **Fornitore di Credenziali**, dovrebbero concentrarsi sul ciclo di vita delle Credenziali Elettroniche e sui flussi di interazione per l'emissione.

**Sezioni essenziali:**

* **Sezione** :ref:`functionalities:Design dell'Esperienza Utente`: Requisiti funzionali di alto livello a supporto dell’Esperienza Utente in tutte le fasi di interazione tra l’Utente e il servizio.
* **Sezione** :ref:`credential-issuer-solution:Soluzione del Fornitore di Attestati Elettronici`: Soluzione di Fornitore di Credenziali - Requisiti completi di implementazione e dettagli dei componenti.
* **Sezione** :ref:`authentic-sources:Fonti Autentiche`: Comprensione dei modelli di integrazione con fonti di dati autorevoli.
* **Sezione** :ref:`digital-credential-management:Gestione degli Attestati Elettronici`: Formati delle Credenziali Elettroniche e gestione del ciclo di vita.
* **Sezione** :ref:`credential-issuance:Emissione di Attestati Elettronici`: Implementazione dettagliata del flusso di emissione.
* **Sezione** :ref:`credential-issuer-endpoint:Endpoint del Credential Issuer`: Specifiche API per la federazione e specifiche per l'emissione.
* **Sezione** :ref:`algorithms:Algoritmi Crittografici`: Algoritmi di firma e requisiti di implementazione della sicurezza.

**Sezioni secondarie:**

* **Sezione** :ref:`wallet-solution:Soluzione Wallet`: Comprensione delle interazioni e dei requisiti dell'Istanza del Wallet.
* **Sezione** :ref:`credential-presentation:Presentazione dell'Attestato Elettronico`: Comprensione di come le Credenziali Elettroniche vengono presentate sia in scenari remoti che di prossimità.
* **Sezione** :ref:`e-service-pdnd:e-Service PDND`: Integrazione con la Piattaforma Nazionale di Interoperabilità dei Dati.

.. note::

    Se il Fornitore di Credenziali autentica l'Utente deve conformarsi alla Sezione :ref:`credential-presentation:Presentazione dell'Attestato Elettronico`. Se la Fonte Autentica che fornisce gli attributi dell'Utente appartiene al settore pubblico deve conformarsi alla Sezione :ref:`e-service-pdnd:e-Service PDND`.  

Fonte Autentica
"""""""""""""""

Se il lettore vuole gestire una **Fonte Autentica**, l'attenzione dovrebbe essere sulla fornitura sicura dei dati e sull'integrazione con i Fornitori di Credenziali.

**Sezioni essenziali:**

* **Sezione** :ref:`functionalities:Design dell'Esperienza Utente`: Requisiti funzionali di alto livello a supporto dell’Esperienza Utente in tutte le fasi di interazione tra l’Utente e il servizio.
* **Sezione** :ref:`authentic-sources:Fonti Autentiche`: Requisiti e modelli di integrazione con i Fornitori di Credenziali.
* **Sezione** :ref:`authentic-source-endpoint:Endpoint delle Fonti Autentiche`: Specifiche API e integrazione del catalogo.
* **Sezione** :ref:`algorithms:Algoritmi Crittografici`: Requisiti di integrità dei dati, autenticazione e sicurezza.
* **Sezione** :ref:`e-service-pdnd:e-Service PDND`: Integrazione PDND e requisiti di interoperabilità.

**Sezioni secondarie:**

* **Sezione** :ref:`credential-issuer-solution:Soluzione del Fornitore di Attestati Elettronici`: Comprensione dei componenti principali dei Fornitori di Credenziali e dei processi di integrazione.
* **Sezione** :ref:`digital-credential-management:Gestione degli Attestati Elettronici`: Comprensione di come i dati autorevoli e gli attributi diventano Credenziali Elettroniche e di come viene gestito il loro ciclo di vita.

Relying Party
"""""""""""""

I lettori interessati all'implementazione o alla gestione di una Soluzione di **Relying Party** per accettare e verificare le Credenziali Elettroniche dovrebbero concentrarsi sui protocolli di presentazione e sui meccanismi di verifica.

**Sezioni essenziali:**

* **Sezione** :ref:`functionalities:Design dell'Esperienza Utente`: Requisiti funzionali di alto livello a supporto dell’Esperienza Utente in tutte le fasi di interazione tra l’Utente e il servizio.
* **Sezione** :ref:`relying-party-solution:Soluzione di Relying Party`: Requisiti completi di implementazione del Verificatore di Credenziali.
* **Sezione** :ref:`digital-credential-management:Gestione degli Attestati Elettronici`: Comprensione dei formati delle Credenziali Elettroniche e verifica della validità.
* **Sezione** :ref:`credential-presentation:Presentazione dell'Attestato Elettronico`: Implementazione del flusso di presentazione sia per scenari remoti che di prossimità.
* **Sezione** :ref:`relying-party-endpoints:Endpoint della Relying Party`: Panoramica completa di tutti gli endpoint della Relying Party e i loro ambiti.
* **Sezione** :ref:`relying-party-endpoints:Endpoint per Flussi Remoti della Relying Party`: Specifiche API complete della Relying Party per flussi remoti e di prossimità.
* **Sezione** :ref:`Endpoint del Backend del Provider di Relying Party <relying-party-provider-backend-endpoint-endpoint-del-backend-del-provider-di-relying-party>`: Specifiche API del Backend del Provider di Relying Party per la gestione del ciclo di vita delle App di Verifica.
* **Sezione** :ref:`algorithms:Algoritmi Crittografici`: Requisiti della suite crittografica.

**Sezioni secondarie:**

* **Sezione** :ref:`wallet-solution:Soluzione Wallet`: Comprensione delle interazioni dell'Istanza del Wallet e dei protocolli di presentazione.
* **Sezione** :ref:`mobile-application-instance:Istanza dell'Applicazione Mobile`: Modelli di implementazione specifici per dispositivi mobili.

Argomenti Trasversali
^^^^^^^^^^^^^^^^^^^^^

Indipendentemente dal ruolo principale, alcune sezioni contengono informazioni rilevanti per tutti i partecipanti all'ecosistema:

**Sicurezza e Conformità:**
    Tutti gli implementatori devono implementare le loro soluzioni secondo la Sezione :ref:`security-privacy-considerations:Considerazioni di Sicurezza e Privacy` e la Sezione :ref:`log-retention-policy:Politiche Generali di Conservazione dei Log`.

**Standard e Riferimenti:**
    La Sezione :ref:`defined-terms-and-references:Termini Definiti e Riferimenti` fornisce riferimenti normativi, termini definiti e standard tecnici per consentire un'interoperabilità sicura e corretta tra tutti i partecipanti.

**Test e Validazione:**
    La Sezione :ref:`test-plans:Test Plans` fornisce una matrice di test completa per la validazione delle implementazioni tra diversi ruoli e flussi di interazione.

Approccio all'Implementazione
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Si suggerisce il seguente approccio di lettura in fasi:

    1. **Fase di Fondazione**: Leggere le Sezioni :ref:`introduction:Introduzione`, :ref:`architecture-overview:Panoramica dell'Architettura`, :ref:`brand-identity:Brand Identity` e :ref:`trust-infrastructure:L'Infrastruttura di Trust` per stabilire una comprensione concettuale del paradigma IT-Wallet, degli elementi di Brand Identity e dell'infrastruttura di fiducia.
    2. **Fase Specifica per Ruolo**: Concentrarsi sulle sezioni essenziali del ruolo primario per comprendere i requisiti specifici di Esperienza Utente, funzionali e di implementazione, i componenti tecnici principali, l'architettura generale e i flussi di interazione (vedere la Sezione :ref:`functionalities:Design dell'Esperienza Utente`, :ref:`entities:Entità` e la Sezione :ref:`endpoints:Endpoints` per maggiori dettagli).
    3. **Fase di Integrazione**: Rivedere le sezioni secondarie rilevanti per le interazioni con altri partecipanti all'ecosistema e i requisiti di integrazione della piattaforma.
    4. **Fase di Validazione**: Studiare le considerazioni sulla sicurezza, le linee guida per i test e i requisiti di conformità secondo le Sezioni :ref:`security-privacy-considerations:Considerazioni di Sicurezza e Privacy`, :ref:`log-retention-policy:Politiche Generali di Conservazione dei Log` e :ref:`test-plans:Test Plans` per ulteriori informazioni.

.. note::

    Per gli implementatori che lavorano su soluzioni che coprono più ruoli (ad esempio, una combinazione di Soluzioni di Fornitore di Credenziali e Relying Party), si raccomanda di rivedere le sezioni per tutti i ruoli pertinenti prima di procedere con gli sviluppi. È importante prestare particolare attenzione ai requisiti di Entity Configuration e ai flussi di federazione che si applicano a più ruoli.

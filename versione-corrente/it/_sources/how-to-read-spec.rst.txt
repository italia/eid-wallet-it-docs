.. include:: ../common/common_definitions.rst

Come leggere le Specifiche
--------------------------

Questa specifica è progettata per soddisfare i requisiti di molteplici stakeholder all'interno dell'ecosistema IT-Wallet. Ogni ruolo ha responsabilità e ambiti diversi e diverse esigenze informative. Questa sezione fornisce percorsi di lettura personalizzati per aiutare il lettore a navigare in modo efficiente verso i contenuti più rilevanti per gli obiettivi di implementazione.

Panoramica della Struttura delle Specifiche
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

La specifica è organizzata nelle seguenti sezioni principali:

**Sezione** :ref:`introduction:Introduzione`: 
  Stabilisce l'ambito e il linguaggio normativo per l'ecosistema IT-Wallet.

**Sezione** :ref:`design:Principi di design`: 
  Fornisce principi di progettazione e requisiti di identità visiva dell'ecosistema IT-Wallet.

**Sezione** :ref:`architecture-overview:Panoramica dell'Architettura`:
  Fornisce funzionalità di sistema di alto livello e guida per navigare nella specifica in base ai requisiti di implementazione.

**Sezione** :ref:`trust:L'Infrastruttura di Trust`:
  Definisce il modello di trust basato sulla federazione, le relazioni tra entità e i meccanismi di valutazione della fiducia che proteggono l'intero ecosistema.

**Sezione** :ref:`entities:Entità`: 
  Requisiti di implementazione completi per ogni partecipante all'ecosistema: Soluzioni Wallet, Fornitori di Credenziali, Relying Party e Fonti Autentiche, inclusi i loro componenti, modelli di interazione e requisiti di configurazione.

**Sezione** :ref:`digital-credential-management:Gestione delle Credenziali Digitali`: 
  Copre i modelli di dati e i formati delle Credenziali Elettroniche, la gestione del ciclo di vita, la verifica della validità e la struttura del catalogo delle Credenziali.

**Sezione** :ref:`digital-credential-flows:Flussi relativi agli Attestati Elettronici`:
  Guida dettagliata all'implementazione per i flussi di emissione e presentazione delle Credenziali Elettroniche, inclusi i flussi di interazione remota e di prossimità.

**Sezione** :ref:`endpoints:Endpoints`: 
  Specifiche tecniche per tutti gli endpoint API esposti da ciascun tipo di entità, inclusi gli endpoint di federazione e le integrazioni di servizi specializzati.

**Sezione** :ref:`algorithms:Algoritmi Crittografici`, :ref:`security-privacy-considerations:Considerazioni di Sicurezza e Privacy`, e :ref:`log-retention-policy:Politiche Generali di Conservazione dei Log` (**Supporto all'Implementazione**): 
  Requisiti crittografici, considerazioni sulla sicurezza e sulla privacy, e politiche di conservazione dei log essenziali per implementazioni conformi.

**Sezione** :ref:`defined-terms-and-references:Termini Definiti e Riferimenti`, :ref:`contribute:Come contribuire`, e :ref:`open-source:Rilasci Open Source` (**Terminologia e Riferimenti**):
  Terminologia completa, riferimenti normativi, linee guida per i contributi.

**Sezione** :ref:`appendix:Appendice`: 
  Fornisce dettagli tecnici supplementari, modelli di implementazione e framework di test, inclusa la gestione delle istanze di applicazioni mobili, specifiche di integrazione della piattaforma nazionale e matrici di test complete per la validazione dell'ecosistema.


Percorsi di Lettura per Ruolo
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Prima di immergersi nelle sezioni specifiche per ruolo, tutti i lettori dovrebbero familiarizzare con i concetti fondamentali delineati nelle Sezioni :ref:`introduction:Introduzione`, :ref:`architecture-overview:Panoramica dell'Architettura` e :ref:`trust:L'Infrastruttura di Trust`, che stabiliscono il vocabolario comune, i principi di progettazione e l'infrastruttura di fiducia che forniscono il quadro sottostante per l'intero ecosistema.

Fornitore di Wallet
"""""""""""""""""""

I lettori che implementano o gestiscono una Soluzione di **Fornitore di Wallet** dovrebbero concentrarsi sulla comprensione di come gestire in modo sicuro le Credenziali Elettroniche e facilitare le interazioni dell'Utente con altri partecipanti all'ecosistema.

**Sezioni essenziali:**

* **Sezione** :ref:`wallet-solution:Soluzione Wallet`: Requisiti completi di implementazione del Wallet, componenti e processi di interazione.
* **Sezione** :ref:`digital-credential-management:Gestione delle Credenziali Digitali`: Modelli di dati, formati e gestione del ciclo di vita delle Credenziali Elettroniche.
* **Sezione** :ref:`digital-credential-flows:Flussi relativi agli Attestati Elettronici`: Flussi di emissione e presentazione per le Credenziali Elettroniche.
* **Sezione** :ref:`wallet-provider-endpoint:Endpoint del Fornitore di Wallet`: Specifiche API per la federazione e specifiche per IT-Wallet.
* **Sezione** :ref:`algorithms:Algoritmi Crittografici`: Requisiti di implementazione per sicurezza e crittografia.
* **Sezione** :ref:`mobile-application-instance:Istanza dell'Applicazione Mobile`: Modelli di implementazione specifici per dispositivi mobili.
* **Sezione** :ref:`e-service-pdnd:e-Service PDND`: Integrazione con la Piattaforma Nazionale di Interoperabilità dei Dati.

**Sezioni secondarie:**

* **Sezione** :ref:`credential-issuer-solution:Soluzione del Fornitore di Credenziale`: Comprensione delle interazioni e dei requisiti del Fornitore di Credenziali.
* **Sezione** :ref:`relying-party-solution:Soluzione di Relying Party`: Comprensione delle interazioni con le Relying Party e dei protocolli di presentazione.


Fornitore di Credenziale
""""""""""""""""""""""""

Per i lettori interessati all'implementazione di una Soluzione di **Fornitore di Credenziale**, dovrebbero concentrarsi sul ciclo di vita delle Credenziali Elettroniche e sui flussi di interazione per l'emissione.

**Sezioni essenziali:**

* **Sezione** :ref:`credential-issuer-solution:Soluzione del Fornitore di Credenziale`: Soluzione di Fornitore di Credenziale - Requisiti completi di implementazione e dettagli dei componenti.
* **Sezione** :ref:`authentic-sources:Fonti Autentiche`: Comprensione dei modelli di integrazione con fonti di dati autorevoli.
* **Sezione** :ref:`digital-credential-management:Gestione delle Credenziali Digitali`: Formati delle Credenziali Elettroniche e gestione del ciclo di vita.
* **Sezione** :ref:`credential-issuance:Emissione di Credenziale Digitale`: Implementazione dettagliata del flusso di emissione.
* **Sezione** :ref:`credential-issuer-endpoint:Endpoint del Credential Issuer`: Specifiche API per la federazione e specifiche per l'emissione.
* **Sezione** :ref:`algorithms:Algoritmi Crittografici`: Algoritmi di firma e requisiti di implementazione della sicurezza.

**Sezioni secondarie:**

* **Sezione** :ref:`wallet-solution:Soluzione Wallet`: Comprensione delle interazioni e dei requisiti dell'Istanza del Wallet.
* **Sezione** :ref:`credential-presentation:Presentazione della Credenziale Digitale`: Comprensione di come le Credenziali Elettroniche vengono presentate sia in scenari remoti che di prossimità.
* **Sezione** :ref:`e-service-pdnd:e-Service PDND`: Integrazione con la Piattaforma Nazionale di Interoperabilità dei Dati.

.. note::

    Se il Fornitore di Credenziale autentica l'Utente deve conformarsi alla Sezione :ref:`credential-presentation:Presentazione della Credenziale Digitale`. Se la Fonte Autentica che fornisce gli attributi dell'Utente appartiene al settore pubblico deve conformarsi alla Sezione :ref:`e-service-pdnd:e-Service PDND`.  

Fonte Autentica
"""""""""""""""

Se il lettore vuole gestire una **Fonte Autentica**, l'attenzione dovrebbe essere sulla fornitura sicura dei dati e sull'integrazione con i Fornitori di Credenziali.

**Sezioni essenziali:**

* **Sezione** :ref:`authentic-sources:Fonti Autentiche`: Requisiti e modelli di integrazione con i Fornitori di Credenziali.
* **Sezione** :ref:`authentic-source-endpoint:Endpoint delle Fonti Autentiche`: Specifiche API e integrazione del catalogo.
* **Sezione** :ref:`algorithms:Algoritmi Crittografici`: Requisiti di integrità dei dati, autenticazione e sicurezza.
* **Sezione** :ref:`e-service-pdnd:e-Service PDND`: Integrazione PDND e requisiti di interoperabilità.

**Sezioni secondarie:**

* **Sezione** :ref:`credential-issuer-solution:Soluzione del Fornitore di Credenziale`: Comprensione dei componenti principali dei Fornitori di Credenziali e dei processi di integrazione.
* **Sezione** :ref:`digital-credential-management:Gestione delle Credenziali Digitali`: Comprensione di come i dati autorevoli e gli attributi diventano Credenziali Elettroniche e di come viene gestito il loro ciclo di vita.

Relying Party
"""""""""""""

I lettori interessati all'implementazione o alla gestione di una Soluzione di **Relying Party** per accettare e verificare le Credenziali Elettroniche dovrebbero concentrarsi sui protocolli di presentazione e sui meccanismi di verifica.

**Sezioni essenziali:**

* **Sezione** :ref:`relying-party-solution:Soluzione di Relying Party`: Requisiti completi di implementazione del Verificatore di Credenziali.
* **Sezione** :ref:`digital-credential-management:Gestione delle Credenziali Digitali`: Comprensione dei formati delle Credenziali Elettroniche e verifica della validità.
* **Sezione** :ref:`credential-presentation:Presentazione della Credenziale Digitale`: Implementazione del flusso di presentazione sia per scenari remoti che di prossimità.
* **Sezione** :ref:`relying-party-endpoint:Endpoint della Relying Party`: Specifiche API relative alla federazione e alla verifica.
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
    La Sezione :ref:`test-plans:Piani di Test` fornisce una matrice di test completa per la validazione delle implementazioni tra diversi ruoli e flussi di interazione.

Approccio all'Implementazione
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Si suggerisce il seguente approccio di lettura in fasi:

    1. **Fase di Fondazione**: Leggere le Sezioni :ref:`introduction:Introduzione`, :ref:`architecture-overview:Panoramica dell'Architettura` e :ref:`trust:L'Infrastruttura di Trust` per stabilire una comprensione concettuale del paradigma IT-Wallet, dei principi di progettazione e dell'infrastruttura di fiducia.
    2. **Fase Specifica per Ruolo**: Concentrarsi sulle sezioni essenziali del ruolo primario per comprendere i requisiti specifici di implementazione, i componenti tecnici principali, l'architettura generale e i flussi di interazione (vedere la Sezione :ref:`entities:Entità` e la Sezione :ref:`endpoints:Endpoints` per maggiori dettagli).
    3. **Fase di Integrazione**: Rivedere le sezioni secondarie rilevanti per le interazioni con altri partecipanti all'ecosistema e i requisiti di integrazione della piattaforma.
    4. **Fase di Validazione**: Studiare le considerazioni sulla sicurezza, le linee guida per i test e i requisiti di conformità secondo le Sezioni :ref:`security-privacy-considerations:Considerazioni di Sicurezza e Privacy`, :ref:`log-retention-policy:Politiche Generali di Conservazione dei Log` e :ref:`test-plans:Piani di Test` per ulteriori informazioni.

.. note::

    Per gli implementatori che lavorano su soluzioni che coprono più ruoli (ad esempio, una combinazione di Soluzioni di Fornitore di Credenziale e Relying Party), si raccomanda di rivedere le sezioni per tutti i ruoli pertinenti prima di procedere con gli sviluppi. È importante prestare particolare attenzione ai requisiti di Entity Configuration e ai flussi di federazione che si applicano a più ruoli.

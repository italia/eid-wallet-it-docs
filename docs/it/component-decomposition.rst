.. include:: ../common/common_definitions.rst
.. Incluso tramite appendix.rst al livello di titolo '=' (titolo del documento).


Decomposizione per Componenti
=============================

Questa appendice decompone il PID Provider e la Soluzione Wallet con la matrice usata dall'Agenzia per la Cybersicurezza Nazionale (ACN): ambito, sottocomponenti, ambito di certificazione, standard, rischi e controlli.

I requisiti funzionali restano nelle sezioni citate nella colonna Standard. Questa appendice non li ripete.


PID Provider
------------

Il PID Provider è il Fornitore di Attestati Elettronici che emette il PID. La Fonte Autentica che fornisce gli attributi del PID è fuori dall'ambito di certificazione del PID Provider. I componenti del PID Provider che recuperano quegli attributi sono dentro quell'ambito.

.. _table_pid_provider_decomposition:
.. list-table:: Decomposizione del PID Provider
   :class: longtable
   :widths: 14 16 14 20 18 18
   :header-rows: 1

   * - **Ambito**
     - **Sottocomponenti**
     - **Ambito di certificazione**
     - **Standard**
     - **Rischi**
     - **Controlli**
   * - Verifica dell'identità
     - Autenticazione dell'Utente per l'emissione del PID
     - In ambito
     - :ref:`credential-issuance-endpoint:Selezione del Metodo di Autenticazione dell'Utente`
     - Emissione a un Utente che non è stato autenticato al livello di garanzia richiesto per il PID
     - Autenticazione dell'Utente per l'emissione del PID, come specificato in :ref:`credential-issuance-endpoint:Selezione del Metodo di Autenticazione dell'Utente`
   * - Emissione del PID
     - Componente di emissione e Authorization Server
     - In ambito
     - [`OpenID4VCI`_], [`ETSI TS 119 472-3`_], [`CIR2024/2982`_]
     - Emissione a un'Istanza del Wallet non autentica, o la cui chiave del PID non è vincolata a quell'Istanza del Wallet
     - Controlli della Wallet Instance Attestation e della Key Attestation in :ref:`credential-issuance:Emissione di Attestati Elettronici`
   * - Gestione del PID
     - Ciclo di vita del PID emesso
     - In ambito
     - :ref:`credential-revocation:Ciclo di Vita degli Attestati Elettronici`
     - Uso di un PID scaduto, sospeso o non più vincolato all'Istanza del Wallet
     - Scadenza, sospensione e revoca in :ref:`credential-revocation:Ciclo di Vita degli Attestati Elettronici`
   * - Gestione dello stato del PID
     - Pubblicazione della Token Status List del PID
     - In ambito
     - `TOKEN-STATUS-LIST`_, :ref:`credential-revocation:Token Status Lists`
     - Presentazione di un PID revocato
     - Valutazione dello stato in :ref:`credential-revocation:Token Status Lists`
   * - Registrazione di audit
     - Traccia di audit degli eventi di emissione e del ciclo di vita del PID
     - In ambito
     - :ref:`log-retention-policy:Politiche Generali di Conservazione dei Log`
     - Uso improprio del servizio di emissione senza una registrazione conservata
     - Registrazione di audit richiesta da :ref:`credential-issuer-solution:Requisiti del Fornitore di Attestati Elettronici` e da :ref:`log-retention-policy:Politiche Generali di Conservazione dei Log`
   * - Interazione con le Fonti Autentiche
     - Recupero degli attributi del PID dalla Fonte Autentica
     - In ambito. La Fonte Autentica è fuori ambito
     - :ref:`authentic-sources:Fonti Autentiche`
     - Emissione di attributi del PID che non provengono dalla Fonte Autentica
     - Recupero tramite l'interfaccia della Fonte Autentica in :ref:`authentic-sources:Fonti Autentiche`
   * - Dispositivo di firma
     - Chiave Sign/Seal usata per firmare il PID
     - In ambito
     - :ref:`infrastructure-trust:X.509 Certificate Profile`, :ref:`infrastructure-trust:EUDIW Trust Artifacts`
     - Un PID firmato con una chiave che le Relying Party non possono ancorare al PID Provider
     - Trust anchor Sign/Seal pubblicato nella PID Providers LoTE, come specificato in :ref:`infrastructure-trust:EUDIW Trust Artifacts`


Soluzione Wallet
----------------

.. note::
   Questa tabella non è normativa. La discussione con l'ACN sulla decomposizione della Soluzione Wallet è ancora aperta. L'ambito di certificazione, i rischi e i controlli di questa tabella diventano normativi solo dopo quella discussione. Fino ad allora, i requisiti della Soluzione Wallet restano quelli in :ref:`wallet-solution-requirements:Requisiti della Soluzione Wallet` e in :ref:`wallet-solution-components:Componenti della Soluzione Wallet`.

Le righe seguenti nominano i sottocomponenti già specificati per la Soluzione Wallet. L'interazione Wallet-to-Wallet e la creazione di firme elettroniche qualificate sono fuori dall'ambito di questa versione, come specificato in :ref:`wallet-solution:Soluzione Wallet`.

.. _table_wallet_solution_decomposition:
.. list-table:: Decomposizione della Soluzione Wallet
   :class: longtable
   :widths: 16 22 16 16 15 15
   :header-rows: 1

   * - **Ambito**
     - **Sottocomponenti**
     - **Ambito di certificazione**
     - **Standard**
     - **Rischi**
     - **Controlli**
   * - Backend del Wallet
     - Componente Frontend
     - In attesa della discussione ACN
     - :ref:`wallet-solution-components:Componente Frontend`
     - In attesa della discussione ACN
     - In attesa della discussione ACN
   * - Backend del Wallet
     - Interfaccia API
     - In attesa della discussione ACN
     - :ref:`wallet-solution-components:Interfaccia API`
     - In attesa della discussione ACN
     - In attesa della discussione ACN
   * - Backend del Wallet
     - Gestione del Ciclo di Vita dell'Istanza del Wallet
     - In attesa della discussione ACN
     - :ref:`wallet-solution-components:Gestione del Ciclo di Vita dell'Istanza del Wallet`
     - In attesa della discussione ACN
     - In attesa della discussione ACN
   * - Backend del Wallet
     - Componente Trust & Security
     - In attesa della discussione ACN
     - :ref:`wallet-solution-components:Componente Trust & Security`
     - In attesa della discussione ACN
     - In attesa della discussione ACN
   * - Unità di Wallet
     - Interfaccia Utente
     - In attesa della discussione ACN
     - :ref:`wallet-solution-components:Interfaccia Utente`
     - In attesa della discussione ACN
     - In attesa della discussione ACN
   * - Unità di Wallet
     - Componente di Gestione del Ciclo di Vita dell'Istanza del Wallet
     - In attesa della discussione ACN
     - :ref:`wallet-solution-components:Componente di Gestione del Ciclo di Vita dell'Istanza del Wallet`
     - In attesa della discussione ACN
     - In attesa della discussione ACN
   * - Unità di Wallet
     - Componente Issuer
     - In attesa della discussione ACN
     - :ref:`wallet-solution-components:Componente Issuer`, [`OpenID4VCI`_]
     - In attesa della discussione ACN
     - In attesa della discussione ACN
   * - Unità di Wallet
     - Componente di Presentazione
     - In attesa della discussione ACN
     - :ref:`wallet-solution-components:Componente di Presentazione`, [`OpenID4VP`_], [`ISO18013-5`_]
     - In attesa della discussione ACN
     - In attesa della discussione ACN
   * - Unità di Wallet
     - Componente di Backup e Ripristino
     - In attesa della discussione ACN
     - :ref:`wallet-solution-components:Componente di Backup e Ripristino`
     - In attesa della discussione ACN
     - In attesa della discussione ACN
   * - Unità di Wallet
     - Dashboard e Registro delle Transazioni
     - In attesa della discussione ACN
     - :ref:`wallet-solution-components:Dashboard e Registro delle Transazioni`
     - In attesa della discussione ACN
     - In attesa della discussione ACN
   * - Unità di Wallet
     - Keystore
     - In attesa della discussione ACN
     - :ref:`wallet-solution-components:Keystore`
     - In attesa della discussione ACN
     - In attesa della discussione ACN
   * - Unità di Wallet
     - WSCA/WSCD Interface
     - In attesa della discussione ACN
     - :ref:`wallet-solution-components:WSCA/WSCD Interface`
     - In attesa della discussione ACN
     - In attesa della discussione ACN

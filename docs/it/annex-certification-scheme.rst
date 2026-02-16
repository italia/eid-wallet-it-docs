.. include:: ../common/common_definitions.rst


.. _annex-certification-scheme:

Schema di Certificazione e Approccio Complessivo
=================================================

Questa appendice descrive lo schema di certificazione e l'approccio complessivo per il sistema IT-Wallet, allineando le specifiche tecniche al paradigma di scomposizione dei componenti utilizzato per la valutazione della certificazione.

Quadro Normativo
----------------

La certificazione dei componenti del Sistema IT-Wallet è disciplinata dal `CIR 2024/2981`_ (**Regolamento di Esecuzione (UE) 2024/2981**). Il regolamento richiede, ai sensi dell'articolo 4, paragrafo 4, lettera d), che rischi, minacce e controlli implementati siano valutati come parte del processo di certificazione.

La scomposizione si basa su:

- **`ARF`_** (Architecture Reference Framework) per EUDI-Wallet
- **Documentazione Tecnica IT-Wallet** (questa specifica)
- **Schema Nazionale ENISA** per la documentazione di certificazione

Paradigma: Gerarchia della Scomposizione
-----------------------------------------

Il paradigma della scomposizione struttura il sistema in:

.. list-table:: Gerarchia della Scomposizione
   :widths: 25 75
   :header-rows: 1

   * - Livello
     - Descrizione
   * - Macro-componente di certificazione
     - Raggruppamento di alto livello (es. Servizi ICT Wallet, Servizi ICT PID Provider); ciascuno ha un proprietario (Fornitore di Wallet, PID Provider).
   * - Componente
     - Componente architetturale principale (es. Wallet Instance, Wallet Provider Backend, PID Provider Backend).
   * - Sottocomponente
     - Sottocomponente con responsabilità funzionale specifica.
   * - Sottocomponenti di basso livello
     - Scomposizione ulteriore opzionale non vincolata a standard esterni.

Ogni elemento può essere classificato come **prodotto ICT** o **processo ICT**. L'**Ambito di Certificazione** indica se il componente è valutato durante la certificazione (In scopo / No).

Componenti In Scopo per la Certificazione
-----------------------------------------

I seguenti componenti sono **in scopo** per la certificazione ai sensi del `CIR 2024/2981`_:

.. list-table:: Componenti In Scopo
   :widths: 35 35 30
   :header-rows: 1

   * - Macro-componente di certificazione
     - Proprietario
     - Riferimento Specifica Tecnica
   * - **Servizi ICT Wallet**
     - Fornitore di Wallet
     - :ref:`wallet-solution-components:Componenti della Soluzione Wallet`
   * - **Servizi ICT PID Provider**
     - PID Provider
     - :ref:`credential-issuer-solution:Soluzione del Fornitore di Attestati Elettronici`
   * - **Servizi ICT di Validazione** (Trust List Backend Services)
     - Fornitore dei Servizi di Validazione
     - :ref:`trust-infrastructure:L'Infrastruttura di Trust`
   * - **Regime di identificazione elettronica** (eID Scheme)
     - Trasversale (Fornitore di Wallet e PID Provider)
     - Schemi eID nazionali (CIEid, SPID); :ref:`credential-issuance-l2plus:Autenticazione eID Substantial con Verifica MRTD per Emissione PID`

Componenti Fuori Scopo per la Certificazione
---------------------------------------------

I seguenti componenti sono **fuori scopo** per la certificazione:

.. list-table:: Componenti Fuori Scopo
   :widths: 40 60
   :header-rows: 1

   * - Componente
     - Note
   * - User Device (Sistema operativo, piattaforma, crittografia locale)
     - Fornito dal Produttore di Dispositivi; non incluso nell'ambito di certificazione.
   * - Fornitore di Attestazioni di Attributi ((Pub/Q)EAA)
     - Certificato secondo schemi separati.
   * - Fonte Autentica (AS)
     - Fonti esterne di dati autorevoli.
   * - Relying Party (RP)
     - Consumer di credenziali; percorso di certificazione separato.
   * - Qualified Signature/Seal Creation Device (QSCD)
     - Fornito da QTSP nell'ambito del regolamento sui servizi fiduciari qualificati.

Cross-Riferimento: Scomposizione e Specifica Tecnica
-----------------------------------------------------

La seguente tabella fornisce un cross-riferimento consolidato dagli elementi della scomposizione alle sezioni rilevanti della specifica tecnica.

.. list-table:: Tabella di Cross-Riferimento
   :widths: 30 45 25
   :header-rows: 1

   * - Elemento Scomposizione
     - Sezione Specifica Tecnica
     - Macro-componente di certificazione
   * - Wallet Instance (WI)
     - :ref:`wallet-solution-components:Unità di Wallet`
     - Servizi ICT Wallet
   * - Wallet Provider Backend (WPBE)
     - :ref:`wallet-solution-components:Backend del Wallet`
     - Servizi ICT Wallet
   * - WSCD / WSCA
     - :ref:`wallet-solution-components:Archiviazione Sicura`
     - Servizi ICT Wallet
   * - PID Provider Backend (PPBE)
     - :ref:`credential-issuer-solution:Soluzione del Fornitore di Attestati Elettronici`
     - Servizi ICT PID Provider
   * - Identity Proofing (PPBE)
     - :ref:`credential-issuer-solution:Componente Relying Party`, :ref:`credential-issuance-l2plus:Autenticazione eID Substantial con Verifica MRTD per Emissione PID`
     - Servizi ICT PID Provider
   * - Trust List Backend Services
     - :ref:`trust-infrastructure:L'Infrastruttura di Trust`
     - Servizi ICT di Validazione
   * - eID Scheme
     - Schemi eID nazionali; :ref:`credential-issuance:Emissione di Attestati Elettronici`
     - Regime di identificazione elettronica

Certificazione Obbligatoria
---------------------------

La colonna **Ambito Certificazione** nelle tabelle di scomposizione (vedere :ref:`wallet-solution-components-decomposition:Scomposizione e Ambito di Certificazione` e :ref:`credential-issuer-solution-decomposition:Scomposizione e Ambito di Certificazione`) indica se è richiesta una certificazione di sicurezza. I casi condizionali includono:

- **WSCD** fornito dall'Utente o dal Fornitore di Wallet (la proprietà del dispositivo influenza lo scopo).
- **Wallet Instance** ambiente di esecuzione (dispositivo Utente vs. interfaccia web).
- **eID Scheme** come elemento trasversale tra Fornitore di Wallet e PID Provider.

Valutazione del Rischio
------------------------

La scomposizione supporta la valutazione del rischio ai sensi dell'articolo 4, paragrafo 4, lettera d) del `CIR 2024/2981`_ attraverso:

- **Rischi (ID e Nome)**: Collegati al catalogo dei rischi dello schema di certificazione (allineato con l'Allegato I del `CIR 2024/2981`_).
- **Minacce**: Identificate per componente.
- **Controlli implementati**: Documentati nelle specifiche tecniche e nei piani di test.

Per la copertura dei test, vedere :ref:`test-plans:Piani di Test` e :ref:`test-plans-wallet-provider:Piani di Test per il Fornitore di Wallet`.

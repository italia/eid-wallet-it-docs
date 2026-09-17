.. include:: ../common/common_definitions.rst


Rilasci Open Source
===================

1. Principi Generali
^^^^^^^^^^^^^^^^^^^^

L'ecosistema IT-Wallet è costruito su principi di apertura e trasparenza. In conformità con il **Codice dell'Amministrazione Digitale (CAD)** e con il **Regolamento europeo eIDAS 2.0**, l'adozione di framework open source, anche durante la fase di sperimentazione, è fortemente incoraggiata come fattore abilitante chiave per garantire fiducia, collaborazione, revisione tra pari e miglioramenti condivisi in tutto l'ecosistema. Questo quadro è allineato con l'**Interoperable Europe Act**, con l'obiettivo di massimizzare il valore pubblico e la sicurezza attraverso la trasparenza.

2. Requisiti Standard
^^^^^^^^^^^^^^^^^^^^^

Tutte le entità (Fornitori di Wallet, Fornitori di Credenziali, Relying Party) coinvolte nell'ecosistema IT-Wallet (di seguito "Proprietari di Progetto") **DOVREBBERO** aderire alle migliori pratiche del settore per garantire che il software sia utilizzabile, conforme e sicuro, seguendo almeno quelle elencate nelle sezioni seguenti.

2.1 Licenze
"""""""""""

- I Proprietari di Progetto **DEVONO** utilizzare una licenza approvata dalla Open Source Initiative (OSI).
- I Proprietari di Progetto **DOVREBBERO** dare priorità alla **EUPL-1.2** (European Union Public License versione 1.2) per garantire la compatibilità legale all'interno del settore pubblico dell'UE, oppure a licenze permissive (es. Apache 2.0, MIT) per SDK e librerie al fine di massimizzarne l'adozione.

2.2 Gestione del Codice e Trasparenza
"""""""""""""""""""""""""""""""""""""

- **Controllo di Versione**: I Proprietari di Progetto **DEVONO** utilizzare piattaforme di hosting del codice che consentano l'accesso pubblico senza richiedere un login (es. GitHub, GitLab), garantendo una cronologia trasparente delle modifiche.
- **Documentazione**: I repository **DEVONO** includere una documentazione chiara, come:

  - ``README.md``: Panoramica del progetto e istruzioni di installazione.
  - ``LICENSE.md``: Termini con cui il titolare del copyright consente al destinatario di utilizzare il software (come descritto nella sezione *Licenze* sopra).
  - ``CONTRIBUTING.md``: Linee guida per i contributi al codice effettuati da soggetti esterni (es. contributori della community).

- **Community**: I Proprietari di Progetto **DOVREBBERO** interagire attivamente con la community per lo sviluppo e il supporto, gestendo le issue e le richieste di contributo in modo tempestivo.

2.3 Sicurezza e Qualità
"""""""""""""""""""""""

- **Qualità del Codice**: I Proprietari di Progetto **DOVREBBERO** implementare test automatizzati (es. test E2E e di integrazione) e pipeline di Continuous Integration. Tali pipeline **DOVREBBERO** essere pubbliche per consentirne l'ispezione.
- **Audit di Sicurezza**: I Proprietari di Progetto **DOVREBBERO** eseguire regolarmente audit del codice e analisi statiche.
- **SBOM**: I Proprietari di Progetto **DOVREBBERO** fornire una Software Bill of Materials (SBOM) per facilitare la gestione delle vulnerabilità, in linea con il **Cyber Resilience Act (CRA)**.

3. Fornitori di Wallet
^^^^^^^^^^^^^^^^^^^^^^

3.1 Open Source Obbligatorio
""""""""""""""""""""""""""""

Ai sensi del **Regolamento consolidato (UE) n. 910/2014 (eIDAS 2.0)**, Art. 5a par. 3, il codice sorgente dei componenti software applicativi delle soluzioni IT-Wallet **DEVE** essere rilasciato con licenza open-source.

Per motivi di sicurezza debitamente giustificati, il codice sorgente di componenti specifici, diversi da quelli installati sui dispositivi degli utenti, **PUÒ** rimanere chiuso, a condizione che ciò non comprometta la verificabilità complessiva della soluzione.

4. Fornitori di Credenziali e Relying Party
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

4.1 Componenti di integrazione
""""""""""""""""""""""""""""""

Per favorire l'interoperabilità dell'ecosistema e ridurre i costi di integrazione:

- I Fornitori di Credenziali e le Relying Party **DOVREBBERO** rilasciare Software Development Kit (SDK), librerie client e specifiche delle API con licenza open-source.

4.2 Infrastruttura di backend
"""""""""""""""""""""""""""""

I Fornitori di Credenziali e le Relying Party **DOVREBBERO** rilasciare la logica core del proprio backend con licenza open-source, a partire dalla fase di sperimentazione, per promuovere trasparenza e riuso.

5. Divulgazione Responsabile e Gestione delle Vulnerabilità
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
In conformità con il **Cyber Resilience Act (CRA)** e la **Direttiva NIS2 (UE) 2022/2555**:

- **Politica di Sicurezza**: Tutti i repository Open Source **DOVREBBERO** contenere un file ``SECURITY.md`` che descriva la procedura per la segnalazione delle vulnerabilità.
- **Segnalazione**: I Proprietari di Progetto **DOVREBBERO** istituire un canale per la divulgazione responsabile, al fine di gestire i problemi di sicurezza in modo riservato prima del rilascio pubblico.
- **Vulnerabilità sfruttate**: I Proprietari di Progetto **DEVONO** cooperare con i Computer Security Incident Response Team (CSIRT) nazionali in merito alle vulnerabilità attivamente sfruttate e seguire rigorosamente i protocolli di divulgazione coordinata per mitigare le minacce derivanti da una divulgazione irresponsabile.



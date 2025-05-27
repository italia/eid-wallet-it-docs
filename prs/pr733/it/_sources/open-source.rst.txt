.. include:: ../common/common_definitions.rst


Rilasci Open Source 
===================

In linea con i principi generali di apertura e trasparenza, i Fornitori di Wallet, i Fornitori di Credenziale e le Relying Party sono incoraggiati a considerare l'adozione di approcci open-source, anche durante la fase di sperimentazione, per promuovere la collaborazione, la revisione tra pari e i miglioramenti condivisi in tutto l'ecosistema. Questo incoraggiamento fa parte di un quadro in evoluzione, in attesa della definizione delle procedure pertinenti dalle `linee guida sull'acquisizione e il riutilizzo del software per le pubbliche amministrazioni <https://docs.italia.it/italia/developers-italia/gl-acquisition-and-reuse-software-for-pa-docs/en/stabile/index.html>`_ ai sensi dell'articolo 64-quater del CAD, che fa riferimento all'articolo 69 riguardante il rilascio del codice sorgente. L'open source è supportato dagli articoli 68 e 69 del Codice dell'Amministrazione Digitale (CAD) (e relative linee guida), dai regolamenti europei (`Artificial Intelligence Act (AI Act) <https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689>`_, `Cyber Resilience Act (CRA) <https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202402847>`_, `Interoperable Europe Act <https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202400903>`_).

Tutti gli implementatori, siano essi Fornitori di Wallet, Fornitori di Credenziale o Relying Party, proprietari del codice del prodotto (da ora in poi Proprietari di Progetti Open Source) DOVREBBERO seguire le migliori pratiche del settore per il software open-source, inclusa una documentazione adeguata, il controllo delle versioni e il coinvolgimento della comunità. In particolare:

- **Trasparenza e Documentazione**: I Proprietari di Progetti Open Source DOVREBBERO produrre una documentazione chiara e linee guida per i contributi.
- **Coinvolgimento della Comunità**: I Proprietari di Progetti Open Source DOVREBBERO favorire il coinvolgimento attivo della comunità per lo sviluppo e il supporto.
- **Controllo di Versione del Software**: I Proprietari di Progetti Open Source DOVREBBERO utilizzare sistemi di controllo delle versioni, come Git, per gestire le modifiche al codice.
- **Pratiche di Sicurezza**: I Proprietari di Progetti Open Source DOVREBBERO produrre audit regolari del codice e standard di codifica sicura.
- **Licenze**: I Proprietari di Progetti Open Source DEVONO utilizzare licenze open-source appropriate, riconosciute come "licenza libera" o "licenza open source" dalla Free Software Foundation o dalla Open Source Initiative.
- **Divulgazione Responsabile della Sicurezza**: I Proprietari di Progetti Open Source DOVREBBERO configurare procedure di divulgazione responsabile della sicurezza per gestire i problemi di sicurezza in modo appropriato, mitigando qualsiasi tipo di minaccia derivante da una divulgazione irresponsabile di problemi di sicurezza.

Fornitori di Wallet
^^^^^^^^^^^^^^^^^^^

I Fornitori di Wallet sono incoraggiati a rilasciare il loro codice sorgente, il sistema di build e tutti gli altri asset necessari alla riproducibilità dell'implementazione al fine di facilitare la trasparenza e l'audit di sicurezza all'interno dell'ecosistema IT-Wallet. Ove applicabile, il rilascio del codice sorgente DOVREBBE seguire le specifiche di seguito:

- **Regolamenti Europei**: Secondo il Regolamento consolidato (UE) 910/2014, Art 5a punto 3, `il codice sorgente dei componenti software applicativi dei Wallet di Identità Digitale Europea deve essere concesso in licenza open-source. Gli Stati membri possono prevedere che, per motivi debitamente giustificati, il codice sorgente di componenti specifici diversi da quelli installati sui dispositivi degli utenti non sia divulgato`.

Fornitori di Credenziale
^^^^^^^^^^^^^^^^^^^^^^^^

I Fornitori di Credenziale sono incoraggiati a rilasciare il loro codice sorgente sotto una licenza open-source, a partire dalla fase di sperimentazione.

Relying Party
^^^^^^^^^^^^^
Le Relying Party sono incoraggiate a seguire le stesse condizioni dei Fornitori di Credenziale per quanto riguarda il rilascio del loro codice sorgente.

Divulgazione Responsabile
^^^^^^^^^^^^^^^^^^^^^^^^^

Nel contesto europeo, il Cyber Resilience Act (CRA) impone procedure per la gestione delle segnalazioni di vulnerabilità e richiede la segnalazione delle vulnerabilità attivamente sfruttate ai Computer Security Incident Response Team (CSIRT). La Direttiva sulla sicurezza delle reti e dei sistemi informativi (UE) 2022/2555 (`NIS2 <https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32022L2555>`_) sottolinea anche la gestione delle vulnerabilità nell'ambito della gestione del rischio di cybersecurity.

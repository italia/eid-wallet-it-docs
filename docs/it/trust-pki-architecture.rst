.. include:: ../common/common_definitions.rst
.. Included via infrastructure-trust.rst at title level '-' (level 1).

PKI Architecture
----------------

I Trust Artifact di entrambi i Trust Framework sono firmati con chiavi la cui parte pubblica è certificata da un'Autorità di Certificazione.
Questa sezione fornisce la vista architetturale di tali Autorità di Certificazione.
Definisce quali di esse sono operate all'interno dell'IT-Wallet, quali certificati ciascuna emette, e quale Trust Anchor è derivato da ciascuna e attraverso quale canale tale Trust Anchor è distribuito.

Il contenuto dei certificati non è definito in questa sede.
I requisiti comuni sono definiti in :ref:`infrastructure-trust:X.509 Certificate Profile` e i requisiti specifici di ciascun certificato sono definiti insieme all'artifact che lo utilizza.
L'emissione dei certificati è parte dell'onboarding (vedere :ref:`onboarding-system:Onboarding Processes`).
L'uso dei Trust Anchor a runtime è definito in :ref:`trust-evaluation:EUDIW Trust Anchor Validation` per il Trust Framework EUDIW e in :ref:`trust-evaluation:Signing Trust Anchor Distribution`, :ref:`trust-evaluation:Wallet Trust Anchor Distribution` e :ref:`trust-evaluation:Authentication Trust Anchor Distribution` per il Trust Framework Nazionale.

Certification Hierarchies
^^^^^^^^^^^^^^^^^^^^^^^^^

All'interno dell'IT-Wallet è operata una singola Root Certification Authority nazionale.
Essa emette i certificati delle Autorità di Certificazione subordinate e non è utilizzata per alcun altro scopo.
Ciascuna Autorità di Certificazione subordinata serve un servizio, e il suo certificato è il Trust Anchor pubblicato per tale servizio.

.. _fig_pki_architecture:
.. plantuml:: plantuml/pki-architecture.puml
    :width: 99%
    :align: center
    :alt: La figura illustra le gerarchie di certificazione dell'ecosistema IT-Wallet e il canale di pubblicazione del Trust Anchor derivato da ciascuna Autorità di Certificazione.
    :caption: `Architettura PKI dell'Ecosistema IT-Wallet. <https://www.plantuml.com/plantuml/svg/dLPHRzis47xNhpYq3tvPx2tOWAqFHHN7NhDagM8xy1u23BHqaeZGP41I3hoW_tqyIYP4EuxRAa02alTztztn8vbFnZ9jcxL81Z16RNd9SsQvab1pr4pdxey19WjuQbPYjvRNJ4eKe4gmDKA1cc-mW8LkZ8LKvhNIPfWavf7B9wRP6apD2lNCPGKb4mPxAmMMh15sggIzPMk4poWsQ9tGwp5p_X_2B-UznLHhzJnMGcbu_wl_UeiQSyja9H1U4e0BbZzMMZMoQEENDRT8yqgx4cAEhpsM9uTZrUiSxwSf_Uop_Eu_D-kJjbk1i5AYSBI9mDA2LQ1vLLieEEN8bKoIdSoxMqOJJ41sVVKEc87RTE744mZrz8DcIbaOfmzoD59bARZ4dq0rrl02_UvicE253tQ5s7eqyfIpBryMUupPrILaMcqSKCESLt8qHoOwwcEBmJDeMcON_wyBdiVSIoO4skFqyVffXMNc-FSaPbawzdHfdgCnaFUGPDLMuso6OajEp9XRTYk1al17UfmsjaPfE_ztEVU9ji3YaFpLjDFxnUU3h6VZWtQ4yK4HJYHqYSOUt-iB3ME56LRSMCqEcnvMJhPxDldpI6ScQNh0UwdoPetI-WNKHthXaCdNdkll6YPSLBX7vgWtFCTGhSVTBUOPlCIv160dV-UOlzr9Ts-JPSt5sNVnPVSNKLcJ-ykhPLVILBCrFYlzw8DTvEGUNeuVGlCWRxY3gRB5Om4JQJcvrXFSq45xyvoTPl07QH1b45TyceDAZhC8K0BvStMImqUzpJ8xoVAc_K-23qp-DwvNjEEMMGmW8Y5ZfDhot4MTdnCbNbscyz6eOrhSH1O8X-M82_pr7ajFqHNkOT6h-Y1zpbiOArdogcb3EjNfXCmWbQMtnbgrTYE0HOtGO-lmrxWrm3IspxgfiI2ElvRN7iEblsTUqp93OjmIbgJWd-5lF_z1eFYcOh888ToOnl6l72Z-7uDW_cfLskaCtH1bqHO0r41we-3ix6DuKleJoomUad-Y6RfhzqDcKGZjU3IcAodfn60u_DYTCA_MZacsFUGqRhTwfqupmSdnPA2X548SfTDcqKrHFdGbHTn1skqlV83mLYwqQNQ-68sIhkAzsF1mnLuA62evXlYtXyjgFpOPzAr5dc-Tw-Q_tsI37p7PuCTCDeXDDWWcInA15Gt2QPahmObIg-SFBQEX7FkgkpVOD2kb2ovfAjAB3Nt9NDc1qjP7WoCDRgAMHLi1N0uJbtMRU_B9_MhMudy0>`_

La tabella seguente elenca le Autorità di Certificazione, i certificati emessi da ciascuna di esse e il canale attraverso il quale è distribuito il Trust Anchor derivato.
Le List of Trusted Entities e le Trusted List nominate nella tabella sono definite in :ref:`infrastructure-trust:Trusted List, Lists of Trusted Lists, and Lists of Trusted Entities`.

.. _table_pki_certification_authorities:
.. list-table:: Autorità di Certificazione e Trust Anchor Derivati
    :class: longtable
    :widths: 24 38 38
    :header-rows: 1

    * - **Autorità di Certificazione**
      - **Certificati Emessi**
      - **Distribuzione del Trust Anchor**

    * - PID Provider Sign/Seal CA
      - :ref:`infrastructure-trust:PID Provider Sign/Seal Certificate`
      - PID Providers LoTE.

    * - Wallet Provider Sign/Seal CA
      - :ref:`infrastructure-trust:Wallet Provider Sign/Seal Certificate`
      - Wallet Providers LoTE nel Trust Framework EUDIW, e la Federation Trust Anchor Entity Configuration come canale di distribuzione del National Wallet Trust Anchor nel Trust Framework Nazionale (vedere :ref:`trust-evaluation:Wallet Trust Anchor Distribution`).

    * - WRPAC CA
      - Certificati di accesso conformi al :ref:`infrastructure-trust:Wallet-Relying Party Access Certificate (WRPAC) Profile`, emessi alle Wallet-Relying Party.
      - Providers of WRPAC LoTE.
        Lo stesso Trust Anchor è inoltre pubblicato nella PID Providers LoTE, perché i trust anchor delle Access Certification Authorities per i PID Provider sono notificati all'interno della notifica del PID Provider, separatamente da quelli per le Wallet-Relying Party (vedere [`EIDAS-ARF`_], Topic 31).

    * - National Authentication CA
      - Certificati di autenticazione della Relying Party utilizzati nel Proximity Flow.
        Seguono lo stesso profilo del Wallet-Relying Party Access Certificate.
      - Entity Configuration del Federation Trust Anchor, come Authentication Trust Anchor (vedere :ref:`trust-evaluation:Authentication Trust Anchor Distribution`).

    * - WRPRC Sign/Seal CA
      - Il Sign/Seal Certificate del Provider of WRPRC (vedere :ref:`infrastructure-trust:Wallet-Relying Party Registration Certificate (WRPRC) Profile`).
      - Providers of WRPRC LoTE.

    * - Registrar Sign/Seal CA
      - :ref:`infrastructure-trust:Registrar Sign/Seal Certificate Profile`
      - Registrar LoTE.

    * - National EAA Sign/Seal CA
      - :ref:`infrastructure-trust:(Q)EAA Provider Sign/Seal Certificate`, per gli Attestati Elettronici ancorati al Trust Framework Nazionale.
      - Entity Configuration del Federation Trust Anchor, come Signing Trust Anchor (vedere :ref:`trust-evaluation:Signing Trust Anchor Distribution`).
        Per una EAA emessa nel Trust Framework EUDIW il Trust Anchor è referenziato nell'Attestation Rulebook, come descritto in :ref:`infrastructure-trust:Trust Anchor Certificate Profile`.

    * - Qualified CA of the QEAA Provider
      - :ref:`infrastructure-trust:(Q)EAA Provider Sign/Seal Certificate`, per la QEAA.
      - Member State Trusted List, pubblicata in conformità all'Articolo 22 di [`EIDAS`_].

    * - Qualified CA of the PuB-EAA Provider
      - :ref:`infrastructure-trust:PuB-EAA Provider Sign/Seal Certificate`, il certificato qualificato a supporto del sigillo elettronico qualificato dell'ente del settore pubblico (Articolo 45f(1)(b) di [`EIDAS`_]).
      - Member State Trusted List, pubblicata in conformità all'Articolo 22 di [`EIDAS`_].

La Qualified CA del QEAA Provider e la PuB-EAA Provider Sign/Seal CA non sono subordinate alla Root Certification Authority nazionale.
Entrambe appartengono al perimetro di un Qualified Trust Service Provider e seguono il proprio regime di vigilanza e pubblicazione.
Il Sign/Seal Certificate di un PuB-EAA Provider è un sigillo elettronico qualificato emesso da un Qualified Trust Service Provider (Articolo 45f di [`EIDAS`_]).

Revocation Trust Anchors
""""""""""""""""""""""""""

Nell'ambito di queste specifiche, si applicano le seguenti condizioni aggiuntive relative ai Trust Anchor di revoca:

- Nell'ambito del Trust Framework EUDIW, i Trust Anchor utilizzati per validare i meccanismi di revoca delle catene di certificati WRPRC, PID e PuB-EAA sono gli stessi Trust Anchor notificati utilizzati dalle corrispondenti PKI di firma.
- Nell'ambito del Trust Framework Nazionale, i Signing Trust Anchor degli EAA Provider sono anche i Trust Anchor utilizzati per validare lo stato di revoca delle catene di certificati di firma EAA.
- Per le Wallet Instance Attestation e le Key Attestation, il Fornitore di Wallet DEVE utilizzare lo stesso Trust Anchor per la validazione della firma e per la validazione delle informazioni di stato o di revoca applicabili. Nel Trust Framework EUDIW, questo Trust Anchor è pubblicato nella Wallet Providers LoTE; nel Trust Framework Nazionale, lo stesso materiale di chiave è distribuito come National Wallet Trust Anchor attraverso la Federation Trust Anchor Entity Configuration (vedere :ref:`trust-evaluation:Wallet Trust Anchor Distribution`).
- Quando un Fornitore di Wallet opera in entrambi i Trust Framework, il suo National Wallet Trust Anchor DEVE essere lo stesso certificato del Trust Anchor notificato alla Commissione Europea e pubblicato nella Wallet Providers LoTE sotto la ``ServiceDigitalIdentity`` del Fornitore di Wallet. La Entity Configuration nazionale è un canale di distribuzione aggiuntivo e NON DEVE introdurre un secondo Trust Anchor.

.. note::
  L'Autorità di Certificazione che emette i Wallet-Relying Party Access Certificate e l'Autorità di Certificazione che emette i certificati di autenticazione della Relying Party del Trust Framework Nazionale utilizzano lo stesso profilo di certificato.

.. note::
  Le Federation Entity Key non sono certificate dalle Autorità di Certificazione descritte in questa sezione.
  Il vincolo tra una Federation Entity e le sue chiavi è fornito dalla Entity Configuration e dal Subordinate Statement emesso dal suo superiore, che sono validati attraverso la Federation Trust Chain e non con un certification path (vedere :ref:`infrastructure-trust:National Trust Artifacts`).
  La Entity Configuration del Federation Trust Anchor è utilizzata come canale di distribuzione dei Trust Anchor delle gerarchie X.509.

Design Principles
^^^^^^^^^^^^^^^^^

Le gerarchie descritte sopra seguono i principi elencati di seguito.

- **Una Sign/Seal Certification Authority per ruolo notificato.** Ciascun ruolo che firma o sigilla un artifact ha una distinta Sign/Seal Certification Authority.
- **Una singola WRPAC Certification Authority.** All'interno dell'IT-Wallet i certificati di accesso sono emessi da una singola Autorità di Certificazione, sia alle Wallet-Relying Party sia ai PID Provider, in quanto seguono lo stesso profilo e la stessa certificate policy.
  I certificati di autenticazione della Relying Party del Trust Framework Nazionale sono emessi da una distinta Autorità di Certificazione.
- **Nessun Trust Anchor senza un consumatore.** All'interno dell'IT-Wallet un Trust Anchor è pubblicato in un canale di distribuzione solo quando una procedura di trust evaluation definita in questa specifica lo ottiene da tale canale.
- **La Root Certification Authority è al di fuori del validation path.** Il certificato Trust Anchor è il punto di terminazione del trust della path validation (vedere :ref:`infrastructure-trust:Trust Anchor Certificate Profile`), pertanto la Root Certification Authority non è mai valutata a runtime e il suo certificato non è pubblicato in alcuna List.
  Essa fornisce una governance comune alle Autorità di Certificazione subordinate e nessuna relazione di trust di per sé.
  Una compromissione della Root Certification Authority non è rilevata dalla path validation ordinaria e, all'interno dell'IT-Wallet, è gestita re-emettendo e ri-notificando i Trust Anchor interessati.
- **Solo end entity al di sotto di un Trust Anchor pubblicato.** All'interno dell'IT-Wallet il Trust Anchor pubblicato è l'Autorità di Certificazione subordinata del servizio, e nessun ulteriore strato di Autorità di Certificazione è emesso al di sotto di essa.
  Ciò è coerente con la raccomandazione ``pathLenConstraint`` di :ref:`infrastructure-trust:Trust Anchor Certificate Profile`.
- **Separazione delle chiavi per scopo.** Un Trust Anchor pubblicato per uno scopo non è utilizzato per certificare gli artifact di un altro scopo.
  Un'entità verificatrice deve poter distinguere quali Trust Anchor sono utilizzabili per quale categoria di Attestation, come richiesto da [`EIDAS-ARF`_].

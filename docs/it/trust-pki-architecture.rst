.. include:: ../common/common_definitions.rst
.. Included via infrastructure-trust.rst at title level '-' (level 1).

PKI Architecture
----------------

Gli Artifact di Trust di entrambi i Trust Framework sono firmati con chiavi la cui parte pubblica è certificata da una Certification Authority.
Questa sezione fornisce la vista architetturale di tali Certification Authorities.
Definisce quali di esse sono operate nell'IT-Wallet, quali certificati ciascuna emette e quale Trust Anchor deriva da ciascuna, nonché attraverso quale canale tale Trust Anchor è distribuito.

Il contenuto dei certificati non è definito qui.
I requisiti comuni sono definiti in :ref:`infrastructure-trust:X.509 Certificate Profile` e i requisiti specifici di ciascun certificato sono definiti insieme all'artifact che lo utilizza.
L'emissione dei certificati fa parte dell'onboarding (vedere :ref:`onboarding-system:Onboarding Processes`).
L'uso dei Trust Anchor a runtime è definito in :ref:`trust-evaluation:EUDIW Trust Anchor Validation` per il EUDIW Trust Framework e in :ref:`trust-evaluation:Signing Trust Anchor Distribution` e :ref:`trust-evaluation:Authentication Trust Anchor Distribution` per il National Trust Framework.

Certification Hierarchies
^^^^^^^^^^^^^^^^^^^^^^^^^

Nell'IT-Wallet è operata una singola Root Certification Authority nazionale.
Essa emette i certificati delle subordinate Certification Authorities e non è utilizzata per altri scopi.
Ciascuna subordinate Certification Authority serve un servizio e il suo certificato è il Trust Anchor pubblicato per quel servizio.

.. _fig_pki_architecture:
.. plantuml:: plantuml/pki-architecture.puml
    :width: 99%
    :align: center
    :alt: La figura illustra le gerarchie di certificazione dell'ecosistema IT-Wallet e il canale di pubblicazione del Trust Anchor derivato da ciascuna Certification Authority.
    :caption: `PKI Architecture of the IT-Wallet Ecosystem. <https://www.plantuml.com/plantuml/svg/dLPHJoCt47xVNp6wUyXBoRQebTfxEDqIGez2kIK9IX-GAhCxsRLmR6HxWr9q_xqUEt7N2I6zMoIGn_DztupzsUQJiKpRRYco0OnGMxxW5RDSIMWvQgOhzyS0apKyTGzYErUrJ4eKe1PWMuGQDLzX3JFT6Gk5h5gbpJ3Bp2ENJqop9PYMrUgPomOMJ1ZipTIuO9sm5qhQ6xP4-8nYXTO9lPupvVyW_7JQcooqLiyZ9PI6zp_xhpUfiR9CDWBX9GCuOzLZerKdwv0_Rxb5YYljMaWvllPOdXoEDQzplByew6UNvLV_kQWlsgu5meCIjQFD12uiM0MQDws5cbEDNCaisygyks4KO0BAgyjtm0pS53Cdda7ifvyqKSh2gBYNUQuM2y4b_W2giuRNw7TdnGIlVR9hnBPvxYadNxxCTXZBotCejLeve8OfRsG-HIOsr8ScesVG16QN_xTBdgRSSoO4siFqwVnnXNdf-7Sa9cKnydH5LQ4nKFMGPDMWSJ91iIOdbinDkvb8IVW3QrnqjaLfj_uFDVU9ri3IbEhLiekxsUUzgYUZlUM8uxqcd4XS9HfxV6zTQ9WgJB3Xncgsl-XnvkXoJyQ_7rYPSL7iyPwhgbkYj7u2zO6rSCZiQy_rjnqJBYlU8rFKArxzrwt7tSwc9RoajKJWHlxMCVz_9zs-JLPsPoVVn5VUdILjZU_EB-URbYuqM-Apqey-sMMEx-3by24qz_AQEvXQ13pMC9QMasizmJKTj3VFsL66S906IGLfnySvgEMqYWWba3zNHpbyrjiiawCiRzh_67ZVv7_Yye5st3AB4KGaP8n2MrwvhDDJeiJBysAQvnkcsNLYWNXO3hWWNE-9z0MwnZqiULNlfQzv3ICb5xpfGif6zM9CPf3AqbjZhLgw4S2iHUYnRV1Nk3R0D8PdtRHO4ySVyokFuTBVCwzfcI4nhWbBKl3Ny9SVVoDGUbCnMSSKRapd-1ySAFqVmyFeQbNQwGpT46KT6W1QG7gZuEJaOtnI-e5vcGx9Fqc4xjhTb4cIGZkUZEbAoZPYC1n-t9mmhnR691iEUHZJLc_LAHATd0OZ3PKGywYSKCKcHFNGbPHmKnyXG3iC7o3Fq-SeSKYUPw6H119U52wRtTniq3SCEJduqSM_tJg3xx7EuFkiCqYjCuZMoJA13GtY6PWgmObIg-SFWT5GZNtLxSjgkWUbQoufbEYbDZrdhkr8QTk3oOa6DycI9Li1N0upLtMeFVlaVdLByIy0>`_

La tabella seguente elenca le Certification Authorities, i certificati emessi da ciascuna di esse e il canale attraverso cui è distribuito il Trust Anchor derivato.
Le Lists of Trusted Entities e le Trusted Lists nominate nella tabella sono definite in :ref:`infrastructure-trust:Trusted List, Lists of Trusted Lists, and Lists of Trusted Entities`.

.. _table_pki_certification_authorities:
.. list-table:: Certification Authorities and Derived Trust Anchors
    :class: longtable
    :widths: 24 38 38
    :header-rows: 1

    * - **Certification Authority**
      - **Issued Certificates**
      - **Trust Anchor Distribution**

    * - PID Provider Sign/Seal CA
      - :ref:`infrastructure-trust:PID Provider Sign/Seal Certificate`
      - PID Providers LoTE.

    * - Wallet Provider Sign/Seal CA
      - :ref:`infrastructure-trust:Wallet Provider Sign/Seal Certificate`
      - Wallet Providers LoTE.

    * - WRPAC CA
      - Access certificates conformi al :ref:`infrastructure-trust:Wallet-Relying Party Access Certificate (WRPAC) Profile`, emessi alle Wallet-Relying Parties.
      - Providers of WRPAC LoTE.
        Lo stesso Trust Anchor è pubblicato anche nella PID Providers LoTE, poiché i trust anchor delle Access Certification Authorities per i PID Provider sono notificati all'interno della notifica del PID Provider, separatamente da quelli per le Wallet-Relying Parties (vedere [`EIDAS-ARF`_], Topic 31).

    * - National Authentication CA
      - Certificati di autenticazione delle Relying Party utilizzati nel Proximity Flow.
        Seguono lo stesso profilo del Wallet-Relying Party Access Certificate.
      - Entity Configuration del Federation Trust Anchor, come Authentication Trust Anchor (vedere :ref:`trust-evaluation:Authentication Trust Anchor Distribution`).

    * - WRPRC Sign/Seal CA
      - Il Sign/Seal Certificate del Provider of WRPRC (vedere :ref:`infrastructure-trust:Wallet-Relying Party Registration Certificate (WRPRC) Profile`).
      - Providers of WRPRC LoTE.

    * - Registrar Sign/Seal CA
      - :ref:`infrastructure-trust:Registrar Sign/Seal Certificate Profile`
      - Registrar LoTE.

    * - National EAA Sign/Seal CA
      - :ref:`infrastructure-trust:(Q)EAA Provider Sign/Seal Certificate`, per le Credenziali Digitali ancorate al National Trust Framework.
      - Entity Configuration del Federation Trust Anchor, come Signing Trust Anchor (vedere :ref:`trust-evaluation:Signing Trust Anchor Distribution`).
        Per un EAA emesso nel EUDIW Trust Framework il Trust Anchor è referenziato nell'Attestation Rulebook, come descritto in :ref:`infrastructure-trust:Trust Anchor Certificate Profile`.

    * - Qualified CA of the QEAA Provider
      - :ref:`infrastructure-trust:(Q)EAA Provider Sign/Seal Certificate`, per la QEAA.
      - Member State Trusted List, pubblicata conformemente all'articolo 22 di [`EIDAS`_].

    * - Qualified CA of the PuB-EAA Provider
      - :ref:`infrastructure-trust:PuB-EAA Provider Sign/Seal Certificate`, il certificato qualificato a supporto del sigillo elettronico qualificato dell'ente del settore pubblico (articolo 45f(1)(b) di [`EIDAS`_]).
      - Member State Trusted List, pubblicata conformemente all'articolo 22 di [`EIDAS`_].

La Qualified CA of the QEAA Provider e la PuB-EAA Provider Sign/Seal CA non sono subordinate alla Root Certification Authority nazionale.
Entrambe appartengono al perimetro di un Qualified Trust Service Provider e seguono il proprio regime di supervisione e pubblicazione.
Il Sign/Seal Certificate di un PuB-EAA Provider è un sigillo elettronico qualificato emesso da un Qualified Trust Service Provider (articolo 45f di [`EIDAS`_]).

.. note::
  La Certification Authority che emette i Wallet-Relying Party Access Certificates e la Certification Authority che emette i certificati di autenticazione delle Relying Party del National Trust Framework utilizzano lo stesso certificate profile.

.. note::
  Le Federation Entity Keys non sono certificate dalle Certification Authorities descritte in questa sezione.
  Il binding tra una Federation Entity e le proprie chiavi è fornito dall'Entity Configuration e dal Subordinate Statement emesso dal superiore, che sono validati attraverso la Federation Trust Chain e non con un certification path (vedere :ref:`infrastructure-trust:National Trust Artifacts`).
  L'Entity Configuration del Federation Trust Anchor è utilizzata come canale di distribuzione per i Trust Anchor delle gerarchie X.509.

Design Principles
^^^^^^^^^^^^^^^^^

Le gerarchie descritte sopra seguono i principi elencati di seguito.

- **One Sign/Seal Certification Authority per notified role.** Ciascun ruolo che firma o sigilla un artifact ha una Sign/Seal Certification Authority distinta.
- **A single WRPAC Certification Authority.** Nell'IT-Wallet i certificati di accesso sono emessi da una singola Certification Authority, sia alle Wallet-Relying Parties sia ai PID Provider, poiché seguono lo stesso profilo e certificate policy.
  I certificati di autenticazione delle Relying Party del National Trust Framework sono emessi da una Certification Authority distinta.
- **No Trust Anchor without a consumer.** Nell'IT-Wallet un Trust Anchor è pubblicato in un canale di distribuzione solo quando una procedura di valutazione del trust definita in questa specifica lo ottiene da quel canale.
- **The Root Certification Authority is outside the validation path.** Il certificato Trust Anchor è il trust termination point della path validation (vedere :ref:`infrastructure-trust:Trust Anchor Certificate Profile`), pertanto la Root Certification Authority non viene mai valutata a runtime e il suo certificato non è pubblicato in alcuna List.
  Fornisce una governance comune alle subordinate Certification Authorities e non stabilisce di per sé alcuna relazione di trust.
  Un compromissione della Root Certification Authority non è rilevata dalla path validation ordinaria e, nell'IT-Wallet, è gestita mediante re-emissione e re-notifica dei Trust Anchor interessati.
- **Only end entities below a published Trust Anchor.** Nell'IT-Wallet il Trust Anchor pubblicato è la subordinate Certification Authority del servizio e non viene emesso alcun ulteriore livello di Certification Authority al di sotto di essa.
  Ciò è coerente con la raccomandazione ``pathLenConstraint`` del :ref:`infrastructure-trust:Trust Anchor Certificate Profile`.
- **Separation of the keys by purpose.** Un Trust Anchor pubblicato per uno scopo non è utilizzato per certificare gli artifact di un altro scopo.
  Un'entità verificante DEVE essere in grado di distinguere quali Trust Anchor sono utilizzabili per quale categoria di Attestation, come richiesto da [`EIDAS-ARF`_].

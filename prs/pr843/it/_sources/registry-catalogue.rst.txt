.. include:: ../common/common_definitions.rst


Catalogo degli Attestati Elettronici
====================================

Il Catalogo degli Attestati Elettronici è il registro di tutti gli Attestati Elettronici disponibili riconosciuti all'interno dell'ecosistema IT-Wallet. È pubblicato dal Trust Anchor ed è pubblicamente disponibile per tutte le Entità attraverso un endpoint di Federazione specializzato. Funge da punto di riferimento unico per tutti gli attori coinvolti nel processo di emissione, verifica e utilizzo degli Attestati Elettronici.

Il Catalogo degli Attestati Elettronici mira a:

  1. Facilitare la *discovery* degli Attestati Elettronici per gli Utenti.
  2. Standardizzare la descrizione tecnica e funzionale degli Attestati Elettronici.
  3. Abilitare l'interoperabilità tra diversi Fornitori di Attestati Elettronici e Relying Party.
  4. Semplificare il processo di integrazione per i Fornitori di Wallet e le Relying Party.
  5. Garantire la fiducia nell'ecosistema attraverso informazioni certificate.
  6. Fornire trasparenza sull'ecosistema degli Attestati Elettronici disponibili.


Le principali Entità coinvolte nel Catalogo degli Attestati Elettronici sono:

  - **Trust Anchor**: Gestisce e mantiene il Catalogo degli Attestati Elettronici, garantendone l'autenticità e l'integrità.
  - **Organismo di Supervisione**: Interagisce con il Trust Anchor e il Catalogo degli Attestati Elettronici per monitorare la fase di registrazione garantendo sicurezza e privacy secondo le normative nazionali/europee, mantenendo tutte le informazioni affidabili e aggiornate.
  - **Fornitori di Attestati Elettronici**: Le entità autorizzate a emettere Attestati Elettronici, registrandoli nel Catalogo.
  - **Relying Party**: Utilizzano il Catalogo degli Attestati Elettronici per raccogliere tutte le informazioni necessarie sugli Attestati Elettronici che intendono richiedere durante la fase di presentazione.
  - **Fornitori di Wallet**: Accedono al Catalogo degli Attestati Elettronici per identificare gli Attestati Elettronici disponibili e per recuperare tutte le informazioni necessarie per integrarli nelle loro Soluzioni Tecniche.
  - **Utenti**: Gli Utenti che utilizzano indirettamente il Catalogo degli Attestati Elettronici attraverso le loro Istanze del Wallet per visualizzare e richiedere Attestati Elettronici.
  - **Fonti Autentiche**: Le Entità che detengono i dati originali attestati negli Attestati Elettronici. Forniscono supporto ai Fornitori di Attestati Elettronici nella registrazione degli stessi nel Catalogo.


.. _fig_catalogue.svg:
.. plantuml:: plantuml/credential-catalogue-entities.puml
    :width: 99%
    :alt: La figura illustra le Entità degli Attestati Elettronici.
    :caption: `Diagramma Entità-Relazione del Catalogo degli Attestati Elettronici. <https://www.plantuml.com/plantuml/svg/ZLJ1Rkis4BpxAxP6WQP00X-QtjeWgPEsFXGmuXGz6ZIvbeb8fCfTEbM__YrDELAUb6ST34khuSnmESjxOXKuLYKysiAoAc4PqA1ZcnwL57mH4Pwam1Pfzfrrkem6uPVbxM9vkrtwglPEy7UpsG_mY7lh43RhvzNBqwO7vbWh4tvQQ5zLtjsDVDbxnpVg3SbNUFFpGcDWkxTQCKv06p6wKpG5MdhzEW4M2GDDyUcBAJ1XEsAO07p5PgAx2J1hjbe5Cm69_-c3SWLkLSbJ-etqohwUW7nJPOaNAHVM4LkER5CuPhFtL5tfSmIlOJvCA7KHdGlW6GjB79hql1H4471eQ-3t85v07PKjrQv46A6JXTzJ7IpZh_DpfkO_Yg4r1lBkAlLTkF-MlvE6PVi_EeAtWmTZINivP53EYEg_4OalQIG-uU-soo4IFpXzy4dd9Rr1VarwwVUNSgf0EgbKoZgM7m4Vy9i3t1ULY8dcfY76wefYBT6qv4FpcpUD26ow2gJIITGxopxGkPig7HJK1qK8w2W6wmeWrFB0pScQQ1sLRlgwlP7kz2rHn42Zfmkh_34vU8WiJP1k6y3sBf9DAuP4SF4isq7eP0EMZNXUgv2OKdHo0ThAF9_ogQ_l4GJsK2Wf1R1kxqELsw1sFZBeSUN-O7NoUIhMmH-joRl_vrI1jjJkMMia6dgmZh48Yh4lcgeUCl471xdKQIlfP5gZDpu64KX2vnAqjQJ-foyD-22DTTBOD0sWc54uZ6XTx7Wtq6c0fBqVijrjg8lqTPVd7A6uAoqTiflVHQMD7JfJUm4Ahz0E4_nnXbQEPQ5c6LBBX_4rVJkVXZtuT1gPe8jjVs6-VZ2CzGQiQvSE-tyc6pSxo6fVyezFuZXc8TCDizVnTP7pO4_BzatlmjG3hdmV3XZJw12qaLuvOkKqGfq11dPDNhvzR0dw3bREs82Qo-RzHgN-bKfVsRYNECIg_080>`_


.. .. figure:: ../../images/catalogue.svg
..     :figwidth: 100%
..     :align: center
..     :target: https://www.plantuml.com/plantuml/svg/ZLHDZnit3BtxLp16WMw1E3wqlHGeaDJR3mD9Qwopw751I_HOM8qq5JdhJdzzAMkyCnixs3aOy53aUq_aezwpO9AszhCtBXZVMeA3ICC_BPS9Z-yg9uTsrp8b4uDGa7Scril6OyWr2nRhtMwv-c6noQ7xJn-NDR9Gqj33AjPD3BccoVYpR-6MzYuGR3Ttwy-_RcTlRFbUh_xwy_xkumHYQHkqwVj1WDFJnLup5jma9yGz_t2R7dofvNKCHSh5uGa1ZyInfiMFIqD9tDuP59fMO55mXpmnsqVpE2qptvydQexLn4p5VA8qBVUHkkbAfsKw-s0msMd9zAyvOAZe0RrC70NneyHcMl8HlQSfm4iNM9oquiuUcisU_NrZKD37ggMtCBzrbTClM2MoUkRGCwpEvtDDkAFAiQGk_rzfHjBarCSWxa4b0JwXyxZp15VWjF2RulQVvsVZpRzJGHjA7CDD7eLYtpEb4uSJzny5XkCXWdLieauVC5Xb_QSbbjSuCfxY3zULrB9y2EOGCy_d_0NbC_FbtoSCM16VM6fqGVJ788ThzncwCoPLuoddjcEX-eRRHZthEARkbsWx9TWE4SYX4saCJcBYSpSn3mkQ0p811MwJ2nKm6VqZtKcQSZsXwSQyezKV-1rpIuclJXVMvJ0h-D2ADa6xRI4VYgDyQHJ80A_Eib-CWJQHxrJp1bD6ojOf0UWZypBbKr-VBGWIeK8D9N1X7rDTse2xs0gOwypZBHleot9iKdnojjp-xrC4-b1_PsE8-LA32q9LGg4nQOv6AC0l59JGm8tQoLnZjh5DIf29pY7eOvdzZ-WjnAID3UWXRmEW22c6LQvNEpuiTLuWRUyBRmyN6YpzTl1piL2xyuuFHSrlojBRZe9jeYOghi9UElZb3gs3QA4HXgEJm_MQiPolcZt5F8q2CDXsN5YU7qhNUWCkzAMN_J-3NHTxuTKnvUzVi-CL2GNkqdi3tc2v2EvKjkz63wQvm2hluGLYNXs6tjBhm8B143GbmSAkA-KFjpt0MC4wM9V8YE-UNrGUFwdyXOpt56nR-_y1


La seguente tabella riassume le principali informazioni che DEVONO essere fornite dal Catalogo degli Attestati Elettronici:

.. list-table:: Catalogo degli Attestati Elettronici - Informazioni principali
   :class: longtable
   :widths: 30 70
   :header-rows: 1

   * - Informazioni relative a
     - Descrizione
   * - Metadati dell'Attestato Elettronico
     - Informazioni identificative essenziali e caratteristiche dell'Attestato Elettronico, tra cui:

       - **Identificatore univoco dell'Attestato Elettronico**: Una stringa che identificativa univocamente il tipo di Attestato Elettronico.
       - **Metodi di autenticazione dell'Utente**: Meccanismi di autenticazione dell'Utente utilizzati per richiedere l'Attestato Elettronico, se richiesti dai Fornitori di Attestati Elettronici o dalle Fonti Autentiche.
       - **Livello minimo di Garanzia**: Il Livello di Garanzia minimo richiesto per l'affidabilità dell'Attestato Elettronico. DEVE tenere conto del Livello di Garanzia dell'autenticazione dell'Utente, quando applicabile, e dell'Istanza del Wallet.
       - **Caratteristiche di visualizzazione aggiuntive**: Specifiche visive e di formattazione, come un'immagine di riferimento di sfondo, logo, ecc.
   * - Fornitori di Attestati Elettronici
     - Dettagli sull'organizzazione autorizzata a emettere l'Attestato Elettronico, come:

       - **Identificatori del Fornitore di Attestati Elettronici**: Identificativo univoco del Fornitore dell'Attestato Elettronico.
       - **Tipologia di Fornitore di Attestati Elettronici**: Classificazione come ad esempio Fornitore di Attestati Elettronici di Dati di Identificazione Personale, Fornitore di Attestati Elettronici di Attributi (Qualificati) o Fornitore di Attestati Elettronici Pubblici di Attributi.
       - **Informazioni aggiuntive**: Dettagli amministrativi come la denominazione, un codice amministrativo e informazioni di contatto.
   * - Fonti Autentiche
     - Informazioni sulla Fonte Autentica dei dati, come:

       - **Identificativi della Fonte Autentica**: Identificativo univoco della Fonte Autentica dell'Attestato Elettronico.
       - **Tipologia di Fonte Autentica**: Classificazione come Entità Pubblica o Privata.
       - **Informazioni aggiuntive**: Dettagli amministrativi come la denominazione, un codice amministrativo e informazioni di contatto.
   * - Specifiche Tecniche
     - Dettagli tecnici, tra cui:

       - **Schemi dell'Attestato Elettronico**: Specifiche relative a framework e struttura dati.
       - **Formati dell'Attestato Elettronico**: Standard di formato dati e codifica.
       - **Policy di autenticazione**: Metodi e requisiti per la verifica.
   * - Termini di Utilizzo
     - Condizioni e limitazioni per l'utilizzo dell'Attestato Elettronico, come:

       - **Validità dell'Attestato Elettronico**: Periodo di tempo durante il quale l'Attestato Elettronico è valido e, quando applicabile, meccanismi e dettagli tecnici per invalidare gli Attestati Elettronici (metodi di revoca/sospensione).
       - **Policy di restrizione**: Se applicabile, regole che governano l'uso dell'Attestato Elettronico e limitazioni secondo le normative nazionali. È utilizzata, ad esempio, per specificare se solo tipologie specifiche di Entità autorizzate, ad esempio Fornitore di Attestati Elettronici Pubblici di Attributi e Soluzioni Wallet pubbliche, possono emettere e ottenere l'Attestato Elettronico.
       - **Pricing Policy**: Informazioni relative ai modelli tariffari dell'Attestato Elettronico, come `free`, `issuance_based`, `verification_based`.
       - **Scopi dell'Attestato Elettronico**: Informazioni relative agli scopi consentiti per cui l'Attestato Elettronico può essere utilizzato. Ogni tipo di Attestato Elettronico può essere utilizzato per più scopi.
   * - Attributi dell'Utente e Riferimenti Tassonomici
     - Informazioni sul contenuto e sulla classificazione:

       - **Elenco degli attributi visualizzati**: Contenuto specifico dell'Attestato Elettronico visualizzato all'Utente.
       - **Riferimenti tassonomici strutturati**: Sistemi di classificazione e vocabolari controllati utilizzati.


Il Trust Anchor DEVE pubblicare e mantenere aggiornate tutte le informazioni all'endpoint `.well-known` del Catalogo degli Attestati Elettronici garantendo l'affidabilità, l'autenticità e l'integrità dei dati. In particolare, il Catalogo degli Attestati Elettronici, gli attributi e la tassonomia DEVONO essere disponibili attraverso l'endpoint ``.well-known/credential-catalogue``.

Categorie di Attestati Elettronici
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gli Attestati Elettronici riconosciuti all'interno dell'ecosistema IT-Wallet sono classificati gerarchicamente e standardizzati secondo i seguenti domini e categorie principali. Categorie aggiuntive POSSONO essere aggiunte man mano che l'ecosistema IT-Wallet cresce.

.. _it-wallet-dc-domains:
.. list-table:: Domini e Categorie degli Attestati Elettronici
   :class: longtable
   :header-rows: 1
   :widths: 20 30 50

   * - **Dominio**
     - **Categoria**
     - **Descrizione**
   * - *IDENTITY*
     - * PERSON_IDENTIFICATION
       * ELECTRONIC_RESIDENCY
     - Attestati Elettronici che stabiliscono o verificano l'identità di una persona, inclusi documenti di identità fisici e digitali legalmente riconosciuti dalle leggi nazionali.
   * - *AUTHORIZATION*
     - * DRIVING_LICENSE
       * PROFESSIONAL_LICENSE
       * TRAVEL_DOCUMENT
       * ACCESS_PERMIT
     - Attestati Elettronici che concedono permessi specifici, diritti o autorizzazioni per svolgere determinate attività o accedere ad aree ristrette.
   * - *EDUCATION*
     - * ACADEMIC_DEGREE
       * CERTIFICATE
       * TRAINING_RECOGNITION
     - Credenziali relative a titoli di studio, qualifiche e certificati professionali.
   * - *HEALTH*
     - * INSURANCE_CARD
       * DISABILITY_CARD
       * MEDICAL_PRESCRIPTION
     - Attestati Elettronici relativi all'accesso all'assistenza sanitaria, alla storia medica, alla copertura assicurativa e ai documenti relativi alla salute.
   * - *FINANCIAL*
     - * INCOME_CERTIFICATE
       * TAX_STATEMENT
       * FAMILY_ECONOMIC_STATUS
     - Attestati Elettronici che attestano lo stato finanziario, i livelli di reddito, la tassazione o la situazione economica di individui o famiglie.
   * - *MEMBERSHIP*
     - * ASSOCIATION
       * LOYALTY_PROGRAM
       * CLUB_MEMBERSHIP
     - Attestati Elettronici che confermano l'affiliazione a organizzazioni, la partecipazione a programmi o lo stato di appartenenza.
   * - *ATTESTATION*
     - * PUBLIC_STATEMENT
       * CIVIL_STATUS
       * CERTIFICATION
     - Attestati Elettronici che forniscono dichiarazioni ufficiali, conferme di stato o certificazioni rilasciate dalle autorità.


Struttura del Catalogo degli Attestati Elettronici
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Il contenuto del Catalogo degli Attestati Elettronici è protetto in un JWS che contiene i seguenti parametri dell'header JOSE:

.. _table_catalogue_parameters:
.. list-table::
   :class: longtable
   :header-rows: 1
   :widths: 25 50 25

   * - Header JOSE
     - Descrizione
     - Riferimento
   * - **typ**
     - OBBLIGATORIO. DEVE essere valorizzato con la stringa ``JOSE``.
     - [:rfc:`7515` Sezione 4.1.9].
   * - **alg**
     - OBBLIGATORIO. Un identificativo di algoritmo di firma digitale come da registro IANA "JSON Web Signature and Encryption Algorithms". DEVE essere uno degli algoritmi supportati nella Sezione :ref:`Algoritmi Crittografici <algorithms:Algoritmi Crittografici>` e NON DEVE essere impostato a ``none`` o con un identificativo di algoritmo simmetrico (MAC).
     - [:rfc:`7515` Sezione 4.1.1].
   * - **kid**
     - OBBLIGATORIO. Identificativo univoco della chiave pubblica.
     - [:rfc:`7515` Sezione 4.1.4].
   * - **x5c**
     - OPZIONALE. Contiene il Certificato di chiave pubblica X.509 o la catena di Certificati [:rfc:`5280`] corrispondente alla chiave utilizzata per firmare digitalmente il JWS. Quando il valore del parametro dell'header `kid` è presente, DEVE riferirsi alla stessa chiave pubblica crittografica della foglia attestata dal Certificato X.509.
     - [:rfc:`7515` Sezione 4.1.6.].
   * - **cty**
     - OBBLIGATORIO. DEVE essere impostato a ``application/json``.
     - [:rfc:`7515` Sezione 4.1.6.].

Il payload JWS contiene i seguenti parametri:

.. list-table:: Campi di primo livello del Catalogo
   :class: longtable
   :header-rows: 1
   :widths: 30 70

  * - Nome
    - Descrizione
  * - **catalog_version**
    - OBBLIGATORIO. Versione del formato del Catalogo degli Attestati Elettronici.
  * - **iss**
    - OBBLIGATORIO. Identificativo del Fornitore del Catalogo degli Attestati Elettronici.
  * - **last_modified**
    - OBBLIGATORIO. Timestamp dell'ultima modifica al Catalogo degli Attestati Elettronici.
  * - **taxonomy_uri**
    - OBBLIGATORIO. URI del documento di riferimento della tassonomia degli attributi.
  * - **taxonomy_uri#integrity**
    - OPZIONALE. Digest crittografico del documento di tassonomia per la verifica dell'integrità.
  * - **credentials**
    - OBBLIGATORIO. Array contenente le definizioni degli Attestati Elettronici.
  * - **wallet_attestation**
    - OBBLIGATORIO. Oggetto JSON contenente le definizioni per le Attestazioni del Wallet supportate, inclusi i loro formati supportati, le claims associate e i Livelli di Assurance (LoA). Questo oggetto è utilizzato da altre entità, come gli Issuer e le Relying Parties, per recuperare informazioni sulle Attestazioni di Wallet supportate all'interno dell'ecosistema.

Ogni elemento dell'array ``credentials`` contiene almeno le seguenti informazioni:

.. list-table:: Campi di primo livello di ogni voce di Attestato Elettronico
  :class: longtable
  :header-rows: 1
  :widths: 30 70

  * - Nome del Campo
    - Descrizione
  * - **version**
    - OBBLIGATORIO. Versione della definizione dell'Attestato Elettronico.
  * - **credential_type**
    - OBBLIGATORIO. Identificativo univoco del tipo di Attestato Elettronico.
  * - **legal_type**
    - OBBLIGATORIO. Classificazione legale dell'Attestato Elettronico (es., ``pub-eaa``, ``qeaa``, ``eaa``).
  * - **localization**
    - OPZIONALE. Impostazioni di localizzazione, inclusi:

      * **default_locale**: localizzazione predefinita per il testo.
      * **available_locales**: Elenco delle localizzazioni supportate.
      * **base_uri**: URI base per le risorse di localizzazione.
      * **version**: Versione dei file di localizzazione.
  * - **name**
    - OBBLIGATORIO. Nome *human-readable* dell'Attestato Elettronico. Un suffisso ``_l10n_id`` PUÒ essere aggiunto per la gestione della localizzazione del contenuto.
  * - **description**
    - OBBLIGATORIO. Descrizione *human-readable* dell'Attestato Elettronico. Un suffisso ``_l10n_id`` PUÒ essere aggiunto per la gestione della localizzazione del contenuto.
  * - **restriction_policy**
    - OPZIONALE. Restrizioni legali sulle Soluzioni tecniche di Fornitori di Wallet e/o di Attestati Elettronici autorizzati a richiedere/emettere un Attestato Elettronico.

      * **allowed_wallet_ids**: Elenco degli identificativi delle Soluzioni Tecniche dei Fornitori di Wallet consentite.
      * **allowed_issuer_ids**: Elenco degli identificativi delle Soluzioni Tecniche dei Fornitori di Attestati Elettronici autorizzati. Se presente, rappresenta una whitelist di Fornitori di Attestati Elettronici che possono essere aggiunti dal Trust Anchor nel campo **issuers** del corrispondente Attestato Elettronico.
  * - **pricing_policy**
    - OPZIONALE. Informazioni sui tariffari dell'Attestato Elettronico, come ad esempio:

      * **models**: OBBLIGATORIO. Array di modelli di tariffari applicabili all'Attestato Elettronico, ciascuno contenente

        - **pricing_type**: Tipo di modello di tariffario, come ``issuance_based``, ``verification_based``, ``subscription_based``, ``other``.
        - **price**: Costo associato al modello.
        - **currency**: Valuta della tariffa.

      * **pricing_model_uri**: URI alla documentazione dettagliata del modello di tariffario.
  * - **validity_info**
    - Informazioni sulla validità dell'Attestato Elettronico, inclusi almeno:

      * **max_validity_days**: Periodo massimo di validità in giorni.
      * **status_methods**: Metodi di verifica dello stato supportati (es. ``status_list``).
      * **allowed_states**: Stati consentiti dell'Attestato Elettronico (es. ``valid``, ``revoked``, ``suspended``).
  * - **authentication**
    - OBBLIGATORIO. Requisiti di autenticazione dell'Attestato Elettronico.

      * **user_auth_required**: OBBLIGATORIO. Flag che indica se l'autenticazione dell'Utente è richiesta durante l'emissione dell'Attestato Elettronico.
      * **min_loa**: OBBLIGATORIO. Livello minimo di Garanzia richiesto per l'autenticazione dell'Attestato Elettronico. DEVE includere il Livello di Garanzia dell'autenticazione dell'Utente e dell'Istanza del Wallet che richiede l'Attestato Elettronico.
      * **supported_eid_schemes**: OBBLIGATORIO se ``user_auth_required`` è ``true``. Schemi di autenticazione dell'identità digitale supportati.
  * - **purposes**
    - OBBLIGATORIO. Array di scopi o ambiti specifici per cui l'Attestato Elettronico può essere utilizzato, definendo contesti di utilizzo specifici e attributi richiesti per ciascuno scopo, come:

      * **id**: Identificativo univoco per lo scopo (es., "driving-authorization", "person-identification").
      * **description**: Descrizione *human-readable* dello scopo con un suffisso ``_l10n_id`` per la localizzazione del contenuto.
      * **category**: Categoria principale nella tassonomia dell'Attestato Elettronico (es., ``AUTHORIZATION``, ``IDENTITY``).
      * **subcategory**: Sottocategoria all'interno della tassonomia (es., ``DRIVING_LICENSE``, ``PERSON_IDENTIFICATION``).
      * **claims_required**: Array di identificativi di claims che sono richiesti quando si utilizza l'Attestato Elettronico per questo scopo.
      * **claims_recommended**: Array di identificativi di claims che sono raccomandati ma non obbligatori per questo scopo.
  * - **issuers**
    - OBBLIGATORIO. Array di informazioni rilevanti sui Fornitori di Attestato Elettronico autorizzati, inclusi dati amministrativi e tecnici come il nome dell'Organizzazione, un riferimento al documento di specifiche API e meccanismi di emissione supportati (ad esempio il supporto al *deferred flow*).
  * - **authentic_sources**
    - OBBLIGATORIO. Array di informazioni rilevanti sulle Fonti Autentiche autorizzate, inclusi dati amministrativi e tecnici relativi alla fornitura di dati agli Emittenti di Credenziali. A meno di indicazioni contrarie, l'array DEVE includere almeno le seguenti informazioni:

      * **id**: Identificatore univoco della Fonte Autentica.
      * **organization_name**: Nome leggibile dall'Utente dell'organizzazione della Fonte Autentica.
      * **organization_code**: Codice amministrativo dell'organizzazione della Fonte Autentica. 
      * **organization_country**: Paese dell'organizzazione della Fonte Autentica, rappresentato come un codice ISO 3166-1 alpha-2 di due lettere.
      * **contacts**: JSON Array di contatti della Fonte Autentica, possono essere inclusi nomi, indirizzi email, numeri di telefono, etc.
      * **homepage_uri**: [OPZIONALE] URI della homepage dell'organizzazione della Fonte Autentica.
      * **logo_uri**: [OPZIONALE] URI del logo dell'organizzazione della Fonte Autentica.
      * **source_type**: Tipo di Fonte Autentica, come ``public`` o ``private``.
      * **service_documentation**: [OPZIONALE] URI che punta alla documentazione del servizio della Fonte Autentica.
      * **data_provision**: [OPZIONALE] Oggetto JSON contenente informazioni sui metodi di fornitura dei dati supportati dalla Fonte Autentica, inclusi:

        * **immediate_flow**: OBBLIGATORIO. Booleano che indica se la Fonte Autentica supporta la fornitura immediata dei dati.
        * **deferred_flow**: OBBLIGATORIO. Booleano che indica se la Fonte Autentica supporta la fornitura differita dei dati.
        * **max_response_time_minutes**: CONDIZIONALE. Tempo massimo in minuti affinché la Fonte Autentica risponda a una richiesta di fornitura differita dei dati. OBBLIGATORIO se ``deferred_flow`` è impostato su ``true``.
        * **notification_methods**: CONDIZIONALE. Array dei metodi di notifica supportati dalla Fonte Autentica per la fornitura differita dei dati, come ``push``, ``poll``.
      * **user_information**:  [OPZIONALE] Una stringa contenente informazioni leggibili dall'uomo sull'Attributo Elettronico rilevanti per l'Utente. Questa stringa DEVE essere fornita dalla Fonte Autentica al Trust Anchor durante l'onboarding e DEVE utilizzare il formato Markdown come definito su :rfc:`7763`. La formattazione Markdown può essere testo semplice o una combinazione di testo e link. Ad esempio, se il database della Fonte Autentica contiene solo i dati richiesti per gli attributi dell'Attributo Elettronico registrati dopo una data specifica, questa informazione devono essere trasmesse al Trust Anchor e riportata nella stringa Markdown.
  * - **formats**
    - OBBLIGATORIO. Array dei formati tecnici supportati per le Credenziali Digitali, che include:

        * **format**: Tipo di formato (ad esempio, ``dc+sd-jwt``, ``mso_mdoc``)
        * **configuration_id**: Identificativo di configurazione del formato dell'Attestato Elettronico. Questo è formato concatenando il valore di ``credential_type`` al ``format`` (ad esempio, ``dc_sd_jwt_mDL`` o ``mso_mdoc_mDL``), ed è usato per fare riferimento in modo univoco alla configurazione per questo formato di Attestato Elettronico.
        * **vct**: CONDIZIONALE. È OBBLIGATORIO solo se il ``format`` è ``dc+sd-jwt``. DEVE essere impostato come una stringa URI nel formato ``https://{dominio Trust Anchor}/{version}/{credential_type}`` (ad esempio, ``https://trust-registry.it-wallet.example.it/v1/mDL``). Eventuali confronti con i caratteri di questa stringa DEVONO essere eseguiti in modo `case-insensitive`.
        * **docType**: CONDIZIONALE. È OBBLIGATORIO solo se il ``format`` è ``mso_mdoc``. Se l'Attestato Elettronico è:

          * definita da uno standard ISO, DEVE essere una stringa nel formato ``iso.org.{iso-number}.{part}.{version}.{credential_type}`` (ad esempio, ``iso.org.18013.5.1.mDL``).
          * definita a livello europeo, DEVE essere una stringa nel formato ``eu.europa.ec.{credential_type}.{version}`` (ad esempio, ``eu.europa.ec.personidentificationdata.1``).
          * definita da uno standard nazionale, DEVE essere una stringa nel formato ``{dominio inverso Trust Anchor}.{credential_type}.{version}`` (ad esempio, ``it.wallet.trust-registry.personidentificationdata.1``).
        * **schema_uri**: URI che punta al documento di specifica del formato.
        * **schema_uri#integrity**: Digest crittografico del documento di specifica del formato per la verifica dell'integrità. DEVE essere una stringa nel formato ``{metodo_digest}-{valore_digest}``, dove ``{metodo_digest}`` è l'algoritmo di digest utilizzato (ad esempio, ``sha-256``) e ``{valore_digest}`` è il valore di digest codificato in base64url.
  * - **display_properties**
    - OBBLIGATORIO. Proprietà di presentazione visiva degli Attestati Elettronici, ad es.:

      * **templates**: Modelli visivi per l'Attestato Elettronico, ad es. template `svg`.
      * **background_color**: Colore di sfondo in formato esadecimale.
      * **text_color**: Colore del testo in formato esadecimale.
      * **logo_uri**: URI al logo dell'Attestato Elettronico.
  * - **claims**
    - OBBLIGATORIO. Array di attributi contenuti nell'Attestato Elettronico. DEVE includere almeno le seguenti claims:

      * **name**: Il nome della claim nell'Attestato Elettronico.
      * **taxonomy_ref**: Stringa contenente il percorso al tipo di claim come definito in :ref:`it-wallet-dc-domains`.
      * **namespaces**: CONDIZIONALE. Namespace a cui appartiene la claim.
      * **display_name_l10n_id**: OPZIONALE. Nome della claim leggibile dall'uomo con un suffisso ``_l10n_id`` per la gestione della localizzazione del contenuto.


L'Oggetto ``wallet_attestation`` contiene almeno le seguenti informazioni:

.. list-table:: Campi di Primo Livello di Ogni Voce di Attestato Elettronico
   :class: longtable
   :header-rows: 1
   :widths: 30 70

   * - Nome Campo
     - Descrizione
   * - **credential_type**
     - OBBLIGATORIO. Identificatore unico dell'Attestazione del Wallet. DEVE essere impostato su ``WalletAttestation``.
   * - **name**
     - OBBLIGATORIO. Nome leggibile dall'Utente dell'Attestazione del Wallet. DEVE essere impostato su ``Wallet Attestation``.
   * - **description**
     - OBBLIGATORIO. Descrizione leggibile dall'Utente dell'Attestato Elettronico.
   * - **aal_values_supported**
     - OBBLIGATORIO. Array di Stringhe, ognuna delle quali rappresenta un Livello di Assurance (LoA) supportato dall'Attestazione del Wallet. DEVE includere almeno i livelli ``low``, ``medium`` e ``high``.
   * - **formats**
     - OBBLIGATORIO. Array dei formati supportati per l'Attestazione del Wallet, che include:

       * **format**: Tipo di formato (ad esempio, ``dc+sd-jwt``, ``mso_mdoc`` o ``oauth-client-attestation+jwt``)
       * **configuration_id**: Identificatore di configurazione dell'Attestazione del Wallet. Questo è formato concatenando la stringa ``wa`` al ``format`` (ad esempio, ``dc_sd_jwt_wa``, ``mso_mdoc_wa``, o ``jwt_wa``), ed è utilizzato per fare riferimento in modo univoco alla configurazione del formato dell'Attestazione del Wallet.
       * **vct**: CONDIZIONALE. È presente solo se il ``format`` è ``dc+sd-jwt``. DEVE essere impostato come una stringa URI nel formato ``https://{dominio Trust Anchor}/{credential_type}`` (ad esempio, ``https://trust-registry.it-wallet.example.it/WalletAttestation``). Eventuali confronti con i caratteri di questa stringa DEVONO essere eseguiti in modo `case-insensitive`.
       * **docType**: CONDIZIONALE. È presente solo se il ``format`` è ``mso_mdoc``. È una stringa nel formato ``{dominio inverso Trust Anchor}.{credential_type}`` (ad esempio, ``it.wallet.trust-registry.WalletAttestation``).
       * **schema_uri**: URI che punta al documento di specifica del formato.
       * **schema_uri#integrity**: Digest crittografico del documento di specifica del formato per la verifica dell'integrità. DEVE essere una stringa nel formato ``{metodo_digest}-{valore_digest}``, dove ``{metodo_digest}`` è l'algoritmo di digest utilizzato (ad esempio, ``sha-256``) e ``{valore_digest}`` è il valore di digest codificato in base64url.
   * - **claims**
     - OBBLIGATORIO. Array di claim contenuti nell'Attestato Elettronico. DEVE includere almeno i seguenti claim:

       * **Name**: Il nome del claim (ad esempio, ``sub``, ``aal``, ``wallet_link``, ``wallet_name``).
       * **Namespaces**: CONDIZIONALE. Array di namespace a cui appartiene il claim. DEVE essere impostato su ``{dominio inverso Trust Anchor}.{credential_type}`` (ad esempio, ``it.wallet.trust-registry.WalletAttestation``).

L'esempio corrispondente del Catalogo degli Attestati Elettronici decodificato in JSON sia per l'header che per il payload è il seguente:

.. literalinclude:: ../../examples/catalogue-example-header.json
  :language: JSON

.. literalinclude:: ../../examples/catalogue-example-payload.json
  :language: JSON

.. note::
  Per una gestione migliore e più efficiente della localizzazione delle informazioni contenute nel Catalogo degli Attestati Elettronici, un'Entità che lo consulta DOVREBBE:

    - Scaricare la versione base del Catalogo degli Attestati Elettronici (compatta, senza localizzazioni) utilizzando l'endpoint ``.well-known/credential-catalogue``.
    - Determinare la lingua preferita dell'Utente.
    - Scaricare solo i bundle di localizzazione necessari.
    - Unire dinamicamente il contenuto localizzato con la struttura del Catalogo degli Attestati Elettronici.

  Un esempio non normativo di output di un bundle di localizzazione è fornito di seguito:

    .. code-block:: json

      {
        "driving_license.name": "Patente di Guida",
        "driving_license.description": "Patente di guida ufficiale valida in Italia e nell'UE",
        "purpose.driving_authorization.name": "Abilitazione alla guida",
        "purpose.driving_authorization.description": "Verifica di Abilitazione alla guida",
        "claims.given_name.name": "Nome",
        "...": "..."
      }

  I bundle di localizzazione DEVONO essere disponibili all'URI specificato nel claim **localization_info.bundles_base_uri** del Catalogo degli Attestati Elettronici. Ogni *bundle locale* DEVE essere accessibile seguendo il pattern di denominazione **{locale_code}.json**, dove **{locale_code}** è sostituito con il codice di localizzazione corrispondente dall'array **available_locales**.

  Un esempio non normativo dell'URI di localizzazione italiana per il bundle mDL è **https://trust-registry.it-wallet.example.it/.well-known/l10n/mdl/it.json**.

  Le Entità DOVREBBERO verificare l'integrità dei bundle di localizzazione scaricati utilizzando il metodo di digest e i valori specificati nel claim **localization_info.integrity**. Questo garantisce che i dati di localizzazione non siano stati manomessi durante la trasmissione.


Tassonomia degli Attributi
^^^^^^^^^^^^^^^^^^^^^^^^^^

Il Catalogo degli Attestati Elettronici DEVE includere anche un URI di riferimento alla Tassonomia degli Attributi che fornisce, in un'unica risorsa, le informazioni semantiche di tutti gli attributi registrati e disponibili all'interno dell'ecosistema IT-Wallet. DEVE essere neutrale rispetto al formato dell'Attestato Elettronico e ha lo scopo di facilitare le integrazioni degli Attestati Elettronici nelle Soluzioni Tecniche IT-Wallet.

Un esempio non normativo della Tassonomia degli Attributi è fornito di seguito.

.. literalinclude:: ../../examples/catalogue-claims-taxonomy.json
  :language: JSON


Endpoint del Catalogo degli Attestati Elettronici
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
L'Endpoint del Catalogo degli Attestati Elettronici DEVE essere un URI HTTPS *well-known* [:rfc:`8615`] che fornisce accesso pubblico alle informazioni relative agli Attestati Elettronici disponibili in IT-Wallet.

Richiesta del Catalogo degli Attestati Elettronici
--------------------------------------------------

La Richiesta del Catalogo degli Attestati Elettronici DEVE essere una GET HTTP utilizzando il *media type* ``application/jose`` come nel seguente esempio non normativo.

.. code-block:: http

    GET /.well-known/credential-catalogue HTTP/1.1
    Host: www.trust-registry.it-wallet.example.it
    Content-Type: application/jose

.. note::
  Come miglioramento futuro, il Trust Anchor PUÒ implementare un endpoint dinamico che consenta di filtrare gli Attestati Elettronici per tipo, offrendo al contempo capacità di paginazione, per supportare una navigazione più efficiente e flessibile del Catalogo degli Attestati Elettronici.


Risposta del Catalogo degli Attestati Elettronici
-------------------------------------------------

La Risposta del Catalogo degli Attestati Elettronici DEVE essere un JWS che contiene i parametri elencati nella :ref:`tabella dei parametri del Catalogo degli Attestati Elettronici <table_catalogue_parameters>`.

Un esempio non normativo della risposta è fornito di seguito.

.. literalinclude:: ../../examples/catalogue-example-jws.txt
  :language: text

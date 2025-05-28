.. include:: ../common/common_definitions.rst

Flussi di Alto Livello per il Rilascio di Attestati Elettronici di Attributi
=====================================================

Flusso di alto livello per il PID
---------------------------------

La :numref:`fig_High-Level-Flow-ITWallet-PID-Issuance` mostra un'architettura generale ed evidenzia le principali operazioni coinvolte nel rilascio di un Attestato Elettronico di Dati di Identificazione Personale.

.. _fig_High-Level-Flow-ITWallet-PID-Issuance:

.. plantuml:: plantuml/pid-issuance-high-level-flow.puml
    :width: 99%
    :alt: La figura illustra l'architettura generale e il flusso di alto livello per il rilascio del PID.
    :caption: `Rilascio del PID - Architettura generale e flusso di alto livello. <https://www.plantuml.com/plantuml/svg/ZLHnR-gs5_q_dy8_LEb7fLQqQz-RD57qU86kaTW3XNJLaof59huD5ecTsJUqsRJllcie45ZwbgfIyFNnESVNn_vYaHiiyypxdrH9LWfWVV-svz_6lbR8fG8pyBo7O3IEvz4u74-ZxxDnzzoR3BzF7wDuChwFuZ3uzI6YccTNKXNSy9nbj12h0fWskDIr2QK5M2ZOzTLLhMguMcsgFrzvtl_P25veFPlFmY0QpslEi2ouC3UzHEUvLeE6cHToVSbVmUeSBZ_r4Z0eNsJ24LgW1KU-uBODDDF9gWMij61i6vywRGCZjZMO5i0LL2tTjO194IVSY1P8U4kMNAKGympRz1li2dNH0ldAimp-ax8dbKM99KeN3cyeH0XPnDDkXzjA9PqBTeRmXhxEjBax6uRXz2c-dtwBOdywcOOqws9xD5kVc6ELmTs8soM82OsxvnJv6HYhLTTrye9r7kdJeU_JnYuBo0vN2R2bpWJDd7lxIzLzbV_6kQNJO7Jxkn-udymPjeMH27UTRGU8ugikbU2cwXPIp8nUIx6HdWKZzZua8VQNn-Zl8BTEd1uHKoqlj0A5zaIkSx4NUpznKZjcCGNXgAULL2cRSOFLWUwTpMSzDX_-DZbXT04dkhyFzWD1YoHMjJtumLWADfAfH9wn7U1PiNiW07V7kj_QlB88UJn-mwuKpjOEVkW25K-vc4sMa0DpjrmmhTXMSgA7x46cIzQTt9pNkruBb7D_EB-DCBSaCInnwSWJDjUbsHxYyDiiF6d0xcqXccCIv0GyR93DmQnb0fPnTUY5Rs2p0vvPvdEgwBJSnUNoVZnY1b9fqLGdgkwP8aMFpcoRKOfTfs_bd_3BzUT1Ft5PPyGzw2y6L_tUOj3lRMhqTQ31ithY2iaBetnrBZh4vQY81Vc7HDUDHFM0qhviejTWw73TDYDJMZoYNoSV6_sfaJ-4FqgmQ8-T4i-FhDuqKcslPODRrc2MxWG5y4E5sqQ5VMWuWdrMD63kxTYpneyRvzn-oFkfaNUwSCco981evA8azYtdLxdhXYceuFxFaAVsRliq7hhreuHyRjGCh2sXrlOle4IPP_y0>`_

Il flusso di alto livello inizia con l'Utente che desidera ottenere un Attestato Elettronico di Dati di Identificazione Personale e avvia la propria Istanza del Wallet (Passo 0). Di seguito la descrizione dei passaggi rappresentati nell'immagine precedente:

    1. **Scoperta e Trust del Fornitore di Attestati Elettronici di Dati di Identificazione Personale**: l'Istanza del Wallet scopre il Fornitore di Attestati Elettronici di Dati di Identificazione Personale fidato utilizzando il Catalogo degli Attestati Elettronici e i Servizi di Federazione, stabilendo la fiducia verso il Fornitore di Attestati Elettronici di Dati di Identificazione Personale secondo il Trust Model e ottenendo i suoi metadati che rivelano i formati del PID, gli algoritmi supportati e qualsiasi altro parametro necessario per esigenze di interoperabilità.
    2. **Richiesta del PID**: utilizzando l'Authorization Code Flow definito in [`OpenID4VCI`_], l'Istanza del Wallet richiede il PID al Fornitore di Attestati Elettronici di Dati di Identificazione Personale.
    3. **Scoperta e Trust del Fornitore di Wallet**: il Fornitore di Attestati Elettronici di Dati di Identificazione Personale verifica l'autenticità e la validità dell'Istanza del Wallet, stabilendo la fiducia verso il Fornitore di Wallet e ottenendo i metadati del Wallet con i parametri necessari per le esigenze di interoperabilità, secondo il Trust Model.
    4. **Autenticazione dell'Utente**: il Fornitore di Attestati Elettronici di Dati di Identificazione Personale autentica l'Utente con CieID Livello di Garanzia Alto (L3), agendo come un Identity and Access Management Proxy verso il sistema nazionale di eID.
    5. **Recupero dei dati PID dal Registro Pubblico Nazionale**: il Fornitore di Attestati Elettronici di Dati di Identificazione Personale ottiene i dati PID richiesti dal Registro Pubblico Nazionale (ANPR) che agisce come Fonte Autentica.
    6. **Rilascio del PID**: il Fornitore di Attestati Elettronici di Dati di Identificazione Personale rilascia un PID vincolato al materiale crittografico detenuto dall'Istanza del Wallet richiedente.


Flusso di alto livello per gli Attestati Elettronici di Attributi (Qualificati)
-------------------------------------------------------------------------------

La :numref:`fig_High-Level-Flow-ITWallet-QEAA-Issuance` mostra un'architettura generale ed evidenzia le principali operazioni coinvolte nel rilascio di un Attestato Elettronico di Attributi (Qualificato), seguendo le ipotesi elencate di seguito:

  - l'Utente ha un PID valido memorizzato nella propria Istanza del Wallet;
  - l'Attestato Elettronico di Attributi (Qualificato) richiede un profilo di implementazione di alta sicurezza.

.. _fig_High-Level-Flow-ITWallet-QEAA-Issuance:
.. plantuml:: plantuml/eaa-issuance-high-level-flow.puml
    :width: 99%
    :alt: La figura illustra l'architettura generale e il flusso di alto livello per il rilascio di Attestati Elettronici di Attributi (Qualificati).
    :caption: `Rilascio di Attestati Elettronici di Attributi (Qualificati) - Architettura generale e flusso di alto livello. <https://www.plantuml.com/plantuml/svg/ZLHXR-964FtkNx6r8XMaH2INt4cj23eEd1vIL2WuZKuwoHgy4xF2xFfsnoHkrV_UMTmSX7DI8oJZcRVllNqxoqT7OAdSvC5FIgTvAL7qHrUzqLKoCfl2QDGq28BFat6KBE9e7atZBxEeqmrkXr-cTt5o6zt4oNpos-UOQu5RArs0XOt8bKQg2XJ6qieSDBIHwB0G5-Vd1rKBUkshxov_2OAVnHWVUBrOpEQJE5eSEAEo06alUwdPR8mUD7GUZAOpU4HdDdZslfUY9VMWKY1iWPP0i0JN1fgRTDq2LZgqherFaxM1CTiMRGlW6gkMxbh0b4nIiB854f_I5UWC4yYfJTxercIA5iX7o7FyNygUqeuKbQJyS0H3AUUOnv1rGd2LJiDJSKBuH2EJ6tjzCfpFf_V9pVJtE1bDRwTpxlgnFUo-Q2oeol5w36w5yfRVErqU-HbQPtJ79tagmZj-XFoytzaL4xO3EaMnChdaJZVuVgawZ-f7d5ywdOol_XnDH4_iViryBJmzSOLLXDTX7GGpVJAbbc2hpZS4c5cpLN9deVD7DneEHLtnckBlGF1dhxnDlJHhx6lkGFb8yB_3PyMNBBPW7CTRAPs96LYgzarFqUZUZpap_RFF8OcUg0EEOSEILbnGgLYOqjPX72r_lfzXzuY0W84tAD62FtknGBjLAJe1MegnoXH1BaOMfHU0t8aHSCLavNFaPpVHM5ZCb2DR7QdwgywA0M-sFcS-kh3lr5_uwyM7GJ_ryoAOUz1V3ixxlUMWtzlL-Eb1Ww_w7ZIn5r6VJNWQCfrdOoA2Lxak6hcEpfTtvrApHLjzrNwpiIqTlL3Ofg_RVTSeCSTl9JfoB7PacBdUSdpPI5SFUODZyQFXv8u7wws0hnebliyE4B9jVX7-AXxIUklWNkLztyWxNH8exLY0oAfboUmrvoVr78SjkE2_9mIPkwx_QVPnlRMN3usQ4-TAFCh-8sfPRl9_0G00>`_

Analogamente al flusso di alto livello del PID, il diagramma sopra illustra un flusso di alto livello per gli Attestati Elettronici di Attributi (Qualificati) che inizia dall'Utente che desidera ottenere un Attestato Elettronico di Attributi (Qualificato) (passo 0). Di seguito la descrizione delle operazioni più rilevanti coinvolte nel rilascio dell'Attestato Elettronico di Attributi (Qualificato):
    1. **Scoperta e Trust del Fornitore di Attestati Elettronici di Attributi (Qualificati)**: l'Istanza del Wallet ottiene l'elenco dei Fornitori di Attestati Elettronici di Attributi (Qualificati) fidati utilizzando il Catalogo degli Attestati Elettronici e le API di Federazione (ad esempio: utilizzando l'endpoint Subordinate Listing del Trust Anchor e dei suoi Intermediari), quindi ispeziona i metadati alla ricerca delle capacità di Credenziale Elettronica di ciascun Fornitore di Attestati Elettronici di Attributi (Qualificati).
    2. **Richiesta dell'Attestato Elettronico di Attributi (Qualificato)**: utilizzando l'Authorization Code Flow, definito in [`OpenID4VCI`_], l'Istanza del Wallet richiede un Attestato Elettronico di Attributi (Qualificato) al Fornitore di Attestati Elettronici di Attributi (Qualificati).
    3. **Scoperta e Trust del Fornitore di Wallet**: il Fornitore di Attestati Elettronici di Attributi (Qualificati) verifica l'autenticità e la validità dell'Istanza del Wallet. Durante questo passaggio, il Fornitore di Attestati Elettronici di Attributi (Qualificati) stabilisce la fiducia con il Fornitore di Wallet e recupera i metadati del Wallet contenenti i parametri necessari per l'interoperabilità, come definito dal Trust Model.
    4. **Autenticazione dell'Utente**: il Fornitore di Attestati Elettronici di Attributi (Qualificati), agendo come Istanza di Relying Party, autentica l'Utente valutando la presentazione del PID.
    5. **Ottenimento degli Attributi**: il Fornitore di Attestati Elettronici di Attributi (Qualificati) recupera gli Attributi dell'Utente dalla relativa Fonte Autentica.
    6. **Rilascio dell'Attestato Elettronico di Attributi (Qualificato)**: il Fornitore di Attestati Elettronici di Attributi (Qualificati) rilascia un Attestato Elettronico di Attributi (Qualificato) vincolato al materiale crittografico detenuto dall'Istanza del Wallet richiedente.

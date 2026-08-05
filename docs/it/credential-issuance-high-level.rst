.. include:: ../common/common_definitions.rst


Flussi ad Alto Livello per l'Emissione di Attestati Elettronici
===============================================================

Flusso ad Alto Livello per PID
------------------------------

La :numref:`fig_High-Level-Flow-ITWallet-PID-Issuance` mostra un'architettura generale ed evidenzia le principali operazioni coinvolte nell'emissione del PID.

.. _fig_High-Level-Flow-ITWallet-PID-Issuance:

.. plantuml:: plantuml/pid-issuance-high-level-flow.puml
    :width: 99%
    :alt: La figura illustra l'architettura generale e il flusso ad alto livello per l'emissione del PID.
    :caption: `Emissione del PID - Architettura generale e flusso ad alto livello. <https://www.plantuml.com/plantuml/svg/ZLHnR-gs5_q_dy8_LEb7fLQqQz-RD57qU86kaTW3XNJLaof59huD5ecTsJUqsRJllcie45ZwbgfIyFNnESVNn_vYaHiiyypxdrH9LWfWVV-svz_6lbR8fG8pyBo7O3IEvz4u74-ZxxDnzzoR3BzF7wDuChwFuZ3uzI6YccTNKXNSy9nbj12h0fWskDIr2QK5M2ZOzTLLhMguMcsgFrzvtl_P25veFPlFmY0QpslEi2ouC3UzHEUvLeE6cHToVSbVmUeSBZ_r4Z0eNsJ24LgW1KU-uBODDDF9gWMij61i6vywRGCZjZMO5i0LL2tTjO194IVSY1P8U4kMNAKGympRz1li2dNH0ldAimp-ax8dbKM99KeN3cyeH0XPnDDkXzjA9PqBTeRmXhxEjBax6uRXz2c-dtwBOdywcOOqws9xD5kVc6ELmTs8soM82OsxvnJv6HYhLTTrye9r7kdJeU_JnYuBo0vN2R2bpWJDd7lxIzLzbV_6kQNJO7Jxkn-udymPjeMH27UTRGU8ugikbU2cwXPIp8nUIx6HdWKZzZua8VQNn-Zl8BTEd1uHKoqlj0A5zaIkSx4NUpznKZjcCGNXgAULL2cRSOFLWUwTpMSzDX_-DZbXT04dkhyFzWD1YoHMjJtumLWADfAfH9wn7U1PiNiW07V7kj_QlB88UJn-mwuKpjOEVkW25K-vc4sMa0DpjrmmhTXMSgA7x46cIzQTt9pNkruBb7D_EB-DCBSaCInnwSWJDjUbsHxYyDiiF6d0xcqXccCIv0GyR93DmQnb0fPnTUY5Rs2p0vvPvdEgwBJSnUNoVZnY1b9fqLGdgkwP8aMFpcoRKOfTfs_bd_3BzUT1Ft5PPyGzw2y6L_tUOj3lRMhqTQ31ithY2iaBetnrBZh4vQY81Vc7HDUDHFM0qhviejTWw73TDYDJMZoYNoSV6_sfaJ-4FqgmQ8-T4i-FhDuqKcslPODRrc2MxWG5y4E5sqQ5VMWuWdrMD63kxTYpneyRvzn-oFkfaNUwSCco981evA8azYtdLxdhXYceuFxFaAVsRliq7hhreuHyRjGCh2sXrlOle4IPP_y0>`_

Il flusso ad alto livello inizia con l'Utente che desidera ottenere un PID e avvia la propria Istanza del Wallet (Passo 0). Di seguito la descrizione dei passaggi rappresentati nell'immagine precedente:

    1. **Individuazione e Trust del PID Provider**: l'Istanza del Wallet individua il PID Provider fidato utilizzando il Catalogo degli Attestati Elettronici e i Servizi di Federazione, stabilendo la trust verso il PID Provider secondo il Trust Model e ottenendo i suoi Metadata, che indicano i formati del PID, gli algoritmi supportati e qualsiasi altro parametro necessario per esigenze di interoperabilità (:ref:`WP_045–046 <wallet-credential-issuance-testcases>`).
    2. **Richiesta del PID**: utilizzando l'Authorization Code Flow definito in [`OpenID4VCI`_], l'Istanza del Wallet richiede il PID al PID Provider (:ref:`WP_051 <wallet-credential-issuance-testcases>`).
    3. **Individuazione e Trust del Fornitore di Wallet**: il PID Provider verifica l'autenticità e la validità dell'Istanza del Wallet, stabilendo la trust verso il Fornitore di Wallet e ottenendo i Metadata del Wallet con i parametri necessari per le esigenze di interoperabilità, secondo il Trust Model.
    4. **Autenticazione dell'Utente**: il PID Provider autentica l'Utente utilizzando CieID nazionale con LoA High (L3).
    5. **Recupero dei dati PID dal Registro Pubblico Nazionale**: il PID Provider ottiene i dati PID richiesti dal Registro Pubblico Nazionale (ANPR), che agisce come Fonte Autentica.
    6. **Emissione del PID**: il PID Provider rilascia un PID vincolato al materiale crittografico posseduto dall'Istanza del Wallet richiedente.

Flusso ad Alto Livello per IT-Wallet ID
---------------------------------------

La :numref:`fig_High-Level-Flow-ITWallet-ID-Issuance` mostra un'architettura generale ed evidenzia le principali operazioni coinvolte nell'emissione di un IT-Wallet ID.

.. _fig_High-Level-Flow-ITWallet-ID-Issuance:

.. plantuml:: plantuml/it-wallet-id-issuance-high-level-flow.puml
    :width: 99%
    :alt: La figura illustra l'architettura generale e il flusso ad alto livello per l'emissione dell'IT-Wallet ID.
    :caption: `Emissione dell'IT-Wallet ID - Architettura generale e flusso ad alto livello. <https://www.plantuml.com/plantuml/svg/ZLHXR-964FtkNp559vL8YKYQt5Mg23hEE0qITo3ZN7HI96kn9x32tgMxOnAtwd_lB0Hmg9CpNundtxxtPlPvFriIXeeyytwHAicA5A7hNtNygzZNYeHKQ7gUTpiS1F4q2i9W7FsO1EqJRzJ_CRwBub5m4yNXyC_RY6kUNKgr4aRaaF56AbS8sj12LnQKJj7Y2YxEpojL8zHoK_tztFD-XG4-ydwOJi9X54mhpgXOYTHSTXATvrhrQbOUsVMPU4AhSppxs4dGa7oKYI1iW4u5YPcmJQ2PJfODO8L5OvlurFCcC6PResa0N6BPq5q3c4pZH9Yq0HAVauLGSun5HatcZNP9UjK0-IIo37zAsP7AagI2f0k7rq_J4BD8pDijOKkLj4xX0-4p-JhJvlf3Fmp7z_7D-5iK--FHEEHL5zjNgzM5APKPNW-4NM0wulVs2KT-WiPgrNQJF8NM7JzQ_BpVs8KXsn4gGLZeBEML4s__KRMVvFznRkjuEBZwxW_TNt26xSf8mklMTW9CyKKNAXMcRACG4wFNCjr83wEp7Ti0WduVNjPO5VxnW7y7xNNYn5c5Q_bAArHaZxHRftlbb-DdwTSiPiKu7d0frHmcmb1ve7jXyw43q_xNqH6ZIplJ_NlePPZo9abbfI5_6CWK1d8kIMIm0pmek44627V6-zQcfINCu-2PsZ9rjdRmmnIuUCm5DbbWZk0--HIqWgtaIFVXLiuNq1vTde0sW3pHQJ5pPqIIz_SBMZY6P6C2dYGju6iO3U0x6lduKgwUNIMMhkr32ZQEXMLlUqwOwi9iez3_DWcF9hUxePZcDGa91Xuc0rCqQvcW1Q4EG_GD0pOzMF05L_Iys8Nkx2OOWC6vj6JA8rLtsR6YnuUzJJg7jzMryc_yu-9JhvkuBmQOkzUTzSwxdLclszdK-Eb0lGTrBnIn5tXGrPosJbjCwrYPaCIRd1Urd5Kc9gvcdby7qYPwZOOJuqOGcSBIAxrrydOJlzKAXlXNWPOirFV0XEyrSLdBkUMfDGurllcRuu2_gN5Lgr79Aze7nI_WBgezQtotyIxicxmVQtd7CnT0om94HiuAPjzoVf6xUR1V3fBB4ecvlTxUmuTvlHUaJ_M7Rcs1TIVm6LLQvDb_>`_

Il flusso ad alto livello inizia con l'Utente che desidera ottenere un IT-Wallet ID e avvia la propria Istanza del Wallet (Passo 0). Di seguito la descrizione dei passaggi rappresentati nell'immagine precedente:

    1. **Individuazione e Trust del Provider di IT-Wallet ID**: l'Istanza del Wallet individua l'EAA Provider di IT-Wallet ID fidato utilizzando il Catalogo degli Attestati Elettronici e i Servizi di Federazione, stabilendo la trust verso l'EAA Provider di IT-Wallet secondo il Trust Model e ottenendo i suoi Metadata, che indicano i formati dell'IT-Wallet ID, gli algoritmi supportati e qualsiasi altro parametro necessario per esigenze di interoperabilità (:ref:`WP_045-046 <wallet-credential-issuance-testcases>`).
    2. **Richiesta dell'IT-Wallet ID**: utilizzando l'Authorization Code Flow definito in [`OpenID4VCI`_], l'Istanza del Wallet richiede l'IT-Wallet ID all'EAA Provider (:ref:`WP_051 <wallet-credential-issuance-testcases>`).
    3. **Individuazione e Trust del Fornitore di Wallet**: l'EAA Provider di IT-Wallet ID verifica l'autenticità e la validità dell'Istanza del Wallet, stabilendo la trust verso il Fornitore di Wallet e ottenendo i Metadata del Wallet con i parametri necessari per le esigenze di interoperabilità, secondo il Trust Model.
    4. **Autenticazione dell'Utente**: Per l'IT-Wallet ID il metodo di autenticazione primario è basato su CieID LoA High (L3). Per scenari in cui il PIN CIE non è immediatamente disponibile, è disponibile un metodo di autenticazione alternativo che combina Autenticazione eID Substantial con Verifica MRTD. Per le specifiche tecniche complete, vedere :ref:`credential-issuance-l2plus:Autenticazione eID Substantial con Verifica MRTD per Emissione IT-Wallet ID`.
    5. **Recupero dei dati dell'IT-Wallet ID dal Registro Pubblico Nazionale**: l'EAA Provider di IT-Wallet ID ottiene i dati richiesti dell'IT-Wallet ID dal Registro Pubblico Nazionale (ANPR), che agisce come Fonte Autentica.
    6. **Emissione dell'IT-Wallet ID**: l'EAA Provider di IT-Wallet ID rilascia un IT-Wallet ID vincolato al materiale crittografico posseduto dall'Istanza del Wallet richiedente.

Flusso ad Alto Livello per (Q)EAA
---------------------------------

La :numref:`fig_High-Level-Flow-ITWallet-QEAA-Issuance` mostra un'architettura generale ed evidenzia le principali operazioni coinvolte nell'emissione di un (Q)EAA, seguendo le ipotesi elencate di seguito:

  - l'Utente ha un PID o un IT-Wallet ID valido memorizzato nella propria Istanza del Wallet;
  - il (Q)EAA richiede un profilo di implementazione ad alta sicurezza.

.. _fig_High-Level-Flow-ITWallet-QEAA-Issuance:
.. plantuml:: plantuml/eaa-issuance-high-level-flow.puml
    :width: 99%
    :alt: La figura illustra l'architettura generale e il flusso di alto livello per l'emissione di (Q)EAA.
    :caption: `Emissione di (Q)EAA - Architettura generale e flusso di alto livello. <https://www.plantuml.com/plantuml/svg/ZLHXR-964FtkNx6r8XMaH2INt4cj23eEd1vIL2WuZKuwoHgy4xF2xFfsnoHkrV_UMTmSX7DI8oJZcRVllNqxoqT7OAdSvC5FIgTvAL7qHrUzqLKoCfl2QDGq28BFat6KBE9e7atZBxEeqmrkXr-cTt5o6zt4oNpos-UOQu5RArs0XOt8bKQg2XJ6qieSDBIHwB0G5-Vd1rKBUkshxov_2OAVnHWVUBrOpEQJE5eSEAEo06alUwdPR8mUD7GUZAOpU4HdDdZslfUY9VMWKY1iWPP0i0JN1fgRTDq2LZgqherFaxM1CTiMRGlW6gkMxbh0b4nIiB854f_I5UWC4yYfJTxercIA5iX7o7FyNygUqeuKbQJyS0H3AUUOnv1rGd2LJiDJSKBuH2EJ6tjzCfpFf_V9pVJtE1bDRwTpxlgnFUo-Q2oeol5w36w5yfRVErqU-HbQPtJ79tagmZj-XFoytzaL4xO3EaMnChdaJZVuVgawZ-f7d5ywdOol_XnDH4_iViryBJmzSOLLXDTX7GGpVJAbbc2hpZS4c5cpLN9deVD7DneEHLtnckBlGF1dhxnDlJHhx6lkGFb8yB_3PyMNBBPW7CTRAPs96LYgzarFqUZUZpap_RFF8OcUg0EEOSEILbnGgLYOqjPX72r_lfzXzuY0W84tAD62FtknGBjLAJe1MegnoXH1BaOMfHU0t8aHSCLavNFaPpVHM5ZCb2DR7QdwgywA0M-sFcS-kh3lr5_uwyM7GJ_ryoAOUz1V3ixxlUMWtzlL-Eb1Ww_w7ZIn5r6VJNWQCfrdOoA2Lxak6hcEpfTtvrApHLjzrNwpiIqTlL3Ofg_RVTSeCSTl9JfoB7PacBdUSdpPI5SFUODZyQFXv8u7wws0hnebliyE4B9jVX7-AXxIUklWNkLztyWxNH8exLY0oAfboUmrvoVr78SjkE2_9mIPkwx_QVPnlRMN3usQ4-TAFCh-8sfPRl9_0G00>`_


.. .. figure:: ../../images/High-Level-Flow-ITWallet-QEAA-Issuance.svg
..     :figwidth: 90%
..     :align: center
..     :target: https://www.plantuml.com/plantuml/svg/ZPJ_Rzgy4yT_pr_XeKgZKccWq2-TsceCw8R46Zv0LqsQ55tYQx0QxCnsQFayUlxtvqo0jfHMYP12xiwlUv_Flg_6WhRvBFK-2HcdEKSsjJOpNtnVm-DX8kmqZtA3EbRIehI7iPhvMGhIhQaPorCH-PrMRUXCjpy7_WoCHKsciADccP9kJURuF_hTNZYUz4QzOF9xsAlkUuFsx-1s4WvwrvDmrF_-OqAspsnbdGJ3i1lStP3DCmz2Pg1Xnb8XqIuoP4hRgV8yzkoIYgF1Z3NgzPTc3VB1cO-QvnxHktXF23OUZlgJtjZxn8llJh_NxzwE1YMA5nPI0Nuii9PeoAOYDdupQhPuetdMmjFZwAnnregYazFxUZrg79sVra_ku_Cch-Dnmn__-kuJI4D8o90OXsQUR5JqEy5DEH4spu3hvdCd17bhznHHCvaM5isg4Pkshk4-BPyfMVJaZND9W4SqQeQrOpz6RSMzYC5YkGKSB4HWIaQdAdue5-dgDoKrgwHa937dgCl5Fk2YhDAoIC7363Gl5unFyHHaWY6ajcGhq3nObPKBVeGqnJ9WNqXZXSsjM9yXhytv2DC99DKAc8MCAmTip-AJxQXKwSkzzcWKt8NNmSqax0I3O4HUTujVULywndQHucKNp1JvWBwh-pG1XgYDabMtkGUiSakl2htlbgfPdoI1Z95DLSh9i__Yefk5iJXZaSeb1xqWnxVLtsfHyrYbosAUSMjBPP_zup5wFhEV82IBr_FCBAsRyLPz56-rE7b1lzlwrUapdot_3PsjSh1NND3BIf6_KFklvsrq_KM0eLPpmPV5Ll-ttsktsTfIMjKyTh8e_xFDl52r9MPr64dDQuhEA8xQkn0oOKFGTl7iT8YTbRahI2GgYfvDUDXxibKm5DhExPGC8gQzpdMnMLk8zI0Xp6k01GgyHeuQN9FO6FLSn6WOICww8d7ZcNKqSfS0KiCwG1QLvEkMrAvxNQOn4SRgnLPMDv0e8prKSd7QgBcL2oF-ZryQ9rSNiJkrZEXN5z5L_SAFhYxyfOtUBkZgZxm3QKaDA_fMEQWGqD48PE5TLcCdQwltL9-9rHpruezqvKvqRkoh3FFuVRb7ErECy6-EnXfAjYMOM1yfRkx45TTWXsBsLd1uIyVhemrkxKonEJrWaMJJ1tC3eS2kk4uxc7V1npl1GMH1I4CPhDKYoWbVGB-9zNxeZ0pkjsSXCPUhWKTfrm4VL7EoCsdVc1otTlyhIawZzJy0

..     (Q)EAA Issuance - General architecture and high level flow

Analogamente al flusso ad alto livello del PID e dell'IT-Wallet ID, il diagramma sopra illustra un flusso ad alto livello per (Q)EAA che inizia dall'Utente che desidera ottenere un (Q)EAA (passo 0). Di seguito la descrizione delle operazioni più rilevanti coinvolte nell'emissione del (Q)EAA:

    1. **Individuazione e Trust del (Q)EAA Provider**: l'Istanza del Wallet ottiene l'elenco dei (Q)EAA Provider fidati utilizzando il Catalogo degli Attestati Elettronici e le API di Federazione (ad esempio, utilizzando l'endpoint Subordinate Listing del Trust Anchor e dei suoi Intermediari), quindi ispeziona i Metadata alla ricerca della disponibilità di Attestati Elettronici di ciascun (Q)EAA Provider (:ref:`WP_045–046 <wallet-credential-issuance-testcases>`).
    2. **Richiesta del (Q)EAA**: utilizzando l'Authorization Code Flow, definito in [`OpenID4VCI`_], l'Istanza del Wallet richiede un (Q)EAA al (Q)EAA Provider (:ref:`WP_051 <wallet-credential-issuance-testcases>`).
    3. **Individuazione e Trust del Fornitore di Wallet**: il (Q)EAA Provider verifica l'autenticità e la validità dell'Istanza del Wallet. Durante questo passaggio, il (Q)EAA Provider stabilisce la trust con il Fornitore di Wallet e recupera i Metadata del Wallet contenenti i parametri necessari per l'interoperabilità, come definito dal Trust Model.
    4. **Autenticazione dell'Utente**: il (Q)EAA Provider, agendo come App di Verifica, autentica l'Utente verificando la presentazione del PID o dell'IT-Wallet ID.
    5. **Ottenimento degli Attributi**: il (Q)EAA Provider recupera gli Attributi dell'Utente dalla relativa Fonte Autentica.
    6. **Emissione del (Q)EAA**: il (Q)EAA Provider rilascia un (Q)EAA vincolato al materiale crittografico posseduto dall'Istanza del Wallet richiedente.


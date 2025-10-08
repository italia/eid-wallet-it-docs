.. include:: ../common/common_definitions.rst


Panoramica dell'Architettura
=============================

Il Sistema IT-Wallet è un ecosistema federato che consente la gestione sicura dell'Identità Digitale e lo scambio di Attestati Elettronici per cittadini e organizzazioni. 
L'ecosistema IT-Wallet è costruito su un'architettura multi-livello, dove gli organi di governance stabiliscono e mantengono l'infrastruttura di trust, gli Attori Primari implementano e gestiscono le Soluzioni Tecniche, e i sistemi esterni forniscono servizi aggiuntivi.

I seguenti diagrammi illustrano la panoramica dell'architettura IT-Wallet.

.. plantuml:: plantuml/architecture-overview-governance.puml
    :width: 99%
    :alt: L'immagine illustra la panoramica dell'architettura IT-Wallet - governance.
    :caption: `Panoramica dell'architettura IT-Wallet - Governance. <https://www.plantuml.com/plantuml/svg/fLNlRzis4Fskl-Bc5fWDvCTQ9uK3B4KTnsq314cGk2ZwoJYHPviOHMgyKr9jsFy-aSuYgManOzC7mpe-Fl6zUoUzOy4WLM7XOh7_6QqbMTxLB5Gifq5jZ92IAX3immT_Jy6XKvJzP9oobIRuTNPqE3jQpdnHUaTEtcOVByxdoxl5_7P-lVXoCn-Eif-1VpEkn805MED8wfB01zdux7BwvVhJOdavVxzOtbvy-BX8yCVgulfcUNxz-IhLpcbb7C7TpUt5OdxNEO1K9UemFbI-ABnx-vsLbNUoZm_4lg3zuqD5GSpAA1JQ0QrHC4UcNOZzcdU06RrK6FGEIFggDkZMj4GhEy0VKlF-3NXe78kHIanqgt5sLh7u0bXgIvnDjPvRAiZ90jV30NsLs7Cxs8EN-NhchG-dWnSdwOgroFnOVOXPIJWVD8N7wZfGFHXzIri6Ks2e-wolNhsPv7edrXU_v4UJoT5pOY6rwRE-KVbulDgDzGWduzSdprdNJydlSq-cuvF9-zsuZuzVZu-d3NScHYorqmRRQOCVJbjiKdi7KoK-S7RcAwSnrCFsS7imUCRwREDW17zcq5mt5DYx8IhNxBl2c0UqCAlpfawg2aPgc5QoyUdVS3gx6WswI7nQamqAq3tQ2eKOPjCp25Jw80peD1ZcgYahNvJMf9EW2B4a8Zw0kUCgH43lqNxLy7Pj8kKvQKgaZIgpCiI0UaE18gjuS8-7Iv1v5Nn9wE29amMZPveFOdy4rtpQw-rBBXiSdGuwCn8xrhKhxtemLIgGDbifSEPrtRUej-p36ftv8zriFNjy5H4dgJ6xpYYqoIgI9CglefySnI4pCNSSOM_J4V-77CxxeQbA2lU6VQYVr7HhULE3G5nwnoQt12iVmBlSOz36hM7kn4ZKOvpuR_gt8aqXYK_TKRx1kifN38LtHdo81Dkkcm2enDmdhWEu42ZGuPeOIWnYb2dH2LYp8bKhIucFKefwCNimie7M40YLfV_YrNQKXWfpRloOUTUeBj9uf8uKv2Iw5NKFcsQbCVad6QH1jHkmtP2d3TiSb1GYeat07g0kZ3CiqR7xfB2DSSl2uDrt0m6B3TNR8Qbx8z8-evs6FdkWtoiJAD7_m2nuSglpCHsCabdfvnBhvQSuAz6pKQUKF4JbEhNq1k9ybFsLPTaxShegxDy0>`_


Il livello di governance richiede a tutti i partecipanti nell'ecosistema di rispettare gli standard e i requisiti di sicurezza e tecnici.

.. plantuml:: plantuml/architecture-overview-primary.puml
    :width: 99%
    :alt: L'immagine illustra la panoramica dell'architettura IT-Wallet - primari.
    :caption: `Panoramica dell'architettura IT-Wallet - Attori Primari. <https://www.plantuml.com/plantuml/svg/dPP_Rzky4SV_zwku-HdG18YJFK-I1ocm5lKITpNMBORjh2WmGA2fiqoK8ZNov5Gj-jwdaoYPJjpCUFINVJgUoC_tVl2T9-6ep3LCbwDFGckaP55vmZmPExbHX99AXydCgLouQl0dPQGkKuI_tbvTt5ubjpOlh453RmSVfdUJPB6Sp2Vtoy-poSdfu1NuByeKmeaSj398LO5W7MtiuEFuy_t3ClauURzCvjE_VrWsxi6wl9ybT_UV_jNOxd2j3C9YDfyk9uje0rGM8dMN5zBckJLl3xnPMqCZyOZUvZYwlf3eIAsL58H7UAU2n4fuF2QmpVmHRYfDf73f4PxuLMw4oJ0HcevmVsJT_g_ZXJAU59Mac5PDzhRqP7FmL6dqWt6QJZJcQ6WfifCXVYLqHkZX6VnvbTrQRTsRuI-lcuTj73bO7pbD6Z_hKdJ1cZciXgTFmnPj7kr7_VNNtszMwL5HV_dBwkhcvkfvO4AvsO_wkrnTNgwFYtebRYv_U_qyQcQtJC58t8zzCxvyVVF-kDZNrxzTNe_hs0DIf75NQD0M6iI51YC8fGPZITRv0IlrnFGtMvgq_dyIQ9x1C7Y4aC5nU0hV1r0__G9HqWODAPbuMpg9lbuwxcomQ6t3OBHEaI2rHGZEODVmuD6zyf2gJ97Gm5K2mgGWY9nQbOJrLxyF1X2UlZ-S29-8GjMXSUJHRHN76y-c_B7vPB5SbneMmSwsJxY2tW-_5jPZ2clhGCZQufN9e3zCs5-pcNEO4gYyQ4Nqu4dmqLFr3LCed2KhhVPD96K8dItGYPNIYghc71uboy1DfJHA2guM3u-ADjttWl4CHCleM_EtXL2cYe2SKDgVSoQGoFoREEbz_PlmpJ2kS4wDWxpIrG5vu2uq9gOK_rwqEtTOir9aNGMUh6DGvPvcaLImTZO7SL3h4uUPyhKd-ZC6jsRgrWWDxGjq_hI6lIETEM5ABJg5G5f3Zbap6SRSSj8sotXJP06DBrqhMoD6ve8AZ51Ya2K2oKKUK-nwT4nmZZgvwxAjXTYXOVUmktf5jw3vyMFG_tm5OwqoqwRBLgNeF5W3j47m8aVGk4MzNrPj0quwVqxVKE5MbysfPrqeLehhCbBSa506tScZVxwmyV-dhKdW1PV4k2XsbWRLOsqLHQ7xNEsJdodlciswD98Q0HKfzEUmt605kJ0YmoxhEM7uhrt3NKYMMuSfnnBQdpsh03JfYEm8JGfefAkAlX9AZw70ra8YbrkVVgg9HzstUQU7QgKNkONBWiKwHVHJ6PFVRHYctfSl8kUbFf0-k7HV1pOorBXFBL5kk4zew0A5vjBwdhMdv5MCnU7MVk4_1_06HJQrdyQUbbUP4JmP6Bz9Gvqq_DkkzAnzlmWpt44YcliiNH6pdAEkUBSpuKZXIo1TqODylkwdsVnlT6gjq3NjQm_VbjzKFo45Wg0eLrh91adXr5OGzkCYwahxxRy96f9tDmlEeCbSMrCjDah2LcYLXWHdlOA_tA3yudSVbDLeLOrIP86EJMM-ABwGo2GueLpf2QPcxOGdLqhMlcyVhGBV3umB4abt_jhdtgmidpgatNjCG_lzZs7kSGBltlry_h8YTXVIu2DC33LzX1FISdECMqqVah--gm1gZkPGjvrgeufOAn-jYzM9hkqHvrO8pY-f2j4gJQM7t1hLZhrQYSFpDrOYF8U0ycQJC0JvYhKxtpmOXxrSiULE-J1VK-YMGovKKogCWM59GKBRZ3kjs0gbnKhZuPuRDQM5t60k_Exc4Sye1iAXbOk8CURpBdlu1k0btsYhdRIyAd37549d3YpZUlb3KpXEoYSyXmz5lGvzZwYhYpR6Hr4b3zqKZnhyQVGsxlln1DvtUpQSNN7GBUvyqRvF1p-QA_W_iDhFtFOo6b_TIyCwa31S98EQmFvuwI_0S_nlYPxytfsvyUSRGBo6VIMgBNgGVHh4pljjT-RGew6dployGvEMkVuV>`_

Il livello operativo primario implementa il ciclo di vita principale degli Attestati Elettronici attraverso interazioni coordinate tra Soluzioni Tecniche specializzate, in modo che tutte le operazioni degli attestati mantengano gli standard di sicurezza e privacy consentendo al contempo esperienze utente fluide.

.. plantuml:: plantuml/architecture-overview-external.puml
    :width: 99%
    :alt: L'immagine illustra la panoramica dell'architettura IT-Wallet - esterni.
    :caption: `Panoramica dell'architettura IT-Wallet - Attori esterni. <https://www.plantuml.com/plantuml/svg/ZPHHRzis4CVVzIbkQe7QW9EiTLAum5hKjTtLGz0OYOkYJyA9FCktIQH0dfAumxxxH5g9dNZ0x0S_tFtvv_5tT_he1PqqLGdpvSbtB4kIx6RZXQfixDIQXPGqZhBPlII_i55bemb-cvoVJSwpYQrgQyZ8X-JBV3hBRfQpwzdLyiTYrkidhy3_nQP6XnMKR4WsDO5rihR9vVZ7rRTbTZdxlCokvxz_MKPv5rrUBRBfrVUlCJQb5Hk2cyNrV3cxsIj0cXgr6vufMrNMVFYFpCeQES4xyhQYauipHKvunGg5Zb1h5CpHqp76jl17o5Xd2fq-GadtQesce0nBEK9-5thsly8pDbvO6k50goKxQRpO2hniIlB9MEjPIHKPMMBHI-bUo1aiqm6yp8k9BQrxdxvu5tyX5foxw5qOaQYpJfFheeMZJTf_Rbixhj1jdhg-VlrsbEkZN5_ycf-FHkU7na9g_TJrhSg7mzLnhkSu6hvvT-XQsDj0mIXwwZqQ3z-DFX_dVN7nPdWnRhqJOIbfjsImNJBONp8uWLb77iPAhFD9-tjr4Fna6wDRa3tg4WD87pKODI1sxouVxqfRMTh_Eu7sjo3dhUaffa7w5OLjE3hNP8Hb0mjdRrcJQq_iifeB5Yo17rHrfuAmAHgiWSby1hqMeH9d3QkTuGITxfzsjXvyo1U0ZQo3GCKhm9ExPTMcqMZezfNqxZuKSPmtqYfMre7D1Tbmy875V1fFeHA-HGd1tUldnaleucaAWvU2XN__PC1zxLZeVTfjQDgFWEBVumUkLskZ1scw1slQuPYYjFUNA6rD5VGMqw_J_hwEpSgX5zV45iVAwoOlMO4E9za8ELkJmvnBbiqfx572q6RDFqd3U37VFXkL8k_32nVZHsG3gD1WGVuvqzOXXgpZdzj8Jd97P212vN2KgtexzRxrKusBlKK9XBQzy6jqfBVrxfRYj8LtWFEHvlvNh4Nw36SeAPCrEvtLwBPbfEEkJjAm32bOR5DX2lzeD2l64go3cwOEp_RMRU2JrTnDp2KLRRupUJXtYNT0fkMcuWi12p8gNlTdvzZXwLWuAfeI9LZddVMkgdm3PUidjci2-9eKhrZjXYr2YdqgOpcriuf8iodyWCqjUU4Yzi63TVktgPPDoOTS3yTqzo5_u7g9c-nRtEKmflrTR3ksXx3xoJz9admaevkg_1S0>`_

I sistemi esterni forniscono servizi che collegano l'ecosistema IT-Wallet all'infrastruttura digitale nazionale, consentendo l'interoperabilità con i servizi governativi esistenti e le fonti di dati.

Questi tre livelli architetturali lavorano insieme per consentire operazioni sicure degli Attestati Elettronici. La natura federata di questa architettura richiede processi sistematici di onboarding per stabilire relazioni di trust tra i partecipanti e standardizzare la semantica delle credenziali attraverso i componenti centralizzati Claims Registry e Taxonomy, come dettagliato in :ref:`registry:Infrastruttura del Registro`.

L'architettura abilita i seguenti processi di interazione principali:

  1. **Onboarding delle Entità e Federazione**: Solo le entità qualificate possono partecipare alla federazione attraverso un onboarding sistematico che garantisce la conformità e stabilisce relazioni di trust crittografiche. Il sistema di onboarding include un **Claims Registry** e una **Taxonomy** che standardizzano le definizioni semantiche per tutte le credenziali, consentendo interoperabilità e governance. L'autorizzazione delle entità segue un approccio basato su policy che concede ambiti operativi specifici basati sulle caratteristiche organizzative e sulla conformità normativa. Vedere Sezione :ref:`onboarding-high-level:Sistema di Onboarding` e :ref:`registry:Infrastruttura del Registro`.

  2. **Discovery delle Credenziali e Gestione del Catalogo**: L'ecosistema supporta meccanismi duali di discovery delle credenziali pubbliche attraverso il :ref:`registry:Catalogo degli Attestati Elettronici` per credenziali di uso generale, e discovery di Attestati Elettronici privati tramite Credential Offer dirette per casi d'uso specifici. Il catalogo viene popolato automaticamente basandosi sulle policy dell'Organismo di Supervisione dalle definizioni registrate nel Claims Registry e nella Taxonomy.

  3. **Rilascio degli Attestati**: I Credential Issuer si coordinano con le Fonti Autentiche tramite API standardizzate per richiedere Attributi dell'Utente verificati, creando Attestati Elettronici basati su dati autorevoli. Il rilascio può procedere sia per attestati pubblicati nel catalogo che per offerte di attestati privati.

  4. **Archiviazione e Gestione degli Attestati**: Le Soluzioni IT-Wallet ricevono e gestiscono gli Attestati Elettronici sui dispositivi degli utenti, consentendo una gestione sicura del ciclo di vita degli attestati.

  5. **Presentazione e Verifica degli Attestati**: Gli Utenti presentano gli Attestati Elettronici alle Relying Party, che verificano i claim attraverso validazione crittografica e verifica dello stato. Le Relying Party operano all'interno di ambiti autorizzati che definiscono quali tipi di attestati e scopi possono richiedere, con validazione contro il :ref:`registry:Registro degli Attributi` per la verifica dello schema.

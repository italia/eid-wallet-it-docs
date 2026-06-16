.. include:: ../common/common_definitions.rst


Soluzione di Relying Party
==========================

Una Relying Party, come entità Organizzativa che si affida all'IT-Wallet, fornisce Soluzioni Tecniche (Soluzione di Relying Party) che potrebbero combinare software, hardware, servizi, impostazioni e configurazioni, incluse App di Verifica per l'autenticazione dell'Utente e la verifica degli Attestati Elettronici.

Per implementare e fornire Soluzioni Tecniche, una Relying Party può avvalersi dei servizi di un **Intermediario di Relying Party**. Ai sensi dell'articolo 5b, paragrafo 8, del `EU_2024_1183`_, gli intermediari che agiscono per conto delle Relying Party sono considerati Relying Party e **non devono conservare dati sul contenuto della transazione** tra l'Utente del Wallet e la Relying Party intermediata. Per le definizioni complete e il quadro giuridico europeo di riferimento, vedi **Intermediario di Relying Party** e **Intermediario IT-Wallet** in :ref:`defined-terms:Definizioni e Acronimi`.

.. note::
  Nel profilo implementativo descritto dalle presenti specifiche tecniche, un Intermediario di Relying Party è anche un'Entità Intermedia OpenID Federation (**Intermediario IT-Wallet**).

Una Relying Party fornisce almeno uno dei seguenti componenti:

- **Backend della Relying Party**: Gestisce la registrazione delle Istanze di Relying Party e la relativa gestione dei Certificati. Ottiene il Certificato X.509 secondo l':ref:`trust-infrastructure:L'Infrastruttura di Trust`. DOVREBBE inoltre fornire un Certificato X.509 alle proprie App di Verifica. Può anche implementare servizi web aggiuntivi e logica di business per i propri scopi e casi d'uso.
- **App di Verifica**: È un frontend fornito agli Utenti per accedere ai Servizi della Relying Party, e può essere fornito come:

  - **Client Web**.
  - **Applicazione Mobile**.

Il seguente diagramma illustra l'Architettura ad alto livello della Soluzione di Relying Party.

.. plantuml:: plantuml/rp-solution-architecture.puml
    :width: 99%
    :alt: La figura illustra l'Architettura ad alto livello della Soluzione di Relying Party.
    :caption: `Architettura di Alto Livello della Soluzione di Relying Party. <https://www.plantuml.com/plantuml/svg/jLHDRzim3BtxLt2vD0NMxTBZC3HD0zJOXXbjYc8dGvQPM9Wi2QBSBXZwtqV9YTtKBOOT5Y2HIVFZlKSn5nI43rshuGRrJfaj56pluDRgBYXhu5fj6_YA3wXXuMMZ0ihGUSpUAIDrLoDyMfv_N9wNIziwQz24prbsdL-jojlrwcRrVVsZMCrFi-m4hd2Z38AGmNe2OMgW7GLiAIlGapNpZj2_XzaT7pC-LnmHNV2eGWFv-knUQ8rXniKouC_Gi5pz2lFWEmgbCBAniSWwch18PYmMlpbHXyGyjug25udT4drG6oL5m1wJy_P1rMmKNtAGmebAQHKKEpRMGsWGkAFoE082bBPdag1bbxOpjV2xkUy5BLqKjApsRWRokjApK_XzJ6pkNLa9-HDDFScwxFq7RjUCNKTo1UI60kk0u9yJZTpaI1PQOSGMM-xo0VBMwVH8K7Ma31A1jbib4sToA6DM70P8GKZCC-9CFoDRLwfzvpUv3jW6hXE-ZrYLKYksEFaUArWcuy2JFMSLOwXXuwq9oAmK7tuZ92QqyVQ0w48JnoH7xbTgguBGiFHOnrVy-80-gT6B_pgSrlByiHJESVDloO25StgVbc0DR_udigViASjkqpLBz_qntRr1yYXDyemIxrVfX8OEVKJ2_7mZFUhKYHhbABjKFBBzBawRtANn7mMz75eUMGiPA2tk9FXOqabmnh4lbddSWhylCGGRY_HbniGfokAmv-o5HP5Jofoa7U5zEwtdE1dAfEjYF_xn_wOVDHjo6F-nS9EY4qp_LlI2UNMj_WC0>`_

.. .. figure:: ../../images/relying_party_solution_high_level_architecture.svg
..   :width: 100%
..   :alt: The image illustrates the Relying Party Solution and its relations and interactions within the ecosystem.
..   :target: https://www.plantuml.com/plantuml/svg/jLHDRziy3BxxL_3DfIdmfhdij5FJD42DhPZHfYXsCcIPIOJ9aY39pOAX_tsadDZDl6BOOGOIcHG_deSVlWvH-DWsEljF6QdR6c4NemiVvtClzbTR5NTjrGRqqfg89bv9syoT5ePzPY7MMbNpvOTPmQgd-y_pHeI8dbJbqZRE6lPn73-xoszNvUDwzR3wilvQhAQNMNO1jxXH1a78Q7q0OMe81mhGXAn07woPSkx_OV94nuJE5Lcm2lQ43FBrx5beZN52mJAWfqzQhhx7QVHjYAKmScSvo9f5MB2OWl4l3w7500-uLI5w4PKri4GVrKP94R73vBnzKJK9nQSSf72YKbf5HOgDzH1t29HHUHm00KhRCKdGiXlRcbhumzIZFYYpBPtmyL1MHpK1UUWkeE0BUBIwPIoJI_XnJcpgNLa9-GrDFVAwwVGdRdU4NJEv0d8JeZ0ImRybojpaG1OQOSGM6-uPv8tJwJK03O0o609ekrKoSGuE9NjnCq2AW85u0ZtfRs3hIdNC_2xN7blFTSHtZrKfjIA9d9-nWcKIZZnPCwi8GmqRdyQq1aM7tmY92IrF3uWsxhXDSk1-gxOg2WrBZpLVqUiB-bIDhlY_XzDOwZ-MmZbAVfy4M3YdJsuCgx_vbyXUizSiUqnZbkPzdsQlBpcN9cc64XzNwIBq6JgBXFdjHdhKALFOAHUo6qKjE-xYECbJQl-PqQzDovcra36anHqPdvLqR9onxVao3rlmvoM6Q3b85sPm7ACiJdjEMbWKUUWypzr6UDzpwpYEcZBAkkZQFtnlZgqcGVRjFolSAEW8qry6lIPURQD_0W00

..   Relying Party Solution High Level Architecture


.. toctree::
  :caption: Indice dei Contenuti della Soluzione di Relying Party
  :maxdepth: 3

  relying-party-instance.rst
  relying-party-entity-configuration.rst
  relying-party-metadata.rst



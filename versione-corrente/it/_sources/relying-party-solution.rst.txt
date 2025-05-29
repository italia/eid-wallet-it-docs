.. include:: ../common/common_definitions.rst


Soluzione di Relying Party
==========================

Una Relying Party, come entità Organizzativa che si affida all'IT-Wallet, fornisce Soluzioni Tecniche (Soluzione di Relying Party) che potrebbero combinare software, hardware, servizi, impostazioni e configurazioni, incluse Istanze di Relying Party per l'autenticazione dell'Utente e la verifica degli Attestati Elettronici.

Per implementare e fornire Soluzioni Tecniche, una Relying Party potrebbe avvalersi dei servizi forniti da un Intermediario. Un Intermediario di Relying Party è un'Entità Organizzativa che può agire per conto della Relying Party offrendo servizi ad essa, consentendo alla Relying Party di connettersi all'Istanza del Wallet e autenticare gli Utenti e verificare gli Attestati Elettronici dell'Utente.

Una Relying Party fornisce almeno uno dei seguenti componenti:

- **Backend della Relying Party**: Gestisce la registrazione delle Istanze di Relying Party e la relativa gestione dei Certificati. Ottiene il Certificato X.509 secondo l':ref:`trust:L'Infrastruttura di Trust`. DOVREBBE inoltre fornire un Certificato X.509 alle proprie Istanze di Relying Party. Può anche implementare servizi web aggiuntivi e logica di business per i propri scopi e casi d'uso.
- **Istanza di Relying Party**: È un frontend fornito agli Utenti per accedere ai Servizi della Relying Party, e può essere fornito come:

  - **Client Web**.
  - **Applicazione Mobile**.

Il seguente diagramma illustra l'Architettura di Alto Livello della Soluzione di Relying Party.

.. plantuml:: plantuml/rp-solution-architecture.puml
    :width: 99%
    :alt: La figura illustra l'Architettura di Alto Livello della Soluzione di Relying Party.
    :caption: `Architettura di Alto Livello della Soluzione di Relying Party. <https://www.plantuml.com/plantuml/svg/jLHDRzim3BtxLt2vD0NMxTBZC3HD0zJOXXbjYc8dGvQPM9Wi2QBSBXZwtqV9YTtKBOOT5Y2HIVFZlKSn5nI43rshuGRrJfaj56pluDRgBYXhu5fj6_YA3wXXuMMZ0ihGUSpUAIDrLoDyMfv_N9wNIziwQz24prbsdL-jojlrwcRrVVsZMCrFi-m4hd2Z38AGmNe2OMgW7GLiAIlGapNpZj2_XzaT7pC-LnmHNV2eGWFv-knUQ8rXniKouC_Gi5pz2lFWEmgbCBAniSWwch18PYmMlpbHXyGyjug25udT4drG6oL5m1wJy_P1rMmKNtAGmebAQHKKEpRMGsWGkAFoE082bBPdag1bbxOpjV2xkUy5BLqKjApsRWRokjApK_XzJ6pkNLa9-HDDFScwxFq7RjUCNKTo1UI60kk0u9yJZTpaI1PQOSGMM-xo0VBMwVH8K7Ma31A1jbib4sToA6DM70P8GKZCC-9CFoDRLwfzvpUv3jW6hXE-ZrYLKYksEFaUArWcuy2JFMSLOwXXuwq9oAmK7tuZ92QqyVQ0w48JnoH7xbTgguBGiFHOnrVy-80-gT6B_pgSrlByiHJESVDloO25StgVbc0DR_udigViASjkqpLBz_qntRr1yYXDyemIxrVfX8OEVKJ2_7mZFUhKYHhbABjKFBBzBawRtANn7mMz75eUMGiPA2tk9FXOqabmnh4lbddSWhylCGGRY_HbniGfokAmv-o5HP5Jofoa7U5zEwtdE1dAfEjYF_xn_wOVDHjo6F-nS9EY4qp_LlI2UNMj_WC0>`_

.. .. figure:: ../../images/relying_party_solution_high_level_architecture.svg
..   :width: 100%
..   :alt: The image illustrates the Relying Party Solution and its relations and interactions within the ecosystem.
..   :target: https://www.plantuml.com/plantuml/svg/jLHDRziy3BxxL_3DfIdmfhdij5FJD42DhPZHfYXsCcIPIOJ9aY39pOAX_tsadDZDl6BOOGOIcHG_deSVlWvH-DWsEljF6QdR6c4NemiVvtClzbTR5NTjrGRqqfg89bv9syoT5ePzPY7MMbNpvOTPmQgd-y_pHeI8dbJbqZRE6lPn73-xoszNvUDwzR3wilvQhAQNMNO1jxXH1a78Q7q0OMe81mhGXAn07woPSkx_OV94nuJE5Lcm2lQ43FBrx5beZN52mJAWfqzQhhx7QVHjYAKmScSvo9f5MB2OWl4l3w7500-uLI5w4PKri4GVrKP94R73vBnzKJK9nQSSf72YKbf5HOgDzH1t29HHUHm00KhRCKdGiXlRcbhumzIZFYYpBPtmyL1MHpK1UUWkeE0BUBIwPIoJI_XnJcpgNLa9-GrDFVAwwVGdRdU4NJEv0d8JeZ0ImRybojpaG1OQOSGM6-uPv8tJwJK03O0o609ekrKoSGuE9NjnCq2AW85u0ZtfRs3hIdNC_2xN7blFTSHtZrKfjIA9d9-nWcKIZZnPCwi8GmqRdyQq1aM7tmY92IrF3uWsxhXDSk1-gxOg2WrBZpLVqUiB-bIDhlY_XzDOwZ-MmZbAVfy4M3YdJsuCgx_vbyXUizSiUqnZbkPzdsQlBpcN9cc64XzNwIBq6JgBXFdjHdhKALFOAHUo6qKjE-xYECbJQl-PqQzDovcra36anHqPdvLqR9onxVao3rlmvoM6Q3b85sPm7ACiJdjEMbWKUUWypzr6UDzpwpYEcZBAkkZQFtnlZgqcGVRjFolSAEW8qry6lIPURQD_0W00

..   Relying Party Solution High Level Architecture


.. toctree::
  :caption: Indice dei Contenuti della Soluzione di Relying Party
  :maxdepth: 3

  relying-party-requirements.rst
  relying-party-instance.rst
  relying-party-entity-configuration.rst
  relying-party-metadata.rst

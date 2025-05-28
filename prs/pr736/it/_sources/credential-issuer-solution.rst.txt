.. include:: ../common/common_definitions.rst


Soluzione del Fornitore di Credenziale
======================================

Un Fornitore di Credenziale, come Entità Organizzativa partecipante all'ecosistema IT-Wallet, DEVE fornire Soluzioni Tecniche (Soluzione del Fornitore) che combinano software, hardware, servizi, impostazioni e configurazioni per emettere Attestati Elettronici alle Istanze del Wallet dell'Utente in modo sicuro e affidabile.

Il seguente diagramma illustra l'Architettura di Alto Livello della Soluzione del Fornitore.

.. plantuml:: plantuml/ci-solution-architecture.puml
    :width: 99%
    :alt: L'immagine illustra la Soluzione del Fornitore di Credenziale e le sue relazioni e interazioni all'interno dell'ecosistema.
    :caption: `Architettura di Alto Livello della Soluzione del Fornitore di Credenziale. <https://www.plantuml.com/plantuml/svg/fLPHRzis47xthxYfmve0pRmsIP42Qr7NIJ4FxUh5QVSeqEHP9Yg96aavyORzznqfAfOinH5QlrWYZzzzT_hkU6-DPTgMMGfJZG9pAraACsDArB1GQMcboc6Y-LfQvBRKEFf1vZmj1SAlqxFnz2oUggnGEPryCnezXKjSoHnXCR-UtLmj6iQsB9ZGfsEkiapbRtfsLYgt9-mMZShmv7pCKLkvafnP760jc6LBPeQOfef_7M1M6jHc24-L334Zj0tg0OPVSJkGtG0pAMBEj1XWYNTypV84OvRQ8Vb6yzMgOe3bBKjJV1HoB7DZfVLwyqAQbiQg38pTfcX64o6kKimmjpSiEOhmpgBEMHezWn-NoLIbIh-EdhpoFxVcaCFghLEkjrDQe0whYSPjTBmFMsYPCRrjepv__l9YAGQXFlbbUNPnSTO5DiXLBZhGB_doz7Gr3FgCNPo-UDM5jfeIrOQzc9o-kdW_3FRy_CNf-OHWTxLhrmYCMwKDi5n0dMimMsCnCwCvQgFo8wV0Pn1zfh-8_gjLMAjKo3o1Ivb8ovfTnJZdXb9iyNNaYukyBZncV7LdZogTn4u7BET8a7_v5PY5bIXuUsfWTdDIRJfConBpkYM9sajGVzjFpgnKP1YZ58JuHtW5d5r2PHOrbqK8HFemx3QauR1Zgk6sKrRQjJlFOwDAxQERr4kmy4ic2ekACCZx1i4rDJ1Xzw33klsrlNfjn9GxmYJm6_SA4__gd5qhPK6jm9l1IcaWHhlSmdiKg7qU3ZjlTEfkrB5TIotYWf4Dcbs8_w206xS5yshBCOBVIo6vkuA8pA8iK6-aKNeBxvIGMEdn0oQqpqAYv6EPQVILNhqLMcsaGBtJspoiH6sojH2C8yKT6SxH619xtJlfqN-odmypgXmJcNRDTMxTfIfzpnYz2mz7qbl49bWGlswPDM12qF3l2EXtVq_NC2kjSekvAuBtuN5d5BbyuB8HBUswweFwcBC8gQ9T8QJprioFNMjL9cjWG43LMKadzOfnX2CdDxnZMP4YBDRgreo_e2OLeHb_P3bBwFyQ_oxHsBvUShnBSMZQpGo7ooawze7lHS_lKU8g4HH7DtsjH7mgC9zTddsPpgBAcDcG4OzW-XY2LL1zQGWjhQdKS26qQLSZ0h5kCGvbL6qs9CcyI1P-sPDq6o_Sqs_4B7K4wmvJcJg-h7LubQhRRoMbCTsIu7rXRrqpgTvXxjxxqpU7CNoQNKxfRp7v-25gDa6VKNyhmAsqQsYrvN3pLAAPpowFGUdAZ5wgrQC_Zwyca-Dl3AOGkOYnLgxZDP_1h1Ph51RmfBRuZjPmc61p2klGR4etbIlaMvvYMxqVwcMeYYWBds1HCMkgOmS66XDfh6PLKp6MsPAIG7Qqir6yVGM4YQD1sat07RBXyZ78IxBQtby_Fy4YB0NRBiDG_q2tAD5et2w1L8q9cSgbLPgIUu2T6_U9tNzxtLPZwkCoQrcO4Qat33JTCOGw5uNNCEdqpwv9SyZeoDmfDrXtlFLrfz07JVWY7ENcWPvJEir1erqzuANTKJujBQEzTdEeiHpr0DCk-VuOkwNSVxX3wR7pBShxpUSBIwMuFtS_guMZdPpk9w2-UTePC0yVxol4Xd2zcUZvGWSWs-KIDEM7CgwtXLM9PiLQSb05wWwzBfTEH_DmcofGKKsM9E0iW7Ga_JqHlfCESfz1pmXyZLPBt3I9kU_NOjSFrXtUVBTct3P54t_k7K7RO0-UxOvRU_Dqc8_3AA125JMRQRDvrG6zfVoMMVe_>`_


.. .. figure:: ../../images/issuer-solution.svg
..    :width: 100%
..    :alt: The image illustrates the Issuer Solution and its relations and interactions within the ecosystem.
..    :target: https://www.plantuml.com/plantuml/svg/fLTjRzis4FxkNt5LXpK1chfvIP4CA537IJSFQUF5IVVHeAMpJ4GIDP9ouWtxxpk-A9PCnnFQVAWbykwvvquFZzTFIZEfgpphlO7X2Gn5Nee22mq9PwbaESo5X95I5KgOYApIN1GmaF62Qunr9R7tYXTnLYK82wrBzKk_BzdZkvJhHJMh5CfO59hmtiKYxvSPAqoi0wMJZC_wmvE3iLcw_tBTpvdIA6bfwZcGJsbu4R5BdFC2OJA-7TrTJNgl4lS-6jvylR-zxX1OLoLBvF6Q0AVTWpbP7AXIKYhAnrzduy7xv9wBmb49DYq2UqGbSZmuxSSeDP_pc6divf0mpMPCTRJEHFpGpTBahpfo5cb7Iy9Seknc-u2hxaoxMV9a6ZEPT3F6ftZ1YXIdBDCTFmMg1otARiQFBCkm2t2V5qfpRO_Divo7bT8Y1wLN6QhU84ckCionq7SitOlmIQCiM1QzXPzcwL1aGdwCNf_RFxDcqFtgepc4rax81ALVJIMkelrDM59vpkIgZNfu-E5ibdH2VVr-Td9sTX82AwIZb0JG7-BPyV6y6_G9Epi-EYVeDn20ooMFKRMnyNn6pBjXiwEpmyFt8MqjAwNRi6U3u_EppzrWJq-FZay71BlkJdg1m68jf09M951_Hr0hfJ5NlJ5A9Oez8_Yt4DtJJqI_RXKM8ajuaS8bJxacfw74XAXobjdSNPFw61bdHL4d5dDwzQJtd1IdHcUiY94W_xGhCF8haO_sHi7exi1j6apDKlMn9RSwYZzfxJW5CnfcsHHvGeXV_IlWw1ASMTHSJdmYtAQXLxuCkmDJrsW7PPLU6FzugaGbRNQ3UWacTab5Vb4G1aLV8fYk2ihlxWnOzzzsLAkDATMEC0dyphp2mBwQOBT2Q11pi6RsVYH6wzh2PqnGsZhi3jwuBSAifth1PJ8j6TcWMgVuDoPmPxPWxBOC8_YzIdXCOW4YCwbASsgKa2ku40b7fyThJ6cVEHJZk9jSeszjrLifnP9JdckzZVrAr2PR2w4-oi1Y-bUHsEicJO_saxtRpSW59ZBjCnSC9pDHsNxKk_0FUznQJ9Mt87xXCMl0-AJXdnxGNojMpdW1SJsVA6Em7fdgE7Df9mzpIZxxnxLHP0g6iqOvQDSSJwZTZ8Ml9Uqc2JTqcWNK2ocgT04C2CZvSlAKSnOZx1azuXFBomnXiX2FglyD9SaCLVyBArXAlxVuLuLARsis--jlu6-CvYVmTsIqRnFtvV65ks3nGpFJe3hnSvIfAnJb6TI_NQYR4elHvSctuIXonapxYba4jIq3q0ASLC3tnARK_MtLJiiDDfHLax0_Xcwl8MbcHJPnBeQZsJWoJxyHiSpmgpkKCpLqMSjvded7x-GaCLlHUR5zOMLwaNk7iNdVNhmnzE5cT3cadydWotNKxA6sdlPIWKUk5z3gwlxYSf8QZoxtGKXdHYzkTU-F_Ql1OF_xSYcJ8fbYBMj3Qpo2KQtao2_WGMtn0urbDx_ciDXW6SWsutECLt66RULUrylW3bZkFy344MjAOmq64bEkj6Ik8odDT4Kr83lQMOguVN_uSQN1sOpj0LTtSL6E5Hcjdg-kds7YbxnjID2t1g0Rc5WqRYRFgSQ4N1HS2qcbtK7E_4U5oFsxqQabPZOjjU2bwf5q_J0KZZ3Kr2YxXadGMaEJve0IQDp8rbi7qROr9jyYbVyWCVBb2-scCeg3HgTw8KgxczpCDAEzZSRWiGnrWZ4ucmS-J38yo3xLq3dWz7_-BSwRhUSRotZoxFSyw7dNeAYR5V2tqaO9rClksmvYGxdMBDdoYNP01kV5YCfETB5SbLgaafKB7eCeKORq0Yv1GxDmIvTeuiPIKd3kGG9D_qY65zn0RZBOCZ_VefOSbqrY5Jcqs6q72oS_swnPh9kYcTvldLytmKBVdlSEfhMDSToFrtuG4FuWDTjfit_vb4md-bMAgYG5Ao07oc1ZSY4BG-2o9Z1pozlxmr0KDYuXRtThoBsRGt306YxmeazGrjrnTiYiWsTmNfe-dyYYohF_0000
      
..    Issuer Solution High Level Architecture

Requisiti del Fornitore di Credenziale
--------------------------------------

La Soluzione del Fornitore di Credenziale Elettronica DEVE:

   1. Registrarsi presso l'Autorità di Federazione per ottenere la corretta autorizzazione per l'emissione di specifici tipi di credenziali.
   2. Implementare meccanismi sicuri di creazione ed emissione che garantiscano integrità e riservatezza.
   3. Comunicare con le Fonti Autentiche attraverso Servizi API sicuri e affidabili per ottenere dati verificati dell'Utente.
   4. Autenticarsi presso le Istanze del Wallet durante l'emissione per dimostrare la propria legittimità.
   5. Supportare il flusso di emissione immediata e PUÒ supportare l'emissione differita per vari scenari operativi.
   6. Implementare una gestione appropriata degli errori e notifiche all'Utente per tutti i processi.
   7. Mantenere tracce di audit complete rispettando le normative sulla privacy.
   8. Emettere Attestati Elettronici che supportano la Divulgazione Selettiva.
   9. Rinnovare periodicamente la propria fiducia con la Federazione.
   10. Registrare il Componente Relying Party all'interno dell'ecosistema di Federazione dell'Identità Digitale CIEid (per l'emissione di PID) e, se richiesto, all'interno dell'ecosistema IT-Wallet (per l'emissione di (Q)EAA).
   11. Per l'emissione di PID, autenticare gli Utenti con LoA High utilizzando i Gestori di Identità Digitale nazionali.
   12. Per l'emissione di (Q)EAA che richiedono autenticazione, verificare un PID valido dall'Istanza del Wallet dell'Utente tramite `OpenID4VP`_.
   13. Implementare procedure adeguate per l'intero ciclo di vita dell'Attestato Elettronico come dettagliato nella Sezione :ref:`credential-revocation:Ciclo di vita delle Credenziali`.

   Per il Componente Frontend (se implementato):

   14. Autenticare gli Utenti con un Livello di Garanzia (LoA) almeno pari a quello utilizzato per ottenere l'Attestato Elettronico che viene emesso o gestito.
   15. Fornire misure di sicurezza appropriate per proteggere i dati dell'Utente e le informazioni dell'Attestato Elettronico.

Dettagli dei Componenti
-----------------------

Componente Frontend
^^^^^^^^^^^^^^^^^^^

Il Componente Frontend, se fornito dal Fornitore di Credenziale, DEVE fornire un'interfaccia Utente basata sul web per la gestione degli Attestati Elettronici, offrendo funzionalità per:

   - Visualizzare e verificare gli Attestati Elettronici emessi e il loro stato.
   - Gestire il ciclo di vita degli Attestati Elettronici (ad es., revoca).
   - Avviare l'emissione attraverso Offerte di Credenziali.
   - Fornire supporto e documentazione all'Utente.

I Fornitori di Credenziale POSSONO fornire servizi aggiuntivi all'Utente attraverso il Componente Frontend. Questi servizi aggiuntivi NON DEVONO essere in conflitto con i requisiti normativi o tecnici definiti in questa specifica tecnica o nelle normative nazionali/europee sulla sicurezza e la privacy.

Componente Fornitore di Credenziale
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Seguendo la specifica `OpenID4VCI`_ e il profilo di implementazione nella Sezione :ref:`credential-issuance:Emissione di Credenziale Digitale`, questo componente DEVE:

   - Emettere Attestati Elettronici alle Istanze del Wallet.
   - Elaborare le richieste di Attestati Elettronici.
   - Ottenere i dati dell'Utente dalle Fonti Autentiche.
   - Generare Attestati Elettronici correttamente formattati e firmati nei formati supportati (SD-JWT-VC, mDoc-CBOR). Vedere la Sezione :ref:`credential-data-model:Modello di Dati delle Credenziali Elettroniche` per maggiori dettagli.
   - Implementare i protocolli e i flussi di emissione degli Attestati Elettronici.

Server di Autorizzazione
^^^^^^^^^^^^^^^^^^^^^^^^

Questo componente basato su OAuth2 DEVE:

   - Gestire i flussi di autenticazione e autorizzazione.
   - Gestire token di accesso/refresh e codici di autorizzazione.
   - Validare l'identità dell'Utente confermata dal Componente Relying Party.

Componente Relying Party
^^^^^^^^^^^^^^^^^^^^^^^^

Quando è richiesta l'autenticazione dell'Utente, questo componente DEVE autenticare gli Utenti:

   - Per l'emissione di PID, tramite Gestori di Identità Digitale nazionali utilizzando OIDC o SAML2.
   - Per l'emissione di (Q)EAA, richiedendo, ottenendo e validando i PID dalle Istanze del Wallet dell'Utente utilizzando `OpenID4VP`_ in conformità con la Sezione :ref:`credential-presentation:Presentazione della Credenziale Digitale`.

Interfaccia API
^^^^^^^^^^^^^^^

Questo componente DEVE stabilire connessioni sicure con le Fonti Autentiche per:

   - Recuperare dati verificati dell'Utente.
   - Autenticare e autorizzare correttamente le connessioni.
   - Formattare i dati secondo gli schemi degli Attestati Elettronici.
   - Fornire prove crittografiche dell'autenticazione dell'Utente quando richiesto.

.. note::
   Per le Fonti Autentiche pubbliche, un Fornitore di Credenziale DEVE utilizzare PDND secondo le regole nelle Sezioni :ref:`e-service-pdnd:e-Service PDND`, :ref:`credential-revocation:Aggiornamento dello Stato da parte delle Fonti Autentiche`, e :ref:`authentic-source-endpoint:e-Service Catalogo delle Fonti Autentiche PDND`.

Gestione del Ciclo di Vita delle Credenziali
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Questo componente DEVE gestire:

   - Gestione dello stato (mantenimento e aggiornamento della validità).
   - Processi di revoca (implementazione di meccanismi per revocare o sospendere gli Attestati Elettronici), secondo la Sezione :ref:`credential-revocation:Ciclo di vita delle Credenziali`.
   - Flussi di rinnovo (gestione dei processi di rinnovo degli Attestati Elettronici), secondo i meccanismi definiti nella Sezione :ref:`credential-issuance:Emissione di Credenziale Digitale`.

Componente Trust & Security
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Questo componente DEVE garantire la sicurezza attraverso:

   - Gestione delle chiavi e dei certificati.
   - Registrazione degli audit.
   - Monitoraggio della sicurezza e risposta agli incidenti.
   - Conformità ai requisiti di sicurezza della Federazione IT-Wallet.

Modelli di Interazione
----------------------

La Soluzione del Fornitore di Credenziale supporta questi modelli di interazione:

   1. **Utente verso Frontend**: Interazioni basate sul web per la gestione degli Attestati Elettronici.
   2. **Frontend verso Fornitore di Credenziale**: Converte le richieste dell'utente in messaggi del protocollo OpenID4VCI.
   3. **Istanza del Wallet verso Fornitore di Credenziale**: Interazioni dirette basate sul protocollo seguendo il flusso di emissione.
   4. **Relying Party verso Gestori di Identità**: Interazioni di autenticazione con i sistemi nazionali eID o verifica PID.
   5. **Interfaccia API verso Fonti Autentiche**: Chiamate API sicure per recuperare dati verificati dell'Utente.

Tutte le interazioni devono seguire le considerazioni di sicurezza nella Sezione :ref:`credential-issuance:Emissione di Credenziale Digitale`, inclusa la corretta gestione di token, prove e materiali crittografici.

.. include:: credential-issuer-entity-configuration.rst
.. include:: credential-issuer-metadata.rst

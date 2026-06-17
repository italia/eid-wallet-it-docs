Matrice di Test per la Valutazione della Fiducia
------------------------------------------------

Questa sezione fornisce l'insieme comune di casi di test per le Soluzioni Wallet, le Relying Party e i Credential Issuer.


.. list-table::
  :class: longtable
  :widths: 15 15 35 35
  :header-rows: 1

  * - Test Case ID
    - Purpose
    - Description
    - Expected Result
  * - ALL-001
    - Security
    - Ottenimento dei materiali crittografici pubblici dei Trust Anchors
    - Le entità ottengono la lista dei Trust Anchors o Certificate Authorities e i loro materiali di chiavi crittografiche pubbliche, assicurandosi periodicamente che questi non siano scaduti, revocati o aggiornati. L'infrastruttura di fiducia fornisce queste informazioni attraverso web endpoint e altri meccanismi out of band, per facilitare il confronto delle informazioni fornite a tutte le entità.
  * - ALL-002
    - Security
    - Auto-valutazione della conformità
    - Le entità valutano periodicamente la loro conformità e presenza all'interno della federazione, controllando che la trust chain su se stesse sia ancora valida, non revocata e conforme alla specifica tecnica. Le entità applicano le policy, controllando che la loro configurazione attuale sia valida con le policy attive su di loro all'interno della federazione. Le trust chain, valutate e memorizzate in formati multipli per facilitare l'interoperabilità nella discovery della fiducia con altre entità, sono memorizzate dalle entità e utilizzate all'occorrenza durante i flussi di scambio dati. Le trust chain sulle entità vengono recuperate o scoperte utilizzando le asserzioni emesse dalle entità.
  * - ALL-003
    - Discovery
    - Pubblicazione delle informazioni su se stessi
    - Le entità firmano e pubblicano tutte le informazioni su di loro, contenenti tutti i metadata del protocollo, materiale crittografico, trust marks, utilizzando il well-known endpoint definito in questa specifica, rendendo queste informazioni pubblicamente scopribili da altre entità.
  * - ALL-004
    - Security
    - Pubblicazione del registro storico delle chiavi
    - Le entità firmano e pubblicano tutte le informazioni sui materiali crittografici non utilizzati o revocati utilizzando well-known endpoint definiti in questa specifica, rendendo queste informazioni pubblicamente scopribili da altre entità.
  * - ALL-005
    - Security
    - Valutazione della conformità con le entità prima dello scambio di dati sull'Utente
    - Le entità valutano la fiducia e la conformità con altre entità prima che qualsiasi informazione relativa a una persona fisica o giuridica possa essere scambiata. Configurazioni false non permettono scambi di dati.
  * - ALL-006
    - Security
    - Valutazione della prova di possesso durante l'uso di un'asserzione firmata in accordo con il metodo di conferma della proprietà di utilizzo configurato.
    - Le entità valutano il metodo di conferma e applicano il suo protocollo per considerare valida la dichiarazione firmata.
  * - ALL-007
    - Security
    - Algoritmi crittografici supportati
    - Le entità valutano la crittografia utilizzata in conformità con gli algoritmi consentiti.
  * - ALL-008
    - Security
    - Attacchi replay
    - Le dichiarazioni firmate utilizzando identificatori univoci sono memorizzate fino al loro tempo di scadenza e controllate contro qualsiasi replay di esse.

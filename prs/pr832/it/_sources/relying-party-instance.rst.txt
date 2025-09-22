.. include:: ../common/common_definitions.rst

.. "included" file, so we start with '-' title level

App di Verifica 
---------------

L'App di Verifica è un'applicazione mobile o embedded progettata per richiedere, ricevere ed elaborare Attestati Elettronici dalle Istanze del Wallet in modo affidabile. Ogni App di Verifica garantisce l'integrità, la riservatezza e l'autenticità degli scambi di Attestati Elettronici, consentendo interazioni sicure tra Utenti e Relying Party (:ref:`test-plans-remote-presentation:Matrice di Test per la Presentazione di Credenziali Remota`, :ref:`test-plans-proximity-presentation:Matrice di Test per la Presentazione di Credenziali in Prossimità`).

Esistono due tipi principali di App di Verifica, ciascuna destinata a diversi ambienti operativi:

- **App di Verifica Embedded**: una soluzione hardware/software che opera su un dispositivo specializzato (ad es., varchi di accesso). Ogni App di Verifica corrisponde a un'installazione specifica dell'applicazione su un dispositivo embedded. Poiché la trust con l'App di Verifica Embedded è stabilita attraverso la trust instaurata con il Mobile Relying Party Provider, l'App di Verifica Embedded può essere considerata un Confidential Client di OAuth.
- **App di Verifica Mobile**: un'applicazione nativa che opera su un dispositivo mobile (ad es., smartphone o tablet). Ogni istanza corrisponde a un'installazione specifica dell'applicazione su un dispositivo. Poiché la trust con la App di Verifica Mobile è stabilita attraverso la trust instaurata con il Mobile Relying Party Provider, l'App di Verifica Mobile può essere considerata un Confidential Client di OAuth.
- **App di Verifica Web**: un'applicazione remota gestita dalla Relying Party. Un'App di Verifica Web opera come Confidential Client di OAuth, il che significa che può memorizzare in modo sicuro configurazioni riservate (come le sue chiavi crittografiche private) su un server remoto. In questo contesto, la Relying Party non è fornita da terzi e la richiesta di presentazione e la successiva validazione sono gestite automaticamente dal software.

.. note::
  Le App di Verifica Embedded e Mobile che agiscono come client pubblici non sono considerate all'interno di queste specifiche.

.. note::
  A differenza della App di Verifica Web, un'App di Verifica Mobile o Embedded richiedono una gestione appropriata del ciclo di vita e procedure ad hoc di registrazione gestite attraverso il Backend della Relying Party.

Ulteriori dettagli tecnici e operativi sono discussi nelle sezioni seguenti.


App di Verifica Mobile
----------------------

Il ciclo di vita di un'App di Verifica include quattro stati principali: **Installed**, **Unverified**, **Verified** e **Uninstalled**, supportando funzionalità come registrazione, riemissione del Certificato di Accesso e revoca.

Ciclo di Vita App di Verifica Mobile 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In questa sezione vengono presentati le macchine a stati finiti per spiegare gli stati dell'App di Verifica Mobile, nonché le loro transizioni e relazioni.

.. _fig_RelyingParty_Instance_Mobile_Lifecycle:
.. plantuml:: plantuml/rp-mobile-instance-lifecycle.puml
    :width: 99%
    :alt: La figura illustra il Ciclo di vita dell'App di Verifica Mobile.
    :caption: `Ciclo di vita della App di Verifica Mobile. <https://www.plantuml.com/plantuml/svg/XP7VQ_em5CNVyrTSzENx5SIkw1X5Ycx6KTYaYpyOZ3reSwk1c4gRRdH__M8DZJZ4FlMU--avXzjHeTUvBlSINaIAIPL8X2m5lKDupJR2J0nb9TGMOiDL42dpWKgGx0H7mFt1Q1oB91S7BJ95Y5bhF65I8eVsT3eUU9xLMolCHIgGjs1T6Eirhw3j-m-Flc-9fVgo2BHJytXUin3ET7BV7_G7X7nqFg7Bis_L3Lrc02oE89hD5wJH6ihQE6uvkoHpiTrfWzRrJX2ZpwGUR_fOIcAg_tPYT6K1PpzCCfdbmKQM6CRHfFVlxJyTZo5cTDYhL-55ihjG04-KBO2-nyI9DnkUe-N15Qcz68tcytFa8l1wsqvJr_7NxZ2XnuEwWWOqaFcP9g0GFnZS-U6mTtmBoGWLB_Vo5m00>`_


.. .. figure:: ../../images/RelyingParty_Instance_Mobile_Lifecycle.svg
..     :figwidth: 100%
..     :align: center
..     :target: https://www.plantuml.com/plantuml/svg/XP5TQy8m58RlyoiEUhC9ObTqZ295jyRH6-bIbS7OHMTEPo3ze4qttAzVx48Z7M9lsfuylE_3oQ9MIQMQJ9A3u0YObUe87Ejz9KebYfmG3IY4CDTlAP73SBLQpXp7p0Sxh4Gga0yWgO5XmeymTDs7HzSrn3R_CWWCK_quJdSWR6XmFvrDPuIyZTvXp8llVEpRJWzO54AuZZUactMKZJ7STjqdA_5vK1fjzVuWHfz9-tirnr0IK_NVYT6T0MpyV5_8el8-P8D-50QJcvTRkbn2nEXyqXxvlMQx8G-UADi0VOs87LurF4URqegqMOo6SNoEz0elsuuwNSjVsaD0JmkrWXhKaBvCNL2B7_JkN7y-ENtvP84vRpBv2m00

..     Lifecycle of the Mobile Relying Party Instance

Come mostrato in :numref:`fig_RelyingParty_Instance_Mobile_Lifecycle`, l'App di Verifica Mobile ha quattro stati distinti: **Installed**, **Unverified**, **Verified** e **Uninstalled**. Ogni stato rappresenta uno stato funzionale specifico e determina le azioni che possono essere eseguite.



Transizione a Installed
"""""""""""""""""""""""

La macchina a stati inizia con l'installazione della App di Verifica (transizione **RPI INST**), dove gli Utenti scaricano e installano una App di Verifica utilizzando l'app store ufficiale del sistema operativo del loro dispositivo, portando allo stato **Installed**.

In questo stato, l'App di Verifica DEVE interagire solo con il Backend della Relying Party per essere registrata (cioè, per verificare l'integrità dell'Istanza, registrare le Cryptographic Hardware Keys e ottenere un Certificato di Accesso).

Quando avviene la revoca dell'App di Verifica (transizione **RPI REV**), l'App di Verifica DEVE tornare da **Verified** a **Installed**. Questa transizione implica le seguenti operazioni:

1. Il Certificato di Accesso DEVE essere revocato.
2. Le Cryptographic Hardware Keys DEVONO essere cancellate.

La revoca può avvenire nei seguenti casi:

- Per motivi di sicurezza (ad es., compromissione del materiale crittografico).
- Per motivi tecnici (ad es., deprecazione della Soluzione di Relying Party).
- In caso di de-registrazione della Relying Party (come dettagliato in `EIDAS-ARF`_, Sezione 6.4.3).
- Attività illegali segnalate da Organi Giudiziari o di Supervisione.

Inoltre, ogni Relying Party DOVREBBE stabilire un periodo di tempo (periodo di grazia) durante il quale l'App di Verifica può richiedere presentazioni di Credenziali Elettroniche autenticandosi verso un'Istanza del Wallet utilizzando un Certificato di Accesso scaduto. Dopo questo periodo, l'App di Verifica DEVE essere de-registrata (transizione **RPI DEREG**) e tornare allo stato **Installed**. Questa transizione implica che le Cryptographic Hardware Keys DEVONO essere cancellate.

Transizione a Verified
""""""""""""""""""""""

L'App di Verifica deve ottenere un Certificato di Accesso appropriato, che sarà utilizzato per autenticarsi verso le Istanze del Wallet. Questo Certificato viene ottenuto interagendo con il Backend della Relying Party, che a sua volta comunica con l'Autorità di Certificazione per i Certificati di Accesso dell'App di Verifica. In particolare, la transizione di registrazione (**RPI REG**) consiste nelle seguenti sottofasi, che portano allo stato **Verified**:

1. **Inizializzazione**: Dopo la verifica dell'integrità dell'App di Verifica, questa registra una coppia di Cryptographic Hardware Keys.
2. **Emissione del Certificato di Accesso**: L'App di Verifica ottiene un Certificato di Accesso.

Nel caso in cui il Certificato di Accesso sia scaduto, un nuovo Certificato di Accesso può essere emesso per l'App di Verifica; questa operazione è rappresentata dalla transizione **CERT REISS** verso lo stato **Verified**.

In questo stato, l'App di Verifica può richiedere la presentazione di Attestati Elettronici alle Istanze del Wallet (**PID/(Q)EAA PRE**), utilizzando il Certificato di Accesso per autenticarsi (:ref:`test-plans-remote-presentation:RPR-11`, :ref:`test-plans-remote-presentation:RPR-21`, :ref:`test-plans-remote-presentation:RPR-22`, :ref:`test-plans-remote-presentation:RPR-50`, :ref:`test-plans-remote-presentation:RPR-51`, :ref:`test-plans-remote-presentation:RPR-61`, :ref:`test-plans-remote-presentation:RPR-62`).


Transizione a Unverified
""""""""""""""""""""""""

La scadenza del Certificato di Accesso (transizione **CERT EXP**) porta allo stato **Unverified**.

In questo stato, l'App di Verifica può ancora richiedere la presentazione di Attestati Elettronici alle Istanze del Wallet durante il periodo di grazia. Tuttavia, poiché il Certificato è scaduto, un disclaimer specifico DEVE essere mostrato all'Utente dell'Istanza del Wallet durante il flusso di presentazione; per questo motivo, questa operazione è rappresentata dall'etichetta **PID/(Q)EAA PRE**. Questo è necessario per supportare i flussi di presentazione offline. Dopo che il periodo di grazia è trascorso, la Relying Party Instance NON DEVE più richiedere presentazioni e sarà de-registrata (:ref:`test-plans-proximity-presentation:PPR-014`, :ref:`test-plans-proximity-presentation:PPR-015`, :ref:`test-plans-proximity-presentation:PPR-017`, :ref:`test-plans-proximity-presentation:PPR-019`).



Transizione a Uninstalled
"""""""""""""""""""""""""

Attraverso gli stati **Installed**, **Verified** e **Unverified**, la Relying Party Instance può essere rimossa completamente attraverso la disinstallazione dell'App di Verifica (transizione **RPI UNINST**), portando allo stato **Uninstalled**. Se un'App di Verifica è **Uninstalled**, termina il suo ciclo di vita (:ref:`test-plans-remote-presentation:RPR-34`, :ref:`test-plans-remote-presentation:RPR-46`, :ref:`test-plans-remote-presentation:RPR-59`, :ref:`test-plans-remote-presentation:RPR-73`, :ref:`test-plans-remote-presentation:RPR-47`, :ref:`test-plans-remote-presentation:RPR-48`, :ref:`test-plans-remote-presentation:RPR-74`, :ref:`test-plans-remote-presentation:RPR-75`).


Funzionalità dell'App di Verifica Mobile
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Un'App di Verifica DEVE supportare tre funzionalità fondamentali: **Registrazione**, **Riemissione del Certificato di Accesso** e **Revoca**. Ogni funzionalità è descritta in dettaglio nelle sezioni seguenti.

.. note::
  In questa sezione, i servizi utilizzati per attestare l'autenticità dell'App di Verifica e del dispositivo in cui è installata sono indicati come **Servizio di Integrità del Dispositivo**. Il Servizio di Integrità del Dispositivo è considerato in modo astratto e si presume che sia un servizio fornito da una terza parte affidabile (cioè, l'API del fornitore del sistema operativo) in grado di eseguire controlli di integrità sull'Istanza del Wallet e sul dispositivo in cui è installata.

.. note::
  I dettagli forniti di seguito sono non normativi e sono destinati a chiarire le funzionalità dell'App di Verifica Mobile. L'implementazione effettiva può variare in base al caso d'uso specifico e ai requisiti della Relying Party.


Registrazione App di Verifica Mobile
""""""""""""""""""""""""""""""""""""""""""

Questo processo consente la registrazione di un'App di Verifica con il Backend della Relying Party e l'emissione di un Certificato di Accesso che sarà utilizzato per autenticarsi verso le Istanze del Wallet durante i flussi di presentazione. Il processo consiste in due sottofasi:

1. **Inizializzazione**: L'App di Verifica richiede un'asserzione di sicurezza e integrità dal produttore del sistema operativo, che lega anche una coppia di chiavi crittografiche asimmetriche a lunga durata memorizzata in un adeguato storage sicuro all'interno del dispositivo stesso; l'asserzione viene quindi convalidata dal Backend della Relying Party. Ulteriori dettagli sono forniti nella Sezione :ref:`mobile-application-instance:Istanza dell'Applicazione Mobile`.
2. **Emissione del Certificato di Accesso**: L'App di Verifica richiede un Certificato di Accesso dal Backend della Relying Party. Prima di interagire con l'Autorità di Certificazione per l'emissione del Certificato di Accesso, il Backend della Relying Party convalida l'integrità e la sicurezza dell'App di Verifica sfruttando le chiavi attestate a lunga durata generate nella sottofase precedente. Il flusso è mostrato in :numref:`fig_RelyingParty_Instance_Mobile_Registration_AccessCertificateIssuance`, mentre una descrizione passo-passo è fornita di seguito.

.. note::
  I Certificati di Accesso POSSONO essere emessi come a breve durata (tipicamente validi entro 24 ore) o a lunga durata.

.. _fig_RelyingParty_Instance_Mobile_Registration_AccessCertificateIssuance:
.. plantuml:: plantuml/rp-mobile-instance-access-certificate-issuance.puml
    :width: 99%
    :alt: La figura illustra il Flusso di Emissione del Certificato di Accesso dell'App di Verifica Mobile.
    :caption: `Flusso di Emissione del Certificato di Accesso della App di Verifica Mobile. <https://www.plantuml.com/plantuml/svg/ZLF1ZjD03BtdAwpX04Zm0psWBMM1QeMqQijjfSYPkCsewSmmdXJozpXX89tL2EsXKMg_Ppy_EtSSCSJXqbSuH6U7IqEXwanBS7GkDkvNLRr-58JHngEDNA6EBe3wpXGK8CF0Gl0B0jGtrvYUO4VzQEm99lO8MokDhAQPWzv3plb4LwD9K95EmGX-Js6Eh1-tVoWO6Lwn3rBo58Xipi-RVKHz9jlEn4QVoz1SrvDTQqtCi2717et6ACs7sBb9pbn9etYnFwnt1zZSxmxRpzlD-d1VoJ3lFyXZ1PkEz1dC4JPXzD6T0lhEQFYAeVs9WU21HeRf1QzeUcnwgcxONyXIm4W2WJEDuD44UAEKlDT-Q9Hw1-bFC5UbtYQkpBSIhtyCn540raqcgsbDvegHvldbDmEN9WjoJYO9Ix2bh411fe1rRyZ6kiM8IW7QzibgT_73ysJT8NTID5N1oAiYO14zOGGkpqMQ-NiRDJ9FIt8s5vf89QLTMa7DvcGn3a5cB48VIAx7s7Owa6JghS_bTCdgT0qCpfPPDxRdUVREChrW0zcfxcMmc_hJuMWEpyuanNB5HSa9cP8Q2zpfSz0u9-Vk2qUY_nhY_5NLUf6QBqrZPiN_2GKpzj45UW5DmDKTsNQuzBy1>`_


.. .. figure:: ../../images/RelyingParty_Instance_Mobile_Registration_AccessCertificateIssuance.svg
..     :figwidth: 100%
..     :align: center
..     :target: https://www.plantuml.com/plantuml/svg/ZPF1ZjCm48RlUOgHEG0Il40FQBFL0XL2MhNbjb8rSQQDrTGszgIGjsSIBDnK5jh3HbdFzu__-JDzY8o1XqjVuS3E3fU6GjMPbk3e73VkTrMzVHR2QEFHSgnGimkWVaGA2Z3244NWCm7gksjCJx2bVZJs19DwX8sDZ5RJh47lOQdvHYFKp2GG6sUXVjx4loXoX3VH1sbr2aHsgLjUyeZwJBQTXOq-Bz6odnTRQqqnmfg4FHgDJ50FtBbWU9mxQPGCTljwkuVrqtQ_-RnPr_kdIeRu-4aUArXtfCzWZh0EesTt2kWxe-4hXlON1W8PBiBqWbSqFJOzLJVgBsGf89CWS9OOF9e0xvIIzuCV6gK-GFedcAjIxvDMvbj9nZy7YYo0TLEuQleyvefCy_poDuFvaapEnMGX7xQqQ52mAR3k3La-jCYe5A1jNwns5p_S5myTnawQfYx8SLK4ikc94LoUsTeqEkRLo2QpeEYoI_4VeZbPv278V4Lqshr7OzjfELAWjncNowMOqoP4SBQiof7VrQDtDj8hqb-iwKu6k-a_BOsEuMv5qjdIST5o8bDHOq6hiQeqpiNvzgoHqtyNuloBEkXiTVdHD2wY-B-W4CQENQ1No0Ik7iYsmwN_0m00

    Flow of the App di Verifica Mobile Access Certificate Issuance


**Passi 1-2:** La App di Verifica Mobile:

  1. Verifica l'esistenza delle Cryptographic Hardware Keys. Se non esistono, è necessaria la re-inizializzazione dell'App di Verifica.
  2. Genera una coppia di chiavi asimmetriche per il Certificato di Accesso (``key_pub``, ``key_priv``).

**Passi 3-5:** L'App di Verifica Mobile richiede un ``nonce`` dall':ref:`relying-party-endpoint:Endpoint Nonce della Relying Party` del Backend della Relying Party. Questo ``nonce`` DEVE essere imprevedibile per servire come principale difesa contro i replay attack.

In caso di richiesta riuscita, l':ref:`relying-party-endpoint:Endpoint Nonce della Relying Party` genera e restituisce il ``nonce`` all'App di Verifica Mobile. L':ref:`relying-party-endpoint:Endpoint Nonce della Relying Party` DEVE garantire che sia monouso e valido solo entro un periodo di tempo specifico.

Esempi non normativi della Richiesta e Risposta del Nonce possono essere trovati rispettivamente nelle sezioni :ref:`mobile-application-instance:Richiesta di Nonce dell'Applicazione Mobile` e :ref:`mobile-application-instance:Risposta di Nonce dell'Applicazione Mobile`.

**Passo 6:** L'App di Verifica:

  1. Genera ``client_data``, un JSON Object che include ``nonce`` e l'impronta digitale di ``key_pub``, ottenuta dalla sua rappresentazione ``JWK``.
  2. Calcola ``client_data_hash`` applicando l'algoritmo SHA256 a ``client_data``.

Di seguito è riportato un esempio non normativo di ``client_data``.

.. code-block:: json

    {
      "nonce": "f3b29a81-45c7-4d12-b8b5-e1f6c9327aef",
      "jwk_thumbprint": "hT3v7KQjFZy6GvDkYgOZ1u2F6T4Nz5bPjX8o1MZ3dJY"
    }

**Passi 7-8:** L'App di Verifica Mobile:

  1. Richiede al Servizio di Integrità del Dispositivo di creare un valore ``integrity_assertion`` collegato al ``client_data_hash``.
  2. Riceve un valore ``integrity_assertion`` firmato dal Servizio di Integrità del Dispositivo, autenticato dall'OEM.

**Passi 9-11:** L'App di Verifica Mobile:

  1. Genera un valore ``hardware_signature`` firmando il ``client_data_hash`` con la chiave privata Cryptographic Hardware, che servirà come prova di possesso per le Cryptographic Hardware Keys.
  2. Genera la :ref:`relying-party-endpoint:Richiesta di Associazione Chiavi della Relying Party` sotto forma di JWT. Questo JWT include ``integrity_assertion``, ``hardware_signature``, ``nonce``, ``hardware_key_tag`` e ``cnf`` (che rappresenta ``key_pub``); è firmato utilizzando ``key_priv``.
  3. Invia il JWT firmato :ref:`relying-party-endpoint:Richiesta di Associazione Chiavi della Relying Party` come parametro ``assertion`` nel corpo di HTTP request all':ref:`relying-party-endpoint:Endpoint di Associazione Chiavi della Relying Party`.

**Passo 12:** Il Backend della Relying Party valuta la Richiesta di Key Binding ed esegue i seguenti controlli:

  1. La richiesta include tutti i parametri di intestazione HTTP richiesti come definito in :ref:`relying-party-endpoint:Richiesta di Associazione Chiavi della Relying Party`.
  2. La firma della Richiesta di Key Binding è valida e verificabile utilizzando il ``jwk`` fornito.
  3. Il valore ``nonce`` è stato generato dal Backend della Relying Party e non è stato utilizzato in precedenza.
  4. L'App di Verifica possiede valide Cryptographic Hardware Keys registrate.
  5. Il ``client_data`` può essere ricostruito utilizzando ``nonce`` e ``cnf`` (che rappresenta ``key_pub``). Il valore del parametro ``hardware_signature`` viene quindi convalidato utilizzando la chiave pubblica della Cryptographic Hardware Key registrata associata all'App di Verifica.
  6. L'``integrity_assertion`` può essere convalidata secondo le linee guida del produttore del dispositivo. I controlli specifici eseguiti dal Backend della Relying Party sono dettagliati nella documentazione del produttore del sistema operativo.
  7. Il dispositivo in uso è privo di difetti di sicurezza noti e soddisfa i requisiti minimi di sicurezza definiti dalla Relying Party.
  8. L'URL nel parametro ``iss`` corrisponde all'identificatore URL della Relying Party.

**Passo 13:** Se i controlli hanno successo, il Backend della Relying Party risponde con una conferma di successo (:ref:`relying-party-endpoint:Risposta di Associazione Chiavi della Relying Party`).

**Passo 14:** L'App di Verifica Mobile genera una Certificate Signing Request (CSR, ``csr``) utilizzando ``key_pub`` e ``key_priv``.

**Passo 15:** L'App di Verifica Mobile invia la CSR al :ref:`relying-party-endpoint:Endpoint del Certificato di Accesso della Relying Party` del Backend della Relying Party, come parte della :ref:`relying-party-endpoint:Richiesta del Certificato di Accesso della Relying Party`.

**Passi 16-17:** Il Backend della Relying Party verifica che la chiave pubblica nella CSR corrisponda a un'App di Verifica che è stata precedentemente convalidata, cioè che corrisponda a quella legata alle Cryptographic Hardware Keys attraverso ``hardware_signature``. Se questo controllo ha successo, il Backend della Relying Party invia la CSR all'Autorità di Certificazione per i Certificati di Accesso dell'App di Verifica.

**Passi 18-19:** L'Autorità di Certificazione per i Certificati di Accesso dell'App di Verifica firma la CSR, ottenendo un Certificato di Accesso valido (``access_certificate``) che invia al Backend della Relying Party.

**Passi 20-21:** Il Backend della Relying Party invia il Certificato di Accesso (come parte della :ref:`relying-party-endpoint:Risposta del Certificato di Accesso della Relying Party`) all'App di Verifica Mobile, che lo memorizza per future autenticazioni verso le Istanze del Wallet.


Riemissione de Certificato di Accesso App di Verifica Mobile
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

L'emissione di un nuovo Certificato di Accesso segue lo stesso flusso descritto nella sezione :ref:`relying-party-instance:Registrazione App di Verifica Mobile` per **Emissione del Certificato di Accesso**. Questi certificati POSSONO essere emessi come a breve durata (tipicamente validi entro 24 ore) o a lunga durata.


Revoca App di Verifica Mobile
""""""""""""""""""""""""""""""""""""""""

Le Relying Party DEVONO verificare periodicamente l'autenticità e la sicurezza delle App di Verifica.
Quando vengono rilevati problemi di sicurezza, le Relying Party DEVONO revocare l'App di Verifica, revocando il suo Certificato di Accesso X.509 (in caso di certificati a lunga durata), e in ogni caso, le Relying Party NON DEVONO consentire la riemissione di certificati.
Di conseguenza, la revoca dell'App di Verifica Mobile DEVE essere legata alla validità dei Certificati di Accesso X.509.

I Certificati X.509 a lunga durata seguono i requisiti relativi al loro ciclo di vita, definiti in :ref:`trust:L'Infrastruttura di Trust`.


App di Verifica Web
--------------------------

Le Web Instance operano controlli di sicurezza lato server che memorizzano in modo sicuro segreti e chiavi crittografiche in un ambiente controllato. Le App di Verifica Web DEVONO essere registrate presso la Trust Anchor o le Entità Intermediarie, secondo :ref:`trust:L'Infrastruttura di Trust`.


Funzionalità dell'App di Verifica Web
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Un'App di Verifica Web DEVE supportare due funzionalità fondamentali: **Registrazione** e **Revoca**. Ogni funzionalità è descritta nelle sezioni seguenti.


Registrazione Revoca App di Verifica Web
"""""""""""""""""""""""""""""""""""""""""

Le App di Verifica Web, in qualità di OAuth Confidential Client, sono registrate direttamente dalla Trust Anchor o un'Entità Intermediaria. La registrazione comporta:

- La Relying Party DEVE registrare la sua App Web con la Trust Anchor o con le appropriate Entità Intermediarie della Federazione.
- La Relying Party DEVE esporre una Entity Configuration come definito nel Trust Framework.
- L'Entity Configuration DEVE contenere tutti i metadati necessari per la federazione, inclusi gli endpoint e le chiavi pubbliche.
- Non è richiesta alcuna gestione del ciclo di vita delle singole istanze, poiché l'App Web opera come parte dell'ambiente server protetto.


Revoca App di Verifica Web
"""""""""""""""""""""""""""""""""""""

Quando una App di Verifica Web deve essere revocata:

- La revoca DEVE essere eseguita secondo le procedure del Trust Framework.
- Le chiavi crittografiche utilizzate dall'App Web DEVONO essere revocate.
- L'Entity Configuration DEVE essere aggiornata per riflettere la revoca.
- La Trust Anchor DEVE essere notificata della revoca per aggiornare i metadata della federazione.

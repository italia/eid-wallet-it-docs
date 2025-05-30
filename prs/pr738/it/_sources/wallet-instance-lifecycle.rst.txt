.. include:: ../common/common_definitions.rst

.. level 3 "included" file, so we start with '"' title level

Ciclo di vita dell'Istanza del Wallet
"""""""""""""""""""""""""""""""""""""

Il Fornitore di Wallet è responsabile dell'implementazione e della fornitura delle Istanze del Wallet, gestendo anche l'intero ciclo di vita.

In questa sezione, vengono presentate macchine a stati per spiegare gli stati delle Istanze del Wallet e delle Credenziali Elettroniche e le loro transizioni e relazioni.

.. note::
  L'Attestato Elettronico di Dati di Identificazione Personale è un tipo specializzato di Credenziale Elettronica che ha impatti sul ciclo di vita dell'Istanza del Wallet. La revoca dell'Attestato Elettronico di Dati di Identificazione Personale PUÒ avere anche potenziali impatti sugli Attestati Elettronici di Attributi (Qualificati), se questi sono stati emessi utilizzando la presentazione dell'Attestato Elettronico di Dati di Identificazione Personale.
  Quando non è necessaria la distinzione tra Attestato Elettronico di Dati di Identificazione Personale e Attestati Elettronici di Attributi (Qualificati), viene utilizzato il termine Credenziale Elettronica.


Come mostrato in :numref:`fig_Wallet_Instance_States`, l'Istanza del Wallet ha quattro stati distinti: **Installato**, **Operativo**, **Valido** e **Disinstallato**.
Ogni stato rappresenta uno stato funzionale specifico e determina le azioni che possono essere eseguite.

.. _fig_Wallet_Instance_States:
.. plantuml:: plantuml/wallet-instance-states.puml
    :width: 99%
    :alt: La figura illustra gli Stati dell'Istanza del Wallet.
    :caption: `Stati dell'Istanza del Wallet. <https://www.plantuml.com/plantuml/svg/XP9HIyCm58NVyoikx4M5qYgRo1XbnMLGa3bNjmdgGsmp5qZJqgQ8_dgJLTjhwzYUnZtVEVVSjjDIiq9NgOGjav9h29MPg9X3f9dc9TcBX0DFS_q92I_ZGkHQP8gGqierRNm93ERpOEHvF_Fxd1VCWap2O6T-ZR9XKXZQyswyPhPMeisPNGz7mn4X0F1yyGfEadqensytZM4RGhY87YtHZXlGXc5qlVWFBiJxNXiQ5JtGmMsDeld9v2uk-Kxt6g_efazsza_YJ6R5-4rMt3zxEAT1064KkSiLdRW7oJ_MhNwiVnEMuSpQiRN6mAdopkgkZpujtLyZl2WicqFS6Rqx6jix6n6TekXKYa_5Qt4hfEBGqwy7IU0Or7nOfa8fllZuyigVkFQVJwPS9LKglm40>`_


.. .. figure:: ../../images/Wallet_Instance_States.svg
..     :figwidth: 100%
..     :align: center
..     :target: https://www.plantuml.com/plantuml/svg/XPBHIuH04CRVzwyOk9SAH8ipGaHESW-4kEpihg1wi7ElMzXRHLUY_lfMAvtMZlD5cUytttpZxgnMMQMQlI0xdZDW-r9zGCxgJSLBnGj9Y0OKWrZgjn0iXyby7hgEyrE_BLcLjM0cOBBLJw-iCy4rxJXNJbzRIJxuH9TJT-eI0W1FPozWvSMxj89XaWSFCSIBzBubXd8FjcOONIt-Wol-jbEQHa4xEhpkK5m_xcpWWctLAF6IhaUaET_V5AAel5VHiE3axfI68SHfQYTBwjkT51pCrltMlmv97BNjkFKR0wifZT5c7trCxDz6U9POrelO4RqvP3jU6n4egB4gnQlYiJWLKf7fyUF14bWQrHTBHwZv9_FEBmBVRhy2CcCorrV-2m00

..     Wallet Instance Lifecycle.

.. note::
  Il Fornitore di Wallet DEVE garantire la sicurezza e l'affidabilità delle Istanze del Wallet. Per raggiungere questo obiettivo, il Fornitore di Wallet DEVE verificare periodicamente lo stato di sicurezza e conformità delle Istanze del Wallet.

Transizione a Installato
........................

La macchina a stati inizia con la transizione di installazione dell'Istanza del Wallet (**WI INST**), dove gli Utenti scaricano e installano un'Istanza del Wallet fornita dal Fornitore di Wallet utilizzando lo
store ufficiale delle applicazioni del sistema operativo del loro dispositivo (questo garantisce l'autenticità tramite controlli di sistema), portando allo stato **Installato**.

Quando lo stato è **Installato**, l'Istanza del Wallet DEVE interagire solo con il Fornitore di Wallet per essere attivata. Quando avviene la revoca dell'Istanza del Wallet, l'Istanza del Wallet DEVE tornare da **Operativo** o **Valido** a **Installato**. La revoca segna la Cryptographic Hardware Key del Wallet, registrata durante l'attivazione
(vedi :ref:`wallet-instance-lifecycle:Transizione a Operativo`), come non più utilizzabile. La revoca può avvenire nei seguenti casi:

* per motivi tecnici di sicurezza (ad esempio, relativi alla compromissione del materiale crittografico);
* in caso di richieste esplicite dell'Utente (ad esempio, a causa di perdita o furto dell'Istanza del Wallet);
* morte dell'Utente;
* attività illegali segnalate da Organi Giudiziari o di Vigilanza.

.. note::
  Mentre per l'ARF la revoca dell'Istanza del Wallet viene realizzata revocando l'Attestato di Wallet (vedi Argomento 9 e Argomento 38 nell'Allegato 2),
  in questa specifica la revoca è gestita diversamente. Essendo l'Attestato di Wallet a breve durata, non ha un meccanismo di gestione dello stato.
  Per questo motivo, la transizione di revoca dell'Istanza del Wallet viene realizzata eliminando la Cryptographic Hardware Key del Wallet dal WSCD dell'Istanza del
  Wallet e dall'account associato all'Utente. Questa transizione viene completata quando l'Istanza del Wallet è online.

Transizione a Operativo
.......................

Dopo l'installazione, l'Utente apre l'Istanza del Wallet e inizia un'attivazione (**WI ACT**).
In questa fase, un account Utente DEVE essere creato con il Fornitore di Wallet e associato all'Istanza del Wallet tramite il Cryptographic Hardware
Key Tag, previa acquisizione del consenso dell'Utente (vedi :ref:`wallet-instance-registration:Inizializzazione e Registrazione dell'Istanza del Wallet` per maggiori dettagli).
Questa associazione consente all'Utente di richiedere direttamente la revoca dell'Istanza del Wallet dal Fornitore di Wallet, e consente anche al Fornitore di Wallet di
revocare l'Istanza del Wallet associata a quell'Utente.

.. note::
  Come risultato della creazione dell'account Utente, DEVE essere impostato un meccanismo di autenticazione per l'Utente per interagire con il portale del Fornitore di Wallet.
  Questa specifica impone l'uso di almeno un secondo fattore per l'autenticazione dell'Utente.

Come parte dell'attivazione, il Fornitore di Wallet DEVE valutare il sistema operativo e le capacità tecniche generali del dispositivo per verificare la conformità
con i requisiti tecnici e di sicurezza, e l'autenticità e l'integrità dell'Istanza del Wallet installata.
Dopo la verifica con successo, il Fornitore di Wallet DEVE emettere almeno un Attestato di Wallet valido all'Istanza del Wallet, quindi l'Istanza del Wallet entra nello stato **Operativo**.

Inoltre, se non è già stato fatto, gli Utenti DEVONO impostare il loro metodo preferito per sbloccare la loro Istanza del Wallet; questo PUÒ essere realizzato inserendo un
numero di identificazione personale (PIN) o utilizzando l'autenticazione biometrica, come l'impronta digitale o il riconoscimento facciale, secondo le preferenze
personali e le capacità del dispositivo. Si prega di fare riferimento a :ref:`wallet-attestation-issuance:Emissione dell'Attestato di Wallet`.

Nello stato **Operativo**, gli Utenti possono richiedere l'emissione dell'Attestato Elettronico di Dati di Identificazione Personale (**PID ISS**) o di Attestati Elettronici di Attributi (Qualificati) se l'Attestato Elettronico di Dati di Identificazione Personale non è richiesto nell'emissione
(**(Q)EEA ISS**). Inoltre, se le Credenziali Elettroniche sono Attestati Elettronici di Attributi (Qualificati) e per la presentazione non richiedono l'Attestato Elettronico di Dati di Identificazione Personale, possono essere presentate
senza far transitare l'Istanza del Wallet a un altro stato (transizione **(Q)EEA PRE**).

Un'Istanza del Wallet **Valida** DEVE transitare nuovamente allo stato **Operativo** a causa della transizione **PID EXP/REV/DEL**, quando l'Attestato Elettronico di Dati di Identificazione Personale associato scade, viene revocato dal suo Fornitore o viene eliminato dall'Utente.

Transizione a Valido
....................

Una transizione allo stato Valido si verifica solo quando l'Istanza del Wallet ottiene un Attestato Elettronico di Dati di Identificazione Personale valido (**PID ISS**). In questo stato, gli Utenti possono ottenere e presentare
nuovi Attestati Elettronici di Attributi (Qualificati) (**(Q)EAA ISS/PRE**), e presentare l'Attestato Elettronico di Dati di Identificazione Personale (**PID PRE**). Si prega di fare riferimento a :ref:`credential-issuance:Emissione di Credenziale Digitale` e :ref:`credential-presentation:Presentazione della Credenziale Digitale`.

.. note::
  Gli Utenti possono avere solo un'Istanza del Wallet in stato **Valido** per la stessa Soluzione Wallet. Pertanto, quando un Utente installa e ottiene un Attestato Elettronico di Dati di Identificazione Personale su una nuova Istanza
  del Wallet della stessa Soluzione Wallet dallo stesso Fornitore di Wallet, l'Attestato Elettronico di Dati di Identificazione Personale nella precedente Istanza del Wallet DEVE essere revocato e l'Istanza del Wallet diventa
  **Operativa**.

Transizione a Disinstallato
...........................

In tutti gli stati, **Installato**, **Attivato**, **Operativo** o **Valido**, l'Istanza del Wallet può essere rimossa completamente attraverso la transizione di disinstallazione dell'Istanza del Wallet
(**WI UNINST**), portando allo stato **Disinstallato**. Se un'Istanza del Wallet è **Disinstallata** termina il suo ciclo di vita.

Gestione del Ciclo di Vita dell'Istanza del Wallet
..................................................

Mentre :numref:`fig_Wallet_Instance_States` mostra i diversi stati che un'Istanza del Wallet può acquisire durante il suo ciclo di vita,
:numref:`fig_Wallet_Instance_Lifecycle` mostra il punto di vista delle Istanze del Wallet e dei Fornitori di Wallet nella gestione del ciclo di vita dell'Istanza del Wallet
e l'effetto sul loro storage locale.

.. _fig_Wallet_Instance_Lifecycle:
.. plantuml:: plantuml/wallet-instance-lifecycle.puml
    :width: 99%
    :alt: La figura illustra la Gestione del Ciclo di Vita dell'Istanza del Wallet.
    :caption: `Gestione del Ciclo di Vita dell'Istanza del Wallet. <https://www.plantuml.com/plantuml/svg/dP9HgzCm5CVVyocEOGyj37ovZqvkRGDtC5r9gqCGHjOSQo1BPdhQESJlxhAvEMP1lQ___Fud_VNaiICLgDzQM2bhaM3kZebh41RcCpQ7nYAyLKwrk4L7x8LnZUqrmglyuMN-iCwz8sKSXjViQLw8TLKBAPRrnr8aAMFLqtArBeMibk_MvLBMCflNCS-qbcXhrIPSR_WK9eJVAFVMXndtGRaMOsYDmz6meeD5c46XkY-e5ySaILF6tlZUQHKEIR-P0h_NkPpo5BupO03LeIFS9ghvEa9d3Pb1aV4EFhbaDOSihrD-17dwkwhHZbGb3hwvhKhnuL8zTgz_hDWa-uvycFAAV50jNiUp7-p6fhcnAOCVZCPmPtFve1RTSrq23l_dSgToCe6Bofz8iklZUQ58GTc7rhZs14qdtIuOmXaFVkE9foTvYVPS-3Ms40jHYtC19gJQRXPVJXh1Q7q5SocoKJ2Ivrtl_u96yhpQ_R_S7d2utlw-BCP7FgBJ_TR-1000>`_


.. .. figure:: ../../images/wallet_instance_lifecycle.svg
..     :figwidth: 100%
..     :align: center
..     :target: https://www.plantuml.com/plantuml/svg/dP9Vgvim6CRl_HIPd0k5ddgpgq7XE0sSGhUAUbO6WnBDYnLYuf9NkpBstPUurPLEs9yRBzuyloV-aZmPP1g7JdYlMbcBWGCv8VRcJHHfTbutBPw6QZ2WQoKH9AvhrKMzOD8nZmQvQAieUVsOkT7BkrtKCOEWxUYOM8Ar4lIwT_tFsvGUYvBcT5z-p6WGUbxnl3ySCveN-_V7R9-NURmjtJpcF0THiYRmUUMlo0F25qoKK7hZAyra0sueRFVYiC2B0B8XAJCdu3ix2KBR-bODaZDz2OPgHVm34mAGRAL19ciWrrK_95yzuX5INAn85x3wyq8whh4T6RPAaayoE6n9d9IXRuD--0lb81RG74PLtw8v_N15BJkVMbe5PuDAh_p2Vba3SxttpRkngMziCgt6beE-ixd-K0FoVrqqZF_cSgSocP3VLEP8q0zkFMN8I3ReffND55ezc5wt21jVgqgXXPny3k87yBCsfJjQqWbmhuKrPkDUJkY2pdeE9ZcD5uDJShhhyv-YBZbTxVblTjSmphk_PEbovHD8FdJYEm00

..     Wallet Instance Lifecycle Management.

Attraverso un'Istanza del Wallet in stato **Installato**, un Utente è in grado di avviare l'**Attivazione dell'Istanza del Wallet** (**WI ACT**).
Come risultato, l'Istanza del Wallet DEVE creare una coppia di Cryptographic Hardware Key. Inoltre, se non è già stato fatto,
gli Utenti DEVONO impostare il loro metodo preferito per sbloccare la loro Istanza del Wallet. Come risultato della **Revoca dell'Istanza del Wallet** (**WI REV**), l'Istanza del Wallet DEVE
eliminare le coppie di Cryptographic Hardware Key.

Un Fornitore di Wallet invece è responsabile per:

* **Attivazione dell'Istanza del Wallet** (**WI ACT**): un account Utente DEVE essere creato e associato all'Istanza del Wallet tramite il Cryptographic Hardware Key Tag. Come risultato della creazione dell'account Utente, DEVE essere impostato un meccanismo di autenticazione di almeno due fattori per l'Utente per interagire con il portale del Fornitore di Wallet.
* **Revoca dell'Istanza del Wallet** (**WI REV**): per motivi tecnici di sicurezza o attivata da entità esterne (ad esempio, Utenti e Organi di Vigilanza) il Cryptographic Hardware Key Tag DEVE essere eliminato dall'account Utente.
* **Eliminazione dei Dati**: attraverso una richiesta esplicita degli Utenti, l'account Utente presso il Fornitore di Wallet DEVE essere rimosso dallo storage locale.

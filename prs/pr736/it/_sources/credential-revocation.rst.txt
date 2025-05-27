.. include:: ../common/common_definitions.rst


Ciclo di vita delle Credenziali
===============================

Il Fornitore di Credenziale è responsabile della creazione e del rilascio delle Credenziali, nonché della gestione del loro ciclo di vita e dello stato di validità.

La Fonte Autentica è l'entità responsabile della gestione e della fornitura degli Attributi dell'Utente ai Fornitori di Credenziale.
Esiste una relazione tra il ciclo di vita degli attributi gestiti dalla Fonte Autentica e il ciclo di vita delle Credenziali
gestito dal Fornitore di Credenziale. Infatti, uno dei motivi per la revoca o la sospensione delle Credenziali è l'aggiornamento/revoca o
sospensione degli attributi contenuti nella Credenziale. In IT Wallet, la fornitura degli Attributi dell'Utente e la notifica di
aggiornamenti o modifiche nello stato degli attributi vengono scambiati utilizzando l'infrastruttura PDND (vedere le relative sezioni per maggiori dettagli).


La :numref:`fig_DigitalCredential_States` mostra gli stati e le transizioni per le Credenziali.
Include quattro stati distinti: **Issued**, **Valid**, **Expired** e **Revoked**. Mentre, nel caso degli Attestati Elettronici di Attributi (Q)EAA c'è uno stato aggiuntivo: **Suspended**.
Una Credenziale in tutti gli stati può essere eliminata (**PID/(Q)EAA DEL**) e questo termina il suo ciclo di vita.

.. _fig_DigitalCredential_States:
.. plantuml:: plantuml/credential-states.puml
    :width: 80%
    :alt: La figura illustra gli Stati delle Credenziali.
    :caption: `Transazioni di Stato delle Credenziali. <https://www.plantuml.com/plantuml/svg/RP9HRzCm4CVV_IbEtSC0AIAK5Q4ze4Lh2fK6b6MRa807BxwrLXmxifsDWFZks8udjr7xLF_kVtS_dN9XBDMsRmNPSOQ0RMS7O6XgpJlBbIHMTM0Lt2jhLGkCQwm39wUGPV0H9Meg7ATRJLimTX1SRbs9c8RBZdh8y87smgwKj1N_W_1clbUiBBLOQAsUBfLG6ku5hPkZzKz8MUX_EorVSOatErut4es1UNJxJ1k4McbdQ81A1iB539XMARj3VUYeLI_PPGZ3F8VuEmL1zHPr70EQCjwRr1P6sg53w9GO_2EszIOXFzkweqIj9JvuQBou2HB-7nH2L2EY1cRk1UDp1l2Nn4pLcmubGmOdgrMnoFF8h_5HDPuktvqjpXQHbhyxhXEDwsyqbOPRhcHO_ZnwRKoFxAk-euApe30IK1e2cpaD6Ar702Tv_Zvt3Wx_UFKBCistEvjzWDXu3flrylMBRo_BelWfrrK5168jPVsaQVJHCsu729-c8V-SvA5UnjIJTDtf7kVmt5tTLfjft4NZYIQhhiixE1AEbvk4o-yRGjBAhEzSzB0vQTn-yI8fFf7O5vY4qlAznK326T974a_WBp_HN9PNvCADwrln7m00>`_


.. .. figure:: ../../images/DigitalCredential_States.svg
..     :figwidth: 100%
..     :align: center
..     :target: https://www.plantuml.com/plantuml/png/RP9HRzCm4CVV_IbEtSC0AIAK5Q4ze4Lh2fK6b6MRa807BxwrLXmxifsDWFZks8udjr7xLF_kVtS_dN9XBDMsRmNPSOQ0RMS7O6XgpJlBbIHMTM0Lt2jhLGkCQwm39wUGPV0H9Meg7ATRJLimTX1SRbs9c8RBZdh8y87smgwKj1N_W_1clbUiBBLOQAsUBfLG6ku5hPkZzKz8MUX_EorVSOatErut4es1UNJxJ1k4McbdQ81A1iB539XMARj3VUYeLI_PPGZ3F8VuEmL1zHPr70EQCjwRr1P6sg53w9GO_2EszIOXFzkweqIj9JvuQBou2HB-7nH2L2EY1cRk1UDp1l2Nn4pLcmubGmOdgrMnoFF8h_5HDPuktvqjpXQHbhyxhXEDwsyqbOPRhcHO_ZnwRKoFxAk-euApe30IK1e2cpaD6Ar702Tv_Zvt3Wx_UFKBCistEvjzWDXu3flrylMBRo_BelWfrrK5168jPVsaQVJHCsu729-c8V-SvA5UnjIJTDtf7kVmt5tTLfjft4NZYIQhhiixE1AEbvk4o-yRGjBAhEzSzB0vQTn-yI8fFf7O5vY4qlAznK326T974a_WBp_HN9PNvCADwrln7m00

..     Digital Credential Lifecycle.

.. note::
  Gli Utenti POSSONO presentare una Credenziale in qualsiasi stato, spetta alla policy della Relying Party accettare una Credenziale non Valida.
  Un esempio di questo scenario è quando una Relying Party deve verificare che l'Utente non sia minorenne. In questo caso, anche se l'Utente presenta una
  Credenziale **Issued/Expired/Revoked** o **Suspended**, l'attributo relativo all'età è ancora affidabile.

.. note::
  Mentre **Issued**, **Valid**, **Expired**, **Revoked** sono esplicitamente menzionati nell'ARF (vedi Figura 5 di ARF v1.4),
  **Suspended** è implicitamente presente in `EIDAS-ARF`_. Questa specifica lo considera esplicitamente.

Transizioni delle Credenziali
-----------------------------

Transizione della Credenziale a Issued
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Affinché la macchina a stati possa avviarsi, l'Istanza del Wallet DEVE essere nello stato **Operational** o **Valid**, consentendo il rilascio di Credenziali.
La macchina a stati inizia con lo stato **Issued**, quando viene attivato un processo di emissione e, di conseguenza, una Credenziale viene rilasciata all'
Istanza del Wallet (**PID/(Q)EAA ISS**). Si prega di fare riferimento a :ref:`credential-issuance:Emissione di Credenziale Digitale`.

Transizione della Credenziale a Valid
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Una Credenziale passa allo stato **Valid** quando:

  * raggiunge la sua data di inizio validità;
  * viene attivato un processo di riattivazione se l'Attestato Elettronico di Attributi (Q)EAA è stato sospeso.


Transizione della Credenziale a Expired
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Una Credenziale passa naturalmente allo stato **Expired** quando scade automaticamente al raggiungimento della sua data di fine validità (**PID/(Q)EAA EXP**),
indicando che non è più valida per l'uso.

Se una Credenziale è **Expired**, l'Istanza del Wallet DOVREBBE notificare all'Utente che la Credenziale è scaduta e l'Utente PUÒ eliminarla (**PID/(Q)EAA DEL**).
Questo termina il suo ciclo di vita.

Transizione della Credenziale a Revoked
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Una Credenziale passa dagli stati **Issued**, **Valid** o **Suspended** allo stato **Revoked** quando viene attivamente revocata dal Fornitore di Credenziale
tramite un processo di revoca (**PID/(Q)EAA REV**). Le Relying Party NON DOVREBBERO più considerare utilizzabile una particolare Credenziale quando è **Revoked**, anche se è
ancora temporalmente valida e contiene una firma valida del Fornitore di Credenziale. La revoca può avvenire nei seguenti casi:

  * per motivi tecnici di sicurezza relativi alla compromissione del materiale crittografico;
  * in caso di richieste esplicite dell'Utente;
  * come conseguenza di un aggiornamento degli attributi da parte delle Fonti Autentiche;
  * in caso di revoca degli attributi contenuti nella Credenziale notificata dalla Fonte Autentica;
  * morte dell'Utente;
  * revoca dell'Istanza del Wallet a cui è stata rilasciata la Credenziale;
  * attività illegali dell'Utente segnalate da Organi Giudiziari o di Vigilanza.

Nel caso del solo Attestato Elettronico di Dati di Identificazione Personale, i seguenti casi si aggiungono a quelli sopra elencati:

  * rilevamento di una violazione dell'identità digitale rilasciata da un Gestore di Identità DIgitale e utilizzata per autenticare l'Utente durante il rilascio del PID;
  * come risultato dell'ottenimento di un nuovo PID su una nuova Istanza del Wallet dallo stesso Fornitore di Wallet che ha fornito l'Istanza del Wallet contenente un PID precedentemente rilasciato.

.. note::
  Un Fornitore di Attestati Elettronici di Attributi (Q)EAA PUÒ revocare un Attestato Elettronico di Attributi (Q)EAA in caso di revoca del PID.

Quando una Credenziale è **Revoked** non può tornare allo stato **Valid**, l'Istanza del Wallet DOVREBBE notificare all'Utente che la Credenziale
è stata revocata e l'Utente PUÒ eliminarla (**PID/(Q)EAA DEL**). Questo termina il suo ciclo di vita.

Transizione della Credenziale a Suspended
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Un Attestato Elettronico di Attributi (Q)EAA passa dagli stati **Issued** o **Valid** allo stato **Suspended** quando viene sospeso dal Fornitore di Credenziale (**(Q)EAA SUSP**).
L'Attestato Elettronico di Attributi (Q)EAA rimane **Suspended** fino a quando non viene ripristinato allo stato **Issued** o **Valid** (**(Q)EAA UNSUSP**) a seconda dello stato precedente, cioè
le condizioni che hanno portato alla sua sospensione vengono risolte, o passa a **Revoked**, **Expired** o viene eliminato. La sospensione di un Attestato Elettronico di Attributi (Q)EAA PUÒ essere:

  * Guidata dal caso d'uso, basata sullo stato di validità degli attributi contenuti nell'Attestato Elettronico di Attributi (Q)EAA. In questo caso, una Fonte Autentica DEVE notificare al Fornitore di Credenziale qualsiasi cambiamento nello stato degli attributi attestati dall'Attestato Elettronico di Attributi (Q)EAA.
  * Esplicitamente richiesta dall'Utente.

Gestione del Ciclo di Vita delle Credenziali
--------------------------------------------

Mentre la :numref:`fig_DigitalCredential_States` mostra i diversi stati che una Credenziale può acquisire durante il suo ciclo di vita,
la :numref:`fig_DigitalCredential_Lifecycle` mostra il punto di vista delle Istanze del Wallet e dei Fornitori di Credenziale nella gestione del ciclo di vita delle Credenziali
e l'effetto sul loro storage locale.

.. _fig_DigitalCredential_Lifecycle:
.. plantuml:: plantuml/credential-lifecycle.puml
    :width: 99%
    :alt: La figura illustra il Ciclo di Vita delle Credenziali.
    :caption: `Gestione del Ciclo di Vita delle Credenziali. <https://www.plantuml.com/plantuml/svg/ZLHTRnCn47pthnYUQAMqLA9FAOM6faYH2gf2IeLQ5BbtUuc5OmVlNjBowucT3-LYABc7ABPdzcCywmiM7QIUMFNAkCBM9U7TvUcRozDXzzdfYIdUAwKIHZalX616Or5tOtBGw9gH4Mrn6QWa9qPREAAI8HwFX7fQQg6o1HdJDgR7N5DWVEvy1vCheU6ycCeKMentaHqPjqm1DHitWaQWaM6XG2LyBKU-EdhKhaJX9vFQhOd5M3j7zbZ5eB5SfTefYf-IOznfQqdGSopQ5NIcbAbmqAUPN_4d52COdk31uHnVHKlDk3Oi-708YKqVF1CVAYW0xJv9C3IZ1d3WVv93vKE4WCK7AhUQvxEqdxIqL4bQzUbNRI9k7bCuZvcsfan7UMXwCYoS3ZTjnaNiPKla5T4ut9yydRnjOV5x-cEdZVYHPSA1yuTGsFvO_5HXbSPKge5LSPahq66c4ANa_HI8RjfFWaRilqdmWWRdw7tvrhdkTVFkrwHYGnfo8WrB4ctiSLmHZDkWxszlkft1LGkTmQ3V-tWxk1ekTt9jzvIteV3Urx7yRJJHAGfYNjaawPULjFdo-Xh7oy6e0l5ultX0Uw5s43HPdwoVB-_xfNoP7i368ZjxM6RH3excwIM9eungaMSNEJSoJe_8QqQdZdNB-g7OWcPpbDz9ljhyYSyBkZV-1WtnnIEiHcC3ZVNc3-PQdCoxlFPkdDiMVC23-uzBppDF_lk-sd7WY2K9bEJnmVnEwfnjup9NDF34knaoJ_X0iVMivHVya3aYkuECk6_6dQbfTycI4AQ1PiRNtE2eLC35Wb9Fx1y0>`_

.. .. figure:: ../../images/DigitalCredential_Lifecycle.svg
..     :figwidth: 100%
..     :target: https://www.plantuml.com/plantuml/svg/XP91Yzim48Nl_XMgsOC3sVMbfq9WKzjq0sbZR8UbK0YoDIW2MV9AetL3wN-lvBPkIbro2T7JzvxVY7cqI0swNaPlXEgaOq3EY8DzbwQ6ZWzSuDcrpeBfj49G-D3fFXqaLS5pRv59qQRPs_ioICUF-xId5i5uwPHv1nKApCCGyfzsUN6gcw8g3itdiaXMKLG_7PvFPL7LXq-dyb0rrNRN17tBM0MoeJo9MHkloHt2Lyoqr6OJQqCLXo1AdxqerdYHG3Oaf_OCRE-LPELJtskd63MNnBLh4ZzJAG79JbcagWFo-pPUaMyHYGYfBnQXJsZtukbSS85Kaim00uN2_zrsBqvOWKAhs1Fnwe-7WLpsv23Xok0TyoFbRJ9Qr6OTr_wNSfX3e-_HLVakbB-At5dhmFnTVox2GIqN-G0A35tgRk1rsLB1g-ucI_f5rSuEe6mu79MT3tFOzLZJL6GUwnya6LoupobIKZh3XU8JjBwpWn48czZeLgCtXOUeGFxi-2lsMERRfWY6QL4ejvkmDAi0XkGPp8jzyL-GWvh1h2gM4oToseVn5Xh8QGl6Mr-Vvnbl3VG8YhbU_W00

..     Digital Credential Lifecycle Management.

Un Utente, attraverso l'Istanza del Wallet, è in grado di acquisire una nuova Credenziale (**Credential Acquisition**) eseguendo il processo **PID/(Q)EAA ISS**. Questo DEVE risultare nella memorizzazione di una
Credenziale nello stato **Issued/Valid**, ed eliminarla quando non è più necessaria o è **Expired/Revoked** (**Credential Deletion**).
Fino alla **Credential Deletion**, una Credenziale può essere presentata alle Relying Party, questa operazione non influenzerà il suo ciclo di vita.

Un Fornitore di Credenziale invece è responsabile per:

  * **Generazione della Credenziale**: la Credenziale viene generata come conseguenza di una richiesta di emissione e DEVE essere aggiunta allo storage locale del Fornitore di Credenziale dopo l'emissione riuscita.
  * **Revoca/Sospensione/Riattivazione della Credenziale** (**PID/(Q)EAA REV** e **(Q)EAA SUSP/UNSUSP**): per motivi tecnici di sicurezza o attivati da entità esterne (ad esempio, Utenti e Fonti Autentiche) lo stato della Credenziale DEVE essere aggiornato localmente.
  * **Eliminazione dei Dati**: dopo aver raggiunto lo stato **Expired**, e in base alle politiche di conservazione del Fornitore di Credenziale, le Credenziali DEVONO essere rimosse dallo storage locale del Fornitore di Credenziale.

Revoca e Sospensione delle Credenziali
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Questa sezione descrive i flussi per richiedere un aggiornamento dello stato di una Credenziale (cioè revoca o sospensione), le entità coinvolte e i meccanismi di validazione per le Credenziali nel sistema IT-Wallet.

Come evidenziato nella Sezione :ref:`credential-revocation:Ciclo di vita delle Credenziali`, il ciclo di vita di una Credenziale è influenzato da:

  - Il ciclo di vita della sua Istanza del Wallet
  - La validità degli Attributi gestiti dalle Fonti Autentiche
  - Solo per i PID, lo stato dell'Identità Digitale utilizzata per l'autenticazione dell'Utente

Fattori esterni relativi all'utente possono anche influenzare il ciclo di vita di una Credenziale, come:

  - Richiesta esplicita dal titolare della Credenziale
  - Morte dell'Utente
  - Attività illegali

Entità Coinvolte
^^^^^^^^^^^^^^^^

Mentre il Fornitore di Credenziale DEVE gestire direttamente lo stato di validità delle Credenziali che ha emesso, altri attori POSSONO attivare il processo di revoca/sospensione della Credenziale:

  - Utenti, attraverso:
  
    - La loro Istanza del Wallet
    - Servizio web fornito dal Fornitore di Credenziale
  
  - La Fonte Autentica quando gli attributi della Credenziale vengono aggiornati o cambiano stato di validità
  - Il Fornitore di Wallet quando revoca un'Istanza del Wallet
  - Il Gestore di Identità DIgitale se l'Identità Digitale utilizzata per il rilascio del PID è stata rubata o compromessa
  - Autorità legali o l'Organo di Vigilanza in caso di attività illegali comprovate

La seguente figura mostra un diagramma delle relazioni tra entità relative al flusso di aggiornamento dello stato.

.. _fig_entity-relation-credential-revocation:
.. plantuml:: plantuml/credential-revocation-entities.puml
    :width: 99%
    :alt: La figura illustra le Entità coinvolte nel Flusso di Revoca delle Credenziali.
    :caption: `Entità coinvolte nel Flusso di Revoca delle Credenziali. <https://www.plantuml.com/plantuml/svg/RPJDZjCm4CVlUOgX5ne9QIzxH6ZPR1150gfs4U8KkV5GHgHsv8-KW7XtngcJXhYLAjUJcVd_vYDzi4uOvqyDbCgH8xH0gjDDXv9_G65G8ZyG3UomqxLmf1MyQ_GvUq6gRhn4U5tStnNtLQ5FhLRi_2RBtc-Uoch_NExApy_VjkKwpx8j6glLsbiqhs3rXOyLduDe3_giI1r1qf4SIzMJgbrnwAFsIWhJhy-YQT1LjhSEJnpzTRZ3VhYlSlYJ0NycaD6V51UfQhn6RA8b88JlHw744Iq4kfSMdY97CUUudRirkYF9DOsfjz4mfevt2mjf44h26G_0aXtL61J-PjbLG7Zt8uZNbTNU3FHlHnFi1rEY4TeAmZb31-_uxZHm16oizMW6nLEiD9WxqP0CxMSYvmF0f5wLlou4sj1lbDL1opu0J9PfNKQ6lMz38LQR_d5m_k0brM5nOf1ZsqRYPU1Jb_9voJHmSh9huoFxg3BSx7-LfCCQ7iV1s6MFPt9ntQhhkh52ccxKBhHoWfITDpWefMtCiXqsSTMNUmAhy2BzH5YkOfu6pHRt2Tc0SwgvVspSbFj64Va5Ai59fMxpsIYO-4_QdxIZx_sjUSW0Jrg552b3cc8X3MRwwubb92z7ccCs9DzA4SurJyhpgSroPdaaIpP-cNN3OCUmqxMZxhB_aIXwfZirTVHkxssBIdB40n_-rFm3>`_


.. .. figure:: ../../images/entity-involved-credential-revocation.svg
..   :figwidth: 100%
..   :align: center
..   :target: https://www.plantuml.com/plantuml/svg/RPFFRjGm4CRlUOfXBsmasbmuSIhTHc8HXLMt5U8KUMEpjN3io1xl4X3lpjXrcYZUI9NhgUVxVlEdDmwPHT-fedWZTQiy5_2CsBiFLMNP-VeeyTaVl1EsDHg5nklMT5Mlc0v9LmwvaeTgy_vg5q9Fzr-gZZaKbaBDndIzqI6dZmQVjdTrit-i7-flZpzszReiYfsmpkXrq7y7goSwLdJM6YKEOCvQwYDmIH1CGMi59p79b5jHwgtncZCxhCzCAO6D6yYte-plyGxxU5-LyBS0-bvXnlTIEsIw5LF6DaK2GlYvPveTXOD0zzR1NUBOp3akQ_VMd2IdcaRfNGgCqkdkO64DJ7CuYmEGvKcs8ZZyAuh9W7by3kPjuuotaVxZ689z36KUeQt04AqyUAGx6g0Cs3hdXOsENQeqX4zCIHxQJqJe2M1oR-hVBmJ6oZ-2DmV3XmWmHY1EJWetCknz7mfnnWwtyV5dpsKhcOAKX1JRSX47FdMfd9Si8oU9JOrFxADBlBbP9PU65V-S1kEMFPxPfNLhfdKZXrnkzDuOZKngDszmSChRM1GFGgLLN-u9h1x4oVmIi5p5SfQKB-wTe82OKytVXyRDjIyKKRv0PJYvrMK-bmoNxoVlhmRbp-7IF7Y0bqO7YPmXarXQWoMYbYM5897zSsGQyo7vdhDmhcbIdavZbpCh4rcsyKlLBO4TmqwtA4zn_qUYz3BVgTUELdllUg5vo0ZV3VtkE_KV

..   Entities involved in Credential Revocation Flow


Flussi di Aggiornamento dello Stato
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Questa sezione descrive i principali flussi per la gestione degli Aggiornamenti di Stato delle Credenziali da parte del Fornitore di Credenziale, in particolare l'Aggiornamento di Stato:

  - relativo all'Utente;
  - attivato da un'Istanza del Wallet;
  - attivato da un Fornitore di Wallet;
  - attivato da una Fonte Autentica.

.. note::
  I Flussi dettagliati di Aggiornamento dello Stato per i Gestori di Identità DIgitale, le autorità legali e l'Organo di Vigilanza saranno trattati nelle versioni future della specifica tecnica.

Aggiornamento dello Stato relativo all'Utente
"""""""""""""""""""""""""""""""""""""""""""""

Gli Utenti POSSONO modificare lo stato di validità della loro Credenziale:

  1. Eliminando la Credenziale dalla loro Istanza del Wallet: l'Istanza del Wallet DEVE utilizzare l'Endpoint di Notifica fornito dal Fornitore di Credenziale come descritto nella Sezione :ref:`credential-revocation:Aggiornamento dello Stato da parte dell'Istanza del Wallet`.
  2. Utilizzando il portale web del Fornitore di Credenziale:

    a. Gli Utenti POSSONO accedere a un'area sicura con almeno lo stesso Livello di Garanzia utilizzato durante la fase di emissione.
    b. Il Fornitore di Credenziale DEVE consentire agli Utenti di:

      - Visualizzare tutte le loro Credenziali contenute nel database del Fornitore di Credenziale.
      - Verificare l'autenticità dei dati.
      - Visualizzare e aggiornare lo stato di validità (revocare le loro Credenziali e, se supportato dal Fornitore di Credenziale, sospenderle).

.. note::
  Se l'Utente attiva un'altra Istanza del Wallet dallo stesso Fornitore di Wallet e utilizzando la stessa Soluzione Wallet e ottiene un nuovo PID, il PID precedente DEVE essere revocato e l'Istanza del Wallet precedente DEVE passare allo stato operativo.

In caso di morte dell'Utente, i Fornitori di Credenziale e il Fornitore di Wallet DEVONO garantire che le Credenziali e le Istanze del Wallet possedute dall'Utente siano revocate.
La morte dell'Utente attiva un cambiamento nello stato di validità degli attributi di identificazione dell'Utente contenuti nel registro pubblico (ANPR). La morte dell'Utente DEVE produrre la revoca del PID. Pertanto, la Fonte Autentica del PID (ANPR) DEVE notificare al Fornitore di Attestati Elettronici di Dati di Identificazione Personale che gli attributi dell'Utente non sono più validi a causa della morte dell'Utente. La Fonte Autentica e il Fornitore di Attestati Elettronici di Dati di Identificazione Personale DEVONO utilizzare i meccanismi forniti nella Sezione :ref:`credential-revocation:Aggiornamento dello Stato da parte delle Fonti Autentiche`.

.. note::
  Le versioni future di questa specifica tecnica definiranno come le informazioni vengono propagate ai Fornitori di Attestati Elettronici di Attributi (Q)EAA e ai Fornitori di Wallet, in conformità con la normativa nazionale. Inoltre, le procedure automatizzate per la revoca delle Credenziali a causa di attività illegali saranno definite nelle specifiche future.

Aggiornamento dello Stato da parte dell'Istanza del Wallet
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Quando l'Utente elimina una Credenziale dall'Istanza del Wallet, l'Istanza del Wallet DEVE notificare questo evento al Fornitore di Credenziale e il Fornitore di Credenziale DEVE revocare la Credenziale. Per notificare questo evento, l'Istanza del Wallet DEVE utilizzare l'*Endpoint di Notifica* descritto nella Sezione :ref:`credential-issuance-endpoint:Endpoint di notifica` utilizzando il parametro ``event`` impostato con il valore ``credential_deleted``.

Quando la Credenziale revocata è il PID, il Fornitore di Credenziale DEVE inviare una notifica di questo evento all'Utente entro 24 ore.
Per qualsiasi altra Credenziale diversa dal PID, il Fornitore di Credenziale DOVREBBE inviare una notifica di questo evento all'Utente. La notifica all'Utente potrebbe essere implementata in diversi modi, come l'utilizzo dell'indirizzo email dell'Utente, del numero di telefono o di qualsiasi altro canale di comunicazione verificato e sicuro, e DEVE includere tutte le informazioni sullo stato di revoca della Credenziale. Il metodo utilizzato per la notifica all'Utente è fuori dall'ambito dell'attuale profilo di implementazione tecnica. Quando avviene la revoca, il Fornitore di Credenziale DEVE aggiornare lo stato della Credenziale di conseguenza. Quando la Risposta di Notifica inviata dal Fornitore di Credenziale viene ricevuta con successo dall'Istanza del Wallet, l'Istanza del Wallet DEVE eliminare la Credenziale.

Aggiornamento dello Stato da parte dei Fornitori di Wallet
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

In aggiunta a quanto già definito in :ref:`credential-revocation:Ciclo di vita delle Credenziali`, il Fornitore di Credenziale DEVE fornire un servizio web (endpoint di Revoca dell'Istanza del Wallet) definito utilizzando PDND, come specificato nella Sezione :ref:`credential-issuer-endpoint:Catalogo e-Service PDND del Credential Issuer`.
Il Fornitore di Wallet che per qualsiasi motivo revoca un'Istanza del Wallet DEVE inviare una notifica ai Fornitori di Credenziale utilizzando questo endpoint.

Aggiornamento dello Stato da parte delle Fonti Autentiche
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Le Fonti Autentiche gestiscono gli attributi separatamente dalle Credenziali, che verificano l'autenticità come i documenti fisici. Perdere un documento fisico non significa perdere i privilegi che rappresenta; significa solo che l'Utente non può provarli. Tuttavia, se un Utente perde i privilegi a causa di un'infrazione grave, la Fonte Autentica revocherà gli attributi correlati. In tali casi, quando gli attributi di un Utente vengono aggiornati, le Fonti Autentiche DEVONO notificare ai Fornitori di Credenziale di aggiornare lo stato di validità di qualsiasi Credenziale contenente tali attributi.

I Fornitori di Credenziale DEVONO fornire un servizio web disponibile tramite PDND per la notifica dell'aggiornamento delle Credenziali e dello stato di validità come definito nella Sezione :ref:`credential-issuer-endpoint:Catalogo e-Service PDND del Credential Issuer`. Per il flusso del protocollo, fare riferimento alla Sezione :ref:`e-service-pdnd:e-Service PDND`.
Le Fonti Autentiche DEVONO utilizzare questo servizio di notifica nei seguenti casi:

  - Il valore di uno o più Attributi contenuti nel database della Fonte Autentica è cambiato.
  - Lo stato di validità degli Attributi è aggiornato (revoca o sospensione).


Meccanismi di Verifica della Validità
-------------------------------------

Per la verifica dello stato di validità di una Credenziale a lunga durata, l'OAuth Status List (`TOKEN-STATUS-LIST`_) DEVE essere supportato sia per lo scenario remoto che per quello di prossimità. Nello scenario remoto, il Fornitore di Credenziale, l'Istanza del Wallet e la Relying Party POSSONO supportare OAuth Status Assertions (`OAUTH-STATUS-ASSERTION`_). La seguente tabella riassume i meccanismi di revoca richiesti per verificare lo stato delle Credenziali a lunga durata.

.. _table_revocation_mechanisms:
.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Flusso**
    - **Meccanismo di Revoca**
    - **Riferimento**
  * - Remoto
    -
      - [OPZIONALE] OAuth Status Assertion,
      - [RICHIESTO] OAuth Status Lists.
    - `OAUTH-STATUS-ASSERTION`_, `TOKEN-STATUS-LIST`_.
  * - Prossimità
    - [RICHIESTO] OAuth Status Lists.
    - `TOKEN-STATUS-LIST`_.

OAuth Status Assertions
^^^^^^^^^^^^^^^^^^^^^^^

Una Status Assertion è un documento firmato che serve come prova dello stato di validità corrente di una Credenziale. Il Fornitore di Credenziale fornisce queste asserzioni ai Titolari che possono presentarle ai Verificatori insieme alle Credenziali corrispondenti.

Le Status Assertions hanno le seguenti caratteristiche:

  - emissione automatizzata, poiché l'autenticazione dell'Utente non è richiesta per la fornitura della Status Assertion;
  - verifica dello stato di validità della Credenziale sia in scenari online che offline;
  - preservazione della privacy, secondo le seguenti evidenze:

    - il Verificatore può controllare la validità della Credenziale durante la fase di presentazione. Non è in grado di controllare la validità di una determinata Credenziale relativa all'Utente nel tempo e al di fuori dell'ambito dell'autenticazione dell'Utente;
    - il Fornitore di Credenziale non è in grado di sapere a quale Verificatore verrà presentata la Credenziale o la Status Assertion;
    - non rivela alcuna informazione sugli Utenti o sul contenuto delle loro Credenziali.

  - DEVE avere un periodo di validità non superiore a 24 ore.

.. note::
  Questa specifica supporta solo il formato JWT e la Status Assertion utilizza il claim ``credential_status_type`` invece di ``credential_status_validity``.

Le seguenti sezioni descrivono come funziona il meccanismo di validazione delle Credenziali attraverso le sue fasi chiave.


Gestione dello Stato delle Credenziali con OAuth Status Assertion
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

I Fornitori di Credenziale, una volta che una Credenziale è stata generata e rilasciata con successo, DEVONO:

  - Memorizzarla localmente con il set minimo di dati necessari per gestire il suo ciclo di vita, incluso lo stato di validità di quella Credenziale;
  - Includere un algoritmo di hash specificato nella Credenziale utilizzando il claim ``credential_hash_alg`` all'interno del membro JSON ``status_assertion`` del claim status

Inoltre, i Fornitori di Credenziale DEVONO aggiungere i seguenti parametri nei loro Metadati:

  - ``status_assertion_endpoint``
  - ``credential_hash_alg_supported``


Verifica dello Stato delle Credenziali da parte dell'Istanza del Wallet
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Un'Istanza del Wallet DEVE controllare periodicamente lo stato di validità della Credenziale che è memorizzata in essa, richiedendo una Status Assertion per ogni Credenziale. In questo caso, l'Istanza del Wallet DEVE inviare una *Richiesta di Status Assertion* al Fornitore di Credenziale secondo la "Specifica OAuth Status Assertion" (vedere `OAUTH-STATUS-ASSERTION`_ per maggiori dettagli) ed è illustrato nel seguente diagramma.

.. _fig_entity-relation-credential-revocation-2:
.. plantuml:: plantuml/status-assertion-flow.puml
    :width: 80%
    :alt: La figura illustra il Flusso di Status Assertion.
    :caption: `Flusso di Status Assertion. <https://www.plantuml.com/plantuml/svg/TOv1IyD048Nl-oiUYyUQ7z23L4Im9uiDU50fOpk7XSqapioIl--IQ27GdERmllU-sPcJUkboeEAzbEwRDGoadivf8774TygP7Nkff9mvWWnZMZ9FoXSMJvInDoki4vL261Fk7v2sEBmUMnoTl1WUpRYMUy5BsnxmnZ-5pV4fY3OH9_edJZg75h75HoM0ktdbEl9NtqnXqpJrVeKGghYQnwfUizhGY_6QTaujhcjdukhTtCIULNjT_hPZkPGk_m80>`_


.. .. figure:: ../../images/High-Level-Flow-Status-Assertion-Request.svg
..     :figwidth: 100%
..     :align: center
..     :target: https://www.plantuml.com/plantuml/svg/TOv1IyD048Nl-oiUYyUQ7z23L4Im9uiDU50fOpk7XSqapioIl--IQ27GdERmllU-sPcJUkboeEAzbEwRDGoadivf8774TygP7Nkff9mvWWnZMZ9FoXSMJvInDoki4vL261Fk7v2sEBmUMnoTl1WUpRYMUy5BsnxmnZ-5pV4fY3OH9_edJZg75h75HoM0ktdbEl9NtqnXqpJrVeKGghYQnwfUizhGY_6QTaujhcjdukhTtCIULNjT_hPZkPGk_m80

..     Status Assertion Flow


**Passo 1 (Richiesta di Status Assertion)**: L'Istanza del Wallet invia la Richiesta di Status Assertion al Fornitore di Credenziale, dove:

  - La richiesta DEVE contenere il valore hash codificato in base64url della parte firmata dal Fornitore di Credenziale, come il JWT firmato dal Fornitore di Credenziale utilizzando :ref:`credential-data-model:Formato Credenziale SD-JWT-VC`, o il Mobile Security Object utilizzando :ref:`credential-data-model:Formato Credenziale mdoc-CBOR`, per cui viene richiesta la Status Assertion, e avvolto in un oggetto di Richiesta di Status Assertion firmato.
  - L'oggetto di Richiesta di Status Assertion DEVE essere firmato con la chiave privata corrispondente al claim di conferma assegnato dal Fornitore di Credenziale e contenuto nella Credenziale.

La richiesta HTTP di Status Assertion può essere inviata a un singolo Fornitore di Credenziale riguardante più Credenziali, e DEVE contenere un oggetto JSON con il membro `status_assertion_requests` come descritto nella Sezione :ref:`credential-revocation:Richiesta HTTP di Status Assertion`.

Il Fornitore di Credenziale che riceve l'oggetto di Richiesta di Status Assertion DEVE:

  - validare che l'Istanza del Wallet che effettua la richiesta sia autorizzata a richiedere Status Assertions. Se si verificano errori durante questo controllo, il Fornitore di Credenziale DEVE fornire una Risposta di Errore di Status Assertion secondo la Sezione :ref:`credential-revocation:Risposta HTTP di Status Assertion`;
  - verificare la conformità di tutti gli elementi nell'oggetto `status_assertion_requests` utilizzando il metodo di conferma contenuto nella Credenziale a cui si riferisce l'oggetto di Richiesta di Status Assertion. In caso di errori, DEVE essere fornita una Risposta di Errore di Status Assertion (vedere la Sezione :ref:`credential-revocation:Risposta HTTP di Status Assertion`);
  - verificare che sia il legittimo Fornitore di Credenziale della Credenziale a cui si riferisce ciascun oggetto di Richiesta di Status Assertion;
  - controllare lo stato di validità per le Credenziali richieste;
  - creare la corrispondente Status Assertion.


**Passo 2 (Risposta di Status Assertion)**: Il *status_assertion_responses* DEVE essere un array di stringhe contenente gli Oggetti JSON *StatusAssertionResponse* e/o *StatusAssertionErrors* relativi alla richiesta effettuata dall'Istanza del Wallet.

L'Istanza del Wallet DEVE:

  - validare la Risposta HTTP di Status Assertion;
  - estrarre e validare le firme di ciascun Oggetto JSON all'interno dell'Array JSON *status_assertion_responses*;
  - presentare una Status Assertion valida a un Verificatore che la richiede per la verifica dello stato di una Credenziale (vedere la Sezione seguente per maggiori dettagli);
  - informare l'Utente in caso di aggiornamento dello stato di validità di una Credenziale.

.. note::
  L'Oggetto JSON Status Assertion Errors PUÒ avere il *parametro dell'header alg* impostato su *none*. Se il Fornitore di Credenziale firma gli Status Assertion Errors, l'Istanza del Wallet DEVE validare la firma. Inoltre, gli Status Assertion Errors NON DEVONO essere presentati ai Verificatori.

I dettagli tecnici sulla Risposta HTTP di Status Assertion sono forniti nella Sezione :ref:`credential-revocation:Risposta HTTP di Status Assertion`.

Richiesta HTTP di Status Assertion
..................................

L'*endpoint di Status Assertion* DEVE essere fornito dal Fornitore di Credenziale nei suoi Metadati.
Le richieste all'*endpoint di Status Assertion* DEVONO essere HTTP con metodo POST, utilizzando i parametri obbligatori elencati di seguito all'interno del corpo del messaggio della richiesta HTTP. Questi DEVONO essere codificati nel formato ``application/json``.

.. _table_revocation_request_params:
.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Claim**
    - **Descrizione**
    - **Riferimento**
  * - **status_assertion_requests**
    - DEVE essere un array di stringhe, dove ciascuna rappresenta un *oggetto di Richiesta di Status Assertion*. Ogni elemento DEVE contenere un JWT firmato, codificato come una serie di valori codificati in base64url (alcuni dei quali possono essere stringhe vuote) separati da caratteri punto ('.'), come prova crittografica del possesso della Credenziale per cui viene richiesta la Status Assertion, in conformità con la Richiesta di Status Assertion descritta nella Sezione 7 di `OAUTH-STATUS-ASSERTION`_. Vedere la :ref:`Tabella <table_status_assertion_req_obj>` sottostante per maggiori dettagli.
    - Questa Specifica.

Di seguito un esempio non normativo che rappresenta un array di Richiesta di Status Assertion con oggetti di Richiesta di Status Assertion in formato JWT.

.. code::

  POST /status HTTP/1.1
  Host: issuer.example.org
  Content-Type: application/json

	{
		"status_assertion_requests" : [
      $status_assertion_request,
      $status_assertion_request,
      ...
    ]
	}

L'**oggetto di Richiesta di Status Assertion** DEVE essere un JWT che DEVE contenere i parametri (Header e Payload) nella seguente tabella.

.. _table_status_assertion_req_obj:
.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Header**
    - **Descrizione**
    - **Riferimento**
  * - **typ**
    - DEVE essere impostato su ``status-assertion-request+jwt``.
    - :rfc:`7516#section-4.1.1`.
  * - **alg**
    - Un identificatore di algoritmo di firma digitale come per il registro IANA "JSON Web Signature and Encryption Algorithms". DEVE essere uno degli algoritmi supportati elencati nella Sezione :ref:`algorithms:Algoritmi Crittografici` e NON DEVE essere impostato su ``none`` o qualsiasi identificatore di algoritmo simmetrico (MAC).
    - :rfc:`7516#section-4.1.1`.


.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Payload**
    - **Descrizione**
    - **Riferimento**
  * - **iss**
    - Impronta digitale del JWK nel parametro ``cnf`` dell'Attestato di Wallet.
    - :rfc:`9126` e :rfc:`7519`.
  * - **aud**
    - DEVE essere impostato sulla stringa URL dell'endpoint di Status Assertion del Fornitore di Credenziale.
    - :rfc:`9126` e :rfc:`7519`.
  * - **exp**
    - Timestamp UNIX con il tempo di scadenza del JWT. DEVE essere maggiore del valore impostato per `iat`.
    - :rfc:`9126` e :rfc:`7519`.
  * - **iat**
    - Timestamp UNIX con il tempo di emissione del JWT.
    - :rfc:`9126` e :rfc:`7519`.
  * - **jti**
    - Identificatore univoco per il JWT di prova di possesso. Il valore DOVREBBE essere impostato utilizzando un valore *UUID v4* secondo [:rfc:`4122`].
    - :rfc:`7519#section-4.1.7`.
  * - **credential_hash**
    - DEVE contenere il valore hash della parte firmata dal Fornitore di Credenziale della Credenziale a cui è legata la Status Assertion.
    - `OAUTH-STATUS-ASSERTION`_.
  * - **credential_hash_alg**
    - DEVE contenere l'Algoritmo utilizzato per l'hashing della Credenziale. Il valore DOVREBBE essere impostato su `sha-256`.
    - `OAUTH-STATUS-ASSERTION`_.

Di seguito, viene fornito un esempio non normativo di un singolo *oggetto di Richiesta di Status Assertion* con header e payload JWT decodificati e senza firma per una migliore leggibilità:

.. code-block:: json

  {
    "alg": "ES256",
    "typ": "status-assertion-request+jwt"
  }
  
.. code-block:: json

  {
    "iss": "0b434530-e151-4c40-98b7-74c75a5ef760",
    "aud": "https://pid-provider.example.org/status",
    "iat": 1698744039,
    "exp": 1698744139,
    "jti": "6f204f7e-e453-4dfd-814e-9d155319408c",
    "credential_hash": "$Issuer-Signed-JWT-Hash",
    "credential_hash_alg": "sha-256"
  }

Risposta HTTP di Status Assertion
.................................

In caso di validazione della Richiesta di Status Assertion riuscita, il *Fornitore di Credenziale* DEVE restituire una risposta HTTP con il codice di stato impostato su *200 OK*. Se il *Fornitore di Credenziale* è in grado di fornire una Status Assertion valida per una Credenziale richiesta, la risposta DEVE contenere un oggetto Status Assertion all'interno di un Array JSON. Altrimenti, un Status Assertion Errors relativo a quella Credenziale DEVE essere incluso nell'Array JSON di Risposta come voce.

Se la Richiesta HTTP di Status Assertion fallisce (ad esempio richiesta non valida, indisponibilità del server, ecc.), un Codice di Stato di Errore HTTP DEVE essere fornito all'interno della Risposta di Status Assertion.

Nella seguente tabella sono elencati i Codici di Stato HTTP che DEVONO essere supportati:

.. list-table::
  :class: longtable
  :widths: 20 20 60
  :header-rows: 1

  * - **Codice di Stato**
    - **Corpo**
    - **Descrizione**
  * - *200 Ok*
    - Risposta di Revoca
    - La Risposta di Revoca è stata creata con successo.
  * - *400 Bad Request*
    - Codice di errore e descrizione
    - Il Fornitore di Credenziale non può soddisfare la richiesta a causa di parametri non validi.
  * - *500 Internal Server Error*
    -
    - Il Fornitore di Credenziale ha riscontrato un problema interno. (:rfc:`6749#section-5.2`).
  * - *503 Service Unavailable*
    -
    - Il Fornitore di Credenziale è temporaneamente non disponibile. (:rfc:`6749#section-5.2`).

La risposta HTTP DEVE:

- Includere un oggetto JSON con un membro denominato `status_assertion_responses`. DEVE essere un array di stringhe, dove ciascuna rappresenta un *oggetto di Risposta di Status Assertion*. Ogni elemento DEVE contenere un JWT firmato, codificato come una serie di valori codificati in base64url (alcuni dei quali possono essere stringhe vuote) separati da caratteri punto ('.') . L'*oggetto di Risposta di Status Assertion* DEVE contenere una Risposta di Status Assertion e un Errore di Status Assertion in analogia con le Sezioni 8 e 9 di `OAUTH-STATUS-ASSERTION`_ per maggiori dettagli.

- Essere codificata nel formato ``application/json``.

Un esempio non normativo di una Risposta HTTP di Status Assertion è fornito di seguito.

.. code::

    HTTP/1.1 200 Ok
    Content-Type: application/json
    {
      "status_assertion_responses": [
        $status_assertion_response,
        $status_assertion_response,
        ...
      ]
    }

La Status Assertion DEVE contenere i parametri e i claim definiti di seguito

.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Header**
    - **Descrizione**
    - **Riferimento**
  * - **alg**
    - Un identificatore di algoritmo di firma digitale come per il registro IANA "JSON Web Signature and Encryption Algorithms". DEVE essere uno degli algoritmi supportati nella Sezione :ref:`Cryptographic Algorithms <algorithms:Algoritmi Crittografici>` e NON DEVE essere impostato su ``none`` o su un identificatore di algoritmo simmetrico (MAC).
    - [:rfc:`7515`], [:rfc:`7517`].
  * - **typ**
    - DEVE essere impostato su `status-assertion+jwt`.
    - [:rfc:`7515`], [:rfc:`7517`], `OAUTH-STATUS-ASSERTION`_.
  * - **kid**
    - Identificatore univoco del JWK del Fornitore di Credenziale. È RICHIESTO quando ``x5c`` non viene utilizzato.
    - [:rfc:`7515`], `OAUTH-STATUS-ASSERTION`_.
  * - **x5c**
    -  Catena di certificati X.509 relativa al Fornitore di Credenziale. È RICHIESTO quando ``kid`` non viene utilizzato.
    - [:rfc:`7515`], `OAUTH-STATUS-ASSERTION`_.

.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Payload**
    - **Descrizione**
    - **Riferimento**
  * - **iss**
    - DEVE essere impostato sull'identificatore del Fornitore di Credenziale.
    - :rfc:`9126` e :rfc:`7519`.
  * - **iat**
    - Timestamp UNIX con il tempo di emissione del JWT.
    - :rfc:`9126` e :rfc:`7519`.
  * - **exp**
    - Timestamp UNIX con il tempo di scadenza del JWT. DEVE essere maggiore del valore impostato per `iat`.
    - :rfc:`9126` e :rfc:`7519`.
  * - **credential_hash**
    - Valore hash della Credenziale a cui è legata la Status Assertion.
    - `OAUTH-STATUS-ASSERTION`_.
  * - **credential_hash_alg**
    - L'Algoritmo utilizzato per l'hashing della Credenziale a cui è legata la Status Assertion. Il valore DOVREBBE essere impostato su ``sha-256``.
    - `OAUTH-STATUS-ASSERTION`_.
  * - **credential_status_type** [#]_
    - Valore numerico che indica la validità della Credenziale collegata alla Status Assertion descrivendo il suo stato, modalità, condizione o fase. Tutti i valori presi dal registro IANA "OAuth Status Types" per i valori di Status List (vedere la Sezione 7 di `TOKEN-STATUS-LIST`_) POSSONO essere supportati. I valori da ``0x00`` a ``0x02`` DEVONO essere supportati con il seguente significato:

      - ``0x00 - VALID``: Lo stato della Credenziale è valido, corretto o legale.
      - ``0x01 - INVALID``: Lo stato della Credenziale è revocato, annullato, ritirato, richiamato o cancellato. Questo stato è irreversibile.
      - ``0x02 - SUSPENDED``: Lo stato della Credenziale è temporaneamente non valido, sospeso, privato del privilegio. Questo stato è reversibile.

    - Questa Specifica, `TOKEN-STATUS-LIST`_ .
  * - **credential_status_detail**
    - RICHIESTO solo se **credential_status_type** non è impostato su `0x00`. Oggetto contenente informazioni dettagliate sullo stato della Credenziale. Contiene:

        - **state**: (RICHIESTO). Valore stringa dello stato della Credenziale. Viene utilizzato per trasmettere una rappresentazione più granulare dello stato di una Credenziale, ad esempio "revoked", "annulled", "debarred", ecc. o in caso di stati di Credenziale specifici dell'applicazione. Il Fornitore di Credenziale DEVE fornire un elenco di stati supportati per la Credenziale emessa nei Metadati del Fornitore di Credenziale.
        - **description**: (RICHIESTO). Stringa contenente la descrizione dello stato della Credenziale.
    - `OAUTH-STATUS-ASSERTION`_.
  * - **cnf**
    - Oggetto JSON contenente metodi di conferma. Il sotto-membro contenuto all'interno del membro `cnf`, come `jwk` per JWT, DEVE corrispondere a quello fornito all'interno della relativa Credenziale. Altri metodi di conferma possono essere utilizzati quando la Credenziale di riferimento li supporta, in conformità con gli standard pertinenti.
    - Sezione 3.1 di :rfc:`7800` e Sezione 3.1 di :rfc:`8747`.

.. warning::
  .. [#] Questa specifica utilizza ``credential_status_type`` invece di ``credential_status_validity`` attualmente supportato in `OAUTH-STATUS-ASSERTION`_ poiché il valore è semanticamente un tipo di stato e non un booleano.

Di seguito un esempio non normativo di un oggetto di Risposta di Status Assertion in formato JWT, con gli header e il payload rappresentati in JSON e senza applicare la firma.

.. code::

  {
    "alg": "ES256",
    "typ": "status-assertion+jwt",
    "kid": "Issuer-JWK-KID"
  }
 .
  {
    "iss": "https://issuer.example.org",
    "jti": "6f204f7e-e453-4dfd-814e-9d155319408c"
    "credential_hash": $CREDENTIAL-HASH,
    "credential_hash_alg": "sha-256",
    "credential_status_type": 0x01,
    "credential_status_detail": {
      "state": "revoked",
      "description": "The Credential is no longer usable as it has been revoked. This state is irreversible"
    },
    "cnf": {
      "jwk": {
        "kty": "EC",
        "crv": "P-256",
        "x": "_2ySUmWFjwmraNlo15r6dIBXerVdy_NpJuwAKJMFdoc",
        "y": "MV3C88MhhEMba6oyMBWuGeB3dKHP4YADJmGyJwwILsk"
      }
    }
  }

L'oggetto Status Assertion Error DEVE contenere i seguenti claim:

.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Header**
    - **Descrizione**
    - **Riferimento**
  * - **alg**
    - Un identificatore di algoritmo di firma digitale come per il registro IANA "JSON Web Signature and Encryption Algorithms". DEVE essere uno degli algoritmi supportati nella Sezione :ref:`Cryptographic Algorithms <algorithms:Algoritmi Crittografici>` e NON DEVE essere impostato su ``none`` o su un identificatore di algoritmo simmetrico (MAC).
    - Sezione 4.1.1 di [:rfc:`7516`].
  * - **typ**
    - DEVE essere impostato su `status-assertion+jwt`.
    - Sezione 4.1.11 di [:rfc:`7516`].

.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Payload**
    - **Descrizione**
    - **Riferimento**
  * - **iss**
    - DEVE essere impostato sull'identificatore del Fornitore di Credenziale.
    - :rfc:`9126` e :rfc:`7519`.
  * - **jti**
    - Identificatore univoco per il JWT.
    - :rfc:`9126` e :rfc:`7519`.
  * - **credential_hash**
    - Valore hash della Credenziale a cui è legato lo Status Assertion Error, DEVE corrispondere a quello contenuto nella Richiesta di Status Assertion.
    - `OAUTH-STATUS-ASSERTION`_.
  * - **credential_hash_alg**
    - L'Algoritmo utilizzato per l'hashing della Credenziale a cui è legato lo Status Assertion Error, DEVE corrispondere a quello contenuto nella Richiesta di Status Assertion. Il valore DOVREBBE essere impostato su ``sha-256``.
    - `OAUTH-STATUS-ASSERTION`_.
  * - **error**
    - Il codice di errore, come registrato nella tabella sottostante.
    - Sezione 4.1.7 di :rfc:`7519`.
  * - **error_description**
    - Testo in forma leggibile dall'uomo che fornisce ulteriori dettagli per chiarire la natura dell'errore riscontrato.
    - Sezione 4.1.7 di :rfc:`7519`.

Gli errori sono destinati a fornire informazioni aggiuntive sul fallimento in modo che l'Utente possa essere informato e intraprendere l'azione appropriata.
Il claim `error` per l'oggetto Status Assertion Error DEVE essere impostato con uno dei valori definiti nella tabella sottostante, in aggiunta ai valori specificati in :rfc:`6749#section-5.2`:

.. list-table::
    :class: longtable
    :widths: 20 80
    :header-rows: 1

    * - **Codice di Errore**
      - **Descrizione**
    * - ``invalid_request``
      - La richiesta non è valida a causa della mancanza o dell'incorrettezza di uno o più parametri. (:rfc:`6749#section-5.2`).
    * - ``invalid_request_signature``
      - La validazione della firma della Richiesta di Revocation Assertion è fallita. Questo tipo di errore viene utilizzato quando la prova di possesso della Credenziale viene trovata non valida all'interno della Richiesta di Revocation Assertion. (Sezione 9.2 di `OAUTH-STATUS-ASSERTION`_).
    * - ``credential_not_found``
      - Il valore `credential_hash` fornito nella Richiesta di Revocation Assertion non corrisponde a nessuna Credenziale attiva. (Sezione 9.2 di `OAUTH-STATUS-ASSERTION`_).
    * - ``unsupported_hash_alg``
      - L'algoritmo di hash impostato in `credential_hash_alg` non è supportato. (Sezione 9.2 di `OAUTH-STATUS-ASSERTION`_).

Di seguito un esempio non normativo di un oggetto Revocation Assertion Error in formato JWT, con gli header e il payload rappresentati in JSON e senza applicare la firma.

.. code::

  {
    "alg": "ES256",
    "typ": "revocation-assertion-error+jwt",
    "kid": "Issuer-JWK-KID"
  }
  .
  {
    "iss": "https://issuer.example.org",
    "jti": "6f204f7e-e453-4dfd-814e-9d155319408c"
    "credential_hash": $CREDENTIAL-HASH,
    "credential_hash_alg": "sha-256",
    "error": "unsupported_hash_alg",
    "error_description": "The hash algorithm is not supported"
  }

Verifica dello Stato delle Credenziali da parte della Relying Party
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Durante il flusso di presentazione, se una Status Assertion relativa a una Credenziale è disponibile, l'Istanza del Wallet DEVE includerla insieme alla relativa Credenziale nell'Array JSON ``vp_token``.
Il Verificatore che vuole fare affidamento sul meccanismo fornito dalla Status Assertion DEVE estrarre la Status Assertion dall'Array ``vp_token`` e, in aggiunta ai controlli richiesti nel Flusso di Presentazione descritto nella Sezione :ref:`remote-flow:Flusso Remoto`, il Verificatore DEVE controllare la presenza del claim ``status.status_assertion`` nella Credenziale. Se vero, i Verificatori DEVONO:

  - validare la firma della Status Assertion;
  - decodificare la Status Assertion fornita nella presentazione, abbinando il parametro dell'header JWS typ impostato su ``status-assertion+jwt`` e cercando il valore ``credential_hash`` che corrisponde all'hash della parte firmata dal Fornitore di Credenziale della Credenziale utilizzando l'algoritmo di hashing configurato in ``status.status_assertion.credential_hash_alg``;
  - valutare la Status Assertion controllando i seguenti elementi:

    - il valore del claim ``iss`` DEVE corrispondere a quello nella Credenziale;
    - il valore del claim ``iat`` DEVE essere uguale o successivo al valore del claim ``iat`` nella Credenziale;
    - il valore ``exp`` DEVE essere successivo all'ora corrente;
    - il valore del claim ``nbf``, se presente, DEVE essere minore o uguale all'ora corrente;
    - l'Oggetto JSON ``cnf`` DEVE corrispondere a quello incluso nella relativa Credenziale;
    - i valori ``credential_status_type`` e ``credential_status_detail``.


OAuth Status Lists
------------------

Questa sezione definisce una struttura di dati Status List, che viene utilizzata per trasmettere informazioni riguardanti gli stati individuali di più Credenziali. Le Credenziali possono essere di qualsiasi formato, come SD-JWT o mdoc ISO/IEC 18013-5. Una Status List descrive lo stato delle Credenziali codificando la loro validità in un array di bit. A ciascuna Credenziale viene assegnato un indice durante l'emissione; questo indice rappresenta la sua posizione all'interno dell'array di bit. Il valore del bit o dei bit in questo indice corrisponde allo stato delle Credenziali. Una Status List viene fornita all'interno di un Token di Status List firmato crittograficamente in formato JWT. Per i dettagli, vedere `TOKEN-STATUS-LIST`_.

In questa specifica, i ruoli di Fornitore di Credenziale e Status Issuer (cioè, l'entità che emette il Token di Status List sulle informazioni di stato della Credenziale) coincidono, mentre lo Status Provider (cioè, l'entità che fornisce il Token di Status List su un endpoint pubblico) PUÒ essere il Fornitore di Credenziale stesso o un'altra entità.

Creazione delle Status Lists
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

 Il Fornitore di Credenziale DEVE

  - definire un numero di bit, k, (1, 2, 4 o 8) che rappresenta la quantità di bit utilizzati per descrivere lo stato di ciascuna Credenziale all'interno di questa Status List. Il Fornitore di Credenziale DEVE configurare il numero di bit. Ogni Credenziale avrà quindi 2^k (dove k è il numero di bit scelto) possibili stati.
  - creare un array di byte di dimensione = (quantità di Credenziali) * k / 8 o maggiore. A seconda di k, ogni byte nell'array corrisponde a 8/k stati (8 se k=1, 4 se k=2, 2 se k=1, o 1 se k=8). Ogni volta che viene emessa una Credenziale, il Fornitore di Credenziale la assegna a una posizione nell'array.
  - impostare i valori di stato per tutte le Credenziali emesse all'interno dell'array di byte. Lo stato di ciascuna Credenziale viene identificato utilizzando un indice che mappa a uno o più bit specifici all'interno dell'array di byte. L'indice inizia a contare da 0 e termina con (quantità di Credenziali) - 1 (essendo l'ultima voce valida). I bit all'interno di un array vengono contati dal bit meno significativo ("0") al bit più significativo ("7"). Tutti i bit dell'array di byte a un particolare indice sono impostati su un valore di stato.
  - comprimere l'array di byte utilizzando DEFLATE [:rfc:`1951`] con il formato dati ZLIB [:rfc:`1950`]. Si RACCOMANDA alle implementazioni di utilizzare il livello di compressione più alto disponibile.
  - rendere disponibile alle Relying Party e alle Istanze del Wallet un endpoint per richiedere le Status Lists.

 Il Fornitore di Credenziale DEVE utilizzare i seguenti valori per i possibili Stati delle Credenziali emesse:

  - 0x00 - ``VALID`` - La Credenziale è valida.
  - 0x01 - ``INVALID`` - La Credenziale è revocata.
  - 0x02 - ``SUSPENDED`` - La Credenziale è temporaneamente non valida, sospesa, privata del privilegio. Questo stato è reversibile.
  - 0x03 - ``UPDATE`` - I parametri dei metadati della Credenziale sono cambiati.
  - 0x04 - ``ATTRIBUTE_UPDATE`` - Gli attributi della Credenziale sono cambiati.

 Ad esempio, se sono possibili cinque stati per una certa Credenziale, allora k=4. Se il Fornitore di Credenziale crea un array per memorizzare gli stati di 6 Credenziali, i cui stati di validità sono 0, 0, 0, 4, 1, 2, rispettivamente; farà:

  - creare l'array di bit ``[0, 0, 0, 0, 0, 0, 0, 0; 0, 1, 0, 0, 0, 0, 0, 0; 0, 0, 1, 0, 0, 0, 0, 1]`` che in notazione esadecimale genera l'array di byte ``[0x00, 0x40, 0x21]``.
  - comprimere l'array utilizzando DEFLATE.

.. note::
  Quando il Fornitore di Credenziale sceglie il numero di bit per trasmettere gli stati delle Credenziali che emette, PUÒ aggiungere altri stati oltre a quelli descritti sopra. L'aggiunta di molti stati diversi per il ciclo di vita di una Credenziale deve tuttavia essere attentamente ponderata poiché rivela informazioni alle Relying Party.

.. note::
  La principale considerazione sulla privacy per una Status List è impedire al Fornitore di Credenziale di tracciare l'uso della Credenziale quando lo stato viene controllato. Se un Fornitore di Credenziale offre informazioni sullo stato facendo riferimento a un token specifico, ciò consentirebbe al Fornitore di Credenziale di creare un profilo per il token emesso correlando la data e l'identità delle Relying Party che richiedono lo stato. Le implementazioni DEVONO quindi integrare le informazioni sullo stato di molte Credenziali nella stessa lista. Di conseguenza, il Fornitore di Credenziale non apprende per quale Credenziale la Relying Party sta richiedendo la Status List. La privacy del Titolare è protetta dall'anonimato all'interno dell'insieme di Credenziali nella Status List, questo limita le possibilità di tracciamento da parte del Fornitore di Credenziale.
  Questo effetto di privacy di gruppo dipende dal numero di entità all'interno della Status List. Una maggiore quantità di Credenziali referenziate in essa risulta in una migliore privacy ma influisce anche sulle prestazioni poiché più dati devono essere trasferiti per leggere la Status List. A seconda dei parametri della Status List (ad esempio la quantità di bit che designano i valori della Credenziale), i Fornitori di Credenziale devono trovare un equilibrio appropriato tra privacy e prestazioni.

  Una volta che la Relying Party riceve una Credenziale, questo le consente di richiedere la Status List per validare il suo stato attraverso il parametro URI fornito e cercare l'indice corrispondente. Tuttavia, la Relying Party è in grado di memorizzare l'URI e l'indice della Credenziale per richiedere nuovamente la Status List in un momento successivo. Facendolo regolarmente, la Relying Party può creare un profilo dello stato di validità della Credenziale. Questo comportamento potrebbe anche essere abusato in casi in cui non è intenzionale e sconosciuto al Titolare, ad esempio profilando la sospensione di una patente di guida. Questo comportamento potrebbe essere mitigato, ad esempio, con la regolare riemissione della Credenziale.

Token di Status List
"""""""""""""""""""""""

 Il Token di Status List è disponibile all'Endpoint di Status List e contiene i seguenti parametri.

.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Header**
    - **Descrizione**
    - **Riferimento**
  * - **alg**
    - RICHIESTO. Un identificatore di algoritmo di firma digitale come per il registro IANA "JSON Web Signature and Encryption Algorithms". DEVE essere uno degli algoritmi supportati nella Sezione :ref:`algorithms:Algoritmi Crittografici` e NON DEVE essere impostato su ``none`` o su un identificatore di algoritmo simmetrico (MAC).
    - [:rfc:`7515`], [:rfc:`7517`].
  * - **typ**
    - RICHIESTO. DEVE essere impostato su ``statuslist+jwt``.
    - `TOKEN-STATUS-LIST`_
  * - **kid**
    - RICHIESTO. Identificatore univoco della chiave pubblica del Fornitore di Credenziale che firma il Token di Status.
    - :rfc:`7638#section_3`.
  * - **x5c**
    - RICHIESTO. Certificato di chiave pubblica X.509 o catena di certificati corrispondente alla chiave utilizzata per firmare il Token di Status List
    - :rfc:`5280`

.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Payload**
    - **Descrizione**
    - **Riferimento**
  * - **sub**
    - RICHIESTO. Il claim del soggetto DEVE specificare l'URI del Token di Status List. Il valore DEVE essere uguale a quello del claim uri contenuto nel claim status_list della Credenziale.
    - [:rfc:`7519`]
  * - **iat**
    - RICHIESTO. Il claim issued at DEVE specificare l'ora in cui è stato emesso il Token di Status List.
    - [:rfc:`7519`]
  * - **exp**
    - RICHIESTO. Il claim expiration time, se presente, DEVE specificare l'ora in cui il Token di Status List è considerato scaduto dal Fornitore di Credenziale.
    - [:rfc:`7519`]
  * - **ttl**
    - OPZIONALE. Il claim time to live, se presente, DEVE specificare la quantità massima di tempo, in secondi, che il Token di Status List può essere memorizzato nella cache da un consumatore prima che una copia fresca DOVREBBE essere recuperata. Il valore del claim DEVE essere un numero positivo codificato in JSON come un numero. Questa quantità di tempo NON DOVREBBE superare il tempo di scadenza definito nel claim **exp**.
    - `TOKEN-STATUS-LIST`_
  * - **status_list**
    - RICHIESTO. Oggetto JSON che contiene una Status List.
    - `TOKEN-STATUS-LIST`_

.. note::
  Si RACCOMANDA che il Fornitore di Credenziale imposti il claim ``exp`` in modo che il Token di Status List abbia una breve durata. In genere, questo comporta che il claim ``exp`` non superi il claim ``iat`` di più di 24 ore.

Una Status List codificata in JSON ha la seguente struttura:

.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Parametro**
    - **Descrizione**
    - **Riferimento**
  * - **bits**
    - RICHIESTO. Intero JSON che specifica il numero di bit per Credenziale nell'array di byte compresso (`lst`). I valori consentiti per bits sono 1,2,4 e 8.
    - `TOKEN-STATUS-LIST`_
  * - **lst**
    - RICHIESTO. Stringa JSON che contiene i valori di stato per tutte le Credenziali di cui trasmette gli stati. Il valore DEVE essere l'array di byte compresso codificato in base64url.
    - `TOKEN-STATUS-LIST`_
  * - **aggregation_uri**
    - OPZIONALE. Stringa JSON che contiene un URI per recuperare l'Aggregazione di Status List per questo tipo di Credenziale o Fornitore di Credenziale.
    - `TOKEN-STATUS-LIST`_

Di seguito è riportato un esempio di Token di Status List prima di applicare la firma e la codifica:

.. code::

  {
    "alg": "ES256",
    "kid": "$KID",
    "typ": "statuslist+jwt"
  }
  .
  {
    "exp": 2291720170,
    "iat": 1686920170,
    "status_list": {
      "bits": 1,
      "lst": "eNrbuRgAAhcBXQ"
    },
    "sub": "https://example-issuer.com/statuslists/",
    "ttl": 43200
  }
 
 
Gestione dello Stato delle Credenziali con Token di Status List
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

 I Fornitori di Credenziale, una volta che una Credenziale è stata generata, DEVONO:

  - Memorizzarla localmente con il set minimo di dati necessari per gestire il suo ciclo di vita, incluso lo stato di validità di quella Credenziale;
  - Includere un claim ``status_list`` all'interno del valore dell'Oggetto JSON del claim ``status`` della Credenziale.

 Il valore del claim ``status_list`` DEVE essere a sua volta un Oggetto JSON con i seguenti parametri

.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Parametro**
    - **Descrizione**
    - **Riferimento**
  * - **idx**
    - RICHIESTO. Il claim idx (indice) DEVE specificare un Intero che rappresenta l'indice da controllare per le informazioni sullo stato nella Status List per la Credenziale corrente. Il valore di idx DEVE essere un numero non negativo, contenente un valore di zero o maggiore.
    - `TOKEN-STATUS-LIST`_
  * - **uri**
    - RICHIESTO. Il claim uri (URI) DEVE specificare un valore String che identifica il Token di Status List contenente le informazioni sullo stato per la Credenziale. Il valore di uri DEVE essere un URI conforme a [:rfc:`3986`].
    - `TOKEN-STATUS-LIST`_


Verifica degli Stati delle Credenziali
""""""""""""""""""""""""""""""""""""""

Il recupero, l'elaborazione e la verifica di un Token di Status List possono essere effettuati sia dall'Istanza del Wallet che da una Relying Party. Di seguito viene descritto per la Relying Party, tuttavia, le stesse regole si applicherebbero anche all'Istanza del Wallet.

.. _fig_entity-relation-credential-revocation-SL:
.. plantuml:: plantuml/status-list-flow.puml
    :width: 80%
    :alt: La figura illustra il Flusso di Status List.
    :caption: `Flusso di Status List. <https://www.plantuml.com/plantuml/svg/RS-n2i8m4CRnFKzn15TVm44AWbfm42suk9pj3OVf9UOkvFMDEXMS_p_u-3erp5Rc05T3AmedLeDzYDLXiIXbVb1sgHaUEQ4O-1k6G0QzgA6Cv04LAY_DBjD4Oem1UjL2-QlOkSgmtW9lu42sc3mEmnakz2gavXfggZRsXsYAeWHt0R_wvKyTufF4kuvaQc_U>`_


.. .. figure:: ../../images/High-Level-Flow-Status-List.svg
..   :figwidth: 100%
..   :align: center
..   :target: https:https://www.plantuml.com/plantuml/svg/TOv1IyD048Nl-oiUYyUQ7z23L4Im9uiDU50fOpk7XSqapioIl--IQ27GdERmllU-sPcJUkboeEAzbEwRDGoadivf8774TygP7Nkff9mvWWnZMZ9FoXSMJvInDoki4vL261Fk7v2sEBmUMnoTl1WUpRYMUy5BsnxmnZ-5pV4fY3OH9_edJZg75h75HoM0ktdbEl9NtqnXqpJrVeKGghYQnwfUizhGY_6QTaujhcjdukhTtCIULNjT_hPZkPGk_m80

..   Status List Flow

Richiesta HTTP di Status Lists
..............................

 Per ottenere il Token di Status List, la Relying Party DEVE inviare una richiesta HTTP GET al valore ``status.status_list.uri`` fornito all'interno della Credenziale.

 La Relying Party DOVREBBE inviare l'Accept-Header ``application/statuslist+jwt`` per indicare che il tipo di risposta richiesto per il Token di Status List è il formato JWT.

 Di seguito è riportato un esempio non normativo di una richiesta per un Token di Status List:

.. code::

  GET /statuslists HTTP/1.1
  Host: example-issuer.com
  Accept: application/statuslist+jwt


Risposta HTTP di Status Lists
.............................

 L'Endpoint di Status List risponde con un Token di Status List e DEVE utilizzare un codice di stato HTTP nell'intervallo 2xx. Nella risposta di successo, lo Status Provider DEVE utilizzare il content-type ``application/statuslist+jwt`` per il Token di Status List in formato JWT.

 La risposta HTTP DOVREBBE utilizzare la Content-Encoding gzip come definito in [:rfc:`9110`].

 Se gli header HTTP relativi alla cache sono presenti nella risposta HTTP, le Relying Party DOVREBBERO dare priorità ai claim ``exp`` e ``ttl`` all'interno del Token di Status List rispetto agli header HTTP per determinare il comportamento della cache.

 Di seguito è riportato un esempio non normativo di una risposta per un Token di Status List con tipo ``application/statuslist+jwt``:

.. code::

  HTTP/1.1 200 OK
  Content-Type: application/statuslist+jwt

  eyJhbGciOiJFUzI1NiIsImtpZCI6IjEyIiwidHlwIjoic3RhdHVzbGlzdCtqd3QifQ.eyJleHAiOjIyOTE3MjAxNzAsImlhdCI6MTY4NjkyMDE3MCwiaXNzIjoiaHR0cHM6Ly9leGFtcGxlLmNvbSIsInN0YXR1c19saXN0Ijp7ImJpdHMiOjEsImxzdCI6ImVOcmJ1UmdBQWhjQlhRIn0sInN1YiI6Imh0dHBzOi8vZXhhbXBsZS5jb20vc3RhdHVzbGlzdHMvMSIsInR0bCI6NDMyMDB9.SSdg3AnTHsyRtCHziLy-QnXg-YRldMEXkdEgDXgE_ZvIvjM0eULQlzEbLBLfCeGhlqKJSReC-m85K79CTjJDzg

Al ricevimento di una Credenziale, una Relying Party DEVE prima eseguire la validazione della Credenziale stessa (ad esempio, controllando gli attributi previsti, la firma valida e il tempo di scadenza). Se questa validazione non ha successo, la Credenziale DEVE essere rifiutata. Se la validazione ha avuto successo, la Relying Party DEVE eseguire i seguenti passaggi di validazione per valutare lo stato della Credenziale:
 
  - Controllare l'esistenza di un claim ``status``, controllare l'esistenza di un claim ``status_list`` all'interno del claim ``status`` e validare che il contenuto di ``status_list`` aderisca alle regole definite nella Sezione :ref:`credential-revocation:Gestione dello Stato delle Credenziali con Token di Status List`.
  - Risolvere il Token di Status List dall'URI fornito.
  - Validare il Token di Status List:
 
    - Validare la firma del Token di Status List seguendo le regole definite nella sezione 7.2 di [:rfc:`7519`]. Questo passaggio richiede la risoluzione di una chiave pubblica come descritto in :ref:`trust:L'Infrastruttura di Trust`.

    - Controllare l'esistenza dei claim richiesti come definito nella Sezione :ref:`credential-revocation:Token di Status List`.

  - Tutti i claim esistenti nel Token di Status List DEVONO essere controllati secondo :ref:`credential-revocation:Token di Status List`.

    - Il claim subject del Token di Status List DEVE essere uguale al claim `uri` nell'oggetto `status_list` della Credenziale.
    - Se la Relying Party ha politiche personalizzate riguardanti la freschezza del Token di Status List, DOVREBBE controllare il claim `iat`.
    - Se il tempo di scadenza è definito, DEVE essere controllato se il Token di Status List è scaduto.
    - Se la Relying Party sta utilizzando un sistema per memorizzare nella cache il Token di Status List, DOVREBBE controllare il claim `ttl` del Token di Status List e recuperare una copia fresca se (tempo in cui lo stato è stato risolto + `ttl` < tempo corrente).

  - Decomprimere la Status List con un decompressore compatibile con DEFLATE [:rfc:`1951`] e ZLIB [:rfc:`1950`].
  - Recuperare il valore di stato dell'indice specificato nella Credenziale come descritto in :ref:`credential-revocation:Creazione delle Status Lists`. Fallire se l'indice fornito è fuori dai limiti della Status List.
  - Controllare il valore di stato come descritto in :ref:`credential-revocation:Creazione delle Status Lists`.

 Se uno di questi controlli fallisce, non è possibile fare alcuna dichiarazione sullo stato della Credenziale e la Credenziale DOVREBBE essere rifiutata.

 Se, ad esempio, l'array di byte decompresso è ``[0x00, 0x40, 0x21]``, corrisponde all'array di bit ``[0, 0, 0, 0, 0, 0, 0, 0; 0, 1, 0, 0, 0, 0, 0, 0; 0, 0, 1, 0, 0, 0, 0, 1]``. Lo Stato della Credenziale il cui valore del claim ``idx`` è ``5`` in questo array si riferisce all'ultima coppia di 4 bit (cioè, ``[0, 0, 1, 0] = 0x02``) il cui valore di stato è ``SUSPENDED``.

 In caso di errore durante la generazione della risposta da parte dell'Endpoint del Token di Status, DEVONO essere supportati i seguenti Codici di Stato HTTP:

.. list-table::
  :class: longtable
  :widths: 20 80
  :header-rows: 1

  * - **Codice di Stato**
    - **Descrizione**
  * - *500 Internal Server Error* [RICHIESTO]
    - Il Provider di Status List ha riscontrato un problema interno.
  * - *503 Service Unavailable* [RICHIESTO]
    - Il Provider di Status List è temporaneamente non disponibile.
  * - *504 Gateway Timeout* [OPZIONALE]
    - Il Provider di Status List non può soddisfare la richiesta entro l'intervallo di tempo definito.

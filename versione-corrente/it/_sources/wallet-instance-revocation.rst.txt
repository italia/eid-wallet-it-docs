.. include:: ../common/common_definitions.rst


Revoca dell'Istanza del Wallet
==============================

Questa sezione descrive le entità coinvolte e le modalità per richiedere la revoca di un'Istanza del Wallet.

Il Fornitore di Wallet DEVE garantire la sicurezza e l'affidabilità delle Istanze del Wallet, mantenendole aggiornate e conformi ai requisiti di sicurezza. Quando, per motivi tecnici di sicurezza (ad esempio, relativi alla compromissione del materiale crittografico) la sicurezza dell'Istanza del Wallet è compromessa, il Fornitore di Wallet DEVE revocare l'Istanza del Wallet.

Come mostrato in :numref:`fig_Wallet_Instance_Revoc_Entities`, altri attori POSSONO attivare il processo di revoca dell'Istanza del Wallet:

- **Utenti**, collegandosi al portale web del Fornitore di Wallet dalla propria Istanza del Wallet o utilizzando un browser esterno.
- **Fornitori di Attestati Elettronici di Dati di Identificazione Personale** quando notificati dalla Fonte Autentica del PID (ANPR) del decesso dell'Utente.
- **Autorità Legali o l'Organismo di Supervisione** in casi di comprovate attività illegali.


.. _fig_Wallet_Instance_Revoc_Entities:
.. plantuml:: plantuml/wallet-instance-revocation-entities.puml
    :width: 99%
    :alt: La figura illustra le Entità coinvolte nel processo di revoca dell'Istanza del Wallet.
    :caption: `Entità coinvolte nel processo di revoca dell'Istanza del Wallet. <https://www.plantuml.com/plantuml/svg/fLDHYnD137xVNn7xuXq8ljoZo7djWXNKqfw8SB1CTs8RtCxKcSpMLVpl9kDsJpk-MIZRfCdtVVcIlOri0gT31xLZOi88v7hVzMZb1_0UuQFfEcHOEYbrBKB0thU6oJiu1jzYZDKJScsNBCAB-Stp-KqpzuUZT-ZuPLMzNYxgPdDVh-ltzvzMzTLrLQqmHE-kKiJm36OVv36JPnOmW3yvShlC_E0kk6VIVEUJioOCLwVyNnE7o7YG_h5sa-FPDVoeG3wJb7CzZLZISOakAVs-DSxiC8BgUnfXGJjYqy4ye1KSCbqK7V_45ZzwiZBL6Ner9ixGOnmBKuspSC8j26LFBIh3pwfw9329zqhUDj6daDM_EgTWarC5XneBXZdGDh74xBEhonWJXinu62VLT6ywihe0KSH91KpiJVtjjm8Vw3lQPklje0Acp7GyPmsRTDH1eWy3t4brPdkJBBLY7uoDF0Z97pDI5gOJB1U5Srbr_4krbcaykXul3QogDNRZbLqig5m-h1_FUerVXOiLGX6AtlAIjFbByQge20NGmVvNH7a0artlFDFdGTUjv_hWB1hUZzJ5raeDO_jIyZjTJilK4rDMVulEfaFt2m00>`_


.. .. figure:: ../../images/wallet_instance_revocation.svg
..     :figwidth: 80%
..     :align: center
..     :target: https://www.plantuml.com/plantuml/svg/fL9TZn8z5BwVNt5URbusSPSRhxnQ5oOHuog1tHYJJIPbMk74JZksf-1e_E-UKmiguvqafFIXpyVvk8sa0gNELl-XQstI1lP4VNmncmLrlDaXxTCsHHDQxyWukcbzD-kjSiAvZgGjRcVpvzShWHxltymw5Sa4XfgvxthlXDEBVlLgkQYRpKEzhjyzV5ZLqwkgMfaGlPkA_ZEOFF8nuRDsX3I0FpfqEw2zWIVtNbbh29QEyxhMJ9XyvvFJAWpJO_wlYGCxTymlRpVvFhc2RnNmvnpdz1wBbZ0kr1cIxxroQcSYIBx_8ooGsw4ip8FHh8FAHixnL-q--0DghkealIh0IRhS8rnOWt8QZcOBR7d0reZ3zwhwPQ0IxSMyRQ9F8QT_UO9Waw6HXpGM5570RIA-ayzTNSQOJCYENQbKu8Eog6K0d8YI13YxD_MNdmbymAz6Drkl1mbmHY3F3aqyPTYaNWg9FWnmnw-ps-kaiKLbeH1fO9FVQiGSJ2fOBaQTowdZ7wdbcTnBr-Db0wjgRMpPiei1ZOSFQtFmhIBqZdz-PYyI2L4OSSUR9EHFvdAg4a84fB1_3J5UW7Extdh2ZuECMzRroMcZQ5-iHrCRPoZq9UCx6KvBU432dFxME9qw-mC0

..     Entities involved in the Wallet Instance revocation process.

.. note::
  - Il flusso per la Revoca dell'Istanza del Wallet attivato dall'Utente è dettagliato di seguito.
  - L'endpoint utilizzato dal Fornitore di Attestati Elettronici di Dati di Identificazione Personale è dettagliato nel Catalogo e-Service del Fornitore di Wallet PDND (vedere la Sezione :ref:`wallet-provider-endpoint:Catalogo e-Service PDND del Fornitore di Wallet` per i dettagli tecnici).
  - Il flusso per le Entità Autorizzate (ad esempio, Organismi di Supervisione) è fuori dall'ambito di questa specifica, sarà gestito da ciascun Fornitore di Wallet.



Richiesta di Revoca dell'Istanza del Wallet
"""""""""""""""""""""""""""""""""""""""""""

Gli Utenti POSSONO richiedere la revoca dell'Istanza del Wallet:

- *Selezionando la funzionalità di revoca dalla propria Istanza del Wallet*: questa funzionalità può essere utilizzata dagli Utenti prima di cambiare il proprio telefono.
- *Utilizzando un user agent esterno*: questo copre i casi in cui gli Utenti perdono il loro dispositivo e quindi l'accesso alla loro Istanza del Wallet.

In entrambi i casi, utilizzando il portale del Fornitore di Wallet:

- Gli Utenti DEVONO autenticarsi con almeno un meccanismo di autenticazione a due fattori, o avere una sessione attiva che soddisfi questo requisito.
- Il Fornitore di Wallet DEVE consentire agli Utenti di visualizzare lo stato delle loro Istanze del Wallet associate alla loro sessione autenticata e chiedere la revoca, inviando una Richiesta di Recupero o Revoca dell'Istanza del Wallet, a seconda dei casi, all'endpoint :ref:`wallet-provider-endpoint:Endpoint di Gestione dell'Istanza di Wallet` del Backend del Fornitore del Portafoglio.

Di seguito è riportato un esempio non normativo di una Richiesta di Recupero delle Istanze del Wallet.

.. code:: http

   GET /wallet-instances HTTP/1.1
   Host: walletprovider.example.com

In caso di recupero riuscito, il Fornitore di Wallet DEVE restituire una risposta di conferma, con lo stato di tutte le Istanze del Wallet associate all'Utente.
Di seguito è riportato un esempio non normativo di una Risposta di Recupero delle Istanze del Wallet.

.. code:: http

   HTTP/1.1 200 OK
   Content-Type: application/json
   Cache-Control: no-store

   [
     {
       "id": "f7b2a8d9",
       "status": "ACTIVE",
       "issued_at": "2024-03-12T10:00:00Z"
     },
     {
       "id": "g8b235c4",
       "status": "REVOKED",
       "issued_at": "2024-02-28T15:30:00Z"
     }
   ]

Una volta che l'Utente identifica l'Istanza del Wallet da revocare, può essere inviata una Richiesta di Revoca dell'Istanza del Wallet all'endpoint, includendo l'ID dell'Istanza del Wallet come parametro di percorso.
Di seguito è riportato un esempio non normativo di una Richiesta di Revoca dell'Istanza del Wallet.

.. code-block:: http

    PATCH /wallet-instances/{f7b2a8d9} HTTP/1.1
    Host: wallet-provider.example.org
    Content-Type: application/json

    {
      "status": "REVOKED"
    }




Risposta alla Revoca dell'Istanza del Wallet
""""""""""""""""""""""""""""""""""""""""""""

In caso di revoca riuscita, il Fornitore di Wallet DEVE restituire una risposta di conferma.
Di seguito è riportato un esempio non normativo di una Risposta di Revoca dell'Istanza del Wallet.


.. code-block:: http

   HTTP/1.1 204 No Content


Meccanismi di Verifica della Revoca
"""""""""""""""""""""""""""""""""""

La verifica della validità dell'Istanza del Wallet DEVE essere eseguita:

- **Durante la fase di emissione o presentazione della Credenziale Elettronica** rispettivamente dai Credential Issuer e dalle Relying Party. Solo le Istanze del Wallet in stato Operativo o Valido hanno Attestati di Wallet validi. Pertanto, la verifica della validità di un'Istanza del Wallet viene eseguita indirettamente dai Credential Issuer e dalle Relying Party verificando la presenza di un Attestato di Wallet valido (cioè non scaduto e firmato da un Fornitore di Wallet affidabile). Durante la presentazione di prossimità, l'Istanza del Wallet potrebbe non essere in grado di recuperare un Attestato di Wallet aggiornato; in questo caso, l'Istanza del Wallet DOVREBBE inviare l'ultima versione dell'Attestato di Wallet. Spetta alla Relying Party determinare se una presentazione con un Attestato di Wallet valido ma scaduto sia valida o meno.

- **Durante il periodo di validità della Credenziale Elettronica** dai Credential Issuer. Infatti, se l'Istanza del Wallet viene revocata, il PID ospitato al suo interno DEVE essere revocato. Anche qualsiasi altra Credenziale Elettronica ottenuta attraverso la presentazione del PID DEVE quindi essere revocata. Nella versione attuale della specifica, i Credential Issuer vengono direttamente notificati della revoca di un'Istanza del Wallet dal Fornitore di Wallet utilizzando un e-service PDND.


.. note::
  Con l'introduzione del **Wallet Trust Evidence (WTE)**, questa sezione sarà aggiornata di conseguenza.

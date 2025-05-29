.. include:: ../common/common_definitions.rst


Inizializzazione e Registrazione dell'Istanza del Wallet
========================================================

Questo processo consente all'Utente che ha appena installato l'applicazione dell'Istanza del Wallet di registrare l'Istanza del Wallet presso il Backend del Fornitore di Wallet. Durante questo processo, l'applicazione dell'Istanza del Wallet richiederà un'attestazione di sicurezza e integrità dal produttore del sistema operativo, che associa anche una coppia di chiavi a lunga durata memorizzata in un adeguato storage sicuro all'interno del dispositivo stesso. Questa attestazione sarà convalidata dal Fornitore di Wallet e, se la convalida ha esito positivo, il Fornitore di Wallet autenticherà l'Istanza del Wallet. Per i dettagli vedere :ref:`mobile-application-instance:Inizializzazione dell'Istanza dell'Applicazione Mobile`.

.. warning::
  Durante la fase di registrazione dell'Istanza del Wallet presso il Fornitore di Wallet è necessario anche associare l'Istanza del Wallet a un Utente specifico, autenticando l'Utente con il Fornitore di Wallet. Il meccanismo di autenticazione è a discrezione del Fornitore di Wallet e non sarà trattato all'interno di queste linee guida, poiché ogni Fornitore di Wallet potrebbe avere già implementato i propri sistemi di autenticazione dell'Utente.

.. note::
  Il Fornitore di Wallet DOVREBBE associare l'Istanza del Wallet (tramite l'identificatore ``hardware_key_tag``) a un Utente specifico identificato in modo univoco all'interno dei sistemi del Fornitore di Wallet. Questo sarà utile per il ciclo di vita dell'Istanza del Wallet e per una futura revoca. Per i dettagli vedere :ref:`mobile-application-instance:Istanza dell'Applicazione Mobile`.

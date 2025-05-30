.. include:: ../common/common_definitions.rst


Fonti Autentiche
================

Le Fonti Autentiche forniscono attributi degli Utenti ai Fornitori di Attestati Elettronici, consentendo loro il rilascio degli Attestati Elettronici. Durante il Flusso di Emissione, i Fornitori di Attestati Elettronici richiedono alle Fonti Autentiche gli attributi necessari per fornire l'Attestato richiesto dall'Utente. Le Fonti Autentiche POSSONO anche fornire una Credential Offer legata ai loro Fornitori di Attestati Elettronici come definito nella Sezione :ref:`credential-issuance-endpoint:Credential Offer Endpoint`.

Le Fonti Autentiche pubbliche DEVONO interagire con i Fornitori di Attestati Elettronici tramite PDND secondo le regole definite nella Sezione :ref:`e-service-pdnd:e-Service PDND` e nella Sezione :ref:`credential-revocation:Aggiornamento dello Stato da parte delle Fonti Autentiche`. Vedere anche la Sezione :ref:`authentic-source-endpoint:Catalogo degli e-Service PDND delle Fonti Autentiche` per ulteriori dettagli.

Le Fonti Autentiche DEVONO:

  - fornire gli attributi dell'Utente quando richiesti dal Fornitore di Attestati Elettronici autorizzato a emettere l'Attestato Elettronico correlato che attesta gli attributi. Le Fonti Autentiche pubbliche DEVONO utilizzare PDND per inviare gli attributi dell'Utente ai loro Fornitori di Attestati Elettronici. Quando gli attributi dell'Utente non sono disponibili durante il Flusso di Emissione, le Fonti Autentiche DEVONO fornire ai Fornitori di Credenziale una stima del tempo in cui i dati dell'Utente saranno disponibili. Le Fonti Autentiche POSSONO richiedere una prova che:

    - la richiesta di attributi degli Utenti sia relativa ai dati che li riguardano;
    - la richiesta di attributi dell'Utente provenga da un'Istanza del Wallet valida;

  - collaborare con i loro Fornitori di Attestati Elettronici in modo che gli attributi dichiarati in un Attestato Elettronico siano sempre mantenuti aggiornati. Le Fonti Autentiche pubbliche DEVONO utilizzare PDND per notificare ai loro Fornitori di Attestati Elettronici qualsiasi aggiornamento riguardante attributi che sono cambiati o che non sono più validi.

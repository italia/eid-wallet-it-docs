.. include:: ../common/common_definitions.rst


Fonti Autentiche
================

Le Fonti Autentiche forniscono gli Attributi dell'Utente ai Fornitori di Attestati Elettronici consentendo loro l'emissione delle Credenziali Elettroniche. Durante il Flusso di Emissione, i Fornitori di Attestati Elettronici richiedono alle Fonti Autentiche gli attributi necessari per fornire l'Attestato Elettronico richiesto. Le Fonti Autentiche POSSONO anche fornire un'Offerta di Atetstato relativa ai loro Fornitori di Attestati Elettronici come definito nella Sezione :ref:`credential-issuance-endpoint:Credential Offer Endpoint`.

Le Fonti Autentiche Pubbliche DEVONO interagire con i Fornitori di Attestati Elettronici tramite PDND secondo le regole definite nella Sezione :ref:`e-service-pdnd:e-Service PDND` e nella Sezione :ref:`credential-revocation:Aggiornamento dello Stato da parte delle Fonti Autentiche`. Vedere anche la Sezione :ref:`authentic-source-endpoint:Catalogo delle Fonti Autentiche e-Service PDND` per ulteriori dettagli.

Le Fonti Autentiche DEVONO:

  - fornire gli Attributi dell'Utente quando richiesto dal Fornitore di Attestati Elettronici autorizzato a emettere la relativa Credenziale Elettronica che attesta gli attributi. Le Fonti Autentiche Pubbliche DEVONO utilizzare PDND per inviare gli Attributi dell'Utente ai loro Fornitori di Attestati Elettronici. Quando gli Attributi dell'Utente non sono disponibili durante il Flusso di Emissione, le Fonti Autentiche DEVONO fornire ai Fornitori di Attestati Elettronici un tempo stimato di quando i dati dell'Utente saranno disponibili. Le Fonti Autentiche POSSONO richiedere una prova che:

    - la richiesta degli Attributi dell'Utente sia relativa a dati che li riguardano;
    - la richiesta degli Attributi dell'Utente provenga da un'Istanza del Wallet valida;

  - cooperare con i Fornitori di Attestati Elettronici in modo che gli Attributi attestati in un Attestato Elettronico siano sempre mantenuti aggiornati. Le Fonti Autentiche Pubbliche DEVONO utilizzare PDND Signal Hub per notificare ai loro Fornitori di Attestati Elettronici qualsiasi aggiornamento riguardante attributi che sono cambiati o non sono più validi.

Panoramica
----------

La funzionalità del servizio elettronico template viene utilizzata per standardizzare la trasmissione dei dati dalle Fonti Autentiche ai Fornitori di Attestati Elettronici.
Il servizio elettronico template DOVREBBE essere pubblicato all'interno della PDND dal Fornitore di Attestati Elettronici ed è accessibile attraverso il Catalogo Template PDND.

Parametri del Template
----------------------

Il servizio elettronico template **DEVE** rispettare le seguenti proprietà:

    - **Name**: IT Wallet - Fonte Autentica - <``Nome dell'Attestato Elettronico``>
    - **Intended Recipients**: IT Wallet - Fonte Autentica - <``Dominio della Fonte Autentica``>
    - **Description**: Descrizioni utili al Fornitore di Attestati Elettronici in relazione al nuovo attestato elettronico <``Nome dell'Attestato Elettronico``>
    - **Technology**: REST
    - **Data variation via Signal Hub**: True
    - **Version changelog**: Servizio elettronico Fonte Autentica tramite implementazione template
    - **Voucher Time Limit**: 20
    - **Suggest custom threshold**: False
    - **Suggest manual agreement approval policy**: False
    - **Attributes**: <``Nome ufficiale dell'Ente Pubblico Fornitore di Attestati Elettronici``>

Istanziazione del Template
--------------------------

Ogni Fonte Autentica **DOVREBBE** istanziare il servizio elettronico template *IT Wallet - Fonte Autentica* nella PDND.  
Il processo di istanziazione risulterà in un nuovo servizio elettronico che **DEVE** soddisfare i seguenti requisiti:

    - **Signal Hub**: True
    - **Politica di approvazione manuale**: False
    - **Soglia giornaliera chiamate API per ogni fornitore**: maggiore di 10000
    - **Soglia giornaliera chiamate API**: maggiore di 10000

Informazioni aggiuntive richieste durante il processo di creazione sono dipendenti dal fornitore.

Specifica OpenAPI della Fonte Autentica PDND
----------------------------------------------

Di seguito è riportata la specifica OpenAPI completa per i servizi elettronici della Fonte Autentica PDND:

.. literalinclude:: ./oas3/OAS3-PDND-AS.yaml
    :language: yaml
    :linenos:

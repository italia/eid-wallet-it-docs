Matrice di Test per la Presentazione di Credenziali Remota
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Questa sezione fornisce l'insieme dei casi di test progettati per implementatori tecnici e team di sviluppo responsabili della creazione e del deployment di soluzioni Credential Verifier per i flussi remoti. È anche destinata agli organismi di valutazione che ispezionano e validano le implementazioni di soluzioni Credential Verifier per i flussi remoti.

.. note::
  Riferimenti sui piani di test ufficiali OpenID4VP aggiorneranno questa sezione nelle versioni future.

.. list-table::
  :class: longtable
  :widths: 15 15 35 35
  :header-rows: 1

  * - Test Case ID
    - Purpose
    - Description
    - Expected Result
  * - RPR-01
    - Same Device Flow
    - Verificare l'URL di redirect HTTP (302).
    - Il Wallet Instance riceve l'URL corretto.
  * - RPR-02
    - Cross Device Flow
    - Verificare la generazione del QR Code per Il Wallet Instance.
    - Il Wallet Instance scansiona il QR Code con successo.
  * - RPR-03
    - Cross Device Flow
    - Verificare che il QR Code contenga i parametri URL corretti.
    - Il Wallet Instance recupera l'URL con i parametri.
  * - RPR-04
    - Cross Device Flow
    - Testare la scansione del QR Code in condizioni di scarsa illuminazione.
    - Il QR Code viene scansionato con successo.
  * - RPR-05
    - Cross Device Flow
    - Verificare il livello di correzione errori del QR Code.
    - Il QR Code rimane leggibile se danneggiato.
  * - RPR-06
    - Cross Device Flow
    - Testare la scansione del QR Code con dispositivi diversi.
    - Il QR Code viene scansionato con successo.
  * - RPR-07
    - Request URI Method
    - Testare `request_uri_method` come `post`.
    - Il Wallet Instance invia i metadata tramite POST.
  * - RPR-08
    - Request URI Method
    - Testare `request_uri_method` come `get`.
    - Il Wallet Instance recupera il Request Object tramite GET.
  * - RPR-09
    - Request URI Method
    - Testare l'assenza di ``request_uri_method``.
    - Il Wallet Instance utilizza il metodo GET come default.
  * - RPR-10
    - Metadata
    - Verificare che i parametri corrispondano ai metadata del credential verifier openid.
    - Solo i parametri consentiti saranno considerati.
  * - RPR-11
    - User Consent
    - Testare l'idoneità di un credential verifier nel richiedere attributi utente.
    - L'utente può modificare la selezione dei dati sugli attributi opzionali.
  * - RPR-12
    - Authorization Response
    - Testare l'invio della Presentation Response.
    - La Relying Party riceve e valida la response con state e nonce.
  * - RPR-13
    - Authorization Response
    - Verificare la crittografia della response.
    - La response viene crittografata utilizzando la chiave pubblica della Relying Party.
  * - RPR-14
    - Error Handling
    - Testare la gestione di Request Object non validi.
    - Viene inviata una Authorization Error Response.
  * - RPR-15
    - Error Handling
    - Testare il recupero da ``server_error``.
    - L'utente viene invitato a riprovare o scansionare un nuovo QR code.
  * - RPR-16
    - Relying Party Response
    - Verificare la gestione corretta della Response.
    - La sessione utente viene aggiornata, viene fornito il redirect URI.
  * - RPR-17
    - Relying Party Response
    - Testare l'assenza di ``redirect_uri``.
    - Viene restituita una error response.
  * - RPR-18
    - Redirect URI
    - Testare il redirect all'endpoint della Relying Party.
    - L'utente viene reindirizzato correttamente.
  * - RPR-19
    - Redirect URI
    - Verificare la gestione di ``redirect_uri`` non validi.
    - Viene restituita una error response.
  * - RPR-20
    - User Consent
    - Verificare la visualizzazione dell'identità della Relying Party.
    - L'identità viene visualizzata chiaramente all'Holder.
  * - RPR-21
    - User Consent
    - Testare la revoca del consenso utente.
    - L'utente può revocare il consenso prima dell'invio.
  * - RPR-22
    - Credential Presentation
    - Verificare la conformità del formato della response.
    - Ogni Credential aderisce al formato specificato.
  * - RPR-23
    - Authorization Response
    - Testare la gestione dei timeout della response.
    - I retry devono avere successo a meno che la response non sia acquisita.
  * - RPR-24
    - Error Handling
    - Verificare la gestione di claims malformati nel payload di presentazione.
    - Viene inviata una Authorization Error Response.
  * - RPR-25
    - Error Handling
    - Verificare la gestione di claims malformati nelle credenziali presentate.
    - Viene inviata una Authorization Error Response.
  * - RPR-26
    - Error Handling
    - Testare la gestione di richieste scadute.
    - L'Holder viene notificato della scadenza.
  * - RPR-27
    - Relying Party Response
    - Verificare l'inclusione del response code.
    - Il response code è crittograficamente casuale.
  * - RPR-28
    - Relying Party Response
    - Testare la gestione di response code non validi.
    - Viene restituita una error response.
  * - RPR-29
    - Status Endpoint
    - Verificare la gestione dell'accesso non autorizzato.
    - L'accesso non autorizzato viene negato.
  * - RPR-30
    - Status Endpoint
    - Testare la gestione di session ID non validi.
    - Viene restituita una error response.
  * - RPR-31
    - Redirect URI
    - Verificare la gestione di sessioni scadute.
    - Viene restituita una error response.
  * - RPR-32
    - Redirect URI
    - Testare la gestione di errori del server.
    - Viene restituita una error response.
  * - RPR-33
    - Presentation Response
    - Verificare la gestione di payload di response di grandi dimensioni.
    - La response viene inviata con successo.
  * - RPR-34
    - Presentation Response
    - Testare la gestione di fallimenti nella crittografia della response.
    - Viene restituita una error response.
  * - RPR-35
    - Error Handling
    - Verificare la gestione di firme non valide.
    - Viene inviata una Authorization Error Response.
  * - RPR-36
    - Error Handling
    - Testare la gestione di valori nonce non validi.
    - Viene restituita una error response.
  * - RPR-37
    - Relying Party Response
    - Verificare la gestione di response malformate.
    - Viene restituita una error response.
  * - RPR-38
    - Relying Party Response
    - Testare la gestione di parametri di response mancanti.
    - Viene restituita una error response.
  * - RPR-39
    - Status Endpoint
    - Verificare la gestione di timeout di sessione.
    - Viene restituita una error response.
  * - RPR-40
    - Status Endpoint
    - Testare la gestione di status code non validi.
    - Viene restituita una error response.
  * - RPR-41
    - Redirect URI
    - Verificare la gestione di sessioni utente non valide.
    - Viene restituita una error response.
  * - RPR-42
    - Redirect URI
    - Testare la gestione di servizi non disponibili.
    - Viene restituita una error response.
  * - RPR-43
    - Same Device Flow
    - Verificare la gestione di cancellazioni utente.
    - L'utente può cancellare il processo.
  * - RPR-44
    - Cross Device Flow
    - Testare la scansione del QR Code con app diverse.
    - Il QR Code viene scansionato con successo.
  * - RPR-45
    - Cross Device Flow
    - Verificare la scansione del QR Code con illuminazione diversa.
    - Il QR Code viene scansionato con successo.
  * - RPR-46
    - Request URI Method
    - Testare la gestione di content type non supportati.
    - Viene restituita una error response.
  * - RPR-47
    - User Consent
    - Verificare la notifica utente sui cambiamenti di consenso.
    - L'utente viene informato sui cambiamenti di consenso.
  * - RPR-48
    - User Consent
    - Testare il consenso utente per dati sensibili.
    - L'utente può acconsentire ai dati sensibili.
  * - RPR-49
    - Authorization Response
    - Verificare la gestione di fallimenti nella decrittografia della response.
    - Viene restituita una error response.
  * - RPR-50
    - Authorization Response
    - Testare la gestione dei controlli di integrità della response.
    - L'integrità della response viene verificata.
  * - RPR-51
    - Relying Party Response
    - Verificare la gestione di fallimenti nella validazione della response.
    - Viene restituita una error response.
  * - RPR-52
    - Relying Party Response
    - Testare la gestione di errori di elaborazione della response.
    - Viene restituita una error response.
  * - RPR-53
    - Protected Resource Endpoint
    - Verificare la gestione di accesso non autorizzato alla sessione.
    - L'accesso non autorizzato viene negato.
  * - RPR-54
    - Redirect URI
    - Verificare la gestione di parametri di redirect non validi.
    - Viene restituita una error response.
  * - RPR-55
    - Redirect URI
    - Testare la gestione di fallimenti nel redirect.
    - Viene restituita una error response.
  * - RPR-56
    - Same Device Flow
    - Verificare la gestione di interruzioni utente.
    - L'utente può riprendere o cancellare il processo.
  * - RPR-57
    - Request URI Method
    - Testare la gestione di metodi HTTP non validi.
    - Viene restituita una error response.
  * - RPR-58
    - User Consent
    - Verificare la notifica utente sulla revoca del consenso.
    - L'utente viene informato sulla revoca del consenso.
  * - RPR-59
    - User Consent
    - Testare il consenso utente per dati opzionali.
    - L'utente può acconsentire ai dati opzionali.
  * - RPR-60
    - Authorization Response
    - Verificare la gestione di fallimenti nella firma della response.
    - Viene restituita una error response.
  * - RPR-61
    - Authorization Response
    - Testare la gestione di errori di formato della response.
    - Viene restituita una error response.
  * - RPR-62
    - Error Handling
    - Verificare la gestione di firme JWT non valide.
    - Viene inviata una Authorization Error Response.
  * - RPR-63
    - Error Handling
    - Testare la gestione di claims JWT non validi.
    - Viene restituita una error response.
  * - RPR-64
    - Relying Party Response
    - Verificare la gestione di errori di parsing della response.
    - Viene restituita una error response.
  * - RPR-65
    - Relying Party Response
    - Testare la gestione di errori di timeout della response.
    - Viene restituita una error response.
  * - RPR-66
    - Status Endpoint
    - Verificare la gestione della scadenza della sessione.
    - Viene restituita una error response.
  * - RPR-67
    - Status Endpoint
    - Testare la gestione di errori di rinnovo della sessione.
    - Viene restituita una error response.
  * - RPR-68
    - Redirect URI
    - Verificare la gestione di errori di loop di redirect.
    - Viene restituita una error response.
  * - RPR-69
    - Redirect URI
    - Testare la gestione di errori di sicurezza del redirect.
    - Viene restituita una error response.
  * - RPR-70
    - Same Device Flow
    - Verificare la gestione di timeout utente.
    - L'utente viene notificato del timeout.
  * - RPR-71
    - Cross Device Flow
    - Testare la scansione del QR Code con dispositivi diversi.
    - Il QR Code viene scansionato con successo.
  * - RPR-72
    - Cross Device Flow
    - Verificare la scansione del QR Code con app diverse.
    - Il QR Code viene scansionato con successo.
  * - RPR-73
    - Request URI Method
    - Testare la gestione di metodi HTTP non supportati.
    - Viene restituita una error response.

  * - RPR-74
    - Cross Device Flow
    - Testare la scansione del QR Code con dispositivi diversi.
    - Il QR Code viene scansionato con successo.

  * - RPR-75
    - Cross Device Flow
    - Verificare la scansione del QR Code con app diverse.
    - Il QR Code viene scansionato con successo.

  * - RPR-76
    - Request URI Method
    - Testare la gestione di metodi HTTP non supportati.
    - Viene restituita una error response.

  * - RPR-77
    - QR Code Generation
    - Verificare che il livello di correzione errori del QR Code sia Q (Quartile - fino al 25%).
    - Il QR Code utilizza il livello di correzione errori Q come richiesto.

  * - RPR-78
    - Request URI Method
    - Testare che il metodo HTTP sia impostato su ``get`` o ``post``.
    - Il metodo HTTP è correttamente impostato su ``get`` o ``post``.

  * - RPR-79
    - Request URI Method
    - Verificare che il metodo GET sia utilizzato come default quando non specificato.
    - Il metodo GET è utilizzato come default quando ``request_uri_method`` non è fornito.

  * - RPR-80
    - JWT Header
    - Testare che l'algoritmo di firma JWT sia supportato e non sia ``none``.
    - L'algoritmo di firma JWT è valido e non è ``none``.

  * - RPR-81
    - JWT Header
    - Verificare che il media type JWT sia ``oauth-authz-req+jwt``.
    - Il media type JWT è correttamente impostato su ``oauth-authz-req+jwt``.

  * - RPR-82
    - JWT Payload
    - Testare che ``response_mode`` sia impostato su ``direct_post.jwt``.
    - ``response_mode`` è correttamente impostato su ``direct_post.jwt``.

  * - RPR-83
    - JWT Payload
    - Verificare che ``response_type`` sia impostato su ``vp_token``.
    - ``response_type`` è correttamente impostato su ``vp_token``.

  * - RPR-84
    - JWT Payload
    - Testare che il nonce abbia almeno 32 cifre di lunghezza.
    - Il nonce ha la lunghezza minima richiesta di 32 cifre.

  * - RPR-85
    - JWT Payload
    - Verificare che il JWT non sia valido dopo la scadenza (exp).
    - Il JWT non è più valido dopo il timestamp di scadenza.

  * - RPR-86
    - Wallet Attestation Request
    - Testare che la richiesta di Wallet Attestation utilizzi una query DCQL standard.
    - La richiesta di Wallet Attestation utilizza correttamente la query DCQL standard.

  * - RPR-87
    - Wallet Attestation Request
    - Verificare che il parametro ``claims`` non sia incluso nella query DCQL per Wallet Attestation.
    - Il parametro ``claims`` non è incluso nella query DCQL per Wallet Attestation.

  * - RPR-88
    - Wallet Attestation Request
    - Testare che il parametro ``vct_values`` sia richiesto nella query DCQL per Wallet Attestation.
    - Il parametro ``vct_values`` è correttamente richiesto nella query DCQL.

  * - RPR-89
    - Error Response
    - Verificare che la Relying Party restituisca error response in formato JSON per errori ``request_uri``.
    - La Relying Party restituisce correttamente error response in formato JSON.

  * - RPR-90
    - Security
    - Testare che il parametro ``request_uri`` sia attestato da terza parte fidata.
    - Il parametro ``request_uri`` è correttamente attestato da terza parte fidata.

  * - RPR-91
    - Security
    - Verificare che il parametro ``response_uri`` sia attestato da terza parte fidata.
    - Il parametro ``response_uri`` è correttamente attestato da terza parte fidata.

  * - RPR-92
    - Wallet Nonce
    - Testare che la Relying Party controlli il ``wallet_nonce`` quando presente.
    - La Relying Party controlla correttamente il ``wallet_nonce`` quando presente.

  * - RPR-93
    - Response Types
    - Verificare che ``response_types_supported`` sia impostato su ``vp_token`` quando presente.
    - ``response_types_supported`` è correttamente impostato su ``vp_token``.

  * - RPR-94
    - Flow Support
    - Testare che la Relying Party supporti i flussi remoti richiesti.
    - La Relying Party supporta sia Same Device che Cross Device.

  * - RPR-95
    - HTTP Method Validation
    - Testare che ``request_uri_method`` sia impostato su ``get`` o ``post``.
    - Il parametro ``request_uri_method`` è correttamente impostato su ``get`` o ``post``.

  * - RPR-96
    - Endpoint Security
    - Testare che ``request_uri`` sia attestato da terza parte fidata.
    - Il parametro ``request_uri`` è correttamente attestato da terza parte fidata.

  * - RPR-97
    - Response Type Validation
    - Testare che ``response_type`` sia impostato su ``vp_token`` quando presente.
    - Il parametro ``response_type`` è correttamente impostato su ``vp_token`` quando presente.

  * - RPR-98
    - Algorithm Validation
    - Testare che l'algoritmo JWT sia supportato e non sia ``none`` o MAC.
    - L'algoritmo JWT è nella lista supportata e non è ``none`` o identificatore MAC.

  * - RPR-99
    - Media Type Validation
    - Testare che ``typ`` del JWT sia impostato su ``oauth-authz-req+jwt``.
    - Il parametro ``typ`` del JWT è correttamente impostato su ``oauth-authz-req+jwt``.

  * - RPR-100
    - Response Mode Validation
    - Testare che ``response_mode`` sia impostato su ``direct_post.jwt``.
    - Il parametro ``response_mode`` è correttamente impostato su ``direct_post.jwt``.

  * - RPR-101
    - Response Type Validation
    - Testare che ``response_type`` sia impostato su ``vp_token``.
    - Il parametro ``response_type`` è correttamente impostato su ``vp_token``.

  * - RPR-102
    - Nonce Entropy
    - Testare che il ``nonce`` abbia sufficiente entropia (32+ cifre).
    - Il parametro ``nonce`` ha entropia sufficiente con almeno 32 cifre.

  * - RPR-103
    - JWT Expiration
    - Testare che ``exp`` del JWT sia impostato correttamente.
    - Il parametro ``exp`` del JWT è impostato correttamente e non è scaduto.

  * - RPR-104
    - Response URI Security
    - Testare che ``response_uri`` sia attestato da terza parte fidata.
    - Il parametro ``response_uri`` è correttamente attestato da terza parte fidata.

  * - RPR-105
    - Wallet Attestation Request
    - Testare che la Relying Party richieda il Wallet Attestation via DCQL.
    - La Relying Party richiede correttamente il Wallet Attestation usando una query DCQL.

  * - RPR-106
    - Error Response Format
    - Testare che l'error response usi il content type ``application/json``.
    - L'error response usa correttamente il content type ``application/json``.

  * - RPR-107
    - Error Response Parameters
    - Testare che l'error response includa i parametri richiesti.
    - L'error response include i parametri ``error`` ed ``error_description``.

  * - RPR-108
    - Presentation Array
    - Testare che ``vp_token`` contenga almeno due presentazioni firmate.
    - ``vp_token`` contiene almeno due presentazioni firmate come richiesto.

  * - RPR-109
    - KB-JWT Validation
    - Testare che la Relying Party validi la firma del KB-JWT.
    - La Relying Party valida correttamente la firma del KB-JWT usando la chiave pubblica.

  * - RPR-110
    - KB-JWT Header
    - Testare che il KB-JWT contenga i parametri di header richiesti.
    - Il KB-JWT contiene i parametri di header ``typ`` e ``alg`` richiesti.

  * - RPR-111
    - KB-JWT Payload
    - Testare che il KB-JWT contenga i parametri di payload richiesti.
    - Il KB-JWT contiene i parametri ``iat``, ``aud``, ``nonce`` e ``sd_hash`` richiesti.

  * - RPR-112
    - KB-JWT Type
    - Testare che ``typ`` di KB-JWT sia impostato su ``kb+jwt``.
    - Il parametro ``typ`` di KB-JWT è correttamente impostato su ``kb+jwt``.

  * - RPR-113
    - KB-JWT Issuance Time
    - Testare che ``iat`` di KB-JWT sia impostato correttamente.
    - Il parametro ``iat`` di KB-JWT è correttamente impostato al tempo di emissione.

  * - RPR-114
    - KB-JWT Audience
    - Testare che ``aud`` di KB-JWT corrisponda all'identificatore della Relying Party.
    - Il parametro ``aud`` di KB-JWT corrisponde all'identificatore univoco della Relying Party.

  * - RPR-115
    - KB-JWT Nonce
    - Testare che il ``nonce`` di KB-JWT corrisponda al ``nonce`` del request object.
    - Il parametro ``nonce`` di KB-JWT corrisponde al ``nonce`` del request object.

  * - RPR-116
    - Response Processing
    - Testare che il Response URI restituisca HTTP 200 in caso di elaborazione riuscita.
    - Il Response URI restituisce HTTP 200 con content type ``application/json``.

  * - RPR-117
    - Wallet Attestation Presentation
    - Testare che l'Istanza del Wallet includa l'Attestazione del Wallet se richiesta.
    - L'Istanza del Wallet include correttamente l'Attestazione del Wallet quando richiesta.

  * - RPR-118
    - Presentation Array
    - Testare che vp_token contenga almeno due presentazioni firmate.
    - vp_token contiene almeno due presentazioni firmate come richiesto.

  * - RPR-119
    - KB-JWT Validation
    - Testare che la Relying Party validi la firma del KB-JWT.
    - La Relying Party valida correttamente la firma del KB-JWT usando la chiave pubblica.

  * - RPR-120
    - KB-JWT Signature Validation
    - Testare che la validazione della firma KB-JWT utilizzi la chiave pubblica corretta.
    - La validazione della firma KB-JWT utilizza la chiave pubblica inclusa nell'SD-JWT.

  * - RPR-121
    - KB-JWT Header
    - Testare che il KB-JWT contenga i parametri di header richiesti.
    - Il KB-JWT contiene i parametri di header ``typ`` e ``alg`` richiesti.

  * - RPR-122
    - KB-JWT Payload
    - Testare che il KB-JWT contenga i parametri di payload richiesti.
    - Il KB-JWT contiene i parametri ``iat``, ``aud``, ``nonce`` e ``sd_hash`` richiesti.

  * - RPR-123
    - KB-JWT Type
    - Testare che ``typ`` di KB-JWT sia impostato su ``kb+jwt``.
    - Il parametro ``typ`` di KB-JWT è correttamente impostato su ``kb+jwt``.

  * - RPR-124
    - KB-JWT Issuance Time
    - Testare che iat di KB-JWT sia impostato correttamente.
    - Il parametro iat di KB-JWT è correttamente impostato al tempo di emissione.

  * - RPR-125
    - KB-JWT Audience
    - Testare che aud di KB-JWT corrisponda all'identificatore della Relying Party.
    - Il parametro aud di KB-JWT corrisponde all'identificatore univoco della Relying Party.

  * - RPR-126
    - KB-JWT Nonce
    - Testare che il ``nonce`` di KB-JWT corrisponda al ``nonce`` del request object.
    - Il parametro ``nonce`` di KB-JWT corrisponde al ``nonce`` del request object.

  * - RPR-127
    - Authorization Error Response
    - Testare che l'Istanza del Wallet notifichi errori di validazione alla Relying Party.
    - L'Istanza del Wallet invia correttamente una Authorization Error Response per errori di validazione.

  * - RPR-128
    - Error Response Format
    - Testare che la risposta di errore contenga i parametri error e error_description.
    - La risposta di errore contiene correttamente i parametri error e error_description.

  * - RPR-129
    - HTTP Status Code Validation
    - Testare che la Relying Party restituisca i codici di stato HTTP corretti per gli errori.
    - La Relying Party restituisce i codici di stato HTTP appropriati per diversi tipi di errore.

  * - RPR-130
    - Error Code Consistency
    - Testare che i codici di errore siano consistenti tra diversi endpoint.
    - I codici di errore sono consistenti tra tutti gli endpoint della Relying Party.

  * - RPR-131
    - Response Code Inclusion
    - Testare che la Relying Party includa il response code nel ``redirect_uri``.
    - La Relying Party include correttamente il response code fresco nel ``redirect_uri``.

  * - RPR-132
    - Redirect URI Security
    - Testare che ``redirect_uri`` sia attestato da terza parte fidata.
    - Il parametro ``redirect_uri`` è correttamente attestato da terza parte fidata.

  * - RPR-133
    - Validation Error Response
    - Testare che il Response URI restituisca una error response in caso di fallimenti di validazione.
    - Il Response URI restituisce una error response quando i controlli di validazione falliscono.


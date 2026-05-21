.. include:: ../common/common_definitions.rst

Matrice di Test per il Verificatore di Credenziali in Remoto
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Questa sezione fornisce l’insieme dei casi di test progettati per implementatori tecnici e team di sviluppo responsabili della creazione e distribuzione di soluzioni Credential Verifier per flussi remoti. È inoltre destinata agli enti di valutazione che ispezionano e validano le implementazioni delle soluzioni Credential Verifier per flussi remoti.

.. note::
  I riferimenti ai piani di test ufficiali OpenID4VP aggiorneranno questa sezione nelle prossime versioni.

.. list-table::
  :class: longtable
  :widths: 15 15 35 35
  :header-rows: 1

  * - ID Caso di Test
    - Scopo
    - Descrizione
    - Risultato Atteso
  * - RPR-01
    - Flusso stesso dispositivo
    - Verifica URL di redirect HTTP (302).
    - Il Relying Party emette un URL corretto utilizzando la base url fornita nei suoi metadati.
  * - RPR-02
    - Flusso tra dispositivi
    - Verifica la generazione del QR Code per l’istanza Wallet.
    - Il Relying Party emette correttamente il QR Code.
  * - RPR-03
    - Flusso tra dispositivi
    - Verifica che il QR Code contenga i parametri URL corretti.
    - Il Relying Party emette il QR-Code contenente un URL che utilizza la base url fornita nei suoi metadati.
  * - RPR-04
    - Flusso tra dispositivi
    - Test della scansione del QR Code in condizioni di scarsa illuminazione.
    - Il QR Code viene scansionato con successo.
  * - RPR-05
    - Flusso tra dispositivi
    - Verifica il livello di correzione degli errori del QR Code.
    - Il QR Code rimane leggibile anche se danneggiato.
  * - RPR-06
    - Flusso tra dispositivi
    - Test della scansione del QR Code con dispositivi diversi.
    - Il QR Code viene scansionato con successo.
  * - RPR-07
    - Metodo request_uri
    - Test di ``request_uri_method`` come ``post``.
    - Il Relying Party accetta i metadati dell’istanza Wallet via POST e risponde con un oggetto Request aggiornato.
  * - RPR-08
    - Metodo request_uri
    - Test di ``request_uri_method`` come ``get``.
    - Il Relying Party emette l’oggetto Request tramite risposta HTTP GET.
  * - RPR-09
    - Metodo request_uri
    - Test dell’assenza di ``request_uri_method``.
    - Il Relying Party accetta e predefinisce il metodo GET.
  * - RPR-10
    - Metadati
    - Verifica che i parametri corrispondano ai metadati OpenID Credential Verifier.
    - Solo i parametri consentiti saranno considerati.
  * - RPR-11
    - Consenso Utente
    - Test dell’idoneità di un Credential Verifier nel richiedere attributi utente.
    - L’utente può modificare la selezione dei dati sugli attributi opzionali.
  * - RPR-12
    - Risposta di Autorizzazione
    - Test dell’invio della Presentation Response.
    - Il Relying Party riceve e valida la risposta con i valori ``state`` e ``nonce``.
  * - RPR-13
    - Risposta di Autorizzazione
    - Verifica la cifratura della risposta.
    - Il Relying Party valuta la risposta cifrata usando la propria chiave pubblica (una delle sue chiavi).
  * - RPR-14
    - Gestione Errori
    - Test della gestione di un oggetto Request non valido.
    - Viene inviata una risposta di errore.
  * - RPR-15
    - Gestione Errori
    - Verifica la registrazione degli errori.
    - Gli errori vengono registrati correttamente.
  * - RPR-16
    - Gestione Errori
    - Test del recupero da errore nella richiesta di autorizzazione.
    - Il Relying Party invita l’utente a riprovare o a scansionare un nuovo QR code.
  * - RPR-17
    - Gestione Errori
    - Test di un cookie HTTP falso.
    - Il Relying Party verifica la coerenza della sessione utente accoppiando il cookie http di sessione con state e nonce forniti.
  * - RPR-19
    - Redirect URI
    - Test del reindirizzamento all’endpoint del Relying Party.
    - L’utente viene reindirizzato correttamente, l’endpoint funziona.
  * - RPR-20
    - Redirect URI
    - Verifica la gestione di un `redirect_uri` non valido.
    - Viene restituita una risposta di errore.
  * - RPR-23
    - Presentazione Credenziali
    - Verifica la conformità del formato della risposta.
    - Il Relying Party supporta tutti i formati di credenziali inclusi nel parametro ``vp_formats_supported`` dei suoi metadati.
  * - RPR-24
    - Risposta di Autorizzazione
    - Test della gestione dei timeout di risposta.
    - I tentativi devono avere successo a meno che non venga acquisita la risposta.
  * - RPR-25
    - Gestione Errori
    - Verifica la gestione di claim malformati nel payload della presentazione.
    - Viene inviata una risposta di errore di autorizzazione.
  * - RPR-26
    - Gestione Errori
    - Verifica la gestione di claim malformati nelle credenziali presentate.
    - Viene inviata una risposta di errore di autorizzazione.
  * - RPR-27
    - Gestione Errori
    - Test della gestione di richieste scadute.
    - Il titolare viene informato della scadenza.
  * - RPR-28
    - Risposta del Relying Party
    - Verifica l’inclusione del codice di risposta.
    - Il codice di risposta è crittograficamente casuale.
  * - RPR-29
    - Risposta del Relying Party
    - Test della gestione di codici di risposta non validi.
    - Viene restituita una risposta di errore.
  * - RPR-30
    - Endpoint di Stato
    - Verifica la gestione di accessi non autorizzati.
    - L’accesso non autorizzato viene negato.
  * - RPR-31
    - Endpoint di Stato
    - Test della gestione di ID di sessione non validi.
    - Viene restituita una risposta di errore.
  * - RPR-32
    - Redirect URI
    - Verifica la gestione di sessioni scadute.
    - Viene restituita una risposta di errore.
  * - RPR-33
    - Redirect URI
    - Test della gestione di errori del server.
    - Viene restituita una risposta di errore.
  * - RPR-34
    - Flusso stesso e tra dispositivi
    - Verifica la gestione di condizioni di rete lente.
    - Il Relying Party fornisce la risposta http entro il limite massimo di 2 secondi.
  * - RPR-36
    - Risposta di Presentazione
    - Verifica la gestione di payload di risposta di grandi dimensioni.
    - La risposta viene valutata entro soglie di sicurezza appropriate.
  * - RPR-37
    - Risposta di Presentazione
    - Test della gestione di errori di cifratura della risposta.
    - Viene restituita una risposta di errore.
  * - RPR-38
    - Gestione Errori
    - Verifica la gestione di firme non valide.
    - Viene inviata una risposta di errore di autorizzazione.
  * - RPR-39
    - Gestione Errori
    - Test della gestione di valori nonce non validi.
    - Viene restituita una risposta di errore.
  * - RPR-40
    - Risposta del Relying Party
    - Verifica la gestione di risposte malformate.
    - Viene restituita una risposta di errore.
  * - RPR-41
    - Risposta del Relying Party
    - Test della gestione di parametri di risposta mancanti.
    - Viene restituita una risposta di errore.
  * - RPR-42
    - Endpoint di Stato
    - Verifica la gestione dei timeout di sessione.
    - Viene restituita una risposta di errore.
  * - RPR-43
    - Endpoint di Stato
    - Test della gestione di codici di stato non validi.
    - Viene restituita una risposta di errore.
  * - RPR-44
    - Redirect URI
    - Verifica la gestione di sessioni utente non valide.
    - Viene restituita una risposta di errore.
  * - RPR-45
    - Redirect URI
    - Test della gestione di servizi non disponibili.
    - Viene restituita una risposta di errore.
  * - RPR-46
    - Flusso stesso dispositivo
    - Verifica la gestione delle cancellazioni da parte dell’utente.
    - L’utente può annullare il processo.
  * - RPR-47
    - Flusso tra dispositivi
    - Test della scansione del QR Code con app diverse.
    - Il QR Code viene scansionato con successo.
  * - RPR-48
    - Flusso tra dispositivi
    - Verifica la scansione del QR Code con illuminazione diversa.
    - Il QR Code viene scansionato con successo.
  * - RPR-49
    - Metodo request_uri
    - Test della gestione di content type non supportati.
    - Viene restituita una risposta di errore.
  * - RPR-50
    - Consenso Utente
    - Verifica la notifica all’utente delle modifiche al consenso.
    - L’utente viene informato delle modifiche al consenso.
  * - RPR-51
    - Consenso Utente
    - Test del consenso dell’utente per dati sensibili.
    - L’utente può acconsentire ai dati sensibili.
  * - RPR-52
    - Risposta di Autorizzazione
    - Verifica la gestione di errori di decifratura della risposta.
    - Viene restituita una risposta di errore.
  * - RPR-53
    - Risposta di Autorizzazione
    - Test della verifica dell’integrità della risposta.
    - L’integrità della risposta è verificata.
  * - RPR-54
    - Risposta del Relying Party
    - Verifica la gestione di errori di validazione della risposta.
    - Viene restituita una risposta di errore.
  * - RPR-55
    - Risposta del Relying Party
    - Test della gestione di errori di elaborazione della risposta.
    - Viene restituita una risposta di errore.
  * - RPR-56
    - Endpoint Risorsa Protetta
    - Verifica la gestione di accessi di sessione non autorizzati.
    - L’accesso non autorizzato viene negato.
  * - RPR-57
    - Redirect URI
    - Verifica la gestione di parametri di redirect non validi.
    - Viene restituita una risposta di errore.
  * - RPR-58
    - Redirect URI
    - Test della gestione di errori di redirect.
    - Viene restituita una risposta di errore.
  * - RPR-59
    - Flusso stesso dispositivo
    - Verifica la gestione di interruzioni da parte dell’utente.
    - L’utente può riprendere o annullare il processo.
  * - RPR-60
    - Metodo request_uri
    - Test della gestione di metodi HTTP non validi.
    - Viene restituita una risposta di errore.
  * - RPR-61
    - Consenso Utente
    - Verifica la notifica all’utente della revoca del consenso.
    - L’utente viene informato della revoca del consenso.
  * - RPR-62
    - Consenso Utente
    - Test del consenso dell’utente per dati opzionali.
    - L’utente può acconsentire ai dati opzionali.
  * - RPR-63
    - Risposta di Autorizzazione
    - Verifica la gestione di errori di firma della risposta.
    - Viene restituita una risposta di errore.
  * - RPR-64
    - Risposta di Autorizzazione
    - Test della gestione di errori di formato della risposta.
    - Viene restituita una risposta di errore.
  * - RPR-65
    - Gestione Errori
    - Verifica la gestione di firme JWT non valide.
    - Viene inviata una risposta di errore di autorizzazione.
  * - RPR-66
    - Gestione Errori
    - Test della gestione di claim JWT non validi.
    - Viene restituita una risposta di errore.
  * - RPR-67
    - Risposta del Relying Party
    - Verifica la gestione di errori di parsing della risposta.
    - Viene restituita una risposta di errore.
  * - RPR-68
    - Risposta del Relying Party
    - Test della gestione di errori di timeout della risposta.
    - Viene restituita una risposta di errore.
  * - RPR-69
    - Endpoint di Stato
    - Verifica la gestione della scadenza della sessione.
    - Viene restituita una risposta di errore.
  * - RPR-70
    - Endpoint di Stato
    - Test della gestione di errori di rinnovo della sessione.
    - Viene restituita una risposta di errore.
  * - RPR-71
    - Redirect URI
    - Verifica la gestione di errori di loop di redirect.
    - Viene restituita una risposta di errore.
  * - RPR-72
    - Redirect URI
    - Test della gestione di errori di sicurezza nel redirect.
    - Viene restituita una risposta di errore.
  * - RPR-73
    - Flusso stesso dispositivo
    - Verifica la gestione dei timeout utente.
    - L’utente viene informato del timeout.
  * - RPR-74
    - Flusso tra dispositivi
    - Test della scansione del QR Code con dispositivi diversi.
    - Il QR Code viene scansionato con successo.
  * - RPR-75
    - Flusso tra dispositivi
    - Verifica la scansione del QR Code con app diverse.
    - Il QR Code viene scansionato con successo.
  * - RPR-76
    - Metodo request_uri
    - Test della gestione di metodi HTTP non supportati.
    - Viene restituita una risposta di errore.

  * - RPR-77
    - Generazione QR Code
    - Verifica che il livello di correzione degli errori del QR Code sia Q (Quartile - fino al 25%).
    - Il QR Code utilizza il livello di correzione Q richiesto.

  * - RPR-78
    - Richiesta Attestazione Wallet
    - Test che la richiesta di Attestazione Wallet utilizzi la query DCQL standard.
    - La richiesta di Attestazione Wallet utilizza correttamente la query DCQL standard.

  * - RPR-79
    - Richiesta Attestazione Wallet
    - Verifica che il parametro ``claims`` non sia incluso nella query DCQL per l’Attestazione Wallet.
    - Il parametro ``claims`` non è incluso nella query DCQL per l’Attestazione Wallet.

  * - RPR-80
    - Richiesta Attestazione Wallet
    - Test che il parametro ``vct_values`` sia richiesto nella query DCQL per l’Attestazione Wallet.
    - Il parametro ``vct_values`` è correttamente richiesto nella query DCQL.

  * - RPR-81
    - Wallet Nonce
    - Test che il Relying Party controlli ``wallet_nonce`` quando presente.
    - Il Relying Party controlla correttamente ``wallet_nonce`` quando presente.

  * - RPR-82
    - Tipi di Risposta
    - Verifica che ``response_types_supported`` sia impostato a ``vp_token`` quando presente.
    - ``response_types_supported`` è correttamente impostato a ``vp_token``.

  * - RPR-83
    - Redirect URI
    - Test che il Relying Party fornisca correttamente il parametro ``redirect_uri`` all’istanza Wallet.
    - Il Relying Party fornisce e gestisce correttamente ``redirect_uri``.

  * - RPR-84
    - Supporto Flussi
    - Test che il Relying Party supporti i flussi remoti richiesti.
    - Il Relying Party supporta sia il flusso stesso dispositivo che tra dispositivi.

  * - RPR-85
    - Sicurezza Endpoint
    - Test che ``request_uri`` sia attestato da una terza parte fidata.
    - Il parametro ``request_uri`` è correttamente attestato da una terza parte fidata.

  * - RPR-86
    - Protezione della Privacy
    - Test che il Relying Party validi correttamente i metadati dell’istanza Wallet senza informazioni utente.
    - Il Relying Party valuta correttamente le capacità tecniche dell’istanza Wallet.

  * - RPR-87
    - Metodo POST request_uri
    - Test che il Relying Party supporti la ricezione dei metadati dell’istanza Wallet via POST all’endpoint ``request_uri`` con content type ``application/x-www-form-urlencoded``.
    - Il Relying Party accetta e processa correttamente i metadati dell’istanza Wallet inviati via POST con il content type richiesto.

  * - RPR-88
    - Validazione Algoritmo
    - Test che l’algoritmo JWT sia supportato e non sia ``none`` o MAC.
    - L’algoritmo JWT è tra quelli supportati e non è ``none`` o un identificatore MAC.

  * - RPR-89
    - Validazione Media Type
    - Test che JWT typ sia impostato a ``oauth-authz-req+jwt``.
    - Il parametro typ di JWT è correttamente impostato a ``oauth-authz-req+jwt``.

  * - RPR-90
    - Validazione Response Mode
    - Test che ``response_mode`` sia impostato a ``direct_post.jwt``.
    - Il parametro ``response_mode`` è correttamente impostato a ``direct_post.jwt``.

  * - RPR-91
    - Validazione Response Type
    - Test che ``response_type`` sia impostato a ``vp_token``.
    - Il parametro ``response_type`` è correttamente impostato a ``vp_token``.

  * - RPR-92
    - Uso di Response URI
    - Test che il Relying Party fornisca correttamente il parametro ``response_uri`` all’istanza Wallet.
    - Il Relying Party invia la risposta di autorizzazione al corretto endpoint ``response_uri``.

  * - RPR-93
    - Entropia del Nonce
    - Test che il nonce abbia sufficiente entropia (32+ cifre).
    - Il parametro nonce ha sufficiente entropia con almeno 32 cifre.

  * - RPR-94
    - Scadenza JWT
    - Test che il parametro ``exp`` di JWT sia impostato correttamente.
    - Il parametro ``exp`` di JWT è correttamente impostato e non scaduto.

  * - RPR-95
    - Sicurezza Response URI
    - Test che ``response_uri`` sia attestato da una terza parte fidata.
    - Il parametro ``response_uri`` è correttamente attestato da una terza parte fidata.

  * - RPR-96
    - Gestione Client Metadata
    - Test che il Relying Party gestisca correttamente il ``client_metadata`` dell’istanza Wallet.
    - Il ``client_metadata`` è correttamente allineato con i metadati della Trust Chain.

  * - RPR-97
    - Richiesta Attestazione Wallet
    - Test che il Relying Party richieda l’Attestazione Wallet tramite DCQL.
    - Il Relying Party richiede correttamente l’Attestazione Wallet usando la query DCQL.

  * - RPR-98
    - Formato Risposta di Errore
    - Test che la risposta di errore utilizzi il content type ``application/json``.
    - La risposta di errore utilizza correttamente il content type ``application/json``.

  * - RPR-99
    - Parametri Risposta di Errore
    - Test che la risposta di errore includa i parametri richiesti.
    - La risposta di errore include i parametri error ed ``error_description``.

  * - RPR-100
    - Presentazione Attestazione Wallet
    - Test che il Relying Party richieda correttamente l’Attestazione Wallet all’istanza Wallet.
    - Il Relying Party valuta correttamente l’Attestazione Wallet quando richiesta.

  * - RPR-101
    - Array Presentazione
    - Test che ``vp_token`` contenga le presentazioni firmate richieste.
    - ``vp_token`` contiene le presentazioni firmate richieste come previsto.

  * - RPR-102
    - Inclusione KB-JWT
    - Test che il Titolare includa KB-JWT in SD-JWT.
    - Il Titolare include correttamente KB-JWT nella presentazione SD-JWT.

  * - RPR-103
    - Validazione KB-JWT
    - Test che il Relying Party validi la firma KB-JWT.
    - Il Relying Party valida correttamente la firma KB-JWT usando la chiave pubblica.

  * - RPR-104
    - Header KB-JWT
    - Test che KB-JWT contenga i parametri header richiesti.
    - KB-JWT contiene i parametri header ``typ`` e ``alg`` richiesti.

  * - RPR-105
    - Payload KB-JWT
    - Test che KB-JWT contenga i parametri payload richiesti.
    - KB-JWT contiene i parametri ``iat``, ``aud``, ``nonce`` e ``sd_hash`` richiesti.

  * - RPR-106
    - Audience KB-JWT
    - Test che ``aud`` di KB-JWT corrisponda all’identificativo del Relying Party.
    - Il parametro ``aud`` di KB-JWT corrisponde all’identificativo univoco del Relying Party.

  * - RPR-107
    - Nonce KB-JWT
    - Test che ``nonce`` di KB-JWT corrisponda al ``nonce`` dell’oggetto request.
    - Il parametro ``nonce`` di KB-JWT corrisponde al ``nonce`` dell’oggetto request.

  * - RPR-108
    - Risposta di Errore di Autorizzazione
    - Test che il Relying Party gestisca correttamente la risposta di errore di autorizzazione dell’istanza Wallet in caso di fallimento della validazione.
    - Il Relying Party valuta correttamente la risposta di errore di autorizzazione quando la validazione fallisce.

  * - RPR-109
    - Codifica Risposta di Errore
    - Test che la risposta di errore di autorizzazione sia codificata correttamente.
    - La risposta di errore di autorizzazione è codificata in formato ``application/x-www-form-urlencoded``.

  * - RPR-110
    - Elaborazione Risposta
    - Test che la Response URI restituisca HTTP 200 in caso di elaborazione corretta.
    - La Response URI restituisce HTTP 200 con content type ``application/json``.

  * - RPR-111
    - Coerenza Codici di Errore
    - Test che i codici di errore siano coerenti tra i diversi endpoint.
    - I codici di errore sono coerenti su tutti gli endpoint del Relying Party.

  * - RPR-112
    - Inclusione Codice di Risposta
    - Test che il Relying Party includa il codice di risposta in ``redirect_uri``.
    - Il Relying Party include un nuovo codice di risposta in ``redirect_uri``.

  * - RPR-113
    - Sicurezza Redirect URI
    - Test che ``redirect_uri`` sia attestato da una terza parte fidata.
    - Il parametro ``redirect_uri`` è correttamente attestato da una terza parte fidata.

  * - RPR-114
    - Risposta di Errore di Validazione
    - Test che la Response URI restituisca una risposta di errore in caso di fallimento della validazione.
    - La Response URI restituisce una risposta di errore quando i controlli di validazione falliscono.

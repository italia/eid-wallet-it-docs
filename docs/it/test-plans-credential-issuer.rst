Matrice dei Test per il Credential Issuer
-----------------------------------------

Questa sezione fornisce l'insieme dei test progettati per implementatori tecnici e team di sviluppo responsabili della creazione e del deployment di soluzioni Credential Issuer. È anche destinata agli organismi di valutazione che ispezionano e validano le implementazioni di soluzioni Credential Issuer.



.. list-table::
  :class: longtable
  :widths: 15 15 35 35
  :header-rows: 1

  * - ID
    - Scopo
    - Descrizione
    - Risultato Atteso
  * - CI_001
    - Trust, Sicurezza
    - Pubblicazione della Entity Configuration
    - L'entità di federazione pubblica la propria Entity Configuration nell’endpoint .well-known/openid-federation.
  * - CI_002
    - Trust, Interoperabilità
    - Verifica del media type della Entity Configuration
    - La risposta HTTP della Entity Configuration è impostata sul media type application/entity-statement+jwt.
  * - CI_003
    - Trust, Sicurezza
    - Crittografia della Entity Configuration
    - La Entity Configuration è firmata crittograficamente.
  * - CI_004
    - Trust, Sicurezza
    - Inclusione della Chiave Pubblica nella Entity Configuration e nella Subordinate Statement
    - La Entity Configuration e la Subordinate Statement emessa dall’entità superiore immediata includono entrambe la parte pubblica della chiave.
  * - CI_005
    - Trust, Sicurezza
    - Trust Mark nella Entity Configuration
    - La Entity Configuration contiene uno o più Trust Mark.
  * - CI_006
    - Trust, Interoperabilità
    - Parametri delle Entity Configuration
    - Le Entity Configuration hanno in comune i seguenti parametri: iss, sub, iat, exp, jwks, metadata.
  * - CI_007
    - Trust, Sicurezza
    - Scoperta del Credential Issuer
    - Il Credential Issuer espone un endpoint well-known che ospita la sua Entity Configuration.
  * - CI_008
    - Trust, Interoperabilità
    - Metadata del Credential Issuer
    - Il Credential Issuer fornisce correttamente i seguenti tipi di metadata: federation_entity, oauth_authorization_server e openVCI_credential_issuer.
  * - CI_009
    - Trust, Interoperabilità
    - Inclusione dei Metadata openVCI_credential_verifier nell’Autenticazione Utente tramite Wallet
    - Quando i Fornitori di Attestati Elettronici di Attributi (Qualificati) autenticano gli utenti tramite la loro Istanza Wallet, i metadata openVCI_credential_verifier sono inclusi oltre ai parametri metadata obbligatori.
  * - CI_010
    - Emissione, Interoperabilità
    - Struttura della URI della Credential Offer
    - Il Credential Issuer genera una Credential Offer composta da un singolo parametro URI di query chiamato "credential_offer", garantendo che l’URL sia ben formato e contenga solo questo parametro per i dati dell’offerta.
  * - CI_011
    - Emissione, Interoperabilità
    - Metodi di Consegna della Credential Offer
    - L’URL della Credential Offer è incorporato con successo in codici QR o incluso come pulsante cliccabile href in pagine HTML.
  * - CI_012
    - Emissione, Interoperabilità
    - Parametri Obbligatori della Credential Offer
    - La Credential Offer contiene tutti e tre i parametri obbligatori (credential_issuer, credential_configuration_ids e grants) con valori validi.
  * - CI_013
    - Emissione, Interoperabilità
    - Struttura del parametro Grants nella Credential Offer
    - Il parametro grants contiene correttamente un oggetto authorization_code che include entrambi i sotto-parametri obbligatori (issuer_state e authorization_server) con valori appropriati.
  * - CI_014
    - Emissione, Interoperabilità
    - Compilazione dell’Oggetto Credential
    - Il Credential Issuer garantisce che l’Oggetto Credential sia compilato correttamente con tutti i campi richiesti, formattazione corretta e strutture dati valide prima della consegna.
  * - CI_015
    - Emissione, Sicurezza
    - Validazione della Firma del Request Object nella PAR
    - Il Credential Issuer valida correttamente la firma del Request Object.
  * - CI_015a
    - Emissione, Sicurezza
    - Elaborazione dell’algoritmo nell’header del Request Object della PAR
    - Il Credential Issuer utilizza l’algoritmo specificato nel parametro di header alg (RFC 9126/9101) per validare la firma del Request Object.
  * - CI_015b
    - Emissione, Sicurezza
    - Recupero della Chiave Pubblica dalla Wallet Attestation nella PAR
    - Il Credential Issuer recupera correttamente la chiave pubblica dal claim cnf.jwk della Wallet Attestation.
  * - CI_015c
    - Emissione, Sicurezza
    - Riferimento al Key Identifier JWT nella PAR
    - Il Credential Issuer fa correttamente riferimento alla chiave giusta tramite il parametro kid nell’header JWT.
  * - CI_015d
    - Emissione, Sicurezza
    - Validazione dell’Integrità della Firma Crittografica nella PAR
    - Il Credential Issuer completa correttamente la validazione dell’integrità della firma crittografica prima di procedere con ulteriori verifiche.
  * - CI_016
    - Emissione, Interoperabilità
    - Codifica dei Parametri HTTP POST nella PAR
    - Il Credential Issuer elabora correttamente le richieste HTTP POST con parametri nel corpo del messaggio codificati in formato application/x-www-form-urlencoded.
  * - CI_017
    - Emissione, Interoperabilità
    - Interpretazione di Scope e Authorization Details nella PAR
    - Quando una richiesta contiene sia il valore scope sia il parametro authorization_details, il Credential Issuer elabora ciascun parametro in modo indipendente.
  * - CI_017a
    - Emissione, Interoperabilità
    - Authorization Details nella PAR
    - Quando sia scope che authorization_details richiedono lo stesso tipo di Credential, il Credential Issuer segue le specifiche fornite dall’oggetto authorization_details.
  * - CI_018
    - Emissione, Sicurezza
    - Validazione della Firma del Request Object nella PAR
    - Il Credential Issuer valida correttamente la firma del Request Object utilizzando l’algoritmo del parametro alg e la chiave pubblica della Wallet Attestation (cnf.jwk, referenziata da kid), confermando l’integrità della firma (RFC 9126/9101).
  * - CI_019
    - Emissione, Sicurezza
    - Verifica di Conformità dell’Algoritmo nella PAR
    - Il Credential Issuer verifica che l’algoritmo di firma nell’header alg corrisponda a uno degli algoritmi approvati nella sezione Algoritmi Crittografici; rifiuta richieste con algoritmi non conformi e restituisce un errore appropriato.
  * - CI_020
    - Emissione, Sicurezza
    - Validazione di Consistenza del Client ID nella PAR
    - Il Credential Issuer conferma che il client_id nel corpo della richiesta PAR corrisponda esattamente al claim client_id nel Request Object; valori non corrispondenti causano il rifiuto con messaggio di errore chiaro.
  * - CI_021
    - Emissione, Sicurezza
    - Corrispondenza Issuer-Client ID nella richiesta PAR
    - Il Credential Issuer valida che il claim iss nel Request Object corrisponda al claim client_id nello stesso Request Object (RFC 9126/9101); discrepanze portano al rifiuto della richiesta.
  * - CI_022
    - Emissione, Sicurezza
    - Verifica dell’Audience Claim nella PAR
    - Il Credential Issuer conferma che il claim aud nel Request Object sia uguale al proprio identificativo (RFC 9126/9101); valori errati comportano il rifiuto immediato.
  * - CI_023
    - Emissione, Sicurezza
    - Rifiuto del parametro Request URI nella PAR
    - Il Credential Issuer rileva e rifiuta qualsiasi richiesta PAR contenente il parametro request_uri (RFC 9126), restituendo un errore che segnala il parametro non supportato.
  * - CI_024
    - Emissione, Sicurezza
    - Validazione dei Parametri Obbligatori nella PAR
    - Il Credential Issuer verifica la presenza di tutti i parametri HTTP obbligatori nel Request Object e valida i loro valori rispetto alle specifiche di tabella definite (RFC 9126); parametri mancanti o non validi causano risposte di errore strutturate.
  * - CI_025
    - Emissione, Sicurezza
    - Controllo della Scadenza del Token nella PAR
    - Il Credential Issuer verifica che il Request Object non sia scaduto controllando il claim exp rispetto al tempo corrente; i token scaduti sono rifiutati con messaggi di errore legati al timestamp.
  * - CI_026
    - Emissione, Sicurezza
    - Validazione del Tempo di Emissione del Token nella PAR
    - Il Credential Issuer conferma che il claim iat rappresenti un timestamp passato.
  * - CI_026a
    - Emissione, Sicurezza
    - Rifiuto Consigliato per Tempo di Emissione Token nella PAR
    - Il Credential Issuer rifiuta richieste in cui iat è superiore a più di 5 minuti dal tempo corrente (RFC 9126); violazioni temporali generano errori "invalid_request".
  * - CI_027
    - Emissione, Sicurezza
    - Prevenzione di Replay Attack nella PAR
    - Il Credential Issuer verifica che il claim jti nel Request Object non sia stato usato prima dall'Istanza Wallet identificata dal client_id.
  * - CI_028
    - Emissione, Sicurezza, Interoperabilità
    - Validazione OAuth Client Attestation PoP
    - Il Credential Issuer valida con successo il parametro OAuth-Client-Attestation-PoP secondo la Sezione 4 di [OAUTH-ATTESTATION-CLIENT-AUTH], confermando la prova di possesso e rifiutando attestazioni non valide con risposte di errore dettagliate.
  * - CI_029
    - Emissione, Fiducia
    - Verifica dell’affidabilità dell’istanza del Wallet
    - Il Credential Issuer verifica con successo l’affidabilità e l’appartenenza indiretta alla Federazione dell’istanza del Wallet attraverso una validazione completa della Wallet Attestation.
  * - CI_030
    - Emissione, Fiducia
    - Validazione dell’appartenenza alla Federazione del Wallet Provider
    - Il Credential Issuer conferma che il Wallet Provider (emittente della Wallet Attestation) è un membro della Federazione riconosciuto e affidabile controllando i registri e le liste di fiducia della Federazione.
  * - CI_031
    - Emissione, Sicurezza
    - Validazione della firma crittografica della Wallet Attestation
    - Il Credential Issuer valida con successo la firma crittografica della Wallet Attestation utilizzando la chiave pubblica del Wallet Provider, garantendo integrità e autenticità della firma.
  * - CI_032
    - Emissione, Sicurezza
    - Controllo della scadenza della Wallet Attestation
    - Il Credential Issuer verifica che la Wallet Attestation non sia scaduta al momento della verifica confrontando i timestamp dichiarati con l’orario corrente.
  * - CI_033
    - Emissione, Sicurezza
    - Accettazione delle chiavi crittografiche attestate nella Wallet Attestation
    - Il Credential Issuer accetta e utilizza solo chiavi crittografiche correttamente derivate dall’istanza del Wallet attestata durante il processo di emissione della credenziale.
  * - CI_034
    - Emissione, Sicurezza
    - Verifica della sicurezza e conformità del dispositivo tramite Wallet Attestation
    - Il Credential Issuer si affida alle dichiarazioni della Wallet Attestation per confermare che l’istanza del Wallet operi su un dispositivo sicuro e affidabile che soddisfi gli standard di sicurezza richiesti dall’Issuer.
  * - CI_035
    - Emissione, Fiducia
    - Valutazione della catena di fiducia del Wallet Provider
    - Il Credential Issuer valuta con successo l’intera catena di fiducia dell’emittente della Wallet Attestation (Wallet Provider).
  * - CI_036
    - Emissione, Fiducia, Interoperabilità
    - Recupero dei metadati della Federazione
    - Il Credential Issuer utilizza con successo gli endpoint API della Federazione (.well-known/openid-federation, /fetch) per recuperare i metadati e le configurazioni aggiornate dei partecipanti alla Federazione, inclusi i Wallet Provider.
  * - CI_037
    - Emissione, Fiducia, Interoperabilità
    - Stabilimento della fiducia nel Wallet Provider
    - Il Credential Issuer stabilisce la fiducia nel Wallet Provider come entità autorizzata della Federazione interrogando gli endpoint API della Federazione (ad es. .well-known/openid-federation, /fetch) e validando lo stato federativo del provider tramite canali ufficiali e processi di verifica della fiducia.
  * - CI_038
    - Emissione, Interoperabilità
    - Fornitura di un URI di richiesta monouso nella risposta PAR
    - Il Credential Issuer genera e fornisce un valore request_uri univoco e utilizzabile una sola volta.
  * - CI_039
    - Emissione, Sicurezza
    - Associazione crittografica del request_uri al client nella risposta PAR
    - Il valore request_uri emesso è crittograficamente vincolato allo specifico client_id fornito nell’oggetto di richiesta.
  * - CI_040
    - Emissione, Sicurezza
    - Durata consigliata di validità del request_uri nella risposta PAR
    - Il tempo di validità del request_uri è impostato a meno di un minuto.
  * - CI_041
    - Emissione, Sicurezza
    - Integrazione di un valore casuale crittografico nella risposta PAR
    - Il request_uri generato include un valore casuale crittografico di almeno 128 bit.
  * - CI_042
    - Emissione, Sicurezza
    - Limitazione consigliata della lunghezza del request_uri nella risposta PAR
    - Il request_uri completo non supera i 512 caratteri ASCII.
  * - CI_043
    - Emissione, Interoperabilità
    - Risposta di verifica positiva della risposta PAR
    - Quando la verifica ha successo, il Credential Issuer restituisce una risposta HTTP con codice di stato 201.
  * - CI_044
    - Emissione, Interoperabilità
    - Struttura JSON della risposta PAR
    - Il corpo del messaggio di risposta HTTP utilizza il tipo media application/json (RFC 8259) e include i parametri richiesti di livello superiore.
  * - CI_044a
    - Emissione, Sicurezza
    - Parametro request_uri nella risposta PAR
    - La risposta HTTP include il parametro request_uri contenente l’URI di autorizzazione generato e utilizzabile una sola volta.
  * - CI_044b
    - Emissione, Sicurezza
    - Parametro expires_in nella risposta PAR
    - La risposta HTTP include il parametro expires_in che specifica la durata di validità in secondi.
  * - CI_045
    - Emissione, Interoperabilità
    - Tabella dei codici di stato HTTP per la risposta PAR
    - Quando l’elaborazione della richiesta PAR incontra errori, il Credential Issuer risponde come definito in RFC 9126, secondo i codici di stato HTTP.
  * - CI_046
    - Emissione, Sicurezza e Privacy
    - Verifica dell’identità dell’utente durante la richiesta di autorizzazione
    - L’Authorization Server verifica con successo l’identità dell’utente proprietario della credenziale tramite meccanismi di autenticazione appropriati, confermando la titolarità prima di procedere con l’autorizzazione della credenziale.
  * - CI_047
    - Emissione, Sicurezza
    - Monouso e scadenza del request_uri nella richiesta di autorizzazione
    - Il Credential Issuer tratta ogni valore request_uri come a utilizzo singolo e rifiuta con successo tutte le richieste scadute.
  * - CI_048
    - Emissione, Sicurezza
    - Tolleranza opzionale per richieste duplicate nella richiesta di autorizzazione
    - Il Credential Issuer consente richieste duplicate quando derivano da ricaricamento o aggiornamento del user-agent da parte dell’utente (derivato da RFC 9126).
  * - CI_049
    - Emissione, Sicurezza
    - Identificazione della richiesta PAR nella richiesta di autorizzazione
    - Il Credential Issuer identifica e correla con successo ogni richiesta di autorizzazione come risultato diretto di una PAR precedentemente inviata (derivato da RFC 9126).
  * - CI_050
    - Emissione, Sicurezza
    - Obbligatorietà del parametro request_uri nella richiesta di autorizzazione
    - Il Credential Issuer rifiuta tutte le richieste di autorizzazione che non contengono il parametro request_uri, poiché la PAR è l’unico metodo per trasmettere richieste di autorizzazione dall’istanza del Wallet (derivato da RFC 9126).
  * - CI_051
    - Emissione, Sicurezza
    - Autenticazione ad alto livello CieID
    - Il PID Provider esegue con successo l’autenticazione dell’utente basata sullo schema CieID con LoAHigh (CIE L3).
  * - CI_052
    - Emissione, Sicurezza e Privacy
    - Consenso dell’utente per l’emissione del PID
    - Il PID Provider ottiene il consenso esplicito dell’utente prima di procedere con l’emissione del PID.
  * - CI_053
    - Emissione, Privacy
    - Raccolta opzionale dei dati di contatto
    - Il PID Provider PUÒ richiedere i dati di contatto dell’utente (email, numero di telefono) per l’invio di notifiche relative al PID emesso.
  * - CI_054
    - Presentazione, Sicurezza di emissione
    - Autenticazione utente basata su PID
    - Il (Q)EAA Provider esegue con successo l’autenticazione dell’utente richiedendo e validando un PID valido dall’istanza del Wallet.
  * - CI_055
    - Presentazione, Emissione, Interoperabilità
    - Utilizzo del protocollo OpenID4VP
    - Il (Q)EAA Provider utilizza il protocollo OpenID4VP per richiedere la presentazione del PID dall’istanza del Wallet.
  * - CI_056
    - Presentazione, Emissione, Sicurezza
    - Consegna della richiesta di presentazione
    - Il (Q)EAA Provider fornisce con successo la richiesta di presentazione al Wallet.
  * - CI_057
    - Emissione, Privacy
    - Raccolta opzionale dei dati di contatto per le credenziali
    - I Credential Issuer richiedono i dati di contatto dell’utente (email, numero di telefono) per l’invio di notifiche relative alle credenziali digitali emesse.
  * - CI_058
    - Emissione, Interoperabilità
    - Validazione dei parametri della risposta di autorizzazione
    - Il Credential Issuer invia con successo una risposta con codice di autorizzazione all’istanza del Wallet che include tutti e tre i parametri richiesti.
  * - CI_058a
    - Emissione, Sicurezza
    - Validazione del parametro code nella risposta di autorizzazione
    - La risposta con codice di autorizzazione include il parametro code.
  * - CI_058b
    - Emissione, Sicurezza
    - Validazione del parametro state nella risposta di autorizzazione
    - La risposta con codice di autorizzazione include il parametro state corrispondente alla richiesta originale.
  * - CI_058c
    - Emissione, Sicurezza
    - Validazione del parametro iss nella risposta di autorizzazione
    - La risposta con codice di autorizzazione include il parametro iss che identifica l’issuer.
  * - CI_059
    - Emissione, Interoperabilità
    - Tabella dei codici di stato HTTP della risposta di autorizzazione
    - Quando la risposta di autorizzazione incontra errori, l’Authorization Server reindirizza l’utente alla redirect_uri con codice di stato HTTP 302 secondo la tabella dei codici di stato HTTP.
  * - CI_060
    - Emissione, Sicurezza
    - Verifica dell’emissione del codice di autorizzazione nella richiesta di token
    - Il Credential Issuer garantisce che il codice di autorizzazione sia emesso all’istanza del Wallet autenticata (RFC 6749) e che non sia stato riutilizzato.
  * - CI_061
    - Emissione, Sicurezza
    - Verifica di validità e utilizzo del Codice di Autorizzazione nella Richiesta di Token
    - Il Credential Issuer verifica che il codice di autorizzazione sia valido e non sia stato precedentemente utilizzato (RFC 6749).
  * - CI_062
    - Emissione, Sicurezza
    - Validazione della corrispondenza del Redirect URI nella Richiesta di Token
    - Il Credential Issuer conferma che il redirect_uri corrisponda esattamente al valore incluso nel precedente Request Object (vedi Sezione 3.1.3.1 di [OIDC]).
  * - CI_063
    - Emissione, Sicurezza
    - Validazione del DPoP Proof JWT nella Richiesta di Token
    - Il Credential Issuer valida correttamente il DPoP Proof JWT secondo la Sezione 4.3 di (RFC 9449).
  * - CI_064
    - Emissione, Interoperabilità
    - Fornitura dell’Access Token nella risposta di Token
    - Il Credential Issuer fornisce al Wallet Instance un Access Token valido dopo un’autorizzazione avvenuta con successo.
  * - CI_065
    - Emissione, Interoperabilità
    - Fornitura opzionale di Refresh Token
    - Se supportato dal Credential Issuer, viene fornito al Wallet Instance un Refresh Token.
  * - CI_066
    - Emissione, Sicurezza
    - Binding crittografico di Access Token e Refresh Token alla chiave DPoP
    - Sia l’Access Token che il Refresh Token (se emesso) sono crittograficamente vincolati alla chiave DPoP.
  * - CI_067
    - Emissione, Interoperabilità
    - Tabella dei Codici di Stato HTTP per le risposte di Token
    - In caso di errori durante la validazione della Richiesta di Token, l’Authorization Server restituisce una risposta di errore come definito in RFC 6749, in accordo con la Tabella dei Codici di Stato HTTP.
  * - CI_068
    - Emissione, Interoperabilità
    - Fornitura di c_nonce
    - Il Credential Issuer fornisce un valore c_nonce al Wallet Instance.
  * - CI_069
    - Emissione, Sicurezza
    - Formato e Sicurezza del c_nonce
    - Il parametro c_nonce è fornito come stringa con sufficiente imprevedibilità per prevenire attacchi di guessing e funge da sfida crittografica che il Wallet Instance utilizza per creare la prova di possesso della chiave (proof claim).
  * - CI_070
    - Emissione, Sicurezza
    - Riutilizzo e rinnovo del c_nonce
    - Il valore c_nonce ricevuto può essere riutilizzato dal Wallet Instance per creare più proof finché il Credential Issuer non ne fornisce uno nuovo.
  * - CI_071
    - Emissione, Interoperabilità
    - Validazione delle Claim obbligatorie nel JWT Proof
    - Il JWT proof include correttamente tutte le claim obbligatorie come specificato nella tabella della Richiesta di Token.
  * - CI_072
    - Emissione, Sicurezza
    - Validazione delle Claim obbligatorie nel JWT Proof per emissione in batch
    - Il Credential Issuer verifica correttamente che l’attributo jwk in ogni key proof sia univoco.
  * - CI_073
    - Emissione, Interoperabilità
    - Dichiarazione del tipo di Key Proof nella Richiesta di Credenziale
    - Il key proof contiene i parametri di header appropriati definiti per il rispettivo tipo di proof.
  * - CI_074
    - Emissione, Sicurezza
    - Obbligo di algoritmo asimmetrico nella Richiesta di Credenziale
    - Il parametro di header alg indica un algoritmo di firma digitale asimmetrico registrato e non è mai impostato su none.
  * - CI_075
    - Emissione, Sicurezza
    - Verifica della firma della chiave pubblica nella Richiesta di Credenziale
    - La firma sul key proof viene verificata correttamente utilizzando la chiave pubblica specificata nel parametro di header.
  * - CI_076
    - Emissione, Sicurezza
    - Esclusione della chiave privata negli header della Richiesta di Credenziale
    - I parametri di header non contengono alcun materiale di chiave privata.
  * - CI_077
    - Emissione, Sicurezza
    - Corrispondenza del c_nonce nella Richiesta di Credenziale
    - Quando un valore c_nonce è stato precedentemente fornito dal server, la claim nonce nel JWT corrisponde esattamente a questo valore.
  * - CI_078
    - Emissione, Sicurezza
    - Validità temporale del JWT nella Richiesta di Credenziale
    - Il tempo di creazione del JWT (tramite claim iat o timestamp gestito dal server attraverso la claim nonce) rientra nella finestra temporale accettabile dal server.
  * - CI_079
    - Emissione, Interoperabilità
    - Registrazione delle Credenziali emesse per revoca
    - Il Credential Issuer registra tutte le Credenziali emesse in un registro di revoca per eventuali necessità future.
  * - CI_080
    - Emissione, Interoperabilità
    - Generazione raccomandata di nuove chiavi crittografiche nella Richiesta di Credenziale
    - È raccomandato che vengano generate nuove chiavi crittografiche per la Richiesta di Credenziale.
  * - CI_081
    - Emissione, Sicurezza
    - Supporto raccomandato al Deferred Flow
    - Quando la Credenziale richiesta non può essere emessa immediatamente e richiede più tempo, il Credential Issuer supporta il Deferred Flow.
  * - CI_081a
    - Emissione, Sicurezza
    - Coerenza nell’emissione batch con Deferred Flow
    - Quando si utilizza il Deferred Flow per l’emissione batch, lo stesso transaction_id consente il recupero di tutte le Credenziali richieste nel batch.
  * - CI_082
    - Emissione, Sicurezza
    - Validazione del DPoP JWT Proof e dell’Access Token nella Risposta di Credenziale
    - Il Credential Issuer valida correttamente il DPoP JWT Proof secondo le procedure della Sezione 4.3 di (RFC 9449) e conferma che l’Access Token sia valido e idoneo per la Credenziale richiesta.
  * - CI_083
    - Emissione, Sicurezza
    - Validazione della prova di possesso del materiale crittografico nella Risposta di Credenziale
    - Il Credential Issuer valida la prova di possesso della chiave alla quale sarà vincolata la nuova Credenziale, secondo la Sezione 8.2.2 di OpenID4VCI.
  * - CI_084
    - Emissione, Sicurezza
    - Creazione e Binding della Credenziale nella Risposta
    - Quando tutte le validazioni hanno esito positivo, il Credential Issuer crea una nuova Credenziale crittograficamente vincolata al materiale di chiave validato e la fornisce al Wallet Instance.
  * - CI_084a
    - Emissione, Sicurezza
    - Controllo del tipo di Credenziale
    - Il Credential Issuer garantisce che il tipo di Credenziale corrisponda a quello richiesto prima dell’emissione.
  * - CI_085
    - Emissione, Interoperabilità
    - Tabella dei Codici di Stato HTTP per la Risposta di Credenziale
    - Quando la Richiesta di Credenziale non contiene un Access Token valido, il Credential Endpoint restituisce una risposta di errore come definito nella Sezione 3 di [RFC 6750], in accordo con la Tabella dei Codici di Stato HTTP.
  * - CI_086
    - Emissione, Interoperabilità
    - Notification ID unificato per operazioni batch
    - Per le Credenziali Digitali emesse in batch, un unico notification_id copre l’intero set emesso. La risposta di notifica si applica a tutte le Credenziali: qualsiasi fallimento parziale è trattato come fallimento dell’intero batch.
  * - CI_087
    - Emissione, Interoperabilità
    - Tabella dei Codici di Stato HTTP per la Risposta di Notifica
    - Quando la Richiesta di Notifica non contiene un Access Token valido, il Notification Endpoint restituisce una risposta di errore come definito nella Sezione 3 di [RFC 6750], in accordo con la Tabella dei Codici di Stato HTTP.
  * - CI_088
    - Emissione, Sicurezza
    - Restrizione dello scope dell’Access Token
    - L’Access Token ottenuto tramite Refresh Token è limitato a tre endpoint specifici: Deferred endpoint, Notification endpoint e Credential endpoint.
  * - CI_088a
    - Emissione, Sicurezza
    - Autorizzazione di accesso al Deferred Endpoint
    - L’Access Token consente l’accesso al Deferred endpoint per ottenere nuove Credenziali Digitali dopo il lead_time o la notifica di readiness.
  * - CI_088b
    - Emissione, Sicurezza
    - Autorizzazione di accesso al Notification Endpoint
    - L’Access Token consente l’accesso al Notification endpoint per notificare l’eliminazione di una Credenziale Digitale al Credential Issuer.
  * - CI_089c
    - Emissione, Sicurezza
    - Autorizzazione di accesso al Credential Endpoint
    - L’Access Token consente l’accesso al Credential endpoint per il rinnovo/re-emissione di Credenziali Digitali esistenti.
  * - CI_090
    - Emissione, Sicurezza
    - Sicurezza del Refresh Token vincolato a DPoP
    - I Refresh Token sono vincolati alle chiavi DPoP per mitigare l’impatto di un furto di token.
  * - CI_091
    - Emissione, Interoperabilità
    - Validazione dell’OAuth Client Attestation PoP per il Refresh
    - Il Credential Issuer valida correttamente il parametro OAuth-Client-Attestation-PoP secondo la Sezione 4 di [OAUTH-ATTESTATION-CLIENT-AUTH].
  * - CI_092
    - Emissione, Sicurezza
    - Validazione del DPoP Proof JWT per il Refresh
    - Il Credential Issuer valida il DPoP Proof JWT secondo la Sezione 4.3 di (RFC 9449).
  * - CI_093
    - Emissione, Sicurezza
    - Controllo di validità e binding del Refresh Token
    - Il Credential Issuer verifica che il Refresh Token non sia scaduto, non sia stato revocato e sia vincolato alle stesse chiavi DPoP usate nel DPoP Proof JWT.
  * - CI_094
    - Emissione, Sicurezza
    - Generazione e Binding dell’Access Token
    - Quando tutte le verifiche hanno esito positivo, il Credential Issuer genera un nuovo Access Token e un nuovo Refresh Token, entrambi vincolati alla chiave DPoP.
  * - CI_095
    - Emissione, Sicurezza
    - Risposta positiva con Refresh Token
    - Sia l’Access Token che il Refresh Token sono inviati al Wallet Instance.
  * - CI_096
    - Emissione, Sicurezza
    - Gestione errori per Refresh Token non valido
    - Quando il Refresh Token è scaduto o non valido, il Credential Issuer restituisce una risposta di errore con il tipo di errore impostato su invalid_grant.
  * - CI_097
    - Emissione, Sicurezza
    - Protezione della riservatezza del Refresh Token
    - La riservatezza dei Refresh Token è garantita sia in transito che a riposo tramite cifratura appropriata e meccanismi sicuri di gestione.
  * - CI_098
    - Emissione, Sicurezza
    - Trasmissione dei Refresh Token protetta da TLS
    - Tutte le trasmissioni di token utilizzano connessioni protette da TLS, garantendo canali di comunicazione cifrati per lo scambio di token.
  * - CI_099
    - Emissione, Sicurezza
    - Proprietà di sicurezza del Refresh Token
    - I Refresh Token sono generati con valori non indovinabili e protetti da modifiche tramite meccanismi crittografici di integrità.
  * - CI_100
    - Emissione, Sicurezza
    - Binding crittografico dei Refresh Token
    - Gli Authorization Server vincolano crittograficamente i Refresh Token al Wallet Instance secondo le specifiche di RFC 9449.
  * - CI_101
    - Emissione, Sicurezza
    - Coerenza di binding della chiave DPoP tra Refresh e Access Token
    - Gli Access Token e i Refresh Token sono vincolati alla stessa chiave DPoP.
  * - CI_102
    - Emissione, Sicurezza
    - Obbligo di DPoP Proof per il Refresh Token
    - Il DPoP Proof è richiesto per tutte le operazioni di refresh per ottenere nuovi Access Token.
  * - CI_103
    - Emissione, Sicurezza
    - Uso coerente della chiave DPoP per il Refresh Token
    - La stessa chiave DPoP viene utilizzata per generare i DPoP Proof degli Access Token in tutte le Richieste di Credenziale.
  * - CI_104
    - Emissione, Sicurezza
    - Gestione della durata di utilizzo del Refresh Token
    - I Credential Issuer gestiscono e limitano la durata per cui i Refresh Token possono essere utilizzati per aggiornare le Credenziali, prima di richiedere il riavvio completo del processo di emissione (OPENID4VC-HAIP).
  * - CI_105
    - Emissione, Sicurezza
    - Allineamento raccomandato delle date di scadenza nelle Credenziali riemesse
    - Le nuove Credenziali Digitali ottenute tramite il flusso di ri-emissione mantengono la stessa scadenza della Credenziale aggiornata.
  * - CI_106
    - Emissione, Sicurezza
    - Obbligo di nuova emissione dopo la scadenza
    - Una volta che una Credenziale Digitale è scaduta, l’Utente deve completare l’intero processo di emissione per ottenere nuove Credenziali Digitali.
  * - CI_107
    - Emissione, Sicurezza
    - Obbligo di coerenza dell’Issuer nella Ri-emissione
    - Le nuove Credenziali Digitali sono emesse esclusivamente dallo stesso Credential Issuer che ha originariamente fornito le credenziali al Wallet Instance.
  * - CI_108
    - Emissione, Sicurezza
    - Limitazione dello scope del Refresh Token per la Ri-emissione
    - Gli Access Token ottenuti tramite Refresh Token non possono essere utilizzati per l’emissione di nuove Credenziali Digitali non già presenti nel Wallet Instance (prima emissione).
  * - CI_109
    - Emissione, Sicurezza
    - Limitazione dello scope del processo di Ri-emissione
    - Il processo di ri-emissione è limitato a due specifici tipi di aggiornamento: aggiornamenti tecnici del modello/formato dei dati e aggiornamenti dell’insieme di attributi dell’Utente.
  * - CI_110
    - Emissione, Sicurezza
    - Aggiornamenti tecnici senza interazione utente
    - Per aggiornamenti tecnici del modello/formato dei dati, la sostituzione e l’archiviazione delle Credenziali Digitali non richiedono il coinvolgimento diretto dell’Utente.
  * - CI_111
    - Emissione, Sicurezza e Privacy
    - Autorizzazione utente per aggiornamento attributi
    - Per aggiornamenti dell’insieme di attributi dell’Utente, il Wallet Instance informa l’Utente delle modifiche e richiede esplicita autorizzazione prima di archiviare la nuova Credenziale Digitale.
  * - CI_112
    - Emissione, Sicurezza
    - Coerenza della data di scadenza nella Ri-emissione
    - Le nuove Credenziali Digitali mantengono la stessa data di scadenza della versione precedente.
  * - CI_113
    - Emissione, Privacy
    - Notifica opzionale out-of-band per aggiornamenti di Ri-emissione
    - Quando una Credenziale Digitale necessita di aggiornamento, i Credential Issuer inviano notifiche agli Utenti tramite canali di comunicazione out-of-band registrati (email, SMS, notifiche push).
  * - CI_114
    - Emissione, Sicurezza
    - Restrizione di prima emissione per i Refresh Token
    - Gli Access Token ottenuti tramite Refresh Token non possono essere utilizzati per la prima emissione di Credenziali Digitali.
  * - CI_115
    - Emissione, Sicurezza
    - Obbligo di coerenza della data di scadenza dopo la Ri-emissione
    - Il Credential Issuer imposta la stessa data di scadenza per le Credenziali Digitali riemesse come per la versione precedente.
  * - CI_116
    - Emissione, Privacy
    - Consenso utente per la Ri-emissione basata su attributi
    - Nei processi di ri-emissione attivati da modifiche degli attributi, viene richiesto il consenso dell’Utente prima dell’archiviazione della nuova Credenziale Digitale.

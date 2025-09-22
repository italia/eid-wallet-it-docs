.. include:: ../common/common_definitions.rst

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
    - Il Credential Issuer fornisce correttamente i seguenti tipi di metadata: *federation_entity*, *oauth_authorization_server* e *openid_credential_issuer*.
  * - CI_009
    - Trust, Interoperabilità
    - Inclusione dei Metadata *openid_credential_verifier* nell’Autenticazione Utente tramite Wallet
    - Quando i Fornitori di Attestati Elettronici di Attributi (Qualificati) autenticano gli utenti tramite la loro Istanza Wallet, i metadata *openid_credential_verifier* sono inclusi oltre ai parametri metadata obbligatori.
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
    - Il parametro grants contiene correttamente un oggetto authorization_code che include entrambi i sotto-parametri obbligatori (*issuer_state* e *authorization_server*) con valori appropriati.
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
    - Il Credential Issuer utilizza l’algoritmo specificato nel parametro di header alg (:rfc:`9126`/:rfc:`9101`) per validare la firma del Request Object.
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
    - Il Credential Issuer valida correttamente la firma del Request Object utilizzando l’algoritmo del parametro alg e la chiave pubblica della Wallet Attestation (cnf.jwk, referenziata da kid), confermando l’integrità della firma (:rfc:`9126`/:rfc:`9101`).
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
    - Il Credential Issuer valida che il claim iss nel Request Object corrisponda al claim client_id nello stesso Request Object (:rfc:`9126`/:rfc:`9101`); discrepanze portano al rifiuto della richiesta.
  * - CI_022
    - Emissione, Sicurezza
    - Verifica dell’Audience Claim nella PAR
    - Il Credential Issuer conferma che il claim aud nel Request Object sia uguale al proprio identificativo (:rfc:`9126`/:rfc:`9101`); valori errati comportano il rifiuto immediato.
  * - CI_023
    - Emissione, Sicurezza
    - Rifiuto del parametro Request URI nella PAR
    - Il Credential Issuer rileva e rifiuta qualsiasi richiesta PAR contenente il parametro request_uri (:rfc:`9126`), restituendo un errore che segnala il parametro non supportato.
  * - CI_024
    - Emissione, Sicurezza
    - Validazione dei Parametri Obbligatori nella PAR
    - Il Credential Issuer verifica la presenza di tutti i parametri HTTP obbligatori nel Request Object e valida i loro valori rispetto alle specifiche di tabella definite (:rfc:`9126`); parametri mancanti o non validi causano risposte di errore strutturate.
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
    - Il Credential Issuer rifiuta richieste in cui iat è superiore a più di 5 minuti dal tempo corrente (:rfc:`9126`); violazioni temporali generano errori "invalid_request".
  * - CI_027
    - Emissione, Sicurezza
    - Prevenzione di Replay Attack nella PAR
    - Il Credential Issuer verifica che il claim jti nel Request Object non sia stato usato prima dall'Istanza Wallet identificata dal client_id.
  * - CI_028
    - Emissione, Sicurezza, Interoperabilità
    - Validazione OAuth Client Attestation PoP
    - Il Credential Issuer valida con successo il parametro OAuth-Client-Attestation-PoP secondo la Sezione 4 di [`OAUTH-ATTESTATION-CLIENT-AUTH`_], confermando la prova di possesso e rifiutando attestazioni non valide con risposte di errore dettagliate.
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
    - Il corpo del messaggio di risposta HTTP utilizza il tipo media application/json (:rfc:`8259`) e include i parametri richiesti di livello superiore.
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
    - Quando l’elaborazione della richiesta PAR incontra errori, il Credential Issuer risponde come definito in :rfc:`9126`, secondo i codici di stato HTTP.
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
    - Il Credential Issuer consente richieste duplicate quando derivano da ricaricamento o aggiornamento del user-agent da parte dell’utente (derivato da :rfc:`9126`).
  * - CI_049
    - Emissione, Sicurezza
    - Identificazione della richiesta PAR nella richiesta di autorizzazione
    - Il Credential Issuer identifica e correla con successo ogni richiesta di autorizzazione come risultato diretto di una PAR precedentemente inviata (derivato da :rfc:`9126`).
  * - CI_050
    - Emissione, Sicurezza
    - Obbligatorietà del parametro request_uri nella richiesta di autorizzazione
    - Il Credential Issuer rifiuta tutte le richieste di autorizzazione che non contengono il parametro request_uri, poiché la PAR è l’unico metodo per trasmettere richieste di autorizzazione dall’istanza del Wallet (derivato da :rfc:`9126`).
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
    - Il Credential Issuer garantisce che il codice di autorizzazione sia emesso all’istanza del Wallet autenticata (:rfc:`6749`) e che non sia stato riutilizzato.
  * - CI_061
    - Emissione, Sicurezza
    - Verifica di validità e utilizzo del Codice di Autorizzazione nella Richiesta di Token
    - Il Credential Issuer verifica che il codice di autorizzazione sia valido e non sia stato precedentemente utilizzato (:rfc:`6749`).
  * - CI_062
    - Emissione, Sicurezza
    - Validazione della corrispondenza del Redirect URI nella Richiesta di Token
    - Il Credential Issuer conferma che il redirect_uri corrisponda esattamente al valore incluso nel precedente Request Object (vedi Sezione 3.1.3.1 di [`OIDC`_]).
  * - CI_063
    - Emissione, Sicurezza
    - Validazione del DPoP Proof JWT nella Richiesta di Token
    - Il Credential Issuer valida correttamente il DPoP Proof JWT secondo la Sezione 4.3 di (:rfc:`9449`).
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
    - In caso di errori durante la validazione della Richiesta di Token, l’Authorization Server restituisce una risposta di errore come definito in :rfc:`6749`, in accordo con la Tabella dei Codici di Stato HTTP.
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
    - Il Credential Issuer valida correttamente il DPoP JWT Proof secondo le procedure della Sezione 4.3 di (:rfc:`9449`) e conferma che l’Access Token sia valido e idoneo per la Credenziale richiesta.
  * - CI_083
    - Emissione, Sicurezza
    - Validazione della prova di possesso del materiale crittografico nella Risposta di Credenziale
    - Il Credential Issuer valida la prova di possesso della chiave alla quale sarà vincolata la nuova Credenziale, secondo la Sezione 8.2.2 di `OpenID4VCI`_.
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
    - Quando la Richiesta di Credenziale non contiene un Access Token valido, il Credential Endpoint restituisce una risposta di errore come definito nella Sezione 3 di [:rfc:`6750`], in accordo con la Tabella dei Codici di Stato HTTP.
  * - CI_086
    - Emissione, Interoperabilità
    - Notification ID unificato per operazioni batch
    - Per le Credenziali Digitali emesse in batch, un unico notification_id copre l’intero set emesso. La risposta di notifica si applica a tutte le Credenziali: qualsiasi fallimento parziale è trattato come fallimento dell’intero batch.
  * - CI_087
    - Emissione, Interoperabilità
    - Tabella dei Codici di Stato HTTP per la Risposta di Notifica
    - Quando la Richiesta di Notifica non contiene un Access Token valido, il Notification Endpoint restituisce una risposta di errore come definito nella Sezione 3 di [:rfc:`6750`], in accordo con la Tabella dei Codici di Stato HTTP.
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
    - Il Credential Issuer valida correttamente il parametro OAuth-Client-Attestation-PoP secondo la Sezione 4 di [`OAUTH-ATTESTATION-CLIENT-AUTH`_].
  * - CI_092
    - Emissione, Sicurezza
    - Validazione del DPoP Proof JWT per il Refresh
    - Il Credential Issuer valida il DPoP Proof JWT secondo la Sezione 4.3 di (:rfc:`9449`).
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
    - Gli Authorization Server vincolano crittograficamente i Refresh Token al Wallet Instance secondo le specifiche di :rfc:`9449`.
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
    - I Credential Issuer gestiscono e limitano la durata per cui i Refresh Token possono essere utilizzati per aggiornare le Credenziali, prima di richiedere il riavvio completo del processo di emissione (`OPENID4VC-HAIP`_).
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
  * - CI_117
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Attributi utente PID italiani
    - Il PID italiano è fornito con successo con gli attributi utente definiti nella rispettiva :ref:`tabella degli Attributi PID dell'Utente <table_sd-jwt-vc_parameters>`.
  * - CI_118
    - Modello di Dati e ciclo di vita, Emissione, Interoperabilità
    - Formati di credenziali (Q)EAA
    - Le (Q)EAA sono rilasciate a un'Istanza del Wallet in formato dati SD-JWT-VC o mdoc-CBOR.
  * - CI_119
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Formato Credenziale Digitale PID/(Q)EAA
    - Il PID/(Q)EAA è emesso con successo sotto forma di Credenziale Digitale con formato Credenziale Digitale SD-JWT come specificato in `SD-JWT-VC`_
  * - CI_120
    - Modello di Dati e ciclo di vita, Sicurezza
    - Firma della credenziale SD-JWT
    - La Credenziale in formato SD-JWT è firmata utilizzando la chiave privata del Fornitore di Attestati Elettronici
  * - CI_121
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Fornitura Metadati Tipo SD-JWT
    - L'SD-JWT è fornito con successo con Metadati Tipo completi per la Credenziale Digitale emessa, conforme alle Sezioni 6 e 6.3 delle specifiche `SD-JWT-VC`_.
  * - CI_122
    - Modello di Dati e ciclo di vita, Sicurezza
    - Validazione Struttura Payload SD-JWT
    - Il payload SD-JWT contiene il claim richiesto *_sd_alg* e tutti gli altri claim obbligatori come specificato nella Sezione 4.1.1 `SD-JWT`_, con formattazione e struttura corrette.
  * - CI_123
    - Modello di Dati e ciclo di vita, Sicurezza
    - Dichiarazione Algoritmo Hash SD-JWT
    - Il claim *_sd_alg* è presente e impostato su un algoritmo supportato definito nella Sezione Algoritmi Crittografici, indicando l'algoritmo hash utilizzato dal Fornitore di Attestati Elettronici per generare i digest come descritto nella Sezione 4.1.1 di `SD-JWT`_.
  * - CI_124
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Organizzazione Divulgazione Selettiva SD-JWT
    - I claim non selettivamente divulgabili appaiono direttamente nel payload SD-JWT così come sono, mentre i digest dei claim selettivamente divulgabili (più eventuali esche) sono organizzati correttamente all'interno degli array *_sd* come descritto nella Sezione 4.2.4.1.
  * - CI_125
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Verifica Integrità disclosure SD-JWT
    - Ogni valore digest viene convalidato correttamente rispetto alla corrispondente disclosure, le cui disclosure contengono i componenti richiesti: salt casuale, nome della claim (per gli elementi oggetto) e valore della claim.
  * - CI_126
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Raccomandazione su Divulgazione Selettiva Oggetti Annidati SD-JWT
    - In un payload SD-JWT annidato, ogni claim a ogni livello della struttura JSON è esplicitamente contrassegnato come selettivamente divulgabile o meno. Di conseguenza, il claim *_sd* contenente digest può legittimamente apparire più volte a livelli diversi all'interno dell'SD-JWT.
  * - CI_127
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Posizionamento digest Disclosure SD-JWT
    - Le disclosures di elementi array sono posizionate correttamente, con digest e digest esca che sostituiscono i valori claim originali nelle loro posizioni array esatte, come specificato nella Sezione 4.2.4.2 `SD-JWT`_.
  * - CI_128
    - Modello di Dati e ciclo di vita, Sicurezza
    - Calcolo Digest Elementi Array SD-JWT
    - I valori digest degli elementi array sono calcolati utilizzando una funzione hash sulle disclosures, contenenti: un salt casuale e l'elemento array.
  * - CI_129
    - Modello di Dati e ciclo di vita, Privacy
    - SD-JWT Array Disclosures
    - La divulgazione selettiva a livello array opera correttamente, consentendo ai Titolari di divulgare selettivamente interi array o singole voci all'interno degli array, come definito nella Sezione 4.2.6 di `SD-JWT`_.
  * - CI_130
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Consegna delle Disclosure nel Formato Combinato SD-JWT
    - Le Disclosures sono fornite con successo al Titolare insieme all'SD-JWT nel Formato Combinato per l'Emissione, formattate come una serie ordinata di valori codificati base64url con ogni valore separato correttamente da un singolo carattere tilde ('~').
  * - CI_131
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Parametro Header JOSE SD-JWT
    - L'header JOSE contiene i parametri definiti nella :ref:`Tabella degli header SD-JWT della Credenziale <table_sd-wt-vc_jose_header>`.
  * - CI_132
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Claim Payload SD-JWT
    - Il payload JWT contiene claim nella Credenziale :ref:`Tabella dei Parametri SD-JWT della Credenziale <table_sd-jwt-vc_parameters>`
  * - CI_133
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Struttura Parametro Lista Stato SD-JWT
    - Quando il parametro status è impostato su status_list, è un Oggetto JSON contenente i seguenti sotto-parametri: *idx* e *uri*
  * - CI_134
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Struttura Parametro SD-JWT Status Assertion
    - Quando il parametro status è impostato su "status_assertion", contiene con successo un Oggetto JSON strutturato correttamente con il claim *credential_hash_alg* richiesto che indica l'algoritmo di hashing utilizzato per legare la Status Assertion alla Credenziale Digitale, con sha-256 come algoritmo raccomandato.
  * - CI_135
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Recupero Opzionale Metadati Tipo Credenziale SD-JWT
    - Il Documento JSON Metadati Tipo Credenziale è recuperato con successo direttamente dall'URL contenuto nel claim vct utilizzando il metodo HTTP GET o tramite il parametro header vctm quando fornito
  * - CI_135a
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Corrispondenza URI Case-Insensitive SD-JWT
    - Quando si recuperano i Metadati Tipo Credenziale tramite vct, la corrispondenza letterale della stringa URI è eseguita in modo case-insensitive, mentre il sistema opera senza richiedere l'endpoint .well-known (come specificato nella Sezione 6.3.1 di `SD-JWT-VC`_), mantenendo opzioni di compatibilità per implementatori che scelgono di utilizzarlo per l'interoperabilità con altri sistemi.
  * - CI_136
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Struttura Oggetto JSON Documento Metadati
    - Il documento tipo Metadati è un oggetto JSON contenente i parametri nella :ref:`Tabella del Type Metadata dell'Attestato Elettronico <table_metadata_type_json_obj>`.
  * - CI_137
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Claim PID Aggiuntivi
    - A seconda del tipo di Credenziale Digitale specificato in vct, i dati dei claim aggiuntivi sono incorporati con successo quando richiesto
  * - CI_138
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Formato Credenziale Mdoc
    - Gli elementi dati mdoc sono codificati con successo in formato CBOR secondo le specifiche :rfc:`8949`, assicurando corretta serializzazione binaria e compatibilità con lo standard ISO/IEC 18013-5.
  * - CI_139
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Organizzazione Struttura Componenti Mdoc
    - La Credenziale Digitale mdoc è strutturata correttamente in componenti distinti inclusi namespace (nameSpaces) e prova crittografica (issuerAuth)
  * - CI_140
    - Modello di Dati e ciclo di vita, Privacy
    - Verifica Integrità Oggetto Sicurezza Mobile Mdoc
    - L'Oggetto Sicurezza Mobile (MSO) memorizza correttamente i digest crittografici degli attributi all'interno dei nameSpaces, consentendo alle Relying Party di validare gli attributi divulgati contro i valori digestID corrispondenti mantenendo la privacy delle informazioni non divulgate. Vedere :ref:`credential-data-model:Mobile Security Object` per dettagli
  * - CI_141
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Conformità Struttura Mdoc-CBOR
    - La Credenziale Digitale mdoc-CBOR è conforme con successo alla struttura richiesta come specificato nella :ref:`tabella del formato mdoc-CBOR <table_mdoc_structure>`.
  * - CI_142
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Organizzazione Struttura Namespace
    - I nameSpaces contengono correttamente uno o più nameSpace, ognuno identificato correttamente da un nome univoco per la categorizzazione organizzata dei dati.
  * - CI_143
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Codifica IssuerSignedItemBytes Namespaces
    - All'interno di ogni nameSpace, uno o più IssuerSignedItemBytes sono codificati correttamente come stringhe di byte CBOR con Tag 24 (#6.24(bstr .cbor)), apparendo come 24(\<\<\... \>\>) in notazione diagnostica
  * - CI_144
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Attributi Informazioni Divulgazione Namespace
    - Ogni IssuerSignedItemBytes rappresenta con successo le informazioni di divulgazione per i digest corrispondenti all'interno dell'Oggetto Sicurezza Mobile e contiene tutti gli attributi come specificato nella :ref:`tabella degli Attributi dei Namespaces <table_attribute_namespaces>`
  * - CI_145
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Inclusione ElementIdentifier Namespace
    - Tutti gli elementIdentifier nella :ref:`tabella <table_element_identifiers_mdoc>` dell'attributo elementIdentifiers sono inclusi correttamente nella Credenziale Digitale codificata in mdoc-CBOR all'interno dei rispettivi nameSpaces, salvo diversa specifica
  * - CI_146
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Struttura COSE Oggetto Sicurezza Mobile
    - L'issuerAuth rappresenta con successo l'Oggetto Sicurezza Mobile come un Documento COSE Sign1 formattato correttamente secondo :rfc:`9052`, contenente la struttura dati completa richiesta con: header protetto, header non protetto, payload e componenti firma.
  * - CI_147
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Codifica Parametro Header Protetto Oggetto Sicurezza Mobile
    - L'header protetto contiene con successo i parametri codificati correttamente in formato CBOR secondo la :ref:`tabella <table_protected_headers_mdoc>` corrispondente.
  * - CI_148
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Algoritmo Header Protetto Oggetto Sicurezza Mobile
    - L'header protetto contiene con successo il parametro algoritmo firma richiesto
  * - CI_148a
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Elementi Non Raccomandati nell'Header Protetto Oggetto Sicurezza Mobile
    - L'header protetto non contiene elementi diversi dall'algoritmo firma
  * - CI_149
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Codifica Parametro Header Non Protetto Oggetto Sicurezza Mobile
    - Salvo diversa specifica, l'header non protetto contiene i parametri conformemente alla :ref:`tabella <table_unprotected_headers_mdoc>` corrispondente.
  * - CI_149a
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Inclusione *x5chain* Oggetto Sicurezza Mobile
    - La *x5chain* è inclusa correttamente nell'header non protetto
  * - CI_150
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Struttura Payload Oggetto Sicurezza Mobile
    - Il payload contiene con successo il MobileSecurityObject codificato correttamente come stringa di byte (bstr) utilizzando CBOR Tag 24, con il parametro header COSE Sign content-type correttamente escluso dalla struttura.
  * - CI_151
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Conformità Attributi Oggetto Sicurezza Mobile
    - Il MobileSecurityObject contiene con successo tutti gli attributi richiesti come specificato nella :ref:`tabella <table_MobileSecurityObject_attributes>` di conformità, con formattazione e valori corretti salvo esenzione esplicita dai requisiti della specifica.
  * - CI_152
    - Emissione, Interoperabilità
    - Verifica stato Istanza del Wallet
    - Il Fornitore di Attestati Elettronici verifica con successo che l'Istanza del Wallet sia in stato Operativo o Valido e procede con l'emissione della Credenziale Digitale.
  * - CI_153
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Gestione Stato Credenziale per Attivazione
    - Una Credenziale Digitale transita con successo allo stato Valido quando la data di inizio validità è raggiunta, o quando il processo di riattivazione è completato per una (Q)EAA precedentemente sospesa.
  * - CI_154
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Gestione Automatica Scadenza Credenziale
    - Una Credenziale Digitale transita con successo allo stato Scaduto quando scade automaticamente al raggiungimento della sua data di fine validità (PID/(Q)EAA EXP),
  * - CI_155
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Gestione Processo Revoca Credenziale
    - Una Credenziale Digitale cambia con successo dagli stati Emesso, Valido o Sospeso allo stato Revocato quando è attivamente revocata dal Fornitore di Attestati Elettronici tramite un processo di revoca (PID/(Q)EAA REV).
  * - CI_156
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Casi d'Uso Revoca Credenziale Digitale
    - La Revoca Credenziale Digitale è implementata correttamente per ogni caso d'uso
  * - CI_156a
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Revoca Credenziale Digitale - Compromissione Sicurezza Tecnica
    - La Credenziale Digitale è revocata con successo quando viene rilevata compromissione del materiale crittografico, con invalidazione immediata e aggiornamento dello stato nei registri di revoca.
  * - CI_156b
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Revoca Credenziale Digitale - Richiesta Utente
    - La Credenziale Digitale è revocata con successo su richiesta esplicita dell'Utente
  * - CI_156c
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Revoca Credenziale Digitale - Aggiornamenti Attributi
    - La Credenziale Digitale è revocata automaticamente quando le Fonti Autentiche notificano cambiamenti di attributi che invalidano la credenziale, innescando il processo di riemissione se applicabile.
  * - CI_156d
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Revoca Credenziale Digitale - Revoca Avviata dalla Fonte
    - La Credenziale Digitale è revocata immediatamente quando la Fonte Autentica notifica la revoca degli attributi sottostanti
  * - CI_156e
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Revoca Credenziale Digitale - Revoca Istanza del Wallet
    - Tutte le Credenziali Digitali sono revocate quando l'Istanza del Wallet contenitore è revocata
  * - CI_156f
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Revoca Credenziale Digitale - Ordine Giudiziario/Supervisorio
    - La Credenziale Digitale è revocata immediatamente quando attività illegali sono segnalate da Organi Giudiziari o Supervisori
  * - CI_156g
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Revoca PID - Violazione Gestore di Identità Digitale
    - Il PID è revocato quando si verifica rilevamento di violazione nel Gestore di Identità Digitale utilizzato per l'autenticazione Utente durante l'emissione PID
  * - CI_157
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Revoca (Q)EAA Opzionale Seguendo Revoca PID
    - Il Fornitore (Q)EAA valuta con successo lo stato di revoca PID e revoca le credenziali (Q)EAA associate
  * - CI_158
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Cambio Stato (Q)EAA a Sospeso
    - La (Q)EAA transita con successo dallo stato Emesso o Valido allo stato Sospeso quando è sospesa dal Fornitore di Attestati Elettronici ((Q)EAA SUSP)
  * - CI_159
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Durata Sospensione (Q)EAA e Recupero Stato
    - La (Q)EAA sospesa rimane nello stato Sospeso finché le condizioni di sospensione non sono risolte e la credenziale è ripristinata allo stato precedente Emesso o Valido, o transita a Revocato, Scaduto, o eliminato
  * - CI_159a
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Sospensione (Q)EAA - Cambiamenti Validità Attributi
    - La sospensione di una (Q)EAA è basata sullo stato di validità dei suoi attributi contenuti
  * - CI_159b
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Sospensione (Q)EAA - Richiesta Utente
    - La (Q)EAA transita con successo allo stato Sospeso su richiesta esplicita dell'Utente.
  * - CI_160
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Gestione Ciclo di Vita Individuale Credenziali Digitali Emesse in Batch
    - Ogni Credenziale Digitale da un'emissione batch entra con successo nella propria macchina a stati del ciclo di vita indipendente. Tutte le transizioni di stato (Emesso → Valido → Scaduto/Sospeso/Revocato) avvengono ancora su base per Credenziale, utilizzando i parametri individuali della Credenziale
  * - CI_161
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Generazione e Memorizzazione Credenziale Digitale
    - Il Fornitore di Attestati Elettronici genera con successo la Credenziale Digitale seguendo il completamento della richiesta di emissione e la memorizza nell'archiviazione locale immediatamente dopo l'emissione riuscita.
  * - CI_161a
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Gestione Stato Credenziale Digitale
    - Il Fornitore di Attestati Elettronici aggiorna con successo lo stato della Credenziale Digitale localmente per eventi di revoca, sospensione o riattivazione innescati da ragioni di sicurezza tecnica, richieste Utente, o da entità esterne (es. Utenti e Fonti Autentiche)
  * - CI_161b
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Eliminazione Dati Credenziale Digitale
    - Il Fornitore di Attestati Elettronici rimuove con successo le Credenziali Digitali dall'archiviazione locale dopo aver raggiunto lo stato Scaduto o basato sulle politiche di ritenzione del Fornitore di Attestati Elettronici.
  * - CI_162
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Gestione Diretta Stato Validità Fornitore di Attestati Elettronici
    - Il Fornitore di Attestati Elettronici gestisce direttamente lo stato di validità delle Credenziali Digitali emesse e gestisce correttamente l'innesco del processo di revoca o sospensione della Credenziale Digitale da parte di altri attori.
  * - CI_162a
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Revoca Avviata dall'Utente tramite Servizio Web del Fornitore di Attestati Elettronici
    - L'Utente avvia con successo la revoca/sospensione della Credenziale Digitale tramite il servizio web del Fornitore di Attestati Elettronici, con verifica dell'autenticazione e processamento della richiesta di revoca.
  * - CI_162b
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Revoca Innescata da Fonte Autentica
    - La Fonte Autentica innesca con successo il processo di revoca/sospensione della Credenziale Digitale quando gli attributi della Credenziale sono aggiornati o cambiano stato di validità.
  * - CI_163
    - Modello di Dati e ciclo di vita, Sicurezza
    - Accesso Utente al Portale Web del Fornitore di Attestati Elettronici con Autenticazione LoA
    - Il Fornitore di Attestati Elettronici assicura che gli utenti possano accedere con successo all'area sicura del suo portale web. Questo accesso richiede autenticazione con un Livello di Garanzia almeno pari al Livello di Garanzia utilizzato durante l'emissione iniziale della credenziale.
  * - CI_163a
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Accesso Utente alla Vista Database Credenziali Digitali
    - Il Fornitore di Attestati Elettronici fornisce con successo agli Utenti una vista completa di tutte le loro Credenziali Digitali contenute nel database del Fornitore di Attestati Elettronici tramite il portale web
  * - CI_163b
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Verifica Autenticità Dati Utente tramite Portale Web
    - Il Fornitor di Credenziali abilita con successo gli Utenti a verificare l'autenticità dei dati delle loro Credenziali Digitali tramite il portale web
  * - CI_163c
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Gestione Stato Validità Utente tramite Portale Web
    - Il Fornitor di Credenziali consente con successo agli Utenti di visualizzare e aggiornare lo stato di validità delle loro Credenziali Digitali tramite il portale web (revocare le loro Credenziali Digitali e, se supportato dal Fornitore, sospenderle).
  * - CI_164
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Revoca PID e Aggiornamento Stato Istanza del Wallet su Nuova Emissione PID
    - Quando l'Utente attiva un'altra Istanza di Wallet dallo stesso Fornitore di Wallet utilizzando la stessa Soluzione Wallet e ottiene un nuovo PID, il PID precedente è revocato con successo e l'Istanza di Wallet precedente transita con successo allo stato operativo, assicurando un singolo PID attivo per Utente per Fornitore di Wallet.
  * - CI_165
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Revoca PID Seguendo Morte Utente e Cambio Stato ANPR
    - La morte dell'Utente innesca con successo il cambio dello stato di validità degli attributi di identificazione dell'Utente nel registro pubblico (ANPR), che produce automaticamente la revoca PID.
  * - CI_166
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Requisito Notifica Revoca PID
    - Il Fornitore di Credenziali invia con successo notifica dell'evento di revoca PID all'Utente entro 24 ore dal verificarsi della revoca
  * - CI_167
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Notifica Revoca Credenziale Non-PID Raccomandata
    - Il Fornitore di Attestati Elettronici invia notifica dell'evento di revoca all'Utente per qualsiasi Credenziale Digitale diversa dal PID
  * - CI_168
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Consegna Notifica Revoca Multi-Canale
    - Il Fornitore di Attestati Elettronici consegna con successo le notifiche di revoca attraverso canali di comunicazione verificati e sicuri (email, telefono, o altri canali autenticati), includendo informazioni complete sullo stato di revoca della Credenziale e la ragione.
  * - CI_169
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Aggiornamento Stato Credenziale Digitale su Revoca
    - Il Fornitore di Attestati Elettronici aggiorna con successo lo stato della Credenziale Digitale immediatamente quando avviene la revoca
  * - CI_170
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Endpoint Revoca Istanza di Wallet tramite PDND
    - Il Fornitore di Attestati Elettronici fornisce con successo servizio web per l'endpoint di Revoca Istanza di Wallet definito utilizzando le specifiche PDND, con implementazione conforme ai requisiti del Catalogo e-Service PDND del Fornitore di Attestati Elettronici.
  * - CI_171
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Servizio Aggiornamento Credenziale e Notifica Stato tramite PDND
    - Il Fornitore di Attestati Elettronici fornisce con successo servizio web disponibile tramite PDND per notifica aggiornamento Credenziale e stato validità come definito nella Sezione specifiche Catalogo e-Service PDND del Fornitore di Attestati Elettronici.
  * - CI_172
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Aggiornamento Stato Credenziale Seguendo Notifica Cambio Dati
    - Il Fornitore di Attestati Elettronici aggiorna con successo lo Stato della Credenziale secondo la modalità definita del meccanismo di validità alla ricezione di notifica dalla Fonte Autentica
  * - CI_172a
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Notifica Utente di Aggiornamento Credenziale
    - Il Fornitore di Attestati Elettronici notifica con successo l'Utente dei cambiamenti della credenziale attraverso canale di comunicazione out-of-band registrato
  * - CI_173
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Notifica Utente su Stato Credenziale INVALIDA
    - Il Fornitore di Attestati Elettronici informa con successo l'Utente quando lo Stato della Credenziale cambia a INVALIDA
  * - CI_174
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Processamento Aggiornamento Stato Batch come Cambiamenti Individuali
    - Il Fornitore di Attestati Elettronici gestisce con successo la richiesta di aggiornamento stato batch singola (che riferisce batch notification_id) da entità autorizzate (es. Istanza di Wallet tramite Endpoint Notifica con event=credential_deleted, o Fornitore di Wallet tramite PDND) come N cambiamenti individuali separati, con lo stato di ogni Credenziale aggiornato indipendentemente (per esempio, cambiando il suo bit status-list a INVALIDO o SOSPESO).
  * - CI_175
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Revoca batch su Richiesta Aggiornamento credenziale
    - Il Fornitore di Attestati Elettronici processa con successo la richiesta aggiornamento batch come richiesta revoca tutto, contrassegnando ogni Credenziale nel batch come revocata ed emettendo singola notifica coprendo l'intero batch.
  * - CI_176
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Eliminazione Credenziale Batch
    - L'eliminazione guidata dall'utente rimuove con successo l'intero batch poiché la Wallet UI  presenta un batch come una Credenziale, con richiesta eliminazione utilizzando il notification_id del batch applicato a tutte le Credenziali in quel batch, poiché non è possibile eliminare o revocare solo una Credenziale.
  * - CI_177
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Supporto Lista Stato OAuth per Credenziali Digitali Longeve
    - La Lista Stato OAuth (`TOKEN-STATUS-LIST`_) è supportata con successo per verifica dello stato validità delle Credenziali Digitali longeve in scenari sia remoti che di prossimità.
  * - CI_178
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Supporto Opzionale OAuth Status Assertions in Scenario Remoto
    - Il Fornitore di Attestati Elettronici, l'Istanza di Wallet e la Relying Party supportano con successo le OAuth Status Assertions (`OAUTH-STATUS-ASSERTION`_) nello scenario remoto.
  * - CI_179
    - Modello di Dati e ciclo di vita, Sicurezza e Privacy
    - OAuth Status Assertions - Archiviazione Locale Credenziale Digitale con Dati Ciclo di Vita
    - I Fornitori di Credenziali memorizzano con successo la Credenziale Digitale generata ed emessa localmente con set minimo di dati richiesto per gestire il suo ciclo di vita, includendo lo stato di validità di quella Credenziale Digitale.
  * - CI_180
    - Modello di Dati e ciclo di vita, Sicurezza
    - OAuth Status Assertions - Specifica Algoritmo Hash Credenziale Digitale
    - I Fornitori di Credenziali includono con successo l'algoritmo hash specificato nella Credenziale Digitale utilizzando il claim *credential_hash_alg* all'interno del membro JSON status_assertion del claim status.
  * - CI_181
    - Modello di Dati e ciclo di vita, Interoperabilità
    - OAuth Status Assertions - Aggiunta Parametri Metadati del Fornitore di Attestati Elettronici
    - I Fornitori di Credenziali aggiungono con successo i parametri *status_assertion_endpoint* e *credential_hash_alg_supported* all'interno dei loro Metadati.
  * - CI_182
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Validazione Autorizzazione Richiesta Status Assertion
    - Il Fornitore di Attestati Elettronici valida con successo che l'Istanza di Wallet che fa la richiesta sia autorizzata a richiedere la Status Assertion, e fornisce Status Assertion Error Response secondo la Sezione HTTP Status Assertion Response se si verificano errori durante questo controllo.
  * - CI_183
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Verifica Conformità Richiesta Status Assertion
    - Il Fornitore di Attestati Elettronici verifica con successo la conformità di tutti gli elementi nell'oggetto status_assertion_requests utilizzando il metodo di conferma contenuto nella Credenziale Digitale dove l'oggetto Status Assertion  è riferito, e fornisce HTTP Status Assertion Response in caso di errori. (vedere Sezione :ref:`credential-revocation:HTTP Status Assertion Response`)
  * - CI_184
    - Modello di Dati e ciclo di vita, Sicurezza
    - Status Assertion Verifica del Fornitore di Attestati Elettronici Legittimo
    - Il Fornitore di Attestati Elettronici verifica con successo di essere Il Fornitore legittimo della Credenziale Digitale a cui ogni oggetto Richiesta di Status Assertion si riferisce.
  * - CI_185
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Status Assertion Controllo Stato Validità Credenziale Digitale
    - Il Fornitore di Attestati Elettronici controlla con successo lo stato di validità per le Credenziali richieste.
  * - CI_186
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Creazione Status Assertion
    - Il Fornitore di Attestati Elettronici che riceve l'oggetto Richiesta Status Assertion crea con successo la Status Assertion corrispondente.
  * - CI_187
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Struttura Array Status Assertion Responses
    - Le status_assertion_responses contengono con successo un array di stringhe con oggetti JSON StatusAssertionResponse e/o StatusAssertionErrors relativi alla richiesta fatta dall'Istanza di Wallet.
  * - CI_188
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Status Assertion Endpoint e Formato Richiesta
    - Lo Status Assertion Endpoint è fornito con successo dal Fornitore di Attestati Elettronici all'interno dei suoi Metadati, con richieste all'endpoint di Status Assertion utilizzando metodo HTTP POST e parametri obbligatori codificati in formato application/json all'interno del corpo del messaggio richiesta HTTP.
  * - CI_189
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Struttura JWT Richiesta Status Assertion
    - L'oggetto Richiesta Status Assertion è con successo un JWT che contiene i parametri Header e Payload nella :ref:`tabella <table_status_assertion_req_obj>` corrispondente
  * - CI_190
    - Modello di Dati e ciclo di vita, Interoperabilità
    - HTTP Status Assertion Response Riuscita
    - Il Fornitore di Attestati Elettronici restituisce con successo risposta HTTP con codice stato impostato a 200 OK in caso di validazione Richiesta Status Assertion riuscita.
  * - CI_191
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Status Assertion Response Valida
    - Il Fornitore di Attestati Elettronici fornisce con successo la Status Assertion valida per Credenziale richiesta, con risposta contenente l'oggetto Status Assertion all'interno Array JSON.
  * - CI_192
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Status Assertion Error Response
    - Gli Status Assertion Error Response relativi a quella Credenziale sono inclusi con successo nell'Array JSON Risposta come voce quando Il Fornitore di Attestati Elettronici non può fornire Status Assertion valida.
  * - CI_193
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Gestione HTTP Status Assertion Error
    - Quando la HTTP Status Assertion Request fallisce (es. richiesta non valida, indisponibilità server, ecc.), un Codice Stato di Errore HTTP è fornito all'interno della Status Assertion Response.
  * - CI_194
    - Modello di Dati e ciclo di vita, Interoperabilità
    - HTTP Status Assertion- Codici Stato HTTP
    - HTTP Status Assertion supporta Codici Stato HTTP secondo la :ref:`tabella <table_http_status_assertion_codes>` corrispondente.
  * - CI_195
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Struttura HTTP Status Assertion Responses
    - La risposta HTTP include con successo un oggetto JSON con un membro chiamato status_assertion_responses.
  * - CI_195a
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Struttura Array Status Assertion Responses
    - Status_assertion_responses contiene con successo un array di stringhe, dove ognuna rappresenta un oggetto Status Assertion Response.
  * - CI_195b
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Formato Elemento JWT Status Assertion Response
    - Ogni elemento contiene con successo il JWT firmato, codificato come valori codificati base64url separati da caratteri punto.
  * - CI_195c
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Requisiti Contenuto Oggetto Status Assertion Response
    - L'oggetto Status Assertion Response contiene con successo Status Assertion Response e Status Assertion Error in analogia con le Sezioni 8 e 9 di `OAUTH-STATUS-ASSERTION`_.
  * - CI_196
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Codifica JSON HTTP Status Assertion Response
    - La risposta HTTP è codificata con successo in formato application/json.
  * - CI_197
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Parametri e Claim Richiesti nella Status Assertion
    - La Status Assertion contiene con successo i parametri e claim richiesti definiti nella :ref:`tabella <table_status_assertion_claims>` corrispondente.
  * - CI_198
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Claim Oggetto Status Assertion Error
    - L'oggetto Status Assertion Error contiene con successo i claim definiti nella :ref:`tabella <table_status_assertion_errors_obj>` corrispondente.
  * - CI_199
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Allocazione Indice Credenziale Digitale e Mappatura Stato
    - Ogni Credenziale Digitale viene allocata con successo con un indice durante l'emissione, che rappresenta la sua posizione all'interno dell'array di bit, con il valore del bit o dei bit a questo indice che corrisponde allo stato della Credenziale Digitale.
  * - CI_200
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Formato Crittografico Status List Token
    - La Status List è fornita con successo all'interno del Status List Token firmato crittograficamente in formato JWT.
  * - CI_201
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Configurazione dei Bit della Status List per le Credenziali Digitali
    - Il Fornitore di Attestati Elettronici definisce il numero di bit, k (che può essere 1, 2, 4 o 8), che rappresenta la quantità di bit usata per descrivere lo stato di ogni Credenziale Digitale all'interno della Status List. Il Fornitore di Attestati Elettronici configura il numero di bit e, di conseguenza, ogni credenziale può avere 2^k stati possibili.
  * - CI_202
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Creazione di un Array di Byte per la Status List e Assegnazione della Posizione della Credenziale.
    - Il Fornitore di Credenziali crea con successo array byte di dimensione = (quantità di Credenziali Digitali) * k / 8 o maggiore, con ogni byte corrispondente a 8/k stati a seconda del valore k (8 se k=1, 4 se k=2, 2 se k=4, o 1 se k=8), e assegna ogni Credenziale Digitale emessa a una posizione nell'array.
  * - CI_203
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Impostazione dei valori di stato delle credenziali digitali nella Status List in un array di byte
    - Il Fornitore di Credenziali imposta con successo valori stato per tutte le Credenziali Digitali emesse all'interno dell'array byte, con ogni stato Credenziale Digitale identificato utilizzando un indice che mappa a bit specifici all'interno dell'array byte, conteggio indice da 0 a (quantità di Credenziale Digitale) - 1, bit contati dal bit meno significativo ("0") al bit più significativo ("7"), e tutti i bit dell'array byte a un particolare indice impostati a un valore stato.
  * - CI_204
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Livello di Compressione Raccomandato per la Status List delle Credenziali Digitali
    - Il Fornitore di Attestati Elettronici comprime con successo l'array byte utilizzando DEFLATE [:rfc:`1951`] con il formato dati ZLIB [:rfc:`1950`]
  * - CI_204a
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Livello di Compressione Raccomandato per la Status List delle Credenziali Digitali
    - Le implementazioni utilizzano con successo il livello di compressione più alto disponibile per la compressione dell'array di byte.
  * - CI_205
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Disponibilità Endpoint Status List
    - Il Fornitore di Attestati Elettronici rende con successo disponibile alle Relying Party e Istanze di Wallet un endpoint per richiedere Liste Stato.
  * - CI_206
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Status List Definizione dei Valori di Stato per le Credenziali Digitali
    - Il Fornitore di Attestati Elettronici utilizza con successo i valori per gli Stati possibili definiti nella :ref:`credential-revocation:Creazione delle Status List`.
  * - CI_207
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Status List Definizione degli stati opzionali di stato delle credenziali digitali
    - Il Fornitore di Attestati Elettronici aggiunge con successo altri stati oltre a quelli descritti sopra quando sceglie il numero di bit per trasmettere gli stati delle Credenziali Digitali emesse, con attenta considerazione per la divulgazione di informazioni alle Relying Party quando aggiunge molti stati diversi per il ciclo di vita della Credenziale Digitale.
  * - CI_208
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Status List Parametri del Token all’Endpoint
    - Il Token Status List è disponibile con successo presso lo Status List Endpoint e contiene i parametri nella :ref:`tabella <table_status_list_endpoint_parameters>` corrispondente.
  * - CI_209
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Impostazione Consigliata di Scadenza Breve del Token Status List
    - Il Fornitore di Attestati Elettronici imposta con successo il claim exp in modo che il Token Status List sia di breve durata, tipicamente con claim exp che non supera il claim iat di più di 24 ore.
  * - CI_210
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Struttura Status List Codificata JSON
    - La struttura della Status List codificata JSON è conforme alla :ref:`Tabella <table_status_list_structure>` corrispondente.
  * - CI_211
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Status List Archiviazione Locale delle Credenziali Digitali
    - I Fornitori di Attestati Elettronici memorizzano con successo la Credenziale Digitale generata localmente con set minimo di dati richiesto per gestire il suo ciclo di vita, includendo lo stato di validità di quella Credenziale Digitale.
  * - CI_212
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Inclusione nella Status List dello Stato delle Credenziali Digitali
    - I Fornitori di Attestati Elettronici includono con successo il claim *status_list* all'interno del valore Oggetto JSON del claim status della Credenziale Digitale una volta generata.
  * - CI_213
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Parametri dell’Oggetto JSON della Status List Claim
    - Il valore del claim *status_list* è con successo un Oggetto JSON con i :ref:`parametri corrispondenti <table_status_list_parameters>`.
  * - CI_214
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Risposta Riuscita dello Status List Endpoint
    - Lo Status List Endpoint risponde con successo con il Token Status List utilizzando il codice stato HTTP nell'intervallo 2xx, con Fornitore Stato che utilizza content-type application/statuslist+jwt per il Token Status List in formato JWT nella risposta riuscita.
  * - CI_215
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Content-Encoding Gzip Risposta Status List HTTP
    - La risposta HTTP utilizza con successo il Content-Encoding gzip come definito nel [:rfc:`9110`].
  * - CI_216
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Autorizzazione e Registrazione del Fornitore di Attestati Elettronici
    - Il Fornitore di Attestati Elettronici registra con successo le proprie Credenziali Digitali nel catalogo.
  * - CI_217
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Informazioni Richieste Catalogo Credenziale Digitale
    - Il Fornitore di Attestati Elettronici fornisce le sue credenziali nel catalogo, insieme alle informazioni nella :ref:`tabella <table_catalogue_main_information>`. corrispondente.
  * - CI_218
    - Modello di Dati e ciclo di vita, Interoperabilità
    - Informazioni Elemento Array Credenziali
    - Ogni elemento dell'array delle credenziali contiene correttamente tutte le informazioni di primo livello definite nella :ref:`Tabella  <table_catalogue_credentials_parameters>` corrispondente.

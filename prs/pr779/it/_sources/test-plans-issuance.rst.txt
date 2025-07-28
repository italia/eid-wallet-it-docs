Matrice di Test per l'Emissione delle Credenziali
-------------------------------------------------

Questa sezione fornisce l'insieme dei test progettati per implementatori tecnici e team di sviluppo responsabili della creazione e del deployment di soluzioni Credential Issuer. È anche destinata agli organismi di valutazione che ispezionano e validano le implementazioni di soluzioni Credential Issuer.

.. note::
  Riferimenti sui piani di test ufficiali OpenID4VCI aggiorneranno questa sezione nelle versioni future.


.. list-table::
  :class: longtable
  :widths: 15 15 35 35
  :header-rows: 1

  * - Test Case ID
    - Purpose
    - Description
    - Expected Result
  * - ISS-001
    - Setup
    - Validare la configurazione della Wallet Instance
    - La Wallet Instance è configurata con una Wallet Attestation valida. Verificare che la chiave pubblica sia valida e correttamente legata a un elemento sicuro.
  * - ISS-002
    - Discovery
    - Credential Issuer Discovery
    - La Wallet Instance scopre con successo i Digital Credential Issuer affidabili utilizzando il Credential Catalogue e verifica la conformità della loro configurazione e delle policy tramite Federation API.
  * - ISS-003
    - Metadata
    - Recupero dei metadata del Credential Issuer
    - La Wallet Instance recupera e valida i metadata del Credential Issuer. I metadata includono i formati PID, gli algoritmi supportati e i parametri di interoperabilità.
  * - ISS-004
    - Authorization, Authentication
    - Richiesta di Credential tramite Authorization Code Flow
    - La Wallet Instance richiede con successo una Credential tramite Authorization Code Flow. Validare l'uso di PKCE con un code verifier di 43-128 caratteri.
  * - ISS-005
    - Authentication
    - Autenticazione dell'Utente con PID Provider
    - L'Utente è autenticato con LoA 3 (High) dal PID Provider. Validare l'uso dello schema di identità digitale CieID e assicurarsi che sia stato ottenuto il consenso dell'Utente.
  * - ISS-006
    - Issuance
    - Emissione della Credential
    - La Credential è emessa e legata al materiale chiave della Wallet Instance. Validare il processo di binding e assicurare l'integrità e la conformità al data model della Credential emessa.
  * - ISS-007
    - Authentication
    - Autenticazione dell'Utente con (Q)EAA Provider
    - L'Utente è autenticato presentando un PID valido. La richiesta di presentazione, il PID è valido e precedentemente ottenuto.
  * - ISS-008
    - Security
    - Validazione della Pushed Authorization Request (PAR)
    - Il Credential Issuer valida con successo la richiesta PAR.
  * - ISS-009
    - Security
    - Validazione della Token Request
    - Il Credential Issuer valida la token request ed emette i token. Validare la prova DPoP e assicurarsi che il codice di autorizzazione sia valido e non riutilizzato.
  * - ISS-010
    - Security
    - Validazione della Credential Request
    - Il Credential Issuer valida la richiesta di Credential ed emette le Credential. Validare la proof of possession e assicurarsi che il tipo di credential corrisponda alla richiesta.
  * - ISS-011
    - Deferred Issuance
    - Flusso di Deferred Issuance
    - La Wallet Instance gestisce correttamente la deferred issuance e recupera le credential successivamente. Validare l'uso di un identificatore univoco di transazione (`transaction_id`) e assicurarsi che la Credential sia emessa dopo il lead time specificato.
  * - ISS-012
    - Notification
    - Gestione delle notifiche
    - La Wallet Instance invia e riceve notifiche correttamente. Validare l'uso di `notification_id` e assicurarsi che il tipo di evento sia correttamente riportato.
  * - ISS-013
    - Credential Issuance
    - Il Provider (Q)EAA offre Credential all'Holder
    - Le Wallet Instance valutano l'offerta e avviano il flusso di autorizzazione dopo aver valutato la fiducia con il Provider (Q)EAA.
  * - ISS-014
    - Security
    - Validare `client_id` nella richiesta PAR
    - Assicurarsi che il `client_id` nel body della richiesta corrisponda al claim `client_id` nel Request Object.
  * - ISS-015
    - Security
    - Validare il claim `iss` nel Request Object
    - Assicurarsi che il claim `iss` nel Request Object corrisponda al claim `client_id`.
  * - ISS-016
    - Security
    - Validare il claim `aud` nel Request Object
    - Assicurarsi che il claim `aud` nel Request Object sia uguale all'identificativo del Credential Issuer.
  * - ISS-017
    - Security
    - Rifiutare la richiesta PAR con `request_uri`
    - Assicurarsi che la richiesta PAR sia rifiutata se contiene il parametro `request_uri`.
  * - ISS-018
    - Security
    - Validare i parametri obbligatori nel Request Object
    - Assicurarsi che il Request Object contenga tutti i parametri obbligatori e che i valori siano validati.
  * - ISS-019
    - Security
    - Validare `OAuth-Client-Attestation-PoP`
    - Assicurarsi che il parametro `OAuth-Client-Attestation-PoP` sia validato.
  * - ISS-020
    - Authorization
    - Validare `request_uri` nella Authorization Request
    - Assicurarsi che i valori di `request_uri` siano monouso e che le richieste scadute siano rifiutate.
  * - ISS-021
    - Authorization
    - Identificare la richiesta dalla PAR inviata
    - Assicurarsi che la richiesta sia identificata come risultato della PAR inviata.
  * - ISS-022
    - Authorization
    - Rifiutare Authorization Request senza `request_uri`
    - Assicurarsi che tutte le Authorization Request senza `request_uri` siano rifiutate.
  * - ISS-023
    - Security
    - Validare i parametri della Authorization Response
    - Assicurarsi che la Authorization Response contenga tutti i parametri definiti.
  * - ISS-024
    - Security
    - Validare il parametro `state` nella Authorization Response
    - Assicurarsi che il parametro `state` nella risposta corrisponda al valore inviato nel Request Object.
  * - ISS-025
    - Security
    - Validare il parametro `iss` nella Authorization Response
    - Assicurarsi che il parametro `iss` corrisponda al Credential Issuer previsto.
  * - ISS-026
    - Security
    - Validare la DPoP Proof per il Token Endpoint
    - Assicurarsi che la DPoP Proof JWT sia valida e leghi l'Access Token alla Wallet Instance.
  * - ISS-027
    - Security
    - Validare i parametri della Token Request
    - Assicurarsi che la token request includa `code`, `code_verifier` e una OAuth 2.0 Attestation valida.
  * - ISS-028
    - Security
    - Validare il codice di autorizzazione nella Token Request
    - Assicurarsi che il codice di autorizzazione sia valido e non riutilizzato.
  * - ISS-029
    - Security
    - Validare `redirect_uri` nella Token Request
    - Assicurarsi che il `redirect_uri` corrisponda al valore nel precedente Request Object.
  * - ISS-030
    - Security
    - Validare la DPoP Proof JWT nella Token Request
    - Assicurarsi che la DPoP Proof JWT sia validata secondo la specifica.
  * - ISS-031
    - Security
    - Validare la Nonce Request
    - Assicurarsi che la Nonce Request sia inviata correttamente e che venga ottenuto un nuovo `c_nonce`.
  * - ISS-032
    - Security
    - Validare la Nonce Response
    - Assicurarsi che il `c_nonce` nella Nonce Response sia imprevedibile e utilizzato correttamente.
  * - ISS-033
    - Security
    - Validare la DPoP Proof per il Credential Endpoint
    - Assicurarsi che la DPoP Proof JWT per il Credential Endpoint sia valida e leghi la Credential alla Wallet Instance.
  * - ISS-034
    - Security
    - Validare i parametri della Credential Request
    - Assicurarsi che la Credential Request includa Access Token, DPoP Proof JWT e una valid proof of possession.
  * - ISS-035
    - Security
    - Validare la JWT Proof nella Credential Request
    - Assicurarsi che la JWT proof includa tutti i claim richiesti e sia firmata correttamente.
  * - ISS-036
    - Security
    - Validare il `c_nonce` nella Credential Request
    - Assicurarsi che il `c_nonce` nella JWT corrisponda al valore fornito dal server.
  * - ISS-037
    - Security
    - Validare i parametri della Credential Response
    - Assicurarsi che la Credential Response contenga tutti i parametri obbligatori e che i valori siano validati.
  * - ISS-038
    - Security
    - Validare l'integrità della Credential
    - Assicurarsi dell'integrità della Credential emessa verificando la firma.
  * - ISS-039
    - Security
    - Validare tipo e schema della Credential
    - Assicurarsi che la Credential emessa corrisponda al tipo richiesto e sia conforme allo schema.
  * - ISS-040
    - Security
    - Validare la Trust Chain nella Credential
    - Assicurarsi che la Trust Chain nell'header della Credential verifichi la fiducia del Credential Issuer al momento dell'emissione.
  * - ISS-041
    - Security
    - Validare i parametri di Deferred Issuance
    - Assicurarsi che i parametri di Deferred Issuance siano usati correttamente e che la Credential sia emessa dopo il lead time specificato.
  * - ISS-042
    - Security
    - Validare i parametri della Notification Request
    - Assicurarsi che la Notification Request includa `notification_id` e un tipo di evento valido.
  * - ISS-043
    - Security
    - Validare la Notification Response
    - Assicurarsi che la Notification Response sia ricevuta con il corretto status code.
  * - ISS-044
    - Security
    - Validare il flusso Refresh Token
    - Assicurarsi che il flusso Refresh Token sia usato correttamente e che i token siano legati alla chiave DPoP.
  * - ISS-045
    - Security
    - Validare la scadenza del Refresh Token
    - Assicurarsi che il Refresh Token non sia scaduto e sia usato entro il tempo consentito.
  * - ISS-046
    - Security
    - Validare i token sender-constrained
    - Assicurarsi che i Refresh Token siano crittograficamente legati alla Wallet Instance.
  * - ISS-047
    - Security
    - Limitare l'uso del Refresh Token
    - Assicurarsi che l'uso dei Refresh Token sia limitato e conforme alla specifica.
  * - ISS-048
    - Revocation
    - Validare la durata delle Wallet Attestation
    - Assicurarsi che le Wallet Attestation siano a breve durata o fornite con Status List se a lunga durata.
  * - ISS-049
    - Security
    - Validare il flusso di Re-Issuance
    - Assicurarsi che il flusso di Re-Issuance sia usato correttamente e conforme alla specifica.
  * - ISS-050
    - Security
    - Validare l'aggiornamento del Data Model/Format
    - Assicurarsi che l'aggiornamento del Data Model/Format sia gestito correttamente durante la Re-Issuance.
  * - ISS-051
    - Security
    - Validare l'aggiornamento del set di attributi utente
    - Assicurarsi che gli aggiornamenti del set di attributi utente siano gestiti correttamente durante la Re-Issuance.
  * - ISS-052
    - Security
    - Validare la scadenza della Credential in Re-Issuance
    - Assicurarsi che la nuova Credential abbia la stessa data di scadenza della precedente.
  * - ISS-053
    - Security
    - Validare l'autenticazione utente in Re-Issuance
    - Assicurarsi che l'autenticazione utente sia richiesta per la Re-Issuance dopo la scadenza della Credential.
  * - ISS-054
    - Security
    - Validare i parametri del Deferred Endpoint
    - Assicurarsi che i parametri del Deferred Endpoint siano usati correttamente e che la Credential sia emessa dopo il lead time specificato.
  * - ISS-055
    - Security
    - Validare la Deferred Credential Request
    - Assicurarsi che la Deferred Credential Request sia inviata correttamente e che la Credential sia emessa.
  * - ISS-056
    - Security
    - Validare la Deferred Credential Response
    - Assicurarsi che la Deferred Credential Response contenga tutti i parametri obbligatori e che i valori siano validati.
  * - ISS-057
    - Security
    - Validare i parametri del Notification Endpoint
    - Assicurarsi che i parametri del Notification Endpoint siano usati correttamente e che l'evento sia riportato.
  * - ISS-058
    - Security
    - Validare la gestione degli errori nel Notification Endpoint
    - Assicurarsi che gli errori nel Notification Endpoint siano gestiti correttamente e riportati.
  * - ISS-059
    - Security
    - Validare la gestione degli errori nel Credential Endpoint
    - Assicurarsi che gli errori nel Credential Endpoint siano gestiti correttamente e riportati.
  * - ISS-060
    - Security
    - Validare la gestione degli errori nel Token Endpoint
    - Assicurarsi che gli errori nel Token Endpoint siano gestiti correttamente e riportati.
  * - ISS-061
    - Security
    - Validare la gestione degli errori nell'Authorization Endpoint
    - Assicurarsi che gli errori nell'Authorization Endpoint siano gestiti correttamente e riportati.
  * - ISS-062
    - Error Handling
    - Validare la gestione degli errori nel PAR Endpoint
    - Assicurarsi che gli errori nel PAR Endpoint siano gestiti correttamente e riportati.
  * - ISS-063
    - Error Handling
    - Validare la gestione degli errori nel Nonce Endpoint
    - Assicurarsi che gli errori nel Nonce Endpoint siano gestiti correttamente e riportati.
  * - ISS-064
    - Error Handling
    - Validare la gestione degli errori nel Deferred Endpoint
    - Assicurarsi che gli errori nel Deferred Endpoint siano gestiti correttamente e riportati.
  * - ISS-065
    - Error Handling
    - Validare la gestione degli errori nel flusso di Re-Issuance
    - Assicurarsi che gli errori nel flusso di Re-Issuance siano gestiti correttamente e riportati.
  * - ISS-066
    - Error Handling
    - Validare la gestione degli errori nel flusso Refresh Token
    - Assicurarsi che gli errori nel flusso Refresh Token siano gestiti correttamente e riportati.
  * - ISS-067
    - Error Handling
    - Validare la gestione degli errori nell'emissione delle Credential
    - Assicurarsi che gli errori nel processo di emissione delle Credential siano gestiti correttamente e riportati.
  * - ISS-068
    - Error Handling
    - Validare la gestione degli errori nella Credential Request
    - Assicurarsi che gli errori nel processo di Credential Request siano gestiti correttamente e riportati.
  * - ISS-069
    - Error Handling
    - Validare la gestione degli errori nella Credential Response
    - Assicurarsi che gli errori nel processo di Credential Response siano gestiti correttamente e riportati.
  * - ISS-070
    - Error Handling
    - Validare la gestione degli errori nella Credential Validation
    - Assicurarsi che gli errori nel processo di Credential Validation siano gestiti correttamente e riportati.
  * - ISS-071
    - Error Handling
    - Validare la gestione degli errori nella Credential Integrity
    - Assicurarsi che gli errori nel processo di Credential Integrity siano gestiti correttamente e riportati.
  * - ISS-072
    - Error Handling
    - Validare la gestione degli errori nel Credential Type and Schema
    - Assicurarsi che gli errori nel processo di Credential Type and Schema siano gestiti correttamente e riportati.
  * - ISS-073
    - Error Handling
    - Validare la gestione degli errori nella Trust Chain Validation
    - Assicurarsi che gli errori nel processo di Trust Chain Validation siano gestiti correttamente e riportati.
  * - ISS-074
    - Error Handling
    - Validare la gestione degli errori nella Deferred Issuance
    - Assicurarsi che gli errori nel processo di Deferred Issuance siano gestiti correttamente e riportati.
  * - ISS-075
    - Error Handling
    - Validare la gestione degli errori nella Notification Handling
    - Assicurarsi che gli errori nel processo di Notification Handling siano gestiti correttamente e riportati.
  * - ISS-076
    - Error Handling
    - Validare la gestione degli errori nell'User Authentication
    - Assicurarsi che gli errori nel processo di User Authentication siano gestiti correttamente e riportati.
  * - ISS-077
    - Error Handling
    - Validare la gestione degli errori nell'User Consent
    - Assicurarsi che gli errori nel processo di User Consent siano gestiti correttamente e riportati.
  * - ISS-078
    - Error Handling
    - Validare la gestione degli errori nell'User Notification
    - Assicurarsi che gli errori nel processo di User Notification siano gestiti correttamente e riportati.
  * - ISS-079
    - Error Handling
    - Validare la gestione degli errori nell'aggiornamento del set di attributi utente
    - Assicurarsi che gli errori nel processo di aggiornamento del set di attributi utente siano gestiti correttamente e riportati.
  * - ISS-080
    - Error Handling
    - Validare la gestione degli errori nell'aggiornamento del Data Model/Format
    - Assicurarsi che gli errori nel processo di aggiornamento del Data Model/Format siano gestiti correttamente e riportati.
  * - ISS-081
    - Error Handling
    - Validare la gestione degli errori nella scadenza della Credential
    - Assicurarsi che gli errori nel processo di scadenza della Credential siano gestiti correttamente e riportati.
  * - ISS-082
    - Error Handling
    - Validare la gestione degli errori nella Re-Issuance della Credential
    - Assicurarsi che gli errori nel processo di Re-Issuance della Credential siano gestiti correttamente e riportati.
  * - ISS-083
    - Error Handling
    - Validare la gestione degli errori nel Credential Binding
    - Assicurarsi che gli errori nel processo di Credential Binding siano gestiti correttamente e riportati.
  * - ISS-084
    - Error Handling
    - Validare la gestione degli errori nella Credential Trust Evaluation
    - Assicurarsi che gli errori nel processo di Credential Trust Evaluation siano gestiti correttamente e riportati.
  * - ISS-085
    - Error Handling
    - Validare la gestione degli errori nel recupero dei metadata della Credential
    - Assicurarsi che gli errori nel processo di recupero dei metadata della Credential siano gestiti correttamente e riportati.
  * - ISS-086
    - Error Handling
    - Validare la gestione degli errori nella Credential Discovery
    - Assicurarsi che gli errori nel processo di Credential Discovery siano gestiti correttamente e riportati.
  * - ISS-087
    - Error Handling
    - Validare la gestione degli errori nella valutazione della Credential Offer
    - Assicurarsi che gli errori nel processo di valutazione della Credential Offer siano gestiti correttamente e riportati.
  * - ISS-088
    - Error Handling
    - Validare la gestione degli errori nell'accettazione della Credential Offer
    - Assicurarsi che gli errori nel processo di accettazione della Credential Offer siano gestiti correttamente e riportati.
  * - ISS-089
    - Error Handling
    - Validare la gestione degli errori nel rifiuto della Credential Offer
    - Assicurarsi che gli errori nel processo di rifiuto della Credential Offer siano gestiti correttamente e riportati.
  * - ISS-090
    - Error Handling
    - Validare la gestione degli errori nella revoca della Credential Offer
    - Assicurarsi che gli errori nel processo di revoca della Credential Offer siano gestiti correttamente e riportati.
  * - ISS-091
    - Error Handling
    - Validare la gestione degli errori nella scadenza della Credential Offer
    - Assicurarsi che gli errori nel processo di scadenza della Credential Offer siano gestiti correttamente e riportati.
  * - ISS-092
    - Error Handling
    - Validare la gestione degli errori nel rinnovo della Credential Offer
    - Assicurarsi che gli errori nel processo di rinnovo della Credential Offer siano gestiti correttamente e riportati.
  * - ISS-093
    - Error Handling
    - Validare la gestione degli errori nell'aggiornamento della Credential Offer
    - Assicurarsi che gli errori nel processo di aggiornamento della Credential Offer siano gestiti correttamente e riportati.
  * - ISS-094
    - Error Handling
    - Validare la gestione degli errori nella validazione della Credential Offer
    - Assicurarsi che gli errori nel processo di validazione della Credential Offer siano gestiti correttamente e riportati.
  * - ISS-095
    - Error Handling
    - Validare la gestione degli errori nella verifica della Credential Offer
    - Assicurarsi che gli errori nel processo di verifica della Credential Offer siano gestiti correttamente e riportati.
  * - ISS-096
    - Error Handling
    - Validare la gestione degli errori nella conferma della Credential Offer
    - Assicurarsi che gli errori nel processo di conferma della Credential Offer siano gestiti correttamente e riportati.
  * - ISS-097
    - Error Handling
    - Validare la gestione degli errori nella notifica della Credential Offer
    - Assicurarsi che gli errori nel processo di notifica della Credential Offer siano gestiti correttamente e riportati.
  * - ISS-098
    - Error Handling
    - Validare la gestione degli errori nella comunicazione della Credential Offer
    - Assicurarsi che gli errori nel processo di comunicazione della Credential Offer siano gestiti correttamente e riportati.
  * - ISS-099
    - Error Handling
    - Validare la gestione degli errori nella trasmissione della Credential Offer
    - Assicurarsi che gli errori nel processo di trasmissione della Credential Offer siano gestiti correttamente e riportati.
  * - ISS-100
    - Error Handling
    - Validare la gestione degli errori nella ricezione della Credential Offer
    - Assicurarsi che gli errori nel processo di ricezione della Credential Offer siano gestiti correttamente e riportati.
  * - ISS-101
    - Error Handling
    - Validare la gestione degli errori nel processing della Credential Offer
    - Assicurarsi che gli errori nel processo di processing della Credential Offer siano gestiti correttamente e riportati.
  * - ISS-102
    - Error Handling
    - Validare la gestione degli errori nell'handling della Credential Offer
    - Assicurarsi che gli errori nel processo di handling della Credential Offer siano gestiti correttamente e riportati.
  * - ISS-103
    - Error Handling
    - Validare la gestione degli errori nel management della Credential Offer
    - Assicurarsi che gli errori nel processo di management della Credential Offer siano gestiti correttamente e riportati.
  * - ISS-104
    - Error Handling
    - Validare la gestione degli errori nell'amministrazione della Credential Offer
    - Assicurarsi che gli errori nel processo di amministrazione della Credential Offer siano gestiti correttamente e riportati.
  * - ISS-105
    - Error Handling
    - Validare la gestione degli errori nel controllo della Credential Offer
    - Assicurarsi che gli errori nel processo di controllo della Credential Offer siano gestiti correttamente e riportati.
  * - ISS-106
    - Error Handling
    - Validare la gestione degli errori nella supervisione della Credential Offer
    - Assicurarsi che gli errori nel processo di supervisione della Credential Offer siano gestiti correttamente e riportati.
  * - ISS-107
    - Error Handling
    - Validare la gestione degli errori nella sorveglianza della Credential Offer
    - Assicurarsi che gli errori nel processo di sorveglianza della Credential Offer siano gestiti correttamente e riportati.
  * - ISS-108
    - Error Handling
    - Validare la gestione degli errori nel monitoraggio della Credential Offer
    - Assicurarsi che gli errori nel processo di monitoraggio della Credential Offer siano gestiti correttamente e riportati.
  * - ISS-109
    - Error Handling
    - Validare la gestione degli errori nella valutazione della Credential Offer
    - Assicurarsi che gli errori nel processo di valutazione della Credential Offer siano gestiti correttamente e riportati.
  * - ISS-110
    - Error Handling
    - Validare la gestione degli errori nell'assessment della Credential Offer
    - Assicurarsi che gli errori nel processo di assessment della Credential Offer siano gestiti correttamente e riportati.


Matrice di Test per la Presentazione di Credenziali in Prossimità
-----------------------------------------------------------------

Questa sezione fornisce l'insieme dei casi di test progettati per implementatori tecnici e team di sviluppo responsabili della creazione e del deployment di soluzioni Credential Verifier per i flussi di prossimità. È anche destinata agli organismi di valutazione che ispezionano e validano le implementazioni di soluzioni Credential Verifier per i flussi di prossimità.

.. note::
  Ulteriori riferimenti sui piani di test ufficiali ISO-18013-5, se disponibili, aggiorneranno questa sezione nelle versioni future.


.. list-table::
  :class: longtable
  :widths: 15 15 35 35
  :header-rows: 1

  * - Test Case ID
    - Purpose
    - Description
    - Expected Result

  * - PPR-001
    - Device Engagement
    - Testare l'avvio del device engagement utilizzando QR code.
    - Il device engagement viene avviato con successo e il QR code viene scansionato.

  * - PPR-002
    - Session Establishment
    - Verificare l'instaurazione della sessione con le session key corrette.
    - La sessione viene stabilita in modo sicuro con le session key corrette.

  * - PPR-003
    - Communication
    - Testare la trasmissione della mdoc request tramite BLE.
    - La mdoc request viene trasmessa in modo sicuro tramite BLE.

  * - PPR-004
    - User Authentication
    - Validare l'autenticazione dell'utente tramite WSCA.
    - L'utente viene autenticato con successo utilizzando WSCA.

  * - PPR-005
    - Attribute Consent
    - Verificare il consenso dell'utente per il rilascio degli attributi.
    - L'utente acconsente al rilascio degli attributi richiesti.

  * - PPR-006
    - Data Retrieval
    - Testare il recupero delle mdoc Digital Credentials.
    - Le mdoc Digital Credentials vengono recuperate con successo.

  * - PPR-007
    - Session Termination
    - Verificare la terminazione della sessione dopo lo scambio di dati.
    - La sessione viene terminata e le chiavi vengono distrutte.

  * - PPR-008
    - Error Handling
    - Testare la gestione di session key non valide.
    - Viene visualizzato un messaggio di errore appropriato per chiavi non valide.

  * - PPR-009
    - BLE Connection
    - Testare la stabilità della connessione BLE durante lo scambio di dati.
    - La connessione BLE rimane stabile durante tutto lo scambio.

  * - PPR-010
    - Document Verification
    - Verificare l'integrità dei documenti ricevuti.
    - I documenti vengono verificati e l'integrità è confermata.

  * - PPR-011
    - Security
    - Testare la crittografia delle mdoc request e response.
    - Tutte le mdoc request e response vengono crittografate correttamente.

  * - PPR-012
    - User Interface
    - Verificare l'interfaccia utente per il consenso agli attributi.
    - L'interfaccia utente visualizza chiaramente la richiesta di consenso agli attributi.

  * - PPR-013
    - Error Handling
    - Testare la risposta a tipi di documento non supportati.
    - Il sistema restituisce un errore appropriato per tipi di documento non supportati.

  * - PPR-014
    - Performance
    - Misurare il tempo impiegato per l'instaurazione della sessione.
    - La sessione viene stabilita entro limiti di tempo accettabili.

  * - PPR-015
    - Compatibility
    - Verificare la compatibilità con diversi dispositivi mobili.
    - Il sistema funziona senza problemi su vari dispositivi mobili.

  * - PPR-016
    - Data Integrity
    - Testare l'integrità dei dati durante la trasmissione.
    - L'integrità dei dati viene mantenuta durante la trasmissione.

  * - PPR-017
    - Session Management
    - Testare la gestione delle sessioni sotto carico elevato.
    - Le sessioni vengono gestite efficacemente in condizioni di carico elevato.

  * - PPR-018
    - BLE Connection
    - Testare la riconnessione dopo la disconnessione BLE.
    - Il sistema si riconnette con successo dopo la disconnessione BLE.

  * - PPR-019
    - User Experience
    - Valutare l'esperienza utente durante il flusso di prossimità.
    - Gli utenti riportano un'esperienza positiva con il flusso di prossimità.

  * - PPR-020
    - Security
    - Testare la resistenza agli attacchi replay.
    - Il sistema è resistente agli attacchi replay.

  * - PPR-021
    - Device Engagement
    - Verificare che la struttura Device Engagement sia codificata in CBOR.
    - La struttura Device Engagement è correttamente codificata in formato CBOR.

  * - PPR-022
    - Device Engagement
    - Testare che la chiave pubblica effimera sia del tipo consentito dalla suite di cifratura.
    - La chiave pubblica effimera rispetta i requisiti della suite di cifratura selezionata.

  * - PPR-023
    - BLE Configuration
    - Verificare che solo la modalità Central Client sia supportata.
    - La modalità Central Client è supportata per le connessioni BLE.

  * - PPR-024
    - Capabilities
    - Testare che ``HandoverSessionEstablishmentSupport`` sia impostato su ``true`` quando presente.
    - ``HandoverSessionEstablishmentSupport`` è correttamente impostato su ``true``.

  * - PPR-025
    - Capabilities
    - Verificare che ``ReaderAuthAllSupport`` sia impostato su ``true`` quando presente.
    - ``ReaderAuthAllSupport`` è correttamente impostato su ``true``.

  * - PPR-026
    - mdoc Request
    - Testare che i messaggi mdoc Request siano codificati in CBOR.
    - I messaggi mdoc Request sono correttamente codificati in formato CBOR.

  * - PPR-027
    - mdoc Request
    - Verificare che la richiesta mdoc sia cifrata con la chiave di sessione.
    - La richiesta mdoc è correttamente cifrata con la chiave di sessione.

  * - PPR-028
    - mdoc Request
    - Testare che la richiesta mdoc sia trasmessa tramite protocollo BLE.
    - La richiesta mdoc è trasmessa correttamente tramite protocollo BLE.

  * - PPR-029
    - mdoc Response
    - Verificare che i messaggi mdoc Response siano codificati in CBOR.
    - I messaggi mdoc Response sono correttamente codificati in formato CBOR.

  * - PPR-030
    - mdoc Response
    - Testare che la risposta mdoc sia cifrata con la chiave di sessione.
    - La risposta mdoc è correttamente cifrata con la chiave di sessione.

  * - PPR-031
    - Key Management
    - Testare che la chiave effimera privata sia mantenuta segreta.
    - La chiave effimera privata è adeguatamente protetta e non esposta.

  * - PPR-032
    - Key Management
    - Testare che la chiave effimera pubblica sia usata nell'instaurazione della sessione.
    - La chiave effimera pubblica è utilizzata correttamente per l'instaurazione della sessione.

  * - PPR-033
    - Derivazione Chiavi di Sessione
    - Testare che le chiavi di sessione siano derivate con il protocollo di accordo chiavi.
    - Le chiavi di sessione sono derivate correttamente usando il protocollo di accordo chiavi.

  * - PPR-034
    - Session Establishment
    - Testare che il messaggio ``SessionEstablishment`` sia preparato correttamente.
    - Il messaggio ``SessionEstablishment`` è preparato correttamente con i componenti richiesti.

  * - PPR-035
    - Session Establishment
    - Testare che il messaggio ``SessionEstablishment`` sia firmato dalla RP Instance.
    - Il messaggio ``SessionEstablishment`` è firmato correttamente dalla Relying Party Instance.

  * - PPR-036
    - Session Establishment
    - Testare che il messaggio ``SessionEstablishment`` sia cifrato con le chiavi di sessione.
    - Il messaggio ``SessionEstablishment`` è correttamente cifrato con le chiavi di sessione.

  * - PPR-037
    - Session Establishment
    - Testare che ``SessionEstablishment`` includa ``EReaderKey.Pub`` e la richiesta di attributi.
    - Il messaggio ``SessionEstablishment`` include ``EReaderKey.Pub`` e la richiesta di attributi richiesti.

  * - PPR-038
    - Trasmissione Messaggi
    - Testare che ``SessionEstablishment`` sia trasmesso su connessione BLE sicura.
    - Il messaggio ``SessionEstablishment`` è trasmesso su connessione BLE sicura.

  * - PPR-039
    - Calcolo Chiave di Sessione
    - Testare che l'Istanza del Wallet calcoli correttamente la chiave di sessione.
    - L'Istanza del Wallet calcola correttamente la chiave di sessione.

  * - PPR-040
    - Decrittazione Messaggi
    - Testare che l'Istanza del Wallet decritti il messaggio ``SessionEstablishment``.
    - L'Istanza del Wallet decritta con successo il messaggio ``SessionEstablishment``.

  * - PPR-041
    - Verifica Firma
    - Testare che l'Istanza del Wallet verifichi la firma della RP Instance.
    - L'Istanza del Wallet verifica correttamente la firma della Relying Party Instance.

  * - PPR-042
    - Elaborazione Richiesta Attributi
    - Testare che l'Istanza del Wallet decritti la richiesta di attributi.
    - L'Istanza del Wallet decritta con successo la richiesta di attributi.

  * - PPR-043
    - Consenso Utente
    - Testare che l'Istanza del Wallet richieda il consenso all'utente.
    - L'Istanza del Wallet richiede correttamente il consenso al rilascio degli attributi.

  * - PPR-044
    - Visualizzazione Certificato
    - Testare che l'Istanza del Wallet mostri il Certificato di Registrazione della RP.
    - L'Istanza del Wallet mostra il Certificato di Registrazione della Relying Party per trasparenza.

  * - PPR-045
    - Recupero Credenziali
    - Testare che l'Istanza del Wallet recuperi le mdoc Digital Credentials richieste.
    - L'Istanza del Wallet recupera con successo le mdoc Digital Credentials richieste.

  * - PPR-046
    - Preparazione ``SessionData``
    - Testare che l'Istanza del Wallet prepari il messaggio ``SessionData``.
    - L'Istanza del Wallet prepara correttamente il messaggio ``SessionData`` con le Digital Credentials.

  * - PPR-047
    - Firma Dati di Autenticazione
    - Testare che l'Istanza del Wallet firmi i dati di autenticazione richiesti.
    - L'Istanza del Wallet firma correttamente i dati di autenticazione richiesti.

  * - PPR-048
    - Cifratura Messaggi
    - Testare che ``SessionData`` sia cifrato con le chiavi di sessione.
    - Il messaggio ``SessionData`` è correttamente cifrato con le chiavi di sessione.

  * - PPR-049
    - Codifica CBOR
    - Testare che la response mdoc sia codificata in formato CBOR.
    - La response mdoc è correttamente codificata in formato CBOR.

  * - PPR-050
    - Verifica Dati
    - Testare che la RP Instance decritti ``SessionData``.
    - La Relying Party Instance decritta con successo ``SessionData``.

  * - PPR-051
    - Verifica Firma
    - Testare che la RP Instance verifichi la firma dell'Istanza del Wallet.
    - La Relying Party Instance verifica correttamente la firma dell'Istanza del Wallet.

  * - PPR-052
    - Validazione Documenti
    - Testare che la RP Instance controlli la validità dell'mdoc e la firma dell'Issuer.
    - La Relying Party Instance valida correttamente l'mdoc e la firma dell'Issuer.

  * - PPR-053
    - Disconnessione BLE
    - Testare che il GATT Client si disiscriva dalle caratteristiche.
    - Il GATT Client si disiscrive correttamente dalle caratteristiche.

  * - PPR-054
    - Disconnessione BLE
    - Testare che il GATT Client si disconnetta dal server GATT.
    - Il GATT Client si disconnette correttamente dal server GATT.

  * - PPR-055
    - Conformità Struttura Request
    - Testare che la mdoc Request sia conforme alla struttura richiesta.
    - La mdoc Request è conforme alla struttura richiesta e include i componenti necessari.

  * - PPR-056
    - Conformità Struttura Response
    - Testare che la mdoc Response sia conforme alla struttura richiesta.
    - La mdoc Response è conforme alla struttura richiesta e include i componenti necessari.

  * - PPR-057
    - Conformità Struttura Documenti
    - Testare che i documenti siano conformi alla struttura richiesta.
    - I documenti sono conformi alla struttura richiesta e includono i componenti necessari.

  * - PPR-058
    - Validazione Tipo Documento
    - Testare che il tipo documento mDL sia impostato correttamente.
    - Il tipo documento mDL è impostato correttamente su ``org.iso.18013.5.1.mDL``.

  * - PPR-059
    - Struttura DeviceSigned
    - Testare che la struttura ``deviceSigned`` sia conforme.
    - La struttura ``deviceSigned`` è conforme al formato richiesto e include i componenti necessari.

  * - PPR-060
    - Autenticazione Dispositivo
    - Testare che ``deviceAuth`` includa ``deviceSignature``.
    - La struttura ``deviceAuth`` include ``deviceSignature`` richiesto per l'autenticazione.

  * - PPR-061
    - Inclusione Wallet Attestation
    - Testare che l'Istanza del Wallet includa il Wallet Attestation quando richiesto.
    - L'Istanza del Wallet include il Wallet Attestation quando richiesto dalla Relying Party.

  * - PPR-062
    - Inclusione Claim AAL
    - Testare che l'Istanza del Wallet includa il claim ``aal`` nel Wallet Attestation.
    - L'Istanza del Wallet include il claim ``aal`` come disclosure nel Wallet Attestation.

  * - PPR-063
    - Bypass Consenso Utente
    - Testare che l'Istanza del Wallet non richieda il consenso utente per il Wallet Attestation.
    - L'Istanza del Wallet non richiede il consenso per gli attributi tecnici del Wallet Attestation.

  * - PPR-064
    - Condizioni di Terminazione Sessione
    - Testare che la sessione venga terminata alle condizioni specificate.
    - La sessione è terminata correttamente quando si verificano le condizioni specificate.

  * - PPR-065
    - Avvio Terminazione Sessione
    - Testare che la terminazione della sessione sia avviata correttamente.
    - La terminazione della sessione è avviata correttamente quando non vengono inviate ulteriori richieste.

  * - PPR-066
    - Distruzione Chiavi
    - Testare che le chiavi di sessione siano distrutte alla terminazione.
    - Le chiavi di sessione e il materiale effimero sono distrutti correttamente.

  * - PPR-067
    - Chiusura Canale
    - Testare che il canale di comunicazione sia chiuso alla terminazione.
    - Il canale di comunicazione usato per il recupero dati è chiuso correttamente.

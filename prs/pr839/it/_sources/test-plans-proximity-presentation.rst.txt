
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

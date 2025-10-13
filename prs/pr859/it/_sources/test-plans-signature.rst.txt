Matrice di Test per la Valutazione delle Firme
----------------------------------------------

Questa sezione fornisce l'insieme comune di casi di test per le Soluzioni Wallet, le Relying Party e i Credential Issuer per la valutazione di qualsiasi dichiarazione firmata, siano queste asserzioni, richieste, attestazioni o Credenziali.


.. list-table::
  :class: longtable
  :widths: 15 15 35 35
  :header-rows: 1

  * - Test Case ID
    - Purpose
    - Description
    - Expected Result
  * - ATT-001
    - Discovery, Security
    - Valutazione dell'emittente
    - Le entità che valutano dichiarazioni firmate stabiliscono fiducia con l'emittente e ne valutano la conformità. Emittenti non scopribili all'interno della federazione o non collegabili a qualsiasi Trust Anchor noto, interrompono qualsiasi comunicazione di protocollo.
  * - ATT-002
    - Discovery, Security
    - Valutazione della firma
    - Le entità valutano le dichiarazioni firmate verificando la firma con il materiale crittografico dell'emittente, a condizione che sia considerato attendibile attraverso un Trust Anchor ben noto. Qualsiasi materiale crittografico non attendibile o firme non valide interrompono le comunicazioni di protocollo.
  * - ATT-003
    - Algorithm Verification
    - Verificare che l'algoritmo specificato nell'header corrisponda a quello utilizzato per le operazioni crittografiche.
    - L'algoritmo nell'header deve corrispondere all'operazione crittografica.
  * - ATT-004
    - Appropriate Algorithms
    - Assicurarsi che vengano utilizzati solo algoritmi crittograficamente attuali.
    - Solo gli algoritmi approvati sono accettati; quelli deprecati sono rifiutati.
  * - ATT-005
    - Signature Validation
    - Validare tutte le operazioni crittografiche e rifiutare se qualsiasi operazione fallisce.
    - Tutte le firme devono essere valide; qualsiasi fallimento risulta in un rifiuto.
  * - ATT-006
    - Key Entropy
    - Assicurarsi che le chiavi crittografiche abbiano entropia sufficiente.
    - Le chiavi devono soddisfare i requisiti di entropia; le chiavi deboli sono rifiutate.
  * - ATT-007
    - Issuer Validation
    - Validare che le chiavi crittografiche appartengano all'emittente.
    - Le chiavi devono essere verificate come appartenenti all'emittente.
  * - ATT-008
    - Audience Validation
    - Validare il claim audience per assicurarsi che il token sia utilizzato dalla parte destinata.
    - Il claim audience deve corrispondere al destinatario previsto.
  * - ATT-009
    - Claim Trust
    - Non fidarsi dei claim ricevuti senza validazione.
    - I claim devono essere validati; i claim non attendibili sono rifiutati.
  * - ATT-010
    - Explicit Typing
    - Utilizzare il typing esplicito per prevenire confusione COSE/JOSE.
    - Il typing deve essere esplicito e validato.
  * - ATT-011
    - Cross-JWT Confusion
    - Prevenire l'uso di COSE/JOSE in contesti non intesi.
    - COSE/JOSE deve essere validato contestualmente per prevenire uso improprio.
  * - ATT-012
    - Substitution Attacks
    - Assicurarsi che COSE/JOSE non siano sostituiti in contesti diversi.
    - COSE/JOSE deve essere validato per l'uso specifico del contesto.
  * - ATT-013
    - Issued At Validation
    - Verificare che il parametro `issued at` sia impostato all'ora corrente, permettendo un periodo di grazia non superiore a 120 secondi.
    - Il valore `issued at` deve essere entro 120 secondi dall'ora corrente.
  * - ATT-014
    - Expiration Validation
    - Assicurarsi che il tempo di `expiration` sia maggiore del tempo `issued at`.
    - Il tempo di `expiration` deve essere successivo al tempo `issued at`.
  * - ATT-015
    - Data model validation
    - Assicurarsi che il tipo JOSE/COSE corrisponda al data model definito.
    - I parametri o claim, i loro valori e lo schema utilizzato per rappresentarli sono conformi al data model.

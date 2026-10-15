.. include:: ../common/common_definitions.rst


.. _identity-matching:

Identity Matching e Identity Reconciliation
===========================================

L'**identity matching** è il processo con cui una Relying Party accerta che gli attributi di identificazione personale presentati in una transazione si riferiscano alla stessa persona fisica. È lo stesso approccio pratico già utilizzato in qualsiasi infrastruttura legacy di autenticazione e autorizzazione. Non è una funzionalità dell'Istanza del Wallet, né un passo del protocollo di presentazione. La verifica crittografica dell'Attestato Elettronico resta un prerequisito distinto, e l'identity reconciliation è un passo successivo e opzionale.

Dopo la verifica crittografica di un Attestato Elettronico presentato, nei flussi remoto o di prossimità, la Relying Party DEVE prima effettuare l'**identity matching**, per accertare che gli attributi di identificazione personale presentati nella transazione corrente si riferiscano alla stessa persona fisica. Solo dopo un identity matching andato a buon fine, la Relying Party PUÒ effettuare l'**identity reconciliation**, collegando quella persona fisica a una precedente sessione Utente o a un record Utente memorizzato.

Se l'identity matching fallisce, la Relying Party NON DEVE effettuare l'identity reconciliation e NON DEVE trattare chi presenta l'Attestato Elettronico come un Utente già noto.

Questa Sezione specifica le regole di matching e reconciliation che si applicano agli Attestati Elettronici di identificazione personale (PID e IT-Wallet ID). La correlazione delle identità durante l'emissione dell'IT-Wallet ID (IdP–MRTD) è specificata in :ref:`credential-issuance-l2plus:Autenticazione eID Substantial con Verifica MRTD per Emissione IT-Wallet ID` ed è fuori dallo scopo di questa Sezione.

Identity Matching
-----------------

L'identity matching determina se gli attributi di identificazione personale presentati identificano una sola persona fisica.

La Relying Party DEVE applicare il pattern di matching del tipo di Attestato Elettronico presentato, come definito di seguito. Tipi diversi di Attestato Elettronico POSSONO definire pattern di identity matching differenti. Per gli attributi Utente del PID, vedere :ref:`credential-data-model-pid:Modello di Dati del PID`. Per gli attributi Utente dell'IT-Wallet ID, vedere :ref:`credential-data-model-it-wallet-id:Modello di Dati dell'IT-Wallet ID`.

Identity Reconciliation
-----------------------

L'identity reconciliation è il passo successivo che associa una persona fisica identificata con successo a un record Utente o a una sessione della Relying Party.

La Relying Party NON DEVE completare l'identity reconciliation se l'identity matching non è andato a buon fine. La reconciliation PUÒ creare un nuovo record Utente quando nessun record memorizzato corrisponde.

Pattern di Matching per Tipo di Attestato Elettronico
-----------------------------------------------------

Unique National Identifier Binding
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Quando è presentato ``personal_administrative_number`` o ``tax_id_code``, la Relying Party DEVE utilizzarlo come chiave primaria di identity matching prima di qualsiasi identity reconciliation con un record Utente memorizzato (:ref:`CI_201 <credential-issuer-testcases>`).

Per l'IT-Wallet ID è presente almeno uno tra ``tax_id_code`` e ``personal_administrative_number``. La Relying Party DEVE utilizzare l'identificativo nazionale univoco presentato come chiave primaria di matching.

Attribute-Based Binding
^^^^^^^^^^^^^^^^^^^^^^^

Per il PID, ``personal_administrative_number`` è OPZIONALE. Le Relying Party NON DEVONO assumere che un identificativo nazionale univoco sia sempre disponibile.

Quando ``personal_administrative_number`` non è presentato, la Relying Party DEVE effettuare *Attribute-Based Binding* confrontando almeno ``family_name``, ``given_name``, ``birth_date`` (o ``birthdate``) e ``place_of_birth`` dopo normalizzazione di maiuscole/minuscole, spazi e diacritici. La Relying Party DEVE applicare la stessa normalizzazione agli attributi presentati e al record Utente memorizzato, inclusi i membri stringa di ``place_of_birth`` (``country``, ``region``, ``locality``). Il confronto della data di nascita DEVE usare la data di calendario ISO 8601 (``YYYY-MM-DD``), indipendentemente dal formato di visualizzazione.

La Relying Party NON DEVE completare l'identity matching su un sottoinsieme di tali attributi che consentirebbe uno scambio di persona (:ref:`CI_202 <credential-issuer-testcases>`). In particolare:

- il matching della sola coppia di nomi, del solo nome e della data di nascita, o di qualsiasi sottoinsieme che ometta ``place_of_birth``, NON DEVE essere trattato come identity matching andato a buon fine;
- una discordanza su qualsiasi attributo del set minimo DEVE far fallire l'identity matching; la Relying Party NON DEVE ignorare una discordanza sul nome attuale (ad esempio dopo un cambio di nome) per forzare un match;
- se l'Attribute-Based Binding corrisponde a più di un record Utente memorizzato, la Relying Party NON DEVE completare l'identity matching. PUÒ richiedere un identificativo nazionale univoco, oppure applicare un metodo di binding supplementare che identifichi univocamente la persona.

Metodi di Binding Supplementari
-------------------------------

I metodi seguenti POSSONO integrare l'Attribute-Based Binding. NON DEVONO sostituire il set minimo di Attribute-Based Binding quando non è presentato un identificativo nazionale univoco:

- **Session-Based Binding**: la presentazione avviene all'interno di una sessione autenticata già associata all'Utente;
- **Issuer-Attested Binding**: l'Issuer attesta che gli attributi presentati appartengono allo stesso soggetto (ad esempio tramite un identificativo di soggetto stabile dell'Issuer);
- **Identificativi specifici della Relying Party**: identificativi precedentemente emessi dalla Relying Party a quell'Utente dopo un identity matching andato a buon fine;
- **Cryptographic Binding**: dimostrando che le chiavi private degli Attestati Elettronici presentati sono gestite dallo stesso Keystore o WSCD.

Privacy e Selective Disclosure
------------------------------

La Selective Disclosure DEVE essere utilizzata affinché gli attributi identificativi necessari solo per il matching non siano rilasciati quando non richiesti dalla specifica transazione, in linea con l'Articolo 5a del Regolamento sull'Identità Digitale Europea e con i principi di combined presentation privacy-preserving dell'ARF, da considerarsi pienamente applicabili quando IT-Wallet sarà notificato come soluzione EUDIW.

Applicazione all'Eliminazione degli Attributi dell'Utente
---------------------------------------------------------

Quando l'Utente richiede la cancellazione degli attributi presentati, la Relying Party DEVE individuare univocamente uno o più Attestati Elettronici applicando l'identity matching, come specificato in :ref:`user-attribute-deletion:Eliminazione degli Attributi dell'Utente`.

Quando l'Utente si autentica all'Endpoint di Cancellazione presentando un Attestato Elettronico dall'Istanza del Wallet, la Relying Party DEVE applicare i pattern di matching di questa Sezione.

Quando l'Utente si autentica all'Endpoint di Cancellazione senza usare l'Istanza del Wallet, la Relying Party PUÒ effettuare l'identity matching e l'identity reconciliation utilizzando gli attributi di identificazione personale ottenuti da uno schema nazionale di autenticazione preesistente (ad esempio CieID), ove tali attributi identifichino univocamente l'Utente nei record della Relying Party.

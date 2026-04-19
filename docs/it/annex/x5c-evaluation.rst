Operazioni di Gestione dei Certificati X.509
=============================================

Questa sezione descrive il lavoro PKIX che gli operatori svolgono quando il materiale certificato è già presente nel dispiegamento. Le attività tipiche includono la costruzione delle catene, la verifica di firme ed estensioni, il controllo della revoca, la pianificazione del rinnovo prima della scadenza e la dismissione delle credenziali non più autorizzate.

Il rapporto tra enrolment OpenID Federation e PKIX, nonché le regole per richiedere i bundle certificati, sono chiariti in :ref:`trust-infrastructure:L'Infrastruttura di Trust` e in :ref:`trust-infrastructure:X.509 PKI`. Questa sezione resta sul piano PKIX. Le valutazioni DEVONO basarsi su librerie PKIX consolidate o su strumenti da riga di comando per X.509, anziché dedurre la fiducia solo dai metadati di federazione.

Classi di certificati PKI IT-Wallet
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Il testo normativo di emissione PKIX resta in :ref:`trust-infrastructure:X.509 PKI`. I livelli seguenti riassumono come IT-Wallet raggruppa il materiale PKIX a scopo orientativo.

	- **Trust Anchor**: certificati della CA radice X.509 che NON DEVONO superare un periodo di validità di **5 anni**.
	- **Certificato di emissione dell'entità**: certificato sub-CA limitato rilasciato da un superiore a un partecipante autorizzato a emettere ulteriori certificati X.509 entro vincoli (in questo profilo, Intermediari di Federazione); tale certificato NON DEVE superare un periodo di validità di **2 anni**. Le Foglie di Federazione NON DEVONO ricoprire questo ruolo.
	- **Certificato di protocollo**: certificato end-entity o di servizio (``CA:FALSE``) per uso applicativo. Le Foglie di Federazione NON DEVONO auto-emetterlo; i loro certificati di protocollo DEVONO essere rilasciati da un Superiore Immediato (o da una CA delegata sotto quel superiore). NON DOVREBBE superare un periodo di validità di **1 anno**.

Per i certificati X.509 di protocollo con validità superiore a ventiquattro ore, l'emittente DEVE pubblicare e mantenere una CRL come specificato in :ref:`trust-infrastructure:X.509 PKI`.

Struttura e Analisi della Catena di Certificati X.509
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

I partecipanti ricevono di norma le catene durante i flussi di onboarding definiti altrove in questa specifica. Indipendentemente dal canale di consegna, ogni partecipante DEVE validare in PKIX la catena per il proprio uso prima di affidarsi ad essa.

Visualizzazione della Catena di Certificati X.509
"""""""""""""""""""""""""""""""""""""""""""""""""""

Lo script seguente è un ausilio non normativo. Aiuta gli operatori a estrarre i campi del certificato, ispezionare estensioni e vincoli e rivedere la gerarchia che collega i certificati end-entity ai propri emittenti.

.. literalinclude:: ../../../utils/certificate-chain-analysis.sh
   :language: bash
   :caption: Script di analisi della catena di Certificati X.509


Validazione della Catena di Certificati X.509
"""""""""""""""""""""""""""""""""""""""""""""

Ogni partecipante DEVE validare in PKIX ogni catena ricevuta in conformità a `RFC 5280`_ e al profilo PKIX IT-Wallet in :ref:`trust-infrastructure:X.509 PKI`. La validazione copre firme, continuità emittente–soggetto, finestre di validità e ogni estensione che il profilo renda obbligatoria.

Esempio non normativo:

.. literalinclude:: ../../../utils/certificate-chain-validation.sh
   :language: bash
   :caption: Script di validazione della catena di Certificati X.509


Le attese dettagliate sulle estensioni per i certificati di emissione rispetto ai certificati di protocollo sono in :ref:`trust-infrastructure:X.509 PKI`.

Gestione della Revoca dei Certificati X.509
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

I partecipanti DEVONO implementare il controllo PKIX della revoca per ogni certificato di cui i propri sistemi si avvalgono per autenticazione, firma o protezione del trasporto.

Distribuzione e Accesso CRL
""""""""""""""""""""""""""""

Gli emittenti pubblicano CRL su endpoint raggiungibili senza credenziali particolari. I partecipanti DEVONO scaricare una CRL, interpretarla e associare i numeri seriali alle voci di revoca ogni volta che il profilo PKIX lo richiede.

Lo script seguente illustra in modo non normativo come individuare i punti di distribuzione CRL sul certificato, recuperare l'elenco corrente e verificarne i campi di aggiornamento.

.. literalinclude:: ../../../utils/crl-analysis.sh
   :language: bash


Verifica della Revoca dei Certificati X.509
"""""""""""""""""""""""""""""""""""""""""""

I partecipanti DEVONO determinare lo stato di revoca confrontando ogni numero seriale con la CRL autoritativa (o con un altro meccanismo PKIX adottato dal dispiegamento). DOVREBBERO automatizzare tale attività per il proprio materiale PKIX, per il materiale delle controparti di cui si fidano e per ogni certificato intermedio ancora presente in una catena attiva.

Esempio non normativo di verifica della revoca:

.. literalinclude:: ../../../utils/certificate-revocation-verification.sh
   :language: bash


Migliori Pratiche per la Gestione dei Certificati X.509
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Integrazione della Validazione dei Certificati X.509
"""""""""""""""""""""""""""""""""""""""""""""""""""""

Ogni volta che il materiale certificativo in uso può essere cambiato, ripetere i controlli PKIX sull'intera catena, sui campi notBefore e notAfter e sulle prove di revoca quali CRL o OCSP. Applicare la stessa disciplina ai certificati di protocollo.

Diagnostica e Risoluzione dei Problemi
"""""""""""""""""""""""""""""""""""""""

I partecipanti DEVONO implementare procedure diagnostiche per individuare e risolvere i problemi legati ai certificati X.509. Il lavoro PKIX tipico include almeno le verifiche seguenti.

  - **Discrepanza dell'Authority Key Identifier.** L'Authority Key Identifier della CRL non corrisponde al Subject Key Identifier del Trust Anchor.
  - **Rotazione del certificato del Trust Anchor.** Un certificato del Trust Anchor obsoleto resta ancorato ai percorsi di validazione.
  - **Normalizzazione del numero seriale.** Il seriale è rappresentato in modo diverso tra certificato e voce della CRL.

Quando la validazione della CRL fallisce, i partecipanti DOVREBBERO accertarsi di fidarsi del certificato corrente del Trust Anchor, confrontare i valori di Authority Key Identifier tra CRL e Trust Anchor, validare la firma della CRL rispetto all'emittente atteso e scaricare un certificato aggiornato del Trust Anchor se è stata annunciata una rotazione.

I partecipanti DOVREBBERO inoltre eseguire test di connettività verso gli endpoint dell'infrastruttura dei certificati da cui dipendono i client PKIX.


Il seguente esempio non normativo fornisce uno script per il test di connettività PKI:

.. literalinclude:: ../../../utils/federation-connectivity-test.sh
   :language: bash


Coordinamento del Ciclo di Vita dei Certificati X.509
"""""""""""""""""""""""""""""""""""""""""""""""""""""

Il lavoro operativo DOVREBBE restare allineato al riepilogo delle classi PKIX in :ref:`annex/x5c-evaluation:Classi di certificati PKI IT-Wallet`. Gli strumenti PKIX DEVONO coprire le finestre di validità e le prove di revoca. Gli operatori DEVONO pubblicare le CRL ove il profilo PKIX lo richieda e DEVONO completare le revoche richieste dalla governance in caso di uscita di un'entità.


Aggiornamenti del materiale certificativo (PKIX)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Ogni volta che un partecipante riceve materiale X.509 nuovo, rinnovato o riemesso, anche dopo la rotazione di una chiave di emissione del superiore, il partecipante DEVE validare in PKIX la catena, i campi temporali e lo stato di revoca in conformità a questa sezione e a :ref:`trust-infrastructure:Revoca di Certificati X.509`. L'ottenimento del materiale è descritto in :ref:`trust-infrastructure:L'Infrastruttura di Trust` e in :ref:`entity-onboarding:Onboarding delle Entità`.

Dopo aver generato una nuova coppia di chiavi, il partecipante ottiene il certificato corrispondente tramite il percorso di registrazione in :ref:`entity-onboarding:Onboarding delle Entità`, lo valida in PKIX prima dell'uso e ritira il materiale PKIX sostituito secondo la policy locale.

.. note::
   Avviare una rotazione delle chiavi di un partecipante è sempre decisione del partecipante; l'autorità emittente risponde con nuovo materiale PKIX secondo le regole di trust.


Gestione del Ciclo di Vita dell'Entità
--------------------------------------

Le regole di ciclo di vita e i processi di alto livello sono in :ref:`onboarding-high-level:Gestione del Ciclo di Vita delle Entità`. Gli aggiornamenti amministrativi restano governati dal programma più ampio e questa sezione PKIX non li tratta.

Manutenzione operativa (PKIX)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  - **Rinnovo.** Generare una CSR, inoltrarla tramite il processo di registrazione in :ref:`entity-onboarding:Onboarding delle Entità`, installare i certificati emessi e validarli in PKIX prima dell'uso in produzione.
  - **Rotazione delle chiavi.** Seguire lo stesso percorso di registrazione per le chiavi sostitutive, validare in PKIX il nuovo materiale e ritirare i certificati obsoleti secondo policy e :ref:`trust-infrastructure:Revoca di Certificati X.509`.
  - **Metadati di servizio.** Quando cambiano endpoint o capacità in modo da toccare certificati o chiavi già in uso, gli operatori DEVONO eseguire un nuovo passaggio PKIX su tutto il materiale coinvolto.

Dopo cambiamenti tecnici sostanziali, validare in PKIX tutto il materiale X.509 impattato usando questa sezione insieme a :ref:`trust-infrastructure:Revoca di Certificati X.509`. Ulteriori verifiche di deployment restano nei capitoli del trust framework.

Procedure di uscita (PKIX)
^^^^^^^^^^^^^^^^^^^^^^^^^^

Il contesto di uscita è descritto in :ref:`onboarding-high-level:Processi di Uscita e Rimozione dalla Federazione`. La rimozione delle registrazioni nel trust layer è specificata in :ref:`trust-infrastructure:L'Infrastruttura di Trust`.

Uscita volontaria — PKIX ed emissione
"""""""""""""""""""""""""""""""""""""

  1. **Richiesta di revoca.** Inviare all'autorità emittente una richiesta firmata. La richiesta DEVE essere firmata con la chiave privata abbinata al certificato da revocare.
  2. **Verifica CRL.** Confermare che il numero seriale del certificato compaia nella CRL aggiornata pubblicata dall'emittente.
  3. **Pulizia nel trust layer.** Completare la deregistrazione presso l'autorità emittente secondo le regole del trust framework applicabili al ruolo.
  4. **Ritiro delle pubblicazioni.** Interrompere la pubblicazione del materiale di fiducia del partecipante quando la governance lo richiede.
  5. **Conferma operativa.** Quando il deployment espone canali di registro o di stato, gli operatori DOVREBBERO verificare che i consumatori a valle abbiano recepito l'esito della revoca. 

Esempio non normativo di richiesta di revoca del Certificato X.509 seguendo il formato :rfc:`3280`:

.. code-block:: text

   Richiesta di Revoca del Certificato X.509:
   Soggetto: CN=credentials.example.gov, OU=Digital Credentials, O=Example Organization, L=Roma, ST=Lazio, C=IT, emailAddress=technical@credentials.example.gov
   Numero Seriale del Certificato X.509: 987654321
   Motivo della Revoca: cessation_of_operation (5)
   Data di Revoca: 2025-12-31T23:59:59Z

   Richiesta firmata con la chiave privata corrispondente a:
   Algoritmo della Chiave Pubblica: id-ecPublicKey
   OID ASN1: prime256v1
   CURVA NIST: P-256
   ID Chiave: NsXymfIILEPR5Y0t

   Nota: La CRR DEVE essere firmata con la stessa chiave privata che corrisponde al
   certificato X.509 che viene revocato per autenticare la richiesta di revoca.

Esempio CRR in formato DER (codificato Base64):

.. code-block:: text

   -----BEGIN CERTIFICATE REVOCATION REQUEST-----
   MIIBVjCB/wIBADBpMQswCQYDVQQGEwJJVDEOMAwGA1UECAwFTGF6aW8xDTALBgNV
   BAcMBFJvbWExGjAYBgNVBAoMEUV4YW1wbGUgT3JnYW5pemF0aW9uMR8wHQYDVQQD
   DBZjcmVkZW50aWFscy5leGFtcGxlLmdvdjBZMBMGByqGSM49AgEGCCqGSM49AwEH
   A0IABIBgZ4HBgUCNXwY5LJSlKzm7gXY4FApFJCj91Gpb1K9GEIouTq2X3L0K64Iq
   0ob4l_gslT14644zbYXYF-xmw7aPdlbMuw3T1URwI4nafMtKrYwDQYJKoZIhvcNAQ
   kEAwIJrRLl1VR987654321gBgJKwYBBQUHAgEWHGh0dHBzOi8vZXhhbXBsZS5vcmcv
   cG9saWN5MAoGCCqGSM49BAMCA0gAMEUCIQC9h3Y6hFgd7zUzZyBrQ3jJ8HmVF2Qa
   -----END CERTIFICATE REVOCATION REQUEST-----

Rimozione da parte dell'organo di supervisione (PKIX)
"""""""""""""""""""""""""""""""""""""""""""""""""""

  1. **Revoca di emergenza**: l'autorità emittente revoca il certificato con motivazione appropriata.
  2. **Aggiornamento CRL**: il Trust Anchor pubblica una CRL aggiornata entro la finestra di emergenza.
  3. **Sospensione nel trust layer**: l'autorità emittente ritira le registrazioni di fiducia del partecipante secondo le regole del trust framework.
  4. **Effetto PKIX**: i relying party DEVONO considerare il certificato non attendibile dopo revoca e verifica CRL.

Esempio di controllo CRL di emergenza:

.. code-block:: bash

   curl -o emergency.crl https://trust-anchor.eid-wallet.example.it/pki/ta-sub.crl
   openssl crl -in emergency.crl -text -noout | grep "Last Update"

**Modifiche a livello di componente**

I componenti di servizio POSSONO cambiare mentre il partecipante resta registrato. Aggiornare i metadati di servizio come richiesto dal trust framework, validare in PKIX i certificati coinvolti, poi eseguire test operativi.

**Obblighi post-uscita**

1. **Pubblicazioni storiche**: mantenere gli endpoint storici richiesti per audit se la governance lo impone.
2. **Archivio X.509**: conservare le catene accessibili per le credenziali esistenti (minimo 7 anni).
3. **Log di audit**: archiviare i log secondo i requisiti normativi.

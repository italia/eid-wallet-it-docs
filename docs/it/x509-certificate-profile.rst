.. include:: ../common/common_definitions.rst
.. Included via infrastructure-trust.rst at title level '-' (level 1).

X.509 Certificate Profile
-------------------------

Questa sezione definisce un **X.509 Certificate Profile** generale, ulteriormente specializzato per i seguenti artifact:

- :ref:`infrastructure-trust:Entity Sign/Seal Certificate Profile` (Trust Framework EUDIW e Nazionale);
- :ref:`infrastructure-trust:Trust Anchor Certificate Profile` (Trust Framework EUDIW e Nazionale);
- :ref:`infrastructure-trust:Wallet-Relying Party Access Certificate (WRPAC) Profile` (Trust Framework EUDIW);
- :ref:`infrastructure-trust:Registrar Sign/Seal Certificate Profile` (Trust Framework EUDIW).

Questo profilo stabilisce i requisiti di sintassi, semantica e codifica per i certificati X.509 sulla base di :rfc:`5280` e ETSI EN 319 412.
Ciascun profilo di certificato X.509 definito da questa specifica DEVE conformarsi ai requisiti di questa sezione, salvo diversa indicazione esplicita.

.. list-table:: Campi del Certificato X.509
   :class: longtable
   :header-rows: 1
   :widths: 20 60 20

   * - **Campo**
     - **Descrizione**
     - **Riferimento**

   * - ``tbsCertificate``
     - OBBLIGATORIO.
     - Section 4.1.1.1

   * - ``signatureAlgorithm``
     - OBBLIGATORIO.
     - Section 4.1.1.2

   * - ``signatureValue``
     - OBBLIGATORIO.
     - Section 4.1.1.3

.. note::

    Il resto della sezione dettaglia il solo contenuto del campo ``tbsCertificate``. Per informazioni aggiuntive sui campi ``signatureAlgorithm`` e ``signatureValue``, fare riferimento a :rfc:`5280`.

Il campo ``tbsCertificate`` DEVE contenere una struttura ``TBSCertificate``, i cui campi DEVONO conformarsi a :rfc:`5280#section-4.1.2`.

La tabella seguente definisce i campi del certificato applicabili al profilo di certificato specificato in questo documento.
Per ciascun campo, la tabella definisce il requisito di presenza, il tipo, la descrizione e il corrispondente riferimento in :rfc:`5280`. I singoli profili di certificato POSSONO fornire note contestuali aggiuntive per tali campi, ma NON DEVONO modificare i requisiti di presenza ivi specificati.

.. list-table:: Campi TBSCertificate
   :class: longtable
   :header-rows: 1
   :widths: 20 60 20

   * - **Campo**
     - **Descrizione**
     - **Riferimento**

   * - ``version``
     - OBBLIGATORIO. DEVE essere la versione 3 (valore ``2``).
     - Section 4.1.2.1

   * - ``serialNumber``
     - OBBLIGATORIO.
     - Section 4.1.2.2

   * - ``signature``
     - OBBLIGATORIO. L'algoritmo referenziato DEVE essere tra quelli definiti in :ref:`algorithms:Cryptographic Algorithms`.
     - Section 4.1.2.3, Section 4.1.1.2

   * - ``issuer``
     - OBBLIGATORIO. DEVE conformarsi ai requisiti applicabili di [`ETSI EN 319 412-2`_] (Clausola 4.2.3.1 per le **persone giuridiche**, Clausola 4.2.3.2 per le **persone fisiche**), come specificato dal corrispondente profilo di certificato.
     - Section 4.1.2.4

   * - ``validity``
     - OBBLIGATORIO.
     - Section 4.1.2.5

   * - ``subject``
     - OBBLIGATORIO. DEVE conformarsi ai requisiti applicabili di [`ETSI EN 319 412-2`_] (Clausola 4.2.4) per le **persone fisiche** e di [`ETSI EN 319 412-3`_] (Clausola 4.2.1) per le **persone giuridiche**, come specificato dal corrispondente profilo di certificato.
     - Section 4.1.2.6

   * - ``subjectPublicKeyInfo``
     - OBBLIGATORIO. L'algoritmo referenziato DEVE essere tra quelli definiti in :ref:`algorithms:Cryptographic Algorithms`.
     - Section 4.1.2.7

   * - ``issuerUniqueID``
     - OPZIONALE. NON DOVREBBE essere presente.
     - Section 4.1.2.8

   * - ``subjectUniqueID``
     - OPZIONALE. NON DOVREBBE essere presente.
     - Section 4.1.2.8

   * - ``extensions``
     - OBBLIGATORIO. DEVE conformarsi alla struttura definita in :rfc:`5280#section-4.2`.
       Le estensioni applicabili e i relativi vincoli specifici del profilo sono definiti di seguito e nel corrispondente profilo di certificato.
     - Section 4.1.2.9

La tabella seguente specifica le estensioni dei certificati X.509 supportate da questa specifica, inclusi i relativi Object Identifier (OID), il tipo, la criticità, la descrizione e i riferimenti normativi. I singoli profili di certificato DEVONO definire il requisito di presenza (OBBLIGATORIO, OPZIONALE o VIETATO) per ciascuna estensione e POSSONO ulteriormente vincolarne la sintassi e i contenuti.

I valori di criticità utilizzati in questa specifica hanno il seguente significato:

- **C**: l'estensione DEVE essere marcata come critica;
- **NC**: l'estensione DEVE essere marcata come non critica.

.. list-table:: Estensioni di Certificato Supportate
   :class: longtable
   :header-rows: 1
   :widths: 25 20 15 40

   * - **Estensione**
     - **OID**
     - **Criticità**
     - **Riferimento**

   * - ``authorityKeyIdentifier``
     - ``2.5.29.35``
     - NC
     - :rfc:`5280#section-4.2.1.1`, Clausola 4.3.1 di [`ETSI EN 319 412-2`_]

   * - ``subjectKeyIdentifier``
     - ``2.5.29.14``
     - NC
     - :rfc:`5280#section-4.2.1.2`

   * - ``keyUsage``
     - ``2.5.29.15``
     - C
     - :rfc:`5280#section-4.2.1.3`, Clausola 4.3.2 di [`ETSI EN 319 412-2`_], Clausola 4.3.1 di [`ETSI EN 319 412-3`_]

   * - ``certificatePolicies``
     - ``2.5.29.32``
     - NC
     - :rfc:`5280#section-4.2.1.4`, Clausola 4.3.3 di [`ETSI EN 319 412-2`_]

   * - ``subjectAltName``
     - ``2.5.29.17``
     - NC
     - :rfc:`5280#section-4.2.1.6`, Clausola 4.3.5 di [`ETSI EN 319 412-2`_], Clausola 6.6.1, GEN-6.6.1-07 di [`ETSI TS 119 411-8`_]

   * - ``issuerAltName``
     - ``2.5.29.18``
     - NC
     - :rfc:`5280#section-4.2.1.7`

   * - ``basicConstraints``
     - ``2.5.29.19``
     - C
     - :rfc:`5280#section-4.2.1.9`

   * - ``cRLDistributionPoints``
     - ``2.5.29.31``
     - NC
     - :rfc:`5280#section-4.2.1.13`, Clausola 4.3.11 di [`ETSI EN 319 412-2`_]

   * - ``authorityInfoAccess``
     - ``1.3.6.1.5.5.7.1.1``
     - NC
     - :rfc:`5280#section-4.2.2.1`, Clausola 4.4.1 di [`ETSI EN 319 412-2`_]

   * - ``ext-etsi-valassured-ST-certs``
     - ``0.4.0.194121.2.1``
     - NC
     - Clausola 5.2.2 di [`ETSI EN 319 412-1`_]

   * - ``noRevAvail``
     - ``2.5.29.56``
     - NC
     - :rfc:`9608#section-2`

   * - ``qcStatements``
     - ``1.3.6.1.5.5.7.1.3``
     - NC
     - :rfc:`3739#section-3.2.6`, Clausola 4.2 di [`ETSI EN 319 412-5`_]

.. warning::
  **Prevenzione delle Dipendenze Circolari negli URI**

  Per prevenire dipendenze circolari di validazione durante gli handshake TLS, gli URI definiti nelle estensioni ``cRLDistributionPoints`` e ``authorityInfoAccess`` DEVONO utilizzare lo schema ``http://`` invece di ``https://``, come suggerito da :rfc:`5280#section-8`.

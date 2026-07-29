.. include:: ../common/common_definitions.rst
.. Included via infrastructure-trust.rst at title level '-' (level 1).

X.509 Certificate Profile
-------------------------

Questa sezione definisce un generale **X.509 Certificate Profile**, ulteriormente specializzato per i seguenti artifact:

- :ref:`infrastructure-trust:Entity Sign/Seal Certificate Profile` (EUDIW e National Trust Framework);
- :ref:`infrastructure-trust:Trust Anchor Certificate Profile` (EUDIW e National Trust Framework);
- :ref:`infrastructure-trust:Wallet-Relying Party Access Certificate (WRPAC) Profile` (EUDIW Trust Framework);
- :ref:`infrastructure-trust:Registrar Sign/Seal Certificate Profile` (EUDIW Trust Framework).

Il profilo comune stabilisce i requisiti di sintassi, semantica e codifica per i certificati X.509 basati su :rfc:`5280` e ETSI EN 319 412.
Ciascun X.509 certificate profile definito da questa specifica DEVE conformarsi ai requisiti di questa sezione, salvo diversa indicazione esplicita.

Il certificato finale si ottiene combinando il certificate body (da ``version`` a ``subjectPublicKeyInfo``) con le certificate extensions richieste dal certificate profile selezionato.
La struttura ASN.1 risultante DEVE essere codificata utilizzando le Distinguished Encoding Rules (DER) come specificato in :rfc:`5280`.

Common Certificate Fields
^^^^^^^^^^^^^^^^^^^^^^^^^

La struttura ``TBSCertificate`` e i relativi campi DEVONO conformarsi a :rfc:`5280#section-4.1`.

La tabella seguente definisce i campi del certificato applicabili ai certificate profile definiti in questa specifica.
Per ciascun campo, la tabella specifica il riferimento :rfc:`5280` corrispondente, il requisito di presenza e gli eventuali vincoli aggiuntivi specifici del profilo.

.. list-table:: Certificate Profile Fields
   :class: longtable
   :header-rows: 1
   :widths: 20 60 20

   * - **Field**
     - **Description**
     - **Reference**

   * - ``version``
     - REQUIRED. DEVE essere la versione 3 (valore ``2``).
     - Section 4.1.2.1

   * - ``serialNumber``
     - REQUIRED.
     - Section 4.1.2.2

   * - ``signature``
     - REQUIRED. L'algoritmo referenziato DEVE essere tra quelli definiti in :ref:`algorithms:Algoritmi Crittografici`.
     - Section 4.1.2.3, Section 4.1.1.2

   * - ``issuer``
     - REQUIRED. DEVE conformarsi ai requisiti applicabili di [`ETSI EN 319 412-2`_] (Clause 4.2.3.1 per **legal persons**, Clause 4.2.3.2 per **natural persons**), come specificato dal corrispondente certificate profile.
     - Section 4.1.2.4

   * - ``validity``
     - REQUIRED.
     - Section 4.1.2.5

   * - ``subject``
     - REQUIRED. DEVE conformarsi ai requisiti applicabili di [`ETSI EN 319 412-2`_] (Clause 4.2.4) per **natural persons** e [`ETSI EN 319 412-3`_] (Clause 4.2.1) per **legal persons**, come specificato dal corrispondente certificate profile.
     - Section 4.1.2.6

   * - ``subjectPublicKeyInfo``
     - REQUIRED. L'algoritmo referenziato DEVE essere tra quelli definiti in :ref:`algorithms:Algoritmi Crittografici`.
     - Section 4.1.2.7

   * - ``issuerUniqueID``
     - OPTIONAL. NON DOVREBBE essere presente.
     - Section 4.1.2.8

   * - ``subjectUniqueID``
     - OPTIONAL. NON DOVREBBE essere presente.
     - Section 4.1.2.8

   * - ``extensions``
     - REQUIRED. DEVE conformarsi alla struttura definita in :rfc:`5280#section-4.2`.
       Le extensions applicabili e i relativi vincoli specifici del profilo sono definiti in :ref:`infrastructure-trust:Supported Certificate Extensions` e nel corrispondente certificate profile.
     - Section 4.1.2.9

Supported Certificate Extensions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

La tabella seguente elenca le certificate extensions supportate dai X.509 certificate profile definiti in questa specifica, insieme ai relativi object identifier, criticality predefinita e riferimenti normativi.
I certificate profile specifici definiscono se un'extension è REQUIRED, OPTIONAL o NON DEVE essere presente, e POSSONO ulteriormente vincolarne i contenuti.

I valori di criticality utilizzati in questa specifica hanno il seguente significato:

- **C**: l'extension DEVE essere marcata come critical;
- **NC**: l'extension DEVE essere marcata come non-critical.

.. list-table:: Supported Certificate Extensions
   :class: longtable
   :header-rows: 1
   :widths: 25 20 15 40

   * - **Extension**
     - **OID**
     - **Criticality**
     - **Reference**

   * - ``authorityKeyIdentifier``
     - ``2.5.29.35``
     - NC
     - :rfc:`5280#section-4.2.1.1`, Clause 4.3.1 of [`ETSI EN 319 412-2`_]

   * - ``subjectKeyIdentifier``
     - ``2.5.29.14``
     - NC
     - :rfc:`5280#section-4.2.1.2`

   * - ``keyUsage``
     - ``2.5.29.15``
     - C
     - :rfc:`5280#section-4.2.1.3`, Clause 4.3.2 of [`ETSI EN 319 412-2`_], Clause 4.3.1 of [`ETSI EN 319 412-3`_]

   * - ``certificatePolicies``
     - ``2.5.29.32``
     - NC
     - :rfc:`5280#section-4.2.1.4`, Clause 4.3.3 of [`ETSI EN 319 412-2`_]

   * - ``subjectAltName``
     - ``2.5.29.17``
     - NC
     - :rfc:`5280#section-4.2.1.6`, Clause 4.3.5 of [`ETSI EN 319 412-2`_], Clause 6.6.1, GEN-6.6.1-07 of [`ETSI TS 119 411-8`]

   * - ``basicConstraints``
     - ``2.5.29.19``
     - C
     - :rfc:`5280#section-4.2.1.9`

   * - ``cRLDistributionPoints``
     - ``2.5.29.31``
     - NC
     - :rfc:`5280#section-4.2.1.13`, Clause 4.3.11 of [`ETSI EN 319 412-2`_]

   * - ``authorityInfoAccess``
     - ``1.3.6.1.5.5.7.1.1``
     - NC
     - :rfc:`5280#section-4.2.2.1`, Clause 4.4.1 of [`ETSI EN 319 412-2`_]

   * - ``ext-etsi-valassured-ST-certs``
     - ``0.4.0.194121.2.1``
     - NC
     - Clause 5.2.2 of [`ETSI EN 319 412-1`_]

   * - ``noRevAvail``
     - ``2.5.29.56``
     - NC
     - :rfc:`9608#section-2`

   * - ``qcStatements``
     - ``1.3.6.1.5.5.7.1.3``
     - NC
     - :rfc:`3739#section-3.2.6`, Clause 4.2 of [`ETSI EN 319 412-5`_]

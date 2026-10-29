.. include:: ../common/common_definitions.rst


e-Service PDND
==============

Il framework `EIDAS-ARF`_ consente agli Stati Membri di stabilire le interfacce, i termini e le condizioni che regolano la comunicazione tra i Fornitori di Credenziali e le Fonti Autentiche. Nel contesto italiano, l'interoperabilità è stabilita sfruttando le seguenti linee guida.

    - "Linee Guida sull'interoperabilità tecnica delle Pubbliche Amministrazioni" (`MODI`_).
    - "Linee Guida sull'infrastruttura tecnologica della Piattaforma Digitale Nazionale Dati per l'interoperabilità dei sistemi informativi e delle basi di dati" (`PDND`_).

Per utilizzare la PDND, le entità DEVONO aderire formalmente, diventando **Aderenti**. All'interno dell'infrastruttura PDND, gli Aderenti DEVONO assumere almeno uno dei seguenti ruoli:

    - **Erogatori**: espongono e-Service ad altri Aderenti.
    - **Fruitori**: utilizzano e-Service offerti dagli Erogatori all'interno dell'Infrastruttura PDND.

L'accesso ad un e-Service richiede ai Fruitori di ottenere uno specifico Access Token, noto all'interno dell'infrastruttura PDND come Voucher.

Requisiti e Pattern di Sicurezza
--------------------------------

Questa specifica si basa sul seguente insieme di requisiti:

.. list-table::
  :class: longtable
  :widths: 10 70 20
  :header-rows: 1

  * - **ID**
    - **Descrizione**
    - **Tipo**
  * - R1
    - Il Fruitore e l'Erogatore hanno entrambi aderito all'infrastruttura PDND.
    - Architetturale
  * - R2
    - La comunicazione tra il Fruitore e l'Erogatore DEVE garantire l'integrità dei dati, l'autenticità, la non ripudiabilità e la protezione contro attacchi di replay.
    - Sicurezza
  * - R3
    - L'Erogatore PUÒ richiedere al Fruitore di includere dati tracciati nella richiesta. In tal caso, DEVE esserci una correlazione tra i dati tracciati e il Voucher.
    - Sicurezza
  * - R4
    - Gli e-Service DEVONO essere implementati in REST, quindi il protocollo SOAP NON DEVE essere utilizzato.
    - Tecnico
  * - R5
    - L'Erogatore DEVE garantire, con un alto grado di certezza, la prova di possesso del Voucher da parte del Fruitore.
    - Sicurezza

`PDND`_ e `MODI`_ definiscono diversi pattern di sicurezza progettati per migliorare specifiche proprietà di sicurezza nelle interazioni tra gli Aderenti. Questa specifica adotta i seguenti pattern di sicurezza:

.. list-table::
  :class: longtable
  :widths: 80 20
  :header-rows: 1

  * - **Pattern di Sicurezza**
    - **Conforme a**
  * - **[REST_JWS_2021_POP]** Profilo di emissione dei Voucher JWS POP (*Allegato 3 - Standard e dettagli tecnici utilizzati per la fruizione dei Voucher di autorizzazione* [`PDND`_]): OBBLIGATORIO. Aggiunge una prova di possesso sul Voucher. Il Fruitore che utilizza il Voucher per accedere a un e-Service DEVE dimostrare la prova di possesso della chiave privata la cui chiave pubblica è attestata nel Voucher.
    - R2, R4, R5
  * - **[ID_AUTH_CHANNEL_01]** Direct Trust Transport-Level Security (*Allegato 2 - Pattern di sicurezza* [`MODI`_]): OBBLIGATORIO. Protegge la comunicazione tra il Fruitore e l'Erogatore garantendo riservatezza, integrità, identificazione dell'Erogatore e mitigazione contro attacchi di replay e spoofing.
    - R1, R2
  * - **[INTEGRITY_REST_02]** Integrità del payload delle richieste REST in PDND (*Allegato 2 - Pattern di sicurezza* [`MODI`_]): Garantisce l'integrità del payload della richiesta REST del Fruitore e della risposta REST dell'Erogatore, all'interno dell'Infrastruttura PDND. È OBBLIGATORIO ogni volta che la richiesta/risposta contiene un payload.
    - R2, R4
  * - **[AUDIT_REST_02]** Inoltro dati tracciati nel dominio del Fruitore REST con correlazione (*Allegato 2 - Pattern di sicurezza* [`MODI`_]): OPZIONALE. L'Erogatore PUÒ richiedere dati aggiuntivi tracciati nel dominio del Fruitore, con una correlazione tra tali dati e il metodo di autenticazione. In tal caso, questo pattern DEVE essere utilizzato.
    - R3, R4
  * - **[ID_AUTH_REST_01]** Direct Trust su PDND tramite token JWT emessi dalla piattaforma (*Allegato 2 - Pattern di sicurezza* [`MODI`_]).
    - R1, R2, R4, R5

.. note::
    In queste specifiche, il pattern di sicurezza ``REST_JWS_2021_POP`` è implementato in conformità a :rfc:`9449`.

    In alternativa, la prova di possesso PUÒ essere attestata dal JWT ``TrackingEvidence`` (come dettagliato di seguito). Tuttavia, mentre il ``TrackingEvidence`` è definito in ``AUDIT_REST_02`` per fornire dati tracciati aggiuntivi, in questo contesto funge da prova di possesso del Voucher. Tali scelte di implementazione saranno indicate rispettivamente come ``POP_DPoP`` e ``POP_TPoP``.

I seguenti pattern di sicurezza definiti in `PDND`_ e `MODI`_ NON DEVONO essere utilizzati. Tali pattern non sono conformi ai requisiti definiti in precedenza.

    - I seguenti pattern possono essere utilizzati solo quando il Fruitore non può iscriversi all'Infrastruttura PDND (ossia quando la trust tra gli Aderenti deve essere stabilita in forma diretta). Tali pattern non risultano conformi a **R1**.

      - **[ID_AUTH_CHANNEL_02]** Direct Trust mutual Transport-Level Security (*Allegato 2 - Pattern di Sicurezza* [`MODI`_]).
      - **[ID_AUTH_REST_02]** Direct Trust su PDND tramite token JWT emessi dalla piattaforma con caratteristiche di unicità del token/messaggio (*Allegato 2 - Pattern di sicurezza* [`MODI`_]).
      - **[INTEGRITY_REST_01]** Integrità del payload messaggio REST (*Allegato 2 - Pattern di sicurezza* [`MODI`_]).

    - Il seguente pattern non fornisce correlazione tra i dati tracciati e il Voucher. Tale pattern non risulta conforme a **R3**.

      - **[AUDIT_REST_01]** Inoltro dati tracciati nel dominio del Fruitore REST (*Allegato 2 - Pattern di sicurezza* [`MODI`_]).

    - I seguenti pattern sono basati su un'architettura SOAP. Tali pattern non risultano conformi a **R4**.

      - **[ID_AUTH_SOAP_01]** Direct Trust con certificato X.509 su SOAP (*Allegato 2 - Pattern di sicurezza* [`MODI`_]).
      - **[ID_AUTH_SOAP_02]** Direct Trust con certificato X.509 su SOAP con unicità del token/messaggio (*Allegato 2 - Pattern di sicurezza* [`MODI`_]).
      - **[INTEGRITY_SOAP_01]** Integrità del payload del messaggio SOAP (*Allegato 2 - Pattern di sicurezza* [`MODI`_]).

    - Il seguente pattern non garantisce la prova di possesso del Voucher. Tale pattern non risulta conforme a **R5**.

      - **[REST_JWS_2021_Bearer]** Profilo di emissione dei Voucher JWS Bearer (*Allegato 3 - Standard e dettagli tecnici utilizzati per la fruizione dei Voucher di autorizzazione* [`PDND`_]).

.. note::
  Nel caso di implementazione ``POP_TPoP``, il Voucher viene emesso come token Bearer. Tuttavia, poiché è accompagnato da una prova di possesso, è comunque conforme al pattern di sicurezza ``REST_JWS_2021_POP`` invece che ``REST_JWS_2021_Bearer``.

Emissione del Voucher PDND
--------------------------

L'Infrastruttura PDND definisce due diversi tipi di Voucher:

  - **Per e-Service**: consentono ai Fruitori di richiedere dati da un e-Service.
  - **Per API di Interoperabilità**: consentono agli Aderenti di richiedere dati dall'API di Interoperabilità, esposta dall'Infrastruttura PDND.

I due flussi sono descritti di seguito.

Voucher PDND per e-Service
^^^^^^^^^^^^^^^^^^^^^^^^^^

Prerequisiti per il Voucher PDND per e-Service
""""""""""""""""""""""""""""""""""""""""""""""

Il **Fruitore** DEVE rispettare i seguenti prerequisiti:

    - Ha completato con successo l'adesione all'Infrastruttura PDND (come da R1).
    - Ha creato un nuovo `Client e-service` per interagire con l'e-Service desiderato. Al momento della creazione, gli è stato assegnato un ``client_id`` dalla Piattaforma PDND.
    - Ha registrato una coppia di chiavi associata al `Client e-service`.
    - Ha richiesto di iscriversi all'e-Service desiderato.
    - Ha definito un nuovo scopo per l'e-Service. Al momento della definizione, gli è stato assegnato un ``purposeId`` dalla Piattaforma PDND.
    - Ha associato il `Client e-service` allo scopo definito.

L'**Erogatore** DEVE rispettare i seguenti prerequisiti:

    - Ha completato con successo l'adesione all'Infrastruttura PDND (come da R1).
    - Ha creato un nuovo e-Service e lo ha pubblicato all'interno del Catalogo API PDND.
    - Ha approvato la richiesta del Fruitore di iscriversi all'e-Service.


Flusso del Voucher PDND per e-Service
"""""""""""""""""""""""""""""""""""""

.. _fig_VoucherIssuance_eService_Flow:
.. plantuml:: plantuml/pdnd-voucher-issuance.puml
    :width: 80%
    :alt: La figura illustra l'emissione del Voucher per e-Service - Flusso dettagliato.
    :caption: `Emissione del Voucher per e-Service - Flusso dettagliato. <https://www.plantuml.com/plantuml/svg/VP71RjH0343lynLMUcaZLaALuD03QfHjrKK8ecQ1O-HEtCqeoJXuF4ktNqycj5s42fSeTkpdP-SoA8h6SO1l76r70fiG8dfBi09QrIHxPycequ7-Ns8mAliutf4OSySFaESb-n17aZo7aysUvM009XHrrate5R8y_r94xQ0S77dDymmmG7bjoBSm8vuvrVhpEZ6AnoZqBqPwiBX7LCSUaXN94x6eZqIU5AvPeFYwtcoRswjwsxmzDp1FNNqehoygePbEyF7x5dww6Mjvd0OQoIlA0LfKXDCismhQtldTrTwrv2rbsPavGigv9of1VLESltiF7OOE-1vUQqkmczE_ysU9DoiRyqmKGYLOLrn1JmUOq0cWRs4IvlkbggWlNdxGBVs853J1xNBQnhLPzWPUGWo191tgzMoZXub-Vze9UbtYPKVnh0Iy9u6YXfDFRjTfvNoVbk_8zY5fBqN65FLgaJzQXObzeAI5rb88ZN9FJmxfzS_1z30veT0udmPVpjWu3hy0>`_


.. .. figure:: ../../images/Low-Level-Flow-AuthenticSource-Voucher-Issuance-eService.svg
..     :figwidth: 100%
..     :align: center
..     :target: https://www.plantuml.com/plantuml/svg/TT5HRzCm40VmTt-AK_QoHLH2a-1X3sXHkcf52AAbm6FakRV6Ik8pvtDPz-cnGxSYjBr4iMF_xd-Nwo2Q9KwZ4YiZmW-AfaU6TGXHEuEm05oqo7jhK2aTXLoSxf6LkgT7ACkQN8WJSbd2sNfFV500FedMMA-TG56MtweeFTIZHITbMO0EKAyKkYqaujbfbb-NsQYU8kDRHduGsoSjbXpaLCX7iMfF8dc15J5KtvVhJNTtqswwzvSAKjN5ftfrrJ0c7U7ppmtyjearDFaH9tIY-G1RBHhEYsB3sWpMxMxsTelEO55Sg1DIfpjH4DhRwlB3H-Xrw84UuBLh6Riz_t__8davibBF8gDEuBAX1WOyWDUMGQUUF1CzpAUgzkhb1ztXhuX1CcxcqNPsMnJlu6MfGq3EWtfzjvE3nx-VTgoT7DUfHtOa2BH7Xgg5iozsrqjZtP2Rxz4C8SUU3obLjOiv_2bLyEG2vbZQ60oX4nhmc26__biO7xrb39rrkV1rOkCq_W40

..     Emissione del Voucher per e-Service - Flusso dettagliato

**Passi 1-2 (Preparazione dei dati tracciati):** Il Fruitore prepara un JWT (``TrackingEvidence``) contenente i dati tracciati che devono essere inviati all'Erogatore. Infine, calcola l'hash SHA-256 di ``TrackingEvidence``.

.. literalinclude:: ../../examples/shared/e-service-pdnd-1.json
   :language: json
   :caption: Esempio non normativo dell'header di ``TrackingEvidence``
   :name: code_VoucherIssuance_eService_Flow_TrackingEvidence_Header


.. literalinclude:: ../../examples/shared/e-service-pdnd-2.json
   :language: json
   :caption: Esempio non normativo del payload di ``TrackingEvidence``
   :name: code_VoucherIssuance_eService_Flow_TrackingEvidence_Payload

.. note::
  I passi 1-2 sono richiesti solo quando si rispetta il pattern di sicurezza ``AUDIT_REST_02`` o l'implementazione ``POP_TPoP``.

**Passo 3 (Generazione coppia di chiavi e `DPoP proof`)**: Il Fruitore DEVE creare una nuova coppia di chiavi e un nuovo JWT di `DPoP proof` come specificato nella Sezione 4 di :rfc:`9449`. Il Fruitore usa tale prova per la richiesta di token all'Authorization Server PDND.

.. note::
  Il passo 3 è richiesto solo quando si segue l'implementazione ``POP_DPoP``.

**Passo 4 (Richiesta di Voucher)**: Il Fruitore crea una `Voucher Request` e la invia all'Authorization Server PDND.

.. literalinclude:: ../../examples/shared/e-service-pdnd-3.http
   :language: http
   :caption: Esempio non normativo della `Voucher Request`
   :name: code_VoucherIssuance_eService_Flow_Request


.. literalinclude:: ../../examples/shared/e-service-pdnd-4.json
   :language: json
   :caption: Esempio non normativo del JOSE header di ``client_assertion``
   :name: code_VoucherIssuance_eService_Flow_ClientAssertion_Header


.. literalinclude:: ../../examples/shared/e-service-pdnd-5.json
   :language: json
   :caption: Esempio non normativo del payload di ``client_assertion``
   :name: code_VoucherIssuance_eService_Flow_ClientAssertion_Payload

.. note::
  Il claim ``purposeId`` nel payload di ``client_assertion`` è richiesto solo quando si richiede un Voucher per e-Service.

.. note::
  Il claim ``digest`` nel payload di ``client_assertion`` è richiesto solo quando si rispetta il pattern di sicurezza ``AUDIT_REST_02`` o l'implementazione ``POP_TPoP``.

Alla ricezione della `Voucher Request`, l'Authorization Server PDND DEVE eseguire i seguenti controlli sui parametri del relativo body:

    - Il claim ``client_assertion_type`` è impostato su ``urn:ietf:params:oauth:client-assertion-type:jwt-bearer``.
    - Il claim ``grant_type`` è impostato su ``client_credentials``.

L'Authorization Server PDND DEVE anche validare il JWT ``client_assertion`` come segue:

    Header:

      - Assicurarsi che il claim ``typ`` sia presente e che il suo valore sia ``JWT``.

    Firma:

      - Ottenere la chiave pubblica del Fruitore corrispondente al parametro header ``kid``, interagendo con l'API di Interoperabilità PDND.
      - Validare la firma del JWT utilizzando la chiave pubblica del Fruitore recuperata e l'algoritmo specificato dal parametro header ``alg``.

    Payload:

      - I claim ``iss`` e ``sub`` DEVONO identificare un Client registrato nell'Infrastruttura PDND.
      - Il claim ``aud`` DEVE rappresentare l'Authorization Server PDND.
      - Il claim ``exp`` DEVE rappresentare un istante temporale successivo all'ora corrente.
      - Se il claim ``nbf`` è presente, DEVE rappresentare un istante temporale precedente all'ora corrente.
      - Il claim ``iat`` DEVE rappresentare un istante temporale precedente all'ora corrente.
      - Il claim ``jti`` NON DEVE essere stato utilizzato in precedenza.
      - Il claim ``purposeId`` DEVE identificare uno scopo registrato nell'Infrastruttura PDND e associato al Client.

.. note::
  L'Authorization Server PDND non deve eseguire alcun controllo sul claim ``digest``.

.. note::
  La verifica dei claim ``exp``, ``nbf``, ``iat`` e ``jti``, come dettagliato sopra, DEVE essere eseguita per tutti i JWT descritti in questa sezione. Questi controlli non saranno esplicitamente menzionati nei riferimenti successivi.

**Passo 6 (Emissione del Voucher)**: Qualora i controlli abbiano successo, l'Authorization Server PDND emette un Voucher, che è incluso nella `Voucher Response` inviata al Fruitore.

.. literalinclude:: ../../examples/shared/e-service-pdnd-6.http
   :language: http
   :caption: Esempio non normativo della `Voucher Response`
   :name: code_VoucherIssuance_eService_Flow_Response

.. literalinclude:: ../../examples/shared/e-service-pdnd-7.json
   :language: json
   :caption: Esempio non normativo del JOSE header di ``access_token``
   :name: code_VoucherIssuance_eService_Flow_AccessToken_Header

.. literalinclude:: ../../examples/shared/e-service-pdnd-8.json
   :language: json
   :caption: Esempio non normativo del payload di ``access_token``
   :name: code_VoucherIssuance_eService_Flow_AccessToken_Payload

.. note::
  Il claim ``digest`` nel payload di ``access_token`` è richiesto solo quando si rispetta il pattern di sicurezza ``AUDIT_REST_02`` o l'implementazione ``POP_TPoP``. Se presente, corrisponde al valore del claim ``digest`` contenuto in ``client_assertion``.

Voucher PDND per API di Interoperabilità
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Prerequisiti per il Voucher PDND per API di Interoperabilità
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

L'**Aderente** DEVE rispettare i seguenti prerequisiti:

  - Ha completato con successo l'adesione all'Infrastruttura PDND.
  - Ha creato un nuovo `Client interop api` per interagire con l'API di Interoperabilità. Al momento della creazione, gli è stato assegnato un ``client_id`` dalla Piattaforma PDND.
  - Ha registrato una coppia di chiavi associata al `Client interop api`.

Flusso del Voucher per API di Interoperabilità
""""""""""""""""""""""""""""""""""""""""""""""

.. _fig_VoucherIssuance_InteroperabilityAPI_Flow:
.. plantuml:: plantuml/pdnd-voucher-issuance-interoperability.puml
    :width: 80%
    :alt: La figura illustra l'emissione del Voucher per API di Interoperabilità - Flusso dettagliato.
    :caption: `Emissione del Voucher per API di Interoperabilità - Flusso dettagliato. <https://www.plantuml.com/plantuml/svg/ZP11ozf048Rl-ok6UD7GqFOg4WmH8L3Qq41FXR0cWrbCTjEPsQ3--heQr4CBtoLavXsUzs6tB9h43ptyShxfaA1Wzjes20aKLf3SYAGFfZToWQmib1ZfySFNIdjnrWy79AKExWnH79UQn3Hcr5RY-BVTiBdY-kkNT9axotv00aURps6RlgKbkScqIAivYc1HJ8uk2c1y0GF_H-QbWxmt60eYq0pvNg5juIRmiBX9xBxluXWMsTKJ_eyHFexCLOjn5Yga2MacPjMBcE-JDAlMpqVvYNyyii0oYfgxHMtQAFe4pr4p8mNclxUrN4PyH4VILkPvfHHP9mXkGhe9mEARENPI6djI07c7pOc3rFr8gQnAaZJVhrzMF3hB6BHqqo1pBUw4iqFuVI_6ysW8kJOs56_Hjdxe_m80>`_


.. .. figure:: ../../images/Low-Level-Flow-AuthenticSource-Voucher-Issuance-InteroperabilityAPI.svg
..   :figwidth: 100%
..   :align: center
..   :target: https://www.plantuml.com/plantuml/svg/TP51ozf048Rl-ok6UD7GqFOg4WmH8L3Qq41FXR36mIp6tNHcLjHVtrqDwk7xBY4px_Ay3xjh5atYJuCI8mF27-Ux7WagPgzjXv11PGN9ZKXwPmOZLoZgIYdjnLb_sY4fjNCNIDAq3YJJcL5RITE_TiNcXillt_9vwIpxKw0wMdsDs_mjhScTpHvfCKK9pAgpewi265_0oFzLUEcX70p6WWGqGxbLQFSG11uMGMBpSvEcC2jkdl0pHlmuCZSjnbbeaCv84x5eNiHoc-L5itnUoc_yvv45vadItIrQiq-IB_0SDJDIP7wyRUKwuYCwK12QveLIP9qWkA0H163smnnwgOqzAe2on-x8KUf-IAcYoRAyt2vVLZmwonYrTDSXSolkY9D3_7qlnije2BarDXQl0pOy_dy0

..   Emissione del Voucher per API di Interoperabilità - Flusso dettagliato

**Passo 1 (Richiesta di Voucher)**: L'Aderente crea una `Voucher Request` e la invia all'Authorization Server PDND.

.. literalinclude:: ../../examples/shared/e-service-pdnd-9.http
   :language: http
   :caption: Esempio non normativo della `Voucher Request`
   :name: code_VoucherIssuance_InteroperabilityAPI_Flow_Request

.. literalinclude:: ../../examples/shared/e-service-pdnd-10.json
   :language: json
   :caption: Esempio non normativo del JOSE header di ``client_assertion``
   :name: code_VoucherIssuance_InteroperabilityAPI_Flow_ClientAssertion_Header

.. literalinclude:: ../../examples/shared/e-service-pdnd-11.json
   :language: json
   :caption: Esempio non normativo del payload di ``client_assertion``
   :name: code_VoucherIssuance_InteroperabilityAPI_Flow_ClientAssertion_Payload

Alla ricezione della `Voucher Request`, l'Authorization Server PDND DEVE eseguire i seguenti controlli sui parametri del relativo body:

  - Il claim ``client_assertion_type`` è impostato su ``urn:ietf:params:oauth:client-assertion-type:jwt-bearer``.
  - Il claim ``grant_type`` è impostato su ``client_credentials``.

L'Authorization Server PDND DEVE anche validare il JWT ``client_assertion`` come segue:

  Header:

  - Assicurarsi che il claim ``typ`` sia presente e che il suo valore sia ``JWT``.

  Firma:

  - Ottenere la chiave pubblica dell'Aderente corrispondente al parametro header ``kid``, interagendo con l'API di Interoperabilità PDND.
  - Validare la firma del JWT utilizzando la chiave pubblica dell'Aderente recuperata e l'algoritmo specificato dal parametro header ``alg``.

  Payload:

  - I claim ``iss`` e ``sub`` DEVONO identificare un Client registrato nell'Infrastruttura PDND.
  - Il claim ``aud`` DEVE rappresentare l'Authorization Server PDND.


**Passo 2 (Emissione del Voucher)**: Qualora i controlli abbiano successo, l'Authorization Server PDND emette un Voucher, che è incluso nella `Voucher Response` inviata all'Aderente.

.. literalinclude:: ../../examples/shared/e-service-pdnd-12.http
   :language: http
   :caption: Esempio non normativo della `Voucher Response`
   :name: code_VoucherIssuance_InteroperabilityAPI_Flow_Response

.. literalinclude:: ../../examples/shared/e-service-pdnd-13.json
   :language: json
   :caption: Esempio non normativo del JOSE header di ``access_token``
   :name: code_VoucherIssuance_InteroperabilityAPI_Flow_AccessToken_Header

.. literalinclude:: ../../examples/shared/e-service-pdnd-14.json
   :language: json
   :caption: Esempio non normativo del payload di ``access_token``
   :name: code_VoucherIssuance_InteroperabilityAPI_Flow_AccessToken_Payload


Endpoint Authorization Server PDND
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

L'Endpoint Authorization Server PDND emette Voucher agli Aderenti. Questi Voucher consentono ai Fruitori di accedere alle risorse degli e-Service e agli Erogatori di interagire con l'API di Interoperabilità.

Richiesta (Voucher PDND)
""""""""""""""""""""""""

La richiesta all'Endpoint Authorization Server PDND aderisce al flusso Client Credentials Grant specificato in :rfc:`6749`. Il client si autentica presentando un'asserzione client basata su JWT come definito in :rfc:`7521` e :rfc:`7523`.

Seguendo le suddette specifiche, la richiesta DEVE essere una richiesta HTTP POST con un corpo codificato in formato ``application/x-www-form-urlencoded``.

La `Voucher Request` DEVE includere i seguenti parametri nell'header HTTP (se non diversamente specificato):

.. list-table::
  :widths: 20 60 20
  :header-rows: 1

  * - **Parametro**
    - **Descrizione**
    - **Riferimento**
  * - **DPoP**
    - JWT di `DPoP proof`, per rispettare il pattern di sicurezza ``REST_JWS_2021_POP``. È obbligatorio solo se il Voucher richiesto è per e-Service (quindi non per API di Interoperabilità) e segue l'implementazione ``POP_DPoP``.
    - [:rfc:`9449`], [`PDND`_]

La `Voucher Request` DEVE includere i seguenti parametri nel body:

.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Parametro**
    - **Descrizione**
    - **Riferimento**
  * - **client_id**
    - Identificativo univoco del Client dell'Aderente, assegnato dalla PDND.
    - [:rfc:`6749`], [:rfc:`7521`], [:rfc:`7523`], [`PDND`_]
  * - **client_assertion**
    - Un JWT che rappresenta l'asserzione del client.
    - [:rfc:`7521`], [:rfc:`7523`], [`PDND`_]
  * - **client_assertion_type**
    - DEVE essere impostato su ``urn:ietf:params:oauth:client-assertion-type:jwt-bearer``.
    - [:rfc:`7521`], [:rfc:`7523`]
  * - **grant_type**
    - DEVE essere impostato su ``client_credentials``.
    - [:rfc:`6749`], [:rfc:`7523`]

Il JWT ``client_assertion`` DEVE includere i seguenti parametri nel JOSE header:

.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Parametro**
    - **Descrizione**
    - **Riferimento**
  * - **alg**
    - Identificativo di un algoritmo di firma digitale.
    - [:rfc:`7515`]
  * - **kid**
    - Identificativo univoco del JWK utilizzato dall'Aderente per firmare ``client_assertion``.
    - [:rfc:`7515`]
  * - **typ**
    - DEVE essere impostato su ``JWT``.
    - [:rfc:`7515`], [:rfc:`7519`]

Il JWT ``client_assertion`` DEVE includere i seguenti claim nel payload (se non diversamente specificato):

.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Claim**
    - **Descrizione**
    - **Riferimento**
  * - **iss**
    - DEVE essere impostato sullo stesso valore di ``client_id``.
    - [:rfc:`7523`]
  * - **sub**
    - DEVE essere impostato sullo stesso valore di ``client_id``.
    - [:rfc:`7523`]
  * - **aud**
    - Identificativo dell'Endpoint Authorization Server PDND.
    - [:rfc:`7523`]
  * - **exp**
    - Timestamp UNIX che rappresenta l'istante di scadenza del JWT.
    - [:rfc:`7523`]
  * - **nbf**
    - Timestamp UNIX che rappresenta il primo istante di validità del JWT (opzionale).
    - [:rfc:`7519`]
  * - **iat**
    - Timestamp UNIX che rappresenta l'istante di emissione del JWT.
    - [:rfc:`7523`]
  * - **jti**
    - Identificativo univoco del JWT per prevenire attacchi di replay.
    - [:rfc:`7523`]
  * - **purposeId**
    - Identificativo dello scopo registrato nella Piattaforma PDND, associato all'e-Service previsto. È obbligatorio solo se il Voucher richiesto è per e-Service (quindi non per API di Interoperabilità).
    - [`MODI`_], [`PDND`_]
  * - **digest**
    - Oggetto JSON contenente il digest del JWT ``TrackingEvidence``. È obbligatorio solo se il Voucher richiesto è per e-Service (quindi non per API di Interoperabilità), e quando si rispetta ``AUDIT_REST_02`` o l'implementazione ``POP_TPoP``. Se presente, DEVE contenere i seguenti claim:

      - **alg**: stringa JSON che rappresenta l'algoritmo di hashing;
      - **value**: stringa JSON che rappresenta il valore del digest.
    - [`MODI`_]

Risposta (Voucher PDND)
"""""""""""""""""""""""

La `Voucher Response` DEVE includere i seguenti parametri nel body:

.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Parametro**
    - **Descrizione**
    - **Riferimento**
  * - **access_token**
    - JWT che rappresenta l'Access Token emesso dall'Endpoint Authorization Server PDND.
    - [:rfc:`6749`], [:rfc:`9449`], [`PDND`_]
  * - **token_type**
    - DEVE essere impostato su:

      - ``DPoP`` in caso di Voucher per e-Service seguendo l'implementazione ``POP_DPoP``;
      - ``Bearer`` in caso di Voucher per API di Interoperabilità, o Voucher per e-Service seguendo l'implementazione ``POP_TPoP``.
    - [:rfc:`6749`], [:rfc:`9449`]
  * - **expires_in**
    - Numero che rappresenta la durata dell'Access Token in secondi come intero positivo.
    - [:rfc:`6749`], [:rfc:`9449`]

Il JWT ``access_token`` DEVE includere i seguenti parametri nel JOSE header:

.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Parametro**
    - **Descrizione**
    - **Riferimento**
  * - **alg**
    - Identificativo di un algoritmo di firma digitale.
    - [:rfc:`7515`]
  * - **kid**
    - Identificativo univoco del JWK utilizzato dall'Endpoint Authorization Server PDND per firmare ``access_token``.
    - [:rfc:`7515`]
  * - **typ**
    - DEVE essere impostato su ``at+jwt``.
    - [:rfc:`9068`]

Il JWT ``access_token`` DEVE includere i seguenti claim nel payload (se non diversamente specificato):

.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Claim**
    - **Descrizione**
    - **Riferimento**
  * - **iss**
    - Identificativo dell'Authorization Server PDND.
    - [:rfc:`7519`], [:rfc:`9068`]
  * - **sub**
    - Identificativo dell'Aderente, corrispondente al parametro ``client_id`` nel body della `Voucher Request`.
    - [:rfc:`7519`], [:rfc:`9068`]
  * - **aud**
    - Identificativo dell'e-Service.
    - [:rfc:`7519`], [:rfc:`9068`]
  * - **exp**
    - Timestamp UNIX che rappresenta l'istante di scadenza del JWT.
    - [:rfc:`7519`], [:rfc:`9068`]
  * - **nbf**
    - Timestamp UNIX che rappresenta il primo istante di validità del JWT (opzionale).
    - [:rfc:`7519`]
  * - **iat**
    - Timestamp UNIX che rappresenta l'istante di emissione del JWT.
    - [:rfc:`7519`], [:rfc:`9068`]
  * - **jti**
    - Identificativo univoco del JWT per prevenire attacchi di replay.
    - [:rfc:`7519`], [:rfc:`9068`]
  * - **client_id**
    - DEVE corrispondere al ``client_id`` contenuto nella `Voucher Request`.
    - [:rfc:`7519`], [:rfc:`8963`], [:rfc:`9068`], [`PDND`_]
  * - **purposeId**
    - DEVE corrispondere al valore del claim ``purposeId`` contenuto nella `Voucher Request`. È obbligatorio solo se il Voucher richiesto è per e-Service (cioè, non per API di Interoperabilità).
    - [`MODI`_], [`PDND`_]
  * - **digest**
    - DEVE corrispondere al valore dell'oggetto ``digest`` contenuto nella `Voucher Request`. È obbligatorio solo quando si rispetta ``AUDIT_REST_02`` o l'implementazione ``POP_TPoP``.
    - [`MODI`_]
  * - **cnf**
    - DEVE contenere un claim **jkt** che è il JWK SHA-256 Thumbprint Confirmation Method. Il valore del claim *jkt* DEVE essere la codifica base64url (come definito in [:rfc:`7515`]) del JWK SHA-256 Thumbprint della chiave pubblica DPoP (in formato JWK) a cui l'Access Token è associato. È obbligatorio solo quando si rispetta l'implementazione ``POP_DPoP``.
    - [:rfc:`9449`. Sezione 6.1] e [:rfc:`7638`].

Se si verificano errori durante la validazione della `Voucher Request`, l'Endpoint Authorization Server PDND DEVE restituire una risposta di errore come definito in :rfc:`6749#section-5.2`. La risposta DEVE utilizzare ``application/json`` come ``Content-Type``. La risposta DEVE includere i seguenti parametri.

  - ``error``: Il codice di errore.
  - ``error_description``: Testo in forma leggibile dall'uomo che fornisce ulteriori dettagli per chiarire la natura dell'errore incontrato.

.. literalinclude:: ../../examples/shared/e-service-pdnd-15.http
   :language: http
   :caption: Esempio non normativo di una `Voucher Error Response`
   :name: code_VoucherIssuance_Endpoint_AuthorizationServer_Error


La seguente tabella elenca gli HTTP Status Code e i relativi codici di errore che DEVONO essere supportati per la risposta di errore:

.. list-table::
  :class: longtable
  :widths: 20 20 60
  :header-rows: 1

  * - **HTTP Status Code**
    - **Codice di Errore**
    - **Descrizione**
  * - ``400 Bad Request``
    - ``invalid_request``
    - La richiesta non può essere soddisfatta perché mancano parametri richiesti, contiene parametri non validi o è in qualche modo malformata [:rfc:`6749#section-5.2`].
  * - ``400 Bad Request``
    - ``invalid_grant``
    - La richiesta non può essere soddisfatta perché il grant fornito (cioè, ``client_assertion``) è scaduto, revocato, già utilizzato o in qualche modo malformato [:rfc:`6749#section-5.2`].
  * - ``400 Bad Request``
    - ``unsupported_grant_type``
    - La richiesta non può essere soddisfatta perché il tipo di grant fornito non è supportato dall'Authorization Server PDND [:rfc:`6749#section-5.2`].
  * - ``400 Bad Request``
    - ``invalid_scope``
    - La richiesta non può essere soddisfatta perché il ``purposeId`` fornito non è valido, è sconosciuto, malformato o non associato al Client [:rfc:`6749#section-5.2`].
  * - ``400 Bad Request``
    - ``invalid_dpop_proof``
    - La richiesta non può essere soddisfatta perché contiene una *DPoP proof* non valida [:rfc:`9449#section-5`].
  * - ``401 Unauthorized``
    - ``invalid_client``
    - La richiesta non può essere soddisfatta perché l'autenticazione del Client è fallita (quindi ``client_assertion`` è malformato, firmato in modo errato, mancante o non verificabile) [:rfc:`6749#section-5.2`].
  * - ``500 Internal Server Error``
    - ``server_error``
    - La richiesta non può essere soddisfatta perché l'Authorization Server PDND ha riscontrato un problema interno.
  * - ``503 Service Unavailable``
    - ``temporarily_unavailable``
    - La richiesta non può essere soddisfatta perché l'Authorization Server PDND è temporaneamente non disponibile (ad esempio, a causa di manutenzione o sovraccarico).

Reperimento delle Chiavi
------------------------

Chiavi dell'Authorization Server PDND
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _fig_KeyRetrieval_PDND_Flow:
.. plantuml:: plantuml/pdnd-key-retrieval.puml
    :width: 80%
    :alt: La figura illustra il reperimento delle chiavi dell'Authorization Server PDND - Flusso dettagliato.
    :caption: `Reperimento delle chiavi dell'Authorization Server PDND - Flusso dettagliato. <https://www.plantuml.com/plantuml/svg/RSx1IWCn58NXVPxYK7U1-01Tb1Qw40ILp6BMQNl4q4nIRsvc79_UgOWAkZsN_-DkgmRHDYJSSuQdIkGO4XoUzWzxer4J_p-PqBJaDXmenXpA6wozxjRYPlVUX0QuB7Gynal8YfMrjnDJSkTSfcpj2g6YDymdBF6t86MC9yfLkIkPyvxJN-Xnr_G5dhKqEH8TPQHyaRxxCNtdDlqQdg-DLV5SvFDrd3bNOthdDhvR_vgsIzc6z040>`_


.. .. figure:: ../../images/Low-Level-Flow-AuthenticSource-KeyRetrieval-PDND.svg
..   :figwidth: 100%
..   :align: center
..   :target: https://www.plantuml.com/plantuml/svg/PS_1IWCn58NXVPxYK7U1-01Tb1Pc8GWgcSMiq_Q8eMbIRsvc79_UgOWAtHxuF-xTLWsYxPoCHat48sTugaIE8S7XfNlgZ0bDIsxdFSMOVVc0jTVTMjpjFflG09T5YOTu2LcnilP-OahkbCkKhLqXL0o6-OWb_XMaZF58kIeF9NFkEDr2pxkcR_2ifSc1w2aZvOVq_P_fUxSPrl1yRwoAroBVf-F4kHepEBVn_VhVj5tAvUil

..   Recupero delle Chiavi per le Chiavi PDND - Flusso dettagliato

**Passo 1 (Richiesta delle chiavi)**: L'Erogatore richiede le chiavi utilizzate dalla PDND per firmare i Voucher.

.. code-block:: http
  :caption: Esempio non normativo della `Keys Request`
  :name: _code_KeyRetrieval_PDND_Flow_Request

  GET /.well-known/jwks.json HTTP/1.1
  Host: interop.pagopa.it

**Passo 2 (Risposta)**: L'Endpoint .well-known restituisce l'elenco delle chiavi utilizzate dalla PDND per firmare i Voucher, come un ``JWK Set`` [:rfc:`7517`].

.. literalinclude:: ../../examples/shared/e-service-pdnd-16.http
   :language: http
   :caption: Esempio non normativo della `Keys Response`
   :name: _code_KeyRetrieval_PDND_Flow_Response

Endpoint .well-known dell'Authorization Server PDND
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

L'Endpoint .well-known fa parte dell'Infrastruttura PDND ed è utilizzato per reperire le chiavi pubbliche utilizzate dall'Authorization Server PDND per firmare i Voucher.

Richiesta (Chiavi dell'Authorization Server PDND)
"""""""""""""""""""""""""""""""""""""""""""""""""

La `Keys Request` è una richiesta HTTP ``GET`` inviata all'Endpoint .well-known. Questo endpoint consente agli Aderenti di reperire le chiavi pubbliche necessarie per verificare le firme digitali sui Voucher emessi dall'Authorization Server PDND.

Risposta (Chiavi dell'Authorization Server PDND)
""""""""""""""""""""""""""""""""""""""""""""""""

L'Endpoint .well-known risponde con un HTTP Status Code ``200 OK`` e un ``JWK Set`` [:rfc:`7517`] contenente le chiavi pubbliche impiegate dall'Authorization Server PDND per firmare i Voucher.

Se si verificano errori durante il reperimento delle chiavi, l'Endpoint .well-known DEVE restituire una risposta di errore. La risposta DEVE utilizzare ``application/json`` come ``Content-Type``. La risposta DEVE includere i seguenti parametri.

  - ``error``: Il codice di errore.
  - ``error_description``: Testo in forma leggibile dall'uomo che fornisce ulteriori dettagli per chiarire la natura dell'errore incontrato.

.. literalinclude:: ../../examples/shared/e-service-pdnd-17.http
   :language: http
   :caption: Esempio non normativo di una `Keys Error Response`
   :name: code_KeyRetrieval_Endpoint_WellKnown_Error


La seguente tabella elenca gli HTTP Status Code e i relativi codici di errore che DEVONO essere supportati per la risposta di errore:

.. list-table::
  :class: longtable
  :widths: 20 20 60
  :header-rows: 1

  * - **HTTP Status Code**
    - **Codice di Errore**
    - **Descrizione**
  * - ``500 Internal Server Error``
    - ``server_error``
    - La richiesta non può essere soddisfatta perché l'Endpoint .well-known ha riscontrato un problema interno.
  * - ``503 Service Unavailable``
    - ``temporarily_unavailable``
    - La richiesta non può essere soddisfatta perché l'Endpoint .well-known è temporaneamente non disponibile (ad esempio, a causa di manutenzione o sovraccarico).

Chiavi degli Aderenti
^^^^^^^^^^^^^^^^^^^^^

Prerequisiti per il Reperimento delle Chiavi degli Aderenti
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

L'**Aderente** che richiede la chiave DEVE rispettare i seguenti prerequisiti:

    - Ha completato con successo l'adesione all'Infrastruttura PDND (come da R1).
    - Ha creato un nuovo `Client api interop` per interagire con l'API di Interoperabilità PDND. Al momento della creazione, gli è stato assegnato un ``client_id`` dalla Piattaforma PDND.
    - Ha registrato una coppia di chiavi associata al `Client api interop`.
    - Ha ottenuto un Voucher valido per interrogare l'API di Interoperabilità PDND, relativo allo specifico `Client api interop`.

Flusso di Reperimento delle Chiavi degli Aderenti
"""""""""""""""""""""""""""""""""""""""""""""""""

.. _fig_KeyRetrieval_Participant_Flow:
.. plantuml:: plantuml/pdnd-key-retrieval-participant.puml
    :width: 80%
    :alt: La figura illustra il reperimento delle chiavi degli Aderenti - Flusso dettagliato.
    :caption: `Reperimento delle chiavi degli Aderenti - Flusso dettagliato. <https://www.plantuml.com/plantuml/svg/fSp1IiGm4CRnUvxY8nw4mBx07fOjRS4YQDcpbxITrM7J92OJjJwz5SGAWXUlC__lTynYavJPuPOMd4WIqujrsA5Vxpnoj5wo4XP7VoVA5Wc-p0CbfORm1cFwvgun1bVLUqcaWBZrqCPqNYY5ICaEx5WML7rdZ8RDw1Jv2QloJMtJJ_4cU5eQUlsDtbT5db0x9YzVMDrkMjtk3jt-HC-5ik0S4dx8rncn38v7N6Xvy6D8YN8CVcB_20d8aKO-hs-jBpnfhQ2wtQ5kz_ynZkIdChiF>`_


.. .. figure:: ../../images/Low-Level-Flow-AuthenticSource-KeyRetrieval-Participant.svg
..     :figwidth: 100%
..     :align: center
..     :target: https://www.plantuml.com/plantuml/svg/fSp1IlGm5CNnVPxYa6_nGQ0lC8jXIbkm25fcxIPjx-XbqYGcDsfzUYk85Low_f_pEsMnIShYbB0umYsjE9CafXVhK67OAayShPUib2qIV5b6IagDuGt63ErTQmp-rUybaGBYleSsflT2AKHATcJ7ig8UUcCqR4QloC_Ob6zgltwADy7JsjBhR_I-BlA4nZ5v-SAQRjUQhZhsXpCz5yg2IqZu8V_FY6LqFE5AwuEVGagKO_0p-qT8G8uqyMNBMbzvrbf1zTMnwGv_CKxavxAu3m00

..     Recupero delle Chiavi per la Chiave del Partecipante - Flusso dettagliato

**Passo 1 (Richiesta della chiave)**: L'Aderente richiede la chiave utilizzata da un altro Aderente, corrispondente a uno specifico ``kid``, alle API di Interoperabilità PDND.

.. literalinclude:: ../../examples/shared/e-service-pdnd-18.http
   :language: http
   :caption: Esempio non normativo della `Key Request`
   :name: _code_KeyRetrieval_Participant_Flow_Request

**Passo 2 (Risposta)**: L'Endpoint API di Interoperabilità restituisce la chiave richiesta, come un ``JWK`` [:rfc:`7517`].

.. literalinclude:: ../../examples/shared/e-service-pdnd-19.http
   :language: http
   :caption: Esempio non normativo della `Key Response`
   :name: _code_KeyRetrieval_Participant_Flow_Response


.. note::
  L'API di Interoperabilità include un endpoint di notifica degli eventi che avvisa gli Aderenti iscritti sui cambiamenti all'interno dell'Infrastruttura PDND. Tra queste notifiche, l'endpoint ``/events/keys`` fornisce aggiornamenti sulle modifiche al materiale crittografico, come aggiunte o eliminazioni di chiavi. Sfruttando questo meccanismo, gli Aderenti possono implementare una strategia di polling periodico per recuperare tutte le chiavi modificate e aggiornare la loro cache locale. Ciò elimina la necessità di richiedere ogni chiave individualmente durante il flusso.

Endpoint API di Interoperabilità PDND
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

L'Endpoint API di Interoperabilità fa parte dell'Infrastruttura PDND ed è utilizzato per recuperare le chiavi pubbliche di altri Aderenti all'Infrastruttura PDND.

Richiesta (Chiave da API di Interoperabilità PDND)
""""""""""""""""""""""""""""""""""""""""""""""""""

La `Key Request` è una richiesta HTTP ``GET`` inviata all'API ``/keys/<kid>``. Questa richiesta viene utilizzata per recuperare una chiave specifica identificata dal suo ``kid`` univoco.

La `Key Request` DEVE includere i seguenti parametri di header HTTP:

.. list-table::
  :widths: 20 60 20
  :header-rows: 1

  * - **Parametro**
    - **Descrizione**
    - **Riferimento**
  * - **Authorization**
    - Voucher rilasciato dall'Authorization Server PDND.
    - [:rfc:`9449`]

Risposta (Chiave da API di Interoperabilità PDND)
"""""""""""""""""""""""""""""""""""""""""""""""""

Nel caso in cui esista una chiave pubblica con il ``kid`` fornito, l'Endpoint dell'API di Interoperabilità risponde con un codice di stato ``200 OK`` e un ``JWK`` [:rfc:`7517`] che rappresenta quella chiave.

Se si verificano errori durante il reperimento della chiave, l'Endpoint API di Interoperabilità DEVE restituire un errore, la cui struttura dipende dalla natura dell'errore.

In caso di problemi di autenticazione (cioè, Voucher non valido o scaduto), la risposta DEVE aderire al formato di errore definito in :rfc:`6750#section-3`. Il formato riguarda in particolare l'uso del parametro di header ``WWW-Authenticate``.

.. literalinclude:: ../../examples/shared/e-service-pdnd-20.http
   :language: http
   :caption: Esempio non normativo di una `Key Error Response` in caso di errori 401
   :name: code_KeyRetrieval_Endpoint_InteroperabilityAPI_Error_401

Per tutti gli altri errori, la risposta DEVE aderire al formato di errore definito in :rfc:`6749#section-5.2`. La risposta DEVE utilizzare ``application/json`` come tipo di contenuto. La risposta DEVE includere i seguenti parametri.

    - ``error``: Il codice di errore.
    - ``error_description``: Testo in forma leggibile dall'uomo che fornisce ulteriori dettagli per chiarire la natura dell'errore incontrato.

.. literalinclude:: ../../examples/shared/e-service-pdnd-21.http
   :language: http
   :caption: Esempio non normativo di una `Key Error Response` in caso di altri errori
   :name: code_KeyRetrieval_Endpoint_InteroperabilityAPI_Error_Others


La seguente tabella elenca gli HTTP Status Code e i relativi codici di errore che DEVONO essere supportati per la risposta di errore:

.. list-table::
  :class: longtable
  :widths: 20 20 60
  :header-rows: 1

  * - **HTTP Status Code**
    - **Codice di Errore**
    - **Descrizione**
  * - ``400 Bad Request``
    - ``invalid_request``
    - La richiesta non può essere soddisfatta perché mancano parametri richiesti, contiene parametri non validi o è in qualche modo malformata [:rfc:`6750#section-3.1`].
  * - ``401 Unauthorized``
    - ``invalid_token``
    - La richiesta non può essere soddisfatta perché il Voucher è scaduto, revocato, malformato o in qualche modo non valido [:rfc:`6750#section-3.1`].
  * - ``404 Not Found``
    - ``not_found``
    - La richiesta non può essere soddisfatta perché non è stata trovata alcuna chiave pubblica corrispondente al ``kid`` fornito.
  * - ``500 Internal Server Error``
    - ``server_error``
    - La richiesta non può essere soddisfatta perché l'Endpoint API di Interoperabilità ha riscontrato un problema interno.
  * - ``503 Service Unavailable``
    - ``temporarily_unavailable``
    - La richiesta non può essere soddisfatta perché l'Endpoint API di Interoperabilità è temporaneamente non disponibile (ad esempio, a causa di manutenzione o sovraccarico).

Utilizzo dell'e-Service
-----------------------

Prerequisiti per l'Utilizzo dell'e-Service
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Il **Fruitore** DEVE rispettare i seguenti prerequisiti:

  - Ha ottenuto un Voucher valido per interagire con l'e-Service desiderato, relativo a uno specifico `Client e-service`.

L'**Erogatore** DEVE rispettare i seguenti prerequisiti:

  - Ha creato un nuovo portachiavi associato allo specifico e-Service.
  - Ha registrato una coppia di chiavi associata al portachiavi.

.. note::
  Il portachiavi dell'Erogatore è la controparte del Client relativo al Fruitore. Memorizza materiale crittografico, consentendo ai Fruitori di verificare l'integrità delle risposte dagli Erogatori.


Flusso di Utilizzo dell'e-Service
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _fig_Usage_Flow:
.. plantuml:: plantuml/pdnd-eservice-usage.puml
    :width: 80%
    :alt: La figura illustra l'Utilizzo dell'e-Service - Flusso dettagliato.
    :caption: `Utilizzo dell'e-Service - Flusso dettagliato. <https://www.plantuml.com/plantuml/svg/ZP31RjGm48RlVegHUm5BAo6EFQ2kaYuK8RfAjd1SkSwGM9jumdYyPVlqE4sxiAfQzHB5zlpVVFelebYMDFI0Ynfvxnt2JRGjAl7IuxDRPPDGICCjibAtz0UCAIZ4D20R0sTNU-A30XWpr3i_sY2WZRbU9kcWw3q6CKQ3ZL2i58O6CkA9iow_bnDZUPyONs9C7s9_RyLJWCaD-P6uh9yHcVQ-cSs-KC13YNSlWIkCbDZXARFwZrci5f-ArVcQCGCGllxSm9tFoUZRO2KnmZkjwwU3rk-F4IWOhI2KQrh3o4I_vgUgFeVIYitBVoUCClD-K7BTL2y7oY7ADja3phxvjfFFZ1WKGD6Xsu7M4rBhIV9X-cqXwnp6k1NQOJW9qoXm7Vh3BABrygQyscohotgp_V0nJmAyXl-tOCFMxNneBwVwWyE7w75D_dcRvx7C4ycgNiojFhQ63JHMhBh88sde_m80>`_


.. .. figure:: ../../images/Low-Level-Flow-AuthenticSource-Usage.svg
..     :figwidth: 100%
..     :align: center
..     :target: https////www.plantuml.com/plantuml/svg/ZP1HRzCm4CVV_IbEtWjOgeHut0DQbQmmX5YLTF1OUSwHM4ryuNpkw3uzph8LAZJK5ykMx_-xd_vNKInB6debNde4NDJ8U-yGxg9jKIcRX48Qxf6LkgTVO4n18QO1sHYukDaJ7nJ0c27U-T460MtCxJ991qNlCOWn6co4OgKmD90HBvnr-RMS6Cl7nFWQOpg8_QCLJm4cD-HduhB-XyYqzyrizea27afyU0rSOQJ43a-PrL_COhNuKAmkrumPWF3v-mOUV4v6tmOhYH7UQ5s_FBH-Uun0mMW5eLpJ6aOc-Z5_LVKbb5PiNlupOPIPzusIwwPwEL0EKRR97d3nnRUTV6J4e02A3jqEj9wGMa-IJzFdXQnp6EDMQ8VX94oZm6te3xE8rikxycQphQxhpVRT-pm9y3_ydmKRjcxdGtizrHySFaMFQ_BbFCzZcIUILRsOMtrk3Hjeh5XrbKVIqFy6

..     Utilizzo dell'e-Service - Flusso dettagliato

**Passo 1 (Preparazione della firma):** Il Fruitore prepara un JWT (``Signature``) contenente le intestazioni firmate del messaggio, per garantire l'integrità.

.. literalinclude:: ../../examples/shared/e-service-pdnd-22.json
   :language: json
   :caption: Esempio non normativo dell'header di ``Signature``
   :name: _code_Usage_Flow_Signature_Header

.. literalinclude:: ../../examples/shared/e-service-pdnd-23.json
   :language: json
   :caption: Esempio non normativo del payload di ``Signature``
   :name: _code_Usage_Flow_Signature_Payload

.. note::
  Il passo 1 è richiesto per rispettare il pattern di sicurezza ``INTEGRITY_REST_02``.

**Passo 2 (`DPoP proof`)**: Il Fruitore DEVE creare un nuovo JWT di `DPoP proof` seguendo le istruzioni fornite nella Sezione 4 di [:rfc:`9449`] per la presentazione del token all'Endpoint e-Service.

.. note::
  Il passo 2 è richiesto solo quando si rispetta l'implementazione ``POP_DPoP``.

**Passo 3 (Richiesta e-Service):** Il Fruitore invia una `e-Service Request` all'Erogatore, includendo il Voucher.

.. literalinclude:: ../../examples/shared/e-service-pdnd-24.http
   :language: http
   :caption: Esempio non normativo della `e-Service Request`
   :name: _code_Usage_Flow_Request

L'Erogatore DEVE validare la `DPoP proof` [:rfc:`9449`].

.. note::
  La validazione della `DPoP proof` è richiesta solo quando si rispetta l'implementazione ``POP_DPoP``.

L'Erogatore DEVE validare il Voucher come segue:

    Header:

      - Assicurarsi che il claim ``typ`` sia presente e che il suo valore sia ``at+jwt``.

    Firma:

      - Reperire l'insieme di chiavi pubbliche pubblicate all'Endpoint .well-known. Da questo insieme, selezionare la chiave pubblica il cui identificatore corrisponde al valore del parametro header ``kid`` nel Voucher.
      - Validare la firma dell'``access_token`` utilizzando la chiave pubblica recuperata e l'algoritmo specificato dal parametro header ``alg``.

    Payload:

      - Il claim ``iss`` DEVE identificare il dominio dell'Authorization Server PDND.
      - Il claim ``sub`` DEVE corrispondere al claim ``client_id``.
      - Il claim ``aud`` DEVE corrispondere all'e-Service previsto.
      - In caso di implementazione ``POP_DPoP``, il claim ``cnf.jkt`` DEVE corrispondere al SHA-256 Thumbprint della chiave pubblica DPoP nel claim ``jwk`` nella prova DPoP.

.. note::
  Se l'Erogatore richiede maggiori informazioni sul contesto della richiesta, può interagire con l'API di Interoperabilità PDND passando il valore del ``purposeId`` come parametro.

L'Erogatore DEVE validare il JWT ``TrackingEvidence`` come segue:

  Header:

    - Assicurarsi che il claim ``typ`` sia presente e che il suo valore sia ``JWT``.

  Firma:

    - Ottenere la chiave pubblica del Fruitore corrispondente al parametro header ``kid``, interagendo con l'API di Interoperabilità PDND.
    - Validare la firma del JWT utilizzando la chiave pubblica del Fruitore recuperata e l'algoritmo specificato dal parametro header ``alg``.

  Payload:

    - Il claim ``iss`` DEVE identificare il Client del Fruitore.
    - Il claim ``aud`` DEVE identificare l'Erogatore.

Inoltre, l'Erogatore DEVE assicurarsi che l'hash del JWT ``TrackingEvidence`` corrisponda al valore del claim ``digest.value`` contenuto nel payload ``access_token``.

.. note::
  La validazione del JWT ``TrackingEvidence`` è richiesta solo quando si rispetta il pattern di sicurezza ``AUDIT_REST_02`` o l'implementazione ``POP_TPoP``.

L'Erogatore DEVE validare il JWT ``Signature`` come segue:

  Header:

    - Assicurarsi che il claim ``typ`` sia presente e che il suo valore sia ``JWT``.

  Firma:

    - Validare la firma del JWT utilizzando la chiave pubblica del Fruitore recuperata e l'algoritmo specificato dal parametro header ``alg``.

  Payload:

    - I claim ``iss`` e ``sub`` DEVONO identificare il Client del Fruitore.
    - Il claim ``aud`` DEVE identificare l'Erogatore.

Inoltre, l'Erogatore DEVE validare l'integrità della `e-Service Request`, verificando che:

  - Il claim ``signed_headers.content-type`` corrisponda al valore dell'header HTTP ``Content-Type`` della `e-Service Request`.
  - Il claim ``signed_headers.digest`` corrisponda al valore del digest del payload della `e-Service Request`, nonché al valore dell'header HTTP ``Digest`` della `e-Service Request`.


Se uno qualsiasi dei controlli precedenti fallisce, l'Erogatore DEVE rifiutare la richiesta.

**Passo 4 (Risposta):** Qualora i controlli abbiano successo, l'Erogatore fornisce al Fruitore i dati richiesti. Nelle intestazioni della risposta DEVE essere presente il JWT (``Signature``) al fine di garantire l'integrità.

.. literalinclude:: ../../examples/shared/e-service-pdnd-25.http
   :language: http
   :caption: Esempio non normativo della `e-Service Response`
   :name: _code_Usage_Flow_Response

Il Fruitore DEVE validare il JWT ``Signature`` come segue:

  Header:

    - Assicurarsi che il claim ``typ`` sia presente e che il suo valore sia ``JWT``.

  Firma:

    - Validare la firma del JWT utilizzando la chiave pubblica del Fruitore recuperata e l'algoritmo specificato dal parametro header ``alg``.

  Payload:

    - I claim ``iss`` e ``sub`` DEVONO identificare l'Erogatore.
    - Il claim ``aud`` DEVE identificare il Client del Fruitore.

Inoltre, il Fruitore DEVE validare l'integrità della `e-Service Response`, verificando che:

  - Il claim ``signed_headers.content-type`` corrisponda al valore dell'header HTTP ``Content-Type`` della `e-Service Response`.
  - Il claim ``signed_headers.digest`` corrisponda al valore del digest del payload della `e-Service Response`, nonché al valore dell'header HTTP ``Digest`` della `e-Service Response`.

Se uno qualsiasi dei controlli precedenti fallisce, il Fruitore DEVE rifiutare la richiesta.

Endpoint e-Service
^^^^^^^^^^^^^^^^^^

Richiesta (e-Service)
"""""""""""""""""""""

La `e-Service Request` DEVE includere i seguenti parametri di header HTTP (se non diversamente specificato):

.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Parametro**
    - **Descrizione**
    - **Riferimento**
  * - **Authorization**
    - Voucher rilasciato dall'Authorization Server PDND.
    - [:rfc:`9449`], [`MODI`_], [`PDND`_]
  * - **DPoP**
    - JWT di `DPoP proof`, per rispettare il pattern di sicurezza ``REST_JWS_2021_POP``. È obbligatorio solo quando si segue l'implementazione ``POP_DPoP``.
    - [:rfc:`9449`], [`PDND`_]
  * - **Agid-JWT-Signature**
    - JWT contenente la firma delle intestazioni del messaggio la cui integrità deve essere garantita, per rispettare il pattern di sicurezza ``INTEGRITY_REST_02``.
    - [`MODI`_]
  * - **Digest**
    - Digest del payload del messaggio, per rispettare il pattern di sicurezza ``INTEGRITY_REST_02``. Secondo :rfc:`3230`, il formato DEVE essere il seguente: ``<digest-algorithm>=<encoded digest output>``.
    - [:rfc:`3230`], [`MODI`_]
  * - **Agid-JWT-TrackingEvidence**
    - JWT contenente i dati tracciati nel dominio del Fruitore. È obbligatorio solo quando si rispetta ``AUDIT_REST_02`` o l'implementazione ``POP_TPoP``.
    - [`MODI`_]

Il JWT ``Signature``, contenuto nell'header HTTP ``Agid-JWT-Signature``, DEVE includere i seguenti parametri nel JOSE header:

.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Parametro**
    - **Descrizione**
    - **Riferimento**
  * - **alg**
    - Identificativo di un algoritmo di firma digitale.
    - [:rfc:`7515`]
  * - **kid**
    - Identificativo univoco del JWK utilizzata dal Fruitore per firmare il JWT.
    - [:rfc:`7515`]
  * - **typ**
    - DEVE essere impostato su ``JWT``.
    - [:rfc:`7515`], [:rfc:`7519`]

Il JWT ``Signature``, contenuto nell'header HTTP ``Agid-JWT-Signature``, DEVE includere i seguenti claim nel payload:

.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Claim**
    - **Descrizione**
    - **Riferimento**
  * - **iss**
    - DEVE essere impostato sullo stesso valore di ``client_id``.
    - [:rfc:`7519`]
  * - **sub**
    - DEVE essere impostato sullo stesso valore di ``client_id``.
    - [:rfc:`7519`]
  * - **aud**
    - Identificativo dell'Erogatore.
    - [:rfc:`7519`]
  * - **exp**
    - Timestamp UNIX che rappresenta l'istante di scadenza del JWT.
    - [:rfc:`7519`]
  * - **nbf**
    - Timestamp UNIX che rappresenta il primo istante di validità del JWT (opzionale).
    - [:rfc:`7519`]
  * - **iat**
    - Timestamp UNIX che rappresenta l'istante di emissione del JWT.
    - [:rfc:`7519`]
  * - **jti**
    - Identificativo univoco del JWT per prevenire attacchi di replay.
    - [:rfc:`7519`]
  * - **signed_headers**
    - Oggetto JSON contenente le intestazioni firmate la cui integrità deve essere protetta, per rispettare ``INTEGRITY_REST_02``. DEVE contenere i seguenti claim:

      - **digest**: stringa JSON che rappresenta la firma dell'header HTTP ``Digest``
      - **content-type**: stringa JSON che rappresenta la firma dell'header HTTP ``Content-Type``
    - [`MODI`_]

Se presente, il JWT ``TrackingEvidence``, contenuto nell'header HTTP ``Agid-JWT-TrackingEvidence``, DEVE includere i seguenti parametri nel JOSE header:

.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Parametro**
    - **Descrizione**
    - **Riferimento**
  * - **alg**
    - Identificativo di un algoritmo di firma digitale.
    - [:rfc:`7515`]
  * - **kid**
    - Identificativo univoco del JWK utilizzato dal Fruitore per firmare il JWT.
    - [:rfc:`7515`]
  * - **typ**
    - DEVE essere impostato su ``JWT``.
    - [:rfc:`7515`], [:rfc:`7519`]

Se presente, il JWT ``TrackingEvidence``, contenuto nell'header HTTP ``Agid-JWT-TrackingEvidence``, DEVE includere i seguenti claim nel payload:

.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Claim**
    - **Descrizione**
    - **Riferimento**
  * - **iss**
    - DEVE essere impostato sullo stesso valore di ``client_id``.
    - [:rfc:`7519`]
  * - **aud**
    - Identificativo dell'Erogatore.
    - [:rfc:`7519`]
  * - **exp**
    - Timestamp UNIX che rappresenta l'istante di scadenza del JWT.
    - [:rfc:`7519`]
  * - **nbf**
    - Timestamp UNIX che rappresenta il primo istante di validità del JWT (opzionale).
    - [:rfc:`7519`]
  * - **iat**
    - Timestamp UNIX che rappresenta l'istante di emissione del JWT.
    - [:rfc:`7519`]
  * - **jti**
    - Identificativo univoco del JWT per prevenire attacchi di replay.
    - [:rfc:`7519`]
  * - **purposeId**
    - Identificativo dello scopo registrato nella Piattaforma PDND, associato all'e-Service previsto.
    - [`MODI`_]
  * - **dnonce**
    - DEVE essere una stringa casuale composta da numeri interi e con una lunghezza di 13 cifre.
    - [`MODI`_]

Quando si rispetta il pattern di sicurezza ``AUDIT_REST_02``, il payload ``TrackingEvidence`` DEVE contenere anche i dati tracciati concordati con l'Erogatore.

Risposta (e-Service)
""""""""""""""""""""

La `e-Service Response` DEVE avere un content type ``application/json``.

La `e-Service Response` DEVE includere i seguenti parametri di header HTTP:

.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Parametro**
    - **Descrizione**
    - **Riferimento**
  * - **Agid-JWT-Signature**
    - JWT contenente la firma delle intestazioni del messaggio la cui integrità deve essere garantita, per rispettare il pattern di sicurezza ``INTEGRITY_REST_02``.
    - [`MODI`_]
  * - **Digest**
    - Digest del payload del messaggio, per rispettare il pattern di sicurezza ``INTEGRITY_REST_02``. Secondo :rfc:`3230`, il formato DEVE essere il seguente: ``<digest-algorithm>=<encoded digest output>``.
    - [:rfc:`3230`], [`MODI`_]

Il JWT ``Signature``, contenuto nell'header HTTP ``Agid-JWT-Signature``, DEVE includere i seguenti claim nel payload:

.. list-table::
  :class: longtable
  :widths: 20 60 20
  :header-rows: 1

  * - **Claim**
    - **Descrizione**
    - **Riferimento**
  * - **iss**
    - Identificativo dell'Erogatore.
    - [:rfc:`7519`]
  * - **sub**
    - Identificativo dell'Erogatore.
    - [:rfc:`7519`]
  * - **aud**
    - Identificativo del Fruitore.
    - [:rfc:`7519`]
  * - **exp**
    - Timestamp UNIX che rappresenta l'istante di scadenza del JWT.
    - [:rfc:`7519`]
  * - **nbf**
    - Timestamp UNIX che rappresenta il primo istante di validità del JWT (opzionale).
    - [:rfc:`7519`]
  * - **iat**
    - Timestamp UNIX che rappresenta l'istante di emissione del JWT.
    - [:rfc:`7519`]
  * - **jti**
    - Identificativo univoco del JWT per prevenire attacchi di replay.
    - [:rfc:`7519`]
  * - **signed_headers**
    - Oggetto JSON contenente le intestazioni firmate la cui integrità deve essere protetta, per rispettare ``INTEGRITY_REST_02``. DEVE contenere i seguenti claim:

      - **digest**: stringa JSON che rappresenta la firma dell'header HTTP ``Digest``
      - **content-type**: stringa JSON che rappresenta la firma dell'header HTTP ``Content-Type``
    - [`MODI`_]

Il payload del JWT della `e-Service Response` include specifici claim relativi ai dati forniti al Fruitore.

Se si verificano errori durante la validazione della `e-Service Request`, l'Endpoint e-Service DEVE restituire un errore, la cui struttura dipende dalla natura dell'errore.

In caso di problemi di autenticazione (cioè, Voucher non valido o scaduto), la risposta DEVE aderire al formato di errore definito in :rfc:`6750#section-3` e :rfc:`9449#section-7.1`. Il formato riguarda in particolare l'uso del parametro di header ``WWW-Authenticate``.

.. literalinclude:: ../../examples/shared/e-service-pdnd-26.http
   :language: http
   :caption: Esempio non normativo di una `e-Service Error Response` in caso di errori 401
   :name: code_Usage_Endpoint_eService_Error_401

Per tutti gli altri errori, la risposta DEVE aderire al formato di errore definito in :rfc:`9457`. La risposta DEVE utilizzare ``application/problem+json`` (secondo MODI ``RAC_GEN_FORMAT_002``) come ``Content-Type``. La risposta DEVE includere i seguenti parametri.

    - ``type``: [OPZIONALE] URI che identifica il tipo di problema.
    - ``title``:  [OBBLIGATORIO] Stringa contenente un breve riepilogo, leggibile dall’utente, del tipo di problema.
    - ``status``: [OBBLIGATORIO] Numero che indica il codice di stato HTTP relativo a questa specifica occorrenza del problema.
    - ``detail``: [OBBLIGATORIO] Stringa contenente una spiegazione, leggibile dall’utente, specifica per questa occorrenza del problema.
    - ``instance``: [OPZIONALE] Stringa contenente un riferimento URI che identifica la specifica occorrenza del problema.

.. literalinclude:: ../../examples/shared/e-service-pdnd-27.http
   :language: http
   :caption: Esempio non normativo di una `e-Service Error Response` in caso di altri errori
   :name: code_Usage_Endpoint_eService_Error


La seguente tabella elenca gli HTTP Status Code che DEVONO essere supportati per la risposta di errore:

.. list-table::
  :class: longtable
  :widths: 50 50
  :header-rows: 1

  * - **HTTP Status Code**
    - **Descrizione**
  * - ``400 Bad Request``
    - La richiesta non può essere soddisfatta perché mancano parametri richiesti, contiene parametri non validi o è in qualche modo malformata.
  * - ``401 Unauthorized``
    - La richiesta non può essere soddisfatta perché il Voucher è scaduto, revocato o in qualche modo malformato.
  * - ``500 Internal Server Error``
    - La richiesta non può essere soddisfatta perché l'Endpoint e-Service ha riscontrato un problema interno.
  * - ``503 Service Unavailable``
    - La richiesta non può essere soddisfatta perché l'Endpoint e-Service è temporaneamente non disponibile (ad esempio, a causa di manutenzione o sovraccarico).



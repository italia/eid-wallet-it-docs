.. include:: ../common/common_definitions.rst

Entity Configuration del Fornitore di Wallet
--------------------------------------------------

Una richiesta HTTP GET all'endpoint della Federazione consente di recuperare la Entity Configuration del Fornitore di Wallet (:ref:`WP_001 <wallet-provider-backend-testcases>`).

La Entity Configuration del Fornitore di Wallet restituita DEVE contenere gli attributi descritti nelle sezioni seguenti.

La Entity Configuration del Fornitore di Wallet è un JWT firmato contenente le chiavi pubbliche e gli algoritmi supportati dalla Soluzione Wallet come componente del Fornitore di Wallet. È strutturata in conformità con `OID-FED`_ e con :ref:`trust-infrastructure:L'Infrastruttura di Trust` delineata in questa specifica (:ref:`WP_002 <wallet-provider-backend-testcases>`).

Header JWT della Entity Configuration del Fornitore di Wallet
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
    :class: longtable
    :widths: 30 70
    :header-rows: 1

    * - **Key**
      - **Value**
    * - alg
      - Algoritmo utilizzato per verificare la firma del token. DEVE essere uno dei possibili valori indicati in :ref:`algorithms:Algoritmi Crittografici` (ad es., ES256).
    * - kid
      - Impronta digitale della chiave pubblica utilizzata per la firma.
    * - typ
      - Tipo di media, impostato su ``entity-statement+jwt``.

Payload JWT della Entity Configuration del Fornitore di Wallet
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
    :class: longtable
    :widths: 30 70
    :header-rows: 1

    * - **Key**
      - **Value**
    * - ``iss``
      - OBBLIGATORIO. URL pubblico della Solutione Wallet.
    * - ``sub``
      - OBBLIGATORIO. URL pubblico della Solutione Wallet.
    * - ``iat``
      - OBBLIGATORIO. Data e ora di emissione in formato Unix Timestamp.
    * - ``exp``
      - OBBLIGATORIO. Data e ora di scadenza in formato Unix Timestamp.
    * - ``authority_hints``
      - OBBLIGATORIO. Array di URL (String) contenente l'elenco degli URL delle Entità superiori immediate, come il Trust Anchor o un Intermediario, che POSSONO emettere un Entity Statement relativo alla Solutione Wallet.
    * - ``jwks``
      - OBBLIGATORIO. Un JSON Web Key Set (JWKS) che rappresenta la parte pubblica delle chiavi di firma dell'Entità di Federazione. La chiave privata corrispondente è utilizzata dalla Soluzione Wallet per firmare la Entity Configuration su se stessa.
    * - ``metadata``
      - OBBLIGATORIO. Oggetto JSON che rappresenta i Tipi di Entità e i metadati per quei Tipi di Entità. Ogni nome membro dell'oggetto JSON è un Identificatore di Tipo di Entità, e ogni valore DEVE essere un oggetto JSON contenente parametri di metadati secondo lo schema di metadati del Tipo di Entità. DEVE contenere i metadati ``wallet_solution`` e OPZIONALMENTE i metadati ``federation_entity``.


.. note::
   I test che coprono la struttura di Entity Configuration (header e payload) sono forniti in :ref:`WP_002a–002h <wallet-provider-backend-testcases>`.

Esempio di Entity Configuration del Fornitore di Wallet
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Di seguito è riportato un esempio non normativo di payload di una Entity Configuration del Fornitore di Wallet contenente metadati per

- `federation_entity`
- `wallet_solution`

.. literalinclude:: ../../examples/ec-wp.json
  :language: JSON



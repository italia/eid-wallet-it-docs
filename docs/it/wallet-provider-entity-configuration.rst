.. include:: ../common/common_definitions.rst

Entity Configuration del Fornitore di Wallet
--------------------------------------------------

Una richiesta HTTP GET all'endpoint della Federazione consente di recuperare la Entity Configuration del Fornitore di Wallet.

La Entity Configuration del Fornitore di Wallet restituita DEVE contenere gli attributi descritti nelle sezioni seguenti.

La Entity Configuration del Fornitore di Wallet è un JWT firmato contenente le chiavi pubbliche e gli algoritmi supportati dal Fornitore di Wallet. È strutturata in conformità con `OID-FED`_ e con :ref:`trust:L'Infrastruttura di Trust` delineata in questa specifica.

Header JWT della Entity Configuration del Fornitore di Wallet
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Key**
      - **Value**
      - **Reference**
    * - alg
      - Algoritmo utilizzato per verificare la firma del token. DEVE essere uno dei possibili valori indicati in :ref:`algorithms:Algoritmi Crittografici` (ad es., ES256).
      - `OID-FED`_.
    * - kid
      - Impronta digitale della chiave pubblica utilizzata per la firma.
      - `OID-FED`_ e :rfc:`7638`.
    * - typ
      - Tipo di media, impostato su ``entity-statement+jwt``.
      - `OID-FED`_.

Payload JWT della Entity Configuration del Fornitore di Wallet
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
    :class: longtable
    :widths: 20 60 20
    :header-rows: 1

    * - **Key**
      - **Value**
      - **Reference**
    * - ``iss``
      - OBBLIGATORIO. URL pubblico del Fornitore di Wallet.
      - `OID-FED`_.
    * - ``sub``
      - OBBLIGATORIO. URL pubblico del Fornitore di Wallet.
      - `OID-FED`_.
    * - ``iat``
      - OBBLIGATORIO. Data e ora di emissione in formato Unix Timestamp.
      - `OID-FED`_.
    * - ``exp``
      - OBBLIGATORIO. Data e ora di scadenza in formato Unix Timestamp.
      - `OID-FED`_.
    * - ``authority_hints``
      - OBBLIGATORIO. Array di URL (String) contenente l'elenco degli URL delle Entità superiori immediate, come il Trust Anchor o un Intermediario, che POSSONO emettere un Entity Statement relativo al Fornitore di Wallet.
      - `OID-FED`_.
    * - ``jwks``
      - OBBLIGATORIO. Un JSON Web Key Set (JWKS) che rappresenta la parte pubblica delle chiavi di firma dell'Entità di Federazione del Fornitore di Wallet. La chiave privata corrispondente è utilizzata dall'Entità per firmare la Entity Configuration su se stessa.
      - :rfc:`7517`, `OID-FED`_.
    * - ``metadata``
      - OBBLIGATORIO. Oggetto JSON che rappresenta i Tipi di Entità e i metadati per quei Tipi di Entità. Ogni nome membro dell'oggetto JSON è un Identificatore di Tipo di Entità, e ogni valore DEVE essere un oggetto JSON contenente parametri di metadati secondo lo schema di metadati del Tipo di Entità. DEVE contenere i metadati ``wallet_provider`` e OPZIONALMENTE i metadati ``federation_entity``.
      - `OID-FED`_.

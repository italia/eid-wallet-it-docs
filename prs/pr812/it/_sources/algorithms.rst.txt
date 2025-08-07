.. include:: ../common/common_definitions.rst


Algoritmi Crittografici
=======================

I seguenti algoritmi DEVONO essere supportati:

.. list-table::
  :class: longtable
  :widths: 20 20 20 20
  :header-rows: 1

  * - **Valore del parametro `alg` dell'algoritmo**
    - **Descrizione**
    - **Operazioni**
    - **Riferimenti**
  * - **ES256**
    - Elliptic Curve Digital Signature Algorithm (ECDSA) utilizzando una delle curve abilitate elencate nella sezione seguente e SHA256.
    - Firma
    - :rfc:`7518`, `[SOG-IS] <https://www.sogis.eu/documents/cc/crypto/SOGIS-Agreed-Cryptographic-Mechanisms-1.3.pdf>`_, `[ETSI] <https://www.etsi.org/deliver/etsi_ts/119300_119399/119312/01.04.03_60/ts_119312v010403p.pdf>`_ .
  * - **ES384**
    - Elliptic Curve Digital Signature Algorithm (ECDSA) utilizzando una delle curve abilitate elencate nella sezione seguente e SHA384.
    - Firma
    - :rfc:`7518`, `[SOG-IS] <https://www.sogis.eu/documents/cc/crypto/SOGIS-Agreed-Cryptographic-Mechanisms-1.3.pdf>`_, `[ETSI] <https://www.etsi.org/deliver/etsi_ts/119300_119399/119312/01.04.03_60/ts_119312v010403p.pdf>`_ .
  * - **ES512**
    - Elliptic Curve Digital Signature Algorithm (ECDSA) utilizzando una delle curve abilitate elencate nella sezione seguente e SHA521.
    - Firma
    - :rfc:`7518`, `[SOG-IS] <https://www.sogis.eu/documents/cc/crypto/SOGIS-Agreed-Cryptographic-Mechanisms-1.3.pdf>`_, `[ETSI] <https://www.etsi.org/deliver/etsi_ts/119300_119399/119312/01.04.03_60/ts_119312v010403p.pdf>`_ .
  * - **RSA-OAEP-256**
    - RSA Encryption Scheme con Optimal Asymmetric Encryption Padding (OAEP) utilizzando la funzione di hash SHA256 e la funzione di generazione MGF1 con SHA-256.
    - Cifratura delle Chiavi
    - :rfc:`7516`, :rfc:`7518`.
  * - **A128CBC-HS256**
    - Cifratura AES in modalità Cipher Block Chaining con valore Initial Vector a 128 bit, più autenticazione HMAC utilizzando SHA-256 e troncando HMAC a 128 bit.
    - Cifratura del Contenuto
    - :rfc:`7516`, :rfc:`7518`.
  * - **A256CBC-HS512**
    - Cifratura AES in modalità Cipher Block Chaining con valore Initial Vector a 256 bit, più autenticazione HMAC utilizzando SHA-512 e troncando HMAC a 256 bit.
    - Cifratura del Contenuto
    - :rfc:`7516`, :rfc:`7518`.

Le seguenti Curve Ellittiche DEVONO essere supportate per l'Elliptic Curve Digital Signature Algorithm:

.. list-table::
  :widths: 20 20 20
  :header-rows: 1

  * - **Famiglia di Curve**
    - **Nome Breve della Curva**
    - **Riferimenti**
  * - **Brainpool**
    - brainpoolP256r1, brainpoolP384r1, brainpoolP512r1.
    - :rfc:`5639`, `[ETSI] <https://www.etsi.org/deliver/etsi_ts/119300_119399/119312/01.04.03_60/ts_119312v010403p.pdf>`_ .
  * - **NIST**
    - P-256, P-384, P-521
    - `[ETSI] <https://www.etsi.org/deliver/etsi_ts/119300_119399/119312/01.04.03_60/ts_119312v010403p.pdf>`_, `[FIPS-186-4] <https://www.nist.gov/publications/digital-signature-standard-dss-2>`_, `[ISO/IEC 14888-3] <https://www.iso.org/standard/76382.html>`_.

Per le Credenziali emesse in formato mdoc, i seguenti algoritmi DEVONO essere supportati:

.. list-table::
  :class: longtable
  :widths: 20 20 20 20
  :header-rows: 1

  * - **Algoritmo**
    - **Descrizione**
    - **Operazioni**
    - **Riferimenti**
  * - **ECKA-DH**
    - Elliptic Curve Key Agreement Algorithm - Diffie-Hellman.
    - Accordo di chiave / Firma
    - BSI TR-03111.
  * - **HKDF**
    - HMAC-based Key Derivation Function.
    - Derivazione della chiave di sessione / Firma
    - :rfc:`5869`.
  * - **AES-256-GCM**
    - Advanced Encryption Standard con Galois/Counter Mode e una lunghezza della chiave di 256.
    - Cifratura della sessione / Firma
    - NIST SP 800-38D.

Si RACCOMANDA di supportare i seguenti algoritmi:

.. list-table::
  :class: longtable
  :widths: 20 20 20 20
  :header-rows: 1

  * - **Valore del parametro `alg` dell'algoritmo**
    - **Descrizione**
    - **Operazioni**
    - **Riferimenti**
  * - **PS256**
    - RSASSA (RSA with Signature Scheme Appendix) con padding PSS (Probabilistic Signature Scheme) utilizzando la funzione di hash SHA256 e la funzione di generazione della maschera MGF1 con SHA-256.
    - Firma
    - :rfc:`7518`, `[SOG-IS] <https://www.sogis.eu/documents/cc/crypto/SOGIS-Agreed-Cryptographic-Mechanisms-1.3.pdf>`_.
  * - **PS384**
    - RSASSA (RSA with Signature Scheme Appendix) con padding PSS (Probabilistic Signature Scheme) utilizzando la funzione di hash SHA384 e la funzione di generazione della maschera MGF1 con SHA-384.
    - Firma
    - :rfc:`7518`, `[SOG-IS] <https://www.sogis.eu/documents/cc/crypto/SOGIS-Agreed-Cryptographic-Mechanisms-1.3.pdf>`_.
  * - **PS512**
    - RSASSA (RSA with Signature Scheme Appendix) con padding PSS (Probabilistic Signature Scheme) utilizzando la funzione di hash SHA512 e la funzione di generazione della maschera MGF1 con SHA-512.
    - Firma
    - :rfc:`7518`, `[SOG-IS] <https://www.sogis.eu/documents/cc/crypto/SOGIS-Agreed-Cryptographic-Mechanisms-1.3.pdf>`_.
  * - **ECDH-ES**
    - Elliptic Curve Diffie-Hellman (ECDH) Ephemeral Static key agreement utilizzando Concat Key Derivation Function (KDF).
    - Cifratura delle Chiavi
    - :rfc:`7518`.
  * - **ECDH-ES+A128KW**
    - ECDH-ES utilizzando Concat KDF e content encryption key (CEK) avvolta utilizzando AES con una lunghezza della chiave di 128 (A128KW).
    - Cifratura delle Chiavi
    - :rfc:`7518`.
  * - **ECDH-ES+A256KW**
    - ECDH-ES utilizzando Concat KDF e content encryption key (CEK) avvolta utilizzando AES con una lunghezza della chiave di 256 (A256KW).
    - Cifratura delle Chiavi
    - :rfc:`7518`.

I seguenti algoritmi NON DEVONO essere supportati:

.. list-table::
  :class: longtable
  :widths: 20 20 20 20
  :header-rows: 1

  * - **Valore del parametro `alg` dell'algoritmo**
    - **Descrizione**
    - **Operazioni**
    - **Riferimenti**
  * - **none**
    - -
    - Firma
    - :rfc:`7518`.
  * - **RSA_1_5**
    - RSAES con schema di padding PKCS1-v1_5. L'uso di questo algoritmo generalmente non è raccomandato.
    - Cifratura delle Chiavi
    - :rfc:`7516`, `[Security Vulnerability] <https://en.wikipedia.org/wiki/Adaptive_chosen-ciphertext_attack>`_, `[SOG-IS] <https://www.sogis.eu/documents/cc/crypto/SOGIS-Agreed-Cryptographic-Mechanisms-1.3.pdf>`_.
  * - **RSA-OAEP**
    - RSA Encryption Scheme con Optimal Asymmetric Encryption Padding (OAEP) utilizzando parametri predefiniti.
    - Cifratura delle Chiavi
    - :rfc:`7518`, `[SOG-IS] <https://www.sogis.eu/documents/cc/crypto/SOGIS-Agreed-Cryptographic-Mechanisms-1.3.pdf>`_.
  * - **HS256**
    - HMAC utilizzando SHA256.
    - Firma
    - :rfc:`7518`.
  * - **HS384**
    - HMAC utilizzando SHA384.
    - Firma
    - :rfc:`7518`.
  * - **HS512**
    - HMAC utilizzando SHA512
    - Firma
    - :rfc:`7518`.

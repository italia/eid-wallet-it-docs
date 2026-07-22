.. include:: ../common/common_definitions.rst


Algoritmi Crittografici
=======================
Questa sezione elenca gli algoritmi crittografici utilizzati nell'ecosistema IT Wallet. Gli identificatori degli algoritmi sono espressi principalmente come valori JOSE ``alg``; quando viene utilizzato COSE, i corrispondenti algoritmi COSE sono indicati esplicitamente (ad esempio, ESP256 rispetto a ES256).

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
    - Elliptic Curve Digital Signature Algorithm (ECDSA) utilizzando P-256 e SHA-256.
    - Firma
    - :rfc:`7518`.
  * - **ES384**
    - ECDSA utilizzando P-384 e SHA-384.
    - Firma
    - :rfc:`7518`.
  * - **ES512**
    - ECDSA utilizzando P-521 e SHA-512.
    - Firma
    - :rfc:`7518`.
  * - **ESP256** (COSE, ``-9``)
    - ECDSA utilizzando P-256 e SHA-256.
    - Firma
    - :rfc:`9864`.
  * - **ESP384** (COSE, ``-51``)
    - ECDSA utilizzando P-384 e SHA-384.
    - Firma
    - :rfc:`9864`.
  * - **ESP512** (COSE, ``-52``)
    - ECDSA utilizzando P-521 e SHA-512.
    - Firma
    - :rfc:`9864`.
  * - **RSA-OAEP-256**
    - RSA Encryption Scheme con Optimal Asymmetric Encryption Padding (OAEP) utilizzando la funzione di hash SHA-256 e la funzione di generazione MGF1 con SHA-256.
    - Cifratura delle Chiavi
    - :rfc:`7516`, :rfc:`7518`.
  * - **ECDH-ES**
    - Elliptic Curve Diffie-Hellman (ECDH) Ephemeral-Static key agreement.
    - Accordo di chiave
    - :rfc:`7516`, :rfc:`7518`.
  * - **A128CBC-HS256**
    - Cifratura AES in modalità Cipher Block Chaining con valore Initial Vector a 128 bit, più autenticazione HMAC utilizzando SHA-256 e troncando HMAC a 128 bit.
    - Cifratura del Contenuto
    - :rfc:`7516`, :rfc:`7518`.
  * - **A256CBC-HS512**
    - Cifratura AES in modalità Cipher Block Chaining con valore Initial Vector a 256 bit, più autenticazione HMAC utilizzando SHA-512 e troncando HMAC a 256 bit.
    - Cifratura del Contenuto
    - :rfc:`7516`, :rfc:`7518`.
  * - **A128GCM**
    - Cifratura AES con Galois/Counter Mode e una lunghezza della chiave di 128.
    - Cifratura del Contenuto
    - :rfc:`7516`, :rfc:`7518`.
  * - **A256GCM**
    - Cifratura AES con Galois/Counter Mode e una lunghezza della chiave di 256.
    - Cifratura del Contenuto
    - :rfc:`7516`, :rfc:`7518`.

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
    - Accordo di chiave
    - BSI TR-03111.
  * - **HKDF**
    - HMAC-based Key Derivation Function.
    - Derivazione della chiave di sessione
    - :rfc:`5869`.
  * - **AES-256-GCM**
    - Advanced Encryption Standard con Galois/Counter Mode e una lunghezza della chiave di 256.
    - Cifratura della sessione
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
    - RSASSA (RSA with Signature Scheme Appendix) con padding PSS (Probabilistic Signature Scheme) utilizzando la funzione di hash SHA-256 e la funzione di generazione della maschera MGF1 con SHA-256.
    - Firma
    - :rfc:`7518`.
  * - **PS384**
    - RSASSA con padding PSS utilizzando la funzione di hash SHA-384 e la funzione di generazione della maschera MGF1 con SHA-384.
    - Firma
    - :rfc:`7518`.
  * - **PS512**
    - RSASSA con padding PSS utilizzando la funzione di hash SHA-512 e la funzione di generazione della maschera MGF1 con SHA-512.
    - Firma
    - :rfc:`7518`.
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
    - HMAC utilizzando SHA-256.
    - Firma
    - :rfc:`7518`.
  * - **HS384**
    - HMAC utilizzando SHA-384.
    - Firma
    - :rfc:`7518`.
  * - **HS512**
    - HMAC utilizzando SHA-512
    - Firma
    - :rfc:`7518`.



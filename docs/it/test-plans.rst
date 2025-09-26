.. include:: ../common/common_definitions.rst


Test Plans
==========

Lo scopo dei piani di test è supportare implementatori, auditor e ambienti di test di conformità nella validazione del comportamento delle Soluzioni Wallet, delle Relying Party e degli Provider di Credenziali in vari scenari operativi e di sicurezza.

Tutti i casi di test sono derivati da regole normative definite nelle specifiche sopra indicate, senza presupposti o estensioni.

.. note::
  Si prega di notare che la matrice dei piani di test potrebbe essere soggetta a modifiche future.

Struttura della Matrice di Test
-------------------------------

Ogni test è identificato da un identificatore univoco (es. WS-001) e categorizzato utilizzando i domini funzionali definiti di seguito.

- **Discovery**
- **Security**
- **Privacy**
- **Authorization**
- **Authentication**
- **User Experience**
- **Credential Issuance**
- **Credential Presentation**
- **Credential Status**
- **Backup & Restore**

Per ogni caso di test, la tabella specifica:

- **Test Case ID**: un identificatore univoco.
- **Purpose**: l'area funzionale coperta dal test.
- **Description**: il requisito che viene testato, sempre basato su un MUST normativo della specifica.
- **Expected Result**: il risultato atteso quando la soluzione è implementata correttamente.


.. toctree::
  :caption: Piani di Test per Ambito
  :maxdepth: 3

  test-plans-signature.rst
  test-plans-trust.rst
  test-plans-wallet.rst
  test-plans-credential-issuer.rst
  test-plans-remote-presentation.rst
  test-plans-proximity-presentation.rst

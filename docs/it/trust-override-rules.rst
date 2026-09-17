.. include:: ../common/common_definitions.rst
.. Included via trust-evaluation.rst at title level '-' (level 1).

Authorization Decision and Override Rules
------------------------------------------

La Authorization Decision può essere ``AUTHORIZED`` oppure ``NOT_AUTHORIZED``.
Le condizioni che determinano questo esito dipendono dalla specifica procedura di Authorization Validation seguita.

- Nel caso in cui la Wallet Unit segua il percorso di valutazione :ref:`trust-evaluation:EUDIW Authorization`, l'esito è:

    - durante la **Presentazione di Attestati**, ``AUTHORIZED`` se il processo termina con ``CERTIFICATE_VALID`` AND ``EDP_SATISFIED`` AND ``VERIFICATION_PASSED``;
    - durante l'**Emissione di Attestati**, ``AUTHORIZED`` se il processo termina con ``CERTIFICATE_VALID`` AND ``VERIFICATION_PASSED``;
    - ``NOT_AUTHORIZED`` altrimenti.

- Nel caso in cui la Wallet Unit segua il percorso di valutazione Nazionale :ref:`trust-evaluation:Authorization`, l'esito è:

    - ``AUTHORIZED`` se il processo termina con ``TRUST_MARK_VALID`` AND ``ENTITLEMENT_VALID`` AND ``VERIFICATION_PASSED``; oppure,
    - ``NOT_AUTHORIZED`` altrimenti.

**Principi di Override**

Una decisione ``NOT_AUTHORIZED`` può essere *non-overridable* (la Wallet Unit blocca l'interazione) oppure *overridable* (la Wallet Unit presenta l'esito negativo e l'Utente può scegliere di proseguire).

- Durante la fase di **Emissione di Attestati**, tutti gli esiti negativi di verifica DEVONO essere *non-overridable*: la Wallet Unit NON DEVE consentire all'Utente di interagire con i fornitori la cui registrazione non può essere confermata.

- Durante la fase di **Presentazione**, tutti gli esiti negativi di verifica DEVONO essere *non-overridable*, salvo i seguenti casi:

    - **Overasking [EUDIW]**.
      Quando il processo termina con ``CERTIFICATE_VALID`` AND ``OVERASKING_DETECTED``, ossia la Authorization Artifact Validation ha avuto esito positivo, ma lo Scope Comparison rileva che la Relying Party richiede più del proprio scope registrato.
    - **Valutazione negativa dell'Embedded Disclosure Policy [EUDIW]**.
      Quando il processo termina con ``CERTIFICATE_VALID`` AND ``EDP_NOT_SATISFIED``, ossia la Authorization Artifact Validation ha avuto esito positivo ma l'Embedded Disclosure Policy non consentirebbe la presentazione alla Relying Party.
    - **WRPRC mancante o non valido [EUDIW]**.
      Quando il processo termina con ``CERTIFICATE_INVALID`` durante la Presentazione di Attestati, ossia il Wallet-Relying Party Registration Certificate è assente, malformato, non autentico o scaduto.
      La Wallet Unit DEVE avvisare l'Utente e NON DEVE interrogare il Register, come specificato in :ref:`trust-evaluation:EUDIW Authorization`.
      Se l'Utente possa comunque approvare dipende dalla policy del Fornitore di Wallet.
    - **Overasking [National]**.
      Quando il processo termina con ``TRUST_MARK_VALID`` AND ``OVERASKING_DETECTED``, ossia la :ref:`trust-evaluation:Trust Mark Validation` ha avuto esito positivo, ma il :ref:`trust-evaluation:Overasking Check` rileva che la Relying Party richiede più del proprio scope registrato.

Tutti gli altri fallimenti di presentazione, inclusi i fallimenti di binding o i fallimenti di binding dell'intermediario, NON DEVONO essere overridable in quanto indicano un problema di integrità piuttosto che una scelta rivolta all'Utente.

In caso di fallimenti non-overridable, la Wallet Unit DEVE informare chiaramente l'Utente sull'esito negativo.
Le informazioni rilevanti per l'Utente relative agli esiti overridable DEVONO essere presentate come avvisi, e l'approvazione dell'Utente DEVE essere un passo distinto rispetto alla Authorization Decision finale.

La *Scope Comparison Procedure* in :ref:`trust-evaluation:Authorization Validation` DEVE essere eseguita durante ogni Presentazione di Attestati rispetto al Wallet-Relying Party Registration Certificate incluso nella richiesta, come specificato in :ref:`trust-evaluation:EUDIW Authorization`.

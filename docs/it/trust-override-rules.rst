.. include:: ../common/common_definitions.rst
.. Included via trust-evaluation.rst at title level '-' (level 1).

Authorization Decision and Override Rules
------------------------------------------

La Authorization Decision può essere ``AUTHORIZED`` oppure ``NOT_AUTHORIZED``.
Le condizioni che determinano questo esito dipendono dalla specifica procedura di Authorization Validation seguita.

- Nel caso in cui la Wallet Unit segua il percorso di valutazione :ref:`trust-evaluation:EUDIW Authorization`, l'esito è:

    - ``AUTHORIZED`` se il processo termina con ``REGISTER_VALID`` OPPURE ``CERTIFICATE_VALID`` E ``EDP_SATISFIED`` E ``VERIFICATION_PASSED``; oppure
    - ``NOT_AUTHORIZED`` in caso contrario.

- Nel caso in cui la Wallet Unit segua il percorso di valutazione :ref:`trust-evaluation:Authorization` del National Trust Framework, l'esito è:

    - ``AUTHORIZED`` se il processo termina con ``TRUST_MARK_VALID`` E ``ENTITLEMENT_VALID`` E ``VERIFICATION_PASSED``; oppure
    - ``NOT_AUTHORIZED`` in caso contrario.

**Override Principles**

Una decisione ``NOT_AUTHORIZED`` può essere *non overridable* (la Wallet Unit blocca l'interazione) oppure *overridable* (la Wallet Unit presenta l'esito negativo e l'Utente può scegliere di procedere).

- Durante la fase di **Credential Issuance**, tutti gli esiti negativi di verifica DEVONO essere *non overridable*: la Wallet Unit NON DEVE consentire all'Utente di interagire con provider la cui registrazione non può essere confermata.

- Durante la fase di **Presentation**, tutti gli esiti negativi di verifica DEVONO essere *non overridable*, ad eccezione dei seguenti casi:

    - **Overasking [EUDIW]**.
      Quando il processo termina con ``REGISTER_VALID`` OPPURE ``CERTIFICATE_VALID`` E ``OVERASKING_DETECTED``, cioè l'Authorization Artifact Validation ha avuto esito positivo, ma la Scope Comparison rileva che la Relying Party richiede più del proprio ambito registrato.
    - **Negative Embedded Disclosure Policy evaluation [EUDIW]**.
      Quando il processo termina con ``REGISTER_VALID`` OPPURE ``CERTIFICATE_VALID`` E ``EDP_NOT_SATISFIED``, cioè l'Authorization Artifact Validation ha avuto esito positivo ma l'Embedded Disclosure Policy non consentirebbe la presentazione alla Relying Party.
    - **Overasking [National]**.
      Quando il processo termina con ``TRUST_MARK_VALID`` E ``OVERASKING_DETECTED``, cioè la :ref:`trust-evaluation:Trust Mark Validation` ha avuto esito positivo, ma la :ref:`trust-evaluation:Overasking Check` rileva che la Relying Party richiede più del proprio ambito registrato.

Tutti gli altri fallimenti di presentazione, inclusi i fallimenti di binding o di intermediary binding, NON DEVONO essere overridable in quanto indicano un problema di integrità piuttosto che una scelta rivolta all'Utente.

In caso di fallimenti non overridable, la Wallet Unit DEVE informare chiaramente l'Utente sull'esito negativo.
Le informazioni rilevanti per l'Utente relative agli esiti overridable DEVONO essere presentate come avvisi e l'approvazione dell'Utente DEVE essere un passo distinto dalla Authorization Decision finale.

.. note::
    **User opt-in**.
    La *Scope Comparison Procedure* in :ref:`trust-evaluation:Authorization Validation` viene eseguita solo se l'Utente ha abilitato la verifica della registrazione.
    I meccanismi di override definiscono cosa accade quando la procedura produce un esito negativo.

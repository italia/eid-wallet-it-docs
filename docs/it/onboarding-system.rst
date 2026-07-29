.. include:: ../common/common_definitions.rst
.. include:: ../common/symbols.rst
.. Included via index.rst at title level '=' (document title).

Onboarding System and Lifecycle Management
==========================================

.. warning::
   Questa sezione è un work in progress ed è pubblicata in forma di bozza.
   La struttura generale è definita, mentre diverse parti devono ancora essere scritte e il contenuto può cambiare.
   Le sottosezioni contrassegnate come bozza di seguito contengono solo una breve descrizione di ciò che forniranno.

Il Sistema di Onboarding è l'insieme di componenti, servizi, processi e procedure che ammette un'Entity nell'ecosistema IT-Wallet, pubblica le informazioni di cui gli altri partecipanti hanno bisogno per riconoscerla e gestisce ciò che accade dopo la registrazione.

Il Sistema di Onboarding copre:

  - **Entities**: le Wallet-Relying Party, i Wallet Provider e le Authentic Sources, dalla loro registrazione fino alla cancellazione di quest'ultima. Un'Entity è registrata, aggiornata, eventualmente sospesa e riattivata, e infine rimossa.
  - **Trust Artifacts**: i certificati, i registration certificate e i federation statement emessi come risultato di una registrazione, e sempre derivati da essa.
  - **Credential types**: le definizioni versionate pubblicate nel Digital Credentials Catalog, con i claim, gli schema e le Authentic Sources da cui dipendono. Un Credential type è registrato, attivato, versionato e disattivato.
  - **Registries and catalogs**: i registri nazionali scritti dal sistema e i cataloghi europei e le List of Trusted Entities verso cui il sistema si allinea o notifica.

Per ciascuno di questi, il Sistema di Onboarding copre l'intero ciclo di vita e non solo il primo onboarding.

Tutti gli eventi relativi alle Entities e ai Credential types producono effetti sui Trust Artifacts e sui registri, e tali effetti sono descritti in questa Sezione, insieme agli eventi che li causano.

Come definito in :ref:`infrastructure-trust:Infrastructure of Trust`, due Trust Framework coesistono nell'IT-Wallet, EUDIW e National Trust Framework, e il Sistema di Onboarding consente alle Entities registrate di operare su entrambi.
Il National Trust Framework è il livello di registrazione per tutte le Entities dell'ecosistema e fornisce i meccanismi che i componenti del Sistema di Onboarding usano per autenticarsi reciprocamente.

Le strutture dati dei registri sono definite in :ref:`registry:Infrastruttura del Registro`, i profili dei Trust Artifacts in :ref:`infrastructure-trust:Infrastructure of Trust`, i meccanismi tecnici che pubblicano lo stato di un certificato in :ref:`infrastructure-trust:Revocation Mechanisms`, e il modo in cui gli artifact sono consumati a runtime in :ref:`trust-evaluation:Trust Evaluation Process`.

La sezione è organizzata in quattro parti.
L'**Overview** presenta gli attori, i componenti e il modo in cui vengono usati i due Trust Framework.
Il **Registration Model** fornisce la vista statica, ossia ciò che ciascun ruolo fornisce e ciò che ottiene.
Gli **Onboarding Processes** forniscono la vista dinamica, ossia come ciascuna procedura viene eseguita.
Il **Lifecycle Management** presenta gli stati, gli eventi e i loro effetti sui registri e sui Trust Artifacts.

.. include:: onboarding-overview.rst
.. include:: onboarding-registration-model.rst
.. include:: onboarding-processes.rst
.. include:: onboarding-processes-entities.rst
.. include:: onboarding-processes-artifacts.rst
.. include:: onboarding-processes-credentials.rst
.. include:: onboarding-lifecycle.rst

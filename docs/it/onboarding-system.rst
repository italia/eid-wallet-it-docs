.. include:: ../common/common_definitions.rst
.. include:: ../common/symbols.rst
.. Included via index.rst at title level '=' (document title).

Onboarding System and Lifecycle Management
==========================================

.. warning::
   Questa sezione è un lavoro in corso ed è pubblicata in forma di bozza.
   La struttura generale è definita, mentre diverse parti sono ancora da scrivere e il contenuto può cambiare.
   Le sottosezioni contrassegnate come bozza di seguito contengono solo una breve descrizione di ciò che forniranno.

L'Onboarding System è l'insieme di componenti, servizi, processi e procedure che ammette un'Entità nell'ecosistema IT-Wallet, pubblica le informazioni di cui gli altri partecipanti hanno bisogno per riconoscerla e gestisce ciò che avviene dopo la registrazione.

L'Onboarding System copre:

  - **Entità**: le Wallet-Relying Party, i Fornitori di Wallet e le Fonti Autentiche, dalla loro registrazione fino alla cancellazione di tale registrazione. Un'Entità è registrata, aggiornata, eventualmente sospesa e riattivata, e infine rimossa.
  - **Trust Artifact**: i certificati, i certificati di registrazione e i federation statement che sono emessi come risultato di una registrazione, e che da essa sono sempre derivati.
  - **Tipi di Attestato**: le definizioni versionate pubblicate nel Catalogo degli Attestati Elettronici, con i claim, gli schemi e le Fonti Autentiche da cui dipendono. Un tipo di Attestato è registrato, attivato, versionato e disattivato.
  - **Registri e cataloghi**: i registri Nazionali che il sistema scrive, e i cataloghi europei e le Lists of Trusted Entities verso i quali il sistema si allinea o notifica.

Per ciascuno di questi, l'Onboarding System copre l'intero ciclo di vita e non solo il primo onboarding.

Tutti gli eventi relativi alle Entità e ai tipi di Attestato producono effetti sui Trust Artifact e sui registri, e tali effetti sono descritti in questa Sezione, insieme agli eventi che li causano.

Come definito in :ref:`infrastructure-trust:Infrastructure of Trust`, nell'IT-Wallet coesistono due Trust Framework, EUDIW e Trust Framework Nazionale, e l'Onboarding System rende le Entità registrate in grado di operare su entrambi.

Il Trust Framework Nazionale è il livello di registrazione per tutte le Entità dell'ecosistema e fornisce i meccanismi che i componenti dell'Onboarding System utilizzano per autenticarsi reciprocamente.

Le strutture dati dei registri sono definite in :ref:`registry:Registry Infrastructure`, i profili dei Trust Artifact in :ref:`infrastructure-trust:Infrastructure of Trust`, i meccanismi tecnici che pubblicano lo stato di un certificato in :ref:`infrastructure-trust:Revocation Mechanisms`, e il modo in cui gli artifact sono consumati a runtime in :ref:`trust-evaluation:Trust Evaluation Process`.

La sezione è organizzata in cinque parti.
La **Overview** presenta gli attori, i componenti e il modo in cui i due Trust Framework sono utilizzati.
Il **Registration Model** fornisce la vista statica, ossia ciò che ciascun ruolo fornisce e ciò che ottiene.
Gli **Onboarding Processes** forniscono la vista dinamica, ossia come ciascuna procedura è eseguita.
La **Notification and Publication** fornisce la procedura che porta le categorie notificate nelle Lists of Trusted Entities, di cui l'Onboarding System gestisce la raccolta dei dati.
Il **Lifecycle Management** presenta gli stati, gli eventi e i loro effetti sui registri e sui Trust Artifact.

.. include:: onboarding-overview.rst
.. include:: onboarding-registration-model.rst
.. include:: onboarding-processes.rst
.. include:: onboarding-processes-entities.rst
.. include:: onboarding-processes-artifacts.rst
.. include:: onboarding-processes-credentials.rst
.. include:: onboarding-notification.rst
.. include:: onboarding-lifecycle.rst

.. include:: ../common/common_definitions.rst


Eliminazione degli Attributi dell'Utente
========================================

Questa funzionalità dell'Istanza del Wallet consente agli Utenti di ottenere un elenco di tutte le Relying Party a cui sono stati presentati Attestati Elettronici. Gli Utenti possono quindi richiedere l'eliminazione degli attributi di uno o più Attestati Elettronici presentati a una Relying Party di loro scelta. La richiesta usa l'interfaccia comune di `EUDI-TS 7`_. Di seguito è presentato il flusso di alto livello (:ref:`WP_115 <user-attribute-deletion-testcases>`).

.. plantuml:: plantuml/user-deletion-attribute-flow.puml
    :width: 99%
    :alt: La figura illustra il Processo di Eliminazione degli Attributi dell'Utente.
    :caption: Processo di Eliminazione degli Attributi dell'Utente.

**Passo 1:** L'Utente richiede l'eliminazione degli attributi invocando la funzione di eliminazione degli attributi dell'Istanza del Wallet.

**Passo 2:** L'Istanza del Wallet raccoglie tutti i dati delle transazioni e mostra all'Utente l'elenco delle Relying Party con cui ha avuto interazioni durante il ciclo di vita dell'Istanza del Wallet e che sono in possesso degli attributi dell'Utente (:ref:`WP_115a <user-attribute-deletion-testcases>`).

**Passo 3:** L'Utente seleziona la Relying Party di destinazione per l'eliminazione degli attributi.

**Passi 4 - 5:** L'Istanza del Wallet determina i canali di contatto registrati per quella Relying Party (:ref:`WP_116 <user-attribute-deletion-testcases>`).

Nel National Trust Framework, il contatto è il ``support_uri`` del Trust Mark di registrazione, come definito in :ref:`infrastructure-trust:Trust Mark Types and Schema`.

Nel EUDIW Trust Framework, i contatti sono i valori di helpdesk e supporto nel Subject Alternative Name del Wallet-Relying Party Access Certificate, come specificato in `EUDI-TS 7`_.

**Passo 6:** L'Istanza del Wallet registra l'avvio della richiesta di cancellazione dei dati come definito in :ref:`wallet-instance-dashboard:Dashboard dell’Istanza del Wallet e Registrazione delle Transazioni`. Questi log MUST includere almeno (:ref:`WP_117a <user-attribute-deletion-testcases>`):

  * la data e l'ora della richiesta,
  * la Relying Party a cui è stata fatta la richiesta,
  * gli attributi di cui è stata richiesta la rimozione.

**Passi 7 - 8:** L'Istanza del Wallet MUST mostrare i contatti che la piattaforma può invocare, oppure applicare una preferenza dell'Utente configurata in precedenza. L'Istanza del Wallet MUST invocare l'applicazione esterna che corrisponde al contatto selezionato (:ref:`WP_117 <user-attribute-deletion-testcases>`, :ref:`WP_118 <user-attribute-deletion-testcases>`).

- L'Istanza del Wallet MUST aprire un URL HTTPS in un browser esterno.
- L'Istanza del Wallet MUST aprire un indirizzo email in un client di posta esterno, quando un client di posta è disponibile, come URI ``mailto``. Il ``subject`` MUST indicare che l'Utente richiede la cancellazione dei dati personali ai sensi dell'Articolo 17 del Regolamento (UE) 2016/679 precedentemente forniti tramite l'Istanza del Wallet. Il ``body`` SHOULD identificare gli attributi di cui è richiesta la cancellazione, oppure indicare che è richiesta la cancellazione di tutti i dati personali precedentemente forniti tramite l'Istanza del Wallet.
- L'Istanza del Wallet MUST aprire un numero di telefono nell'applicazione telefonica, quando un'applicazione telefonica è disponibile.

**Passo 9:** Prima di eliminare gli attributi, la Relying Party MUST autenticare l'Utente, o la richiesta, con un meccanismo di autenticazione di sua scelta. La Relying Party SHOULD usare le funzionalità di autenticazione e di firma dell'Istanza del Wallet dell'Utente. Dopo l'autenticazione dell'Utente, la Relying Party MUST eliminare gli attributi degli Attestati Elettronici individuati con l'identity matching, come specificato in :ref:`identity-matching`.

.. note::
  Il meccanismo specifico di autenticazione è lasciato alla Relying Party. Se l'Utente non si autentica tramite l'Istanza del Wallet, l'identity matching e l'identity reconciliation MAY usare uno schema nazionale di autenticazione preesistente, ove possibile, come specificato in :ref:`identity-matching`. Dopo l'autenticazione dell'Utente, la Relying Party MAY chiedere all'Utente di confermare la cancellazione.

**Passo 10:** L'Istanza del Wallet MUST informare l'Utente che la richiesta di cancellazione dei dati è stata avviata (:ref:`WP_119 <user-attribute-deletion-testcases>`, :ref:`WP_119a <user-attribute-deletion-testcases>`). Il completamento della cancellazione da parte della Relying Party è fuori da questo protocollo, come specificato in `EUDI-TS 7`_.

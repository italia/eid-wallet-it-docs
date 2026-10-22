.. include:: ../common/common_definitions.rst
.. Incluso tramite normative-ref.rst al livello di titolo '-' (livello 1).


Risorse Ufficiali
-----------------

Questa sezione contiene asset, risorse e artefatti che non possono essere distribuiti sotto forma di documentazione tecnica ma devono essere forniti nel loro formato digitale nativo. Questi includono file sorgente in formati come SVG, immagini raster, repository di codice, file di configurazione e altri asset digitali essenziali per la progettazione e l'implementazione delle Soluzioni Tecniche del Sistema IT-Wallet.

Qualsiasi risorsa tecnica aggiuntiva, repository e documentazione aggiuntiva saranno rese disponibili in questa sezione nelle versioni successive delle presenti specifiche tecniche.

Sito Ufficiale
^^^^^^^^^^^^^^

Il sito ufficiale del Sistema IT-Wallet è disponibile all'indirizzo seguente:

- **Sito Ufficiale IT-Wallet**: `https://www.wallet.gov.it <https://www.wallet.gov.it>`_

Risorse Grafiche
^^^^^^^^^^^^^^^^

Di seguito sono elencate le risorse grafiche ufficiali. Le risorse sono disponibili per il download nella cartella `official_resources/ <https://github.com/italia/eid-wallet-it-docs/tree/versione-corrente/official_resources>`_ di questo repository.

- **Logo IT-Wallet**: Logo ufficiale del Sistema IT-Wallet (formato SVG). `Scarica il logo <_static/IT-Wallet-Logo/IT-Wallet-Logo-Primary-BlueItalia.svg>`_.
- **Pittogramma IT-Wallet**: Pittogramma ufficiale del Sistema IT-Wallet. `Scarica il pittogramma <_static/IT-Wallet-Symbol/IT-Wallet-Symbol-Primary-BlueItalia.svg>`_.
- **IT-Wallet ID**: Elemento grafico ufficiale per l’identificazione univoca degli Attestati di identificazione personale (IT-Wallet ID / PID) tra tutte le Soluzioni Wallet. `Scarica IT-Wallet ID <_static/IT-Wallet-ID/IT-Wallet-ID-Primary-BlueItalia.svg>`_.
- **Trust Mark**: Elemento grafico ufficiale per l'attestazione dell'appartenenza al Sistema IT-Wallet. `Scarica Trust Mark <_static/IT-Wallet-Trust-Mark/ITA/Trust-Mark-ITA-Blue-Primary.svg>`_. Consulta la sezione :ref:`brand-identity:Trust Mark`.
- **Authentication Button**: Pulsante ufficiale per l'autenticazione tramite IT-Wallet. `Scarica Authentication Button <_static/IT-Wallet-Authentication-Button/ITA/IT-Wallet-Authentication-Button-ITA-Standard-Default.svg>`_.
- **Template di pagina**: Modelli delle pagine appartenenti al flusso di Autenticazione. Le pagine sono Discovery page, Selection page, QR code page, Thank you page ed Error page. Consulta `Pages-templates/ <https://github.com/italia/eid-wallet-it-docs/tree/versione-corrente/official_resources/Pages-templates>`_.
- **Icone e pittogrammi**: Icone e pittogrammi utili per l'implementazione del flusso di Autenticazione. `Scarica OK State <_static/Icons-and-pictograms/OK_State.svg>`_. `Scarica KO state <_static/Icons-and-pictograms/KO_State.svg>`_. `Scarica order <_static/Icons-and-pictograms/Order.svg>`_.

Componenti HTML
^^^^^^^^^^^^^^^

I seguenti componenti HTML ufficiali sono disponibili nella cartella `official_resources/ <https://github.com/italia/eid-wallet-it-docs/tree/versione-corrente/official_resources>`_ di questo repository.

- **Authentication Button Component**: Componente HTML/CSS ufficiale per l'autenticazione tramite IT-Wallet. Il componente si basa sulla libreria `Bootstrap Italia <https://italia.github.io/bootstrap-italia/docs/componenti/buttons/>`__. `Vedi il componente <https://github.com/italia/eid-wallet-it-docs/tree/versione-corrente/official_resources/authentication-button>`__. `Demo live <_static/authentication-button/authentication-button.html>`__.
- **Discovery Page**: Template HTML/CSS/JS ufficiale e autoconsistente per la selezione del metodo di autenticazione (identità digitale). Il template si basa sulla libreria `Bootstrap Italia <https://italia.github.io/bootstrap-italia/>`__. `Vedi il template <https://github.com/italia/eid-wallet-it-docs/tree/versione-corrente/official_resources/discovery-page>`__. `Demo live <_static/discovery-page/disco.html>`__.
- **IT-Wallet Selection Page**: Template HTML/CSS/JS ufficiale e autoconsistente per la selezione del portafoglio digitale (wallet) con cui proseguire l'autenticazione. Il template si basa sulla libreria `Bootstrap Italia <https://italia.github.io/bootstrap-italia/>`__. `Vedi il template <https://github.com/italia/eid-wallet-it-docs/tree/versione-corrente/official_resources/it-wallet-selection-page>`__. `Demo live <_static/it-wallet-selection-page/it-wallet.html>`__.
- **IT-Wallet Presentation QR Code Page**: Template HTML/CSS/JS ufficiale e autoconsistente per la pagina QR del flusso remoto di presentazione OpenID4VP (**Cross Device**). Il template include un payload dimostrativo di Authorization Request. Il payload usa un custom URL scheme (``openid4vp://`` o ``haip-vp://``, Request Object by reference, come descritto in :ref:`remote-flow:Flusso Remoto`). Le card della Selection Page puntano a questa demo. Il template si basa sulla libreria `Bootstrap Italia <https://italia.github.io/bootstrap-italia/>`__. `Vedi il template <https://github.com/italia/eid-wallet-it-docs/tree/versione-corrente/official_resources/it-wallet-presentation-qr-code-page>`__. `Demo live <_static/it-wallet-presentation-qr-code-page/qr-code-page.html>`__.

Gli asset statici comuni alle tre pagine sono centralizzati in `official_resources/shared-ui/`. Gli asset comprendono Bootstrap Italia, CSS, JavaScript condivisi, sprite SVG, favicon e loghi. Le pagine li referenziano con percorsi relativi ``../shared-ui/...``.

Brand Manual
^^^^^^^^^^^^

Il Brand Manual contenente le indicazioni complete per l'utilizzo delle risorse grafiche e dell'identità visiva del Sistema IT-Wallet sarà prossimamente disponibile sul :ref:`sito ufficiale <official-resources:Sito Ufficiale>`.


Flusso di Recupero dei Wallet Metadata
======================================

Alcuni flussi relativi agli Attestati Elettronici richiedono il recupero delle informazioni del Wallet prima di interagire con il Wallet stesso. Ad esempio, per abilitare l'opzione di selezione della Soluzione Wallet durante un flusso di Credential Offer o un flusso di presentazione. 
A tal fine, le terze parti che offrono il Credential Offer (ad esempio, Authentic Source, Registro, Catalogo) e le Relying Party consultano il Registro del Sistema IT-Wallet, in particolare il Registro di Federazione, tramite gli endpoint del Trust Anchor.

In primo luogo, con l'Immediate Subordinate Listing endpoint ottengono la lista di tutti i subordinati del Trust Anchor identificati dal loro ``entity_id``. Per ottenere solo l'``entity_id`` relativi ai Wallet Provider, è POSSIBILE utilizzare il parametro di query ``entity_type`` con valore  ``wallet_provider``. 
Se il Trust Anchor non supporta questa funzione, DEVE utilizzare il codice di stato HTTP 400 e il Content Type  ``application/json``, con il codice di errore ``unsupported_parameter``.

Quindi, dato l'``entity_id``, per ciascun Wallet Provider recuperano la corrispondente configurazione utilizzando l'endpoint dei metadati della federazione (GET .well-known/openid-federation) 
e ottengono i metadati della Wallet Solution (vedere :ref:`wallet-solution-metadata:Metadati della Soluzioen Wallet`). Maggiori dettagli sull'uso degli endpoint del Trust Anchor sono forniti in :ref:`trust-infrastructure:L'Infrastruttura di Trust`.

All'interno dei metadati, le terze parti che supportano il Credential Offer e le Relying Party recuperano le informazioni necessarie per la Selection Page, ovvero il logo e il nome completo delle Soluzioni Wallet.
Maggiori dettagli sulla progettazione della Selection Page sono disponibili in :ref:`functionalities:Design dell'Esperienza Utente`.


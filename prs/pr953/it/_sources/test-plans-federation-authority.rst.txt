.. include:: ../common/common_definitions.rst


Matrice di Test per le Autorità di Federazione
----------------------------------------------

Questa sezione definisce i casi di test per le Autorità di Federazione (Trust Anchor e Intermediari) responsabili del funzionamento dell'Infrastruttura di Trust come descritto in :ref:`trust-infrastructure:L'Infrastruttura di Trust`. I test si concentrano sulla correttezza e conformità di:

- Entity Configuration (``.well-known/openid-federation``)
- Subordinate Statement restituiti da ``/fetch``
- Endpoint del registro di federazione (``/list``, ``/fetch``, ``/trust_mark_status``, ``/historical-jwks``)

Tutte le validazioni sono allineate con (`OID-FED`_).


.. list-table::
  :class: longtable
  :widths: 15 15 35 35
  :header-rows: 1

  * - Test Case ID
    - Purpose
    - Description
    - Expected Result
  * - FA_001
    - Discovery, Interoperability
    - Media type dell'Entity Configuration
    - ``GET /.well-known/openid-federation`` restituisce HTTP 200 con ``Content-Type: application/entity-statement+jwt``.
  * - FA_002
    - Security
    - Integrità della firma dell'Entity Configuration
    - L'Entity Configuration è un JWT firmato; la firma è verificabile usando una delle chiavi pubbliche della Federation Entity contenute in ``jwks`` secondo `OID-FED`_.
  * - FA_003
    - Interoperability
    - Parametri JOSE dell'header dell'Entity Configuration
    - L'header JOSE contiene ``alg`` (permesso), ``kid`` opzionale riferito a una chiave in ``jwks``, e ``typ`` impostato a ``entity-statement+jwt``.
  * - FA_004
    - Security
    - Claim standard nell'Entity Configuration
    - Il payload include ``iss`` e ``sub`` entrambi uguali all'URL identificativo dell'Autorità di Federazione; include ``iat`` e ``exp`` come Unix timestamp validi; ``exp`` > ``iat`` e l'ora corrente < ``exp``.
  * - FA_005
    - Security, Interoperability
    - Parametri comuni dell'Entity Configuration
    - Il payload contiene ``jwks`` e ``metadata`` con l'oggetto ``federation_entity`` che include gli endpoint della Federazione pubblicati come da :ref:`trust-infrastructure:Integrazione tra Infrastruttura di Trust e Registry`.
  * - FA_006
    - Security
    - Validità del materiale crittografico
    - Le voci in ``jwks.keys[*]`` usano algoritmi e dimensioni di chiave consentiti; le chiavi non sono scadute o revocate secondo ``/historical-jwks``; ogni ``kid`` è univoco.
  * - FA_007
    - Security
    - Tolleranza di validazione per ``exp``
    - La validazione rifiuta l'Entity Configuration se ``exp`` è nel passato; può essere applicato uno skew massimo di 120 secondi quando si confrontano ``iat``/``exp`` con l'ora corrente.
  * - FA_008
    - Security
    - Firma e durata del Subordinate Statement
    - ``GET /fetch?sub={entity}`` restituisce un JWT firmato (Subordinate Statement); header e payload sono validi secondo `OID-FED`_; ``iss`` uguale all'Autorità emittente; ``sub`` uguale al soggetto richiesto; ``iat``/``exp`` validi.
  * - FA_009
    - Interoperability
    - Schema del Subordinate Statement
    - Il Subordinate Statement contiene le chiavi pubbliche del subordinato (direttamente o per riferimento) e le eventuali policy di metadata o i metadata applicabili, conformi alla struttura della draft-43.
  * - FA_010
    - Discovery
    - Elenco dei subordinati
    - ``GET /list`` restituisce un array JSON o un elenco JWT-wrapped degli identificativi dei subordinati correnti; il formato della risposta e il media type corrispondono a quanto pubblicato nei metadata; HTTP 200.
  * - FA_011
    - Security
    - Endpoint di stato dei Trust Mark
    - ``GET /trust_mark_status?id={tm_id}&sub={entity}`` restituisce lo stato corrente con HTTP 200 e un oggetto protetto in integrità (JWT se pubblicizzato). Trust Mark ID o soggetti sconosciuti restituiscono l'appropriato 4xx.
  * - FA_012
    - Security
    - Endpoint delle chiavi storiche
    - ``GET /historical-jwks`` restituisce chiavi revocate/scadute con le motivazioni della revoca. La struttura è valida come JWKS o JWKS incapsulato in JWT in base al media type pubblicizzato.
  * - FA_013
    - Security
    - Propagazione della rotazione delle chiavi
    - Dopo la rotazione delle chiavi, ``/.well-known/openid-federation`` e ``/historical-jwks`` sono aggiornati in modo atomico o entro una finestra di propagazione massima documentata. La verifica con la nuova chiave ha esito positivo e la chiave precedente compare nell'elenco storico.
  * - FA_014
    - Security
    - Disabilitare ``alg": "none"`` e algoritmi deboli
    - Qualsiasi Entity Configuration o Subordinate Statement con ``alg": "none"`` o un algoritmo non consentito è rifiutato; l'endpoint restituisce un errore appropriato (ad es., 400/422).
  * - FA_015
    - Security
    - Risoluzione del ``kid`` e gestione mismatch
    - Se l'header JOSE include ``kid``, questo corrisponde a una chiave in ``jwks`` corrente; in caso di mismatch, la verifica fallisce con errore chiaro.
  * - FA_016
    - Interoperability
    - Scoperta endpoint dai metadata
    - I metadata ``federation_entity`` dell'Entity Configuration includono URL funzionanti per ``federation_list_endpoint``, ``federation_fetch_endpoint``, ``federation_trust_mark_status_endpoint`` e ``historical-jwks`` (se pubblicato); ciascuno risponde secondo il proprio contratto.
  * - FA_017
    - Security
    - Auto-coerenza issuer/subject
    - Per l'Entity Configuration, ``iss == sub ==`` URL dell'Autorità; per i Subordinate Statement, ``iss`` è l'URL dell'Autorità e ``sub`` è l'URL del subordinato; qualsiasi deviazione è rifiutata.
  * - FA_018
    - Interoperability
    - Correttezza dei media type (fetch/list/status)
    - ``/fetch``, ``/list``, ``/trust_mark_status`` e ``/historical-jwks`` restituiscono i media type dichiarati nei metadata ``federation_entity``; le risorse JWT-wrapped usano il ``Content-Type`` corretto (ad es., ``application/entity-statement+jwt``, ``application/jwk-set+jwt``).
  * - FA_019
    - Security
    - Prevenzione replay dello Statement (``jti`` opzionale)
    - Se ``jti`` è pubblicato, il riutilizzo entro la finestra di validità è rilevato e loggato o rifiutato secondo policy; altrimenti, l'unicità non è richiesta.
  * - FA_020
    - Security
    - Applicazione delle policy di metadata (se usate)
    - Quando nel Subordinate Statement sono presenti policy di metadata, i metadata effettivi risultanti da policy + metadata sorgente sono conformi alle regole della draft-43; i conflitti sono risolti in modo deterministico.



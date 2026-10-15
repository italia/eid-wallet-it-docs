# Discovery Page - Selezione identità digitale

Pagina ufficiale di *discovery* per la selezione del metodo di autenticazione (identità digitale), basata sulla libreria [Bootstrap Italia](https://italia.github.io/bootstrap-italia/) e conforme all'identità visiva del Sistema IT-Wallet.

## Descrizione

`disco.html` è la pagina con cui l'utente sceglie il metodo di autenticazione (IT-Wallet, CIE, SPID, eIDAS, CNS, IDEM, ...). I metodi e i relativi testi sono caricati dinamicamente a runtime dai file in `locales/` tramite [i18next](https://www.i18next.com/), quindi è possibile aggiungere, rimuovere o tradurre le card senza modificare l'HTML.

Questo pacchetto condivide con le altre pagine HTML ufficiali gli asset in `../shared-ui/` (CSS, JavaScript comuni, font, sprite SVG, favicon e loghi condivisi). Nella cartella `discovery-page/` restano solo i file specifici della discovery (HTML, loader, localizzazione, asset SPID/CIE/IT-Wallet).

## Caratteristiche

- **Conforme alle linee guida PA**: basata su Bootstrap Italia
- **Multilingua**: italiano e inglese tramite i file in `locales/` (i18next)
- **Contenuti data-driven**: i metodi di autenticazione sono definiti nei file di localizzazione
- **Accessibile**: skip-link, ruoli ARIA, gestione del focus e supporto da tastiera
- **Responsive**: layout adattabile a diverse dimensioni di schermo
- **Identità visiva**: utilizza i colori e lo stile ufficiali del Sistema IT-Wallet

## Utilizzo

Poiché la pagina carica i file di localizzazione via `fetch`, va servita tramite un server HTTP (l'apertura diretta con `file://` può essere bloccata dai browser per le richieste `fetch`).

```bash
# dalla cartella discovery-page/
python3 -m http.server 8000
# poi apri http://localhost:8000/disco.html
```

### Personalizzazione dei metodi di autenticazione

Modifica i file `locales/eid-it.json` e `locales/eid-en.json`. Ogni voce in `digital_id` e `alternative_id` definisce nome, logo, testo del pulsante, URL di login e testi di approfondimento.

### Configurazione degli URL di login (placeholder `CAMBIAMI`)

> ⚠️ **Importante**: gli URL di login (`login_url`) presenti nei file di localizzazione sono volutamente impostati al valore segnaposto `CAMBIAMI`. **Ogni `login_url` con valore `CAMBIAMI` DEVE essere sostituito** con l'endpoint reale del proprio ambiente prima di andare in produzione.

Per configurare, apri `locales/eid-it.json` e `locales/eid-en.json` e sostituisci ogni occorrenza di `"login_url": "CAMBIAMI"` con l'URL che avvia il flusso di autenticazione del relativo metodo. Puoi individuarle rapidamente cercando la stringa `CAMBIAMI`.

Esempi del formato atteso (da adattare al proprio proxy/IdP):

| Metodo | Esempio di `login_url` da impostare al posto di `CAMBIAMI` |
| --- | --- |
| CIE SAML2 | `/Saml2/disco?entityID=<ENTITY_ID_IDP_CIE>&return=<RETURN_URL>` |
| CIE OpenID Connect | `/Saml2/disco?entityID=<ENTITY_ID_OP_CIE_OIDC>` |
| eIDAS | `/Saml2/disco?entityID=<ENTITY_ID_EIDAS_NODE>&return=<RETURN_URL>` |
| IDEM | `https://wayf.idem.garr.it/WAYF?entityID=<TUO_ENTITY_ID>&return=<RETURN_URL>` |
| CNS / altri metodi | URL del rispettivo flusso di autenticazione |

**Valori che NON vanno modificati** (non sono endpoint da configurare):

- `"login_url": "it-wallet.html"` — navigazione interna verso la pagina di selezione del wallet inclusa in queste risorse.
- `"login_url": "#spid-idp-button-xlarge-post"` — àncora dell'interfaccia che apre il menu dei gestori SPID (la lista dei gestori è gestita separatamente, vedi sotto).

Gli altri URL informativi (`find_how_to_get_digital_id_url`, `learn_more_link`) puntano per default alle pagine pubbliche ufficiali e possono essere personalizzati opzionalmente.

### Configurazione dei gestori (IdP) SPID

I pulsanti dei gestori SPID NON sono nei file di localizzazione: vengono iniettati a runtime dalla classe `Ita` (`js/ita.min.js`) nel menu `[data-spid-remote]` a partire dall'elenco locale `js/spid-idps-default.json`. Ogni voce ha la forma:

```json
{ "organization_name": "Nome Gestore", "entity_id": "https://idp.example.it", "logo_uri": "img/spid-idp-esempio.svg" }
```

Per personalizzare l'elenco:

- modifica `js/spid-idps-default.json` (aggiungi/rimuovi gestori, allineandoli a `https://registry.spid.gov.it/entities-idp`);
- inserisci i relativi loghi in `img/` e referenziali con un percorso relativo in `logo_uri` (se `logo_uri` è vuoto viene mostrato il nome testuale del gestore);
- l'URL di login del singolo gestore è costruito automaticamente dalla funzione `href` in `js/ita.min.js` come `<return>?entityID=<entity_id>&return=<return>`. Adatta quella funzione al proprio flusso SAML/proxy se necessario.

> Nota: per impostazione predefinita l'elenco è caricato dal file locale (`local = true` in `js/ita.min.js`). È possibile invece recuperarlo dal registro SPID remoto impostando `local = false`, ma in tal caso la richiesta a `registry.spid.gov.it` è soggetta alle policy CORS del browser.

### Dipendenze esterne (CDN)

La libreria i18next è caricata da CDN (jsDelivr); è quindi richiesta una connessione di rete:

```html
<script src="https://cdn.jsdelivr.net/npm/i18next-http-backend@1.3.1/i18nextHttpBackend.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/i18next@25.5.2/i18next.min.js"></script>
```

## Struttura File

```
discovery-page/
├── README.md
├── disco.html
├── js/
│   ├── eid-cards-loader.js
│   └── spid-idps-default.json
├── locales/
│   ├── eid-it.json
│   └── eid-en.json
├── img/                            # Loghi specifici (eIDAS, CNS, IDEM, gestori SPID)
├── cie/cie_white.svg
├── it-wallet/wallet_icon.svg
└── spid/                           # Pulsante e script SPID (favicon in ../shared-ui/spid/)

../shared-ui/                       # Asset condivisi con selection e QR page (vedi README)
```

## Libreria di Riferimento

Questo template è basato su [Bootstrap Italia](https://italia.github.io/bootstrap-italia/), che fornisce componenti conformi alle linee guida di design per i servizi web della Pubblica Amministrazione italiana.

## Accessibilità

La pagina è progettata per rispettare gli standard WCAG 2.1 livello AA: contrasto adeguato, navigazione da tastiera, focus visibile, ruoli ARIA e annunci per screen reader.

## Licenza

Questo componente fa parte delle risorse ufficiali del Sistema IT-Wallet ed è distribuito secondo la licenza del progetto principale.

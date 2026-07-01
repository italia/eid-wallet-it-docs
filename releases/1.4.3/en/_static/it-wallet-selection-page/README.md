# IT-Wallet Selection Page - Scelta dell'app wallet

Pagina ufficiale per la selezione del portafoglio digitale (IT-Wallet) con cui proseguire l'autenticazione, basata sulla libreria [Bootstrap Italia](https://italia.github.io/bootstrap-italia/) e conforme all'identità visiva del Sistema IT-Wallet.

## Descrizione

`it-wallet.html` è la pagina in cui l'utente, dopo aver scelto IT-Wallet nella *discovery page*, seleziona l'app/portafoglio digitale con cui autenticarsi. L'elenco dei wallet è caricato dinamicamente a runtime da `data/it-wallets.json`, mentre i testi dell'interfaccia provengono dai file in `locales/` tramite [i18next](https://www.i18next.com/). Quando i wallet disponibili sono numerosi, vengono mostrati gli strumenti di ricerca e ordinamento.

Questo pacchetto condivide con le altre pagine HTML ufficiali gli asset in `../shared-ui/` (CSS, JavaScript comuni, font, sprite SVG, favicon e loghi condivisi). Nella cartella `it-wallet-selection-page/` restano solo i file specifici della selezione wallet (HTML, loader, dati, localizzazione e icone UI di ricerca/ordinamento).

## Caratteristiche

- **Conforme alle linee guida PA**: basata su Bootstrap Italia
- **Multilingua**: italiano e inglese tramite i file in `locales/` (i18next)
- **Elenco data-driven**: i wallet sono definiti in `data/it-wallets.json`
- **Ricerca e ordinamento**: filtro per nome e ordinamento A-Z / Z-A (visibili oltre una soglia di wallet)
- **Accessibile**: skip-link, ruoli ARIA, gestione del focus, menu da tastiera e annunci live
- **Responsive**: pannello di controlli adattivo tra desktop e mobile

## Utilizzo

Poiché la pagina carica i dati e i file di localizzazione via `fetch`, va servita tramite un server HTTP (l'apertura diretta con `file://` può essere bloccata dai browser per le richieste `fetch`).

```bash
# dalla cartella it-wallet-selection-page/
python3 -m http.server 8000
# poi apri http://localhost:8000/it-wallet.html
```

### Personalizzazione dei wallet

Modifica `data/it-wallets.json`. Ogni voce in `immediate_subordinate_entities` definisce `id`, `name`, `logo_uri`, `description` e `uri` (URL della pagina successiva nel flusso).

Per l'anteprima statica ufficiale, ogni card punta alla QR code page di presentazione remota:

```json
"uri": "../it-wallet-presentation-qr-code-page/qr-code-page.html"
```

Sostituisci l'`uri` con l'endpoint reale del proprio ambiente (es. OpenID4VP / pre-request) prima di andare in produzione.

### Personalizzazione dei testi

Modifica `locales/it-wallet-it.json` e `locales/it-wallet-en.json` (titoli, sottotitoli, etichette di ricerca/ordinamento, footer).

### Dipendenze esterne (CDN)

La libreria i18next è caricata da CDN (jsDelivr); è quindi richiesta una connessione di rete:

```html
<script src="https://cdn.jsdelivr.net/npm/i18next-http-backend@1.3.1/i18nextHttpBackend.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/i18next@25.5.2/i18next.min.js"></script>
```

## Struttura File

```
it-wallet-selection-page/
├── README.md
├── it-wallet.html
├── js/it-wallet-loader.js
├── locales/it-wallet-it.json, it-wallet-en.json
├── data/it-wallets.json
├── img/                            # Icone UI ricerca/ordinamento
└── it-wallet/io_logo.svg

../shared-ui/                       # Asset condivisi (vedi README)
```

## Libreria di Riferimento

Questo template è basato su [Bootstrap Italia](https://italia.github.io/bootstrap-italia/), che fornisce componenti conformi alle linee guida di design per i servizi web della Pubblica Amministrazione italiana.

## Accessibilità

La pagina è progettata per rispettare gli standard WCAG 2.1 livello AA: contrasto adeguato, navigazione da tastiera, focus visibile, ruoli ARIA, menu accessibili e annunci per screen reader.

## Licenza

Questo componente fa parte delle risorse ufficiali del Sistema IT-Wallet ed è distribuito secondo la licenza del progetto principale.

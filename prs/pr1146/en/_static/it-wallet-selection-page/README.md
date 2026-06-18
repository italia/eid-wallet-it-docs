# IT-Wallet Selection Page - Scelta dell'app wallet

Pagina ufficiale per la selezione del portafoglio digitale (IT-Wallet) con cui proseguire l'autenticazione, basata sulla libreria [Bootstrap Italia](https://italia.github.io/bootstrap-italia/) e conforme all'identità visiva del Sistema IT-Wallet.

## Descrizione

`it-wallet.html` è la pagina in cui l'utente, dopo aver scelto IT-Wallet nella *discovery page*, seleziona l'app/portafoglio digitale con cui autenticarsi. L'elenco dei wallet è caricato dinamicamente a runtime da `data/it-wallets.json`, mentre i testi dell'interfaccia provengono dai file in `locales/` tramite [i18next](https://www.i18next.com/). Quando i wallet disponibili sono numerosi, vengono mostrati gli strumenti di ricerca e ordinamento.

Questo pacchetto è **autoconsistente**: tutti gli asset statici necessari (CSS, JavaScript, font, immagini, sprite SVG, file di localizzazione e dati) sono inclusi e referenziati con percorsi relativi.

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

Modifica `data/it-wallets.json`. Ogni voce in `immediate_subordinate_entities` definisce `id`, `name`, `logo_uri`, `description` e `uri` (URL di avvio del flusso).

### Configurazione degli URL di login (placeholder `CAMBIAMI`)

> ⚠️ **Importante**: il campo `uri` di ogni wallet in `data/it-wallets.json` è volutamente impostato al valore segnaposto `CAMBIAMI`. **Ogni `uri` con valore `CAMBIAMI` DEVE essere sostituito** con l'URL reale che avvia il flusso di autenticazione/presentazione (es. OpenID4VP) del proprio ambiente prima di andare in produzione.

Per configurare, apri `data/it-wallets.json` e sostituisci ogni occorrenza di `"uri": "CAMBIAMI"` con l'URL corretto. Puoi individuarle rapidamente cercando la stringa `CAMBIAMI`.

Esempio del formato atteso (da adattare al proprio proxy):

```json
"uri": "/Saml2/disco?entityID=wallet"
```

> Nota: quando l'`uri` contiene `entityID=wallet`, lo script `js/it-wallet-loader.js` instrada la richiesta verso il flusso wallet (OpenID4VP) e vi aggiunge automaticamente i parametri `return` ed `entityID` presenti nella query string della pagina.

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
├── README.md                       # Questa documentazione
├── it-wallet.html                  # Pagina di selezione del wallet
├── css/                            # Fogli di stile
│   ├── style.css                   # Stili della pagina e delle card wallet
│   ├── bootstrap-italia.min.css    # Bootstrap Italia (autoconsistente, asset in data-URI)
│   └── ita.min.css                 # Componenti .Italia aggiuntivi
├── js/                             # Script
│   ├── it-wallet-loader.js         # Logica di rendering, ricerca e ordinamento (i18next + data)
│   ├── header-lang-dropdown.js     # Selettore di lingua nell'header
│   └── bootstrap-italia.bundle.min.js
├── locales/                        # Testi dell'interfaccia (i18next)
│   ├── it-wallet-it.json
│   └── it-wallet-en.json
├── data/it-wallets.json            # Elenco dei wallet disponibili
├── svg/sprites.svg                 # Sprite delle icone .Italia
├── img/                            # Loghi e icone (logo IT-Wallet, icone UI, placeholder)
├── it-wallet/io_logo.svg           # Logo dell'app IO
├── spid/favicon-32x32.png          # Favicon
└── bootstrap-italia/fonts/         # Font statici (Titillium Web, Lora, Roboto Mono)
```

## Libreria di Riferimento

Questo template è basato su [Bootstrap Italia](https://italia.github.io/bootstrap-italia/), che fornisce componenti conformi alle linee guida di design per i servizi web della Pubblica Amministrazione italiana.

## Accessibilità

La pagina è progettata per rispettare gli standard WCAG 2.1 livello AA: contrasto adeguato, navigazione da tastiera, focus visibile, ruoli ARIA, menu accessibili e annunci per screen reader.

## Licenza

Questo componente fa parte delle risorse ufficiali del Sistema IT-Wallet ed è distribuito secondo la licenza del progetto principale.

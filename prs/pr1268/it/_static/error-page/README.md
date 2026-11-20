# Error Page - Errore di autenticazione

Pagina ufficiale di *error* del flusso di Autenticazione, basata sulla libreria [Bootstrap Italia](https://italia.github.io/bootstrap-italia/) e conforme all'identità visiva del Sistema IT-Wallet.

## Descrizione

`error_page.html` informa l'utente che si è verificato un errore durante l'autenticazione e propone le azioni successive (ritorno alla pagina di accesso, assistenza). I testi sono caricati a runtime da `locales/` tramite [i18next](https://www.i18next.com/).

Questo pacchetto condivide con le altre pagine HTML ufficiali gli asset in `../shared-ui/` (CSS, JavaScript comuni, font, sprite SVG, favicon e loghi). Nella cartella `error-page/` restano solo i file specifici della pagina di errore (HTML, i18n, localizzazione).

L'header (`header-title-section`) è allineato a discovery, selection e QR code page (wordmark placeholder `#header-logo`).

## Caratteristiche

- **Conforme alle linee guida PA**: basata su Bootstrap Italia
- **Multilingua**: italiano e inglese tramite i file in `locales/` (i18next)
- **Accessibile**: skip-link, ruoli ARIA, gestione del focus e supporto da tastiera
- **Responsive**: layout adattabile a diverse dimensioni di schermo
- **Identità visiva**: colori e stile ufficiali del Sistema IT-Wallet; pittogramma `../shared-ui/img/error-icon.svg`

## Utilizzo

Poiché la pagina carica i file di localizzazione via `fetch`, va servita tramite un server HTTP:

```bash
cd official_resources
python3 -m http.server 8000
# http://localhost:8000/error-page/error_page.html
```

### Personalizzazione

| Elemento | Dove |
|----------|------|
| Testi UI (IT/EN) | `locales/error-it.json`, `locales/error-en.json` |
| URL CTA accesso | `href` su `.error-page-cta` in `error_page.html` |
| URL assistenza / privacy / note legali | link in footer e `.error-page-assistance` |

## Dipendenze esterne (CDN)

```html
<script src="https://cdn.jsdelivr.net/npm/i18next-http-backend@1.3.1/i18nextHttpBackend.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/i18next@25.5.2/i18next.min.js"></script>
```

## Struttura

```
error-page/
├── README.md
├── error_page.html
├── js/
│   └── error-i18n.js
└── locales/
    ├── error-it.json
    └── error-en.json

../shared-ui/                       # CSS, JS comuni, sprite, favicon, error-icon.svg
../Pages-templates/*/Error-page/    # Mockup SVG di riferimento
```

## Riferimenti

- Specifica: sezioni Error Page in `docs/it/functionalities.rst` / `docs/en/functionalities.rst`
- Template di riferimento implementativo: `iam-proxy-italia-project/static/error_page.html`

## Licenza

Risorsa ufficiale del Sistema IT-Wallet; stessa licenza del progetto principale.

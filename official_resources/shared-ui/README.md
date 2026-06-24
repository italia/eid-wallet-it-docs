# Shared UI assets

Risorse statiche condivise dalle pagine HTML ufficiali del flusso di autenticazione/presentazione:

- `discovery-page/disco.html`
- `it-wallet-selection-page/it-wallet.html`
- `it-wallet-presentation-qr-code-page/qr-code-page.html`

## Contenuto

| Percorso | Descrizione |
|----------|-------------|
| `bootstrap-italia/` | Font Bootstrap Italia |
| `css/` | `style.css`, `bootstrap-italia.min.css`, `ita.min.css` |
| `js/` | `bootstrap-italia.bundle.min.js`, `header-lang-dropdown.js`, `jquery-3.7.0.min.js`, `ita.min.js` |
| `js/qrcode/` | Web component per il rendering del codice QR |
| `svg/sprites.svg` | Sprite icone .Italia |
| `spid/favicon-32x32.png` | Favicon comune |
| `img/` | Loghi e icone di stato condivisi (IT-Wallet, placeholder wallet, QR) |

## Riferimenti dalle pagine

Ogni pagina usa percorsi relativi `../shared-ui/...` per gli asset condivisi e mantiene nella propria cartella solo file specifici (HTML, loader JS, locale, dati, asset SPID/CIE, ecc.).

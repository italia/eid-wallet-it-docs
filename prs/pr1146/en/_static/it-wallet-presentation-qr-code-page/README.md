# IT-Wallet Presentation QR Code Page

Pagina ufficiale statica per il **flusso Cross Device** della presentazione remota (OpenID4VP), mostrata dopo la selezione del wallet in `it-wallet-selection-page`.

L'export è pensato per anteprima, review UX e integrazione documentale: non richiede backend SATOSA/pyeduwi. Il countdown del timer è simulato lato client; non è presente polling sullo `status` endpoint. Gli asset UI comuni (CSS, JS, font, sprite, favicon, loghi) sono in `../shared-ui/`.

## Collegamento dalla Selection Page

Le card in `../it-wallet-selection-page/data/it-wallets.json` puntano a questa pagina:

```json
"uri": "../it-wallet-presentation-qr-code-page/qr-code-page.html"
```

Aprendo `it-wallet.html` e selezionando un wallet si visualizza staticamente la QR code page.

## Contenuto del QR (custom URI scheme)

Il payload del codice QR è configurato in `data/qr-demo-config.json` e costruito come **Authorization Request by reference**, in linea con gli esempi non normativi del flusso remoto (`docs/it/remote-flow.rst`):

- `client_id`
- `request_uri`
- `request_uri_method` (es. `post`)

Schema URL predefinito: **`haip://`** (come negli stack di riferimento pyeduwi / profilo HAIP). Sono supportati anche `haip-vp://` e `openid4vp://` documentati in OpenID4VC-HAIP e OpenID4VP: basta impostare `url_scheme` nel file di configurazione.

Esempio generato (valori di demo):

```text
haip://?client_id=openid_federation%3A%2F%2Frelying-party.example.org%2FOpenID4VP&request_uri=https%3A%2F%2Frelying-party.example.org%2FOpenID4VP%2Frequest-uri%3Fid%3D7f3c2a1b-9c4d-4e5f-a6b7-8d9e0f1a2b3c&request_uri_method=post
```

Il blocco `<details>` in pagina mostra il payload effettivo per verifica manuale.

## Utilizzo

Servire la cartella `official_resources/` (o almeno `it-wallet-selection-page` + questa directory) via HTTP:

```bash
cd official_resources
python3 -m http.server 8000
# http://localhost:8000/it-wallet-selection-page/it-wallet.html
# oppure direttamente:
# http://localhost:8000/it-wallet-presentation-qr-code-page/qr-code-page.html
```

## Personalizzazione

| File | Scopo |
|------|--------|
| `data/qr-demo-config.json` | Schema URL, `client_id`, `request_uri`, timeout QR, logo |
| `locales/qr-it.json`, `locales/qr-en.json` | Testi interfaccia (i18next) |

Parametri principali di `qr-demo-config.json`:

| Campo | Descrizione |
|-------|-------------|
| `url_scheme` | Schema personalizzato (`haip`, `haip-vp`, `openid4vp`, …) |
| `client_id` | Identificativo RP (es. `openid_federation:https://…`) |
| `request_uri` | URI monouso del Request Object (by reference) |
| `request_uri_method` | `get` o `post` |
| `qrcode_expiration_time` | Secondi mostrati dal countdown (solo demo statica) |
| `selection_page_url` | Link del pulsante «Indietro» |

## Struttura

```
it-wallet-presentation-qr-code-page/
├── README.md
├── qr-code-page.html
├── data/qr-demo-config.json
├── locales/qr-it.json, qr-en.json
└── js/qr-code-page.js

../shared-ui/                       # CSS, JS comuni, web component QR, loghi (vedi README)
```

## Riferimenti

- Flusso remoto: `docs/it/remote-flow.rst` (Cross Device, QR code, custom URL schemes)
- Template di riferimento implementativo: `iam-proxy-italia-project/templates/qr_code.html`

## Licenza

Risorsa ufficiale del Sistema IT-Wallet; stessa licenza del progetto principale.

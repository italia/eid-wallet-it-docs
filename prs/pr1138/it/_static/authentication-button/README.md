# Authentication Button - IT-Wallet

Pulsante ufficiale per l'autenticazione tramite IT-Wallet, basato sulla libreria [Bootstrap Italia](https://italia.github.io/bootstrap-italia/docs/componenti/buttons/) e conforme all'identità visiva del Sistema IT-Wallet.

## Descrizione

Il bottone "Authentication Button" è un componente HTML/CSS ufficiale progettato per consentire agli utenti di autenticarsi tramite il Sistema IT-Wallet. Il componente è un'istanza del bottone "icon button" standard del design system .Italia e rispetta le specifiche del Brand Manual.

## Specifiche Brand Manual

Secondo il Brand Manual del Sistema IT-Wallet:

- **Icona**: Simbolo IT-Wallet (posizione consentita solo a sinistra)
- **Font**: Titillium Sans Pro (dimensioni secondo design system)
- **Variante colore**: Solo primary blue `#0066CC` (varianti outline non consentite)
- **Varianti di posizionamento**: Tre varianti disponibili per icona e label:
  1. **Standard**: Icona e label allineate a sinistra, dimensione del bottone dipende dalla lunghezza della label
  2. **Fixed Centered**: Dimensione del bottone fissa, icona e label allineate al centro
  3. **Fixed Justified**: Dimensione del bottone fissa, icona allineata a sinistra, label centrata nello spazio rimanente

Per le linee guida di spaziatura e design, consultare la pagina dei bottoni del design system .Italia.

## Caratteristiche

- **Conforme alle linee guida PA**: Basato su Bootstrap Italia
- **Accessibile**: Rispetta gli standard WCAG per l'accessibilità
- **Responsive**: Adattabile a diverse dimensioni dello schermo
- **Varianti di dimensione**: Disponibile in tre dimensioni (large, medium, small)
- **Varianti di posizionamento**: Tre varianti per icona e label
- **Identità visiva**: Utilizza i colori e lo stile ufficiali del Sistema IT-Wallet

## Colori Ufficiali

- **Colore primario**: `#0066CC` (Blu Italia)
- **Testo**: `#FFFFFF` (Bianco)

## Utilizzo

### Installazione

Includere il file CSS nella pagina HTML:

```html
<link rel="stylesheet" href="authentication-button.css">
```

**Nota sui font**: Il componente include i font Titillium Web come file statici locali nella cartella `fonts/`. Se preferisci utilizzare i font da Google Fonts CDN, decommenta la riga `@import` nel file CSS e commenta le dichiarazioni `@font-face` locali.

### Varianti di Posizionamento

#### 1. Standard (Default)
Icona e label allineate a sinistra. La dimensione del bottone dipende dalla lunghezza della label.

```html
<button class="btn btn-itwallet-auth btn-standard" type="button">
  <span class="btn-icon">
    <svg width="20" height="24" viewBox="0 1.999 20.0764 24.002" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M9.4711 2.1181C9.3255 2.0357 9.1708 1.9991 9.0207 2C8.5465 2.0037 8.1117 2.3836 8.1144 2.9127L8.141 7.7572L1.3722 3.9609C1.2258 3.8785 1.0711 3.8419 0.9209 3.8428C0.4467 3.8464 0.0156 4.2264 0.0146 4.7555L0 20.7225C0 21.4429 0.3241 22.0709 1.018 22.46L7.1029 25.8819C7.2493 25.9643 7.404 26.0009 7.5542 26C8.0284 25.9963 8.4605 25.6164 8.4605 25.0873V8.7138L11.6773 10.5044C12.3721 10.8907 12.6953 11.5215 12.6953 12.2419V21.8357L18.7124 25.2109C18.8589 25.2933 19.0136 25.3299 19.1637 25.329C19.6379 25.3253 20.07 24.9454 20.07 24.4163L20.0764 9.2338C20.0764 8.5133 19.7523 7.8854 19.0584 7.4963L9.4711 2.1181Z" fill="currentColor"/>
    </svg>
  </span>
  <span class="btn-text">Entra con IT-Wallet</span>
</button>
```

#### 2. Fixed Centered
Dimensione del bottone fissa. Icona e label sono allineate al centro.

```html
<button class="btn btn-itwallet-auth btn-fixed-centered" type="button">
  <span class="btn-icon">...</span>
  <span class="btn-text">Entra con IT-Wallet</span>
</button>
```

#### 3. Fixed Justified
Dimensione del bottone fissa. L'icona è allineata a sinistra, mentre la label è centrata nello spazio rimanente.

```html
<button class="btn btn-itwallet-auth btn-fixed-justified" type="button">
  <span class="btn-icon">...</span>
  <span class="btn-text">Entra con IT-Wallet</span>
</button>
```

### Varianti di Dimensione

La dimensione di default è **Small (S)**. Per usare il bottone in dimensione default non è necessario aggiungere classi di size.

#### Small (Default)
```html
<button class="btn btn-itwallet-auth btn-sm" type="button">
  <span class="btn-icon">...</span>
  <span class="btn-text">Entra con IT-Wallet</span>
</button>
```

#### Medium
```html
<button class="btn btn-itwallet-auth btn-md" type="button">
  <span class="btn-icon">...</span>
  <span class="btn-text">Entra con IT-Wallet</span>
</button>
```

#### Large
```html
<button class="btn btn-itwallet-auth btn-lg" type="button">
  <span class="btn-icon">...</span>
  <span class="btn-text">Entra con IT-Wallet</span>
</button>
```

**Nota**: Le dimensioni del font seguono le specifiche del design system .Italia.

### Stato Disabilitato

```html
<button class="btn btn-itwallet-auth" type="button" disabled>
  <span class="btn-icon">...</span>
  <span class="btn-text">Entra con IT-Wallet</span>
</button>
```

## Struttura File

```
authentication-button/
├── README.md                    # Questa documentazione
├── authentication-button.css     # File CSS principale
├── authentication-button.html    # Esempio HTML
├── Authentication-button.svg     # Identità visiva ufficiale
└── fonts/                        # Font files statici per "Titillium Sans Pro"
    ├── titillium-web-400.ttf     # Font weight 400 (normal)
    ├── titillium-web-600.ttf     # Font weight 600 (semi-bold)
    └── titillium-web-700.ttf     # Font weight 700 (bold)
```

## Libreria di Riferimento

Questo componente è basato sulla libreria [Bootstrap Italia](https://italia.github.io/bootstrap-italia/docs/componenti/buttons/), che fornisce componenti conformi alle linee guida di design per i servizi web della Pubblica Amministrazione italiana.

## Identità Visiva

L'identità visiva del bottone è definita nel Brand Manual, indicato nella sezione :ref:`official-resources:Risorse Ufficiali`.

## Accessibilità

Il componente è progettato per essere accessibile e rispettare gli standard WCAG 2.1 livello AA:
- Contrasto del testo conforme agli standard
- Supporto per screen reader
- Navigazione da tastiera
- Focus visibile


## Licenza

Questo componente fa parte delle risorse ufficiali del Sistema IT-Wallet ed è distribuito secondo la licenza del progetto principale.

## Supporto

Per domande o supporto, consultare la documentazione tecnica del Sistema IT-Wallet o contattare il team di sviluppo.

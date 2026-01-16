# Authentication Button - IT-Wallet

Pulsante ufficiale per l'autenticazione tramite IT-Wallet, basato sul framework [dev-kit-italia](https://github.com/italia/dev-kit-italia/tree/main/packages/button) e conforme all'identità visiva del Sistema IT-Wallet.

## Descrizione

Il bottone "Authentication Button" è un componente HTML/CSS ufficiale progettato per consentire agli utenti di autenticarsi tramite il Sistema IT-Wallet. Il componente è conforme alle linee guida di design per i servizi web della Pubblica Amministrazione italiana e utilizza il framework dev-kit-italia.

## Caratteristiche

- **Conforme alle linee guida PA**: Basato su Bootstrap Italia e dev-kit-italia
- **Accessibile**: Rispetta gli standard WCAG per l'accessibilità
- **Responsive**: Adattabile a diverse dimensioni dello schermo
- **Varianti**: Disponibile in tre dimensioni (large, medium, small)
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

### Esempio Base

```html
<button class="btn btn-itwallet-auth" type="button">
  <span class="btn-icon">
    <svg width="20" height="24" viewBox="0 0 20 24" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M9.4711 2.1181C9.3255 2.0357 9.1708 1.9991 9.0207 2C8.5465 2.0037 8.1117 2.3836 8.1144 2.9127L8.141 7.7572L1.3722 3.9609C1.2258 3.8785 1.0711 3.8419 0.9209 3.8428C0.4467 3.8464 0.0156 4.2264 0.0146 4.7555L0 20.7225C0 21.4429 0.3241 22.0709 1.018 22.46L7.1029 25.8819C7.2493 25.9643 7.404 26.0009 7.5542 26C8.0284 25.9963 8.4605 25.6164 8.4605 25.0873V8.7138L11.6773 10.5044C12.3721 10.8907 12.6953 11.5215 12.6953 12.2419V21.8357L18.7124 25.2109C18.8589 25.2933 19.0136 25.3299 19.1637 25.329C19.6379 25.3253 20.07 24.9454 20.07 24.4163L20.0764 9.2338C20.0764 8.5133 19.7523 7.8854 19.0584 7.4963L9.4711 2.1181Z" fill="currentColor"/>
    </svg>
  </span>
  <span class="btn-text">Entra con IT-Wallet</span>
</button>
```

### Varianti di Dimensione

#### Large (Default)
```html
<button class="btn btn-itwallet-auth btn-lg" type="button">
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

#### Small
```html
<button class="btn btn-itwallet-auth btn-sm" type="button">
  <span class="btn-icon">...</span>
  <span class="btn-text">Entra con IT-Wallet</span>
</button>
```


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
└── Authentication-button.svg     # Identità visiva ufficiale
```

## Framework di Riferimento

Questo componente è basato sul framework [dev-kit-italia](https://github.com/italia/dev-kit-italia/tree/main/packages/button), che fornisce componenti conformi alle linee guida di design per i servizi web della Pubblica Amministrazione italiana.

## Identità Visiva

L'identità visiva del bottone è definita nel file `Authentication-button.svg`, disponibile anche all'indirizzo:
https://raw.githubusercontent.com/italia/eidas-it-wallet-docs/versione-corrente/docs/it/images/svg/Authentication-button.svg

## Accessibilità

Il componente è progettato per essere accessibile e rispettare gli standard WCAG 2.1 livello AA:
- Contrasto del testo conforme agli standard
- Supporto per screen reader
- Navigazione da tastiera
- Focus visibile

## Browser Supportati

- Chrome (ultime 2 versioni)
- Firefox (ultime 2 versioni)
- Safari (ultime 2 versioni)
- Edge (ultime 2 versioni)

## Licenza

Questo componente fa parte delle risorse ufficiali del Sistema IT-Wallet ed è distribuito secondo la licenza del progetto principale.

## Supporto

Per domande o supporto, consultare la documentazione tecnica del Sistema IT-Wallet o contattare il team di sviluppo.

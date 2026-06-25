/* global i18next, initHeaderLangDropdown */

const DEFAULT_WALLET_BRAND = 'IT-Wallet';

const QR_CONFIG_FALLBACK = {
  url_scheme: 'haip',
  client_id: 'openid_federation:https://relying-party.example.org/OpenID4VP',
  request_uri: 'https://relying-party.example.org/OpenID4VP/request-uri?id=7f3c2a1b-9c4d-4e5f-a6b7-8d9e0f1a2b3c',
  request_uri_method: 'post',
  qrcode_size: 250,
  qrcode_color: '#000000',
  qrcode_logo_path: '../shared-ui/img/IT-Wallet-Logo-Primary-BlueItalia.svg',
  qrcode_expiration_time: 120,
  selection_page_url: '../it-wallet-selection-page/it-wallet.html',
};

let demoConfig = { ...QR_CONFIG_FALLBACK };
let selectedWallet = {
  name: DEFAULT_WALLET_BRAND,
  logo: null,
};
let expirationTime = demoConfig.qrcode_expiration_time;
let countdown = null;
let countdownStarted = false;

function resolveAsset(path) {
  if (!path) return path;
  if (/^(https?:|\/)/.test(path)) return path;
  return new URL(path, window.location.href).href;
}

function getBasePath() {
  const path = window.location.pathname;
  const lastSlash = path.lastIndexOf('/');
  return lastSlash >= 0 ? path.slice(0, lastSlash + 1) : '/';
}

function buildAuthorizationRequestUrl(scheme, params) {
  let normalizedScheme = scheme || 'haip';
  if (!normalizedScheme.includes('://')) {
    normalizedScheme = `${normalizedScheme}://`;
  }
  const query = new URLSearchParams(params).toString();
  const separator = normalizedScheme.includes('?') ? '' : '?';
  return `${normalizedScheme}${separator}${query}`;
}

function buildDemoQrPayload(config) {
  const params = {
    client_id: config.client_id,
    request_uri: config.request_uri,
  };
  if (config.request_uri_method) {
    params.request_uri_method = config.request_uri_method;
  }
  return buildAuthorizationRequestUrl(config.url_scheme, params);
}

function getWalletBrandName() {
  return selectedWallet.name || DEFAULT_WALLET_BRAND;
}

function readSelectedWalletFromUrl() {
  const params = new URLSearchParams(window.location.search);
  const name = params.get('wallet_name')?.trim();
  const logo = params.get('wallet_logo')?.trim();
  if (name) selectedWallet.name = name;
  if (logo) selectedWallet.logo = logo;
}

function substituteWalletBrand(text, walletName) {
  if (!text || typeof text !== 'string') return text;
  return text.replace(/IT-Wallet/g, walletName);
}

function walletTranslation(t, key, extra = {}) {
  const walletName = getWalletBrandName();
  return substituteWalletBrand(
    t(key, {
      ...extra,
      walletName,
      interpolation: { escapeValue: false },
    }),
    walletName,
  );
}

function applyQrVisualConfig(config) {
  const root = document.documentElement;
  root.style.setProperty('--qr-size', `${config.qrcode_size}px`);

  const payloadUrl = buildDemoQrPayload(config);

  const qrCode = document.querySelector('qr-code');
  if (qrCode) {
    qrCode.setAttribute('module-color', config.qrcode_color);
    qrCode.setAttribute('position-ring-color', config.qrcode_color);
    qrCode.setAttribute('position-center-color', config.qrcode_color);
    qrCode.setAttribute('contents', payloadUrl);
  }

  const logo = document.querySelector('.icon-qr-code');
  if (logo) {
    const logoPath = config.qrcode_logo_path || QR_CONFIG_FALLBACK.qrcode_logo_path;
    logo.onerror = () => {
      logo.onerror = null;
      logo.src = resolveAsset(QR_CONFIG_FALLBACK.qrcode_logo_path);
    };
    logo.src = resolveAsset(logoPath);
  }

  const qrCodeLink = document.getElementById('qr-code-link');
  if (qrCodeLink) {
    qrCodeLink.href = payloadUrl;
  }

  const payloadPreview = document.getElementById('qr-payload-preview');
  if (payloadPreview) {
    payloadPreview.href = payloadUrl;
    payloadPreview.textContent = payloadUrl;
  }
}

function newWindowHintText(t) {
  return t('footer.new_window_hint');
}

function setFooterLink(el, text, href, hint) {
  if (!el) return;
  el.textContent = text;
  if (href) el.setAttribute('href', href);
  el.setAttribute('aria-label', `${text} (${hint})`);
}

function updateTimerDisplay() {
  const timer = document.getElementById('timer');
  if (timer) {
    timer.textContent = String(Math.max(expirationTime, 0));
  }
}

function setupBackLink() {
  const backLink = document.getElementById('back-link');
  if (!backLink) return;
  const params = new URLSearchParams(window.location.search);
  const search = params.toString();
  const selectionUrl = demoConfig.selection_page_url || '../it-wallet-selection-page/it-wallet.html';
  backLink.href = search ? `${selectionUrl}?${search}` : selectionUrl;
}

function updateBackLink(t) {
  const backText = t('backLabel', { defaultValue: 'Torna indietro' });
  const backLink = document.getElementById('back-link');
  if (backLink) backLink.setAttribute('aria-label', backText);
  const backLabel = document.querySelector('.it-wallet-back-label');
  if (backLabel) backLabel.textContent = backText;
}

function updateShellTexts(t) {
  const regionEl = document.getElementById('header-region-name');
  if (regionEl) regionEl.textContent = t('header.region_name');

  const skipNav = document.querySelector('.it-skip-links');
  if (skipNav) skipNav.setAttribute('aria-label', t('skip_links.nav_label'));

  const skipMain = document.getElementById('skip-main');
  if (skipMain) skipMain.textContent = t('skip_links.main_content');

  const skipFooter = document.getElementById('skip-footer');
  if (skipFooter) skipFooter.textContent = t('skip_links.footer');

  const eidTitle = document.getElementById('eid-title');
  const logoAlt = t('header.logo_alt');
  if (eidTitle) eidTitle.textContent = logoAlt;

  const headerLogoText = document.getElementById('header-logo-text');
  if (headerLogoText) headerLogoText.textContent = logoAlt;

  document.querySelectorAll('.qr-header-logo-wallet').forEach((img) => {
    img.setAttribute('alt', getWalletBrandName());
  });

  const qrCodeLink = document.getElementById('qr-code-link');
  if (qrCodeLink) {
    qrCodeLink.setAttribute('aria-label', walletTranslation(t, 'qrCodeLinkAriaLabel'));
  }

  const hint = newWindowHintText(t);
  setFooterLink(document.getElementById('footer-legal'), t('footer.legal_notice'), t('footer.legal_url'), hint);
  setFooterLink(document.getElementById('footer-privacy'), t('footer.privacy_policy'), t('footer.privacy_url'), hint);
  setFooterLink(document.getElementById('footer-accessibility'), t('footer.accessibility_statement'), t('footer.accessibility_url'), hint);

  const footerNav = document.getElementById('footer-legal-nav');
  if (footerNav) footerNav.setAttribute('aria-label', t('footer.nav_label'));

  const noscriptMsg = document.getElementById('noscript-message');
  if (noscriptMsg) noscriptMsg.textContent = t('noscript.message');

  const pageTitle = t('page_title');
  const tabTitle = document.getElementById('tab-title');
  if (tabTitle) tabTitle.textContent = pageTitle;
  document.title = pageTitle;

  const metaDesc = document.getElementById('meta-description');
  if (metaDesc) metaDesc.setAttribute('content', walletTranslation(t, 'meta.description'));

  const payloadSummary = document.getElementById('qr-payload-summary');
  if (payloadSummary) payloadSummary.textContent = t('demoPayloadLabel');

  const reloadLabel = document.getElementById('qr-reload-label');
  if (reloadLabel) reloadLabel.textContent = t('qrCodeReloadLabel');

  updateBackLink(t);
}

function updateTexts(t) {
  updateShellTexts(t);

  const title = document.getElementById('content-title');
  if (title) title.textContent = t('contentTitle');

  const info = document.getElementById('content-qrcode-info-text');
  if (info) {
    info.innerHTML = t('qrCodeValidInfo', { seconds: String(Math.max(expirationTime, 0)) });
  }

  const support = document.getElementById('content-text');
  if (support) support.innerHTML = walletTranslation(t, 'supportText');
}

function stopCountdown() {
  if (countdown) {
    clearInterval(countdown);
    countdown = null;
  }
}

function startCountdown(t) {
  if (countdownStarted) return;
  countdownStarted = true;
  countdown = setInterval(() => {
    expirationTime -= 1;
    updateTimerDisplay();
    if (expirationTime < 0) {
      stopCountdown();
      showExpiredState(t);
    }
  }, 1000);
}

function showExpiredState(t) {
  const qrLink = document.getElementById('qr-code-link');
  if (qrLink) qrLink.classList.add('qr-faded');

  const info = document.getElementById('content-qrcode-info-text');
  if (info) info.innerHTML = walletTranslation(t, 'qrCodeExpiredInfo');

  const actions = document.getElementById('content-function');
  if (!actions) return;

  const reloadLabel = document.getElementById('qr-reload-label');
  if (reloadLabel) reloadLabel.textContent = t('qrCodeReloadLabel');

  actions.hidden = false;
  document.getElementById('qr-reload-btn')?.addEventListener('click', () => {
    window.location.reload();
  });
}

async function loadDemoConfig() {
  try {
    const response = await fetch(`${getBasePath()}data/qr-demo-config.json`);
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    const data = await response.json();
    demoConfig = { ...QR_CONFIG_FALLBACK, ...data };
  } catch (err) {
    console.warn('qr-code-page: using fallback demo config', err);
    demoConfig = { ...QR_CONFIG_FALLBACK };
  }
  if (selectedWallet.logo) {
    demoConfig.qrcode_logo_path = selectedWallet.logo;
  }
  expirationTime = Number(demoConfig.qrcode_expiration_time) || 120;
  applyQrVisualConfig(demoConfig);
}

function initI18n() {
  const initialLang = localStorage.getItem('lang') || 'it';

  i18next
    .use(i18nextHttpBackend)
    .init({
      lng: initialLang,
      fallbackLng: 'it',
      backend: {
        loadPath: `${getBasePath()}locales/qr-{{lng}}.json?v=wallet-ui-qr-20260624`,
      },
    })
    .then((t) => {
      if (typeof initHeaderLangDropdown === 'function') {
        initHeaderLangDropdown(i18next, {
          afterLanguageChange(lng) {
            const code = (lng || 'it').split('-')[0];
            localStorage.setItem('lang', code === 'en' ? 'en' : 'it');
            updateTexts(i18next.t);
          },
        });
      }
      updateTexts(t);
      startCountdown(t);
    })
    .catch((err) => {
      console.error('qr-code-page: i18next init failed', err);
    });
}

document.addEventListener('DOMContentLoaded', async () => {
  readSelectedWalletFromUrl();
  await loadDemoConfig();
  setupBackLink();
  initI18n();
});

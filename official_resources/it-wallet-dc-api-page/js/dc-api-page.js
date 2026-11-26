/* global i18next, initHeaderLangDropdown, getPreferredLang, DigitalCredential */

const CONFIG_FALLBACK = {
  selection_page_url: '../it-wallet-selection-page/it-wallet.html',
  discovery_page_url: '../discovery-page/disco.html',
  protocol: 'openid4vp-v1-unsigned',
  demo_request: {
    response_type: 'vp_token',
    client_id: 'openid_federation:https://relying-party.example.org/OpenID4VP',
    nonce: 'demo-nonce-example-org',
  },
};

let demoConfig = { ...CONFIG_FALLBACK };
let apiSupported = false;
let autoRedirectTimer = null;

function getBasePath() {
  const path = window.location.pathname;
  const lastSlash = path.lastIndexOf('/');
  return lastSlash >= 0 ? path.slice(0, lastSlash + 1) : '/';
}

function fitHeaderLogoToText() {
  const svg = document.getElementById('header-logo');
  const text = document.getElementById('header-logo-text');
  if (!(svg instanceof SVGSVGElement) || !text || typeof text.getBBox !== 'function') return;
  const box = text.getBBox();
  const x = Math.min(0, box.x);
  const width = Math.max(1, box.x + box.width - x);
  svg.setAttribute('viewBox', `${x} 0 ${width} 40`);
  svg.style.width = '';
}

function preservedSearch() {
  return window.location.search || '';
}

function selectionPageUrl() {
  const base = demoConfig.selection_page_url || CONFIG_FALLBACK.selection_page_url;
  return `${base}${preservedSearch()}`;
}

function discoveryPageUrl() {
  const base = demoConfig.discovery_page_url || CONFIG_FALLBACK.discovery_page_url;
  const params = new URLSearchParams(window.location.search);
  const search = params.toString();
  return search ? `${base}?${search}` : base;
}

function redirectToSelection() {
  window.location.assign(selectionPageUrl());
}

function isDigitalCredentialsSupported() {
  if (typeof navigator === 'undefined' || !navigator.credentials || typeof navigator.credentials.get !== 'function') {
    return false;
  }
  if (typeof window.DigitalCredential === 'undefined') {
    return false;
  }
  const protocol = demoConfig.protocol || CONFIG_FALLBACK.protocol;
  if (typeof DigitalCredential.userAgentAllowsProtocol === 'function') {
    try {
      return DigitalCredential.userAgentAllowsProtocol(protocol) === true;
    } catch {
      return true;
    }
  }
  return true;
}

function setStatus(text) {
  const el = document.getElementById('dc-api-status');
  if (el) el.textContent = text || '';
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
  fitHeaderLogoToText();
  if (document.fonts?.ready) {
    document.fonts.ready.then(() => fitHeaderLogoToText());
  }

  document.querySelectorAll('.header-title-section .it-wallet-navbar-logo').forEach((img) => {
    img.setAttribute('alt', t('header.wallet_brand_alt'));
  });

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
  if (metaDesc) metaDesc.setAttribute('content', t('meta.description'));

  const backText = t('backLabel');
  const backLink = document.getElementById('back-link');
  if (backLink) {
    backLink.setAttribute('aria-label', backText);
    backLink.href = discoveryPageUrl();
  }
  const backLabel = document.querySelector('.it-wallet-back-label');
  if (backLabel) backLabel.textContent = backText;

  const cancelLink = document.getElementById('dc-api-cancel');
  if (cancelLink) {
    cancelLink.textContent = t('cancelLabel');
    cancelLink.href = discoveryPageUrl();
  }

  const title = document.getElementById('content-title');
  if (title) title.textContent = t('contentTitle');

  const support = document.getElementById('content-text');
  if (support) {
    support.textContent = apiSupported ? t('supportText') : t('unsupportedText');
  }

  const startLabel = document.getElementById('dc-api-start-label');
  if (startLabel) startLabel.textContent = t('startLabel');

  const fallback = document.getElementById('dc-api-fallback');
  const fallbackLabel = document.getElementById('dc-api-fallback-label');
  if (fallback) fallback.href = selectionPageUrl();
  if (fallbackLabel) fallbackLabel.textContent = t('fallbackLabel');

  const startBtn = document.getElementById('dc-api-start');
  if (startBtn) {
    startBtn.hidden = !apiSupported;
    startBtn.disabled = false;
  }

  applySupportOutcome(t);
}

function applySupportOutcome(t) {
  const startBtn = document.getElementById('dc-api-start');
  if (apiSupported) {
    if (startBtn) startBtn.hidden = false;
    // Outcome of support check: DC API button is available. No lingering "checking" status.
    setStatus('');
    return;
  }

  if (startBtn) startBtn.hidden = true;
  setStatus(t('unsupportedText'));
}

function classifyCredentialError(err) {
  const name = err?.name || '';
  const message = String(err?.message || '').toLowerCase();
  if (name === 'NotAllowedError' || name === 'AbortError') return 'cancelled';
  if (message.includes('no matching') || message.includes('provider') || message.includes('not found')) {
    return 'no_provider';
  }
  return 'error';
}

async function invokeDigitalCredentials(t) {
  const startBtn = document.getElementById('dc-api-start');
  if (startBtn) startBtn.disabled = true;
  setStatus(t('statusWaiting'));

  const protocol = demoConfig.protocol || CONFIG_FALLBACK.protocol;
  const data = demoConfig.demo_request || CONFIG_FALLBACK.demo_request;

  try {
    const credential = await navigator.credentials.get({
      digital: {
        requests: [
          {
            protocol,
            data,
          },
        ],
      },
    });

    if (credential) {
      setStatus(t('statusSuccess'));
    } else {
      setStatus(t('statusNoProvider'));
      scheduleFallbackRedirect();
    }
  } catch (err) {
    console.warn('dc-api-page: credentials.get failed', err);
    const kind = classifyCredentialError(err);
    if (kind === 'cancelled') {
      setStatus(t('statusCancelled'));
    } else if (kind === 'no_provider') {
      setStatus(t('statusNoProvider'));
    } else {
      setStatus(t('statusError'));
    }
    scheduleFallbackRedirect();
  } finally {
    if (startBtn) startBtn.disabled = false;
  }
}

function scheduleFallbackRedirect() {
  if (autoRedirectTimer) clearTimeout(autoRedirectTimer);
  autoRedirectTimer = setTimeout(() => {
    redirectToSelection();
  }, 2800);
}

function setupActions(t) {
  const startBtn = document.getElementById('dc-api-start');
  if (startBtn) {
    startBtn.addEventListener('click', () => {
      if (autoRedirectTimer) clearTimeout(autoRedirectTimer);
      invokeDigitalCredentials(t);
    });
  }
}

async function fetchDemoConfig() {
  try {
    const response = await fetch(`${getBasePath()}data/dc-api-demo-config.json?v=wallet-ui-dc-20261126`);
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    const data = await response.json();
    demoConfig = { ...CONFIG_FALLBACK, ...data };
  } catch (err) {
    console.warn('dc-api-page: using fallback demo config', err);
    demoConfig = { ...CONFIG_FALLBACK };
  }
}

function initI18n() {
  const initialLang =
    typeof getPreferredLang === 'function' ? getPreferredLang() : (localStorage.getItem('lang') || 'it');

  i18next
    .use(i18nextHttpBackend)
    .init({
      lng: initialLang,
      fallbackLng: 'it',
      backend: {
        loadPath: `${getBasePath()}locales/dc-api-{{lng}}.json?v=wallet-ui-dc-20261126c`,
      },
    })
    .then((t) => {
      if (typeof initHeaderLangDropdown === 'function') {
        initHeaderLangDropdown(i18next, {
          afterLanguageChange() {
            updateShellTexts(i18next.t);
          },
        });
      }
      updateShellTexts(t);
      setupActions(t);

      if (!apiSupported) {
        scheduleFallbackRedirect();
      }
    })
    .catch((err) => {
      console.error('dc-api-page: i18next init failed', err);
      redirectToSelection();
    });
}

document.addEventListener('DOMContentLoaded', async () => {
  await fetchDemoConfig();
  apiSupported = isDigitalCredentialsSupported();
  initI18n();
});

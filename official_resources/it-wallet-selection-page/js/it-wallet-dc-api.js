/* global DigitalCredential */

const DC_API_CONFIG_FALLBACK = {
  protocol: 'openid4vp-v1-unsigned',
  demo_request: {
    response_type: 'vp_token',
    client_id: 'openid_federation:https://relying-party.example.org/OpenID4VP',
    nonce: 'demo-nonce-example-org',
  },
};

let dcApiConfig = { ...DC_API_CONFIG_FALLBACK };
let dcApiSupported = false;
let dcApiBound = false;

function isDigitalCredentialsSupported(config = dcApiConfig) {
  if (typeof navigator === 'undefined' || !navigator.credentials || typeof navigator.credentials.get !== 'function') {
    return false;
  }
  if (typeof window.DigitalCredential === 'undefined') {
    return false;
  }
  const protocol = config.protocol || DC_API_CONFIG_FALLBACK.protocol;
  if (typeof DigitalCredential.userAgentAllowsProtocol === 'function') {
    try {
      return DigitalCredential.userAgentAllowsProtocol(protocol) === true;
    } catch {
      return true;
    }
  }
  return true;
}

function setDcApiStatus(text) {
  const el = document.getElementById('dc-api-status');
  if (el) el.textContent = text || '';
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

async function invokeDigitalCredentials(resource) {
  const startBtn = document.getElementById('dc-api-start');
  if (startBtn) startBtn.disabled = true;
  setDcApiStatus(resource?.dc_api?.status_waiting || '');

  const protocol = dcApiConfig.protocol || DC_API_CONFIG_FALLBACK.protocol;
  const data = dcApiConfig.demo_request || DC_API_CONFIG_FALLBACK.demo_request;

  try {
    const credential = await navigator.credentials.get({
      digital: {
        requests: [{ protocol, data }],
      },
    });

    if (credential) {
      setDcApiStatus(resource?.dc_api?.status_success || '');
    } else {
      setDcApiStatus(resource?.dc_api?.status_no_provider || '');
    }
  } catch (err) {
    console.warn('it-wallet-dc-api: credentials.get failed', err);
    const kind = classifyCredentialError(err);
    if (kind === 'cancelled') {
      setDcApiStatus(resource?.dc_api?.status_cancelled || '');
    } else if (kind === 'no_provider') {
      setDcApiStatus(resource?.dc_api?.status_no_provider || '');
    } else {
      setDcApiStatus(resource?.dc_api?.status_error || '');
    }
  } finally {
    if (startBtn) startBtn.disabled = false;
  }
}

function isDcApiDisabledByQuery() {
  const value = new URLSearchParams(window.location.search).get('dc-api');
  if (value == null) return false;
  return /^(0|false|no|off)$/i.test(String(value).trim());
}

export async function fetchDcApiConfig(basePath) {
  if (isDcApiDisabledByQuery()) {
    dcApiSupported = false;
    return false;
  }

  try {
    const response = await fetch(`${basePath}data/dc-api-demo-config.json?v=wallet-ui-20261126d`);
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    const data = await response.json();
    dcApiConfig = { ...DC_API_CONFIG_FALLBACK, ...data };
  } catch (err) {
    console.warn('it-wallet-dc-api: using fallback config', err);
    dcApiConfig = { ...DC_API_CONFIG_FALLBACK };
  }
  dcApiSupported = isDigitalCredentialsSupported(dcApiConfig);
  return dcApiSupported;
}

/**
 * Supported: page header explains the device-wallet path; button below;
 * "Scegli l'app" / subtitle sit under the button as list intro.
 * Unsupported: hide DC block; page header becomes the classic choose-app copy.
 */
export function updateDcApiPanel(resource) {
  const section = document.getElementById('it-wallet-dc-api');
  const startBtn = document.getElementById('dc-api-start');
  const startLabel = document.getElementById('dc-api-start-label');
  const pageTitle = document.getElementById('page-title');
  const pageSubtitle = document.getElementById('page-subtitle');
  const listIntro = document.getElementById('wallet-list-intro');
  const listHeading = document.getElementById('wallet-list-heading');
  const listSubtitle = document.getElementById('wallet-list-subtitle');
  const listSurface = document.querySelector('.it-wallet-layout-surface');
  const tabTitle = document.getElementById('tab-title');

  const chooseTitle = resource?.titles?.page_title || "Scegli l'app";
  const chooseSubtitle = resource?.titles?.page_subtitle
    || 'Seleziona il portafoglio digitale con cui proseguire';

  if (!section) return;

  if (!dcApiSupported) {
    section.hidden = true;
    setDcApiStatus('');
    if (pageTitle) {
      pageTitle.textContent = chooseTitle;
      pageTitle.classList.remove('it-wallet-title-heading--single-line');
    }
    if (pageSubtitle) {
      pageSubtitle.hidden = false;
      pageSubtitle.textContent = chooseSubtitle;
    }
    if (listIntro) listIntro.hidden = true;
    if (listSurface) listSurface.setAttribute('aria-labelledby', 'page-title');
    if (tabTitle) tabTitle.textContent = chooseTitle;
    document.title = chooseTitle;
    return;
  }

  const introTitle = resource?.dc_api?.intro_title
    || 'Usa il selettore di Portafoglio del tuo sistema operativo';
  const introText = resource?.dc_api?.intro_text
    || 'Funziona solo se, in fase di emissione, hai registrato gli attestati nel sistema operativo.';

  if (pageTitle) {
    pageTitle.textContent = introTitle;
    pageTitle.classList.add('it-wallet-title-heading--single-line');
  }
  if (pageSubtitle) {
    pageSubtitle.hidden = false;
    pageSubtitle.textContent = introText;
  }
  if (tabTitle) tabTitle.textContent = introTitle;
  document.title = introTitle;

  if (listIntro) listIntro.hidden = false;
  if (listHeading) listHeading.textContent = resource?.dc_api?.list_heading || 'Oppure';
  if (listSubtitle) listSubtitle.textContent = chooseSubtitle;
  if (listSurface) listSurface.setAttribute('aria-labelledby', 'wallet-list-heading');

  section.hidden = false;
  section.setAttribute(
    'aria-label',
    resource?.dc_api?.section_label || introTitle,
  );
  if (startLabel) {
    startLabel.textContent = resource?.dc_api?.start_label
      || 'Continua con il portafoglio sul dispositivo';
  }
  if (startBtn) {
    startBtn.hidden = false;
    startBtn.disabled = false;
  }
  setDcApiStatus('');

  if (!dcApiBound && startBtn) {
    dcApiBound = true;
    startBtn.addEventListener('click', () => {
      const lang = i18next.language || 'it';
      let current = i18next.getResourceBundle(lang, 'translation');
      if (!current || typeof current !== 'object') {
        current = i18next.store?.data?.[lang]?.translation || resource || {};
      }
      invokeDigitalCredentials(current);
    });
  }
}

export function isDcApiSupported() {
  return dcApiSupported;
}

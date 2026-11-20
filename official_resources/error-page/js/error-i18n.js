/* global initHeaderLangDropdown, getPreferredLang */
/**
 * i18n for error_page.html: load locale and apply to data-i18n / data-i18n-title elements.
 */

function fitHeaderLogoToText() {
  var svg = document.getElementById('header-logo');
  var text = document.getElementById('header-logo-text');
  if (!(svg instanceof SVGSVGElement) || !text || typeof text.getBBox !== 'function') return;
  var box = text.getBBox();
  var x = Math.min(0, box.x);
  var width = Math.max(1, box.x + box.width - x);
  svg.setAttribute('viewBox', x + ' 0 ' + width + ' 40');
  svg.style.width = '';
}

function applyErrorTranslations() {
  var pageTitle = i18next.t('meta.title');
  document.title = pageTitle;
  var titleEl = document.getElementById('error-page-title');
  if (titleEl) titleEl.textContent = pageTitle;
  var metaDesc = document.querySelector('meta[name="description"]');
  if (metaDesc) metaDesc.setAttribute('content', i18next.t('meta.description'));

  // data-i18n: set textContent (with fallback for header.region_name -> header.organization_name)
  document.querySelectorAll('[data-i18n]').forEach(function (el) {
    var key = el.getAttribute('data-i18n');
    if (!key) return;
    var val = i18next.t(key);
    if (val === key && key === 'header.region_name') {
      val = i18next.t('header.organization_name');
    }
    el.textContent = val;
  });

  // Header logo wordmark (same structure as disco / it-wallet / qr-code)
  var logoTitle = i18next.t('header.logo_title');
  var eidTitle = document.getElementById('eid-title');
  if (eidTitle) eidTitle.textContent = logoTitle;
  var headerLogoText = document.getElementById('header-logo-text');
  if (headerLogoText) headerLogoText.textContent = logoTitle;
  var headerLogoImg = document.getElementById('header-logo');
  if (headerLogoImg && headerLogoImg.tagName === 'IMG') {
    headerLogoImg.setAttribute('alt', logoTitle);
  }
  fitHeaderLogoToText();
  if (document.fonts && document.fonts.ready) {
    document.fonts.ready.then(fitHeaderLogoToText);
  }

  // data-i18n-aria-label: set aria-label attribute (skip links nav, footer nav, ...)
  document.querySelectorAll('[data-i18n-aria-label]').forEach(function (el) {
    var key = el.getAttribute('data-i18n-aria-label');
    if (key) el.setAttribute('aria-label', i18next.t(key));
  });

  // data-i18n-newwindow: build an accessible name that announces the link opens
  // in a new window/tab ("<visible text> (<hint>)"), mirroring disco/it-wallet.
  var newWindowHint = i18next.t('footer.new_window_hint');
  document.querySelectorAll('[data-i18n-newwindow]').forEach(function (el) {
    var textEl = el.matches('[data-i18n]') ? el : el.querySelector('[data-i18n]');
    var text = (textEl ? textEl.textContent : el.textContent) || '';
    text = text.trim();
    el.setAttribute('aria-label', newWindowHint ? text + ' (' + newWindowHint + ')' : text);
  });

  // Update html lang
  document.documentElement.lang = i18next.language === 'it' ? 'it' : 'en';
}

function initErrorI18n() {
  applyErrorTranslations();
  if (typeof initHeaderLangDropdown === 'function') {
    initHeaderLangDropdown(i18next, { afterLanguageChange: applyErrorTranslations });
  }
}

if (typeof i18next !== 'undefined' && typeof i18nextHttpBackend !== 'undefined') {
  var basePath = (function () {
    var path = window.location.pathname;
    var lastSlash = path.lastIndexOf('/');
    return lastSlash >= 0 ? path.substring(0, lastSlash + 1) : '/';
  })();
  i18next
    .use(i18nextHttpBackend)
    .init({
      lng: (typeof getPreferredLang === 'function' ? getPreferredLang() : (localStorage.getItem('lang') || document.documentElement.lang || 'it')),
      fallbackLng: 'it',
      backend: {
        loadPath: basePath + 'locales/error-{{lng}}.json'
      }
    })
    .then(initErrorI18n)
    .catch(function (err) {
      console.error('Error loading error page translations:', err);
    });
} else {
  console.warn('i18next not loaded: error page translations skipped');
}

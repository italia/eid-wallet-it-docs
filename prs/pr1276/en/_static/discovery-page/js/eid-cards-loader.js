/* global initHeaderLangDropdown */

const EID_LOADING_FALLBACK = 'Caricamento in corso...';
const EID_ERROR_FALLBACK = 'Impossibile caricare i metodi di autenticazione. Ricarica la pagina.';

function getEidCardsContainer() {
  return document.getElementById('eid-cards-container');
}

function eidLoadingMessage(resource) {
  return resource?.loading?.in_progress ?? EID_LOADING_FALLBACK;
}

function eidErrorMessage(resource) {
  return resource?.loading?.error ?? EID_ERROR_FALLBACK;
}

function setEidCardsLoading(message) {
  const container = getEidCardsContainer();
  if (!container) return;
  container.setAttribute('aria-busy', 'true');
  container.replaceChildren();
  const status = document.createElement('p');
  status.className = 'eid-list-state eid-list-state--loading';
  status.setAttribute('role', 'status');
  status.textContent = message;
  container.appendChild(status);
}

function setEidCardsError(message) {
  const container = getEidCardsContainer();
  if (!container) return;
  container.setAttribute('aria-busy', 'false');
  container.replaceChildren();
  const alert = document.createElement('p');
  alert.className = 'eid-list-state eid-list-state--error';
  alert.setAttribute('role', 'alert');
  alert.textContent = message;
  container.appendChild(alert);
}

setEidCardsLoading(EID_LOADING_FALLBACK);

// ----------------------- i18next -----------------------
function loadEidCardsi18next() {
  const lang = i18next.language;
  let eidBundle = i18next.getResourceBundle(lang, "translation");
  if (!eidBundle) {
    eidBundle = i18next.store?.getDataByLanguage?.(lang)?.translation ?? i18next.store?.data?.[lang]?.translation;
  }
  if (!eidBundle) {
    console.error("eid-cards: locale bundle not loaded for", lang);
    setEidCardsError(EID_ERROR_FALLBACK);
    return;
  }
  setEidCardsLoading(eidLoadingMessage(eidBundle));
  loadDocument(eidBundle);
  loadEidCards(eidBundle);
  if (typeof Ita !== "undefined") {
    new Ita();
  }
  //  if (typeof Cie !== "undefined") {
  //    new Cie();
  //  }
}

// Inizializza i18next
i18next
  .use(i18nextHttpBackend)
  .init({
    lng: 'it',
    fallbackLng: 'it',
    backend: {
      loadPath: 'locales/eid-{{lng}}.json'
    }
  })
  .then(() => {
    if (typeof initHeaderLangDropdown === "function") {
      initHeaderLangDropdown(i18next, {
        afterLanguageChange: () => loadEidCardsi18next(),
      });
    }
    loadEidCardsi18next();
  })
  .catch((err) => {
    console.error('Error loading eid-cards:', err);
    setEidCardsError(EID_ERROR_FALLBACK);
  });

function newWindowHintText(resource) {
  return resource?.footer?.new_window_hint ?? 'si apre in una nuova finestra';
}

function setExternalLinkA11y(linkEl, visibleText, resource) {
  if (!linkEl || visibleText == null) return;
  linkEl.setAttribute('aria-label', `${visibleText} (${newWindowHintText(resource)})`);
}

let eidCardsLoadedOnce = false;

function focusPageHeadingAfterUpdate() {
  const heading = document.getElementById('eid-selection-title');
  if (!heading) return;
  heading.setAttribute('tabindex', '-1');
  heading.focus({ preventScroll: true });
  heading.addEventListener('blur', () => heading.removeAttribute('tabindex'), { once: true });
}

function updatePageHeading(resource) {
  const heading = document.getElementById('eid-selection-title');
  if (!heading) return;
  const hasDigital = checkId(resource.digital_id);
  const hasAlternative = checkId(resource.alternative_id);
  if (hasDigital) {
    heading.textContent = resource.titles.login_digital_identity;
    heading.className = 'h2 text-center mb-4';
  } else if (hasAlternative) {
    heading.textContent = resource.titles.login_alternative_method;
    heading.className = 'h2 text-center mb-3 pb-4';
  }
}

// ----------------------- Document Loader -----------------------
function loadDocument(resource) {
  // header (use bundle or i18next.t so it works regardless of bundle structure)
  const regionEl = document.getElementById('header-region-name');
  if (regionEl) {
    const regionName = resource?.header?.region_name ?? i18next.t('header.region_name');
    regionEl.textContent = regionName || '';
  }
  const skipNav = document.querySelector('.it-skip-links');
  if (skipNav) skipNav.setAttribute('aria-label', resource?.skip_links?.nav_label ?? 'Collegamenti di salto');
  const skipMain = document.getElementById('skip-main');
  if (skipMain) skipMain.textContent = resource?.skip_links?.main_content ?? 'Vai al contenuto principale';
  const skipFooter = document.getElementById('skip-footer');
  if (skipFooter) skipFooter.textContent = resource?.skip_links?.footer ?? 'Vai al piè di pagina';
  const eidTitle = document.getElementById('eid-title');
  const logoText = resource?.titles?.login_logo ?? resource?.header?.region_name ?? '';
  if (eidTitle) eidTitle.textContent = logoText;
  const headerLogoText = document.getElementById('header-logo-text');
  if (headerLogoText) headerLogoText.textContent = logoText;
  const headerLogo = document.getElementById('header-logo');
  if (headerLogo instanceof HTMLImageElement) {
    headerLogo.setAttribute('alt', logoText);
  } else if (headerLogo instanceof SVGElement && eidTitle) {
    headerLogo.setAttribute('role', 'img');
    headerLogo.setAttribute('aria-labelledby', 'eid-title');
  }
  const footerLegal = document.getElementById('footer-legal');
  const footerPrivacy = document.getElementById('footer-privacy');
  const footerAccess = document.getElementById('footer-accessibility');
  const newWindowHint = newWindowHintText(resource);
  const setFooterLink = (el, text) => {
    if (!el || text == null) return;
    el.textContent = text;
    el.setAttribute('aria-label', `${text} (${newWindowHint})`);
  };
  setFooterLink(footerLegal, resource?.footer?.legal_notice ?? '');
  setFooterLink(footerPrivacy, resource?.footer?.privacy_policy ?? '');
  setFooterLink(footerAccess, resource?.footer?.accessibility_statement ?? '');
  const footerNav = document.getElementById('footer-legal-nav');
  if (footerNav) footerNav.setAttribute('aria-label', resource?.footer?.nav_label ?? '');
  const noscriptMsg = document.getElementById('noscript-message');
  if (noscriptMsg) noscriptMsg.textContent = resource?.noscript?.message ?? '';
  const tabTitle = document.getElementById("tab-title");
  const pageTitle = resource?.titles?.page_title ?? '';
  if (tabTitle && tabTitle.textContent !== pageTitle) {
    tabTitle.textContent = pageTitle;
  }
  if (pageTitle && document.title !== pageTitle) {
    document.title = pageTitle;
  }
  const metaDescription = resource?.meta?.description ?? '';
  const metaDesc = document.querySelector('meta[name="description"]');
  if (metaDesc && metaDescription && metaDesc.getAttribute('content') !== metaDescription) {
    metaDesc.setAttribute('content', metaDescription);
  }
}

// ----------------------- Eid Cards Loader -----------------------
function loadEidCards(resource) {
  const container = getEidCardsContainer();
  if (!container) return;
  updatePageHeading(resource);
  container.setAttribute('aria-busy', 'false');
  container.innerHTML = '';
  document.getElementById('eid-alternative-section')?.remove();

  const hasDigital = checkId(resource.digital_id);
  const hasAlternative = checkId(resource.alternative_id);
  if (!hasDigital && !hasAlternative) {
    setEidCardsError(eidErrorMessage(resource));
    return;
  }

  if (hasDigital) {
    const digitalSection = document.createElement('section');
    digitalSection.className = 'mb-4';

    createEidCardsRow(resource, "digital_id", digitalSection);
    container.appendChild(digitalSection);

    const havenDigitalId = resource.titles.havent_digital_identy;
    if (havenDigitalId) {
      const infoSection = document.createElement('section');
      infoSection.className = 'd-flex flex-column align-items-center mb-4';
      infoSection.setAttribute('aria-labelledby', 'eid-havent-digital-id-title');
      const infoTitle = document.createElement('h2');
      infoTitle.id = 'eid-havent-digital-id-title';
      infoTitle.className = 'eid-havent-digital-id-heading';
      infoTitle.textContent = havenDigitalId;

      const infoLink = document.createElement('a');
      infoLink.className = 'eid-find-how-link';
      infoLink.appendChild(document.createTextNode(resource.titles.find_how_to_get_digital_id));
      const findUrl = (resource.titles.find_how_to_get_digital_id_url || '').toString().trim();
      if (findUrl) {
        infoLink.href = findUrl;
        infoLink.target = '_blank';
        infoLink.rel = 'noopener noreferrer';
        setExternalLinkA11y(infoLink, resource.titles.find_how_to_get_digital_id, resource);
      } else {
        infoLink.href = '#';
        infoLink.addEventListener('click', (e) => e.preventDefault());
      }
      const svgNs = 'http://www.w3.org/2000/svg';
      const linkIcon = document.createElementNS(svgNs, 'svg');
      linkIcon.setAttribute('aria-hidden', 'true');
      linkIcon.setAttribute('width', '16');
      linkIcon.setAttribute('height', '16');
      linkIcon.setAttribute('viewBox', '0 0 24 24');
      linkIcon.setAttribute('fill', '#0066cc');
      const path = document.createElementNS(svgNs, 'path');
      path.setAttribute('d', 'M21 3v6h-1V4.7l-7.6 7.7-.8-.8L19.3 4H15V3h6zm-4 16.5c0 .3-.2.5-.5.5h-12c-.3 0-.5-.2-.5-.5v-12c0-.3.2-.5.5-.5H12V6H4.5C3.7 6 3 6.7 3 7.5v12c0 .8.7 1.5 1.5 1.5h12c.8 0 1.5-.7 1.5-1.5V12h-1v7.5z');
      linkIcon.appendChild(path);
      infoLink.appendChild(linkIcon);
      infoSection.appendChild(infoTitle);
      infoSection.appendChild(infoLink);
      container.appendChild(infoSection);
    }
  }

  if (checkId(resource.alternative_id)) {
    const altWrapper = document.createElement('section');
    altWrapper.id = 'eid-alternative-section';
    altWrapper.className = 'py-4 eid-alternative-section';
    altWrapper.setAttribute('role', 'region');

    const altSection = document.createElement('div');
    altSection.className = 'container mb-0';
    const hasDigitalSection = checkId(resource.digital_id);
    const altTitleId = 'eid-alternative-title';
    const title = document.createElement(hasDigitalSection ? 'h2' : 'h1');
    title.id = hasDigitalSection ? altTitleId : 'eid-selection-title';
    title.textContent = resource.titles.login_alternative_method;
    title.className = 'h2 text-center mb-3 pb-4';
    altWrapper.setAttribute('aria-labelledby', hasDigitalSection ? altTitleId : 'eid-selection-title');
    altSection.appendChild(title);

    createEidCardsRow(resource, 'alternative_id', altSection, {
      cardHeadingLevel: hasDigitalSection ? 3 : 2,
    });
    altWrapper.appendChild(altSection);
    const authMethods = document.getElementById('auth-methods');
    (authMethods || container.closest('main'))?.appendChild(altWrapper);
  }

  if (eidCardsLoadedOnce) {
    focusPageHeadingAfterUpdate();
  }
  eidCardsLoadedOnce = true;
}

// ----------------------- Create Eid Cards Row -----------------------
function createEidCardsRow(resource, id_key, container, options = {}) {
  const cardHeadingLevel = options.cardHeadingLevel ?? 2;
  const listLabel = id_key === 'alternative_id'
    ? (resource?.titles?.login_alternative_method ?? '')
    : (resource?.titles?.login_digital_identity ?? '');
  const row = document.createElement('ul');
  row.className = 'row it-card-list justify-content-center align-items-start eid-cards-row';
  if (listLabel) row.setAttribute('aria-label', listLabel);

  const entries = getEidEntriesForRow(resource[id_key]);
  entries.forEach((eid) => {
    const col = document.createElement('li');
    col.className = 'col-12 col-md-3 mb-3 mb-md-4 eid-card-col';
    col.appendChild(createEidCardBox(resource, eid, cardHeadingLevel));
    row.appendChild(col);
  });
  container.appendChild(row);
}

// Merge CIE SAML2 and CIE OIDC into single card with dropdown when both present
function getEidEntriesForRow(entriesObj) {
  if (!entriesObj || typeof entriesObj !== 'object') return [];
  const entries = Object.entries(entriesObj);
  const hasCie = entries.some(([k]) => k === 'cie');
  const hasCieOidc = entries.some(([k]) => k === 'cie_oidc');
  if (hasCie && hasCieOidc) {
    const cie = entriesObj.cie;
    const cieOidc = entriesObj.cie_oidc;
    const mergedCie = {
      name: 'CIE',
      logo_text: cie.logo_text || 'Login with CIE',
      logo: cie.logo,
      login_url: '#cie-idp-button',
      _cieOptions: [cie, cieOidc],
      learn_more_descr: cie.learn_more_descr,
      learn_more_link: cie.learn_more_link
    };
    const result = [];
    let mergedCieInserted = false;
    for (const [k, v] of entries) {
      if (k === 'cie' || k === 'cie_oidc') {
        if (!mergedCieInserted) {
          result.push(mergedCie);
          mergedCieInserted = true;
        }
      } else {
        result.push(v);
      }
    }
    return result;
  }
  return entries.map(([, v]) => v);
}

// ----------------------- Eid Card Box (Bootstrap Italia it-card) -----------------------
function createEidCardBox(resource, eid, headingLevel = 2) {
  // Bootstrap Italia card: https://italia.github.io/bootstrap-italia/docs/componenti/card/
  const card = document.createElement('article');
  card.className = 'it-card shadow';

  const safeLevel = Math.min(6, Math.max(2, headingLevel));
  const title = document.createElement(`h${safeLevel}`);
  title.className = 'it-card-title mb-3 h4';
  title.id = `eid-card-title-${eidCardSlug(eid)}`;
  title.textContent = eid.name;
  card.setAttribute('aria-labelledby', title.id);

  const body = document.createElement('div');
  body.className = 'it-card-body d-flex flex-column';
  const bodyRow = document.createElement('div');
  bodyRow.className = 'd-flex justify-content-between align-items-center flex-wrap gap-2';

  const withLearnMore = !!eid.learn_more_link || !!eid.learn_more_descr;
  bodyRow.appendChild(createLogoButton(eid, withLearnMore));
  body.appendChild(bodyRow);

  if (withLearnMore) {
    const learnMoreElem = createLearnMore(resource, eid, title.id);
    if (learnMoreElem) {
      learnMoreElem.classList.add('mt-2');
      body.appendChild(learnMoreElem);
    }
  }

  card.appendChild(title);
  card.appendChild(body);
  return card;
}

const EID_SPID_DISCOVERY_MENU_ID = 'spid-idp-button-xlarge-post';

function isSpidDiscoveryMenuOpen(menu, trigger) {
  if (!(menu instanceof HTMLElement) || !(trigger instanceof HTMLElement)) return false;
  if (!trigger.classList.contains('spid-idp-button-open')) return false;
  return getComputedStyle(menu).display !== 'none';
}

function getSpidMenuFocusableLinks(menu) {
  if (!(menu instanceof HTMLElement)) return [];
  return Array.from(menu.querySelectorAll('a[href]')).filter((link) => {
    if (!(link instanceof HTMLAnchorElement)) return false;
    return link.offsetParent !== null || getComputedStyle(link).display !== 'none';
  });
}

function applySpidMenuRovingTabindex(links, activeIndex) {
  links.forEach((link, index) => {
    if (index === activeIndex) {
      link.tabIndex = 0;
    } else {
      link.tabIndex = -1;
    }
  });
}

function resetSpidMenuRovingTabindex(menu) {
  getSpidMenuFocusableLinks(menu).forEach((link) => link.removeAttribute('tabindex'));
}

function focusSpidMenuLinkByIndex(links, index) {
  if (links.length === 0) return;
  const safeIndex = ((index % links.length) + links.length) % links.length;
  applySpidMenuRovingTabindex(links, safeIndex);
  links[safeIndex].focus({ preventScroll: true });
}

function onSpidMenuOpened(menu, trigger, options = {}) {
  const { focusLast = false } = options;
  const links = getSpidMenuFocusableLinks(menu);
  if (links.length === 0) return;
  const index = focusLast ? links.length - 1 : 0;
  focusSpidMenuLinkByIndex(links, index);
  trigger.setAttribute('aria-expanded', 'true');
}

function handleSpidMenuArrowNavigation(event, menu, trigger) {
  const links = getSpidMenuFocusableLinks(menu);
  if (links.length === 0) return false;

  const { key } = event;
  const isNext = key === 'ArrowDown' || key === 'ArrowRight';
  const isPrev = key === 'ArrowUp' || key === 'ArrowLeft';
  if (!isNext && !isPrev && key !== 'Home' && key !== 'End') return false;

  event.preventDefault();
  event.stopPropagation();

  let currentIndex = links.indexOf(document.activeElement);
  if (currentIndex < 0 && document.activeElement === trigger) {
    currentIndex = isPrev || key === 'End' ? 0 : -1;
  }

  if (isNext) {
    focusSpidMenuLinkByIndex(links, currentIndex + 1);
  } else if (isPrev) {
    focusSpidMenuLinkByIndex(links, currentIndex <= 0 ? links.length - 1 : currentIndex - 1);
  } else if (key === 'Home') {
    focusSpidMenuLinkByIndex(links, 0);
  } else if (key === 'End') {
    focusSpidMenuLinkByIndex(links, links.length - 1);
  }
  return true;
}

function openSpidDiscoveryMenu(trigger, menu, options = {}) {
  if (!(trigger instanceof HTMLElement) || !(menu instanceof HTMLElement)) return;
  menu.style.removeProperty('display');
  if (!trigger.classList.contains('spid-idp-button-open') && typeof window.jQuery === 'function') {
    window.jQuery(trigger).trigger('click');
  }
  requestAnimationFrame(() => onSpidMenuOpened(menu, trigger, options));
}

function bindSpidMenuKeyboard(menu, trigger) {
  if (!(menu instanceof HTMLElement) || !(trigger instanceof HTMLElement)) return;
  if (menu.dataset.eidSpidKbBound === 'true') return;
  menu.dataset.eidSpidKbBound = 'true';

  menu.addEventListener(
    'keydown',
    (event) => {
      if (!isSpidDiscoveryMenuOpen(menu, trigger)) return;
      handleSpidMenuArrowNavigation(event, menu, trigger);
    },
    true
  );

  trigger.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') return;
    if (isSpidDiscoveryMenuOpen(menu, trigger)) {
      if (handleSpidMenuArrowNavigation(event, menu, trigger)) return;
      return;
    }
    if (event.key === 'ArrowDown' || event.key === 'ArrowRight') {
      event.preventDefault();
      openSpidDiscoveryMenu(trigger, menu, { focusLast: false });
    } else if (event.key === 'ArrowUp' || event.key === 'ArrowLeft') {
      event.preventDefault();
      openSpidDiscoveryMenu(trigger, menu, { focusLast: true });
    }
  });

  if (typeof window.jQuery === 'function') {
    window.jQuery(menu).on('show.eidSpidKb', () => {
      if (!isSpidDiscoveryMenuOpen(menu, trigger)) return;
      const links = getSpidMenuFocusableLinks(menu);
      if (links.length === 0) return;
      if (!links.includes(document.activeElement)) {
        onSpidMenuOpened(menu, trigger);
      }
    });
  }
}

function ensureEidSpidGlobalListeners() {
  if (window.__eidSpidGlobalListenersBound) return;
  window.__eidSpidGlobalListenersBound = true;

  // Clear inline display (including prior !important close) before the SPID jQuery
  // handler runs, so .show() can open the panel.
  document.addEventListener(
    'click',
    (e) => {
      const trigger = e.target?.closest?.('[spid-idp-button]');
      if (!(trigger instanceof HTMLElement)) return;
      const sel = trigger.getAttribute('spid-idp-button');
      if (!sel) return;
      const panel = document.querySelector(sel);
      if (panel instanceof HTMLElement) panel.style.removeProperty('display');
    },
    true
  );

  document.addEventListener(
    'keydown',
    (e) => {
      if (e.key !== 'Escape') return;
      if (!closeEidSpidDiscoveryMenu()) return;
      e.preventDefault();
      e.stopPropagation();
    },
    true
  );
}

/**
 * Closes the SPID discovery panel. Uses display:none !important so Italia .ita
 * focus-within rules cannot keep the menu visible while focus is on an IdP link.
 */
function closeEidSpidDiscoveryMenu(trigger, menuEl) {
  let t = trigger;
  let m = menuEl;
  if (!m) m = document.getElementById(EID_SPID_DISCOVERY_MENU_ID);
  if (!t) t = document.querySelector('.eid-card-btn-spid.spid-idp-button-open');
  if (!t && m instanceof HTMLElement) {
    const cs = getComputedStyle(m);
    if (cs.display !== 'none' && cs.visibility !== 'hidden') {
      t = document.querySelector(`[spid-idp-button="#${EID_SPID_DISCOVERY_MENU_ID}"]`);
    }
  }
  if (!(t instanceof HTMLElement) || !(m instanceof HTMLElement)) return false;
  t.focus({ preventScroll: true });
  if (typeof window.jQuery === 'function') {
    window.jQuery(m).removeData('spid-idp-button-trigger');
    window.jQuery(t).spidIDPButton('hide');
  }
  t.classList.remove('spid-idp-button-open');
  t.setAttribute('aria-expanded', 'false');
  m.style.setProperty('display', 'none', 'important');
  resetSpidMenuRovingTabindex(m);
  return true;
}

// ----------------------- Logo Button -----------------------
function createLogoButton(eid, _hasLearnMore = false) {
  const createLogoImg = () => {
    const img = document.createElement('img');
    img.src = eid.logo;
    img.alt = '';
    img.setAttribute('aria-hidden', 'true');
    img.className = 'eid-card-logo';
    return img;
  };

  const createTextSpan = () => {
    const span = document.createElement('span');
    span.className = 'eid-card-btn-label';
    span.textContent = eid.logo_text;
    return span;
  };

  // CIE multiprovider: dropdown when both CIE SAML2 and CIE OIDC are present
  if (eid._cieOptions && eid._cieOptions.length > 0) {
    const wrapper = document.createElement('div');
    wrapper.className = 'ita ita-dropdown ita-l ita-fixed eid-cie-dropdown-wrapper';

    const btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'btn btn-primary d-flex align-items-center eid-card-btn eid-card-btn-cie';
    btn.setAttribute('aria-haspopup', 'true');
    btn.setAttribute('aria-expanded', 'false');

    const menuId = `eid-cie-menu-${eidCardSlug(eid)}`;
    btn.setAttribute('aria-controls', menuId);

    btn.appendChild(createLogoImg());
    const cieSep = document.createElement('span');
    cieSep.className = 'eid-card-separator';
    cieSep.setAttribute('aria-hidden', 'true');
    btn.appendChild(cieSep);
    btn.appendChild(createTextSpan());

    const menu = document.createElement('ul');
    menu.id = menuId;
    menu.className = 'cie-dropdown-menu spid-idp-button-link';
    menu.setAttribute('role', 'list');

    eid._cieOptions.forEach((opt) => {
      const li = document.createElement('li');
      li.className = 'spid-idp-button-link';
      const link = document.createElement('a');
      link.href = opt.login_url;
      link.innerHTML = `<img src="${opt.logo}" alt=""> <span class="cie-option-label">${opt.name}</span>`;
      li.appendChild(link);
      menu.appendChild(li);
    });

    const closeMenu = () => {
      menu.classList.remove('is-open');
      btn.setAttribute('aria-expanded', 'false');
      document.removeEventListener('click', outsideClick);
      document.removeEventListener('keydown', onDocumentKeydown, true);
    };
    const outsideClick = (e) => {
      if (!wrapper.contains(e.target)) closeMenu();
    };
    const onDocumentKeydown = (e) => {
      if (e.key === 'Escape') {
        e.preventDefault();
        closeMenu();
        btn.focus();
      }
    };

    const toggleMenu = (e) => {
      e.preventDefault();
      e.stopPropagation();
      const isOpen = menu.classList.contains('is-open');
      if (isOpen) {
        closeMenu();
      } else {
        menu.classList.add('is-open');
        btn.setAttribute('aria-expanded', 'true');
        requestAnimationFrame(() => {
          requestAnimationFrame(() => {
            document.addEventListener('click', outsideClick);
            document.addEventListener('keydown', onDocumentKeydown, true);
          });
        });
      }
    };
    btn.addEventListener('click', toggleMenu);
    btn.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        toggleMenu(e);
      } else if (e.key === 'Escape') {
        e.preventDefault();
        closeMenu();
      }
    });

    wrapper.appendChild(btn);
    wrapper.appendChild(menu);

    return wrapper;
  }

  if (eid.login_url?.includes("#spid-idp-button")) {
    const wrapper = document.createElement('div');
    // Do not use `ita-dropdown` here: that style can open menu on focus.
    // SPID menu must open only on explicit activation (click/Enter/Space).
    wrapper.className = 'ita ita-l ita-fixed eid-cie-dropdown-wrapper';

    const btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'btn btn-primary d-flex align-items-center eid-card-btn eid-card-btn-spid';
    btn.setAttribute('spid-idp-button', `#${EID_SPID_DISCOVERY_MENU_ID}`);
    btn.setAttribute('aria-haspopup', 'true');
    btn.setAttribute('aria-expanded', 'false');
    btn.setAttribute('aria-controls', EID_SPID_DISCOVERY_MENU_ID);

    btn.appendChild(createLogoImg());
    const spidSep = document.createElement('span');
    spidSep.className = 'eid-card-separator';
    spidSep.setAttribute('aria-hidden', 'true');
    btn.appendChild(spidSep);
    btn.appendChild(createTextSpan());

    const menu = document.createElement('div');
    menu.id = EID_SPID_DISCOVERY_MENU_ID;
    menu.className = 'ita-menu';
    menu.setAttribute('data-spid-remote', '');
    // Prevent CSS `:focus-within` from auto-opening on Tab focus.
    // The menu is shown only by explicit activation handled by the SPID plugin.
    menu.style.display = 'none';

    wrapper.appendChild(btn);
    wrapper.appendChild(menu);

    const hideSpidMenu = () => {
      closeEidSpidDiscoveryMenu(btn, menu);
    };

    // Toggle behavior: second click on an open SPID trigger closes the menu.
    btn.addEventListener('click', (e) => {
      if (!btn.classList.contains('spid-idp-button-open')) return;
      e.preventDefault();
      e.stopPropagation();
      hideSpidMenu();
    }, { capture: true });

    btn.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        e.preventDefault();
        hideSpidMenu();
      }
    });

    bindSpidMenuKeyboard(menu, btn);
    ensureEidSpidGlobalListeners();

    return wrapper;
  }

  let href = eid.login_url;
  const isWallet = eid.name?.toLowerCase().includes('it-wallet') || eid.logo?.toLowerCase().includes('it-wallet');
  if (isWallet && window.location.search) {
    const sep = href.includes('?') ? '&' : '?';
    href = href + sep + window.location.search.slice(1);
  }
  const isCie = eid.name?.toLowerCase().includes('cie') || eid.logo?.toLowerCase().includes('cie');
  const isEidas =
    eid.name?.toLowerCase().includes('eidas') ||
    eid.logo_text?.toLowerCase().includes('eidas') ||
    eid.logo?.toLowerCase().includes('eidas');
  const btnClassName =
    'btn btn-primary d-flex align-items-center eid-card-btn' +
    (isCie ? ' eid-card-btn-cie' : '') +
    (isWallet ? ' eid-card-btn-wallet' : '') +
    (isEidas ? ' eid-card-btn-eidas' : '');

  const btn = document.createElement('button');
  btn.type = 'button';
  btn.className = btnClassName;
  btn.addEventListener('click', () => {
    window.location.href = href;
  });

  btn.appendChild(createLogoImg());
  if (!isWallet) {
    const sep = document.createElement('span');
    sep.className = 'eid-card-separator';
    sep.setAttribute('aria-hidden', 'true');
    btn.appendChild(sep);
  }
  btn.appendChild(createTextSpan());

  return btn;
}

// ----------------------- Learn More -----------------------
function eidCardSlug(eid) {
  return (eid.name || 'card').toLowerCase().replace(/[^a-z0-9]+/g, '-');
}

function syncLearnMoreToggleA11y(toggle, content, cardTitleId, actionId, isExpanded) {
  toggle.setAttribute('aria-expanded', isExpanded ? 'true' : 'false');
  toggle.setAttribute('aria-labelledby', `${actionId} ${cardTitleId}`);
  toggle.classList.toggle('expanded', isExpanded);
  content.classList.toggle('is-open', isExpanded);
  if (isExpanded) {
    content.removeAttribute('hidden');
  } else {
    content.setAttribute('hidden', '');
  }
}

/** Move focus into expanded panel so screen readers can read new content (WCAG 2.4.3). */
function focusLearnMorePanel(content) {
  if (!(content instanceof HTMLElement)) return;
  const focusable = content.querySelector('a[href], button:not([disabled])');
  if (focusable instanceof HTMLElement) {
    focusable.focus({ preventScroll: true });
    return;
  }
  if (!content.hasAttribute('tabindex')) {
    content.setAttribute('tabindex', '-1');
  }
  content.focus({ preventScroll: true });
}

function createLearnMore(resource, eid, cardTitleId) {
  const toggleLabelText = eid.learn_more_toggle_label ?? resource.titles.learn_more;
  const ctaLabelText = eid.learn_more_label ?? resource.titles.find_how_to_get_digital_id ?? resource.titles.learn_more;
  const appendExternalIcon = (linkEl) => {
    const svgNs = 'http://www.w3.org/2000/svg';
    const icon = document.createElementNS(svgNs, 'svg');
    icon.setAttribute('aria-hidden', 'true');
    icon.setAttribute('width', '16');
    icon.setAttribute('height', '16');
    icon.setAttribute('viewBox', '0 0 24 24');
    icon.setAttribute('fill', '#0066cc');
    const path = document.createElementNS(svgNs, 'path');
    path.setAttribute('d', 'M21 3v6h-1V4.7l-7.6 7.7-.8-.8L19.3 4H15V3h6zm-4 16.5c0 .3-.2.5-.5.5h-12c-.3 0-.5-.2-.5-.5v-12c0-.3.2-.5.5-.5H12V6H4.5C3.7 6 3 6.7 3 7.5v12c0 .8.7 1.5 1.5 1.5h12c.8 0 1.5-.7 1.5-1.5V12h-1v7.5z');
    icon.appendChild(path);
    linkEl.appendChild(document.createTextNode(' '));
    linkEl.appendChild(icon);
  };
  if (eid.learn_more_descr) {
    const container = document.createElement('div');
    container.className = 'mt-2';

    const cardSlug = eidCardSlug(eid);
    const contentId = `eid-learn-more-${cardSlug}`;
    const toggleId = `${contentId}-toggle`;
    const actionId = `${contentId}-action`;
    const resolvedCardTitleId = cardTitleId || `eid-card-title-${cardSlug}`;

    const toggle = document.createElement('button');
    toggle.type = 'button';
    toggle.id = toggleId;
    toggle.className = 'eid-learn-more-toggle';
    toggle.setAttribute('aria-controls', contentId);

    const toggleLabel = document.createElement('span');
    toggleLabel.id = actionId;
    toggleLabel.className = 'eid-learn-more-toggle-label';
    toggleLabel.textContent = toggleLabelText;
    toggle.appendChild(toggleLabel);

    const svgNs = 'http://www.w3.org/2000/svg';
    const arrow = document.createElementNS(svgNs, 'svg');
    arrow.setAttribute('class', 'eid-learn-more-arrow');
    arrow.setAttribute('aria-hidden', 'true');
    arrow.setAttribute('width', '4');
    arrow.setAttribute('height', '3');
    arrow.setAttribute('viewBox', '0 0 16 16');
    const arrowPath = document.createElementNS(svgNs, 'path');
    arrowPath.setAttribute('fill', 'none');
    arrowPath.setAttribute('stroke', '#0066cc');
    arrowPath.setAttribute('stroke-width', '2');
    arrowPath.setAttribute('stroke-linecap', 'round');
    arrowPath.setAttribute('stroke-linejoin', 'round');
    arrowPath.setAttribute('d', 'm2 5 6 6 6-6');
    arrow.appendChild(arrowPath);
    toggle.appendChild(arrow);

    const text = document.createElement('div');
    text.id = contentId;
    text.setAttribute('role', 'region');
    text.setAttribute('aria-live', 'off');
    text.setAttribute('aria-labelledby', `${resolvedCardTitleId} ${actionId}`);
    text.innerHTML = eid.learn_more_descr;
    if (eid.learn_more_link) {
      const inlineCta = document.createElement('a');
      inlineCta.href = eid.learn_more_link;
      inlineCta.target = '_blank';
      inlineCta.rel = 'noopener noreferrer';
      inlineCta.className = 'eid-find-how-link';
      inlineCta.textContent = ctaLabelText;
      setExternalLinkA11y(inlineCta, ctaLabelText, resource);
      appendExternalIcon(inlineCta);
      text.appendChild(inlineCta);
    }
    text.className = 'mt-2 eid-learn-more-content';

    syncLearnMoreToggleA11y(toggle, text, resolvedCardTitleId, actionId, false);

    toggle.addEventListener('click', () => {
      const isExpanded = toggle.getAttribute('aria-expanded') === 'true';
      const nextExpanded = !isExpanded;
      syncLearnMoreToggleA11y(toggle, text, resolvedCardTitleId, actionId, nextExpanded);
      if (nextExpanded) {
        requestAnimationFrame(() => focusLearnMorePanel(text));
      }
    });

    container.appendChild(toggle);
    container.appendChild(text);
    return container;
  } else if (eid.learn_more_link) {
    const link = document.createElement('a');
    link.href = eid.learn_more_link;
    link.target = '_blank';
    link.rel = 'noopener noreferrer';
    link.className = 'd-block mt-2';
    link.textContent = ctaLabelText;
    setExternalLinkA11y(link, ctaLabelText, resource);
    appendExternalIcon(link);
    return link;
  }
  return null;
}

// ----------------------- Helpers -----------------------
function checkId(id) {
  return id && typeof id === 'object' && Object.keys(id).length > 0;
}

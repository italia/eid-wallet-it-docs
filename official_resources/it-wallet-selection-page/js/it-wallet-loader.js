/**
 * IT-Wallet selection page: load wallets, random default order,
 * optional search/sort controls and card rendering.
 */

const SHOW_CARD_LEARN_MORE = false;
const SEARCH_MIN_WALLETS = 7;
const WALLET_LOADING_FALLBACK = 'Caricamento in corso...';
const WALLET_ERROR_FALLBACK = 'Impossibile caricare l\'elenco wallet. Ricarica la pagina.';

function getWalletGrid() {
  return document.getElementById('wallet-grid');
}

function walletLoadingMessage(resource) {
  return resource?.loading?.in_progress ?? WALLET_LOADING_FALLBACK;
}

function walletErrorMessage(resource) {
  return resource?.loading?.error ?? WALLET_ERROR_FALLBACK;
}

function setWalletGridLoading(message) {
  const grid = getWalletGrid();
  if (!grid) return;
  grid.setAttribute('aria-busy', 'true');
  grid.replaceChildren();
  const status = document.createElement('p');
  status.className = 'it-wallet-list-state it-wallet-list-state--loading col-12 text-center';
  status.setAttribute('role', 'status');
  status.textContent = message;
  grid.appendChild(status);
}

function setWalletGridError(message) {
  const grid = getWalletGrid();
  if (!grid) return;
  grid.setAttribute('aria-busy', 'false');
  grid.replaceChildren();
  const alert = document.createElement('p');
  alert.className = 'it-wallet-list-state it-wallet-list-state--error col-12 text-center';
  alert.setAttribute('role', 'alert');
  alert.textContent = message;
  grid.appendChild(alert);
}

setWalletGridLoading(WALLET_LOADING_FALLBACK);

function getBasePath() {
  const path = window.location.pathname;
  const lastSlash = path.lastIndexOf('/');
  return lastSlash >= 0 ? path.substring(0, lastSlash + 1) : '/';
}

function loadDocument(resource) {
  const regionEl = document.getElementById('header-region-name');
  if (regionEl) regionEl.textContent = resource?.header?.region_name ?? '';
  const skipNav = document.querySelector('.it-skip-links');
  if (skipNav) skipNav.setAttribute('aria-label', resource?.skip_links?.nav_label ?? 'Collegamenti di salto');
  const skipMain = document.getElementById('skip-main');
  if (skipMain) skipMain.textContent = resource?.skip_links?.main_content ?? 'Vai al contenuto principale';
  const skipFooter = document.getElementById('skip-footer');
  if (skipFooter) skipFooter.textContent = resource?.skip_links?.footer ?? 'Vai al piè di pagina';
  const eidTitle = document.getElementById('eid-title');
  const logoText = resource?.titles?.logo_title ?? 'Il tuo logo';
  if (eidTitle) eidTitle.textContent = logoText;
  const headerLogoText = document.getElementById('header-logo-text');
  if (headerLogoText) headerLogoText.textContent = logoText;
  const headerLogo = document.getElementById('header-logo');
  if (headerLogo instanceof SVGElement && eidTitle) {
    headerLogo.setAttribute('role', 'img');
    headerLogo.setAttribute('aria-labelledby', 'eid-title');
  }
  const tabTitle = document.getElementById('tab-title');
  if (tabTitle) tabTitle.textContent = resource?.titles?.page_title ?? '';
  const pageTitle = document.getElementById('page-title');
  if (pageTitle) pageTitle.textContent = resource?.titles?.page_title ?? '';
  const pageSubtitle = document.getElementById('page-subtitle');
  if (pageSubtitle) pageSubtitle.textContent = resource?.titles?.page_subtitle ?? '';

  const searchInput = document.getElementById('wallet-search');
  const searchLabel = document.getElementById('wallet-search-label');
  if (searchLabel) searchLabel.textContent = resource?.search?.label ?? 'Cerca wallet per nome';
  if (searchInput) {
    searchInput.removeAttribute('aria-label');
    searchInput.placeholder = resource?.search?.placeholder ?? 'Cerca per nome';
  }
  const searchToggle = document.getElementById('wallet-search-toggle');
  if (searchToggle) {
    searchToggle.setAttribute('aria-label', resource?.search?.toggle_open ?? 'Apri ricerca e ordinamento wallet');
  }
  const searchClearBtn = document.getElementById('search-clear-btn');
  if (searchClearBtn) {
    searchClearBtn.setAttribute('aria-label', resource?.search?.clear_label ?? 'Reset ricerca');
  }
  const searchBtn = document.getElementById('search-btn');
  const searchError = document.getElementById('wallet-search-error');
  if (searchBtn) searchBtn.textContent = resource?.search?.button ?? 'Cerca';
  if (searchError) searchError.textContent = resource?.search?.empty_error ?? 'Inserisci un termine di ricerca';
  const walletNavbarLogo = document.querySelector('.it-wallet-navbar-logo');
  if (walletNavbarLogo) {
    walletNavbarLogo.setAttribute('alt', resource?.titles?.wallet_brand_alt ?? 'IT-Wallet');
  }
  const sortSelect = document.getElementById('wallet-sort');
  if (sortSelect) {
    const options = sortSelect.options;
    if (options[0]) options[0].textContent = resource?.sort?.default ?? 'Ordine predefinito';
    if (options[1]) options[1].textContent = resource?.sort?.az ?? 'Alfabetico A-Z';
    if (options[2]) options[2].textContent = resource?.sort?.za ?? 'Alfabetico Z-A';
  }
  const sortItemDefault = document.getElementById('wallet-sort-item-default');
  if (sortItemDefault) sortItemDefault.textContent = resource?.sort?.default ?? 'Ordine predefinito';
  const sortItemAz = document.getElementById('wallet-sort-item-az');
  if (sortItemAz) sortItemAz.textContent = resource?.sort?.az ?? 'Alfabetico A-Z';
  const sortItemZa = document.getElementById('wallet-sort-item-za');
  if (sortItemZa) sortItemZa.textContent = resource?.sort?.za ?? 'Alfabetico Z-A';
  const sortTrigger = document.getElementById('wallet-sort-trigger');
  const sortLabel = resource?.sort?.trigger_label ?? 'Ordina wallet';
  if (sortTrigger) sortTrigger.setAttribute('aria-label', sortLabel);
  const backLink = document.getElementById('back-link');
  const backText = resource?.nav?.back ?? 'Torna indietro';
  if (backLink) backLink.setAttribute('aria-label', backText);
  const backLabel = document.querySelector('.it-wallet-back-label');
  if (backLabel) {
    backLabel.textContent = typeof backText === 'string' ? backText : 'Torna indietro';
  }

  const footerLegal = document.getElementById('footer-legal');
  const footerPrivacy = document.getElementById('footer-privacy');
  const footerAccess = document.getElementById('footer-accessibility');
  const newWindowHint = resource?.footer?.new_window_hint ?? 'si apre in una nuova finestra';
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
  const pageTitleText = resource?.titles?.page_title ?? '';
  if (pageTitleText) document.title = pageTitleText;
  const metaDescription = resource?.meta?.description ?? '';
  const metaDesc = document.querySelector('meta[name="description"]');
  if (metaDesc && metaDescription) metaDesc.setAttribute('content', metaDescription);
}

function shuffleWallets(wallets) {
  const shuffled = [...wallets];
  for (let i = shuffled.length - 1; i > 0; i -= 1) {
    const j = Math.floor(Math.random() * (i + 1));
    [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
  }
  return shuffled;
}

function sortWallets(wallets, sortValue) {
  if (sortValue === 'az') {
    return [...wallets].sort((a, b) => (a.name || '').localeCompare(b.name || '', undefined, { sensitivity: 'base' }));
  }
  if (sortValue === 'za') {
    return [...wallets].sort((a, b) => (b.name || '').localeCompare(a.name || '', undefined, { sensitivity: 'base' }));
  }
  return wallets;
}

/** LIKE-style match: substring, case-insensitive */
function matchesLike(text, query) {
  if (!query || !query.trim()) return true;
  const q = query.trim().toLowerCase();
  const t = (text || '').toLowerCase();
  return t.includes(q);
}

function filterWallets(wallets, query) {
  if (!query || !query.trim()) return wallets;
  const q = query.trim().toLowerCase();
  return wallets.filter((w) => {
    const idMatch = matchesLike(w.id, q);
    const nameMatch = matchesLike(w.name, q);
    return idMatch || nameMatch;
  });
}

function buildWalletUri(uri) {
  const params = new URLSearchParams(window.location.search);
  // Default return to proxy's disco callback when missing (e.g. direct access or params lost)
  const returnUrl = params.get('return') || (window.location.origin + '/Saml2/disco');
  // For wallet flow, entityID must be 'wallet' to route to OpenID4VP; do not overwrite with page params
  const entityID = uri.includes('entityID=wallet') ? 'wallet' : (params.get('entityID') || 'wallet');
  try {
    const u = new URL(uri, window.location.origin);
    u.searchParams.set('return', returnUrl);
    u.searchParams.set('entityID', entityID);
    return u.toString();
  } catch {
    return uri + (uri.includes('?') ? '&' : '?') + 'return=' + encodeURIComponent(returnUrl) + '&entityID=' + encodeURIComponent(entityID);
  }
}

function walletCardSlug(wallet) {
  const raw = wallet.id || wallet.name || 'wallet';
  return String(raw).toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '') || 'wallet';
}

function createWalletCard(wallet, resource, basePath) {
  const col = document.createElement('div');
  col.className = 'col-12 col-lg-6 it-wallet-grid-col';
  const card = document.createElement('article');
  card.className = 'it-card shadow it-wallet-card';

  const body = document.createElement('div');
  body.className = 'it-card-body d-flex flex-column justify-content-center';

  const cardLink = document.createElement('a');
  cardLink.href = buildWalletUri(wallet.uri);
  cardLink.className = 'it-wallet-card-hit';

  const row = document.createElement('div');
  row.className = 'd-flex align-items-center w-100 it-wallet-card-main-row';

  const left = document.createElement('div');
  left.className = 'it-wallet-card-left';
  const img = document.createElement('img');
  img.src = (wallet.logo_uri || '').startsWith('/') ? wallet.logo_uri : basePath + (wallet.logo_uri || '');
  img.alt = '';
  img.setAttribute('aria-hidden', 'true');
  img.className = 'wallet-card-logo flex-shrink-0';
  left.appendChild(img);

  const title = document.createElement('h2');
  title.id = `it-wallet-card-title-${walletCardSlug(wallet)}`;
  title.className = 'it-card-title mb-0 it-wallet-card-title text-start h5';
  title.textContent = wallet.name;
  card.setAttribute('aria-labelledby', title.id);
  left.appendChild(title);

  const arrow = document.createElement('span');
  arrow.className = 'it-wallet-card-arrow flex-shrink-0';
  arrow.setAttribute('aria-hidden', 'true');
  const arrowSvg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
  arrowSvg.setAttribute('class', 'icon');
  const arrowUse = document.createElementNS('http://www.w3.org/2000/svg', 'use');
  arrowUse.setAttribute('href', basePath + 'svg/sprites.svg#it-arrow-right');
  arrowSvg.appendChild(arrowUse);
  arrow.appendChild(arrowSvg);

  row.appendChild(left);
  row.appendChild(arrow);
  cardLink.appendChild(row);
  body.appendChild(cardLink);

  if (SHOW_CARD_LEARN_MORE) {
    const learnMoreLabel = resource?.learn_more?.link ?? 'Scopri di più';
    const descContainer = document.createElement('div');
    descContainer.className = 'wallet-learn-more';

    const toggle = document.createElement('a');
    toggle.href = '#';
    toggle.className = 'eid-learn-more-toggle';
    toggle.textContent = learnMoreLabel;

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

    const desc = document.createElement('p');
    desc.className = 'text-muted small mb-0 mt-2';
    desc.textContent = wallet.description || '';

    const howToGetLabel = resource?.learn_more?.how_to_get ?? 'Scopri come ottenerlo';
    const howToGetLink = document.createElement('a');
    howToGetLink.href = wallet.how_to_get_url || '#';
    howToGetLink.className = 'wallet-how-to-get-link text-decoration-none d-inline-flex align-items-center gap-1 mt-2';
    howToGetLink.textContent = howToGetLabel;
    const extIcon = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    extIcon.setAttribute('class', 'icon icon-sm ms-1');
    extIcon.setAttribute('aria-hidden', 'true');
    const useEl = document.createElementNS('http://www.w3.org/2000/svg', 'use');
    useEl.setAttribute('href', basePath + 'svg/sprites.svg#it-external-link');
    extIcon.appendChild(useEl);
    howToGetLink.appendChild(extIcon);

    const contentWrapper = document.createElement('div');
    contentWrapper.className = 'eid-learn-more-content';
    contentWrapper.appendChild(desc);
    contentWrapper.appendChild(howToGetLink);

    toggle.addEventListener('click', (e) => {
      e.preventDefault();
      e.stopPropagation();
      const box = toggle.closest('.it-card');
      const isExpanded = toggle.classList.contains('expanded');
      if (!isExpanded) {
        toggle.classList.add('expanded');
        contentWrapper.classList.add('is-open');
        if (box) box.style.height = 'auto';
      } else {
        toggle.classList.remove('expanded');
        contentWrapper.classList.remove('is-open');
        if (box) box.style.height = '';
      }
    });

    descContainer.appendChild(toggle);
    descContainer.appendChild(contentWrapper);
    body.appendChild(descContainer);
  }

  card.appendChild(body);
  col.appendChild(card);
  return col;
}

function renderWallets(wallets, resource, basePath) {
  const grid = getWalletGrid();
  if (!grid) return;
  grid.setAttribute('aria-busy', 'false');
  grid.innerHTML = '';
  grid.classList.toggle('it-wallet-grid-single', wallets.length === 1);
  if (wallets.length === 0) {
    const noResultsLabel = resource?.search?.no_results ?? 'Nessun risultato';
    const emptyDiv = document.createElement('div');
    emptyDiv.className = 'col-12 d-flex flex-column align-items-center justify-content-center py-5';
    const img = document.createElement('img');
    img.src = basePath + 'img/error-icon.svg';
    img.alt = '';
    img.className = 'it-wallet-no-results-icon mb-3';
    img.setAttribute('aria-hidden', 'true');
    const msg = document.createElement('p');
    msg.className = 'it-wallet-no-results-text mb-0';
    msg.setAttribute('role', 'status');
    msg.textContent = noResultsLabel;
    emptyDiv.appendChild(img);
    emptyDiv.appendChild(msg);
    grid.appendChild(emptyDiv);
  } else {
    wallets.forEach((w) => {
      grid.appendChild(createWalletCard(w, resource, basePath));
    });
  }
}

function getWalletResource() {
  const lang = i18next.language || 'it';
  let resource = i18next.getResourceBundle(lang, 'translation');
  if (!resource) {
    resource = i18next.store?.getDataByLanguage?.(lang)?.translation ?? i18next.store?.data?.[lang]?.translation ?? {};
  }
  return resource;
}

function setupBackLink() {
  const backLink = document.getElementById('back-link');
  if (backLink) {
    const params = new URLSearchParams(window.location.search);
    const search = params.toString();
    const discoUrl = '../discovery-page/disco.html';
    backLink.href = search ? discoUrl + '?' + search : discoUrl;
  }
}

function walletResultsStatusMessage(resource, count, context) {
  const search = resource?.search ?? {};
  if (count === 0) {
    return search.results_none ?? search.no_results ?? 'Nessun risultato trovato';
  }
  if (context === 'clear') {
    return (search.results_reset ?? 'Ricerca azzerata, {{count}} wallet disponibili').replace('{{count}}', String(count));
  }
  const template = count === 1
    ? (search.results_one ?? '{{count}} risultato trovato')
    : (search.results_many ?? '{{count}} risultati trovati');
  return template.replace('{{count}}', String(count));
}

function announceWalletStatusMessage(message) {
  const status = document.getElementById('wallet-results-status');
  if (!status) return;
  status.textContent = '';
  requestAnimationFrame(() => {
    status.textContent = message;
  });
}

function announceWalletResults(resource, count, context) {
  announceWalletStatusMessage(walletResultsStatusMessage(resource, count, context));
}

async function loadItWalletPage() {
  const basePath = getBasePath();
  const resource = getWalletResource();
  loadDocument(resource);
  setWalletGridLoading(walletLoadingMessage(resource));

  let wallets = [];
  let loadFailed = false;
  try {
    const resp = await fetch(basePath + 'data/it-wallets.json');
    if (!resp.ok) {
      loadFailed = true;
      console.error('Error loading it-wallets.json: HTTP', resp.status);
    } else {
      const data = await resp.json();
      wallets = data.immediate_subordinate_entities || [];
    }
  } catch (err) {
    loadFailed = true;
    console.error('Error loading it-wallets.json:', err);
  }

  if (loadFailed) {
    setWalletGridError(walletErrorMessage(resource));
    document.getElementById('wallet-controls')?.classList.add('d-none');
    const titleActions = document.getElementById('wallet-title-actions');
    if (titleActions) titleActions.hidden = true;
    setupBackLink();
    return;
  }

  const defaultWalletOrder = shuffleWallets(wallets);
  const searchInput = document.getElementById('wallet-search');
  const searchBtn = document.getElementById('search-btn');
  const searchForm = document.getElementById('wallet-search-form');
  const searchClearBtn = document.getElementById('search-clear-btn');
  const sortSelect = document.getElementById('wallet-sort');
  const sortTrigger = document.getElementById('wallet-sort-trigger');
  const sortMenu = document.getElementById('wallet-sort-menu');
  const sortMenuItems = Array.from(document.querySelectorAll('.it-wallet-sort-menu-item'));
  const controls = document.getElementById('wallet-controls');
  const titleActions = document.getElementById('wallet-title-actions');
  const searchToggle = document.getElementById('wallet-search-toggle');
  const iconSearchOpen = document.getElementById('wallet-search-toggle-icon-open');
  const iconSearchClose = document.getElementById('wallet-search-toggle-icon-close');
  const showControls = defaultWalletOrder.length >= SEARCH_MIN_WALLETS;
  controls?.classList.toggle('d-none', !showControls);
  if (titleActions) titleActions.hidden = !showControls;
  let appliedQuery = '';

  function isWalletDesktopLayout() {
    return window.matchMedia('(min-width: 992px)').matches;
  }

  function syncMobilePanelUi(open) {
    if (!searchToggle) return;
    searchToggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    const searchLabels = getWalletResource()?.search ?? {};
    searchToggle.setAttribute(
      'aria-label',
      open
        ? (searchLabels.toggle_close ?? 'Chiudi ricerca e ordinamento wallet')
        : (searchLabels.toggle_open ?? 'Apri ricerca e ordinamento wallet')
    );
    if (iconSearchOpen) {
      iconSearchOpen.hidden = open;
      iconSearchOpen.style.display = open ? 'none' : '';
      iconSearchOpen.setAttribute('aria-hidden', 'true');
    }
    if (iconSearchClose) {
      iconSearchClose.hidden = !open;
      iconSearchClose.style.display = open ? 'block' : 'none';
      iconSearchClose.setAttribute('aria-hidden', 'true');
    }
  }

  function setMobilePanelOpen(open) {
    if (!controls || !showControls) return;
    if (isWalletDesktopLayout()) return;
    const resource = getWalletResource();
    controls.classList.toggle('is-mobile-panel-open', open);
    controls.hidden = !open;
    syncMobilePanelUi(open);
    if (open) {
      announceWalletStatusMessage(resource?.search?.panel_open ?? 'Strumenti di ricerca e ordinamento visualizzati');
      if (searchInput) {
        requestAnimationFrame(() => searchInput.focus());
      }
    } else {
      announceWalletStatusMessage(resource?.search?.panel_closed ?? 'Strumenti di ricerca e ordinamento nascosti');
      if (searchToggle) {
        requestAnimationFrame(() => searchToggle.focus());
      }
    }
  }

  function resetMobilePanelForDesktop() {
    if (!controls) return;
    controls.classList.remove('is-mobile-panel-open');
    controls.hidden = false;
    syncMobilePanelUi(false);
  }

  function applyFiltersAndSort(options = {}) {
    const { announce = false, announceContext = 'search' } = options;
    const res = getWalletResource();
    const query = showControls ? appliedQuery : '';
    const sortValue = showControls ? (sortSelect?.value || 'default') : 'default';
    const filtered = filterWallets(defaultWalletOrder, query);
    const sorted = sortWallets(filtered, sortValue);
    renderWallets(sorted, res, basePath);
    searchClearBtn?.classList.toggle('d-none', !(searchInput?.value || '').trim());
    if (announce) {
      announceWalletResults(res, sorted.length, announceContext);
    }
  }

  function clearSearchError() {
    const errorEl = document.getElementById('wallet-search-error');
    if (errorEl) errorEl.hidden = true;
    if (searchInput) {
      searchInput.removeAttribute('aria-invalid');
      searchInput.removeAttribute('aria-describedby');
    }
  }

  function showSearchError() {
    const resource = getWalletResource();
    const errorEl = document.getElementById('wallet-search-error');
    const message = resource?.search?.empty_error ?? 'Inserisci un termine di ricerca';
    if (errorEl) {
      errorEl.textContent = message;
      errorEl.hidden = false;
    }
    if (searchInput) {
      searchInput.setAttribute('aria-invalid', 'true');
      searchInput.setAttribute('aria-describedby', 'wallet-search-error');
      searchInput.focus();
    }
  }

  function setSearchAppliedVisual(active) {
    searchBtn?.classList.toggle('is-search-applied', !!active);
  }

  function syncSearchButtonState() {
    if (searchBtn) searchBtn.disabled = false;
    const hasQuery = !!(searchInput?.value || '').trim();
    if (hasQuery) {
      clearSearchError();
    } else {
      setSearchAppliedVisual(false);
    }
  }

  function closeSortMenu(restoreFocus = false) {
    if (!sortMenu || !sortTrigger) return;
    sortMenu.hidden = true;
    sortTrigger.setAttribute('aria-expanded', 'false');
    sortMenuItems.forEach((item) => {
      item.tabIndex = -1;
    });
    if (restoreFocus) {
      requestAnimationFrame(() => sortTrigger.focus());
    }
  }

  function getActiveSortMenuIndex() {
    const activeIndex = sortMenuItems.findIndex((item) => item.classList.contains('is-active'));
    return activeIndex >= 0 ? activeIndex : 0;
  }

  function focusSortMenuItem(index) {
    if (sortMenuItems.length === 0) return;
    const normalized = ((index % sortMenuItems.length) + sortMenuItems.length) % sortMenuItems.length;
    sortMenuItems.forEach((item, itemIndex) => {
      item.tabIndex = itemIndex === normalized ? 0 : -1;
    });
    sortMenuItems[normalized].focus();
  }

  function openSortMenu(focusIndex) {
    if (!sortMenu || !sortTrigger) return;
    sortMenu.hidden = false;
    sortTrigger.setAttribute('aria-expanded', 'true');
    focusSortMenuItem(typeof focusIndex === 'number' ? focusIndex : getActiveSortMenuIndex());
  }

  function setSortMenuSelection(value) {
    sortMenuItems.forEach((item) => {
      const isActive = item.dataset.value === value;
      item.classList.toggle('is-active', isActive);
      item.setAttribute('aria-checked', isActive ? 'true' : 'false');
    });
  }

  function setSortValue(value) {
    if (!sortSelect) return;
    sortSelect.value = value;
    setSortMenuSelection(value);
    applyFiltersAndSort({ announce: true, announceContext: 'search' });
  }

  if (searchInput) {
    searchInput.oninput = () => {
      searchClearBtn?.classList.toggle('d-none', !(searchInput.value || '').trim());
      setSearchAppliedVisual(false);
      syncSearchButtonState();
    };
  }
  if (searchForm) {
    searchForm.addEventListener('submit', (event) => {
      event.preventDefault();
      const query = (searchInput?.value || '').trim();
      if (!query) {
        showSearchError();
        return;
      }
      clearSearchError();
      appliedQuery = query;
      setSearchAppliedVisual(true);
      applyFiltersAndSort({ announce: true, announceContext: 'search' });
    });
  }
  if (sortSelect) {
    sortSelect.onchange = () => {
      setSortMenuSelection(sortSelect.value || 'default');
      applyFiltersAndSort({ announce: true, announceContext: 'search' });
    };
  }
  if (sortTrigger && sortMenu) {
    sortTrigger.onclick = (event) => {
      event.stopPropagation();
      if (sortMenu.hidden) {
        openSortMenu(getActiveSortMenuIndex());
      } else {
        closeSortMenu(true);
      }
    };
    sortTrigger.addEventListener('keydown', (event) => {
      if (event.key === 'ArrowDown') {
        event.preventDefault();
        if (sortMenu.hidden) {
          openSortMenu(getActiveSortMenuIndex());
        } else {
          focusSortMenuItem(getActiveSortMenuIndex() + 1);
        }
        return;
      }
      if (event.key === 'ArrowUp' && sortMenu.hidden) {
        event.preventDefault();
        openSortMenu(sortMenuItems.length - 1);
      }
    });
    sortMenu.addEventListener('keydown', (event) => {
      if (sortMenu.hidden || sortMenuItems.length === 0) return;
      const currentIndex = sortMenuItems.findIndex((item) => item === document.activeElement);
      const baseIndex = currentIndex >= 0 ? currentIndex : getActiveSortMenuIndex();

      if (event.key === 'ArrowDown') {
        event.preventDefault();
        focusSortMenuItem(baseIndex + 1);
      } else if (event.key === 'ArrowUp') {
        event.preventDefault();
        focusSortMenuItem(baseIndex - 1);
      } else if (event.key === 'Home') {
        event.preventDefault();
        focusSortMenuItem(0);
      } else if (event.key === 'End') {
        event.preventDefault();
        focusSortMenuItem(sortMenuItems.length - 1);
      } else if (event.key === 'Enter' || event.key === ' ') {
        const activeItem = document.activeElement;
        if (activeItem instanceof HTMLElement && activeItem.classList.contains('it-wallet-sort-menu-item')) {
          event.preventDefault();
          activeItem.click();
        }
      }
    });
  }
  if (sortMenuItems.length > 0) {
    sortMenuItems.forEach((item) => {
      item.tabIndex = -1;
      item.addEventListener('click', () => {
        const value = item.dataset.value || 'default';
        setSortValue(value);
        closeSortMenu(true);
      });
    });
  }
  if (searchClearBtn) {
    searchClearBtn.onclick = () => {
      if (searchInput) {
        searchInput.value = '';
        searchInput.focus();
      }
      clearSearchError();
      appliedQuery = '';
      syncSearchButtonState();
      applyFiltersAndSort({ announce: true, announceContext: 'clear' });
    };
  }

  if (searchToggle) {
    searchToggle.onclick = () => {
      if (!showControls || isWalletDesktopLayout()) return;
      const next = !controls?.classList.contains('is-mobile-panel-open');
      setMobilePanelOpen(next);
    };
  }
  window.__itWalletCloseMobilePanel = () => {
    if (!controls?.classList.contains('is-mobile-panel-open')) return;
    setMobilePanelOpen(false);
  };
  window.__itWalletCloseSortMenu = () => closeSortMenu(true);
  if (!window.__itWalletEscapeListenerBound) {
    window.__itWalletEscapeListenerBound = true;
    document.addEventListener('keydown', (event) => {
      if (event.key !== 'Escape') return;
      const menu = document.getElementById('wallet-sort-menu');
      const trigger = document.getElementById('wallet-sort-trigger');
      if (menu && trigger && !menu.hidden) {
        if (typeof window.__itWalletCloseSortMenu === 'function') {
          window.__itWalletCloseSortMenu();
        } else {
          menu.hidden = true;
          trigger.setAttribute('aria-expanded', 'false');
          trigger.focus();
        }
        event.preventDefault();
        return;
      }
      if (window.matchMedia('(min-width: 992px)').matches) return;
      const panel = document.getElementById('wallet-controls');
      if (!panel?.classList.contains('is-mobile-panel-open')) return;
      if (typeof window.__itWalletCloseMobilePanel === 'function') {
        window.__itWalletCloseMobilePanel();
        event.preventDefault();
      }
    });
  }
  if (!window.__itWalletLayoutListenersBound) {
    window.__itWalletLayoutListenersBound = true;
    window.addEventListener('resize', () => {
      if (isWalletDesktopLayout()) resetMobilePanelForDesktop();
    });
  }
  if (!window.__itWalletSortMenuListenersBound) {
    window.__itWalletSortMenuListenersBound = true;
    document.addEventListener('click', (event) => {
      const menu = document.getElementById('wallet-sort-menu');
      const trigger = document.getElementById('wallet-sort-trigger');
      if (!menu || !trigger || menu.hidden) return;
      const target = event.target;
      if (!(target instanceof Node)) return;
      if (menu.contains(target) || trigger.contains(target)) return;
      if (typeof window.__itWalletCloseSortMenu === 'function') {
        window.__itWalletCloseSortMenu();
      } else {
        menu.hidden = true;
        trigger.setAttribute('aria-expanded', 'false');
        trigger.focus();
      }
    });
  }
  if (isWalletDesktopLayout()) resetMobilePanelForDesktop();
  else {
    syncMobilePanelUi(false);
    if (controls) controls.hidden = true;
  }

  setSortMenuSelection(sortSelect?.value || 'default');
  syncSearchButtonState();
  applyFiltersAndSort();
  setupBackLink();
}

i18next
  .use(i18nextHttpBackend)
  .init({
    lng: 'it',
    fallbackLng: 'it',
    backend: { loadPath: getBasePath() + 'locales/it-wallet-{{lng}}.json' }
  })
  .then(() => {
    if (typeof window.initHeaderLangDropdown === 'function') {
      window.initHeaderLangDropdown(i18next, { afterLanguageChange: () => loadItWalletPage() });
    }
    return loadItWalletPage();
  })
  .catch((err) => {
    console.error('Error loading it-wallet page:', err);
    setWalletGridError(WALLET_ERROR_FALLBACK);
  });

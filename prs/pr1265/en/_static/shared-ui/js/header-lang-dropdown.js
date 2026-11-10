/**
 * Language switcher aligned with developers.italia.it (slim header dropdown + link-list).
 */
(function (global) {
  /** Spazio tra trigger e menu: il margin sul .dropdown-menu è ignorato da Popper (usa transform). */
  var MENU_OFFSET_PX = 24;

  var LANG_DISPLAY = { it: 'Italiano', en: 'English' };
  var boundI18next = null;

  function normalizeLang(lng) {
    return (lng || 'it').split('-')[0] === 'en' ? 'en' : 'it';
  }

  function setDocumentLanguage(lng) {
    var code = normalizeLang(lng);
    if (global.document && global.document.documentElement) {
      global.document.documentElement.lang = code;
    }
    return code;
  }

  function langActiveHint(lng) {
    if (boundI18next && typeof boundI18next.t === 'function') {
      return boundI18next.t('header.lang_active_hint');
    }
    return normalizeLang(lng) === 'en' ? 'active language:' : 'lingua attiva:';
  }

  function triggerAriaLabel(selectedCode) {
    var name = LANG_DISPLAY[selectedCode] || LANG_DISPLAY.it;
    if (boundI18next && typeof boundI18next.t === 'function') {
      return boundI18next.t('header.lang_trigger', { name: name });
    }
    if (selectedCode === 'en') {
      return 'Language selection, ' + name + ' selected';
    }
    return 'Selezione lingua, ' + name + ' selezionata';
  }

  function bindLangMenuPopper(toggle) {
    if (!global.bootstrap || !global.bootstrap.Dropdown || !toggle) return;
    var existing = bootstrap.Dropdown.getInstance(toggle);
    if (existing) existing.dispose();
    new bootstrap.Dropdown(toggle, {
      popperConfig: function (defaultConfig) {
        var base = defaultConfig || {};
        var mods = Array.isArray(base.modifiers) ? base.modifiers.slice() : [];
        var found = false;
        mods = mods.map(function (m) {
          if (m.name !== 'offset') return m;
          found = true;
          var opt = Object.assign({}, m.options || {});
          opt.offset = [0, MENU_OFFSET_PX];
          return Object.assign({}, m, { options: opt });
        });
        if (!found) {
          mods.push({
            name: 'offset',
            options: { offset: [0, MENU_OFFSET_PX] },
          });
        }
        return Object.assign({}, base, { modifiers: mods });
      },
    });
  }

  function syncRoot(root, lng) {
    var code = normalizeLang(lng);
    var label = root.querySelector('.it-header-lang-label');
    if (label) label.textContent = code === 'en' ? 'EN' : 'ITA';

    var activeHint = root.querySelector('#header-lang-active-hint');
    if (activeHint) activeHint.textContent = langActiveHint(code);

    var toggle = root.querySelector('[data-bs-toggle="dropdown"]');
    if (toggle) {
      toggle.setAttribute('aria-label', triggerAriaLabel(code));
    }

    var menu = root.querySelector('.link-list');
    if (menu && !menu.getAttribute('role')) {
      menu.setAttribute('role', 'menu');
    }

    root.querySelectorAll('.it-lang-option').forEach(function (a) {
      var optionLang = a.getAttribute('data-lang');
      var isActive = optionLang === code;
      a.classList.toggle('active', isActive);
      a.setAttribute('role', 'menuitemradio');
      a.setAttribute('aria-checked', isActive ? 'true' : 'false');
      if (isActive) {
        a.setAttribute('aria-current', 'true');
      } else {
        a.removeAttribute('aria-current');
      }
    });
  }

  function syncAllLangDropdowns(lng) {
    setDocumentLanguage(lng);
    document.querySelectorAll('.it-header-lang-dropdown').forEach(function (root) {
      syncRoot(root, lng);
    });
  }

  global.initHeaderLangDropdown = function (i18next, options) {
    if (!i18next || typeof i18next.changeLanguage !== 'function') return;
    boundI18next = i18next;
    options = options || {};
    var afterChange = options.afterLanguageChange;

    if (!global.__headerLangDropdownLanguageListener) {
      global.__headerLangDropdownLanguageListener = true;
      i18next.on('languageChanged', function (lng) {
        syncAllLangDropdowns(lng);
      });
    }

    syncAllLangDropdowns(i18next.language);

    document.querySelectorAll('.it-header-lang-dropdown').forEach(function (root) {
      if (root.dataset.langDropdownBound === '1') return;
      root.dataset.langDropdownBound = '1';

      var toggle = root.querySelector('[data-bs-toggle="dropdown"]');
      if (!toggle) return;

      bindLangMenuPopper(toggle);

      root.querySelectorAll('.it-lang-option').forEach(function (a) {
        a.addEventListener('click', function (e) {
          e.preventDefault();
          var lng = a.getAttribute('data-lang');
          if (!lng) return;
          if (global.bootstrap && toggle) {
            var dd = bootstrap.Dropdown.getInstance(toggle);
            if (dd) dd.hide();
          }
          i18next.changeLanguage(lng).then(function () {
            setDocumentLanguage(lng);
            if (typeof afterChange === 'function') afterChange(lng);
          });
        });
      });
    });
  };
})(typeof window !== 'undefined' ? window : this);

/**
 * IT-Wallet docs theme — Bootstrap Italia + Sphinx helpers.
 */
(function () {
  "use strict";

  var LANG_MENU_OFFSET_PX = 24;
  var MOBILE_MQ = window.matchMedia("(max-width: 991.98px)");
  var BRIGHTNESS_STORAGE_KEY = "it-docs-brightness";
  var BRIGHTNESS_MODES = ["light", "middle", "black"];

  function bindHeaderDropdownPopper(toggle) {
    if (!window.bootstrap || !window.bootstrap.Dropdown || !toggle) return;
    var existing = window.bootstrap.Dropdown.getInstance(toggle);
    if (existing) existing.dispose();
    new window.bootstrap.Dropdown(toggle, {
      popperConfig: function (defaultConfig) {
        var base = defaultConfig || {};
        var mods = Array.isArray(base.modifiers) ? base.modifiers.slice() : [];
        var found = false;
        mods = mods.map(function (modifier) {
          if (modifier.name !== "offset") return modifier;
          found = true;
          var options = Object.assign({}, modifier.options || {});
          options.offset = [0, LANG_MENU_OFFSET_PX];
          return Object.assign({}, modifier, { options: options });
        });
        if (!found) {
          mods.push({
            name: "offset",
            options: { offset: [0, LANG_MENU_OFFSET_PX] },
          });
        }
        return Object.assign({}, base, { modifiers: mods });
      },
    });
  }

  function initLangDropdowns() {
    document.querySelectorAll(".it-header-lang-dropdown").forEach(function (root) {
      var toggle = root.querySelector('[data-bs-toggle="dropdown"]');
      if (toggle) bindHeaderDropdownPopper(toggle);
    });
  }

  function updateBrightnessUi(mode) {
    document.querySelectorAll(".it-docs-brightness-option").forEach(function (button) {
      var isActive = button.getAttribute("data-it-docs-brightness") === mode;
      button.classList.toggle("active", isActive);
      button.setAttribute("aria-checked", isActive ? "true" : "false");
    });

    var currentLabel = document.getElementById("it-docs-brightness-current-label");
    var activeOption = document.querySelector(
      '.it-docs-brightness-option[data-it-docs-brightness="' + mode + '"] span'
    );
    if (currentLabel && activeOption) {
      currentLabel.textContent = activeOption.textContent;
    }
  }

  function setBrightness(mode, options) {
    if (BRIGHTNESS_MODES.indexOf(mode) === -1) {
      mode = "light";
    }

    if (mode === "light") {
      document.documentElement.removeAttribute("data-it-docs-brightness");
    } else {
      document.documentElement.setAttribute("data-it-docs-brightness", mode);
    }

    updateBrightnessUi(mode);

    var shouldPersist = !options || options.persist !== false;
    if (!shouldPersist) return;

    try {
      if (mode === "light") {
        localStorage.removeItem(BRIGHTNESS_STORAGE_KEY);
      } else {
        localStorage.setItem(BRIGHTNESS_STORAGE_KEY, mode);
      }
    } catch (error) {
      /* ignore storage errors */
    }
  }

  function initBrightnessToggle() {
    var storedMode = "light";
    try {
      var stored = localStorage.getItem(BRIGHTNESS_STORAGE_KEY);
      if (stored && BRIGHTNESS_MODES.indexOf(stored) !== -1) {
        storedMode = stored;
      }
    } catch (error) {
      /* ignore storage errors */
    }

    setBrightness(storedMode, { persist: false });

    document.querySelectorAll(".it-docs-brightness-option").forEach(function (button) {
      button.addEventListener("click", function () {
        setBrightness(button.getAttribute("data-it-docs-brightness"));
        var toggle = document.getElementById("it-docs-brightness-toggle");
        if (toggle && window.bootstrap && window.bootstrap.Dropdown) {
          var dropdown = window.bootstrap.Dropdown.getInstance(toggle);
          if (dropdown) dropdown.hide();
        }
      });
    });

    var toggle = document.getElementById("it-docs-brightness-toggle");
    if (toggle) bindHeaderDropdownPopper(toggle);
  }

  function markCurrentLocalTocLink() {
    var hash = window.location.hash;
    var links = document.querySelectorAll(".it-docs-local-toc a");
    links.forEach(function (link) {
      link.classList.remove("active");
      if (hash && link.getAttribute("href") === hash) {
        link.classList.add("active");
      }
    });
    if (!hash && links.length) {
      links[0].classList.add("active");
    }
    syncLocalNavScroll();
  }

  function syncLocalNavScroll() {
    var container = document.querySelector(".it-docs-navscroll-col .it-docs-navscroll-sticky");
    if (!container) return;

    var activeLink = document.querySelector(".it-docs-local-toc a.active");
    if (activeLink) {
      var containerTop = container.getBoundingClientRect().top;
      var linkTop = activeLink.getBoundingClientRect().top;
      container.scrollTop += linkTop - containerTop;
      return;
    }

    container.scrollTop = 0;
  }

  function getSphinxTocContainer() {
    return document.querySelector(".it-docs-sidebar-col .menu-wrapper.it-docs-menu-scroll");
  }

  function getCurrentSphinxTocLink() {
    var toc = document.querySelector(".it-docs-sidebar-col .it-docs-sphinx-toc");
    if (!toc) return null;
    var currentLinks = toc.querySelectorAll("a.current");
    if (!currentLinks.length) return null;
    return currentLinks[currentLinks.length - 1];
  }

  function syncSphinxTocScroll() {
    var container = getSphinxTocContainer();
    if (!container) return;

    var currentLink = getCurrentSphinxTocLink();
    if (currentLink) {
      var containerTop = container.getBoundingClientRect().top;
      var linkTop = currentLink.getBoundingClientRect().top;
      container.scrollTop += linkTop - containerTop;
      return;
    }

    container.scrollTop = 0;
  }

  function initSphinxTocScroll() {
    window.requestAnimationFrame(function () {
      syncSphinxTocScroll();
      syncLocalNavScroll();
    });
    window.addEventListener("resize", function () {
      syncSphinxTocScroll();
      syncLocalNavScroll();
    });
    MOBILE_MQ.addEventListener("change", function () {
      syncSphinxTocScroll();
      syncLocalNavScroll();
    });
    document.querySelectorAll('[data-it-docs-nav-target="#itDocsPrimaryNav"]').forEach(function (toggler) {
      toggler.addEventListener("click", function () {
        window.requestAnimationFrame(syncSphinxTocScroll);
      });
    });
  }

  function isMobileViewport() {
    return MOBILE_MQ.matches;
  }

  function getNavPanelToggler(panel) {
    if (!panel || !panel.id) return null;
    return document.querySelector('[data-it-docs-nav-target="#' + panel.id + '"]');
  }

  function closeNavPanel(panel) {
    if (!panel) return;
    panel.classList.remove("expanded");
    var toggler = getNavPanelToggler(panel);
    if (toggler) {
      toggler.setAttribute("aria-expanded", "false");
    }
  }

  function closeAllNavPanels() {
    document.querySelectorAll(".navbar-collapsable.expanded").forEach(closeNavPanel);
    document.body.classList.remove("it-docs-nav-open");
  }

  function syncNavPanelState(panel) {
    var isOpen = panel.classList.contains("expanded");
    var toggler = getNavPanelToggler(panel);
    if (toggler) {
      toggler.setAttribute("aria-expanded", isOpen ? "true" : "false");
    }

    if (!isMobileViewport()) {
      document.body.classList.remove("it-docs-nav-open");
      return;
    }

    var anyOpen = document.querySelector(".navbar-collapsable.expanded");
    document.body.classList.toggle("it-docs-nav-open", Boolean(anyOpen));

    if (isOpen) {
      var closeBtn = panel.querySelector(".close-menu");
      if (closeBtn) closeBtn.focus();
    }
  }

  function initMobileNavPanels() {
    document.querySelectorAll("[data-it-docs-nav-toggle]").forEach(function (toggler) {
      toggler.addEventListener("click", function (event) {
        if (!isMobileViewport()) return;
        event.preventDefault();
        var selector = toggler.getAttribute("data-it-docs-nav-target");
        var panel = selector ? document.querySelector(selector) : null;
        if (!panel) return;

        var willOpen = !panel.classList.contains("expanded");
        closeAllNavPanels();
        if (willOpen) {
          panel.classList.add("expanded");
        }
        syncNavPanelState(panel);
      });
    });

    document.querySelectorAll(".navbar-collapsable").forEach(function (panel) {
      var observer = new MutationObserver(function () {
        syncNavPanelState(panel);
      });
      observer.observe(panel, {
        attributes: true,
        attributeFilter: ["class"],
      });

      panel.querySelectorAll(".overlay, .close-menu").forEach(function (control) {
        control.addEventListener("click", function () {
          if (!isMobileViewport()) return;
          closeNavPanel(panel);
        });
      });
    });

    document.addEventListener("keydown", function (event) {
      if (event.key !== "Escape" || !isMobileViewport()) return;
      closeAllNavPanels();
      var openToggler = document.querySelector(
        '[data-it-docs-nav-toggle][aria-expanded="true"]'
      );
      if (openToggler) openToggler.focus();
    });

    MOBILE_MQ.addEventListener("change", function () {
      if (!isMobileViewport()) {
        closeAllNavPanels();
      }
    });
  }

  function initFooterExternalLinks() {
    var hint =
      document.documentElement.lang && document.documentElement.lang.indexOf("it") === 0
        ? "si apre in una nuova scheda"
        : "opens in a new tab";
    document
      .querySelectorAll("#footer-partners-nav a[target='_blank']")
      .forEach(function (link) {
      var label = (link.textContent || "").trim();
      var img = link.querySelector("img");
      if (img && img.alt) {
        label = img.alt.trim();
      }
      if (!label || link.getAttribute("aria-label")) return;
      link.setAttribute("aria-label", label + " (" + hint + ")");
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    initLangDropdowns();
    initBrightnessToggle();
    initMobileNavPanels();
    initFooterExternalLinks();
    initSphinxTocScroll();
    markCurrentLocalTocLink();
    window.addEventListener("hashchange", markCurrentLocalTocLink);
  });
})();

/**
 * IT-Wallet docs — search UX: dedupe by page, contextual previews.
 */
(function () {
  "use strict";

  if (typeof Search === "undefined") return;

  var originalPerformSearch = Search._performSearch;
  var originalPerformSearchUi = Search.performSearch;

  function dedupeResultsByDocument(results) {
    var bestByDoc = new Map();

    results.forEach(function (item) {
      var docName = item[0];
      var previous = bestByDoc.get(docName);
      if (!previous) {
        bestByDoc.set(docName, item);
        return;
      }

      var score = item[4];
      var previousScore = previous[4];
      var hasAnchor = Boolean(item[2]);
      var previousHasAnchor = Boolean(previous[2]);

      if (
        score > previousScore ||
        (score === previousScore && hasAnchor && !previousHasAnchor)
      ) {
        bestByDoc.set(docName, item);
      }
    });

    return Array.from(bestByDoc.values()).sort(_orderResultsByScoreThenName);
  }

  Search._performSearch = function (
    query,
    searchTerms,
    excludedTerms,
    highlightTerms,
    objectTerms
  ) {
    var results = originalPerformSearch.call(
      this,
      query,
      searchTerms,
      excludedTerms,
      highlightTerms,
      objectTerms
    );
    return dedupeResultsByDocument(results);
  };

  Search.makeSearchSummary = function (htmlText, keywords, anchor) {
    var text = Search.htmlToText(htmlText, anchor);
    if (!text) return null;

    var textLower = text.toLowerCase();
    var matchPosition = -1;

    Array.from(keywords).forEach(function (keyword) {
      var index = textLower.indexOf(String(keyword).toLowerCase());
      if (index > -1 && (matchPosition === -1 || index < matchPosition)) {
        matchPosition = index;
      }
    });

    var startWithContext = Math.max(matchPosition - 120, 0);
    var excerptLength = 240;
    var top = startWithContext === 0 ? "" : "…";
    var excerpt = text.substr(startWithContext, excerptLength).replace(/\s+/g, " ").trim();
    var tail = startWithContext + excerptLength < text.length ? "…" : "";

    var summary = document.createElement("p");
    summary.classList.add("context", "it-docs-search-snippet");
    summary.textContent = top + excerpt + tail;
    return summary;
  };

  function safeHighlight(node, term, className) {
    if (typeof _highlightText !== "function" || !term) return;
    try {
      _highlightText(node, term, className);
    } catch (error) {
      /* skip highlight for malformed terms */
    }
  }

  function displayItem(item, searchTerms, highlightTerms) {
    var listItem = document.createElement("li");
    listItem.classList.add("it-docs-search-result");

    var docBuilder = DOCUMENTATION_OPTIONS.BUILDER;
    var docFileSuffix = DOCUMENTATION_OPTIONS.FILE_SUFFIX;
    var docLinkSuffix = DOCUMENTATION_OPTIONS.LINK_SUFFIX;
    var showSearchSummary = DOCUMENTATION_OPTIONS.SHOW_SEARCH_SUMMARY;
    var contentRoot = document.documentElement.dataset.content_root;

    var docName = item[0];
    var title = item[1];
    var anchor = item[2];
    var descr = item[3];
    var score = item[4];

    var requestUrl;
    var linkUrl;
    if (docBuilder === "dirhtml") {
      var dirname = docName + "/";
      if (dirname.match(/\/index\/$/)) {
        dirname = dirname.substring(0, dirname.length - 6);
      } else if (dirname === "index/") {
        dirname = "";
      }
      requestUrl = contentRoot + dirname;
      linkUrl = requestUrl;
    } else {
      requestUrl = contentRoot + docName + docFileSuffix;
      linkUrl = docName + docLinkSuffix;
    }

    var linkEl = listItem.appendChild(document.createElement("a"));
    linkEl.classList.add("it-docs-search-result-link");
    linkEl.href = linkUrl + anchor;
    linkEl.dataset.score = score;
    linkEl.innerHTML = title;

    if (descr) {
      var descrEl = listItem.appendChild(document.createElement("span"));
      descrEl.classList.add("it-docs-search-result-descr");
      descrEl.innerHTML = " (" + descr + ")";
      if (typeof SPHINX_HIGHLIGHT_ENABLED !== "undefined" && SPHINX_HIGHLIGHT_ENABLED) {
        highlightTerms.forEach(function (term) {
          safeHighlight(listItem, term, "highlighted");
        });
      }
    } else if (showSearchSummary) {
      fetch(requestUrl)
        .then(function (responseData) {
          if (!responseData.ok) return "";
          return responseData.text();
        })
        .then(function (data) {
          if (!data) return;
          var summary = Search.makeSearchSummary(data, searchTerms, anchor);
          if (summary) listItem.appendChild(summary);
          if (typeof SPHINX_HIGHLIGHT_ENABLED !== "undefined" && SPHINX_HIGHLIGHT_ENABLED) {
            highlightTerms.forEach(function (term) {
              safeHighlight(listItem, term, "highlighted");
            });
          }
        })
        .catch(function () {
          /* ignore fetch errors (offline preview, missing pages) */
        });
    }

    Search.output.appendChild(listItem);
  }

  function finishSearch(resultCount) {
    Search.stopPulse();
    Search.title.innerText = _("Search Results");
    if (!resultCount) {
      Search.status.innerText = Documentation.gettext(
        "Your search did not match any documents. Please make sure that all words are spelled correctly and that you've selected enough categories."
      );
    } else {
      Search.status.innerText = _(
        "Search finished, found ${resultCount} page(s) matching the search query."
      ).replace("${resultCount}", resultCount);
    }
  }

  function displayNextItem(results, resultCount, searchTerms, highlightTerms) {
    if (results.length) {
      displayItem(results.pop(), searchTerms, highlightTerms);
      setTimeout(function () {
        displayNextItem(results, resultCount, searchTerms, highlightTerms);
      }, 5);
    } else {
      finishSearch(resultCount);
    }
  }

  Search.query = function (query) {
    var parsed = Search._parseQuery(query);
    var results = Search._performSearch(
      parsed[0],
      parsed[1],
      parsed[2],
      parsed[3],
      parsed[4]
    );
    displayNextItem(results, results.length, parsed[1], parsed[3]);
  };

  Search.performSearch = function (query) {
    originalPerformSearchUi.call(Search, query);
    if (Search.output) {
      Search.output.classList.add("it-docs-search-results");
    }
  };
})();

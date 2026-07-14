/**
 * IT-Wallet docs — search UX: advanced query syntax, dedupe by page, previews.
 *
 * Supported operators:
 *   "exact phrase"     — words must appear adjacent, in order (page body)
 *   +term              — term required (default for plain terms)
 *   -term              — exclude pages containing term
 *   term1 OR term2     — either branch may match (union of results)
 *   title:term / t:term — term must appear in page or section title
 *   title:"phrase"     — exact phrase in a title
 */
(function () {
  "use strict";

  if (typeof Search === "undefined") return;

  var originalPerformSearch = Search._performSearch;
  var originalPerformSearchUi = Search.performSearch;
  var documentTextCache = new Map();

  function normalizeWhitespace(value) {
    return String(value || "").replace(/\s+/g, " ").trim();
  }

  function indexTermMatchesFile(indexEntry, file) {
    if (indexEntry === undefined) return false;
    if (indexEntry === file) return true;
    if (Array.isArray(indexEntry)) return indexEntry.includes(file);
    return false;
  }

  function indexTermExcludesFile(termsIndex, titleTermsIndex, term, file) {
    return (
      indexTermMatchesFile(termsIndex[term], file) ||
      indexTermMatchesFile(titleTermsIndex[term], file)
    );
  }

  function splitOrBranches(query) {
    var placeholders = [];
    var tokenized = String(query || "").replace(/"([^"]*)"/g, function (match) {
      placeholders.push(match);
      return "\x00Q" + (placeholders.length - 1) + "\x00";
    });
    tokenized = tokenized.replace(/'([^']*)'/g, function (match) {
      placeholders.push(match);
      return "\x00Q" + (placeholders.length - 1) + "\x00";
    });

    var parts = tokenized
      .split(/\s+OR\s+/i)
      .map(function (part) {
        return part
          .replace(/\x00Q(\d+)\x00/g, function (_match, index) {
            return placeholders[Number(index)];
          })
          .trim();
      })
      .filter(Boolean);

    return parts.length ? parts : [normalizeWhitespace(query)];
  }

  function parseBranch(segment) {
    var phrases = [];
    var titlePhrases = [];
    var required = [];
    var titleRequired = [];
    var excluded = [];
    var cleaned = normalizeWhitespace(segment);

    cleaned = cleaned.replace(/(?:title|t):"([^"]+)"/gi, function (_match, phrase) {
      var normalized = normalizeWhitespace(phrase);
      if (normalized) titlePhrases.push(normalized);
      return " ";
    });
    cleaned = cleaned.replace(/(?:title|t):'([^']+)'/gi, function (_match, phrase) {
      var normalized = normalizeWhitespace(phrase);
      if (normalized) titlePhrases.push(normalized);
      return " ";
    });
    cleaned = cleaned.replace(/"([^"]+)"/g, function (_match, phrase) {
      var normalized = normalizeWhitespace(phrase);
      if (normalized) phrases.push(normalized);
      return " ";
    });
    cleaned = cleaned.replace(/'([^']+)'/g, function (_match, phrase) {
      var normalized = normalizeWhitespace(phrase);
      if (normalized) phrases.push(normalized);
      return " ";
    });

    cleaned.split(/\s+/).filter(Boolean).forEach(function (token) {
      if (/^(?:title|t):/i.test(token)) {
        var titleTerm = token.replace(/^(?:title|t):/i, "");
        if (titleTerm) titleRequired.push(titleTerm);
        return;
      }
      if (token.charAt(0) === "-" && token.length > 1) {
        excluded.push(token.slice(1));
      } else if (token.charAt(0) === "+" && token.length > 1) {
        required.push(token.slice(1));
      } else if (!/^OR$/i.test(token)) {
        required.push(token);
      }
    });

    phrases.forEach(function (phrase) {
      phrase.split(/\s+/).filter(Boolean).forEach(function (word) {
        required.push(word);
      });
    });
    titlePhrases.forEach(function (phrase) {
      phrase.split(/\s+/).filter(Boolean).forEach(function (word) {
        titleRequired.push(word);
      });
    });

    return {
      raw: segment,
      phrases: phrases,
      titlePhrases: titlePhrases,
      required: required,
      titleRequired: titleRequired,
      excluded: excluded,
    };
  }

  function tokenizeAdvancedQuery(query) {
    var branches = splitOrBranches(query).map(parseBranch);
    var phrases = [];
    var titlePhrases = [];
    var required = [];
    var titleRequired = [];
    var excluded = [];

    branches.forEach(function (branch) {
      phrases = phrases.concat(branch.phrases);
      titlePhrases = titlePhrases.concat(branch.titlePhrases);
      required = required.concat(branch.required);
      titleRequired = titleRequired.concat(branch.titleRequired);
      excluded = excluded.concat(branch.excluded);
    });

    return {
      branches: branches,
      phrases: phrases,
      titlePhrases: titlePhrases,
      required: required,
      titleRequired: titleRequired,
      excluded: excluded,
    };
  }

  function stemToken(term, stemmer) {
    var lower = String(term || "").toLowerCase();
    if (!lower) return null;
    if (typeof stopwords !== "undefined" && stopwords.indexOf(lower) !== -1) {
      return null;
    }
    if (/^\d+$/.test(lower)) return null;
    return stemmer.stemWord(lower);
  }

  function buildStemmedSet(terms, stemmer) {
    var set = new Set();
    terms.forEach(function (term) {
      var stemmed = stemToken(term, stemmer);
      if (stemmed) set.add(stemmed);
    });
    return set;
  }

  function collectHighlightTerms(parsed) {
    var highlightTerms = new Set();

    function addTerm(term) {
      var lower = String(term || "").toLowerCase();
      if (lower) highlightTerms.add(lower);
    }

    parsed.branches.forEach(function (branch) {
      branch.required.forEach(addTerm);
      branch.titleRequired.forEach(addTerm);
      branch.excluded.forEach(addTerm);
      branch.phrases.forEach(function (phrase) {
        phrase.split(/\s+/).filter(Boolean).forEach(addTerm);
      });
      branch.titlePhrases.forEach(function (phrase) {
        phrase.split(/\s+/).filter(Boolean).forEach(addTerm);
      });
    });

    return highlightTerms;
  }

  Search._parseQuery = function (query) {
    var stemmer = new Stemmer();
    var parsed = tokenizeAdvancedQuery(query);
    var searchTerms = buildStemmedSet(parsed.required, stemmer);
    var excludedTerms = buildStemmedSet(parsed.excluded, stemmer);
    var highlightTerms = collectHighlightTerms(parsed);
    var objectTerms = new Set();

    parsed.required.forEach(function (term) {
      objectTerms.add(String(term).toLowerCase());
    });
    parsed.titleRequired.forEach(function (term) {
      objectTerms.add(String(term).toLowerCase());
    });

    Search._parsedBranches = parsed.branches.slice();
    Search._parsedPhrases = parsed.phrases.slice();
    Search._parsedTitlePhrases = parsed.titlePhrases.slice();

    if (typeof SPHINX_HIGHLIGHT_ENABLED !== "undefined" && SPHINX_HIGHLIGHT_ENABLED) {
      localStorage.setItem("sphinx_highlight_terms", Array.from(highlightTerms).join(" "));
    }

    return [query, searchTerms, excludedTerms, highlightTerms, objectTerms];
  };

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

  function performTitleTermsSearch(titleSearchTerms, excludedTerms) {
    if (!titleSearchTerms.size) return [];

    var terms = Search._index.terms;
    var titleTermsIndex = Search._index.titleterms;
    var filenames = Search._index.filenames;
    var docNames = Search._index.docnames;
    var titles = Search._index.titles;

    var scoreMap = new Map();
    var fileMap = new Map();

    titleSearchTerms.forEach(function (word) {
      var files = [];
      var arr = [{ files: titleTermsIndex[word], score: Scorer.title }];

      if (word.length > 2) {
        var escapedWord = _escapeRegExp(word);
        if (!titleTermsIndex.hasOwnProperty(word)) {
          Object.keys(titleTermsIndex).forEach(function (term) {
            if (term.match(escapedWord)) {
              arr.push({ files: titleTermsIndex[term], score: Scorer.partialTitle });
            }
          });
        }
      }

      if (arr.every(function (record) {
        return record.files === undefined;
      })) {
        return;
      }

      arr.forEach(function (record) {
        if (record.files === undefined) return;

        var recordFiles = record.files;
        if (recordFiles.length === undefined) recordFiles = [recordFiles];
        files.push.apply(files, recordFiles);

        recordFiles.forEach(function (file) {
          if (!scoreMap.has(file)) scoreMap.set(file, {});
          scoreMap.get(file)[word] = record.score;
        });
      });

      files.forEach(function (file) {
        if (!fileMap.has(file)) fileMap.set(file, [word]);
        else if (fileMap.get(file).indexOf(word) === -1) fileMap.get(file).push(word);
      });
    });

    var results = [];
    for (var fileMapEntry of fileMap) {
      var file = fileMapEntry[0];
      var wordList = fileMapEntry[1];
      var filteredTermCount = Array.from(titleSearchTerms).filter(function (term) {
        return term.length > 2;
      }).length;

      if (
        wordList.length !== titleSearchTerms.size &&
        wordList.length !== filteredTermCount
      ) {
        continue;
      }

      if (
        Array.from(excludedTerms).some(function (term) {
          return indexTermExcludesFile(terms, titleTermsIndex, term, file);
        })
      ) {
        continue;
      }

      var score = Math.max.apply(
        null,
        wordList.map(function (word) {
          return scoreMap.get(file)[word];
        })
      );

      results.push([
        docNames[file],
        titles[file],
        "",
        null,
        score,
        filenames[file],
      ]);
    }

    return results;
  }

  function getDocumentTitleHaystack(docName) {
    var docNames = Search._index.docnames;
    var titles = Search._index.titles;
    var allTitles = Search._index.alltitles;
    var haystack = "";

    docNames.forEach(function (name, file) {
      if (name !== docName) return;
      haystack += " " + String(titles[file] || "").toLowerCase();
    });

    Object.keys(allTitles).forEach(function (title) {
      allTitles[title].forEach(function (entry) {
        if (docNames[entry[0]] === docName) {
          haystack += " " + String(title).toLowerCase();
        }
      });
    });

    return normalizeWhitespace(haystack);
  }

  function filterResultsByTitlePhrases(results, titlePhrases) {
    if (!titlePhrases.length) return results;

    return results.filter(function (item) {
      var haystack = getDocumentTitleHaystack(item[0]);
      if (!haystack) return false;

      return titlePhrases.every(function (phrase) {
        return haystack.indexOf(normalizeWhitespace(phrase).toLowerCase()) !== -1;
      });
    });
  }

  function performBranchSearch(branch) {
    var stemmer = new Stemmer();
    var bodyTerms = buildStemmedSet(branch.required, stemmer);
    var titleTerms = buildStemmedSet(branch.titleRequired, stemmer);
    var excludedTerms = buildStemmedSet(branch.excluded, stemmer);
    var highlightTerms = collectHighlightTerms({
      branches: [branch],
    });
    var objectTerms = new Set();

    branch.required.forEach(function (term) {
      objectTerms.add(String(term).toLowerCase());
    });
    branch.titleRequired.forEach(function (term) {
      objectTerms.add(String(term).toLowerCase());
    });

    var results = [];

    if (bodyTerms.size > 0) {
      results = originalPerformSearch.call(
        Search,
        branch.raw,
        bodyTerms,
        excludedTerms,
        highlightTerms,
        objectTerms
      );
    }

    if (titleTerms.size > 0) {
      var titleResults = performTitleTermsSearch(titleTerms, excludedTerms);
      if (bodyTerms.size > 0) {
        var titleDocs = new Set(titleResults.map(function (item) {
          return item[0];
        }));
        results = results.filter(function (item) {
          return titleDocs.has(item[0]);
        });
      } else {
        results = titleResults;
      }
    }

    if (bodyTerms.size === 0 && titleTerms.size === 0 && branch.phrases.length) {
      results = originalPerformSearch.call(
        Search,
        branch.raw,
        bodyTerms,
        excludedTerms,
        highlightTerms,
        objectTerms
      );
    }

    results = filterResultsByTitlePhrases(results, branch.titlePhrases);
    return dedupeResultsByDocument(results);
  }

  function unionBranchResults(branchResultSets) {
    var bestByDoc = new Map();

    branchResultSets.forEach(function (results) {
      results.forEach(function (item) {
        var docName = item[0];
        var previous = bestByDoc.get(docName);
        if (!previous || item[4] > previous[4]) {
          bestByDoc.set(docName, item);
        }
      });
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
    var branches = Search._parsedBranches || [];
    if (!branches.length) {
      return dedupeResultsByDocument(
        originalPerformSearch.call(
          this,
          query,
          searchTerms,
          excludedTerms,
          highlightTerms,
          objectTerms
        )
      );
    }

    if (branches.length === 1) {
      return performBranchSearch(branches[0]);
    }

    return unionBranchResults(
      branches.map(function (branch) {
        return performBranchSearch(branch);
      })
    );
  };

  function buildDocumentRequestUrl(docName) {
    var docBuilder = DOCUMENTATION_OPTIONS.BUILDER;
    var docFileSuffix = DOCUMENTATION_OPTIONS.FILE_SUFFIX;
    var contentRoot = document.documentElement.dataset.content_root;

    if (docBuilder === "dirhtml") {
      var dirname = docName + "/";
      if (dirname.match(/\/index\/$/)) {
        dirname = dirname.substring(0, dirname.length - 6);
      } else if (dirname === "index/") {
        dirname = "";
      }
      return contentRoot + dirname;
    }

    return contentRoot + docName + docFileSuffix;
  }

  function fetchDocumentText(docName) {
    if (documentTextCache.has(docName)) {
      return Promise.resolve(documentTextCache.get(docName));
    }

    return fetch(buildDocumentRequestUrl(docName))
      .then(function (response) {
        if (!response.ok) return "";
        return response.text();
      })
      .then(function (html) {
        var text = Search.htmlToText(html || "", "");
        documentTextCache.set(docName, text);
        return text;
      })
      .catch(function () {
        documentTextCache.set(docName, "");
        return "";
      });
  }

  function documentContainsPhrases(text, phrases) {
    if (!phrases.length) return true;
    var haystack = normalizeWhitespace(text).toLowerCase();
    if (!haystack) return false;

    return phrases.every(function (phrase) {
      return haystack.indexOf(normalizeWhitespace(phrase).toLowerCase()) !== -1;
    });
  }

  var PHRASE_FETCH_CONCURRENCY = 4;

  function filterResultsByPhrases(results, phrases) {
    if (!phrases.length) {
      return Promise.resolve(results);
    }

    var filtered = [];

    function processBatch(start) {
      if (start >= results.length) {
        return Promise.resolve(filtered);
      }

      var batch = results.slice(start, start + PHRASE_FETCH_CONCURRENCY);
      return Promise.all(
        batch.map(function (item) {
          return fetchDocumentText(item[0]).then(function (text) {
            return documentContainsPhrases(text, phrases) ? item : null;
          });
        })
      ).then(function (items) {
        items.forEach(function (item) {
          if (item) filtered.push(item);
        });
        return processBatch(start + PHRASE_FETCH_CONCURRENCY);
      });
    }

    return processBatch(0);
  }

  function filterBranchesByPhrases(branches) {
    return Promise.all(
      branches.map(function (branch) {
        var results = performBranchSearch(branch);
        if (!branch.phrases.length) {
          return Promise.resolve(results);
        }
        return filterResultsByPhrases(results, branch.phrases);
      })
    ).then(function (branchResultSets) {
      return unionBranchResults(branchResultSets);
    });
  }

  Search.makeSearchSummary = function (htmlText, keywords, anchor) {
    var text = Search.htmlToText(htmlText, anchor);
    if (!text) return null;

    var textLower = text.toLowerCase();
    var matchPosition = -1;
    var phrases = Search._parsedPhrases || [];

    phrases.forEach(function (phrase) {
      var index = textLower.indexOf(normalizeWhitespace(phrase).toLowerCase());
      if (index > -1 && (matchPosition === -1 || index < matchPosition)) {
        matchPosition = index;
      }
    });

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
    documentTextCache.clear();
    var parsed = Search._parseQuery(query);
    var branches = Search._parsedBranches || [];
    var needsPhraseFilter = branches.some(function (branch) {
      return branch.phrases.length > 0;
    });

    if (!needsPhraseFilter) {
      var results = Search._performSearch(
        parsed[0],
        parsed[1],
        parsed[2],
        parsed[3],
        parsed[4]
      );
      displayNextItem(results, results.length, parsed[1], parsed[3]);
      return;
    }

    filterBranchesByPhrases(branches).then(function (filtered) {
      displayNextItem(filtered, filtered.length, parsed[1], parsed[3]);
    });
  };

  Search.performSearch = function (query) {
    originalPerformSearchUi.call(Search, query);
    if (Search.output) {
      Search.output.classList.add("it-docs-search-results");
    }
  };
})();

/* Load Algolia DocSearch v5 + Ask AI when public config is complete.
   searchMode in algolia-public.js is the operator switch:
     lunr    — Material MkDocs search only
     keyword — DocSearch keyword search (no Ask AI tab)
     askAi   — DocSearch + Ask AI
   If Ask AI completions fail with a quota/auth error (empty DeepSeek
   credits, revoked provider key), remount keyword search for this tab
   so the visitor does not sit on an Ask AI error. Lunr stays if config
   or the CDN/init fails. */
(function () {
  var CSS_HREF = "https://cdn.jsdelivr.net/npm/@docsearch/css@5/dist/style.css";
  var JS_AI = "https://cdn.jsdelivr.net/npm/@docsearch/js@5/dist/umd/index.js";
  var JS_SEARCH = "https://cdn.jsdelivr.net/npm/@docsearch/js@5/dist/umd/docsearch.js";
  var ASK_AI_OFF_KEY = "wiki-algolia-askai";
  var instance = null;
  var askAiOff = false;
  var mountedAskAi = false;
  var watching = false;

  function config() {
    var c = window.__ALGOLIA_DOCSEARCH;
    if (!c || typeof c !== "object") return null;
    var mode = normalizeMode(c.searchMode, c);
    if (mode === "lunr") return { mode: "lunr" };
    if (!c.appId || !c.apiKey || !c.indexName) return null;
    return {
      appId: c.appId,
      apiKey: c.apiKey,
      indexName: c.indexName,
      markdownIndexName: c.markdownIndexName,
      assistantId: c.assistantId,
      mode: mode,
    };
  }

  function normalizeMode(mode, c) {
    if (mode === "lunr" || mode === "keyword" || mode === "askAi") return mode;
    if (c && c.assistantId) return "askAi";
    if (c && c.appId && c.apiKey && c.indexName) return "keyword";
    return "lunr";
  }

  function readAskAiOff() {
    if (askAiOff) return true;
    try {
      return sessionStorage.getItem(ASK_AI_OFF_KEY) === "off";
    } catch (err) {
      return false;
    }
  }

  function writeAskAiOff() {
    askAiOff = true;
    try {
      sessionStorage.setItem(ASK_AI_OFF_KEY, "off");
    } catch (err) {
      /* Incognito WebView may reject storage; in-memory flag still holds. */
    }
  }

  function wantsAskAi(cfg) {
    return cfg.mode === "askAi" && !!cfg.assistantId && !readAskAiOff();
  }

  function ready(fn) {
    if (document.readyState === "loading") {
      document.addEventListener("DOMContentLoaded", fn);
    } else {
      fn();
    }
  }

  function loadStyle(href) {
    return new Promise(function (resolve, reject) {
      var link = document.createElement("link");
      link.rel = "stylesheet";
      link.href = href;
      link.onload = function () {
        resolve();
      };
      link.onerror = function () {
        reject(new Error("docsearch css"));
      };
      document.head.appendChild(link);
    });
  }

  function loadScript(src) {
    return new Promise(function (resolve, reject) {
      var script = document.createElement("script");
      script.src = src;
      script.async = true;
      script.onload = function () {
        resolve();
      };
      script.onerror = function () {
        reject(new Error("docsearch js"));
      };
      document.body.appendChild(script);
    });
  }

  function unmount() {
    if (instance && typeof instance.destroy === "function") {
      try {
        instance.destroy();
      } catch (err) {
        /* Ignore destroy races while a completion is in flight. */
      }
    }
    instance = null;
    mountedAskAi = false;
    var el = document.getElementById("docsearch");
    if (el && el.parentNode) el.parentNode.removeChild(el);
  }

  function mount(cfg, withAskAi) {
    var search = document.querySelector(".md-search");
    if (!search || !search.parentNode) return;
    if (typeof window.docsearch !== "function") return;

    unmount();

    var el = document.createElement("div");
    el.id = "docsearch";
    search.parentNode.insertBefore(el, search);

    try {
      var opts = {
        container: "#docsearch",
        appId: cfg.appId,
        apiKey: cfg.apiKey,
        indices: [cfg.indexName],
        theme: "dark",
        insights: false,
        disableUserPersonalization: true,
      };
      if (withAskAi && cfg.assistantId) {
        opts.askAi = {
          assistantId: cfg.assistantId,
          indexName: cfg.markdownIndexName || cfg.indexName,
        };
      }
      instance = window.docsearch(opts);
      mountedAskAi = !!(withAskAi && cfg.assistantId);
      document.documentElement.classList.add("wiki-algolia");
    } catch (err) {
      unmount();
      mountedAskAi = false;
      document.documentElement.classList.remove("wiki-algolia");
    }
  }

  function requestUrl(input) {
    if (typeof input === "string") return input;
    if (input && typeof input.url === "string") return input.url;
    try {
      return String(input);
    } catch (err) {
      return "";
    }
  }

  function isCompletionsUrl(url) {
    if (!url) return false;
    var s = String(url);
    if (s.indexOf("askai.algolia.com") !== -1) return true;
    return (
      s.indexOf("/agent-studio/") !== -1 && s.indexOf("/completions") !== -1
    );
  }

  function isQuotaText(text) {
    var t = (text || "").toLowerCase();
    if (!t) return false;
    if (t.indexOf("cloudflare") !== -1) return false;
    return (
      t.indexOf("insufficient") !== -1 ||
      t.indexOf("quota") !== -1 ||
      t.indexOf("credit") !== -1 ||
      t.indexOf("balance") !== -1 ||
      t.indexOf("payment required") !== -1 ||
      t.indexOf("billing") !== -1 ||
      t.indexOf("out of funds") !== -1 ||
      t.indexOf("exceeded your") !== -1
    );
  }

  function isAskAiUnusable(resp) {
    var status = resp.status;
    if (status === 401 || status === 402) return Promise.resolve(true);
    if (status >= 200 && status < 300) return Promise.resolve(false);
    return resp
      .clone()
      .text()
      .then(function (text) {
        var lower = (text || "").toLowerCase();
        if (lower.indexOf("cloudflare") !== -1) return false;
        if (status === 403) return true;
        return isQuotaText(lower);
      })
      .catch(function () {
        return status === 403;
      });
  }

  function fallbackToKeyword(cfg) {
    writeAskAiOff();
    if (!mountedAskAi) return;
    mount(cfg, false);
  }

  function watchAskAiFailures(cfg) {
    if (watching) return;
    if (typeof window.fetch !== "function") return;
    watching = true;
    var orig = window.fetch;
    window.fetch = function (input, init) {
      var pending = orig.apply(this, arguments);
      if (!isCompletionsUrl(requestUrl(input))) return pending;
      return pending.then(function (resp) {
        return isAskAiUnusable(resp).then(function (unusable) {
          if (unusable) fallbackToKeyword(cfg);
          return resp;
        });
      });
    };
  }

  ready(function () {
    var cfg = config();
    if (!cfg || cfg.mode === "lunr") return;
    var withAskAi = wantsAskAi(cfg);
    var jsSrc = withAskAi ? JS_AI : JS_SEARCH;
    Promise.all([loadStyle(CSS_HREF), loadScript(jsSrc)])
      .then(function () {
        mount(cfg, withAskAi);
        if (withAskAi) watchAskAiFailures(cfg);
      })
      .catch(function () {
        /* Leave Material lunr in place. */
      });
  });
})();

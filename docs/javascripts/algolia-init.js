/* Load Algolia DocSearch v5 + Ask AI when public config is complete.
   If anything is missing or the CDN/init fails, Material lunr search stays. */
(function () {
  var CSS_HREF = "https://cdn.jsdelivr.net/npm/@docsearch/css@5/dist/style.css";
  var JS_SRC = "https://cdn.jsdelivr.net/npm/@docsearch/js@5/dist/umd/index.js";

  function config() {
    var c = window.__ALGOLIA_DOCSEARCH;
    if (!c || typeof c !== "object") return null;
    if (!c.appId || !c.apiKey || !c.indexName || !c.assistantId) return null;
    return c;
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

  function mount(cfg) {
    var search = document.querySelector(".md-search");
    if (!search || !search.parentNode) return;
    if (typeof window.docsearch !== "function") return;

    var el = document.createElement("div");
    el.id = "docsearch";
    search.parentNode.insertBefore(el, search);

    try {
      window.docsearch({
        container: "#docsearch",
        appId: cfg.appId,
        apiKey: cfg.apiKey,
        indices: [cfg.indexName],
        theme: "dark",
        insights: false,
        disableUserPersonalization: true,
        askAi: {
          assistantId: cfg.assistantId,
          indexName: cfg.markdownIndexName || cfg.indexName,
        },
      });
      document.documentElement.classList.add("wiki-algolia");
    } catch (err) {
      if (el.parentNode) el.parentNode.removeChild(el);
    }
  }

  ready(function () {
    var cfg = config();
    if (!cfg) return;
    Promise.all([loadStyle(CSS_HREF), loadScript(JS_SRC)])
      .then(function () {
        mount(cfg);
      })
      .catch(function () {
        /* Leave Material lunr in place. */
      });
  });
})();

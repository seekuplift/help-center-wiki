/* Public Algolia DocSearch config. Safe to commit: search-only key.
   Admin / write keys must never be placed here.

   searchMode is the operator switch (commit + push to Pages):
     "askAi"   — DocSearch keyword search + Ask AI tab
     "keyword" — DocSearch keyword search only (no Ask AI tab)
     "lunr"    — Material MkDocs search only
   Keep assistantId even when searchMode is keyword or lunr so turning
   Ask AI back on is one field. README: "Switching search modes". */
window.__ALGOLIA_DOCSEARCH = {
  "appId": "9BRV23BPIK",
  "apiKey": "0c38ad4e137ebba8dc95f59868a374f0",
  "indexName": "help_center",
  "markdownIndexName": "help_center_markdown",
  "assistantId": "657f2af2-ffc1-4a73-8014-34df1439c03d",
  "searchMode": "askAi"
};

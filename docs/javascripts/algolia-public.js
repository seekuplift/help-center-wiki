/* Public Algolia DocSearch config. Safe to commit: search-only key.
   Admin / write keys must never be placed here.

   searchMode is the operator switch (commit + push to Pages):
     "askAi"   — DocSearch keyword search + Ask AI tab
     "keyword" — DocSearch keyword search only (no Ask AI tab)
     "lunr"    — Material MkDocs search only
   Keep assistantId even when searchMode is keyword or lunr so turning
   Ask AI back on is one field. README: "Switching search modes". */
window.__ALGOLIA_DOCSEARCH = {
  "appId": "YN9LHHY3JW",
  "apiKey": "8e1024885365e67a9c4c641a60a7e8a1",
  "indexName": "help_center",
  "markdownIndexName": "help_center_markdown",
  "assistantId": "dbf5f1be-667c-4500-a94a-f32fb02c4363",
  "searchMode": "askAi"
};

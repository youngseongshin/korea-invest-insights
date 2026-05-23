/*
 * GoatCounter view-count widget.
 * Looks up the current page's unique-visit count from the public counter API
 * and writes the formatted number into every [data-goatcounter-views] element.
 *
 * Endpoint pattern:
 *   https://<site-code>.goatcounter.com/counter/<URL-encoded-path>.json
 * Response shape (success):
 *   { "count": "123", "count_unique": "100" }
 *
 * Failure modes are silenced: the placeholder ('—') stays so the meta row
 * never breaks when the API is unreachable.
 */
(function () {
  'use strict';

  var els = document.querySelectorAll('[data-goatcounter-views]');
  if (!els.length) return;

  var ENDPOINT_BASE = 'https://korea-invest-insights.goatcounter.com/counter/';

  // Each element carries its own target path via the attribute value
  // (set by the article-details partial as $Page.RelPermalink). On list
  // pages this is critical: every card has a DIFFERENT path, not the
  // page-level window.location.pathname. The empty-attribute case falls
  // back to the current page path for safety.
  function normalisePath(raw) {
    if (!raw) return '/';
    if (raw === '/') return '/';
    return raw.replace(/\/$/, '');
  }

  // Group elements by the path they want to count, so we only fetch each
  // unique path once even when the same article appears multiple times
  // on a list page.
  var groups = {};
  for (var i = 0; i < els.length; i++) {
    var el = els[i];
    var attr = el.getAttribute('data-goatcounter-views');
    var rawPath = (attr && attr !== 'true') ? attr : window.location.pathname;
    var path = normalisePath(rawPath);
    if (!groups[path]) groups[path] = [];
    groups[path].push(el);
  }

  function applyCount(targets, value) {
    var n = parseInt(String(value || '0').replace(/[^0-9]/g, ''), 10);
    if (!Number.isFinite(n)) return;
    var formatted = n.toLocaleString();
    for (var i = 0; i < targets.length; i++) {
      targets[i].textContent = formatted;
      targets[i].removeAttribute('aria-busy');
    }
  }

  Object.keys(groups).forEach(function (path) {
    var url = ENDPOINT_BASE + encodeURIComponent(path) + '.json';
    fetch(url, { cache: 'no-store', credentials: 'omit' })
      .then(function (r) { return r.ok ? r.json() : null; })
      .then(function (j) {
        if (!j) return;
        var raw = j.count_unique != null ? j.count_unique : j.count;
        applyCount(groups[path], raw);
      })
      .catch(function () { /* silent */ });
  });
})();

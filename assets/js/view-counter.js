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

  // Strip trailing slash to align with how GoatCounter records paths,
  // but keep the leading slash that the counter endpoint expects.
  var rawPath = window.location.pathname || '/';
  var path = rawPath === '/' ? '/' : rawPath.replace(/\/$/, '');

  var endpoint = 'https://korea-invest-insights.goatcounter.com/counter/' +
    encodeURIComponent(path) + '.json';

  fetch(endpoint, { cache: 'no-store', credentials: 'omit' })
    .then(function (r) { return r.ok ? r.json() : null; })
    .then(function (j) {
      if (!j) return;
      // Prefer unique-visit count when present, fall back to total count.
      var raw = j.count_unique != null ? j.count_unique : j.count;
      var n = parseInt(String(raw || '0'), 10);
      if (!Number.isFinite(n)) return;
      var formatted = n.toLocaleString();
      for (var i = 0; i < els.length; i++) {
        els[i].textContent = formatted;
        els[i].removeAttribute('aria-busy');
      }
    })
    .catch(function () { /* silent */ });
})();

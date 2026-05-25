/*
 * Article micro-interactions for Korea Invest Insights.
 *
 *   1. Scroll progress bar       — fixed cobalt strip at the top of the
 *                                  viewport, scaled horizontally as the
 *                                  reader scrolls. Auto-hidden on short
 *                                  pages where scrolling isn't meaningful.
 *
 *   2. TOC active section        — toggles .is-active on the TOC link
 *                                  whose target heading is currently in
 *                                  the viewport, using IntersectionObserver.
 *
 *   3. Share buttons             — Web Share API when available, with a
 *                                  copy-to-clipboard fallback and a brief
 *                                  toast confirmation.
 *
 * All three are no-ops when their target markup is absent, so the script
 * is safe to load on every page.
 */
(function () {
  'use strict';

  // ──────────────────────────────────────────────
  // Helpers
  // ──────────────────────────────────────────────

  function ready(fn) {
    if (document.readyState !== 'loading') return fn();
    document.addEventListener('DOMContentLoaded', fn, { once: true });
  }

  function toast(message) {
    var el = document.createElement('div');
    el.className = 'kii-toast';
    el.textContent = message;
    document.body.appendChild(el);
    // Force reflow before adding the visibility class so the transition fires.
    void el.offsetWidth;
    el.classList.add('is-visible');
    setTimeout(function () {
      el.classList.remove('is-visible');
      setTimeout(function () { el.remove(); }, 240);
    }, 1800);
  }

  // ──────────────────────────────────────────────
  // 1. Scroll progress bar
  // ──────────────────────────────────────────────

  function initScrollProgress() {
    // Skip on very short pages — no meaningful scrolling.
    var docH = document.documentElement.scrollHeight;
    var winH = window.innerHeight;
    if (docH - winH < 240) return;

    var bar = document.createElement('div');
    bar.className = 'kii-scroll-progress';
    var fill = document.createElement('span');
    fill.className = 'kii-scroll-progress-bar';
    bar.appendChild(fill);
    document.body.insertBefore(bar, document.body.firstChild);

    var ticking = false;
    function update() {
      var sH = document.documentElement.scrollHeight - window.innerHeight;
      var sT = window.scrollY || document.documentElement.scrollTop || 0;
      var ratio = sH > 0 ? Math.min(1, Math.max(0, sT / sH)) : 0;
      fill.style.transform = 'scaleX(' + ratio + ')';
      ticking = false;
    }
    function onScroll() {
      if (!ticking) {
        window.requestAnimationFrame(update);
        ticking = true;
      }
    }
    update();
    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', onScroll, { passive: true });
  }

  // ──────────────────────────────────────────────
  // 2. TOC active section
  // ──────────────────────────────────────────────

  function initTocActive() {
    var tocLinks = document.querySelectorAll('.widget--toc .toc-nav a[href^="#"]');
    if (!tocLinks.length || !('IntersectionObserver' in window)) return;

    // Map heading id → toc link.
    var linksById = {};
    var headings = [];
    Array.prototype.forEach.call(tocLinks, function (link) {
      var id = decodeURIComponent(link.getAttribute('href').slice(1));
      if (!id) return;
      var h = document.getElementById(id);
      if (!h) return;
      linksById[id] = link;
      headings.push(h);
    });
    if (!headings.length) return;

    var visible = new Set();

    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          visible.add(e.target.id);
        } else {
          visible.delete(e.target.id);
        }
      });

      // Pick the topmost heading that is currently in the viewport. If none,
      // fall back to the heading whose top is just above the viewport.
      var current = null;
      if (visible.size) {
        var minTop = Infinity;
        visible.forEach(function (id) {
          var h = document.getElementById(id);
          if (!h) return;
          var top = h.getBoundingClientRect().top;
          if (top < minTop) { minTop = top; current = id; }
        });
      } else {
        // Find last heading above the fold.
        for (var i = headings.length - 1; i >= 0; i--) {
          if (headings[i].getBoundingClientRect().top < 80) {
            current = headings[i].id;
            break;
          }
        }
      }

      Array.prototype.forEach.call(tocLinks, function (link) {
        link.classList.remove('is-active');
      });
      if (current && linksById[current]) {
        linksById[current].classList.add('is-active');
      }
    }, {
      // Trigger as a heading crosses ~25% from the top of the viewport.
      rootMargin: '-25% 0px -65% 0px',
      threshold: 0
    });

    headings.forEach(function (h) { io.observe(h); });
  }

  // ──────────────────────────────────────────────
  // 3. Share buttons
  // ──────────────────────────────────────────────

  function copyToClipboard(text) {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      return navigator.clipboard.writeText(text);
    }
    return new Promise(function (resolve, reject) {
      try {
        var ta = document.createElement('textarea');
        ta.value = text;
        ta.setAttribute('readonly', '');
        ta.style.position = 'absolute';
        ta.style.left = '-9999px';
        document.body.appendChild(ta);
        ta.select();
        document.execCommand('copy');
        document.body.removeChild(ta);
        resolve();
      } catch (e) { reject(e); }
    });
  }

  function initShare() {
    var buttons = document.querySelectorAll('[data-share]');
    if (!buttons.length) return;

    Array.prototype.forEach.call(buttons, function (btn) {
      btn.addEventListener('click', function (ev) {
        ev.preventDefault();
        var kind = btn.getAttribute('data-share');
        var url = btn.getAttribute('data-url') || window.location.href;
        var title = btn.getAttribute('data-title') || document.title;
        var labelDone = btn.getAttribute('data-label-done') || 'Copied';
        var labelToast = btn.getAttribute('data-label-toast') || labelDone;

        if (kind === 'native' && navigator.share) {
          navigator.share({ title: title, url: url }).catch(function () { /* user cancelled */ });
          return;
        }

        if (kind === 'twitter') {
          var tw = 'https://twitter.com/intent/tweet?text=' +
            encodeURIComponent(title) + '&url=' + encodeURIComponent(url);
          window.open(tw, '_blank', 'noopener,noreferrer');
          return;
        }

        if (kind === 'linkedin') {
          var li = 'https://www.linkedin.com/sharing/share-offsite/?url=' +
            encodeURIComponent(url);
          window.open(li, '_blank', 'noopener,noreferrer');
          return;
        }

        // Default: copy link.
        copyToClipboard(url).then(function () {
          btn.setAttribute('data-copied', 'true');
          toast(labelToast);
          setTimeout(function () { btn.removeAttribute('data-copied'); }, 1800);
        }).catch(function () { /* silent */ });
      });
    });
  }

  // ──────────────────────────────────────────────
  // Boot
  // ──────────────────────────────────────────────

  ready(function () {
    initScrollProgress();
    initTocActive();
    initShare();
  });
})();

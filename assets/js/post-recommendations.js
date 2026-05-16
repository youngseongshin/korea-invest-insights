(function () {
  const WIDGET_SELECTOR = "[data-recommendation-widget]";
  const VOTER_KEY = "kii:recommendations:voter";
  const VOTE_PREFIX = "kii:recommendations:voted:";

  function storageGet(key) {
    try {
      return window.localStorage.getItem(key);
    } catch (_) {
      return null;
    }
  }

  function storageSet(key, value) {
    try {
      window.localStorage.setItem(key, value);
    } catch (_) {
      /* localStorage can be unavailable in strict privacy modes. */
    }
  }

  function randomId() {
    if (window.crypto && typeof window.crypto.randomUUID === "function") {
      return window.crypto.randomUUID();
    }
    const bytes = new Uint8Array(16);
    if (window.crypto && typeof window.crypto.getRandomValues === "function") {
      window.crypto.getRandomValues(bytes);
      return Array.from(bytes, (byte) => byte.toString(16).padStart(2, "0")).join("");
    }
    return `${Date.now()}-${Math.random().toString(16).slice(2)}`;
  }

  function getVoterId() {
    let voterId = storageGet(VOTER_KEY);
    if (!voterId) {
      voterId = randomId();
      storageSet(VOTER_KEY, voterId);
    }
    return voterId;
  }

  function formatCount(value) {
    const number = Number(value);
    if (!Number.isFinite(number) || number < 0) return "0";
    return new Intl.NumberFormat(document.documentElement.lang || undefined).format(number);
  }

  function voteStorageKey(key) {
    return `${VOTE_PREFIX}${key}`;
  }

  function isLocallyRecommended(key) {
    return storageGet(voteStorageKey(key)) === "1";
  }

  function markLocallyRecommended(key) {
    storageSet(voteStorageKey(key), "1");
  }

  function setStatus(widget, message, isError) {
    const status = widget.querySelector(".post-recommendation-status");
    if (!status) return;
    status.textContent = message || "";
    status.hidden = !message;
    status.dataset.state = isError ? "error" : "info";
  }

  function setButtonState(widget, recommended, busy) {
    const button = widget.querySelector(".post-recommendation-button");
    const text = widget.querySelector(".post-recommendation-button-text");
    if (!button || !text) return;

    const labelButton = widget.dataset.labelButton || "Recommend";
    const labelDone = widget.dataset.labelDone || "Recommended";

    button.disabled = Boolean(busy || recommended);
    button.setAttribute("aria-pressed", recommended ? "true" : "false");
    widget.dataset.recommended = recommended ? "true" : "false";
    text.textContent = recommended ? labelDone : labelButton;
  }

  function setCount(widget, count) {
    const countNode = widget.querySelector(".post-recommendation-count");
    if (countNode) countNode.textContent = formatCount(count);
  }

  function endpointUrl(endpoint, key) {
    const url = new URL(endpoint, window.location.origin);
    url.searchParams.set("key", key);
    return url;
  }

  async function loadCount(widget) {
    const endpoint = widget.dataset.endpoint;
    const key = widget.dataset.key;
    if (!endpoint || !key) return;

    const response = await fetch(endpointUrl(endpoint, key), {
      method: "GET",
      headers: { Accept: "application/json" },
      credentials: "omit",
    });

    if (!response.ok) throw new Error(`GET ${response.status}`);
    const payload = await response.json();
    setCount(widget, payload.count || 0);
  }

  async function submitRecommendation(widget) {
    const endpoint = widget.dataset.endpoint;
    const key = widget.dataset.key;
    if (!endpoint || !key) return;

    const response = await fetch(endpoint, {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      credentials: "omit",
      body: JSON.stringify({
        key,
        voter: getVoterId(),
      }),
    });

    if (!response.ok) throw new Error(`POST ${response.status}`);
    const payload = await response.json();
    setCount(widget, payload.count || 0);
    markLocallyRecommended(key);
    setButtonState(widget, true, false);
  }

  function initWidget(widget) {
    const key = widget.dataset.key;
    const button = widget.querySelector(".post-recommendation-button");
    if (!key || !button) return;

    setButtonState(widget, isLocallyRecommended(key), true);
    loadCount(widget)
      .catch(() => {
        setStatus(widget, widget.dataset.labelError || "Recommendation count is temporarily unavailable.", true);
      })
      .finally(() => {
        setButtonState(widget, isLocallyRecommended(key), false);
      });

    button.addEventListener("click", async () => {
      if (isLocallyRecommended(key)) {
        setButtonState(widget, true, false);
        return;
      }

      setStatus(widget, "", false);
      setButtonState(widget, false, true);

      try {
        await submitRecommendation(widget);
      } catch (_) {
        setStatus(widget, widget.dataset.labelError || "Recommendation count is temporarily unavailable.", true);
        setButtonState(widget, false, false);
      }
    });
  }

  function init() {
    document.querySelectorAll(WIDGET_SELECTOR).forEach(initWidget);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init, { once: true });
  } else {
    init();
  }
})();

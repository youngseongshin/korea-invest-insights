// KII post -> Substack draft, run inside a logged-in https://<pub>.substack.com page.
//
// Why in-page: Substack auth is an HttpOnly session cookie that scripts cannot read, and
// the browser pane denies local-network access, so nothing is served from this machine.
// Everything is fetched from public CORS-open sources (raw GitHub markdown, live site SVG)
// and the page's own session authenticates the same-origin Substack API calls.
//
// Converts: SVG figures -> PNG, markdown tables -> PNG (Substack has no table node),
// [^key] -> native footnotes, bold/italic/code/links, bullets, headings, rules.
// Site-relative links (/post/..., /ko/post/...) become absolute site URLs, because Substack
// resolves a relative href against the publication domain and the link breaks.
//
// Use (javascript_tool):
//   1. open https://<pub>.substack.com/publish/post/<draftId> in the pane (logged in)
//   2. paste this file once: it defines window.__kiiRun(overrides)
//   3. window.__kiiRun({slug:'<slug>', draft:<id>, dry:true})   structure check, no writes
//   4. window.__kiiRun({slug:'<slug>', draft:<id>})             render, upload, replace the draft body
//   5. poll window.__kii -> {step, done, total, error, result, summary, hash}; never await run
//   6. await window.__kiiVerify({draft:<id>})        reread the saved draft: figure, table and
//      footnote counts must match __kii.summary, no literal markdown, no unuploaded image
//   7. await window.__kiiPublish({draft:<id>})       refuses a title that is already published,
//      publishes ({send:true} emails subscribers; pass send:false for web only), returns the URL
//   8. on a https://substack.com page, paste this file again and
//      await window.__kiiNote({title, desc, url})    posts the Note, returns its URL
//   9. record: scripts/substack_record_browser_publish.py --slug ... --substack-url ...
//      --draft-id ... --note-url ...   (post_publish_distribution.py waits for this receipt)
// Footnote numbers follow first reference. The draft stays private until you publish it.
// Literal markdown or HTML left in a text node means the converter missed a construct.
window.__kiiLintRes = [/\[\^/, /\]\(/, /<\/?\w+/, /\*\*/, /&\w+;/, /^!\[/];
// An HTML entity left in image alt text is read aloud literally by screen readers ("P&amp;L").
window.__kiiAltRe = /&#?\w+;/;
// A link that is not absolute resolves against the Substack domain, so it is a defect.
window.__kiiLinkOk = href => /^(https?:\/\/|mailto:)/i.test(href || '');
window.__kiiBadLinks = n => (n.marks || []).filter(m => m.type === 'link' && !window.__kiiLinkOk((m.attrs || {}).href))
  .map(m => 'relative link: ' + (m.attrs || {}).href);
window.__kiiRun = (over = {}) => {
  const CFG = {slug: '', draft: 0, lang: 'en', dry: false,
    raw: 'https://raw.githubusercontent.com/youngseongshin/korea-invest-insights/main',
    site: 'https://koreainvestinsights.com', ...over};
  const LANGS = [['English', '', 'en'], ['Korean', '/ko', 'ko'], ['Japanese', '/ja', 'ja'], ['Chinese', '/zh', 'zh'],
                 ['Spanish', '/es', 'es'], ['French', '/fr', 'fr'], ['Vietnamese', '/vi', 'vi']];
  const st = window.__kii = {step: 'init', done: 0, total: 0, error: null, result: null, doc: null, hash: null};

  const INLINE = new RegExp(
    '(?<fn>\\[\\^(?<fnkey>[^\\]]+)\\])' +
    '|(?<bi>\\*\\*\\*(?<bit>.+?)\\*\\*\\*)' +
    '|(?<b>\\*\\*(?<bt>.+?)\\*\\*)' +
    '|(?<sb><strong>(?<sbt>.+?)</strong>)' +
    '|(?<i>\\*(?!\\s)(?<it>.+?)(?<!\\s)\\*)' +
    '|(?<c>`(?<ct>[^`]+)`)' +
    '|(?<l>\\[(?<lt>[^\\]]+)\\]\\((?<lu>[^)\\s]+)\\))', 'g');
  const esc = s => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  // Figure alt comes from an HTML attribute, so decode its entities once (&amp;lt; stays &lt;).
  const NAMED = {amp: '&', lt: '<', gt: '>', quot: '"', apos: "'"};
  const unesc = s => s.replace(/&(?:#(\d+)|#x([0-9a-f]+)|(amp|lt|gt|quot|apos));/gi, (m, d, x, n) =>
    d ? String.fromCodePoint(+d) : x ? String.fromCodePoint(parseInt(x, 16)) : NAMED[n.toLowerCase()]);

  class Numbering {
    constructor(defs) { this.defs = defs; this.order = []; }
    number(key) {
      if (!(key in this.defs)) throw new Error('footnote reference without definition: ' + key);
      if (!this.order.includes(key)) this.order.push(key);
      return this.order.indexOf(key) + 1;
    }
  }
  const addMark = (n, mark) => n.type === 'text' ? {...n, marks: [...(n.marks || []), mark]} : n;
  const absHref = u => /^\/(?!\/)/.test(u) ? CFG.site + u : u;

  function parseInline(text, nums) {
    const out = [];
    let pos = 0;
    for (const m of text.matchAll(INLINE)) {
      const g = m.groups;
      if (m.index > pos) out.push({type: 'text', text: text.slice(pos, m.index)});
      if (g.fn) out.push({type: 'footnoteAnchor', attrs: {number: nums.number(g.fnkey)}});
      else if (g.bi) parseInline(g.bit, nums).forEach(n => out.push(addMark(addMark(n, {type: 'strong'}), {type: 'em'})));
      else if (g.b || g.sb) parseInline(g.bt || g.sbt, nums).forEach(n => out.push(addMark(n, {type: 'strong'})));
      else if (g.i) parseInline(g.it, nums).forEach(n => out.push(addMark(n, {type: 'em'})));
      else if (g.c) out.push({type: 'text', text: g.ct, marks: [{type: 'code'}]});
      else if (g.l) {
        const link = {type: 'link', attrs: {href: absHref(g.lu), target: '_blank', rel: 'noopener noreferrer nofollow', class: null}};
        parseInline(g.lt, nums).forEach(n => out.push(addMark(n, link)));
      }
      pos = m.index + m[0].length;
    }
    if (pos < text.length) out.push({type: 'text', text: text.slice(pos)});
    return out.filter(n => n.type !== 'text' || n.text);
  }

  function inlineHtml(text, nums) {
    return parseInline(text, nums).map(n => {
      if (n.type === 'footnoteAnchor') return `<sup class="fn">${n.attrs.number}</sup>`;
      let s = esc(n.text);
      for (const mk of n.marks || []) {
        s = mk.type === 'strong' ? `<b>${s}</b>` : mk.type === 'em' ? `<i>${s}</i>`
          : mk.type === 'code' ? `<code>${s}</code>` : `<span class="lk">${s}</span>`;
      }
      return s;
    }).join('');
  }

  const TABLE_CSS = '#t{width:1080px;padding:20px 24px 22px;box-sizing:content-box;color:#1f2328;background:#fff;' +
    'font:15px/1.5 Helvetica,Arial,sans-serif}table{border-collapse:collapse;width:100%}' +
    'th{background:#eef2f1;text-align:left;font-weight:700;padding:10px 12px;border-bottom:2px solid #0f6b57}' +
    'td{padding:9px 12px;border-bottom:1px solid #dfe5e3;vertical-align:top}' +
    'tr:nth-child(even) td{background:#f8faf9}.r{text-align:right}.c{text-align:center}' +
    'sup.fn{font-size:.72em;color:#0f6b57;font-weight:700;margin-left:1px}' +
    '.lk{color:#0b5cad;text-decoration:underline}code{font:13px Menlo,monospace;background:#eef2f1;padding:1px 4px;border-radius:3px}';

  function parseTable(lines) {
    const cells = l => l.trim().replace(/^\|/, '').replace(/\|$/, '').split('|').map(c => c.trim());
    const rows = lines.map(cells);
    if (!rows[1].every(c => /^:?-{3,}:?$/.test(c))) throw new Error('table without separator: ' + lines[0].slice(0, 60));
    const aligns = rows[1].map(c => (c.endsWith(':') && !c.startsWith(':')) ? 'r' : (c.startsWith(':') && c.endsWith(':')) ? 'c' : 'l');
    const body = [rows[0], ...rows.slice(2)];
    for (const r of body) if (r.length !== rows[0].length) throw new Error('ragged table row: ' + r.slice(0, 2));
    return [body, aligns];
  }

  async function loadImage(src) {
    return new Promise((res, rej) => { const im = new Image(); im.onload = () => res(im); im.onerror = () => rej(new Error('image load failed')); im.src = src; });
  }
  const toPng = async (im, w, h) => {
    const cv = document.createElement('canvas'); cv.width = w; cv.height = h;
    const cx = cv.getContext('2d'); cx.fillStyle = '#fff'; cx.fillRect(0, 0, w, h); cx.drawImage(im, 0, 0, w, h);
    return new Promise(res => cv.toBlob(res, 'image/png'));
  };
  async function svgToBlob(svgUrl) {
    const text = await (await fetch(svgUrl)).text();
    const m = text.match(/viewBox="0 0 (\d+(?:\.\d+)?) (\d+(?:\.\d+)?)"/);
    if (!m) throw new Error('no viewBox: ' + svgUrl);
    const w = Math.round(+m[1]), h = Math.round(+m[2]);
    const im = await loadImage(URL.createObjectURL(new Blob([text], {type: 'image/svg+xml'})));
    return {blob: await toPng(im, w * 2, h * 2), w: w * 2, h: h * 2};
  }
  async function rasterUrl(url) {
    if (/\.svg$/i.test(url)) return svgToBlob(url);
    if (!/\.png$/i.test(url)) throw new Error('unsupported image type: ' + url);
    const blob = await (await fetch(url)).blob();
    const bm = await createImageBitmap(blob);
    return {blob, w: bm.width, h: bm.height};
  }
  async function tableToBlob(rows, aligns, nums) {
    const cell = (tag, c, a) => `<${tag}${a === 'r' ? ' class="r"' : a === 'c' ? ' class="c"' : ''}>${inlineHtml(c, nums)}</${tag}>`;
    const head = rows[0].map((c, i) => cell('th', c, aligns[i])).join('');
    const body = rows.slice(1).map(r => '<tr>' + r.map((c, i) => cell('td', c, aligns[i])).join('') + '</tr>').join('');
    const inner = `<div id="t"><table><thead><tr>${head}</tr></thead><tbody>${body}</tbody></table></div>`;
    const host = document.createElement('div');
    host.style.cssText = 'all:initial;position:absolute;left:-99999px;top:0';
    const root = host.attachShadow({mode: 'open'});
    root.innerHTML = `<style>${TABLE_CSS}</style>${inner}`;
    document.body.appendChild(host);
    const h = Math.ceil(root.getElementById('t').getBoundingClientRect().height);
    host.remove();
    const w = 1128;
    const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="${w}" height="${h}"><foreignObject width="100%" height="100%">` +
      `<div xmlns="http://www.w3.org/1999/xhtml"><style>${TABLE_CSS}</style>${inner}</div></foreignObject></svg>`;
    const im = await loadImage('data:image/svg+xml;charset=utf-8,' + encodeURIComponent(svg));
    return {blob: await toPng(im, w * 2, h * 2), w: w * 2, h: h * 2};
  }

  const imageNode = (src, alt, w, h, bytes) => ({type: 'captionedImage', attrs: {}, content: [{type: 'image2', attrs: {
    src, srcNoWatermark: null, fullscreen: null, imageSize: null, height: h, width: w, resizeWidth: null, bytes, alt,
    title: null, type: 'image/png', href: null, belowTheFold: false, topImage: false, internalRedirect: null}}]});

  const api = async (method, path, body) => {
    const r = await fetch('/api/v1' + path, {method, credentials: 'same-origin',
      headers: {'Content-Type': 'application/json'}, body: body ? JSON.stringify(body) : undefined});
    const t = await r.text();
    if (!r.ok) throw new Error(`${method} ${path} ${r.status} ${t.slice(0, 200)}`);
    return t ? JSON.parse(t) : {};
  };
  const dataUri = blob => new Promise(res => { const f = new FileReader(); f.onload = () => res(f.result); f.readAsDataURL(blob); });
  const upload = async blob => (await api('POST', '/image', {image: await dataUri(blob), postId: CFG.draft})).url;
  const sha = async s => [...new Uint8Array(await crypto.subtle.digest('SHA-256', new TextEncoder().encode(s)))]
    .map(b => b.toString(16).padStart(2, '0')).join('');

  async function run() {
    st.step = 'fetch';
    const postUrl = `${CFG.raw}/content/post/${CFG.slug}`;
    const md = await (await fetch(`${postUrl}/index.${CFG.lang}.md`)).text();
    const fm = md.split('---');
    const meta = {};
    for (const line of fm[1].trim().split('\n')) {
      const k = line.indexOf(':');
      if (k > 0) meta[line.slice(0, k).trim()] = line.slice(k + 1).trim().replace(/^["']|["']$/g, '');
    }
    const body = fm.slice(2).join('---').replace(/^\n+|\n+$/g, '');
    const defs = {}, lines = [];
    for (const l of body.split('\n')) {
      const m = l.match(/^\[\^([^\]]+)\]:\s*(.+)$/);
      if (m) defs[m[1]] = m[2].trim(); else lines.push(l);
    }
    const nums = new Numbering(defs);
    // Footer links only for languages that exist; many posts are ko+en only.
    const have = [];
    for (const l of LANGS) if ((await fetch(`${postUrl}/index.${l[2]}.md`, {method: 'HEAD'})).ok) have.push(l);
    const content = [], images = [];
    let bullets = [];
    const flush = () => { if (bullets.length) { content.push({type: 'bullet_list', content: bullets}); bullets = []; } };
    const addImage = (name, alt, w, h, blob) => {
      images.push({name, blob, content: null});
      const node = imageNode('local:' + name, alt, w, h, blob ? blob.size : 0);
      images[images.length - 1].node = node;
      content.push(node);
    };

    st.step = 'convert';
    for (let i = 0; i < lines.length;) {
      const s = lines[i].trim();
      if (!s) { flush(); i++; continue; }
      if (s.startsWith('<div') && s.includes('fig-scroll')) {
        flush();
        const im = s.match(/<img src="([^"]+)" alt="([^"]*)"/);
        if (!im) throw new Error('figure wrapper without img: ' + s.slice(0, 80));
        const stem = im[1].split('/').pop().replace(/\.svg$/, '').replace(/\./g, '-');
        const name = `fig-${String(images.length + 1).padStart(2, '0')}-${stem}.png`;
        const r = CFG.dry ? {blob: null, w: 0, h: 0} : await svgToBlob(CFG.site + im[1]);
        addImage(name, unesc(im[2]), r.w, r.h, r.blob);
        i++; continue;
      }
      const mi = s.match(/^!\[([^\]]*)\]\(([^)\s]+)\)$/);
      if (mi) {
        flush();
        const stem = mi[2].split('/').pop().replace(/\.[a-z]+$/i, '').replace(/\./g, '-');
        const name = `fig-${String(images.length + 1).padStart(2, '0')}-${stem}.png`;
        const r = CFG.dry ? {blob: null, w: 0, h: 0} : await rasterUrl(mi[2].startsWith('/') ? CFG.site + mi[2] : mi[2]);
        addImage(name, unesc(mi[1]), r.w, r.h, r.blob);
        i++; continue;
      }
      if (s.startsWith('|')) {
        flush();
        let j = i;
        while (j < lines.length && lines[j].trim().startsWith('|')) j++;
        const [rows, aligns] = parseTable(lines.slice(i, j).map(l => l.trim()));
        const name = `table-${String(images.length + 1).padStart(2, '0')}.png`;
        const r = CFG.dry ? (rows.forEach(rw => rw.forEach(c => inlineHtml(c, nums))), {blob: null, w: 0, h: 0}) : await tableToBlob(rows, aligns, nums);
        addImage(name, 'Table: ' + rows[0].map(c => c.replace(/\[\^[^\]]+\]/g, '')).join(' | '), r.w, r.h, r.blob);
        i = j; continue;
      }
      if (/^[-*] /.test(s)) {
        bullets.push({type: 'list_item', content: [{type: 'paragraph', content: parseInline(s.slice(2), nums)}]});
        i++; continue;
      }
      flush();
      const hm = s.match(/^(#{1,4}) (.+)$/);
      if (hm) content.push({type: 'heading', attrs: {level: hm[1].length}, content: parseInline(hm[2], nums)});
      else if (['---', '***', '___'].includes(s)) content.push({type: 'horizontal_rule'});
      else if (s.startsWith('> ')) content.push({type: 'blockquote', content: [{type: 'paragraph', content: parseInline(s.slice(2), nums)}]});
      else content.push({type: 'paragraph', content: parseInline(s, nums)});
      i++;
    }
    flush();

    const em = {type: 'em'};
    const foot = [{type: 'text', text: 'This analysis is also available in ', marks: [em]}];
    have.forEach(([name, prefix], k) => {
      if (k) foot.push({type: 'text', text: k === have.length - 1 ? ', and ' : ', ', marks: [em]});
      foot.push({type: 'text', text: name, marks: [em, {type: 'link', attrs: {
        href: `${CFG.site}${prefix}/post/${meta.slug}/`, target: '_blank', rel: 'noopener noreferrer nofollow', class: null}}]});
    });
    foot.push({type: 'text', text: '.', marks: [em]});
    content.push({type: 'horizontal_rule'}, {type: 'paragraph', content: foot});
    nums.order.forEach((key, n) => content.push({type: 'footnote', attrs: {number: n + 1},
      content: [{type: 'paragraph', content: parseInline(defs[key], new Numbering({}))}]}));

    const doc = {type: 'doc', content};
    const stripped = JSON.stringify(content.filter(n => n.type !== 'captionedImage'));
    st.hash = await sha(stripped);
    st.summary = {blocks: content.length, images: images.length, footnotes: nums.order.length,
      unusedDefs: Object.keys(defs).filter(k => !nums.order.includes(k)).length};
    const bad = [];
    const lintWalk = n => {
      if (n.type === 'text') for (const re of window.__kiiLintRes) if (re.test(n.text)) bad.push(re.source + ': ' + n.text.slice(0, 80));
      if (n.type === 'text') bad.push(...window.__kiiBadLinks(n));
      if (n.type === 'image2' && window.__kiiAltRe.test(n.attrs.alt || '')) bad.push('alt entity: ' + n.attrs.alt.slice(0, 80));
      (n.content || []).forEach(lintWalk);
    };
    content.forEach(lintWalk);
    st.lint = bad.slice(0, 20);
    let desc = meta.description || '';
    if (desc.length > 240) desc = desc.slice(0, 237).replace(/\s+\S*$/, '') + '…';
    if (CFG.dry) { st.doc = doc; st.step = 'dry-done'; return; }
    if (bad.length) throw new Error('lint failed (' + bad.length + '): ' + bad[0]);

    st.total = images.length + 1;
    st.step = 'upload';
    const urls = {};
    for (const im of images) { urls['local:' + im.name] = await upload(im.blob); st.done++; }
    let cover = null;  // many posts have no cover file
    if (meta.image) {
      const cr = await fetch(`${postUrl}/${meta.image}`);
      if (cr.ok) cover = await upload(await cr.blob());
    }
    st.done++;
    const walk = n => { if (n.attrs && urls[n.attrs.src]) n.attrs.src = urls[n.attrs.src]; (n.content || []).forEach(walk); };
    walk(doc);
    st.step = 'save';
    const put = {draft_title: meta.title, draft_subtitle: desc, draft_body: JSON.stringify(doc)};
    if (cover) put.cover_image = cover;
    const r = await api('PUT', '/drafts/' + CFG.draft, put);
    st.result = {id: r.id, title: (r.draft_title || '').slice(0, 60), bodyLen: (r.draft_body || '').length};
    try { sessionStorage.setItem('kii-summary-' + CFG.draft, JSON.stringify(st.summary)); } catch (e) { /* verify takes expect */ }
    st.step = 'done';
  }
  run().catch(e => { st.error = String(e && e.stack || e).slice(0, 600); st.step = 'error'; });
  return 'started';
};

window.__kiiGetDraft = async draft => {
  const r = await fetch(`/api/v1/drafts/${draft}`, {credentials: 'same-origin'});
  if (!r.ok) throw new Error(`GET /drafts/${draft} ${r.status}`);
  return r.json();
};

// Reread the saved draft. expect defaults to the summary the last live __kiiRun for this
// draft kept in sessionStorage, so the check also works after reloading the tab.
window.__kiiVerify = async ({draft, expect} = {}) => {
  const d = await window.__kiiGetDraft(draft);
  const doc = JSON.parse(d.draft_body || '{"type":"doc","content":[]}');
  const got = {blocks: (doc.content || []).length, images: 0, footnotes: 0, notUploaded: 0};
  const lint = [], links = [];
  const walk = n => {
    if (n.type === 'captionedImage') got.images++;
    if (n.type === 'footnote') got.footnotes++;
    if (n.type === 'image2' && !/^https:\/\//.test((n.attrs || {}).src || '')) got.notUploaded++;
    if (n.type === 'text') for (const re of window.__kiiLintRes) if (re.test(n.text)) lint.push(re.source + ': ' + n.text.slice(0, 80));
    if (n.type === 'text') links.push(...window.__kiiBadLinks(n));
    if (n.type === 'image2' && window.__kiiAltRe.test((n.attrs || {}).alt || '')) lint.push('alt entity: ' + n.attrs.alt.slice(0, 80));
    (n.content || []).forEach(walk);
  };
  (doc.content || []).forEach(walk);
  let want = expect || null;
  if (!want) try { want = JSON.parse(sessionStorage.getItem('kii-summary-' + draft) || 'null'); } catch (e) { want = null; }
  const problems = [];
  if (!d.draft_title) problems.push('no title');
  if (got.notUploaded) problems.push(got.notUploaded + ' image(s) not uploaded');
  if (lint.length) problems.push('literal markdown/HTML: ' + lint[0]);
  if (links.length) problems.push(links.length + ' ' + links[0]);
  if (want) {
    for (const k of ['blocks', 'images', 'footnotes']) if (want[k] !== got[k]) problems.push(`${k} ${got[k]} != expected ${want[k]}`);
  } else {
    problems.push('no expected summary: run __kiiRun for this draft in this tab first, or pass expect');
  }
  return {ok: !problems.length, problems, got, expected: want, title: d.draft_title,
    published: !!d.is_published, slug: d.slug || null, lint: lint.slice(0, 10), links: links.slice(0, 10)};
};

// Publish the draft. A title already in the public archive (another post id) stops it,
// because an orphan draft of a post that already went out was republished on 2026-10-22.
window.__kiiPublish = async ({draft, send = true} = {}) => {
  const d = await window.__kiiGetDraft(draft);
  const title = (d.draft_title || '').trim();
  if (!title) throw new Error('draft has no title');
  if (d.is_published && send) throw new Error('already published; republish a fix with send:false');
  const norm = s => (s || '').toLowerCase().replace(/\s+/g, ' ').trim();
  const dup = [];
  for (let offset = 0; offset < 500; offset += 50) {
    const r = await fetch(`/api/v1/archive?sort=new&offset=${offset}&limit=50`, {credentials: 'same-origin'});
    if (!r.ok) throw new Error(`archive ${r.status}: cannot check for duplicates`);
    const page = await r.json();
    if (!Array.isArray(page) || !page.length) break;
    for (const p of page) if (p.id !== d.id && norm(p.title) === norm(title)) dup.push({id: p.id, slug: p.slug, date: p.post_date});
    if (page.length < 50) break;
  }
  if (dup.length) throw new Error('same title already published: ' + JSON.stringify(dup));
  const r = await fetch(`/api/v1/drafts/${draft}/publish`, {method: 'POST', credentials: 'same-origin',
    headers: {'Content-Type': 'application/json'}, body: JSON.stringify({send, type: 'new'})});
  const t = await r.text();
  if (!r.ok) throw new Error(`publish ${r.status} ${t.slice(0, 200)}`);
  const after = await window.__kiiGetDraft(draft);
  if (!after.is_published || !after.slug) throw new Error('publish call returned but the draft is not published');
  return {draftId: draft, slug: after.slug, url: `${location.origin}/p/${after.slug}`, emailed: send,
    postDate: after.post_date || null};
};

// Post the Note from a substack.com page (the feed API lives on that origin).
// The text matches substack_notes.build_note_text: description hook, then the post URL.
window.__kiiNote = async ({title = '', desc = '', url, max = 420} = {}) => {
  if (location.hostname !== 'substack.com') throw new Error('open a https://substack.com page first');
  if (!/^https:\/\/[a-z0-9-]+\.substack\.com\/p\/[A-Za-z0-9-]+\/?$/.test(url || '')) throw new Error('url must be the published post');
  let hook = (desc || '').replace(/\s+/g, ' ').trim().replace(/[ .…]+$/, '') || title;
  const budget = max - url.length - 5;
  if (hook.length > budget) hook = hook.slice(0, budget - 1).replace(/\s+\S*$/, '') + '…';
  const text = `${hook}\n\n→ ${url}`;
  const r = await fetch('/api/v1/comment/feed', {method: 'POST', credentials: 'same-origin',
    headers: {'Content-Type': 'application/json'}, body: JSON.stringify({
      bodyJson: {type: 'doc', attrs: {schemaVersion: 'v1'}, content: [{type: 'paragraph', content: [{type: 'text', text}]}]},
      tabId: 'for-you', surface: 'feed', replyMinimumRole: 'everyone'})});
  const t = await r.text();
  if (!r.ok) throw new Error(`note ${r.status} ${t.slice(0, 200)}`);
  const data = t ? JSON.parse(t) : {};
  const id = data.id || (data.comment || {}).id;
  if (!id) throw new Error('note response has no id: ' + t.slice(0, 200));
  return {noteId: id, noteUrl: `https://substack.com/note/c-${id}`, text};
};
'defined'

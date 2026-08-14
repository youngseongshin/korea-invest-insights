# -*- coding: utf-8 -*-
"""Inline-SVG chart primitives for korea-invest-insights posts.

Emits theme-aware SVG that uses the site's validated categorical CSS
variables (--kii-cat-1..5, defined in assets/css/site-enhancements.css)
so light and dark each render their own selected steps. Mark specs follow
the dataviz rules: thin marks, rounded data ends, hairline recessive grid,
legend for multi-series, selective direct labels only, and every figure
ships with a table-view twin via figure().

Usage from a scratchpad script:
    import sys; sys.path.insert(0, "/Users/youngseongshin/korea-invest-insights/scripts")
    from blog_viz import dbar, vbar, timeline, figure
"""

CAT = ["var(--kii-cat-1)", "var(--kii-cat-2)", "var(--kii-cat-3)",
       "var(--kii-cat-4)", "var(--kii-cat-5)"]
INK = "var(--card-text-color-main)"
INK2 = "var(--card-text-color-secondary)"
INK3 = "var(--card-text-color-tertiary)"
GRID = "var(--kii-chart-grid)"
AXIS = "var(--kii-chart-axis)"

# For rendering previews outside the site (rsvg-convert), substitute the
# CSS variables with the light-mode literals.
PREVIEW_SUBS = [
    ("var(--kii-cat-1)", "#0f8a70"), ("var(--kii-cat-2)", "#2563eb"),
    ("var(--kii-cat-3)", "#c8811a"), ("var(--kii-cat-4)", "#a13268"),
    ("var(--kii-cat-5)", "#6b4fc4"),
    ("var(--card-text-color-main)", "#22272e"),
    ("var(--card-text-color-secondary)", "#59625c"),
    ("var(--card-text-color-tertiary)", "#7a837d"),
    ("var(--kii-chart-grid)", "rgba(34,39,46,0.10)"),
    ("var(--kii-chart-axis)", "rgba(34,39,46,0.28)"),
]


def esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def dbar(rows, width=700, row_h=36, pad_l=150, pad_r=168, pad_t=18, pad_b=50,
         axis_label=None, lo=None, hi=None, ticks=None,
         fmt=lambda v: f"{v:+.2f}%", tick_fmt=lambda t: f"{t:+.0f}%"):
    """Diverging horizontal bars around a zero line.

    rows: list of (label, value) or (label, value, right_note).
    Positive bars use slot 1, negative slot 4.
    """
    n = len(rows)
    plot_w = width - pad_l - pad_r
    height = pad_t + n * row_h + pad_b
    vals = [r[1] for r in rows]
    lo = lo if lo is not None else min(min(vals), 0) * 1.15
    hi = hi if hi is not None else max(max(vals), 0) * 1.15
    span = hi - lo
    x0 = pad_l + plot_w * (0 - lo) / span
    out = [f'<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg" role="img">']
    for t in (ticks or []):
        x = pad_l + plot_w * (t - lo) / span
        out.append(f'<line x1="{x:.1f}" y1="{pad_t}" x2="{x:.1f}" y2="{pad_t+n*row_h:.1f}" stroke="{GRID}" stroke-width="1"/>')
        out.append(f'<text x="{x:.1f}" y="{pad_t+n*row_h+18:.1f}" fill="{INK3}" font-size="11" text-anchor="middle">{esc(tick_fmt(t))}</text>')
    for i, r in enumerate(rows):
        label, v = r[0], r[1]
        note = r[2] if len(r) > 2 else None
        y = pad_t + i * row_h + row_h / 2
        x = pad_l + plot_w * (v - lo) / span
        color = CAT[3] if v < 0 else CAT[0]
        bx, bw = min(x0, x), abs(x - x0)
        out.append(f'<text x="{pad_l-12}" y="{y+4:.1f}" fill="{INK}" font-size="12.5" text-anchor="end">{esc(label)}</text>')
        out.append(f'<rect x="{bx:.1f}" y="{y-8:.1f}" width="{max(bw,2):.1f}" height="16" rx="4" fill="{color}"/>')
        tx = (x + 9) if v >= 0 else (x - 9)
        anc = "start" if v >= 0 else "end"
        out.append(f'<text x="{tx:.1f}" y="{y+4:.1f}" fill="{INK}" font-size="12" font-weight="600" text-anchor="{anc}">{esc(fmt(v))}</text>')
        if note:
            out.append(f'<text x="{width-12:.1f}" y="{y+4:.1f}" fill="{INK3}" font-size="11" text-anchor="end">{esc(note)}</text>')
    out.append(f'<line x1="{x0:.1f}" y1="{pad_t}" x2="{x0:.1f}" y2="{pad_t+n*row_h:.1f}" stroke="{AXIS}" stroke-width="1.4"/>')
    if axis_label:
        out.append(f'<text x="{pad_l+plot_w/2:.1f}" y="{height-8}" fill="{INK3}" font-size="11.5" text-anchor="middle">{esc(axis_label)}</text>')
    out.append('</svg>')
    return "\n".join(out)


def vbar(cats, vals, notes=None, width=700, height=300, pad_l=60, pad_r=24,
         pad_t=40, pad_b=64, ticks=5, fmt=lambda v: f"{v:.0f}%", y_label=None,
         colors=None):
    """Vertical bars, one series; per-bar colors allowed for status contrast."""
    plot_w = width - pad_l - pad_r
    plot_h = height - pad_t - pad_b
    mx = max(vals) * 1.12
    bw = plot_w / len(cats) * 0.5
    out = [f'<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg" role="img">']
    for i in range(ticks + 1):
        v = mx * i / ticks
        y = pad_t + plot_h - plot_h * i / ticks
        out.append(f'<line x1="{pad_l}" y1="{y:.1f}" x2="{pad_l+plot_w:.1f}" y2="{y:.1f}" stroke="{GRID}" stroke-width="1"/>')
        out.append(f'<text x="{pad_l-9}" y="{y+4:.1f}" fill="{INK3}" font-size="11" text-anchor="end">{esc(fmt(v))}</text>')
    for i, (c, v) in enumerate(zip(cats, vals)):
        cx = pad_l + plot_w * (i + 0.5) / len(cats)
        bh = max(2.0, plot_h * v / mx)
        y = pad_t + plot_h - bh
        col = colors[i] if colors else CAT[0]
        out.append(f'<rect x="{cx-bw/2:.1f}" y="{y:.1f}" width="{bw:.1f}" height="{bh:.1f}" rx="4" fill="{col}"/>')
        out.append(f'<text x="{cx:.1f}" y="{y-8:.1f}" fill="{INK}" font-size="12.5" font-weight="600" text-anchor="middle">{esc(fmt(v))}</text>')
        out.append(f'<text x="{cx:.1f}" y="{pad_t+plot_h+20:.1f}" fill="{INK2}" font-size="12" text-anchor="middle">{esc(c)}</text>')
        if notes and notes[i]:
            out.append(f'<text x="{cx:.1f}" y="{pad_t+plot_h+38:.1f}" fill="{INK3}" font-size="10.5" text-anchor="middle">{esc(notes[i])}</text>')
    out.append(f'<line x1="{pad_l}" y1="{pad_t+plot_h:.1f}" x2="{pad_l+plot_w:.1f}" y2="{pad_t+plot_h:.1f}" stroke="{AXIS}" stroke-width="1"/>')
    if y_label:
        out.append(f'<text x="{pad_l}" y="{pad_t-16}" fill="{INK3}" font-size="11.5">{esc(y_label)}</text>')
    out.append('</svg>')
    return "\n".join(out)


def timeline(rows, width=700, pad_l=132, pad_t=26, row_h=54):
    """Vertical timeline. rows = (when, what, sub, kind), kind in now/soon/later."""
    n = len(rows)
    height = pad_t + n * row_h + 30
    out = [f'<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg" role="img">']
    x = pad_l
    out.append(f'<line x1="{x}" y1="{pad_t-6}" x2="{x}" y2="{pad_t+n*row_h-14:.0f}" stroke="{AXIS}" stroke-width="1.5"/>')
    for i, (when, what, sub, kind) in enumerate(rows):
        y = pad_t + i * row_h
        col = CAT[0] if kind == "now" else (CAT[2] if kind == "soon" else CAT[3])
        out.append(f'<text x="{x-16}" y="{y+4:.0f}" fill="{INK2}" font-size="12" font-weight="600" text-anchor="end">{esc(when)}</text>')
        out.append(f'<circle cx="{x}" cy="{y}" r="6" fill="{col}"/>')
        out.append(f'<circle cx="{x}" cy="{y}" r="9" fill="none" stroke="{col}" stroke-opacity="0.32" stroke-width="2"/>')
        out.append(f'<text x="{x+20}" y="{y+4:.0f}" fill="{INK}" font-size="13" font-weight="600">{esc(what)}</text>')
        out.append(f'<text x="{x+20}" y="{y+22:.0f}" fill="{INK3}" font-size="11.5">{esc(sub)}</text>')
    out.append('</svg>')
    return "\n".join(out)


def path_chart(points, width=700, height=286, pad_l=76, pad_r=110, pad_t=40,
               pad_b=56, y_label=None, base_label=None, fmt=lambda v: f"{v:,}"):
    """Line path with labelled points. points = (xlabel, value, sublabel)."""
    n = len(points)
    plot_w = width - pad_l - pad_r
    plot_h = height - pad_t - pad_b
    vals = [p[1] for p in points]
    lo, hi = min(vals) * 0.96, max(vals) * 1.04
    span = (hi - lo) or 1
    xs = [pad_l + plot_w * i / (n - 1) for i in range(n)]
    ys = [pad_t + plot_h - plot_h * (v - lo) / span for v in vals]
    out = [f'<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg" role="img">']
    for i in range(5):
        y = pad_t + plot_h * i / 4
        out.append(f'<line x1="{pad_l}" y1="{y:.1f}" x2="{pad_l+plot_w:.1f}" y2="{y:.1f}" stroke="{GRID}" stroke-width="1"/>')
    base = ys[0]
    out.append(f'<line x1="{pad_l}" y1="{base:.1f}" x2="{pad_l+plot_w:.1f}" y2="{base:.1f}" stroke="{AXIS}" stroke-width="1" stroke-opacity="0.55"/>')
    if base_label:
        out.append(f'<text x="{pad_l+plot_w+8:.1f}" y="{base+4:.1f}" fill="{INK3}" font-size="11">{esc(base_label)}</text>')
    d = " ".join(("M" if i == 0 else "L") + f" {xs[i]:.1f} {ys[i]:.1f}" for i in range(n))
    out.append(f'<path d="{d}" fill="none" stroke="{CAT[0]}" stroke-width="2.2" stroke-linejoin="round"/>')
    for i, (lab, v, sub) in enumerate(points):
        col = CAT[3] if i == n - 1 else CAT[0]
        out.append(f'<circle cx="{xs[i]:.1f}" cy="{ys[i]:.1f}" r="5.5" fill="{col}"/>')
        out.append(f'<circle cx="{xs[i]:.1f}" cy="{ys[i]:.1f}" r="8.5" fill="none" stroke="{col}" stroke-opacity="0.3" stroke-width="2"/>')
        dy = -16 if i % 2 == 0 else 24
        out.append(f'<text x="{xs[i]:.1f}" y="{ys[i]+dy:.1f}" fill="{INK}" font-size="12" font-weight="600" text-anchor="middle">{esc(fmt(v))}</text>')
        out.append(f'<text x="{xs[i]:.1f}" y="{pad_t+plot_h+20:.1f}" fill="{INK2}" font-size="12" text-anchor="middle">{esc(lab)}</text>')
        if sub:
            out.append(f'<text x="{xs[i]:.1f}" y="{pad_t+plot_h+37:.1f}" fill="{INK3}" font-size="10.5" text-anchor="middle">{esc(sub)}</text>')
    if y_label:
        out.append(f'<text x="{pad_l}" y="{pad_t-16}" fill="{INK3}" font-size="11.5">{esc(y_label)}</text>')
    out.append('</svg>')
    return "\n".join(out)


def figure(svg, caption, table_md=None, table_summary="표로 보기"):
    """Wrap an SVG in the site figure shell with its table-view twin."""
    parts = ['<figure class="kii-figure">',
             '<div class="kii-figure__frame">', svg, '</div>',
             f'<figcaption>{caption}</figcaption>']
    if table_md:
        parts.append(f'<details class="kii-figure__table"><summary>{table_summary}</summary>')
        parts.append("")
        parts.append(table_md.strip())
        parts.append("")
        parts.append('</details>')
    parts.append('</figure>')
    return "\n".join(parts)


def assemble(lang, src, dst, figs_dir, captions, summary=None):
    """Replace <<<FIGN>>> placeholders in src with figure blocks, write dst.

    captions: {n: (caption_html, table_md_or_None)}; SVG files are
    f"{figs_dir}/fig{n}_{lang}.svg".
    """
    import io, os
    summary = summary or ("표로 보기" if lang == "ko" else "View as table")
    body = io.open(src, encoding="utf-8").read()
    for n in sorted(captions):
        svg = io.open(os.path.join(figs_dir, f"fig{n}_{lang}.svg"), encoding="utf-8").read()
        cap, tbl = captions[n]
        token = f"<<<FIG{n}>>>"
        if token not in body:
            print("!! missing token", token)
        body = body.replace(token, figure(svg, cap, tbl, summary))
    io.open(dst, "w", encoding="utf-8").write(body)
    print("assembled", dst, len(body))

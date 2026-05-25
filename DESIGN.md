# Korea Invest Insights Design System

## Direction

Use a restrained editorial research style:

- Editorial density: premium finance/research note, not SaaS landing page.
- Data order: tables and numbers should feel precise, compact, and scannable.
- Quiet surfaces: panels should be separated by spacing, tone, and shadow rather than visible borders.

The desired mood is:

> Graphite Sage research surfaces + restrained Cobalt action/link accents.

## Palette

- Page background: warm stone / graphite paper, around `#f7f7f4`.
- Card surface: warm white, around `#fffefa`.
- Primary text: graphite, around `#22272e`.
- Secondary text: muted graphite/sage, around `#59625c`.
- Quiet surface tint: muted sage, around `#2f7d6b` at low alpha.
- Action/link accent: cobalt, around `#2563eb`.

Use sage for calm UI surfaces, table hover states, summary boxes, hub cards, and quiet chips.
Use cobalt only for true actions: links, active TOC, progress bar, buttons, and copied/share states.

## Typography

- Headings: editorial serif.
- Body: clean sans with Korean readability.
- Numbers: tabular numerals wherever possible.
- Do not use negative letter spacing.
- Do not scale font size directly with viewport width except existing clamp-based headings.

## Layout

- Article body should be wide enough for research paragraphs and tables, but not full bleed.
- Keep article/card radius small: 6-8px.
- Avoid nested cards.
- Avoid heavy borders. Section/card borders should usually be transparent.
- Prefer spacing, quiet background tint, and subtle shadow for hierarchy.

## Tables

- Table wrapper outer border should be transparent.
- Table should be centered within the article content width.
- Keep internal cell hairlines for data readability.
- Header row should be pale graphite/sage, not bright blue.
- Numbers should be right-aligned and tabular.
- Mobile tables must retain horizontal scrolling.

## Callouts

- TL;DR / 핵심 요약 blocks should use soft sage background and no visible border.
- Avoid thick left accent bars unless the block is a warning or high-priority alert.

## Avoid

- Gradient orbs, bokeh blobs, neon glow, glassmorphism, and AI/SaaS hero styling.
- Oversized bento cards for dense research pages.
- Purple/blue gradient-heavy palettes.
- Large decorative cards inside other cards.
- Marketing-copy sections that explain how to use the site.

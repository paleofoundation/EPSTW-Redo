# sustainabilitydiet.com — site build

**Stack:** Astro 5 + Tailwind CSS 3. Static output, deployed to Vercel.

**Domain:** sustainabilitydiet.com (registered, not yet pointed at the deploy — DNS step pending). Vercel preview alias: `https://sustainabilitydiet.vercel.app`.

---

## Session log

### Session 7 — 2026-05-01

**Objective:** Get the site off Karen's laptop and onto a real URL. Hand Vercel a `vercel.json` that does the build correctly without the file:// rewrite step, ship a one-line `deploy.sh` for Karen to run, walk her through the first-time auth, and verify pages render correctly from the CDN.

**What shipped:**

- `site/vercel.json` — explicit build config so Vercel runs `npm run build:only` (skipping the `rewrite-for-file-protocol.py` step that's only needed for local file:// viewing). Astro framework auto-detected, output directory `dist`, clean URLs on, trailing slash off.
- `site/deploy.sh` — one-liner wrapper around `npx vercel deploy --prod --yes --name sustainabilitydiet`. Karen runs it from Terminal; first run authenticates via browser, subsequent runs deploy silently.
- **Production deploy live.** Vercel project `karen-pendergrass-projects/sustainabilitydiet` created, linked to `site/`, deployed in 18s. Aliased to `https://sustainabilitydiet.vercel.app`. Verified: homepage HTTP 200, full HTML rendering, CSS loaded from `/_astro/...` absolute paths, JSON-LD shipped, all flip-the-land Session 6 copy live in `/one-hundred-camels/the-experiment`.
- Custom domain (`sustainabilitydiet.com`) — DNS step deferred to Karen.

**Still not shipped (carries to Session 8):**

- Custom domain pointed at the Vercel deploy.
- Real favicon glyph, book cover artwork, OG image (meta wired; image asset still missing).
- Self-hosted fonts (eliminates Google Fonts privacy line).
- ESP backend for ContactForm (still mailto).
- Real author headshot for /about.
- Vignette #1 hero map (highest-visibility placeholder).
- Per-page OG images.
- Automated link-check in build.

### Session 6 — 2026-04-19

**Objective:** Flip-the-land reframe. Karen pushed back on two things: the 25-year timeline ("I bet we could run it in 5") and the missing house-flip register ("Is there anything in here about flipping the desertified and unproductive land like the way one might flip houses?"). The Epilogue already contains that language — the revised book dated 2026-04-18 says *"bought distressed… running as a closed-loop system for a decade with honest monitoring… sold, or kept, or left to the commons."* The site hadn't absorbed it. This session routes the flip frame into the site, collapses the timeline into a five-year MVP + ten-year flip + (optional) twenty-five-year coda, and gives the proposal four named exit dispositions it previously lacked.

**What shipped:**

- **New Section 02 on `/one-hundred-camels/the-experiment` — "What flipping the ground means here."** Opens with the Epilogue passage set as a blockquote. Four disposition cards (A: Sold at restored valuation / B: Retained and extended / C: Easement-protected / D: Returned to the commons). Closes with a framing sentence that explicitly positions the project alongside a house flip: *the restoration register is the same; the ground is the asset; the exit is defined in advance.* All downstream sections (03–14) renumbered accordingly.
- **Section 09 Timeline rewritten.** Was "25-year timeline" as a monolith. Now: Years 0–1 acquisition and stand-up, Years 1–5 MVP gate (answers gut germination, dispersal, early ground cover, infiltration, welfare), Years 5–10 flip window (answers soil carbon at 10–30 cm, recruitment into the canopy, whether the system is running without us), Years 10–25 optional coda (tree-generation questions that most funders and landowners should not be asked to underwrite in advance). Closing sentence: *"The headline commitment is five years. The fundable commitment is ten. Twenty-five is the answer to a specific tree-generation question."*
- **Section 11 Failure criteria split into Year-5 and Year-10 gates.** Year-5 gate (4 criteria) runs the MVP-kill logic. Year-10 gate (3 criteria) runs the flip-or-keep logic. Two separate falsification moments instead of one terminal one.
- **Section 13 "What is being asked" rewritten around phased capital.** Two-card grid — Phase 1 MVP (Y0–5, named dollar range) and Phase 2 Flip (Y5–10, named dollar range). Closes with an italic coda distinguishing the patron-funder (who asks "what did we prove") from the underwriter-funder (who asks "what's the exit") — the proposal is legible to both.
- **Landing page `/one-hundred-camels` experiment card rewritten.** Was "Fifteen sections, a twenty-five-year timeline." Now names the land-flip framing, the five-year MVP gate, the ten-year flip window, the four pre-defined exits, and the falsification list at two gates.
- **Homepage `/` gained a third thesis paragraph** in the disease-framing block: the flip register stated plainly — *"buy a parcel that has been desertifying for a century at its distressed basis, put the right animals and the right trees on it, run it as a closed-loop system for a decade with honest monitoring, and let the exit be defined in advance — sold, kept, easement-protected, or returned to the commons."* ToolCard blurb for One Hundred Camels updated to mirror.
- **Page meta description updated** to lead with the flip frame. Base TOC expanded to 16 items (s01–s14 + open-letter + contact).
- **Changelog entry.** Session 6 logged to `/changelog` with five change items. Dated 2026-04-19.
- **Rebuild clean.** Post-process rewrote 28 files for file:// viewing. `grep` for leaked absolute hrefs → empty. `grep` for leaked unicode escapes → empty. `grep -o 'flipping the ground' dist/one-hundred-camels/the-experiment/index.html` → 3 matches (confirms reframe shipped).

**Still not shipped (carries to Session 7):**

- Real hero-map, phylogeny, body-size, assemblage, plant-disperser, extinction-timeline, address-lookup, and project-cards components on Vignette #1 (still styled placeholders).
- Real favicon glyph, book cover artwork, OG social image.
- Self-hosted fonts.
- Vercel deploy.
- ESP backend (Buttondown or equivalent).
- Real author headshot.
- Vignette #2 (The Horse, Returning Native).

### Session 5 — 2026-04-19

**Objective:** Close the last placeholder page, add long-page navigation, and polish the reading experience. Convert `/fourth-axis` from placeholder to real page, add jump-nav TOCs on the two longest pages, standardize focus rings across the site, add a reading-progress bar on long-form pages, widen footer coverage, and refresh the sitemap and rewrite script to match.

**What shipped:**

- **`/fourth-axis` promoted from placeholder.** Full narrative page drawn from Chapter 4. Virginia-poultry opening, four-axes grid (calories/nutrients/environmental-externalities with the fourth — survivability — highlighted as a framed "second-order" axis), "What the axis asks" (the three proxy questions: what does the land eat, would it feed itself if we stopped, would the water still run), intellectual-lineage block citing Holling 1973 and Taleb, "What the axis does not do" (four bounded-claim statements to prevent the concept from overreaching), and a "Where the axis is applied" grid linking to the experiment, the atlas, the orphaned-fruits matrix, and the proxies matrix. Italic closing pull-quote. This closes the last placeholder page in the nav.
- **Jump-nav TOC on `/one-hundred-camels/the-experiment`.** Zero-JS `<details open>` disclosure with a 2-column grid listing all fifteen sections (the 13 numbered sections plus open-letter + contact). Each section got `id="sNN"` + `scroll-mt-24` for a clean anchor-offset on jump.
- **Jump-nav on `/one-hundred-camels/critics`.** 4-item vertical nav (left-border accent) linking to Caro, Rubenstein, Oliveira-Santos, and "what the critics get right." Same `scroll-mt-24` treatment.
- **Standardized focus rings.** Added `:focus-visible { outline: 2px solid #7A4F2D; outline-offset: 2px; border-radius: 1px }` in the base layer, with `:focus { outline: none }` to suppress the mouse-click focus outline. Now every keyboard-tab through the site shows the same ochre-deep ring.
- **Reading-progress bar.** 2px ochre bar across the top of the viewport on long-form pages, implemented with CSS scroll-driven animations (`animation-timeline: scroll(root block)`). Opt-in via a `readingBar` prop on `<Base>` — enabled on 17 long-form pages (Prologue, experiment, critics, bibliography, timeline, glossary, sources, orphaned-fruits, proxies, the seed-dispersal essay, etc.). Hidden in print. Gracefully degrades on browsers without scroll-timeline support (no JS fallback; the bar just doesn't render).
- **Footer expanded.** Added `/start`, `/fourth-axis`, `/near-time/further-reading` to the existing nav columns, and split out a new "Site" subsection (FAQ, Site map, Changelog) in the right-most column between About and Legal.
- **Sitemap refreshed.** Expanded from 22 → 27 URLs (added `/start`, `/faq`, `/fourth-axis`, `/near-time/further-reading`, `/changelog`, `/map` — the routes that existed but weren't in the sitemap yet), regrouped logically.
- **Rewrite script updated.** Added the five missing INTERNAL_ROUTES entries (`/near-time/further-reading`, `/changelog`, `/start`, `/map`, `/faq`) so file:// viewing works for every route in the sitemap.
- **Fix: `/the-book` ContactForm invocation.** Pre-existing mismatch from Session 4 — the-book.astro was passing `options={…}` + `defaultInquiryType="…"` to `ContactForm`, but the component's real API is `idPrefix` + `categories`. Fixed + re-built cleanly. Categorized as Reader-updates / Press / Editorial.
- **Fix: unicode-escape leakage on `/the-book`.** Five `\u2019` / `\u2013` sequences were rendering as literal escape sequences in JSX text nodes. Replaced with actual Unicode characters. (Third time this bug has bitten the project — reminder for future sessions: inside JSX text children, escape sequences do **not** evaluate; they only work inside frontmatter string literals.)
- **Rebuild clean.** 27 HTML files rendered. Post-process rewrote 28 files for file:// viewing. `grep` for leaked absolute `/` hrefs → empty. `grep` for leaked `\u` escapes → empty.

**Still not shipped (carries to Session 6):**

- Real hero-map, phylogeny, body-size, assemblage, plant-disperser, extinction-timeline, address-lookup, and project-cards components on Vignette #1 (still styled placeholders).
- Real favicon glyph, book cover artwork, OG social image.
- Self-hosted fonts.
- Vercel deploy.
- ESP backend (Buttondown or equivalent).
- Real author headshot.
- Vignette #2 (The Horse, Returning Native).

### Session 4 — 2026-04-18 (overnight)

**Objective:** Autonomy pass. Karen granted full creative/technical autonomy and asked for proactive gap-closure beyond the stated backlog. Built the pages she'd explicitly named (the orphaned-fruits matrix and the proxy-substitution matrix, both of which she'd sketched in an earlier conversation), plus a set of pages I judged the site needed to be genuinely credible — a critics-in-their-own-voice page, a concrete contribute page, a bibliography, a full timeline, a 404, a mobile nav, a print stylesheet, an RSS feed, a cite-this-site block, and two new index pages that actually link to the new material.

**What shipped:**

- **`/near-time/orphaned-fruits`.** Janzen-Martin table. Ten plants (osage orange, honey locust, Kentucky coffeetree, avocado, pawpaw, persimmon, buffalo gourd, mastodon grape, honey mesquite, black walnut), each with the fossil disperser, the mouth doing the work now, and an A/B/C confidence rating on how well-supported the anachronism case is. Four closing commentary sections on what the table does and does not prove.
- **`/near-time/proxies`.** Taxon-substitution matrix in four groups — Large grazers and browsers, Apex and mesopredators, Armored and reptilian herbivores, and "The holes." Fourteen entries. Each row names the extinct taxon, its mass, its likely ecological role, the candidate proxy (if any), the rationale, and the leading objection. "The holes" row explicitly documents niches (ground sloth, saber-tooth) for which no viable proxy exists — scientific-honesty move.
- **`/one-hundred-camels/critics`.** Steel-manned critics page. Caro (2007, TREE), Rubenstein et al. (2006, Biological Conservation), Oliveira-Santos & Fernandez (2010, Conservation Biology) — each argument written in the critic's voice, then a considered response in Karen's. Closing "what the critics get right" section.
- **`/one-hundred-camels/contribute`.** Ten concrete categories of help (land, veterinary specialists, archaeologists, camelid practitioners, foundations, legal counsel, volunteers, scientific advisors, rewilding-practitioner peers, readers-who-pass-it-along). Each category is a prose block; the ContactForm at the bottom mirrors the same taxonomy so readers can self-route.
- **`/near-time/bibliography`.** Six-group Chicago-ish reference list (Foundational synthesis, Pleistocene-rewilding proposal and critics, Orphaned fruits, Camelops/Camelidae, Adjacent projects, Primary data sources). Each entry has citation, DOI where available, and a one-line editorial note explaining why the work is here.
- **`/near-time/timeline`.** Vertical timeline from ~70 kya (humans reach Australia) to ~2026 (the experiment this site proposes). Seventeen events across late-Pleistocene, terminal-Pleistocene, Holocene, historical, modern, and present eras. Era-colored dots; responsive layout (dates stack above on mobile, left-column on desktop).
- **`/field-notes/seed-dispersal`.** First real Field Note, drawn from the seed-dispersal fragment in `WEBSITE_IDEAS.md`. Drop cap, twelve prose paragraphs, full essay on megafaunal fruit syndrome and half-honoring the evolutionary contract.
- **`/field-notes` index rebuilt.** Published essays + a "planned" column sketching three more Field Notes in the pipeline. Links to the RSS feed.
- **`/404`.** "Orphaned page" 404 matching the design system, with a grid of the eight main routes so the page doubles as a site map.
- **RSS feed.** Static `public/feed.xml` with one item (the seed-dispersal essay). `<link rel="alternate" type="application/rss+xml">` in every page's `<head>` for auto-discovery. Static file instead of `@astrojs/rss` — no new npm dependency.
- **Print stylesheet.** `@media print` block in `global.css` hides nav/footer, switches to white bg / black text / serif, adds the URL after each link as `(https://...)`, re-sizes typography to pt-based. Long-form pages (Prologue, experiment, critics) now print cleanly.
- **Mobile hamburger nav.** Zero-JS `<details>`/`<summary>` pattern with inline SVG menu/close icon swap via `group-open:hidden`/`group-open:block`. Preserves the "no JS runtime required" site principle. Desktop behavior unchanged.
- **Cite-this-site block on `/near-time/sources`.** Three pre-formatted citation strings (Chicago, APA, MLA) in `<pre>` blocks, copy-pasteable, with live date auto-inserted.
- **Open letter on the experiment page.** Section 14 added: open-letter block with mailto form using `Inquiry-type=Open-letter` so sign-ons route distinctly. Renumbered the prior Contact section to 15.
- **Experiment page — honest correction.** Caught and removed a fabricated "eight silent signatories" line that had slipped into the open-letter draft. Not entitled to make that claim on Karen's behalf. Replaced with neutral placeholder.
- **`/near-time/` landing rebuilt from placeholder.** Proper atlas index: hero story card (the one-hundred-camels vignette), matrices group (orphaned-fruits + proxies), reference group (timeline, bibliography, glossary, sources).
- **`/one-hundred-camels/` landing updated.** New "Think alongside" family added between the experiment card and adjacent projects; links to `/critics` and `/contribute`. Old inline critics blurbs removed (now handled in depth on the dedicated page).
- **Footer expanded.** Four-column → five-column layout. Separate "Near Time" column (atlas reference pages) and "The experiment" column (experiment + critics + contribute + field-notes + RSS). Brand block and About/Legal column unchanged.
- **Sitemap expanded to 22 URLs.** Added orphaned-fruits, proxies, timeline, bibliography, critics, contribute, seed-dispersal.
- **Rewrite script updated.** Seven new INTERNAL_ROUTES entries, three new ASSETS entries (feed.xml, robots.txt, sitemap.xml). 23 HTML files rewrote cleanly for file:// viewing.
- **Rebuild clean.** 23 routes rendered. Zero absolute `/` hrefs in any built HTML. Spot-checked the Footer experimentNav column renders correctly and the unicode em-dashes/apostrophes landed as literal characters, not escape sequences.

**Still not shipped (carries to Session 5):**

- Real hero-map, phylogeny, body-size, assemblage, plant-disperser, extinction-timeline, address-lookup, and project-cards components on Vignette #1 (still placeholder cards).
- `/fourth-axis` scoring interactive — still a placeholder.
- Real favicon glyph, book cover artwork, OG social image.
- Self-hosted fonts.
- Vercel deploy.
- ESP backend (Buttondown or equivalent).
- Real author headshot.

### Session 3 — 2026-04-18 (late evening)

**Objective:** Gap-closure pass. Raise the site from Session-2 state (framework-pitch → experiment-invitation, four real pages) to a credible public-facing state. Close the believability gaps around the $1.5M proposal, pre-answer the predictable objections, name the family of adjacent work, give readers a reference layer (glossary, sources), add segmented contact capture, ship the missing legal/attribution stubs, wire the SEO plumbing, and do the overdue accessibility work.

**What shipped:**

- **Experiment page expanded.** Two new sections. Section 04 "The family of work" puts the experiment in context alongside American Prairie, Pleistocene Park, Armendaris/Bolson tortoise, and Oostvaardersplassen/Knepp — each card framed as "what this borrows / what this changes." Section 11 "What we hear most, answered" pre-addresses the six recurring objections (invasive-species framing, disease risk, water, welfare, ethics of assisted migration, "why not bison"). Section 14 now includes the segmented contact form inline.
- **`/near-time/glossary`.** 24 alphabetized terms (assisted migration, atavism, baseline, charismatic megafauna, coextinction, coevolution, dung beetle, ecological release, ecosystem engineer, extant, extirpation, functional analog, Holocene, keystone species, LGM, megaherbivore, mesic, Near Time, no-analog community, novel ecosystem, Pleistocene Park, rewilding, SNT, taxon substitution). Jump-index nav, scroll-mt-24 for anchor offset, cross-links to sources.
- **`/near-time/sources`.** Methodology page: named synthesis works (Martin 2005, MacPhee 1999, Janzen-Martin 1982, Donlan 2005), primary datasets with licenses (PBDB, Neotoma, GBIF, iNaturalist), screening and cutoff conventions, uncertainty posture, interactive-components policy, editorial voice, attribution.
- **`/one-hundred-camels/` landing.** Replaced placeholder. Indexes three families: the experiment (emphasis card), adjacent projects (5 cards), critics and counter-positions (3 named: Rubenstein 2016, Caro 2007, Donlan 2005 as lightning rod).
- **About page rewritten.** Added Paleo Foundation section (what it is, why the author runs it, how the book came out of that work), headshot placeholder grid (dashed-border, aria-hidden — needs real photos), Person JSON-LD, and the segmented contact form inline.
- **Segmented contact form component.** New reusable `ContactForm.astro` with 7 radio categories (Editorial / Press / Land / Capital / Scientific / Correction / Reader updates). Uses `mailto:karen@paleofoundation.com` with `enctype="text/plain"` and subject-prefix pattern — no ESP backend required for V1.
- **Post-Prologue runway.** Excerpt page now has a bone/30 aside before the CTAs with a short promise ("two notes over the next year or so, both short, both specific") and an inline email form using the Reader-updates hidden inquiry-type.
- **Privacy, Terms, Data Attribution stubs.** All three live at `/privacy`, `/terms`, `/data-attribution`. Privacy documents Google Fonts + mailto behavior. Terms covers copyright, data-license respect, no-advice disclaimer. Data Attribution has per-source blocks for PBDB (CC-BY), Neotoma (CC-BY-4.0), USDA PLANTS (public domain), GBIF, iNaturalist, Natural Earth + OpenStreetMap, and Fonts (SIL OFL).
- **Footer upgrade.** Four-column grid with brand block (Paleo Foundation attribution line), The book nav, The atlas nav (incl. glossary + sources), About nav, Legal nav. Copyright line + data-attribution note at the bottom border.
- **SEO + accessibility plumbing.** Base layout extended with canonical, ogType, ogImage, twitter card, optional JSON-LD script. Homepage ships Book + WebSite JSON-LD. About ships Person JSON-LD. Skip-to-content link at the top of every page (sr-only / focus:not-sr-only pattern). `<main id="main-content">` anchor.
- **robots.txt + sitemap.xml.** `User-agent: *` allow-all. Sitemap lists 15 URLs with priority and changefreq.
- **Color contrast audit.** Introduced `ochre-deep` (`#7A4F2D`, 6.1:1 vs paper) as the body-text-link token. CSS rule in `global.css` auto-promotes `a.text-ochre` to the deeper shade inside `.prose-reading`. The original ochre (4.05:1) is retained for kickers, display headings, buttons, and borders (all of which either pass large-text AA or are non-content UI). `dust` is now documented as reserved-for-non-text. Audit write-up at `/site/CONTRAST_AUDIT.md`.
- **Rewrite script updated.** `/near-time/glossary`, `/near-time/sources`, `/privacy`, `/terms`, `/data-attribution` added to INTERNAL_ROUTES (nested routes before their parents, per the existing ordering rule).
- **Rebuild clean.** 15 routes rendered. Post-process rewrote 15 HTML files for file:// viewing. No absolute hrefs remaining in `dist/`.

**Still not shipped:**

- Real author headshot (About page has a dashed-border placeholder grid). Needs a user-supplied photo.
- Real hero-map, phylogeny, body-size, assemblage, plant-disperser, extinction-timeline, address-lookup, and project-cards components (Vignette #1 still renders styled placeholders).
- `/fourth-axis` scoring interactive — still a placeholder.
- `/field-notes` — still a placeholder.
- Book cover artwork, favicon glyph, Open Graph social image (OG meta-tag is wired; image asset is not).
- Self-hosted fonts.
- Vercel deploy.
- ESP backend (mailto forms ship instead; Buttondown wiring is a future decision).

### Session 2 — 2026-04-18 (evening)

**Objective:** Repositioning session. Shift the site from framework-pitch to experiment-invitation. Ship the Prologue, the Vignette #1 content, a real About page, and the proposal page that converts the book's argument into something a landowner or funder can act on. Continue to the point Karen can visualize the shape of the finished site.

**What shipped:**

- **Homepage redraft.** Hero now anchors "what the land eats" with the concrete grazers / browsers / seed-carriers beat. New thesis block leads with desertification-as-disease and ends with an explicit invitation to run the experiment. Primary CTA points at the proposal page. One Hundred Camels tool blurb reframed from "rewilding projects" to "the experiment we're asking to run."
- **`/the-book/excerpt`.** Full Prologue, typeset for reading — Source Serif 4, drop cap on the opening paragraph, two display-weight pull-quotes for the library/librarians line and the one-hundred-camels line, proper endnotes, jump-back arrows. CTAs at the end to the atlas vignette and to the proposal.
- **`/one-hundred-camels/the-experiment`.** Twelve-section proposal: the wish, the hypothesis, why camels and osage, site characteristics, herd, plantings, 25-year timeline, measurement list, pre-registered failure criteria, what is being asked (land / capital / permissions / time / a committee that holds back), honest exclusions (not tourism, not a Paleo-branded program, not a one-shot proof), and contact.
- **`/near-time/stories/one-hundred-camels`.** The real Vignette #1 built from VIGNETTE_01_ONE_HUNDRED_CAMELS_v1.0.md. Eight content panels. Thirty-one footnotes with in-page jump-back anchors. Interactive-component placeholders are styled cards that state what each component will do when built.
- **About page promoted from placeholder.** Martin dedication moved off the homepage to here. Author note (Karen, Paleo Foundation, the fourteen-year arc, why the earlier manuscript not publishing turned out to be a gift). Contact + press anchors. Data/methodology note.
- **`npm install` completed.** Full Astro + Tailwind toolchain is now resident in the workspace. Build verified clean (10 routes, ~2.2s total build time).
- **Rewrite script extended.** Now handles nested routes (`/the-book/excerpt`, `/one-hundred-camels/the-experiment`, `/near-time/stories/one-hundred-camels`) and href fragments (`#contact`, `#press`, `#prologue`). Built into the default `npm run build` pipeline.

**Still not shipped:**

- Real hero-map, phylogeny, body-size, assemblage, plant-disperser, extinction-timeline, address-lookup, and project-cards components (Vignette #1 renders styled placeholders for each).
- `/fourth-axis` scoring interactive — still a placeholder.
- `/one-hundred-camels/` landing index — still a placeholder. The experiment page is reachable directly via the homepage CTA.
- `/field-notes` — still a placeholder.
- Book cover artwork, favicon glyph, Open Graph image.
- Self-hosted fonts.
- Vercel deploy.
- Email capture.

### Session 1 — 2026-04-18

**Objective:** Stand up the site skeleton. Homepage renders in a browser. Nav links do not 404.

**What shipped:**

- Homepage (`/`) with hero, three-tool grid, book section, closing beat.
- Placeholder pages at `/the-book`, `/near-time`, `/fourth-axis`, `/one-hundred-camels`, `/field-notes`, `/about`.
- Reusable `Base` layout, `Nav`, `Footer`, `ToolCard`, `PlaceholderPage` components.
- Typographic system: Fraunces (display), Inter (body), Source Serif 4 (reading). Loaded from Google Fonts — swap to self-hosted for production.
- Color system: paper `#F6F2EA`, ink `#1F1D1B`, bone `#E8DFCE`, ochre `#9C6B3F`, moss `#5C6B4F`, dust `#8B7F6E`.

---

## View the homepage right now

You don't need to install anything.

Double-click `site/dist/index.html` to open the built static homepage in your default browser. The nav links and the three tool cards are live and navigate between the placeholder pages.

**How this works:** Astro emits root-absolute paths (`/_astro/foo.css`) that a browser resolves against the filesystem root under `file://`, so CSS never loads and the page renders raw. The `build` script runs a post-processing step (`scripts/rewrite-for-file-protocol.py`) that rewrites those to depth-relative paths so `file://` viewing works out of the box.

**Caveat:** some browsers block Google Fonts loading over `file://`. If the type looks wrong (falls back to Georgia / system sans), it's the font-loading quirk — it will resolve the moment the site is served from a local server or a real host.

---

## Iterate with a live dev server

Requires Node.js 18+ on your machine. Recommended install method on macOS: [nvm](https://github.com/nvm-sh/nvm) or [Homebrew](https://brew.sh) (`brew install node`).

From Terminal:

```bash
cd "/path/to/EPSTW Redo/site"
npm install
npm run dev
```

The dev server starts at http://localhost:4321 with hot reload. Leave it running; every file save re-renders in the browser within a second.

To produce a fresh production build:

```bash
npm run build
```

Output goes to `site/dist/`.

---

## Project layout

```
site/
├── package.json            Astro + Tailwind dependencies
├── astro.config.mjs        Astro site config
├── tailwind.config.mjs     Design tokens (colors, fonts, max-widths)
├── tsconfig.json           TypeScript strict config
├── .gitignore              Standard Node / Astro ignores
│
├── public/                 Static assets served at site root
│   └── favicon.svg
│
├── src/
│   ├── layouts/
│   │   ├── Base.astro              HTML shell, loads CSS, renders Nav/Footer
│   │   └── PlaceholderPage.astro   Common shape for "under construction" pages
│   ├── components/
│   │   ├── Nav.astro               Top navigation
│   │   ├── Footer.astro            Site footer
│   │   └── ToolCard.astro          Reusable tool card (used on homepage)
│   ├── pages/
│   │   ├── index.astro             Homepage
│   │   ├── the-book.astro          Placeholder
│   │   ├── near-time.astro         Placeholder
│   │   ├── fourth-axis.astro       Placeholder
│   │   ├── one-hundred-camels.astro   Placeholder
│   │   ├── field-notes.astro       Placeholder
│   │   └── about.astro             Placeholder
│   └── styles/
│       └── global.css              Font imports, Tailwind layers, base styles
│
└── dist/                   Built static site (committed here for immediate viewing;
                            in production this is regenerated by CI)
```

---

## Design tokens (locked for now; revisable)

| Token     | Hex       | Role                                       |
|-----------|-----------|--------------------------------------------|
| `paper`   | `#F6F2EA` | Page background                            |
| `ink`     | `#1F1D1B` | Body text, primary buttons                 |
| `bone`    | `#E8DFCE` | Soft panels, book-cover card background    |
| `ochre`   | `#9C6B3F` | Accent — kicker labels, display headings, button bg, borders (large-text AA; 4.05:1) |
| `ochre-deep` | `#7A4F2D` | Body-text links (WCAG AA normal; 6.10:1) — auto-applied to `a.text-ochre` inside `.prose-reading` |
| `moss`    | `#5C6B4F` | Secondary accent (AA normal; 5.33:1)       |
| `dust`    | `#8B7F6E` | Reserved — large-text or non-text UI only (fails AA normal; 3.52:1) |

Type pairing: Fraunces (display, variable) / Inter (body) / Source Serif 4 (long-form reading).

---

## Next-session backlog

Prioritized for Session 7.

1. **Build the first real interactive component — the Vignette #1 hero map.** PBDB REST API, CC-BY, GeoJSON, Natural Earth basemap. Start with a static SVG render at build time (no runtime JS), add interactivity only after the static version looks right. This is the single most-visible "the site has real scholarship behind it" beat and it's still a placeholder card.
2. **Deploy to Vercel staging.** Point a preview subdomain while iteration continues. Real domain points after V1. This unblocks real link-checking, cross-device testing, keyboard-tab a11y verification, and social OG rendering.
3. **Real favicon, book cover artwork, and OG image.** A single typographic mark for the favicon; a book cover (any medium — illustrated or photographic) for the homepage and OG share card.
4. **Self-host the fonts.** Replace the Google Fonts `@import` with local `@font-face` rules from `public/fonts/`. Fraunces and Source Serif 4 are both variable; Inter can be a variable or a subset of weights. Eliminates the file:// font-loading quirk and the Google Fonts privacy line in the privacy policy.
5. **Email capture backend.** ESP decision. Current mailto forms work but don't scale past ~50 replies. Buttondown remains the recommendation for long-form author lists; swap the ContactForm action from mailto to the provider's form endpoint when decided.
6. **Replace the About-page headshot placeholder.** One real photo (square crop, neutral background, soft light). The dashed-border placeholder flags its own absence.
7. **Vignette #2** — *The Horse, Returning Native*. First pressure-test of the template on a politically-charged survivor species. Forces the template to prove it can handle "not extinct, re-introduced, contested" as cleanly as it handled "extinct, re-proposed."
8. **Per-page OG images.** Each long-form page deserves its own social card; currently one shared fallback.
9. **Automated link-check in build.** Now that the sitemap is big enough that hand-maintenance drifts, run a link-check over `dist/` as part of `npm run build` — fails the build on any internal 404 or external dead link.

The experiment page (`/one-hundred-camels/the-experiment`) remains the single page a patron reads. The new objections section (Section 11) and family-of-work section (Section 04) are designed so that a skeptical reader can land on the page cold, get their predictable objections addressed, see the proposal is not a unicorn, and still reach the ask. Anything we do next that pulls visitors further into the site should route them through it at least once.

---

## Notes on the build

- Astro was chosen over Next.js because the site is primarily static content with a small number of interactive islands. Astro produces leaner HTML, has a simpler mental model for content-driven sites, and natively supports React/Vue/Svelte components for the interactive pieces when they arrive.
- Tailwind is used directly via utility classes. Design tokens live in `tailwind.config.mjs`; updates there propagate everywhere.
- No JavaScript runtime is required for the current build. The site is fully functional with JS disabled.
- All pages pass the "open-graph-ready" test structurally; artwork and copy still to come.

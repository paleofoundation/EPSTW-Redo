# sustainabilitydiet.com — Website Plan v0.1

**Draft date:** 2026-04-18
**Drafted by:** Claude (Opus 4.7), in collaboration with Karen Pendergrass
**Status:** Draft for review
**Source material:** `10_outline_master.md`, `00_PROJECT_README.md`, `11_voice_and_style_notes.md`, `WEBSITE_IDEAS.md`, and the manuscript as it stands (Prologue + 13 chapters + Epilogue drafted).

---

## 1. Framing the problem of the domain

The domain `sustainabilitydiet.com` is the public home of the book. It is also, separately, a very good name for a piece of intellectual property — the phrase is short, declarative, and carries the book's core move (sustainability is a diet; a diet is a set of choices about what a system consumes and what sustains it) before anyone has read a word. Keeping it. Good.

The implication is that "Ghost Ecosystem Atlas" is not the site. It is one of several interactive tools the site hosts. The site is *The Sustainability Diet*, and the interactive features are the book's ideas made inhabitable. The framing inversion that makes this feel native rather than forced: the sustainability diet isn't only what humans eat — it's what the *land* eats. What the land used to eat. What it eats now. What it could eat again. That sentence is the bridge between the book's title and the interactive work, and it should appear on the homepage.

## 2. Naming, drawn from the book's own vocabulary

Three tools, three names. Each is taken directly from the manuscript; none is borrowed or invented.

**Near Time.** The interactive paleo-ecological atlas. Named for Chapter 3 (*Near Time*) and MacPhee's 1999 volume. This is the feature I was calling "Ghost Ecosystem Atlas" — place-based, time-scrubbable, showing what stood where the reader stands, when it was lost, and what remains. The name is scientifically grounded, carries the book's seriousness, and does the thing good product naming does: it rewards the reader who has read the book (they recognize the title) and intrigues the reader who hasn't (*near time, what does that mean?*).

**The Fourth Axis.** The survivability scoring tool. A reader enters a food system (their farm, their region's dominant agriculture, a product they're considering) and the tool walks them through scoring it on all four axes — economic, social, environmental, survivability — producing a defensible, sourced score rather than a vibe. This operationalizes Chapter 4 and is the feature most likely to drive professional use (farmers, extension agents, journalists, policy staff).

**One Hundred Camels.** The rewilding-now index. Current projects, measurable outcomes, ways to support. Named for the Prologue / Epilogue closure — the author's longing made actionable. This is where the site converts readers who finished the book into people who do something.

Secondary writing lives under **Field Notes** — the existing `WEBSITE_IDEAS.md` content (the seed-dispersal essay, the future fragments) publishes here as short-form essays.

## 3. Information Architecture

```
sustainabilitydiet.com
├── /                              homepage
│   └── one-line mission, Near Time teaser tile,
│       book cover, "Start here" entry points for
│       three reader types (reader, producer, policy)
│
├── /the-book                      book landing
│   ├── /the-book/excerpt          Prologue in full, plus the
│   │                              meat-counter opening (Ch. 1)
│   ├── /the-book/reading-guide    chapter-by-chapter companion
│   ├── /the-book/bibliography     every citation in the book,
│   │                              with DOI links, groupable by chapter
│   └── /the-book/errata           corrections, with dates
│
├── /near-time                     THE ATLAS (flagship)
│   ├── /near-time/map             place-based entry (zip, address,
│   │                              or click-to-explore)
│   ├── /near-time/species/:slug   per-species pages
│   │                              (Camelops hesternus, Mammut americanum,
│   │                               Maclura pomifera, etc.)
│   ├── /near-time/stories/:slug   the curated vignettes (see §5)
│   └── /near-time/about           methods, data sources, known biases
│
├── /fourth-axis                   SCORING TOOL
│   ├── /fourth-axis/score         the interactive scoring walkthrough
│   ├── /fourth-axis/library       pre-scored systems (Polyface, APR,
│   │                              Knepp, an industrial feedlot, an
│   │                              Alaskan salmon fishery, etc.)
│   └── /fourth-axis/methodology   the framework, fully sourced
│
├── /one-hundred-camels            REWILDING-NOW INDEX
│   ├── /one-hundred-camels/projects
│   ├── /one-hundred-camels/map    (projects layered on Near Time base)
│   └── /one-hundred-camels/support
│
├── /field-notes                   essays, fragments, future
│                                  book material
│
└── /about                         Karen, Paleo Foundation, contact,
                                   press
```

**Cross-linking rule.** Every book-bibliography entry links to any Near Time species page, Field Notes essay, or Fourth Axis library entry that cites it. Every vignette in Near Time links to the book chapter that anchors it. Every Fourth Axis library entry shows which chapter established the scoring logic. The site is a graph, not a tree, with the book as the spine.

**URL design.** Species slugs use common name with scientific name as fallback: `/near-time/species/western-camel` (aliased from `/near-time/species/camelops-hesternus`). This matters for SEO; people searching "western camel extinct" are more numerous than people searching by binomial.

## 4. Data Sourcing Plan

### 4.1 Fossil occurrences (paleofauna)

**Paleobiology Database (PBDB).** pbdb.org. Primary source for Pleistocene occurrence data. CC-BY licensing. REST API returns GeoJSON. Every occurrence carries a reference, so attribution is automatic and defensible. This is the backbone of Near Time.

**Neotoma Paleoecology Database.** neotomadb.org. Primary source for Quaternary pollen, plant macrofossils, and vertebrate material from lake-sediment and cave contexts. CC-BY-4.0. Critical for the flora side of the atlas — this is where we find evidence that *Gleditsia* grew in a place, not just inference from modern range.

**FAUNMAP II** (integrated into Neotoma). North American late Quaternary mammal distributions. Already cleaned.

**San Diego Natural History Museum, La Brea Tar Pits, Mammoth Site of Hot Springs, Page Museum, Florida Museum of Natural History.** Institution-level datasets, some publicly accessible, some requiring a request. Begin with PBDB/Neotoma; fill gaps by institution.

### 4.2 Flora and plant distributions

**GBIF.** gbif.org. Global Biodiversity Information Facility. Comprehensive occurrence records for extant species. CC-BY or CC0 per dataset; filter at query time. Primary source for current distributions of the candidate "orphan" plants (osage orange, honey locust, pawpaw, Kentucky coffeetree, avocado, persimmon, etc.).

**USDA PLANTS Database.** plants.usda.gov. Public domain. Authoritative for U.S. native/introduced status and county-level distribution.

**iNaturalist.** inaturalist.org. CC licensing varies by observation. Research-grade observations only. Valuable for showing *where readers are seeing these plants today* — the citizen-science layer that makes the atlas feel alive rather than historical.

**BIEN (Botanical Information and Ecology Network).** bien.nceas.ucsb.edu. Plant species distributions with climate and trait data; well-curated for New World species.

### 4.3 Human arrival / archaeological chronology

**Canadian Archaeological Radiocarbon Database (CARD 2.1)** and **p3k14c** (global radiocarbon synthesis). Peer-reviewed, open-data, published in *Scientific Data*. This is what lets Near Time show, honestly, when humans arrived at a given latitude. Necessary for the book's Chapter 3 material to have a visual companion.

**ArchaeoGLOBE.** Land-use through time, expert-sourced. For long-duration bioregional context.

### 4.4 Paleoclimate and paleogeography

**PaleoView** and **WorldClim-past** (CHELSA-TraCE21k). Paleoclimate reconstructions from 21,000 BP to present at sub-millennial resolution. Needed for the time-slider to make sense: when you pull the slider to 18,000 BP, ice-sheet extent and coastlines have to change, or the map is lying.

**Natural Earth.** Public-domain basemaps and political boundaries. Use for all current-geography layers.

### 4.5 Rewilding projects (current / One Hundred Camels)

No single database. Curation required.

Anchor projects (each with public documentation, most with press kits):
- American Prairie Reserve (Montana)
- Knepp Estate (West Sussex, UK)
- Oostvaardersplassen (Netherlands) — include the honest history, including the welfare controversy
- Pleistocene Park (Chersky, Siberia)
- Rewilding Europe (multi-site)
- Iberá Wetlands (Argentina) — jaguar reintroduction
- Tauros Programme / European bison reintroductions
- Yellowstone wolf reintroduction (U.S., reference case, 1995–)
- The American bison restoration network (InterTribal Buffalo Council, tribal lands)
- Feral hog management programs (Texas, for the Chapter 8 example)

For each: name, location, species involved, status, a single defensible outcome metric (where available), a photo, a link to their site, and — honestly — the controversies.

### 4.6 Bioregional layers

**EPA Level III Ecoregions** (U.S.), **Olson et al. WWF Terrestrial Ecoregions** (global). Public or research-use. These matter for Chapter 11 (Bioregional and Urban) and for letting readers see their own place mapped to an ecoregion rather than a political jurisdiction.

### 4.7 Licensing, attribution, and the honest caveat

All data sources listed are usable for a project of this kind with attribution. None should be republished verbatim as redistributable bulk data — they are *consulted at query time* via APIs or pre-processed into a site database that carries source IDs.

**Every record on the site carries its source ID and a citation.** This is not optional. It is the thing that makes the site survivable to academic scrutiny — which it will receive, because if it's good, paleoecologists and conservation biologists will find it and talk about it. The moment a Camelops dot lacks a PBDB ID that a researcher can verify, the site becomes vulnerable in the exact way that academic consumers of this kind of work are most sensitive to. Build with transparency as the default.

**Sampling bias, stated plainly on /near-time/about.** A one-paragraph note: fossil localities reflect where paleontologists have dug, not where animals lived. Absence of dots does not mean absence of species. The map is a map of our evidence, not of the Pleistocene. This is the sentence that protects the project from the kind of takedown that would be fair.

## 5. Prioritised Vignette List

Ten regional stories, each anchored to one or more book chapters, each designed to be the first thing a visitor to Near Time experiences. Order reflects priority for v1 build — the first five should ship together; the second five can follow in a v2 drop.

### V1: Launch vignettes (ship with the site)

**1. Camelops in the American West — "One Hundred Camels" (Prologue, Epilogue).**
The book's own opening image, given its own page. *Camelops hesternus*, extinct ~13,000 BP, ranged across the American West. Co-occurring flora: mesquite, acacia, giant chollas, and — at the eastern edge of its range — osage orange. Current analogous landscape: the Sonoran, the Mojave, the shortgrass prairie. Embedded tool: a zip-code entry that returns "here's what stood where you're standing." Outbound link: the Prologue excerpt.

**2. The Horse, Returning Native (Ch. 2 — Columbian Curtain).**
The book's central conceptual move. *Equus* evolution timeline (55 Mya origin on this continent through ~10,000 BP extirpation through 1493 return). Distribution across time as an animation. The question the page asks: *when does "native" start counting?* Ties directly to the Columbian Curtain chapter excerpt.

**3. Mastodons and the Forgotten Fruits (Ch. 2, Ch. 3).**
The Eastern woodlands story, which is the emotional heart of Janzen & Martin 1982. *Mammut americanum* range. Paired with osage orange (*Maclura pomifera*), honey locust (*Gleditsia triacanthos*), Kentucky coffeetree (*Gymnocladus dioicus*), pawpaw (*Asimina triloba*), and common persimmon (*Diospyros virginiana*). Each of these is an extant plant producing fruits or pods that the modern eastern megafauna (white-tailed deer, raccoons) cannot effectively disperse. *The fruit is a message to a mouth that no longer exists* — the line from Karen's own seed-dispersal fragment lives on this page.

**4. The Southwest's Missing Grazers (Ch. 7 — Wrong Proxy, Right Place).**
The Savory food-truck chapter, made visual. Pleistocene fossil occurrences for the Southwest: equids (*Equus conversidens*, *Equus scotti*), camelids (*Camelops*, *Hemiauchenia*), not bovids. Current management: cattle. The page argues Chapter 7's argument through the data. Links to the chapter excerpt.

**5. Near Time — What Was Lost, When (Ch. 3).**
Not a place-story but a time-story. A global (or continental-selector) extinction timeline from 50,000 BP to present. Overlay: human arrival by continent. Overlay: Younger Dryas onset (12,800 BP). Overlay: climate proxy (sea level, temperature). The page lets the reader see, rather than read, the Chapter 3 argument that the question of *cause* is multifactorial. The rewilding case does not depend on which cause prevails — the page states this, once, below the timeline.

### V2: Second wave (deepen and internationalise)

**6. Florida's Lost Subtropical Ecosystem.**
*Eremotherium laurillardi* (giant ground sloth), *Holmesina* (pampathere), *Panthera onca augusta* (Pleistocene jaguar), *Tapirus veroensis*. Extraordinary fossil density. Co-occurring megafaunal fruits that persist: pond apple, possibly pawpaw at northern edge. Why this matters: Florida is where the North American megafaunal-fruit hypothesis is strongest, because the fossil density lets you pair specific animals to specific plants at specific sites.

**7. The Great Plains, Where Giants Grazed (Ch. 8 — Rewilding the Plate).**
Mammoth-mastodon-sloth-bison assemblage. The current rewilding project (American Prairie Reserve) gets its own One Hundred Camels entry and is cross-linked here. This is the page that asks: *what does a restored shortgrass prairie eat?*

**8. Australia, 45,000 Years Ago.**
*Diprotodon*, *Thylacoleo carnifex*, *Genyornis newtoni*, *Procoptodon* (giant short-faced kangaroos). The Australian collapse is the closest thing to a controlled experiment for the overkill hypothesis — climate was not changing catastrophically at 45 kya, humans had just arrived, most genera went. The page presents the case fairly and marks where the scholarly uncertainty still lives. Important because it de-provincialises the book's argument.

**9. Madagascar and the Elephant Birds.**
*Aepyornis maximus*, giant lemurs (*Archaeoindris*, *Palaeopropithecus*), pygmy hippos, the Malagasy crocodile. Holocene extinction (~1,000–500 BP), which makes the human causation argument especially tight. Tentative flora orphans: certain Malagasy baobabs, the triangle palm, possibly *Uncarina* seed morphology. Include honestly that the baobab-elephant-bird hypothesis is *contested*; the page does not overclaim.

**10. The Pacific Northwest and the Otter Line (Ch. 10 — Indigenous and Marine).**
The marine companion piece. Not a Pleistocene story — the sea-otter collapse was 18th-century — but the same structural logic: a keystone vertebrate is removed and the ecosystem (kelp forest) loses its functional structure. Belongs in the atlas because Chapter 10's argument is that water-column rewilding is part of the same project. Links to the chapter, to the Elakha Alliance, to the otter-recovery reference literature.

### Held for V3 (good stories, but not first)

- New Zealand's moa and the divaricating plants (Holocene, ~700 BP — the freshest extinction, strongest ghost-form evidence in living plants).
- The Caribbean's recent sloths (persisted until ~4,500 BP on the islands, long after mainland extinction — the forgotten extinction).
- The Neotropics: avocado, gomphotheres, and Janzen-Martin's original paper given proper treatment.
- The Mammoth Steppe: Pleistocene Park's actual premise, for readers who want to understand what Zimov is trying to do.
- The Eurasian temperate zone: aurochs, forest bison, European lion, where Rewilding Europe is currently working.

## 6. Minimum Viable V1

Ship, in order:

1. Homepage, About, Book page, Prologue excerpt, bibliography (static).
2. Near Time: vignettes 1–5 above, fully written and sourced. Species pages for the ten species those vignettes anchor to. Crude zip-code lookup that returns "species documented within N km of you." No time slider yet.
3. Fourth Axis: scoring walkthrough with three pre-scored systems (industrial feedlot, Polyface, Knepp). No user-submission feature yet.
4. One Hundred Camels: static project cards for the ten anchor rewilding projects. No map overlay yet.
5. Field Notes: the existing seed-dispersal fragment published as the first essay.
6. Email capture on homepage.

What is explicitly **not** in v1: the time slider, user-submitted Fourth Axis scores, the trophic-web visualization, user accounts, comments. Those are v2 or later. Shipping the vignettes and one good scoring tool is enough to establish the site's seriousness; the rest is earned.

## 7. Open questions for Karen

These are decisions the plan cannot make on its own.

- **Launch timing relative to book publication.** Does the site precede the book (as a discovery surface and mailing-list builder), coincide with it, or follow it? Each has different implications for what ships in v1.
- **Site development resource.** Is there an existing Paleo Foundation web stack this should live on, a preferred builder (Webflow, Framer, custom Next.js), or is this a clean build? This changes estimates and vendor choices.
- **Bibliographic exposure.** Does the bibliography page link out to DOIs only, or also host PDFs where permitted? The second is far more useful to researchers and far more legally involved.
- **Data freshness cadence.** PBDB and Neotoma update continuously. Does the site re-pull monthly, quarterly, or at each v-release? This is a maintenance-cost decision disguised as a technical one.
- **Commercial posture.** Is the site strictly non-commercial (book promotion, foundation mission), or does it host affiliate links, commerce for rewilding project partners, or sponsorships? This affects which data licenses are usable and which partnerships are available.
- **Scholarly partnership.** Would you want to invite a paleoecologist (Tony Barnosky, the Svenning group, someone at the Neotoma consortium) onto an informal advisory role before launch? The cost is low; the credibility return is substantial. A single named scientific advisor, credited on /near-time/about, answers the "is this real" question before anyone asks it.

---

**Next step suggestion.** Before any build work, the single highest-leverage next document is the full content for Vignette #1 (Camelops / One Hundred Camels) — written to shipping quality, with every citation in place. It sets the template for the other nine and surfaces, in practice, every technical and editorial decision the site will have to make. If you want, I can draft that next.

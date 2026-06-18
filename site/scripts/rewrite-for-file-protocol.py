#!/usr/bin/env python3
"""
Post-process dist/ HTML so that file:// viewing works.

Rewrites root-absolute paths (e.g. /_astro/foo.css, /about) into paths
relative to each HTML file's location. Safe to run against a production
build because it only touches the dist/ copy.

Run after `npm run build`.
"""

import re
import sys
from pathlib import Path

DIST = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent / "dist"

if not DIST.exists():
    print(f"No dist/ at {DIST}. Run `npm run build` first.")
    sys.exit(1)

# Known internal routes (root-relative). Each maps to its on-disk target.
# Order matters: longer/nested routes must appear before their parent so the
# replace pass matches the most specific one first.
INTERNAL_ROUTES = [
    "/near-time/stories/one-hundred-camels",
    "/one-hundred-camels/the-experiment",
    "/one-hundred-camels/critics",
    "/one-hundred-camels/contribute",
    "/field-notes/seed-dispersal",
    "/near-time/orphaned-fruits",
    "/near-time/further-reading",
    "/near-time/bibliography",
    "/near-time/timeline",
    "/near-time/glossary",
    "/near-time/sources",
    "/near-time/proxies",
    "/the-book/excerpt",
    "/the-book",
    "/near-time",
    "/fourth-axis",
    "/one-hundred-camels",
    "/field-notes",
    "/data-attribution",
    "/changelog",
    "/privacy",
    "/start",
    "/terms",
    "/about",
    "/map",
    "/faq",
]

# Assets that sit at dist root
ASSETS = [
    "/_astro/",
    "/favicon.svg",
    "/feed.xml",
    "/robots.txt",
    "/sitemap.xml",
]


def rewrite(html: str, html_path: Path) -> str:
    # Depth below dist/
    rel = html_path.relative_to(DIST).parent
    depth = len(rel.parts)
    up = "../" * depth if depth > 0 else "./"

    # Rewrite asset references
    for asset in ASSETS:
        html = html.replace(f'href="{asset}', f'href="{up}{asset.lstrip("/")}')
        html = html.replace(f'src="{asset}', f'src="{up}{asset.lstrip("/")}')

    # Rewrite internal route links to point at index.html files so file:// can open them.
    # Handles exact href="/route", href="/route#anchor", and href="/route?query"
    for route in INTERNAL_ROUTES:
        base = f'{up}{route.lstrip("/")}/index.html'
        # exact
        html = html.replace(f'href="{route}"', f'href="{base}"')
        # with hash
        html = re.sub(
            r'href="' + re.escape(route) + r'(#[^"]*)"',
            lambda m: f'href="{base}{m.group(1)}"',
            html,
        )
        # with query
        html = re.sub(
            r'href="' + re.escape(route) + r'(\?[^"]*)"',
            lambda m: f'href="{base}{m.group(1)}"',
            html,
        )

    # Also rewrite href="/" (the homepage link in the logo)
    home_target = f'{up}index.html'
    html = re.sub(r'href="/"', f'href="{home_target}"', html)

    # Rewrite href="/#..." (homepage anchors, e.g. the Subscribe CTA in the nav)
    html = re.sub(
        r'href="/(#[^"]*)"',
        lambda m: f'href="{home_target}{m.group(1)}"',
        html,
    )

    return html


count = 0
for html_path in DIST.rglob("*.html"):
    src = html_path.read_text(encoding="utf-8")
    out = rewrite(src, html_path)
    if out != src:
        html_path.write_text(out, encoding="utf-8")
        count += 1
        print(f"rewrote {html_path.relative_to(DIST)}")

print(f"\n[OK] rewrote {count} file(s) for file:// protocol compatibility")
print(f"  double-click {DIST / 'index.html'} to view")

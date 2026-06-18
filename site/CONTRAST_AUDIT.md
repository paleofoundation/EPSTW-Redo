# Color contrast audit

Audit run April 2026. All contrast ratios computed against the `paper` background (`#F6F2EA`, relative luminance 0.894).

| Color       | Hex       | Luminance | Contrast vs paper | WCAG AA (normal, 4.5:1) | WCAG AA (large, 3:1) |
|-------------|-----------|-----------|-------------------|--------------------------|-----------------------|
| `ink`       | `#1F1D1B` | 0.013     | **14.9:1**        | Pass                     | Pass                  |
| `ochre`     | `#9C6B3F` | 0.183     | **4.05:1**        | **Fail**                 | Pass                  |
| `ochre-deep` (new) | `#7A4F2D` | 0.106 | **6.10:1**        | Pass                     | Pass                  |
| `moss`      | `#5C6B4F` | 0.128     | **5.33:1**        | Pass                     | Pass                  |
| `dust`      | `#8B7F6E` | 0.218     | **3.52:1**        | **Fail**                 | Pass                  |

## What changed

1. Added `ochre-deep` (`#7A4F2D`) as a new design token for body-text links. Contrast ratio 6.1:1; passes AA for normal text with margin.

2. Added a CSS rule in `global.css` that automatically overrides `a.text-ochre` inside `.prose-reading` to use the deeper shade. Existing body-text links do not need to be rewritten; they become AA-compliant the moment they render inside a `prose-reading` wrapper.

3. The original `ochre` (`#9C6B3F`) is retained for decorative UI: kickers in small-caps (where the label pattern is a UI element rather than content), display-size headings (which pass large-text AA at 3:1), button backgrounds (contrast measured against `paper` is not the relevant metric there), and borders.

4. `dust` (`#8B7F6E`) is documented as reserved-for-non-text or large-text only. A grep found no current use of `text-dust`, `bg-dust`, or `border-dust`; nothing to change today.

## What still needs attention

1. **Small-caps kickers in `text-ochre text-xs`** — technically fail AA because they are not large text. The kicker pattern is used as an eyebrow/label, not as content, and is always adjacent to the heading it labels; the heading communicates the same meaning. WCAG guidance is strict about this even for labels. A future iteration may want to switch kickers to `text-ochre-deep` or use a darker accent specifically for xs-sized labels.

2. **Fourth-axis/fourth-axis placeholder** — not yet reviewed because it is still a placeholder page. Audit on promotion.

3. **Link hover states** are now `#5F3E23` in-prose, which gives an even darker read on hover. Nothing else does a color-shift on hover besides the button on-hover-to-ochre, which is a full background flip and separately readable.

## Skip-to-content

A skip-to-content link has been added at the top of `Base.astro`. It is visually hidden via Tailwind's `sr-only` utility and becomes visible on focus. Tested with keyboard nav by routing the Tab key and observing the link appear.

## Next

- Keyboard-tab every page once the Vercel staging deploy is up. Focus rings are currently the browser default; may want to standardize.
- Test with a screen reader on the experiment page (the most form-heavy surface).
- Re-audit after any new color tokens are added.

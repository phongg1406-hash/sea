# Sunlit Shore — interactive portfolio prototype

A **code-first, zero-dependency** prototype of the agreed Sunlit Shore concept. It is an **implemented visual/interaction prototype**, not a production-ready personal portfolio. No AI image generation, image understanding, build service, Docker, or external network request is required.

## Open it

Option 1: double-click `index.html`. All core resources are local.

Option 2 (recommended for iterative work): open this folder in VS Code, then run:

```powershell
py -m http.server 8000
```

Visit `http://localhost:8000`. VS Code Live Server also works. For automated browser tests, run `python tests/visual_check.py` from a Python environment with Playwright and Chromium installed; this script uses in-memory document injection because the creation environment blocks Chromium navigation to local addresses.

## What's implemented

- **Desktop spatial world**: 2500×2300 logical-pixel coast; drag empty space to pan; scroll wheel traverses narrative waypoints, shift/trackpad horizontal gesture pans; Ctrl+wheel and +/- controls adjust zoom; section links and mini-map allow direct travel.
- **Mobile**: linear, naturally scrollable sections, functional hamburger menu, sea-themed Hero, touch-enabled small wake response without intercepting scrolling.
- **Stylized water wake**: directionally offset trails that react to pointer velocity, spread slightly and fade. No circular stone-impact ripples, particle engine or full fluid solver. Renders only while needed. This is a first-pass perceptual approximation; it does **not** implement true water refraction or a velocity field.
- **Postcard featured projects** and **minimal archive cards** (grid/list switcher), functional accessible detail dialog.
- **Modular playground**: three draggable objects within a bounded local panel, keyboard arrow-key movement, reset button.
- **Low-motion switch**, respects `prefers-reduced-motion`, hidden-tab animation pause.
- SVG shoreline, summer palette, decorative code-first assets. No remote font, background photo or library.

## Controls

| Mode | Control | Result |
|---|---|---|
| Desktop | Move pointer over ocean | Directional water trail |
| Desktop | Drag empty background | Pan the entire spatial world |
| Desktop | Scroll wheel | Follow narrative anchors |
| Desktop | Shift + wheel / trackpad horizontal | Pan horizontally |
| Desktop | Ctrl + wheel / +/- | Zoom |
| Desktop | Navigation or mini-map | Jump to section |
| Desktop | Arrow keys when not inside a control | Pan |
| Any | Click project postcard/card | Show project details |
| Playground | Drag an object / focus and arrow keys | Move toy inside its zone |
| Mobile | Swipe scroll | Browse sections normally |
| Mobile | Tap empty area in ocean Hero | Brief directed wake |
| Any | Motion on/off | Stop / resume decorative animation |

## Important unfinished production work

1. Replace placeholder name, biography, contact email and GitHub link.
2. Replace `Next up`, `Tiny experiments` and other sample project data in `app.js` with verified real projects. `Light` is marked in development and needs review before publication.
3. Replace the CSS-only placeholder project art with actual screenshots (your AI coding tool needs only file paths, alt text, aspect ratios and crop positions; no image-reading model is necessary).
4. Review the desktop world route and wheel-vs-pan feel with real users; some visitors will prefer conventional scrolling. Keep direct navigation.
5. Run field/lab performance measurements on your own device and at least one lower-end mobile device. **No real Lighthouse or field Core Web Vitals scores are claimed.**
6. Do visual accessibility audit, performance profiling, and deployment-specific SEO/metadata before production.

## Files

- `index.html` — semantic content and initial module placeholders.
- `styles.css` — responsive art direction, spatial modules and card layouts.
- `app.js` — camera, water wake, project dialog, archive views and draggable toys.
- `assets/favicon.svg` — local custom mark.
- `docs/DESIGN_SPEC.md` — decisions and precise design tokens.
- `docs/SPATIAL_MAP.svg` — explorable world map.
- `docs/WIREFRAMES.svg` — desktop/mobile visual blueprint.
- `docs/IMPLEMENTATION_PLAN.md` — project roadmap, acceptance checklist and validation rules.
- `docs/AI_HANDOFF.md` — prompt for text-only AI coding assistant.
- `docs/TONG_QUAN_VI.md` — Vietnamese handoff summary.
- `tests/visual_check.py` — in-memory Playwright integration/screenshot checks.
- `tests/*.png` — sample desktop/mobile captures generated during checking.

## Technical posture

Standard browser APIs and no framework dependencies. This choice makes the prototype portable and easy to inspect with text-only AI coding. A future Next.js/React implementation is possible, but should preserve the DOM/CSS spatial-world model instead of replacing all content with an inaccessible WebGL scene.

© Concept prototype 2026. Text and sample art are placeholders until replaced with your own identity and project assets.

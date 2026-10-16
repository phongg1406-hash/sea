# AI coding handoff — use with a text-only coding agent

You are maintaining **Sunlit Shore**, a custom personal portfolio prototype. Read `README.md`, `docs/DESIGN_SPEC.md`, `docs/IMPLEMENTATION_PLAN.md`, `docs/SPATIAL_MAP.svg`, then inspect `index.html`, `styles.css`, `app.js` before editing.

## Non-negotiable design decisions

- Global navigable 2D desktop canvas (DOM-based world; not a bitmap text canvas).
- Mobile is intentionally standard vertical reading flow; don't hijack touch scroll.
- Visual direction: playful brutalism + stylized bright turquoise sea, warm sand, sunlight.
- Water signature: **directional finger-stir wake** following velocity, fading naturally; **never replace it with concentric impact rings**.
- Featured projects as postcards; archive as minimal cards.
- Code-first artwork (CSS/SVG/canvas), no required Vision, no generated fake screenshots or invented project claims.
- Performance and accessibility are first-class product requirements.

## Constraints

- The user's local environment is Windows 11 Home; do not require Docker.
- No requirement to use external image generation, paid libraries or remote fonts.
- Do not rewrite into a framework unless there is a concrete user-approved value. First fix current code.
- Keep content data distinct from visual presentation; placeholders must be clearly labeled.
- Do not claim good performance because the bundle is small; measure the runtime.

## Coding workflow

1. State which file(s) will change and why.
2. Make one focused change at a time.
3. `node --check app.js` after changing JS.
4. Test interactions in a real browser, including 390px mobile, 1440px desktop and reduced motion.
5. Report visual testing limitations accurately if browser/vision unavailable.
6. Record regressions and testing results in `docs/IMPLEMENTATION_PLAN.md`.

## Priority backlog

P0 — Replace sample personal details, real project metadata and actual screenshots after user supplies them.

P1 — Gather subjective feedback on Wake directionality; improve flow only if visual review supports it, ideally using a few more very faint curved filaments or small texture displacement, with benchmark.

P1 — Keyboard and focus audit of scene navigation; ensure focus and camera location agree when anchors are used.

P1 — Usability test whether wheel-by-waypoint should remain default or become optional.

P2 — Content case-study subpages and production-grade discoverability, if wanted.

P2 — Automated accessibility checks and performance measurement across desktop/mobile.

Never start by adding 3D physics or an elaborate fluid simulation. A lightweight and intelligible experience is the goal.

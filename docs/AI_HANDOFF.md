# AI coding handoff — use with a text-only coding agent

You are maintaining **Sunlit Shore**, a custom personal portfolio prototype. Read `README.md`, `docs/DESIGN_SPEC.md`, `docs/IMPLEMENTATION_PLAN.md`, `docs/ARCHITECTURE/OVERVIEW.md`, then inspect `index.html`, `styles.css`, `app.js` before editing.

## Non-negotiable design decisions (Sunlit Shore v2.0)

- **Continuous Vertical Coastal Scroll**: The primary navigation is natural vertical scrolling, replacing the previous website-wide freely pannable 2D spatial canvas.
- **Mobile is intentionally standard vertical reading flow**: Don't hijack touch scroll.
- **Visual direction**: Playful Brutalism + Coastal Editorial Design + Stylized Tropical Environment with Warm Cream Sand and Dynamic Ocean.
- **Water signature**: **Directional finger-stir wake** following velocity, fading naturally; **never replace it with concentric impact rings**.
- **Featured projects as postcards**; archive as minimal cards.
- **Shared Project Detail Modal** used for both PROJECTS and PROJECT ARCHIVE sections.
- **Code-first artwork** (CSS/SVG/canvas), no required Vision, no generated fake screenshots or invented project claims.
- **Performance and accessibility** are first-class product requirements.
- **Eight main destinations** along a continuous coastal journey representing Vietnam's coastline.
- **Geographic Shore Map** as separate navigation component (collapsed by default).
- **Vũng Tàu Secret Easter Egg** as out-of-flow destination accessible only through discovery flow.
- **Skill Net** as signature visual feature in the SKILLS section (Đà Nẵng).
- **Scroll fade-in/fade-out** between sections.

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

## Key architectural changes from v1.0

**REPLACED**: Website-wide freely pannable 2D spatial canvas  
**WITH**: Continuous Vertical Coastal Scroll with fixed left-land/right-ocean composition  

**REPLACED**: Six regions in zig-zag spatial arrangement  
**WITH**: Eight destinations in continuous vertical scroll journey  

**REPLACED**: Poetic section headings (Make waves, etc.)  
**WITH**: Conventional portfolio labels (HOME, PROJECTS, ABOUT ME, etc.)

**ADDED**: Geographic Shore Map as separate navigation component  
**ADDED**: Vũng Tàu Secret Easter Egg as out-of-flow discovery  
**ADDED**: Skill Net as signature visual feature in SKILLS section  
**ADDED**: Scroll fade-in/fade-out behavior between sections

See `docs/DESIGN_SPEC.md` for complete specification and `docs/ARCHITECTURE/OVERVIEW.md` for architectural details.
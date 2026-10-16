# SUNLIT SHORE — Design Specification v1.1

Status: **Concept fixed; working prototype built; production data and performance approval outstanding.**

## 1. North Star

A playful, warm, summer-beach personal portfolio with a **desktop-wide navigable spatial canvas**, project-first storytelling and a light **Directional Water Wake**. Not an ocean simulator and not a dashboard. Code-created visual language is mandatory; photorealistic textures are optional and currently not used. Text-only AI coding must be sufficient to maintain the project.

Three product priorities, in order:
1. Visitors can find projects, identify the creator, and navigate with ordinary controls.
2. Visual personality and tangible interaction create an experience worth exploring.
3. Effects must remain adaptive and inexpensive; all essential content survives without animation.

## 2. Layout and world geometry

Desktop world: **2500×2300 logical px** (not infinite). The viewport reveals a portion of this world; the world is a transformable HTML/CSS/SVG DOM stage, **not** a bitmap canvas containing all text. Camera moves it with `translate3d` and `scale`. Camera translation is clamped so visitors cannot drift unbounded into empty space.

| Region | World x,y origin | Approximate box | Primary activity |
|---|---:|---:|---|
| Ocean Hero | 155,235 | 1030×555 | Intro, water wake |
| Selected Work | 1425,177 | 900×650 | Featured postcard projects |
| Playground | 220,1005 | 980×690 | Local drag and bento modules |
| Project Archive | 1470,1040 | 820×650 | Grid/list browsing |
| About | 180,1800 | 1050×420 | Editorial profile & skills |
| Contact | 1480,1765 | 860×435 | Links and close |

World route follows a zig-zag: **Hero → Selected Work → Playground → Archive → About → Contact**. The route is represented by in-page anchor links, a mini-map and wheel-based waypoint progression. Viewport can pan anywhere inside a bounded world, subject to clamping.

**Pan vs scroll:** on desktop, drag blank canvas to pan. Standard wheel navigates waypoints; a trackpad horizontal input or Shift+wheel pans sideways. Section navigation gives reliable access. Mobile does not inherit desktop drag-to-pan: it uses an ordinary vertical content order. This deliberate responsive mode avoids scroll capture and touch conflicts.

## 3. Visual language

**Art direction**: Playful Brutalism × Stylized Tropical Shore, tempered by editorial spacing. Top-down scene; not a photographic horizon, game world, neumorphism or glassmorphism.

| Token | Value | Purpose |
|---|---|---|
| Ocean | `#00BCCD` | Water primary |
| Shallow | `#75E3DF` | Near-shore water |
| Sand | `#FFF0CB` | Warm content background |
| Foam | `#FFFDF4` | Highlights and card paper |
| Sun | `#FFB950` | Warm accent |
| Deep ocean ink | `#07515D` | Text on cyan |
| Sand ink | `#39352F` | Text on cream |
| Coral accent | `#FF7858` | Selected typography, icons |

Typography in this prototype: local **Arial/Helvetica** for headlines and content, **Georgia** for humanist italic accent, **Courier New** for navigation labels and metadata. This avoids remote requests; if design review later approves Space Grotesk / Inter / Space Mono, use self-hosted, legally sourced font subsets, loaded conditionally as appropriate.

Headline 85–146 desktop px, 54–96 mobile; section headlines ≈40–67 px. Text ≈16–23 px. The design should never require a graphic image model to interpret a screenshot in order to implement spacing: dimensions and tokens are represented in CSS.

Shape treatments: smooth organic shoreline; rounded rectangular UI ≈6–13 px; project postcards with near-sharp corners; 1.5–2 px outlined forms; hard but modest shadows; restrained organic stickers, stars and sun.

## 4. Ocean layers and water wake

The scene consists of (a) CSS gradient water, (b) static caustic-like line texture, (c) SVG coastal sand and foam paths, and (d) a transparent overlay rendering **only transient wake strokes**. No external image resources.

**Interaction reference: a finger stirring water sideways**. Moving a cursor should leave a **directional, non-concentric, asymmetrical wake**, not circular radial pulses.

Behavior table:

| Gesture | Visual feedback |
|---|---|
| Slow sideways move | Thin offset channel follows cursor vector |
| Fast move | Broader/taller channel; highlights spread |
| Curve / reversal | Old and new trails bend and cross |
| Stop | Trails fade over ≈1.2 sec |
| Exit water | Trail deactivates; no splashes over sand |
| Drag background to pan | Water wake is suppressed during pan |
| Touch | Short wake on tap; scrolling remains native |

**Prototype technique:** bounded recent pointer samples (`≤34` points; historical spec suggested 10–20, now capped higher for continuous cursors), `requestAnimationFrame` only while trails exist, two offset channels derived from the motion normal, short specular fragments, time-decay fade. Downsample transient canvas to ~75% CSS resolution with DPR capped at 1.25, without affecting the DOM text resolution. No simulated pressure field, particle pool or WebGL render loop. No rings are drawn. Switch off on hidden document/reduced-motion/lite mode.

**Visual limitation:** strokes suggest wake but do not bend/refraction-distort the background texture yet. This is an intentional lightweight starting point. Future enhancement: a low-resolution directional displacement shader limited to ocean area, gated behind profiling and hardware testing.

## 5. Project gallery

Two complementary treatments:

**Featured Work** uses beach postcard visuals, playful rotation and lift-on-hover. Each postcard remains a native button with accessible label and a project detail dialog. A postcard is not just a thumbnail; it establishes the coast/art-direction identity.

**Archive** uses minimal cards without unnecessary visual decoration, a Grid/List toggle with `aria-pressed` and dedicated metadata. It provides dependable access and comparison.

Project data shape: `id, title, type, description, tags[], year, status, art, sample`. Current data has sample entries; it must not be used publicly as if it were actual finished work. A project media asset manifest should also capture filename, aspect ratio, crop position and alt text, not require automatic visual AI interpretation.

## 6. Playground

Bounded local panel with draggable cards/objects and reset, plus adjacent Bento content modules. Local toy drag takes interaction priority over world pan. A keyboard-accessible fallback moves focused objects using arrow keys, Shift to step faster.

An experimental mini-app can be added later only if it has a distinct purpose, is discoverable and adds real value to the portfolio.

## 7. Mobile and accessibility

At `≤800px`: one-column vertical reading order, standard page scroll, no global free pan; the shore is still visually represented, with a local interactive water surface. Text and links remain DOM-based. Core project links never require drag/hover. Navigation menu uses real buttons, dialog uses native `<dialog>`, and desktop spatial map uses buttons.

Accessibility requirements: keyboard-accessible controls, visible focus, reduced motion, meaningful structure, alternative text for actual project screenshots, no scroll traps, no water canvas hit-testing over controls, target WCAG AA contrast for text. Unverified items require review rather than a compliance claim.

## 8. Motion and performance budgets

- Hover 120–200 ms; lift 180–280 ms; module transitions 200–350 ms; camera navigation ≈620 ms.
- Decorative canvas updates only in the presence of wake; frame loop ends after trails decay.
- The resize handler reconfigures the effect and spatial camera for desktop/mobile.
- Avoid complex backdrop filters, full-screen blur and particles.
- Animation is optional. `prefers-reduced-motion` disables transient water; manual Motion toggle available.
- Target real-world Core Web Vitals: LCP ≤2.5 s, INP ≤200 ms, CLS ≤0.1 (75th percentile as standard measurement practice). Smooth response target ≈60 FPS on ordinary desktop hardware; not verified in a lab or field.
- Use reduced quality for weaker devices when measured. Do not infer device power solely from user agent.

## 9. Content requirements

Before production replace: name/title, role, biography, real project metadata, real project screenshots and alternative text, contact email, repository/profile links, optional résumé and case study URLs. Sample art, contact details and project placeholders must never silently be treated as completed projects.

## 10. Acceptance criteria

1. All six regions accessible by global nav; drag/wheel/map also usable on desktop.
2. No unbounded panning, unexpected scroll traps or project-control capture by pan.
3. Wake follows pointer direction, no concentric ring bursts.
4. Wake stops rendering when idle/hidden/lite/reduced-motion.
5. Project postcards open details; Archive Grid/List works; Playground drag/reset works.
6. Mobile has natural page scrolling and functional navigation.
7. Keyboard focus and modal dismissal work.
8. No horizontal overflow at target mobile widths, no layout-breaking overlap at desktop targets.
9. Actual projects and links validated before production.
10. Performance and visual acceptance measured, not inferred from source code alone.

## 11. Known open decisions

- Exact personal identity and content, unprovided by user.
- Whether to retain wheel-by-waypoint navigation or enable conventional vertical scroll as an option after usability testing.
- Whether to upgrade simple wake strokes to a low-resolution distortion shader after a visual review and frame profiling.
- Deployment platform and final analytics/SEO stack.

**Guiding statement:** Build an experience, not a simulation.

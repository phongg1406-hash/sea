# SUNLIT SHORE — Design Specification v2.0

Status: **Concept fixed; Visual Prototype v2 recommended; production data and performance approval outstanding.**

## 1. North Star

A journey along Vietnam's coast personal portfolio with **Continuous Vertical Coastal Scroll**, playful coastal visual language, and a light **Directional Water Wake**. Not an ocean simulator and not a dashboard. Code-created visual language is mandatory; photorealistic textures are optional and currently not used. Text-only AI coding must be sufficient to maintain the project.

Three product priorities, in order:
1. Visitors can find projects, identify the creator, and navigate with ordinary controls.
2. Visual personality and tangible interaction create an experience worth exploring.
3. Effects must remain adaptive and inexpensive; all essential content survives without animation.

## 2. Layout and world geometry

**Continuous Vertical Coastal Scroll** replaces the previous spatial canvas. The document flows vertically with the coastline as a continuous artistic element.

- **Viewport**: Reveals a portion of the vertically scrolling document
- **Document nature**: Transformable HTML/CSS/SVG DOM stage (not bitmap canvas)
- **Primary navigation**: Natural vertical scrolling (mouse wheel, touch drag, keyboard arrow keys)
- **Secondary navigation**: Anchor links, Geographic Shore Map
- **Clamping**: Prevents unbounded drifting into empty space (top/bottom bounds)

### Section Positions and Sequential Order

The eight destinations follow Vietnam's coastline from north to south:

| Section | Destination | Primary activity | Land/Water Composition |
|---------|-------------|------------------|------------------------|
| 01 | TRÀ CỔ / HOME | Introduction, water wake | Hero left (sand), right (ocean) |
| 02 | HẠ LONG / PROJECTS | Featured postcard projects | Left (sand/postcards), right (ocean/postcards) |
| 03 | LĂNG CÔ / ABOUT ME | Editorial profile & personal journal | Left (sand/content), right (ocean/distant mountains) |
| 04 | ĐÀ NẴNG / SKILLS | Bento Cards + Floating Skill Net | Left (sand/bento), right (ocean/skill net) |
| 05 | QUY NHƠN / RESUME | Editorial Timeline + Compact Cards | Left (sand/timeline), right (ocean/cards) |
| 06 | NHA TRANG / PLAYGROUND | Interactive Lab Cards + Coastal Decorations | Left (sand/lab cards), right (ocean/decorations) |
| 07 | MŨI NÉ / PROJECT ARCHIVE | Coastal Project Library | Left (sand/project grid), right (ocean/dunes/kites) |
| 08 | MŨI CÀ MAU / CONTACT | Open Invitation + Thank You | Left (sand/content), right (ocean/mangroves/alluvial) |

### Visual Composition Rules

1. **Sand/land stays on the left side** of the artistic Main Scene
2. **Ocean stays on the right side** of the artistic Main Scene
3. **Their proportions vary continuously** along the document
4. **The coast must remain visually continuous** across all eight sections
5. **Content remains more important than effects**
6. **No mandatory horizontal panning** for primary navigation
7. **No scroll-jacking or mandatory scroll snapping**
8. **The coastline curves left and right** within the visual scene, creating an S-shaped coastal journey

### Coastal Geometry

Develop a continuous coastline geometry spanning the primary scroll journey with:
- Coastline control points
- Vertical composition strategy
- Land/water masking strategy
- Transition regions
- Responsive geometry behavior
- Content-safe regions
- Section anchoring strategy
- Coastline continuity constraints
- How composition changes with content height

Avoid brittle fixed coordinates tied to an assumed final document height.

## 3. Visual language

**Art direction**: Playful Brutalism × Coastal Editorial Design × Stylized Tropical Environment

| Token | Value | Purpose |
|-------|-------|---------|
| Ocean | `#00BCCD` | Water primary (varies by section) |
| Shallow | `#75E3DF` | Near-shore water |
| Sand | `#FFF0CB` | Warm content background |
| Foam | `#FFFDF4` | Highlights and card paper |
| Sun | `#FFB950` | Warm accent |
| Deep ocean ink | `#07515D` | Text on cyan |
| Sand ink | `#39352F` | Text on cream |
| Coral accent | `#FF7858` | Selected typography, icons |
| Light Silt (Cà Mau) | `#B8B59A` | Mangrove/alluvial areas |
| Alluvial Water (Cà Mau) | `#A4AA8E` | Silt-rich tidal water |
| Deep Water (Cà Mau) | `#87967E` | Earthy green-brown water |
| Mangrove (Cà Mau) | `#597D61` | Mangrove forests |

### Section-Specific Palette Transitions

- **TRÀ CỔ to HẠ LONG**: Warm turquoise ocean
- **HẠ LONG to LĂNG CÔ**: Limestone islands, consistent tropical water
- **LĂNG CÔ to ĐÀ NẴNG**: Transition to central coast waters
- **ĐÀ NẴNG to QUY NHƠN**: Continued central coast palette
- **QUY NHƠN to NHA TRANG**: South central coast, Nha Trang specific decorations
- **NHA TRANG to MŨI NÉ**: Transition to southeastern coast
- **MŨI NÉ to MŨI CÀ MAU**: **Gradual transition** from bright turquoise to earthy green-brown water and mangroves
  - Do NOT abruptly replace bright turquoise with brown at a hard section boundary
  - Gradient transition through the coastal journey

### Typography

- **Headline**: 85–146 desktop px, 54–96 mobile
- **Section headlines**: ≈40–67 px
- **Body text**: ≈16–23 px
- **Type system**: Use semantic tokens; design should never require graphic model to interpret spacing
- **Fonts**: Prefer system fonts or self-hosted, legally sourced subsets (Space Grotesk / Inter / Space Mono if approved)

### Shape treatments

- Smooth organic shoreline
- Rounded rectangular UI: ≈6–13 px radius
- Project postcards: near-sharp corners
- 1.5–2 px outlined forms
- Hard but modest shadows
- Restrained organic stickers, stars and sun
- Floating Skill Net: diamond-shaped interconnected mesh with slight curvature

## 4. Ocean layers and water wake

The scene consists of (a) CSS gradient water, (b) static caustic-like line texture, (c) SVG coastal sand and foam paths, and (d) a transparent overlay rendering **only transient wake strokes**. No external image resources.

**Interaction reference**: A finger stirring water sideways. Moving a cursor should leave a **directional, non-concentric, asymmetrical wake**, not circular radial pulses.

### Behavior table

| Gesture | Visual feedback |
|---------|-----------------|
| Slow sideways move | Thin offset channel follows cursor vector |
| Fast move | Broader/taller channel; highlights spread |
| Curve / reversal | Old and new trails bend and cross |
| Stop | Trails fade over ≈1.2 sec |
| Exit water | Trail deactivates; no splashes over sand |
| Drag background to pan | Water wake is suppressed during pan (does not affect main scroll) |
| Touch | Short wake on tap; scrolling remains native |

### Implementation Technique

- Bounded recent pointer samples (≤34 points)
- requestAnimationFrame only while trails exist
- Two offset channels derived from the motion normal
- Short specular fragments
- Time-decay fade
- Downsample transient canvas to ~75% CSS resolution with DPR capped at 1.25
- No simulated pressure field, particle pool or WebGL render loop
- No rings drawn
- Switch off on hidden document/reduced-motion/lite mode

### Visual limitation

Strokes suggest wake but do not bend/refraction-distort the background texture yet. This is an intentional lightweight starting point.

## 5. Project gallery

Two complementary treatments:

### Featured Work (Hạ Long / Projects)

- Uses beach postcard visuals, **subtle, deliberate rotation** and lift-on-hover
- Each postcard remains a native button with accessible label and a project detail dialog
- **One larger featured postcard and two supporting postcards** (Approved Option C)
- Postcards distributed across sand and ocean (not randomly regenerated)
- Avoid cluttering the reading area
- Stylized limestone islands in the background
- Clicking a postcard opens the **Shared Project Detail Modal**

### Project Archive (Mũi Né / Project Archive)

- Uses minimal cards without unnecessary visual decoration
- Grid/List toggle with `aria-pressed` and dedicated metadata
- Provides dependable access and comparison
- **Structured project grid** (Approved Option A)
- Search input
- Useful category filters
- Responsive project cards
- Consistent project thumbnails
- Project names, summaries, and technology tags
- **Shared Project Detail Modal** from Hạ Long
- Data shared with Featured Projects
- No inconsistent duplicate content
- Search/filter UI should match the actual number and type of projects

### Project data shape

`id, title, type, description, tags[], year, status, art, sample`

Current data has sample entries; it must not be used publicly as if it were actual finished work.

A project media asset manifest should capture filename, aspect ratio, crop position and alt text.

## 6. Playground (Nha Trang / Playground)

**Interactive Lab Cards + Nha Trang Coastal Decorations**

This section is reserved for real creative coding experiments and small interactive demos.

Cards may represent:
- Water or procedural graphic experiments
- Motion/UI experiments
- Mini interactive experiences

Avoid duplicating decorative effects already present throughout the website unless a demo provides a genuinely new interaction.

Local environmental references:
- Hòn Chồng rock formations
- Small stylized silhouette inspired by Po Nagar Cham Towers
- Tropical marine life and small coral details

Keep decorative elements recognizable but restrained.

Use the location label:
`06 / NHA TRANG, KHÁNH HÒA`

Main heading remains:
`PLAYGROUND`

Do not invent working demos or present placeholders as completed projects.

## 7. Skills (Đà Nẵng / Skills)

Approved composition:

**Bento Cards on the Sand + Floating Skill Net on the Water**

### Bento Cards

Four primary content categories:
1. Frontend & UI
2. Backend & Data
3. Tools & Workflow
4. Currently Learning

Bento sizes should be asymmetric but carefully aligned.

Cards must remain readable and accessible.

The listed skills must ultimately reflect real user proficiency.

Do not fabricate expertise or show arbitrary percentage-based skill bars.

### Floating Skill Net

This is a signature visual feature.

A fishing-net-inspired mesh floats ON TOP OF the sea on the right side.

Required visual characteristics:
- Diamond-shaped interconnected net
- Roughly 8–10 recognizable skill logos on desktop, adjusted for actual space
- Technologies such as Git, React, SQL, TypeScript, etc. are examples
- Skill logos are nodes at net intersections
- Small buoys may appear at selected net edges
- Net strands have slight visual curvature
- Entire structure gently rises and falls with the waves
- Adjacent nodes move with phase offsets
- Motion resembles flexible netting floating on water, not a rigid board rotating
- Logos stay legible and must not be distorted excessively

### Interaction

- Cursor proximity gently deforms nearby mesh nodes
- Deformation relaxes back to equilibrium
- Hovering React can highlight the Frontend Bento Card
- Hovering Git can highlight Tools
- Hovering SQL can highlight Backend & Data
- Selecting a Bento Card can highlight the corresponding net nodes
- Skill information must remain accessible without interacting with the net

Prioritize SVG-based rendering and a lightweight custom motion model.

Do not require full physics simulation.

On mobile, simplify the mesh and reduce visible logos.

## 8. Resume (Quy Nhơn / Resume)

Approved layout:

**Editorial Timeline + Compact Cards**

This is ONE main section containing:
- Experience
- Education
- Certifications

Do not create separate main destinations for Education or Certifications.

### Desktop

- Large vertical Experience Timeline
- Compact Education Card
- Compact Certifications Card
- Download Resume PDF action

Certification entries should support credential verification links if available.

Do not display incomplete certifications as completed.

No invented education, employment, dates, or credentials.

### Environment

- Stylized coastal rock formations
- Light, professional styling
- Limited decorative movement

### Mobile

- Experience
- Education
- Certifications

Stack sections naturally.

## 9. About Me (Lăng Cô / About Me)

Layout: **Coastal Editorial × Personal Journal**

Approved personal-image concept:

**Floating Film Photo**

- Large simple heading: ABOUT ME
- One concise personal introduction
- A small film-style personal photograph close to the shoreline
- Slightly tilted photo, like a memory placed by the sea
- Two or three Personal Notes modules
- Suggested note themes:
  - Interests
  - My Approach
  - Currently Learning
- Calm environment with stylized distant mountains
- Clear editorial typography
- More negative space and fewer moving objects than PROJECTS

Do not use poetic primary headings.

The image is personal content and must remain a placeholder until the user supplies the actual photo.

## 10. Contact (Mũi Cà Mau / Contact)

Approved layout:

**Open Invitation + Thank You**

Required content:
- Clear heading: CONTACT
- Short invitation to get in touch
- Primary email CTA
- Visible email address
- GitHub and LinkedIn links, where provided
- Back to Top
- Minimal footer

No contact form is required for the initial version.

### Friendly Thank You message

Include a brief, sincere thank-you note toward the end.

Approved draft direction:
"Thanks for stopping by! ♡

Thank you for taking the time to explore my work and considering me. It really means a lot.

I hope we get to create something together someday!"

This is draft copy, not mandatory final wording.

Keep the sentiment warm, simple, and professional.

### Cà Mau landscape

This region must look meaningfully different from the earlier turquoise-water destinations.

Environmental references:
- Mangrove forests
- Coastal alluvial land
- Silt-rich tidal water
- Earthy green-brown water
- Warm muted foam

Proposed palette starting points:
- Light Silt: #B8B59A
- Alluvial Water: #A4AA8E
- Deep Water: #87967E
- Mangrove: #597D61

Gradually transition the ocean palette from Mũi Né to Cà Mau.

Do NOT abruptly replace bright turquoise with brown at a hard section boundary.

At CONTACT:
- Content fades in
- Once visible near the document end, it should remain readable
- Do not force a fade out at the bottom
- Show a subtle 08/08 journey completion state
- Back to Top returns to Trà Cổ

## 11. Mobile and accessibility

At ≤800px: one-column vertical reading order, standard page scroll, no global free pan; the shore is still visually represented, with a local interactive water surface. Text and links remain DOM-based. Core project links never require drag/hover. Navigation menu uses real buttons, dialog uses native `<dialog>`, and desktop spatial map uses buttons.

Accessibility requirements: keyboard-accessible controls, visible focus, reduced motion, meaningful structure, alternative text for actual project screenshots, no scroll traps, no water canvas hit-testing over controls, target WCAG AA contrast for text. Unverified items require review rather than a compliance claim.

## 12. Motion and performance budgets

- Hover 120–200 ms; lift 180–280 ms; module transitions 200–350 ms; camera navigation ≈620 ms (for geographic map interactions)
- Decorative canvas updates only in the presence of wake; frame loop ends after trails decay.
- The resize handler reconfigures the effect and spatial camera for desktop/mobile.
- Avoid complex backdrop filters, full-screen blur and particles.
- Animation is optional. `prefers-reduced-motion` disables transient water; manual Motion toggle available.
- Target real-world Core Web Vitals: LCP ≤2.5 s, INP ≤200 ms, CLS ≤0.1 (75th percentile as standard measurement practice). Smooth response target ≈60 FPS on ordinary desktop hardware; not verified in a lab or field.
- Use reduced quality for weaker devices when measured. Do not infer device power solely from user agent.

## 13. Content requirements

Before production replace: name/title, role, biography, real project metadata, real project screenshots and alternative text, contact email, repository/profile links, optional résumé and case study URLs. Sample art, contact details and project placeholders must never silently be treated as completed projects.

## 14. Acceptance criteria

1. All eight regions accessible by natural vertical scrolling; anchor navigation and geographic map also usable.
2. No unbounded panning, unexpected scroll traps or project-control capture by pan (replaced with vertical scroll).
3. Wake follows pointer direction, no concentric ring bursts.
4. Wake stops rendering when idle/hidden/lite/reduced-motion.
5. Project postcards open details; Archive Grid/List works; Playground drag/reset works.
6. Mobile has natural page scrolling and functional navigation.
7. Keyboard focus and modal dismissal work.
8. No horizontal overflow at target mobile widths, no layout-breaking overlap at desktop targets.
9. Actual projects and links validated before production.
10. Performance and visual acceptance measured, not inferred from source code alone.

## 15. Known open decisions

- Exact personal identity and content, unprovided by user.
- Whether to retain wheel-by-waypoint navigation for geographic map or enable conventional vertical scroll as an option.
- Whether to upgrade simple wake strokes to a low-resolution distortion shader after a visual review and frame profiling.
- Deployment platform and final analytics/SEO stack.

**Guiding statement**: Build an experience, not a simulation.
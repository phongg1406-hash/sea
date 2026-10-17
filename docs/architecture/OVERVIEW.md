# Architecture Overview

## Boundaries

- **Continuous Vertical Coastal Scroll**: The primary document flow with natural vertical scrolling, replacing the previous spatial canvas.
- **Main Scene**: The artistic representation of Vietnam's coastline with sand on left, ocean on right.
- **Geographic Shore Map**: A separate navigation component showing actual geographic locations.
- **Project Gallery**: Structured project grids with postcards (Featured Work) and minimal cards (Archive).
- **Shared Project Detail Modal**: Consistent modal used for both PROJECTS and PROJECT ARCHIVE sections.
- **Directional Water Wake**: A stylized water effect responding to cursor movement.
- **Floating Skill Net**: Signature visual feature in the SKILLS section (Đà Nẵng).
- **Vũng Tàu Secret Easter Egg**: Out-of-flow destination accessible through discovery flow.
- **Modular Components**: UI built with React and TypeScript, following a feature-based structure.
- **State Management**: To be determined based on complexity (prefer React Context or lightweight solutions).
- **Styling**: CSS modules or styled-components for scoped styles, with a focus on performance.
- **Assets**: Optimized images, icons, and textures stored in `public/assets`.

## Technical Stack

- React 18+
- TypeScript
- Vite (build tool)
- TODO: Additional libraries as needed (e.g., for animations, gestures)

## Performance Considerations

- Code-splitting and lazy loading of features.
- Minimizing JavaScript bundle size.
- Efficient rendering of the continuous coastal scroll and water wake.
- Accessibility-first development (WCAG 2.1 AA).

## Architectural Decision Record

### Replaced: Website-wide Freely Pannable 2D Spatial Canvas

**Decision**: Replace the website-wide freely pannable 2D spatial canvas with a Continuous Vertical Coastal Scroll.

**Date**: 2026-10-17 (per DESIGN FREEZE V2.0)

**Status**: Supersedes the previous spatial canvas approach documented in SPATIAL_COMPOSITION.md

**Rationale**:
1. **Usability**: Users found spatial navigation disorienting and preferred conventional scrolling for primary navigation.
2. **Accessibility**: Vertical scrolling is more accessible and familiar to users, especially those using assistive technologies.
3. **Performance**: Eliminates complexity of 2D world management, camera systems, and spatial hit-testing.
4. **Focus on Content**: Allows users to focus on portfolio content rather than learning a novel navigation system.
5. **Mobile Experience**: Provides consistent experience across devices without requiring different interaction models.

**Consequences**:
- **Positive**:
  - Simplified implementation and maintenance
  - Better accessibility and usability
  - More predictable performance characteristics
  - Familiar interaction model for users
- **Negative**:
  - Loss of exploratory 2D world discovery
  - Requires rethinking of certain spatial interactions (now expressed through vertical progression)
  - Need to express geographical journey through vertical scroll rather than 2D movement

**Mitigations**:
- The artistic Main Scene still shows a continuous S-shaped coastline journey
- The Geographic Shore Map provides actual geographic context
- Section-themed environmental decorations maintain the coastal journey theme
- Scroll fade-in/fade-out provides transitional feedback between sections
- Anchor navigation allows direct access to sections

**Alternatives Considered**:
1. **Hybrid Approach**: Keep spatial canvas for desktop, vertical scroll for mobile - Rejected due to inconsistency and development complexity.
2. **Scroll-jacking with Snapping**: Hijack scroll to force section-by-section progression - Rejected due to accessibility concerns and user preference for natural scrolling.
3. **Waypoint-only Navigation**: Only allow navigation via waypoints/mini-map - Rejected due to poor discoverability and accessibility.

**Related Documents**:
- This decision supersedes the spatial canvas specifications in `docs/design/SPATIAL_COMPOSITION.md`
- See `docs/DESIGN_SPEC.md` for the approved Continuous Vertical Coastal Scroll specification
- See `docs/design/RESPOVSIVE_SPEC.md` for responsive behavior guidelines

### Added: Geographic Shore Map as Separate Navigation Component

**Decision**: Implement a separate geographic navigation map showing actual Vietnamese coast locations.

**Date**: 2026-10-17

**Status**: New addition

**Rationale**:
1. **Educational Value**: Provides real geographic context for the artistic coastline journey.
2. **Accessibility**: Offers an alternative navigation mechanism for users who prefer map-based navigation.
3. **Context Preservation**: Maintains the connection to real-world geography while allowing artistic freedom in the Main Scene.
4. **Discovery Enabler**: Essential for the Vũng Tàu Easter Egg discovery flow.

**Implementation**:
- Collapsed by default (shows "MAP · 01/08")
- Expands to show actual Vietnamese coastline with eight main destinations marked
- Uses appropriate geographic data sources with proper attribution
- Handles disputed sovereignty responsibly (Hoàng Sa and Trường Sa)
- Supports mouse, touch, keyboard, and screen reader interaction
- Updates active destination automatically with scroll progress
- On mobile, uses compact expandable navigation panel

**Technical Considerations**:
- SVG-based for lightweight, scalable output
- Data sources must be verified and licensed appropriately
- Responsive design to work across device sizes
- Accessible labels and keyboard navigation required

### Added: Vũng Tàu Secret Easter Egg as Out-of-Flow Destination

**Decision**: Implement Vũng Tàu as a separate route/view/overlay scene, not part of the normal document flow.

**Date**: 2026-10-17

**Status**: New addition

**Rationale**:
1. **Preserve Main Journey**: The primary scroll journey must always have exactly eight destinations.
2. **Discovery Experience**: The Easter Egg should feel special and discovered, not accidentally encountered.
3. **Accessibility**: Must be optional and not interfere with primary portfolio experience.
4. **Technical Cleanliness**: Avoids complications with scroll position, document length, and focus management.

**Implementation Approaches Evaluated**:
1. **Hidden DOM Section**: Rejected - violates requirement that Easter Egg must NEVER appear through ordinary vertical scrolling.
2. **Route/View (SPA)**: Selected - Using React router or similar to create separate view.
3. **Overlay Scene**: Selected - Creating absolutely positioned overlay that preserves scroll context.
4. **Dialog/Modal Approach**: Considered but less suitable for immersive experience.

**Selected Approach**: Overlay scene with scroll position preservation
- Opening the Easter Egg preserves exact prior scroll position and focus context
- Closing restores the user to their exact previous location
- Main document scroll length and section order remain unchanged (always eight destinations)
- Discovery state may be remembered locally (browser storage)
- No database or account required to unlock
- Works across desktop and mobile with touch support

**Key Requirements**:
- Discovery flow: Bottle → Hint → Golden Starfish on Map → Vũng Tàu Memories → Return
- Must not obscure Contact content when bottled
- Must be discoverable but not overly conspicuous
- Golden Starfish marker hidden before bottle is opened
- Clear Return action to restore prior state

## Responsive Strategy

### Desktop (≥ 800px)
- Continuous Vertical Coastal Scroll with artistic Main Scene
- Left sand / right ocean composition maintained
- Geographic Shore Map as expandable panel
- Full Directional Water Wake implementation
- Floating Skill Net with 8-10 visible logos
- Hover-based interactions where appropriate

### Mobile (< 800px)
- Natural vertical scrolling continues as primary behavior
- Coastline may become narrower decorative edge or simplified water area
- Skills Bento Cards stack appropriately
- Floating Skill Net uses fewer visible nodes/logos
- Floating Projects rearrange to fit mobile without overlap
- Project Detail Modal is mobile-friendly
- Geographic Shore Map becomes compact expandable navigation panel
- Vũng Tàu discovery works through touch
- Touch gestures for scrolling take priority over Water Wake and decorative dragging
- Local water interaction replaces global wake (performance optimization)

### Breakpoints
- Primary: 800px (as specified in DESIGN_SPEC.md)
- Secondary breakpoints for refinement as needed
- Mobile-first approach: design for smallest screen first, then enhance

## Accessibility/Performance Concerns

### Accessibility
- All essential content and functionality must work without animation (`prefers-reduced-motion`)
- Keyboard navigation must reach all interactive elements
- Focus management must be preserved during section transitions and Easter Egg opening/closing
- Alternative text for all meaningful images and decorative elements
- Sufficient color contrast (WCAG AA minimum)
- Touch targets minimum 44x44px with adequate spacing
- Semantic HTML and ARIA labels where needed
- Reduced motion alternatives for all animated elements
- Skip navigation links available
- Visible focus indicators

### Performance
- Main rendering risks: Coastline layout complexity, SVG sizing constraints
- Mitigation: Use CSS where possible, optimize SVG paths, implement viewport culling for distant sections
- Skill Net animation costs: Use lightweight custom motion model, avoid physics simulation
- Water Wake performance costs: Canvas 2D with bounded history, downsample resolution, automatic deactivation
- Map data and licensing concerns: Use verified open-source geographic data with proper attribution
- Responsive risks: Test across device sizes, ensure content remains readable
- Accessibility issues: Audit with screen readers and keyboard-only navigation
- Scroll behavior conflicts: Ensure anchor navigation reveals target content correctly
- Browser compatibility: Test target browsers, provide fallbacks where needed

## Rendering Boundaries

### What belongs in the Main Scene (artistic coastline):
- Continuous S-shaped coastline geometry
- Sand/land areas (left side)
- Ocean/water areas (right side)
- Section-specific environmental decorations
- Floating Skill Net (in SKILLS section only)
- Directional Water Wake (water areas only)
- Interactive beach objects (shells, crabs, etc.)
- Marine life where appropriate
- Skill Net buoys and deformation effects
- Vũng Tàu discovery bottle (in Cà Mau waters)
- Scroll fade-in/fade-out transitional effects

### What belongs in separate components/UI layers:
- Geographic Shore Map (separate navigation component)
- Navigation controls (skip links, menu toggles)
- Section headings and primary content
- Project cards and postcards
- Bento Cards and Compact Cards
- Project Detail Modal
- Vũng Tàu Easter Egg (out-of-flow overlay/scene)
- UI overlays (tooltips, hints, prompts)
- Scroll hints and progress indicators
- Motion toggles and accessibility controls

### What is strictly prohibited in Main Scene:
- Actual project screenshots as UI textures/backgrounds
- Photorealistic textures that require image editing software
- External UI kits that conflict with code-first approach
- Random card positions at runtime
- Unnecessary full-screen loading animations
- Excessive 3D or heavy image assets
- Content that obscures essential information
- Decorative physics that moves actual buttons, navigation items, or project cards out of place

## Data Flow

1. **Content Data**: Project metadata, personal information, skills list (stored in JSON or similar)
2. **Presentation Data**: Design tokens, layout specifications, interaction states (managed by React state/CSS)
3. **Navigation State**: Scroll position, active section, map state, Easter Egg discovery state
4. **Interaction State**: Cursor position (for Water Wake), hover states, focus states, drag states
5. **Environmental State**: Water wake trails, Skill Net deformation, ambient animations

## Component Hierarchy (Conceptual)

```
App
├── Header (branding, navigation, controls)
├── Main
│   ├── GeographicShoreMap (collapsible/expandable panel)
│   ├── ContinuousCoastalScroll
│   │   ├── BackgroundLayers (ocean, sand, coastline)
│   │   ├── Section01_Home (Trà Cổ)
│   │   │   ├── HeroIntroduction
│   │   │   ├── OceanInteractionArea
│   │   │   └── DirectionalWaterWake
│   │   ├── Section02_Projects (Hạ Long)
│   │   │   ├── FloatingPostcardGallery
│   │   │   ├── StylizedLimestoneIslands
│   │   │   └── SharedProjectDetailModal (portal)
│   │   ├── Section03_AboutMe (Lăng Cô)
│   │   │   ├── CoastalEditorialContent
│   │   │   ├── FloatingFilmPhoto
│   │   │   └── PersonalNotesModules
│   │   ├── Section04_Skills (Đà Nẵng)
│   │   │   ├── BentoCardsOnSand
│   │   │   │   ├── FrontendUI
│   │   │   │   ├── BackendData
│   │   │   │   ├── ToolsWorkflow
│   │   │   │   ├── CurrentlyLearning
│   │   │   │   └── FloatingSkillNetOnWater
│   │   ├── Section05_Resume (Quy Nhơn)
│   │   │   ├── EditorialTimeline
│   │   │   ├── CompactCards
│   │   │   │   ├── Education
│   │   │   │   └── Certifications
│   │   ├── Section06_Playground (Nha Trang)
│   │   │   ├── InteractiveLabCards
│   │   │   └── NhaTrangCoastalDecorations
│   │   ├── Section07_ProjectArchive (Mũi Né)
│   │   │   ├── CoastalProjectLibrary
│   │   │   │   ├── StructuredProjectGrid
│   │   │   │   ├── SearchInput
│   │   │   │   ├── CategoryFilters
│   │   │   │   └── SharedProjectDetailModal (portal)
│   │   └── Section08_Contact (Mũi Cà Mau)
│   │       ├── OpenInvitation
│   │       │   ├── PrimaryEmailCTA
│   │   │   ├── VisibleEmailAddress
│   │   │   ├── GitHubLinkedInLinks
│   │   │   └── BackToTop
│   │       └── ThankYouMessage
│   ├── WaterWakeCanvas (transparent overlay)
│   └── ScrollFadeSystem (entrance/exit transitions)
├── VungTauEasterEgg (out-of-flow overlay/scene)
│   ├── DiscoveryBottle (in Cà Mau waters)
│   ├── HintSystem
│   ├── GoldenStarfishMarker (on Geographic Map)
│   └── VungTauMemoriesScene
├── Footer (attribution, legal)
└── Modals
    ├── SharedProjectDetailModal (referenced from sections)
    └── SystemModals (alerts, confirms, etc.)
```
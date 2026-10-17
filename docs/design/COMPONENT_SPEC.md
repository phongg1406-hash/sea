# Sunlit Shore Component Specification

## Overview

This document specifies the visual and interaction design for all UI components in the Sunlit Shore project, based on the approved DESIGN_SPEC.md and architectural guidelines.

## Design Principles

Following the principles from DESIGN_SPEC.md:
- Playful Brutalism × Coastal Editorial Design × Stylized Tropical Environment
- Code-first artwork (CSS/SVG/canvas)
- Performance-conscious implementations
- Accessibility-first approach (WCAG 2.1 AA)
- Minimal necessary interactions

## Component Categories

### 1. Navigation Components

#### Primary Navigation
- **Purpose**: Global site navigation between the eight sections
- **Location**: Fixed or persistent based on viewport
- **Design**: 
  - Text labels only (no icons) using Courier New
  - Horizontal arrangement on desktop, vertical collapse on mobile
  - Active state indicator: Underline or background tint
  - Hover/focus states: Subtle color shift or outline
- **States**: Default, hover, focus, active/current, disabled

#### Geographic Shore Map
- **Purpose**: Visual indication of current location along Vietnam's coastline
- **Design**:
  - Collapsible/expandable panel (shows "MAP · 01/08" when collapsed)
  - Actual Vietnamese coastline with eight main destinations marked when expanded
  - Current section highlighted
  - Hover/tooltip showing section name
  - Click to navigate to section
  - Handles disputed sovereignty responsibly (Hoàng Sa and Trường Sa)
  - Supports mouse, touch, keyboard, and screen reader interaction
  - Updates active destination automatically with scroll progress
  - On mobile, uses compact expandable navigation panel

### 2. Interactive Components

#### Buttons
- **Primary Button**:
  - Shape: Square-cornered or slightly rounded (max 8px radius)
  - Background: Sun accent (#FFB950)
  - Text: Sand ink (#39352F) or Deep ocean ink (#07515D) for contrast
  - Height: Minimum 44px for touch targets
  - Hover: Slightly darker shade or opacity shift
  - Active/Pressed: Deeper shade or scale down slightly
- **Secondary/Button Outline**:
  - Background: Transparent or Foam (#FFFDF4)
  - Border: 1-2px solid Sun accent or Ocean
  - Text: Matching border color
  - Hover: Background tint to Sun at 10-20% opacity

#### Project Postcards (Featured Work)
- **Purpose**: Visual representation of featured projects
- **Design** (from DESIGN_SPEC.md):
  - Beach postcard visuals
  - Playful rotation (slight random tilt: -5° to +5°)
  - Lift-on-hover/subtle elevation
  - Near-sharp corners (4-6px radius)
  - 1.5-2px outlined forms
  - Accessible label and project detail dialog trigger
- **States**: Default, hover, focus, pressed, disabled
- **Content**: Project thumbnail, title, optional tags/category

#### Archive Cards (Project Archive)
- **Purpose**: Minimal project representation for browsing
- **Design** (from DESIGN_SPEC.md):
  - Minimal cards without unnecessary decoration
  - Grid/List toggle with aria-pressed
  - Dedicated metadata display
  - Dependable access and comparison
- **States**: Default, hover, focus, selected
- **Content**: Project title, type/tags, year, status indicators

### 3. Form Components

#### Input Fields
- **Design**:
  - Height: Minimum 44px for touch
  - Border: 1-2px solid, rounded corners (4-6px)
  - Background: Foam (#FFFDF4) or transparent
  - Text: Sand ink (#39352F)
  - Placeholder: Muted Sand ink at 50% opacity
  - Focus: Outline or border color shift to Sun accent
  - Error: Border color shift to Coral accent (#FF7858)
- **Types**: Text, email, textarea, select

#### Toggle Controls
- **Design**:
  - Visual indicator of state (checked/unchecked)
  - Sufficient touch target (44x44px minimum)
  - Clear on/off distinction
  - Animation for state change (if enabled)
- **Examples**: Grid/List toggle, Motion toggle, Reduced motion toggle

### 4. Display Components

#### Project Detail Dialog
- **Purpose**: Show detailed information about a selected project
- **Design**:
  - Modal/dialog overlay with backdrop
  - Responsive sizing (max-width, max-height)
  - Close button (top corner or bottom)
  - Scrollable content if needed
  - Project media (images/screenshots)
  - Metadata: title, type, tags, year, description
  - Action links: live site, repository, case study
- **Accessibility**: Proper focus trap, ESC to close, aria-label
- **Note**: Shared component used for both PROJECTS and PROJECT ARCHIVE sections

#### Metadata Displays
- **Purpose**: Show structured information (project details, skills, etc.)
- **Design**:
  - Label-value pairs
  - Labels: Courier New, medium weight, text-transform: uppercase
  - Values: Arial/Helvetica, regular weight
  - Dividers: Subtle lines or spacing
  - Icons: Optional SVG icons for visual scanning

#### Labels & Tags
- **Purpose**: Categorization and status indication
- **Design**:
  - Small pill or rounded rect shape
  - Background: Tint of accent color at 10-20% opacity
  - Text: Matching accent color at 80-100% opacity
  - Radius: 4-8px
  - Font: Smaller than body text
  - Examples: Project types, skill levels, status indicators

### 5. Layout & Structural Components

#### Continuous Vertical Coastal Scroll Container
- **Purpose**: Houses the vertically scrolling document with continuous coastline
- **Design**:
  - Natural vertical scrolling (mouse wheel, touch drag, keyboard arrow keys)
  - Overflow: auto to enable scrolling
  - Background: Gradient or solid water color varying by section
  - Sand/land masking: Left side of artistic Main Scene
  - Ocean/water area: Right side of artistic Main Scene
  - Coastline continuity: Visually continuous S-shaped coastal journey
  - Section anchoring: Clear visual separation between sections
  - Scroll fade system: Entrance/exit transitions between sections
  - Event handling: Capture pointer events for Water Wake generation

#### Ocean/Water Layer
- **Purpose**: Visual water base for the continuous coastal scroll
- **Design**:
  - CSS gradient or animated texture
  - Base color varies by section (Ocean to Alluvial Water/Mangrove)
  - Shallow water transition: Shallow (#75E3DF) near shores
  - Optional: SVG coastal paths for sand/foam boundaries
  - Performance: Limited repaints, CSS-only where possible
  - Section-specific palette transitions: Gradual changes between sections

#### Directional Water Wake
- **Purpose**: Transient visual feedback for cursor movement
- **Design** (from DESIGN_SPEC.md):
  - Transparent overlay rendering only transient wake strokes
  - No external image resources
  - Interaction reference: finger stirring water sideways
  - Directional, non-concentric, asymmetrical wake
  - Behavior table from spec implemented exactly
  - Technique: bounded recent pointer samples, requestAnimationFrame while trails exist
  - Visual limitation acknowledged: strokes suggest wake but don't bend/refract background yet
  - Performance: Switch off on hidden document/reduced-motion/lite mode

#### Vũng Tàu Secret Easter Egg Container
- **Purpose**: Out-of-flow destination accessible through discovery flow
- **Design**:
  - Absolutely positioned overlay/scene (not part of normal document flow)
  - Preserves exact prior scroll position and focus context when opened
  - Closing restores user to exact previous location
  - Main document scroll length and section order remain unchanged (always eight destinations)
  - Discovery state may be remembered locally (browser storage)
  - Works across desktop and mobile with touch support
  - Discovery flow: Bottle → Hint → Golden Starfish on Map → Vũng Tàu Memories → Return
  - Must not obscure Contact content when bottled
  - Golden Starfish marker hidden before bottle is opened
  - Clear Return action to restore prior state

#### Bento Grid (Skills section)
- **Purpose**: Display skills in four categories on sand area
- **Design**:
  - Four primary content categories:
    1. Frontend & UI
    2. Backend & Data
    3. Tools & Workflow
    4. Currently Learning
  - Asymmetric but carefully aligned layout
  - Readable and accessible cards
  - Reflects real user proficiency (no fabricated expertise)
  - No percentage-based skill bars
  - Positioned on sand/land area (left side)

#### Floating Skill Net (Skills section)
- **Purpose**: Signature visual feature in SKILLS section (Đà Nẵng)
- **Design**:
  - Fishing-net-inspired mesh floats ON TOP OF the sea on the right side
  - Diamond-shaped interconnected net
  - Roughly 8-10 recognizable skill logos on desktop, adjusted for actual space
  - Technologies such as Git, React, SQL, TypeScript, etc. as examples
  - Skill logos are nodes at net intersections
  - Small buoys may appear at selected net edges
  - Net strands have slight visual curvature
  - Entire structure gently rises and falls with the waves
  - Adjacent nodes move with phase offsets
  - Motion resembles flexible netting floating on water, not a rigid board rotating
  - Logos stay legible and must not be distorted excessively
  - Interaction: Cursor proximity gently deforms nearby mesh nodes
  - Hovering React can highlight the Frontend Bento Card
  - Hovering Git can highlight Tools
  - Hovering SQL can highlight Backend & Data
  - Selecting a Bento Card can highlight the corresponding net nodes
  - Skill information must remain accessible without interacting with the net
  - Prioritize SVG-based rendering and lightweight custom motion model
  - Do not require full physics simulation
  - On mobile, simplify the mesh and reduce visible logos

### 6. Feedback & Status Components

#### Loading States
- **Design**:
  - Skeleton screens or placeholder shapes
  - Minimal animation (if not reduced motion)
  - Clear indication of loading status
  - Respects prefers-reduced-motion

#### Error States
- **Design**:
  - Clear, actionable error messages
  - Visual prominence without alarm
  - Recovery options when applicable
  - Consistent with brand colors (Coral accent for emphasis)

#### Success States
- **Design**:
  - Subtle visual confirmation
  - Temporary status indicators
  - Positive reinforcement without distraction

#### Scroll Fade System
- **Purpose**: Provide transitional feedback between sections
- **Design**:
  - Fade-in/fade-out effects as sections enter/leave viewport
  - Implemented as transparent overlays
  - Performance-conscious implementation
  - Respects prefers-reduced-motion setting

## Interaction Patterns

### Hover & Focus
- **Timing**: 120-200ms hover, 180-280ms lift (from DESIGN_SPEC.md)
- **Feedback**: Visual change indicating interactivity
- **Consistency**: Similar patterns across similar elements
- **Accessibility**: Visible focus indicators (minimum 2px outline)

### Touch & Gesture
- **Targets**: Minimum 44x44px (Apple/Material guidelines)
- **Spacing**: 8px+ between touch targets
- **Primary Interactions**: Tap/click, not hover-reliant
- **Feedback**: Press/tap feedback within 100ms
- **Gesture Conflicts**: Avoid horizontal swipe on main content

### Keyboard Navigation
- **Order**: Logical, follows visual flow
- **Indicators**: Visible focus on all interactive elements
- **Traps**: None - easy escape from all components
- **Shortcuts**: Consider power-user shortcuts where beneficial

### Motion & Animation
- **Principles**:
  - Purposeful animation (conveys meaning, not just decoration)
  - Context-aware timing
  - Spatial continuity maintained
  - Respects prefers-reduced-motion
  - Performance conscious (transform/opacity only)
- **Specifics**:
  - Entrance animations: staggered by 60-90ms
  - Feedback animations: press, hover, focus
  - One moving element requirement (from design-taste-frontend)
  - Signature move: Directional water wake
  - Floating Skill Net: Gentle wave-like motion with phase offsets
  - Scroll transitions: Fade effects between sections

## Implementation Guidelines

### CSS Approach
- **Scope**: CSS modules or scoped styling to prevent leakage
- **Variables**: Use CSS custom properties for theme values
- **Units**: Prefer relative units (rem, em, %) where appropriate
- **Breakpoints**: Systematic breakpoints (mobile-first approach)
- **Performance**: Minimize layout thrashing, use transform/opacity for animation

### Accessibility Requirements
- **Contrast**: Minimum 4.5:1 for normal text (WCAG AA)
- **Focus**: Visible indicators on all interactive elements
- **Labels**: Proper form labeling, aria-label for icon-only buttons
- **Semantics**: Correct HTML elements for meaning
- **Keyboard**: Full functionality via keyboard
- **ARIA**: Appropriate roles, states, properties where needed
- **Reduced Motion**: All essential content and functionality must work without animation

### Performance Considerations
- **Render Frequency**: Limit expensive operations (especially water wake)
- **Asset Size**: Optimize images, inline critical SVG/CSS
- **JavaScript**: Minimize main thread work, use requestAnimationFrame
- **Layout**: Avoid forced synchronous layouts
- **Memory**: Clean up event listeners, observers, timeouts
- **Water Wake Performance**: Canvas 2D with bounded history, downsample resolution, automatic deactivation
- **Map Data**: Use verified open-source geographic data with proper attribution
- **Skill Net Animation**: Lightweight custom motion model, avoid physics simulation

### Code-First Artwork Rules
- **No External Images**: All visuals created via CSS/SVG/canvas
- **Exceptions**: Actual project screenshots (content, not UI)
- **Procedural Generation**: Where possible, use code to generate patterns
- **SVG**: For scalable vector graphics (icons, shapes, paths)
- **Canvas**: Only where necessary (water wake implementation)
- **CSS**: For shapes, gradients, positioning, transitions

### Rendering Boundaries

#### What belongs in the Main Scene (artistic coastline):
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

#### What belongs in separate components/UI layers:
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

#### What is strictly prohibited in Main Scene:
- Actual project screenshots as UI textures/backgrounds
- Photorealistic textures that require image editing software
- External UI kits that conflict with code-first approach
- Random card positions at runtime
- Unnecessary full-screen loading animations
- Excessive 3D or heavy image assets
- Content that obscures essential information
- Decorative physics that moves actual buttons, navigation items, or project cards out of place

## Component States Matrix

All interactive components should define these states clearly:
- **Default**: Normal, resting state
- **Hover**: Pointer over element (not touch)
- **Focus**: Element has keyboard focus
- **Active/Pressed**: Element being activated
- **Disabled**: Non-interactive state
- **Selected**: Currently chosen option (for toggles, radio, etc.)
- **Error**: Validation failure state
- **Loading**: Async operation in progress

## Naming Conventions (for implementation)
- **Components**: PascalCase (ProjectPostcard, ArchiveCard)
- **Props/Props**: camelCase (onClick, isDisabled)
- **CSS Classes**: kebab-case (.project-postcard, .archive-card)
- **CSS Variables**: kebab-case prefixed (--color-accent-primary)
- **Events**: camelCase (onHoverStart, onWakeUpdate)

## Migration Path from Prototype
Review the existing references/prototype/index.html implementation and:
1. Identify which components match this specification
2. Note deviations requiring updates
3. Plan phased implementation to maintain functionality
4. Ensure all new components follow this specification exactly

## Future Extensibility
- Design system approach for easy addition of new components
- Consistent API patterns (props, events, styling hooks)
- Theming capability through CSS variables
- Performance budgets maintained with additions
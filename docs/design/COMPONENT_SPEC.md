# Sunlit Shore Component Specification

## Overview

This document specifies the visual and interaction design for all UI components in the Sunlit Shore project, based on the approved DESIGN_SPEC.md and architectural guidelines.

## Design Principles

Following the principles from DESIGN_SPEC.md:
- Playful Brutalism × Stylized Tropical Shore aesthetic
- Code-first artwork (CSS/SVG/canvas)
- Performance-conscious implementations
- Accessibility-first approach (WCAG 2.1 AA)
- Minimal necessary interactions

## Component Categories

### 1. Navigation Components

#### Primary Navigation
- **Purpose**: Global site navigation between the six regions
- **Location**: Fixed or persistent based on viewport
- **Design**: 
  - Text labels only (no icons) using Courier New
  - Horizontal arrangement on desktop, vertical collapse on mobile
  - Active state indicator: Underline or background tint
  - Hover/focus states: Subtle color shift or outline
- **States**: Default, hover, focus, active/current, disabled

#### Section Navigation (Mini-map/Waypoints)
- **Purpose**: Visual indication of current location in spatial world
- **Design**:
  - Small circular indicators connected by lines
  - Current waypoint highlighted
  - Hover/tooltip showing section name
  - Click to navigate to section

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

### 5. Spatial Components

#### Spatial Canvas Container
- **Purpose**: Houses the navigable 2D world
- **Design**:
  - Fixed positioning or constrained to viewport
  - Overflow: hidden to prevent scrollbars
  - Background: Gradient or solid water color
  - Transform origin: Center for predictable scaling/panning
  - Event handling: Capture pointer events for wake generation

#### Ocean/Water Layer
- **Purpose**: Visual water base for the spatial canvas
- **Design**:
  - CSS gradient or animated texture
  - Base color: Ocean (#00BCCD)
  - Shallow water transition: Shallow (#75E3DF) near shores
  - Optional: SVG coastal paths for sand/foam
  - Performance: Limited repaints, CSS-only where possible

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

### 6. Layout & Structural Components

#### Bento Grid (Project Archive alternative view)
- **Purpose**: Alternative project display with varying sizes
- **Design**:
  - Asymmetric grid layout
  - Varied card sizes (1x1, 2x1, 1x2, 2x2 units)
  - Consistent spacing between items
  - Responsive rearrangement at breakpoints
  - Accessible navigation and focus order

#### Section Containers
- **Purpose**: Wrapper for each of the six main regions
- **Design**:
  - Clear visual separation (generous spacing: 120-220px desktop)
  - Distinct background treatments per section
  - Consistent inner padding/margins
  - Responsive behavior: stack vertically on mobile
  - Anchors for waypoint navigation

#### Explore Tools Panel
- **Purpose**: Housing experimental interaction tools
- **Design** (referencing existing prototype):
  - Collapsible/expandable panel
  - Icon-only buttons with tooltips (accessible)
  - Consistent styling with other UI elements
  - Positioned for easy access without obstruction

### 7. Feedback & Status Components

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

### Performance Considerations
- **Render Frequency**: Limit expensive operations (especially water wake)
- **Asset Size**: Optimize images, inline critical SVG/CSS
- **JavaScript**: Minimize main thread work, use requestAnimationFrame
- **Layout**: Avoid forced synchronous layouts
- **Memory**: Clean up event listeners, observers, timeouts

### Code-First Artwork Rules
- **No External Images**: All visuals created via CSS/SVG/canvas
- **Exceptions**: Actual project screenshots (content, not UI)
- **Procedural Generation**: Where possible, use code to generate patterns
- **SVG**: For scalable vector graphics (icons, shapes, paths)
- **Canvas**: Only where necessary (water wake implementation)
- **CSS**: For shapes, gradients, positioning, transitions

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
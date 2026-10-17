# Sunlit Shore Spatial Composition

## Overview

This document specifies the spatial composition and world design for the Sunlit Shore project's navigable 2D canvas, based on the approved DESIGN_SPEC.md, SPATIAL_MAP.svg, and architectural guidelines.

## Spatial World Foundation

Based on DESIGN_SPEC.md:
- **Desktop world**: 2500×2300 logical px (not infinite)
- **Viewport**: Reveals a portion of this world
- **World nature**: Transformable HTML/CSS/SVG DOM stage (not bitmap canvas)
- **Camera movement**: Uses `translate3d` and `scale`
- **Camera clamping**: Prevents unbounded drifting into empty space
- **World route**: Hero → Selected Work → Playground → Archive → About → Contact
- **Pan vs scroll distinction**: 
  - Desktop: drag blank canvas to pan; wheel navigates waypoints; trackpad horizontal input or Shift+wheel pans sideways
  - Mobile: standard vertical content order (no global free pan)

## World Geometry and Coordinates

The spatial world uses a 2D coordinate system where:
- Origin (0,0) is at the top-left of the world space
- X increases to the right
- Y increases downward
- All positions and dimensions are in logical pixels

### Section Positions and Dimensions

From DESIGN_SPEC.md Table (Section 2):

| Region | World x,y origin | Approximate box | Primary activity |
|--------|------------------|-----------------|------------------|
| Ocean Hero | 155,235 | 1030×555 | Intro, water wake |
| Selected Work | 1425,177 | 900×650 | Featured postcard projects |
| Playground | 220,1005 | 980×690 | Local drag and bento modules |
| Project Archive | 1470,1040 | 820×650 | Grid/list browsing |
| About | 180,1800 | 1050×420 | Editorial profile & skills |
| Contact | 1480,1765 | 860×435 | Links and close |

### Spatial Relationships

#### World Route Progression
The intended exploratory path follows:
1. **Ocean Hero** (155,235) - Introduction and water interaction
2. **Selected Work** (1425,177) - Featured projects display
3. **Playground** (220,1005) - Interactive experimentation area
4. **Project Archive** (1470,1040) - Systematic project browsing
5. **About** (180,1800) - Personal/professional information
6. **Contact** (1480,1765) - Closing and connection methods

This creates a zig-zag pattern across the world space that encourages discovery.

#### Relative Positioning
- **Hero to Selected Work**: Move right and up (1270px right, -58px up)
- **Selected Work to Playground**: Move left and down (-1205px right, 828px down)
- **Playground to Archive**: Move right and up (-250px right, -35px down)
- **Archive to About**: Move left and down (-1290px right, 756px down)
- **About to Contact**: Move right and down (130px right, -35px down)

#### Visual Flow Considerations
- The route avoids straight lines, creating visual interest
- Major direction changes encourage users to reorient
- Distances are substantial enough to feel like journeying
- No section is too close to cause accidental overlap confusion

## Camera System Specifications

### Viewport Transformation
The camera transforms the world space to viewport space using:
- **Translation**: `translate3d(x, y, 0)` for panning
- **Scale**: `scale(z)` for zooming
- **Combined**: `translate3d(x, y, 0) scale(z)` applied to world container

### Constraints and Clamping
To prevent drifting into empty space:
- **X bounds**: Minimum and maximum values based on world width and viewport width
- **Y bounds**: Minimum and maximum values based on world height and viewport height
- **Implementation**: `clamp(cameraX, minX, maxX)` and `clamp(cameraY, minY, maxY)`
- **Padding**: Optional edge padding to prevent sections from touching viewport edges

### Navigation Methods

#### 1. Free Panning (Desktop)
- **Activation**: Click and drag on empty canvas (water areas)
- **Constraints**: 
  - Only works when not interacting with UI elements
  - Disabled during active water wake generation
  - Completely disabled on mobile devices
- **Feedback**: 
  - Cursor may change to indicate pan ability
  - Optional: subtle grid or hint when panning available
  - Performance: throttled to prevent excessive updates

#### 2. Waypoint Navigation (Wheel/Click)
- **Activation**: 
  - Mouse wheel (defaults to waypoint progression)
  - Click on mini-map/waypoint indicators
  - Trackpad horizontal input or Shift+wheel for sideways panning
- **Behavior**:
  - Wheel: progresses to next/previous waypoint in route order
  - Mini-map click: jumps directly to selected section
  - Animation: smooth transition per MOTION_SPEC.md (≈620ms)
- **Accessibility**: 
  - Keyboard equivalents (arrow keys for waypoint navigation)
  - Screen reader labels for waypoint indicators

#### 3. Programmatic Navigation
- **Section Links**: Anchor links or JS functions for direct navigation
- **Return Home**: Possible button to return to Ocean Hero
- **Progress Tracking**: Visual indication of progress through route

## Section Boundary Definitions

While the world is continuous, sections need clear visual and functional boundaries for usability.

### Visual Boundary Techniques
1. **Spacing**: Generous gaps between sections (120-220px as per SPEC.md)
2. **Background Shift**: Subtle color or texture transition at boundaries
3. **Elevation**: Section base at slightly different "height" (visual, not functional)
4. **Framing**: Subtle outline or shadow to define section area
5. **Gradient Edges**: Fade between section background types

### Functional Boundary Considerations
- **Interaction Priority**: 
  - In Playground: local drag takes priority over world pan
  - In forms/controls: element interaction takes precedence
  - In water areas: wake generation takes priority when active
- **Event Handling**: 
  - Proper event bubbling and capture
  - Prevention of conflicting interactions (pan vs drag)
  - Clear hit-testing rules for overlapping areas
- **Performance**: 
  - Sections outside viewport may simplify rendering
  - Distant sections reduce wake complexity
  - Caching of static section properties

## Water System Integration

The ocean/water system spans the world and connects all sections.

### Base Water Layer
- **Coverage**: Entire world space or defined ocean area
- **Appearance**: 
  - Base color: Ocean (#00BCCD)
  - Gradient possibility: deeper colors at edges
  - Shallow transition: where water meets "shore" at section boundaries
- **Performance**: 
  - CSS gradient where possible
  - Minimal repaints
  - Limited to visible viewport plus buffer

### Shoreline and Land Areas
- **Sand Regions**: 
  - Defined per section where appropriate (Hero bottom, Selected Work base, etc.)
  - Color: Sand (#FFF0CB) transitioning to Foam (#FFFDF4)
  - Texture: subtle noise or pattern via CSS
  - Edge: meeting water with foam/transition effects
- **Foam Elements**: 
  - Generated at water-sand interfaces
  - Animated or static based on performance
  - Color: Foam (#FFFDF4) with possible animation
- **Coordinate Alignment**: 
  - Water boundaries should align with section positions where relevant
  - Consistent "shore level" across connected water areas

### Wake System Boundaries
- **Activation Area**: 
  - Primarily water areas (defined by Ocean/Shallow colors)
  - Possibly extends slightly onto sand for realism
  - Disabled over UI elements and controls
  - May be confined to viewport plus margin for performance
- **Behavior at Edges**: 
  - Wake dissipates naturally at section boundaries
  - No artificial bouncing or reflection
  - Performance culling when wake moves far from viewport
- **Section-Specific Variations**: 
  - Hero: full wake implementation (signature feature)
  - Other sections: possibly limited or modified wake
  - Playground: may interact with local drag systems
  - Archive: wake may be subdued to maintain readability

## Implementation from Reference Materials

### From SPATIAL_MAP.svg
Review the SVG to:
1. Verify exact positioning matches specifications
2. Confirm section relative sizes and arrangement
3. Use as reference for implementation coordinates
4. Note any additional landmarks or routing hints

### From references/prototype/index.html
Review the existing implementation to:
1. Determine current spatial realization
2. Compare against specification coordinates and behavior
3. Plan evolution toward full specification compliance
4. Maintain backward compatibility during transition
5. Ensure camera clamping and navigation methods work correctly

## Performance Considerations

### Rendering Optimization
- **Viewport Culling**: Only render sections near viewport
- **Level of Detail**: Distant sections use simplified representations
- **Frame Budget**: Spatial updates should fit within animation frame (~16ms)
- **Paint Minimization**: Use transform/opacity for movement, avoid layout changes
- **Layer Separation**: 
  - Static world background
  - Section content layers
  - UI overlays (navigation, controls)
  - Wake and transient effects

### Memory Management
- **Section Data**: Load/unload or activate/deactivate based on distance
- **Asset Caching**: Cache images, SVG, and generated assets
- **Event Listeners**: Proper cleanup when sections deactivate
- **Animation Frameworks**: Efficient use of requestAnimationFrame

### Camera System Efficiency
- **Transform Updates**: Batch position/scale changes
- **Bounds Checking**: Efficient clipping algorithms
- **Hit Testing**: Spatial partitioning for interaction detection
- **Zoom Limits**: Reasonable min/max scale to prevent excessive detail

## Accessibility in Spatial Design

### Navigation Accessibility
- **Keyboard**: 
  - Waypoint navigation via arrow keys or custom shortcuts
  - Sequential access to all sections
  - Clear focus indicators when navigating
- **Screen Reader**: 
  - Landmark roles for major sections
  - Clear labels for navigational elements
  - Announcements of section transitions
  - Description of spatial relationships when useful
- **Focus Order**: 
  - Logical sequence following spatial or reading order
  - No trapping in any section or component
  - Escape mechanisms for all interactive states

### Reduced Motion Considerations
- **Camera Movement**: 
  - Option to disable smooth transitions
  - Instant section jumping when preferred
  - Maintain spatial awareness without animation
- **Wake Effect**: 
  - Disabled completely when prefers-reduced-motion is active
  - No substitution needed for core functionality
- **Transitions**: 
  - Section entrances may be instant or greatly reduced
  - Content remains accessible and usable

### Visual Accessibility
- **Color Coding**: 
  - Never rely on color alone to distinguish sections
  - Use patterns, icons, or text labels in addition
- **Contrast**: 
  - Section boundaries meet WCAG AA contrast ratios
  - Interactive elements clearly distinguishable
  - Text on section backgrounds readable
- **Spatial Clarity**: 
  - Avoid overly complex arrangements that cause confusion
  - Maintain identifiable landmarks for orientation
  - Consider providing mini-map or overview for orientation

## Responsive Spatial Behavior

### Desktop (≥ 800px)
- Full spatial canvas implementation
- Exact world coordinates as specified
- Global panning and waypoint navigation active
- Directional water wake fully implemented
- Camera clamping to prevent drifting
- All six sections accessible via spatial navigation

### Mobile (< 800px)
- Standard vertical scrolling layout
- Sections stacked in world route order
- No global canvas panning (standard page scroll)
- Local water interaction: 
  - Possibly: section-specific water areas
  - Possibly: limited interaction zones
  - Performance-optimized for mobile
- Spatial coordinates transformed to vertical flow:
  - Hero → top of page
  - Selected Work → next section
  - Playground → following
  - etc.
- Section heights: content-driven with minimums for usability
- Water wake: localized or simplified implementations

### Transition Between Modes
- **Breakpoint**: 800px as specified in DESIGN_SPEC.md
- **Transformation**: 
  - At 800px: switch from spatial to vertical layout
  - Below 800px: vertical layout with standard scroll
  - Above 800px: spatial canvas with panning/waypoints
- **State Preservation**: 
  - Scroll position maintained when possible
  - Interactive states preserved across transition
  - No loss of data or user progress
- **Animation**: 
  - Optional crossfade or transition between layouts
  - Instant switch acceptable for performance
  - Never animate layout change during interaction

## Implementation Guidelines

### Coordinate System
- **Units**: Logical pixels matching specifications exactly
- **Origin**: Top-left of world space (0,0)
- **Precision**: Integer coordinates sufficient for layout
- **Storage**: Store section positions as constants or configuration

### Section Definition
Each section should define:
- **World Position**: x, y coordinates (top-left corner)
- **Dimensions**: width, height in logical pixels
- **Content**: Internal layout and components
- **Boundaries**: Interaction and visual boundary definitions
- **Navigation**: Waypoint identifiers and connections

### Camera Implementation
```javascript
// Camera state
let camera = {
  x: 0,      // world x position
  y: 0,      // world y position
  scale: 1,  // zoom level
};

// Target world size (from spec)
const WORLD_WIDTH = 2500;
const WORLD_HEIGHT = 2300;

// Viewport size (updated on resize)
let viewportWidth = window.innerWidth;
let viewportHeight = window.innerHeight;

// Clamping function
function clampCamera() {
  const maxX = Math.max(0, WORLD_WIDTH - viewportWidth / camera.scale);
  const maxY = Math.max(0, WORLD_HEIGHT - viewportHeight / camera.scale);
  
  camera.x = Math.max(0, Math.min(camera.x, maxX));
  camera.y = Math.max(0, Math.min(camera.y, maxY));
}

// Apply transformation
function applyCameraTransform() {
  return `translate3d(${camera.x}px, ${camera.y}px, 0) scale(${camera.scale})`;
}

// Update on resize
function onViewportResize() {
  viewportWidth = window.innerWidth;
  viewportHeight = window.innerHeight;
  clampCamera(); // Ensure camera still in bounds after resize
}
```

### Waypoint System
- **Definitions**: 
  - Each section has a waypoint at its center or entrance
  - Waypoints ordered according to world route
  - Optional: visual indicators for waypoints
- **Navigation**: 
  - Wheel increments/decrements waypoint index
  - Click jumps to specific waypoint
  - Animation follows MOTION_SPEC.md timing
- **API**: 
  - `goToWaypoint(index)` 
  - `goToNextWaypoint()`
  - `goToPreviousWaypoint()`
  - `getCurrentWaypoint()`

## Testing and Verification

### Spatial Accuracy Tests
- **Coordinate Verification**: 
  - Sections appear at specified world positions
  - Dimensions match approximate box specifications
  - Route follows defined sequence
- **Camera Behavior**: 
  - Clamping prevents drift beyond world bounds
  - Smooth transitions between sections
  - Correct response to panning and wheel input
- **Boundary Detection**: 
  - Sections maintain proper separation
  - Intersection behavior matches expectations
  - No unintended overlapping or gaps

### Interaction Tests
- **Panning**: 
  - Works on empty canvas areas
  - Disabled over UI controls
  - Suppressed during active wake
  - Proper touch vs mouse distinction
- **Waypoint Navigation**: 
  - Wheel progresses in correct order
  - Click jumps to selected section
  - Animation timing matches specification
  - Accessible via keyboard alternatives
- **Wake Interaction**: 
  - Responds correctly to cursor movement
  - Behavior table implemented exactly
  - Performance remains acceptable
  - Disabled appropriately

### Responsive Tests
- **Breakpoint**: 
  - Layout changes correctly at 800px
  - Mobile: vertical scrolling order maintained
  - Desktop: spatial navigation restored above breakpoint
- **Content Preservation**: 
  - No loss of information when switching modes
  - Interactive states maintained where appropriate
  - Water interaction adapted appropriately
- **Performance**: 
  - Maintains target frame rates in both modes
  - Memory usage stable across transitions
  - No layout thrashing during resize

## Future Considerations

### Enhanced Spatial Features
- **Dynamic World**: Procedural generation or adaptive layouts
- **Multiple Routes**: Alternative paths through the world space
- **Points of Interest**: Discoverable elements beyond main sections
- **Environmental Storytelling**: World details that reveal information
- **User-Generated Content**: Ability to add personal landmarks or notes

### Navigation Improvements
- **Continuous Navigation**: Options for smooth, uninterrupted travel
- **Speed Control**: Modifiers for faster/slower movement
- **Orientation Aids**: Compass, minimap, or breadcrumb navigation
- **Search**: Ability to jump to specific content by name or tag
- **History**: Back/forward navigation through visited sections

### World Persistence
- **Saved Views**: Ability to bookmark favorite positions
- **Shareable Links**: Direct links to specific world coordinates
- **Offline Functionality**: Core spatial experience available offline
- **Multi-User Awareness**: Subtle indications of others' explorations
- **Analytics**: Tracking popular paths through the world space

### Technical Evolution
- **WebGPU/Canvas2D**: For advanced water or particle effects
- **Worklets**: For high-performance paint/layout work
- **WebAssembly**: For computationally intensive spatial operations
- **Server-Side Rendering**: For initial world state delivery
- **Progressive Loading**: Load distant sections on demand

This spatial composition specification completes the foundational documentation for implementing the Sunlit Shore project's navigable 2D world, ensuring alignment with all approved design decisions and technical requirements.
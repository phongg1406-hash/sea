# Sunlit Shore Section Layouts

## Overview

This document specifies the layout and composition for each of the six main regions in the Sunlit Shore spatial canvas, based on the approved DESIGN_SPEC.md, SPATIAL_MAP.md, and architectural guidelines.

## Spatial Canvas Foundation

Based on DESIGN_SPEC.md:
- Desktop world: 2500×2300 logical px (not infinite)
- Viewport reveals portion of this world
- World is transformable HTML/CSS/SVG DOM stage (not bitmap canvas)
- Camera moves with translate3d and scale
- Camera translation clamped to prevent unbounded drifting
- World route: Hero → Selected Work → Playground → Archive → About → Contact
- Pan vs scroll: Desktop drag blank canvas to pan; wheel navigates waypoints; mobile uses vertical reading order

## Section Specifications

### 1. Ocean Hero
- **World Position**: 155,235
- **Approximate Box**: 1030×555
- **Primary Activity**: Introduction, water wake demonstration

#### Layout Composition
- **Fixed Elements**: 
  - Hero headline (site title or personal name)
  - Supporting tagline/description
  - Primary call-to-action (explore/projects)
- **Interactive Elements**:
  - Directional water wake responsive to cursor movement
  - Subtle floating/animated decorative elements (stars, etc.)
- **Background Treatment**:
  - Ocean base (#00BCCD) with possible gradient variation
  - Shallow water transition where meeting "shore"
  - SVG coastal sand and foam paths at bottom
  - Optional CSS-generated caustic-like line texture
- **Visual Hierarchy**:
  - Dominant: Site identification (large headline)
  - Secondary: Water interaction demonstration
  - Tertiary: Navigation cues to other sections
- **Responsive Behavior**:
  - Mobile: Stacked vertical layout with reduced water wake interaction
  - Tablet: Adaptive spacing and sizing
  - Desktop: Full spatial positioning as specified

#### Content Guidelines
- Headline: Personal name or site title (large display type)
- Subheadline: Brief descriptor or tagline
- CTA: Clear invitation to explore work ("View Projects", "See Work")
- Secondary links: Subtle navigation to About or Contact

### 2. Shoreline Transition
- **World Position**: Between Hero and Selected Work (approximately)
- **Purpose**: Visual and spatial transition from introduction to work
- **Note**: Not explicitly listed in WORLD ROUTE but implied by spatial positioning

#### Layout Composition
- **Visual Treatment**:
  - Gradient transition from water to sand
  - Animated shoreline elements (gentle wave motion)
  - Sand texture or pattern near "shoreline"
  - Foam and water edge effects
- **Spatial Function**:
  - Creates sense of moving from deep water to shallower area
  - Visual cue that we're approaching the "shore" where work begins
  - May include subtle interactive elements responding to proximity
- **Dimensions**: Variable based on positioning between sections

### 3. Selected Work
- **World Position**: 1425,177
- **Approximate Box**: 900×650
- **Primary Activity**: Featured postcard projects

#### Layout Composition
- **Primary Display**: 
  - 3-5 featured project postcards
  - Arranged with playful rotation and slight overlap
  - Each postcard: beach postcard visual with lift-on-hover
- **Secondary Elements**:
  - Section heading ("Selected Work" or similar)
  - Subtle decorative elements (small icons, markers)
  - Navigation indicators to adjacent sections
- **Background Treatment**:
  - Sand base (#FFF0CB) or Foam (#FFFDF4)
  - Subtle texture or pattern to suggest beach material
  - Optional: distant ocean/water visible at edges
- **Visual Hierarchy**:
  - Dominant: Featured project postcards
  - Secondary: Section identification
  - Tertiary: Spatial navigation cues
- **Interaction Model**:
  - Postcards: hover lift, click to open detail dialog
  - Possible: drag to rearrange (if implementing customization)
  - Section-level: visual response to nearby cursor wake

#### Content Guidelines
- Section heading: Clear label for this area
- Postcards: Each showing a different featured project
- Postcard content: Project thumbnail, title, optional badges/tags
- Spacing: Generous between postcards for hover lift effect

### 4. Playground
- **World Position**: 220,1005
- **Approximate Box**: 980×690
- **Primary Activity**: Local drag and bento modules

#### Layout Composition
- **Primary Display**:
  - Bento grid layout (asymmetric card arrangements)
  - Draggable objects/elements for interaction
  - Reset button to return to initial state
- **Secondary Elements**:
  - Section heading ("Playground" or similar)
  - Instructional cues for interaction
  - Visual separation from adjacent sections
- **Background Treatment**:
  - Sand base with possible variation
  - Subtle texture suggesting beach or playground surface
  - Boundary markers or low "fencing" to define play area
- **Visual Hierarchy**:
  - Dominant: Interactive bento modules and draggables
  - Secondary: Section identification and instructions
  - Tertiary: Boundary definition and spatial context
- **Interaction Model**:
  - Draggable elements: follow pointer with appropriate feedback
  - Bento modules: static display or simple hover effects
  - Reset: returns all elements to starting positions
  - Boundaries: soft stop at edges, not hard blocking

#### Content Guidelines
- Section heading: Clear label encouraging interaction
- Draggable objects: Simple shapes or representations related to work
- Bento modules: Project details, skills displays, or interesting tidbits
- Instructions: Minimal, intuitive interaction cues ("Drag to play", "Reset to start")

### 5. Project Archive
- **World Position**: 1470,1040
- **Approximate Box**: 820×650
- **Primary Activity**: Grid/list browsing

#### Layout Composition
- **Primary Display**:
  - Project cards in grid or list formation
  - Toggle between Grid and List views (aria-pressed button)
  - Consistent card spacing and alignment
- **Secondary Elements**:
  - Section heading ("Project Archive" or similar)
  - Sorting/filtering controls (if implemented)
  - Item counter showing total/shown projects
- **Background Treatment**:
  - Foam base (#FFFDF4) for clean, readable surface
  - Subtle texture or pattern to prevent visual flatness
  - Optional: faint grid or guide lines for alignment
- **Visual Hierarchy**:
  - Dominant: Project browsing interface
  - Secondary: Section identification and controls
  - Tertiary: Spatial context and navigation cues
- **Interaction Model**:
  - Grid view: Cards arranged in rows and columns
  - List view: Vertical stack with detailed metadata
  - Toggle: smooth transition between views
  - Card interaction: hover/focus states, click to open detail
  - Selection: visual indication of chosen item(s)

#### Content Guidelines
- Section heading: Clear label for browsing area
- Project cards: Consistent design showing essential metadata
- Card content: Title, type/tags, year, status indicator
- Controls: Clearly labeled toggle, accessible sorting/filtering
- Empty state: Helpful message when no projects to show

### 6. About
- **World Position**: 180,1800
- **Approximate Box**: 1050×420
- **Primary Activity**: Editorial profile & skills

#### Layout Composition
- **Primary Display**:
  - Editorial-style biography section
  - Skills or expertise visualization
  - Personal/professional details
- **Secondary Elements**:
  - Section heading ("About" or similar)
  - Professional portrait or avatar (if desired)
  - Contact information or social links
- **Background Treatment**:
  - Sand base with possible variation toward Foam
  - Subtle texture suggesting professional document or canvas
  - Optional: faint watermark or pattern
- **Visual Hierarchy**:
  - Dominant: Biographical/content information
  - Secondary: Section identification
  - Tertiary: Visual elements supporting the narrative
- **Interaction Model**:
  - Primarily readable/scannable content
  - Possible: expandable sections for detailed information
  - Links: standard hover/focus states for navigation
  - Contact: clear invocation methods (email, social media)

#### Content Guidelines
- Section heading: Clear label for biographical area
- Biography: Concise but complete professional/personal overview
- Skills: Visual grouping or categorization of abilities
- Details: Education, experience, location, etc. as appropriate
- Links: Functional contact methods with clear labels

### 7. Contact
- **World Position**: 1480,1765
- **Approximate Box**: 860×435
- **Primary Activity**: Links and close

#### Layout Composition
- **Primary Display**:
  - Contact information and methods
  - Social media/profile links
  - Closing message or thank you
- **Secondary Elements**:
  - Section heading ("Contact" or similar)
  - Visual closing element or signature
  - Spatial boundary indicator (edge of explorable world)
- **Background Treatment**:
  - Sand or Foam base
  - Subtle gradient or variation suggesting "endpoint"
  - Optional: symbolic elements (setting sun, etc.)
- **Visual Hierarchy**:
  - Dominant: Contact information and invitation
  - Secondary: Section identification
  - Tertiary: Closure and boundary indication
- **Interaction Model**:
  - Links: standard hover/focus states, clear activation
  - Forms: if implemented, proper validation and feedback
  - Closing: sense of completion, not abrupt termination
  - Boundaries: visual cue that this is the end of the journey

#### Content Guidelines
- Section heading: Clear label for contact area
- Contact methods: Email, social profiles, professional networks
- Message: Brief thank you or closing statement
- Links: Functional and clearly labeled
- Boundary: Visual indication that world continues but exploration ends here

## Layout Implementation Guidelines

### Spatial Positioning
- **Coordinate System**: Use exact world positions from SPEC.md
- **Bounding Boxes**: Respect approximate box dimensions as guides
- **Clamping**: Implement camera position clamping to prevent drift
- **Waypoints**: Use section centers as navigation targets
- **Routing**: Follow specified world route for progressive disclosure

### Responsive Behavior
- **Mobile (< 800px)**: 
  - Convert to standard vertical scrolling order
  - Stack sections vertically in logical sequence
  - Disable global canvas panning
  - Maintain local water interaction where appropriate
  - Adjust spacing and sizing for thumb reach
- **Tablet (800px-1200px)**:
  - Adaptive layout between spatial and vertical
  - Consider horizontal scrolling or modified panning
  - Scale spatial world appropriately
- **Desktop (> 1200px)**:
  - Full spatial canvas implementation
  - Exact positioning as specified
  - Global panning and waypoint navigation

### Visual Separation
- **Between Sections**: 
  - Generous spacing (120-220px desktop as per SPEC.md)
  - Visual gradient or transition between zone types
  - Optional: subtle boundary markers or landmarks
  - Consistent treatment regardless of actual distance
- **Within Sections**:
  - Appropriate padding and margins for content
  - Clear visual hierarchy and grouping
  - Responsive adjustment of internal spacing

### Performance Considerations
- **Render Distance**: Consider culling or simplifying distant sections
- **Level of Detail**: Reduce complexity for off-screen sections
- **Cache Properties**: Minimize recalculation of static layouts
- **Transform Efficiency**: Use translate3d for GPU acceleration
- **Bounds Checking**: Efficient clamping implementation

### Accessibility in Layout
- **Keyboard Navigation**: Logical tab order following spatial or reading sequence
- **Focus Management**: Clear indication when moving between sections
- **Screen Reader**: Proper landmarks and labeling for navigation
- **Reduce Motion**: Option to disable parallax or transition effects
- **Touch Targets**: Maintain minimums even in spatial layout

## Implementation from Prototype

Review the existing references/prototype/index.html to:
1. Map current implementation to these specifications
2. Identify which sections closely match the spec
3. Note areas requiring adjustment or redesign
4. Plan implementation that maintains backward compatibility where possible
5. Ensure all new layouts follow spatial positioning exactly

## Future Considerations

- **Dynamic World**: Potential for procedurally generated or adaptive world
- **Multiple Routes**: Alternative paths through the spatial world
- **Seasonal Variations**: Layout or visual changes based on time/date
- **User Customization**: Ability to rearrange or personalize layout
- **Analytics Integration**: Tracking popular paths through the world
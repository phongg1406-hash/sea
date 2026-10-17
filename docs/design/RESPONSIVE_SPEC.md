# Sunlit Shore Responsive Specification

## Overview

This document specifies the responsive behavior and breakpoints for the Sunlit Shore project, based on the approved DESIGN_SPEC.md, AI_HANDOFF.md, and architectural guidelines.

## Responsive Philosophy

Following the principles from DESIGN_SPEC.md:
- **At ≤800px**: One-column vertical reading order, standard page scroll, no global free pan
- **Mobile is intentionally standard vertical reading flow**: Don't hijack touch scroll
- **The shore is still visually represented**: With a local interactive water surface
- **Text and links remain DOM-based**
- **Core project links never require drag/hover**
- **Navigation menu uses real buttons, dialog uses native `<dialog>`**
- **Desktop spatial map uses buttons**

Following principles from design-taste-frontend skill:
- Mobile-first approach: design for smallest screen first, then enhance
- Viewport meta tag: width=device-width initial-scale=1 (never disable zoom)
- Readable font sizes: minimum 16px body text on mobile
- Touch targets: minimum 44x44px with 8px+ spacing
- Content priority: show core content first on mobile
- No horizontal scroll on mobile: ensure content fits viewport width

## Breakpoint System

Based on the 800px threshold specified in DESIGN_SPEC.md and common device widths:

### Primary Breakpoint
- **Mobile**: < 800px
  - Vertical scrolling layout
  - Standard page scroll behavior
  - Local water interaction only
  - No global canvas panning

- **Desktop**: ≥ 800px
  - Spatial canvas with 2D world navigation
  - Global panning and waypoint navigation
  - Full directional water wake
  - Complex layout arrangements

### Secondary Breakpoints (for refinement)
- **Small Mobile**: < 480px
  - Most constrained layout
  - Touch optimization critical
  - Single column with minimal complexity

- **Standard Mobile**: 480px - 799px
  - Enhanced mobile layout
  - More complex components possible
  - Better use of available width

- **Compact Desktop**: 800px - 1023px
  - Desktop layout activated
  - May need adjustments for narrower screens
  - Touch still possible but secondary

- **Standard Desktop**: 1024px - 1399px
  - Full desktop experience
  - Optimal for spatial canvas
  - Primary design target

- **Wide Desktop**: ≥ 1400px
  - Additional horizontal space
  - Potential for expanded layouts
  - Consider multi-panel or enhanced features

## Layout Transformation Rules

### From Spatial to Vertical (Desktop → Mobile)

#### Section Order
When converting from spatial layout to vertical stack at ≤800px, sections should follow this order:
1. Ocean Hero (Introduction)
2. Shoreline Transition (if implemented as separate section)
3. Selected Work (Featured Projects)
4. Playground (Interactive Area)
5. Project Archive (Browsing)
6. About (Profile/Skills)
7. Contact (Footer/Closing)

This maintains the spatial world route as a vertical journey.

#### Spatial Properties Conversion
- **Position**: World coordinates (x,y) become irrelevant; sections stack vertically
- **Size**: World dimensions (width,height) become viewport-constrained with vertical scrolling
- **Transform**: translate3d/scale becomes standard document flow
- **Clamping**: Removed (no bounds needed in vertical layout)
- **Panning**: Disabled (standard scroll takes over)
- **Waypoint Navigation**: Converted to anchor links or progressive disclosure

#### Water System
- **Global Water Wake**: Replaced with local water interaction
- **Scope**: Limited to visible viewport or section-specific area
- **Performance**: Reduced complexity for mobile performance
- **Visual**: Still present but contained to appropriate areas

### Layout Preservation Principles

#### Visual Identity Maintenance
- **Color System**: Unchanged across breakpoints
- **Typography**: Scaled appropriately but same typefaces
- **Component Styles**: Consistent shapes, radii, borders
- **Iconography**: Same SVG icons where used
- **Interaction Patterns**: Similar feedback, adjusted for touch

#### Content Priority
- **Essential First**: Core identity and navigation always visible
- **Progressive Disclosure**: Secondary content available but not overwhelming
- **Touch Optimization**: Controls enlarged and spaced appropriately
- **Thumb Zones**: Important controls placed in easy-to-reach areas

## Component-Specific Responsive Behavior

### Navigation
- **Desktop (≥ 800px)**:
  - Spatial navigation: panning, waypoints, mini-map
  - Persistent or fixed positioning based on design
  - Hover-based interaction for desktop precision
  
- **Mobile (< 800px)**:
  - Standard navigation: fixed/top or bottom positioned
  - Button-based navigation (real `<button>` elements)
  - Clear labels, touch-optimized targets
  - Hamburger menu or tab bar if many items
  - No reliance on hover

### Project Postcards (Featured Work)
- **Desktop**:
  - Spatial placement within Selected Work section
  - Playful rotation and lift-on-hover
  - Possible overlap and arrangement
  
- **Mobile**:
  - Vertical stack or horizontal scroll (if many)
  - Reduced or no rotation (can interfere with reading)
  - Lift may become scale or opacity change
  - Full width or constrained to comfortable width
  - Vertical spacing optimized for touch

### Archive Cards
- **Desktop**:
  - Grid layout within Project Archive section
  - Possible hover previews or expansions
  - Arrange based on available width
  
- **Mobile**:
  - Single column list or 2-column grid (if wide enough)
  - Stacked vertical presentation
  - Simplified metadata display
  - Touch-optimized hit areas

### Forms and Inputs
- **Both**:
  - Minimum 44px height for touch targets
  - Clear labels and placeholder text
  - Validated input types (email, tel, etc.)
  
- **Desktop**:
  - Possible side-by-side layout for related fields
  - Hover-based help or validation
  
- **Mobile**:
  - Stacked vertical form fields
  - Full-width inputs where appropriate
  - Native keyboard optimization (email, number, etc.)

### Dialogs and Overlays
- **Desktop**:
  - Centered modal dialogs
  - Possible larger dimensions
  - Outside-click to close (with confirmation if needed)
  
- **Mobile**:
  - Top-aligned or bottom-aligned (safer for reach)
  - Full-width or near-full-width
  - Swipe-to-dismiss options (with confirmation)
  - Outside-click behavior considered carefully

### Water Interaction
- **Desktop (≥ 800px)**:
  - Global directional water wake across spatial canvas
  - Full implementation per MOTION_SPEC.md
  - Responsive to canvas movements and panning
  
- **Mobile (< 800px)**:
  - Local water interaction: limited to visible area or section
  - Possibly: 
    - Small interactive pond at bottom of screen
    - Section-specific water areas
    - Touch-driven ripples instead of cursor wake
  - Simplified physics for performance
  - Wake disabled during scroll (preserve native behavior)

## Implementation Guidelines

### CSS Approach
- **Mobile-First**: Write base styles for mobile, then enhance with min-width queries
- **Breakpoint Naming**: Use descriptive names rather than just numbers
- **Viewport Units**: Use vw, vh, vmin, vmax appropriately for spatial elements
- **Pixel Values**: Use px for fixed values like borders, but prefer relative for typography/spacing
- **Flexbox/Grid**: Use for layout adaptation rather than absolute positioning where possible

```css
/* Mobile-first base */
.section {
  padding: 1rem;
  margin-bottom: 2rem;
}

/* Tablet and up */
@media (min-width: 800px) {
  .section {
    /* Spatial layout properties */
    position: absolute;
    /* ... */
  }
}

/* Desktop enhancements */
@media (min-width: 1024px) {
  .section {
    /* Enhanced spatial layout */
    /* ... */
  }
}
```

### JavaScript Approach
- **Feature Detection**: Test for touch capabilities, not just screen width
- **Event Handling**: Separate pointer vs touch vs mouse events appropriately
- **Resize Handling**: Debounce resize events for performance
- **Orientation Change**: Handle both resize and orientationchange events
- **MatchMedia**: Use window.matchMedia() for efficient breakpoint testing

```javascript
// Efficient breakpoint checking
const mediaQuery = window.matchMedia('(min-width: 800px)');

function handleBreakpointChange(e) {
  if (e.matches) {
    // Enable desktop features
    enableSpatialCanvas();
    enableGlobalWake();
    disableStandardScroll();
  } else {
    // Enable mobile features
    disableSpatialCanvas();
    disableGlobalWake();
    enableStandardScroll();
    enableLocalWaterInteraction();
  }
}

// Initial setup
handleBreakpointChange(mediaQuery);
mediaQuery.addEventListener('change', handleBreakpointChange);

// Cleanup
// mediaQuery.removeEventListener('change', handleBreakpointChange);
```

### Performance Considerations
- **Style Recalculation**: Minimize DOM reads/writes during resize
- **Layout Thrashing**: Batch DOM writes after reads
- **Image Loading**: Use responsive images (srcset/sizes) for different breakpoints
- **Resource Loading**: Conditionally load heavy assets only when needed
- **Animation Frame**: Use requestAnimationFrame for visual updates during resize

### Accessibility in Responsive Design
- **Touch Targets**: Maintain 44x44px minimum regardless of breakpoint
- **Text Scaling**: Support user-initiated text size changes (especially mobile)
- **Orientation**: Ensure usability in both portrait and landscape
- **Zoom**: Never disable user scaling (viewport meta: user-scalable=yes)
- **Focus Order**: Maintain logical sequence in both layouts
- **Hidden Content**: Ensure accessibility of content revealed at different breakpoints

## Specific Section Responsive Rules

### Ocean Hero
- **Desktop**: 
  - Positioned at world coordinates (155,235)
  - Full spatial dimensions (1030×555)
  - Global water wake active
  
- **Mobile**:
  - Full width viewport or constrained width
  - Height: content-driven with minimum viewport height
  - Local water interaction at bottom or specific area
  - Headline size reduced per DESIGN_SPEC.md (54-96px range)
  - CTA buttons full-width or touch-optimized

### Selected Work
- **Desktop**:
  - Positioned at world coordinates (1425,177)
  - Spatial dimensions (900×650)
  - Arranged postcards with possible overlap
  
- **Mobile**:
  - Full width container
  - Postcards in vertical stack or swipeable carousel
  - Consistent sizing for touch targets
  - Reduced or eliminated rotation
  - Vertical spacing for comfortable viewing

### Playground
- **Desktop**:
  - Positioned at world coordinates (220,1005)
  - Spatial dimensions (980×690)
  - Full bento grid and draggables
  
- **Mobile**:
  - Full width container
  - Stacked vertical layout of components
  - Touch-optimized drag targets
  - Possible: simplified interactions due to space
  - Reset button prominently placed

### Project Archive
- **Desktop**:
  - Positioned at world coordinates (1470,1040)
  - Spatial dimensions (820×650)
  - Grid layout with possible List toggle
  
- **Mobile**:
  - Full width container
  - Single column list view (Grid may be impractical)
  - Toggle may switch between compact and detailed views
  - Optimized for vertical scrolling

### About and Contact
- **Desktop**:
  - Positioned at their world coordinates
  - Specified approximate box dimensions
  - Spatial arrangement maintained
  
- **Mobile**:
  - Full width containers
  - Standard vertical flow
  - Content-sized height (not constrained to box dimensions)
  - Preserved readability and accessibility

## Implementation from Prototype

Review the existing prototype implementation to:
1. Determine current responsive behavior
2. Identify gaps relative to this specification
3. Plan responsive improvements that maintain core functionality
4. Ensure mobile experience follows vertical reading order exactly
5. Verify that global panning is disabled on mobile per spec

## Testing Methodology

### Device Testing
- **Physical Devices**: Test on actual iOS/Android devices when possible
- **Emulation**: Use browser dev tools for various screen sizes
- **Breakpoints**: Test at exact breakpoint values and slightly above/below
- **Orientation**: Test both portrait and landscape where applicable

### Feature Testing
- **Touch Events**: Verify proper touch target sizes and feedback
- **Mouse Events**: Ensure desktop hover/click still works
- **Keyboard**: Confirm full accessibility in both layouts
- **Screen Reader**: Validate announcements and navigation
- **Reduced Motion**: Test that core functionality works without animation

### Performance Testing
- **Frame Rate**: Maintain 60fps during interactions and scrolling
- **Memory Usage**: Watch for leaks during resize/orientation changes
- **Battery Impact**: Consider especially for mobile water interaction
- **Load Time**: Ensure responsive changes don't delay initial render

## Future Considerations

### Advanced Adaptive Behaviors
- **Dynamic Breakpoints**: Content-based rather than fixed pixel values
- **User Preferences**: Respect reduced motion, contrast, spacing settings
- **Environmental Awareness**: Adjust based on ambient light, time of day
- **Input Modalities**: Seamless transition between touch, pen, mouse, keyboard
- **Foldable/Special Screens**: Adapt to device posture and hinge states

### Progressive Enhancement
- **Core First**: Ensure basic content and navigation work everywhere
- **Enhance Capably**: Add features as device capabilities allow
- **Graceful Degradation**: Maintain usability when features unsupported
- **Feature Detection**: Never assume capabilities based on UA alone

### Analytics and Feedback
- **Usage Patterns**: Track how users navigate in each layout mode
- **Performance Metrics**: Monitor frame times and responsiveness
- **User Feedback**: Collect subjective impressions of mobile/desktop experience
- **Conversion Tracking**: Ensure core user flows work across breakpoints
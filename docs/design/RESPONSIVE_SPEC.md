# Sunlit Shore Responsive Specification

## Overview

This document specifies the responsive behavior and breakpoints for the Sunlit Shore project, based on the approved DESIGN_SPEC.md v2.0, AI_HANDOFF.md v2.0, and architectural guidelines.

## Responsive Philosophy

Following the principles from DESIGN_SPEC.md v2.0:
- **At ≤800px**: One-column vertical reading order, standard page scroll, no global free pan
- **Mobile is intentionally standard vertical reading flow**: Don't hijack touch scroll
- **The shore is still visually represented**: With a local interactive water surface
- **Text and links remain DOM-based**
- **Core project links never require drag/hover**
- **Navigation menu uses real buttons, dialog uses native `<dialog>`**
- **Geographic Shore Map uses compact expandable navigation panel**

Following principles from design-taste-frontend skill:
- Mobile-first approach: design for smallest screen first, then enhance
- Viewport meta tag: width=device-width initial-scale=1 (never disable zoom)
- Readable font sizes: minimum 16px body text on mobile
- Touch targets: minimum 44x44px with 8px+ spacing
- Content priority: show core content first on mobile
- No horizontal scroll on mobile: ensure content fits viewport width

## Breakpoint System

Based on the 800px threshold specified in DESIGN_SPEC.md v2.0 and common device widths:

### Primary Breakpoint
- **Mobile**: < 800px
  - Vertical scrolling layout
  - Standard page scroll behavior
  - Local water interaction only
  - No global canvas panning

- **Desktop**: ≥ 800px
  - Continuous Vertical Coastal Scroll with artistic Main Scene
  - Left sand / right ocean composition maintained
  - Geographic Shore Map as expandable panel
  - Full Directional Water Wake implementation
  - Floating Skill Net with 8-10 visible logos
  - Hover-based interactions where appropriate

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
  - Optimal for Continuous Vertical Coastal Scroll
  - Primary design target

- **Wide Desktop**: ≥ 1400px
  - Additional horizontal space
  - Potential for expanded layouts
  - Consider multi-panel or enhanced features

## Layout Transformation Rules

### From Spatial Canvas to Vertical Scroll (Conceptual Update)

**Note**: This project has transitioned from a spatial canvas to a Continuous Vertical Coastal Scroll. The following transformation rules are provided for conceptual understanding of the shift from the previous spatial design to the current vertical scroll layout.

#### Section Order
The eight sections follow Vietnam's coastline from north to south in vertical scroll order:
1. TRÀ CỐ / HOME (Introduction)
2. HẠ LONG / PROJECTS (Featured postcard projects)
3. LĂNG CÔ / ABOUT ME (Editorial profile & personal journal)
4. ĐÀ NẴNG / SKILLS (Bento Cards + Floating Skill Net)
5. QUY NHƠN / RESUME (Editorial Timeline + Compact Cards)
6. NHA TRANG / PLAYGROUND (Interactive Lab Cards + Coastal Decorations)
7. MŨI NÉ / PROJECT ARCHIVE (Coastal Project Library)
8. MŨI CÀ MAU / CONTACT (Open Invitation + Thank You)

This maintains the coastal journey as a vertical experience.

#### Layout Properties
- **Position**: Vertical document flow replaces world coordinates
- **Size**: Viewport-constrained with vertical scrolling
- **Transform**: Standard document flow replaces translate3d/scale
- **Clamping**: Top/bottom bounds on document scrolling
- **Panning**: Replaced with natural vertical scrolling
- **Waypoint Navigation**: Converted to anchor links and Geographic Shore Map

#### Water System
- **Global Water Wake**: Replaced with directional water wake over water areas
- **Scope**: Limited to water areas (right side of Main Scene)
- **Performance**: Canvas 2D with bounded history, downsampled resolution
- **Visual**: Present but contained to appropriate water areas

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
  - Continuous Vertical Coastal Scroll: natural vertical scrolling
  - Persistent or fixed positioning based on design
  - Hover-based interaction for desktop precision
  - Geographic Shore Map as expandable panel
  
- **Mobile (< 800px)**:
  - Standard navigation: fixed/top or bottom positioned
  - Button-based navigation (real `<button>` elements)
  - Clear labels, touch-optimized targets
  - Hamburger menu or tab bar if many items
  - No reliance on hover
  - Geographic Shore Map uses compact expandable navigation panel

### Project Postcards (Featured Work)
- **Desktop**:
  - Placement within Hạ Long/Projects section (left sand, right ocean)
  - Beach postcard visuals with subtle, deliberate rotation and lift-on-hover
  - One larger featured postcard and two supporting postcards (Approved Option C)
  - Possible overlap and arrangement (not random regeneration)
  
- **Mobile**:
  - Vertical stack or horizontal scroll (if many)
  - Reduced or no rotation (can interfere with reading)
  - Lift may become scale or opacity change
  - Full width or constrained to comfortable width
  - Vertical spacing optimized for touch

### Archive Cards
- **Desktop**:
  - Grid layout within Mũi Né/Project Archive section (left sand, right ocean)
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
  - Directional water wake over water areas (right side of Main Scene)
  - Full implementation per MOTION_SPEC.md
  - Responsive to cursor movement over water
  
- **Mobile (< 800px)**:
  - Local water interaction: limited to visible water area or section
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
- **Viewport Units**: Use vw, vh, vmin, vmax appropriately for layout elements
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
    /* Continuous Vertical Coastal Scroll layout properties */
    /* ... */
  }
}

/* Desktop enhancements */
@media (min-width: 1024px) {
  .section {
    /* Enhanced Continuous Vertical Coastal Scroll layout */
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
    enableVerticalCoastalScroll();
    enableDirectionalWake();
    enableGeographicMap();
    disableStandardScrollEnhancements();
  } else {
    // Enable mobile features
    disableVerticalCoastalScrollEnhancements();
    disableDirectionalWake();
    enableGeographicMapCompact();
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
- **Water Wake Performance**: Canvas 2D with bounded history, downsample resolution, automatic deactivation
- **Skill Net Animation**: Lightweight custom motion model, avoid physics simulation

### Accessibility in Responsive Design
- **Touch Targets**: Maintain 44x44px minimum regardless of breakpoint
- **Text Scaling**: Support user-initiated text size changes (especially mobile)
- **Orientation**: Ensure usability in both portrait and landscape
- **Zoom**: Never disable user scaling (viewport meta: user-scalable=yes)
- **Focus Order**: Maintain logical sequence in both layouts
- **Hidden Content**: Ensure accessibility of content revealed at different breakpoints
- **Reduced Motion**: All essential content and functionality must work without animation

## Specific Section Responsive Rules

### TRÀ CỐ / HOME
- **Desktop (≥ 800px)**: 
  - Positioned at top of document
  - Left sand / right ocean composition
  - Full Directional Water Wake implementation
  - Hero introduction content
  
- **Mobile (< 800px)**:
  - Full width viewport or constrained width
  - Height: content-driven with minimum viewport height
  - Local water interaction at bottom or specific area
  - Headline size reduced per DESIGN_SPEC.md (54-96px range)
  - CTA buttons full-width or touch-optimized
  - Sand/water composition maintained (may be narrower decorative edge)

### HẠ LONG / PROJECTS
- **Desktop (≥ 800px)**:
  - Positioned second in vertical scroll
  - Left sand / right ocean composition
  - Beach postcard visuals with subtle, deliberate rotation and lift-on-hover
  - One larger featured postcard and two supporting postcards (Approved Option C)
  - Stylized limestone islands in background (ocean area)
  
- **Mobile (< 800px)**:
  - Full width container
  - Postcards in vertical stack or swipeable carousel
  - Consistent sizing for touch targets
  - Reduced or eliminated rotation
  - Lift may become scale or opacity change
  - Vertical spacing for comfortable viewing
  - Sand/water composition maintained

### LĂNG CÔ / ABOUT ME
- **Desktop (≥ 800px)**:
  - Positioned third in vertical scroll
  - Left sand / right ocean composition
  - Coastal editorial content section
  - Personal journal/modules area
  - Floating film-style personal photograph (placeholder)
  
- **Mobile (< 800px)**:
  - Full width container
  - Standard vertical flow
  - Content-sized height (not constrained to box dimensions)
  - Preserved readability and accessibility
  - Sand/water composition maintained

### ĐÀ NẴNG / SKILLS
- **Desktop (≥ 800px)**:
  - Positioned fourth in vertical scroll
  - Left sand / right ocean composition
  - Bento Cards on sand area (left side)
  - Floating Skill Net on water area (right side)
  
- **Mobile (< 800px)**:
  - Full width container
  - Bento Cards stack vertically or adapt to width
  - Floating Skill Net simplified with fewer visible nodes/logos
  - Sand/water composition maintained (may be narrower decorative edge)
  - Touch-optimized interactions

### QUY NHƠN / RESUME
- **Desktop (≥ 800px)**:
  - Positioned fifth in vertical scroll
  - Left sand / right ocean composition
  - Large vertical Experience Timeline (left side)
  - Compact Education Card (left side)
  - Compact Certifications Card (left side)
  - Download Resume PDF action
  
- **Mobile (< 800px)**:
  - Full width container
  - Standard vertical flow
  - Experience timeline scrollable within section
  - Cards adapt to width (may stack vertically)
  - Sand/water composition maintained
  - Preserved readability and accessibility

### NHA TRANG / PLAYGROUND
- **Desktop (≥ 800px)**:
  - Positioned sixth in vertical scroll
  - Left sand / right ocean composition
  - Interactive Lab Cards (left side)
  - Nha Trang Coastal Decorations (right side)
  
- **Mobile (< 800px)**:
  - Full width container
  - Standard vertical flow
  - Interactive elements adapt to width and touch
  - Decorations scale appropriately
  - Sand/water composition maintained
  - Preserved readability and accessibility

### MŨI NÉ / PROJECT ARCHIVE
- **Desktop (≥ 800px)**:
  - Positioned seventh in vertical scroll
  - Left sand / right ocean composition
  - Structured project grid (Approved Option A)
  - Search input
  - Category filters
  
- **Mobile (< 800px)**:
  - Full width container
  - Standard vertical flow
  - Project grid adapts to width (may become list view)
  - Search and filter controls touch-optimized
  - Sand/water composition maintained
  - Preserved readability and accessibility

### MŨI CÀ MAU / CONTACT
- **Desktop (≥ 800px)**:
  - Positioned eighth (bottom) in vertical scroll
  - Left sand / right ocean composition transitioning to mangroves/alluvial
  - Clear heading: CONTACT
  - Short invitation to get in touch
  - Primary email CTA
  - Visible email address
  - GitHub and LinkedIn links (where provided)
  - Back to Top
  - Minimal footer
  
- **Mobile (< 800px)**:
  - Full width container
  - Standard vertical flow
  - Content-sized height (not constrained to box dimensions)
  - Contact information and invitation readable
  - Social links touch-optimized
  - Back to Top returns to Trà Cổ section
  - Sand/water composition maintained through mangrove transition
  - Preserved readability and accessibility

## Implementation from Prototype

Review the existing prototype implementation to:
1. Determine current responsive behavior
2. Identify gaps relative to this specification
3. Plan responsive improvements that maintain core functionality
4. Ensure mobile experience follows vertical reading order exactly
5. Verify that global panning is disabled on mobile per spec
6. Confirm Continuous Vertical Coastal Scroll replaces spatial canvas concept

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
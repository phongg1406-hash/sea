# Sunlit Shore Motion Specification

## Overview

This document specifies the motion and interaction design for the Sunlit Shore project, based on the approved DESIGN_SPEC.md, AI_HANDOFF.md, and incorporating principles from the design-taste-frontend skill.

## Motion Principles

Following the principles from DESIGN_SPEC.md:
- Animation is optional; `prefers-reduced-motion` disables transient water
- Manual Motion toggle available
- Decorative canvas updates only in the presence of wake
- Frame loop ends after trails decay
- Performance conscious: Hover 120-200ms, lift 180-280ms, module transitions 200-350ms, camera navigation ≈620ms
- All essential content survives without animation
- Effects must remain adaptive and inexpensive

Following principles from design-taste-frontend skill:
- Motion should express cause-effect relationships, not just decoration
- Entrance animations for section parts (heading → text → picture)
- Feedback on every control (press, hover, focus)
- One signature move (the directional water wake)
- One moving picture requirement
- Transform and opacity only for performance
- Respects reduced motion preferences

## Motion Categories

### 1. Signature Move: Directional Water Wake
**The defining interaction of Sunlit Shore**

#### Specification (from DESIGN_SPEC.md)
- **Interaction Reference**: A finger stirring water sideways
- **Visual Feedback**: Directional, non-concentric, asymmetrical wake (not circular radial pulses)
- **Behavior Table**:
  - Slow sideways move: Thin offset channel follows cursor vector
  - Fast move: Broader/taller channel; highlights spread
  - Curve/reversal: Old and new trails bend and cross
  - Stop: Trails fade over ≈1.2 sec
  - Exit water: Trail deactivates; no splashes over sand
  - Drag background to pan: Water wake suppressed during pan
  - Touch: Short wake on tap; scrolling remains native

#### Implementation Technique
- Bounded recent pointer samples (≤34 points; historical spec suggested 10-20, now capped higher)
- `requestAnimationFrame` only while trails exist
- Two offset channels derived from the motion normal
- Short specular fragments
- Time-decay fade
- Downsample transient canvas to ~75% CSS resolution with DPR capped at 1.25
- No simulated pressure field, particle pool or WebGL render loop
- No rings drawn
- Switch off on hidden document/reduced-motion/lite mode

#### Performance Characteristics
- Active only when cursor is moving over water area
- Memory efficient: bounded history of pointer samples
- CPU efficient: calculations only during active wake
- GPU efficient: limited canvas size and resolution
- Automatic deactivation when not needed

#### Reduced Motion Fallback
- When `prefers-reduced-motion` is enabled:
  - Wake rendering disabled completely
  - No visual wake trails
  - Cursor position may still be tracked for other purposes
  - Alternative subtle feedback may be provided (optional)

### 2. Entrance Animations
**For section content as it enters viewport**

#### Specification
- **Pattern**: Staggered entrance of section components
- **Order**: Heading → then text/content → then pictures/media
- **Timing**: 60-90ms stagger between elements
- **Animation**: 
  - Rising 16-32px with opacity fade-in
  - Transform/translate only (performance conscious)
  - Easing: deceleration when arriving (ease-out curve)
- **Duration**: 300-500ms total for each element
- **Trigger**: Element entering viewport (intersection observer or scroll event)

#### Application
- **Sections**: All six main regions (Hero, Selected Work, Playground, Archive, About, Contact)
- **Components**: Headings, body text, images, cards, interactive elements
- **Exceptions**: 
  - Immediately critical navigation elements (may appear instantly)
  - Background layers and static textures
  - Elements already visible on initial load

#### Reduced Motion Fallback
- When `prefers-reduced-motion` is enabled:
  - Elements appear instantly without animation
  - Maintain proper initial state and positioning
  - No layout shift or jarring appearance

### 3. Control Feedback Animations
**For interactive elements**

#### Button Press/Activation
- **Timing**: 100-150ms total duration
- **Animation**:
  - Scale: 0.95-1.05 on press (subtle tactile feedback)
  - Restore on release
  - Transform only (performance conscious)
  - Easing: spring or natural decay curve
- **States**: 
  - Default → Pressed → Released (with possible hover state)

#### Hover Indicators
- **Timing**: 120-200ms onset (as per DESIGN_SPEC.md)
- **Animation**:
  - Property shift: color, background, border, or transform
  - Easing: ease-in-out for smooth transition
  - Duration matching onset timing
- **Examples**:
  - Button color shift or opacity change
  - Card elevation/lift
  - Outline or border appearance
  - Icon rotation or scale

#### Focus Indicators
- **Timing**: 100-150ms onset
- **Animation**:
  - Outline or ring appearance
  - Transform scale or size increase
  - Color shift to accent
  - Easing: ease-in for immediate feedback
- **Accessibility**: Must be visible and meet contrast requirements

### 4. Section Transitions
**For camera movement between sections**

#### Waypoint Navigation (Wheel/Click)
- **Timing**: ≈620ms as per DESIGN_SPEC.md
- **Animation**:
  - Smooth camera translation and scaling
  - Easing: natural deceleration curve (ease-out)
  - Path: direct or slightly curved for natural feel
- **Trigger**: 
  - Wheel scroll (waypoint progression)
  - Mini-map/waypoint click
  - Programmatic navigation

#### Canvas Panning (Drag)
- **Timing**: 1:1 tracking with optional overshoot
- **Animation**:
  - Immediate response to drag input
  - Optional: subtle overshoot and bounce-back at bounds
  - Easing: linear during drag, spring-back at release
- **Constraints**: 
  - Camera position clamped to world bounds
  - Wake suppressed during active pan
  - Momentum continuation optional (with friction)

#### Reduced Motion Fallback
- When `prefers-reduced-motion` is enabled:
  - Transitions may be instant or greatly reduced
  - Maintain spatial relationship and orientation
  - Consider crossfade instead of movement (optional)

### 5. Module and Component Transitions
**For internal component state changes**

#### Project Detail Dialog
- **Open Animation**:
  - Fade-in backdrop (200-300ms)
  - Scale-up from center (0.95 to 1.0 over 200-300ms)
  - Easing: ease-out or spring
- **Close Animation**:
  - Fade-out backdrop (150-200ms)
  - Scale-down to center (1.0 to 0.95 over 150-200ms)
  - Easing: ease-in

#### Grid/List Toggle (Project Archive)
- **Transition**:
  - Crossfade between grid and list layouts (300-400ms)
  - Maintain scroll position where possible
  - Easing: ease-in-out
  - Transform: none (layout change only)

#### Bento Module Interactions
- **States**: Default, hover, active
- **Animations**: 
  - Subtle scale or elevation changes (100-200ms)
  - Color or opacity shifts
  - Easing: ease-in-out for hover, spring for active

### 6. Loading and Placeholder Animations
**For async content and skeleton screens**

#### Skeleton Screens
- **Animation**:
  - Shimmer or pulse effect over placeholder content
  - Linear gradient moving left-to-right
  - Duration: 1.5s cycle, infinite loop
  - Easing: linear for consistent movement
- **Trigger**: Content loading state
- **Completion**: Replace with actual content

#### Progress Indicators
- **Use Sparingly**: Only for operations >1 second
- **Animation**:
  - Circular progress or bar fill
  - Steady indication of progress
  - Easing: linear for predictable timing
- **Alternative**: Skeleton screens preferred for section loading

### 7. Ambient and Idle Animations
**Subtle movements for lifefulness**

#### Background Elements
- **Types**:
  - Very slow floating/swaying decorative objects
  - Gentle pulsing of ambient lights or highlights
  - Imperceptible background texture shifts
- **Timing**: Very slow (4-8s+ cycles)
- **Amplitude**: Minimal (<5px movement, <5% opacity change)
- **Performance**: Extremely lightweight, CSS-only preferred

#### Water Ambient
- **Base Layer**: 
  - Near-still ocean with almost imperceptible drift
  - Optional: very slow gradient shift
  - Performance: CSS transitions or minimal canvas
- **Interaction Layer**: 
  - Wake provides all interesting motion
  - Base remains calm and performant

#### Reduced Motion Fallback
- When `prefers-reduced-motion` is enabled:
  - All ambient animations disabled
  - Static backgrounds and elements
  - No unnecessary CPU/GPU usage

## Motion Implementation Guidelines

### Animation Properties
- **Transform First**: Use translate/rotate/scale/skew before other properties
- **Opacity Second**: For fade effects, combine with transform
- **Avoid**: Animating width, height, top, left (causes layout thrashing)
- **Performance**: Will-change hint only when proven beneficial
- **Easing Curves**: 
  - Entrance: ease-out (deceleration on arrival)
  - Exit: ease-in (acceleration on departure)
  - Hover/Focus: ease-in-out (symmetric)
  - Spring: for bouncy, natural feel when appropriate
  - Linear: for consistent rate needs (progress indicators, some ambient)

### Timing Values (from SPEC.md and best practices)
- **Ultra-fast**: 50-100ms (button press feedback)
- **Fast**: 100-200ms (hover onset, focus appearance)
- **Moderate**: 200-400ms (entrance animations, module transitions)
- **Slow**: 400-600ms (section navigation, major transitions)
- **Extended**: 800ms-2s+ (ambient, loading, special effects)
- **Wake Fade**: ≈1200ms as specified

### Performance Considerations
- **Layer Separation**: 
  - Static background (no animation)
  - Wake layer (conditional animation)
  - Content layer (entrance/interaction animation)
  - UI overlay layer (minimal animation)
- **RequestAnimationFrame**: Use for custom animations like wake
- **CSS Animations**: For simpler, repeatable animations
- **Web Animations API**: For complex orchestration when needed
- **Compositor-only Properties**: Stick to transform and opacity
- **Event Delegation**: Minimize listeners for performance

### Accessibility in Motion
- **Reduced Motion**: 
  - Respect `prefers-reduced-motion` media query
  - Provide meaningful static alternatives
  - Never rely on animation to convey essential information
- **Seizure Safety**: 
  - No flashing >3Hz
  - No high contrast patterns that could trigger
  - Consider photosensitive users in all animations
- **ADHD/Cognitive**: 
  - Avoid distracting or unnecessary animation
  - Ensure animation doesn't impede focus or reading
  - Provide controls to disable or reduce motion

### Implementation Approach
1. **Core Motion First**: Implement directional water wake as signature move
2. **Entrance Patterns**: Apply staggered entrance to all sections
3. **Control Feedback**: Add press/hover/focus animations to interactive elements
4. **Transitions**: Implement smooth camera navigation between sections
5. **Module Animations**: Add internal component state changes
6. **Ambient Polish**: Add subtle background animations last
7. **Testing**: Verify with reduced motion enabled throughout

### CSS Variables for Motion
```css
:root {
  /* Timing */
  --motion-duration-fast: 100ms;
  --motion-duration-moderate: 250ms;
  --motion-duration-slow: 400ms;
  --motion-duration-wake-fade: 1200ms;
  --motion-duration-navigation: 620ms;
  
  /* Easing */
  --motion-easing-entrance: cubic-bezier(0.25, 0.8, 0.25, 1); /* ease-out */
  --motion-easing-exit: cubic-bezer(0.4, 0, 0.2, 1); /* ease-in */
  --motion-easing-hover: cubic-bezier(0.3, 0, 0.5, 1); /* ease-in-out */
  --motion-easing-spring: cubic-bezier(0.68, -0.55, 0.265, 1.55);
  
  /* Distances */
  --motion-distance-entrance-rise: 20px;
  --motion-distance-scale-press: 0.05; /* 5% scale change */
  --motion-distance-focus-outline: 3px;
  
  /* Wake Specific */
  --motion-wake-sample-count: 34;
  --motion-wake-decay-time: 1200ms;
  --motion-wake-downsample: 0.75; /* 75% resolution */
  --motion-wake-dpr-cap: 1.25;
}
```

### JavaScript Animation Patterns
```javascript
// Entrance observer
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('is-visible');
      // Add stagger delay based on index or position
    }
  });
});

// Wake-style animation loop (simplified)
function animateWake() {
  if (!isWakeActive) return;
  
  // Update wake based on pointer history
  renderWake();
  
  // Continue only while active
  if (hasActiveTrails()) {
    requestAnimationFrame(animateWake);
  }
}

// Button press feedback
button.addEventListener('pointerdown', () => {
  button.style.transform = 'scale(0.95)';
});

button.addEventListener('pointerup pointerleave', () => {
  button.style.transform = '';
});
```

## Testing and Verification

### Motion Quality Checks
- **Performance**: Maintain 60fps on target hardware
- **Reduced Motion**: All essential functionality works without animation
- **Accessibility**: Navigable and understandable with motion disabled
- **Intent**: Each animation has clear purpose and feedback value
- **Performance**: No layout thrashing or excessive repaints

### Browser Compatibility
- **CSS Animations**: Wide support with fallbacks
- **Web Animations API**: Progressive enhancement
- **RequestAnimationFrame**: Universal support
- **Intersection Observer**: Polyyfill available if needed
- **Prefers-reduced-motion**: Standard media query support

## Implementation from Existing Code

Review the existing prototype implementation in `references/prototype/index.html`, `styles.css`, and `app.js` to:
1. Identify current motion implementations
2. Compare against this specification
3. Plan evolution toward full specification compliance
4. Maintain backward compatibility during transition
5. Ensure all new motion follows the principles exactly

## Future Enhancements (Post-MVP)

- **Low-resolution displacement shader**: For wake distortion of background (perf-tested)
- **Advanced ambient systems**: More sophisticated background interactions
- **Gesture-driven transitions**: Swipe or pinch for section navigation
- **Audio-reactive elements**: Optional sound-responsive visualizations
- **Multi-user awareness**: Subtle indications of others' interactions
- **Environmental responsiveness**: Wake changes based on time/date/weather
# Sunlit Shore Asset Manifest

## Overview

This document specifies all visual assets used in the Sunlit Shore project, following the code-first artwork principle from DESIGN_SPEC.md and AI_HANDOFF.md. It distinguishes between assets created in code (CSS/SVG/canvas) and those that are actual project content (screenshots, photographs).

## Code-First Artwork Principle

As specified in DESIGN_SPEC.md and AI_HANDOFF.md:
- **Code-created visual language is mandatory**
- **Photorealistic textures are optional and currently not used**
- **Text-only AI coding must be sufficient to maintain the project**
- **No required Vision, no generated fake screenshots or invented project claims**

This means:
- All UI elements, backgrounds, textures, and effects should be created with CSS, SVG, or canvas
- Actual project screenshots are allowed as content (not UI)
- No reliance on external image generation tools for core UI
- No use of photorealistic textures that would require image editing software

## Asset Categories

### 1. Code-Generated Assets (Preferred)

These assets are created entirely through code and should constitute the majority of the visual design.

#### CSS-Generated
- **Gradients**: Water backgrounds, sand textures, button backgrounds
- **Shapes**: Geometric forms, decorative elements, icons
- **Patterns**: Repeating textures, noise, halftones (via CSS)
- **Filters**: Basic color adjustments, blurs (performance-considered)
- **Variables**: All color tokens, typography settings, spacing

#### SVG Assets
- **Icons**: Navigation icons, UI symbols, decorative marks
- **Paths**: Coastal outlines, sand/water boundaries, foam lines
- **Shapes**: Geometric decorations, symbols, markers
- **Symbols**: Reusable icons and graphic elements
- **Filters**: SVG filters for performance-effective effects

#### Canvas Assets
- **Water Wake**: Transient directional wake effect (primary canvas use)
- **Particle Systems**: Optional subtle effects (performance-tested)
- **Data Visualization**: Skills charts, project statistics (if implemented)
- **Generative Art**: Algorithmic patterns based on project data

### 2. Actual Project Content (Allowed)

These are genuine assets from the project owner's work and should be clearly labeled as such.

#### Project Screenshots
- **Allowed**: Actual screenshots of deployed projects
- **Requirements**: 
  - Clearly labeled as project work
  - Optimized for web (WebP/AVIF, appropriate dimensions)
  - Alternative text describing the project
  - Not used as UI textures or decorative elements
- **Format**: WebP preferred, PNG for lossless when needed
- **Usage**: In project cards, detail dialogs, archive views

#### Photographs of Owner
- **Allowed**: genuine photographs of the project owner
- **Requirements**:
  - Clearly personal portraits, not stock images
  - Optimized for web performance
  - Alternative text provided
  - Used sparingly (About section primarily)
- **Usage**: Biography section, professional profiles

#### Scanned Physical Work
- **Allowed**: if applicable to owner's field
- **Requirements**:
  - Clearly identified as source material
  - Optimized for web viewing
  - Context provided about the work
- **Usage**: Process display, portfolio items (if relevant)

### 3. Prohibited Assets

These assets violate the code-first artwork principle and should not be used.

#### Photorealistic Textures
- **Prohibited**: 
  - Water textures attempting to look like real water
  - Sand textures attempting to look like real sand
  - Material textures (wood, metal, fabric) for UI decoration
- **Exception**: Actual project screenshots showing these materials in context

#### Stock Photography
- **Prohibited**: 
  - Generic business/technology stock photos
  - Lifestyle images not featuring the owner or actual work
  - Nature scenes used as UI backgrounds or decoration
- **Exception**: Actual location photos if personally taken by owner

#### Generated/Fake Content
- **Prohibited**:
  - AI-generated "project" screenshots
  - Fake testimonials or reviews
  - Generated profile pictures of non-existent people
  - Placeholder content pretending to be real work
- **Allowed**: Clearly labeled placeholder content during development

#### External UI Kits
- **Discouraged**: 
  - Complete icon sets that don't match visual language
  - Pre-built components requiring override
  - Assets that conflict with code-first approach
- **Allowed**: Individual SVG icons that are modified to match system

## Asset Creation Guidelines

### For Code-Generated Assets
1. **Performance First**: Consider repaint cost, file size, animation impact
2. **Maintainability**: Use clear naming, modular structure, comments
3. **Scalability**: SVG for icons/shapes that need to scale
4. **Reusability**: Create symbols and reusable patterns
5. **Accessibility**: Ensure sufficient contrast, provide alternatives
6. **File Size**: Keep code assets lightweight, consider inlining critical CSS/SVG

### For Actual Project Content
1. **Optimization**: 
   - Format: WebP for lossy, PNG for lossless/text, SVG for vector
   - Dimensions: Resize to display dimensions, not upload raw
   - Compression: Optimize without losing quality
   - Lazy Loading: Use for below-fold content
2. **Attribution**:
   - Clear labeling of what the asset shows
   - Context for project screenshots (tech stack, role, etc.)
   - Dates if relevant (when work was completed)
3. **Alternative Text**:
   - Descriptive and meaningful
   - Empty decorative="" for purely decorative images
   - Context-rich for informative images
4. **Usage Context**:
   - Never use project screenshots as UI textures/backgrounds
   - Always maintain clear distinction between UI and content
   - Content should enhance, not replace, effective UI design

## Specific Asset Types

### Icons and Symbols
- **Preferred Method**: Inline SVG or SVG sprites
- **Style**: Match visual language (corner radius, stroke weight, style)
- **Sizes**: Define in CSS, not HTML attributes where possible
- **Accessibility**: 
  - Decorative: aria-hidden="true"
  - Informative: provide text alternative or label
  - Interactive: ensure adequate touch target with icon

### Backgrounds and Textures
- **Water**: CSS gradients with possible animation (performance-tested)
- **Sand**: CSS patterns, gradients, or noise
- **Foam/Cards**: Solid colors with subtle texture via CSS
- **Performance**: Avoid large background images; use CSS where possible

### Decorative Elements
- **Stars/Suns**: CSS shapes or minimal SVG
- **Geometric Patterns**: CSS repeating-linear-gradient or canvas
- **Organic Shapes**: SVG paths simplified for performance
- **Usage**: Sparingly, to avoid visual clutter

### Data Visualization
- **Charts**: SVG or canvas, preferring SVG for accessibility
- **Diagrams**: Simple SVG for flow or relationship visualization
- **Maps**: SVG for schematic, not literal geographic
- **Performance**: Update only when data changes, not continuously

## Implementation from Prototype

Review the existing prototype in `references/prototype/index.html` to:
1. Identify current asset usage (images, SVG, CSS effects)
2. Determine which assets comply with code-first principle
3. Note any non-compliant assets requiring replacement
4. Plan migration to compliant assets where feasible
5. Ensure all new assets follow these guidelines exactly

## Asset Optimization Checklist

For all assets (especially project content):
- [ ] Properly formatted (WebP/AVIF/SVG preferred)
- [ ] Appropriately dimensioned for use
- [ ] Compressed without quality loss
- [ ] Lazy loaded if below-the-fold
- [ ] Has appropriate alternative text
- [ ] Clearly labeled as code-generated or actual content
- [ ] Used in appropriate context (UI vs content)
- [ ] Optimized for performance (file size, decode time)
- [ ] Accessible (contrast, labeling, alternatives)
- [ ] Maintainable (clear naming, organization)

## Future Asset Considerations

### Potential Code-Generated Enhancements
- **Procedural textures**: CSS/SVG patterns that simulate materials authentically
- **Algorithmic decoration**: Generated elements based on project data or time
- **Interactive generative art**: Canvas elements responding to interaction
- **Data-driven visuals**: Visual representations of skills, experience, etc.

### Content Asset Guidelines (if expanded)
- **Photography**: If personally taken, optimize and attribute clearly
- **Video**: If owner-created, provide controls, captions, performance considerations
- **Documents**: If relevant, provide as downloadable with clear labeling
- **Audio**: Minimal use, with controls and alternatives, performance considered

### Tools and Workflow
- **Build Process**: 
  - Image optimization as build step
  - SVG sprite generation
  - Critical CSS inlining
  - Asset hashing for cache busting
- **Development**: 
  - Local optimization tools
  - Preview at multiple sizes/network conditions
  - Automated accessibility checking
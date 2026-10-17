# Sunlit Shore Section Layouts

## Overview

This document specifies the layout and composition for each of the eight main sections in the Sunlit Shore Continuous Vertical Coastal Scroll, based on the approved DESIGN_SPEC.md v2.0 and architectural guidelines.

## Continuous Vertical Coastal Scroll Foundation

Based on DESIGN_SPEC.md v2.0:
- **Primary navigation**: Natural vertical scrolling (mouse wheel, touch drag, keyboard arrow keys)
- **Secondary navigation**: Anchor links, Geographic Shore Map
- **Document nature**: Transformable HTML/CSS/SVG DOM stage (not bitmap canvas)
- ** lớng akikpx**: Reveals a portion of the vertically scrolling document
- **Clamping**: Prevents unbounded drifting into empty space (top/bottom bounds)
- **Visual composition**: Sand/land stays on left side, ocean stays on right side, proportions vary continuously
- **Coastline**: Continuous S-shaped coastal journey from Trà Cổ to Mũi Cà Mau
- **Eight destinations**: Follow Vietnam's coastline from north to south

## Section Specifications

### 1. TRÀ CỐ / HOME
- **Vertical Position**: Top of document
- **Primary Activity**: Introduction, water wake demonstration
- **Land/Water Composition**: Hero left (sand), right (ocean)

#### Layout Composition
- **Fixed Elements**: 
  - Hero headline (site title or personal name)
  - Supporting tagline/description
  - Primary call-to-action (explore/projects)
- **Interactive Elements**:
  - Directional water wake responsive to cursor movement
  - Subtle floating/animated decorative elements (stars, etc.)
- **Background Treatment**:
  - Ocean base (`#00BCCD`) with possible gradient variation
  - Shallow water transition where meeting "shore"
  - SVG coastal sand and foam paths at bottom
  - Optional CSS-generated caustic-like line texture
- **Visual Hierarchy**:
  - Dominant: Site identification (large headline)
  - Secondary: Water interaction demonstration
  - Tertiary: Navigation cues to other sections
- **Responsive Behavior**:
  - Mobile (≤800px): Stacked vertical layout with reduced water wake interaction
  - Desktop (>800px): Full coastal scroll positioning as specified

#### Content Guidelines
- Headline: Personal name or site title (large display type)
- Subheadline: Brief descriptor or tagline
- CTA: Clear invitation to explore work ("View Projects", "See Work")
- Secondary links: Subtle navigation to About or Contact

### 2. HẠ LONG / PROJECTS
- **Vertical Position**: Second section
- **Primary Activity**: Featured postcard projects
- **Land/Water Composition**: Left (sand/postcards), right (ocean/postcards)

#### Layout Composition
- **Primary Display**: 
  - 3 featured project postcards (1 larger, 2 supporting per Approved Option C)
  - Arranged with subtle, deliberate rotation and lift-on-hover
  - Each postcard: beach postcard visual with accessible label
- **Secondary Elements**:
  - Section heading ("PROJECTS")
  - Stylized limestone islands in background (ocean area)
  - Navigation indicators to adjacent sections
- **Background Treatment**:
  - Sand base (`#FFF0CB`) on left side
  - Ocean base (`#00BCCD`) on right side
  - Sand/water boundary follows coastline contour
- **Visual Hierarchy**:
  - Dominant: Featured project postcards
  - Secondary: Section identification
  - Tertiary: Background environmental context
- **Interaction Model**:
  - Postcards: hover lift, click to open Shared Project Detail Modal
  - Section-level: visual response to nearby cursor wake

#### Content Guidelines
- Section heading: "PROJECTS"
- Postcards: Each showing a different featured project
- Postcard content: Project thumbnail, title, optional badges/tags
- Spacing: Appropriate for hover lift effect without cluttering reading area

### 3. LĂNG CÔ / ABOUT ME
- **Vertical Position**: Third section
- **Primary Activity**: Editorial profile & personal journal
- **Land/Water Composition**: Left (sand/content), right (ocean/distant mountains)

#### Layout Composition
- **Primary Display**:
  - Coastal editorial content section
  - Personal journal/modules area
  - Floating film-style personal photograph (placeholder)
- **Secondary Elements**:
  - Section heading ("ABOUT ME")
  - Professional portrait or avatar (if desired)
  - Contact information or social links
- **Background Treatment**:
  - Sand base with possible variation toward Foam
  - Distant mountain silhouettes in ocean area
  - Subtle texture suggesting professional document or canvas
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
- Section heading: "ABOUT ME"
- Introduction: Concise personal/professional overview
- Personal Notes: 2-3 modules with suggested themes (Interests, My Approach, Currently Learning)
- Floating Film Photo: Large simple photograph close to shoreline (placeholder until user supplies actual photo)
- Distant Environment: Stylized mountains visible in ocean area

### 4. ĐÀ NẴNG / SKILLS
- **Vertical Position**: Fourth section
- **Primary Activity**: Bento Cards + Floating Skill Net
- **Land/Water Composition**: Left (sand/bento), right (ocean/skill net)

#### Layout Composition
- **Primary Display**:
  - Bento Cards on sand area (left side)
  - Floating Skill Net on water area (right side)
- **Secondary Elements**:
  - Section heading ("SKILLS")
  - Skill category labels (Frontend/UI, Backend/Data, Tools/Workflow, Currently Learning)
- **Background Treatment**:
  - Sand base (`#FFF0CB`) on left side for Bento Cards
  - Ocean base (`#00BCCD`) on right side for Skill Net
  - Clear sand/water separation following coastline
- **Visual Hierarchy**:
  - Dominant: Skills visualization (Bento Cards + Skill Net)
  - Secondary: Section identification
  - Tertiary: Background environmental context
- **Interaction Model**:
  - Bento Cards: hover states to highlight related Skill Net nodes
  - Floating Skill Net: cursor proximity deforms mesh, hover highlights related categories
  - Skill information accessible without interacting with net

#### Content Guidelines
- Section heading: "SKILLS"
- Bento Categories:
  1. Frontend & UI
  2. Backend & Data
  3. Tools & Workflow
  4. Currently Learning
- Bento Sizes: Asymmetric but carefully aligned
- Floating Skill Net: Diamond-shaped interconnected mesh with 8-10 skill logos (desktop)
- Skill Logos: Examples include Git, React, SQL, TypeScript, etc.
- Buoys: May appear at selected net edges
- Motion: Gentle wave-like motion with phase offsets

### 5. QUY NHƠN / RESUME
- **Vertical Position**: Fifth section
- **Primary Activity**: Editorial Timeline + Compact Cards
- **Land/Water Composition**: Left (sand/timeline), right (ocean/cards)

#### Layout Composition
- **Primary Display**:
  - Large vertical Experience Timeline (left side)
  - Compact Education Card (left side)
  - Compact Certifications Card (left side)
  - Download Resume PDF action
- **Secondary Elements**:
  - Section heading ("RESUME")
  - Stylized coastal rock formations
  - Light, professional styling
- **Background Treatment**:
  - Sand base (`#FFF0CB`) on left side for timeline and cards
  - Ocean base (`#00BCCD`) on right side
  - Sand/water boundary follows coastline contour
- **Visual Hierarchy**:
  - Dominant: Professional timeline and credentials
  - Secondary: Section identification
  - Tertiary: Background environmental context
- **Interaction Model**:
  - Timeline: scrollable experience entries
  - Cards: hover/focus states for Education and Certifications
  - Resume PDF: clear download action

#### Content Guidelines
- Section heading: "RESUME"
- Experience: Vertical timeline with roles, companies, dates
- Education: Compact card with institution, degree, dates
- Certifications: Compact card with name, issuing organization, dates
- Download Action: Clear button/link for resume PDF
- Credential Verification: Support for verification links if available
- Environment: Stylized coastal rock formations, limited decorative movement

### 6. NHA TRANG / PLAYGROUND
- **Vertical Position**: Sixth section
- **Primary Activity**: Interactive Lab Cards + Coastal Decorations
- **Land/Water Composition**: Left (sand/lab cards), right (ocean/decorations)

#### Layout Composition
- **Primary Display**:
  - Interactive Lab Cards (left side)
  - Nha Trang Coastal Decorations (right side)
- **Secondary Elements**:
  - Section heading ("PLAYGROUND")
  - Location label: "06 / NHA TRANG, KHÁNH HÒA"
- **Background Treatment**:
  - Sand base (`#FFF0CB`) on left side for Lab Cards
  - Ocean base (`#00BCCD`) on right side for decorations
  - Sand/water boundary follows coastline contour
- **Visual Hierarchy**:
  - Dominant: Interactive experimentation area
  - Secondary: Section identification and location
  - Tertiary: Coastal environmental context
- **Interaction Model**:
  - Lab Cards: interactive demos and experiments
  - Decorations: passive environmental elements
  - Reset: return interactive elements to initial state (if applicable)

#### Content Guidelines
- Section heading: "PLAYGROUND"
- Location: `06 / NHA TRANG, KHÁNH HÒA`
- Interactive Lab Cards: represent real creative coding experiments
  - Water or procedural graphic experiments
  - Motion/UI experiments
  - Mini interactive experiences
- Coastal Decorations: recognizable but restrained
  - Hòn Chồng rock formations
  - Small stylized silhouette inspired by Po Nagar Cham Towers
  - Tropical marine life and small coral details
- Guidelines: Avoid duplicating decorative effects already present unless demo provides genuinely new interaction

### 7. MŨI NÉ / PROJECT ARCHIVE
- **Vertical Position**: Seventh section
- **Primary Activity**: Coastal Project Library
- **Land/Water Composition**: Left (sand/project grid), right (ocean/dunes/kites)

#### Layout Composition
- **Primary Display**:
  - Structured project grid (Approved Option A)
  - Search input
  - Category filters
- **Secondary Elements**:
  - Section heading ("PROJECT ARCHIVE")
  - Visual indicator of Grid/List toggle (aria-pressed)
  - Item counter showing total/shown projects
- **Background Treatment**:
  - Sand base (`#FFF0CB`) on left side for project grid
  - Ocean base transitioning to `#87967E` (Deep Water/Cà Mau) on right side
  - Stylized dunes and kites in ocean area
  - Sand/water boundary follows coastline contour
- **Visual Hierarchy**:
  - Dominant: Project browsing interface
  - Secondary: Section identification and controls
  - Tertiary: Background environmental context
- **Interaction Model**:
  - Grid view: Cards arranged in rows and columns
  - List view: Vertical stack with detailed metadata
  - Toggle: smooth transition between views
  - Search: real-time filtering of projects
  - Filters: category-based narrowing of project list
  - Card interaction: hover/focus states, click to open Shared Project Detail Modal
  - Selection: visual indication of chosen item(s)

#### Content Guidelines
- Section heading: "PROJECT ARCHIVE"
- Project Cards: Consistent design showing essential metadata
- Card content: Title, type/tags, year, status indicator
- Search: clearly labeled input field
- Filters: clearly labeled category controls
- Empty state: Helpful message when no projects to show
- Environment: Stylized dunes and kites visible in ocean area
- Shared Modal: Consistent Project Detail Modal used with PROJECTS section

### 8. MŨI CÀ MAU / CONTACT
- **Vertical Position**: Bottom of document
- **Primary Activity**: Open Invitation + Thank You
- **Land/Water Composition**: Left (sand/content), right (ocean/mangroves/alluvial)

#### Layout Composition
- **Primary Display**:
  - Clear heading: CONTACT
  - Short invitation to get in touch
  - Primary email CTA
  - Visible email address
  - GitHub and LinkedIn links (where provided)
  - Back to Top
  - Minimal footer
- **Secondary Elements**:
  - Section heading ("CONTACT")
  - Friendly Thank You message
  - Cà Mau landscape elements
- **Background Treatment**:
  - Sand base transitioning to `#B8B59A` (Light Silt) on left side
  - Ocean base transitioning through `#A4AA8E` (Alluvial Water) to `#87967E` (Deep Water) to `#597D61` (Mangrove) on right side
  - Gradual palette transition from Mũi Né to Cà Mau
  - Sand/water boundary follows coastline contour
- **Visual Hierarchy**:
  - Dominant: Contact information and invitation
  - Secondary: Section identification and thank you message
  - Tertiary: Background environmental context showing transition to mangroves
- **Interaction Model**:
  - Email: clear CTA and visible address
  - Social Links: standard hover/focus states for GitHub/LinkedIn
  - Back to Top: returns to Trà Cổ section
  - Thank You: sincere, warm, professional message

#### Content Guidelines
- Section heading: "CONTACT"
- Invitation: Short, friendly invitation to get in touch
- Primary Email CTA: Clear call-to-action for email
- Visible Email Address: Actual email address for contact
- Social Links: GitHub and LinkedIn icons/links where provided
- Back to Top: Returns user to Trà Cổ section
- Thank You Message: Brief, sincere thank-you (approved draft: "Thanks for stopping by! ♡\n\nThank you for taking the time to explore my work and considering me. It really means a lot.\n\nI hope we get to create something together someday!")
- Cà Mau Landscape:
  - Mangrove forests
  - Coastal alluvial land
  - Silt-rich tidal water
  - Earthy green-brown water
  - Warm muted foam
  - Palette: Light Silt (`#B8B59A`), Alluvial Water (`#A4AA8E`), Deep Water (`#87967E`), Mangrove (`#597D61`)
- Important: Do NOT abruptly replace bright turquoise with brown at hard boundary; gradual transition required
- Contact Behavior: Content fades in, remains readable near document end, no forced fade out at bottom
- Journey Completion: Show subtle 08/08 state when visible near document end

## Layout Implementation Guidelines

### Vertical Positioning
- **Scroll Direction**: Natural vertical scrolling as primary navigation
- **Section Order**: Fixed sequence Trà Cổ → Hạ Long → Lăng Cô → Đà Nẵng → Quy Nhơn → Nha Trang → Mũi Né → Mũi Cà Mau
- **Boundary Definition**: Clear visual separation between sections using spacing and background transitions
- **Content-safe Regions**: Ensure critical content remains within visible areas accounting for scroll position

### Responsive Behavior
- **Mobile (≤800px)**:
  - One-column vertical reading order, standard page scroll
  - Shore still visually represented with narrower decorative edge or simplified water area
  - Text and links remain DOM-based
  - Core project links never require drag/hover
  - Navigation menu uses real buttons, dialog uses native `<dialog>`
  - Geographic Shore Map uses compact expandable navigation panel
  - Touch gestures for scrolling take priority over Water Wake and decorative dragging
  - Local water interaction replaces global wake (performance optimization)
- **Desktop (>800px)**:
  - Continuous Vertical Coastal Scroll with artistic Main Scene
  - Left sand / right ocean composition maintained
  - Geographic Shore Map as expandable panel
  - Full Directional Water Wake implementation
  - Floating Skill Net with 8-10 visible logos
  - Hover-based interactions where appropriate

### Visual Separation
- **Between Sections**: 
  - Generous spacing (implementation-defined, consistent with scroll behavior)
  - Background gradient or transition between zone types (palette shifts, environmental changes)
  - Optional: subtle boundary markers or landmarks
  - Consistent treatment regardless of actual distance
  - Scroll fade-in/fade-out effects provide transitional feedback
- **Within Sections**:
  - Appropriate padding and margins for content
  - Clear visual hierarchy and grouping
  - Responsive adjustment of internal spacing
  - Content prioritization: show core content first on mobile

### Performance Considerations
- **Render Distance**: Consider culling or simplifying distant sections in Main Scene
- **Level of Detail**: Reduce complexity for off-screen sections
- **Water Wake Performance**: Canvas 2D with bounded history, downsample resolution, automatic deactivation
- **Map Data**: Use verified open-source geographic data with proper attribution
- **Skill Net Animation**: Lightweight custom motion model, avoid physics simulation
- **Section Transitions**: Lightweight CSS transitions for fade effects

### Accessibility in Layout
- **Keyboard Navigation**: Logical tab order following visual flow
- **Focus Management**: Clear indication when moving between sections; preserved during Easter Egg opening/closing
- **Screen Reader**: Proper landmarks and labeling for navigation
- **Reduce Motion**: All essential content and functionality must work without animation (`prefers-reduced-motion`)
- **Touch Targets**: Minimum 44x44px with adequate spacing
- **Semantic HTML**: Correct elements for meaning; ARIA labels where needed
- **Visible Focus Indicators**: Clear indication of focused element
- **Contrast**: Minimum 4.5:1 for normal text (WCAG AA)
- **Alternative Text**: Descriptive and meaningful for informative images; empty decorative="" for purely decorative images

### Scroll Fade System
- **Purpose**: Provide transitional feedback between sections
- **Design**:
  - Fade-in/fade-out effects as sections enter/leave viewport
  - Implemented as transparent overlays
  - Performance-conscious implementation
  - Respects prefers-reduced-motion setting
- **Behavior**:
  - Sections fade in as they enter viewport from top
  - Sections fade out as they leave viewport toward bottom
  - Overlays do not interfere with interaction or readability
  - Transitions are subtle and purposeful, not distracting

### Geographic Shore Map Integration
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

### Vũng Tàu Secret Easter Egg Container
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

## Implementation from Prototype

Review the existing references/prototype/index.html to:
1. Map current implementation to these specifications
2. Identify which sections closely match the spec
3. Note areas requiring adjustment or redesign
4. Plan implementation that maintains backward compatibility where possible
5. Ensure all new layouts follow vertical scroll positioning exactly

## Future Considerations

- **Dynamic Content**: Potential for content-driven section height adjustment
- **Section Variations**: Layout adjustments based on actual content volume
- **Seasonal Variations**: Palette or environmental changes based on time/date
- **User Customization**: Ability to adjust density or spacing preferences
- **Analytics Integration**: Tracking popular sections, discovery flow completion, interaction patterns
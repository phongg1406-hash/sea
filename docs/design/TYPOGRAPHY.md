# Sunlit Shore Typography System

## Approved Typography (from DESIGN_SPEC.md)

Based on the approved design specification, Sunlit Shore uses the following font families:

- Headlines and content: local **Arial/Helvetica** (system fonts to avoid remote requests)
- Humanist italic accent: **Georgia**
- Navigation labels and metadata: **Courier New**

The specification notes that if design review later approves, we could use self-hosted, legally sourced font subsets like Space Grotesk / Inter / Space Mono.

## Semantic Typography Roles

Following the principles from the design-taste-frontend skill about proper type scaling and hierarchy:

### Type Scale
Based on the DESIGN_SPEC.md guidelines (Headline 85–146 desktop px, 54–96 mobile; section headlines ≈40–67 px; Text ≈16–23 px):

- `--type-step-0` (min): 1rem (16px) - Body text minimum
- `--type-step-1`: 1.125rem (18px) - Body text
- `--type-step-2`: 1.25rem (20px) - Body text maximum / lead-in text
- `--type-step-3`: 1.5rem (24px) - Section subheadings / metadata
- `--type-step-4`: 2rem (32px) - Section headings (lower end)
- `--type-step-5`: 2.5rem (40px) - Section headings (upper end)
- `--type-step-6`: 3rem (48px) - Page section titles
- `--type-step-7`: 4rem (64px) - Hero headlines (lower end)
- `--type-step-8`: 5rem (80px) - Hero headlines (upper end)
- `--type-step-9`: 6rem (96px) - Hero headlines maximum
- `--type-step-10`: 7rem (112px) - Hero headlines (for large displays)
- `--type-step-11`: 8rem (128px) - Hero headlines maximum
- `--type-step-12`: 9rem (144px) - Special hero treatments

### Font Family Mapping
- `--font-family-display`: 'Arial', 'Helvetica', sans-serif - For headlines and prominent text
- `--font-family-body`: 'Arial', 'Helvetica', sans-serif - For body content
- `--font-family-accent`: 'Georgia', serif - For humanist italic accents, quotes
- `--font-family-meta`: 'Courier New', monospace - For navigation labels, metadata, code-like text

### Font Weights
Following design-taste-frontend principles for weight hierarchy:
- `--font-weight-light`: 300 - For subtle text, secondary information
- `--font-weight-regular`: 400 - For body text, primary content
- `--font-weight-medium`: 500 - For subheadings, emphasized text
- `--font-weight-semibold`: 600 - For section headings, important UI elements
- `--font-weight-bold`: 700 - For hero headlines, primary actions
- `--font-weight-extrabold`: 800 - For special emphasis, data visualization

### Line Heights & Letter Spacing
Based on DESIGN_SPEC.md and design-taste-frontend principles:
- `--line-height-tight`: 1.2 - For headlines, compact spacing
- `--line-height-normal`: 1.5 - For body text, comfortable reading
- `--line-height-relaxed`: 1.75 - For lead-in text, improved readability
- `--letter-spacing-normal`: 0 - Default spacing
- `--letter-spacing-tight`: -0.02em - For display type (HEADLINES)
- `--letter-spacing-wide`: 0.05em - For metadata, all caps, tracking

## Specific Element Styles

### Headlines
- Hero headline: `var(--type-step-8)` to `var(--type-step-11)` (5rem-8rem / 80px-128px)
  - Font: `var(--font-family-display)`
  - Weight: `var(--font-weight-bold)` to `var(--font-weight-extrabold)`
  - Letter spacing: `var(--letter-spacing-tight)` (-0.02em)
  - Line height: `var(--line-height-tight)` (1.2)

- Section headline: `var(--type-step-4)` to `var(--type-step-5)` (2rem-2.5rem / 32px-40px)
  - Font: `var(--font-family-display)`
  - Weight: `var(--font-weight-semibold)` (600)
  - Letter spacing: `var(--letter-spacing-tight)` (-0.02em)
  - Line height: `var(--line-height-normal)` (1.5)

- Subsection headline: `var(--type-step-3)` (1.5rem / 24px)
  - Font: `var(--font-family-display)`
  - Weight: `var(--font-weight-medium)` (500)
  - Letter spacing: `var(--letter-spacing-normal)` (0)
  - Line height: `var(--line-height-normal)` (1.5)

### Body Text
- Primary body: `var(--type-step-1)` to `var(--type-step-2)` (1.125rem-1.25rem / 18px-20px)
  - Font: `var(--font-family-body)`
  - Weight: `var(--font-weight-regular)` (400)
  - Letter spacing: `var(--letter-spacing-normal)` (0)
  - Line height: `var(--line-height-normal)` (1.5)

- Lead-in/summary text: `var(--type-step-2)` (1.25rem / 20px)
  - Font: `var(--font-family-body)`
  - Weight: `var(--font-weight-regular)` (400)
  - Letter spacing: `var(--letter-spacing-normal)` (0)
  - Line height: `var(--line-height-relaxed)` (1.75)

### Metadata & Captions
- Metadata: `var(--type-step-3)` (1.5rem / 24px)
  - Font: `var(--font-family-meta)`
  - Weight: `var(--font-weight-medium)` (500)
  - Letter spacing: `var(--letter-spacing-wide)` (0.05em)
  - Line height: `var(--line-height-normal)` (1.5)

- Captions: `var(--type-step-0)` (1rem / 16px)
  - Font: `var(--font-family-body)`
  - Weight: `var(--font-weight-light)` (300)
  - Letter spacing: `var(--letter-spacing-normal)` (0)
  - Line height: `var(--line-height-normal)` (1.5)
  - Opacity: 0.7-0.8 for secondary importance

### Navigation & UI Elements
- Navigation labels: `var(--type-step-3)` (1.5rem / 24px)
  - Font: `var(--font-family-meta)`
  - Weight: `var(--font-weight-medium)` (500)
  - Letter spacing: `var(--letter-spacing-wide)` (0.05em)
  - Text transform: uppercase (for Courier New aesthetic)

- Button text: `var(--type-step-2)` (1.25rem / 20px)
  - Font: `var(--font-family-display)`
  - Weight: `var(--font-weight-semibold)` (600)
  - Letter spacing: `var(--letter-spacing-normal)` (0)
  - Line height: `var(--line-height-normal)` (1.5)

## Responsive Typography Breakpoints

Following mobile-first approach from design-taste-frontend:
- Mobile (< 800px): All type scales reduced by approximately 30-40% as per DESIGN_SPEC.md
- Tablet (800px-1200px): Intermediate scaling
- Desktop (> 1200px): Full scale as defined above

Specific mobile adjustments from DESIGN_SPEC.md:
- Hero headline: 54-96px (vs 85-146px desktop)
- Section headlines: proportionally reduced
- Body text: proportionally maintained readability

## Implementation Guidelines

### CSS Variables Example
```css
:root {
  /* Type scale */
  --type-step-0: 1rem;
  --type-step-1: 1.125rem;
  --type-step-2: 1.25rem;
  --type-step-3: 1.5rem;
  --type-step-4: 2rem;
  --type-step-5: 2.5rem;
  --type-step-6: 3rem;
  --type-step-7: 4rem;
  --type-step-8: 5rem;
  --type-step-9: 6rem;
  --type-step-10: 7rem;
  --type-step-11: 8rem;
  --type-step-12: 9rem;

  /* Font families */
  --font-family-display: 'Arial', 'Helvetica', sans-serif;
  --font-family-body: 'Arial', 'Helvetica', sans-serif;
  --font-family-accent: 'Georgia', serif;
  --font-family-meta: 'Courier New', monospace;

  /* Font weights */
  --font-weight-light: 300;
  --font-weight-regular: 400;
  --font-weight-medium: 500;
  --font-weight-semibold: 600;
  --font-weight-bold: 700;
  --font-weight-extrabold: 800;

  /* Line heights */
  --line-height-tight: 1.2;
  --line-height-normal: 1.5;
  --line-height-relaxed: 1.75;

  /* Letter spacing */
  --letter-spacing-tight: -0.02em;
  --letter-spacing-normal: 0;
  --letter-spacing-wide: 0.05em;
}
```

### Usage Principles (from design-taste-frontend)
1. Limit to two typefaces maximum (we're using three but with specific roles: display/body same, accent different, meta different)
2. Headlines should never exceed two lines at any width
3. Body text should be 16px or minimum for readability
4. Use semantic styling rather than font-specific classes
5. Maintain vertical rhythm through consistent line heights
6. Ensure sufficient contrast between text and backgrounds

### Fallback Strategy
Since we're using system fonts, we have excellent fallbacks built-in:
- Arial → Helvetica → sans-serif
- Georgia → serif
- Courier New → monospace

This approach satisfies the requirement to avoid remote requests while maintaining typographic quality.
# Sunlit Shore Color System

## Approved Palette (from DESIGN_SPEC.md)

Based on the approved design specification, Sunlit Shore uses the following color tokens:

| Token | Value | Purpose |
|-------|-------|---------|
| Ocean | `#00BCCD` | Water primary |
| Shallow | `#75E3DF` | Near-shore water |
| Sand | `#FFF0CB` | Warm content background |
| Foam | `#FFFDF4` | Highlights and card paper |
| Sun | `#FFB950` | Warm accent |
| Deep ocean ink | `#07515D` | Text on cyan |
| Sand ink | `#39352F` | Text on cream |
| Coral accent | `#FF7858` | Selected typography, icons |

## Semantic Color Roles

Following the principles from the design-taste-frontend skill, we map these colors to semantic roles for consistent application:

### Ground Colors (Backgrounds)
- `--color-ground-primary`: `#FFF0CB` (Sand) - Main content background
- `--color-ground-secondary`: `#FFFDF4` (Foam) - Elevated surfaces, cards, highlights
- `--color-ground-accent`: `#FFB950` (Sun) - Accent backgrounds, interactive elements

### Ink Colors (Text & Primary Content)
- `--color-ink-primary`: `#39352F` (Sand ink) - Primary text on light backgrounds
- `--color-ink-secondary`: `#07515D` (Deep ocean ink) - Text on water backgrounds
- `--color-ink-muted`: `#6b5b51` (adjusted from design-taste) - Secondary text, captions

### Accent Colors
- `--color-accent-primary`: `#FFB950` (Sun) - Primary accent, buttons, highlights
- `--color-accent-secondary`: `#FF7858` (Coral accent) - Selected states, icons, typography accents
- `--color-accent-water`: `#00BCCD` (Ocean) - Water-related accents, interactive water elements

### Water Colors (Specialized)
- `--color-water-primary`: `#00BCCD` (Ocean) - Main water color
- `--color-water-shallow`: `#75E3DF` (Shallow) - Near-shore, shallow water
- `--color-water-deep`: `#07515D` (Deep ocean ink) - Deep water, text contrast

## Usage Guidelines

### Background Applications
- Primary content areas: Use `--color-ground-primary` (Sand)
- Cards and elevated surfaces: Use `--color-ground-secondary` (Foam)
- Interactive elements (buttons, links): Use `--color-ground-accent` (Sun) on hover/active states
- Background sections: Alternate between Sand and Foam for visual rhythm

### Text Applications
- Primary body text: `--color-ink-primary` (Sand ink) on Sand/Foam backgrounds
- Secondary text/captions: `--color-ink-muted` at 60-70% opacity
- Text on water backgrounds: `--color-ink-secondary` (Deep ocean ink) on Ocean/Shallow backgrounds
- Inverted text (on Sun accent): `--color-ground-primary` (Sand) or `--color-ground-secondary` (Foam)

### Accent Applications
- Primary buttons, active states: `--color-accent-primary` (Sun)
- Selected items, active tabs: `--color-accent-secondary` (Coral accent)
- Water interactions, wave highlights: `--color-accent-water` (Ocean)
- Icons and small decorative elements: `--color-accent-secondary` (Coral accent)

### Border and Outline Applications
- Subtle borders: `--color-ink-muted` at 20-30% opacity
- Defined borders: `--color-ink-primary` (Sand ink) at 50% opacity
- Interactive borders: `--color-accent-primary` (Sun) on hover/focus
- Water element outlines: `--color-accent-water` (Ocean) with low opacity

## Implementation Notes

Following the design-taste-frontend skill principles:
1. Use CSS custom properties for all color values
2. Apply colors semantically rather than using raw hex values in components
3. Ensure sufficient contrast ratios (WCAG AA minimum 4.5:1 for normal text)
4. Test color combinations for accessibility, especially text on backgrounds
5. Limit the use of accent colors to maintain visual hierarchy

## CSS Variables Example

```css
:root {
  /* Ground colors */
  --color-ground-primary: #FFF0CB; /* Sand */
  --color-ground-secondary: #FFFDF4; /* Foam */
  --color-ground-accent: #FFB950; /* Sun */
  
  /* Ink colors */
  --color-ink-primary: #39352F; /* Sand ink */
  --color-ink-secondary: #07515D; /* Deep ocean ink */
  --color-ink-muted: #6b5b51; /* Muted */
  
  /* Accent colors */
  --color-accent-primary: #FFB950; /* Sun */
  --color-accent-secondary: #FF7858; /* Coral accent */
  --color-accent-water: #00BCCD; /* Ocean */
  
  /* Water colors */
  --color-water-primary: #00BCCD; /* Ocean */
  --color-water-shallow: #75E3DF; /* Shallow */
  --color-water-deep: #07515D; /* Deep ocean ink */
}
```
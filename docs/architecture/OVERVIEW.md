# Architecture Overview

## Boundaries

- **Spatial Canvas**: A website-wide spatial canvas that houses interactive elements.
- **Project Gallery**: A bento grid layout showcasing projects.
- **Hybrid Postcard**: Minimal project cards with playful interactions.
- **Directional Water Wake**: A stylized water effect responding to cursor movement.
- **Modular Components**: UI built with React and TypeScript, following a feature-based structure.
- **State Management**: To be determined based on complexity (prefer React Context or lightweight solutions).
- **Styling**: CSS modules or styled-components for scoped styles, with a focus on performance.
- **Assets**: Optimized images, icons, and textures stored in `public/assets`.

## Technical Stack

- React 18+
- TypeScript
- Vite (build tool)
- TODO: Additional libraries as needed (e.g., for animations, gestures)

## Performance Considerations

- Code-splitting and lazy loading of features.
- Minimizing JavaScript bundle size.
- Efficient rendering of the spatial canvas and water wake.
- Accessibility-first development (WCAG 2.1 AA).
# Rendering Strategy Decision

## Date: 2026-10-16

## Evaluation

We evaluated PixiJS for implementing the Water Wake and spatial canvas interactions in Sunlit Shore.

### Considerations

- **Bundle Size**: PixiJS adds approximately 200KB minified (or more with plugins), which could impact initial load performance.
- **Performance**: PixiJS is a powerful 2D rendering engine that offers good performance for complex scenes, but for the intended Water Wake (a stylized cursor-triggered effect) and spatial canvas (likely a combination of CSS transforms and canvas drawing), lighter alternatives may suffice.
- **Maintainability**: Introducing PixiJS requires learning its API and managing its lifecycle. For simple effects, native Canvas 2D or CSS-based solutions may be easier to maintain.
- **Feature Requirements**: The Water Wake is described as a "stylized Directional Water Wake responding to cursor movement." This can likely be achieved with Canvas 2D using simple line drawing or with WebGL shaders if more advanced fluid simulation is desired. However, the design emphasizes performance-first and code-first visuals without AI image generation, suggesting that a lightweight solution is preferred.

### Decision

We will **not** install PixiJS as a runtime dependency during the setup phase. Instead, we will proceed with native web technologies:

- For the spatial canvas: Use CSS transforms and positioning for layout, and potentially Canvas 2D for custom drawing if needed.
- For the Water Wake: Implement using Canvas 2D to draw lines or shapes that follow the cursor, or use SVG for simpler effects.

If during the design phase it becomes evident that PixiJS provides significant benefits (e.g., complex particle systems, performance advantages for large numbers of sprites), we will revisit this decision and document the change in a subsequent decision record.

### Next Steps

- Implement prototype interactions using Canvas 2D and measure performance.
- Evaluate if PixiJS becomes necessary based on actual implementation challenges.

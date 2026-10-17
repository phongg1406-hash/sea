# Sunlit Shore - Claude Code Guidelines

## Principles

1. Read the relevant project documentation before changing code.
2. Respect the approved Sunlit Shore concept.
3. Prefer maintainable, minimal solutions.
4. Avoid unnecessary abstraction and dependencies.
5. Use TypeScript with strict typing.
6. Follow accessibility and responsive design requirements.
7. Treat performance as an architectural requirement.
8. Prefer native browser capabilities when sufficient.
9. Do not add 3D engines or full fluid simulations without demonstrated need.
10. Do not assume image recognition or image generation is available.
11. Never modify unrelated files.
12. Run appropriate checks after each implementation task.
13. Report changes, tests, remaining issues, and next steps.
14. Never claim a feature is working without verification.
15. Do not begin implementation without an explicit follow-up instruction.

## Skill Selection Policy

Skills should be invoked by task relevance rather than loading every skill indiscriminately.

- **Superpowers**: planning, testing, debugging.
- **Ponytail**: simplicity and avoiding overengineering.
- **UI UX Pro Max**: design-system research and UI planning.
- **Taste Skill**: frontend aesthetic quality.
- **Impeccable**: UI quality checks and refinement.
- **Vercel React Best Practices**: React performance.
- **Web Design Guidelines**: accessibility and UI audits.
- **Emil Kowalski**: motion-specific tasks.
- **PixiJS**: only if its rendering stack is adopted (see docs/decisions/0002-rendering-strategy.md).

## Skill-Routing Policy for Sunlit Shore Project

Based on `docs/DESIGN_SPEC.md` priorities and verified project skills, use this policy to select and invoke relevant skills before implementation:

### Task-Based Skill Selection

#### 1. Planning, Debugging, Testing Workflows
   - **Skills**: Superpowers (planning, systematic-debugging, test-driven-development, receiving-code-review, etc.)
   - **When**: Before any implementation, when encountering bugs, writing tests, or reviewing code
   - **Example**: `superpowers:systematic-debugging` for test failures, `superpowers:test-driven-development` before feature implementation

#### 2. Interface Design & UI/Quality
   - **Skills**: `ui-ux-pro-max` (primary), `design-taste-frontend` (for public-facing pages), `impeccable` (for refinement)
   - **When**: Designing/building interfaces, reviewing UX/accessibility/visual quality, implementing design systems
   - **Priority**: Prioritize `docs/DESIGN_SPEC.md` requirements over generic suggestions
   - **Example**: Use `ui-ux-pro-max` for spatial canvas layout, responsive breakpoints, accessibility compliance

#### 3. Motion Design & Performance
   - **Skills**: `animate` (core), `animation-performance` (performance), `animation-vocabulary` (naming), `find-animation-opportunities` (identification)
   - **When**: Implementing Water Wake, hover/lift effects, module transitions, motion performance optimization
   - **Constraint**: Respect `prefers-reduced-motion`; animation is optional per spec
   - **Example**: Use `animation-performance` to keep wake effects inside frame budget

#### 4. Implementation Reviews
   - **Skills**: `vercel-react-best-practices` (React performance), `web-design-guidelines` (accessibility/UI audits)
   - **When**: Reviewing React/Vite implementation, checking Core Web Vitals, validating accessibility
   - **Example**: Use `web-design-guidelines` to audit WCAG AA contrast, focus management

### 5. Specialized Skills (Manual Invocation)
   - **Always require explicit user request**: `banner-design`, `brand`, `slides`, `ui-styling`
   - **Conditional**: PixiJS skills remain disabled unless explicitly selected as rendering dependency
   - **Never auto-invoke**: Skills conflicting with SPEC (e.g., ocean simulators, 3D engines, photorealistic textures)

## Additional Notes

- Keep changes surgical and goal-driven.
- Define success criteria and loop until verified.
- Simplicity first: minimum code that solves the problem.
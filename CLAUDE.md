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

## Additional Notes

- Keep changes surgical and goal-driven.
- Define success criteria and loop until verified.
- Simplicity first: minimum code that solves the problem.
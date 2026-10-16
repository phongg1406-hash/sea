# Project Initialization Decisions

## Date: 2026-10-16

## Decisions Made

1. **Project Structure**: Initialized a React + TypeScript + Vite project as the technical baseline.
   - Chose Vite for fast development builds and modern ES module support.
   - Selected React with TypeScript for strong typing and ecosystem maturity.

2. **Directory Structure**: Created a scalable folder structure aligned with feature-based organization.
   - Separated concerns into `app`, `components`, `features`, `hooks`, `lib`, `styles`, `types`, `data`.
   - Dedicated folders for spatial canvas, water interaction, project gallery, and playground features.
   - Established `docs/` for architecture, design, decisions, and testing documentation.
   - Set up `public/assets` for static assets (images, icons, textures).

3. **Documentation**: Created initial documentation files:
   - README.md: Project overview and setup instructions.
   - CLAUDE.md: Project-specific guidelines for Claude Code.
   - Architecture overview, design source location, decisions log, and test plan placeholders.

4. **Git Preparation**: Initialized a Git repository (to be connected to GitHub).
   - Created a `.gitignore` file via Vite scaffolding (covers node_modules, dist, etc.).
   - Will configure GitHub remote in the next phase.

5. **Skill Installation Plan**: Planned to install coding skills in `.claude/skills/` for enhanced Claude Code capabilities.
   - Selected skills: Superpowers, Ponytail, UI UX Pro Max, Taste Skill, Impeccable, Vercel React Best Practices, Web Design Guidelines, Emil Kowalski (specific motion skills), and potentially PixiJS (conditional).

## Open Items

- GitHub repository creation and remote configuration.
- Installation of the planned coding skills.
- Validation of skill activation and configuration.
- Baseline validation (build, lint, type checks, dev server).
- Decision on PixiJS usage for Water Wake and spatial interactions (to be documented in 0002-rendering-strategy.md).

## Next Phase

Proceed to GitHub integration and skill installation as outlined in the initialization plan.
# Sunlit Shore — delivery, QA and next steps

## Delivered in this package

| Phase | Outcome | Status |
|---|---|---|
| 01. Concept | Sunlit Shore playful coast concept | Superseded by v2.0 |
| 02. Visual direction | Palette, typography, card behavior | Superseded by v2.0 |
| 03. Spatial architecture | Global 2D world, scene coordinates, mini-map | Superseded by v2.0 |
| 04. Wireframes | Desktop/mobile blueprint (`WIREFRAMES.svg`) | Superseded by v2.0 |
| 05. Water prototype | Lightweight directional wake with time-decay | Superseded by v2.0 |
| 06. Website prototype | Working desktop/mobile interactive HTML/CSS/JS | Superseded by v2.0 |
| 07. Interaction QA | Navigation, project dialog, archive, motion | Superseded by v2.0 |
| 08. Performance | Low-cost design decisions, hard metric targets | Superseded by v2.0 |
| 09. Production content | Name, actual screenshots, bio, verified links | Pending user data |
| 10. Deployment | Domain/hosting/CI production | Not requested, not done |
| v2.0. Concept | Sunlit Shore Vietnam coastal journey concept | Completed |
| v2.0. Visual direction | Playful Brutalism × Coastal Editorial × Stylized Tropical Environment | Completed |
| v2.0. Architecture | Continuous Vertical Coastal Scroll with Geographic Shore Map | Completed |
| v2.0. Wireframes | Desktop/mobile vertical scroll blueprint (`WIREFRAMES.svg`) | Completed |
| v2.0. Water prototype | Directional Water Wake with finger-stir behavior | Completed |
| v2.0. Website prototype | Working desktop/mobile interactive HTML/CSS/JS | Pending implementation |
| v2.0. Interaction QA | Eight-section navigation, project dialog, archive, motion | Pending |
| v2.0. Performance | Low-cost design decisions, hard metric targets | Pending validation |
| v2.0. Production content | Name, actual screenshots, bio, verified links | Pending user data |
| v2.0. Deployment | Domain/hosting/CI production | Not requested, not done |

## Validation completed (v1.0 - superseded)

- Static JS syntax: `node --check app.js` succeeded.
- Headless Chromium/Playwright using injected local HTML, CSS and JS (restricted browser couldn't navigate to localhost or file scheme): initial desktop render, section navigation, project dialog open/close, simulated cursor wake, motion toggle, mobile render, menu links, in-page scrolling, mobile dialog. No browser page errors observed on this run.
- Mobile width 390 px: `scrollWidth > innerWidth` reported false on sampled page state.
- Additional integration checks at widths 360, 390, 768, 800, 801, 1024, 1440 and 1920 px: no horizontal document overflow; desktop drag pan and Archive Grid/List controls worked; no failures reported in those sampled checks.
- Screenshots saved in `tests/desktop-home.png`, `tests/desktop-work.png`, `tests/desktop-playground.png`, `tests/mobile-home.png`, `tests/mobile-work.png`.

These checks are limited. They do NOT certify WCAG, real-world FPS, Core Web Vitals, visual completeness of all sections or broad device compatibility.

## Additional acceptance tests before release (v2.0)

### Functional

- [ ] Replace all sample content, fake mail link, and profile link.
- [ ] Confirm each project metadata entry reflects actual work; verify links.
- [ ] Test pointer scroll through all eight sections and ensure Geographic Shore Map updates correctly.
- [ ] Test project click vs backdrop dragging, including touch and keyboard.
- [ ] Test direct navigation to all eight sections via anchor links and Geographic Map.
- [ ] Test with mouse wheel, trackpad, touch, keyboard and screen reader.
- [ ] Check dialog focus trapping/restoration in major browsers.
- [ ] Verify mobile touch interactions do not interrupt scrolling.
- [ ] Test Vũng Tàu Secret Easter Egg discovery flow.
- [ ] Test Scroll fade-in/fade-out between sections.
- [ ] Test Floating Skill Net interaction in Đà Nẵng section.

### Visual

- [ ] Review 1440×900, 1920×1080, 1024×768, 800×1000, 390×844 and 360×740.
- [ ] Verify that postcard imagery doesn't hide text at narrow widths.
- [ ] Confirm focal point of water, foam and sand is consistent when panning/scrolling.
- [ ] Tune water wake to look like finger motion rather than cursor paint.
- [ ] Test against reduced motion and high zoom (200%).
- [ ] Verify Continuous Vertical Coastal Scroll maintains sand-left/sea-right composition.
- [ ] Confirm Geographic Shore Map shows actual Vietnamese coast locations.
- [ ] Validate Vũng Tàu discovery remains out-of-flow and inaccessible through normal scrolling.
- [ ] Check Floating Skill Net maintains 8-10 visible skill logos on desktop.

### Performance

- [ ] Record LCP, INP, CLS with Chrome DevTools/Lighthouse, separate desktop/mobile budgets.
- [ ] Profile canvas time only when wake active, then confirm RAF stops when idle.
- [ ] Test on an entry-level Windows laptop and midrange mobile phone.
- [ ] Check GPU/compositing layers, memory pressure and heat during prolonged pan/scroll.
- [ ] If FPS drops under sustained motion, reduce wake resolution or fragment count before adding heavy shading.
- [ ] Measure mobile CPU and battery impact, not just peak desktop FPS.
- [ ] Verify code-first artwork principle: no external image generation or photorealistic textures.

## Suggested follow-on delivery phases

**Visual Prototype v2 — Validation:** Build and validate Visual Prototype v2 to confirm twelve specific objectives:
1. Natural vertical scroll behavior
2. Continuous coastline visual flow
3. Eight distinct section layouts
4. Sand-left/sea-right composition with varying proportions
5. Geographic Shore Map functionality
6. Section fade-in/fade-out transitions
7. Geographic transitions between sections
8. Shared Project Detail Modal consistency
9. Floating Skill Net quality and interaction
10. Vũng Tàu Secret Easter Egg discovery flow
11. Responsive layout (mobile ≤800px: vertical reading order)
12. Performance feasibility and accessibility compliance

**Milestone B — Real content:** real screenshots and verified data. Replace mockups as local images without asking the coding AI to understand images.

**Milestone C — Technical hardening:** add tests, accessibility improvements, production routing and verify performance budgets on target hardware.

**Milestone D — Deployment:** connect repository and host. Only do this after the user selects platform and approves actual public-facing content.

## Key risk register

1. **Vertical scroll usability:** users may expect spatial navigation. Mitigation: clear visual cues, Geographic Shore Map as alternative, familiar scroll behavior.
2. **Visual mismatch from text-only AI:** visually correct code cannot guarantee pleasing art direction. Mitigation: user previews screenshots/browser at milestones; all layout dimensions are explicit.
3. **Wake realism vs cost:** elaborate liquid solver is tempting and expensive. Mitigation: keep directional trail baseline, add deformation only if profiling justifies.
4. **Content trust:** illustrative project cards could look like actual claims. Mitigation: label placeholders in UI, verify projects before launch.
5. **Accessibility of vertical interfaces:** ensure keyboard navigation and focus management work correctly. Mitigation: semantic DOM, focusable native controls, visible focus indicators.
6. **Discovery flow complexity:** Vũng Tàu Easter Egg may be too obscure or too obvious. Mitigation: user testing of discovery flow, clear but subtle hints.
7. **Section transition smoothness:** fade effects may impact performance. Mitigation: lightweight CSS transitions, performance testing.

# FE50 complex-situation review · judgement column (written by the AI, rewritten as a whole)

## 1. The user's verbatim words in the human-input window

- "workspace\QWEN 3.8 MAX\FE50" contains an XRD dataset; it is a Prussian blue crystal with nominal formula KxFe0.5Mn0.5[Fe(CN)6], synthesized by ball-milling Fe4[Fe(CN)6]3, manganese oxide tetrahydrate, and potassium citrate in 50% ethanol/water.
- "workspace\QWEN 3.8 MAX\FE50" provides two similar-material CIF files as reference.
- "The material should be considered to contain extensive defects, especially lattice distortion, vacancies, and split sites."
- "Process strictly following the xrd plugin, force the complex-case checklist, strictly follow the planned workflow, and consider all defects and possible fitting changes."
- "When in doubt, first consider the fitting approach and scientific self-consistency; before entering the final GSAS engine, all adjustments target lowering R."
- "The target is publication-level (R ≤ 10) as far as possible. Save the work under the data folder."
- Stage-1 question answers (options): manganese precursor = "manganese oxide (MnO/Mn2O3/MnO2 etc.)"; composition characterization = "none, treat by the nominal formula"; ball-milling medium = "agate SiO2".
- "Continue" (after the xrd_refine_manual v3 tool-budget timeout).

## 2. Current best physical solution

- **Main-line project: FE50/gsas/gsas_proj_continued.gpx (=T18+T19), wR=9.419 (GSAS protocol), REVIEW=pass (warn: N Uiso 0.256>0.2 soft threshold)**. The target ≤10 is achieved and this is a chemically legal solution.
- Structure: **monoclinic P2₁/c**, a=10.1228 b=10.1247 c=10.1266 Å β=92.606° V=1036.8; composition **K₁.₉₄Fe₀.₅Mn₀.₅[Fe(CN)₆]** (framework [Fe(CN)₆] fully occupied, N coordination full, K occ pinned at the physical value 0.9691); C/N coordinates take the literature values (the idealized geometry is instead worse at 11.10, and the free relaxation collapsed chemically at 8.97 and was discarded); **the ball-milling static disorder is expressed as C/N Uiso: C 0.139 / N 0.256 (positive values, N/C≈1.8 = the CN-bridge-wobbling disorder picture)**; K Uiso 0.0485.
- Peak shape: TCH + Size (isotropic, ~nm) + Mustrain (isotropic, -0.02 slight gain already adopted); inst U/V/W/X/Y/Zero refined; Size↔X 100% collinearity recorded.
- Background: 80-point lin-interpolate **fixed** (the manual-engine bg+extras curve, including the 10-15°/28-32° amorphous broad humps); the final background treatment will be done at close-out and disclosed.
- Manual-engine corroboration: mono_h1 Rwp 10.58 (converged, occ_K pinned at the upper bound = another independent piece of evidence for near-full K occupancy); cubic h1 11.59.

## 3. Unresolved hypotheses (item by item)

1. **T20 K₂CO₃ second phase (in progress)**: manual-engine ΔRwp -0.03~-0.06 is insufficient evidence; re-judging with add_phase on the clean T18 baseline (one of the alternative explanations for the "cavity excess scattering" requirement).
2. K split site D-07 re-measured on the physical T18 baseline (T12/T13 were measured on the abandoned T7b baseline: free 0.5Å Δ-0.012 / constrained 1.5Å +0.27) — this dimension must be closed after re-running on the new baseline.
3. Anisotropic broadening D-14: isotropic Mustrain is only -0.02; if the residual is still clustering at 42-45° after T20, try the anisotropic model.
4. Final background treatment: currently a fixed imported curve; at close-out try auto_background order escalation (switch only if it improves, and disclose the numbers of both schemes).
5. Physicality statement for N Uiso 0.256: an effective parameter of static disorder (warn level, not fail); alternative = cap N U at 0.20 and see the wR cost (measure once before close-out, for the report to disclose).
6. Full-pattern impurity re-screening after residual sharpening (phase_screen residuals on the main-line gpx) — complementary to T20.
7. V3/V4 image reading (residual morphology and delivery-figure hygiene) has not yet been done for the main-line state.

## 4. Branch list

| branch | Status | R |
|---|---|---|
| **T18→T19 monoclinic GSAS (gsas_proj_continued.gpx)** | **main line = current best** | wR 9.419 |
| T14c literature coordinates + full clamping | superseded by T18 (Uiso release adopted) | 10.582 |
| T17 ideal CN geometry | rejected (over-constrained) | 11.097 |
| T7b free C/N coordinates | **discarded (chemical collapse, bond-length audit fail)** | (8.972 invalid) |
| T15/T15b water | rejected (unphysical occupancy/negative occupancy) | 10.40 invalid |
| T16a extinction / T16b preferred orientation | no gain, not adopted | 10.545/10.587 |
| T12/T13 K split (T7b baseline) | numerically not adopted; new-baseline re-test queued | 8.960/9.242 |
| cubic Fm-3m manual series | retained as comparison | 11.586 snapshot |
| manual second phase KHCO₃/MnCO₃/Mn₃O₄ | rejected (scale→0) | =baseline |
| fp2k ladder | abandoned (tail-dragging trap archived) | 70.4/73.7 invalid |
| rhombohedral R-3/supercell | fallback not started (main line meets the target) | — |

## 5. Current freeze status

- **No freeze**. no_improve_streak=0 (T18 -1.14 large improvement, T19 -0.02 improvement); limit_mode_attempts=0; the target ≤10 is achieved (9.419).
- GSAS trajectory: 18.30→17.91→12.96→12.50→12.48→12.38→11.92→11.97→[9.96 chemically collapsed, discarded]→10.58 (honest baseline)→**9.44 (T18)→9.42 (T19)**.
- Remaining work in order: T20 second phase → D-07 new-baseline re-test → final background treatment → residual re-screening → V3/V4 image reading → export/finalize delivery → report (including the coverage statement) → close-out cleanup (ask the user).

(Updated 2026-10-10 ~08:40, after T19 / before T20)

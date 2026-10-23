# journal.md — Fe2O3_Fe3O4 two-phase sample XRD refinement overview (generated from journal.jsonl)

round | engine | stage/level | model | Rwp | baseline | verdict | why | artifacts
--- | --- | --- | --- | --- | --- | --- | --- | ---
0 | visual + numerical peak picking | stages 1-3 | - | - | - | phase determination complete | all peaks of the hematite main phase + magnetite weak phase matched; CIFs built with build_orbit from literature and double-validated | xrd_workflow/pattern_2theta_fit.png; two CIFs
0.5 | cif_to_pcr+fp2k | 4-Ⅰ | physics | 8.99 (single phase) | 98.6 | both structures verified | origin-choice trap found and resolved; pcr data-range line manually corrected | work/fp/*.pcr
1 | xrd_refine_manual | 4-Ⅱ twophase | physics | 96.42 | 99.73 | rolled back (re-run) | default vary had no background terms, both scales at the upper bound | work/manual/result.json
2 | xrd_refine_manual | 4-Ⅱ twophase | physics | **2.30** | 99.73 | both phases settled | flags empty; hematite a=5.04717; magnetite scale=17.98 non-zero; handoff gate passed | work/manual/r2/result.json
3 | xrd_refine_gsas | 4-Ⅲ handoff ladder | physics | 2.692 | 99.73 | wR on target but negative Uiso to be fixed | 8 steps, 7 accepted, 1 rolled back; hematite Fe1/O2 negative Uiso violates the delivery red line; the instprm double-comment bug was cleared | work/gsas/gsas_proj.gpx
4 | xrd_gsas_ops | 4-Ⅲ uiso clamping | physics | 2.711 | - | physical compliance achieved | negative Uiso clamped to 0.005, at a cost of 0.02; review pass | work/gsas/gsas_ops_out.gpx
5 | xrd_refine_gsas | 4-Ⅲ final refinement | physics | **2.347** | - | **on target (wR 2.35<<10)** | inst (U/V/W/X/Y/Zero) refined into place; phase fractions 64.7/35.3 wt% | work/gsas/gsas_proj_continued.gpx
6 | gsas python | D2 defect discrimination | physics | 2.3401 | - | no B-site vacancies | Fe2(16d) occupancy pushed to 1.100(24), i.e. "more than fully occupied", the opposite direction to γ-Fe2O3 vacancies and physically illegal; stoichiometric Fe3O4 confirmed; the physical model has been restored | work/gsas/Fe2O3_Fe3O4_physical.gpx
7 | xrd_finalize | 5 delivery | physics | 2.35 | - | delivery package generated | clean gpx+lst+two-phase CIFs+figure+report; V4 visual inspection passed | Fe2O3_Fe3O4_final/

## Material and target
- Sample: a weighed two-phase mixture of α-Fe2O3 (hematite) + Fe3O4 (magnetite), source Zenodo 14959531 (the original file name implies 70-30, but it is treated as a blind test and not presupposed).
- Data: Panalytical X'Pert PRO, Bragg-Brentano, Cu Kα doublet (1.54056/1.54439/0.5, no monochromator), 10.013–119.967°, step 0.026°, 4230 points.
- Target (user): publication-grade refinement, R ≤ 10. **Achieved: GSAS-II wR = 2.35%, R = 1.76%**.

## Phases and crystal families (conclusion + evidence + the families excluded and why)
- **Main phase α-Fe2O3 hematite, R-3c (hexagonal)**: all peaks matched at 24.3/33.3/35.8/41.0/49.6/54.2/64.1°; refined a=5.03666(36) c=13.7543(8) Å agrees with the Maslen (1994) literature values 5.0356/13.7489 (<0.04%). wt% = 64.73(67).
- **Second phase Fe3O4 magnetite, Fd-3m inverse spinel (origin choice 2)**: characteristic peaks 18.4/30.3/37.2/43.3/53.6/57.2° all present; refined a=8.38713(65) Å; isotropic microstrain 4248(306)×10⁻⁶ (the physical origin of its peaks being broader than those of hematite); the D2 occupancy discrimination confirms stoichiometry (no B-site vacancies). wt% = 35.27(67).
- Excluded: γ-Fe2O3 (maghemite, B-site-vacancy type) — the Fe2(16d) occupancy is pushed by LS to 1.100(24) (more than fully occupied, physically illegal), the opposite direction to the vacancy hypothesis, so partial oxidation is excluded; FeO and other iron oxides — no corresponding peaks.
- Structure source: the MP/COD candidates were of poor quality (1926 rough cell/high-pressure structure/primitive-cell coordinates), so build_orbit was used instead to build them from literature ambient-pressure values (hematite Maslen1994; magnetite Fleet1981), and validate + Fe-O coordination double verification passed.

## Defect summary table (enumerate → screen → execute)
| Hypothesis | Verdict | Evidence | Execution |
| --- | --- | --- | --- |
| Magnetite B-site vacancies (partial oxidation→γ-Fe2O3) | **not applicable (does not exist)** | D2 single variable: Fe2 occ→1.100(24), the direction is opposite to vacancies and >1 is illegal; ΔwR 0.007, a noise-level value | GSAS actually run (round 6) |
| Magnetite cation inversion/co-occupancy | not applicable | a stoichiometric weighed mixture, no evidence of inversion; the A/B site occupancy tests compensate each other and are degenerate with Scale (93.97% correlation), which is not evidence of a defect | GSAS actually run (multi-occupancy control) |
| Hematite Fe/O occupancy defects | not applicable | occ→1.0001/1.0035 ≈1, no information | GSAS actually run (control) |
| Third-phase impurity | not applicable | no unexplained peaks in the residuals (the residual spikes are all at already-modelled peak positions) | V3/V4 numerical residual analysis |
| Insufficient background order | not tried (not needed) | wR 2.35 already far exceeds the target; a 6th-order background is already fitted; raising the order is a conditional escalation action | not executed (reason sufficient) |
| Preferred orientation | not tried | both phases are powder weighed mixtures, and the residuals show no systematic orientation features | not executed |

## Results achieved (R and convention written separately)
- **GSAS-II convention (delivered)**: wR = **2.35%**, R = 1.76%, Rb = 2.57%, wRmin = 0.89%, GOF = 2.63, DW = 0.176 (4230 observations, 18 parameters).
- Manual-engine convention (corroboration): Rwp = 2.30 (Rexp 0.89).
- fp2k single-phase scoring (structure verification only): hematite single phase 50.5 / magnetite single phase 8.99 (its complex background absorbed the main-phase peaks, so only the peak positions are verified).
- FullProf density sentinel: the magnetite pcr density 5.195 g/cm³, a=8.3967, consistent with the structure (Rwp 99.4 is a picture of an unrefined state and does not enter the conclusions).
- Phase fractions (GSAS): hematite **64.73(67) wt%** + magnetite **35.27(67) wt%**.
- Refined structure: hematite Fe z=0.35522(24), O x=0.31514(222), a=5.03666(36)/c=13.7543(8); magnetite a=8.38713(65) (contracted by 0.11% relative to Fleet 8.3967, not caused by vacancies, reported as-is according to its esd); the Uiso values are all nominal (hematite clamped at the 0.005 lower bound, magnetite 0.01; releasing them immediately goes negative/worsens wR — a limitation of the data's information content).

## Not tried · unresolved items
- **Not tried**: ① SH/L axial-asymmetry refinement and sample displacement (Shift) — the remaining mismatch at GOF 2.63 is mainly peak-shape detail, and both are expected to lower GOF further, but the target is already far exceeded (wR 2.35 vs ≤10), so no further iteration was done; ② background-order upgrade (bg_scan/auto_background iterate) — not executed for the same reason; ③ preferred orientation (March-Dollase) — no evidence of orientation; ④ anisotropic size/strain broadening — the magnetite isotropic microstrain is already modelled.
- **Unresolved**: ① the physical explanation of the 0.11% (15σ) magnetite a contraction (a real cell difference / microabsorption effect / residual peak-shape detail); comparison is recommended when characterisation data for this sample are available (e.g. Fe²⁺/Fe³⁺ titration or Mossbauer); ② phase fractions 64.7/35.3 vs the 70-30 implied by the source file name — the refined values are authoritative, and the difference may come from weighing or from microabsorption (Brindley effect); no absorption correction was applied.
- Bound-hit record: round 1 (manual engine) both scales at the upper bound 50 — the R value of 96.42 from that round is invalid and it was re-run; round 6 occupancy 1.100 out of bounds — this is a discriminative test (expected), and the physical model has been restored.

## Suggestions for the next handler
1. If GOF is to be pushed further down (currently 2.63 → theoretical 1.0): release SH/L (gsas_ops set_hist Instrument Parameters) and Sample Parameters Shift (sample height); the residual spikes are expected to converge markedly; working projects `work/gsas/Fe2O3_Fe3O4_physical.gpx` (physical model state) or `work/gsas/gsas_proj_continued.gpx`.
2. To publish thermal parameters: stronger high-angle data or neutron data are needed; the current Uiso values are nominal (as noted in the report).
3. Microabsorption (Brindley) correction can correct the phase fractions by ~1-2 wt% (Fe absorption is strong, BB geometry); it can be added if strict quantification is required.
4. Tool pitfalls (reusable across samples): ① magnetite/spinel structures sent to FullProf must use origin-2 coordinates (FeA ⅛,FeB ½,O x≈0.2548), while pymatgen/GSAS use origin-1 (FeA 0,FeB ⅝,O x≈0.3798); GSAS-II reads the CIF symmetry-operation block and automatically applies the 1→2 translation; ② the pcr from cif_to_pcr needs Thmin/Step/Thmax manually changed to the actual data values (the converter's default is 11/0.02/120); ③ a GSAS instprm allows only one comment line (ReadInstprm parsing pitfall: two consecutive comment lines → split crash); ④ the manual engine's twophase stage default vary does not include background terms, so bg0 must be given explicitly; ⑤ when handoff is passed to xrd_refine_gsas the ladder may not contain an inst step, so the instrument parameters need a separate additional refinement.

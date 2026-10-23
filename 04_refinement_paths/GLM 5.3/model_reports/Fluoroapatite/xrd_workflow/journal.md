# FAP refinement journal overview (journal.md — generated from journal.jsonl)

| round | engine | stage/level | model | R | baseline | verdict | why | artifacts |
|---|---|---|---|---|---|---|---|---|
| 1 | xrd_refine_auto | 4-Ⅰ-scoring | physics | 100.0 | 100.0 | no discrimination | score-only refines no parameters, all 4 candidates 100–114 | 4 sets of .fp2k-work-* |
| 2 | xrd_refine_auto | 4-Ⅰ-adjudication | physics | 92.3 | 100.0 | all failed | 1010996/1533064 wrong cell (peak positions +0.05°); for 1549763/mp the scale step was pushed to 1e-9, the background blew up to 398–759, and V,U became NaN | 4 sets of fp2k_result.json |
| 3 | xrd_refine_auto | 4-Ⅰ-diagnosis | physics | 100.0 | 100.0 | diagnosis complete | scale scan fixes the optimum at ≈1.1e-3; 1549763 cell aligned; Caglioti measured 0.0629/−0.0635/0.0232 | probe_s3.prf etc. |
| 4 | xrd_refine_auto | 4-Ⅱ-M1 | physics | 58.0 | 100.0 | progress | **three-column dat (σ) fixed the weight degeneracy** + manual code (bg1-3+scale+zero refined together) 100→58 | eed193 end |
| 5 | xrd_refine_auto | 4-Ⅱ-M2 | physics | 32.6 | 100.0 | progress | +cell a/c → 9.3703/6.8848 | 5cddff end |
| 6 | xrd_refine_auto | 4-Ⅱ-M3 | physics | 32.5 | 100.0 | progress (slight) | +W (initial value already near optimal) | 9e71e2 end |
| 7 | xrd_refine_auto | 4-Ⅱ-M4 | physics | 29.3 | 100.0 | progress | +background orders 4–6 | a6f10a end |
| 8 | xrd_refine_auto | 4-Ⅱ-M5 | physics | 25.4 | 100.0 | progress | +V,U (components narrow after Kα2 subtraction) | a6b09f end |
| 9 | xrd_refine_auto | 4-Ⅱ-M6 | physics | **18.7** | 100.0 | progress (fp2k optimum) | +X Lorentzian component; V3: what remains = strong-peak intensity mismatch | a15868 end + M6_fit.png |
| 10 | xrd_refine_auto | 4-Ⅱ-M7 | physics | 20.6 | 100.0 | rolled back | all coordinates (13) diverged (.new) | 531359 end |
| 11 | xrd_refine_auto | 4-Ⅱ-M7a | physics | 21.0 | 100.0 | rolled back | cation coordinates in batches still diverge; single-crystal-grade coordinates already near optimal | a3f892 end |
| 12 | xrd_refine_auto | 4-Ⅱ-M8 | physics | 21.4 | 100.0 | rolled back | PO (March-Dollase) diverged; the intensity problem handed over to GSAS | 6eef42 end |
| 13 | xrd_refine_auto | 4-Ⅱ-M9 | physics | 22.5 | 100.0 | rolled back; **R-value basin** | Biso also diverged; all 4 families failed ⇒ fp2k basin = 18.7, switch to stage Ⅲ GSAS-II | ec13c6 end |
| 14 | xrd_refine_gsas | 4-Ⅲ-build | physics | 41.22 | 100.0 | progress | **instprm root cause fixed** (official template with Type:PXC/I(L2)/I(L1)); bg 50.12→cell 49.33→profile 41.22; opening all atoms was rejected | gsas_proj.gpx |
| 15 | xrd_refine_gsas | 4-Ⅲ-inst | physics | 30.28 | 100.0 | progress | +inst (U,V,W,X,Y,Zero); cell 9.3738/6.8881 | gsas_proj_continued.gpx |
| 16 | xrd_refine_gsas | 4-Ⅲ-atoms-accident | physics | 69.38 | 100.0 | rolled back; accident | scale unstable + atom coupling diverged, the cell was pulled far off (11.71); a gap in `hold` rollback across calls | (discarded) |
| 17 | xrd_gsas_ops | 4-Ⅲ-rebuild | physics | 10.26 | 100.0 | progress | from the clean 41.22 state +Sample scale +inst → 10.26; cell 9.3704/6.8849 consistent with the fp2k basin; Size;i↔X 100% correlated, to be handled | gsas_rebuild.gpx |
| 18 | xrd_gsas_ops | 4-Ⅲ-final-families | physics | **9.75** | 100.0 | progress; **target achieved** | turning off Size refinement→PO(001, ratio≈1 no significant PO)→Ca/P coordinates 10.07→O coordinates 9.97→Biso 9.75; all Uiso positive 0.012–0.022; review pass | gsas_final.gpx |
| 19 | finalize+export | 5-delivery | physics | 9.75 | 100.0 | **delivered** | FAP_final/ delivery package; wR=9.75, R=7.66, GOF=1.74; bond lengths pass (Ca-F 2.302 / Ca-O 2.34–2.51 / P-O 1.52–1.57); V4 visual inspection passed | FAP_final/ |

## Material and target
- Sample: fluoroapatite ore powder Ca5(PO4)3F (raw data raw/FAP.XRA, GSAS-II tutorial data); Cu Kα doublet (1.5405/1.5443/0.5, self-declared in the data header); 15–130.02°, 5752 points.
- Target (confirmed by the user): full structure refinement (publication grade) — cell/coordinates/occupancies/Biso + the three-piece set; reference target Rwp ≲10% (inferred from the data quality).

## Phases and crystal families (conclusion + evidence + the families excluded and why)
- **Main phase: fluoroapatite Ca5(PO4)3F, P6₃/m (No.176), single phase**.
- Evidence: all 40 picked peaks are explained by this family (31.87=(211), 25.87=(002), 33.10=(300)…); 6-candidate scoring from two databases (xrd_phase_screen) + actual fp2k runs + .prf peak-position evidence: **cod_1549763 (the 2018 natural-FAP single-crystal refined-coordinate family) wins**; the final GSAS whole-pattern refinement converged at wR=9.75 with residuals mainly noise and no systematic remaining peaks ⇒ no resolvable second phase exists.
- Excluded: cod_1010996/1011044 (1930s cell 9.37/6.88 → systematic peak-position shift of +0.05°); cod_1533064 (hydroxyl-fluorapatite F0.4/O0.1, chemistry does not match the "pure phase" target); mp-aaacrvgo (DFT distortion, score 0.68); mp-aaaaajoz (P1 42-atom dump, ladder failure + unconstrained over-parameterisation).
- Structure source: build_orbit built the pure Ca end-member from the 1549763 coordinates (validate pass, min contact 1.535 Å).

## Defect summary table (enumerate → screen → execute)
| Hypothesis | Screening | Execution | Conclusion |
|---|---|---|---|
| [001] preferred orientation | V3 strong-peak intensity mismatch hinted at it | GSAS MD(001) refinement (round 18) | **no significant PO** (ratio≈1, wR unchanged) |
| Coordinates deviate from single-crystal values | fp2k diverged, not adjudicated | GSAS grouped refinement Ca/P→O (round 18) | slight adjustment (Ca2 x −0.0078 vs −0.0072), wR −0.5 |
| Per-atom Biso | fp2k diverged, not adjudicated | GSAS all-atom Uiso (round 18) | all positive 0.012–0.022 (F largest, normal), wR −0.22 |
| Second phase | peak picking + residual screening | no fit needed | not found (the remaining peaks are all at background-noise level) |
| Occupancy defects | pure-phase model with occ=1 converged | no need to release | no evidence (the gap between wRmin=5.61 and wR=9.75 is a normal statistical level) |

## Results achieved (R and convention written separately)
- **GSAS-II convention (delivered): wR = 9.75%, R = 7.66%, Rb = 7.47%, wRmin = 5.61%, GOF = 1.74**.
- fp2k conventional Rwp convention (corroboration): 18.7 (stage Ⅱ basin). The two conventions differ and are not directly comparable.
- Unit cell: a = b = 9.3703(1) Å, c = 6.8849(0) Å, V = 523.524 Å³ (P6₃/m).
- Bond lengths (pymatgen re-check): Ca–F 2.302 Å; Ca–O 2.344–2.509 Å; P–O 1.519–1.573 Å — standard apatite geometry, pass.
- Two-engine cross-validation: fp2k and GSAS independently converge to the same cell (9.3703/6.8848 vs 9.3703/6.8849).

## Not tried · unresolved items (must not be left empty)
- **Not tried**: background-order upgrade iteration (auto_background/bg_scan) — **condition not triggered** (the target was already achieved; per the agreement, the order is raised only when the other parameters are optimised and the target is still not met, so this round is "not needed" rather than "cannot be improved"); LeBail intensity floor (specific to limit mode, not triggered); anisotropic ADP (at this data resolution isotropic is already sufficient, GOF 1.74); absorption/roughness correction (Bragg-Brentano flat-plate sample, not modelled, listed as an approximation item).
- **Unresolved**: a small residual remains at the strong peaks 31–33°/46–50° (observed at V4, small in amplitude, suspected residual peak-shape detail); the true instrument parameters are unknown (started from the INST_XRY.PRM placeholder values and converged by refinement; U/V/W/X have converged but there is no independent instrument calibration to reconcile against).

## Suggestions for the next handler
- To push R further down: first do the background-order upgrade (auto_background iterate) and SH/L asymmetry refinement; next try a second check of isotropic→isotropic+preferred orientation.
- For publication-grade esd: use FAP_final/FAP_final.gpx directly (GSAS-II 5839); the fp2k-side esd is not trustworthy (a skill red line).
- A second-phase search can re-examine the 15–25° residual region at higher sensitivity (currently no evidence).

**§6 checklist**: first complete execution (2026-10-09, between rounds 16–17) — all failures were numerical/in-design rejections; no second-phase/defect features; limit mode not entered (limit_mode_attempts=1).
**Honesty statement**: the target R≲10% has been achieved (9.75%); all failed rounds (10–12, 16) have been faithfully recorded and rolled back; the delivered structure satisfies the physical constraints (all Uiso positive, all occupancies 1, standard bond lengths); the "dimensions not tried" are listed separately above (non-exhaustion statement).

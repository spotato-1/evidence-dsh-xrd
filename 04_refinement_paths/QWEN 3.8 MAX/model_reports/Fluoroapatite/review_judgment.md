# review_judgment.md — Fluoroapatite (judgement column, written by the AI; the mechanical column review_mechanical_FAP.json is maintained by the plugin, do not edit by hand)

## 1. What the user said in the human-input window (verbatim, not paraphrased)

1. "workspace\QWEN 3.8 MAX\Fluoroapatite" contains an XRD dataset; the composition is a fluorapatite ore powder sample. Process the data strictly following the xrd plugin. Save the work under the data folder.
2. Question-box answers (stage 1): fitting objective = "publication-level structural refinement (recommended)"; supplementary information = "none".
3. "Continue" (after one xrd_refine_auto call was interrupted).

## 2. Current best physical solution (delivery state)

- **Main phase**: fluoroapatite Ca5(PO4)3F, P6₃/m (#176), Z=2; CIF source `ref/FAP_modern_orbit_01.cif` (modern experimental coordinates, build_orbit+validate pass).
- **Final GSAS-II project**: `gsas_proj_final.gpx` — **wR=11.50%, GOF=2.06 (Rexp≈5.58), R_Bragg=4.77% (325 reflections)**; cell a=9.37074, c=6.88499 Å, V=523.58 (consistent with the literature); coordinate relaxation 0.001–0.006; Uiso all physical (Ca 0.0217/0.0219, P 0.0216, O 0.0256–0.0261, F 0.0339 Å²); REVIEW pass (0 clamps, 0 negative values, occupancies all 1.0).
- **GSAS ladder trajectory**: bg 30.57 → inst 25.45 → cell 14.40 → scale 13.96 → atoms 11.70 → inst+SH/L 11.691 → (size-only 11.728, noise level) → **auto_background (12/14/16→order 16) 11.498**. The re-fits of cell/scale/atoms and the profile family (joint ×2, size-only ×1) all showed no improvement and were rolled back / accepted as noise.
- **Stage Ⅱ manual-engine plateau**: Rwp=23.212151 (r18/r19/r20 bit-identical); occ_F1→1.0 (D3 shows no fluorine-vacancy direction).
- **Impurity screening (residual of the converged project)**: all 30 residual peaks fall at main-phase Bragg positions, with no out-of-phase peaks ⇒ **no detectable second phase found**.
- **Correlation warnings (final lst/ops log)**: `0:0:Size;i ↔ :0:X @100%` (Size is fully collinear with the anisotropic parameter — the reason the profile family was repeatedly ineffective); `:0:Scale` likewise shows a 100% correlation warning (coupled with background/scale, the value itself is stable).
- **Engine-level faults and workarounds (recorded)**: ① the fp2k scale step's LS optimum is negative→clamped to 1e-10 (a real fault, line frozen, leaving only a single-point verification after delivery); ② in the bundled GSAS-II tree the powder instrument Type must be 'XRC' ('XRD'→dmin not bound; 'SXC'→single-crystal twin branch NTL crash).

## 3. Unresolved hypotheses (item by item)

1. **The remaining gap between wR 11.50 and Rexp 5.58**: attributed to the ceiling of the peak-shape model (no real instrument parameter file, starting from a generic placeholder + data self-correction; Size↔X collinearity; anisotropic broadening not modelled) plus the weak residual above the 16th-order background. Within the families already tried there is no further means of improvement; not tried = anisotropic Uij, anisotropic microstrain (generalized mustrain), a mustrain-only single test.
2. **Fluorine occupancy**: kept at stoichiometry (manual occ→1.0 upper bound, no F signature in the GSAS residual); F occ was not released in GSAS for re-checking (listed as a not-tried item).
3. **Trace impurities**: not detected by residual screening; the detection limit is constrained by the main-phase peak-shape residual (a weak impurity peak may be submerged in the ±4500 main-peak residual — stated truthfully).

## 4. Branch list (including frozen ones)

| branch | Status | Description |
|---|---|---|
| GSAS-II line | **converged/delivery state** | gsas_proj_final.gpx wR=11.498; finalize delivery package being generated |
| impurity/second phase | screened = not detected | all 30 residual peaks at main-phase positions |
| manual-engine line | plateau (23.212151) | r9–r20; engine copy xrd_engine_custom.py |
| fp2k line | **frozen (real fault)** | single-point sentinel (density/cell) via xrd_verify_fp2k after delivery |
| profile family | exhausted (joint ×2, size-only ×1 ineffective; Size↔X collinear) | mustrain-only not tried (listed under coverage) |
| 1932-coordinate CIF / MP P6₃ / 1533064 as-is | excluded / coordinates only | see the previous record |
| F vacancy hypothesis | rejected by the manual direction | not re-checked in GSAS (listed as a not-tried item) |
| instprm 'XRD'/'SXC' | abandoned | the correct answer is 'XRC' |

## 5. Current freeze status

- **No freeze**. The GSAS line improved continuously and then converged normally (the last three steps were rollback/noise level), `no_improve_streak` is not counted under the clear-on-convergence-exit semantics; `limit_mode_attempts=0`; the complex checklist was not triggered (stoichiometric mineral, no second phase detected, no input event).

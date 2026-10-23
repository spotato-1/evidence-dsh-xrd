# journal.md — Fluoroapatite (human-readable quick view; close-out version, regenerated in full from journal.jsonl; the authoritative record is jsonl)

## Round table

| Round | Engine | Stage | Model | Rwp | Baseline R | Verdict | Why | Artifacts |
|---|---|---|---|---|---|---|---|---|
| — | record | λ facts | — | — | — | record | Cu doublet 1.540500/1.544300/0.5, from lines 8-9 of the data file header (explicit, measured-data authoritative level) | workflow_state.inputs.wavelength |
| 1 | xrd_refine_auto | Ⅱ-ladder | physical | 92.3 | 100.0 | not at plateau (invalid) | the converter's pcr as-is: phase block Npr=7 (TCHz) pathological peak shape Bragg_R≈90; scale step collapses (→1e-9, code10); coordinates drift unphysically (P1→0.471,0.506); the always-constant shift of the .prf difference column is a display artifact | fp2k/.fp2k-work-*-26f6cd |
| 2 | xrd_refine_auto | Ⅱ-ladder | physical | — | — | interrupted | the tool call was interrupted at step14/15, no result JSON; the leftover .out shows 605 (overshoot state, not counted) | fp2k/.fp2k-work-*-82440c |
| 3 | xrd_refine_auto | Ⅱ-ladder | physical | 64.4 | 120.0 | not at plateau (invalid) | Npr→5; scale still collapses; 64.4 = spurious improvement of Y,X on a calc≈0 state; X (η slope) drives η>1 unphysically above >52°→no R line in later steps | fp2k/.fp2k-work-*-55cfd0 |
| 4 | xrd_refine_auto | Ⅱ-ladder | physical | 83.2 | 123.0 | not at plateau (invalid) | zero=-0.05 + measured UVW + η0=0.5 + X=0; scale collapse as before (independent of initial value/zero) | fp2k/.fp2k-work-*-3a3140 |
| 5 | xrd_refine_auto | Ⅱ-ladder | physical | 83.2 | 124.0 | not at plateau (invalid) | zero=-0.07 (6 isolated peaks aligned to 0.00±0.02°) + Thmax=130.00 (excludes the last-point zero intensity); collapse as before; s*=+1.03 proves the baseline state is healthy | fp2k/.fp2k-work-*-4ea684 |
| 6 | xrd_refine_auto | Ⅰ-diagnosis | physical | 100.0 | 124.0 | diagnosis complete→switch backend | controlled variables exhausted (code 1/11, scale 1e-4/1.5e-3/1e-2, Npr 5/7, AsyLim 180/60, Zero±0.07, last point): the fp2k scale LS optimum is negative (-1.6e-3±7e-5, WARNING Scale<0→1E-10) = a real fault; per §4.2 switch to manual | ccea8a/02c933/b3d33b/a48170/7b815e |
| — | record | failure classification | — | — | — | real fault | the fp2k scale step is numerically pathological (not an in-design rejection / not an environment limitation)→switch to xrd_refine_manual | — |
| 9 | xrd_refine_manual | calibrate | physical | 33.1168 | 88.859 | effective (not yet at plateau) | scale/zero/a/U/V/W/η/bg6; zero=-0.0914 agrees with the .prf measurement; **c not in the parameter set** | result/components/plan_calibrate |
| 10 | xrd_refine_manual | structure (default stage) | physical | 33.1168 | 88.859 | effective (not yet at plateau) | stage_hint=structure actually opened no structural parameters (same solution as 9)→an explicit plan is needed | plan_structure |
| 11 | xrd_refine_manual | structure (plan) | physical | 39.1403 | 59.814 | **invalid (local minimum)** | a defect in the bundled engine's addp initial-value priority (the U/V/W/η/zero warm start was overridden by hard-coded defaults)→η pinned at the 0.98 bound; nfev=89; products mistakenly landed in the root directory | (leftover result/components in the root directory) |
| 12 | xrd_refine_manual | structure (engine copy + 12 coordinates) | physical | 31.7674 | 33.043 | progress (verdict: contains unphysical degrees of freedom) | fixed engine (xrd_engine_custom.py, addp pdef priority); later found that coord_vary moves only the first orbit mirror of each label→breaks the P6₃/m symmetry→methodological rollback of the coordinates | xrd_engine_custom.py; plan_structure_r11 |
| —(13) | xrd_refine_manual | structure (coordinates off) | physical | 31.0528 | 32.140 | progress | fixed literature coordinates + dw{Ca.8/P.6/O1.0/F1.5} = a clean physical model, better than 31.77 | plan_manual_r13 |
| —(14) | xrd_refine_manual | structure (modern CIF) | physical | 24.2370 | 26.870 | progress | **structural treatment (§6.2)**: the 1932 coordinates give P-O=1.824Å out of range (export fail)→build_orbit modern coordinates (COD 1533064 experimental values, OH/O4 removed, F→full occupancy 2a; validate pass, min contact 1.503Å); the V3 visual check shows the residual concentrated on strong peaks, supporting the replacement | ref/FAP_modern_orbit_01.cif; plan_manual_r14 |
| —(15) | xrd_refine_manual | dw comparison ① | physical | 24.7847 | 26.653 | not lowered (comparison) | B=0: the direction of the literature dw values is correct (Δ-0.55) | plan_manual_r15 |
| —(16) | xrd_refine_manual | dw comparison ② | physical | 24.2703 | 26.606 | not lowered (comparison) | group B Ca.6/P.4/O.7/F1.0 differs from r14 by 0.03 (noise) | plan_manual_r16 |
| —(17) | xrd_refine_manual | bg_scan escalation | physical | 23.2122 | 26.870 | **progress (last substantive improvement)** | background 6→16th order (R boundary order = 16), the per-order curves bg_n06…bg_n16 exported for GSAS | plan_manual_r17 |
| 17(18) | xrd_refine_manual | occ_F probe | physical | 23.2122 | 26.870 | not lowered (D3: no vacancies) | occ_F1 is pushed back by the LS to the 1.0 upper bound (the physical boundary = the answer itself); at_bound here is a physical, not a numerical, failure | plan_manual_r18 |
| 18(19) | xrd_refine_manual | bg window comparison | physical | 23.2122 | 61.220 | not lowered | the Chebyshev window (72.5,±57.5) gives the same minimum (same function space, mathematically inevitable) | plan_manual_r19 |
| 19(20) | xrd_refine_manual | confirmation re-run | physical | 23.2122 | 61.220 | **numerical plateau established** | rounds 17/18/19 give 23.212151 three times, bit-identical, none lower | plan_manual_r20 |
| 20 | xrd_refine_gsas | Ⅲ-build | physical | —(wR) | — | real fault (fixed) | self-made instprm Type:XRD is invalid: strIO:3007 branches on Type[1][2]∈{A,B,C}, 'D' falls through everything→dmin unbound→crash at every step; 0/5 executed | gsas_proj.gpx (initial build) |
| 21 | xrd_refine_gsas | Ⅲ-build | physical | —(wR) | — | real fault (fixed) | Type:SXC = single-crystal type (S=Single): the strMath 'S' in hType mistakenly enters the twin branch→'0:0:NTL' missing→the objective function crashes at the first evaluation; do_refinements only prints without raising→5/5 steps were wrongly marked accepted while actually doing nothing (no cycles in the lst) | gsas_proj.gpx; probe_*.py |
| 22 | xrd_refine_gsas | Ⅲ-ladder | physical | 11.7277(wR) | 30.5734(wR) | progress (convergence basin) | **Type:XRC is the correct answer**; handoff seeds W=26.2/Zero=-0.0829 (U/V were rejected by the 10x safeguard, self-corrected in the inst step); bg 30.57→inst 25.45→cell 14.40→scale 13.96→atoms 11.70→+SH/L 11.691 (cell/scale/atoms re-fits got worse and were rolled back); profile joint ×2 + size-only ×1 ineffective (Size;i↔X 100% collinear) | gsas_proj_continued.gpx/.lst |
| 23 | xrd_gsas_ops | Ⅲ-final | physical | **11.498(wR)** | 11.7277(wR) | **final convergence (delivery state)** | auto_background's first coeffs shape was passed wrongly→degraded to order 6, wR 12.54 (input not covered); after correction [12,14,16]→order 16 is best (consistent with the manual boundary order)→11.498; GOF 2.06, R_Bragg 4.77%; review pass; finalize delivery package + V4 passed + CIF check pass | gsas_proj_final.gpx; FAP_final/ |
| — | record | verify skipped | — | — | — | environment limitation | cif_to_pcr host 120s budget timeout (converter historically ~110s)→the optional item xrd_verify_fp2k skipped; substitute sentinels: hand-computed density 3.199 g/cm³, cell consistent with the literature, CIF bond lengths pass | verify/ (CIF copy only) |

Note: the jsonl engine's automatic numbering is offset from the working names (one accidental write to the root directory); the plateau window follows jsonl rounds 17/18/19.

## Materials and objective

- **Material**: fluoroapatite ore powder Ca5(PO4)3F (explicitly stated by the user); data `pattern_2theta.txt` (source GSAS-II tutorial FAP.XRA; Cu Kα doublet not stripped 1.540500/1.544300/0.5; 15.000–130.020°, step 0.0200, 5752 points; the last point at 130.02° has intensity=0 and was already excluded in fp2k with Thmax=130.00, the data file was not modified).
- **Objective (confirmed by the user)**: publication-grade structural refinement (full Rietveld, GSAS-II delivery); impurities screened from the data by ourselves. Objective sentence (§1.3 protocol): the goal is rwp_mean < ≈10% (a reference value, not a hard threshold) and GSAS wR approaching Rexp; if none of the attempts reaches the ideal result, report truthfully.
- **Achievement (truthfully)**: manual-engine plateau 23.21 (did not reach the ≈10 reference value — the engine's capability boundary: no peak-shape asymmetry / no Uiso refinement / coordinates without symmetry constraints, so per the workflow it switched to GSAS); **GSAS-II delivery wR=11.50% (wRmin/Rexp≈5.58-5.61, GOF=2.06), R_Bragg=4.77%** — excellent at the structure-factor level; the remaining gap between wR and Rexp is mainly peak-shape/background residual (starting from a generic instrument model, no real instrument parameter file, Size↔X collinearity). The reference value was not reached in the manual protocol and was partially reached in the GSAS protocol, which does not constitute a task failure (§1.3), nor did it trigger limit mode (fewer than 3 full checklists, and the GSAS line kept improving to convergence).

## Phases and crystal families (conclusion + basis + excluded families and why)

- **Conclusion**: single-phase fluoroapatite, hexagonal P6₃/m (#176), Z=2; a=9.37074, c=6.88499 Å, V=523.58 Å³ (GSAS refinement, esd in the lst).
- **Basis**: ① wide-in screen (3 COD candidates tied at 2.36-2.38, all main peaks explained |Δ2θ|≤0.06°); ② V2 visual check: all ticks correspond with no systematic offset; ③ GSAS R_Bragg=4.77%; ④ all 30 residual peaks of the converged project are at main-phase positions (no second phase).
- **Exhaustive crystal-family list (§6.3Ⅲ① protocol)**: hexagonal P6₃/m fluoroapatite standard type (**hit**); monoclinic P21/n|P21/b hydroxyapatite low-temperature type (this pattern's 31.9/32.2/33.1 triplet shows no monoclinic splitting, excluded); hexagonal P-3 carbonate-substituted francolite type (no superstructure peaks, excluded).
- **Excluded candidates**: MP mp-aaacrvgo (P6₃ relaxed, peak positions offset 0.17-0.23°, 12 hits); COD 1549763 (Sr/Mn doped, composition mismatch); COD 1010996 (1932 coordinates, P-O 1.824 Å out of range→export fail); COD 1011044 (redundant within the same family); COD 1533064 as-is (composition F0.8(OH)0.2 mismatch — only its modern experimental coordinates were taken).

## Defect master table (exhaustive → screening → execution)

| id | defect | source | reported | verdict | reason | backend | geometry_ref | exec | status |
|---|---|---|---|---|---|---|---|---|---|
| F-01 | F-site vacancy/non-stoichiometry | mineralogical common knowledge + COD 1533064 (F0.8) | yes (literature) | **not applicable (this sample)** | the occ_F1 multiplier is pushed back by the LS to the 1.0 upper bound (D3: pushed back ≈1 ⇒ no vacancies); the GSAS residual shows no F signature | manual (occ = a regular parameter, allowed) | 2a (0,0,¼) | 23.2122→23.2122 | executed |
| F-02 | Ca/P site vacancies | exhaustive | — | not applicable | stoichiometry explicitly stated by the user; no composition characterization hint; no residual signal | — | — | — | not executed (no residual signal, no characterization input) |
| O-01 | OH/CO3 substitution | mineralogical common knowledge | yes (literature) | not applicable | the user explicitly stated fluoroapatite; V1 shows no amorphous hump; the residual is entirely at main-phase positions | — | — | — | not executed (as above) |
| X-01 | second phase/associated impurity | screening requested by the user | — | **not detected** | in the wR=11.5 converged project all 30 residual peaks fall at main-phase Bragg positions, with no out-of-phase peaks; the detection limit is constrained by the main-phase peak-shape residual (stated truthfully) | xrd_phase_screen(residuals) | — | 30/30 main-phase positions | executed |
| X-02 | preferred orientation (MD) | exhaustive (common in minerals) | — | not tried (weak evidence does not support it) | the residual morphology is a peak-shape mismatch rather than a systematic intensity deviation of a specific hkl family | gsas (possible) | MD 001 | — | not executed (low priority, listed as not tried) |
| X-03 | anisotropic broadening/microstrain | residual concentrated on strong peaks | — | partially executed/already tried without effect | size+mustrain joint ×2 rolled back; size-only noise level (+0.037); Size;i↔X 100% collinear; generalized mustrain/HStrain not tried | gsas | — | 13.96→13.99;11.691→11.728 | partially executed |

## Achieved results (R and protocol written separately; FullProf Rwp and GSAS wR are not directly comparable)

- **GSAS-II (delivery protocol)**: wR=**11.50%**, R=8.81%, Rb=9.15%, wRb=11.49, **wRmin≈5.61**, GOF=**2.06** (Rexp≈5.58), χ²raw=24160; **R_Bragg=4.77% (325 reflections)**.
- **Deliverables**: `FAP_final/` (FAP_final.gpx clean project, FAP_final.lst, FAP_built.cif = official export_CIF, FAP_fit.png = V4 passed, FAP_report.md, manifest). CIF bond-length check **pass**: P-O 1.515–1.566, Ca-O 2.346–2.514, Ca-F 2.302 Å.
- **Structural parameters**: cell a=9.37074, c=6.88499 Å; Uiso (Å²) Ca1 0.0217/Ca2 0.0219/P1 0.0216/O1 0.0261/O2 0.0256/O3 0.0257/F1 0.0339; coordinates (Ca1 z=0.00168; Ca2 0.24141,0.99185; P1 0.39705,0.36770; O1 0.32571,0.48599; O2 0.58971,0.46938; O3 0.34019,0.25918,0.07102; F1 0,0,¼ fixed).
- **Manual engine (stage Ⅱ protocol)**: plateau Rwp=**23.2122%** (Rexp 5.60, χ² 17.19).
- **fp2k**: no valid refinement (real fault in the scale step, line frozen); the fixed-scale baseline only proves the structure/peak positions (Bragg_R≈51).
- **Density sentinel**: ρ=2×504.3/(523.58 Å³×N_A)=**3.199 g/cm³** (literature 3.18–3.20 ✓).

## Not tried / undecided items

- **Not tried**: anisotropic Uij; generalized/uniaxial mustrain and HStrain; a mustrain-only single test; MD preferred orientation; releasing F/Ca occ inside GSAS for re-checking; LeBail intensity floor (a limit-mode tool, not triggered); xrd_verify_fp2k (environment limitation: converter timeout; an optional item, substitute sentinels already exist).
- **Undecided**: the gap between wR (11.50) and Rexp (5.58) is limited by having **no real instrument parameter file** (starting from a generic placeholder + data self-correction) and by the ceiling of the peak-shape model; it is expected to drop further once a measured standard-sample instrument file is provided.
- **Background protocol disclosure (§6.8)**: manual bg_scan was done (boundary order 16); GSAS auto_background was done (12/14/16→16 best); 18/20 was not escalated (the manual-protocol R boundary stops at 16, and escalating further enters the overfitting risk zone).
- **"Not tried" ≠ "cannot be improved"**: until the not-tried items above are completed, the conclusion is only "converged within what was tried".

## Handover recommendations

1. The delivery state = `FAP_final/`; continue from `gsas_proj_final.gpx` (do not touch the files inside the delivery package).
2. Route to lower wR: supply a measured instrument parameter file (standard sample Si/LaB6)→ anisotropic Uij (O/P first)→ uniaxial/generalized mustrain → MD orientation; one variable at a time + entry=hold rollback.
3. Do not use the fp2k line for refining this data (real fault in the scale step, evidence chain rounds 1-6); the cross-validation can be added once the converter no longer times out.
4. Three pitfalls of this bundled GSAS-II tree: the powder instrument Type must be **'XRC'** ('XRD'→dmin crash, 'SXC'→NTL crash); SetDefaultDData PWDR Extinction takes a 2-tuple (strIO 3212 expects a 3-tuple); do_refinements only prints 'Refinement error' without raising (when wR=? always check the lst).
5. The last data point (130.02°, I=0): already excluded by fp2k with Thmax=130.00; GSAS Limits were not trimmed (no weight anomaly seen); if a weight problem occurs during continuation, trim Limits first.
6. The engine copy `xrd_engine_custom.py` (addp initial-value priority fix) is what this sample's manual line depends on; it is recommended to keep it until the project is archived.

# FE50 journal quick view (summarized from journal.jsonl; the authoritative record = jsonl, 40 lines)

| Round | Engine | Stage | Model | Rwp/wR | Baseline R | Verdict | Why | Artifacts |
|---|---|---|---|---|---|---|---|---|
| 0 | data_io | initial screening | physical | — | — | λ determination + V1 | Cu doublet explicit; main phase PBA~25nm + high-angle splitting + broad hump | peak_survey.md |
| 1 | fp2k | I-D0 | physical | 415/311 | — | invalid | scale initial value off by an order of magnitude | .fp2k-work-* |
| 2 | fp2k | I-ladder | physical | 70.4/73.7 | 415/311 | invalid, tail-dragging trap | W→1.98 unphysical smearing | .fp2k-work-* |
| 3 | manual | calibrate | physical | 13.009 | 97.8 | snapshot (hit 8000) | V/eta/ex0_c at bounds | manual_cubic |
| 4 | manual | calibrate | physical | 13.201 | 96.3 | converged, 4 parameters pinned at bounds | monoclinic comparison | manual_mono |
| 5 | manual | calibrate | physical | 12.422 | 96.7 | converged, 3 parameters pinned at bounds | cubic calibrate endpoint | manual_cubic |
| 6 | manual | v4 | physical | 12.689 | 13.01 | worse than v2 | warm start mistakenly used the v1 parameters | manual_cubic_v3 |
| 7 | manual | v5 | physical | 12.274 | 12.42 | snapshot (hit 20000) | X/Y→0 pinned at bottom, V/eta pinned at new bounds | manual_cubic_v5 |
| 8 | manual | mono v4 | physical | 11.938 | 13.21 | converged, monoclinic ahead | a,b,c,β released | manual_mono_v3 |
| 9 | manual | H1 K occupancy | physical | 11.586 | 12.27 | K occupancy wins (-0.69) | occ_K→1.294 (K=0.97, x≈1.94) | cubic_H/h1_kocc |
| 10-11 | manual | H2/H3 | physical | 12.2735 | — | invalid rounds | occ initial value = max, zero-gradient freeze (fixed in h2b/h3b) | cubic_H/h2,h3 |
| 12-13 | manual | H4/H5 K2CO3 | physical | 12.219/12.248 | 12.27 | insufficient evidence | scale stalls at 0.052 | cubic_H/h4,h5 |
| 14-15 | manual | H6/H7 | physical | =baseline | 12.27 | KHCO3/MnCO3 rejected | scale→1.6e-10/5.1e-7 | cubic_H/h6,h7 |
| — | manual | H8 Mn3O4 | physical | =baseline | 12.27 | rejected | scale→0.003 pinned at bottom | cubic_H/h8_mn3o4 |
| — | manual | mono_h1 | physical | 10.580 | 13.2 | converged, K pinned at the upper bound | K occupancy transplant to monoclinic confirmed (-1.36) | mono_h1_kocc |
| 16 | gsas | first ladder | physical | 12.956 | — | bg/cell/size adopted, atoms rejected | handoff safeguard rejects degenerate seeds | gsas_proj.gpx |
| 17 | gsas | inst | physical | 12.495 | 12.96 | adopted | U,V,W,X,Y,Zero | gsas_proj_continued |
| 18 | gsas | T1/T1b | physical | 12.378 | 12.50 | K occupancy-Uiso alternate verification | occ out of range 1.045→U released and falls back | gsas_T1b |
| 19 | gsas | T2/T3 | physical | 11.971 | 12.38 | all Uiso + clamping + Scale | Fe negative U clamped at 0.005 | gsas_T3 |
| 20 | gsas | T4/T5 | physical | 10.123 | 11.97 | coordinates greatly improved but C/N U negative→clamped | ⚠ later judged chemically collapsed by the bond-length audit | gsas_T5 |
| 21 | gsas | T6 | physical | 9.010 | 10.12 | background import (-1.11) | bg+extras 80 points fixed | gsas_T6 |
| 22 | gsas | T7/T7b | physical | 8.972 | 9.01 | framework vacancies→none (pinned at 1.0) | occ→1.0022 | gsas_T7b |
| 23 | gsas | T8 | physical | 8.975 | 8.97 | N-coordinated vacancies→none | sums 0.9956 | gsas_T8 |
| 24 | gsas | T9 | physical | 8.975 | — | Mustrain gives no gain | (T7b baseline, later abandoned) | continued |
| 25 | gsas | T14abc | physical | 10.582 | — | **bond-length audit ⇒ discard the 8.97 solution** | literature C/N+K pinned at 0.969 = honest baseline | gsas_T14c |
| 26 | gsas | T15ab | physical | 10.402 | 10.58 | water rejected (dual scheme) | free: cavity total occupancy 1.46; conserved: Ow negative | gsas_T15b |
| 27 | gsas | T16ab | physical | 10.545 | 10.58 | extinction/PO not adopted | -0.04/+0.005 | gsas_T16a |
| 28 | manual | T15m | physical | 10.670 | — | bond-length-constrained coordinate relaxation ≈ unmoved | chemically legal displacements give no gain | mono_T15m |
| 29 | gsas | T17 | physical | 11.097 | 10.58 | ideal CN rejected | over-constrained | gsas_T17 |
| 30 | gsas | **T18** | physical | **9.442** | 10.58 | **C/N Uiso static disorder adopted (-1.14)** | C 0.155/N 0.25 positive values | gsas_T18 |
| 31 | gsas | T19 | physical | 9.419 | 9.44 | Mustrain adopted (-0.02) | Size-X/Mustrain-Y collinearity recorded | continued |
| 32 | gsas | T20 | physical | 9.393 | 9.42 | K2CO3 rejected (-0.026) | X-01 closed loop | gsas_T20 |
| 33 | gsas | T22 | physical | 9.349 | 9.42 | K split rejected | -0.07 but U→0.0006 unphysical | gsas_T22 |
| 34 | gsas | T23 | physical | 9.401 | 9.42 | K occ re-check 0.978≤1 ✓ | x≈1.956 | gsas_T23 |
| 35 | gsas | T24 | physical | 11.979 | 9.40 | background order escalation rejected | Cheb best n=10 still worse; curve retained | gsas_T24 |
| 36 | gsas | **T25** | physical | **9.404** | 9.40 | **delivery state (all pass)** | N U pinned at 0.20 (+0.003 free); K 0.9937 | **gsas_T25_NUclamp** |
| 37 | gsas | T26 | physical | 9.479 | 9.40 | N3 correction rejected (+0.075) | the data support the literature N3 (disorder manifestation) | gsas_T26 |
| 38 | finalize | V | physical | **9.40** | — | **delivery package complete** | wRmin 7.92/GOF 1.19; V3/V4 passed | **FE50_final/** |

## Materials and objective
FE50: a Prussian blue analogue, nominal KxFe0.5Mn0.5[Fe(CN)6]; Fe4[Fe(CN)6]3 + manganese oxide tetrahydrate + potassium citrate, ball-milled (agate) in 50% aqueous ethanol. The user specified consideration of high defectiveness (lattice distortion/vacancies/split sites), the objective is publication grade R≤10 (GSAS-II wR protocol), and the products are stored in the FE50 directory. **Target achieved: wR=9.40% (REVIEW all pass)**.

## Phases and crystal families (conclusion + basis + excluded families and why)
- **Conclusion: monoclinic P2₁/c (pseudo-cubic)**, a=10.1223(18) b=10.1267(5) c=10.1262(13) Å β=92.611(31)° V=1036.9(12) Å³; the final composition is **K₁.₉₉Fe₀.₅Mn₀.₅[Fe(CN)₆]** (Everitt salt type fully reduced K-rich phase; charge self-consistency K⁺₁.₉₉+Fe²⁺₀.₅+Mn²⁺₀.₅+[Fe²⁺(CN)₆]⁴⁻).
- Basis: ① the manual engine under the same protocol gives 11.94 vs 12.27/12.42 for cubic; ② **empirical evidence of P-lattice additional reflections** — (011) 12.23°/(11-1) 14.79°/(111) 15.26°/(021) 19.46°/(211) 21.0-21.7° are visible in the data and explained by the model (F-centered cubic forbids these reflections).
- Excluded: cubic Fm-3m (R disadvantage + cannot explain the additional reflections and the (420)/(422) splitting; the comparison branch is retained); rhombohedral R-3 and vacancy-ordered supercells (the fallback was not started — the main line meets the target and there is no supercell-peak evidence); the literature exhaustive list of 4 families and their sources are in phase_summary.json; MP/COD have no entry for this composition (recorded).

## Defect master table (exhaustive → screening → execution)
All 16 items are recorded in `defect_table.json` (10 fields). Key points:
- **Adopted**: monoclinic lattice distortion (D-09, β=92.61°); K off-centering displacement (D-08, K1 off-center by ~0.62 Å); slight K deficiency (D-01, occ 0.9937); nanoscale size (D-12, Size isotropic); microstrain (D-11, weak, collinear with instrumental Y); **C/N static disorder** (large Uiso: C 0.189/N 0.200 — the average-structure expression of the ball-milling-distorted CN framework, the main gain of wR -1.14); amorphous component (X-02, expressed by a fixed background curve).
- **Judged absent/rejected**: [Fe(CN)₆] framework vacancies (occ→1.002); N-coordinated vacancies (sums→0.996); zeolitic water (dual scheme: cavity total occupancy 1.46 impossible / negative occupancy under conservation); K split site (dual scheme × dual baseline: -0.012/-0.07 + unphysical U→0.0006/+0.27 — "this data cannot resolve it", not "it does not exist"); crystalline impurity second phase (rejected empirically 6 times / noise level: KHCO₃, MnCO₃, Mn₃O₄, K₂CO₃×2, GSAS re-judgement); extinction/preferred orientation (no gain).
- **Key event of the chemical self-consistency review**: the GSAS free C/N coordinate solution (wR 8.97) was judged **chemically collapsed** by the bond-length audit (Fe–C 2.36 Å/C–N 2.28 Å/M–N 1.39 Å) and abandoned; ideal CN geometry (11.10) and the N3 surgical correction (9.48) were both rejected by the data ⇒ literature C/N coordinates + large Uiso is the self-consistent intersection of data and chemistry; the literature model's own local defects of Mn–N3 1.54 Å/C3–N3 1.73 Å are disclosed as "the average-structure manifestation of static disorder".

## Achieved results (R and protocol written separately)
- **GSAS-II (delivery protocol)**: wR=9.40%, R=7.43%, Rb=7.79%, wRb=8.88%, wRmin=7.92%, GOF=1.19 — **≤10 target met**, 1.48 points from the statistical limit.
- Manual bounded engine (corroborating protocol, not directly comparable with the above): mono_h1 Rwp 10.58 (converged); cubic h1 11.59.
- FullProf fp2k: used only for candidate scoring, abandoned after falling into the tail-dragging trap (70.4/73.7 archived as invalid).
- Data statistics: max 739 counts (weak data); Rexp≈7.9 sets the lower bound of wR.

## Not tried / undecided items (must not be left empty; "not tried" ≠ "cannot be improved")
1. **Anisotropic broadening model (D-14)**: GSAS anisotropic Mustrain/HStrain not tried (the monoclinic symmetry already absorbs the main part; the 39-45° residual of ±40 counts may contain an anisotropic component).
2. **Stacking faults (D-10)**: not modelled (no directional evidence + tool boundary).
3. **Third scheme for the K split site**: the transverse splitting direction (y/z axis or <111>) was not tried separately (the x-axis dual scheme is closed).
4. **C/N anisotropic ADP**: not tried (risk of over-parameterization: 12 atoms × 6 parameters against 2802 points of weak data).
5. **lin-interpolate background point refinement**: not tried (risk of overfitting with 80 free background parameters; Chebyshev order escalation was tried and rejected at 11.98).
6. **Rhombohedral R-3 family**: the fallback was not started (the main line meets the target).
7. **Twinning (D-13)**: requires TEM, XRD cannot decide it.
8. Residual degeneracy between K occ and Scale/Uiso (Scale-Scale 100% correlation warning) — the esd of x=1.99 is optimistic, ICP re-checking is recommended.

## Handover recommendations
- Delivery project `FE50_final/FE50_final.gpx` (**do not refine again**: stale constraints have been cleared and the cached wR is frozen); the working copy that may be refined = `gsas/gsas_T25_NUclamp.gpx`.
- If wR needs to be pushed lower (→below 9.0): try anisotropic Mustrain first (39-45° residual) and C/N anisotropic ADP (constrained to 2-3 independent components); keep the background as a fixed curve.
- If ICP/EDS is obtained: pin K occ with the measured x and then re-refine Scale/Uiso (the current x=1.99 is the XRD value).
- Chemical point: the sample is a fully reduced Fe²⁺ system (reduced by potassium citrate); air oxidation will cause K to leach out / Fe³⁺ to rise — pay attention during characterization.
- Bond-length violation disclosure: Mn–N3 1.54 Å, C3–N3 1.73 Å (the data-supported literature geometry; both idealization and the single-point correction make wR worse, see T17/T26).
- All 40 rounds recorded: `xrd_workflow/journal.jsonl`; state: `workflow_state.json`; final defect adjudication: `defect_table.json`; judgement history: `review_judgment.md`.

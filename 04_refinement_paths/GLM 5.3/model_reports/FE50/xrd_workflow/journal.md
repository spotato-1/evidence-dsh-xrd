# FE50 journal.md overview (generated from journal.jsonl)

| round | engine | stage/level | model | Rwp | baseline | verdict | why | artifacts |
|---|---|---|---|---|---|---|---|---|
| 1 | xrd_refine_auto | candidate scoring | physics | 70.6 | 100.0 | not yet at the basin; fp2k ladder hung (numerical) | all background steps rejected; Rexp≈16 is a weighting-convention artefact | .fp2k-work-* |
| 2 | manual | calibrate | physics | 13.78 | 97.65 | not yet at the basin; M2 slightly better | M2 13.78 vs M1 14.22; common residual (220) undercalculated + broad halos | result.json ×2 |
| 3 | manual | structure-TCH | physics | 10.74 | 96.57 | progress | TCH+extras took effect; K-C occupancy degeneracy found → needs GSAS coupling | r3/result.json |
| 4 | manual | structure-TCH (M1 control) | physics | 11.80 | 97.91 | family adjudication: M2 wins | same parameterisation Δ=1.07; broad halos = (111)/(311) forbidden positions | r4/result.json |
| 5 | GSAS (stepwise) | III-A bg+scale | physics | 23.77 | — | GSAS channel repaired | instprm/HAP fixed; 93s→4s/cycle | FE50_fix2.gpx |
| 6 | GSAS | III-B/C/D cell+inst+bg6 | physics | 13.92 | 23.77 | progress | bg6 absorbs the broad-halo shape | — |
| 7 | GSAS | III-E Uiso equivalence group | physics | 12.99 | 13.92 | progress (drift allowed) | large CN Uiso = static disorder; metal negative Uiso to be fixed | — |
| 8 | GSAS | III-F occupancy | physics | 12.77 | 12.99 | progress | equiv/conserve ran away → bounded grid; w=0.60 k=0.80 | occscan.json |
| 9 | GSAS | III-G wrap-up + B5 | physics | 11.26 | 13.30 | progress | diffuse-scattering curve imported; CN Uiso free 0.056 | FE50_cnu_ref.gpx |
| 10 | GSAS | III-H re-scan + delivery | physics | 11.00 | 11.60 | **delivered** | w=0.60 k=0.70; wRmin=7.92; not reaching 10 reported as-is | FE50_final/ |

## Material and target
- Sample FE50: KxFe0.5Mn0.5[Fe(CN)6], ball-mill synthesised (Fe4[Fe(CN)6]3 + manganese oxide tetrahydrate + potassium citrate, 50%EtOH/H2O)
- Target: publication-grade structure refinement, R<≈10 (reference value); if not reached, report as-is
- λ: Cu doublet 1.5406/1.54439/0.5 (Rigaku header, Monochromator=0)

## Phases and crystal families (conclusion + evidence + exclusion)
- **Selected: monoclinic P2₁/c** (candidate_B with Sb removed, N site Fe0.5Mn0.5) — an actual run with the same parameterisation beats cubic by ΔRwp=1.07 (r3/r4)
- Excluded: cubic Fm-3m (M1, r4=11.80 worse than 10.74; extras all at the H=4 bound, degenerate)
- Excluded: hexagonal P-31m (M3, excluded by screening: diagnostic peaks 13.8/21.9/29.6° missing + chemical mismatch, no actual refinement round burned)
- Database search: MP (K-Mn-Fe-C-N empty; Mn-Fe-C-N→P-31m; K-Fe-C-N→K3Fe(CN)6 salts not applicable); COD (cod_1516491=CdPt(CN)6 framework prototype a=10.166 corroborates the geometry)

## Defect summary table (enumerate→screen→execute)
- D-01 vacancies: **[Fe(CN)6] 40%** (w=0.60, quantified by grid); N site fully occupied; K 0.70
- D-09 distortion: monoclinic wins; β=87.2°
- D-07 K split sites: constraint scheme + indistinguishable verdict
- D-02/D-03 antisite/mixed occupancy: indistinguishable by X-ray (conservation-constrained actual run drifted without bounds), not judged as "does not exist"
- D-05 diffuse scattering: 15°/29° = (111)/(311) forbidden-position broad halos, empirical component + fixed background import
- D-11/D-12 strain/size: apparent 21–29 nm (instrumental not subtracted); TCH X=0.58
- X-01 impurity: no sharp impurity peaks
- See defect_table.json for details (15 entries, exec/status complete)

## Results achieved (R and convention written separately)
- **GSAS-II (delivery convention): wR=11.00 %, R=8.72, Rb=10.25, wRmin=7.92** (FE50_final/)
- Manual engine (corroboration convention): Rwp=10.74 (r3, including the empirical diffuse-scattering component and free occupancies — its occ_C=0.14 is a degeneracy artefact and is not accepted)
- FullProf fp2k: ladder 70.6 (background step hung, numerical, not used for adjudication)
- The conventions are not directly comparable; the target R≤10 was not fully reached (short by 1.0), see report §4 for the attribution

## Not tried · unresolved items
- Not tried: peak-shape asymmetry (SH/L), free refinement of CN coordinates (exempted on resolution grounds), anisotropic broadening, iterative background-order upgrade (orders 8–20, expected gain <0.5), free K-site-coordinate scheme (exempted by the resolution argument)
- Unresolved: w-k degeneracy and charge-balance inconsistency (needs ICP/XPS/Mössbauer); the microscopic origin of the diffuse scattering; the Fe/Mn antisite ratio

## Suggestions for the next handler
1. Add ICP+XPS → re-check charge balance and the w-k degeneracy
2. To push wR<10, first try asymmetry and a second diffuse-scattering component
3. Mössbauer to determine the Fe valence and hence the vacancy morphology
4. On re-measurement, reduce the step size and extend the range to improve resolution

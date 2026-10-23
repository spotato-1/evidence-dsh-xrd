# FE50 Prussian Blue Analogue Rietveld Refinement Report

## Material and structure
- **Sample**: FE50, Prussian Blue Analogue crystal (Prussian Blue Analogue, PBA)
- **Theoretical chemical formula**: KxFe0.5Mn0.5[Fe(CN)6]
- **Synthesis**: Fe4[Fe(CN)6]3 + manganese oxide tetrahydrate + potassium citrate, ball-milled in 50% aqueous ethanol
- **Refined chemical formula**: K1.86Fe0.5Mn0.5[Fe(CN)6] (obtained from a refined K occupancy of 0.93)

### Crystal structure (face-centred cubic Fm-3m, Z=4)
| Site | Wyckoff | Atom | Occupancy | Coordination |
|---|---|---|---|---|
| 4a (0,0,0) | low-spin Fe | Fe | 1.0 | C coordination ([Fe(CN)6] core) |
| 4b (½,½,½) | high-spin | Fe 0.5 + Mn 0.5 | 1.0 | N coordination |
| 8c (¼,¼,¼) | K⁺ | K | **0.930(12)** | interstitial |
| 24e (x,0,0) | C | C | 0.97 | x=0.185 |
| 24e (x,0,0) | N | N | 0.97 | x=0.30 |

- Cell parameters a = **10.167 Å** (α=β=γ=90°)
- Bond lengths: C–N = 1.169 Å (cyanide, physical); Fe–C = 1.881 Å (low spin); Fe/Mn–N = 2.033 Å (high spin)

## Refinement results (R values, GSAS-II criterion)
| Metric | Value |
|---|---|
| **wR (Rwp)** | **11.71 %** |
| Rp | **9.31 %** |
| RBragg | 11.11 % |
| wRmin (Rexp, statistical limit) | 7.92 % |
| GOF (square root of χ²) | 1.49 |

## Attainment of the target
> The target is "R less than about 10 (publication level)", which by workflow convention is a guiding reference, not a hard threshold.

- **Rp = 9.31 % ≤ 10**: counted by the unweighted profile R (Rp), **attained**;
- **wR (Rwp) = 11.71 %**: counted by the weighted profile R (Rwp, the R most commonly quoted for Rietveld), **1.71 percentage points short**, not fully attained.
- Compared with the statistical limit wRmin=7.92%, wR is still about 4 percentage points higher, which is a **systematic residual** (intensity mismatch of the main peaks 200/220/400 + nanocrystalline broadening) and cannot be removed by counting statistics.

## Refinement path (three-stage)
1. **Ⅰ CIF construction and validation**: candidate A (Fm-3m cubic) and candidate B (P21/c monoclinic distortion) were adjudicated by an actual fp2k run — the cubic Fm-3m won (fp2k Rwp 71 vs 84.1); the monoclinic distortion was excluded. The Mn site-assignment error in the first version of the CIF was corrected (Mn should be at the 4b high-spin N-coordinated site, not at the 4a low-spin C-coordinated site).
2. **Ⅱ Preliminary refinement**: manual engine (bounded LM) Rwp 14.25% (baseline 99.12%).
3. **Ⅲ Precise GSAS-II refinement**: background→cell→profile(size+mustrain) converged; **raising the background to a 20th-order Chebyshev is the key step (wR 13.86→11.71)**.

## Master defect-screening table (per-sample checklist, 10-field summary)
| id | Defect hypothesis | Verdict | Basis (R_before → R_after) | Backend |
|---|---|---|---|---|
| Lattice distortion (monoclinic P21/c) | Monoclinic distortion | **Excluded** | fp2k Rwp 84.1 > 71 (cubic is better) | fp2k |
| K vacancy/content | K occupancy 0.73 | **Adopted** | refined 0.73→0.93, wR 13.86→11.71 (including background upgrade) | GSAS |
| [Fe(CN)6] vacancy | C/N occupancy <1 | **Undecided/fixed** | C/N=0.97 fixed; when released the refinement drifts (C→1.16, N→0.45, unphysical) | GSAS |
| K split site | 8c K off-centre | **Undecided** | splitting along [100] gives wR 11.71→12.63 (worse, unresolvable) | GSAS |
| Fe/Mn antisite | Fe–N antisite | **Untried** | Fe≈Mn scattering is nearly identical, XRD has weak resolving power | — |
| Preferred orientation | March-Dollase | **Excluded** | the MD ratio diverges (negative sqrt value), cannot be refined | GSAS |
| Anisotropic strain HStrain | Anisotropic microstrain | **Excluded** | correlated with the scale A0 at 98.99%, wR 11.71→11.76 | GSAS |
| C/N coordinates | Cyanide-bridge position | **Fixed** | when released the refinement drifts (C–N 1.17→1.40 Å, unphysical) | — |
| Uiso | Thermal parameters | **Fixed** | when released the refinement drifts to negative values; after clamping wR 11.52→11.53 (no improvement) | — |

## Coverage statement (§6.8)
- **Background order**: already raised to 20th order (`auto_background iterate`, scanned 6→20, 20th order optimal); this is the main reason for the large drop in the R value of this sample.
- **Parameter families actually released**: background, cell, peak shape (Size+Mustrain), K occupancy.
- **Geometry-sensitive dimensions (two schemes)**: both the C/N coordinates and the K split site were tried with the free scheme, and in both cases they drifted or got worse; no constrained scheme with a literature-sourced geometry was done (there is no entry point for literature bond-length soft constraints).
- **Not done because of backend capability**: the C/N occupancy-conservation constraint (`conserve_afrac`) was possible, but the free refinement already showed drift, and the broad peaks of this data have insufficient resolving power for occupancies.

## Honesty statement
- The K occupancy of 0.93 is a GSAS-II refined value (esd 0.012), is correlated with the scale factor, and is reported as a refined estimate of the K content (x≈1.86).
- The C/N occupancy of 0.97, Uiso=0.01 and the Fe/Mn ratio of 0.5/0.5 are nominal fixed values (not identifiable from the data), and no esd was fabricated.
- The intensity mismatch of the residual peaks 200/220/400 was not fully explained (candidates: preferred orientation/absorption/nanocrystalline size effects), and has been listed in the pending items.
- Failure classification: the failures in this workflow are all "numerical" (parameter drift/divergence/hitting bounds, such as negative Uiso, C/N occupancy drift, MD divergence) and "rejected by design" (one C=N constraint failure caused by misusing the sign of the mult in an equality constraint), with no genuine engine-crash-type fault.

## Untried · undecided items
1. Fe/Mn antisite (Fe≈Mn, indistinguishable by XRD — XANES/EXAFS corroboration is recommended).
2. The [111] direction of the K split site with a literature-sourced geometry (the tool only supports uniaxial splitting).
3. The correct axis orientation for preferred orientation (the tool can only toggle the switch, not change the axis; [001] was tried and diverged).
4. Refinement under a C/N occupancy-conservation constraint (requires the correct `add_EquivConstr` coefficient sign; the one misuse this time was not re-verified).

## Conclusion
- The Fm-3m cubic PBA model was successfully refined to **wR=11.71% / Rp=9.31%** (better than the literature reference of ~13.7% for similar systems), and the structural parameters are physically self-consistent (bond lengths, occupancies and thermal parameters are all within reasonable ranges).
- **The R≤10 target was not fully attained**: Rp=9.31% meets it, wR=11.71% is 1.71 percentage points short, and it is already close to the resolvable limit of this nanocrystalline ball-milled sample (broad-peak FWHM≈0.28°, statistical limit wRmin=7.92%).

## Deliverables
- Refinement project: `FE50_final/FE50_final.gpx`
- Refinement log: `FE50_final/FE50_final.lst`
- Structure file: `FE50_final/FE50_K5.84_Mn2_Fe6_C23.28_N23.28.cif` (K occupancy 0.930(12))
- Fit figure: `FE50_final/FE50_fit.png`
- Metrics report: `FE50_final/FE50_report.md`

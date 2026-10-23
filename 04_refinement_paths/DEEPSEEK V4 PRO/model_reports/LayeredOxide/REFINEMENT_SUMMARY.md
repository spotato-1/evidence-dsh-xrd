# LayeredOxide XRD Rietveld Refinement Summary Report

## Material and objective

- **Sample**: layered oxide cathode material, theoretical chemical formula Na₀.₇₂Ni₀.₃₃Mn₀.₆₂Mo₀.₀₅O₂ (feed ratio).
- **Synthesis**: sol-gel method + ball milling, calcined at 450℃ 5 h + 900℃ 12 h; raw materials NaOH, Na₂MoO₄·2H₂O, Ni(CH₃COO)₂·4H₂O, Mn(CH₃COO)₂·4H₂O, citric acid.
- **Impurity**: sodium molybdate Na₂MoO₄.
- **Objective**: publication-level Rietveld refinement, GSAS wR ≤ 10.

## Data

- Rigaku Cu Kα (Kα1=1.5406 Å, Kα2=1.54439 Å, ratio 0.5, Monochromator=0 i.e. Kα2 not stripped).
- Range 10–80° (2θ), step 0.0204°, 3432 points.

## Phase and crystal family (conclusion + basis)

| Phase | Space group | Cell | Conclusion |
|---|---|---|---|
| Main phase P2-Na₀.₇₂(Ni₀.₃₃Mn₀.₆₂Mo₀.₀₅)O₂ | P 6₃/m m c (194) | a=2.8889(5) Å, c=11.1340(5) Å, V=80.47 Å³ | selected |
| Impurity Na₂MoO₄ | F d -3 m (227) | a=9.1089 Å (fixed, COD 2240655 neutron structure) | selected |

**Criteria for the main phase**: the first strong peak 15.77°=(002), d=5.61 Å → c≈11.13 Å (P2 bilayer); (100) 35.72° → a≈2.89 Å; there is no (003) peak of O3 (~16.7°) → O3 is excluded. Candidate structures were taken with `polymorphs` (9 polymorphs of NaMnO₂) → P6₃/mmc (P2) and R-3m (O3) were screened, and P2 is consistent with the full pattern.

**Criteria for the impurity**: the peaks of Na₂MoO₄ (Fd-3m spinel, Mo@8a, Na@16d, O@32e) overlap those of the main phase at 27.5°(220), 32.4°(311), 39.4°(400), 43.5°(331), 48.8°(422), which is co-evidenced by multiple peaks of the same origin.

## Refinement results (final GSAS-II)

| Metric | Value |
|---|---|
| **wR (Rwp)** | **9.82%** ✅ (target ≤10 met) |
| R | 6.68% |
| Rb (Bragg) | 14.49% |
| wRmin (Rexp) | 4.97% |
| GOF (χ²)^½ | 1.98 |

**Main-phase atom parameters** (P 6₃/m m c, 2a TM / 4f O / 2b+2d Na):

| Site | Wyckoff | x | y | z | Occupancy | Uiso (Å²) |
|---|---|---|---|---|---|---|
| Mn | 2a | 0 | 0 | 0 | 0.62 | 0.005 |
| Ni | 2a | 0 | 0 | 0 | 0.33 | 0.005 |
| Mo | 2a | 0 | 0 | 0 | 0.05 | 0.005 |
| O | 4f | 1/3 | 2/3 | 0.0971(28) | 1.0 | 0.005 |
| Na(2b) | 2b | 0 | 0 | 1/4 | 0.283(54) | 0.059 |
| Na(2d) | 2d | 2/3 | 1/3 | 1/4 | 0.437(54) | 0.011 |

- Na occupancy conservation: Na(2b)+Na(2d)=0.72 (feed ratio); after refinement it occupies mainly the 2d (face-sharing) site.
- Impurity Na₂MoO₄ weight fraction about **24.8%** (GSAS refined value; a fairly large amount of synthesis by-product).
- TM site (2a) Uiso equality constraint (mixed occupancy at the same position); the impurity Uiso is fixed to the COD neutron value.

## Master list of defects (per-sample checklist, §6.9)

| id | defect | verdict | reason | backend | exec |
|---|---|---|---|---|---|
| D-01 | Na occupancy distribution (2b/2d) | applicable | after refinement 0.283/0.437, conserved 0.72 | GSAS conserve_afrac | wR 13.65→9.82 |
| D-02 | TM-site mixed occupancy (Mn/Ni/Mo together on 2a) | applicable | three rows at the same position, Uiso equality constraint | GSAS equiv_uiso | stabilisation |
| D-03 | second phase Na₂MoO₄ | applicable | co-evidenced by multiple peaks of the same origin, two-phase refinement | GSAS two-phase | required |
| D-04 | preferred orientation (layered platelet) | undecided | MD[001] refinement r≈1.07, limited improvement | GSAS Pref.Ori. | small effect |
| D-05 | microstrain/grain size (Mustrain/Size) | not applicable | refinement gave no improvement (wR 10.06→10.11), peaks are dominated by instrumental broadening | GSAS | excluded |
| D-06 | interlayer cation mixing (Ni/Mn entering the Na layer) | not executed | requires adding TM sites to the Na layer as a test, the data have insufficient information content | GSAS | untried |
| D-07 | oxygen vacancies | not executed | no independent evidence, not refined | — | untried |

## Coverage statement (§6.8)

- **Background order**: 6th-order Chebyshev, **no background-order upgrade iteration was done** (wRmin=4.97%, the gap between the current wR 9.82% and the statistical limit is mainly due to the defect model/peak shape, not the background; an upgrade is an unconventional escalation action and was not triggered).
- **Parameter families actually released**: background, instrument (U/V/W/Zero, X/Y fixed), cell (main phase), scale (both phases), atoms (coordinates/occupancies/Uiso, including uiso_floor clamping), Pref.Ori..
- **Never released even once**: Mustrain/HStrain (tried, of no benefit), higher-order spherical harmonics for preferred orientation (only first-order MD), Na-layer antisite occupancy.
- **Geometry-sensitive dimensions**: Na 2b/2d have no free coordinates (special positions), the O z has been refined; no two-scheme side-by-side comparison was done (no split sites).
- **Untried dimensions**: interlayer cation mixing (D-06), oxygen-vacancy ordering (D-07), higher-order background — these are all "untried" rather than "impossible to improve".
- **Conclusion criterion**: within the range tried, wR fell to 9.82% (target met); the untried items above do not exclude further room for fine-tuning.

## Deliverables

Directory `LayeredOxide_final/`:
- `LayeredOxide_final.gpx` (clean GSAS project, do not refine again)
- `LayeredOxide_final.lst` (refinement log)
- `LayeredOxide_fit.png` (refinement figure, wR=9.82%)
- `LayeredOxide_report.md` (machine report)
- `LayeredOxide_built.cif` (main phase, official export)
- `LayeredOxide_sodium_molybdate.cif` (impurity phase)

## Conclusion

The main phase is the **P2-type layered oxide Na₀.₇₂(Ni₀.₃₃Mn₀.₆₂Mo₀.₀₅)O₂ (P 6₃/m m c, a=2.889 Å, c=11.134 Å)**, containing about 25 wt% Na₂MoO₄ impurity. The two-phase Rietveld refinement in GSAS-II converged to **wR = 9.82%**, meeting the publication-level target (≤10), with GOF=1.98 and physically reasonable structural parameters (no negative Uiso, occupancy conserved).

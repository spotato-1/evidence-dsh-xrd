# Fe₂O₃ + Fe₃O₄ two-phase mixed sample XRD Rietveld refinement report

**Sample**: a weighed two-phase mixture of α-Fe₂O₃ (hematite) + Fe₃O₄ (magnetite)　**Data**: Panalytical X'Pert PRO, Bragg-Brentano geometry, Cu Kα (40 kV / 30 mA, no monochromator ⇒ Kα1/Kα2 doublet, λ₁=1.54056 Å / λ₂=1.54439 Å / I₂/I₁=0.5), 10.013–119.967° 2θ, step 0.026°, 4230 data points
**Target (user)**: publication-grade refinement, R ≤ 10 — **achieved**

---

## 1. Goodness of fit (final delivery: GSAS-II)

| Metric | Value |
| --- | --- |
| **wR (Rwp)** | **2.35 %** |
| R (profile) | 1.76 % |
| Rb / wRb | 2.57 % / 3.28 % |
| wRmin (statistical limit) | 0.89 % |
| GOF (χ²) | 2.63 |
| Observed points / refined parameters | 4230 / 18 |
| Durbin-Watson | 0.176 |

Target R ≤ 10: **wR = 2.35 %, far below the target line** (about 1/4 of the target). Corroboration: the manual engine (bounded LM) gives Rwp = 2.30 % for the same model.

## 2. Phase composition and quantification

| Phase | Space group | Unit cell (Å) | Volume (Å³) | **Mass fraction** | Microstrain |
| --- | --- | --- | --- | --- | --- |
| α-Fe₂O₃ hematite (main phase) | R-3c | a=5.03666(36), c=13.7543(8) | 302.172(35) | **64.7(7) wt%** | — |
| Fe₃O₄ magnetite | Fd-3m | a=8.38713(65) | 589.98(14) | **35.3(7) wt%** | 4248(306)×10⁻⁶ (isotropic) |

- The hematite cell agrees with the ambient-pressure literature values of Maslen et al. (1994) (a=5.0356, c=13.7489) to <0.04%.
- The magnetite a is contracted by 0.11% relative to the Fleet (1981) literature value of 8.3967 (significant at 15σ). **Occupancy discrimination test** (only the Fe occupancy of the 16d site released): least squares pushed it to 1.100(24) ("more than fully occupied", physically illegal), the opposite direction to the γ-Fe₃O₄-type B-site vacancy hypothesis, with ΔwR of only 0.007 — therefore it is judged that **there are no B-site vacancies and the material is stoichiometric Fe₃O₄**; the a contraction is reported as-is according to its esd (it may be a real cell difference of the sample / microabsorption / peak-shape detail, see the unmodelled items in §5).
- The phase fractions 64.7 : 35.3 are of the same order as the "70-30" implied by the data source file name; the refined values are authoritative (the difference may come from weighing or from the Brindley microabsorption effect; no absorption correction was applied).

## 3. Structural parameters (GSAS-II, magnetite described with origin choice 2)

**Hematite** (Fe 12c, O 18e):

| Site | x | y | z | Occupancy | Uiso (Å²) |
| --- | --- | --- | --- | --- | --- |
| Fe1 | 0 | 0 | 0.35522(24) | 1 | 0.005* |
| O2 | 0.31514(222) | 0 | 0.25 | 1 | 0.005* |

**Magnetite** (Fe_A 8a, Fe_B 16d, O 32e; density 5.213 g/cm³):

| Site | x | y | z | Occupancy | Uiso (Å²) |
| --- | --- | --- | --- | --- | --- |
| Fe1 (tetrahedral A) | 0.125 | 0.125 | 0.125 | 1 | 0.010* |
| Fe2 (octahedral B) | 0.5 | 0.5 | 0.5 | 1 | 0.010* |
| O3 | 0.2548 | 0.2548 | 0.2548 | 1 | 0.010* |

\* **The thermal parameters are nominal values (not refined values)**: releasing the hematite Uiso for refinement immediately converges to a negative value (overfitting compensation; it was clamped to the physical lower bound 0.005 and frozen); releasing the magnetite Uiso makes wR worse (insufficient information from the weak phase), so it is kept at 0.01. Refining the magnetite O x(32e) was likewise rejected (wR became worse), and the literature value 0.2548 is kept. This is a limitation on the information content regarding thermal parameters / the weak phase's internal coordinates for this data set, not a defect of the model.

**Instrument/sample** (Bragg-Brentano, Cu Kα doublet): U=52.9(14), V=-23.2(14), W=9.97(40) (centideg²), X=9.04(9), Y=-18.45(24), Zero=0.1429(17)°; background Chebyshev order 6.

## 4. Refinement path (traceable)

1. **Stages 1–3**: visual + numerical dual peak determination confirmed the two phases; the CIFs were built from literature ambient-pressure parameters (build_orbit, hematite Maslen1994 / magnetite Fleet1981), and the symmetry, occupancy audit and Fe–O coordination (8× tetrahedral 1.888 Å + 16× octahedral 2.060 Å) all passed verification.
2. **Stage 4-Ⅰ**: FullProf fp2k single-phase scoring verified both structures (all peak positions hit).
3. **Stage 4-Ⅱ**: the manual engine (bounded LM) two-phase fit converged at Rwp=2.30% (both phases settled, phase fraction/cell/peak shape within bounds).
4. **Stage 4-Ⅲ**: handoff into GSAS-II (phase fraction/main-phase cell/instrument-parameter seeds), stepped refinement (background→cell→scale→atoms→instrument U/V/W/X/Y/Zero→microstrain) to wR=2.35%; negative-Uiso clamping fix; occupancy discrimination test confirmed stoichiometry.
5. **Stage 5**: delivery package packed (no parameter was changed afterwards).

The complete round-by-round record is in `xrd_workflow/journal.jsonl` and the overview `xrd_workflow/journal.md`.

## 5. Honesty statement (unmodelled items / coverage)

- **Unmodelled/nominalised items**: ① SH/L axial-divergence asymmetry and sample-height displacement (Shift) were not refined — the remaining mismatch at GOF 2.63 is mainly peak-shape detail at the strong peaks (the residual spikes are all at already-modelled peak positions, with no unexplained peaks); ② the thermal parameters are nominal values (see the note in §3); ③ microabsorption (Brindley) correction was not applied (it can affect the phase fractions by ~1–2 wt%); ④ Kα2 was modelled as a doublet with a fixed ratio (no fine RaCONvolut line shape).
- **Parameter-family coverage**: released — background (order 6), both phases' cells, both phases' scales, hematite coordinates (Fe z / O x), instrument U/V/W/X/Y/Zero, magnetite isotropic microstrain, occupancies (discrimination test). Not released — SH/L, Shift, preferred orientation (no evidence of orientation), anisotropic broadening, magnetite internal coordinates (releasing them immediately makes the fit worse).
- **Background order**: order 6 (default), not raised — wR 2.35 already far exceeds the target, so raising the order is unnecessary (coverage statement: no background-order upgrade was performed).
- **Bound-hit record**: in round 1 of the manual engine both scales sat at the upper bound (R 96.42 invalid, already re-run); the occupancy test value of 1.100 going out of bounds is the expected discriminative outcome (the physical model has been restored to occ=1.0).
- **Convention**: FullProf fp2k and manual-engine Rwp are not directly comparable with GSAS wR; the delivered values in this report are in the GSAS-II convention.

## 6. Deliverables (all inside the data folder)

| File | Description |
| --- | --- |
| `Fe2O3_Fe3O4_final/Fe2O3_Fe3O4_final.gpx` | Clean converged project (GSAS-II 5839; **do not open with an older version / do not refine again**, do not rename) |
| `Fe2O3_Fe3O4_final/Fe2O3_Fe3O4_final.lst` | Refinement log (including all esd) |
| `Fe2O3_Fe3O4_final/Fe2O3_Fe3O4_fit.png` | Publication-grade fit figure (obs/calc/difference + two-phase peak-position ticks + hkl labels) |
| `Fe2O3_Fe3O4_final/Fe2O3_Fe3O4_built.cif` / `_built_1.cif` | Two-phase CIFs (generated by the official GSAS-II export_CIF) |
| `Fe2O3_Fe3O4_final/Fe2O3_Fe3O4_report.md` | Metrics/cell/atom/strong-reflection tables |
| `xrd_workflow/journal.jsonl` + `journal.md` | Authoritative round-by-round record + summary sections |
| `work/gsas/Fe2O3_Fe3O4_physical.gpx` | Physical-model working project (start from this project if further refinement is needed) |
| `Fe2O3_hematite_orbit_01.cif` / `Fe3O4_magnetite_o1_orbit_01.cif` | Two-phase starting structure models (built from literature parameters) |
| `review_judgment.md` / `review_mechanical_Fe2O3_Fe3O4.json` | Refinement-process review records |

## 7. Tool-layer lessons (reusable across samples)

1. **Spinel origin trap**: pymatgen/gemmi's "Fd-3m" = origin choice 1, FullProf/CIFs_to_PCR = origin choice 2 (and it ignores the CIF symmetry-operation block); GSAS-II reads the CIF symmetry-operation block and automatically applies the 1→2 translation. Magnetite-type structures sent to FullProf must use origin-2 coordinates (Fe_A ⅛, Fe_B ½, O x≈0.2548), while those sent to pymatgen/GSAS use origin-1 (Fe_A 0, Fe_B ⅝, O x≈0.3798). A cif_to_pcr occupancy audit reporting fail when the origins do not match is a false alarm, and the multiplicity must be verified by reading the pcr text directly.
2. **pcr data-range line**: the Thmin/Step/Thmax written by CIFs_to_PCR are default values (11/0.02/120) and must be manually changed to the actual data values, otherwise Rwp≈100%.
3. **GSAS instprm comments**: only one line of '#' comment is allowed (ReadInstprm crashes on a split when there are two consecutive comment lines).
4. **Manual engine twophase stage**: the default vary set does not include background terms, so bg0 must be given explicitly (the 6th-order background is then automatically fully opened).
5. **handoff ladder**: the stepped ladder of xrd_refine_gsas with phases[] does not include an inst step; the instrument U/V/W/X/Y/Zero need a separate additional refinement round.

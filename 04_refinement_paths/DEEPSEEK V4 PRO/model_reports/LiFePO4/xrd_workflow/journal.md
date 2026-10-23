# XRD work log LiFePO4 (human-readable quick view)

| round | engine | stage | model | Rwp/wR | baseline R | verdict | why | artifacts |
|---|---|---|---|---|---|---|---|---|
| 1 | xrd_refine_auto (fp2k) | calibrate | physical | 22.8 (conventional) | 73.8 | progress | the full olivine Pnma structure ladder converged, Bragg R≈7.7%, the cell agrees with the literature | LiFePO4_olivine_orbit_01.pcr |
| 2 | xrd_refine_gsas | structure | physical | 10.24 (wR) | — | progress | pure olivine baseline, but 4 atoms have negative Uiso | gsas_proj.gpx |
| 3 | xrd_gsas_ops | structure | physical | 10.08 (wR) | 10.48 | R-value plateau | Li/Fe antisite introduced (occupancy conserved), x=4.91%, all physical properties reasonable | LiFePO4_final/ |

## Material and objective
- Material: LiFePO4 olivine (Pnma, #62), targeted to contain the Li/Fe antisite defect, lowest R value.
- Data: Rigaku SmartLab binary RAW → parsed as 2θ=10–80°, step 0.01°, 7001 points, Cu Kα (1.54056/1.54439, Kα2 doublet).

## Phase and crystal family (conclusion + basis + families excluded and why)
- Conclusion: LiFePO4 olivine Pnma. Basis: the measured peak positions 17.14/20.76/22.67/25.54/29.70/32.19/35.57/36.51/42.19° correspond one-to-one with the olivine (200)(101)(210)(111)(211)(301)(311)(121)(112); confirmed by fp2k Bragg R≈7.7% and GSAS Bragg R≈5.1%.
- Families excluded: among the 10 LiFePO4 structures returned by MP, P1/P-1/Cc/Imma/P6₄22/P2₁/c etc. (cell volumes of 341 Å³ etc. do not match the measurement), none is the phase of this sample.

## Master list of defects (exhaustive → screening → execution)
- Li/Fe antisite (applicable): interchange of Li at the 4a site ↔ Fe at the 4c site. Execution: GSAS-II set_site_composition + conserve_afrac (site sum=1) + equiv_afrac (Fe_on_Li=Li_on_Fe). Result x=4.91%.
- Other defects (not applicable/not evidenced): Li vacancies, Fe valence state, oxygen vacancies — no input evidence, not refined (need XPS/EDS/Mössbauer corroboration).

## Results achieved (R and criterion written separately)
- fp2k (FullProf) conventional Rwp = 22.8% (Bragg R ≈ 7.7%).
- GSAS-II wR = 10.08% (R=7.39%, Rb=10.25%, GOF=1.64, wRmin=6.15%).
- The two criteria are not directly comparable. Delivery uses GSAS-II wR=10.08%.
- Antisite fraction x = 4.91% ((Li0.9509Fe0.0491)(Fe0.9509Li0.0491)PO4); cell a=10.3366(2), b=6.0118(1), c=4.6966(1) Å.

## Untried · undecided items
- Untried: anisotropic thermal parameters (ADP), preferred orientation, higher-order background (>10), Williamson-Hall microstrain separation.
- Undecided: the antisite fraction is correlated with the Fe Uiso, with an intrinsic uncertainty of about ±1% (when Uiso is released the antisite drifts to 8–10% and Uiso becomes negative); the Fe valence state/Li vacancies need supplementary characterisation to confirm.

## Suggestions for the next handler
- The deliverable package is in `LiFePO4_final/` (clean gpx + lst + CIF + fit figure + report.md).
- To push R further down: give priority to the anisotropic thermal parameters (Fe) and preferred orientation; the background has already been raised to 10th order, and wR still has room down to wRmin=6.15% but is limited by the information content of the data.
- A publication-grade determination of the antisite fraction is recommended in combination with neutron diffraction or Mössbauer/XPS.

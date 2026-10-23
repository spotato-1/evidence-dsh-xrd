# Fe2O3_Fe3O4_2ph - final refinement deliverable

- generated: 2026-10-11 15:32:52
- engine: GSAS-II 5839 (scripting interface, not GUI)
- source project: `workspace\DEEPSEEK V4 PRO\Fe2O3_Fe3O4_2ph\gsas_proj_continued.gpx`
- histogram: `PWDR pattern.fxye Bank 1`
- refinement log: `Fe2O3_Fe3O4_2ph_final.lst`

## 1. Goodness of fit

| metric | value |
| --- | --- |
| Rwp (%) | 1.6 |
| R (%) | 1.226 |
| Rb (%) | 1.826 |
| wRb (%) | 2.93 |
| wRmin (%) | 0.8926 |
| chi**2 | 1.359e+04 |
| GOF | 1.8 |

## 2. Phases and cells

| phase | space group | a | b | c | alpha | beta | gamma | V |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| built | R -3 c | 5.0366(0.0003) | 5.0366(0.0003) | 13.7540(0.0005) | 90.000 | 90.000 | 120.000 | 302.155(0.025) |
| built_1 | F d -3 m | 8.3869(0.0005) | 8.3869(0.0005) | 8.3869(0.0005) | 90.000 | 90.000 | 90.000 | 589.939(0.100) |

## 3. Atom parameters

| phase | label | element | x | y | z | Occ | Mult | Uiso | flag |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| built | Fe1 | Fe | 0.00000 | 0.00000 | 0.35530 | 1.0000 | 12 | 0.0103 | U |
| built | O2 | O | 0.30590 | 0.00000 | 0.25000 | 1.0000 | 18 | 0.0083 | U |
| built_1 | Fe1 | Fe | 0.37500 | 0.37500 | 0.37500 | 1.0000 | 8 | 0.0475 | U |
| built_1 | Fe2 | Fe | 0.00000 | 0.00000 | 0.00000 | 1.0000 | 16 | 0.0067 | U |
| built_1 | O3 | O | 0.24520 | 0.24520 | 0.24520 | 1.0000 | 32 | 0.0568 | U |

## 4. Strongest reflections (top 15 by Icorr)

**built**

| hkl | 2-theta (deg) | Icorr |
| --- | --- | --- |
| (10-2) | 24.2840 | 10.25 |
| (113) | 40.9921 | 7.08 |
| (104) | 33.2902 | 5.40 |
| (110) | 35.7638 | 4.67 |
| (116) | 54.1937 | 4.06 |
| (211) | 56.2855 | 3.77 |
| (21-2) | 57.5743 | 3.61 |
| (202) | 43.6386 | 3.12 |
| (214) | 62.5598 | 3.10 |
| (21-5) | 66.1528 | 2.80 |
| (20-4) | 49.5899 | 2.42 |
| (119) | 72.3974 | 2.41 |
| (217) | 75.3083 | 2.27 |
| (223) | 78.8934 | 2.13 |
| (31-1) | 79.6047 | 2.11 |

**built_1**

| hkl | 2-theta (deg) | Icorr |
| --- | --- | --- |
| (111) | 18.4488 | 3.70 |
| (311) | 35.6114 | 2.93 |
| (220) | 30.2552 | 2.04 |
| (531) | 65.9662 | 1.75 |
| (331) | 47.3404 | 1.65 |
| (422) | 53.6215 | 1.29 |
| (642) | 86.9742 | 1.18 |
| (731) | 89.8756 | 1.15 |
| (842) | 114.7941 | 1.14 |
| (511) | 57.1515 | 1.14 |
| (753) | 113.7350 | 1.13 |
| (751) | 105.5253 | 1.09 |
| (222) | 37.2448 | 0.89 |
| (442) | 67.0215 | 0.85 |
| (620) | 71.1652 | 0.77 |

## 5. Deliverable validation

| check | result |
| --- | --- |
| written by GSAS-II | 5839 static 87e7f2c4 |
| source constraints (Hist/HAP/Phase) | 0 / 0 / 0 |
| constraints in package | none |
| reopen: phases / histograms | 2 / 1 |
| reopen: cached wR | 1.60% |

> A .gpx is a GSAS-II pickle: never rename it, never edit it as text, and never open it with an OLDER GSAS-II than the version above (older builds report "not a current GSAS-II .gpx").
> Stale constraints were cleared as deliverable hygiene - do NOT re-refine this project afterwards, or the cached converged wR is lost.

## 6. Package contents

- `Fe2O3_Fe3O4_2ph_final.gpx`
- `Fe2O3_Fe3O4_2ph_final.lst`
- `Fe2O3_Fe3O4_2ph_fit.png`
- `Fe2O3_Fe3O4_2ph_report.md`
- `Fe2O3_Fe3O4_2ph_built.cif`
- `Fe2O3_Fe3O4_2ph_built_1.cif`

## 7. Notes

- Packaging only: no refinement parameter was changed and no refinement was run.
- CIF files are produced by the official GSAS-II exporter `G2Phase.export_CIF` (never hand-written).
- One row of reflection ticks per phase (peak assignment); the strongest peaks carry hkl labels whose heights are staggered to avoid mutual overlap.
- Legend and statistics box are placed by data occupancy in the four corners, and the top of the main panel is padded, so peaks are never covered.

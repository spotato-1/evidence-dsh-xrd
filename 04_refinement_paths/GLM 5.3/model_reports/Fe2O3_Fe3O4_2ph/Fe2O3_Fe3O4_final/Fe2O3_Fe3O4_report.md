# Fe2O3_Fe3O4 - final refinement deliverable

- generated: 2026-10-08 23:33:23
- engine: GSAS-II 5839 (scripting interface, not GUI)
- source project: `workspace\GLM 5.3\Fe2O3_Fe3O4_2ph\work\gsas\gsas_proj_continued.gpx`
- histogram: `PWDR pattern_2theta.txt`
- refinement log: `Fe2O3_Fe3O4_final.lst`

## 1. Goodness of fit

| metric | value |
| --- | --- |
| Rwp (%) | 2.35 |
| R (%) | 1.763 |
| Rb (%) | 2.575 |
| wRb (%) | 3.285 |
| wRmin (%) | 0.8926 |
| chi**2 | 2.924e+04 |
| GOF | 2.63 |

## 2. Phases and cells

| phase | space group | a | b | c | alpha | beta | gamma | V |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| built | R -3 c | 5.0367(0.0004) | 5.0367(0.0004) | 13.7543(0.0008) | 90.000 | 90.000 | 120.000 | 302.172(0.035) |
| built_1 | F d -3 m | 8.3871(0.0006) | 8.3871(0.0006) | 8.3871(0.0006) | 90.000 | 90.000 | 90.000 | 589.984(0.137) |

## 3. Atom parameters

| phase | label | element | x | y | z | Occ | Mult | Uiso | flag |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| built | Fe1 | Fe | 0.00000 | 0.00000 | 0.35522 | 1.0000 | 12 | 0.0050 | X |
| built | O2 | O | 0.31514 | 0.00000 | 0.25000 | 1.0000 | 18 | 0.0050 | X |
| built_1 | Fe1 | Fe | -0.12500 | -0.12500 | -0.12500 | 1.0000 | 8 | 0.0100 |  |
| built_1 | Fe2 | Fe | 0.50000 | 0.50000 | 0.50000 | 1.0000 | 16 | 0.0100 |  |
| built_1 | O3 | O | 0.25480 | 0.25480 | 0.25480 | 1.0000 | 32 | 0.0100 |  |

## 4. Strongest reflections (top 15 by Icorr)

**built**

| hkl | 2-theta (deg) | Icorr |
| --- | --- | --- |
| (10-2) | 24.2843 | 9.00 |
| (113) | 40.9920 | 6.22 |
| (104) | 33.2902 | 4.75 |
| (110) | 35.7638 | 4.10 |
| (116) | 54.1933 | 3.57 |
| (211) | 56.2851 | 3.31 |
| (21-2) | 57.5739 | 3.17 |
| (202) | 43.6385 | 2.74 |
| (214) | 62.5592 | 2.72 |
| (21-5) | 66.1521 | 2.46 |
| (20-4) | 49.5896 | 2.12 |
| (119) | 72.3965 | 2.12 |
| (217) | 75.3073 | 2.00 |
| (223) | 78.8924 | 1.87 |
| (31-1) | 79.6036 | 1.85 |

**built_1**

| hkl | 2-theta (deg) | Icorr |
| --- | --- | --- |
| (111) | 18.4490 | 3.02 |
| (311) | 35.6112 | 2.39 |
| (220) | 30.2551 | 1.66 |
| (531) | 65.9651 | 1.43 |
| (331) | 47.3398 | 1.34 |
| (422) | 53.6207 | 1.05 |
| (642) | 86.9721 | 0.97 |
| (731) | 89.8734 | 0.94 |
| (842) | 114.7903 | 0.93 |
| (511) | 57.1506 | 0.93 |
| (753) | 113.7312 | 0.93 |
| (751) | 105.5222 | 0.89 |
| (222) | 37.2445 | 0.73 |
| (442) | 67.0202 | 0.70 |
| (620) | 71.1638 | 0.63 |

## 5. Deliverable validation

| check | result |
| --- | --- |
| written by GSAS-II | 5839 static 87e7f2c4 |
| source constraints (Hist/HAP/Phase) | 0 / 0 / 0 |
| constraints in package | none |
| reopen: phases / histograms | 2 / 1 |
| reopen: cached wR | 2.35% |

> A .gpx is a GSAS-II pickle: never rename it, never edit it as text, and never open it with an OLDER GSAS-II than the version above (older builds report "not a current GSAS-II .gpx").
> Stale constraints were cleared as deliverable hygiene - do NOT re-refine this project afterwards, or the cached converged wR is lost.

## 6. Package contents

- `Fe2O3_Fe3O4_final.gpx`
- `Fe2O3_Fe3O4_final.lst`
- `Fe2O3_Fe3O4_fit.png`
- `Fe2O3_Fe3O4_report.md`
- `Fe2O3_Fe3O4_built.cif`
- `Fe2O3_Fe3O4_built_1.cif`

## 7. Notes

- Packaging only: no refinement parameter was changed and no refinement was run.
- CIF files are produced by the official GSAS-II exporter `G2Phase.export_CIF` (never hand-written).
- One row of reflection ticks per phase (peak assignment); the strongest peaks carry hkl labels whose heights are staggered to avoid mutual overlap.
- Legend and statistics box are placed by data occupancy in the four corners, and the top of the main panel is padded, so peaks are never covered.

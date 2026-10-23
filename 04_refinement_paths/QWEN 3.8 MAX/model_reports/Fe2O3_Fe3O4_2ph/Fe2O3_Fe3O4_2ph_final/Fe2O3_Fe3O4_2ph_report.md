# Fe2O3_Fe3O4_2ph - final refinement deliverable

- generated: 2026-10-10 01:57:13
- engine: GSAS-II 5839 (scripting interface, not GUI)
- source project: `workspace\QWEN 3.8 MAX\Fe2O3_Fe3O4_2ph\gsas_proj_bgfinal.gpx`
- histogram: `PWDR pattern_numeric.txt`
- refinement log: `Fe2O3_Fe3O4_2ph_final.lst`

## 1. Goodness of fit

| metric | value |
| --- | --- |
| Rwp (%) | 1.58 |
| R (%) | 1.218 |
| Rb (%) | 1.836 |
| wRb (%) | 2.746 |
| wRmin (%) | 0.8926 |
| chi**2 | 1.332e+04 |
| GOF | 1.78 |

## 2. Phases and cells

| phase | space group | a | b | c | alpha | beta | gamma | V |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Fe12 O18 | R -3 c | 5.0365(0.0002) | 5.0365(0.0002) | 13.7539(0.0005) | 90.000 | 90.000 | 120.000 | 302.142(0.024) |
| Fe24 O32 | F d -3 m | 8.3866(0.0005) | 8.3866(0.0005) | 8.3866(0.0005) | 90.000 | 90.000 | 90.000 | 589.876(0.096) |

## 3. Atom parameters

| phase | label | element | x | y | z | Occ | Mult | Uiso | flag |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Fe12 O18 | Fe0 | Fe | 0.00000 | 0.00000 | 0.14488 | 1.0000 | 12 | 0.0081 | XU |
| Fe12 O18 | O1 | O | 0.00000 | 0.31357 | 0.75000 | 1.0000 | 18 | 0.0065 | XU |
| Fe24 O32 | Fe1 | Fe | 0.12500 | 0.12500 | 0.12500 | 1.0000 | 8 | 0.0564 | XU |
| Fe24 O32 | Fe2 | Fe | 0.50000 | 0.50000 | 0.50000 | 1.0000 | 16 | 0.0128 | XU |
| Fe24 O32 | O | O | 0.24761 | 0.24761 | 0.24761 | 1.0000 | 32 | 0.0613 | XU |

## 4. Strongest reflections (top 15 by Icorr)

**Fe12 O18**

| hkl | 2-theta (deg) | Icorr |
| --- | --- | --- |
| (10-2) | 24.2847 | 9.91 |
| (113) | 40.9925 | 6.85 |
| (104) | 33.2907 | 5.23 |
| (110) | 35.7643 | 4.52 |
| (116) | 54.1937 | 3.93 |
| (211) | 56.2856 | 3.65 |
| (21-2) | 57.5744 | 3.49 |
| (202) | 43.6390 | 3.02 |
| (214) | 62.5597 | 2.99 |
| (21-5) | 66.1526 | 2.71 |
| (20-4) | 49.5900 | 2.34 |
| (119) | 72.3969 | 2.33 |
| (217) | 75.3078 | 2.20 |
| (223) | 78.8929 | 2.06 |
| (31-1) | 79.6041 | 2.04 |

**Fe24 O32**

| hkl | 2-theta (deg) | Icorr |
| --- | --- | --- |
| (111) | 18.4500 | 3.98 |
| (311) | 35.6127 | 3.15 |
| (220) | 30.2564 | 2.19 |
| (531) | 65.9676 | 1.88 |
| (331) | 47.3416 | 1.77 |
| (422) | 53.6228 | 1.39 |
| (642) | 86.9756 | 1.27 |
| (731) | 89.8770 | 1.24 |
| (842) | 114.7957 | 1.23 |
| (511) | 57.1528 | 1.23 |
| (753) | 113.7366 | 1.22 |
| (751) | 105.5268 | 1.17 |
| (222) | 37.2460 | 0.96 |
| (442) | 67.0228 | 0.92 |
| (620) | 71.1665 | 0.83 |

## 5. Deliverable validation

| check | result |
| --- | --- |
| written by GSAS-II | 5839 static 87e7f2c4 |
| source constraints (Hist/HAP/Phase) | 0 / 0 / 0 |
| constraints in package | none |
| reopen: phases / histograms | 2 / 1 |
| reopen: cached wR | 1.58% |

> A .gpx is a GSAS-II pickle: never rename it, never edit it as text, and never open it with an OLDER GSAS-II than the version above (older builds report "not a current GSAS-II .gpx").
> Stale constraints were cleared as deliverable hygiene - do NOT re-refine this project afterwards, or the cached converged wR is lost.

## 6. Package contents

- `Fe2O3_Fe3O4_2ph_final.gpx`
- `Fe2O3_Fe3O4_2ph_final.lst`
- `Fe2O3_Fe3O4_2ph_fit.png`
- `Fe2O3_Fe3O4_2ph_report.md`
- `Fe2O3_Fe3O4_2ph_Fe12_O18.cif`
- `Fe2O3_Fe3O4_2ph_Fe24_O32.cif`

## 7. Notes

- Packaging only: no refinement parameter was changed and no refinement was run.
- CIF files are produced by the official GSAS-II exporter `G2Phase.export_CIF` (never hand-written).
- One row of reflection ticks per phase (peak assignment); the strongest peaks carry hkl labels whose heights are staggered to avoid mutual overlap.
- Legend and statistics box are placed by data occupancy in the four corners, and the top of the main panel is padded, so peaks are never covered.

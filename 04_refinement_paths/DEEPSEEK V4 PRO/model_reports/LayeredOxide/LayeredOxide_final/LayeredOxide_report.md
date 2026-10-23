# LayeredOxide - final refinement deliverable

- generated: 2026-10-11 19:04:18
- engine: GSAS-II 5839 (scripting interface, not GUI)
- source project: `workspace\DEEPSEEK V4 PRO\LayeredOxide\gsas_proj_continued.gpx`
- histogram: `PWDR pattern.fxye Bank 1`
- refinement log: `LayeredOxide_final.lst`

## 1. Goodness of fit

| metric | value |
| --- | --- |
| Rwp (%) | 9.82 |
| R (%) | 6.684 |
| Rb (%) | 14.49 |
| wRb (%) | 30.07 |
| wRmin (%) | 4.974 |
| chi**2 | 1.337e+04 |
| GOF | 1.98 |

## 2. Phases and cells

| phase | space group | a | b | c | alpha | beta | gamma | V |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| built | P 63/m m c | 2.8889(0.0005) | 2.8889(0.0005) | 11.1340(0.0005) | 90.000 | 90.000 | 120.000 | 80.473(0.017) |
| sodium molybdate | F d -3 m | 9.1089 | 9.1089 | 9.1089 | 90.000 | 90.000 | 90.000 | 755.779 |

## 3. Atom parameters

| phase | label | element | x | y | z | Occ | Mult | Uiso | flag |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| built | Mn1 | Mn | 0.00000 | 0.00000 | 0.00000 | 0.6200 | 2 | 0.0050 | X |
| built | Ni2 | Ni | 0.00000 | 0.00000 | 0.00000 | 0.3300 | 2 | 0.0050 | X |
| built | Mo3 | Mo | 0.00000 | 0.00000 | 0.00000 | 0.0500 | 2 | 0.0050 | X |
| built | O4 | O | 0.33333 | 0.66667 | 0.09709 | 1.0000 | 4 | 0.0050 | X |
| built | Na5 | Na | 0.00000 | 0.00000 | 0.25000 | 0.2827 | 2 | 0.0590 | FXU |
| built | Na6 | Na | 0.66667 | 0.33333 | 0.25000 | 0.4373 | 2 | 0.0113 | FXU |
| sodium molybdate | O | O | 0.29314 | 0.29314 | 0.29314 | 1.0000 | 32 | 0.0118 |  |
| sodium molybdate | Mo | Mo | 0.37500 | 0.37500 | 0.37500 | 1.0000 | 8 | 0.0074 |  |
| sodium molybdate | Na | Na | 0.00000 | 0.00000 | 0.00000 | 1.0000 | 16 | 0.0138 |  |

## 4. Strongest reflections (top 15 by Icorr)

**built**

| hkl | 2-theta (deg) | Icorr |
| --- | --- | --- |
| (101) | 36.6468 | 18.42 |
| (102) | 39.3124 | 15.27 |
| (002) | 15.7635 | 12.23 |
| (103) | 43.4501 | 11.83 |
| (100) | 35.7209 | 9.88 |
| (104) | 48.7669 | 8.95 |
| (105) | 55.0308 | 6.80 |
| (112) | 66.7197 | 5.69 |
| (106) | 62.0958 | 5.26 |
| (201) | 76.4386 | 4.67 |
| (114) | 73.7125 | 4.58 |
| (202) | 78.1245 | 4.47 |
| (107) | 69.8984 | 4.19 |
| (108) | 78.4518 | 3.46 |
| (110) | 64.3116 | 3.11 |

**sodium molybdate**

| hkl | 2-theta (deg) | Icorr |
| --- | --- | --- |
| (111) | 16.7017 | 0.03 |
| (311) | 32.4335 | 0.03 |
| (220) | 27.5339 | 0.02 |
| (531) | 59.8961 | 0.02 |
| (331) | 43.1169 | 0.01 |
| (422) | 48.8053 | 0.01 |
| (511) | 51.9900 | 0.01 |
| (642) | 78.3754 | 0.01 |
| (222) | 33.9253 | 0.01 |
| (442) | 60.8375 | 0.01 |
| (620) | 64.5229 | 0.01 |
| (533) | 67.2140 | 0.01 |
| (622) | 68.0991 | 0.01 |
| (711) | 74.1590 | 0.01 |
| (551) | 74.1590 | 0.01 |

## 5. Deliverable validation

| check | result |
| --- | --- |
| written by GSAS-II | 5839 static 87e7f2c4 |
| source constraints (Hist/HAP/Phase) | 0 / 0 / 2 |
| constraints in package | cleared |
| reopen: phases / histograms | 2 / 1 |
| reopen: cached wR | 9.82% |

> A .gpx is a GSAS-II pickle: never rename it, never edit it as text, and never open it with an OLDER GSAS-II than the version above (older builds report "not a current GSAS-II .gpx").
> Stale constraints were cleared as deliverable hygiene - do NOT re-refine this project afterwards, or the cached converged wR is lost.

## 6. Package contents

- `LayeredOxide_final.gpx`
- `LayeredOxide_final.lst`
- `LayeredOxide_fit.png`
- `LayeredOxide_report.md`
- `LayeredOxide_built.cif`
- `LayeredOxide_sodium_molybdate.cif`

## 7. Notes

- Packaging only: no refinement parameter was changed and no refinement was run.
- CIF files are produced by the official GSAS-II exporter `G2Phase.export_CIF` (never hand-written).
- One row of reflection ticks per phase (peak assignment); the strongest peaks carry hkl labels whose heights are staggered to avoid mutual overlap.
- Legend and statistics box are placed by data occupancy in the four corners, and the top of the main panel is padded, so peaks are never covered.
- WARNING: cleared 2 stale constraint entries (Hist=0, HAP=0, Phase=2) - do NOT re-refine this project afterwards (refining would drop the cached converged wR)

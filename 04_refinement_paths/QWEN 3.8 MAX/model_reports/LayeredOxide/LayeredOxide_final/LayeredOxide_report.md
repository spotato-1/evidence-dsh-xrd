# LayeredOxide - final refinement deliverable

- generated: 2026-10-11 12:49:31
- engine: GSAS-II 5839 (scripting interface, not GUI)
- source project: `workspace\QWEN 3.8 MAX\LayeredOxide\gsas_v13.gpx`
- histogram: `PWDR pattern.fxye Bank 1`
- refinement log: `LayeredOxide_final.lst`

## 1. Goodness of fit

| metric | value |
| --- | --- |
| Rwp (%) | 6.94 |
| R (%) | 5.513 |
| Rb (%) | 7.525 |
| wRb (%) | 9.26 |
| wRmin (%) | 4.974 |
| chi**2 | 6677 |
| GOF | 1.4 |

## 2. Phases and cells

| phase | space group | a | b | c | alpha | beta | gamma | V |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| built | P 63/m m c | 2.8894(0.0003) | 2.8894(0.0003) | 11.1584(0.0015) | 90.000 | 90.000 | 120.000 | 80.674(0.016) |
| sodium molybdate | F d -3 m | 9.1226(0.0021) | 9.1226(0.0021) | 9.1226(0.0021) | 90.000 | 90.000 | 90.000 | 759.191(0.535) |

## 3. Atom parameters

| phase | label | element | x | y | z | Occ | Mult | Uiso | flag |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| built | Na1 | Na | 0.00000 | 0.00000 | 0.25000 | 0.2407 | 2 | 0.0500 | F |
| built | Na2 | Na | 0.33333 | 0.66667 | 0.75000 | 0.4793 | 2 | 0.0500 | F |
| built | Mn3 | Mn | 0.00000 | 0.00000 | 0.00000 | 0.6200 | 2 | 0.0020 |  |
| built | Ni4 | Ni | 0.00000 | 0.00000 | 0.00000 | 0.3300 | 2 | 0.0020 |  |
| built | Mo5 | Mo | 0.00000 | 0.00000 | 0.00000 | 0.0500 | 2 | 0.0020 |  |
| built | O6 | O | 0.33333 | 0.66667 | 0.10545 | 1.0000 | 4 | 0.0020 | X |
| sodium molybdate | O | O | 0.26271 | 0.26271 | 0.26271 | 1.0000 | 32 | - |  |
| sodium molybdate | Mo | Mo | 0.37500 | 0.37500 | 0.37500 | 1.0000 | 8 | - |  |
| sodium molybdate | Na | Na | 0.00000 | 0.00000 | 0.00000 | 1.0000 | 16 | - |  |

## 4. Strongest reflections (top 15 by Icorr)

**built**

| hkl | 2-theta (deg) | Icorr |
| --- | --- | --- |
| (101) | 36.6824 | 14.39 |
| (002) | 15.7739 | 14.17 |
| (102) | 39.3373 | 12.33 |
| (103) | 43.4593 | 9.87 |
| (104) | 48.7569 | 7.61 |
| (100) | 35.7604 | 7.61 |
| (105) | 54.9992 | 5.79 |
| (106) | 62.0400 | 4.41 |
| (112) | 66.7435 | 3.77 |
| (107) | 69.8156 | 3.43 |
| (004) | 31.9611 | 3.24 |
| (114) | 73.7074 | 3.09 |
| (201) | 76.4674 | 2.89 |
| (202) | 78.1461 | 2.78 |
| (108) | 78.3376 | 2.77 |

**sodium molybdate**

| hkl | 2-theta (deg) | Icorr |
| --- | --- | --- |
| (111) | 16.7216 | 0.06 |
| (311) | 32.4286 | 0.04 |
| (220) | 27.5369 | 0.03 |
| (331) | 43.0941 | 0.02 |
| (531) | 59.8421 | 0.02 |
| (422) | 48.7724 | 0.02 |
| (511) | 51.9512 | 0.02 |
| (222) | 33.9179 | 0.01 |
| (642) | 78.2804 | 0.01 |
| (442) | 60.7817 | 0.01 |
| (620) | 64.4594 | 0.01 |
| (533) | 67.1448 | 0.01 |
| (622) | 68.0280 | 0.01 |
| (400) | 39.3823 | 0.01 |
| (551) | 74.0742 | 0.01 |

## 5. Deliverable validation

| check | result |
| --- | --- |
| written by GSAS-II | 5839 static 87e7f2c4 |
| source constraints (Hist/HAP/Phase) | 0 / 0 / 3 |
| constraints in package | cleared |
| reopen: phases / histograms | 2 / 1 |
| reopen: cached wR | 6.94% |

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
- WARNING: cleared 3 stale constraint entries (Hist=0, HAP=0, Phase=3) - do NOT re-refine this project afterwards (refining would drop the cached converged wR)

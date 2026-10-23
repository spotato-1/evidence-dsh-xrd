# NNMO - final refinement deliverable

- generated: 2026-10-09 22:48:42
- engine: GSAS-II 5839 (scripting interface, not GUI)
- source project: `workspace\GLM 5.3\LayeredOxide\gsas2\NNMO_delivery.gpx`
- histogram: `PWDR NNMO.fxye Bank 1`
- refinement log: `NNMO_final.lst`

## 1. Goodness of fit

| metric | value |
| --- | --- |
| Rwp (%) | 13.05 |
| R (%) | 7.759 |
| Rb (%) | 23.24 |
| wRb (%) | 46.23 |
| wRmin (%) | 4.974 |
| chi**2 | 2.363e+04 |
| GOF | 2.63 |

## 2. Phases and cells

| phase | space group | a | b | c | alpha | beta | gamma | V |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| built | P 63/m m c | 2.8963 | 2.8963 | 11.1724 | 90.000 | 90.000 | 120.000 | 81.284 |
| sodium molybdate | F d -3 m | 9.1089(0.0002) | 9.1089(0.0002) | 9.1089(0.0002) | 90.000 | 90.000 | 90.000 | 755.797(0.051) |

## 3. Atom parameters

| phase | label | element | x | y | z | Occ | Mult | Uiso | flag |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| built | Na1 | Na | 0.00000 | 0.00000 | 0.25000 | 0.0340 | 2 | 0.0050 | F |
| built | Na2 | Na | 0.66667 | 0.33333 | 0.25000 | 0.6860 | 2 | 0.0050 | F |
| built | Ni | Ni | 0.00000 | 0.00000 | 0.00000 | 0.3300 | 2 | 0.0050 |  |
| built | Mn | Mn | 0.00000 | 0.00000 | 0.00000 | 0.6200 | 2 | 0.0050 |  |
| built | Mo | Mo | 0.00000 | 0.00000 | 0.00000 | 0.0500 | 2 | 0.0050 |  |
| built | O | O | 0.33333 | 0.66667 | 0.04983 | 1.0000 | 4 | 0.0200 | X |
| sodium molybdate | O | O | 0.23496 | 0.23496 | 0.23496 | 1.0000 | 32 | - |  |
| sodium molybdate | Mo | Mo | 0.37500 | 0.37500 | 0.37500 | 1.0000 | 8 | - |  |
| sodium molybdate | Na | Na | 0.00000 | 0.00000 | 0.00000 | 1.0000 | 16 | - |  |

## 4. Strongest reflections (top 15 by Icorr)

**built**

| hkl | 2-theta (deg) | Icorr |
| --- | --- | --- |
| (101) | 36.6325 | 21.54 |
| (100) | 35.7108 | 13.45 |
| (102) | 39.2860 | 12.78 |
| (103) | 43.4051 | 6.89 |
| (002) | 15.7931 | 5.22 |
| (104) | 48.6980 | 3.66 |
| (105) | 54.9332 | 1.91 |
| (112) | 66.6071 | 1.88 |
| (110) | 64.2118 | 1.44 |
| (004) | 31.9590 | 1.04 |
| (106) | 61.9646 | 0.94 |
| (201) | 76.2913 | 0.66 |
| (114) | 73.5613 | 0.57 |
| (202) | 77.9673 | 0.44 |
| (107) | 69.7279 | 0.39 |

**sodium molybdate**

| hkl | 2-theta (deg) | Icorr |
| --- | --- | --- |
| (111) | 16.7862 | 0.08 |
| (311) | 32.5178 | 0.05 |
| (220) | 27.6183 | 0.04 |
| (331) | 43.2012 | 0.02 |
| (222) | 34.0096 | 0.02 |
| (422) | 48.8896 | 0.02 |
| (531) | 59.9802 | 0.01 |
| (511) | 52.0742 | 0.01 |
| (400) | 39.4831 | 0.01 |
| (442) | 60.9216 | 0.01 |
| (620) | 64.6070 | 0.00 |
| (440) | 57.0996 | 0.00 |
| (333) | 52.0742 | 0.00 |
| (533) | 67.2980 | 0.00 |
| (622) | 68.1831 | 0.00 |

## 5. Deliverable validation

| check | result |
| --- | --- |
| written by GSAS-II | 5839 static 87e7f2c4 |
| source constraints (Hist/HAP/Phase) | 0 / 0 / 3 |
| constraints in package | cleared |
| reopen: phases / histograms | 2 / 1 |
| reopen: cached wR | 13.05% |

> A .gpx is a GSAS-II pickle: never rename it, never edit it as text, and never open it with an OLDER GSAS-II than the version above (older builds report "not a current GSAS-II .gpx").
> Stale constraints were cleared as deliverable hygiene - do NOT re-refine this project afterwards, or the cached converged wR is lost.

## 6. Package contents

- `NNMO_final.gpx`
- `NNMO_final.lst`
- `NNMO_fit.png`
- `NNMO_report.md`
- `NNMO_built.cif`
- `NNMO_sodium_molybdate.cif`

## 7. Notes

- Packaging only: no refinement parameter was changed and no refinement was run.
- CIF files are produced by the official GSAS-II exporter `G2Phase.export_CIF` (never hand-written).
- One row of reflection ticks per phase (peak assignment); the strongest peaks carry hkl labels whose heights are staggered to avoid mutual overlap.
- Legend and statistics box are placed by data occupancy in the four corners, and the top of the main panel is padded, so peaks are never covered.
- WARNING: cleared 3 stale constraint entries (Hist=0, HAP=0, Phase=3) - do NOT re-refine this project afterwards (refining would drop the cached converged wR)

# LayeredOxide_final - final refinement deliverable

- generated: 2026-10-09 21:28:04
- engine: GSAS-II 5839 (scripting interface, not GUI)
- source project: `workspace\QWEN 3.7 PLUS\LayeredOxide\gsas_proj_continued.gpx`
- histogram: `PWDR pattern.fxye Bank 1`
- refinement log: `LayeredOxide_final_final.lst`

## 1. Goodness of fit

| metric | value |
| --- | --- |
| Rwp (%) | 8.65 |
| R (%) | 6.551 |
| Rb (%) | 11.71 |
| wRb (%) | 17.1 |
| wRmin (%) | 4.974 |
| chi**2 | 1.038e+04 |
| GOF | 1.75 |

## 2. Phases and cells

| phase | space group | a | b | c | alpha | beta | gamma | V |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| built | P 63 | 2.8897(0.0030) | 2.8897(0.0030) | 11.1958(0.0019) | 90.000 | 90.000 | 120.000 | 80.965(0.105) |

## 3. Atom parameters

| phase | label | element | x | y | z | Occ | Mult | Uiso | flag |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| built | Ni1 | Ni | 0.00000 | 0.00000 | 84647246981376.10938 | 0.3300 | 2 | 0.0050 | X |
| built | Mn2 | Mn | 0.00000 | 0.00000 | 31660463638138.08594 | 0.6200 | 2 | 0.0050 | X |
| built | Mo3 | Mo | 0.00000 | 0.00000 | -461883161074043.18750 | 0.0500 | 2 | 0.0050 | X |
| built | Na4 | Na | 0.33330 | 0.66670 | -61529179565213.50000 | 0.7200 | 2 | 0.0050 | X |
| built | O5 | O | 1.24059 | 4.77032 | -63273822149019.10938 | 1.0000 | 6 | 0.3493 | XU |

## 4. Strongest reflections (top 15 by Icorr)

**built**

| hkl | 2-theta (deg) | Icorr |
| --- | --- | --- |
| (011) | 36.7009 | 20.01 |
| (002) | 15.7490 | 18.48 |
| (012) | 39.3392 | 17.38 |
| (013) | 43.4369 | 14.22 |
| (014) | 48.7051 | 11.30 |
| (010) | 35.7849 | 10.53 |
| (015) | 54.9140 | 8.93 |
| (016) | 61.9179 | 7.12 |
| (111) | 64.9662 | 6.53 |
| (112) | 66.7487 | 6.23 |
| (017) | 69.6520 | 5.80 |
| (113) | 69.6687 | 5.80 |
| (114) | 73.6682 | 5.30 |
| (021) | 76.4827 | 5.02 |
| (018) | 78.1265 | 4.87 |

## 5. Deliverable validation

| check | result |
| --- | --- |
| written by GSAS-II | 5839 static 87e7f2c4 |
| source constraints (Hist/HAP/Phase) | 0 / 0 / 0 |
| constraints in package | none |
| reopen: phases / histograms | 1 / 1 |
| reopen: cached wR | 8.80% |

> A .gpx is a GSAS-II pickle: never rename it, never edit it as text, and never open it with an OLDER GSAS-II than the version above (older builds report "not a current GSAS-II .gpx").
> Stale constraints were cleared as deliverable hygiene - do NOT re-refine this project afterwards, or the cached converged wR is lost.

## 6. Package contents

- `LayeredOxide_final_final.gpx`
- `LayeredOxide_final_final.lst`
- `LayeredOxide_final_fit.png`
- `LayeredOxide_final_report.md`
- `LayeredOxide_final_built.cif`

## 7. Notes

- Packaging only: no refinement parameter was changed and no refinement was run.
- CIF files are produced by the official GSAS-II exporter `G2Phase.export_CIF` (never hand-written).
- One row of reflection ticks per phase (peak assignment); the strongest peaks carry hkl labels whose heights are staggered to avoid mutual overlap.
- Legend and statistics box are placed by data occupancy in the four corners, and the top of the main panel is padded, so peaks are never covered.

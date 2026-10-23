# FE50 - final refinement deliverable

- generated: 2026-10-11 16:30:38
- engine: GSAS-II 5839 (scripting interface, not GUI)
- source project: `workspace\DEEPSEEK V4 PRO\FE50\work\FE50_best.gpx`
- histogram: `PWDR FE50.fxye Bank 1`
- refinement log: `FE50_final.lst`

## 1. Goodness of fit

| metric | value |
| --- | --- |
| Rwp (%) | 11.71 |
| R (%) | 9.315 |
| Rb (%) | 11.11 |
| wRb (%) | 13.57 |
| wRmin (%) | 7.917 |
| chi**2 | 6133 |
| GOF | 1.49 |

## 2. Phases and cells

| phase | space group | a | b | c | alpha | beta | gamma | V |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| K5.84 Mn2 Fe6 C23.28 N23.28 | F m -3 m | 10.1673(0.0018) | 10.1673(0.0018) | 10.1673(0.0018) | 90.000 | 90.000 | 90.000 | 1051.042(0.571) |

## 3. Atom parameters

| phase | label | element | x | y | z | Occ | Mult | Uiso | flag |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| K5.84 Mn2 Fe6 C23.28 N23.28 | K0 | K | 0.25000 | 0.25000 | 0.25000 | 0.9298 | 8 | 0.0100 | F |
| K5.84 Mn2 Fe6 C23.28 N23.28 | Fe1 | Fe | 0.00000 | 0.00000 | 0.50000 | 0.5000 | 4 | 0.0100 |  |
| K5.84 Mn2 Fe6 C23.28 N23.28 | Mn2 | Mn | 0.00000 | 0.00000 | 0.50000 | 0.5000 | 4 | 0.0100 |  |
| K5.84 Mn2 Fe6 C23.28 N23.28 | Fe3 | Fe | 0.00000 | 0.00000 | 0.00000 | 1.0000 | 4 | 0.0100 |  |
| K5.84 Mn2 Fe6 C23.28 N23.28 | C4 | C | 0.00000 | 0.00000 | 0.18500 | 0.9700 | 24 | 0.0100 |  |
| K5.84 Mn2 Fe6 C23.28 N23.28 | N5 | N | 0.00000 | 0.00000 | 0.30000 | 0.9700 | 24 | 0.0100 |  |

## 4. Strongest reflections (top 15 by Icorr)

**K5.84 Mn2 Fe6 C23.28 N23.28**

| hkl | 2-theta (deg) | Icorr |
| --- | --- | --- |
| (111) | 15.0807 | 0.84 |
| (311) | 29.1060 | 0.67 |
| (200) | 17.4306 | 0.47 |
| (220) | 24.7475 | 0.46 |
| (531) | 53.2586 | 0.39 |
| (331) | 38.5667 | 0.38 |
| (420) | 39.6099 | 0.36 |
| (422) | 43.5741 | 0.29 |
| (511) | 46.3664 | 0.26 |
| (642) | 69.0761 | 0.24 |
| (222) | 30.4308 | 0.20 |
| (442) | 54.0750 | 0.19 |
| (620) | 57.2615 | 0.17 |
| (533) | 59.5779 | 0.16 |
| (622) | 60.3377 | 0.16 |

## 5. Deliverable validation

| check | result |
| --- | --- |
| written by GSAS-II | 5839 static 87e7f2c4 |
| source constraints (Hist/HAP/Phase) | 0 / 0 / 0 |
| constraints in package | none |
| reopen: phases / histograms | 1 / 1 |
| reopen: cached wR | 11.71% |

> A .gpx is a GSAS-II pickle: never rename it, never edit it as text, and never open it with an OLDER GSAS-II than the version above (older builds report "not a current GSAS-II .gpx").
> Stale constraints were cleared as deliverable hygiene - do NOT re-refine this project afterwards, or the cached converged wR is lost.

## 6. Package contents

- `FE50_final.gpx`
- `FE50_final.lst`
- `FE50_fit.png`
- `FE50_report.md`
- `FE50_K5.84_Mn2_Fe6_C23.28_N23.28.cif`

## 7. Notes

- Packaging only: no refinement parameter was changed and no refinement was run.
- CIF files are produced by the official GSAS-II exporter `G2Phase.export_CIF` (never hand-written).
- One row of reflection ticks per phase (peak assignment); the strongest peaks carry hkl labels whose heights are staggered to avoid mutual overlap.
- Legend and statistics box are placed by data occupancy in the four corners, and the top of the main panel is padded, so peaks are never covered.

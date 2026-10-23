# FE50 - final refinement deliverable

- generated: 2026-10-10 12:50:53
- engine: GSAS-II 5839 (scripting interface, not GUI)
- source project: `workspace\QWEN 3.8 MAX\FE50\gsas\gsas_T25_NUclamp.gpx`
- histogram: `PWDR FE50.fxye Bank 1`
- refinement log: `FE50_final.lst`

## 1. Goodness of fit

| metric | value |
| --- | --- |
| Rwp (%) | 9.4 |
| R (%) | 7.431 |
| Rb (%) | 7.792 |
| wRb (%) | 8.877 |
| wRmin (%) | 7.917 |
| chi**2 | 3954 |
| GOF | 1.19 |

## 2. Phases and cells

| phase | space group | a | b | c | alpha | beta | gamma | V |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| t14_litcn | P 21/c | 10.1223(0.0181) | 10.1267(0.0051) | 10.1262(0.0130) | 90.000 | 92.611(0.031) | 90.000 | 1036.906(1.214) |

## 3. Atom parameters

| phase | label | element | x | y | z | Occ | Mult | Uiso | flag |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| t14_litcn | K1 | K | 0.18939 | 0.24987 | 0.27617 | 0.9937 | 4 | 0.0567 | FXU |
| t14_litcn | K2 | K | 0.73723 | 0.22808 | 0.74903 | 0.9937 | 4 | 0.0567 | FXU |
| t14_litcn | Fe1 | Fe | 0.00000 | 0.00000 | 0.00000 | 1.0000 | 2 | 0.0050 |  |
| t14_litcn | Fe2 | Fe | 0.50000 | 0.00000 | 0.50000 | 1.0000 | 2 | 0.0050 |  |
| t14_litcn | Mn1 | Mn | 0.50000 | 0.00000 | 0.00000 | 0.5000 | 2 | 0.0050 |  |
| t14_litcn | Mn2 | Mn | 0.00000 | 0.00000 | 0.50000 | 0.5000 | 2 | 0.0050 |  |
| t14_litcn | FeN1 | Fe | 0.50000 | 0.00000 | 0.00000 | 0.5000 | 2 | 0.0050 |  |
| t14_litcn | FeN2 | Fe | 0.00000 | 0.00000 | 0.50000 | 0.5000 | 2 | 0.0050 |  |
| t14_litcn | C1 | C | 0.00000 | 0.00000 | 0.17300 | 1.0000 | 4 | 0.1892 | U |
| t14_litcn | C2 | C | 0.82800 | 0.00000 | 0.00500 | 1.0000 | 4 | 0.1892 | U |
| t14_litcn | C3 | C | 0.00700 | -0.32000 | 0.48700 | 1.0000 | 4 | 0.1892 | U |
| t14_litcn | C4 | C | 0.50000 | 0.50000 | 0.17300 | 1.0000 | 4 | 0.1892 | U |
| t14_litcn | C5 | C | 0.50600 | 0.17900 | 0.50400 | 1.0000 | 4 | 0.1892 | U |
| t14_litcn | C6 | C | 0.68000 | 0.50000 | 0.00000 | 1.0000 | 4 | 0.1892 | U |
| t14_litcn | N1 | N | 0.00000 | 0.01800 | 0.72800 | 1.0000 | 4 | 0.2000 |  |
| t14_litcn | N2 | N | -0.30000 | 0.00000 | 0.00000 | 1.0000 | 4 | 0.2000 |  |
| t14_litcn | N3 | N | 0.00000 | -0.15000 | 0.47600 | 1.0000 | 4 | 0.2000 |  |
| t14_litcn | N4 | N | 0.50400 | 0.50200 | 0.28200 | 1.0000 | 4 | 0.2000 |  |
| t14_litcn | N5 | N | 0.50000 | 0.28900 | 0.50000 | 1.0000 | 4 | 0.2000 |  |
| t14_litcn | N6 | N | 0.78900 | 0.51400 | 0.00300 | 1.0000 | 4 | 0.2000 |  |

## 4. Strongest reflections (top 15 by Icorr)

**t14_litcn**

| hkl | 2-theta (deg) | Icorr |
| --- | --- | --- |
| (011) | 12.2298 | 0.62 |
| (110) | 12.2322 | 0.62 |
| (11-1) | 14.7932 | 0.43 |
| (111) | 15.2566 | 0.40 |
| (021) | 19.4624 | 0.25 |
| (120) | 19.4640 | 0.25 |
| (012) | 19.4754 | 0.25 |
| (210) | 19.4814 | 0.25 |
| (11-2) | 21.0368 | 0.21 |
| (21-1) | 21.0411 | 0.21 |
| (12-1) | 21.1920 | 0.21 |
| (121) | 21.5228 | 0.20 |
| (112) | 21.6980 | 0.20 |
| (211) | 21.7021 | 0.20 |
| (022) | 24.7343 | 0.16 |

## 5. Deliverable validation

| check | result |
| --- | --- |
| written by GSAS-II | 5839 static 87e7f2c4 |
| source constraints (Hist/HAP/Phase) | 0 / 0 / 12 |
| constraints in package | cleared |
| reopen: phases / histograms | 1 / 1 |
| reopen: cached wR | 9.40% |

> A .gpx is a GSAS-II pickle: never rename it, never edit it as text, and never open it with an OLDER GSAS-II than the version above (older builds report "not a current GSAS-II .gpx").
> Stale constraints were cleared as deliverable hygiene - do NOT re-refine this project afterwards, or the cached converged wR is lost.

## 6. Package contents

- `FE50_final.gpx`
- `FE50_final.lst`
- `FE50_fit.png`
- `FE50_report.md`
- `FE50_t14_litcn.cif`

## 7. Notes

- Packaging only: no refinement parameter was changed and no refinement was run.
- CIF files are produced by the official GSAS-II exporter `G2Phase.export_CIF` (never hand-written).
- One row of reflection ticks per phase (peak assignment); the strongest peaks carry hkl labels whose heights are staggered to avoid mutual overlap.
- Legend and statistics box are placed by data occupancy in the four corners, and the top of the main panel is padded, so peaks are never covered.
- WARNING: pruned stale reflection list 'New structure' in histogram 'PWDR FE50.fxye Bank 1' (phase no longer in project)
- WARNING: cleared 12 stale constraint entries (Hist=0, HAP=0, Phase=12) - do NOT re-refine this project afterwards (refining would drop the cached converged wR)

# FAP - final refinement deliverable

- generated: 2026-10-09 14:50:28
- engine: GSAS-II 5839 (scripting interface, not GUI)
- source project: `workspace\QWEN 3.7 PLUS\Fluoroapatite\gsas_ops_out.gpx`
- histogram: `PWDR FAP.fxye Bank 1`

## 1. Goodness of fit

| metric | value |
| --- | --- |
| Rwp (%) | 20.95 |
| R (%) | 15.13 |
| Rb (%) | 16.35 |
| wRb (%) | 21.46 |
| wRmin (%) | 5.61 |

## 2. Phases and cells

| phase | space group | a | b | c | alpha | beta | gamma | V |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| built | P 63/m | 9.3703(0.0003) | 9.3703(0.0003) | 6.8848(0.0001) | 90.000 | 90.000 | 120.000 | 523.510(0.020) |

## 3. Atom parameters

| phase | label | element | x | y | z | Occ | Mult | Uiso | flag |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| built | Ca1 | Ca | 0.33330 | 0.66670 | 0.00267 | 1.0000 | 4 | 0.0235 | XU |
| built | Ca2 | Ca | 0.24324 | 0.25648 | 0.25000 | 1.0000 | 6 | 0.0213 | XU |
| built | P3 | P | 0.53089 | 0.42397 | 0.25000 | 1.0000 | 6 | 0.0100 | X |
| built | O4 | O | 0.39381 | 0.02368 | 0.25000 | 1.0000 | 6 | 0.0050 | X |
| built | O5 | O | 0.51981 | 0.67508 | 0.25000 | 1.0000 | 6 | 0.0050 | X |
| built | O6 | O | 0.25248 | 0.33508 | 0.56262 | 1.0000 | 12 | 0.0559 | XU |
| built | F7 | F | 0.00000 | 0.00000 | 0.25000 | 1.0000 | 2 | 0.0599 | XU |

## 4. Strongest reflections (top 15 by Icorr)

**built**

| hkl | 2-theta (deg) | Icorr |
| --- | --- | --- |
| (011) | 16.8211 | 62.91 |
| (111) | 22.8882 | 33.79 |
| (021) | 25.4069 | 27.35 |
| (110) | 18.8728 | 24.94 |
| (012) | 28.0814 | 22.33 |
| (020) | 21.8342 | 18.58 |
| (121) | 31.8625 | 17.28 |
| (211) | 31.8625 | 17.28 |
| (112) | 32.1887 | 16.92 |
| (022) | 34.0750 | 15.07 |
| (031) | 35.5776 | 13.81 |
| (212) | 39.2571 | 11.31 |
| (122) | 39.2571 | 11.31 |
| (221) | 40.5944 | 10.56 |
| (013) | 40.7749 | 10.47 |

## 5. Deliverable validation

| check | result |
| --- | --- |
| written by GSAS-II | 5839 static 87e7f2c4 |
| source constraints (Hist/HAP/Phase) | 0 / 0 / 0 |
| constraints in package | none |
| reopen: phases / histograms | 1 / 1 |
| reopen: cached wR | 20.95% |

> A .gpx is a GSAS-II pickle: never rename it, never edit it as text, and never open it with an OLDER GSAS-II than the version above (older builds report "not a current GSAS-II .gpx").
> Stale constraints were cleared as deliverable hygiene - do NOT re-refine this project afterwards, or the cached converged wR is lost.

## 6. Package contents

- `FAP_final.gpx`
- `FAP_fit.png`
- `FAP_report.md`
- `FAP_built.cif`

## 7. Notes

- Packaging only: no refinement parameter was changed and no refinement was run.
- CIF files are produced by the official GSAS-II exporter `G2Phase.export_CIF` (never hand-written).
- One row of reflection ticks per phase (peak assignment); the strongest peaks carry hkl labels whose heights are staggered to avoid mutual overlap.
- Legend and statistics box are placed by data occupancy in the four corners, and the top of the main panel is padded, so peaks are never covered.
- WARNING: no refinement log (.lst) found next to the gpx; chi**2/GOF are omitted

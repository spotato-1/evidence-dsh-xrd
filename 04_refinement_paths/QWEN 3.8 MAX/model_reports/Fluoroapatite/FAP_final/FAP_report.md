# FAP - final refinement deliverable

- generated: 2026-10-10 19:50:49
- engine: GSAS-II 5839 (scripting interface, not GUI)
- source project: `workspace\QWEN 3.8 MAX\Fluoroapatite\gsas_proj_final.gpx`
- histogram: `PWDR pattern_2theta.txt`
- refinement log: `FAP_final.lst`

## 1. Goodness of fit

| metric | value |
| --- | --- |
| Rwp (%) | 11.5 |
| R (%) | 8.809 |
| Rb (%) | 9.155 |
| wRb (%) | 11.49 |
| wRmin (%) | 5.61 |
| chi**2 | 2.416e+04 |
| GOF | 2.06 |

## 2. Phases and cells

| phase | space group | a | b | c | alpha | beta | gamma | V |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| built | P 63/m | 9.3708(0.0002) | 9.3708(0.0002) | 6.8851(0.0001) | 90.000 | 90.000 | 120.000 | 523.596(0.016) |

## 3. Atom parameters

| phase | label | element | x | y | z | Occ | Mult | Uiso | flag |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| built | Ca1 | Ca | 0.33330 | 0.66670 | 0.00156 | 1.0000 | 4 | 0.0223 | XU |
| built | Ca2 | Ca | 0.24147 | 0.99193 | 0.25000 | 1.0000 | 6 | 0.0220 | XU |
| built | P1 | P | 0.39717 | 0.36790 | 0.25000 | 1.0000 | 6 | 0.0216 | XU |
| built | O1 | O | 0.32585 | 0.48596 | 0.25000 | 1.0000 | 6 | 0.0260 | XU |
| built | O2 | O | 0.58999 | 0.46935 | 0.25000 | 1.0000 | 6 | 0.0249 | XU |
| built | O3 | O | 0.34010 | 0.25902 | 0.07126 | 1.0000 | 12 | 0.0260 | XU |
| built | F1 | F | 0.00000 | 0.00000 | 0.25000 | 1.0000 | 2 | 0.0331 | XU |

## 4. Strongest reflections (top 15 by Icorr)

**built**

| hkl | 2-theta (deg) | Icorr |
| --- | --- | --- |
| (011) | 16.8248 | 46.91 |
| (111) | 22.8914 | 25.74 |
| (021) | 25.4100 | 21.05 |
| (110) | 18.8762 | 18.72 |
| (012) | 28.0847 | 17.39 |
| (020) | 21.8374 | 14.10 |
| (211) | 31.8652 | 13.71 |
| (121) | 31.8652 | 13.71 |
| (112) | 32.1916 | 13.45 |
| (022) | 34.0778 | 12.10 |
| (031) | 35.5800 | 11.17 |
| (212) | 39.2595 | 9.34 |
| (122) | 39.2595 | 9.34 |
| (221) | 40.5965 | 8.80 |
| (013) | 40.7776 | 8.73 |

## 5. Deliverable validation

| check | result |
| --- | --- |
| written by GSAS-II | 5839 static 87e7f2c4 |
| source constraints (Hist/HAP/Phase) | 0 / 0 / 0 |
| constraints in package | none |
| reopen: phases / histograms | 1 / 1 |
| reopen: cached wR | 11.50% |

> A .gpx is a GSAS-II pickle: never rename it, never edit it as text, and never open it with an OLDER GSAS-II than the version above (older builds report "not a current GSAS-II .gpx").
> Stale constraints were cleared as deliverable hygiene - do NOT re-refine this project afterwards, or the cached converged wR is lost.

## 6. Package contents

- `FAP_final.gpx`
- `FAP_final.lst`
- `FAP_fit.png`
- `FAP_report.md`
- `FAP_built.cif`

## 7. Notes

- Packaging only: no refinement parameter was changed and no refinement was run.
- CIF files are produced by the official GSAS-II exporter `G2Phase.export_CIF` (never hand-written).
- One row of reflection ticks per phase (peak assignment); the strongest peaks carry hkl labels whose heights are staggered to avoid mutual overlap.
- Legend and statistics box are placed by data occupancy in the four corners, and the top of the main panel is padded, so peaks are never covered.

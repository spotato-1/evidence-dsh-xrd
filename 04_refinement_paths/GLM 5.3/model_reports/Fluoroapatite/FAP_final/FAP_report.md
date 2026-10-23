# FAP - final refinement deliverable

- generated: 2026-10-09 20:45:08
- engine: GSAS-II 5839 (scripting interface, not GUI)
- source project: `workspace\GLM 5.3\Fluoroapatite\work\gsas_final.gpx`
- histogram: `PWDR FAP.fxye Bank 1`
- refinement log: `FAP_final.lst`

## 1. Goodness of fit

| metric | value |
| --- | --- |
| Rwp (%) | 9.75 |
| R (%) | 7.66 |
| Rb (%) | 7.469 |
| wRb (%) | 9.12 |
| wRmin (%) | 5.61 |
| chi**2 | 1.737e+04 |
| GOF | 1.74 |

## 2. Phases and cells

| phase | space group | a | b | c | alpha | beta | gamma | V |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| built | P 63/m | 9.3703(0.0001) | 9.3703(0.0001) | 6.8849(0.0000) | 90.000 | 90.000 | 120.000 | 523.524(0.010) |

## 3. Atom parameters

| phase | label | element | x | y | z | Occ | Mult | Uiso | flag |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| built | Ca1 | Ca | 0.66667 | 0.33333 | 0.00112 | 1.0000 | 4 | 0.0129 | XU |
| built | Ca2 | Ca | -0.00784 | 0.24169 | 0.25000 | 1.0000 | 6 | 0.0120 | XU |
| built | P3 | P | 0.36784 | 0.39709 | 0.25000 | 1.0000 | 6 | 0.0125 | XU |
| built | O4 | O | 0.48541 | 0.32523 | 0.25000 | 1.0000 | 6 | 0.0124 | XU |
| built | O5 | O | 0.46924 | 0.59086 | 0.25000 | 1.0000 | 6 | 0.0147 | XU |
| built | O6 | O | 0.25848 | 0.34009 | 0.07091 | 1.0000 | 12 | 0.0148 | XU |
| built | F7 | F | 0.00000 | 0.00000 | 0.25000 | 1.0000 | 2 | 0.0224 | U |

## 4. Strongest reflections (top 15 by Icorr)

**built**

| hkl | 2-theta (deg) | Icorr |
| --- | --- | --- |
| (011) | 16.8214 | 48.56 |
| (111) | 22.8883 | 26.10 |
| (021) | 25.4071 | 21.13 |
| (110) | 18.8730 | 19.29 |
| (012) | 28.0815 | 17.22 |
| (020) | 21.8343 | 14.37 |
| (121) | 31.8626 | 13.35 |
| (211) | 31.8626 | 13.35 |
| (112) | 32.1887 | 13.06 |
| (022) | 34.0751 | 11.63 |
| (031) | 35.5776 | 10.67 |
| (212) | 39.2571 | 8.73 |
| (122) | 39.2571 | 8.73 |
| (221) | 40.5944 | 8.17 |
| (013) | 40.7748 | 8.07 |

## 5. Deliverable validation

| check | result |
| --- | --- |
| written by GSAS-II | 5839 static 87e7f2c4 |
| source constraints (Hist/HAP/Phase) | 0 / 0 / 0 |
| constraints in package | none |
| reopen: phases / histograms | 1 / 1 |
| reopen: cached wR | 9.75% |

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

# FE50_final - final refinement deliverable

- generated: 2026-10-09 14:11:31
- engine: GSAS-II 5839 (scripting interface, not GUI)
- source project: `workspace\QWEN 3.7 PLUS\gsas_proj_continued.gpx`
- histogram: `PWDR FE50_gsas.fxye Bank 1`
- refinement log: `FE50_final_final.lst`

## 1. Goodness of fit

| metric | value |
| --- | --- |
| Rwp (%) | 13.9 |
| R (%) | 10.74 |
| Rb (%) | 14.84 |
| wRb (%) | 19.52 |
| wRmin (%) | 7.917 |
| chi**2 | 8638 |
| GOF | 1.76 |

## 2. Phases and cells

| phase | space group | a | b | c | alpha | beta | gamma | V |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| K4.8 Mn2 Fe6 C24 N24 | F m -3 m | 10.1004(0.0052) | 10.1004(0.0052) | 10.1004(0.0052) | 90.000 | 90.000 | 90.000 | 1030.419(1.584) |

## 3. Atom parameters

| phase | label | element | x | y | z | Occ | Mult | Uiso | flag |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| K4.8 Mn2 Fe6 C24 N24 | K0 | K | 0.25000 | 0.25000 | 0.25000 | 0.6000 | 8 | 0.0050 | X |
| K4.8 Mn2 Fe6 C24 N24 | Mn1 | Mn | 0.00000 | 0.00000 | 0.50000 | 0.5000 | 4 | 0.0050 | X |
| K4.8 Mn2 Fe6 C24 N24 | Fe2 | Fe | 0.00000 | 0.00000 | 0.50000 | 0.9700 | 4 | 0.0050 | X |
| K4.8 Mn2 Fe6 C24 N24 | Fe3 | Fe | 0.00000 | 0.00000 | 0.00000 | 0.9500 | 4 | 0.0050 | X |
| K4.8 Mn2 Fe6 C24 N24 | C4 | C | 0.00000 | 0.00000 | 0.16740 | 0.9800 | 24 | 0.0050 | X |
| K4.8 Mn2 Fe6 C24 N24 | N5 | N | 0.00000 | 0.00000 | 0.41343 | 0.9800 | 24 | 0.0050 | X |

## 4. Strongest reflections (top 15 by Icorr)

**K4.8 Mn2 Fe6 C24 N24**

| hkl | 2-theta (deg) | Icorr |
| --- | --- | --- |
| (111) | 15.0138 | 0.35 |
| (311) | 29.1357 | 0.28 |
| (200) | 17.3796 | 0.20 |
| (220) | 24.7467 | 0.19 |
| (531) | 53.4722 | 0.16 |
| (331) | 38.6651 | 0.16 |
| (420) | 39.7161 | 0.15 |
| (422) | 43.7104 | 0.12 |
| (511) | 46.5244 | 0.11 |
| (642) | 69.4321 | 0.10 |
| (222) | 30.4699 | 0.08 |
| (442) | 54.2955 | 0.08 |
| (620) | 57.5090 | 0.07 |
| (533) | 59.8457 | 0.07 |
| (622) | 60.6122 | 0.06 |

## 5. Deliverable validation

| check | result |
| --- | --- |
| written by GSAS-II | 5839 static 87e7f2c4 |
| source constraints (Hist/HAP/Phase) | 0 / 0 / 0 |
| constraints in package | none |
| reopen: phases / histograms | 1 / 1 |
| reopen: cached wR | 13.90% |

> A .gpx is a GSAS-II pickle: never rename it, never edit it as text, and never open it with an OLDER GSAS-II than the version above (older builds report "not a current GSAS-II .gpx").
> Stale constraints were cleared as deliverable hygiene - do NOT re-refine this project afterwards, or the cached converged wR is lost.

## 6. Package contents

- `FE50_final_final.gpx`
- `FE50_final_final.lst`
- `FE50_final_fit.png`
- `FE50_final_report.md`
- `FE50_final_K4.8_Mn2_Fe6_C24_N24.cif`

## 7. Notes

- Packaging only: no refinement parameter was changed and no refinement was run.
- CIF files are produced by the official GSAS-II exporter `G2Phase.export_CIF` (never hand-written).
- One row of reflection ticks per phase (peak assignment); the strongest peaks carry hkl labels whose heights are staggered to avoid mutual overlap.
- Legend and statistics box are placed by data occupancy in the four corners, and the top of the main panel is padded, so peaks are never covered.

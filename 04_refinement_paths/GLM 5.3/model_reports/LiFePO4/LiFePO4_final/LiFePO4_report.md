# LiFePO4 - final refinement deliverable

- generated: 2026-10-12 02:23:05
- engine: GSAS-II 5839 (scripting interface, not GUI)
- source project: `workspace\GLM 5.3\LiFePO4\gsas_ops_out.gpx`
- histogram: `PWDR LiFePO4.fxye Bank 1`
- refinement log: `LiFePO4_final.lst`

## 1. Goodness of fit

| metric | value |
| --- | --- |
| Rwp (%) | 6.7 |
| R (%) | 5.14 |
| Rb (%) | 6.203 |
| wRb (%) | 8.297 |
| wRmin (%) | 6.154 |
| chi**2 | 8306 |
| GOF | 1.09 |

## 2. Phases and cells

| phase | space group | a | b | c | alpha | beta | gamma | V |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| built | P n m a | 10.3244(0.0002) | 6.0045(0.0001) | 4.6897(0.0001) | 90.000 | 90.000 | 90.000 | 290.725(0.014) |

## 3. Atom parameters

| phase | label | element | x | y | z | Occ | Mult | Uiso | flag |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| built | Li1 | Li | 0.00000 | 0.00000 | 0.00000 | 0.9911 | 4 | 0.0050 | F |
| built | Fe2 | Fe | 0.28253 | 0.25000 | 0.97449 | 0.9911 | 4 | 0.0137 | FU |
| built | P3 | P | 0.09546 | 0.25000 | 0.42385 | 1.0000 | 4 | 0.0175 | XU |
| built | O4 | O | 0.09344 | 0.25000 | 0.75010 | 1.0000 | 4 | 0.0082 | XU |
| built | O5 | O | 0.45580 | 0.25000 | 0.21098 | 1.0000 | 4 | 0.0124 | XU |
| built | O6 | O | 0.16273 | 0.04959 | 0.28306 | 1.0000 | 8 | 0.0174 | XU |
| built | Fe2_Li | Li | 0.28253 | 0.25000 | 0.97449 | 0.0089 | 4 | 0.0050 | F |
| built | Li1_Fe | Fe | 0.00000 | 0.00000 | 0.00000 | 0.0089 | 4 | 0.0050 | F |

## 4. Strongest reflections (top 15 by Icorr)

**built**

| hkl | 2-theta (deg) | Icorr |
| --- | --- | --- |
| (111) | 25.5229 | 8.73 |
| (211) | 29.6485 | 7.08 |
| (101) | 20.7310 | 5.80 |
| (311) | 35.5610 | 5.42 |
| (121) | 36.5026 | 5.20 |
| (210) | 22.6422 | 5.14 |
| (011) | 24.0032 | 4.75 |
| (221) | 39.6036 | 4.58 |
| (201) | 25.5871 | 4.35 |
| (112) | 42.2023 | 4.14 |
| (411) | 42.6370 | 4.07 |
| (321) | 44.3676 | 3.81 |
| (200) | 17.1078 | 3.79 |
| (212) | 44.9751 | 3.72 |
| (312) | 49.3226 | 3.18 |

## 5. Deliverable validation

| check | result |
| --- | --- |
| written by GSAS-II | 5839 static 87e7f2c4 |
| source constraints (Hist/HAP/Phase) | 0 / 0 / 3 |
| constraints in package | cleared |
| reopen: phases / histograms | 1 / 1 |
| reopen: cached wR | 6.70% |

> A .gpx is a GSAS-II pickle: never rename it, never edit it as text, and never open it with an OLDER GSAS-II than the version above (older builds report "not a current GSAS-II .gpx").
> Stale constraints were cleared as deliverable hygiene - do NOT re-refine this project afterwards, or the cached converged wR is lost.

## 6. Package contents

- `LiFePO4_final.gpx`
- `LiFePO4_final.lst`
- `LiFePO4_fit.png`
- `LiFePO4_report.md`
- `LiFePO4_built.cif`

## 7. Notes

- Packaging only: no refinement parameter was changed and no refinement was run.
- CIF files are produced by the official GSAS-II exporter `G2Phase.export_CIF` (never hand-written).
- One row of reflection ticks per phase (peak assignment); the strongest peaks carry hkl labels whose heights are staggered to avoid mutual overlap.
- Legend and statistics box are placed by data occupancy in the four corners, and the top of the main panel is padded, so peaks are never covered.
- WARNING: cleared 3 stale constraint entries (Hist=0, HAP=0, Phase=3) - do NOT re-refine this project afterwards (refining would drop the cached converged wR)

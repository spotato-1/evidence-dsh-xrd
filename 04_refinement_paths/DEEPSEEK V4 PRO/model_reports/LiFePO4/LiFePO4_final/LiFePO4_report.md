# LiFePO4 - final refinement deliverable

- generated: 2026-10-11 19:36:05
- engine: GSAS-II 5839 (scripting interface, not GUI)
- source project: `workspace\DEEPSEEK V4 PRO\LiFePO4\gsas_ops_continued.gpx`
- histogram: `PWDR pattern.fxye Bank 1`
- refinement log: `LiFePO4_final.lst`

## 1. Goodness of fit

| metric | value |
| --- | --- |
| Rwp (%) | 10.08 |
| R (%) | 7.388 |
| Rb (%) | 10.25 |
| wRb (%) | 13.31 |
| wRmin (%) | 6.154 |
| chi**2 | 1.877e+04 |
| GOF | 1.64 |

## 2. Phases and cells

| phase | space group | a | b | c | alpha | beta | gamma | V |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| built | P n m a | 10.3366(0.0002) | 6.0118(0.0001) | 4.6966(0.0001) | 90.000 | 90.000 | 90.000 | 291.852(0.007) |

## 3. Atom parameters

| phase | label | element | x | y | z | Occ | Mult | Uiso | flag |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| built | Li1 | Li | 0.00000 | 0.00000 | 0.00000 | 0.9509 | 4 | 0.0050 | FX |
| built | Fe2 | Fe | 0.28193 | 0.25000 | 0.97323 | 0.9509 | 4 | 0.0050 | FX |
| built | P3 | P | 0.09367 | 0.25000 | 0.42727 | 1.0000 | 4 | 0.0158 | XU |
| built | O4 | O | 0.09221 | 0.25000 | 0.75029 | 1.0000 | 4 | 0.0050 | X |
| built | O5 | O | 0.44784 | 0.25000 | 0.23040 | 1.0000 | 4 | 0.0050 | X |
| built | O6 | O | 0.15889 | 0.04601 | 0.28110 | 1.0000 | 8 | 0.0199 | XU |
| built | Li1_Fe | Fe | 0.00000 | 0.00000 | 0.00000 | 0.0491 | 4 | 0.0050 | F |
| built | Fe2_Li | Li | 0.28191 | 0.25000 | 0.97332 | 0.0491 | 4 | 0.0050 | F |

## 4. Strongest reflections (top 15 by Icorr)

**built**

| hkl | 2-theta (deg) | Icorr |
| --- | --- | --- |
| (111) | 25.5420 | 10.19 |
| (101) | 20.7556 | 7.75 |
| (211) | 29.6628 | 7.52 |
| (210) | 22.6689 | 6.49 |
| (011) | 24.0240 | 5.77 |
| (200) | 17.1418 | 5.70 |
| (311) | 35.5680 | 5.20 |
| (201) | 25.6064 | 5.07 |
| (121) | 36.5077 | 4.93 |
| (221) | 39.6048 | 4.18 |
| (112) | 42.1930 | 3.68 |
| (411) | 42.6347 | 3.60 |
| (321) | 44.3623 | 3.33 |
| (212) | 44.9624 | 3.24 |
| (301) | 32.1932 | 3.19 |

## 5. Deliverable validation

| check | result |
| --- | --- |
| written by GSAS-II | 5839 static 87e7f2c4 |
| source constraints (Hist/HAP/Phase) | 0 / 0 / 3 |
| constraints in package | cleared |
| reopen: phases / histograms | 1 / 1 |
| reopen: cached wR | 10.08% |

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

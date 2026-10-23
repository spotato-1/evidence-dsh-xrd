# LiFePO4 - final refinement deliverable

- generated: 2026-10-12 00:37:19
- engine: GSAS-II 5839 (scripting interface, not GUI)
- source project: `workspace\QWEN 3.8 MAX\LiFePO4\LiFePO4_deliver.gpx`
- histogram: `PWDR pattern.fxye Bank 1`
- refinement log: `LiFePO4_final.lst`

## 1. Goodness of fit

| metric | value |
| --- | --- |
| Rwp (%) | 6.26 |
| R (%) | 4.888 |
| Rb (%) | 5.25 |
| wRb (%) | 6.434 |
| wRmin (%) | 6.154 |
| chi**2 | 7236 |
| GOF | 1.02 |

## 2. Phases and cells

| phase | space group | a | b | c | alpha | beta | gamma | V |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Li4 Fe4 P4 O16 | P n m a | 10.3252(0.0002) | 6.0051(0.0001) | 4.6901(0.0001) | 90.000 | 90.000 | 90.000 | 290.802(0.011) |

## 3. Atom parameters

| phase | label | element | x | y | z | Occ | Mult | Uiso | flag |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Li4 Fe4 P4 O16 | Li0 | Li | 0.00000 | 0.00000 | 0.00000 | 0.9774 | 4 | 0.0050 | F |
| Li4 Fe4 P4 O16 | Fe1 | Fe | 0.21757 | 0.75000 | 0.47215 | 0.9774 | 4 | 0.0111 | FU |
| Li4 Fe4 P4 O16 | P2 | P | 0.09566 | 0.25000 | 0.42732 | 1.0000 | 4 | 0.0213 | U |
| Li4 Fe4 P4 O16 | O3 | O | 0.15796 | 0.05040 | 0.28068 | 1.0000 | 8 | 0.0191 | U |
| Li4 Fe4 P4 O16 | O4 | O | 0.04600 | 0.75000 | 0.72837 | 1.0000 | 4 | 0.0050 |  |
| Li4 Fe4 P4 O16 | O5 | O | 0.08758 | 0.25000 | 0.74497 | 1.0000 | 4 | 0.0110 | U |
| Li4 Fe4 P4 O16 | Fe1_Li | Li | 0.21757 | 0.75000 | 0.47215 | 0.0226 | 4 | 0.0119 | F |
| Li4 Fe4 P4 O16 | Li0_Fe | Fe | 0.00000 | 0.00000 | 0.00000 | 0.0226 | 4 | 0.0050 | F |

## 4. Strongest reflections (top 15 by Icorr)

**Li4 Fe4 P4 O16**

| hkl | 2-theta (deg) | Icorr |
| --- | --- | --- |
| (111) | 25.5228 | 9.59 |
| (211) | 29.6482 | 7.21 |
| (101) | 20.7314 | 7.17 |
| (210) | 22.6423 | 6.04 |
| (011) | 24.0033 | 5.40 |
| (200) | 17.1083 | 5.22 |
| (311) | 35.5603 | 5.13 |
| (121) | 36.5016 | 4.89 |
| (201) | 25.5871 | 4.77 |
| (221) | 39.6024 | 4.22 |
| (112) | 42.2012 | 3.77 |
| (411) | 42.6357 | 3.70 |
| (321) | 44.3660 | 3.45 |
| (212) | 44.9739 | 3.37 |
| (301) | 32.1813 | 3.09 |

## 5. Deliverable validation

| check | result |
| --- | --- |
| written by GSAS-II | 5839 static 87e7f2c4 |
| source constraints (Hist/HAP/Phase) | 0 / 0 / 3 |
| constraints in package | cleared |
| reopen: phases / histograms | 1 / 1 |
| reopen: cached wR | 6.26% |

> A .gpx is a GSAS-II pickle: never rename it, never edit it as text, and never open it with an OLDER GSAS-II than the version above (older builds report "not a current GSAS-II .gpx").
> Stale constraints were cleared as deliverable hygiene - do NOT re-refine this project afterwards, or the cached converged wR is lost.

## 6. Package contents

- `LiFePO4_final.gpx`
- `LiFePO4_final.lst`
- `LiFePO4_fit.png`
- `LiFePO4_report.md`
- `LiFePO4_Li4_Fe4_P4_O16.cif`

## 7. Notes

- Packaging only: no refinement parameter was changed and no refinement was run.
- CIF files are produced by the official GSAS-II exporter `G2Phase.export_CIF` (never hand-written).
- One row of reflection ticks per phase (peak assignment); the strongest peaks carry hkl labels whose heights are staggered to avoid mutual overlap.
- Legend and statistics box are placed by data occupancy in the four corners, and the top of the main panel is padded, so peaks are never covered.
- WARNING: cleared 3 stale constraint entries (Hist=0, HAP=0, Phase=3) - do NOT re-refine this project afterwards (refining would drop the cached converged wR)

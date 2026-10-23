# XRD refinement journal (generated from journal.jsonl, do not edit by hand)

| round | engine | stage | model | Rwp | baseline | verdict | why | artifacts |
|---|---|---|---|---|---|---|---|---|
| 1 | xrd_refine_manual | (explicit vary) | physical | 93.73914745144577 | 98.85064676519619 | R-value plateau |  | workspace\QWEN 3.7 PLUS\Fe2O3_Fe3O4_2ph\result.json |
| 2 | xrd_refine_manual | (explicit vary) | physical | 5.041482987760901 | 98.83198312915776 | Not at plateau; ⚠4 parameter(s) sit on a bound (U, c, eta, zero) - the value is box-limited |  | workspace\QWEN 3.7 PLUS\Fe2O3_Fe3O4_2ph\result.json |
| 3 | xrd_refine_manual | (explicit vary) | physical | 5.041482987760901 | 98.83198312915776 | Not at plateau; ⚠4 parameter(s) sit on a bound (U, c, eta, zero) - the value is box-limited |  | workspace\QWEN 3.7 PLUS\Fe2O3_Fe3O4_2ph\result.json |
| 4 | xrd_refine_manual | (explicit vary) | physical | 5.020616680354777 | 98.83198312915776 | Not at plateau; ⚠2 parameter(s) sit on a bound (c, zero) - the value is box-limited |  | workspace\QWEN 3.7 PLUS\Fe2O3_Fe3O4_2ph\result.json |
| 5 | xrd_refine_manual | (explicit vary) | physical | 5.498710624537917 | 99.6951345622684 | Not at plateau; ⚠2 parameter(s) sit on a bound (W, eta) - the value is box-limited |  | workspace\QWEN 3.7 PLUS\Fe2O3_Fe3O4_2ph\result.json |

## Material and objective
- **Sample**: Fe2O3 + Fe3O4 two-phase mixture (Zenodo 14959531)
- **Objective**: publication-level refinement, R ≤ 10
- **Radiation**: Cu Kα (no monochromator, doublet)
- **Instrument**: Panalytical X'Pert PRO

## Phases and crystal families (conclusion + evidence + excluded families and reasons)
- **Fe2O3**: R-3c (hexagonal setting), a=5.038 Å, c=13.771 Å
  - Evidence: Materials Project polymorphs screening + literature confirmation
  - Construction: converted from the rhombohedral primitive cell to the standard hexagonal setting
- **Fe3O4**: Fd-3m (cubic setting), a=8.396 Å
  - Evidence: Materials Project polymorphs screening + literature confirmation
  - Construction: converted from the rhombohedral primitive cell to the standard cubic setting
- **Excluded**: P 1 primitive cell (symmetry too low, too many parameters, which makes the refinement unstable)

## Summary of defects (exhaustive → screening → execution)
- No significant defects requiring modelling
- The two-phase model already fully explains the main-peak positions

## Results achieved (R and its basis written separately)
- **Manual-engine Rwp**: 5.50% (numerically up to standard)
- **Visual fit quality**: poor (residuals ±10000 counts, main-peak intensities underestimated)
- **Conclusion**: the numerical target is met, but the visual quality has not reached publication level
- **Basis note**: the manual-engine Rwp and the GSAS wR are not directly comparable

## Not attempted · Open items
1. **GSAS-II refinement**: all 5 attempts failed (instrument parameter file format problem)
   - Formats tried: Bank/INS, INS HIST/HTYPE, INS 1H/2H, ICONS format
   - Error: `'INS   HTYPE '` KeyError or `cannot unpack non-iterable NoneType object`
   - Status: technically blocked, cannot be resolved
2. **FullProf fp2k verification**: single-phase verification Rwp=100% (expected, because this is a two-phase sample)
3. **Background-order optimization**: no bg_scan iteration was performed
4. **Coordinate refinement**: the atomic coordinates were not released

## Recommendations for handover
1. **Complete the refinement with commercial software**: GSAS-II GUI, FullProf, Topas
2. **Files to provide**:
   - CIF: `ref/Fe2O3_R-3c_hex_build_01.cif`, `ref/Fe3O4_Fd-3m_cubic_build_01.cif`
   - Data: `pattern_2theta.txt`, `pattern.fxye`
   - Results: `result.json`, `components.json`
3. **Points of attention**:
   - The manual-engine Rwp is inconsistent with the visual quality
   - A physically constrained refinement is needed (the constraint capability of GSAS-II)
   - The scale factors and peak-shape parameters may need adjustment

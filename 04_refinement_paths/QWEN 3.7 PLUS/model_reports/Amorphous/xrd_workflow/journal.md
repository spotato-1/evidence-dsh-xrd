# XRD refinement journal (generated from journal.jsonl, do not edit by hand)

| round | engine | stage | model | Rwp | baseline | verdict | why | artifacts |
|---|---|---|---|---|---|---|---|---|
| 1 | xrd_refine_manual | (explicit vary) | physical | 7.908078712772669 | 97.63155407731037 | Not at plateau; ⚠1 parameter(s) sit on a bound (ex0_c) - the value is box-limited |  | workspace\QWEN 3.7 PLUS\Amorphous\result.json |
| 2 | xrd_refine_manual | (explicit vary) | physical | 6.626177989715128 | 96.52440088375988 | Not at plateau; ⚠2 parameter(s) sit on a bound (ex0_c, ex1_c) - the value is box-limited |  | workspace\QWEN 3.7 PLUS\Amorphous\result.json |
| 3 | xrd_refine_manual | (explicit vary) | physical | 8.675609038617127 | 94.88529315783082 | R-value plateau |  | workspace\QWEN 3.7 PLUS\Amorphous\result.json |
| 4 | xrd_refine_manual | (explicit vary) | physical | 4.535711027809168 | 96.52440088375988 | Not at plateau; ⚠1 parameter(s) sit on a bound (scale) - the value is box-limited |  | workspace\QWEN 3.7 PLUS\Amorphous\result.json |
| 5 | xrd_refine_manual | (explicit vary) | physical | 6.778037189120267 | 95.13884870177684 | Not at plateau; ⚠1 parameter(s) sit on a bound (ex3_c) - the value is box-limited |  | workspace\QWEN 3.7 PLUS\Amorphous\result.json |
| 6 | xrd_refine_manual | (explicit vary) | physical | 9.269501128397934 | 96.44196820825961 | R-value plateau |  | workspace\QWEN 3.7 PLUS\Amorphous\result.json |
| 7 | xrd_refine_manual | (explicit vary) | physical | 7.7880060987277915 | 96.27345142217439 | Not at plateau; ⚠2 parameter(s) sit on a bound (ex1_c, scale) - the value is box-limited |  | workspace\QWEN 3.7 PLUS\Amorphous\result.json |
| 8 | xrd_refine_manual | (explicit vary) | physical | 4.535711027809168 | 96.52440088375988 | Not at plateau; ⚠1 parameter(s) sit on a bound (scale) - the value is box-limited |  | workspace\QWEN 3.7 PLUS\Amorphous\result.json |

## Material and objective

**Material**: g-C3N4 hollow microrod-derived carbon, sintered at 1100°C in Ar, three-layer carbon structure by TEM
**Objective**: Decompose the XRD signal of the three-layer carbon structure with empirical broad peaks, and characterize the degree of graphitization and the coherence length

## Phases and crystal families

**Conclusion**: The three empirical broad peaks correspond to three carbon structures of different density
- Peak 1 (17.1°, d=5.19Å): highly disordered carbon of the outer layer
- Peak 2 (24.5°, d=3.63Å): turbostratic carbon of the middle layer (graphite 002)
- Peak 3 (41.9°, d=2.14Å): in-plane graphitic carbon of the inner layer (graphite 100/101)

**Excluded**: crystalline impurity phases (no sharp diffraction peaks); residual g-C3N4 (fully carbonized at 1100°C)

## Summary of defects

This sample is a carbon material and does not involve conventional crystal defects. "Three layers of different density" is a structural feature rather than a defect.

## Results achieved

**Best Rwp**: 4.54% (manual-engine basis), Rexp=3.69%, χ²=1.51
**Scherrer size (apparent)**: inner layer La~4.4 nm, middle layer Lc~2.2 nm
**Background**: 20th-order Chebyshev (iteratively optimized, boundary effect at order 12→14)

## Not attempted · Open items

**Not attempted**:
1. Accurate refinement with GSAS-II (limited improvement for amorphous-dominated materials)
2. Cross-validation by Raman spectroscopy (D/G peak ratio)
3. Solid-state ¹³C NMR (sp²/sp³ ratio)

**Open**:
1. The physical assignment of peak 1 (17.1°) requires confirmation by other characterizations
2. The parameters of peak 1 and peak 2 have large uncertainties, and the decomposition is non-unique
3. Whether the proportions of carbon in each layer need to be quantified (requires standard samples)

## Recommendations for handover

1. The current results already satisfy the need for semi-quantitative characterization of the three-layer carbon structure
2. It is recommended to verify the degree of graphitization in combination with Raman
3. The parameters of peak 1 are unreliable; if an accurate decomposition is required, higher-resolution data or synchrotron radiation are needed
4. If publication-grade results are required, it is recommended to add HRTEM selected-area electron diffraction

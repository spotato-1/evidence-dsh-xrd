 Data checking, phase identification, FullProf/manual-engine pre-staging, final GSAS-II refinement, structure review and delivery have been completed in strict accordance with the dsh-xrd plugin five-stage workflow. All results are saved in the original data directory.

## Main conclusions

- **Main phase**: fluoroapatite `Ca5(PO4)3F`
- **Space group**: `P6₃/m`
- **Final model**: single-phase, ideal stoichiometric average structure
- **Distinguishable impurity phase**: no second phase supported by multiple independent reflections and reliably quantifiable was found  
  - the main residuals are concentrated at the positions of strong fluoroapatite reflections, which is more consistent with peak-shape/intensity residuals
  - trace impurities below the detection limit of routine powder XRD cannot be excluded

## Final GSAS-II results

| Metric | Result |
|---|---:|
| wR | **12.53%** |
| R | 10.12% |
| Rb | 10.92% |
| GOF | 2.24 |
| wRmin | 5.61% |
| a = b | 9.37046 Å |
| c | 6.88484 Å |
| V | 523.5354 Å³ |

Structural physical review results:

- GSAS parameter review: **pass**
- Final CIF sanity: **pass**
- occupancies all within the physical range
- all 7 independent atoms use isotropic ADP
- Uiso range approximately **0.01115–0.02031 Å²**
- no negative Uiso, and no thermal parameter below the set lower limit of 0.005 Å²
- typical bond lengths:
  - Ca–F: about 2.301 Å
  - Ca–O: about 2.346–2.507 Å
  - P–O: about 1.518–1.570 Å

## Peak width and size

The apparent coherence length of 5 representative main peaks is approximately **67–102 nm**.

This result:

- is not corrected for the measured instrumental broadening
- is an **apparent value**
- cannot be equated directly with the crystallite size in the strict sense
- was not subjected to size–microstrain separation

## Main delivered files

Complete delivery package:

- `workspace\GPT 5.6 SOL\Fluoroapatite\Fluoroapatite_final`

Including:

- Final report: `Fluoroapatite_final\Fluoroapatite_report.md`
- Fit figure: `Fluoroapatite_final\Fluoroapatite_fit.png`
- Final CIF: `Fluoroapatite_final\Fluoroapatite_Ca10_P6_O24_F2.cif`
- GSAS-II project that can be refined further: `Fluoroapatite_final\Fluoroapatite_final.gpx`
- GSAS-II log: `Fluoroapatite_final\Fluoroapatite_final.lst`
- File manifest: `Fluoroapatite_final\manifest.json`

Workflow records:

- `workflow_state.json`
- `phase_summary.json`
- `xrd_workflow\journal.jsonl`
- `xrd_workflow\journal.md`
- `gsas\review_judgment.md`

The final fit figure has been visually reviewed: the legend, statistics box, axes and main hkl labels are clear, there is no severe occlusion, and the main diffraction peaks are all explained by the model.

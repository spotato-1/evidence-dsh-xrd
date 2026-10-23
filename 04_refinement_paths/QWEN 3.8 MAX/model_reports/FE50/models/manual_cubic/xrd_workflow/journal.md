# XRD refinement journal (automatically generated from journal.jsonl, do not edit by hand)

| Round | Engine | Stage | Model | Rwp | Baseline R | Verdict | Why | Artifacts |
|---|---|---|---|---|---|---|---|---|
| 1 | xrd_refine_manual | (explicit vary) | physical | 13.009103247877462 | 97.83853012583086 | not yet at the plateau; ⚠the optimiser did not report convergence (Tolerance seems to be too small. Could not estimate error-bars.); stopped at max_nfev=8000 - Rwp is a snapshot, not a minimum; 3 parameter(s) sit on a bound (V, eta, ex0_c) - the value is box-limited |  | workspace\QWEN 3.8 MAX\FE50\models\manual_cubic\result.json |
| 2 | xrd_refine_manual | (explicit vary) | physical | 12.42202899453035 | 96.66406030428803 | not yet at the plateau; ⚠3 parameter(s) sit on a bound (V, eta, ex0_H) - the value is box-limited | numerical treatment of the round3 snapshot (hit max_nfev=8000, ex0_c at the 13.6 bound): raise max_nfev to 40000 and move the extras initial values near the round3 final values to eliminate the bound hitting | workspace\QWEN 3.8 MAX\FE50\models\manual_cubic\result.json |

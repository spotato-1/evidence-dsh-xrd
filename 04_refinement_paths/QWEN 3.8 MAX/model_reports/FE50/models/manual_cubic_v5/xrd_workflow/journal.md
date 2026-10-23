# XRD refinement journal (automatically generated from journal.jsonl, do not edit by hand)

| Round | Engine | Stage | Model | Rwp | Baseline R | Verdict | Why | Artifacts |
|---|---|---|---|---|---|---|---|---|
| 1 | xrd_refine_manual | (explicit vary) | physical | 12.273527683581893 | 12.422079177529005 | not yet at the plateau; ⚠the optimiser did not report convergence (Tolerance seems to be too small. Could not estimate error-bars.); stopped at max_nfev=20000 - Rwp is a snapshot, not a minimum; 4 parameter(s) sit on a bound (V, X, Y, eta) - the value is box-limited | v5: warm start from the true final values of v2 (12.422; v4 had mistakenly used the v1 parameters and fell into the worse minimum at 12.69); the X/Y Lorentzian terms are released, V≥-3/eta≤0.995/extrasH≤8; testing whether the size-broadening term improves things | result.json |

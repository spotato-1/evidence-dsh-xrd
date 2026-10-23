# XRD refinement journal (generated from journal.jsonl, do not edit by hand)

| round | engine | stage | model | Rwp | baseline | verdict | why | artifacts |
|---|---|---|---|---|---|---|---|---|
| 1 | xrd_refine_manual | structure | physics | 10.735148582939017 | 96.56788556268147 | not yet at the basin; ⚠4 parameter(s) sit on a bound (dw_C, dw_Fe, dw_Mn, occ_Mn1) - the value is box-limited | residual: broad halos at 28-30°/43-46°/12-16° (amorphous/nanodomains), (220) undercalculated (sensitive to K occupancy), eta at the upper bound (missing Lorentzian size term). This round: TCH peak shape + per-element B + K/Mn/Fe-N/C/N occupancies + 3 empirical broad peaks | workspace\GLM 5.3\FE50\work\M2_mono\r3\result.json |

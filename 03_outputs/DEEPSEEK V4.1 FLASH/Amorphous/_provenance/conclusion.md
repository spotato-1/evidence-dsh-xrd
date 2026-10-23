Processing is complete per the xrd plugin's five-stage workflow, and the results are delivered as follows.

## Core quantitative results

| Quantity | This sample | Graphite reference | Note |
|---|---|---|---|
| **d002** | **3.04 Å** (peak center 29.36°) | 3.354 Å | interlayer spacing **tighter** than graphite |
| **Lc** | **6.9 Å** (≈2.3 layers) | — | Scherrer K=0.9, apparent value |
| **d100 / in-plane a** | **2.154 Å / 2.487 Å** | 2.131 / 2.461 Å | slight in-plane expansion |
| **La (sp² clusters)** | **26.2 Å** | — | Warren K=1.84, apparent value |

Whole-pattern model: 4 pseudo-Voigt (η free) + 6th-order background, **Rwp = 3.499 %, χ²/dof = 1.037** (baseline 97.7 %).

## Three interpretation conclusions you need to know

1. **There is no crystalline graphite phase** — three independent pieces of evidence: in the manual engine the scale of the formal graphite phase was pinned at the lower bound, the whole pattern contains no sharp peak falling at graphite's 26.55/42.38/44.58°, and in a single fp2k baseline `SumYcal` is only 14 % of `SumYobs`.
2. **d002 is tighter than graphite, the opposite of the usual hard-carbon behavior**. For polymer-precursor hard carbon, (002) is usually at 22–24°, d ≈ 3.7–3.9 Å ([hard-carbon review](https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/cnl2.146), [Nature Comms PXRD](https://static-content.springer.com/esm/art%3A10.1038%2Fs41467-024-45460-3/MediaObjects/41467_2024_45460_MOESM2_ESM.pdf)). This sample goes the opposite way; taken together with the slightly expanded in-plane a, **we infer that it is related to the N doping introduced by the g-C₃N₄ precursor, but this is an inference, not corroborated by elemental analysis**.
3. **The model needs 4 components to be sufficient** (F test F = 254.6 significant; 5 components not significant), which is consistent with the **three layers of tube wall with different density** you saw in TEM — coexisting multiple spacings manifest as a multi-component superposition of the broad hump, not a single (002).

## Three things that must be stated honestly from the process

- **Engine capability boundary**: the manual engine's empirical broad-peak H cap is only 4.0° (source `xrd_engine.py:415`), whereas this sample's broad hump reaches FWHM 7–12°, which it **cannot express**. I confirmed this with one diagnostic control (after dropping the background to 2nd order, Rwp deteriorated to 32.28 % with 3 parameters at the bound), so the final quantification switched to whole-pattern modeling, and I cross-validated that two independent fits both point to d ≈ 3.0 Å. This is not a "fit failure", it is a clear tool boundary.
- **I did not use fp2k's 10.9 % as a conclusion**: the final `.out`/`.sum` carrying that value contains only the banner and cannot be reviewed, and for an amorphous sample the Rietveld Rwp has no discriminating meaning. I take it only as circumstantial evidence for "no crystalline graphite".
- **No GSAS-II refinement was done**: the amorphous bulk has no Bragg reflections, so cell/occupancy/Uiso have no observation to support them, and forcing a refinement amounts to fitting noise into structural parameters (false improvement). This was written into the coverage statement per the workflow rather than silently skipped. In addition, `xrd_data_io`'s `fwhm` action failed on this sample (reporting spurious peaks at 17.3°/50.1° and negative Caglioti coefficients), which is recorded as well.

**Two limitations**: no 2θ standard was available this time, so **the absolute d values carry an uncalibrated zero-position uncertainty**; the "peak" reported by the machine at 60.7° was verified to be statistical noise (counts in that region 410–486, σ≈19) and has been excluded.

## Outputs (all under `Amorphous`, 2.72 MB total, all retained as you requested)

- `W_XRD_report.md` — complete report (including the coverage statement and untried items)
- `work/W_final_fit.png` — final fit figure (obs/calc/4 components/background + residual panel)
- `work/hump_model.json`, `work/derived.json` — model parameters and derived quantities (machine-readable)
- `work/xrd_workflow/journal.jsonl`, `journal.md` — authoritative round-by-round log + quick overview
- `workflow_state.json` — state protocol
- `work/r1/`, `work/r2/`, `work/fp/` — engine products of the three rounds

**Suggested next experiments**: give priority to XPS/EA to confirm the N doping (this is the key to explaining 3.04 Å); add Raman to cross-validate La = 26.2 Å; if publication-level absolute d values are needed, also measure a Si or Al₂O₃ standard.

Full-process handling of the amorphous carbon anode XRD data has been completed (strictly following the dsh-xrd plugin workflow), and all products are saved under the data folder.

## Processing results

**Data pre-screening and λ reconciliation**
- Rigaku RAW, Cu Kα, 2θ = 10–80°, step 0.0204°, 3432 points.
- λ reconciled field by field from the RAW header: `Anode=Cu`, `Alpha1=1.5406`, `Alpha2=1.54439`, `AlphaRatio=0.5`, `Monochromator=0` → **Cu Kα doublet, and Kα2 was not stripped**; the doublet wavelengths are passed explicitly downstream, and the Scherrer calculation uses Kα1=1.5406 Å.

**Material type determination = C (amorphous-dominated)** — the full pattern has no sharp Bragg peaks, only two broad humps; the Rietveld route was not taken, and the "empirical fitting of amorphous broad envelopes + Scherrer coherence size" route was used instead.

**Core results**

| Broad hump | 2θ (°) | d (Å) | FWHM (°) | Apparent coherence size (nm) |
|---|---|---|---|---|
| (002) main broad hump | 29.75 | 3.00 | 2.26 | 3.63 |
| (10)/(100) broad shoulder | 41.30 | 2.18 | 3.20 | 2.66 |

- Empirical fit (xrd_refine_manual extras + 6th-order background, dummy main phase scale fixed at 0): **Rwp = 6.04%** (baseline 97.62%, Rexp 3.70%, χ² 2.66), with no crystalline impurity phase.
- In the fit the half-width H of the two broad humps is held up against the engine's 4.0° upper limit (parameter at the bound), which is a model limitation; it was re-checked that the half-width of the main broad hump after background subtraction is still 2.26°, so the conclusions on peak position and coherence size are unaffected. The attempt with an engine copy with the H upper limit relaxed was not completed because execution timed out, and this is disclosed honestly in the report and the logs.

**One point to draw attention to**: d(002)=3.00 Å is smaller than typical hard carbon (3.6–4.0 Å) and even graphite (3.35 Å), which leans toward a more condensed/graphite-like short-range order; without an internal standard a 2θ calibration offset cannot be excluded, so re-checking by Raman or interlayer-spacing measurement is recommended.

## Products (all in the data folder)

- `report.md` — full report (including λ reconciliation, convention notes and boundary disclosure)
- `amorphous_carbon_fit.png` — full-pattern plot; `amorphous_carbon_fit_fit.png` — fit figure (observed/calculated/background/residual)
- `result.json` / `components.json` — fit record and component curves
- `plan_amorphous.json` — fit plan; `pattern_twocol.txt` — cleaned two-column data
- `workflow_state.json`, `xrd_workflow/journal.jsonl`, `xrd_workflow/journal.md` — workflow state and logs (including the summary section)

As agreed, the wrap-up has cleaned up temporary progress/cache and intermediate working files (including the abandoned engine-edit copy), keeping the logs, the fit record and the final deliverables. If the decomposition of the two broad humps is to be made cleaner (letting H come off the 4° bound and reducing the systematic residual in the broad-hump region), the engine copy with the relaxed H upper limit can be re-run following the "handover suggestions" in `report.md`.

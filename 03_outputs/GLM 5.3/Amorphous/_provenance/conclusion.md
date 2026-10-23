<code>
Processing complete. The amorphous carbon anode XRD data have been processed strictly according to the dsh-xrd five-stage workflow, and all work is saved under the `Amorphous` folder.

## Conclusion summary

**The sample is confirmed fully amorphous (class C)**: the whole pattern consists of only 3 smooth broad humps + a smoothly decaying background, **with no sharp impurity peaks at all** (no Cu foil/Al/Si), and no crystalline main phase—therefore Rietveld does not apply, and the class C route was followed with empirical broad-hump modelling.

**Final fit (round 4, clean convergence)**:
| Metric | Value |
|---|---|
| **Rwp** | **3.82%** (baseline 98.62%, reference target <10 ✓ met) |
| Rexp / χ² | 3.70% / 1.06 (already at the statistical limit) |
| fit_status | success, zero parameters at the bound, zero warnings, plateau=true |

**Broad-hump parameters** (pseudo-Voigt, ±1σ):

| Broad hump | Centre 2θ | d spacing | FWHM | Area share | Scherrer apparent D (window/model, two readings) |
|---|---|---|---|---|---|
| Low angle | 16.66±0.05° | 5.32 Å | 7.62° | 18.3% | — / ≈1.05 nm |
| **main** | **30.06±0.07°** | **2.97 Å** | 10.13° | 63.9% | **≈2.29 nm / ≈0.81 nm** |
| secondary | 41.92±0.04° | 2.15 Å (≈ carbon (10) band) | 7.08° | 17.9% | ≈4.26 nm / ≈1.20 nm |

**Assignment caveat (reported as-is)**: the main broad hump at 30.06° (d=2.97 Å) **does not match typical hard carbon (002)** (23–25°, d 3.6–4.0 Å) and lies between (002)/(100)—per "do not force a fit when information is insufficient" it was not forcibly indexed; supplementing **Raman (D/G bands) / XPS / synthesis route** information before assigning it is recommended. All Scherrer values are **apparent coherence lengths** (no standard sample, no instrumental broadening subtracted), and the area shares are **semi-quantitative** (broad-hump/background decomposition is not unique and must not be read as phase fractions).

## Process highlights
- **λ reconciliation**: the data header confirms the Cu Kα doublet is not stripped (Monochromator=0) and it was passed explicitly to the engine; d spacings use Kα1=1.5406 Å
- **Engine adaptation** (the formal route per xrd-refinement §4.3): fully amorphous with no cif/atoms, so an engine copy was taken for a minimal amorphous-only adaptation (refusing to fabricate a nominal graphite cell—d002=3.0 Å is unphysical)
- **4 iterations**: r1/r2 hit bounds and were invalid → r3 converged but degenerated against the bound → r4 merged the redundant broad humps and then converged cleanly; the mid-way 19.24° doubt was verified against the raw data as noise
- **Wrap-up cleanup** was carried out as agreed: the logs, the final fit record and the deliverables were kept, and intermediate work files were cleaned

## Main deliverables (all in the `Amorphous` folder)
- `report.md` — full report (including all honesty statements and coverage statements)
- `Amorphous_final_fit.png` — final fit figure (obs/calc/bg/components + residual)
- `result.json` / `components.json` / `plan_amorphous_r4.json` / `xrd_engine_custom.py` — fit results and what is needed to reproduce them
- `peak_survey.json` / `phase_summary.json` / `workflow_state.json` / `xrd_workflow/journal.jsonl`+`journal.md` — peak survey, phase-identification conclusions, state and per-round log
</code>

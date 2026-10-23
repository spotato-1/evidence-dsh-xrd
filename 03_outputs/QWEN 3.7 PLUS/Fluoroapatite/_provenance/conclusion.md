## Fluoroapatite XRD: Refinement complete

### Refinement results

| Metric | Value |
|------|-----|
| **wR** | 20.95% |
| **R** | 15.13% |
| **Rb** | 16.35% |
| **wRmin (statistical limit)** | 5.61% |

### Cell parameters

- **a** = 9.3703 Å
- **c** = 6.8848 Å  
- **V** = 523.51 Å³
- **Space group**: P6₃/m (No.176)

### Deliverables

All results are saved in the `FAP_final/` directory:

- `FAP_final.gpx` — GSAS-II refinement project
- `FAP_built.cif` — refined structure CIF
- `FAP_fit.png` — fit figure
- `FAP_report.md` — refinement report

### Work log

- `xrd_workflow/journal.md` — complete refinement history (15 rounds)
- `workflow_state.json` — work state snapshot
- `review_judgment.md` — complex-case review judgement panel

### Explanation of the missed target

The target R value <10% was not reached. The main problems are:
1. Refining the atomic coordinates made wR worse (20.95% → 31.38%); there may be a systematic bias in the initial CIF values
2. The Uiso of some atoms is rather high (O3: 0.056, F: 0.060 Å²) or was clamped (O1/O2: 0.005 Å²)
3. Default instrument parameters were used; a measured instrument parameter file, if available, could improve this further

**Recommendation**: inspect the residual plot manually in the GSAS-II GUI, and try anisotropic thermal parameters or a revised constraint strategy.

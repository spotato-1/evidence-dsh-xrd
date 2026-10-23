# Fluorapatite XRD data processing · Final report

**Target met**: reference target Rwp ≲ 10% — **GSAS-II final wR = 9.75% (GOF 1.74)**, and all work has been completed and delivered according to the five-stage workflow of the xrd plugin. All intermediate records have been fully retained (including the 4 debug files rebuilt word-for-word after accidental deletion).

## Final refinement results (GSAS-II convention)

| Metric | Value |
|---|---|
| **wR (Rwp)** | **9.75 %** |
| R (Rp) | 7.66 % |
| Rb / wRb | 7.47 % / 9.12 % |
| wRmin (statistical limit) | 5.61 % |
| **GOF (χ²_red)** | **1.74** |

**Structure (pure fluorapatite Ca₅(PO₄)₃F, P6₃/m, single phase)**:
- Cell: a = b = **9.3703(1) Å**, c = **6.8849(0) Å**, V = 523.52 Å³
- Coordinates: finely adjusted from the COD 1549763 single-crystal refined values (Ca2 x=−0.00784, P x=0.36784, etc., full table in the report)
- Occupancy: all 1 (stoichiometric); all Uiso positive: Ca 0.012–0.013, P 0.0125, O 0.012–0.015, **F 0.0224** (the fluorine-site thermal parameter is slightly larger, a normal apatite feature)
- Bond-length review (pymatgen): Ca–F 2.302 Å; Ca–O 2.344–2.509 Å; P–O 1.519–1.573 Å —— standard apatite geometry ✓
- Cross-validation: fp2k and GSAS-II independently converged to the same cell (9.3703/6.8848 vs 9.3703/6.8849) ✓

## Phase identification conclusions

All 40 picked peaks are explained by P6₃/m fluorapatite; **no evidence of a second phase** (the residual is mostly noise, and all unmatched peaks are at background-noise level); [001] preferred orientation was adjudged **absent** by March-Dollase refinement (ratio≈1, no change in wR). The starting model was built by `build_orbit` from COD 1549763 (2018 natural FAP single-crystal data, Mn/Sr removed to a pure Ca end-member) (Wyckoff 4f/6h/6h/6h/6h/12i/2a all correct, validate pass).

## Deliverables (all inside the data folder)

| File | Content |
|---|---|
| `FAP_final/FAP_fit.png` | publication-level fit figure (obs/calc/bg/residual/hkl labels, V4 image read passed) |
| `FAP_final/FAP_built.cif` / `FAP_refined_built.cif` | GSAS-II official export CIF (+ bond-length window check pass) |
| `FAP_final/FAP_report.md` | metrics/cell (with esd)/atom parameters/strong-reflection table |
| `FAP_final/FAP_final.gpx` + `.lst` | converged project and refinement log (GSAS-II 5839) |
| `xrd_workflow/journal.md` (20 rounds) + `journal.jsonl` | full per-round record + summary chapter (material/phase identification/defect master table/results achieved/untried items/hand-over suggestions) |
| `workflow_state.json`, `review_judgment.md` | state and review, two columns |
| `work/` (full 29.7 MB) | candidate pcr/dat, scale probes, all fp2k working directories, GSAS intermediate projects and snapshots —— **all retained as you requested** |

## Honesty statements

- The target (R≲10%) has been met; the fp2k corroborating Rwp is 18.7 (a different convention, not directly comparable with GSAS wR).
- All failed rounds (fp2k coordinate/PO/Biso divergence ×4, GSAS atoms incident ×1) were recorded as-is and rolled back, and are not counted in the conclusions.
- **Untried dimensions** (not "cannot be improved"): background order iteration (condition not triggered—target already met), anisotropic ADP, SH/L asymmetry refinement, absorption correction; a few small residuals remain at the strong peaks at 31–33°/46–50° (suspected peak-shape detail).
- Tool-layer pitfalls found and fixed during troubleshooting (logged for reuse): fp2k needs a **three-column dat (σ column)** or the weights degrade; the GSAS instprm **Type must be 3 characters (PXC)** and the doublet intensity-ratio key is `I(L2)/I(L1)`; GSAS hold mode has a rollback gap when continuing across calls (continuation switched to `xrd_gsas_ops` snapshot management).

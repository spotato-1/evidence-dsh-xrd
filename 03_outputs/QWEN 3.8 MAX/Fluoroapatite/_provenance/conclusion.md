Task wrap-up complete. Per your choice **no file was deleted** (the cleanup decision has been recorded in the state file), and the goal is marked complete.

# Wrap-up summary

**Final delivery** (all under the `Fluoroapatite` folder):

| Deliverable | Path |
|---|---|
| Delivery package (clean project/log/CIF/figure/report) | `FAP_final/` (FAP_final.gpx, FAP_final.lst, FAP_built.cif, FAP_fit.png, FAP_report.md) |
| Continuation starting project | `gsas_proj_final.gpx` |
| Authoritative log (24 strict JSON entries) + human-readable quick overview (with summary subsection) | `xrd_workflow/journal.jsonl`, `xrd_workflow/journal.md` |
| State file (schema 2, phase 5) | `workflow_state.json` |
| Phase identification record / review judgment column | `phase_summary.json`, `review_judgment.md` |
| Structure source CIFs (6 candidates + final modern coordinates) | `ref/` (final: `ref/FAP_modern_orbit_01.cif`) |
| Home-made instrument file (Type:XRC, including pitfall notes) | `INST_FAP.instprm` |

**Core numbers**: single-phase fluoroapatite P6₃/m; GSAS-II delivery basis **wR=11.50%, GOF=2.06, R_Bragg=4.77% (325 reflections)**; a=9.37074, c=6.88499 Å; all Uiso physical, REVIEW pass, CIF bond-length audit pass (P–O 1.515–1.566 Å); impurity residual screening **detected no second phase**; F occupancy fully occupied (D3 criterion).

**Reported honestly**: the manual-engine basis reference value (≈10%) was not reached (numerical plateau 23.21%, an engine capability boundary); the remaining gap between wR and Rexp≈5.6 is attributed to peak-shape/background model limits (no real instrument parameter file, Size↔X collinearity) — the untried items (anisotropic Uij, generalized mustrain, MD orientation, etc.) are listed one by one in the coverage subsection of `journal.md`, and "untried" and "cannot be improved" are stated separately.

Should wR be pushed lower later, the "Hand-over suggestions" in `journal.md` give the route (supplement a measured instrument file → anisotropic Uij → uniaxial microstrain, single variable + entry=hold rollback). The run can be resumed from this directory at any time.

All complete. Below are the processing results for this PbSO₄ data.

## Conclusions

| Item | Result |
|---|---|
| Phase | **PbSO₄ anglesite (barite type), space group #62** — single phase, no evidence of a second phase |
| Structure source | COD 9015524 (Antao 2012), `validate` = pass (24 atoms/cell, shortest contact 1.448 Å = S–O bond) |
| **Delivered R value** | **GSAS-II wR = 9.51 %** (R 7.28 %, Rb 7.25 %, **wRmin 4.94 %**, **GOF 1.93**, chi² 22174.9, RF 3.57 %) |
| Corroboration | FullProf fp2k Rwp 18.4 % (conventional), Bragg R 6.9 % — *the two bases are not directly comparable* |
| Cell parameter | a 6.960893 / b 8.481366 / c 5.399204 Å, V 318.758 Å³ (deviation from literature < 0.05 %) |
| Structure | anisotropic Uij for Pb and S (all diagonal terms positive, tensor positive definite); isotropic Uiso for O all positive; occupancies fixed at nominal values |
| Bond lengths | S–O 1.427–1.516 Å, shortest Pb–O 2.610 Å; `xrd_export_cif` verdict = **pass**, 0 anomalous |
| Target | the reference value "R < about 8 %" **not reached** (1.5 percentage points short) — honestly reported as required |

## Two key judgments in the process

1. **Zero-point error (the biggest breakthrough this time)**: fp2k's first round pushed Rwp from 87.4 down to 27.1, but a peak-by-peak check found the calculated peak positions **systematically off by +0.025° (exactly one data step)**, while the ladder scheduled the zero refinement at too early a position (when the background and peak shape were still poor), so it was rejected and the error was absorbed by the **cell** (the cell expanded by 0.1 % overall). After manually turning on the zero refinement code, **27.1 → 18.4**, and the cell simultaneously returned to the literature value. An independent GSAS-II refinement gives Zero = −0.045162(32)°, cross-corroborating fp2k's −0.0459(4)°.

2. **Two exclusions of "lower R but not delivered"** (this is the red line most in need of being held this time):
   - **All-atom anisotropic ADP**: wR 9.695 → 9.440, but review judged **fail** (O2's U33 and O3's U22 are **negative diagonal elements**) ⇒ 30 Uij exceed what the data can determine, **a false gain, discarded**. Redone as **partial anisotropy** (Pb/S only) gives wR = **9.506 %** with review = **pass**, and that is the delivered model.
   - **20th-order background**: raising the clean model to the tool's hard cap of 20 orders gives wR 9.076 % with review also pass, but the highest-order oscillation period ≈ 7.5° is already close to the peak spacing (the classic "background eating peaks" regime), and O2's Uiso was changed by **+23 %** and S's U12 halved ⇒ **recorded only in the coverage statement, not used as a delivered result**.

## Main outputs

- `XRD_analysis and refinement report.md` — complete report (including coverage statement, untried items, defect master table)
- `PbSO4_final/` — **delivery package**: `PbSO4_final.gpx` (clean GSAS project), `PbSO4_final.lst`, `PbSO4_O4_Pb_S.cif` (official GSAS export), `PbSO4_fit.png`, `PbSO4_report.md`
- `PbSO4_final/PbSO4_fit_export.png` — second-version figure (the V4 image reading found a slight overlap between the delivery package's statistics box and the apex of the 29.7° main peak; this version has no occlusion and is suitable for publication)
- `xrd_workflow/journal.jsonl` (14-round round-by-round log) + `journal.md` (including the summary sections: material and goal / phases and crystal family / defect master table / results achieved / **untried · undecided items** / suggestions for whoever takes over)
- `workflow_state.json`, `review_judgment.md` — state and review-judgment columns

## Untried items (listed separately, not written as "cannot be improved")

Other polymorphs of PbSO₄ were not exhaustively enumerated (judged an A-class standard sample, not mandatory per the workflow) · whole-pattern residual phase screening on the converged project was not done · **the manual-engine basis has no independent R value** (the 1500 s budget was exhausted, and a genuine engine fault `NameError: EngineStopped` was hit — "environment limitation + genuine fault", recorded) · the zero-point source was not reconciled with the vendor's original `raw/PBSO4.XRA` · the intermediate ADP combination of Pb+S+partial O was not tried.

Per your choice, **all intermediate products have been retained** (about 25.3 MB, including each round's pcr/gpx/lst/out/prf in `round/r02…r14` and the step-by-step R trace), with no closing cleanup done.

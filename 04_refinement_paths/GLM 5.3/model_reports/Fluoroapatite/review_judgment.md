# Complex-case review · judgment panel (AI maintained)

## I. What the user said in the manual input window (original words, not paraphrased)

1. "workspace\GLM 5.3\Fluoroapatite" contains an XRD dataset; the composition is a fluorapatite ore powder sample. Process the data strictly following the xrd plugin. Save the work under the data folder.
2. "Continue"
3. Option-box reply: fitting objective = "publication-level structural refinement (recommended)"; supplementary information = "none".
4. Wrap-up cleanup option-box reply: "Do not clean files".
5. "Continue; do not delete any intermediate records"

## II. Current best physical solution (final delivery state)

- Model: pure fluoroapatite Ca5(PO4)3F, P6₃/m, 7 sites (Ca1 4f / Ca2 6h / P 6h / O1 6h / O2 6h / O3 12i / F 2a).
- **Final metrics (GSAS-II convention): wR = 9.75%, R = 7.66%, Rb = 7.47%, wRmin = 5.61%, GOF = 1.74 — the reference target ≲10% has been achieved.**
- Unit cell a=b=9.3703(1) Å, c=6.8849(0) Å, V=523.52 Å³; coordinates slightly adjusted from the 1549763 starting point (Ca2 x −0.00784, etc.); all Uiso positive (Ca 0.012–0.013 / P 0.0125 / O 0.012–0.015 / F 0.0224); all occupancies 1; bond lengths pass (Ca–F 2.302 / Ca–O 2.344–2.509 / P–O 1.519–1.573 Å).
- Deliverables: FAP_final/ (gpx + lst + FAP_fit.png + FAP_report.md + FAP_built.cif + FAP_refined_built.cif).
- Cross-validation: fp2k and GSAS independently converge to the same cell (9.3703/6.8848 vs 9.3703/6.8849).

## III. Unresolved hypotheses (item by item, final state)

1. ~~[001] preferred orientation~~ — **adjudicated: no significant PO** (GSAS MD ratio≈1, wR unchanged).
2. ~~Coordinate fine-tuning~~ — adjudicated: accepted by grouped GSAS refinement (10.26→9.97).
3. ~~Per-atom Biso~~ — adjudicated: all positive, wR −0.22, accepted.
4. ~~Second phase~~ — not found (the residuals are mainly noise; the remaining peaks are all at background level).
5. Remaining minor items (disclosed, non-blocking): a small amount of residual at the strong peaks 31–33°/46–50° (suspected peak-shape detail); background-order upgrade not enabled (condition not triggered: the target was already achieved); anisotropic ADP not tried (isotropic is already sufficient, GOF 1.74).

## IV. branch list (including frozen ones)

| branch | status | note |
|---|---|---|
| Main line: pure-phase model → GSAS-Ⅱ → delivery | **complete** | wR 9.75%, FAP_final/ delivered |
| cod_1010996/1011044, cod_1533064, mp_aaaaajoz | closed | wrong cell/chemical mismatch/P1 unfavourable/DFT distortion |
| M7–M9 (fp2k-side coordinates/PO/Biso) | frozen | fp2k diverged; already adjudicated in GSAS |
| GSAS atoms released all at once, the 69.38 contaminated state | closed | divergence accident; the grouped retry succeeded |

## V. Current freeze state

- No workflow freeze; the §6 checklist has been fully executed once (numerical / in-design rejection classified, limit mode not entered).
- **Wrap-up policy (user adjudication, round 20)**: keep everything, delete no intermediate record. The 4 debug files that were once mistakenly deleted (dbg_gsas.py / dbg_out.txt / dbg_err.txt / plot_prf.py) have been rebuilt verbatim from the session record and marked RECONSTRUCTED. No deletion will be performed from now on.
- All work is complete: refinement delivered (wR 9.75%) + records complete (journal 20 rounds, state files, dual-panel review, delivery package FAP_final/).

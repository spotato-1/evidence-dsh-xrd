# LiFePO4 XRD refinement final report

## I. Results achieved (target met)

| Metric (GSAS-II convention, delivery convention) | Value |
|---|---|
| **wR** | **6.70%** (reference target <8% ✓) |
| R / Rb / wRb | 5.14% / 6.20% / 8.30% |
| wRmin (statistical limit) | 6.15% |
| **GOF** | **1.09** (only 9% above the statistical limit) |
| chi² | 8306 (7001 observed points) |

Cross-conventions (not directly comparable, written separately as-is): FullProf(fp2k) ladder Rwp_mean=18.5 (the 4-I adjudication value); manual engine Rwp=26.92 (the 4-II numerical-plateau value).

## II. Structural results (Pnma olivine, #62, Z=4)

| Parameter | Value |
|---|---|
| Cell | a=10.3244(2), b=6.0045(1), c=4.6897(1) Å, V=290.725(14) ų (consistent with the ICSD 16147 literature) |
| **Li/Fe antisite (user-mandated, must do)** | **pairwise exchange model x = 0.89%** (0.89% Fe on the Li site ↔ 0.89% Li on the Fe site, stoichiometry keeping LiFePO4 exactly satisfied); under three conservation constraints the LS-determined value is 0.71%, a fixed-x scan gives a minimum of ≈0.7%, the same order as well-crystallised LiFePO4 in the literature (0.37%); **recommended quoted range 0.5–1.5%** (flat curve, large uncertainty) |
| Uiso (Å²) | Fe 0.0137 / P 0.0175 / O 0.008–0.017 (all physical); Li fixed at 0.005 (XRD-insensitive, declared as-is as a non-measured value) |
| Bond lengths | Fe–O 2.088–2.252 / P–O 1.530–1.574 / O–O 2.407–2.599 Å (all textbook-grade) |
| Corrections | surface roughness (SurfRough, intensity systematic error of a strongly absorbing sample) + 14th-order Chebyshev background + isotropic microstrain 4483×10⁻⁶ |

## III. Workflow and checklist execution

All five stages completed: **①identification** (class A, the complex checklist triggered because "the antisite must be considered") → **②preliminary screening** (binary RAW parsed to 7001 points over 10–80°; Cu Kα doublet determination: header string Cu anode + no monochromator) → **③phase identification** (polymorphs 26 structure types + literature enumeration over 3 families → fp2k actually-run adjudication Pnma 18.5 ≪ Cmcm 86.3 / Pna21 82.6) → **④refinement** (the three stages I/II/III, fp2k numerical plateau 18.5, manual engine numerical plateau 26.92 with no decrease in three attempts → GSAS) → **⑤delivery**.

The entry-by-entry adjudication of the 17 entries of the defect master table (14 categories + 3 endnotes) is in `defect_table.json`: **D-02 antisite applies and was adopted**; D-11 microstrain applies; Li vacancies (D-01/N-03) **undecided**——XRD is intrinsically insensitive to Li (scan effect ≲0.02 wR points) and ICP/EDS is needed; all the others are not applicable, each with a written reason.

**Two hard fights during the process (reported as-is, both diagnosed and fixed)**:
1. **The GSAS first-round delivery project was in fact a bad state**: the reported wR 7.53 belonged to a non-physical intermediate state with negative Uiso on all atoms; after Uiso clamping, further refinement crashed because the σ² full-angle clamp (negative U/V/W) → 3 zero SVDs in the Hessian → a wild step hit a negative cell, with a true wR=39.78 (the cached value was misleading). Fix: rebuild the project with a non-degenerate parameterisation (X/Y never opened, profile opens Mustrain only).
2. **Pure-Lorentzian peak-shape trap**: once σ² is clamped dead the U/V/W derivatives are identically zero and the LS can never escape → the strongest peak's calc apex sits 40–50% below obs. Fix: manually reset the Gaussian component seeds → wR 11.35→7.80. **The first-round "antisite 4.5%" conclusion was voided with it** (it was compensating a wrong peak shape); under the correct peak shape both paths re-adjudicate to 0.7–0.9%.

## IV. Coverage statement (honesty, as the checklist requires)

- **Tried and ineffective** (kept separate from "untried"): SH/L asymmetry, March-Dollase preferred orientation (010), Kα2 ratio refinement (kept at 0.5), Li vacancies (insensitive), negative Uiso (rejected as non-physical).
- **Untried**: background orders 16–20 (gain rate already <0.03/order); generalised anisotropic broadening (isotropic already at the statistical limit); Li Uiso; size/strain separation (no standard sample); twinning (no TEM evidence, marked undecided per D-13). Conclusion wording: **"within the range tried, it has reached the statistical noise level (GOF 1.09)"**.
- **Visual check V1–V4 disclosure**: both office_read_image and modlens_read_image failed twice because of an engine JSON contract mismatch (environment limitation) ⇒ throughout, the workflow fell back to channel ③ numerical criteria (peak-position table/residual pattern/FWHM table); please eyeball the finished figure `LiFePO4_fit.png` yourself (legend/statistics box laid out per the occlusion-prevention rules).
- Failure classification (D18③): the two crashes are environmental/numerical (fixed, not tool defects); one interactive question was interrupted and then confirmed orally by you ("keep everything").

## V. Deliverables (all under the data folder, all retained per your decision)

- **delivery package `LiFePO4_final/`**: clean project gpx + lst + official-export CIF + occlusion-safe fit figure (with hkl assignment ticks) + report.md
- CIF: `LiFePO4_built.cif` (mixed sites carrying antisite semantics), `LiFePO4_final/LiFePO4_built.cif`
- Authoritative logs: `xrd_workflow/journal.jsonl` (16 lines) + `journal.md` (with summary chapter) + `defect_table.json` + `workflow_state.json` + `review_judgment.md`
- Key-node projects: `gsas_proj.gpx` (rebuilt baseline), `LiFePO4_final_work.gpx` (joint-refinement state), `gsas_ops_out.gpx` (final delivery source) and all other intermediate files are retained per your instruction

**Hand-over note**: do not refine the delivery project any further (the constraints have been cleaned and the cached wR will be lost); to continue the work, branch from `gsas_ops_out.gpx`. The residual is already at the statistical noise level, physical measures are expected to lower it by ≤0.5 points more, and pressing R further is not recommended to avoid overfitting.

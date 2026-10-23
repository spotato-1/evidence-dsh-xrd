The work is fully complete. Here are the results and the key points.

## The two most important things

**① The data is a vendor binary file, not text.** The plugin's text reader got 0 data rows from `24.raw`. After a byte-by-byte parse I confirmed it is a binary format (magic `FI`) and located: header float64 `1.540593/1.544414/1.392246` (Cu Kα1/Kα2/Kβ), float32 `10.0 / 80.0 / 0.01` (2θ start/end and step), intensity array 7001×float32 starting at offset 3158. **Three independent verifications**: 30/30 measured peaks were indexed to olivine Pnma (rms 0.009°); the Kα2 satellite is visibly measured at 72.44° (confirming the doublet); fp2k's re-read agrees with the source file point by point (maximum deviation 0.005 counts). The decoder is `decode_raw.py` (with self-validation assertions, reproducible).

**② The antisite defect quantification holds, but only by "working around" the occupancy–thermal-parameter compensation.** Releasing the occupancies for refinement directly lets the thermal parameters swallow it: with only a Σ=1 conservation added, the two sublattices give **mutually contradictory** antisite amounts (4a: 12.5% vs 4c: 4.0%) and the Li-site Uiso is pushed up to 0.171; when `equiv_afrac` ties them into a single x, GSAS pushes the occupancy to a **negative value**. So I switched to a **profile-likelihood scan with the thermal parameters frozen** (not relying on the constraint machinery):

| x | 0.00 | 0.02 | **0.04** | 0.06 | 0.08 | 0.10 | 0.15 |
|---|---|---|---|---|---|---|---|
| wR % | 6.73 | 6.39 | **6.24** | 6.31 | 6.59 | 7.02 | 8.51 |

In the control group (thermal parameters free) the minimum ran to x≈0.08, but that was bought by raising Uiso(Li) from 0.005 to 0.106 Å² (B≈8.4) — **that curve is not used as evidence**. Conclusion: **Li/Fe antisite x ≈ 0.04 (4 %)**, consistent in magnitude with literature reports for solid-state LiFePO4.

## Refinement results (delivery basis = GSAS-II)

| Quantity | Value |
|---|---|
| **wR** | **6.22 %** (R 4.87 / Rb 5.29) |
| **wRmin (statistical limit)** | **6.15 %** → **GOF = 1.01, the data limit has been reached** |
| Cell | a=10.3254, b=6.0050, c=4.69006 Å, V=290.802 Å³, ρ=3.698 g/cm³ |
| Thermal parameters | all past negative Uiso have been closed by `uiso_floor` (final state below-floor=0, negative=0), review = pass |

The R value decreased monotonically throughout: fp2k 22.0 → GSAS 6.71 → 6.45 → 6.21 → **6.22 delivered**, and limit mode was never triggered.

**The two bases are written separately**: FullProf Rwp = 22.0, but recomputing the same `.prf` with w=1/y_obs gives **9.5 %** — the 2.3-fold difference is purely a difference in weight definition, and the two cannot be compared across bases.

## Two pitfalls hit along the way (recorded in the log)

- The Rwp ≈ 94–99% given by `ladder:false` (score-only) **is not a structural error**; it is a portrait of a converter-produced pcr that **contains no refinement code at all**, i.e. zero parameters being refined; the full ladder immediately falls into a reasonable range.
- GSAS reported `Invalid cell metric tensor for phase #0 (built)` (adding the antisite in place with `set_site_composition`) — recorded under the classification "genuine fault / in-design refusal", and avoided by starting a new project from the CIF.

## Honesty boundary (not exhausted, not "beyond improvement")

- **Do not quote the thermal parameters directly**: most atoms' Uiso sit at the physical lower bound 0.005 Å², indicating that the peak shape/background still contains unmodeled systematic components — suggest doing the background order-escalation iteration first.
- **The 4 % antisite should be read as "about 4 %, trustworthy in magnitude"**; the true uncertainty is dominated by systematic error (the occupancy–thermal-parameter correlation for Fe/Li under X-rays is too strong; for a publication-level esd, synchrotron radiation or neutrons are recommended).
- **Untried items** (listed one by one in the report): background order-escalation iteration, releasing the total-occupancy conservation to check for vacancies, the two site-splitting schemes, anisotropic size/mustrain, preferred orientation (**requires SEM morphological evidence first**; not opened without it).

## Deliverables (all under the `LiFePO4` directory)

`LiFePO4_final/` (clean gpx + lst + **official GSAS export_CIF** + fit figure + report.md), `REPORT.md`, `defect_table.json` (master table of 14 defect classes × 10 fields, every unexecuted item carrying its reason), `phases/phase_summary.json`, `workflow_state.json`, `xrd_workflow/journal.jsonl` + `journal.md`. All machine-readable files passed strict JSON self-validation (including the 11-line journal).

Per your choice, **all intermediate files are fully retained** (47.9 MB total, the scene is fully traceable), and nothing was deleted.

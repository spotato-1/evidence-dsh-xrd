The XRD data processing and refinement of ZnO have been run through per the dsh-xrd five-stage workflow, and all outputs are under `ZnO/`.

## Conclusions

**Phase**: wurtzite ZnO, **P6_3mc (#186)**, single phase. The cell is given by **indexing of the data's own peak positions** (not a database cell): **a = 3.25019(3) Å, c = 5.20928(3) Å, V = 47.657(1) Å³**; Zn (1/3,2/3,−0.00205(9)) Uiso 0.0052 Å², O (1/3,2/3,0.38118(9)) Uiso 0.0028 Å²; Zn–O = 1.973–1.996 Å.

**Fit (GSAS-II delivery basis)**: **wR = 10.43 %**, GOF 1.90, wRmin 5.48 %, **RF = 2.20 %** (90 reflections); review = pass, occupancy 1.000/1.000.

## Three points that must be made clear

1. **The target was not reached, honestly reported.** The target was "Rwp below ≈8%" (reference value). The delivery is 10.43 %, 4.95 percentage points away from the statistical limit of 5.48 %. But at the **structural level it is already publication-level** (RF 2.20 %); the residual is attributed to **peak-shape mismatch** (the residual concentrates at the strongest peak, Durbin–Watson 0.24), **not** to a missing phase, missing defects or insufficient background.

2. **Two "false improvements" were blocked, and this is the most valuable part of this task.**
   - I initially used Materials Project's DFT cell as the starting point, which is 0.4 % smaller than measured → the least squares could not remove the peak-position misalignment, so it **widened the peak width by 3–6 fold to cover it up**, and Rwp stuck at 54–72 %. After switching to the cell from the data's own indexing and fixing it, Rwp dropped directly from 37 % to 11.55 %.
   - During occupancy refinement **O was pushed to 1.095 (above 1, non-physical)**, buying only 0.096 percentage points of R at the cost of doubling O's Uiso — a typical false gain. Per the red line that "a delivered structure in normal mode must obey physical limits", **the model containing that occupancy does not enter the deliverables**, and is only kept on file in `work/gsas_occ/`.

3. **Do not quote GSAS's `Size` for the crystallite size.** The `Size = 10.000 µm` in the delivered project is a nominal value: after fixing the instrument profile to the 11-BM default, wR deteriorated to 20.88 %, showing that the size broadening has been effectively absorbed by the peak shape and cannot be separated. An independent Scherrer basis gives an **apparent coherence length ≈32 nm (26.4–36.8 nm)**, about 2.1 times the nominal 15 nm — I **reported this inconsistency honestly and did not smooth it over** (it may be a basis difference between TEM number-average and XRD volume-average; adding TEM/SAXS is suggested).

**Cross-check** (the meas you chose): meas wR 10.441 %, a=3.24961, c=5.20838; the angular scale correction shifts the cell overall by only about 0.02 %, so the conclusion is robust. Incidentally, the **zero = +0.0008°** from indexing the corr data also proves in turn that your choice of corr as the primary data was right.

## Two environment problems encountered midway (resolved)
- `cif_to_pcr` / `xrd_refine_auto` require approval to execute external programs; the first two waits timed out, and after your approval they ran normally.
- GSAS-II could not read a `.instprm` in which I had written 6 lines of provenance comments (`KeyError 'Type'`); after changing it to the standard single-line header it was normal; the provenance note was moved to `APS11BM_30keV.instprm.PROVENANCE.txt`.

## Main outputs
`REPORT.md` (complete report), `xrd_workflow/journal.jsonl` (12-round authoritative log) + `journal.md` (including the fixed summary sections and coverage statement), `workflow_state.json`, `ZnO_final/` (delivery package: clean gpx + lst + official GSAS CIF + figure + report.md), `analysis/index_peaks.py` + `indexation.json`, `ref/ZnO_wurtzite_P63mc_measured_orbit_01.cif`.

Per your choice **all files are retained and not cleaned up** (138.5 MB, including the step-by-step fp2k backups and candidate-screening copies, fully reproducible). **The untried dimensions** are also listed item by item in the report (preferred orientation, anisotropic Uij/Mustrain, changing the peak-shape function), so the conclusion says "no improvement within the range tried" and does not say "the data limit has been reached".

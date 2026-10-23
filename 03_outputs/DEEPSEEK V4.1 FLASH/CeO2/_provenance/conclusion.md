The CeO₂ analysis has been run to completion per the dsh-xrd plugin's five-stage workflow, and all outputs are under the `CeO2` folder (per your choice, all process files were retained and none were cleaned up).

## Results

| Item | Result |
|---|---|
| Phase | **fluorite-type CeO₂, Fm-3m**, Ce 4a ×4 + O 8c ×8 |
| Cell | **a = 5.41089 Å**, V = 158.419 Å³ |
| Density | 7.2165 g/cm³ (theoretical 7.22 ✓) |
| Ce–O | 2.343 Å (= a√3/4, geometrically self-consistent) |
| Coherence size | **0.60193 µm** (isotropic) |
| Microstrain | **777.3 µε** |
| **R value (delivery basis GSAS wR)** | **16.10 %** (wRmin 4.41 %, GOF 3.65) |
| R value on target (R < about 10%) | **Not reached, honestly reported** |

## Two key findings

**1. Starting from a database model leads you into a ditch.** MP's CeO₂ is a GGA-relaxed primitive cell (a_conv=5.4675, 1.03 % larger than measured) and is written as a P1 primitive cell; starting a fit directly from it makes FullProf and the manual engine **fall into a wrong minimum at the same time** (Rwp 98 % / 89.6 %). I first determined a = 5.4118 ± 0.0011 Å by independently indexing 20 peaks, then built a normalized CIF with `build_orbit`, and only then was the space group correctly recognized (general position 192 → occupancy audit pass; earlier, under P1, the audit **passed just the same**, so looking only at the audit would miss it).

**2. The real bottleneck is axial-divergence asymmetry.** The equal-offset intensity ratio on the two sides of (111) reaches 9–12 fold (higher on the low-angle side), while high-angle (440) is nearly symmetric — because this data's peaks are extremely narrow (FWHM 0.0127°), the relative asymmetry of the fixed-width low-angle tail is sharply amplified. The manual engine has no asymmetry model at all, and the converter-produced pcr sets Asy1–4 all to 0, so both were stuck at 51.8 % / 60.9 %. **After releasing FCJ's `SH/L` in GSAS-II, wR dropped from 32.20 % to 25.98 % in one step**, the largest single-step improvement of the whole run.

## Two tool issues you need to know about

- **`xrd_refine_gsas`'s data+cif new-project path necessarily fails on this package**: the plugin passes `wavelength=` unconditionally, whereas this package's GSAS-II `add_powder_histogram()` has no such parameter. I built the project with this package's own bundled `GSASIIscriptable` API (`work/gsas/make_gpx.py`), then returned to the plugin's `gpx=` continuation path — **without replacing the plugin engine**.
- **`xrd_refine_auto`'s ladder returns a degenerate value Rwp=100 at every step after the `zero` step** and gets rolled back. This is a driver-level problem, not a sample conclusion.

## One declaration that must not be ambiguous

A free refinement once reached **wR = 12.84 %**, but in that one **Ce1's Uiso is −9.667×10⁻⁵ (non-physical)**, and per the red line it is **not delivered**. After imposing a Uiso lower bound the delivery is 16.09 % — **these 3.25 percentage points are exactly the improvement bought by the "non-physical degree of freedom", and have been discarded**. At the same time, the Uiso of the two atoms is now fixed at the nominal value 0.005 Å² with the U flag removed, which **counts as "not identifiable ⇒ nominally fixed", not a measured value**. The coverage list still contains "untried" items (occupancy, anisotropic thermal parameters, stacking faults/dislocations), so the conclusion states only that "**within the range tried, R could not be reduced further**".

## Main outputs

- `CeO2_XRDrefinement report.md` — complete report (including peak table, coverage statement, honesty statement, tool-issue disclosure)
- `CeO2_final/` — delivery package: clean gpx + lst + official GSAS CIF + occlusion-controlled fit figure + report
- `xrd_workflow/journal.jsonl` / `journal.md` — authoritative round-by-round log (11 rounds) + closing summary sections
- `workflow_state.json`, `review_judgment.md` — state protocol and judgment column

If you want to push R down further next, I suggest measuring an **instrumental standard** (LaB₆/NIST 660c) to decouple the instrument profile from size/strain — the bottleneck is no longer the background (raising the order 6→12 brought only a 0.001 improvement) nor the structural model.

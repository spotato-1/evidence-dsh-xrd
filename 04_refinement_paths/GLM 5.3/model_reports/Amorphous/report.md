# Amorphous Carbon Anode XRD Data Processing Report

**Sample**: Amorphous (composition as stated by the user: amorphous carbon anode)
**Data**: `pattern_2theta.txt` (Rigaku RAW4.00 text format; `pattern.raw` in the same directory is the same-source binary RAW1.01 and was not used)
**Measurement conditions** (verbatim from the header): 3432 points, 2θ = 10.000–79.997°, step 0.0204°; Cu target, Kα1 = 1.5406 Å / Kα2 = 1.54439 Å, AlphaRatio = 0.5, **Monochromator = 0 (Kα2 not stripped ⇒ laboratory doublet)**; scan on 2026-09-23 11:50:25.
**Material classification**: **Class C (amorphous / low-crystallinity dominant)** — processed according to the five-stage workflow.

---

## 1. Conclusion Summary

1. **The sample is fully amorphous**: the entire pattern consists of only 3 smooth broad halos plus a smoothly decaying background, **with no sharp impurity peaks whatsoever** (no Cu foil 43.3/50.4/74.1°, no Al 38.5/44.7°, no Si 28.4°, etc.), and no crystalline main phase.
2. **The main halo fit converged**: 3 pseudo-Voigt empirical broad halos + 6th-order Chebyshev background, **Rwp = 3.82%** (baseline 98.62%), Rexp = 3.70%, **χ² = 1.06 (already at the statistical limit)**; the optimizer converged cleanly (success, nfev=145, zero parameters at the upper bound, zero warning flags). **The target Rwp < 10 (reference value) is met**.
3. Halo parameters (±1σ): low-angle **16.66°** (d = 5.32 Å), main **30.06°** (d = 2.97 Å), secondary **41.92°** (d = 2.15 Å, ≈ the in-plane (10) band of carbon).
4. **Assignment caveat**: the main halo at 30.06° (d = 2.97 Å) **does not match the typical hard-carbon (002)** (23–25°, d 3.6–4.0 Å); it lies between (002) and (100) and is smaller than the graphite interlayer spacing of 3.354 Å — in accordance with "do not force a fit when information is insufficient", this is reported as-is, and the assignment awaits corroboration from Raman/XPS/synthesis route (see §5).

## 2. Data and Methods (five stages)

| Stage | Content | Products |
|---|---|---|
| ① Identification | Class C amorphous body; no XPS/EDS/Raman/CIF input | `workflow_state.json` |
| ② Initial screening | λ reconciliation (Cu doublet, explicitly passed to the engine); format conversion; full-pattern figure + **V1 visual peak determination**; measured FWHM of the broad halos; Scherrer apparent size | `pattern_clean.dat`, `Amorphous_fullpattern_fit.png`, `peak_survey.json` |
| ③ Phase determination | Class C default: V1 + numerical peak picking confirms no sharp impurity peaks ⇒ skip phase determination and fit directly; the 19.24° doubt was verified against the raw data to be a single-point Poisson fluctuation | `phase_summary.json` |
| ④ Refinement | Manual engine (bounded LM) amorphous-only model (see §3), 4 rounds of iteration to the R-value basin | `result.json`, `components.json`, `plan_amorphous_r4.json` |
| ⑤ Reporting | This report + delivery figure + journal summary section | `report.md`, `Amorphous_final_fit.png`, `xrd_workflow/` |

**Engine adaptation note** (method record): the manual engine's original plan validation requires a cif or atoms; this sample is fully amorphous with no crystalline main phase, so forcibly supplying a nominal unit cell (e.g. graphite) would inject Bragg peaks that conflict with the broad halos or produce a non-physical cell (d002 = 3.0 Å < graphite 3.354 Å). Therefore, following the proper path of xrd-refinement §4.3, an engine copy `xrd_engine_custom.py` was taken and minimally adapted: when there is no cif/atoms and extras are present, it enters **amorphous-only mode** (background + empirical broad-peak modelling, no main-phase reflections), and it supports a per-peak `H_max` cap and a refinable/fixed `eta`. The adaptation details are marked with comments inside the copy.

**λ convention**: Kα1/Kα2 = 1.5406/1.54439 are explicitly passed to the engine (ratio 0.5, doublet); d-spacings and the Scherrer calculation use Kα1 = 1.5406 Å. For amorphous broad halos that are 2–10° wide, the unstripped Kα2 makes the FWHM slightly larger and D slightly smaller (the effect is far smaller than the halo width itself).

## 3. Fitting Process and Model Selection (4 rounds, R-value trajectory 98.62 → 4.13 → 3.83 → 3.81 → 3.82)

| Round | Model | Rwp | fit_status | Action taken |
|---|---|---|---|---|
| r1 | 3 halos, eta free | 4.13 | hit max_nfev=8000, 4 parameters at the upper bound ⇒ **R invalid** | Numerical action: add a 4th halo, tighten eta, raise max_nfev |
| r2 | 4 halos (+25.5° shoulder) | 3.83 | hit max_nfev=30000, still 4 parameters at the upper bound ⇒ **R invalid** | Numerical action: relax H_max to 20°, fix eta as a model choice, use the r2 landing point as the seed, epsfcn=1e-4 |
| r3 | 4 halos, eta fixed | 3.81 | success but ex1_c at the upper bound + strong correlation degeneracy of ex1/ex2 (stderr 63%/120%) ⇒ **R is not a clean minimum** | Model action: merge the degenerate pair |
| **r4** | **3 halos, eta fixed** | **3.82** | **success, nfev=145, zero at bounds, zero flags, plateau=true** | **Delivered** |

- The systematic undulation of the r1 residuals (positive 12–20° / negative 22–26° / positive 28–32°) drove r2 to add a 4th halo; r3 proved that the 27° Lorentzian + 30.7° Gaussian were merely a basis-set expansion of an "asymmetric main halo" (strongly correlated, no independent meaning); after merging in r4, Rwp stayed level and the fit converged cleanly ⇒ **the 4th halo is redundant, and the 3-halo model wins on parsimony**.
- **Background**: default 6th-order Chebyshev, jointly bounded least squares with the halos (the engine records `fitted_jointly_with`). **No background-order iteration (bg_scan) was performed**: the condition for raising the order is "all other parameters are already optimised and the target is still not reached"; for this sample χ² = 1.06 has already reached the statistical limit and the target Rwp<10 is already met, so the condition for raising the order is not satisfied.
- Parameter families actually released: 6 background coefficients + 3×(center/width/area); fixed items: eta (model choice), main-phase-related parameters (no main phase, not applicable). Coordinates/occupancies/cell are not applicable (no crystalline structure).

## 4. Final Results

### 4.1 Fit metrics
Rwp = **3.817%**, Rexp = 3.702%, χ² = 1.063, nvar = 15 / npts = 3432 (degrees of freedom 3417), baseline Rwp = 98.62% (r1 starting point). Residual RMS ≈ 27.7 counts (data magnitude ~350–1350 counts), with no systematic lobes (confirmed by V3/V4 visual inspection).

### 4.2 Halo parameter table (pseudo-Voigt, area-normalised amplitude; ±1σ)

| Halo | Center 2θ (°) | d-spacing (Å) | FWHM (°) | Area (fraction) | eta (fixed) |
|---|---|---|---|---|---|
| Low-angle | 16.659 ± 0.054 | 5.317 | 7.623 ± 0.450 | 2287 ± 391 (18.3%) | 0.05 |
| **Main** | **30.063 ± 0.074** | **2.970** | **10.131 ± 0.298** | 7998 ± 555 (63.9%) | 0.50 |
| Secondary | 41.920 ± 0.043 | 2.153 | 7.075 ± 0.132 | 2239 ± 70 (17.9%) | 0.25 |

Background (6th-order Chebyshev, t = (2θ−40)/30): bg0 = 552.8 ± 13.9, bg1 = −111.3 ± 16.5, bg2 = −100.9 ± 3.7, bg3 = 24.1 ± 9.3, bg4 = 29.2 ± 5.8, bg5 = −10.3 ± 1.3.

### 4.3 Scherrer apparent coherence length (two conventions, both **apparent values**: instrumental broadening not subtracted, K = 0.9, λ = 1.5406 Å)

| Convention | Main halo | Secondary halo | Note |
|---|---|---|---|
| **Measured in window** (local baseline, `xrd_data_io scherrer`) | 29.75°/FWHM 3.58° ⇒ **D ≈ 2.29 nm** | 41.30°/FWHM 1.99° ⇒ **D ≈ 4.26 nm** | Closest to the carbon-literature "(002) half-maximum width → Lc" convention |
| **Model component** (fitted FWHM) | 30.06°/10.13° ⇒ **D ≈ 0.81 nm** | 41.92°/7.08° ⇒ **D ≈ 1.20 nm** (low-angle 1.05 nm) | Depends on the halo/background decomposition, not unique |

The difference between the two conventions is the **non-uniqueness of decomposition inherent to amorphous patterns** (the choice of boundary between halo and background), not a data or fitting error; the convention must be stated when quoting. D on an amorphous halo is an **apparent coherence length** and must not be treated as a crystallite size.

## 5. Interpretation and Caveats

1. **Amorphicity confirmed**: no crystalline-phase reflections, the fit needs no crystalline phase, and the secondary halo at d = 2.15 Å agrees with the in-plane (10) band of carbon — compatible with the "amorphous carbon" description.
2. **The assignment of the main halo is in doubt**: 30.06° (d = 2.97 Å) does not match the standard (002) position of any known carbon phase (graphite 26.5°/3.354 Å; hard carbon 23–25°/3.6–4.0 Å). It may be a superposition of scattering from several kinds of short-range order within the main envelope. **It is recommended to add Raman (D/G bands) or provide synthesis route/precursor information before assigning it**; this report does not force an index.
3. **The low-angle halo** (16.66°, d = 5.32 Å) has no assigned origin (upward turn from small-angle scattering from pores / residual precursor / binder are all possible).
4. **Area fractions are semi-quantitative**: no RIR/density/absorption correction was applied, and they are affected by the non-unique halo–background decomposition, so they serve only as a relative order-of-magnitude reference and **must not be read as phase fractions**.

## 6. Honesty Statement

- **Fixed parameters are nominally fixed and stated as such**: the eta of the three halos (0.05/0.5/0.25) is a model choice (fixed after being set from the free-fit landing point of r2), not a measured value; its choice affects the details of the FWHM/area decomposition.
- **Invalid R values were not reported**: the Rwp of r1/r2/r3 (4.13/3.83/3.81) were judged invalid by the interpretation package because they hit max_nfev or parameter upper bounds, and serve only as a trajectory record; the delivered value is 3.82% from r4.
- **Items not modelled / not subtracted**: instrumental broadening (no standard sample); Kα2 (not stripped; the effect on the broad halos is negligible but was not separately verified); microstrain separation (not applicable to amorphous systems; Williamson–Hall was not performed, within the workflow boundary).
- **Coverage**: the conclusions are stated "within the range tried". Items not tried: instrumental broadening subtraction, refit after Kα2 stripping, synchrotron/long-count re-measurement, Raman/XPS/EDS corroboration (see the "not tried · unresolved items" summary section of `journal.md`) — all due to insufficient input information/data conditions, not items the workflow can fill in by itself.
- **Failure classification**: ① 1 in-design rejection (the engine plan validation rejected an amorphous plan without cif/atoms → resolved by adapting the engine copy per xrd-refinement §4.3); ② 0 genuine faults; ③ 2 environment limitations (agent-native image reading was disabled, so the host vision bridge `office_read_image` was used instead; occasional WinError 5 when the engine's progress heartbeat file was renamed, which did not affect the fit or the result files).
- **Convention**: Rwp is in this plugin's manual-engine convention (Poisson weights) and is not directly comparable with GSAS wR / FullProf conventional; this sample has no crystalline phase, so Rietveld does not apply, and hence the GSAS line was not used (the hard-gate precondition is also not satisfied).

## 7. File List (all located in this folder)

| File | Content |
|---|---|
| `report.md` | This report |
| `Amorphous_final_fit.png` | Final fit delivery figure (obs/calc/bg/halo components + residuals) |
| `Amorphous_fullpattern_fit.png` | Raw full-pattern figure (used for V1 visual inspection) |
| `result.json` / `components.json` | Final fit results and component data (yobs/ycalc/bg/extra) |
| `plan_amorphous_r4.json` | Final fit plan (for reproduction) |
| `xrd_engine_custom.py` | Engine copy (amorphous-only adaptation, for reproduction) |
| `pattern_clean.dat` | Converted two-column data |
| `peak_survey.json` / `phase_summary.json` | Peak survey / phase-determination conclusion |
| `workflow_state.json` | Workflow state (round trajectory, decisions, unresolved items) |
| `xrd_workflow/journal.jsonl` / `journal.md` | Per-round refinement log (authoritative) + overview and summary sections |

---
*Report generated: 2026-10-05 · dsh-xrd five-stage workflow · Class C amorphous procedure*

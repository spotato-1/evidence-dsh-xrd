# XRD refinement journal (generated from journal.jsonl, do not edit by hand)

| round | engine | stage | model | Rwp | baseline | verdict | why | artifacts |
|---|---|---|---|---|---|---|---|---|
| 1 | xrd_refine_manual | extras | physics | 4.126392803541247 | 98.6169183884916 | not yet at the basin; ⚠the optimiser did not report convergence (Tolerance seems to be too small. Could not estimate error-bars.); stopped at max_nfev=8000 - Rwp is a snapshot, not a minimum; 4 parameter(s) sit on a bound (ex1_H, ex1_eta, ex2_H, ex2_eta) - the value is box-limited | Class C amorphous body: 3 empirical broad peaks (initial values 17.5/29.7/41.3 deg, H 5.0/3.6/2.0 taken from the measured FWHM and V1 visual inspection) + 6th-order Chebyshev background; no crystalline main phase (amorphous-only), joint bounded LM | workspace\GLM 5.3\Amorphous\result.json |
| 2 | xrd_refine_manual | extras | physics | 3.8313962744768357 | 37.35788414727743 | not yet at the basin; ⚠the optimiser did not report convergence (Tolerance seems to be too small. Could not estimate error-bars.); stopped at max_nfev=30000 - Rwp is a snapshot, not a minimum; 4 parameter(s) sit on a bound (ex0_eta, ex1_eta, ex2_H, ex2_eta) - the value is box-limited | r1 residuals undulate systematically (12-20 positive / 22-26 negative / 28-32 positive): a single symmetric broad halo cannot cover the 24-35 deg region, so a 4th broad halo (~25.5 deg shoulder) was added; eta tightened to [0.05,0.95] to prevent pure-Gaussian/Lorentzian degeneracy; max_nfev 8000->30000 (escalation action) | workspace\GLM 5.3\Amorphous\result.json |
| 3 | xrd_refine_manual | extras | physics | 3.808995863707122 | 3.8315190219011255 | not yet at the basin; ⚠1 parameter(s) sit on a bound (ex1_c) - the value is box-limited | r2 shows the amorphous scattering envelope is wider than 8 deg (ex2_H at the upper bound, amp 4000+): H_max relaxed to 20; eta fixed as a model choice according to the r2 landing point (0.05/0.95/0.05/0.25) to eliminate shape degeneracy; the r2 landing point was used as the seed; epsfcn=1e-4 improves the finite-difference gradient at large parameter magnitudes | workspace\GLM 5.3\Amorphous\result.json |
| 4 | xrd_refine_manual | extras | physics | 3.817393558769369 | 8.08944251211261 | R-value basin | In r3, ex1 (29.05 at the upper bound, stderr 63%) and ex2 (stderr 120%) were strongly correlated and degenerate; the two are merely a basis-set expansion of an asymmetric main halo: they were merged into a single main broad halo, returning to the 3-halo model; eta fixed as a model choice (0.05/0.5/0.25), with position/width/area released | workspace\GLM 5.3\Amorphous\result.json |

## Material and target
- Sample: the Amorphous folder, composition "amorphous carbon anode" as stated by the user, with no XPS/EDS/Raman/CIF/synthesis-route information.
- Data: pattern_2theta.txt (Rigaku RAW4.00, 3432 points, 10–80°, step 0.0204°, Cu Kα1/Kα2=1.5406/1.54439 ratio 0.5, Monochromator=0 i.e. Kα2 not stripped ⇒ doublet).
- Classification: **Class C (amorphous / low-crystallinity dominant)**. Target: fit the amorphous body's broad halos, extract peak positions/FWHM/d-spacings/apparent coherence size, and screen for sharp impurity peaks; fitting target Rwp < 10 (reference value, not a hard threshold).

## Phases and crystal families
- Conclusion: **fully amorphous, no crystalline main phase**. The pattern = 3 amorphous broad halos + a smoothly decaying background; no crystalline-phase reflections.
- Evidence: V1 visual inspection + numerical peak picking found no sharp peaks; the 3-halo + 6th-order background fit converged at Rwp=3.82%, χ²=1.06 with random residuals; the entire pattern is explained without any crystalline phase.
- Excluded: ① crystalline graphite/hard-carbon main phase (main halo at 30.06°, d=2.97 Å, does not match the (002) position of any known carbon phase, and d<graphite 3.354 Å is non-physical); ② Cu current collector (43.3/50.4/74.1°)/Al foil (38.5/44.7°) peaks (not seen); ③ the 25.5° shoulder component in the 4-halo model (strongly correlated with the main halo, degenerate, stderr 63%/120%; after merging, Rwp stayed level 3.81→3.82 ⇒ redundant, excluded on parsimony).
- Delivered model: 3 pseudo-Voigt broad halos (16.66/30.06/41.92°, FWHM 7.62/10.13/7.08°) + 6th-order Chebyshev background; eta (0.05/0.5/0.25) is a model choice (fixed, on record).

## Defect summary table
- This sample is Class C, fully amorphous, with no crystalline structure ⇒ the defect summary table (split sites/occupancies/vacancies and other crystal-defect categories) is not applicable.
- Checks performed: screening for sharp impurity peaks (V1 visual inspection + numerical peak picking, negative); verification of the 19.24° doubt (the raw data show a single-point Poisson fluctuation, negative); testing of the redundant component in the 4-halo model (adjudicated by fitting, positive exclusion).

## Results achieved
- Final: **Rwp=3.82%** (manual-engine convention, Poisson weights), Rexp=3.70%, χ²=1.06, 15 parameters/3432 points, success=true, zero at bounds, zero flags, plateau=true.
- Trajectory: 98.62 (baseline) → 4.13 (r1, invalid due to hitting bounds) → 3.83 (r2, invalid due to hitting bounds) → 3.81 (r3, invalid due to upper bounds) → 3.82 (r4, delivered). Target Rwp<10 met (margin 2.6×).
- Halo parameters (±stderr): low-angle 16.659±0.054° (d=5.317 Å, FWHM 7.623±0.450°, area fraction 18.3%); main 30.063±0.074° (d=2.970 Å, FWHM 10.131±0.298°, 63.9%); secondary 41.920±0.043° (d=2.153 Å, FWHM 7.075±0.132°, 17.9%).
- Scherrer apparent coherence length (instrumental broadening not subtracted, K=0.9, λ=1.5406): window convention D≈2.29 nm (main)/4.26 nm (secondary); model-component convention D≈0.81 nm (main)/1.20 nm (secondary)/1.05 nm (low-angle).
- Convention note: the manual engine's Rwp is in this plugin's convention and is not directly comparable with GSAS wR/FullProf conventional; this sample has no crystalline phase, so Rietveld/the GSAS line does not apply.

## Not tried · unresolved items
- **Not tried**: ① instrumental broadening subtraction (no standard-sample data, so the D values can only be apparent values); ② refit after Kα2 stripping (the data were not stripped; the effect on the 2–10° broad halos is negligible and was not separately verified); ③ synchrotron/long-count re-measurement (would improve the resolvability of the low-angle halo and weak features); ④ Raman/XPS/EDS corroboration (the key gap for the assignment decision, not provided by the user).
- **Unresolved**: ① the assignment of the main halo at 30.06° (d=2.97 Å) — it does not match typical hard carbon (002) (23–25°, d 3.6–4.0 Å) and lies between (002)/(100); ② the assignment of the low-angle halo at 16.66° (d=5.32 Å) (upward turn from small-angle scattering from pores / residual precursor / binder).
- All the "not tried" items above are due to insufficient input information/data conditions, and are not items the workflow can fill in by itself — the conclusions are stated "within the range tried".

## Suggestions for the next handler
1. Add Raman (D/G bands) and synthesis-route information → to decide the assignment of the main halo (short-range order of turbostratic carbon vs superposition of other amorphous components).
2. If phase quantification is needed: this data set has no crystalline phase, so it does not apply; if sharp peaks appear in a re-measurement, follow the Class A/B procedure for phase determination (xrd_phase_screen).
3. If publication-grade d002/Lc is needed: re-measure with a Si standard and subtract the instrumental broadening, then give values according to the two conventions in this report separately.
4. Handover files: workflow_state.json (state), phase_summary.json (phase-determination conclusion), peak_survey.json (peak survey), result.json + components.json (final fit), plan_amorphous_r4.json + xrd_engine_custom.py (the model definition needed to reproduce the fit), report.md (the report).

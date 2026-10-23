# XRD Data Processing Report for the Amorphous Carbon Anode

**Sample**: amorphous carbon anode (stated by the user) **Directory**: `Amorphous/` **Date**: 2026-10-09
**Workflow**: dsh-xrd plugin five-stage workflow (①identification → ②initial screening → ③routing → ④fitting → ⑤report), material category **C (amorphous-dominated)**
**One-sentence conclusion**: the data are consistent with "amorphous carbon" — the full pattern has no sharp Bragg peak at all (**no crystalline impurity phase detected**), the diffuse scattering is described by 3 empirical broad humps, the fit reaches the statistical limit (**Rwp=3.81%, χ²=1.06**; the reference target of <≈10% **has been achieved**), and the apparent coherence domain is **~1–2 nm** (no long-range crystalline order).

---

## 1. Data and measurement facts (stage ② initial screening)

| Item | Value | Source |
|---|---|---|
| Data file | `pattern_2theta.txt` (actually Rigaku **ASCII RAW4.00**: `;RAW4.00` header + `[Data]` block) | format sniffing |
| Archived file | `pattern.raw` (Rigaku **binary RAW1.01**, not readable by the plugin tools, not used for the calculations) | format sniffing |
| Range / points / step | 10.000–79.997°, 3432 points, 0.0204012° | `xrd_data_io read` |
| Tube | Cu (Anode=Cu), 40 kV / 40 mA | RAW header |
| **λ (explicit reconciliation)** | **Kα1=1.5406 Å, Kα2=1.54439 Å, ratio=0.5**; `Monochromator=0` ⇒ **Kα2 not stripped** (the `ActuallyUsedLambda=1.5418` in the header is the Kα average value and **must not** be used as monochromatic Kα1) | RAW header `[HardwareConfiguration]`; authority order = measured data > other inputs |
| Measurement date | 2026-09-23 11:50 | RAW header |
| Converted product | `pattern.txt` (two-column format, used by all downstream steps) | `xrd_data_io convert` |

The λ doublet was **passed explicitly** in all 4 fitting rounds (plan `lambda` block, the engine log marks it `[explicit]`); the Scherrer calculation uses the single value λ=1.5406 (the effect of not stripping Kα2 is declared in the protocol — for broad humps with FWHM≈3–12°, the doublet splitting of ~0.1° is negligible).

## 2. Interpretation of the line shape (V1 full-pattern image reading + numerical evidence)

- The full pattern shows only **broad diffuse humps**, with no sharp peak whatsoever; at high angles it decays smoothly to ~370 counts.
- Quantitative (`xrd_data_io fwhm`, raw-window protocol): main broad hump **29.75°, FWHM 4.48°**; second broad hump **41.30°, FWHM 3.19°**; the binned profile additionally shows a low-angle rise from 10→16° (porosity-related scattering).
- **Category-C routing**: no sharp impurity ⇒ the workflow skips phase identification / two-phase searching and models the main broad humps empirically; the peak-cutting (cut) gate **was not triggered and was not executed** (there is no current-collector / artifact peak that needs to be removed).

## 3. Fitting process (stage ④, 4 rounds, criterion = monotonic decrease of R until the plateau)

| Round | Model | Rwp% | Interpretation |
|---|---|---|---|
| Baseline | starting parameters (not fitted) | 95.30 | baseline |
| 1 | 2 empirical broad peaks (standard engine) + 6th-order Chebyshev background | 6.174 | clean convergence, but the residual bins show systematic structure (±190 counts) ⇒ **model-related** treatment |
| 2 | same as above, with the **AI-edited engine copy** releasing the peak-shape degrees of freedom (H upper bound 4→15°, η refinable) | 4.312 | R drops by 1.86; both η pinned at the artificial inward-shifted bound ⇒ numerical treatment (the bound is relaxed to the physical [0,1]) |
| 3 | **+ low-angle broad component** (the residual at 14–18° is still +31/+41) | 3.808 | R drops by 0.50; the systematic residual bins are **all cleared**, χ²=1.06 reaches the statistical limit |
| 4 | same as round 3, with the endpoint η frozen (delivery round) | **3.808** | **R plateau**: plateau=true, flags=[], covariance/esd complete |

- Engine: `xrd_refine_manual` (bounded LM, Poisson weights), **AI-edited copy** `xrd_engine_custom.py` (both edits are commented: the extras H upper bound 4.0→15.0; η becomes a refinable parameter ex*_e∈[0,1]). Reason for the edits: the amorphous broad humps have FWHM up to 4.5–12°, and the standard engine's H≤4.0 upper bound and fixed η, designed for sharp impurity peaks, cannot express this material's line shape (demonstrated by the Round 1 residual).
- Placeholder main phase: the engine interface requires a main phase to exist, so a nominal C (cubic a=10 Å) is given with **scale fixed at 0** — it contributes nothing to the line shape, it is pure scaffolding, and this is disclosed truthfully.
- Background: **6th-order default, not iterated** (bg_scan not enabled). Reason disclosed (§6.8): χ²≈1.06 has already reached the statistical limit (Rwp cannot go below Rexp=3.70 unless the noise is overfitted) and the target has been achieved; the background is refined jointly with the other parameters in the same bounded least-squares (the engine's default path).
- Not passed to GSAS-II / FullProf: an amorphous material has **no crystal structure model**, so Rietveld does not apply; per the plugin's specification, the `components` source of `xrd_export_cif` is the output protocol for "data that cannot be Rietveld-refined" (the figure of this report is produced by it).

## 4. Final model parameters (Round 4, esd from the full covariance)

**Three empirical broad humps** (area-normalized pseudo-Voigt, `amp` = integrated area in counts·deg):

| Component | Center 2θ (°) | FWHM (°) | Area | η | d (Å) | Loose assignment |
|---|---|---|---|---|---|---|
| ex2 | 16.506 ± 0.050 | 7.55 ± 0.33 | 2358 ± 278 | 0 (pure Gaussian, frozen) | **5.366** | low-angle porosity / expanded interlayer correlation scattering (typical of amorphous carbon) |
| ex0 | 29.942 ± 0.061 | 11.84 ± 0.34 | 13926 ± 875 | 1.0 (pure Lorentzian, frozen) | **2.982** | main diffuse band: interlayer-type correlation of strongly disordered sp2 clusters; d smaller than graphite's 3.35 Å ⇒ strongly turbostratic / bent stacking, **not graphite long-range order** |
| ex1 | 42.132 ± 0.041 | 6.80 ± 0.19 | 2344 ± 274 | 0.574 ± 0.142 | **2.143** | in-plane (100)-type C–C correlation (graphite 2.13 Å, assignment robust) |

Background: Chebyshev 6th order (center 45, halfwidth 35): bg0=469.36±13.52, bg1=−92.21±15.34, bg2=−59.03±5.76, bg3=21.67±7.62, bg4=31.95±5.55, bg5=−20.56±2.91.

**Disclosure of the endpoint η freeze**: after being released for refinement, the η of ex0/ex1 runs to the physical endpoint of the PV family (pure Lorentzian / pure Gaussian) — the endpoint values are a **model-family constraint**, not measured values; the delivery round freezes them in order to obtain a clean esd, and Rwp agrees with the pre-freeze value to 10⁻⁷.

**Band area fractions** (semi-quantitative protocol: RIR/density/absorption are not divided out, this is only the area apportionment of the diffuse scattering, **not a phase fraction**): ex0 74.8% / ex1 12.6% / ex2 12.7%.
**Crystallinity cannot be given**: there is no crystalline phase reference within the pattern, and all scattering is diffuse.

## 5. Scherrer apparent coherence length (the protocol must be restated together with the numbers)

**Protocol as directly measured by the tool** (raw-pattern window FWHM; `xrd_data_io scherrer`):

| Broad hump | 2θ | FWHM | D (apparent) |
|---|---|---|---|
| Main broad hump | 29.75° | 4.48° | **1.84 nm** |
| Second broad hump | 41.30° | 3.19° | **2.66 nm** |

Protocol declaration: **instrumental broadening not subtracted ⇒ apparent value (corrected:false)**; K=0.9, λ=1.5406 Å, Kα2 not stripped; for an amorphous broad hump, D is the **apparent coherence length** of that hump, not a crystallite size; no microstrain separation was performed (Williamson-Hall is a deliberate boundary of the plugin, and it is meaningless for an amorphous material).

**Model dependence disclosed**: converted from the widths of the Round 4 fitted components, D is 0.69–1.25 nm (caused by ex0 serving also as the diffuse base in the empirical decomposition and by the different width protocol). Both protocols jointly support a robust conclusion: **coherence domain of order ~1–2 nm (roughly 2–6 graphene layers), no long-range crystalline order**.

## 6. Impurity screening conclusion (step 2 of the category-C recipe)

- Final residual rms=27.7 counts ≈ Poisson noise (√mean counts); the **z scan (residual/σ) has 0 points >4σ** (maximum |z|≈3.5, a normal tail for 3432 points).
- The residual file `residual_round4.txt` was picked by `xrd_phase_screen peaks`: all 40 "peaks" are 12–28 counts ≈ noise level, none is sharp, and there is no angular clustering.
- **Conclusion: no crystalline impurity phase detected** (including the Cu/Al current-collector foil peaks: 43.3/50.4/74.1°, 38.5/44.7/65.1/78.2° all show no signal). Detection-limit statement: diffuse / trace crystalline contributions weaker than ~1σ noise are not visible in this data; to check for <1% trace crystalline phases, a re-measurement with longer counting is recommended.

## 7. R values and statement of target achievement

- **Protocol**: manual-engine Rwp (Poisson-weighted bounded LM) — this sample has no FullProf/GSAS numbers, so no cross-protocol comparison exists.
- **Final**: Rwp = **3.808%**, Rexp = 3.702%, χ² = **1.058**, GOF ≈ 1.03 (nvar=16, npts=3432); baseline 95.30%.
- **Target judgement**: the reference target "Rwp < ≈10%" **has been achieved** (non-exhaustion statement: the background order was not escalated — for the reason see the disclosure in §3; the model dimensionality has been exhausted within the statistical limit, and the residual has no systematic structure).
- fit_status for the delivery round is entirely clean (success / no max_nfev / no bound hitting / covariance complete), r_plateau=true.

## 8. List of deliverables (all in this directory)

| File | Description |
|---|---|
| `report.md` | this report |
| `round4_final_fit.png` | final fit figure (obs/calc/bg/residual, V3/V4 image reading passed) |
| `result_round4_final.json` | final parameters + esd + interpretation package (authoritative numbers) |
| `components_round4_final.json` | x/yobs/ycalc/bg/component curves |
| `plan_round4_final.json` | complete plan of the delivery round (reproducible) |
| `xrd_engine_custom.py` | AI-edited engine copy (required for reproduction, both edits commented) |
| `xrd_workflow/journal.jsonl` + `journal.md` | round-by-round authoritative log + quick view (including the summary section) |
| `workflow_state.json` | workflow state (phase 5, rounds 1–4) |
| `pattern.txt` | two-column-format converted data |
| `residual_round4.txt` | final residual (evidence for impurity screening) |
| Intermediate products | `plan_round1-3.json`, `pattern_full_fit.png` (V1), `round1_fit_fit.png`, `data_io_*/phase_screen_*/export_*` temporary JSON, `.xrd-progress*`, `.mplcache/` |

## 9. Open items and recommendations (not blocking this delivery)

1. **Complementary characterization**: Raman (D/G ratio, sp2/sp3) compared against the band widths/areas of this fit is the standard complement for amorphous carbon; if evidence for porosity and surface chemistry is needed: TEM/specific surface area/XPS.
2. **Deeper investigation of the main band d=2.98 Å**: it is smaller than the typical hard-carbon (002) (3.3–3.6 Å) — if materials science requires distinguishing "strongly bent graphene clusters / sp3-rich a-C / mixed phases", XRD alone cannot decide it, and Raman+TEM is recommended.
3. **Synthesis-route information** is missing, which limits the depth of the physical interpretation of ex2 (porosity component 12.7%).
4. For cross-sample comparison, **the same decomposition protocol must be fixed** (number of components, shape family, background order) — an empirical broad-hump decomposition carries an inherent model dependence.

# XRD Data Processing Report for Amorphous Carbon Anode

## 1. Sample and Data

| Item | Value |
|---|---|
| Sample | Amorphous carbon anode (composition given by the user) |
| Data file | `pattern_2theta.txt` (Rigaku RAW text export `;RAW4.00`; `pattern.raw` in the same directory is the binary raw file of the same measurement) |
| 2θ range | 10.000 – 79.997° |
| Step size | 0.0204° |
| Number of data points | 3432 |
| Instrument | Rigaku, Locked Coupled, 40 kV / 40 mA |

### λ (wavelength) reconciliation (mandatory at the data entry point)

Read field by field from the Rigaku RAW header:

| Header field | Value |
|---|---|
| `Anode` | Cu |
| `Alpha1` | 1.5406 |
| `Alpha2` | 1.54439 |
| `AlphaRatio` | 0.5 |
| `Monochromator` | 0 (→ Kα2 **not stripped**) |
| `ActuallyUsedLambda` | 1.5418 (Kα average, **not** Kα1) |

**Determination**: laboratory Cu tube → **doublet**; `Monochromator=0` → Kα2 not stripped.
Downstream, **Cu Kα1 1.5406 / Kα2 1.54439 / ratio 0.5** is passed explicitly (authority order: measured data header > engine default).
The Scherrer formula uses **Kα1 = 1.5406 Å** (the tool echoes the caveat that "unstripped Kα2 makes the FWHM too large and D too small").

## 2. Material-type determination and workflow

- **Material type = C (amorphous / low-crystallinity dominated)**. The full pattern has no sharp Bragg diffraction peaks, only broad humps → no Rietveld structure refinement is performed,
  but the "empirical fit of amorphous broad humps + Scherrer coherence size" route is taken (the class-C recipe of xrd-preflight stage 3).
- No sharp impurity peaks → no phase identification is needed, and the main broad peaks are fitted directly.

## 3. Full-pattern morphology (visual inspection V1)

The full pattern shows **only two broad humps** and no sharp diffraction peaks whatsoever, consistent with the characteristics of amorphous carbon:

1. **Main broad peak (002)**: 2θ ≈ **29.75°**, the strongest (≈1433 counts);
2. **Broad shoulder (10)/(100)**: 2θ ≈ **41.3°**, weaker (≈977 counts);
3. The background at low angle (10–16°) rises from ~671 to ~900 (air scattering/Compton/sample fluorescence, etc.), and decays monotonically to ~366 at high angle.

## 4. Peak positions, FWHM and Scherrer coherence size

| Broad peak | 2θ (°) | d (Å) | FWHM (°) | Coherence size D (nm, apparent) |
|---|---|---|---|---|
| (002) main broad peak | 29.75 | 3.00 | 2.26 | 3.63 |
| (10)/(100) broad shoulder | 41.30 | 2.18 | 3.20 | 2.66 |

Caveat statement (must be relayed together with the numbers):
- **D is an apparent value (APPARENT)**: instrumental broadening is not subtracted. But for amorphous broad humps of the order of 2–3°, the instrumental broadening (~0.05°) is negligible.
- **D is a coherence length, not a crystallite size**: for an amorphous broad hump it is the apparent coherence length of that hump.
- **No strain separation was performed** (Williamson-Hall is deliberately left out of scope), and Kα2 is not stripped (which makes the FWHM slightly too large and D slightly too small).
- Scherrer formula: D = K·λ/(β·cosθ), K = 0.9, λ = 1.5406 Å.

## 5. Empirical fit of the amorphous broad humps

Model: `xrd_refine_manual` extras (2 empirical broad peaks) + 6th-order Chebyshev background; the main phase uses a nominal single C atom placeholder
(lattice a=2.5 Å) and its **phase scale is fixed at 0** (purely amorphous, no crystalline main phase), so that the background + broad peaks carry all the intensity.

| Quantity | Value |
|---|---|
| Rwp | **6.04 %** |
| baseline Rwp | 97.62 % |
| Rexp | 3.70 % |
| χ² | 2.66 |

Fit parameters (extras):

| Broad peak | Center 2θ (°) | d (Å) | Area amp | H (FWHM) |
|---|---|---|---|---|
| ex0(002) | 30.32 | 2.94 | 2035 | **4.0 (upper bound)** |
| ex1(10) | 42.03 | 2.15 | 872 | **4.0 (upper bound)** |

**Fit-boundary statement (reported truthfully)**:
- The **H (FWHM) of both broad peaks is pinned by the engine's hard upper limit of 4.0°** (`fit_status`: 2 parameters at the bound), so H is a lower bound of "≥4°",
  not a measured value; this R value is not a strict minimum. The attempt to relax the H upper limit (an edited copy of the engine) was not completed because of an execution timeout.
- But this **does not affect** the peak-position and coherence-size conclusions: after subtracting the 6th-order background, the measured FWHM of the main broad peak is still **2.26°**
  (consistent with `xrd_data_io fwhm`), and the Scherrer size of 3.6 nm is the correct value under that criterion.
- The residual panel shows **systematic undulation (±150–200 counts)** in the 10–50° broad-peak region — this comes from the fact that "a single pseudo-Voigt + H at the upper bound"
  cannot fully express the asymmetric line shape of the amorphous (002); this is a model limitation, not a data anomaly; there is no unfitted sharp impurity peak.

## 6. Conclusions

1. The sample is **amorphous carbon**, and the XRD pattern shows the typical double broad hump: main broad peak 2θ=29.75° (d=3.00 Å) + broad shoulder 2θ=41.3° (d=2.18 Å).
2. **Apparent coherence size**: D(002)≈ **3.6 nm**, D(10)≈ **2.7 nm**.
3. Empirical fit Rwp=**6.04%** (χ²=2.66), with no crystalline impurity phase; the fact that the broad-peak H is pinned by the engine's 4° upper limit is a model limitation, already disclosed in Section 5.
4. **Note**: d(002)=3.00 Å is smaller than that of typical hard carbon (3.6–4.0 Å) and even than that of graphite (3.35 Å), tending towards a more condensed/graphite-like short-range order;
   without an internal standard, a 2θ calibration offset cannot be ruled out, and confirmation in combination with Raman / interlayer-spacing measurements is recommended.

## 7. List of products (located in the data folder)

- `amorphous_carbon_fit.png` — full-pattern figure (raw data)
- `amorphous_carbon_fit_fit.png` — fit figure (observed/calculated/background/residual)
- `result.json` / `components.json` — fit results and component curves (fit record)
- `pattern_twocol.txt` — cleaned two-column data
- `plan_amorphous.json` — fit plan
- `workflow_state.json` / `xrd_workflow/journal.jsonl` / `xrd_workflow/journal.md` — workflow state and log
- `report.md` — this report

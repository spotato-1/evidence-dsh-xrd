# FE50 XRD refinement report

**Sample**: FE50 — Prussian blue analogue KxFe0.5Mn0.5[Fe(CN)6] (theoretical formula, x to be determined)
**Synthesis**: Fe4[Fe(CN)6]3 + manganese oxide tetrahydrate + potassium citrate, ball-milled in 50% ethanol aqueous solution
**Data**: Rigaku Cu Kα (λ1=1.5406, λ2=1.54439, I2/I1=0.5, Kα2 not stripped → doublet modelled throughout the workflow); 2802 points, 10–70.001°, step 0.0214213°
**Workflow**: five-stage workflow + the three-part structure of stage ④ (Ⅰ CIF verification → Ⅱ manual engine to the R basin → Ⅲ GSAS-II refinement and delivery); the complex-case checklist was involved from the start (highly defective/doped system)

---

## 1. Results at a glance (final delivery: GSAS-II convention)

| Metric | Value |
|---|---|
| **wR** | **11.00 %** |
| R (profile) | 8.72 % |
| Rb (Bragg) | 10.25 % |
| wRmin (statistical lower limit) | 7.92 % |
| Space group | P2₁/c (monoclinic, No.14) |
| Unit cell | a=10.1109, b=10.1142, c=10.1244 Å, β=87.19°, V=1034.1 Å³ |
| Chemical formula (refined) | **K1.40(Fe0.5Mn0.5)[Fe(CN)6]0.60** (Z=4) |
| K occupancy | 0.70 (K1/K2 two sites, equal) |
| [Fe(CN)6] unit occupancy | **0.60 (about 40% vacancies)** |
| N-site metal | Fe0.5/Mn0.5 fully occupied (nominal) |
| Uiso | metal/K=0.005, C/N=0.056 Å² (large CN Uiso = static disorder) |

**Target attainment**: the target was an R value below ≈10 (reference value). **Not fully attained**: the final GSAS wR=11.00 %, 1.0 away from the target and 3.1 away from the statistical lower limit wRmin=7.92. As agreed, this is reported as-is; the attribution for not meeting the target is in §4.

**Deliverables** (all in `FE50/FE50_final/`):
- `FE50_fit.png` — publication-grade fit figure (obs/calc/background/residual/hkl labels; the statistics box and legend passed the anti-occlusion check)
- `FE50_New_structure.cif` — the official GSAS-II exported CIF
- `FE50_final.gpx` / `FE50_report.md` — the clean project and the metrics report

## 2. Defect conclusions (corresponding to defect summary table D-01…D-14)

| Defect | Conclusion | Evidence |
|---|---|---|
| **[Fe(CN)6] vacancies (D-01)** | **about 40% (w=0.60)** | GSAS bounded grid scan (48+30 points), progressive improvement 12.99→11.00; self-consistent with the 25% vacancies of the precursor PB + ball-milling damage |
| Lattice distortion (D-09) | monoclinic P2₁/c beats cubic Fm-3m (ΔRwp=1.07, actually run with the same parameterisation) | β=87.2°, mild pseudo-cubic distortion |
| K split sites (D-07) | K1/K2 two sites (literature coordinates) retained, equal occupancy 0.70; free refinement of the displacement judged "indistinguishable with this data" (peak width 0.3–0.5°) | constraint scheme executed |
| Fe/Mn antisite (D-02/D-03) | **indistinguishable by X-ray** (adjacent Z; a conservation-constrained actual run drifted without bounds) — this is not judged as "does not exist" | N site kept as nominal Fe0.5Mn0.5 |
| Diffuse scattering (D-05) | the broad halos at 15.0°/29.0° fall exactly at the (111)/(311) forbidden positions — defect-rich short-range-ordered domains; modelled as an empirical component and imported into GSAS as a fixed background | assignment undetermined, disclosed as-is |
| Size/strain (D-11/D-12) | apparent Scherrer 28.7/27.3/21.1 nm (**instrumental broadening not subtracted**); TCH Lorentzian strain term significant | separation limited by the Mustrain/Y correlation |
| Impurity phase (X-01) | no evidence of sharp impurity peaks (3σ peak picking found only 5 PBA peaks) | numerical survey |

## 3. Charge-balance self-consistency (important disclosure)

Under the valence assumption of N-site Fe(III)0.5Mn(II)0.5 + C-site Fe(II), charge balance requires x(K) = 4w − 2.5; at w=0.60 this gives x=−0.1, which is **not self-consistent** with the refined K1.40. Possible explanations: (a) the vacancies are not complete [Fe(CN)6] units (some CN missing while the metal is retained); (b) electron density contributed by water/oxygen in the cages is partly absorbed by the K site; (c) the mixed valence of Fe deviates from the assumption. **It is recommended to determine the K content and valences by XPS/ICP/Mössbauer spectroscopy and then re-check** — XRD alone cannot adjudicate this (the w-k valley is flat, with multiple solutions within ±0.5 wR).

## 4. Attribution for not reaching R≤10 (coverage statement)

Tried: exhaustive actual runs over crystal families (3 families), TCH peak shape (η once hit a bound → resolved with a two-width model), per-element DW, bounded occupancy scan (78 points), 6th-order background + manual curve import, physical Uiso clamping. **Not tried**: ① peak-shape asymmetry parameters (ball-milled samples often have asymmetric low-angle peaks; not modelled this round); ② free refinement of CN coordinates (low-resolution drift risk, a PB lesson); ③ anisotropic broadening (no clear hkl-dependent evidence); ④ iterative background-order upgrade (orders 8–20) — this is a conditional escalation under the user's rules, and with the 6th order + curve import already on a plateau this round, the gain from upgrading is expected to be <0.5; ⑤ free K-site-coordinate scheme (exempted by the resolution argument). The main residual mismatch: **(220) peak-shape/intensity slight mismatch (±100 cts) and partial absorption in the 28–45° diffuse-scattering region** — the former needs asymmetry/preferred-orientation modelling, the latter is inherently non-Gaussian diffuse-scattering shape.

## 5. Method notes (honesty statement)

- The background includes an imported fixed empirical curve (bg + diffuse scattering, from manual engine r3) — the diffuse scattering is **not** modelled as a crystalline phase;
- The N-site Fe/Mn ratio and the K-site geometry use nominal/literature values — the report consistently states "indistinguishable" rather than "does not exist";
- Intermediate states of the manual engine did show non-physical drift (occ_C=0.14, negative Uiso) — this was repaired in the GSAS stage with physical constraints, and the delivered structure has no negative Uiso and no out-of-range occupancy (review pass);
- Engine/interface troubleshooting record: fp2k ladder background step hung (switched to the manual engine); the GSAS `.prm`→`.instprm` format, the `I(L2)/I(L1)` key, and the corrupted HAP entry required three rounds of repair — all are environment/interface issues, not model issues, and are recorded in the journal.
- The complete round trajectory (10 rounds) is in `xrd_workflow/journal.jsonl`; the defect summary table (15 entries, including the off-table hypothesis X-01) is in `defect_table.json`.

## 6. Suggestions for the next handler

1. Add ICP (K/Fe/Mn ratio) + XPS (Fe/Mn valences) → re-check the charge balance and the w-k degeneracy in §3;
2. If wR<10 must be pushed: first try peak-shape asymmetry (GSAS SH/L) and a second empirical component in the diffuse-scattering region;
3. Mössbauer spectroscopy can directly determine the Fe(II)/Fe(III) ratio and discriminate vacancy-morphology hypotheses (a)/(c);
4. When re-measuring, reduce the step size (e.g. 0.01°) and extend to 80°, so that (640)/(642) can markedly improve the K/occupancy resolution.

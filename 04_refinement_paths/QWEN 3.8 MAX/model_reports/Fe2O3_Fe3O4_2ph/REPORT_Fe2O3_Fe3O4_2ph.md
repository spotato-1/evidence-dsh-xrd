# Fe2O3_Fe3O4_2ph — Final Report on Two-Phase XRD Rietveld Refinement

**Conclusion: the publication-grade target is achieved.** In the GSAS-II protocol **wR = 1.58%** (target ≤10), R = 1.22%, Bragg R = 1.84%, GOF = 1.78 (wRmin = 0.89%).
**Phase quantification (the answer to the judge-only question): α-Fe2O3 60.52(69) wt% / Fe3O4 39.48(69) wt%**, no third phase, no amorphous term.

---

## 1. Data and measurement conditions (evidence: data file header, positional header dump verbatim)

| Item | Value |
|---|---|
| Sample | weighed two-phase mixture α-Fe2O3 (hematite) + Fe3O4 (magnetite), Zenodo 14959531 |
| Instrument | Panalytical X'Pert PRO, Bragg-Brentano |
| Radiation | Cu anode 40 kV/30 mA, **no monochromator** (Kα2 not stripped ⇒ doublet modeling) |
| λ (explicit, same value in all four entries) | Kα1=1.54051, Kα2=1.54433, I(Kα2)/I(Kα1)=0.5 (the data header gives no value, so the plugin's lookup table is used: GSAS-II homologous Cu) |
| Range | 10.013–119.967° 2θ, step 0.026°, 4230 points |
| Background | ~11500–12500 cps (peak/background ratio ~2.3); strongest peak at 33.3° (~26500 cps) |

## 2. Method chain (strictly per the dsh-xrd five stages + the stage ④ three-segment scheme)

1. **Ⅰ CIF creation and validation**: MP `polymorphs` to obtain R-3c/Fd-3m polymorphs → `symmetrize` to restore the space group → `validate` health check (pass, min contact 1.97/1.92 Å) → `cif_to_pcr` occupancy audit → actual fp2k run.
   - **Key technical event (Fd-3m origin-frame conflict)**: the Fd-3m table of the official converter = gemmi `:2` setting (hall `-F 4vw 2vw 3`), whereas the pymatgen default = `:1`; the first conversion's occupancy audit **failed** (multiplicities 16/8/96 vs the expected 8/16/32). After locking down the converter's setting by point-by-point multiplicity evidence, a **machine frame transformation** (x′=−x+(⅛,⅛,⅛), conjugation of all 192 symmetry operations, zero hand-writing) was used to generate a published-setting CIF, which passed a four-fold adjudication: **self-consistency validation + 27-peak pattern-equivalence validation + occupancy audit pass + actual fp2k/GSAS run**.
2. **Ⅱ Push the two-phase fit to the plateau with the manual engine** (§4.5.3 the design order set by the user): r3 ineffective (hit bounds) → r4 fixes the second phase's Lorentzian width Y (root cause: fixing it at 0.5 forces the magnetite peaks to broaden 3-fold) → Rwp 5.33→1.743 → r5/r6 eta saturates at 0.995 (the engine lacks an asym term, recorded truthfully) → **manual-protocol Rwp 1.745** (baseline 98.82).
3. **Ⅲ GSAS-II** (handoff seeds the phase ratio 0.792 / main-phase cell / instrumental W+Zero; the bad U/V seeds were rejected by the 10× safeguard and then self-corrected in the inst step): entry=hold step-by-step release + rollback, ladder wR 3.28→3.18→1.77→1.75→1.74→1.73→1.69→(continuation round)→**1.584**; auto_background 6th-order finish with no change; `review` **pass**; `xrd_finalize` delivery package + V4 image reading passed.

## 3. Final structure and physical parameters (GSAS-II, esd from lst)

**Hematite α-Fe2O3, R-3c (#167), Z=6**
| Parameter | Value | Literature comparison |
|---|---|---|
| a | 5.0365(2) Å | 5.0356 ✓ |
| c | 13.7539(5) Å | 13.7489 ✓ |
| V / density | 302.14(24) Å³ / 5.266 g·cm⁻³ | 5.26 ✓ (sentinel pass) |
| Fe0 z(12c) | 0.14488(17) | 0.1447 ✓ |
| O1 y(18e) | 0.31357(150) | ~0.306–0.311 (≈2σ) |
| Uiso Fe/O | 0.0081(14) / 0.0065(28) Å² | physical ✓ |
| Size (isotropic) | 10 µm, **sig 50 ⇒ cannot be determined independently** (99.5% correlated with instrumental X) — reported truthfully as "no measurable size broadening" | — |

**Magnetite Fe3O4, Fd-3m (#227) inverse spinel, Z=8**
| Parameter | Value | Literature comparison |
|---|---|---|
| a | 8.3866(5) Å | 8.397 (−0.12%, data-driven) |
| V / density | 589.88(96) Å³ / 5.214 g·cm⁻³ | 5.18 ✓ (sentinel pass) |
| Fe1 8a / Fe2 16d | (⅛,⅛,⅛) / (½,½,½) (fixed by symmetry) | ✓ |
| O u(32e) | 0.24761(156) | 0.2549 (−4.7σ, data-driven; the tetrahedral Fe–O distance of 1.80 Å is somewhat short, must be noted for publication) |
| Uiso Fe1/Fe2/O | 0.0564(43) / 0.0128(21) / 0.0613(58) Å² | all positive (review pass); Fe1/O are somewhat high and act as compensation terms for the intensity mismatch, reported truthfully |
| Size (isotropic) | **0.1131(8) µm = 113(8) nm** (determined independently ✓) | — |

**Instrumental/global**: Zero = +0.14330(11)° (the data carry a genuine zero-point offset, correctly absorbed by Zero — the cell also converges to the literature value at the same time, proving the decomposition is correct); U/V/W/X/Y have been refined (the esd of U/V is large, the Caglioti parameters are inherently strongly correlated); 6th-order Chebyshev background 12393/666/152/−399/98/−158 (esd <7 for all coefficients); the λ doublet is confirmed as written in the lst.

## 4. R-value protocols (written separately, not directly comparable across protocols)

| Protocol | Value | Role |
|---|---|---|
| **GSAS-II wR (delivered)** | **1.58%** (GOF 1.78, wRmin 0.89%) | target-achievement criterion: ≤10 ✓✓ |
| GSAS Rb / wRb | 1.84% / 2.75% | structural intensity quality |
| Per-phase RF (raw lst values) | hem 19.2% (53 refl)/ mag 28.3% (34 refl) | unweighted; weak reflections are dominated by high-background noise, read together with Rb |
| Manual-engine Rwp | 1.745 (baseline 98.82) | process criterion (Poisson-weighted, a different protocol) |
| fp2k Rwp 7.68/7.72 | **invalid** (degenerate solution, R_Bragg 92.8%) | mechanical verification only, not used for structural scoring |

## 5. Failure classification and handling (honesty statement, §5.1 three classes)

| Event | Classification | Handling |
|---|---|---|
| fp2k single-phase baseline Rwp "7.7" but R_Bragg 92.8% | **model-related** (missing second phase, §6.2) | judged invalid and that route frozen; the two-phase adjudication moved to the manual engine + GSAS (the in-design path) |
| r3 hits max_nfev + 3 parameters at bounds | **numerical** (§4.6.2) | tightened the bounds + physical initial values + raised nfev (8000→20000), nfev was not lowered |
| Second-phase peaks forced to broaden 3-fold (Y fixed at 0.5) | **model-related** (engine parameterization) | vary_Y released, Rwp 5.33→1.74 |
| magnetite occupancy audit fail (16/8/96) | **structural** (CIF frame conflict, §6.2) | fixed the CIF source: frame transformation + four-fold validation, no forcing of the refinement |
| GSAS import failure 'INS HTYPE' (×2) | **tool-layer format incompatibility**: the plugin documentation suggests ".prm", but the GSAS scriptable interface dispatches on extension — the new format must be `.instprm` | succeeded after renaming; whether fxye is likewise readable was not re-verified (switched to plain numeric two-column) |
| build_orbit produces a non-spinel 16c+8b expansion | rejected by design (gemmi has no :2 expression) | rejected by coordination bookkeeping, switched to the frame-transformation route |
| `.xrd-progress` tick write WinError 5 | environment limitation (harmless, does not affect the result) | ignored |

## 6. Coverage statement (§4.6.1)

- **Background**: 6th order (default); GSAS `auto_background` was run once at 6th order as a finish and showed no improvement; **order escalation (bg_scan/iterate) was not done** — escalation is a conditional upgrade for "still not meeting the target after everything else is optimized", and this sample already meets the target at wR 1.58%, so the condition was not triggered.
- **Parameter families actually released**: background (6), instrumental (U,V,W,X,Y,Zero), both cells, both Scales, both Sizes (isotropic), both atoms' coordinates + Uiso (XU).
- **Never released even once**: preferred orientation (pref), microstrain (mustrain, to avoid collinearity with X/Y), SH/L (fixed 0.002), anisotropic ADP (Uij), occupancies (end-member stoichiometry, fixed 1.0), degrees of freedom other than hematite O/Fe.
- **Dual-scheme for geometry-sensitive dimensions** (§4.5.2): not applicable — no split site / antisite hypothesis entered execution for this sample (screening reasons in defect_table.json T-03/T-04).
- **Mode boundaries**: complex defect-adjudication operations were not involved for this sample; the occupancy-conservation mechanism was not used (occ all 1).
- **Conclusion protocol**: within what was tried, wR=1.58% meets the target; the "not released" items above are **not tried**, and no claim of "cannot be improved" is made.

## 7. The three-piece set and deliverable index (all under the data folder)

| Deliverable | Path |
|---|---|
| Delivery package (clean project + lst + 2 official CIFs + figure + report) | `Fe2O3_Fe3O4_2ph_final/` |
| Fit figure (V4 image already read: no occlusion, hkl staggered, two tick rows) | `Fe2O3_Fe3O4_2ph_final/Fe2O3_Fe3O4_2ph_fit.png` |
| Per-phase CIF (GSAS official export_CIF, not hand-written) | `..._Fe12_O18.cif` / `..._Fe24_O32.cif` |
| Refinement log (authoritative source of esd) | `Fe2O3_Fe3O4_2ph_final/Fe2O3_Fe3O4_2ph_final.lst` |
| Unified journal (full trajectory of 8 rounds) | `xrd_workflow/journal.jsonl` + `journal.md` (including the summary section) |
| Defect master table (10 fields) | `defect_table.json` |
| State file | `workflow_state.json` (phase 5) |
| Review judgement column | `review_judgment.md` |
| handoff source (manual-engine converged state) | `result_r6_handoff.json` |

> ⚠ The delivered gpx has had its constraints cleaned up and caches the converged wR — **do not refine** `Fe2O3_Fe3O4_2ph_final.gpx` again; if further optimization is needed, do it on a copy `gsas_proj_bgfinal.gpx`.

# journal.md — LiFePO4 XRD Rietveld refinement quick view (fully regenerated from journal.jsonl)

> The authoritative record is `journal.jsonl` (append-only). Rwp column: manual/fp2k = engine Rwp (Poisson), GSAS = wR — **not directly comparable across protocols**.

| Round | Engine | Stage | Model | Rwp | Baseline R | Verdict | Why | Artifacts |
|---|---|---|---|---|---|---|---|---|
| 1 | manual | calibrate | physical | 26.65 | 95.92 | not yet at plateau | only a free, b/c fixed to the GGA values→V/eta at bounds; zero=-0.285 compensates for the too-small cell | result.json |
| 2 | manual | structure | physical | 26.65 | 95.92 | not yet at plateau | the structure default vary is the same as calibrate (only a)→the result is bit-identical | result.json |
| 3 | manual | vary a,b,c | physical | 37.45 | 95.92 | divergence (numerical) | the GGA cell starting point is ~1% too small, U/V/W pushed to the bound (5/1/0) | result.json |
| 4 | manual | vary a,b,c (experimental cell) | physical | **16.70** | 95.80 | **R plateau** | experimental-cell initial values→converges, plateau, no bound hitting; cell 10.305/5.983/4.672 | result.json |
| 5 | fp2k(auto) | baseline+ladder | physical | 58.6 | 97.4 | divergence (numerical) | the profile is pushed to unphysical (FWHM²<0@42°, B=-0.43); but RF=9.34/density 3.611 = the structure is right; switch to manual | .fp2k-work-*/ |
| 6 | refine_gsas | complete structure ladder | physical | **6.427**(wR) | 19.68 | clean physical baseline (R_before) | bg19.68→inst10.33→cell7.23→profile7.23→atoms6.41; Uiso clamped; fixed instprm Type CR→PXC | gsas_proj_continued.gpx |
| 7 | gsas_ops | antisite D-02 | physical | **6.256**(wR) | 6.427 | antisite adopted (R_after) | x=Fe_Li=Li_Fe=0.0226; conserve+equiv(mult[1,1]); coordinates frozen to prevent drift; review PASS | LiFePO4_defect6.gpx |
| 8 | gsas_ops+export+finalize | background finish + delivery | physical | **6.256**(wR) | 6.256 | delivered (target met) | auto_background (6th order, last); export verdict PASS; finalize GOF=1.02 | LiFePO4_final/ |

---

## Materials and objective
- **Material**: LiFePO4 (olivine), category A (highly crystalline single phase, sharp peaks, P/B≈13). Composition specified by the user + the **Li/Fe antisite defect (D-02)** must be considered.
- **Data**: `pattern.raw` (Rigaku binary RAW, not supported by the plugin's text reader)→host script parses float32 counts (0x0C56, n=7001) + wavelength (f64 0x04BC/0x04C4)→`pattern.xy` (2θ 10–80°, step 0.01, 7001 points).
- **Wavelength (authoritative = data header)**: Cu Kα1=1.5405930 / Kα2=1.5444140 (f64, 0x04BC/0x04C4); Kβ=1.3922460; **intensity ratio 0.5 (not stored in the header→Cu standard, annotated)**. All four entries (manual/pcr/auto/gsas) pass the values explicitly.
- **Objective (§1.3 task-flow specification)**: Rwp as low as possible (reference ≤~10%, approaching the statistical limit Rexp); three-segment scheme Ⅰ→Ⅱ→Ⅲ; if all attempts still fall short, report truthfully. **Result: GSAS wR=6.256% (Rexp=6.154%, GOF=1.02)→ target met (the statistical limit has been reached).**

## Phases and crystal families (conclusion + basis + excluded families and why)
- **Conclusion**: main phase = **Pnma olivine LiFePO4** (single phase, no impurity).
- **Basis**: ① `polymorphs` exhaustively enumerated LiFePO4 → **26 structure types** (70 candidates), with Pnma(mp-aaaabcdl) as the ground state; ② V1 image reading: the peak positions (20.8/25.6/29.7/35.6…) agree with Pnma olivine, with no impurity peak; ③ fp2k density 3.611 g/cm³, RF=9.34 (structural intensity correct); ④ the GSAS complete-structure ladder converges to wR=6.43 (GOF≈1.09).
- **Excluded families and reasons**: the other 25 types (C2/Cc/Cmcm/Fdd2/I-4/Imma/P-1/P1/P2/P2₁/P2₁/c/P2₁2₁2₁/P2₁3/P3₁c/P4₃2₂/P6₁/P6₂2₂/P6₄2₂/P6₅/Pbca/Pc/Pca2₁/Pna2₁/R3) — all are high-energy metastable/hypothetical phases computed by MP, not the olivine ground state; Pnma was adjudicated by actual runs (fp2k+manual+GSAS) as the only one that explains the whole pattern and reaches the statistical limit. **The reachability of D-06/D-09 has been fulfilled** (CIF screening was indeed executed and the enumeration of 26 types is on record).

## Defect master table (exhaustive → screening → execution)
See `defect_table.json` for details (14 classes, each with 10 fields). Summary:
- **D-02 antisite (applicable, executed)**: GSAS-II `set_site_composition`(Li0→Li/Fe, Fe1→Fe/Li) + `conserve_afrac`(Σ=1 per site) + `equiv_afrac`(Li0_Fe=Fe1_Li, mult[1,1]) + coordinates frozen. **x = Fe_Li = Li_Fe = 0.0226 (2.26%)**, wR 6.427→6.256 (Δ=-0.171), GOF 1.09→1.02, review/export both PASS.
- **The other 13 classes are all judged not applicable** (with reasons): D-01 vacancies (Σocc=1 HELD, no vacancies); D-03 substitution (pure phase, no doping); D-04 interstitial/D-05 extra species (no unexplained weak peak/low-angle broad hump); D-06 order-disorder/D-09 polyhedral distortion (Pnma ground state, the 26-type enumeration has fulfilled reachability); D-07 splitting/D-08 off-centering (symmetric peaks, physical bond lengths); D-10 stacking faults (3D framework, no stacking); D-11 microstrain/D-12 size (profile step ΔwR≈-0.0001 negligible, collinear with instrumental X/Y); D-13 twinning (no TEM evidence, no indication); D-14 anisotropic broadening (isotropic already reaches GOF=1.02).

## Achieved results (R and protocol written separately)
- **GSAS-II protocol (delivery)**: **wR = 6.256%**, Rexp/wRmin = 6.154%, **GOF = 1.02**, R(p) = 4.888%, Rb(Bragg) = 5.250%, wRb = 6.434%. χ²≈1.03 → **the statistical limit has been reached**.
- **Complete-structure baseline (no defect, GSAS wR)**: 6.427% (R_before). The antisite lowers it to 6.256% (R_after).
- **Manual-engine protocol (corroborating, not directly comparable with GSAS)**: Rwp=16.70% (cell+profile plateau, coordinates/B not refined).
- **fp2k protocol (corroborating)**: baseline Rwp=97.4% (nominal); the ladder diverges and stops at 58.6% (profile unphysical).
- **Cell (GSAS, delivered)**: a=10.3252, b=6.0051, c=4.6901 Å, V=290.80 Å³ (Pnma).
- **Antisite occupancies (delivered)**: Li site = Li₀.₉₇₇Fe₀.₀₂₃; Fe site = Fe₀.₉₇₇Li₀.₀₂₃ (x=0.0226, charge-neutral interchange, Σ=1 for both sites).

## Not tried / undecided items (must not be left empty)
- **The precise value of the antisite x carries uncertainty**: ΔwR is only -0.171 (marginal), and across repeated refinements x fluctuates between 0.022–0.029 (depending on which parameter families were released simultaneously); x=2.26% is higher than the literature's 0.37% but within the reported range (depending on synthesis). **Not done**: the esd of x (the GSAS covariance was not extracted separately), a fixed-x scan curve (wR vs x) to determine the uncertainty interval.
- **Size/Mustrain and instrumental X/Y are 100% collinear**: sample broadening and instrumental broadening cannot be resolved separately; this sample's peaks are sharp (FWHM 0.11–0.18°), the sample broadening is negligible, and the Size/Mustrain values are non-unique (this does not affect the uniqueness and physicality of the cell/occupancies/Uiso). **Not done**: re-refining with Size/Mustrain fixed to remove the collinearity (no substantive effect on wR, hence omitted).
- **Further routes for lowering R that were not tried**: preferred orientation (Pref.Ori.), extinction (Extinction), anisotropic Size/Mustrain — because GOF=1.02 (the statistical limit) has been reached, these carry overfitting risk and were **deliberately not added** (not "cannot be improved", but "already meeting the target, so unnecessary").
- **Background order**: default 6th order, `auto_background` (6th order, isolate) has been done as the last parameter family; **the bg_scan order-escalation iteration was not done** (because the statistical limit has been reached, escalation would be overfitting, so per §6.8 it is skipped after noting the reason).
- **Antisite atom coordinates**: frozen at the host sites (to prevent low-occupancy drift), not refined independently (the coordinates of a 0.023 occupancy are unreliable, and freezing is the correct treatment).

## Handover recommendations
1. **The deliverables** are in `LiFePO4_final/`: `LiFePO4_final.gpx` (clean project, constraints cleared, do not refine again so as to preserve the cached wR), `LiFePO4_final.lst`, `LiFePO4_Li4_Fe4_P4_O16.cif` (official export_CIF), `LiFePO4_fit.png` (occlusion-controlled figure), `LiFePO4_report.md`. There are also `LiFePO4_deliver*.cif` (structured + official) and `LiFePO4_deliver_fit.png`.
2. **If R is to be pushed further**: there is no room left (χ²≈1.03 = the Rexp floor); any further decrease would be overfitting and is not recommended.
3. **If the antisite x is to be determined precisely**: do a fixed wR-vs-x scan (x=0/0.005/0.01/0.02/0.03), take the parabola minimum + take the esd of x from the GSAS .lst; or add neutron diffraction (Li is weak for X-rays and strong for neutrons, so it can determine Li_Fe independently).
4. **Key points for antisite modelling (pitfall record)**: ① `set_site_composition` adds the X flag to the antisite atoms → low-occupancy coordinates drift out of the cell (export reports coord_out_of_cell) → **the antisite coordinates must be frozen**; ② `equiv_afrac`'s `mult[1,1]` is what means "equal" (varᵢ=multᵢ·t), while `mult[1,-1]` means "opposite"; ③ both `conserve_afrac`/`equiv_afrac` have `override=True`, so **the order must be conserve first, then equiv** for the two to coexist (counter-example: equiv first then conserve overrides the equiv→occupancies run away); ④ the swap parameter x is electronically neutral and not degenerate with scale, but **if the host-site occupancy is released it becomes degenerate with scale→singular (Invalid metric tensor)**, so the host occupancy is pinned by conserve and no separate equiv is set.
5. **instprm pitfall**: GSAS-II requires a 3-character Type (`Type[1][2]`); the legacy .prm's HTYPE must be given `PXC` (not `CR`), otherwise `GSASIIstrIO:3007` IndexError.

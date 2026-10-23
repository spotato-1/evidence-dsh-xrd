# XRD refinement journal (generated from journal.jsonl)

| round | engine | stage | model | Rwp | baseline | verdict | why | artifacts |
|---|---|---|---|---|---|---|---|---|
| λ | - | - | - | - | - | fact | Cu Kα doublet 1.54056/1.54439/0.5; source RAW header DteX100/Cu/monochromator None; explicitly passed | - |
| 2 | manual | explicit vary | physics | 26.92 | 95.79 | numerical re-run | hit max_nfev=8000 ⇒ raise nfev | result.json |
| 3 | manual | explicit vary | physics | 26.92 | 95.79 | numerical re-run | nfev=30000 gives the same result; V/η at the upper bound | result.json |
| 4 | manual | plan, relax η | physics | 26.92 | 32.16 | **R-value basin** | no decrease in three attempts ⇒ basin, switch to Ⅲ | result.json |
| 5 | fp2k | 4-I Pnma (MP cell) | physics | 69.9 | 94.9 | rolled back | MP cell deviation ~1% + initial W too narrow: the cell a step was rejected, W inflated and swallowed the misalignment | .fp2k-work-…-5a97eb |
| 6 | fp2k | 4-I Pnma (literature cell) | physics | **18.5** | 94.9 | progress | literature cell + Caglioti seeding; the last 6 steps all rejected/diverged ⇒ fp2k-side basin | .fp2k-work-…-bd3216 |
| 7 | fp2k | 4-I Cmcm | physics | 86.3 | 98.6 | excluded | all cell/background steps rejected, only the peak shape swallowing the misalignment was left | .fp2k-work-…-5f8c66 |
| 8 | fp2k | 4-I Pna21 | physics | 82.6 | 98.8 | excluded | 4-I adjudication complete: main phase = Pnma olivine | .fp2k-work-…-643619 |
| 9 | gsas | 4-III ladder#1 | physics | 7.53* | 27.35 | rolled back | *the reported value belongs to a non-physical intermediate state with negative Uiso; refinement crashed after uiso_floor clamping (SVD zero step → negative cell); the true wR=39.78 | gsas_proj.gpx (old) diag_refine.log |
| 10 | gsas | 4-III ladder#2 rebuild | physics | **12.62** | 27.35 | progress | non-degenerate parameterisation (X/Y never opened, profile opened for Mustrain only); genuinely converged, lst complete | gsas_proj.gpx (rebuilt) |
| 11 | gsas_ops | D2 antisite scan#1 | physics | 12.28 | 12.66 | discarded | x=4.5% was built on a wrong pure-Lorentzian peak shape; the constraint machinery crashed three times on the bad project (this diagnosis prompted the round-12 fix) | LiFePO4_antisite_scan.gpx |
| 12 | gsas_ops | **Voigt peak-shape repair** | physics | **7.80** | 11.35 | progress | σ² full-angle clamping trap (the U/V/W derivatives are identically zero, so it cannot escape) ⇒ manually reset the Gaussian components to 721/-193/48.3; the strongest peak top recovered, a direct drop of 3.5 points | gsas_ops_continued.gpx |
| 13 | gsas_ops | D2 antisite re-scan + constraints | physics | 7.47 | 7.48 | progress | scan minimum x≈0.007; three-conservation LS refinement x=0.0071 with all conservations HELD (same order of magnitude as the literature 0.0037) | LiFePO4_constrained.gpx |
| 14 | gsas_ops | Uiso physicalisation + joint refinement | physics | **6.86** | 7.44 | progress | under the correct peak shape all Uiso turned positive (the root cause of the negative Uiso = bad peak shape); coordinates/cell/peak shape refined jointly; Kα2/SH-L/PO(010) all showed no improvement and were excluded | LiFePO4_final_work.gpx |
| 15 | gsas_ops | background order upgrade | physics | **6.70** | 6.86 | progress | auto_background 6→14 orders, order 14 is optimal (+0.15); 16+ not tried (gain rate <0.03/order) | gsas_ops_out.gpx |
| 16 | export+finalize | 5 delivery | physics | **6.70** | - | complete | all bond lengths physical; GOF=1.09 (9% above wRmin 6.15); delivery package LiFePO4_final/ | LiFePO4_final/ |

## Material and target
- Material: LiFePO4 (specified by the user), Rigaku DteX100 binary RAW (Cu Kα doublet, no monochromator), 7001 points 10-80°/0.01°.
- Target: R as low as possible (reference set at <8%); **achieved: GSAS-II wR=6.70% (GOF=1.09, wRmin=6.15)**.
- Additional user requirement: consider Li/Fe antisite defects ⇒ the complex-case checklist is triggered (AI semantic judgement: highly defective system).

## Phases and crystal families (conclusion + evidence + the families excluded and why)
- **Conclusion: main phase = olivine LiFePO4, Pnma (#62), Z=4.**
- Evidence: ① all 25 measured peaks match Pnma reflections (numerical V1); ② `polymorphs` retrieved 26 crystal forms + an exhaustive literature screen of 3 families; ③ fp2k actual-run adjudication: Pnma 18.5 ≪ Cmcm 86.3 / Pna21(Pn21a) 82.6; ④ GSAS converged at GOF=1.09.
- Excluded: Cmcm (high-temperature metastable family) — all cell/background steps rejected, 86.3; Pna2_1/Pn21a (pseudo-olivine family) — 82.6; the remaining 23 MP candidates had low probability and were not run one by one (the screen scores are false signals in the noise, see the notes in journal rounds 7-8).
- Unit cell: a=10.3244(2), b=6.0045(1), c=4.6897(1) Å, V=290.725(14) ų (consistent with the ICSD 16147 literature values 10.329/6.007/4.691; the small difference is related to stoichiometry/antisite).

## Defect summary table (enumerate → screen → execute)
- **D-02 Li/Fe antisite (specified by the user): applicable and adopted** — pair-exchange model (equal amounts of Fe on the Li site and Li on the Fe site); under three conservation constraints LS determines x=0.0071, and after full-parameter joint refinement **x=0.0089 (0.89%)**; an independent fixed-x scan gives a consistent minimum ≈0.007; same order of magnitude as well-crystallised LiFePO4 in the literature (0.0037). The stoichiometry remains exactly LiFePO4.
- D-01/N-03 Li vacancies/non-stoichiometry: **pending** — XRD is insensitive to Li (scan effect ≲0.02 wR points, Li scattering accounts for ~3%), so ICP/EDS is required.
- D-11 microstrain: applicable (isotropic Mustrain 4483×10⁻⁶ adopted from refinement).
- The other 11 categories: not applicable/pending, item-by-item reasons in `defect_table.json` (including D-06/D-09 reachability — the crystal-family exhaustion has been executed).

## Results achieved (R and convention written separately)
- **GSAS-II convention (delivery convention): wR=6.70%, R=5.14%, Rb=6.20%, wRb=8.30%, wRmin=6.15%, GOF=1.09, chi²=8306**.
- FullProf (fp2k) convention (4-Ⅱ intermediate value, not directly comparable with GSAS wR): Pnma ladder Rwp_mean=18.5.
- Manual engine convention (4-Ⅱ basin, Poisson weights): Rwp=26.92 (the V/η upper bound is on record).
- Structure: Pnma; atomic parameters in `LiFePO4_final/LiFePO4_report.md`; bond lengths Fe-O 2.088-2.252 / P-O 1.530-1.574 / O-O 2.407-2.599 Å, all physical.
- Uiso: Li fixed at 0.005 (XRD insensitive, declared as-is); Fe 0.0137 / P 0.0175 / O 0.008-0.0174.
- Corrections: surface roughness (SurfRoughA=0.247/B=0.620, strongly absorbing sample) + 14th-order Chebyshev background.

## Not tried · unresolved items
- **Not tried**: background orders 16-20 (the gain rate is already <0.03/order, scan upper limit 14); generalised anisotropic Mustrain/Size models (isotropic has reached the statistical limit); Li Uiso refinement (XRD insensitive); instrument size/strain separation (no standard sample); twin modelling (no TEM evidence, pending per D-13); actual runs of the 23 MP candidates other than Cmcm/Pna21 (low prior).
- **Tried and ineffective**: SH/L asymmetry (Δ≈noise), PO March-Dollase(010) (Δ≈noise), Kα2-ratio refinement (0.5 unchanged), Li vacancies (XRD insensitive), negative Uiso (rejected as non-physical).
- **Unresolved**: Li vacancies/stoichiometry deviation (needs ICP/EDS); crystallite size (needs a standard); visual detection V1-V4 (two vision-bridge engine contract failures — an environment limitation; fallback to the numerical criteria via channel ③ was made and disclosed; the finished figure is left for the user to inspect manually).

## Suggestions for the next handler
1. If data can be added: ICP/EDS to determine the Li/Fe ratio and adjudicate Li vacancies; a standard sample (e.g. LaB6) to determine the instrumental broadening and separate size/strain.
2. To push R further down: the residuals are already at the statistical noise level (GOF 1.09), and physical measures are expected to gain ≤0.5 points; overfitting is not recommended.
3. Do not refine the delivered project again (the constraints have been cleared and the cached wR would be lost); to continue, branch from `gsas_ops_out.gpx`.
4. The uncertainty of the antisite value 0.89% is large (the scan curve is flat), and a range of 0.5-1.5% is recommended when quoting it.

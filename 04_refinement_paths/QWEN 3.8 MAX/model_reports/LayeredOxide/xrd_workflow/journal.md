# XRD refinement journal (fully regenerated from journal.jsonl; the close-out summary section is at the end)

| Round | Engine | Stage | Model | Rwp | Baseline R | Verdict | Why | Artifacts |
|---|---|---|---|---|---|---|---|---|
| 1 | xrd_refine_auto | fp2k-ladder | physical | 68.8 | 99.3 | progress | the P2 family ladder descends normally 93.2→78.8→78.5→72.8→72→68.8; the single-phase value being rather high is expected (impurity not modelled); adjudicating the main phase against O3 | .fp2k-work-P2_NaNMnMoO2_main-0ecb3e/ |
| 2 | xrd_refine_auto | fp2k-ladder | physical | 96.5 | 96.8 | switch phase/exclude O3 | the O3 ladder shows almost no improvement and the cell step was rejected ⇒ cannot be indexed; P2 wins (68.8 vs 96.5) | .fp2k-work-O3_NaNMnMoO2_cand_orbit_01-7ca3f5/ |
| 3 | xrd_refine_manual | twophase (default 3 parameters) | physical | 85.12 | 99.10 | not yet at plateau | the twophase stage by default releases only scale/zero/s2_scale | result.json |
| 4 | xrd_refine_manual | (explicit vary) | physical | 13.31 | 99.10 | not yet at plateau; ⚠U/W/eta at bounds | peak-shape parameterization out of control (U=5!) | result.json |
| 5 | xrd_refine_manual | (explicit vary, nfev 40000) | physical | 13.31 | 99.10 | not yet at plateau; ⚠same as above | raising nfev has no effect ⇒ a bad local solution, not non-convergence | result.json |
| 6 | xrd_refine_manual | (r7 tight physical bounds) | physical | 9.517 | 97.26 | not yet at plateau; ⚠W at the lower bound | tight bounds (k∈[0.99,1.015], Y≤0.3, U≤0.25) give a big improvement; an asymmetric residual of (002) appears | plan_r7_twophase.json |
| 7 | xrd_refine_manual | (r8 Ama2 impurity) | physical | 10.127 | 96.82 | exclude Ama2; ⚠U/W/s2_scale at bounds | s2_scale→0.012 hits bottom = the fit rejects Ama2 as a single-phase substitute | plan_r8_ama2.json |
| 8 | xrd_refine_manual | (r9s c=11.19) | physical | 9.163 | 96.67 | progress (clean) | c=11.189 makes (004)31.97/(106)61.95/(008)66.90 all line up; zero=-0.077 is dragged off by the (002) asymmetry | plan_r9s.json |
| 9 | xrd_refine_manual | (r10 extras trailing peak) | fallback | 9.358 | 96.50 | rollback | empirical trailing peak + tight zero is worse than free zero | plan_r10_extras.json |
| 10 | xrd_refine_manual | (r11 Na-occ+dw) | physical | 9.192 | 96.82 | not yet at plateau; ⚠occ_Na1 at bound | Na→0.828 false gain (D0 criterion), R did not drop ⇒ rejected | plan_r11_struct.json |
| 11 | xrd_refine_manual | (r12 O-z ±0.05) | physical | 9.012 | 96.63 | invalid (unphysical bound) | cz_O3→0.1324 exceeds the physical range of P2 (TM–O 2.23 Å)⇒ boundary false gain voided | plan_r12_oz.json |
| 12 | xrd_refine_manual | (r13 O-z physical window) | physical | 9.160 | 96.63 | **R plateau** | plateau=true, flags=[]; clean sequence 9.163/9.358/9.160 plateau ⇒ switch to GSAS-II; handoff source | plan_r13_oz_phys.json, result.json |
| 13 | xrd_refine_gsas+ops | v1-v3 (handoff lineage) | physical | 12.42(wR) | — | abandoned (lineage frozen) | the handoff instrument U/V/W was seeded ×1803 (should be ×1e4)⇒ inst diverges (Zero=-0.211, U=-5663, correlation 99%+); v2 negative Uiso (review fail); v3 MD texture collapses (002) (residual +2374) | gsas_v1_handoff_backup.gpx/.lst, gsas_v2_atoms.gpx, gsas_v3_md.gpx |
| 14 | xrd_refine_gsas | v4 fresh rebuild | physical | 12.298(wR) | 15.584 | progress | INST_CuKa2.instprm (×1e4 healthy seed, Zero=0 fixed) + scale2_init=0.25, no handoff; Na2MoO4 a=9.1296 | gsas_proj.gpx |
| 15 | xrd_gsas_ops | v4→cell/SH-L/W | physical | 10.017(wR) | 12.298 | progress | cell→11.964, SH/L(0.0465)→11.910, W→10.017 (-1.89) | gsas_v4.gpx |
| 16 | xrd_gsas_ops | v5-v8 atoms/three phases/Na-occ | physical | 8.479(wR) | 10.017 | progress + two rejections | atoms→8.254, after clamping 8.479 (TM/O negative U clamped at 0.002 and fixed); ternary Na-Mn-Mo-O Δ-0.003 rejected; Ama2 Δ-0.002 rejected; Na-occ→0.6908 but wR+0.05 ⇒ nominal 0.72 fixed + U(Na)=0.05 (D3) | gsas_v5/v6_tert/v7_ama2/v8_naocc.gpx |
| 17 | xrd_gsas_ops | v9 Zero released + bg | physical | 7.575(wR) | 8.530 | progress | Zero=-0.0954° (sample displacement ~0.24mm, physical) single step -0.95; (002)@(004) agree simultaneously ⇒ the d-ratio 2.007 mystery = Zero + c re-anchoring (not a stacking fault); GOF 1.53 | gsas_v9.gpx |
| 18 | xrd_gsas_ops | v10/v11 V,X+Uiso re-test | physical | 7.327(wR) | 7.575 | **GSAS plateau** | V/X→7.326; the Uiso release transiently gives 6.997 but TM/O go negative again ⇒ clamped back to 0.002 (negative-U false gain does not enter the delivery); clean plateau 7.33 | gsas_v10.gpx, gsas_v11.gpx |
| 19 | xrd_gsas_ops | v12/v13 Na 2b/2d split | physical | 6.938(wR) | 7.327 | adopted (D4) | structure-factor analysis: Na(2d) contributes negatively to F(100) while F(002) is insensitive to it ⇒ splitting only raises hk; 2b:2d=0.241:0.479 (the two sites in the P2 literature), conserve_afrac 0.72 HELD; ⚠tool pitfall: replace_phase mistakenly deleted the impurity phase (restored with add_phase) | gsas_v12_splitna.gpx, gsas_v13.gpx, P2_NaNMnMoO2_splitNa_orbit_01.cif |
| 20 | xrd_finalize | delivery | physical | **6.94(wR)** | — | **target-met delivery** | wR=6.94≤10 ✓; R=5.51, Rb=7.53, GOF=1.40, wRmin=4.97; after the V4 hygiene check the figure was re-exported with top_peaks=0 | LayeredOxide_final/ |

> Protocol: rounds 1–12 Rwp = manual/fp2k protocol (decision values); rounds 13–20 Rwp = GSAS wR protocol. The two protocols are not directly comparable; **the delivery protocol = GSAS wR**. Round 5a (r6-plan, 12.765, voided for bound hitting) is recorded in the workspace-root xrd_workflow/journal.jsonl because of an out_dir mistake.

## Materials and objective

- Sample: LayeredOxide; feed ratio Na0.72Ni0.33Mn0.62Mo0.05O2 layered oxide; raw materials NaOH, Na2MoO4·2H2O, Ni(CH3COO)2·4H2O, Mn(CH3COO)2·4H2O, citric acid; sol-gel + ball milling; calcined at 450°C/5h + 900°C/12h.
- Data: Rigaku RAW4.00 (pattern_2theta.txt); Cu Kα doublet [1.5406, 1.54439, 0.5] (data header Monochromator=0; the measured doublet at 64.31/64.51 confirms it); 10.000–79.997°, 3432 points, step 0.0204012°.
- Objective (user): publication-grade two-phase Rietveld (main phase + sodium molybdate impurity), **R ≤ 10 (delivery protocol GSAS-II wR)**; if not achieved, report truthfully.
- **Result: wR = 6.94% ≤ 10, target met** (GOF=1.40, wRmin=4.97, review=pass).

## Phases and crystal families (conclusion + basis + excluded families and why)

- **Main phase: P2-type Na0.72(Ni0.33Mn0.62Mo0.05)O2, P63/mmc**. Basis: phase_screen 2.184/n=8 (O3 only 0.188/n=1); the fp2k actual-run adjudication 68.8 vs 96.5; the exhaustive literature families P2/O3/OP4/O3' (the Mo-doped Na0.66Ni0.33Mn0.67−xMoxO2 belongs to the P2 family, J. Alloys Compd. 2017 S0925838817306461). Final state: a=2.88936(4), c=11.1584(15) Å, V=80.674(17) ų; Na1@2b 0.2407 + Na2@2d 0.4793 (total 0.720 conserved); TM@2a Mn0.62/Ni0.33/Mo0.05 (nominally fixed); O@4f z=0.1055(9), TM–O≈2.02 Å.
- **Impurity phase: Na2MoO4 (sodium molybdate) cubic Fd-3m** (COD 2240655), a=9.1226(2) Å; its characteristic independent peak is (220)@27.54. This confirms the user's prior statement.
- Excluded: O3(R-3m) (screen+fp2k); OP4/O3' (all (00l) agree after P2+Zero re-anchoring, so unnecessary); Na2MoO4 Ama2/C2c (actual run scale→0 / ΔwR≈0); Na2CO3 (its strongest line at 29.4° is absent); MoO3 (its strongest line at 12.7° is absent); low-valence Na-Mo phases (chemically unreasonable in 900°C air); ternary Na3.13Mn1.43Mo3O12 (cod_1560391, actual run ΔwR=-0.003 rejected); the Na-Mn-O candidate family (the screen hit is a scoring artifact and did not pass the actual-run/chemistry gate).

## Defect master table (exhaustive → screening → execution)

See `defect_table.json` in the same directory (10 fields). Key points: Na 2b/2d split mixed occupancy = **adopted** (conservation constraint, 2b:2d≈1:2, wR -0.39); O-z = **adopted** (0.1055(9)); Na total occupancy = nominal 0.72 fixed (releasing it drifts with no improvement); TM composition = nominally fixed (degenerate with scale, needs ICP/EDS); TM/O Uiso = clamped at 0.002 and fixed (LS pushing to negative = false gain, does not enter the delivery); MD texture = rejected by actual run; anisotropic broadening/stacking fault/antisite = not executed (reasons in defect_table and in the not-tried items below).

## Achieved results (R and protocol written separately; FullProf Rwp and GSAS wR are not directly comparable)

- **Delivery (GSAS-II wR protocol)**: wR=**6.94%**, R=5.51%, Rb=7.53%, wRb=9.26%, wRmin=4.97%, χ²=6677, GOF=**1.40**. Instrument: Zero=-0.0954°, SH/L=0.0465, U=1657/V=-635(fixed)/W=60.4/X=0/Y≈2.0; 6th-order Chebyshev background (fitted last ✓, not escalated — the target was already met).
- Manual-engine protocol (corroborating evidence): r13 Rwp=9.160 (Rexp 4.961, plateau, flags=[]).
- fp2k protocol (corroborating evidence): P2 single phase 68.8 / O3 96.5 (family adjudication).
- Phase scale: Na2MoO4 Scale/main-phase Scale ≈ 0.25 (GSAS phase scale ratio; the mass fraction can be computed in report.md from Scale·MW/V).

## Not tried / undecided items

- **Not tried (with reasons)**: anisotropic Size/Mustrain/HStrain (GOF 1.40 is already good, avoiding overfitting); stacking fault/DIFFaX (the engine has no such capability; after Zero + c re-anchoring (002)/(004) agree, so the necessity disappears); Na/TM antisite (the Na splitting already explains the hk intensity gap); TM composition refinement (degenerate with scale, needs ICP/EDS); background order escalation iteration (not done — order 6 already meets the target, and per the rules no escalation is made); custom-engine asym branch (GSAS SH/L already solves it, abandoned).
- **Residual small peaks (disclosed truthfully, not "cannot be improved")**: 31.97°(+267), 64.31/64.51°(+203/+161), 35.81°(+155), 62.04°(+131), 39.40°(+113), 43.50°(+105) — mild intensity residual at the hk/(004) peak tops (~10–25% of the net height), suspected to be the remaining systematic error of the TM-layer intensity distribution (the cost of clamping TM Uiso at 0.002 and fixing the composition nominally); 78.5°(+75) is at noise level and unassigned.
- **Fixed-value statement**: Na Uiso=0.05, TM/O Uiso=0.002, Na total occupancy=0.72, TM composition=nominal — all fixed-by-constraint, not measured values, no esd reported; O6 z=0.1055(9) and the cell/Zero/SH-L/U/W/Y are measured values.
- The impurity phase's atom coordinates/ADP are frozen at the COD single-crystal values (a weak second-phase powder is not measurable).

## Handover recommendations

- Final products = `LayeredOxide_final/` (clean gpx + lst + 2 CIFs + fit.png + report.md); **do not refine that gpx again** (stale constraints have been cleared and further refinement would lose the cached wR).
- To keep lowering wR, branch from `gsas_v13.gpx` (candidate actions: anisotropic Mustrain/HStrain, TM-composition-constrained refinement).
- The abandoned lineage v1-v3 (handoff unit contamination) is archived only; two tool-layer lessons are recorded in journal rounds 13/19: ① handoff instrument ×1803 vs ×1e4; ② replace_phase replaces all phases.

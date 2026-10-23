Task complete, goal achieved and closed. Final summary:

## ✅ Result: publication-level two-phase Rietveld refinement meets target

**Delivery basis (GSAS-II): wR = 6.94% ≤ 10**, R = 5.51%, Rb = 7.53%, GOF = **1.40**, wRmin = 4.97, plausibility review **pass** (no negative Uiso, occupancy conservation measured HELD).

### Final structural model (two phases)

| Phase | Structure | Key parameters |
|---|---|---|
| **Main phase P2-Na₀.₇₂(Ni₀.₃₃Mn₀.₆₂Mo₀.₀₅)O₂** | P6₃/mmc | a=2.88936(4) Å, c=11.1584(15) Å; **Na split two-site** Na1@2b 0.241 + Na2@2d 0.479 (total 0.720 conserved); TM@2a mixed occupancy (fixed at the nominal feed ratio); O@4f z=0.1055(9), TM–O≈2.02 Å |
| **Impurity sodium molybdate Na₂MoO₄** | Fd-3m cubic (COD 2240655) | a=9.1226(2) Å; phase scale ratio ≈0.25; user prior **confirmed** |

### Key physical findings
1. **The (002)/(004) d ratio 2.007 "anomaly" is not a stacking fault** — it is the geometric effect of a constant zero-point offset Zero=-0.095° (sample displacement ~0.24 mm); after Zero is released, (002)/(004)/(006)/(008) all agree simultaneously;
2. **The hk/(00l) intensity imbalance is resolved by the Na 2b/2d split mixed occupancy** (wR 7.33→6.94), with 2b:2d≈1:2 consistent with the standard P2 literature refinement;
3. The O3/OP4/O3' crystal family, Ama2/C2c-Na₂MoO₄, Na₂CO₃, MoO₃, ternary Na-Mn-Mo-O and the various Na-Mn-O candidates were all excluded one by one under "two-level funnel + single-variable actual run" (on record).

### Workflow execution (strictly the xrd plugin's five stages, all 20 rounds recorded)
①identification (B class, target R≤10) → ②initial screening (Cu Kα doublet taken from the data header [1.5406, 1.54439, 0.5], measured doublet confirmed; V1 figure review) → ③phase identification (literature-family enumeration + screen + fp2k actual-run adjudication P2 vs O3 = 68.8 vs 96.5) → ④three-stage (Ⅰ build_orbit+validate+cif_to_pcr; Ⅱ manual engine numerical plateau Rwp 9.16, invalid rounds all handled under the flags rules; Ⅲ GSAS-II: the handoff lineage was discarded and rebuilt due to unit-conversion contamination → fresh v4→v13 stepwise 12.30→6.94) → ⑤delivery (finalize package + V4 output-figure hygiene recheck).

### Deliverables (under the `LayeredOxide` folder, user chose to **retain everything**, no file deleted)
- Delivery package: `LayeredOxide_final/LayeredOxide_final.gpx`, `LayeredOxide_final.lst`, `LayeredOxide_fit.png`, `LayeredOxide_report.md`, `LayeredOxide_built.cif`, `LayeredOxide_sodium_molybdate.cif`
- Final source project: `gsas_v13.gpx` (continue from this branch, do not touch the final package)
- Records: `xrd_workflow/journal.jsonl` (20 rounds) + `xrd_workflow/journal.md` (including the fixed summary section), `workflow_state.json`, `defect_table.json`, `review_judgment.md`, `phase_summary.json`

### Honest disclosure (see "Untried · Unresolved items" in journal.md)
- Residual small peaks: 31.97°(+267), 64.3/64.5°(+203/+161), 35.8°(+155) and other slight intensity residuals at the tops of hk peaks (net height 10–25%), suspected to be residual systematic error of the TM-layer intensity model; 78.5°(+75) is at noise level and unassigned — **these are "no further improvement within what has been tried", not "cannot be improved"** (untried: anisotropic broadening, TM composition-constrained refinement [requires ICP/EDS], antisite testing; the background stays at order 6 without escalation — target already met, so per the rules no escalation).
- Fixed-value declaration: total Na occupancy 0.72, TM composition, Uiso(Na)=0.05, Uiso(TM/O)=0.002 are all fixed-by-constraint (not determined, no esd reported); the impurity-phase atom parameters are frozen at the COD single-crystal values.

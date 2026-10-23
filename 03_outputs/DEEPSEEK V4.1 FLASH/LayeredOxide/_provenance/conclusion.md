Analysis complete, target achieved.

## Results

| Item | Result |
|---|---|
| **Main phase** | **P2-type layered oxide**, P6₃/mmc, a = 2.8875(4) Å, c = 11.1561(21) Å |
| **Impurity** | **anhydrous Na₂MoO₄**, Fd-3m, a = 9.1173(25) Å |
| **Phase fractions** | main phase 91.01(4) wt% / Na₂MoO₄ **8.99(4) wt%** (≈4.87 mol%) |
| **R (GSAS-II delivery basis)** | **wR = 7.78%**, R = 5.81%, Rb = 9.47%, wRmin = 4.97%, **GOF = 1.57** |
| Target | publication-level **R ≤ 10 → achieved**, REVIEW pass (no negative Uiso, no occupancy out of range) |

R progression: fp2k single phase 23.6 → manual single phase 10.97 → manual two phase **8.96** → GSAS **7.78**.

## Three scientific points worth your attention

**1. It is P2, not O3.** Joint indexing of 17 reflections gives rms = 0.047°. The strongest peak is at **15.75°**, whereas O3 requires (003) at 16.8°; at 43.46° the reflection is **(103)**, not (104) — only P2's (100)/(102)/(103)/(104) sequence can explain the spacings 35.77/39.36/43.46/48.78 simultaneously.

**2. The sodium molybdate content is self-consistent with the feed ratio.** The refinement gives 4.87 mol% Na₂MoO₄, while putting the nominal 0.05 mol Mo entirely into sodium molybdate should give **4.76 mol%** — they agree. On that basis I ran a control (main phase TM changed to Mo-free); the result was wR 7.68% vs 7.64%, **the difference is within the noise**: XRD cannot tell whether this 5% Mo is in the TM layer or in the sodium molybdate, so the delivery kept your nominal composition.

**3. One methodological pitfall (the most important one this time).** Releasing GSAS's `U/V/W` together with `Size/Mustrain` and `Uiso` makes the least squares drift to **U=−3080, V=+6602, W=−2067** (σ²<0), dragging the impurity phase's Mo–O from 1.773 Å to 2.08 Å and turning **all 9 Uiso negative**. **The negative Uiso are taking the blame for a broken peak shape**. The fix is to freeze the profile at the physical values given by the bounded manual engine, and then tie Mn/Ni/Mo on the same 2a site into a single Uiso with an equality constraint (Mo's occupancy is only 0.05, and when freely refined its Uiso once drifted to 9.97×10⁷).

## Honesty statements that must be carried along

- All 6 main-phase Uiso are **clamped at the physical lower bound 0.005**; they are "set by constraint", **not measured values**, so do not give esd or cite them as thermal-vibration results.
- The short **Na–Na 1.671 Å** contact in the main phase is an inherent product of P2's **disordered average structure** (2b and 2d lie in the same layer at a/√3 with mutually exclusive occupancy, and literature CIFs are the same), not a structural error.
- **Two schemes were given for O's z**: free (TM–O 2.08 Å, wR 7.78) / literature-constrained (1.935 Å, wR 8.54), both ≤10. By the feed ratio, charge balance gives a TM average valence ≈ +3.14 including Mn³⁺ (Jahn-Teller), so 2.08 Å has a chemical explanation.
- **Untried items** (so we can only say "on target within the range tried", not the data limit): background order escalation, Na occupancy + conservation constraint, other polymorphs of Na₂MoO₄, a third phase, oxygen vacancies.
- `raw/Mo.raw` is **binary RAW1.01**, unsupported by the plugin reader and unused; the synthesis raw-material list **does not list a Mo source** — please confirm these two points.

## Main outputs

- `LO_final/` — delivery package: `LO_final.gpx`, `LO_final.lst`, `LO_fit.png`, `LO_report.md`, two official GSAS-II `export_CIF` files
- `LO_analysis_report.md` — complete report (including all the statements above and the untried list)
- `xrd_workflow/journal.jsonl` / `journal.md` — 9-round authoritative record + quick overview
- `workflow_state.json`, `defect_table.json`, `review_judgment.md` — state and review columns
- `work/gsas_r05/gsas_proj_r08.gpx` — the as-delivered project (to continue, derive from here; **do not re-refine `LO_final.gpx`**, it will lose the cached wR)

The working directory is **fully retained** per your choice, with no cleanup done.

(One plugin defect for your reference: in `xrd_cif_edit`'s `edit_text`, `drop_sites` does not actually delete atom rows, it only skips formatting — I bypassed it by switching to `build`. Also, `xrd_finalize` reads the wR cached in the project, so if `fix_uiso` is later used to change values without re-running the refinement, the packaged R will be the old value.)

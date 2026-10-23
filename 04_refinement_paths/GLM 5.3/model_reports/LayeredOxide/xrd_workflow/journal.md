# NNMO sample work journal (overview)

> Generated from journal.jsonl. Sample: Na0.72Ni0.33Mn0.62Mo0.05O2, P2 layered oxide + Na2MoO4 impurity.

| round | engine | stage/level | model | Rwp | baseline | verdict | why | artifacts |
|---|---|---|---|---|---|---|---|---|
| 1 | xrd_refine_manual | calibrate | physics | 10.19 | 99.10 | R-value basin | P2 single-phase bounded fit, converged cleanly | result.json |
| 2 | xrd_refine_manual | calibrate | physics | 16.40 | 98.94 | not yet at the basin | crystal-family adjudication control: O3 with five parameters at the upper bound, P2 wins | result.json |
| 3 | xrd_refine_manual | twophase | physics | 12.75 | 99.10 | not yet at the basin | zero pushed to the −0.5 lower bound and degenerated with k, worse than the single phase; switched to a seeded plan | result.json |
| 4 | xrd_refine_manual | twophase | physics | 9.35 | 13.89 | R-value basin | two-phase seeded fit; Na2MoO4 fraction 0.24, k=1.0017 | result.json |
| 5 | gsas | build+bg | physics | 18.24 | - | progress | GSAS project built (handoff: phase fraction/main-phase cell/Zero), background step | gsas_proj.gpx |
| 6 | gsas | inst+cell+profile | physics | 16.27 | - | progress | ladder bg→inst→cell:all→profile; leftover Cell flag + negative mustrain | gsas_proj_continued.gpx |
| 7 | gsas | scale2 retry | physics | - | - | rolled back | a set_cell mis-write polluted both projects (operational type); root cause = second-phase cell not cubic | - |
| 8 | gsas | rebuild + per-phase ladder | physics | 14.38 | - | progress | rebuilt with per-phase `phases` switches: bg 15.76→inst 15.27→scale2 14.38 | gsas_proj.gpx |
| 9 | gsas | atoms + clamping | physics | 13.66 | - | progress | atoms 13.46 but negative Uiso; the equiv+conserve+floor trio repaired it to a physical state | gsas_proj_continued.gpx |
| 10 | gsas | MD texture + Na conservation | physics | 13.38 | - | progress | March-Dollase(001)=0.919, significant texture; Na occupancy refined with conservation F | gsas_proj_continued.gpx |
| 11 | gsas | background order upgrade + O fixed | physics | 13.01 | - | progress | auto_background 6→12 iteration; O Uiso set to 0.02; R(profile)=7.74 | gsas_final_d.gpx |
| 12 | gsas | SH/FCJ/wrap-up trial | physics | 13.02 | - | R-value basin | SH 12.93 negative Uiso discarded; FCJ ineffective; wrap-up fine-tuning gain <0.02 — the GSAS parameterisation basin | NNMO_delivery.gpx |

## Material and target
- Na0.72Ni0.33Mn0.62Mo0.05O2 (batch ratio), P2 layered main phase + Na2MoO4 impurity (explicitly stated by the user).
- Target: publication grade, target R ≤ 10 (in task-flow form, not a hard threshold; if not reached, report as-is).

## Phases and crystal families (conclusion + evidence + the families excluded and why)
- Main phase P2 (P6₃/mmc): all 11 significant peaks indexed (a≈2.89/c≈11.23) + adjudication with the manual engine under the same settings (P2 10.19 converged cleanly vs O3 16.40 with five parameters at the upper bound).
- Excluded: O3 ((003) predicted 16.7° vs the strongest observed peak 15.77°; at the upper bound); P3 (no corresponding peaks for (102)39.4/(103)43.5).
- Second phase α-Na2MoO4 (Fd-3m, COD 2240655): characteristic peaks at 27.50/32.46° + consistent with the two-phase refinement; Na-O 2.399×6 / Mo-O 1.772×4 numerically verified.
- Both candidates in the fp2k crystal-form scoring were polluted by unbounded peak-shape divergence (P2 negative W / O3 V=31.8, spurious 25.7) — an environmental failure, not accepted.

## Defect summary table (enumerate → screen → execute)
- Negative Uiso (atoms step): repaired with the trio equiv_uiso (Na group/TM group) + conserve_afrac (Na=0.72) + uiso_floor(0.005); the delivered state is fully physical.
- Occupancy conservation: conserve_afrac HELD (re-checked by an actual check_conservation).
- c-axis texture: March-Dollase(001)=0.919→1.475, significant, adopted.
- Negative mustrain (legacy ladder): switched to a size-only per-phase scheme, mustrain turned off.
- TM same-site occupancy: in principle unresolvable by XRD, fixed at the batch ratio (stated as-is).

## Results achieved (R and convention written separately)
- GSAS-II (delivered): **Rwp=13.05%, R(profile)=7.76%**, Rexp=4.97, GOF=2.63. R ≤ 10 met; Rwp not met (short by 3.05, composition already localised: the under-fit of the (002) peak top contributes about 1/3 + the expressive limit of the peak-shape parameters, U/W, X/Y, SH/L/Zero correlated 99%+).
- Manual engine (corroboration): Rwp=9.35% (Poisson convention, not directly comparable with GSAS wR).
- Basin criterion: SH texture 12.93 (negative Uiso, discarded), FCJ ineffective, wrap-up fine-tuning gain <0.02 — the numerical basin of the GSAS parameterisation is established (no effective decrease in the last three attempts).

## Not tried · unresolved items
- Synchrotron/neutron supplementary data (could resolve the (002) peak top and the texture/thermal-parameter degeneracy).
- Manual step-by-step peak-shape tuning in the GSAS GUI (the scripting layer has reached the parameterisation limit).
- A physical version of spherical-harmonic texture (SH was tried but needs redesigning together with the Uiso constraints; not completed).
- TM occupancy needs XPS/ICP corroboration (unresolvable by XRD).

## Suggestions for the next handler
- If Rwp<10 is needed: prefer supplementary data or GUI refinement (do not refine the delivered project NNMO_final/NNMO_final.gpx again — the cached wR would be lost; continue from gsas2/gsas_final_d.gpx or NNMO_delivery.gpx).
- Report citations: main phase a=2.8963 c=11.1724 Å; Na2MoO4 a=9.1089(2) Å; MD(001)=1.475; Na 0.034+0.686=0.72 (conservation HELD).
- Data convention: Cu Kα doublet (1.54060/1.54439/0.5).

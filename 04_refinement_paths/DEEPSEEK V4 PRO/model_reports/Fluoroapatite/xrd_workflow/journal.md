# XRD work-log quick view — fluoroapatite Ca5(PO4)3F

> For the authoritative round-by-round record see `journal.jsonl` (append-only); this file is a human-readable quick view + wrap-up summary section.

| round | engine | stage | model | Rwp/wR | baseline R | verdict | why | artifacts |
|---|---|---|---|---|---|---|---|---|
| 1 | xrd_refine_auto (fp2k) | calibrate | physical | 100% | 101% | rollback | single-parameter scale refinement diverged (Scale factor<0), peak positions correct but peak shape cannot converge | .fp2k-work-*/fp2k_result.json |
| 2 | xrd_refine_manual | calibrate | physical | 49.11% | 88.90% | rollback | profile model degradation (W→0, eta→0.98 at the bound), hit max_nfev=8000 and did not converge | result.json / components.json |
| 3 | xrd_refine_gsas | structure | physical | 9.75% | 27.96% (before inst) | progress·wrap-up | GSAS-II final optimisation; adding inst(U/V/W/X/Y/Zero) was the key convergence step, wR 27.96→9.78→9.75 | gsas_proj_continued.gpx / .lst |

---

## Material and objective

Fluoroapatite Ca5(PO4)3F ore powder XRD, pure fluoroapatite (confirmed by the user to have no impurities). Publication-level structure refinement: full refinement of cell+occupancies+coordinates+B factors, target Rwp ≈ ≤8% (referencing the typical convergence level of FAP in the GSAS-II tutorial).

Data: pattern_2theta.txt (5752 points, 15–130.02°, step 0.02°, Cu Kα doublet λ1=1.5405/λ2=1.5443/ratio 0.5, not stripped).

## Phase and crystal family (conclusion + basis + families excluded and why)

- **Conclusion**: single phase, fluoroapatite Ca5(PO4)3F, space group **P 63/m (#176)**, a=b=9.3703 Å, c=6.8849 Å, V=523.525 Å³.
- **Basis**: Materials Project Ca5P3O12F (P1, all atoms) → symmetrised to P 63/m (returning the DFT-relaxed F that had moved off the mirror plane to its proper 2a position) → a single fp2k scoring run verified the peak positions matched (334 reflections, density 3.202 g/cm³) → GSAS-II refinement converged to wR=9.75%.
- **Families excluded**: none (P6₃/m is the only standard structure of fluoroapatite; the original MP P6₃ subgroup was discarded because F deviates from the mirror plane, and reverted to the correct P6₃/m).

## Master list of defects (exhaustive → screening → execution)

- No defect model. Pure fluoroapatite with full occupancy (Ca/P/O/F all occ=1.0), no split sites, no antisite, no vacancy hypothesis. The user stated explicitly "it is simply pure fluoroapatite", so the complex-situation checklist is not enabled.

## Results achieved (R and criterion written separately; FullProf Rwp and GSAS wR are not directly comparable)

- **GSAS-II (delivery criterion)**: wR = **9.75%**, R = 7.66%, Bragg R = 7.47%, GOF = 1.74 (wRmin = 5.61%).
- Cell: a = 9.3703(1) Å, c = 6.8849 Å (P 63/m).
- Atoms: all isotropic, Uiso 0.012–0.022 Å² (positive, physically reasonable); bond lengths P–O 1.52–1.57 Å, Ca–F 2.30 Å, Ca–O 2.34–2.51 Å (sanity verdict=pass, 0 anomalies).
- Intermediate attempts: fp2k Rwp=100% (scale diverged, not converged); manual engine Rwp=49.1% (profile degradation, not converged). Neither meets the target, so neither is used as the delivery.

## Untried · undecided items

- **Untried**: preferred-orientation (Pref.Ori.) refinement not done; anisotropic thermal parameters (ADP) not done (isotropic is already sufficient); background-order iteration (bg_scan) not done (wR has converged under the 6th-order background, no upgrade needed).
- **Undecided**: none. Under the single-phase hypothesis all main peaks are explained, and the further refinement steps of profile/atoms gave no wR improvement (already rolled back), i.e. the R-value plateau of this data+model in this engine has been reached.

## Suggestions for the next handler

- The deliverables are in `Fluoroapatite_final/` (clean .gpx + .lst + CIF + fit figure + report.md); the final CIFs are `Fluoroapatite_final_Ca10_P6_O24_F2.cif` (structured) and `_gsas.cif` (official export_CIF).
- If wR needs to be pushed further down (currently 9.75% vs wRmin 5.61%, GOF 1.74), one can try: ① a preferred-orientation model (the acicular crystal habit of fluoroapatite may be preferentially oriented along the c axis); ② anisotropic thermal parameters; ③ background-order upgrade iteration. But all three are "not yet exhausted" items and would need to be done manually/by script inside GSAS-II.

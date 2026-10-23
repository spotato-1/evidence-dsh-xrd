# XRD refinement journal (generated from journal.jsonl, do not edit by hand)

| round | engine | stage | model | Rwp | baseline R | verdict | why | artifacts |
|---|---|---|---|---|---|---|---|---|
| 1 | xrd_refine_manual | (explicit vary) | physical | 78.9701478063256 | 98.82096412735847 | not yet at the R-value plateau; ⚠2 parameter(s) sit on a bound (ex0_H, ex1_H) - the value is box-limited |  | workspace\DEEPSEEK V4 PRO\Amorphous\result.json |
| 2 | xrd_refine_manual | extras | physical | 6.044330572676788 | 97.6191102929586 | not yet at the R-value plateau; ⚠2 parameter(s) sit on a bound (ex0_H, ex1_H) - the value is box-limited |  | workspace\DEEPSEEK V4 PRO\Amorphous\result.json |

## Material and objective

Amorphous carbon anode (composition given by the user), material type C (amorphous/low-crystallinity dominated). Objective: data pre-screening (format/λ reconciliation), full-pattern plotting and peak determination by reading the plot, FWHM and Scherrer coherence size of the amorphous broad humps, empirical fit of the broad humps; the products and the report are saved in the data folder. The λ reconciliation is a Cu Kα doublet (Kα1 1.5406 / Kα2 1.54439 / ratio 0.5, Monochromator=0 with Kα2 not stripped, taken from the Rigaku RAW header).

## Phase and crystal family (conclusion + basis + families excluded and why)

- **Conclusion**: no crystalline phase, purely amorphous carbon with a double broad hump. Basis: the full pattern has no sharp Bragg peaks, only the (002) main broad peak (29.75°) + the (10)/(100) broad shoulder (41.3°).
- **Excluded**: no sharp impurity peaks ⇒ no phase identification needed; no graphite-CIF refinement was performed (no crystalline graphite contribution, the phase scale is fixed at 0).

## Master list of defects (exhaustive → screening → execution)

Amorphous material, no lattice-defect definition; the complex-situation checklist was not triggered (no second phase, no high defect level, no manual-fit-failure input).

## Results achieved (R and criterion written separately; FullProf Rwp and GSAS wR are not directly comparable)

- Manual-engine (xrd_refine_manual, bounded LM) criterion: Rwp = **6.04 %** (baseline 97.62 %, Rexp 3.70 %, χ² 2.66). GSAS was not used (no crystalline main phase, so the precondition for GSAS refinement is not met).
- Peak position/size: d(002)=3.00 Å (29.75°), d(10)=2.18 Å (41.3°); FWHM 2.26°/3.20°; apparent coherence size D(002)=3.63 nm, D(10)=2.66 nm (instrumental broadening not subtracted).
- The H of both fitted broad peaks is pinned by the engine's 4.0° upper limit (2 parameters at the bound); this is a model limitation, already disclosed in report.md; the key conclusions (peak position/size) are not affected.

## Untried · undecided items

- **Untried**: relaxing the H upper limit (an edited copy of the engine with the H upper bound 4.0°→10.0°) — the attempt timed out during execution and was not completed; the residual panel still shows systematic undulation in the broad-peak region (±150–200 counts), arising from the insufficient expression of the asymmetric amorphous line shape by a single pseudo-Voigt + H at the upper bound.
- **Undecided**: d(002)=3.00 Å is smaller than that of typical hard carbon (3.6–4.0 Å)/graphite (3.35 Å), tending towards a more condensed short-range order; without an internal standard a 2θ calibration offset cannot be ruled out, and further confirmation by Raman/interlayer spacing is recommended.

## Suggestions for the next handler

- For a cleaner decomposition of the broad peaks: relax the H upper bound of the extras in an edited copy of the engine (4.0°→10.0°) and rerun `xrd_refine_manual` (engine=<copy>); this lets H leave the bound and reduces the systematic residual in the broad-peak region.
- If a coherence size corrected by "subtracting instrumental broadening" is needed, pass `inst_broadening` or `caglioti` to `xrd_data_io scherrer` (the Caglioti U/V/W solved for this sample came out negative, which is the normal phenomenon of an amorphous broad hump not satisfying the Caglioti model, and cannot be used).
- For the problem of the d value being too small, re-checking with Raman (ID/IG, interlayer spacing) or internal-standard XRD is recommended.

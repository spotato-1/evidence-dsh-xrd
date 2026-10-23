# Complex-case review · judgment panel (AI maintained, wholly rewritten · wrap-up version)

> Sample: NNMO (Na0.72Ni0.33Mn0.62Mo0.05O2 + Na2MoO4 impurity). The mechanical panel is in `gsas/review_mechanical_NNMO.json` (plugin maintained, do not edit by hand).
> **Status: refinement wrapped up, delivery package generated. This file is the final version.**

## I. The user's original words in the manual input window

> "workspace\GLM 5.3\LayeredOxide" contains an XRD dataset; it is a layered oxide crystal with nominal formula Na0.72Ni0.33Mn0.62Mo0.05O2 (feed ratio), raw materials NaOH, Na2MoO4·2H2O, Ni(CH3COO)2·4H2O, Mn(CH3COO)2·4H2O, citric acid; synthesis: sol-gel then ball milling, calcined at 450 °C for 5 h + 900 °C for 12 h. The material should be considered to contain some sodium molybdate impurity. Process the data strictly following the xrd plugin; the target is publication-level (R ≤ 10). Save the work under the data folder.

(Apart from this the user gave no other input; there was no manual refinement-failure report and no takeover declaration.)

## II. Current best physical solution (= the delivered solution)

- **Model**: two-phase = P2 main phase Na0.72Ni0.33Mn0.62Mo0.05O2 (P6₃/mmc, a=2.8963, c=11.1724 Å) + α-Na2MoO4 (Fd-3m, a=9.1089(2) Å).
- **Final metrics (GSAS-II, delivery package NNMO_final)**: **Rwp=13.05%, R(profile)=7.76%** (✅ ≤10), Rexp=4.97%, GOF=2.63. Manual engine corroboration Rwp=9.35%.
- **Structural key points**: Na1(2b)=0.034 + Na2(2d)=0.686 (Σ=0.72 conserved HELD); O(4f) z freely refined; MD(001)=1.475 (platelet texture); background order 12; all Uiso physical (0.005–0.02 fixed/clamped); second-phase Uij reset to literature values.
- **Deliverables**: `NNMO_final/` (figure + 2 CIFs + report + clean gpx + lst), `NNMO_REPORT.md`, `journal.md` (including the summary sections), `workflow_state.json`.

## III. Unresolved hypotheses (wrap-up leftovers, all faithfully written into the report)

1. **Rwp 13.05 vs the target 10**: the composition of the gap has been localised (under-fit of the (002) peak top ~1/3 + the expressive limit of the peak-shape parameterisation), and it was not eliminated within the range tried (27 GSAS rounds) — reported as-is per §1.3, not falsely upgraded.
2. **TM occupancy (Ni/Mn/Mo at the same site)**: in principle unresolvable by XRD, fixed at the batch ratio — needs XPS/ICP corroboration.
3. **The Na distribution 0.034/0.686 deviates from common literature values**: partly degenerate with the MD texture; the report states it according to the measurement.
4. **SH texture 12.93 not delivered** (negative Uiso, non-physical) — kept as a direction for the next handler.

## IV. Branch list (final version)

| # | Branch | Status | Evidence |
|---|---|---|---|
| 1 | P2 + Na2MoO4 two-phase (main branch) | **delivered** (NNMO_delivery.gpx → NNMO_final/) | whole chain complete, review=pass |
| 2 | SH texture (12.93 negative Uiso) | frozen · not delivered | non-physical |
| 3 | XFU fully released (13.32 negative Uiso) | frozen · not delivered | non-physical |
| 4 | O3/P3/fp2k/manual Na occupancy/old gsas project family | excluded/frozen | earlier adjudication |
| 5 | further background order upgrade (>12) | frozen | boundary=12 |

## V. Current freeze state

- **Not frozen** (frozen.active=false, the task came to a natural wrap-up). Improvement chain throughout: manual 10.19→9.35; GSAS 18.24→16.27→14.38→13.66→13.38→13.05. The last three rounds (SH/FCJ/wrap-up) confirmed the numerical basin of the GSAS parameterisation, and it was wrapped up with a faithful report per §1.3.
- No pending items afterwards; handover directions in the "handover suggestions" of journal.md.

# review_judgment.md — complex-case review judgment panel (AI maintained, wholly rewritten · final version)

## Manual input window (the user's original words)
- "workspace\GLM 5.3\LiFePO4" contains an XRD dataset; the composition is LiFePO4, and Li/Fe antisite defects should be considered. Process the data strictly following the xrd plugin, load the full complex-case checklist; the target is the lowest possible R. Save the work under the data folder."

## Current best physical solution (final version)
- Delivery package `LiFePO4_final/` (source project gsas_ops_out.gpx, wR=6.70%, GOF=1.09, wRmin=6.15).
- Pnma olivine: a=10.3244(2), b=6.0045(1), c=4.6897(1) Å, V=290.725(14) ų.
- **Li/Fe antisite (D-02, specified by the user): pair-exchange model x=0.89%** (three-conservation LS x=0.0071 → joint refinement 0.0089; fixed-x scan minimum ≈0.007 consistent; literature reference 0.0037, same order of magnitude).
- All Uiso physical (Fe 0.0137/P 0.0175/O 0.008-0.017; Li fixed at 0.005, XRD insensitive); surface-roughness correction adopted; 14th-order background.
- Bond lengths: Fe-O 2.088-2.252 / P-O 1.530-1.574 / O-O 2.407-2.599 Å (textbook-grade).

## Unresolved hypotheses (item by item · final state)
- H1 main phase Pnma — confirmed (4-Ⅰ actual run + GOF 1.09).
- H2 Li/Fe antisite — **confirmed and adopted**: x=0.89% (large uncertainty, a quoted range of 0.5-1.5% is recommended; improvement ~0.01-0.02 wR points, close to noise but consistent along both paths).
- H3 Li vacancies — pending: XRD insensitive (needs ICP/EDS).
- H4 second phase — no evidence (the residual peaks are all at main-phase peak positions).
- H5 need for negative Uiso — resolved (the root cause was a bad pure-Lorentzian peak shape; after the fix the Uiso naturally became physical).

## branch list (including frozen ones)
- branch-A (main line): Pnma → antisite → Voigt repair → joint refinement → delivery — **complete**
- branch-B: Cmcm/Pna21 — frozen (excluded at 4-Ⅰ)
- branch-E: the old bad project and its derivatives — frozen (discarded; the diagnostic records of rounds 9-11 are retained)

## Current freeze state
- Not frozen. The whole workflow is complete and the deliverables are in place; awaiting the user's confirmation of the wrap-up cleanup scope.

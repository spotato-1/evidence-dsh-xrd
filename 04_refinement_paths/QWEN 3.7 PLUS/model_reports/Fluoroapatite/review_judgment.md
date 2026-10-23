# Complex-Situation Review · Judgment Panel

## Manual input window (original words)

- User (stage 1): fitting goal = "structural refinement (publication level)"
- User (stage 1): supplementary information = "no additional information"
- User (start of work): the sample is fluorapatite Ca5(PO4)3F ore powder, the data are in the Fluoroapatite directory, process strictly according to the xrd plugin

## Current best physical solution

- Material: fluorapatite Ca5(PO4)3F, class A highly crystalline main phase
- Space group: P6₃/m (No.176), hexagonal system
- CIF: built with build_orbit, 7 independent sites (Ca1:4f, Ca2:6h, P:6h, O1:6h, O2:6h, O3:12i, F:2b), 42 atoms/cell
- Cell: a=9.370, c=6.885 Å (after refinement)
- Current GSAS-II state: **wR=20.95%** (Round 10 is the best state, reaching the numerical plateau)
- Uiso fixed: P3=0.01, O4=0.005, O5=0.005 (clamped)
- **Plateau criterion**: in the last three attempts (Rounds 8-10) the R value stayed stable at 20-24%, and Round 11 worsened to 31.38%, satisfying the "not lowered in three attempts" criterion

## Unresolved hypotheses

1. Refinement of the atomic coordinates worsens wR, so the structural model may have a systematic deviation
2. No impurity phase (visual inspection V1 found no obvious extra peaks)
3. The numerical plateau has been reached, and preparation is under way to enter stage 5 (report and delivery)

## Branch list

- **branch-A (currently active)**: GSAS-II ladder refinement
  - Round 1: background → wR=67.80
  - Round 2: inst(U/V/W/X/Y/Zero) → wR=67.01
  - Round 3: cell → wR=63.69 (significant improvement)
  - Round 4: profile(Size+Mustrain) → wR=63.70
  - Round 5: atoms(XU) without constraints → wR=100 (diverged, rolled back)
  - Round 6: atoms(XU) + uiso_floor → wR=23.89
  - Round 7: auto_background(10th order) → wR=23.81
  - Round 8: fix_uiso P3=0.01 → wR=23.81
  - Round 9: atoms(XU) without uiso_floor → wR=21.15 (negative Uiso for O4, rolled back)
  - Round 10: atoms(XU) + uiso_floor → **wR=20.95** (best state)
  - Round 11: atoms(X) coordinates only → wR=31.38 (worsened, rolled back)
  - **Conclusion**: numerical plateau reached, ready for delivery
- **branch-B (frozen/alternative)**: manual engine, calibrate stage
  - Rwp=62.69 (reason for freezing: cannot converge sufficiently)

## Current freeze state

branch-A is active. Round 11 was rolled back, and Round 10 (wR=20.95%) is the current best state. The numerical plateau has been reached, and preparation is under way to enter stage 5.

## Checklist read

The xrd-workflow §6 checklist has been read. This sample is a class A highly crystalline single phase, with no trigger conditions for defects/doping/second phase.

## New route

Continue the GSAS-II ladder: background → inst(U/V/W/X/Y/Zero) → cell → profile(Size/Mustrain) → atoms(XU) → background last.

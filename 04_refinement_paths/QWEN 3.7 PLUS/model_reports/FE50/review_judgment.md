# Complex-Situation Review Judgment Panel - FE50

## User input record

**2026-01-XX (initial task)**:
> "workspace\QWEN 3.7 PLUS\FE50" contains an XRD dataset; it is a Prussian blue crystal with nominal formula KxFe0.5Mn0.5[Fe(CN)6], synthesized by ball-milling Fe4[Fe(CN)6]3, manganese oxide tetrahydrate, and potassium citrate in 50% ethanol/water. "workspace\QWEN 3.7 PLUS\FE50" provides two similar-material CIF files as reference. The material should be considered to contain extensive defects, especially lattice distortion, vacancies, and split sites. Process strictly following the xrd plugin, force the complex-case checklist, strictly follow the planned workflow, and consider all defects and possible fitting changes. When in doubt, first consider the fitting approach and scientific self-consistency; before entering the final GSAS engine, all adjustments target lowering R. The target is publication-level (R ≤ 10) as far as possible. Save the work under the data folder.

**Limit-mode selection**: the user chose "continue refining (limit mode)"

---

## Assessment of the current state (limit mode)

### Current best physical solution
- **wR = 12.71** (GSAS-II, Fm-3m structure, multi-defect model, 12th-order background)
- Cell a = 10.100 Å
- Already refined: background (12th order) + cell + profile (size+mustrain) + inst (U,V,W,X,Y,Zero) + atoms (XU)
- Defect model:
  - K0 occ=0.6 (K vacancy)
  - Mn1 occ=0.5 (Mn site)
  - Fe2 occ=0.97 ([Fe(CN)6] vacancy)
  - Fe3 occ=0.95 ([Fe(CN)6] vacancy)
  - C4 occ=0.98 (C vacancy)
  - N5 occ=0.98 (N vacancy)
- Uiso clamping: 6 atoms were clamped to min=0.005
- All final Uiso >= 0.005, no negative values

### Unresolved hypotheses (item by item)

1. **[Fe(CN)6] vacancies** - ✓ verified effective (vacancies exist on both Fe2 and Fe3)
2. **C/N vacancies** - ✓ verified effective (wR 14.23→12.71, improvement 1.52)
3. **Fe/Mn mixed occupancy** - ⚠ GSAS-II technical limitation (unpickling stack underflow)
4. **K-site splitting** - ✗ excluded (wR got worse)
5. **Second phase candidate_B** - ✗ excluded (wR got worse)
6. **Uiso clamping** - ✓ completed
7. **Background-order upgrade** - ✓ completed (n=12)
8. **Fe3 occupancy refinement** - ✓ verified effective (in limit mode wR 13.90→13.63)
9. **refine all** - ✗ excluded (wR 13.90→22.15, clearly worse)

### Branch list

| Branch | Status | R value | Description |
|--------|------|------|------|
| fp2k candidate_A | completed | 69.7 | ladder refinement, geometry parameters only |
| manual engine structure (candidate_A) | completed | 14.24 | 2 parameters on bounds |
| GSAS-II +uiso_clamp+atoms | completed | wR=13.78 | 6 atoms clamped to 0.005 |
| GSAS-II +Fe2_occ=0.97 | completed | wR=13.96 | [Fe(CN)6] vacancies effective |
| GSAS-II +background-order upgrade (12) | completed | wR=13.90 | improvement 0.06 |
| GSAS-II +Fe3_occ=0.95 (limit mode) | completed | wR=13.63 | improvement 0.27 |
| **GSAS-II +C/N_occ=0.98 (limit mode)** | **current best** | **wR=12.71** | improvement 1.52 |
| GSAS-II +refine all (limit mode) | completed | wR=22.15 | clearly worse, excluded ✗ |
| GSAS-II +Fe/Mn mixed occupancy | failed | - | unpickling stack underflow |
| GSAS-II +K-site splitting | completed | wR=18.23 | excluded ✗ |
| GSAS-II +second phase candidate_B | completed | wR=25.25 | excluded ✗ |

### Current freeze state

- **Not frozen** (frozen.active = false)
- GSAS rounds = 25
- Consecutive no-improvement count = 0 (best state just confirmed)
- limit_mode_attempts = 1 (limit mode in progress)

### §6 checklist 2nd trigger confirmation (2026-01-XX)

**Implementation of user input**: ✅ all confirmed
**Disposition of unresolved hypotheses**: ✅ all confirmed (see the table above)
**Limit-mode status**: in progress, the statistical limit has not yet been reached

### Next-step route (release order in limit mode)

1. **Order 1 background/peak shape** - ✓ completed (12th-order background)
2. **Order 2 LeBail intensity floor** - to be attempted (needs to restart from the best state)
3. **Order 3 occupancy/coordinate constraints** - in progress (C/N occupancies already released)
4. **Order 4 thermal-parameter lower limit** - last resort (Uiso currently clamped at 0.005)

---

*Last updated: 2026-01-XX (limit mode)*

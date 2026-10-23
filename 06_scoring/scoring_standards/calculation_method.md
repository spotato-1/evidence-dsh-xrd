# DSH-XRD Two-Set Benchmark Calculation Method

- Fixed date: 2026-10-13 (Asia/Shanghai).
- Materials: Amorphous, Fe2O3_Fe3O4_2ph, Fluoroapatite, FE50, LayeredOxide, LiFePO4.
- Compared models: GPT 5.6 SOL, GLM 5.3, QWEN 3.6 FLASH, QWEN 3.7 PLUS, QWEN 3.8 MAX, DEEPSEEK V4 PRO. Kimi is excluded.
- The two benchmark sets are computed independently. Set 2 outputs three percentage metrics (answer, time, cost); they are not summed into a total.

## Set 1: Full Agent Capability

Each model is tested on six materials; each material is scored on six directions A–F, giving 36 scoring cells.

| Direction | Content | Per-material scoring |
|---|---|---|
| A | Workflow loading, route, stage order, checklist, state handoff | five items, each 0 or 1 |
| B | Whether a red line in the plugin core skill was violated | 5 if no confirmed violation, 0 if any confirmed |
| C | Call purpose, judgment transitions, using feedback, avoiding idle calls, reasonable stopping | five items, each 0 or 1 |
| D | Method, structure/composition, scientific question, numerical consistency, conclusion boundary | five items, each 0 or 1 |
| E | Hypothesis basis, testability, CIF/model, initial values, correction choices | five items, each 0 or 1 |
| F | Tool use, input, state understanding, troubleshooting, handoff/export | five items, each 0 or 1; whole-cell 0 on confirmed misuse |

For model m and direction a, the direction total is S_{m,a} = Σ_{i=1..6} s_{m,i,a}, with 0 ≤ S_{m,a} ≤ 30. Percent form: S^{100}_{m,a} = S_{m,a}/30 × 100. The six directions are not weighted and not summed into a composite ranking.

### Set 1 boundary rules

- Background-order errors are recorded under A3 and do not trigger B or auto-deduct Set 2.
- B is based only on the red lines actually provided in the plugin core skill at run time; B=5 means no confirmed violation, not that all scientific results are correct.
- Cleanup is judged by the historical core clauses: no cleanup during analysis/refinement; keep logs, named fit records, and final outputs; ask first when uncertain; honor the user's keep decisions.
- Multiple red-line violations in one case still zero B only once (B is a whole-cell 5/0 gate, not five independent penalties).
- F misuse is separate from B; historical authorized automatic FP2K iteration is not automatically misuse.

## Set 2: Answer score

The answer score = result accuracy (50) + material key questions (50).

### 1. Result accuracy (50)

Six materials are weighted equally; five items per material (D1–D5), each 1 or 0:

- D1: method boundary, main phase, or applicable model correct.
- D2: structure, site, multiplicity, composition, occupancy, and physical conditions self-consistent.
- D3: correctly answers the key scientific question required for that material.
- D4: reported values and metric definitions match the delivered products.
- D5: correctly distinguishes fixed priors, fitted values, model-dependent values, and open items.

Accuracy for model m, material i: d_{m,i} = Σ_{p=1..5} x_{m,i,p}. The accuracy part is R_m = (50/30) × Σ_{i=1..6} d_{m,i}. Each material contributes at most 50/6, each accuracy item 50/30 = 5/3, and the six materials sum to at most 50. This is discrete item scoring, not an Rwp-derived or mean-percentage-error score.

### 2. Material key questions (50)

Ten key questions, each up to 5 points:

| Material | Key questions | Cap |
|---|---|---|
| Amorphous | K01: amorphous method boundary and decomposition non-uniqueness | 5 |
| Fe2O3_Fe3O4_2ph | K02: credible two-phase fit and ratio under strong background | 5 |
| Fluoroapatite | K03: CIF symmetry, multiplicity, stoichiometry, coordination | 5 |
| FE50 | K04: reference-CIF transfer; K05: cubic/monoclinic decision; K06: sustained optimization and reasonable closure | 15 |
| LayeredOxide | K07: verify sodium-molybdate impurity; K08: composition, two-phase content, element-balance self-consistency | 10 |
| LiFePO4 | K09: structure and antisite conservation; K10: antisite identifiability and parameter coupling | 10 |
| Total | ten questions | 50 |

Each key question (except K06) is scored on five points, one each: (1) identify the problem from the data rather than repeating the prompt; (2) propose a suitable model, constraint, or control; (3) deliver verifiable parameters, calculation, project, or control; (4) accept, revise, roll back, or retain a judgment based on evidence; (5) state fixed parameters, scope, and conclusion boundary.

The answer total is Q_m = R_m + P_m = (50/30)Σd + Σk.

### 3. Weighting

Only the accuracy part is six-material-equal-weight; the whole answer score is not. FE50 carries more key-question points (15) than amorphous/two-phase iron oxide/fluoroapatite (5 each) or layered oxide/LiFePO4 (10 each).

## Time and cost

### 1. Normalize per material, then average over six materials

For material i, take the maximum over the fixed six-model set: t_ref,i = max_m t_mi and c_ref,i = max_m c_mi. When the reference maximum is positive, T_mi = 100(1 − t_mi/t_ref,i) and C_mi = 100(1 − c_mi/c_ref,i). Overall T_m = (1/6)Σ_i T_mi and C_m = (1/6)Σ_i C_mi.

The maximum consumer gets 0; the smallest positive consumer need not get 100 (this is not min–max stretching). The maximum is a comparison reference, not a preset quota or stop threshold.

### 2. Time

Recorded model generation, tool execution, service waits, and retries are included; recorded human waits and idle intervals are excluded. Main-session and sub-agent active intervals are unioned (parallel overlap counted once). The time is the total duration of the active-interval union, not pure model compute time.

### 3. Cost

Each request is split into mutually exclusive ordinary input, cache-read, chargeable cache-write, and output tokens, priced per provider tier (USD per million tokens), converted at the frozen exchange rate, and summed for the material's main model and sub-agent requests.

- Sub-agents are priced by their actual model, not the main model.
- Cache categories are not double-counted against ordinary input.
- Cost is reported as "official API-equivalent cost", not account charges.
- Failed requests with no returned usage are marked as a measurement gap, not inferred as free.

## Missing, failure, and final output

- Confirmed no-delivery or unprocessed items: 0.
- Evidence that should exist but is unavailable or undecidable: NA (not auto-0 or auto-1).
- Incomplete runs keep their consumed time and cost, but a high resource score only means low consumption, not successful delivery.
- Internal values are unrounded; final display is rounded uniformly.

Each model delivers: (1) Set 1 A–F totals (each ≤30); (2) Set 2 answer/100, time/100, cost/100 with raw hours and USD; (3) per-item judgments, evidence locators, brief reasons, and unknowns, with B/F gates listed separately.

The two benchmark sets are not summed; the three Set 2 metrics are not summed into a composite ranking.

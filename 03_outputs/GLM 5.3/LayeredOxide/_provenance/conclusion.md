The refinement task is complete. The following is the final summary:

---

## NNMO (Na₀.₇₂Ni₀.₃₃Mn₀.₆₂Mo₀.₀₅O₂) XRD refinement · Final report

### I. Phase identification conclusions

| Phase | Space group | Cell | Basis |
|---|---|---|---|
| **main phase: P2-type layered oxide** | P6₃/mmc | a = 2.8963 Å, c = 11.1724 Å | all 11 significant peaks indexed; crystal-family adjudication P2 (10.19, clean convergence) vs O3 (16.40, five parameters at the bound); P3 excluded by peak positions |
| **impurity: α-Na₂MoO₄** | Fd-3m | a = 9.1089(2) Å | characteristic peaks at 27.50°/32.46° (220/311); COD 2240655 (neutron-refined structure, coordination numerically verified) |

### II. Final metrics (GSAS-II two-phase Rietveld)

| Metric | Value | Note |
|---|---|---|
| **R (profile)** | **7.76 %** | ✅ **meets the publication-level target R ≤ 10** |
| Rwp (wR) | 13.05 % | 10 not reached; the make-up of the gap has been located and is reported as-is |
| Rexp / GOF | 4.97 % / 2.63 | fit quality not yet at the statistical limit |
| manual engine Rwp (corroborating) | 9.35 % | bounded LM, Poisson convention |

**Truthful note on the Rwp gap**: the residual concentrates in a general under-fitting of the apexes of the main peaks (the (002) single peak contributes about 1/3), and the root cause is the expressiveness limit of laboratory data under this peak-shape parameterisation (U/W, X/Y, SH/L/Zero are all 99%+ correlated); this was exhausted over 27 GSAS iterations (including texture, background order 6→12, conserved occupancies, FCJ probes)——reported as-is as the workflow requires, not overstated.

### III. Structural highlights

- **Na distribution**: Na1(2b) = 0.034 + Na2(2d) = 0.686, **Σ = 0.72 conservation constraint (measured HELD)**
- **Texture**: March-Dollase (001) = 1.475 (plate-like particles textured along the c axis, significant)——confirmed and adopted
- **O 4f z** freely refined; **all Uiso physically positive** (negative values had appeared; fixed with the trio of equivalence constraints + clamping + occupancy conservation)
- **TM site (Ni/Mn/Mo)**: XRD is in principle unable to resolve the proportion of same-site cations, so it is fixed at the nominal feed ratio (the report notes that XPS/ICP corroboration is needed)
- impurity phase fraction ≈ 0.018 (Rietveld phase-fraction ratio)

### IV. Deliverables (all under the data folder)

- **`NNMO_final/`** — delivery package: fit figure (V4 check, no occlusion), two-phase CIF (GSAS official export), clean project + lst, report.md
- **`NNMO_REPORT.md`** — final report (phase identification, metrics, structure parameters, honesty statements, coverage statements, failure classification)
- **`xrd_workflow/journal.md`** — 12-round per-round record + summary chapter (material/phase families/defect master table/results achieved/untried items/hand-over suggestions)
- **`workflow_state.json` / `review_judgment.md`** — state protocol and review record
- Process directories (cand, gsas2, manual_*, etc.) **all retained** per your choice

If Rwp needs to be pushed lower, the suggested directions (already written into the journal hand-over suggestions): add synchrotron/neutron data, or manually tune the peak shape peak-by-peak in the GSAS GUI (the script layer has reached its parameterisation limit).

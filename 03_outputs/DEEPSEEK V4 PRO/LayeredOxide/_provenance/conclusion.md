Refinement complete, and the **publication-level target has been reached (GSAS wR = 9.82% ≤ 10)**. The full results follow.

## Conclusion

The main phase of this sample is the **P2-type layered oxide Na₀.₇₂(Ni₀.₃₃Mn₀.₆₂Mo₀.₀₅)O₂**, and it also contains a significant amount of **Na₂MoO₄ impurity** (about 24.8 wt%).

| Phase | Space group | Cell |
|---|---|---|
| Main phase | P 6₃/m m c (194) | a = 2.8889(5) Å, c = 11.1340(5) Å, V = 80.47 Å³ |
| Impurity Na₂MoO₄ | F d -3 m (227) | a = 9.1089 Å (fixed, COD 2240655 neutron structure) |

**Fit quality**: wR = **9.82%** (✅ ≤10), R = 6.68%, Rb = 14.49%, GOF = 1.98, wRmin = 4.97%.

**Key structural parameters** (main phase): O z = 0.0971(28); Na occupancy Na(2b)=0.283 / Na(2d)=0.437 (conserving 0.72, mainly occupying the 2d face-sharing site); the TM site (2a) is mixed-occupied by Mn/Ni/Mo, with an equivalent-Uiso constraint.

## Key process points

1. **Phase separation and identification**: the data are Rigaku Cu Kα (doublet, Kα2 not stripped); the criterion for the P2 main phase is a first peak at 15.77°=(002) and no O3 (003); `polymorphs` was used to fetch several NaMnO₂ polymorphs, and P6₃/mmc was selected.
2. **Two-phase refinement**: the manual engine established the two-phase solution → GSAS-II finished with a two-phase ladder.
3. **Key troubleshooting**: midway the GSAS instrument parameters U/V/W/X/Y/Zero **diverged to absurd values** (U=-20232), leaving wR stuck at 13.6%; after they were reset to physical values and X/Y were fixed, wR dropped abruptly from 13.58% to 10.16% and finally converged to 9.82%.
4. **Physical constraints**: Na occupancy conservation (conserve_afrac), equivalent Uiso at the TM site (equiv_uiso), negative-Uiso clamping (uiso_floor), and impurity thermal parameters fixed at the COD neutron values.

## Deliverables (inside the data folder)

- `LayeredOxide_final/` — delivery package (clean .gpx, .lst, fit figure, per-phase CIF, machine report)
- `REFINEMENT_SUMMARY.md` — full summary report (including the coverage statement and the defect summary table)
- `defect_table.json` — per-sample defect checklist (§6.9)
- `workflow_state.json` / `xrd_workflow/journal.jsonl` — state and logs
- `main_P2_orbit_01.cif`, `cod_2240655.cif`, `INST_CuKa.instprm` — key inputs

## Honesty statement

The target (wR ≤ 10) **has been reached**, but the coverage is not exhaustive: dimensions such as interlayer cation mixing, oxygen vacancies and higher-order background were **untried** (the information content of the data is insufficient to resolve them independently), and this is written out item by item in the coverage statement of `REFINEMENT_SUMMARY.md` — it is not "impossible to improve". The Uiso at the Na(2b) site is somewhat large at ≈0.059 Å² (esd≈0.05, within 2σ), the thermal parameter of a low-occupancy Na site being inherently uncertain, and this has been flagged in the report.

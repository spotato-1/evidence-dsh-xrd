 ## Refinement complete

FE50's structure screening, bounded manual optimisation, GSAS-II refinement, defect testing and delivery review have been completed in strict accordance with the dsh-xrd five-stage workflow, the three-part process of stage ④, and the complex-problem checklist.

### Final results

The **P2₁/c monoclinic average-structure model** was finally adopted:

- **GSAS-II wR: 11.7347%**
- R: 9.2024%
- Rb: 11.9631%
- wRmin: 7.9169%
- Cell:
  - a = 10.2552 Å
  - b = 10.1515 Å
  - c = 10.1646 Å
  - β = 92.283°
  - V = 1069.331 Å³

The target wR≤10% was **not reached**, falling short by about 1.73 percentage points. The R value was not forcibly pushed down through non-physical occupancies or negative thermal parameters.

Final project review passed:

- all atoms use isotropic ADP;
- Uiso = 0.01 Å²;
- no negative Uiso/Uij;
- final occupancies are all within the physical range;
- the GSAS project reopens normally, and the cached wR is verified as 11.73%.

### Main model conclusions

- The monoclinic model is superior to the Fm-3m model in both manual fitting and theoretical peak matching.
- The lowest valid result of the bounded manual engine is:
  - Rwp = 10.6165%
  - Rexp = 7.8829%
  - χ² = 1.8138
- This manual model contains three empirical broad-peak proxies; its values cannot be interpreted as crystalline phase fractions.
- Free refinement of the Fe/Mn occupancy produced huge positive and negative values, proving that routine PXRD on this sample set cannot determine the Fe/Mn ratio independently, so the nominal 0.5/0.5 was finally fixed.
- Refining a single N vacancy produced a negative occupancy; the coupled Fe/C/N vacancy model, although physical, did not lower wR. Vacancies may therefore exist, but they cannot be reliably quantified from the current data.
- Neither of the two fixed geometries of 1.3 Å and 1.5 Å for the K split site improved the fit; the free scheme suffered a constraint error. The only possible conclusion is "the current data cannot resolve it"; it must not be claimed that no split site exists.
- Neither isotropic size nor microstrain improved the fit; anisotropic broadening, stacking faults and secondary phases have still not been exhausted.

### Final delivery package

Main delivery directory:

`workspace\GPT 5.6 SOL\FE50\deliverables\FE50_final`

Contains:

- `FE50_final.gpx`: final GSAS-II project
- `FE50_final.lst`: refinement log
- `FE50_built.cif`: CIF officially exported by GSAS-II
- `FE50_fit.png`: fit figure, residuals and reflection ticks
- `FE50_report.md`: GSAS-II parameter report
- `FE50_scientific_assessment.md`: scientific conclusions, defect assessment, limitations and follow-up recommendations
- `FE50_finalize.json`: delivery packaging record

Recommended reading, in priority order:

- `FE50\deliverables\FE50_final\FE50_scientific_assessment.md`
- `FE50\xrd_workflow\journal.md`
- `FE50\defect_table.json`

### Workflow and audit files

- `FE50\workflow_state.json`: final state and the entire refinement trace
- `FE50\xrd_workflow\journal.jsonl`: machine-readable round-by-round log
- `FE50\xrd_workflow\journal.md`: complete human-readable summary
- `FE50\phase_summary.json`: crystal-family selection and the basis for exclusion
- `FE50\defect_table.json`: item-by-item checklist of 14 classes of defects
- `FE50\review_judgment.md`: complex-case judgement panel
- `FE50\gsas\best_physical\FE50_best_physical.gpx`: the physical project that should be used to continue refinement
- `FE50\gsas\final_audit\FE50_final_audit.gpx`: audit copy of the final parameters

### Points to note

The delivered figure passed the V4 check, and readability and annotation hygiene are acceptable, but systematic residuals still remain at about 17°, 25°, 28–30°, 35°, 39–43°, 46–48° and 56–58°. The current result is therefore suitable as a **best physical average structure and diagnostic delivery**, and it is not appropriate to claim that all local-structure or secondary-phase problems have been solved.

The CIF bond-length check still flags anomalous C–N and metal–N geometries. This is mainly inherited from the reference monoclinic CIF; the atomic coordinates were not reliably refined under bond-length constraints. The current CIF is therefore suitable for reporting the space group, cell and nominal site topology, but is not appropriate to publish directly as a complete local bond-length structure.

If wR≤10% is to be pursued further, the most effective next step is to provide:

1. measured XRD/CIF of the original Prussian blue and MnO₂;
2. K/Fe/Mn composition from ICP;
3. water and cyano content from CHN/TGA;
4. Mössbauer or XAS/PDF;
5. elemental spatial distribution from STEM-EDS.

Then, along the prescribed route of "manual bounded two-phase ratio → handoff → GSAS-II", add the residual PB, MnO₂ or a second PBA phase, rather than continuing to release occupancies without constraints.

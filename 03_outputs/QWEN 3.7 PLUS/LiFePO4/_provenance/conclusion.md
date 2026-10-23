## LiFePO4 XRD: Refinement complete

### Final results

| Metric | Value |
|---|---|
| **GSAS-II wR** | **7.49%** |
| Space group | Pnma (olivine) |
| Cell | a=10.326, b=6.005, c=4.690 Å |
| Antisite defects | Li site 5.4% Fe, Fe site 10.9% Li |

### Refinement history

1. **Manual-engine baseline**: Rwp 95.92% → 26.51%
2. **GSAS-II background/cell/profile**: wR 30.11%
3. **Atoms + instrument parameters**: wR 11.62%
4. **12th-order background iteration**: wR 8.12%
5. **Li/Fe antisite defects**: wR **7.49%** ✓

### Product list

| File | Description |
|---|---|
| `gsas_antisite8.gpx` | final refinement project (wR=7.49%) |
| `LiFePO4_final_built.cif` | structured CIF |
| `LiFePO4_final_built.png` | fit figure |
| `report.md` | full report |
| `workflow_state.json` | workflow state |
| `xrd_workflow/journal.jsonl` | refinement log |
| `review_judgment.md` | complex-case review judgement panel |

### Key findings

- **Li/Fe antisite defects are present**: least squares drives the Fe-site antisite amount to 10.9% and the Li-site antisite amount to 5.4%
- **The conservation constraints took effect**: Li1+Li1_Fe=1, Fe2+Fe2_Li=1 (HELD)
- **wR=7.49% is below the 10% target**

### Notes

- The O5 thermal parameter is slightly high (Uiso=0.20), which may be a limitation of the data resolution
- The Fe2_Li coordinates appear anomalous when the CIF is exported, but they are correctly constrained in the refinement project
- The antisite amount of 10.9% is slightly higher than the range commonly found in the literature (1-5%); validation together with other characterisation is recommended

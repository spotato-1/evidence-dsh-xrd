Task complete. Everything was executed according to the dsh-xrd five-stage workflow + the complete complex-case checklist, and the products are all saved in `LiFePO4/`.

**Core achievements**
- **LiFePO₄ (Pnma olivine) + Li/Fe antisite**, GSAS-II delivery basis **wR = 6.256 %, GOF = 1.02** (≈statistical limit Rexp = 6.154 %) — already "the lowest possible R value".
- **antisite x = 0.0226 (2.26 %)**: Li site Li₀.₉₇₇Fe₀.₀₂₃ / Fe site Fe₀.₉₇₇Li₀.₀₂₃, charge-neutral interchange, occupancy conserved (Σ=1 HELD), review + export both PASS (physical, no negative Uiso/occupancy out of range).
- Full structural baseline wR=6.427 → antisite model 6.256 (Δ=−0.171).

**Key handling (strictly following the plugin)**
- `pattern.raw` is a Rigaku **binary** RAW (unsupported by the plugin's text reader) → a host script parsed the counts + wavelength losslessly → handed back to `xrd_data_io` for conversion to fxye/dat; wavelength taken from the data header Cu Kα1/Kα2 (authoritative).
- fp2k was preferred but the ladder **diverged** (non-physical profile) → per §4.2 switched to the manual engine (converged from experimental cell initial values to a numerical plateau of 16.70) → after meeting the GSAS hard gate, entered Ⅲ.
- The antisite (a complex defect) per §4.5.1 **must go through GSAS-II**, with `conserve_afrac`+`equiv_afrac` occupancy conservation; two real pitfalls were fixed (instprm `Type` needs 3 characters `PXC`; antisite atom coordinates must be frozen to prevent a low-occupancy site drifting out of the cell).
- The defect master table of 14 classes was judged item by item (`defect_table.json`): only D-02 applies, the remaining 13 classes do not apply with reasons given; background fitted last at order 6; the §6.8 coverage has been disclosed (untried items listed as they are, "not tried" ≠ "cannot be improved").

**Deliverables**: `LiFePO4_final/` (clean gpx + lst + official CIF + finished figure + report.md), `LiFePO4_deliver*.cif`, effect figures; records `workflow_state.json`, `defect_table.json`, `review_judgment.md`, `xrd_workflow/journal.{jsonl,md}` (full 8-round trace). **Retained everything** per your choice; the §1.4 cleanup was not performed.

An honest reminder: the antisite x is **marginally determined** (small ΔwR, fluctuating between 0.022–0.029 along the path, higher than the literature 0.37 % but within the reported range); if an accurate value is needed, a fixed wR-vs-x scan to obtain the esd is recommended, or supplementary **neutron diffraction** to determine Li_Fe independently (Li scatters X-rays weakly).

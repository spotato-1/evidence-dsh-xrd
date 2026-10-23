# review_judgment.md — LiFePO4 (complex-situation review · judgement column; written by the AI, rewritten as a whole, the mechanical column is not modified)

## Human input (the user's verbatim words)
"workspace\QWEN 3.8 MAX\LiFePO4" contains an XRD dataset; the composition is LiFePO4, and Li/Fe antisite defects should be considered. Process the data strictly following the xrd plugin, load the full complex-case checklist; the target is the lowest possible R. Save the work under the data folder."

## Current best physical solution (delivered)
- **Main phase**: Pnma olivine LiFePO4 (single phase; V1 image reading shows no impurity peak; polymorphs exhaustively enumerated 26 structure types, Pnma is the ground state and wins the actual-run adjudication).
- **Li/Fe antisite (D-02, requested by the user)**: x = Fe_Li = Li_Fe = **0.0226 (2.26%)**; the Li site Li₀.₉₇₇Fe₀.₀₂₃, the Fe site Fe₀.₉₇₇Li₀.₀₂₃ (charge-neutral interchange, Σocc=1 HELD for both sites).
- **GSAS-II delivery protocol**: **wR = 6.256%**, Rexp/wRmin = 6.154%, **GOF = 1.02**, Rp = 4.888%, Rb = 5.250%; χ²≈1.03 → **the statistical limit has been reached**.
- **Cell**: a=10.3252, b=6.0051, c=4.6901 Å, V=290.80 (Pnma).
- **Physicality**: all occupancies within (0,1], all Uiso positive (Li0/O4 clamped to 0.005), the antisite atoms' coordinates frozen at the host sites (no drift); gsas_ops review **PASS** + export_cif verdict **PASS** (bond lengths Fe/Li-O 2.03–2.28, P-O 1.49–1.64, O-O 2.40–2.59 Å all physical).
- **Wavelength**: Cu Kα1=1.5405930/Kα2=1.5444140 (authoritative from the data header), intensity ratio 0.5 (not stored in the header→Cu standard, annotated).

## Unresolved hypotheses (item by item)
- **The precise value of the antisite x carries uncertainty**: ΔwR (complete 6.427 → antisite 6.256) is only -0.171, which is marginal; x fluctuates between 0.022–0.029 along different refinement paths. x=2.26% is higher than the literature's 0.37% but within the reported range. **Not done**: a fixed wR-vs-x scan to determine the uncertainty, taking the esd of x from the .lst, and independently determining Li_Fe by neutron diffraction (Li is weak for X-rays).
- **Size/Mustrain ↔ instrumental X/Y 100% collinear**: sample broadening and instrumental broadening cannot be resolved separately; the sample peaks are sharp (FWHM 0.11–0.18°), so the sample broadening is negligible and the Size/Mustrain values are non-unique (this does not affect the uniqueness and physicality of the cell/occupancies/Uiso).
- The other 12 defect classes (D-01/03/04/05/06/07/08/09/10/11/12/13/14) are all judged **not applicable**, with reasons in defect_table.json (the complete structure already reaches GOF=1.02, with no corresponding signal).

## Branch list (including frozen ones)
- **fp2k (FullProf)** [abandoned · numerical failure]: baseline Rwp=97.4 (nominal, but RF=9.34/density 3.611 = the structure is correct); the ladder diverges and stops at 58.6 (V→-3.19 at the bound, FWHM²<0@42°, B=-0.43). → switch to manual.
- **Manual engine** [plateau · corroborating evidence]: calibrate 26.65 (V/eta at bounds) → releasing abc (GGA cell) diverges to 37.45 → **experimental-cell initial values 16.70 plateau (plateau)**. Diagnosed that the GGA cell is ~1% too small and that zero compensates for it. Used as the GSAS gate.
- **GSAS-II complete structure** [R_before]: ladder bg19.68→inst10.33→cell7.23→profile7.23→atoms6.41; uiso_floor clamping → **wR=6.427** (clean physical baseline). Fixed instprm Type CR→PXC (GSASIIstrIO:3007 IndexError).
- **GSAS-II antisite attempts** [partially frozen]: defect_refined (equiv overridden by conserve→occupancies run away, Fe1_Li<0, wR6.315 unphysical); defect2 (dual equiv host+swap degenerate with scale→Invalid metric tensor singularity); defect3 (mult[1,-1] sign inverted→Fe1_Li<0); defect4/5 (mult[1,1] but the antisite atoms carry the X flag→coordinates drift out of the cell, export fail).
- **GSAS-II antisite (adopted)** [current best · delivered]: defect6 = conserve→equiv(mult[1,1]) + **all coordinates frozen** → wR=6.256, x=0.0226, review PASS; auto_background (6th order, last) → deliver; export PASS; finalize GOF=1.02.

## Current freeze status
**No freeze**. Stage ④-Ⅲ + ⑤ are complete, the objective is achieved (wR=6.256%≈Rexp, the antisite is physical and both PASS). no_improve_streak=0, limit_mode_attempts=0 (limit mode not triggered: the complete checklist did not reach 3 times before the target was met). To do: ask the user about the scope of the close-out cleanup (§1.4).

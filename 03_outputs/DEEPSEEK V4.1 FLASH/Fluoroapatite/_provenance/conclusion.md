The state file has been repaired and passes strict JSON validation (this is exactly what the plugin's §2/§8.5 requires — "self-validate immediately after writing; a parse failure must not be silent" — I followed it, and did not continue carrying a bad file).

## Final delivery

**Fluorapatite ore powder = single-phase hexagonal Ca₅(PO₄)₃F (P6₃/m)**, GSAS-II refinement **wR = 9.70 %, GOF = 1.74** (wRmin = 5.61 %), cell a = 9.3705(1) Å, c = 6.8849(0) Å.

The core outputs are in `FAP_final\`:

- `FAP_final.gpx`, `FAP_final.lst`, `FAP_Ca5_F_O12_P3.cif` (official GSAS export)
- `FAP_fit.png` (obs/calc/residual + per-phase reflection ticks + hkl labels)
- `FAP_report.md` (metrics / cell with esd / atom parameters / strong-reflection table)

The working record is in `xrd_workflow\journal.jsonl` + `journal.md` (12-round trajectory, defect master table, coverage statement, closing state), `workflow_state.json`, `review_judgment.md`.

## Three points in this task most worth your attention

1. **The "low-angle impurity peaks" were a false alarm** — theoretical calculation confirms that the three peaks at 16.82/21.84/22.88° are fluorapatite's own reflections; the sample is **single-phase**, not a mixture.
2. **The real bottleneck is the CIF source** — all three fluorapatite CIFs in COD are 1940s powder data and none contains Biso; the P–O bond length of the original coordinates is 1.817 Å (physical value ≈1.53). After releasing coordinates + Uiso in GSAS-II, wR fell straight from 24.01 % to 10.11 %; the P–O in the finally delivered CIF is back to 1.531–1.581 Å.
3. **The FullProf leg never worked, and I did not disguise that** — all five candidates stalled at Rwp 92–100 %. I ran control experiments to localize it (a 40× scale made it worse → not a single-scaling problem), classified it as numerical + model-related, and per the workflow switched to the bounded manual engine instead of retrying repeatedly. The cost is that **the two-stage funnel's "strict exit" (the fp2k real-run adjudication) was not completed**, and this was written into the log.

In addition, 4 **environment-level** facts were found (not plugin logic defects), recorded in `work\INST_XRY_provenance.txt`: the portable package **contains no instrument parameter file at all**, GSAS-II dispatches the instrument-file parser by extension, the new-style `.instprm` tolerates only one line of `#` comments, and GSAS-II reads files by system locale (GBK) so both must be pure ASCII. If these are worth feeding back to the plugin side, this record can be used directly.

Per your choice, `work\` and `refine\` (about 19 MB / 424+ files) are **all retained**, with no intermediate product deleted. There are still 4 **untried** items (carbonate substitution quantification, supercell/order-disorder, Kα2-stripping control, re-running with a measured instrument parameter file), so the wording of the conclusion is "no improvement margin **within the range tried**", not "the data limit has been reached".

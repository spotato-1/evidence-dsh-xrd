# FE50 judgment panel (review_judgment.md)

## First half · manual input window (the user's own words, not paraphrased)

- "workspace\DEEPSEEK V4 PRO\FE50" contains an XRD dataset; it is a Prussian blue crystal with nominal formula KxFe0.5Mn0.5[Fe(CN)6], synthesized by ball-milling Fe4[Fe(CN)6]3, manganese oxide tetrahydrate, and potassium citrate in 50% ethanol/water.
- "workspace\DEEPSEEK V4 PRO\FE50" provides two similar-material CIF files as reference.
- "The material should be considered to contain extensive defects, especially lattice distortion, vacancies, and split sites."
- "Process strictly following the xrd plugin, force the complex-case checklist, strictly follow the planned workflow, and consider all defects and possible fitting changes."
- "When in doubt, first consider the fitting approach and scientific self-consistency; before entering the final GSAS engine, all adjustments target lowering R."
- "The target is publication-level (R ≤ 10) as far as possible. Save the work under the data folder."

## Second half · judgment (wrap-up)

### Current best physical solution
- Face-centred cubic Fm-3m PBA, K1.86Fe0.5Mn0.5[Fe(CN)6]: 4a=low-spin Fe ([Fe(CN)6] core, C coordination), 4b=high-spin Fe0.5Mn0.5 (N coordination), 8c=K 0.930(12), 24e=C/N 0.97.
- Cell a=10.167 Å; bond lengths C–N=1.169, Fe–C=1.881, Fe/Mn–N=2.033 Å (all physical).
- **GSAS-II final wR=11.71%, Rp=9.31%, RBragg=11.11%, wRmin=7.92%, GOF=1.49**.
- Two key steps: ① correcting the Mn site to 4b (14.56→13.86); ② raising the background to a 20th-order Chebyshev (13.86→11.71).

### Unresolved assumptions (item by item; each has been tried or is marked untried)
1. K split site: splitting along [100] is worse (11.71→12.63), **undecided** ([111] direction untried, the tool is limited to uniaxial splitting).
2. Fe/Mn antisite: **untried** (Fe≈Mn scattering is nearly identical, indistinguishable by XRD).
3. [Fe(CN)6] vacancy: C/N=0.97 fixed; free refinement drifts (C→1.16/N→0.45, unphysical), **fixed**.
4. Preferred orientation: [001] MD ratio diverges, **excluded**.
5. Anisotropic strain HStrain: correlated with the scale at 98.99%, **excluded**.
6. C/N coordinates, Uiso: drifts are unphysical, **fixed**.
7. Monoclinic distortion P21/c: excluded by fp2k.

### branch list
- `cubic-Fm3m(correct sites) + K occupancy + 20th-order background`: **adopted** (wR=11.71, delivered).
- `cubic-Fm3m + C/N coordinates / Uiso / K-split / HStrain / pref-orientation`: all frozen (drift/worse/divergence).
- `monoclinic-P21c`: frozen/excluded.

### Current frozen state
- Not frozen. The complex checklist §6.2–6.4 has completed one full round (the four-way failure classification + item-by-item defect discrimination D0–D5), with no limit-mode trigger for failing to reach the target (limit_mode_attempts=0, the R value kept decreasing to 11.71 and afterwards no attempt at the various defects gave an improvement or was physical).

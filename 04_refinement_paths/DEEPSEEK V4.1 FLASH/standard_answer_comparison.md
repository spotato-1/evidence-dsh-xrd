# Comparison of the Manual/Standard Answers with the DSH-XRD Plugin Results of This Round

## Scope and Answer Grades

9 of the 12 cases contain answer assets that can be used for comparison:

- **Formal or external standards**: CeO2 (the paper round-robin consensus), Fe2O3/Fe3O4 (gravimetric true value), Fluoroapatite (official GSAS-II example), PbSO4 (official GSAS-II project), ZnO (official Topas structure of NIST SRM 1979).
- **Machine reference answers but no unique formal ground truth**: Y2O3 (two coexist, the historical plugin one and the AutoFP one).
- **User-specified final answer CIF**: the answer for LayeredOxide is only `answer/20260813_SG_BM_P2_Mo_final.cif`; `raw/手动精修结构/*.gpx` is process material, not the answer.
- **Manual-refinement comparison projects, not formal ground truth**: LayeredOxide_2ph, LiFePO4.
- **No answer asset**: Amorphous, FE50, FE60, and therefore this report does not score these 3 samples against a standard answer.

This grading matters: a manual project can reveal differences but cannot automatically be taken as absolute ground truth. LayeredOxide must take the user-specified final CIF as its answer; the manual GPX of LayeredOxide_2ph and LiFePO4 is used for method and result comparison and cannot directly serve as ground truth.

### Independence of the Refinement Starting Point

This round of testing did not provide the above answer CIF/GPX to the model as a fitting starting point. Apart from **the FE series, where the user injected a CIF in the second-round interaction**, the structural CIFs of all other samples were built by the AI after retrieving information itself; the first round of the FE series was also AI-built. Therefore the structural agreement described below is not inherited from the answer files, and model differences should also be attributed to the AI's phase determination, modelling and refinement behaviour. What LayeredOxide_2ph received in the second round was the user-provided textual conclusion on phase identity/space group, while the specific CIF was still AI-built.

## Overall Judgement

| Sample | Degree of agreement with the answer | Core judgement |
|---|---|---|
| CeO2 | **Cannot be scored directly** | Only the sharp sample `stephsh` was obtained this round, while the standard answer targets the size/strain of the broadened sample; the test input is incomplete |
| Fe2O3/Fe3O4 | **Fairly good** | Both phases are correct; 72.355/27.645 wt% is only 1.855 percentage points from the gravimetric true value |
| Fluoroapatite | **Very good** | The space group agrees, and a/c differ from the official values by only about 0.014% |
| LayeredOxide | **The main structure of the answer is highly consistent, but the phase composition differs** | Highly consistent with the P63/mmc cell of the final answer CIF; the plugin additionally adds about 9 wt% Na2MoO4, but the answer itself does not provide a comparable wR |
| LayeredOxide_2ph | **The number of phases is close, but the main-phase structure does not agree** | The data correspond completely; the manual answer is C2/m+P63/mmc, while the plugin obtained only an R-3m proxy+P63/mmc |
| LiFePO4 | **The main structure agrees, the AI fit is slightly better, and the true antisite fraction is undecided** | The manual project gives 0.37% and the plugin 4.0%; the manual value is not a standard answer, so evidence quality must be compared rather than judging the plugin wrong by it |
| PbSO4 | **Very good** | Pnma/Pbnm is only an axis permutation; the cell differs by about 0.011%, and the current wR is slightly lower than the official XRA |
| Y2O3 | **The blind-start structure succeeded, but the values fall short of the reference that had a prior** | The historical low R used the data provider's CIF/PCR; these assets were not provided this round and the CIF was AI-built, so it cannot be explained as a "regression" under equal conditions |
| ZnO | **The structure is very good, but the size conclusion has not reproduced the certified convention** | The cell differs from the official value by about 0.012–0.014%; the 32 nm apparent size is inconsistent with the 15 nm nominal value |

## Verification of Data Correspondence

### All Run Inputs

Comparing files of the same name by SHA-256, the original/input files in this round's DSH workspace are all identical to the corresponding files in `test_set`; LiFePO4's `24_twocol_probe.txt` is a file derived during the run, not an original of the test set. The only gap in the test design is that **the CeO2 working directory contains only `stephsh_2th.txt` and no `stephbr_2th.txt`**.

### Dedicated Verification for LayeredOxide_2ph

The histogram name of the manual answer project `20251121.gpx` is `PWDR Na0.9K0.1.csv`. The point-by-point check gives:

- `Na0.9K0.1.csv`, manual GPX: 6861 points, **both x and y_obs are exactly identical point by point**.
- `91.txt` and the above data: all 6861 **y_obs values are exactly identical point by point**; x is only rounded to 0.001°, with a maximum difference of `0.000499734°` and a mean difference of `0.000249978°`.
- The float64 SHA-256 of `y_obs` is `aac717b7f4a70d43aff62d760222c18bc6fbe61205d589964cef62b6253af1d3` for all three.
- The plugin tool trace of this round shows that `raw/91.txt` was actually used; the SHA-256 of both the DSH-workspace copy of that file and the original of the test set is `FA08FBE5D71976470364B42F75C1FCF0D9272E4274D9E77FB2EC6EFE8DC78C70`.
- The `y_calc/y_bkg` carried in `91.txt` are not the same as the final calculated pattern of the manual answer GPX, but the plugin reads the file as two-column data and uses only x/y_obs. These old calculated columns therefore did not leak the manual answer into the refinement.

Conclusion: **the manual answer and the plugin test of LayeredOxide_2ph come from the same set of observed data; the differences in space group and unit cell are not caused by taking the wrong data, by omission, or by misremembering.**

## Case-by-Case Differences

### 1. CeO2: What Was Actually Run Is the Instrument Sharp Sample, Not the Standard Broadened Sample Under Test

The standard case consists of a pair of data sets from the same instrument:

- `stephbr_2th.txt`: the broadened sample, the target being domain size/strain.
- `stephsh_2th.txt`: the annealed sharp sample, used to estimate instrumental broadening.

The paper consensus is AWDS of about 16.6–16.8 nm, VWDS of about 22.3–32 nm, and strain of about 0. This round's DSH working directory contains only the sharp sample, and the plugin explicitly took the 24000-point `stephsh_2th.txt` as the refinement object, obtaining a size of 0.60193 µm and a microstrain of 777.3 µε.

These two numbers cannot be compared with the broadened-sample consensus. They only show that on the sharp sample the plugin interpreted the remaining instrumental peak-width component as size/microstrain. The Fm-3m phase identification and `a=5.410894 Å` remain reasonable, but this round does not constitute a valid test of the CeO2 size–strain round-robin.

### 2. Fe2O3/Fe3O4: The Phase Fractions Are Close to the Gravimetric True Values

| | Fe2O3 | Fe3O4 |
|---|---:|---:|
| Gravimetric true value | 70.5 wt% | 29.5 wt% |
| Paper re-check | 67.9 wt% | 32.1 wt% |
| This round's plugin | 72.355 wt% | 27.645 wt% |
| Plugin − true value | +1.855 pp | −1.855 pp |

The absolute error of the plugin's main phase is about 0.745 percentage points smaller than that of the paper re-check, and both the qualitative and the quantitative results are fairly good. However, about 99% of the counts come from the Fe fluorescence background, so `wR=2.35%` cannot serve as proof of extremely high phase-fraction precision; the actual deviation of 1.855 pp from the true value should be taken as the main achievement.

### 3. Fluoroapatite: In the Same Solution as the Official Structure

| | Official example | This round's plugin | Relative difference |
|---|---:|---:|---:|
| Space group | P63/m | P63/m | Agrees |
| a / Å | 9.37189 | 9.370519 | −0.0146% |
| c / Å | 6.88591 | 6.884920 | −0.0144% |
| wR | 10.38% | 9.704% | −0.676 pp |

The test set also retains a historical plugin answer of `wR=9.32%`, which is 0.384 pp lower than this round. The R differences among the three mainly reflect the refinement route and the parameterisation, not a conflict in the phase/cell conclusions. The structural conclusion of this round passes the standard comparison.

### 4. LayeredOxide: Taking the Final Answer CIF as the Standard, the Main Structure Is Highly Consistent

The authoritative answer for this case is:

`workspace\test_set\LayeredOxide\answer\20260813_SG_BM_P2_Mo_final.cif`

`raw/手动精修结构/20260813 SG+BM.gpx` is merely a process working file, and its `wR=12.106%` **is not part of the standard answer and cannot be used for a performance comparison with the plugin's wR**. Although the 3432 y_obs values of the process GPX and of the plugin project are identical point by point, this only proves that they processed the same measured pattern.

| | Final answer CIF | This round's plugin |
|---|---:|---:|
| Main structure | P2_Mo, P63/mmc | P2, P63/mmc |
| a / Å | 2.88757 | 2.887450 (−0.0042%) |
| c / Å | 11.15398 | 11.156121 (+0.0192%) |
| CIF/model composition | Na0.4088Ni0.33Mn0.62Mo0.05O2 | Main phase taken as nominal Na0.72Ni0.33Mn0.62Mo0.05O2, plus Na2MoO4 8.991 wt% |
| Answer fit metrics | Not provided | wR 7.779% |

Therefore the plugin's **independent reproduction of the main-phase space group and unit cell is very good**. The main difference is not the main structure but the phase composition and occupancies: the answer CIF encodes only the P2_Mo structure and has no Na2MoO4 phase, whereas the plugin extracts about 9 wt% Na2MoO4 from extra peaks. Whether the answer CIF describes only the main phase or has excluded impurity phases must be interpreted according to how the answer is defined, and it cannot be overridden merely on the strength of the plugin's lower internal wR.

The two models also leave different chemical questions: computed from occupancies/multiplicities, the answer CIF gives Na/TM≈0.409, below the nominal 0.72; the plugin retains the nominal Mo0.05 in the main phase while also adding Na2MoO4, so the overall Mo balance is not closed. At present, therefore, it can be confirmed that the P2 main structure was reproduced successfully, but the Na occupancy, the fate of Mo and the quantification of the impurity phase still require separate adjudication.

### 5. LayeredOxide_2ph: The Data Are Correct, but the Main-Phase Space Group Was Not Reproduced

Results of the manual project:

- O3 `C2/m`: 94.395 wt%, `a=5.294635, b=9.177481, c=5.644291 Å, β=107.9197°`.
- P2 `P63/mmc`: 5.605 wt%, `a=2.779811, c=11.187864 Å`.
- GSAS-II `wR=8.199%`.

The plugin's second answer confirms about 5% P2, but the main phase still uses the O3 `R-3m` proxy; its C2/m attempt gives `Rwp=21.61%`. The starting cell used in that attempt is about `a=5.13, b=2.903, c=5.74 Å, β=106.5°`, which is not the C2/m reference cell of the manual project. This high R therefore cannot prove that the reference C2/m is wrong; it can only prove that the particular C2/m model the plugin constructed does not fit.

The P2 cell also differs substantially: the plugin gives about `a=2.8853, c=11.1478 Å`, which is +3.79% and −0.36% relative to the manual project. The difference in a is far larger than a normal refinement error, and either a re-indexing is needed or the P2 cell setting of the manual project must be checked.

### 6. LiFePO4: The AI Result Is Slightly Better in Both Fit and Argumentation, but the True Antisite Value Is Undecided

The x grids of the manual and plugin GPX are identical point by point; the plugin's y_obs is exactly 0.2 times that of the manual project and its weight is 5 times, showing that this is an overall scale conversion of the same pattern, not a different sample.

| | Manual project | This round's plugin |
|---|---:|---:|
| Space group | Pnma | Pnma |
| a,b,c / Å | 10.329446, 6.007306, 4.691861 | 10.325358, 6.005014, 4.690060 |
| Li/Fe antisite | 0.37% | 4.0% |
| wR | 6.443% | 6.223% |

The manual project is not standard ground truth, so the plugin cannot be judged wrong simply because it gives 4%. Comparing on the available evidence:

- The plugin's R, Rb and wR are all slightly lower (wR improved by 0.220 pp), and it explicitly performed a profile-likelihood scan of the antisite fraction under fixed thermal parameters and also identified and rejected the confounded solution of about 8% caused by free thermal parameters; its chain of argument is more complete than that of the manual project.
- The manual project gives 0.37%, but that project contains no independent error analysis sufficient to elevate this value to ground truth; it is more like a manually converged solution.
- Both sides fix Uiso at 0.01, and Li scatters X-rays very weakly. The overall intensity scale and the statistical weights of the two projects also differ, so GOF/wRmin cannot directly arbitrate which one is more real.

The current judgement should therefore be: **the AI result is slightly better in fit values and in defect-confounding analysis, but which of 4% and 0.37% is physically more real remains unresolved**. A unified profile-likelihood under identical weights/background/peak shape is needed, and it would be best to verify further with neutron diffraction or other occupancy-sensitive evidence.

### 7. PbSO4: Highly Consistent with the Official Answer

The official answer is Pnma; the plugin exports Pbnm, which is an axis permutation of the same #62 space group. After converting the plugin cell to the official Pnma order:

- Official: 8.480443, 5.398619, 6.960131 Å.
- Plugin: 8.481366, 5.399204, 6.960893 Å.
- All three axes are only about 0.011% higher.

The plugin's single-histogram X-ray wR is 9.506%, while the official XRA is 10.11%. The current fit value is slightly lower, but the official structure comes from a joint neutron + X-ray refinement, so the official answer should still take priority for the atomic coordinates/thermal parameters.

### 8. Y2O3: The Structure Was Independently Reproduced from a Blind Start and Cannot Be Compared Side-by-Side Simply with a Low R That Had a Prior

- Historical plugin answer: Ia-3, `a=10.6003 Å`, wR 11.81%; that route used the data provider's CIF starting structure.
- AutoFP reference: `a=10.603124 Å`, Rwp 7.04%; it used the data provider's CIF/PCR starting assets, and the final result came with negative Biso, an over-full O occupancy and strong preferred orientation, so it cannot be delivered directly.
- This round's plugin: the above CIF/PCR were not provided and the AI built the starting CIF itself; in the end it still correctly obtained Ia-3, `a=10.600066 Å`, wR 16.938%.

Therefore the most important positive result of this round is: **under blind-start conditions without the data provider's CIF/PCR, the AI independently completed correct phase determination, space-group selection and unit-cell construction**. Its wR is about 5.13 percentage points higher than that of the historical plugin, showing that the final peak-shape/instrument treatment still falls short of the reference route that had a starting prior, but this is not a direct performance regression under equal starting conditions. AutoFP's 7.04% both enjoys the advantage of a starting PCR/CIF and contains non-physical degrees of freedom, so it is even less admissible as a hard R threshold for this round.

To evaluate the algorithm itself, two control arms should be established: arm A keeps this round's "no CIF/PCR given, AI-built"; arm B provides the data provider's CIF/PCR to the same model. Only when A/B use the same refinement backend and physical constraints can the difference be split into "starting-model information" and "refinement capability".

### 9. ZnO: The Structure Passes, the Size Has Not Yet Reproduced the Reference-Material Convention

| | NIST/Topas answer | This round's plugin |
|---|---:|---:|
| Space group | P63mc | P63mc |
| a / Å | 3.24981 | 3.250249 (+0.0135%) |
| c / Å | 5.20875 | 5.209375 (+0.0120%) |
| z of O relative to Zn | 0.38226 | about 0.38323 |

The structural reproduction is good. As for size, the plugin explicitly considers the GSAS `Size=10 µm` a nominal value that is unusable, and an independent Scherrer calculation gives about 32 nm (26.4–36.8 nm), about 2.1 times the 15 nm nominal value. Because this round did not reliably separate the 11-BM instrumental broadening, and because the answer directory of this test set does not give a certified size value that can be compared directly, this size cannot serve as a valid reproduction of the SRM 1979 certified quantity; it should be judged as the structural refinement passing and the size verification being incomplete, rather than simply as wrong.

## Main Causes of the Differences

1. **Incomplete test input**: CeO2 provides only the sharp sample, which turns the standard task from "size/strain of the broadened sample" into "structural refinement of the sharp sample".
2. **Unequal starting information**: the historical low-R Y2O3 result used the provider's CIF/PCR, while this round adopted an AI-built CIF; the R difference cannot be attributed entirely to refinement performance.
3. **Inconsistent cell/model construction**: the plugin's C2/m attempt for LayeredOxide_2ph did not use the reference monoclinic cell of the manual project, so the high R cannot adjudicate the real C2/m.
4. **Weakly identifiable parameters**: the Li/Fe antisite of LiFePO4, the size of ZnO and the Mo partitioning of LayeredOxide all depend strongly on the instrument, the background and the constraint model.
5. **Different R conventions and physical constraints**: AutoFP's low R for Y2O3 came with non-physical parameters; the extremely low wR of the two Fe phases is diluted by a strong background.
6. **Different answer grades**: LayeredOxide takes a final CIF as its answer but contains no comparable R value; the manual GPX of LayeredOxide_2ph and LiFePO4 are comparison objects rather than absolute ground truth.

## Suggested Priority for Retesting

1. **CeO2**: place `stephbr_2th.txt` and `stephsh_2th.txt` together in the same case at the same time, calibrate the instrument with the sharp sample first, and then determine size/strain from the broadened sample only.
2. **LayeredOxide_2ph**: export the accurate CIFs/cell settings of O3 C2/m and P2 directly from the manual `20251121.gpx`, then, with the same data and weights fixed, carry out a controlled A/B refinement.
3. **LiFePO4**: under exactly identical weights, background, peak shape and Uiso constraints, perform a one-dimensional profile-likelihood over 0.37%, 4% and the continuous antisite fraction; do not merely compare the two final wR values.
4. **Y2O3**: establish two controlled routes, a blind start (AI-built CIF) and a seeded start (provider's CIF/PCR), using the same backend and physical constraints, in order to split the 5.13 pp difference into what comes from the starting prior and what comes from peak-shape/instrument treatment.
5. **LayeredOxide**: test separately "all Mo in the main phase", "all Mo in Na2MoO4" and "a two-phase model constrained by total Mo conservation", in order to close the elemental balance.

## Machine-Verification Artifacts

- `standard_answer_matrix.csv`: a machine-readable summary of the 9 comparable cases.
- `gpx_answer_extract.json`: read-only extraction of phases, unit cells, occupancies, residuals and phase fractions from the manual and plugin GPX.
- `layered2_data_identity.json`: point-by-point consistency of the two-phase layered oxide CSV/TXT/GPX.
- `layered_data_identity.json`: data consistency between the raw process project of LayeredOxide and the plugin project; that process GPX does not serve as the answer.
- `lifepo4_data_identity.json`: the data scale and weight relationship of the two LiFePO4 projects.

All source answers, raw data, GPX, CIF and existing measured evidence remain unmodified.

# Analysis of Refinement Differences Between DEEPSEEK V4.1 FLASH and GPT 5.6 SOL

## Statistical Scope

The official LiFePO4 result for GPT 5.6 SOL now uses the rerun session `session-e03ae580-d18c-423f-806e-9920746a5e8e`. The old session `session-3c0c083d-6e54-4a2b-896f-5e4e320ea939` has been withdrawn from the main evidence set, the ledger, and the comparison data, and moved into the recoverable `dsh-xrd-test-evidence-superseded`, and no longer participates in the model capability statistics.

## Conclusions First

Both models used the same test inputs. The main differences come from the starting structure and unit-cell calibration, the physical constraints on the profile parameters, the order in which parameters are released, and the method of quantifying defects, rather than from a difference in the raw patterns.

In LiFePO4, the GPT rerun has made substantial progress relative to the old result: the unit cell is restored to a reasonable range, the `0.0037` from the defect summary table is no longer fixed as the antisite fraction in the final result, and approximately 1–4% is explicitly treated as a model-sensitive range rather than as a quantitative result. However, the final instrument profile parameters still fall into a severely non-physical domain, with wR=23.76%, clearly worse than DEEPSEEK's 6.22%.

Therefore:

- For the average structure and the overall pattern fit, the DEEPSEEK solution remains clearly better;
- For the caution of the antisite conclusion, the GPT rerun is better than the old GPT: it did not write an unsupported precise value into the final structure;
- DEEPSEEK's approximately 4% is supported by a controlled scan, but it is still an in-model estimate and should not be regarded as an absolute true value;
- GPT's main remaining problem has shifted from "wrong unit cell + fixed exemplar value" to "profile parameters out of domain + systematic residual at the main peaks".

## 1. Comparability and Input Consistency

The raw-data hashes of the six shared samples are identical. Both the test-set RAW for LiFePO4 and the GPT rerun workspace RAW are 31,162 bytes, and both have the SHA-256:

`922b80d830628ed03d7407561fc634eea1116b8b3e9afc331b197bf230e2e1dd`

The correlation coefficient between the LiFePO4 `yobs` arrays in the final GPX files of GPT and DEEPSEEK is `0.9999999999999992`, with a linear slope of `1.0000000008`. The final differences cannot therefore be attributed to a change of data or weights.

The prompt only required that Li/Fe antisite be considered, and did not provide 0.37%, 0.0037, 4%, or any other antisite fraction. Both GPT and DEEPSEEK read the plugin's defect summary table, so both were exposed to the concrete LiFePO4 exemplar in it; this is a shared prior risk.

FE50 is still not a strictly blind, equivalent comparison: GPT already had a candidate CIF at the start; DEEPSEEK's FE50/FE60 shared a session, and the CIF was only injected in the second round.

## 2. Final-Engineering Comparison of the Five Crystalline Samples

| Sample | DEEPSEEK wR | GPT wR | Fraction of angular points with a negative Gaussian width term for GPT | Main difference |
|---|---:|---:|---:|---|
| Fe2O3 + Fe3O4 | 2.35% | 2.73% | 59.7% | Both identify two phases; GPT did not report the key mass fractions, and its low R is affected by a high background |
| FE50 | 11.42% | 11.73% | 12.2% | Not a strictly blind equivalent; GPT's P21/c local geometry is still unstable |
| Fluoroapatite | 9.70% | 12.53% | 93.9% | Both are P63/m; the difference mainly comes from coordinate and profile optimization |
| LayeredOxide | 7.78% | 14.55% | 100% | Both identify the P2 main phase and Na2MoO4; GPT's impurity-phase and profile settings are unstable |
| LiFePO4 | 6.22% | 23.76% | 98.5% | GPT's unit cell has been restored, but the instrument profile is still out of domain, with an obvious residual at the main peaks |

The Gaussian width term is defined by the continuous-wavelength profile:

`G(θ) = U tan²θ + V tanθ + W`

A large negative area means the optimization relies on numerical lower bounds, and the parameters no longer represent credible instrumental broadening. In DEEPSEEK's five crystalline deliverables, G remains positive within each respective measurement range; GPT, by contrast, exhibits a systematic profile-gating gap across samples.

## 3. Detailed LiFePO4 Comparison

### 3.1 The Unit Cell Is No Longer the Main Problem

| Result | a / Å | b / Å | c / Å | V / Å³ |
|---|---:|---:|---:|---:|
| Historical manual low-R project (reference only) | 10.32945 | 6.00731 | 4.69186 | 291.140 |
| DEEPSEEK | 10.32536 | 6.00501 | 4.69006 | 290.802 |
| GPT official rerun | 10.33376 | 6.00576 | 4.68885 | 291.000 |

The difference between GPT and DEEPSEEK is only `+0.00841/+0.00074/-0.00121 Å`, with a volume difference of about 0.198 Å³. Phase-family selection and unit-cell recovery are already essentially correct.

### 3.2 The Main Gap Has Shifted to the Instrument Profile

| Parameter | DEEPSEEK | GPT official rerun |
|---|---:|---:|
| Zero / °2θ | -0.0534 | -0.0563 |
| U | 34.33 | -13493.19 |
| V | -18.01 | 991.01 |
| W | 11.23 | 30.10 |
| X | 8.06 | -39.18 |
| Y | -7.22 | 228.73 |
| Proportion of non-positive Gaussian terms | 0% | 98.53% |
| Proportion of non-positive Lorentz terms | 0% | 13.90% |

GPT's zero point is already reasonable, but U/V/W/X/Y show more severe mutual compensation. Although the structural review reports `pass`, it only checked the atomic coordinates, occupancies, Uiso, and short contacts, and did not cover the instrument function.

GPT's 18th-order background baseline once reached wR=23.635%, while the final "strict structure + profile/pref" project was 23.759%. The final choice is not the lowest R over the whole workflow, and both share the out-of-domain profile problem. The difference curve still shows systematic spikes at the main-phase peaks around 17, 21, 29.5, 35.5, and 52–62°, so the remaining problem lies first in the peak-width/peak-intensity model, not in the antisite occupancy.

### 3.3 The Antisite Result No Longer Directly Copies `0.0037`

In the GPT rerun's actual tool calls, the starting point was 1%, with the Li site and the Fe site set to `0.99/0.01` respectively, and `0.0037` was not used as a numerical seed. The branch results include:

- about 6.42%: free coordinates diverged, discarded;
- about 4.07% to 9.49%: drifted markedly with the background and coordinate treatment;
- about 1.01% to 3.96%: the strict-occupancy branch still varied with the background;
- final GPX/CIF: no antisite mixed-occupancy value written in.

This shows that GPT recognized the weak identifiability of Li/Fe antisite from X-ray data. The final text still compares 1.01% with the 0.37% exemplar in the defect summary table as "of the same order", so the exemplar remains a narrative anchor but is no longer the source of the final value.

After freezing Uiso, DEEPSEEK scanned x=0, 0.02, 0.04, 0.06, 0.08, 0.10, 0.15, and wR forms an in-model minimum near x≈0.04, so the evidence chain for 4% is more complete than an arbitrarily fixed single point. However, owing to the X-ray sensitivity to light elements and the correlation with Uiso and the background, it should still be reported as a model estimate with a fairly large systematic uncertainty.

### 3.4 Impact of the Runtime Infrastructure

The request header of the GPT rerun session has no `reasoningEffort` field and used the provider default. The session was interrupted twice, at 19:57:32 and 20:07:43, with `PI_AI_ERROR`, and both errors explicitly pointed to the upstream OpenAI service being unavailable; the third turn eventually completed.

This proves that the run was contaminated by infrastructure interruptions, but it cannot prove that the server automatically lowered the reasoning effort. The session had a total of 116 tool calls, 11 recorded turns, and 36,615 assistant output tokens, so the workload was not low. The official evidence is therefore marked `eligible_with_warnings`, rather than failed or "confirmed low reasoning effort".

## 4. Summary of the Other Samples

### Amorphous

Both correctly refused to force a crystal structure. DEEPSEEK used 4 broad peaks plus a background to obtain an empirical Rwp=3.499%; GPT used two broad peaks and obtained 6.50%. This is a difference in the empirical whole-pattern description, not in the quality of a crystal structure.

### Fe2O3 + Fe3O4

Both identified R-3c hematite and Fd-3m magnetite. DEEPSEEK gives 72.4/27.6 wt%, close to the weighed reference values of 70.5/29.5; GPT omitted the mass fractions, and its profile has a non-physical domain.

### FE50

DEEPSEEK adopted an Fm-3m average model; GPT adopted P21/c but still has anomalous C–N and metal–N geometry. Because the starting CIF conditions differ, this case cannot serve as a pure blind model comparison.

### Fluoroapatite

Both give P63/m, with almost identical unit cells. GPT's Gaussian width term is negative at about 93.9% of the measurement points, so the gap is mainly one of coordinate/profile optimization and gating quality.

### LayeredOxide

Both identified the P63/mmc P2 main phase and a Na2MoO4 candidate. DEEPSEEK obtained about 8.99 wt% Na2MoO4; GPT's impurity-phase representation, phase scale, and profile were all unstable.

## 5. Summary of Root Causes

1. **Missing physical boundaries for the profile**: GPT repeatedly let U/V/W/X/Y enter mutually compensating or numerically clamped regions.
2. **Insufficient gating coverage**: `review=pass` focuses on structural hygiene and did not verify that the instrument profile is positive within the measurement range.
3. **Parameter hierarchy**: although GPT corrected the unit cell, the subsequent background, instrument, profile, and structure parameters still lacked stable separation.
4. **Handling of defect identifiability**: the final characterization in the GPT rerun is more cautious; DEEPSEEK's controlled scan is more complete within the model.
5. **Plugin exemplar anchoring**: both models could see a concrete numerical exemplar for the same material; the GPT rerun did not copy that value, but still cited it in its final explanation.
6. **Infrastructure contamination**: the official GPT rerun was interrupted twice by the upstream service, and should be flagged separately in the repeatability statistics.

## 6. Recommendations for Subsequent Testing

1. Explicitly fix the API reasoning effort and record the request receipts; repeat the identical input at least 3 times.
2. Mark runs containing `PI_AI_ERROR` as infrastructure-contaminated, and do not treat them as fully equivalent to error-free runs.
3. Add `G(θ)>0` and Lorentz-term positivity gating at the plugin level, covering all actual Bragg positions.
4. The LiFePO4 antisite must be scanned at fixed Uiso on the same low-R, physically acceptable-profile baseline.
5. Split "whether an unsupported precise value was given" and "overall fit quality" into two separate scoring items.

## 7. Audit Artifacts

- `common_cases_cross_model_gpx.json`: official GPX comparison of the five shared crystalline samples.
- `lifepo4_cross_model_gpx.json`: the manual reference, DEEPSEEK, the GPT official rerun, and the intermediate branches of the GPT rerun.
- `cross_model_summary.csv`: summary of the main metrics.
- `LiFePO4_GPT56_rerun_analysis.md`: audit of the single-case run and server interruptions of the GPT rerun.
- `compare_common_cases.py`, `compare_lifepo4_models.py`: read-only extraction scripts.

The original DSH workspace and the original session containers were not modified; the old GPT LiFePO4 evidence was withdrawn only from the main statistics and is kept in the recoverable superseded area.

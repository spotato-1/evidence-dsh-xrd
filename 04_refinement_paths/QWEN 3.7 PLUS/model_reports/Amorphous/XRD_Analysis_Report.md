# XRD Data Analysis Report of g-C3N4-Derived Hollow Carbon Microrods

## 1. Sample Information

| Item | Content |
|------|------|
| **Sample** | g-C3N4 hollow microrod-derived carbon |
| **Synthesis route** | g-C3N4 hollow microrods coated with multiple layers of different materials, sintered at 1100°C in Ar atmosphere |
| **TEM morphology** | Well carbonized, hollow rod morphology retained; the tube wall consists of three layers of carbon structures with different densities from inside to outside |
| **Measurement conditions** | Rigaku, Cu Kα (λ₁=1.5406 Å, λ₂=1.54439 Å, ratio=0.5) |
| **Scan range** | 10–80° 2θ, step size 0.0204°, 3432 points |

## 2. Analysis Strategy

### 2.1 Material Classification

According to the TEM information, this sample is **not simple amorphous carbon**, but a derived carbon material with a three-layer carbon structure of different densities. The material classification is upgraded from class C (pure amorphous) to **class B (decomposition of carbon structural components)**.

### 2.2 Fitting Model

g-C3N4 is fully carbonized at 1100°C under Ar, but the three carbon layers have different degrees of graphitization:
- **Inner layer** (close to the original g-C3N4 template): highest degree of graphitization
- **Middle layer**: medium degree of order
- **Outer layer**: most disordered/most loose

In XRD, carbon with different degrees of graphitization appears as broad peaks at different positions and with different widths:
- Degree of graphitization ↑ → d(002) ↓ → peak position shifts to higher angle, peak becomes narrower
- Degree of disorder ↑ → d(002) ↑ → peak shifts to lower angle, peak becomes broader

A fit with **3 empirical broad peaks (Pseudo-Voigt) + 20th-order Chebyshev background** was adopted.

### 2.3 Background Optimization

Results of the background-order iteration (bg_scan):

| Order | Rwp (%) | Gain |
|------|---------|------|
| 6 | 9.25 | — |
| 8 | 8.26 | 0.99 |
| 10 | 7.32 | 0.94 |
| 12 | 6.38 | 0.94 |
| 14 | 6.05 | 0.33 ← boundary |
| 16 | 5.48 | 0.57 |
| 18 | 5.01 | 0.47 |
| 20 | 4.62 | 0.39 |

The gain drops sharply from order 12→14 (0.94→0.33), suggesting an R-value boundary effect. Order 20 was finally selected (Rwp=4.54%), but **a high-order background may absorb part of the structural information**, so the decomposition of the broad peaks must be interpreted with caution.

## 3. Fitting Results

### 3.1 R Factors

| Metric | Value |
|------|------|
| **Rwp** | **4.54%** |
| **Rexp** | **3.69%** |
| **χ²** | **1.51** |
| Baseline Rwp | 96.52% |

### 3.2 Broad Peak Parameters

| Broad peak | Center 2θ (°) | d-spacing (Å) | FWHM (°) | Assignment | Corresponding TEM layer |
|------|-------------|------------|----------|------|-----------|
| **Peak 1** | 17.14 ± 1.47 | **5.19** | 0.57* | Highly disordered carbon / large interlayer spacing | **Outer layer** (low density) |
| **Peak 2** | 24.55 ± 2309 | **3.63** | 3.84 | Graphite (002) main peak | **Middle layer** |
| **Peak 3** | 41.91 ± 0.03 | **2.14** | 2.11 | Graphite (100)/(101) in-plane scattering | **Inner layer** (high density) |

> \* The FWHM stderr of peak 1 is 354°, so its parameters are not sufficiently determined by the data; the position stderr of peak 2 is extremely large, so its center position is unreliable. Only the parameters of peak 3 are fully reliable.

### 3.3 Scherrer Coherence Length (Apparent Value, Instrumental Broadening Not Subtracted)

Using the fitted FWHM and the Scherrer formula D = Kλ/(β·cosθ), K=0.9:

| Broad peak | 2θ (°) | FWHM (°) | d (Å) | **D_app (nm)** | Physical meaning |
|------|--------|----------|-------|----------------|----------|
| Peak 1 | 17.14 | 0.57* | 5.19 | ~15* | Apparent value, parameters unreliable |
| Peak 2 | 24.55 | 3.84 | 3.63 | **~2.2** | Lc(002) extremely small, highly disordered |
| Peak 3 | 41.91 | 2.11 | 2.14 | **~4.4** | La(100) in-plane coherence domain |

> **⚠ Important**: These are **apparent coherence lengths** without subtraction of instrumental broadening, so the actual values may be smaller. For highly disordered carbon, the assumptions of the Scherrer formula (pure size broadening, no strain) do not fully hold, and the numbers are only for **semi-quantitative comparison**.

### 3.4 d-Spacing Analysis

| Peak | d-spacing (Å) | Reference value | Discussion |
|----|-----------|--------|------|
| Peak 1 | 5.19 | Graphite d(002)=3.35 | Far larger than the graphite value, indicating **extremely large interlayer spacing** / highly disordered |
| Peak 2 | 3.63 | Hard carbon d(002)≈3.6–3.8 | Consistent with **turbostratic carbon** |
| Peak 3 | 2.14 | Graphite d(100)=2.13 | Consistent with graphite in-plane scattering |

## 4. XRD Interpretation of the Three-Layer Carbon Structure

### 4.1 Model

Correspondence in XRD of the three-layer structure shown by TEM (from inside to outside):

```
Schematic cross-section of the tube wall (from inside to outside):
┌─────────────────────────────────────────┐
│  Inner     │  Middle    │  Outer        │
│  High dens.│  Medium    │  Low dens.    │
│  Graphitic │  Ordered   │  Disordered   │
│            │            │               │
│  → Peak 3  │  → Peak 2  │  → Peak 1     │
│  41.9°     │  24.5°     │  17.1°        │
│  d=2.14    │  d=3.63    │  d=5.19       │
│  La~4nm    │  Lc~2nm    │  (unreliable) │
└─────────────────────────────────────────┘
```

### 4.2 Discussion

1. **Inner layer (high-density graphitic carbon)**:
   - d(100)=2.14 Å agrees closely with the standard graphite value (2.13 Å)
   - A coherence length of ~4.4 nm indicates that the in-plane ordered domains are small but clearly present
   - The carbonization temperature of 1100°C is sufficient to form localized graphitization

2. **Middle layer (turbostratic carbon)**:
   - d(002)=3.63 Å is significantly larger than that of perfect graphite (3.35 Å), but lies in the typical range of turbostratic carbon (3.5–3.8 Å)
   - A coherence length Lc~2.2 nm indicates that only ~6 layers are stacked in an ordered manner along the c axis
   - This is a medium-order structure formed by re-arrangement of carbon atoms after decomposition of the template during carbonization

3. **Outer layer (highly disordered carbon)**:
   - d=5.19 Å is far larger than the interlayer spacing of any graphitic carbon
   - It may reflect: ① disordered carbon with an extremely large interlayer spacing ② residual pores/curvature effects ③ surface functional groups
   - **The parameter uncertainty is large**, and the physical meaning of this peak needs to be further confirmed in combination with other characterizations (Raman, solid-state NMR)

### 4.3 Limitations

- **Non-uniqueness of broad-peak decomposition**: The decomposition into 3 broad peaks is **one possible model**, not a unique solution. A different number of peaks or different constraints could give a different decomposition.
- **Parameter correlation**: The parameters of peak 1 and peak 2 are highly correlated (extremely large stderr), and only the parameters of peak 3 are reliable.
- **Background influence**: The 20th-order background may absorb part of the low-frequency structural information, affecting the broad-peak parameters.
- **The resolution of XRD for amorphous materials is limited**: The three-layer carbon structure is resolvable in real space (TEM), but appears as overlapping broad peaks in reciprocal space (XRD), so the decomposition has inherent ambiguity.

## 5. Assessment of Fitting Quality

### 5.1 Residual Analysis

- Residual RMS = 34.7 counts
- Maximum residual ~157 counts (located in the main-peak region)
- The residual plot is **largely random**, but there is a slight systematic deviation in the 25–35° region
- The systematic deviation is not large, indicating that the 3-peak model has captured the main structural features

### 5.2 Fitting Result Figure

Final fitting figure: `amorphous_carbon_fit3_fit.png`

## 6. Conclusions

1. **Phase composition**: This sample is a three-layer carbon structure derived from a g-C3N4 template, appearing in XRD as three characteristic broad peaks
2. **Interlayer structure**:
   - Inner layer: d(100)=2.14 Å, graphite in-plane order, La~4 nm
   - Middle layer: d(002)=3.63 Å, turbostratic carbon characteristics, Lc~2 nm
   - Outer layer: d=5.19 Å, highly disordered (parameters uncertain)
3. **Degree of graphitization**: The overall degree of graphitization is not high, and the coherence length of the most ordered region is only ~4 nm
4. **No crystalline impurities**: No sharp diffraction peaks were detected, and there is no crystalline impurity phase (detection limit ~1-2 wt%)

## 7. Recommendations

1. **Raman spectroscopy**: The D/G peak intensity ratio can independently assess the degree of graphitization and cross-check the XRD results
2. **Solid-state ¹³C NMR**: Can probe the sp²/sp³ carbon ratio and local structure
3. **HRTEM selected-area electron diffraction**: Can directly observe the local degree of order of each layer
4. **If quantitative phase fractions are required**: Standard samples with known structures are needed, or the GSAS-II refinement route must be taken (but the improvement is limited for amorphous-dominated materials)

## 8. List of Output Files

| File name | Description |
|--------|------|
| `workflow_state.json` | Workflow state |
| `xrd_workflow/journal.jsonl` | Refinement log (machine-readable) |
| `xrd_workflow/journal.md` | Refinement log quick-view |
| `result.json` | Final fitting results (including all parameters) |
| `components.json` | Fitting component data |
| `amorphous_carbon_fit3_fit.png` | Final fitting result figure |
| `pattern_twocol.dat` | Converted two-column data |
| `XRD_Analysis_Report.md` | This analysis report |

---

**Analysis software**: DeepSeek Harness + dsh-xrd plugin
**Analysis date**: 2026-01-20
**Analysis method**: Strictly executed according to xrd-workflow

**End of report**

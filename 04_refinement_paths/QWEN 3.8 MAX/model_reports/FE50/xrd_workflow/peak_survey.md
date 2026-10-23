# FE50 peak survey (stage 2 initial screening, V1 joint visual + numerical interpretation)

Data: `pattern_2theta.txt` (Rigaku RAW4.00, Cu target, Kα2 not stripped, 10.000–70.001°, step 0.0214213, 2802 points, 40 kV/40 mA, PSD).
λ determination: doublet [Kα1=1.5406, Kα2=1.54439, ratio=0.5], source = data header Alpha1/Alpha2/AlphaRatio (authoritative); `ActuallyUsedLambda=1.5418` is the Kα average and is not used as monochromatic.

## Main peaks (PBA main phase, cubic indexing a≈10.14–10.20 Å)
| 2θ (°) | Net intensity | hkl (cubic Fm-3m) | FWHM (°) | Remarks |
|---|---|---|---|---|
| 17.39 | 282 | (200) | 0.285 | sharp |
| 24.76 | 478 | (220) | 0.292 | strongest peak |
| 35.36 | 289 | (400) | 0.383 | slightly broader than (200)/(220) → may contain a distortion/strain component |
| ~39.1–39.9 | 27–55 | (420) region | — | **multiple extrema, suspected splitting** |
| ~43.0–44.5 | 59–113 | (422) region | — | **broad cluster of multiple extrema, suspected splitting/impurity overlap** |
| 50.9 | 59 | (440) | unreliable (noise) | weak |
| 57.4 | 63 | (620) | unreliable (noise) | weak |
| >58.4 | — | (640)/(444) missing | — | intensity sunk into the noise |

From (200) a≈10.20 Å; from (400)/(440)/(620) a≈10.14–10.15 Å — **the a values at high and low angle are inconsistent (~0.6%)**, pointing to a zero-point shift, sample displacement or **non-cubic distortion** (consistent with the lattice distortion indicated by the user).

## Broad humps / suspicious impurities
| Region | Shape | Hypothesis |
|---|---|---|
| 10.3–15.4° | strongly decaying broad hump (net 63→25) | amorphous component / low-angle air scattering; the weak bump at 15.1° may be PBA (111) |
| 28.4–29.5° + 31.3–31.9° | broad cluster | ① amorphous broad hump ② **monoclinic ZrO₂ grinding-media contamination** (m-ZrO₂: 28.2/31.5°) ③ PBA (222)≈30.4° broadened |
| 36.3, 40.1–41.2, 45.2–46.2° | weak broad clusters | pending residual screening (KCl 28.3/40.5? WC? amorphous) |

## Preliminary microstructure assessment
- Apparent Scherrer size (instrumental broadening not subtracted, corrected:false): D≈28.2 nm (200), 27.8 nm (220), 21.7 nm (400) — **nanocrystalline PBA ~25 nm**
- The high-angle data are weak and noisy (maximum 739 counts over the whole pattern): the statistical limit Rexp is expected to be high, which is an objective constraint on the R≤10 target
- Caglioti solved from noisy windows gives U=-1.78 (invalid, recorded only); the peak-shape parameters are re-solved by the refinement engine

## Pending user confirmation (stage 1 gaps)
Manganese precursor species / EDS·ICP·XPS composition and valence states / ball-milling media material

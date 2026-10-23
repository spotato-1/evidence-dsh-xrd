# XRD refinement journal (automatically generated from journal.jsonl, do not edit by hand)

| Round | Engine | Stage | Model | Rwp | Baseline R | Verdict | Why | Artifacts |
|---|---|---|---|---|---|---|---|---|
| 1 | xrd_refine_manual | (explicit vary) | physical | 10.665533212636268 | 10.671348351817096 | R plateau | T7b's free C/N coordinates chemically collapsed (bond-length audit: Fe-C 2.36 mean, C-N 2.28, Fe/Mn-N 1.39/1.41, impossible) => handled structurally by reverting to the literature coordinates (wR 10.58, the honest baseline), and now bond_targets soft constraints (Fe-C 1.90/C-N 1.15/Mn-N 2.12/Fe-N 2.10, anchored on the globally shortest contacts) are used to relax C/N within the chemically legal space (the ball-milling real distortion = CN-bridge-bending hypothesis); warm start from mono_h1 (10.58, occ_K at the bound); dw K=0.0124 takes the T14c value; incidentally correcting the too-short defects of the literature model, Mn-N 1.56/C-N 1.03 | result.json |

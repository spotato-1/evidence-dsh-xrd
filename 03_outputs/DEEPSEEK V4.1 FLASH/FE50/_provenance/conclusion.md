I did as you asked — "start from the template geometry + bond-length restraints throughout" — and **I got halfway; to report honestly: I could not finish this experiment in this round.**

## What was genuinely fixed this round

**Learned from failure and corrected:**

| Problem | Fix | Result |
|---|---|---|
| Atom identifier taken from the wrong place | Switched to the **ranId** at `Atoms[cia+8]` (confirmed at `GSASIImath.py:1032/1045`; in GSASIIscriptable it is taken from `GAtomRecord.cia`, and measured cia=9 ⇒ ranId is at index 17) | ✅ |
| Bond search did not cross symmetry operations | Changed to iterate over `SGData['SGOps']` | ✅ **correctly found 40 bonds** (M–C 12 / M–N 20 / C–N 8) |
| The starting point was an already-broken state | Changed to start from the **template geometry** | ✅ and **verified that the template geometry really is good**: C10–N16 = 1.114 Å, C11–N17 = 1.128 Å, C12–N18 = 1.123 Å, Fe3–N14 = 2.045 Å |

**This is valuable in itself**: the P21/c template you gave is a **chemically acceptable starting point** (C≡N bond lengths correct).

## But the restraints still did not take effect, and I located the root cause

v2 results: wR 25.13 → 23.63 → 16.02 → **16.04**, and after refinement **all 40/40 bonds were off target** (C8–N14 became 0.860 Å, C12–N18 became 0.786 Å).

**Root cause (located)**: `GSASIIstrMath.py:694-701` is

```python
for phase in Phases:
    ...
    if phase not in restraintDict: continue
```

i.e. the restraint dictionary is indexed by **phase NUMBER ('0'/'1')** — **not by phase name**. I installed it under `'built'` (a name) ⇒ **it was silently ignored**.

In v3 I fixed the key (installing it under `'0'`/name/probe keys at once), and **the restraints did work this time** (off target 40/40 → **26/40**), **but the refinement itself collapsed**: it reported `Error: 9 Parameter(s) dropped`, after refinement the cell was **digit-for-digit identical** to the template (indicating the ladder never moved), and the wR 25.51% in the lst is essentially an unrefined state. My phase-key probe was still wrong as well (it picked up `'data'` instead of `'0'`).

## Conclusion: **whether P21/c is more appropriate — still undecided**

Four points already confirmed:

| Experiment | Result | Meaning |
|---|---|---|
| P21/c without restraints | wR 10.36 / 8.60, C–N 0.88–2.56 Å | low R but **chemically invalid** |
| P21/c with C/N coordinates frozen | wR **27.87** | the low R **depends entirely** on the cyano degrees of freedom |
| restraints added afterwards (v1) | no change | the state was already broken, beyond rescue |
| from template + restraints throughout v2 | wR 16.04, 40/40 off target | restraints **did not take effect** (wrong bond names) |
| from template + restraints throughout v3 | wR 25.51, refinement **collapsed** | restraints took effect, but 9 parameters were dropped |

**Note that 16.04 in v2** — with the restraints not taking effect at all (equivalent to a free refinement of the template), P21/c only reached 16.04, which is **worse than the cubic phase's 16.44 on the same ladder? Actually comparable**. This suggests that **P21/c's advantage may have come from overfitting with those 36 degrees of freedom all along**, rather than from monoclinic symmetry itself. But this is still a **suggestion, not a conclusion** — it must wait for an experiment where the restraints really take effect.

## The correct recipe for the next round (I have written the root cause into the log)

1. **First print the real structure of `gpx.data`** to confirm the Phases key names (no more guessing), and install the restraints under the correct **phase number** key
2. **Make the weights gentler** (esd 0.02 may be too strong, causing 9 parameters to be dropped) — suggest esd 0.05–0.10, or restrain only C–N (8 bonds) first and then add more gradually
3. Run the ladder **in steps and report wR step by step**; stop immediately if it collapses, do not run it all at once

## Currently deliverable conclusion (unchanged)

**FE60 = Fm-3m, wR 14.23 % / R 11.02 % / GOF 1.60, the target R ≤ 10 was not achieved.**
`FE60_P21c_final/` and `FE50_P21c_final/` are both **not deliverable** (chemically invalid).
**For FE50 I stopped at "unrestrained P21/c ran to 8.60 and was then falsified"** — I did not repeat the same mistake on it, and will do it together once the correct way to handle P21/c is settled.

Log: `xrd_workflow/journal.jsonl` rounds 42–43 (43 lines total, 0 invalid), script `work/restrained_p21c_v2.py`, logs `work/restrained_v2.log` / `restrained_v3.log`.

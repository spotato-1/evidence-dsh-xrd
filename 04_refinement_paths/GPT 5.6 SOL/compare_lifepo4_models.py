# -*- coding: utf-8 -*-
"""Read-only structural and pattern comparison for the LiFePO4 final GPX files."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np


ROOT = Path(r"D:\AI\codex\workspace")
GSAS_ROOT = ROOT / "DSH" / "dsh-portable" / "gsas"
sys.path.insert(0, str(GSAS_ROOT))
sys.path.insert(0, str(GSAS_ROOT / "GSASII"))

from GSASII import GSASIIscriptable as G2sc  # noqa: E402


PROJECTS = {
    "manual": ROOT / "测试" / "测试集" / "LiFePO4" / "answer" / "精修完成版.bak17.bak0.bak0.gpx",
    "deepseek": ROOT / "DEEPSEEK V4.1 FLASH" / "dsh-xrd-test-evidence" / "runs" / "session-ae4d57b2-f73e-40d2-ad3d-91e64c9602e0" / "artifacts" / "LiFePO4" / "LiFePO4_final" / "LiFePO4_final.gpx",
    "gpt56_baseline": ROOT / "GPT 5.6 SOL" / "dsh-xrd-test-evidence" / "runs" / "session-e03ae580-d18c-423f-806e-9920746a5e8e" / "workspace_snapshot" / "LiFePO4_final_physical_final" / "LiFePO4_final_physical_final.gpx",
    "gpt56_strict": ROOT / "GPT 5.6 SOL" / "dsh-xrd-test-evidence" / "runs" / "session-e03ae580-d18c-423f-806e-9920746a5e8e" / "workspace_snapshot" / "LiFePO4_strict_final" / "LiFePO4_strict_final.gpx",
    "gpt56": ROOT / "GPT 5.6 SOL" / "dsh-xrd-test-evidence" / "runs" / "session-e03ae580-d18c-423f-806e-9920746a5e8e" / "workspace_snapshot" / "LiFePO4_best_physical_final" / "LiFePO4_best_physical_final.gpx",
}


def simple(value):
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    if hasattr(value, "item"):
        try:
            return value.item()
        except Exception:
            pass
    if isinstance(value, (list, tuple)):
        return [simple(item) for item in value]
    if isinstance(value, dict):
        return {str(key): simple(item) for key, item in value.items()}
    return repr(value)


def compare(left, right):
    left = np.asarray(left, dtype=float)
    right = np.asarray(right, dtype=float)
    if left.shape != right.shape:
        return {
            "same_shape": False,
            "left_shape": list(left.shape),
            "right_shape": list(right.shape),
        }
    delta = right - left
    slope, intercept = np.polyfit(left, right, 1)
    transformed_residual = right - (slope * left + intercept)
    return {
        "same_shape": True,
        "n": int(left.size),
        "exact_equal": bool(np.array_equal(left, right)),
        "max_abs_diff": float(np.max(np.abs(delta))),
        "mean_abs_diff": float(np.mean(np.abs(delta))),
        "correlation": float(np.corrcoef(left, right)[0, 1]),
        "right_from_left_slope": float(slope),
        "right_from_left_intercept": float(intercept),
        "rmse_after_linear_transform": float(np.sqrt(np.mean(transformed_residual**2))),
    }


def extract(path):
    project = G2sc.G2Project(gpxfile=str(path))
    hist = project.histograms()[0]
    arrays = hist.data["data"][1]
    metadata = hist.data["data"][0]
    phase_rows = []
    for phase in project.phases():
        general = phase.data.get("General", {})
        histogram_parameters = {}
        for hist_name, values in phase.data.get("Histograms", {}).items():
            histogram_parameters[hist_name] = simple(
                {
                    key: values.get(key)
                    for key in ("Scale", "PhaseFraction", "Size", "Mustrain", "Pref.Ori.")
                    if key in values
                }
            )
        phase_rows.append(
            {
                "name": phase.name,
                "space_group": general.get("SGData", {}).get("SpGrp"),
                "cell": simple(phase.get_cell()),
                "composition_per_cell": simple(phase.composition),
                "density": float(phase.density),
                "atoms": [
                    {
                        "label": atom.label,
                        "element": atom.element,
                        "coordinates": [float(value) for value in atom.coordinates],
                        "occupancy": float(atom.occupancy),
                        "multiplicity": int(atom.mult),
                        "adp_type": atom.adp_flag,
                        "adp": simple(atom.ADP),
                    }
                    for atom in phase.atoms()
                ],
                "histogram_parameters": histogram_parameters,
            }
        )
    return {
        "path": str(path),
        "bytes": path.stat().st_size,
        "histogram": hist.name,
        "residuals": simple(
            {
                key: metadata.get(key)
                for key in ("Nobs", "R", "Rb", "wR", "wRb", "wRmin", "Durbin-Watson")
            }
        ),
        "histogram_model": simple(
            {
                key: hist.data.get(key)
                for key in ("Background", "Instrument Parameters", "Sample Parameters", "Limits")
                if key in hist.data
            }
        ),
        "phases": phase_rows,
        "arrays": [np.asarray(array, dtype=float) for array in arrays[:6]],
    }


def main():
    extracted = {name: extract(path) for name, path in PROJECTS.items()}
    array_fields = ("x", "yobs", "weight", "ycalc", "ybkg", "ydiff")
    comparisons = {}
    for left, right in (
        ("manual", "deepseek"),
        ("manual", "gpt56"),
        ("deepseek", "gpt56_baseline"),
        ("deepseek", "gpt56_strict"),
        ("deepseek", "gpt56"),
        ("gpt56_strict", "gpt56"),
    ):
        comparisons[f"{left}_vs_{right}"] = {
            field: compare(extracted[left]["arrays"][index], extracted[right]["arrays"][index])
            for index, field in enumerate(array_fields)
        }
    for project in extracted.values():
        del project["arrays"]
    output = Path(__file__).with_name("lifepo4_cross_model_gpx.json")
    output.write_text(
        json.dumps(
            {
                "note": "Read-only extraction; source GPX files were not modified.",
                "projects": extracted,
                "comparisons": comparisons,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    print(output)


if __name__ == "__main__":
    main()
